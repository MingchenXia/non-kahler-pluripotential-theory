# Verification report: Gauduchon volume Hessian and class recovery

**Run:** `gauduchon_volume_hessian_01`  
**Verdict:** **correct**, under the explicitly accepted prerequisites.  
**Findings:** 0 critical errors; 0 gaps.  
**Coverage:** 20 sequential proof-item checks, with every local deduction recorded, followed by 6 reference and context checks.  
**Input:** [Supplied proof](/Users/mingchen/Non-Kahler/research/rethlas/verification/inputs/gauduchon-volume-hessian.md).  
**Strict output:** [verification.json](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/gauduchon_volume_hessian_01/verification.json).

## 1. Scope and accepted prerequisites

This audit covers the entire submitted text, in its written order: the second-variation proposition and subsequent quotient metric, the derivative-recovery proposition and curve paragraph, the product-surface example, and the closing discussion. It checks the new deductions rather than re-certifying prerequisites the user explicitly instructed the verifier to accept. The book was read without modification.

The setting is a compact connected complex manifold \(X\), \(\dim_{\mathbb C}X=n\geq1\), with a fixed smooth strictly positive top-degree form \(\mu\) satisfying \(\int_X\mu=1\). The cone \(\mathscr P\) consists of smooth real \((1,1)\)-backgrounds admitting a smooth positive representative. Classes mean the quotient by \(dd^c C^\infty(X,\mathbb R)\); the backgrounds need not be \(d\)-closed.

Accepted inputs, with their stated scope:

- The internal dual formula \(\lambda_\mu(\theta)=c_\theta(\mu)^{1/n}\), \(\mathcal V_\mu(\theta)=c_\theta(\mu)\).
- Ordinary smooth Hermitian Monge–Ampère existence and uniqueness of the positive solution form, with potentials unique up to constants.
- For \(n\geq2\), the unique minimizing Gauduchon ray conformal to the solution.
- Smooth dependence of the solution and scalar on finite-dimensional smooth families, using a fixed mean normalization, and the stated first-variation formula.
- The smooth strictly positive adjoint probability and its mean-trace-zero identity.
- The positive \((n-1,n-1)\)-root construction for \(n\geq2\), and scalar Green solvability on compact connected curves.

No bounded mass property, global \(dd^c\)-lemma, infinite-dimensional distance theorem, boundary extension, or novelty assertion is assumed or inferred.

## 2. Definitions and normalization audit

The exact definitions read in the book are
\[
D_\mu(\gamma)
 =\int_X\left(\frac{\mu}{\gamma^n}\right)^{1/n}\gamma^n,
\qquad
\lambda_\mu(\theta)
 =\inf_{\gamma\ {\rm Gauduchon}}
 \frac{\int_X\theta\wedge\gamma^{n-1}}{D_\mu(\gamma)},
\qquad
\mathcal V_\mu=\lambda_\mu^n.
\]

| Quantity or convention | Checked normalization |
|---|---|
| Positive solution | \(\Omega=\theta+dd^cu\), \(\Omega^n=\lambda^n\mu\) |
| Gauduchon condition | \(dd^c(\gamma^{n-1})=0\), with no assertion that \(d\gamma=0\) |
| Denominator scaling | \(D_\mu(s\gamma)=s^{n-1}D_\mu(\gamma)\), \(s>0\) |
| Trace | \(\operatorname{tr}_\Omega\eta=n\,\eta\wedge\Omega^{n-1}/\Omega^n\) |
| Adjoint multiplier | \(e^{(n-1)g}\), when \(\gamma=e^g\Omega\) |
| Adjoint probability | \(d\nu_\Omega=e^{(n-1)g}\Omega^n/\int_Xe^{(n-1)g}\Omega^n\) |
| Direction endomorphism | \(A_\chi=\Omega^{-1}(\chi+dd^c\dot u)\), self-adjoint for \(\Omega\) |
| Root normalization | \(\widehat\gamma^{n-1}=\Xi_\theta\), \(D_\mu(\widehat\gamma)=1\) |
| Curve convention | \(D_\mu=1\), \(\lambda_\mu(\theta)=\int_X\theta\), \(\nu_\Omega=\mu\) |
| Product-surface factor | \((a\alpha+b\beta)^2=2ab\,\alpha\wedge\beta\) |

