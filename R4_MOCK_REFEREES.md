# R4-J — Adversarial referee gate

**Result: 0 FATAL, 3 MUST_FIX (2 closed this round, 1 open), 4 MINOR, 8 REJECTED_WITH_REASON.**

Two independent passes, run against the compiled manuscript. As with R4-I, I ran these myself and
know the work, so the useful output is the objections that *survive* — where I could not answer from
the manuscript, or where answering required an experiment I had not done. One such objection forced
a new computation; its result is in §1.1 and is now in the paper.

---

## 1. Mathematical referee

### 1.1 "The searched designs are selected and evaluated on the same operating point. The 0.803 is overfitted." → **MUST_FIX → CLOSED with a new test**

The strongest objection in either pass, and it could not be answered from the manuscript as it
stood. Answering it required an actual held-out comparison, which the validation grid happens to
support: the search ran at `A = 0.25` only, while the 672-cell grid also contains `A = 0.20`.

| design | in-sample `A=0.25` | held-out `A=0.20` | change |
|---|---:|---:|---:|
| SEARCH#0 pwc6 | 0.9463 | 0.8948 | −0.0515 |
| SEARCH#3 pwc6 | 0.8183 | **0.9067** | +0.0883 |
| SEARCH#2 pwc6 | 0.9231 | 0.8669 | −0.0562 |
| prbs (best classical out) | 0.7723 | 0.8365 | +0.0642 |
| multiscale (safe classical) | 0.6917 | 0.4208 | −0.2708 |
| pulse | 0.8448 | 0.4992 | −0.3456 |

Mean drop moving to held-out: **searched designs −0.060, classical families −0.087.** The searched
designs generalise *better* than baselines that were never optimised at all. The best searched
design still leads the best classical design out of sample (0.907 vs 0.837), and its advantage over
the safe classical design is *larger* out of sample (+0.486) than in sample (+0.255), because
multiscale degrades sharply at the lower threshold.

**Objection does not survive.** A paragraph reporting this is now in `sec8`; artifact
`rescue_compute/r3_safe_design_search/r4j_leakage_test.json`.

### 1.2 "The positive-SOE construction and root-exponential order are not yours." → **REJECTED_WITH_REASON**
Agreed, and the manuscript says so in a dedicated attribution block naming McLean, Beylkin–Monzón,
Jiang et al., the quadrature source and the optimality context, followed by "We claim no new
approximation method, no new rate law, and no priority for positive weights." Demoted to a lemma;
removed from every contribution list.

### 1.3 "The quantifier order in the endpoint lemma hides a divergent constant." → **REJECTED_WITH_REASON**
Stated explicitly in the text: the constant diverges as `c → π√(α(1−α))`, the boundary rate is not
established, and attainment/optimality is declared open. The lemma is quantified as
"for every `c < …` there exists `A(α,c)`", never at the boundary.

### 1.4 "You conflate kernel error with response error." → **REJECTED_WITH_REASON**
A dedicated subsection defines the three objects, states `(O3) ≤ (O2)`, and states that no constant
relates (O1) to (O2) — with the measured attenuation range 1.009 → 0.675 as the reason. The text says
kernel-level numbers are never propagated into response-level claims.

### 1.5 "The minimax reduction is under-specified: what exactly are the two hypotheses?" → **REJECTED_WITH_REASON**
The observation model is now fully specified before the theorem: prey channel, `n` samples in `(0,T]`,
additive Gaussian noise with **common** covariance `σ²I` under both hypotheses, means from convolving
each response kernel with the **same** input. `Ψ` is gone; the exact bound `Φ(−d/2)` is primary and
Pinsker is explicitly comparability-only.

### 1.6 "The `m = 64, 128` numbers are presented as certified." → **REJECTED_WITH_REASON**
They are labelled, in the theory section and in the table caption, as high-accuracy floating-point
with a two-mesh quadrature-error estimate, **not** enclosures, and as upper bounds on `Ê_m^state`
(hence conservative floors). The `m ≤ 32` values are separately labelled as interval enclosures.

