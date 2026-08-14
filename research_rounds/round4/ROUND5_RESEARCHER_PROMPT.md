# Round 5 Researcher Prompt — Hard Gate + Safe Memory-Discrimination Atlas

## Governance

Do **not** start by plotting an atlas.

Round 5 has a mathematical Phase 0 gate.  Only if the gate closes may you generate and integrate the Safe Memory-Discrimination Atlas.

Do not rerun the large factorial benchmark.  Use lightweight theorem-directed calculations / validation only.

Read first:

- `CHIEF_ROUND4_AUDIT.md`
- `THEOREM_LEDGER_after_R4_CHIEF.md`
- `NOVELTY_LEDGER_after_R4_CHIEF.md`
- `chief_round4/Ebar_interval_bounds.json`

The chief has already repaired T20/T21 and replaced the false QUADPACK certificates by interval enclosures.  Do not undo those edits.

---

# Phase 0A — Close the hierarchy-uniform Strong-Allee interface

The current A~0.32 crossover is only a diagnostic over the five locked benchmark rivals.  It is **not** a supremum over K_m.

For a declared transient protocol class (start with pulse; multiscale second), do one of the following rigorously:

### Preferred route

Define the actual ecological realization for every `k in K_m` and obtain a theorem-valid bound on

`d_rob(K_m,u0) = sup_{k in K_m} max_t[-H_{x,k}u0(t)]_+ / ||u0||_2`.

Then

`B_Allee(A,m) = rho_eta / d_rob(K_m,u0)`

is a necessary outer bound for the common-safe ray.

You may use an analytic upper bound, validated optimization, or interval enclosure.  If the bound is conservative, report that honestly.

### Acceptable negative route

If no finite/non-vacuous hierarchy-uniform bound follows from the current mass/rate constraints, prove that and **narrow the rival/experiment class explicitly** before proceeding.  Do not silently substitute the benchmark five-model maximum.

### Gate A

We need a theorem-valid quantity depending on A and m that can enter T20 for the same adversarial class, OR a rigorous negative result showing why that cannot be done under the frozen hierarchy.

---

# Phase 0B — Attempt the ecological-state lift of T20

The current T20 controls the kernel convolution experiment `S(k*u)`.  The paper's ecological object is the linearized predator-prey Volterra system.

Write the zero-initial-deviation systems explicitly, e.g.

`xi_alpha = k_alpha * (J xi_alpha + B u)`

and the corresponding finite-memory realization with `k_m`.

Try to prove a finite-horizon continuous-dependence inequality of the form

`||C(xi_alpha-xi_m)||_Y <= C_dyn(A,alpha,T,M_T) ||k_alpha-k_m||_1 ||u||_X`.

Do **not** use the small-gain denominator `1-||J||||k||_1` unless it is actually <1 in the parameter region.  Prefer a Volterra resolvent / fractional-Gronwall argument valid on the full finite horizon.

### Gate B

- If a non-vacuous C_dyn is proved: derive the ecological-state version of T20.
- If the resulting constant is mathematically valid but numerically useless: keep it as a scope theorem and do not use it for the headline atlas.
- If the lift cannot be closed: state that cleanly; the atlas must then be labeled kernel-level theoretical + full-state empirical, not a single certified ecological theorem.

---

# Phase 0C — Freeze the asymptotic hierarchy correctly

The finite m<=32 running windows do not prove E_m->0.

If the final paper wants an asymptotic hierarchy claim, define an explicit expanding nested window sequence containing a T9b approximation subsequence and prove

`K_m subset K_{m+1}` and `E_m -> 0`.

Otherwise remove the asymptotic hierarchy claim entirely and keep only finite-budget statements.

---

# Phase 1 — Atlas construction (only after the Phase 0 verdict)

Construct the strongest defensible atlas from theorem-valid quantities.

Preferred coordinates:

1. `(A, alpha)` panels at fixed m and sigma;
2. `(alpha, m)` panels at fixed A / safety margin;
3. one frontier panel showing where the active outer budget changes from actuator-limited to Allee-limited **only if Phase 0A made this hierarchy-uniform**.

Classification should be theorem-based, for example:

- `provably hard at target error p0` if the T20 lower bound >= p0;
- `bound inconclusive` otherwise;
- optionally `unsafe / no common-safe ray` if certified by Phase 0A.

Do not label the complement `provably discriminable`; a lower-bound failure is not an achievability theorem.

Use interval-enclosed `Ehat_m^IA` or a stronger validated replacement, never the old QUADPACK values as certificates.

---

# Phase 2 — Adversarial checks

Stress the atlas and theorem at:

- alpha -> 1;
- increasing m;
- A approaching the coexistence/stability edge;
- sigma low/high;
- actuator cap changes;
- protocol sign reversal where relevant.

Check all monotonicities that are actually implied by the definitions.  Do not infer monotonicity from a nonmonotone list of tuned candidate mixtures; use the nested running upper envelope.

---

# Phase 3 — Manuscript / visual integration

Only after the atlas gate:

- add 1 headline atlas figure (2–4 panels maximum);
- optionally one supporting frontier figure;
- revise Abstract / Introduction / Discussion to the strongest theorem that truly survived;
- keep the existing 16 Q1 figures otherwise frozen;
- move detailed atlas tables to supplement.

The final visual should make the interaction

`memory complexity x observation noise x ecological safety`

visible without overstating achievability.

---

# Required outputs

- `ROUND5_PHASE0_GATE.md`
- `ROUND5_RESULTS.md`
- `THEOREM_LEDGER_after_R5.md`
- `NOVELTY_LEDGER_after_R5.md`
- `MANUSCRIPT_IMPACT_after_R5.md`
- lightweight proof/check scripts
- atlas data JSON/CSV
- atlas figure(s) only if the gate passes
- updated manuscript only if the gate passes