All these conventions agree with the submitted formulas. In particular, neither an extra factor \(n\) in the first derivative nor an extra factorial in the positive root is needed.

## 3. Main calculations verified

### 3.1 Affine second variation

For \(\theta_t=\theta+t\chi\), fixed \(\mu\), and \(r=\dot\lambda/\lambda\),
\[
\operatorname{tr}A_\chi=nr,
\qquad
\operatorname{tr}_\Omega(dd^c\ddot u)
 -\operatorname{tr}(A_\chi^2)
 =n(\log\lambda)''.
\]
Here \(\ddot\Omega=dd^c\ddot u\) because the background path is affine. Integrating this already differentiated identity against the single probability at the base point gives
\[
-D^2\log\lambda_\mu|_\theta(\chi,\chi)
 =\frac1n\int_X\operatorname{tr}(A_\chi^2)\,d\nu_\Omega.
\]
No varying measure is differentiated in this step.

Since \(A_\chi\) is Hermitian and its trace is the spatially constant number \(nr\),
\[
\frac{\ddot\lambda}{\lambda}
 =-\frac1n\int_X\|A_\chi-rI\|_\Omega^2\,d\nu_\Omega.
\]
Strict positivity of the adjoint density gives the exact equality cases:
\[
\ddot\lambda=0
 \iff \chi=r\theta+dd^cf
 \quad(r\in\mathbb R,\ f\in C^\infty(X,\mathbb R)),
\]
\[
D^2\log\lambda_\mu|_\theta(\chi,\chi)=0
 \iff \chi=dd^cf.
\]
The converse directions follow from smooth gauge invariance and degree-one homogeneity.

Linearity of the normalized linearized equation gives the symmetric real bilinear form
\[
\mathfrak g_\theta(\chi_1,\chi_2)
 =\frac1n\int_X
 \operatorname{tr}(A_{\chi_1}A_{\chi_2})\,d\nu_\Omega.
\]
Its kernel is exactly the smooth \(dd^c\) directions. Both the base representative and representatives of tangent directions can be changed without changing this form. Smooth finite-dimensional affine slices with independent quotient directions therefore carry the stated Riemannian metric.

### 3.2 Recovery from value and derivative

For \(n\geq2\), knowing the derivative on all smooth real \((1,1)\)-forms determines
\[
\Xi_\theta=\frac{\gamma_\theta^{n-1}}{D_\mu(\gamma_\theta)}.
\]
Its unique positive root is
\[
\widehat\gamma
 =D_\mu(\gamma_\theta)^{-1/(n-1)}\gamma_\theta,
\qquad D_\mu(\widehat\gamma)=1.
\]
Conformality and the prescribed positive volume form then determine
\[
\Omega_\theta
 =\lambda_\mu(\theta)
 \left(\frac{\mu}{\widehat\gamma^n}\right)^{1/n}
 \widehat\gamma.
\]
Thus the value and derivative recover the class; equality of derivatives alone is equivalent to equality of positive class rays.

The inverse of the normalized-class-to-Gauduchon-ray map is
\[
[\gamma]_{\mathbb R_{>0}}
 \longmapsto
 \left[
 \left(\frac{\mu}{\gamma^n}\right)^{1/n}\gamma
 \right]_{dd^c}.
\]
It is independent of constant scale, has \(\lambda_\mu=1\), and has \(\gamma\) as a minimizing metric. Both surjectivity and injectivity are proved.

### 3.3 Curves and the product example

On a curve, the Green operator identifies equal integrals with equal smooth \(dd^c\) classes. The formulas reduce to
\[
\lambda_\mu(\theta)=\int_X\theta,\qquad
\mathfrak g_\theta(\chi,\chi)
 =\frac{(\int_X\chi)^2}{(\int_X\theta)^2}.
\]
The root Hessian is identically zero, exactly as its equality characterization requires.

