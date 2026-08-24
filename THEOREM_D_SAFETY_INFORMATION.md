# THEOREM_D_SAFETY_INFORMATION — Round 01, Task 6 (highest-value task)

# CONCLUSION: **GREEN**

A mathematically correct, non-trivial safety-constrained information ceiling **is available**, with
explicit computable constants, and it reproduces a phenomenon already measured in the frozen v3
benchmark. Its scope is strictly delimited below (linearized, single collocated channel), and its
novelty must be positioned against `SAFE26A` — it is *not* the first "safety limits information"
theorem, it is the first such statement for **hereditary mechanism discrimination with an explicit
latent-complexity budget**, as far as this round's literature audit could determine.

---

## 1. The chain, proved

Setting: strong-Allee coexistence equilibrium `z*=(x*,y*(A))`, linearization
`τ₀^{α−1} D^α ξ = J(A)ξ + Bu`, collocated prey channel (`B=e₁`, `C=e₁ᵗ`, so `CB=1≠0`), observations
`y_k = (Cξ)(t_k)+ε_k`, `ε_k~N(0,σ²)`, `k=1..n`, `t_k∈(0,T]`.

**(i) Safety ⇒ state constraint.** The ecological safety requirement `x(t) ≥ A+δ` for `δ>0` is, in
perturbation coordinates, `ξ_x(t) ≥ −ρ(δ)` with
\[
\rho(\delta) := x^\*-A-\delta .
\]
It is therefore implied by `‖ξ‖_∞ ≤ ρ(δ)`.

**(ii) State constraint ⇒ admissible excitation bound.** With impulse response
`H_α(t)=τ₀^{1−α}t^{α−1}E_{α,α}(τ₀^{1−α}Jt^α)B` and
\[
\Gamma_T := \sup_{0\le t\le T}\int_0^t\|H_\alpha(s)\|\,ds ,
\]
Young's inequality gives `‖ξ‖_{L^∞(0,T)} ≤ Γ_T‖u‖_{L^∞(0,T)}`. Hence every input with
\[
\boxed{\;\|u\|_\infty \;\le\; U(\delta):=\rho(\delta)/\Gamma_T\;}
\]
keeps the linearized trajectory inside the safe set. `U(δ)` is **strictly decreasing in `δ`**.

**(iii) Excitation bound ⇒ observable-separation ceiling.** Let `k_α` be the fractional memory kernel
and `k_m` the best `m`-mode positive latent surrogate, `E_m := ‖k_α−k_m‖_{L¹(0,T)}` (equivalently, at
prey-response level, the certified enclosure `Ê_m^state` of `thm:T23`). For any admissible input,
\[
\|\mu_\alpha-\mu_m\|_\infty \;\le\; E_m\,\|u\|_\infty \;\le\; \boxed{S_{\max}(\delta,m) := E_m\,U(\delta)} .
\]

**(iv) Separation ceiling ⇒ testing-error floor.** By Theorem C′ (exact two-point Gaussian bound,
`THEOREM_C_TESTING_OBSTRUCTION.md`),
\[
\boxed{\;P_e^\*(m,\delta)\;\ge\;\Phi\!\Big(-\frac{\sqrt n}{2\sigma}\,E_m\,\frac{x^\*-A-\delta}{\Gamma_T}\Big)\;}
\]
**uniformly over every safe admissible input**. The bound is monotone: increasing the safety margin
`δ` decreases `U(δ)`, decreases `S_max`, and **increases the error floor**. Increasing the latent
budget `m` decreases `E_m` and also increases the floor. ∎

> ### Theorem D (safety-constrained information ceiling)
> Under (i)–(iv), for every `δ>0` and every `m`, no test based on `n` samples of the collocated prey
> channel under any excitation that is safe in the sense `‖u‖_∞ ≤ U(δ)` can achieve error below
> `Φ(−(√n/2σ)·E_m·(x*−A−δ)/Γ_T)`. In particular, if the admitted latent hierarchy satisfies
> `E_m → 0`, then for **every fixed safety margin `δ>0`** the safe-experiment error floor tends to
> `1/2`: safety-constrained discrimination of the memory mechanism becomes impossible.

## 2. Computed constants (this round, not inherited)

`A=0.25`, `x*=2/3`, `x*−A=0.4167`, `n=120`.

`Γ_T = sup_t ∫₀^t‖H_α‖`, computed from the PECE impulse response:

| `α` | `T=6` | `T=12` | `T=24` |
|---|---:|---:|---:|
| 0.70 | 4.0600 | 5.7353 | 6.8536 |
| 0.85 | 4.3292 | **5.7815** | 6.5099 |
| 0.95 | 4.7371 | 7.2499 | 9.3798 |

Safe amplitude ceiling at `α=0.85, T=12`:

| `δ` | `ρ(δ)` | `U(δ)` |
|---:|---:|---:|
| 0.02 | 0.3967 | 0.0686 |
| 0.05 | 0.3667 | **0.0634** |
| 0.10 | 0.3167 | 0.0548 |
| 0.20 | 0.2167 | 0.0375 |
| 0.30 | 0.1167 | 0.0202 |

**Error floors** using the **certified** enclosures of `thm:T23` (`Ê_4=0.5335`, `Ê_32=0.0070`;
`m=8,16` geometrically interpolated and marked as illustrative):

