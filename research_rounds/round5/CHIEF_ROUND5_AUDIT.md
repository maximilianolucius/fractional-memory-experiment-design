# Chief Audit — Round 5

Date: 2026-08-14

## Verdict

**Researcher R5 as delivered: CONDITIONAL FAIL as a certified atlas.**

**After chief repairs: PARTIAL PASS / GO to Round 6.**

The structural extremal result behind T22 is useful and survives. The headline atlas, however, was overstated in four places: the implemented latent windows were not actually nested; the alpha=0.70 constructive competitors violated the frozen mass cap; the Strong-Allee energy bound is protocol-ray-specific rather than an outer bound for arbitrary safe waveforms; and the d_rob maximization/crossover was not interval-certified despite being called certified.

No large benchmark rerun was needed. All chief work below is lightweight theorem/code auditing and small validation.

---

## P0.1 — Implemented finite-m windows were not nested

Section 6 and the Round-4 governance declare

\[
\ell_m=\min_{j\le m}\ell_j^*,\qquad L_m=\max_{j\le m}L_j^*,
\]

so that \(\mathcal K_m\subseteq\mathcal K_{m+1}\).

But `compute_round5.py` / `compute_round5_atlas.py` used the raw tuned windows from Round 3. They are not nested. Examples:

- m=3: [0.04084, 1.19560]
- m=4: [0.02064, 0.80704]
- m=5: [0.02904, 1.36296]

Thus zero-weight padding did not in general put a stored m=j competitor into every later class, and the running minimum \(\widehat E_m=\min_{j\le m}U_j\) was not justified by the implemented class.

### Chief repair

The theorem hierarchy now uses the true running envelopes. For the headline budgets:

| m | corrected hierarchy window |
|---:|---|
| 4 | [0.020645, 1.195601] |
| 8 | [0.014678, 1.553743] |
| 16 | [0.007419, 1.553743] |
| 32 | [0.007419, 2.991314] |

The explicit constructive mixtures remain admissible because their original windows are contained in these envelopes.

---

## P0.2 — Every alpha=0.70 approximant violated the frozen mass cap

The atlas varies alpha while defining

\[
M_T(\alpha)=\|k_\alpha\|_{L^1(0,T)}+1.
\]

For alpha=0.70, \(M_T=7.26665\), but the raw constructive mixtures had masses between about 8.06 and 10.73. In particular, at the headline budgets:

| m | raw mass | cap | admissible? |
|---:|---:|---:|---|
| 4 | 9.1088 | 7.2667 | no |
| 8 | 9.1065 | 7.2667 | no |
| 16 | 8.0616 | 7.2667 | no |
| 32 | 8.5489 | 7.2667 | no |

Therefore the reported alpha=0.70 \(\widehat E_m^{IA}\) values were not upper bounds produced by competitors in the stated adversarial class.

### Chief repair

For any raw mixture with excessive mass I rescaled all nonnegative coefficients by

\[
s_m=\min\{1,M_T/\|k_m\|_1\}.
\]

The rescaled mixture remains a positive exponential mixture in the rate window and now belongs to \(\mathcal K_m\). I recomputed an interval upper enclosure of the L1 error.

Corrected alpha=0.70 enclosures:

| m | coefficient scale | interval upper error | nested available bound |
|---:|---:|---:|---:|
| 4 | 0.79776 | 1.58076 | 1.58076 |
| 8 | 0.79796 | 1.43595 | 1.43595 |
| 16 | 0.90139 | 1.48068 | 1.43595 |
| 32 | 0.85001 | 1.30750 | 1.30750 |

The alpha=0.85 and 0.95 headline competitors already satisfy their corresponding mass caps.

---

## P0.3 — T22 is a fixed-protocol-ray result, not a bound for all safe waveforms

Theorem T22 fixes a shape \(u_0\) and studies

\[
u=c u_0,\qquad c\ge0.
\]

Its Strong-Allee outer energy bound

\[
\|u\|_2\le B_{\rm Allee}(A,m;u_0)
\]

therefore applies to that ray. It does **not** imply that every arbitrary common-safe input in T20 has energy below this quantity.

This distinction is load-bearing: inserting \(B_{\rm Allee}\) into T20 is valid only after restricting T20's input class to the same protocol ray.

### Chief repair

I added a protocol-restricted corollary and relabeled the atlas as a **positive pulse-ray** atlas. The general T20 theorem remains valid with any independently justified global input-energy cap, such as the universal actuator peak bound.

This reduces the breadth of the R5 headline claim but makes it correct.

---

## P0.4 — The extremal identity is exact; the numerical maximization is not certified

The useful mathematical part survives:

\[
d_{\rm rob}(\mathcal K_m,u_0)
=M_T\max_{\lambda\in[\ell_m,L_m]}\frac{F(\lambda)}{w(\lambda)}.
\]

The proof does not require d(k) itself to be linear. The **state response** is linear in the positive measure; d(k) is sublinear, and the upper bound is attained by the one-mode kernel at the maximizing rate. I corrected the wording accordingly.

However, the code did not perform an outward-rounded global maximization of \(F/w\). `F_over_w_certified` estimates a time derivative on a finer grid and then adds heuristic factors (including a 25% rate margin). That is useful numerical validation, but it is not an interval certificate of the continuum maximum.

### Chief repair

- the structural identity remains `PROVED`;
- the displayed d_rob constants and actuator/Allee crossover are now labeled **high-accuracy numerical estimates**;
- “certified crossover” was removed.

A genuine interval global-max enclosure can be added later, but it is not necessary to continue the mathematics.

---

## P0.5 — Atlas mixed stable and unstable focal Caputo cells

The paper's ecological interpretation is explicitly centered on a certified stable equilibrium and the empirical benchmark is stable-only. The R5 atlas nevertheless included parameter cells beyond the focal Matignon stability boundary.

Across the 432 cells:

- 320 are in the focal Caputo Matignon-stable regime;
- 112 are outside it.

Examples of excluded focal regimes include alpha=0.85 at A=0.38 and 0.42, and alpha=0.95 from A=0.32 upward.

### Chief repair

The headline atlas now hatches these cells and excludes them from stable-regime conclusions.

Corrected stable-regime pulse-ray counts after the nested-window and mass-cap repair:

| alpha | hard >=0.25 | moderate >=0.10 | inconclusive |
|---:|---:|---:|---:|
| 0.70 | 100 | 16 | 12 |
| 0.85 | **112** | 0 | 0 |
| 0.95 | 11 | 11 | 58 |

Thus the focal alpha=0.85 conclusion survives in its correct form: **every displayed Matignon-stable cell in the pulse-ray atlas has a lower bound at least 0.25.**

This is not a theorem about the best arbitrary safe experiment.

---

## Visual audit — Figure 18

The researcher's Figure 18 had title/colorbar collisions and presented out-of-stability cells on equal footing with the stable operating regime. I regenerated it.

Changes:

- more horizontal room;
- concise two-line panel titles;
- explicit “Pulse-ray” scope in all panels;
- focal-unstable cells hatched;
- corrected mass-valid alpha=0.70 data;
- true nested-window hierarchy;
- panel (c) says `grid estimate`, not `certified frontier`;
- explanatory footer distinguishing structural theorem from numerical maximization.

The previous 16 Q1 figures were not changed.

---

## Gate 0B / ecological lift

The negative result from R5 is useful but should not be read as showing that a full ecological-state latent approximation is impossible. It shows only that the particular factorization

\[
h_J^\alpha \approx h_J*k_m
\]

cannot converge through \(\|k_\alpha-k_m\|_1\) because the fractional backbone is not equal to `ODE backbone * fractional kernel`.

The natural Round-6 route is therefore to approximate the **true full fractional transfer**

\[
G_\alpha(s)=C(s^\alpha I-J)^{-1}B
\]

directly by stable finite-dimensional real rational/latent transfers, rather than factorizing through \((sI-J)^{-1}s^{-\alpha}\).

---

## Round-5 status after audit

| Object | Chief status |
|---|---|
| T22 exact single-mode extremal reduction | **PROVED**, fixed protocol shape |
| T22 claim for arbitrary safe waveforms | **NOT PROVED / removed** |
| Nested latent hierarchy | **REPAIRED** |
| alpha=0.70 atlas approximation constants | **REPAIRED with mass-valid interval competitors** |
| R5 d_rob numerical constants | **VALIDATED NUMERICALLY, not interval-certified** |
| “certified crossover” | **WITHDRAWN; numerical bracket only** |
| 432-cell atlas as universal safe-design theorem | **WITHDRAWN** |
| protocol-restricted atlas | **VALIDATED / retained** |
| full ecological-state testing theorem | **OPEN** |

## Novelty assessment

After correcting scope, I do **not** accept the researcher's 9.3–9.5 estimate yet. My current assessment is approximately **9.0–9.2/10** for concept/novelty.

The combination is still unusual and strong: finite-horizon fractional approximation, bounded latent complexity, Strong-Allee safety, and a quantitative testing obstruction are now connected. But the strongest new result is presently kernel-level and pulse-protocol-restricted, while generic safe information limits and safe active model discrimination already have close contemporary prior art.

Round 6 is the opportunity to earn the remaining step by obtaining a full ecological-state theorem from a backbone-consistent finite-dimensional latent approximation, or by closing the paper honestly if that route fails.
