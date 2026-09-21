# Verification report: numa_selected_limit_01

## Verdict and scope

Correct under the expressly accepted inputs and the conditional exact existence/root assertion of prop:numa-radial-continuum. All 72 sequential deductions and five reference records pass. The weak flux argument justifies scalar semiconvexity, the fixed angular volume, convolution and bounded-product convergence, the jump mass formula, and continuity without discarding a possible Cantor derivative. Interior inversion and the contact-component argument then classify the slope. Exterior flux minima force positive horizontal coefficients; boundedness at the Fubini–Study end fixes the integration constant, and ordinary ODE uniqueness propagates the zero exterior slope. Canonical representatives and normalization give uniqueness among bounded K-invariant solutions. Accepted precompactness and identification of every cluster imply uniform convergence to the explicit C1,1 solution. No new outside PDE regularity theorem or all-solutions uniqueness is used. This verdict does not certify numa_radial_family_01; book inclusion still requires that audit to pass. Full report: results/numa_selected_limit_01/verification_report.md.

**Verdict:** `correct` under the stated prerequisites. **Critical errors:** 0. **Gaps:** 0. **Repair hints:** none.

The submitted proof was checked in textual order. The independent cross-checks of the flux lemma and of the subsequent uniqueness argument agreed with the primary audit. No book source or prior result was edited.

## Inputs and exact source context

- Accepted projective construction: [section_degenerate_nonuniqueness.tex](/Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex), including its full coefficients and geometry. The existing `degenerate_nonuniqueness_01` verdict is `correct`.
- Accepted cluster result: [section_symmetric_equation_selection.tex](/Users/mingchen/Non-Kahler/book/author/section_symmetric_equation_selection.tex). The existing `symmetric_equation_selection_01` verdict is `correct`.
- Conditional exact explicit existence and root: [section_numa_radial_family.tex](/Users/mingchen/Non-Kahler/book/author/section_numa_radial_family.tex), proposition `numa-radial-continuum`. Its independent audit is not presumed successful. The conditional input does not include exhaustiveness of the family.
- Accepted standard tools: one-dimensional convex/BV distribution calculus, bounded local Bedford–Taylor uniform continuity, canonical quasi-plurisubharmonic representatives, and local uniqueness of smooth ODEs.
- Fixed convention: $dd^c=\frac{i}{2\pi}\partial\bar\partial$, $R=dr\wedge d^cr$, and $(xP+yQ+zR)^3=6xyz\,P\wedge Q\wedge R$.

## Critical weak-measure and contact checks

The convolution argument uses a lower Hessian bound, not an upper Hessian bound. On a compact interval, $h_\varepsilon$ is bounded and $h_\varepsilon'\geq-(z*\eta_\varepsilon)$. Thus $dd^cG_\varepsilon(r)\geq-C\omega_{\mathrm{eucl}}$ locally. Adding one fixed smooth quadratic produces bounded psh potentials converging uniformly. Bedford–Taylor continuity of their powers, followed by expansion against the smooth form $\omega_0-dd^cB$, gives the required signed-product convergence even though $\omega_0$ is nonclosed.

Jump elimination leaves open a continuous singular derivative at the lemma's intermediate stage. The proof correctly concludes only that $h$ has a continuous representative. The $C^1$ flux and the inverse function theorem give smoothness where $A>0$. In the positive half-band, every component of $\{h+p>0\}$ after $t_*$ would satisfy $(h+p)'=p'-z_0<0$ starting from a continuous zero endpoint; hence none exists. This pointwise identification with $-p$ removes any Cantor-contact ambiguity. No global absolute continuity assumption is inserted.

At an exterior lower contact, the nonnegative $C^1$ flux $\Psi=\Phi(r,h)-\Phi(r,-x)$ would have derivative $+k$ at its interior minimum zero. At an upper contact, $\Phi(r,y)-\Phi(r,h)$ would have derivative $-k$. Since $k>0$ there, both are impossible. The exterior ODE is therefore smooth. Boundedness forces $a=\sigma+h\to1$ at the Fubini–Study end, fixing $F(a)-F(\sigma)=0$ for $F(s)=s^2/2-s^3/3$, so $h=0$. Local ODE uniqueness propagates this on the open interval $r>1$ without any assertion at the degenerate endpoint.

