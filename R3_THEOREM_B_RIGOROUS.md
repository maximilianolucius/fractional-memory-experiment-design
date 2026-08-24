# R3-A — Theorem B (finite-horizon exponential-sum approximation), rigorised

**Round 03, researcher deliverable.**
**Verdict up front: the result is correct, the proof is now complete, and it must be
demoted from a headline theorem to a lemma/tool. The technique is McLean (2018).**

---

## 1. Final statement (safe form)

Let `0 < α < 1` and let

```
K_α(t) = t^{α−1} / Γ(α),      t ∈ (0,T]
```

be the Riemann–Liouville / Caputo memory kernel. Let

```
E_m^+(α,T) = inf { || K_α − Σ_{j=1..m} c_j e^{−λ_j ·} ||_{L¹(0,T)}  :  c_j > 0, λ_j > 0 }
```

be the best `L¹(0,T)` approximation error over **positive** exponential mixtures of order `m`.

> **Lemma B.2.** For every `α ∈ (0,1)`, every `T > 0`, and **every** `c < π√(α(1−α))`
> there exists a finite constant `A(α,c)` such that
> ```
> E_m^+(α,T)  ≤  A(α,c) · T^α · e^{−c√m}       for all m ≥ 1.
> ```
> The construction is explicit (truncated trapezoidal quadrature of the Stieltjes
> representation on a logarithmic grid) and yields positive weights and positive rates.
>
> **Corollary B.3 (complexity).** `m(ε) = ⌈ c^{−2} log²(A(α,c) T^α / ε) ⌉ = O(log²(1/ε))`.

The quantifier order matters and is the whole point of the "safe form": the constant
`A(α,c)` **blows up as `c ↑ π√(α(1−α))`**, and this argument does **not** establish the
endpoint rate `c = π√(α(1−α))` with a finite constant. Any statement of the form
"`E_m ≤ A e^{−π√(α(1−α)m)}`" is stronger than what is proved here and must not be written.

---

## 2. Reduction to `T = 1` (Lemma B.1) — exact, and numerically confirmed

Substitute `t = Ts` and use the homogeneity `K_α(Ts) = T^{α−1} K_α(s)`:

```
|| K_α − Σ c_j e^{−λ_j ·} ||_{L¹(0,T)}
   = T ∫_0^1 | T^{α−1} K_α(s) − Σ c_j e^{−(λ_j T) s} | ds
   = T^α ∫_0^1 | K_α(s) − Σ (T^{1−α} c_j) e^{−(λ_j T) s} | ds.
```

The map `(c_j, λ_j) ↦ (T^{1−α} c_j, T λ_j)` is a bijection of the admissible set
`{c_j > 0, λ_j > 0}` onto itself, so taking infima on both sides,

```
E_m^+(α,T) = T^α · E_m^+(α,1).                                        (B.1)
```

**This is exact, and the 285-cell C-1 sweep confirms it to machine precision.** For every
`α ∈ {0.3, 0.5, 0.7, 0.85, 0.95}` and every `m ∈ {8, 32, 128}`:

| α | E(10)/E(1) | 10^α | E(100)/E(1) | 100^α |
|---|---:|---:|---:|---:|
| 0.30 | 1.9953 | 1.9953 | 3.9811 | 3.9811 |
| 0.50 | 3.1623 | 3.1623 | 10.0000 | 10.0000 |
| 0.70 | 5.0119 | 5.0119 | 25.1189 | 25.1189 |
| 0.85 | 7.0795 | 7.0795 | 50.1187 | 50.1187 |
| 0.95 | 8.9125 | 8.9125 | 79.4328 | 79.4328 |

and the *relative* error is invariant in `T` to all printed digits (e.g. `α=0.3, m=8`:
0.075835 at `T = 1, 10, 100`). This is the cleanest verified statement in the whole rescue.

Everything below is therefore on `(0,1)`.

---

## 3. Construction and the three error sources

**Stieltjes representation.** With `c_α = sin(πα)/π = 1/(Γ(α)Γ(1−α))`,

```
K_α(t) = c_α ∫_0^∞ λ^{−α} e^{−λt} dλ,     since ∫_0^∞ λ^{−α}e^{−λt}dλ = Γ(1−α) t^{α−1}
```

and `c_α Γ(1−α) = 1/Γ(α)`, so the identity is exact. Substituting `λ = e^x`:

```
K_α(t) = c_α ∫_{−∞}^{∞} g(x,t) dx,        g(x,t) = e^{(1−α)x} e^{−t e^x}.
```

