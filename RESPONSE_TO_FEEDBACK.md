# Response to the requested Q1 revisions

## 1. Restructure the paper and highlight the main contributions

Completed. The main manuscript was rebuilt around a conventional model-methods-results structure, closer to the previous validated paper:

1. Introduction
2. Ecological Model and Competing Memory Mechanisms
3. Analytical Backbone: Four Results Used by the Experiments
4. Numerical Methods and Validation
5. Frequency-Domain and Finite-Horizon Numerical Evidence
6. Fractional-Delay Model: Dedicated Simulation Study
7. Experiment Design and Safety
8. Large-Scale Model-Discrimination Benchmark
9. Prospective Experimental Interpretation
10. Discussion
11. Conclusion

The Introduction now states four contributions explicitly. Figure 1 was regenerated to show the new paper architecture.

## 2. Reduce the number of theoretical results

Completed substantially beyond the requested threshold.

- Previous main manuscript: ~50 pages, 20 theorem environments.
- Revised main manuscript: **19 pages total**, with **4 theorem environments**.
- The main analytical development occupies only the early part of the paper (roughly the first 6-7 pages including the ecological model), well below the requested 29-page theoretical limit.
- Detailed proofs, secondary theorems, safety derivations, optimal-design proofs, and the Bayesian extension were moved to a **39-page Supplementary Material** rather than deleted.

The four main-text analytical results are only those required to interpret the experiments:

1. structural separation;
2. finite-horizon latent approximation / complexity barrier;
3. complexity-dependent testing obstruction;
4. interval-certified finite-state approximation of the ecological prey response.

## 3. Strengthen the experimental/numerical part

Completed.

The main paper now gives numerical evidence its own sections rather than treating simulations as a final validation appendix. It contains:

- solver and limiting-case validation;
- frequency-domain response figures;
- finite-horizon approximation and testing atlas;
- six input waveforms and design ranking;
- nonlinear safety geometry;
- large four-class model-discrimination benchmark;
- confusion matrix, alpha sensitivity, SNR/channel sensitivity, and safety-information trade-off;
- a new dedicated fractional-delay simulation study.

The revised main text contains **19 figures**.

## 4. Add simulations and graphical illustrations for the delay-fractional model

Completed with a new combined model:

\[
\tau_0^{\alpha-1}{}^CD_t^\alpha x
=P(x;A)-\frac{axy}{1+hx}+u(t),
\]
\[
\tau_0^{\alpha-1}{}^CD_t^\alpha y
=e\frac{a x(t-\tau)y(t)}{1+h x(t-\tau)}-my.
\]

It has the exact numerical limits needed for interpretation:

- \(\tau=0\): pure Caputo model;
- \(\alpha=1\): retarded DDE benchmark.

Four new main-text figures were generated:

- **Fig. 9**: fractional-delay trajectories for increasing delay;
- **Fig. 10**: heat maps over the \((\alpha,\tau)\) plane showing distance to pure Caputo, distance to pure DDE, and minimum Allee margin;
- **Fig. 11**: input-design ranking for exposing fractional-delay dynamics together with Allee-crossing fraction;
- **Fig. 12**: delay sweep showing predator-peak timing, peak amplitude, and safety-margin changes.

No large exploratory computation campaign was launched. These are targeted experiments using the existing ecological backbone and benchmark input families.
