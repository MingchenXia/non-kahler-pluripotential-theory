# Verification report: divisorial constraints and residual volume

**Run:** `divisorial_gauduchon_volume_01`  
**Verdict:** **correct**  
**Findings:** 0 critical errors; 0 gaps.

## Summary and scope

All claims in the supplied two sections pass, including feasibility for nonclosed backgrounds, the attained coefficient threshold, gauge-independent residual volume, the smooth-remainder equation, scalar uniqueness for every bounded ordinary-type remainder, the root-volume variation statements, and the Hopf constants and upper-mass claim. The audit accepts exactly the prerequisites authorized by the user and checks their applications here. It makes no uniqueness assertion for an arbitrary bounded remainder.

The standing hypotheses are compact connected complex X, dimension n>=1, ddc=i partial barpartial/(2 pi), a smooth real background, a finite effective real divisor, and the inherited smooth strictly positive probability form mu. The fixed divisor is nonzero in the threshold discussion and its coefficient family; effective coefficients t are nonnegative. No BMP or PVP is assumed.

**Input:** [supplied statement and proof](/Users/mingchen/Non-Kahler/research/rethlas/verification/inputs/divisorial-gauduchon-volume.md). The local input was read and matches the user text. Book and source files were used only as evidence and were not edited.

## Sequential verification

The items below follow the proof's textual order. Each numbered deduction was checked individually.

### 1. Divisorial setup and degree identity

1. Local log norms are log|f_j|^2 minus smooth metric weights, hence locally integrable and quasi-psh; finite real weighted sums are permitted.
2. Poincare-Lelong in ddc=i partial barpartial/(2 pi) gives ddc sigma_D=[D]-eta_D with no missing factor.
3. For rational a_j choose m with m a_j integers; locally sigma_D=m^{-1}log|product f_j^{m a_j}|^2+smooth. This is a single principal-ideal analytic singularity expression.
4. Integration currents over compact analytic divisors have finite mass; a strictly positive complementary metric gives strictly positive degree when D is nonzero, including weighted point counts for n=1.
5. Distributional Stokes gives integral ddc sigma_D wedge gamma^{n-1}=integral sigma_D ddc gamma^{n-1}=0.

**Finding:** no critical error or gap.

### 2. Proposition Divisorial feasibility

1. For T=theta+ddc u the smooth derivative is dtheta; accepted nonclosed divisorial removal applies to the qpsh potential without assuming T closed.
2. Removing full generic coefficients and adding back the nonnegative excess proves T-[D]>=0.
3. u-sigma_D is an L1 distribution with ddc bounded below by the smooth -beta_D, so its canonical quasi-psh representative lies in PSH(beta_D).
4. Conversely v in PSH(beta_D) gives the globally quasi-psh u=sigma_D+v and positive T=[D]+beta_D+ddc v. Local generic Lelong numbers add and that of v is nonnegative.
5. Accepted Lamari applies to the arbitrary smooth real residual background when n>=2; its degrees are exactly the displayed residual integrals.
6. For n=1, m=integral beta_D>=0 and smooth probability mu make m mu-beta_D integral zero. The accepted Green criterion provides smooth f with beta_D+ddc f=m mu>=0; necessity is Stokes.
7. None of these implications forces bounded residual type or exact coefficients.

**Finding:** no critical error or gap.

### 3. Equation divisorial-gaud-threshold and endpoint attainment

1. D is fixed nonzero and t ranges over nonnegative coefficients. Every denominator is strictly positive.
2. Pseudoeffectivity of theta makes all ratios nonnegative; testing any fixed Gauduchon metric gives a finite upper bound.
3. Feasibility is equivalent to t being no greater than every ratio, equivalently t<=their infimum.
4. At the infimum every weak inequality still holds. Apply residual feasibility/Lamari (Green for curves) directly, including when tau=0.
5. The current attains the coefficient threshold; no assertion that a smooth test metric attains the infimum is needed.

**Finding:** no critical error or gap.

### 4. Residual volume definition and equation divisorial-gaud-volume

