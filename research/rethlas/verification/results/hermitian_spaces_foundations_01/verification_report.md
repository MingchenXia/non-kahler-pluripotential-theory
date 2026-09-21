# Verification report: Hermitian foundations on unibranch compact complex spaces

**Run:** hermitian_spaces_foundations_01  
**Verdict:** correct  
**Critical errors:** 0  
**Gaps:** 0

## Summary

The complete submitted appendix passes the sequential audit under the inputs explicitly accepted in the request. The argument retains the exact nonclosed background, proves descent with canonical disk representatives, handles compact connected fibers even when a component is entirely at minus infinity, and justifies upper semicontinuous regularization of envelopes. The new all-weight modification lemma is proved by local Bergman ideal types and Jacobian orders; its proof does not import the source's global Kähler modification theorem. The resulting resolution-ideal envelope, normalized topology, extended measures, capacity convergence and damped continuity are independent of the chosen smooth resolution.

The proof asserts neither a multiplier-ideal identification on singular local rings nor solvability of singular or degenerate equations. The supplied book and SGPT sources were used as mathematical evidence and were not edited.

This is an audit of the submitted text, in its original order. The detailed explanations below verify the intermediate inferences; they do not supply a new hypothesis or replace an invalid argument.

## 1. Hypotheses and permitted inputs

| Hypothesis or input | Role in the proof |
| --- | --- |
| Reduced complex space with compatible local embeddings | Defines smooth pullbacks and supplies the ambient local setting for the FN criterion. |
| Irreducibility and pure dimension \(n\geq1\) | Gives a dense regular locus, connected smooth models and a fixed dimension for all Jacobian and damping exponents. |
| Unibranchness | Gives connected fibers and irreducible sufficiently small local neighborhoods. It is used essentially in descent. |
| Compactness and properness | Give compact fibers, finite component and chart covers, closed images, normalized compactness and finite integrability covers. |
| Smooth real \((1,1)\)-background \(\theta\) | Gives smooth local dominating corrections and smooth pullbacks. Neither \(d\theta=0\) nor positivity is assumed. |
| Local genuineness and canonical disk representatives | Exclude open collapse and upward spikes that a distribution inequality alone would miss. |
| Accepted local SGPT facts | Resolutions/common refinements, connected fibers, FN and finite ramified disk lifting. |
| Accepted local ideal and Bergman inputs | All-positive-weight valuative criterion, local Bergman ideal type and lower estimate. |
| Accepted smooth book inputs | Normalized compactness, arbitrary-background ideal projection and damping/continuity, together with the specified local product and capacity facts. |

The normalized family can be empty for a background with no potentials; compactness then holds vacuously. Envelopes and constructions requiring a potential explicitly start with a nonempty family or a given genuine potential. There is no tacit assertion that every background admits one.

### Exact supplied-source locations

The local files are the controlling evidence for the accepted inputs.

