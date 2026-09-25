"""R6: interval-certified prey-response approximation error at m = 4 ... 128.

Upgrades R3-E (high-accuracy floating point) to a rigorous enclosure, using Arb ball
arithmetic (python-flint). The object certified is the same explicit positive-weight
exponential-sum surrogate R3-E evaluated, so the certified numbers are upper bounds on
the optimised-class quantity E_m^state exactly as the manuscript already states.

Reduction that makes m = 128 tractable
---------------------------------------
With C = B = e1 and the exact Jacobian J = [[-1/8, -1/2], [1/2, 0]] (J22 = 0),

    G(s) = C (X(s)^{-1} I - J)^{-1} B = X / det(I - X J) = 4 X / ((X - r1)(X - r2)),

where r1, r2 = -1/4 +- i sqrt(63)/4 are the roots of r^2 + r/2 + 4 = 0, and X(s) is
s^{-alpha} (fractional model) or R_m(s) = sum_j c_j/(s + lambda_j) (surrogate).
Partial fractions give G = K1/(X - r1) + conj, K1 = 4 r1/(r1 - r2). Hence

    g_alpha(t) = 2 Re[K1 phi_alpha(t)],  phi_alpha(t) = -mu^2 t^{a-1} E_{a,a}(mu t^a), mu = 1/r1
    g_m(t)     = 2 Re[K1 phi_m(t)],      phi_m(t)     = sum_p exp(p t) / R_m'(p)

with p running over the m roots of the secular equation R_m(p) = r1 (the delta terms
cancel exactly between the two conjugate branches). No matrix exponential, no stiffness:
the fast surrogate modes (lambda up to ~1e6) enter only as explicit decaying exponentials.

Rigour
------
* roots p: every root is enclosed by an Arb box on which interval Newton
  N(X) = p0 - F(p0)/F'(X) satisfies N(X) in X with 0 not in F'(X), F = R_m - r1
  (existence + uniqueness); the m boxes are checked pairwise disjoint, so these are all
  m roots of the degree-m polynomial N - r1 D, all simple, and Re p < 0 is checked.
* point values of d = g_alpha - g_m: Arb series for E_{a,a} with an explicit tail bound
  (Gautschi: Gamma(b)/Gamma(b+a) <= (b+a-1)^{-a}).
* per interval [a,b]:   int_a^b |d| <= h (|d(a)| + |d(b)|)/2 + h^3/12 sup_[a,b] |d''|,
  sup|d''| <= 2|K1| (sum_k |mu|^{k+2} |(b_k-1)(b_k-2)| sup t^{b_k-3}/Gamma(b_k) + tail
                     + sum_p |p|^2 / |R'(p)| exp(Re p * a)).
* [0, t0]: int |d| <= 2|K1| (t0 sum_p 1/|R'(p)| + sum_k |mu|^{k+2} t0^{b_k}/Gamma(b_k+1)).
Every number reported as a bound is an Arb upper endpoint.
"""
import sys, os, json, math, time
import numpy as np
from flint import arb, acb, ctx, fmpq

PREC = 256
T_END = 12.0
ALPHA_F = 0.85
ALPHA_Q = fmpq(17, 20)
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


def constants():
    ctx.prec = PREC
    a = arb(ALPHA_Q)
    r1 = acb(arb(-1)/4, arb(63).sqrt()/4)
    r2 = r1.conjugate()
    mu = 1/r1
    K1 = 4*r1/(r1 - r2)
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
        r1h = acb(arb(-1)/4, arb(63).sqrt()/4)
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
        if not (X.real.upper() < 0):
            raise RuntimeError("root with nonnegative real part: %r" % g)
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
        term = arb(2)**(-(k+2)) * _pow(t0, beta) * (beta + 1).rgamma()
        s += term
        rho = arb(fmpq(1, 2)) * ta * _pow(beta + a, -a)
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
        term = arb(2)**(-(k+2)) * poly * mono * beta.rgamma()
        s += term
        if beta.lower() > 3.5:
            f = ((beta + a - 1)*(beta + a - 2)) / ((beta - 1)*(beta - 2))
            rho = (arb(fmpq(1, 2)) * _pow(B, a) * _pow(beta + a - 1, -a) * f).upper()
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


def sup_phi_m_dd(A, boxes, res):
    s = arb(0)
    for X, r in zip(boxes, res):
        s += X.abs_upper()**2 * r.abs_upper() * (X.real.upper()*A).exp()
    return s.upper()


