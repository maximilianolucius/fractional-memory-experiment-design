"""
benchmark_safe_v4 (Task R2-F) — amplitude-stratified re-run. FROZEN v3 IS NOT TOUCHED.
Stage-A amplitudes: 0.050, 0.063 (= U(0.05) linear certificate), 0.100 (v3 baseline, comparable).
Same designs, same channels, same SNRs, same sampling, same scoring, same seeds as v3.
Per-cell safety instrumentation: Allee margin, crossing flag, realized |u|_inf gain.
NOTE: the 0.050/0.063 runs are LINEAR-CERTIFICATE DIAGNOSTICS, not a nonlinear-safe benchmark,
until U_NL(delta) is established (chief instruction).
"""
import json, os, sys, itertools, time
import numpy as np
from multiprocessing import Pool
from scipy.optimize import minimize_scalar
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core, designs, bench

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "artifacts")
os.makedirs(OUT, exist_ok=True)
STATE = os.path.join(OUT, "state_v4.jsonl")
CAND = ["ODE", "Caputo", "DDE", "latent3"]
AMPS = [float(x) for x in os.environ.get("FMED_AMPS", "0.050,0.063,0.100").split(",")]
ALL_AMPS = [0.050, 0.063, 0.100]        # for aggregation across machines
STABLE_A = [0.20, 0.25]
INPUTS = ["pulse", "sinusoid", "multisine", "multiscale", "chirp", "prbs"]

def _true_class(m): return "latent3" if m in ("latent1", "latent3") else m

def fit_candidate(model, data, A, uf, T, N, C, tsamp, amp):
    def sse_of(param):
        kw = {}
        if model == "Caputo": kw["alpha"] = param
        elif model == "DDE": kw["tau"] = param
        elif model == "latent3": kw["lam"] = (param, param*1.6, param*0.6)
        _, tr = bench.sim_nonlinear(model, A, kw.get("alpha", 0.9), uf, T, N,
                                    tau=kw.get("tau", bench.DDE_TAU),
                                    lam=kw.get("lam", bench.LAT_RATES), amp=amp)
        mu = (C @ bench._sample(np.linspace(0, T, N+1), tr, tsamp).T).T.flatten()
        if not np.all(np.isfinite(mu)): return np.inf
        return float(np.sum((data - mu)**2))
    if model == "ODE": return sse_of(None), 0
    bnd = {"Caputo": (0.55, 0.999), "DDE": (0.05, 0.8), "latent3": (0.2, 3.0)}[model]
    r = minimize_scalar(sse_of, bounds=bnd, method="bounded",
                        options={"xatol": 2e-2, "maxiter": 20})
    return float(r.fun), 1

def work_cell(cell):
    true_m, A, alpha, inp, obs, snr, amp, reps, N, seed0 = cell
    T = designs.HORIZON["med"]; tsamp = designs.sample_times(T)
    C = designs.CHANNELS[obs]; uf = designs.INPUTS[inp]
    tsf, tr = bench.sim_nonlinear(true_m, A, alpha, uf, T, N, amp=amp)
    base = {"true": true_m, "A": A, "alpha": alpha, "input": inp, "obs": obs,
            "snr": snr, "amp": amp}
    safety = bench.safety_metrics(tr, A)
    # realized sup-norm gain: ||xi||_inf / ||u||_inf  (empirical Gamma for THIS design)
    xs, ys = core.x_star(), core.y_star(A)
    fin = np.isfinite(tr[:, 0])
    realized_gain = float(np.max(np.abs(tr[fin] - np.array([xs, ys])))/amp) if fin.any() else None
    if bench.diverged(tr):
        return {**base, "diverged": True, "reps": 0, "selected": {c: 0 for c in CAND},
                "accuracy": None, "safety": safety, "realized_gain": realized_gain}
    clean = (C @ bench._sample(tsf, tr, tsamp).T).T.flatten()
    sigma = designs.noise_sigma(clean, designs.SNR_DB[snr])
    conf = {c: 0 for c in CAND}; correct = 0
    for r in range(reps):
        rng = np.random.default_rng(seed0 + r)          # SAME seeds as v3
        data = clean + rng.normal(0, sigma, clean.shape)
        bics = []
        for c in CAND:
            sse, k = fit_candidate(c, data, A, uf, T, N, C, tsamp, amp)
            n = data.size
            if not np.isfinite(sse): bics.append(np.inf); continue
            ll = -0.5*n*np.log(2*np.pi*sigma**2) - 0.5*sse/sigma**2
            bics.append(k*np.log(n) - 2*ll)
        b = np.asarray(bics, float)
        if not np.any(np.isfinite(b)): continue
        b[~np.isfinite(b)] = np.inf
        sel = CAND[int(np.argmin(b))]; conf[sel] += 1
        if sel == _true_class(true_m): correct += 1
    used = sum(conf.values())
    return {**base, "diverged": False, "reps": used, "selected": conf,
            "accuracy": (correct/used) if used else None, "safety": safety,
            "realized_gain": realized_gain, "sigma": float(sigma)}

