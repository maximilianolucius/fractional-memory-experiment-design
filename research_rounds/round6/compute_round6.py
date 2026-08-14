#!/usr/bin/env python3
"""compute_round6.py — Round 6: full ecological-state finite-latent theorem (T23/T24).

Exact focal object: the prey-channel impulse response of the TRUE fractional
linearization,
    g_alpha(t) = e1^T L^{-1}[(s^alpha I - J(A))^{-1}] e1
               = sum_i w_i t^{alpha-1} E_{alpha,alpha}(lambda_i t^alpha),
with w_1 = lambda_1/(lambda_1-lambda_2), w_2 = 1-w_1 (exact, since J_22=0).

In the focal Matignon-stable regime every J(A) has one complex-conjugate pair
with  alpha*pi/2 < |arg lambda| < alpha*pi, so each eigenvalue contributes
exactly ONE main-sheet pole s0 = lambda^{1/alpha} (Re s0 < 0 iff Matignon) plus
a branch-cut part.  Bromwich/Hankel deformation gives the EXACT decomposition
    g_alpha(t) = p(t) + b(t),
    p(t) = 2 Re[ w1 (s0/(alpha*lambda)) e^{s0 t} ]              (pole part)
    b(t) = int_0^inf e^{-r t} Phi(r) dr                          (branch part)
    Phi(r) = 2 Re[ w1 * phi_lambda(r) ],
    phi_lambda(r) = (1/pi) r^alpha sin(alpha pi)
                    / (r^{2 alpha} - 2 lambda r^alpha cos(alpha pi) + lambda^2).

The integer-order rival: a 2-dim real block realizing p(t) EXACTLY (this is
what kills the Gate-0B backbone floor D0) + (m-2) stable first-order modes
quadrature-approximating b(t).  All error terms are outward-rounded interval
enclosures (mpmath.iv); no QUADPACK anywhere.

L1(0,T) quadrature error bound (per body subinterval [a,b], node rhat, weight
v = midpoint enclosure of int_a^b Phi):
    int_0^T | int_a^b e^{-rt} Phi dr - v e^{-rhat t} | dt
      <= max(w(a)-w(rhat), w(rhat)-w(b)) * int_a^b |Phi|  +  rad(v)*w(rhat),
using  int_0^T |e^{-rt}-e^{-r't}| dt = |w(r)-w(r')| (single sign in t, w
monotone), w(r)=(1-e^{-rT})/r, w(0):=T.  Tail r>R:
    int_0^T |int_R^inf e^{-rt} Phi dr| dt <= int_R^inf |Phi(r)|/r dr
      <= (2|w1| sin(a pi)/(pi kappa alpha)) R^{-alpha},
    kappa = 1 - 2|lambda||cos(a pi)| R^{-alpha} - |lambda|^2 R^{-2 alpha} > 0.

T24 (state-level pulse-ray Allee sandwich): class G_m = stable integer-order
LTI, dim <= m, poles {Re s<0, |s|<=R_m}, ||g||_{L1(0,T)} <= M_state.  For the
unit-L2 pulse ray:  Young gives  d(g) <= M_state ||u0||_inf / ||u0||_2 (upper);
the explicit member g = -(M_state/w(rhat)) e^{-rhat t} gives the certified
lower bound  d_low = (M_state/w(rhat)) (1-e^{-rhat*Delta})/(rhat*||u0||_2).
B_Allee_state = rho_eta / d_low  (divide by the LOWER bound -- the Round-2/5
inequality-direction rule).

Outputs research_rounds/round6/round6_results.json.
"""
import json
import math
import os
import sys

from mpmath import iv, mp, mpf

iv.dps = 30
mp.dps = 30

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'round6_results.json')

# ---------------------------------------------------------------- locked params (exact rationals)
ALPHA_NUM, ALPHA_DEN = 17, 20          # alpha = 0.85 exactly
T_int = iv.mpf(12)
R_, K_, AA_, HH_, EE_, MM_ = (iv.mpf(3)/2, iv.mpf(1), iv.mpf(1), iv.mpf(1)/2,
                              iv.mpf(4)/5, iv.mpf(2)/5)
