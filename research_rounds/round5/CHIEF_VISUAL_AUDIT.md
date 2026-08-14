# Chief Visual Audit — Q1 Visual Pass

Date: 2026-08-14
Package reviewed: `submission-2026-08-14-q1visual`

## Overall visual verdict

The researcher's Q1 visual pass is a **substantial improvement**. The paper now has a genuine visual narrative rather than a cluster of benchmark plots. In particular, the new system schematic, ecological-backbone view, model-family diagram, exact-separation/approximation synthesis, safety geometry, Bayesian loop, and paper-workflow figure materially improve reviewer readability.

The main remaining problems I found were not stylistic preferences; they were places where a figure's wording or construction could make a mathematically stronger claim than the underlying evidence supported. I corrected those directly and regenerated the figures. No factorial benchmark was rerun.

## Figure 11 — Bayesian sequential safe-design loop

This is the figure that required the most researcher effort, and I **kept the visual concept**. I did not replace it with a different figure.

The issue I found was semantic: the prior version had dashed feedback arrows whose direction made the sequential logic ambiguous and treated the model prior as visually static across iterations.

I regenerated it as the explicit loop

`current belief -> safe admissible designs -> expected information -> choose/execute/observe -> Bayesian update -> stopping test`,

with

`continue: p_n <- p_{n+1}`

shown explicitly. I also enlarged its manuscript width from 0.92 to 0.98 `\textwidth` and retained the bottom guard that says the Bayesian layer is specified but not executed in the present BIC benchmark.

**Verdict after patch:** keep Figure 11 in the main paper. It is now one of the useful synthesis figures and no longer risks suggesting an executed Bayesian loop.

## Important correctness issue — the benchmark rectangle

Several new graphics described the plotted rectangle as a **certified safe box**. I checked the strict face inequalities required by Theorem T17 at the representative benchmark setting

- `A = 0.25`,
- prey-only input,
- `|u| <= 0.10`,
- the rectangle used by the benchmark.

The four worst-case face left-hand sides are

- lower prey: `-0.59206349` — fails the required `>= 0` sign;
- upper prey: `-0.55762319` — satisfies the required `<= 0` sign;
- lower predator: `-0.07619048` — fails the required `>= 0` sign;
- upper predator: `+0.33043478` — fails the required `<= 0` sign.

Therefore that plotted rectangle is **not certified invariant by T17 under the full +/-0.10 input budget**. This does not invalidate the benchmark. It means the rectangle is a **benchmark diagnostic rectangle**, while a T17 invariant-set claim is conditional on separately verifying the strict face conditions.

I changed this wording consistently in the system schematic, ecological-backbone figure, safety geometry, abstract/discussion/captions, and benchmark description. The reproducible check is in `chief_checks/check_strict_rectangle.py`.

## Figure 7 — exact separation vs finite-horizon approximation

The researcher's synthesis idea is strong, but two display choices needed repair.

1. Panel (b) originally used arbitrary theorem-admissible truncation parameters that made the exponential approximation look much worse than it needs to be. I used a **small deterministic grid search over the theorem's free `(ell,L)` display parameters**. This is not a new simulation campaign and does not change any theorem; it simply prevents a poor arbitrary parameter choice from visually misrepresenting the constructive approximation.
2. Panel (c) drew a "noise floor" created from the last plotted approximation error. That threshold was not tied to the manuscript's observation-noise model. I removed it. The panel now shows deterministic approximation error versus latent-mode budget and explicitly says that no statistical noise threshold is being asserted.

The caption was updated to match the repaired figure.

**Verdict:** keep the figure. It is a valuable synthesis figure after this correction.

## Figures 4–5 — input families and linear ranking

The original visual language used "safe-by-construction" even though the linear ranking only uses a common peak-amplitude budget and some of the designs cross the Allee threshold in the nonlinear benchmark.

I changed the interpretation to

- lower crossing rate / transient,
- higher crossing rate / broadband,

and renamed the linear ranking as a result under a **common amplitude budget**, not nonlinear state safety.

No ranking values were changed.

## Figure 10 — safety geometry

The basic figure is good and should remain in the main text. I changed the legend/caption to distinguish

- `no crossing in this run`,
- `crosses A in this run`,

from a theorem-level invariant-set certificate. The plotted single-cell margins remain the researcher's computed values (`+0.369` for multiscale and `-0.257` for PRBS).

## Figure 3 — ecological backbone

This is one of the strongest additions conceptually. I retained it, but changed the rectangle wording to diagnostic rather than certified. The figure now correctly distinguishes

- rigorous prior information: the Allee threshold/extinction structure,
- illustrative numerically integrated recovery/collapse trajectories,
- the diagnostic benchmark rectangle.

## Render-level cleanup

A direct render check found clipped titles in four generated PDFs:

- transfer magnitude,
- high-frequency phase panel,
- solver convergence,
- confusion matrix.

I shortened the titles and regenerated the PDFs. The scientific detail stays in the captions. A second edge check found the titles fully inside the figure canvases.

## Reproducibility / build fixes

Two packaging issues were fixed:

1. `make_q1_figures.py` wrote to `paper/figures/` even though this flattened submission's manuscript reads `figures/`. It now regenerates the actual manuscript figures.
2. A clean LaTeX build exposed a `natbib` mode mismatch (`plain` numeric bibliography with default author-year natbib). `main.tex` now requests `natbib` numeric mode. The build script also falls back to the released `main.bbl` if BibTeX is not installed.

Final local preflight after the patch:

- 67 pages,
- 16 generated figure PDFs,
- 0 undefined citations,
- 0 undefined references,
- 0 LaTeX warnings,
- 0 TeX errors.

## Visual recommendation for the researcher

Do **not** start another visual redesign now. The figure architecture is good enough to support the next research rounds. Preserve the figure generator and only modify figures when new mathematics from R2–R5 changes the substantive story.

The final Q1 visual pass should happen after the Safe Memory-Discrimination Atlas exists; that atlas, not another cosmetic schematic, should become the next headline visual object.