1. The inherited denominator is D_mu(gamma)=integral (mu/gamma^n)^{1/n}gamma^n>0 for smooth strictly positive probability mu.
2. The displayed formula is exactly the accepted definition lambda_mu(beta_D) after using the degree identity; its nth power is the defined residual volume.
3. Residual pseudoeffectivity makes every quotient nonnegative. One fixed metric bounds it above finitely.
4. A change of line-bundle metric changes eta_D by smooth ddc f, hence changes the numerator by zero against every Gauduchon test. The same holds for a smooth ddc change of theta.
5. For n=1 D_mu=integral mu=1 and the residual volume is integral theta-degree D. No mass invariant of all singular or bounded potentials is being defined.

**Finding:** no critical error or gap.

### 5. The residual equation: smooth remainder

1. Choose a smooth positive representative of beta_D. The accepted smooth equation setup and dual formula supply normalized smooth v, Omega=beta_D+ddc v>0 and Omega^n=V_mu(beta_D)mu with positive scalar.
2. Poincare-Lelong gives the positive current theta+ddc(sigma_D+v)=[D]+Omega.
3. Off the divisor the potential is smooth and its local top-degree product is Omega^n. Both the smooth measure and the non-pluripolar extension give zero mass to the divisor, hence they agree globally.
4. The residual smooth equation uniqueness gives uniqueness modulo constants of smooth remainders and of their scalar. Positivity of any smooth residual competitor follows by continuity from the complement; a positive smooth density makes that form positive definite.

**Finding:** no critical error or gap.

### 6. The residual equation: arbitrary bounded ordinary-type remainder

1. Ordinary type means two-sided bounded difference from sigma_D. Thus w=u-sigma_D is bounded off D and defines an L1 function; it is not presumed smooth, continuous or already residual-psh.
2. On a relatively compact coordinate ball choose q=A|z|^2 with ddc q>=beta_D. Then p=w+q is bounded psh off D and extends as a bounded psh function across D by the permitted removability theorem.
3. The extension agrees with the L1 function p because D has zero Lebesgue measure; local choices glue to the canonical qpsh representative of w.
4. Write T=beta_D+ddc w=ddc p+(beta_D-ddc q). With kappa=ddc|z|^2, the trace ddc p wedge kappa^{n-1} is a locally bounded BT mixed measure and has no mass on D. Positive-current coefficient measures are controlled by this trace; the smooth correction also has no mass on D. Thus T has no coefficient mass on D and its positivity on the complement extends globally.
5. For n=1 the complementary factor is 1 and bounded subharmonic Laplacian measures have no point atoms. The same current extension argument applies.
6. The local bounded residual top product is the finite signed expansion sum binomial(n,k)(ddc p)^k wedge (beta_D-ddc q)^{n-k}. Every term has zero mass on D, because its coefficient measures are bounded BT measures times smooth factors. This remains valid without closedness or semipositivity of beta_D.
7. Off D the residual bounded product and the original extended product coincide by local potential calculus. Both vanish on D, yielding the asserted global measure identity. This is an equality of measures, not the false current identity theta+ddc u=beta_D+ddc w.
8. Subtract v0 to put both bounded residual potentials in the same strictly positive Hermitian background Omega0.
9. If scalar A is smaller than B>0, the two measures satisfy MA(a)<=q MA(b+C) globally for every C, with q=A/B<1. Accepted strict domination then gives a>=b+C for all C, a contradiction. If A=0, q=0 is explicitly allowed, so the same argument works.
10. This proves scalar uniqueness for every bounded ordinary-type remainder and makes no claim of uniqueness of that bounded remainder; no uniform mass bound or uniform positive lower mass is used.

**Finding:** no critical error or gap.

### 7. Concavity, monotonicity, derivative, and nef endpoint paragraph

