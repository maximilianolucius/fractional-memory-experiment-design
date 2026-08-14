# Round 1 Results — Safe Discriminability as the New Central Object

Date: 2026-08-14
Status: **GO**

## 1. Round objective

Round 1 does **not** rewrite the manuscript. Its purpose is to fix the novelty boundary after reading the closest 2026 prior art and to identify a mathematically defensible object that the next rounds can develop without rediscovering generic safe experimental-design theory.

The central conclusion is that the paper should not claim novelty for

- optimal experimental design for history-dependent/fractional models,
- safe information maximization under a quadratic budget,
- safe active model discrimination for a finite model list, or
- exponential-sum approximation of power-law kernels.

Those ingredients now have close prior art. The remaining high-value direction is the **interaction between a nested approximation class of latent memory mechanisms and ecological safety**.

## 2. Central object

Let `C_alpha` denote the focal Caputo linearized input-output model, and let `L_m` be a class of latent-state alternatives having at most `m` admissible exponential memory modes. Let `S` be the observation operator and let all compared observation laws have common Gaussian covariance `R > 0`.

For a family of candidate models `M`, define the robust common-safe input class

\[
\mathcal U_{\mathrm{safe}}(\mathfrak M,\mathcal S,T)
:=
\left\{u:
 z_M^u(t)\in\mathcal S
 \ \forall M\in\mathfrak M,\ \forall t\in[0,T]
\right\}.
\]

For the Caputo model versus latent complexity `m`, define

\[
\Delta_{\mathrm{safe}}^{(m)}
:=
\sup_{u\in\mathcal U_{\mathrm{safe},m}}
\inf_{L\in\mathcal L_m}
D_{\mathrm{KL}}\!\left(P_{C_\alpha}^{u}\,\|\,P_L^{u}\right),
\]

where

\[
\mathcal U_{\mathrm{safe},m}
=
\mathcal U_{\mathrm{safe}}(\{C_\alpha\}\cup\mathcal L_m,\mathcal S,T).
\]

This quantity is deliberately different from a generic safe-information objective: the rival class itself becomes increasingly capable of approximating the fractional law as `m` grows.

## 3. New Round-1 theorem candidate

### Theorem R1 — Uniform complexity-induced collapse over a safe input class

Let `k_alpha in L^1(0,T)` be the fractional convolution kernel and let `K_m subset L^1(0,T)` be an admissible latent-kernel class. Suppose the observed linear response under kernel `k` and input `u` is

\[
Y_k^u = S(k*u)+\varepsilon,
\qquad
\varepsilon\sim\mathcal N(0,R),
\]

where

\[
S:L^2(0,T)\to\mathbb R^q
\]

is bounded and `R` is positive definite. Define

\[
E_m(\alpha,T)
:=
\inf_{k_m\in\mathcal K_m}
\|k_\alpha-k_m\|_{L^1(0,T)}.
\]

Assume

\[
B_{\mathrm{safe},m}
:=
\sup_{u\in\mathcal U_{\mathrm{safe},m}}
\|u\|_{L^2(0,T)}<\infty.
\]

Then

\[
\boxed{
\Delta_{\mathrm{safe}}^{(m)}
\le
\frac12
\|R^{-1/2}S\|_{L^2\to\mathbb R^q}^{2}
B_{\mathrm{safe},m}^{2}
E_m(\alpha,T)^2.
}
\]

If every admissible input also satisfies `||u||_infty <= u_max`, then

\[
B_{\mathrm{safe},m}\le \sqrt{T}\,u_{\max},
\]

hence

\[
\boxed{
\Delta_{\mathrm{safe}}^{(m)}
\le
\frac{T u_{\max}^{2}}{2}
\|R^{-1/2}S\|^{2}
E_m(\alpha,T)^2.
}
\]

If the latent classes are nested,

\[
\mathcal K_m\subseteq\mathcal K_{m+1},
\]

and the common-safe classes are correspondingly nested,

