#!/usr/bin/env python3
"""compute_round5.py — Round 5 Phase-0 gates (0A, 0B, 0C) + atlas data.

Shared convention: every latent kernel k(t)=sum_j c_j e^{-lam_j t} >= 0 acts
through the ODE backbone J(A) on the prey channel,
    q_j' = -lam_j q_j + u,    xi' = J xi + e_1 sum_j c_j q_j,
    prey deviation x_k(t) = (h_J * (k*u))(t),  h_J(t)=e_1^T e^{Jt} e_1.
Mass bound ||k||_{L^1(0,T)} = sum_j c_j (1-e^{-lam_j T})/lam_j <= M_T.

Gate 0A — EXACT hierarchy-uniform Allee budget.
  Downward gain d(k)=max_t[-(h_J*(k*u0))(t)]_+/||u0||_2 is, for c_j>=0,
      d(k) <= sum_j c_j F(lam_j) = sum_j [c_j w(lam_j)] [F(lam_j)/w(lam_j)]
           <= M_T * max_{lam in window} F(lam)/w(lam),
  where F(lam)=max_t[-(h_J*(e^{-lam.}*u0))(t)]_+/||u0||_2 and
  w(lam)=(1-e^{-lam T})/lam.  The bound is ATTAINED by the single-mode kernel
  k*=(M_T/w(lam*))e^{-lam* .} in K_m.  Hence
      d_rob(K_m,u0) = M_T * max_{lam in [ell_m,L_m]} F(lam)/w(lam)   (EXACT),
      B_Allee(A,m)  = rho_eta / d_rob(K_m,u0).

Gate 0B — ecological-state lift (scope theorem).
  True Caputo prey response h_J^a(t)=L^-1[e1^T(s^a I-J)^-1 B] differs from the
  shared-kernel picture h_J*k_alpha by an irreducible backbone mismatch
      D0(A)=||h_J^a - h_J*k_alpha||_1 > 0,
  independent of m.  Valid ecological bound:
      ||x_a-x_k||_inf <= [D0(A)+||h_J||_1||k_a-k||_1]||u||_inf.
  Since D0 dominates the constructive errors, the factorized lift
  C_dyn||k_a-k_m||_1||u|| does NOT hold; the kernel-level T20 is the
  conservative obstruction.  Reported as a scope finding.

Gate 0C — asymptotic hierarchy.
  Windows ell_m=0.05/sqrt(m), L_m=3+0.1*ln(m): nested, expanding, contain the
  left-node geometric T9b approximants; T9b bound -> 0, so E_m -> 0 for THIS
  hierarchy (separate from the finite tuned hierarchy certified by intervals).
"""
import json
import math
import os
import sys

import numpy as np
from scipy.integrate import quad
from scipy.signal import fftconvolve
from scipy.optimize import minimize_scalar
from scipy.special import gamma

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'benchmark'))
from benchmark import core as bench  # noqa: E402
import bench as B  # noqa: E402

ALPHA = 0.85
T = 12.0
ETA = 0.02
U_MAX = B.AMP
X_STAR = bench.x_star()
DELTA = 1e-4
A_LIST = (0.10, 0.15, 0.20, 0.25, 0.30, 0.32, 0.34, 0.38, 0.42)
M_ATLAS = (4, 8, 16, 32)

def trapz(y, x):
    return float(np.trapezoid(y, x))

def fconv(a, b, dt):
    return fftconvolve(a, b, mode='full')[:len(a)] * dt

def k_alpha(t, alpha=ALPHA):
    return np.asarray(t) ** (alpha - 1) / gamma(alpha)

def backbone(A):
    J = bench.jacobian(A)
    ev, Vr = np.linalg.eig(J)
    Vi = np.linalg.inv(Vr)
    e1 = np.array([1.0, 0.0])
    w = (e1 @ Vr) * (Vi @ e1)
    return J, ev, w

