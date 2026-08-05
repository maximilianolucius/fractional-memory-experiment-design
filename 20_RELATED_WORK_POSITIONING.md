# Related Work and Defensible Novelty Positioning

## 1. The closest prior-art cluster

The nearest literature is not generic fractional ecology. It is the intersection of:

1. optimal input/experiment design for fractional-order identification;
2. model-discrimination design for dynamic biological systems;
3. structural identifiability of fractional systems;
4. ecological predator–prey experimentation.

### Fractional-order experiment design

| Work | Main target | What it does not provide for this paper |
|---|---|---|
| Malti, Mayoufi & Victor (2022), FOED01 | experiment design for elementary fractional models | no ecological competing-mechanism design; no safe Allee constraints |
| Jakowluk (2019), FOED02 | optimal input for fractional parameter identification | uses an approximation/identification objective rather than Caputo-vs-DDE-vs-latent discrimination |
| Sebastià Bargues et al. (2023), FOED03 | D-optimal frequencies for fractional bioimpedance | parameter precision in a fixed model; not model-class discrimination |
| Jakowluk & Świercz (2025), FOED04 | minimum-power LMI input under model-accuracy constraints | not ecological, not Bayesian model discrimination, not safety-constrained |

### Dynamic model-discrimination design

| Work | Main contribution | Missing element addressed here |
|---|---|---|
| Atkinson & Fedorov (1975), O01–O02 | T-optimal rival-model discrimination | no memory operators or dynamic ecological safety |
| Skanda & Lebiedz (2010), O10 | dynamic biochemical model discrimination | integer-order biochemical systems; no fractional approximation barrier |
| Flassig & Sundmacher (2012), O11 | robust stimulus design under uncertainty | no Caputo/DDE/latent structural separation theorem |
| Bayesian OED literature O05–O09 | expected information gain and computational methods | no paper-specific ecological mathematics or certified safe domain |

### Fractional identifiability

| Work | Main contribution | Distinction |
|---|---|---|
| Kharazmi et al. (2021), I06 | integer/fractional identifiability and predictability with PINNs | passive inverse problem rather than active ecological design |
| Varalda & Pequito (2026), I07 | graph-structural identifiability in fractional-order networks | discrete-time network structure, not continuous Caputo ecological mechanism discrimination |

## 2. Correct novelty statement

Do not write:

> “We introduce optimal experimental design for fractional-order systems.”

That claim is false in light of FOED01–FOED04.

Write instead:

> We develop a safety-constrained active-discrimination framework for ecological memory mechanisms. Around a certified strong-Allee predator–prey equilibrium, we derive conditions and optimal designs that separate a commensurate Caputo model from classical ODE, delay, and bounded-dimension latent-state alternatives, while quantifying the finite-horizon noise barrier created by exponential-mixture approximations.

## 3. Theoretical novelty components

The paper’s mathematical novelty should be expressed as the combination of:

1. **exact ideal separation:** a noninteger Caputo input–output transfer cannot be identical to a finite-dimensional rational latent-state transfer under the stated channel assumptions;
2. **exact DDE distinction:** fractional branch behavior is not identical to a finite discrete-delay quasi-polynomial transfer;
3. **finite-horizon limitation:** exponential mixtures approximate the fractional kernel below any fixed tolerance when latent dimension is unrestricted;
4. **design solution:** the pairwise energy-constrained optimum is the dominant eigenfunction of the model-difference operator;
5. **robust frequency support:** an optimal robust spectral design can be chosen with finite support under the finite-comparison formulation;
6. **safe informativeness:** an interior equilibrium with nonzero model separation admits sufficiently small perturbations that remain inside a declared safe set.

No single reference above supplies this package.

## 4. Empirical novelty components

An experimental contribution is defensible only if the paper delivers:

- a declared actuator channel with physical units;
- feasible pulse/chirp/multisine constraints;
- measurement variables and schedules;
- a fixed complexity cap on latent alternatives;
- pre-registered model-discrimination metrics;
- safety margins tied to the Allee threshold;
- out-of-family stress tests.

The microbial systems in E10–E12 are precedents for controlled predator–prey experimentation, not automatic validation of the proposed interventions.

## 5. Recommended related-work subsection structure

1. Fractional ecological dynamics: E06–E09.
2. Identifiability of fractional models: I06–I08.
3. Classical and Bayesian model-discrimination design: O01–O09.
4. Dynamic biological stimulus design: O10–O12.
5. Fractional-order experiment/input design: FOED01–FOED04.
6. Remaining gap and contribution statement.

## 6. Reviewer-facing comparison table

| Dimension | Existing fractional OED | Existing dynamic biological discrimination | Proposed paper |
|---|---:|---:|---:|
| Fractional operator | Yes | Usually no | Yes |
| Competing ODE/DDE/latent mechanisms | Rare/no | Competing ODE mechanisms | Yes |
| Exact structural separation theorem | No for this ecological comparison | No | Yes |
| Finite-horizon latent approximation barrier | No | No | Yes |
| Optimal perturbation | Yes | Yes | Yes |
| Optimal observation schedule | Sometimes | Yes | Yes |
| Strong-Allee safety constraint | No | No | Yes |
| Certified ecological baseline | No | No | Yes |
| Bayesian nonlinear extension | Limited | Yes | Yes |

This table should be updated only after the final implementation determines which columns are actually delivered.
