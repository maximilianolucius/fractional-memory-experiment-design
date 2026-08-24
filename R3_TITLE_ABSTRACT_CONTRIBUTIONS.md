# R3-J — Title, abstract and contributions, rewritten

**Round 03, researcher deliverable.** Drafts for chief/author decision. The rewrite is forced
by R3-F (the submitted headline claim is falsified) and constrained by R3-A (Lemma B.2 must be
demoted).

---

## 1. What is wrong with the submitted framing

| submitted claim | status after Round 03 | source |
|---|---|---|
| "Safe identification of ecological memory is constrained by an explicit safety–informativeness trade-off" | **falsified as a general claim** — a safe design at the same budget scores 0.803 vs 0.514 for the only safe classical design | R3-F |
| Trade-off is the paper's concluding contribution | must be demoted to a property of six classical waveform families | R3-F |
| Constructive `L¹` approximation (T9b / Lemma B.2) as a headline analytical result | **technique is McLean (2018)**; ours is the endpoint-inclusive corollary | R3-A |
| `Ê_m^state` table stops at `m = 32`, floor 0.498 | floor reaches 0.49999 at `m = 128`; truncation hides the strength of the obstruction | R3-E |
| Safety decided by grid sampling | now certified a posteriori; sampled verdicts confirmed 28/28 | R3-D |
| Pinsker used for the testing floor | exact two-point bound is tighter (`0.340 → 0.374` at `m=4`) | R3-G |

The paper's actual best result was never stated: **the binding obstruction to identifying
ecological memory is latent complexity, not safety** — and that is a sharper, more defensible
claim than the one submitted.

---

## 2. Title

Submitted:
> Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee
> Predator–Prey Model

It is not wrong, but it is generic and it promises the trade-off framing. Three options, in my
order of preference:

**T1 (recommended).**
> Waveform Design, Not Amplitude, Governs Safe Memory Discrimination in a Strong-Allee
> Predator–Prey Model

States the falsification as the finding, is specific, and is honest about what was measured
(amplitude was tested and rejected as the knob — R3-H).

**T2.**
> Safe Active Discrimination of Ecological Memory: Latent Complexity, Not Safety, Is the
> Binding Obstruction

Leads with the theoretical conclusion. Stronger for a mathematics venue; slightly overpromises
generality since everything is one locked model.

**T3 (conservative).**
> Safe Experimental Design for Discriminating Fractional, Delayed and Finite-Latent Memory in a
> Strong-Allee Predator–Prey Model

Minimal edit to the submitted title, drops the implicit trade-off claim. Use this if the chief
wants the smallest possible delta from the desk-rejected version.

---

## 3. Abstract (rewritten)

> A fitted fractional order `α` does not identify a fractional mechanism: on a finite horizon
> `[0,T]`, delayed feedback or a few hidden states reproduce similar trajectories. We ask when a
> *safe* controlled experiment can separate these mechanisms in a strong-Allee predator–prey
> system with coexistence equilibrium `x* = 2/3`, `y*(A) = 2(2−3A)/(9A)`, whose model, locked
> parameters and Jacobian `J(A)` are inherited from a previously submitted companion paper and
> are not claimed as new.
>
> Two obstructions are separated. The first is structural and is **not** binding: the collocated
> Caputo transfer decays as `O(ω^{−α})`, which no finite rational latent transfer and no strictly
> proper retarded-delay model reproduces exactly. The second is quantitative and **is** binding:
> positive exponential mixtures approximate the memory kernel in `L¹(0,T)` at a root-exponential
> rate — for every `c < π√(α(1−α))` there is `A(α,c)` with `E_m ≤ A(α,c) T^α e^{−c√m}`, a
> lemma-level extension of McLean's positive-weight quadrature construction to the singular
> endpoint — so that `m(ε) = O(log²(1/ε))` hidden states suffice. Computed directly at the prey
> response level, the `L¹` surrogate error falls from `1.29` at `m = 4` to `4.8e−5` at `m = 128`,
> and the induced minimax testing error rises from `0.220` to `0.49999`: at attainable latent
> orders the finite-state rival is indistinguishable.
>
> Against that obstruction we test whether safe excitation must sacrifice information. It must
> not. In a 756-cell, four-class BIC benchmark at three amplitudes (2268 cells, no divergences),
> reducing input amplitude fails as a safety strategy — PRBS still crosses the Allee threshold in
> 71% of cells at half amplitude while remaining the most informative design — and only one of
> six classical waveform families is safe, scoring macro-accuracy 0.514 against 0.537 overall.
> Searching 163 840 candidate waveforms outside those families under a hard margin constraint at
> the *same* amplitude budget yields piecewise-constant designs that are safe and far more
> informative: macro-accuracy **0.803** with zero threshold crossings, versus 0.514 for the only
> safe classical design and 0.763 for the best classical design of any kind, which crosses in
> 35.7% of cells. A posteriori validated integration certifies the safety of these trajectories
> (12 of 28 classifications SAFE-CERTIFIED, 16 CROSSING-CERTIFIED, none indeterminate), whereas an
> invariant-ball certificate admits only `‖u‖_∞ ≤ 1.4e−3`, 70× smaller, and is useless at that
> amplitude.
>
> The safety–informativeness trade-off reported for classical excitation families is therefore an
> artifact of the waveform parameterisation, not a property of the system. What survives is the
> latent-complexity obstruction: even the best safe design recovers only `0.475` recall on the
> finite-latent rival. Safe identification of ecological memory is limited by the declared
> rival-complexity budget `m`, not by the safety margin.

