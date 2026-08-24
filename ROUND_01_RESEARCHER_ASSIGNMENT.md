# Round 01 — Researcher assignment

**Branch:** `rescue/aims-desk-rejection`  
**Priority:** CRITICAL  
**Goal:** establish whether the desk-rejected manuscript can be upgraded to a theorem-first paper with general mathematical significance.

## Non-negotiable principle

Do **not** start by polishing prose, adding figures, or migrating LaTeX. This round is about proving or falsifying the strongest mathematical claims that could materially change editorial perception.

The submission target will ultimately require **100% of mandatory requirements and >=99% of the current applicable journal checklist**, but template work is downstream of the mathematical rescue.

---

## Task 1 — Freeze and inventory the rejected baseline

Identify the exact rejected manuscript source and record:

- title;
- author list;
- page count;
- theorem/lemma/proposition count;
- figure count;
- table count;
- supplement structure;
- bibliography style;
- all places where the companion paper is referenced;
- all places where novelty is explicitly disclaimed (`inherited`, `not new`, `previous paper`, etc.).

Create:

`REJECTED_BASELINE_AUDIT.md`

Do not alter the baseline files during this step.

---

## Task 2 — Build an adversarial novelty matrix

Create:

`NOVELTY_MATRIX.md`

Search the closest literature, not generic background. Cover at least:

- fractional system identification;
- fractional-vs-delay discrimination;
- diffusive representation / exponential sums;
- rational approximation of fractional kernels or transfer functions;
- finite-horizon identifiability;
- minimax testing for dynamical systems;
- active model discrimination;
- safe experiment design;
- safety-constrained identification;
- fractional/delayed predator–prey systems.

For each closest work, state exactly what theorem/result it contains and exactly what this paper would add.

### Required adversarial question

Could a specialist reasonably say:

> “The four analytical results are standard consequences of known approximation and testing tools, with the only novelty being the ecological case study”?

Answer this explicitly with evidence. If the answer is partly yes, say so and identify what theorem would be needed to escape that critique.

---

## Task 3 — Audit Theorem A: structural non-equivalence

Reconstruct the current theorem from source and supplementary proofs.

Then attempt a stronger general theorem for hereditary input/output systems.

Must explicitly analyze:

- `CB != 0` vs `CB = 0`;
- input/output channel placement;
- exact transfer-function equality;
- cancellations;
- partial observation;
- proper/improper rational models;
- one vs multiple delays;
- branch-cut and analytic-domain assumptions;
- whether the claimed high-frequency distinction is sufficient for the exact model classes actually used.

Create:

`THEOREM_A_AUDIT.md`

Include:

1. current statement;
2. strongest correct generalized statement found;
3. full proof or proof skeleton;
4. counterexamples to stronger false variants;
5. recommendation: headline theorem / supporting theorem / remove.

---

## Task 4 — Audit Theorem B: quantitative finite-horizon approximation

Current qualitative idea: approximate the Caputo kernel on `[0,T]` by a positive finite exponential sum / finite latent-memory realization.

The rescue priority is to obtain a **complexity law**.

Try to establish an explicit relation of the form

\[
\|k_\alpha-k_m\|_{L^1(0,T)} \le \varepsilon(m,T,\alpha)
\]

or the inverse

\[
m \ge m(\varepsilon,T,\alpha) \implies
\|k_\alpha-k_m\|_{L^1(0,T)}\le\varepsilon.
\]

Investigate constructive quadrature/diffusive-representation approaches and known best approximation rates. Distinguish clearly between:

- positive exponential sums;
- arbitrary rational approximants;
- approximating the kernel vs transfer function;
- approximation away from `t=0` vs in `L1(0,T)` including the singular endpoint.

Create:

`THEOREM_B_COMPLEXITY_LAW.md`

If an explicit rate cannot be proved, identify the exact obstruction and the strongest rigorous weaker bound.

---

## Task 5 — Audit Theorem C: finite-experiment testing obstruction

Derive from first principles the statistical lower bound for the actual observation model.

Do not inherit constants blindly.

Audit:

- continuous vs sampled observation;
- number and placement of samples;
- Gaussian covariance structure;
- equal/unequal priors;
- deterministic model mismatch vector;
- KL divergence;
- total variation;
- Pinsker or sharper Gaussian testing formula;
- input norm/budget;
- convolution inequality;
- observation operator norm;
- uniformity over all admissible inputs.

Target a theorem where a latent complexity sequence satisfying `E_m -> 0` forces minimax or Bayes discrimination error toward `1/2` on finite horizons under bounded excitation.

Create:

`THEOREM_C_TESTING_OBSTRUCTION.md`

Required output:

1. exact observation model;
2. exact lower bound;
3. dependence on `m,T,U,sigma,n,C_obs`;
4. whether the result is uniform;
5. tightness discussion;
6. any stronger direct Gaussian bound that improves on generic Pinsker.

---

## Task 6 — Highest-value task: attempt Theorem D

Attempt a genuinely new **safety-constrained information ceiling**.

Starting point:

- strong-Allee safety condition such as `x(t) >= A + delta`;
- safe inputs are a strict subset of all bounded inputs;
- discriminating information requires excitation;
- richer latent approximants reduce observable discrepancy.

Try to prove a chain:

\[
\text{safety margin}
\Rightarrow
\text{admissible input bound}
\Rightarrow
\text{observable separation ceiling}
\Rightarrow
\text{testing-error floor}.
\]

The theorem may first be proved for a local linearization / generic state-space system, then specialized to the strong-Allee model.

Create:

`THEOREM_D_SAFETY_INFORMATION.md`

This file must contain one of only two conclusions:

### GREEN
A mathematically correct, nontrivial theorem with assumptions, proof, limitations and specialization.

### RED
No defensible theorem at the desired level. Give the minimal extra assumptions needed, counterexamples to overstrong versions, and recommend treating the result as certified numerical evidence only.

Do not return an ambiguous YELLOW conclusion.

---

## Task 7 — Self-containment and provenance audit

Create:

`OVERLAP_PROVENANCE_AUDIT.md`

Explicitly resolve the wording problem where the manuscript uses “our previously submitted companion paper” while the current manuscript author list and the bibliographic author list of `P01` are not identical.

Inventory:

- reused equations;
- reused parameters;
- equilibrium/Jacobian;
- reused text;
- reused figures;
- dependencies on unpublished results;
- what must be reproduced in this paper to make it self-contained.

Recommend exact neutral provenance wording.

---

## Task 8 — Claim/evidence ledger

Create:

`RESCUE_CLAIM_EVIDENCE_LEDGER.md`

For every major prospective claim:

| Claim | Type | Proof/evidence | General or model-specific? | Prior-work comparator | Status |
|---|---|---|---|---|---|

Status must be one of:

- `PROVED`
- `CERTIFIED_NUMERICALLY`
- `EMPIRICAL`
- `CONJECTURAL`
- `REMOVE`

No claim may remain unlabeled.

---

## Task 9 — Round decision memo

Create:

`ROUND_01_DECISION.md`

Answer directly:

1. Is there a credible theorem-first rescue?
2. Which of A–D should be headline results?
3. What is actually new after the literature audit?
4. What must be dropped or softened?
5. Is AIMS Mathematics still a rational target after the mathematical audit?
6. If not, what journal *type* better matches the resulting paper?
7. What exact work should Round 02 perform?

### Mandatory journal-compliance note

Record that final submission work must use the **then-current official journal instructions and official TeX template**, with **100% mandatory compliance and >=99% total applicable checklist compliance**. Do not treat the repository's current `aims_math_style.sty` as source of truth.

---

## Deliverable quality bar

This is a research round, not a prose-polish round. The response is insufficient if it merely restates the manuscript or produces generic recommendations.

You are expected to:

- derive mathematics;
- search for counterexamples;
- compare closest literature;
- tighten constants;
- separate general theorems from model-specific facts;
- explicitly falsify claims that do not survive audit;
- leave the repository in a state from which the Chief can decide whether the rescue is mathematically viable.