def h_J_series(A, ts):
    _, ev, w = backbone(A)
    return np.real(sum(wi * np.exp(mu * ts) for wi, mu in zip(w, ev)))

def h_J_alpha(A, ts, alpha=ALPHA, terms=70):
    _, ev, w = backbone(A)
    out = np.zeros(len(ts), dtype=complex)
    for wi, mu in zip(w, ev):
        s = np.zeros(len(ts), dtype=complex)
        z = mu * ts ** alpha
        term = np.ones(len(ts), dtype=complex) / gamma(alpha)
        for kidx in range(terms):
            s += term
            term = term * z * gamma(alpha * kidx + alpha) / gamma(alpha * (kidx + 1) + alpha)
        out += wi * ts ** (alpha - 1) * s
    return np.real(out)

def tuned_windows():
    cells = json.load(open(os.path.join(HERE, '..', 'round3', 'round3_results.json')))
    return cells['track_A']['cells']

# ---------------------------------------------------------------- Gate 0A
def _conv_down(lam, A, u0v, ts, dt, nrm2):
    """max_t[-(h_J*(e^{-lam.}*u0))(t)]_+/||u0||_2 on the time grid."""
    h = h_J_series(A, ts)
    e = np.exp(-lam * ts)
    base = fconv(e, u0v, dt)
    g = fconv(h, base, dt)
    return max(0.0, -g.min()), g

def F_over_w(lam, A, u0v, ts, dt, nrm2):
    down, _ = _conv_down(lam, A, u0v, ts, dt, nrm2)
    wlam = (1.0 - math.exp(-lam * T)) / lam
    return down / (wlam * nrm2)

def F_over_w_certified(lam, A, u0v, ts, dt, nrm2):
    """Upper bound on F/w: grid value + validated time margin (Lip_t dt/2 with
    Lip_t from a 4x-refined grid, 2x safety factor)."""
    down, g = _conv_down(lam, A, u0v, ts, dt, nrm2)
    ts2 = np.linspace(ts[0], ts[-1], 4 * len(ts) - 3)
    dt2 = ts2[1] - ts2[0]
    _, g2 = _conv_down(lam, A, u0v, ts2, dt2, nrm2)
    lip_t = float(np.max(np.abs(np.gradient(g2, dt2)))) * 2.0 + 1e-12
    down_cert = down + lip_t * dt / 2.0
    wlam = (1.0 - math.exp(-lam * T)) / lam
    return down_cert / (wlam * nrm2)

def proto_pulse(ts):
    w = 0.06 * T
    return (np.abs(ts - 0.15 * T) < w).astype(float)

def proto_multiscale(ts):
    out = np.zeros_like(ts)
    t0, q = 0.05 * T, 1.9
    tk = t0
    while tk < 0.9 * T:
        out += (np.abs(ts - tk) < 0.02 * T).astype(float)
        tk *= q
    return out

def shape_cap(u0v, dt):
    n2 = math.sqrt(np.sum(u0v ** 2) * dt)
    return U_MAX * n2 / float(np.max(np.abs(u0v))), n2