## Full sequential deduction record

### 1. Input contract and opening of section / theorem numa-selected-limit

**1.1 — Usable proof and audit scope.** The complete supplied section is usable mathematical proof text. The goal is uniqueness only among bounded K-invariant normalized omega-psh solutions for these fixed data, followed by convergence of the fixed positive-exponent approximation.

**1.2 — Accepted and conditional hypotheses.** Accepted: full projective construction, passed cluster proposition, one-dimensional convex/BV calculus, bounded local Bedford–Taylor uniform continuity, canonical qpsh representatives and smooth ODE uniqueness. Conditional: exact C1,1 radial existence and unique symmetric transition root, not classification of bounded solutions. No outside PDE regularity is assumed.

**1.3 — Actual source and conventions.** Read all of section_degenerate_nonuniqueness.tex, section_numa_radial_family.tex, and section_symmetric_equation_selection.tex in /Users/mingchen/Non-Kahler/book/author. The construction uses dd^c=i/(2pi) partial barpartial, R=dr wedge d^c r, dd^c G=G'(P-Q)+G''R, and cube coefficient 6xyz. Saved accepted audits both say correct.

**1.4 — Symmetries of data.** Block unitary transformations preserve r, the base pullbacks P,Q, R, and Fubini–Study. Exchange sends r to -r, swaps P,Q, fixes R, and x(-r)=y(r), z(-r)=z(r). Even rho preserves omega=omega0+dd^c rho. The common cube is zero on the symmetric closed band and omega0^3 outside, hence invariant under K.

**1.5 — Definition and normalization of u_*.** The expressly conditional radial construction supplies G_* with odd slope for I=-t_*, J=t_* and an even primitive. Then G_*(r)-rho is invariant under both block unitaries and exchange. Subtraction of the global supremum preserves its equation and all symmetries.

**1.6 — Definitions of A and Phi.** A(r,s)=(x+s)(y-s)=xy+(y-x)s-s^2; Phi(r,s)=xy s+(y-x)s^2/2-s^3/3. Thus partial_s Phi=A exactly, while partial_r keeps s fixed. x+y>0 at every finite r, including r=±1 where it equals 1.

**Finding:** checked; no critical error or gap.

### 2. Lemma numa-radial-flux, first paragraph: orbit reduction

**2.1 — Level sets are single block-unitary orbits.** After normalizing |A|^2+|B|^2=1, fixed r fixes both positive block lengths. U(2) is transitive on each sphere of that radius, so the two unitary factors map any pair with the same r to the other pair, modulo the common projective phase.

**2.2 — Existence of bounded scalar G.** Invariance of u and radial rho therefore gives u+rho=G(r) on U. Boundedness of u and global smooth rho makes G bounded; a local smooth section of the r submersion gives a measurable scalar representative.

**Finding:** checked; no critical error or gap.

### 3. Lemma numa-radial-flux, positivity and one-dimensional regularity

**3.1 — Weak chain rule before regularity.** r is a smooth submersion on U. Approximate its bounded scalar distribution G by smooth scalar convolutions; distributional continuity of dd^c gives dd^c G(r)=G'(r)(P-Q)+G''(r)R. This extension does not require the approximants to preserve omega0-positivity.

**3.2 — Radial testing isolates G''+z.** The independent complex coframe underlying P,Q,R has a smooth dual radial vector annihilated by P and Q, with R strictly positive on it. Testing the original positive current omega0+dd^cG against the corresponding nonnegative test forms yields G''+z>=0 as a scalar distribution. Positive coordinate weights can be absorbed into the tests; local tests in angular variables recover all nonnegative scalar tests.

**3.3 — Semiconvex representative.** Choose a smooth Z with Z''=z on an interval. Then (G+Z)''>=0 distributionally, so its finite convex representative is locally Lipschitz. Subtracting Z gives a continuous locally Lipschitz representative of G. The resulting continuous function composed with r and the original qpsh function agree almost everywhere; canonical qpsh representatives identify them pointwise.

