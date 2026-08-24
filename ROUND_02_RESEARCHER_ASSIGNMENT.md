# Round 02 — Researcher assignment

**Branch:** `rescue/aims-desk-rejection`  
**Chief source of truth:** `CHIEF_REVIEW_ROUND_01.md`  
**Round objective:** close the load-bearing mathematical gaps identified after Round 01 before any full manuscript rewrite.

---

# 0. Non-negotiable priorities

Round 02 is **not** primarily a prose/template round.

The order is:

1. repair Round-01 claim statuses;
2. separate memory-kernel error from actual input→output response error;
3. attempt a nonlinear robust-safety lift of Theorem D;
4. prove the strongest defensible endpoint-inclusive positive-SOE complexity bound;
5. run the newly authorized amplitude-controlled benchmark without overwriting v3;
6. only then produce a journal-positioning decision.

Do not hide a failed proof with softer wording. If a route fails, produce the exact obstruction and a counterexample/minimal missing hypothesis.

---

# 1. Task R2-A — repair Round-01 asymptotic claims

Audit and correct:

- `THEOREM_B_COMPLEXITY_LAW.md`
- `ROUND_01_DECISION.md`
- `RESCUE_CLAIM_EVIDENCE_LEDGER.md`

Remove any inference from finite fits that:

- the true asymptotic convergence is sub-exponential;
- it is asymptotically faster than algebraic;
- `m(ε)=O(log^κ(1/ε))` follows from C-1.

Permitted empirical wording:

> Over the tested range `m≤128`, stretched-exponential fits outperform a single algebraic fit for the tested orders; the asymptotic class remains unresolved.

Preserve Lemma B.1 as PROVED.

### Deliverable

`ROUND_01_STATUS_CORRECTIONS.md`

Include a before/after table for every corrected claim.

---

# 2. Task R2-B — operator bridge: memory kernel vs observed Green function

This is a **hard gate**.

The current rescue chain risks conflating:

- bare Caputo/diffusive kernel `K_α`;
- finite positive exponential approximation `K_m`;
- actual linearized prey input→prey output transfer/Green function `G_α`;
- actual latent-rival transfer/Green function `G_m`.

## Required work

### B1. Write the exact operator equations

For the frozen linearized system, derive the input-output operators under:

- the fractional model;
- the finite latent realization;
- any delayed model used in the discrimination set.

Define precisely where the exponential mixture enters the state dynamics.

### B2. Prove one of the following

Preferred:

\[
E_m^G:=\|G_\alpha-G_m\|_{L^1(0,T)}
\le C_{\rm res}(T,\alpha,J,B,C,\ldots)
\,E_m^K,
\]

with an explicit resolvent perturbation constant and all stability assumptions stated.

Acceptable alternative:

Do not use `E_m^K` in the ecological testing theorem at all. Formulate Theorems C′/D entirely with `E_m^G`, using T23 or a newly certified response-level approximation.

### B3. Audit the `m=64,128` floors

Determine whether the C-1 kernel errors can legitimately yield ecological error floors.

- If yes: provide the proved bridge and certified/high-confidence error propagation.
- If no: retract the ecological interpretation of `0.474` and `0.4997`; retain them only for the abstract convolution-kernel model.

### Deliverable

`R2_OPERATOR_BRIDGE.md`

**Gate B:** no manuscript may use “equivalently” between kernel-level and prey-response errors unless the bridge is proved.

---

# 3. Task R2-C — nonlinear safety theorem

This is the highest-value task.

Start from the full nonlinear strong-Allee system around coexistence:

\[
\tau_0^{\alpha-1}D_C^\alpha \xi
=J\xi+Bu+R(\xi),
\qquad R(0)=0,\quad DR(0)=0.
\]

Use the **actual nonlinear vector field**, not an abstract remainder unless all constants are later instantiated.

## C1. Explicit nonlinear remainder

