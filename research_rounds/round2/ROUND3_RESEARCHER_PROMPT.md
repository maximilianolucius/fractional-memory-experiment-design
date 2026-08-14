# Round 3 Prompt — Latent Complexity Law + Safety-Interface Repair

Do **not** update the manuscript yet. Work only in `research_rounds/round3/` and update theorem/novelty ledgers.

## Starting point

Round 1 remains valid:

\[
\Delta_{\rm safe}^{(m)}
\le
\tfrac12\|R^{-1/2}S\|^2 B_{\rm safe,m}^2 E_m(\alpha,T)^2,
\]

provided `B_safe,m` is a genuine **outer** energy bound for the safe class.

The chief audit rejected the Round-2 claim `B_safe <= sqrt(T) rho/Gamma_T`: `rho/Gamma_T` defines a sufficient **inner** safe amplitude ball, not an outer bound on all safe inputs. Preserve R2a as a protocol certificate; do not reuse it as a universal impossibility ceiling.

## Track A — Freeze and quantify the latent approximation class

1. Define exactly `L_m` / `K_m`:
   - exponential modes,
   - positivity/sign constraints,
   - admissible rate interval,
   - normalization/coupling bounds,
   - nestedness in `m`,
   - common observed prey/predator output map.
2. Establish or import (with exact theorem/citation hypotheses checked) a quantitative rate/bound for

\[
E_m(\alpha,T)
=\inf_{k_m\in K_m}\|k_\alpha-k_m\|_{L^1(0,T)}.
\]

3. Do not claim novelty for SOE approximation itself. Novelty is its coupling to safe discrimination.
4. Provide constructive constants usable in R4/R5, not only big-O notation.

## Track B — Repair the Strong-Allee safety outer bound

The target is a **necessary** outer bound, not another sufficient inner certificate.

1. Explain/prove why state safety alone does not generally upper-bound input energy for an unrestricted strictly proper stable system (high-frequency/null-direction issue).
2. Freeze an experimentally defensible input class `V` already compatible with the paper (e.g. finite waveform dictionary, bounded frequency band, bounded switching/rate/TV).
3. Define an input-to-prey safety operator `H_x` and seek a coercivity constant

\[
\kappa_V
=
\inf_{u\in V,\ \|u\|_2=1}\|H_xu\|_{\rm safety}.
\]

If `kappa_V>0`, derive the necessary outer bound

\[
\|u\|_2\le \rho/\kappa_V
\]

for the declared symmetric local trust-region safe class, or an appropriate one-sided variant for the prey floor.
4. For robust common safety, define the ecological prey state/output for every rival and take the appropriate worst-case/coercive constant over the candidate family.
5. If no nontrivial outer bound is possible under a scientifically reasonable class, prove that negative result and redesign R4 around the explicit actuator cap rather than hiding the obstruction.

## Mandatory scope guards

- Use `rho_eta = x*-(A+eta)` with `eta>0` for strict Allee safety.
- Do not assert monotonicity of `Gamma_T` in `alpha` from a 12-cell grid.
- Do not claim the focal Caputo gain certifies all rival models.
- Do not integrate R1/R2/R3 into `main.tex` before the end-of-R3 GO/NO-GO gate.

## Required outputs

- `ROUND3_RESULTS.md`
- `THEOREM_LEDGER_after_R3.md`
- `NOVELTY_LEDGER_after_R3.md`
- `MANUSCRIPT_IMPACT_after_R3.md`
- exact citations / theorem-hypothesis audit for the chosen SOE approximation rate
- reproducible lightweight checker(s) for any numerical constants

## End-of-round gate

R4 is allowed only if we have both:

1. a usable quantitative `E_m(alpha,T)` bound for the frozen latent class; and
2. a mathematically valid outer safe-excitation bound for the declared experiment class **or** a rigorous negative theorem showing why the paper must retain only the explicit actuator cap.
