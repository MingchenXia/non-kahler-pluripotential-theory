# Verification report: analytic_density_example_01

**Verdict: correct within the requested scope.** No critical errors or substantive gaps were found.

This audit covers every assertion in sections 7 and 8 of the supplied manuscript, *Uniqueness Criteria for Hermitian Monge–Ampère Equations*: the prescribed analytic-density counterexample, its projective and product extensions, sharpness sublevel and inverse-power claims, the component remark, normalization constants, envelope definitions, and all ALS/BGL applications. The mathematical source was read in textual order. The earlier definitions and operator convention were used only to interpret notation; the positive uniqueness theorems in sections 1–6 were neither assumed nor audited. Section 9 and novelty certification are outside this run.

The manuscript and book were not edited. The analysis below recomputes this prescribed density directly and does not use any prior NUMA verification as evidence. An independent construction audit and two independent primary-reference audits corroborated the findings.

| Audit component | Result |
| --- | --- |
| Sequential deductions | 52 checks in 8 textual-order records; all pass |
| External applications | 4 applications from 2 primary papers; all match and apply |
| Critical errors | 0 |
| Substantive gaps | 0 |

## Sequential mathematical audit

The following numbering follows the manuscript, including the final remark of section 7 and the final distinctions of section 8. Each item records the inference and why its required hypotheses hold.

### Section 7, Theorem analytic-example, rank-one frame and radial identities

**1. Global t and open block coordinates.** t is invariant under common complex scaling. On Z0,W0 nonzero choose ζ=Z1/Z0, η=W1/W0, λ=W0/Z0; r=log(1+|ζ|²)-log(1+|η|²)-log|λ|². λ≠0.

**2. P and Q descend and have independent rank-one directions.** Changes of holomorphic lift add log|g|², whose dd^c is zero. P=(i/2π)dζ∧dζbar/(1+|ζ|²)² and Q=(i/2π)dη∧dηbar/(1+|η|²)².

**3. R is independent rank one.** R=dr∧d^c r=(i/2π)∂r∧bar∂r and ∂r has nonzero coefficient −1/λ on dλ. Thus dζ,dη,∂r form a coframe.

**4. Squares, positivity and top wedge.** P²=Q²=R²=0; PQR>0. Diagonal positivity is equivalent to positivity of its three coefficients, and (xP+yQ+zR)^3=6xyzPQR.

**5. Radial Hessian.** dd^c r=P−Q and the chain rule gives dd^c G=G'(P−Q)+G''R with the stated convention.

