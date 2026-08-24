"""
R3-F Stage 1/2 — adversarial search for a SAFE and INFORMATIVE input outside the six historical
families. Falsification task: try to break our own negative result.

Deterministic objective (NOT noisy BIC):
    J(u) = min_{i != j}  || S_n(mu_i(u) - mu_j(u)) ||_2 / sigma
with sigma set exactly as the benchmark does (SNR-relative to the reference clean response), so J
measures the SHAPE of the input, not its scale.
Hard safety constraint: every mechanism must satisfy min_t x(t) >= A + delta.

Three finite-dimensional families (chief's list):
  pwc(K)      : K piecewise-constant segments,  K = 4, 6, 8
  fourier(H)  : H harmonics, free amplitude/frequency/phase, H = 3..6
  pulses(P)   : P pulses, free centre/width/sign/amplitude, P = 2..4
Search: massive Sobol/LHS scan (parallel) + local Nelder-Mead refinement of the best safe candidates.
"""
import json, os, sys, time, itertools
import numpy as np
from multiprocessing import Pool
from scipy.optimize import minimize
from scipy.stats import qmc
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core, designs, bench

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "artifacts")
os.makedirs(OUT, exist_ok=True)
A_ECO, ALPHA, T, N = 0.25, 0.85, 12.0, 400
DELTA = 0.05                      # required Allee margin
U_CAP = 0.10                      # amplitude budget = the v3 baseline (maximum freedom)
SNR = "med"
CAND = ["ODE", "Caputo", "DDE", "latent3"]
TS = np.linspace(0.0, T, N + 1)
TSAMP = designs.sample_times(T)
COBS = designs.CHANNELS["both"]   # best case for the adversary

# ---------- control families: params in [0,1]^d -> callable u(t_array, T) ----------
def make_pwc(p, K):
    a = (2*p[:K] - 1.0)
    a = a/max(1e-12, np.max(np.abs(a)))
    edges = np.linspace(0, T, K+1)
    def u(ts, TT):
        idx = np.clip(np.searchsorted(edges, ts, side="right")-1, 0, K-1)
        return U_CAP*a[idx]
    return u
def make_fourier(p, H):
    amp = 2*p[0:H]-1.0; frq = 0.05 + p[H:2*H]*2.95; pha = p[2*H:3*H]*2*np.pi
    def u(ts, TT):
        v = sum(amp[h]*np.sin(2*np.pi*frq[h]*ts + pha[h]) for h in range(H))
        m = np.max(np.abs(v)); return U_CAP*v/m if m > 0 else v
    return u
def make_pulses(p, P):
    ctr = p[0:P]*T; wid = 0.05 + p[P:2*P]*1.95; sgn = 2*p[2*P:3*P]-1.0
    def u(ts, TT):
        v = np.zeros_like(ts)
        for q in range(P): v += sgn[q]*np.exp(-0.5*((ts-ctr[q])/wid[q])**2)
        m = np.max(np.abs(v)); return U_CAP*v/m if m > 0 else v
    return u
# picklable dispatch (no lambdas: multiprocessing must be able to pickle the job tuples)
FAMILY_SPEC = ([("pwc%d"%K, K, "pwc", K) for K in (4,6,8)] +
               [("fourier%d"%H, 3*H, "fourier", H) for H in (3,4,5,6)] +
               [("pulses%d"%P, 3*P, "pulses", P) for P in (2,3,4)])
def make_input(kind, order, p):
    if kind == "pwc":     return make_pwc(p, order)
    if kind == "fourier": return make_fourier(p, order)
    if kind == "pulses":  return make_pulses(p, order)
    raise ValueError(kind)

def evaluate(uf):
    """returns (J, min_margin_over_mechanisms, per-mechanism margins) ; J=None if any sim diverges"""
    mus, margins = {}, {}
    for mdl in CAND:
        _, tr = bench.sim_nonlinear(mdl, A_ECO, ALPHA, uf, T, N, amp=U_CAP)
        if bench.diverged(tr): return None, -9.9, {}
        s = bench.safety_metrics(tr, A_ECO)
        margins[mdl] = s["allee_margin"] if s["allee_margin"] is not None else -9.9
        mus[mdl] = (COBS @ bench._sample(TS, tr, TSAMP).T).T.flatten()
    sigma = designs.noise_sigma(mus["Caputo"], designs.SNR_DB[SNR])
    J = min(np.linalg.norm(mus[a]-mus[b])/sigma for a, b in itertools.combinations(CAND, 2))
    return float(J), float(min(margins.values())), {k: float(v) for k, v in margins.items()}

