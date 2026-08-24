# ROUND_02_DECISION — Researcher memo to Chief

**Branch:** `rescue/aims-desk-rejection` · **Round:** 02 · Adversarial, per the final instruction:
the goal was the strongest *true* statement, not the preservation of Theorem D.

---

## 1. The three hard targets — outcome

| Hard target | Outcome |
|---|---|
| **kernel error ⟶ actual response error** | **PROVED — and it works against us.** Proposition B.1 gives `E_m^G ≤ C_res E_m^K U` via fractional Grönwall (the naive Neumann route fails: `‖J‖‖K_α‖₁=4.95>1`). But `C_res = E_α(‖J‖T^α)(‖J‖Γ_T+‖B‖) ≈ 2352` at `α=0.85,T=12`, so kernel proximity is a **weak proxy** for response indistinguishability. The Round-01 ecological floors at `m=64,128` (`0.474`, `0.4997`) are **retracted**; after bridging they are `0.0000`, `0.0482`. |
| **linear safety ⟶ nonlinear robust safety** | **YELLOW, and the benchmark refutes the linear certificate.** Theorem D-NL is proved but operationally vacuous: `U_NL(0.05)=1.6·10^{-3}` = **2.5 %** of `U_lin`, capped by `Γ_R M₂≈30` at radius `0.035` against an ecological margin of `0.367`. Two stronger routes **fail structurally**: no inward-pointing rectangle exists around the coexistence equilibrium (predator faces are uncontrolled and `e a x/(1+hx)−m` vanishes exactly at `x*`), and weighted norms do not help (best `w=0.30`, still 2.5 %). Robust hierarchy-uniform safety: **not proved**. |
| **finite numerical fit ⟶ proved endpoint complexity law** | **GREEN.** Theorem B.2: `ε_rel ≤ A(α)e^{−c(α)√m}` with **`c(α)=π√(α(1−α))`**, endpoint included, weights positive, uniform in `T` (Lemma B.1). Verified: at `α=1/2`, predicted `π/2=1.5708` vs measured `1.5653` — **0.35 %**, `R²=0.9995`. `m(ε)=O(log²(1/ε))` is now a corollary of a proof, not of a fit. |

**Two of three closed in the direction the rescue needed; the middle one closed against it.**

## 2. The result that changes the paper

The v4 benchmark (Task R2-F, 2 of 3 amplitudes complete, 1512 cells) produced the finding that should
drive the manuscript:

- At `amp = 0.063`, which **is** the linearized safe amplitude `U(0.05)`, `sinusoid` and `prbs` cross
  the Allee threshold in **93 %** of cells, with realized gains up to **22.6** against the linear
  worst case `Γ_T = 5.78`. **The linear certificate is not a nonlinear safety guarantee** — measured,
  not argued. (This independently confirms `U_NL ≪ U_lin`.)
- Restricted to designs that **never** cross: the best accuracy is **0.259** at `amp=0.063`
  (`pulse`), against a chance level of **0.25**.

> **Within genuinely non-crossing excitation, discrimination of the memory mechanism is essentially at
> chance.** v3's headline `0.537` was obtained 58 % above the linear certificate — outside any safe
> regime.

**Consequence.** The paper's story is no longer "safe designs discriminate less well". It is
**"no safe excitation discriminates at all, in this system, under this budget, with this decision
rule"** — a genuine practical-impossibility result, partially explained by the ceiling theorem and fed
by the complexity law. That is a *stronger and more honest* contribution than the original claim, but
it is a **different paper** from the one that was rejected, and the abstract must say so.

## 3. Acceptance gates

