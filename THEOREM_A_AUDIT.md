# THEOREM_A_AUDIT — Round 01, Task 3 (structural non-equivalence)

**Outcome: the current theorem is true but proved by a fragile argument, and a strictly stronger,
simpler theorem is available.** A counterexample to the statement *without* its `CB≠0` hypothesis was
found and verified numerically to machine precision, inside the manuscript's own model.

---

## 1. Current statement (`thm:T4`, `paper/sections/sec3.tex`)

> For `0<α<1` and `CB≠0`, the Caputo transfer cannot equal any finite-dimensional rational latent
> transfer on a nonempty open subset of a common analytic domain. It also cannot equal a strictly
> proper finite-state retarded model with finitely many discrete delays, because the latter has
> `O(ω^{-1})` high-frequency decay whereas the Caputo channel has `O(ω^{-α})` decay.

**Proof mechanism used:** leading high-frequency asymptotics (`s^{-α}` vs integer powers).

**Weaknesses of that mechanism.**
1. It compares only the *leading* term. Two functions can share leading asymptotics and differ, and —
   more dangerously — non-integer leading exponents can *collapse to integers* when `α` is rational
   (see §3).
2. It restricts the delay class to *strictly proper*, *retarded*, *finitely many* delays. Neutral
   delay systems, feedthrough, and distributed delays are left uncovered (a defect already flagged as
   P1.5 in `audits/PAPER_AUDIT.md`).
3. It never states where the analytic domain is cut, although `s^α` requires a branch cut.

---

## 2. Exact criterion found (necessary **and** sufficient)

Write, with `τ₀=1` w.l.o.g., `q_α(s)=s^α` and

  `R(q) := C(qI−J)^{-1}B = N(q)/Δ(q)`  in coprime form, `J∈ℝ^{n×n}`.

Let `E := { e ∈ ℤ≥0 : the coefficient of q^e is nonzero in N or in Δ }` be the set of **effectively
present exponents**. Then:

> **Lemma A.0 (rationality criterion).** `G_α(s) := R(s^α)` is a rational function of `s`
> **if and only if** `α·e ∈ ℤ` for every `e ∈ E`.

*Proof.* (⇐) If every present exponent satisfies `αe∈ℤ` then each monomial `q^e = s^{αe}` is an
integer power of `s`, so `N(s^α)` and `Δ(s^α)` are polynomials in `s` and their quotient is rational.
(⇒) Conversely, `s ↦ s^α` maps a punctured neighbourhood of `0` onto a Riemann-surface sheet; if some
`e∈E` has `αe∉ℤ`, then continuing `G_α` once around `s=0` returns a different branch, so `G_α` is not
single-valued, hence not rational (rational functions are single-valued and meromorphic). ∎

**Verified numerically in both directions** (`rescue_src`, machine precision):
- `α=1/2`, `n=2`, `tr J=0`, cross channel: `E={0,2}`, `α·E={0,1}⊂ℤ` ⇒ predicted rational; measured
  `max|G_α − d/(s+D)| = 2.24e-16` ⇒ **exactly rational**.
- `α=1/3`, `n=3`, characteristic polynomial `q³+D`, channel isolating `1/Δ`: `E={0,3}` ⇒ predicted
  rational; measured `2.48e-16` against `1/(s+D)`.
- Same `J`, channel exposing `q¹`: `α·1=1/3∉ℤ` ⇒ predicted non-rational; branch factor visible.

---

## 3. Counterexample to the statement **without** `CB≠0`

Take the 2×2 coexistence structure `J=[[T,−c],[d,0]]` used throughout the manuscript, put `T=0`, and
observe the **cross** channel (`B=e₁`, `C=e₂`, so `CB=0`). Then
`Δ_α(s)=q²−Tq+cd = s+cd` for `α=1/2`, and

  `G_{y←x}(s) = d/Δ_α(s) = d/(s+cd)`,

which is **exactly a first-order rational transfer function**. Verified to `2.2e-16`.

**Where this lives in the paper's own model.** `T(A)=(7A−2)/(8A)=0 ⟺ A=2/7`. So the counterexample
sits precisely at `A=2/7 ≈ 0.2857`, the model's own trace-sign/stability boundary and the very
threshold used to split the benchmark's "stable" from "verdict" regimes.

**Consequence.** `CB≠0` is **not a cosmetic hypothesis**: dropping it makes the theorem false. The
manuscript keeps the hypothesis, so `thm:T4` is *not wrong* — but it must stop justifying it by
asymptotics and state the exception explicitly, because a referee testing `α=1/2` on a cross channel
will find an exactly rational Caputo transfer.

---

## 4. Strongest correct generalized statement found