| `m` | `Ê_m` | `S_max` (δ=0.05) | floor, σ=0.005 | σ=0.02 | σ=0.05 |
|---:|---:|---:|---:|---:|---:|
| 4 | 0.5335 | 3.38e-2 | 0.000 | 0.000 | 0.000 |
| 8 | 0.2873* | 1.82e-2 | 0.000 | 0.000 | 0.023 |
| 16 | 0.0833* | 5.28e-3 | 0.000 | 0.074 | 0.281 |
| 32 | 0.0070 | 4.44e-4 | 0.313 | **0.452** | 0.481 |

At the larger margin `δ=0.20` (`U=0.0375`) the `m=32` floor rises to **0.471** (σ=0.02).
*(\* interpolated, not certified.)*

**Kernel-level floors from computation C-1** (same constants, `E_m` = measured best `m`-term relative
`L¹` error × `‖k_α‖_{L¹}`, `α=0.85`, `δ=0.05`, `σ=0.02`, `n=120`):

| `m` | `E_m` (absolute) | `S_max` | `P_e` floor |
|---:|---:|---:|---:|
| 32 | 2.56e-2 | 1.62e-3 | 0.3282 |
| 64 | 3.73e-3 | 2.36e-4 | 0.4742 |
| **128** | 4.07e-5 | 2.58e-6 | **0.4997** |

At `m=128` the floor is `0.4997` — **indistinguishable from chance (0.5) to four decimals**. This is
the sharpest available statement of the obstruction: within the certified-safe excitation envelope, a
128-mode latent hierarchy cannot be separated from fractional memory at all.

**Interpretation.** Few latent modes ⇒ mechanisms separable (floor ≈ 0). At `m=32`, safe excitation
cannot push the error below ≈45 %, i.e. **essentially chance (50 %)**. Demanding more safety makes it
worse. This is the quantitative content of the safety–informativeness trade-off that the manuscript
currently reports only as a numerical observation.

## 3. Independent consistency check against the frozen v3 benchmark

The v3 benchmark used peak amplitude **0.10**, which exceeds `U(δ)` for every `δ ≥ 0.02`
(58 % above `U(0.05)`; 167 % above `U(0.20)`). Theorem D therefore predicts that v3 was **not** in the
certified-safe regime. Measured Allee-crossing rates (`benchmark/results/nonlinear_confusion.json`):

| design | crossing rate | `min(x−A)` |
|---|---:|---:|
| sinusoid | 1.00 | −0.306 |
| prbs | 1.00 | −0.314 |
| chirp | 0.93 | −0.301 |
| multisine | 0.36 | −0.240 |
| pulse | 0.07 | −0.121 |
| multiscale | 0.00 | **+0.292** |

Consistent with the theorem: `Γ_T` is a **worst-case** (sustained-excitation) gain, so sustained /
broadband designs realize it and cross; transient designs (pulse, multiscale) do not realize the worst
case and stay safe at the same nominal amplitude. The bound is therefore **correct but conservative
for transient inputs** — a limitation, stated in §5, not a contradiction.

## 4. Assumptions (must be stated verbatim in the paper)

1. Linearization valid on the excursion set (guaranteed a posteriori by `‖ξ‖_∞ ≤ ρ(δ)`).
2. Collocated prey channel with `CB ≠ 0`; single input, single output.
3. Matignon-stable operating point so that `H_α ∈ L¹(0,T)` and `Γ_T < ∞`.
4. Equal-covariance Gaussian observation noise, equal priors, `n` samples in `(0,T]`.
5. Latent rivals: positive `m`-mode relaxation hierarchies (physically realizable), approximation
   measured in `L¹(0,T)` — **not** `L²`, which is vacuous for `α ≤ 1/2` (see Theorem C audit).
6. `δ>0` strictly, so `ρ(δ)>0`, i.e. `δ < x*−A`.

## 5. Limitations (do not overclaim)

- **Linearized.** The safety guarantee is for the linearized trajectory; the nonlinear statement
  requires a Volterra/Grönwall step that this round did **not** close.
- **One channel.** Prey-collocated only. A full-state or multi-channel version is open (this is the
  same boundary the chief-audit already drew around `thm:T23`).
- **Conservative for transient inputs.** `Γ_T` is a worst-case gain; a design-dependent refinement
  (e.g. replacing `Γ_T` by the realized gain of the specific waveform) would tighten the ceiling and
  is the natural Round-02 target.
- **Not the first safety-vs-information theorem.** `SAFE26A` (Saligrama, arXiv:2607.16895) proves an
  information ceiling under safety in the constrained-LQ/regret setting. Theorem D must be presented
  as the *hereditary-mechanism, complexity-budgeted, testing-error analogue*, citing `SAFE26A`
  prominently. Claiming priority on the concept would be false.

## 6. Specialization to the strong-Allee model

All constants are explicit and certified at the operating point: `x*=2/3` exactly; `A=0.25`;
`Γ_T=5.7815` (`α=0.85,T=12`); `U(0.05)=0.0634`; `Ê_32=0.0070` by outward-rounded interval
subdivision (`thm:T23`). The Allee threshold is what makes `ρ(δ)` finite and small — in a model
without an extinction threshold the safety constraint would be inactive and the ceiling vacuous.
**That is precisely why the ecological specialization is not decorative:** the strong Allee effect
supplies the binding constraint.

## 7. Recommendation

**Headline result**, stated as Theorem D with the boxed inequality of §1(iv), the constant table of
§2, and the limitations of §5 in the theorem's immediate neighbourhood — not hidden in a discussion
section. Pair it with Theorem C′ (which supplies step iv) and with Theorem B's rate (which supplies
`E_m`, see `THEOREM_B_COMPLEXITY_LAW.md`).
