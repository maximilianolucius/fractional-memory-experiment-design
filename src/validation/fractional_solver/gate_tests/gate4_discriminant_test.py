#!/usr/bin/env python3
"""
Test Gate 4: Verify discriminant factorization.
We use the fractional solver to simulate the system and compute the Jacobian along the trajectory?
But for simplicity, we just compute the Jacobian at equilibrium and verify the factorization analytically.
"""
import sys
import numpy as np
import math
sys.path.append('src')
from solvers.fractional import solve_fractional_caputo
from models.predator_prey import PredatorPreyModel

def test_gate4_discriminant():
    """
    Test Gate 4: Verify discriminant factorization.
    """
    # We'll use the predator prey model to compute the Jacobian and discriminant.
    model = PredatorPreyModel()
    A = 0.5  # some value in the admissible range
    J = model.jacobian(A)
    T = np.trace(J)
    D = np.linalg.det(J)
    discriminant = T**2 - 4*D
    # From source_pack/04_EXACT_STRONG_ALLEE_BASELINE.md, equation (9):
    expected_discriminant = ((19*A - 10)*(23*A - 2)) / (320 * A**2)
    # We'll also use the fractional solver to simulate the system and ensure that the Jacobian computed
    # along the trajectory is consistent? For now, we just do the analytic check.
    print(f"Gate 4 - Discriminant factorization:")
    print(f"  A={A}")
    print(f"  T={T}, D={D}")
    print(f"  discriminant={discriminant}")
    print(f"  expected={expected_discriminant}")
    error = abs(discriminant - expected_discriminant)
    tolerance = 1e-6
    print(f"  error={error}, tolerance={tolerance}")
    assert error < tolerance, f"Gate 4 failed: error {error} >= tolerance {tolerance}"
    print("✓ Gate 4: Discriminant factorization passed")
    return True

if __name__ == '__main__':
    test_gate4_discriminant()