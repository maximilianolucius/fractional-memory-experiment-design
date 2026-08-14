# Novelty Ledger — After Round 3

Date: 2026-08-14

## Unchanged from Round 1

The prior-art collisions (Saligrama 2607.16895 generic safe information;
Ni/Ornik/Chou/Coogan safe active discrimination; Bhattacharya/Cao/Stuart OED
for history-dependent laws; Chaudhary et al. SOE approximation of power-law
kernels) still close the broad claims. SOE approximation rates remain
infrastructure, not novelty.

## Round-3 novelty accounting

**Not novel (infrastructure, correctly attributed):**
- the constructive L1 exponential-sum bound (manuscript T9b, proved in-paper);
- exponential-sum approximation rates (Beylkin-Monzon 2005/2010; Braess-Hackbusch 2005);
- high-frequency attenuation of strictly proper systems (classical);
- coercivity via smallest singular value of a restricted convolution operator (standard).

**Novel (survives stress test):**
1. **The joint object** `sup_{u common-safe} inf_{L in L_m} KL(P_C^u || P_L^u)`
   with a nested latent hierarchy against fractional memory under a Strong-Allee
   barrier (Round-1 hypothesis, unchanged).
2. **Theorem R3b-neg** — the *explicit* negative result that state safety alone
   never bounds input energy for unrestricted inputs (high-frequency null
   direction), proved for the fractional prey channel and verified numerically.
   Prior safe-OED work assumes quadratic safety budgets; nobody we found states
   the obstruction for state-threshold safety.
3. **Theorem R3b-pos** — a *protocol-relative* Allee-dependent outer bound:
   `||u||_2 <= rho_eta/kappa_V^robust` for frozen transient protocols, robust
   over the full rival family with a frozen ecological output. The dependence
   on `rho_eta = x* - (A+eta)` is the ecological signature no generic safe-OED
   result carries.
4. **The repaired interface B.5** — the safe-energy budget that R4 consumes is
   now a min of the actuator cap and the Allee-coercive protocol budget, with
   the crossover computed at the benchmark cells.

## Wording discipline (carried into R4)

- never claim "all safe experiments are information-poor near the threshold"
  (R3b-neg disproves it); claim "every fixed-shape transient protocol budget
  shrinks like rho_eta" (R3b-pos);
- never claim the Caputo gain certifies the rival family (use the robust
  worst case);
- rate diagnostics are finite-window observations, not theorems.
