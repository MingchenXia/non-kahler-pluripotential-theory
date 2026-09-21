# Verification report: numa_radial_family_01

## Verdict

**Correct**, conditional on the expressly accepted prerequisite `degenerate_nonuniqueness_01`.

- Critical errors: 0.
- Gaps: 0.
- Sequential audit: 75 individual deductions in 15 ordered records.
- Reference audit: 3 records.
- Repair hints: none required.

## Scope

The complete [accepted prerequisite](/Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex) was read to recover the exact coefficients, supports, normalization, background and source. Its validity was accepted as instructed. Every use in the new proof was checked. The book and earlier verification results were not edited.

The proof establishes an uncountable family of normalized global C1,1 solutions of the same smooth degenerate Hermitian Monge–Ampère equation and a directly constructed invariant solution when the cutoff for rho is even. No positive-exponent selection or convergence result is claimed.

## Sequential deduction audit

### 1. Input assumptions and accepted prerequisite

1. The supplied proof is usable mathematical text. Its target is an uncountable set of normalized global C1,1 solutions for one fixed smooth positive Hermitian background and one fixed smooth density, with an explicitly constructed block-exchange invariant member when the cutoff for rho is even.

2. The entire named prerequisite has been read and is accepted rather than reverified. X=P(C^2 directsum C^2), U={A!=0,B!=0}, r=log(|A|^2/|B|^2), and all forms use ddc=i/(2pi) partial barpartial.

3. On U, P,Q,R are independent smooth semipositive rank-one forms, ddc G(r)=G'(P-Q)+G''R, and (xP+yQ+zR)^3=6xyz P wedge Q wedge R. The displayed local expression for partial r has nonzero -d tau/tau component, so every finite r-level is a smooth real hypersurface.

4. From the precise construction: p=beta/2 is smooth, even, supported on [-1,1], positive in the interior and flat at its endpoints; q=p' is positive on (-1,0), negative on (0,1). The cutoff a is nonnegative, equals 1 for r<=-2/3 and 0 for r>=-1/3; b(r)=a(-r) and thus b=0 for r<=1/3. The even chi has compact support in (-1/3,1/3) and chi(0)>0.

5. z0=sqrt(q^2+chi^2) is smooth and even, positive in the interior, flat at the endpoints, >=|q|, and >|q| near zero. On the band x=p+a,y=p+b,z=z0; globally x(-r)=y(r),z(-r)=z(r), and omega0 is smooth semipositive, equal to omega_X near X minus U.

6. omega=omega0+ddc rho is already known smooth and strictly positive. rho=epsilon(r^2-1)kappa(r), with kappa compactly supported in (-2,2) and equal to 1 on [-3/2,3/2]; an even kappa is allowed. The fixed source f omega_X^3 is zero on the closed band and equals omega0^3 outside it. Original radial slopes are -p and +p. Permitted analytic inputs are real Lipschitz/Sobolev calculus and bounded local Bedford--Taylor uniform continuity.

**Finding:** checked; no critical error or gap.

### 2. Opening paragraph and eq:numa-half-excess

1. The retained identities x=p+a, y=p+b, z=z0 and p'=q match the prerequisite exactly, without a normalization factor or sign change.

2. Because p(1)=0 and p'<0 on (0,1), the fundamental theorem of calculus gives integral_0^1 |p'| = -integral_0^1 p' = p(0).

3. The continuous nonnegative difference z0-|p'| is strictly positive on a nonempty interval to the right of zero, since chi(0)>0 and chi is continuous. Its integral is strictly positive. Therefore integral_0^1 z0 > p(0), as claimed.

**Finding:** checked; no critical error or gap.

### 3. prop:numa-radial-continuum: balance equation and interval of roots

1. K(I,J)=integral_I^J z0-p(I)-p(J) is continuous jointly on the relevant compact ranges, with the auxiliary boundary value I=0 legitimate even though final parameters must be negative.

