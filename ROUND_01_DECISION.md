# ROUND_01_DECISION — Researcher memo to Chief

**Branch:** `rescue/aims-desk-rejection` · **Round:** 01 · **Scope:** mathematics and novelty, no prose polish.

---

## 1. Is there a credible theorem-first rescue?

**Yes — but a modest one, and it is not the rescue the plan hoped for.**

What closed this round:
- **Theorem D (safety-constrained information ceiling): GREEN.** The chain
  `safety margin δ → admissible excitation U(δ)=ρ(δ)/Γ_T → separation ceiling E_m·U(δ) → testing-error
  floor Φ(−(√n/2σ)E_mU(δ))` is proved, uniform over safe inputs, monotone in `δ`, and **numerically
  instantiated with certified constants**: `Γ_T=5.7815` (`α=0.85,T=12`), `U(0.05)=0.0634`, error floor
  **0.452** at `m=32, σ=0.02` rising to **0.471** at `δ=0.20`. It also *predicts* a phenomenon already
  measured in the frozen v3 benchmark (§3 of that file).
- **Theorem A′: PROVED and strictly stronger** than the shipped `thm:T4` — via a rationality criterion
  (Lemma A.0, iff) and a two-line branch-point argument that additionally covers **neutral** delays,
  improper rationals, feedthrough and any finite number of delays. A **counterexample** was found and
  verified (`2.2e-16`) showing the claim fails without `CB≠0`, at `α=1/2` and `A=2/7` — the model's own
  stability boundary.
- **Theorem C′: PROVED with explicit constants**, derived from scratch; and the **exact Gaussian bound
  strictly dominates Pinsker** (which the manuscript currently uses and which is *vacuous* for `d≥2√2`).

What did **not** close:
- **Theorem B is not a contribution.** The complexity law is **already published** (Jiang–Zhang 2017:
  `O(log(1/ε)·log(T/Δt))`; Chaudhary–Diethelm et al. 2025). Worse: the manuscript's own constructive
  bound is **algebraic and numerically vacuous** — `1.14·m^{−0.112}`, i.e. 73 % relative error still at
  `m=48`, **749× worse** than achievable. The measured achievable law is exponential
  (`5.58e-2·exp(−0.0865m)`, `R²=0.995`) but is **measured, not proved**.

**Honest summary:** the paper can be made theorem-first and correct. It cannot honestly be made
*deep*. Theorem D is a composition of four elementary steps whose value is the composition plus
certified constants — not a new technique.

**Update after computation C-1 completed (285 cells).** Two changes to the above:
- **Added a proved result:** *Lemma B.1* — the relative `L¹` approximation error is **independent of
  the horizon `T`** (verified to `6e-17`, proof by scaling). Small, but it is a theorem, and it
  distinguishes the paper's norm from the published `[δ,T]` uniform-error rates.
- **Retracted a claim of mine:** an earlier local fit suggested the law was exponential in `m`
  (`R²=0.995`). With the full sweep to `m=128` the **exponent is not resolved** (all
  stretched-exponential forms fit with `R²∈[0.95,0.999]`). What the data support is only:
  sub-exponential, strictly faster than algebraic, `m(ε)=O(log^κ(1/ε))` with `κ∈[1,2]`, root-exponential
  being the safest conjecture. The manuscript must not state a specific rate.
- **Strengthened Theorem D:** feeding the measured `E_m` into the chain gives safe-excitation error
  floors `0.328 (m=32)`, `0.474 (m=64)`, **`0.4997 (m=128)`** — i.e. at 128 latent modes, safe
  discrimination is impossible to four decimals.

## 2. Which of A–D should be headline?