**6. Fubini–Study normalization.** Write log(|Z|²+|W|²)=log|W|²+log(1+e^r). Its Hessian is σP+(1−σ)Q+σ'R. Since σ'=σ(1−σ), its cube is 6(σ')²PQR.

**7. Exterior derivative.** dP=dQ=0, dR=−dr∧(P−Q); differentiating xP+yQ+zR gives dr∧((x'−z)P+(y'+z)Q).

**Local result:** pass; no critical errors or substantive gaps.

### Section 7, Prescribing the determinant

**8. Divided differences.** The integral definitions give σ(r)−a=(r+1)k_− and σ(r)−b=(r−1)k_+. Each k is positive and smooth on all finite r; H_*=k_−k_+σ'>0. Therefore d_*=(1−r²)²H_*² including both endpoints.

**9. Parity.** a+b=1 and σ(−r)=1−σ(r) imply d_* even. The positive quotient root H_* is even off ±1 and hence everywhere by continuity.

**10. Flat bump and derivative.** Every derivative of exp(−1/(1−r²)) is an exponential times a rational power expression on the band and tends to zero at both endpoints. Thus the extension by zero is C∞ and q=−2rp/(1−r²)² inside.

**11. First radicand.** q²+2H_*²>0 at every finite r, so z_b is smooth, positive, even and z_b>|q|.

**12. Second radicand.** r²+4p²+2z_b(1−r²)² is positive: if r≠0 the first term is positive; at r=0 both p and z_b are positive. Thus S_* is one globally smooth positive even function.

**13. Baseline coefficients.** x_b−y_b=−r, x_by_b=(S_*²−r²)/4=p²+(z_b/2)(1−r²)². S_*≥|r|, with equality exactly at ±1, yielding nonnegative coefficients and endpoint pairs (1,0),(0,1).

**14. Band positivity.** S_*²−(2p+|r|)²=2z_b(1−r²)²−4p|r|=2(1−r²)²(z_b−|q|)>0. Hence min(x_b,y_b)>p and both perturbed triples are positive.

**15. Cancellation identity.** Let L=1−r². D=x_by_b−p²=z_b L²/2 and E=p(x_b−y_b)=−rp. Thus qD=z_bE on |r|<1, and by continuity/vanishing outside everywhere. The products are (D+E)(z_b−q) and (D−E)(z_b+q), each D(z_b²−q²)/z_b=L²H_*²=d_*.

**16. Endpoints and exterior baseline determinant.** For |r|≥1, p=q=0, so x_by_bz_b=d_*. At ±1 precisely one x/y entry vanishes and the other equals 1 while z_b=√2 H_*>0; both perturbed forms have rank 2.

**Local result:** pass; no critical errors or substantive gaps.

### Section 7, The global patch

**17. Cutoff and overlapping definitions.** A smooth even cutoff with plateaux at |r|≤3/2 and |r|≥2 exists. On |r|>5/4 the density is positive, so κ=f_*(σ(r))^(1/3) is smooth and positive. Convex combinations give x,y>0 and z=d_*/(xy)>0. On 5/4<|r|<3/2, η=1 and p=q=0, so z=z_b; the definitions agree as smooth functions on an open overlap.

**18. Exact tail form and projective extension.** On |r|≥2, x=κσ, y=κ(1−σ), and z=κσ', because d_*=κ³(σ')² and xy=κ²σ'. Hence ω0=κΩ. Near t=0,1, f_*(t)>0 and κ is smooth, so this extends positively across both omitted projective lines.

**19. Global baseline ranks.** The inner formula is semipositive and has rank 2 exactly at r=±1. The outer formula and both projective extensions are positive. No patch introduces a new zero.

**20. F and half-Hessian.** F'=2p, F''=2q. F is smooth, nonconstant, and constant for r≤−1 and r≥1, so it extends smoothly across the lines. H0=dd^cF/2=p(P−Q)+qR.

**21. Solution forms and prescribed global measure.** On the band A0,B0 have the two checked triples. Outside it H0=0 and the patch preserves xyz=d_*. Their cubes equal 6d_*PQR=f_*(t)Ω³ on the open block set; smoothness extends equality globally. They are positive except for the two rank-2 levels.

**22. Symmetry.** p,z_b,S_* and κ are even, q odd, x_b(−r)=y_b(r). The even cutoff preserves x(−r)=y(r) and z(−r)=z(r).

**Local result:** pass; no critical errors or substantive gaps.

### Section 7, Repairing the background

**23. Global correction and coefficient formula.** h=(r²−1)η is identically zero on both tails and hence smooth globally. dd^c(εh)=εh'(P−Q)+εh''R, giving the exact three coefficients claimed.

**24. Positivity on the inner interval.** Here h'=2r and h''=2. On [0,3/2], x+2εr>0: x only vanishes at 1, where 2εr>0, and x(0)>0. On [−3/2,0], x has positive minimum m0 and 2εr≥−3ε. Choose ε>0 with 3ε<m0. Reflection proves y−2εr>0; z+2ε>0.

**25. Positivity on the transition and tails.** Original x,y,z have a common positive minimum m1 on the compact transition 3/2≤|r|≤2. With |h'|+|h''|≤M1, ε<m1/(M1+1) keeps every coefficient positive. Outside, the correction is zero and ω=κΩ>0. These finitely many inequalities have a common positive ε.

**26. Nonclosedness.** dω=dω0 since ddd^cρ=0. Near 0, S_* even gives x'(0)=−1/2,y'(0)=1/2; hence dω0=(z_b(0)+1/2)dr∧(Q−P). Its wedge with P and d^cr is a nonzero signed multiple of PQR. Thus dω≠0.

