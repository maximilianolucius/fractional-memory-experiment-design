# Sample Complexity and Error Probability

## 1. Two simple Gaussian models

Suppose

\[
Y\mid M_i\sim\mathcal N(\mu_i,R),
\qquad i=1,2,
\]

with equal prior probabilities. Define the squared Mahalanobis separation

\[
d^2=(\mu_1-\mu_2)^\top R^{-1}(\mu_1-\mu_2).
\]

The KL divergence is

\[
D_{\mathrm{KL}}(M_1\|M_2)=\frac{d^2}{2}.
\]

## Theorem 1 — exact optimal classification error

The Bayes-optimal error probability is

\[
\boxed{
P_e^*=\Phi\left(-\frac d2\right)
=\Phi\left(-\sqrt{\frac{D_{\mathrm{KL}}}{2}}\right),
}
\tag{1}
\]

where \(\Phi\) is the standard normal distribution function.

### Proof

The log-likelihood ratio is affine in \(Y\). Projecting onto the normalized discriminant direction reduces the problem to two univariate normals with equal variance and means separated by \(d\). The optimal threshold is the midpoint, giving (1). ∎

## Theorem 2 — independent replicate requirement

For \(N\) independent identical experiments, the total KL divergence is \(ND_1\) and

\[
P_{e,N}^*=\Phi\left(-\sqrt{\frac{ND_1}{2}}\right).
\]

To guarantee \(P_{e,N}^*\le\delta<1/2\), it is necessary and sufficient that

\[
\boxed{
N\ge
\frac{2[\Phi^{-1}(1-\delta)]^2}{D_1}.
}
\tag{2}
\]

Round the right-hand side upward to the next integer.

## 2. Independent sampled time points

If

\[
y_k=\mu_i(t_k)+\varepsilon_k,
\qquad \varepsilon_k\sim\mathcal N(0,R_k)
\]

independently, then

\[
D_{12}(d)=\frac12\sum_k
\delta\mu(t_k)^\top R_k^{-1}\delta\mu(t_k),
\]

where \(\delta\mu=\mu_1-\mu_2\). Substitution into (1) converts an experimental design directly into a predicted simple-hypothesis error probability.

## 3. Horizon requirement from a KL rate

If repeated cycles or a stationary experiment accumulate KL approximately at rate \(\dot D>0\), so that \(D(T)\approx T\dot D\), then the error target \(\delta\) requires

\[
\boxed{
T\gtrsim
\frac{2[\Phi^{-1}(1-\delta)]^2}{\dot D}.
}
\tag{3}
\]

This is the clean sample-horizon quantity to report in simulation studies.

## 4. Composite-model caution

Equations (1)–(3) are exact for fixed means and common covariance. When parameters are unknown:

- replacing each model by its best-fitting parameter value gives an optimistic generalized likelihood ratio;
- integrating parameters gives mixture distributions with no general closed-form error;
- minimax design should use the smallest separation over admissible parameters;
- Bayesian design should average over the prior/posterior and report prior sensitivity.

The exact simple-model formula remains a benchmark and a lower-level unit test for the numerical Bayesian pipeline.