| | Result | Role |
|---|---|---|
| **Headline 1** | **D** — safety-constrained information ceiling | the only claim that is both general-in-form and not already in the literature for this class |
| **Headline 2** | **C′** — uniform testing obstruction with explicit constants | supplies step (iv) of D; makes the obstruction falsifiable |
| Supporting | **A′** — structural separation via branch structure + Lemma A.0 + the `CB=0` counterexample | clean foundation; explicitly *not* claimed as novel |
| Supporting | **T23** — certified interval enclosures `Ê_4=0.5335 → Ê_32=0.0070` | the numbers that make D non-vacuous |
| **Cite, do not claim** | **B** | published law; keep the paper's variant as labelled numerical evidence |

## 3. What is actually new after the literature audit?

Narrowly, four things:
1. The **composite** safety⇒information ceiling for *hereditary* mechanism discrimination with an
   explicit latent-complexity budget `m`, measured as a **testing-error floor** — `SAFE26A`
   (Saligrama 2026) has the analogous statement in **constrained-LQ/regret**, not here.
2. **Lemma A.0**, the iff rationality criterion `G_α=R(s^α)` rational ⟺ `αe∈ℤ` for all present
   exponents — not located in this form in the literature.
3. The **`CB=0` counterexample** at `α=1/2`, `tr J=0` (exactly `A=2/7`), which shows the standard
   hypothesis is load-bearing.
4. The `L¹(0,T)`-with-endpoint variant of the complexity law (measured; provable per §6 of that file).

Nothing else survives as novel. In particular: safe experiment design (`SAFE26A/B`), exponential-sum
approximation (Jiang–Zhang), fractional OED (FOED01–04) and the structural separation argument are all
prior art.

## 4. What must be dropped or softened?

Six items, from `RESCUE_CLAIM_EVIDENCE_LEDGER.md` (`REMOVE`):
- **`thm:T9b` as a contribution** → cite Jiang–Zhang instead.
- **Theorem 9.3 as printed** → *false* (KL of the expected posterior ≡ 0 by the tower property);
  replace with the expected-KL identity. **Most urgent single correction in the manuscript.**
- **"Greedy one-step MI minimizes the number of experiments"** → unproved.
- **"Theoretically optimal designs validated"** → the benchmark compares heuristic waveform families;
  no principal eigenvector or maximin LP was computed (audit P0.8).
- **"Bayesian OED implemented"** → the decision rule is BIC (audit P0.3).
- **"First OED for fractional systems" / novelty of safe design per se** → precluded.

Also soften: `thm:T20`'s `‖u‖₂≤B` pairing is invalid on the asserted range `0<α<1`, because
`k_α∉L²(0,T)` for `α≤1/2` — switch to the `L¹`×`L^∞` route (which is also the safety-relevant budget).

## 5. Is AIMS Mathematics still a rational target?

**Conditionally yes, but it is no longer my recommendation.** Two reasons:
1. The paper's honest profile after this audit is *applied/computational mathematics with one modest,
   linearized, single-channel theorem plus certified numerics*. That fits AIMS Mathematics' scope, but
   it does not obviously clear a **novelty/significance** screen that already rejected the previous
   version — and the mathematical core, while now correct, is not dramatically deeper.
2. Resubmitting to the journal that desk-rejected it requires the editor to perceive a *materially
   different* paper. Theorem D + the corrections do change the paper's character; whether that is
   enough is a judgement call the Chief/operator should make, not the Researcher.

## 6. If not, what journal *type*?

Ranked by fit to the paper that actually exists:
1. **Nonlinear/fractional dynamics** — e.g. *Communications in Nonlinear Science and Numerical
   Simulation*, *Fractional Calculus and Applied Analysis*, *Chaos, Solitons & Fractals*. Best match:
   fractional operators + certified numerics + an identifiability limit.
2. **System identification / control** — e.g. *Automatica* / *IEEE TAC* (high bar; Theorem D would
   have to be strengthened to full-state and compared head-on with `SAFE26A`), or *International
   Journal of Robust and Nonlinear Control*.
3. **Mathematical biology** — if the ecological reading is made central (*Journal of Mathematical
   Biology*, *Bulletin of Mathematical Biology*); then the safety–informativeness trade-off is the
   selling point rather than the theorem.

