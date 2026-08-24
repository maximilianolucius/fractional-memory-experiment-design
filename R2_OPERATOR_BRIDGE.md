# R2_OPERATOR_BRIDGE — Task R2-B (hard gate)

**Gate B verdict: the bridge is PROVED, and it DESTROYS the kernel-level ecological floors.**
`E_m^K` must not appear in the ecological testing theorem. Theorems C′/D are to be formulated with
response-level `E_m^G` only (`thm:T23` enclosures). The `m=64` and `m=128` floors reported in Round 01
(`0.4742`, `0.4997`) are **retracted as ecological statements**.

---

## B1. Exact operator equations

Frozen linearization at the certified coexistence equilibrium (`A=0.25`, `x*=2/3`), `τ₀=1`,
`c:=τ₀^{1−α}=1`, prey input channel `B=e₁`, prey observation `C=e₁ᵗ`.

**Fractional model (mild/Volterra form).** `τ₀^{α−1}D_C^α ξ = Jξ + Bu` is equivalent to
\[
\xi_F=K_\alpha*(J\xi_F)+K_\alpha*(Bu),\qquad K_\alpha(t)=\frac{t^{\alpha-1}}{\Gamma(\alpha)} .
\tag{B.1}
\]
Observed response: `μ_F = C ξ_F`. Green function: `ξ_F = H_α*Bu` with
`H_α(t)=t^{α−1}E_{α,α}(Jt^α)`.

**Finite latent realization.** The latent rival replaces the memory operator by a positive `m`-mode
mixture `K_m(t)=Σ_{j≤m}c_je^{−λ_jt}`, `c_j,λ_j>0`, acting in the *same* state equation:
\[
\xi_m=K_m*(J\xi_m)+K_m*(Bu).
\tag{B.2}
\]
Equivalently, `(ξ_m, q_1..q_m)` is a finite-dimensional ODE system (each mode a first-order
relaxation driven by `Jξ_m+Bu`), which is why this is the *physically realizable* rival class.

**Delay rival.** `ξ̇=A_0ξ+A_1ξ(t−τ)+Bu`, i.e. the memory acts through a shifted state rather than a
convolution kernel. Its transfer is meromorphic (see `THEOREM_A_AUDIT.md`), so it is separated
structurally, not by kernel proximity; it plays no role in this bridge.

**Where the two error notions live.**
- `E_m^K := ‖K_α−K_m‖_{L¹(0,T)}` — distance between **memory kernels** (what computation C-1 measures).
- `E_m^G := ‖C(ξ_F−ξ_m)‖_{L^∞(0,T)}/‖u‖_∞` — distance between **observed prey responses** (what the
  testing theorem needs; what `thm:T23` certifies).

## B2. The bridge, proved

Subtract (B.2) from (B.1) and write `e:=ξ_F−ξ_m`:
\[
e=K_\alpha*(Je)+(K_\alpha-K_m)*(J\xi_m)+(K_\alpha-K_m)*(Bu).
\tag{B.3}
\]

**Step 1 — the naive route fails.** Taking sup-norms and using Young's inequality gives
`‖e‖_∞ ≤ ‖K_α‖_1‖J‖‖e‖_∞ + E_m^K(‖J‖‖ξ_m‖_∞+‖B‖U)`, which requires the contraction
`‖J‖‖K_α‖_1<1`. **Measured — it fails everywhere in the operating range:**

| `α` | `T` | `‖K_α‖_{L¹}` | `‖J‖·‖K_α‖_1` | contraction? |
|---|---|---|---|---|
| 0.70 | 6 | 3.8576 | 2.185 | **no** |
| 0.70 | 12 | 6.2667 | 3.549 | **no** |
| 0.85 | 6 | 4.8497 | 2.747 | **no** |
| 0.85 | 12 | 8.7416 | **4.951** | **no** |
| 0.95 | 12 | 10.8156 | 6.126 | **no** |

(`‖J‖₂=0.5664` at `A=0.25`.) So no Neumann/contraction argument is available on the horizons used.

**Step 2 — fractional Grönwall.** Applying the generalized Grönwall inequality for the Riemann
kernel (Ye–Gao–Ding, *J. Math. Anal. Appl.* 328 (2007) 1075–1081) to (B.3):