1. On the feasible interval each quotient is A_gamma-t B_gamma with B_gamma=degree_gamma D/D_mu(gamma)>0 for fixed nonzero D. The infimum of these affine functions is concave and nonincreasing.
2. On a subinterval with positive residual representatives, the accepted first variation applies to the smooth family theta-t eta_D with variation -eta_D; degree/Stokes identifies its derivative with the stated negative ratio.
3. A minimizing metric exists there by the accepted positive-cone dual formula; scaling it changes numerator and denominator equally.
4. For n=1 every quotient is integral theta-t degree D, and D_mu=1, giving derivative -degree D.
5. If an endpoint background is nef in the nonclosed definition, the accepted nef-limit theorem identifies its volume with the decreasing limit of positive perturbed equation scalars. No endpoint differentiability is asserted.

**Finding:** no critical error or gap.

### 8. Hopf setup and Proposition hopf-divisorial-threshold: threshold

1. Use accepted normalized Hopf geometry: alpha closed semipositive rank 2, zeta semipositive rank 1, complementary kernels, alpha^3=zeta^2=0, ddc zeta=-alpha^2, integral alpha^2 zeta=2.
2. The hyperplane pullback line bundle has smooth metric curvature alpha, so ddc sigma_H=[H]-alpha. Projectivization is a submersion with connected elliptic fibers and H is a nonzero effective divisor.
3. R_a=(1-a)alpha+zeta is positive for a<1 and semipositive at a=1, proving feasibility for 0<=a<=1.
4. gamma_t=alpha+t zeta is positive for t>0. Since alpha is closed, ddc(gamma_t^2)=2t alpha wedge ddc zeta=-2t alpha^3=0; there are no omitted torsion cross terms.
5. gamma_t^2=alpha^2+2t alpha zeta, so degree_gamma_t H=4t and integral omega gamma_t^2=2+4t. The ratio (1+2t)/(2t) tends to 1 as t tends to infinity.
6. The general threshold formula bounds tau above by 1 and the semipositive endpoint bounds it below by 1.

**Finding:** no critical error or gap.

### 9. Proposition hopf-divisorial-threshold: residual volume and boundary

1. omega^3=3 alpha^2 zeta and integral omega^3=6, hence mu0=omega^3/6 is a smooth strictly positive probability measure.
2. R_a^3=3(1-a)^2 alpha^2 zeta=6(1-a)^2 mu0. For a<1 the zero smooth remainder is a positive equation solution, so the accepted dual formula identifies its scalar with residual volume.
3. zeta+epsilon omega=epsilon alpha+(1+epsilon)zeta is positive; this proves nefness in the accepted nonclosed sense.
4. Its cube is 6 epsilon^2(1+epsilon)mu0, so the perturbed scalars converge to zero. The accepted nef-limit theorem gives V_mu0(zeta)=0.
5. At a=1, theta+ddc sigma_H=[H]+zeta is a nonzero positive current while its non-pluripolar top measure is zero: off H it is zeta^3=0 and H is discarded. No current mass is confused with the top non-pluripolar measure.

**Finding:** no critical error or gap.

### 10. Proposition hopf-divisorial-threshold: infinite upper mass

1. For each fixed real a<1, choose delta>0 no greater than both 1-a and 1. Then R_a-delta omega=(1-a-delta)alpha+(1-delta)zeta>=0.
2. The accepted smooth Hopf sequence gives R_a+ddc(delta V_j)>0, since it is the sum of this semipositive form and delta times a positive form.
3. Pointwise determinant monotonicity yields (R_a+ddc(delta V_j))^3>=delta^3(omega+ddc V_j)^3.
4. delta is fixed as j varies and positive, so integrating gives divergence to infinity. Smooth potentials are bounded on compact X, proving infinite upper mass. The proof even works for negative a if one considers R_a simply as a background, though divisorial effectiveness uses a>=0.
5. This does not contradict the finite Gauduchon volume, which is the scalar for one fixed prescribed probability density.

**Finding:** no critical error or gap.

### 11. Closing interpretation and hypothesis audit

