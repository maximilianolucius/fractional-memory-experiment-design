# CHIEF REVIEW — ROUND 03

**Branch:** `rescue/aims-desk-rejection`  
**Reviewed commit:** `b115f2b80b051363c89c77f93c4f07533a315967`  
**Chief verdict:** **MAJOR SCIENTIFIC ADVANCE — ACCEPTED, WITH THREE BLOCKING CORRECTIONS BEFORE SUBMISSION**

Round 03 changes the paper more fundamentally than Rounds 01–02. The adversarial search did exactly what it was supposed to do: it falsified our own negative narrative. That is a success, not a failure. The desk-rejected paper treated the six historical waveform families as if they exposed an intrinsic safety–informativeness frontier. They did not. A constrained search over previously untested piecewise-constant waveforms found safe designs that outperform every historical baseline at the same peak-amplitude budget.

The rescued paper must now be written around that falsification and the positive design result, while preserving the separate finite-horizon latent-complexity obstruction.

---

# 1. Decision on the blocking theorem-status item

## **DECISION: DEMOTE T9b / B.2.**

This is mandatory.

The positive exponential-sum construction, positivity of the weights, logarithmic quadrature idea, and root-exponential order are established prior art. McLean (2018), building on Beylkin–Monzón and related exponential-sum quadrature work, treats positive exponential approximations to `t^{-β}` on `[δ,T]`, `δ>0`, using essentially the same technique.

The manuscript may retain our useful endpoint-inclusive observation, but only as a **supporting lemma/tool**:

> For `0<α<1`, the best positive exponential approximation in `L¹(0,T)` obeys the exact scaling `E_m^+(α,T)=T^α E_m^+(α,1)`. Moreover, for every `c<π√(α(1−α))` there exists `A(α,c)<∞` such that `E_m^+(α,T)≤A(α,c)T^α e^{-c√m}`.

Permitted novelty statement:

> The paper uses the classical positive-SOE/log-quadrature construction and records an endpoint-inclusive `L¹(0,T)` estimate and exact horizon scaling adapted to the convolution norm required by the discrimination argument.

Not permitted:

- “new exponential-sum approximation method”;
- “new root-exponential law”;
- priority for positive weights;
- the boundary value `c=π√(α(1−α))` as proved;
- a standalone FCAA-paper claim based on this result.

### Consequences

1. Change the environment of current `thm:T9b` from headline theorem to **Lemma / supporting approximation result**.
2. Attribute the technique explicitly to **McLean (2018)** and cite Beylkin–Monzón, Jiang et al., and the quadrature source used in the proof.
3. Keep the finite-horizon “unbounded latent dimension destroys uniform separation in the closure” statement as a **corollary**, not as novelty of the SOE construction.
4. Remove T9b/B.2 from the headline contribution list.
5. **FCAA split is formally withdrawn.** CNSNS is the only active target.

This correction is non-negotiable. Submitting the current manuscript with T9b still framed as a contribution would recreate the same novelty-positioning failure that triggered the desk rejection.

---

# 2. The new scientific headline

Round 03 established a much better story:

> **The severe safety–informativeness frontier seen in the six classical waveform families is a parameterisation artifact. Under the same peak-amplitude budget and a hard Allee-margin constraint, searched piecewise-constant waveforms can be simultaneously safe and substantially more informative.**

At the frozen Round-03 protocol:

- best found safe design: macro BIC `0.8030`, zero observed crossings;
- only historical design safe under all four candidate mechanisms: `0.5141`;
- best historical design of any kind: `0.7628`, but unsafe;
- Stage 1 evaluated `163,840` candidates, `87,601` satisfying the hard safety constraint;
- Stage 2 used the actual four-class BIC pipeline on `672` cells × `100` replicates with zero divergences.

This is the main result of the rescued paper.

## But scope it correctly

Do **not** say:

- “waveform design governs safety” as a universal system law;
- “amplitude never controls safety”;
- “safety imposes no information cost”;
- “latent complexity, not safety, is the only binding limitation.”

Round 03 itself shows a remaining Pareto cost: the best unsafe Stage-1 candidate has much larger separation than the best safe candidate. What was falsified is the **severe frontier inferred from the six classical families**, not the existence of any safety–information frontier.

Preferred conclusion:

> **Optimising waveform shape recovers most of the discrimination lost by the classical safe designs; increasing latent-model complexity remains a separate finite-horizon obstruction that waveform search does not remove.**

---

# 3. Working title — change again

The current title

> *Waveform Design, Not Amplitude, Governs Safe Memory Discrimination in a Strong-Allee Predator–Prey Model*

is stronger than the evidence because “governs” reads as a general causal statement.

**Chief-selected working title:**

> **Safe discrimination of fractional, delayed, and latent memory beyond classical waveforms in a strong-Allee predator–prey model**

This title states what was actually demonstrated and keeps the mechanism classes visible to a CNSNS editor.

---

# 4. Safety wording is reopened: R3-D is not yet a rigorous certificate

Round 03 substantially improves the safety evidence, but `R3_VALIDATED_SAFETY_REPORT.md` explicitly states that:

- `ε_solver` is a mesh-refinement **estimate**, not a rigorous bound;
- the tube bound `F` is evaluated on a fine grid, not by interval enclosure.

Therefore the manuscript may currently say:

> “a posteriori trajectory verification with a rigorous inter-node modulus and refinement-based solver-error control”

but it may **not yet** say without qualification:

> “validated integration certifies these trajectories”

or call the `+0.092` margin fully certified.

The numerical slack is very large, so this is likely easy to close for the headline designs. Round 04 must do one of two things:

### Preferred
Obtain a genuinely rigorous enclosure for the headline trajectories — at minimum the found `pwc6` and the historical `multiscale` baseline under all four candidate mechanisms (8 trajectories). Use validated Volterra/Caputo integration and interval/Taylor-model bounds, or another method that produces an actual enclosure of solver error and the vector-field tube bound.

### Fallback
If a true enclosure cannot be produced, globally downgrade “certified/validated” to “a posteriori verified” and state the solver-error caveat next to the headline result.

No ambiguous middle status is allowed.

---

# 5. Theorem C / response-level obstruction survives, but the manuscript theory section is stale

The Round-03 audits correctly separate:

- bare kernel error;
- response/impulse-response error;
- fixed-input discrepancy;
- induced input→output gain.

The large-`m` response computation to `m=128` is useful and materially stronger than the rejected version. However `paper/sections/sec3.tex` still contains the old `L²`-budget / unspecified `Ψ` / Pinsker theorem and still presents T9b as a theorem contribution.

Round 04 must replace the theory section with the final semantics:

1. structural separation — supporting foundation, not priority claim;
2. McLean-attributed endpoint-inclusive SOE lemma — supporting tool;
3. exact equal-covariance Gaussian two-point bound at the **response-operator** level;
4. certified/high-accuracy finite-state prey-response approximations, with the status of each numeric enclosure stated exactly;
5. the finite-horizon latent-complexity corollary.

Do not use a kernel-level error as though it were a response-level design objective.

---

# 6. Abstract and provenance

The current abstract is too long for CNSNS and contains two unacceptable phrases:

- “inherited from a previously submitted companion paper”; and
- “validated integration certifies these trajectories” (until §4 is closed).

CNSNS currently requires an abstract of **no more than 250 words**, 1–7 keywords, and mandatory 3–5 highlights of at most 85 characters each. The live Guide for Authors, not the repository’s historical assumptions, is the source of truth.

The abstract must:

1. be ≤250 words;
2. lead with the falsification / positive safe-design result;
3. describe latent complexity as a separate obstruction, not the sole limitation;
4. use one concise neutral provenance sentence at most, or leave provenance to the Introduction;
5. contain no “our previous paper” / “previously submitted” language;
6. use only 3–5 headline numbers.

In the Introduction, delete the companion-comparison table. One neutral paragraph is enough:

> “The ecological backbone follows the companion certification study [P01]; the equations, locked parameters, coexistence equilibrium and Jacobian are restated here for self-containment and are not claimed as contributions of the present work.”

---

# 7. Journal decision

**CNSNS remains the sole active target.**

The current live CNSNS Guide for Authors is consistent with this paper’s content: it explicitly includes fractional dynamics, analytical methods, computational methods, and nonlinear modelling/simulation. It also makes clear that the editor performs an initial suitability screen, so novelty must be visible immediately.

Important compliance correction: **do not invent requirements.** The current guide requires editable `.tex` sources but does not make “use `elsarticle`” a standalone scientific acceptance criterion, and it does not impose a strict bibliography style at initial submission beyond consistency and numbered square-bracket citations. Use the then-current official Elsevier template if available/appropriate, but the compliance matrix must distinguish **mandatory**, **recommended**, and **our own house preference**.

Final policy remains:

- **100% of mandatory requirements PASS**;
- **≥99% of the complete applicable checklist PASS**;
- live instructions/template rechecked within 24 hours before submission.

---

# 8. Chief status of Round-03 claims

| Item | Chief status |
|---|---|
| Safe PWC design existence and BIC improvement | **GREEN — EMPIRICAL/REPRODUCED** |
| Claim that six-family frontier is intrinsic | **RETRACTED / FALSIFIED** |
| “waveform parameterisation artifact” within tested protocol | **GREEN, scoped** |
| Universal “waveform governs safety” | **NOT PROVED** |
| McLean-style SOE construction/root-exponential order | **PRIOR ART — SUPPORTING LEMMA** |
| Endpoint-inclusive `L¹(0,T)` safe-form bound | **PROVED, supporting** |
| Boundary constant attainment / optimality | **OPEN** |
| FCAA split | **WITHDRAWN** |
| Large-`m` prey-response indistinguishability | **GREEN at declared response-level computation/certificate status; do not route through bare kernel error** |
| R3-D “fully certified trajectory safety” | **YELLOW until solver/tube enclosures are rigorous** |
| CNSNS target | **GREEN provisional → now active** |

---

# 9. Round 04 purpose

Round 04 is the **submission-closure round**. It is not another open-ended research round.

Its job is to:

1. execute the McLean demotion/citation;
2. close or honestly downgrade the rigorous-safety wording;
3. rewrite the theory section consistently;
4. redraw the main safety/information figure around the new PWC result;
5. rewrite title/abstract/contributions/provenance;
6. rebuild the manuscript under current CNSNS instructions;
7. run mock-editor and mock-referee gates;
8. produce the final submission package only if all scientific and compliance gates are GREEN.
