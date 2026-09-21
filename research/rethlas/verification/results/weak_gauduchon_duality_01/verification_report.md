# Verification report: weak_gauduchon_duality_01

## Verdict

**Correct.** No critical errors or gaps were found in the submitted proof. The earlier manuscript results identified by the user are accepted inputs; their definitions and applications have been checked.

The entire proof is correct under the stated accepted manuscript inputs and the manuscript convention that X is connected, compact and without boundary. All 15 sequential audit items pass, with no critical errors or gaps.

The trace normalization and cofactor calculation give the exact 1/n factors. The determinant is taken on matrix densities relative to the full trace measure, including singular parts; no wedge of nonsmooth currents is used. The continuous-test dual infimum is justified by the regularized matrices, global Lusin–Tietze bundle approximation, spectral truncation, determinant normalization and dominated convergence, including rank-deficient densities. Concavity, homogeneity and upper semicontinuity follow.

The compact maximum equals exp(-B0(F)/n) and agrees with the smooth supremum. Distributional Stokes bounds every current, conformal Gauduchon metrics attain equality for smooth F, and equality plus elliptic regularity and the accepted adjoint kernel proves uniqueness among all currents in that case. The distributional regularity step also matches [Dyatlov, Theorem 14.2](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf). Uniform approximation of F establishes the continuous-data formula without approximating arbitrary currents.

The two signed multipliers prove weighted-measure continuity for near-maximizers. Measure concavity and equal masses prove affineness on maximizers. Jensen gives the supporting inequality; the uniform Taylor expansion and compactness yield the right derivative with the correct negative-maximum sign. Weak-* Hahn–Banach separation proves that every supporting probability is represented. Absolute continuity of the weighted measures follows only from the accepted theorem for A0(F). No absolute continuity of the currents, continuous-F uniqueness, weak linearized Monge–Ampere operator, or global mass hypothesis is asserted or used.

The complete deduction-by-deduction audit and reference checks are saved in results/weak_gauduchon_duality_01/verification_report.md and the run memory.

## Sequential verification

The proof was read in its written order. Each numbered deduction below was checked directly; no independent proof items were delegated or reordered.

### 1. sec:weak-gauduchon-duality — setting, compactness and topology

**Status:** checked; no errors or gaps.

1. The manuscript convention (book/author/conventions.tex:3), read as mathematical context, makes X connected, compact and without boundary; omega means a smooth strictly positive real (1,1)-form. This supplies compactness, Stokes without boundary and the connectedness used in the later kernel argument.
2. Gauduchon's accepted theorem supplies a smooth gamma>0 with ddc(gamma^(n-1))=0. Its positive finite omega-trace can be divided out, so G_omega is nonempty.
3. Positive (n-1,n-1) currents have matrix coefficient measures. Strict positivity of omega and finitely many relatively compact frame charts bound the total variation of every coefficient by a uniform multiple of int omega wedge T=1.
4. Bounded coefficient measures have weak-* convergent subnets, and sequential subsequences since the continuous section space over compact metrizable X is separable. Positivity is closed; the trace constraint is tested by the fixed smooth omega; ddc-closedness is tested by smooth ddc phi. All pass to limits.
5. Convex combinations preserve positivity, ddc-closedness and trace one.
6. Uniform approximation of continuous test forms by smooth ones, together with the uniform coefficient variation bound, shows that current convergence and convergence against continuous coefficient forms agree on this bounded set. This also justifies the later sequential compactness arguments.

### 2. eq:weak-gaud-functional — trace density and finite measure

**Status:** checked; no errors or gaps.

