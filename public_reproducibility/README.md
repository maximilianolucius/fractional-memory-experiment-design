# Reproducibility package

Code and numerical artifacts supporting

> **Safe discrimination of fractional, delayed, and latent memory beyond classical
> waveforms in a strong-Allee predator–prey model**
> I. Alraddadi

Everything reported in the paper is reproducible from this package. The frozen outputs in
`data/` are the exact files the manuscript's tables and figures were generated from, so the
numbers can be checked without re-running any computation.

---

## Layout

```
code/benchmark/        solvers, model definitions, waveform families, benchmark driver, figures
code/rescue_compute/   the computations behind the headline claims (search, certification,
                       response-level approximation, validated enclosure)
data/                  frozen machine-readable outputs used by the manuscript
data/benchmark_v3_frozen/   the frozen four-class benchmark (1512 cells x 200 replicates)
data/benchmark_v4/          the three-amplitude benchmark (2268 cells, no divergences)
data/safe_design_search/    waveform search: candidates, refinement, BIC validation, held-out test
figures/               the headline figure as published
requirements.txt       library versions used
CLAIM_ARTIFACT_MAP.md  every headline number -> script + artifact
MANIFEST_SHA256.txt    checksums for every file here
```

## Checking the numbers without recomputing

Each entry in `CLAIM_ARTIFACT_MAP.md` names the artifact and the key holding the value. For
example, the headline comparison:

```bash
python3 - <<'PY'
import json
s = json.load(open("data/safe_design_search/r3f_stage2_summary.json"))
for k in ("SEARCH#0_pwc6", "HIST_multiscale", "HIST_multisine"):
    v = s[k]
    print(f"{k:>18}  macro={v['macro']:.4f}  crossing={v['cross_rate']:.3f}  margin={v['min_margin']:+.4f}")
PY
```

prints `0.8030 / 0.000`, `0.5141 / 0.000` and `0.7628 / 0.357` — the three numbers in the abstract.

## Re-running

From `code/`, with `requirements.txt` installed. Steps 1–6 are independent of each other;
step 7 needs 4 and 6. Wall-clock figures are for the hardware described in `requirements.txt`.

```bash
cd code

# 1. kernel-level complexity law: 285 cells               (~35 min, 60 workers)
python3 rescue_compute/c1_complexity_law.py

# 2. interval-certified nonlinear constants               (~2 min, single core)
python3 rescue_compute/r3c_interval_constants.py

# 3. prey-response approximation error to m=128           (~8 min, single core)
python3 rescue_compute/r3e_response_cert.py

# 4. waveform search: 163,840 candidates, then BIC validation
python3 rescue_compute/r3f_safe_design_search.py         # (~35 min, 100 workers)
python3 rescue_compute/r3f_stage2_bic.py 100 100         # (~15 min, 100 workers)

# 5. three-amplitude benchmark, shard by amplitude
FMED_AMPS=0.050,0.063 python3 rescue_compute/v4_safe_benchmark.py
FMED_AMPS=0.100       python3 rescue_compute/v4_safe_benchmark.py

# 6. trajectory safety: a posteriori verification, then validated enclosure
python3 rescue_compute/r3d_validated_safety.py           # (~25 min)
python3 rescue_compute/r4b_enclosure.py                  # (~40 min)

# 7. the headline figure
python3 benchmark/make_r4_headline_figure.py
```

The scripts locate `benchmark/` by relative path from their own location, so run them from
`code/` as shown. Outputs are written next to the corresponding inputs; to compare against the
frozen values, copy `data/` aside first.

## Determinism

| component | deterministic |
|---|---|
| Sobol search | yes — `scipy.stats.qmc.Sobol(scramble=True, seed=12345)` |
| Nelder–Mead refinement | yes — starts from each family's best Sobol point |
| BIC replicates | yes — per-cell seed `1000 + 7919*k + floor(100*amp)` |
| interval certification, response-level computation, enclosure | yes — no RNG |

`scipy.optimize.nnls` can reach its iteration cap on a few cells of the complexity-law sweep.
Those cells are caught and recorded rather than aborting the pool, so the artifact is complete
with a fallback value on a handful of entries.

## The headline waveform

Six-level piecewise-constant input on six equal sub-intervals of `[0, 12]`. The Sobol
coordinates `p` map to levels `2p - 1`, and the waveform is then scaled so `||u||_inf = 0.100`
exactly as `bench.build_input` does:

```
p      = [0.756699881516397, 0.1325216805562377, 0.8458247799426317,
          0.7344822846353054, 0.14397935662418604, 0.32357181794941425]
levels = [+0.513, -0.735, +0.692, +0.469, -0.712, -0.353]   (units of the peak budget)
```

Search configuration: peak budget `0.100`, required margin `delta = 0.05`, `alpha = 0.85`,
`A = 0.25`, `T = 12`, both observation channels, objective
`J(u) = min over class pairs ||mu_a - mu_b|| / sigma`.

## One label to be aware of

The four candidate classes are `ODE`, `Caputo`, `DDE`, `latent3`. The **data-generating** set
contains latent generators of two orders, `latent1` and `latent3`, both scored against the single
`latent3` hypothesis. So in every class-wise statistic the latent class is **pooled** over the two
generators. The raw files keep the original generator labels (`true` field), so the pooling can be
undone by anyone who wants the per-order breakdown.

## Licences

Code under MIT (`LICENSE-CODE.txt`); data and figures under CC BY 4.0 (`LICENSE-DATA.txt`).
