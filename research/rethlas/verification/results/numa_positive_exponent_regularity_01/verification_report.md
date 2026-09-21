# Verification report: numa_positive_exponent_regularity_01

## Verdict and scope

**Correct.** All 73 individual deductions in 15 ordered statement records and all six reference/application records pass. Critical errors: 0. Gaps: 0. Repair hints: none.

The assertion is for every fixed positive exponent and the entire open zero-density band. The unique bounded exponential solution differs from the explicitly selected u_star by one constant there. Both potentials are C1,1 on the band and fail to have second derivatives at every point of the two transition hypersurfaces. The audit establishes no global C1,1 property for u_lambda and makes no claim for strictly positive density.

## Accepted inputs and actual sources read

The full supplied proof was examined in its textual order. The following book sources and full saved reports were read:

- [section_degenerate_nonuniqueness.tex](/Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex) and [its passed report](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/degenerate_nonuniqueness_01/verification.json).
- [section_numa_radial_family.tex](/Users/mingchen/Non-Kahler/book/author/section_numa_radial_family.tex) and [its passed report](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/numa_radial_family_01/verification_report.md).
- [section_symmetric_equation_selection.tex](/Users/mingchen/Non-Kahler/book/author/section_symmetric_equation_selection.tex) and [its passed report](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/symmetric_equation_selection_01/verification_report.md).
- [section_numa_canonical_limit.tex](/Users/mingchen/Non-Kahler/book/author/section_numa_canonical_limit.tex) and [its passed report](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/numa_selected_limit_01/verification_report.md).

The earlier selected-limit report's conditional exact existence/root requirement is satisfied by the now-passed radial-family audit. Chapter10 exponential existence and bounded uniqueness, standard BV calculus and bounded local Bedford–Taylor uniform continuity are expressly accepted. The actual chapter_weak_equations.tex, conventions.tex and bounded-product definition in chapter_products.tex were also inspected. No prior theorem is silently strengthened.

## Decisive checks

The coefficient convention is
\[
A(r,s)=(x(r)+s)(y(r)-s),\quad
\Phi(r,s)=xys+\frac{y-x}{2}s^2-\frac{s^3}{3},
\quad P\wedge Q\wedge R=dr\wedge\nu.
\]
Thus \(f\omega_X^3=6k(r)\,dr\wedge\nu\), and the new equation gives exactly
\[
d[\Phi(r,h_\lambda)]
=\bigl(e^{\lambda(G_\lambda-\rho)}k
       -A(r,h_\lambda)z+\Phi_r(r,h_\lambda)\bigr)\,dr.
\]
The geometric convolution proof precedes identifying the source coefficient. Its signed-product convergence requires a common lower Hessian bound, furnished by positivity; no upper Hessian bound or differentiability of the original solution is inserted.

For each fixed \(\lambda>0\), boundedness makes the exponential coefficient locally bounded. At an upward jump, the flux atom would be
\[
\int_{h_\lambda(r_0-)}^{h_\lambda(r_0+)}
 (x(r_0)+s)(y(r_0)-s)\,ds>0,
\]
because both traces are admissible and \(x+y>0\), including at \(r_0=\pm1\). The right side has no atoms, so no jumps remain. This proves continuity of the BV slope, while allowing a continuous singular derivative at this intermediate stage. It then gives \(G_\lambda\in C^1\), continuous \(k_\lambda\), and \(C^1\) flux inversion where \(A>0\).

On \(0<r<1\), the exact cutoffs give \(x=p>0\), \(y=p+b\ge p>0\), \(z=z_0>0\), and \(p'<0\). Symmetry gives \(h_\lambda(0)=0\). The interior branch is \(-\int_0^r z_0\) and reaches \(-p\) at the unique root \(t_*\). Any departure component has a strictly negative left endpoint value and cannot reach zero because \(h_\lambda'=-z_0<0\). Hence its whole interior obeys \((h_\lambda+p)'=p'-z_0<0\), contradicting departure from a zero. This excludes accumulating components and removes any contact-set ambiguity.

