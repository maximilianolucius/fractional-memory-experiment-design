# Author metadata — confirmation required before submission

**For: Ibrahim Alraddadi (corresponding author).**
**All metadata items are resolved.** Funding confirmed as *no external funding* and inserted; the
data deposit is published with a DOI and cited in the article. The only item still open is the
authorship question in §4, which is not a metadata field.

---

## 1. Resolved

| item | value | status |
|---|---|---|
| Name | Ibrahim Alraddadi | in the manuscript |
| Affiliation | Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah 42351, Saudi Arabia | in the manuscript title page |
| Email | `ialraddadi@iu.edu.sa` | in the manuscript, marked as corresponding |
| ORCID | `0000-0002-0094-7937` | **confirmed by the operator**; inserted on the title page as an author URL |
| Telephone | `+966 50 650 8891` | **supplied by the operator**; goes in the Editorial Manager submission form, **not** in the manuscript (Elsevier collects it as submission metadata, and printing a personal phone number in the PDF is neither required nor desirable) |

CNSNS's submission checklist asks for the corresponding author's full contact details — email,
full postal address and phone number. All three are now available. Enter the phone number in the
submission form; it is deliberately absent from the `.tex`.

## 2. Funding — **RESOLVED**

Confirmed by the operator: **no external funding.** Inserted in `main.tex` as

```latex
\section*{Funding}
This research received no external funding.
```

The original blocker text is kept below for the record.

### (original) BLOCKER — funding statement

Elsevier requires a funding declaration either way; silence is not an option, and the status must
not be inferred from other papers. **Exactly one** of the following goes into `main.tex`, and I
have inserted neither, because asserting an unverified funding status in a submitted record would
be a fabrication.

**Option 1 — no external funding**

```latex
\section*{Funding}
This research received no external funding.
```

**Option 2 — funded**

```latex
\section*{Funding}
This research was supported by [FUNDER] under grant [NUMBER].
```

Please state which applies, and for Option 2 the exact funder name and grant number as the funder
requires them to be cited.

## 3. Data deposit — **RESOLVED**

Published to Zenodo and cited in the article:

| | |
|---|---|
| DOI | **`10.5281/zenodo.22087770`** |
| Record | `https://zenodo.org/records/22087770` |
| Creator | Alraddadi, Ibrahim — ORCID `0000-0002-0094-7937` |
| Access | **open** |
| Licence | CC BY 4.0 |
| File | `fmed-reproducibility-2026-08-24.zip`, 303 461 bytes, md5 `877cfd04e5896824dd72a8ab57939648` |

Upload verified: Zenodo's checksum matches the local file byte for byte, the record resolves, and
the manifest inside the zip verifies 49/49. Access was set to **open** deliberately — Elsevier's
research-data Option C requires the data to be deposited *and accessible*, so a restricted record
would not have satisfied the data statement.

The article's statement now reads: *"The code and research data supporting the findings of this
study are openly available in Zenodo at https://doi.org/10.5281/zenodo.22087770."* No placeholder
text remains anywhere in the manuscript.

### (original) BLOCKER — data deposit identifier

The manuscript's data-availability statement currently reads:

> The code and research data supporting the findings of this study are available in
> [REPOSITORY], [DOI].

The deposit itself is built and verified: `public_reproducibility/`, 50 files, 2.8 MB, SHA256
manifest checked, and the package regenerates the headline figure from a clean copy. It needs to be
uploaded to Zenodo and the resulting DOI substituted for the two placeholders. **The final
submission package must contain no placeholder text**, so this is a hard blocker.

## 4. Authorship — a factual matter the operator must decide

This is not a metadata field; it is a discrepancy that a CNSNS editor can find in one search, so it
is raised here rather than buried.

A **public preprint of this same work already exists**:

| | |
|---|---|
| DOI | `10.5281/zenodo.21809908` |
| Title | *Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator-Prey Model* |
| Creator | **Lucius, Maximiliano** — sole creator, no other author listed |
| Date | 5 August 2026 |
| Licence | CC BY 4.0 |
| Type | Preprint (manuscript + source code + benchmark results) |

Two consequences:

1. **The title is nearly identical to the submitted manuscript and the content is an earlier version
   of it.** Elsevier's policy permits preprints, but requires that the preprint be disclosed at
   submission and cited in the article. That disclosure is currently missing from the manuscript.
2. **The preprint's sole creator is not the submitting author.** A public record showing different
   authorship for substantially the same work is exactly the pattern that triggers an authorship
   query, and it is trivially discoverable.

The instruction received was to remove Maximiliano Lucius as an author. That has been done in the
manuscript and its bibliography (see `R5_REFERENCE_AUDIT.md`), but **removing a name from the
submitted files does not change the public Zenodo record.** One of the following has to happen
before submission:

- **(a)** update the Zenodo record's creator list so it matches the manuscript's authorship, and
  disclose the preprint in the article ("An earlier version of this work was posted as a preprint,
  DOI …"); or
- **(b)** keep the record as it stands and state the relationship explicitly in the cover letter and
  the article, explaining the authorship change; or
- **(c)** withdraw or restrict the Zenodo record if it was posted in error.

I cannot choose among these — it is a question of fact about who did the work and who is entitled to
authorship, and only you and the author can answer it. What I can say plainly is that submitting
without resolving it carries a real risk of an authorship investigation, which would be far more
damaging than the desk rejection this rescue was built to overcome.

Note that this is independent of where future deposits live: keeping the Zenodo *account* under
Maximiliano's login is a purely administrative matter and raises no issue, as long as the **creator
metadata of the record** matches the paper's authorship.

## 5. Checklist for the operator

- [x] Funding: **no external funding**, inserted
- [x] Upload `public_reproducibility/` to Zenodo, obtain the DOI — **`10.5281/zenodo.22087770`**
- [x] Phone number supplied for the submission form
- [x] Postal address confirmed (Madinah 42351)
- [ ] **Decide (a) / (b) / (c) on the existing preprint record and its creator list** — still open;
      an "ok" does not select among the three, and the three lead to different text in the article
      and the cover letter