1. The conclusions concern a specified finite divisor on X and do not assert compatibility on modifications. Pullback of a smooth positive volume form under a nontrivial modification is allowed to vanish along the exceptional locus, outside the smooth strictly positive-density equation hypothesis.
2. Compactness supplies finite integrals, global smooth bounds and boundedness of individual smooth potentials; connectedness underlies the Green solvability condition and uniqueness modulo one additive constant.
3. Finiteness/effectivity of D supplies finite nonnegative currents and positive degrees; nonzero D is needed for threshold denominators and strict derivative. Rationality is optional and used only for the analytic-singularity remark.
4. The proof covers n=1 separately and never assumes nonclosed backgrounds have local potentials. It uses local smooth corrections and signed bounded expansions instead.
5. No BMP, PVP, arbitrary singular uniqueness theorem, or uniform noncollapse statement is imported.

**Finding:** no critical error or gap.


## Expanded check of the bounded-remainder argument

This is the main analytic point. The following makes explicit the reasoning already present in the proof, using the permitted local inputs.

Let \(A=|D|\), and let \(w=u-\sigma_D\) on \(X\setminus A\). Ordinary singularity type gives a two-sided bound for \(w\). On a relatively compact coordinate ball choose \(q=C|z|^2\) with \(dd^cq\geq\beta_D\). Then \(p=w+q\) is bounded psh off \(A\) and has a bounded psh extension \(\widetilde p\). Since \(A\) has Lebesgue measure zero, this extension represents the original \(L^1\) function \(w+q\); choosing the canonical representative does not insert an extra distributional term.

Write \(\kappa=dd^c|z|^2\). The trace measure \(dd^c\widetilde p\wedge\kappa^{n-1}\) is a locally bounded Bedford–Taylor mixed measure and does not charge \(A\). The coefficient measures of a positive current are controlled by its trace. The smooth form \(B=\beta_D-dd^cq\) also has no mass on \(A\). Therefore
\[
T=\beta_D+dd^cw=dd^c\widetilde p+B
\]
has zero coefficient-measure restriction to \(A\). Its restriction to the complement is positive, so the current is positive everywhere. The local extensions give the canonical bounded residual-psh representative.

For \(n=1\), the complementary factor is \(1\); the statement is that a bounded subharmonic function has no atomic Laplacian mass at a divisor point. Thus the same argument works on curves.

The nonclosed bounded product is locally
\[
T^n=\sum_{k=0}^n\binom nk(dd^c\widetilde p)^k\wedge B^{n-k}.
\]
The summands are not individually presumed positive. Each has locally finite variation and zero mass on \(A\): its BT factor has noncharging coefficient measures, and the other factor is smooth. This includes the all-smooth term. Local equality of products off \(A\), together with zero mass on \(A\) on both sides, now proves
\[
\mathrm{MA}^{\mathrm{ext}}_\theta(u)=T^n.
\]
Compactness makes the mass of this fixed bounded product finite. The underlying current remains
\[
\theta+dd^cu=[D]+T.
\]
This is why removal of divisorial mass from the measure does not remove it from the current.

Finally choose \(\Omega_0=\beta_D+dd^cv_0>0\). If two bounded residual potentials have scalars \(0\leq A_0<B_0\), label their \(\Omega_0\)-psh representatives \(f,g\). For every real \(C\),
\[
\mathrm{MA}_{\Omega_0}(f)
=\frac{A_0}{B_0}\,\mathrm{MA}_{\Omega_0}(g+C).
\]
Restriction to \(\{f<g+C\}\) is exactly the accepted bounded strict-domination hypothesis, with ratio in \([0,1)\). It would give \(f\geq g+C\) for all \(C\), impossible for bounded functions.

This includes \(A_0=0\). The proof's non-collapse sentence is an immediate consequence of the same accepted theorem, by comparing a hypothetical zero-measure bounded potential with a constant above its supremum. There is no additional theorem or uniform positive lower mass assumption. The conclusion concerns scalar uniqueness for every bounded ordinary-type remainder and does not infer equality of arbitrary bounded remainders.

## Explicit arithmetic checks

