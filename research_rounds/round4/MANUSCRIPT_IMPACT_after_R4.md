# Manuscript Impact — After Round 4

Date: 2026-08-14

## Decision

**Phase 3 executed: the manuscript integrates the Round-4 theorem set.**

All three integration conditions from MANUSCRIPT_IMPACT_after_R3_CHIEF.md were
met before integration:

1. the latent hierarchy is frozen consistently across approximation (K_m),
   ecological realization (shared backbone + memory kernels), and common
   safety (mass bound, one-sided interface) — Phase 0 item 0.1;
2. the testing lower bound is mathematically valid (Theorem T20, direction
   verified) and numerically non-vacuous in a defensible regime
   (P_e >= 0.33 at m=16, sigma=0.10; >= 0.39 at m=32) — Phase 2 gate;
3. every numeric constant is labeled analytic, certified numerical,
   diagnostic, or empirical throughout.

## What changed in the manuscript (this round)

- Abstract rewritten around the three-way interaction (fractional
  approximation x latent complexity x Allee safety) with the testing bound
  and the protocol-relative crossover.
- Sec 1: contribution paragraph extended with T20/T21.
- Sec 6 (approximation): new subsections — frozen hierarchy K_m with nested
  windows and mass bound; certified approximation error definition + constant
  table (m = 1..32); Theorem T20 with proof.
- Sec 8 (safety): new subsection — Theorem T21 (negative scope, uniform
  Riemann-Lebesgue proof) and the corrected one-sided transient interface
  with the A≈0.32 crossover (diagnostics explicitly labeled).
- Sec 12 (discussion): trade-off paragraph now states the certified
  protocol-relative ceiling; the constrained-optimization open problem kept.
- Sec 14: theorem index rows for T20 and T21.
- bibliography.bib: T01 (Tsybakov 2009) added.
- Author block: Ibrahim Alraddadi, Islamic University of Madinah
  (per user instruction).
- PDF artifact renamed: fractional-memory-experiment-design.pdf (build script
  updated).

## What stayed frozen

- All 16 Q1 manuscript figures: unchanged (chief instruction).
- Benchmark results and archived JSONs: unchanged.
- Bayesian layer (Sec 9): specified-not-executed, unchanged.

## Build verification

exit 0; 71 pages; 0 undefined citations; 0 undefined references; 0 LaTeX
warnings. bibtex run clean (72 entries, T01 new).

## Next round (R5)

Safe Memory-Discrimination Atlas: theorem-driven figures mapping
(Ebar_m^cert, B_eff, sigma) -> P_e lower bounds across the parameter space;
window-wide worst case over the declared latent window if the atlas bound is
to be window-robust; nonlinear-lift scope sentence for the safety statements.
