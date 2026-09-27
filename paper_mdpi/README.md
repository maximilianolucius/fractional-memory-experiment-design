# MDPI version — mathematics-fmed.tex

New version of the paper following `agent_directives_publishable_first_submission.md`
(fractional-d-stability-networks repo) and the MDPI template exactly as the accepted
reference paper (mathematics-4528508, the companion study).

Build (no shell-escape, no bibtex needed — manual thebibliography):

    pdflatex mathematics-fmed.tex && pdflatex mathematics-fmed.tex

State: 20 pages (ceiling 25), 12 figure environments / 19 panels, 2 tables,
0 errors, 0 undefined references, 0 overfull boxes, 0 AI references.

Companion artifacts required by the directives: `../research/CLAIMS.md`,
`../research/SCOPE_MATRIX.md`, `../research/PRE_SUBMISSION_RESPONSE.md`.

## Decisions taken per the directives, flagged for the operator

1. **AI-use declaration removed** (directive §0.2 forbids any AI reference). The CNSNS
   version keeps its declaration; MDPI's disclosure, if required by current policy, must
   go in the submission system, not the manuscript, or the directive must be revisited.
2. **Preprint disclosure moved out of the body.** The Zenodo preprint
   (10.5281/zenodo.21809908) is not cited in this version; disclose it in the MDPI
   submission form / cover letter. The record's creator republish is still pending.
3. **Companion NOT cited** (directive: no unpublished references; it is accepted but has
   no DOI yet). Backbone attributed to Wang–Shi–Wei (J. Math. Biol. 2011); stability facts
   re-derived from the exact invariants. Re-cite the companion once its DOI exists.
   Two arXiv references replaced by published sources (Sui et al. ICML 2015; Harirchi & Ozay
   Automatica 2018).
4. **Data availability statement removed on operator instruction (2026-09-27).**
   The manuscript carries no data statement; if MDPI requires one at submission,
   supply it in the submission form or reinstate the paragraph.