For a radius `r` contained in the biologically admissible neighborhood, derive a computable constant such as

\[
\|R(\xi)\|\le M_2(r)\|\xi\|^2
\]

and/or

\[
\|R(\xi)-R(\eta)\|\le L_R(r)\|\xi-\eta\|.
\]

Use analytic derivatives/Hessian bounds where possible; interval arithmetic is strongly preferred for the final constants.

## C2. Nonlinear invariant safe ball

Write the mild fractional solution and derive a sufficient invariant-ball condition. A target shape is

\[
\Gamma_B(T)U + \Gamma_R(T)M_2(r)r^2\le r,
\]

or a sharper inequality justified from the actual resolvent.

For `r = x^*-A-δ` or a geometry-aware rectangle/weighted norm, derive an explicit

\[
U_{NL}(δ)>0.
\]

Do not force a Euclidean/sup ball if a rectangle or weighted norm yields a materially stronger ecological certificate.

## C3. Robust safety across rival mechanisms

Preferred theorem semantics:

> every admissible mechanism in the declared fractional/latent rival family remains above the Allee safety margin under the certified input class.

Construct a hierarchy-uniform gain/remainder bound if feasible.

Possible routes:

- a common bound over the finite certified hierarchy;
- positivity/mass bounds for positive relaxation modes;
- T23-type response enclosures plus margin transfer;
- interval maximization over the declared finite parameter/model class.

If robust safety cannot be proved, explicitly classify the theorem as **one-sided/reference-model safety** and explain why.

## C4. Nonlinear discrimination discrepancy

For fractional trajectory `ξ_F` and latent trajectory `ξ_m`, derive a Volterra/fractional-Grönwall estimate of the form

\[
\|C(\xi_F-\xi_m)\|_\infty
\le A_{NL}(r,T)\,E_m^{G/K}\,\|u\|_\infty,
\]

or another explicit bound sufficient for the Gaussian testing step.

The amplification factor must be explicit and finite on the certified safe set.

## C5. Nonlinear Theorem D

Target final chain:

\[
\text{robust nonlinear safety}
\Rightarrow
\|u\|_\infty\le U_{NL}(δ)
\Rightarrow
\|\Delta\mu\|_\infty\le S_{NL}(m,δ)
\Rightarrow
P_e^*\ge\Phi\!\left(-\frac{\sqrt n}{2\sigma}S_{NL}(m,δ)\right).
\]

State exactly what is uniform over:

- inputs;
- sample schedules;
- model family;
- latent dimension/budget;
- safety margin.

### Deliverable

`THEOREM_D_NONLINEAR_LIFT.md`

Must end with one of:

- **GREEN — robust nonlinear theorem proved**;
- **YELLOW — one-sided nonlinear theorem proved**;
- **RED — nonlinear lift fails**, with exact failed inequality / missing hypothesis and the strongest surviving linearized theorem.

---

# 4. Task R2-D — endpoint-inclusive positive-SOE complexity theorem

Do not assume the rate before proving it.

Lemma B.1 allows normalization to `T=1` for the **relative** `L¹` best-approximation problem. Exploit this aggressively.

## D1. Preferred target

Try to prove an explicit positive exponential-sum construction with endpoint included and a rate of at least root-exponential type:

\[
\frac{\|K_\alpha-K_m\|_{L^1(0,T)}}{\|K_\alpha\|_{L^1(0,T)}}
\le A(\alpha)e^{-c(\alpha)\sqrt m},
\]

which implies

\[
m(\varepsilon)=O_\alpha(\log^2(1/\varepsilon)).
\]

This is a **target**, not a permitted assumption.

## D2. Suggested route

1. normalize `T=1` using Lemma B.1;
2. use the positive diffusive representation;
3. transform `λ=e^s`;
4. split the endpoint interval `(0,δ)` from `[δ,1]`;
5. use a published away-from-zero SOE/trapezoid estimate on `[δ,1]`;
6. bound both the exact kernel and the constructed positive approximant on `(0,δ)`;
7. choose `δ=δ(m)` by balancing endpoint and quadrature/truncation errors;
8. track positivity of all weights;
9. recover arbitrary `T` by scaling.

