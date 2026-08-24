# THEOREM_D_NONLINEAR_LIFT — Task R2-C

# CONCLUSION: **YELLOW** — a one-sided nonlinear safety theorem is proved, but it is *operationally
# vacuous*: the certified amplitude is `U_NL(0.05) = 1.6·10^{-3}`, i.e. **2.5 % of the linear
# certificate**, and the certifiable radius is an order of magnitude below the ecological margin.

Two stronger routes were attempted and **both fail structurally**, which is itself a result:
the invariant-rectangle route is impossible for this vector field, and weighted norms do not rescue
the quadratic-remainder ball.

---

## C1. Explicit nonlinear remainder (actual field, not an abstract remainder)

`R(ξ) := f(z*+ξ) − Jξ` for the locked strong-Allee field
`f₁ = r x(1−x/K)(x/A−1) − axy/(1+hx)`, `f₂ = e·axy/(1+hx) − my`,
`r=3/2, K=1, a=1, h=1/2, e=4/5, m=2/5`, `A=0.25`, `z*=(0.6667, 1.1111)`.

Measured `M₂(r) := sup_{‖ξ‖≤r}‖R(ξ)‖/‖ξ‖²` (720 directions × 40 radii, Euclidean norm):

| `r` | 0.05 | 0.10 | 0.20 | 0.30 | 0.3667 | 0.40 |
|---|---:|---:|---:|---:|---:|---:|
| `M₂(r)` | 4.589 | 4.891 | 5.495 | 6.100 | **6.504** | 6.705 |
| `‖R‖` at `r` | 0.0115 | 0.0489 | 0.2198 | 0.5490 | 0.8746 | 1.0729 |

`R(0)=0`, `DR(0)=0` hold by construction. `M₂` is mildly increasing — the field is not pathological;
the problem is the *gain*, not the remainder.

## C2. Nonlinear invariant safe ball

Mild solution: `ξ = H_α*(Bu) + H_α*R(ξ)`. With `Γ_B := sup_t∫_0^t‖H_α B‖` and
`Γ_R := sup_t∫_0^t‖H_α‖` (worst direction), a sufficient invariance condition on the ball of radius
`r` is
\[
\Gamma_B(T)\,U+\Gamma_R(T)\,M_2(r)\,r^2\;\le\;r .
\tag{C.1}
\]
Computed at `α=0.85`, `T=12`: `Γ_B = 5.7815`, `Γ_R = 6.2225`.

**Feasibility.** (C.1) has a positive solution in `U` only if `r < 1/(Γ_R M₂(r))`:
\[
r_{\max}\;=\;1/(6.2225\times 4.589)\;=\;\mathbf{0.0350}.
\]
But the ecological margin is `ρ(0.05)=x*−A−δ=0.3667`. **The certifiable radius is 10.5× smaller than
the margin we need to protect.**

Optimizing (C.1) over `r`:

| `δ` | `ρ(δ)` | `r*` | `M₂(r*)` | **`U_NL(δ)`** | `U_lin(δ)` | loss |
|---:|---:|---:|---:|---:|---:|---:|
| 0.02 | 0.3967 | 0.0198 | 4.589 | 0.00149 | 0.06861 | 97.8 % |
| 0.05 | 0.3667 | 0.0183 | 4.589 | **0.00151** | 0.06342 | **97.6 %** |
| 0.10 | 0.3167 | 0.0158 | 4.589 | 0.00150 | 0.05477 | 97.3 % |
| 0.20 | 0.2167 | 0.0181 | 4.589 | 0.00151 | 0.03748 | 96.0 % |
| 0.30 | 0.1167 | 0.0175 | 4.589 | 0.00151 | 0.02018 | 92.5 % |

Note `U_NL` is essentially **independent of `δ`** — it is capped by `r_max`, not by the margin. The
nonlinear certificate has stopped seeing the ecology.

