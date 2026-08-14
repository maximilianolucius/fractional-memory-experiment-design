# Chief Audit — Round 4

Date: 2026-08-14

## Verdict

**Round 4 researcher submission: CONDITIONAL FAIL as submitted.**

**After the chief repairs in this package: PARTIAL PASS / GO TO ROUND 5 WITH A HARD GATE.**

The central testing idea survives.  However, the researcher integrated it into the manuscript before two load-bearing numerical/mathematical issues were actually closed.  I repaired the parts that can be repaired locally without a new research campaign.  The genuinely unresolved item is the hierarchy-uniform Strong-Allee / ecological-state lift; that is now the first gate of Round 5.

---

## P0.1 — The claimed `certified` L1 errors were not certificates

The Round-4 prompt explicitly required that ordinary quadrature not be called certified.  Nevertheless `compute_round4.py` used `scipy.integrate.quad` and declared

> adaptive quadrature with returned error estimate added = rigorous certificate.

That is not an accepted proof object.  QUADPACK's returned error estimate is a numerical estimator, not an outward-rounded interval enclosure.

### Chief repair performed

I added

`chief_round4/validate_Ebar_interval.py`

which independently encloses every displayed explicit mixture by interval arithmetic.  On each body subinterval I, it encloses the entire range of

`k_alpha(t)-k_m(t)`

and uses

`int_I |f| <= |I| sup_I |f|`.

The singular head is bounded by the exact integrals of the two positive kernels.  The resulting interval upper bounds are:

| m | interval upper | old quad estimate | uplift |
|---:|---:|---:|---:|
| 1 | 0.924877 | 0.923446 | 0.155% |
| 2 | 0.568627 | 0.567308 | 0.233% |
| 3 | 0.540636 | 0.539241 | 0.259% |
| 4 | 0.352397 | 0.351163 | 0.351% |
| 5 | 0.374891 | 0.373533 | 0.363% |
| 6 | 0.247850 | 0.246643 | 0.489% |
| 8 | 0.264516 | 0.263173 | 0.510% |
| 12 | 0.235528 | 0.234344 | 0.505% |
| 16 | 0.199831 | 0.198605 | 0.617% |
| 24 | 0.213323 | 0.212033 | 0.608% |
| 32 | 0.133856 | 0.132451 | 1.061% |

Because the latent classes are nested, the theorem now uses the running best constructive enclosure

`Ehat_m^IA = min_{j<=m} U_j^IA`,

so the bound itself respects the class nesting even when a newly tuned explicit mixture is worse than a smaller padded one.

**Consequence:** the non-vacuity conclusion survives; the constants move only slightly.

---

## P0.2 — The observation operator was missing from Theorem T20

The submitted proof wrote

`KL = (1/(2 sigma^2)) ||S((k_alpha-k_m)*u)||^2 <= Ebar^2 B^2/(2 sigma^2)`

without a norm bound on S.  That implication is false for a general observation operator.

There was a second conflation: the research notes called continuous Gaussian observation and fixed-variance point sampling `equivalent`.  They are not equivalent under the L2 bound used in the proof.  In particular, point evaluation is not a bounded operator on bare L2.

### Chief repair performed

T20 now states a bounded operator

`S : L2(0,T) -> R^q`

with common covariance R and the explicit constant

`C_obs = (1/2)||R^{-1/2} S||^2`.

The theorem is

`U_m = C_obs (Ehat_m^IA)^2 B_eff^2`

followed by the testing lower bound.

The numerical non-vacuity example is now explicitly a **normalized bounded Gaussian observation experiment** (`||S||<=1`, `R=sigma^2 I`), not a claimed guarantee for the point-sampled benchmark.

This distinction is important: the benchmark remains an empirical validation layer, not the numerical instantiation of T20.

---

## P0.3 — The minimax object and the adversarial step were under-defined

The submission referred to a `robust minimax error` but did not define its quantifier order.  It also said the adversary chooses a competitor `attaining this bound`, although the constructive error is only an upper bound and no attainment of the infimum was proved.

### Chief repair performed

T20 now defines the equal-prior composite risk explicitly:

`inf_u inf_test sup_{k in K_m} binary risk`.

The proof uses one **explicit padded constructive competitor** whose interval-enclosed L1 error is known.  A composite problem is at least as hard as that fixed two-point subproblem; no attainment claim is needed.

Pinsker is clipped at zero, and the Gaussian two-point formula is retained as the strongest of the displayed elementary bounds.

---

## P0.4 — T21 had the wrong safety quantifier

The submitted theorem defined safety using

`sup_t [x* + H_x u] >= A+eta`,

which only requires the trajectory to be above the floor at *some* time.  Ecological safety requires

