# What to upload to CNSNS, and as what

Editorial Manager, *Communications in Nonlinear Science and Numerical Simulation*.
Single anonymized review — the manuscript is **not** blinded and does not need to be.

**Before uploading, read §4. One item is not closed.**

---

## 1. Files, by Elsevier item type

| Elsevier item type | file(s) here |
|---|---|
| **Manuscript** (LaTeX source) | `manuscript/main.tex`, `manuscript/sections/sec1.tex` … `sec11.tex`, `manuscript/bibliography.bib` |
| **Manuscript PDF** | `manuscript.pdf` — 44 pp, built from the source in `manuscript/` |
| **Highlights** | `highlights.txt` — 5 bullets, longest 84 characters |
| **Figure** (one item per file) | the 18 PDFs in `figures/` |
| **Cover letter** | `cover_letter.md` — paste into the portal's cover-letter field |

Upload the source files and the figures; Editorial Manager compiles its own PDF and the one here is
for comparison.

## 2. Fields to enter in the portal, not present in the files

| field | value |
|---|---|
| Corresponding author | Ibrahim Alraddadi |
| Email | `ialraddadi@iu.edu.sa` |
| Postal address | Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah 42351, Saudi Arabia |
| Telephone | `+966 50 650 8891` |
| ORCID | `0000-0002-0094-7937` |

The phone number is deliberately absent from the manuscript: Elsevier collects it as submission
metadata, and printing a personal number in the PDF is neither required nor desirable.

## 3. Verified state of this package

```
isolated build from this directory alone   exit 0
LaTeX errors                               0
undefined references / citations           0
BibTeX warnings                            0
placeholder text in the source             0
AIMS branding in source or PDF metadata    0
abstract                                   243 words   (CNSNS limit 250)
keywords                                   6           (CNSNS range 1-7)
highlights                                 5 bullets, max 84 chars
figures cited / supplied                   18 / 18
bibliography rendered / cited              27 / 27
pages                                      44
```

The build was tested by copying `manuscript/` and `figures/` into an empty directory and compiling
there, so nothing here depends on the development tree.

## 4. One item is NOT closed

The article and the cover letter both disclose the earlier Zenodo preprint,
DOI `10.5281/zenodo.21809908`. **That record's public creator list still shows a different sole
creator than this manuscript's byline.** The correction is prepared as an unpublished edit draft on
the record; it needs one action:

> open `https://zenodo.org/deposit/21809908` and press **Publish**
> (the creator field already shows Alraddadi with the ORCID; a metadata-only republish does not
> change the DOI)

Two consequences until that is done:

1. The cover letter's §3 contains a **bracketed sentence** asserting that the record's metadata has
   been corrected. **Delete the brackets and keep the sentence only after republishing.** Sending it
   beforehand would be a false statement to an editor.
2. Submitting while the public record and the byline disagree on authorship is the one remaining
   risk in this package — see `../R5_PREPRINT_DISCLOSURE.md` and
   `../FINAL_AUTHORSHIP_DECISION_REQUIRED.md`.

## 5. Also recheck at the moment of submission

The live CNSNS Guide for Authors and submission checklist should be re-read within 24 hours of
uploading (chief's condition 12). Everything in §3 was verified against the guide as of
2026-08-24.

## 6. Not part of this package

The reproducibility deposit is already published separately and is **not** uploaded to CNSNS:
DOI `10.5281/zenodo.22087770`, open access. The manuscript's data-availability statement cites it.
