# Final Reproducibility Guide

Date: 2026-08-14 (updated after the chief typography fix and the operator-requested 9pt extarticle class).  Every command below was executed on the archive machine
(Linux, Python ≥3.10 with numpy/scipy/mpmath, TeX Live with pdflatex+bibtex)
and produces the stated output.  Commands are relative to the package root.

## 1. Build the main paper

```bash
cd paper   # (in the repo; in the submission package the tex sources are at the root)
rm -f main.aux main.bbl main.blg main.log main.out sections/*.aux
bash build_latex.sh
```
Expected: exit 0; `fractional-memory-experiment-design.pdf` with **50 pages**,
0 undefined citations, 0 undefined references, 0 LaTeX warnings on the final pass.

## 2. Build the supplement (after the main paper — it reads `main.aux` via xr)

```bash
pdflatex -interaction=nonstopmode supplement.tex
bibtex supplement
pdflatex -interaction=nonstopmode supplement.tex
pdflatex -interaction=nonstopmode supplement.tex
```
Expected: `supplement.pdf` with **18 pages**, 0 undefined, 0 warnings.

## 3. Kernel-level interval enclosures (T20 constants)

```bash
python3 chief_round4/validate_Ebar_interval.py
```
Expected: interval upper enclosures matching `chief_round4/Ebar_interval_bounds.json`
exactly (m=1..32: 0.925, 0.569, 0.541, 0.352, 0.248, 0.248, 0.236, 0.200, 0.200, 0.134).

## 4. Chief-corrected pulse-ray atlas (fig18 data)

```bash
python3 chief_round5/repair_atlas.py
```
Expected: regenerates `research_rounds/round5/atlas_cells_CHIEF_CORRECTED.json`
(numerically identical; float-formatting differences only) and prints stable-regime
counts `0.70: 100/16/12, 0.85: 112/0/0, 0.95: 11/11/58`.

## 5. Certified prey-response enclosures (T23 constants; ~2 min per cell)

```bash
python3 research_rounds/round6/compute_round6.py 0.25 0.30
```
Expected: writes `research_rounds/round6/round6_results.json`; prints per-cell
lines ending with `mass_ok=True`; E_state upper enclosures
A=0.25: 0.5335/0.1254/0.0273/0.0070 and A=0.30: 0.4706/0.0899/0.0204/0.0067
for m=4/8/16/32.  The remaining stable cells run as
`python3 compute_round6.py 0.10` (etc.); A=0.10 is slow (pole–cut
quasi-resonance requires deep adaptive subdivision).

## 6. Independent cross-checks of T23 (no interval code shared)

Lightweight (chief's transformed-grid checker, seconds):
```bash
python3 chief_round6/check_round6_lightweight.py
```
Expected: 8/8 focal cells pass; float/certified ratios ≈ 0.19–0.38, matching
`chief_round6/lightweight_check.json`.

Full (dense-grid Mittag-Leffler validator, ~4 min):
```bash
python3 research_rounds/round6/check_round6.py
```
Expected: `N checks, 0 failures` over every `round6_results*.json` present
(36 checks when all seven stable-cell JSONs are present), plus internal
decomposition cross-checks at ~1e-11 agreement.

## 7. Benchmark consistency (frozen v3 — do NOT re-run the factorial)

```bash
cd benchmark && python3 validate_results.py
```
Expected: `PASS: linear factorial contains 1458 cells` and
`ALL ARCHIVED-RESULT CONSISTENCY CHECKS PASSED`.
`python3 smoke_test.py` additionally verifies the analytic gates
(x*=2/3, alpha*(0.30)=0.9690122761517083) before any solver use.

## 8. Figures

- fig01–fig17: frozen (byte-identical to the audited packages; provenance in
  FIGURE_PROVENANCE.md).  fig11 SHA-256-verified against the post-R5 package.
- fig13: chief-corrected; regenerate with `chief_round6/plot_fig13_chief_corrected.py`.
- fig19: chief-corrected 2-panel; regenerate with
  `chief_round6/plot_fig19_chief_corrected.py` (reads `round6_results*.json`).

## 9. What is deliberately not reproducible from this package

- The benchmark factorial itself is archived, not re-run (frozen by governance);
  its manifest is `benchmark/results/manifest_orion.json`.
- The audit trail (round ledgers) documents process, not results; all
  result-bearing claims map to the artifacts above (see
  FINAL_CLAIM_EVIDENCE_MATRIX.md).