# ----------------------------------------------------------------------------- mesh
def build_mesh(t0=2.0**-40, q=1.0 + 1.0/256, hmax=2.0**-12):
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
        return (2*(K1*(phi_m(t, boxes, res) - phi_alpha(t, a, mu, fmpq(1, 2))))).real.abs_upper()
    first = arb(0); second = arb(0)
    dprev = absd(pts[lo])
    for i in range(lo, hi):
        A, B = pts[i], pts[i+1]
        h = arb(B) - arb(A)
        dnext = absd(B)
        first += h*(dprev + dnext)/2
        sdd = twoK * (sup_phi_alpha_dd(arb(A), arb(B), a) + sup_phi_m_dd(arb(A), boxes, res))
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
    pts = build_mesh()
    t0 = arb(pts[0])
    twoK = (2*K1).abs_upper()
    sum_res = sum((r.abs_upper() for r in res), arb(0))
    near0 = (twoK * (t0*sum_res + int_abs_phi_alpha_0(t0, a))).upper()
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
    return dict(m=mm, roots_certified=mm, max_root_box_radius=max_box, max_root_real_part=max_re,
                min_root_modulus=min_root, lambda_min=float(lam.min()), lambda_max=float(lam.max()),
                n_intervals=n, t0=pts[0],
                near_zero=float(near0), first_order=float(first), second_order=float(second),
                E_upper=float(E*arb(fmpq(1000000001, 1000000000))),
                E_upper_str=(E*arb(fmpq(1000000001, 1000000000))).str(10, radius=False),
                floor_lower=float(floor_lo*arb(fmpq(999999999999, 1000000000000))),
                floor_lower_str=(floor_lo*arb(fmpq(999999999999, 1000000000000))).str(10, radius=False),
                prec_bits=PREC, seconds=round(time.time()-t_start, 1),
                coeffs_c_hex=[float(x).hex() for x in c], coeffs_lambda_hex=[float(x).hex() for x in lam])


# ----------------------------------------------------------------------------- self-check
def selfcheck():
    """Floating-point cross-check of the scalar reduction against the matrix formulas."""
    ctx.prec = PREC
    a, r1, mu, K1 = constants()
    J = np.array([[-0.125, -0.5], [0.5, 0.0]])
    out = {}
    # (i) g_alpha scalar vs matrix Mittag-Leffler series
    def g_alpha_matrix(t, terms=400):
        acc = np.zeros((2, 2)); Jk = np.eye(2); ta = t**ALPHA_F
        for k in range(terms):
            acc += Jk * math.exp(-math.lgamma(ALPHA_F*(k+1)))
            Jk = Jk @ J * ta
            if np.abs(Jk).max() < 1e-300: break
        return (t**(ALPHA_F-1) * acc)[0, 0]
    errs = []
    for t in (0.01, 0.3, 1.0, 4.0, 11.5):
        gs = float((2*(K1*phi_alpha(arb(t), a, mu, fmpq(1, 2)))).real.mid())
        errs.append(abs(gs - g_alpha_matrix(t)))
    out["g_alpha_scalar_vs_matrix_maxabs"] = max(errs)
    # (ii) g_m scalar (roots) vs 2m-dim realisation (numpy eig), m = 16
    c, lam = soe_positive(ALPHA_F, 16)
    boxes, res = certify_roots(c, lam, r1, seeds=seed_roots(c, lam, r1))
    m = len(c); n = 2*m
    Aw = np.zeros((n, n)); Bw = np.zeros(n); Cw = np.zeros(n)
    for j in range(m):
        sl = slice(2*j, 2*j+2)
        Aw[sl, sl] -= lam[j]*np.eye(2)
        for k in range(m):
            Aw[sl, 2*k:2*k+2] += c[k]*J
        Bw[sl] = [1, 0]; Cw[sl] = [c[j], 0]
    w, V = np.linalg.eig(Aw); Vi = np.linalg.inv(V)
    coef = (Cw @ V) * (Vi @ Bw)
    errs = []
    for t in (0.001, 0.1, 1.0, 5.0, 11.0):
        gm_mat = float(np.real(np.sum(coef*np.exp(w*t))))
        gm_sc = float((2*(K1*phi_m(arb(t), boxes, res))).real.mid())
        errs.append(abs(gm_mat - gm_sc))
    out["g_m_scalar_vs_matrix_maxabs_m16"] = max(errs)
    return out


if __name__ == "__main__":
    workers = int(os.environ.get("R6_WORKERS", "4"))
    ms = [int(x) for x in sys.argv[1:]] or MS
    outpath = os.environ.get("R6_OUT", "r6_response_interval_cert.json")
    results = {"selfcheck": selfcheck()}
    print("selfcheck:", results["selfcheck"], flush=True)
    for m in ms:
        r = certify(m, workers)
        results[str(m)] = r
        print("m=%3d  roots=%d  E_upper=%s  (near0 %.2e, first %.6e, second %.2e)  floor>=%s  [%ss, %d intervals]"
              % (r["m"], r["roots_certified"], r["E_upper_str"], r["near_zero"], r["first_order"],
                 r["second_order"], r["floor_lower_str"], r["seconds"], r["n_intervals"]), flush=True)
        json.dump(results, open(outpath, "w"), indent=1)
    print("DONE", flush=True)
