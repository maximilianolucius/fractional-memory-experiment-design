# Round 6 — Final Novelty Round / Ecological-State Closeout

## Governance

This is the final planned novelty round. Do not launch another broad factorial benchmark. Do not redo the 16 frozen Q1 figures. Do not restore any Round-5 claim removed by the chief audit.

Read first:
- CHIEF_ROUND5_AUDIT.md
- THEOREM_LEDGER_after_R5_CHIEF.md
- NOVELTY_LEDGER_after_R5_CHIEF.md
- chief_round5/repair_summary.json

## Primary objective

Attempt to close the **full ecological-state** finite-latent approximation/testing theorem for the true fractional linearization

\[
G_\alpha(s)=C(s^\alpha I-J(A))^{-1}B,
\]

without using the false factorization

\[
(s^\alpha I-J)^{-1}\equiv(sI-J)^{-1}s^{-\alpha}.
\]

### Preferred route

1. Diagonalize / real-block-decompose J(A) in the certified stable regime.
2. Work with the exact impulse kernel
   \[
   g_\alpha(t)=C\,t^{\alpha-1}E_{\alpha,\alpha}(Jt^\alpha)B.
   \]
3. Construct a real, stable, finite-dimensional rational/latent transfer G_m whose impulse response g_m satisfies a rigorous finite-horizon bound
   \[
   \|g_\alpha-g_m\|_{L^1(0,T)}\le \widehat E^{state}_m.
   \]
   Complex-conjugate exponential pairs / real 2x2 blocks are allowed. The rival must remain a genuinely integer-order finite-state model.
4. Freeze one coherent hierarchy for approximation, testing, and safety. State pole/gain/mass constraints explicitly.
5. Derive the corresponding Gaussian testing bound directly at ecological output level:
   \[
   D_{KL}\le C_{obs}(\widehat E^{state}_m)^2B^2,
   \]
   then a lower bound on minimax testing error.
6. Make the result non-vacuous numerically on at least the focal cells A=0.25 and A=0.30, alpha=0.85, using lightweight validation only.

## Safety interface

Two acceptable outcomes:

### A — preferred
Derive a hierarchy-uniform Strong-Allee outer budget for the SAME full-state latent hierarchy, at least for the declared pulse ray, and combine it with the state-level approximation/testing theorem.

### B — acceptable fallback
If the full-state latent hierarchy does not admit a clean Allee extremal theorem, use only the universal actuator peak cap in the full-state theorem and retain T22 separately as the kernel-level pulse-ray Strong-Allee result. Do not force an invalid unification.

## Optional secondary target

Only if the primary objective closes cleanly: extend T22 from one ray to a finite experimentally implementable cone/dictionary of transient waveforms. Any such result must state the coefficient/peak constraints and prove a true outer L2 bound. Do not claim arbitrary-waveform safety.

## Hard gates

Before integrating a new theorem into the paper, verify:

1. the rival is integer-order and finite-dimensional;
2. the exact focal object is G_alpha(s)=C(s^alpha I-J)^{-1}B;
3. the approximation error is a genuine upper enclosure, not a QUADPACK error estimate;
4. every constructive rival satisfies the declared pole/gain/mass constraints;
5. the same rival hierarchy is used in approximation and testing;
6. any Allee safety bound is for exactly the input class stated;
7. all plotted cells used as “stable ecological” satisfy the Matignon criterion;
8. no lower-bound failure is called discriminability.

## Stop rule

If a rigorous, non-vacuous full ecological-state lift cannot be obtained during this round, stop. Do not invent a new model class solely to make the theorem true. Close the paper around the chief-corrected R5 kernel-level/protocol result and document the state-level lift as the principal limitation/future paper.

## Required artifacts

- ROUND6_RESULTS.md
- ROUND6_PROOF.md
- THEOREM_LEDGER_after_R6.md
- NOVELTY_LEDGER_after_R6.md
- MANUSCRIPT_IMPACT_after_R6.md
- reproducible lightweight checker(s)
- if and only if the theorem passes: integrate it into main.tex and update Figure 18 or add one state-level figure; otherwise no new headline figure.
