#!/usr/bin/env python3
"""compute_B_safe.py — Round 2: Strong-Allee-dependent safe energy/amplitude bound.

Derives the numerical value of the linear safe-excitation interface

    B_safe(A, alpha, T, rho) = sqrt(T) * rho / Gamma_T(A, alpha),

where Gamma_T is the finite-horizon L1->Linf gain of the linearized Caputo
impulse response (manuscript Lemma `lem:linear_safety`) and rho = x* - A is
the Allee margin in the prey coordinate. This is the quantity Theorem R1
(research_rounds/round1) consumes.

No factorial benchmark is re-run. This script only evaluates closed-form
linear-system quantities on the locked ecological parameters
(source_pack/04, benchmark/core.py).

Validation gate: at alpha = 1 the Mittag-Leffler kernel reduces to the matrix
exponential, and Gamma_T must match integral ||expm(J t) B|| dt computed with
scipy. This is asserted before any bound is reported.
"""
import json
import os

import numpy as np
from math import lgamma
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "benchmark"))
import core

TAU0 = 1.0
T_BENCH = 12.0          # benchmark horizon (designs.HORIZON["med"])
U_CAP = 0.10            # common peak-amplitude budget of the benchmark
Bvec = np.array([1.0, 0.0])


def ml2(a, b, z, kmax=400, tol=1e-14):
    """Two-parameter Mittag-Leffler E_{a,b}(z) for scalar/array complex z, float64.

    E_{a,b}(z) = sum_k z^k / Gamma(a k + b). Term magnitudes are controlled via
    log-space; truncation when the running term drops below tol * partial sum.
    """
    z = np.asarray(z, dtype=complex)
    out = np.zeros_like(z)
    log_abs = np.full(z.shape, -np.inf)
    term_log = -np.array([lgamma(b)] * 1)  # k=0: 1/Gamma(b)
    # k = 0 term
    out = out + (1.0 / np.exp(lgamma(b)))
    running = np.abs(out)
    for k in range(1, kmax + 1):
        c = np.exp(k * np.log(np.maximum(np.abs(z), 1e-300)) - lgamma(a * k + b))
        # phase of z^k
        phase = np.exp(1j * k * np.angle(z))
        term = np.where(np.abs(z) == 0, 0.0, c) * phase
        out = out + term
        running = running + np.abs(term)
        if np.max(np.abs(term)) <= tol * max(np.max(running), 1e-300):
            break
    return out


def impulse_norm(A_param, alpha, ts):
    """||H_alpha(t)|| for the prey channel, H_alpha(t) = tau0^{1-a} t^{a-1} E_{a,a}(J t^a) B."""
    J = core.jacobian(A_param)
    w, V = np.linalg.eig(J)
    Vi = np.linalg.inv(V)
    VB = Vi @ Bvec                      # coordinates of B in the eigenbasis
    H = np.zeros((len(ts), 2), dtype=complex)
    for i, t in enumerate(ts):
        if t == 0:
            H[i] = 0.0
            continue
        za = TAU0 ** (1 - alpha) * (t ** alpha) * w
        E = ml2(alpha, alpha, za)
        xi = V @ (E * VB)               # E_{a,a}(J t^a) B
        H[i] = TAU0 ** (1 - alpha) * t ** (alpha - 1) * xi
    return np.linalg.norm(H.real, axis=1)   # imaginary parts cancel (real system)


def gamma_T(A_param, alpha, T, n=24000, eps=1e-6):
    """Gamma_T = int_0^T ||H_alpha(s)|| ds, with analytic head int_0^eps."""
    ts = eps + (T - eps) * (np.arange(n + 1) / n) ** 2   # clustered near eps
    norms = impulse_norm(A_param, alpha, ts)
    body = np.trapezoid(norms, ts)
    # head: ||H(t)|| ~ t^{a-1} ||B|| / Gamma(a) as t -> 0
    head = np.linalg.norm(Bvec) * eps ** alpha / (alpha * np.exp(lgamma(alpha)))
    return head + body


def validate_alpha1(A_param, T=6.0):
    """Gate: at alpha=1, Gamma_T must equal int ||expm(J t) B|| dt (scipy)."""
    from scipy.linalg import expm
    J = core.jacobian(A_param)
    ts = np.linspace(0, T, 40001)
    ref = np.array([np.linalg.norm(expm(J * t) @ Bvec) for t in ts])
    ref_val = np.trapezoid(ref, ts)
    our_val = gamma_T(A_param, 1.0, T)
    rel = abs(our_val - ref_val) / ref_val
    print(f"VALIDATION A={A_param}: alpha=1 Gamma_T = {our_val:.10f} "
          f"vs scipy {ref_val:.10f} (rel err {rel:.2e})")
    assert rel < 1e-6, "alpha->1 gate FAILED"
    return ref_val


if __name__ == "__main__":
    out = {"T_bench": T_BENCH, "u_cap": U_CAP, "locked_params": {"r": 1.5, "K": 1.0, "a": 1.0,
           "h": 0.5, "e": 0.8, "m": 0.4}, "x_star": core.x_star(), "cells": []}

    # gate first
    for A_g in (0.25, 0.30):
        validate_alpha1(A_g)

    A_grid = [0.20, 0.25, 0.30]
    alpha_grid = [0.70, 0.85, 0.90, 0.95]
    for A in A_grid:
        rho = core.x_star() - A
        astar = core.alpha_star(A)
        for alpha in alpha_grid:
            gT = gamma_T(A, alpha, T_BENCH)
            u_safe = rho / gT
            B_safe = np.sqrt(T_BENCH) * u_safe
            B_cap = np.sqrt(T_BENCH) * U_CAP
            cell = {"A": A, "alpha": alpha, "alpha_star": astar,
                    "rho_allee": rho, "Gamma_T": gT,
                    "u_safe": u_safe, "B_safe": B_safe,
                    "B_generic_cap": B_cap,
                    "tightness_vs_cap": min(1.0, u_safe / U_CAP),
                    "cap_active": bool(u_safe >= U_CAP)}
            out["cells"].append(cell)
            print(f"A={A:.2f} alpha={alpha:.2f} alpha*={astar if astar else '-'}: "
                  f"Gamma_T={gT:.4f}, u_safe={u_safe:.4f} (cap {U_CAP}), "
                  f"B_safe={B_safe:.4f} vs generic {B_cap:.4f}")

    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "B_safe_grid.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("wrote", os.path.join(here, "B_safe_grid.json"))
