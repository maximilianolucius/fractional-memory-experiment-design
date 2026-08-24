# R4-G — Format and end matter

**Status: PARTIAL. End matter added and building; template conversion deliberately deferred;
two metadata items cannot be closed by me.**

---

## 1. End matter as it now stands

| section | before | after |
|---|---|---|
| Author contributions | prose paragraph | **`CRediT authorship contribution statement`** using CRediT taxonomy terms (Conceptualization, Methodology, Formal analysis, Software, Investigation, Validation, Data curation, Visualization, Writing – original draft, Writing – review & editing) |
| Conflict of interest | "The author declares no conflict of interest." | **`Declaration of competing interest`** with Elsevier's standard formulation ("no known competing financial interests or personal relationships that could have appeared to influence the work") |
| Use of AI tools | present | kept, unchanged. It is explicit about language editing, LaTeX formatting, code and documentation assistance, and that responsibility for the content remains with the author. **Do not remove it** — Elsevier requires the declaration, and a vaguer version would be worse than the current one. |
| Data availability | absent | **added** (see §2 for the decision behind the wording) |
| Highlights | absent | **`paper/highlights.txt`** created: 5 bullets, longest 84 characters, filename contains "highlights" as required |
| Funding | absent | **still absent** — see §3 |
| Acknowledgements | absent | none added; the "immediately before references" ordering rule therefore does not bind |

Order in `main.tex`: CRediT → AI declaration → competing interest → data availability →
bibliography. If an acknowledgements section is added later it must go immediately before the
bibliography.

## 2. Data availability — a decision I am flagging, not taking

The statement now reads:

> The source code implementing the solvers, the waveform search, the four-class discrimination
> benchmark and the trajectory verification, together with the numerical artifacts from which every
> table and figure in this paper is generated, are available from the author on request.

"On request" is accepted by Elsevier, but a concrete deposit is stronger and reviewers increasingly
expect one. **I did not point the statement at the existing public repository, and this is
deliberate.** That repository
(`github.com/maximilianolucius/fractional-memory-experiment-design`, and the Zenodo deposit
`10.5281/zenodo.21809908`) currently contains the entire rescue record: the desk-rejection recovery
plan, every chief review, the round-by-round decision memos, and the audits in which we falsify our
own earlier claims. Putting that URL in the paper hands a referee the full internal history,
including the previous rejection.

That may be exactly what the chief wants — it is unusually transparent and everything in it is
honest work. But it is a disclosure decision with real consequences and it is not mine to make.

**Recommended resolution:** publish a *curated* deposit containing only `benchmark/`,
`rescue_compute/`, the frozen artifacts listed in `R4_REPRODUCIBILITY_FREEZE.md`, and a README —
without the rescue documents — mint a DOI for it, and point the statement there. That is roughly an
hour of work once the chief authorises which files go in.

## 3. What I could not close, and did not invent

| item | why it is open |
|---|---|
| **Funding disclosure** | I do not know whether the work was funded. Elsevier requires the statement either way; the standard no-funding sentence is *"This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."* I have **not** inserted it, because asserting a funding status I cannot verify would be a fabrication in the submitted record. |
| **Corresponding-author postal address and ORCID** | Not in my possession. The manuscript carries name, department, faculty, institution, city, country and email. Elsevier's checklist asks for full contact details. |
| **Keyword count** | 6 keywords are supplied. The permitted maximum at CNSNS could not be read (ScienceDirect 403). Almost certainly compliant; not verified. |

These three are the entire remaining gap on gate R4.7 together with the data statement, and none
of them is scientific.

## 4. Template conversion: deferred, with reasoning

The manuscript still uses `aims_math_style.sty`, a house style written for the previous AIMS
submission. It builds cleanly and produces a conventional single-column article.

**Per the chief's explicit correction, `elsarticle` is recorded as recommended, not mandatory:**
what the live guide requires is editable source, and it offers Word and LaTeX templates rather than
imposing a class as an acceptance criterion. Converting now would mean re-flowing 25 pages, 19
figures and 8 tables while the content is still under chief review, with a real chance of
introducing the kind of LaTeX breakage this project has already lost time to. The conversion is
mechanical and is best done once §2 and §3 are resolved and the content is frozen.

**Concretely, what conversion involves:** replace the `\AIMS*` front-matter macros with
`elsarticle`'s `\title`/`\author`/`\address`/`\begin{abstract}`/`\begin{keyword}`, switch
`\documentclass` to `elsarticle` with the `[preprint,3p]` or `[review,12pt]` option, and drop
`aims_math_style.sty`. The section bodies, figures, tables and bibliography need no edits;
`natbib` numbered citations are already what CNSNS uses.

## 5. Reference hygiene

| check | result |
|---|---|
| undefined citations | **0** |
| undefined references | **0** |
| multiply-defined labels | **0** |
| every `\includegraphics` target exists | **19/19** verified against `paper/figures/` |
| DOIs on new entries | `K07`, `K08`, `K09` all carry DOIs |
| DOIs on pre-existing entries | **not swept** — a full DOI sweep of the other 73 entries is outstanding and is a genuine (if minor) compliance item |
| unused bibliography entries | **not pruned** — `bibtex` emits no warnings, so nothing is *broken*, but the `.bib` carries entries beyond those cited |

## 6. Build

Clean directory build: `bash paper/build_latex.sh` → exit 0. 25 pages. Zero LaTeX errors, zero
undefined references or citations.
