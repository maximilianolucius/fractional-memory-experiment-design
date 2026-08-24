"""
Analytic unit tests for the predator-prey model.
"""

import numpy as np
import sys
sys.path.append('src')
from models.predator_prey import PredatorPreyModel, ModelParameters


def test_equilibrium():
    """Test the coexistence equilibrium formula."""
    model = PredatorPreyModel()
    # Test with a=0.5 (within admissible range)
    A = 0.5
    eq = model.equilibrium(A)
    x_star, y_star = eq['coexistence']
    # Expected from paper: x* = 2/3, y* = 2*(2-3A)/(9A)
    expected_x = 2.0 / 3.0
    expected_y = 2.0 * (2.0 - 3.0 * A) / (9.0 * A)
    assert np.isclose(x_star, expected_x), f"x_star: {x_star} != {expected_x}"
    assert np.isclose(y_star, expected_y), f"y_star: {y_star} != {expected_y}"
    assert eq['admissible'] == True, "Equilibrium should be admissible for A=0.5"
    
    # Test with A outside admissible range (A >= 2/3)
    A = 0.7
    eq = model.equilibrium(A)
    assert eq['admissible'] == False, "Equilibrium should not be admissible for A=0.7"
    
    print("Equilibrium test passed.")


def test_jacobian():
    """Test the Jacobian at coexistence."""
    model = PredatorPreyModel()
    A = 0.5
    J = model.jacobian(A)
    # Expected from paper: J = [[(7A-2)/(8A), -1/2], [(2-3A)/(10A), 0]]
    expected_J = np.array([
        [(7.0*A - 2.0) / (8.0*A), -0.5],
        [(2.0 - 3.0*A) / (10.0*A), 0.0]
    ])
    assert np.allclose(J, expected_J), f"Jacobian mismatch:\n{J}\nvs\n{expected_J}"
    
    # Check trace and determinant
    T = np.trace(J)
    D = np.linalg.det(J)
    expected_T = (7.0*A - 2.0) / (8.0*A)
    expected_D = (2.0 - 3.0*A) / (20.0*A)
    assert np.isclose(T, expected_T), f"Trace mismatch: {T} != {expected_T}"
    assert np.isclose(D, expected_D), f"Determinant mismatch: {D} != {expected_D}"
    
    print("Jacobian test passed.")


def test_transfer_function_shape():
    """Test that the transfer function returns a complex number."""
    model = PredatorPreyModel()
    alpha = 0.8
    omega = 1.0
    G = model.transfer(alpha, omega)
    assert isinstance(G, complex), f"Transfer function should return complex, got {type(G)}"
    print("Transfer function shape test passed.")


if __name__ == '__main__':
    test_equilibrium()
    test_jacobian()
    test_transfer_function_shape()
    print("All analytic unit tests passed.")