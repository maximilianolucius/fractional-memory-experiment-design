#!/usr/bin/env python3
"""compute_round3.py — Round 3: latent complexity law E_m + safety-interface repair.

Track A: quantitative E_m(alpha,T) for the frozen left-node exponential-sum class.
Track B: (i) high-frequency null-direction theorem (no Allee-only outer energy
bound exists); (ii) coercivity constants kappa_V for the frozen design families
of benchmark/designs.py; (iii) effective outer safe-energy bound combining the
coercivity certificate with the explicit actuator cap.

Reuses the released benchmark/core.py and benchmark/designs.py. No factorial
benchmark is re-run.
"""
import json
import os
import sys

import numpy as np
from math import lgamma
from scipy.linalg import svdvals

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "benchmark"))
sys.path.insert(0, os.path.join(ROOT, "research_rounds", "round2"))
import core
import designs
from compute_B_safe import ml2   # validated two-parameter Mittag-Leffler (alpha->1 gate)

T_BENCH = 12.0          # medium horizon
U_MAX = 0.10            # explicit actuator cap (benchmark)
ETA = 0.02              # strict Allee reserve (R2a scope guard)
ALPHA = 0.85            # primary focal order
A_PRI = 0.25            # primary stable baseline
CA = np.sin(np.pi * ALPHA) / np.pi

Bvec = np.array([1.0, 0.0])


def k_exact(t):
    return t ** (ALPHA - 1) / np.exp(lgamma(ALPHA))


# --------------------------------------------------------------------------
# Track A — E_m law for the frozen left-node class
# --------------------------------------------------------------------------
def l1_err(m, ell, L, T=T_BENCH):
    """||k_alpha - k_m||_{L^1(0,T)} for the left-node sum of Theorem T9b,
    evaluated by composite quadrature with analytic singular head."""
    h = (L - ell) / m
    lam = ell + np.arange(m) * h
    # quadrature: dense near 0, coarser away
    n1, n2 = 400, 1600
    t1 = np.linspace(1e-6, 0.5, n1)
    t2 = np.linspace(0.5, T, n2)
    tt = np.concatenate([t1, t2])
    exact = k_exact(tt)
    approx = CA * h * np.sum(lam[:, None] ** (-ALPHA) * np.exp(-lam[:, None] * tt[None, :]), axis=0)
    err = np.trapezoid(np.abs(exact - approx), tt)
    # analytic head contribution on (0, 1e-6): |k_alpha - k_m| ~ k_alpha there
    head = (1e-6) ** ALPHA / (ALPHA * np.exp(lgamma(ALPHA)))
    return err + head


def r1_bound(m, ell, L, T=T_BENCH):
    """Manuscript Theorem T9b polynomial bound (eq. 4)."""
    h = (L - ell) / m
    return CA * (T * ell ** (1 - ALPHA) / (1 - ALPHA) + L ** (-ALPHA) / ALPHA + T * h * ell ** (-ALPHA))


def tune_E(m):
    """Deterministic tuning over the theorem's free truncation parameters."""
    ELL = np.logspace(-4.5, -0.5, 28)
    LG = np.logspace(-0.15, 1.5, 30)
    best = (np.inf, None, None)
    for ell in ELL:
        for L in LG:
            if L <= ell:
                continue
            e = l1_err(m, ell, L)
            if e < best[0]:
                best = (e, ell, L)
    return best


def track_A():
    ms = [1, 2, 3, 4, 5, 6, 8, 12, 16, 24, 32]
    rows = []
    for m in ms:
        e, el, L = tune_E(m)
        rb = r1_bound(m, el, L)
        rows.append({"m": m, "E_m": e, "ell": el, "L": L, "T9b_bound_at_tuned": rb})
        print(f"A: m={m:3d}  E_m={e:.6f}  (ell={el:.3g}, L={L:.3g})  T9b bound={rb:.4f}")
    # geometric fit on the empirical envelope
    mm = np.array([r["m"] for r in rows], float)
    ee = np.minimum.accumulate(np.array([r["E_m"] for r in rows]))
    # least squares log E ~ a + b m  (geometric rate rho = exp(b))
    bfit = np.polyfit(mm[mm >= 2], np.log(ee[mm >= 2]), 1)
    rho_emp = float(np.exp(bfit[0]))
    # exp(-c sqrt(m)) fit (Braess-Hackbusch-type scale)
    sq = np.sqrt(mm[mm >= 2])
    cfit = np.polyfit(sq, np.log(ee[mm >= 2]), 1)
    print(f"A: empirical geometric rate rho ~ {rho_emp:.4f} (fit on m>=2)")
    print(f"A: exp(-c sqrt(m)) fit: c ~ {-cfit[0]:.4f} (finite-window diagnostic only)")
    return {"cells": rows, "empirical_geometric_rate": rho_emp,
            "exp_sqrtm_c": float(-cfit[0]),
            "note": "envelope of best displayed errors over deterministic (ell,L) grid"}


