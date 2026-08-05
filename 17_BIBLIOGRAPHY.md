# Verified Bibliography for the Paper

## Scope and editorial rule

This bibliography is the reference backbone for the proposed paper

> **Optimal Excitation for Distinguishing Fractional, Delayed, and Latent Ecological Memory**.

Only references with traceable bibliographic metadata are included in the manuscript-ready list. A citation must support the exact claim for which it is used. In particular:

- fractional-calculus sources must not be used as references for HMC/NUTS, particle MCMC, simulation-based inference, or ecological datasets;
- exponential-sum papers support approximation algorithms and norm-specific error statements, not a universal claim of observational equivalence without a declared interval and norm;
- stability of a nonlinear Caputo equilibrium must cite both the sector condition and a valid nonlinear linearization result;
- model-discrimination design must be distinguished from parameter-estimation design;
- the two uploaded predecessor papers are project sources, not substitutes for external literature.

The machine-readable companion is `references.bib`. The claim-by-claim placement is in `18_CITATION_MAP.md`; removed and replaced citations from `main.pdf` are documented in `19_BIBLIOGRAPHIC_AUDIT.md`.

---

## A. Fractional calculus, well-posedness, and stability

### [F01] Caputo derivative

Caputo, M. (1967). Linear models of dissipation whose Q is almost frequency independent—II. *Geophysical Journal International*, **13**(5), 529–539. DOI: `10.1111/j.1365-246X.1967.tb02303.x`.

**Use:** historical definition and interpretation of the Caputo operator. Do not use as the sole source for modern stability or numerical claims.

### [F02] Standard fractional-calculus monograph

Podlubny, I. (1999). *Fractional Differential Equations*. Mathematics in Science and Engineering, Vol. 198. Academic Press. ISBN: `978-0-12-558840-9`.

**Use:** Laplace transforms, Mittag–Leffler solutions, scalar fractional equations, and general notation.

### [F03] Rigorous FDE analysis

Diethelm, K. (2010). *The Analysis of Fractional Differential Equations: An Application-Oriented Exposition Using Differential Operators of Caputo Type*. Lecture Notes in Mathematics, Vol. 2004. Springer. DOI: `10.1007/978-3-642-14574-2`.

**Use:** existence, uniqueness, comparison arguments, numerical analysis, and Caputo initial-value problems.

### [F04] General reference work

Kilbas, A. A., Srivastava, H. M., & Trujillo, J. J. (2006). *Theory and Applications of Fractional Differential Equations*. North-Holland Mathematics Studies, Vol. 204. Elsevier. ISBN: `978-0-444-51832-3`.

**Use:** operator identities and Mittag–Leffler functions.

### [F05] Matignon sector condition

Matignon, D. (1996). Stability results for fractional differential equations with applications to control processing. In *Computational Engineering in Systems Applications*, Vol. 2, pp. 963–968. IMACS/IEEE-SMC, Lille, France.

**Use:** the commensurate linear-sector condition

\[
|\arg \lambda_j|>\frac{\alpha\pi}{2}.
\]

### [F06] Nonlinear linearization theorem

Cong, N. D., Doan, T. S., Siegmund, S., & Tuan, H. T. (2016). Linearized asymptotic stability for fractional differential equations. *Electronic Journal of Qualitative Theory of Differential Equations*, **2016**(39), 1–13. DOI: `10.14232/ejqtde.2016.1.39`.

**Use:** transferring asymptotic stability from a valid linearization to the nonlinear Caputo system under the theorem’s hypotheses.

### [F07] Fractional linearization

Li, C., & Ma, Y. (2013). Fractional dynamical system and its linearization theorem. *Nonlinear Dynamics*, **71**(4), 621–633. DOI: `10.1007/s11071-012-0601-1`.

**Use:** nonlinear local analysis and the conditions under which Jacobian-based reasoning is legitimate.

### [F08] Mittag–Leffler stability

Li, Y., Chen, Y. Q., & Podlubny, I. (2009). Mittag–Leffler stability of fractional order nonlinear dynamic systems. *Automatica*, **45**(8), 1965–1969. DOI: `10.1016/j.automatica.2009.04.018`.

