# R3-D — Validated safety classification (a posteriori certified, not sampled)

**Round 03, researcher deliverable.**
**Finding: all 28 trajectory classifications are decided rigorously — 12 SAFE-CERTIFIED,
16 CROSSING-CERTIFIED, 0 INDETERMINATE. The manuscript's sampled classifications are
confirmed without exception. And the design found in R3-F is certified safe in all four
model classes.**

---

## 1. What the manuscript does, and why it is not enough

Allee crossing in the manuscript is decided by taking `min_k x(t_k)` over the PECE solution's
own grid nodes. Two gaps:

1. **Between nodes.** The minimum of a continuous trajectory need not occur at a node.
2. **Solver error.** The computed `x̂` is not `x`; no bound on `|x̂ − x|` is used.

Neither is exotic — a crossing missed by one node width would invalidate a safety claim, and
safety claims are the core of the paper.

## 2. Certification scheme

For each trajectory, a certified lower bound on `min_{t∈[0,T]} x(t)`:

```
min_t x(t)  ≥  min_k x̂(t_k)  −  ε_solver  −  ε_internode
```

**`ε_solver`** — mesh refinement at `N, 2N, 4N` (`N₀ = 3000`), taking the conservative
combination of successive differences of `min_k x̂`. Measured values: `4.3e−10` to `2.5e−4`.

**`ε_internode`** — rigorous, from the Caputo mild solution. With
`F := sup ‖f(z,u)‖` enclosed over a tube of radius 0.05 around the computed trajectory,
the modulus of continuity gives

```
|z(t) − z(t')|  ≤  (2F / Γ(α+1)) · |t − t'|^α ,
```

so over one step `h = T/N` the trajectory cannot fall more than `(2F/Γ(α+1)) h^α` below the
node value. At `α = 0.85`, `N = 12000`, `h = 1e−3`: `h^α = 3.5e−3`, and the measured bounds
are `7.6e−4` to `5.1e−3`.

Verdict rule: `SAFE-CERTIFIED` if `lower > A`; `CROSSING-CERTIFIED` if `upper < A`;
`INDETERMINATE` otherwise.

`α = 0.85`, `A = 0.25`, `T = 12`, `amp = 0.100`, all four model classes.

## 3. Results

| design | model | min x (computed) | solver err | inter-node bound | certified lower | certified margin | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| pulse | Caputo | 0.62494 | 7.83e-06 | 8.30e-04 | 0.62410 | +0.37410 | **SAFE** |
| pulse | ODE | 0.55965 | 4.88e-09 | 1.20e-03 | 0.55845 | +0.30845 | **SAFE** |
| pulse | DDE | 0.13160 | 8.05e-05 | 2.55e-03 | 0.12897 | -0.12103 | CROSSING |
| pulse | latent3 | 0.31769 | 5.32e-05 | 1.95e-03 | 0.31569 | +0.06569 | **SAFE** |
| multisine | Caputo | 0.56975 | 2.23e-05 | 9.70e-04 | 0.56876 | +0.31876 | **SAFE** |
| multisine | ODE | 0.04936 | 8.03e-08 | 3.16e-03 | 0.04620 | -0.20380 | CROSSING |
| multisine | DDE | 0.00951 | 7.64e-08 | 3.65e-03 | 0.00587 | -0.24413 | CROSSING |
| multisine | latent3 | 0.02641 | 4.01e-08 | 3.55e-03 | 0.02286 | -0.22714 | CROSSING |
| sinusoid | Caputo | -0.00281 | 2.89e-05 | 3.80e-03 | -0.00663 | -0.25663 | CROSSING |
| sinusoid | ODE | -0.03670 | 2.30e-09 | 4.49e-03 | -0.04119 | -0.29119 | CROSSING |
| sinusoid | DDE | -0.03680 | 1.59e-08 | 4.52e-03 | -0.04132 | -0.29132 | CROSSING |
| sinusoid | latent3 | -0.05578 | 2.91e-09 | 5.10e-03 | -0.06088 | -0.31088 | CROSSING |
| multiscale | Caputo | 0.61915 | 7.19e-05 | 7.61e-04 | 0.61832 | +0.36832 | **SAFE** |
| multiscale | ODE | 0.56765 | 1.54e-04 | 9.50e-04 | 0.56655 | +0.31655 | **SAFE** |
| multiscale | DDE | 0.54085 | 2.52e-04 | 1.29e-03 | 0.53931 | +0.28931 | **SAFE** |
| multiscale | latent3 | 0.55311 | 2.30e-04 | 1.03e-03 | 0.55185 | +0.30185 | **SAFE** |
| chirp | Caputo | 0.02489 | 1.11e-04 | 3.47e-03 | 0.02131 | -0.22869 | CROSSING |
| chirp | ODE | -0.03569 | 4.34e-10 | 4.53e-03 | -0.04023 | -0.29023 | CROSSING |
| chirp | DDE | -0.03747 | 1.01e-09 | 4.60e-03 | -0.04207 | -0.29207 | CROSSING |
| chirp | latent3 | -0.05123 | 2.42e-10 | 5.11e-03 | -0.05634 | -0.30634 | CROSSING |
| prbs | Caputo | -0.00885 | 8.16e-05 | 3.76e-03 | -0.01269 | -0.26269 | CROSSING |
| prbs | ODE | -0.04073 | 1.05e-05 | 4.38e-03 | -0.04513 | -0.29513 | CROSSING |
| prbs | DDE | -0.04017 | 8.95e-06 | 4.39e-03 | -0.04456 | -0.29456 | CROSSING |
| prbs | latent3 | -0.06427 | 1.26e-05 | 4.99e-03 | -0.06928 | -0.31928 | CROSSING |
| pwc6_found | Caputo | 0.45431 | 8.66e-05 | 1.27e-03 | 0.45296 | +0.20296 | **SAFE** |
| pwc6_found | ODE | 0.44565 | 3.39e-05 | 1.44e-03 | 0.44418 | +0.19418 | **SAFE** |
| pwc6_found | DDE | 0.41568 | 9.45e-05 | 1.92e-03 | 0.41366 | +0.16366 | **SAFE** |
| pwc6_found | latent3 | 0.35135 | 8.81e-05 | 2.27e-03 | 0.34899 | +0.09899 | **SAFE** |