| Input | Location and exact label |
| --- | --- |
| Connected fibers; resolution and domination | [SGPT unibranch appendix](</Users/mingchen/Downloads/Singularities in global pluripotential theory_Final/author/appendix_unibranch.tex:37>): thm:Zariskimain, thm:HironakaChow, thm:res. |
| FN disk criterion | [SGPT unibranch appendix](</Users/mingchen/Downloads/Singularities in global pluripotential theory_Final/author/appendix_unibranch.tex:117>): thm:FN; compare def:unibranch:L105. |
| Finite ramified disk lift | [SGPT unibranch appendix](</Users/mingchen/Downloads/Singularities in global pluripotential theory_Final/author/appendix_unibranch.tex:158>): disk-lifting paragraph in the proof of thm:GRexten2. |
| Local all-weight ideal criterion | [chapter_igood.tex](/Users/mingchen/Non-Kahler/book/author/chapter_igood.tex:43): thm:local-i-inputs, item 1, and its explicit local-scope paragraph. |
| Valuative source context | [SGPT psh chapter](</Users/mingchen/Downloads/Singularities in global pluripotential theory_Final/author/chapter_pshfunctions.tex:1173>): thm:valuativemulti; also prop:Lelongnumfrommis at line 1152. |
| Bergman ideal type and estimates | [chapter_analytic_approximation.tex](/Users/mingchen/Non-Kahler/book/author/chapter_analytic_approximation.tex:35): local finite-generation paragraph; prop:bergman-local-estimates at line 53. |
| Normalized compactness | [chapter_compactness.tex](/Users/mingchen/Non-Kahler/book/author/chapter_compactness.tex:10): thm:normalized-compactness. |
| Smooth ideal envelope and projection | [chapter_igood.tex](/Users/mingchen/Non-Kahler/book/author/chapter_igood.tex:30): def:hermitian-i-envelope; thm:hermitian-i-projection at line 80. |
| Arbitrary-background damping and continuity | [chapter_damped_measures.tex](/Users/mingchen/Non-Kahler/book/author/chapter_damped_measures.tex:376): thm:general-background-damping, including thm:damped-continuity at line 238 and thm:undamped-tail-continuity at line 280. |
| Smooth extended-product construction | [chapter_products.tex](/Users/mingchen/Non-Kahler/book/author/chapter_products.tex:93): arbitrary-background construction, including thm:arbitrary-extended-ma at line 128. This identifies the smooth measure already used by the accepted damping input. |
| Kähler theorem deliberately not imported | [SGPT envelopes chapter](</Users/mingchen/Downloads/Singularities in global pluripotential theory_Final/author/chapter_envelopes.tex:1996>): the Kähler standing assumption, prop:Iequivchar, prop:Ienvbimero and prop:Ienvelopebimero. |

## 2. Sequential verification

Each numbered item within a subsection is a separate checked deduction. Every subsection has status **passed**, with no critical error or gap.

### 2.1. Opening conventions and accepted complex-space facts

1. Reduced irreducible compact unibranch X has dense regular locus and a connected smooth compact resolution; its dimension remains n.

2. Embedding-smooth theta pulls back smoothly through holomorphic maps; positivity may degenerate and closedness is never asserted.

3. Resolution/common-refinement existence, connected fibers, the FN criterion and local finite ramified disk lifting are exactly the user-accepted complex-space inputs.

4. The source's later closed/Kahler descent and ideal-envelope conclusions are not taken as inputs to the new assertions.

### 2.2. def:space-theta-psh and following disk-potential paragraph

1. USC with values below +infinity gives local upper bounds; the separate nonempty-open-set condition excludes local collapse.

2. Every pulled-back real (1,1)-form on a one-dimensional disk is locally dd^c of a smooth function, regardless of d theta on X.

3. Canonical quasi-subharmonic representatives turn the distribution inequality into actual subharmonicity after that smooth addition; distribution positivity alone would not exclude an upward spike.

4. Restrictions identically -infinity, including constant disks through poles, are explicitly allowed.

### 2.3. lem:space-local-correction

1. After shrinking an embedding chart, a large positive multiple of the ambient squared norm has dd^c r>=theta.

2. For every disk in this chart, dd^c((u+r) o f)>=f^*(dd^c r-theta)>=0 and the representative remains canonical, or the restriction is identically -infinity.

3. USC and FN give space-psh u+r. Unibranchness permits an irreducible local neighborhood, and local genuineness excludes collapse.

4. On a manifold, choose a nonnegative radial convolution kernel. Distribution convolution gives dd^c u_epsilon>=-theta_epsilon with theta_epsilon tending smoothly to theta.

5. Writing u=p-r locally, p_epsilon decreases pointwise to p and remains psh; r_epsilon tends smoothly to r.

6. On every genuine disk, p_epsilon o f decreases to the genuine subharmonic restriction p o f and converges locally in L1. Thus the pulled-back smooth inequalities pass to distributions with exact f^*theta.

7. Conversely local correction gives a canonical locally integrable qpsh u. For a fixed complex direction, Fubini disintegrates the nonnegative directional distribution against nonnegative tests along affine disks.

