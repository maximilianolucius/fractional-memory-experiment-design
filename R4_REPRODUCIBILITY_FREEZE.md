# R4-H — Reproducibility freeze

**Every headline number in the manuscript is traced here to a script, an artifact and a checksum.
No Round-03 output was overwritten in Round 04.**

---

## 1. Provenance rule enforced this round

Round-04 work is additive. The Round-03 artifacts listed in §3 were read but never rewritten; the
new files are `r4b_enclosure_results.json` and `fig24_safe_design_frontier.pdf`. The frozen v3
benchmark under `benchmark/results/` was not touched at any point in Rounds 01–04.

## 2. Environment

| host | role | python | numpy | scipy | other |
|---|---|---|---|---|---|
| local workstation | interval certification, response-level computation, enclosure, figures | 3.14.3 | 2.4.4 | 1.17.1 | matplotlib 3.10.9, mpmath 1.3.0 |
| Orion (100 workers) | waveform search stages 1–2, complexity-law sweep, v4 amplitudes 0.050/0.063 | 3.14.4 | 2.5.2 | 1.18.0 | — |
| Aureus (32 cores) | v4 amplitude 0.100 shard | as Orion | — | — | — |

The two `numpy`/`scipy` versions differ between hosts. That is not an accident to be hidden: it is
the reason the cross-host reproduction in §3 row 5 is meaningful — the frozen benchmark reproduces
to four decimals across *different* library versions, not merely on a second machine.

## 3. Headline claim → artifact map

| # | claim as printed | script | artifact | md5 (12) |
|---:|---|---|---|---|
| 1 | search evaluated 163 840 candidates, 87 601 safe; best safe `J=6.225`; all top-12 safe are piecewise-constant | `rescue_compute/r3f_safe_design_search.py` | `rescue_compute/r3_safe_design_search/r3f_summary.json` | `567d5f9bb7ab` |
| 2 | exact switching levels of the six leading designs | same | `…/r3f_top12.json` | `25f69d4accc5` |
| 3 | Stage-2 BIC validation: 12 designs, 56 cells × 100 reps, 0 divergences; macro 0.803 / 0.514 / 0.763; recalls 0.911, 0.853, 0.475 | `rescue_compute/r3f_stage2_bic.py` | `…/r3f_stage2_summary.json` | `dbd6bf810c68` |
| 4 | three-amplitude benchmark: macro 0.457 / 0.471 / 0.537; crossings 71.4 / 92.9 / 100 %; realised gain 28.07 vs `Γ_T=5.78` | `rescue_compute/v4_safe_benchmark.py` | `rescue_compute/r3_v4/v4_all_amplitudes.json` (+ the two raw `state_v4_*.jsonl`) | `d08536f9d1b4` |
| 5 | v4 @ 0.100 reproduces frozen v3 to four decimals (0.5369 vs 0.537; 0.5836 vs 0.584; 0.5829 vs 0.583; 0.3235 vs 0.324) | same | `rescue_compute/r3_v4/state_v4_amp100.jsonl` vs `benchmark/results/` | — |
| 6 | response-level `L¹` error to `m=128` (4.83e−5) and floors 0.4996 / 0.49999 | `rescue_compute/r3e_response_cert.py` | `rescue_compute/r3e_response_cert.json` | `e22ba5a4bb61` |
| 7 | kernel→response attenuation 1.009 → 0.675 | `rescue_compute/r3b_response_semantics.py` | recomputed on demand (deterministic, no RNG) | — |
| 8 | a posteriori verified safety, 28 trajectories, 12 safe / 16 crossing / 0 indeterminate | `rescue_compute/r3d_validated_safety.py` | `rescue_compute/r3d_validated_safety.json`, `r3d_pwc6.json` | `38394b8b21f3` |
| 9 | validated enclosure, 4 of 8 headline trajectories; rigorous lower bounds 0.441 and 0.309 | `rescue_compute/r4b_enclosure.py` | `rescue_compute/r4b_enclosure_results.json` | `d7490c2e1ae7` |
| 10 | `T^α` scaling to machine precision; bound active with `A ∈ [0.29, 11.1]`; `m(ε)` within a factor ~1.5 | `rescue_compute/c1_complexity_law.py` | `rescue_compute/c1_complexity_law.json` | `a3cbd1348946` |
| 11 | interval-certified `M₂(r)`; `r_max = 0.02937`; `U_NL = 1.419e−3` | `rescue_compute/r3c_interval_constants.py` | `rescue_compute/r3c_M2_certified.json`, `r3c_UNL_certified.json` | `b85fa16c6104` |
| 12 | headline figure | `benchmark/make_r4_headline_figure.py` | `paper/figures/fig24_safe_design_frontier.pdf` | — |