On \(\mathbb P^1\times\mathbb P^1\), closed Stokes gives, for every permitted \(\mu\),
\[
\mathcal V_\mu(a\alpha+b\beta)=2ab,\qquad
\lambda_\mu(a\alpha+b\beta)=\sqrt{2ab}.
\]
The family \(e^t\alpha+e^{-t}\beta\) consequently has the constant volume profile \(2\), while its first factor period \(e^t\) distinguishes all its classes.

The restricted metric is
\[
\mathfrak g
 =\frac12\left(\frac{da^2}{a^2}+\frac{db^2}{b^2}\right).
\]
The global coordinates \(x=\log(a)/\sqrt2\), \(y=\log(b)/\sqrt2\) give \(dx^2+dy^2\) on all of \(\mathbb R^2\), proving intrinsic completeness of this family. The hyperbola has squared speed \(\tfrac12(1+1)=1\). These conclusions are confined to the indicated finite-dimensional family.

## 4. Complete sequential audit

The following items follow the submitted proof's textual order. “dot” and “double-dot” in the step descriptions denote first and second derivatives at the base point. Every item passed; no missing hypothesis or unsupported deduction was found.

### 1. Second variation on background classes — setting and solution

**Result: Pass.**

1. The book defines P by existence of a smooth positive representative, not by d-closedness of theta. For theta in P choose u0 with theta+dd^c u0>0, apply the accepted ordinary smooth Hermitian equation to that representative, and absorb u0 into the solution potential.

2. The accepted dual theorem identifies the scalar c with lambda^n and V_mu with c, and lambda>0. Consequently log lambda and all displayed ratios are defined.

3. The first-variation supporting functional is interpreted using gamma^(n-1)/D_mu(gamma), not the metric gamma without normalization. No uniform mass bound is needed.

### 2. Second variation on background classes — adjoint probability

**Result: Pass.**

1. For n>=2, the accepted conformal theorem gives gamma=e^g Omega with dd^c(gamma^(n-1))=0; its constant scale does not change nu_Omega.

2. With Z=integral e^((n-1)g) Omega^n, the book's trace convention gives integral tr_Omega(dd^c f) dnu=(n/Z) integral dd^c f wedge gamma^(n-1)=0. This requires dd^c-closedness of gamma^(n-1), not d-closedness of gamma or theta.

3. Z is finite and strictly positive on compact X, so nu is a smooth strictly positive probability. For n=1, Omega=lambda mu and integral Omega=lambda give nu=mu, and integral tr_Omega(dd^c f)dnu=lambda^(-1) integral dd^c f=0.

### 3. Second variation on background classes — affine path and normalization

**Result: Pass.**

1. The direction chi is a smooth real (1,1)-form, as fixed by the tangent space and the cited first-variation proposition. If Omega=theta+dd^c u>0, then Omega+t chi>0 for all sufficiently small real t by compactness, hence theta+t chi remains in P.

2. Use one fixed mean normalization, for example integral u_t mu=0, so the accepted smooth dependence supplies dot u and double-dot u. No supremum normalization is differentiated.

3. Raising an index with Omega makes A_chi=Omega^(-1)(chi+dd^c dot u) self-adjoint for Omega. Its trace and trace of its square are invariant under coordinate changes.

### 4. Proposition prop:gaud-volume-hessian — first logarithmic derivative

**Result: Pass.**

1. In local coordinates, the fixed-density equation is log det Omega_t=n log lambda_t+log density(mu), up to a fixed coordinate factor.

2. The derivative of log det Omega_t is tr(Omega_t^(-1) dot Omega_t); at t=0, dot Omega=chi+dd^c dot u.

3. Therefore tr A_chi=n dot lambda/lambda pointwise. The right side is a real scalar independent of position on X, since mu is fixed.

### 5. Proposition prop:gaud-volume-hessian — second logarithmic derivative

**Result: Pass.**

1. Differentiate the inverse matrix: (Omega_t^(-1))dot=-Omega_t^(-1)dot Omega_t Omega_t^(-1). Thus the second derivative of log det is tr(Omega^(-1) double-dot Omega)-tr(A_chi^2).

