# Verification report: local homogeneous Dirichlet replacement

**Run:** local_homogeneous_dirichlet_01  
**Verdict:** correct under the accepted inputs  
**Findings:** 0 critical errors; 0 gaps  
**Coverage:** 56 sequential local deduction checks and 10 external applicability checks.

## Scope and accepted hypotheses

This report audits only the complete proof supplied for this run. It is independent of the local-big-continuity audit. The manuscript has not been edited.

- \(B=B_R\subset\mathbb C^n\), \(R>0\), \(n\ge1\), is a Euclidean coordinate ball.
- \(\theta\) is a smooth real \((1,1)\)-form near \(\overline B\). It may be nonpositive and nonclosed.
- \(dd^c=(i/(2\pi))\partial\bar\partial\) and \(\beta=dd^c|z|^2\).
- Admissibility means the current inequality \(\theta+dd^c u\ge0\) with the usual upper semicontinuous representative.
- Positivity and continuity of locally bounded admissible products under compact-local uniform convergence are accepted manuscript prerequisites.
- Scalar Poisson Dirichlet solvability, the linear elliptic maximum principle, and the submean characterization of plurisubharmonic functions are accepted.
- Guan–Li Theorem 1.1 is the one new external input. Its exact hypotheses and normalization are checked in Section 11.

The proof text was usable and was checked in its written order. In the deduction ledger below, ASCII names such as theta, beta, phi, epsilon, delta, ddc, and partial B denote the corresponding mathematical symbols in the proof. “Closed B” means \(\overline B\). Each item is an explicit check of the supplied deduction, with elementary details expanded where needed; none requires an additional unproved assertion.

## Sequential deduction ledger

### 1. Section setup and definitions

**Status:** checked; no critical errors or gaps.

**1.1. Arbitrary smooth real theta is permitted locally.**

Every local matrix, trace, and continuity argument is meaningful without dtheta=0 or positivity of theta. The sole external existence input has been verified as recorded in Section 11.

**1.2. Admissibility and products use the accepted definitions.**

theta-psh is the current inequality theta+ddc u>=0 with its usual upper semicontinuous representative. All constructed functions and competitors used below are continuous, hence locally bounded, so the accepted product theory applies.

**1.3. beta is a fixed positive translation-invariant form.**

With ddc=(i/(2pi)) partial barpartial, beta=(i/(2pi)) sum dz_j wedge dbar z_j. Matrix inequalities and determinant ratios are taken relative to this form.

### 2. Classical positive-density input, proof

**Status:** checked; no critical errors or gaps.

**2.1. Smooth extension of boundary data exists.**

Smooth sphere data extend using a collar and a smooth cutoff into the ball; all derivatives used below are bounded on the compact closure.

**2.2. The quadratic function is strictly admissible and has sufficient determinant.**

If theta+ddc tilde_phi >= -K beta on the closed ball, then theta+ddc under_v >= (A-K) beta. Choosing A>K+epsilon^(1/n) gives determinant strictly larger than epsilon beta^n, as well as positive definiteness. Equality of boundary values follows from |z|^2-R^2=0.

**2.3. Guan–Li applies for n>=2.**

The specialization is M=closed B, chi=theta, omega=beta, psi=epsilon, boundary datum phi/pi, and GL potential u=v/pi. It is algebraically exact because (i/2) partial barpartial (v/pi)=ddc v. The separate primary-source check in Section 11 confirms every existence hypothesis, including arbitrary chi, smooth boundary, and the constructed strict subsolution.

**2.4. n=1 follows from Poisson solvability.**

Writing theta=t beta, the equation is ddc v=(epsilon-t) beta, a scalar Poisson equation with smooth forcing and smooth Dirichlet data. The resulting background form equals epsilon beta>0.

**2.5. Uniqueness follows by linearization.**

For positive matrices A and B, log det A-log det B=int_0^1 tr(((1-t)B+tA)^(-1)(A-B)) dt. Here A-B is the complex Hessian of the difference with a fixed positive normalization. Positive smooth matrices on the compact closure give positive bounded elliptic coefficients for each pair of solutions. There is no zero-order term. Zero boundary difference and L(v1-v2)=0 imply equality.

### 3. Smooth comparison paragraph after the lemma

**Status:** checked; no critical errors or gaps.

**3.1. The determinant inequality has the claimed comparison sign.**

