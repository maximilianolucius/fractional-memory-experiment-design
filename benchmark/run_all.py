"""
run_all.py — full benchmark driver for fractional-memory-experiment-design.
Phases: (1) analytic gates, (2) Caputo PECE vs Mittag-Leffler solver validation,
(3) FULL-factorial linear-Gaussian discrimination (exact), (4) nonlinear Monte-Carlo
confirmation over a factorial grid x replicates (parallel), (5) manifest.
JSONL resume for phases (state_v.jsonl) and per-cell for the nonlinear sweep.

Run:  ~/fmi_venv/bin/python run_all.py --workers 300 --reps 200
"""
import os, sys, json, time, argparse, itertools, hashlib
import numpy as np
from multiprocessing import Pool
from scipy.optimize import minimize_scalar
import core, designs, bench

ART = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "artifacts")
os.makedirs(ART, exist_ok=True)
STATE = os.path.join(ART, "state_v.jsonl")
NLSTATE = os.path.join(ART, "state_nl.jsonl")

def jdump(name, obj):
    with open(os.path.join(ART, name), "w") as f: json.dump(obj, f, indent=2, default=float)
def done_stage(tag):
    return os.path.exists(STATE) and any(json.loads(l).get("stage") == tag for l in open(STATE))
def mark_stage(tag, extra=None):
    with open(STATE, "a") as f: f.write(json.dumps({"stage": tag, "t": time.time(), **(extra or {})}) + "\n")

# ------------------------------------------------------------------ (1) analytic gates
def phase_gates():
    g = {}
    g["x_star"] = core.x_star()
    g["x_star_ok"] = abs(core.x_star() - 2.0 / 3.0) < 1e-12
    for A in designs.A_GRID:
        T, D = core.trace_det(A)
        g[f"A={A}"] = {"y_star": core.y_star(A), "T": T, "D": D,
                       "T_exact": (7 * A - 2) / (8 * A), "D_exact": (2 - 3 * A) / (20 * A),
                       "alpha_star": core.alpha_star(A), **core.ctrb_obsv_ranks(A)}
    a03 = core.alpha_star(0.30)
    g["alpha_star_0.30"] = a03
    g["alpha_star_0.30_ref"] = 0.9690122761517084
    g["alpha_star_0.30_ok"] = (a03 is not None) and abs(a03 - 0.9690122761517084) < 1e-12
    g["ranks_full"] = all(core.ctrb_obsv_ranks(A)[k] == 2 for A in designs.A_GRID
                          for k in ("ctrb_prey", "ctrb_pred", "obsv_prey", "obsv_pred"))
    g["PASS"] = bool(g["x_star_ok"] and g["alpha_star_0.30_ok"] and g["ranks_full"])
    jdump("gates.json", g); return g

# ------------------------------------------------------------------ (2) solver validation vs Mittag-Leffler
def phase_solver():
    lam, alpha = -0.7, 0.85
    res = {}
    for N in (250, 500, 1000):
        ts = np.linspace(0.0, 8.0, N + 1)
        g = lambda t, z: np.array([lam * z[0]])
        num = core.caputo_pece(g, np.array([1.0]), 8.0, N, alpha)[:, 0]
        ref = core.ml_reference_scalar(lam, ts, alpha)
        res[f"N={N}"] = {"max_abs_err": float(np.max(np.abs(num - ref)))}
    errs = [res[f"N={N}"]["max_abs_err"] for N in (250, 500, 1000)]
    res["converges"] = bool(errs[0] > errs[1] > errs[2])
    res["final_err"] = errs[-1]
    res["PASS"] = bool(res["converges"] and errs[-1] < 5e-3)
    jdump("solver_validation.json", res); return res

# ------------------------------------------------------------------ (3) FULL-factorial linear-Gaussian discrimination
CAND = ["ODE", "Caputo", "DDE", "latent3"]   # candidate mechanism classes
def _true_class(m): return "latent3" if m in ("latent1", "latent3") else m

