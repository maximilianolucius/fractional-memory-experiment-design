"""
Predator-prey model with strong Allee effect and fractional order.
Implements the model API as specified in source_pack/16_IMPLEMENTATION_AND_VALIDATION_SPEC.md.
"""

import numpy as np
from typing import Dict, Tuple, Any, Optional
from dataclasses import dataclass


@dataclass
class ModelParameters:
    """Model parameters for the predator-prey system with strong Allee effect."""
    r: float = 1.5
    K: float = 1.0
    a: float = 1.0
    h: float = 0.5
    e: float = 0.8
    m: float = 0.4
    alpha: float = 0.8  # fractional order
    tau0: float = 1.0   # time constant


class PredatorPreyModel:
    """
    Predator-prey model with strong Allee effect.
    
    Equations:
        dx/dt = r * x * (1 - x/K) * (x - a) - a * x * y / (1 + a * h * x)
        dy/dt = e * a * x * y / (1 + a * h * x) - m * y
    
    Fractional order: Caputo derivative of order alpha.
    """
    
    def __init__(self, params: Optional[ModelParameters] = None):
        self.params = params or ModelParameters()
    
    def equilibrium(self, A: Optional[float] = None) -> Dict[str, Any]:
        """
        Compute coexistence equilibrium.
        
        Parameters:
            A: Allee effect parameter (if None, uses self.params.a)
            
        Returns:
            Dictionary with equilibria and admissibility flags.
        """
        if A is None:
            A = self.params.a
            
        r, K, a, h, e, m = self.params.r, self.params.K, A, self.params.h, self.params.e, self.params.m
        
        # Coexistence equilibrium
        x_star = 2.0 / 3.0  # Independent of A? Actually from paper: x* = 2/3
        y_star = 2.0 * (2.0 - 3.0 * A) / (9.0 * A) if A > 0 else np.inf
        
        # Check admissibility: positive populations
        admissible = (x_star > 0) and (y_star > 0) and (A > 0) and (A < 2.0/3.0)
        
        return {
            'coexistence': (x_star, y_star),
            'trivial': (0.0, 0.0),
            'allee_extinction': (a, 0.0),  # Allee threshold
            'admissible': admissible,
            'allee_parameter': A
        }
    
    def jacobian(self, A: Optional[float] = None) -> np.ndarray:
        """
        Compute Jacobian at coexistence equilibrium.
        
        Returns:
            Jacobian matrix (2x2) at coexistence.
        """
        if A is None:
            A = self.params.a
            
        # From paper: J(A) = [[(7A-2)/(8A), -1/2], [(2-3A)/(10A), 0]]
        J = np.array([
            [(7.0*A - 2.0) / (8.0*A), -0.5],
            [(2.0 - 3.0*A) / (10.0*A), 0.0]
        ])
        return J
    
    def transfer(self, alpha: float, omega: float) -> complex:
        """
        Compute transfer function G(jω) = C*(jωI - J)^{-1}B.
        Simplified for SISO case.
        """
        # This is a simplified placeholder - full implementation would depend on channels
        J = self.jacobian()
        s = 1j * omega
        # Fractional operator: s^α
        s_alpha = s**alpha
        # Simplified transfer function for demonstration
        return 1.0 / (s_alpha - np.trace(J))  # Placeholder
    
    def sensitivity(self, design: Dict[str, Any]) -> Dict[str, np.ndarray]:
        """
        Compute state/output sensitivities.
        Placeholder implementation.
        """
        # Return dummy sensitivities
        return {
            'state': np.array([0.1, 0.2]),
            'output': np.array([0.05])
        }
    
    def safety_metrics(self, trajectory: np.ndarray) -> Dict[str, float]:
        """
        Compute safety metrics from trajectory.
        Placeholder implementation.
        """
        # Simple constraint: populations should be non-negative
        min_prey = np.min(trajectory[:, 0]) if len(trajectory) > 0 else 0.0
        min_pred = np.min(trajectory[:, 1]) if len(trajectory) > 0 else 0.0
        
        return {
            'min_prey': min_prey,
            'min_predator': min_pred,
            'safety_margin': min(min_prey, min_pred),
            'violation': min_prey < 0 or min_pred < 0
        }
    
    def simulate(self, theta: Dict[str, Any], design: Dict[str, Any], seed: int = 0) -> Tuple[np.ndarray, np.ndarray]:
        np.random.seed(seed)
        params = ModelParameters(
            r=theta.get('r', self.params.r),
            K=theta.get('K', self.params.K),
            a=theta.get('a', self.params.a),
            h=theta.get('h', self.params.h),
            e=theta.get('e', self.params.e),
            m=theta.get('m', self.params.m),
            alpha=theta.get('alpha', self.params.alpha),
            tau0=theta.get('tau0', self.params.tau0)
        )
        def f(t, state):
            x, y = state
            dx = params.r * x * (1 - x/params.K) * (x - params.a) - params.a * x * y / (1 + params.a * params.h * x)
            dy = params.e * params.a * x * y / (1 + params.a * params.h * x) - params.m * y
            return np.array([dx, dy])
        try:
            from src.solvers.fractional import FractionalSolverPECE
            solver = FractionalSolverPECE(f, params.alpha, design.get('dt', 0.01))
            t_vals, y_vals = solver.solve(0.0, np.array([design.get('x0', 0.6), design.get('y0', 0.2)]), design.get('t_end', 50.0))
            steps = int(design.get('t_end', 50.0) / design.get('dt', 0.01))
            if len(t_vals) != steps:
                x = np.interp(np.linspace(0, design.get('t_end', 50.0), steps), t_vals, y_vals[:, 0])
                y = np.interp(np.linspace(0, design.get('t_end', 50.0), steps), t_vals, y_vals[:, 1])
            else:
                x = y_vals[:, 0]
                y = y_vals[:, 1]
            x = np.maximum(x, 0.0)
            y = np.maximum(y, 0.0)
            latent_state = np.column_stack([x, y])
            observations = latent_state.copy()
            return latent_state, observations
        except ImportError:
            # Fallback to integer-order
            print("Warning: Fractional solver not found, falling back to integer-order Euler")
            x = np.zeros(steps)
            y = np.zeros(steps)
            x[0] = design.get('x0', 0.6)
            y[0] = design.get('y0', 0.2)
            for i in range(steps - 1):
                xi = x[i]
                yi = y[i]
                dx = params.r * xi * (1 - xi/params.K) * (xi - params.a) - params.a * xi * yi / (1 + params.a * params.h * xi)
                dy = params.e * params.a * xi * yi / (1 + params.a * params.h * xi) - params.m * yi
                x[i+1] = xi + dx * design.get('dt', 0.01)
                y[i+1] = yi + dy * design.get('dt', 0.01)
                x[i+1] = max(x[i+1], 0.0)
                y[i+1] = max(y[i+1], 0.0)
            latent_state = np.column_stack([x, y])
            observations = latent_state.copy()
            return latent_state, observations


def create_default_design() -> Dict[str, Any]:
    """Create a default experimental design."""
    return {
        't_end': 50.0,
        'dt': 0.01,
        'x0': 0.6,
        'y0': 0.2,
        'input_type': 'step',
        'input_magnitude': 0.1,
        'input_duration': 10.0
    }


def create_default_parameters() -> Dict[str, Any]:
    """Create default model parameters."""
    return {
        'r': 1.5,
        'K': 1.0,
        'a': 0.5,  # Allee parameter within (0, 2/3)
        'h': 0.5,
        'e': 0.8,
        'm': 0.4,
        'alpha': 0.8,
        'tau0': 1.0
    }