# R3-G — Nonlinear discrimination bound: gain double-counting audit

**Round 03, researcher deliverable.**
**Finding: the manuscript's chain is clean. My own Round-02 Theorem D-NL double-counts the
gain and is therefore VACUOUS as written. Corrected below.**

---

## 1. The manuscript chain is correct (verified)

The published chain is: Young's inequality (`L¹ ∗ L² → L²`) to convert a certified response-kernel
error into a mean separation, then Pinsker to convert separation into a testing-error floor.

With `σ = 0.10`, `‖u‖₂ ≤ 0.120`, and the interval-certified prey-response errors
`Ê_m^state`:

| m | `Ê_m^state` | `‖Δμ‖₂ = Ê·‖u‖₂` | KL | TV ≤ √(KL/2) | Pinsker `P_e ≥ (1−TV)/2` | manuscript |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0.5335 | 6.402e−02 | 2.049e−01 | 0.3201 | **0.3400** | 0.340 |
| 32 | 0.0070 | 8.400e−04 | 3.528e−05 | 0.0042 | **0.4979** | 0.498 |

**Reproduced exactly.** There is **no** gain double-counting in the manuscript: `Ê_m^state` is
defined as the `L¹` error of the *end-to-end prey-response kernel*, so Young closes the chain in
one step and no amplification factor is needed or used. The audit clears the paper on this point.

### 1.1 One improvement the manuscript should take

Pinsker is loose. The two hypotheses are Gaussian with **common** covariance `σ²I`, so the exact
minimax error is available in closed form, `P_e^* = Φ(−d/2)` with `d = ‖Δμ‖₂/σ`:

| m | Pinsker (manuscript) | exact `Φ(−d/2)` | gain |
|---:|---:|---:|---:|
| 4 | 0.3400 | **0.3744** | +0.0344 |
| 32 | 0.4979 | **0.4983** | +0.0004 |

The exact bound is tighter, simpler, and requires no extra assumption. It should replace Pinsker
throughout. The qualitative conclusion at `m = 32` is unchanged (both say "chance"); at `m = 4`
the manuscript understates the floor by 0.034.

---

## 2. Where the double-counting actually is: my Round-02 Theorem D-NL

`THEOREM_D_NONLINEAR_LIFT.md` §C4–C5 states

```
||C(ξ_F − ξ_m)||_∞  ≤  A_NL(r,T) · E_m^G · ||u||_∞ ,
     A_NL(r,T) = ||C|| · E_α( (||J|| + M₂(r) r) T^α )
```

and then feeds that into `P_e^* ≥ Φ( −(√n/2σ) A_NL E_m^G U_NL(δ) )`.

**This multiplies a gain onto a quantity that already contains it.** `E_m^G` (equivalently
`Ê_m^state`) is the `L¹` error of the *response* operator, prey-input to prey-output — the whole
propagation through the system is already inside it. Young's inequality then gives
`‖Δ output‖ ≤ E_m^G ‖u‖` with **no** further factor. The Mittag-Leffler / Grönwall amplification
`E_α((‖J‖+M₂r)T^α)` is a second, redundant copy of the same input-to-state gain, and it is
enormous.

Exact constants for the locked model at `A = 0.25`:

```
J = [ −0.125  −0.500 ]      trace = −0.125  (= (7A−2)/(8A))     ✓
    [ +0.500   0.000 ]      det   = +0.250  (= (2−3A)/(20A))    ✓
||J||₂ = 0.566391      ||J||_∞ = 0.625
```

With `α = 0.85`, `T = 12`, `r* = 0.0183`, `M₂ = 4.589`:

| norm used | `(‖J‖+M₂r*)T^α` | `E_α(·)` (asymptotic) | `A_NL·E_m^G·U_NL` at m=4 | resulting bound |
|---|---:|---:|---:|---:|
| `‖J‖₂` | 5.376 | 1.63e+03 | 1.313 | `P_e^* ≥ 2.6e−11` |
| `‖J‖_∞` | 5.861 | 3.53e+03 | 2.844 | `P_e^* ≥ 3.4e−46` |