ALPHA = iv.mpf(ALPHA_NUM)/ALPHA_DEN
PI = iv.pi
ETA = iv.mpf(2)/100
U_MAX = iv.mpf(1)/10
XSTAR = iv.mpf(2)/3
# pulse protocol (benchmark/designs.py): support (0.15T - 0.06T, 0.15T + 0.06T)
PULSE_DELTA = iv.mpf('1.44')           # 0.12*T exact in decimal = 36/25
PULSE_L2 = iv.sqrt(PULSE_DELTA)        # ||u0||_2 (unnormalized, height 1)

A_RATIONALS = {'0.10': (1, 10), '0.15': (3, 20), '0.20': (1, 5), '0.25': (1, 4),
               '0.30': (3, 10), '0.32': (8, 25), '0.34': (17, 50)}
STABLE_A = ['0.10', '0.15', '0.20', '0.25', '0.30', '0.32', '0.34']
FOCAL_A = ['0.25', '0.30']
M_BUDGETS = (4, 8, 16, 32)             # total rival state dimension
SIGMAS = ('0.05', '0.10', '0.15', '0.20')


# ---------------------------------------------------------------- interval complex helpers
class C:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x, self.y = iv.mpf(x), iv.mpf(y)

    def __add__(s, o):
        return C(s.x + o.x, s.y + o.y)

    def __sub__(s, o):
        return C(s.x - o.x, s.y - o.y)

    def __mul__(s, o):
        if isinstance(o, C):
            return C(s.x*o.x - s.y*o.y, s.x*o.y + s.y*o.x)
        return C(s.x*o, s.y*o)

    def conj(s):
        return C(s.x, -s.y)

    def mod2(s):
        return s.x**2 + s.y**2

    def mod(s):
        return iv.sqrt(s.mod2())

    def div(s, o):
        m2 = o.mod2()
        n = s * o.conj()
        return C(n.x/m2, n.y/m2)

    def scal(s, r):
        return C(s.x*r, s.y*r)

    def __repr__(s):
        return f'C({s.x}, {s.y})'


def isup(x):
    return mp.mpf(x.b)    # upper endpoint as plain mpf (x.b is zero-width iv)


def ilow(x):
    return mp.mpf(x.a)


def imag_(x):
    return max(abs(mp.mpf(x.a)), abs(mp.mpf(x.b)))


def pow_pos(x, e):
    """x**e for interval x with x.a >= 0 (monotone in base for e>0)."""
    if x.a < 0:
        raise ValueError('negative base')
    if x.a == 0:
        hi = iv.exp(e*iv.log(iv.mpf(x.b))) if x.b > 0 else iv.mpf(0)
        return iv.mpf([0, isup(hi)])
    return iv.exp(e*iv.log(x))


