# R5-I — Final CNSNS compliance matrix

**Target:** *Communications in Nonlinear Science and Numerical Simulation* (Elsevier, ISSN 1007-5704).
**Gate:** 100% mandatory PASS, ≥99% applicable PASS.
**Result: mandatory 12/14 PASS, 2 RED. Gate NOT met. Both RED items are author-controlled.**

---

## 0. Source of truth

Rows marked **LIVE** are confirmed against the current CNSNS Guide for Authors. Rows marked
**LIVE(chief)** were verified by the chief on 2026-08-24 and recorded in `CHIEF_REVIEW_ROUND_04.md`.
Rows marked **ELSEVIER** come from Elsevier's current journal-wide author policies.

The chief's D2 closed the one item that was unverifiable in Round 04: the guide states **1–7
keywords**. Nothing in this matrix is now marked unverified.

Per the chief's item 12, the live guide and submission checklist must be re-read within 24 hours of
the actual submission. This matrix reflects the state as of this round.

## 1. Mandatory

| # | Requirement | Source | Evidence | Status |
|---|---|---|---|---|
| M1 | Abstract ≤ 250 words | LIVE | **243** words after template migration | **PASS** |
| M2 | Abstract stands alone; no references; no non-standard abbreviations | LIVE | cites nothing; only standard notation | **PASS** |
| M3 | Keywords 1–7 | LIVE(chief) | **6** | **PASS** |
| M4 | Highlights: 3–5 bullets, ≤85 chars incl. spaces, separate editable file with "highlights" in the name | LIVE | `paper/highlights.txt`, **5** bullets, longest **84** chars; survived migration | **PASS** |
| M5 | Numbered square-bracket citations | LIVE | `elsarticle-num`; renders `[1]`-style | **PASS** |
| M6 | Editable source files | ELSEVIER | `main.tex`, `sections/*.tex`, `bibliography.bib` | **PASS** |
| M7 | Declaration of competing interest | ELSEVIER | present, Elsevier's standard wording | **PASS** |
| M8 | Declaration of generative-AI use | ELSEVIER | present and specific | **PASS** |
| M9 | No AI-generated or AI-altered images | ELSEVIER | every figure produced by `benchmark/*.py` from numerical output | **PASS** |
| M10 | Corresponding author: email | ELSEVIER | `ialraddadi@iu.edu.sa`, marked corresponding | **PASS** |
| M11 | Corresponding author: full postal address | LIVE | Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah **42351**, Saudi Arabia | **PASS** |
| M12 | Corresponding author: telephone | LIVE | `+966 50 650 8891` — supplied; goes in the Editorial Manager form, deliberately not printed in the PDF | **PASS** |
| M13 | **Funding declaration** | ELSEVIER | **absent.** Both candidate snippets prepared; neither inserted, because the status is unverified and inventing it would be fabrication | **RED** |
| M14 | **Research data: Option C — deposit and cite/link, or explain why not** | LIVE | deposit **built, checksummed and tested** (`public_reproducibility/`, 50 files); statement present but carries `[REPOSITORY]`, `[DOI]` placeholders pending upload | **RED** |

**Mandatory: 12 PASS, 2 RED.**

## 2. Recommended / applicable

| # | Item | Status |
|---|---|---|
| R1 | Current Elsevier LaTeX format; zero AIMS branding | **PASS** — `elsarticle`, 0 `AIMS` in source or PDF metadata (the 2 hits in rendered text are the word "cl*aims*") |
| R2 | Elsevier-compatible numeric bibliography style (not `plain`) | **PASS** — `elsarticle-num` |
| R3 | CRediT authorship contribution statement | **PASS** — CRediT taxonomy terms |
| R4 | ORCID on the title page | **PASS** — `0000-0002-0094-7937`, confirmed |
| R5 | Numbered sections | **PASS** |
| R6 | Concise manuscript | **PASS** — 44 pp in `preprint,12pt` double-spaced review layout |
| R7 | Artwork: vector preferred; raster ≥300 dpi halftone / ≥1000 dpi line | **PASS** — all 18 cited figures are vector PDF, no raster panels |
| R8 | Figures as separate files | **PASS** — one PDF per figure in `paper/figures/` |
| R9 | Every bibliography entry cited; every citation resolves | **PASS** — 26 rendered, 26 cited by the main text, 0 unresolved, 0 orphaned; 47 uncited entries parked in `bibliography_unused.bib` |
| R10 | DOIs where they exist | **PASS** — 26/30 (87%); the 4 without are two pre-DOI monographs, a 1996 proceedings and the unpublished companion, each with ISBN/venue given |
| R11 | Acknowledgements immediately before references | **n/a** — no acknowledgements section |
| R12 | Graphical abstract | **not prepared** — optional |
| R13 | Clean build: 0 errors, 0 undefined, 0 BibTeX warnings | **PASS** — verified from a fresh directory |

**Applicable: 12 mandatory PASS + 11 recommended PASS + 1 n/a + 1 not-prepared-optional, against
2 mandatory RED.** Of 25 scored items, 23 PASS → **92%**, below the 99% bar because the two RED
items are mandatory.

## 3. Gate arithmetic

- Mandatory: **12/14 = 86%** → fails the 100% requirement.
- Applicable: **23/25 = 92%** → fails the ≥99% requirement.

Both failures reduce to the same two facts, and neither is technical:

1. **Funding status is unknown to me.** Elsevier requires a declaration either way. The standard
   no-funding sentence is one line, but asserting it unverified would put a false statement in the
   submitted record.
2. **The data deposit has no DOI yet.** The package is finished, verified and portable; it needs an
   upload and the identifier that comes back.

## 4. What changed since the Round-04 matrix

| item | Round 04 | now |
|---|---|---|
| keyword count | OPEN (unverifiable, ScienceDirect 403) | **PASS** — chief verified 1–7 |
| postal address | OPEN | **PASS** — Madinah 42351 inserted |
| ORCID | absent | **PASS** — inserted on the title page |
| telephone | OPEN | **PASS** — supplied, for the submission form |
| `elsarticle` | not used, recorded as recommended | **PASS** — migrated |
| bibliography hygiene | 73 entries un-swept, DOIs partial | **PASS** — pruned to 30, 87% DOI, two 2026 arXiv entries verified against the live records |
| data statement | "on request" | Option-C deposit built; **RED only on the DOI** |
| funding | OPEN | still **RED** |

Round 04 had 4 open mandatory items; two are now closed by information the operator supplied, one
by the chief's verification, one by engineering. The two that remain need the author.
