# Round 3 Results — Latent Complexity Law + Safety-Interface Repair

Date: 2026-08-14
Status: **GO for R4** (gate conditions 1 and 2 both satisfied; see §6)

Round 3 executes `ROUND3_RESEARCHER_PROMPT.md`. Nothing below is integrated into
`main.tex` (governance: research rounds stay outside the manuscript until the
end-of-R3 gate; this document records the gate outcome).

Reproducible computation: `compute_round3.py` (Track A + Track B + robust
common safety), `plot_round3.py` (diagnostic figure), outputs
`round3_results.json`, `round3_diagnostic.pdf`. Reuses released
`benchmark/core.py`, `benchmark/designs.py`, `benchmark/bench.py` and the
Round-2 validated Mittag-Leffler evaluator (`compute_B_safe.ml2`,
alpha->1 gate rel err ~1e-10). No factorial benchmark re-run.

Locked constants: `T=12` (medium horizon), `u_max=0.10`, `eta=0.02`
(strict Allee reserve, scope guard), focal `alpha=0.85`, primary `A=0.25`,
`x*=2/3`, hence `rho_eta(0.25)=0.3933`.

---

## Track A — Frozen latent class and quantitative E_m(alpha,T)

### A.1 Frozen class K_m (scope guard satisfied)

We freeze the latent kernel class as

    K_m = { k_m(t) = sum_{j=1}^m c_j e^{-lambda_j t} :
            c_j >= 0, lambda_j in [ell_min, L_max] },

with `ell_min = 1e-3`, `L_max = 10` (window covers every tuned optimum below
with margin). Properties, as required by the prompt:

- **exponential modes**: yes, by construction;
- **positivity/sign constraints**: nonnegative weights `c_j >= 0` (fractional
  kernel is completely monotone; the constructive T9b member has strictly
  positive weights);
- **admissible rate interval**: `[1e-3, 10]`, frozen;
- **normalization/coupling bounds**: weights free in `[0, inf)`; the T9b
  construction (eq. (3) of the manuscript) supplies an explicit member with
  `c_j = c_alpha h lambda_j^{-alpha}`;
- **nestedness**: `K_m subset K_{m+1}` trivially (pad with zero weights);
- **common observed prey/predator output map**: see Track B.4 — every rival
  simulator (ODE, Caputo, DDE, latent1, latent3) exposes ecological states as
  its first two coordinates (`bench.lin_response` convention, including the
  latent models where `Abar[:2,:2]=J`, `Bbar[0]=1`).