2. Affineness is essential: double-dot theta=0, hence double-dot Omega=dd^c double-dot u. There is no omitted background acceleration term.

3. The resulting identity is tr_Omega(dd^c double-dot u)-tr(A_chi^2)=n(double-dot lambda/lambda-(dot lambda/lambda)^2)=n(log lambda)double-dot.

### 6. Proposition prop:gaud-volume-hessian — fixed adjoint integration

**Result: Pass.**

1. Integrate the preceding pointwise identity only after differentiating it, against the single base-point probability nu_Omega.

2. The first term integrates to zero by the adjoint identity applied to the smooth function double-dot u. The scalar right side is unchanged because nu has total mass one.

3. Therefore -(log lambda)double-dot=(1/n) integral tr(A_chi^2)dnu. No derivative of nu, g, or a Gauduchon metric has been omitted: no varying integral was differentiated.

### 7. Proposition prop:gaud-volume-hessian — root Hessian and its equality case

**Result: Pass.**

1. Set r=dot lambda/lambda. Hermitian self-adjointness and tr A=nr give ||A-rI||_Omega^2=tr((A-rI)^2)=tr(A^2)-nr^2.

2. The logarithmic identity gives double-dot lambda/lambda=r^2-(1/n)integral tr(A^2)dnu=-(1/n)integral||A-rI||^2dnu, with exactly the stated sign and factor 1/n.

3. A smooth nonnegative integrand has zero integral against a strictly positive smooth density if and only if it vanishes everywhere. Thus root-Hessian equality is exactly A=rI.

4. The identity chi+dd^c dot u=r(theta+dd^c u) rearranges to chi=r theta+dd^c(ru-dot u); r is a constant and the potential is smooth real.

5. Conversely, chi=r theta+dd^c f implies theta_t=(1+rt)theta+t dd^c f. For sufficiently small t, 1+rt>0; smooth gauge invariance and degree-one homogeneity give lambda_t=(1+rt)lambda and zero second derivative.

### 8. Proposition prop:gaud-volume-hessian — logarithmic equality case

**Result: Pass.**

1. For Hermitian A, tr(A^2) is the sum of squares of real eigenvalues and equals its squared Omega norm. Vanishing of its integral is equivalent to A=0 everywhere.

2. A=0 gives chi=-dd^c dot u, hence a smooth dd^c direction. Conversely, theta+t dd^c f stays in the same smooth class and lambda is constant.

3. The root kernel contains the radial direction; the logarithmic kernel contains only dd^c directions. In particular chi=theta gives A=I and g_theta(theta,theta)=1, a consistency check of the normalization.

### 9. Equation eq:gaud-background-quadratic-form — linearity and polarization

**Result: Pass.**

1. At fixed theta the normalized pair (dot u,r) solves L_Omega dot u-nr=-tr_Omega chi, with L_Omega=tr_Omega dd^c. Integration fixes nr=integral tr_Omega chi dnu, and the accepted normalized inverse fixes dot u.

2. The linear equation and uniqueness show that dot u, r, and A_chi depend real-linearly on chi.

3. Polarizing the square gives (1/n)integral tr(A_chi1 A_chi2)dnu. Cyclicity of trace makes this symmetric even when the matrices do not commute. For two Hermitian matrices the trace of their product is real.

4. Smooth dependence on each finite-dimensional two-parameter family identifies this polarization with the mixed affine Hessian -D^2 log lambda.

### 10. Equation eq:gaud-background-quadratic-form — quotient and gauge invariance

**Result: Pass.**

1. If chi is replaced by chi+dd^c h, replace dot u by dot u-h plus the constant required by the fixed normalization. Thus A_chi is unchanged, so all bilinear pairings descend to the quotient by dd^c C-infinity.

2. The exact logarithmic kernel already proved shows that a nonzero quotient direction has strictly positive squared norm. This is positive definiteness on the algebraic tangent quotient.

3. If theta is replaced by theta+dd^c h, uniqueness of the smooth equation gives exactly the same solution form Omega, with u replaced by u-h plus a constant. The linearized operator, A, and adjoint probability are consequently unchanged.

