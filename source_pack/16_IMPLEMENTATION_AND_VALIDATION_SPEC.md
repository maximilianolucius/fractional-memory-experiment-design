# IMPLEMENTATION AND VALIDATION SPECIFICATION FOR FRACTIONAL SOLVER

# 16_IMPLEMENTATION_AND_VALIDATION_SPEC.md

## Overview
This document specifies the 7 gates that must be passed for the fractional Caputo solver to be considered rigorously implemented and validated.

## The 7 Gates

1. **Analytic tests**: Verify the solver reproduces the equilibrium x* = 2/3 to at least 12 decimal places for the test problem dx/dt = -x^3 + x^2, x(0)=0.5, alpha=0.3.
2. **Equilibrium time T(A)**: Compute the time to reach within 1% of x* for initial condition x(0)=A, for A in [0.1, 0.9], and verify against the analytical expression T(A) = (1/(1-alpha)) * ln((A - x*)/(0.01*A)).
3. **Decay rate D(A)**: Verify the decay rate from x(0)=A to x* matches the analytical expression D(A) = (1-alpha)*(A - x*)^alpha.
4. **Controlled equilibrium shift alpha*(0.3)**: For the controlled system dx/dt = -x^3 + x^2 + u, with u chosen to shift equilibrium to x*=0.3, verify the required constant control input matches the analytical expression u* = 0.3^3 - 0.3^2.
5. **Controllability range**: Verify that for control input u in [-0.5, 0.5], the equilibrium x* can be shifted continuously from 0.1 to 0.9.
6. **Observability range**: Verify that the output y = x^2 allows observation of x in the range [0.1, 0.9] with sufficient signal-to-noise ratio.
7. **Step refinement and independent re-simulation**: Demonstrate convergence under h-refinement (halving time step) and that an independent re-simulation with different solver (e.g., Adams-Bashforth-Moulton) yields identical results within tolerance.

## Tolerances
All numerical comparisons must use a tolerance of 1e-6 unless otherwise specified (e.g., 12 digits for analytic test).

## Implementation Notes
- The solver must be a proper fractional Caputo solver, either predictor-corrector PECE or convolution quadrature.
- The solver must handle variable step sizes if adaptive.
- The solver must be implemented in the same language as the rest of the codebase (Python).
- The solver must be encapsulated in a function with signature: solve_fractional_caputo(f, tspan, x0, alpha, h, tol) -> (t, x).

## Validation Procedure
For each gate:
1. Implement the test as a separate script.
2. Run the test using the fractional solver.
3. Compare numerical results to analytical expressions using the specified tolerance.
4. Log pass/fail and any discrepancies.

## Required Deliverables
- The fractional solver function.
- Validation scripts for each of the 7 gates.
- A manifest entry with:
    solver: fractional_solver_PECE (or similar)
    status: PASS (only after all gates pass)
    solver_tolerances: 
        status: VERIFIED
        spec: [description of what was verified]

## Notes
- The analytic test (Gate 1) must be passed at 12 digits.
- Gates 2-6 use tolerance 1e-6.
- Gate 7 uses tolerance 1e-6 for comparison between original and re-simulation.