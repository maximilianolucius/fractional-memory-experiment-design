"""R3-C: interval-certified safety constants for the locked strong-Allee field.

Certifies M2(r) = sup_{||xi||<=r} ||R(xi)|| / ||xi||^2  with R(xi)=f(z*+xi)-J xi,
via the Taylor remainder bound  ||R(xi)|| <= (1/2) sup_{ball} ||D^2 f|| ||xi||^2,
where the Hessian tensor norm is enclosed by branch-and-bound interval arithmetic.
No sampling.
"""
from mpmath import iv, mpf
import mpmath, math, json, sys

iv.dps = 40
# all model constants as degenerate intervals so every operation stays in iv
R_ = iv.mpf(3)/3*iv.mpf(3)/2*iv.mpf(1)   # = 3/2 exactly
R_ = iv.mpf(3)/iv.mpf(2)
K_ = iv.mpf(1)
a_ = iv.mpf(1)
h_ = iv.mpf(1)/iv.mpf(2)
e_ = iv.mpf(4)/iv.mpf(5)
m_ = iv.mpf(2)/iv.mpf(5)

def hess_bounds(A, X, Y):
    """Interval enclosures of all second partials of f1,f2 on box X x Y."""
    A = iv.mpf(A)
    # f1 = R x (1-x/K)(x/A-1) - a x y /(1+h x)
    # P(x) = R x (1-x)(x/A-1)  [K=1]
    # d2/dx2 of R x(1-x)(x/A-1) = R * d2/dx2 [ x(1-x)(x/A-1) ]
    # expand: x(1-x)(x/A-1) = x[(x/A -1) - x^2/A + x] = x^2/A - x - x^3/A + x^2
    #        = -x^3/A + x^2(1/A + 1) - x
    # d2 = -6x/A + 2(1/A+1)
    d2P = R_ * (-6*X/A + 2*(1/A + 1))
    den = 1 + h_*X
    # g = a x y/(1+h x);  d2g/dx2 = a y * d2/dx2 [x/(1+hx)] = a y * (-2h/(1+hx)^3)
    d2g_xx = a_*Y*(-2*h_)/den**3
    # d2g/dxdy = a * d/dx[x/(1+hx)] = a * 1/(1+hx)^2
    d2g_xy = a_/den**2
    # d2g/dy2 = 0
    H1xx = d2P - d2g_xx
    H1xy = -d2g_xy
    H1yy = iv.mpf(0)
    # f2 = e*a*x*y/(1+hx) - m y
    H2xx = e_*d2g_xx
    H2xy = e_*d2g_xy
    H2yy = iv.mpf(0)
    return (H1xx,H1xy,H1yy),(H2xx,H2xy,H2yy)

def _absmax(iv_val):
    "float upper bound on |x| for x in the interval"
    lo = float(mpmath.mpf(iv_val.a)); hi = float(mpmath.mpf(iv_val.b))
    return max(abs(lo), abs(hi))

def hess_norm_upper(A, X, Y):
    """Upper bound on sup over unit v of || (v^T H_i v)_i ||_2 / ... ->
    uses ||R(xi)|| <= (1/2) sqrt( sum_i (sup|v^T H_i v|)^2 ) ||xi||^2,
    with sup_{|v|=1} |v^T H v| <= ||H||_2 <= |Hxx|+|Hxy| , |Hxy|+|Hyy| row bound."""
    (a11,a12,a22),(b11,b12,b22) = hess_bounds(A,X,Y)
    def specbound(h11,h12,h22):
        # symmetric 2x2: ||H||_2 <= max row abs-sum
        r1 = _absmax(h11)+_absmax(h12); r2 = _absmax(h12)+_absmax(h22)
        return max(r1,r2)
    n1 = specbound(a11,a12,a22); n2 = specbound(b11,b12,b22)
    return math.sqrt(n1*n1+n2*n2)

