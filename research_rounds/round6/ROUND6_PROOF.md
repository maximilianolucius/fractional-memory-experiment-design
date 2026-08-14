# Round 6 — Full ecological-state finite-latent approximation and testing theorem

Date: 2026-08-14.  Status: statements + proofs, with the interval-certification
contract of each constant.  Companion code: `compute_round6.py` (outward-rounded
interval certificates, mpmath.iv), `check_round6.py` (independent float
validation; QUADPACK used only as a cross-check, never as a certificate).

Everything below is for the locked parameters r=3/2, K=1, a=1, h=1/2, e=4/5,
m_mort=2/5 (so x*=2/3), horizon T=12, fractional order alpha=17/20, and the
focal Caputo linearization at the coexistence equilibrium.

---

## 0. Setting and the exact focal object

The linearized Caputo dynamics at the coexistence equilibrium, with prey-channel
actuation and prey-channel observation, is

    D^alpha xi = J(A) xi + e_1 u,     x(t) = e_1^T xi(t),

with J(A) the exact coexistence Jacobian (source_pack/04, eq. 5–6; J_22 = 0).
Its transfer function is the TRUE fractional transfer

    G_alpha(s) = e_1^T (s^alpha I - J(A))^{-1} e_1,

(the object mandated by the Round-6 prompt; no use is made of the false
factorization (s^alpha I - J)^{-1} = (sI - J)^{-1} s^{-alpha}).  Its impulse
response is

    g_alpha(t) = e_1^T t^{alpha-1} E_{alpha,alpha}(J t^alpha) e_1
               = w_1 e_alpha(t; lambda_1) + w_2 e_alpha(t; lambda_2),

where lambda_{1,2} are the eigenvalues of J(A),
e_alpha(t;lambda) = t^{alpha-1} E_{alpha,alpha}(lambda t^alpha) is the scalar
fractional-relaxation kernel (inverse Laplace transform of 1/(s^alpha-lambda)),
and, because J_22 = 0 and the eigenvalues are distinct,

    w_1 = lambda_1/(lambda_1 - lambda_2),   w_2 = 1 - w_1        (exact).

In the whole focal atlas range A in {0.10,...,0.34} the eigenvalues form one
complex-conjugate pair lambda, lambda-bar with Im lambda > 0, and w_2 =
w_1-bar, so g_alpha is real.

**Sector facts (interval-verified per cell).**  For every Matignon-stable focal
cell (all A in {0.10, 0.15, 0.20, 0.25, 0.30, 0.32, 0.34} at alpha = 0.85):

    alpha*pi/2 < |arg lambda| < alpha*pi.

The right inequality says the equation s^alpha = lambda has exactly one
solution on the principal sheet |arg s| < pi, namely s_0 =
|lambda|^{1/alpha} e^{i arg(lambda)/alpha}; the left inequality (Matignon) says
precisely Re s_0 < 0.  Both are checked by outward-rounded interval arithmetic
in `backbone_iv` (hard assertions).

---

## Lemma R6.1 (exact pole/branch-cut decomposition)

For 0 < alpha < 1 and lambda in C with alpha*pi/2 < |arg lambda| < alpha*pi,
for all t > 0:

    e_alpha(t; lambda) = (s_0/(alpha*lambda)) e^{s_0 t}
                         + int_0^inf e^{-r t} phi_lambda(r) dr,

    phi_lambda(r) = (1/pi) * r^alpha sin(alpha*pi)
                    / (r^{2 alpha} - 2 lambda r^alpha cos(alpha*pi) + lambda^2).

