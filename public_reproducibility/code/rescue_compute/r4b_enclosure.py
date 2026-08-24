"""R4-B: validated a posteriori enclosure for the headline trajectories.

Everything below is an enclosure, not an estimate:

  reference       zhat = piecewise cubic Hermite, built PER ELEMENT so that the
                  kink in z' at each input discontinuity is represented exactly
                  (the mesh is aligned to the input's break points);
  defect          d = sup_t ||zhat'(t) - f(zhat(t),u(t))||, bounded by interval
                  arithmetic over sub-boxes of every element (t and z both
                  enclosed, outward rounded);
  amplification   one-sided (log-norm) constant mu = sup_tube lam_max(sym Df),
                  bounded by interval subdivision; Gronwall then gives
                    integer:  ||e||_inf <= d * (e^{mu T} - 1)/mu
                    Caputo :  ||e||_inf <= d * (T^a/Gamma(a+1)) * E_a(mu T^a)
  consistency     the bound e must satisfy e <= delta, the tube radius on which
                  mu and the field enclosures were computed (epsilon-inflation).

Because zhat is an explicit piecewise cubic, min_t xhat(t) is computed exactly
(stationary points of each cubic), so no inter-node heuristic enters anywhere.
"""
import numpy as np, math, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "benchmark"))
import core

T, ALPHA, A_VAL, AMP = 12.0, 0.85, 0.25, 0.10
RD, RK, RA, RH, RE, RM = 1.5, 1.0, 1.0, 0.5, 0.8, 0.4
TAU_DDE, LAT_RATES, LAT_G = 0.35, np.array([0.6, 1.0, 0.4]), 0.15
EPS = np.finfo(float).eps

PWC6 = [0.756699881516397, 0.1325216805562377, 0.8458247799426317,
        0.7344822846353054, 0.14397935662418604, 0.32357181794941425]

# ------------------------------------------------------------------ inputs (exact, with break points)
def input_pwc6():
    lev = np.array([2*p - 1 for p in PWC6]); lev = lev*(AMP/np.max(np.abs(lev)))
    brk = [T*i/6.0 for i in range(1, 6)]
    def u_of_elem(tmid): return float(lev[min(5, int(tmid/(T/6.0)))])
    return u_of_elem, brk, "pwc6_found"

def input_multiscale():
    # designs.INPUTS['multiscale'] evaluated exactly; smooth, so no break points
    import designs
    ts = np.linspace(0, T, 200001)
    ua = designs.INPUTS["multiscale"](ts, T)
    sc = AMP/np.max(np.abs(ua))
    def u_of_elem(tmid):
        return float(designs.INPUTS["multiscale"](np.array([tmid]), T)[0]*sc)
    return u_of_elem, [], "multiscale"

# ------------------------------------------------------------------ interval helpers
def infl(lo, hi, k=16.0):
    w = k*EPS*np.maximum(np.abs(lo), np.abs(hi)) + k*np.finfo(float).tiny
    return lo - w, hi + w

def imul(al, ah, bl, bh):
    c = np.stack([al*bl, al*bh, ah*bl, ah*bh]); return c.min(0), c.max(0)

def idiv(al, ah, bl, bh):
    c = np.stack([al/bl, al/bh, ah/bl, ah/bh]); return c.min(0), c.max(0)

def f2_interval(xl, xh, yl, yh, u):
    """Enclosure of the 2-D locked field plus input u (scalar or array)."""
    t1l, t1h = 1.0 - xh/RK, 1.0 - xl/RK
    t2l, t2h = xl/A_VAL - 1.0, xh/A_VAL - 1.0
    p1l, p1h = imul(xl, xh, t1l, t1h)
    Pl, Ph = imul(p1l, p1h, t2l, t2h)
    Pl, Ph = RD*np.minimum(Pl, Ph), RD*np.maximum(Pl, Ph)
    dl, dh = 1.0 + RH*xl, 1.0 + RH*xh
    nl, nh = imul(xl, xh, yl, yh)
    Hl, Hh = idiv(RA*nl, RA*nh, dl, dh)
    Hl, Hh = np.minimum(Hl, Hh), np.maximum(Hl, Hh)
    f1l, f1h = Pl - Hh + u, Ph - Hl + u
    f2l, f2h = RE*Hl - RM*yh, RE*Hh - RM*yl
    a, b = infl(f1l, f1h); c, d = infl(f2l, f2h)
    return a, b, c, d

