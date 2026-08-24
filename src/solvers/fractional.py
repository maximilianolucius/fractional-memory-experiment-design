"""
Fractional order solver using PECE (Predictor-Evaluate-Corrector-Evaluate) method
for Caputo fractional differential equations.
"""
import math
import numpy as np
from typing import Callable, Tuple, Optional


class FractionalSolverPECE:
    """
    PECE solver for fractional differential equations:
        D^alpha y = f(t, y), 0 < alpha <= 1
    using Caputo derivative.
    """

    def __init__(self, f: Callable[[float, np.ndarray], np.ndarray], alpha: float, h: float):
        """
        Args:
            f: Function computing the right-hand side f(t, y).
            alpha: Fractional order (0 < alpha <= 1).
            h: Fixed step size.
        """
        if alpha <= 0 or alpha > 1:
            raise ValueError("Alpha must be in (0, 1]")
        self.f = f
        self.alpha = alpha
        self.h = h
        self.lambda_ = h**alpha / math.gamma(alpha + 2)
        # History of f values: f_history[k] ≈ f(t_k, y_k)
        self.f_history = []
        # Solution history: y_history[k] ≈ y(t_k)
        self.y_history = []
        self.t_history = []

    def solve(self, t0: float, y0: np.ndarray, t_end: float) -> Tuple[np.ndarray, np.ndarray]:
        """
        Solve the fractional ODE from t0 to t_end.

        Returns:
            t: array of time points
            y: array of solution values (shape: [n_steps+1, dim])
        """
        # Initialize
        self.f_history = []
        self.y_history = []
        self.t_history = []

        n_steps = int(round((t_end - t0) / self.h))
        # Adjust t_end to exactly n_steps * h to avoid drift
        t_end = t0 + n_steps * self.h

        t = t0
        y = y0.copy()

        self.t_history.append(t)
        self.y_history.append(y.copy())
        # Compute f at initial condition
        f0 = self.f(t, y)
        self.f_history.append(f0.copy())

        for n in range(n_steps):
            t_n = self.t_history[-1]
            y_n = self.y_history[-1]
            t_next = t_n + self.h

            # --- Predictor step ---
            # Compute predictor weights b_j^{(n+1)} for j=0..n
            b_weights = []
            for j in range(n + 1):
                # b_j = (n+1-j)^alpha - (n-j)^alpha
                term1 = (n + 1 - j) ** self.alpha
                term2 = (n - j) ** self.alpha if n - j >= 0 else 0.0
                b_weights.append(term1 - term2)
            b_weights = np.array(b_weights)

            # Predictor sum: sum_{j=0}^{n} b_j * f(t_j, y_j)
            f_hist = np.array(self.f_history)  # shape (n+1, dim)
            pred_sum = np.dot(b_weights, f_hist)  # shape (dim,)
            y_pred = y0 + self.lambda_ * pred_sum

            # Evaluate f at predicted value
            f_pred = self.f(t_next, y_pred)

            # --- Corrector step ---
            # Compute corrector weights a_j^{(n+1)} for j=0..n
            a_weights = []
            for j in range(n + 1):
                if j == 0:
                    a_weights.append(1.0)
                else:
                    # a_j = (n-j+2)^{alpha+1} + (n-j)^{alpha+1} - 2*(n-j+1)^{alpha+1}
                    term1 = (n - j + 2) ** (self.alpha + 1)
                    term2 = (n - j) ** (self.alpha + 1)
                    term3 = (n - j + 1) ** (self.alpha + 1)
                    a_weights.append(term1 + term2 - 2 * term3)
            a_weights = np.array(a_weights)

            # Corrector sum: sum_{j=0}^{n} a_j * f(t_j, y_j)
            corr_sum = np.dot(a_weights, f_hist)
            y_corr = y0 + self.lambda_ * (f_pred + corr_sum)

            # Accept corrected value
            y_next = y_corr
            f_next = self.f(t_next, y_next)

            # Store
            self.t_history.append(t_next)
            self.y_history.append(y_next.copy())
            self.f_history.append(f_next.copy())

            # Update for next iteration
            t = t_next
            y = y_next

        t_arr = np.array(self.t_history)
        y_arr = np.array(self.y_history)
        return t_arr, y_arr


def solve_fractional_caputo(f: Callable[[float, np.ndarray], np.ndarray],
                            tspan: Tuple[float, float],
                            x0: np.ndarray,
                            alpha: float,
                            h: float,
                            tol: Optional[float] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Solve fractional Caputo ODE using PECE method.

    Args:
        f: RHS function f(t, x).
        tspan: Tuple (t0, t_end) of time interval.
        x0: Initial condition.
        alpha: Fractional order (0 < alpha <= 1).
        h: Fixed step size.
        tol: Tolerance (not used in fixed-step PECE, kept for interface compatibility).

    Returns:
        t: time points.
        x: solution values.
    """
    solver = FractionalSolverPECE(f, alpha, h)
    t, x = solver.solve(tspan[0], x0, tspan[1])
    return t, x