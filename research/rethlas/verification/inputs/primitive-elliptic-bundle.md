Run_id: primitive_elliptic_bundle_01

Run scope: Bounded verification through the normal Rethlas workflow. The parent owns manuscript edits, build and release. Restrict writes to normal verifier tools, memory and results. Do not alter book/editorial/blueprint/status/changelog files, frozen inputs, original references or historical reports. Do not commit or push.

Statement: Verify the four complete mathematical items in the supplied proof, in order. They treat primitive holomorphic line-bundle quotients over compact Kähler surfaces: metric construction and exact upper mass; an elementary sharp periodic variance bound; a positive mass bound for separated potentials and an exact radial infimum; and a specific K3 base with no curves giving a total space with no divisors and only elliptic fiber curves. No unrestricted lower-mass conclusion or novelty is claimed. This scope does not include the pending determination of lower mass on the general family.

Accepted inputs: Scalar Poisson solvability for smooth mean-zero functions on a compact Kähler manifold; the book's proved equality of bounded-potential and smooth strictly admissible mass extrema in a Hermitian background; classical Stokes, projection of integration currents under proper generically finite maps, proper mapping theorem, adjunction, elementary periodic convolution and Baire's theorem. The standard K3 facts listed before Proposition4's proof are accepted as reference inputs; verify their exact application to the lattice, period and chosen Kähler class. The primary author-hosted source has been consulted at https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf Theorem7.4.1 (draft p134), Theorem8.5.2 (draft p163), and the integral (1,1) characterization in Remark7.3.8. Its author errata were also consulted; none of the entries concern these uses. Do not treat the rest of that book or any theorem of Popovici as an input. No result of Popovici is used here.

Checks: Verify all signs in d^c and the Chern curvature, the global meaning of t and its differentials, compactness, the vertical and horizontal splitting, fiber period and volume constants, and the smooth mass integration by parts. The canonical-bundle formula must respect both line-bundle trivializations and the quotient action. c being nonzero must be distinguished from its real class, with the equivalence established using primitivity. In the variance argument p need not be monotone; preserve the positive distributional atom when smoothing the extremal profile. Check T=2M and the strict inequalities. In Proposition3 the cohomological amplitude condition gives only a lower bound for the separated class; do not turn it into a sufficient pointwise condition or claim sharpness there. Pointwise amplitude suffices only in the purely radial class. Check the average kappa versus maximum lambda. In Proposition4 verify that a primitive square-minus-four class can be the entire Picard group, that adjunction excludes every irreducible curve including singular curves, that a Kähler class orthogonal to it exists, and that the projection/Stokes argument excludes all divisors of the total space. Do not infer v_->0 or v_-=0 from any of these results.

Proof:

# Primitive elliptic bundles

Conventions: d^c=i/(4*pi)(bar-partial minus partial), dd^c=i/(2*pi) partial bar-partial. A closed Kähler current is a closed positive (1,1)-current dominating a Hermitian form times a positive constant. Lower and upper masses are the infimum and supremum over bounded admissible potentials; for a Hermitian background they equal the corresponding extrema over smooth strictly admissible potentials, by the book's already proved exact-background regularization. No lower-mass assumption is made.

## Proposition 1: geometry and upper mass

Let (B,eta) be a connected compact Kähler surface, and let L be a holomorphic line bundle with integral_B c_1(L) wedge eta=0. For q>1 set X=L^times/<w -> qw> and pi:X->B. There is a smooth Hermitian metric h_L on L such that, with t=log|w|_(h_L)^2 on L^times,

dd^c t=pi^*c, eta wedge c=0, D=dt wedge d^c t, omega=pi^*eta+D.

The form c is a smooth closed real (1,1)-representative of -c_1(L). The forms dt,d^c t,D and omega descend. The space X is a connected compact complex threefold, omega is Hermitian, and, writing T=2 log q and A=integral_B eta^2,

d(omega^2)=0, dd^c omega=-pi^*(c^2)>=0, integral_X omega^3=3TA.

For every smooth real u,

integral_X(omega+dd^c u)^3=3TA-3 integral_X du wedge d^c u wedge (-pi^*c^2).

In particular v_+(omega)=3TA. Moreover K_X is holomorphically isomorphic to pi^*K_B. If c_1(L) is nonzero in real cohomology, X has no pluriclosed Hermitian metric and no closed Kähler current. If c_1(L) is zero in real cohomology, the chosen omega is Kähler.

Proof. Start with any smooth metric on L, with c_0=dd^c log h_L in a holomorphic frame; this represents -c_1(L). Its eta-trace has mean zero by the assumed degree condition. The scalar Poisson equation on the compact Kähler surface supplies a smooth real phi with tr_eta dd^c phi=-tr_eta c_0. Replacing h_L by e^phi h_L makes c=c_0+dd^c phi primitive.

The action w->qw is free and properly discontinuous, because t increases by T>0. The closed strip 0<=t<=T is compact: it is the annulus of bundle norms between 1 and q over the compact base. It meets every orbit. The quotient is therefore compact. A line-bundle trivialization identifies pi locally holomorphically with the projection U times (C^*/q^Z)->U. Connectedness follows from connectedness of base and fiber. Although t changes by T, its differentials descend. The form D=i/(2*pi) partial t wedge bar-partial t has rank one and is positive on the vertical complex line. Its kernel projects isomorphically to TB, so omega>0.

