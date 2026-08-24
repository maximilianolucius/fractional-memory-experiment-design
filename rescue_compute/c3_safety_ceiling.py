"""
C-3 — Theorem D: safety-constrained information ceiling. Computes the real constants of the chain
    safety margin delta  ->  admissible input bound U(delta)  ->  observable separation ceiling
    ->  testing-error floor.

Analytic chain being verified (linearized around the certified coexistence equilibrium):
  (i)   safety x(t) >= A + delta  <=>  |xi_x(t)| <= rho(delta) := x* - A - delta
  (ii)  |xi(t)| <= Gamma_T * ||u||_inf  with  Gamma_T = sup_{t<=T} Int_0^t ||H_alpha(s)|| ds
        => admissible bound U(delta) = rho(delta)/Gamma_T
  (iii) observable separation  ||(H_1-H_2)*u||_inf <= ||Delta H||_{L1(0,T)} * U(delta)  =: S_max
  (iv)  two-hypothesis Gaussian testing floor with n samples, noise sigma:
        P_e >= Phi( -(1/2) * sqrt(n) * S_max / sigma )
Also computes the ACHIEVABLE separation (bang-bang u = U*sign(DeltaH(T-.)), optimal for L-inf
input / L-inf output) to test whether the ceiling is tight or vacuous.

Parallel: one task per (alpha, delta, T, m_latent).
"""
import json, os, sys, itertools, time
import numpy as np
from math import gamma as G, sin, pi, sqrt
from multiprocessing import Pool
from scipy.stats import norm
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core   # exact strong-Allee algebra + Caputo PECE (reused, unchanged)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
os.makedirs(OUT, exist_ok=True)
A_ECO = 0.25            # stable regime (A < 2/7), matches the frozen v3 benchmark
Bch = np.array([1.0, 0.0])
Cobs = np.array([1.0, 0.0])   # collocated prey channel (CB != 0)

def impulse_fractional(alpha, T, N, J):
    """H_alpha(t) = prey-channel impulse response of tau0^(a-1) D^a xi = J xi + B u, via PECE."""
    h = T / N
    g = lambda t, x: (J @ x)          # homogeneous; impulse enters as initial condition B
    # impulse response == solution with xi(0+) = B for the Caputo state-space (Mittag-Leffler)
    z = core.caputo_pece(lambda t, x: J @ x, Bch.copy(), T, N, alpha)
    return np.linspace(0, T, N + 1), z

def gamma_T(ts, Z):
    """Gamma_T = sup_t Int_0^t ||H(s)|| ds  (L1 gain of the impulse response)."""
    nrm = np.linalg.norm(Z, axis=1)
    cum = np.concatenate([[0.0], np.cumsum(0.5 * (nrm[1:] + nrm[:-1]) * np.diff(ts))])
    return float(np.max(cum)), nrm

def latent_impulse(J, T, N, m, rate_lo=0.05, rate_hi=50.0):
    """m-mode latent rival: exponential-sum surrogate of the fractional kernel (positive weights)."""
    ts = np.linspace(0, T, N + 1)
    s = np.linspace(np.log(rate_lo), np.log(rate_hi), m)
    lam = np.exp(s)
    w = np.ones(m) / m
    # build a latent state-space whose prey-channel impulse response mimics the fractional one
    Z = np.zeros((N + 1, 2))
    for wj, lj in zip(w, lam):
        Zj = np.zeros((N + 1, 2))
        # first-order relaxation driven through the same Jacobian backbone
        for i in range(N):
            dt = ts[i+1] - ts[i]
            Zj[i+1] = Zj[i] + dt * (J @ Zj[i] - lj * Zj[i] + (Bch * lj if i == 0 else 0.0))
        Z += wj * Zj
    return ts, Z

def task(args):
    alpha, delta, T, m = args
    N = 3000
    J = core.jacobian(A_ECO)
    xs = core.x_star()
    rho = xs - A_ECO - delta                     # available safety margin in prey state
    if rho <= 0:
        return {"alpha": alpha, "delta": delta, "T": T, "m": m, "infeasible": True}
    ts, Zf = impulse_fractional(alpha, T, N, J)
    GT, _ = gamma_T(ts, Zf)
    U = rho / GT                                  # (ii) admissible input bound
    ts2, Zl = latent_impulse(J, T, N, m)
    dH = (Cobs @ (Zf - Zl).T)                     # prey-channel kernel difference
    dH_L1 = float(np.trapezoid(np.abs(dH), ts)) if hasattr(np, "trapezoid") else float(np.trapz(np.abs(dH), ts))
    S_ceiling = dH_L1 * U                         # (iii) separation ceiling
    # achievable separation: bang-bang input saturating |u|<=U  (max of |conv| at t=T)
    S_achieved = float(np.trapezoid(np.abs(dH), ts)) * U if hasattr(np, "trapezoid") else S_ceiling
    n, sigma = 120, 0.02
    d = sqrt(n) * S_ceiling / sigma
    Pe_floor = float(norm.cdf(-0.5 * d))          # (iv) testing-error floor
    return {"alpha": alpha, "delta": delta, "T": T, "m": m, "infeasible": False,
            "x_star": xs, "rho": rho, "Gamma_T": GT, "U_admissible": U,
            "dH_L1": dH_L1, "S_ceiling": S_ceiling, "S_achieved": S_achieved,
            "n": n, "sigma": sigma, "Pe_floor": Pe_floor}

if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 140
    alphas = [0.70, 0.85, 0.95]
    deltas = [0.02, 0.05, 0.10, 0.20, 0.30]
    Ts = [6.0, 12.0, 24.0]
    ms = [1, 2, 4, 8, 16, 32, 64]
    tasks = list(itertools.product(alphas, deltas, Ts, ms))
    print(f"C-3: {len(tasks)} cells, workers={workers}", flush=True)
    t0 = time.time(); res = []
    with Pool(workers) as p:
        for i, r in enumerate(p.imap_unordered(task, tasks, chunksize=1)):
            res.append(r)
            if i % 50 == 0: print(f"  {i}/{len(tasks)} ({time.time()-t0:.0f}s)", flush=True)
    json.dump(res, open(os.path.join(OUT, "c3_safety_ceiling.json"), "w"), indent=1)
    good = [r for r in res if not r.get("infeasible")]
    print("DONE cells=%d  example: %s" % (len(good), json.dumps(good[0], default=float)[:300]), flush=True)
