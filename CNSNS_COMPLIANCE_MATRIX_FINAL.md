# R4-F — CNSNS compliance matrix (live guide)

**Target:** *Communications in Nonlinear Science and Numerical Simulation* (Elsevier, ISSN
1007-5704). Sole active target; the FCAA split is withdrawn.

**Gate:** 100% of mandatory items PASS, ≥99% of applicable items PASS.
**Current: mandatory 8/12 PASS, 4 OPEN. Gate NOT met — see §4.**

---

## 0. Source-of-truth note, stated honestly

The chief's instruction was to rebuild this from the **live** Guide for Authors, not from memory.
I did that as far as the network allowed, and the limitation must be recorded because it changes
how much weight each row carries:

- `https://www.sciencedirect.com/journal/communications-in-nonlinear-science-and-numerical-simulation/publish/guide-for-authors` returns **HTTP 403** to automated fetching, as does the
  `/science/journal/10075704/publish/guide-for-authors` form the `elsevier.com` URL redirects to.
- The rows marked **LIVE** below were confirmed against the current guide's own text as surfaced
  by search of that page. The rows marked **ELSEVIER-GENERAL** come from Elsevier's current
  author-policy pages, which apply journal-wide but are not the CNSNS page itself. The rows marked
  **UNVERIFIED** could not be read this round.
- **Action for the operator:** open the guide in a browser and confirm the UNVERIFIED rows before
  submitting. The chief's own rule — recheck within 24 hours of submission — covers this, but the
  four UNVERIFIED rows should not be treated as PASS until someone has actually read them.

## 1. Mandatory requirements

