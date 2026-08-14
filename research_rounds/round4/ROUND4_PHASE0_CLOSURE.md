# Round 4 — Phase 0 Closure of the Round-3 Chief Audit

Date: 2026-08-14
Status: **ALL FIVE ITEMS CLOSED** — Phase 1 (testing theorem) may proceed.

This document closes CHIEF_ROUND3_AUDIT.md items P0.1–P0.7 per
ROUND4_RESEARCHER_PROMPT.md Phase 0. No manuscript edits in this phase.

---

## 0.1 ONE coherent latent hierarchy (closes P0.2, P0.3, P0.4)

**Decision: Option A (expanding nested rate windows), with a declared mass
constraint and a kernel-level ecological realization.**

The hierarchy `K_m` is now the single class that defines (i) the approximation
adversary in `E_m`, (ii) the latent ecological realization, and (iii) the
common-safety family:

    K_m = { k_m(t) = sum_{j=1}^m c_j e^{-lambda_j t} :
            c_j >= 0,
            lambda_j in [ell_m, L_m],
            ||k_m||_{L^1(0,T)} <= M_T }

with

- **mode-rate domain, nested in m (Option A):** running windows
  `ell_m = min_{j<=m} ell_j^*`, `L_m = max_{j<=m} L_j^*`, where `(ell_j^*,
  L_j^*)` are the tuned truncation parameters of the T9b left-node
  construction. Verified: all 11 stored tuned competitors (m = 1..32) lie in
  their windows and the windows are nested
  (`[0.0574, 0.708] ⊃ ... ⊃ [0.0074, 2.991]`); the T9b approximants belong to
  the hierarchy by construction, and the hierarchy is nested, so `E_m -> 0`
  remains a legitimate asymptotic claim for the class.
- **positivity:** `c_j >= 0` (completely monotone kernels, matching k_alpha);
- **coupling/mass normalization (closes P0.3):** declared mass bound
  `||k_m||_1 <= M_T := ||k_alpha||_1 + 1 = 9.7416` at T=12. Verified for all
  11 stored competitors: max mass 9.24 (m=1), all <= M_T. This bounds the
  DC gain / ecological coupling of every rival uniformly and prevents the
  unbounded-weight trivialization of the chief audit.
- **ecological realization:** every rival acts through the shared backbone:
  Jacobian skeleton J(A), prey input channel B = e_1, and a prey-channel
  memory kernel — the latent realization adds m auxiliary modes
  `q̇ = -diag(lambda) q + 1 u` whose weighted contribution to the prey
  equation has coupling `g c_j` (benchmark convention: coordinates 0..1 are
  the ecological prey/predator states; coordinates 2+ are memory modes).
- **input channel:** prey-only additive actuation, `||u||_inf <= u_max`;
- **observation channel:** prey channel `C = e_1^T` (the safety-relevant
  coordinate; the theorem's observation operator S is the benchmark sampling
  map);
- **nestedness:** `K_m ⊆ K_{m+1}` by zero-weight padding + window nesting.

**Resolution of P0.4 (common safety over the same class).** The R4 theorem
uses the chief's second option: every common-safe input is in particular safe
for the focal Caputo model, hence the focal-model outer bound is a valid
necessary bound for the common-safe class; the benchmark five-simulator
worst-case constants are reported strictly as diagnostics of the locked
realizations, never as certificates for K_m. The five simulators are no longer
called "the full rival family" of any theorem.

## 0.2 E_m terminology and certified constants (closes P0.1)

The deterministic `(ell, L)` search produces constructive candidate upper
errors. Notation fixed throughout:

    E_m <= Ebar_m <= Ebar_m^cert

where `Ebar_m` is the candidate error and `Ebar_m^cert` the **rigorous
numerical certificate** computed in `compute_round4.py`:

- head `(0, delta)`, delta = 1e-4: exact integration of BOTH kernels (no
  triangle inequality): `delta^alpha/(alpha Gamma(alpha)) +
  c_alpha h sum_j lambda_j^{-alpha}(1-e^{-lambda_j delta})/lambda_j`;
- body `[delta, T]`: adaptive quadrature with the returned error estimate
  added;
- result: a true upper bound on `||k_alpha - k_m||_{L^1(0,T)}`.

| m | candidate Ebar_m | certified Ebar_m^cert | slack |
|---|---|---|---|
| 1 | 0.9257 | 0.9234 | cert tighter than grid candidate |
| 2 | 0.5696 | 0.5673 | ditto |
| 3 | 0.5415 | 0.5392 | ditto |
| 4 | 0.3534 | 0.3512 | ditto |
| 5 | 0.3758 | 0.3735 | ditto |
| 6 | 0.2489 | 0.2466 | ditto |
| 8 | 0.2654 | 0.2632 | ditto |
| 12 | 0.2366 | 0.2343 | ditto |
| 16 | 0.2009 | 0.1986 | ditto |
| 24 | 0.2143 | 0.2120 | ditto |
| 32 | 0.1347 | 0.1325 | ditto |