## 4. Exact parameters of the headline design

`pwc6`, six equal sub-intervals on `[0,12]`, switching levels in units of the peak budget
`U_cap = 0.100` (the raw Sobol coordinates `p` map to levels `2p−1`, then the whole waveform is
scaled so that `‖u‖_∞ = 0.100`, exactly as `bench.build_input` does):

```
p      = [0.756699881516397, 0.1325216805562377, 0.8458247799426317,
          0.7344822846353054, 0.14397935662418604, 0.32357181794941425]
levels = [+0.513, -0.735, +0.692, +0.469, -0.712, -0.353]   (units of U_cap)
```

Search protocol: `U_cap = 0.100`, `δ = 0.05`, `α = 0.85`, `A = 0.25`, `T = 12`, both channels,
objective `J(u) = min over class pairs ‖μ_a−μ_b‖/σ`. Stage-2 seeding: `seed = 1000 + 7919·k + ⌊100a⌋`
for replicate `k` at amplitude `a` — identical to the frozen benchmark's scheme, which is what
makes the comparison in row 3 like-for-like.

## 5. Reproduction sequence

```bash
# 1. kernel-level complexity law (285 cells, ~35 min on 60 workers)
python rescue_compute/c1_complexity_law.py

# 2. interval-certified nonlinear constants (local, ~2 min)
python rescue_compute/r3c_interval_constants.py

# 3. response-level error to m=128 (local, ~8 min)
python rescue_compute/r3e_response_cert.py

# 4. safe-design search, stage 1 then stage 2 (100 workers, ~35 + ~15 min)
python rescue_compute/r3f_safe_design_search.py
python rescue_compute/r3f_stage2_bic.py 100 100

# 5. three-amplitude benchmark (shard by amplitude via FMED_AMPS)
FMED_AMPS=0.050,0.063 python rescue_compute/v4_safe_benchmark.py     # Orion
FMED_AMPS=0.100       python rescue_compute/v4_safe_benchmark.py     # Aureus

# 6. safety verification and enclosure (local, ~25 + ~40 min)
python rescue_compute/r3d_validated_safety.py
python rescue_compute/r4b_enclosure.py

# 7. headline figure, then the manuscript
python benchmark/make_r4_headline_figure.py
bash paper/build_latex.sh          # -> exit 0, 25 pages
```

Steps 1–6 are order-independent. Step 7 requires 4, 6.

## 6. Determinism

| component | deterministic? |
|---|---|
| Sobol search (stage 1) | yes — `scipy.stats.qmc.Sobol` with a fixed seed; the candidate set is reproducible |
| Nelder–Mead refinement | yes — deterministic from each family's best Sobol point |
| BIC replicates | yes — explicit per-cell seed formula (§4) |
| interval certification, response-level computation, enclosure | yes — no RNG |
| `multiprocessing` result order | irrelevant — results are keyed, not appended positionally |

`scipy.optimize.nnls` in the complexity-law sweep can hit its iteration cap on a few cells; those
are caught and recorded rather than crashing the pool, so the artifact is complete but a handful of
cells carry the fallback value. This is in the code and is not hidden.

## 7. Not frozen

- No container image or lockfile. The two host environments are recorded in §2 but not pinned; a
  `requirements.txt` with exact versions would be the next step and is not done.
- The curated public deposit discussed in `R4_FORMAT_AND_ENDMATTER_AUDIT.md` §2 does not exist yet,
  so the data-availability statement currently says "on request" rather than naming a DOI.