1. Each coefficient is absolutely continuous with respect to sigma_T=omega wedge T by positivity. Radon-Nikodym applied in frames gives a measurable positive semidefinite Hermitian density.
2. The density is normalized by beta wedge T=(1/n)tr(B P_T) sigma_T. Taking beta=omega, hence B=I, gives tr P_T=n sigma_T-almost everywhere. Thus every eigenvalue lies in [0,n].
3. The pairing uniquely determines P_T up to sigma_T-null sets. Under an omega-unitary change of frame the matrix is conjugated, so its determinant is a well-defined measurable scalar.
4. f_F=(e^F dV/omega^n)^(1/n) is positive continuous and bounded on compact X. Matrix AMGM gives 0<=det(P_T)^(1/n)<=tr(P_T)/n=1, whence Gamma_F(T) is a finite positive measure with mass at most ||f_F||_infinity.
5. The matrix density is taken relative to the entire trace measure, including its part singular to smooth volume. No absolute continuity with respect to dV is assumed, and no multiplication or wedge of nonsmooth currents occurs.
6. Rank-deficient density matrices have determinant zero, so Gamma may vanish for an individual current without obstructing the definitions.

### 3. sec:weak-gauduchon-duality — consistency for smooth powers and scaling

**Status:** checked; no errors or gaps.

1. For T=gamma^(n-1) and the matrix G of gamma relative to omega, the coefficient matrix for the pairing relative to omega^n is S=adj(G)=det(G)G^(-1): beta wedge gamma^(n-1)=(1/n)tr(BS)omega^n.
2. Consequently sigma_T=(tr S/n)omega^n and P_T=nS/tr S. Therefore det(P_T)^(1/n) sigma_T=det(S)^(1/n)omega^n, with no missing n or factorial.
3. det S=(det G)^(n-1) and det G=gamma^n/omega^n. Multiplication by f_F gives exactly (e^F dV/gamma^n)^(1/n)gamma^n.
4. For c>0, sigma_(cT)=c sigma_T while P_(cT)=P_T; hence both Gamma and D scale by c. At T=0 the value is zero. The same density prescription therefore extends to arbitrary finite positive trace mass.
5. For n>=2, scaling the positive form gamma by c^(1/(n-1)) produces c gamma^(n-1); the normalized smooth members used later are well defined. The equality with the previously defined smooth denominator is exact even when e^F dV is not normalized.

### 4. lem:weak-gaud-determinant-dual — finite dimensional infimum, including singular matrices

**Status:** checked; no errors or gaps.

1. For P>=0 and Q>0 with det Q=1, Q^(1/2)P Q^(1/2)>=0 has trace tr(QP) and determinant det P. AMGM yields tr(QP)/n>=det(P)^(1/n), without assuming QP itself Hermitian.
2. Q_epsilon=det(P+epsilon I)^(1/n)(P+epsilon I)^(-1) is positive definite and has determinant one.
3. Writing the eigenvalues of P as lambda_i gives tr(Q_epsilon P)/n=[prod_i(lambda_i+epsilon)]^(1/n) sum_i lambda_i/(lambda_i+epsilon)/n.
4. When P>0 this expression tends to det(P)^(1/n); when P is singular the product prefactor tends to zero while the sum of ratios is at most n. This includes P=0.
5. If tr P=n, AMGM bounds the prefactor by 1+epsilon, and the average of ratios is at most one. Hence the entire trace expression is bounded by 1+epsilon.
6. The test set for continuous beta is nonempty: beta=f_F omega has beta^n=e^F dV. For every admissible beta its matrix is f_F Q with Q positive continuous and det Q=1, so the pointwise lower bound integrates to D_F(T)<=int beta wedge T.

### 5. lem:weak-gaud-determinant-dual — global continuous approximation and determinant normalization

**Status:** checked; no errors or gaps.

