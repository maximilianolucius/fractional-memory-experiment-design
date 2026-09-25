# R6 — Interval certification of the response-level error at m = 64 and m = 128

**Status: DONE.** The m = 64 and m = 128 values that the manuscript previously labelled
"high-accuracy floating point, not enclosures" are now **interval-certified**, as are
m = 4 … 32 for the same surrogate. Computed on Aureus only (`nice -n 19`, 4 workers, < 50 MB RAM
per process, 31 s wall-clock at m = 128).

## Result

| m | certified `‖g_α − g_m‖_{L¹(0,12)} ≤` | R3-E float value | slack | certified `P_e* ≥` |
|---:|---:|---:|---:|---:|
| 4 | 1.286030822 | 1.286030 | 6e-7 | 0.2201702 |
| 8 | 0.4975068184 | 0.4975063 | 5e-7 | 0.3826592 |
| 16 | 0.1301656873 | 0.1301651 | 6e-7 | 0.4688745 |
| 32 | 0.02311313301 | 0.02311259 | 5e-7 | 0.4944677 |
| **64** | **0.001577778946** | 0.001577235 | 5e-7 (+0.03%) | **0.4996223** |
| **128** | **4.889029734e-5** | 4.834163e-5 | 5.5e-7 (+1.1%) | **0.4999883** |

Floors: exact two-point bound `Φ(−E·B/(2σ))`, `B = 0.120`, `σ = 0.10`, evaluated in Arb
(lower endpoint). Reported bounds are Arb upper endpoints inflated by 1e-9 relative for decimal
printing; floors are lower endpoints deflated by 1e-12.

## Why a direct approach fails, and the reduction used

At m = 128 the surrogate's rates span **λ ∈ [2.7e-35, 1.2e6]** (41 orders of magnitude). Ball
enclosures of `exp(A_w t)` for the 256-dimensional realisation blow up (`e^{‖A‖h}` with
`‖A‖ ≈ 1e6`), and double-precision eigensolvers cannot resolve roots of size 1e-35.

With `C = B = e₁`, `J = [[−1/8, −1/2], [1/2, 0]]` exactly (`J₂₂ = 0`):

```
G(s) = 4X / ((X − r₁)(X − r₂)),   X = s^{−α} or R_m(s) = Σ c_j/(s+λ_j),   r₁,₂ = −1/4 ± i√63/4
g_α = 2 Re[K φ_α],  φ_α(t) = −μ² t^{α−1} E_{α,α}(μ t^α),  μ = 1/r₁,  K = 4r₁/(r₁−r₂)
g_m = 2 Re[K φ_m],  φ_m(t) = Σ_p e^{pt}/R_m'(p),  R_m(p) = r₁   (m roots)
```

The δ-terms of the two conjugate branches cancel exactly. Self-check against the matrix formulas:
`g_α` scalar vs matrix Mittag-Leffler series agree to **2.7e-14**; `g_m` scalar vs the 2m-dimensional
realisation agree to **1.9e-15** (m = 16).

## Rigour, step by step

1. **Roots.** Seeds: eigenvalues of `M = −diag(λ) + c 1ᵀ/r₁` from Arb at 1024 bits (double precision
   failed at m = 32 — the smallest root is ~1e-17 there, ~4e-35 at m = 128). Each root is then
   enclosed in a box `X` with relative radius 2^-140 on which interval Newton
   `N(X) = p₀ − F(p₀)/F'(X) ⊂ X`, `0 ∉ F'(X)`, `F = R_m − r₁` — existence and uniqueness. All m boxes
   are pairwise disjoint, so these are **all** m roots of the degree-m polynomial `N − r₁D`, all simple.
   Every root has certified `Re p < 0` (max Re at m = 128: −3.8e-35). Roots re-verified in every worker.
2. **Point values** of `d = g_α − g_m`: Arb series for `E_{α,α}` with explicit geometric tail from
   Gautschi's inequality `Γ(β)/Γ(β+α) ≤ (β+α−1)^{−α}`.
3. **Per interval** `[a,b]`, `h = b − a`:
   `∫|d| ≤ h(|d(a)|+|d(b)|)/2 + h³/12 · sup|d''|`, with
   `sup|d''| ≤ 2|K| ( Σ_k |μ|^{k+2}|(β−1)(β−2)| sup t^{β−3}/Γ(β) + tail + Σ_p |p|²/|R'(p)| e^{Re p·a} )`.
   This avoids the dependency problem (the difference is 1e-6 of each term).
4. **Near zero** `[0, 2^-40]`: `∫|d| ≤ 2|K| (t₀ Σ_p 1/|R'(p)| + Σ_k |μ|^{k+2} t₀^β/Γ(β+1))` — 7e-11.
5. **Mesh**: graded (ratio 1+1/256) from 2^-40 to 0.0625, then uniform h = 2^-12; 55 297 intervals.
   Second-order term 5.5e-7 at every m (1.1% of the total at m = 128).
6. Partial sums transported between processes as exact mantissa/exponent pairs (no decimal rounding).

## What changed in the manuscript

- `sec3`: status paragraph rewritten — m = 64, 128 are now "also interval-certified"; a paragraph
  describes the reduction and the certificate.
- `sec5`: `tab:state-approx-large` now shows certified upper bounds and certified floors; the
  quadrature-error column is gone.
- Abstract, `sec1`, `sec10`, `sec11`, highlights, cover letter: "reaches 0.49999" → "exceeds 0.49998".
  The old wording rounded a *lower* bound (0.4999883) upward; the new wording is what is proved.
- `sec1` evidence sentence: surrogate errors are interval-certified at every latent order reported.

Build: exit 0, 0 LaTeX errors, 0 undefined references, 0 BibTeX warnings, 44 pages, abstract
244 words.

## Scope, stated exactly

- Certified for the **explicit surrogate** of Lemma `lem:soe` (coefficients stored as exact doubles in
  the JSON, `coeffs_c_hex`, `coeffs_lambda_hex`). Because it is one admissible element, the bound is an
  upper bound on the optimised-class `Ê_m^state`; the m ≤ 32 optimised-class enclosures of T23 are a
  separate, tighter computation.
- α = 0.85, A = 0.25, T = 12, prey channel only.

## Artifacts

`rescue_compute/r6_response_interval_cert.py`, `r6_response_interval_cert.json`,
`r6_response_interval_cert.log`.

## Open

The published reproducibility deposit (DOI 10.5281/zenodo.22087770) predates this certificate and
does **not** contain `r6_response_interval_cert.py`. The manuscript's claim is reproducible from the
repository, but not yet from the cited deposit. Fix: publish a new version of the deposit (new
version DOI, concept DOI unchanged) and cite it.