**27. Smooth normalized distinct solutions.** Set tilde u=−F/2−ρ, tilde v=F/2−ρ. Adding their Hessians to ω cancels the correction and yields A0,B0. Their suprema are finite by smoothness and compactness; subtraction preserves Hessians and gives sup 0. Difference=−F+constant is nonconstant.

**Local result:** pass; no critical errors or substantive gaps.

### Section 7, Zeros and higher dimensions; sharpness and closing remark

**28. Analyticity and complete zero set.** t is a ratio of real polynomials with positive denominator in every projective chart. f_*(t) is real analytic and nonnegative, with zeros exactly t=a,b in (0,1).

**29. Regular connected hypersurfaces.** On the open block set dr has nonzero radial λ derivative, so dt=σ'dr≠0. The level t=c is (S³_{√c}×S³_{√(1−c)})/S¹, a connected compact quotient by a free simultaneous phase action. Its real dimension is 5, and it has zero smooth volume.

**30. Quadratic transverse factors.** Near r=−1 the remaining factor in f_*(σ(r))=(r+1)²(r−1)²k_−²k_+² is positive and smooth; near +1 the analogous factor is positive. Both zero orders are exactly two.

**31. Product normalization.** On P³×P^(n−3), only the summand with exactly three first-factor (1,1)-forms survives. Both solution top powers and Ω_n^n carry the same coefficient binom(n,3). Consequently the pulled-back density is exactly f_*(t), without a missing dimensional factor.

**32. Other product conclusions.** The background sum is positive; pullback to a slice has nonzero exterior derivative. Solution ranks are 2+n−3=n−1 at the two product levels and n elsewhere. Surjective pullback preserves sup 0 and nonconstancy. Product levels remain connected and regular, and density remains analytic with quadratic transverse zeros.

**33. Sublevel and inverse-power sharpness.** Compactness supplies a finite tubular cover with c s²≤f_*≤C s² and a volume Jacobian bounded above and below by positive constants. The complement has density bounded below. Tubes of width proportional to √τ give two-sided sublevel volume bounds. The local integrability integral is ∫_0^δ s^(−2α) ds, finite exactly for α<1/2; α=1/2 diverges logarithmically. This holds in every dimension n≥3 and for any smooth positive reference volume.

**34. Components, degeneracy and extrema remark.** The three t intervals [0,a),(a,b),(b,1] give exactly three connected open components in X; connected levels and radial rescaling prove connectedness directly. A+B=2ω0 is positive off the zero levels and degenerate on them. Continuity excludes an almost-everywhere uniform positive lower bound around a degenerate point, so E_unif=U. The outer closures {t≤a},{t≥b} are disjoint. Since (u−v)'=−2p, its maximum and minimum occur on these outer closures and it varies strictly through the band. This verifies the remark directly, without invoking the excluded anchor theorem.

**Local result:** pass; no critical errors or substantive gaps.

### Section 8, Proposition constant and envelope definitions

**35. Proportional constant for C² potentials.** For ε>0 a global maximum of u−(1+ε)v exists. There dd^cu−(1+ε)dd^cv≤0, equivalently A+εω≤(1+ε)B. A≥0 and ω>0 imply B>0 there, so the determinant inequality A≤(1+ε)B can be divided by B^n>0 to give c≤(1+ε)^n. A^n=cB^n>0 also gives A>0. Reversing u,v yields c^(−1)≤(1+ε)^n. Letting ε↓0 proves c=1, without a positive-density assumption or results from sections 1–6.

**36. Envelope definition is meaningful.** Pω(h) is the upper regularization of the ω-psh minorant supremum. The condition Pω(ta)∈PSH for every t≥1 means those envelopes are not identically −∞; this is separate from a closed-background fixed-total-mass definition.

