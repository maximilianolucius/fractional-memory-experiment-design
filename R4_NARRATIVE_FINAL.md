# R4-D — Title, abstract, introduction, contributions, conclusion

**Status: DONE. All five rewritten in the manuscript. Abstract 243 words (limit 250,
verified against the live CNSNS guide). Build clean.**

---

## 1. Title

Chief-selected, applied verbatim:

> **Safe discrimination of fractional, delayed, and latent memory beyond classical waveforms in a
> strong-Allee predator--prey model**

The Round-03 title ("Waveform Design, Not Amplitude, Governs …") is withdrawn: "governs" reads as
a general causal claim, which the evidence does not support.

## 2. Abstract — 243 words

Full text as it stands in `paper/main.tex`:

> Fitting a fractional order $\alpha$ does not identify a fractional mechanism: on a finite
> horizon, delayed feedback or a few hidden states reproduce similar trajectories. We ask when a
> controlled experiment can separate these mechanisms in a strong-Allee predator--prey system
> while keeping the prey above its Allee threshold. Among six classical excitation families the
> accuracy-leading designs all cross the threshold and the only safe one is the least informative,
> which suggests an intrinsic safety--informativeness frontier. We show that frontier belongs to
> the waveform parameterisation, not to the system. Reducing amplitude does not restore safety ---
> the leading design still crosses in $71\%$ of cells at half amplitude --- whereas a constrained
> search over $163\,840$ candidate waveforms, at the same peak-amplitude budget and under a hard
> margin constraint, returns piecewise-constant designs with four-class model-selection accuracy
> $0.803$ and no observed crossings, against $0.514$ for the only safe classical family and
> $0.763$ for the best classical design of any kind, which crosses in $36\%$ of cells. Their
> safety is verified a posteriori by mesh refinement with a rigorous inter-node modulus, and for
> half of the headline trajectories by a validated enclosure. A Pareto cost nevertheless remains,
> so safety is not free. A second obstruction survives waveform search: computed at the
> prey-response level, the finite-state approximation error falls to $5\cdot10^{-5}$ at latent
> order $128$ and the induced exact minimax testing floor reaches $0.49999$. Identifying
> ecological memory is limited by the declared rival-complexity budget rather than by the safety
> margin.

Requirement check:

| requirement | status |
|---|---|
| ≤250 words | **243** ✔ |
| problem in one sentence | sentence 1 ✔ |
| main falsification / positive design result | sentences 3–6 ✔ |
| scope: six classical families vs searched PWC class | named explicitly ✔ |
| large-`m` obstruction as a *separate* result | "A second obstruction survives waveform search" ✔ |
| exact safety wording from R4-B | "verified a posteriori … and for half of the headline trajectories by a validated enclosure" ✔ |
| ≤3–5 numerical values/groups | 4 groups: (71%), (163 840; 0.803/0.514/0.763; 36%), (5e−5 at 128), (0.49999) ✔ |
| no "inherited from a previously submitted companion paper" | absent ✔ |
| no "our previous paper" | absent ✔ |
| no universal "waveform governs" | absent ✔ |
| no categorical "safety is not binding" | explicitly contradicted: "A Pareto cost nevertheless remains, so safety is not free" ✔ |
| no headline novelty for SOE/root-exponential | SOE not mentioned in the abstract at all ✔ |

## 3. Introduction

**Companion-comparison table deleted.** `tab:paper-relation` and its surrounding two paragraphs
are gone; zero references remain to that label. Replaced by one neutral paragraph, the chief's
wording:

> **Provenance of the ecological backbone.** The ecological backbone follows the companion
> certification study [P01]: the equations, locked parameters, coexistence equilibrium and
> Jacobian are restated here for self-containment and are not claimed as contributions of the
> present work. That study certifies dynamical regimes of a specified Caputo model; it does not
> address whether such a model can be told apart from a delayed or latent mechanism reproducing
> the same observations to within $\sigma$, which is the question posed here. No result below
> recertifies the backbone.

Closest prior art is stated **before** the endpoint lemma is invoked: the contribution list ends
with a paragraph naming McLean, Beylkin–Monzón and the structural-separation literature as *not*
contributions.

## 4. Contribution hierarchy as printed

**Headline**
1. Safe waveforms outside the classical families outperform every classical baseline at the same
   budget (0.803 vs 0.514 safe-classical, vs 0.763 best-classical-any).
2. The six-family frontier is not a property of the system — amplitude fails as the knob (71.4%
   crossings at half amplitude, realised gain 4.86× the linear certificate), and a Pareto cost
   remains, so safety is not free.
3. A separate finite-horizon latent-complexity obstruction, quantified at response level to
   `m = 128` (floor 0.49999), which waveform search does not remove.

**Supporting**
4. Trajectory safety status stated exactly: verified a posteriori throughout, validated enclosure
   for 4 of 8 headline trajectories, and only those called rigorous; interval-certified nonlinear
   constants showing the invariant-set route admits inputs 70× smaller.
5. Cross-host reproducibility of the frozen benchmark (2268 cells, three amplitudes, no
   divergences).
6. *Explicitly not contributions*: structural separation (classical) and the positive-SOE
   construction (McLean); only the endpoint-inclusive `L¹(0,T)` variant with exact horizon scaling
   is recorded, as a lemma.

## 5. Conclusion

Rewritten in full. Structure: constructive part (the frontier is a parameterisation artifact, with
the Pareto cost stated), negative part (latent complexity, input-independent because the surrogate
error is an operator norm), then the change of question — from "which safe perturbation separates
the mechanisms", which now has a constructive answer, to "what latent complexity the experiment is
willing to admit as a rival".

## 6. Deleted-claim checklist

| claim | where it was | status |
|---|---|---|
| general safety–informativeness trade-off as a conclusion | abstract, `sec8` subsection title, `sec10` conclusion 3, `sec11`, Fig. 10 caption | **deleted / scoped to the six families** |
| "the most informative perturbation is not the safest, by a wide margin" (unscoped) | `sec10` | scoped ✔ |
| "waveform design governs safety" | Round-03 title | **deleted** |
| "validated integration certifies these trajectories" | `sec10` | downgraded ✔ |
| "certified margins" for the searched designs | `sec8` | → "verified margins" ✔ |
| `thm:T9b` as a contribution | `sec1` contribution 1, `sec14` index | **deleted** ✔ |
| companion-comparison table | `sec1` | **deleted** ✔ |
| "inherited from a previously submitted companion paper" | abstract | **deleted** ✔ |
| Pinsker as the operative theorem | `sec3` `thm:T20` | replaced by the exact bound ✔ |
| unspecified `Ψ` | `sec3` | **deleted** ✔ |
| FCAA split | `ROUND_02_JOURNAL_DECISION.md` | marked WITHDRAWN ✔ |