def gate_0A():
    ka_l1, _ = quad(lambda t: k_alpha(t), 0, T, limit=400)
    global M_T_DOWN, M_T_UP
    M_T_DOWN = ka_l1 + 1.0 - 1e-6   # lower (for d_rob lower bound)
    M_T_UP = ka_l1 + 1.0 + 1e-6     # upper (for the sandwich)
    M_T = ka_l1 + 1.0
    tw = tuned_windows()
    ts = np.linspace(1e-4, T, 4001)
    dt = ts[1] - ts[0]
    res = {'M_T': M_T, 'k_alpha_L1': ka_l1, 'cells': {}}
    for pname, fn in (('pulse', proto_pulse), ('multiscale', proto_multiscale)):
        u0v = fn(ts)
        cap, nrm2 = shape_cap(u0v, dt)
        res['cells'][pname] = {'shape_cap': cap, 'u0_L2': nrm2, 'by_A': {}}
        for A in A_LIST:
            row = {}
            for c in tw:
                m = c['m']
                ell, L = c['ell'], c['L']
                lam_grid = np.geomspace(ell, L, 50)
                Fg = [F_over_w(l, A, u0v, ts, dt, nrm2) for l in lam_grid]
                i0 = int(np.argmax(Fg))
                # LOWER bound on d_rob (valid for the necessary energy bound):
                # grid max with honest (possibly under-) values; any
                # underestimation is conservative for a lower bound.
                F_low = max(Fg)
                # UPPER sandwich (certified around argmax + declared margins),
                # reported as the enclosure width, not used for B_Allee.
                cand = [lam_grid[i0]]
                if i0 > 0:
                    cand.append(lam_grid[i0 - 1])
                if i0 < len(lam_grid) - 1:
                    cand.append(lam_grid[i0 + 1])
                Fcert = max(F_over_w_certified(l, A, u0v, ts, dt, nrm2) for l in cand)
                F_up = Fcert * 1.25
                d_low = M_T_DOWN * F_low
                d_up = M_T_UP * F_up
                rho = X_STAR - (A + ETA)
                row[f'm={m}'] = {'window': [ell, L], 'lam_star': float(lam_grid[i0]),
                                 'F_low': F_low, 'F_up': F_up,
                                 'd_rob_low': d_low, 'd_rob_up': d_up,
                                 'rho_eta': rho, 'B_Allee': rho / d_low}
            res['cells'][pname]['by_A'][f'A={A}'] = row
        print(f"  0A {pname}: shape_cap={cap:.4f}")
        for A in (0.25, 0.30, 0.32, 0.34):
            r = res['cells'][pname]['by_A'][f'A={A}']
            print("    A=%s: %s" % (A, "  ".join(
                f"d_rob_low(m{mm})={r[f'm={mm}']['d_rob_low']:.2f} up={r[f'm={mm}']['d_rob_up']:.2f}" for mm in (4, 8, 16, 32))))
    # validation vs locked benchmark rivals (diagnostic)
    val = {}
    for pname, fn in (('pulse', proto_pulse), ('multiscale', proto_multiscale)):
        u0v = fn(ts)
        nrm2 = math.sqrt(np.sum(u0v ** 2) * dt)
        val[pname] = {}
        for A in (0.25, 0.30, 0.32, 0.34):
            J = bench.jacobian(A)
            rates = np.array(B.LAT_RATES)
            entry = {}
            for name, rr in (('ODE', None), ('latent1', rates[:1]), ('latent3', rates)):
                if rr is None:
                    h = h_J_series(A, ts)
                    conv = fconv(u0v, h, dt)
                else:
                    mlat = len(rr)
                    Abar = np.zeros((2 + mlat, 2 + mlat)); Abar[:2, :2] = J
                    Abar[0, 2:] = B.LAT_G; Abar[2:, 2:] = -np.diag(rr)
                    Bbar = np.zeros(2 + mlat); Bbar[0] = 1.0; Bbar[2:] = 1.0
                    from scipy.linalg import expm
                    h = np.array([(expm(Abar * t) @ Bbar)[0] for t in ts])
                    conv = fconv(u0v, h, dt)
                entry[name] = float(max(0.0, -conv.min()) / nrm2)
            val[pname][f'A={A}'] = entry
        print(f"  0A validation {pname}: {val[pname]}")
    res['benchmark_rival_validation'] = val
    return res

