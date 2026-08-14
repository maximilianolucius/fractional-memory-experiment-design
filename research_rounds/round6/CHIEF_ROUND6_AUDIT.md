# Chief Audit — Round 6

Date: 2026-08-14

## Executive verdict

**Researcher R6 as delivered:** CONDITIONAL FAIL on the claimed *full ecological-state + hierarchy-wide Strong-Allee closure*.

**After chief repairs:** **PASS for a narrower but mathematically strong result:** an exact **prey-to-prey ecological response** decomposition, interval-certified finite-state approximation, and a Gaussian testing lower bound under a physical pulse/actuator budget.

This is enough to terminate the novelty campaign. I do **not** recommend a seventh mathematical novelty round.

The remaining work should be Q1 closeout: manuscript compression, journal targeting, supplementary-material split, and editorial polish.

---

## 1. What R6 genuinely closes

For the linearized Caputo predator-prey system, the focal prey channel is

\[
G_\alpha(s)=e_1^\top(s^\alpha I-J(A))^{-1}e_1.
\]

For the conjugate eigenpair \(\lambda,\bar\lambda\), the scalar Mittag-Leffler mode admits the pole/branch representation

\[
e_\alpha(t;\lambda)
=
\frac{s_0}{\alpha\lambda}e^{s_0t}
+
\int_0^\infty e^{-rt}\varphi_\lambda(r)\,dr,
\qquad
s_0=\lambda^{1/\alpha},
\]

in the declared sector. The pole pair is realizable **exactly** by a stable real two-state integer-order block. The signed branch remainder can be approximated by stable first-order modes.

This directly bypasses the false factorization route

\[
(s^\alpha I-J)^{-1}\ne (sI-J)^{-1}s^{-\alpha}.
\]

### Accepted R6 theorem

For the displayed Matignon-stable cells and \(m\in\{4,8,16,32\}\), there is an explicit strictly proper stable finite-state prey-response surrogate \(g_m\) with

\[
\|g_\alpha-g_m\|_{L^1(0,T)}
\le
\widehat E_m^{\rm state}.
\]

The shipped enclosures are genuinely interval-based on the finite rate intervals plus an analytic tail bound.

For \(\alpha=0.85\), \(T=12\):

| A | m=4 | m=8 | m=16 | m=32 |
|---|---:|---:|---:|---:|
| 0.25 | 0.5334 | 0.1254 | 0.0273 | 0.00692 |
| 0.30 | 0.4706 | 0.0898 | 0.0204 | 0.00662 |

These are useful and non-vacuous.

---

## 2. Independent numerical audit I ran

The researcher's full validator is extremely expensive because it evaluates a long Mittag-Leffler series on a very dense time grid. I therefore wrote a lightweight **independent floating-point checker**. It does not certify anything; it cross-checks the interval enclosures through a mathematically independent route.

A subtle numerical issue appeared during the audit: a coarse **uniform** time grid strongly overestimates the \(L^1\) error because the fractional impulse response has an integrable near-zero singularity \(t^{\alpha-1}\). I fixed the audit by using the transformed grid

\[
t=T x^3,
\]

which resolves the singular endpoint.

All eight focal cells then pass comfortably:

| A | m | independent float L1 | certified upper | ratio |
|---|---:|---:|---:|---:|
| 0.25 | 4 | 0.09978 | 0.53343 | 0.187 |
| 0.25 | 8 | 0.03511 | 0.12536 | 0.280 |
| 0.25 | 16 | 0.00637 | 0.02730 | 0.233 |
| 0.25 | 32 | 0.00183 | 0.00692 | 0.265 |
| 0.30 | 4 | 0.09207 | 0.47055 | 0.196 |
| 0.30 | 8 | 0.03312 | 0.08982 | 0.369 |
| 0.30 | 16 | 0.00781 | 0.02039 | 0.383 |
| 0.30 | 32 | 0.00175 | 0.00662 | 0.265 |

Thus the apparent failure produced by my first coarse-grid check was a **checker discretization artifact**, not a defect in T23. I corrected the checker and preserved the result in `chief_round6/lightweight_check.json`.

---

## 3. Main mathematical overclaim in the researcher R6

The researcher's ledger called T23 a **full ecological-state approximation theorem**. That is too strong.

The theorem controls

\[
e_1^\top(s^\alpha I-J)^{-1}e_1,
\]

namely **prey input -> prey output**. It does not yet control the full vector state, the predator channel, or a matrix transfer norm.

I therefore changed the manuscript language to:

> **Certified ecological prey-response approximation**

and consistently describe it as linearized and prey-channel specific.

This is still a significant advance over the kernel-only theorem from R4/R5.

---

## 4. T24 does not pass the intended R6 hard gate

The researcher defined a broad response class \(\mathcal G_m\) using:

- stable poles,
- a pole-radius restriction,
- a finite-horizon \(L^1\) mass cap.

The proposed Strong-Allee extremizer was

\[
g(t)=-a e^{-rt},
\]

with \(a\) chosen to saturate the mass cap.

The problem is that this class has **no independent residue/gain cap**. For large \(r\), the residue can become very large while the finite-horizon \(L^1\) mass remains fixed. The witness also does not retain the exact two-state pole block used in the approximation construction.

