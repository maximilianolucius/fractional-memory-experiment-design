# Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator–Prey Model

Companion repository: manuscript, reproducible benchmark, and source material.

**Published record (open access):** DOI [10.5281/zenodo.21809908](https://doi.org/10.5281/zenodo.21809908)

## What this is
A safety-constrained framework for **actively discriminating** fractional (Caputo),
delayed (DDE), and bounded-complexity latent-state memory mechanisms around a certified
strong-Allee predator–prey equilibrium. It combines exact linear transfer-function
separation, a finite-horizon exponential-approximation obstruction, and computable
input/observation designs, evaluated in a calibrated, safety-instrumented, stable-only
nonlinear benchmark.

## Repository layout
```
paper/            LaTeX source, figures, and compiled main.pdf (57 pp, 10 figures)
benchmark/        reproducible code + machine-readable results
  *.py            core algebra + Caputo PECE solver, designs, simulators, driver, figure/export scripts
  results/*.json  gates, solver validation, linear-Gaussian factorial, nonlinear confusion, manifest
source_pack/      mathematical development pack (theorem statements + derivations)
audits/           academic audit + mathematical repair notes + response/handoff status
artifacts/        run manifest
17..20_*.md       verified bibliography, claim-to-citation map, bibliographic audit, related-work positioning
IDEA.md, INITIAL_PROMPT.md, *_PROPOSAL.md   project brief and original proposal
```

## Build the manuscript
```bash
cd paper && bash build_latex.sh      # pdflatex -> bibtex -> pdflatex x2
```
Requires a standard TeX Live (article, amsmath, amssymb, amsthm, graphicx, hyperref, natbib).

## Reproduce the benchmark
```bash
python benchmark/run_all.py --workers 300 --reps 200 --N 400   # executed on a 344-core server
python benchmark/make_figures.py                                # regenerates paper/figures/
```
Every number and figure in the paper is generated from `benchmark/` — none is entered by hand.
Headline result: exact analytic gates and a Mittag–Leffler-validated Caputo solver; an exact
linear-Gaussian design ranking; a calibrated stable-only nonlinear benchmark with macro-averaged
model-selection accuracy 0.54 (chance 0.25) exhibiting a safety–informativeness trade-off.

## Status (honest)
Revised working draft responding to an academic audit. Under revision (see
`audits/AUDIT_HANDOFF.md`): the Theorem 9.3 statement, the proof appendix, and a full Bayesian
sequential-design layer (future work).

## License
CC-BY-4.0 (matching the Zenodo record).
