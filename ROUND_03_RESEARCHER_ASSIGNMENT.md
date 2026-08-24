# ROUND 03 — RESEARCHER ASSIGNMENT

**Branch:** `rescue/aims-desk-rejection`  
**Role:** Researcher under Chief review  
**Round objective:** convert the Round-02 rescue from a strong but partially empirical/provisional story into a manuscript-ready theorem/certificate package.

Read first:

1. `CHIEF_REVIEW_ROUND_02.md`
2. `ROUND_02_DECISION.md`
3. `THEOREM_B_ENDPOINT_COMPLEXITY_PROOF.md`
4. `THEOREM_C_PRIME_FINAL.md`
5. `THEOREM_D_NONLINEAR_LIFT.md`
6. `R2_OPERATOR_BRIDGE.md`
7. `SAFE_BENCHMARK_V4_REPORT.md`
8. `R2_MANDATORY_MANUSCRIPT_CORRECTIONS.md`

The purpose of this round is **not** to defend Round 02. Attempt to falsify it. Any theorem that fails must be downgraded immediately.

---

# R3-A — rigorous repair of Theorem B.2

## Objective

Produce a publication-grade endpoint-inclusive positive-SOE theorem, or downgrade the statement to the strongest theorem actually proved.

The current target is root-exponential order. The exact boundary constant is **not assumed**.

### Mandatory tasks

1. Rebuild the proof around an **infinite logarithmic trapezoidal/sinc grid plus explicit truncation**, not a finite left rule to which an infinite-grid theorem is applied implicitly.
2. Separate and bound:
   - infinite-grid discretization error;
   - negative-index tail;
   - positive-index tail;
   - endpoint-integrated error.
3. Repair the endpoint estimate. Use
   \[
   \int_0^\delta K_m(t)\,dt
   =\sum_j\frac{c_j}{\lambda_j}(1-e^{-\lambda_j\delta})
   \]
   and split rates at `\lambda\approx1/\delta`, or give another rigorous bound that removes the spurious `\delta L^{1-\alpha}` inflation.
4. Handle the analytic-strip boundary correctly. Either:
   - prove the exact boundary exponent using Poisson summation / Mellin transform / a quantitative version of the trapezoidal theorem; or
   - state the safe result
     \[
     \forall c<\pi\sqrt{\alpha(1-\alpha)}\quad
     \exists A(\alpha,c):
     \varepsilon_m^{rel}\le A(\alpha,c)e^{-c\sqrt m}.
     \]
5. Correct the complexity inversion. No coefficient-one sufficiency statement may survive hidden prefactors.
6. Give exact dependencies of all constants on `α` and any auxiliary `c,d`.
7. Search the literature adversarially for prior endpoint-inclusive `L^1(0,T)` positive-exponential/sinc/SOE results. Include at least:
   - exponential/sinc quadrature for fractional powers;
   - Beylkin–Monzón style exponential approximations;
   - McLean-type exponential-sum approximations;
   - Jiang–Zhang and successors;
   - rational/Stieltjes approximation literature relevant to positive residues.
8. If the result is not novel after this search, relabel it as a lemma/tool and do not headline it.

### Stretch target

Attempt a **lower bound** for positive `m`-term exponentials showing that root-exponential complexity is optimal or near-optimal in the endpoint-inclusive relative `L^1` norm. Even a lower bound over a restricted positive class would materially strengthen the result and reopen the FCAA split option.

### Deliverable

`R3_THEOREM_B_RIGOROUS.md`

Must contain:

- final theorem statement;
- full proof;
- exact status of boundary constant;
- literature novelty table;
- corollary for `m(ε)`;
- explicit list of statements retracted from Round 02.

---

# R3-B — response-level operator semantics and T23 audit

## Problem

The current definition

\[
E_m^G=\|\mu_F-\mu_m\|_\infty/\|u\|_\infty
\]

is ambiguous between a fixed-input quotient and an induced operator norm.

A waveform-uniform testing theorem requires a uniform gain.

## Tasks

1. Locate the exact mathematical object certified by `thm:T23` and its scripts.
2. Distinguish, with separate notation:
   \[
   E_{m,u}^{resp}:=\frac{\|\mu_F(u)-\mu_m(u)\|_\infty}{\|u\|_\infty},
   \]
   \[
   \mathcal E_m^{op}:=
   \sup_{u\ne0}
   \frac{\|(\mathcal G_F-\mathcal G_m)u\|_\infty}{\|u\|_\infty},
   \]
   and, where applicable,
   \[
   E_m^{imp}:=\|g_F-g_m\|_{L^1(0,T)}.
   \]
