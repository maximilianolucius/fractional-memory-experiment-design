"""r6b_case_floor: interval-certified response error for the VOLE-WEASEL CASE STUDY.

Same machinery as r6_response_interval_cert.py, at the empirically anchored cell:
exact rational Jacobian invariants T = 16/53, D = 25/636 (r=1, K=150, A=75/2,
a=100, h=1/6, mu=5/4, e=53/24000, x*=100, y*=53/540), alpha = 2/5.
Partial-fraction poles rho = (96 +- 2 i sqrt(1671))/25 have POSITIVE real part
(fractional-stabilization regime): surrogate secular roots with Re p > 0 are
admissible here and reported, with exponential bounds taken at the correct
interval endpoint. |mu| = sqrt(25/636) < 1/5; tails use the exact bound 1/5.
"""

import sys, os, json, math, time
import numpy as np
from flint import arb, acb, ctx, fmpq

PREC = 256
T_END = 12.0
ALPHA_F = 0.40
ALPHA_Q = fmpq(2, 5)
MS = [4, 8, 16, 32, 64, 128]


def soe_positive(alpha, m, d=1.4):
    """Identical to rescue_compute/r3e_response_cert.py (the surrogate being certified)."""
    ca = math.sin(math.pi*alpha)/math.pi
    h = math.sqrt(2*math.pi*d/(m*alpha*(1-alpha)))
    for _ in range(3):
        Mp = max(1, int(round(2*math.pi*d/(alpha*h*h))))
        Mm = max(1, int(round(2*math.pi*d/((1-alpha)*h*h))))
        tot = Mp+Mm+1
        h *= math.sqrt(tot/m)
    Mp = max(1, int(round(2*math.pi*d/(alpha*h*h))))
    Mm = max(1, int(round(2*math.pi*d/((1-alpha)*h*h))))
    k = np.arange(-Mm, Mp+1)
    lam = np.exp(k*h); c = ca*h*lam**(1-alpha)
    return c, lam


MUB = fmpq(1, 5)          # exact upper bound on |mu| = sqrt(25/636) = 0.19829...

def constants():
    ctx.prec = PREC
    a = arb(ALPHA_Q)
    r1 = acb(arb(96)/25, 2*arb(1671).sqrt()/25)   # rho1: D rho^2 - T rho + 1 = 0
    r2 = r1.conjugate()
    mu = 1/r1
    q = arb(636)/25                                # 1/D
    K1 = q*r1/(r1 - r2)
    return a, r1, mu, K1


# ----------------------------------------------------------------------------- roots
def seed_roots(c, lam, r1, prec=1024):
    """Approximate roots of R_m(p) = r1 as eigenvalues of M = -diag(lam) + c 1^T / r1,
    computed by Arb at `prec` bits. Double precision cannot be used: the surrogate's
    rates span ~41 orders of magnitude (lambda from ~1e-35 to ~1e6), so the smallest
    roots sit far below a double-precision eigensolver's absolute error."""
    from flint import acb_mat
    old = ctx.prec; ctx.prec = prec
    try:
        m = len(c)
        r1h = acb(arb(96)/25, 2*arb(1671).sqrt()/25)   # case-cell rho1, rebuilt at this precision
        Ma = acb_mat(m, m)
        for i in range(m):
            ci = acb(float(c[i]))/r1h
            for j in range(m):
                Ma[i, j] = ci - (acb(float(lam[i])) if i == j else acb(0))
        ev = Ma.eig(algorithm="approx")
        return [acb(z.real.mid(), z.imag.mid()) for z in ev]
    finally:
        ctx.prec = old


def certify_roots(c, lam, r1, seeds=None):
    """Interval-Newton-certified enclosures of all m roots of R_m(p) = r1."""
    m = len(c)
    cA = [arb(float(x)) for x in c]          # doubles are exact dyadics
    lA = [arb(float(x)) for x in lam]
    guesses = seed_roots(c, lam, r1) if seeds is None else seeds

    def F(s):
        acc = acb(0)
        for cj, lj in zip(cA, lA):
            acc += cj/(s + lj)
        return acc - r1

    def Fp(s):
        acc = acb(0)
        for cj, lj in zip(cA, lA):
            q = s + lj
            acc -= cj/(q*q)
        return acc

    boxes = []
    for g in guesses:
        s = acb(g.real.mid(), g.imag.mid()) if isinstance(g, acb) else acb(float(g.real), float(g.imag))
        for _ in range(80):                      # Newton at 256 bits on midpoints
            step = F(s)/Fp(s)
            s = acb(s.real.mid(), s.imag.mid()) - acb(step.real.mid(), step.imag.mid())
            if step.abs_upper() < s.abs_upper() * arb(2)**(-230) + arb(2)**(-1000):
                break
        s = acb(s.real.mid(), s.imag.mid())
        rho = s.abs_upper() * arb(2)**(-140)            # relative box: roots span ~1e-35..1e6
        unit = arb(0, 1)
        X = acb(s.real.mid() + unit*rho, s.imag.mid() + unit*rho)
        dX = Fp(X)
        if dX.contains(acb(0)):
            raise RuntimeError("F'(X) contains 0 at root guess %r" % g)
        N = s - F(s)/dX
        if not X.contains(N):
            raise RuntimeError("interval Newton failed at root guess %r" % g)
        # fractional-stabilization regime: roots with Re p > 0 are admissible; recorded, not fatal
        boxes.append(X)
    for i in range(m):
        for j in range(i+1, m):
            if boxes[i].overlaps(boxes[j]):
                raise RuntimeError("root boxes %d and %d overlap (duplicate/missed root)" % (i, j))
    res = [1/Fp(X) for X in boxes]               # encloses 1/R'(p)
    return boxes, res