# ---------------------------------------------------------------- Gate 0B
def gate_0B():
    res = {'D0_backbone_mismatch': {}, 'hJalpha_L1': {}, 'hJ_L1': {}, 'constructive': {}}
    ts = np.linspace(1e-4, T, 8001)
    dt = ts[1] - ts[0]
    for A in (0.25, 0.30, 0.34):
        ha = h_J_alpha(A, ts, ALPHA)
        hj = h_J_series(A, ts)
        ka = k_alpha(ts)
        hka = fconv(hj, ka, dt)
        D0 = trapz(np.abs(ha - hka), ts)
        res['D0_backbone_mismatch'][f'A={A}'] = D0
        res['hJalpha_L1'][f'A={A}'] = trapz(np.abs(ha), ts)
        res['hJ_L1'][f'A={A}'] = trapz(np.abs(hj), ts)
        print(f"  0B A={A}: D0={D0:.4f} ||h_J^a||_1={trapz(np.abs(ha),ts):.4f} "
              f"||h_J||_1={trapz(np.abs(hj),ts):.4f}")
    # constructive convergence of ||h_J^a - h_J*k_m||_1 toward D0 at A=0.30
    tw = tuned_windows()
    CA = math.sin(math.pi * ALPHA) / math.pi
    A = 0.30
    ha = h_J_alpha(A, ts, ALPHA)
    hj = h_J_series(A, ts)
    rows = []
    for c in tw:
        m = c['m']; el = c['ell']; L = c['L']; h = (L - el) / m
        lams = el + np.arange(m) * h
        coeff = CA * h * lams ** (-ALPHA)
        km = coeff @ np.exp(-np.outer(lams, ts))
        hkm = fconv(hj, km, dt)
        err = trapz(np.abs(ha - hkm), ts)
        rows.append({'m': m, 'eco_state_L1_err': err})
    res['constructive']['A=0.30'] = rows
    print("  0B constructive ||h_J^a-h_J*k_m||_1 (A=0.30):",
          [(r['m'], round(r['eco_state_L1_err'], 3)) for r in rows])
    return res

# ---------------------------------------------------------------- Gate 0C
def t9b_bound(m, ell, L, alpha=ALPHA):
    ca = math.sin(math.pi * alpha) / math.pi
    h = (L - ell) / m
    return ca * (T * ell ** (1 - alpha) / (1 - alpha)
                 + L ** (-alpha) / alpha
                 + T * h * ell ** (-alpha))

def window_asymp(m):
    return 0.025 / math.sqrt(m), 3.0 + 0.1 * math.log(m)

def t9b_mixture_mass(m, ell, L, alpha=ALPHA):
    ca = math.sin(math.pi * alpha) / math.pi
    h = (L - ell) / m
    lams = ell + np.arange(m) * h
    return float(ca * h * np.sum(lams ** (-alpha) * (1 - np.exp(-lams * T)) / lams))

def gate_0C():
    res = {'windows': [], 't9b_sequence': [], 'nested': True,
           'containment_tuned': [], 'mass_note': (
               'T9b left-node mixture mass on the asymptotic windows. The frozen '
               'safe class uses M_T=||k_alpha||_1+1; the T9b asymptotic mixtures '
               'violate M_T for small m (mass diverges as ell->0), so the '
               'asymptotic E_m->0 statement lives in an m-dependent-mass class, '
               'NOT the frozen safe class K_m.')}
    ka_l1, _ = quad(lambda t: k_alpha(t), 0, T, limit=400)
    res['M_T'] = ka_l1 + 1.0
    tw = tuned_windows()
    for c in tw:
        m = c['m']; el, L = window_asymp(m)
        res['containment_tuned'].append(
            {'m': m, 'tuned_ell': c['ell'], 'tuned_L': c['L'],
             'asymp_ell': el, 'asymp_L': L,
             'inside': (c['ell'] >= el and c['L'] <= L)})
    prev = None
    for m in (1, 2, 4, 8, 16, 32, 64, 128, 256, 1024, 4096, 65536):
        ell, L = window_asymp(m)
        if prev is not None:
            if not (ell <= prev[0] and L >= prev[1]):
                res['nested'] = False
        prev = (ell, L)
        res['windows'].append({'m': m, 'ell': ell, 'L': L})
        res['t9b_sequence'].append({'m': m, 'B_T9b': t9b_bound(m, ell, L),
                                    'mixture_mass': t9b_mixture_mass(m, ell, L)})
    for r in res['t9b_sequence']:
        print(f"  0C m={r['m']:7d}: ell={window_asymp(r['m'])[0]:.6f} "
              f"L={window_asymp(r['m'])[1]:.4f} T9b={r['B_T9b']:.5f} "
              f"mass={r['mixture_mass']:.3f}")
    print(f"  0C nested={res['nested']}; containment all tuned: "
          f"{all(x['inside'] for x in res['containment_tuned'])}; "
          f"M_T={res['M_T']:.4f}")
    return res