3. Prove all inequalities connecting these quantities.
4. Determine whether T23 certifies `E_m^{imp}`, `\mathcal E_m^{op}`, or only `E_{m,u}^{resp}` for a prescribed waveform.
5. Rewrite Theorem C′ accordingly.
6. Formalize the composite minimax risk from first principles. Define the null, rival family, test class, loss, and the exact two-point reduction. Remove any factor ambiguity.
7. Verify dimensions/units throughout.

### Deliverables

- `R3_RESPONSE_OPERATOR_AUDIT.md`
- `R3_THEOREM_C_FINAL.md`

**Hard gate:** no claim of waveform-uniformity unless `\mathcal E_m^{op}` is actually bounded.

---

# R3-C — rigorous nonlinear safety constants

## Problem

The symbolic sufficient-ball inequality is valid, but Round 02 used sampled estimates for `M_2(r)` and numerical gain values for `Γ_B,Γ_R`.

## Tasks

1. Derive `D^2 f(x,y)` analytically for the locked strong-Allee vector field.
2. On each candidate ball/box, obtain a **rigorous upper bound** on the Hessian/operator norm and hence on
   \[
   M_2(r)=\sup_{\|\xi\|\le r}\frac{\|R(\xi)\|}{\|\xi\|^2}.
   \]
   Prefer interval subdivision with outward rounding or a closed analytic bound.
3. Rigorously enclose `Γ_B(T)` and `Γ_R(T)`:
   - interval evaluation of the Mittag-Leffler/Green function; or
   - an analytic resolvent bound with explicit constants.
4. Recompute the sufficient nonlinear amplitude.
5. Separate:
   - symbolic theorem;
   - rigorously certified numeric instantiation;
   - high-accuracy but non-certified diagnostics.
6. If the rigorous constant becomes even smaller, report it. Do not tune the method to recover a desirable number.

### Deliverable

`R3_NONLINEAR_CERTIFICATE_CONSTANTS.md`

### Gate

`U_NL(δ)` may be called **certified** only if every constant entering it has a rigorous enclosure.

---

# R3-D — validated trajectory safety classification

The main ecological story requires more than sampled PECE margins.

## Preferred route: a posteriori validated residual enclosure

For each candidate input `u`, compute a high-accuracy approximate trajectory `\tilde z(t)` and a rigorous residual enclosure for the fractional Volterra equation. Use a fractional Grönwall/resolvent estimate to certify

\[
\|z-\tilde z\|_\infty\le \eta_{val}.
\]

Then:

- **certified safe** if `\tilde x(t)-\eta_{val}>A+δ` for every `t`;
- **certified crossing** if there exists a time interval on which `\tilde x(t)+\eta_{val}<A`;
- otherwise **unresolved**.

Alternative validated-integration machinery is allowed if genuinely rigorous.

## Required designs/amplitudes first

At minimum certify or classify:

- pulse: `amp=0.050,0.063`;
- multiscale: `amp=0.050,0.063`;
- multisine: `amp=0.050,0.063`;
- PRBS: `amp=0.063`;
- sinusoid: `amp=0.063`.

Do this on the focal `A=0.25, α=0.85` cell first. Expand only after the method is validated.

## Robust-safety extension

Because the mechanism is unknown during experiment design, evaluate whether safety must hold under every candidate true mechanism. Construct the intersection

\[
\mathcal U_{safe}^{rob}
=
\bigcap_{M\in\mathcal M}
\{u: x_M(t;u)\ge A+δ\ \forall t\}.
\]

At minimum report model-wise safety. If a robust intersection can be certified, use it in the headline.

### Deliverable

`R3_VALIDATED_SAFETY_REPORT.md`

No “genuinely safe” wording without this gate.

---

# R3-E — response-level certification at m=64 and m=128

Round 01 large-`m` ecological floors were retracted because kernel error is not response error.

Attempt direct response-level certification for the focal ecological channel.

## Tasks

1. Construct stable `m=64` and `m=128` positive latent realizations using the best available log-scale/SOE nodes.
2. Certify the **observed response impulse difference** or induced `L^∞→L^∞` gain directly, not through the `C_res≈2352` kernel bridge.
3. Use interval arithmetic / outward-rounded quadrature consistent with the T23 certification machinery.
4. Verify latent-state stability and numerical conditioning.
5. If `m=128` is computationally prohibitive, obtain the strongest certified upper bound possible and document the bottleneck.

### Deliverable

`R3_RESPONSE_CERT_M64_M128.md`

### Gate

Only direct response-level certificates may feed ecological testing floors.

---

# R3-F — adversarial search for a safe and informative counterexample

This is a mandatory **falsification** task.

The current negative result covers six waveform families. Search outside them.

## Stage 1 — broad numerical search

Declare at least three finite-dimensional control families:

1. piecewise-constant `K=4,6,8` segments;
2. Fourier/multisine coefficients with 3–6 harmonics and free phases;
3. pulse-train / multiscale controls with free locations, widths, signs and amplitudes.

