# Current Assignment

**Task:** Desk-rejection rescue — Round 05 final CNSNS submission closure  
**Status:** IN PROGRESS  
**Timestamp:** 2026-08-24 17:18 ART  
**Branch:** `rescue/aims-desk-rejection`

## Assigned role

Researcher under Chief review.

## Round-04 status

Round 04 is **scientifically accepted**. The remaining blockers are submission engineering, author metadata and persistent data deposition.

Read first:

- `CHIEF_REVIEW_ROUND_04.md`
- `ROUND_05_SUBMISSION_CLOSURE.md`
- `ROUND_04_DECISION.md`
- `CNSNS_COMPLIANCE_MATRIX_FINAL.md`

## Chief decisions now in force

### Science

No new open-ended mathematics is required for this submission.

The final scientific message is:

> A severe safety-information frontier appears when design is restricted to the six classical waveform families, but it is not intrinsic to the system. Expanding the waveform class finds safe, substantially more informative piecewise-constant inputs, while increasing latent-rival complexity remains a separate finite-horizon identifiability obstruction.

Keep all scope restrictions and the Round-04 safety downgrade.

### Journal

- **CNSNS is the sole active target.**
- AIMS Mathematics is not a target.
- FCAA split is withdrawn.

### Template

**AUTHORIZED AND REQUIRED:** remove all AIMS branding and migrate the final submission source to the current Elsevier/CNSNS LaTeX format. No `aims_math_style.sty` or `\AIMS*` macros may remain in the submission package.

### Journal rules newly verified by Chief

The current CNSNS Guide for Authors states:

- abstract <=250 words;
- **1–7 keywords** — the manuscript's 6 keywords are compliant;
- highlights required: 3–5 bullets, <=85 characters each including spaces, separate editable file;
- editable source files required;
- research-data policy **Option C**: deposit and cite/link the data, or explain why sharing is impossible;
- corresponding author submission checklist requires full contact details including **email, full postal address and phone numbers**.

### Corresponding author

Public academic records strongly support:

- Ibrahim Alraddadi
- Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah 42351, Saudi Arabia
- `ialraddadi@iu.edu.sa`
- ORCID `0000-0002-0094-7937`

Insert affiliation/postal code and ORCID, but obtain author confirmation before metadata freeze. **Do not invent the phone number.**

### Funding

Funding status must be explicitly confirmed by the author. Do not infer “no funding.”

### Data availability

Chief decision: **curated persistent deposit**, not “available on request.” Prepare `public_reproducibility/` containing only publication-facing code/data/artifacts, then deposit it in Zenodo or another persistent repository and cite the DOI/identifier in the manuscript. Internal rescue/review documents are excluded from the curated data package.

### Visuals

- Keep `fig24_safe_design_frontier` as the headline figure.
- Remove old Fig. 10 from the main manuscript; move to supplement only if it adds unique context.

### Benchmark label

Fix the undocumented pooled latent label (`latent1 + latent3`) in manuscript tables/captions/prose without changing frozen raw data.

## Round-05 priorities

1. Current Elsevier/CNSNS LaTeX migration; zero AIMS branding.
2. Add public-record author affiliation/postal code + ORCID; create author-confirmation checklist for phone/funding.
3. Build curated `public_reproducibility/` deposit staging area.
4. Change data statement from “on request” to persistent-repository wording with DOI placeholder until deposit exists.
5. Mark keyword rule PASS (1–7; six supplied).
6. Fix pooled latent-class documentation.
7. Remove/relegate redundant Fig. 10.
8. Full DOI/reference sweep.
9. Rebuild final CNSNS compliance matrix.
10. Clean build + submission package manifest.
11. Produce binary Round-05 decision.

## Hard authorization gate

Final submission requires:

- **100% mandatory requirements PASS**;
- **>=99% applicable checklist PASS**;
- author-confirmed phone number;
- author-confirmed funding statement;
- persistent data-deposit identifier/DOI;
- live CNSNS Guide/checklist rechecked within 24 hours before submission;
- clean build and zero AIMS branding.

Until phone, funding and deposit DOI are resolved, the strongest permissible status is **READY-PENDING-AUTHOR-METADATA**.

**Next Chief action:** review the Round-05 closure package; authorize submission only when every hard gate is green.