*Proof.*  Invert 1/(s^alpha - lambda) along a Bromwich contour deformed onto
the Hankel contour around the negative real axis (principal branch of
s^alpha).  Since |1/(s^alpha - lambda)| = O(|s|^{-alpha}) as |s| -> infinity
uniformly in |arg s| <= pi, the large arcs contribute zero (Jordan-type
estimate on e^{st} for t>0), and the small circle around the origin also
vanishes as its radius -> 0 because the integrand is O(rho^{-alpha}) with
alpha < 1 while the arc length is O(rho).  The deformation crosses exactly the
principal-sheet zeros of s^alpha - lambda.  By the sector hypothesis
|arg lambda| < alpha*pi there is exactly one such zero s_0 =
lambda^{1/alpha}; the residue of e^{st}/(s^alpha - lambda) there equals
e^{s_0 t}/(alpha s_0^{alpha-1}) = (s_0/(alpha lambda)) e^{s_0 t}, using
s_0^alpha = lambda.  The two rays s = r e^{+-i pi} contribute

    (1/(2 pi i)) int_0^inf e^{-r t} [ 1/(r^alpha e^{-i alpha pi} - lambda)
                                    - 1/(r^alpha e^{+i alpha pi} - lambda) ] dr
    = int_0^inf e^{-rt} phi_lambda(r) dr

after the elementary algebra
1/(x e^{-i a pi} - lambda) - 1/(x e^{i a pi} - lambda)
= 2 i x sin(a pi) / (x^2 - 2 lambda x cos(a pi) + lambda^2), x = r^alpha.
The denominator x^2 - 2 lambda x cos(a pi) + lambda^2 =
(x - lambda e^{i a pi})(x - lambda e^{-i a pi}) never vanishes for x > 0
because |arg lambda| < alpha*pi strictly; so phi_lambda is smooth on (0,inf).
Near r = 0, phi_lambda(r) = O(r^alpha); as r -> inf, phi_lambda(r) =
(sin(alpha pi)/pi) r^{-alpha} (1 + O(r^{-alpha})).  Hence the integral
converges absolutely for every t > 0 and defines a completely monotone-type
remainder.  QED.

(Independent numerical validation: the decomposition agrees with the
Mittag-Leffler series to ~1e-11 at scattered t; `check_round6.py`.)

**Corollary (real form).**  Summing over the conjugate pair with conjugate
weights,

    g_alpha(t) = p(t) + b(t),
    p(t) = 2 Re[ P e^{s_0 t} ],   P := w_1 s_0/(alpha lambda),
    b(t) = int_0^inf e^{-r t} Phi(r) dr,   Phi(r) := 2 Re[ w_1 phi_lambda(r) ],

with p, b real, p the impulse response of the REAL 2-dimensional integer-order
system

    dot z = [[sigma, omega], [-omega, sigma]] z + beta u,   y = gamma^T z,

(sigma = Re s_0 < 0, omega = Im s_0; suitable beta, gamma realizing amplitude
2|P| and phase arg P), and Phi a smooth real (generally signed) density.

**Remark (why Gate 0B is bypassed).**  The Round-5 negative Gate 0B showed the
irreducible mismatch D0(A) = ||h_J^alpha - h_J * k_alpha||_1 between the true
fractional backbone and any "shared-kernel x integer backbone" factorization.
In the decomposition above, the oscillatory pole pair — exactly the backbone
content that the factorized route could not reproduce — is realized EXACTLY by
an integer-order 2-dimensional block, and what remains is a smooth completely
monotone-type branch part, which finite exponential mixtures approximate to
arbitrary accuracy.  The obstruction D0 was a property of the factorized
construction, not of the model class.

---

## Definition (full-state latent rival hierarchy)

For a state-dimension budget m >= 3 and a declared rate cutoff R_m > 0, let

    G_m := { stable integer-order LTI systems of state dimension <= m,
             all poles in { s : Re s < 0, |s| <= max(R_m, |s_0|) },
             impulse response mass ||g||_{L1(0,T)} <= M_state },

with the declared mass cap

    M_state(A) := (interval upper enclosure of ||g_alpha||_{L1(0,T)}) + 1,

in exact analogy with the kernel-level M_T = ||k_alpha||_1 + 1.  The class is
nested in m and in R_m.  (Certified values of M_state: `round6_results*.json`,
field `M_state`; 4.5661 at A=0.25, 6.5453 at A=0.30.)