The accepted Hopf normalization is \(\int_X\alpha^2\wedge\zeta=2\). Thus
\[
\gamma_t^2=\alpha^2+2t\alpha\wedge\zeta,\qquad
\deg_{\gamma_t}H=4t,\qquad
\int_X\omega\wedge\gamma_t^2=2+4t.
\]
The ratio is \(1+1/(2t)\), tending to \(1\) as \(t\to+\infty\). The semipositive residual form at coefficient \(1\) supplies the reverse inequality and endpoint feasibility.

For the volume,
\[
\omega^3=3\alpha^2\wedge\zeta,\qquad
\int_X\omega^3=6,\qquad
R_a^3=6(1-a)^2\mu_0.
\]
The zero smooth remainder is an admissible positive solution for \(a<1\). At the endpoint,
\[
(\zeta+\epsilon\omega)^3
=(\epsilon\alpha+(1+\epsilon)\zeta)^3
=6\epsilon^2(1+\epsilon)\mu_0.
\]
The accepted nef-limit theorem therefore gives zero boundary volume. Separately, the nonzero positive current \([H]+\zeta\) has zero non-pluripolar top measure.

For each fixed \(a<1\), choose \(0<\delta\leq\min(1-a,1)\). Then
\[
R_a-\delta\omega=(1-a-\delta)\alpha+(1-\delta)\zeta\geq0
\]
and the accepted smooth sequence gives
\[
\int_X(R_a+dd^c(\delta V_j))^3
\geq\delta^3\int_X(\omega+dd^cV_j)^3\longrightarrow+\infty.
\]
The constant \(\delta\) is fixed while \(j\) varies. The conclusion is infinite upper mass for every \(a<1\), while the fixed-density Gauduchon volume remains finite.

## Reference evidence

The following exact local statements and definitions were consulted. Accepted prerequisite proofs and their upstream chapters were not re-audited.

| Reference | Location |
| --- | --- |
| Nonclosed divisorial removal | [chapter_divisorial_models.tex](/Users/mingchen/Non-Kahler/book/author/chapter_divisorial_models.tex:18) |
| Generalized Lamari criterion | [chapter_gauduchon.tex](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon.tex:127) |
| Smooth positive probability density and volume definition | [chapter_gauduchon_variational_volume.tex](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:10) |
| Smooth equation setup and positive-cone dual formula | [smooth setup](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:55), [dual formula](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:64) |
| First variation | [proposition](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:119) |
| Nef definition and limit | [definition and theorem](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon_variational_volume.tex:152) |
| Ordinary singularity type | [chapter_framework.tex](/Users/mingchen/Non-Kahler/book/author/chapter_framework.tex:89) |
| Nonclosed bounded-product convention | [chapter_products.tex](/Users/mingchen/Non-Kahler/book/author/chapter_products.tex:18) |
| Bounded strict domination and its nonzero-mass consequence | [theorem](/Users/mingchen/Non-Kahler/book/author/section_modified_comparison.tex:87), [corollary](/Users/mingchen/Non-Kahler/book/author/section_modified_comparison.tex:124) |
| Hopf sequence, geometry, and normalization | [sequence](/Users/mingchen/Non-Kahler/book/author/chapter_hopf.tex:8), [geometry](/Users/mingchen/Non-Kahler/book/author/chapter_hopf.tex:23), [fiber normalization](/Users/mingchen/Non-Kahler/book/author/chapter_hopf.tex:73) |
| Source-book analytic singularities | [SGPT Definition 1.6.1](/Users/mingchen/Non-Kahler/research/sources/SGPT.txt:1938) |

### External search and convention comparison

The full analytic-singularity definition was submitted first to search_arxiv_theorems. The three returned definitions (arXiv:1909.08820, 2211.08630, and 2210.06026) permit real or nonnegative coefficients, so they were not treated as exact matches to the source book's rational convention.