**Quadrature.** Apply the infinite trapezoidal rule with step `h`, then truncate:

```
K_α(t) ≈ c_α h Σ_{k=−M₋}^{M₊} g(kh,t)  =  Σ_j c_j e^{−λ_j t},
      λ_k = e^{kh} > 0,     c_k = c_α h e^{(1−α)kh} = c_α h λ_k^{1−α} > 0,
      m = M₋ + M₊ + 1.
```

Positivity of weights and rates is automatic. Three error sources — **not four**; see §4.

**(E1) Discretisation error of the infinite trapezoidal rule.**
For `|Im x| ≤ d < π/2`,
```
|g(x+iy,t)| = e^{(1−α)x} e^{−t e^x cos y} ≤ e^{(1−α)x} e^{−t e^x cos d}.
```
The strip norm is finite and computable: substituting `u = e^x cos d`,
```
N(g(·,t),d) := ∫_R (|g(x+id,t)| + |g(x−id,t)|) dx ≤ 2 (cos d)^{α−1} Γ(1−α) t^{α−1}.
```
By the standard analytic-strip trapezoidal estimate (Stenger; Trefethen–Weideman 2014),
```
| ∫_R g dx − h Σ_{k∈Z} g(kh,t) |  ≤  N(g(·,t),d) · e^{−2πd/h} / (1 − e^{−2πd/h}).
```
Integrating in `t` over `(0,1)` and using `∫_0^1 t^{α−1} dt = 1/α`:
```
E1 ≤ (2 / Γ(α+1)) · (cos d)^{α−1} · e^{−2πd/h} / (1 − e^{−2πd/h}).            (E1)
```
using `c_α Γ(1−α)/α = 1/(α Γ(α)) = 1/Γ(α+1)`.

**(E2) Large-λ truncation tail** (`k > M₊`). Using `∫_0^1 e^{−λt} dt ≤ 1/λ`:
```
E2 ≤ c_α h Σ_{k>M₊} e^{(1−α)kh} e^{−kh} = c_α h e^{−α(M₊+1)h} / (1 − e^{−αh})
   ≤ (c_α/α) · e^{−α M₊ h} · κ(αh),       κ(s) = s/(1−e^{−s}) → 1 as s→0.   (E2)
```

**(E3) Small-λ truncation tail** (`k < −M₋`). Using `∫_0^1 e^{−λt} dt ≤ 1`:
```
E3 ≤ c_α h Σ_{k<−M₋} e^{(1−α)kh} = c_α h e^{−(1−α)(M₋+1)h} / (1 − e^{−(1−α)h})
   ≤ (c_α/(1−α)) · e^{−(1−α) M₋ h} · κ((1−α)h).                              (E3)
```

---

## 4. Correction: the endpoint split is unnecessary