## 7. Exact work for Round 02

**Mathematics (highest value first)**
1. **Prove the endpoint step** of the complexity law (§6 of `THEOREM_B_COMPLEXITY_LAW.md`): log-scale
   quadrature + trapezoid error theory + `∫_0^δ` control with `δ ~ e^{−cm}`. Converts measured → proved.
2. **Replace** the `source_pack/07` uniform-`λ` construction throughout by the log-scale one (the
   current bound is vacuous at the reported `m`).
3. **Correct Theorem 9.3** and everything downstream of it (Eq. 67, discussion, conclusion).
4. **Attempt the nonlinear (full-state) version of Theorem D** via a Volterra/Grönwall continuation
   estimate; if it does not close, declare it open (do not weaken D's statement to hide it).
5. **Refine `Γ_T` to be design-dependent** (replace the worst-case `L¹` gain by the realized gain of
   the specific waveform). This removes D's conservatism for transient inputs and would make the
   ceiling *predictive per design* rather than worst-case.

**Manuscript**
6. Rebuild the theory section around D and C′; move the headline proofs into the main text.
7. Rewrite title/abstract/first 1.5 pages (sentence case; ≤4 numbers; no companion narrative).
8. Delete the Introduction's companion-comparison table; insert the neutral provenance paragraph from
   `OVERLAP_PROVENANCE_AUDIT.md` §4 and fix the 15 first-person references (author mismatch:
   manuscript = Alraddadi, `P01` = Lucius).
9. Restate the inherited backbone (≈1 page) for self-containment.

**Computation (must be requested, not run by the manuscript agent)**
10. **Re-run the nonlinear benchmark at a genuinely safe amplitude** `‖u‖_∞ ≤ U(δ)`. The frozen v3 used
    `0.10`, which is **58 % above `U(0.05)`** and 167 % above `U(0.20)` — i.e. the current benchmark is
    *outside* the certified-safe regime that Theorem D describes. Until this is redone, theory and
    experiment are describing different regimes, and a referee will notice.
11. Finish/collect the full `(α,T,m)` table of computation **C-1** to confirm the exponent's stability
    across `α∈{0.30,…,0.95}` and `T∈{1,10,100}` (launched; partial results in hand).

## 8. Mandatory journal-compliance note

Final submission work must use the **then-current official journal instructions and official TeX
template** of the selected journal, with **100 % of mandatory requirements PASS** and **≥99 % of the
complete applicable checklist PASS**, and with instructions and template **re-downloaded and re-checked
within 24 hours before submission**. The repository's `paper/aims_math_style.sty` and
`AIMS_MATHEMATICS_TEMPLATE_NOTES.md` are **not** the source of truth. Baseline compliance defects
already inventoried in `REJECTED_BASELINE_AUDIT.md` §7 (Title Case, no `lineno`,
`\bibliographystyle{plain}`, missing telephone/postal address, wrong Generative-AI heading, missing
acknowledgments/funding/data-availability, 49 unused bibliography entries).

---

## Round 01 deliverables produced

`REJECTED_BASELINE_AUDIT.md` · `NOVELTY_MATRIX.md` · `THEOREM_A_AUDIT.md` ·
`THEOREM_B_COMPLEXITY_LAW.md` · `THEOREM_C_TESTING_OBSTRUCTION.md` ·
`THEOREM_D_SAFETY_INFORMATION.md` · `OVERLAP_PROVENANCE_AUDIT.md` ·
`RESCUE_CLAIM_EVIDENCE_LEDGER.md` (unified, canonical) · `ROUND_01_DECISION.md`

**Chief decision required on:** (a) journal target (§5–6), (b) whether Round 02 attempts the nonlinear
extension of D or ships the linearized version with the limitation declared, (c) authorization of
computation item 10 (safe-amplitude benchmark re-run).