2. K(0,0)=-2p(0)<0. K(0,1)=integral_0^1 z0-p(0)-p(1)>0 by the preceding excess and p(1)=0.

3. Continuity of I -> K(I,0) and I -> K(I,1), together with their strict signs at zero, yields one epsilon>0 for which both signs persist for all I in [-epsilon,0]. Shrinking epsilon below 1 ensures -1<I<0 for final parameters.

4. For J in (0,1), partial_J K=z0(J)-p'(J)>0 because p'(J)<0 and z0(J)>=|p'(J)|. Thus K(I,.) is strictly increasing on [0,1].

5. For each I in [-epsilon,0), the intermediate value theorem supplies a root J(I) in (0,1); strict increase proves uniqueness. No continuity or differentiability of I -> J(I) is required for the later injection argument.

6. The proposition first constructs an interval of admissible pairs. Its subsequent verification is stated for every pair -1<I<0<J<1 satisfying balance, so the later symmetric pair need not belong to this particular small parameter interval.

**Finding:** checked; no critical error or gap.

### 4. prop:numa-radial-continuum: definition of h and primitive G

1. At I the middle expression equals p(I), matching the left branch. At J, balance yields p(I)-integral_I^J z0=-p(J), matching the right branch.

2. On the three pieces the derivatives are p', -z0, and -p', all bounded. At +/-1 the function matches zero because p is flat there. A continuous function with these finitely many bounded-derivative pieces is globally Lipschitz, including both transition points and the extension by zero.

3. Since I>-1 and J<1, h coincides with the flat smooth functions p and -p in neighborhoods inside the two band endpoints and with zero outside. Therefore it is smooth and vanishes to all orders at +/-1. No smoothness of h at I or J is asserted.

4. A primitive G can be defined by integrating the continuous globally Lipschitz h. It is C1 with G'=h globally Lipschitz, hence C1,1; it is constant separately on each of the two tails r<=-1 and r>=1. The tail constants are not required to agree.

**Finding:** checked; no critical error or gap.

### 5. prop:numa-radial-continuum: global extension to X

1. On every relatively compact coordinate chart in U the smooth function r has bounded first and second derivatives. Since G'=h is Lipschitz, d(G(r))=h(r)dr is locally Lipschitz; thus composition gives C1,1 regularity, including across r=I and r=J.

2. The band {|r|<=1} is a compact subset of U: the continuous ratio |A|^2/(|A|^2+|B|^2) stays in [1/(1+e),e/(1+e)]. Consequently finitely many such coordinate estimates cover the entire region where G is nonconstant.

3. Near the line {A=0}, r<-1 and G(r) equals its left tail constant. Near the disjoint line {B=0}, r>1 and G(r) equals its right tail constant. These locally constant extensions are smooth; distinct constants on disjoint end neighborhoods present no compatibility problem.

4. The finite chart cover of the compact band and the smooth end neighborhoods give a global C1,1 function on compact X. Flat matching at +/-1 yields smoothness there as well. The potentially unbounded derivatives of r near X minus U are irrelevant because G(r) is exactly constant there.

**Finding:** checked; no critical error or gap.

### 6. prop:numa-radial-continuum: middle-interval slope bounds

1. On (I,J), h'=-z0. Thus (h-p)'=-z0-p'<=0 because z0>=|p'|, for either sign of p'.

2. At I, h(I)-p(I)=0. Integrating the preceding nonpositive derivative forward gives h-p<=0 throughout [I,J].

3. Likewise (h+p)'=-z0+p'<=0. Balance gives h(J)+p(J)=0. A nonincreasing function ending at zero is nonnegative at every earlier point, so h+p>=0 on [I,J].

4. Together these give -p<=h<=p with the stated directions of both inequalities; the second estimate is obtained using its terminal value, not its initial value.

**Finding:** checked; no critical error or gap.