The same log-determinant linearization yields L(a-b)>=0, since det(theta+ddc a)>=det(theta+ddc b). With a-b<=0 on the boundary, the maximum principle gives a-b<=0.

**3.2. The segment stays elliptic.**

Convex combinations of positive definite Hermitian matrices remain positive definite. In every application the matrices are smooth and strictly positive on the relevant compact closure for each fixed epsilon. Uniformity as epsilon tends to zero is unnecessary for this maximum argument.

**3.3. Nonsmooth intersection boundaries do not obstruct comparison.**

This is a maximum principle for functions continuous on the closure of a bounded open set, not an existence or boundary-regularity theorem. It needs boundary inequalities, not smoothness of the boundary.

**3.4. Nonclosed theta causes no extra terms.**

At each point the backgrounds in A and B are identical and cancel in A-B. Linearization is in the matrix variable; no derivative or primitive of theta is used.

### 4. Homogeneous replacement theorem, uniform barriers

**Status:** checked; no critical errors or gaps.

**4.1. One fixed lower barrier works for all 0<epsilon<=1.**

Choose under_v with determinant>=beta^n. Its determinant is then >=epsilon beta^n and its boundary equals phi, so comparison gives under_v<=v_epsilon.

**4.2. Admissibility yields an epsilon-independent scalar Laplacian lower bound.**

The beta trace gives tr_beta(ddc v_epsilon)>=-tr_beta theta. In these coordinates tr_beta(ddc v)=Delta v/4, for the real Euclidean Laplacian. Thus one can choose C>=max(0,4 sup_closedB tr_beta theta).

**4.3. The upper barrier q exists and bounds v_epsilon from above.**

Accepted scalar Poisson solvability gives smooth q with Delta q=-C and q=phi on the sphere. Delta(v_epsilon-q)>=0 and zero boundary data imply v_epsilon<=q. q need not be theta-admissible.

**4.4. The boundary-distance estimate follows uniformly.**

Both under_v-tilde_phi and q-tilde_phi are smooth and vanish on the sphere. Their absolute values are <= their respective gradient suprema times dist(z,partial B), by integrating along a nearest radial segment. Sandwiching v_epsilon-tilde_phi between them proves the displayed absolute-value bound with one C1 independent of epsilon.

**4.5. The barriers give a common bound on the closed ball.**

under_v<=v_epsilon<=q and compactness give an epsilon-independent C0 bound. All boundary values equal phi.

### 5. Homogeneous replacement theorem, translated matrices and domains D_h

**Status:** checked; no critical errors or gaps.

**5.1. The background difference is bounded by C2 |h| beta.**

Write theta as a smooth Hermitian matrix in fixed Euclidean coordinates. The operator norm of its first derivative is bounded on the closed ball. The segment from z to z+h lies in the convex ball, so theta(z)-theta(z+h)>=-C2|h| beta. This compares translated coefficient matrices and requires no closedness.

**5.2. The corrected translate is strictly admissible.**

ddc w=ddc(v_epsilon composed with translation)+C2|h| beta. Hence theta(z)+ddc w is the translated positive matrix theta(z+h)+ddc v_epsilon(z+h) plus the positive semidefinite correction theta(z)-theta(z+h)+C2|h| beta.

**5.3. The determinant is at least epsilon beta^n.**

If A>=B>0, then B^(-1/2) A B^(-1/2)>=I, so det A>=det B. Translation preserves beta^n. This is pointwise Hermitian matrix monotonicity, not a comparison theorem for nonsmooth potentials.

**5.4. The two boundary cases exhaust partial D_h.**

For small |h|, the intersection of the two open balls is nonempty and its boundary is contained in the union of their spherical boundaries. Thus either z or z+h lies on partial B and both lie in the closed ball. The other point has boundary distance<=|h| by the reverse triangle inequality.

**5.5. The boundary estimate gives w<=v_epsilon on both spherical pieces.**

If z is on the sphere, v(z+h)-v(z)<=C1|h|+Lip(tilde_phi)|h|. If z+h is on the sphere, the same bound follows from the lower boundary-distance estimate at z. The quadratic term C2|h|(|z|^2-R^2) is nonpositive. Therefore C3>=C1+Lip(tilde_phi) works in both cases, including their common edge.

