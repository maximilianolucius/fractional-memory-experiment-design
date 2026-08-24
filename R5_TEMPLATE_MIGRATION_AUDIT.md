# R5-A — Template migration audit

**Status: DONE. AIMS branding removed, `elsarticle` in place, clean build.**

---

## 1. What was replaced

| before | after |
|---|---|
| `\documentclass[10pt]{article}` + `\usepackage{aims_math_style}` | `\documentclass[preprint,12pt]{elsarticle}` |
| `\AIMSJournalHeader`, `\AIMSResearchArticle` | removed (the class handles the preprint header) |
| `\AIMSTitle{...}` | `\title{...}` inside `\begin{frontmatter}` |
| `\AIMSAuthors{Ibrahim Alraddadi$^{1,*}$}` | `\author[iu]{Ibrahim Alraddadi\corref{cor1}}` + `\cortext[cor1]{Corresponding author.}` |
| `\AIMSAffiliation{...}` | `\address[iu]{...}` with the postal code added |
| `\AIMSCorrespondence{Email: ...}` | `\ead{ialraddadi@iu.edu.sa}` + `\ead[url]{https://orcid.org/0000-0002-0094-7937}` |
| `\begin{AIMSAbstract}` | `\begin{abstract}` |
| `\AIMSKeywords{a; b; c}` | `\begin{keyword} a \sep b \sep c \end{keyword}` |
| `\AIMSMSC{...}` | `\MSC[2020] 34A08 \sep 34K20 \sep 62K05 \sep 92D25` |
| `\bibliographystyle{plain}` | `\bibliographystyle{elsarticle-num}` |
| — | `\journal{Communications in Nonlinear Science and Numerical Simulation}` added |

`aims_math_style.sty` is no longer loaded. It remains in the repository but is not part of the
submission source; the pre-migration `main.tex` is preserved at
`paper/backup_preR3/main_preR5_aims.tex`.

Preserved unchanged: title, all section content, theorem environments and numbering
(`\numberwithin{equation}{section}`, `theorem`/`lemma`/`corollary` shared counter), every
cross-reference, the 243-word abstract, the 6 keywords, numbered square-bracket citations, and
figure/table placement.

## 2. Hard checks

| check | result |
|---|---:|
| `AIMS` in `main.tex` | **0** |
| `AIMS` in `sections/*.tex` | **0** |
| `aims_math_style` anywhere in the submission source | **0** |
| `AIMS` in PDF metadata | **0** |
| `aims` in rendered PDF text | 2 — both inside the word "cl**aims**"; no branding |
| LaTeX errors | **0** |
| undefined references / citations | **0** |
| BibTeX warnings | **0** |
| abstract after conversion | **243 words** (limit 250) |
| pages | 44 (`preprint,12pt` is single-column double-spaced; the journal-format page count is far lower) |

## 3. Two build failures fixed on the way

**(a) BibTeX splitting UTF-8 characters.** `elsarticle-num.bst` line-wraps the `.bbl`, and BibTeX
0.99 is not UTF-8 aware, so it cut a two-byte character in half and produced
`! LaTeX Error: Invalid UTF-8 byte sequence` — a fatal error with no output PDF. This did not appear
under the previous `plain` style because the wrap points differed.

Fixed by converting all 14 affected bibliography entries from literal accented characters to LaTeX
accent commands (`ö` → `{\"o}`, `é` → `{\'e}`, `š` → `{\v{s}}`, and so on), leaving the `.bib`
pure ASCII. This is the standard remedy and it removes the failure mode permanently rather than
papering over one wrap position. `\usepackage[utf8]{inputenc}` was also restored.

**(b) `Warning--empty pages in E08`.** The chief's gate requires zero BibTeX warnings.
`elsarticle-num` warns on an `@incollection` with no `pages`. Added the chapter page range
`211--232`, the series name, the publisher address, and corrected the DOI from the book-level
`10.1007/978-981-16-0626-7` to the chapter-level `10.1007/978-981-16-0626-7_9`.

## 4. Class-option choice

`[preprint,12pt]` is Elsevier's recommended option for a manuscript under review: single column,
generous leading, line-numbering-friendly. The alternatives (`final,5p` two-column journal layout)
are for accepted papers and would make the review copy harder to annotate. If the editor asks for a
different layout, the change is a single option in `\documentclass`.

## 5. Residual

`aims_math_style.sty` is still present in `paper/`. It is not referenced by the submission source
and is excluded from `SUBMISSION_PACKAGE_MANIFEST.md`. I left the file in the repository rather
than deleting it, so the AIMS version remains reproducible from history if anyone needs to compare
against the desk-rejected submission.