1. Since 0<=P_T<=nI, for fixed epsilon>0 the eigenvalues of Q_epsilon lie between epsilon/(n+epsilon) and (1+epsilon)/epsilon. Thus it is a measurable section of a compact positive interval in the bundle of omega-Hermitian endomorphisms.
2. Choose a finite trivializing cover with an omega-unitary frame on each chart and a subordinate partition of unity with compact supports in those charts. Apply Lusin to the matrix entries on these supports, losing arbitrarily little sigma_T mass in each chart. This works for an arbitrary finite Radon measure, including singular and atomic parts.
3. On the Lusin compact sets the field is continuous. Tietze extension of real coordinates in the Hermitian matrix space produces continuous local Hermitian fields; multiplication by the partition functions and summation gives a global continuous Hermitian section. Where every contributing chart is in its Lusin compact set, the sum equals Q_epsilon. The bad set has arbitrarily small sigma_T measure.
4. The intrinsic spectral truncation A -> min(M_epsilon,max(m_epsilon,A)) is continuous, is equivariant under unitary changes of frame, and fixes Q_epsilon. It gives a global continuous positive field in the fixed positive interval. Uniform boundedness and the small exceptional measure yield L1(sigma_T) convergence.
5. The map N(A)=A/det(A)^(1/n) is continuous and uniformly continuous on that compact positive interval; its output has determinant one and eigenvalues uniformly bounded above and away from zero. Since N(Q_epsilon)=Q_epsilon, convergence in measure plus boundedness, or a uniform-continuity split, gives L1 convergence of the normalized approximants.
6. For the associated beta_k=f_F Q_k, beta_k^n=e^F dV holds pointwise. The trace pairing converges because |tr((Q_k-Q_epsilon)P_T)|/n <= ||Q_k-Q_epsilon||_op and f_F is bounded.
7. Taking k to infinity shows that the infimum over continuous admissible beta is at most the measurable Q_epsilon trace integral. For 0<epsilon<=1 the integrands are bounded by 2f_F, and the preceding eigenvalue calculation gives pointwise convergence including rank-deficient P_T. Dominated convergence proves the reverse inequality and hence the asserted infimum formula.
8. No uniform bound independent of epsilon is needed on the approximating forms themselves: approximation is first completed for each fixed epsilon, followed by epsilon tending to zero.

### 6. lem:weak-gaud-determinant-dual — arbitrary mass, concavity, semicontinuity and intrinsic meaning

**Status:** checked; no errors or gaps.

1. The density proof uses only positivity and finite trace, not ddc-closedness. Dividing a nonzero positive finite-mass current by its trace reduces the assertion to trace one; positivity of omega ensures zero trace implies the zero current.
2. Every beta in the infimum is fixed and continuous, so T -> int beta wedge T is continuous linear in the specified weak topology. An infimum of continuous linear functionals is concave and upper semicontinuous, and is positively homogeneous on the positive cone.
3. The infimum is finite and has a common nonempty test class determined solely by beta>0 and beta^n=e^F dV. Thus the value does not depend on frames or on the auxiliary metric used for its matrix-density expression.
4. If metric independence is read as including Gamma itself, apply the intrinsic formula to chi T for every continuous chi>=0: Gamma_F(chi T)=chi Gamma_F(T) by degree-one homogeneity. Equality of all these localized masses gives equality of the measures computed in different auxiliary metrics.
5. This independence does not assert that the constraint set G_omega is unchanged if its normalizing background omega is changed; omega remains fixed in that constraint. Only the expression of the same current's functional or measure is auxiliary.

### 7. thm:weak-gaud-compact-duality — scalar convention, attainment and smooth dual equality

**Status:** checked; no errors or gaps.

1. B0 is the logarithm of the scalar multiplying e^F dV in the zero-reference equation, as assumed by the user and defined in the normalization chapter. It is not the scalar itself, nor a normalization of e^F dV to a probability.
2. Upper semicontinuity on nonempty compact G_omega gives a maximum. It is finite by the bound ||f_F||_infinity and strictly positive by testing a smooth strictly positive normalized Gauduchon power.
3. The maximizer set is closed by upper semicontinuity and convex by concavity, hence nonempty compact convex.
4. For smooth F the accepted equation supplies smooth u and Omega=omega+ddc u>0 with Omega^n=e^(B0(F)+F)dV. The smooth form beta=e^(-B0(F)/n)Omega satisfies beta^n=e^F dV exactly.
5. The dual infimum gives D_F(T)<=int beta wedge T for every current in G_omega. Distributional Stokes pairs the smooth u with ddc T=0, so int ddc u wedge T=0. Hence the upper bound is e^(-B0(F)/n) for every such current, with no current product or global Monge-Ampere mass hypothesis.
6. Choose the accepted Gauduchon conformal representative gamma=e^g Omega. Its cofactor matrix is a positive scalar multiple of the inverse matrix of Omega, so the AMGM equality condition holds at every point for T proportional to gamma^(n-1).
7. Dividing gamma^(n-1) by its positive trace integral gives an element of G_omega attaining the upper bound. Thus the maximum and smooth supremum equal e^(-B0(F)/n) for smooth data.

