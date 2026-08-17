# Fractional-delay numerical extension

## Model and purpose

The new simulation model carries both Caputo memory and an explicit trophic delay. It is designed as a numerical stress test that bridges the two previously competing explanations rather than as an additional headline theorem.

The numerical implementation is in:

`benchmark/fractional_delay_experiments.py`

## Validation gates

At `A=0.25`, `tau=0.35`, `T=6`, the `alpha=1` fractional-delay solver converges to the independent DDE RK4 solver:

| N | max absolute difference |
|---:|---:|
| 200 | 6.75e-6 |
| 400 | 1.68e-6 |
| 800 | 4.20e-7 |

For the representative fractional-delay cell `(alpha,tau)=(0.85,0.35)`, the max difference versus the N=800 solution decreases from `2.18e-3` at N=200 to `8.05e-4` at N=400.

The `tau=0` boundary delegates directly to the validated pure Caputo solver.

## Design stress test

For `alpha={0.75,0.85,0.95}`, `tau={0.15,0.30,0.45}`, `A=0.25`, and the common peak-amplitude budget:

| Design | Mean minimum distance to Caputo/DDE limits | Allee-crossing fraction |
|---|---:|---:|
| multisine | 0.1332 | 0.333 |
| PRBS | 0.0909 | 1.000 |
| sinusoid | 0.0894 | 1.000 |
| chirp | 0.0861 | 1.000 |
| pulse | 0.0627 | 0.000 |
| multiscale | 0.0338 | 0.000 |

The new study therefore reproduces the paper's central safety-information trade-off inside a model that contains fractional memory and delay simultaneously.

## Reproducibility

Run:

```bash
python benchmark/fractional_delay_experiments.py
```

Outputs include the four PDF figures, JSON validation data, design-ranking JSON, and the `(alpha,tau)` bridge data.