8. The lines whose restrictions are identically -infinity have transverse measure zero by local integrability. Countably many dense directions give a positive Hermitian matrix of coefficient measures by polarization and continuity.
**Representative and convolution check.** Choose the convolution kernel to be nonnegative and radial, as is standard for this local regularization. If \(u=p-r\), then
\[
u_\varepsilon=p_\varepsilon-r_\varepsilon,\qquad
p_\varepsilon\downarrow p,\qquad r_\varepsilon\to r\ \text{smoothly}.
\]
The monotone family is the psh correction \(p_\varepsilon\), not necessarily \(u_\varepsilon\). Along a genuine disk its restriction converges in local \(L^1\), which is precisely what passing the pulled-back inequalities to distributions requires. The proof does not try to pull back an arbitrary coefficient measure directly.

For the converse, the local psh correction already ensures that the coefficients of \(dd^c u+\theta\) are measures. Fubini proves nonnegativity of its scalar contraction against each fixed complex direction. The countable dense set can be chosen to include polarization directions; it determines a positive matrix-valued measure. The null family of entirely polar lines causes no loss in the distribution calculation.


### 2.4. thm:hermitian-space-descent

1. Disk composition proves the forward curvature condition; the dense isomorphism locus ensures genuineness on every nonempty open subset upstairs. Surjectivity gives injectivity.

2. On a neighborhood of a fiber, dd^c(v+r o pi)>=pi^*(dd^c r-theta)>=0 is valid on the smooth resolution, with r a dominating correction rather than a potential for theta.

3. A compact analytic fiber has finitely many irreducible components. The restriction to the resolution of each component is psh or identically -infinity; compactness and the maximum principle make it constant.

4. At an intersection point both component constants equal the same value of v+r o pi. This includes -infinity: a finite constant component cannot intersect an all-minus-infinity component.

5. The finite component intersection graph is connected, so every component has the same extended-real constant. This proves fiberwise constancy without assuming restrictions are all genuine.

6. The descended u is USC since pi({v>=c})={u>=c} is closed by properness. If u collapsed on an open set, v would collapse on its nonempty open inverse image.

7. For a local finite lift pi o f'=f o rho, rho(t)=t^k, choose dd^c a=f^*theta on the original disk. Then dd^c(a o rho)=f'^*pi^*theta exactly.

8. The canonical subharmonic function (u o f+a) o rho descends on the punctured disk via inverse branches. At the branch point its value equals the punctured limsup because the lifted function is canonical and t^k maps small punctured disks onto small punctured disks.

9. The finite value/integrability alternative is local; locally identically-minus-infinity branches are allowed, and propagation on the connected disk excludes an open collapse when the whole restriction is genuine.

10. Order, pointwise suprema, uniform bounds and inequalities with additive constants follow from surjectivity and literal pointwise pullback.
**Exact nonclosed curvature and the ramification point.** Put \(g=u\circ f+a\), where \(dd^ca=f^*\theta\) on the original disk. The lifted expression satisfies
\[
g\circ\rho=v\circ f'+a\circ\rho,\qquad
dd^c(a\circ\rho)=\rho^*f^*\theta=f'^*\pi^*\theta.
\]
Thus the correction recovers the original background, including its full nonclosed contribution. There is no assertion that \(\theta=dd^cr\) on a neighborhood in \(X\).

If \(h=g\circ\rho\) is genuine, its canonical value gives
\[
g(0)=h(0)
=\limsup_{s\to0,\ s\ne0}h(s)
=\limsup_{t\to0,\ t\ne0}g(t).
\]
The last equality uses that \(s\mapsto s^k\) maps small punctured disks onto small punctured disks. Away from zero, inverse branches give subharmonicity. Local upper boundedness and this precise value identify the removable subharmonic extension. If a local lift is identically minus infinity, so is the corresponding local base restriction; the usual connected-domain alternative for locally subharmonic functions accounts for that case. No extra finiteness of restrictions to fibers or disks is needed.


### 2.5. prop:space-envelope-pullback

