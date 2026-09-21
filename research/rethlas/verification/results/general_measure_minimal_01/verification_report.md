# Verification report: general_measure_minimal_01

**Verdict: correct. Critical errors: 0. Gaps: 0.**

## Scope and audit basis

The submitted proof was checked in textual order against the supplied hypotheses and accepted internal inputs. The corresponding source text is [section_general_measure_minimal.tex](/Users/mingchen/Non-Kahler/book/author/section_general_measure_minimal.tex:1). It was read, not modified. This report contains all 74 deduction checks and 11 source checks. The accepted internal proofs were treated as inputs; their exact statements, definitions, uses and relevant dependencies were checked. Cegrell’s new external input was independently checked against the primary paper, including visual PDF inspection. ALS26 was checked for historical attribution only.

The carrier allows zero or nonzero finite positive non-pluripolar measures on compact connected complex X with smooth semipositive big theta. The equation theorem additionally requires mu(X)>0 and v_-(theta)>0. Theta need not be closed. The conclusion concerns the global envelope class E_env(X,theta,0). No bounded mass property or arbitrary prescribed-singularity conclusion is assumed.

## Summary

The complete supplied proof is correct under the explicitly accepted internal inputs. The audit checked 74 small deductions across 20 proof locations in textual order and matched 11 reference records, and found no critical errors or gaps. The bounded-carrier lemma needs no volume property. The equation reconstruction uses v_-(theta)>0 and does not require the bounded mass property.

Cegrell’s Theorem 6.3 was verified in the archived primary PDF at physical page 23, printed page 209, together with the local E_0 definition and standing n>=2 hypothesis at physical page 2, printed page 188. The local theorem supplies the claimed bounded-potential decomposition for compactly supported positive measures on bounded hyperconvex domains. Non-pluripolarity eliminates the positive pluripolar summand. Its local energy class is correctly distinguished from the global envelope class. The separate disk argument is valid: truncation locality gives ddc exp(a_M)>=1_{a>-M}exp(a)tau; bounded decreasing convergence and monotone convergence yield the limiting inequality; the polar pole set is tau-null, giving absolute continuity. [Cegrell primary PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6561-11511_2006_Article_BF02392899.pdf).

The local-to-global construction is justified for nonclosed theta. Strict analytic regularization supplies rho; the strict curvature margin absorbs each cutoff; the boundary collar makes the first maximum equal rho before gluing; semipositivity permits the final constant truncation while preserving agreement near K_i. Positive bounded mixed products give the local domination. The weighted series converges uniformly, its unused weight belongs to the zero potential, and its two-term convex decompositions give MA_theta(psi)>=t_i^n MA_theta(q_i). Countability and mu(Z)=0 then imply global absolute continuity. Finiteness of this one bounded-potential measure follows from local bounded theory and compactness, without any uniform mass property.

The internal definitions and hypotheses match exactly. Zero satisfies both parts of the required model condition, including P_{epsilon theta}(0)=0 for every epsilon>0. Constant competitors prove bounded-potential membership in global E_0 and translation invariance directly. The accepted lower-mass theorem therefore yields MA_theta^ext(w)(X)>=v_-(theta) by letting epsilon decrease to zero. No implication from E_0 membership to finite mass is used.

For positive exponent, each truncated density is bounded and nonzero, so the accepted bounded subsolution theorem applies. The order direction is correct: increasing densities produce decreasing solutions. Positive lower mass bounds their suprema below, ensuring a genuine L1 limit before fixed-measure continuity is invoked. All its hypotheses hold, with dominating measure exp(lambda sup_X u_1)mu. Dominated convergence gives total-variation convergence of the right sides and identifies the equation. Every competing solution has finite MA by its equation and bounded-above potential, so exponential order in both directions proves uniqueness.

For zero exponent, w_j/j-h=(j-1)(H-h)/j>=0 gives the correct comparison u_j<=w_j. Thus v_-(theta)/mu(X)<=c_j<=exp(H), ensuring a positive scalar limit. Normalized compactness supplies a genuine normalized L1 limit of v_j. Bounded truncation proves ddc exp(v_j/j)>=-exp(v_j/j)theta/j>=-Omega across poles, with the canonical exponential value zero there. The uniform normalized L1 bound implies ||1-exp(v_j/j)||_{L1(dV)}<=C/j. These functions meet every hypothesis of the accepted fixed-NPP integration lemma, yielding L1(mu) convergence and then total-variation convergence to c mu. Domination by exp(H)mu permits the second fixed-measure continuity application. The scalar corollary in both directions proves uniqueness of c, without claiming uniqueness of the normalized potential.