A direct corollary from a published SOE theorem is acceptable **only if every hypothesis matches** and the endpoint contribution is proved rather than hand-waved.

## D3. Stronger result allowed

If a genuine geometric `e^{-cm}` bound can be proved with the endpoint included, present it. But do not write such a rate merely because log-scale quadrature is exponentially convergent for fixed `t>0`; the singular endpoint changes the complexity balance.

## D4. Failure mode

If no rigorous rate closes, preserve only:

- Lemma B.1;
- constructive existence;
- finite-range C-1 numerical evidence;
- published away-from-zero rates.

### Deliverable

`THEOREM_B_ENDPOINT_COMPLEXITY_PROOF.md`

Include exact citations and a proof-dependency map.

---

# 5. Task R2-E — re-audit Theorem C′ at the correct operator level

After Task B, rewrite the testing theorem with the actual observed response discrepancy.

For two simple equal-covariance Gaussian hypotheses,

\[
P_e^*=\Phi(-d/2)
\]

is exact. For the **composite** alternative family, state carefully how the selected rival yields a minimax lower bound.

Required checks:

1. distinguish simple Bayes risk from composite minimax risk;
2. define priors when Bayes language is used;
3. define the observation norm and sampling map;
4. verify the `√n` bound for arbitrary sample locations;
5. carry the correct response-level `E_m^G` or proved resolvent constant;
6. do not call the Young/sampling chain “tight to first order” unless the slack from those inequalities is actually controlled.

### Deliverable

`THEOREM_C_PRIME_FINAL.md`

---

# 6. Task R2-F — authorized safe-amplitude benchmark, versioned

**AUTHORIZED. Do not overwrite frozen v3.**

Create a new directory/version, e.g. `benchmark_safe_v4/` or an equivalent immutable namespace.

## F1. Stage-A amplitudes

At minimum run:

- peak amplitude `0.050`;
- peak amplitude `0.063` (near the Round-01 linear certificate `0.0634`);
- peak amplitude `0.100` using the same pipeline as the frozen baseline for comparison.

If `U_NL(δ)` is established during the round, add a run at or below the nonlinear certified amplitude.

## F2. Controlled comparability

Keep fixed wherever possible:

- design families;
- horizon;
- sampling cadence;
- parameter grid;
- latent budgets;
- noise/SNR grid;
- random seeds;
- BIC fitting/scoring implementation.

The purpose is to isolate the effect of the safe amplitude constraint.

## F3. Required outputs

For each mechanism/design/amplitude:

- minimum `x-A`;
- safety crossing indicator/rate;
- macro accuracy + confusion matrix;
- pairwise fractional-vs-latent error;
- BIC gaps;
- realized `||u||∞`, `||u||2`;
- realized output separation;
- realized gain `||ξ||∞/||u||∞`;
- safety status under every rival model if robust-safety semantics are used.

Also compute uncertainty over Monte Carlo replicates.

## F4. No circular certification

Simulation may validate or falsify a theorem-derived certificate, but must not be used as the proof of that certificate.

### Deliverables

- `SAFE_BENCHMARK_V4_REPORT.md`
- code + raw results under the new benchmark namespace
- machine-readable summary JSON/CSV
- reproducibility command

---

# 7. Task R2-G — correct known manuscript-critical defects

Without doing a full prose rewrite, prepare exact replacement math/text for the known false or overstated claims:

1. Theorem 9.3: remove the false claim that the KL of the expected posterior supplies information; replace with the correct expected-information identity.
2. Remove “greedy one-step MI minimizes number of experiments.”
3. Remove “theoretically optimal designs validated” unless the actual optimization is executed.
4. Do not claim Bayesian OED was executed when the benchmark uses BIC.
5. Do not claim first OED for fractional systems.
6. Replace invalid `L²`-kernel pairing on `0<α≤1/2` with the valid operator/norm statement.
7. Fix all “our previous paper” provenance language where authorship does not match.

