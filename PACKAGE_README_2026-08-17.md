# Q1-restructured submission package - 2026-08-17

This revision implements the requested restructuring and numerical strengthening, explicitly discloses reuse of the ecological backbone from the previously submitted companion paper, and extends the main manuscript by 8 pages without expanding the theorem count.

## Final manuscript

- `main.pdf` / `fractional-memory-experiment-design.pdf`: main paper extended by ~8 pages of content over the 19-page baseline (28 pages in the reference 9pt layout; 22 pages in the final AIMS Mathematics layout).
- `supplement.pdf`: detailed analytical supplement (38 pages in the reference 9pt layout; 29 pages in the AIMS layout).
- Main paper: 4 essential theorems and 19 figures, with the extension concentrated on experimental design, numerical validation, fractional-delay evidence, benchmark tables, and explicit companion-paper disclosure.

## Key new material

- `sections/sec6.tex`: dedicated fractional-delay numerical study.
- `benchmark/fractional_delay_experiments.py`: combined Caputo-delay solver and targeted experiments.
- `figures/fig20_fractional_delay_trajectories.pdf`
- `figures/fig21_fractional_delay_bridge.pdf`
- `figures/fig22_fractional_delay_design_ranking.pdf`
- `figures/fig23_fractional_delay_sweep.pdf`

## Review documentation

- `RESPONSE_TO_FEEDBACK.md`
- `FRACTIONAL_DELAY_NUMERICAL_REPORT.md`
- `Q1_RESTRUCTURE_CHANGELOG.md`

## Build

Run `bash build_all.sh`.

## AIMS Mathematics template conversion (2026-08-17)

The main manuscript and supplement are now typeset in an AIMS Mathematics submission layout based on the official journal template conventions. See `AIMS_MATHEMATICS_TEMPLATE_NOTES.md`.

Primary files:
- `main.pdf` — AIMS Mathematics formatted main manuscript.
- `fractional-memory-experiment-design-AIMS-Mathematics.pdf` — identical submission PDF with descriptive filename.
- `supplement.pdf` — matching supplementary material.
- `main.tex`, `supplement.tex`, `aims_math_style.sty` — editable LaTeX sources.
