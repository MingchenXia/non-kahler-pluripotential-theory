# Verification report: symmetric_equation_selection_01

## Verdict and scope

**Verdict: correct.** There are **0 critical errors and 0 gaps** under the user's accepted inputs and conditional prerequisite. This is a bounded mathematical review, not formal verification.

The proposition proves relative compactness of the normalized family in \(C(X)\), identifies every cluster limit at zero, and proves invariance under every biholomorphism preserving the background and data measure. The corollary provides at least three distinct normalized bounded solutions for the symmetric NUMA data: two smooth and an invariant Hölder solution.

The full construction is a separate prerequisite. Its saved [verification.json](../degenerate_nonuniqueness_01/verification.json) was read and has verdict **correct**, with no errors or gaps. Its additional symmetry specialization was checked afresh here, including an independent parallel cross-check. This report does not re-audit the full NUMA construction or attribute the third-solution theorem to the source PDF.

The book was only read. Neither convergence of the entire family nor smoothness of the third solution is concluded. No general mass bound or uniqueness of a zero-exponent potential is used.

## Answers to the specific checks

Write \(D=M-m\). The exact identities and bounds are
\[
 |w_\lambda|\le D,\qquad -2D\le a_\lambda\le0,\qquad
 e^{\lambda u_\lambda}=c e^{\lambda w_\lambda},\qquad
 \|c e^{\lambda w_\lambda}f\|_{L^p(dV)}
 \le c e^D\|f\|_{L^p(dV)}\quad(0<\lambda\le1).
\]
Thus the fixed-exponent Hölder constants are uniform despite the shift
\((\log c)/\lambda\). If \(V=\int_XdV\), replace \(dV\) by \(dV/V\) and the
right-side density by \(V c e^{\lambda w_\lambda}f\); its norm changes by
the fixed factor \(V^{1-1/p}\).

For \(\mu=f\,dV\), pullback gives
\[
 \operatorname{MA}_\omega(u_\lambda\circ g)
 =g^*(e^{\lambda u_\lambda}\mu)
 =e^{\lambda(u_\lambda\circ g)}g^*\mu
 =e^{\lambda(u_\lambda\circ g)}\mu.
\]
Preservation of \(\mu\) suffices; preservation of \(dV\) separately is
unnecessary. Positive-exponent uniqueness then gives invariance, and
\(\|a\circ g-a\|_\infty\le2\|a-a_{\lambda_j}\|_\infty\) passes it to the same
limit for every \(g\).

For the involution,
\[
 \iota^*A_0=B_0,\quad \iota^*B_0=A_0,\quad
 u\circ\iota=v,\quad v\circ\iota=u,\quad u\ne v.
\]
An invariant \(a\) therefore cannot equal either \(u\) or \(v\).
The uniform Hölder modulus passes directly to \(a\).

## Sequential verification

The following checks follow the supplied proof's textual order. Mathematical steps are written out individually; each item passed.

### 1. prop:symmetric-equation-clusters — hypotheses and equation

1. conventions.tex:3 supplies connected compact complex X, n>=1, without boundary, and defines a Hermitian form as smooth real strictly positive (1,1). Thus compactness is a standing hypothesis, not an omitted new assumption.

2. f is fixed, nonnegative and nonzero in Lp(dV), p>1; on compact X with smooth positive dV this implies 0<integral f dV<infinity. These are exactly the existence-theorem hypotheses; no strictly positive pointwise lower bound for f is required.

3. thm:kn-continuous provides a continuous omega-psh zero-exponent solution and c>0; only uniqueness of c, as accepted and stated in prop:vanishing-exponent, is used.

4. thm:nguyen-exp provides a unique continuous solution for each lambda>0. Its use as uniqueness among bounded solutions is compatible with the accepted Holder theorem: for any fixed bounded solution h, exp(lambda h)f is in Lp, and constant normalization preserves its Monge–Ampere measure; Holder regularity then makes h continuous. No uniform estimate for arbitrary h is needed for this observation.

**Finding:** checked; no critical errors or gaps.

### 2. prop:symmetric-equation-clusters — first proof paragraph: barriers, bounds, densities

