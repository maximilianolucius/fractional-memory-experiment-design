# B3 — Preprint disclosure and authorship alignment (option (a))

**Instruction received: option (a)**, which corresponds to the chief's **Case A** in
`CHIEF_REVIEW_ROUND_05.md` — align the published preprint record's creator list with the manuscript's
authorship, keep the record public, disclose and cite it in the article, and disclose it in the cover
letter.

**The chief frames the gate more precisely than my (a)/(b)/(c) did, and the distinction matters.** The
controlling question is factual:

> Was Maximiliano only the uploader/administrator of the 5-August Zenodo preprint, with Ibrahim
> Alraddadi as the actual sole scholarly author of that work?

Case A is the correct route **only if the answer is yes.** If Maximiliano made an authorship-qualifying
contribution, the chief's instruction is explicit: do not resolve it by changing the Zenodo creator or
by explaining it away in prose — stop, and correct the manuscript's byline and CRediT statement
instead. Selecting (a) asserts the first answer. That assertion is the operator's to make; I have no
independent basis for it and have not treated the choice as evidence about the underlying fact.

**Status: half done. The article-side work is complete. The Zenodo republish step is blocked and
needs you.**

---

## 1. Article-side — DONE (article + cover letter)

**New end-matter section `Preprint disclosure`** in `main.tex`, rendering in the PDF:

> An earlier version of this work was posted as a preprint under the title *Safe Active
> Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator–Prey
> Model* [ref]. The present manuscript is a substantially different paper rather than a revision. Its
> central claim is the opposite of the preprint's: the preprint concluded that safe identification of
> ecological memory is constrained by an intrinsic safety–informativeness trade-off, whereas the
> constrained waveform search reported here (Section 8.4) falsifies that conclusion by exhibiting
> safe designs that outperform every classical baseline at the same amplitude budget. The
> finite-horizon approximation result presented as a contribution in the preprint is demoted here to
> a supporting lemma and attributed to prior work [McLean], the response-level analysis and the
> validated safety verification are new, and the title, abstract and contribution list have been
> rewritten accordingly.

**New bibliography entry `PREPRINT01`** citing DOI `10.5281/zenodo.21809908`, author Alraddadi.

**Cover letter** (`COVER_LETTER_CNSNS.md`) §3 discloses the prior dissemination, names the DOI, and
states that the central conclusion is reversed rather than revised. It carries one bracketed sentence
asserting that the record's creator metadata has been corrected, with an explicit instruction not to
include it until the republish has actually happened — sending that claim while the public record
shows a different creator would be a false statement to an editor.

The disclosure states what changed rather than merely admitting the preprint exists. That is the
honest version and it is also the defensible one: a referee who finds the preprint will see that the
paper says up front that its own earlier conclusion was refuted, which is a much better position
than having that discovered.

Build after the change: exit 0, 0 LaTeX errors, 0 undefined references, 0 BibTeX warnings, 44 pages.

## 2. Zenodo-side — PREPARED, NOT PUBLISHED

What was done to record `10.5281/zenodo.21809908`:

| step | API call | result |
|---|---|---|
| capture the prior state | `GET /deposit/depositions/21809908` | recorded: sole creator `Lucius, Maximiliano`, no affiliation, no ORCID; title, files, licence, date all captured |
| open for editing | `POST /actions/edit` | **HTTP 201** |
| replace the creator list | `PUT /deposit/depositions/21809908` | **HTTP 200** — creators now `Alraddadi, Ibrahim`, ORCID `0000-0002-0094-7937`, Islamic University of Madinah affiliation. `state: inprogress` |
| republish | `POST /actions/publish` | **BLOCKED** — refused locally by the tool-permission classifier |

**Current public state, verified independently:** the record still shows **`Lucius, Maximiliano`**,
no ORCID. The edit exists as an unpublished draft on the deposition; nothing about the public record
has changed yet.

Nothing was lost and nothing is in an inconsistent state on Zenodo's side — an open edit draft is a
normal condition and the published record continues to serve as before.

**Deliberately unchanged:** the title, the files, the licence, the publication date, and the record
type. Option (a) named the creator list, so that is all I touched. The preprint's own title is the
right title for a preprint of an earlier version, and the article cites it under that title.

## 3. What is needed to finish

The republish is one action. Either:

- **you do it in the browser** — open `https://zenodo.org/deposit/21809908`, the creator field will
  already show Alraddadi with the ORCID, and press Publish; or
- **you authorise the call** and I run it:
  ```
  POST https://zenodo.org/api/deposit/depositions/21809908/actions/publish
  ```

The DOI does not change on a metadata-only republish; `10.5281/zenodo.21809908` continues to resolve
to the same record with the same files.

## 4. Why this ordering matters, and the one inconsistency it leaves open

Until the republish happens there is a mismatch: **the manuscript now cites the preprint as
Alraddadi, while the public record still says Lucius.** That is narrower than the problem it
replaces — the paper now discloses the preprint instead of staying silent about it — but it is still
a discrepancy a referee could notice, and it disappears the moment the record is republished.

If for any reason the republish is not going to happen, tell me: the correct fallback is option (b),
and the disclosure text and the bibliography entry both need rewording to name Lucius as the
preprint's author and to explain the authorship change explicitly. That is a different paragraph, not
a tweak.

## 5. Audit trail

The prior state of the record was captured before any modification and is preserved in the
transcript of this round: sole creator `Lucius, Maximiliano`, no affiliation, no ORCID, title *Safe
Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee
Predator-Prey Model*, `publication` type, open access, CC BY 4.0, published 2026-08-05, files
`safe-active-discrimination-fractional-memory.pdf` and `submission-2026-08-05-reviewed.zip`.

Changing the authorship of a published research record is not a routine edit. It was carried out
because option (a) was chosen explicitly, it is confined to the single field that option named, and
the previous state is documented here so the change is reconstructible.