The supplied SGPT text explicitly requires positive rational coefficients and bounded remainders; a smooth remainder gives neat analytic singularities. A web fallback corroborated this in the author's [SGPT lecture manuscript, Definition 1.6.1](https://mingchenxia.github.io/Lectures/SGPT2.pdf#page=41). The final-version URL returned a browser error, so the readable supplied local source is the principal evidence. Clearing denominators in the finite rational divisor gives exactly the required single-generator expression.

The remaining citations in the proof are the accepted book prerequisites or the explicitly permitted local inputs. Their exact applicability is documented below; no stronger external singular-equation or uniqueness theorem was substituted.

## Exact reference applications

### R1. Divisorial setup: rational coefficients and analytic singularities

**Referenced content:** SGPT Definition 1.6.1: locally phi=c log(sum |f_j|^2)+R, with c in Q_{>0}, holomorphic f_j and bounded R; if R is smooth, neat analytic singularities.

**Definition and hypothesis check:** The cited source requires rational c, unlike the real-c conventions in the arXiv search results. For the supplied divisor choose a common denominator m and a single holomorphic generator g=product f_j^{m a_j}; c=1/m and R is smooth. Thus the exact cited convention is satisfied.

**Finding:** matched or explicitly accepted prerequisite; applicable; no critical error or gap.

### R2. Divisorial feasibility

**Referenced content:** lem:nonclosed-divisorial-removal: for any smooth real (1,1)-form beta, w in PSH(beta), and finitely many distinct prime divisors E_j, beta+ddc w-sum nu(w,E_j)[E_j]>=0; beta need not be closed. thm:lamari: PSH(X,theta) nonempty iff integral theta gamma^{n-1}>=0 for all Gauduchon gamma (used for n>=2).

**Definition and hypothesis check:** The manuscript's T=theta+ddc u is not presumed closed. Apply exactly the nonclosed removal lemma, then the smooth residual nonclosed Lamari theorem. For curves use the explicitly accepted Green criterion, not the (n-1)-root argument.

**Scope:** These exact book results and the curve criterion were explicitly accepted by the user; only their statements, definitions and application were checked.

**Finding:** matched or explicitly accepted prerequisite; applicable; no critical error or gap.

### R3. Residual volume, smooth equation, derivative and nef endpoint

**Referenced content:** D_mu(gamma)=integral (mu/gamma^n)^{1/n} gamma^n; lambda_mu(theta)=inf integral theta gamma^{n-1}/D_mu(gamma), V_mu=lambda_mu^n. The positive-cone dual formula identifies this scalar with the normalized smooth equation, attains the infimum, and supplies minimizing Gauduchon metrics. First variation is integral chi gamma_theta^{n-1}/D_mu(gamma_theta) for n>=2, integral chi for n=1. For nef theta, V_mu(theta)=lim_{epsilon downarrow0} c_{theta+epsilon h}(mu).

**Definition and hypothesis check:** The domain is smooth real backgrounds modulo smooth ddc, including nonclosed ones, with a fixed smooth strictly positive probability density mu. The positive cone means existence of a smooth positive representative, not positivity of the displayed initial representative. Nef means theta+epsilon h belongs to that cone for every epsilon>0. The curve denominator is 1. All supplied applications use these exact hypotheses.

**Scope:** Accepted audits 51/55; no re-audit of chapter or upstream smooth existence theorem.

**Finding:** matched or explicitly accepted prerequisite; applicable; no critical error or gap.

### R4. Residual equation: ordinary type and local products

**Referenced content:** Ordinary singularity equivalence is u<=v+C and v<=u+C'. Bounded nonclosed products are locally defined by sum_j binomial(k,j)(ddc p)^j wedge (theta-ddc q)^{k-j}, with p=u+q bounded psh. Extended products restrict bounded truncation products to sets where the potential is untruncated and discard the pole set.

**Definition and hypothesis check:** Two-sided bounded equivalence, rather than equality of Lelong numbers, multiplier ideals, or relative full mass, supplies the bounded w. No local potential for the arbitrary smooth beta_D is assumed. The signed expansion separates the smooth nonclosed part and makes each coefficient measure locally finite and noncharging by the permitted local BT input. Only this local finite-divisor use of the definitions is needed, not any unproved general singular theorem.

