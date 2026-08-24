# Experimental Design for Fractional Memory Ecological Systems

## Overview
This document outlines the experimental design for distinguishing fractional, delayed, and latent ecological memory mechanisms in predator-prey systems with strong Allee effects.

## Core Experimental Design

### System Under Study
We consider the dimensionally consistent Caputo predator-prey model with strong Allee effect:
```
τ₀^(α-1) ⁰D_t^α z(t) = f(z(t);θ) + Bu(t)
y(t) = Cz(t)
```
where z = [x,y]ᵀ represents prey (x) and predator (y) populations.

### Memory Hypotheses to Test
1. **Fractional Memory**: Memory kernel follows power-law decay t^(α-1)/Γ(α)
2. **Delayed Memory**: Discrete time-delay representation
3. **Latent Memory**: Finite-dimensional latent state approximation

## Experimental Protocol

### Phase 1: Baseline Characterization
- Establish coexistence equilibrium (x* = 2/3, y* = 2(2-3A)/9A)
- Verify system stability for α < α*(A) ≈ 0.969 (for A=0.3)
- Measure natural decay rates following small perturbations

### Phase 2: Perturbation Experiments
Apply controlled perturbations:
1. **Prey pulses**: Brief increases in prey population
2. **Predator pulses**: Brief increases in predator population
3. **Chirp signals**: Frequency-swept inputs for frequency response measurement

### Phase 3: Measurement Protocol
- High-frequency sampling immediately post-perturbation (dt = 0.01τ₀)
- Extended monitoring to capture long-term memory effects (up to T = 50τ₀)
- Dual-species monitoring to capture cross-species memory effects

## Fractional Memory Signatures

### Temporal Signature
- **Fractional**: Power-law decay y(t) ~ t^(-α)
- **Delayed**: Exponential decay with time delay
- **Latent**: Multi-exponential decay

### Frequency Domain Signature
- **Fractional**: Constant phase angle -(1-α)π/2 in intermediate frequencies
- **Delayed**: Linear phase shift -ωτ
- **Latent**: Rational function approximation

## Recent Findings Incorporated (2024-2025)

- Fractional derivatives with Mittag-Leffler kernels provide better fit to ecological memory data than power-law kernels (see source_pack/17_BIBLIOGRAPHY.md and docs/math_appendix.md Section 119-123)
- Distributed order fractional derivatives can capture more complex memory effects than single-order fractional derivatives (see docs/math_appendix.md Section 125-130)
- Variable order fractional derivatives allow modeling of time-varying memory properties (see docs/math_appendix.md Section 132-137)
- Hybrid fractional-delay models capture both long-term memory and immediate feedback effects
- Distributed delay models can approximate fractional dynamics but require commensurate orders
- Fractional-order experiment design under model-accuracy constraints (Jakowluk & Świercz, 2025) provides minimum-power LMI input, which can be adapted for ecological systems while considering safety constraints (see 20_RELATED_WORK_POSITIONING.md)

## Recent Findings Incorporated (2024)
- Fractional derivatives with Mittag-Leffler kernels provide better fit to ecological memory data than power-law kernels (see source_pack/17_BIBLIOGRAPHY.md and docs/math_appendix.md Section 119-123)
- Distributed order fractional derivatives can capture more complex memory effects than single-order fractional derivatives (see docs/math_appendix.md Section 125-130)
- Variable order fractional derivatives allow modeling of time-varying memory properties (see docs/math_appendix.md Section 132-137)
- Hybrid fractional-delay models capture both long-term memory and immediate feedback effects
- Distributed delay models can approximate fractional dynamics but require commensurate orders

## Safety Constraints
All experiments must maintain:
- Population bounds: 0 < x,y < 10 (normalized units)
- Control effort: ||u(t)|| ≤ 1.0
- Minimum prey threshold: x(t) > A (Allee threshold)

## Data Analysis Protocol
1. Preprocessing: Detrend and normalize time series
2. Model fitting: Compare fractional, delayed, and latent models using:
   - Akaike Information Criterion (AIC)
   - Bayesian Information Criterion (BIC)
   - Cross-validation error
3. Residual analysis: Check for remaining structure in residuals
4. Parameter uncertainty: Profile likelihood or MCMC sampling

## Expected Outcomes
Discrimination between memory mechanisms based on:
- Decay exponent estimation
- Phase shift measurements
- Model comparison metrics
- Residual structure analysis

## Linearized Model and Transfer Functions
Based on source pack documentation, the linearized model around equilibrium is:
```
τ₀^(α-1) ⁰D_t^α ξ(t) = Jξ(t) + Bu(t)
y(t) = Cξ(t)
```
where the transfer function is:
```
G_α(s) = C(τ₀^α s^α I - J)^(-1)B
```

For the specific case where CB ≠ 0:
```
G_α(s) = (CB)τ₀^(1-α)s^(-α) + O(|s|^(-2α))
```

This yields the frequency response:
```
|G_α(iω)| = |CB|τ₀^(1-α)ω^(-α)
∠G_α(iω) = -(1-α)π/2 + arg(CB)
```

## Controllability and Observability
Based on source pack analysis:
- Prey-only intervention (u₁) and predator-only intervention (u₂) provide independent control channels
- The system is controllable and observable for the strong-Allee model with parameters r=3/2, K=1, a=1, h=1/2, e=4/5, m=2/5
- The Jacobian at equilibrium (x*=2/3, y*=2(2-3A)/9A) has the form:
  J = [T  -c]
      [d   0]
  where T, c, d are functions of equilibrium point and parameters.