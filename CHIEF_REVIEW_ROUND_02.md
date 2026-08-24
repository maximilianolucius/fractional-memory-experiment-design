# CHIEF REVIEW — ROUND 02

**Branch:** `rescue/aims-desk-rejection`  
**Reviewed commit:** `17f04a86abf148570ff78413de93ce2791b9ee05`  
**Chief verdict:** **ACCEPTED AS A RESEARCH ADVANCE, NOT YET ACCEPTED AS MANUSCRIPT-READY MATHEMATICS**

Round 02 materially improves the rescue. It also exposes that two claims currently marked GREEN/PASS are not yet rigorous enough for publication in the form written. The correct response is not to retreat to the rejected manuscript. We keep the narrative pivot, but Round 03 must close the proof/certification gaps before the manuscript is rebuilt.

---

# 1. Chief decisions

## Decision 1 — narrative pivot: **YES**

The main paper should pivot away from the old message

> “safe designs discriminate less well”

and toward the stronger, true empirical finding:

> **Within the tested strong-Allee protocol, the waveform families that remain non-crossing lose essentially all useful memory-mechanism discrimination at the linear-certificate amplitude, while the most discriminative sustained designs frequently cross the Allee threshold.**

This is a materially different paper from the desk-rejected version.

### Mandatory wording restriction

Do **not** write:

> “no safe excitation discriminates”

or

> “safe discrimination is impossible in this system”

at theorem level yet.

The v4 experiment covers six waveform families, a finite ecological grid, finite sampling, one scoring rule (BIC), and safety is presently measured on a PECE grid rather than validated. The strongest current empirical statement is therefore:

> **None of the evaluated non-crossing waveform families achieved useful discrimination under the specified benchmark protocol; at amplitude 0.063 the best zero-observed-crossing design attained 0.259 macro-accuracy versus 0.25 chance.**

A universal impossibility statement requires either a theorem over an admissible input class or a certified global optimization/upper bound over a declared finite-dimensional design class.

---

## Decision 2 — FCAA split: **NO, NOT NOW**

Do not split Lemma B.1 + Theorem B.2 into a separate FCAA paper at this stage.

Reasons:

1. The endpoint theorem is currently the strongest analytic novelty supporting the CNSNS rescue. Removing it now would make the main manuscript look more like a benchmark paper.
2. The proof of Theorem B.2 still has gaps in the exact constant and in the way the trapezoidal theorem is invoked; Round 03 must repair them before we decide whether it is independently publishable.
3. The novelty search for endpoint-inclusive positive-SOE approximation is not yet deep enough to justify a standalone FCAA priority claim.
4. A later standalone analysis paper would be stronger if it adds an optimality/lower-bound result, not merely the current upper bound.

**Revisit the split only if Round 03 obtains either:**

- a fully rigorous sharp/near-sharp endpoint theorem plus a lower complexity bound; or
- a clearly distinct best-approximation result that is too large to remain supporting analysis in the CNSNS paper.

For now, keep B.1/B.2 in the rescued paper.

---

## Decision 3 — journal: **CNSNS remains the provisional primary target**

The paper that now exists is best described as nonlinear/fractional dynamics + mechanism discrimination + validated/certified numerics + an ecological safety obstruction. That remains a natural CNSNS profile.

Do not migrate the LaTeX template yet. Content and theorem status must stabilize first. Journal formatting begins only after Round 03 scientific gates close.

---

# 2. What Round 02 genuinely established

## 2.1 Kernel error is not response error — **important correction**

The operator bridge correctly identifies the central distinction:

\[
E_m^K=\|K_\alpha-K_m\|_{L^1}
\qquad\text{versus}\qquad
E_m^G=\text{input-to-observed-response discrepancy}.
\]

The naive contraction route fails because the relevant gain exceeds one on the manuscript horizon. The large Grönwall amplification shows that the Round-01 `m=64,128` ecological floors obtained directly from kernel errors were unjustified. Their retraction is correct.

