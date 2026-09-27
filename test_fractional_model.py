#!/usr/bin/env python3
"""Quick test of the fractional predator-prey model."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from models.predator_prey import PredatorPreyModel, create_default_parameters, create_default_design
import numpy as np

def test_model():
    print("Testing predator-prey model with fractional solver...")
    model = PredatorPreyModel()
    params = create_default_parameters()
    design = create_default_design()
    # Run a short simulation
    latent, obs = model.simulate(params, design, seed=42)
    print(f"Simulation completed. Latent state shape: {latent.shape}")
    print(f"First 5 time steps of prey: {latent[:5, 0]}")
    print(f"First 5 time steps of predator: {latent[:5, 1]}")
    # Check for negative values (should be non-negative due to clipping)
    if np.any(latent < 0):
        print("ERROR: Negative values found in latent state!")
        return False
    else:
        print("SUCCESS: No negative values.")
    return True

if __name__ == "__main__":
    success = test_model()
    sys.exit(0 if success else 1)