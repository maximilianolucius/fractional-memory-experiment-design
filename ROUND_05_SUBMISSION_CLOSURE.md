# ROUND 05 — FINAL CNSNS SUBMISSION CLOSURE

**Branch:** `rescue/aims-desk-rejection`  
**Role:** Researcher under Chief review  
**Objective:** close the remaining non-scientific blockers and produce a submission-ready CNSNS package. **No new open-ended research.**

Read first:

1. `CHIEF_REVIEW_ROUND_04.md`
2. `ROUND_04_DECISION.md`
3. `CNSNS_COMPLIANCE_MATRIX_FINAL.md`
4. `R4_FORMAT_AND_ENDMATTER_AUDIT.md`
5. `R4_REPRODUCIBILITY_FREEZE.md`
6. `R4_MOCK_EDITOR.md`
7. `R4_MOCK_REFEREES.md`

---

# R5-A — remove AIMS branding and convert the LaTeX submission source

**Authorized. Required.**

1. Replace AIMS front-matter/style with the current Elsevier/CNSNS LaTeX submission format.
2. Prefer the current official Elsevier LaTeX template if available (`elsarticle` if that is the current template in the environment).
3. Remove:
   - `\usepackage{aims_math_style}`;
   - all `\AIMS*` macros;
   - AIMS banner/running headers;
   - AIMS-specific end-matter wording.
4. Preserve:
   - title and scientific content;
   - theorem numbering/cross-references;
   - current abstract <=250 words;
   - 6 keywords;
   - numbered square-bracket citations;
   - figure/table placement where possible.
5. Use an Elsevier-compatible numeric bibliography style; do not use `plain`.
6. Produce a clean-directory build.

**Hard checks:** grep must return zero occurrences of `AIMS`, `aims_math_style`, `\AIMS` in the submission source/PDF metadata and rendered text, except historical/internal files outside the final package.

Deliverable: `R5_TEMPLATE_MIGRATION_AUDIT.md`.

---

# R5-B — corresponding-author metadata

Public records support the following candidate metadata:

- Ibrahim Alraddadi
- Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah 42351, Saudi Arabia
- `ialraddadi@iu.edu.sa`
- ORCID `0000-0002-0094-7937`

Insert the affiliation/postal code and ORCID in the title-page metadata, but mark them in the audit as **PUBLIC-RECORD / AWAITING AUTHOR CONFIRMATION** until final confirmation.

**Do not invent a phone number.** CNSNS's current submission checklist asks for full corresponding-author contact details including phone numbers. Create `AUTHOR_METADATA_CONFIRMATION.md` containing exactly the items the author must confirm/provide:

- preferred full postal address;
- ORCID confirmation;
- corresponding-author telephone number;
- funding statement (see R5-C).

Submission remains blocked until the author provides the phone/funding answer.

Deliverable: `AUTHOR_METADATA_CONFIRMATION.md`.

---

# R5-C — funding statement placeholder, no fabrication

Do not guess funding.

Prepare both candidate snippets in `AUTHOR_METADATA_CONFIRMATION.md`:

**Option 1 — no external funding**
> This research received no external funding.

**Option 2 — funded**
> This research was supported by [FUNDER] under grant [NUMBER].

Only one may enter `main.tex`, after author confirmation.

Until then, keep a clearly marked placeholder in the working branch if necessary, but **the final submission package must contain no placeholder text**.

---

# R5-D — curated public reproducibility deposit package

Create a directory `public_reproducibility/` that is suitable for a persistent archive such as Zenodo.

It must contain only publication-facing reproducibility material:

- final benchmark code needed for manuscript results;
- Round-03/04 computation scripts needed for headline claims;
- frozen machine-readable outputs used by final tables/figures;
- final PWC waveform definitions;
- seed formula and benchmark configuration;
- dependency/environment specification;
- `README.md` with reproduction commands and expected outputs;
- `CLAIM_ARTIFACT_MAP.md` mapping each headline number/table/figure to code + data;
- `MANIFEST_SHA256.txt`;
- code/data license files where appropriate.

Do **not** include Chief reviews, researcher assignments, retraction histories, recovery-plan files, or orchestration internals unless they are necessary to reproduce a published artifact.

