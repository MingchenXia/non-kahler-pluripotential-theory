# Dimension-independent kernel probability stability — checkpoint 431

The 430 parameter formulas concern a fixed selected space. Normalizing its kernel by its dimension exposes estimates uniform in that dimension, without an assumption on the background curvature or growth degree. This review reconstructs those estimates directly. No external new theorem or novelty claim is needed.

## Symmetric coherent-state coupling

Keep the compact selected-space setting of Section26.1. Fix m and a real continuous weight v with N=dim V_m>0. Put mu_v=B_v nu/N. For a weighted orthonormal basis s_i choose local unit fiber covectors and write F_i(x)=exp(-mv(x)/2) ell_x(s_i). Then B_v(x)=sum_i |F_i(x)|^2. The function C(x,y)=sum_i F_i(x) conjugate(F_i(y)) depends on those phases, but |C(x,y)|^2 and each F_i(x) conjugate(F_j(x)) do not. Orthonormality gives integral |C(x,y)|^2 dnu(y)=B_v(x).

Consequently dJ_v(x,y)=|C(x,y)|^2 dnu(x)dnu(y)/N is a symmetric probability coupling of mu_v with itself. On the common zero locus B_v=0 and C(x,y)=0; this locus is mu_v-null. Off it, disintegration gives exactly the probability sigma_v,x of equation(26.5). Define Q_v f(x)=integral f(y) dsigma_v,x(y), with value zero on the common zero locus. Q_v preserves constants mu_v-almost everywhere and preserves the integral. Jensen's inequality and the invariant marginal show that it is a contraction on L2(mu_v). Symmetry of J_v makes it selfadjoint.

It is also positive semidefinite. For f in L2(mu_v), expansion of the squared kernel gives

    <Q_v f,f>_mu = (1/N) sum_ij |integral f F_i conjugate(F_j) dnu|^2 >= 0.

All matrix integrals exist: |F_i conjugate(F_j)|<=B_v and f is in L1(mu_v). The expansion is finite. Thus positivity does not require an interchange of an infinite series or a pointwise positive matrix inverse. Q_v is a Markov contraction; it is not claimed to be an orthogonal projection.

## Total-variation derivative

For a real q in C(X), the 430 diagonal formula gives the signed measure identity

    D mu_v[q] = m (Q_v q-q) mu_v.

The derivative is in total variation; the common zero locus contributes zero. The following elementary L1 estimate uses positivity of Q_v, not just a pointwise oscillation bound.

Let g=q-Q_vq, whose mean is zero, and A={g>0}, p=mu_v(A). Selfadjointness gives integral_A g dmu_v=<q,(I-Q_v)1_A>. On A the function 1_A-Q_v1_A is nonnegative; on its complement it is nonpositive. Subtract inf q, using integral(1_A-Q_v1_A)=0. Bounding q-inf q by osc(q)=sup q-inf q gives

    ||g||_L1 = 2 integral_A g
              <= 2 osc(q) [p-<1_A,Q_v1_A>]
              <= 2 osc(q) p(1-p)
              <= osc(q)/2.

The middle inequality follows by writing 1_A=p+(1_A-p): Q_v1=1, preservation of the mean kills the cross terms, and positivity gives <1_A,Q_v1_A>>=p^2. Indicators are legitimate L2(mu_v) functions. The convention is the full total-variation norm, so a signed density has norm integral of its absolute value; it is twice the common probability-distance convention.

Therefore ||D mu_v[q]||_TV<=m osc(q)/2. Along the segment from v to w, N and the selected space remain fixed. Integration of the total-variation derivative yields

    ||mu_w-mu_v||_TV <= min(2, m osc(w-v)/2).

This bound is uniform in the metric, continuous base weight, positive volume, dimension N and selecting potential, once the two measures use the same degree and space. It makes no comparison between different selecting ideals. For sequences of nonempty spaces, m osc(w_m-v_m)->0 is sufficient for the two probability sequences to have the same limit whenever either converges, including convergence in total variation. Additive constants cancel exactly.

## Uniform analytic radius at the microscopic scale

For fixed real v define F_{m,v}(f)=mu_{v+f/m} for real continuous f. Let rho=log(3/2). The compressed Gram operator is T(f)=P_v exp(-f) on V_m. For complex f with ||f||_infinity<rho, its inverse has norm at most two. The holomorphic continuation of the density is

    exp(-mv(x)-f(x)) ell_x(T(f)^(-1)k_v,x)/N.