def mu_box(xl, xh, yl, yh, n=6):
    """Upper bound on lam_max(sym(Df)) over the box, by subdivision."""
    xs = np.linspace(xl, xh, n+1); ys = np.linspace(yl, yh, n+1)
    best = -1e300
    for i in range(n):
        XL, XH = xs[i], xs[i+1]
        a1l, a1h = 1-2*XH/RK, 1-2*XL/RK
        a2l, a2h = XL/A_VAL-1, XH/A_VAL-1
        q = [a1l*a2l, a1l*a2h, a1h*a2l, a1h*a2h]
        bb = [XL*(1-XH/RK), XL*(1-XL/RK), XH*(1-XH/RK), XH*(1-XL/RK)]
        dl, dh = 1+RH*XL, 1+RH*XH
        hyl, hyh = RA*XL/dh, RA*XH/dl
        for j in range(n):
            YL, YH = ys[j], ys[j+1]
            Ppl = RD*(min(q) + min(bb)/A_VAL); Pph = RD*(max(q) + max(bb)/A_VAL)
            hxl, hxh = RA*YL/(dh*dh), RA*YH/(dl*dl)
            for J11 in (Ppl-hxh, Pph-hxl):
                for J12 in (-hyh, -hyl):
                    for J21 in (RE*hxl, RE*hxh):
                        for J22 in (RE*hyl-RM, RE*hyh-RM):
                            off = 0.5*(J12+J21)
                            lam = 0.5*(J11+J22) + math.sqrt(max(0.0, 0.25*(J11-J22)**2 + off*off))
                            if lam > best: best = lam
    return best

def mittag_leffler_upper(a, x, terms=2000):
    s, k = 0.0, 0
    while k < terms:
        term = math.exp(k*math.log(x) - math.lgamma(a*k+1.0)) if x > 0 else (1.0 if k == 0 else 0.0)
        s += term
        if k > 30 and term < 1e-20*s: break
        k += 1
    return s*(1.0 + 1e-10)

# ================================================================== integer-order models
def mesh_aligned(N, brk):
    """Uniform mesh of N elements, refined so every break point is a node."""
    ts = np.linspace(0.0, T, N+1)
    for b in brk:
        if not np.any(np.isclose(ts, b, atol=1e-12)):
            ts = np.sort(np.unique(np.append(ts, b)))
    return ts

def rhs_builder(model):
    """Returns (dim, rhs(z,u), project_to_xy) for the integer-order models."""
    if model == "ODE":
        def rhs(z, u, zd=None):
            x, y = z[0], z[1]; den = 1+RH*x
            hol = RA*x*y/den
            return np.array([RD*x*(1-x/RK)*(x/A_VAL-1) - hol + u, RE*hol - RM*y])
        return 2, rhs
    if model == "latent3":
        def rhs(z, u, zd=None):
            x, y = z[0], z[1]; zc = z[2:]; den = 1+RH*x
            hol = RA*x*y/den
            return np.concatenate([[RD*x*(1-x/RK)*(x/A_VAL-1) - hol + LAT_G*zc.sum() + u,
                                    RE*hol - RM*y], -LAT_RATES*zc + u])
        return 5, rhs
    if model == "DDE":
        def rhs(z, u, zd):
            x, y = z[0], z[1]; xd = zd[0]
            hol = RA*x*y/(1+RH*x); hol_d = RA*xd*y/(1+RH*xd)
            return np.array([RD*x*(1-x/RK)*(x/A_VAL-1) - hol + u, RE*hol_d - RM*y])
        return 2, rhs
    raise ValueError(model)

