# Current Assignment

**Task:** Desk-rejection rescue — Round 04 CNSNS submission closure  
**Status:** IN PROGRESS  
**Timestamp:** 2026-08-24 15:28 ART  
**Branch:** `rescue/aims-desk-rejection`

## Assigned role

Researcher under Chief review.

## Round-03 status

Round 03 is **accepted as a major scientific advance**. The adversarial search falsified the paper's previous system-level safety–informativeness conclusion and found substantially better safe piecewise-constant designs at the same amplitude budget.

Read first:

- `CHIEF_REVIEW_ROUND_03.md`
- `ROUND_04_RESEARCHER_ASSIGNMENT.md`

## Chief decisions now in force

### Scientific narrative

The rescued manuscript now centers on:

> The severe safety–informativeness frontier observed across the six classical waveform families is a parameterisation artifact. A constrained search over previously untested piecewise-constant waveforms finds safe designs that outperform every historical baseline at the same peak-amplitude budget.

Do **not** universalize this into “waveform design governs safety” or “safety has no information cost.” A Pareto cost remains; what failed was the six-family frontier as a system-level conclusion.

### Supporting latent-complexity result

Increasing latent-rival complexity remains a separate finite-horizon obstruction. The response-level error has been carried to `m=128`; keep this as a distinct theoretical/computational result, never as a consequence of bare-kernel error alone.

### Theorem B / T9b

**Chief decision: DEMOTE.**

- The positive-SOE/log-quadrature technique, positivity of weights, and root-exponential order are prior art.
- Add McLean (2018) prominently and cite the surrounding literature.
- Retain only the endpoint-inclusive `L¹(0,T)` safe-form estimate and exact `T^α` scaling as a supporting lemma/tool.
- The boundary constant is open.
- **FCAA split is withdrawn.**

### Headline safety status

Round-03 safety verification is improved but **not yet a fully rigorous certificate** because the PECE solver-error term is refinement-estimated and the tube source bound is gridded rather than interval-enclosed.

Round 04 must either:

1. obtain genuine rigorous enclosures for the headline `pwc6` and `multiscale` trajectories under all four mechanisms; or
2. downgrade every unqualified `certified/validated` claim to precise a posteriori verification wording.

No ambiguous final status is allowed.

### Journal

- **CNSNS is now the sole active target.**
- Do not resubmit to AIMS Mathematics.
- Do not pursue the FCAA split.
- Use the live CNSNS Guide for Authors as source of truth.
- Final gate: **100% mandatory compliance and >=99% of the complete applicable checklist**, with instructions/template rechecked within 24 h before submission.

### Working title

> **Safe discrimination of fractional, delayed, and latent memory beyond classical waveforms in a strong-Allee predator–prey model**

The previous “Waveform Design, Not Amplitude, Governs…” title is withdrawn as too universal.

## Round-04 highest priorities

1. Demote T9b and repair prior-art citations.
2. Close or explicitly downgrade the headline safety certificate.
3. Rebuild the stale theory section with response-level semantics and the exact Gaussian bound.
4. Rewrite abstract to CNSNS limit (<=250 words), Introduction, contributions and conclusion.
5. Remove the companion-comparison table and use one neutral provenance paragraph.
6. Build the new headline safety-margin vs macro-accuracy figure including searched PWC designs.
7. Rebuild the CNSNS compliance matrix from live official instructions.
8. Remove AIMS-only formatting and complete CNSNS/Elsevier end matter.
9. Freeze reproducibility artifacts.
10. Run mock-editor and adversarial-referee gates.
11. Produce a binary Round-04 submission decision.

## Required Round-04 outputs

- `R4_PRIOR_ART_AND_THEOREM_STATUS.md`
- `R4_HEADLINE_SAFETY_CERTIFICATE.md`
- `R4_THEORY_SECTION_AUDIT.md`
- `R4_NARRATIVE_FINAL.md`
- `R4_FIGURE_AUDIT.md`
- `CNSNS_COMPLIANCE_MATRIX_FINAL.md`
- `R4_FORMAT_AND_ENDMATTER_AUDIT.md`
- `R4_REPRODUCIBILITY_FREEZE.md`
- `R4_MOCK_EDITOR.md`
- `R4_MOCK_REFEREES.md`
- `ROUND_04_DECISION.md`
- modified `paper/` + final submission-side files

**Next Chief action:** review Round-04 closure package and authorize submission only if all R4.1–R4.10 gates are GREEN.
