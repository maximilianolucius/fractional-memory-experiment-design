# Claim-to-Citation Map

This document assigns references to the exact mathematical and methodological claims in the paper. It is designed to prevent citation drift and the reuse of unrelated sources.

## 1. Introduction and novelty

| Claim | Required citations | Editorial note |
|---|---|---|
| Fractional derivatives model hereditary/nonlocal dynamics | F01–F04 | Keep the claim general; do not claim ecological mechanism from calculus alone. |
| Fractional predator–prey systems are an established literature | E06–E09 | These papers establish application precedent, not empirical proof of genuine memory. |
| Experiment design already exists for fractional-order identification | FOED01–FOED04 | Mandatory to avoid an overstated novelty claim. |
| Novelty is active discrimination among Caputo, DDE, and latent-state ecological mechanisms under safety constraints | O01–O12, FOED01–FOED04, I07 | Phrase as the gap left after these works, not as “first OED for fractional systems.” |
| Ecological perturbation experiments are feasible in microcosms | E10–E12 | Supports the laboratory direction, not the exact proposed protocol. |

## 2. Fractional model and exact ecological baseline

| Mathematical object | Citations |
|---|---|
| Caputo derivative and initial conditions | F01–F04 |
| Dimensionally consistent scaling with a declared reference time | F02–F04 plus the dimensional derivation in this project |
| Holling type-II functional response | E01 |
| Rosenzweig–MacArthur predator–prey structure | E02 |
| Strong Allee threshold terminology | E03–E05 |
| Exact project baseline and certified parameter slice | P01 |

The reference-time factor \(\tau_0^{\alpha-1}\) is justified directly by dimensional analysis. It should be presented as a derivation, with F02–F04 supplying operator conventions rather than as a theorem copied from a source.

## 3. Local stability

| Claim | Citations |
|---|---|
| Linear commensurate sector condition | F05 |
| Validity of nonlinear linearization | F06 and/or F07 |
| Mittag–Leffler decay/stability terminology | F08 |
| Two-dimensional or multi-order cautions | F10 |
| No exact autonomous periodic orbit under the standard hypotheses | F09 |
| Certified baseline boundary \(\alpha^*(A)\) | P01 |

Never cite F05 alone for a nonlinear theorem. The recommended combination is `F05 + F06`.

## 4. Controllability, observability, and structural identifiability

| Claim | Citations |
|---|---|
| PBH controllability/observability tests | I05 |
| Structural identifiability definition | I01, I02 |
| Practical dynamic identification | I03, I04 |
| Recent fractional inverse-problem difficulties | I06 |
| Current structural identifiability in fractional networks | I07 |
| Fractional parameter-estimation precedent | I08 |

The exact 2×2 rank calculations in `05_CONTROLLABILITY_OBSERVABILITY_AND_CHANNELS.md` are original derivations and need only the standard PBH reference I05.

## 5. Caputo versus finite-dimensional latent states

| Claim | Citations |
|---|---|
| Finite-dimensional LTI transfer functions are rational | I05 |
| Fractional transfer functions contain noninteger powers/branch behavior | F02–F04 |
| DDE characteristic functions are quasi-polynomial | D01, D02 |
| Exact non-equivalence theorem | Original theorem in this project, built on the preceding standard facts |

Do not cite an exponential-sum approximation paper as proof of exact non-equivalence. Approximation and identity are separate statements.

## 6. Exponential-mixture approximation and impossibility barrier

| Claim | Citations |
|---|---|
| Positive diffusive representation of the fractional kernel | K02, F02–F04 |
| Constructive exponential-sum approximation | K03, K04 |
| Fast tolerance-controlled Caputo implementation | K05, K06 |
| Numerical convolution quadrature | K01, K06 |
| Finite-horizon no-free-lunch theorem | Original theorem; K02–K05 justify the approximation machinery |

Every approximation statement must include:

1. the target kernel;
2. the interval, normally \([\delta,T]\) rather than including the singular endpoint without qualification;
3. the norm;
4. the dependence on tolerance and number of exponentials;
5. how kernel error propagates to output error.

## 7. Optimal input design

| Claim | Citations |
|---|---|
| Classical T-optimal discrimination | O01, O02 |
| KL discrimination with non-Gaussian outputs | O03 |
| Robust/maximin T-optimality | O04 |
| Dynamic model-discrimination experiments | O10, O11, O12 |
| Pairwise energy-constrained eigenfunction solution | Original Hilbert-space/Rayleigh-quotient derivation; cite I04 and O01 for context |
| Fractional-order optimal input precedents | FOED01, FOED02, FOED04 |
| Frequency-selection precedent in fractional bioimpedance | FOED03 |

The paper must explicitly distinguish:

- parameter information, e.g. D- or A-optimality;
- pairwise model separation, e.g. T-optimality or KL divergence;
- Bayesian expected model information;
- robust minimum pairwise separation.

## 8. Optimal observation times and variables

| Claim | Citations |
|---|---|
| Fisher-information design | I02, O05 |
| Dynamic biological measurement design | O10–O12 |
| Exact Gaussian pairwise sampling result | S01–S05 plus original derivation |
| Sensor/variable selection via projected model separation | I04, O03, O06 |

## 9. Fisher information and sensitivity to fractional order

| Claim | Citations |
|---|---|
| Fisher-information framework | I02, O05 |
| Fractional parameter-identification context | I08, FOED01–FOED04 |
| Derivative of \((i\omega)^\alpha\) | F02–F04 plus direct complex-calculus derivation |

The formulas in `10_PARAMETER_IDENTIFIABILITY_AND_FISHER_INFORMATION.md` are derivations, not quoted results.

## 10. Sample complexity and model error

| Claim | Citations |
|---|---|
| KL divergence | S01, S03 |
| Chernoff exponent | S02, S03 |
| Gaussian detection error | S04, S05 |
| Replicate/sample-complexity formula | Original specialization of standard Gaussian testing theory |

## 11. Safe experiment design

| Claim | Citations |
|---|---|
| Caputo existence and continuous dependence | F03, F04, F11 |
| Safe ecological domain and Allee threshold | E03–E05, P01 |
| Certified baseline safety information | P01, V01, V02 |
| Existence of a sufficiently small safe informative perturbation | Original continuity/separation theorem in this project |

The project theorem is local. It must not be described as a global safe-control theorem.

## 12. Nonlinear Bayesian extension

| Method | Correct citations |
|---|---|
| Bayesian OED and expected information gain | O05–O09 |
| Simulation-based nonlinear OED | O06, O07 |
| Neural mutual-information estimator | O08 |
| HMC/NUTS | B01, B02 |
| Particle MCMC | B03 |
| Simulation-based calibration | B04 |
| Predictive validation / PSIS-LOO | B05 |
| WAIC theory | B06 |

No claim that these methods were run may appear until code, diagnostics, and outputs exist.

## 13. Empirical/laboratory section

| Proposed content | Citations |
|---|---|
| Microbial predator–prey microcosm design | E10, E11 |
| Long nonlinear food-web dynamics | E12 |
| Holling/Allee ecological interpretation | E01–E05 |
| Fractional ecological comparison class | E06–E09 |
| Dynamic perturbation optimization | O10–O12 |

## 14. Citation density recommendation

- Introduction: 15–22 distinct references.
- Mathematical model and stability: 8–12.
- Related work/OED: 12–18.
- Bayesian computation: cite only methods actually used.
- Discussion: reuse citations; do not introduce unsupported new literatures.

A compact manuscript should contain approximately 45–60 references, of which at least half should be directly load-bearing rather than broad background.