### Deliverable

`R2_MANDATORY_MANUSCRIPT_CORRECTIONS.md`

Give exact section/equation/theorem targets from the current manuscript.

---

# 8. Task R2-H — journal decision after mathematics closes

Do not select a journal by prestige first. Select it by the paper that exists at the end of the round.

### Outcome map

**Case H1 — nonlinear robust D + endpoint complexity theorem GREEN**  
Evaluate CNSNS and FCAA head-to-head; FCAA becomes a credible stretch option.

**Case H2 — nonlinear D GREEN, endpoint complexity only supporting**  
Primary recommendation: CNSNS.

**Case H3 — nonlinear lift fails, linearized theorem + certified numerics remain**  
Primary recommendation: CNSNS or another nonlinear/fractional dynamics journal; do not resubmit AIMS as the first choice.

**Case H4 — both key upgrades fail**  
Reframe toward mathematical biology / computational fractional dynamics, reduce theorem-first claims, and choose a narrower venue.

### Deliverable

`ROUND_02_JOURNAL_DECISION.md`

For the selected top 2 journals include:

- current official scope quote/paraphrase with source URL/date;
- manuscript fit;
- main desk-rejection risk;
- what must be emphasized/de-emphasized;
- current mandatory submission/template source;
- preliminary compliance gaps.

No submission formatting migration yet unless the Chief explicitly authorizes it after this decision.

---

# 9. Round-02 acceptance gates

## G2.1 — Claim-status repair

No finite-fit asymptotic claim survives without proof.

## G2.2 — Operator correctness

Kernel-level and response-level approximation errors are separated and connected rigorously or kept separate.

## G2.3 — Safety semantics

The theorem clearly distinguishes:

- linear vs nonlinear;
- sufficient certified input set vs all safe inputs;
- one-sided vs robust model-family safety.

## G2.4 — Nonlinear attempt

A serious Volterra/fractional-Grönwall lift is completed or fails with a documented mathematical obstruction.

## G2.5 — Complexity theorem

Endpoint-inclusive rate is either proved with explicit dependencies or explicitly left unresolved.

## G2.6 — Benchmark consistency

A versioned low-amplitude rerun exists and does not overwrite v3.

## G2.7 — Known false claims

Theorem 9.3 and OED/Bayesian overclaims have exact replacement instructions.

## G2.8 — Journal recommendation

Venue choice follows the actual end-of-round result profile.

---

# 10. Required Round-02 deliverables

1. `ROUND_01_STATUS_CORRECTIONS.md`
2. `R2_OPERATOR_BRIDGE.md`
3. `THEOREM_D_NONLINEAR_LIFT.md`
4. `THEOREM_B_ENDPOINT_COMPLEXITY_PROOF.md`
5. `THEOREM_C_PRIME_FINAL.md`
6. `SAFE_BENCHMARK_V4_REPORT.md`
7. benchmark-safe-v4 code/raw machine-readable outputs
8. `R2_MANDATORY_MANUSCRIPT_CORRECTIONS.md`
9. `ROUND_02_JOURNAL_DECISION.md`
10. updated `RESCUE_CLAIM_EVIDENCE_LEDGER.md`
11. `ROUND_02_DECISION.md`

---

# 11. Final instruction to Researcher

Be adversarial. The goal is not to preserve Theorem D or the rescue narrative. The goal is to determine the **strongest true statement** that survives:

- operator-level scrutiny;
- nonlinear dynamics;
- model uncertainty;
- statistical decision theory;
- and reproducible numerical verification.

A smaller theorem with clean hypotheses is preferable to a broader theorem whose ecological or safety interpretation is not actually proved.
