# R3-F — Adversarial search for safe-and-informative designs

**Round 03, researcher deliverable. Status: the Round-02 negative result is FALSIFIED.**

Assignment: attempt to break our own claim that safety and informativeness are in
irreducible conflict, by searching input waveforms outside the six historical families.
The search succeeded. This document reports the falsification, its scope, and what it
forces us to retract.

---

## 1. Headline

The safety–informativeness trade-off reported in the submitted manuscript is **not a
property of the system**. It is an artifact of restricting the input to six classical
parametric waveform families. Optimising over piecewise-constant inputs at the *same*
peak-amplitude budget yields designs that are simultaneously

- **strictly safer** than every accuracy-leading historical design (0% Allee crossings,
  positive certified margin), and
- **more informative** than the best historical design of *any* kind, safe or not.

| | best safe design found | only safe historical design | best historical design (any) |
|---|---|---|---|
| waveform | `pwc6` (6-level piecewise constant) | multiscale | multisine |
| BIC macro-accuracy | **0.8030** | 0.5141 | 0.7628 |
| Allee crossing rate | **0.000** | 0.000 | 0.357 |
| min Allee margin | **+0.0920** | +0.2921 | −0.2405 |

Gain over the only safe historical design: **+0.2890 macro-accuracy**.
Gain over the best historical design of any kind: **+0.0403 macro-accuracy, while
eliminating a 35.7% crossing rate.**

All twelve designs were evaluated by the *same* BIC classifier, at the *same* amplitude,
on the *same* 56-cell grid with the *same* 100 replicate seeds. No divergences.

---

## 2. Search protocol (Stage 1)

Fixed and frozen from the manuscript configuration:

| quantity | value |
|---|---|
| peak-amplitude budget `U_cap` | 0.100 (identical to v3/v4 `amp=0.100`) |
| required safety margin `δ` | 0.050 (min over the four model classes) |
| fractional order `α` | 0.85 |
| horizon `T` | 12.0 |
| Allee threshold `A` | 0.25 |
| observation | both channels |

Objective, computed over the four candidate classes `{ODE, Caputo, DDE, latent3}`:

```
J(u) = min over pairs (a,b) of  || mu_a(u) - mu_b(u) || / sigma
```

i.e. the *minimum* pairwise separation in noise units — a minimax discrimination
surrogate, not an average. Hard constraint: `min_class allee_margin(u) >= δ`.

Families searched (Sobol sequence, then Nelder–Mead refinement of the per-family best):
piecewise-constant `pwc4/pwc6/pwc8`, free multisine `fourier3…fourier6`,
pulse trains `pulses2/pulses3/pulses4`.

**Coverage: 163 840 evaluated candidates; 87 601 (53.5%) satisfy the safety constraint.**

Historical baselines re-evaluated under the identical objective:

| design | J | min margin | safe (δ=0.05) |
|---|---:|---:|:--:|
| prbs | 2.393 | −0.3139 | no |
| pulse | 2.101 | −0.1207 | no |
| multisine | 1.910 | −0.2405 | no |
| sinusoid | 1.616 | −0.3058 | no |
| multiscale | **1.452** | **+0.2921** | **yes** |
| chirp | 1.346 | −0.3012 | no |

So among the six historical families, exactly **one** is safe at this amplitude, and it
is the *least* informative of the six by the objective. That is the entire empirical
basis of the manuscript's trade-off claim.

Search result:

- best **safe** candidate: `J = 6.225` (`pwc6`, after refinement; margin +0.0500, constraint active)
- best safe candidate before refinement: `J = 5.669`
- best **unsafe** candidate: `J = 15.919` (`pwc6`, margin −0.3279)

The best safe design beats the only safe historical design by a factor **6.225 / 1.452 = 4.29**
on the discrimination objective, and beats the best *unsafe* historical design
(prbs, J = 2.393) by a factor **2.60** while remaining safe.

Distribution of J over the 163 840 candidates:

| | max | p99 | median |
|---|---:|---:|---:|
| safe (n=87 601) | 5.669 | 1.881 | 0.123 |
| unsafe (n=76 239) | 15.919 | 6.261 | 1.814 |

Composition of the top-500 safe candidates:
`pwc4:119, pwc6:116, pwc8:99, pulses4:35, pulses3:28, fourier3:25, fourier6:24, pulses2:21, fourier4:19, fourier5:14`.
**All top-12 safe candidates are piecewise-constant.** Piecewise-constant inputs are
absent from the six historical families — the manuscript never tested this class.

---

## 3. Validation with the real classifier (Stage 2)

Stage 1 uses a Gaussian two-point separation surrogate. It could be optimistic. Stage 2
therefore re-runs the **actual BIC four-class classifier** used for the manuscript
benchmark, on the top six search designs and all six historical designs, at
`amp = 0.100`, 56 cells × 100 replicates per design (672 cells total), identical seeds.

