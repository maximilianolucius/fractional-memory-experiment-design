# Academic Audit of *Fractional Memory Experiment Design*

## Scope

This audit compares the submitted 55-page PDF, *Fractional Memory Experiment Design: Active and Safe Discrimination between Fractional, Delayed, and Latent Memory via Optimal Excitation*, against the original proposal, *Optimal Experimental Design for Identifying Ecological Memory*.

The PDF was reviewed page by page, including its rendered layout, theorem statements, proofs, tables, numerical claims, bibliography, and correspondence with the proposal.

**Important limitation:** only the PDF was attached in this turn. The LaTeX source, benchmark code, JSON outputs, manifest, and raw simulation logs claimed in Section 10 were not provided. Therefore, the numerical benchmark is audited for internal consistency but cannot be independently reproduced or verified.

---

## Editorial verdict

**Current decision: reject in present form / invite resubmission after major reconstruction.**

The central research question is viable, but the manuscript is not submission-ready. The most serious defects are not cosmetic:

1. a central Bayesian theorem is mathematically false as stated;
2. several appendix proofs contradict or fail to prove the corresponding main-text theorems;
3. the numerical benchmark does not implement the Bayesian optimal-design pipeline claimed by the paper;
4. model definitions and fitting procedures are insufficient to interpret the reported classification rates;
5. several numerical statements contradict the displayed confusion matrix;
6. safety is asserted but not numerically certified;
7. the document contains unresolved LaTeX commands and source-pack references;
8. the bibliography is malformed and appears before the manuscript body.

A journal referee would not be able to determine which claims are theorems, which are heuristic design principles, and which are supported by computation.

### Indicative scores

| Dimension | Score | Assessment |
|---|---:|---|
| Research question | 7/10 | Important and falsifiable |
| Mathematical correctness | 4/10 | Several valid derivations, but central errors remain |
| Statistical methodology | 3/10 | Bayesian framework stated but not executed |
| Numerical evidence | 2/10 | Internally inconsistent and not reproducible from the submission |
| Reproducibility | 1/10 | Code and result artifacts not attached |
| Bibliography | 2/10 | Severe BibTeX and placement defects |
| Editorial quality | 2/10 | Broken references, raw markup, duplicated proofs |
| Overall readiness | 3/10 | Requires reconstruction, not line editing |

---

# 1. P0 defects: must be corrected before any submission

## P0.1 — Theorem 9.3 is false as written

Section 9.5 defines

\[
\widetilde q(M)=\mathbb E_Y[p(M\mid Y_{1:n},Y)]
\]

and then claims

\[
I(M;Y_{n+1}\mid Y_{1:n},d_{n+1})
=
D_{\mathrm{KL}}\!\left(\widetilde q\,\|\,p(M\mid Y_{1:n})\right).
\]

This is false. By the tower property,

\[
\mathbb E_Y[p(M\mid Y_{1:n},Y,d)]
=
p(M\mid Y_{1:n}),
\]

so the displayed KL divergence is identically zero.

The correct identity is

\[
I(M;Y_{n+1}\mid Y_{1:n},d)
=
\mathbb E_{Y_{n+1}\mid Y_{1:n},d}
\left[
D_{\mathrm{KL}}\!\left(
 p(M\mid Y_{1:n},Y_{n+1},d)
 \|\
 p(M\mid Y_{1:n})
\right)
\right].
\]

The appendix gives this expected-KL form, which directly contradicts the main theorem. The main theorem, its proof, Equation (67), the discussion, and the conclusion must be replaced.

The additional claim that greedy one-step mutual-information maximization “minimizes the number of experiments” is not generally valid. Such a result requires additional assumptions, for example adaptive submodularity, a specific stopping loss, or a dynamic-programming argument.

---

## P0.2 — The appendix does not prove the main results

The proof appendix should not be retained in its current form.

### Theorem 7.1

The appendix states that the “optimal amplitude” is \(\sqrt{P\lambda_{\max}(Q)}\). The energy-constrained optimal input is instead

\[
u^*=\sqrt P\,v_{\max}.
\]

The quantity \(\sqrt{P\lambda_{\max}(Q)}\) is associated with the norm of the whitened output separation, not the input amplitude.