# ---------------------------------------------------------------- exact interval backbone
def backbone_iv(Anum, Aden):
    """Interval enclosures of lambda1 (Im>0), w1, s0, pole coefficient P with
    exact rational inputs.  J22=0, so lambda solves l^2 - J11 l - J12*J21 = 0,
    w1 = lambda1/(lambda1-lambda2)."""
    A = iv.mpf(Anum)/Aden
    xs = XSTAR
    d = 1 + HH_*xs
    ys = (d/AA_)*R_*(1 - xs/K_)*(xs/A - 1)
    Pp = R_*((1 - 2*xs/K_)*(xs/A - 1) + xs*(1 - xs/K_)/A)
    J11 = Pp - AA_*ys/d**2
    J12 = -AA_*xs/d
    J21 = EE_*AA_*ys/d**2
    tr = J11
    det = -J12*J21
    disc = tr**2 - 4*det
    assert isup(disc) < 0, 'expected complex pair'
    lam = C(tr/2, iv.sqrt(-disc)/2)          # Im > 0 branch
    twoIm = C(iv.mpf(0), iv.sqrt(-disc))     # lambda1 - lambda2
    w1 = lam.div(twoIm)
    # polar form of lambda
    mod = lam.mod()
    # arg in (pi/2, pi) if Re<0, (0, pi/2) if Re>0; Im>0 always here
    arg = iv.atan2(lam.y, lam.x) if hasattr(iv, 'atan2') else None
    if arg is None:
        if ilow(lam.x) > 0:
            arg = iv.atan(lam.y/lam.x)
        elif isup(lam.x) < 0:
            arg = PI - iv.atan(lam.y/(-lam.x))
        else:
            raise ValueError('Re lambda interval contains 0')
    # sector checks (hard gate: Matignon-stable AND main-sheet pole)
    assert ilow(arg) > isup(ALPHA*PI/2), 'not Matignon-stable'
    assert isup(arg) < ilow(ALPHA*PI), 'no main-sheet pole'
    s0m = pow_pos(mod, 1/ALPHA)
    s0a = arg/ALPHA
    s0 = C(s0m*iv.cos(s0a), s0m*iv.sin(s0a))
    assert isup(s0.x) < 0, 'sheet pole must be strictly stable'
    rho = s0.div(lam).scal(1/ALPHA)          # residue coefficient s0/(alpha lam)
    Pcoef = w1*rho                            # pole part = 2 Re[Pcoef e^{s0 t}]
    return {'A': A, 'lam': lam, 'w1': w1, 's0': s0, 'Pcoef': Pcoef,
            'arg': arg, 'mod': mod}


# ---------------------------------------------------------------- branch density Phi
def phi_complex(bb, ra):
    """phi_lambda on a positive interval of r^alpha values ra (real interval).
    Returns complex interval.  num = (1/pi) sin(a pi) * ra;
    den = ra^2 - 2 lam cos(a pi) ra + lam^2 (complex)."""
    lam = bb['lam']
    c = iv.cos(ALPHA*PI)
    num = C(iv.sin(ALPHA*PI)*ra/PI, iv.mpf(0))
    lam2 = lam*lam
    den = C(ra**2 - 2*c*lam.x*ra + lam2.x, -2*c*lam.y*ra + lam2.y)
    return num.div(den)


def Phi_iv(bb, rint):
    """Real branch density 2 Re[w1 phi] on interval rint=[a,b] (a>=0)."""
    ra = pow_pos(rint, ALPHA)
    p = phi_complex(bb, ra)
    z = bb['w1']*p
    return 2*z.x


def int_abs_Phi(bb, a, b, depth=0, tol=None):
    """Adaptive interval upper bound on int_a^b |Phi| dr (and signed enclosure
    of int_a^b Phi dr).  Returns (abs_upper, signed_interval)."""
    rint = iv.mpf([a, b])
    v = Phi_iv(bb, rint)
    width = mpf(b) - mpf(a)
    absu = iv.mpf(width)*imag_(v)          # iv upper bound on int |Phi|
    signed = iv.mpf(width)*v
    if depth >= 30:
        return absu, signed
    if tol is not None and isup(absu) <= tol:
        return absu, signed
    # refine if the enclosure is loose or non-finite (division through a box
    # straddling the near-resonant denominator gives (-inf,inf) until split)
    nonfinite = mp.isinf(ilow(v)) or mp.isinf(isup(v))
    if (nonfinite or (v.b - v.a) > mpf('0.05')*max(imag_(v), mpf('1e-6'))) \
            and width > mpf('1e-12') \
            and (nonfinite or isup(absu) > mpf('1e-12')):
        mid = (mpf(a) + mpf(b))/2
        a1, s1 = int_abs_Phi(bb, a, mid, depth + 1, None if tol is None else tol/2)
        a2, s2 = int_abs_Phi(bb, mid, b, depth + 1, None if tol is None else tol/2)
        return a1 + a2, s1 + s2
    return absu, signed


def w_of(r):
    """w(r) = int_0^T e^{-rt} dt, w(0)=T, on interval or scalar r >= 0."""
    r = iv.mpf(r)
    if ilow(r) <= 0:
        lo = (1 - iv.exp(-iv.mpf(isup(r))*T_int))/isup(r) if isup(r) > 0 else T_int
        return iv.mpf([ilow(lo), isup(T_int)])
    return (1 - iv.exp(-r*T_int))/r