### 8. thm:weak-gaud-compact-duality — uniqueness among all currents for smooth F

**Status:** checked; no errors or gaps.

1. For a maximizing T, the pointwise nonnegative defect between the beta trace integrand and the determinant integrand has integral zero, so it vanishes sigma_T-almost everywhere.
2. The test matrix B is smooth positive definite. Equality in AMGM means B^(1/2)P_T B^(1/2)=lambda I. Since tr P_T=n, lambda>0; a rank-deficient P_T cannot satisfy equality. Thus P_T=n B^(-1)/tr(B^(-1)).
3. The cofactor direction of gamma^(n-1), for gamma conformal to Omega, is the same inverse-matrix direction. Therefore T=a gamma^(n-1) for a nonnegative scalar distribution represented by a finite measure relative to a fixed smooth volume. This does not yet assume that a is a function.
4. The scalar operator a -> ddc(a gamma^(n-1))/gamma^n has smooth coefficients and elliptic principal symbol since gamma>0. Its distributional kernel is smooth by elliptic regularity. Thus the possibly measure-valued coefficient a becomes a smooth function.
5. If L_gamma v=n ddc v wedge gamma^(n-1)/gamma^n, integration by parts gives L_gamma^* a=n ddc(a gamma^(n-1))/gamma^n with adjoint taken relative to gamma^n. The factor n has no effect on the kernel.
6. On the connected compact manuscript manifold, the accepted trace-kernel/index-zero argument makes ker L_gamma^* one-dimensional. The Gauduchon identity makes the constant function 1 belong to that kernel. Hence a is constant.
7. The normalization int omega wedge T=1 fixes a=1/(int omega wedge gamma^(n-1)), proving uniqueness among all positive currents, not just smooth competitors.

### 9. thm:weak-gaud-compact-duality — passage to continuous logarithmic densities

**Status:** checked; no errors or gaps.

1. For continuous F,G the same trace and matrix density occur in Gamma_F and Gamma_G, and f_F/f_G=e^((F-G)/n). This gives the displayed two-sided multiplicative bound for every T, including those with D_G(T)=0.
2. Taking maxima, or taking suprema over the fixed smooth positive normalized Gauduchon subclass, preserves these bounds.
3. Uniform approximation F_j -> F by smooth functions and the accepted uniform 1-Lipschitz property give B0(F_j)->B0(F).
4. Applying the multiplicative bounds to both the full maximum and the smooth supremum squeezes each to e^(-B0(F)/n), since the two coincide at every smooth F_j.
5. The approximation is of the prescribed logarithmic density alone. No density of smooth ddc-closed positive forms within all currents is used, and no convergence or regularity of weak solution potentials is needed.

### 10. lem:gaud-maximizer-measure-continuity — probability normalization and near-maximizer convergence

**Status:** checked; no errors or gaps.

1. For T in M(F), Gamma_F(T) is positive and has mass M(F)>0, so nu_(T,F)=Gamma_F(T)/M(F) is a probability.
2. If T_j -> T and D_F(T_j)->M(F), upper semicontinuity gives D_F(T)>=M(F); the maximality bound gives equality.
3. The measures Gamma_F(T_j) have uniformly bounded masses and thus weakly convergent subsequences on compact X. Testing with 1 shows each cluster point Gamma' has mass M(F), equal to Gamma_F(T)(X).
4. For each real h in C(X), choose epsilon>0 with epsilon||h||_infinity<1. The functions F_plus/minus=F+n log(1 plus/minus epsilon h) are continuous, and Gamma_(F_plus/minus)(S)=(1 plus/minus epsilon h)Gamma_F(S) for every current S.
5. Along a subsequence defining Gamma', upper semicontinuity of D_(F_plus/minus) gives int(1 plus/minus epsilon h)dGamma' <= int(1 plus/minus epsilon h)dGamma_F(T).
6. The equal masses cancel the constant terms. The plus sign gives int h dGamma' <= int h dGamma_F(T), and the minus sign gives the reverse inequality.
7. Therefore Gamma'=Gamma_F(T) for every cluster point, and compactness implies convergence of the full sequence. The weak topologies here are metrizable on the bounded sets, so this sequential statement also proves the claimed continuity on M(F).

