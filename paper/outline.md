# Paper Outline: Optimal Excitation for Distinguishing Fractional, Delayed, and Latent Ecological Memory

## Section 1: Introduction and falsifiable memory question
- **Claim**: The problem of distinguishing fractional, delayed, and latent ecological memory is well-posed only when complexity restrictions (finite latent dimension) are imposed; otherwise, the finite-horizon discrimination problem is ill-posed due to the no-free-lunch theorem.
- **Evidence**: Theorem T10 (no-free-lunch result) and the MVP setup with fixed maximum latent dimension m (IDEA.md section 4, source_pack/README.md).
- **Claim Type**: Inference (based on theorem T10).
- **Claim State**: DRAFTING (requires no simulation, permitted after analytical work alone).

## Section 2: Certified strong-Allee ecological backbone
- **Claim**: The predator-prey strong-Allee model from the validated literature provides a certified ecological nonlinear dynamics that serves as the digital twin for our study.
- **Evidence**: source_pack/04_EXACT_STRONG_ALLEE_BASELINE.md and the validated predator-prey model cited in IDEA.md section 1.
- **Claim Type**: Fact (based on certified model).
- **Claim State**: DRAFTING (requires no simulation, permitted after analytical work alone).

## Section 3: Dimensionally consistent controlled memory models
- **Claim**: We define four competing models with a common fractional order α, two input channels (prey/predator), and three observation regimes: M_ODE (integer-order), M_Caputo (fractional derivative), M_DDE (discrete delay), M_latent,m (finite latent dimension with fixed maximum m).
- **Evidence**: source_pack/03_DIMENSIONALLY_CONSISTENT_CONTROLLED_MODEL.md and source_pack/04_EXACT_STRONG_ALLEE_BASELINE.md.
- **Claim Type**: Fact (model definitions).
- **Claim State**: DRAFTING (requires no simulation, permitted after analytical work alone).

## Section 4: Exact linearization, transfer functions, and channels
- **Claim**: Linearization around the coexistence equilibrium yields exact Jacobian matrices, transfer functions, and input/output channels for each model; the Jacobian and Matignon stability boundary are given analytically (T1, T2).
- **Evidence**: Theorem T1 (exact coexistence equilibrium and Jacobian), Theorem T2 (exact T(A), D(A), discriminant, α*(A)), and source_pack/05_CONTROLLABILITY_OBSERVABILITY_AND_CHANNELS.md.
- **Claim Type**: Fact (exact analytical results).
- **Claim State**: DRAFTING (requires no simulation, permitted after analytical work alone).

## Section 5: Structural separation from finite latent and delay models
- **Claim**: The Caputo fractional transfer function is not equivalent to any finite-dimensional integer-order latent-state transfer function nor to any finite-dimensional delay transfer function under a direct input–output channel (structural non-equivalence).
- **Evidence**: Theorem T4 (Caputo ≠ rational finite-dimensional) and Theorem T5 (Caputo ≠ finite DDE).
- **Claim Type**: Fact (proved non-equivalence).
- **Claim State**: DRAFTING (requires no simulation, permitted after analytical work alone).

## Section 6: Finite-horizon exponential approximation and impossibility barrier
- **Claim**: The fractional kernel admits an exact continuous exponential mixture representation (T7) and a constructive finite exponential-sum approximation with explicit L¹ error bound (T9); however, if the latent dimension is unrestricted, finite-horizon discrimination becomes impossible below any noise floor (T10).
- **Evidence**: Theorem T7 (exact continuum exponential representation), Theorem T9 (constructive finite-horizon L¹ approximation), Theorem T10 (unrestricted-latent no-free-lunch).
- **Claim Type**: Mixture of fact (T7, T9) and impossibility result (T10).
- **Claim State**: DRAFTING (requires no simulation, permitted after analytical work alone).