Use Orion for global/derivative-free search. Candidate algorithms may include Sobol + local refinement, CMA-ES, differential evolution, Bayesian optimization, or a custom maximin search.

Do **not** optimize noisy BIC accuracy first. Optimize a deterministic discrimination objective such as

\[
J(u)=\min_{i\ne j}
\frac{\|S_n(\mu_i(u)-\mu_j(u))\|_2}{\sigma}
\]

subject to a safety penalty/constraint. Then run the benchmark classifier only on the best candidates.

## Stage 2 — validate the Pareto frontier

For every candidate on the safety/information Pareto frontier:

- validated safety classification from R3-D;
- deterministic pairwise separation;
- BIC macro-accuracy with confidence intervals;
- mechanism-wise crossing status.

## Stage 3 — optional global certificate

For a modest family, e.g. `K=4` piecewise-constant inputs, attempt interval branch-and-bound to upper-bound `J(u)` over the validated-safe parameter domain.

A successful bound of the form

\[
\sup_{u\in\mathcal U_{K}^{safe}}J(u)\le J_{crit}
\]

would convert the practical-impossibility story into a **certified finite-class impossibility result**.

Failure to prove the global bound is acceptable. Failure to search for counterexamples is not.

### Deliverables

- `R3_SAFE_DESIGN_ADVERSARIAL_SEARCH.md`
- code/data under `rescue_compute/r3_safe_design_search/`

---

# R3-G — re-derive the nonlinear discrimination equation

Do not reuse Round-02 symbols until their semantic level is fixed in R3-B.

## Tasks

1. Write the nonlinear fractional and latent mild equations.
2. Subtract them exactly.
3. Identify the forcing term caused by the mechanism/operator mismatch.
4. Bound the nonlinear difference using a local Lipschitz/Hessian constant on a **validated** safe set.
5. State clearly whether the multiplier acts on:
   - kernel error;
   - linear response-operator error;
   - or an already nonlinear response error.
6. Avoid multiplying a response-level gain by another response-level gain without a derivation.
7. If no useful bound closes, say so and keep the nonlinear result empirical/certificate-based.

### Deliverable

`R3_NONLINEAR_DISCRIMINATION_AUDIT.md`

---

# R3-H — complete v4 reproducibility control

When the existing `amp=0.100` run finishes:

1. append its results to `SAFE_BENCHMARK_V4_REPORT.md`;
2. compare every cell against frozen v3 with identical seeds;
3. report mismatches and explain them;
4. do not alter v3;
5. include hash/manifests for the new raw output.

### Deliverable

`R3_V4_REPRODUCIBILITY_CONTROL.md`

This task must not restart or duplicate the running computation.

---

# R3-I — manuscript correction execution

Only after R3-A through R3-G stabilize the claim set:

1. execute `R2_MANDATORY_MANUSCRIPT_CORRECTIONS.md`;
2. delete the orphan `sec14.tex`/`sec15.tex` if they are truly unreachable and obsolete;
3. replace the companion-comparison table with one provenance paragraph;
4. fix all first-person provenance errors;
5. replace the old `thm:T20` with the R3-final response-operator theorem;
6. remove Pinsker where the exact Gaussian formula applies;
7. remove all “optimal”/Bayesian-OED claims that lack executed optimization;
8. prune uncited bibliography entries;
9. move headline proofs into the main text;
10. preserve the rejected version as a frozen baseline.

### Narrative structure

The revised paper should communicate this sequence:

1. fractional and finite-latent mechanisms are structurally different;
2. positive latent hierarchies approximate fractional memory rapidly on finite horizons;
3. **that kernel-level fact does not automatically imply ecological response indistinguishability**;
4. safe excitation in a strong-Allee system is a nonlinear constraint and the linear certificate can fail badly;
5. under the evaluated/validated safe protocol, informative sustained excitations are unsafe while non-crossing designs approach chance-level discrimination;
6. the safe/informative frontier is mapped and adversarially searched rather than assumed.

### Deliverables

- modified `paper/` sources;
- `R3_MANUSCRIPT_CHANGELOG.md`.

---

# R3-J — title, abstract, and contribution rewrite

Prepare **three title candidates**, one abstract, and a 3–4 item contribution list.

## Abstract restrictions

- 180–240 words;
- ≤4 numerical values;
- no companion-paper narrative;
- no universal “no safe excitation” claim unless R3-F certifies it over a declared class;
- distinguish PROVED, CERTIFIED, and EMPIRICAL statements;
- foreground the negative safe-discrimination result.

Suggested conceptual title direction:

> **When informative excitation is unsafe: finite-horizon discrimination of fractional and latent memory in a strong-Allee system**

Do not adopt this title automatically; produce alternatives after Round-03 results.

### Deliverable