### 7. prop:numa-radial-continuum: eq:numa-slope-form

1. Subtracting the already fixed smooth rho preserves global C1,1 regularity of u_tilde=G(r)-rho.

2. Linearity of distributional ddc and omega=omega0+ddc rho yield omega+ddc u_tilde=omega0+ddc G(r) exactly. No parameter-dependent change to omega, rho, f, or omega_X is made.

3. Away from I,J, G is smooth and the accepted chain formula gives ddc G(r)=h(P-Q)+h'R; adding omega0 gives coefficients x+h, y-h, z+h'. All factors and signs agree with the fixed ddc convention.

4. The nonsmooth r-levels have volume zero, because dr has the nonzero tau component given by the accepted coordinate formula. Hence this piecewise formula is an almost-everywhere identity on U. Its validity as a distributional identity is checked below, rather than assumed from pointwise calculations.

**Finding:** checked; no critical error or gap.

### 8. prop:numa-radial-continuum: coefficient positivity and vanishing directions

1. On I<r<J, the three coefficients are p+a+h, p+b-h, 0. Nonnegativity of a,b and the bounds -p<=h<=p prove both first coefficients nonnegative; the third vanishes because h'=-z0.

2. On -1<r<I<0, the exact support b=0 on r<=1/3 applies. The coefficients are 2p+a, b=0, z0+p'. The first is nonnegative, and the third is nonnegative since z0>=|p'|.

3. On 0<J<r<1, the exact support a=0 on r>=-1/3 applies. The coefficients are a=0, 2p+b, z0-p'. The latter two are nonnegative.

4. Outside the band h=h'=0, so the form is omega0, which is already smooth semipositive globally and smooth positive outside the closed band. Near X minus U the same equality follows from the constant extension of G.

5. Since P,Q,R are semipositive, the coefficient inequalities imply an almost-everywhere positive semidefinite form. On each open subband at least one coefficient is zero. No positivity conclusion requires the first two middle coefficients to be strictly positive.

**Finding:** checked; no critical error or gap.

### 9. prop:numa-radial-continuum: distributional Hessian and absence of surface terms

1. The established global C1,1 regularity implies membership in W2,infinity in smooth local coordinates; its distributional second derivatives are represented by its bounded almost-everywhere second derivatives.

2. In local real coordinates on U, D2(G(r))=h'(r) dr tensor dr + h(r) D2r almost everywhere. This follows from the permitted Lipschitz/Sobolev chain rule and gives the displayed complex Hessian with the accepted normalization.

3. Across r=I and r=J, the first derivative d(G(r))=h(r)dr has matching traces, because h is continuous there. In piecewise integration by parts the jump in this first derivative, which would be the coefficient of a hypersurface measure in D2(G(r)), is zero. A jump in h' is merely a jump between bounded Hessian densities.

4. Across r=+/-1 all derivatives match smoothly by endpoint flatness. Near the deleted projective lines the extension is constant, so there is no extra distribution supported there either.

5. Subtracting smooth rho adds no singular term. Testing the almost-everywhere positive semidefinite L-infinity form against nonnegative test forms proves positivity as a current; consequently the continuous u_tilde is omega-plurisubharmonic and locally quasi-plurisubharmonic.

**Finding:** checked; no critical error or gap.

### 10. prop:numa-radial-continuum: Bedford--Taylor/a.e. Hessian-product identification

1. Fix a coordinate ball and then a smaller relatively compact ball. For the locally C1,1 quasi-plurisubharmonic potential u_tilde, choose a fixed real smooth quadratic psi=C|z|^2 with sufficiently large C so that v=u_tilde+psi is plurisubharmonic on the larger ball. This uses the local bounded lower Hessian bound (also supplied by ddc u_tilde>=-omega and smoothness of omega). v remains C1,1.

