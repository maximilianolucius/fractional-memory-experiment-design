#!/usr/bin/env python3
"""
Test Gate 2: Equilibrium time T(A)
Compute the time to reach within 1% of x* for initial condition x(0)=A, for A in [0.1, 0.9],
and verify against the analytical expression T(A) = (1/(1-alpha)) * ln((A - x*)/(0.01*A)).
"""
import sys
import numpy as np
import math
sys.path.append('src')
from solvers.fractional import solve_fractional_caputo

def test_gate2_equilibrium_time():
    """
    Test Gate 2: Equilibrium time T(A)
    """
    # Parameters for the ODE: dx/dt = -x^3 + x^2
    def f(t, x):
        return np.array([-x[0]**3 + x[0]**2])
    
    alpha = 0.3
    x_star = 2.0 / 3.0
    # We'll test for a few values of A in [0.1, 0.9]
    A_vals = [0.1, 0.3, 0.5, 0.7, 0.9]
    h = 0.01  # small step size
    max_time = 200.0  # maximum time to simulate
    
    print("Gate 2 - Equilibrium Time T(A):")
    all_passed = True
    for A in A_vals:
        x0 = np.array([A])
        tspan = (0.0, max_time)
        t, x = solve_fractional_caputo(f, tspan, x0, alpha, h)
        # Find the first time when |x - x*| <= 0.01 * x* (within 1% of equilibrium)
        # Actually, the spec says "within 1% of x*", meaning |x - x*| <= 0.01 * x*?
        # Let's interpret as |x - x*| <= 0.01 * x* (relative error)
        # But the analytical expression uses 0.01*A? Wait: T(A) = (1/(1-alpha)) * ln((A - x*)/(0.01*A))
        # That seems to be the time to reach within 1% of the initial distance? Let's re-read:
        # "Compute the time to reach within 1% of x* for initial condition x(0)=A"
        # So we want |x(t) - x*| <= 0.01 * x*? Or 0.01 * |A - x*|? The expression given uses (A - x*)/(0.01*A)
        # Actually, the expression T(A) = (1/(1-alpha)) * ln((A - x*)/(0.01*A)) suggests:
        # We want the time when the remaining error is 1% of the initial error? Let's derive:
        # For the linearized system near equilibrium, the decay is like exp(-lambda t) with lambda = (1-alpha)*(x* - A)? Not sure.
        # We'll use the given expression as the analytical target.
        # We'll compute the numerical time when |x - x*| <= 0.01 * x* (i.e., within 1% of the equilibrium value).
        # But note: the expression uses 0.01*A, which is 1% of the initial condition? That seems odd.
        # Let's look at the expression: T(A) = (1/(1-alpha)) * ln((A - x*)/(0.01*A))
        # If A > x*, then A - x* is positive. The argument of ln is (A - x*)/(0.01*A) = 100*(A - x*)/A.
        # This is the time for the error to reduce to 1% of the initial error? Because ln(error0/error) = lambda*t => t = (1/lambda) * ln(error0/error).
        # Here error0 = A - x*, and we want error = 0.01 * A? That doesn't match.
        # Actually, if we want the error to be 1% of the initial error, then error/error0 = 0.01 => t = (1/lambda) * ln(1/0.01) = (1/lambda)*ln(100).
        # But the expression has ln((A - x*)/(0.01*A)) = ln(100*(A - x*)/A) = ln(100) + ln((A-x*)/A).
        # That is not exactly ln(100) unless (A-x*)/A = 1, which is not true.
        # Let's re-examine the spec: "Compute the time to reach within 1% of x* for initial condition x(0)=A"
        # It might mean: |x(t) - x*| <= 0.01 * x* (i.e., within 1% of the equilibrium value).
        # Then the error we care about is |x - x*|. Let epsilon = 0.01 * x*.
        # We want the time when |x - x*| <= epsilon.
        # For linear decay, x(t) - x* = (A - x*) * exp(-lambda t). Then |x - x*| = |A - x*| * exp(-lambda t).
        # Set equal to epsilon: exp(-lambda t) = epsilon / |A - x*| => t = (1/lambda) * ln(|A - x*| / epsilon).
        # Here epsilon = 0.01 * x*, so t = (1/lambda) * ln(|A - x*| / (0.01 * x*)).
        # The spec says T(A) = (1/(1-alpha)) * ln((A - x*)/(0.01*A)).
        # So they are using lambda = (1-alpha) and epsilon = 0.01 * A? That doesn't match.
        # Let's check the lambda: For the ODE dx/dt = -x^3 + x^2, linearizing around x*: 
        # f(x) = -x^3 + x^2, f'(x) = -3x^2 + 2x, f'(x*) = -3*(4/9) + 2*(2/3) = -4/3 + 4/3 = 0.
        # So the linearization gives zero eigenvalue? That can't be right.
        # Wait, the ODE dx/dt = -x^3 + x^2 = x^2(1 - x). The equilibrium x*=2/3: f'(x*) = -3*(4/9)+2*(2/3)= -4/3+4/3=0.
        # So the linearization is zero, meaning the decay is not exponential? Actually, near x*, the cubic term dominates? 
        # Let's not overcomplicate. We'll use the given analytical expression as the target.
        # We'll compute the time when |x - x*| <= 0.01 * x* (within 1% of equilibrium value) and compare to the given formula.
        # But note: the given formula uses A in the denominator inside the log, which is strange.
        # Let's assume the spec is correct and use their formula as the analytical target.
        # We'll compute the numerical time when the absolute error |x - x*| is less than or equal to 0.01 * x*.
        # However, to match the formula, we might need to use a different threshold.
        # Let's read the spec again: "Compute the time to reach within 1% of x* for initial condition x(0)=A"
        # It doesn't specify relative to what. In many contexts, "within 1% of x*" means |x - x*| <= 0.01 * |x*|.
        # We'll go with that.
        # We'll compute the time when the absolute error first falls below 0.01 * x*.
        # We'll also compute the analytical expression as given and see if they match within tolerance.
        # If not, we might adjust our interpretation.
        
        # Compute numerical time when |x - x*| <= 0.01 * x*
        error_threshold = 0.01 * x_star
        # Find first index where condition is met
        abs_error = np.abs(x[:, 0] - x_star)
        below_threshold = np.where(abs_error <= error_threshold)[0]
        if len(below_threshold) == 0:
            # If never within threshold within max_time, set t_nan
            t_numerical = float('inf')
        else:
            t_numerical = t[below_threshold[0]]
        
        # Analytical expression from spec
        if A == x_star:
            t_analytical = 0.0
        else:
            # Avoid log of negative or zero
            inner = (A - x_star) / (0.01 * A)
            if inner <= 0:
                t_analytical = float('inf')
            else:
                t_analytical = (1.0 / (1.0 - alpha)) * math.log(inner)
        
        print(f"  A={A:.1f}: numerical t={t_numerical:.6f}, analytical t={t_analytical:.6f}")
        
        # Check if they are close (within 1e-6 relative or absolute?)
        if np.isinf(t_numerical) and np.isinf(t_analytical):
            passed = True
        elif np.isinf(t_numerical) or np.isinf(t_analytical):
            passed = False
        else:
            # Use relative tolerance if values are large, else absolute
            if abs(t_analytical) > 1e-6:
                rel_error = abs(t_numerical - t_analytical) / abs(t_analytical)
                passed = rel_error < 1e-6
            else:
                passed = abs(t_numerical - t_analytical) < 1e-6
        
        if not passed:
            all_passed = False
            print(f"    FAILED: difference = {abs(t_numerical - t_analytical)}")
        else:
            print(f"    PASSED")
    
    if all_passed:
        print("✓ Gate 2: Equilibrium time T(A) passed")
    else:
        print("❌ Gate 2: Equilibrium time T(A) failed")
        raise AssertionError("Gate 2 failed")
    
    return all_passed

if __name__ == '__main__':
    test_gate2_equilibrium_time()