### Theorem 7.5

The main proof correctly invokes Carathéodory’s theorem for a vector of \(P\) continuous pairwise scores. The appendix replaces this with a Fejér–Riesz argument requiring a nonnegative trigonometric polynomial. That assumption is absent from the theorem, and the zero-count argument does not prove the stated support bound. Delete the appendix proof and retain a corrected Carathéodory proof.

### Theorem 7.7

The main theorem concerns selecting time–channel observations without coupling constraints. The appendix changes the problem to frequency selection with a minimum-separation constraint. It is a different theorem.

### Theorem 8.1

The appendix claims that an \(L^\infty\)-ball is compact in the norm topology and invokes the extreme-value theorem. This is false in infinite-dimensional \(L^\infty\). It also changes the theorem from existence of a small informative perturbation to existence of a global maximizer.

### Theorem 8.4

The appendix introduces a nonsmooth max function \(V\), a quasimonotonicity assumption, and an inequality \({}^CD_t^\alpha V\le -\eta V\) that is not derived from the face conditions. It is not a proof of the theorem in the main text.

### Theorem 9.1

The main theorem permits a nonlinear observation map. The appendix replaces it by a linear-Gaussian approximation and then claims a Gaussian posterior. This requires a Gaussian prior and does not prove the nonlinear statement.

### Theorem 9.3

The appendix uses the correct expected posterior KL identity, whereas the main theorem uses the KL of the expected posterior. The manuscript is internally contradictory.

**Required action:** remove Section 14 and rebuild it theorem by theorem. Do not retain two incompatible proofs of the same result.

---

## P0.3 — The benchmark does not test the paper’s claimed Bayesian OED method

Sections 9 and 13 present the contribution as a nonlinear Bayesian sequential experimental-design framework based on expected mutual information, nested Monte Carlo, posterior updates, chance constraints, and adaptive design.

Section 10 instead reports classification by **Bayesian Information Criterion**. It does not report:

- posterior model probabilities;
- expected model information gain;
- nested Monte Carlo estimates;
- evidence-estimator convergence;
- adaptive design iterations;
- posterior safety probabilities;
- chance-constraint feasibility;
- posterior odds;
- prior sensitivity;
- utility confidence intervals.

Therefore, the benchmark does not validate the method developed in Section 9. The discussion and conclusion nevertheless claim that posterior odds, Bayesian adaptive design, KL divergences, and safety-violation rates confirm the theory. Those quantities are not shown.

The paper must choose one of two coherent versions:

1. **Linear/robust OED + BIC benchmark:** remove claims that full Bayesian adaptive OED was implemented.
2. **Bayesian OED paper:** actually implement the posterior, marginal likelihoods, mutual-information estimator, adaptive schedule, diagnostics, and safety probabilities.

The current hybrid is not defensible.

---

## P0.4 — The numerical results are not reproducible from the submitted material

Section 10 claims that all numbers are read from files such as:

- `benchmark/*.py`;
- `benchmark/results/*.json`;
- `state_nl.jsonl`;
- `artifacts/manifests/manifest.json`.

None of these artifacts is embedded in the PDF or included with the submission. The PDF contains no attachments. Consequently, the following cannot be verified:

- exact model equations used by the simulator;
- parameter grids and priors;
- waveform normalization;
- random-number generation;
- BIC likelihood and penalty definitions;
- optimization procedure;
- solver tolerances;
- safety checks;
- confusion-matrix aggregation;
- the stated runtime and worker count.

“No numbers are hand-entered” is not a reproducibility result. The submission needs a code archive or repository snapshot, environment lockfile, executable manifest, and machine-readable result tables.

---

## P0.5 — The benchmark model classes are insufficiently defined

The paper never gives the concrete nonlinear DDE and latent-state models used in Section 10. It is unclear:

- where the delay enters the ecological vector field;
- whether one or several state components are delayed;
- how \(A_0,A_1,\tau\) are chosen or estimated;
- how latent modes couple to prey, predator, and intervention;
- whether latent coefficients are positive, signed, diagonal, or general;
- which parameters are known and which are fitted;
- whether rival models are calibrated to have matching equilibrium and local response;
- how many free parameters each BIC model has;
- how the fractional order is searched;
- how DDE histories and Caputo initialization are specified.