Prepare the directory so the operator can upload it unchanged to Zenodo. Do not fabricate a DOI.

The final manuscript data statement must be prepared as:

> The code and research data supporting the findings of this study are available in [REPOSITORY], [DOI/PERSISTENT IDENTIFIER].

Keep `[REPOSITORY]` / `[DOI...]` as explicit blockers until the deposit exists.

Deliverables:

- `public_reproducibility/`
- `R5_DATA_DEPOSIT_AUDIT.md`

---

# R5-E — keyword and highlights verification

The live CNSNS Guide for Authors states:

- **1–7 keywords** required;
- highlights **3–5 bullets**;
- each highlight <=85 characters including spaces;
- highlights submitted as a separate editable file with `highlights` in the filename.

Tasks:

1. Keep 6 keywords unless scientifically improved.
2. Recount the highlights programmatically by characters including spaces.
3. Verify the separate editable highlights file survives template migration.

Deliverable: update `CNSNS_COMPLIANCE_MATRIX_FINAL.md` with M12 = PASS.

---

# R5-F — pooled latent-class documentation repair

No recomputation.

Audit every manuscript occurrence of `latent3` in benchmark tables/captions/prose. Where the reported classification column actually pools `latent1 + latent3`, label it explicitly, e.g.:

> finite-latent class (pooled latent1/latent3 generators)

or another concise unambiguous formulation.

Do not change raw class labels in frozen data files if that would break reproducibility; document the mapping in the manuscript and `public_reproducibility/README.md`.

Deliverable: `R5_LATENT_LABEL_AUDIT.md`.

---

# R5-G — visual pruning

`fig24_safe_design_frontier` is the headline figure.

Remove the old Fig. 10 from the **main manuscript**. If it adds unique historical context, move it to the supplement; otherwise drop it from the submission package. Do not preserve redundancy merely to avoid renumbering.

After removal, check every figure reference and rebuild.

Deliverable: update `R4_FIGURE_AUDIT.md` or create `R5_FIGURE_PRUNE_AUDIT.md`.

---

# R5-H — reference/DOI final sweep

For every cited reference:

1. verify bibliographic metadata;
2. add DOI where one exists;
3. verify every bibliography entry is cited and every citation resolves;
4. ensure McLean and all supporting SOE/quadrature references remain correctly attributed;
5. ensure no withdrawn novelty wording reappears during template migration.

Deliverable: `R5_REFERENCE_AUDIT.md`.

---

# R5-I — final compliance and package audit

Rebuild `CNSNS_COMPLIANCE_MATRIX_FINAL.md` against the live current Guide for Authors.

Current verified journal rules include:

- abstract <=250 words;
- keywords 1–7;
- highlights required, 3–5 bullets, <=85 chars each including spaces;
- editable source files required;
- research data policy Option C: deposit and link data, or explain why it cannot be shared;
- corresponding author must have full contact details including email, full postal address and phone number.

Final internal standard:

- **100% mandatory PASS**;
- **>=99% applicable PASS**.

Anything depending on author confirmation or a Zenodo DOI stays RED rather than guessed.

Deliverable: `R5_COMPLIANCE_FINAL.md`.

---

# R5-J — final clean build and submission package

Once all non-author-controlled tasks are complete:

1. build from a fresh directory;
2. 0 LaTeX errors;
3. 0 undefined refs/citations;
4. 0 BibTeX warnings;
5. 0 stale AIMS branding;
6. abstract <=250 words;
7. all figures separate and present;
8. highlights separate and present;
9. manuscript, bibliography, source figures, supplement and public reproducibility staging all internally consistent.

Create `SUBMISSION_PACKAGE_MANIFEST.md` listing every file to upload to CNSNS and its purpose.

Do not mark **SUBMISSION AUTHORIZED** until phone + funding + persistent data identifier are resolved.

---

# Round 05 final decision states

Only one of these is allowed:

- **READY-PENDING-AUTHOR-METADATA** — all technical work complete, only phone/funding and/or deposit DOI missing.
- **SUBMISSION AUTHORIZED** — every gate green, including author metadata and persistent data deposit.
- **NOT READY** — any scientific, format, build or compliance defect remains.

Deliverable: `ROUND_05_DECISION.md`.
