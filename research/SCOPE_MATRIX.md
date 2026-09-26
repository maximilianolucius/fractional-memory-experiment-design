# Scope matrix (directives §23)

| statement | whole family | family + condition | one-param slice | benchmark only | certified box only | numerical only |
|---|---|---|---|---|---|---|
| THM-SEP | ✔ (CB≠0, α irrational) | | | | | |
| LEM-SOE scaling (exact) | ✔ all (α,T) | | | | | |
| LEM-SOE rate | ✔ ∀c<π√(α(1−α)) | | | | | |
| COR-CLOSURE | ✔ | | | | | |
| THM-FLOOR (identity) | ✔ Gaussian common-cov | | | | | |
| CERT-GM32 values | | | | | ✔ (α,A)=(0.85,0.25), m≤32 | |
| CERT-SUR128 values | | | | | ✔ same cell, m≤128 | |
| atlas figure | | | ✔ (α,A,m) grid via floor | | | |
| EMP-FRONTIER | | | | ✔ 6 families, locked ecology | | ✔ |
| EMP-AMPLITUDE | | | | ✔ 3 amplitudes | | ✔ |
| EMP-SEARCH existence | | | | ✔ one amplitude, one α | | ✔ |
| held-out control | | | | ✔ A∈{0.20,0.25} | | ✔ |
| CERT-SAFETY4 | | | | | ✔ 4 named trajectories | |
| CERT-M2 / U_NL | | | | | ✔ (cond. on Γ_B,Γ_R numeric) | |
| pooled-latent recall remark | | | | ✔ | | ✔ |

Promotion guard: nothing in row "benchmark only" appears in the abstract without its
qualifier; the abstract's only unconditional claims are THM-FLOOR + CERT rows and the
existence (not optimality) reading of EMP-SEARCH.