Without this information, high accuracy can simply reflect poorly matched rival models rather than successful memory discrimination.

A valid discrimination benchmark must first calibrate all rival classes to the same passive baseline, equilibrium, and low-frequency behavior. Active inputs should then be evaluated on their ability to separate mechanisms that were intentionally made difficult to distinguish.

---

## P0.6 — The experiment confounds memory discrimination with stability discrimination

The benchmark varies \(A\in\{0.25,0.30,0.40\}\). For the integer-order Jacobian,

\[
T(A)=\frac{7A-2}{8A}.
\]

Thus the ODE equilibrium has positive trace for \(A>2/7\approx0.2857\). At \(A=0.30\) and \(A=0.40\), the ODE skeleton is locally unstable, while selected fractional models can remain stable.

This means part of the classification task can be solved by detecting growth versus decay, not by identifying the shape of memory. The paper itself acknowledges this distinction in Sections 2 and 11, but the main benchmark mixes the regimes.

**Required redesign:**

- use a **stable-versus-stable primary benchmark**, for example \(A<2/7\), to test memory-kernel discrimination;
- report the \(A>2/7\) stability-verdict experiment separately as an easier stress-test;
- stratify every accuracy and information metric by stability regime;
- do not average the two tasks into one headline result.

---

## P0.7 — The displayed confusion matrix contradicts the prose

The matrix in Table 5 is

| True / Predicted | ODE | Caputo | DDE | latent3 |
|---|---:|---:|---:|---:|
| ODE | 26104 | 290 | 327 | 279 |
| Caputo | 20331 | 58159 | 1491 | 1019 |
| DDE | 4595 | 362 | 21273 | 770 |
| latent3 | 11836 | 1503 | 4680 | 35981 |

From this table:

- total count = \(189000\), consistent with \(945\times200\);
- diagonal count = \(141517\);
- overall accuracy = \(141517/189000=0.74877\), consistent with the stated 0.749;
- ODE↔Caputo off-diagonal count = \(290+20331=20621\), **not 34621**;
- the Caputo row contains \(81000\) trials, not 80854 as stated in the caption.

The latent row appears to merge latent-1 and latent-3 trials, while Table 4 reports them separately. That aggregation must be explained exactly. If five data-generating classes are used and then collapsed into four decision classes, report both confusion matrices and both chance baselines.

---

## P0.8 — Claims of “theoretically optimal” designs are unsupported by the reported experiment

Theorems 7.1 and 7.5 define:

- a principal-eigenvector/eigenfunction input for a fixed pair;
- a maximin spectral-measure optimization for finitely many fixed pairs.

The benchmark compares named heuristic waveform families: PRBS, pulse, multiscale, multisine, sinusoid, and chirp. It does not show that:

- the principal eigenfunction was computed;
- the maximin linear program was solved;
- the multisine frequencies and weights are optimal;
- the constrained waveform is the projection or solution of the theoretical program;
- the observation schedule is the top-\(n\) or constrained optimum.

Consequently, the benchmark can support the statement “broadband families performed better in this grid,” but not “the theoretically optimal experiment was validated.”

PRBS is also omitted from the nonlinear ranking, so the nonlinear study cannot confirm the complete linear ranking in Table 2.

---

## P0.9 — The safety claims are not numerically certified

The paper claims zero unsafe divergence and states that the optimal design respects a safety rectangle. However, it does not report:

- the numerical rectangle \([x_L,x_U]\times[y_L,y_U]\);
- the certified distance \(\rho\);
- the calculated \(\Gamma_T\);
- the resulting amplitude ceiling \(\rho/\Gamma_T\);
- values of the four boundary inequalities;
- minimum prey abundance relative to \(A\);
- posterior or robust safety probabilities;
- the number of safety-triggered terminations;
- interval enclosures or numerical error margins.

“Zero solver divergence” is not equivalent to ecological safety. A trajectory may remain numerically finite while crossing the Allee threshold or leaving the certified neighborhood.

