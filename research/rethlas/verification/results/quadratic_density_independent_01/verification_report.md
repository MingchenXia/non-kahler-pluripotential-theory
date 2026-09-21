# Independent verification report

Run: `quadratic_density_independent_01`

**Strict verdict: correct.** Critical errors: **0**. Mathematical gaps: **0**.

This audit verifies the submitted quadratic-density construction in its written order. It uses the accepted rank-one frame and scalar coordinate from [the original source, lines 15–50](/Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex:15), together with the expressly permitted scalar ODE theory, elementary calculus, Hermitian positivity, and closed bounded Bedford–Taylor/Stokes. Every new coefficient, correction, density, and ODE argument has been recomputed. No numerical evidence, finite-order uniqueness theorem, new PDE premise, or novelty claim is used. No other audit or memory of this quadratic construction was inspected. The book was not edited.

The source was read only to verify the accepted frame and normalization. An initial source keyword scan displayed some surrounding material from the original section; none of those other constructions or arguments was adopted. All persistent audit records belong to this run.

## Main identities checked

The exact source normalization gives
\[
dd^c G(r)=G'(r)(P-Q)+G''(r)R,\qquad
\sigma'=\sigma(1-\sigma),
\]
and
\[
g=\frac{xyz}{\sigma(1-\sigma)\sigma'},\qquad
h'=h\,\frac{z(x-y+h)}{(x+h)(y-h)}.
\]
The factors \(6P\wedge Q\wedge R\) cancel in the density identity.

For \(d=1-|r|\) near either interface, the logarithmic estimates give
\[
|h(r)|\le C e^{-A/d},\qquad
|h^{(j)}(r)|\le C_j e^{-A/d}d^{-N_j}\quad(j\ge0).
\]
The derivative argument keeps the same positive \(A\) at every order. At each interface, \(h=h'=0\), and the solution form has the same rank-two value as \(\omega_0\).

The bounded-mass conclusion is the uniform estimate
\[
\sup_{v\in {\rm PSH}(X,\omega)\cap L^\infty(X)}
\int_X(\omega+dd^c v)^3
\le C^3\int_X\omega_X^3<\infty.
\]

## Sequential deduction checks

The following items follow the textual order of the submitted proof. The substeps explicitly expand the standard calculus and continuation arguments already present in the submission; they do not insert an additional construction or hypothesis.

### 01. Theorem and accepted frame recall

Status: **passes**.

1. Target requires one fixed globally smooth nonclosed positive background with BMP, a globally smooth nonnegative density with exactly two hypersurface zeros of exact order two, and an uncountable family of distinct normalized smooth semipositive solutions.

2. Source lines 15–50 give ddc=(i/2pi)∂bar∂ in the book normalization, since source 2i∂bar∂ is 4pi times the book operator. The scalar functions are not rescaled; P,Q,R and FS use the same rescaled operator.

3. With R=dr∧d^c r and dd^c r=P−Q, dd^c G=G'(P−Q)+G''R exactly; sigma'=e^r/(1+e^r)^2=sigma(1−sigma). Cubes are 6 times the coefficient product times PQR, so there is no missing factor in the density or ODE.

4. The local expression ∂r=(bar a da)/(1+|a|²)−dτ/τ−(bar b db)/(1+|b|²) proves dr is nonzero on U. Finite r levels are compact smooth real hypersurfaces away from the two projective lines.

### 02. Equation (quadratic-background): cutoff existence, zero sets and global extension

Status: **passes**.

1. Smooth cutoffs with the stated plateaus and ranges exist by elementary smooth step functions; monotonicity of a is unnecessary. b(r)=a(−r) and even chi imply y(r)=x(−r).

2. p=(1−r²)^2 is nonnegative and vanishes only at r=±1. z=(1−chi)+chi sigma' is strictly positive at every finite r.

3. If chi>0 then the positive FS summand makes x and y strictly positive. If chi=0 then x=p+a and y=p+b. At −1, a=1,b=0, so (x,y,z)=(1,0,1); at +1, a=0,b=1, so (x,y,z)=(0,1,1). These are all zeros.

4. All coefficients are smooth on R. For |r|>=3/2 they coincide identically with FS coefficients, so omega0=FS on neighborhoods of both omitted lines and extends smoothly. Its rank is three off M± and two on M±.

5. The real hypersurfaces M± are disjoint and compact: |A|²=e^{±1}|B|² precludes either A=0 or B=0.

### 03. Strict correction omega=omega0+ddc rho

Status: **passes**.

1. rho=epsilon(r²−1)kappa is smooth and identically zero near both projective ends, hence global. On |r|<=3/2, rho'=2epsilon r and rho''=2epsilon exactly.

2. On [0,3/2], x+2epsilon r>0: x>0 except at r=1 where 2epsilon r>0; at r=0, x=1. On [−3/2,0], x has a strictly positive compact minimum m, so epsilon<m/3 suffices for x+2epsilon r>0.

3. Using y(r)=x(−r), y−2epsilon r is positive by the reflected same argument. No evenness of kappa is required outside this central interval.

4. z+2epsilon>0 centrally. On the compact annuli 3/2<=|r|<=2, all original FS coefficients have a strictly positive minimum and rho',rho'' are uniformly O(epsilon); one sufficiently small common positive epsilon preserves all three coefficients.

5. For |r|>=2, rho=0 and omega=FS. Frame independence equates positivity of all three coefficients with positive definiteness, establishing a global smooth Hermitian background.

### 04. Nonclosedness at r=0

Status: **passes**.

1. dP=dQ=0 follows from their dd^c definitions, and dR=−dr∧dd^c r=−dr∧(P−Q). Therefore d omega0=dr∧((x'−z)P+(y'+z)Q). Since ddd^c rho=0, d omega=d omega0.

2. Near zero, chi=a=b=0, so x=y=p, x'(0)=y'(0)=0 and z=1. Thus d omega|_{r=0}=dr∧(Q−P).

3. This 3-form is nonzero: wedging it with d^c r∧P gives Q∧R∧P (up to the immaterial reordering sign) and the P² term vanishes, leaving nonzero PQR. Hence omega is not closed.

### 05. Definition and exact quadratic vanishing of g; baseline solution

Status: **passes**.

1. Define g=omega0³/FS³ globally. The denominator is a nowhere-zero smooth volume form, giving a global smooth function; g=1 near the omitted lines.

2. On U, g=xyz/[sigma(1−sigma)sigma']. Near −1 the exact coefficients are (1+p,p,1), and near +1 they are (p,1+p,1); hence xyz=(1+p)p in both neighborhoods.

3. For t=r−1 near +1, p=t²(r+1)²; for t=r+1 near −1, p=t²(1−r)². In either case g=t² q with q smooth strictly positive, since the extra square factor equals 4 at the interface and sigma(1−sigma)sigma'>0. Thus the vanishing order is exactly two.

4. The rank/zero calculation proves g>0 everywhere else, with no zeros introduced by cutoff transitions or at the projective lines.

5. omega+dd^c(−rho)=omega0 is globally semipositive and has cube g FS³, so −rho is a smooth baseline solution.

### 06. Lemma quadratic-density-trapping: smooth ODE domain and residual calculations

Status: **passes**.

1. Inside (−1,1), chi=0 and p>0, hence x=p+a>0, y=p+b>0 and z=1. The open domain D={−x<h<y} contains the zero graph and F(r,0)=0; at r=0 it also contains h=−eta for eta<1.

2. For B(r)=−cp, B'=−cp', so the contact residual is F(r,B)−B'=F(r,−cp)+cp'. At the left it equals (1+p)/[(1+(1−c)p)(1+c)]−1+cp', tending to −c/(1+c). At the right it equals (1+p)/[(1−c)(1+(1+c)p)]−1+cp', tending to c/(1−c). Both cancellations divide only by p>0 inside the band.

3. Fix any c in (0,1), for example c=1/2. Exact endpoint coefficients and strict residual limits hold on fixed sufficiently small neighborhoods, independent of eta. The lower barrier lies in D there.

4. At contact w=h+cp=0, w'<0 on the left; a graph w>0 at a fixed right-hand point cannot become negative while integrating backward. On the right w'>0 at contact prevents loss of w>0 while integrating forward. Both directions are correct.

### 07. Lemma quadratic-density-trapping: common eta interval, sign and continuation

Status: **passes**.

1. Choose fixed ell<0<t in the left and right barrier neighborhoods. On [ell,t], the zero graph is compactly contained in D. A uniform tube of radius delta smaller than half the minimum of x,y and smaller than cp(ell),cp(t) is available.

2. Permitted compact ODE continuous dependence around the zero solution supplies a single eta0>0 such that every 0<eta<eta0 exists on the entire fixed middle interval, remains in this tube and lies above the lower barrier at its endpoints. This is a common parameter interval, not an eta-dependent shrinking sequence.

3. Uniqueness on D implies a solution starting negative cannot meet the exact solution zero at any interior finite time, so h<0 on its connected maximal interval.

4. The crossing arguments preserve −cp<h<0 on each endpoint neighborhood within the maximal interval. On the left, x+h>=1+(1−c)p and y−h>=p; on the right, x+h>=(1−c)p and y−h>=1+p.

5. On every compact part of an endpoint neighborhood inside (−1,1), p has a positive minimum and the closed trap is bounded and compactly contained in D. The middle graph is already compactly contained in D. A putative finite interior endpoint therefore has a compact continuation neighborhood with bounded smooth F, contradicting maximality.

6. Thus the solution exists on (−1,1). No existence or uniqueness assertion is used at the singular boundary points (±1,0).

### 08. Lemma quadratic-density-trapping: exact logarithmic factorization and signs

Status: **passes**.

1. xy−(x+h)(y−h)=h(x−y+h), giving exactly h'=h z(x−y+h)/[(x+h)(y−h)]. For h<0, d/dr log(−h)=h'/h=L; there is no extra minus sign.

2. On the left, L=(1+h)/[(1+p+h)(p−h)]. Trap and small p give 1+h>=1−cp>=1/2, and the positive denominator is <=(1+p)(1+c)p. Hence L>=C1/p for a fixed C1>0.

3. On the right, L=(−1+h)/[(p+h)(1+p−h)]. The numerator is <=−1 and the positive denominator is <=p(1+(1+c)p). Thus L<=−C2/p for C2>0; bounding this negative quotient uses the correct inequality direction.

4. On either endpoint neighborhood, p=d²(2−d)² is comparable to d² and satisfies p<=4d². With f=log(−h), backward left integration yields f(r)<=f(ell)−(C1/4)[1/(1+r)−1/(1+ell)].

5. Forward right integration yields f(r)<=f(t)−(C2/4)[1/(1−r)−1/(1−t)]. Taking A=min(C1,C2)/4 gives |h|<=C exp(−A/d) on both ends. Polynomial p creates inverse-square logarithmic drift, which produces exponential decay; it does not obstruct it.

### 09. Lemma quadratic-density-trapping: partial-derivative bounds and all-order induction

Status: **passes**.

1. In the endpoint neighborhoods x,y are explicit polynomials in r, z=1, and h is bounded. On the left the denominator factors of L are >=1 and >=p; on the right they are >=(1−c)p and >=1. Every mixed partial derivative of the rational function L evaluated on the graph is bounded by a finite power of p^(-1), hence d^(-1).

2. Assume |h^(k)|<=Ck exp(−A/d)d^(−Nk) for all k<=j. Then h^(j+1)=sum_{k=0}^j binom(j,k) h^(k) D^(j−k)[L(r,h(r))].

3. Every composite derivative of order j−k uses only partial derivatives of L and h-derivatives through order j−k<=j. The induction hypothesis bounds these polynomially after discarding their factors exp(−A/d)<=1. No derivative of order j+1 appears on the right.

4. The explicit factor h^(k) in every summand retains exp(−A/d). A finite sum therefore yields the same exponential factor with a new finite polynomial power. The base j=0 follows from the decay estimate and polynomial bound for L.

5. Every derivative tends to zero, since exp(−A/d)d^(−N)→0 for each finite N. Extending derivatives by zero gives continuous functions. Applying the mean value theorem to endpoint difference quotients identifies each successive extension as the derivative of the preceding one. The zero extension is C∞ and flat.

### 10. Theorem proof: global primitives, semipositivity and fixed equation

Status: **passes**.

1. A primitive G_eta of the smooth zero extension satisfies G_eta'=h_eta. It is constant on each of (−infinity,−1] and [1,infinity), possibly with different constants; those disjoint neighborhoods extend over the corresponding projective lines. Thus G_eta and u_eta=G_eta−rho are globally smooth.

2. The accepted chain rule gives omega+ddc u_eta=(x+h_eta)P+(y−h_eta)Q+(z+h_eta')R exactly. Inside the band the first two coefficients are positive and the ODE gives z+h_eta'=xyz/[(x+h_eta)(y−h_eta)]>0.

3. Outside the band h_eta=h_eta'=0, so the form equals omega0. At r=±1 flatness gives the same equality and hence exactly rank two, retaining the radial coefficient z=1. There are no interface delta terms because the potential is smooth.

4. Inside the band the coefficient product is xyz. The cube identity equals omega0³ there and outside. At the interfaces it holds either by direct coefficient substitution or continuity, without evaluating the singular quotient ODE.

5. Both omega and g were fixed before eta. Therefore every u_eta solves precisely the same global equation and is smooth omega-psh.

### 11. Theorem proof: normalization and uncountable distinctness

Status: **passes**.

1. For eta!=theta, d(u_eta−u_theta)|_{r=0}=(theta−eta)dr is nonzero. The common correction cancels, and dr≠0 on that hypersurface. Thus the potentials do not differ by constants.

2. Compactness and smoothness ensure each finite supremum is attained. Subtracting it changes neither dd^c nor semipositivity nor the equation.

3. If normalized potentials coincided, their unnormalized difference would be constant, contradicting the derivative at zero. Thus the map from the nonempty interval (0,eta0) to normalized solutions is injective, providing uncountably many.

### 12. Theorem proof: bounded mass using closed bounded Bedford–Taylor/Stokes

Status: **passes**.

1. Compactness and strict positivity of FS yield a constant C with omega<=C FS. For any bounded omega-psh v, T=omega+ddc v>=0 and A=C FS+ddc v=T+B>=0, with B=C FS−omega a smooth semipositive form. A is closed and has locally bounded psh potentials.

2. For smooth forms, positivity of the mixed expansion gives 0<=T³<=(T+B)³=A³. For bounded v this follows using only permitted closed BT: on a smaller chart use a nonnegative radial mollifier on a bounded psh local potential of A, and convolve B at the same scale. Then A_e=T_e+B_e with T_e,B_e>=0, hence 0<=T_e³<=A_e³.

3. Closed bounded BT convergence gives A_e^j→A^j; B_e→B smoothly. Expansion of (A_e−B_e)³ then passes to the BT polynomial defining T³, proving 0<=T³<=A³ without assuming a new theorem for nonclosed backgrounds.

4. Closed bounded Stokes yields integral_X A³=C³ integral_X FS³. Consequently integral_X(omega+ddc v)³<=C³ integral_X FS³ uniformly over all bounded omega-psh v; this is BMP, stronger than a bound merely on the displayed smooth family.

5. The prior-construction phrase 'as before' is unnecessary: this argument is recomputed from the present positive background and the allowed closed bounded inputs.

### 13. Concluding interpretation and scope

Status: **passes**.

1. Quadratic density zeros coexist here with smooth nonuniqueness; no finite-order uniqueness theorem is assumed or contradicted as a premise. The positive-density set is exactly the three r-regions cut out by −1 and +1, with the appropriate projective lines included in the outer regions.

2. Each region is connected: choose unit vectors alpha,beta in S³ and use [e^{r/2}alpha:beta]; S³×S³×I maps continuously onto the corresponding U-region for any interval I. Adding the limiting projective line to either outer region preserves connectedness.

3. Precise meaning of the informal phrase 'flat differences of potentials': h_eta−h_theta is flat, and each potential difference minus its own limiting constant has a zero infinite jet at each interface. The constants at the two interfaces need not be equal. The proof never requires the potential difference itself to have zero value at both interfaces under one global normalization.

4. This terminological precision affects no deduction: smooth gluing uses only the proved flatness of h and its derivatives. No claim concerning a connected positive-density set or novelty is established or needed.

## Reference and independence checks

1. **Accepted internal frame.** The source uses \(r=\log(|A|^2/|B|^2)\), \(P=dd^c\log|A|^2\), \(Q=dd^c\log|B|^2\), and \(R=dr\wedge d^c r\). Its convention is checked in item 01. No earlier background, positivity correction, density, or nonuniqueness construction is accepted as an input.

2. **Scalar ODE principles.** These are expressly permitted. Their hypotheses are checked on the open smooth domain and compact subintervals in items 06–09. In particular, uniqueness is never invoked at \((\pm1,0)\).

3. **Closed bounded Stokes.** As corroboration of this permitted input, the full bounded Kähler total-mass statement was queried with search_arxiv_theorems first. The three returned statements, from arXiv:1602.03778, 1606.05470, and 1609.01377, concern different results and were rejected as matches. Built-in web search with the same statement then located the standard mass identity in the proof of Proposition 3.5(1), printed page 615, of [Guedj–Zeriahi, *Intrinsic capacities on compact Kähler manifolds*](https://www.math.univ-toulouse.fr/~guedj/fichierspdf/JGA05.pdf). That identity concerns a **closed Kähler background** and bounded plurisubharmonic potentials. In the present proof it is applied only to \(C\omega_X\). Item 12 separately proves the inequality transferring the bound to the constructed nonclosed background. No new literature premise enters.

4. **Earlier-construction allusions.** The phrases “same kind of correction as before” and “same uniform bounded-mass estimate as before” create no unresolved dependency: the correction and bound were verified directly from the submitted data. No other quadratic-construction report or memory was read.

## Precision about “flat differences”

The formal lemma proves flatness of the zero-extended **slopes** \(h_\eta\). Consequently, for any two parameters, every positive-order derivative of \(G_\eta-G_\theta\) vanishes at both interfaces. More precisely,
\[
(G_\eta-G_\theta)(r)-(G_\eta-G_\theta)(\pm1)
\]
has zero infinite jet at the corresponding interface. The two endpoint constants generally differ.

Indeed, uniqueness prevents two distinct slope solutions from meeting anywhere inside the band, so their difference has one strict sign there. Its integral from \(-1\) to \(1\) is nonzero. Thus a single global additive constant cannot make the potential difference have zero value at both interfaces.

The introductory and concluding descriptions of potential differences as “flat” should therefore be understood as **locally constant to infinite order at each interface**. This is a terminology clarification, not a missing hypothesis or a gap in the proof: the gluing argument explicitly relies on the proved flatness of \(h_\eta\), and it correctly allows the primitive to have different constants at the two projective ends.

## Strict disposition

Every formal assertion needed for the theorem passes: global smoothness, strict positivity of the corrected background, nonclosedness, exactly quadratic density vanishing, existence on one common parameter interval, continuation throughout the open band, decay at both ends, smooth flat extension, rank-two semipositive gluing, one fixed equation, normalized injection, and bounded mass.

- Critical errors: none.
- Mathematical gaps: none.
- Repair hints: empty, as required for a correct verdict.

The machine-readable companion is [verification.json](verification.json). Ordered details and reference checks are also persisted in this run's MCP memory.