> **Theorem A′ (structural non-equivalence via branch structure).** Let `0<α<1`, `J∈ℝ^{n×n}`,
> `B∈ℝ^n`, `C∈ℝ^{1×n}` with **`CB≠0`**, and `G_α(s)=C(q_α(s)I−J)^{-1}B` on the principal branch.
> Then `G_α` is **not meromorphic** on any punctured neighbourhood of `s=0`. Consequently `G_α` does
> not agree, on any nonempty open subset of a common domain of analyticity, with the transfer function
> of
> (i) any finite-dimensional rational (latent-state) model, proper or improper, with or without
>     feedthrough;
> (ii) any finite-state delay system — **retarded or neutral**, with **any finite number** of discrete
>     delays, commensurate or not;
> (iii) any finite algebraic combination (sum, product, feedback interconnection) of the above.

*Proof.* Expanding the resolvent, `R(q)=N(q)/Δ(q)` with `deg Δ = n` (monic) and `deg N = n−1` with
leading coefficient `CB ≠ 0`. Hence `{n−1, n} ⊆ E`. If `G_α` were meromorphic near `0` it would in
particular be single-valued, so by Lemma A.0 we would need `α(n−1)∈ℤ` and `αn∈ℤ`, whence
`α = αn − α(n−1) ∈ ℤ`, contradicting `0<α<1`. Therefore `G_α` has a genuine branch point at `s=0`.
Every object in (i)–(iii) is meromorphic on `ℂ` (rational functions trivially; delay transfers because
`sI−A₀−Σ A_je^{−sτ_j}` is entire, so its inverse is meromorphic; algebraic combinations of meromorphic
functions are meromorphic). A function with a branch point cannot coincide with a meromorphic function
on an open set, since agreement on an open set forces agreement of all analytic continuations. ∎

**Why this is strictly stronger than `thm:T4`.**
- Covers **neutral** delay systems, feedthrough and improper rationals, which the asymptotic argument
  cannot reach (`O(ω^{-1})` fails for neutral systems).
- Covers **any finite number** of delays, commensurate or not.
- Removes the dependence on comparing leading asymptotics, hence immune to the `α`-rational collapse
  of §3.
- Proof is two lines from `{n−1,n} ⊆ E`, and makes transparent *why* `CB≠0` is the right hypothesis:
  it forces two **consecutive** exponents to be present, and `gcd`-style divisibility then forces
  `α∈ℤ`.

**Assumptions to state explicitly in the manuscript:** principal branch with the cut along
`(−∞,0]`; `CB≠0`; `0<α<1`; single input/single output (the MIMO version holds entrywise for any entry
with `C_iB_j≠0`).

---

## 5. Adversarial checks performed

| Attack | Result |
|---|---|
| `CB=0` | **Breaks the strong claim.** Counterexample of §3 (exact rational). `Theorem A′` correctly excludes it by hypothesis |
| `α` rational, e.g. `1/2`, `1/3` | Leading-exponent argument collapses (`α·e∈ℤ` possible); `Theorem A′` unaffected because it uses two consecutive exponents |
| Pole–zero cancellation in `R` | Handled: `E` is defined **after** reduction to coprime form; cancellation can only remove exponents, and `CB≠0` guarantees `deg N = n−1` survives |
| Non-collocated / partial observation | These are exactly the `CB=0` cases: criterion decides case by case; no blanket claim admissible |
| Improper / feedthrough rationals | Covered by `Theorem A′` (meromorphy is all that is used) |
| Neutral DDE, multiple delays | Covered by `Theorem A′`; **not** covered by the asymptotic argument |
| Distributed delay / kernel with continuous measure | **Not covered.** `∫e^{−sτ}dμ(τ)` need not be meromorphic. This must be declared as outside the class |
| MIMO with `C_iB_j=0` for all `i,j` | Not covered; requires the higher Markov-parameter index. Declared as excluded |

---

## 6. Recommendation

**Supporting theorem, upgraded and re-proved — not a headline.**

- Replace the asymptotic proof by `Lemma A.0 + Theorem A′` (shorter, exact, strictly more general).
- Keep the high-frequency phase result (`arg G_α → −απ/2`) as a *diagnostic/experimental* corollary,
  not as the proof mechanism.
- State the `CB=0` exception with the `α=1/2, A=2/7` counterexample — this converts an audit
  liability into evidence of rigour, and it is directly relevant because `A=2/7` is the model's own
  regime boundary.
- Novelty positioning (see `NOVELTY_MATRIX.md`, N4): this remains **known-style mathematics**; the
  branch-structure argument is standard in fractional-systems theory. Present it as a clean, complete
  foundation, and do **not** claim it as a contribution.
