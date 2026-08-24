"""
core.py — fractional-memory-experiment-design benchmark core.

Certified strong-Allee predator-prey backbone, exact algebra (analytic gates),
dimensionally-consistent Caputo PECE solver (validated vs Mittag-Leffler), and the
linearized transfer functions used by the linear-Gaussian discrimination layer.

All math follows source_pack/{03,04,05,06,07,10}. Locked parameters from
source_pack/04_EXACT_STRONG_ALLEE_BASELINE.md:
    r=3/2, K=1, a=1, h=1/2, e=4/5, m=2/5.
"""
import numpy as np
from math import gamma
from mpmath import mp, mpf, matrix as mpmatrix
import mpmath

# ----------------------------------------------------------------------------- locked params
R, K, A_DEFAULT, AA, HH, EE, MM = 1.5, 1.0, 0.3, 1.0, 0.5, 0.8, 0.4  # AA=a, HH=h

def P(x, A):
    return R * x * (1.0 - x / K) * (x / A - 1.0)

def f_vec(z, A):
    """Ecological vector field f(z;theta), z=(x,y). Units [x][t]^-1."""
    x, y = z[0], z[1]
    hol = AA * x * y / (1.0 + HH * x)
    return np.array([P(x, A) - hol, EE * hol - MM * y])

# ----------------------------------------------------------------------------- exact equilibrium / Jacobian (T1, T2)
def x_star():
    return MM / (AA * (EE - MM * HH))            # = 2/3 exactly

def y_star(A):
    xs = x_star()
    return (1.0 + HH * xs) / AA * R * (1.0 - xs / K) * (xs / A - 1.0)

def jacobian(A):
    """Exact coexistence Jacobian J(A) (source_pack/04 eq.5-6)."""
    xs, ys = x_star(), y_star(A)
    d = 1.0 + HH * xs
    # P(x)=r x (1-x/K)(x/A-1);  P'(x)=r[(1-2x/K)(x/A-1) + x(1-x/K)/A]
    Pp = R * ((1.0 - 2.0 * xs / K) * (xs / A - 1.0) + xs * (1.0 - xs / K) * (1.0 / A))
    J11 = Pp - AA * ys / d**2
    J12 = -AA * xs / d
    J21 = EE * AA * ys / d**2
    J22 = 0.0
    return np.array([[J11, J12], [J21, J22]])

def trace_det(A):
    J = jacobian(A)
    return J[0, 0] + J[1, 1], J[0, 0] * J[1, 1] - J[0, 1] * J[1, 0]

def alpha_star(A, dps=40):
    """Exact Matignon critical order for the complex-pair regime 2/7<A<10/19
    (source_pack/04 Thm 3). Returns None outside that regime."""
    mp.dps = dps
    T, D = trace_det(A)
    T, D = mpf(T), mpf(D)
    disc = 4 * D - T**2
    if disc <= 0 or T <= 0:
        return None
    return float((2 / mp.pi) * mpmath.atan(mpmath.sqrt(disc) / T))

# ----------------------------------------------------------------------------- controllability / observability (T3)
def ctrb_obsv_ranks(A):
    J = jacobian(A)
    out = {}
    for name, B in (("prey", np.array([1.0, 0.0])), ("pred", np.array([0.0, 1.0]))):
        C = np.column_stack([B, J @ B]);  out["ctrb_" + name] = np.linalg.matrix_rank(C)
    for name, Cr in (("prey", np.array([1.0, 0.0])), ("pred", np.array([0.0, 1.0]))):
        O = np.vstack([Cr, Cr @ J]);      out["obsv_" + name] = np.linalg.matrix_rank(O)
    return out

# ----------------------------------------------------------------------------- Caputo PECE solver (Diethelm ABM)
def _weights_predictor(alpha, N, h):
    j = np.arange(N + 1)
    # b_{j} for step n: (h^a/a)[(n+1-j)^a-(n-j)^a]; precompute k^a
    return (h**alpha) / alpha

def caputo_pece(g, z0, T, N, alpha, tau0=1.0):
    """Solve tau0^{a-1} D^a z = f  <=>  D^a z = tau0^{1-a} f, via fractional
    Adams-Bashforth-Moulton PECE (Diethelm et al. 2002). g(t,z) already returns
    the RHS of D^a z (i.e. includes tau0^{1-a} and any input). O(N^2)."""
    h = T / N
    a = alpha
    z = np.zeros((N + 1, len(z0)));  z[0] = z0
    ha = h**a
    ga1 = gamma(a + 1.0)
    ga2 = gamma(a + 2.0)
    gvals = np.zeros((N + 1, len(z0)));  gvals[0] = g(0.0, z0)
    ka1 = np.arange(N + 2, dtype=float) ** (a + 1.0)   # k^{a+1}
    kaa = np.arange(N + 2, dtype=float) ** a           # k^a
    for n in range(N):
        # predictor weights b_j = (h^a/a)[(n+1-j)^a-(n-j)^a], j=0..n
        idx = np.arange(n + 1)
        b = (ha / a) * (kaa[n + 1 - idx] - kaa[n - idx])
        zP = z[0] + (b[:, None] * gvals[:n + 1]).sum(axis=0)
        # corrector weights a_j (Diethelm)
        aw = np.empty(n + 2)
        aw[0] = ha / ga2 * (n**(a + 1.0) - (n - a) * (n + 1.0)**a)
        if n >= 1:
            jj = np.arange(1, n + 1)
            aw[1:n + 1] = ha / ga2 * (ka1[n - jj + 2] + ka1[n - jj] - 2.0 * ka1[n - jj + 1])
        aw[n + 1] = ha / ga2
        tn1 = (n + 1) * h
        gP = g(tn1, zP)
        z[n + 1] = z[0] + (aw[:n + 1, None] * gvals[:n + 1]).sum(axis=0) + aw[n + 1] * gP
        gvals[n + 1] = g(tn1, z[n + 1])
    return z

# ----------------------------------------------------------------------------- Mittag-Leffler reference (solver gate)
def mittag_leffler(a, z, terms=200):
    mp.dps = 30
    s = mpf(0)
    for k in range(terms):
        s += mpf(z)**k / mpmath.gamma(a * k + 1)
    return float(s)

def ml_reference_scalar(lam, t_arr, alpha):
    """Exact y(t)=E_alpha(lam t^alpha) for scalar D^alpha y = lam y, y0=1."""
    return np.array([mittag_leffler(alpha, lam * (t**alpha)) for t in t_arr])

# ----------------------------------------------------------------------------- linear transfer functions (T4-T6)
def q_alpha(s, alpha, tau0=1.0):
    return tau0**(-1.0) * (s * tau0) ** alpha

def G_caputo(s, alpha, J, B, C, tau0=1.0):
    q = q_alpha(s, alpha, tau0)
    return (C @ np.linalg.solve(q * np.eye(2) - J, B))

def G_ode(s, J, B, C):
    return (C @ np.linalg.solve(s * np.eye(2) - J, B))

def G_dde(s, A0, A1, tau, B, C):
    return (C @ np.linalg.solve(s * np.eye(len(B)) - A0 - A1 * np.exp(-s * tau), B))

def G_latent(s, Abar, Bbar, Cbar):
    return (Cbar @ np.linalg.solve(s * np.eye(len(Abar)) - Abar, Bbar))
