# Fractional Memory Experiment Design — Mathematical Development Pack

## Direct answer

Yes. The proposal contains enough mathematics for a strong theoretical paper, but the mathematics should **not** be built on the identifiability claims currently written in `main.pdf`. Several of those claims are either false, stated for the nonlinear model as though it were linear, or too strong for the cited approximation results.

This pack reconstructs the project on a rigorous basis. The central tractable object is the dimensionally consistent, controlled linearization of the certified predator–prey model around a coexistence equilibrium:

\[
\tau_0^{\alpha-1}{}^C D_t^\alpha \xi(t)=J\xi(t)+Bu(t),
\qquad y(t)=C\xi(t)+\varepsilon(t).
\]

For this object, the following mathematics is solved here:

1. exact coexistence equilibrium, Jacobian, trace, determinant, discriminant, and Matignon boundary for the strong-Allee model;
2. exact controllability and observability for prey-only and predator-only interventions/measurements;
3. exact non-equivalence of a noninteger Caputo transfer function and any finite-dimensional integer-order latent-state transfer function under a direct input–output channel;
4. explicit high-frequency amplitude and phase signatures of fractional memory;
5. exact positive continuum-of-exponentials representation of the fractional kernel;
6. a constructive finite exponential-sum approximation with an explicit finite-horizon \(L^1\) error bound;
7. a no-free-lunch theorem showing that unrestricted latent dimension makes finite-horizon discrimination impossible below any prescribed noise floor;
8. the pairwise optimal input under an energy constraint as a principal singular vector/eigenfunction;
9. the optimal frequency-domain input for fixed linear models, and a finite-support theorem for robust multi-model spectra;
10. the optimal sampling times for two simple Gaussian hypotheses;
11. Fisher information and exact fractional-order sensitivities;
12. exact Gaussian classification error and replicate/sample-complexity formulas;
13. existence of a nonzero safe and informative perturbation under explicit interior-margin and local-separation assumptions;
14. sufficient inward-pointing inequalities for a safe invariant rectangle in a Caputo system.

## What is not claimed as analytically solved

The globally optimal intervention for the full nonlinear, partially observed, stochastic, multi-model Bayesian problem has no general closed form. It should be solved numerically after the analytical results above reduce and validate the design space. The distinction is important:

- **proved here:** linearized identifiability, exact transfer separation, approximation limits, Gaussian design, safety existence;
- **algorithmically specified:** nonlinear Bayesian expected information gain, posterior-averaged safety, adaptive experiments;
- **requires actual computation/data:** empirical rankings, posterior model probabilities, confusion matrices, and ecological conclusions.

## Recommended paper identity

**Primary paper:** a theorem-driven optimal experimental design paper with a controlled simulation benchmark.

**Recommended title:**

> **Optimal Excitation for Distinguishing Fractional, Delayed, and Latent Ecological Memory**

The strongest novelty is not “we fit many models.” It is:

> finite-dimensional latent models are exactly distinguishable from a Caputo model in ideal broadband experiments, but arbitrarily good finite-horizon latent approximations create a precise noise-dependent impossibility barrier; optimal excitation should therefore target the frequencies and channels that maximize the remaining separation.

## File map

- `01_RESEARCH_POSITIONING.md` — relation to the two previous papers.
- `02_MAIN_DRAFT_MATHEMATICAL_AUDIT.md` — corrections required before reusing `main.pdf`.
- `03_DIMENSIONALLY_CONSISTENT_CONTROLLED_MODEL.md` — correct controlled model and transform conventions.
- `04_EXACT_STRONG_ALLEE_BASELINE.md` — complete ecological algebra.
- `05_CONTROLLABILITY_OBSERVABILITY_AND_CHANNELS.md` — exact input/output results.
- `06_EXACT_MODEL_DISCRIMINATION_THEOREMS.md` — non-equivalence and frequency separation.
- `07_EXPONENTIAL_MIXTURES_AND_IMPOSSIBILITY.md` — constructive approximation and no-free-lunch theorem.
- `08_OPTIMAL_INPUT_DESIGN.md` — solved pairwise and robust spectral designs.
- `09_OPTIMAL_OBSERVATION_DESIGN.md` — solved sampling/variable selection subproblems.
- `10_PARAMETER_IDENTIFIABILITY_AND_FISHER_INFORMATION.md` — order sensitivities and rank conditions.
- `11_SAMPLE_COMPLEXITY.md` — exact error/replicate formulas.
- `12_SAFE_EXPERIMENT_DESIGN.md` — safe informative experiments and barrier conditions.
- `13_NONLINEAR_BAYESIAN_EXTENSION.md` — rigorous computational extension.
- `14_WORKED_ECOLOGICAL_DESIGNS.md` — concrete protocols for the certified parameter slice.
- `15_PAPER_BLUEPRINT_AND_CLAIM_MATRIX.md` — manuscript structure and admissible claims.
- `16_IMPLEMENTATION_AND_VALIDATION_SPEC.md` — implementation contract.
- `17_BIBLIOGRAPHY.md` — references.
- `THEOREM_INDEX.md` — theorem inventory.

## Recommended starting point

Start with the four-model minimum viable paper:

\[
M_{\mathrm{ODE}},\quad M_{\mathrm{Caputo}},\quad
M_{\mathrm{DDE}},\quad M_{\mathrm{latent},m},
\]

with a **fixed maximum latent dimension \(m\)**. Use the strong-Allee system from the validated paper, common order \(\alpha\), two intervention channels, and three observation regimes. Do not begin with distributed order or unrestricted learned kernels: without complexity restrictions, the discrimination problem is mathematically ill-posed on a finite horizon.