**37. Bounded functions belong to E_env.** For bounded a, each ta has a global constant lower bound and finite upper bound. Constants are ω-psh since ω>0. Thus the envelope family is nonempty and bounded above; upper regularization preserves the ω-psh current inequality, and the envelope is finite and bounded.

**38. Non-pluripolar truncation formula.** Since −j and a are ω-psh, max(a,−j) is bounded ω-psh. Locality on {a>−j} makes the restricted truncation measures an increasing sequence; their limit is the non-pluripolar measure. For bounded smooth a sufficiently large j leaves a unchanged, so it equals the classical top power.

**39. v_− and v_+ domains.** The infimum and supremum both range over all bounded ω-psh functions; additive normalizations do not change their masses. The domain is nonempty (constants). These are not presumed equal on the nonclosed equation form.

**Local result:** pass; no critical errors or substantive gaps.

### Section 8, ALS strict domination, solvability, constants and twisted uniqueness

**40. Exact ALS envelope class specialization.** ALS Definition 3.2 gives u⪯φ and Pθ(bu−(b−1)φ)∈PSH for all b≥1; at θ=ω,φ=0 this is precisely E_env. Compact quasi-psh upper boundedness supplies u⪯0. Positive ω is semipositive and big; Definition 2.13 explicitly admits φ=0 as model.

**41. Strict domination hypotheses.** ALS Theorem 3.14 matches the stated inequality with κ<1 and at least one finite total mass. Its additional b⪯φ hypothesis becomes automatic at φ=0. It requires v_−>0, not a v_+ bound; the manuscript retains all nonautomatic hypotheses.

**42. Untwisted equation.** ALS Section 5.2 assumes v_−>0; Corollary 5.9 supplies a positive constant and a solution for a nonzero non-pluripolar Radon measure and makes only the constant unique. Compactness makes the Radon measure finite, so each solution has finite mass cν(X). No uniqueness of the potential is inferred.

**43. Positive-exponent equation.** ALS Theorem 5.8 gives uniqueness of the potential in the same envelope class for λ>0. For any solution, its mass is bounded by e^(λ sup a)ν(X)<∞. On {a<b−δ}, the measure inequality has strict factor e^(−λδ), so Theorem 3.14 compares a with b−δ. Reversing and sending δ↓0 verifies uniqueness, without ever replacing κ<1 by 1.

**44. Operator conventions.** Under D0=k dd^c, the potential a/k has exactly the same solution form. The envelope obeys P_D0(h/k)=P_dd^c(h)/k; truncation levels are cofinal and strict sublevel sets correspond. For the twisted equation use λ0=kλ. Thus the exact class and all claims are invariant under any positive conventional scaling.

**Local result:** pass; no critical errors or substantive gaps.

### Section 8, Theorem fullmass-counter and final distinctions

**45. Metric comparison.** On the compact projective manifold the smooth positive forms ω and Ω have uniformly positive and finite relative eigenvalues. Thus one can choose 0<ε≤C with εΩ≤ω≤CΩ, also for each product example.

**46. Upper mass bound.** For every bounded ω-psh a, T=ω+dd^ca≥0 and CΩ+dd^ca=T+(CΩ−ω)≥T. Expanding its n-th power gives T^n plus nonnegative bounded mixed products. Since a is also bounded CΩ-psh and CΩ is closed, the total mass of that closed-background top power is C^n∫Ω^n. Thus v_+(ω)≤C^n∫Ω^n<∞, proving the manifold's bounded mass property without assuming closedness of ω.

**47. BGL lower-volume application.** BGL Proposition 3.7 assumes the bounded mass property in its section and compares smooth θ1≤θ2 with ordered θi-psh potentials φ1≤φ2. Set θ1=εΩ,θ2=ω,φ1=φ2=0. Both currents are positive; no closedness of θ2 is required.

**48. Exact lower-volume definition.** BGL Definition 3.1 takes the infimum of ∫(θ+dd^cψ)^n over θ-psh ψ with ψ=φ+O(1). For φ=0 this is exactly all bounded θ-psh ψ, matching the manuscript's v_−. Consequently v_−(ω)≥v_−(εΩ)=ε^n∫Ω^n>0. The closed-background identity is used only on εΩ.