**Use:** Mittag–Leffler stability and fractional Lyapunov terminology.

### [F09] No exact periodic solutions

Tavazoei, M. S., & Haeri, M. (2009). A proof for non-existence of periodic solutions in time invariant fractional order systems. *Automatica*, **45**(8), 1886–1890. DOI: `10.1016/j.automatica.2009.04.001`.

**Use:** excluding exact nonconstant periodic solutions in the standard autonomous fractional class covered by the paper. State the hypotheses; do not extend the conclusion to forced, variable-order, reset, or hybrid systems without proof.

### [F10] Two-dimensional/multi-order stability review

Brandibur, O., Garrappa, R., & Kaslik, E. (2021). Stability of systems of fractional-order differential equations with Caputo derivatives. *Mathematics*, **9**(8), 914. DOI: `10.3390/math9080914`.

**Use:** exact stability regions for low-dimensional Caputo systems and warning against applying a scalar Matignon rule independently to unrelated component orders.

### [F11] Fractional Grönwall inequality

Ye, H., Gao, J., & Ding, Y. (2007). A generalized Grönwall inequality and its application to a fractional differential equation. *Journal of Mathematical Analysis and Applications*, **328**(2), 1075–1081. DOI: `10.1016/j.jmaa.2006.05.061`.

**Use:** perturbation bounds and continuous dependence estimates.

---

## B. Memory kernels, diffusive representations, and fast solvers

### [K01] Convolution quadrature / discretized fractional calculus

Lubich, C. (1986). Discretized fractional calculus. *SIAM Journal on Mathematical Analysis*, **17**(3), 704–719. DOI: `10.1137/0517050`.

**Use:** numerical fractional operators and convolution quadrature foundations.

### [K02] Diffusive representation

Montseny, G. (1998). Diffusive representation of pseudo-differential time-operators. *ESAIM: Proceedings*, **5**, 159–175. DOI: `10.1051/proc:1998005`.

**Use:** continuum-of-exponentials realization of hereditary operators.

### [K03] Exponential-sum construction I

Beylkin, G., & Monzón, L. (2005). On approximation of functions by exponential sums. *Applied and Computational Harmonic Analysis*, **19**(1), 17–48. DOI: `10.1016/j.acha.2005.01.003`.

**Use:** constructive approximation by exponential sums.

### [K04] Exponential-sum construction II

Beylkin, G., & Monzón, L. (2010). Approximation by exponential sums revisited. *Applied and Computational Harmonic Analysis*, **28**(2), 131–149. DOI: `10.1016/j.acha.2009.08.011`.

**Use:** efficient SOE construction. Every theorem in the paper must specify the approximated function, interval, and norm rather than citing an informal `Ce^{-\beta m}` formula.

### [K05] Fast Caputo evaluation

Jiang, S., Zhang, J., Zhang, Q., & Zhang, Z. (2017). Fast evaluation of the Caputo fractional derivative and its applications to fractional diffusion equations. *Communications in Computational Physics*, **21**(3), 650–678. DOI: `10.4208/cicp.OA-2016-0136`.

**Use:** SOE-based acceleration, complexity, and tolerance-controlled kernel approximation.

### [K06] Fast and oblivious convolution quadrature

Schädle, A., López-Fernández, M., & Lubich, C. (2006). Fast and oblivious convolution quadrature. *SIAM Journal on Scientific Computing*, **28**(2), 421–438. DOI: `10.1137/050623139`.

**Use:** fast history evaluation and reproducible solver design.

---

## C. Delay and latent-state alternatives

### [D01] Functional differential equations

Hale, J. K., & Verduyn Lunel, S. M. (1993). *Introduction to Functional Differential Equations*. Applied Mathematical Sciences, Vol. 99. Springer. DOI: `10.1007/978-1-4612-4342-7`.

**Use:** discrete-delay models, state histories, and linear DDE characteristic equations.

### [D02] Time-delay stability

Michiels, W., & Niculescu, S.-I. (2014). *Stability, Control, and Computation for Time-Delay Systems: An Eigenvalue-Based Approach* (2nd ed.). SIAM. DOI: `10.1137/1.9781611973631`.

