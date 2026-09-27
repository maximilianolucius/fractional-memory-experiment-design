"""Empirically parameterized case study: boreal vole--weasel system.

Anchors (literature): Turchin & Hanski (1997) vole-weasel parameterization --
prey K = 150 voles/ha, Holling-II specialist response with maximum consumption
Q = 600 voles/yr/weasel and half-saturation D0 = 6 voles/ha, weasel demography
of order 1/yr. Mapping decisions (declared in the manuscript): the net prey
growth coefficient r = 1.0/yr absorbs generalist predation (the G-term of T&H);
the strong-Allee threshold A = 37.5 voles/ha is a SCENARIO value replicating the
benchmark's relative geometry (A/K = 1/4, x*/K = 2/3); weasel efficiency e is
set so the coexistence equilibrium sits at x* = 100 voles/ha; the fractional /
delayed / latent response laws are scenario mechanisms, not measurements.

Derived cell: x* = 100, y* = 0.0981481 weasels/ha, T = tr J = 0.301889,
D = det J = 0.0393122, complex eigenvalues, alpha*(A) = 0.44777 -> the ODE
equilibrium is UNSTABLE while the Caputo law at alpha = 0.40 is Matignon-stable:
the case study operates in the fractional-stabilization regime of the companion.

Outputs: case_study_vole.json + two publication figures
  fig_case_traj.pdf   trajectories of the four laws under the S0 pwc6 design,
                      with the Allee threshold and the safety margin
  fig_case_design.pdf margin-vs-accuracy plane for 6 classical families + S0
"""
import json, math, os, sys, zlib
import numpy as np
from math import gamma as _gamma
from scipy.optimize import minimize_scalar

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "benchmark"))
import core  # caputo_pece(g, z0, T, N, alpha) is parameter-agnostic

# ----------------------------------------------------------------- case parameters
R_, K_, A_, AA_, HH_ = 1.0, 150.0, 37.5, 100.0, 1.0/6.0     # r, K, Allee, a=Q/D0, h=1/D0
MU_ = 1.25                                                   # weasel loss rate /yr
XSTAR = 100.0
E_ = MU_ * (1.0/XSTAR + HH_) / AA_                           # places x* at 100 exactly
T_, N_ = 12.0, 400
ALPHA, TAU, LAT_RATES, LAT_G = 0.40, 0.35, np.array([0.6, 1.0, 0.4]), 0.15
AMP = 0.08 * XSTAR                                           # 8% relative forcing (all-law-safe for S0)
STATE_BOUND = 20.0 * K_
SNR_DB = {"hi": 20.0, "med": 10.0}
PWC6 = [0.756699881516397, 0.1325216805562377, 0.8458247799426317,
        0.7344822846353054, 0.14397935662418604, 0.32357181794941425]
CAND = ["ODE", "Caputo", "DDE", "latent3"]


def P(x):  return R_ * x * (1 - x/K_) * (x/A_ - 1)
def hol(x, y): return AA_ * x * y / (1 + HH_ * x)

def f_vec(z):
    x, y = z
    return np.array([P(x) - hol(x, y), E_ * hol(x, y) - MU_ * y])

def equilibrium():
    ys = P(XSTAR) * (1 + HH_*XSTAR) / (AA_ * XSTAR)
    Pp = R_ * ((1 - 2*XSTAR/K_) * (XSTAR/A_ - 1) + XSTAR * (1 - XSTAR/K_) / A_)
    den = 1 + HH_*XSTAR
    J11 = Pp - AA_*ys/den**2
    J12 = -AA_*XSTAR/den
    J21 = E_*AA_*ys/den**2
    Tt, Dd = J11, -J12*J21
    lam_im = math.sqrt(max(Dd - Tt*Tt/4, 0.0))
    astar = 2.0/math.pi * math.atan2(lam_im, Tt/2)
    return ys, np.array([[J11, J12], [J21, 0.0]]), Tt, Dd, astar

YSTAR, J_, TRJ, DETJ, ASTAR = equilibrium()

# ----------------------------------------------------------------- inputs
def _scale(uarr):
    m = np.max(np.abs(uarr));  return uarr*(AMP/m) if m > 0 else uarr

def build_input(uf, N=N_):
    ts = np.linspace(0.0, T_, N+1)
    ua = _scale(np.asarray(uf(ts)))
    return lambda t: float(np.interp(t, ts, ua))

