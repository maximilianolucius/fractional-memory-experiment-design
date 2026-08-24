"""
C-1 — Theorem B complexity law: best L1(0,T) approximation of the Caputo kernel
k_alpha(t) = t^(alpha-1)/Gamma(alpha) by a POSITIVE m-term exponential sum.

Exact diffusive representation (source_pack/07, T7):
    k_alpha(t) = (sin(pi*alpha)/pi) * Integral_0^inf lambda^(-alpha) e^(-lambda t) dlambda
Substituting lambda = e^s makes the integrand doubly-exponentially decaying and analytic,
so the trapezoidal rule in s converges geometrically -> candidate law eps ~ A exp(-c*m^beta).

For each (alpha, T, m): optimize the truncation window [s_min, s_max] (grid + local refine),
then optionally refine weights by non-negative least squares. Report the achieved
E(m) = || k_alpha - k_m ||_{L1(0,T)}.
Fully parallel: one task per (alpha, T, m).
"""
import json, os, sys, itertools, time
import numpy as np
from math import gamma, sin, pi
from multiprocessing import Pool

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
os.makedirs(OUT, exist_ok=True)

def t_grid(T, n=24000, tmin_rel=1e-13):
    """log-graded grid on (0,T]: resolves the t->0 singularity; L1 integrable."""
    tmin = T * tmin_rel
    return np.geomspace(tmin, T, n)

def k_exact(t, alpha):
    return t ** (alpha - 1.0) / gamma(alpha)

def k_sum(t, alpha, s):
    """positive exponential sum from trapezoid nodes s (lambda=e^s)."""
    h = s[1] - s[0] if len(s) > 1 else 1.0
    c = (sin(pi * alpha) / pi) * h * np.exp((1.0 - alpha) * s)   # weights > 0
    lam = np.exp(s)
    return (c[None, :] * np.exp(-lam[None, :] * t[:, None])).sum(axis=1)

def L1err(t, ke, ks):
    """integral |ke-ks| dt on the log grid (trapezoid in t)."""
    return float(np.trapezoid(np.abs(ke - ks), t)) if hasattr(np, "trapezoid") \
        else float(np.trapz(np.abs(ke - ks), t))

def err_for_window(t, ke, alpha, smin, smax, m):
    s = np.linspace(smin, smax, m)
    return L1err(t, ke, k_sum(t, alpha, s))

def best_window(alpha, T, m, t, ke):
    """coarse grid then local refinement over (smin, smax)."""
    best = (np.inf, None, None)
    lo_c = np.linspace(np.log(1e-6 / T), np.log(5.0 / T), 9)
    hi_c = np.linspace(np.log(1.0 / T), np.log(1e9 / T), 11)
    for smin in lo_c:
        for smax in hi_c:
            if smax <= smin: continue
            e = err_for_window(t, ke, alpha, smin, smax, m)
            if e < best[0]: best = (e, smin, smax)
    e, smin, smax = best
    for _ in range(60):                      # coordinate refine
        improved = False
        for d in (0.5, 0.15, 0.05):
            for ds, de in ((d,0),(-d,0),(0,d),(0,-d)):
                a, b = smin + ds, smax + de
                if b <= a: continue
                e2 = err_for_window(t, ke, alpha, a, b, m)
                if e2 < e - 1e-15:
                    e, smin, smax, improved = e2, a, b, True
        if not improved: break
    return e, smin, smax

def nnls_refine(alpha, T, m, t, ke, smin, smax):
    """refine weights by non-negative least squares on the log grid (keeps positivity)."""
    try:
        from scipy.optimize import nnls
    except Exception:
        return None
    s = np.linspace(smin, smax, m); lam = np.exp(s)
    B = np.exp(-lam[None, :] * t[:, None])
    w = np.sqrt(np.gradient(t))                      # weight ~ measure, for L1 proxy
    try:                                             # ill-conditioned exponential basis:
        c, _ = nnls(B * w[:, None], ke * w, maxiter=20 * m + 200)
    except Exception:
        return None                                  # keep the quadrature result instead
    return L1err(t, ke, (c[None, :] * B).sum(axis=1)), c

def task(args):
    alpha, T, m = args
    t = t_grid(T); ke = k_exact(t, alpha)
    e, smin, smax = best_window(alpha, T, m, t, ke)
    rel = e / (T ** alpha / (alpha * gamma(alpha)))   # relative to ||k_alpha||_{L1(0,T)}
    out = {"alpha": alpha, "T": T, "m": m, "L1_err": e, "L1_rel": rel,
           "smin": smin, "smax": smax}
    try:
        r = nnls_refine(alpha, T, m, t, ke, smin, smax)
    except Exception:
        r = None
    if r is not None:
        out["L1_err_nnls"] = r[0]
        out["L1_rel_nnls"] = r[0] / (T ** alpha / (alpha * gamma(alpha)))
    return out

if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 280
    alphas = [0.30, 0.50, 0.70, 0.85, 0.95]
    Ts = [1.0, 10.0, 100.0]
    ms = [2,3,4,6,8,10,12,16,20,24,28,32,40,48,56,64,80,96,128]
    tasks = list(itertools.product(alphas, Ts, ms))
    print(f"C-1: {len(tasks)} cells, workers={workers}", flush=True)
    t0 = time.time(); res = []
    with Pool(workers) as p:
        for i, r in enumerate(p.imap_unordered(task, tasks, chunksize=1)):
            res.append(r)
            if i % 25 == 0: print(f"  {i}/{len(tasks)} ({time.time()-t0:.0f}s)", flush=True)
    json.dump(res, open(os.path.join(OUT, "c1_complexity_law.json"), "w"), indent=1)
    # fit laws per (alpha,T):  log eps = a - c*m^beta   for beta in {1, 1/2, 1/3}
    fits = []
    for alpha in alphas:
        for T in Ts:
            sub = sorted([r for r in res if r["alpha"]==alpha and r["T"]==T], key=lambda r: r["m"])
            m = np.array([r["m"] for r in sub], float)
            e = np.array([min(r["L1_rel"], r.get("L1_rel_nnls", np.inf)) for r in sub], float)
            ok = (e > 0) & np.isfinite(e)
            if ok.sum() < 5: continue
            best = None
            for beta in (1.0, 0.5, 1/3):
                A = np.vstack([np.ones(ok.sum()), -(m[ok] ** beta)]).T
                coef, res_, *_ = np.linalg.lstsq(A, np.log(e[ok]), rcond=None)
                r2 = 1 - (res_[0] if len(res_) else 0) / max(1e-30, ((np.log(e[ok]) - np.log(e[ok]).mean())**2).sum())
                if best is None or r2 > best["r2"]:
                    best = {"beta": beta, "logA": float(coef[0]), "c": float(coef[1]), "r2": float(r2)}
            fits.append({"alpha": alpha, "T": T, **best,
                         "eps_at_m64": float(e[m==64][0]) if (m==64).any() else None})
    json.dump(fits, open(os.path.join(OUT, "c1_fits.json"), "w"), indent=1)
    print("DONE", json.dumps(fits[:3]), flush=True)
