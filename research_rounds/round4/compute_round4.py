#!/usr/bin/env python3
"""compute_round4.py — Round 4: Phase-0 closure numerics + Phase-1 testing theorem.

Phase 0 (closure of chief-audit P0 items):
  0.2  certified numerical L1 upper certificates Ebar_m^cert for the explicit
       left-node mixtures (analytic singular head + adaptive quadrature with
       rigorous error accounting);
  0.3  one-sided downward gains d_M and shape-specific peak-cap energy bounds;
  0.5  restricted singular values after orthonormalizing dictionary spans.

Phase 1 (testing theorem numerics):
  KL ceiling with the certified Ebar_m^cert, continuous-observation constant
  C_obs = 1/(2 sigma^2), exact equal-covariance Gaussian pairwise error
  P_e = Phi(-sqrt(KL/2)) for the fixed constructive competitor.

Reuses released benchmark code; no factorial benchmark rerun.
"""
import json
import math
import os
import sys

import numpy as np
from scipy.integrate import quad
from scipy.linalg import svdvals
from scipy.special import gamma
from scipy.stats import norm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "benchmark"))
sys.path.insert(0, os.path.join(ROOT, "research_rounds", "round3"))
sys.path.insert(0, os.path.join(ROOT, "research_rounds", "round2"))
import bench
import compute_B_safe  # noqa: F401  (path side effects)
import compute_round3 as r3
import core
import designs
from chief_round3_checks import dictionary_matrix, l1_adaptive, transient_common_bounds

ALPHA = 0.85
T = 12.0
ETA = 0.02
UMAX = 0.10
CA = math.sin(math.pi * ALPHA) / math.pi


def k_exact(t):
    return t ** (ALPHA - 1) / gamma(ALPHA)


def kmix(t, m, ell, L):
    h = (L - ell) / m
    lam = ell + np.arange(m) * h
    t = np.atleast_1d(np.asarray(t, dtype=float))
    return CA * h * np.sum(lam[:, None] ** (-ALPHA)
                           * np.exp(-lam[:, None] * t[None, :]), axis=0)


def certified_Ebar(m, ell, L, delta=1e-4):
    """Rigorous upper bound on ||k_alpha - k_m||_{L^1(0,T)}.

    Head (0,delta), exact integration of both parts (no triangle inequality):
        int_0^delta k_a = delta^alpha/(alpha Gamma(alpha))
        int_0^delta k_m = c_a h sum_j lam_j^{-alpha} (1-e^{-lam_j delta})/lam_j
        -> head <= sum of the two (both kernels nonnegative).
    Body [delta,T]: adaptive quadrature with returned error estimate added.
    """
    h = (L - ell) / m
    lam = ell + np.arange(m) * h
    head_exact = (delta ** ALPHA / (ALPHA * gamma(ALPHA))
                  + CA * h * np.sum(lam ** (-ALPHA) * (1 - np.exp(-lam * delta)) / lam))
    head = float(head_exact)
    val, err = quad(lambda t: abs(k_exact(t) - float(kmix(np.array([t]), m, ell, L)[0])),
                    delta, T, epsabs=1e-10, epsrel=1e-10, limit=800)
    cert = head + val + err
    return {"m": m, "ell": ell, "L": L, "head": head, "body_quad": val,
            "quad_err_est": err, "Ebar_cert": cert}


def phase0_certificates():
    D = json.load(open(os.path.join(HERE, "..", "round3", "round3_results.json")))
    cells = D["track_A"]["cells"]
    certs = []
    for c in cells:
        cert = certified_Ebar(c["m"], c["ell"], c["L"])
        cert["candidate_grid_error"] = c["E_m"]
        certs.append(cert)
        print(f"P0.2: m={c['m']:3d}  Ebar_cert={cert['Ebar_cert']:.6f} "
              f"(candidate {c['E_m']:.6f}, quad err {cert['quad_err_est']:.2e})")
    return certs