This is scientifically valuable even though it weakens a headline number: the rescue is now separating the abstract memory approximation problem from the actual ecological response problem.

---

## 2.2 Safe-amplitude v4 reveals a real safety/informativeness conflict — **EMPIRICAL, strong**

The completed `amp=0.050` and `amp=0.063` runs show a clear regime separation:

- high-discrimination sustained designs often cross the Allee threshold;
- transient designs can remain non-crossing at the same nominal amplitude;
- among the zero-observed-crossing designs at `amp=0.063`, the best macro-accuracy is only `0.259` versus `0.25` chance.

This is a strong result for the benchmark protocol. It should become the ecological headline **after validated safety classification is added**.

The result also shows why the linear gain certificate must never be called a nonlinear safety certificate.

---

## 2.3 Lemma B.1 — **accepted as PROVED**

The scale-invariance result for the best relative `L^1` positive-SOE approximation is clean:

\[
\varepsilon_m^{\rm rel}(\alpha,T)
=
\varepsilon_m^{\rm rel}(\alpha,1).
\]

This is simple but useful, and it removes horizon dependence from the norm actually used in the approximation layer.

---

# 3. Chief re-openings: claims that are not yet GREEN

## 3.1 Theorem B.2: root-exponential rate is plausible; the **exact theorem as written is not yet accepted**

The Round-02 file states

\[
\varepsilon_m^{\rm rel}
\le A(\alpha)e^{-\pi\sqrt{\alpha(1-\alpha)}\sqrt m}
\]

and additionally claims that

\[
m\ge
\frac{\log^2(1/\varepsilon)}{\pi^2\alpha(1-\alpha)}
\]

“suffices.” The root-exponential conclusion is credible, but the present proof does not yet justify that exact boundary constant or the displayed sufficiency statement.

### Gap B2.1 — finite truncation versus infinite trapezoidal theorem

Step 8 cites the exponentially convergent trapezoidal-rule theorem for strip-analytic functions, but the constructed approximant is a **finite truncated left-node sum** on `[s_min,s_max]`. The proof must explicitly decompose:

1. infinite log-grid discretization error;
2. negative-index truncation;
3. positive-index truncation;
4. endpoint-integrated error.

Do not apply an infinite-grid theorem directly to the finite rule without this decomposition.

### Gap B2.2 — taking `d ↑ π/2`

The standard strip theorem gives, for every fixed `d<π/2`, a factor of the form

\[
\exp(-2\pi d/h).
\]

The constants generally deteriorate as `d→π/2`. One cannot simply let `d↑π/2` and retain a uniform prefactor to claim the exact exponent `π^2/h`.

A safe theorem, unless a sharper Mellin/Poisson calculation is supplied, is likely of the form:

> for every `c < π√(α(1−α))`, there exists `A(α,c)` such that
> \[
> \varepsilon_m^{\rm rel}\le A(\alpha,c)e^{-c\sqrt m}.
> \]

If the boundary constant is desired, prove it separately using a quantitative Fourier/Mellin/Poisson-summation argument.

### Gap B2.3 — endpoint balance

The current endpoint estimate contains

\[
\delta L^{1-\alpha}.
\]

With the stated choices `δ^α≈ε` and `L≈\log(1/ε)/δ`, this term scales like

\[
\varepsilon\,\log^{1-\alpha}(1/\varepsilon),
\]

so it is **not** “lower order” relative to `ε`.

Repair options:

- use the exact identity
  \[
  \int_0^\delta K_m(t)dt
  =\sum_j \frac{c_j}{\lambda_j}(1-e^{-\lambda_j\delta})
  \]
  and split modes at `\lambda\approx1/\delta`; this should recover an `O(\delta^\alpha)` endpoint contribution without an artificial `L^{1-\alpha}` factor; or
- choose `δ` with the required logarithmic correction and propagate it through the complexity balance.

### Gap B2.4 — hidden prefactor