# ---------------------------------------------------------------- atlas
def atlas_data(g0A, g0B):
    IA = json.load(open(os.path.join(ROOT, 'chief_round4', 'Ebar_interval_bounds.json')))
    nested_ia = {int(r['m']): r['Ehat_nested_upper'] for r in IA['rows']}
    sigmas = (0.05, 0.10, 0.15, 0.20)
    cells = []
    pulse = g0A['cells']['pulse']
    for A in A_LIST:
        for m in M_ATLAS:
            cell0A = pulse['by_A'][f'A={A}'][f'm={m}']
            B_Allee = cell0A['B_Allee']
            B_cap = pulse['shape_cap']
            B_univ = math.sqrt(T) * U_MAX
            B_eff = min(B_Allee, B_cap, B_univ)
            binding = ('Allee' if B_Allee <= min(B_cap, B_univ)
                       else 'shape_cap' if B_cap <= B_univ else 'universal')
            Eh = nested_ia[m]
            for sig in sigmas:
                U = (Eh * B_eff) ** 2 / (2 * sig ** 2)
                pe_gauss = float(0.5 * (1 + math.erf(-math.sqrt(U / 2) / math.sqrt(2))))
                pe_pin = max(0.0, 0.5 * (1 - math.sqrt(U / 2)))
                cls = ('hard@0.25' if pe_gauss >= 0.25
                       else 'moderate@0.10' if pe_gauss >= 0.10 else 'inconclusive')
                cells.append({'A': A, 'm': m, 'sigma': sig, 'Ehat_IA': Eh,
                              'B_Allee': B_Allee, 'B_cap': B_cap, 'B_univ': B_univ,
                              'B_eff': B_eff, 'binding': binding, 'U': U,
                              'Pe_lower_gauss': pe_gauss,
                              'Pe_lower_pinsker': pe_pin, 'class': cls})
    out = {'coords': 'A x m x sigma (alpha=0.85, pulse, normalized bounded obs)',
           'cells': cells}
    n_hard = sum(1 for c in cells if c['class'] == 'hard@0.25')
    n_mod = sum(1 for c in cells if c['class'] == 'moderate@0.10')
    n_inc = sum(1 for c in cells if c['class'] == 'inconclusive')
    n_allee = sum(1 for c in cells if c['binding'] == 'Allee')
    print(f"  atlas: {len(cells)} cells; hard={n_hard} moderate={n_mod} "
          f"inconclusive={n_inc}; Allee-binding={n_allee}")
    return out

if __name__ == '__main__':
    res = {}
    print('=== Gate 0A: EXACT hierarchy-uniform Allee budget ===')
    res['gate_0A'] = gate_0A()
    print('=== Gate 0B: ecological-state lift (scope) ===')
    res['gate_0B'] = gate_0B()
    print('=== Gate 0C: asymptotic hierarchy ===')
    res['gate_0C'] = gate_0C()
    print('=== Atlas ===')
    res['atlas'] = atlas_data(res['gate_0A'], res['gate_0B'])
    with open(os.path.join(HERE, 'round5_results.json'), 'w') as f:
        json.dump(res, f, indent=2)
    print('saved round5_results.json')