**Use:** quasi-polynomial spectra, delay stability, and frequency-domain distinctions from fractional branch behavior.

---

## D. Structural identifiability, controllability, observability, and system identification

### [I01] Structural identifiability origin

Bellman, R., & Åström, K. J. (1970). On structural identifiability. *Mathematical Biosciences*, **7**(3–4), 329–339. DOI: `10.1016/0025-5564(70)90132-X`.

### [I02] Parametric identification

Walter, E., & Pronzato, L. (1997). *Identification of Parametric Models from Experimental Data*. Springer. DOI: `10.1007/978-1-4471-0501-4`.

### [I03] Dynamic system identification

Ljung, L. (1999). *System Identification: Theory for the User* (2nd ed.). Prentice Hall.

### [I04] Frequency-domain identification

Pintelon, R., & Schoukens, J. (2012). *System Identification: A Frequency Domain Approach* (2nd ed.). Wiley-IEEE Press. DOI: `10.1002/9781118287422`.

### [I05] Linear systems and PBH tests

Kailath, T. (1980). *Linear Systems*. Prentice Hall.

**Use:** controllability, observability, PBH tests, and minimal realizations.

### [I06] Fractional-model identifiability in inverse problems

Kharazmi, E., Cai, M., Zheng, X., Zhang, Z., Lin, G., & Karniadakis, G. E. (2021). Identifiability and predictability of integer- and fractional-order epidemiological models using physics-informed neural networks. *Nature Computational Science*, **1**, 744–753. DOI: `10.1038/s43588-021-00158-0`.

**Use:** recent evidence that integer/fractional alternatives can be difficult to identify; not a source for particle MCMC or SBI.

### [I07] Recent structural identifiability for fractional networks

Varalda, A., & Pequito, S. (2026). Structural identifiability in fractional-order networks. *IFAC Journal of Systems and Control*, **35**, 100397. DOI: `10.1016/j.ifacsc.2026.100397`.

**Use:** current related work on graph-structural identifiability in fractional-order networks. Its object is discrete-time/network structural identifiability, not ecological active model discrimination.

### [I08] Fractional parameter identification

Petráš, I., Sierociuk, D., & Podlubny, I. (2012). Identification of parameters of a half-order system. *IEEE Transactions on Signal Processing*, **60**(10), 5561–5566. DOI: `10.1109/TSP.2012.2205920`.

**Use:** parameter-estimation precedents for fractional systems.

---

## E. Classical model-discrimination and robust optimal design

### [O01] T-optimality: two models

Atkinson, A. C., & Fedorov, V. V. (1975). The design of experiments for discriminating between two rival models. *Biometrika*, **62**(1), 57–70. DOI: `10.1093/biomet/62.1.57`.

### [O02] T-optimality: several models

Atkinson, A. C., & Fedorov, V. V. (1975). Optimal design: experiments for discriminating between several models. *Biometrika*, **62**(2), 289–303. DOI: `10.1093/biomet/62.2.289`.

### [O03] KL discrimination beyond Gaussian errors

López-Fidalgo, J., Tommasi, C., & Trandafir, P. C. (2007). An optimal experimental design criterion for discriminating between non-normal models. *Journal of the Royal Statistical Society: Series B*, **69**(2), 231–242. DOI: `10.1111/j.1467-9868.2007.00586.x`.

### [O04] Robust T-optimality

Dette, H., Melas, V. B., & Shpilev, P. (2013). Robust T-optimal discriminating designs. *The Annals of Statistics*, **41**(4), 1693–1715. DOI: `10.1214/13-AOS1117`.

### [O05] Bayesian design review

Chaloner, K., & Verdinelli, I. (1995). Bayesian experimental design: A review. *Statistical Science*, **10**(3), 273–304. DOI: `10.1214/ss/1177009939`.

### [O06] Simulation-based nonlinear Bayesian OED

Huan, X., & Marzouk, Y. M. (2013). Simulation-based optimal Bayesian experimental design for nonlinear systems. *Journal of Computational Physics*, **232**(1), 288–317. DOI: `10.1016/j.jcp.2012.08.013`.

### [O07] Computational Bayesian OED review