The CONSTRUCTED member g_m in G_m is: the exact 2-dim pole block + N = m-2
first-order modes v_j e^{-rhat_j t} with nodes rhat_j in [0, R_m] and weights
v_j given by midpoint enclosures of int_{a_j}^{b_j} Phi over a partition
0 = a_1 < b_1 = a_2 < ... < b_N = R_m.  If the certified rival mass exceeds
M_state, all v_j are rescaled by the certified factor s < 1 and the additional
error (1-s)*||mixture||_1 is added to the enclosure (the chief's P0.2 repair
pattern); in the shipped table no rescale was triggered.

---

## Theorem T23 (certified full ecological-state approximation)

For every focal Matignon-stable cell A and every budget m in {4,8,16,32}
there is an explicit g_m in G_m with

    || g_alpha - g_m ||_{L1(0,T)} <= Ehat_m^state(A),

where Ehat_m^state(A) is an outward-rounded interval enclosure composed of:

(i) **body terms.**  For each partition interval [a,b] with node rhat and
    weight v (midpoint of the interval enclosure S0 of int_a^b Phi):

    int_0^T | int_a^b e^{-rt} Phi(r) dr - v e^{-rhat t} | dt
      <= min{ B1, B2 } + rad(S0) * w(rhat),

    B1 = max( w(a)-w(rhat), w(rhat)-w(b) ) * int_a^b |Phi|,
    B2 = |int_a^b (r-rhat) Phi dr| * G1(a) + (1/2) int_a^b (r-rhat)^2 |Phi| dr * G2(a),

    with w(r) = int_0^T e^{-rt} dt (w(0)=T), G1(a) >= int_0^T t e^{-at} dt,
    G2(a) >= int_0^T t^2 e^{-at} dt.

(ii) **tail term.**  int_0^T | int_{R_m}^inf e^{-rt} Phi dr | dt
      <= int_{R_m}^inf |Phi(r)|/r dr
      <= (2 |w_1| sin(alpha pi) / (pi kappa alpha)) R_m^{-alpha},
    kappa = 1 - 2|lambda| |cos(alpha pi)| R_m^{-alpha} - |lambda|^2 R_m^{-2 alpha} > 0.

All integrals of Phi over compact intervals are enclosed by adaptive interval
subdivision of the explicit elementary expression for Phi; no numerical
quadrature routine's error estimate is used anywhere.

*Proof of (i).*  Write the local error as
int (f_t(r) - f_t(rhat)) Phi dr + (int Phi - v) f_t(rhat) with f_t(r)=e^{-rt}.
For B1: for fixed r, e^{-rt} - e^{-rhat t} has a single sign in t on [0,T], so
int_0^T |e^{-rt} - e^{-rhat t}| dt = |w(r) - w(rhat)|, and w is decreasing, so
the sup over r in [a,b] is max(w(a)-w(rhat), w(rhat)-w(b)).  For B2: Taylor
with exact remainder around rhat, |f_t(r) - f_t(rhat) + t(r-rhat) e^{-rhat t}|
<= (t^2/2) e^{-at} (r-rhat)^2 for r, rhat >= a; integrate in t using
int_0^T t e^{-rhat t} dt <= G1(a) and int_0^T t^2 e^{-at} dt <= G2(a).  The
weight-radius term uses int_0^T e^{-rhat t} dt = w(rhat).  Both bounds are
valid simultaneously, so their minimum is valid.  *Proof of (ii).*
|int_R^inf e^{-rt} Phi dr| <= int_R^inf e^{-rt} |Phi| dr; integrate in t first:
int_0^T e^{-rt} dt <= 1/r; then bound |Phi(r)| <= (2|w_1| sin(alpha pi)/pi)
r^{-alpha}/kappa via the reverse triangle inequality
|x^2 - 2 lambda x cos + lambda^2| >= x^2 (1 - 2|lambda||cos|/x - |lambda|^2/x^2),
x = r^alpha >= R^alpha, and integrate r^{-alpha-1}.  QED.

**Certified table (alpha=0.85, T=12; `round6_results.json`):**

    A=0.25:  Ehat^state_4  <= 0.5335   Ehat^state_8  <= 0.1254
             Ehat^state_16 <= 0.0274   Ehat^state_32 <= 0.0070
    A=0.30:  Ehat^state_4  <= 0.4706   Ehat^state_8  <= 0.0899
             Ehat^state_16 <= 0.0204   Ehat^state_32 <= 0.0067

