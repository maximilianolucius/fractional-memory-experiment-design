# REJECTED_BASELINE_AUDIT — Round 01, Task 1

**Purpose.** Frozen inventory of the desk-rejected manuscript. No baseline file was modified while
producing this audit. All numbers are measured from the sources, not recalled.

**Baseline identified.** `paper/main.tex` + `paper/sections/sec1..sec11.tex` +
`paper/supplement.tex`, compiled artifacts `paper/main.pdf` (= `paper/fractional-memory-experiment-design.pdf`,
identical size 724 009 B, 2026-08-17) and `paper/supplement.pdf`. Submission package of record:
`submission-staging/submission_fractional-memory-experiment-design_2026-08-17-AIMS-v1.3.zip`.

---

## 1. Identity

| Field | Value |
|---|---|
| Title | *Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator–Prey Model* |
| Title case | **Title Case** — AIMS requires **sentence case** ⇒ non-compliant |
| Author | Ibrahim Alraddadi (single author), `\AIMSAuthors{Ibrahim Alraddadi$^{1,*}$}` |
| Affiliation | Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah, Saudi Arabia |
| Corresponding contact | Email only (`ialraddadi@iu.edu.sa`). **No telephone, no exact postal address** ⇒ non-compliant |
| Layout | `paper/aims_math_style.sty` — a **local imitation** of AIMS, not the official TeX template |
| Document class | `\documentclass[10pt]{article}` |

## 2. Size and content ratio

| Quantity | Count |
|---|---:|
| Main pages | 21 |
| Supplement pages | 29 |
| `theorem` environments (main) | **4** |
| `lemma` / `proposition` / `corollary` / `definition` / `remark` environments (main) | 0 / 0 / 0 / 0 / 0 |
| `\includegraphics` (main) | **20** |
| `\begin{table}` (main) | **13** |
| Sections input by `main.tex` | 11 (`sec1`–`sec11`) |
| Orphan section files present but not input | `sec14.tex`, `sec15.tex` |

**Critical structural finding.** All four theorems live in a **single file, `sec3.tex`**; sections
4–11 are numerical, discussion and end matter. The main text therefore presents **4 theorems against
33 visual objects (20 figures + 13 tables) in 21 pages**, with the mathematics concentrated in one of
eleven sections. This is precisely the editorial signal the recovery plan diagnoses: the manuscript
reads as a benchmark/case study with supporting theory. The supplement, where "complete proofs" are
said to live, declares **one** `\section` ("Fractional solver validation") across 29 pages.

## 3. Bibliography state

| Item | Value |
|---|---|
| Entries in `bibliography.bib` | 76 |
| Distinct keys actually cited | **27** |
| Unused entries | **49** (≈64 % of the file) |
| Style | `\bibliographystyle{plain}` ⇒ **alphabetical**; AIMS requires numbering **by order of first citation** ⇒ non-compliant |
| `lineno` / `\linenumbers` | **absent** ⇒ non-compliant with the current AIMS guidance |

Three load-bearing references audited (Task 2 verifies them externally):
- `P01` — **Lucius, Maximiliano**, *Computer-Assisted Stability and Extinction Certificates for a
  Caputo Predator–Prey System with a Strong Prey Allee Effect*; note: companion manuscript, published
  as Zenodo preprint **DOI 10.5281/zenodo.21809908**.
- `SAFE26A` — Saligrama, *When Can Safe Controllers Adapt? Information before Commitment*, arXiv:2607.16895.
- `SAFE26B` — Ni, Ornik, Chou, Coogan, *Safe, Real-Time Active Model Discrimination and Fault
  Diagnosis for Nonlinear Systems via Differentiable Reachability*, arXiv:2606.19590.

## 4. End matter (as submitted)

Present: `Author contributions`, `Use of AI tools declaration`, `Conflict of interest`.

| Required by AIMS | Present? |
|---|---|
| Author contributions | yes |
| Heading exactly **"Use of Generative-AI tools declaration"** | **no** — reads `Use of AI tools declaration` |
| Generative-AI declaration **before** Acknowledgments | n/a — Acknowledgments absent |
| Acknowledgments | **missing** |
| Funding disclosure | **missing** |
| Conflict of interest | yes |
| Data availability statement | **missing** (and the paper ships a computational package, so it is appropriate) |

## 5. Every place the companion paper is referenced

15 occurrences, confined to `sec1.tex` (Introduction) and `sec10.tex` (Discussion). Verbatim forms found:

- "previously submitted companion paper"
- "previously submitted companion paper and the present manuscript" — the heading of the
  **comparison table in the Introduction** that the recovery plan orders removed
- "previously submitted paper"
- table column header: `Previously submitted paper~\cite{P01}` vs `\textbf{Present paper}`

**Provenance inconsistency (confirmed).** The manuscript has a single author, **Alraddadi**, while
`P01` is authored by **Lucius**. Any first-person phrasing ("our previously submitted companion
paper") is therefore factually wrong and must be replaced by neutral third-person provenance
(handled in Task 7).

## 6. Every place novelty is explicitly disclaimed

Verbatim, all in the main text:

- "**no novelty is claimed for safe experimental design per se**"
- "**inherited** inputs, not new contributions of the present paper"
- "**Inherited backbone versus new experimental layer**" (a heading)
- "inherited from~\cite{P01}: the strong-Allee equations, the …"
- "inherited from~\cite{P01}, where they were derived and certified"
- "each inherited stability fact enters only to select an admissible operating regime"

These sit in the Introduction and Discussion — the two places an editor uses to judge novelty. The
manuscript spends part of its novelty budget arguing what is *not* new.

## 7. Compliance defects already visible in the baseline

1. Title in Title Case (needs sentence case).
2. No `lineno` line numbering.
3. `\bibliographystyle{plain}` (alphabetical, not citation order).
4. Corresponding author lacks telephone and exact postal address.
5. AI-declaration heading not the exact required string.
6. Acknowledgments, funding and data-availability statements missing.
7. Layout produced by a home-made `aims_math_style.sty` rather than the official template.
8. 49 unused bibliography entries.
9. Two orphan section files in the source tree.

## 8. Baseline freeze

Frozen for the rescue: the artifacts listed above plus the v1.3 submission ZIP. Round 01 does not
edit them; all rescue work happens on branch `rescue/aims-desk-rejection`.