**3.4 — BV derivative and radial inequality.** The derivative of a one-dimensional convex function is locally monotone and BV. Subtracting the smooth Z' gives h=G' in BV_loc, and the scalar distribution inequality is exactly dh+z dr>=0. The singular part of dh is therefore nonnegative.

**3.5 — Horizontal constraints.** Use dual complex horizontal directions annihilating R and the opposite base form. The corresponding current coefficients are x+h and y-h with respect to Lebesgue measure, proving -x<=h<=y almost everywhere; no contribution from the radial singular measure enters these contractions.

**3.6 — Both traces and upward jumps.** At each finite r, BV left/right limits exist. Limits along full-measure sets where the inequalities hold and continuity of x,y give -x(r)<=h(r±)<=y(r). Each jump is the atom of dh; dh+z dr>=0 implies h(r+)-h(r-)>=0.

**Finding:** checked; no critical error or gap.

### 4. Lemma numa-radial-flux, product identification and angular volume

**4.1 — Global product U=R x Y.** For F_t[A:B]=[e^{t/2}A:B], r(F_t q)=r(q)+t. The map (t,q)↦F_t q from R×Y to U has inverse q↦(r(q),F_{-r(q)}q); both are smooth. This fixes the scaling sign and factor.

**4.2 — Y is compact and smooth.** Y={|A|^2/(|A|^2+|B|^2)=1/2} is a closed subset of projective space disjoint from both excluded end loci. Since r is a submersion there, Y is a compact smooth five-dimensional orbit.

**4.3 — P,Q have no radial dependence or radial component.** Both forms are pullbacks from [A] and [B] in the two projective lines. The bases are unchanged by F_t, and both forms annihilate the real scaling direction. Thus their pullbacks to the product are fixed forms from Y.

**4.4 — d^c r is independent of r and has no dt component.** Each fixed F_t is holomorphic, so F_t^*d^c r=d^c(r+t)=d^c r. If V is its real infinitesimal generator, JV changes only relative phase, so dr(JV)=0 and d^c r(V)=0. Consequently the pulled-back one-form is fixed on Y.

**4.5 — Volume factor and normalization.** Set nu=(P wedge Q wedge d^c r)|Y. Then P wedge Q wedge R=dr wedge nu with no r-dependent factor. The source rank-one positivity makes nu a smooth positive nowhere-zero volume form in the orientation chosen. All d^c normalization constants remain in this nu; the cube coefficient is exactly 6.

**Finding:** checked; no critical error or gap.

### 5. Lemma numa-radial-flux, smooth wedge and weak convolution limit

**5.1 — Smooth coefficient identity.** For smooth G, omega0+dd^cG=(x+h)P+(y-h)Q+(z+h')R. The rank-one polynomial identity, valid even if some smooth coefficients have a negative sign, gives its cube as 6A(r,h)(z+h') dr wedge nu.

**5.2 — Flux primitive and partial-r convention.** The ordinary chain rule is d[Phi(r,h(r))]=[partial_r Phi(r,h)+A(r,h)h']dr. Rearranging yields A(z+h')dr=Az dr+dPhi-partial_r Phi dr, with the stated signs and no derivative of the angular volume.

**5.3 — Uniform scalar convergence and slope bounds.** On a compact interval strictly inside a slightly larger one, G is Lipschitz. A nonnegative standard convolution gives G_epsilon→G uniformly, h_epsilon=h*eta_epsilon uniformly bounded, and h_epsilon→h almost everywhere and in all finite L^q. Local boundedness of h suffices.

**5.4 — Lower radial Hessian bound survives convolution.** Convolving dh+z dr>=0 gives h_epsilon'>=-(z*eta_epsilon), which is uniformly bounded below on the compact interval. No upper bound on h_epsilon' is claimed or needed.

**5.5 — Common lower complex Hessian bound.** dd^cG_epsilon(r)=h_epsilon(P-Q)+h_epsilon'R. The bounded horizontal coefficients, smooth bounded P,Q,R on compact coordinate subsets, and semipositivity of R imply dd^cG_epsilon(r)>=-C omega_eucl. Thus a single smooth local quadratic B makes G_epsilon(r)+B and G(r)+B bounded psh.