2. Convolving v by a nonnegative smooth approximate identity on the smaller ball gives smooth plurisubharmonic v_delta. The weak Hessian of v is locally L-infinity and D2 v_delta is its convolution, hence uniformly bounded on each still smaller ball.

3. Approximate-identity convergence gives D2 v_delta -> D2 v strongly in L^s locally for every 1<=s<infinity. Uniform convergence v_delta -> v follows from continuity, indeed C1,1 regularity, on compact subsets. No assertion of L-infinity convergence of Hessians is needed.

4. Each coefficient of a wedge power of degree k<=3 is a finite sum of products of k complex Hessian entries. Telescoping a difference of products and bounding the other k-1 entries uniformly shows its L1 norm tends to zero. Therefore every (ddc v_delta)^k converges coefficientwise in L1 to the algebraic a.e. wedge (ddc v)^k.

5. The permitted bounded local Bedford--Taylor uniform continuity applies to these locally bounded psh v_delta converging uniformly to v, for each degree k<=3. It identifies the same weak-current limit with the Bedford--Taylor power of v. Uniqueness of limits therefore proves the a.e. Hessian-product identification, not just convergence of formal smooth products.

6. Set S=omega-ddc psi, a smooth (1,1)-form which need not be closed. The local background product is sum_{k=0}^3 binomial(3,k) S^{3-k} wedge (ddc v)^k. Multiplication of a current by a smooth form is defined without closedness, and the same polynomial expansion holds for a.e. matrices. Applying the preceding identification to every k gives the claimed product for the original nonclosed background.

7. The resulting top-degree measure has locally bounded density and is absolutely continuous with respect to coordinate volume. Consequently no nonlinear concentration or additional measure on r=I,J,+/-1 can remain. The argument uses only the explicitly permitted analytic inputs and no new PDE theorem.

**Finding:** checked; no critical error or gap.

### 11. prop:numa-radial-continuum: equation and normalization

