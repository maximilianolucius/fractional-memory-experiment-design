# ROUND_01_STATUS_CORRECTIONS — Task R2-A

Every Round-01 claim that inferred an **asymptotic** property from the finite C-1 fits is corrected
below. `Lemma B.1` is preserved as **PROVED**. Files corrected:
`THEOREM_B_COMPLEXITY_LAW.md`, `ROUND_01_DECISION.md`, `RESCUE_CLAIM_EVIDENCE_LEDGER.md`.

**Permitted empirical wording adopted verbatim where needed:**
> Over the tested range `m ≤ 128`, stretched-exponential fits outperform a single algebraic fit for the
> tested orders; the asymptotic class remains unresolved.

---

## Before / after table

| # | Where | Round-01 wording (**before**) | Corrected wording (**after**) | Basis |
|---|---|---|---|---|
| 1 | `THEOREM_B` §3c, `ROUND_01_DECISION` §1 | "Convergence is **sub-exponential but strictly faster than algebraic**" | "Over the tested range `m≤128`, stretched-exponential fits outperform a single algebraic fit for the tested orders; **the asymptotic class remains unresolved** by C-1." | asymptotic class cannot be read off 17 points per order |
| 2 | `THEOREM_B` §3c(2) | "Therefore `m(ε)=O(log^κ(1/ε))` with `κ∈[1,2]`" — presented as following from C-1 | **Deleted as an inference from C-1.** The statement `m(ε)=O(log²(1/ε))` now holds **because it is proved** in `THEOREM_B_ENDPOINT_COMPLEXITY_PROOF.md` (Theorem B.2), independently of any fit | C-1 is verification, not foundation |
| 3 | `THEOREM_B` §3c(3) | "`β=1/2` … is the safest form to *conjecture*, and `κ=2` the safest bound to *assume*" | "`β=1/2` is now **derived**: Theorem B.2 gives `ε ≤ A(α)e^{−π√(α(1−α)m)}`. C-1 **confirms the constant** at `α=1/2` to 0.35 %." | proof replaces conjecture |
| 4 | Earlier `THEOREM_B` (already retracted once in Round 01) | "`ε ≈ 5.58e-2·exp(−0.0865m)`, exponential in `m`, `R²=0.995`" | Retraction stands. Additionally: this local fit is **not** evidence for any exponent; it is superseded by Theorem B.2 | double retraction recorded |
| 5 | `ROUND_01_DECISION` §1 (update block) | "**Added a proved result:** Lemma B.1" | **Unchanged — Lemma B.1 remains PROVED** (scaling bijection; verified to `6e-17`) | proof independent of fits |
| 6 | `THEOREM_D` §2 + `ROUND_01_DECISION` | Ecological error floors "`0.474` (m=64)", "**`0.4997`** (m=128)", "at 128 latent modes safe discrimination is impossible to four decimals" | **RETRACTED as ecological statements.** They were computed from kernel-level `E_m^K` with no operator bridge. With the proved bridge (`C_res≈2.4·10³`) the corresponding ecological floors are `0.0000`, `0.0000`, `0.0482`. The kernel-level numbers survive **only** for the abstract convolution model | `R2_OPERATOR_BRIDGE.md` §B3 |
| 7 | `THEOREM_D` §2 (T23-based rows) | Floors `0.452` (`m=32`, `δ=0.05`), `0.471` (`δ=0.20`) | **Unchanged and valid** — these use `Ê_m^state` from `thm:T23`, which is certified **at response level** and needs no bridge | interval certification |
| 8 | `RESCUE_CLAIM_EVIDENCE_LEDGER` claim 5 | "`m(ε)=O(log^κ(1/ε))`, `κ∈[1,2]` … **EMPIRICAL**" | Split: **claim 5** → "over `m≤128` stretched-exponential fits beat a single algebraic fit; asymptotic class unresolved" (**EMPIRICAL**); **new claim 5d** → Theorem B.2 rate (**PROVED**) | separates measurement from theorem |
| 9 | `RESCUE_CLAIM_EVIDENCE_LEDGER` claim 5c | Kernel-level floors `m=32→0.328`, `m=64→0.474`, `m=128→0.4997` as "CERTIFIED_NUMERICALLY" | Reclassified: valid **only** for the abstract convolution-kernel model; **ecological reading removed** | Gate B |
| 10 | `ROUND_01_DECISION` §3 (novelty item 4) | "The `L¹(0,T)`-with-endpoint variant of the complexity law (measured; provable per §6)" | "…**proved** (Theorem B.2), with constant `c(α)=π√(α(1−α))`; prior art covers `[δ,T]` only" | Task R2-D closed |

## Net effect on the Round-01 verdict

- **Strengthened:** the complexity law moved from *measured* to *proved* (Theorem B.2), and Lemma B.1
  stands as an independent proved result.
- **Weakened:** the headline safety-ceiling numbers at large `m` lose their ecological interpretation;
  only the `thm:T23`-based floors (`m≤32`) survive ecologically.
- **Unchanged:** Theorem A′ and its counterexample; Theorem C′'s derivation and the
  exact-beats-Pinsker finding; the six `REMOVE` claims.