Put a=dt,b=d^c t on X. We have da=0, db=pi^*c, d^c a=-pi^*c and d^c b=0. Therefore D^2=0, dD=-a wedge pi^*c, and dd^c D=-pi^*(c^2). The primitivity condition makes d(omega^2)=-2 pi^*(eta wedge c) wedge a=0. At a point of B the eigenvalues of c relative to eta are lambda and -lambda. Consequently c^2=-lambda^2 eta^2, proving the sign of dd^c omega.

In a logarithmic fiber coordinate z=x+i*y the real periods are log q and 2*pi. On the fiber t=2x+constant and D=pi^(-1) dx wedge dy, so integral_E D=T. Since omega^3=3 pi^*(eta^2) wedge D, fiber integration proves the total volume formula.

For the mass identity, expand the cube. The term 3 integral_X dd^c u wedge omega^2 vanishes because omega^2 is closed. The term integral_X(dd^c u)^3 vanishes because dd^c u is exact and closed. Writing S=dd^c omega=-pi^*c^2, two integrations by parts give

integral_X(dd^c u)^2 wedge omega=integral_X u dd^c u wedge S=-integral_X du wedge d^c u wedge S.

Here S is closed, so the last equality also follows directly from integration of d(u d^c u wedge S). This proves the identity. Since S is semipositive, all smooth strictly admissible masses are at most 3TA, and the zero potential attains it. The already established equality of bounded and smooth extrema gives v_+(omega)=3TA.

If c is exact, Stokes gives integral_B c^2=0. The pointwise identity c^2=-lambda^2 eta^2 then makes c=0. Conversely c=0 certainly represents the zero real class. Thus a nonzero real Chern class gives a nonzero smooth semipositive form S. Pairing S with any hypothetical pluriclosed metric gamma gives a strictly positive integral but also integral_X gamma wedge S=integral_X omega wedge dd^c gamma=0. Pairing with a hypothetical closed positive current R>=epsilon omega likewise gives a positive integral and integral_X R wedge S=integral_X omega wedge dd^c R=0. These are pairings with smooth forms, not singular products. Both are contradictions. If c=0, d omega=0 and omega is Kähler.

Finally, in a local holomorphic frame of L use the nonzero fiber coordinate w. If sigma is a local holomorphic base two-form, then pi^*sigma wedge dw/w is invariant under w->qw. Changing the frame changes dw/w by a horizontal holomorphic one-form, whose wedge with sigma vanishes. Changing sigma has exactly the transition function of K_B. These local nowhere-zero identifications prove K_X=pi^*K_B.

## Lemma 2: a periodic variance bound

For M,T>0 let p be a smooth real T-periodic function with zero mean, |p|<M and p'>-1. Define

F(M,T)=T^2/12 if T<=2M, and F(M,T)=M^2-4M^3/(3T) if T>=2M.

Then (1/T) integral_0^T p^2 < F(M,T). The supremum of the left side over this smooth class is F(M,T).

Proof. The zero function is immediate. Otherwise put a=max p>0,b=-min p>0,r=a+b. Choose a forward interval I of length ell<=T from a maximum to a subsequent minimum. Since -p'<1, integration gives r<ell<=T; also r<2M. Let G(s)=(a-s)(s+b). It is nonnegative on [-b,a], and G(p)>=-G(p)p'. The mean-zero identity and the endpoint values give

ab T-integral_0^T p^2=integral_0^T G(p)>=-integral_I G(p)p'=integral_(-b)^a G(s) ds=r^3/6.

This uses no monotonicity of p. Since ab<=r^2/4, the average square is at most r^2/4-r^3/(6T). This expression is strictly increasing for 0<r<T. Evaluating its supremum at min(2M,T) gives the displayed F and the strict inequality.

For sharpness, when T>=2M let a_0=(T-2M)/2 and define a periodic profile p_0 equal to M on [0,a_0), equal to M-(s-a_0) on [a_0,a_0+2M), and equal to -M on [a_0+2M,T). When T<=2M use p_0(s)=T/2-s on [0,T). The definitions agree at equality. Both profiles have mean zero and |p_0|<=M, and their distributional derivatives on the circle are >=-1: the period join contributes a positive atom. Direct integration gives average square F(M,T). For a nonnegative smooth periodic approximate identity rho_epsilon of integral one, put p_epsilon=(1-epsilon)(p_0*rho_epsilon). It has zero mean, |p_epsilon|<M, p_epsilon'>=-1+epsilon, and tends to p_0 in L2. This proves sharpness.

## Proposition 3: separated and purely radial potentials

In Proposition 1 assume c_1(L) is nonzero in real cohomology and put kappa=(-integral_B c^2)/A>0. Every smooth strictly omega-psh potential u=f(t)+pi^*v, with f T-periodic and v smooth real on B, satisfies

integral_X(omega+dd^c u)^3 > 3TA(1-kappa F(kappa^(-1/2),T)) > 0.