**5.6. Comparison gives the corrected translation inequality.**

w and v_epsilon are continuous on closed D_h, smooth and strictly admissible there for each fixed epsilon, det(theta+ddc w)>=det(theta+ddc v_epsilon), and w<=v_epsilon on the boundary. The previously proved smooth comparison applies despite the intersection's edge.

**5.7. The one-sided inequality is a uniform O(|h|) estimate.**

Rearranging w<=v_epsilon gives v_epsilon(z+h)-v_epsilon(z)<=(C2(R^2-|z|^2)+C3)|h|<=(C2 R^2+C3)|h|.

**5.8. Reversing translation gives the other sign.**

Apply the same construction with base point z+h and displacement -h; the constants are unchanged and z+h is in D_{-h}. The resulting reverse difference has the same upper bound. Set C4=C2 R^2+C3.

**5.9. Small-displacement estimates give a global Lipschitz bound.**

Subdivide the straight segment between two interior points into finitely many increments below the displacement threshold. All lie in B by convexity, and their lengths sum to the original distance. Summing yields the same C4. Approximate boundary points by interior points and use continuity to extend the estimate to the closed ball.

### 6. Homogeneous replacement theorem, zero-density limit for smooth boundary data

**Status:** checked; no critical errors or gaps.

**6.1. v_epsilon increases as epsilon decreases.**

For 0<epsilon1<epsilon2, v_epsilon2 has the larger determinant and the same boundary value. The comparison sign proved above gives v_epsilon2<=v_epsilon1.

**6.2. A finite pointwise limit exists on the whole closed ball.**

Monotonicity and the common upper barrier q give H_phi(z)=sup_{0<epsilon<=1} v_epsilon(z)<infinity, with the common lower barrier. On the sphere this supremum equals phi.

**6.3. The limit is Lipschitz.**

Pass to the pointwise limit in |v_epsilon(x)-v_epsilon(y)|<=C4|x-y|. The resulting inequality holds on the closed ball, so H_phi is Lipschitz and continuous there.

**6.4. Convergence is uniform for the entire family epsilon down to zero.**

For any tolerance choose a finite sufficiently fine net in the compact closed ball. Pointwise convergence at the finitely many net points holds simultaneously below one epsilon0. The common Lipschitz bounds for H_phi and v_epsilon control the errors between net points. This proves sup_closedB(H_phi-v_epsilon) tends to zero for all sufficiently small epsilon, not just a subsequence.

**6.5. The current inequality survives the limit.**

Uniform convergence implies distributional convergence of ddc v_epsilon to ddc H_phi. Pairing with each compactly supported positive test form preserves nonnegativity, so theta+ddc H_phi>=0.

**6.6. The homogeneous product equation follows.**

The common bounds give locally bounded potentials, and the convergence is uniform on each compact subset. The accepted local product-continuity prerequisite applies to theta+ddc v_epsilon. The measures epsilon beta^n tend weakly to zero on B, hence (theta+ddc H_phi)^n=0. No boundary or total-mass convergence is required.

**6.7. Smooth-data contraction holds before and after the limit.**

Set c=sup_partialB|phi-psi|. Adding c to v_epsilon,psi leaves its matrix and density unchanged and makes its boundary value >=phi. Comparison gives v_epsilon,phi<=v_epsilon,psi+c; interchanging phi and psi gives the reverse bound. Uniform limiting in epsilon proves the same norm inequality for H_phi and H_psi.

### 7. Homogeneous replacement theorem, extension to continuous boundary data

**Status:** checked; no critical errors or gaps.

**7.1. Smooth uniform approximants exist.**

Continuous functions on the compact smooth sphere can be approximated uniformly by smooth functions using finitely many charts, mollification, and a smooth partition of unity.

**7.2. The smooth replacements are uniformly Cauchy.**

The smooth-data contraction gives ||H_phi_j-H_phi_k||_closedB<=||phi_j-phi_k||_partialB, and the right side tends to zero.

**7.3. The limit is continuous with the exact boundary values.**

C(closed B) is complete under the uniform norm. The uniform limit is continuous, and restricting to the sphere gives lim phi_j=phi.

**7.4. The limit remains admissible and homogeneous.**

Uniform convergence preserves the current inequality as in step 6.5. The sequence and its limit are uniformly bounded on the compact closure, so the accepted product continuity applies. Every approximant's product vanishes on B, hence so does the limit's.

