#!/usr/bin/env python3
"""compute_round5_atlas.py — full atlas grid over (A, alpha, m, sigma).

Uses theorem-valid quantities only:
- Ehat_m^IA(alpha): interval-enclosed constructive L1 upper errors (chief R4
  machinery generalized to arbitrary alpha);
- d_rob(K_m,u0)(alpha) = M_T(alpha) * max_lam F(lam)/w(lam)  (Gate 0A exact
  reduction; F/w is alpha-free, only M_T carries alpha);
- shape cap, universal cap.
Classification: 'hard@0.25' / 'moderate@0.10' / 'inconclusive' from the
Gaussian two-point lower bound.  Nothing is labeled 'discriminable'.
"""
import json
import math
import os
import sys

import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from compute_round5 import (  # noqa: E402
    tuned_windows, proto_pulse, shape_cap, A_LIST, M_ATLAS, T, ETA, U_MAX,
    X_STAR, h_J_series, fconv, trapz)

def certified_Ebar_interval_alpha(m, ell, L, alpha, terms_head=True):
    import mpmath as mp
    mp.iv.dps = 25
    I = mp.iv
    aI = I.mpf([str(alpha), str(alpha)])
    ca = I.sin(I.pi * aI) / I.pi
    gam = I.gamma(aI)
    el = I.mpf([str(ell), str(ell)])
    LI = I.mpf([str(L), str(L)])
    hI = (LI - el) / m
    lams = [el + j * hI for j in range(m)]
    coeff = [ca * hI * (lam ** (-aI)) for lam in lams]
    DELTA = 1e-4
    dI = I.mpf([str(DELTA), str(DELTA)])
    head = dI ** aI / (aI * gam)
    for cj, lam in zip(coeff, lams):
        head += cj * (1 - I.exp(-lam * dI)) / lam
    SPLIT = 0.1
    xs = np.unique(np.concatenate([
        np.geomspace(DELTA, SPLIT, 1000 + 1),
        np.linspace(SPLIT, T, 1800 + 1)]))
    body = I.mpf([0, 0])
    p = aI - I.mpf([1, 1])
    for a_, b_ in zip(xs[:-1], xs[1:]):
        ti = I.mpf([str(float(a_)), str(float(b_))])
        ka = (ti ** p) / gam
        km = I.mpf([0, 0])
        for cj, lam in zip(coeff, lams):
            km += cj * I.exp(-lam * ti)
        bi = I.mpf([str(float(b_)), str(float(b_))])
        ai = I.mpf([str(float(a_)), str(float(a_))])
        body += (bi - ai) * abs(ka - km)
    return float((head + body).b)

def main():
    g5 = json.load(open(os.path.join(HERE, 'round5_results.json')))
    tw = {c['m']: (c['ell'], c['L']) for c in tuned_windows()}
    ts = np.linspace(1e-4, T, 4001)
    dt = ts[1] - ts[0]
    u0v = proto_pulse(ts)
    cap, nrm2 = shape_cap(u0v, dt)
    # F/w max per m (alpha-free part) — LOWER bound direction (grid max,
    # honest values; conservative for the necessary energy bound B_Allee).
    F_over_w_low = {}
    F_over_w_up = {}
    for m in M_ATLAS:
        ell, L = tw[m]
        from compute_round5 import F_over_w, F_over_w_certified
        lam_grid = np.geomspace(ell, L, 50)
        for A in A_LIST:
            Fg = [F_over_w(l, A, u0v, ts, dt, nrm2) for l in lam_grid]
            i0 = int(np.argmax(Fg))
            cand = [lam_grid[i0]]
            if i0 > 0:
                cand.append(lam_grid[i0 - 1])
            if i0 < len(lam_grid) - 1:
                cand.append(lam_grid[i0 + 1])
            Fcert = max(F_over_w_certified(l, A, u0v, ts, dt, nrm2) for l in cand)
            F_over_w_low[(A, m)] = max(Fg)
            F_over_w_up[(A, m)] = Fcert * 1.25
        print(f"  F/w max for m={m} done", flush=True)
    alphas = (0.70, 0.85, 0.95)
    sigmas = (0.05, 0.10, 0.15, 0.20)
    Ehat = {}
    for alpha in alphas:
        best = float('inf')
        for m in sorted(tw):
            ell, L = tw[m]
            U = certified_Ebar_interval_alpha(m, ell, L, alpha)
            best = min(best, U)
            Ehat[(alpha, m)] = best
        print(f"  interval enclosures alpha={alpha}: "
              f"Ehat(4)={Ehat[(alpha,4)]:.4f} Ehat(32)={Ehat[(alpha,32)]:.4f}",
              flush=True)
    M_T = {}
    M_T_down = {}
    for alpha in alphas:
        l1, _ = quad(lambda t: t ** (alpha - 1) / gamma(alpha), 0, T, limit=400)
        M_T[alpha] = l1 + 1.0
        M_T_down[alpha] = l1 + 1.0 - 1e-6
    cells = []
    for alpha in alphas:
        for A in A_LIST:
            rho = X_STAR - (A + ETA)
            for m in M_ATLAS:
                d_rob = M_T_down[alpha] * F_over_w_low[(A, m)]
                d_rob_up = M_T[alpha] * F_over_w_up[(A, m)]
                B_Allee = rho / d_rob
                B_univ = math.sqrt(T) * U_MAX
                B_eff = min(B_Allee, cap, B_univ)
                binding = ('Allee' if B_Allee <= min(cap, B_univ)
                           else 'shape_cap' if cap <= B_univ else 'universal')
                Eh = Ehat[(alpha, m)]
                for sig in sigmas:
                    U = (Eh * B_eff) ** 2 / (2 * sig ** 2)
                    pe = float(0.5 * (1 + math.erf(-math.sqrt(U / 2) / math.sqrt(2))))
                    pe_pin = max(0.0, 0.5 * (1 - math.sqrt(U / 2)))
                    cls = ('hard@0.25' if pe >= 0.25
                           else 'moderate@0.10' if pe >= 0.10 else 'inconclusive')
                    cells.append({'alpha': alpha, 'A': A, 'm': m, 'sigma': sig,
                                  'M_T': M_T[alpha], 'Ehat_IA': Eh,
                                  'd_rob_low': d_rob, 'd_rob_up': d_rob_up,
                                  'B_Allee': B_Allee,
                                  'B_cap': cap, 'B_univ': B_univ,
                                  'B_eff': B_eff, 'binding': binding, 'U': U,
                                  'Pe_gauss': pe, 'Pe_pinsker': pe_pin,
                                  'class': cls})
    out = {'alpha_grid': list(alphas), 'A_grid': list(A_LIST),
           'm_grid': list(M_ATLAS), 'sigma_grid': list(sigmas),
           'protocol': 'pulse (benchmark definition)',
           'cells': cells}
    with open(os.path.join(HERE, 'atlas_cells.json'), 'w') as f:
        json.dump(out, f, indent=1)
    n = len(cells)
    n_hard = sum(1 for c in cells if c['class'] == 'hard@0.25')
    n_mod = sum(1 for c in cells if c['class'] == 'moderate@0.10')
    n_allee = sum(1 for c in cells if c['binding'] == 'Allee')
    worst = min(cells, key=lambda c: c['Pe_gauss'])
    best = max(cells, key=lambda c: c['Pe_gauss'])
    print(f"atlas: {n} cells; hard={n_hard} moderate={n_mod}; "
          f"Allee-binding={n_allee}")
    print(f"weakest cell: {worst}")
    print(f"strongest cell: {best}")

if __name__ == '__main__':
    main()