**The bound as written is vacuous.** It asserts that the testing error is at least `10^{−11}`,
which is true of every testing problem and says nothing. My Round-02 document graded this
"YELLOW — true but operationally vacuous" for a *different* reason (the tiny certified amplitude);
the actual defect is worse and structural: the stated inequality carries no information at all.

---

## 3. Corrected bound

Drop `A_NL`. On the certified safe ball, with `‖u‖_∞ ≤ U_NL(δ) = 1.51e−3`:

```
S_NL := E_m^G · U_NL(δ)        (Young; no amplification factor)
P_e^* ≥ Φ( −(√n/2σ) S_NL )     (exact two-point Gaussian, common covariance)
```

At `n = 1`, `σ = 0.10`:

| m | `E_m^G` | `S_NL` | corrected `P_e^*` ≥ | as written (vacuous) |
|---:|---:|---:|---:|---:|
| 4 | 0.5335 | 8.056e−04 | **0.498393** | 2.6e−11 |
| 32 | 0.0070 | 1.057e−05 | **0.499979** | 3.4e−46 |

Removing the double-counted gain moves the bound from *vacuous* to *maximally informative*: inside
the nonlinearly certified safe set, the four-class problem is indistinguishable from coin-flipping
**even at `m = 4`**, where the surrogate error is 0.53 — two orders of magnitude larger than at
`m = 32`.

That is a substantively different conclusion from Round 02's. It sharpens, not weakens, the
qualitative finding, and it relocates the blame precisely:

- **Not** the memory-approximation mechanism (`E_m^G` at `m=4` is huge and still yields chance).
- **The certified amplitude.** `U_NL = 1.51e−3` is 2.5% of the linear certificate. There is simply
  not enough excitation left after paying for nonlinear safety via an invariant-ball argument.

So the invariant-ball route to nonlinear safety is not merely lossy — it is self-defeating: it
buys a safety certificate by shrinking the input to the point where nothing can be identified.
This is the strongest argument for the validated-integration route (R3-D) over the invariant-set
route, and it is consistent with R3-F, where designs certified *empirically* safe at
`U = 0.100` — 66× the invariant-ball budget — reach macro-accuracy 0.803.

---

## 4. Retractions

1. **`THEOREM_D_NONLINEAR_LIFT.md` §C4–C5.** The factor `A_NL(r,T)` must be deleted from the
   discrimination inequality and from Theorem D-NL. As published in that document the bound is
   vacuous (`P_e^* ≥ 2.6·10⁻¹¹`).
2. **The stated reason for the YELLOW verdict** was incomplete. The verdict stands (the theorem is
   operationally useless) but the mechanism is the certified amplitude, quantified in §3, not a
   residual nonlinear effect. The Round-02 claim that "the nonlinearity is not what breaks the
   discrimination step; the safety step is" is *correct* and is now proved properly rather than by
   an argument that happened to contain a redundant factor.

## 5. Recommendations for the manuscript

- Keep the `Ê_m^state` → Young → testing-floor chain. It is correct.
- Replace Pinsker with the exact `Φ(−d/2)` bound (§1.1). Update `0.340 → 0.374`; `0.498` is unchanged
  to three decimals.
- Do **not** import Theorem D-NL in any form that carries `A_NL`.
- If a nonlinear safety statement is wanted, take it from R3-D (validated enclosures at usable
  amplitude), not from the invariant-ball certificate.

## 6. Not done

- `n > 1` sample schedules: the `√n` scaling is stated but the correlated-noise case
  (measurements at nearby times on a smooth trajectory are not independent) is **not** analysed.
  The `‖·‖₂ ≤ √n‖·‖_∞` step is valid but crude, and with correlated noise the effective `n` is
  smaller. Untouched, and it makes the reported floors *conservative* in the safe direction.
- The Mittag-Leffler values in §2 use the large-argument asymptote `E_α(x) ≈ α^{−1}exp(x^{1/α})`.
  The conclusion (vacuity) is insensitive to this: any `E_α(5.4) > 10` already destroys the bound.