The reference to Theorem 9.1 as explaining zero divergence is also incorrect: Theorem 9.1 is a Bayes-update identity, not a stability or safety theorem.

---

## P0.10 — Theorem 8.4 needs stronger assumptions or a cited viability theorem

The first-exit argument can be made plausible under **strict inward-pointing inequalities** and an interior initial condition. The theorem currently uses non-strict inequalities and then treats

\[
0\le F_i(t^*,z(t^*))={}^CD_t^\alpha z_i(t^*)\le0
\]

as a contradiction. It is not a contradiction without strictness.

The degenerate case is handled informally, and the appendix proof is unrelated. A safe version is:

- assume \(z(0)\in\operatorname{int}R\);
- require a uniform margin \(F_i\ge\eta>0\) on lower faces and \(F_i\le-\eta<0\) on upper faces;
- invoke a precisely stated Caputo extremum principle;
- then prove no first boundary hit is possible.

If non-strict invariance is desired, use an established fractional viability/invariance theorem and verify all of its hypotheses.

---

## P0.11 — The finite-horizon no-free-lunch theorem is overextended

Theorems 6.3–6.5 establish approximation of the scalar kernel and its convolution with a fixed input:

\[
\|(k_\alpha-k_m)*u\|_2
\le
\|k_\alpha-k_m\|_1\|u\|_2.
\]

That is a valid linear convolution result. It does **not by itself** prove that the full nonlinear Caputo predator–prey input–output map can be approximated below any noise floor by a finite latent ODE.

To extend the result to the nonlinear model, the paper needs:

- a Volterra integral formulation of the nonlinear Caputo system;
- a common invariant/trust region;
- Lipschitz and boundedness assumptions on the nonlinear vector field;
- a continuous-dependence estimate propagating kernel error to state/output error;
- a construction showing that the finite exponential mixture corresponds to the admitted latent-state class.

Until then, Corollary 6.6 must be described as a **linearized fixed-input impossibility result**, not a universal finite-data theorem for arbitrary nonlinear ecological memory hypotheses.

---

## P0.12 — The bibliography is not submission quality

The reference list occupies pages 1–5, before the introduction. Numerous entries reveal malformed BibTeX author fields and metadata, for example:

- “Caputo and M.” instead of “Caputo, M.”;
- “Holling and C. S.”;
- “Kailath and T.”;
- “Diethelm and K.”;
- broken ISBN-like page fields such as “Springer:978–3” and “pages 978–0”;
- duplicated journal information in the Oikos entry;
- a malformed Chaos entry: `Chaos, 170:**170**, 2023`;
- inconsistent capitalization of titles and journal names;
- the unpublished source-pack manuscript used as Reference [1].

The bibliography must be regenerated from verified BibTeX records. References belong after the conclusion and appendices. Project drafts should be cited with complete authorship and a stable repository identifier, or the relevant derivations should be made self-contained.

---

# 2. P1 mathematical and methodological corrections

## P1.1 — The model count and shared-order statement are inconsistent

Section 3 says “three competing model classes” and then lists four: ODE, Caputo, DDE, and latent. It also says all models share the same fractional order \(\alpha\), although the ODE, DDE, and latent models are defined with integer derivatives.

Replace this by a precise common-backbone statement: the models share the same equilibrium, ecological Jacobian skeleton, input matrix, observation operator, and units; only the memory operator differs.

---

## P1.2 — Theorem 5.4 requires a compact frequency band

A nonzero analytic function has isolated zeros, but the zero set along an unbounded imaginary-axis interval can be countably infinite with accumulation only at infinity or a boundary. The proof incorrectly says the exceptional set is finite.

State the theorem on a compact band \([\omega_{\min},\omega_{\max}]\) contained in a common analytic domain and away from poles and the branch point. Then each pair has only finitely many zeros on that compact segment.

---

## P1.3 — Theorem 7.1 needs an attainment assumption in function space

The Rayleigh quotient gives an eigenvector automatically in a finite discretization. In an infinite-dimensional input space, the top spectral value need not be an eigenvalue unless the whitened difference operator is compact or another attainment condition is imposed.

State either:

- the theorem only for the finite-dimensional discretized design used in computation; or
- \(A=R^{-1/2}\Delta H\) is compact, so \(Q=A^*A\) is compact, self-adjoint, and positive, and its largest eigenvalue is attained.

---

## P1.4 — Theorem 7.5 does not solve composite-model discrimination as written

The finite-support result is valid for finitely many fixed continuous score functions \(w_p\). It does not automatically prevent a parameter-tunable latent family from fitting all selected frequencies.

For composite alternatives, the robust program contains infinitely many parameter-indexed constraints. A finite support bound then requires discretization, an equivalence theorem, or a semi-infinite programming argument. The sentence claiming that \(P+1\) tones “deny the adaptive latent model the frequency on which it could cheat” must be weakened.

---

## P1.5 — The DDE non-equivalence theorem is narrower than the prose

Theorem 5.2 treats a strictly proper **retarded**, finite-state, single-discrete-delay transfer function

\[
C(sI-A_0-A_1e^{-s\tau})^{-1}B.
\]

It does not cover neutral DDEs, derivative outputs, direct feedthrough, distributed delays, or arbitrary delay operators. Replace “any finite-delay model” by the exact class proved.

A DDE is infinite-dimensional as a dynamical system. Avoid calling it a “finite-dimensional delay model”; use “finite state dimension with finitely many discrete delays.”

---

## P1.6 — The generic phase statement is misapplied to cross channels

Equation (15) gives the direct-channel asymptotic phase when \(CB\neq0\):

\[
\arg G_\alpha(i\omega)\to-\alpha\pi/2.
\]

For a cross channel with \(CB=0\), the leading term is generally proportional to \(s^{-2\alpha}\), so the asymptotic phase is different. Section 7.6 should not attribute the direct-channel gap \((1-\alpha)\pi/2\) to cross-species phase coupling.

---

## P1.7 — Caputo prehistory is incorrectly described

Section 9.8 states that a standard Caputo derivative beginning at zero depends on an arbitrary history \(z(\tau)\) for \(\tau\in[-T_{\mathrm{pre}},0]\). A standard Caputo initial-value problem uses initial values at its lower terminal, not a DDE-like prehistory function.

A prehistory can enter through an initialized fractional derivative or a chosen memory initialization model, but that formulation must be defined explicitly.

---

## P1.8 — The latent-dimension cap \(m\le5\) is unsupported

The manuscript states that \(m\le5\) is consistent with “known ecological complexity constraints.” No result or citation establishes such a universal bound.

Present \(m_{\max}\) as a declared experimental-model complexity budget and perform sensitivity analysis over several caps. Do not give it a biological interpretation without evidence.

---

## P1.9 — Theorem 9.1 overstates its linear reduction

Bayes’ rule in Equations (63)–(64) is correct under conditional independence. However:

- a nonlinear Gaussian observation model has a Gaussian likelihood conditional on parameters, not generally a Gaussian posterior;
- a likelihood linear in parameters integrates analytically only with compatible priors, especially Gaussian priors;
- the model-discrimination operator \(Q=\Delta H^*R^{-1}\Delta H\) comes from differences in predictive means, not from a generic “gradient at zero parameter perturbation.”

Rewrite the theorem as a proposition defining the posterior and state separately the special linear-Gaussian conjugate case.

---

## P1.10 — The robust KL objective can remain zero even with bounded latent dimension

A finite cap on \(m\) does not guarantee positive minimax separation. Model classes can overlap at boundary or degenerate values, for example:

- \(\alpha\to1\) versus an ODE;
- \(\tau\to0\) versus an ODE;
- zero latent coupling;
- parameter settings producing identical sampled outputs.

Positivity requires compact parameter sets and an explicit exclusion of intersections, or a positive minimum distance under the selected design.

---

## P1.11 — The safety projection is not an optimal constrained design

Pointwise saturation of the unconstrained eigenvector can strongly alter frequency content and is not generally the optimizer of the box/rate/budget constrained problem.

The correct wording is: saturation produces a feasible candidate and lower bound on achieved information. The constrained design must be re-optimized or compared against the unconstrained upper bound.

The instruction to “increase the box” when a face condition fails can also weaken safety and is not a mathematical remedy.

---