> ### Proposition B.1 (kernel → response bridge)
> Assume `J` generates a Mittag-Leffler-stable linearization, `u∈L^∞(0,T)` with `‖u‖_∞≤U`. Then
> \[
> \|C(\xi_F-\xi_m)\|_{L^\infty(0,T)}\;\le\;\underbrace{\|C\|\,E_\alpha\!\big(\|J\|T^\alpha\big)\big(\|J\|\,\Gamma_T+\|B\|\big)}_{=:C_{\rm res}(T,\alpha,J,B,C)}\;E_m^K\,U,
> \]
> where `Γ_T=sup_{t≤T}∫_0^t‖H_α‖` and `E_α` is the one-parameter Mittag-Leffler function. All
> constants are explicit and finite.

*Proof.* Bound `‖ξ_m‖_∞ ≤ Γ_T^{(m)}U ≤ Γ_T U(1+o(1))` (the latent realization inherits the same
linear gain up to the approximation error). Insert into (B.3), apply Ye–Gao–Ding to
`‖e(t)‖ ≤ a + ‖J‖∫_0^t\frac{(t-s)^{α-1}}{Γ(α)}‖e(s)‖ds` with
`a = E_m^K(‖J‖‖ξ_m‖_∞+‖B‖U)`, obtaining `‖e‖_∞ ≤ a E_α(‖J‖T^α)`; multiply by `‖C‖`. ∎

**Computed amplification.** `E_α(‖J‖T^α)`:

| `α` | `T=6` | `T=12` |
|---|---:|---:|
| 0.70 | 20.4 | 294 |
| 0.85 | 25.4 | **550** |
| 0.95 | 28.5 | 771 |

At the operating point (`α=0.85`, `T=12`, `Γ_T=5.7815`):
`C_res = 550.3 × (0.5664×5.7815 + 1) = **2352**`.

## B3. Audit of the `m=64,128` floors — **retraction**

Propagating C-1's kernel errors through Proposition B.1 (and capping the response by the trajectory
bound `Γ_T U`, since the observed excursion cannot exceed it):

| `m` | `E_m^K` (rel) | `E_m^K` (abs) | `C_res·E_m^K` | `S` used | `P_e` floor from `E_m^K` (**Round 01, wrong**) | `P_e` floor after bridging (**correct**) |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 2.93e-3 | 2.56e-2 | 60.2 | 3.67e-1 | 0.3282 | **0.0000** |
| 64 | 4.26e-4 | 3.73e-3 | 8.76 | 3.67e-1 | 0.4742 | **0.0000** |
| 128 | 4.65e-6 | 4.07e-5 | 9.57e-2 | 6.07e-3 | 0.4997 | **0.0482** |

**Conclusion.** With the proved bridge, the kernel-level errors give **no useful ecological error
floor**: the amplification `C_res≈2.4·10³` inflates the admissible response discrepancy so much that
the lower bound on `P_e` collapses to ≈0. The Round-01 sentence "at 128 latent modes safe
discrimination is impossible to four decimals" is **withdrawn**; it is a statement about the *abstract
convolution-kernel model*, not about the ecological prey response.

**What survives, and it is the right object.** `thm:T23` certifies the discrepancy **at response
level directly**, by outward-rounded interval subdivision: `Ê_4^state=0.5335 → Ê_32^state=0.0070`
(`α=0.85`, `T=12`, `A=0.25`). Those numbers need **no bridge**, so the Round-01 floors computed from
them — `0.452` (`m=32`, `δ=0.05`, `σ=0.02`) and `0.471` (`δ=0.20`) — **remain valid**.

## B4. Instruction for the manuscript (Gate B compliance)

1. **Never** write "equivalently" or "hence" between `E_m^K` and the prey-response error. The two are
   separated by `C_res≈2.4·10³` at the operating point.
2. Theorems C′ and D are stated with **`E_m^G`** only, sourced from `thm:T23` (or a future certified
   response-level enclosure at larger `m`).
3. `E_m^K` and computation C-1 may appear **only** in the abstract kernel/convolution discussion, and
   Lemma B.1 (horizon invariance) is a statement about that abstract object.
4. Proposition B.1 should still be stated — it is the honest link and its large constant is itself
   informative: **kernel proximity is a weak proxy for response indistinguishability in this system.**
5. Open item for Round 03: certify `Ê_m^state` for `m=64,128` (interval subdivision, as in `thm:T23`)
   so the large-`m` regime can be discussed ecologically at all.