If the theorem contains an unspecified `A(α)`, then the statement that a coefficient-one expression in `log(1/ε)` “suffices” is not valid. The complexity statement must include the prefactor/hidden constants, e.g.

\[
m(\varepsilon)
\le C_\alpha\,[\log(A_\alpha/\varepsilon)]^2
\]

or an equivalent asymptotic statement.

### Chief status

- **Root-exponential order:** `PROVISIONALLY PROVED / REQUIRES R3 RIGORIZATION`.
- **Exact constant `π√(α(1−α))`:** `UNPROVED AT THE BOUNDARY AS CURRENTLY WRITTEN`.
- **Coefficient-one sufficiency formula:** `RETRACT UNTIL REPAIRED`.

---

## 3.2 Theorem C′: the response discrepancy must be an **operator norm**, not a fixed-input quotient

`THEOREM_C_PRIME_FINAL.md` defines

\[
E_m^G :=
\frac{\|\mu_F-\mu_m\|_\infty}{\|u\|_\infty}
\]

and then calls the resulting testing bound uniform over every waveform shape.

That is only valid if `E_m^G` is itself a uniform induced gain, for example

\[
\boxed{
\mathcal E_m^G
:=
\sup_{u\ne0}
\frac{\| (\mathcal G_F-\mathcal G_m)u\|_\infty}{\|u\|_\infty}
}
\]

or if it is upper-bounded by a certified impulse-response quantity such as

\[
\|g_F-g_m\|_{L^1(0,T)}.
\]

Round 03 must determine exactly what `thm:T23` certifies.

- If T23 certifies an `L^1` Green-function difference, define `\mathcal E_m^G` from that and the uniform theorem survives.
- If T23 certifies only one fixed pulse/waveform response, Theorem C′ must be restricted to that design and cannot be called waveform-uniform.

This is a hard semantic/mathematical gate.

---

## 3.3 Theorem D-NL numerical constant is **not certified yet**

The symbolic sufficient-ball inequality

\[
\Gamma_B U + \Gamma_R M_2(r)r^2\le r
\]

is legitimate as a conditional theorem.

However, the current `M_2(r)` is described as measured using `720` directions × `40` radii. A sampled maximum is **not** a rigorous supremum over the ball. Likewise `Γ_B` and `Γ_R` must be enclosed rigorously if the manuscript calls `U_NL` a certificate.

Therefore:

- the **symbolic theorem** can remain;
- `U_NL(0.05)=1.51e−3` is currently a **numerical estimate of a sufficient bound**, not a validated certificate, unless interval/analytic enclosures for `M_2,Γ_B,Γ_R` are supplied.

Round 03 must produce either:

1. analytic Hessian bounds for `M_2(r)` + rigorous/interval gain bounds; or
2. interval subdivision over the ball and validated convolution/resolvent bounds.

The analytic impossibility of an inward-pointing rectangle around the coexistence equilibrium is separate and appears sound; keep it as a negative structural lemma.

---

## 3.4 The nonlinear discrimination factor must be re-derived

The current nonlinear lift writes a bound schematically as

\[
\|C(\xi_F-\xi_m)\|_\infty
\le A_{NL}(r,T) E_m^G\|u\|_\infty.
\]

But `E_m^G` elsewhere is already defined as a response-level gain. Multiplying it by another resolvent amplification factor risks double-counting unless a new forcing/error object is explicitly defined.

Round 03 must write the nonlinear difference equation from scratch and identify exactly which quantity is multiplied by `A_NL`:

- kernel/operator perturbation;
- linear Green-function difference;
- or nonlinear response difference.

No symbol may change semantic level across the proof.

---

# 4. The practical-impossibility story: accepted, but with a stronger falsification protocol

The current v4 result is strong enough to motivate the paper, but not to establish universal impossibility.

Round 03 must attempt to **break the negative result**.

The Researcher must search aggressively for a safe-but-informative input outside the six original waveform families.

