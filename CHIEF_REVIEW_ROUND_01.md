# Chief review — Round 01

**Branch:** `rescue/aims-desk-rejection`  
**Reviewed commit:** `c0bf63901afae27cbc43a656b5c2315e11d85311`  
**Date:** 2026-08-24  
**Decision:** **ROUND 01 ACCEPTED WITH MANDATORY CORRECTIONS; proceed to Round 02.**

---

## 1. Executive decision

Round 01 materially improved the paper. Three items are worth keeping:

1. **Lemma B.1 (scale invariance)** is correct and useful: for the best positive `m`-term exponential approximation of the Caputo kernel in **relative** `L¹(0,T)`, the optimum is independent of the horizon `T`.
2. **Theorem C′** gives the correct simple-Gaussian two-point testing formula and removes the weak/vague Pinsker presentation.
3. **Theorem D** identifies the right architecture for a safety–informativeness result.

However, the Chief does **not** accept the current Round-01 wording of Theorem D as the final headline theorem, and does **not** accept the asymptotic interpretation currently attached to computation C-1. There are four load-bearing issues that Round 02 must resolve before manuscript rewriting can be considered scientifically safe.

---

# 2. Mandatory Chief corrections to Round 01

## C1. C-1 does **not** establish an asymptotic convergence class

The following statements in `THEOREM_B_COMPLEXITY_LAW.md`, `ROUND_01_DECISION.md`, and the rescue ledger are too strong:

- “convergence is sub-exponential”;
- “strictly faster than algebraic” as an asymptotic statement;
- `m(ε)=O(log^κ(1/ε))`, `κ∈[1,2]`, inferred from the finite sweep.

A finite fit over `m≤128` cannot determine the asymptotic class, and the data do not even exclude `β=1` for all `α`. In particular, calling the convergence **sub-exponential** while reporting competitive `β=1` fits is internally inconsistent.

### Required replacement

Until proved, state only:

> “Over the computed range `m≤128`, stretched-exponential models fit the observed errors substantially better than a single algebraic model for the tested orders. The asymptotic convergence class is unresolved.”

No big-O complexity claim may be inferred from C-1.

### New analytical target

The natural conservative target is a **root-exponential upper bound** (equivalently `m(ε)=O(log²(1/ε))`) for positive exponential sums in relative `L¹(0,T)` including `t=0`. This is consistent with the endpoint singularity and with combining an away-from-zero SOE estimate with an endpoint cutoff. If a stronger rate is proved, use it; do **not** assume geometric `e^{-cm}` convergence in advance.

---

## C2. Do not conflate the bare Caputo kernel with the ecological input→output Green function

`THEOREM_C_TESTING_OBSTRUCTION.md` writes

`Δμ = (k_α-k_m)*u`,

while `THEOREM_D_SAFETY_INFORMATION.md` alternates between:

- the **bare memory kernel** `k_α(t)=t^{α-1}/Γ(α)` and its SOE approximation; and
- the **prey-input→prey-output impulse response** certified by T23.

These are not automatically equivalent objects.

For the linearized fractional state-space system, replacing the memory operator changes the **resolvent** of the state equation. A bare-kernel `L¹` error does not, by itself, imply the same numerical `L¹` error for the observable transfer kernel unless an explicit resolvent perturbation estimate is proved.

### Required Round-02 audit

Introduce distinct notation, for example:

- `K_α`, `K_m`: memory kernels / diffusive representation;
- `G_α`, `G_m`: actual input→observed-output Green functions;
- `E_m^K = ||K_α-K_m||_1`;
- `E_m^G = ||G_α-G_m||_1`.

Then prove either

`E_m^G ≤ C_res E_m^K`

with an explicit, valid `C_res`, or route the testing theorem **only through `E_m^G`** (T23 for the ecological specialization).

**Until that bridge is proved, the C-1 kernel errors at `m=64,128` may not be fed directly into the ecological Theorem D.** The reported `0.474` and `0.4997` floors are therefore **not yet accepted as certified ecological floors**.

The T23 prey-response enclosure at `m=32`, by contrast, is the correct kind of object for an ecological input-output testing statement, subject to the safety corrections below.

---

## C3. “Safe inputs” is too broad: the current theorem only covers a sufficient amplitude ball

The current derivation proves:

`||u||∞ ≤ U(δ)=ρ(δ)/Γ_T  ⇒  the LINEARIZED fractional trajectory stays inside the prescribed state ball.`

It does **not** prove the converse. The frozen benchmark already contains transient inputs with amplitudes larger than `U(δ)` that remain safe.

Therefore the theorem must not say “uniformly over every safe input.” It may currently say only:

> “uniformly over every input in the certified amplitude class `||u||∞≤U(δ)`.”

This distinction is essential. The amplitude ball is a conservative **inner approximation** of the safe experiment set.

---

## C4. Linearized state containment does not certify nonlinear ecological safety

The Round-01 assumption

> “Linearization valid on the excursion set (guaranteed a posteriori by `||ξ||∞≤ρ(δ)`)”

is not justified. Staying in a state ball does not prove that the nonlinear trajectory is close to its linearization.

This is the central reason Round 02 **must attempt the nonlinear lift** rather than shipping the current theorem immediately.