**5.6 — Signed products with nonclosed background.** Use the accepted Bedford–Taylor continuity for all powers of dd^c(G_epsilon+B) under uniform convergence. Expand (omega0+dd^cG_epsilon)^3 as the finite sum of these powers wedged with smooth powers of omega0-dd^cB. Each term converges as a current. The smooth form need not be closed or positive. This identifies the limit with the bounded product of omega0+dd^cG and hence with MA_omega(u), since G=u+rho.

**5.7 — Scalar right-hand convergence without multiplying a singular derivative.** A(r,h_epsilon)z and partial_r Phi(r,h_epsilon) converge in L^1 by boundedness and almost-everywhere convergence of h_epsilon. Phi(r,h_epsilon)→Phi(r,h) in L^1, so its derivative converges distributionally. The proof never replaces A dh by an unjustified pointwise product at jumps.

**5.8 — Correct data coefficient and smooth joins.** The accepted construction has common cube zero on |r|<=1 and omega0^3=6xyz dr wedge nu for |r|>1. Equality of the product measures therefore gives the displayed flux identity with k as defined. Test against a fixed angular function of nonzero nu-integral to recover the scalar identity. Flat endpoint joins make k smooth, including at ±1.

**Finding:** checked; no critical error or gap.

### 6. Lemma numa-radial-flux, jumps, Cantor derivative, and regularity where A>0

**6.1 — The flux has no atomic right side.** At the initial BV stage h is locally bounded. Every term k-A(r,h)z+partial_r Phi(r,h) on the right is locally bounded measurable, so this side is absolutely continuous with respect to dr.

**6.2 — Exact jump mass.** Smooth composition with a locally BV function has one-sided traces Phi(r0,h(r0±)). The atom of dPhi is their difference, equal to the integral of A(r0,s) between h(r0-) and h(r0+). No assignment of an arbitrary value of h at the jump enters this formula.

**6.3 — Strict positive mass of any jump.** All jumps are upward and both traces lie in [-x(r0),y(r0)]. Since x+y>0, A=(x+s)(y-s) is positive strictly between these endpoints, and a nonzero interval between admissible traces has strictly positive integral, even if one trace is a boundary. This contradicts the absence of atoms on the right.

**6.4 — Continuity does not discard Cantor measure.** For a one-dimensional BV derivative, atoms are exactly the differences between left and right limits. Removing all jumps makes these limits equal at every point and yields a continuous representative. A continuous singular (Cantor) part of dh may still remain at this stage. dh consists of an absolutely continuous part and a nonnegative singular part; the proof does not infer absolute continuity here.

**6.5 — G is C1.** The locally Lipschitz G has weak derivative equal almost everywhere to the now continuous h. The fundamental theorem for absolutely continuous G identifies its derivative with h at every point, so G is C1.

**6.6 — C1 flux.** The representative W(r)=Phi(r,h(r)) is continuous, and its distributional derivative equals the now continuous right-hand function. Thus W is C1 with that derivative.

**6.7 — Inverse function argument.** At any point with A(r,h)>0, the smooth map (r,s)↦(r,Phi(r,s)) has nonzero Jacobian in s and a smooth local inverse. Applying it to the C1 graph (r,W(r)) gives h in C1 locally. Differentiating cancels the two partial_r Phi terms and yields A h'=k-Az.

**6.8 — Smoothness and singular derivative only on contact set.** The ODE h'=k/A-z has smooth coefficients on its open domain -x<h<y. Repeated differentiation gives h smooth on each such interval. In particular no Cantor derivative survives there. The lemma does not claim that its possible singular derivative on A=0 has already vanished; the theorem's contact analysis is still needed.

**Finding:** checked; no critical error or gap.

### 7. Theorem numa-selected-limit proof, parity and first contact inside the band

**7.1 — Parity and initial condition.** For an arbitrary bounded normalized K-invariant solution, exchange invariance and even rho make G(-r)=G(r). The proved C1 regularity makes h odd pointwise, hence h(0)=0.

**7.2 — Exact positive-band coefficients.** The source cutoff a is zero for r>=-1/3. Therefore on 0<r<1, x=p>0 and y=p+b>=p>0. Also p'=q<0, z=z0>0, and k=0; these statements use the actual source, not generic symmetric data.

