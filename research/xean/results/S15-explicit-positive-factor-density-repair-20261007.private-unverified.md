# S15: explicit auxiliary density for the complete named-factor proof

New private, unverified mathematical material. The whole-class original-task
review of 7 October returned INCONCLUSIVE. Its complete report and original
five factor notes remain unchanged. This note supplies the missing explicit
choice in the full submitted factor chain; it does not change that verdict,
certify this revision, or solve unrestricted S15. The conditional A--G cold
reconstruction has no access to this note or any author proof.

Use exactly the quotient, charts, operator and matrix convention of the five
P07-factor-blind notes included in the full S15 argument. In particular
sigma_s=i ds wedge dbar(s)/(2pi)=dRe(s)dIm(s)/pi. FIX, rather than quantify
over unspecified allowable densities,

    b(s)=exp(-1/(1-|s|^2)) for |s|<1, and b(s)=0 for |s|>=1;
    Z=integral_C b(s) sigma_s;
    p(s)=b(s)/Z.

Then 0<Z<infinity. The function b is C-infinity across |s|=1, since every
derivative of exp(-1/t), extended by zero for t<=0, tends to zero as t
decreases to zero. Thus p is a globally smooth probability, supported in
the closed unit disk, positive on its open interior. In particular

    min_(|s|<=1/4) p(s)=Z^(-1) exp(-16/15)>0.             (R1)

All densities p_delta(s)=delta^(-2)p(s/delta) have integral one relative
to sigma_s, by the real two-dimensional change of variables. For the actual
sequence delta_j=2^(-j)/1000, their support lies in |s|<1/100, inside the
injective logarithmic chart and inside the compact parameter region of n3.
Their extension to the elliptic fiber is smooth. No uniform derivative bound
as delta decreases to zero is required.

For clarity, the original *statement-only factor input* actually specified
that p is positive throughout the open unit disk. The full S15 argument
contained only the five proof notes and referred to 'allowed p from I'
without including that definition. This is a missing self-contained
qualification in that submission. We preserve the review's recorded gap
and make the density explicit here instead of changing its historical text.

## Exact effect on every step of the five-note dependency

n1 is independent of p: it gives the actual connected compact quotient,
the descending genuinely nonclosed positive omega and volume24pi. It also
gives the nonempty normalized closed positive test family.

For n2, this actual p satisfies every smoothness, support and probability
requirement. The concentration forms B_delta are smooth, semipositive, and
converge to chi0(x)chi0(y)[zeta=0]. Their pairings against all normalized
positive dd^c-closed tests are finite. The Lamari and canonical compactness
argument, local CLOSED-current Siu application, and translated-divisor
contradiction imply C_delta tends to infinity. That argument uses no lower
bound on p away from its support, so no new uniformity premise is added.

For n3, choose the other probabilities exactly as in that note:

    r(a)=1/2 k_(1/16)(a-1)+1/2 k_(1/16)(a+1),
    k(b)=k_1(b), l_epsilon(e)=k_(epsilon/(64(1+epsilon)))(e),

where k_R is the normalized disk bump relative to sigma, with radius R.
The family of actual compact curves and its incidence-submersion argument
therefore gives globally smooth closed semipositive T_(delta,epsilon) and
a uniform omega-degree bound. Every parameter support lies in the same
compact region used in its proof. For FIXED delta, convolution in e gives
the printed smooth local limit

    Q_(delta,0)=P_delta(zeta) integral r(a)k(y-ax)
                       (1,a,0)^T(1,a,0)^* sigma_a.

On V_delta={|x|,|y|<1/4, |zeta|<delta/4}, equation(R1) gives
P_delta(zeta)>=Z^(-1) exp(-16/15) delta^(-2). Because |a|<=17/16,
|y-ax|<33/64<17/32. Hence k_*:=min_(|b|<=17/32)k(b)>0.
The symmetry of r eliminates the cross moment and |a|>=15/16>7/8 on
its support. Consequently

    integral r(a)(1,a)^T(1,a)^* sigma_a >= (7/8)^2 I_2,
    Q_(delta,0)=diag(B,0),
    B >= [Z^(-1)exp(-16/15) k_*(7/8)^2] delta^(-2) I_2. (R2)

The bracket is a fixed strictly positive number, independent of delta.
This proves precisely the horizontal block bound missing in the review.
No density supported away from the central disk is being admitted.

n4 now uses actual(R2) together with its full-family concentration witnesses
from n2. Its translation average S_delta Theta stays globally smooth,
strictly positive and dd^c-closed, with uniformly bounded omega degree.
For each fixed delta_j its determinant/root argument gives a strictly
positive Gamma_j=S_(delta_j)Theta_j+T_(delta_j,epsilon_j) with

    D_j:=integral omega wedge Gamma_j <= K+D,
    V_j:=integral eta_j^3 -> infinity, Gamma_j=eta_j^2.

The root is eta_j=sqrt(det Q_j/2) Q_j^(-1) in its tangent convention;
uniqueness makes the local roots patch globally. Selection of epsilon_j
uses only fixed-delta smooth convergence. Neither uniform-in-delta
convergence nor a global smooth limit T_(delta,0) is used.

Finally fix ANY smooth positive Hermitian h on this quotient. Smooth
Tosatti--Weinkove existence supplies supremum-normalized smooth u_j with

    (h+D u_j)^3=c_j eta_j^3, h+D u_j>0.

Smooth Stokes and D Gamma_j=0 give
integral(h+D u_j) wedge Gamma_j=integral h wedge Gamma_j<=K_h D_j,
since h<=K_h omega on the compact manifold. Pointwise matrix AM--GM gives
(h+D u_j) wedge eta_j^2 >= c_j^(1/3) eta_j^3. After integration,

    c_j V_j <= (K_h D_j)^3/V_j^2 ->0.

Thus these are actual smooth collapsing currents for every h. The root,
global smoothing, concentration and compactness proofs are the ENTIRE
five earlier notes, now applied to the explicitly chosen density above.
Their foundational primary applications still require independent exact
assessment; the density calculation cannot substitute for those proofs.

This repairs the identified factor premise at a concrete admissible choice.
It does not alter the old n3, its old result, or the original INCONCLUSIVE
S15 review. It remains new unverified material until combined final review.