Compare the kernel-level enclosures 0.352 / 0.248 / 0.200 / 0.134 (m = 4, 8,
16, 32): once the pole pair is matched exactly, the remaining smooth branch
density is far easier to approximate, and the certified state-level error
drops below the kernel-level one from m = 8 on — by an order of magnitude at
m = 16.  Independent float validation puts the true L1 distances at 3–5x
below the enclosures (`check_round6.py`, 8/8 OK at the focal cells).

**Convergence.**  With m -> inf, choosing R_m -> inf and refining the
partition, Ehat^state_m -> 0 (tail = O(R_m^{-alpha}), body terms -> 0 by
second-order locality); the hierarchy has no analogue of the Gate-0B floor.

---

## Theorem T23' (ecological-state testing bound)

Let S : L^2(0,T) -> R^q be a bounded linear observation operator on the PREY
deviation channel, observations Gaussian with covariance R, and
C_obs = (1/2) ||R^{-1/2} S||^2 as in T20.  Let U be any common-safe input
class with ||u||_2 <= B_eff for all u in U.  Then the robust minimax error of
testing the true fractional ecological response against the latent class G_m
satisfies

    P_e^*(m) >= Psi( C_obs (Ehat_m^state)^2 B_eff^2 ),

with the same Psi_Pin / Psi_BH / Psi_G as in T20.

*Proof.*  Identical to T20 with k_alpha, k_m replaced by g_alpha, g_m: Young's
inequality gives ||(g_alpha - g_m)*u||_2 <= Ehat_m^state B_eff; the Gaussian
KL of the two-point subproblem is at most C_obs (Ehat_m^state B_eff)^2; the
composite minimax risk dominates the two-point Bayes risk; the KL ceiling is
uniform over U.  QED.

Unlike T20 — which is a statement about the abstract memory KERNEL fed
through a shared convolution — T23' bounds discrimination of the true
fractional PREY RESPONSE against genuinely integer-order finite-state
ecological models.  This is the full ecological-state theorem that Round 5
left open, with the observation channel e_1 (prey); any bounded observation
operator on the prey deviation is covered by C_obs.

---

## Theorem T24 (state-level pulse-ray Strong-Allee budget: sandwich)

Fix the declared positive pulse ray u = c u_0, c >= 0, u_0 the unit-L2
rectangular protocol pulse (support length Delta = 1.44, ||u_0||_inf/||u_0||_2
= 1/sqrt(Delta)).  For the class G_m:

(upper/Young)     d(g) := max_t [-(g*u_0)(t)]_+ / 1  <=  M_state/sqrt(Delta)
                  for every g in G_m,

(lower/witness)   d_rob(G_m, u_0) := sup_{g in G_m} d(g)
                  >= d_low := (M_state / w(rhat)) (1 - e^{-rhat Delta}) / (rhat sqrt(Delta)),

for any admissible rate 0 < rhat <= R_m, realized by the member
g = -(M_state/w(rhat)) e^{-rhat t} in G_m (dimension 1, pole -rhat, mass
exactly M_state).  Consequently every common-safe ray amplitude satisfies the
necessary outer bound

    ||u||_2 = c <= rho_eta / d_rob(G_m,u_0) <= rho_eta / d_low
             =: B_Allee^state(A, m),      rho_eta = x* - (A + eta).

*Proof.*  Upper: Young, ||g*u_0||_inf <= ||g||_{L1(0,T)} ||u_0||_inf <=
M_state ||u_0||_inf, and ||u_0||_inf = 1/sqrt(Delta) for the unit-L2
rectangle.  (For t in (T, T+Delta) the response depends only on g on (0,T)
shifted; the same bound holds on any horizon.)  Lower: for the exhibited
member, (e^{-rhat .} * u_0)(t) is maximal at the trailing edge of the pulse
with value (1 - e^{-rhat Delta})/(rhat sqrt(Delta)) —  the elementary
closed-form convolution of an exponential with a rectangle — so
d(g) = (M_state/w(rhat)) (1-e^{-rhat Delta})/(rhat sqrt(Delta)).  Membership:
||g||_{L1(0,T)} = (M_state/w(rhat)) w(rhat) = M_state, dimension 1 <= m, pole
in the declared region.  Safety against every member of G_m (one-sided prey
threshold, exactly as in T22) forces c d(g) <= rho_eta for all g, hence
c <= rho_eta / d_rob <= rho_eta / d_low.  QED.