### 11. lem:gaud-maximizer-measure-continuity — measure concavity and affineness on maximizers

**Status:** checked; no errors or gaps.

1. Let mu=sigma_(T1)+sigma_(T2), r_i=d sigma_(Ti)/d mu, and A_i=r_i P_(Ti), defined as zero where r_i=0. The pairing relative to mu has matrix A_i, and Gamma_F(T_i)=f_F det(A_i)^(1/n)mu by degree-one homogeneity.
2. The coefficient matrix of tT1+(1-t)T2 relative to mu is tA1+(1-t)A2. This formulation compares matrices with one common dominating measure, rather than incorrectly adding densities with respect to different trace measures.
3. The determinant root is concave on all positive semidefinite matrices, including boundary matrices, as follows directly from the earlier infimum of linear trace expressions; it is homogeneous of degree one.
4. Applying that matrix inequality mu-almost everywhere yields Gamma_F(tT1+(1-t)T2)>=tGamma_F(T1)+(1-t)Gamma_F(T2) as an inequality of measures.
5. If T1 and T2 maximize, concavity of D shows their convex combination also maximizes. Both sides then have mass M(F), so the nonnegative difference measure has mass zero and is identically zero.
6. Thus Gamma, and after division by the fixed M(F) also nu, is affine on M(F). Together with the preceding continuity and compactness of M(F), its image N(F) is nonempty weak-* compact convex.

### 12. thm:gaud-current-all-adjoints — Jensen inclusion into the supporting probability set

**Status:** checked; no errors or gaps.

1. For a maximizer T at F and any real continuous G, Gamma_G(T)=e^((G-F)/n)Gamma_F(T). Hence M(G)>=D_G(T)=M(F) int e^((G-F)/n)dnu_(T,F).
2. All masses and the exponential integral are strictly positive. Applying -n log reverses the inequality and uses B0(H)=-n log M(H), giving B0(G)<=B0(F)-n log int e^((G-F)/n)dnu_(T,F).
3. Jensen for the probability nu_(T,F) gives log int e^((G-F)/n)dnu >= (1/n)int(G-F)dnu. Multiplication by -n yields the second displayed inequality with the stated sign.
4. The resulting inequality is exactly the manuscript definition of A0(F): probabilities nu with B0(G)<=B0(F)-int(G-F)dnu for all G in C(X). Thus N(F) is contained in A0(F), with no differentiation of a weak potential.

### 13. thm:gaud-current-all-adjoints — uniform Taylor expansion and directional derivative

**Status:** checked; no errors or gaps.

1. For fixed real h in C(X), D_(F+th)(T)=int e^(th/n)dGamma_F(T). The exponential remainder satisfies |e^(th/n)-1-th/n| <= t^2||h||_infinity^2 e^(|t|||h||_infinity/n)/(2n^2).
2. Since Gamma_F(T)(X)<=||f_F||_infinity uniformly on G_omega, the integrated remainder is O(t^2) uniformly in every current T. No continuity of Gamma on the full current set is assumed.
3. For a maximizer at F the constant Taylor term equals M(F). Taking the member of the compact image N(F) that maximizes int h dnu gives the lower right difference-quotient bound (M(F)/n) max_(nu in N(F)) int h dnu.
4. For each t>0 choose T_t maximizing at F+th; existence was proved. With a=||h||_infinity/n, D_F(T_t)>=e^(-ta)M(F+th)>=e^(-2ta)M(F), and D_F(T_t)<=M(F). Thus these are near-maximizers at F.
5. For any sequence t_j down to zero, compactness gives a converging subsequence of T_(t_j). The preceding lemma gives convergence of its Gamma_F measures to that of a member of M(F).
6. Taylor expansion at the moving maximizer gives [M(F+th)-M(F)]/t <= (1/n)int h dGamma_F(T_t)+O(t), because [D_F(T_t)-M(F)]/t<=0. Applying the previous subsequence statement to a sequence attaining the limsup proves the matching upper bound.
7. Hence M'_+(F;h)=(M(F)/n)max_(nu in N(F))int h dnu. Since M(F)>0 and B0=-n log M, the logarithm derivative yields (B0)'_+(F;h)=-max_(nu in N(F))int h dnu. Both factors of n and M(F) cancel exactly.
8. Existence of the right derivative is proved by these bounds; the argument does not merely invoke a Danskin theorem whose continuity hypotheses might fail.