# --------------------------------------------------------------------------
# Track B — null-direction theorem + coercivity
# --------------------------------------------------------------------------
def impulse_matrices(A, alpha, ts):
    """Return prey kernel h_x(t) = e_1^T H_alpha(t) for t in ts.

    Uses the validated ml2 (two-parameter Mittag-Leffler) through the
    eigenbasis of J; same machinery as round2/compute_B_safe.py.
    """
    J = core.jacobian(A)
    w, V = np.linalg.eig(J)
    Vi = np.linalg.inv(V)
    VB = Vi @ Bvec
    n = len(ts)
    hx = np.zeros(n)
    for i, t in enumerate(ts):
        if t <= 0:
            continue
        za = (t ** alpha) * w
        E = ml2(alpha, alpha, za)          # complex array, convergent series
        xi = V @ (E * VB)
        hx[i] = float(np.real(t ** (alpha - 1) * xi[0]))
    return hx


def toeplitz_conv(h, dt):
    """Lower-triangular convolution matrix (y = h * u sampled, causal)."""
    n = len(h)
    K = np.zeros((n, n))
    for j in range(n):
        K[j:, j] = h[: n - j]
    return K * dt


def hf_null_test(A=0.25, alpha=0.85, T=12.0):
    """High-frequency probe u_eps(t) = sqrt(eps/T) sin(t/eps), ||u_eps||_2 ~ 1.
    Theory predicts sup_t |x_eps(t)| = O(eps^alpha)."""
    n = 6000
    ts = np.linspace(0, T, n)
    dt = ts[1] - ts[0]
    hx = impulse_matrices(A, alpha, ts)
    K = toeplitz_conv(hx, dt)
    rows = []
    for eps in [1.0, 0.1, 0.01, 0.002]:
        u = np.sqrt(eps / T) * np.sin(ts / eps)
        u = u / np.sqrt(np.sum(u**2) * dt)          # unit L2
        x = K @ u
        rows.append({"eps": eps, "L2_u": float(np.sqrt(np.sum(u**2) * dt)),
                     "sup_x_unit_energy": float(np.max(np.abs(x)))})
        print(f"B-hf: eps={eps:6.3f}  ||u||_2={rows[-1]['L2_u']:.3f}  sup|x|={rows[-1]['sup_x_unit_energy']:.3e}")
    return rows


def kappa_family(name, A=0.25, alpha=0.85, T=12.0):
    """Coercivity constant kappa_V = min singular value of the prey-channel
    convolution operator restricted to a 1-parameter input family."""
    n = 500
    ts = np.linspace(T / n, T, n)
    dt = ts[1] - ts[0]
    hx = impulse_matrices(A, alpha, ts)
    K = toeplitz_conv(hx, dt)
    fam = designs.INPUTS[name]
    if name == "sinusoid":
        ws = np.linspace(0.05, 3.0, 24)
        M = np.column_stack([fam(ts, T, amp=1.0, w=w) for w in ws])
    elif name == "multisine":
        base = (0.12, 0.49, 1.6)
        Ms = []
        for k in range(24):
            ws = tuple(base[j] * (1 + 0.15 * (k - 12) / 12) for j in range(3))
            Ms.append(fam(ts, T, amp=1.0, ws=ws))
        M = np.column_stack(Ms)
    elif name == "chirp":
        M = np.column_stack([fam(ts, T, amp=1.0, f0=0.05, k=kk) for kk in np.linspace(0.005, 0.12, 20)])
    elif name == "prbs":
        M = np.column_stack([fam(ts, T, amp=1.0, nseg=15, seed=s) for s in range(24)])
    elif name == "pulse":
        M = np.column_stack([fam(ts, T, amp=1.0) for _ in range(1)])  # fixed shape
    elif name == "multiscale":
        M = np.column_stack([fam(ts, T, amp=1.0) for _ in range(1)])
    else:
        raise ValueError(name)
    # L2-normalize generators so svdvals(K @ Mhat) is the coercivity constant
    # in the L2 metric: kappa_V = inf_{u in span(M), ||u||_2=1} ||H_x u||_2.
    colnorms = np.sqrt(np.sum(M**2, axis=0) * dt)
    Mhat = M / np.where(colnorms > 0, colnorms, 1.0)
    s = svdvals(K @ Mhat)
    kappa = float(s.min())
    return kappa, float(s.max()), M.shape


def kappa_linf_family(name, A=0.25, alpha=0.85, T=12.0):
    """Linf-in-time safety coercivity for a fixed-shape family:
    kappa_V^inf = ||H_x u0||_{L^inf(0,T)} / ||u0||_2, which yields the sharp
    one-sided outer bound ||u||_2 <= rho_eta / kappa_V^inf."""
    n = 500
    ts = np.linspace(T / n, T, n)
    dt = ts[1] - ts[0]
    hx = impulse_matrices(A, alpha, ts)
    K = toeplitz_conv(hx, dt)
    u0 = designs.INPUTS[name](ts, T, amp=1.0)
    nu = np.sqrt(np.sum(u0**2) * dt)
    x = K @ u0
    return float(np.max(np.abs(x)) / nu)


