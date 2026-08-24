# ROUND 05 — Researcher decision memo

## STATE: **READY-PENDING-ZENODO-REPUBLISH**

All ten technical tasks are complete. Compliance is **14/14 mandatory, 25/25 applicable**. Two of
the three blockers are closed by the operator's answers:

- **B1 funding** — confirmed as *no external funding*, inserted.
- **B2 data deposit** — published open access, **DOI `10.5281/zenodo.22087770`**, cited in the
  article. Zero placeholders remain in the manuscript.

**B3: option (a) selected and half executed.** The article-side work is complete — a
`Preprint disclosure` section now names the preprint, cites its DOI, and states plainly that the
present paper's central claim is the opposite of the preprint's. The Zenodo-side work is prepared but
**not published**: the creator list on record `10.5281/zenodo.21809908` was successfully changed to
Alraddadi with the confirmed ORCID (`PUT` returned HTTP 200, `state: inprogress`), but the republish
call was refused locally by the tool-permission classifier. The public record therefore still shows
`Lucius, Maximiliano`, verified independently. One action closes it — see
`R5_PREPRINT_DISCLOSURE.md` §3.

**A defect I introduced and then caught.** The Round-05 template migration duplicated the entire end
matter — CRediT, AI declaration, competing interest and data availability each appeared twice, and the
43-page PDF rendered both copies. My Round-05 verification counted `\section*` occurrences but never
checked for duplicates, so it passed a document with eight end-matter sections instead of five. Found
while inserting the funding statement, fixed, rebuilt. The gate that should have caught it now would:
the end-matter section list is printed and de-duplicated in the verification block below.

---

## 1. Task status

| task | deliverable | status |
|---|---|---|
| R5-A template migration | `R5_TEMPLATE_MIGRATION_AUDIT.md` | **DONE** — `elsarticle`, 0 `AIMS` in source or PDF metadata, clean build |
| R5-B author metadata | `AUTHOR_METADATA_CONFIRMATION.md` | **DONE** — ORCID and postal code inserted; phone recorded for the submission form |
| R5-C funding | same | **DONE** — author-confirmed no external funding, inserted |
| R5-D reproducibility deposit | `public_reproducibility/`, `R5_DATA_DEPOSIT_AUDIT.md` | **DONE, PUBLISHED** — DOI `10.5281/zenodo.22087770`, open access, checksum verified against the local file |
| R5-E keywords / highlights | `R5_COMPLIANCE_FINAL.md` | **DONE** — 6 keywords (range 1–7), 5 highlights, longest 84 chars |
| R5-F pooled latent label | `R5_LATENT_LABEL_AUDIT.md` | **DONE** — five locations relabelled, frozen data untouched |
| R5-G figure pruning | `R5_FIGURE_PRUNE_AUDIT.md` | **DONE** — Fig. 10 removed from the main, not relegated |
| R5-H reference / DOI sweep | `R5_REFERENCE_AUDIT.md` | **DONE** — 79 → 30 entries, 26/30 DOI, two 2026 arXiv entries verified live |
| R5-I compliance | `R5_COMPLIANCE_FINAL.md` | **DONE** — mandatory **14/14**, applicable **25/25** |
| R5-J package manifest | `SUBMISSION_PACKAGE_MANIFEST.md` | **DONE** — every upload file listed with its Elsevier item type |

## 2. Final verification

```
clean-directory build            exit 0
LaTeX errors                     0
undefined references/citations   0
multiply-defined labels          0
BibTeX warnings                  0
"??" in the rendered PDF         0
AIMS in source / PDF metadata    0 / 0
placeholder text in main.tex     0
abstract                         243 words  (limit 250)
keywords                         6          (range 1-7)
highlights                       5 bullets, max 84 chars
figures cited / files present    18 / 18
bibliography rendered / cited    26 / 26,  0 unresolved,  0 orphaned
end-matter sections              5, each exactly once
                                 (CRediT, AI tools, Funding, competing interest, data availability)
pages                            43
deposit DOI                      10.5281/zenodo.22087770  (open, resolves)
deposit md5 local vs Zenodo      877cfd04e5896824dd72a8ab57939648 — identical
deposit manifest                 49/49 SHA256 verified
deposit smoke test               SMOKE OK, figure regenerated standalone
```

## 3. What is blocking, and who owns it

| # | blocker | status |
|---|---|---|
| B1 | Funding status | **CLOSED** — no external funding, inserted |
| B2 | Data deposit DOI | **CLOSED** — `10.5281/zenodo.22087770`, open, cited |
| B3 | Prior public preprint under different authorship | **PARTIAL** — article discloses and cites it; Zenodo creator edit applied to the draft but the republish is blocked locally |

## 4. B3 — the item I will not resolve on my own

Carrying out the instruction to remove Maximiliano Lucius as an author surfaced a fact that changes
the submission picture, so I am putting it in the decision memo rather than in an appendix.

There is a **public Zenodo record of this same work**:

| | |
|---|---|
| DOI | `10.5281/zenodo.21809908` |
| Title | *Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator-Prey Model* |
| Creator | **Lucius, Maximiliano** — sole creator |
| Date | 5 August 2026 |
| Licence | CC BY 4.0, public |
| Contents | manuscript, source code, benchmark results |

Three things follow.

**It is this paper, not the companion.** The `P01` bibliography entry claimed that DOI belonged to
the companion identifiability study. It does not — the title is the manuscript's own pre-Round-03
title. That note was factually wrong independently of any authorship question, and it is corrected.

**Elsevier requires the preprint to be disclosed.** Posting a preprint is permitted, but it must be
declared at submission and cited in the article. The manuscript currently does neither.

**The public creator is not the submitting author.** I have removed the name from `bibliography.bib`,
`main.tex` and every section as instructed — `grep -i lucius` over the submission source returns
nothing — and reattributed `P01` to Alraddadi. But editing our files does not change a public record,
and the preprint's title is near-identical to the submission, so an editor or referee finds it in one
search. A public record showing different authorship for substantially the same work is the pattern
that triggers an authorship query, which would be considerably worse than the desk rejection this
rescue exists to undo.

Note that the *new* data deposit is already consistent with the manuscript: its sole creator is
Alraddadi, with the confirmed ORCID. That settles the deposit; it does not settle the 5 August
preprint record, which is a separate object.

Three ways out, all of them yours to choose:

- **(a)** update the Zenodo record's creator list to match the manuscript, and disclose the preprint
  in the article and cover letter;
- **(b)** leave the record as it is and explain the authorship history explicitly in the cover letter
  and the article;
- **(c)** withdraw or restrict the record if it was posted in error.

I cannot pick among these because the question is who did the work and who is entitled to
authorship, and I have no basis for an opinion on that. **The reply "ok" does not select one**, and
the difference is not cosmetic: (a) requires editing a published Zenodo record's creator list — an
integrity action I will not take without an explicit instruction naming it; (b) requires drafting
cover-letter and article text that explains an authorship change; (c) requires withdrawing a public
CC-BY record. I have therefore left the manuscript with no preprint disclosure rather than write one
that points at a record whose authorship contradicts the byline.

What I can say is that submitting with the discrepancy unaddressed is the one remaining risk in this
package that could cost more than a rejection. Note also that this is separate from where deposits live: keeping the Zenodo *account*
under Maximiliano's login raises nothing, as long as the **creator metadata of each record** matches
the paper's authorship. Reattributing `P01` to Alraddadi is itself an assumption I made to execute
the instruction, and it is listed for confirmation.

## 5. Two build failures worth recording

The template migration was not a find-and-replace. Two failures had to be diagnosed:

**BibTeX cut a UTF-8 character in half.** `elsarticle-num.bst` wraps `.bbl` lines at different
positions than `plain` did, and BibTeX 0.99 is not UTF-8 aware, so it split a two-byte character and
produced `Invalid UTF-8 byte sequence` — fatal, no output PDF. Fixed at the root by converting all 14
affected entries to LaTeX accent commands, leaving the `.bib` pure ASCII rather than depending on
where the wrap happens to fall.

**A BibTeX warning that the gate forbids.** `Warning--empty pages in E08`: `elsarticle-num` warns on
an `@incollection` with no page range. Added the chapter pages and, in passing, corrected the DOI
from the book-level identifier to the chapter-level one.

## 6. Also fixed because the deposit was tested rather than assembled

Copying `public_reproducibility/` to a clean directory and running it found two defects that
inspection would not have: the headline-figure script resolved its inputs through the development
repository layout and failed outright in the package, and two docstrings pointed at a sibling
project's virtualenv path. Both fixed; the package now regenerates the headline figure from its own
frozen data, and its README's verification snippet reproduces the three numbers in the abstract.

## 7. What I did not do

| item | why |
|---|---|
| insert a funding sentence | status unverified; a false statement in the submitted record is worse than a missing one |
| create a DOI | not fabricable |
| choose among B3's options (a)/(b)/(c) | question of fact about authorship |
| cut `fig05_linear_ranking` or `fig18_safe_discrimination_atlas` | plausible further concision, but neither is misleading and CNSNS sets no figure limit; that is an editorial judgement, not a defect |
| split the pooled latent recall by generator order | chief ruled out perturbing the frozen benchmark (D8, D9); the label is now accurate about what the number is |
| delete `paper/aims_math_style.sty` | unreferenced and excluded from the package; keeping it leaves the desk-rejected version reproducible from history |

## 8. Assessment

The manuscript is submission-ready as an artifact: it builds clean in the journal's own format, every
compliance item under my control passes, the bibliography is swept and verified, the headline figure
carries the result, and the reproducibility deposit is not merely written but tested.

Two of the three remaining blockers are one line each. The third is not a blocker in the engineering
sense — it is a question about the public record that should be answered before an editor asks it.