if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    reps = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    N = 400
    cells = []; k = 0
    for amp in AMPS:
        for tm in designs.TRUE_MODELS:
            for A in STABLE_A:
                for inp in INPUTS:
                    for obs in ["prey", "pred", "both"]:
                        for snr in list(designs.SNR_DB):
                            for a in (designs.ALPHA_GRID if tm == "Caputo" else [0.90]):
                                cells.append((tm, A, a, inp, obs, snr, amp, reps, N,
                                              1000 + 7919*k + int(a*100))); k += 1
    key = lambda d: (d["true"], d["A"], d["alpha"], d["input"], d["obs"], d["snr"], d["amp"])
    done = set()
    if os.path.exists(STATE):
        for l in open(STATE):
            try: done.add(key(json.loads(l)))
            except Exception: pass
    todo = [c for c in cells if (c[0],c[1],c[2],c[3],c[4],c[5],c[6]) not in done]
    print(f"v4: {len(cells)} cells ({len(AMPS)} amplitudes), {len(todo)} to run, workers={workers}", flush=True)
    t0 = time.time()
    if todo:
        with Pool(workers) as p:
            for i, r in enumerate(p.imap_unordered(work_cell, todo, chunksize=2)):
                with open(STATE, "a") as f: f.write(json.dumps(r, default=float)+"\n")
                if i % 100 == 0: print(f"  {i}/{len(todo)} ({time.time()-t0:.0f}s)", flush=True)
    rows = [json.loads(l) for l in open(STATE)]
    out = {"n_cells": len(rows), "amplitudes": ALL_AMPS, "this_shard": AMPS, "reps_per_cell": reps, "N": N, "by_amp": {}}
    for amp in ALL_AMPS:
        sub = [d for d in rows if abs(d["amp"]-amp) < 1e-9 and not d.get("diverged") and d.get("accuracy") is not None]
        if not sub: continue
        conf4 = {t: {c: 0 for c in CAND} for t in set(_true_class(m) for m in designs.TRUE_MODELS)}
        tot = cor = 0
        for d in sub:
            u = sum(d["selected"].values()); tot += u
            cor += d["selected"].get(_true_class(d["true"]), 0)
            for c in CAND: conf4[_true_class(d["true"])][c] += d["selected"][c]
        recall = {c: (conf4[c][c]/sum(conf4[c].values()) if sum(conf4[c].values()) else None) for c in CAND}
        byin = {}
        for d in sub:
            u = sum(d["selected"].values())
            byin.setdefault(d["input"], [0,0])
            byin[d["input"]][0] += d["selected"].get(_true_class(d["true"]),0); byin[d["input"]][1] += u
        saf = {}
        for d in [x for x in rows if abs(x["amp"]-amp)<1e-9]:
            s = d.get("safety") or {}
            e = saf.setdefault(d["input"], {"n":0,"crossed":0,"min_margin":None,"max_gain":None})
            e["n"] += 1; e["crossed"] += 1 if s.get("allee_crossed") else 0
            if s.get("allee_margin") is not None:
                e["min_margin"] = s["allee_margin"] if e["min_margin"] is None else min(e["min_margin"], s["allee_margin"])
            if d.get("realized_gain") is not None:
                e["max_gain"] = d["realized_gain"] if e["max_gain"] is None else max(e["max_gain"], d["realized_gain"])
        for e in saf.values(): e["cross_rate"] = e["crossed"]/e["n"] if e["n"] else None
        out["by_amp"][str(amp)] = {
            "n_good": len(sub), "micro_accuracy": cor/tot if tot else None,
            "macro_accuracy": float(np.mean([r for r in recall.values() if r is not None])),
            "per_class_recall": recall,
            "design_ranking": dict(sorted({k2:(v[0]/v[1] if v[1] else 0) for k2,v in byin.items()}.items(), key=lambda kv:-kv[1])),
            "confusion_4class": conf4, "safety": saf,
            "n_diverged": sum(1 for x in rows if abs(x["amp"]-amp)<1e-9 and x.get("diverged"))}
    json.dump(out, open(os.path.join(OUT, "v4_safe_benchmark.json"), "w"), indent=1)
    for a in ALL_AMPS:
        s = out["by_amp"].get(str(a))
        if s: print("  amp=%.3f  macro=%.4f micro=%.4f best=%s diverged=%d" %
                    (a, s["macro_accuracy"], s["micro_accuracy"], next(iter(s["design_ranking"])), s["n_diverged"]), flush=True)
    print("DONE", flush=True)
