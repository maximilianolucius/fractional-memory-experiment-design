"""
bench.py — model simulators (linear + nonlinear) for the 4 memory mechanisms and
the discrimination primitives. v2: equal-ENERGY small perturbations (local regime,
source_pack/08 T11), interpolated-history RK4 DDE, divergence/safety guard.

Mechanisms: ODE (alpha=1), Caputo (alpha), DDE (gestation delay tau), latent (m
unobserved relaxation modes). Ecological params LOCKED; candidates differ only in
the memory mechanism + its one parameter.
"""
import numpy as np
from math import gamma
import core

TAU0 = 1.0
Bch = np.array([1.0, 0.0])     # prey intervention channel (collocated, CB!=0)
AMP = 0.10                     # SAFE peak-amplitude budget |u|_inf (audit P0.9 / pack T8.2).
                               # Calibrated on Orion: keeps min_x >> Allee for ALL rivals at A>=0.20.
DDE_TAU = 0.35                 # calibrated delay: linearly stable + safe (min_x margin >0.15 at umax=0.10),
                               # a genuine gestation delay (not tau~0); instability sets in only for tau >~ 0.5.
LAT_G = 0.15                   # calibrated latent coupling (small => stable + matched low-freq baseline)
LAT_RATES = (0.6, 1.0, 0.4)
STATE_BOUND = 8.0              # |state| beyond this => diverged / unsafe design

def _rk4(rhs, z0, ts):
    z = np.zeros((len(ts), len(z0))); z[0] = z0
    for i in range(len(ts) - 1):
        h = ts[i + 1] - ts[i]; t = ts[i]; zi = z[i]
        k1 = rhs(t, zi); k2 = rhs(t + h / 2, zi + h / 2 * k1)
        k3 = rhs(t + h / 2, zi + h / 2 * k2); k4 = rhs(t + h, zi + h * k3)
        z[i + 1] = zi + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if not np.all(np.isfinite(z[i + 1])) or np.max(np.abs(z[i + 1])) > 1e3:
            z[i + 1:] = np.nan; break
    return z

def build_input(uf, T, N, amp=AMP):
    """Fine-grid input clamped to peak amplitude `amp` (|u|_inf=amp) on [0,T]. Equal-amplitude
    is the SAFETY-relevant budget (pack T8.2 uses ||u||_inf), not equal-energy. Returns (ts,uarr,uval)."""
    ts = np.linspace(0.0, T, N + 1)
    uarr = uf(ts, T)
    m = np.max(np.abs(uarr))
    if m > 0: uarr = uarr * (amp / m)
    def uval(t): return float(np.interp(t, ts, uarr))
    return ts, uarr, uval

def diverged(traj):
    return (not np.all(np.isfinite(traj))) or (np.nanmax(np.abs(traj)) > STATE_BOUND)

