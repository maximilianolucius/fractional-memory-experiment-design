# R3-B — Response-operator semantics, and audit of Theorem T23

**Round 03, researcher deliverable.**
**Finding: T23 is well-posed and the testing chain that uses it is valid. But the manuscript
never separates three distinct error objects, and two of them are used interchangeably in
the prose. One consequence is a design recommendation that the data contradict.**

---

## 1. Three different objects

The manuscript works with quantities that all look like "the order-`m` approximation error".
They are not the same object and they do not have a fixed ratio.

**(O1) Memory-kernel error.** `E_m = ‖K_α − Σ_j c_j e^{−λ_j ·}‖_{L¹(0,T)}`, `K_α(t)=t^{α−1}/Γ(α)`.
A statement about the *fractional operator*, independent of `J`, `B`, `C`. This is what
Lemma B.2 (R3-A) and the C-1 sweep measure.

**(O2) Induced response-operator error.** For the linearised plant,
```
G_α(s) = C (s^α I − J)^{−1} B ,     G_m(s) = C (R_m(s)^{−1} I − J)^{−1} B ,   R_m(s) = Σ_j c_j/(s+λ_j)
Ê_m^state = inf over the admissible class of  ‖g_α − g_m‖_{L¹(0,T)}  (time-domain response kernels)
```
The operator norm of the *difference of input-output maps*, `L^∞ → L^∞`. This is what T23
certifies and what the testing bound needs. It is a **minimax** quantity: infimum over rival
models of a supremum over inputs.

**(O3) Fixed-input response error.** `‖(g_α − g_m) ∗ u‖ / ‖u‖` for one specific `u`. What an
actual experiment with an actual waveform sees.

By construction `(O3) ≤ (O2)` for every `u`. The relation between (O1) and (O2) is **not** an
inequality in either direction — it depends on `J`, `B`, `C` and on `α`.

---

## 2. (O1) vs (O2) measured on the same construction

To compare (O1) and (O2) fairly they must come from the *same* surrogate. Below, both are
computed from the positive-weight trapezoidal SOE of Lemma B.2 at `α = 0.85`, `A = 0.25`,
`T = 12`, prey→prey channel, `J = [[−0.125, −0.5],[0.5, 0]]`, `‖J‖₂ = 0.566391`.

| m | (O1) kernel `L¹` | (O2) response `L¹` | ratio (O2)/(O1) | `H∞`: `sup_ω|ΔG|` | `H∞`/(O1) |
|---:|---:|---:|---:|---:|---:|
| 5 | 1.274672e+00 | 1.286030e+00 | 1.009 | 1.217136e+00 | 0.955 |
| 8 | 5.258967e−01 | 4.975063e−01 | 0.946 | 6.630582e−01 | 1.261 |
| 16 | 1.390370e−01 | 1.301651e−01 | 0.936 | 1.714956e−01 | 1.234 |
| 32 | 3.077963e−02 | 2.311259e−02 | 0.751 | 2.514938e−02 | 0.817 |
| 64 | 2.271856e−03 | 1.577235e−03 | 0.694 | 1.261622e−03 | 0.555 |
| 128 | 7.157331e−05 | 4.834163e−05 | 0.675 | 5.889653e−05 | 0.823 |

Read the **third** column: compared in the *same* norm, the plant **attenuates** the kernel
error, monotonically, from a factor 1.01 at `m ≈ 5` down to 0.675 at `m = 128`, apparently
converging to a limit near 0.67. That is an ordered relationship, not an erratic one.

The last two columns are the `H∞` operator gain, which is what an earlier draft of this
document compared against (O1). **That comparison mixed norms** (`L¹` against `H∞`) and
produced a spuriously non-monotone ratio (0.555–1.261). The `L¹`-to-`L¹` comparison is the
correct one and it is well behaved; the `H∞` column is retained only because §4 needs the
frequency at which `|ΔG|` peaks.

**Audit consequence.** Any sentence that treats a kernel-error number as a response-error number,
or that propagates one into the other with a fixed constant, is unjustified: the attenuation
factor moves from 1.01 to 0.675 over the `m` range of interest, so a constant is wrong by up
to 50% at the ends. The manuscript keeps
the two symbols distinct (`Ê_m` vs `Ê_m^state`) — that is correct — but the surrounding prose
("the same response to any tolerance", "the kernel error therefore controls the response") elides
the distinction. **T23 itself is clean; the narrative around it needs the separation made explicit.**

Consistency check against the manuscript: T23 reports `Ê_m^state = 0.5335` at `m = 4` and
`0.0070` at `m = 32`, obtained by interval arithmetic over the *optimised* strictly-proper class
`𝒢_m`. My SOE is a *particular* construction, not the infimum, so it must be larger — and it is,
by factors 2.3 (`m≈4`) and 3.6 (`m=32`). Consistent. My numbers are upper bounds on T23's; the
ratios in the table are internally consistent because both columns come from the same surrogate.

---