INPUTS = {
    "pulse":      lambda ts: ((ts >= 1.0) & (ts <= 2.0)).astype(float),
    "sinusoid":   lambda ts: np.sin(2*np.pi*ts/3.0),
    "multisine":  lambda ts: (np.sin(2*np.pi*ts/6)+np.sin(2*np.pi*ts/2)+np.sin(2*np.pi*ts/0.8))/3,
    "multiscale": lambda ts: (np.sin(2*np.pi*ts/12)+0.5*np.sin(2*np.pi*ts/4))/1.5,
    "chirp":      lambda ts: np.sin(2*np.pi*(0.1+0.4*ts/T_)*ts),
    "prbs":       lambda ts: np.sign(np.sin(2*np.pi*ts/1.5)+0.6*np.sin(2*np.pi*ts/0.53)+0.3),
    "pwc6-S0":    lambda ts: 2*np.asarray(PWC6)[np.clip((ts/(T_/6)).astype(int), 0, 5)]-1,
}

# ----------------------------------------------------------------- simulators
def _rk4(rhs, z0, ts):
    z = np.zeros((len(ts), len(z0))); z[0] = z0
    for i in range(len(ts)-1):
        h = ts[i+1]-ts[i]; t = ts[i]; zi = z[i]
        k1 = rhs(t, zi); k2 = rhs(t+h/2, zi+h/2*k1)
        k3 = rhs(t+h/2, zi+h/2*k2); k4 = rhs(t+h, zi+h*k3)
        z[i+1] = zi + h/6*(k1+2*k2+2*k3+k4)
        if not np.all(np.isfinite(z[i+1])) or np.max(np.abs(z[i+1])) > STATE_BOUND:
            z[i+1:] = np.nan; break
    return z

def sim(model, uval, alpha=ALPHA, tau=TAU, gl=LAT_G, N=N_):
    ts = np.linspace(0.0, T_, N+1)
    z0 = np.array([XSTAR, YSTAR]); B = np.array([1.0, 0.0])
    if model == "ODE":
        return ts, _rk4(lambda t, z: f_vec(z) + B*uval(t), z0, ts)
    if model == "Caputo":
        return ts, core.caputo_pece(lambda t, z: f_vec(z) + B*uval(t), z0, T_, N, alpha, 1.0)
    if model == "DDE":
        h = ts[1]-ts[0]; z = np.zeros((N+1, 2)); z[0] = z0
        def hist(tq, i):
            if tq <= 0: return z0
            k = min(int(tq/h), i); fr = tq/h - k
            return z[k]*(1-fr) + z[min(k+1, i)]*fr
        def F(t, zi, zd):
            x, y = zi
            return np.array([P(x) - hol(x, y) + uval(t),
                             E_*AA_*zd[0]*y/(1+HH_*zd[0]) - MU_*y])
        for i in range(N):
            t = ts[i]
            k1 = F(t, z[i], hist(t-tau, i))
            k2 = F(t+h/2, z[i]+h/2*k1, hist(t+h/2-tau, i))
            k3 = F(t+h/2, z[i]+h/2*k2, hist(t+h/2-tau, i))
            k4 = F(t+h, z[i]+h*k3, hist(t+h-tau, i))
            z[i+1] = z[i] + h/6*(k1+2*k2+2*k3+k4)
            if not np.all(np.isfinite(z[i+1])) or np.max(np.abs(z[i+1])) > STATE_BOUND:
                z[i+1:] = np.nan; break
        return ts, z
    if model == "latent3":
        rates = LAT_RATES; m = len(rates)
        def rhs(t, za):
            x, y = za[0], za[1]; q = za[2:]
            u = uval(t)
            return np.concatenate([[P(x) - hol(x, y) + gl*XSTAR*q.sum()/10.0 + u,
                                    E_*hol(x, y) - MU_*y], -rates*q + np.full(m, u/AMP)])
        za = _rk4(rhs, np.concatenate([z0, np.zeros(m)]), ts)
        return ts, za[:, :2]
    raise ValueError(model)

def diverged(tr): return (not np.all(np.isfinite(tr))) or np.nanmax(np.abs(tr)) > STATE_BOUND

# ----------------------------------------------------------------- BIC layer (benchmark rule)
TSAMP = np.linspace(0.5, T_, 24)

