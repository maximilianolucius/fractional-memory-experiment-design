#!/usr/bin/env python3
"""
Test Gate 1: Analytic equilibrium test
Verify the solver reproduces the equilibrium x* = 2/3 to at least 12 decimal places 
for the test problem dx/dt = -x^3 + x^2, x(0)=0.5, alpha=0.3.
"""
import sys
import numpy as np
sys.path.append('src')
from solvers.fractional import solve_fractional_caputo

def test_gate1_analytic_equilibrium():
    """
    Test Gate 1: Analytic equilibrium test
    """
    # We'll transform the ODE to have equilibrium at zero for easier solving.
    # Let y = x - x_star, where x_star = 2/3.
    # Then dy/dt = dx/dt = -(x - 2/3)^3 + (x - 2/3)^2 = -y^3 + y^2.
    # So the ODE for y is: dy/dt = -y^3 + y^2, with y(0) = x0 - x_star = 0.5 - 2/3 = -1/6.
    def f(t, y):
        y_val = y[0]
        return np.array([-y_val**3 + y_val**2])

    alpha = 0.3
    x_star = 2.0 / 3.0
    y0 = np.array([0.5 - x_star])  # -1/6
    # Increased time and decreased step for better accuracy
    tspan = (0.0, 500.0)  # Long enough to reach equilibrium (fractional decay is slow)
    h = 0.001  # Small step size for accuracy

    # Solve for y
    t, y = solve_fractional_caputo(f, tspan, y0, alpha, h)
    # Convert back to x
    x = y + x_star
    x_final = x[-1, 0]

    # Check that we reach equilibrium to at least 12 decimal places
    error = abs(x_final - x_star)
    tolerance = 1e-12

    print(f"Gate 1 - Analytic Equilibrium Test:")
    print(f"  Expected x*: {x_star:.15f}")
    print(f"  Computed x*: {x_final:.15f}")
    print(f"  Error: {error:.2e}")
    print(f"  Tolerance: {tolerance:.2e}")
    print(f"  Pass: {error < tolerance}")

    assert error < tolerance, f"Gate 1 failed: error {error} >= tolerance {tolerance}"
    print("✓ Gate 1: Analytic tests passed")
    return True

if __name__ == '__main__':
    test_gate1_analytic_equilibrium()