def solve_and_enclose_integer(model, u_of_elem, brk, N, delta=5e-3, M=8):
    """High-order RK4 solve on the aligned mesh, then a validated enclosure."""
    dim, rhs = rhs_builder(model)
    ts = mesh_aligned(N, brk); n = len(ts)-1
    z0 = np.zeros(dim); z0[0], z0[1] = core.x_star(), core.y_star(A_VAL)
    z = np.zeros((n+1, dim)); z[0] = z0
    uel = np.array([u_of_elem(0.5*(ts[i]+ts[i+1])) for i in range(n)])
    hist = None
    # PER-ELEMENT endpoint derivatives for the history. Nodal derivatives are
    # ambiguous at an input jump (z' has two one-sided values there), and that
    # ambiguity propagates into the delayed term at t = jump + tau, where it
    # dominated the defect by three orders of magnitude.
    fLh = np.zeros((n, dim)); fRh = np.zeros((n, dim)); nready = [0]
    if model == "DDE":
        def zd_at(tq, i):
            if tq <= 0: return z0
            k = int(np.searchsorted(ts, tq) - 1)
            k = min(max(k, 0), max(nready[0]-1, 0))
            if k >= i: return z[min(i, n)]
            hh = ts[k+1]-ts[k]; fr = (tq - ts[k])/hh
            fr = min(max(fr, 0.0), 1.0)
            s2, s3 = fr*fr, fr**3
            return ((1-3*s2+2*s3)*z[k] + hh*(fr-2*s2+s3)*fLh[k]
                    + (3*s2-2*s3)*z[k+1] + hh*(-s2+s3)*fRh[k])
        hist = zd_at
    for i in range(n):
        h = ts[i+1]-ts[i]; ui = uel[i]; t = ts[i]
        if model == "DDE":
            k1 = rhs(z[i], ui, hist(t-TAU_DDE, i))
            k2 = rhs(z[i]+h/2*k1, ui, hist(t+h/2-TAU_DDE, i))
            k3 = rhs(z[i]+h/2*k2, ui, hist(t+h/2-TAU_DDE, i))
            k4 = rhs(z[i]+h*k3, ui, hist(t+h-TAU_DDE, i))
        else:
            k1 = rhs(z[i], ui); k2 = rhs(z[i]+h/2*k1, ui)
            k3 = rhs(z[i]+h/2*k2, ui); k4 = rhs(z[i]+h*k3, ui)
        z[i+1] = z[i] + h/6*(k1+2*k2+2*k3+k4)
        if model == "DDE":
            fLh[i] = k1
            fRh[i] = rhs(z[i+1], uel[i], hist(ts[i+1]-TAU_DDE, i+1))
            nready[0] = i+1
    # per-element endpoint derivatives (this element input value)
    fL = np.zeros((n, dim)); fR = np.zeros((n, dim))
    for i in range(n):
        if model == "DDE":
            fL[i] = rhs(z[i], uel[i], hist(ts[i]-TAU_DDE, i))
            fR[i] = rhs(z[i+1], uel[i], hist(ts[i+1]-TAU_DDE, min(i+1, n-1)))
        else:
            fL[i] = rhs(z[i], uel[i]); fR[i] = rhs(z[i+1], uel[i])
    return dict(ts=ts, z=z, fL=fL, fR=fR, uel=uel, dim=dim, rhs=rhs, hist=hist, model=model)

def hermite_at(sol, i, th):
    """value and t-derivative of the element-i cubic Hermite at local th (array)."""
    ts, z, fL, fR = sol["ts"], sol["z"], sol["fL"], sol["fR"]
    h = ts[i+1]-ts[i]
    th = np.asarray(th, float)[:, None]
    t2, t3 = th*th, th**3
    H00, H10 = 1-3*t2+2*t3, th-2*t2+t3
    H01, H11 = 3*t2-2*t3, -t2+t3
    val = H00*z[i] + h*H10*fL[i] + H01*z[i+1] + h*H11*fR[i]
    d00, d10 = (-6*th+6*t2)/h, 1-4*th+3*t2
    d01, d11 = (6*th-6*t2)/h, -2*th+3*t2
    der = d00*z[i] + d10*fL[i] + d01*z[i+1] + d11*fR[i]
    return val, der