**7.5. The construction is independent of the approximation.**

For two smooth approximation sequences phi_j and phi'_j of the same phi, contraction bounds the difference of replacements by ||phi_j-phi'_j||, which tends to zero. Thus H_phi is well defined.

**7.6. Contraction extends to any two continuous data.**

Approximate phi and psi by smooth sequences, use their contraction, and pass to the uniform limits on the ball and sphere. Norms are continuous under uniform convergence.

### 8. Homogeneous replacement theorem, upper-test positivity for p_delta

**Status:** checked; no critical errors or gaps.

**8.1. Quadratic perturbation gives strict current positivity and unchanged boundary data.**

rho=|z|^2-R^2 satisfies ddc rho=beta, rho=0 on the sphere, and -R^2<=rho<=0. Thus p_delta=p+delta rho is continuous, has the same boundary trace as p, and theta+ddc p_delta>=delta beta.

**8.2. Freezing theta permits an arbitrarily small correction.**

For any eta>0, continuity of the Hermitian coefficients gives a ball around z0 contained in B such that theta(z0)-theta(z)>=-eta beta throughout it. This radius may shrink with eta; no fixed positive radius as eta tends to zero is required.

**8.3. The frozen form has a quadratic potential.**

In coordinates write theta(z0)=(i/(2pi)) sum T_jbar_k dz_j wedge dbar z_k with T Hermitian. Q0(z)=sum T_jbar_k (z_j-z0_j) conjugate(z_k-z0_k) is real and has ddc Q0=theta(z0). The constant matrix may be indefinite.

**8.4. The corrected local function is psh.**

Let F_eta=p_delta-delta|z|^2+Q0+eta|z-z0|^2. Its current Hessian is >=theta(z0)-theta(z)+eta beta>=0 on the chosen ball. F_eta is continuous and is the usual psh representative. Equivalently, mollify on smaller balls, use positivity of the mollified Hessians and their complex-line submean inequalities, then pass through local uniform convergence.

**8.5. A test for p_delta becomes a test for F_eta.**

If a>=p_delta locally with equality at z0, then A_eta=a-delta|z|^2+Q0+eta|z-z0|^2 satisfies A_eta>=F_eta locally and equality at z0.

**8.6. An upper test for a psh function has nonnegative complex Hessian.**

On every sufficiently small complex-line circle centered at z0, A_eta(z0)=F_eta(z0)<=mean F_eta<=mean A_eta. Taylor expansion of the C2 function A_eta and division by the square of the radius yield nonnegative Levi form in that line direction. All complex directions are allowed, so ddc A_eta(z0)>=0.

**8.7. Letting the correction tend to zero gives the exact matrix bound.**

The previous inequality is theta(z0)+ddc a(z0)-delta beta+eta beta>=0. The cone of positive semidefinite Hermitian matrices is closed, so eta down to zero yields theta(z0)+ddc a(z0)>=delta beta. This is a direct current-to-upper-test implication, with its proof supplied; no Monge–Ampere viscosity equivalence is assumed.

### 9. Homogeneous replacement theorem, domination for smooth data

**Status:** checked; no critical errors or gaps.

**9.1. A positive maximum lies in the interior.**

p_delta-v_epsilon is continuous on the compact closure and its boundary values are p-phi<=0. If its maximum m is positive, it is attained at an interior point z0.

**9.2. v_epsilon plus the maximum is the required upper test.**

By the definition of the maximum, p_delta<=v_epsilon+m everywhere and equality holds at z0. v_epsilon+m is smooth near z0 and has the same Hessian as v_epsilon.

**9.3. The test inequality forces a determinant lower bound.**

Step 8.7 gives theta(z0)+ddc v_epsilon(z0)>=delta beta. All eigenvalues relative to beta are at least delta, so its determinant ratio is >=delta^n.

**9.4. The positive maximum is impossible for epsilon<delta^n.**

The smooth equation at z0 says that same determinant ratio equals epsilon. The two assertions contradict epsilon<delta^n. Consequently p_delta<=v_epsilon for every 0<epsilon<min(1,delta^n).

**9.5. The successive limits give p<=H_phi.**