1. Descent identifies both competitor families and their pointwise suprema; local upper bounds pull back.

2. A genuine lower competitor prevents collapse of the upstairs USC envelope, which is pi^*theta-psh by the smooth supremum property.

3. Descent gives a USC q on X dominating s, hence q>=s^* because s^* is the least USC majorant under local upper bounds.

4. For each y over x and each neighborhood U of x, the upstairs unregularized supremum is bounded by sup_U s on pi^{-1}(U). Upper regularization at y is therefore at most sup_U s.

5. Infimizing over U proves q(x)<=s^*(x), so USC regularization commutes even over exceptional fibers.

6. Ordinary model-envelope competitors are identified by their upper bound and ordinary singularity comparison, including the comparison constants. The same argument applies.

### 2.6. Normalized compactness and independence of pullback L1 topology

1. The order bijection preserves suprema, identifying normalized families on X and any resolution.

2. The accepted thm:normalized-compactness applies to any smooth real background, including degenerate pi^*theta, on the connected compact smooth resolution.

3. Two smooth positive volume forms on a fixed compact resolution have bounded positive density ratios and equivalent L1 norms.

4. For a further modification rho:Z->Y, normalized sequences on both spaces are relatively compact with limits in their normalized psh classes.

5. On relatively compact subsets of the isomorphism locus, bounded smooth Jacobian factors identify any pair of L1 cluster limits by w=v o rho.

6. The complement is proper analytic; canonical qpsh representatives that agree there agree everywhere. Thus every cluster limit is uniquely the pullback of the downstairs limit.

7. Applying the subsequence argument in both directions proves equivalence of convergence. Both topologies are metrizable, so this is topological equivalence.

8. A common smooth refinement compares arbitrary resolutions. No global uniform L1-norm comparison through a modification is claimed.
**Why the topology argument is sufficient.** Given a sequence converging on \(Y\), take any subsequence of its pullbacks on \(Z\). Compactness gives a further convergent subsequence. On the isomorphism locus its limit must be the pullback of the original limit, and canonical representatives determine the value across the analytic complement. Every subsequence therefore has a further subsequence converging to the same limit, which proves convergence of the full sequence. Start with a convergent sequence on \(Z\) and use compactness on \(Y\) to obtain the reverse implication. Since these are metric topologies induced by \(L^1\), the sequential criterion proves topology independence.


### 2.7. lem:ideal-equivalence-modification

1. Work locally on Y and add a smooth psh correction to a and b. Smooth corrections preserve all multiplier ideals and Lelong numbers.

2. The accepted Bergman construction has analytic type (1/m,I(ma)); removing the correction leaves a_m>=a-C/m on a smaller neighborhood.

3. For F=rho o tau, where tau is any local smooth modification of Z, F is a generically one-to-one holomorphic map between n-manifolds. Its holomorphic Jacobian is nonzero as a germ and has finite order j at the chosen point.

4. For h in I(ma), the change-of-variables formula makes |h o F|^2 |J_F|^2 exp(-m a o F) locally integrable. This uses the Jacobian factor, not ordinary ideal pullback.

5. Let ell=ord_z((h o F)J_F), nu=nu(a o F,z). The psh logarithmic upper bound a o F <= (nu-epsilon) log|w-z|^2+C and a cone on which the leading homogeneous part is nonzero give a lower integrand bound.

6. The radial integral is bounded below by a positive multiple of integral r^{2ell-2m(nu-epsilon)+2n-1} dr. Integrability forces ell+n>m(nu-epsilon); letting epsilon decrease to zero gives ord_z(h o F)>=m nu-n-j.

7. For finite nonzero local generators h_l of I(ma), the pulled-back analytic type has Lelong number min_l ord_z(h_l o F)/m. Thus nu(a o F,z)-(n+j)/m<=nu(a_m o F,z).

8. The pulled-back Bergman lower bound reverses Lelong order and gives nu(a_m o F,z)<=nu(a o F,z). The Jacobian order depends on fixed F,z, not on m.