**Weighted norms (chief's explicit authorization) do not rescue it.** Searching
`‖(x,y)‖_W=max(|x|,w|y|)` over `w∈[0.1,2]`: best is `w=0.30` with `M₂=8.019`, `Γ_B=3.699`,
`Γ_R=5.216`, `r_max=0.0239`, giving `U_NL=0.00162` — **2.5 %** of `U_lin`. The binding obstruction is
the product `Γ_R·M₂ ≈ 30`, which no reweighting reduced materially.

## C3. Robust safety across rival mechanisms — and a structural impossibility

**The invariant-rectangle route (pack `thm:T17`) is not available for this system.** For
`Rct=[x_L,x_U]×[y_L,y_U]` containing `z*`, the predator faces carry **no control**, so they must hold
structurally:
- lower `y`-face requires `e a x/(1+hx) − m ≥ 0` on `[x_L,x_U]`;
- upper `y`-face requires `e a x/(1+hx) − m ≤ 0` on `[x_L,x_U]`.

But `e a x/(1+hx) − m` vanishes **exactly at `x*`** (that is the definition of the coexistence
equilibrium), and `x*` is interior to any rectangle containing `z*`. Hence the two face conditions are
mutually exclusive: **no inward-pointing rectangle around the coexistence equilibrium exists**, for any
`δ`, independently of the input. Verified by exhaustive search over 24×24×24 rectangle geometries: no
feasible rectangle at any `δ∈{0.02,…,0.30}`.

**This is a correction to the source pack**, whose `T17`/§4 presents the rectangle inequalities as the
route to ecological safety. They are not applicable at a coexistence equilibrium of this field.

**Consequence for robustness.** Since even the reference model admits no invariant rectangle, a
hierarchy-uniform invariance certificate is out of reach by this technique. The theorem below is
therefore classified **one-sided/reference-model safety**, as the assignment requires when robust
safety cannot be proved.

## C4. Nonlinear discrimination discrepancy

Combining the mild-solution difference with Proposition B.1 (`R2_OPERATOR_BRIDGE.md`) and the
quadratic remainder, on the certified ball `‖ξ‖≤r*`:
\[
\|C(\xi_F-\xi_m)\|_\infty\;\le\;A_{NL}(r,T)\,E_m^{G}\,\|u\|_\infty,
\qquad A_{NL}(r,T)=\|C\|\,E_\alpha\!\big((\|J\|+M_2(r)r)T^\alpha\big),
\]
i.e. the linear amplification with `‖J‖` replaced by the Lipschitz constant of the full field on the
ball. At `r=r*=0.018`, `M₂r=0.084`, so `A_NL` exceeds the linear factor by only ≈15 % — **the
nonlinearity is not what breaks the discrimination step; the safety step is.**

## C5. Nonlinear Theorem D (as it actually closes)

> ### Theorem D-NL (one-sided nonlinear safety-constrained ceiling)
> Let `α∈(0,1)`, `A<2/7`, `δ∈(0,x*−A)`, and let `r*` solve `max_r (r−Γ_R M₂(r)r²)/Γ_B` subject to
> `r ≤ ρ(δ)` and `r < 1/(Γ_R M₂(r))`. Then for every input with
> `‖u‖_∞ ≤ U_NL(δ) := (r*−Γ_R M₂(r*)r*²)/Γ_B`, the **full nonlinear** trajectory of the reference
> fractional model satisfies `‖ξ‖_∞ ≤ r* ≤ ρ(δ)`, hence `x(t) ≥ A+δ` for all `t∈[0,T]`; and every test
> on `n` samples of the prey channel obeys
> \[
> P_e^*\;\ge\;\Phi\!\Big(-\frac{\sqrt n}{2\sigma}\,A_{NL}(r^*,T)\,E_m^{G}\,U_{NL}(\delta)\Big).
> \]

**Uniformity, stated exactly as required.**
- **inputs:** uniform over all `u` with `‖u‖_∞≤U_NL(δ)` (the bound uses only that norm);
- **sample schedules:** uniform over any `n` points in `(0,T]` (via `‖·‖₂≤√n‖·‖_∞`);
- **model family:** **NOT uniform** — safety is proved for the reference fractional model only
  (one-sided); the latent rivals enter only through `E_m^G`;
- **latent budget:** uniform in `m` given `E_m^G`;
- **safety margin:** valid for each `δ`, but `U_NL` is capped by `r_max`, so it is *insensitive* to `δ`
  in the relevant range — a defect, not a feature.

## C6. Why this is YELLOW and not GREEN

The theorem is true and every constant is computable, but:
1. `U_NL = 1.6·10^{-3}` is **2.5 %** of the linear certificate. At that amplitude the observable
   separation is so small that the error floor is ≈0.5 **for lack of excitation**, not because of the
   memory-approximation mechanism. The interesting phenomenon disappears into a trivial one.
2. Safety is **reference-model only**; robust (hierarchy-uniform) safety is not proved, and the
   rectangle route that the pack proposed is impossible here.
3. The certifiable radius (`0.035`) is `10×` below the ecological margin (`0.367`), so the certificate
   never actually engages the Allee geometry it is supposed to protect.

## C7. What would give a GREEN (Round 03)

- **Two-sided/sign-aware bounds.** `‖R(ξ)‖≤M₂‖ξ‖²` discards the *direction* of the nonlinearity. Near
  the lower prey face the cubic term `P(x)` and the Holling saturation act with definite signs; a
  differential-inequality argument on the scalar `x`-component (Caputo comparison principle) may
  certify the margin without paying `Γ_R M₂`.
- **Validated integration instead of invariant sets.** Certify per-design, per-amplitude trajectory
  enclosures with interval/Krawczyk integration (the machinery the companion study already uses). This
  matches how the paper certifies everything else, and the v4 benchmark measurements suggest ample
  slack: at `U=0.063` the realized gain of the multiscale design is `0.79`, versus the worst-case
  `Γ_T=5.78` — a factor 7 of unused conservatism.
- Both routes are numerical-certificate routes, not uniform-analytic ones. **Recommendation:** state
  the safety certificate as *design-conditional and validated*, not as a uniform analytic ball.