# ---- interpolated-history DDE integrator (RK4) : dz/dt = F(t, z(t), z(t-tau), u) ----
def _dde_rk4(F, z0, ts, tau):
    n = len(ts); h = ts[1] - ts[0]; z = np.zeros((n, len(z0))); z[0] = z0
    def hist(tq, i):
        if tq <= 0: return z0
        k = tq / h
        lo = int(np.floor(k)); lo = min(lo, i); frac = k - lo
        if lo >= i: return z[i]
        return z[lo] * (1 - frac) + z[min(lo + 1, i)] * frac
    for i in range(n - 1):
        t = ts[i]
        k1 = F(t, z[i], hist(t - tau, i))
        k2 = F(t + h / 2, z[i] + h / 2 * k1, hist(t + h / 2 - tau, i))
        k3 = F(t + h / 2, z[i] + h / 2 * k2, hist(t + h / 2 - tau, i))
        k4 = F(t + h, z[i] + h * k3, hist(t + h - tau, i))
        z[i + 1] = z[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if not np.all(np.isfinite(z[i + 1])) or np.max(np.abs(z[i + 1])) > 1e3:
            z[i + 1:] = np.nan; break
    return z

# ============================================================ NONLINEAR forward simulators (data-generating)
def sim_nonlinear(model, A, alpha, uf, T, N, tau=DDE_TAU, lam=LAT_RATES, gcoup=LAT_G, amp=AMP):
    ts, uarr, uval = build_input(uf, T, N, amp)
    xs, ys = core.x_star(), core.y_star(A); z0 = np.array([xs, ys])
    if model == "ODE":
        return ts, _rk4(lambda t, z: core.f_vec(z, A) + Bch * uval(t), z0, ts)
    if model == "Caputo":
        g = lambda t, z: TAU0 ** (1 - alpha) * (core.f_vec(z, A) + Bch * uval(t))
        return ts, core.caputo_pece(g, z0, T, N, alpha, TAU0)
    if model == "DDE":
        def F(t, z, zd):
            xd = zd[0]
            hol_d = core.AA * xd * z[1] / (1 + core.HH * xd)
            dx = core.P(z[0], A) - core.AA * z[0] * z[1] / (1 + core.HH * z[0]) + uval(t)
            dy = core.EE * hol_d - core.MM * z[1]
            return np.array([dx, dy])
        return ts, _dde_rk4(F, z0, ts, tau)
    if model in ("latent1", "latent3"):
        rates = np.array(lam if model == "latent3" else lam[:1]); m = len(rates)
        def rhs(t, za):
            x, y = za[0], za[1]; zc = za[2:]
            hol = core.AA * x * y / (1 + core.HH * x)
            return np.concatenate([[core.P(x, A) - hol + gcoup * zc.sum() + uval(t),
                                    core.EE * hol - core.MM * y], -rates * zc + uval(t)])
        za = _rk4(rhs, np.concatenate([z0, np.zeros(m)]), ts)
        return ts, za[:, :2]
    raise ValueError(model)

# ============================================================ LINEAR simulators (about equilibrium)
def _sample(ts_fine, traj, tsamp):
    return np.array([np.interp(tsamp, ts_fine, traj[:, j]) for j in range(traj.shape[1])]).T

def lin_response(model, A, alpha, uf, T, N, C, tsamp, tau=DDE_TAU, lam=LAT_RATES, gcoup=LAT_G, amp=AMP):
    J = core.jacobian(A); ts, uarr, uval = build_input(uf, T, N, amp)
    if model == "ODE":
        out = _rk4(lambda t, xi: J @ xi + Bch * uval(t), np.zeros(2), ts)
    elif model == "Caputo":
        g = lambda t, xi: TAU0 ** (1 - alpha) * (J @ xi + Bch * uval(t))
        out = core.caputo_pece(g, np.zeros(2), T, N, alpha, TAU0)
    elif model == "DDE":
        J0 = J.copy(); J1 = np.zeros((2, 2)); J1[1, 0] = J[1, 0]; J0[1, 0] = 0.0
        out = _dde_rk4(lambda t, xi, xid: J0 @ xi + J1 @ xid + Bch * uval(t), np.zeros(2), ts, tau)
    elif model in ("latent1", "latent3"):
        rates = np.array(lam if model == "latent3" else lam[:1]); m = len(rates)
        Abar = np.zeros((2 + m, 2 + m)); Abar[:2, :2] = J
        Abar[0, 2:] = gcoup; Abar[2:, 2:] = -np.diag(rates)
        Bbar = np.zeros(2 + m); Bbar[0] = 1.0; Bbar[2:] = 1.0
        out = _rk4(lambda t, xa: Abar @ xa + Bbar * uval(t), np.zeros(2 + m), ts)[:, :2]
    else:
        raise ValueError(model)
    return (C @ _sample(ts, out, tsamp).T).T

# ============================================================ discrimination primitives
from scipy.stats import norm

def pairwise_error(mu_i, mu_j, sigma):
    d2 = np.sum((mu_i - mu_j) ** 2) / (sigma ** 2)
    return float(norm.cdf(-0.5 * np.sqrt(d2))), float(0.5 * d2)

def safety_metrics(traj, A):
    """Numerical safety certificate (audit P0.9/P1.12): distance above the Allee
    threshold and to a safe rectangle around the equilibrium. NOT 'zero divergence'."""
    xs, ys = core.x_star(), core.y_star(A)
    xL = max(A + 0.02, 0.5 * xs); xU = 1.6 * xs
    yL = max(1e-3, 0.4 * ys);     yU = 1.9 * ys
    x, y = traj[:, 0], traj[:, 1]
    fin = np.isfinite(x) & np.isfinite(y)
    if not fin.any():
        return {"allee_margin": None, "face_dist": None, "allee_crossed": True, "rect": [xL, xU, yL, yU]}
    x, y = x[fin], y[fin]
    return {"allee_margin": float(x.min() - A),
            "face_dist": float(min(x.min() - xL, xU - x.max(), y.min() - yL, yU - y.max())),
            "allee_crossed": bool(x.min() <= A),
            "min_x": float(x.min()), "max_x": float(x.max()), "rect": [xL, xU, yL, yU]}