def task(arg):
    fam, kind, order, p = arg
    try:
        J, mm, marg = evaluate(make_input(kind, order, np.asarray(p)))
    except Exception:
        return None
    if J is None: return None
    return {"family": fam, "params": list(map(float, p)), "J": J, "min_margin": mm,
            "safe": bool(mm >= DELTA), "margins": marg}

if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    n_per_family = int(sys.argv[2]) if len(sys.argv) > 2 else 1200
    # ---------- baseline: the six historical designs at the SAME amplitude ----------
    base = {}
    for name in ["pulse","sinusoid","multisine","multiscale","chirp","prbs"]:
        J, mm, marg = evaluate(designs.INPUTS[name])
        base[name] = {"J": J, "min_margin": mm, "safe": bool(mm is not None and mm >= DELTA)}
        print("  baseline %-11s J=%s  min_margin=%+.4f  safe=%s" %
              (name, ("%.3f"%J) if J else "div", mm, base[name]["safe"]), flush=True)
    json.dump(base, open(os.path.join(OUT, "r3f_baseline.json"), "w"), indent=1)
    # ---------- Stage 1: Sobol scan over all families ----------
    jobs = []
    for fam, dim, kind, order in FAMILY_SPEC:
        s = qmc.Sobol(d=dim, scramble=True, seed=12345)
        P = s.random(n_per_family)
        jobs += [(fam, kind, order, p) for p in P]
    print("Stage 1: %d evaluations over %d families, workers=%d" % (len(jobs), len(FAMILY_SPEC), workers), flush=True)
    t0 = time.time(); res = []
    with Pool(workers) as pool:
        for i, r in enumerate(pool.imap_unordered(task, jobs, chunksize=4)):
            if r: res.append(r)
            if i % 2000 == 0: print("  %d/%d (%.0fs)" % (i, len(jobs), time.time()-t0), flush=True)
    json.dump(res, open(os.path.join(OUT, "r3f_stage1.json"), "w"))
    safe = [r for r in res if r["safe"]]
    print("Stage 1 done: %d valid, %d SAFE (margin>=%.2f)" % (len(res), len(safe), DELTA), flush=True)
    if safe:
        best = max(safe, key=lambda r: r["J"])
        print("  best SAFE J=%.3f (family %s)" % (best["J"], best["family"]), flush=True)
    # ---------- Stage 1b: local refinement of the best safe candidates per family ----------
    ref = []
    for fam, dim, kind, order in FAMILY_SPEC:
        cand = sorted([r for r in safe if r["family"] == fam], key=lambda r: -r["J"])[:3]
        for c in cand:
            def neg(p, kind=kind, order=order):
                pp = np.clip(p, 0, 1)
                J, mm, _ = evaluate(make_input(kind, order, pp))
                if J is None or mm < DELTA: return 1e3       # infeasible
                return -J
            r = minimize(neg, np.array(c["params"]), method="Nelder-Mead",
                         options={"maxiter": 220, "xatol": 1e-3, "fatol": 1e-4})
            pp = np.clip(r.x, 0, 1); J, mm, marg = evaluate(make_input(kind, order, pp))
            if J is not None and mm >= DELTA:
                ref.append({"family": fam, "params": list(map(float, pp)), "J": J,
                            "min_margin": mm, "safe": True, "margins": marg, "refined": True})
    json.dump(ref, open(os.path.join(OUT, "r3f_refined.json"), "w"), indent=1)
    allsafe = safe + ref
    out = {"U_cap": U_CAP, "delta": DELTA, "alpha": ALPHA, "T": T, "n_eval": len(res),
           "n_safe": len(safe), "baseline": base,
           "best_safe": (max(allsafe, key=lambda r: r["J"]) if allsafe else None),
           "best_overall": (max(res, key=lambda r: r["J"]) if res else None),
           "per_family_best_safe": {}}
    for fam, dim, kind, order in FAMILY_SPEC:
        f = [r for r in allsafe if r["family"] == fam]
        if f: out["per_family_best_safe"][fam] = max(f, key=lambda r: r["J"])
    json.dump(out, open(os.path.join(OUT, "r3f_summary.json"), "w"), indent=1)
    print("DONE  best_safe_J=%s  best_overall_J=%.3f" %
          (("%.3f" % out["best_safe"]["J"]) if out["best_safe"] else "NONE",
           out["best_overall"]["J"]), flush=True)
