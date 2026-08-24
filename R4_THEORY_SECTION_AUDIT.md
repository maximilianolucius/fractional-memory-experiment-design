# R4-C — Theory section rebuilt

**Status: DONE. `paper/sections/sec3.tex` replaced in full. Pre-edit version kept at
`paper/backup_preR3/sec3_preR4.tex`.**

The old section carried three defects the chief flagged: it presented the SOE construction as a
theorem contribution, it stated the testing bound through an unspecified function `Ψ` with Pinsker
as the operative inequality, and it moved between kernel-level and response-level error without
marking the transition. All three are gone.

---

## 1. Final chain, in the required order

| # | item | label | status as stated in the text |
|---|---|---|---|
| 1 | Structural exact separation | `thm:T4` | **foundation** — "classical fractional-systems material; no novelty is claimed for it" |
| 2 | Positive-SOE endpoint-inclusive estimate + exact horizon scaling | `lem:soe` | **borrowed tool**, attributed to McLean~`K07` in the same subsection, with proof |
| 3 | Finite-horizon closure of the latent hierarchy | `cor:closure` | corollary of 2 |
| 4 | Three error objects (O1)/(O2)/(O3) separated | §`subsec:semantics` | **proved/measured**, with the measured attenuation range |
| 5 | Exact two-point Gaussian obstruction at response-operator level | `thm:T20` | **proved here** |
| 6 | Certified finite-state prey-response approximation | `thm:T23` | **computed**, interval enclosure for `m ≤ 32` |
| 7 | Response-level continuation to `m = 64, 128` | `tab:state-approx-large` | **computed**, high-accuracy floating point, labelled as such |

## 2. Semantic constraints — how each is enforced in the text

**"Never identify bare-kernel error with prey-response error."** A dedicated subsection defines
(O1) kernel error, (O2) induced response-operator error, (O3) fixed-input discrepancy, states
`(O3) ≤ (O2)` and then says explicitly:

> There is no inequality in either direction between (O1) and (O2), and no constant relating them:
> computed from the same surrogate family, the plant *attenuates* the kernel error monotonically,
> by a factor 1.009 at `m ≈ 5` falling to 0.675 at `m = 128`. Kernel-level numbers are therefore
> never propagated into response-level claims anywhere in this paper.

**"Never read `Ê_m^state` as a design objective."** Stated as a consequence in the same subsection,
with the in-paper counterexample:

> $\widehat E_m^{\rm state}$ is an *obstruction certificate and not a design objective*: the
> frequency band that maximises $|G_\alpha-G_m|$ (here $\omega\approx0.4$) selects the multiscale
> waveform, which excites 87% of the worst case at $m=32$ and is nonetheless the *least*
> informative design in the four-class benchmark.

**"Define the test/minimax reduction unambiguously."** The observation model is now fully specified
before the theorem: prey channel, `n` sample times in `(0,T]`, additive Gaussian noise with
**common** covariance `σ²I` under both hypotheses, means obtained by convolving each response
kernel with the **same** admissible input. The two hypotheses are named explicitly.

**"Exact Gaussian bound is primary; Pinsker only for comparability."** `thm:T20` now reads
`P_e^* = Φ(−d/2)` with `d = ‖Δμ‖₂/σ`, and `d ≤ Ê_m^state B/σ` by Young. The paragraph after it
states that Pinsker appears in `tab:state-approx` only for comparability and is uniformly looser,
by 0.034 at `m = 4`. **`Ψ` no longer appears anywhere.**

**"No invalid `L²` kernel pairing."** Stated as hygiene in the text: *"The bound is routed through
the `L¹` norm of the response kernel, never through `‖k_α−k_m‖_{L²}`, which is infinite for
`α ≤ 1/2` and would make any such statement vacuous on part of the declared range."*

**"Label high-accuracy numerical vs interval-certified."** `tab:state-approx` (`m ≤ 32`) is stated
to be **interval enclosures**; `tab:state-approx-large` (`m ≤ 128`) is stated to be
**high-accuracy floating-point evaluations with a two-mesh quadrature-error estimate, not
enclosures**, and — because that surrogate is one admissible element rather than the infimum —
upper bounds on `Ê_m^state`, hence inducing conservative floors. The sentence "The distinction is
maintained wherever these numbers are used" is in the text.

## 3. Numerical support quoted in the section

| claim in `sec3` | source | status |
|---|---|---|
| `E(T) = T^α E(1)` verified to machine precision, 285 cells | `rescue_compute/c1_complexity_law.json` | measured |
| bound holds at `c = π√(α(1−α))` with constants 0.29–11.1; attained to within 1.00 at `α=0.70, m=128` | same | measured |
| plant attenuation 1.009 → 0.675 | `rescue_compute/r3b_response_semantics.py`, `r3e_response_cert.json` | measured |
| exact bound tighter than Pinsker by 0.034 at `m=4` | recomputed on the manuscript's own `Ê_m^state` | measured |
| floors 0.374 / 0.4996 / 0.49999 at `m = 4 / 64 / 128` | `rescue_compute/r3e_response_cert.json` | measured |

## 4. What is deliberately *not* claimed

- No priority for the branch-point/high-frequency separation argument.
- No new approximation method, rate law, or positive-weight priority.
- The boundary constant `c = π√(α(1−α))` is **not** claimed attained; the text says it is open.
- No lower bound on `E_m^+` is claimed (none was proved).
- `thm:T23` remains scoped to "the displayed Matignon-stable cells" and `m ∈ {4,8,16,32}` — the
  extension to `m = 64,128` is explicitly a different, non-enclosed computation.

## 5. Build

`bash paper/build_latex.sh` → exit 0, zero LaTeX errors, zero undefined references, zero
multiply-defined labels. 25 pages.
