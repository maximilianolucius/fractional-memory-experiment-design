# Claim → artifact map

Every headline number in the paper, with the script that produces it and the file it lives in.
Paths are relative to the root of this package.

## Abstract

| value | where in the paper | artifact | key |
|---|---|---|---|
| `0.803` four-class accuracy, no crossings | abstract, Table (waveform search), Fig. 1 | `data/safe_design_search/r3f_stage2_summary.json` | `SEARCH#0_pwc6.macro`, `.cross_rate` |
| `0.514` only safe classical family | abstract, same table | same | `HIST_multiscale.macro` |
| `0.763` best classical of any kind, crosses `36%` | abstract, same table | same | `HIST_multisine.macro`, `.cross_rate` |
| `163 840` candidates evaluated | abstract, search subsection | `data/safe_design_search/r3f_summary.json` | `n_eval` (and `n_safe` = 87 601) |
| `71%` crossings at half amplitude | abstract, amplitude subsection | `data/benchmark_v4/v4_all_amplitudes.json` | `["0.05"].safety.prbs.cross_rate` |
| `5e-5` response error at `m=128` | abstract, response table | `data/r3e_response_cert.json` | `["128"].L1` |
| `0.49999` testing floor at `m=128` | abstract, response table | derived from the above: `Phi(-E*0.120/0.10/2)` | — |

## Waveform search and its validation

| claim | script | artifact |
|---|---|---|
| Stage-1 protocol, baselines re-scored, per-family best safe candidate | `code/rescue_compute/r3f_safe_design_search.py` | `data/safe_design_search/r3f_summary.json` |
| exact switching levels of the twelve best safe candidates | same | `data/safe_design_search/r3f_top12.json` |
| Nelder–Mead refinement traces | same | `data/safe_design_search/r3f_refined.json` |
| Stage-2 BIC validation, 672 cells × 100 replicates, 0 divergences | `code/rescue_compute/r3f_stage2_bic.py` | `data/safe_design_search/r3f_stage2_summary.json` (per design), `r3f_stage2.json` (per cell) |
| held-out test: searched designs lose `0.060` moving to `A=0.20`, classical lose `0.087` | derived from the per-cell file | `data/safe_design_search/r4j_leakage_test.json` |

## Benchmark

| claim | script | artifact |
|---|---|---|
| frozen four-class benchmark: macro `0.537`, prbs `0.584`, multisine `0.583`, multiscale `0.324` | `code/benchmark/run_all.py` | `data/benchmark_v3_frozen/nonlinear_confusion.json` |
| linear-Gaussian design ranking | same | `data/benchmark_v3_frozen/linear_factorial.json` |
| PECE solver validation against exact Mittag-Leffler | same | `data/benchmark_v3_frozen/solver_validation.json` |
| three amplitudes: macro `0.457 / 0.471 / 0.537`, crossing `71.4 / 92.9 / 100 %`, realised gain up to `28.07` vs `Gamma_T = 5.78` | `code/rescue_compute/v4_safe_benchmark.py` | `data/benchmark_v4/v4_all_amplitudes.json`, raw cells in the two `state_v4_*.jsonl` |
| cross-host reproduction of the frozen benchmark to four decimals | same, run on a second host | compare `state_v4_amp100.jsonl` with `benchmark_v3_frozen/` |

## Approximation and testing bounds

| claim | script | artifact |
|---|---|---|
| exact horizon scaling `E(T) = T^alpha E(1)` to machine precision, 285 cells | `code/rescue_compute/c1_complexity_law.py` | `data/c1_complexity_law.json` |
| root-exponential bound active with constants `0.29`–`11.1`; tight at `alpha=0.70, m=128` | same | same (`L1_err_nnls` column) |
| kernel-vs-response attenuation `1.009 -> 0.675` | `code/rescue_compute/r3b_response_semantics.py` | recomputed on demand (deterministic, no RNG) |
| response-level `L1` error `m = 4 … 128` and induced floors | `code/rescue_compute/r3e_response_cert.py` | `data/r3e_response_cert.json` |

## Safety

| claim | script | artifact |
|---|---|---|
| a posteriori verification, 28 trajectories: 12 safe, 16 crossing, 0 indeterminate | `code/rescue_compute/r3d_validated_safety.py` | `data/r3d_validated_safety.json`, `data/r3d_pwc6.json` |
| validated enclosure, 4 of 8 headline trajectories; rigorous lower bounds `0.441` and `0.309` | `code/rescue_compute/r4b_enclosure.py` | `data/r4b_enclosure_results.json` |
| interval-certified `M2(r)`; `r_max = 0.02937`; `U_NL = 1.419e-3` | `code/rescue_compute/r3c_interval_constants.py` | `data/r3c_M2_certified.json`, `data/r3c_UNL_certified.json` |

## Figure

| figure | script | file |
|---|---|---|
| safety–informativeness plane and per-class recall | `code/benchmark/make_r4_headline_figure.py` | `figures/fig24_safe_design_frontier.pdf` |

## Not in this package

Two quantities in the paper are computed inside the manuscript's own interval-arithmetic pipeline
rather than by a script here: the certified prey-response bounds for `m <= 32` and the
Matignon-boundary values inherited from the companion study. They are reported in the paper with
their status stated; everything else is above.