| design | family | macro | micro | crossing rate | min margin | ODE | Caputo | DDE | latent3 | safe |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|:--:|
| S#0_pwc6 | pwc6 | **0.8030** | 0.7870 | 0.000 | +0.0920 | 0.974 | 0.911 | 0.853 | 0.475 | yes |
| S#3_pwc6 | pwc6 | **0.7830** | 0.7529 | 0.000 | +0.1215 | 0.976 | 0.910 | 0.927 | 0.318 | yes |
| S#2_pwc6 | pwc6 | **0.7828** | 0.7648 | 0.000 | +0.0963 | 0.968 | 0.875 | 0.816 | 0.472 | yes |
| S#1_pwc6 | pwc6 | **0.7796** | 0.7445 | 0.000 | +0.1094 | 0.966 | 0.838 | 0.897 | 0.416 | yes |
| S#5_pwc8 | pwc8 | **0.7687** | 0.7273 | 0.000 | +0.1760 | 0.976 | 0.844 | 0.926 | 0.328 | yes |
| multisine | historical | **0.7628** | 0.7246 | 0.357 | -0.2405 | 0.971 | 0.844 | 0.902 | 0.333 | no |
| S#4_pwc6 | pwc6 | **0.7497** | 0.7204 | 0.000 | +0.0670 | 0.979 | 0.766 | 0.743 | 0.511 | yes |
| prbs | historical | **0.7105** | 0.7132 | 1.000 | -0.3139 | 0.973 | 0.802 | 0.521 | 0.546 | no |
| sinusoid | historical | **0.6847** | 0.6866 | 1.000 | -0.3058 | 0.966 | 0.844 | 0.549 | 0.380 | no |
| chirp | historical | **0.6826** | 0.6836 | 0.929 | -0.3012 | 0.960 | 0.832 | 0.547 | 0.391 | no |
| pulse | historical | **0.6207** | 0.5521 | 0.071 | -0.1207 | 0.981 | 0.528 | 0.647 | 0.326 | no |
| multiscale | historical | **0.5141** | 0.4439 | 0.000 | +0.2921 | 0.964 | 0.404 | 0.445 | 0.244 | yes |

Stage 2 confirms Stage 1 qualitatively and quantitatively:

- **6/6 search designs are safe** (0.000 crossing rate, margins +0.067 to +0.176).
- **5/6 search designs outrank the best historical design of any kind**, including the
  unsafe ones.
- The surrogate is a usable but weak ranker *within* the search set: over the six search
  designs, Spearman `rho = 0.714` (p = 0.111, n = 6), Pearson `r = 0.773` (p = 0.071).
  Not significant at n = 6. What it does get right is the top: the design with the highest
  `J` (5.669) is also the highest-accuracy design overall (0.8030). Treat `J` as a screen,
  not as a calibrated predictor.
- Stage 1 is *conservative* about the historical designs relative to Stage 2 (multisine
  ranks 3rd of 6 by `J` but 1st of 6 historical by BIC accuracy), so the surrogate does
  not manufacture the advantage — it understates the historical baselines and still loses
  to the search designs by a wide margin.

Where the gain comes from, by class recall (`SEARCH#0_pwc6` vs `multiscale`, the safe
historical design):

| class | multiscale | pwc6 (found) | Δ |
|---|---:|---:|---:|
| ODE | 0.964 | 0.974 | +0.010 |
| Caputo | 0.404 | **0.911** | **+0.507** |
| DDE | 0.445 | **0.853** | **+0.408** |
| latent3 | 0.244 | 0.475 | +0.231 |

The safe historical design was essentially unable to recognise fractional or delayed
memory (recall 0.40 / 0.45 against chance 0.25). The found design recognises both at
0.85–0.91 *without leaving the safe set*. This is the substantive scientific content of
the falsification: the manuscript's conclusion that safe excitation cannot identify
memory structure is wrong, and it was wrong because of the waveform parameterisation.

Reproducible parameters of the top designs (switching levels in units of `U_cap`, equal
sub-intervals over `[0,T]`):


| rank | family | J (stage 1) | min margin | switching levels (units of U_cap) |
|---:|---|---:|---:|---|
| 0 | pwc6 | 5.6690 | +0.0920 | +0.513, -0.735, +0.692, +0.469, -0.712, -0.353 |
| 1 | pwc6 | 5.1832 | +0.1094 | +0.391, +0.234, -0.489, +0.699, +0.761, +0.702 |
| 2 | pwc6 | 4.7860 | +0.0963 | +0.567, -0.944, +0.926, +0.649, -0.786, -0.620 |
| 3 | pwc6 | 4.3276 | +0.1215 | +0.814, -0.903, +0.772, +0.734, +0.962, -0.847 |
| 4 | pwc6 | 4.2741 | +0.0670 | +0.266, +0.081, -0.519, +0.693, +0.748, -0.114 |
| 5 | pwc8 | 4.2022 | +0.1760 | +0.750, +0.317, -0.996, +0.804, +0.589, +0.046, -0.252, +0.692 |

---

## 4. What survives of the trade-off

