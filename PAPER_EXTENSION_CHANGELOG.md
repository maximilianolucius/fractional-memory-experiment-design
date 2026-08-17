# Paper extension and ecological-backbone disclosure - 2026-08-17

## Requested changes

1. Explicitly disclose that the present manuscript reuses the **ecological backbone** from the previously submitted companion paper: the same strong-Allee model, locked ecological parameters, coexistence equilibrium, and Jacobian.
2. Extend the main paper by approximately 6-8 pages without re-expanding the theorem-heavy structure.

## Implemented

### Explicit companion-paper disclosure
The disclosure now appears in three prominent locations:

- **Abstract:** states that the ecological backbone is intentionally inherited and is not a new contribution.
- **Introduction:** adds an explicit relationship paragraph and a comparison table separating the two research questions, mathematics, computations, and headline outputs.
- **Model section / Discussion:** states exactly which quantities are inherited and why they are reused as a controlled experimental test bed.

The present paper continues to claim novelty only for memory-mechanism discrimination, finite-horizon approximation/testing results, experiment design, benchmark results, and fractional-delay simulations.

### Main-paper extension
The main-paper content increased by ~8 pages in the reference 9pt layout (19/20 -> 28 pages; renders as 22 pages in the final AIMS Mathematics layout). The theorem count remains **4**. The added material is concentrated on numerical and experimental evidence rather than new theory:

- relationship-to-previous-paper comparison table;
- locked ecological-backbone table;
- numerical validation matrix;
- experimental-grid/reproducibility table;
- certified finite-state response/testing table;
- quantitative fractional-delay bridge table;
- fractional-delay waveform ranking table;
- delay-sweep endpoint table;
- expanded four-class benchmark interpretation;
- stratified accuracy table;
- nonlinear safety/informativeness table;
- a two-stage prospective microcosm protocol;
- expanded discussion of the experimental meaning of the results.

### Fractional-delay numerical evidence
The targeted fractional-delay scripts were rerun to regenerate their JSON/NPZ data and figures. No new broad computational campaign was launched. The expanded text uses the archived/reproduced numerical outputs.

## Build / visual gate

- `main.pdf`: **22 pages** (AIMS layout; 28 in the reference 9pt layout)
- `supplement.pdf`: **29 pages** (AIMS layout; 38 in the reference 9pt layout)
- 4 main theorems
- 19 main figures
- 0 undefined citations
- 0 undefined references
- 0 LaTeX warnings in the main final pass
- 0 overfull boxes in the main final pass

The full main PDF was rendered and visually inspected after compilation in both layouts.