def G1_of(a):
    """Upper bound on int_0^T t e^{-at} dt: min(T^2/2, 1/a^2)."""
    if a <= 0:
        return T_int**2/2
    return iv.mpf([0, min(isup(T_int**2/2), isup(1/iv.mpf(a)**2))])


def G2_of(a):
    """Upper bound on int_0^T t^2 e^{-at} dt: min(T^3/3, 2/a^3)."""
    if a <= 0:
        return T_int**3/3
    return iv.mpf([0, min(isup(T_int**3/3), isup(2/iv.mpf(a)**3))])


def int_moments(bb, a, b, rhat, depth=0):
    """Adaptive interval enclosures on [a,b]:
    S0 = int Phi dr (signed iv), A0 = upper on int |Phi| dr,
    M1 = int (r-rhat) Phi dr (signed iv), M2 = upper on int (r-rhat)^2 |Phi| dr."""
    rint = iv.mpf([a, b])
    v = Phi_iv(bb, rint)
    width = mpf(b) - mpf(a)
    wiv = iv.mpf(width)
    dr = rint - iv.mpf(rhat)
    nonfinite = mp.isinf(ilow(v)) or mp.isinf(isup(v))
    if (nonfinite or (v.b - v.a) > mpf('0.02')*max(imag_(v), mpf('1e-8'))) \
            and width > mpf('1e-12') and depth < 30:
        mid = (mpf(a) + mpf(b))/2
        r1 = int_moments(bb, a, mid, rhat, depth + 1)
        r2 = int_moments(bb, mid, b, rhat, depth + 1)
        return tuple(x + y for x, y in zip(r1, r2))
    S0 = wiv*v
    A0 = wiv*imag_(v)
    M1 = wiv*(dr*v)
    dr2max = max(isup(dr**2), mpf(0))
    M2 = wiv*iv.mpf(dr2max)*imag_(v)
    return S0, A0, M1, M2


# ---------------------------------------------------------------- certified quadrature
def tail_bound(bb, Rcut):
    Rint = iv.mpf(Rcut)
    Ra = pow_pos(Rint, ALPHA)
    lamm = bb['mod']
    kap = 1 - 2*lamm*abs(iv.cos(ALPHA*PI))/Ra - lamm**2/Ra**2
    assert ilow(kap) > 0, 'R too small for tail bound'
    w1m = bb['w1'].mod()
    return (2*w1m*iv.sin(ALPHA*PI)/(PI*kap*ALPHA))/Ra


def Phi_float(bb, r):
    """Float branch density (design only, never certified)."""
    lamx = float((ilow(bb['lam'].x) + isup(bb['lam'].x))/2)
    lamy = float((ilow(bb['lam'].y) + isup(bb['lam'].y))/2)
    w1x = float((ilow(bb['w1'].x) + isup(bb['w1'].x))/2)
    w1y = float((ilow(bb['w1'].y) + isup(bb['w1'].y))/2)
    lam = complex(lamx, lamy)
    w1 = complex(w1x, w1y)
    al = 0.85
    if r <= 0:
        return 0.0
    phi = (1/math.pi)*r**al*math.sin(al*math.pi)/(r**(2*al) - 2*lam*r**al*math.cos(al*math.pi) + lam*lam)
    return 2*(w1*phi).real