**7.3 — Initial nondegenerate interval.** At r=0 both horizontal coefficients equal p(0)>0. Continuity gives an interval where A>0, on which the flux lemma implies the smooth equation h'=-z0 and the initial condition gives h(r)=-integral_0^r z0.

**7.4 — No upper first contact.** This explicit branch is strictly negative for r>0 and strictly decreasing, while y(r)>0 for 0<r<1. It cannot meet the upper boundary before lower contact.

**7.5 — First lower contact exactly at t_*.** The lower difference on the initial branch is h+p=p(r)-integral_0^r z0=-L(r). The conditional root assertion says L has its unique zero t_* in (0,1); the actual coefficients give L'=z0-p'>0, L(0)<0. Thus h+p stays positive before t_*, vanishes at t_*, and would become negative after it. Continuity and local regularity prevent the initial A>0 interval from ending earlier or extending past this contact.

**Finding:** checked; no critical error or gap.

### 8. Theorem numa-selected-limit proof, complementarity after lower contact

**8.1 — All possible departures are open components.** The global constraint h>=-p on (0,1) and continuity make E={r in (t_*,1):h(r)+p(r)>0} open. Any connected component (a,b) has a finite left endpoint a in [t_*,1) with h(a)+p(a)=0; at a=t_* this follows from first contact.

**8.2 — Strict negativity at the left endpoint.** p(a)>0 because t_*<=a<1, so h(a)=-p(a)<0. Continuity makes h<0 immediately to the right of a.

**8.3 — Interior equation throughout a candidate component.** On the component the lower coefficient h+p is positive. As long as h<0, the upper coefficient y-h is also positive, so the lemma gives h'=-z0<0. Integrating from the continuous left endpoint shows h remains at most h(a)<0. A first point with h=0 is therefore impossible. Thus A>0 and the smooth ODE hold throughout the component.