# ----------------------------------------------------------------------------- phi_alpha
def _pow(t, e):
    return (e * t.log()).exp()


def phi_alpha(t, a, mu, halfmu):
    """-mu^2 t^{a-1} E_{a,a}(mu t^a), with rigorous tail. t: exact positive arb."""
    acc = acb(0)
    mupow = mu*mu                 # mu^{k+2}, starts k=0
    ta = _pow(t, a)
    k = 0
    while True:
        beta = a*(k+1)
        term = mupow * _pow(t, beta - 1) * beta.rgamma()
        acc += term
        # |mu|=1/2 exactly: ratio bound for j>=k
        rho = arb(halfmu) * ta * _pow(beta + a - 1, -a) if (beta + a - 1) > 0 else arb(10)
        if k >= 8 and rho.upper() < 0.5:
            tk = term.abs_upper()
            if tk < arb(2)**(-140):
                tail = (tk * rho.upper() / (1 - rho.upper())).upper()
                unit = arb(0, 1)                     # the interval [-1, 1]
                acc += acb(unit*tail, unit*tail)
                return -acc
        mupow *= mu
        k += 1
        if k > 5000:
            raise RuntimeError("phi_alpha series did not converge")


def int_abs_phi_alpha_0(t0, a):
    """Upper bound on int_0^t0 |phi_alpha|."""
    s = arb(0); k = 0
    ta = _pow(t0, a)
    while True:
        beta = a*(k+1)
        term = arb(MUB)**(k+2) * _pow(t0, beta) * (beta + 1).rgamma()
        s += term
        rho = arb(MUB) * ta * _pow(beta + a, -a)
        if k >= 4 and rho.upper() < 0.5 and term.upper() < arb(2)**(-PREC):
            return (s + term*rho/(1-rho)).upper()
        k += 1


def sup_phi_alpha_dd(A, B, a):
    """Upper bound on sup_[A,B] |phi_alpha''|."""
    s = arb(0); k = 0
    while True:
        beta = a*(k+1)
        poly = ((beta - 1)*(beta - 2)).abs_upper()
        ex = beta - 3
        base = A if ex.upper() <= 0 else B
        mono = _pow(base, ex).upper() if not ex.contains(0) else max(_pow(A, ex).upper(), _pow(B, ex).upper())
        term = arb(MUB)**(k+2) * poly * mono * beta.rgamma()
        s += term
        if beta.lower() > 3.5:
            f = ((beta + a - 1)*(beta + a - 2)) / ((beta - 1)*(beta - 2))
            rho = (arb(MUB) * _pow(B, a) * _pow(beta + a - 1, -a) * f).upper()
            if rho < 0.5 and term.upper() < arb(2)**(-40) * (s.upper() + arb(2)**(-200)):
                return (s + term*rho/(1-rho)).upper()
        k += 1
        if k > 20000:
            raise RuntimeError("phi_alpha'' series did not converge")


# ----------------------------------------------------------------------------- phi_m
def phi_m(t, boxes, res):
    acc = acb(0)
    for X, r in zip(boxes, res):
        acc += (X*t).exp() * r
    return acc


def sup_phi_m_dd(A, boxes, res, Bnd=None):
    if Bnd is None: Bnd = A
    s = arb(0)
    for X, r in zip(boxes, res):
        re_up = X.real.upper()
        expo = re_up*Bnd if re_up > 0 else re_up*A
        s += X.abs_upper()**2 * r.abs_upper() * expo.exp()
    return s.upper()


# ----------------------------------------------------------------------------- mesh
def build_mesh(t0=2.0**-64, q=1.0 + 1.0/256, hmax=2.0**-12):
    pts = [t0]
    while pts[-1] < T_END:
        nxt = min(pts[-1]*q, pts[-1] + hmax)
        if nxt >= T_END - 1e-12:
            nxt = T_END
        pts.append(nxt)
    return pts


def _exact(x):
    """exact (mantissa, exponent) of an exact arb, for lossless transport between processes"""
    man, ex = x.mid().man_exp()
    return int(man), int(ex)


def _from_exact(me):
    man, ex = me
    return arb(man) * arb(2)**ex