The desired route is to write the nonlinear perturbation dynamics in mild/Volterra form

`D_C^α ξ = Jξ + Bu + R(ξ)`, `R(0)=DR(0)=0`,

obtain an explicit remainder bound on the candidate safe ball,

`||R(ξ)|| ≤ M_R(r)||ξ||²`

(or a suitable local Lipschitz form), and close an invariant-ball inequality such as

`Γ_B U + Γ_R M_R(r) r² ≤ r`.

This would produce a genuinely nonlinear certified amplitude

`U_NL(δ) = [r - Γ_R M_R(r)r²]/Γ_B`

or a sharper analogue.

Then derive a nonlinear model-discrepancy estimate by a fractional Volterra/Grönwall argument.

---

# 3. Additional issue: safety under model uncertainty

The current `Γ_T` is computed for the fractional model. If the experiment is advertised as **safe mechanism discrimination**, safety should normally hold regardless of which admissible mechanism is true.

Round 02 must explicitly choose and state one of two semantics:

1. **Robust safety (preferred):** safety for the fractional model **and all rival latent models in the declared hierarchy/class**. Prove a common gain/remainder bound or a hierarchy-uniform safe input set.
2. **One-sided safety:** safety is guaranteed only under the fractional reference model. This is mathematically valid but scientifically weaker and must be named as such.

The preferred paper headline requires option 1.

---

# 4. Status of the three Chief decisions requested by the Researcher

## Decision 1 — Journal

**Do not resubmit the present reconstruction to AIMS Mathematics.** The rejection was on novelty/general significance, and Round 01 has improved correctness more than depth. A near-term AIMS resubmission risks a second desk rejection.

**Provisional primary fit:** *Communications in Nonlinear Science and Numerical Simulation (CNSNS)*, because the paper combines nonlinear modeling, theoretical analysis and numerical simulation in a biological nonlinear system.

**Stretch target:** *Fractional Calculus and Applied Analysis* only if Round 02 produces a genuinely nontrivial endpoint-positive-SOE theorem and a clean nonlinear lift.

**Alternative:** *Chaos, Solitons & Fractals* only if the nonlinear/physical insight becomes strong enough that numerics are clearly supporting rather than driving the paper.

The exact journal is locked **after Round 02**, because the correct venue depends on which mathematics actually closes.

Regardless of journal, the submission rule remains:

- **100% of mandatory journal requirements PASS**;
- **≥99% of the complete applicable checklist PASS**;
- official instructions and official TeX template re-downloaded and re-checked within 24 h of submission.

---

## Decision 2 — Nonlinear extension of D

**YES. Mandatory Round-02 attempt.**

Do not ship the linearized result yet. Spend one focused round trying to close the nonlinear Volterra/Grönwall lift with explicit constants.

**Stop-loss:** if the nonlinear lift fails after a serious, documented attempt, preserve the linear theorem but rename it explicitly as a **linearized certified-excitation information ceiling**, remove any nonlinear ecological safety implication, and choose the journal accordingly.

---

## Decision 3 — Safe-amplitude benchmark

**AUTHORIZED, with a stricter protocol.**

Do **not** overwrite frozen v3. Create a new benchmark namespace/version.

Stage A may run immediately at amplitudes below the Round-01 linear certificate, but it must be labelled **linear-certificate diagnostic**, not final nonlinear-safe evidence.

Required amplitudes should include at least:

- `0.050` (clear margin below `U(0.05)=0.0634`);
- approximately `0.063` (near the linear bound);
- the frozen `0.100` baseline for direct comparison.

Use the same design families, sampling schedule, model grid, seeds and scoring pipeline whenever possible so that amplitude is the principal changed variable.

After `U_NL(δ)` is proved, run the **final nonlinear-safe benchmark** at or below that amplitude.

For each design/model report:

- minimum `x(t)-A`;
- crossing rate;
- classification/confusion metrics;
- BIC separation;
- realized input/output gain;
- whether safety holds under each rival mechanism, not only the fractional reference, if robust-safety semantics are adopted.

---

# 5. What Round 01 did establish

Accepted after the corrections above:

- **Lemma B.1:** PROVED.
- **Theorem A′:** useful supporting theorem/counterexample structure; novelty claim must remain conservative.
- **Theorem C′:** PROVED for the simple equal-covariance Gaussian observation model once the discrepancy object is correctly defined as the actual output response.
- **Theorem D architecture:** PROMISING but **not yet final GREEN** as an ecological safety theorem.
- **T23 `m=32` prey-response enclosure:** valuable certified numerical bridge.
- Theorem 9.3 defect and OED/Bayesian overclaims identified: mandatory manuscript fixes.

---

# 6. Chief target for Round 02

A successful Round 02 should turn the paper's main chain into:

`robust nonlinear safety`
`⇒ certified admissible excitation set`
`⇒ actual input-output discrepancy ceiling`
`⇒ exact Gaussian testing floor`
`⇒ monotone safety–informativeness trade-off`.

In parallel, the approximation layer should aim for a rigorous endpoint-inclusive positive-SOE complexity result, preferably of root-exponential type.

If both close, the paper changes category materially. If only the linear chain survives, we will still have a correct paper, but we will position it as applied nonlinear/fractional dynamics rather than as a broad mathematical theorem paper.