4. The quotient includes arbitrary smooth real (1,1)-forms; it is not restricted to ordinary Bott-Chern cohomology. No global dd^c lemma is invoked.

### 11. Second variation — finite-dimensional metric and scope

**Result: Pass.**

1. On an affine family theta_s=theta0+sum s_i chi_i with directions independent modulo smooth dd^c, any nonzero parameter tangent determines a nonzero quotient direction, so the displayed Gram matrix is positive definite.

2. The coefficients are second derivatives of the smooth function -log lambda on that finite-dimensional family, hence are smooth. This establishes a smooth Riemannian metric on its open domain in P.

3. Varying a potential in one fixed background class gives precisely dd^c tangent directions, which the form kills. The book's energy chapter instead uses smooth functions as potential-space tangent vectors.

4. A pointwise positive form on an infinite-dimensional quotient does not by itself prove nondegeneracy or completeness of a path distance. The supplied text makes neither assertion.

### 12. Recovering a positive class — derivative form Xi

**Result: Pass.**

1. By the accepted first-variation formula, Xi=gamma^(n-1)/D_mu(gamma) represents d lambda on all smooth real (1,1)-directions.

2. Under gamma -> s gamma, both numerator and denominator scale by s^(n-1); Xi is independent of the minimizing metric's constant scale.

3. D_mu(gamma) is a positive number, so Xi is a smooth strictly positive (n-1,n-1)-form and dd^c Xi=0 by the Gauduchon condition.

4. The derivative is a functional on the quotient as well: integration of dd^c f wedge Xi vanishes. It is still evaluated on every smooth (1,1)-form through its representative.

### 13. Proposition prop:gaud-derivative-recovery — pairing and positive root

**Result: Pass.**

1. If two smooth (n-1,n-1)-forms pair equally with every smooth real (1,1)-form, their difference vanishes. The pointwise wedge pairing is nondegenerate and arbitrary localized smooth tests are allowed.

2. For n>=2, the accepted positive-root linear algebra gives the unique smooth positive (1,1)-form hat gamma with (hat gamma)^(n-1)=Xi, using exactly the same wedge-power convention as in the book.

3. If D=D_mu(gamma), uniqueness of the root gives hat gamma=D^(-1/(n-1))gamma. The root is Gauduchon because dd^c Xi=0.

4. The exact formula D_mu(s gamma)=s^(n-1)D_mu(gamma) yields D_mu(hat gamma)=D^(-1)D=1. There is no missing exponent or wedge factorial.

### 14. Proposition prop:gaud-derivative-recovery — reconstructing the class and its ray

**Result: Pass.**

1. The accepted unique-minimizer statement makes Omega pointwise conformal to hat gamma: Omega=q hat gamma with a smooth positive function q.

2. The fixed-density equation gives q^n (hat gamma)^n=lambda^n mu. The unique positive solution is q=lambda(mu/(hat gamma)^n)^(1/n), exactly the displayed formula.

3. Since Omega=theta+dd^c u, the value and full derivative determine a representative of the smooth class.

4. The derivative alone fixes hat gamma and hence Omega/lambda. Two backgrounds with equal derivative therefore have Omega2=(lambda2/lambda1)Omega1, so their classes differ by the positive constant lambda2/lambda1.

5. Conversely, positive scaling of a class scales its solution form, leaves its conformal Gauduchon ray unchanged, and hence leaves Xi unchanged. Thus equality of derivatives is equivalent to equality of positive class rays.

### 15. Proposition prop:gaud-derivative-recovery — bijection

**Result: Pass.**

1. For any Gauduchon gamma, set Omega_gamma=(mu/gamma^n)^(1/n)gamma. Under gamma -> s gamma, the density factor scales by s^(-1), so Omega_gamma is unchanged.

2. The positive smooth density ratio makes Omega_gamma Hermitian, and (Omega_gamma)^n=mu. With background Omega_gamma, the zero potential solves the normalized smooth equation, so lambda_mu(Omega_gamma)=1.

3. Directly, integral Omega_gamma wedge gamma^(n-1)=integral(mu/gamma^n)^(1/n)gamma^n=D_mu(gamma). This test quotient is 1, the dual infimum; gamma is therefore a minimizer. This also expands the cited pointwise AM-GM equality.