\[
\mathcal U_{\mathrm{safe},m+1}
\subseteq
\mathcal U_{\mathrm{safe},m},
\]

then `Delta_safe^(m)` is non-increasing in `m`. In particular, if `E_m(alpha,T) -> 0` and the safe energy bounds remain uniformly bounded, then

\[
\boxed{
\Delta_{\mathrm{safe}}^{(m)}\to0
}
\]

**uniformly over all safe experiments**, not merely for one fixed input.

### Proof

For any fixed admissible input `u` and latent kernel `k_m`, equal-covariance Gaussian laws satisfy

\[
D_{\mathrm{KL}}(P_{C_\alpha}^{u}\|P_{k_m}^{u})
=
\frac12
\left\|
R^{-1/2}S\big((k_\alpha-k_m)*u\big)
\right\|_2^2.
\]

By boundedness of `S`,

\[
D_{\mathrm{KL}}
\le
\frac12
\|R^{-1/2}S\|^2
\|(k_\alpha-k_m)*u\|_{L^2}^2.
\]

Young's convolution inequality `L^1 * L^2 -> L^2` gives

\[
\|(k_\alpha-k_m)*u\|_{L^2}
\le
\|k_\alpha-k_m\|_{L^1}\,\|u\|_{L^2}.
\]

For arbitrary `epsilon > 0`, choose `k_m^(epsilon)` with

\[
\|k_\alpha-k_m^{(\epsilon)}\|_{L^1}
\le E_m+\epsilon.
\]

This single competitor is admissible in the inner infimum for every `u`, so

\[
\inf_{k_m\in\mathcal K_m}D_{\mathrm{KL}}
\le
\frac12\|R^{-1/2}S\|^2(E_m+\epsilon)^2\|u\|_{L^2}^2.
\]

Take the supremum over the safe class, then let `epsilon -> 0`. This proves the bound. The amplitude-budget version follows from

\[
\|u\|_2^2\le T\|u\|_\infty^2.
\]

For nested latent and common-safe classes, increasing `m` enlarges the set in the inner infimum and cannot enlarge the set in the outer supremum, hence `Delta_safe^(m+1) <= Delta_safe^(m)`. The limit statement follows from the displayed upper bound.

## 4. Why this matters relative to the current manuscript

The manuscript's current finite-horizon impossibility statement is explicitly restricted to a **fixed input**. The result above upgrades the mechanism to a **uniform statement over an entire safe input class** provided that class has bounded energy.

That is precisely the bridge needed for the planned sequence:

\[
\text{latent approximation complexity}
\to
\text{uniform safe KL ceiling}
\to
\text{testing lower bound}
\to
\text{safe-memory discrimination atlas}.
\]

The Strong-Allee geometry has not yet entered quantitatively. Round 2 should replace the generic `B_safe` interface by a rigorously derived ecological bound depending on the safety margin and model parameters.

## 5. Round-1 limits

This theorem is intentionally scoped.

- It is a **linear convolution / Gaussian observation** result.
- It does not yet prove the analogous statement for the full nonlinear Caputo predator-prey map.
- It assumes a declared latent class `K_m`; positivity, admissible rate ranges, coupling bounds, and nestedness must be frozen before Round 2/3.
- It gives an upper bound on robust KL, not yet a lower bound on classification error.
- It does not claim a new exponential-sum approximation rate; `E_m` should import the strongest appropriate approximation result from the numerical-analysis literature.
- `B_safe` is only an interface in Round 1. The ecological derivation belongs to Round 2.

## 6. GO / NO-GO decision

**GO.** The novelty program survives the literature stress test only after narrowing its center from generic safe OED to **safe discrimination against an approximation hierarchy of memory laws**.

The next round should attack exactly one problem:

> Derive a rigorous Strong-Allee-dependent safe excitation/energy bound `B_safe(A, alpha, T, rho, ...)` that can be inserted into Theorem R1.

Do not re-derive the generalized-Rayleigh safe-information theorem of arXiv:2607.16895.
