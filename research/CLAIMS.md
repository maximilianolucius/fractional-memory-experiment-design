# Claim registry — MDPI version (directives §4)

Every statement in the abstract/conclusions traces to a claim here. Evidence classes per
directives §20: THEOREM / CERTIFIED / CORROBORATION / OPEN.

```text
CLAIM: THM-SEP (Theorem 1)
statement: G_alpha not meromorphic at s=0; O(w^-alpha) rolloff unreachable by rational
           and strictly proper retarded transfers
scope: linearized prey channel, CB != 0, alpha irrational
status: THEOREM (classical mechanism, stated for scope; no priority claimed)
boundary_cases: alpha rational -> excluded by hypothesis; CB=0 -> fails (known counterexample)
machine_audit: none needed (classical)

CLAIM: LEM-SOE (Lemma 1)
statement: E+_m(alpha,T) = T^alpha E+_m(alpha,1) exactly; for every c < pi*sqrt(alpha(1-alpha))
           exists A(alpha,c): E+_m <= A T^alpha exp(-c sqrt(m)); m(eps)=O(log^2(1/eps))
scope: all alpha in (0,1), all T>0, positive weights/rates
status: THEOREM (proof in paper; technique attributed to McLean 2018)
boundary_cases: c = pi*sqrt(alpha(1-alpha)) NOT established (constant diverges) -> OPEN-1
proof_dependencies: Stieltjes representation; analytic-strip trapezoid (Trefethen-Weideman)
machine_audit: rescue_compute/c1_complexity_law.py (285 cells; scaling verified to machine
               precision; bound active with A in [0.29, 11.1]) - corroboration, not proof

CLAIM: COR-CLOSURE (Corollary 1)
statement: finite-horizon closure of the latent hierarchy; discrimination meaningful only
           relative to declared budget m
status: THEOREM (immediate from LEM-SOE)

CLAIM: THM-FLOOR (Theorem 2)
statement: P_e* = Phi(-d/2) exactly (common covariance); P_e* >= Phi(-E B/(2 sigma)),
           uniform over ||u||_2 <= B and over sampling schedules
scope: linearized prey response; Gaussian noise, common covariance
status: THEOREM (two-point identity textbook; pairing at response level is the content)
boundary_cases: equality iff u attains Young bound; degenerate only if E*B/sigma -> infinity
forbidden: routing through ||k_alpha - k_m||_{L2} (infinite for alpha <= 1/2)

CLAIM: CERT-GM32
statement: E_m^state enclosures 0.5334 / 0.1254 / 0.0273 / 0.0069 at m=4/8/16/32
scope: alpha=0.85, A=0.25, T=12; optimized class G_m (pole region + L1 mass cap)
status: CERTIFIED (outward-rounded interval subdivision)

CLAIM: CERT-SUR128
statement: ||g_alpha - g_m||_L1 <= 1.2861 / 0.49751 / 0.13017 / 0.023113 / 1.5778e-3 /
           4.8890e-5 at m=4..128 for the explicit SOE surrogate; floors 0.2201 .. 0.499988
scope: same cell; one admissible element -> upper bound on the class error
status: CERTIFIED (Arb 256-bit; scalar reduction eq.(6)-(8); interval-Newton poles:
        existence+uniqueness per box, pairwise disjoint, Re p < 0; graded 55,297-interval
        mesh; Gautschi tails; exact inter-process transport)
machine_audit: rescue_compute/r6_response_interval_cert.py + .json
negative_fixture: double-precision seed at m=32 correctly REJECTED by interval Newton
cross_check: scalar vs matrix formulas: 2.7e-14 (g_alpha), 1.9e-15 (g_m, m=16)

CLAIM: EMP-FRONTIER
statement: classical six-family frontier (0.584/0.583 accuracy at 100%/35.7% crossings;
           only safe family scores 0.324 at benchmark layer / 0.514 at validation layer)
status: CORROBORATION (1512 cells x 200 reps; frozen)

CLAIM: EMP-AMPLITUDE
statement: halving amplitude leaves PRBS most informative and still crossing 71.4%;
           realized gain 28.07 vs linear certificate 5.78 (4.86x violation)
status: CORROBORATION (2268 cells, 3 amplitudes, 0 divergences)

CLAIM: EMP-SEARCH
statement: 163,840 candidates, 87,601 safe; best safe J=6.23 vs 1.45 classical;
           top-12 safe all piecewise-constant; validated: S0 macro 0.803, 0 crossings,
           margin +0.092; vs 0.514 (safe classical) and 0.763 (best classical)
status: CORROBORATION (existence result; NOT a certified global optimum)
held_out: A=0.20 fully held out; searched lose 0.060 avg vs classical 0.087;
          out-of-sample lead 0.907 vs 0.837; advantage larger out of sample

CLAIM: CERT-SAFETY4
statement: validated enclosures for 4/8 headline trajectories; rigorous prey-minimum
           lower bounds 0.441 and 0.309 vs A=0.25
status: CERTIFIED for those four ONLY; other four verified-not-enclosed with structural
        failure causes stated (delay: input discontinuities re-enter through retarded
        argument; Caputo: solver order limits the defect)

CLAIM: CERT-M2
statement: M2(0.05) <= 5.47 interval-certified (sampling underestimates 19%);
           r_max = 0.0294; U_NL = 1.42e-3 (70x below budget) -> invariant-ball route closed
status: CERTIFIED (conditional on numerically computed Gamma_B, Gamma_R - stated)

CLAIM: EMP-REPRO
statement: frozen benchmark reproduces to 4 decimals cross-host, different numpy/scipy
status: CORROBORATION

OPEN-1: attainment/optimality of the boundary rate in LEM-SOE
OPEN-2: certified global optimum over the PWC class
OPEN-3: enclosures for delayed/Caputo headline trajectories
OPEN-4: penalty-free decision layer separating floor from BIC dimension preference
```
