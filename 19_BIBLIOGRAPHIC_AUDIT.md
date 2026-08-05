# Bibliographic Audit of `main.pdf`

## Verdict

The bibliography in `main.pdf` cannot be transferred verbatim to the new paper. It mixes valid sources, unresolved sources, incorrect source-to-claim assignments, and references used to support results that were never actually computed. The corrected bibliography is in `17_BIBLIOGRAPHY.md`; the BibTeX database is `references.bib`.

## 1. Valid references that can be retained after normalization

| Draft citation | Correct use | Final key |
|---|---|---|
| Podlubny (1999) | Fractional calculus, Laplace transforms, Mittag–Leffler functions | F02 |
| Ranjith Kumar & Ramesh (2024) | Fractional predator–prey model with explicit delay/refuge mechanisms | E09 |
| Rihan (2021) | Fractional-delay predator–prey context | E08 |
| Saccomani et al. (2003) | General biochemical structural-identifiability context, if specifically needed | Optional; I01–I02 are the main sources |
| Walter & Pronzato (1997) | Parametric identifiability and experiment design | I02 |
| Stan Development Team / Stan | Replace with the peer-reviewed Stan paper | B01 |
| Ahmed et al. (2007) | Early fractional predator–prey application | E06 |
| Javidi & Nyamoradi (2013) | Fractional prey–predator dynamics with harvesting | E07 |
| Kharazmi et al. (2021) | Identifiability/predictability of integer versus fractional models | I06 |
| Beylkin & Monzón | Exponential-sum approximation only | K03–K04 |

## 2. Incorrect source-to-claim assignments

### 2.1 Beylkin–Monzón was used as an ecological dataset source

This is incorrect. Beylkin–Monzón concerns approximation by exponential sums. It provides no microbial predator–prey dataset.

**Replacement:** use E10–E12 for controlled microbial/plankton predator–prey experiments. A particular empirical dataset still requires its own repository or data-paper citation.

### 2.2 Fractional-calculus sources were used for HMC/NUTS

A fractional-calculus monograph does not establish the NUTS algorithm.

**Replacement:** B02 for NUTS and B01 for Stan.

### 2.3 Kharazmi et al. was used for particle MCMC or generic SBI

Kharazmi et al. studies identifiability/predictability with physics-informed neural networks. It is not the source for particle MCMC.

**Replacement:** B03 for particle MCMC. For likelihood-free Bayesian design, use O08 and the broader O06–O09 literature.

### 2.4 Approximation papers were used as though they proved universal exponential convergence on `[0,T]`

The fractional kernel is singular at the origin, and approximation rates depend on the target, interval, tolerance, and norm.

**Replacement:** K02–K06, together with a theorem stated on a precise interval such as `[δ,T]` and an explicit output-error propagation argument.

## 3. Unresolved or rejected bibliographic records

### 3.1 `Ghosh et al. (2024)`

The record stated as *Fractional-order modeling of ecological and epidemiological systems: ambiguities and challenges*, *Sankhya B*, was not matched to a reliable publication record. Remove it unless a DOI or publisher page is supplied.

### 3.2 `Bellmann and Lopez (2013)`

The identity of this source is unresolved. More importantly, the draft’s associated claim—that a nonlinear Caputo model can be treated as pseudo-rational in `s^α` after an informal transform—is not valid as written. Remove both the citation and the claim.

### 3.3 `Mondal and Kar (2026)`

The exact title, venue, DOI, and claimed comparison were not established. Do not cite it in the submitted manuscript without verification.

### 3.4 `Baez and Rodriguez (2020)` and `Heymans and Bauwens (2021)`

The entries are incomplete and were not independently established in this audit. Quarantine them rather than guessing metadata.

## 4. Mathematical claims that cannot be repaired by adding citations

The following statements require rewriting or deletion, not merely a new reference:

1. a nonlinear Laplace transform written as though `L{f(x(t))}=f(X(s))`;
2. a universal time change `τ=t^α/Γ(1+α)` reducing a Caputo system to an ODE;
3. independent Matignon wedges for a coupled component-specific-order system;
4. reduction of distributed-order stability to the mean order;
5. a universal factorization `K_c(α,θ)=K_c^{ODE}(θ)g(α)`;
6. an exact fractional limit cycle born at a Matignon crossing in the standard autonomous class;
7. empirical ELPD, Bayes factors, posterior intervals, or SBC p-values without data/code/results.

The relevant mathematical corrections are in `02_MAIN_DRAFT_MATHEMATICAL_AUDIT.md` and the theorem files.

## 5. Novelty correction forced by the bibliography

The paper must **not** claim to be the first use of optimal experimental design for fractional systems. FOED01–FOED04 already cover fractional-model experiment/input design.

The defensible novelty is narrower and stronger:

> active, safety-constrained discrimination among fractional, delayed, and finite-dimensional latent ecological memory mechanisms, with exact separation results, a finite-horizon approximation barrier, and optimal input/observation design around a certified strong-Allee equilibrium.

## 6. Required empirical citations still missing

Before an empirical section can be written, obtain exact citations for:

- the actual dataset or repository used;
- the measurement protocol and units;
- the intervention apparatus/procedure;
- species-specific biological parameter ranges;
- ethical or biosafety requirements, when applicable.

E10–E12 establish feasibility and precedent; they do not automatically document a new dataset.

## 7. Submission gate

A bibliography-ready manuscript must pass these checks:

- every in-text key exists in `references.bib`;
- every BibTeX entry used in the paper has authors, year, title, venue, and either DOI/ISBN or an explicit no-DOI note;
- no source is used for a claim outside its scope;
- project drafts P01–P03 are replaced by archival citations before journal submission whenever possible;
- no `et al.` appears in the bibliography author field;
- no empirical result is presented solely because it appeared in `main.pdf`.