**49. NMA, measure and class of exhibited solutions.** Both constructed smooth potentials are bounded, hence in E_env, and deep truncations give the same smooth top powers. Set ν to their common top power. Relative to ω^n its density is f_*(t)Ω^n/ω^n, a smooth nonnegative function with positive smooth multiplier. Its exact two quadratic hypersurface zeros are unchanged; it is positive almost everywhere and has positive finite mass. Pluripolar sets are locally contained in a psh −∞ locus and have zero smooth volume, so ν is non-pluripolar.

**50. Unique c but distinct normalized potentials.** With v_−>0 and nonzero finite non-pluripolar ν, ALS applies to all competing E_env solutions, whose masses are finite cν(X). The exhibited c=1 fixes the unique constant. Their nonconstant difference and supremum normalizations remain as checked in section 7. Thus 0<v_−≤v_+<∞ and two distinct normalized solutions coexist.

**51. Concluding background and class distinctions.** The constructed projective manifolds admit the explicit auxiliary Kähler form Ω or Ω_n; the nonclosed object is the equation form ω or ω_n. The envelope definition for that nonclosed form is not identified with a mass-equality class for a different closed form or a prescribed singularity type. No comparison on ω is imported from its auxiliary Kähler metric.

**52. Scope and assumption audit.** All requested construction, normalization and envelope assertions have been checked in their written order. Positive uniqueness in sections 1–6 was never assumed, and the section 7 geometric remark was verified directly. The result verifies the supplied sections rather than certifying novelty or the unexamined manuscript portions.

**Local result:** pass; no critical errors or substantive gaps.

## External reference verification

The checks below concern the actual statements, their definitions, and their use in this manuscript. The cited primary results are verified as external inputs; this run does not re-prove their full papers. Unrelated theorem-search hits were rejected as evidence. Exact results were then established from the primary papers and their archived full texts.

### Reference 1: Section 8, ALS strict domination

**Statement used.** Under v_-(ω)>0, if a∈E_env(X,ω), b∈PSH(X,ω), at least one non-pluripolar measure has finite mass, and 1_{a<b}NMAω(a)≤κ1_{a<b}NMAω(b) for 0≤κ<1, then a≥b.