**Finding:** matched or explicitly accepted prerequisite; applicable; no critical error or gap.

### R5. Residual equation: scalar uniqueness including zero

**Referenced content:** thm:bounded-strict-domination: for bounded u,v in PSH(X,omega), omega a smooth positive Hermitian form, and 0<=q<1, if 1_{u<v} omega_u^n <= q 1_{u<v} omega_v^n, then u>=v.

**Definition and hypothesis check:** Set omega=Omega0, u=w-v0 and the comparison potential to v-v0 plus an arbitrary constant. A global ratio inequality implies the required sublevel inequality. Zero is explicitly permitted for q. Non-collapse of each bounded potential follows by comparing a zero-measure potential against a constant above its supremum; this is not PVP or a uniform positive lower mass.

**Scope:** User accepted bounded_comparison_01; no import of a stronger uniqueness or singular domination theorem.

**Finding:** matched or explicitly accepted prerequisite; applicable; no critical error or gap.

### R6. Hopf proposition

**Referenced content:** thm:hopf-unbounded gives smooth V_j with omega+ddc V_j>0 and integrals of their cubes tending to infinity on the quotient by z -> e^{-1}z. The normalized forms obey alpha^3=zeta^2=0, d alpha=0, ddc zeta=-alpha^2, alpha=pi^*omega_FS, integral alpha^2 zeta=2.

**Definition and hypothesis check:** All forms use ddc=i partial barpartial/(2 pi), already rescaled from the original external paper. The same fixed positive omega and the same smooth sequence are used. The proof scales potentials by delta and bounds matrices pointwise; it does not invoke invariance of raw mass.

**Scope:** User accepted hopf_counterexample_01; no re-audit of the Hopf construction or original paper.

**Finding:** matched or explicitly accepted prerequisite; applicable; no critical error or gap.


## Assumption audit and limits of the conclusions

- **Compactness and connectedness:** used for finite integrals, global bounds, the curve Green criterion, and a single additive normalization in smooth uniqueness.
- **Dimension one:** every Hermitian metric is an allowed test and \(D_\mu(\gamma)=1\). The threshold is \(\int_X\theta/\deg D\), residual volume is \(\int_X\theta-\deg D\), and the derivative in direction \(D\) is \(-\deg D\). Divisor atoms remain in the current and are absent from its non-pluripolar measure.
- **Divisor assumptions:** finiteness makes all prescribed currents finite. Effectivity gives nonnegative coefficients. Nonzero \(D\) gives positive threshold denominators and the strict derivative. At \(t=0\), \(D_t=0\) but its fixed direction \(D\) remains nonzero. Rationality is optional and used only in the analytic-singularity remark.
- **Kinds of positivity:** residual pseudoeffectivity suffices for feasibility and the volume definition; a smooth positive representative is required for the equation and exact derivative; the endpoint limit uses the stated nonclosed definition of nefness.
- **Attainment:** the coefficient threshold is attained by a positive current. No minimizing smooth Gauduchon metric at the boundary is required.
- **Mass and uniqueness:** the residual volume is the scalar for a fixed probability density. It does not give the mass of every bounded potential. The bounded-remainder conclusion fixes the scalar and does not prove equality of arbitrary bounded remainders.
- **Modifications:** no compatibility theorem is asserted. Pullback of a smooth positive volume form by a nontrivial modification can vanish along the exceptional locus, so the earlier strictly positive-density equation cannot be applied there without further work.
- **Dependencies:** neither closedness, a global local-potential representation for the background, BMP, PVP, nor an additional singular existence or uniqueness theorem is assumed.

## Final findings

**Critical errors:** none.

**Gaps:** none.

**Verdict:** correct under the stated assumptions and explicitly accepted prerequisites.

**Repair hints:** none required.

The machine-readable result is saved separately as verification.json. The run memory contains all sequential statement checks, reference checks, report records, and events; the failed_checks channel is empty because no proof issue was detected.

