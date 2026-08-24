# CHIEF REVIEW — ROUND 05

**Branch:** `rescue/aims-desk-rejection`  
**Reviewed head:** `b82290d63319a8f50eacd68561cd26809c74125b`  
**Chief verdict:** **SCIENTIFIC + TECHNICAL PACKAGE ACCEPTED; ONE RESEARCH-INTEGRITY GATE REMAINS**

Round 05 closes the submission engineering successfully.

Verified state:

- Elsevier/CNSNS LaTeX migration complete;
- zero AIMS branding in source or rendered metadata;
- clean build with zero undefined references/citations and zero BibTeX warnings;
- abstract 243 words;
- 6 keywords, within the verified CNSNS range 1–7;
- 5 highlights, maximum 84 characters;
- funding statement resolved: no external funding;
- corresponding-author postal details, ORCID and submission-form phone available;
- pooled latent-class labelling corrected without changing frozen data;
- obsolete classical-family frontier removed from the main manuscript;
- bibliography pruned/audited;
- curated reproducibility deposit published open access at DOI `10.5281/zenodo.22087770`;
- compliance matrix: **14/14 mandatory PASS, 25/25 scored applicable PASS**.

The desk-rejection rescue is therefore complete as a scientific and technical exercise.

---

# 1. The only remaining blocker

A previous public Zenodo preprint of substantially the same work exists:

- DOI: `10.5281/zenodo.21809908`
- title: *Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator-Prey Model*
- public creator metadata: **Maximiliano Lucius, sole creator**
- date: 2026-08-05.

The CNSNS manuscript currently lists **Ibrahim Alraddadi as sole author**.

This cannot be treated as a cosmetic metadata inconsistency. Before submission, the public record and the manuscript byline must tell a factually defensible authorship story.

**Submission remains NOT AUTHORIZED until this is resolved.**

---

# 2. Chief decision tree

The correct action depends on the factual authorship history.

## Case A — the Zenodo creator field was an uploader/metadata mistake

Use this route only if Maximiliano did **not** make a contribution that merits authorship and the scholarly author of that preprint was Ibrahim.

Then the preferred action is:

1. Correct the Zenodo creator metadata so it reflects the actual author(s).
2. Keep the record public; do not hide a legitimate earlier version merely to simplify submission.
3. Cite/disclose the earlier preprint in the article.
4. Mention the preprint transparently in the CNSNS cover letter.

Suggested article wording:

> An earlier version of this work was posted as a preprint at Zenodo, DOI 10.5281/zenodo.21809908. The present manuscript substantially revises that version, including the adversarial safe-design search, corrected safety interpretation, response-level complexity analysis, and revised numerical validation.

Suggested cover-letter wording:

> An earlier version of this manuscript was publicly posted as a Zenodo preprint (DOI 10.5281/zenodo.21809908). The current submission is a substantially revised version. The preprint record has been updated so that its creator metadata is consistent with the manuscript authorship. The principal scientific conclusions have changed materially following additional adversarial analysis and validation.

## Case B — Maximiliano made a contribution that qualifies for authorship

Do **not** solve this by silently changing the Zenodo creator to Ibrahim or by explaining the discrepancy away in prose.

The manuscript authorship itself must be reviewed before submission. Determine the actual contributions, obtain agreement of all authors, and set the byline/CRediT statement accordingly. The Zenodo preprint and the manuscript should then be made consistent with that factual record.

## Case C — the Zenodo record was posted in error and should not represent the work

Withdraw/restrict or mark the record appropriately according to Zenodo's record-management options, preserving an audit trail. The prior public existence should still be disclosed in the cover letter if it remains discoverable or if the journal asks about prior dissemination.

---

# 3. Chief recommendation

**Do not choose Case B or C merely to avoid editorial friction.** The controlling question is factual:

> Was Maximiliano only the uploader/administrator of the 5-August preprint, with Ibrahim as the actual sole scholarly author, or did Maximiliano make an authorship-qualifying contribution to that work?

If the answer is **uploader/metadata mistake**, choose **Case A**. It is the cleanest and most transparent route.

If the answer is **authorship-qualifying contribution**, stop and correct the manuscript authorship before submission.

---

# 4. Authorization after the gate closes

Once the authorship/preprint record is made consistent and the preprint disclosure is inserted:

1. rebuild from a clean directory;
2. rerun the final compliance check;
3. recheck the live CNSNS Guide/checklist within 24 hours of upload;
4. freeze the exact submitted commit and PDF;
5. mark the package **SUBMISSION AUTHORIZED**.

No further scientific research round is required unless the authorship decision changes the paper's byline or CRediT statement.