Ryan, E. G., Drovandi, C. C., McGree, J. M., & Pettitt, A. N. (2016). A review of modern computational algorithms for Bayesian optimal design. *International Statistical Review*, **84**(1), 128–154. DOI: `10.1111/insr.12107`.

### [O08] Likelihood-free mutual-information design

Kleinegesse, S., & Gutmann, M. U. (2020). Bayesian experimental design for implicit models by mutual information neural estimation. In *Proceedings of the 37th International Conference on Machine Learning*, PMLR **119**, 5316–5326.

### [O09] Modern Bayesian design synthesis

Rainforth, T., Foster, A., Ivanova, D. R., & Bickford Smith, F. (2024). Modern Bayesian experimental design. *Statistical Science*, **39**(1). DOI: `10.1214/23-STS915`.

### [O10] Dynamic biochemical model discrimination

Skanda, D., & Lebiedz, D. (2010). An optimal experimental design approach to model discrimination in dynamic biochemical systems. *Bioinformatics*, **26**(7), 939–945. DOI: `10.1093/bioinformatics/btq074`.

### [O11] Robust dynamic stimulus design

Flassig, R. J., & Sundmacher, K. (2012). Optimal design of stimulus experiments for robust discrimination of biochemical reaction networks. *Bioinformatics*, **28**(23), 3089–3096. DOI: `10.1093/bioinformatics/bts585`.

### [O12] Experimental design in dynamic biological systems

Kreutz, C., & Timmer, J. (2009). Systems biology: experimental design. *The FEBS Journal*, **276**(4), 923–942. DOI: `10.1111/j.1742-4658.2008.06843.x`.

---

## F. Closest literature on experimental design for fractional-order systems

These references are mandatory in the introduction because they delimit the real novelty claim.

### [FOED01] Elementary fractional models

Malti, R., Mayoufi, M., & Victor, S. (2022). Experiment design for elementary fractional models. *Communications in Nonlinear Science and Numerical Simulation*, **110**, 106337. DOI: `10.1016/j.cnsns.2022.106337`.

**Relation:** fractional experiment design for estimating elementary fractional-model parameters; not active discrimination among ecological memory mechanisms.

### [FOED02] Fractional optimal input design

Jakowluk, W. (2019). Optimal input signal design for fractional-order system identification. *Bulletin of the Polish Academy of Sciences: Technical Sciences*, **67**(1), 37–44. DOI: `10.24425/bpas.2019.127336`.

**Relation:** input design for parameter identification after rational approximation.

### [FOED03] Fractional bioimpedance OED

Àngela Sebastià Bargues, J.-L. Polo Sanz, I. García-Camacha Gutiérrez, & R. Martín Martín. (2023). Practical implementation of optimal experimental design using the fractional-order Fricke–Morse bioimpedance model. *Chaos, Solitons & Fractals*, **170**, 113374. DOI: `10.1016/j.chaos.2023.113374`.

**Relation:** D-optimal frequency selection for a fractional bioimpedance model; parameter estimation rather than memory-mechanism discrimination.

### [FOED04] Recent LMI frequency-domain input design

Jakowluk, W., & Świercz, M. (2025). Optimal input design for fractional-order system identification using an LMI-based frequency error criterion. *Applied Sciences*, **15**(23), 12665. DOI: `10.3390/app152312665`.

**Relation:** minimum-power open-loop input satisfying an accuracy criterion for an approximated fractional system. It does not address Caputo-versus-DDE-versus-latent ecological discrimination or ecological safety constraints.

---

## G. Information theory, detection, and sample complexity

### [S01] KL divergence

Kullback, S., & Leibler, R. A. (1951). On information and sufficiency. *The Annals of Mathematical Statistics*, **22**(1), 79–86. DOI: `10.1214/aoms/1177729694`.

### [S02] Chernoff information

Chernoff, H. (1952). A measure of asymptotic efficiency for tests of a hypothesis based on the sum of observations. *The Annals of Mathematical Statistics*, **23**(4), 493–507. DOI: `10.1214/aoms/1177729330`.

### [S03] Information theory

Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley. DOI: `10.1002/047174882X`.

### [S04] Detection and estimation

