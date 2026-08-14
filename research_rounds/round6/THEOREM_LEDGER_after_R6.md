# Theorem Ledger — After Round 6

Date: 2026-08-14

| Object | Status | Scope |
|---|---|---|
| T4–T7 structural separation | PROVED | existing stated regimes |
| T8–T10 finite-horizon kernel results | PROVED | existing stated regimes |
| T11–T13 optimal design | PROVED | existing stated regimes |
| T16–T17 safety results | PROVED | stated strict assumptions |
| T20 Gaussian composite testing bound | PROVED | any input class with an independently valid L2 outer budget |
| T21 state threshold alone does not bound input energy | PROVED | no actuator/bandwidth cap |
| T22 single-mode extremal Strong-Allee reduction | PROVED | fixed positive protocol ray; kernel class K_m (chief-repaired scope) |
| Nested K_m finite hierarchy | REPAIRED (chief R5) | running-envelope windows |
| d_rob (kernel) numerical values / crossover | NUMERICALLY VALIDATED | not interval-certified (unchanged) |
| Pulse-ray kernel atlas | VALIDATED / THEOREM-GUIDED | stable focal cells; unstable masked |
| **Lemma R6.1 pole/branch-cut decomposition** | **PROVED (R6)** | alpha*pi/2 < \|arg lambda\| < alpha*pi; sector interval-verified per cell |
| **T23 certified full ecological-state approximation** | **PROVED (R6)** | true G_alpha(s)=C(s^alpha I−J)^{-1}B; integer-order rival class G_m; outward-rounded interval enclosures E_state_m; no QUADPACK |
| **Cor. state testing bound (T23')** | **PROVED (R6)** | same proof pattern as T20 at ecological output level; same hierarchy G_m |
| **T24 state-level pulse-ray Allee budget** | **PROVED (R6), interval-certified end to end** | declared positive pulse ray only; closed-form Young/witness sandwich, d_low/d_up ≥ 0.986; divisor is the certified LOWER bound |
| Gate-0B factorized-lift obstruction | UNCHANGED (negative) | now correctly scoped: it obstructs the FACTORIZED route only; T23 shows the model class itself is not obstructed |
| Full ecological-state testing theorem | **CLOSED by T23 + T23' + T24** | linearized state level (Option A scope); nonlinear Volterra extension remains future work |

## Key certified constants (alpha=0.85, T=12, pulse ray)

- E_state enclosures (A=0.25): 0.5335 / 0.1254 / 0.0274 / 0.0070 for m=4/8/16/32.
- E_state enclosures (A=0.30): 0.4706 / 0.0899 / 0.0204 / 0.0067.
- Kernel-level comparison (chief R4): 0.352 / 0.248 / 0.200 / 0.134 — the
  state-level enclosure drops below kernel level from m=8 on.
- M_state: 4.5661 (A=0.25), 6.5453 (A=0.30) — declared cap = ||g_alpha||_1
  enclosure + 1; constructive rival mass verified against it per cell (no
  rescale triggered).
- B_Allee^state: 0.104–0.106 (A=0.25), 0.0636–0.0644 (A=0.30); active below
  shape cap 0.120 and universal cap 0.346.
- Certified Pinsker state-level bounds at sigma=0.10:
  A=0.25: 0.359/0.467/0.493/0.498; A=0.30: 0.424/0.486/0.497/0.499
  (m=4/8/16/32).  Universal-cap variant non-vacuous from m=8 on
  (0.391/0.476/0.494 at A=0.25).

## Validation

- Independent float check (`check_round6.py`): 8/8 focal certificates hold
  with true L1 distances 3–5x below the enclosures; decomposition validated
  against the Mittag-Leffler series (1e-11) by an independent route.
- All eight ROUND6 hard gates pass (see ROUND6_RESULTS.md).