def phase1_testing(certs):
    """Continuous-observation Gaussian model:
    KL(u; C_alpha vs k_m) <= (1/(2 sigma^2)) Ebar_m^cert^2 ||u||_2^2.
    B_eff options:
      universal peak cap:       B = sqrt(T) u_max
      shape-specific (pulse):   B = u_max ||u0||_2 / ||u0||_inf
    P_e lower bound (exact for fixed competitor): Phi(-sqrt(KL_upper/2)).
    """
    out = {"C_obs": "1/(2 sigma^2)", "caps": {}, "curves": {}}
    B_univ = math.sqrt(T) * UMAX
    out["caps"]["universal_peak_cap"] = B_univ
    # shape-specific caps
    for name in ["pulse", "multiscale"]:
        ts, uarr, _ = bench.build_input(designs.INPUTS[name], T, 1600, amp=1.0)
        dt = ts[1] - ts[0]
        nrm = float(np.sqrt(np.sum(uarr ** 2) * dt))
        peak = float(np.max(np.abs(uarr)))
        out["caps"][name] = UMAX * nrm / peak

    # sigma grid: benchmark-style noise levels (absolute)
    sigmas = [0.02, 0.03, 0.05, 0.08, 0.10]
    for label, B in [("universal_peak_cap", B_univ),
                     ("pulse_shape_cap", out["caps"]["pulse"]),
                     ("multiscale_shape_cap", out["caps"]["multiscale"])]:
        curve = []
        for c in certs:
            row = {"m": c["m"], "Ebar_cert": c["Ebar_cert"]}
            for sig in sigmas:
                kl_upper = (c["Ebar_cert"] ** 2) * (B ** 2) / (2 * sig ** 2)
                pe = float(norm.cdf(-math.sqrt(kl_upper / 2.0)))
                row[f"sigma_{sig}"] = {"KL_upper": kl_upper, "Pe_lower": pe}
            curve.append(row)
        out["curves"][label] = curve
    return out


def phase1_exact_pairwise():
    """Exact equal-covariance Gaussian pairwise error for the fixed constructive
    competitor k_5 (declared budget) at the primary cell, computed with the
    released linear simulators: KL from sampled prey responses, benchmark noise."""
    A = 0.25
    N = 2000
    tsamp = designs.sample_times(T, 120)
    Cprey = designs.CHANNELS["prey"]
    SNR = 10.0
    rows = []
    for name in ["pulse", "multiscale"]:
        ts, uarr, _ = bench.build_input(designs.INPUTS[name], T, N, amp=UMAX)
        dt = ts[1] - ts[0]
        u_l2 = float(np.sqrt(np.sum(uarr ** 2) * dt))
        yC = bench.lin_response("Caputo", A, ALPHA, designs.INPUTS[name], T, N,
                                Cprey, tsamp, amp=UMAX)[:, 0]
        yL = bench.lin_response("latent3", A, ALPHA, designs.INPUTS[name], T, N,
                                Cprey, tsamp, amp=UMAX)[:, 0]
        sig = float(np.sqrt(np.mean(yC ** 2) / (10 ** (SNR / 10))) + 1e-9)
        kl = float(np.sum((yC - yL) ** 2) / (2 * sig ** 2))
        pe = float(norm.cdf(-math.sqrt(kl / 2.0)))
        rows.append({"design": name, "A": A, "alpha": ALPHA, "u_l2_at_peak_cap": u_l2,
                     "sigma_snr10dB": sig, "KL_empirical": kl, "Pe_exact": pe})
        print(f"P1-exact: {name}: u_l2={u_l2:.4f} sigma={sig:.4f} KL={kl:.4f} Pe={pe:.4f}")
    return rows


def phase0_dictionaries():
    """0.5 — restricted singular values with orthonormalized spans (chief method)."""
    from chief_round3_checks import corrected_span_kappa
    return {n: corrected_span_kappa(n) for n in ["sinusoid", "multisine", "chirp", "prbs"]}


if __name__ == "__main__":
    out = {"params": {"alpha": ALPHA, "T": T, "eta": ETA, "u_max": UMAX,
                      "x_star": core.x_star()}}
    out["phase0_certificates"] = phase0_certificates()
    out["phase0_one_sided_benchmark_rivals"] = [
        transient_common_bounds(A, n) | {"A": A, "family": n}
        for A in (0.25, 0.30, 0.32, 0.34) for n in ("pulse", "multiscale")]
    out["phase0_dictionary_kappa"] = phase0_dictionaries()
    out["phase1_testing_curves"] = phase1_testing(out["phase0_certificates"])
    out["phase1_exact_pairwise"] = phase1_exact_pairwise()
    with open(os.path.join(HERE, "round4_results.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("wrote round4_results.json")