### 14. thm:gaud-current-all-adjoints — reverse inclusion, absolute continuity and final scope

**Status:** checked; no errors or gaps.

1. If nu belongs to A0(F), apply its defining supporting inequality to F+th with t>0 and divide by t: [B0(F+th)-B0(F)]/t <= -int h dnu.
2. Taking the right limit and using the derivative formula gives int h dnu <= max_(nu_tilde in N(F))int h dnu_tilde for every real continuous h. The inequality direction is correct.
3. N(F) is weak-* compact convex in C(X;R)^*. Hahn-Banach separation is applied with this weak-* topology, whose continuous linear functionals are evaluations at h in C(X;R). A point outside N(F) would violate exactly one of the inequalities just obtained. Therefore nu lies in N(F).
4. Combining both inclusions yields A0(F)={Gamma_F(T)/M(F):T in M(F)}, including every supporting probability rather than only limits produced by a chosen smooth approximation.
5. The user-accepted theorem thm:weak-adjoint-probabilities states that every member of A0(F) is absolutely continuous with respect to dV. Since M(F)>0, the equality of sets implies Gamma_F(T)<<dV for every maximizer.
6. Absolute continuity of Gamma is not used earlier and is not inferred solely from the uniform Lipschitz bound for B0. Neither sigma_T nor T is thereby asserted absolutely continuous: determinant weighting may vanish on rank-deficient singular trace densities.
7. Uniqueness of the supporting probability at continuous F is exactly constancy of the map T -> Gamma_F(T)/M(F) on M(F). Affineness and continuity do not assert constancy or injectivity, so neither supporting-probability uniqueness nor current uniqueness is claimed at continuous F.
8. All geometric objects constructed are finite positive currents and ordinary matrix-density measures. No product rho omega_u^(n-1), nonsmooth current wedge, or weak linearized Monge-Ampere operator is defined. No novelty assertion is made.

### 15. Whole proof — hypothesis and dependency audit

**Status:** checked; no errors or gaps.

1. Strict positivity of omega is essential for coefficient control by trace, a positive continuous f_F, unitary bundle frames, and the accepted smooth Hermitian equation; the proof is not silently extended to a merely semipositive background.
2. Compactness and absence of boundary are used for finite covers, bounded continuous functions, weak compactness, uniform smooth approximation and distributional Stokes; connectedness is used for the constant-kernel uniqueness conclusion. These are explicit manuscript conventions.
3. n>=2 matches the conformal Gauduchon theorem and the interpretation of normalized currents as (n-1)st powers; no dimension-one argument is silently substituted.
4. The smooth equation and Gauduchon theorem give the dual value and smooth equality case; elliptic regularity and accepted kernel constants give uniqueness. Uniform Lipschitz continuity of B0 identifies the continuous extension.
5. The accepted concavity of B0 is consistent with its supporting-probability convention but need not be separately invoked in the new derivative argument, which proves its requisite right derivative directly. This redundant availability is not a missing step.
6. The accepted absolute-continuity theorem for A0 is used only at the final consequence. Probability normalization of dV fixes the scalar convention; the new determinant construction itself also works with positive unnormalized e^F dV.
7. No global Monge-Ampere mass bound, current smoothing theorem, regularity of continuous-F solutions, or weak adjoint differential equation is assumed in any new deduction.
8. All proof paragraphs, both lemmas and both theorems have been checked in textual order; all displayed matrix, exponential, logarithmic, Jensen and derivative factors match.