Finally,
\[
h_\lambda'(t_*-)=-z_0(t_*)<0<
-p'(t_*)=h_\lambda'(t_*+).
\]
Through every \(q=[A:B]\) at \(r(q)=r_0\), the curve
\(\gamma_q(s)=[e^{(s-r_0)/2}A:B]\) has \(r(\gamma_q(s))=s\).
Restriction gives \(G_\lambda(s)-\rho(s)\); subtracting smooth \(\rho\) cannot remove the unequal one-sided second derivatives. Reflection gives the same failure at \(-t_*\).

## Full sequential deduction audit

### 1. Input contract and opening paragraph

**1.1.** The supplied section is usable proof text. The audited assertion is for every fixed finite lambda>0 and for the band {-1<r<1}; u_lambda is the unique bounded omega-psh solution stipulated in the input.

**1.2.** All four preceding audits pass. The exact symmetric root and explicit u_star supplied by numa_radial_family_01 discharge the conditional dependency stated in numa_selected_limit_01. No unproved existence or exhaustiveness of a radial family is being assumed.

**1.3.** The symmetric projective data use an even rho, smooth strictly positive Hermitian omega, and smooth nonnegative nonzero f. The introductory loss-of-C2 assertion is the proposition's conclusion, justified by the argument below.

**Finding:** checked; no critical error or gap.

### 2. prop:numa-positive-exponent-nonc2 — uniqueness, invariance, and scalar reduction

**2.1.** For mu=f omega_X^3 and g in K, bounded-product pullback and g*omega=omega give MA_omega(u_lambda composed with g)=e^{lambda(u_lambda composed with g)}g*mu=e^{lambda(u_lambda composed with g)}mu.

**2.2.** Pullback preserves boundedness and omega-psh positivity. Accepted uniqueness for the same lambda>0 therefore implies u_lambda composed with g=u_lambda, without averaging or altering the equation.

**2.3.** Block-unitary orbits in U are exactly r-level sets: after normalizing total squared norm, fixed r fixes both positive block lengths and the two unitary groups act transitively. Since rho is radial, u_lambda+rho=G_lambda(r). Bounded u_lambda and smooth bounded rho give bounded G_lambda.

**2.4.** The same rho occurs in omega=omega0+ddc rho and u_lambda=G_lambda(r)-rho; hence omega+ddc u_lambda=omega0+ddc G_lambda(r) exactly. The book convention is ddc=i/(2pi) partial barpartial, with no new source rescaling.

**Finding:** checked; no critical error or gap.

### 3. prop:numa-positive-exponent-nonc2 — positivity before any regularity assumption

**3.1.** The weak scalar chain rule follows distributionally by scalar convolution along the smooth submersion r. Testing the positive current in the dual radial direction annihilating P,Q gives G_lambda''+z>=0; this uses the original solution's positivity, not positivity of the approximants.

**3.2.** On a larger compact interval choose smooth Z with Z''=z. Then G_lambda+Z has nonnegative distributional second derivative and a finite convex representative. It is locally Lipschitz, so G_lambda is locally Lipschitz. Its continuous representative agrees with the original canonical qpsh representative.

**3.3.** Subtracting smooth Z' from the monotone weak derivative of the convex function gives h_lambda=G_lambda' in BV_loc. The radial inequality is dh_lambda+z dr>=0.

**3.4.** Horizontal positivity gives -x<=h_lambda<=y almost everywhere. BV traces and continuity of x,y give the same bounds for h_lambda(r-) and h_lambda(r+) at every finite r.

**3.5.** The singular part of dh_lambda is nonnegative because z dr is absolutely continuous. In particular, every possible jump is upward. No C1, absolute-continuity-of-h, or C1,1 premise is used.

**Finding:** checked; no critical error or gap.

### 4. prop:numa-positive-exponent-nonc2 — exact positive-exponent radial coefficient

**4.1.** The actual flux conventions are A(r,s)=(x+s)(y-s)=xy+(y-x)s-s^2 and Phi(r,s)=xy s+(y-x)s^2/2-s^3/3. Thus partial_s Phi=A; partial_r keeps s fixed.

