# Final Claim-to-Evidence Matrix

Date: 2026-08-14.  Scope: every headline claim of the main paper, mapped to its
theorem/proof, its numerical/data evidence, and the reproducible artifact.
Statuses follow the chief-audited ledger (THEOREM_LEDGER_after_R6_CHIEF.md).

| # | Headline claim (main paper) | Theorem / statement | Evidence & certification status | Artifact(s) |
|---|---|---|---|---|
| 1 | The Caputo transfer signature is not reproducible by any finite-dimensional integer-order latent model on a compact band (collocated channel, $CB\neq0$) | Thm 5.x (T4), Thm (T7) | PROVED (analytic); no numerics required | main paper Sec. 5; proofs at statement |
| 2 | Nor by any strictly proper retarded single-delay model of the stated class | Thm (T5) | PROVED (stated class only; scope remark) | main paper Sec. 5 |
| 3 | Quantitative high-frequency remainder for the fractional signature | Thm (T6) | PROVED | main paper Sec. 5 |
| 4 | Fractional kernel admits exact positive diffusive representation; no uniform approximation at the singular endpoint; constructive finite $L^1$ approximation on finite horizon | Thms (T8, T9a, T9b) | PROVED; constructive proof + explicit parameter choices in Supplement S2 | Supplement S2 |
| 5 | Finite-horizon impossibility barrier: unrestricted latent dimension destroys robust discrimination (linearized, fixed input) | Thm (T10), Cor. (unrestricted) + scope remark | PROVED (linearized fixed-input scope stated) | main paper Sec. 6 |
| 6 | Kernel-level interval-enclosed approximation errors for the frozen nested hierarchy $\mathcal K_m$ | Definition + table in Sec. 6 | CERTIFIED (outward-rounded interval arithmetic; QUADPACK never used as certificate); values 0.925..0.134 for m=1..32 | `chief_round4/validate_Ebar_interval.py`, `Ebar_interval_bounds.json` |
| 7 | Composite Gaussian testing lower bound under bounded safe excitation (kernel level) | Thm (T20) | PROVED; non-vacuity numbers at $\sigma=0.10$ under universal cap (e.g. $P_e^*(32)\ge0.384$) | main Sec. 6; proof in Supplement S2 |
| 8 | Hierarchy-uniform Strong-Allee budget on the fixed positive pulse ray; exact single-mode extremizer | Thm (T22) | PROVED (protocol ray only); displayed $d_{\rm rob}$ constants are high-accuracy numerics, NOT interval-certified (stated in text) | main Sec. 6; proof in Supplement S2; `research_rounds/round5/compute_round5.py`, chief-corrected atlas `atlas_cells_CHIEF_CORRECTED.json` |
| 9 | Theorem-guided pulse-ray atlas; every displayed Matignon-stable cell at $\alpha=0.85$ has $P_e^*\ge0.25$ | Atlas (fig18) + T20/T22 | VALIDATED (theorem-guided; 112/112 stable cells hard; unstable cells hatched and excluded) | `chief_round5/repair_atlas.py`, `repair_summary.json`, fig18 |
| 10 | State safety alone does not bound input energy (physical input class required) | Thm (T21) | PROVED (negative theorem) | main Sec. 8 |
| 11 | Pole/branch-cut decomposition of the fractional relaxation mode in the sector $\alpha\pi/2<\lvert\arg\lambda\rvert<\alpha\pi$; Matignon condition = stability of the principal-sheet pole | Lemma (polebranch) | PROVED; sector verified per cell by interval arithmetic; decomposition cross-checked vs Mittag-Leffler series (~1e-11) | main Sec. 6; proof in Supplement S2; `research_rounds/round6/compute_round6.py` (assertions), `check_round6.py` |
| 12 | Certified ecological prey-response approximation: explicit stable integer-order finite-state surrogate with interval-certified $L^1(0,T)$ enclosures; e.g. $A{=}0.25$: 0.5335/0.1254/0.0274/0.0070 for $m{=}4/8/16/32$ | Thm (T23) | CERTIFIED (outward-rounded enclosures + analytic tail; **prey-input→prey-output channel only** — chief-corrected scope); all 8 focal cells independently cross-checked (transformed-grid float ratios 0.19–0.38) | `research_rounds/round6/compute_round6.py`, `round6_results*.json`, `chief_round6/check_round6_lightweight.py`, `lightweight_check.json` |
| 13 | Prey-response Gaussian testing bound under the physical pulse cap $B=0.120$: $P_e$ lower bounds 0.340→0.498 ($A{=}0.25$), 0.359→0.498 ($A{=}0.30$) at $\sigma=0.10$ | Cor. (prey-response testing) | PROVED; headline values use the pulse shape/peak cap, NOT any Strong-Allee state-hierarchy claim (chief repair) | main Sec. 6; fig19 (chief-corrected 2-panel); `chief_round6/plot_fig19_chief_corrected.py` |
| 14 | Safety certificates: safe informative perturbation exists; strict fractional inward-pointing rectangle invariance | Thms (T16, T17) | PROVED (strict stated assumptions); face inequalities derived in Supplement S4 | main Sec. 8; Supplement S4; `chief_checks/check_strict_rectangle.py` (diagnostic) |
| 15 | Optimal design: energy-optimal input, finite multisine support, top-$n$ schedule | Thms (T11, T12, T13) | PROVED (linear-Gaussian regime) | main Sec. 7; proofs in Supplement S3 |
| 16 | Bayesian layer: nonlinear posterior update and sequential information identity/bound | Thms (T18, T19) | PROVED; layer specified, NOT executed (BIC used in benchmark; stated everywhere) | main Sec. 9; Supplement S5 |
| 17 | Benchmark: macro-accuracy 0.537 vs chance 0.25, stable-only, BIC; safety–informativeness trade-off | empirical | VALIDATED (frozen benchmark v3; amplitude-cap protocol; not a theorem) | `benchmark/` + `results/` + `validate_results.py` |
| 18 | Novelty position: the joint construction (certified Allee backbone + fractional-vs-latent hierarchy + protocol-restricted safety + interval-certified prey-response approximation + complexity-driven identifiability loss), not any generic component | Related-work statement | Chief-corrected positioning with added citations | main Sec. 1/12; NOVELTY_LEDGER_after_R6_CHIEF.md |

## Explicitly NOT claimed (guarded in text)

- A full-vector ecological-state approximation theorem (T23 is one scalar channel).
- A hierarchy-wide Strong-Allee safety theorem for physically constrained
  full-state latent rivals (open; the R6 mass-only witness is demoted and not
  used anywhere in the headline chain).
- Nonlinear (Volterra) lifts of any linearized statement.
- Novelty of contour/Hankel Mittag-Leffler technology, rational/Prony
  approximation, or safe information limits in isolation.
- Any "provably discriminable" label; inconclusive atlas cells are never
  upgraded.
- Benchmark accuracy as a theorem-level guarantee.