## P1.12 — “Zero divergence” is not a safety metric

Report the actual safety quantities:

\[
\min_t(x(t)-A),\quad
\min_t(x(t)-x_L),\quad
\min_t(y(t)-y_L),
\]

maximum upper-bound excursions, face-condition margins, and numerical enclosures. Solver non-divergence should be reported separately.

---

# 3. Proposal-to-manuscript assessment

The manuscript implements only part of the original proposal.

## Material substantially delivered

- active rather than passive discrimination framing;
- ODE, Caputo, DDE, and finite latent alternatives;
- exact local Jacobian and transfer channels;
- high-frequency structural separation;
- finite-horizon exponential approximation argument;
- pairwise energy-optimal linear input;
- finite-support result for fixed pairwise scores;
- distinction between parameter estimation and model discrimination;
- a prospective safety layer;
- a large claimed simulation campaign.

## Material missing or only aspirational

- distributed-order models;
- learned/nonparametric memory kernels;
- colored process noise and time-varying parameters as fitted alternatives;
- passive-observation baseline;
- full Bayesian model evidence and expected information gain;
- adaptive Bayesian design in the benchmark;
- parameter recovery for \(\alpha,\tau\), latent rates, and ecological parameters;
- posterior entropy and false-discovery analysis;
- non-Gaussian noise experiments;
- missing-data experiments;
- prior sensitivity;
- intervention-amplitude uncertainty;
- solver-bias analysis inside the model-selection result;
- actual environmental covariate design;
- empirical or laboratory validation;
- safety probability or validated safety certificate.

The paper may legitimately adopt the proposal’s “minimum viable paper,” but it must say so and remove claims that the complete proposal was executed.

---

# 4. Editorial and LaTeX defects

## Broken commands and source-pack leakage

The rendered PDF contains literal unresolved tokens, including:

- `citeP01`;
- `citeF08`;
- `citeF02`;
- `refsec:benchmark`;
- `refsec:separation`;
- `refsec:bayesian`;
- `textttsource_pack/...`.

It also references Theorems T1–T3 and T7–T9 that are not presented under those labels in the manuscript.

## Raw Markdown inside LaTeX

The “Minimum simulation matrix” is printed as raw pipe-delimited Markdown rather than a LaTeX table.

## Visible hyperlink borders

Colored hyperlink rectangles are visible throughout the rendered PDF. Use `hidelinks` or a journal-compatible link style.

## Missing figures

The paper promises heatmaps, frequency separation, optimal spectra, solver convergence, confusion structure, and robustness surfaces, but contains no scientific figures. At minimum, include:

1. transfer magnitude and phase for all rival mechanisms;
2. optimized spectral weights;
3. waveform comparison under equal energy and amplitude;
4. solver convergence plot;
5. stable-only and mixed-regime confusion matrices;
6. accuracy/information versus \(\alpha\), delay, SNR, and horizon;
7. safety-margin trajectories;
8. robustness heatmaps actually generated from the benchmark.

## Abstract

The abstract is too short, calls the design “definitive,” and reports no quantitative result. It should state:

- the exact problem and model scope;
- the main theoretical results with qualifications;
- the benchmark design;
- one or two verified quantitative results;
- the principal limitation.

## Redundancy

Many proofs appear in full in the main text and again in incompatible form in the appendix. The paper should be shortened after correctness is restored.

## Language defects

Examples include:

- “Gaussanity”;
- “Dagnooptimization”;
- “worst-case Salien trajectory”;
- “for every prey value in of x”;
- “amplification of the model set” instead of expansion;
- ambiguous “pre-emption removal by positive predator pulses.”

These are symptoms of insufficient final editing, but they are secondary to the mathematical defects.

---

# 5. Required benchmark redesign

## 5.1 Define a difficult and fair rival-model ensemble

For every generated model class:

1. enforce the same coexistence equilibrium;
2. match steady-state gain where possible;
3. calibrate low-frequency recovery to passive data;
4. fit rival parameters before evaluating active discrimination;
5. specify admissible parameter domains and complexity penalties;
6. distinguish fixed-model and composite-model experiments.

## 5.2 Separate two scientific tasks

### Task A — Memory-shape discrimination