9. All-weight equality downstairs implies identical integer-weight Bergman ideal types; their pullbacks have the same Lelong number for each m. Squeezing as m tends to infinity yields equality for a o F and b o F.

10. Quantifying over every local tau and point of its smooth source gives exactly the accepted local valuative criterion on Z. No global extension of tau and no Kahler model are used.

11. For the converse, fix any real t>0 and a base germ h. Downstairs local integrability is equivalent to upstairs integrability of (h o rho)J_rho at every point of the compact fiber.

12. Properness gives finitely many relatively compact integrability neighborhoods covering the fiber and a smaller base neighborhood whose inverse image lies in that cover.

13. Equality of upstairs multiplier ideals at this same real t applies to the holomorphic germs (h o rho)J_rho. Change of variables then transfers integrability to b; symmetry gives equality downstairs for every t>0.
**Explicit Jacobian-order calculation.** Fix \(F,z\), and set
\[
H=(h\circ F)J_F,\quad
\ell=\operatorname{ord}_zH,\quad
j=\operatorname{ord}_zJ_F,\quad
\nu=\nu(a\circ F,z).
\]
A nonzero leading homogeneous polynomial is bounded below in absolute value on some open set of angular directions. On a smaller cone there,
\[
|H(w)|^2e^{-ma\circ F(w)}
\geq c_\varepsilon |w-z|^{2\ell-2m(\nu-\varepsilon)}.
\]
The real volume element in complex dimension \(n\) contributes \(r^{2n-1}\,dr\). Therefore integrability forces
\[
\int_0^\delta r^{2\ell-2m(\nu-\varepsilon)+2n-1}\,dr<\infty,
\quad\text{hence}\quad
\ell+n>m(\nu-\varepsilon).
\]
Taking \(\varepsilon\downarrow0\) yields the non-strict bound
\[
\operatorname{ord}_z(h\circ F)=\ell-j\geq m\nu-n-j.
\]
For local generators \(h_\alpha\) of \(\mathcal I(ma)\), the analytic-type convention gives
\[
\nu(a_m\circ F,z)
=\frac1m\min_\alpha\operatorname{ord}_z(h_\alpha\circ F).
\]
Combining this with the pulled-back Bergman lower bound proves exactly
\[
\nu(a\circ F,z)-\frac{n+\operatorname{ord}_zJ_F}{m}
\leq\nu(a_m\circ F,z)\leq\nu(a\circ F,z).
\]
The loss is attached to the fixed germ \(F,z\), so it disappears as \(m\to\infty\). No uniformity in all modifications at once is necessary: the quantifiers are “fix a modification and point, then let \(m\to\infty\).”

For the converse, local integrability around every point of the fiber must first be turned into integrability over the inverse image of one base neighborhood. Choose finitely many relatively compact integrability neighborhoods covering the compact fiber. Properness allows the base neighborhood to shrink so its entire inverse image lies in their union. Summing their finite integrals supplies the required finite integral. This verifies the finite-cover step and shows why the Jacobian factor is indispensable.


### 2.8. Definition of resolution-ideal equivalence

1. All positive weights are explicitly required on a smooth resolution.

2. Pullback and converse in the new lemma transport equality in both directions along each morphism from a common smooth refinement.

3. The definition therefore does not depend on the chosen resolution.

4. Only smooth-model multiplier ideals are used; no ideal on a singular local ring is implicitly identified with them.

### 2.9. prop:space-resolution-i-envelope

1. On a fixed resolution, the accepted arbitrary-background projection theorem gives a genuine Q in the original all-weight ideal class.

2. The descent theorem gives a unique potential downstairs.

3. For rho:Z->Y, every upstairs Q competitor descends; normalization v<=0 is preserved and the new lemma identifies its ideal class with the downstairs one.

4. The regularized supremum compatibility already proved for envelopes therefore applies to Q.

5. Two resolutions give the same potential after pullback to a common refinement; surjectivity proves equality on X.

