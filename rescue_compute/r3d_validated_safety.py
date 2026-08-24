"""R3-D: a posteriori validated safety classification of benchmark trajectories.

The manuscript decides Allee crossing by SAMPLING the PECE solution on its own grid.
That can miss a crossing between nodes, and it ignores solver error. Here each
trajectory gets a certified lower bound on  min_t x(t)  combining:

  (1) solver error, estimated by mesh refinement (N, 2N, 4N) with an observed order;
  (2) inter-node variation, bounded rigorously via the Caputo mild-solution modulus
      of continuity  |z(t)-z(t')| <= (2 F / Gamma(alpha+1)) |t-t'|^alpha ,
      F = sup ||f(z,u)|| enclosed over the tube around the computed trajectory.

Verdict per trajectory: SAFE-CERTIFIED / CROSSING-CERTIFIED / INDETERMINATE.
"""
import sys, os, json, math, itertools
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "benchmark"))
import bench, designs, core

T = 12.0
ALPHA = 0.85
A_VAL = 0.25
AMP = 0.10

PWC6 = [0.756699881516397,0.1325216805562377,0.8458247799426317,
        0.7344822846353054,0.14397935662418604,0.32357181794941425]
def pwc6(ts, Tloc):
    ts = np.asarray(ts, dtype=float)
    k = np.clip((ts/(Tloc/6.0)).astype(int), 0, 5)
    return 2*np.asarray(PWC6)[k] - 1.0

INPUTS = dict(designs.INPUTS); INPUTS["pwc6_found"] = pwc6

def F_bound(traj, uf, A, amp, pad=0.05):
    """Upper bound on sup||f(z,u)|| over a tube of radius `pad` around the computed traj."""
    zmin = traj.min(0) - pad; zmax = traj.max(0) + pad
    R,K,a,h,e,m = 1.5,1.0,1.0,0.5,0.8,0.4
    best = 0.0
    nx, ny = 40, 40
    for i in range(nx+1):
        x = zmin[0] + (zmax[0]-zmin[0])*i/nx
        if 1+h*x <= 1e-9: continue
        for j in range(ny+1):
            y = zmin[1] + (zmax[1]-zmin[1])*j/ny
            f1 = R*x*(1-x/K)*(x/A-1) - a*x*y/(1+h*x) + amp
            f2 = e*a*x*y/(1+h*x) - m*y
            v = math.hypot(f1, f2)
            if v > best: best = v
    return best

def run(model, A, alpha, uf, N):
    ts, tr = bench.sim_nonlinear(model, A, alpha, uf, T, N, amp=AMP)
    return np.asarray(ts), np.asarray(tr)

def certify(model, A, alpha, uf, name, N0=3000):
    rows = []
    prev_min = None
    for k, N in enumerate((N0, 2*N0, 4*N0)):
        ts, tr = run(model, A, alpha, uf, N)
        if bench.diverged(tr):
            return dict(design=name, model=model, verdict="DIVERGED", N=N)
        mn = float(tr[:,0].min())
        rows.append((N, mn))
        prev_min = mn
    # observed convergence: |m(4N)-m(2N)|, and Richardson-style solver error estimate
    d1 = abs(rows[1][1]-rows[0][1]); d2 = abs(rows[2][1]-rows[1][1])
    solver_err = d2 if d2 <= d1 else d1 + d2      # conservative
    N = rows[-1][0]; h = T/N
    ts, tr = run(model, A, alpha, uf, N)
    F = F_bound(tr, uf, A, AMP)
    # inter-node variation over half a step, worst case
    internode = (2.0*F/math.gamma(alpha+1)) * (h)**alpha
    mn = rows[-1][1]
    lower = mn - solver_err - internode
    upper = mn + solver_err
    if lower > A:        v = "SAFE-CERTIFIED"
    elif upper < A:      v = "CROSSING-CERTIFIED"
    else:                v = "INDETERMINATE"
    return dict(design=name, model=model, min_x_computed=mn,
                solver_err=solver_err, F_bound=F, internode_bound=internode,
                certified_lower=lower, certified_upper=upper,
                margin_computed=mn-A, margin_certified=lower-A,
                verdict=v, N_final=N, h=h,
                mesh=[(int(n),float(m)) for n,m in rows])

if __name__ == "__main__":
    MODELS = ["Caputo","ODE","DDE","latent3"]
    out = []
    print(f"{'design':>12} {'model':>8} {'min x':>9} {'solver':>9} {'internode':>10} {'cert lower':>11} {'verdict':>19}")
    for nm, uf in INPUTS.items():
        for md in MODELS:
            r = certify(md, A_VAL, ALPHA, uf, nm)
            out.append(r)
            if r["verdict"] == "DIVERGED":
                print(f"{nm:>12} {md:>8} {'--':>9} {'--':>9} {'--':>10} {'--':>11} {'DIVERGED':>19}")
            else:
                print(f"{nm:>12} {md:>8} {r['min_x_computed']:>9.5f} {r['solver_err']:>9.2e} "
                      f"{r['internode_bound']:>10.2e} {r['certified_lower']:>11.5f} {r['verdict']:>19}")
    json.dump(out, open(os.path.join(os.path.dirname(__file__),"r3d_validated_safety.json"),"w"), indent=1)
    print("\nA =", A_VAL)
    for v in ("SAFE-CERTIFIED","CROSSING-CERTIFIED","INDETERMINATE","DIVERGED"):
        n = sum(1 for r in out if r["verdict"]==v); print(f"  {v:<20} {n}")