**Directional discipline (the Round-2/Round-5 error class).**  B_Allee^state
divides rho_eta by the certified LOWER bound d_low of the supremum; this is
the direction that makes the budget a TRUE outer bound (c <= rho_eta/sup <=
rho_eta/d_low).  The Young bound shows the sandwich is tight: at the focal
cells d_low/d_up ~ 0.987–1.0 with rhat = R_m (both endpoints are closed-form
interval numbers; no grid maximization is involved anywhere in T24, so —
unlike the T22 constants — the state-level budget IS interval-certified end
to end).

**Certified budgets (focal cells, s=0.10 shown; full grid in JSON):**

    A=0.25: B_Allee^state = 0.1042–0.1057 (m-dependent), active over
            shape cap 0.1200 and universal cap 0.3464.
    A=0.30: B_Allee^state = 0.0636–0.0644, active.

With Corollary cor:pulse_testing's B_eff = min(B_Allee^state, shape cap,
universal cap), the certified state-level lower bounds at sigma = 0.10 are

    A=0.25:  P_e >= 0.359 (m=4), 0.467 (m=8), 0.493 (m=16), 0.498 (m=32)
    A=0.30:  P_e >= 0.424 (m=4), 0.486 (m=8), 0.497 (m=16), 0.499 (m=32)

— every focal cell is hard at the 0.25 level, at every latent budget, for the
declared pulse ray.  This closes the Round-6 primary objective with safety
outcome A (state-level pulse-ray Allee budget for the same hierarchy), and
the universal actuator cap variant (outcome B) is also reported in the JSON
(`testing_universal_cap`) and remains non-vacuous from m = 8 on.

---

## Hard-gate checklist (ROUND6_RESEARCHER_PROMPT)

1. Rival integer-order and finite-dimensional: YES (2-dim real pole block +
   first-order modes; rational transfer, dimension <= m).
2. Exact focal object is G_alpha(s) = C (s^alpha I - J)^{-1} B: YES (spectral
   decomposition of exactly that transfer; no factorization through
   (sI-J)^{-1} s^{-alpha} anywhere).
3. Genuine upper enclosure, no QUADPACK: YES (mpmath.iv outward-rounded
   enclosures; QUADPACK appears only in the independent float cross-check).
4. Constructive rival satisfies declared pole/gain/mass constraints: YES
   (mass check certified per cell; automatic rescale path present, not
   triggered; poles inside the declared region by construction).
5. Same hierarchy in approximation and testing: YES (G_m in T23 and T23').
6. Allee bound for exactly the stated input class: YES (positive pulse ray
   only; T24 states the ray explicitly; no arbitrary-waveform claim).
7. All "stable ecological" cells satisfy Matignon: YES (interval-verified
   sector assertions per cell; A=0.38, 0.42 are excluded by the assertion
   itself).
8. No lower-bound failure called discriminability: YES (only P_e lower bounds
   are reported; no "discriminable" labels anywhere in Round 6).

## Scope and honesty

- T23/T23'/T24 are linearized statements at the coexistence equilibrium, same
  scope as T20/T22 (Option A of the paper).
- The Allee budget is protocol-ray-restricted, exactly like the chief-repaired
  T22; no universal safe-design claim.
- The T22 kernel-level result remains a separate theorem about the abstract
  latent kernel hierarchy; T23 does not supersede it (different adversarial
  classes), it supplies the ecological-state lift that Rounds 4–5 could not.
- Ehat^state constants are interval-certified; the T24 budget endpoints are
  closed-form interval numbers; nothing in Round 6 relies on grid maximization
  presented as certified.