6. Preservation of the resolution-ideal class, idempotence and supremum zero follow from their smooth counterparts under the bijection.

### 2.10. eq:space-extended-ma and thm:space-extended-measures

1. Choose a resolution that is an isomorphism above X_reg, as allowed by the accepted resolution input. The inverse image of X_sing is a proper analytic set.

2. The smooth extended product charges neither that analytic set nor other pluripolar sets.

3. On X_reg all resolutions identify the same smooth background and canonical potential. Local bounded BT expansions, truncation and exhaustion are invariant under biholomorphic change of coordinates.

4. Thus the pushforwards agree on X_reg and have zero mass on its complement; this proves independence without already assuming singular-space measure functoriality.

5. Pushforward preserves positivity and the Borel measure property. Sigma-finiteness uses the Borel isomorphism off the analytic null set; it is not inferred for an arbitrary pushforward.

6. Locally pluripolar sets pull back to pluripolar sets on the isomorphism locus, and the remaining exceptional set is null.

7. For bounded u its pullback is bounded on compact Y, so a finite cover and local bounded-product mass estimates give finite total mass.

8. The accepted arbitrary-background damping theorem applies to pi^*theta for any nonpositive pulled-back u, without positivity of the background or a Kahler metric.

9. The equality of weighted pushforward integrals gives exactly the two stated bounds with r_n=max(n-2,0), p>0 and q>r_n. Constants are uniform in u on one fixed resolution.

10. The argument permits infinite undamped total mass; finiteness is asserted only in the bounded case or after damping.
**Measure interpretation.** The conclusion is a positive sigma-finite Borel measure, possibly with infinite mass on a compact space; it is not asserted to be globally locally finite or to define a global order-zero current when the mass is infinite. The proof's sigma-finiteness argument specifically uses a Borel isomorphism away from an analytic null set. Arbitrary pushforwards of sigma-finite measures need not be sigma-finite.

The weighted pushforward identity is exact, including poles:
\[
\int_X W(u)\,d\pi_*\mu
=\int_Y W(u\circ\pi)\,d\mu,
\]
where \(W(t)=e^{pt}\) or \(W(t)=(1-t)^{-q}\) for \(t\leq0\), with value zero at \(t=-\infty\). The pole set is already null for the extended measure. The ranges \(p>0\) and \(q>\max(n-2,0)\) are unchanged because a resolution has the same dimension.

Sigma-finiteness can also be checked directly from the accepted damping bound: after an additive normalization \(w\leq0\), the sets \(\{w\geq-k\}\) have mass at most \(e^k\int e^w\,d\mu\), and these sets exhaust the complement of the null pole set.


### 2.11. Capacity convergence and resolution independence

1. Changing the smooth Hermitian capacity on one compact resolution preserves convergence by the accepted local capacity equivalence and a finite chart cover.

2. For rho:Z->Y, let A be an analytic exceptional image outside which rho is an isomorphism and B=rho^{-1}(A). Both have arbitrarily small-capacity open neighborhoods.

3. To transfer capacity-small E_j on Y upwards, first discard a fixed neighborhood V of B with small capacity on Z.

4. Z\V is compact inside the isomorphism locus. A finite biholomorphic chart cover compares capacity of rho^{-1}(E_j) there with capacity of E_j on Y.

5. Subadditivity yields limsup_j Cap_Z(rho^{-1}(E_j))<=Cap_Z(V); let this bound go to zero.

6. For the converse first discard a small-capacity neighborhood U of A on Y and compare on the compact Y\U, using its compact lifted image. This avoids requiring synchronized neighborhoods or global capacity constants.

