# ROUND 03 — Researcher decision memo

**Branch:** `rescue/aims-desk-rejection`. All 11 assigned tasks (R3-A … R3-K) executed.
**Headline: I broke our own negative result. The safety–informativeness trade-off that the
submitted paper concludes with is a waveform-parameterisation artifact.**

---

## 1. The one thing that matters

The chief asked me to try to break the Round-02 negative result by searching outside the six
historical waveform families. It broke.

At the *same* peak-amplitude budget (`U = 0.100`) and under a *hard* Allee-margin constraint
(`δ = 0.05`), piecewise-constant inputs achieve:

| | best safe design found | only safe classical design | best classical design (any) |
|---|---|---|---|
| BIC macro-accuracy | **0.803** | 0.514 | 0.763 |
| Allee crossing rate | **0.000** | 0.000 | 0.357 |
| certified margin | **+0.092** | +0.292 | −0.240 |

163 840 candidates evaluated, 87 601 safe. Validated with the *actual* BIC classifier on 672
cells × 100 replicates, identical seeds, zero divergences. Six of six search designs are safe;
five of six beat the best classical design of any kind, safe or not. All twelve best safe
candidates are piecewise constant — a class the paper never tested.

Consequences: the abstract's concluding sentence is false as stated, Discussion §3 is unscoped,
Figure 10 plots a frontier that is not the frontier, and the paper's real result — *latent
complexity, not safety, is the binding obstruction* — was never stated. All four are now fixed
in the manuscript (R3-I), which compiles clean.

## 2. Deliverables

| task | file | verdict |
|---|---|---|
| R3-A | `R3_THEOREM_B_RIGOROUS.md` | Proof completed and simplified (endpoint split unnecessary). **Demoted to a lemma: the technique is McLean (2018).** FCAA split withdrawn. |
| R3-B | `R3_RESPONSE_OPERATOR_SEMANTICS.md` | T23 stands. Three error objects separated; the plant attenuates the kernel error monotonically `1.009 → 0.675`. Warns against reading `Ê_m^state` as a design objective, with an in-paper counterexample. |
| R3-C | `R3_NONLINEAR_CERTIFICATE_CONSTANTS.md` | `M₂` interval-certified; Round-02 sampling understated it 19–76%. `r_max = 0.0294` (not 0.0350). Invariant-ball route structurally closed. |
| R3-D | `R3_VALIDATED_SAFETY_REPORT.md` | 28/28 verdicts certified, 0 indeterminate. **Every sampled verdict in the manuscript confirmed.** The found design is certified safe under all four models. |
| R3-E | `R3_RESPONSE_CERT_M64_M128.md` | Response-level error to `m = 128`; testing floor `0.49999`. |
| R3-F | `R3_SAFE_DESIGN_ADVERSARIAL_SEARCH.md` | **The falsification.** §1 above. |
| R3-G | `R3_NONLINEAR_DISCRIMINATION_AUDIT.md` | Manuscript chain clean. **My own Round-02 Theorem D-NL is vacuous** (`P_e^* ≥ 2.6e−11`) from a double-counted gain; corrected to `0.4984`. Exact bound replaces Pinsker. |
| R3-H | `R3_V4_REPRODUCIBILITY_CONTROL.md` | v4 complete, 3 amplitudes, 2268 cells. **v3 reproduces to four decimals on another host.** Amplitude hypothesis refuted. |
| R3-I | `R3_MANUSCRIPT_CORRECTIONS_EXECUTED.md` | 11 edits executed; build clean (exit 0, 0 undefined refs, 24 pp). |
| R3-J | `R3_TITLE_ABSTRACT_CONTRIBUTIONS.md` | New title, abstract, six-item contribution list, deletion list. |
| R3-K | `CNSNS_COMPLIANCE_MATRIX_DRAFT.md` | One **blocking** item: prior-art citation for T9b. |

The `amp = 0.100` v4 job was allowed to finish without restart, as instructed. It completed on
Aureus (756/756, `DONE`, 0 divergences).

## 3. What I retracted this round

Seven items, all mine, listed in `RESCUE_CLAIM_EVIDENCE_LEDGER.md` §"Round 03 retractions". The
two that matter:

- **Theorem D-NL (Round 02) is vacuous as written.** The factor `A_NL = ‖C‖E_α((‖J‖+M₂r)T^α)`
  multiplies a bound that Young's inequality already closes, because `E_m^G` is an *end-to-end
  response* error. With `‖J‖₂ = 0.5664` this makes the stated floor `2.6e−11`. Removing the
  factor gives `0.4984` — the conclusion strengthens, but the inequality I wrote carried no
  information.
- **The root-exponential constant "verified to 0.35%" was a single-`α` reading.** Across five
  `α`, `c_fit/c_theory ∈ [0.81, 1.32]`. Withdrawn. What *is* verified: the bound holds with
  constants `A ∈ [0.29, 11.1]` on 285 cells, is tight at `α = 0.70, m = 128` (slack 1.00×), and
  `m(ε)` predicts the measured latent budget within a factor ~1.5.

## 4. Decisions I need from the chief

1. **T9b demotion — blocking for submission, and I did not do it unilaterally.** R3-A shows the
   `L¹` exponential-sum construction is McLean (2018), same technique, positive weights, on
   `[δ,T]`. Ours adds the endpoint. That is a lemma. Changing a theorem's claimed status in the
   manuscript is your call; wording and the six references are in R3-A §8. **Submitting without
   this repeats the desk-rejection failure mode.**
2. **Title.** I applied option T1 ("Waveform Design, Not Amplitude, …"). T2 leads with the
   theoretical conclusion, T3 is the minimal edit. Easy to switch.
3. **Figures.** Fig. 10's caption is corrected but the figure still plots six points; and the
   paper's main result (margin vs accuracy over 12 designs) has no figure. Both need
   `make_figures.py` work — say the word and I do it.
4. **Journal.** With the FCAA split withdrawn, CNSNS is the only target. Confirm, or reconsider
   now that the headline is a falsification plus a positive design result rather than an
   approximation theorem.
5. **Scope of Stage 3.** A certified global bound over the `pwc4` class (interval
   branch-and-bound) would upgrade R3-F from *existence* to *optimality*. Not done. Worth it?

## 5. Honest assessment

The paper is better than the one that was desk-rejected, and for the right reason: its central
claim was wrong and we found that out ourselves rather than having a referee find it. What is
now on the table is a falsification with 163 840 evaluations behind it, a positive design result
that beats every published baseline in the paper, a reproducibility control almost no submission
carries, and an honest statement of the obstruction that actually binds.

The remaining risk is not scientific, it is decision 1 of §4 above: one uncited 2018 paper.