def _sample(ts, tr): return np.array([np.interp(TSAMP, ts, tr[:, j]) for j in range(2)]).T

def observe(ts, tr, C):  return (C @ _sample(ts, tr).T).T.flatten()

def noise_sigma(sig, db): return float(np.sqrt(np.mean(sig**2)) * 10**(-db/20.0))

def fit(model, data, uval, C):
    def sse(p):
        kw = {}
        if model == "Caputo": kw["alpha"] = p
        elif model == "DDE": kw["tau"] = p
        elif model == "latent3": kw["gl"] = p
        ts, tr = sim(model, uval, **kw)
        if diverged(tr): return np.inf
        return float(np.sum((observe(ts, tr, C) - data)**2))
    if model == "ODE": return sse(None), 0
    b = {"Caputo": (0.15, 0.999), "DDE": (0.05, 0.8), "latent3": (0.02, 0.6)}[model]
    r = minimize_scalar(sse, bounds=b, method="bounded", options={"xatol": 2e-2, "maxiter": 20})
    return float(r.fun), 1

def run_design(name, reps=100, snrs=("hi", "med"), channels=("prey", "both"), seed0=7000):
    uval = build_input(INPUTS[name])
    CH = {"prey": np.array([[1.0, 0.0]]), "both": np.array([[1.0, 0.0], [0.0, XSTAR/YSTAR/10]])}
    out = {"design": name, "cells": []}
    margin = np.inf
    for true_m in CAND:
        ts, tr = sim(true_m, uval)
        assert not diverged(tr), (name, true_m)
        margin = min(margin, float(np.nanmin(tr[:, 0]) - A_))
        for snr in snrs:
            for ch in channels:
                C = CH[ch]
                clean = observe(ts, tr, C)
                sg = noise_sigma(clean, SNR_DB[snr])
                conf = {c: 0 for c in CAND}
                for r in range(reps):
                    rng = np.random.default_rng(seed0 + 977*r + zlib.crc32(f"{name}|{true_m}|{snr}|{ch}".encode()) % 1000)
                    data = clean + rng.normal(0, sg, clean.shape)
                    bics = []
                    for c in CAND:
                        s_, k = fit(c, data, uval, C); n = data.size
                        bics.append(np.inf if not np.isfinite(s_) else
                                    k*np.log(n) - 2*(-0.5*n*np.log(2*np.pi*sg**2) - 0.5*s_/sg**2))
                    b = np.asarray(bics, float); b[~np.isfinite(b)] = np.inf
                    conf[CAND[int(np.argmin(b))]] += 1
                out["cells"].append({"true": true_m, "snr": snr, "ch": ch, "conf": conf})
    rec = {}
    for c in CAND:
        sel = sum(cell["conf"][c] for cell in out["cells"] if cell["true"] == c)
        tot = sum(sum(cell["conf"].values()) for cell in out["cells"] if cell["true"] == c)
        rec[c] = sel/tot if tot else None
    out["recall"] = rec
    out["macro"] = float(np.mean([v for v in rec.values() if v is not None]))
    out["min_margin"] = margin
    return out


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=100)
    ap.add_argument("--designs", nargs="*", default=list(INPUTS))
    ap.add_argument("--out", default="case_study_vole.json")
    args = ap.parse_args()
    meta = dict(r=R_, K=K_, A=A_, a=AA_, h=HH_, e=E_, mu=MU_, x_star=XSTAR, y_star=YSTAR,
                trJ=TRJ, detJ=DETJ, alpha_star=ASTAR, alpha=ALPHA, tau=TAU, T=T_, N=N_,
                amp=AMP, snr_db=SNR_DB, tsamp=[float(x) for x in TSAMP])
    print(json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in meta.items()
                      if not isinstance(v, (list, dict))}), flush=True)
    res = {"meta": meta, "designs": {}}
    for d in args.designs:
        r = run_design(d, reps=args.reps)
        res["designs"][d] = r
        print(f"{d:>11}  macro={r['macro']:.4f}  min_margin={r['min_margin']:+8.2f}  "
              f"recall={{{', '.join(f'{k}:{v:.2f}' for k, v in r['recall'].items())}}}", flush=True)
        json.dump(res, open(args.out, "w"), indent=1)
    print("DONE", flush=True)
