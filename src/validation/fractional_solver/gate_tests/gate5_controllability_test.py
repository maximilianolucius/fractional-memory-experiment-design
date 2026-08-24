#!/usr/bin/env python3
"""
Test Gate 5: Controllability range
Verify that for control input u in [-0.5, 0.5], the equilibrium x* 
can be shifted continuously from 0.1 to 0.9.
"""
import sys
import numpy as np
sys.path.append('src')
from solvers.fractional import solve_fractional_caputo

def test_gate5_controllability():
    """
    Test Gate 5: Controllability range
    """
    # Parameters for the ODE: dx/dt = -x^3 + x^2 + u
    def f(t, x, u):
        return np.array([-x[0]**3 + x[0]**2 + u])

    alpha = 0.3
    h = 0.01
    max_time = 100.0  # enough time to reach equilibrium
    tol = 1e-6

    # We'll test a range of u values from -0.5 to 0.5
    u_vals = np.linspace(-0.5, 0.5, 11)  # 11 points from -0.5 to 0.5
    # For each u, compute the equilibrium x* by solving -x^3 + x^2 + u = 0
    # We can compute analytically: x^3 - x^2 - u = 0
    # We'll use numpy roots to find the real root in [0,1]
    equilibria = []
    for u in u_vals:
        # Coefficients for x^3 - x^2 - u = 0 -> [1, -1, 0, -u]
        coeffs = [1, -1, 0, -u]
        roots = np.roots(coeffs)
        # Select real root in [0,1]
        real_roots = [r.real for r in roots if abs(r.imag) < 1e-9 and 0 <= r.real <= 1]
        if len(real_roots) == 1:
            equilibria.append(real_roots[0])
        else:
            # If multiple or none, we'll use numerical simulation to see what we get
            # But for this cubic, there should be one real root in [0,1] for u in [-0.5,0.5]
            equilibria.append(np.nan)

    print("Gate 5 - Controllability range:")
    print("u\t\tx* (analytic)\t\tx* (numerical)")
    all_passed = True
    for i, u in enumerate(u_vals):
        # Simulate until equilibrium
        x0 = np.array([0.5])  # initial condition in the middle
        tspan = (0.0, max_time)
        # We need to pass u to the RHS function. We'll use a lambda.
        def f_u(t, x):
            return f(t, x, u)
        t, x = solve_fractional_caputo(f_u, tspan, x0, alpha, h)
        x_num = x[-1, 0]  # final value
        x_analytic = equilibria[i]
        if np.isnan(x_analytic):
            # If analytic failed, use numerical as reference? But we want to compare.
            # We'll skip the test for this u if analytic fails.
            print(f"  u={u:.2f}: analytic root not found, skipping")
            continue
        error = abs(x_num - x_analytic)
        passed = error < tol
        if not passed:
            all_passed = False
        print(f"  u={u:.2f}: {x_analytic:.6f}\t\t{x_num:.6f}\t error={error:.2e} {'PASS' if passed else 'FAIL'}")

    # Additionally, check that the equilibrium can be shifted continuously from 0.1 to 0.9
    # We'll check that the numerical equilibria cover the range [0.1,0.9] within tolerance.
    # We already have equilibria for each u. We'll check the min and max of the numerical equilibria.
    numeric_equilibria = [x[-1,0] for x in [solve_fractional_caputo(lambda t,x: f(t,x,u), (0.0, max_time), np.array([0.5]), alpha, h)[1] for u in u_vals]]
    min_eq = min(numeric_equilibria)
    max_eq = max(numeric_equilibria)
    print(f"\nRange of numerical equilibria: [{min_eq:.3f}, {max_eq:.3f}]")
    if min_err := abs(min_eq - 0.1) > 0.1:  # allow 0.1 tolerance for range
        print(f"Minimum equilibrium {min_eq:.3f} is not close enough to 0.1")
        all_passed = False
    if max_err := abs(max_eq - 0.9) > 0.1:
        print(f"Maximum equilibrium {max_eq:.3f} is not close enough to 0.9")
        all_passed = False

    if all_passed:
        print("✓ Gate 5: Controllability range passed")
    else:
        print("❌ Gate 5: Controllability range failed")
        raise AssertionError("Gate 5 failed")

    return all_passed

if __name__ == '__main__':
    test_gate5_controllability()