1. Choose one continuous solution u; compactness makes m=inf u and M=sup u finite. Write D=M-m>=0.

2. Subtract log(c)/lambda from both accepted barriers. This gives u-M<=w_lambda<=u-m with w_lambda=u_lambda-log(c)/lambda.

3. Because -D<=u-M<=0 and 0<=u-m<=D, one has |w_lambda|<=D uniformly for every lambda>0.

4. sup u_lambda=log(c)/lambda+sup w_lambda; hence a_lambda=w_lambda-sup w_lambda. The bounds -D<=w_lambda<=D give -2D<=a_lambda<=0 and sup a_lambda=0. Constants have zero ddc, so a_lambda remains omega-psh.

5. Constant invariance of the bounded product gives MA_omega(a_lambda)=MA_omega(u_lambda). The exact exponential identity is exp(lambda u_lambda)=exp(log c+lambda w_lambda)=c exp(lambda w_lambda), giving MA_omega(a_lambda)=c exp(lambda w_lambda) f dV.

6. For 0<lambda<=1, exp(-D)<=exp(lambda w_lambda)<=exp(D); therefore ||c exp(lambda w_lambda)f||_Lp(dV)<=c exp(D)||f||_Lp(dV). c is one fixed positive scalar, so the divergent additive shift produces no lambda dependence in this bound.

**Finding:** checked; no critical errors or gaps.

### 3. prop:symmetric-equation-clusters — first proof paragraph: uniform Holder regularity and compactness

1. If V=integral dV is not 1, apply the Holder theorem with dV_hat=dV/V and density F_lambda_hat=V c exp(lambda w_lambda)f. The measure is unchanged, and ||F_lambda_hat||_Lp(dV_hat)=V^(1-1/p)||c exp(lambda w_lambda)f||_Lp(dV). This is a fixed rescaling; if the base datum is renamed, it is f_hat=Vf, so c is unchanged.

2. Fix one beta with 0<beta<2(p-1)/(np+3(p-1)). This interval is nonempty because p>1 and n>=1. Geometry and beta are fixed, a_lambda satisfies the common normalized bound C0=2D (or any larger fixed positive bound), and the right sides have a common Lp bound.

3. The exact uniformity clause of thm:hermitian-holder-elementary (section_holder_regularization.tex:75–84) therefore gives a common beta-Holder constant for all 0<lambda<=1. No dependence on ||u_lambda||_infinity is introduced, because the theorem is applied to a_lambda.

4. Uniform boundedness and the common Holder modulus give equicontinuity on compact metrizable X. Standard Arzela–Ascoli makes the entire family {a_lambda:0<lambda<=1} relatively compact in C(X). No compactness of the parameter interval at zero and no general Monge–Ampere mass estimate are needed.

**Finding:** checked; no critical errors or gaps.

### 4. prop:symmetric-equation-clusters — second proof paragraph: identifying cluster limits

1. For any lambda_j decreasing to zero and uniformly convergent a_lambda_j, the limit a is continuous and bounded with -2D<=a<=0.

2. Uniform convergence implies distributional convergence of ddc a_lambda_j to ddc a; positivity of omega+ddc a_lambda_j passes to the limit. Equivalently, use one common local strictly psh correction on each coordinate ball. Thus a is omega-psh, with its continuous representative.

3. |sup a-sup a_lambda_j|<=||a-a_lambda_j||_infinity implies sup a=0.

4. Since |lambda w_lambda|<=lambda D, ||exp(lambda w_lambda)-1||_infinity<=exp(lambda D)-1 tends to zero; no convergence of w_lambda itself is assumed.

5. ||c(exp(lambda w_lambda)-1)f||_Lp<=c(exp(lambda D)-1)||f||_Lp tends to zero. Finite volume also gives L1, hence weak measure convergence of the right sides to cf dV.

6. The accepted bounded local product continuity applies to this uniformly bounded, uniformly convergent sequence. For a nonclosed background one locally expands using a fixed smooth correction q with a_lambda_j+q psh and smooth remainder omega-ddc q. Each bounded local product converges and the finite sum gives MA_omega(a_lambda_j) tending weakly to MA_omega(a).

