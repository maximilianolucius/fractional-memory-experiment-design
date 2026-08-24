# CNSNS submission package — file manifest

Every file to upload, and what it is for. Nothing else from this repository goes to the journal.

**Submission portal:** Editorial Manager. **Review model:** single anonymized.
**State:** `READY-PENDING-PREPRINT-DISCLOSURE` — compliance is 14/14 mandatory and the build is
clean; the one open item is the preprint disclosure in §5.

---

## 1. Manuscript source (Elsevier item type: *Manuscript*)

| file | purpose |
|---|---|
| `paper/main.tex` | master source: `elsarticle` front matter, `\input` of the twelve section files, end matter, bibliography call |
| `paper/sections/sec1.tex` | Introduction: problem, provenance paragraph, contribution list |
| `paper/sections/sec2.tex` | Ecological model and the four competing memory mechanisms |
| `paper/sections/sec3.tex` | Analytical backbone: separation, the attributed SOE lemma, error semantics, testing obstruction, prey-response approximation |
| `paper/sections/sec4.tex` | Numerical methods and solver validation |
| `paper/sections/sec5.tex` | Frequency-domain and finite-horizon evidence, response-level tables to `m=128` |
| `paper/sections/sec6.tex` | Fractional-delay simulation study |
| `paper/sections/sec7.tex` | Experiment design and safety |
| `paper/sections/sec8.tex` | Benchmark, amplitude diagnostic, waveform search, headline figure |
| `paper/sections/sec9.tex` | Prospective experimental interpretation |
| `paper/sections/sec10.tex` | Discussion |
| `paper/sections/sec11.tex` | Conclusion |
| `paper/bibliography.bib` | 30 entries, all cited by the manuscript or its supplement sources; 26 render |

**Not submitted:** `paper/aims_math_style.sty` (obsolete, unreferenced), `paper/sections/sec14.tex`
and `sec15.tex` (orphan supplement sources, not `\input` by `main.tex`),
`paper/bibliography_unused.bib` (47 parked entries), `paper/backup_preR3/` (pre-migration copies).

## 2. Figures (Elsevier item type: *Figure*, one file each)

All vector PDF. Eighteen files, in citation order:

| file | first cited in |
|---|---|
| `fig11_system_schematic.pdf` | sec1 |
| `fig12_backbone_regime.pdf`, `fig15_safety_geometry.pdf` | sec2 |
| `fig01_transfer_magnitude.pdf`, `fig02_phase_2panel.pdf`, `fig18_safe_discrimination_atlas.pdf` | sec5 |
| `fig20_fractional_delay_trajectories.pdf`, `fig21_fractional_delay_bridge.pdf`, `fig22_fractional_delay_design_ranking.pdf`, `fig23_fractional_delay_sweep.pdf` | sec6 |
| `fig04_waveforms.pdf`, `fig05_linear_ranking.pdf`, `fig17_paper_workflow.pdf` | sec7 |
| `fig07_confusion.pdf`, `fig08_accuracy_vs_alpha.pdf`, `fig09_accuracy_snr_channel.pdf`, **`fig24_safe_design_frontier.pdf`** | sec8 |
| `fig06_solver_convergence.pdf` | sec4 |

`fig24_safe_design_frontier.pdf` is the headline figure. `fig10_safety_tradeoff.pdf` is **withdrawn**
and must not be uploaded.

## 3. Required separate files

| file | Elsevier item type | notes |
|---|---|---|
| `paper/highlights.txt` | *Highlights* | 5 bullets, longest 84 characters; filename contains "highlights" as required |
| `paper/main.pdf` | *Manuscript PDF* | build output, 44 pp; regenerate with `bash paper/build_latex.sh` |

## 4. Entered in the submission form, not in the files

| field | value |
|---|---|
| Corresponding author | Ibrahim Alraddadi |
| Email | `ialraddadi@iu.edu.sa` |
| Postal address | Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah 42351, Saudi Arabia |
| Telephone | `+966 50 650 8891` |
| ORCID | `0000-0002-0094-7937` |
| Suggested classification | nonlinear dynamics; fractional-order systems; computational methods |

## 5. Blockers — the package must not be uploaded until these are closed

| # | blocker | status |
|---|---|---|
| B1 | Funding declaration | **CLOSED** — author-confirmed no external funding; `Funding` section inserted |
| B2 | Data statement placeholders | **CLOSED** — deposit published, DOI `10.5281/zenodo.22087770`, cited in the article; zero placeholders remain |
| B3 | **Prior public preprint of this work, under different authorship** | **OPEN** — see `AUTHOR_METADATA_CONFIRMATION.md` §4. Elsevier requires the preprint to be disclosed and cited at submission; the manuscript does neither, and the creator-list discrepancy determines *how* it should be disclosed |

## 6. Verification at the moment of writing

```
clean-directory build            exit 0
LaTeX errors                     0
undefined references/citations   0
multiply-defined labels          0
BibTeX warnings                  0
"??" in the rendered PDF         0
AIMS in PDF metadata             0
abstract                         243 words   (limit 250)
keywords                         6           (range 1-7)
highlights                       5 bullets, max 84 chars
figures cited / present          18 / 18
pages                            44
```

## 7. Companion deposit (on Zenodo, not uploaded to CNSNS)

Published: **`10.5281/zenodo.22087770`**, open access, CC BY 4.0, creator Alraddadi with ORCID.
`fmed-reproducibility-2026-08-24.zip`, 303 461 bytes, md5 `877cfd04e5896824dd72a8ab57939648` —
Zenodo's checksum matches the local file exactly. Contents, exclusions and the verification performed
are in `R5_DATA_DEPOSIT_AUDIT.md`. The article's data statement cites this DOI.