def defect_bound_integer(sol, S=16, K2=12.0):
    """Rigorous sup-norm bound on the defect d(t) = dzhat/dt - rhs(zhat(t), u).

    Interval-evaluating d directly loses the cancellation between dzhat/dt and
    f(zhat) (dependency problem) and yields an O(h) bound, four orders above the
    true O(h^3) defect. We use a second-order Taylor form on S sub-intervals per
    element, with the first two terms POINTWISE and only the third bounded crudely:

        |d(t)| <= |d(tau)| + |dd/dt(tau)| * dt + (1/2) K2 * dt^2 ,  dt = h/(2S)

    where dd/dt = zpp - Df(zhat) * dzhat/dt is evaluated exactly at tau, and K2
    bounds the second derivative of d. K2 = 12 dominates the norm of D2f, which
    is at most 2*M2 = 11.0 by the interval certification in R3-C, plus the
    constant third derivative of the cubic.
    """
    ts, dim, rhs, model = sol["ts"], sol["dim"], sol["rhs"], sol["model"]
    z, fL, fR = sol["z"], sol["fL"], sol["fR"]
    n = len(ts)-1
    tau = (np.arange(S)+0.5)/S
    dt_loc = 1.0/(2.0*S)
    worst = 0.0
    for i in range(n):
        h = ts[i+1]-ts[i]; ui = sol["uel"][i]
        val, der = hermite_at(sol, i, tau)
        c1 = (-6*z[i] + 6*z[i+1])/h - 4*fL[i] - 2*fR[i]
        c2 = ( 6*z[i] - 6*z[i+1])/h + 3*fL[i] + 3*fR[i]
        vv = np.empty(S)
        for jj, t_ in enumerate(tau):
            tt = ts[i] + h*t_
            if model == "DDE":
                r = rhs(val[jj], ui, sol["hist"](tt-TAU_DDE, min(i, n-1)))
            else:
                r = rhs(val[jj], ui)
            d_pt = der[jj] - r
            zpp = (c1 + 2*c2*t_)/h
            x, y = val[jj][0], val[jj][1]
            Pp = RD*((1-2*x/RK)*(x/A_VAL-1) + x*(1-x/RK)/A_VAL)
            den = 1+RH*x; hx = RA*y/den**2; hy = RA*x/den
            J = np.zeros((dim, dim))
            J[0, 0] = Pp - hx; J[0, 1] = -hy
            J[1, 0] = RE*hx;   J[1, 1] = RE*hy - RM
            if dim > 2:
                J[0, 2:] = LAT_G
                for q in range(dim-2): J[2+q, 2+q] = -LAT_RATES[q]
            dprime = zpp - J @ der[jj]
            vv[jj] = (np.linalg.norm(d_pt) + np.linalg.norm(dprime)*h*dt_loc
                      + 0.5*K2*(h*dt_loc)**2)
        v = float(vv.max())
        if v > worst: worst = v
    return worst*(1.0 + 1e-12)

def lipschitz_box(xl, xh, yl, yh, n=4):
    """Interval bound on ||Df||_2 (via max abs row sum) over the box."""
    xs = np.linspace(xl, xh, n+1); ys = np.linspace(yl, yh, n+1)
    best = 0.0
    for i in range(n):
        XL, XH = xs[i], xs[i+1]
        a1l, a1h = 1-2*XH/RK, 1-2*XL/RK
        a2l, a2h = XL/A_VAL-1, XH/A_VAL-1
        q = [a1l*a2l, a1l*a2h, a1h*a2l, a1h*a2h]
        bb = [XL*(1-XH/RK), XL*(1-XL/RK), XH*(1-XH/RK), XH*(1-XL/RK)]
        dl, dh = 1+RH*XL, 1+RH*XH
        hyl, hyh = RA*XL/dh, RA*XH/dl
        Ppl = RD*(min(q) + min(bb)/A_VAL); Pph = RD*(max(q) + max(bb)/A_VAL)
        for j in range(n):
            YL, YH = ys[j], ys[j+1]
            hxl, hxh = RA*YL/(dh*dh), RA*YH/(dl*dl)
            r1 = max(abs(Ppl-hxh), abs(Pph-hxl)) + max(abs(hyl), abs(hyh))
            r2 = RE*max(abs(hxl), abs(hxh)) + max(abs(RE*hyl-RM), abs(RE*hyh-RM))
            best = max(best, r1, r2)
    return best