Fix delta>0 first and let epsilon down to zero along the entire small-density range to obtain p_delta<=H_phi. Then p_delta converges uniformly to p as delta down to zero, with error<=delta R^2. Thus p<=H_phi. No comparison of nonsmooth Monge–Ampere measures or total masses is used.

### 10. Homogeneous replacement theorem, domination for continuous data and final maximality note

**Status:** checked; no critical errors or gaps.

**10.1. The shifted competitor fits each smooth approximating boundary datum.**

a_j=||phi_j-phi||_partialB>=0 and phi-a_j<=phi_j pointwise. Hence p-a_j<=phi_j on the sphere. Subtracting a constant preserves continuity and theta-admissibility.

**10.2. Smooth-data domination passes to the limit.**

Apply the proved result to p-a_j and phi_j, giving p-a_j<=H_phi_j. Since a_j tends to zero and H_phi_j converges uniformly to H_phi, obtain p<=H_phi.

**10.3. H_phi is the largest continuous admissible function with boundary values at most phi.**

H_phi itself belongs to this class and the proved domination bounds every member above by H_phi. Therefore it is its largest element.

**10.4. The final note does not claim uniqueness of every homogeneous solution.**

The argument establishes the constructed solution's domination. It does not assert that every other homogeneous solution dominates H_phi. The final note accurately limits the conclusion and creates no missing uniqueness obligation.

**10.5. All hypotheses have accounted-for roles.**

Smoothness and compact local geometry control the subsolution, trace bound, matrices and translations; sphere smoothness gives Dirichlet solvability and data extensions; convexity gives translations and segments; continuity of competitors gives maxima and boundary control; product continuity yields homogeneous limits. Closedness, positivity of theta, global geometry, and total mass are absent assumptions and are not secretly required by these steps. The exact external existence hypotheses are verified in Section 11.

## 11. Exact external reference verification

### Search sequence and evidence