If one is found, that improves the paper by identifying the actual safe frontier.

If none is found, that is useful only as empirical evidence unless the design class is globally bounded/certified.

The preferred upgrade is:

\[
\max_{u\in\mathcal U_K}
\;\mathcal J(u)
\quad\text{s.t.}\quad
x_j(t;u)\ge A+\delta
\;\forall t,\forall j\in\mathcal M,
\]

where `\mathcal U_K` is a declared finite-dimensional input family and `\mathcal M` is the rival mechanism set.

Suggested `\mathcal U_K`:

- piecewise-constant controls with `K=4,6,8` segments;
- finite Fourier/multisine coefficients with bounded peak amplitude;
- pulse-train/multiscale families.

Suggested deterministic objective before BIC Monte Carlo:

\[
\mathcal J(u)=
\min_{i\ne j}
\frac{\|S_n(\mu_i(u)-\mu_j(u))\|_2}{\sigma},
\]

or a weighted/maximin variant.

Run a broad adversarial search first. Then validate the best candidates. A global interval upper bound over a modest `K` would be a major upgrade; it is a stretch goal, not assumed feasible.

---

# 5. Amp=0.100 run

Let the existing Orion/Aureus `amp=0.100` control finish. Do not restart it. Append the result to the v4 report and compare cell-by-cell against frozen v3 using identical seeds.

This is a reproducibility control, not a blocker for starting Round 03.

---

# 6. Round-03 priority order

1. **Rigorize Theorem B.2** and downgrade the exact constant if necessary.
2. **Fix the response-operator semantics** in Theorem C′/T23.
3. **Validated safety classification** for the candidate non-crossing designs.
4. **Certify response-level approximants at `m=64,128`** if computationally feasible.
5. **Adversarial safe-design search** beyond the six historical waveform families.
6. **Re-derive nonlinear discrimination** with no kernel/response semantic mixing.
7. Complete `amp=0.100` reproducibility control.
8. Execute the mandatory manuscript corrections only after the claims above stabilize.
9. Rebuild title/abstract/contributions around the corrected negative result.
10. Prepare CNSNS compliance matrix; template migration waits until the end of the round.

---

# 7. Publication-level claim hierarchy after Chief review

## PROVED / accepted

- Lemma B.1 — horizon invariance of best relative `L^1` positive-SOE approximation.
- Theorem A′ structural separation, subject to its stated channel conditions and counterexample.
- Exact Gaussian simple-vs-simple testing identity.
- Structural impossibility of the proposed inward-pointing rectangle around the coexistence equilibrium, if the algebra in the Round-02 file is preserved exactly.

## PROVISIONAL — proof/certification repair required

- Root-exponential endpoint complexity theorem B.2.
- Waveform-uniform Theorem C′.
- Numerical `U_NL` certificate.
- Nonlinear testing ceiling.

## EMPIRICAL

- v4 crossing rates.
- v4 macro-accuracy values.
- “best zero-observed-crossing design = 0.259 at amp=0.063.”

## PROHIBITED

- universal “no safe excitation discriminates” statement;
- kernel-level `m=64,128` ecological floors;
- `0.063` as nonlinear-safe amplitude;
- `U_NL=1.51e−3` as rigorous certificate before constant validation;
- exact `c(α)=π√(α(1−α))` boundary constant before the strip-limit gap is closed;
- a waveform-uniform bound using a fixed-input `E_m^G`.

---

# 8. Round-02 verdict

Round 02 is **scientifically successful** because it changed our beliefs in the correct direction:

- one attractive Round-01 ecological claim was retracted;
- the benchmark exposed the failure of the linear-safety interpretation;
- the endpoint approximation problem produced a promising analytic theorem;
- the negative ecological result became substantially sharper.

That is exactly what a rescue round should do.

But the eight Researcher gates are **not all publication-PASS yet**. Round 03 is therefore a proof-and-certificate round, not merely a prose-rewrite round.