Van Trees, H. L., & Bell, K. L. (2013). *Detection, Estimation, and Modulation Theory, Part I* (2nd ed.). Wiley.

### [S05] Statistical signal processing

Kay, S. M. (1998). *Fundamentals of Statistical Signal Processing, Volume II: Detection Theory*. Prentice Hall.

---

## H. Bayesian inference and validation tools

### [B01] Stan

Carpenter, B., Gelman, A., Hoffman, M. D., Lee, D., Goodrich, B., Betancourt, M., Brubaker, M., Guo, J., Li, P., & Riddell, A. (2017). Stan: A probabilistic programming language. *Journal of Statistical Software*, **76**(1), 1–32. DOI: `10.18637/jss.v076.i01`.

### [B02] NUTS

Hoffman, M. D., & Gelman, A. (2014). The No-U-Turn sampler: Adaptively setting path lengths in Hamiltonian Monte Carlo. *Journal of Machine Learning Research*, **15**, 1593–1623.

### [B03] Particle MCMC

Andrieu, C., Doucet, A., & Holenstein, R. (2010). Particle Markov chain Monte Carlo methods. *Journal of the Royal Statistical Society: Series B*, **72**(3), 269–342. DOI: `10.1111/j.1467-9868.2009.00736.x`.

### [B04] Simulation-based calibration

Talts, S., Betancourt, M., Simpson, D., Vehtari, A., & Gelman, A. (2018). Validating Bayesian inference algorithms with simulation-based calibration. arXiv:`1804.06788`.

### [B05] PSIS-LOO

Vehtari, A., Gelman, A., & Gabry, J. (2017). Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC. *Statistics and Computing*, **27**, 1413–1432. DOI: `10.1007/s11222-016-9696-4`.

### [B06] WAIC theory

Watanabe, S. (2010). Asymptotic equivalence of Bayes cross validation and widely applicable information criterion in singular learning theory. *Journal of Machine Learning Research*, **11**, 3571–3594.

---

## I. Ecological model, Allee effect, and experimental systems

### [E01] Functional responses

Holling, C. S. (1959). Some characteristics of simple types of predation and parasitism. *The Canadian Entomologist*, **91**(7), 385–398. DOI: `10.4039/Ent91385-7`.

### [E02] Rosenzweig–MacArthur dynamics

Rosenzweig, M. L., & MacArthur, R. H. (1963). Graphical representation and stability conditions of predator–prey interactions. *The American Naturalist*, **97**(895), 209–223. DOI: `10.1086/282272`.

### [E03] Definition of the Allee effect

Stephens, P. A., Sutherland, W. J., & Freckleton, R. P. (1999). What is the Allee effect? *Oikos*, **87**(1), 185–190. DOI: `10.2307/3547011`.

### [E04] Ecological consequences of Allee effects

Courchamp, F., Clutton-Brock, T., & Grenfell, B. (1999). Inverse density dependence and the Allee effect. *Trends in Ecology & Evolution*, **14**(10), 405–410. DOI: `10.1016/S0169-5347(99)01683-3`.

### [E05] Multiple Allee effects

Berec, L., Angulo, E., & Courchamp, F. (2007). Multiple Allee effects and population management. *Trends in Ecology & Evolution*, **22**(4), 185–191. DOI: `10.1016/j.tree.2006.12.002`.

### [E06] Early fractional predator–prey application

Ahmed, E., El-Sayed, A. M. A., & El-Saka, H. A. A. (2007). Equilibrium points, stability and numerical solutions of fractional-order predator–prey and rabies models. *Journal of Mathematical Analysis and Applications*, **325**(1), 542–553. DOI: `10.1016/j.jmaa.2006.01.087`.

### [E07] Fractional prey–predator model with harvesting

Javidi, M., & Nyamoradi, N. (2013). Dynamic analysis of a fractional order prey–predator interaction with harvesting. *Applied Mathematical Modelling*, **37**(20–21), 8946–8956. DOI: `10.1016/j.apm.2013.04.024`.

### [E08] Fractional predator–prey and delays

Rihan, F. A. (2021). Fractional-order delay differential equations with predator–prey systems. In *Delay Differential Equations and Applications to Biology*. Springer Singapore. DOI for the volume: `10.1007/978-981-16-0626-7`.

