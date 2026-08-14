# Theorem Ledger — Chief status after Round 6

Date: 2026-08-14

| Object | Chief status | Correct scope |
|---|---|---|
| T4–T7 structural separation | PROVED | stated compact-band / channel / retarded single-delay assumptions |
| T8–T10 finite-horizon kernel results | PROVED | stated linearized convolution/fixed-input regimes |
| T11–T13 optimal design | PROVED | stated linear-Gaussian regimes and compactness assumptions |
| T16–T17 safety results | PROVED | strict stated assumptions |
| T20 Gaussian composite testing bound | PROVED | requires an independently valid L2 input outer budget |
| T21 threshold-only non-coercivity | PROVED | no actuator/bandwidth cap |
| T22 hierarchy-uniform Strong-Allee reduction | PROVED | fixed positive protocol ray, kernel hierarchy K_m; displayed constants numerical where stated |
| Lemma R6.1 pole/branch decomposition | PROVED | scalar Mittag-Leffler mode, principal branch, alpha*pi/2 < |arg lambda| < alpha*pi |
| T23 ecological prey-response finite-state approximation | **PROVED / ACCEPTED** | linearized prey-input -> prey-output channel only; explicit stable strictly proper LTI response surrogate |
| R6 interval E_state values | **CERTIFIED / ACCEPTED** | outward-rounded compact-rate enclosures + analytic tail; all 8 focal cells cross-checked numerically |
| Prey-response Gaussian testing corollary | **PROVED / ACCEPTED** | bounded linear observation operator; valid input energy cap; headline values use pulse shape/peak cap B=0.120 |
| Researcher T24 mass-only state-response Allee witness | **DEMOTED / NOT HEADLINE** | mathematically valid only for overly broad mass-only response class; lacks independent residue/gain cap and backbone-consistency required by intended R6 hard gate |
| Full-vector ecological state approximation | **NOT PROVED** | T23 controls one scalar prey channel, not the full vector state or predator channel |
| Hierarchy-wide Strong-Allee safety for physically constrained full-state latent rivals | **OPEN** | explicitly future work |
| Nonlinear Volterra/state-response lift | OPEN | future work |

## Accepted focal certified enclosures

alpha=0.85, T=12:

- A=0.25: E_state = 0.53343 / 0.12536 / 0.02730 / 0.00692 for m=4/8/16/32.
- A=0.30: E_state = 0.47055 / 0.08982 / 0.02039 / 0.00662.

Independent transformed-grid Mittag-Leffler cross-checks put the actual floating-point L1 errors at approximately 18.7%–38.3% of these certified upper bounds.

## Headline testing interface retained

Rectangular pulse support Delta=1.44 and peak cap 0.10 imply

B <= 0.10 sqrt(1.44) = 0.120.

At sigma=0.10, Pinsker lower bounds:

- A=0.25: 0.340 / 0.462 / 0.492 / 0.498.
- A=0.30: 0.359 / 0.473 / 0.494 / 0.498.
