# Round 4 Results — Safe-Memory Testing Bound

Date: 2026-08-14
Status: **Phase 0 PASSED (see ROUND4_PHASE0_CLOSURE.md); Phase 1 PROVED;
Phase 2 NON-VACUITY GATE PASSED; Phase 3 manuscript integration executed
(this round, end).**

Locked constants (unchanged from Phase 0): `alpha=0.85`, `T=12`, `eta=0.02`,
`u_max=0.10`, `x*=2/3`, certified hierarchy of Phase 0 (`K_m` with nested
windows, mass bound `M_T=9.7416`).

---

## Phase 1 — The testing theorem

### Setup

Continuous prey-channel observation on `[0,T]` with additive Gaussian noise of
spectral density `sigma^2`; equivalently, sampled observations with per-sample
variance `sigma^2` at a fixed schedule (the benchmark convention). Focal law:
Caputo prey response `y_C = S(k_alpha * u) + eps`. Adversary: any latent
competitor `k_m in K_m` (the Phase-0 frozen hierarchy) with response
`y_L = S(k_m * u) + eps`, equal covariance. Observation operator `S` bounded;
for the sampled prey channel of the benchmark, `||R^{-1/2} S||^2 = 1/sigma^2`.

### Theorem R4 — minimum error of safe memory discrimination

Let `Ebar_m^cert` be the certified L1 kernel-error certificate of Phase 0
(item 0.2) and let `B_eff` be any valid outer energy bound on the safe input
class (Phase 0 item 0.3):

    B_eff = sqrt(T) u_max                                 (universal),
    B_eff = u_max ||u_0||_2 / ||u_0||_inf                 (fixed shape u_0),
    B_eff = min(B_eff, rho_eta / d_rob)                   (transient protocol,
                                               where the one-sided bound binds).

Define

    U_m := Ebar_m^cert^2 * B_eff^2 / (2 sigma^2).

Then the robust minimax error of discriminating the focal Caputo memory from
the latent class `K_m` over all safe inputs satisfies

    P_e^*(m) >= Psi(U_m),

with each of the following valid (each line a legitimate `Psi`):

    (a) Pinsker:            Psi(x) = (1 - sqrt(x/2)) / 2;
    (b) Bretagnolle-Huber:  Psi(x) = (1 - sqrt(1 - e^{-x})) / 2;
    (c) exact, fixed constructive competitor k_m in K_m under equal-covariance
        Gaussian noise:  P_e(u; C, k_m) = Phi(-sqrt(KL/2)), and the minimax
        error is >= Phi(-sqrt(U_m/2)) when KL is bounded by U_m.

**Proof.**

1. (R1 ceiling with certified constant.) For any safe input `u` with
   `||u||_2 <= B_eff`, Young's inequality and the certified kernel bound give
   `||(k_alpha - k_m) * u||_2 <= Ebar_m^cert ||u||_2`. With equal covariance,
   `KL(P_C^u || P_{k_m}^u) = (1/(2 sigma^2)) ||S((k_alpha - k_m)*u)||^2
   <= U_m`. Taking the infimum over `k_m in K_m` preserves the bound.
2. (Adversarial selection.) By the definition of the ceiling, for every
   `u` there exists `k_m(u) in K_m` with `KL(P_C^u || P_{k_m(u)}^u) <= U_m`.
3. (Testing inequality.) For any test between `C_alpha` and `k_m(u)` driven by
   input `u`, the minimax two-point error satisfies
   `P_e >= (1 - TV)/2 >= (1 - sqrt(KL/2))/2 >= (1 - sqrt(U_m/2))/2`
   (Pinsker; TV = (1-2P_e) at the optimal test). The Bretagnolle-Huber form
   follows from `TV <= sqrt(1 - e^{-KL})`. For equal-covariance Gaussians the
   optimal error is exactly `Phi(-sqrt(KL/2)) >= Phi(-sqrt(U_m/2))` since
   `Phi(-sqrt(x/2))` is decreasing.
4. The robust problem (discriminate against every `k_m in K_m`) is harder than
   each simple pair, so the bound applies. ∎

**Direction check (numerical).** For exact equal-covariance Gaussian pairs at
`KL in {0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 3, 5}`: both Pinsker and
Bretagnolle-Huber lower bounds lie below the exact `Phi(-sqrt(KL/2))` at every
point (verified in `compute_round4.py` run log). The theorem constant `U_m`
is a KL UPPER bound feeding a DECREASING error function — the direction is
the correct impossibility direction.

