# Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator–Prey Model

Manuscript, supplementary material, reproducible benchmark, certified-computation
code, and the complete research record. Companion to Zenodo record
[10.5281/zenodo.21809908](https://doi.org/10.5281/zenodo.21809908).

## What this paper does

A safety-constrained framework for discriminating Caputo (fractional), delayed
(DDE), and finite-state latent memory mechanisms around a certified strong-Allee
predator–prey equilibrium:

- exact transfer-function separation of the fractional signature from finite
  latent and retarded single-delay models on compact bands;
- finite-horizon exponential-approximation bounds with **interval-arithmetic
  certified** $L^1$ enclosures (no numerical quadrature error estimate is ever
  used as a certificate);
- a Gaussian minimax testing obstruction coupling approximation error, latent
  complexity, and a protocol-restricted Strong-Allee safety budget;
- a certified **ecological prey-response** finite-state approximation theorem:
  the exact Caputo prey transfer splits into a principal-sheet pole pair
  (realized exactly by a two-state integer-order block) plus a branch-cut
  Laplace mixture, with certified enclosures driving testing lower bounds
  toward chance as latent complexity grows;
- optimal input/observation design, strict fractional invariance safety
  certificates, a specified (not executed) Bayesian sequential layer, and a
  calibrated stable-only simulation benchmark (macro-accuracy 0.537 vs chance
  0.25) exposing a safety–informativeness trade-off.

## Repository layout

| Path | Content |
|---|---|
| `paper/` | LaTeX sources and compiled PDFs: main manuscript (19 pp, results-driven Q1 restructure of 2026-08-17: 4 essential theorems + 19 figures) and standalone detailed supplement (39 pp). Build: `bash paper/build_all.sh`. |
| `benchmark/` | Frozen benchmark v3: solver, designs, factorial results, validation (`python3 benchmark/validate_results.py`). |
| `research_rounds/` | Complete auditable research record, rounds 1–6: results, proofs, theorem/novelty ledgers, per-round audits, and the certified-computation scripts (`round6/compute_round6.py`, `round6/check_round6.py`). |
| `chief_round4/`, `chief_round5/`, `chief_round6/`, `chief_checks/`, `final_chief_checks/` | Independent audit machinery: interval-enclosure validators, atlas repair, lightweight cross-checks, figure regeneration. |
| `source_pack/` | Original mathematical source pack (exact baseline algebra). |
| `FINAL_CLAIM_EVIDENCE_MATRIX.md` | Every headline claim mapped to its theorem, certification status, and artifact. |
| `FINAL_REPRODUCIBILITY.md` | Exact commands and expected outputs for every verification layer. |
| `FINAL_CHANGELOG.md`, `FINAL_CHIEF_AUDIT.md`, `FINAL_PRE_SUBMISSION_GATE.md`, `JOURNAL_POSITIONING.md`, `TYPOGRAPHY_AND_FIGURE_FIXES.md` | Closeout documents. |
| `17–20_*.md`, `IDEA.md`, `INITIAL_PROMPT.md`, `*_PROPOSAL.md` | Bibliography apparatus and project genesis documents. |

## Reproducing the certified numbers

```bash
# kernel-level interval enclosures
python3 chief_round4/validate_Ebar_interval.py
# chief-corrected pulse-ray atlas
python3 chief_round5/repair_atlas.py
# prey-response certified enclosures (focal cells)
python3 research_rounds/round6/compute_round6.py 0.25 0.30
# independent cross-checks
python3 chief_round6/check_round6_lightweight.py
python3 research_rounds/round6/check_round6.py
# archived benchmark consistency
cd benchmark && python3 validate_results.py
```

Requirements: Python ≥ 3.10 with `numpy`, `scipy`, `mpmath`, `matplotlib`;
TeX Live with `pdflatex` + `bibtex` (`extarticle` class).

## Honest-scope notes

The prey-response theorem is linearized and single-channel; a full-vector
ecological-state theorem, a hierarchy-wide Strong-Allee safety theorem for
physically constrained latent rivals, and nonlinear (Volterra) lifts remain
open and are declared as such in the paper. The benchmark rectangle is a
diagnostic, not a certified invariant set, at the full amplitude budget.