**Primary source.** [Alehyane–Lu–Salouf, arXiv:2511.02339v1, Theorem 3.14 (p.16), Definitions 2.13 (p.11) and 3.2 (p.12).](https://arxiv.org/html/2511.02339v1)

**Definitions and applicability.** ALS uses a smooth semipositive big θ and model φ. Positive ω and φ=0 satisfy these requirements. The relative class formula Pθ(ta−(t−1)φ)∈PSH and a⪯φ becomes precisely the manuscript formula; b⪯0 is automatic by compact upper boundedness. The finite-mass and strict-factor hypotheses are exactly retained.

**Search and verification.** Required full-statement theorem search first returned unrelated results; built-in web fallback and archived primary ALS26.pdf/text confirmed the exact theorem.

**Result:** matched and applicable; no critical errors or substantive gaps.

### Reference 2: Section 8, ALS existence and unique normalizing constant

**Statement used.** For a nonzero non-pluripolar positive Radon measure ν and v_-(ω)>0, NMAω(a)=cν admits a solution a∈E_env and has a unique possible positive c; no uniqueness of a is asserted.

**Primary source.** [ALS Corollary 5.9 (pp.29–30), Section 5.2 hypothesis (p.28), Corollary 3.15 (p.17).](https://arxiv.org/html/2511.02339v1)

**Definitions and applicability.** Section 5.2 assumes v_-(θ)>0 without v_+(θ)<∞. At φ=0 the exact envelope class is E_env. Radon measures on compact X have finite total mass, and competing solutions have mass cν(X), so uniqueness applies to all such solutions. Corollary 5.9 uniquely specifies c, not u.

**Search and verification.** Full-statement theorem search first (one deadline timeout followed by an allowed successful retry); unrelated hits rejected, then built-in web fallback plus archived primary text.

**Result:** matched and applicable; no critical errors or substantive gaps.

### Reference 3: Section 8, ALS positive-exponent potential uniqueness

**Statement used.** For λ>0, the corresponding equation NMAω(a)=e^(λa)ν has a unique potential in E_env when v_-(ω)>0 and ν is a nonzero non-pluripolar positive Radon measure.

**Primary source.** [ALS Theorem 5.8 (pp.28–29) and Theorem 3.14.](https://arxiv.org/html/2511.02339v1)

**Definitions and applicability.** The same θ=ω,φ=0 specialization applies. Each solution has mass ≤e^(λ sup a)ν(X)<∞. Comparing a with b−δ gives strict factor e^(−λδ); reverse and let δ↓0. This validates the downstream uniqueness sentence without using κ=1 domination.

**Search and verification.** Required full-statement theorem search first found no match; built-in web fallback and archived ALS primary confirmed the numbered theorem.

**Result:** matched and applicable; no critical errors or substantive gaps.

### Reference 4: Section 8, BGL lower-volume monotonicity

**Statement used.** On a compact complex manifold with the bounded mass property, smooth real forms θ1≤θ2 and potentials φi∈PSH(θi) with φ1≤φ2 give lower_vol(θ1+dd^cφ1)≤lower_vol(θ2+dd^cφ2), and the analogous upper-volume inequality.

**Primary source.** [Boucksom–Guedj–Lu, arXiv:2406.01090v1, Definition 3.1 (p.19), Proposition 3.7 (p.21); corroborated in the published article.](https://arxiv.org/html/2406.01090v1)

**Definitions and applicability.** The section assumes the bounded mass property. The manuscript's upper bound proves it. Set θ1=εΩ, θ2=ω, φ1=φ2=0. Smooth forms are quasi-closed in BGL's sense (smooth exterior derivative); closedness of ω is not required. Definition 3.1 competitors ψ=φ+O(1) become exactly all bounded potentials at φ=0. Thus the inequality gives v_-(ω)≥v_-(εΩ)=ε^n∫Ω^n. Published D0=4π dd^c is handled by a→a/(4π), preserving currents and masses.

**Search and verification.** Initial manuscript-derived theorem-search payload was rejected by automatic review. It was not rerouted. Public bibliographic identifiers and archived primary text established provenance; a subsequent public Proposition 3.7 statement query was approved and returned unrelated hits. Built-in web fallback matched the published primary statement.

The statement was also checked in the [published primary article](https://link.springer.com/article/10.1007/s42543-025-00105-2).

**Result:** matched and applicable; no critical errors or substantive gaps.

## Strict aggregation and repair status

All 52 sequential deductions and all 4 reference applications were included in the aggregation. Both the critical-error list and the gap list are empty. The strict rule therefore gives `correct`, and `repair_hints` is the empty string. The verdict is limited to sections 7 and 8; it does not certify the excluded positive theorems or novelty.

The resulting construction has exactly the analytic density stated relative to the specified Fubini–Study volume. Relative to the constructed equation volume, its density need only be smooth: multiplication by the positive smooth volume ratio preserves its zero set and its precise quadratic transverse orders. No real-analytic regularity of the bump, potentials, or equation form is required or asserted.

## Reproducibility and saved artifacts

- [Strict output JSON](verification.json)
- [Independent section 7 recomputation](independent_section_7_audit.md)
- [Detailed ALS reference audit](als_reference_audit.md)
- [ALS reference search record](als_reference_searches.json)
- [Detailed BGL reference audit and search trail](bgl_reference_audit.md)
- Run memory: `memory/analytic_density_example_01/` (statement checks, reference checks, reports, failed checks, and events).

The initial BGL search carrying manuscript-derived wording was rejected by automatic approval review. The rejected content was not rerouted. Verification completed through archived primary sources and an approved search restricted to the already public theorem statement, followed by the required web fallback. The event is recorded in memory and in the BGL note; no approval blocker remains.
