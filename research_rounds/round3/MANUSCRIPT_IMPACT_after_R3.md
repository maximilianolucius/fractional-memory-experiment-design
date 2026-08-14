# Manuscript Impact — After Round 3

Date: 2026-08-14

## Governance decision

**Round-3 gate PASSED — R4 authorized. The manuscript is still not updated.**

Per the standing rule (MANUSCRIPT_IMPACT.md, Round 1), research-round results
stay outside `main.tex` until the program reaches a stable theorem set. The
end-of-R3 gate is a necessary condition for manuscript integration, not the
trigger: integration happens at R4, when the testing bound is proved and the
final novelty statement is locked.

## What R4 will change in the manuscript (planned, not executed)

1. **Abstract / Introduction** — replace generic safe-OED language with the
   three-way interaction (fractional approximation × latent complexity ×
   Strong-Allee safety) and the honest scope: the impossibility is
   protocol-relative (Theorem R3b-neg), the quantitative bound is for frozen
   transient protocols (Theorem R3b-pos).
2. **Section 6 (approximation)** — promote `K_m` / `E_m(alpha,T)` to first-class
   quantities; cite the T9b certified bound as the R4 interface; optionally add
   K07 (Braess-Hackbusch 2005) if rate discussion enters.
3. **Section 8 (safety)** — add the repaired interface B.5 as a remark:
   diagnostic rectangle (already chief-patched) + threshold-envelope inner
   certificate (R2a) + protocol-relative outer bound (R3b-pos).
4. **New headline theorem (R4)** — minimum-error testing lower bound for
   discriminating Caputo from the nested latent hierarchy under the
   B.5 budget, via R1 + certified E_m.
5. **Discussion** — position the negative theorem prominently: broadband
   protocols evade the Allee-coercive bound only through amplitude that the cap
   separately limits.

## Immediate manuscript state (unchanged by this round)

- `main.tex` and all sections: chief-patched q1visual version (67 pp, exit 0,
  0 undefined). Not touched in R3.
- Figure set: 16 manuscript figures pixel-identical to the chief-verified
  package (chief's 100-dpi raster comparison, mean absolute difference = 0).
- Research figures (`round2/B_safe_vs_alpha_CHIEF_CORRECTED.pdf`,
  `round3/round3_diagnostic.pdf`) live in `research_rounds/` and are NOT
  manuscript figures.

## Open items before integration (R4 prerequisites)

- certified `m(eps)` inversion of the T9b bound for the R4 constants;
- window-wide worst-case over the declared latent window `[1e-3,10]` if the
  R4 bound is to be window-robust (latent3 is only one locked realization);
- one-line scope sentence for the nonlinear lift (linearized regime only),
  matching manuscript Remark `rem:nfl_scope`.