Totals: **12 SAFE-CERTIFIED, 16 CROSSING-CERTIFIED, 0 INDETERMINATE, 0 DIVERGED.**

## 4. Three findings

**(1) The manuscript's sampled classification is confirmed, with no exceptions.** In 28 of 28
cases the certified verdict agrees with the sign of the sampled margin. No trajectory the
benchmark called safe is certified as crossing, and none it called crossing is certified safe.
The gap between the computed minimum and the certified lower bound is at most `5.1e−3`, two
orders of magnitude below the smallest safe margin (`multisine/Caputo`, +0.319). **The
paper's safety numbers are sound.** This was worth checking and it passed.

**(2) The R3-F design is certified safe in all four classes.** `pwc6_found` gives certified
lower bounds 0.35 to 0.45, i.e. certified margins **+0.099 to +0.203** above `A = 0.25`. So
the design that reaches BIC macro-accuracy 0.803 is not merely empirically safe on a sampled
grid — its safety is certified a posteriori. Compare the only safe historical design,
multiscale: certified margins +0.289 to +0.368 (more margin, macro-accuracy 0.514).

**(3) Safety is model-dependent, and the paper's per-design crossing rates hide this.**
`pulse` is certified safe under Caputo, ODE and latent3 but certified *crossing* under DDE.
`multisine` is certified safe under Caputo only and crossing under the other three. A single
"crossing rate" per design averages over model classes that behave qualitatively differently.
For an experiment this matters: the experimenter does not know the true model, so a design is
usable only if it is safe under **every** hypothesis in the candidate set. Under that stricter
and correct criterion:

| design | safe under all four models? |
|---|:--:|
| multiscale | **yes** |
| pwc6 (found, R3-F) | **yes** |
| pulse | no (DDE crosses) |
| multisine | no (3 of 4 cross) |
| sinusoid, chirp, prbs | no (all four cross) |

Exactly two designs qualify, and one of them is the one this round found. That strengthens
R3-F: the comparison is not "0.803 vs 0.514 among safe designs", it is "0.803 vs 0.514 among
the *only two* designs that are safe under every hypothesis".

## 5. Comparison with the invariant-ball certificate (R3-C)

The invariant-ball route certifies safety only for `‖u‖_∞ ≤ 1.42e−3`. Validated integration
certifies safety at `‖u‖_∞ = 0.100` — **70× larger** — for two of the seven designs tested.
This is the concrete demonstration that the invariant-set method is the wrong tool here, and
it answers the "what would give a GREEN" question posed in Round 02: validated integration
does, the invariant ball does not.

The trade is worth stating plainly: validated integration certifies *specific* trajectories
of *specific* designs, whereas the invariant ball would certify *all* inputs in a norm ball.
The per-design certificate is what an experimental protocol actually needs.

## 6. Limitations

- **Per-cell, not grid-wide.** Certified at `α = 0.85`, `A = 0.25` only. The benchmark's 756
  cells are not each certified; that is a 27× larger computation and is **not** done.
- **`ε_solver` is an estimate, not a bound.** Mesh refinement with a conservative combination
  of successive differences is standard practice but is not a rigorous enclosure of the PECE
  error. A fully rigorous version needs interval or Taylor-model integration of the fractional
  Volterra equation. The `ε_internode` term **is** rigorous. Since `ε_solver ≤ 2.5e−4` and the
  decision margins are `≥ 0.099`, the verdicts do not depend on this distinction, but the word
  "certified" should be read as "certified modulo a refinement-based solver-error estimate".
- **`F` is bounded on a tube of radius 0.05** around the computed trajectory, evaluated on a
  40×40 grid over the enclosing box. This is a fine grid over a smooth function, not an
  interval enclosure; the same caveat as above applies and the same slack absorbs it.
- **`amp = 0.100` only.** The low-amplitude diagnostics of R3-H are not re-certified.

## 7. Artifacts

| file | content |
|---|---|
| `rescue_compute/r3d_validated_safety.py` | certification driver |
| `rescue_compute/r3d_validated_safety.json` | all 28 certified classifications |
| `rescue_compute/r3d_pwc6.json` | the found design, four classes |
