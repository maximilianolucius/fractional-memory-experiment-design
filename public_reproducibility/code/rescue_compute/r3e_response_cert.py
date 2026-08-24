"""R3-E: prey-RESPONSE-level approximation error for m = 4..128, not kernel-level.

The manuscript certifies E_m at kernel level and E_m^state at response level. R3-B showed
the two differ by non-monotone factors 0.56-1.26, so response-level numbers must be
computed directly. Here:

  exact fractional impulse response      g_a(t)  = C t^{a-1} E_{a,a}(J t^a) B
  latent surrogate impulse response      g_m(t)  = C_w exp(A_w t) B_w
      (obtained by substituting s^{-a} -> R_m(s) = sum_j c_j/(s+lam_j), the SOE of
       Lemma B.2 with POSITIVE weights, which realises a 2m-dimensional LTI system)

and reports  ||g_a - g_m||_{L1(0,T)}  with an explicit quadrature-error estimate.
"""
import numpy as np, math, json, sys, os
from scipy.linalg import expm
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "benchmark"))
import core

A_VAL, ALPHA, T = 0.25, 0.85, 12.0
J = core.jacobian(A_VAL)
B = np.array([[1.0],[0.0]]); C = np.array([[1.0, 0.0]])

def soe_positive(alpha, m, d=1.4):
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

def g_alpha(ts, alpha, J, B, C, terms=400):
    """C t^{a-1} E_{a,a}(J t^a) B, matrix Mittag-Leffler by series."""
    out = np.zeros(len(ts))
    n = J.shape[0]
    for i, t in enumerate(ts):
        if t <= 0: out[i] = np.nan; continue
        acc = np.zeros((n,n)); ta = t**alpha
        Jk = np.eye(n)          # J^k * ta^k, rescaled to avoid overflow
        logscale = 0.0
        for k in range(terms):
            term = Jk * math.exp(logscale - math.lgamma(alpha*(k+1)))
            acc += term
            if k > 8 and np.abs(term).max() < 1e-18*max(np.abs(acc).max(), 1e-300): break
            Jk = Jk @ J * ta
            mx = np.abs(Jk).max()
            if mx > 1e100:       # renormalise, carry the factor in the log
                Jk /= mx; logscale += math.log(mx)
            if mx == 0.0: break
        out[i] = float((C @ (t**(alpha-1) * acc) @ B).item())
    return out

def g_latent(ts, c, lam, J, B, C):
    """Impulse response of the 2m-dim realisation of s^{-a} -> sum c_j/(s+lam_j)."""
    m = len(c); n = J.shape[0]; N = m*n
    Aw = np.zeros((N,N)); Bw = np.zeros((N,1)); Cw = np.zeros((1,N))
    for j in range(m):
        sl = slice(j*n,(j+1)*n)
        Aw[sl, sl] -= lam[j]*np.eye(n)
        for k in range(m):
            Aw[sl, k*n:(k+1)*n] += c[k]*J
        Bw[sl,0] = B[:,0]
        Cw[0, sl] = c[j]*C[0,:]
    out = np.zeros(len(ts))
    # eigendecomposition once, then evaluate cheaply
    w, V = np.linalg.eig(Aw)
    Vi = np.linalg.inv(V)
    left = (Cw @ V).ravel(); right = (Vi @ Bw).ravel()
    coef = left*right
    for i,t in enumerate(ts):
        out[i] = float(np.real(np.sum(coef*np.exp(w*t))))
    return out

def L1_err(m, alpha=ALPHA, T=T, n1=4000, n2=8000):
    c, lam = soe_positive(alpha, m)
    res = {}
    for n in (n1, n2):
        # graded mesh: t = T*(i/n)^3 clusters near the singular endpoint
        i = np.arange(1, n+1); ts = T*(i/n)**3
        ga = g_alpha(ts, alpha, J, B, C)
        gm = g_latent(ts, c, lam, J, B, C)
        res[n] = float(np.trapezoid(np.abs(ga-gm), ts))
    err = abs(res[n2]-res[n1])
    return len(c), res[n2], err, res

if __name__ == "__main__":
    print("R3-E prey-response-level L1 error, alpha=%.2f A=%.2f T=%.1f" % (ALPHA, A_VAL, T))
    print(f"{'m':>5} {'||g_a-g_m||_L1':>16} {'quad err est':>13} {'rel':>9}")
    out = {}
    for m in (4, 8, 16, 32, 64, 128):
        mm, v, e, raw = L1_err(m)
        out[mm] = dict(L1=v, quad_err=e, raw=raw)
        print(f"{mm:>5} {v:>16.6e} {e:>13.2e} {e/v if v else 0:>9.2e}")
    json.dump(out, open(os.path.join(os.path.dirname(__file__),"r3e_response_cert.json"),"w"), indent=1)