**8.4 — Contradiction at departure.** On (a,b), (h+p)'=p'-z0<0. For a<r<b integrate this continuous bounded right side from a+delta to r and let delta down to zero. Since h(a)+p(a)=0, one obtains h(r)+p(r)=integral_a^r(p'-z0)<0, contradicting the definition of the component. No derivative at a is assumed.

**8.5 — Cantor/contact configurations excluded.** Every positive departure would contain one of the components just ruled out. Therefore E is empty and h=-p at every point of [t_*,1], including r=1 by continuity and p(1)=0. This pointwise identification with a smooth branch precludes a hidden Cantor variation on that segment; the argument never replaces continuity by absolute continuity without proof.

**8.6 — Negative half and exact symmetric slope.** Oddness gives h=p on [-1,-t_*] and the even-z0 integral gives h=-integral_0^r z0 on [-t_*,t_*]. For I=-t_* the conditional formula p(I)-integral_I^r z0 equals this central expression because p(t_*)=integral_0^{t_*}z0. Hence the slope matches the supplied symmetric construction on the entire closed band.

**Finding:** checked; no critical error or gap.

### 9. Theorem numa-selected-limit proof, exterior horizontal positivity

**9.1 — Strict exterior data positivity.** For each finite r>1, the actual source has x,y,z>0 and k=xyz>0. At r=1 they may vanish; the argument only uses the open interval (1,infinity).

**9.2 — Lower flux is nonnegative and C1.** For -x<=h<=y, the integrand A(r,s) is nonnegative throughout [-x,h]. Hence Psi=integral_{-x}^h A>=0. The identity Psi=Phi(r,h)-Phi(r,-x) writes Psi as a C1 function minus a smooth one, independently of differentiability of h at a contact.

**9.3 — Lower endpoint derivative is +k.** Differentiate using the flux identity and the smooth moving lower endpoint: Psi'=k-A(r,h)z+Phi_r(r,h)-Phi_r(r,-x), because A(r,-x)=0 makes the endpoint velocity term vanish. If h(r0)=-x(r0), the A term vanishes and the Phi_r terms cancel, so Psi'(r0)=k(r0)>0.

**9.4 — Lower contact contradiction.** A contact has Psi(r0)=0 and is an interior minimum of the nonnegative C1 function Psi, requiring Psi'(r0)=0. The computed derivative rules out every such contact.

**9.5 — Upper flux and sign.** Xi=integral_h^y A=Phi(r,y)-Phi(r,h)>=0 is C1. Its derivative is Xi'=Phi_r(r,y)-k+A(r,h)z-Phi_r(r,h), since A(r,y)=0. At h(r0)=y(r0), Xi'= -k(r0)<0, again contradicting the derivative zero at an interior minimum.

**9.6 — Exterior smooth ODE.** Both contacts being impossible and the closed bounds already known, -x<h<y and A>0 throughout r>1. Thus h is smooth and solves the lemma's ODE everywhere on this connected interval.

**Finding:** checked; no critical error or gap.

### 10. Theorem numa-selected-limit proof, Fubini–Study end and ODE propagation

**10.1 — Exact end coefficients and variable.** For r>=2 the source has x=sigma, y=1-sigma, z=sigma', sigma=e^r/(1+e^r). Write a=sigma+h; the horizontal bounds give 0<a<1 and A=a(1-a). This new a is distinct from the source cutoff, already zero here.

**10.2 — End ODE.** The lemma gives A(h'+sigma')=k=sigma(1-sigma)sigma'. Since a'=sigma'+h', a(1-a)a'=sigma(1-sigma)sigma'>0, with no missing sigma factor.

**10.3 — Limit of a.** The positive right side and a(1-a)>0 imply a is strictly increasing. Its upper bound one gives a limit L<=1; a(2)>0 implies L>0.

**10.4 — Boundedness forces L=1.** If L<1, sigma→1 gives h=a-sigma→L-1<0. Then G'=h<=-epsilon eventually for some epsilon>0, so G tends to -infinity. This contradicts bounded u and smooth bounded rho on compact X. Thus L=1; no end derivative condition was assumed.

**10.5 — Integration constant.** For F(s)=s^2/2-s^3/3, F'(s)=s(1-s). The ODE says d[F(a)-F(sigma)]/dr=0. The common limit a,sigma→1 gives C=F(1)-F(1)=0.

**10.6 — Unique inversion.** F'(s)>0 on (0,1), so F(a)=F(sigma) implies a=sigma, hence h=0 on r>=2.

**10.7 — Zero is a solution on the exterior.** H(r,s)=xyz/[(x+s)(y-s)]-z is smooth for r>1 and -x<s<y. Since x,y>0 and H(r,0)=0, the identically zero function is an admissible solution on all (1,infinity).

**10.8 — ODE propagation.** Both h and zero solve that ODE and agree on r>=2. Their equality set is relatively closed by continuity and open by local uniqueness at every point (r,0), where the coefficients are nondegenerate. Connectedness gives h=0 throughout (1,infinity), without invoking uniqueness or uniform ellipticity at r=1.

**10.9 — Negative end.** Oddness gives h=0 for r<-1. Continuity and the band formula also give h(±1)=0.

**Finding:** checked; no critical error or gap.

### 11. Theorem numa-selected-limit proof, global normalized uniqueness

**11.1 — Equality with the exact conditional slope.** The proven h is zero outside [-1,1], equals p on [-1,-t_*], equals -integral_0^r z0 on [-t_*,t_*], and equals -p on [t_*,1]. These are exactly the supplied formula for h_{-t_*,t_*}, including the joins. No other family member or classification theorem was assumed.

**11.2 — One additive constant on U.** Both scalar primitives are C1 on the connected real line and have the same derivative everywhere. Their difference is one constant, so u=u_*+C on U after subtracting the same rho.

**11.3 — Equality across the projective ends.** X\U is the union of the two projective lines {A=0} and {B=0}, a measure-zero analytic subset. Thus the two qpsh functions agree almost everywhere on X up to C. Equality of their canonical local qpsh representatives gives equality everywhere, without assuming an extra boundary regularity theorem.

**11.4 — Normalization.** sup_Xu=sup_Xu_*=0 forces C=0. The arbitrary bounded normalized K-invariant solution therefore equals the conditionally supplied u_*.

**Finding:** checked; no critical error or gap.

### 12. Theorem numa-selected-limit proof, convergence and final scope

**12.1 — Cluster proposition hypotheses.** The fixed omega is smooth Hermitian, dV=omega_X^3 is smooth positive, and f is smooth nonnegative nonzero, hence in L^p for every finite p>1. The accepted symmetric-equation-clusters proposition therefore supplies normalized C0 precompactness and bounded zero-equation cluster solutions.

**12.2 — Scalar is exactly one.** The accepted projective construction already supplies bounded solutions to MA_omega(u)=f omega_X^3. In the accepted proposition's unique-scalar convention this gives c=1, so every cluster solves exactly the equation classified here.

**12.3 — Full group invariance of clusters.** Every element of K is a biholomorphism preserving omega and f omega_X^3. The accepted proposition applies to this entire group: uniqueness at positive exponent gives invariance, preserved under normalization and uniform limits. The argument does not infer K invariance merely from exchange invariance.

**12.4 — Identification of all clusters.** Uniform limits remain normalized. Every cluster is consequently within the bounded normalized K-invariant class just classified and equals u_*.

**12.5 — Precompactness implies convergence of the entire family.** If uniform convergence as lambda→0 failed, some epsilon>0 and a sequence lambda_j→0 would have uniform distance at least epsilon from u_*. Precompactness gives a uniformly convergent subsequence, whose limit must be u_*, contradicting that distance. This is valid for the parameter family, not just one chosen sequence.

**12.6 — C1,1 conclusion and limits of the claim.** The selected limit is C1,1 because it is identified with the expressly conditional explicit C1,1 solution. No claim of convergence in C1,1, uniqueness of all zero-equation solutions, general selection, or novelty certification is used or obtained.

**12.7 — Assumption-use audit.** Fixed coefficients give the signs, flat joins, volume frame and exact FS tail. Block invariance gives radial reduction; exchange gives the zero initial slope and the negative-side identification. Boundedness gives finite convex representatives, local bounded products and the decisive end condition. Positivity gives semiconvexity and slope bounds; smooth density eliminates jump atoms and exterior contacts. Conditional existence/root supplies the comparison solution and t_*. Accepted cluster compactness supplies convergence. No suspiciously unused hypothesis or unsupported exhaustiveness premise remains.

**Finding:** checked; no critical error or gap.

## Full reference and prerequisite record

### Reference 1: sec:degenerate-hermitian-nonuniqueness

**Location:** Opening; notation before Lemma numa-radial-flux; exterior-end calculation.

**Referenced statement/input:** On X=P(C^2⊕C^2), U={A≠0,B≠0}, r=log(|A|²/|B|²), P=dd^c log|A|², Q=dd^c log|B|², R=dr∧d^cr. P²=Q²=R²=0, PQR>0; dd^cG=G'(P−Q)+G''R. omega0=xP+yQ+zR; omega=omega0+dd^c rho. On the band x=p+a,y=p+b,z=z0, p'=q; the common data cube is zero. Outside the band the data cube is omega0³. For |r|≥2, (x,y,z)=(sigma,1−sigma,sigma').

**Context and definitions:** All forms are in the supplied dd^c=i/(2pi)∂∂̄ convention; the source's historical 4pi conversion has already been incorporated. The geometric rank-one statements and coefficient identities are exactly those used. The current audit checks their specializations to x=p on r>0, p'<0, z0>0, exterior positivity and exact FS tails.

**Application check:** Matched and applicable. Read the full source and its passed degenerate_nonuniqueness_01 verdict; no reopening of inherited external-paper references is needed under the accepted-input contract.

**External search required:** no. **Critical errors/gaps:** none.

### Reference 2: prop:numa-radial-continuum

**Location:** Definition of u_*; first-contact root; final slope identification and C1,1 conclusion.

**Referenced statement/input:** For −1<I<0<J<1 satisfying integral_I^J z0=p(I)+p(J), the slope is p on [−1,I], p(I)−integral_I^r z0 on [I,J], −p on [J,1], and zero outside. A primitive minus rho, normalized by its supremum, is a C1,1 solution. L(t)=integral_0^t z0−p(t) has a unique zero t_* in (0,1). I=−t_*,J=t_* yields the odd middle slope −integral_0^r z0 and an even solution when rho is even.

**Context and definitions:** The user expressly authorizes only this exact existence and root assertion as a conditional prerequisite. The source uses the same background, density, rho, p,z0 and normalization. The full continuum classification or exhaustiveness of these solutions is not an input.

**Application check:** Matched. Every use is legitimate: supplies existence and regularity of u_*, locates first contact, and permits equality of the eventual classified slope with the explicit one. The proof itself classifies all bounded K-invariant solutions through the flux analysis. This verdict remains conditional and does not declare numa_radial_family_01 passed.

**External search required:** no. **Critical errors/gaps:** none.

### Reference 3: prop:symmetric-equation-clusters

**Location:** Final paragraph of theorem proof.

**Referenced statement/input:** Let omega be Hermitian, dV smooth positive, 0≤f∈L^p(dV), p>1, nonzero, and c>0 the unique scalar for the bounded equation MA_omega(u)=cf dV. The normalized solutions a_lambda=u_lambda−sup_X u_lambda of MA_omega(u_lambda)=e^(lambda u_lambda)f dV, 0<lambda≤1, are relatively compact in C(X). Every cluster limit as lambda↓0 is a normalized bounded solution with scalar c. If a group of biholomorphisms preserves omega and f dV, each a_lambda and each cluster is invariant under that group.

**Context and definitions:** Here dV=omega_X³, the fixed f is smooth nonnegative nonzero, omega is the constructed Hermitian form, and existing accepted solutions have scalar one. K consists of holomorphic projective block unitaries and block exchange preserving both required objects.

**Application check:** Matched and applicable; source and passed symmetric_equation_selection_01 audit read. The input gives only cluster compactness and equations. Full-family convergence follows from the new invariant uniqueness plus the explicit subsequence contradiction, which was independently checked.

**External search required:** no. **Critical errors/gaps:** none.

### Reference 4: One-dimensional convex/BV calculus; bounded local Bedford–Taylor uniform continuity; canonical qpsh representatives; smooth ODE uniqueness

**Location:** Radial lemma and global proof.

**Referenced statement/input:** The user expressly permits standard one-dimensional convex/BV distribution calculus, bounded local Bedford–Taylor continuity under uniform convergence, canonical quasi-plurisubharmonic representatives, and local uniqueness for smooth ordinary differential equations.

**Context and definitions:** Convexity is used after adding a double primitive of z; BV traces and smooth composition give the flux atom. Uniform BT continuity is applied only after one fixed smooth local correction produces uniformly convergent bounded psh potentials; smooth finite expansions handle the nonclosed background. Canonical representatives identify functions already equal almost everywhere. ODE uniqueness is used solely where A>0, on finite exterior points.

**Application check:** All applications remain within the accepted standard facts. Continuity of h is not confused with absolute continuity, and no new outside PDE regularity theorem is invoked.

**External search required:** no. **Critical errors/gaps:** none.

### Reference 5: inventory

**Location:** Whole submitted proof: external-reference inventory.

**Referenced statement/input:** No new theorem, lemma or definition from an external paper is cited in the submitted selected-limit proof.

**Context and definitions:** The displayed cross-references point to the three provided internal manuscript sources. Bedford–Taylor and one-dimensional calculus are expressly accepted inputs. External citations appearing inside accepted source files are inherited prerequisites, not new references introduced by this proof.

**Application check:** There is no introduced external-paper reference to query. Accordingly neither search_arxiv_theorems nor web search was needed; if a new external reference had arisen, the mandated arXiv-first, web-fallback order would apply.

**External search required:** no. **Critical errors/gaps:** none.

## Aggregation and strict verdict

12 statement records contain 72 individual deductions. All 5 reference records were checked in their exact contexts. Every critical-error and gap array is empty. The failed-check inventory contains zero mathematical failures. Under the required rule, the verdict is `correct` and `repair_hints` is the empty string.

This is an audit of the supplied proof for the fixed symmetric data. It proves uniqueness only in the bounded normalized $K$-invariant class and convergence only for the stated normalized positive-exponent family. The $C^{1,1}$ conclusion is for the selected limit, inherited from the conditional explicit construction.