### [E09] Recent fractional Bazykin model with delay

Ranjith Kumar, G., & Ramesh, K. (2024). Dynamical analysis of fractional-order Bazykin’s model with prey refuge, gestation delay and density-dependent mortality rate. *Iranian Journal of Science*, **49**(1), 79–91. DOI: `10.1007/s40995-024-01658-0`.

### [E10] Controlled predator–prey microcosm

Fussmann, G. F., Ellner, S. P., Shertzer, K. W., & Hairston, N. G., Jr. (2000). Crossing the Hopf bifurcation in a live predator–prey system. *Science*, **290**(5495), 1358–1360. DOI: `10.1126/science.290.5495.1358`.

### [E11] Eco-evolutionary predator–prey experiment

Yoshida, T., Jones, L. E., Ellner, S. P., Fussmann, G. F., & Hairston, N. G., Jr. (2003). Rapid evolution drives ecological dynamics in a predator–prey system. *Nature*, **424**, 303–306. DOI: `10.1038/nature01767`.

### [E12] Long nonlinear microbial dynamics

Becks, L., Hilker, F. M., Malchow, H., Jürgens, K., & Arndt, H. (2005). Experimental demonstration of chaos in a microbial food web. *Nature*, **435**, 1226–1229. DOI: `10.1038/nature03627`.

---

## J. Validated numerics and reproducibility of the ecological baseline

### [V01] Interval analysis

Moore, R. E., Kearfott, R. B., & Cloud, M. J. (2009). *Introduction to Interval Analysis*. SIAM. DOI: `10.1137/1.9780898717716`.

### [V02] Verification methods

Rump, S. M. (2010). Verification methods: Rigorous results using floating-point arithmetic. *Acta Numerica*, **19**, 287–449. DOI: `10.1017/S096249291000005X`.

---

## K. Project sources

### [P01] Validated predecessor paper

*Computer-Assisted Stability and Extinction Certificates for a Caputo Predator–Prey System with a Strong Prey Allee Effect*. Uploaded project manuscript, draft dated 2026-07-30.

**Use:** exact baseline model, certified equilibrium, Matignon boundary, extinction funnel, and validated-numerics architecture. Replace this project-style entry with the final author list, year, repository DOI, or journal citation before submission.

### [P02] Identifiability predecessor draft

`main.pdf`. Uploaded project draft.

**Use:** historical problem framing only. Mathematical and empirical claims from this draft must not be cited as established results until corrected and reproduced.

### [P03] Current proposal

*Optimal Experimental Design for Identifying Ecological Memory*. Project proposal.

**Use:** project design requirements, not external evidence.

---

## L. References removed or quarantined

The following citations appearing in `main.pdf` are **not admitted to the final bibliography without a verifiable record**:

- `Ghosh et al. (2024), Fractional-order modeling of ecological and epidemiological systems: ambiguities and challenges, Sankhya B` — no reliable bibliographic match was established;
- `Bellmann and Lopez (2013)` as a pseudo-rational identifiability source — bibliographic identity is unresolved and the associated mathematical reduction is invalid;
- `Mondal and Kar (2026)` as described in the draft — exact publication metadata and the claimed content were not established here;
- `Baez and Rodriguez (2020)` and `Heymans and Bauwens (2021)` as written in the draft — retain only after exact title, venue, and DOI are independently confirmed;
- the alleged microbial dataset attributed to Beylkin–Monzón — false attribution;
- any empirical ELPD, Bayes-factor, posterior-interval, or SBC result in `main.pdf` — these are results requiring data and code, not bibliography entries.

Use `[[CITE-NEEDED: exact claim]]` in the manuscript rather than inventing a source.

---

## M. Minimum citation set for a compact first submission

A compact theorem-driven paper can be supported by the following 25 load-bearing sources:

`F02, F03, F05, F06, F09, F10, K02, K03, K04, K05, D01, I01, I02, I05, I06, I07, O01, O02, O04, O05, O06, FOED01, FOED02, FOED03, FOED04`.

Add `E01–E12` for ecological motivation and experimental implementation, and `B01–B06` only when those computational procedures are actually implemented.
