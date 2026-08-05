# Worked Ecological Designs

## Design A — stability-verdict experiment at the certified baseline

### Parameters

\[
A=0.3,
\qquad \alpha=0.9,
\qquad \alpha^*(0.3)\approx0.969012276.
\]

The Caputo model is locally stable, whereas the integer-order model with the same Jacobian is unstable.

### Intervention

Apply a small collocated prey or predator pulse, with amplitude selected by the safety bound in `12_SAFE_EXPERIMENT_DESIGN.md`.

### Measurements

- high-rate measurement of the perturbed species immediately after the pulse;
- both species during the recovery window;
- enough duration to distinguish algebraic decay from growing/undamped oscillation.

### Utility

The models differ qualitatively in local stability. This can produce high information but also creates the greatest risk that the unstable alternative leaves the local regime. Use it as a stress-test design, not the sole benchmark.

## Design B — fair stable frequency-response benchmark

Choose

\[
A=\frac14.
\]

Then

\[
J=\begin{pmatrix}-1/8&-1/2\\1/2&0\end{pmatrix},
\]

and the ODE and Caputo alternatives are locally stable.

For \(\tau_0=1\), \(\alpha=0.9\), and the same \(J\), direct numerical maximization of

\[
|G_{0.9}(i\omega)-G_1(i\omega)|^2
\]

for each single input/output channel gives a broad optimum near

\[
\boxed{\omega\tau_0\approx0.49.}
\]

This value is a worked numerical result, not a universal constant. It should be recomputed for every parameter posterior and actuator band.

### Recommended waveform

Use a multisine containing:

- a component near \(0.5/\tau_0\);
- a lower-frequency component probing static/recovery behavior;
- a higher-frequency component probing the fractional \(-\alpha\pi/2\) phase and \(\omega^{-\alpha}\) decay.

The exact frequencies and weights should solve the maximin spectral program.

## Design C — repeated-pulse memory-shape experiment

Let pulse times be logarithmically spaced:

\[
t_k=t_0q^k,
\qquad q>1.
\]

This probes the kernel over multiple decades. Optimize \(q\), amplitudes, and signs rather than selecting them heuristically.

### Rationale

A single recovery curve can be matched by a small latent model. Repeated pulses at noncommensurate spacings test superposition across several memory ages and make a low-dimensional exponential approximation less flexible.

## Design D — latent-environment disambiguation

Use the augmented model

\[
\dot\xi=J\xi+gz+Bu,
\qquad \dot z=-\lambda z+\gamma u.
\]

Calculate

\[
\eta_C(\lambda)=|C(J+\lambda I)^{-1}g|.
\]

- If \(\eta_C\) is large, the latent mode is visible in population measurements.
- If \(\eta_C\) is small, measure an environmental proxy directly or change the output channel.

This turns “measure environmental covariates” into a quantitative channel-selection rule.

## Design E — safe adaptive protocol near the Allee threshold

1. choose \(x_L>A\) and a safety probability \(1-\delta_s\);
2. begin with a small positive or predator-channel pulse;
3. update model and parameter posteriors;
4. solve the next-step information problem under the chance constraint;
5. prohibit negative prey pulses unless the robust lower-face inequality remains satisfied;
6. stop if no safe design reaches the minimum expected KL/MI.

## Minimum simulation matrix

| Factor | Levels |
|---|---|
| True model | ODE, Caputo, DDE, latent-1, latent-3 |
| \(A\) | 0.25, 0.30, 0.40 |
| \(\alpha\) | 0.70, 0.85, 0.95 |
| observation | prey, predator, both, both+environment |
| input | pulse, optimized sinusoid, robust multisine, adaptive |
| SNR | high, medium, low |
| horizon | short, medium, long |
| latent dimension cap | 1, 3, 6 |

The latent-dimension cap must be explicit because discrimination against unrestricted \(m\) is ill-posed.