Word count ≈ 400; trim to the target venue. Every number above is traceable to a Round-03
deliverable and reproducible from `rescue_compute/`.

---

## 4. Contributions, reordered

Replace the submitted contribution list with:

1. **A falsification of the safety–informativeness trade-off for this system.** Under a fixed
   peak-amplitude budget and a hard Allee-margin constraint, an unrestricted piecewise-constant
   search finds designs that dominate every classical waveform family on four-class BIC accuracy
   *while* being certified safe (0.803 vs 0.763 best-unsafe / 0.514 best-safe). [R3-F, R3-D]
2. **A negative result on amplitude.** Halving the excitation does not buy safety: crossing rates
   fall only 100% → 71% for the leading design, while the realised response gain *rises* to 4.86×
   the linear certificate, the signature of basin escape rather than linear response. [R3-H]
3. **A quantified latent-complexity obstruction at response level out to `m = 128`,** with the
   induced minimax testing floor reaching 0.49999 — the obstruction that does bind. [R3-E, R3-B]
4. **Validated (a posteriori certified) safety classification** of benchmark trajectories,
   replacing grid sampling; 28/28 decided, and interval-certified nonlinear constants showing the
   invariant-ball route is structurally closed for this vector field. [R3-D, R3-C]
5. **A reproducibility control**: the frozen benchmark reproduces to four decimals on an
   independent host under a re-implemented driver. [R3-H]
6. *Supporting lemmas, not headline claims*: the `T^α` scaling reduction, and the endpoint-inclusive
   `L¹(0,T)` form of the positive-weight exponential-sum rate, both attributed to the existing
   literature for the technique. [R3-A]

Items 1–3 are new; 4–5 are methodological; 6 is explicitly demoted.

---

## 5. Claims to delete outright

- Any sentence asserting a general safety–informativeness trade-off (abstract, Discussion §3,
  Conclusions).
- "the most informative perturbation is not the safest, by a wide margin" — unscoped.
- Novelty language around the `L¹` approximation construction.
- The FCAA split proposed in `ROUND_02_JOURNAL_DECISION.md` (withdrawn in R3-A §6).
- Any reading of `Ê_m^state` as a design objective (it is an obstruction certificate — R3-B §4).

## 6. Figure consequences

- **Fig. 10** (`fig10_safety_tradeoff`): as drawn it is the six-family frontier presented as *the*
  frontier. Must be redrawn with the search designs, which changes its shape qualitatively, or
  relabelled explicitly as "classical waveform families only".
- **New figure recommended**: safety margin vs macro-accuracy scatter over the 12 designs of R3-F
  Stage 2, with the certified-safe region shaded. This is the paper's main result and it currently
  has no figure.
- **Table** `tab:state-approx`: extend to `m = 64, 128` (R3-E) and switch Pinsker → exact bound.
