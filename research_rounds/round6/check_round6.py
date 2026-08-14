#!/usr/bin/env python3
"""check_round6.py — independent float validation of the Round-6 certificate.

For each certified cell (A, m) in round6_results*.json:
  1. reconstruct the constructed integer-order rival
         g_m(t) = 2 Re[Pcoef e^{s0 t}] + sum_j v_j e^{-rhat_j t}
     from the JSON nodes (exact 2-dim pole block + first-order modes);
  2. evaluate the TRUE fractional impulse response
         g_alpha(t) = 2 Re[ w1 t^{a-1} E_{a,a}(lambda t^a) ]
     by the Mittag-Leffler series (independent of the certifier's
     pole/branch-cut route);
  3. trapezoid L1(0,T) distance on a fine grid must be <= E_upper.

Also re-validates the pole/branch decomposition itself against the series at
scattered times (QUADPACK used HERE ONLY as a float cross-check, never as a
certificate), and checks the T24 sandwich d_low <= d_up.

Exit code 0 iff every check passes.
"""
import glob
import json
import math
import os
import sys

import numpy as np
from scipy.integrate import quad
from scipy.special import gamma as G

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA, T = 0.85, 12.0

sys.path.insert(0, os.path.join(HERE, '..', '..', 'benchmark'))
import core as bench  # noqa: E402


def eig_w(A):
    J = bench.jacobian(A)
    tr = J[0, 0]
    det = -J[0, 1]*J[1, 0]
    disc = complex(tr*tr - 4*det)
    l1 = (tr + np.sqrt(disc))/2
    l2 = (tr - np.sqrt(disc))/2
    return l1, l1/(l1 - l2)


def ml_term(t, lam, terms=160):
    z = lam*t**ALPHA
    s = 0j
    term = 1.0/G(ALPHA)
    for k in range(terms):
        s += term
        term = term*z*G(ALPHA*k + ALPHA)/G(ALPHA*(k + 1) + ALPHA)
    return t**(ALPHA - 1)*s


def g_alpha(ts, lam, w1):
    return np.array([2*(w1*ml_term(t, lam)).real for t in ts])


def main():
    files = sorted(glob.glob(os.path.join(HERE, 'round6_results*.json')))
    if not files:
        print('no results json found')
        return 1
    failures = 0
    checks = 0
    for fp in files:
        res = json.load(open(fp))
        for Akey, cell in res['cells'].items():
            Aval = float(Akey.split('=')[1])
            lam, w1 = eig_w(Aval)
            # cross-check certified backbone constants
            assert abs(lam.real - cell['lambda'][0]) < 1e-10
            assert abs(lam.imag - cell['lambda'][1]) < 1e-10
            s0 = abs(lam)**(1/ALPHA)*np.exp(1j*np.angle(lam)/ALPHA)
            assert abs(s0.real - cell['s0'][0]) < 1e-10
            Pcoef = w1*(s0/(ALPHA*lam))
            # decomposition spot-check (float, independent route)
            def phi(r):
                return (1/math.pi)*r**ALPHA*math.sin(ALPHA*math.pi) / \
                    (r**(2*ALPHA) - 2*lam*r**ALPHA*math.cos(ALPHA*math.pi) + lam*lam)
            for t in (0.2, 1.7, 9.0):
                re, _ = quad(lambda r: (np.exp(-r*t)*2*(w1*phi(r)).real), 0, np.inf,
                             limit=400)
                v_dec = 2*(Pcoef*np.exp(s0*t)).real + re
                v_ser = 2*(w1*ml_term(t, lam)).real
                assert abs(v_dec - v_ser) < 1e-8, (Akey, t, v_dec, v_ser)
            # per-budget L1 check
            ts = np.linspace(1e-6, T, 48001)
            ga = g_alpha(ts, lam, w1)
            for mkey, cert in cell['budgets'].items():
                gm = 2*(Pcoef*np.exp(s0*ts)).real
                for nd in cert['nodes']:
                    gm = gm + nd['v']*np.exp(-nd['rhat']*ts)
                l1 = float(np.trapezoid(np.abs(ga - gm), ts))
                ok = l1 <= cert['E_upper']*(1 + 1e-9)
                al = cert['allee']
                ok2 = al['d_low'] <= al['d_up']*(1 + 1e-12)
                checks += 1
                status = 'OK ' if (ok and ok2) else 'FAIL'
                if not (ok and ok2):
                    failures += 1
                print(f'{status} {Akey} {mkey}: float L1={l1:.6f} <= '
                      f'E_upper={cert["E_upper"]:.6f} '
                      f'(ratio {l1/cert["E_upper"]:.3f}) '
                      f'd_low={al["d_low"]:.3f} <= d_up={al["d_up"]:.3f}')
    print(f'{checks} checks, {failures} failures')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