def chunk_bound(args):
    m, lo, hi, pts, seeds_exact = args
    ctx.prec = PREC
    a, r1, mu, K1 = constants()
    c, lam = soe_positive(ALPHA_F, m)
    seeds = [acb(_from_exact(re), _from_exact(im)) for re, im in seeds_exact]
    boxes, res = certify_roots(c, lam, r1, seeds=seeds)     # re-verified in every worker
    twoK = (2*K1).abs_upper()
    def absd(tf):
        t = arb(tf)
        return (2*(K1*(phi_m(t, boxes, res) - phi_alpha(t, a, mu, MUB)))).real.abs_upper()
    first = arb(0); second = arb(0)
    dprev = absd(pts[lo])
    for i in range(lo, hi):
        A, B = pts[i], pts[i+1]
        h = arb(B) - arb(A)
        dnext = absd(B)
        first += h*(dprev + dnext)/2
        sdd = twoK * (sup_phi_alpha_dd(arb(A), arb(B), a) + sup_phi_m_dd(arb(A), boxes, res, arb(B)))
        second += h**3/12 * sdd
        dprev = dnext
    return _exact(first.upper()), _exact(second.upper())


def certify(m, workers):
    from multiprocessing import Pool
    t_start = time.time()
    ctx.prec = PREC
    a, r1, mu, K1 = constants()
    c, lam = soe_positive(ALPHA_F, m)
    seeds = seed_roots(c, lam, r1)
    boxes, res = certify_roots(c, lam, r1, seeds=seeds)
    seeds_exact = [(_exact(X.real.mid()), _exact(X.imag.mid())) for X in boxes]
    mm = len(c)
    max_box = max(float(max(X.real.rad(), X.imag.rad())) for X in boxes)
    min_root = min(float(X.abs_lower()) for X in boxes)
    max_re = max(float(X.real.upper()) for X in boxes)
    n_unstable = sum(1 for X in boxes if X.real.upper() > 0)
    pts = build_mesh()
    t0 = arb(pts[0])
    twoK = (2*K1).abs_upper()
    sum_res = sum((r.abs_upper() for r in res), arb(0))
    re_max = max([X.real.upper() for X in boxes] + [arb(0)])
    near0 = (twoK * (t0*sum_res*(re_max*t0).exp() + int_abs_phi_alpha_0(t0, a))).upper()
    n = len(pts) - 1
    step = max(1, n // (workers*8))
    jobs = [(m, lo, min(lo+step, n), pts, seeds_exact) for lo in range(0, n, step)]
    with Pool(workers) as pool:
        out = pool.map(chunk_bound, jobs)
    first = sum((_from_exact(x) for x, _ in out), arb(0)).upper()
    second = sum((_from_exact(y) for _, y in out), arb(0)).upper()
    E = (near0 + first + second).upper()
    # induced exact two-point floor, ||u||_2 <= 0.120, sigma = 0.10: Phi(-E B/(2 sigma))
    z = E * arb(fmpq(12, 100)) / (2*arb(fmpq(1, 10))) / arb(2).sqrt()
    floor_lo = (arb(1)/2 * z.erfc()).lower()
    return dict(m=mm, roots_certified=mm, n_unstable_roots=n_unstable, max_root_box_radius=max_box, max_root_real_part=max_re,
                min_root_modulus=min_root, lambda_min=float(lam.min()), lambda_max=float(lam.max()),
                n_intervals=n, t0=pts[0],
                near_zero=float(near0), first_order=float(first), second_order=float(second),
                E_upper=float(E*arb(fmpq(1000000001, 1000000000))),
                E_upper_str=(E*arb(fmpq(1000000001, 1000000000))).str(10, radius=False),
                floor_lower=float(floor_lo*arb(fmpq(999999999999, 1000000000000))),
                floor_lower_str=(floor_lo*arb(fmpq(999999999999, 1000000000000))).str(10, radius=False),
                prec_bits=PREC, seconds=round(time.time()-t_start, 1),
                coeffs_c_hex=[float(x).hex() for x in c], coeffs_lambda_hex=[float(x).hex() for x in lam])


if __name__ == "__main__":
    workers = int(os.environ.get("R6_WORKERS", "4"))
    ms = [int(x) for x in sys.argv[1:]] or MS
    outpath = os.environ.get("R6_OUT", "r6b_case_floor.json")
    results = {}
    for m in ms:
        r = certify(m, workers)
        results[str(m)] = r
        print("m=%3d  roots=%d  E_upper=%s  (near0 %.2e, first %.6e, second %.2e)  floor>=%s  [%ss, %d intervals]"
              % (r["m"], r["roots_certified"], r["E_upper_str"], r["near_zero"], r["first_order"],
                 r["second_order"], r["floor_lower_str"], r["seconds"], r["n_intervals"]), flush=True)
        json.dump(results, open(outpath, "w"), indent=1)
    print("DONE", flush=True)
