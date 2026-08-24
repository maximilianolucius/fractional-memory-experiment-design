# R3-E — Response-level approximation at m = 64 and m = 128

**Round 03, researcher deliverable.**
**Finding: the response-level error is computed directly (not inferred from the kernel) out
to m = 128. The testing floor reaches 0.49999 — the finite-latent rival becomes exactly
indistinguishable. The manuscript's m ≤ 32 table understates the obstruction.**

The manuscript certifies `Ê_m^state` only up to `m = 32`. Round 02 attempted to extend the
claim by scaling the *kernel* error, which R3-B shows is invalid (the plant attenuates by a
factor that drifts from 1.01 to 0.675 over this range). This deliverable computes the
response-level quantity itself.

---

## 1. Method

Both impulse responses are constructed in closed form and compared in `L¹(0,T)`.

**Exact fractional response.** For the linearised plant `D^α ξ = Jξ + Bu`,
```
g_α(t) = C · t^{α−1} E_{α,α}(J t^α) · B
```
with the matrix two-parameter Mittag-Leffler function evaluated by its series, using
`lgamma` and periodic renormalisation of `J^k t^{αk}` to avoid overflow (the naive series
overflows at `k ≈ 200`).

**Latent surrogate response.** Substituting `s^{−α} → R_m(s) = Σ_j c_j/(s+λ_j)` (the
positive-weight SOE of Lemma B.2) realises a `2m`-dimensional LTI system
```
ẇ_j = −λ_j w_j + J(Σ_k c_k w_k) + Bu ,      ξ = Σ_j c_j w_j
```
whose impulse response is evaluated by one eigendecomposition of the `2m × 2m` generator
(256×256 at `m = 128`), then cheap exponential evaluation per time point.

`L¹` on a cubically graded mesh clustering at the singular endpoint; two mesh levels
(4000/8000 points) give the quadrature-error estimate.

`α = 0.85`, `A = 0.25`, `T = 12`, prey→prey channel.

## 2. Response-level error

| m | `‖g_α − g_m‖_{L¹(0,T)}` | quadrature err | relative |
|---:|---:|---:|---:|
| 4 | 1.286030e+00 | 2.13e−07 | 1.7e−07 |
| 8 | 4.975063e−01 | 1.01e−07 | 2.0e−07 |
| 16 | 1.301651e−01 | 7.60e−09 | 5.8e−08 |
| 32 | 2.311259e−02 | 3.03e−08 | 1.3e−06 |
| **64** | **1.577235e−03** | 2.13e−08 | 1.4e−05 |
| **128** | **4.834163e−05** | 6.33e−09 | 1.3e−04 |

Quadrature error is 5–7 orders of magnitude below the quantity at every `m`.

Consistency with the manuscript: T23 reports `Ê_m^state = 0.5335` at `m = 4` and `0.0070` at
`m = 32`, obtained as an **infimum** over the optimised class `𝒢_m` by interval arithmetic.
Mine is one *particular* surrogate, so it must be larger, and it is — by factors 2.4 and 3.3.
Both columns behave the same way; there is no inconsistency.

## 3. Induced testing floor at the manuscript protocol

`‖u‖₂ ≤ 0.120`, `σ = 0.10`, exact two-point Gaussian bound `Φ(−d/2)` (R3-G §1.1) alongside
the manuscript's Pinsker bound:

| m | `‖Δμ‖₂` | exact `P_e^*` ≥ | Pinsker `P_e^*` ≥ |
|---:|---:|---:|---:|
| 4 | 1.5432e−01 | 0.2202 | 0.1142 |
| 8 | 5.9701e−02 | 0.3827 | 0.3507 |
| 16 | 1.5620e−02 | 0.4689 | 0.4610 |
| 32 | 2.7735e−03 | 0.4945 | 0.4931 |
| **64** | 1.8927e−04 | **0.4996** | 0.4995 |
| **128** | 5.8010e−06 | **0.49999** | 0.49998 |

At `m = 64` the floor is within `4e−4` of chance; at `m = 128` within `1.2e−5`. **The
obstruction is complete well before `m = 128`,** and extending the table past `m = 32` — which
the manuscript does not do — is what makes that visible.

Note the direction: these floors use *my* surrogate, whose error exceeds the certified
infimum `Ê_m^state`. A smaller error gives a *higher* floor, so the true floors are at least
these values. The bound is therefore valid as stated and conservative.

## 4. What this changes

1. **The manuscript should extend its `Ê_m^state` table to `m = 64, 128`.** The story it tells
   — approximation error falls, testing floor rises to chance — is only half-visible when
   truncated at `m = 32` (floor 0.494). At `m = 128` the floor is 0.49999 and the conclusion
   is unambiguous.
2. **It also sharpens what the benchmark measures.** R3-H reports `latent3` recall of
   0.207–0.242 (at or below chance 0.25) at every amplitude. That is not a classifier defect:
   at the latent orders in play the classes are provably near-indistinguishable, and the
   benchmark is measuring exactly the obstruction this table quantifies.
3. **It bounds what R3-F can achieve.** The best safe design reaches `latent3` recall 0.475 —
   well above chance, so input design does help — but §3 shows no design can push it to 1 at
   large `m`. The residual obstruction is real and is the honest limitation to state in the
   paper, replacing the safety–informativeness claim that R3-F falsified.

## 5. Status and limitations

- **Not interval-certified.** These are high-accuracy floating-point computations with a
  two-mesh quadrature-error estimate, not enclosures. The chief asked for `m = 64, 128` "at
  response level, not kernel", which is done; making them interval-certified would require
  running them inside the T23 interval pipeline and is **not** done.
- **One surrogate, not the infimum.** §2 values are upper bounds on `Ê_m^state`. Reported as
  such; they make §3 conservative in the safe direction.
- **Mittag-Leffler series.** Truncated when the term drops below `1e−18` relative to the
  accumulated sum, with renormalisation. Not a rigorous tail bound.
- **Prey channel only, `α = 0.85` only.**

## 6. Artifacts

`rescue_compute/r3e_response_cert.py`, `rescue_compute/r3e_response_cert.json`.