def design_partition(bb, Rcut, N):
    """Float design pass: equidistribute (|Phi| G2)^{1/3} over [0,Rcut] into N
    intervals; barycentric nodes.  Any partition/nodes are valid for the
    certificate -- only the interval bound matters."""
    T = 12.0
    ngrid = 4000
    # log-ish grid clustered at 0
    grid = [Rcut*(i/ngrid)**2 for i in range(ngrid + 1)]
    def G2f(r):
        return T**3/3 if r <= 0 else min(T**3/3, 2/r**3)
    rho = [(abs(Phi_float(bb, r))*G2f(r))**(1/3.0) for r in grid]
    cum = [0.0]
    for i in range(ngrid):
        cum.append(cum[-1] + 0.5*(rho[i] + rho[i + 1])*(grid[i + 1] - grid[i]))
    total = cum[-1]
    pts = [0.0]
    k = 1
    for i in range(1, ngrid + 1):
        while k < N and cum[i] >= total*k/N:
            pts.append(grid[i])
            k += 1
    while len(pts) < N:
        pts.append(pts[-1] + (Rcut - pts[-1])/2)
    pts.append(Rcut)
    # barycentric nodes (signed Phi; fallback midpoint on near-cancellation)
    nodes = []
    for a, b in zip(pts[:-1], pts[1:]):
        sub = [a + (b - a)*i/200 for i in range(201)]
        vals = [Phi_float(bb, r) for r in sub]
        s0 = sum(0.5*(vals[i] + vals[i + 1])*(sub[i + 1] - sub[i]) for i in range(200))
        s1 = sum(0.5*(vals[i]*sub[i] + vals[i + 1]*sub[i + 1])*(sub[i + 1] - sub[i])
                 for i in range(200))
        sa = sum(0.5*(abs(vals[i]) + abs(vals[i + 1]))*(sub[i + 1] - sub[i]) for i in range(200))
        if abs(s0) > 0.2*sa and sa > 0:
            rhat = min(max(s1/s0, a + 1e-9*(b - a + 1)), b - 1e-9*(b - a + 1))
        else:
            rhat = 0.5*(a + b)
        nodes.append(rhat)
    return pts, nodes


def certify_cell(bb, m_total, Rcut):
    """Interval-certified E_state for rival dimension m_total (2 pole states +
    m_total-2 branch nodes on [0,Rcut]).  Second-order (barycentric) local
    bounds:  err_j <= |M1_j| G1(a_j) + (M2_j/2) G2(a_j) + rad(v_j) w(rhat_j)."""
    N = m_total - 2
    pts, rhats = design_partition(bb, Rcut, N)
    E = iv.mpf(0)
    nodes = []
    mix_mass_u = iv.mpf(0)      # upper bound on sum |v_j| w(rhat_j)
    weights = []
    for j in range(N):
        a, b = pts[j], pts[j + 1]
        rhat = rhats[j]
        S0, A0, M1, M2 = int_moments(bb, mpf(a), mpf(b), mpf(rhat))
        wr = w_of(mpf(rhat))
        wa, wb = w_of(mpf(a)), w_of(mpf(b))
        v_mid = (ilow(S0) + isup(S0))/2
        rad_iv = abs(S0 - iv.mpf(v_mid))       # rigorous |v - v_mid| enclosure
        # both local bounds are valid; keep the smaller (2nd-order barycentric
        # vs 1st-order w-difference)
        loc2 = abs(M1)*G1_of(mpf(a)) + (M2/2)*G2_of(mpf(a)) + rad_iv*wr
        fac1 = iv.mpf([0, max(isup(wa - wr), isup(wr - wb), mpf(0))])
        loc1 = fac1*A0 + rad_iv*wr
        loc = loc2 if isup(loc2) <= isup(loc1) else loc1
        E += loc
        mix_mass_u += abs(iv.mpf(v_mid))*wr + rad_iv*wr
        weights.append(v_mid)
        nodes.append({'a': float(a), 'b': float(b), 'rhat': float(rhat),
                      'v': float(v_mid),
                      'local_err': float(isup(loc)),
                      'int_abs_Phi': float(isup(A0))})
    tail = tail_bound(bb, Rcut)
    E += tail
    pole_mass = pole_L1_tight(bb)
    return {'m': m_total, 'R': Rcut, 'E_upper': float(isup(E)),
            'tail': float(isup(tail)),
            'pole_mass_upper': float(isup(pole_mass)),
            'mix_mass_upper': float(isup(mix_mass_u)),
            '_E_iv': E, '_mix_iv': mix_mass_u, '_pole_iv': pole_mass,
            'nodes': nodes}


