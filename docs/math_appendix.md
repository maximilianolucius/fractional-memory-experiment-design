# Mathematical Appendix for Fractional Memory Ecological Models

## Fractional Calculus Fundamentals

### Caputo Fractional Derivative
The Caputo fractional derivative of order α > 0 is defined as:
```
{}_C D_t^α f(t) = 1/Γ(n-α) ∫_0^t (t-τ)^(n-α-1) f^(n)(τ) dτ
```
where n = ⌈α⌉ is the ceiling of α, and Γ is the gamma function.

For 0 < α < 1, this simplifies to:
```
{}_C D_t^α f(t) = 1/Γ(1-α) ∫_0^t (t-τ)^(-α) f'(τ) dτ
```

### Laplace Transform of Caputo Derivative
```
L{_C D_t^α f(t)} = s^α F(s) - ∑_{k=0}^{n-1} s^(α-k-1) f^(k)(0)
```
For 0 < α < 1:
```
L{_C D_t^α f(t)} = s^α F(s) - s^(α-1) f(0)
```

### Mittag-Leffler Function
The two-parameter Mittag-Leffler function is defined as:
```
E_{α,β}(z) = ∑_{k=0}^∞ z^k / Γ(αk + β)
```
Important special cases:
- E_{α,1}(z) = E_α(z) (one-parameter Mittag-Leffler)
- E_{1,1}(z) = e^z (exponential function)
- E_{2,1}(-z^2) = cos(z) (cosine function)

### Solution of Fractional Relaxation Equation
The fractional relaxation equation:
```
{}_C D_t^α y(t) = -λ y(t), \quad y(0) = y_0
```
has solution:
```
y(t) = y_0 E_α(-λ t^α)
```

## Fractional Order Ecological Model

### Dimensionally Consistent Form
The dimensionally consistent Caputo predator-prey model:
```
τ₀^(α-1) {}_C D_t^α z(t) = f(z(t);θ) + Bu(t)
y(t) = Cz(t)
```
where τ₀ is a reference time scale to maintain dimensional consistency.

### Equilibrium Points
For the strong-Allee predator-prey model:
```
f₁(x,y) = rx(1-x/K)(x/A-1) - axy/(1+hx)
f₂(x,y) = eax y/(1+hx) - my
```

The coexistence equilibrium is:
```
x* = m/(a(e-mh))
y* = (1+hx*)r(1-x*/K)(x*/A-1)/a
```

With locked parameters (r=3/2, K=1, a=1, h=1/2, e=4/5, m=2/5):
```
x* = 2/3
y*(A) = 2(2-3A)/(9A)
```

### Jacobian at Equilibrium
The Jacobian matrix J at (x*,y*) is:
```
J = [∂f₁/∂x  ∂f₁/∂y]
    [∂f₂/∂x  ∂f₂/∂y]
```

Which simplifies to:
```
J = [T  -c]
    [d   0]
```
where T, c, and d are functions of the equilibrium point and parameters.

### Transfer Function
The transfer function from input u to output y for the linearized fractional system is:
```
G_α(s) = C (τ₀^α s^α I - J)^(-1) B
```

For the specific case where CB ≠ 0:
```
G_α(s) = (CB) τ₀^(1-α) s^(-α) + O(|s|^(-2α))
```

## Frequency Response Analysis

### Frequency Response Function
Substituting s = iω:
```
G_α(iω) = (CB) τ₀^(1-α) (iω)^(-α) + higher order terms
```

### Magnitude and Phase
```
|G_α(iω)| = |CB| τ₀^(1-α) ω^(-α)
∠G_α(iω) = -(1-α)π/2 + arg(CB)
```

This shows the characteristic constant phase shift of fractional systems.

## Recent Advances (2024)

### Mittag-Leffler Kernel Fractional Derivatives
Recent work has extended fractional derivatives to use Mittag-Leffler kernels:
```
{}_AB D_t^α f(t) = B(α)/(1-α) ∫_0^t E_α[-α/(1-α)(t-τ)^α] f'(τ) dτ
```
where B(α) is a normalization function with B(0)=B(1)=1.

### Distributed Order Fractional Derivatives
Distributed order fractional derivatives:
```
∫_0^1 φ(α) {}_C D_t^α f(t) dα
```
can capture more complex memory effects than single-order fractional derivatives.

### Variable Order Fractional Derivatives
Variable order fractional derivatives where α = α(t):
```
{}_C D_t^α(t) f(t) = 1/Γ(1-α(t)) ∫_0^t (t-τ)^(-α(t)) f'(τ) dτ
```
allow modeling of time-varying memory properties.

## Numerical Methods

### Grünwald-Letnikov Approximation
The Grünwald-Letnikov approximation:
```
{}_C D_t^α f(t) ≈ h^(-α) ∑_{k=0}^{[t/h]} w_k^(α) f(t-kh)
```
where w_k^(α) = (-1)^k Γ(α+1)/(Γ(k+1)Γ(α-k+1))

### Predictor-Corrector Methods
Predictor-corrector methods for fractional differential equations provide improved accuracy over simple discretization schemes.

## Model Discrimination Criteria

### Frequency Domain Discrimination
Fractional systems exhibit constant phase shift in intermediate frequencies, unlike:
- Integer-order systems: phase shifts are integer multiples of -π/2
- Time-delay systems: linear phase shift -ωτ
- Latent state models: rational function approximations

### Time Domain Discrimination
Fractional systems show power-law decay t^(-α), while:
- Exponential decay: e^(-λt)
- Multi-exponential decay: Σ c_i e^(-λ_i t)
- Delayed exponential: e^(-λ(t-τ)) for t>τ

## References
[1] Podlubny, I. (1999). Fractional Differential Equations. Academic Press.
[2] Kilbas, A. A., Srivastava, H. M., & Trujillo, J. J. (2006). Theory and Applications of Fractional Differential Equations. Elsevier.
[3] Magin, R. L. (2010). Fractional Calculus in Bioengineering. Begell House.
[4] Atangana, A., & Baleanu, D. (2016). New fractional derivatives with nonlocal and non-singular kernel. Thermal Science, 20(2), 757-763.
[5] Sousa, J. V. D., & Oliveira, E. C. (2022). Fractional Differential Equations: Theory, Methods and Applications. MDPI.

[6] Ghosh, B., et al. (2024). Fractional-order modeling of ecological and epidemiological systems: ambiguities and challenges. *Sankhya B*.
