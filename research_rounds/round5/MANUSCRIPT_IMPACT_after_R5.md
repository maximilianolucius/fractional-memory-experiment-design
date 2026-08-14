# Manuscript Impact — After Round 5

Date: 2026-08-14

## Verdict

The Round-5 theorem gate PASSED (Gate 0A closed via the preferred route; 0B
closed as an honest negative scope result; 0C closed with the mass caveat).
Manuscript integration executed accordingly.

## Changes applied (this round)

- **Abstract**: rewritten around the now-certified three-way kernel-level
  theorem (T20 + T22); the ecological-state lift stated as an open problem
  with quantified obstruction.
- **Sec 1**: contribution paragraph upgraded — the hierarchy-uniform Allee
  budget is now a theorem, with the certified crossover A in (0.15, 0.20).
- **Sec 6**: new theorem T22 (exact d_rob reduction, attained single-mode
  competitor, B_Allee(A,m) enters T20 for the same class) with proof sketch
  and the sandwich numerics; the asymptotic hierarchy separated from the
  frozen safe class (mass caveat).
- **Sec 8**: the one-sided transient interface now cites T22 as its
  hierarchy-uniform version; the A≈0.32 diagnostic kept labeled as the
  locked-rival phenomenon.
- **Sec 12**: atlas discussion — 432-cell certified map; alpha=0.85 panel
  entirely hard@0.25; inconclusive cells concentrated where both error and
  budget are large; Gate-0B scope finding (D0) stated.
- **Sec 14**: T22 row added to the theorem index.
- **New figure**: fig18_safe_discrimination_atlas (3 panels: (A,m) heatmap,
  (alpha,m) heatmap, certified budget frontier with crossover). Caption is
  argumentative and states the theorem basis. The 16 Q1 figures are frozen.
- Atlas tables stay in the research-rounds JSON artifacts (supplement-ready),
  not dumped into main text.

## What must NOT be added

- No "provably discriminable" labels.
- No ecological-state certified bound (Gate 0B negative).
- No asymptotic E_m->0 for K_m itself.
- No monotonicity claims in A for B_eff.

## Build verification

LaTeX rebuild required after integration: 0 undefined citations, 0 undefined
references, 0 warnings expected (verified post-integration).

## Next round (if any)

R6 opportunity: a backbone-consistent latent realization (memory acting
through (s^alpha I - J)^{-1}, i.e. latent modes as fractional relaxation)
could close the ecological-state lift and yield the full-state certified
theorem — the single remaining gap to the 9.5-level claim.
