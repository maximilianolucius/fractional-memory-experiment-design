# Validation Report — Chief Round 6

Date: 2026-08-14

## Mathematical/numerical audit

- Exact scalar pole/branch decomposition checked against the Mittag-Leffler series at representative times by the released researcher validator.
- Full researcher validator is computationally expensive; a chief lightweight independent checker was added using a transformed time grid `t = T x^3` to resolve the integrable near-zero singularity.
- All 8 focal T23 cells pass the independent float cross-check.
- Float/certified ratios range from approximately 0.187 to 0.383.
- The first coarse uniform-grid audit that appeared to fail at `(A,m)=(0.30,16)` was diagnosed as a quadrature-grid artifact and replaced by the transformed-grid checker.

## Visual audit

- Figure 11: byte-identical to post-R5 chief package; frozen.
- Figure 13: corrected because the original semantics incorrectly implied identical Jacobian generators across all rival mechanisms.
- Figure 19: replaced by a two-panel theorem-faithful figure; broad mass-only Strong-Allee panel removed.
- All other pre-R6 figure PDFs are byte-identical to the post-R5 chief package.
- Selected final PDF pages were rendered at 130 dpi and inspected; no clipping or overlap found on the changed pages.

## Build

Final chief build:

- pages: 80
- undefined citations: 0
- undefined references: 0
- final-pass LaTeX/package warnings: 0

`bibtex` is unavailable in the current runtime, so `main.bbl` was updated consistently with the four added verified related-work references. `bibliography.bib` contains the corresponding records for a future normal BibTeX rebuild.
