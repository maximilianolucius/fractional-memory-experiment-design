# Research Positioning Relative to the Previous Papers

## 1. What the validated paper already supplies

The validated paper supplies a mathematically valuable ecological backbone:

- a Caputo predator–prey model with a strong prey Allee effect;
- exact locked ecological parameters;
- a certified coexistence equilibrium;
- a closed-form and machine-certified Matignon stability boundary \(\alpha^*(A)\);
- certified local bistability and global extinction/ultimate-boundedness statements;
- a methodological warning that ordinary forward Euler can invert the stability verdict.

Those results answer a **dynamical certification** question: what can be rigorously said about the system at specified parameters?

They do not answer the new question: **which perturbation and observation strategy can identify the memory mechanism?** The new paper should therefore use the certified model and parameter slice as a digital twin, not repeat the certification paper.

## 2. What `main.pdf` tries to supply

The draft `main.pdf` attempts to introduce:

- structural identifiability of fractional order;
- observational equivalence with delay and latent states;
- Bayesian model comparison;
- simulation and empirical studies.

Its high-level scientific motivation is useful. Its mathematical sections are not a reliable foundation in their current form. In particular, the draft repeatedly applies Laplace-domain linear formulas directly to nonlinear systems, asserts incorrect stability rules for multi-order/distributed-order models, and reports empirical numbers without an auditable computational artifact.

The appropriate use of `main.pdf` is therefore:

- retain the problem statement and taxonomy of confounders;
- discard or rewrite the claimed theorems;
- do not reuse the reported empirical values as results;
- move passive-data comparison to a secondary validation role.

## 3. The exact research gap for the new paper

The new paper should formalize a three-level distinction.

### Level I — exact structural separation

Under ideal continuous-frequency, noise-free observation, a noninteger Caputo transfer function is not a finite-dimensional rational transfer function. This gives an exact structural distinction.

### Level II — finite-horizon approximation barrier

The fractional kernel is an exact continuum mixture of exponentials and can be approximated by finite positive exponential sums on a finite horizon. Hence, a sufficiently high-dimensional latent model can lie below the experimental noise floor.

### Level III — optimal active separation

Given a restricted set of alternative models, actuator limits, observation costs, and a noise floor, optimize the intervention and sampling design to maximize KL divergence, mutual information, or a robust minimum pairwise separation.

This three-level structure is the paper’s mathematical spine.

## 4. Dependency graph

```text
validated dynamics paper
    ├── exact nonlinear model
    ├── certified equilibrium / Jacobian regime
    ├── safe/extinction constraints
    └── Matignon boundary
             ↓
new experiment-design paper
    ├── dimensionally consistent controlled model
    ├── linear transfer functions around certified equilibrium
    ├── exact separation vs rational/delay alternatives
    ├── finite-horizon approximation barrier
    ├── optimal input and observation theorems
    └── nonlinear Bayesian simulation benchmark
             ↓
future laboratory paper
    ├── microcosm intervention
    ├── measured environmental covariates
    └── prospective validation
```

## 5. Novelty that is defensible

A defensible novelty statement is:

> We derive active-experiment conditions that separate fractional ecological memory from finite-dimensional delay/latent alternatives, quantify when finite-horizon exponential approximations defeat that separation at a given noise floor, and solve the corresponding linear-Gaussian input and observation design problems around a certified strong-Allee predator–prey equilibrium.

This is stronger and more precise than claiming that multiscale forcing “usually works.”