7. Uniqueness of a weak limit of measures identifies MA_omega(a)=cf dV. This establishes the equation of each cluster limit, without uniqueness of the limiting potential.

**Finding:** checked; no critical errors or gaps.

### 5. prop:symmetric-equation-clusters — third proof paragraph: symmetry and existence

1. Let mu=f dV and fix g in G. Biholomorphic pullback commutes with ddc and the bounded product. As g*omega=omega, MA_omega(u_lambda composed with g)=g*MA_omega(u_lambda).

2. g*(exp(lambda u_lambda)mu)=exp(lambda(u_lambda composed with g)) g*mu=exp(lambda(u_lambda composed with g))mu. Preservation of mu alone is sufficient: in density notation, g*(f dV)=(f composed with g)J_g dV=f dV, so any volume Jacobian is already absorbed. No assertion g*dV=dV is used.

3. The pullback is a bounded continuous omega-psh solution of the identical positive-exponent equation. Uniqueness for lambda>0 gives u_lambda composed with g=u_lambda.

4. Bijectivity implies sup(u_lambda composed with g)=sup u_lambda; consequently a_lambda composed with g=a_lambda.

5. For a fixed convergent subsequence and every g, ||a composed with g-a||_infinity<=2||a-a_lambda_j||_infinity tends to zero. Hence the same limit is invariant under all of G, even if G is infinite or uncountable; no g-dependent subsequence is required.

6. Apply relative compactness to lambda_j=1/j and extract a subsequence. The parameter still tends to zero, so the previous paragraph supplies a normalized solution of cf dV, and that solution is G-invariant.

7. No step uses zero-exponent potential uniqueness, a bounded mass hypothesis, or equality of all cluster limits.

**Finding:** checked; no critical errors or gaps.

### 6. cor:numa-third-solution — first proof paragraph: even cutoff, parity, invariant backgrounds

1. The full base construction is the user-specified conditional prerequisite. Its saved report results/degenerate_nonuniqueness_01/verification.json was read and has verdict correct with no errors or gaps. This is a dependency-status observation, not a replacement for the fresh symmetry checks below.

2. section_degenerate_nonuniqueness.tex:108 requires kappa smooth with compact support in (-2,2) and kappa=1 on [-3/2,3/2]. Replacing any admissible kappa by (kappa(r)+kappa(-r))/2 preserves these properties and makes it even. A nonnegative cutoff can also be retained. The correction proof at lines 113–117 remains valid for a fixed such cutoff and sufficiently small positive epsilon; choosing the cutoff even does not change the required plateau derivatives.

3. rho(r)=epsilon(r^2-1)kappa(r) is even. It vanishes at both ends, so its global extension is also invariant.

4. At lines 54–59 beta is even with integral 2 and F(r)=-1+integral from -1 to r of beta. Substituting t=-s gives F(-r)=-F(r) on (-1,1); the prescribed constant tails have the same parity. Thus w=F(r) satisfies w composed with iota=-w.

5. The block swap iota[A:B]=[B:A] is induced by an invertible complex linear map, hence a global biholomorphism with square identity. It preserves U={A!=0,B!=0} and r composed with iota=-r.

6. From P=ddc log|A|^2 and Q=ddc log|B|^2, biholomorphic pullback gives iota*P=Q and iota*Q=P. Holomorphic changes of homogeneous lift have pluriharmonic log squared modulus and do not change these forms. R=dr wedge dc r satisfies iota*R=d(-r) wedge dc(-r)=R.

7. In the central interval, p=beta/2 is even, q=beta'/2 is odd, b(r)=a(-r), and chi is even. Thus z0(-r)=sqrt(q(-r)^2+chi(-r)^2)=z0(r), x(-r)=p(r)+b(r)=y(r), and y(-r)=x(r). The exterior definitions at line 80 impose exactly the same reflection identities, so they hold everywhere, including the flat joins.

8. Using omega0=x(r)P+y(r)Q+z(r)R, iota*omega0=x(-r)Q+y(-r)P+z(-r)R=omega0. The equality extends from dense U to all of X by the smooth extensions.

