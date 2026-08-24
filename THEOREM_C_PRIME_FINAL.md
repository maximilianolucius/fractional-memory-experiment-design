# THEOREM_C_PRIME_FINAL — Task R2-E (testing theorem at the correct operator level)

Rewritten with the **observed response discrepancy** `E_m^G`, per Gate B. All six required checks are
answered explicitly, including the one that forces me to withdraw a Round-01 tightness claim.

---

## 1. Observation model and sampling map

State `ξ` on `[0,T]`; observation operator `C` (prey channel, `‖C‖=1`); sampling map
`S_n:C([0,T])→ℝ^n`, `(Sμ)_k=μ(t_k)`, `t_k∈(0,T]` arbitrary (not necessarily uniform);
`y=S_nμ+ε`, `ε~N(0,σ²I_n)`. Frozen benchmark: `n=120`, `T=12`.

## 2. Simple-vs-simple case (exact)

`H_1: μ=μ_F` (fractional), `H_2: μ=μ_m` (a **fixed** `m`-mode latent rival), equal covariance, equal priors:
\[
P_e^{\rm Bayes}=\Phi(-d/2),\qquad d=\|S_n(\mu_F-\mu_m)\|_2/\sigma .
\]
This is an identity, not a bound (affine log-likelihood ratio; midpoint threshold).

## 3. From the response discrepancy to `d`

With `Δμ:=μ_F−μ_m` and `E_m^G:=‖Δμ‖_{L^∞(0,T)}/‖u‖_∞` (**response level**, certified by `thm:T23`):
\[
\|S_n\Delta\mu\|_2\;\le\;\sqrt n\,\|\Delta\mu\|_\infty\;\le\;\sqrt n\,E_m^G\,U
\quad\Longrightarrow\quad
d\;\le\;\frac{\sqrt n\,E_m^G\,U}{\sigma}.
\tag{C.1}
\]

> ### Theorem C′ (final form)
> For every sampling schedule `{t_k}⊂(0,T]^n` and every input with `‖u‖_∞≤U`,
> \[
> P_e^{\rm Bayes}\;\ge\;\Phi\!\Big(-\frac{\sqrt n}{2\sigma}\,E_m^G\,U\Big).
> \]
> The bound depends on the design **only** through `n`, `U` and `T`; hence it is uniform over
> waveform shape and over sample placement.

## 4. Composite alternative — stated correctly

The latent hierarchy is a **family** `{μ_m(θ):θ∈Θ_m}`, so the relevant risk is not the simple Bayes
risk. Two correct statements, and the difference matters:

- **Minimax lower bound (what we may claim).** For any *particular* admissible rival `θ_0∈Θ_m`,
  the two-point argument gives
  `inf_tests sup_{θ∈Θ_m} R(test,θ) ≥ ½·2·Φ(−d(θ_0)/2)` in the sense that no test can beat the
  simple-vs-simple error for that pair. Therefore **exhibiting one rival with small `E_m^G` suffices**
  to lower-bound the composite minimax error. This is the honest logic: the obstruction is
  *constructive* (we build the confuser), not a statement about all of `Θ_m`.
- **What we may NOT claim.** That the composite Bayes risk with a prior on `Θ_m` equals `Φ(−d/2)`;
  that the bound is uniform *over the rival family* (it is uniform over designs, not over rivals).

**Priors.** Wherever "Bayes" is used, the prior is `(1/2,1/2)` on the two exhibited hypotheses — stated
explicitly. No prior is placed on `Θ_m`.

## 5. The `√n` step for arbitrary sample locations

`‖S_nΔμ‖_2 ≤ √n‖Δμ‖_∞` holds for **any** `n` points, with no regularity or spacing assumption; this is
what makes Theorem C′ uniform over schedules. Equality requires `|Δμ(t_k)|=‖Δμ‖_∞` at every sample —
i.e. it is attained only by pathological designs.

## 6. **Withdrawal of the Round-01 tightness claim**

Round 01 stated the chain was "tight to first order in `d`". **That is withdrawn.** The slack is not
controlled:
- **Young/response step:** `E_m^G U` replaces the true `‖Δμ‖_∞`; for the certified enclosures the
  ratio is not tracked.
- **Sampling step:** `√n‖Δμ‖_∞` overestimates `‖S_nΔμ‖_2` by up to `√n` when `Δμ` is concentrated —
  at `n=120` that is a factor up to ≈11 in `d`, i.e. a large change in the floor.
- Only the *final* Gaussian step (`Φ(−d/2)`) is exact.

Correct wording: **"the bound is exact in its last step and conservative in the two preceding ones;
the accumulated slack is not quantified."** A quasi-uniform-sampling refinement
(`Σ_kΔμ(t_k)² ≈ (n/T)∫Δμ²`) would reduce it and is a Round-03 item.

## 7. What survives, with numbers

Using `thm:T23` response-level enclosures (`α=0.85`, `T=12`, `A=0.25`, `n=120`, `σ=0.02`) and the
**linear** certificate `U(0.05)=0.0634`:

| `m` | `Ê_m^state` | `S=Ê·U` | `P_e` floor |
|---:|---:|---:|---:|
| 4 | 0.5335 | 3.38e-2 | 0.000 |
| 32 | 0.0070 | 4.44e-4 | **0.452** |

With the **nonlinear** certificate `U_NL(0.05)=1.6e-3` (`THEOREM_D_NONLINEAR_LIFT.md`) the floor at
`m=32` rises to `≈0.4987` — but, as recorded there, that is dominated by lack of excitation and is
therefore not an informative statement.

## 8. Required corrections to the manuscript's `thm:T20`

1. State with `E_m^G` (response level), **never** `E_m^K`.
2. Replace `Ψ`/Pinsker by `Φ(−d/2)` (exact; strictly stronger — Pinsker is vacuous at `d≥2√2`).
3. Use `‖u‖_∞≤U`, not `‖u‖₂≤B` (the `L²` pairing is invalid for `α≤1/2`, since `K_α∉L²(0,T)` there).
4. Define `C_obs:=‖C‖` explicitly.
5. Say "minimax lower bound via an exhibited confuser", not "composite Bayes risk".
6. Delete any "tight to first order" language (§6).