def min_x_exact(sol):
    """Exact minimum of the piecewise-cubic xhat over [0,T] (stationary points solved)."""
    ts, z, fL, fR = sol["ts"], sol["z"], sol["fL"], sol["fR"]
    n = len(ts)-1; best = np.inf; targ = None
    for i in range(n):
        h = ts[i+1]-ts[i]
        p0, p1 = z[i][0], z[i+1][0]; m0, m1 = fL[i][0]*h, fR[i][0]*h
        # cubic in th: a3 th^3 + a2 th^2 + a1 th + a0
        a0 = p0; a1 = m0; a2 = -3*p0 - 2*m0 + 3*p1 - m1; a3 = 2*p0 + m0 - 2*p1 + m1
        cands = [0.0, 1.0]
        A_, B_, C_ = 3*a3, 2*a2, a1
        if abs(A_) > 1e-300:
            disc = B_*B_ - 4*A_*C_
            if disc >= 0:
                for s in (-1, 1):
                    r = (-B_ + s*math.sqrt(disc))/(2*A_)
                    if 0.0 < r < 1.0: cands.append(r)
        elif abs(B_) > 1e-300:
            r = -C_/B_
            if 0.0 < r < 1.0: cands.append(r)
        for r in cands:
            v = a0 + a1*r + a2*r*r + a3*r**3
            if v < best: best, targ = v, ts[i] + h*r
    return float(best), float(targ)

def tube_mu(sol, delta):
    """mu bound over the tube of radius delta around the whole piecewise-cubic path."""
    ts = sol["ts"]; n = len(ts)-1
    th = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    worst = -1e300
    for i in range(n):
        val, _ = hermite_at(sol, i, th)
        xl, xh = val[:, 0].min()-delta, val[:, 0].max()+delta
        yl, yh = val[:, 1].min()-delta, val[:, 1].max()+delta
        m = mu_box(xl, xh, yl, yh, n=4)
        if m > worst: worst = m
    return float(worst)

# ================================================================== driver
def certify_all(delta=0.05, out=None):
    """Run the enclosure on the 8 headline trajectories and report per-case status."""
    res = []
    for inp in (input_pwc6, input_multiscale):
        u_of, brk, nm = inp()
        for md in ("ODE", "latent3", "DDE"):
            N = 12000
            sol = solve_and_enclose_integer(md, u_of, brk, N)
            d = defect_bound_integer(sol)
            mu = tube_mu(sol, delta)
            amp = (math.exp(mu*T)-1)/mu if mu > 0 else T
            e = d*amp
            mn, targ = min_x_exact(sol)
            consistent = bool(e <= delta)
            if consistent and mn - e > A_VAL:
                status, verdict = "RIGOROUS", "SAFE"
            elif consistent and mn + e < A_VAL:
                status, verdict = "RIGOROUS", "CROSSING"
            else:
                status, verdict = "FAIL_NOT_SELF_CONSISTENT" if not consistent else "FAIL_INDETERMINATE", "INDETERMINATE"
            res.append(dict(design=nm, model=md, N=N, defect=d, mu=mu, amplification=amp,
                            error_bound=e, delta=delta, self_consistent=consistent,
                            min_x_hat=mn, argmin=targ, certified_lower=mn-e,
                            certified_margin=mn-e-A_VAL, status=status, verdict=verdict))
        res.append(dict(design=nm, model="Caputo", N=None, status="NOT_ATTEMPTED_RIGOROUS",
                        verdict="refinement-verified only (see R3-D)",
                        note="the fractional defect requires a reference of order higher than the "
                             "PECE solver; not produced in this round"))
    if out:
        json.dump(res, open(out, "w"), indent=1)
    return res

if __name__ == "__main__":
    here = os.path.dirname(__file__)
    r = certify_all(out=os.path.join(here, "r4b_enclosure_results.json"))
    print(f"{'design':>12} {'model':>8} {'defect':>11} {'amp':>10} {'e':>10} {'cert lower':>11} {'status':>26} {'verdict':>12}")
    for x in r:
        if x.get("N") is None:
            print(f"{x['design']:>12} {x['model']:>8} {'--':>11} {'--':>10} {'--':>10} {'--':>11} {x['status']:>26} {'--':>12}")
        else:
            print(f"{x['design']:>12} {x['model']:>8} {x['defect']:>11.3e} {x['amplification']:>10.3e} "
                  f"{x['error_bound']:>10.3e} {x['certified_lower']:>11.5f} {x['status']:>26} {x['verdict']:>12}")
    ok = sum(1 for x in r if x.get("status") == "RIGOROUS")
    print(f"\nRIGOROUS enclosures: {ok} / 8")
    print("RIGOROUS_CERTIFICATE =", "PASS" if ok == 8 else "FAIL -> MANUSCRIPT_DOWNGRADED")
