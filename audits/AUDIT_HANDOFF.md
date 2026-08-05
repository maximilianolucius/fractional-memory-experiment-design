# Audit response — status and handoff (2026-08-05)

Response to `audits/PAPER_AUDIT.md` (referee reject + major reconstruction). Scope adopted:
**Option A** (linearized structural discrimination + calibrated stable-only IC benchmark; full
Bayesian OED = future work).

## DONE (paper compiles clean: exit 0, 53 pp, 0 undefined citations)

### Benchmark reconstruction (Orion, v3 calibrated-safe) — closes P0.5/P0.6/P0.7/P0.9
- Rivals calibrated to a common safe backbone (shared equilibrium/Jacobian; DDE `tau=0.35`
  stable, latent coupling `0.15`); inputs at a common peak-amplitude budget `|u|_inf<=0.10`.
- **P0.6** stable regime `A in {0.20,0.25}` (memory-shape, primary) vs verdict `A in {0.30,0.40}`
  (stability, separate). **P0.7** balanced metrics, 5-class and 4-class confusion, stratification.
  **P0.9** numerical Allee safety margins per design.
- Honest result: stable macro-accuracy **0.537** (chance 0.25); safety-informativeness trade-off
  (transient designs safe but weak; broadband designs strong but cross Allee). Supersedes 0.749.
- Code `benchmark/*.py`, results `benchmark/results/*.json`, manifest `artifacts/manifests/manifest.json`.
- Section 10 rewritten clean around these numbers; labeled BIC / information-criterion, **not**
  Bayesian evidence (**P0.3**).

### Editorial P0
- Retitled "Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a
  Strong-Allee Predator--Prey Model" (dropped "definitive").
- Abstract rewritten: quantitative (0.54 vs chance 0.25), states the trade-off and the limitation.
- Bibliography moved from the front (was pages 1--5) to after the appendix; removed the
  `cite`/`natbib` conflict; `hyperref` `hidelinks`; escaped `&` in the `.bib`; fixed malformed cite.
- Removed a stray `\end{document}` in sec14 and the garbled sec10 LaTeX (`\end{0}`, brace/env errors).

## NOT DONE — handoff (deep math; needs careful editing, not the auto-loop)

Exact replacement statements are in `audits/MATHEMATICAL_REPAIR_NOTES.md`.

- **P0.1 Theorem 9.3 is FALSE.** Replace "KL of the expected posterior" by the **expected KL**
  identity (repair-notes sec 6); fix Eq (67), the discussion, and the conclusion. Remove the claim
  that greedy one-step MI maximization minimizes the number of experiments.
- **P0.2 Appendix (sec14) contradicts the main theorems.** Reconstruct theorem-by-theorem
  (repair-notes sec 10). Current wrong proofs: T11 amplitude `sqrt(P lambda_max)` (should be
  `u*=sqrt(P) v_max`); T12 Fejer--Riesz (use Caratheodory); T16 "extreme value theorem on an
  L-infinity ball" (false in infinite dim); T17 unstated quasimonotone `eta`; T18/9.1 linear-Gaussian
  posterior claimed for nonlinear; T19/9.3 same false identity.
- **P0.10** Theorem 8.4: use STRICT inward-pointing inequalities (margin `eta>0`).
- **P0.11** No-free-lunch: label Corollary 6.6 as a linearized fixed-input result (or add the
  Volterra/Gronwall extension, repair-notes sec 3).
- **P1.1--P1.12** (repair-notes + PAPER_AUDIT sec 2): model-count wording; compact frequency band
  (5.4); attainment/compactness (7.1); composite-model caveat (7.5); exact retarded-DDE class (5.2);
  cross-channel phase (7.6); Caputo prehistory (9.8); `m<=5` as a budget not biology; robust-KL can be
  zero at degeneracies; safety projection is feasible-not-optimal; "zero divergence" is not safety.
- **Figures**: none present; the audit lists 8 expected. Generate from `benchmark/results/`.
- **P0.12** bibliography: entries now resolve and are at the end, but some BibTeX metadata still needs
  normalization (author fields, a malformed Chaos entry) per PAPER_AUDIT sec 1.

The loop is STOPPED. To resume the deep reconstruction, re-inject `OP-AUDIT-FIX` (already in the
repo) after considering a stronger/faster model or Aureus egress (the `.144` NVIDIA route throttles).