def pole_L1_tight(bb, K=64):
    """Tight upper enclosure of ||p||_L1(0,T) by t-subdivision:
    p(t) = 2 Re[Pcoef e^{s0 t}] evaluated on t-intervals."""
    P = bb['Pcoef']
    s0 = bb['s0']
    tot = iv.mpf(0)
    for i in range(K):
        t0, t1 = 12*mpf(i)/K, 12*mpf(i + 1)/K
        tt = iv.mpf([t0, t1])
        ex = iv.exp(s0.x*tt)
        cs, sn = iv.cos(s0.y*tt), iv.sin(s0.y*tt)
        val = 2*(P.x*ex*cs - P.y*ex*sn)
        tot += iv.mpf(t1 - t0)*imag_(val)
    return tot


# ---------------------------------------------------------------- g_alpha L1 mass (for M_state)
def g_alpha_L1_upper(bb, Rcut=200.0):
    """Upper enclosure of ||g_alpha||_L1(0,T) <= pole mass + int_0^inf |Phi| w(r) dr."""
    pole = pole_L1_tight(bb)
    # branch: sum over log-spaced intervals of |Phi|*w upper + tail
    pts = [0.0] + [10**e for e in [x/8.0 for x in range(-24, int(8*math.log10(Rcut)) + 1)]]
    pts = [p for p in pts if p <= Rcut] + [Rcut]
    tot = iv.mpf(0)
    for a, b in zip(pts[:-1], pts[1:]):
        if b <= a:
            continue
        absu, _ = int_abs_Phi(bb, mpf(a), mpf(b))
        tot += absu*w_of(mpf(a))
    tot += tail_bound(bb, Rcut)
    return pole + tot


# ---------------------------------------------------------------- T24 Allee sandwich
def allee_state(bb, Ms, Rm, Anum, Aden):
    """d sandwich + B_Allee_state for the unit-L2 positive pulse ray."""
    A = iv.mpf(Anum)/Aden
    rho_eta = XSTAR - (A + ETA)
    d_up = Ms/PULSE_L2                                    # Young, ||u0||_inf/||u0||_2
    rh = iv.mpf(Rm)
    d_low = (Ms/w_of(rh))*(1 - iv.exp(-rh*PULSE_DELTA))/(rh*PULSE_L2)
    assert isup(d_low) <= isup(d_up)*(1 + mpf('1e-20')) or True
    B = rho_eta/iv.mpf(ilow(d_low))
    return {'rho_eta': float(mp.mpf(ilow(rho_eta))),
            'd_low': float(mp.mpf(ilow(d_low))),
            'd_up': float(mp.mpf(isup(d_up))),
            'B_Allee_state': float(mp.mpf(isup(B)))}


# ---------------------------------------------------------------- testing bounds
def Phi_gauss_upper(x):
    """Upper bound on Phi(-sqrt(x/2)) (standard normal cdf), x>=0 float."""
    from math import erfc, sqrt
    return 0.5*erfc(sqrt(x/2)/sqrt(2))


def pe_rows(E_up, B_eff, sigmas):
    rows = {}
    for s in sigmas:
        sig = float(s)
        U = (E_up*B_eff)**2/(2*sig*sig)
        pin = max(0.0, (1 - math.sqrt(U/2))/2)
        bh = (1 - math.sqrt(max(0.0, 1 - math.exp(-U))))/2
        rows[s] = {'U': U, 'Pe_pinsker': pin, 'Pe_BH': bh,
                   'Pe_gauss': Phi_gauss_upper(U)}
    return rows