def phase_linear():
    N = 800
    rows = []
    design_score = {}   # input -> list of min-pairwise-KL across cells
    for A, alpha, inp, obs, snr, hz in itertools.product(
            designs.A_GRID, designs.ALPHA_GRID, list(designs.INPUTS),
            list(designs.CHANNELS), list(designs.SNR_DB), list(designs.HORIZON)):
        T = designs.HORIZON[hz]; tsamp = designs.sample_times(T)
        C = designs.CHANNELS[obs]; uf = designs.INPUTS[inp]
        mus = {m: bench.lin_response(m, A, alpha, uf, T, N, C, tsamp) for m in CAND}
        ref = mus["ODE"].flatten()
        sigma = designs.noise_sigma(ref if np.any(ref) else np.ones(1), designs.SNR_DB[snr])
        kls = []
        for i in range(len(CAND)):
            for j in range(i + 1, len(CAND)):
                Pe, KL = bench.pairwise_error(mus[CAND[i]].flatten(), mus[CAND[j]].flatten(), sigma)
                kls.append(KL)
        minkl = float(min(kls))
        rows.append({"A": A, "alpha": alpha, "input": inp, "obs": obs, "snr": snr,
                     "hz": hz, "min_pairwise_KL": minkl, "mean_pairwise_KL": float(np.mean(kls))})
        design_score.setdefault(inp, []).append(minkl)
    ranking = {k: float(np.mean(v)) for k, v in design_score.items()}
    ranking = dict(sorted(ranking.items(), key=lambda kv: -kv[1]))
    out = {"n_cells": len(rows), "design_ranking_by_mean_min_pairwise_KL": ranking, "rows": rows}
    jdump("linear_factorial.json", out); return out

# ------------------------------------------------------------------ (4) nonlinear Monte-Carlo confirmation (parallel)
def _fit_sse(model, data, A, uf, T, N, C, tsamp, param):
    kw = {}
    if model == "Caputo": kw["alpha"] = param
    elif model == "DDE": kw["tau"] = param
    elif model == "latent3": kw["lam"] = (param, param * 1.6, param * 0.6)
    _, tr = bench.sim_nonlinear(model, A, kw.get("alpha", 0.9), uf, T, N,
                                tau=kw.get("tau", bench.DDE_TAU), lam=kw.get("lam", bench.LAT_RATES))
    mu = (C @ bench._sample(np.linspace(0, T, N + 1), tr, tsamp).T).T.flatten()
    if not np.all(np.isfinite(mu)): return np.inf, mu
    return float(np.sum((data - mu) ** 2)), mu

def _fit_candidate(model, data, A, uf, T, N, C, tsamp):
    if model == "ODE":
        sse, mu = _fit_sse(model, data, A, uf, T, N, C, tsamp, None); return sse, 0
    bnd = {"Caputo": (0.55, 0.999), "DDE": (0.05, 0.8), "latent3": (0.2, 3.0)}[model]
    r = minimize_scalar(lambda p: _fit_sse(model, data, A, uf, T, N, C, tsamp, p)[0],
                        bounds=bnd, method="bounded", options={"xatol": 2e-2, "maxiter": 20})
    return float(r.fun), 1

def work_cell(cell):
    (true_m, A, alpha, inp, obs, snr, regime, reps, N, seed0) = cell
    T = designs.HORIZON["med"]; tsamp = designs.sample_times(T)
    C = designs.CHANNELS[obs]; uf = designs.INPUTS[inp]
    tsf, tr = bench.sim_nonlinear(true_m, A, alpha, uf, T, N)
    base = {"true": true_m, "A": A, "alpha": alpha, "input": inp, "obs": obs, "snr": snr, "regime": regime}
    safety = bench.safety_metrics(tr, A)
    if bench.diverged(tr):
        return {**base, "diverged": True, "reps": 0, "selected": {c: 0 for c in CAND}, "accuracy": None, "safety": safety}
    clean = (C @ bench._sample(tsf, tr, tsamp).T).T.flatten()
    sigma = designs.noise_sigma(clean, designs.SNR_DB[snr])
    conf = {c: 0 for c in CAND}; correct = 0
    for r in range(reps):
        rng = np.random.default_rng(seed0 + r)
        data = clean + rng.normal(0, sigma, clean.shape)
        bics = []
        for c in CAND:
            sse, k = _fit_candidate(c, data, A, uf, T, N, C, tsamp)
            n = data.size
            if not np.isfinite(sse):
                bics.append(np.inf); continue
            ll = -0.5 * n * np.log(2 * np.pi * sigma**2) - 0.5 * sse / sigma**2
            bics.append(k * np.log(n) - 2 * ll)
        bics = np.asarray(bics, float)
        if not np.any(np.isfinite(bics)):
            continue
        bics[~np.isfinite(bics)] = np.inf
        sel = CAND[int(np.argmin(bics))]; conf[sel] += 1
        if sel == _true_class(true_m): correct += 1
    used = sum(conf.values())
    return {**base, "diverged": False, "reps": used, "selected": conf,
            "accuracy": (correct / used) if used else None, "safety": safety}