`R3_TITLE_ABSTRACT_CONTRIBUTIONS.md`

---

# R3-K — provisional CNSNS compliance matrix

Create a compliance matrix against the **current official CNSNS/Elsevier instructions**.

This is preparatory only; do not migrate to `elsarticle` until the Chief approves the Round-03 science.

Required policy remains:

- **100% of mandatory requirements PASS**;
- **≥99% of complete applicable checklist PASS**;
- official instructions/template refreshed again within 24 h of actual submission.

### Deliverable

`CNSNS_COMPLIANCE_MATRIX_DRAFT.md`

---

# R3-L — updated claim/evidence ledger and decision memo

Update `RESCUE_CLAIM_EVIDENCE_LEDGER.md` with strict statuses:

- `PROVED`
- `CERTIFIED_NUMERICALLY`
- `VALIDATED_TRAJECTORY`
- `EMPIRICAL`
- `CONJECTURAL`
- `RETRACTED/REMOVE`

Every headline sentence proposed for the manuscript must map to one ledger row.

Create `ROUND_03_DECISION.md` answering:

1. What is the strongest true headline after adversarial safe-design search?
2. Is Theorem B.2 fully rigorous, and what constant is actually proved?
3. Is its novelty sufficient to remain a headline?
4. Is Theorem C′ genuinely waveform-uniform?
5. Which designs are validated safe, validated crossing, or unresolved?
6. Do `m=64,128` ecological response certificates exist?
7. Was a safe informative counterexample found?
8. Is any finite design class globally certified as non-discriminable?
9. Is the paper now strong enough for CNSNS?
10. Should the FCAA split remain deferred?

---

# Round-03 acceptance gates

## G3.1 — endpoint theorem rigor
PASS only if every use of trapezoidal/sinc theory matches the actual finite/infinite construction and all hidden constants are reflected honestly.

## G3.2 — operator semantics
PASS only if fixed-input response error and induced response-operator error are never conflated.

## G3.3 — nonlinear certificate rigor
PASS only if every numeric constant called “certified” has an analytic/interval enclosure.

## G3.4 — validated safety
PASS only if at least the focal candidate safe/crossing designs receive validated trajectory labels, not grid-sampled labels.

## G3.5 — large-m ecological layer
PASS if `m=64` and preferably `128` response-level enclosures are certified, or if the failure/bottleneck is rigorously documented and the manuscript does not use those values.

## G3.6 — falsification of negative result
PASS only if a broad safe-design search is executed outside the original six families.

## G3.7 — no semantic double counting
PASS only if the nonlinear difference theorem uses consistently defined operator/error quantities.

## G3.8 — v4 reproducibility
PASS after the running `amp=0.100` control is reconciled with frozen v3.

## G3.9 — manuscript claim repair
PASS only after every known false/obsolete claim is removed from the compiled paper.

## G3.10 — editorial positioning
PASS only if title/abstract/contributions distinguish theorem, certificate, and empirical result and avoid universal claims unsupported by the admissible input class.

## G3.11 — journal compliance preparation
PASS when the current CNSNS checklist is documented and the ≥99% policy is preserved.

---

# Computational policy

- Orion: use for large parallel search, response certification grids, and Monte Carlo.
- Aureus: 32 cores; do not assume 100. Use a conservative worker count consistent with current load.
- Do not overwrite frozen v3 or Round-02 raw data.
- Every long computation must be restartable and checkpointed.
- Keep raw outputs and scripts under versioned `rescue_compute/` namespaces.

---

# Required Round-03 deliverables

1. `R3_THEOREM_B_RIGOROUS.md`
2. `R3_RESPONSE_OPERATOR_AUDIT.md`
3. `R3_THEOREM_C_FINAL.md`
4. `R3_NONLINEAR_CERTIFICATE_CONSTANTS.md`
5. `R3_VALIDATED_SAFETY_REPORT.md`
6. `R3_RESPONSE_CERT_M64_M128.md`
7. `R3_SAFE_DESIGN_ADVERSARIAL_SEARCH.md`
8. `R3_NONLINEAR_DISCRIMINATION_AUDIT.md`
9. `R3_V4_REPRODUCIBILITY_CONTROL.md`
10. modified `paper/` + `R3_MANUSCRIPT_CHANGELOG.md`
11. `R3_TITLE_ABSTRACT_CONTRIBUTIONS.md`
12. `CNSNS_COMPLIANCE_MATRIX_DRAFT.md`
13. updated `RESCUE_CLAIM_EVIDENCE_LEDGER.md`
14. `ROUND_03_DECISION.md`
15. versioned code/raw outputs under `rescue_compute/`

**Chief instruction:** prefer a narrower theorem that is fully true over a broad theorem with one hidden numerical or semantic assumption. The purpose of Round 03 is to make the rescue referee-resistant.