Round 02 (and the chief's suggested route) treated `t → 0` by splitting `(0,δ) ∪ (δ,1)`,
approximating only on `(δ,1)`, and balancing `δ = δ(m)`. That produced a spurious
`δ L^{1−α}`-type term and a worse rate.

**It is not needed.** The strip bound `N(g(·,t),d) ∝ t^{α−1}` is integrable on `(0,1)`
precisely because `α > 0`, so (E1) holds on the *whole* interval including the singular
endpoint, with the finite constant `1/Γ(α+1)`. The singularity is absorbed by the
`t`-integration, not by excising a neighbourhood of zero.

This is a genuine simplification of the proof and it removes the endpoint term entirely.
It is also what makes the result an `L¹(0,T)`-statement rather than an `[δ,T]`-statement —
which, as §6 shows, is the *only* thing separating it from the published literature.

---

## 5. Balancing and the rate

Equalise the three exponents. Setting `α M₊ h = (1−α) M₋ h = 2πd/h` gives

```
M₊ = 2πd/(α h²),   M₋ = 2πd/((1−α) h²),
m ≈ M₊ + M₋ = (2πd/h²) · 1/(α(1−α)),
h = √( 2πd / (m α(1−α)) ),
2πd/h = √( 2πd · α(1−α) · m ).
```

Hence, for fixed `d < π/2`,

```
E_m^+ ≤ A(α,d) · exp( −√(2πd α(1−α) m) ),      A(α,d) ∝ (cos d)^{α−1}/Γ(α+1) + …
```

As `d ↑ π/2` the exponent tends to `√(π² α(1−α) m) = π√(α(1−α) m)`, while
`(cos d)^{α−1} → ∞` since `α − 1 < 0`. Therefore:

- for every `c < π√(α(1−α))` pick `d < π/2` with `√(2πd α(1−α)) > c`; then `A(α,c) := A(α,d) < ∞`. ✓
- at `c = π√(α(1−α))` the argument gives **no finite constant**. ✗

**Status of the boundary constant: open.** Whether `π√(α(1−α))` is attained with a finite
constant, and whether it is optimal, is not settled by this proof and not settled by us.

---

## 6. Adversarial novelty check — the result is not new as a technique

Searched deliberately for prior art that would kill the theorem. It largely does.

| reference | kernel / object | weights | domain | rate | overlaps our proof? |
|---|---|---|---|---|---|
| **McLean, "Exponential sum approximations for `t^{−β}`" (2018), arXiv:1606.00123** | `t^{−β}`, i.e. our `K_α` up to constant | **positive** (`w>0, a>0`) | **compact `[δ,T]`, `δ>0`** | quadrature + Prony reduction | **Yes — same technique: trapezoidal rule on an integral representation, positive weights.** Does **not** treat `t=0` / `L¹(0,T)`. |
| Beylkin–Monzón (2005, 2010) | general completely monotone | positive | away from 0 | numerically near-optimal, not the closed-form rate | Same family of ideas; no endpoint-inclusive `L¹` rate |
| Jiang–Zhang–Zhang–Zhao (2017) | Caputo kernel for fast time-stepping | positive | `[Δt, T]`, excludes first step | `O(log(1/ε)·log(T/Δt))`-type node counts | Same purpose (SOE for fractional kernels); excludes the singular step by construction |
| Schädle–López-Fernández–Lubich (2006); Banjai–López-Fernández | contour/quadrature for fractional convolution | complex (contour) | `t` bounded away from 0 | root-exponential in nodes | Rate of the same type, but complex weights and no `L¹(0,T)` |
| Stenger (sinc quadrature); Trefethen–Weideman (2014) | general analytic-strip quadrature | n/a | n/a | `e^{−2πd/h}` | **This is the engine we invoke**, cited as such |
| Stahl; Gonchar–Rakhmanov | rational approximation of algebraic singularities | n/a | n/a | root-exponential is the *known optimal* order for algebraic branch points | Confirms the `e^{−c√m}` order is expected, not surprising |
| Chaudhary–Diethelm; Li (2010); Baffet–Hesthaven | diffusive/SOE realisations of fractional operators | positive/mixed | typically `t>0` | various | Same construction family |

**Honest reading.** The construction, the positivity of the weights, and the
root-exponential order are all **known**. Our contribution is narrow and technical:

1. the estimate is carried out in `L¹(0,T)` **including the singular endpoint `t = 0`**,
   which the cited works exclude (McLean explicitly works on `[δ,T]`);
2. the elimination of the endpoint split (§4), which is what makes (1) possible in five
   lines rather than via a `δ(m)` balance;
3. an explicit rate constant `π√(α(1−α))` in the safe quantifier form, with the exact
   `T^α` scaling (B.1).

That is a **lemma**, not a headline theorem, and root-exponential order for algebraic
singularities is exactly what Stahl / Gonchar–Rakhmanov theory predicts.

**Consequences (both are retractions of my own Round-02 recommendations):**

- **Demote.** In the manuscript this becomes a lemma/tool supporting the discrimination
  results (it is what makes the `latent3` rival genuinely hard, i.e. it feeds Theorem
  T9b/T20), and is **not** claimed as a headline contribution.
- **Withdraw the FCAA split.** `ROUND_02_JOURNAL_DECISION.md` proposed a separate short
  analysis paper (Lemma B.1 + Theorem B.2) to *Fractional Calculus and Applied Analysis*.
  **That recommendation is withdrawn.** Against McLean (2018) it would not clear novelty,
  and submitting it would repeat exactly the error that produced the desk rejection.

---

## 7. Numerical status of the rate (285-cell C-1 sweep, positive weights)

The relevant measured quantity is `L1_err_nnls` (non-negative least squares = positive
weights, matching the theorem). `T = 1`, `m` from 2 to 128, five `α`.

**(a) Is the bound satisfied with a *useful* constant at the theoretical rate
`c = π√(α(1−α))`?** Yes — this is the strong result.

| α | c_theory | smallest valid A | argmax m | E(m=128) | bound at 128 | slack |
|---|---:|---:|---:|---:|---:|---:|
| 0.30 | 1.4397 | 11.11 | 16 | 2.58e−09 | 9.37e−07 | 363× |
| 0.50 | 1.5708 | 5.156 | 10 | 4.50e−08 | 9.87e−08 | 2.19× |
| 0.70 | 1.4397 | 10.98 | 128 | 9.27e−07 | 9.27e−07 | **1.00×** |
| 0.85 | 1.1218 | 3.947 | 80 | 4.92e−06 | 1.22e−05 | 2.47× |
| 0.95 | 0.6847 | 0.2891 | 24 | 1.16e−06 | 1.25e−04 | 107× |

The constants needed are `O(1)`–`O(10)`, and at `α = 0.70` the bound is **attained** at
`m = 128` (slack 1.00×). So the bound is active and non-vacuous on the measured range.

**(b) Does the complexity corollary predict the measured latent budget?** Yes, within a
small factor. Using `c = 0.9 π√(α(1−α))` and the corresponding fitted `A`:

| α | m(1e−3) predicted | m(1e−3) measured | m(1e−6) predicted | m(1e−6) measured |
|---|---:|---:|---:|---:|
| 0.30 | 45.5 | 40 | 145.8 | 80 |
| 0.50 | 32.4 | 28 | 112.0 | 96 |
| 0.70 | 35.1 | 40 | 126.7 | 128 |
| 0.85 | 52.0 | 56 | 197.5 | >128 |
| 0.95 | 74.9 | 48 | 394.5 | >128 |

**(c) Is the exponent empirically `1/2`? No — and this retracts a Round-02 claim.**
Free fit of `log E = log A − c m^β`:

| α | β fitted | 95% CI | contains 1/2? |
|---|---:|---|:--:|
| 0.30 | 0.783 | [0.738, 0.829] | **no** |
| 0.50 | 0.556 | [0.507, 0.604] | **no** (barely) |
| 0.70 | 0.531 | [0.463, 0.599] | yes |
| 0.85 | 0.777 | [0.706, 0.849] | **no** |
| 0.95 | 1.270 | [1.164, 1.375] | **no** |

Every fitted `β ≥ 0.53 > 1/2`, so the measured decay is at least as fast as
root-exponential and the **bound is never violated** — but the data do not identify `√m`
as the exact rate on `m ≤ 128`, and the apparent exponent varies with `α`. Two
explanations, both plausible and not separated here: (i) NNLS on a fixed grid is a
different (possibly better) construction than the balanced trapezoidal one; (ii) the
asymptotic regime is not reached by `m = 128`.

**Retraction 1.** Round 01/02 reported "exponential in `m`, `R² = 0.995`" from a `β = 1`
fit. With `β` free, `β = 1` is preferred only at `α = 0.95`. The exponent is **not**
resolved by this data and the earlier claim overstated it.

**Retraction 2.** Round 02 reported the root-exponential constant "verified to 0.35%".
That was a single-`α` reading. Across the five `α`, the ratio `c_fit / c_theory` is
1.32, 1.01, 0.81, 0.81, 1.32 (full range `m`) — a spread of −19% to +32%. **The 0.35%
figure is withdrawn.** The defensible numerical claim is (a) and (b) above, not a
constant match.

---

## 8. What to write in the manuscript

- State Lemma B.1 (`T^α` scaling) — exact, cheap, verified to machine precision.
- State Lemma B.2 in the safe quantifier form of §1, with the construction, and cite
  McLean (2018), Beylkin–Monzón, Jiang et al., Stenger, Trefethen–Weideman **and** the
  Stahl / Gonchar–Rakhmanov optimality context. Attribute the technique.
- Add one sentence saying what is ours: the `L¹(0,T)` endpoint-inclusive form and the
  explicit constant, and nothing more.
- Do **not** headline it. Do **not** split it out as a separate paper.
- Report §7(a)–(b) as the numerical validation. Do **not** report a fitted exponent or a
  matched constant.

## 9. Not done

- **Lower bound.** No matching lower bound on `E_m^+`. Whether `π√(α(1−α))` is optimal for
  positive-weight mixtures in `L¹(0,T)` is open (Stahl-type theory suggests the *order* is
  optimal; the constant is not addressed). Stretch goal, not achieved.
- **Boundary constant.** Attainment at `c = π√(α(1−α))` unresolved (§5).
- **McLean's exact rate/norm.** Confirmed from the abstract: interval `[δ,T]`, positive
  weights, endpoint not addressed. The precise rate in that paper was not extracted from
  the full text; this does not affect the verdict, which rests on the technique being the
  same and the domain being `[δ,T]`.