STABLE_A = [0.20, 0.25]           # ODE stable, comfortable margin below 2/7=0.2857 (audit P0.6)
VERDICT_A = [0.30, 0.40]          # A > 2/7: stability-verdict stress-test (reported separately)
INPUTS_NL = ["pulse", "sinusoid", "multisine", "multiscale", "chirp", "prbs"]

def phase_nonlinear(workers, reps, N):
    cells = []; k = 0
    for regime, Aset in (("stable", STABLE_A), ("verdict", VERDICT_A)):
        for tm in designs.TRUE_MODELS:
            for A in Aset:
                for inp in INPUTS_NL:
                    for obs in ["prey", "pred", "both"]:
                        for snr in list(designs.SNR_DB):
                            for a in (designs.ALPHA_GRID if tm == "Caputo" else [0.90]):
                                cells.append((tm, A, a, inp, obs, snr, regime, reps, N, 1000 + 7919 * k + int(a * 100)))
                                k += 1
    key = lambda d: (d["true"], d["A"], d["alpha"], d["input"], d["obs"], d["snr"], d.get("regime"))
    done = set()
    if os.path.exists(NLSTATE):
        for l in open(NLSTATE):
            try: done.add(key(json.loads(l)))
            except Exception: pass
    todo = [c for c in cells if (c[0], c[1], c[2], c[3], c[4], c[5], c[6]) not in done]
    print(f"nonlinear: {len(cells)} cells, {len(todo)} to run, workers={workers}", flush=True)
    t0 = time.time()
    if todo:
        with Pool(workers) as pool:
            for i, res in enumerate(pool.imap_unordered(work_cell, todo, chunksize=4)):
                with open(NLSTATE, "a") as f: f.write(json.dumps(res, default=float) + "\n")
                if i % 100 == 0: print(f"  {i}/{len(todo)} ({time.time()-t0:.0f}s)", flush=True)
    rows = [json.loads(l) for l in open(NLSTATE)]

    def agg(sub):
        good = [d for d in sub if not d.get("diverged") and d.get("accuracy") is not None]
        if not good: return None
        conf5 = {t: {c: 0 for c in CAND} for t in designs.TRUE_MODELS}
        conf4 = {t: {c: 0 for c in CAND} for t in set(_true_class(m) for m in designs.TRUE_MODELS)}
        tot = cor = 0
        for d in good:
            u = sum(d["selected"].values()); tot += u; cor += d["selected"].get(_true_class(d["true"]), 0)
            for c in CAND:
                conf5[d["true"]][c] += d["selected"][c]; conf4[_true_class(d["true"])][c] += d["selected"][c]
        recall = {c: (conf4[c][c] / sum(conf4[c].values())) if sum(conf4[c].values()) else None for c in CAND}
        precision = {c: (conf4[c][c] / sum(conf4[t][c] for t in conf4)) if sum(conf4[t][c] for t in conf4) else None for c in CAND}
        macro = float(np.mean([r for r in recall.values() if r is not None]))
        byin = {}
        for d in good:
            u = sum(d["selected"].values())
            byin.setdefault(d["input"], [0, 0]); byin[d["input"]][0] += d["selected"].get(_true_class(d["true"]), 0); byin[d["input"]][1] += u
        rank = dict(sorted({kk: (v[0] / v[1] if v[1] else 0) for kk, v in byin.items()}.items(), key=lambda kv: -kv[1]))
        return {"n_good": len(good), "micro_accuracy": cor / tot if tot else None, "macro_accuracy": macro,
                "per_class_recall": recall, "per_class_precision": precision, "design_ranking": rank,
                "confusion_5class": conf5, "confusion_4class": conf4}

    def strat(sub, field):
        o = {}
        for d in sub:
            if d.get("diverged") or d.get("accuracy") is None: continue
            kk = str(d["A"] if field == "A" else d.get(field))
            o.setdefault(kk, [0, 0]); o[kk][0] += d["selected"].get(_true_class(d["true"]), 0); o[kk][1] += sum(d["selected"].values())
        return {kk: (v[0] / v[1] if v[1] else 0) for kk, v in o.items()}

    def safety_agg(sub):
        o = {}
        for d in sub:
            s = d.get("safety") or {}; e = o.setdefault(d["input"], {"n": 0, "crossed": 0, "min_allee_margin": None, "min_face_dist": None})
            e["n"] += 1; e["crossed"] += 1 if s.get("allee_crossed") else 0
            for fld, kk in (("allee_margin", "min_allee_margin"), ("face_dist", "min_face_dist")):
                if s.get(fld) is not None: e[kk] = s[fld] if e[kk] is None else min(e[kk], s[fld])
        for e in o.values(): e["allee_cross_rate"] = e["crossed"] / e["n"] if e["n"] else None
        return o

    stable = [d for d in rows if d.get("regime") == "stable"]; verdict = [d for d in rows if d.get("regime") == "verdict"]
    out = {"n_cells": len(rows), "reps_per_cell": reps, "N_solver": N,
           "n_diverged": sum(1 for d in rows if d.get("diverged")),
           "stable": agg(stable), "verdict": agg(verdict),
           "stable_stratified": {"by_A": strat(stable, "A"), "by_alpha": strat(stable, "alpha"),
                                 "by_snr": strat(stable, "snr"), "by_channel": strat(stable, "obs")},
           "safety_stable": safety_agg(stable), "safety_verdict": safety_agg(verdict)}
    jdump("nonlinear_confusion.json", out); return out

# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=300)
    ap.add_argument("--reps", type=int, default=200)
    ap.add_argument("--N", type=int, default=500)
    args = ap.parse_args()
    t0 = time.time()
    if not done_stage("gates"): g = phase_gates(); mark_stage("gates", {"PASS": g["PASS"]}); print("gates", g["PASS"], flush=True)
    if not done_stage("solver"): s = phase_solver(); mark_stage("solver", {"PASS": s["PASS"]}); print("solver", s["PASS"], flush=True)
    if not done_stage("linear"): L = phase_linear(); mark_stage("linear", {"n": L["n_cells"]}); print("linear cells", L["n_cells"], flush=True)
    NL = phase_nonlinear(args.workers, args.reps, args.N)
    mark_stage("nonlinear", {"stable_macro": (NL.get("stable") or {}).get("macro_accuracy")})
    # manifest
    gj = json.load(open(os.path.join(ART, "gates.json")))
    sj = json.load(open(os.path.join(ART, "solver_validation.json")))
    status = "PASS" if (gj["PASS"] and sj["PASS"]) else "PENDING-VERIFICATION"
    st = NL.get("stable") or {}; vd = NL.get("verdict") or {}
    manifest = {
        "git_commit": os.environ.get("FMED_GIT", "orion-run"),
        "seed": 1000, "solver": "caputo_pece_abm",
        "solver_tolerances": {"tol": sj["final_err"], "mittag_leffler_validated": sj["PASS"]},
        "design": {"decision_rule": "BIC (information-criterion; NOT full Bayesian evidence)",
                   "reps_per_cell": args.reps, "N": args.N,
                   "stable_A": STABLE_A, "verdict_A": VERDICT_A, "inputs": INPUTS_NL},
        "primary_task": "memory-shape discrimination, stable-only A<2/7 (audit P0.6)",
        "objective_name": "stable-only macro-averaged model-selection accuracy",
        "objective_estimate": st.get("macro_accuracy"), "stable_micro_accuracy": st.get("micro_accuracy"),
        "best_design_stable": next(iter(st.get("design_ranking", {})), None),
        "verdict_macro_accuracy": vd.get("macro_accuracy"),
        "n_diverged": NL.get("n_diverged"),
        "gates_PASS": gj["PASS"], "solver_PASS": sj["PASS"],
        "status": status, "wall_seconds": time.time() - t0,
    }
    jdump("manifest_orion.json", manifest)
    print("DONE", json.dumps(manifest, default=float), flush=True)

if __name__ == "__main__":
    main()