The trade-off is **not** eliminated, only relocated. Three limits remain, stated honestly:

1. **A frontier still exists.** The best unsafe candidate reaches `J = 15.9`, 2.6× the
   best safe candidate. Requiring safety does cost information. The claim that dies is
   not "safety costs information" but "safety costs *most* of the information", and the
   specific numbers in the manuscript abstract.

2. **The safety constraint is active.** The refined optimum sits at margin +0.0500,
   exactly on the constraint boundary, and the Stage-2 winner at +0.0920. The safe
   historical design sits at +0.2921. The found designs buy accuracy by spending margin
   down to the declared tolerance δ. A stricter δ will give a worse objective — the
   Pareto curve is real, we have simply shown the manuscript was not on it.

3. **`latent3` remains the hard class.** Even the best design reaches recall 0.475 on
   the finite-latent rival against chance 0.25. This is consistent with Theorem T9b /
   the complexity law (R3-A): a sufficiently rich latent model is genuinely hard to
   exclude on a finite horizon, and no input design removes that obstruction. The part of
   the manuscript's pessimism that is *theoretically grounded* survives; the part that
   was an artifact of waveform choice does not.

4. **Scope of the search.** Fixed `α = 0.85`, `A = 0.25`, `T = 12`, both channels,
   `U_cap = 0.100`, `δ = 0.050`. Stage 1 is a Sobol + Nelder–Mead search, not a global
   optimisation: it produces *existence* of better safe designs, which is all the
   falsification requires, but it does **not** certify a global optimum. A certified
   global bound over the `pwc4` class (interval branch-and-bound) is listed as optional
   Stage 3 and is **not** done — see §6.

---

## 5. Consequences for the manuscript (mandatory)

These are corrections that R3-I must execute; they are not optional.

**C1 — Abstract.** The sentence
> "Safe identification of ecological memory is therefore constrained by an explicit
> safety–informativeness trade-off."

is not supported and must be replaced. The supported statement is that within classical
parametric waveform families the trade-off is severe, and that optimising the waveform
shape removes most of it. Reporting the six-family frontier as *the* frontier is a
parameterisation artifact.

**C2 — Abstract numbers.** The clause
> "PRBS and multisine discriminate best (0.584, 0.583) but cross the Allee threshold in
> 100% and 35.7% of stable cells, while the safest input (multiscale, 0% crossings)
> scores only 0.324"

is numerically correct (reproduced to four decimals, see R3-H) but is now *misleading by
omission*: a safe design scoring 0.803 exists at the same budget. Either the sentence
gains the counterexample or it goes.

**C3 — Discussion §3, "the most informative perturbation is not the safest, by a wide
margin".** False as a general statement. Must be scoped to the six-family study.

**C4 — Contributions and title.** The safety–informativeness trade-off cannot be a
headline contribution. The defensible headline is the opposite and stronger result:
*safe active design over an unrestricted piecewise-constant class recovers most of the
discrimination power, and the residual obstruction is the latent-complexity one, not the
safety one.* This is a better paper than the one submitted, and it is the version the
evidence supports.

**C5 — Figure 10 (`fig10_safety_tradeoff`).** The plotted frontier is the six-family
frontier. It must either be relabelled as such or redrawn with the search designs
included, which changes its shape qualitatively.

---

## 6. Not done / open

- **Stage 3 (certified global bound).** Interval branch-and-bound over `pwc4` to certify
  that no safe `pwc4` input exceeds a given `J`. Not executed. Without it we have
  existence, not optimality. This is honest scope, not a gap in the falsification.
- **Amplitude dependence.** The search was run only at `U_cap = 0.100`. Whether the
  advantage persists at 0.050/0.063 is untested. R3-H shows the historical designs behave
  *worse* relatively at low amplitude, so the expectation is that it does, but this is
  **inferred, not evidenced**.
- **Robustness of the found designs.** They were selected at `α = 0.85`; their
  performance across the `α` grid enters Stage 2 through the 56-cell grid, but they were
  not re-optimised per cell. A design tuned per-cell would do better; a design that must
  work without knowing `α` may do worse. Untested.

---

## 7. Artifacts

| file | content |
|---|---|
| `rescue_compute/r3f_safe_design_search.py` | Stage 1 search (Sobol + Nelder–Mead, multiprocessing) |
| `rescue_compute/r3f_stage2_bic.py` | Stage 2 BIC validation, 672 cells |
| `rescue_compute/r3_safe_design_search/r3f_summary.json` | Stage 1 protocol, baselines, per-family best |
| `rescue_compute/r3_safe_design_search/r3f_top12.json` | top-12 safe candidates with parameters |
| `rescue_compute/r3_safe_design_search/r3f_stage2_summary.json` | Stage 2 per-design accuracy, recall, safety |
| `rescue_compute/r3_safe_design_search/r3f_refined.json` | Nelder–Mead refinement traces |

Compute: Stage 1 on Orion (100 workers), Stage 2 on Orion (100 workers). Zero divergences
in 672 cells × 100 replicates.
