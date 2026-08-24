# THEOREM_B_COMPLEXITY_LAW — Round 01, Task 4

**Bottom line.** A complexity law **exists**, is **exponential in `m`**, and is **already published**
for the norm the literature uses. The manuscript's own constructive bound is *algebraic* and, at the
values of `m` the paper actually reports, **numerically vacuous** (73 % relative error at `m=48`).
The genuinely open item is narrow: the same rate in `L¹(0,T)` **including the singular endpoint**,
with positive weights. This round **measured** that rate (fit `R²=0.995`) but did **not prove** it.

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

## 3. Measurement (computation C-1, `α=0.85`, `T=12`, Orion + local)

Relative `L¹(0,T)` error of the best positive `m`-term exponential sum (log-scale quadrature window
optimized, then NNLS weight refinement), normalized by `‖k_α‖_{L¹(0,T)}=8.7416`:

| `m` | 2 | 4 | 8 | 12 | 16 | 24 | 32 | 48 |
|---|---|---|---|---|---|---|---|---|
| `ε_rel` | 4.43e-2 | 4.14e-2 | 2.84e-2 | 1.96e-2 | 1.58e-2 | 6.56e-3 | 2.93e-3 | 9.81e-4 |

Law fits (`log ε = a − c·m^β`):

| model | fit | `R²` |
|---|---|---|
| **`β=1` (exponential)** | `ε_rel ≈ 5.58e-2 · exp(−0.0865 m)` | **0.9950** |
| `β=1/2` | `1.88e-1 · exp(−0.715 √m)` | 0.9617 |
| `β=1/3` | `6.13e-1 · exp(−1.640 m^{1/3})` | 0.9298 |
| algebraic | `2.19e-1 · m^{−1.172}` | 0.8328 |

**Measured law.** Exponential in `m` wins decisively, hence
\[
m(\varepsilon)\;\gtrsim\;\frac{1}{0.0865}\,\ln\!\frac{5.58\times10^{-2}}{\varepsilon}
\;=\;O\!\big(\log(1/\varepsilon)\big),
\]
i.e. **the same order as the published `[δ,T]` rate, but attained in `L¹(0,T)` with the endpoint
included and with positive weights.** This is the statement the paper needs.

**Status: MEASURED, NOT PROVED.** A least-squares fit over 9 values of `m` at one `(α,T)` is evidence,
not a theorem. The full `(α,T,m)` table (5 orders × 3 horizons × 19 budgets) was launched on Orion as
computation C-1 to test stability of the exponent across the grid.

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