1. On each of the three open subbands the coefficient calculation supplies a zero factor in 6(x+h)(y-h)(z+h') P wedge Q wedge R. The rank-one formula therefore gives zero cube almost everywhere in the full band.

2. Outside the band the solution form equals omega0, so its cube equals omega0^3. On neighborhoods of X minus U this follows from the smooth extension; there is no missing region in the equality.

3. The transition hypersurfaces and band endpoints have coordinate volume zero, and the product just shown is absolutely continuous. Thus the almost-everywhere cube equality gives equality of measures globally, including across all interfaces.

4. The prescribed source is exactly zero on the closed band and exactly omega0^3 outside by the accepted prerequisite. Consequently MA_omega(u_tilde)=f omega_X^3 with precisely the same f and omega and no multiplicative constant or change in normalization.

5. Compactness of X and continuity of u_tilde give a finite supremum. Subtracting it produces sup_X u=0, preserves C1,1 regularity and positivity, and leaves ddc u and its Monge--Ampere measure unchanged.

**Finding:** checked; no critical error or gap.

### 12. prop:numa-radial-continuum: parameter distinctness and uncountability

1. For I1<I2<0 and I1<r<I2, the slope with switch I2 is still on its left branch p(r). The slope with switch I1 is on its middle branch, since r<0<J(I1).

2. Using the middle formula and the fundamental theorem of calculus gives p(r)-h_{I1,J(I1)}(r)=p(r)-p(I1)+integral_{I1}^r z0=integral_{I1}^r (p'+z0).

3. On the entire nonempty integration interval p'>0 and z0>=|p'|, so the integrand is strictly positive and the integral is strictly positive. The slopes therefore differ on an open interval.

4. Two primitives differing by a constant have identical slopes. Thus these primitives cannot differ by a constant. The radial coordinate attains every real value on U (for example [A:B]=[(1,0):t(1,0)] with |t| varying), so the same nonconstancy holds on X.

5. Subtracting the same rho and then possibly different supremum constants cannot make these functions equal. The assignment I -> u_{I,J(I)} is injective on the nondegenerate interval [-epsilon,0), which is uncountable.

6. The original solutions have radial primitives +/-F/2 and slopes +/-p. Each constructed slope equals +p on the nonempty interval (-1,I), where p>0, so it differs from -p. It equals -p on the nonempty interval (J,1), so it differs from +p. The same constant-normalization argument proves distinction from both original smooth solutions.

**Finding:** checked; no critical error or gap.

### 13. prop:numa-radial-continuum: symmetric root and admissible pair

1. L(t)=integral_0^t z0-p(t) is continuous on [0,1]. L(0)=-p(0)<0 and L(1)=integral_0^1 z0>0, since p(1)=0 and z0 is positive in the interior.

2. For 0<t<1, L'(t)=z0(t)-p'(t)>0. The intermediate value theorem and strict monotonicity produce a unique t_* in (0,1), so I=-t_* and J=t_* satisfy all strict endpoint requirements.

3. L(t_*)=0 means integral_0^{t_*} z0=p(t_*). Evenness gives integral_{-t_*}^{t_*} z0=2p(t_*)=p(-t_*)+p(t_*), which is exactly the required balance equation.

4. The preceding slope, regularity, positivity, and equation arguments apply to every admissible pair, so they apply to this symmetric pair even if -t_* lies outside the small interval originally used to exhibit uncountability. The full constructed family includes this pair.

**Finding:** checked; no critical error or gap.

### 14. prop:numa-radial-continuum: odd slope, even primitive, and involution invariance

1. For -t_*<=r<=t_*, the middle formula and the zero equation give h(r)=p(t_*)-[integral_{-t_*}^0 z0+integral_0^r z0]=-integral_0^r z0. The integral of the even z0 from zero is odd, hence h is odd on the middle interval.

2. For t_*<=r<=1, h(r)=-p(r) and h(-r)=p(-r)=p(r), and the zero extensions beyond +/-1 also agree with oddness. Thus h is globally odd.

3. The primitive G(r)=integral_0^r h(s) ds is even. Its smooth end extensions therefore have equal tail constants in the symmetric case, and preserve the symmetry.

4. The block exchange iota sends r to -r, interchanges P and Q, and fixes R because both dr and d^c r change sign. The prerequisite has x(-r)=y(r) and z(-r)=z(r) globally, so omega0 is invariant.

5. Choosing the permitted kappa even makes rho=epsilon(r^2-1)kappa(r) even. This is one fixed allowed choice in the accepted construction; all solutions are then built using this same rho and the same resulting positive omega. Pullback commutes with ddc, so omega is invariant as well.

6. G(r)-rho(r) is fixed by iota on U, and continuity of the global extension gives invariance on all X. Subtracting a scalar supremum preserves invariance.

7. The data are consistent with this symmetry: the band is invariant, omega0^3 is invariant, and omega_X is invariant under the unitary block exchange. Thus both the exact density f and background omega are invariant in the even-cutoff case. The proof does not obtain this solution by averaging other solutions.

**Finding:** checked; no critical error or gap.

### 15. Closing paragraph and full hypothesis-use audit

1. The injective construction yields uncountably many normalized C1,1 solutions of the one fixed equation, and the direct symmetric construction gives the stated invariant solution. This proves the proposition under the explicit prerequisite.

2. Every transition occurs at -1<I<0<J<1, hence both transition hypersurfaces lie strictly inside the zero-density band. The proof claims C1,1 regularity and makes no unjustified assertion of smoothness at the transitions.

3. Endpoint flatness is used for smooth gluing; the strict excess near zero for roots; signs of p' for strict monotonicity and distinctness; z0>=|p'| for all coefficient estimates; a,b support conditions for vanishing outer coefficients; positivity of omega for the solution class; and the exact prescribed density for the global measure equality.

4. Evenness of p,z0 is used for the symmetric pair and odd slope; even rho is required only for the invariant-solution clause. The frame independence and explicit submersion coordinate justify the cube and measure-zero transitions. The additional detailed shape of cutoffs and the prior construction's bounded-mass discussion are not needed after these accepted properties and supply no hidden missing argument.

5. The new proof is a derived consequence of the supplied construction. It attributes no new family theorem to NUMA, makes no novelty claim, imports no new PDE result, and asserts no convergence or selection of positive-exponent approximations. Its final separation of the approximation question is logically accurate.

**Finding:** checked; no critical error or gap.

## Reference audit

### 1. Internal references to thm:degenerate-hermitian-nonuniqueness and eq:numa-rank-frame

**Classification:** accepted local prerequisite.

**Statement checked:** The same fixed smooth background and density of the accepted projective-threefold construction; P^2=Q^2=R^2=0 and P wedge Q wedge R>0; cube=6xyz P wedge Q wedge R.

The whole local source was read. Its exact coefficients, endpoint flatness, support cutoffs, ddc normalization, global extensions, background, density and original slopes agree with every use in the new proof. This prerequisite is expressly accepted under degenerate_nonuniqueness_01, so its external citations are not reopened.

**Finding:** applicable; no critical error or gap.

### 2. Lipschitz/Sobolev calculus and elementary real-variable steps

**Classification:** explicitly permitted standard calculus.

**Statement checked:** Continuous finitely piecewise smooth functions with bounded derivatives are Lipschitz; C1,1 functions have L-infinity weak Hessians; the local Sobolev chain rule and mollification approximation apply; the intermediate value theorem and elementary integration apply.

All applications have been expanded in ordered statement checks: finite joins match, charts are restricted to compact subsets, local smoothing stays inside the larger coordinate ball, and the root functions have strict opposite endpoint signs. No external-paper citation or new PDE theorem is used.

**Finding:** applicable; no critical error or gap.

### 3. Bedford--Taylor paragraph: local uniform continuity

**Classification:** explicitly permitted input with arxiv first corroboration.

**Statement checked:** Let v_j and v be locally bounded plurisubharmonic functions on an open subset of C^n. If v_j converges locally uniformly to v, then for each 1 <= k <= n the Bedford--Taylor currents (dd^c v_j)^k converge weakly to (dd^c v)^k.

The theorem covers locally bounded psh approximants converging uniformly on compact subsets to continuous psh limits, together with positive closed currents converging weakly. Here use the repeated limit v=u_tilde+psi, its smooth psh convolutions, and the fixed degree-zero current 1. The limit is C1,1, hence continuous. This gives every required power up to degree three. A positive constant change of ddc convention rescales both sides equally.

**Corroborating source:** [Mounir Hajli, Théorème 4.1, equation (6), printed page 5](https://arxiv.org/pdf/1301.1796). The theorem-search result was checked against the PDF.

The decreasing-sequence statement in arXiv:1804.02894 and the capacity/Cegrell-class statement in arXiv:1601.03152 were not used: they have different hypotheses. The uniform-convergence theorem is the applicable returned result.

The nonclosed background is not substituted for the theorem's closed current. It is incorporated afterwards by multiplying identified powers by smooth forms in the algebraic expansion; statement check 10 verifies this separately.

The PDF was successfully read and confirms the arXiv theorem result; the experimental HTML endpoint was unavailable. No new PDE result is imported.

**Finding:** applicable; no critical error or gap.

## Independent cross-checks

One independent audit examined global regularity, weak Hessians, local Bedford–Taylor products and the nonclosed-background expansion. A second examined scalar roots, support conditions, distinctness and involution symmetry. Both found zero errors or gaps; their reasoning was reconciled with the ordered audit above.

## Final synthesis

All required hypotheses and every deduction pass. Both issue lists are empty, so the strict verdict is **correct**. No repair is required. The authoritative JSON is [verification.json](verification.json), written through the verification MCP.
