# THEOREM_C_TESTING_OBSTRUCTION — Round 01, Task 5

**Mandate:** derive the statistical lower bound from first principles for the *actual* observation
model; inherit no constants. Done below. Two concrete defects of the current `thm:T20` are identified
and both are fixable in a way that makes the theorem **stronger**, not weaker.

---

## 1. Current statement (`thm:T20`)

> If the admissible experiment class satisfies `‖u‖₂ ≤ B`, then the composite minimax error for
> testing the fractional response against a latent hierarchy containing an explicit competitor with
> error `Ê_m` obeys `P_e*(m) ≥ Ψ(C_obs Ê_m² B²)`, where `Ψ` is any valid equal-covariance Gaussian
> two-point lower bound (Pinsker is used in the numerical plots). Thus `P_e*(m) → 1/2` whenever
> `Ê_m → 0` and `B` remains bounded.

**Defect 1 — `Ψ` is unspecified.** "Any valid bound" is not a falsifiable statement, and the constant
`C_obs` is never given. A referee cannot check the numbers in the figures.

**Defect 2 — norm mismatch.** The input budget is `‖u‖₂ ≤ B` (an `L²` budget). Pairing an `L²` input
budget with a kernel error through Young/Cauchy–Schwarz requires `‖k_α−k_m‖_{L²(0,T)}`. But

  `k_α(t)=t^{α−1}/Γ(α) ∈ L²(0,T) ⟺ 2(α−1) > −1 ⟺ **α > 1/2**`.

Verified numerically: at `T=12`, `‖k_α‖_{L²}` **diverges** for `α = 0.30, 0.50` while the `L¹` norm is
finite for every `α∈(0,1)` (2.35, 3.91 respectively). **Any bound routed through the `L²` kernel norm
is vacuous for `α ≤ 1/2`**, although the theorem is asserted for `0<α<1`. The benchmark only uses
`α ∈ {0.70,0.85,0.95}`, so the *numbers* are safe — the *statement* is not.

---

## 2. Exact observation model (as implemented)

`y_k = μ(t_k) + ε_k`, `ε_k ~ N(0, σ²)` i.i.d., `k = 1,…,n`, sample times `t_k ∈ (0,T]`;
`μ(t) = (C ξ)(t)` on the collocated prey channel; both hypotheses share the same input `u`, the same
sampling design and the same covariance `σ²I_n`. In the frozen v3 benchmark: `n = 120`, `T = 12`,
noise set by SNR.

Hypotheses: `H_1` fractional kernel `k_α`; `H_2` best `m`-mode positive latent surrogate `k_m`.

## 3. Derivation from first principles

**Step 1 — exact Bayes error (no inequality).** For two simple Gaussian hypotheses with common
covariance `σ²I` and equal priors, the log-likelihood ratio is affine in `y`; projecting on the
normalized discriminant direction reduces the problem to two univariate normals with equal variance
whose means differ by `d`, and the optimal threshold is the midpoint. Hence **exactly**

  `P_e* = Φ(−d/2)`,  `d² = Σ_{k=1}^n Δμ(t_k)² / σ² = ‖Δμ‖₂²/σ²`,  `Δμ := μ_1 − μ_2`.

**Step 2 — kernel error to output discrepancy.** `Δμ = (k_α − k_m) * u` on the prey channel. Two
admissible routes:

| Route | Inequality | Validity |
|---|---|---|
| **A (recommended)** | `‖Δμ‖_∞ ≤ ‖k_α−k_m‖_{L¹(0,T)} · ‖u‖_∞` | **all `α∈(0,1)`** (`L¹` norm always finite) |
| B (current) | `‖Δμ‖_∞ ≤ ‖k_α−k_m‖_{L²(0,T)} · ‖u‖_{L²}` | **only `α>1/2`** |

**Step 3 — sampling.** `‖Δμ‖₂ ≤ √n ‖Δμ‖_∞`, hence with route A and `‖u‖_∞ ≤ U`:

  `d ≤ √n · ε_m^{(1)} · U / σ`,  `ε_m^{(1)} := ‖k_α−k_m‖_{L¹(0,T)}`.

**Step 4 — the bound.** `Φ` is decreasing, so