## Section 7: Optimal input and observation design
- **Claim**: For fixed linear-Gaussian models, the pairwise optimal input under an energy constraint is the principal singular vector of the difference operator (T11); the optimal sampling times for two simple Gaussian hypotheses are given (T13); and the optimal frequency-domain input for fixed linear models is given (T12).
- **Evidence**: Theorem T11 (pairwise energy-optimal input), Theorem T12 (robust spectral design has finite support), Theorem T13 (optimal pairwise sampling schedule).
- **Claim Type**: Fact (proved optimality results).
- **Claim State**: DRAFTING (requires no simulation, permitted after analytical work alone).

## Section 8: Safety-constrained design
- **Claim**: Under explicit interior-margin and local-separation assumptions, there exists a nonzero safe and informative perturbation (T16); furthermore, sufficient inward-pointing inequalities define a safe invariant rectangle in the state space (T17).
- **Evidence**: Theorem T16 (existence of a safe informative input) and Theorem T17 (inward-pointing safe rectangle).
- **Claim Type**: Fact (proved existence (T16) and sufficient conditions (T17).
- **Claim State**: DRAFTING (requires no simulation, permitted after analytical work alone).

## Section 9: Nonlinear Bayesian implementation
- **Claim**: For the full nonlinear, partially observed, stochastic, multi-model Bayesian problem, the optimal experiment design can be approximated via nonlinear Bayesian expected information gain, posterior-averaged safety, and adaptive experiments (algorithmic specification).
- **Evidence**: source_pack/13_NONLINEAR_BAYESIAN_EXTENSION.md (rigorous computational extension).
- **Claim Type**: Algorithmic specification (requires computation, not yet proven in closed form).
- **Claim State**: DRAFTING (requires simulation or algorithmic implementation, permitted after analytical work plus simulation validation).

## Section 10: Simulation benchmark
- **Claim**: A reproducible simulation benchmark validates the analytical results and compares the performance of various excitation waveforms under a common energy budget, using the validated digital twin.
- **Evidence**: source_pack/16_IMPLEMENTATION_AND_VALIDATION_SPEC.md (implementation contract) and the validation specs therein.
- **Claim Type**: Fact (based on simulation that passes validation gates).
- **Claim State**: DRAFTING (requires running the simulation benchmark and verifying it passes the gates of source_pack/16_*).

## Section 11: Prospective microcosm protocol or calibrated digital twin
- **Claim**: The paper provides an implementable prospective laboratory protocol (or a calibrated digital twin) for applying the optimal excitation design to real ecological systems, including safety checks and observability recommendations.
- **Evidence**: source_pack/14_WORKED_ECOLOGICAL_DESIGNS.md (concrete protocols for the certified parameter slice) and source_pack/20_RELATED_WORK_POSITIONING.md.
- **Claim Type**: Fact (based on worked designs) and prospective protocol.
- **Claim State**: DRAFTING (requires worked designs, permitted after analytical work plus validation).

## Section 12: Discussion and limitations
- **Claim**: We discuss the limitations of our approach, including the reliance on the linearized model for optimality results, the gap between the linear Bayesian design and the full nonlinear Bayesian solution, and the assumptions required for safety and informativity.
- **Evidence**: The paper's own analysis and the assumptions stated in theorems T16 and T17.
- **Claim Type**: Reflection (based on the paper's contributions and assumptions).
- **Claim State**: DRAFTING (requires writing after all sections are drafted).

## Section 13: Conclusion
- **Claim**: We have established a rigorous framework for optimal experimental design to distinguish fractional, delayed, and latent ecological memory, combining exact linearized results, a simulation benchmark, and a practical protocol.
- **Evidence**: The cumulative results of the paper (theorems T1-T17, simulation benchmark, worked designs).
- **Claim Type**: Summary (based on the paper's contributions).
- **Claim State**: DRAFTING (requires writing after all sections are drafted).

## Section 14: Proof appendices
- **Claim**: Appendices contain detailed proofs of theorems T1-T17 and derivations of corollaries.
- **Evidence**: source_pack/03_*.md through 14_*.md (detailed proofs and derivations).
- **Claim Type**: Fact (proofs from the source pack).
- **Claim State**: DRAFTING (requires copying/adapting proofs from the source pack, permitted after analytical work alone).