**4.2.** Under U=R times Y induced by [A:B] -> [e^{t/2}A:B], P,Q,d^c r are independent of t and have no scaling-direction component. The fixed positive angular volume satisfies P wedge Q wedge R=dr wedge nu.

**4.3.** The smooth rank-one formula is (omega0+ddc G)^3=6 A(r,h)(z+h') dr wedge nu. Rewriting gives radial coefficient Az dr+d[Phi(r,h)]-partial_r Phi(r,h) dr, after dividing by 6 nu.

**4.4.** The accepted data measure is exactly 6 k(r) dr wedge nu, where k=0 on |r|<=1 and k=xyz outside. Multiplication by e^{lambda u_lambda}=e^{lambda(G_lambda-rho)} therefore gives precisely 6 k_lambda(r) dr wedge nu. There is no angular Jacobian, derivative of the exponential, extra scalar, factorial, or 4pi factor.

**4.5.** For each fixed lambda>0, bounded u_lambda implies 0<e^{-lambda ||u_lambda||infinity}<=e^{lambda u_lambda}<=e^{lambda ||u_lambda||infinity}. Since k is smooth, k_lambda is locally bounded measurable at the initial bounded stage. No estimate uniform in lambda is required.

**Finding:** checked; no critical error or gap.

### 5. prop:numa-positive-exponent-nonc2 — extension of the scalar convolution and signed-product proof

**5.1.** The cited lemma proves a geometric identity before it identifies the prescribed k. On a compact interval inside a larger one, convolve the established Lipschitz G_lambda. Then G_epsilon converges uniformly, h_epsilon is uniformly bounded, and h_epsilon converges almost everywhere and in every finite Lq to h_lambda.

**5.2.** Convolving dh_lambda+z dr>=0 gives h_epsilon'>=-(z*eta_epsilon), a common lower bound. The formula ddc G_epsilon(r)=h_epsilon(P-Q)+h_epsilon'R, bounded horizontal slopes, smooth local frame, and semipositivity of R give a common lower complex Hessian bound.

**5.3.** On each smaller coordinate ball a fixed smooth quadratic B makes G_epsilon(r)+B and G_lambda(r)+B bounded psh with uniform convergence. Accepted bounded local BT continuity applies to each wedge power.

**5.4.** Expand (omega0+ddc G_epsilon)^3 using the psh powers of ddc(G_epsilon+B) and the fixed smooth remainder omega0-ddc B. Each term converges; the remainder need not be positive or closed. The limit is exactly MA_omega(u_lambda) by the accepted bounded-product definition.

**5.5.** On the scalar side, A(r,h_epsilon)z and partial_r Phi(r,h_epsilon) converge in L1, while Phi(r,h_epsilon) converges in L1 and its distributional derivative converges. Thus the same weak identity holds. No pointwise product A dh is assigned across jumps.

**5.6.** The approximants are not asserted to solve an exponential equation. Only after taking the geometric measure limit is the actual solution equation used to identify the coefficient as k_lambda.

**5.7.** The resulting identity is d[Phi(r,h_lambda)]=[k_lambda-A(r,h_lambda)z+partial_r Phi(r,h_lambda)]dr. This extension requires only local boundedness of k_lambda at this point, exactly as supplied.

**Finding:** checked; no critical error or gap.

### 6. prop:numa-positive-exponent-nonc2 — absence of atoms and elimination of all jumps

**6.1.** At the BV stage h_lambda is locally bounded. Together with smooth x,y,z and locally bounded k_lambda, every term on the flux right side is locally bounded measurable. Its measure is absolutely continuous and has no atoms.

**6.2.** At a putative jump r0, the atom of d[Phi(r,h_lambda)] is the difference of the two traces Phi(r0,h_lambda(r0+))-Phi(r0,h_lambda(r0-)), equal to the integral of (x(r0)+s)(y(r0)-s) between the traces.

**6.3.** The jump can only be upward, and both traces belong to [-x(r0),y(r0)]. On the interior of this interval the integrand is strictly positive.

**6.4.** The actual coefficient construction has x+y>0 at every finite r, including r=+-1 where x+y=1. Every upward jump of positive size therefore has strictly positive flux atom, even if a trace is at a boundary. This contradicts the atom-free right side.

**6.5.** Consequently all one-sided traces of the BV slope agree. Its continuous representative exists. This inference permits a continuous singular/Cantor component of dh_lambda at this stage; it does not assert h_lambda is absolutely continuous.

**Finding:** checked; no critical error or gap.

### 7. prop:numa-positive-exponent-nonc2 — C1 primitive, continuous coefficient, and flux inversion

**7.1.** A locally Lipschitz G_lambda is locally absolutely continuous. Since its weak derivative equals the continuous representative h_lambda almost everywhere, the fundamental theorem of calculus shows G_lambda is C1 with derivative h_lambda everywhere.

**7.2.** Smooth rho and k then make k_lambda=e^{lambda(G_lambda-rho)}k continuous. This upgrade is established before invoking a continuous right-hand flux.

**7.3.** W(r)=Phi(r,h_lambda(r)) is continuous, and its distributional derivative is now the continuous function k_lambda-Az+Phi_r. Therefore W is C1.

**7.4.** Where A(r,h_lambda)>0, the smooth map (r,s)->(r,Phi(r,s)) has nonzero Jacobian in s and a smooth local inverse. Applying it to (r,W(r)) gives h_lambda in C1 on this open set.

**7.5.** Differentiating there gives Phi_r+A h_lambda'=k_lambda-Az+Phi_r, hence h_lambda'=k_lambda/A-z. The proof applies no inversion at A=0 and makes no global regularity conclusion from this step.

**Finding:** checked; no critical error or gap.

### 8. prop:numa-positive-exponent-nonc2 — zero-density band and parity

**8.1.** On -1<r<1, k=0, so k_lambda=0 exactly for every lambda>0, regardless of the value or additive level of u_lambda.

**8.2.** Exchange invariance and even rho imply G_lambda(-r)=G_lambda(r). Since G_lambda is now C1, its derivative is odd and h_lambda(0)=0.

**8.3.** The actual cutoff has a=0 for r>=-1/3. Hence on 0<r<1, x=p>0 and y=p+b>=p>0, while z=z0>0 and p'=q<0. At zero, a=b=0 and both horizontal factors at h_lambda=0 equal p(0)>0.

**Finding:** checked; no critical error or gap.

### 9. prop:numa-positive-exponent-nonc2 — first-contact argument

**9.1.** Continuity and strict horizontal positivity at zero give an initial interval with -p<h_lambda<y. The interior flux equation there reduces to h_lambda'=-z0, and h_lambda(0)=0 gives h_lambda(r)=-integral_0^r z0(s) ds.

**9.2.** For r>0 this branch is strictly negative and decreasing, while y(r)>0. It cannot first contact the upper boundary.

**9.3.** For L(t)=integral_0^t z0-p(t), the actual smooth coefficients give L(0)=-p(0)<0, L(1)=integral_0^1 z0>0, and L'=z0-p'>0 on (0,1). The accepted radial construction's unique root t_star therefore lies in (0,1).

**9.4.** On the initial branch, h_lambda+p=-L. It stays positive for r<t_star, vanishes at t_star, and would be negative after it. Continuity prevents the interior interval ending earlier without a contact; local inversion extends it at any earlier strictly interior endpoint. Thus the first contact is exactly h_lambda(t_star)=-p(t_star).

**Finding:** checked; no critical error or gap.

### 10. prop:numa-positive-exponent-nonc2 — no-departure argument with all sign hypotheses

**10.1.** The lower slope constraint on (0,1) is h_lambda>=-p. The set E={r in (t_star,1):h_lambda(r)+p(r)>0} is open by continuity.

**10.2.** Every connected component (alpha,beta) of E has finite left endpoint alpha in [t_star,1), with h_lambda(alpha)+p(alpha)=0 by continuity and the first-contact value. Since p(alpha)>0, h_lambda(alpha)=-p(alpha)<0.

**10.3.** Immediately to the right of alpha, h_lambda<0<y. Within the component the lower factor is positive. For as long as h_lambda remains negative, both factors are positive, so h_lambda'=-z0<0.

**10.4.** Integration from alpha+epsilon followed by epsilon down to zero shows h_lambda remains below its strictly negative endpoint value. A first zero is impossible. Thus the interior equation applies on the whole proposed component, including when its right endpoint is 1.

**10.5.** Throughout the component, (h_lambda+p)'=p'-z0<0. Integrating from the continuous zero at alpha gives h_lambda(r)+p(r)=integral_alpha^r(p'-z0)<0, contradicting membership in E.

**10.6.** This excludes every component separately, including arbitrarily many or accumulating components. E is empty and h_lambda=-p pointwise on [t_star,1). No differentiability at contact or prior absolute continuity on the contact set has been assumed; no Cantor variation can remain on this explicitly identified branch.

**Finding:** checked; no critical error or gap.

### 11. prop:numa-positive-exponent-nonc2 — displayed slope and one additive constant

**11.1.** Oddness gives h_lambda=p on (-1,-t_star], the central expression -integral_0^r z0 on [-t_star,t_star], and -p on [t_star,1). Evenness of z0 makes the central expression odd.

**11.2.** At t_star, the root identity integral_0^{t_star} z0=p(t_star) matches the central and right branches; at -t_star, even p,z0 give the matching central and left branches.

**11.3.** The accepted symmetric construction with I=-t_star,J=t_star has exactly these derivatives for u_star+rho; supremum normalization changes only the scalar primitive's constant.

**11.4.** Both scalar primitives are C1 on the connected interval (-1,1) with identical derivatives everywhere. Their difference is one constant C_lambda on that entire interval, not separate constants on subbands. Subtracting the same rho gives u_lambda-u_star=C_lambda on the whole band.

**11.5.** Block-unitary reduction already identifies the values on every r-level, and the band is the product (-1,1) times the connected orbit Y. The constant therefore applies to all its manifold points.

**Finding:** checked; no critical error or gap.

### 12. prop:numa-positive-exponent-nonc2 — local C1,1 regularity

**12.1.** The displayed slope is continuous with finitely many smooth pieces. On those pieces its derivatives are p', -z0, and -p', all bounded on [-1,1]. Integrating across matching joins proves the slope is Lipschitz.

**12.2.** Each scalar primitive is C1 with Lipschitz derivative, hence C1,1 on (-1,1). At the transition points the lack of a classical derivative of the slope does not conflict with Lipschitz regularity.

**12.3.** On relatively compact coordinate charts in U, r is smooth with bounded first and second derivatives, and d[G(r)]=h(r)dr is locally Lipschitz. Subtracting smooth rho preserves C1,1.

**12.4.** The closure of the band stays a compact subset of U, as the block norm ratio stays bounded away from zero and infinity. The stated band regularity is therefore legitimate on the manifold. No exterior slope of u_lambda or behavior at the projective ends is inferred.

**Finding:** checked; no critical error or gap.

### 13. prop:numa-positive-exponent-nonc2 — unequal second derivatives at positive transition

**13.1.** The root is strictly inside (0,1), where z0(t_star)>0 and p'(t_star)<0 by the exact data. Thus h_lambda'(t_star-)=-z0(t_star)<0 and h_lambda'(t_star+)=-p'(t_star)>0.

**13.2.** These are the actual left and right difference-quotient limits of the continuous slope, since its adjoining smooth branches match at t_star. Their opposite signs give unequal limits.

**13.3.** A scalar primitive G_lambda with derivative h_lambda consequently has no second derivative at t_star, a stronger obstruction than mere discontinuity of an existing second derivative.

**13.4.** The same computed slope applies to the scalar primitive u_star+rho, so it has the identical obstruction.

**Finding:** checked; no critical error or gap.

### 14. prop:numa-positive-exponent-nonc2 — transfer to every manifold point and negative transition

**14.1.** Every point with finite r=+-t_star lies in U. The accepted local expression for partial r has a nonzero -d tau/tau component, so dr is nonzero and r is a smooth real submersion there.

**14.2.** For each q=[A:B] with r(q)=r0, the smooth curve gamma_q(s)=[e^{(s-r0)/2}A:B] passes through q at s=r0 and satisfies r(gamma_q(s))=s. It can be restricted to any small coordinate neighborhood of q.

**14.3.** Along this curve u_lambda(gamma_q(s))=G_lambda(s)-rho(s). Its two one-sided second derivatives at t_star differ by the nonzero amount z0(t_star)-p'(t_star). The smooth term rho'' has the same value from both sides and cannot cancel their discrepancy.

**14.4.** If u_lambda were C2 at q, its restriction to every such smooth curve would have a second derivative there. The exhibited curve contradicts this at each point of r=t_star, with no exceptional angular points.

**14.5.** Oddness of h_lambda gives h_lambda'(-t_star-)=-p'(t_star)>0 and h_lambda'(-t_star+)=-z0(t_star)<0. The identical argument applies at each point of r=-t_star and to u_star.

**14.6.** The hypersurfaces are nonempty because r attains every real value on U. Failure at their points rules out global C2 regularity for each positive-exponent solution.

**Finding:** checked; no critical error or gap.

### 15. Closing paragraph and complete hypothesis-use/scope audit

**15.1.** The original f vanishes throughout the closed band |r|<=1; thus it vanishes on the open band used here. The new result concerns a smooth nonnegative density with an open zero set.

**15.2.** For each lambda>0, e^{lambda u} is strictly increasing as a function of u, and accepted exponential uniqueness applies although f vanishes. The text refers to this scalar exponential factor and does not require the full product f e^{lambda u} to be strictly increasing at points where f=0.

**15.3.** The construction therefore shows that smoothness and nonnegativity of the input f do not guarantee C2 regularity, even with positive exponential parameter. It makes no assertion about smooth strictly positive densities in the Hermitian Calabi-Yau theorem and no novelty claim.

**15.4.** All deductions work for an arbitrary fixed lambda>0. The argument neither passes to lambda=0 nor relies on smallness of lambda, convergence as lambda tends to zero, or bounds uniform over lambda.

**15.5.** Boundedness supplies finite scalar data, convex/BV control and bounded exponential coefficient; positivity supplies trace and jump signs; exact coefficient support supplies x=p and y>0; symmetry supplies h(0)=0 and oddness; k=0 supplies the interior ODE; p'<0,z0>0 supply contact and nonC2 signs; explicit accepted u_star supplies the comparison slope; submersion and smooth rho transfer regularity.

**15.6.** No global C1,1 statement for u_lambda is asserted or needed. Global C1,1 for the already accepted u_star is compatible but stronger than the present band conclusion. Exterior flux uniqueness and bounded-end classification from the zero-exponent proof are not imported for u_lambda.

**15.7.** The supplied proof's internal shorthand 'apply verbatim' is justified because all hypotheses of the referenced first-contact and no-departure argument were checked above. No critical error, gap, suspiciously unused necessary assumption, or unsupported existence premise remains.

**Finding:** checked; no critical error or gap.

## Full reference and definition audit

### R1. thm:numa-selected-limit and its accepted prerequisites

**Location:** Proposition data and introductory selected-solution assertion.

**Referenced statement/input:** For the symmetric projective data, u_star is the unique normalized bounded K-invariant solution of MA_omega(u)=f omega_X^3; normalized positive-exponent solutions converge uniformly to u_star as lambda decreases to zero. The selected limit is C1,1.

**Context and exact definitions:** Here K is generated by block unitaries U(2) times U(2) and block exchange, rho is even, and u_star is the explicitly normalized primitive from the symmetric radial pair. The same omega, f, r, p, z0, rho and ddc convention are used. The selected-limit audit's earlier conditional existence/root requirement is discharged by the now-passed radial-family audit.

**Application check:** Only the fixed data and identity of u_star are inherited. The positive-exponent band slope is proved anew and is not inferred from convergence of u_lambda as lambda tends to zero. No global exterior classification for a zero-exponent solution is misapplied to a positive-exponent one.

**Sources:**

- /Users/mingchen/Non-Kahler/book/author/section_numa_canonical_limit.tex
- /Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex
- results/degenerate_nonuniqueness_01/verification.json
- results/numa_selected_limit_01/verification_report.md

**Finding:** matched and applicable under the accepted-input contract; no critical error or gap. No new external search required.

### R2. lem:numa-radial-flux

**Location:** Proof first paragraph — cited radial positivity and flux argument.

**Referenced statement/input:** For a bounded block-unitary-invariant zero-exponent solution, u+rho=G(r), G is locally Lipschitz, h=G' is BV_loc, -x<=h(r+-)<=y, dh+z dr>=0; h is continuous and d[Phi(r,h)]=[k-A(r,h)z+partial_r Phi(r,h)]dr, with A=(x+h)(y-h). Where A>0 the smooth slope obeys h'=k/A-z.

**Context and exact definitions:** The lemma's stated equation is zero-exponent. Its actual proof first obtains positivity/BV and a geometric signed-product identity for any bounded radial omega-psh potential; only afterward does it identify the source coefficient k. The angular volume is fixed, the cube coefficient is 6, and Phi_r holds its scalar argument fixed.

**Application check:** The supplied new proof explicitly extends this mechanism rather than substituting a positive-exponent solution into the lemma's zero-exponent hypothesis. Sequential checks 3-7 verify every changed step: k_lambda=e^{lambda(G-rho)}k is bounded, the weak identity survives the same convolution, all jumps give positive atoms, and continuity precedes flux inversion. No cited smooth-coefficient conclusion is used before its premises are reestablished.

**Sources:**

- /Users/mingchen/Non-Kahler/book/author/section_numa_canonical_limit.tex
- results/numa_selected_limit_01/verification_report.md

**Finding:** matched and applicable under the accepted-input contract; no critical error or gap. No new external search required.

### R3. First two paragraphs of the proof of thm:numa-selected-limit; prop:numa-radial-continuum

**Location:** Proof second paragraph — first contact, no departure, and slope identification.

**Referenced statement/input:** For -1<I<0<J<1 satisfying integral_I^J z0=p(I)+p(J), the slope p, then p(I)-integral_I^r z0, then -p, extended by zero outside [-1,1], has a global C1,1 primitive whose normalization after subtracting rho solves the zero-exponent equation. L(t)=integral_0^t z0-p(t) has a unique root t_star in (0,1); I=-t_star,J=t_star gives an odd slope and even invariant primitive. The selected-limit band argument starting at h(0)=0 reaches -p at t_star and forbids subsequent departures by p'-z0<0.

**Context and exact definitions:** The same exact coefficients satisfy a=0 on (0,1), x=p>0, y=p+b>=p>0, z=z0>0, p'<0, and p,z0 even. t_star is the root integral_0^{t_star}z0=p(t_star), not a different transition parameter from the nonsymmetric subfamily.

**Application check:** Checks 8-11 establish all initial, first-contact and open-component hypotheses for h_lambda. The source's argument truly transfers on the zero-density band because k_lambda=0 there. The precise symmetric member supplies the comparison derivative; no classification of all members or exterior continuation is required.

**Sources:**

- /Users/mingchen/Non-Kahler/book/author/section_numa_radial_family.tex
- /Users/mingchen/Non-Kahler/book/author/section_numa_canonical_limit.tex
- results/numa_radial_family_01/verification_report.md

**Finding:** matched and applicable under the accepted-input contract; no critical error or gap. No new external search required.

### R4. Accepted chapter10 weak exponential theory and passed symmetric-equation-selection audit

**Location:** Proposition existence/uniqueness premise and first proof sentence.

**Referenced statement/input:** For smooth Hermitian omega, smooth positive dV, nonnegative nonzero f in Lp(dV) with p>1, and each lambda>0, the equation MA_omega(u_lambda)=e^{lambda u_lambda}f dV has a unique bounded omega-psh solution. Biholomorphisms preserving omega and f dV preserve that solution.

**Context and exact definitions:** The user explicitly accepts bounded exponential existence/uniqueness. The chapter states continuous existence and also gives bounded exponential order; its conventions already absorb the reference's factor-two ddc and exponent conversion. On compact P^3 the smooth nonnegative nonzero f lies in every finite Lp, and dV=omega_X^3 is smooth positive.

**Application check:** The current equation is used in the book's convention without another factor-two change. The original unnormalized solution is pulled back at the same lambda; constant normalization is not applied to its exponential equation. No assumption f>0 everywhere or restriction lambda<=1 is needed.

**Sources:**

- /Users/mingchen/Non-Kahler/book/author/chapter_weak_equations.tex
- /Users/mingchen/Non-Kahler/book/author/section_symmetric_equation_selection.tex
- results/symmetric_equation_selection_01/verification_report.md

**Finding:** matched and applicable under the accepted-input contract; no critical error or gap. No new external search required.

### R5. Expressly accepted BV/convex calculus, bounded local BT uniform continuity, and standard calculus

**Location:** Weak flux and scalar-to-manifold regularity steps.

**Referenced statement/input:** A finite one-dimensional convex function is locally Lipschitz with BV derivative; BV traces give jump atoms and a continuous representative when all jumps vanish. Bounded local Bedford-Taylor powers converge under locally uniform convergence after a common psh correction. A C1 flux with nonzero scalar partial derivative can be locally inverted, and continuous finitely piecewise smooth slopes with bounded derivatives are Lipschitz.

**Context and exact definitions:** BT uniform continuity is an explicit accepted input; it is not confused with the decreasing-approximation formulation printed in the product chapter. Signed products use a fixed smooth correction and finite expansion. The independent frame yields a smooth submersion r; through every [A:B] at r0, gamma(s)=[e^{(s-r0)/2}A:B] satisfies r=s.

**Application check:** All prerequisites are established before each use. No upper Hessian bound or C1,1 regularity is assumed during convolution, no Cantor derivative is discarded when eliminating jumps, inversion is confined to A>0, and smooth-curve restriction is applied through every transition point.

**Sources:**

- User's accepted inputs
- /Users/mingchen/Non-Kahler/book/author/chapter_products.tex
- /Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex

**Finding:** matched and applicable under the accepted-input contract; no critical error or gap. No new external search required.

### R6. No new external-paper citation

**Location:** Whole proof and closing paragraph — external-reference inventory.

**Referenced statement/input:** The proof introduces no new theorem, lemma, definition, external-paper reference, or novelty claim. Its mention of strictly positive densities in the Hermitian Calabi-Yau theorem only delimits the claim's scope.

**Context and exact definitions:** All displayed cross-references point to accepted internal manuscript results. The new work is the positive-exponent extension of an already-read local flux proof. Historical external citations in the accepted sources are not new references of this submission.

**Application check:** No new external statement requires search_arxiv_theorems or web fallback. Had a new external-paper theorem been used, the mandated arXiv-first procedure would apply. The last paragraph makes no application of a strictly-positive-density theorem to the present degenerate f.

**Sources:**

- Submitted proof
- Four expressly accepted preceding sections and reports

**Finding:** matched and applicable under the accepted-input contract; no critical error or gap. No new external search required.

## Independent cross-checks

A separate read-only audit checked the exact exponential flux coefficient, convolution and signed-product extension, absence of regularity circularity, jump elimination and C1 inversion. Another checked every band contact/departure sign, one-constant identification, local C1,1 regularity and the every-point nonC2 transfer. Both found no errors or gaps. Their reasoning agrees with the primary ordered audit above.

## Failed checks and strict aggregation

All persisted statement and reference records were queried again before synthesis. There are 15 statement records, 73 deductions, six reference records, and zero failed mathematical checks. All critical-error and gap arrays are empty, so the strict verdict is **correct** and repair_hints is the empty string.

The initial positivity-to-BV passage, generalized coefficient, possible singular derivative and no-departure hypotheses were checked explicitly. No issue was suppressed on the basis of an accepted label or a plausible conclusion. No new external-paper citation occurs; inherited references within the accepted inputs were not reopened.

## Persistence

The authoritative records, including this full Markdown report, are persisted through the verification MCP in memory/numa_positive_exponent_regularity_01/. A readable copy is exported as verification_report.md in this run's results directory. The final machine-readable payload is validated and written through write_verification_output to [verification.json](verification.json). No book or prior results were edited.
