#!/usr/bin/env python3
"""
Test Gate 7: Step refinement and independent re-simulation
Demonstrate convergence under h-refinement (halving time step) and that an independent 
re-simulation with different solver (e.g., Adams-Bashforth-Moulton) yields identical 
results within tolerance.
"""
import sys
import numpy as np
sys.path.append('src')
from solvers.fractional import solve_fractional_caputo

def test_gate7_step_refinement_and_re_simulation():
    """
    Test Gate 7: Step refinement and independent re-simulation
    """
    # Parameters for the ODE: dx/dt = -x^3 + x^2
    def f(t, x):
        return np.array([-x[0]**3 + x[0]**2])

    alpha = 0.3
    x0 = np.array([0.5])
    tspan = (0.0, 20.0)  # sufficiently long to see decay
    tol = 1e-6

    # We'll compute the solution with two different step sizes: h and h/2
    h1 = 0.1
    h2 = h1 / 2.0

    # Solve with h1
    t1, x1 = solve_fractional_caputo(f, tspan, x0, alpha, h1)
    # Solve with h2
    t2, x2 = solve_fractional_caputo(f, tspan, x0, alpha, h2)

    # To compare, we need to interpolate the finer solution onto the coarse grid (or vice versa).
    # We'll interpolate the fine solution (h2) onto the coarse time points (t1).
    # Since t1 is a subset of t2? Not necessarily because tspan is the same and h2 is half of h1,
    # so t1 should be a subset of t2 if t0 and tend are multiples of h1 and h2.
    # We adjusted t_end in the solver to be exactly n_steps * h, so we might have a slight difference.
    # We'll use interpolation.

    # Interpolate x2 onto t1
    x2_interp = np.interp(t1, t2, x2[:, 0])

    # Compute the difference between x1 and interpolated x2
    diff = np.max(np.abs(x1[:, 0] - x2_interp))
    print(f"Gate 7 - Step refinement:")
    print(f"  Max difference between h={h1} and h={h2} solutions: {diff:.2e}")

    # For independent re-simulation, we need a different solver.
    # We don't have another fractional solver implemented, but we can use a very small step size
    # with the same PECE method as a proxy? Alternatively, we can implement a simple Adams-Bashforth-Moulton
    # for fractional orders? That's complex.
    # Since the requirement is to demonstrate with an independent re-simulation (e.g., Adams-Bashforth-Moulton),
    # and we don't have that, we can note that we have not implemented an alternative solver.
    # However, we can at least show convergence with h-refinement.

    # We'll set a tolerance for the step refinement test (say 1e-4 for h=0.1 vs h=0.05?).
    # The method is expected to be convergent, so we expect the error to decrease as h decreases.
    # We can do a simple check: the error should be less than some threshold (say 1e-3) for h=0.1.
    # But note: the tolerance for gate 7 is 1e-6 for comparison between original and re-simulation.
    # We'll use 1e-4 for the step refinement as a proxy.

    step_refinement_passed = diff < 1e-4
    print(f"  Step refinement test passed (diff < 1e-4): {step_refinement_passed}")

    # For independent re-simulation, we will skip for now and note that we need to implement an alternative solver.
    # We'll mark it as not passed until we have an alternative solver.
    independent_re_simulation_passed = False  # Placeholder

    if step_refinement_passed and independent_re_simulation_passed:
        print("✓ Gate 7: Step refinement and independent re-simulation passed")
        return True
    else:
        print("❌ Gate 7: Step refinement and independent re-simulation failed")
        if not step_refinement_passed:
            print("   Step refinement test failed.")
        if not independent_re_simulation_passed:
            print("   Independent re-simulation not implemented.")
        raise AssertionError("Gate 7 failed")

if __name__ == '__main__':
    test_gate7_step_refinement_and_re_simulation()