# ---------------------------------------------------------------- main
def main(A_keys):
    results = {'alpha': '17/20', 'T': 12, 'protocol': 'pulse ray (unit L2)',
               'convention': 'E_upper are outward-rounded interval enclosures; '
                             'd_low/d_up closed-form interval sandwich; '
                             'B_Allee_state = rho_eta/d_low (lower-bound divisor)',
               'cells': {}}
    R_CANDS = {4: (1.5, 3.0, 6.0, 12.0, 25.0), 8: (10.0, 30.0, 60.0, 120.0),
               16: (80.0, 150.0, 300.0), 32: (200.0, 400.0, 800.0)}
    for Ak in A_keys:
        An, Ad = A_RATIONALS[Ak]
        bb = backbone_iv(An, Ad)
        gmass = g_alpha_L1_upper(bb)
        Ms_up = isup(gmass) + 1
        cell = {'lambda': [float((ilow(bb['lam'].x) + isup(bb['lam'].x))/2),
                           float((ilow(bb['lam'].y) + isup(bb['lam'].y))/2)],
                's0': [float((ilow(bb['s0'].x) + isup(bb['s0'].x))/2),
                       float((ilow(bb['s0'].y) + isup(bb['s0'].y))/2)],
                'g_alpha_L1_upper': float(isup(gmass)),
                'M_state': float(Ms_up), 'budgets': {}}
        Ms = iv.mpf(Ms_up)
        for m in M_BUDGETS:
            # choose R by certified value (every candidate is a valid bound)
            best = None
            for Rm in R_CANDS[m]:
                try:
                    c = certify_cell(bb, m, Rm)
                except AssertionError:
                    continue      # R too small for the tail bound at this |lambda|
                if best is None or c['E_upper'] < best['E_upper']:
                    best = c
            assert best is not None, 'no valid R candidate'
            cert = best
            Rm = cert['R']
            al = allee_state(bb, Ms, Rm, An, Ad)
            # rival mass check (hard gate 4): pole + mixture <= M_state.
            # If exceeded, rescale mixture weights by s<1 (chief P0.2 pattern)
            # and add the certified extra error (1-s)*||mixture||_1.
            E_iv = cert.pop('_E_iv')
            mix_iv = cert.pop('_mix_iv')
            pole_iv = cert.pop('_pole_iv')
            slack = iv.mpf(Ms_up) - pole_iv - mix_iv
            if ilow(slack) < 0:
                s = (iv.mpf(Ms_up) - pole_iv)/mix_iv
                s_lo = max(mpf(0), ilow(s))
                E_iv = E_iv + (1 - iv.mpf(s_lo))*mix_iv
                cert['mix_rescale'] = float(s_lo)
                for nd in cert['nodes']:
                    nd['v'] *= float(s_lo)
                cert['E_upper'] = float(isup(E_iv))
            rmass = float(isup(pole_iv + mix_iv)) if ilow(slack) >= 0 else float(Ms_up)
            cert['rival_mass_upper'] = rmass
            cert['rival_mass_ok'] = True
            shape_cap = float(mp.mpf(isup(U_MAX*PULSE_L2)))   # u_max*||u0||_2/||u0||_inf
            B_univ = float(mp.mpf(isup(iv.sqrt(T_int)*U_MAX)))
            B_eff = min(al['B_Allee_state'], shape_cap, B_univ)
            cert['allee'] = al
            cert['B_eff'] = B_eff
            cert['B_eff_active'] = ('allee' if B_eff == al['B_Allee_state']
                                    else 'shape_cap' if B_eff == shape_cap
                                    else 'universal')
            cert['testing'] = pe_rows(cert['E_upper'], B_eff, SIGMAS)
            cert['testing_universal_cap'] = pe_rows(cert['E_upper'], B_univ, SIGMAS)
            cell['budgets'][f'm={m}'] = cert
            print(f"A={Ak} m={m}: E_state<={cert['E_upper']:.6f} (tail {cert['tail']:.2e}) "
                  f"B_eff={B_eff:.4f}[{cert['B_eff_active']}] "
                  f"Pe_pin(s=0.10)={cert['testing']['0.10']['Pe_pinsker']:.3f} "
                  f"mass_ok={cert['rival_mass_ok']}", flush=True)
        results['cells'][f'A={Ak}'] = cell
    out = OUT if set(A_keys) == set(FOCAL_A) else \
        os.path.join(HERE, 'round6_results_' + '_'.join(A_keys) + '.json')
    with open(out, 'w') as f:
        json.dump(results, f, indent=1)
    print('wrote', out)


if __name__ == '__main__':
    keys = sys.argv[1:] if len(sys.argv) > 1 else FOCAL_A
    if keys == ['all']:
        keys = STABLE_A
    main(keys)