4. Thus every Gauduchon constant-scaling ray is obtained from a normalized positive class. Conversely, identical minimizing rays give identical density-normalized solution forms by the recovery formula, so the normalized classes are equal.

5. The bijection concerns all positive smooth dd^c classes. It does not assert that the density-normalized form itself is Gauduchon or d-closed.

### 16. Dimension-one paragraph — Green and the Hessian special case

**Result: Pass.**

1. For n=1, D_mu(gamma)=integral mu=1 and lambda_mu(theta)=V_mu(theta)=integral theta. Its derivative is the fixed functional chi -> integral chi.

2. On a compact connected curve, the accepted Green operator writes every smooth real top-degree form with zero integral as dd^c f. Equality of integrals is therefore equivalent to equality of smooth dd^c classes.

3. Every direction has chi=r theta+dd^c f with r=(integral chi)/(integral theta), as integral theta>0 in P. Thus the root Hessian is zero in every direction, in agreement with the first equality statement.

4. Omega=lambda mu and dot Omega=(integral chi)mu give the scalar endomorphism A=rI. Hence -D^2 log lambda(chi,chi)=(integral chi)^2/(integral theta)^2, whose kernel is exactly the smooth dd^c directions. No n>=2 positive-root assertion is used on curves.

### 17. Equal volume profiles — product forms and total volume

**Result: Pass.**

1. For pullbacks of forms from complex curves, alpha^2=beta^2=0; product integration and the factor normalizations give integral alpha wedge beta=1.

2. For a,b>0, a alpha+b beta is smooth positive and d-closed, hence Kahler. Its top power is 2ab alpha wedge beta and its total mass is 2ab.

3. For each smooth positive probability mu, the accepted smooth equation has Omega=theta+dd^c u and Omega^2=lambda^2 mu. Since theta is d-closed, integral theta wedge dd^c u=0 and integral(dd^c u)^2=0 by Stokes.

4. Consequently lambda^2=integral Omega^2=integral theta^2=2ab. Thus V_mu=2ab and lambda_mu=sqrt(2ab) for every such mu. Closedness is used here and was not silently assumed in the general nonclosed argument.

### 18. Equal volume profiles — distinct smooth classes

**Result: Pass.**

1. For a=e^t and b=e^(-t), the product ab=1, so every member has the identical volume profile mu -> 2 over all smooth positive probability measures.

2. On C=P1 x {p}, integral_C alpha=1 and integral_C beta=0, hence integral_C theta=e^t.

3. The pullback of dd^c f to C is dd^c(f restricted to C) and integrates to zero. Distinct real t give distinct periods and hence distinct smooth dd^c classes.

4. The example does not conflict with recovery: values for varying mu do not supply derivatives in the background direction for a fixed mu.

### 19. Equal volume profiles — induced metric, completeness, and speed

**Result: Pass.**

1. On the affine two-dimensional cone, log lambda=(1/2)log 2+(1/2)log a+(1/2)log b, so its negative affine Hessian is diag(1/(2a^2),1/(2b^2)) with zero mixed coefficient.

2. The directions alpha and beta are independent modulo dd^c, as integration over the two factor curves detects their coefficients. The restricted Hessian therefore is the positive Riemannian metric claimed.

3. The global coordinates x=(log a)/sqrt(2) and y=(log b)/sqrt(2) map the whole positive quadrant diffeomorphically onto R^2 and give g=dx^2+dy^2. The intrinsic Riemannian metric on this family is complete.

4. Along a=e^t, b=e^(-t), squared speed is (1/2)((dot a/a)^2+(dot b/b)^2)=(1/2)(1+1)=1. The curve is defined for all real t.

5. No completeness or distance assertion for paths through other background classes follows from this restriction, and none is made in the supplied proof.

### 20. Closing paragraph and hypothesis audit

**Result: Pass.**

1. The summary about value, derivative, and second variation follows from the preceding results, with fixed mu and smooth positive classes understood.

2. The final sentence identifies an extension problem at nef boundary points or singular residual classes; it asserts no proved boundary metric, recovery theorem, or convergence theorem.