Use parameters for which all rival models are stable. This is the main scientific task.

### Task B — Stability-verdict discrimination

Use \(A>2/7\) where ODE and Caputo may predict different stability. Report this as a separate, easier task.

## 5.3 Implement one coherent statistical decision rule

For a Bayesian paper, report:

- priors and prior predictive checks;
- marginal likelihood or posterior model probabilities;
- nested estimator bias/variance diagnostics;
- simulation-based calibration where applicable;
- expected mutual information with Monte Carlo confidence intervals;
- adaptive sequence and stopping rule.

If BIC is retained, describe the paper as a frequentist/information-criterion benchmark and remove Bayesian posterior claims.

## 5.4 Report balanced metrics

The class counts are unequal. Report:

- macro-averaged accuracy;
- balanced accuracy;
- per-class recall and precision;
- five-class and collapsed four-class confusion matrices;
- cell-level uncertainty, not only replica-level uncertainty;
- worst-case rather than only mean performance;
- performance stratified by \(A,\alpha\), SNR, horizon, and observation channel.

## 5.5 Verify safety independently of solver success

For every trial, log:

- minimum distance above the Allee threshold;
- minimum distance to each rectangle face;
- maximum actuator magnitude and cumulative impact;
- safety termination status;
- numerical error bound;
- robust/chance constraint value.

## 5.6 Make every claim traceable

Each table and figure should be generated from a named machine-readable artifact with:

- schema;
- seed;
- code commit;
- environment hash;
- command line;
- checksum;
- timestamp;
- exact aggregation script.

---

# 6. Recommended reconstructed paper

## Suggested title

**Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator–Prey Model**

Avoid “definitive.”

## Defensible novelty claim

> The paper develops a safety-constrained active model-discrimination framework for distinguishing Caputo, retarded-delay, and bounded-complexity latent-state mechanisms around a strong-Allee ecological equilibrium. It combines exact linear transfer-function separation, a finite-horizon exponential-approximation obstruction, and computable input/observation designs, then evaluates them in a stable-versus-stable nonlinear benchmark.

## Recommended structure

1. Introduction and precise novelty
2. Common ecological backbone and rival memory classes
3. Scope and assumptions
4. Structural separation on collocated channels
5. Linearized finite-horizon approximation barrier
6. Fixed-model and composite-model OED
7. Safety constraints and certified feasible set
8. Numerical methods and reproducibility protocol
9. Stable-versus-stable benchmark
10. Separate stability-verdict benchmark
11. Robustness and model discrepancy
12. Prospective microcosm protocol
13. Limitations
14. Conclusion
15. Correct proof appendix
16. References

---

# 7. Submission gates

The manuscript should not be resubmitted until all of the following are true:

- [ ] Equation (67) and Theorem 9.3 are corrected.
- [ ] Every appendix proof matches its theorem.
- [ ] Theorem 8.4 has valid assumptions and proof.
- [ ] The nonlinear scope of the no-free-lunch result is either proved or narrowed.
- [ ] Fixed and composite model discrimination are separated.
- [ ] The actual DDE and latent benchmark equations are given.
- [ ] The benchmark separates stable-only and stability-verdict regimes.
- [ ] The confusion-matrix inconsistencies are corrected.
- [ ] PRBS treatment is consistent across linear and nonlinear comparisons.
- [ ] Bayesian claims match the implemented inference method.
- [ ] Code, data, environment, and JSON outputs are attached.
- [ ] Safety margins are numerically reported and certified.
- [ ] Raw LaTeX commands and source-pack references are eliminated.
- [ ] The bibliography is rebuilt and moved to the end.
- [ ] The abstract and conclusion report only demonstrated results.
- [ ] All figures promised by the methodology are included.

---

## Final assessment

The current PDF should not be submitted. The paper contains a publishable research direction, but the manuscript must be reconstructed around a smaller set of claims that are actually proved and actually tested. The fastest defensible route is to make the first paper a rigorous **linearized structural-discrimination plus stable-only computational benchmark**, with safety treated through explicit numerical certificates. The full nonlinear Bayesian adaptive design should either be implemented and validated or moved to a separate follow-up paper.