The external references were checked with arXiv theorem search first and primary-source web fallback. ALS26 Theorem 5.8 and Corollary 5.9 match the historical attribution in their semipositive big, positive-lower-volume context; neither is used as an existence input. [ALS primary paper](https://arxiv.org/abs/2511.02339v1). The checked internal dependencies introduce neither hidden bounded mass nor circular general existence. Arbitrary prescribed singularities remain outside the proved result. Full deduction and reference records are persisted for general_measure_minimal_01, with a readable companion report in results/general_measure_minimal_01/verification_report.md.

## Sequential deduction checks

Each check below passed. Locality, bounded mixed positivity, monotone convergence, canonical representatives, normalized quasi-psh compactness, convex composition and strict analytic regularization are used within the explicitly accepted standard-input scope.

### 1. Section introduction

1. **The section claims reconstruction from bounded subsolutions and dominated continuity, with ALS26 used only historically.** The only existence theorem invoked in the subsequent proof before the new limit is the accepted bounded subsolution theorem. ALS26 is not used to obtain a carrier, an unbounded solution, or compactness. Attribution is tracked in reference_checks.

### 2. lem:bounded-measure-carrier — local decomposition (n>=2)

1. **Use Cegrell Theorem 6.3 on a bounded hyperconvex domain for a compactly supported finite positive measure.** This is an external input to be matched to its local E_0 definition and standing dimension hypothesis in reference_checks; coordinate balls meet the domain requirement.

2. **Non-pluripolar tau eliminates the pluripolar summand.** For the positive decomposition tau=g(ddc v)^n+tau_s, one has 0<=tau_s<=tau. If tau_s is supported on a pluripolar set, non-pluripolarity gives tau_s(X)=0.

3. **Infer tau absolutely continuous with respect to (ddc v)^n.** The remaining summand has nonnegative integrable density g, giving precisely absolute continuity. No bound on g is claimed.

4. **Distinguish local E_0 and absorb ddc normalization.** Only boundedness and local psh positivity from local E_0 are used later. No local energy/zero-boundary property is identified with global envelope membership. Rescaling ddc by a positive constant rescales its n-th power and is absorbed in g.

**External verification resolved:** the deferred source match in the original sequential record was completed successfully by `external_ceg98_thm6_3`, detailed below. There is no unresolved reference or gap.

### 3. lem:bounded-measure-carrier — disk Green potential

1. **Take the negative Green potential a of finite compactly supported non-polar tau with ddc a=tau.** On a disk the Green kernel has locally integrable logarithmic singularities; finiteness and compact support make its integral a genuine subharmonic function, finite almost everywhere for area and with a<=0. This uses the standard linear Green construction, not a nonlinear existence theorem.

2. **Set v=e^a and truncate a_M=max(a,-M).** a_M is bounded subharmonic; e^{a_M} is bounded subharmonic by convex increasing composition, decreases to e^a, and remains in [0,1]. The limit is therefore bounded subharmonic and takes value zero at poles.

3. **ddc e^{a_M} >= e^{a_M} ddc a_M.** For bounded subharmonic functions this is the convex chain inequality; positive gradient term can be discarded. Local regularization and the bounded chain/BT convergence justify the measure-valued inequality, without assuming differentiability.

4. **On {a>-M}, the right side agrees with e^a tau.** Locality for the truncation on the strict level set yields 1_{a>-M} ddc a_M=1_{a>-M} tau. The set need not be Euclidean open; the accepted psh truncation/plurifine locality is the applicable formulation. Positivity gives the global inequality ddc e^{a_M} >= 1_{a>-M} e^a tau.

5. **Pass to the limit M->infinity.** The bounded decreasing exponentials converge in L1 locally, so their distributional Laplacians converge. Positive right-hand measures increase to 1_{a>-infinity} e^a tau. The pole set of the genuine subharmonic a is polar, and tau does not charge it.

6. **Conclude tau << ddc v.** ddc v >= e^a tau and e^a>0 tau-almost everywhere. If ddc v(A)=0, then integral_A e^a d tau=0 and tau(A)=0. Local E_0 membership of v is neither asserted nor needed.

### 4. lem:bounded-measure-carrier — strict barrier and local covering (lines 30–38)

1. **Obtain rho with analytic singularities and theta+ddc rho>=kappa omega.** This is exactly the accepted strict analytic regularization input for a smooth big background, including nonclosed theta; section_big_continuous_contact.tex lines 7–11 explicitly formulates it. It requires neither volume property.

2. **Use compact inner balls K_i and larger balls B_i relatively compact in X\Z.** The smooth manifold is second countable, and X\Z is open. Coordinate balls can be chosen with compact nested closures and inner balls covering X\Z. As rho is genuine, Z is a proper analytic, hence pluripolar, set.

3. **Apply the local assertion to mu_i=1_{K_i}mu on B_i.** Each restriction is finite, positive, non-pluripolar, and supported on a compact subset of a bounded hyperconvex coordinate ball. It may charge the boundary of K_i; local decomposition allows arbitrary compact supports. Countably many overlaps cause no difficulty because only absolute continuity is sought.

4. **Normalize each local bounded potential to 1<=v_i<=2 by a positive affine map.** Boundedness permits such a map. Adding a constant leaves ddc unchanged; positive scaling multiplies the n-th MA power by a strictly positive scalar and preserves absolute continuity. Zero restrictions may be discarded.

### 5. lem:bounded-measure-carrier — cutoff, collar maximum and bounded truncation (lines 39–44)

1. **Choose chi_i=0 near K_i and chi_i=-3 on a boundary collar.** K_i is compactly contained in B_i, so a smooth cutoff with these constant regions exists. Its derivatives have compact support; ddc chi_i>=-A_i omega for a finite A_i.

2. **Choose epsilon_i sufficiently small to retain the strict lower bound.** For epsilon_i A_i<=kappa/2, theta+ddc(rho+epsilon_i(v_i+chi_i))=(theta+ddc rho)+epsilon_i ddc chi_i+epsilon_i ddc v_i >=(kappa/2)omega+epsilon_i ddc v_i.

3. **Take the maximum with rho in B_i and extend by rho.** Both branches are theta-psh. The maximum preserves that exact current lower bound for a smooth nonclosed background (local convex maximum/freeze-and-limit argument). On the whole boundary collar v_i+chi_i<=2-3=-1, so the maximum equals rho there and glues with no boundary distribution.

4. **Take a second maximum with the constant -C_i.** Semipositivity makes the constant theta-psh. The result is globally bounded below by -C_i and above by a finite constant, since rho is bounded above on compact X and the local perturbation is bounded.

5. **Arrange agreement with rho+epsilon_i v_i near K_i.** In a neighborhood where chi_i=0, v_i>=1 forces the first maximum to take the perturbed branch. On a slightly smaller compact neighborhood rho has a finite lower bound, so sufficiently large C_i makes the last truncation inactive there. No continuity of v_i is needed.

### 6. lem:bounded-measure-carrier — local mixed domination (lines 44–48)

1. **MA_theta(q_i)>=(epsilon_i)^n(ddc v_i)^n near K_i.** There theta+ddc q_i=(theta+ddc rho)+epsilon_i ddc v_i. The first summand is smooth positive, the second a positive bounded local psh Hessian. Multilinear bounded BT expansion has nonnegative mixed terms, so it dominates its pure second-summand term. The smooth summand need not be closed; no Stokes or cohomological mass identity is used.

2. **Conclude mu_i << MA_theta(q_i) globally.** mu_i is supported in K_i. For any MA_theta(q_i)-null Borel set A, the displayed inequality makes (ddc v_i)^n(A intersect K_i)=0; local absolute continuity gives mu_i(A)=0.

### 7. lem:bounded-measure-carrier — countable uniform convex sum (lines 51–60)

1. **Translate q_i to be nonpositive and choose positive weights.** Translation changes neither theta-psh status nor MA. For an enumeration i>=1, t_i=2^(-i-1)/(1+||q_i||_infinity) provides both sum t_i<1 and sum t_i||q_i||_infinity<infinity; a finite family is handled by the same choice.

2. **psi=sum t_i q_i is bounded theta-psh.** The weighted sup norms make the series uniformly convergent. Each partial sum is a convex combination of its q_i and the constant zero with residual positive weight, hence theta-psh by theta>=0. Uniform limits preserve the canonical upper-semicontinuous representative and current inequality.

3. **For each fixed i write psi=t_i q_i+(1-t_i)w_i.** Define w_i=(sum_{k!=i}t_k q_k)/(1-t_i), with unused weight (1-sum t_k)/(1-t_i) on zero. These coefficients are nonnegative and sum to one. The remaining series is uniformly convergent; w_i is globally bounded theta-psh.

4. **MA_theta(psi)>=t_i^n MA_theta(q_i).** theta+ddc psi=t_i(theta+ddc q_i)+(1-t_i)(theta+ddc w_i). The bounded mixed-product expansion is positive termwise. This avoids any unproved continuity of an infinite product or any uniform bound for all q_i masses.

### 8. lem:bounded-measure-carrier — global absolute continuity and density (line 61)

1. **MA_theta(psi) is one finite non-pluripolar measure.** A single globally bounded theta-psh potential has locally finite BT products with finite total mass by a finite chart cover and local bounded estimates. Its MA does not charge pluripolar sets. This is individual finiteness, not the bounded mass property for all potentials.

2. **mu << MA_theta(psi).** The preceding domination gives mu_i << MA_theta(psi) for every retained i. If A is null for MA_theta(psi), then mu(A intersect K_i)=0 for each i, and countable covering gives mu(A\Z)=0. Non-pluripolarity gives mu(Z)=0. Discarded zero pieces remain null and need not themselves cover.

3. **Obtain nonnegative f in L1 with mu=f MA_theta(psi).** Both measures are finite positive Borel measures, so Radon–Nikodym applies; integral f dMA_theta(psi)=mu(X)<infinity.

4. **Handle mu=0 with psi=0 and f=0.** theta>=0 makes zero theta-psh; its smooth MA is finite and the identity is immediate. No positivity-of-mass claim is needed in this case.

### 9. thm:general-measure-minimal — reference zero and class definitions (line 78)

1. **Reference zero satisfies the required model condition.** The actual condition in chapter_envelopes.tex lines 471–475 is P_theta[phi]=phi and a genuine P_{epsilon theta}(phi) for some epsilon in (0,1). Zero itself is admissible under theta>=0, all competitors of P_theta[0] are <=0, and zero is among them, so P_theta[0]=0. Likewise P_{epsilon theta}(0)=0 for every epsilon>0. No equivalence with a volume-defined model condition is invoked.

2. **Every bounded theta-psh w belongs to the global E_0.** The definition is u preceq 0 and a theta-psh h satisfying h/b<=u for each b>=1. Bounded w is bounded above, and h=-bC works if w>=-C and C>=0. The constant is theta-psh. This checks every envelope quantifier directly and uses neither local Cegrell E_0 nor E_vol.

3. **Constant translations preserve E_0 and extended MA.** If h/b<=u, then (h+bA)/b<=u+A; reverse translation proves equivalence. Curvature and all truncation-defined extended products are unchanged by constants. This will justify normalization in the zero-exponent part.

### 10. thm:general-measure-minimal — eq:minimal-lower-mass (lines 78–82)

1. **Apply thm:relative-uniform-mass-lower with phi=0 for each epsilon in (0,1).** Its standing hypotheses are compact connected X, smooth semipositive big theta, the model condition, and genuine P_{epsilon theta}(phi). These all hold; the exact estimate is MA_theta^ext(w)(X)>=(1-epsilon)^n v_-(theta) for every w in E_phi (chapter_relative_finite_measures.tex lines 6–12, 98–112). It does not require finite mass.

2. **Let epsilon decrease to zero to obtain MA_theta^ext(w)(X)>=v_-(theta).** Reference zero meets the smaller-background condition for every epsilon, so the same fixed w satisfies all estimates. The lower bound tends to v_-(theta). This is a limit of numerical lower bounds, not a convergence assertion for potentials or MA measures.

3. **Identify the extra positive volume hypothesis.** The source's eq:relative-positive-lower-volume is exactly v_-(theta)>0 (lines 117–121), not the bounded mass property or a finite upper volume. Its use begins here for the noncollapse and finite-measure comparison arguments.

### 11. thm:general-measure-minimal — positive exponent: density truncation and bounded solutions (lines 84–87)

1. **Use the carrier to write mu=f nu with nu=MA_theta(psi).** The preceding lemma supplies a globally bounded theta-psh psi and nonnegative integrable f; nu is one finite non-pluripolar measure.

2. **Each f_j=min(f,j) is bounded and nonzero as a density measure.** mu(X)>0 means f is positive on a set of positive nu-measure; therefore integral min(f,j)dnu>0 for every integer j>=1. There is no required lower bound for f_j.

3. **Invoke thm:bounded-subsolution for each f_j and fixed lambda>0.** The exact source theorem, section_bounded_subsolution.tex lines 61–73, assumes theta semipositive big, bounded psi, nonnegative essentially bounded density, and positive measure mass. All hold. It explicitly imposes no bounded mass hypothesis and gives a bounded solution of precisely MA_theta(u_j)=e^{lambda u_j}f_j nu.

4. **Place u_j in E_0 and ensure finite MA before comparison.** Boundedness gives E_0 by seq 9 and individual finite MA by local bounded BT theory, agreeing with extended MA. Thus the finite-measure order corollary may be applied.

### 12. thm:general-measure-minimal — positive exponent: order and genuine noncollapse (lines 88–93)

1. **Increasing f_j forces decreasing u_j.** e^{-lambda u_j}MA(u_j)=f_j nu<=f_{j+1}nu=e^{-lambda u_{j+1}}MA(u_{j+1}). The exact corollary's direction is weighted MA(u)<=weighted MA(v) implies u>=v. It yields u_j>=u_{j+1}; all first potentials have finite MA and both are in E_0.

2. **Obtain a common upper bound.** The canonical pointwise comparison gives u_j<=u_1, and bounded u_1 has finite supremum.

3. **Obtain a common lower bound for sup_X u_j.** The lower mass estimate and equation give 0<v_-(theta)<=integral e^{lambda u_j} f_j dnu<=e^{lambda sup u_j}mu(X), hence sup u_j>=(1/lambda)log(v_-(theta)/mu(X)). Only finite mu and positive lower mass enter.

4. **The decreasing limit is genuine and convergence is L1.** For decreasing upper-semicontinuous functions on compact X with suprema bounded below, the nested nonempty closed superlevel sets (at any smaller common level) have nonempty intersection, excluding an identically -infinity limit. Standard decreasing qpsh convergence on connected X then gives a genuine canonical theta-psh limit and L1 convergence. No class closure is presumed at this point.

### 13. thm:general-measure-minimal — positive exponent: fixed domination and continuity (lines 94–97)

1. **MA_theta(u_j)<=e^{lambda sup u_1}mu.** Use u_j<=u_1 and f_j<=f in the equation; the multiplier is a single finite constant independent of j. Since mu is finite non-pluripolar, so is this dominating measure.

2. **Apply thm:relative-fixed-measure-continuity at phi=0.** The exact source requires: smooth semipositive big theta and compact connected X; model phi with a genuine smaller-background envelope; v_-(theta)>0; u_j in E_phi; L1 convergence to a genuine theta-psh u; and domination by a single fixed finite non-pluripolar measure. Seq 9–12 and the preceding inequality establish every hypothesis before invocation.

3. **Conclude u in E_0, capacity convergence, and weak extended MA convergence.** These are precisely the theorem's conclusions (section_dominated_relative_compactness.tex lines 66–72). The proof uses only the class and weak-measure conclusions. Neither E_0 closedness under arbitrary L1 limits nor undominated unbounded MA continuity is presumed.

### 14. thm:general-measure-minimal — positive exponent: total variation and uniqueness (line 97)

1. **e^{lambda u_j}f_j converges nu-almost everywhere to e^{lambda u}f.** The decreasing canonical potentials converge pointwise to u. The integrable RN derivative f is finite nu-almost everywhere, and min(f,j)->f there. At poles e^{lambda u}=0 gives the same limit; nu as a bounded MA measure is non-pluripolar.

2. **Apply dominated convergence in L1(nu).** 0<=e^{lambda u_j}f_j<=e^{lambda sup u_1}f and the right side is nu-integrable. This yields TV convergence of the density measures, with total variation bounded by the corresponding L1 difference.

3. **Identify MA_theta^ext(u)=e^{lambda u}mu.** The TV limit and the weak MA limit must agree as finite Borel measures. mu=f nu supplies the asserted RHS.

4. **Prove uniqueness among all E_0 solutions.** Any genuine theta-psh solution is bounded above on compact X, so its equation makes its MA finite. The weighted measures of any pair both equal mu off their pole sets; mu and the extended MAs vanish on those pluripolar sets. Apply the finite exponential-order corollary in both directions, giving equality of canonical potentials.

### 15. thm:general-measure-minimal — zero exponent: bounded comparison potential (lines 99–110)

1. **For each j use the proven lambda=1/j solution u_j in E_0.** This depends only on the completed positive-exponent argument, not on the zero-exponent target. These unbounded solutions have finite MA from their equations and bounded-above potentials.

2. **Construct bounded h with MA(h)=e^h min(f,1)nu.** The density min(f,1) is bounded nonnegative and has positive integral, and psi remains the bounded carrier. Thus the accepted bounded subsolution theorem applies with exponent one. H=||h||_infinity is finite and nonnegative.

3. **w_j=h+(j-1)H satisfies w_j/j>=h.** The exact difference is (w_j/j)-h=(j-1)(H-h)/j>=0 since h<=H. Translation preserves its MA, boundedness and E_0 membership.

4. **Establish the weighted measure inequality.** MA(w_j)=MA(h); hence e^{-w_j/j}MA(w_j)<=e^{-h}MA(h)=min(f,1)nu<=f nu=mu. The equation of u_j gives mu=e^{-u_j/j}MA^ext(u_j) off its pole set, and mu gives that set zero mass.

5. **Use order to infer u_j<=w_j.** Apply cor:relative-finite-exponential-order with its first potential w_j (in E_0 and finite MA), its second potential u_j (theta-psh, bounded above, hence preceq0), and exponent 1/j. The source's inequality implies w_j>=u_j, exactly the claimed direction.

### 16. thm:general-measure-minimal — zero exponent: normalization and nonzero scalar limit (lines 111–120)

1. **Set M_j=sup u_j, v_j=u_j-M_j, c_j=e^{M_j/j}.** The genuine u_j has finite supremum; normalization gives sup v_j=0. E_0 and MA are invariant under these constant translations. The equation becomes MA^ext(v_j)=c_j e^{v_j/j}mu.

2. **0<c_j<=e^H.** u_j<=w_j gives M_j<=sup h+(j-1)H<=jH. Exponentiation gives the stated bound; c_j is positive by its definition.

3. **c_j>=v_-(theta)/mu(X)>0.** The lower mass bound applies to v_j in E_0. Since v_j<=0, one has e^{v_j/j}<=1, including at poles with value zero, so v_-(theta)<=c_j integral e^{v_j/j}dmu<=c_j mu(X). No upper mass property enters.

4. **Extract v_j->v in L1 with v genuine and sup v=0, simultaneously c_j->c>0.** Normalized theta-psh compactness on compact connected X supplies genuine normalized subsequential limits and uniform smooth-volume L1 bounds. The scalars lie in the compact positive interval [v_-/mu(X),e^H], so a common further subsequence converges to c in this interval. Denominators retain the original indices tending to infinity.

### 17. thm:general-measure-minimal — zero exponent: chain inequality across poles (lines 122–126)

1. **The normalized bound implies ||v_j/j||_{L1(dV)}->0.** Normalized compactness supplies ||v_j||_{L1(dV)}<=C uniformly. Dividing by original j tending to infinity gives convergence to zero. No integrability of v_j against mu is asserted or needed.

2. **Define a_j=e^{v_j/j} in [0,1], with value zero at poles.** v_j<=0, so the range follows. Since v_j is canonical upper semicontinuous, at a pole its values in neighborhoods tend uniformly below each finite negative level; composition extended by zero is the canonical upper-semicontinuous representative.

3. **Justify ddc a_j>=-(a_j/j)theta across poles.** For fixed j truncate b_{j,M}=max(v_j,-M). Constants are theta-psh under theta>=0, so b_{j,M} is bounded theta-psh and <=0. The bounded convex chain rule gives ddc exp(b_{j,M}/j)>=(1/j)exp(b_{j,M}/j)ddc b_{j,M}>=-(1/j)exp(b_{j,M}/j)theta. The bounded exponentials decrease to a_j in L1, including at poles. Passing to distributional limits in both sides gives the claimed exact inequality.

4. **Obtain one common smooth lower curvature bound.** Choose a Hermitian Omega>=theta using compactness. Because theta>=0, 0<=a_j<=1 and j>=1, one has -(a_j/j)theta>=-Omega. Therefore all a_j and the limit function 1 are uniformly bounded quasi-psh functions with the same smooth lower curvature bound.

5. **a_j->1 in smooth-volume L1.** For each finite v_j<=0, the elementary inequality 0<=1-e^{v_j/j}<=-v_j/j gives ||1-a_j||_{L1(dV)}<=C/j. Pole sets have smooth-volume measure zero, so the almost-everywhere inequality suffices.

### 18. thm:general-measure-minimal — zero exponent: fixed NPP integration and TV limit (lines 126–132)

1. **Apply lem:fixed-npp-integrals to a_j and 1.** The actual lemma requires one fixed finite non-pluripolar measure, uniform boundedness of the quasi-psh functions and their limit, a common smooth lower curvature bound, and smooth-volume L1 convergence. mu is fixed and seq 17 establishes every function hypothesis. Hence ||a_j-1||_{L1(mu)}->0. Smooth-volume almost-everywhere convergence alone was not used to claim mu convergence.

2. **Translate the equations and prove TV convergence to c mu.** MA^ext(v_j)=MA^ext(u_j)=c_j a_j mu. The estimate ||c_j a_j mu-c mu||_TV<=e^H||a_j-1||_{L1(mu)}+|c_j-c|mu(X) tends to zero. This works even if the negative parts of v_j are not mu-integrable.

3. **Establish uniform fixed domination.** 0<=c_j a_j<=e^H yields MA^ext(v_j)<=e^H mu, a single finite NPP measure independent of j. The bound comes from the equation and the constructed bounded comparison, not from an upper-volume hypothesis.

### 19. thm:general-measure-minimal — zero exponent: continuity and scalar uniqueness (line 133)

1. **Apply thm:relative-fixed-measure-continuity to v_j.** All v_j belong to E_0 by constant translation; their extracted L1 limit v is already genuine theta-psh; phi=0 satisfies the exact model condition; v_-(theta)>0 is assumed; and seq 18 gives the required single finite NPP dominating measure. The theorem yields v in E_0, capacity convergence, and weak MA convergence.

2. **Identify the limiting equation.** The weak MA limit must equal the already established TV limit c mu. The normalization sup v=0 was preserved by normalized compactness, and c>=v_-/mu(X)>0.

3. **Prove uniqueness of the positive scalar.** For two finite-measure solutions MA(v)=c mu and MA(w)=d mu with c,d>0, the scalar corollary applied to MA(v)=(c/d)MA(w) gives c/d>=1; reversed roles give d/c>=1. Both first potentials are in E_0 with finite MA. Thus c=d; no uniqueness of normalized potentials is inferred.

### 20. Closing scope paragraph (line 136)

1. **The two limits use the advertised distinct compactness mechanisms.** For lambda>0, monotonicity plus lower mass establishes genuine L1 convergence and fixed domination identifies MA. For lambda down to zero, normalized compactness gives L1 potentials while bounded exponential weights and fixed NPP integration identify the RHS in TV; the same fixed-domination theorem identifies MA.

2. **The result is confined to the minimal global envelope class.** The carrier is bounded in the same theta and E_0 membership of limits comes from continuity at reference zero. No carrier of a prescribed singular type is constructed, and no arbitrary prescribed-reference existence theorem is invoked.

3. **Audit all hypotheses and the absence of BMP.** Bigness supplies the strict analytic barrier and is required by accepted bounded existence/relative theorems; semipositivity supplies constants, convex residual weight and truncation admissibility; compactness supplies finite chart estimates and normalized compactness; connectedness excludes componentwise collapse; NPP discards analytic/polar sets and permits fixed-measure integration/continuity; finiteness supplies RN integrability, domination, DCT and order; mu(X)>0 ensures nonzero bounded truncations; v_->0 supplies uniform lower mass and relative comparison/continuity. No hypothesis is suspiciously unused. There is no use of v_+<infinity, fixed cohomological mass, or the implication E_0=>finite MA.

## Reference checks

The three external references were searched using the full referenced statements through `search_arxiv_theorems` first. No exact matches were returned; built-in web search and the archived primary PDFs then supplied the exact matches. The remaining eight records check the accepted internal inputs and definitions directly in the source files.

### R1. external_ceg98_thm6_3

**Use:** Lemma bounded-measure-carrier, first paragraph

**Source:** [Ceg98.pdf](/Users/mingchen/Non-Kahler/research/sources/Ceg98.pdf), physical 23 / printed 209. Definition: physical 2 / printed 188.

**Primary online source:** [paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6561-11511_2006_Article_BF02392899.pdf).

**Referenced statement:** Cegrell, Pluricomplex energy (1998), Theorem 6.3: Let tau be a positive compactly supported measure on a bounded hyperconvex domain Omega in C^n, n>=2. Then tau = g(dd^c v)^n + tau_s, where v belongs to the local class E_0 of bounded negative plurisubharmonic functions with zero boundary values and finite total Monge-Ampere mass, 0 <= g in L^1((dd^c v)^n), and tau_s is carried by a pluripolar set.

**Context and definitions:** Section2 defines local E0 as negative bounded psh functions with limit0 at every boundary point and finite total Bedford–Taylor mass. This is different from the book's global envelope class E_env(X,theta,0). There is no energy-integrability hypothesis on tau in Theorem6.3; the present finite compact restrictions satisfy its measure assumptions. Balls are bounded connected hyperconvex domains.

**Formula comparison:** The proof's local E0 definition agrees exactly with the source. No global-envelope class conclusion is imported from local E0. The source's positive ddc normalization rescales its nth power by a positive constant, absorbed into the density.

**arXiv-first check:** Full referenced statement queried first via search_arxiv_theorems. Five returned statements concern dbar equations, pluriharmonic currents, and tangent cones; none matches Cegrell Theorem6.3.

**Primary-source fallback:** The same full statement was then searched with Codex web. Exact primary archive PDF was returned. Archived PDF pages were rendered locally and visually inspected because web screenshot could not parse its content type.

**Application checks:**

- tau_s<=tau, so if tau vanishes on pluripolar sets and tau_s is supported on such a set, tau_s=0.
- Hence tau is absolutely continuous with respect to (ddc v)^n; only this is used downstream.
- Cegrell applies only to n>=2; the submitted proof supplies a separate n=1 Green-potential argument, outside this citation.
- No closed global theta or upper/lower global volume property enters this local theorem. Its local existence ingredients are not the global target theorem.

**Result:** verified; no critical error or gap.

### R2. external_als26_thm5_8_attribution

**Use:** Section introduction: historical attribution to ALS26 Theorem5.8

**Source:** [ALS26.pdf](/Users/mingchen/Non-Kahler/research/sources/ALS26.pdf), printed/physical28, continuing29.

**Primary online source:** [paper](https://arxiv.org/pdf/2511.02339v1).

**Referenced statement:** ALS26, Theorem 5.8: Fix lambda > 0 and let mu be a positive Radon measure vanishing on pluripolar sets. Then there is a unique function u in E(X,theta,varphi) solving (theta+dd^c u)^n=e^(lambda u) mu. Moreover, integral_X theta_u^n >= v_{-,varphi}(theta). Standing hypothesis v_-(theta)>0.

**Context and definitions:** Throughout source, X is compact Hermitian and theta is smooth semipositive big. The reference varphi is a theta-model potential: P_theta[varphi]=varphi and P_{epsilon theta}(varphi) is genuine for some epsilon in(0,1). Definition3.2 uses u more singular than varphi and P_theta(bu-(b-1)varphi) genuine for every b>=1; model0 is explicitly valid. No bounded-mass property is in this statement or its standing assumptions.

**Formula comparison:** For varphi=0, source class is exactly theta-psh u with genuine P_theta(bu) for all b>=1. The book's class uses competitors h with b^(-1)h+(1-b^(-1))*0<=u, equivalently h<=bu; therefore the definitions agree at reference0, including poles. This is unrelated to Cegrell's bounded local E0.

**arXiv-first check:** Full referenced statement queried first via search_arxiv_theorems. First attempt encountered an approval-review timeout, retried once successfully. Returned older ALS24 theorem4.2 and results in closed Kahler/local contexts; none was exact ALS26 Theorem5.8.

**Primary-source fallback:** Codex web search used the same full referenced statement. It returned the paper text, and the exact primary arXiv2511.02339v1 PDF was opened; archived source agrees.

**Application checks:**

- The submitted proof cites this result solely as historical attribution of its minimal-reference conclusion.
- No solution, carrier, convergence assertion or class membership is imported from Theorem5.8 in the reconstruction.
- The source's broader prescribed-reference scope is not asserted as newly reconstructed.
- The submitted theorem explicitly assumes mu(X)>0; finite NPP measure on compact X is a Radon measure under the usual Borel-measure convention.

**Result:** verified_attribution_only; no critical error or gap.

### R3. external_als26_cor5_9_attribution

**Use:** Section introduction: historical attribution to ALS26 Corollary5.9

**Source:** [ALS26.pdf](/Users/mingchen/Non-Kahler/research/sources/ALS26.pdf), printed/physical29, proof continuing30.

**Primary online source:** [paper](https://arxiv.org/pdf/2511.02339v1).

**Referenced statement:** ALS26, Corollary 5.9: Let mu be a positive Radon measure vanishing on pluripolar sets. Then there is a unique c>0 and a function u in E(X,theta,varphi) such that integral_X theta_u^n >= v_{-,varphi}(theta) and (theta+dd^c u)^n=c mu. Standing hypothesis v_-(theta)>0.

**Context and definitions:** Same smooth semipositive big theta and admissible model-reference hypotheses as Theorem5.8. At varphi=0 the source's stretched-envelope class equals the book's global E0. The uniqueness phrase attaches to c, not to u, matching the submitted theorem's explicit refusal to assert normalized-potential uniqueness.

**arXiv-first check:** Full referenced statement queried first via search_arxiv_theorems. Results include Kahler relative energy existence, local Cegrell class equations, and older ALS24 positive-exponent theorem4.2; none matches exact Corollary5.9.

**Primary-source fallback:** Codex web search used the same full referenced statement; exact paper was identified and primary arXiv2511.02339v1 PDF opened and compared against local archive.

**Application checks:**

- Subtracting sup_Xu does not change the Monge–Ampere measure or membership in the envelope class, so the submitted normalization is compatible with the attributed result.
- The submitted zero-exponent proof obtains its sequence using its own positive-exponent reconstruction and its scalar using its own limiting estimates.
- The external corollary is never used as an existence, scalar-positivity, scalar-uniqueness, or convergence input.
- No historical novelty is claimed and arbitrary prescribed singularity is explicitly left outside this reconstruction.

**Result:** verified_attribution_only; no critical error or gap.

### R4. internal_strict_analytic_barrier

**Use:** lem:bounded-measure-carrier — lines 30–34

**Source:** [section_big_continuous_contact.tex](/Users/mingchen/Non-Kahler/book/author/section_big_continuous_contact.tex:7) (lines 7–11).

**Referenced statement:** A smooth big real (1,1)-background admits a genuine quasi-psh rho with analytic singularities, smooth off its analytic pole set Z, and theta+ddc rho>=kappa omega for some kappa>0.

**Context and definitions:** Smooth theta is not assumed closed or semipositive for this input. Bigness and accepted strict analytic regularization give the strict barrier; the application additionally has theta>=0.

**Application checks:**

- Strict margin absorbs epsilon_i ddc chi_i on B_i.
- rho is smooth and bounded below on neighborhoods of K_i.
- Analytic pole set is pluripolar and mu-null.

**Result:** matched_and_applicable; no critical error or gap.

### R5. internal_global_class_model

**Use:** thm:general-measure-minimal — line 78 and all class uses

**Source:** [chapter_envelopes.tex](/Users/mingchen/Non-Kahler/book/author/chapter_envelopes.tex:352) (lines 352–387, 453–475).

**Referenced statement:** E_env(X,theta,phi) consists of u preceq phi such that for every b>=1 there is h in PSH(X,theta) with h/b+(1-1/b)phi<=u. The ALS model condition is P_theta[phi]=phi and P_{epsilon theta}(phi) genuine for some epsilon in (0,1).

**Context and definitions:** This is a convex-competitor definition, with no total-mass finiteness requirement. It is distinct from the local E_0 of Cegrell and from E_vol, whose definition is explicitly restricted to bounded mass.

**Application checks:**

- phi=0 satisfies both required model conditions by the zero competitor.
- Every bounded theta-psh potential satisfies each stretched inequality with a sufficiently negative constant.
- Translation preserves class membership by h->h+bA.
- No full-mass-volume equivalence requiring BMP is invoked.

**Result:** matched_and_applicable; no critical error or gap.

### R6. internal_bounded_subsolution

**Use:** thm:general-measure-minimal — lines 84–87 and 99–103

**Source:** [section_bounded_subsolution.tex](/Users/mingchen/Non-Kahler/book/author/section_bounded_subsolution.tex:61) (lines 61–73).

**Referenced statement:** For semipositive big theta, bounded theta-psh psi, nonnegative f in L-infinity(MA_theta(psi)) with integral f dMA_theta(psi)>0, and every lambda>0, there is a unique bounded theta-psh u satisfying MA_theta(u)=e^{lambda u} f MA_theta(psi). No bounded mass hypothesis is required.

**Context and definitions:** The source requires an essentially bounded density with respect to one bounded reference measure, not a smooth-volume density. The theorem and its prior independent audit are accepted inputs; this run checks its exact statement and instantiations.

**Application checks:**

- f_j=min(f,j) has positive integral, nonnegative bounded density, and the same bounded carrier psi.
- h uses min(f,1) with exponent one and the same reference.
- No unbounded density is supplied directly to the bounded theorem.

**Dependency check:** The inspected accepted source does not invoke thm:general-measure-minimal or ALS26 Theorem 5.8/Corollary 5.9 as an existence input.

**Result:** matched_and_applicable; no critical error or gap.

### R7. internal_lower_mass

**Use:** thm:general-measure-minimal — eq:minimal-lower-mass and its applications

**Source:** [chapter_relative_finite_measures.tex](/Users/mingchen/Non-Kahler/book/author/chapter_relative_finite_measures.tex:6) (lines 6–12, 98–112, 117–121).

**Referenced statement:** Under compact connected X, smooth semipositive big theta, the ALS model condition and genuine P_{epsilon theta}(phi), every w in E_phi has MA_theta^ext(w)(X)>=(1-epsilon)^n v_-(theta), and individually positive mass. The theorem does not assert finiteness.

**Context and definitions:** The source's subsequent PVP hypothesis is exactly v_-(theta)>0. Its v_- is the infimum of MA masses over all bounded theta-psh potentials (chapter_prescribed_equations.tex lines 166–171), without assuming v_+ finite.

**Application checks:**

- For phi=0 every epsilon in (0,1) is available, so sending epsilon to zero is valid.
- Positive-exponent approximants acquire a lower bound on their suprema from this mass bound and their equation.
- Zero-exponent scalars acquire a common strictly positive lower bound.
- No inference of finite mass from class membership is made.

**Result:** matched_and_applicable; no critical error or gap.

### R8. internal_exponential_order_scalar

**Use:** thm:general-measure-minimal — lines 88, 97, 105–110, 133

**Source:** [chapter_relative_finite_measures.tex](/Users/mingchen/Non-Kahler/book/author/chapter_relative_finite_measures.tex:123) (lines 123–129, 158–170).

**Referenced statement:** Under positive lower volume and standing model hypotheses, if u in E_phi has finite MA and v is theta-psh with v preceq phi, then e^{-lambda u}MA(u)<=e^{-lambda v}MA(v) implies u>=v. Also MA(u)<=c MA(v) for a finite c>=0 implies c>=1.

**Context and definitions:** Finiteness is required for the first potential's extended measure, not for every E_phi member. Exponential weights are canceled off poles; the relevant NPP measures ignore poles.

**Application checks:**

- f_j<=f_{j+1} gives u_j>=u_{j+1}.
- The bounded w_j is the first potential for the zero-exponent comparison, giving w_j>=u_j.
- Any positive-exponent solution has finite MA because its potential is bounded above and mu is finite.
- Comparing c mu and d mu both ways gives c/d>=1 and d/c>=1, hence c=d only.

**Result:** matched_and_applicable; no critical error or gap.

### R9. internal_fixed_measure_continuity

**Use:** thm:general-measure-minimal — lines 97 and 133

**Source:** [section_dominated_relative_compactness.tex](/Users/mingchen/Non-Kahler/book/author/section_dominated_relative_compactness.tex:66) (lines 66–100).

**Referenced statement:** Under v_-(theta)>0 and standing compact connected semipositive big/model hypotheses, u_j in E_phi converging in L1 to a genuine theta-psh u, with MA_theta^ext(u_j)<=nu for one fixed finite NPP measure, satisfy u in E_phi, capacity convergence, and weak MA convergence to MA_theta^ext(u)<=nu.

**Context and definitions:** Genuine L1 convergence is a hypothesis, not a conclusion rescuing a collapsed sequence. The source explicitly does not use v_+(theta)<infinity. The prior reconstructed proof is an accepted input.

**Application checks:**

- First invocation: bounded u_j in E_0; monotone genuine L1 limit established first; domination by exp(lambda sup u_1)mu.
- Second invocation: normalized translates v_j in E_0; normalized compactness yields genuine L1 limit first; domination by exp(H)mu.
- Reference zero satisfies the full standing model condition in both calls.

**Dependency check:** Operative source proof uses lower-mass envelopes, finite-measure domination and raw-tail continuity, not general existence.

**Result:** matched_and_applicable; no critical error or gap.

### R10. internal_fixed_npp_integration

**Use:** thm:general-measure-minimal — lines 122–126

**Source:** [section_relative_compactness.tex](/Users/mingchen/Non-Kahler/book/author/section_relative_compactness.tex:8) (lines 8–22).

**Referenced statement:** If uniformly bounded quasi-psh a_j,a have a common smooth lower curvature bound and converge in smooth-volume L1 on X, then integral |a_j-a|dnu tends to zero for each fixed finite NPP measure nu.

**Context and definitions:** This is convergence against a fixed measure; it neither concerns moving measures nor allows dropping uniform boundedness or the common curvature bound. The user accepts its prior proof.

**Application checks:**

- a_j=exp(v_j/j) and a=1 are canonical and uniformly in [0,1].
- Bounded truncation proves ddc a_j>=-(a_j/j)theta>=-Omega globally across poles.
- Uniform normalized L1 bound gives ||a_j-1||L1(dV)<=C/j.
- nu is the same fixed finite NPP mu, yielding the exact L1(mu) conclusion needed for TV convergence.

**Result:** matched_and_applicable; no critical error or gap.

### R11. internal_normalized_compactness

**Use:** thm:general-measure-minimal — lines 93, 120 and 122

**Source:** [chapter_compactness.tex](/Users/mingchen/Non-Kahler/book/author/chapter_compactness.tex:10) (lines 10–43).

**Referenced statement:** For a fixed smooth real background on compact connected X, the normalized theta-psh family sup_X u=0 is compact in L1 and has a uniform L1 bound. A decreasing sequence with bounded L1 norms has a genuine theta-psh limit and converges in L1.

**Context and definitions:** No MA mass bound is assumed. Connectedness prevents uncontrolled collapse on another component, and canonical representatives preserve normalization.

**Application checks:**

- Positive-exponent sup bounds combined with normalized L1 control exclude decreasing collapse.
- Zero-exponent normalized v_j have a genuine normalized L1 subsequential limit.
- The same uniform L1 bound controls v_j/j and then 1-exp(v_j/j).

**Result:** matched_and_applicable; no critical error or gap.

## Complete findings and strict verdict

- Critical errors: none.
- Gaps: none.
- Failed mathematical checks: none.
- Verdict: **correct**.
- Repair hints: empty, as required by the zero-error/zero-gap rule.

The source definitions do not conflate bounded local Cegrell energy with global stretched-envelope membership, or envelope membership with finite total mass. All mass upper bounds used in the limiting arguments come from their equations and one fixed finite measure. No general existence result supplies a missing step.

## Persistence and reproducibility

The run’s MCP memory contains `statement_checks` (20 ordered records with 74 deductions), `reference_checks` (11 records), `failed_checks` (empty), `events`, and `verification_reports`. Source-search no-matches and recovered tool timeouts are recorded as operational events/reference evidence, not mathematical failures. The final contract is written by `write_verification_output` to `results/general_measure_minimal_01/verification.json`. This readable report is persisted through MCP in `verification_reports` and exported verbatim to `results/general_measure_minimal_01/verification_report.md`. No book file, source paper, or prior result was edited.