3. Compactness is used for positivity under small perturbations, integration by parts, elliptic theory, and positive finite adjoint normalization. Connectedness is used for the accepted scalar/constant-kernel and Gauduchon-ray uniqueness statements and the curve Green result.

4. Strict smooth positivity of mu and the solution underlies the logarithmic equation, positive adjoint density, smooth roots, and equality-to-pointwise-zero arguments; integral mu=1 fixes all scalar normalizations.

5. Affineness is used in the second-variation identity, d-closedness only in the product example, and n>=2 only where the Gauduchon ray and positive root require it. No BMP, global dd^c lemma, boundary regularity, or novelty assumption is used.

## 5. Reference and context checks

The required reference-checking skill was applied after the sequential audit. No new external-paper citation occurs in the supplied proof. The arXiv-then-web search requirement therefore has no applicable reference here. Accepted prerequisites were checked for their exact local statements and applicability, without reopening their proofs or claiming external searches.

### R1. Definitions used throughout; positive class cone

**Status:** Matched and applicable within the accepted scope.

**Sources:** [chapter_gauduchon_variational_volume.tex, lines 10–30, 55–61](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:10)

**Statement or dependency:** D_mu(gamma)=integral_X (mu/gamma^n)^(1/n) gamma^n; lambda_mu(theta)=inf_Gauduchon gamma (integral theta wedge gamma^(n-1))/D_mu(gamma); V_mu=lambda_mu^n. P consists of backgrounds admitting a smooth positive representative, and backgrounds are identified modulo smooth dd^c.

**Definitions and context:** mu is a smooth strictly positive probability form; gamma is Hermitian with dd^c(gamma^(n-1))=0; these classes include non-d-closed forms and are not ordinary Bott-Chern cohomology.

**Comparison and downstream use:** Exact match. D_mu has degree n-1, lambda degree 1, and V_mu degree n. In dimension one D_mu=1. All new calculations preserve these conventions.

### R2. Solution, prop:gaud-volume-hessian, and derivative recovery

**Status:** Matched and applicable within the accepted scope.

**Sources:** [chapter_gauduchon_variational_volume.tex, lines 55–84, 119–145](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:55); [chapter_smooth_equations.tex, lines 6–25](/Users/mingchen/Non-Kahler/book/author/chapter_smooth_equations.tex:6)

**Statement or dependency:** For theta in P the ordinary smooth Hermitian equation has a unique positive solution form Omega=theta+dd^c u with Omega^n=c_theta(mu)mu. The dual formula gives lambda=c_theta(mu)^(1/n). For n>=2 the minimizers are precisely the constant multiples of the Gauduchon metric conformal to Omega. The normalized solution and scalar vary smoothly in finite-dimensional smooth families, and d lambda_theta(chi)=integral chi wedge gamma_theta^(n-1)/D_mu(gamma_theta).

**Definitions and context:** The equation is the ordinary (1,1)-background Hermitian Monge-Ampere equation. Its scalar is unknown; it is not a prescribed-mass equation without a free normalization, and it is not the STW (n-1)-form equation. Smoothness is used with a fixed mean normalization.

**Comparison and downstream use:** Exact match to the accepted statements. These are explicitly accepted completed prerequisites, not re-certified here. No BMP or differentiated supremum is used. The submitted second-variation result is not used in any accepted prerequisite, so the local dependency is not circular.

### R3. Adjoint probability and AM-GM minimizer checks

**Status:** Matched and applicable within the accepted scope.

**Sources:** [chapter_gauduchon.tex, lines 6–46, 95–114, 203–232](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon.tex:6)

**Statement or dependency:** For n>=2 every Hermitian eta has a conformal Gauduchon representative gamma=rho^(1/(n-1))eta with rho>0 unique up to a positive constant and dd^c(rho eta^(n-1))=0. For L v=n dd^c v wedge eta^(n-1)/eta^n, normalize integral rho eta^n=1; then integral L v rho eta^n=0. Also eta wedge gamma^(n-1)>= (eta^n/gamma^n)^(1/n)gamma^n, with equality when the relative eigenvalues are equal.

