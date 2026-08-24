"""smoke_test.py — exercise every path once, tiny, to catch bugs before the full run."""
import time, numpy as np
import core, designs, bench, run_all

t0 = time.time()
print("== gates ==")
g = run_all.phase_gates()
print("  x*=%.6f ok=%s | alpha*(0.3)=%r ok=%s | ranks_full=%s | PASS=%s"
      % (g["x_star"], g["x_star_ok"], g["alpha_star_0.30"], g["alpha_star_0.30_ok"],
         g["ranks_full"], g["PASS"]))

print("== solver vs Mittag-Leffler (N=250) ==")
ts = np.linspace(0, 8, 251)
num = core.caputo_pece(lambda t, z: np.array([-0.7 * z[0]]), np.array([1.0]), 8.0, 250, 0.85)[:, 0]
ref = core.ml_reference_scalar(-0.7, ts, 0.85)
print("  max_abs_err=%.2e" % np.max(np.abs(num - ref)))

print("== nonlinear sims (each true model) ==")
for m in designs.TRUE_MODELS:
    tsf, tr = bench.sim_nonlinear(m, 0.30, 0.9, designs.INPUTS["pulse"], 12.0, 300)
    print("  %-8s traj shape=%s finite=%s x_range=[%.3f,%.3f]"
          % (m, tr.shape, np.all(np.isfinite(tr)), tr[:, 0].min(), tr[:, 0].max()))

print("== lin_response (each candidate) ==")
tsamp = designs.sample_times(12.0)
for m in run_all.CAND:
    mu = bench.lin_response(m, 0.30, 0.9, designs.INPUTS["multisine"], 12.0, 400,
                            designs.CHANNELS["both"], tsamp)
    print("  %-8s mu shape=%s finite=%s" % (m, mu.shape, np.all(np.isfinite(mu))))

print("== work_cell (reps=8): stable A=0.25 + verdict A=0.30, safety + regime ==")
for tm in ["ODE", "Caputo", "DDE", "latent3"]:
    for A, reg in [(0.25, "stable"), (0.30, "verdict")]:
        cell = (tm, A, 0.85, "multiscale", "both", "med", reg, 8, 300, 42)
        res = run_all.work_cell(cell)
        s = res.get("safety") or {}
        print("  true=%-8s A=%.2f(%s) div=%s acc=%s allee_margin=%s crossed=%s sel=%s" %
              (tm, A, reg, res.get("diverged"), res["accuracy"],
               (round(s["allee_margin"],3) if s.get("allee_margin") is not None else None),
               s.get("allee_crossed"), res["selected"]))

print("SMOKE OK  (%.1fs)" % (time.time() - t0))
