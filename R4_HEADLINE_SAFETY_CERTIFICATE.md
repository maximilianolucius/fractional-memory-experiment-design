# R4-B — Headline safety status

## `RIGOROUS_CERTIFICATE = FAIL → MANUSCRIPT_DOWNGRADED`

4 of the 8 required trajectories now carry a genuine validated enclosure. 4 do not.
Per the chief's rule, no ambiguous middle status is allowed in the manuscript, so the
**fallback is applied globally**: all unqualified `certified` / `validated integration
certifies` language is replaced by `a posteriori verified` / `refinement-verified`, and
`+0.092` is never called a certified margin.

The partial success is reported here because it is real and because it identifies exactly
what a future round would have to fix.

---

## 1. What a genuine enclosure required, and what was built

R3-D was not a certificate: its solver error was a mesh-refinement estimate and its tube
bound was a fine-grid evaluation. Both are replaced here.

**Reference object.** `zhat` = piecewise **cubic Hermite** interpolant of the solver output,
built **per element** so the kink in `z'` at every input discontinuity is represented
exactly, on a mesh aligned to those discontinuities. Because `zhat` is an explicit
piecewise cubic, `min_t xhat(t)` is computed **exactly** (stationary points of each cubic
solved in closed form). The inter-node heuristic of R3-D disappears by construction.

**Defect.** `d = sup_t ‖zhat'(t) − f(zhat(t),u(t))‖`, bounded rigorously. Interval-evaluating
`d` directly loses the cancellation between `zhat'` and `f(zhat)` — the dependency problem —
and gives an `O(h)` bound four orders above the true defect. A second-order Taylor form on
16 sub-intervals per element is used instead, with the first two terms pointwise and only
`sup|d''|` bounded crudely by `K2 = 12 ≥ 2M₂ = 11.0` (the `M₂` interval-certified in R3-C):

```
|d(t)| ≤ |d(τ)| + |d'(τ)|·dt + ½ K2 dt²,     d' = zhat'' − Df(zhat) zhat',   dt = h/32
```

Measured convergence order 2.01, reaching `5.87e−09` at `N = 12000`.

**Amplification.** One-sided (log-norm) constant `μ = sup_tube λ_max(sym Df)`, bounded by
interval subdivision over the tube of radius `δ` around the whole piecewise-cubic path.
Gronwall then gives `‖e‖_∞ ≤ d·(e^{μT}−1)/μ`. Using `μ` rather than `‖Df‖` is what makes
this finite at all: `‖Df‖ = 1.62` would give `E_α`-type amplifications of order `10⁹`.

**Self-consistency.** The resulting bound `e` must satisfy `e ≤ δ`, the radius on which `μ`
and the field enclosures were computed (epsilon-inflation). A case that fails this is
reported as FAIL, not as a certificate.

## 2. Results, `α = 0.85`, `A = 0.25`, `T = 12`, `U = 0.100`, `δ = 0.05`, `N = 12000`

| design | model | defect | amplification | error bound `e` | `e ≤ δ` | certified lower bound on `min x` | status |
|---|---|---:|---:|---:|:--:|---:|---|
| pwc6 (found) | ODE | 5.87e−09 | 7.77e+05 | 4.56e−03 | yes | **0.44105** | **RIGOROUS — SAFE** |
| pwc6 (found) | latent3 | 5.87e−09 | 7.20e+06 | 4.22e−02 | yes | **0.30902** | **RIGOROUS — SAFE** |
| pwc6 (found) | DDE | 3.66e−06 | 2.39e+06 | 8.75e+00 | **no** | — | FAIL (not self-consistent) |
| pwc6 (found) | Caputo | — | — | — | — | — | not attempted rigorously |
| multiscale | ODE | 5.86e−09 | 3.32e+04 | 1.95e−04 | yes | **0.56729** | **RIGOROUS — SAFE** |
| multiscale | latent3 | 5.86e−09 | 4.03e+04 | 2.36e−04 | yes | **0.55270** | **RIGOROUS — SAFE** |
| multiscale | DDE | 2.08e−06 | 1.10e+05 | 2.29e−01 | **no** | — | FAIL (not self-consistent) |
| multiscale | Caputo | — | — | — | — | — | not attempted rigorously |

**Rigorous enclosures: 4 / 8.** For those four, safety is proved, not estimated: the found
`pwc6` design keeps prey above `0.441` under ODE and above `0.309` under latent3, i.e.
rigorous margins of `+0.191` and `+0.059` over `A = 0.25`.

## 3. Why the other four fail, precisely

**DDE (2 trajectories).** The defect stalls at `O(h)`, three orders above the ODE/latent3
defect at the same `N`. Diagnosis is exact, not speculative: the defect is concentrated in
five elements, at

```
t = 2.348, 4.348, 6.348, 8.348, 10.348     i.e.  t = (input jump) + τ,  τ = 0.35
```

with median defect over all other elements `4.6e−12`. The delayed argument `z(t−τ)` reaches
back to an input jump, where `z'` has two one-sided values; the history interpolant must
therefore carry **per-element** endpoint derivatives. Switching the history from linear to
cubic Hermite improved the defect by 3× and switching to per-element derivatives improved it
again, but the order stays at 1 — the remaining error is the propagation of the jump into the
delayed term itself, which needs the history to be split at every `jump + kτ` inside the
history evaluation, not merely at mesh level. That is a mechanical fix and is **not done**.

**Caputo (2 trajectories).** Not attempted rigorously. The fractional defect
`D^α zhat − f(zhat)` is `O(N²)` to evaluate and, more importantly, is limited by the PECE
solver's own order (`≈ 1+α = 1.85`): at `h = 10⁻³` the defect would be `≈ 10⁻⁵`, and with the
Caputo amplification `(T^α/Γ(α+1))·E_α(μT^α) ≈ 1.5e+06` the bound is `≈ 15`, useless. Closing
Caputo requires a **higher-order reference** — product-integration collocation on a graded
mesh, or deferred correction of the PECE output — which is a distinct piece of work.

## 4. What the manuscript now says

Downgrade applied globally (see `R4_FORMAT_AND_ENDMATTER_AUDIT.md` for the diff list):

| before | after |
|---|---|
| "validated integration certifies these trajectories" | "a posteriori verified by mesh refinement with a rigorous inter-node modulus" |
| "certified margin +0.092" | "verified margin +0.092 (refinement-based solver-error control)" |
| "12 SAFE-CERTIFIED" | "12 verified safe" |
| Fig./table labels "certified" | "verified" |

The four genuine enclosures of §2 are reported separately and explicitly, with the word
"rigorous" reserved for them alone.

## 5. Honest cost of the downgrade

The headline result does **not** depend on this. The falsification in R3-F is empirical: the
`pwc6` design attains BIC macro-accuracy `0.803` with zero observed crossings across
56 cells × 100 replicates, against `0.514` for the only safe classical design. That comparison
is unaffected by whether the safety of two of the four hypothesis-classes is *certified* or
*verified*. What the downgrade costs is the stronger sentence "safety is certified", which we
are not entitled to write for DDE and Caputo, and now do not.

## 6. Artifacts

| file | content |
|---|---|
| `rescue_compute/r4b_enclosure.py` | the enclosure (interval field/`μ`/Hermite/defect/Gronwall) |
| `rescue_compute/r4b_enclosure_results.json` | all 8 cases with every intermediate quantity |
| `rescue_compute/r3d_validated_safety.py` | the refinement-verified pass, still used for the other 20 cases |
