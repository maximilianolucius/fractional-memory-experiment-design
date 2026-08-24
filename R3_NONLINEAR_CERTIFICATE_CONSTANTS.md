# R3-C — Interval-certified safety constants

**Round 03, researcher deliverable.**
**Finding: Round 02's sampled constants were optimistic. Replacing sampling with interval
certification degrades every derived quantity by 5–19% and confirms the qualitative
conclusion: the invariant-ball certificate never engages the ecological margin.**

---

## 1. What was wrong with the Round-02 constants

`THEOREM_D_NONLINEAR_LIFT.md` §C1 obtained the quadratic-remainder constant

```
M₂(r) := sup_{‖ξ‖≤r} ‖R(ξ)‖ / ‖ξ‖²,     R(ξ) = f(z*+ξ) − Jξ
```

by **sampling** 720 directions × 40 radii. A sampled supremum is a *lower* bound. Using it
in a safety certificate is unsound: the certificate needs an upper bound on `M₂`, and a
lower bound makes the certified region look larger than it is.

## 2. Certified `M₂` (no sampling)

Certification route: Taylor with remainder gives
`‖R(ξ)‖ ≤ ½ · sup_{ball} ‖D²f‖ · ‖ξ‖²`, so it suffices to enclose the Hessian tensor of the
locked field over the ball. Both components are elementary — the cubic Allee term is
polynomial, the Holling term is rational with `1+hx > 0` on the region — so the second
partials have closed forms:

```
∂²f₁/∂x² = R(−6x/A + 2(1/A+1)) + 2ahy/(1+hx)³        ∂²f₁/∂x∂y = −a/(1+hx)²      ∂²f₁/∂y² = 0
∂²f₂/∂x² = −2eahy/(1+hx)³                            ∂²f₂/∂x∂y = ea/(1+hx)²      ∂²f₂/∂y² = 0
```

These are enclosed with `mpmath` interval arithmetic (40 digits) on a branch-and-bound cover
of the ball, and each symmetric `2×2` block is bounded in spectral norm by its maximum
absolute row sum. `A = 0.25`, `z* = (2/3, 10/9)`:

| r | `M₂` certified (upper) | `M₂` sampled (Round 02) | ratio |
|---:|---:|---:|---:|
| 0.0183 | **4.895659** | — | — |
| 0.05 | **5.467810** | 4.589 | 1.192 |
| 0.10 | **6.370688** | 4.891 | 1.303 |
| 0.20 | **8.171405** | 5.495 | 1.487 |
| 0.30 | **9.974847** | 6.100 | 1.635 |
| 0.3667 | **11.177401** | 6.504 | 1.719 |
| 0.40 | **11.777659** | 6.705 | 1.757 |

The sampled values understate `M₂` by 19% at `r = 0.05` and by 76% at `r = 0.40`. Part of
this is genuine (sampling misses the supremum) and part is conservatism of the Hessian
bound (it discards the direction of `R`, exactly as the Round-02 document already noted).
The certified column is the one that may be used in a certificate.

## 3. Derived constants

With `Γ_B = 5.7815`, `Γ_R = 6.2225` and the certified `M₂`, solving
`max_r (r − Γ_R M₂(r) r²)/Γ_B` subject to `r ≤ ρ(δ)` and `Γ_R M₂(r) r < 1`:

| δ | ρ(δ) = x*−A−δ | `r*` certified | `U_NL` certified | `U_NL` Round 02 | degradation |
|---:|---:|---:|---:|---:|---:|
| 0.02 | 0.3967 | 0.01642 | **0.001419** | 0.00149 | 4.7% |
| 0.05 | 0.3667 | 0.01641 | **0.001419** | 0.00151 | 6.0% |
| 0.10 | 0.3167 | 0.01642 | **0.001419** | 0.00150 | 5.4% |
| 0.20 | 0.2167 | 0.01641 | **0.001419** | 0.00151 | 6.0% |
| 0.30 | 0.1167 | 0.01641 | **0.001419** | 0.00151 | 6.0% |

```
certified r_max = 0.02937          (Round 02 claimed 0.0350 — an overestimate by 19%)
ρ(0.05)/r_max   = 12.5×            (Round 02 reported 10.5×)
```

`U_NL` remains flat in `δ` — the certificate is capped by `r_max`, not by the ecological
margin, confirming Round 02's diagnosis with sound constants.

## 4. Verdict

The Round-02 conclusion **survives certification and gets slightly worse**:

- the certifiable radius is `0.0294`, **12.5×** below the margin it is supposed to protect;
- the certified amplitude is `1.42e−3`, **2.2%** of the linear certificate `U_lin ≈ 0.0634`;
- combined with R3-G (which removes the double-counted gain), the testing floor inside this
  ball is `P_e^* ≥ 0.4984` even at `m = 4` — the certified regime cannot identify anything.

**The invariant-ball route to nonlinear safety is closed.** Not because the constants were
sloppy — certified, they are 5–19% worse — but because the method is structurally lossy for
this vector field. The usable route is validated integration at realistic amplitude (R3-D),
which certifies the `U = 0.100` designs that the invariant ball rejects by a factor of 70.

## 5. Honest status of each constant

| constant | value | status |
|---|---:|---|
| `x*`, `y*(A)`, `J(A)`, trace, det | exact | **closed form**, verified symbolically (`trace = −0.125`, `det = +0.250` reproduce `(7A−2)/(8A)`, `(2−3A)/(20A)`) |
| `‖J‖₂` | 0.566391 | exact (2×2 SVD) |
| `M₂(r)` | table §2 | **interval-certified upper bound** |
| `ρ(δ)` | `2/3 − A − δ` | exact |
| `Γ_B` | 5.7815 | **numerical quadrature, NOT certified** |
| `Γ_R` | 6.2225 | **numerical quadrature, NOT certified** |
| `r_max`, `U_NL` | §3 | certified *conditional* on `Γ_B`, `Γ_R` |

**Not done:** interval certification of `Γ_B` and `Γ_R`. These are suprema over `t ∈ [0,T]`
of integrals of the matrix Mittag-Leffler resolvent kernel; certifying them needs an enclosure
of `E_α(Jt^α)` in the operator norm, which is a separate piece of work. Until then, §3 is
"certified modulo two numerically computed gains", and that must be stated wherever these
numbers appear. Since the conclusion is negative (the certificate is useless), the missing
certification does not threaten any claim we make — but it would if anyone tried to use `U_NL`
as a positive safety guarantee.

## 6. Artifacts

| file | content |
|---|---|
| `rescue_compute/r3c_interval_constants.py` | Hessian enclosures, branch-and-bound, derived constants |
| `rescue_compute/r3c_M2_certified.json` | certified `M₂(r)` table |
| `rescue_compute/r3c_UNL_certified.json` | certified `r*`, `U_NL`, `r_max` per `δ` |