(The certificate integrates the exact singular head analytically, so it comes
out slightly below the gridded candidate while remaining a rigorous upper
bound: quadrature error estimates <= 4.7e-10 are added, and the head bound is
exact.) The T9b analytic bound at tuned parameters (13–20) remains valid but
is never used as the theorem constant; it is superseded by `Ebar_m^cert`
everywhere a numerical constant is needed.

## 0.3 One-sided Allee safety + shape-specific cap (closes P0.5, P0.6)

**One-sided downward gain.** For a positive fixed-shape ray `u = c u_0`,
`c >= 0`, safety is the one-sided floor `x*(A) + c (H_{x,M} u_0)(t) >= A + eta`,
giving the necessary bound

    ||u||_2 <= rho_eta / d_rob,
    d_M(u_0) = max_t [-H_{x,M} u_0(t)]_+ / ||u_0||_2,
    d_rob = sup over the considered family.

Recomputed exactly as in `chief_round3_checks.py` (reproduced locally; the
chief's JSON and my run agree to all displayed digits on shared cells).
Benchmark-rival diagnostics (focal cell alpha=0.85, T=12, eta=0.02):

| A | family | rho_eta | d_rob (latent3 binds) | rho_eta/d_rob | shape cap | binding |
|---|---|---|---|---|---|---|
| 0.25 | pulse | 0.3967 | 1.1816 | 0.3357 | 0.1200 | shape cap |
| 0.25 | multiscale | 0.3967 | 0.8953 | 0.4431 | 0.1549 | shape cap |
| 0.30 | pulse | 0.3467 | 2.1128 | 0.1641 | 0.1200 | shape cap |
| 0.30 | multiscale | 0.3467 | 1.5489 | 0.2238 | 0.1549 | shape cap |
| 0.32 | pulse | 0.3267 | 2.7305 | 0.1196 | 0.1200 | **Allee (0.1196)** |
| 0.32 | multiscale | 0.3267 | 2.1792 | 0.1499 | 0.1549 | **Allee** |
| 0.34 | pulse | 0.3067 | 3.6106 | 0.0849 | 0.1200 | Allee |
| 0.34 | multiscale | 0.3067 | 3.0831 | 0.0995 | 0.1549 | Allee |

**Shape-specific peak-cap energy bound.** `||u||_2 <= u_max ||u_0||_2 /
||u_0||_inf`: pulse 0.1200, multiscale 0.1549 (not the loose 0.3464).

**Crossover confirmed at A ≈ 0.32**, exactly as the chief predicted: below it,
the shape-specific actuator cap is the binding outer bound; at and above it,
the Allee-coercive one-sided bound is tighter. The R3 claim that the Allee
bound binds already at A=0.25 is withdrawn (it used both the wrong one-sided
constant and the wrong cap).

## 0.4 High-frequency theorem proof repaired (closes P0.7/P1.1)

R3b-neg is now proved via the uniform Riemann–Lebesgue lemma: with
`h_x in L^1(0,T)`,

    sup_{t<=T} |int_0^t h_x(r) e^{-i omega r} dr| -> 0   (omega -> inf),

so for unit-L2-normalized `sin(omega t)` the prey output sup-norm tends to 0;
scaling each input by `rho/(2 delta_omega)` keeps it symmetrically safe while
its L2 norm diverges. No uniform `O(omega^{-alpha})` rate is claimed in the
theorem; the observed `eps^alpha` decay remains a numerical diagnostic only.

## 0.5 Dictionary null claim removed (closes P0.7/P0.5)

Restricted singular values are now computed after orthonormalizing each
dictionary span (chief method, reproduced locally):

| family | numerical rank | corrected s_min |
|---|---|---|
| sinusoid | 21 | 0.0532 |
| multisine | 13 | 0.1441 |
| chirp | 11 | 0.0997 |
| prbs | 15 | 0.2840 |

The R3 statement that the dictionaries contain machine-zero physical null
directions is **withdrawn**; the near-zero values were coefficient
non-identifiability from redundant columns. These L2→L2 constants still do
not settle one-sided Allee safety (they are not used in the R4 theorem).

---

## Phase-0 gate

All of 0.1–0.5 resolved. **GATE PASSED — proceeding to Phase 1.**

Reproducible: `compute_round4.py` (certificates, one-sided bounds, dictionary
constants) reuses `chief_round3_checks.py` functions; `round4_results.json`
stores all constants. No factorial benchmark rerun.