## Reference verification

No external-paper citation occurs in the submitted text. Accepted manuscript results were checked against their local statements. The supplementary standard elliptic-regularity check followed the required arXiv-first, web-fallback sequence.

### R1. Whole proof — reference inventory and accepted-input policy

**Status:** checked.

**Statement:** The proof refers to manuscript chapters chap:normalization and thm:weak-adjoint-probabilities and invokes smooth Hermitian Monge-Ampere solvability, Gauduchon's theorem, and its elliptic adjoint kernel.

**Context:** No external-paper citation occurs in the submitted new proof. The user explicitly accepts the earlier manuscript results; these are checked for exact definitions and applicability rather than reopened. The standard elliptic distributional-regularity step is additionally checked through arXiv-first then primary-source web search. External bibliography items appearing inside the evidence chapters are not new dependencies requiring re-audit.

**Evidence:**

- [conventions.tex:3](/Users/mingchen/Non-Kahler/book/author/conventions.tex:3)
- [chapter_smooth_equations.tex:16](/Users/mingchen/Non-Kahler/book/author/chapter_smooth_equations.tex:16)
- [chapter_gauduchon.tex:17](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon.tex:17)
- [chapter_normalization.tex:136](/Users/mingchen/Non-Kahler/book/author/chapter_normalization.tex:136)
- [chapter_gauduchon_variational_volume.tex:10](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:10)

### R2. thm:weak-gaud-compact-duality — accepted smooth scalar and Gauduchon inputs

**Status:** matched_and_applicable.

**Statement:** For smooth real F there is smooth u and b with (omega+ddc u)^n=e^(F+b)dV and omega+ddc u>0; b=B0(F). Every Hermitian eta in dimension n>=2 has a smooth positive rho with ddc(rho eta^(n-1))=0; gamma=rho^(1/(n-1))eta. For a Gauduchon gamma the scalar adjoint kernel is constants.

**Context:** Manuscript X is connected compact without boundary. Hermitian means smooth strictly positive. ddc=(i/(2pi))partial barpartial, and volume is the nth power without 1/n!. The scalar is logarithmic and dV may be any smooth positive volume. Gauduchon means ddc(gamma^(n-1))=0, not d gamma=0 or d(gamma^(n-1))=0.

**Application:** The proof uses eta=Omega and gamma^(n-1)=rho Omega^(n-1), tests beta=e^(-B0/n)Omega, and applies the adjoint relative to gamma^n only after distributional elliptic regularity. All hypotheses and constants match.

**Evidence:**

- [chapter_smooth_equations.tex:6](/Users/mingchen/Non-Kahler/book/author/chapter_smooth_equations.tex:6)
- [chapter_smooth_equations.tex:16](/Users/mingchen/Non-Kahler/book/author/chapter_smooth_equations.tex:16)
- [chapter_normalization.tex:222](/Users/mingchen/Non-Kahler/book/author/chapter_normalization.tex:222)
- [chapter_gauduchon.tex:17](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon.tex:17)
- [chapter_gauduchon.tex:26](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon.tex:26)

### R3. sec:weak-gauduchon-duality — accepted smooth denominator

**Status:** matched_and_applicable.

**Statement:** D_mu(gamma)=int (mu/gamma^n)^(1/n)gamma^n and the smooth Gauduchon quotient is int omega wedge gamma^(n-1)/D_mu(gamma).

**Context:** The chapter uses the full nth power without factorial and normalizes mu to a probability. The denominator formula is homogeneous of degree 1/n in mu, so replacing mu by the positive unnormalized density e^F dV is legitimate; the new proof also derives the resulting identity directly.

**Application:** With trace-normalized T=gamma^(n-1), the exact cofactor calculation gives the stated denominator, and taking its maximum corresponds to the reciprocal of the smooth quotient infimum. The new proof derives the value from the accepted scalar equation rather than assuming it for singular currents.