### 1.7 "The correlated-noise case is ignored: `‖·‖₂ ≤ √n‖·‖_∞` is crude." → **MINOR**
Correct and acknowledged. Samples on a smooth trajectory are not independent, so the effective `n`
is smaller than the nominal one. This makes the reported floors **conservative**, i.e. it works
against us, not for us. Noted in `R3_NONLINEAR_DISCRIMINATION_AUDIT.md` §6; not in the manuscript.
Worth one sentence but not blocking.

### 1.8 "No lower bound on `E_m^+`, so you cannot claim the rate is sharp." → **REJECTED_WITH_REASON**
No sharpness is claimed anywhere. The lemma is an upper bound; the text says the boundary constant
and its optimality are open.

## 2. Computational / nonlinear referee

### 2.1 "Reusing the same seeds across designs is a methodological error." → **REJECTED_WITH_REASON**
It is the opposite: identical seeds make the design comparison paired, removing replicate noise from
the contrast that matters. Independent seeds per design would *add* variance to exactly the quantity
being compared. The seeds are also disclosed in full (`R4_REPRODUCIBILITY_FREEZE.md` §4).

### 2.2 "'Global optimum' language." → **REJECTED_WITH_REASON**
Never claimed. The figure caption and the body both say the search establishes *existence*, "Sobol
sampling with local refinement over the stated families, at a single amplitude and a single `α`", and
"is not a certified global optimum". The absent Stage-3 branch-and-bound is listed as not done.

### 2.3 "The safety criterion assumes you know the true mechanism." → **REJECTED_WITH_REASON**
The opposite: the constraint requires margin `≥ δ` under **all four** candidate mechanisms
simultaneously, which is the correct worst-case criterion for an experimenter who does not know the
truth. The consequence is reported honestly — under that stricter criterion only two of twelve designs
qualify, and the figure encodes exactly this.

### 2.4 "Your safety certificates are mesh-refinement estimates dressed up as proofs." → **REJECTED_WITH_REASON, after a downgrade**
This objection was valid against the Round-03 text and is why the wording was changed. The manuscript
now says "verified a posteriori by mesh refinement with a rigorous inter-node modulus", calls the
`+0.092` a *verified* margin, and reserves "rigorous" for the four trajectories that carry a genuine
validated enclosure with self-consistent error control. The four failures (DDE ×2, Caputo ×2) and
their exact causes are stated in `R4_HEADLINE_SAFETY_CERTIFICATE.md`.

### 2.5 "BIC penalises the latent model for its extra parameters, so its sub-chance recall is an artifact of the decision rule, not evidence of an obstruction." → **MUST_FIX → CLOSED (claim weakened)**

This one has real force and I could not dismiss it. `latent3` recall is 0.207–0.242 across amplitudes,
**at or below the 0.25 chance level**, and BIC's complexity penalty is a plausible cause independent
of any approximation-theoretic obstruction. The paper currently reads the low recall as corroborating
the latent-complexity result, which is over-claiming: the two explanations are not separated.

The theoretical obstruction (Theorem `thm:T20` plus the response-level errors) does **not** depend on
BIC and stands on its own. What is not licensed is using the benchmark's `latent3` recall as
*evidence for* it. Minimum fix: state that the sub-chance recall is consistent with the obstruction
but also with the BIC penalty, and that the two are not separated here. A proper fix would rerun the
decision layer with a penalty-free rule (likelihood ratio at matched dimension, or a Bayes factor
with explicit priors) and report whether the recall moves. *The **minimum fix is applied**: all four
places where the manuscript used that recall as support now state that it is *consistent with* the
obstruction but not evidence for it, and name the BIC penalty as an unseparated competing
explanation. The obstruction is asserted on the analytical grounds alone. The **proper** fix — rerun
the decision layer with a penalty-free rule and report whether the recall moves — is **not done**
and is the one substantive open item for the chief.*

