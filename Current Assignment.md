# Current Assignment

**Task:** Desk-rejection rescue — Round 02 mathematical closure before manuscript rebuild  
**Status:** IN PROGRESS  
**Timestamp:** 2026-08-24 12:34 ART  
**Branch:** `rescue/aims-desk-rejection`

## Assigned role

Researcher under Chief review.

## Round-01 status

Round 01 is **accepted with mandatory Chief corrections**. The detailed review is in:

- `CHIEF_REVIEW_ROUND_01.md`

The full Round-02 mandate is:

- `ROUND_02_RESEARCHER_ASSIGNMENT.md`

## Current objective

Determine whether the rescue can be upgraded from a correct but modest **linearized** safety/information result into a genuinely stronger paper with:

1. a rigorously separated memory-kernel vs actual input→output approximation layer;
2. a **nonlinear**, preferably model-family-robust Strong-Allee safety certificate;
3. an explicit nonlinear safety→separation→Gaussian-testing chain;
4. a proved endpoint-inclusive positive-exponential-sum complexity bound;
5. a benchmark rerun in a genuinely lower-amplitude regime, without overwriting frozen v3.

## Chief decisions now in force

### Journal

- **Do not resubmit the current reconstruction to AIMS Mathematics.**
- Provisional primary fit after Round 02: **Communications in Nonlinear Science and Numerical Simulation (CNSNS)**.
- *Fractional Calculus and Applied Analysis* is a stretch option only if both the endpoint complexity theorem and nonlinear lift become materially strong.
- Final journal selection occurs after Round 02.

### Nonlinear theorem

- **Attempt the nonlinear Volterra/fractional-Grönwall lift now.**
- Do not ship the present linearized Theorem D before this attempt.
- If the lift fails, document the exact obstruction and retain a narrower linearized theorem with corrected language.

### Benchmark

- **Low-amplitude benchmark rerun is authorized.**
- Frozen v3 must remain immutable.
- Run a new version at least at peak amplitudes `0.050`, `0.063`, and the `0.100` comparison baseline.
- Runs below the Round-01 bound are initially labelled **linear-certificate diagnostics**, not nonlinear safety certificates, until `U_NL(δ)` is proved.

## Mandatory Chief corrections inherited from Round 01

1. Finite C-1 fits do **not** determine the asymptotic convergence class; remove unsupported big-O claims.
2. Separate bare Caputo kernel error `E_m^K` from actual prey-response error `E_m^G`.
3. Do not feed `m=64,128` C-1 kernel errors into the ecological Theorem D without a proved resolvent bridge.
4. Replace “all safe inputs” by the precise certified sufficient input class unless equivalence is proved.
5. A linearized state ball does not certify nonlinear ecological safety.
6. Prefer robust safety across the declared rival mechanism class; otherwise label the result one-sided.

## Round-02 highest priorities

1. `R2_OPERATOR_BRIDGE.md`
2. `THEOREM_D_NONLINEAR_LIFT.md`
3. `THEOREM_B_ENDPOINT_COMPLEXITY_PROOF.md`
4. `THEOREM_C_PRIME_FINAL.md`
5. `SAFE_BENCHMARK_V4_REPORT.md`
6. exact correction package for Theorem 9.3 / OED / Bayesian overclaims
7. journal decision based on the actual mathematics that survives

## Journal-compliance policy

The final selected journal submission must follow the **then-current official instructions and official TeX template**:

- **100% compliance with mandatory requirements**;
- **>=99% compliance with the complete applicable checklist**;
- instructions and template re-downloaded and re-checked within 24 hours before submission.

No homemade journal-like style is a source of truth.

## Required Round-02 outputs

- `ROUND_01_STATUS_CORRECTIONS.md`
- `R2_OPERATOR_BRIDGE.md`
- `THEOREM_D_NONLINEAR_LIFT.md`
- `THEOREM_B_ENDPOINT_COMPLEXITY_PROOF.md`
- `THEOREM_C_PRIME_FINAL.md`
- `SAFE_BENCHMARK_V4_REPORT.md`
- versioned benchmark code/raw outputs
- `R2_MANDATORY_MANUSCRIPT_CORRECTIONS.md`
- `ROUND_02_JOURNAL_DECISION.md`
- updated `RESCUE_CLAIM_EVIDENCE_LEDGER.md`
- `ROUND_02_DECISION.md`

**Next Chief action:** review Round-02 outputs and decide whether the manuscript has crossed the threshold for a nonlinear theorem-first rebuild, or should be reframed as a narrower applied fractional-dynamics paper.