## 3. (O2) vs (O3): how much of the worst case does a real waveform excite?

Fraction of the operator error actually excited, `[‖ΔG·U‖₂/‖U‖₂] / sup_ω|ΔG|`:

| input | m≈5 | m=32 | m=128 |
|---|---:|---:|---:|
| multiscale | **0.657** | **0.865** | **0.539** |
| pulse | 0.317 | 0.414 | 0.264 |
| pwc6 (found by R3-F) | 0.301 | 0.384 | 0.252 |
| chirp | 0.132 | 0.174 | 0.117 |
| multisine | 0.088 | 0.089 | 0.085 |
| sinusoid | 0.024 | 0.072 | 0.052 |

Spread of **more than 30×** between waveforms. The worst-case operator bound is therefore very
loose for most designs: at `m = 32` a sinusoid sees 7% of the certified error, multiscale 87%.

**This is the direction the testing bound needs and it is safe.** The obstruction argument requires
an *upper* bound on separation that is uniform over admissible inputs, so using (O2) is correct and
conservative: no design in the budget can separate the hypotheses better than `Ê_m^state·‖u‖`. The
floors `P_e^* ≥ 0.340 / 0.498` (see R3-G, where the exact bound gives 0.374 / 0.498) are valid.

**But it must not be read in the other direction**, and §4 shows the manuscript is close to doing so.

---

## 4. The design corollary the manuscript implies is contradicted by its own benchmark

`sup_ω|ΔG|` peaks at **`ω ≈ 0.38–0.49`** for every `m` tested — a low frequency. Reading (O2) as a
design guide gives: *concentrate input energy near `ω ≈ 0.45` to separate Caputo from a finite-latent
rival*. Among the six historical waveforms exactly one does that — multiscale, whose components sit
at `ω = 2π/12 = 0.52` and `2π/4 = 1.57` — and accordingly it excites 87% of the worst case at `m=32`,
by far the highest.

Multiscale is also **the worst design in the four-class BIC benchmark** (macro 0.514, `Caputo` recall
0.404, `latent3` recall 0.244; R3-F Stage 2).

There is no contradiction, but there is a trap, and it must be stated in the paper:

- `sup_ω|ΔG|` measures only the **Caputo-vs-latent** pair.
- The benchmark decides among **four** classes; the binding difficulty is `ODE` vs the memory models
  and `DDE` vs the rest, which live at different frequencies.
- Maximising one pairwise discrepancy therefore does **not** maximise multi-class accuracy. R3-F's
  objective avoided this by construction — it uses `min` over *all* pairs, not one pair — which is
  why its designs (`pwc6`, excitation fraction 0.38) beat multiscale (0.87) by +0.29 macro-accuracy.

**Audit consequence.** Any statement of the form "the response-operator error identifies the most
informative excitation band" must be scoped to the two-class problem. In the four-class problem it
is false, and the paper's own Table (benchmark ranking) is the counterexample.

---

## 5. Verdict on T23 and required edits

**T23 stands.** Statement, hypotheses (exact prey-to-prey `G_α`; strictly proper finite-state class
`𝒢_m`; pole-region and `L¹` mass cap; interval enclosures) and use (Corollary → testing floor) are
correct and correctly typed as a response-operator quantity.

Required edits, for R3-I:

1. **Add a definitions paragraph** distinguishing (O1)/(O2)/(O3) explicitly, with the notation the
   paper already uses (`Ê_m`, `Ê_m^state`, and a new symbol for the fixed-input error).
2. **State the quantifier order of `Ê_m^state`** — infimum over rivals of the supremum over inputs —
   and state that the testing floor is therefore uniform in the input within the budget. This is a
   strength of the result and it currently goes unstated.
3. **Remove or scope any kernel→response propagation in prose.** Give the measured attenuation
   range (1.01 → 0.675, monotone decreasing in `m`) as the reason it cannot be done with a
   single constant.
4. **Add the §4 warning.** One sentence: the band that maximises a single pairwise discrepancy is not
   the band that maximises multi-class accuracy, with multiscale as the in-paper counterexample.
5. **Do not** advertise `Ê_m^state` as a design objective. It is an obstruction certificate.

## 6. Not done

- The (O2) values here come from my SOE construction, **not** from the interval-certified infimum
  over `𝒢_m`. They are valid upper bounds and internally consistent, but the ratio table would shift
  (not qualitatively) if recomputed with T23's optimised surrogates. Recomputing (O1)/(O2) inside the
  interval-arithmetic pipeline is the clean version and is **not** done.
- `sup_ω` was taken over `ω ∈ [10⁻³, 10³]` on 4000 log-spaced points. The peak is interior
  (`ω ≈ 0.4`), so the grid is adequate, but this is a discrete maximum, not a certified enclosure.
- Only the prey→prey channel. The predator channel and the two-channel case are untouched.

## 7. Artifacts

`rescue_compute/r3b_response_semantics.py` — reproduces every number in §2 and §3.
