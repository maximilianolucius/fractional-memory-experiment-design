# Round 6 — Results

Date: 2026-08-14.  Primary objective: **CLOSED** (full ecological-state
certified theorem, safety outcome A).  Stop rule not triggered.

## What was done

1. **Chief round-5 audit integrated first**: chief-repaired manuscript adopted
   (nested windows, mass-valid alpha=0.70 competitors, protocol-ray scope for
   T22, "certified" wording removed from grid maximizations, stability-masked
   fig18); `chief_round5/repair_atlas.py` re-run locally with exact numerical
   agreement (structural diff of the corrected atlas: 0 differences); build
   reproduced (exit 0, 75 pp, 0 undefined, 0 warnings).

2. **The mathematics (ROUND6_PROOF.md).**  The true fractional transfer
   G_alpha(s) = e1^T (s^alpha I - J(A))^{-1} e1 is decomposed per eigenvalue via
   Bromwich/Hankel deformation (Lemma R6.1): in the entire focal
   Matignon-stable regime the eigenvalue sector satisfies
   alpha*pi/2 < |arg lambda| < alpha*pi (interval-verified per cell), so the
   response splits EXACTLY into
   - a principal-sheet pole pair s0 = lambda^{1/alpha} (Re s0 < 0 iff
     Matignon) — realized exactly by a 2-dimensional real integer-order
     block; this is precisely the backbone content on which the Round-5
     factorized lift failed (Gate 0B), and
   - a smooth branch-cut density Phi(r), approximated by m-2 first-order
     modes with interval-certified L1(0,T) quadrature error.

   This yields T23 (certified state-level approximation, enclosures
   Ehat_m^state), Corollary state-testing (T20's proof pattern at ecological
   output level), and T24 (state-level pulse-ray Strong-Allee budget as a
   closed-form Young/witness sandwich — interval-certified end to end, unlike
   the kernel-level d_rob constants).

3. **Certified computation** (`compute_round6.py`, mpmath.iv outward
   rounding, no QUADPACK): focal cells on R11, full stable-A table on Orion
   (344-core box; 7 cells x 4 budgets).  Independent float validation
   (`check_round6.py`): 36/36 certificates hold (all 7 stable cells x 4 budgets, focal cells double-checked in both JSON sources), true L1 errors 3-5x
   below enclosures; decomposition cross-checked against the Mittag-Leffler
   series (agreement ~1e-11).

## Headline certified numbers (alpha=0.85, T=12, pulse ray)

E_state upper enclosures (vs chief kernel-level 0.352/0.248/0.200/0.134):

| A | m=4 | m=8 | m=16 | m=32 |
|---|---|---|---|---|
| 0.25 | 0.5335 | 0.1254 | 0.0274 | 0.0070 |
| 0.30 | 0.4706 | 0.0899 | 0.0204 | 0.0067 |

Certified Pinsker state-level testing bounds (sigma=0.10, B_eff active =
Allee state budget):

| A | m=4 | m=8 | m=16 | m=32 |
|---|---|---|---|---|
| 0.25 | 0.359 | 0.467 | 0.493 | 0.498 |
| 0.30 | 0.424 | 0.486 | 0.497 | 0.499 |

Stable-A table (Orion): A in {0.15, 0.20, 0.32, 0.34} hard@0.25 from m=8 on
(e.g. 0.436-0.492); at m=4, A=0.15 is moderate (0.216) and A=0.10 is
inconclusive (near-cut quasi-resonance: |arg lambda| = 2.6494 vs alpha*pi =
2.6704, within 0.021 rad of the branch cut, so the branch density has a
sharp integrable peak and 2 nodes cannot resolve it); A=0.10 is hard from
m=8 on (0.395, 0.473, ...).  Nothing inconclusive is labeled discriminable.

B_Allee^state: 0.104-0.106 (A=0.25), 0.0636-0.0644 (A=0.30) — active below
the shape cap 0.120; at A in {0.10, 0.15, 0.20} the shape cap is active.
Sandwich tightness d_low/d_up >= 0.986.

## Hard gates (all 8 PASS)

1. Rival integer-order, finite-dimensional (pole block + first-order modes).
2. Exact focal object G_alpha(s) = C(s^alpha I - J)^{-1} B (no factorization).
3. Genuine upper enclosures (mpmath.iv); QUADPACK only in the float
   cross-check, never as a certificate.
4. Pole/gain/mass constraints declared and verified (M_state cap; rescale
   path present, not triggered).
5. Same hierarchy G_m in approximation and testing.
6. Allee bound stated for exactly the declared positive pulse ray.
7. Stable-cell claims all behind interval-verified Matignon assertions
   (A=0.38, 0.42 excluded by the assertion itself).
8. Only P_e lower bounds reported; no discriminability labels.

## Safety interface outcome

**Outcome A achieved**: hierarchy-uniform state-level Allee budget for the
declared pulse ray (T24), combined with the state-level testing theorem over
the same class.  The universal actuator-cap variant (outcome B) is reported
alongside in the JSON and remains non-vacuous from m=8 on.

## Manuscript integration

- sec6: new subsection `subsec:state_theorem` (Lemma R6.1 + T23 +
  cor:state_testing + T24 + certified tables + fig19).
- sec1, abstract: factorized-lift obstruction retained, closure by the
  backbone-consistent realization stated.
- sec12: three-levels discussion updated; limitations keep the nonlinear
  Volterra extension open (T23 is linearized-state level).
- sec14: index rows for Lemma R6.1, T23, cor:state_testing, T24.
- New figure fig19_state_theorem (3 panels, certified quantities only);
  the 16 Q1 figures and fig18 untouched.

## Artifacts

- research_rounds/round6/{compute_round6.py, check_round6.py,
  plot_round6_state.py, round6_results.json, round6_results_<A>.json,
  ROUND6_PROOF.md, ROUND6_RESULTS.md, THEOREM_LEDGER_after_R6.md,
  NOVELTY_LEDGER_after_R6.md, MANUSCRIPT_IMPACT_after_R6.md}
- paper/figures/fig19_state_theorem.pdf
- Orion working dir: ~/fmed_work/round6 (same scripts, md5-matched).

## What was NOT done (per governance)

- No benchmark rerun; no touching the 16 frozen Q1 figures or fig18.
- No claim for arbitrary safe waveforms (T24 is ray-restricted).
- No restoration of any claim removed by the round-5 chief audit.
- The nonlinear (Volterra) state-level extension remains declared future work.