The benchmark's arbitrary-realization latent models (`core.G_latent`) are NOT
members of `K_m`; they are used only for the robust common-safety worst case
of Track B.4. This separation is the freezing the chief audit demanded (item B:
"the current arbitrary latent realization does not by itself specify which
latent coordinates constitute ecological prey/predator states").

### A.2 Quantitative E_m law

`E_m(alpha,T) = inf_{k_m in K_m} ||k_alpha - k_m||_{L^1(0,T)}` evaluated by
deterministic tuning of the T9b left-node family over `(ell,L)` (28x30 grid,
same scheme as the chief-corrected Figure 14). Focal cell `alpha=0.85, T=12`:

| m | best displayed E_m | T9b bound at tuned (ell,L) |
|---|---|---|
| 1 | 0.9257 | 20.55 |
| 2 | 0.5696 | 17.43 |
| 3 | 0.5415 | 17.42 |
| 4 | 0.3534 | 15.89 |
| 5 | 0.3758 | 16.30 |
| 6 | 0.2489 | 14.62 |
| 8 | 0.2654 | 15.57 |
| 12 | 0.2366 | 13.21 |
| 16 | 0.2009 | 12.99 |
| 24 | 0.2143 | 12.87 |
| 32 | 0.1347 | 13.71 |

Envelope `E_m^env` (monotone in m, as the class is nested):
E_1=0.93, E_2=0.57, E_3=0.54, E_4=0.35, E_5=0.35, E_6=0.25, E_8=0.25,
E_12=0.24, E_16=0.20, E_24=0.20, E_32=0.13.

**Rate diagnostics (finite window, not a theorem).** Geometric fit
`E_m ~ C rho^m`: `rho ~ 0.96` — i.e. the left-node/Riemann family is barely
geometric; `exp(-c sqrt(m))` fit: `c ~ 0.30`. The subgeometric behavior is
expected: left-node Riemann sums must resolve the `t^{alpha-1}` singularity by
pushing `ell -> 0`, which is exactly the bottleneck of Theorem T9b's
`T ell^{1-alpha}/(1-alpha)` term.

**Constructive constants usable in R4 (certified, not empirical).** For any
prescribed tolerance the manuscript's own parameter choice (sec 6.4) gives an
explicit `m(eps)`; conversely for a fixed `m` the T9b bound at tuned `(ell,L)`
is a valid (conservative, factor ~60-100) certified upper bound on `E_m`.
R4 must use the T9b bound, not the envelope, whenever a certified constant is
required; the envelope is reported as the achievable scale.

**Citation / hypothesis audit (exact).** The constructive L1 bound used here is
the manuscript's Theorem T9b — proved in full in `paper/sections/sec6.tex`
(three-region split: low-rate tail `T ell^{1-alpha}/(1-alpha)`, high-rate tail
`L^{-alpha}/alpha`, middle Riemann gap `T h ell^{-alpha}`); no external
theorem is imported for it. External rates for optimized exponential-sum
approximation of completely monotone kernels (NOT claimed as our novelty, per
NOVELTY_LEDGER R1): Beylkin & Monzon, ACHA 19 (2005) 17-48 and ACHA 28 (2010)
131-149 (already in `bibliography.bib` as K03/K04), and Braess & Hackbusch,
IMA J. Numer. Anal. 25 (2005) 685-697 (best approximation of `1/x` by
exponential sums; the canonical `exp(-c sqrt m)` scale for this problem class;
NOT currently in `bibliography.bib` — add as K07 if/when these results enter
the manuscript). Our left-node family achieves the subgeometric scale; a
Gauss-Laguerre or sinc-based quadrature would improve constants but is out of
scope — R4 needs only a valid bound, which T9b supplies.

---

## Track B — Repair of the Strong-Allee safety outer bound

### B.1 Negative theorem: state safety does not bound input energy (unrestricted class)

**Theorem R3b-neg.** Let `H_x u = e_1^T (H_alpha * u)` be the prey-channel map
of the focal linearized Caputo system and let the local safe class be
`U_safe = {u in L^2(0,T) : sup_{t<=T} |H_x u(t)| <= rho_eta}`. Then
`sup_{u in U_safe} ||u||_2 = +infinity`.

**Proof.** (i) `H_x` is linear and `U_safe` is star-shaped (balanced): if
`u in U_safe` then `c u in U_safe` for `|c| <= 1`. (ii) For `eps > 0` set
`u_eps(t) = sqrt(2/T) sin(t/eps)`, so `||u_eps||_2 = 1 + O(eps/T)`. Since
`h_x in L^1(0,T)` is smooth on `(0,T]` and the system is strictly proper with
`|G_alpha(i omega)| = O(omega^{-alpha})`, integration by parts gives
`||H_x u_eps||_inf = O(eps^alpha) -> 0`. (iii) Hence for `eps` small enough,
`sup|H_x u_eps| <= rho_eta`, i.e. `u_eps in U_safe` with unit energy; by
star-shapedness, `(rho_eta / ||H_x u_eps||_inf) u_eps in U_safe` and its L2
norm diverges as `eps -> 0`. ∎

**Numerical verification** (`compute_round3.py`, unit-energy probes):

| eps | sup_t \|x_eps(t)\| |
|---|---|
| 1.0 | 6.43e-01 |
| 0.1 | 9.79e-02 |
| 0.01 | 1.39e-02 |
| 0.002 | 3.12e-03 |

Decay is consistent with `eps^alpha` (0.003/0.014 ~= (0.2)^0.85). This is the
high-frequency/null-direction obstruction named in the chief audit: an
arbitrarily energetic safe experiment exists in the unrestricted class, so
**no Allee-dependent outer energy bound can hold without restrictions on the
input class**. The explicit actuator cap `||u||_inf <= u_max` remains the
universal outer interface, as the chief predicted.

### B.2 Frozen implementable design class V (compatible with the paper)

We freeze `V` as the benchmark's six released design families
(`benchmark/designs.py`), split by structure:

- **fixed-shape families** `pulse`, `multiscale`: one-dimensional scale
  families `{c u_0 : c in R}`;
- **parameterized families** `sinusoid` (w in [0.05,3]), `multisine`
  (3-frequency base, +-15% detuning), `chirp` (sweep rate), `prbs` (seed):
  finite dictionaries of 20-24 generators each.

### B.3 Coercivity constants and the outer bound

For a fixed-shape family the prey-safety operator restricted to the family is
`c -> c H_x u_0`, and the sharp one-sided outer bound of the prompt holds:

    kappa_V^inf := ||H_x u_0||_{L^inf(0,T)} / ||u_0||_2  > 0
    ==>  every safe u = c u_0 satisfies  ||u||_2 <= rho_eta / kappa_V^inf.

Focal-cell values (`A=0.25`, Caputo, direct Mittag-Leffler convolution,
500-point causal Toeplitz):

| family | kappa_V^inf | rho_eta/kappa | cap sqrt(T)u_max | binding at A=0.25 |
|---|---|---|---|---|
| pulse | 0.9407 | 0.4217 | 0.3464 | cap |
| multiscale | 0.5814 | 0.6823 | 0.3464 | cap |

At `A=0.30` (closer to threshold): pulse `kappa=1.119`, outer `0.3097 < 0.3464`
— the Allee-coercive bound becomes the binding outer bound exactly near the
extinction threshold, as intended.

For the parameterized families, the L2-metric coercivity
`kappa_V = inf_{u in span(M), ||u||_2=1} ||H_x u||_2` (smallest singular value
of the discretized convolution restricted to the generator span) is
**numerically zero**:

| family | kappa_V | sigma_max |
|---|---|---|
| sinusoid | 2.2e-15 | 18.5 |
| multisine | 2.6e-15 | 35.9 |
| chirp | 2.4e-15 | 49.4 |
| prbs | 9.9e-16 | 18.2 |

Interpretation: each parameterized dictionary already contains unit-energy
combinations that the fractional prey channel attenuates to machine precision —
concrete instances of the B.1 null direction inside the frozen dictionaries.
Therefore no coercive outer bound exists for these families, and the actuator
cap is their only valid outer bound. (Scope guard honored: this is a property
of the locked dictionaries at `alpha=0.85`, not a monotonicity or universality
claim.)

### B.4 Robust common safety across the rival family

The chief audit (item B) required the ecological safety output to be frozen
for every rival before any common-safe claim. Frozen convention (already the
benchmark's): in all released simulators the first two state coordinates are
the ecological (prey, predator) states — `bench.lin_response` for ODE, Caputo,
DDE returns 2-states; for `latent1/latent3` the state is `(z, q)` with
`Abar[:2,:2]=J`, `Bbar[0]=1`, so coordinates 0-1 are ecological and 2+ are
memory modes. Safety output: `e_1^T z` (prey floor).

Worst-case prey-channel coercivity across the full rival family, focal cell
(`A=0.25`, unit-amplitude shapes, `amp=1.0` passed explicitly):

| family | ODE | Caputo | DDE | latent1 | latent3 | worst | rho_eta/worst | cap |
|---|---|---|---|---|---|---|---|---|
| pulse | 0.997 | 0.951 | 1.048 | 1.087 | 1.265 | **1.265** | **0.3135** | 0.3464 |
| multiscale | 0.660 | 0.593 | 0.816 | 0.742 | 0.890 | **0.890** | 0.4456 | 0.3464 |

The latent-3 rival is the worst case (memory coupling amplifies prey
excursion), and the focal Caputo gain does NOT dominate the family — the chief
audit's warning is quantitatively confirmed (Caputo alone would give 0.42/0.68,
the robust constants are 0.31/0.45).

**Theorem R3b-pos (robust outer bound for the frozen transient protocol
class).** For the fixed-shape families and the common ecological prey output,
every input common-safe for the rival family `{ODE, Caputo, DDE, latent1,
latent3}` satisfies

    ||u||_2 <= rho_eta(A) / kappa_V^{robust}(A),
    kappa_V^{robust} = max_M kappa_{V,M}^inf,

and at the primary cell this gives `||u||_2 <= 0.3135` (pulse) — a genuine
Strong-Allee-dependent outer bound, tighter than the actuator cap, valid for
all rivals simultaneously. ∎

### B.5 The repaired safety interface for R1/R4

Combining B.1-B.4, the valid outer safe-energy interface is

    B_safe,m <= sqrt(T) u_max                          (all design classes),
    B_safe,m <= min(sqrt(T) u_max, rho_eta/kappa_V^robust)
                                          (fixed-shape transient protocols).

The first line is R1's generic interface (already proved in Round 1). The
second is the new Allee-dependent refinement, restricted to transient protocol
classes. The fundamental statement "Allee proximity forces ALL safe experiments
to carry little information" is **false as stated** (Theorem R3b-neg) and
**true protocol-relative** (Theorem R3b-pos): proximity to the Allee threshold
shrinks the safe budget of every transient protocol class through
`rho_eta -> 0`, while broadband/parameterized protocols evade it only by
spending amplitude budget that the cap independently limits.

---

## Gate decision (end of Round 3)

The prompt's gate allows R4 iff both:

1. **a usable quantitative E_m bound for the frozen class** — SATISFIED:
   certified T9b bound + empirical envelope + rate diagnostics (§A.2);
2. **a mathematically valid outer safe-excitation bound for the declared
   experiment class OR a rigorous negative theorem** — SATISFIED with BOTH:
   negative theorem R3b-neg for the unrestricted class and coercive outer
   bound R3b-pos for the frozen transient class (§B).

**Decision: GO for Round 4.** R4 should combine R1 + R3a (T9b-certified E_m)
+ the repaired interface B.5 into a universal testing lower bound for the
declared experiment class — i.e., a minimum-error statement for discriminating
Caputo memory from the nested latent hierarchy under the actuator cap and,
for transient protocols, under the Allee-coercive budget. R4 must keep the
negative theorem visible: the impossibility is protocol-relative, not absolute.

Residual items for R4/R5 (not blocking):
- certified (T9b) `m(eps)` inversion for the R4 constants;
- whether the robust worst case over a *declared* (not benchmark-locked)
  latent window `[ell_min,L_max]` exceeds latent3's value — open, needs the
  window-wide worst case, deferred to R4 if the testing bound is to be
  window-robust;
- nonlinear lift of all safety statements remains scoped to the linearized
  regime (manuscript Remark `rem:nfl_scope`).
