# R4-A — Prior-art repair and theorem status

**Status: DONE. `thm:T9b` no longer exists in the manuscript. The construction is attributed
to McLean (2018) and demoted to a supporting lemma. Build clean, zero undefined references.**

---

## 1. What changed

| item | before | after |
|---|---|---|
| environment | `\begin{theorem}[Finite-horizon approximation and complexity barrier]`, label `thm:T9b` | `\begin{lemma}[Endpoint-inclusive $L^1$ estimate and exact horizon scaling]`, label `lem:soe` |
| the closure statement | folded into the same theorem | split out as `\begin{corollary}` `cor:closure` |
| attribution | none | explicit block quote naming McLean~\cite{K07}, Beylkin--Monzón~\cite{K03,K04}, Jiang et al.~\cite{K05}, the quadrature source~\cite{K08}, and the optimality context~\cite{K09} |
| proof | absent (statement only) | full proof given, with the quantifier order stated and the boundary case declared open |
| contribution list | "Structural and finite-horizon separation (Theorems T4 and T9b)" as contribution 1 | contribution list rebuilt; a closing paragraph states explicitly that neither the structural separation nor the SOE construction is a contribution |
| references to `thm:T9b` | 11 occurrences across `sec1`, `sec5`, `sec10`, `sec14` | 0 occurrences; each replaced by `cor:closure` or `lem:soe` according to what the sentence actually invokes |

## 2. The attribution as written in the manuscript

> **Attribution.** This construction is prior art. Positive exponential-sum approximation of
> $t^{-\beta}$ by quadrature of an integral representation, including the positivity of the
> weights and the root-exponential order in the number of terms, is due to McLean [K07],
> building on the exponential-sum approximation theory of Beylkin and Monzón [K03, K04]; the
> same construction underlies the fast Caputo evaluation of Jiang et al. [K05]. The quadrature
> estimate we invoke is the analytic-strip trapezoidal bound [K08], and root-exponential order
> is the expected optimal order for an algebraic branch point [K09]. We claim no new
> approximation method, no new rate law, and no priority for positive weights.

Followed by the scoped claim:

> What we add is narrow and technical: the published estimates are stated on a compact interval
> $[\delta,T]$ with $\delta>0$, excluding the singularity at the origin, whereas the
> discrimination argument needs the convolution norm $L^1(0,T)$ *including* $t=0$. The strip
> bound is $t$-integrable there because $\alpha>0$, so no excision is required.

## 3. Statement as it now stands

> **Lemma (endpoint-inclusive $L^1$ estimate and exact horizon scaling).** Let
> $E_m^+(\alpha,T)$ be the least $L^1(0,T)$ error of an $m$-term exponential sum with positive
> weights and rates. Then $E_m^+(\alpha,T)=T^\alpha E_m^+(\alpha,1)$, and for every
> $c<\pi\sqrt{\alpha(1-\alpha)}$ there is $A(\alpha,c)<\infty$ with
> $E_m^+(\alpha,T)\le A(\alpha,c)T^\alpha e^{-c\sqrt m}$. Consequently
> $m(\varepsilon)=O(\log^2(1/\varepsilon))$.

The manuscript then states, in the body text: *"The quantifier order is not cosmetic: the
constant diverges as $c$ approaches $\pi\sqrt{\alpha(1-\alpha)}$, so the boundary rate is not
established, and whether it is attained or optimal is open."*

Forbidden phrasings checked absent from the whole `paper/` tree:

| forbidden | occurrences |
|---|---:|
| "new exponential-sum" / "novel approximation" | 0 |
| "new root-exponential law" | 0 |
| priority language for positive weights | 0 |
| $c=\pi\sqrt{\alpha(1-\alpha)}$ asserted as proved | 0 (stated as a strict upper limit only) |
| FCAA / standalone-paper language | 0 in `paper/`; `ROUND_02_JOURNAL_DECISION.md` carries an explicit WITHDRAWN note |

## 4. Bibliography audit

Three entries added; all three are cited, and all pre-existing relevant entries were already
present and are now used.

| key | reference | DOI | cited in |
|---|---|---|---|
| `K07` | McLean, *Exponential Sum Approximations for $t^{-\beta}$*, in Contemporary Computational Mathematics, Springer 2018, pp. 911–930 | `10.1007/978-3-319-72456-0_40` | `sec3` (attribution), `sec1` (contribution disclaimer), `sec14` (theorem index) |
| `K08` | Trefethen & Weideman, *The Exponentially Convergent Trapezoidal Rule*, SIAM Review 56(3) 2014, 385–458 | `10.1137/130932132` | `sec3` (attribution, and invoked inside the proof) |
| `K09` | Stahl, *Best Uniform Rational Approximation of $x^\alpha$ on $[0,1]$*, Acta Math. 190 2003, 241–306 | `10.1007/BF02392691` | `sec3` (optimality context) |
| `K03`,`K04` | Beylkin & Monzón, ACHA 2005 and 2010 | pre-existing | `sec3`, `sec1` |
| `K05` | Jiang, Zhang, Zhang & Zhao, Commun. Comput. Phys. 21 2017 | pre-existing | `sec3` |

Verification: `bibtex` completes with no warnings; the compiled PDF renders "McLean", "Trefethen",
"Stahl", "Beylkin" and "Jiang" in the reference list; zero undefined citations; zero duplicate keys.

**Note on `ML01`.** The bibliography already contained a McLean entry — *Numerical Evaluation of
Mittag-Leffler Functions*, Calcolo 58 (2021). That is a different paper and is **not** the prior
art at issue. It remains cited where it belongs; `K07` is the 2018 exponential-sum chapter.

## 5. Residual risk

None that I can see for this gate. The one judgement call is that the endpoint-inclusive variant
is recorded at all. It is defensible because the discrimination argument genuinely needs the
$L^1(0,T)$ norm and the cited works genuinely exclude the origin, and it is stated as a lemma
with the technique attributed in the same paragraph. If a referee still objects, the fallback is
to delete the lemma and cite McLean for an $[\delta,T]$ estimate plus a one-line remark that the
endpoint contributes $O(\delta^\alpha)$ — the paper's numbers do not depend on it.