### 2.6 "Class imbalance: the Caputo class spans an `α` grid while the rivals sit at a single parameter value." → **MINOR**
True of the cell counts. It is handled by pooling per-class recall rather than averaging per-cell
accuracy, which is why the reported macro is a per-class mean; the two estimators differ (0.5369 vs
0.4780 at amplitude 0.100) and the manuscript uses the per-class one consistently, matching the frozen
benchmark. Worth a sentence in the methods; not blocking.

### 2.7 "Comparing macro-accuracy across amplitudes is meaningless: lower amplitude is lower SNR, so accuracy must fall." → **MINOR**
Correct, and the manuscript does not use the amplitude comparison to argue about *information*. It uses
it for **safety**: crossing rate stays at 71.4% at half amplitude, and realised gain *rises* to 4.86×
the linear certificate. Those two quantities are not SNR artifacts. The accuracy trend is reported
alongside, and the low-amplitude runs are explicitly labelled linear-certificate diagnostics rather
than a safe benchmark.

### 2.8 "Cross-host reproducibility across different library versions could hide a compensating error." → **REJECTED_WITH_REASON**
Reproduction to four decimal places on macro-accuracy, three per-design accuracies and three crossing
rates simultaneously, under a re-implemented driver on a different host with different `numpy`/`scipy`
versions, is not a plausible coincidence. The version difference is disclosed rather than hidden
(`R4_REPRODUCIBILITY_FREEZE.md` §2) and is what makes the check informative.

### 2.9 "The PECE solver is order ≈1.85 and you run it at N=400 in the benchmark." → **MINOR**
The benchmark grid uses `N = 400`; the verification and enclosure work uses `N` up to 12000. Solver
validation against the exact Mittag-Leffler solution is reported (max error `2.5e−4` at production
resolution). The benchmark's decision statistic is a BIC comparison between models integrated on the
*same* grid, so a common discretisation bias largely cancels. Worth stating that argument explicitly
in the methods; it currently is not.

### 2.10 "Only one `α` for the search, one horizon, one channel pair." → **MUST_FIX → CLOSED as scope**
Now stated in three places: the figure caption, the search subsection's qualifications, and the
limitations paragraph. Combined with §1.1's held-out result, the scope is declared and the
generalisation is measured rather than assumed.

## 3. Summary table

| # | objection | class | status |
|---|---|---|---|
| 1.1 | search overfitting | MUST_FIX | **closed** — held-out test added to `sec8` |
| 2.10 | single-point search scope | MUST_FIX | **closed** — scoped in three places |
| 2.5 | BIC penalty vs latent obstruction not separated | MUST_FIX | **closed by weakening the claim** in four places; penalty-free rerun still open |
| 1.7 | correlated noise / crude `√n` | MINOR | open, conservative direction |
| 2.6 | class imbalance in cell counts | MINOR | open, estimator disclosed |
| 2.7 | cross-amplitude accuracy comparison | MINOR | open, already scoped in text |
| 2.9 | benchmark solver resolution | MINOR | open, argument not written down |
| 1.2–1.6, 1.8, 2.1–2.4, 2.8 | prior art, quantifiers, semantics, minimax, `m=128` status, seeds, global optimum, safety criterion, certificates, reproducibility | REJECTED_WITH_REASON | answerable from the manuscript |

**No FATAL objections. All three MUST_FIX items are closed.** 2.5 was closed the honest way — by
stopping the over-claim rather than by arguing with the objection: the theoretical obstruction stands
without the benchmark recall, so the manuscript no longer offers that recall as evidence for it. What
remains open is one optional strengthening (a penalty-free decision rule) and four MINOR items, none
of which affects a reported number.

**A correction made during this pass, recorded because it nearly entered the manuscript.** While
weakening the 2.5 claim I wrote that "no design exceeds 0.55 recall against the finite-latent rival".
Checking it against the cell-level data gave 0.945. The benchmark's reported figure of 0.475 is the
recall of the *pooled* latent class (`latent1` and `latent3` together), not of `latent3` alone. The
sentence was removed rather than re-quoted, and the manuscript now makes no aggregate claim about
latent recall beyond the frozen benchmark's own number. Worth flagging to the chief: the symbol
`latent3` in the benchmark tables denotes the pooled latent class, which the manuscript does not
currently say.