9. Because pullback commutes with ddc and rho composed with iota=rho, omega=omega0+ddc rho is invariant.

10. omega_X is invariant: the block swap preserves |A|^2+|B|^2, hence its local Fubini–Study Hessian. Equivalently use omega_X=sigma(r)P+sigma(-r)Q+sigma'(r)R with sigma' even. Smooth extension again yields the global identity.

**Finding:** checked; no critical errors or gaps.

### 7. cor:numa-third-solution — second proof paragraph: form swap, measure, normalized potentials

1. H=(1/2)ddc w, so iota*H=(1/2)ddc(-w)=-H. This also follows from p even, q odd, and the frame transformation in H=p(P-Q)+qR.

2. A0=omega0-H and B0=omega0+H give iota*A0=B0 and iota*B0=A0.

3. Using the prerequisite's equality A0^3=B0^3, iota*(A0^3)=(iota*A0)^3=B0^3=A0^3. As f omega_X^3=A0^3, the required data measure is invariant. Invariance of omega_X also implies f composed with iota=f, but this stronger fact is unnecessary for applying the proposition.

4. The formulas tilde u=-w/2-rho and tilde v=w/2-rho give tilde u composed with iota=tilde v and tilde v composed with iota=tilde u.

5. Bijectivity of iota gives their common supremum S. Therefore u=tilde u-S and v=tilde v-S still satisfy u composed with iota=v and v composed with iota=u.

6. With this common normalization, v-u=w exactly; F takes different constant values at the two ends, so w is nonconstant and u!=v.

7. If either u or v were invariant under iota, the swap identity would force u=v. Thus neither constructed normalized solution is invariant.

**Finding:** checked; no critical errors or gaps.

### 8. cor:numa-third-solution — third proof paragraph: scalar, application, third solution

1. Set dV=omega_X^3. The prerequisite provides a smooth strictly positive Hermitian omega on compact P^3 and a smooth nonnegative nonzero f. Hence f is Lp for every finite p>1, even though it vanishes on an open set. The preceding checks supply invariance of omega and f dV under G={id,iota}. These are all hypotheses of the proposition.

2. The prerequisite's equation is MA_omega(u)=f omega_X^3, already with scalar 1. Uniqueness of the zero-exponent scalar identifies the proposition's c=1. This invokes no uniqueness of u or v.

3. conventions.tex:7–8 has dc=i/(4pi)(barpartial-partial) and ddc=i/(2pi)partial barpartial. section_degenerate_nonuniqueness.tex:15 specifies that all source (1,1)-forms are divided by 4pi while potentials are unchanged. Both A0^3 and omega_X^3 acquire the same factor (4pi)^(-3); their ratio f and the scalar 1 are unchanged. H=(1/2)ddc w and the displayed tilde potentials are therefore in the correct convention. Normalizing dV for the Holder theorem rescales the density as well and does not change this conclusion.

4. The proposition gives at least one normalized bounded invariant cluster solution a with MA_omega(a)=f omega_X^3.

5. If a=u then invariance of a would imply u=u composed with iota=v, a contradiction. If a=v the same argument gives v=u. Thus a is distinct from each of the two smooth solutions.

6. For one fixed admissible Holder exponent beta the uniform bound |a_lambda(x)-a_lambda(y)|<=C d(x,y)^beta passes to every uniform limit; hence a is Holder. Alternatively apply the accepted Holder theorem to its bounded equation with the smooth density f.

7. u, v and a are therefore at least three distinct normalized bounded solutions; u and v are smooth by the prerequisite and a is Holder. No smoothness of a is proved or needed.

**Finding:** checked; no critical errors or gaps.

### 9. Closing paragraph and complete-proof scope

1. The third-solution statement is a new deduction from the accepted approximation theory and the conditional NUMA construction. The proof does not attribute it to NUMA or require any new external paper theorem.

2. The argument only extracts subsequences and identifies their measures and symmetries. It neither proves all cluster limits are equal nor proves convergence of the entire normalized family. The closing distinction between selection for this procedure and uniqueness of all limiting-equation solutions is logically correct.

