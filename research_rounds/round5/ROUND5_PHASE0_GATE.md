# Round 5 — Phase 0 Gate Verdict

Date: 2026-08-14
Status: **ALL THREE GATES DECIDED — atlas authorized (with Gate-0B scope
labeling).**

Governance compliance: no plotting before gates; no factorial benchmark
rerun; chief R4 repairs untouched.

---

## Gate 0A — hierarchy-uniform Strong-Allee interface: **CLOSED (preferred route)**

**Theorem (Gate 0A).** Ecological realization of `k = sum_j c_j e^{-lam_j t}
in K_m` (memory drives the prey channel through the ODE backbone J(A)):

    q_j' = -lam_j q_j + u,      xi' = J xi + e_1 sum_j c_j q_j,
    x_k(t) = (h_J * (k*u))(t),  h_J(t) = e_1^T e^{Jt} e_1.

For a fixed shape u0 and the downward gain
`d(k) = max_t[-(h_J*(k*u0))(t)]_+ / ||u0||_2`,

    d_rob(K_m, u0) := sup_{k in K_m} d(k)
                    = M_T * max_{lam in [ell_m, L_m]} F(lam)/w(lam),
    F(lam) = max_t[-(h_J*(e^{-lam .}*u0))(t)]_+ / ||u0||_2,
    w(lam) = (1 - e^{-lam T})/lam.

**Proof sketch.** Linearity in the positive mode measure dmu = sum c_j
delta_{lam_j}:
`d(k) <= sum_j c_j F(lam_j) = sum_j [c_j w(lam_j)] [F(lam_j)/w(lam_j)]
      <= M_T max(F/w)` since `sum c_j w(lam_j) = ||k||_1 <= M_T`.
**Attainment (lower bound):** the single-mode kernel
`k* = (M_T/w(lam*)) e^{-lam* .}` belongs to K_m (one mode, mass exactly M_T,
rate in the window) and achieves the value, so the bound is EXACT, not merely
conservative.

Consequence:
    **B_Allee(A,m) = rho_eta / d_rob(K_m,u0)**
is a theorem-valid, m-dependent, hierarchy-uniform outer budget for the
common-safe ray — exactly the quantity the chief required to enter T20 for
the same adversarial class.

**Numerics (sandwich; lower bound drives B_Allee — direction validated):**
pulse protocol, benchmark windows, d_rob in [low, up]:

| A | d_rob low/up m=4 | m=8 | m=16 | m=32 |
|---|---|---|---|---|
| 0.25 | 6.70 / 8.38 | 7.56 / 9.47 | 7.14 / 8.93 | 7.87 / 9.85 |
| 0.30 | 11.96 / 14.96 | 13.02 / 16.29 | 12.51 / 15.65 | 13.39 / 16.76 |
| 0.32 | 15.44 / 19.30 | 16.62 / 20.79 | 16.05 / 20.08 | 17.03 / 21.31 |
| 0.34 | 20.26 / 25.33 | 21.72 / 27.17 | 21.07 / 26.35 | 22.20 / 27.77 |

**Inequality direction (checked against the Round-2 class of error).**
B_Allee = rho_eta/d_rob is a necessary OUTER bound on the safe ray's energy,
so it must divide by a LOWER bound on d_rob. B_Allee uses d_rob_low (honest
grid max, conservative when underestimated). The upper sandwich (grid max +
time-grid Lipschitz margin + 25% lambda margin, M_T rounded up) is reported
for the enclosure width only and is never used as the divisor.

Locked-rival validation (diagnostic): latent3 actual downward gain 1.18 at
A=0.25 vs d_rob_low 6.70 — the hierarchy-uniform bound is ~5–6x conservative
over the benchmark rivals, as expected and honestly reported.

**Certified crossover:** the switch shape-cap -> Allee binding occurs at
A in (0.15, 0.20) for every m (alpha=0.85). This is MORE conservative than
the benchmark diagnostic A≈0.32. The 0.32 diagnostic remains labeled as the
locked-rival-set phenomenon; the theorem crossover is the (0.15, 0.20)
interval.

**Gate A: PASSED.**

## Gate 0B — ecological-state lift of T20: **CLOSED as a scope theorem (negative route)**

The true focal prey response is `h_J^alpha = L^{-1}[e_1^T (s^alpha I - J)^{-1} B]`
(backbone in the fractional sense), while the shared-kernel picture gives
`h_J * k_alpha = L^{-1}[e_1^T (sI-J)^{-1} B * s^{-alpha}]`. These differ by the
**irreducible backbone mismatch**

    D0(A) = ||h_J^alpha - h_J*k_alpha||_1
          = 9.11 (A=0.25), 16.96 (A=0.30), 24.15 (A=0.34),

independent of m. The constructive latent errors
`||h_J^alpha - h_J*k_m||_1` converge to ~16.6–17.2 (A=0.30) — i.e. to D0, not
to 0 — confirming D0 is the floor. Hence a factorized ecological lift
`C_dyn ||k_alpha-k_m||_1 ||u||` is **false** for the true fractional backbone;
no small-gain denominator was attempted (it would be vacuous anyway).

**Gate B: closed negative.** The atlas is labeled **kernel-level theoretical
obstruction + full-state empirical benchmark**, not a single certified
ecological-state theorem. The valid ecological bound is
`||x_alpha - x_k||_inf <= [D0(A) + ||h_J||_1 ||k_alpha-k||_1] ||u||_inf`,
useful as scope but not headline.

## Gate 0C — asymptotic hierarchy: **CLOSED with a mass caveat**

Explicit expanding nested windows
    ell_m = 0.025/sqrt(m),  L_m = 3 + 0.1 ln(m)
are nested, contain all 11 tuned R3/R4 competitor cells, and along them the
T9b analytic bound tends to 0 (125.4 at m=1 down to 3.22 at m=65536), proving
`E_m -> 0` for THIS hierarchy (T9b left-node mixtures).

**Caveat (reported honestly):** the T9b asymptotic mixtures violate the
frozen safe-class mass bound M_T = 9.74 for small m (mixture mass ~102.5 at
m=1, falling below M_T only from m ~ 256). Therefore the asymptotic E_m->0
claim lives in an **m-dependent-mass approximation class**, not in the frozen
safe class K_m. The finite-m theorem (T20 with interval-enclosed Ehat_m^IA)
is unaffected and remains the certified statement; no asymptotic claim is
made for K_m itself.

**Gate C: PASSED (with the above scope separation).**

---

## Phase 0 verdict

**GO for atlas construction.** Atlas uses only theorem-valid quantities:
interval-enclosed Ehat_m^IA (multi-alpha), the exact Gate-0A d_rob, shape cap,
universal cap. Classification: `hard@0.25` / `moderate@0.10` /
`inconclusive`; nothing is ever labeled "discriminable".