No sharpness is claimed for this general separated class. For the purely radial subclass v=0 the exact infimum instead is

3TA(1-kappa F(M_0,T))>0, where M_0=1/max_B lambda and c^2=-lambda^2 eta^2, lambda>=0.

This infimum is approached by smooth strictly admissible radial potentials and is not attained in that class.

Proof. Put p=f'. It has mean zero. The chain rule gives

omega+dd^c u=pi^*(eta+p c+dd^c v)+(1+p')D.

For each value of t modulo T every base point has a point of that value above it. Restriction to the vertical line gives p'>-1, and restriction to ker partial t gives positivity of eta+p c+dd^c v on B for each value of p. The latter form is closed, and its square has integral A+p^2 integral_B c^2=A(1-kappa p^2), since integral eta c=0 and all exact terms disappear by Stokes. Thus |p|<kappa^(-1/2).

Only the vertical derivative of u contributes to the mass identity in Proposition 1. The fiber formula integral_E F_0(t)D=integral_0^T F_0(s)ds for periodic F_0 gives

integral_X(omega+dd^c u)^3=3TA(1-(kappa/T) integral_0^T p^2).

Apply Lemma 2 with M=kappa^(-1/2). Its explicit formula gives F(M,T)<M^2, so the lower bound is positive.

For v=0, diagonalization of c against eta shows that the horizontal positivity condition is exactly |p|<M_0. Indeed each base point sees every p, and the eigenvalues are 1+p lambda and 1-p lambda. Conversely that condition together with p'>-1 makes the full form positive in the adapted horizontal-vertical decomposition. Also kappa is the eta^2-average of lambda^2, so kappa<=M_0^(-2). Lemma 2 and the exact mass formula prove the asserted positive infimum and strict nonattainment. Its smooth sharpness profiles have mean-zero derivatives, hence smooth periodic primitives f_epsilon; taking u_epsilon=f_epsilon(t) proves attainability as an infimum.

## Proposition 4: a K3 test with no divisors

There is a K3 surface B with Pic(B)=Z[L], c_1(L)^2=-4, and a Kähler form eta with integral_B c_1(L) eta=0. It has no compact complex curves. The corresponding X of Proposition 1 has trivial canonical bundle, is balanced, has finite upper mass, admits no pluriclosed metric or closed Kähler current, and has no divisors. Every compact irreducible curve in X is an elliptic fiber.

Standard K3 inputs: every complex K3 surface is Kähler; the K3 lattice is 3U plus 2E8(-1); every period line satisfying sigma^2=0 and sigma bar-sigma>0 occurs; integral (1,1) classes are Chern classes of holomorphic line bundles and Pic^0(B)=0; the intersection form on H^(1,1)(B,R) has signature (1,19); the Kähler cone is the component of the positive cone cut out by positivity on smooth rational curves; adjunction gives C^2=2p_a(C)-2>=-2 for an irreducible curve on a K3 surface. The first two and the cone assertion were checked at Huybrechts's author-hosted K3Global.pdf, Theorem7.4.1 (draft page134) and Theorem8.5.2 (draft page163); this uses them as standard reference inputs, not as newly proved statements. No result of Popovici is used.

Proof. In a hyperbolic plane with basis e,f and e.f=1, choose ell=e-2f, so ell is primitive and ell^2=-4. Choose a period in ell^perp avoiding the hyperplanes perpendicular to every integral vector outside Z ell. Such periods exist: ell^perp has signature (3,18), its period domain is nonempty, and each excluded hyperplane is proper; there are countably many of them. The period theorem and the integral (1,1) description give Pic(B)=Z[L] with c_1(L)=ell under the marking. An irreducible curve cannot have zero class because its Kähler area is positive. Any other possible class m ell has square -4m^2<-2, contradicting adjunction. Thus B has no curves.

The orthogonal complement of ell in H^(1,1)(B,R) has signature (1,18), so it contains a class of positive square. Choose its sign in the positive component containing Kähler classes. There are no rational curves, so the Kähler-cone theorem makes this class Kähler. Choose eta representing it. Proposition 1 now gives all the stated metric and canonical-bundle properties.

It remains to check analytic subsets of X. If an irreducible divisor Z dominated B, the proper map pi|_Z would be generically finite of positive degree m. Projection of integration currents would give pi_*[Z]=m, and therefore

integral_X [Z] wedge (-pi^*c^2)=m integral_B(-c^2)>0.

The left side is zero by Stokes, because -pi^*c^2=dd^c omega and [Z] is closed. Thus no divisor dominates B. The proper image of any other divisor would be a curve or a point. There are no curves on B, and a fiber has dimension one, so it cannot contain a divisor of X. There are no divisors. Similarly, the proper image of an irreducible compact curve is a point, so that curve is contained in a fiber and equals it.

Research boundary: None of these statements determines v_-(X). In particular, the positive bound for separated potentials is not a positive-lower-mass theorem for X. The known averaging of compact rational curves cannot supply transverse horizontal directions on this K3 example. Whether unrestricted lower mass vanishes here is a question unresolved in this project, not a claimed globally open problem.