3. All stated analytic assumptions have a role: compactness for bounded extrema and Arzela–Ascoli; Hermitian positivity for existence, barriers and Holder regularity; p>1 for the positive Holder-exponent range; nonzero f for positive scalar/exponential existence; invariance of omega and the data measure for pullback uniqueness; nonconstant w and involution swap for the third solution.

4. The audit of the base construction includes an independent bounded-mass statement, but this deduction does not use it. The normalized C0 and Lp bounds here come directly from one solution and the accepted barriers.

5. Every deduction in the supplied proof has been checked in textual order; no critical errors or gaps were detected under the accepted inputs and the stated conditional prerequisite.

**Finding:** checked; no critical errors or gaps.

## Exact reference and definition checks

The proof cites accepted internal manuscript results. Their exact statements and applicability were checked below. The accepted local continuity input is uniform-convergence continuity; it was not confused with the decreasing-convergence statement printed in the bounded-products chapter. No new external-paper reference is introduced by this deduction, so the external arXiv-search-first and web-fallback procedure is not triggered. The supplied NUMA paper and the full construction belong to the designated separate audit.

### R1. conventions.tex and bounded product definition

**Location of use:** Proposition — standing definitions and normalized bounded solution class.

**Source:** /Users/mingchen/Non-Kahler/book/author/conventions.tex:3–20; /Users/mingchen/Non-Kahler/book/author/chapter_products.tex:18–26.

**Statement or definition checked:** X is a connected compact complex manifold of complex dimension n>=1, without boundary; Hermitian means smooth real strictly positive (1,1)-form. dc=i/(4pi)(barpartial-partial), ddc=i/(2pi)partial barpartial. Locally, for p=u+q plurisubharmonic and beta=theta-ddc q, (theta+ddc u)^k=sum_{j=0}^k binom(k,j)(ddc p)^j wedge beta^(k-j).

**Context and application:** These are the actual manuscript standing hypotheses and bounded-product definition. They justify compactness of X, exact convention, invariance under constant shifts, and use of a smooth local correction instead of a local potential for nonclosed omega.

**Finding:** matched and applicable; no critical errors or gaps.

### R2. thm:kn-continuous

**Location of use:** Proposition — zero-exponent solution.

**Source:** /Users/mingchen/Non-Kahler/book/author/chapter_weak_equations.tex:6–18.

**Statement or definition checked:** For a Hermitian form omega, smooth positive volume form dV, and nonnegative f in Lp(X,dV), p>1, with integral f dV>0, there are c>0 and u in PSH(X,omega) intersect C(X) such that (omega+ddc u)^n=c f dV. One may normalize sup_X u=0.

**Context and application:** Exact accepted internal existence statement. The current data meet all hypotheses. The manuscript explicitly says it does not assert uniqueness of the normalized potential. The proof chooses one u only.

**Finding:** matched and applicable; no critical errors or gaps.

### R3. thm:nguyen-exp

**Location of use:** Proposition — positive-exponent solutions and symmetry.

**Source:** /Users/mingchen/Non-Kahler/book/author/chapter_weak_equations.tex:20–29.

**Statement or definition checked:** Under the same Hermitian, volume and nonnegative nonzero Lp hypotheses, for every lambda>0 there is a unique continuous omega-plurisubharmonic u_lambda satisfying (omega+ddc u_lambda)^n=exp(lambda u_lambda) f dV.

**Context and application:** Exact accepted internal theorem in the book's ddc convention. lambda stays strictly positive wherever uniqueness is used. Pullbacks solve this same equation. The bounded formulation is justified by applying the accepted Holder theorem to any fixed bounded solution, since its exponential density is Lp. No source normalization change is applied again.

**Finding:** matched and applicable; no critical errors or gaps.

### R4. prop:vanishing-exponent

**Location of use:** Proposition — barriers and uniqueness of scalar; corollary — c=1.

**Source:** /Users/mingchen/Non-Kahler/book/author/chapter_weak_equations.tex:60–89.

**Statement or definition checked:** If u is continuous omega-psh and c>0 satisfy omega_u^n=c f dV, m=inf_X u and M=sup_X u, then u+log(c)/lambda-M <= u_lambda <= u+log(c)/lambda-m. In particular ||lambda u_lambda-log c||_infinity<=lambda(M-m), exp(lambda u_lambda) tends uniformly to c, and the scaling constant c is unique.