**Definitions and context:** The multiplier in the submitted notation is rho=e^((n-1)g)/Z, not e^g/Z. The trace includes the factor n. The adjoint condition is dd^c-closedness of the (n-1)st power, not closedness of the metric.

**Comparison and downstream use:** Exact match. The submitted measure, factor 1/n in the Hessian, fixed-measure integration, and use of conformality for equality all have the correct definitions and factors.

### R4. Positive root in prop:gaud-derivative-recovery; dimension-one Green statement

**Status:** Matched and applicable within the accepted scope.

**Sources:** [chapter_gauduchon.tex, lines 136–140](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon.tex:136); [chapter_gauduchon_variational_volume.tex, lines 30, 84, 116, 126](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:30); [chapter_smooth_equations.tex, lines 22–23](/Users/mingchen/Non-Kahler/book/author/chapter_smooth_equations.tex:22)

**Statement or dependency:** For n>=2 every smooth strictly positive (n-1,n-1)-form Gamma has a unique smooth strictly positive (1,1)-root Gamma=gamma^(n-1). With a consistent wedge normalization its diagonal eigenvalues obey lambda_i=(product_j g_j)^(1/(n-1))/g_i. On a compact connected curve every smooth real top-degree form of integral zero is dd^c f for a smooth real f.

**Definitions and context:** The root operation is pointwise and smooth only on the strictly positive cone; dd^c Gamma=0 makes the root Gauduchon. On a curve the Green compatibility condition is total integral zero, and all real (1,1)-forms have top degree.

**Comparison and downstream use:** Exact match and explicitly allowed by the user. The scaling D^(-1/(n-1)) is valid only for n>=2 and is used only there. The curve paragraph correctly uses Green instead of the root construction.

### R5. Potential-space comparison and product example

**Status:** Matched and applicable within the accepted scope.

**Sources:** [chapter_energy.tex, lines 1–10](/Users/mingchen/Non-Kahler/book/author/chapter_energy.tex:1); [chapter_gauduchon_variational_volume.tex, lines 180–184](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:180)

**Statement or dependency:** The energy chapter concerns smooth positive potentials for a fixed background, with smooth real functions as tangent directions. For d-closed backgrounds in the smooth equation, Stokes identifies the normalization with integral theta^n.

**Definitions and context:** The potential-space reference is only a comparison of spaces, not an invocation of an energy primitive or a distance theorem. The explicit product backgrounds are Kahler and thus meet the closedness hypothesis for Stokes.

**Comparison and downstream use:** The comparison is accurate. The Stokes application, 2ab factor, period obstruction, Euclidean logarithmic coordinates, completeness within the two-dimensional family, and unit-speed calculation were checked directly; no external theorem is used to infer them.

### R6. External-reference inventory for the entire supplied proof

**Status:** Matched and applicable within the accepted scope.

**Statement or dependency:** The supplied proof contains internal cross-references to prop:gaud-volume-first-variation and chap:energy, a reference to the book's positive-root linear algebra, and standard inputs explicitly accepted by the user. It contains no new citation to an external paper.

**Definitions and context:** Bibliographic citations inside the already accepted source chapters do not create an obligation to re-prove or re-search those accepted prerequisites. Neither Collins' broader concavity theorem nor an STW existence theorem is used as a new result in this audit.

**Comparison and downstream use:** All cited statements needed here have been located locally and their exact hypotheses, formulas, and downstream applications checked. The required external-paper search rule is vacuous for this submission; no arXiv or web search was required or claimed.

## 6. Final findings and verdict

- **Critical errors:** none.
- **Gaps:** none.
- **Repair hints:** none required.
- **Strict verdict:** `correct`.

Every supplied mathematical assertion passes within its stated smooth positive setting and the expressly accepted prerequisites. The final remarks about degenerating Gauduchon metrics are a statement of work needed for extensions, not a theorem asserting such extensions. No claim of novelty is made.

The book was not edited. The complete structured audit is also preserved in the run's `statement_checks` and `reference_checks` memory channels. The strict JSON follows the required three-field contract.