> ### Theorem C′ (uniform finite-experiment testing obstruction)
> For the observation model of §2, every test satisfies
> \[
> P_e^* \;\ge\; \Phi\!\Big(-\tfrac12\,\sqrt{n}\;\varepsilon_m^{(1)}\,U/\sigma\Big),
> \]
> **uniformly over every admissible input with `‖u‖_∞ ≤ U`** and every sampling design with `n`
> points in `(0,T]`. If `‖C‖≠1`, multiply `ε_m^{(1)}` by `‖C‖`. Consequently `ε_m^{(1)} → 0` with
> `n, U, σ, T` fixed forces `P_e* → 1/2`.

**Refinement (tighter, if the sampling is quasi-uniform).** Replacing `‖Δμ‖₂ ≤ √n‖Δμ‖_∞` by a
quadrature estimate `Σ_k Δμ(t_k)² ≈ (n/T)∫_0^T Δμ²` gives
`d² ≲ (n/(Tσ²))·‖k_α−k_m‖_{L¹}²·‖u‖_{L²}²`, which is sharper when `Δμ` is not concentrated at a few
samples.

## 4. Answering the required output items

1. **Exact observation model** — §2.
2. **Exact lower bound** — Theorem C′, `Φ(−½√n ε_m U/σ)`.
3. **Dependence** — `m` only through `ε_m^{(1)}`; `T` through `ε_m^{(1)}` and the sampling window;
   `U` linearly; `σ` inversely; `n` as `√n`; `C_obs` as the multiplicative factor `‖C‖`. No hidden
   constants remain.
4. **Uniformity** — **yes, and provably so**: the bound depends on the input *only* through `‖u‖_∞`.
   No admissible input escapes it. This is the property the manuscript asserts but never isolates.
5. **Tightness** — the two lossy steps are Young (route A) and `‖·‖₂ ≤ √n‖·‖_∞`. In the
   small-discrepancy regime that matters (`d→0`) the bound behaves as `1/2 − 0.19947·d`, so it is
   tight to first order in `d`; the slack is a constant factor, not an order.
6. **Stronger bound than generic Pinsker — yes.** Verified numerically:

| `d` | exact `Φ(−d/2)` | Pinsker `(1−√(KL/2))/2` | gain |
|---:|---:|---:|---:|
| 0.10 | 0.48006 | 0.47500 | +0.0051 |
| 0.50 | 0.40129 | 0.37500 | +0.0263 |
| 1.00 | 0.30854 | 0.25000 | +0.0585 |
| 2.00 | 0.15866 | **0.00000 (vacuous)** | +0.1587 |

Expansions: exact `= 1/2 − d/(2√(2π)) = 1/2 − 0.19947 d`; Pinsker `= 1/2 − d/4 = 1/2 − 0.25 d`. The
**exact bound is strictly stronger for every `d>0`**, and Pinsker becomes vacuous at `d ≥ 2√2` while
the exact bound stays informative. **Recommendation: drop Pinsker entirely from the plots and the
theorem; use `Φ(−d/2)`.** This is a free strengthening of the paper's central obstruction.

## 5. Required corrections to `thm:T20`

1. Replace `Ψ` by the explicit exact bound `Φ(−½√n ε_m U/σ)`; delete "any valid bound".
2. Switch the input budget from `‖u‖₂ ≤ B` to **`‖u‖_∞ ≤ U`** (route A), which (a) is valid for all
   `α∈(0,1)`, and (b) is the *safety-relevant* budget — the same `U` that Theorem D constrains. If the
   `L²` budget is kept for other reasons, restrict the theorem to `α>1/2` **explicitly**.
3. Give `C_obs` a definition (`‖C‖`) instead of leaving it symbolic.
4. State the uniformity claim as part of the theorem, since that is what makes it an *obstruction*
   rather than a statement about one experiment.
5. Note that `ε_m^{(1)}` is supplied by the approximation layer (Theorem B) and that its **rate** is
   what turns this into a complexity law — see `THEOREM_B_COMPLEXITY_LAW.md`.

## 6. Recommendation

**Headline-supporting theorem, upgraded.** Theorem C′ is correct, uniform, constant-explicit, valid
for all `α∈(0,1)`, and strictly stronger than the version in the manuscript. It is *not* novel as a
technique (exact Gaussian two-point testing is textbook, e.g. Van Trees; Kay) — its value is as the
rigorous bridge between the approximation layer and the safety layer. Novelty must be claimed for the
**composite** with Theorem D, not for this step.