**Context and application:** The exact sign and placement of m, M and log(c)/lambda match the supplied proof. Subtracting the shift yields the displayed uniform bounds; unique scalar identifies c=1 for the constructed equation. No zero-exponent potential uniqueness follows or is used.

**Finding:** matched and applicable; no critical errors or gaps.

### R5. thm:hermitian-holder-elementary

**Location of use:** Proposition — uniform Holder estimate; corollary — regularity of third solution.

**Source:** /Users/mingchen/Non-Kahler/book/author/section_holder_regularization.tex:6,75–84.

**Statement or definition checked:** For Hermitian omega and smooth positive probability dV, if p>1 and u in PSH(X,omega) intersect L-infinity solves MA_omega(u)=f dV with 0<=f in Lp(dV), then u is Holder continuous with every exponent 0<beta<2(p-1)/(np+3(p-1)). For a fixed bound -C0<=u<=0 and a fixed bound for ||f||_p, the Holder constants are uniform.

**Context and application:** The exact uniformity clause was read, not inferred from qualitative regularity. Apply it to normalized a_lambda with C0=2(M-m) and density c exp(lambda w_lambda)f; normalize dV together with its density by one fixed scalar if needed. Geometry, exponent, C0 and Lp bound are all independent of lambda. Degenerate densities are expressly allowed; no lower bound or mass hypothesis is required.

**Finding:** matched and applicable; no critical errors or gaps.

### R6. Accepted local product continuity; standard Arzela–Ascoli and biholomorphic pullback

**Location of use:** Proposition — limit identification, compactness and pullback.

**Source:** Explicit accepted inputs in the user's statement; local product definition in /Users/mingchen/Non-Kahler/book/author/chapter_products.tex:18–26.

**Statement or definition checked:** Bounded local Monge–Ampere products are continuous under uniform convergence with uniform local boundedness. A uniformly bounded equicontinuous family in C(X) on compact metric X is relatively compact. Biholomorphic pullback commutes with ddc and the bounded local products.

**Context and application:** All sequence hypotheses are established before applying product continuity. This uniform-convergence input is explicitly accepted by the user; it is not silently identified with the decreasing-convergence formulation in chapter_products.tex. Arzela–Ascoli and pullback are the stipulated standard tools. Measure pullback is g*(h mu)=(h composed with g)g*mu, which requires preservation of mu alone.

**Finding:** matched and applicable; no critical errors or gaps.

### R7. thm:degenerate-hermitian-nonuniqueness

**Location of use:** Corollary — base construction and fresh symmetry specialization.

**Source:** /Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex:6–132; /Users/mingchen/Non-Kahler/research/rethlas/verification/results/degenerate_nonuniqueness_01/verification.json.

**Statement or definition checked:** On X=P^3 there exist a smooth Hermitian omega with d omega!=0, a smooth nonnegative nonzero f, and distinct smooth u,v in PSH(X,omega), sup u=sup v=0, such that (omega+ddc u)^3=f omega_X^3=(omega+ddc v)^3. The density vanishes on a nonempty open set, and both potentials have minimal singularities.

**Context and application:** The full NUMA construction is the explicit conditional prerequisite, whose saved audit was found correct. Its definitions and exact parity formulas were independently read and checked for this corollary. The source-form factor 4pi is already accounted for in manuscript line 15; it does not alter f or c=1. The current proof does not claim that the supplied NUMA-Xia.pdf states the third-solution result. No new external source theorem is invoked.

**Finding:** matched and applicable; no critical errors or gaps.

## Aggregate findings and verdict rule

- Sequential records: 9, containing 57 individual checks.
- Reference and definition records: 7.
- Critical errors: 0.
- Gaps: 0.
- Failed mathematical checks: 0.
- Strict verdict: **correct**, because both issue lists are empty.
- Repair hints: empty; no repair is required under the accepted inputs.

Detailed records are persisted under `memory/symmetric_equation_selection_01/`. The machine-readable result is [verification.json](verification.json).