def robust_worst_case_coercivity(name, A=0.25, alpha=0.85, T=12.0):
    """Track B item 4: worst-case prey-output excursion across ALL released
    rival simulators (ODE, Caputo, DDE, latent1, latent3) via bench.lin_response.

    Common ecological safety output, frozen per chief audit B: in every rival
    the first two state coordinates are the ecological (prey, predator) states
    (benchmark convention, incl. the latent models where coords 0..1 are
    ecological and 2.. are memory modes). Prey safety output = e_1^T z.
    Returns per-model sup|prey excursion| for the unit-L2 shape and the
    worst-case (robust) value.
    """
    import bench
    N = 2000
    ts, uarr, uval = bench.build_input(designs.INPUTS[name], T, N, amp=1.0)
    dt = ts[1] - ts[0]
    nu = np.sqrt(np.sum(uarr**2) * dt)
    Cprey = designs.CHANNELS["prey"]
    tsamp = designs.sample_times(T, 240)
    per_model = {}
    for model in ["ODE", "Caputo", "DDE", "latent1", "latent3"]:
        y = bench.lin_response(model, A, alpha, designs.INPUTS[name], T, N,
                               Cprey, tsamp, amp=1.0)
        # y is (240,1) prey samples of the UNIT-AMPLITUDE shape; scale by 1/nu
        per_model[model] = float(np.max(np.abs(y[:, 0])) / nu)
    worst = max(per_model.values())
    return per_model, worst


def track_B():
    hf = hf_null_test()
    kappa = {}
    for name in ["sinusoid", "multisine", "chirp", "prbs", "pulse", "multiscale"]:
        kmin, kmax, shape = kappa_family(name)
        kappa[name] = {"kappa": kmin, "sigma_max": kmax, "basis_shape": list(shape)}
        print(f"B: kappa[{name}] = {kmin:.3e}  (sigma_max {kmax:.3e}, basis {shape})")
    return {"hf_null": hf, "kappa": kappa}


if __name__ == "__main__":
    out = {"params": {"T": T_BENCH, "u_max": U_MAX, "eta": ETA, "alpha": ALPHA,
                      "A_primary": A_PRI, "x_star": core.x_star()},
           "track_A": track_A(),
           "track_B": track_B()}

    # effective outer bounds at the primary cell and neighbors.
    # Sharp one-sided form (prompt): ||u||_2 <= rho_eta / kappa_V^inf.
    cells = []
    for A in (0.20, 0.25, 0.30):
        rho_eta = core.x_star() - (A + ETA)
        if rho_eta <= 0:
            continue
        for name in ["pulse", "multiscale"]:
            kin = kappa_linf_family(name, A=A, alpha=ALPHA, T=T_BENCH)
            kmin, _, _ = kappa_family(name, A=A, alpha=ALPHA, T=T_BENCH)
            E_outer = rho_eta / kin                      # sharp L-inf form
            E_outer_l2 = np.sqrt(T_BENCH) * rho_eta / kmin  # L2-metric form
            cap = np.sqrt(T_BENCH) * U_MAX
            cells.append({"A": A, "family": name,
                          "kappa_linf": kin, "kappa_l2": kmin,
                          "outer_rho_over_kappa_inf": E_outer,
                          "outer_l2_form": E_outer_l2,
                          "actuator_cap": cap,
                          "effective_outer": min(E_outer, cap),
                          "binding": "cap" if cap <= E_outer else "allee_coercivity"})
            print(f"EFF: A={A} {name:10s} kappa_inf={kin:.4f} rho/kappa={E_outer:.4f} "
                  f"(L2 form {E_outer_l2:.4f}) cap={cap:.4f} -> "
                  f"effective={min(E_outer, cap):.4f} ({cells[-1]['binding']})")
    out["effective_outer_bounds"] = cells

    # Track B item 4: robust common-safety coercivity across the full rival family
    robust = {}
    for name in ["pulse", "multiscale"]:
        per_model, worst = robust_worst_case_coercivity(name, A=A_PRI, alpha=ALPHA, T=T_BENCH)
        rho_eta = core.x_star() - (A_PRI + ETA)
        robust[name] = {"per_model_kappa_inf": per_model,
                        "worst_case_kappa_inf": worst,
                        "robust_outer_bound": rho_eta / worst,
                        "cap": np.sqrt(T_BENCH) * U_MAX}
        print(f"ROBUST: {name}: per-model {per_model}")
        print(f"ROBUST: {name}: worst-case kappa={worst:.4f} -> outer={rho_eta/worst:.4f} vs cap {np.sqrt(T_BENCH)*U_MAX:.4f}")
    out["robust_common_safety"] = robust

    with open(os.path.join(HERE, "round3_results.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("wrote round3_results.json")