| Gate | Status | Evidence |
|---|---|---|
| **G2.1** claim-status repair | **PASS** | `ROUND_01_STATUS_CORRECTIONS.md`: 10-row before/after table; every finite-fit asymptotic inference deleted; the asymptotic statement now rests on Theorem B.2; Lemma B.1 preserved as PROVED |
| **G2.2** operator correctness | **PASS** | `R2_OPERATOR_BRIDGE.md`: `E_m^K` and `E_m^G` defined separately, connected by Proposition B.1 with an explicit constant, and the manuscript is instructed to use `E_m^G` only in ecological theorems |
| **G2.3** safety semantics | **PASS** | `THEOREM_D_NONLINEAR_LIFT.md` §C5: linear vs nonlinear separated; `U_NL` presented as a *sufficient certified* input set (not all safe inputs); classified explicitly **one-sided / reference-model**, with robustness declared unproved |
| **G2.4** nonlinear attempt | **PASS** (fails with documented obstruction) | Volterra/mild-solution + fractional-Grönwall lift completed; obstruction quantified (`Γ_R M₂≈30` ⇒ `r_max=0.035`); rectangle route proved impossible; weighted norms exhausted |
| **G2.5** complexity theorem | **PASS** | `THEOREM_B_ENDPOINT_COMPLEXITY_PROOF.md`: proved with explicit dependencies, proof-dependency map, and honest note that `A(α)` and the strip constant are not tracked |
| **G2.6** benchmark consistency | **PASS** | `benchmark_safe_v4` in a separate namespace (`rescue_compute/`, `state_v4.jsonl`); frozen v3 untouched; identical seeds/designs/scoring; amp `0.100` still running |
| **G2.7** known false claims | **PASS** (with a finding) | `R2_MANDATORY_MANUSCRIPT_CORRECTIONS.md`: exact replacement text for `thm:T20`; **and** the discovery that the Bayesian layer is *absent* from the compiled paper, so Theorem 9.3 and the greedy-MI claim are no longer present — plus a new defect (orphan `sec14/sec15` with 14 nonexistent labels) |
| **G2.8** journal recommendation | **PASS** | `ROUND_02_JOURNAL_DECISION.md`: classified `H3′`; CNSNS primary with scope quotes and dated sources; FCAA proposed for a **split** of Theorem B.2 |

## 4. What I recommend the paper now claims

**Headline (proved, general):** the endpoint-inclusive root-exponential complexity law (Theorem B.2)
and the horizon-invariance lemma (B.1).
**Headline (measured, ecological):** no non-crossing excitation discriminates above chance in the
certified strong-Allee operating window; the linear safety envelope is measurably insufficient.
**Supporting:** Theorem A′ (structural separation, with the `CB=0` counterexample); Theorem C′
(uniform obstruction with explicit constants, exact Gaussian bound replacing Pinsker); Theorem D-NL
(one-sided nonlinear certificate) **stated with its 2.5 % penalty visible**.
**Do not claim:** robust nonlinear safety; kernel-level ecological floors; any design as "optimal";
Bayesian OED; tightness of the testing chain.

## 5. Chief decisions required

1. **Narrative pivot.** Do we reframe the paper around the *negative* result (§2)? I recommend yes: it
   is the strongest true statement and it is defensible. It requires rewriting the abstract and the
   contribution list, not new mathematics.
2. **Split to FCAA.** Publish Lemma B.1 + Theorem B.2 (+ Proposition B.1's cautionary constant) as a
   short analysis paper, and let the CNSNS paper cite it? This is the cleanest use of the round's only
   general proved result.
3. **Round 03 scope.** My priority order: (a) validated-integration safety certificates per design
   (replacing uniform invariant sets — the measured gains of 1.5–2.1 for transient designs show large
   unused slack); (b) certify `Ê_m^state` at `m=64,128` so the large-`m` regime can be discussed
   ecologically at all; (c) sign-aware nonlinear bounds on the prey component; (d) delete
   `sec14/sec15` and execute the `R2_MANDATORY_MANUSCRIPT_CORRECTIONS` list.
4. **Amp 0.100 completion.** Running on Orion + Aureus; will be appended to
   `SAFE_BENCHMARK_V4_REPORT.md` as the reproducibility control against frozen v3.

## 6. Round-02 deliverables

1. `ROUND_01_STATUS_CORRECTIONS.md` ✔  2. `R2_OPERATOR_BRIDGE.md` ✔
3. `THEOREM_D_NONLINEAR_LIFT.md` ✔ (YELLOW)  4. `THEOREM_B_ENDPOINT_COMPLEXITY_PROOF.md` ✔ (GREEN)
5. `THEOREM_C_PRIME_FINAL.md` ✔  6. `SAFE_BENCHMARK_V4_REPORT.md` ✔ (2/3 amplitudes)
7. code + raw outputs in `rescue_compute/` ✔  8. `R2_MANDATORY_MANUSCRIPT_CORRECTIONS.md` ✔
9. `ROUND_02_JOURNAL_DECISION.md` ✔  10. `RESCUE_CLAIM_EVIDENCE_LEDGER.md` updated ✔ (claims 23–34)
11. `ROUND_02_DECISION.md` ✔ (this file)
