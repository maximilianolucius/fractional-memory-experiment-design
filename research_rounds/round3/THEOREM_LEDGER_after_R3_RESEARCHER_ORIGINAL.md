# Theorem Ledger — After Round 3

Date: 2026-08-14

| ID | Claim | Status | Notes |
|---|---|---|---|
| Existing T4–T7 | Exact structural separation from declared finite latent / retarded-delay classes | PROVED IN MANUSCRIPT | Preserve scope. |
| Existing T9a–T9c | No uniform approx at zero / constructive L1 approximation / convolution output bound | PROVED IN MANUSCRIPT | T9b is the certified E_m bound for R4. |
| Existing corollary | Unrestricted latent complexity destroys robust separation for a fixed linearized input | PROVED, FIXED-INPUT | Superseded in scope by R1 (bounded classes). |
| Existing T11/T12 | Linear-Gaussian optimal input / finite-support robust multisine | PROVED IN MANUSCRIPT | Generic OED not novelty center. |
| Existing T16/T17 | Small safe-informative perturbation / strict rectangle invariance | PROVED UNDER STATED ASSUMPTIONS | Benchmark rectangle remains diagnostic only (chief check FAIL). |
| **R1** | Uniform complexity-induced KL collapse over a bounded safe input class | **PROVED IN ROUND-1 NOTES** | Outer energy interface: generic actuator cap (valid) + R3b-pos refinement for transient protocols. |
| **R2a** | `\|\|u\|\|_inf < rho_eta/Gamma_x,T` sufficient Strong-Allee prey-floor certificate (focal Caputo) | **PROVED** | Inner safe ball; eta>0 for strictness. |
| **R2b** | `B_safe <= sqrt(T) rho/Gamma_T` outer bound for full safe class | **REJECTED BY CHIEF AUDIT** | Direction error; preserved as R2a certificate. |
| **R2c** | Common-safe across rivals via shared Jacobian | **REPLACED BY R3b.4** | Robust worst-case over `{ODE,Caputo,DDE,latent1,latent3}` with frozen ecological output. |
| **R3a** | Quantitative E_m(alpha,T) for frozen nested class K_m | **PROVED (constructive + certified)** | K_m frozen (nonneg weights, rates in [1e-3,10], nested); T9b bound certified; envelope rho~0.96 geometric / exp(-0.30 sqrt m) diagnostics (finite window). |
| **R3b-neg** | No Allee-dependent outer energy bound for unrestricted L2 safe class | **PROVED** | High-frequency null direction; sup_{U_safe}\|\|u\|\|_2 = +infinity; numerically verified eps^alpha decay. |
| **R3b-pos** | Coercive outer bound `\|\|u\|\|_2 <= rho_eta/kappa_V^robust` for fixed-shape transient protocols, common-safe across all rivals | **PROVED (linearized)** | kappa_V^inf > 0 for pulse/multiscale; robust worst case = latent3; focal-cell outer 0.3135 (pulse) < cap 0.3464; binding at A=0.30. |
| R4 | Safe-memory testing lower bound for the declared experiment class | OPEN / NEXT (GATE PASSED) | Combine R1 + T9b-certified E_m + interface B.5. Impossibility is protocol-relative (R3b-neg), not absolute. |
| R5 | Safe-memory discrimination atlas | OPEN | After R4 theorem interfaces are frozen. |

## Gate record

End-of-R3 gate (per ROUND3_RESEARCHER_PROMPT.md): **PASS** — condition 1
(quantitative E_m for frozen class) and condition 2 (valid outer bound OR
rigorous negative theorem — both delivered) satisfied. R4 authorized.