So T24 is mathematically valid for that broad mass-only response class, but it does **not** close the intended theorem for a physically constrained ecological latent hierarchy.

I therefore removed T24 from the headline theorem chain and did not use its very small Allee budgets in the state-response testing figure.

The manuscript now states explicitly that hierarchy-wide Strong-Allee safety for physically constrained full-state latent rivals remains open.

---

## 5. What testing theorem survives

Using the certified response approximation and a bounded observation operator \(S\),

\[
C_{\rm obs}
=
\frac12\|R^{-1/2}S\|^2,
\]

we have for any valid input energy bound \(B\):

\[
D_{\rm KL}
\le
C_{\rm obs}
(\widehat E_m^{\rm state})^2B^2.
\]

For the actual rectangular pulse used by the experiment design,

\[
\|u\|_\infty\le0.10,
\qquad
\Delta=1.44,
\]

so the protocol-specific physical cap gives

\[
B\le0.10\sqrt{1.44}=0.120.
\]

At \(\sigma=0.10\), the corresponding Pinsker minimax-error lower bounds are:

| A | m=4 | m=8 | m=16 | m=32 |
|---|---:|---:|---:|---:|
| 0.25 | 0.340 | 0.462 | 0.492 | 0.498 |
| 0.30 | 0.359 | 0.473 | 0.494 | 0.498 |

This is a clean result: as latent complexity increases, the certified finite-state rival can become so close to the fractional prey response that even the physical pulse protocol has a testing error forced toward chance.

Crucially, this statement **does not pretend that the physical pulse cap is itself an Allee-safety theorem for the entire state-response hierarchy**.

---

## 6. Literature/novelty correction

The pole/branch contour technology should not itself be presented as new. Pole-aware contour evaluation and rational approximation of Mittag-Leffler functions are established numerical tools; finite-Prony versus fractional branch-cut structure also has prior literature.

Likewise, general safe information limits and safe active model discrimination under state/input constraints already exist in contemporary work.

I added citations and rewrote the related-work statement so that the novelty claim is now the **joint construction** rather than any one generic component:

1. certified strong-Allee ecological backbone;
2. fractional-vs-latent finite-horizon approximation hierarchy;
3. protocol-restricted ecological safety interface;
4. interval-certified prey-response finite-state approximation;
5. testing lower bounds showing complexity-driven loss of memory identifiability.

This is a much more defensible Q1 novelty position.

---

## 7. Visual audit

### Figure 11

The expensive Figure 11 from the visual round is untouched. SHA-256 comparison against the post-R5 chief package confirms it is byte-identical. **Do not rework it.**

### Figure 13

I did change Figure 13 because it contained a conceptual error: it stated that all rivals shared an identical Jacobian backbone, while the actual DDE and latent equations use their own generators.

The corrected figure now says:

- common experimental operating point;
- common input/observation channels and units;
- ODE/Caputo share \(J(A)\);
- DDE/latent are calibrated alternative response laws.

This is a mathematical correction, not an aesthetic redesign.

### New R6 Figure 19

The researcher's three-panel version relied on T24's broad mass-only Strong-Allee budget. I replaced it with a two-panel figure:

- certified prey-response approximation versus \(m\);
- testing lower bound under the actual pulse peak cap.

It is visually cleaner and exactly matches the theorem that survives the audit.

### Other visuals

Against the R5 chief package, all earlier figures except Figure 13 are byte-identical; Figure 19 is new. There is **no reason for another general figure campaign**.

---

## 8. Publication-language cleanup performed

The manuscript still contained internal workflow language such as:

- “chief rerun”,
- “Round-6 hard gate”,
- “researcher derived”,
- “Round-5 chief-audit artifact”.

I removed this language from the active manuscript. Those details belong in audit artifacts, not in a journal paper.

I also corrected the Introduction, which still claimed that all four rival mechanisms shared the same Jacobian skeleton despite the repaired Section 3.

---

## 9. Build status after chief corrections

Clean build result:

- **80 pages**;
- **0 undefined citations**;
- **0 undefined references**;
- **0 LaTeX/package warnings on the final pass**.

The page increase relative to the previous build is from the added contemporary related-work references.

The main remaining editorial problem is length, not compilation.

---

## 10. Final novelty assessment

My assessment after R6 is:

\[
\boxed{\text{Novelty / paper concept: approximately }9.1\text{--}9.3/10}
\]

I would **not** assign 9.5 yet because:

- the new theorem is one linearized prey channel, not the full state;
- the strongest R6 Strong-Allee safety closure did not survive the physically constrained hierarchy audit;
- finite-state/rational approximations of Mittag-Leffler responses are not new in isolation;
- safe information limits and safe model discrimination are also not new in isolation.

What *is* distinctive is the way these ingredients are tied together around fractional-memory identifiability in a certified strong-Allee ecological system.

That is strong enough. A seventh novelty round is more likely to create scope creep than to improve the submission.

---

## 11. Decision

\[
\boxed{\textbf{STOP mathematical novelty rounds. Proceed to Q1 closeout.}}
\]

Next priorities:

1. compress the 80-page manuscript;
2. move proof/checker detail and secondary diagnostics to Supplementary Material;
3. select the target journal and adapt structure/style;
4. run one final claim-to-evidence audit;
5. keep the current figure system essentially frozen.