def certify_M2(A, r, depth=7):
    """Branch-and-bound over the ball ||xi||<=r (covered by a box) -> certified M2 bound."""
    xs = mpf(2)/3
    ys = 2*(2-3*mpf(A))/(9*mpf(A))
    best = 0.0
    # cover the ball by a grid of boxes; each box intersected with the ball
    n = 2**depth
    step = 2*mpf(r)/n
    for i in range(n):
        x0 = -mpf(r) + i*step; x1 = x0+step
        for j in range(n):
            y0 = -mpf(r) + j*step; y1 = y0+step
            # skip boxes entirely outside the ball
            cx = min(abs(x0),abs(x1)) if x0*x1>0 else mpf(0)
            cy = min(abs(y0),abs(y1)) if y0*y1>0 else mpf(0)
            if cx*cx + cy*cy > mpf(r)*mpf(r): continue
            X = iv.mpf([xs+x0, xs+x1]); Y = iv.mpf([ys+y0, ys+y1])
            b = hess_norm_upper(A, X, Y)
            if b > best: best = b
    return best/2.0   # Taylor remainder factor 1/2

if __name__ == "__main__":
    A = 0.25
    print("R3-C interval-certified M2(r) for A=%.2f (no sampling)" % A)
    print(f"{'r':>8} {'M2_certified':>14} {'M2_sampled(R2)':>15} {'ratio':>7}")
    sampled = {0.05:4.589, 0.10:4.891, 0.20:5.495, 0.30:6.100, 0.3667:6.504, 0.40:6.705}
    out={}
    for r in (0.0183, 0.05, 0.10, 0.20, 0.30, 0.3667, 0.40):
        depth = 6 if r>0.1 else 5
        M = certify_M2(A, r, depth=depth)
        s = sampled.get(r)
        out[str(r)] = float(M)
        rr = f"{float(M)/s:.4f}" if s else "  --  "
        ss = f"{s:.3f}" if s else "  --  "
        print(f"{r:>8} {float(M):>14.6f} {ss:>15} {rr:>7}")
    json.dump(out, open("rescue_compute/r3c_M2_certified.json","w"), indent=1)
    print("\nwritten rescue_compute/r3c_M2_certified.json")

# ---------------------------------------------------------------------------
# Derived safety constants recomputed with the CERTIFIED M2 (appended R3-C part 2)
# ---------------------------------------------------------------------------
def M2_cert_interp(r, table):
    """monotone upper bound: use the certified value at the smallest tabulated radius >= r"""
    ks = sorted(float(k) for k in table)
    for k in ks:
        if k >= r - 1e-12: return table[str(k)] if str(k) in table else table[repr(k)]
    return table[str(ks[-1])]

def solve_UNL(GB, GR, table, rho, n=20000):
    """max over r of (r - GR*M2(r)*r^2)/GB  s.t. r<=rho and GR*M2(r)*r<1"""
    best = (0.0, None)
    rmax = 0.0
    for i in range(1, n+1):
        r = rho*i/n
        M2 = M2_cert_interp(r, table)
        if GR*M2*r >= 1.0: break
        rmax = r
        U = (r - GR*M2*r*r)/GB
        if U > best[0]: best = (U, r)
    return best[0], best[1], rmax

if __name__ == "__main__":
    import json
    tab = json.load(open("rescue_compute/r3c_M2_certified.json"))
    GB, GR = 5.7815, 6.2225          # from Round 02 (numerical quadrature, NOT interval-certified)
    xs = 2.0/3.0; A = 0.25
    print()
    print("Derived constants with CERTIFIED M2 (Gamma_B, Gamma_R still numerical):")
    print(f"{'delta':>7} {'rho(delta)':>11} {'r*_cert':>9} {'U_NL_cert':>11} {'U_NL_R02':>10} {'degradation':>12}")
    R02 = {0.02:0.00149, 0.05:0.00151, 0.10:0.00150, 0.20:0.00151, 0.30:0.00151}
    out = {}
    for d in (0.02,0.05,0.10,0.20,0.30):
        rho = xs - A - d
        U, rstar, rmax = solve_UNL(GB, GR, tab, rho)
        out[str(d)] = dict(rho=rho, r_star=rstar, U_NL_cert=U, r_max=rmax)
        deg = (1 - U/R02[d])*100
        print(f"{d:>7} {rho:>11.4f} {rstar:>9.5f} {U:>11.6f} {R02[d]:>10.5f} {deg:>11.1f}%")
    _,_,rmax = solve_UNL(GB, GR, tab, xs-A-0.02)
    print(f"\ncertified r_max = {rmax:.5f}   (Round 02 claimed 0.0350, an overestimate)")
    print(f"ecological margin rho(0.05) = {xs-A-0.05:.4f}  ->  ratio {(xs-A-0.05)/rmax:.1f}x")
    json.dump(out, open("rescue_compute/r3c_UNL_certified.json","w"), indent=1)