The required arXiv theorem search was run first using the full cited existence claim and its intended general setting. Its five results were from arXiv:2201.05030, 1909.00447, 1210.5551, 2402.03098, and 2203.03439. They concerned different equations or papers and were not accepted as matches. Built-in web search then used the same query and located the primary paper. The [arXiv record 0910.1851](https://arxiv.org/abs/0910.1851) confirms the paper's identity.

The primary PDF and local extracted text were inspected, and PDF pages 2–3 were rendered and viewed to resolve underlining and closure notation. The theorem is on printed p. 1186; the following paragraph on p. 1187 explicitly excludes positivity of \(\chi\) as a requirement. Equations (1.1)–(1.5) give the operator, admissibility and subsolution definitions. The later conditions (1.8) concern a separate problem without boundary. [Guan–Li primary PDF](https://people.math.osu.edu/guan.19/Papers/Guan-Li.aim.pdf)

Theorem 1.1 provides existence of a smooth strictly admissible solution from a \(C^4\) strictly admissible subsolution with matching boundary values and the stated determinant inequality. Its printed statement does not assert uniqueness or require \(\psi_u\ge0\). The supplied proof establishes uniqueness separately for constant density. [Theorem 1.1](https://people.math.osu.edu/guan.19/Papers/Guan-Li.aim.pdf)

### Specialization and formula checks

Use
\[
\overline M=\overline B,\qquad
\omega=\beta,\qquad
\chi=\theta,\qquad
u_{\rm GL}=\frac{v}{\pi},\qquad
\varphi_{\rm GL}=\frac{\varphi}{\pi},\qquad
\psi(z,u)=\varepsilon.
\]
Then
\[
\chi+\frac i2\partial\bar\partial u_{\rm GL}
=\theta+\frac{i}{2\pi}\partial\bar\partial v
=\theta+dd^c v.
\]
The subsolution is likewise \(\underline u_{\rm GL}=\underline v/\pi\). If
\(\theta+dd^c\widetilde\varphi\ge-K\beta\), choosing
\(A>K+\varepsilon^{1/n}\) gives the strict matrix inequality and a determinant strictly exceeding the required density on the entire closed ball. Its boundary value is exactly \(\varphi/\pi\).

The choice \(\omega=\beta\) is a legitimate Hermitian metric form. If one instead chooses \(\omega=(i/2)\partial\bar\partial|z|^2=\pi\beta\), the right-hand side must be \((\varepsilon/\pi^n)\omega^n\). Thus there is no missing power of \(\pi\) in the manuscript's normalization.

**R1. Ambient dimension and boundary.** The theorem's compact Hermitian setting with smooth boundary and n>=2 includes the closed Euclidean ball with omega=beta. The manuscript handles n=1 separately by the accepted Poisson theorem.

**R2. Background positivity.** The paragraph immediately after Theorem 1.1 explicitly says chi>0 is not an assumption. The supplied arbitrary smooth real theta fits chi=theta.

**R3. Background closedness.** Theorem 1.1 and its preceding setup impose no dchi=0 condition. Conditions (1.8) concern the later compact-without-boundary problem and are not hypotheses here. Section 6.2 separately addresses the Dirichlet case.

**R4. Strict admissibility and regularity of the subsolution.** under_u=under_v/pi is smooth and hence C4 on the closure. The previously checked estimate theta+ddc under_v >=(A-K) beta>0 verifies membership in H_chi at every point, including the boundary.

**R5. Subsolution inequality and boundary matching.** Choose A>K+epsilon^(1/n). Then the determinant is >(epsilon beta^n), which is stronger than the source's >= requirement. under_u equals phi/pi on the sphere.

**R6. Constant positive density.** Take omega=beta and psi(z,u)=epsilon. This is smooth and positive on the full required domain. Its derivative in u is zero; no monotonicity issue arises, and no density or mass normalization is required.

**R7. Exact potential normalization.** u_GL=v/pi gives chi+(i/2) partial barpartial u_GL=theta+ddc v exactly. The boundary datum and subsolution are likewise divided by pi. If instead omega were chosen as (i/2) partial barpartial |z|^2=pi beta, the same equation would use psi=epsilon/pi^n; both give constant positive density.

**R8. Smoothness and positivity of the resulting solution.** The conclusion u_GL in H_chi intersect C-infinity(closed M) becomes v=pi u_GL smooth on the closed ball with theta+ddc v>0. This is precisely the existence and strict-admissibility part of the lemma.

**R9. Uniqueness is not misattributed.** The theorem's printed conclusion supplies existence. The manuscript independently proves uniqueness for its u-independent right side and background by log-determinant linearization and the maximum principle; this deduction is valid.

**R10. No weaker viscosity subsolution or degenerate theorem is imported.** The source's subsequent relaxation of subsolution regularity under chi>0 is unused. Only the smooth strictly admissible positive-density theorem is used. The homogeneous limit and its domination are established within the submitted proof.

All ten applicability checks pass. This closes the external dependency in the classical positive-density lemma.

## 12. Explicit formulas for the delicate local steps

These formulas spell out the short arguments already present in the submitted proof.

### Boundary barriers and translated comparison

Take \(C\ge \max(0,4\sup_{\overline B}\operatorname{tr}_{\beta}\theta)\). Then
\[
\Delta v_\varepsilon\ge-C=\Delta q,\qquad
\underline v\le v_\varepsilon\le q.
\]
Both barrier differences from \(\widetilde\varphi\) vanish on the sphere. A common bound on their gradients therefore gives the asserted distance estimate. No estimate for derivatives of \(v_\varepsilon\) is used to obtain it.

For \(L=\operatorname{Lip}(\widetilde\varphi)\), both boundary cases in \(\partial D_h\) give
\[
v_\varepsilon(z+h)-v_\varepsilon(z)\le(C_1+L)|h|.
\]
Choose \(C_3\ge C_1+L\). Since \(|z|^2-R^2\le0\), the corrected function satisfies \(w\le v_\varepsilon\) on the whole intersection boundary. Its matrix difference is exactly
\[
(\theta+dd^c w)(z)
-\bigl(\theta(z+h)+dd^c v_\varepsilon(z+h)\bigr)
=\theta(z)-\theta(z+h)+C_2|h|\beta\ge0.
\]
Thus smooth comparison has the correct determinant sign and yields
\[
v_\varepsilon(z+h)-v_\varepsilon(z)
\le(C_2R^2+C_3)|h|.
\]
The same formula with \(-h\) proves the reverse inequality. For each fixed \(\varepsilon>0\), all needed ellipticity bounds exist on the compact closure. Their uniformity as \(\varepsilon\to0\) is not required.

### Uniformity of the full limit

Let \(L_*=C_4\), and choose a finite \(r\)-net \(\{x_i\}\) in \(\overline B\). At every point \(x\), for a net point within distance \(r\),
\[
0\le H_\varphi(x)-v_\varepsilon(x)
\le 2L_*r+\max_i\bigl(H_\varphi(x_i)-v_\varepsilon(x_i)\bigr).
\]
First choose \(r\) small and then choose one \(\varepsilon_0\) controlling all finitely many net points. This proves uniform convergence for every \(0<\varepsilon<\varepsilon_0\). It justifies the boundary trace and all later uniform-limit steps.

### Upper-test matrix inequality

Fix \(\eta>0\), and shrink a ball about \(z_0\) so that
\[
\theta(z_0)-\theta(z)+\eta\beta\ge0.
\]
A real quadratic \(Q_0\) exists with \(dd^cQ_0=\theta(z_0)\), even when this constant form is indefinite. The function
\[
F_\eta=p_\delta-\delta|z|^2+Q_0+\eta|z-z_0|^2
\]
has positive current Hessian and is plurisubharmonic there. If \(a\) touches \(p_\delta\) from above, then
\[
A_\eta=a-\delta|z|^2+Q_0+\eta|z-z_0|^2
\]
touches \(F_\eta\) from above. For any complex line through \(z_0\),
\[
A_\eta(z_0)=F_\eta(z_0)
\le \frac1{2\pi}\int_0^{2\pi}F_\eta(z_0+r e^{it}\xi)\,dt
\le \frac1{2\pi}\int_0^{2\pi}A_\eta(z_0+r e^{it}\xi)\,dt.
\]
Taylor expansion as \(r\to0\) gives \(dd^cA_\eta(z_0)\ge0\) in every direction. Consequently
\[
\theta(z_0)+dd^ca(z_0)\ge(\delta-\eta)\beta.
\]
Letting \(\eta\downarrow0\) proves exactly the claimed lower bound \(\delta\beta\). The local ball may depend on \(\eta\).

At a positive maximum of \(p_\delta-v_\varepsilon\), the upper test is \(a=v_\varepsilon+\max(p_\delta-v_\varepsilon)\). Hence
\[
\varepsilon\beta^n=(\theta+dd^cv_\varepsilon)^n(z_0)
\ge\delta^n\beta^n,
\]
which contradicts \(\varepsilon<\delta^n\). This proves domination without a global comparison principle, total-mass comparison, or an assumed Monge–Ampère viscosity equivalence.

## 13. Aggregation and verdict

- **Critical errors:** none.
- **Gaps:** none.
- **Verdict:** correct under the stated accepted inputs.
- **Repair hints:** empty.

The proof establishes existence, prescribed continuous boundary trace, the homogeneous product equation, contraction, Lipschitz regularity for smooth boundary data, and domination of every continuous admissible competitor with boundary at most \(\varphi\). Since the constructed function is itself a competitor, it is the largest member of that class. This is exactly the maximality stated in the final note. No uniqueness claim about all homogeneous solutions is required.

## Evidence and persistence

The structured checks are stored in this run's memory channels. The empty failed_checks channel records that no mathematical issue was detected. A transient failure to append item 7 was retried successfully; item numbers preserve the verified textual order. All reference-search and local rendering failures were recovered and do not leave unresolved dependencies.

- [Input proof](/Users/mingchen/Non-Kahler/research/rethlas/verification/inputs/local-homogeneous-dirichlet.md)
- [Primary local PDF](/Users/mingchen/Non-Kahler/research/sources/GuanLi10-dirichlet.pdf)
- [Primary local extraction](/Users/mingchen/Non-Kahler/research/sources/GuanLi10-dirichlet.txt)
- [Statement checks](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/local_homogeneous_dirichlet_01/statement_checks.jsonl)
- [Reference checks](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/local_homogeneous_dirichlet_01/reference_checks.jsonl)
- [Final JSON](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/local_homogeneous_dirichlet_01/verification.json)

SHA-256:

| Evidence | Hash |
| --- | --- |
| Input | c6245b9329e67c5cf2a1282d178c254db6b3f26469cf98c21b6679c47457af2e |
| Primary PDF | 92b751a4f7a8945c4734dc18ffbfa5fa3f973e57b5a680888aca4dab05a9d25c |
| Extracted text | 9a16eaf9705f113eb469a7cf233f4f60951e48fb21f6d07bb76cebdeede21fd3 |

