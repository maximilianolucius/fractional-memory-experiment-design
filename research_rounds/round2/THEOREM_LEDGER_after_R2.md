# Theorem Ledger — after Round 1

| ID | Claim | Status | Notes |
|---|---|---|---|
| Existing T4–T7 | Exact structural separation from the declared finite latent / retarded-delay classes | PROVED IN MANUSCRIPT | Keep original scope; do not broaden to all delays or all latent mechanisms. |
| Existing T9b–T9c | Constructive finite-horizon exponential approximation / convolution output bound | PROVED IN MANUSCRIPT | Approximation method itself is not a novelty claim. |
| Existing corollary | Unrestricted latent complexity destroys robust separation for a fixed linearized input | PROVED, FIXED-INPUT SCOPE | This is weaker than R1. |
| Existing T11/T12 | Linear-Gaussian optimal input and finite-support robust multisine result | PROVED IN MANUSCRIPT | Generic design theory is not the new novelty center. |
| Existing T16/T17 | Existence of small safe-informative perturbation / strict fractional rectangle invariance | PROVED UNDER STATED ASSUMPTIONS | The benchmark rectangle is not automatically a T17-certified invariant set. |
| **R1** | Uniform complexity-induced KL collapse over a bounded safe input class | **PROVED IN ROUND-1 NOTES** | Candidate new contribution. Linear convolution + equal Gaussian covariance. Not yet integrated into manuscript. |
| R2 | Explicit Strong-Allee safe energy/amplitude bound `B_safe(A,alpha,T,rho)` | **PROVED IN ROUND-2 NOTES (linearized, numerically evaluated)** | `B_safe = sqrt(T)·rho/Gamma_T(A,alpha)` with rho = x*−A and Gamma_T the exact Mittag-Leffler impulse-response gain. Validation gate alpha→1 vs scipy expm passed (rel err ~1e-10). Tightens the R1 ceiling by factors 0.12–0.69 (squared) in the primary regime A>=0.25, alpha>=0.85. Also established: the benchmark diagnostic rectangle is structurally non-invariant at any amplitude (3/4 faces point outward with zero input), confirming the chief's wording and motivating the threshold-envelope interface. Nonlinear lift deferred to R3. |
| R3 | Quantitative latent-complexity law for `E_m(alpha,T)` suited to the declared `L_m` class | OPEN / NEXT | Reuse/cite approximation theory; novelty lies in coupling the rate to discrimination, not in rediscovering SOE approximation. Should also scope the nonlinear lift of R2. |
| R4 | Safe-memory testing impossibility / minimum-error lower bound | OPEN | Derive from R1 + R2 + R3 using an appropriate testing inequality. |
| R5 | Certified safe-memory discrimination atlas | OPEN | Computation/certification layer, not a theorem until acceptance rules are frozen. |
