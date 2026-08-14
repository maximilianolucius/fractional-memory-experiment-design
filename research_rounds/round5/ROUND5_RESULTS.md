# Round 5 Results — Safe Memory-Discrimination Atlas

Date: 2026-08-14
Status: **Phase 0 gates decided (see ROUND5_PHASE0_GATE.md); atlas built and
integrated.**

## Headline results

1. **Gate 0A (closed, preferred route).** The hierarchy-uniform Strong-Allee
   budget exists and is EXACT:
   `d_rob(K_m,u0) = M_T max_{lam} F(lam)/w(lam)` (attained by a single-mode
   kernel), giving `B_Allee(A,m) = rho_eta/d_rob_low` — a theorem-valid,
   m-dependent outer budget over the SAME adversarial class as T20. Sandwich
   enclosures [d_low, d_up] reported (e.g. m=16, A=0.30: [12.51, 15.65]).
2. **Certified crossover:** shape-cap -> Allee binding at A in (0.15, 0.20)
   for every m at alpha=0.85 (more conservative than the 0.32 benchmark
   diagnostic). At A=0.42 the backbone response weakens and B_Allee rises
   again — reported as-is, no monotonicity asserted.
3. **Gate 0B (closed negative).** Irreducible backbone mismatch
   D0(A)=||h_J^alpha - h_J*k_alpha||_1 = 9.11/16.96/24.15 (A=0.25/0.30/0.34),
   m-independent and dominant; constructive full-state errors converge to D0,
   not to 0. The factorized ecological lift is false; the atlas is labeled
   kernel-level theoretical + full-state empirical.
4. **Gate 0C (closed with caveat).** Explicit nested expanding windows
   ell_m=0.025/sqrt(m), L_m=3+0.1 ln m contain all tuned competitors and give
   T9b -> 0, proving E_m -> 0 for THAT hierarchy; the T9b mixtures violate the
   frozen mass bound M_T=9.74 at small m, so the asymptotic claim lives in an
   m-dependent-mass class, separate from the frozen safe class K_m.

## Atlas (theorem-valid quantities only)

Grid: alpha in {0.70, 0.85, 0.95} x A in {0.10..0.42} (9 values) x
m in {4,8,16,32} x sigma in {0.05,0.10,0.15,0.20}; pulse protocol; 432 cells.
Inputs: interval-enclosed Ehat_m^IA (multi-alpha), exact-reduction d_rob_low,
shape cap 0.120, universal cap 0.346.

| alpha | hard@0.25 | moderate@0.10 | inconclusive |
|---|---|---|---|
| 0.70 | 87 | 32 | 25 |
| 0.85 | **144 (all)** | 0 | 0 |
| 0.95 | 65 | 21 | 58 |

- alpha=0.85 (focal): every cell provably hard, P_e >= 0.335 (worst:
  A=0.10, m=4, sigma=0.05) up to 0.499. The safety-impossibility interaction
  is certified across the whole parameter panel.
- alpha=0.70/0.95: hard in the majority of cells; inconclusive cells
  concentrate at (A low, m low, sigma low) where BOTH the approximation error
  (kernel well separated from any mixture) and the safe budget are large —
  exactly where discrimination is genuinely plausible, honestly labeled.
- Binding budget: Allee-binding in 320/432 cells; shape-cap at low A;
  universal cap never binding for pulse.
- Nothing is labeled "provably discriminable" anywhere.

Adversarial checks: Ehat nonincreasing in m (0 violations of 432 checks);
P_e nondecreasing in sigma (0 violations); B_eff deliberately NOT asserted
monotone in A (backbone response J(A) nonmonotone near the stability edge;
the A=0.38->0.42 uptick is real and reported).

## What this buys the paper

The chief's Round-4 condition — "no theorem yet in which fractional
approximation x latent complexity x Strong-Allee safety enter simultaneously"
— is now closed at the kernel level: T20 with the Gate-0A B_Allee(A,m) budget
is a single theorem carrying all three objects over the same hierarchy K_m.
The full ecological-state version remains open (Gate 0B negative) and is
stated as such.

## Files

- compute_round5.py, compute_round5_atlas.py, plot_round5_atlas.py
- round5_results.json, atlas_cells.json
- fig18_safe_discrimination_atlas.pdf/.png (paper/figures/)
- ROUND5_PHASE0_GATE.md, THEOREM_LEDGER_after_R5.md,
  NOVELTY_LEDGER_after_R5.md, MANUSCRIPT_IMPACT_after_R5.md
