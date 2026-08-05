# Proposal Compliance Matrix

## Source comparison

- **Original proposal:** *Optimal Experimental Design for Identifying Ecological Memory*.
- **Resulting manuscript:** *Fractional Memory Experiment Design: Active and Safe Discrimination between Fractional, Delayed, and Latent Memory via Optimal Excitation*.

The manuscript is best interpreted as an attempted minimum-viable subset of the proposal, not execution of the complete proposed program.

---

| Proposal component | Manuscript status | Audit finding | Required action |
|---|---|---|---|
| Active discrimination instead of passive fitting | Implemented conceptually | Central framing is present | Retain |
| ODE model | Present | Defined locally and used in benchmark | Clarify nonlinear benchmark form |
| Caputo model | Present | Defined with dimensional scaling | Clarify initialization and fitted parameters |
| DDE model | Partial | Linear form given; nonlinear benchmark unspecified | Give exact equations, delay placement, history, parameter domain |
| Finite latent-state model | Partial | Generic LTI form; benchmark coupling unspecified | Define latent dynamics, signs, rates, coupling, fitting |
| Distributed-order model | Missing | Mentioned only as future work | Remove from scope or implement |
| Nonparametric memory kernel | Missing | Not included in benchmark | Remove from scope or implement |
| Colored process noise | Missing | Listed as robustness axis only | Implement or mark as future work |
| Time-varying parameters | Missing | Not tested | Implement or remove from current claims |
| Model discrepancy | Aspirational | Alternative functional responses listed but no results shown | Supply results or move to limitations |
| Single pulse | Implemented | Included in rankings | Define exact normalization |
| Repeated pulses | Partial | Multiscale family used, exact waveform absent | Give waveform and optimization variables |
| Chirp | Implemented | Included in rankings | Specify band, sweep, phase, energy |
| PRBS | Partial | Linear results only; omitted from nonlinear ranking | Include nonlinear results or explain exclusion |
| Multisine | Partial | Family tested; theoretical optimum not shown | Report optimized frequencies and weights |
| Adaptive intervention | Not implemented | Equation given only | Implement sequential loop or remove empirical claim |
| Prey-only observation | Claimed | Structural analysis present | Report benchmark results by channel |
| Predator-only observation | Claimed | Structural analysis present | Report benchmark results by channel |
| Both species | Claimed | Appears in planned matrix | Give actual factor levels and outcomes |
| Environmental covariate | Not implemented | Only prospective PBH-style rule | Move to future protocol |
| Expected model information gain | Theoretical only | No numerical EIG result | Implement or remove benchmark claims |
| Robust maximin criterion | Theoretical only | Finite-support theorem present; no solved design reported | Show LP solution and achieved worst-case score |
| Parameter estimation | Missing | No RMSE, intervals, or coverage | Implement or narrow paper to model selection |
| Bayesian posterior probabilities | Missing | Benchmark uses BIC | Choose Bayesian evidence or rewrite statistical framing |
| Posterior entropy | Missing | No result | Implement if retained as metric |
| Expected log predictive density | Missing | No result | Implement or remove |
| False discovery rate for fractional memory | Missing | No result | Implement or remove |
| Safety probability | Missing | Zero numerical divergence substituted | Compute actual safety metrics |
| Safe intervention theorem | Partial | Main argument needs stricter assumptions; appendix invalid | Reprove and numerically instantiate |
| Structural frequency separation | Substantially present | Useful but scope must be narrowed | Retain with corrected hypotheses |
| Non-discriminating input / impossibility result | Partial | Kernel-level result valid; nonlinear conclusion overbroad | Add nonlinear error propagation or narrow claim |
| Persistent-excitation condition | Missing as such | Broadband heuristics and fixed-pair design given | State a precise identifiability theorem or remove claim |
| Sample-complexity lower bound | Missing | No testing-error or sample-size theorem | Add or remove from contribution list |
| Large simulation benchmark | Claimed | 189,000 trials reported; artifacts absent | Attach code/results and repair inconsistencies |
| Alternative priors | Missing | Listed only | Run sensitivity analysis |
| Non-Gaussian noise | Missing | Listed as future work | Do not claim robustness to it |
| Missing observations | Missing | Listed only | Run dropout experiments |
| Intervention error | Missing | Listed only | Run actuator-error experiments |
| Solver approximation error | Partial | Scalar solver table only | Propagate numerical error into classification outcomes |
| Laboratory validation | Missing | Prospective protocol only | Label section explicitly prospective |
| Calibrated digital twin | Partial | Strong-Allee baseline used | Explain calibration source and uncertainty |
| Reproducible repository | Claimed but not delivered | Paths named in PDF only | Attach archive/repository snapshot |

---

## Minimum viable paper test

The proposal’s minimum viable paper required:

- one predator–prey baseline;
- ODE, Caputo, delay, and latent mechanisms;
- pulse, multiscale pulse train, and chirp;
- prey-only and both-species observation regimes;
- expected model-information gain;
- one robust-design criterion;
- a large simulation benchmark;
- one analytical identifiability or frequency-response result.

### Assessment

| Minimum requirement | Status |
|---|---|
| One baseline | Met |
| Four mechanisms | Nominally met, but benchmark definitions incomplete |
| Three intervention families | Met |
| Two observation regimes | Not demonstrated in results |
| Expected model-information gain | Not implemented numerically |
| Robust design criterion | Formulated but not solved/reported |
| Large benchmark | Claimed, not independently reproducible |
| Analytical frequency result | Met with scope corrections |

The manuscript therefore does **not yet satisfy its own minimum viable paper specification**.

---

## Recommended scope decision

### Option A — Fastest defensible paper

Restrict the paper to:

- ODE, Caputo, retarded DDE, and latent exponential mixtures;
- linearized structural results;
- stable-only nonlinear benchmark;
- fixed and bounded-complexity rival classes;
- exact equal-energy input comparisons;
- deterministic safety margins;
- BIC or likelihood-based selection, consistently described.

Move full Bayesian sequential design to a second paper.

### Option B — Full proposal paper

Add:

- priors and posterior inference;
- evidence calculations;
- expected mutual-information optimization;
- adaptive intervention sequence;
- parameter recovery;
- robustness axes;
- missing-data and non-Gaussian experiments;
- posterior safety constraints;
- complete code and diagnostics.

This is substantially more work and should not be implied by the current benchmark.
