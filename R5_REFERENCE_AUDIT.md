# R5-H — Reference and DOI audit

**Status: DONE. Bibliography reduced to what the paper cites, all citations resolve, DOI coverage
26/30, two arXiv references verified against the live records.**

---

## 1. Reconciliation

| quantity | count |
|---|---:|
| entries in `bibliography.bib` before | 79 |
| entries after | **30** |
| entries parked in `bibliography_unused.bib` | 47 |
| `\bibitem`s rendered in the PDF | **26** |
| cited by the main manuscript | **26** |
| cited only by `sec14`/`sec15` (orphan supplement sources, not in this build) | 4 — `K01`, `K02`, `S01`, `S02` |
| cited but unresolved | **0** |
| in the PDF without a bibliography entry | **0** |

The 47 uncited entries were **not deleted**. They are preserved in `bibliography_unused.bib` with a
header explaining what they are, so nothing is lost if a section that cites them returns. That file
is excluded from the submission package.

The four entries cited only by the orphan supplement sources are kept in `bibliography.bib`
deliberately: if `sec14`/`sec15` are later submitted as supplementary material they will need them,
and BibTeX ignores uncited entries, so their presence costs nothing in the compiled article.

## 2. DOI coverage

**26 of 30 entries carry a DOI (87%).** The four without one, and why:

| key | reference | why no DOI |
|---|---|---|
| `F02` | Podlubny, *Fractional Differential Equations*, Academic Press, 1999 | 1999 Academic Press monograph; no DOI issued. ISBN `978-0-12-558840-9` supplied. |
| `F04` | Kilbas, Srivastava & Trujillo, *Theory and Applications of Fractional Differential Equations*, Elsevier, 2006 | North-Holland Mathematics Studies vol. 204; no volume DOI. ISBN `978-0-444-51832-3` supplied. |
| `F05` | Matignon, *Stability Results for Fractional Differential Equations…*, CESA 1996 | 1996 conference proceedings, pre-DOI. Volume, pages and venue supplied. |
| `P01` | companion manuscript | unpublished; no identifier yet. |

DOIs added this round: `10.48550/arXiv.2607.16895` and `10.48550/arXiv.2606.19590` (see §3), plus
the corrected chapter-level DOI for `E08` (`10.1007/978-981-16-0626-7_9`, was the book-level DOI).

## 3. Two references verified against live records

`SAFE26A` and `SAFE26B` were `@misc` arXiv entries with no DOI, dated 2026. A 2026 arXiv identifier
in a bibliography is exactly the kind of entry that turns out not to exist, so both were checked
against arXiv directly:

| key | claimed | live record | verdict |
|---|---|---|---|
| `SAFE26A` | Saligrama, *When Can Safe Controllers Adapt? Information before Commitment*, arXiv:2607.16895 | title and sole author match; submitted 18 July 2026 | **verified** |
| `SAFE26B` | Ni, Ornik, Chou & Coogan, *Safe, Real-Time Active Model Discrimination and Fault Diagnosis for Nonlinear Systems via Differentiable Reachability*, arXiv:2606.19590 (cs.RO) | title and all four authors match; submitted 17 June 2026 | **verified** |

Both are cited in the introduction for the general safety-constrained-information literature, where
the manuscript explicitly disclaims novelty for safe experimental design as such. The attribution is
correct and the records exist.

## 4. Prior-art attribution survived the migration

The chief required that the withdrawn novelty wording must not reappear during template conversion.
Re-checked after migration:

| check | count |
|---|---:|
| `K07` (McLean 2018) cited | 3 places — attribution block in `sec3`, contribution disclaimer in `sec1`, theorem index in `sec14` |
| `K08` (Trefethen–Weideman) cited | in the attribution block and inside the lemma's proof |
| `K09` (Stahl) cited | optimality context in `sec3` |
| `K03`, `K04` (Beylkin–Monzón), `K05` (Jiang et al.) | cited in the attribution block |
| "new exponential-sum" / "novel approximation" / "new root-exponential" | **0** |
| `thm:T9b` anywhere | **0** |
| FCAA / standalone-paper language in `paper/` | **0** |

## 5. Authorship change to `P01`

Per instruction, Maximiliano Lucius is removed as an author from the submission source.

| entry | before | after |
|---|---|---|
| `P01` (cited 9×) | `author = {Lucius, Maximiliano}`, with a note claiming the work was "published as Zenodo preprint DOI 10.5281/zenodo.21809908 (companion project fractional-memory-identifiability)" | `author = {Alraddadi, Ibrahim}`, note reduced to "Companion manuscript; validated-numerics certification of the shared ecological backbone" |
| `P02`, `P03` | `author = {Lucius, Maximiliano}`, cited **0** times | **entries removed** |

`grep -i lucius` over `bibliography.bib`, `main.tex` and `sections/*.tex` returns nothing.

**Two things about this change that need stating.**

First, the old `P01` note was **factually wrong** and its correction is independent of the
authorship instruction: DOI `10.5281/zenodo.21809908` is not the companion study. It is a public
preprint of *this* manuscript — title *"Safe Active Discrimination of Fractional, Delayed, and
Finite Latent Memory in a Strong-Allee Predator-Prey Model"*, deposited 5 August 2026, CC BY 4.0.
Citing it as a different paper would have been an incorrect reference regardless of whose name was
on it.

Second, and this is the part I cannot resolve: **that public record lists Lucius, Maximiliano as its
sole creator.** Removing the name from the submitted `.tex` does not change the record. Elsevier
permits preprints but requires them to be disclosed and cited at submission, and a public preprint
of substantially this work under different authorship is discoverable in one search of the title.
Attributing `P01` to Alraddadi is the only attribution consistent with the manuscript, but it is an
assumption I made to carry out the instruction, not a fact I verified — so it is listed for author
confirmation alongside the funding statement in `AUTHOR_METADATA_CONFIRMATION.md` §4, with the three
resolution options.

## 6. Build after all reference changes

Clean-directory build: exit 0, 0 LaTeX errors, 0 undefined references, 0 undefined citations,
**0 BibTeX warnings**, 26 rendered references.