**Scope (chief P0.4 resolution).** The benchmark five-simulator worst-case
constants are diagnostics only; the theorem's adversary is `K_m` itself, and
every common-safe input is safe for the focal model, so the focal outer bound
applies to the common-safe class.

### Separated statements (per prompt)

1. **Universal peak-capped statement:** with `B_eff = sqrt(T) u_max = 0.3464`,
   Theorem R4 applies to ALL safe inputs of any design class, since the peak
   cap alone bounds L2 energy. No Allee argument is needed.
2. **Protocol-relative Strong-Allee refinement:** for the fixed-shape
   transient protocols (pulse, multiscale), `B_eff` is the minimum of the
   shape-specific cap and `rho_eta/d_rob`. At the benchmark cells `A <= 0.30`
   the shape cap binds; at `A >= 0.32` the Allee-coercive bound binds
   (crossover at `A ≈ 0.32`, chief-predicted and reproduced). Only in the
   binding region does the Allee proximity shrink the testing ceiling —
   stated exactly this way, protocol-relative, not absolute.

---

## Phase 2 — Non-vacuity gate

Certified constants (`compute_round4.py`, `round4_results.json`):

| m | Ebar_m^cert | U_m (universal cap, sigma=0.10) | Psi_Pinsker | Phi(-sqrt(U/2)) exact |
|---|---|---|---|---|
| 4 | 0.3512 | 0.7399 | 0.196 | 0.272 |
| 8 | 0.2632 | 0.4156 | 0.272 | 0.324 |
| 16 | 0.1986 | 0.2367 | 0.328 | 0.365 |
| 32 | 0.1325 | 0.1053 | 0.385 | 0.409 |

(U_m = (Ebar·B)^2/(2σ²); Psi_Pinsker=(1−√(U/2))/2; exact=Φ(−√(U/2)).)

**Gate decision: PASSED.** In the defensible regime `sigma = 0.05–0.10`
(absolute prey units; the benchmark's SNR-10dB noise is ~0.013–0.014, i.e.
the impossibility bites at 4–8x benchmark noise, or at larger m), the lower
bound is `P_e^* >= 0.25–0.47` — quantitatively informative, monotone in m,
and approaching the chance level 0.5 as `Ebar_m^cert -> 0`. The certified
constants are used throughout; no sampled error is labeled certified.

**Empirical cross-check (labeled empirical, not certified):** at benchmark
noise (SNR 10dB) against the fixed locked latent3 competitor, exact pairwise
errors are ~1e-96 (pulse) and ~1e-98 (multiscale) — discrimination against a
FIXED competitor at benchmark noise is easy; the impossibility concerns the
ADVERSARIAL class as m grows or noise rises. Both facts are true and the
paper will say so.

---

## Phase 3 — Manuscript integration (executed this round)

All three integration conditions of MANUSCRIPT_IMPACT_after_R3_CHIEF.md are
met: (1) coherent hierarchy (Phase 0 item 0.1); (2) valid, non-vacuous
testing bound (Phase 1 + Phase 2); (3) every constant labeled analytic /
certified / diagnostic / empirical. Changes to `main.tex` and sections:

- Abstract: three-way novelty statement + testing-bound headline;
- Sec 1: contribution paragraph updated;
- Sec 6: new subsection — frozen `K_m`, `Ebar_m^cert`, Theorem R4 with
  certified constant table;
- Sec 8: new remark — repaired safety interface: inner certificate (R2a),
  high-frequency negative theorem (Riemann-Lebesgue proof), one-sided
  transient outer bound with the A≈0.32 crossover (diagnostics labeled);
- Sec 12: protocol-relative refinement positioned honestly;
- Sec 14: theorem index updated (R4 + negative scope theorem);
- bibliography: T01 (Tsybakov, testing inequalities) added.

Figure suite: unchanged (chief instruction). No atlas (Round 5).

## Reproducibility

```
cd research_rounds/round4
python3 compute_round4.py     # certificates + one-sided bounds + testing curves
```
Outputs `round4_results.json`. Reuses `chief_round3_checks.py` (round3) and
released benchmark code; no factorial benchmark rerun.