`inf_t [x* + H_x u] >= A+eta`.

The proof also claimed the one-sided safe set was balanced under negative scaling, which is false.

### Chief repair performed

- `sup_t` -> `inf_t`;
- removed the negative-scaling symmetry claim;
- used a strict half-margin scaling `rho_eta/(2 delta_omega)` in the high-frequency construction.

The resulting Riemann-Lebesgue argument is now aligned with the actual all-times state floor.

---

## P0.5 — The Strong-Allee crossover is not yet a theorem over K_m

The `A ~= 0.32` crossover uses `d_rob` computed over the **five locked benchmark realizations**.  It is not a supremum over the frozen hierarchy `K_m`.

Therefore it cannot yet be inserted as the Allee-dependent `B_eff` in T20 for the full adversarial class.

This is the main unresolved mathematical issue.

### Chief correction to manuscript wording

The crossover is now called what it is:

**a protocol-relative diagnostic of the locked benchmark rival set.**

For the hierarchy-level theorem, the currently valid outer budget is the actuator peak cap.  Round 5 must either:

1. obtain a hierarchy-uniform Allee-dependent outer bound for the declared protocol class; or
2. prove that the hierarchy is too broad for such a bound and narrow the experimental rival class explicitly.

Until then, the paper does **not** yet have a theorem in which all three of

`fractional approximation x latent complexity x Strong-Allee safety`

enter simultaneously.

---

## P0.6 — The finite table did not prove E_m -> 0 for the frozen numerical windows

The T9b theorem proves arbitrary L1 approximation when truncation windows are allowed to expand appropriately.  A finite list of tuned running windows at m <= 32 does not by itself prove asymptotic convergence of the specific frozen numerical hierarchy.

### Chief repair performed

The manuscript now separates:

- T9b: the analytic unrestricted constructive approximation theorem;
- the finite-m frozen hierarchy used for the current numerical constants.

No `Ehat_m^IA -> 0` statement is inferred from the finite table.

If the final paper wants an asymptotic result *inside the same K_m hierarchy*, Round 5 must define an explicit expanding nested window sequence containing a T9b approximating subsequence.

---

## P1.1 — T20 is still kernel-level, not yet the full ecological input-output theorem

The actual linearized Caputo predator-prey system satisfies a Volterra state equation involving J and B.  The scalar T20 experiment compares

`S(k*u)`

and therefore controls a kernel-probe convolution experiment.  It is not yet a continuous-dependence theorem for the full state response

`xi_alpha` versus `xi_m`.

I made this scope explicit rather than silently treating the two as identical.

This is the second major Round-5 opportunity: derive a resolvent / fractional-Gronwall constant

`||C(xi_alpha-xi_m)|| <= C_dyn ||k_alpha-k_m||_1 ||u||`

for the shared linearized ecological backbone.  If closed non-vacuously, this would materially strengthen both the theorem and the novelty claim.

---

## P1.2 — Build / packaging claims were stale

The delivered root `VALIDATION_REPORT.md` still reported 61 pages, while the actual Round-4 manuscript is longer.  A clean build also had five final-pass hyperref warnings even though the round notes claimed zero.

### Chief repair performed

- section headings with raw math removed from PDF bookmarks;
- Design A-E headings in Section 11 promoted to the correct hierarchy level;
- clean rebuild completed.

Final chief build:

- **72 pages**;
- **0 undefined citations**;
- **0 undefined references**;
- **0 final-pass LaTeX warnings**.

---

## Visual audit

All 16 manuscript figure PDFs are SHA-256 identical to the chief-audited Round-3 package.

**No visual regression.**

I would not spend another general visual round here.  The next new main-text visual should be the Round-5 Safe Memory-Discrimination Atlas, provided the mathematics behind the atlas passes its gate.

---

# Chief verdict by component

| Component | Verdict after chief repair |
|---|---|
| Structural separation T4-T7 | unchanged / accepted |
| Finite-horizon T8-T10 | unchanged / accepted in stated scope |
| Finite-m constructive L1 constants | **repaired with interval upper enclosures** |
| T20 generic bounded-observation testing theorem | **PROVED after repair** |
| T20 point-sampled benchmark interpretation | **NOT PROVED; explicitly separated** |
| T21 high-frequency negative theorem | **PROVED after repair** |
| A ~= 0.32 crossover | **DIAGNOSTIC ONLY** |
| hierarchy-uniform Strong-Allee B_eff | **OPEN** |
| full ecological-state lift of T20 | **OPEN** |
| Q1 figures | frozen / accepted |

## Round decision

**GO to Round 5, but Round 5 begins with a hard theorem gate, not with plotting.**
