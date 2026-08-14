# Round 4 Researcher Prompt — Closure + Safe-Memory Testing Bound

## Governance

Do **not** rewrite the manuscript at the start of this round. First close the Round-3 P0 issues below. Only if the theorem passes should you integrate the mature result into `main.tex` at the end of R4.

Do not launch a broad simulation campaign.

---

## Phase 0 — Mandatory Round-3 closure

### 0.1 Freeze ONE latent hierarchy

The same `L_m` / `K_m` must define all three objects:

1. the competitor in `E_m`;
2. the latent ecological realization used for outputs;
3. the family over which common safety is required.

State explicitly:

- mode-rate domain and how it depends on `m`;
- positivity/sign restrictions;
- coupling / mass / DC-gain normalization;
- ecological prey/predator coordinates;
- input channel;
- observation channel;
- nestedness.

You must choose either:

- expanding nested rate windows compatible with T9b and asymptotic approximation; or
- a permanently fixed rate window, in which case do not claim T9b proves `E_m -> 0` inside that class.

### 0.2 Correct `E_m` terminology

The current deterministic `(ell,L)` search produces a constructive upper error `Ebar_m`, not the exact infimum `E_m`.

Keep

`E_m <= Ebar_m`.

If you need a numerical theorem constant, either derive a tighter analytic upper bound or create a validated numerical `L1` upper certificate for the explicit mixture. Ordinary quadrature may be reported as evidence but not called certified.

### 0.3 Repair one-sided Allee safety

For positive transient protocols use the downward gain

\[
d_M(u_0)=\max_t[-H_{x,M}u_0(t)]_+/\|u_0\|_2.
\]

For common safety use the correct supremum over the SAME rival hierarchy. For signed amplitudes treat the two signs separately.

Also use the shape-specific peak-cap energy bound

\[
\|u\|_2\le u_{\max}\|u_0\|_2/\|u_0\|_\infty,
\]

not merely `sqrt(T) u_max` when discussing a fixed waveform.

### 0.4 Repair the high-frequency theorem proof

Use the uniform Riemann--Lebesgue argument for the finite-horizon convolution operator. Do not use an unproved uniform `O(epsilon^alpha)` rate in the theorem.

### 0.5 Remove the false dictionary-null claim

If finite dictionary spans are discussed, orthonormalize the span before computing restricted singular values. The chief check found positive restricted minima; near-zero values in the submitted code were caused by redundant dictionary columns.

**Phase-0 gate:** write `ROUND4_PHASE0_CLOSURE.md`. If any of 0.1--0.5 is unresolved, STOP and do not claim the R4 theorem.

---

## Phase 1 — Testing theorem

Assume equal-covariance Gaussian observations and use the accepted R1 KL ceiling. Derive a rigorous lower bound on the minimum binary testing error for Caputo versus the best latent alternative in `L_m`.

Use a standard testing inequality with the direction checked carefully. Give at least one of:

- Pinsker-based bound;
- Bretagnolle--Huber / Le Cam-type exponential bound;
- exact equal-covariance Gaussian pairwise error when the adversarial latent competitor is fixed constructively.

The theorem must be expressed in terms of a **valid upper bound** on KL, not an empirical best fit mislabeled as an infimum.

Target structure:

\[
\mathrm{KL}_{\rm safe}^{(m)}
\le C_{\rm obs}\,B_{\rm eff}(A,m,T)^2\,\bar E_m(\alpha,T)^2
\]

followed by

\[
P_e^*\ge \Psi\!\left(C_{\rm obs}B_{\rm eff}^2\bar E_m^2\right).
\]

Separate:

1. universal peak-capped statement;
2. protocol-relative Strong-Allee refinement, only where the corrected Allee bound is actually tighter than the waveform-specific peak cap.

---

## Phase 2 — Non-vacuity gate

Before manuscript integration, demonstrate at least one defensible parameter regime where the final testing lower bound is quantitatively informative.

If T9b is too loose, do NOT hide this. Either:

- produce a tighter validated mixture-error certificate; or
- keep the theorem symbolic and state that numerical certification is deferred to R5.

Do not use ordinary sampled errors as “certified” theorem constants.

---

## Phase 3 — Manuscript integration (only after gates pass)

Only after Phases 0--2 pass:

- update Abstract / Introduction novelty statement;
- promote the coherent `K_m`, `E_m`/`Ebar_m`, and testing theorem;
- add the corrected high-frequency negative result as a scope theorem/remark;
- integrate the Strong-Allee refinement honestly as protocol-relative;
- keep the existing Q1 figure suite unchanged unless a theorem-specific figure is indispensable.

Do not create the final atlas yet; that is Round 5.

---

## Required round outputs

- `ROUND4_PHASE0_CLOSURE.md`
- `ROUND4_RESULTS.md`
- `THEOREM_LEDGER_after_R4.md`
- `NOVELTY_LEDGER_after_R4.md`
- `MANUSCRIPT_IMPACT_after_R4.md`
- proof/check scripts used for lightweight verification
- updated manuscript only if all gates pass
