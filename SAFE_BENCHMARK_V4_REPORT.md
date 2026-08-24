# SAFE_BENCHMARK_V4_REPORT — Task R2-F

**Status: 2 of 3 amplitudes complete (1512 of 2268 cells).** `amp=0.050` and `amp=0.063` are finished
(756 cells each, 200 replicates per cell); `amp=0.100` (the v3-comparable baseline) is still running,
split across Orion and Aureus. The two completed amplitudes are the *linear-certificate diagnostics*
and they already settle the scientific question. **Frozen v3 was not touched.**

**Naming discipline (chief instruction, honored).** The `0.050`/`0.063` runs are called
**linear-certificate diagnostics**, not a "nonlinear-safe benchmark": `0.063 = U(0.05)` is the
*linearized* safe amplitude. The genuinely nonlinear certificate is `U_NL(0.05)=1.6·10^{-3}`
(`THEOREM_D_NONLINEAR_LIFT.md`), i.e. **40× smaller**, so these runs are *not* certified-safe. §4 shows
that this distinction is not pedantic — it is measured.

**Comparability.** Identical designs (6), channels (3), SNRs (3), sampling (`n=120`, `T=12`), scoring
(BIC over 4 candidate classes), stable-regime `A∈{0.20,0.25}`, model set (5 generators), and **identical
seeds** (`1000+7919k+⌊100α⌋`) as frozen v3. Only `‖u‖_∞` changes. Code: `rescue_compute/v4_safe_benchmark.py`;
raw per-cell records: `state_v4.jsonl`.

---

## 1. Accuracy versus amplitude

| amplitude | cells | micro-accuracy | **macro-accuracy** | diverged |
|---|---:|---:|---:|---:|
| 0.050 | 756 | 0.4084 | **0.4570** | 0 |
| 0.063 (`=U(0.05)`) | 756 | 0.4253 | **0.4712** | 0 |
| 0.100 (v3 baseline) | running | — | (v3 measured **0.537**) | — |

Chance level is 0.25. Lowering the amplitude from the v3 baseline to the linear certificate costs
≈0.066 of macro-accuracy (0.537 → 0.471), and a further drop to 0.050 costs ≈0.014 more.

**Per-class recall.**

| amplitude | ODE | Caputo | DDE | latent |
|---|---:|---:|---:|---:|
| 0.050 | 0.980 | 0.412 | 0.229 | 0.207 |
| 0.063 | 0.974 | 0.445 | 0.264 | 0.202 |
| 0.100 (v3) | 0.972 | 0.524 | 0.410 | 0.242 |

Every non-ODE class degrades as the amplitude falls, while ODE recall stays ≈0.97: **under weak
excitation BIC increasingly defaults to the simplest mechanism.** DDE is the most amplitude-sensitive
(0.410 → 0.229, a 44 % relative loss).

## 2. Design ranking versus amplitude

| design | 0.050 | 0.063 | 0.100 (v3) |
|---|---:|---:|---:|
| prbs | **0.706** | **0.615** | 0.584 |
| sinusoid | 0.589 | 0.559 | 0.534 |
| chirp | 0.427 | 0.482 | 0.507 |
| multisine | 0.304 | 0.401 | 0.583 |
| pulse | 0.221 | 0.259 | 0.414 |
| multiscale | 0.202 | 0.236 | 0.324 |

The ranking is **not** amplitude-invariant: `prbs` and `sinusoid` *improve* their relative standing as
amplitude falls, while `multisine` collapses (0.583 → 0.304). Any claim that a design ordering is
intrinsic must therefore be stated **at a fixed amplitude**.

## 3. Safety instrumentation (the point of this run)

Allee-crossing rate and worst-case margin `min_t(x−A)` per design:

| design | cross rate @0.050 | margin @0.050 | cross rate @0.063 | margin @0.063 | max realized gain @0.063 |
|---|---:|---:|---:|---:|---:|
| sinusoid | 0.71 | −0.274 | **0.93** | −0.284 | 16.8 |
| prbs | 0.71 | −0.252 | **0.93** | −0.282 | **22.6** |
| chirp | 0.50 | −0.229 | 0.71 | −0.266 | 10.8 |
| multisine | **0.00** | **+0.233** | 0.14 | −0.122 | 8.6 |
| pulse | **0.00** | **+0.345** | **0.00** | **+0.323** | 2.1 |
| multiscale | **0.00** | **+0.354** | **0.00** | **+0.338** | 1.5 |

## 4. **The linear certificate does not certify the nonlinear system** (measured)

At `amp=0.063`, which *is* the linearized safe amplitude `U(0.05)=0.0634`, `sinusoid` and `prbs` cross
the Allee threshold in **93 %** of cells. The linear envelope is therefore **not** a safety guarantee
for the nonlinear trajectory.

The mechanism is visible in the last column: the **realized gain** `‖ξ‖_∞/‖u‖_∞` reaches **22.6**
(prbs) and 16.8 (sinusoid), versus the linear worst case `Γ_T = 5.78`. Exceeding `Γ_T` is not a
contradiction of the linear theory — it is the signature of **leaving the linear regime**: once the
prey crosses `A`, the strong-Allee extinction funnel amplifies the excursion far beyond anything the
linearization predicts. Conversely `pulse` (gain 2.1) and `multiscale` (gain 1.5) stay well inside the
linear envelope and never cross.

**This vindicates the chief's naming instruction.** Had these runs been published as a
"nonlinear-safe benchmark", the paper would have asserted safety for designs that violate it 93 % of
the time. It also gives independent, measured support to the `U_NL ≪ U_lin` finding of
`THEOREM_D_NONLINEAR_LIFT.md`: the nonlinear certificate is 40× below the linear one, and at 40× above
it, safety fails for sustained designs.

## 5. The headline result: safe discrimination is barely better than chance

Restricting attention to designs that **never** cross the Allee threshold:

| amplitude | safe designs (0 % crossing) | best accuracy among them | chance |
|---|---|---:|---:|
| 0.050 | multisine, pulse, multiscale | **0.304** (multisine) | 0.25 |
| 0.063 | pulse, multiscale | **0.259** (pulse) | 0.25 |

At the linear certificate amplitude, the best *never-crossing* design achieves **0.259 against a
chance level of 0.25**. The designs that discriminate well (prbs 0.615, sinusoid 0.559) cross in 93 %
of cells. **Within genuinely non-crossing excitation, memory-mechanism discrimination is essentially at
chance.** This is the safety–informativeness ceiling, measured in the regime where it applies, and it
is a materially stronger and more honest statement than v3's `0.537` — which was obtained 58 % above
the linear certificate, i.e. outside any safe regime.

## 6. No circular certification (F4 compliance)

Safety was **not** assumed from the amplitude bound and then reported as verified. Each cell's margin
was measured from the simulated nonlinear trajectory (`bench.safety_metrics`), independently of the
amplitude used to generate it. That is precisely why the `0.063` failures could be detected.

## 7. Limitations

- `amp=0.100` is incomplete; its row is quoted from frozen v3, which used the same code path, seeds and
  scoring. The v4 `0.100` run exists to confirm reproducibility and will be reported when it lands.
- Margins are measured on a `N=400` PECE grid, not interval-certified. A rigorous claim needs validated
  integration (recommended in `THEOREM_D_NONLINEAR_LIFT.md` §C7).
- BIC, not Bayesian evidence (unchanged from v3, by design).
- Two `A` values only (`0.20, 0.25`), both in the stable regime.