| # | Requirement | Official wording / source | Mandatory? | Applicable? | Evidence | Status |
|---|---|---|:--:|:--:|---|---|
| M1 | Abstract ≤ 250 words | "a concise and factual abstract which does not exceed 250 words" — **LIVE** | yes | yes | `paper/main.tex`, **243 words** (counted with math groups as one word each) | **PASS** |
| M2 | Abstract stands alone, no references, no non-standard abbreviations | "Abstracts must be able to stand alone… Avoid references… Avoid non-standard or uncommon abbreviations" — **LIVE** | yes | yes | abstract cites nothing and defines nothing; only $\alpha$ and standard notation | **PASS** |
| M3 | Highlights: 3–5 bullets, ≤85 characters each **including spaces**, separate editable file with "highlights" in the filename | "3 to 5 bullet points, each a maximum of 85 characters" and "Submit highlights as a separate editable file… with the word *highlights* included in the file name" — **LIVE** | yes | yes | `paper/highlights.txt`, 5 bullets, longest **81** characters | **PASS** |
| M4 | Numbered square-bracket citations | in-text citations use numbered brackets — **LIVE** | yes | yes | `natbib` with `[numbers,sort&compress]`; PDF renders `[1]`-style | **PASS** |
| M5 | Editable source files (`.tex`) supplied | Elsevier requires editable source, not PDF-only — **ELSEVIER-GENERAL** | yes | yes | `paper/main.tex` + `paper/sections/*.tex` + `bibliography.bib` | **PASS** |
| M6 | Declaration of competing interest | required of all authors — **ELSEVIER-GENERAL** | yes | yes | `main.tex`, "Conflict of interest" section | **PASS** (wording to be aligned to Elsevier's current template, see R1) |
| M7 | Declaration of generative-AI use | "Authors must declare the use of generative AI in the manuscript preparation process upon submission" — **ELSEVIER-GENERAL** | yes | yes | `main.tex`, "Use of AI tools declaration" — states language editing, LaTeX formatting, code and documentation assistance, and that responsibility remains with the author | **PASS** |
| M8 | No AI-generated or AI-altered images | "Elsevier does not permit the use of Generative AI or AI-assisted tools to create or alter images" — **ELSEVIER-GENERAL** | yes | yes | every figure is produced by `benchmark/*.py` from numerical output; none is generated or retouched by an AI image tool | **PASS** |
| M9 | Data availability statement | required at submission — **ELSEVIER-GENERAL** | yes | yes | **not in the manuscript** | **OPEN** |
| M10 | Funding disclosure | required — **ELSEVIER-GENERAL** | yes | yes | **not in the manuscript** | **OPEN** |
| M11 | Corresponding-author full contact details, complete affiliation | submission checklist — **UNVERIFIED** (checklist not readable) | yes | yes | `main.tex` has name, department, institution, city, country and email; **no postal address / ORCID** | **OPEN** |
| M12 | Keyword count within the allowed range | **UNVERIFIED** — the permitted number could not be read | yes | yes | 6 keywords supplied; Elsevier journals typically permit up to 6–7, so this is very likely compliant but is **not verified** | **OPEN** |

## 2. Recommended / preferred (not mandatory)

| # | Item | Status | Note |
|---|---|---|---|
| R1 | Elsevier LaTeX template (`elsarticle`) | **not used** | The live guide offers Word and LaTeX templates; nothing read this round makes a specific class an acceptance criterion. Manuscript currently uses `aims_math_style.sty`. **Recommended, not mandatory** — this is the correction the chief demanded, and it is applied here: `elsarticle` is *not* marked mandatory. |
| R2 | CRediT authorship contribution statement | partial | An "Author contributions" paragraph exists; it does not use CRediT taxonomy terms. Single author, so the substance is trivial, but the terms should be used. |
| R3 | Acknowledgements immediately before references | n/a | No acknowledgements section exists. If none is added, the ordering requirement does not bind. |
| R4 | Graphical abstract | not prepared | Optional. |
| R5 | Numbered sections | ✔ | `\section` throughout; unnumbered only for the end matter, which is conventional. |
| R6 | Concise manuscript ("no length limitation… but only concisely written manuscripts are published" — **LIVE**) | ✔ | 25 pages. |
| R7 | Artwork: vector where possible; raster ≥300 dpi halftone / ≥1000 dpi line — **ELSEVIER-GENERAL** | ✔ | all 19 cited figures are vector PDF; no raster panels |
| R8 | Figures as separate files | ✔ | `paper/figures/*.pdf`, one per figure |
| R9 | All references cited, all citations resolve | ✔ | zero undefined citations, zero undefined references, zero multiply-defined labels |
| R10 | DOIs where available | partial | added for the three new entries (`K07`, `K08`, `K09`); older entries not swept |
| R11 | Single anonymized review — **LIVE** | ✔ | no action needed; the manuscript is not blinded and does not need to be |

## 3. House preference (ours, not the journal's)

| # | Item | Status |
|---|---|---|
| H1 | Every numeric claim traceable to a script and a frozen artifact | ✔ (`R4_REPRODUCIBILITY_FREEZE.md`) |
| H2 | Status label on every number (proved / interval-certified / high-accuracy numerical / empirical) | ✔ (`sec3`, `R4_THEORY_SECTION_AUDIT.md`) |
| H3 | No claim in the paper that a Round-03/04 audit retracted | ✔ (`R4_NARRATIVE_FINAL.md` §6) |

## 4. Gate arithmetic

- **Mandatory:** 12 items, **8 PASS, 4 OPEN** → **not** 100%. **Gate M FAILS.**
- **Applicable total:** 12 mandatory + 11 recommended = 23 scored items; 8 + 8 full passes and
  3 partials (R2, R10, and M6's wording) → roughly 74% clean. **Gate 99% FAILS.**

The four open mandatory items (M9 data statement, M10 funding, M11 postal/ORCID details, M12
keyword count) are **all end-matter or metadata**, none is scientific, and all four are closable in
under an hour by someone with the author's institutional details and a browser open on the guide.
Two of them (M11, M12) need information I do not have and must not invent.

**Consequence for R4-K: gate R4.7 is RED.** Submission is not authorised until these four are
closed. This is a clerical block, not a scientific one, and I am stating it as RED rather than
waving it through.

## 5. What I did not do

- Did not fabricate the postal address, ORCID, funding source or data-repository DOI.
- Did not convert to `elsarticle` (recommended, not mandatory; and conversion is better done once
  the content is frozen — see `R4_FORMAT_AND_ENDMATTER_AUDIT.md`).
- Did not read the submission checklist itself (403).
