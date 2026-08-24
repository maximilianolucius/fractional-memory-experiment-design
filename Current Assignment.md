# Current Assignment

**Task:** Desk-rejection rescue — Round 03 proof rigorization, validated safety, and adversarial safe-design search  
**Status:** IN PROGRESS  
**Timestamp:** 2026-08-24 14:08 ART  
**Branch:** `rescue/aims-desk-rejection`

## Assigned role

Researcher under Chief review.

## Round-02 status

Round 02 is **accepted as a major scientific advance**, but several Researcher PASS/GREEN labels were reopened by Chief review before manuscript publication.

Read:

- `CHIEF_REVIEW_ROUND_02.md`
- `ROUND_03_RESEARCHER_ASSIGNMENT.md`

## Chief decisions now in force

### Narrative pivot

**YES.** The rescued paper will pivot toward the negative safety/informativeness result.

Current permissible headline wording is protocol-bounded:

> Within the evaluated strong-Allee benchmark, the waveform families that remain non-crossing lose essentially all useful memory-mechanism discrimination at the linear-certificate amplitude, while the most discriminative sustained designs frequently cross the Allee threshold.

Do **not** claim universal “no safe excitation discriminates” until a theorem or a certified global bound over a declared input class exists.

### Journal

- Do not resubmit to AIMS Mathematics.
- **CNSNS remains the provisional primary target.**
- Do not migrate to `elsarticle` yet; content/theorem status must stabilize first.
- Final submission must later satisfy **100% mandatory requirements** and **>=99% of the complete applicable checklist**, using instructions/template refreshed within 24 h of submission.

### FCAA split

**Deferred.** Keep Lemma B.1 / Theorem B.2 in the main rescue for now. Reconsider a standalone analysis paper only if Round 03 produces a fully rigorous sharp/near-sharp endpoint theorem and preferably a lower/optimality result.

## Mandatory Chief re-openings from Round 02

1. **Theorem B.2 exact constant is not yet accepted.** The finite/infinite trapezoidal construction, `d→π/2` limit, endpoint term, and hidden prefactor must be repaired.
2. **Theorem C′ operator semantics must be fixed.** A fixed-input response quotient cannot support waveform-uniformity; use an induced operator norm or certified impulse-response `L¹` bound.
3. **`U_NL` is not yet a rigorous numeric certificate** if `M₂`, `Γ_B`, or `Γ_R` are based on sampled/high-accuracy rather than interval/analytic suprema.
4. **Nonlinear discrimination must be re-derived** so kernel-level, linear response-level, and nonlinear response-level errors are never multiplied or renamed inconsistently.
5. v4’s “0.259 vs 0.25” result is **EMPIRICAL** until trajectory safety is validated.
6. The negative result must be attacked by searching for safe informative inputs outside the original six waveform families.

## Round-03 hard targets

1. Publication-grade endpoint positive-SOE theorem.
2. Exact response-operator semantics and final Gaussian/minimax theorem.
3. Rigorous nonlinear safety constants.
4. Validated trajectory safety/crossing labels.
5. Direct response-level `m=64,128` certification if feasible.
6. Adversarial safe-design search over new finite-dimensional waveform classes.
7. Correct nonlinear difference theorem.
8. Complete `amp=0.100` v4 reproducibility control when the already-running computation finishes.
9. Execute all mandatory manuscript corrections only after claims stabilize.
10. Rewrite title/abstract/contributions around the corrected negative result.
11. Build a provisional CNSNS compliance matrix while preserving the >=99% policy.

## Required Round-03 outputs

- `R3_THEOREM_B_RIGOROUS.md`
- `R3_RESPONSE_OPERATOR_AUDIT.md`
- `R3_THEOREM_C_FINAL.md`
- `R3_NONLINEAR_CERTIFICATE_CONSTANTS.md`
- `R3_VALIDATED_SAFETY_REPORT.md`
- `R3_RESPONSE_CERT_M64_M128.md`
- `R3_SAFE_DESIGN_ADVERSARIAL_SEARCH.md`
- `R3_NONLINEAR_DISCRIMINATION_AUDIT.md`
- `R3_V4_REPRODUCIBILITY_CONTROL.md`
- modified `paper/` + `R3_MANUSCRIPT_CHANGELOG.md`
- `R3_TITLE_ABSTRACT_CONTRIBUTIONS.md`
- `CNSNS_COMPLIANCE_MATRIX_DRAFT.md`
- updated `RESCUE_CLAIM_EVIDENCE_LEDGER.md`
- `ROUND_03_DECISION.md`
- versioned code/raw outputs under `rescue_compute/`

## Computational policy

- Orion: large parallel search/certification/Monte Carlo.
- Aureus: **32 cores**, use a conservative worker count consistent with current load.
- Do not restart the already-running `amp=0.100` control.
- Do not overwrite frozen v3, Round-02 raw data, or historical certificates.
- Long jobs must checkpoint and be restartable.

**Next Chief action:** review Round-03 theorem/certificate outputs and decide whether the reconstructed manuscript is strong enough to enter final CNSNS formatting/compliance and mock-referee review.
