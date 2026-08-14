# Theorem Ledger — Chief audit after Round 2

| ID | Claim | Status | Notes |
|---|---|---|---|
| Existing T4–T7 | Exact structural separation from declared finite latent / retarded-delay classes | PROVED IN MANUSCRIPT | Preserve scope. |
| Existing T9b–T9c | Constructive finite-horizon exponential approximation / convolution output bound | PROVED IN MANUSCRIPT | Approximation method itself not the novelty claim. |
| Existing corollary | Unrestricted latent complexity destroys robust separation for a fixed linearized input | PROVED, FIXED-INPUT | R1 is stronger on bounded input classes. |
| Existing T11/T12 | Linear-Gaussian optimal input / finite-support robust multisine | PROVED IN MANUSCRIPT | Generic OED not novelty center. |
| Existing T16/T17 | Small safe-informative perturbation / strict rectangle invariance | PROVED UNDER STATED ASSUMPTIONS | Benchmark rectangle remains diagnostic only. |
| **R1** | Uniform complexity-induced KL collapse over a bounded safe input class | **PROVED IN ROUND-1 NOTES** | Generic actuator cap gives valid outer energy bound. |
| **R2a** | `||u||_inf < rho_eta/Gamma_x,T` is a sufficient Strong-Allee prey-floor certificate for focal linearized Caputo model | **PROVED** | Inner safe ball. Use `eta>0` for strict safety. Coordinate gain is sharper than vector gain. |
| **R2b** | `B_safe <= sqrt(T) rho/Gamma_T` for the full safe class | **FALSE / REJECTED** | Lemma gives safe-ball inclusion in the opposite direction. Cannot feed this quantity into R1 as an outer bound. |
| **R2c** | Same Gamma certificate is common-safe for ODE/Caputo/DDE/arbitrary latent rivals | **NOT PROVED** | Different propagators; latent class lacks frozen ecological safety-state map/uniform gain. |
| R3a | Quantitative latent-complexity law `E_m(alpha,T)` for frozen nested latent class | OPEN / NEXT | Reuse approximation theory, derive exact applicability to declared class. |
| R3b | Necessary/coercive Strong-Allee outer bound on safe excitation within a frozen implementable input class | OPEN / REQUIRED BEFORE R4 | Likely needs finite waveform/bandwidth/TV restriction plus nonzero coercivity constant. A negative no-bound result without these restrictions is also acceptable and informative. |
| R4 | Safe-memory testing lower bound for all designs in declared safe design class | BLOCKED BY R3b | Combine R1 + R3a + repaired safety outer bound. |
| R5 | Safe-memory discrimination atlas | OPEN | Only after theorem interfaces are frozen. |
