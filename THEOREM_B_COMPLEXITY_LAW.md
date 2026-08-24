# THEOREM_B_COMPLEXITY_LAW — Round 01, Task 4

**Bottom line.** A complexity law **exists**, is **exponential in `m`**, and is **already published**
for the norm the literature uses. The manuscript's own constructive bound is *algebraic* and, at the
values of `m` the paper actually reports, **numerically vacuous** (73 % relative error at `m=48`).
The genuinely open item is narrow: the same rate in `L¹(0,T)` **including the singular endpoint**,
with positive weights. This round **measured** that rate over 285 cells and additionally **proved** that the relative error is horizon-independent (Lemma B.1); the *exponent* of the law is **not resolved** by the data (§3c).

---

## 1. Current statement (`thm:T9b`) and why it cannot be a contribution

> For every `T<∞` and `ε>0` there exists a finite positive exponential mixture whose `L¹(0,T)`
> distance from the Caputo kernel is below `ε`. Consequently, without a finite complexity restriction
> on the latent rival, no fixed finite-horizon experiment can guarantee uniform positive separation.

This is **existence only** — no dependence of `m` on `ε`. Published work is strictly stronger:

| Reference | Result | Norm / interval |
|---|---|---|
| Jiang, Zhang, Zhang, Zhang (2017), Commun. Comput. Phys.; arXiv:1511.03453 | `N_exp = O( log(1/ε)(log log(1/ε)+log(T/Δt)) + log(1/Δt)(log log(1/ε)+log(1/Δt)) )` for the power-law kernel with **uniform absolute error `ε`** | uniform; singularity handled through a `Δt` cutoff |
| Chaudhary, **Diethelm**, Farhadi, Fuchs (2025), arXiv:2508.20311 | prescribes the number of exponentials and minimizes the error | explicitly `[δ,T]`, `δ>0` — **endpoint excluded** |

⇒ **`thm:T9b` must be cited, not claimed.** Presenting an existence statement as a contribution when
an explicit `N_exp(ε)` is in print since 2017 is exactly the kind of thing a specialist referee
punishes (see the adversarial question in `NOVELTY_MATRIX.md`).

## 2. The genuinely open gap

The published rates are for the **uniform** error on an interval **bounded away from `t=0`** (or with
a `Δt` cutoff). The manuscript's chain does not need that norm: the object that controls the *output*
separation through Young's inequality is
\[
E_m=\|k_\alpha-k_m\|_{L^1(0,T)},\qquad\text{endpoint included,}
\]
with **weights kept positive** (the latent rival must be a physically realizable relaxation
hierarchy). Translating a `[δ,T]` uniform rate into an `L¹(0,T)` rate requires bounding the
contribution of `(0,δ)`, where `k_α` is unbounded — precisely the region the literature excises.

## 3. Measurement (computation C-1: 285 cells on Orion, `α∈{.30,.50,.70,.85,.95}`, `T∈{1,10,100}`, 19 budgets `m≤128`)

### 3a. A provable by-product: the relative error is **independent of `T`**

> **Lemma B.1 (scale invariance).** For `k_α(t)=t^{α−1}/Γ(α)` and any `λ>0`, the map
> `(c_j,λ_j) ↦ (λ^{α−1}c_j, λ_j/λ)` is a bijection between `m`-term positive exponential sums on
> `[0,T]` and on `[0,λT]`, and it scales **both** `‖k_α−k_m‖_{L¹}` and `‖k_α‖_{L¹}` by `λ^α`.
> Hence the **relative** `L¹` error of the best `m`-term approximant depends only on `(m,α)` — not on `T`.

*Proof.* `k_α(λt)=λ^{α−1}k_α(t)`. Given `k_m(t)=Σc_je^{−λ_jt}`, set `k̃_m(t)=λ^{α−1}Σc_je^{−(λ_j/λ)t}`,
so `k̃_m(λt)=λ^{α−1}k_m(t)`. Substituting `u=λt`,
`∫_0^{λT}|k_α−k̃_m| = λ^{α}∫_0^{T}|k_α−k_m|`, while `‖k_α‖_{L¹(0,λT)}=λ^α‖k_α‖_{L¹(0,T)}`. The ratio is
unchanged; positivity of weights is preserved. ∎