7. Apply to the discrepancy sets of a sequence of potentials; pole-set conventions do not matter since those sets are pluripolar. A common refinement compares arbitrary resolutions.
**The two capacity comparisons use different discarded neighborhoods.** Let \(A\subset Y\) be a proper analytic set such that \(\rho\) is an isomorphism off \(A\), and put \(B=\rho^{-1}(A)\). For any \(\varepsilon>0\), choose an open \(V\supset B\) with \(\operatorname{Cap}_Z(V)<\varepsilon\). Finite chart comparison on \(Z\setminus V\) gives, for Borel sets \(E\subset Y\),
\[
\operatorname{Cap}_Z(\rho^{-1}E)
\leq \varepsilon+C_\varepsilon\operatorname{Cap}_Y(E).
\]
For the other direction choose an open \(U\supset A\) with \(\operatorname{Cap}_Y(U)<\varepsilon\). Comparison on \(Y\setminus U\) gives
\[
\operatorname{Cap}_Y(E)
\leq \varepsilon+C'_\varepsilon\operatorname{Cap}_Z(\rho^{-1}E).
\]
These are the local capacity comparisons stipulated as accepted inputs, summed over fixed finite covers. The constants may deteriorate as \(\varepsilon\downarrow0\); taking the sequence limit first avoids any need to control that deterioration. Applying the inequalities to discrepancy sets proves both directions of convergence. Any ambiguity in subtracting two values equal to minus infinity is confined to pluripolar sets of capacity zero.


### 2.12. Damped and undamped weak continuity under capacity convergence

1. Resolution-independent capacity convergence implies capacity convergence of the nonpositive pullbacks on any fixed resolution.

2. The accepted thm:general-background-damping explicitly includes continuity for both exponential and polynomial damping in the displayed ranges.

3. For a continuous test function phi on X, phi o pi is continuous on compact Y. Weak convergence upstairs therefore pushes forward.

4. For undamped continuity, pi^{-1}({u_j<-T})={u_j o pi<-T}, and both total masses and deep-sublevel masses are equal under the measure pushforward.

5. The stated uniform total-mass bound and uniform tail condition are exactly the accepted smooth undamped hypotheses. Their transfer yields a finite limit and weak convergence downstairs.
**Undamped tail transfer.** If \(\mu_j^Y\) is the smooth extended measure of \(u_j\circ\pi\), then
\[
\mu_j^Y(Y)=\mu_j^X(X),\qquad
\mu_j^Y(\{u_j\circ\pi<-T\})
=\mu_j^X(\{u_j<-T\}).
\]
Thus the two stated tail hypotheses upstairs are exactly those stated downstairs. They imply finiteness of the limit as well as weak convergence by the accepted smooth theorem. The appendix does not claim undamped continuity from capacity convergence alone.


### 2.13. The limits of this extension and final synthesis

1. Pullback of a positive background can have vertical null directions on an exceptional fiber, so the smooth strictly positive equation theorem does not apply directly.

2. An embedding-smooth top-degree volume pulls back degenerately on the exceptional locus where the differential loses full rank. No positive smooth volume input is asserted there.

3. No existence, regularity or normalization theorem for singular or degenerate equations is deduced.

4. Resolution-ideal equivalence alone does not construct restricted-ideal traces supported in the singular locus or singular-local-ring regularization; these are explicitly excluded.

5. The claims actually established use local complex-space theory and arbitrary-background smooth inputs, never a Kahler resolution or a uniform undamped mass bound.
## 3. External-reference verification and definition comparisons

The required arXiv theorem search was run first with six full statement queries. Unrelated results were not accepted as matches. Built-in web search followed, and the supplied local source files were compared directly throughout. The author's online SGPT version also supplied matching primary-source statements.