The Riesz identity at the real base norm bounds its absolute value by 2 exp(||f||) B_v(x)/N. Hence ||F_{m,v}(f)||_TV<=3 on that complex ball, independently of m,N and v. Holomorphy in total variation follows from the finite-space diagonal argument at430 and the bounded linear passage to measures. This complex continuation is not a probability for a nonreal f.

For any complex constant c, T(f+c)=exp(-c)T(f); the density's opposite exponential factor cancels, so the continuation is invariant under constant shifts wherever both expressions are defined. For real q, shift by c=(sup q+inf q)/2. Cauchy's estimate along the resulting complex parameter line gives, for every k>=1,

    ||d^k mu_{v+tq}/dt^k at t=0||_TV
        <=3 k! [m osc(q)/(2 rho)]^k.

The estimate is obtained on each circle of radius less than rho/(m||q-c||), then by taking the limit of these radii. Constant q gives an identically fixed probability and zero derivatives. This is a uniform radius in the rescaled weight f=m delta-v; it does not assert a radius uniform in m for unscaled weight increments or justify differentiating a limiting envelope.

## The inverse-degree scale can change a nonzero limit

Let Y be a connected compact complex manifold of positive dimension with a smooth positive probability nu_Y, and X=P1 times Y. Pull back O(1) with its Fubini--Study metric and select all sections. Compact connected fibers imply that every section descends; N_m=m+1. Use the product volume nu_FS times nu_Y, with nu_FS of mass one. The full base kernel is constant m+1: its norm and metric are invariant under the transitive unitary action on P1, and its integral is its dimension.

Choose a nonconstant real continuous q on Y and put v_m=q/m on X, Z_q=integral_Y exp(-q)dnu_Y and nu_q=exp(-q)nu_Y/Z_q. The weighted section norm is Z_q times the base norm. Thus, exactly for every m,

    B_{m,v_m}(b,y)=(m+1) exp(-q(y))/Z_q,
    mu_{m,v_m}=nu_FS times nu_q,
    mu_{m,0}=nu_FS times nu_Y.

The two probabilities have positive total-variation distance independent of m: equality would force exp(-q)/Z_q=1 almost everywhere, hence everywhere by continuity and positive volume, making q constant. With intrinsic normalization r=1 the kernel measures are (m+1)/m times these probabilities and have distinct nonzero limits. Ambient normalization in dimension 1+dim Y gives zero. Meanwhile v_m tends uniformly to zero and the kernel logarithmic potentials differ by (-q-log Z_q)/m, which also tends uniformly to zero. Thus uniform convergence of the norm weights or logarithmic kernel potentials alone does not determine these intrinsic measure limits. Y may be non-Kahler.

This directly restates the retained-fiber mechanism already present in Section26.11.3 in terms of an inverse-degree norm-weight perturbation. Its existing 189-line horizontal-kernel input was freshly read completely, together with the complete 283-line partial-kernel root and162-line parameter input reused at their actual430 scope. It does not settle the general approximation problem P20, classify all scaling thresholds in positive-curvature regimes or solve any other original problem.

## Reading and literature boundary

All eight current new/recent lists for math.CV, math.DG, math.AG and math.AP were retrieved successfully on5 October with show=2000; parsed entry counts equal the advertised totals. Their972 rows contain706 distinct IDs and mechanically match the424 scan, including titles, authors, versions and available listing abstracts. They still advertise2 October as the latest date and28 September--2 October in recent lists. There are no unseen IDs within those actual lists. This is a fresh retrieval/comparison, not a new706-paper complete abstract reading; historical replacement gaps remain open. No newly retrieved paper is adopted.

The automatic second complete mathematical read checks the phase cancellation, both marginals, finite Gram-square positivity, L2 domain, sign set and total-variation factor, constant shifts, the complex radius and its degree rescaling, exact product norm and nonzero intrinsic limit. It retains a fixed selecting space whenever a weight is varied. Next: integrate this directly proved stability supplement beside Section26.5.1, retaining the distinction between probability and intrinsic/ambient normalization.

All333 book files and1012 proof bodies, both catalogues/manifests,451 protected sources and six incoming author blobs remain exact. Package validation passes with2168 archive entries,2167 checksum-validated current payloads and330 book-source files matching the actual430 empty reconstruction. No new author build, empty reconstruction, native call or publication occurs.