**Evidence:**

- [chapter_gauduchon_variational_volume.tex:10](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:10)
- [chapter_gauduchon_variational_volume.tex:22](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:22)
- [chapter_gauduchon_variational_volume.tex:71](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:71)

### R4. thm:gaud-current-all-adjoints — exact B0 and A0 definitions, continuity and absolute continuity

**Status:** matched_and_applicable.

**Statement:** B_phi(F)=log c_phi(F) where MA_theta^ext(u)=c_phi(F)e^F dV; B_phi is concave and 1-Lipschitz. A_phi(F) consists of all Borel probabilities nu such that B_phi(G)<=B_phi(F)-int(G-F)dnu for every continuous G. Every member of A_phi(F) is absolutely continuous with respect to dV.

**Context:** The user explicitly accepts these inputs for strictly positive omega and reference zero. This specialization is consistent with the chapter: omega is semipositive and big, 0 is its model envelope, and P_(epsilon omega)(0)=0. No bounded-mass assumption appears in the chapter setting. The probabilities are negatives of supergradients; their supporting inequality uses a minus sign.

**Application:** The Lipschitz input is used in the continuous-F extension. Jensen gives precisely the all-G supporting inequality, and the derivative/separation argument uses the same sign. Only after equality of sets is proved does the accepted absolute-continuity result imply Gamma_F(T)<<dV. There is no claim of T<<dV or an Lp bound.

**Evidence:**

- [chapter_normalization.tex:16](/Users/mingchen/Non-Kahler/book/author/chapter_normalization.tex:16)
- [chapter_normalization.tex:30](/Users/mingchen/Non-Kahler/book/author/chapter_normalization.tex:30)
- [chapter_normalization.tex:83](/Users/mingchen/Non-Kahler/book/author/chapter_normalization.tex:83)
- [chapter_normalization.tex:136](/Users/mingchen/Non-Kahler/book/author/chapter_normalization.tex:136)
- [chapter_normalization.tex:143](/Users/mingchen/Non-Kahler/book/author/chapter_normalization.tex:143)

### R5. thm:weak-gaud-compact-duality — standard distributional elliptic regularity

**Status:** matched_and_applicable.

**Statement:** If L is a linear elliptic differential operator with smooth coefficients on a smooth manifold and a is a distribution such that La is smooth, then a is smooth. In particular, a distributional solution of ddc(a gamma^{n-1})=0 for a smooth positive Hermitian metric gamma is smooth.

**Context:** This theorem applies to distributions for elliptic differential operators with smooth variable coefficients on a manifold. Ellipticity means nonvanishing principal symbol at every nonzero real covector; it does not require analyticity or self-adjointness.

**Application:** After dividing by gamma^n, a -> ddc(a gamma^(n-1)) is a smooth scalar second-order operator with definite principal symbol because gamma is strictly positive. Its value on a is zero. The theorem therefore makes a smooth before the accepted adjoint-kernel argument is applied.

**arXiv comparison:** The three returned results require analytic coefficients, or an already smooth solution of a nonlinear equation. They do not match the smooth-variable-coefficient distributional regularity statement and are not used. Search results: 1811.08623, Theorem 2.8; 2401.01446, Corollary 6.7; 2206.04954, Theorem 5. These search mismatches are not flaws in the submitted proof.

**Primary web evidence:** [Semyon Dyatlov, Theorem 14.2 (Elliptic Regularity III), p.181; Definition 14.1.](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).

## Findings and scope

- Critical errors: none.
- Gaps: none.
- Repair hints: none required.
- Book files were not edited.
- The verdict concerns the new deductions under the user-accepted earlier results, not a re-verification of those earlier proofs.
- Current uniqueness is proved for smooth F only. The final continuous-F uniqueness question and any weak linearized operator remain outside the proved conclusions.

## Persistence

The run memory contains 15 statement-check records, five reference-check records, the verification report and workflow events. The failed-check channel is empty because no mathematical issue was detected. Two transient approval-review timeouts during memory appends were resolved by the permitted single retries and introduced no duplicates.