| Reference group | Search and source outcome | Applicability |
| --- | --- | --- |
| Resolution/common refinement and connected fibers | Initial theorem search did not give the exact combined statement. The supplied appendix and the author's PDF give the needed complex-space statements. | Matches the accepted complex-space hypotheses; no Kähler hypothesis is inserted. |
| FN criterion | Initial theorem search returned insufficient manifold-only or unrelated statements. The supplied source and online Theorem B.2.1 give the exact complex-space criterion. | Applied to a genuine local psh correction, with USC and actual canonical restrictions. |
| Finite ramified disk lifting | Initial search did not give the cited statement. It occurs explicitly in the source proof and its online version. | The proof uses a local lift after shrinking, exactly as supplied. |
| Local all-weight ideal criterion | ArXiv search found Theorem 1.1 of arXiv:2310.00368, formulated with \(\mathcal I_+\). The supplied book states the exact accepted \(\mathcal I\)-version locally. | Strong openness and the weight normalization are explicitly accounted for. |
| Local Bergman type and lower estimate | The exact accepted statement is in the supplied analytic-approximation chapter. Web search also located Demailly's local Theorem 14.2. | The factor-of-two convention is translated; no global regularization theorem is required. |
| SGPT bimeromorphic ideal equivalence | The supplied source proposition and online Proposition 3.2.2 explicitly have Kähler context. | Used as source attribution only. The appendix proves its needed non-Kähler version independently. |

The author's online appendix confirms connected fibers, the complex-space FN criterion and the finite ramified lifting paragraph. The relevant statements are Theorems B.1.1–B.1.3, Theorem B.2.1 and the proof of Theorem B.2.2. These complex-space inputs precede the subsequent closed/Kähler specialization. [SGPT, Appendix B](https://mingchenxia.github.io/Lectures/SGPT_final.pdf#page=515).

The arXiv match is not treated as literal equality of differently defined ideals. Its Theorem 1.1 uses
\[
\mathcal I_+(tu)=\bigcup_{p>1}\mathcal I(ptu),
\]
and the same page defines its ideal using \(e^{-2u}\) and records strong openness \(\mathcal I_+=\mathcal I\). Consequently, after substituting the appropriate half-weight, its all-positive-weight equivalence agrees with the convention in the submitted proof. [Bao–Guan–Mi–Yuan, Theorem 1.1 and accompanying definitions](https://arxiv.org/pdf/2310.00368#page=3).

Demailly's local approximation uses \(e^{-2m\phi}\) and \(\phi_m=(2m)^{-1}\log\sum|\sigma_\ell|^2\). Setting \(\psi=2\phi\) and \(\beta_m=2\phi_m\) gives the proof's normalization and lower bound, with a renamed constant. [Demailly, Analytic Methods in Algebraic Geometry, Theorem 14.2](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/analmeth_book.pdf#page=136).

The source's global bimeromorphic ideal proposition has a Kähler assumption; the appendix correctly avoids importing it as a theorem in its new setting. Its radial/Jacobian proof establishes the needed implication directly, and its converse retains the Jacobian in the integrability test. [SGPT, Proposition 3.2.2](https://mingchenxia.github.io/Lectures/SGPT_final.pdf#page=139).

The remaining book references were expressly accepted as already verified. Their exact statements and hypotheses were checked for applicability, rather than reproved. All match the use made of them.

## 4. Final findings

### Critical errors

None.

### Gaps

None.

### Assumption-use conclusion

All material hypotheses have a justified role. Unibranchness is used for connected fibers; compactness and properness supply the finite covers and global compactness arguments; irreducibility prevents disconnected normalization problems; smoothness supplies local curvature bounds and ordinary pullbacks. The proof consistently allows the pullback background to be degenerate and nonclosed.

The delicate assertions singled out in the request have all been checked: local genuineness, canonical disk values, exact curvature after a finite cover, all-minus-infinity fiber components, regularized supremum descent, normalized topology independence, the all-weight Bergman/Jacobian argument, resolution-ideal \(Q\), extended measure independence and sigma-finiteness, and capacity/damping pushforward.

### Verdict and repair hints

**Verdict: correct.** Both finding lists are empty, so the strict acceptance rule is satisfied.

**Repair hints:** empty. No mathematical repair is required under the stipulated inputs.

## 5. Audit artifacts

The run contains 13 sequential statement records covering 90 individual deductions, reference checks with their contextual comparisons, and event records. The machine-readable verdict is [verification.json](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/hermitian_spaces_foundations_01/verification.json). The persistent audit channels are under [memory/hermitian_spaces_foundations_01](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/hermitian_spaces_foundations_01).

All verification output is confined to this verification workspace. No book or SGPT source was edited.