**Verified to machine precision:** at `m=16`, the relative error across `T=1,10,100` agrees to
`6·10^{-17}` (`α=0.30`), `9·10^{-18}` (`α=0.70`), `1·10^{-16}` (`α=0.95`).

**Why this matters.** The published rate (Jiang–Zhang) carries a `log(T/Δt)` factor because it
measures **uniform absolute** error; in the **relative `L¹`** norm that the output-separation chain
actually needs, the horizon drops out entirely. This is a small but genuinely useful observation and it
is *proved*, not fitted.

### 3b. Measured relative error (`T=10`, identical for all `T` by Lemma B.1)

| `α` | `m=16` | `m=32` | `m=64` | `m=128` |
|---|---|---|---|---|
| 0.30 | 9.35e-3 | — | 7.10e-6 | 2.32e-9 |
| 0.50 | — | — | 7.09e-6 | 3.99e-8 |
| 0.70 | 4.74e-3 | — | 4.70e-5 | 8.42e-7 |
| 0.85 | 1.58e-2 | 2.93e-3 | 4.26e-4 | 4.65e-6 |
| 0.95 | 1.21e-2 | — | 3.01e-4 | 1.14e-6 |

### 3c. **Correction to an earlier statement in this file.** The shape of the law is *not* resolved

An earlier local sweep (`α=0.85`, `m≤48`) fitted `ε ≈ 5.58e-2·exp(−0.0865m)` with `R²=0.995` and this
file previously reported that as "exponential in `m`". **With the full sweep to `m=128` that claim does
not hold as a determination of the exponent.** Comparing `log ε = a − c·m^β`:

| `α` | `R²(β=1)` | `R²(β=0.75)` | `R²(β=0.5)` | `R²(β=1/3)` | `R²` algebraic | verdict |
|---|---|---|---|---|---|---|
| 0.30 | 0.9937 | **0.9991** | 0.9829 | 0.9580 | 0.8745 | β not resolved |
| 0.50 | 0.9636 | 0.9912 | **0.9994** | 0.9909 | 0.9367 | β not resolved |
| 0.70 | 0.9702 | 0.9919 | **0.9942** | 0.9822 | 0.9234 | β not resolved |
| 0.85 | 0.9906 | **0.9943** | 0.9769 | 0.9514 | 0.8668 | β not resolved |
| 0.95 | **0.9798** | 0.9466 | 0.8890 | 0.8371 | 0.7072 | β≈1 (only case discriminated) |

**What the data do support, and nothing more:**
1. Convergence is **sub-exponential but strictly faster than algebraic** — the algebraic fit is the
   worst model at every `α` (`R²` 0.71–0.94 vs ≥0.95 for every stretched-exponential form).
2. Therefore `m(ε) = O(log^κ(1/ε))` with `κ∈[1,2]`; the data cannot pin `κ`.
3. `β=1/2` (root-exponential) is the value expected from classical rational/exponential approximation
   of algebraic singularities (Stahl; Gonchar–Rakhmanov for `x^α`), and it is the best fit at
   `α=0.5,0.7`. It is the safest form to *conjecture*, and `κ=2` the safest bound to *assume*.

**Status: MEASURED, and the exponent is UNRESOLVED.** Any manuscript sentence must say
"polylogarithmic in `1/ε`, consistent with root-exponential convergence" — **never** a specific rate
on the strength of these fits.

## 4. The manuscript's own rigorous bound is algebraic — and vacuous

`source_pack/07` (T9) proves, via a **uniform** trapezoid in `λ` with nodes on `[ℓ,L]`, `h=(L−ℓ)/m`:
\[
\|k_\alpha-k_m\|_{L^1(0,T)}\le c_\alpha\Big[\tfrac{T\ell^{1-\alpha}}{1-\alpha}+\tfrac{L^{-\alpha}}{\alpha}+T h \ell^{-\alpha}\Big].
\]
Optimizing over `(ℓ,L)` numerically for each `m` (Nelder–Mead, multi-start) gives:

| `m` | rigorous bound (rel) | measured optimum (rel) | ratio |
|---:|---:|---:|---:|
| 2 | 1.043 | 4.43e-2 | 23.5× |
| 8 | 0.912 | 2.84e-2 | 32.2× |
| 16 | 0.841 | 1.58e-2 | 53.3× |
| 32 | 0.772 | 2.93e-3 | 263× |
| 48 | **0.734** | 9.81e-4 | **749×** |

Fit: `ε_rel ≈ 1.14·m^{−0.112}` (`R²=0.9963`), matching the exponent `1−α = 0.15` predicted by
balancing the three terms.

**Two consequences.**
1. **The paper's rigorous bound is unusable as a complexity law.** At `m=48` it still permits 73 %
   relative error, so any statement of the form "`E_m→0` therefore the error floor rises" is, at the
   rigorous level, an asymptotic promise with no useful finite-`m` content. (The manuscript avoids
   this in practice by using the *certified interval enclosures* of `thm:T23` — `Ê_32=0.0070` — rather
   than this bound. That is legitimate, but it means the general theorem and the certified numbers are
   supported by **different** machinery, which must be said explicitly.)
2. **The obstruction is identified precisely: it is the quadrature.** A uniform trapezoid in `λ`
   cannot do better than algebraically, because the integrand `λ^{-α}e^{-λt}` spans many decades. The
   substitution `λ = e^s` makes it analytic with doubly-exponential decay, for which the trapezoid
   rule converges **geometrically** — this is exactly why the measured error is exponential and why
   Jiang–Zhang obtain `O(log(1/ε))`.

## 5. Strongest rigorous statement available right now

- **Rigorous, general, weak:** `E_m ≤ C(α,T)·m^{−(1−α)}` (from `source_pack/07` after optimizing the
  window; verified numerically, exponent `1−α`). Honest but nearly vacuous for `α` close to 1.
- **Rigorous, published, in a different norm:** `N_exp = O(log(1/ε)·log(T/Δt))` on intervals away
  from the singularity (Jiang–Zhang 2017) — cite this for the *shape* of the law.
- **Measured, in the required norm:** exponential with the constants of §3 — present as numerical
  evidence, clearly labelled, until proved.

## 6. What a proof would require (Round 02 target)

1. Replace the uniform-`λ` construction by the **log-scale quadrature** `λ=e^s`, nodes
   `s_j ∈ [s_min, s_max]`, weights `c_j = (sin πα/π)h e^{(1−α)s_j} > 0` (positivity is automatic —
   important, since the latent rival must be a genuine relaxation hierarchy).
2. Apply the standard trapezoidal-rule error theory for analytic integrands with doubly-exponential
   decay (geometric convergence in the number of nodes), which is the technical core of Jiang–Zhang.
3. Bound the **endpoint contribution** `∫_0^{δ}|k_α−k_m|` separately: `k_α` is integrable there
   (`∫_0^δ k_α = δ^α/(αΓ(α))`) and `k_m` is bounded by `Σc_j`, so the term is `O(δ^α + δΣc_j)`;
   choose `δ` as a function of `m` (e.g. `δ ~ e^{−cm}`) so it does not dominate.
4. Combine to obtain `E_m ≤ A e^{−cm}` with `A, c` explicit in `α, T`.

Steps 2–3 are the only real work; both are standard, which is why this is a Round-02 item, not a
research risk. **But it must not be asserted as proved until step 3 is written.**

## 7. Recommendation

**Supporting theorem, re-founded and honestly attributed.**
- Delete the existence-only framing of `thm:T9b` as a contribution; cite Jiang–Zhang (2017) and
  Chaudhary–Diethelm et al. (2025) for the law.
- State the paper's needed variant (`L¹(0,T)`, endpoint included, positive weights) as either
  (a) a proved proposition, once §6 is completed, or (b) explicitly *numerical evidence* with the
  table of §3 — never as a theorem on the strength of the fit alone.
- **Replace** the `source_pack/07` uniform-`λ` construction in the manuscript by the log-scale one;
  keeping an algebraic bound that permits 73 % error at `m=48` is an open invitation for a referee.
- Keep `thm:T23`'s certified enclosures as the numbers that feed Theorems C′/D, and say plainly that
  they come from interval certification, not from the analytic bound.
