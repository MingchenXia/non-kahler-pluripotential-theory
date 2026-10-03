# Gauduchon normalization of polar trace data

Research continuation through manuscript checkpoint347, based on independently verified private checkpoint346, 215870599210b88db11de8051c9136250dffb2f4.

Status: the elementary comparison, analytic-model separation, curve reduction, raw gauge identity and ambient completeness are integrated in manuscript continuation 337, Propositions 15.6.20 and 15.6.21. Checkpoint 338 adds a complete local proof of polar-current invariance under bounded equivalence and applies it to ordinary-model gauge transport. Its clean manuscript compilation, both complete source/proof reads and affected output review pass. Empty-source reconstruction and private synchronization follow the release record. The book writes this comparison as \(\delta_\omega^{\mathrm{pol}}\). Checkpoint343 disproves general separation and exact ideal analytic closure for this first-polar candidate, even at positive lower volume and independently of all Gauduchon choices. Simultaneous realization remains a further problem; the required complete replacement topology is unresolved. The comparison does not solve P01/P17. No novelty claim or independent external certification is made.

## Setting and comparison

Fix a connected compact complex manifold \(X\), of dimension \(n\geq1\), and a Hermitian form \(\omega\). Let \(\mathscr R\) be a set of smooth modifications \(\pi:Y_\pi\to X\) containing the identity and common log resolutions for pairs of analytic singularity types. Choose a Gauduchon form \(\eta_\pi\) on each \(Y_\pi\), so that
\[
 \operatorname{dd}^{\mathrm c}\eta_\pi^{n-1}=0.
\]
These are fixed choices; no general independence of the choice of Gauduchon forms is asserted.

For a genuine \(u\in\operatorname{PSH}(X,\omega)\), put
\[
 T_\pi(u)=\pi^*\omega+
       \operatorname{dd}^{\mathrm c}(u\circ\pi),\qquad
 \mu_\pi(u)=\mathbf1_{\{u\circ\pi=-\infty\}}
       T_\pi(u)\wedge\eta_\pi^{n-1},
\]
where the current restriction is coefficientwise, as in the manuscript's polar-current section. Define
\[
 A_\pi=\int_{Y_\pi}\pi^*\omega\wedge\eta_\pi^{n-1},
 \qquad
 D_\omega(u,v)=\sup_{\pi\in\mathscr R}
       \frac{\|\mu_\pi(u)-\mu_\pi(v)\|_{\mathrm{TV}}}{A_\pi}.
\]
The intended domain is the normalized ordinary models. Defining the same expression on all genuine potentials helps distinguish exact gauge transport from ordinary-model projection.

## Uniform bound and pseudometric

Each \(A_\pi\) is strictly positive and finite: the smooth form \(\pi^*\omega\) is semipositive and is positive on the nonempty isomorphism locus. The pullback potential is genuine and has positive curvature by the manuscript's modification descent theorem. Distributional Stokes and the Gauduchon equation give
\[
 \int_{Y_\pi}T_\pi(u)\wedge\eta_\pi^{n-1}
       =A_\pi.
\]
Thus \(\mu_\pi(u)\) is a positive finite measure with
\[
 \mu_\pi(u)(Y_\pi)\leq A_\pi,
 \qquad 0\leq D_\omega(u,v)\leq2.
\]
This uses linear trace mass, not a top-degree volume bound. The background need not be closed.

For each coordinate, total variation is a norm on finite signed measures. Dividing by the fixed positive \(A_\pi\) preserves symmetry and the triangle inequality. Taking the supremum preserves both. Consequently \(D_\omega\) is a bounded pseudometric. Separation on all ordinary models fails by checkpoint343; the formula remains a pseudometric there.

Multiplying any \(\eta_\pi\) by a positive constant multiplies both its numerator and denominator by the same factor. The coordinate comparison is unchanged. This removes scalar rescaling of the chosen Gauduchon forms, but does not compare different Gauduchon shapes on infinitely many modifications.

## Separation on analytic ordinary models

Let \(p,q\) be normalized ordinary models with analytic singularities. Choose a common log resolution \(\pi\in\mathscr R\), with prime divisors \(E_1,\ldots,E_N\). On resolution charts, write their singular parts as
\[
 p\circ\pi=\sum_i a_i\log|s_i|^2+O(1),\qquad
 q\circ\pi=\sum_i b_i\log|s_i|^2+O(1),
\]
including zero coefficients for components absent from one type. Their pole sets are precisely the unions of components with positive coefficients. The divisorial restriction argument in the proof of manuscript Lemma 1.17.1 gives
\[
 \mu_\pi(p)=\sum_i a_i[E_i]\wedge\eta_\pi^{n-1},\qquad
 \mu_\pi(q)=\sum_i b_i[E_i]\wedge\eta_\pi^{n-1}.
\]
The smooth local correction used in that argument does not charge a divisor. Distinct divisors have no overlapping trace mass on their intersections. Since each divisor has strictly positive Hermitian trace mass, equality of these two measures implies \(a_i=b_i\) for every \(i\).

If \(D_\omega(p,q)=0\), equality holds in this coordinate. The logarithmic terms then cancel, giving bounded ordinary equivalence upstairs. A finite cover of the compact resolution bounds the difference away from the common pole set. Surjectivity descends the two inequalities to the complement of the pole set downstairs; canonical quasi-plurisubharmonic representatives extend them everywhere. Hence \(p\sim q\). Ordinary envelope projection depends only on this equivalence class, so the two normalized ordinary models are equal.

This proves separation on analytic ordinary models. It uses the manuscript's existing analytic-resolution and divisorial-restriction inputs, not a fresh external proof audit. Checkpoint 342 extends recovery of the whole polar currents from these scalar traces to arbitrary pole sets, after the local complete-pluripolar restriction proof is checked. General model separation from these currents fails by the diffuse-product example below.

## Complete ambient coordinate space

Consider the full coordinate space
\[
 \mathscr B=\prod_{\pi\in\mathscr R}
    \{\mu\text{ positive finite Borel on }Y_\pi:
                    \mu(Y_\pi)\leq A_\pi\},
\]
with the supremum of normalized total-variation distances. This is a metric bounded by two and is complete.

Indeed, a Cauchy sequence is Cauchy in every coordinate in the Banach space of finite signed measures. Its coordinate limit is positive and satisfies the same mass bound. Given \(\varepsilon>0\), choose \(N\) such that for all \(j,k\geq N\) and every \(\pi\), the normalized coordinate distance is at most \(\varepsilon\). Letting \(k\to\infty\) separately in each coordinate retains this inequality for its limit. Taking the supremum then proves convergence in the ambient metric.

The map \(\Phi(u)=(\mu_\pi(u))_\pi\) takes values in this complete space. Completeness of \(\mathscr B\) does not prove that the ordinary-model image is closed. A simultaneous realization theorem for its limiting coordinates is the missing assertion.

One necessary property of a coordinate limit is retained without such a theorem. If \(\mu_\pi(p_j)\) converges in total variation, its limit is carried by the countable union of the actual pole sets \(\{p_j\circ\pi=-\infty\}\): the complement has zero measure for every sequence term, and its limit mass is bounded by the variation distance. This does not construct a single potential realizing the limits across modifications.

## Curves and smooth gauges

In dimension one, every modification of smooth connected compact curves is an isomorphism. Its trace exponent is zero, \(A_\pi=\int_X\omega\), and pullback preserves the total variation of the polar curvature measure. Therefore, on curve models,
\[
 D_\omega(p,q)=
       \frac{\|\mu_p-\mu_q\|_{\mathrm{TV}}}{\int_X\omega}.
\]
For a fixed positive-area background this is a constant multiple of the complete curve metric already proved in manuscript Section 29.12. It has the same topology, completeness and analytic closure. It is not a construction over varying zero-area backgrounds, where this normalization has a zero denominator.

Exact smooth-gauge transport also holds on genuine potentials. If \(\omega'=\omega+\operatorname{dd}^{\mathrm c}f\) and \(u'=u-f\), then their pulled-back curvature currents and pole sets agree. Distributional Stokes gives \(A_{\pi,\omega'}=A_{\pi,\omega}\), using the same Gauduchon forms. Thus their coordinate comparisons agree. For an ordinary fixed point, the gauge estimate bounds the projected model plus the smooth gauge between the original model plus the minimum and maximum of that gauge. The two potentials are therefore boundedly equivalent. The local bounded-invariance proposition proves equality of all their pulled-back polar current restrictions, so the comparison is also preserved after this projection. Ordinary-envelope dependence on the bounded class proves the inverse and fixed-point assertions; no unrestricted idempotence or positive-volume theorem is used. Analytic and ideal models are preserved by the existing ideal gauge and projection identities.

## Local bounded-invariance proof boundary

The foundation proof has three components. A locally bounded function with measure Laplacian has locally square-integrable gradient, obtained by testing its smooth mollifications against its product with a squared cutoff and absorbing the cross term. A negative quasi-psh potential after smooth correction has truncations whose Laplacian masses are bounded on each fixed compact set; their cutoff energies grow at most linearly in the truncation depth. Dividing by that depth gives smooth functions equal to one near any compact subset of the pole set, with Sobolev norm tending to zero.

For the bounded difference of two locally equivalent quasi-psh potentials, every real and imaginary Hessian coefficient is both a signed measure and a continuous functional on the local Sobolev space. On a compact subset of its positive Hahn set inside the common pole set, choose the test support so that the negative Jordan mass is arbitrarily small. The vanishing Sobolev norm then forces the positive mass of that compact set to vanish. Inner regularity and the same argument for the negative part exclude every coefficient from the pole set. Smooth backgrounds give no mass there either.

This proves coefficientwise polar invariance on all complex manifolds, with locally bounded equivalence. It neither identifies a general ordinary model from its polar coordinates nor proves a general projection identity for arbitrary potentials. The argument is internal; no novelty or independently updated literature claim is attached to it.

## Recovery for closed pole sets

For two closed positive (1,1)-currents carried by a common Lebesgue null set, equality of the trace for one smooth Hermitian form forces equality of the currents. Locally write them as complex Hessians of psh potentials. The difference satisfies a homogeneous scalar uniformly elliptic equation with smooth coefficients, so elliptic regularity makes it smooth. Its Hessian is smooth and still carried by the null set; it therefore vanishes.

For a potential with a closed pole set, add a local smooth correction to get a closed positive Hessian. The closed complete pluripolar restriction theorem makes its polar restriction closed and positive; the smooth remainder has no polar coefficient mass. Thus equality of the fixed Gauduchon traces on each modification is equivalent to equality of those full polar currents. This identifies what the scalar coordinates retain in this regime and does not separate general ordinary models.

Exact classical inputs: Demailly's *Complex Analytic and Differential Geometry*, Chapter III, local-potential discussion and Proposition 1.19, page 135; Lemma 2.2, Theorem 2.3 and Corollary 2.4, pages 138-140. The complete relevant statements, extension proof and cutoff construction were read from the retrieved PDF whose SHA-256 is d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1, identical to the earlier supplied local copy. Poincare/Dolbeault, Richberg smoothing and elliptic regularity remain classical dependencies, not a fresh whole-book audit. The theorem explicitly requires a **closed** complete pluripolar set; it is not cited for an arbitrary nonclosed pole set. The clean manuscript compilation, complete first and second proof reads and all affected output inspections pass. Source-package reconstruction and private synchronization follow the checkpoint 339 release record.

## Remaining obligations before a topology claim

1. Separation is disproved by checkpoint343: a nonzero positive-volume ordinary model and zero have identical first polar currents on every modification.
2. Prove that limits in the complete ambient coordinate space are simultaneously realized by ordinary models. Coordinatewise positive measures and preserved carriers are insufficient.
3. Exact ideal analytic closure fails by the same example: the polar-comparison closure contains the nonideal model. A replacement requires richer data.
4. Compare this pseudometric with the established complete topology under bounded mass and positive lower volume.
5. Control two-sided background changes and degeneration of the background normalization. Smooth-gauge transport after model projection is covered by checkpoint 338; projection of an arbitrary non-model potential is not asserted to preserve its polar data.

In dimension at least two, the manuscript's prescribed-countable-modification obstruction is respected: replacing \(\mathscr R\) by any fixed countable family leaves some analytic ideal models indistinguishable. The present construction uses a collection containing common resolutions and does not reduce that requirement to countably many fixed detectors.

## Auxiliary choices and positive-volume compatibility

Checkpoint 340, Proposition 15.6.22, proves that arbitrary independent Gauduchon choices can fail compatibility even on a common positive-volume sector of analytic ideal models on P2. Fix a rational coefficient a between zero and one and distinct point poles. Each modification contracts curves over only finitely many of those points. Choosing eta_pi=pi*omega+epsilon_pi gamma_pi with the fixed epsilon_pi small enough gives polar distance to zero at most 1/j on all modifications. The denominator is at least one, and contracted curves see only the epsilon term. The single-point blowup and bounded residual Stokes give both singularity volumes 1-a^2, so the upper-volume comparison with zero stays a^2. The complete source/proof reads and exact support theorem checks are recorded in research/editorial/gauduchon-choice-topology-obstruction-340.md. Analytic separation remains valid; auxiliary-form restrictions, general model separation, realization and exact analytic closure remain open.

## Compatible closed-pole current limits

Checkpoint 341 gives arbitrary-pole pushforward in foundation Proposition 1.25.2. Coefficientwise restriction to an inverse-image Borel set commutes with proper pushforward of the full curvature. Proposition 15.6.22 applies this to comparison-Cauchy normalized models with closed poles. Their traces converge in total variation and retain the countable union of pole sets as a null carrier. Positive-current compactness and null-current trace recovery give unique weak full-current limits, and proper pushforward makes them compatible on every stated pair of coordinates. A dyadic sum of the normalized potentials gives one genuine global pole carrier. This does not identify that potential as a realization of the current family, nor assert strong coefficient variation. Both complete revised-input reads and final output checks are recorded in research/editorial/compatible-polar-current-limits-341.md. Before extending beyond closed poles, check the local non-pluripolar first-current closedness proof at its full needed scope. General separation, ordinary-model realization, exact analytic closure and auxiliary-choice compatibility remain separate obligations.

## Arbitrary-pole closedness and trace recovery

Checkpoint 342 reconstructs the complete-pluripolar restriction cutoff argument from the BEGZ author preprint arXiv:0812.3674v2, 9 September 2010, Theorem 1.8, Lemma 1.9 and Remark 1.10. The full closedness and chain-rule proofs and the adjacent local construction were read on PDF pages 4-11. The retrieved 54-page preprint has SHA-256 43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd. This is a scoped author-version proof check, not a fresh read of the published article or the whole source.

On a local ball let a be a negative psh correction of the potential and Theta=ddc a. Bounded psh cutoffs w_k=chi(exp(a/k)) vanish on the pole set and tend to one elsewhere. The differentiated weighted currents have a uniform local energy bound. The derivative of the outer cutoff tends to zero everywhere, including on the pole set; dominated convergence uses the fixed locally finite trace of Theta. Thus the complementary restriction and its polar difference are closed. A smooth correction has no coefficient mass on the pole set. Foundation Proposition 1.25.3 therefore proves closed positive polar curvature for every quasi-psh potential and smooth real background, without requiring that full background current be closed.

Corollary 15.6.13 and Proposition 15.6.22 consequently lose their closed-pole hypothesis. The latter still gives weak current convergence, total-variation trace convergence and one genuine pole carrier, without ordinary-model realization or strong coefficient variation. Earlier closed-pole source checks above retain their historical scope and are superseded by this argument for the current theorem scope. No degree-one non-pluripolar identification or unchecked EK24 proposition is needed. Citation attribution and exact author-version locators are confined to the history chapter. General separation, simultaneous model realization, exact analytic closure and auxiliary-choice compatibility remain open. Final complete source reads, selected output review and empty-source reconstruction pass; see research/editorial/arbitrary-pole-polar-closedness-342.md. Private synchronization follows this snapshot.

## Diffuse product obstruction on every modification

Checkpoint343, Proposition15.6.24, gives a normalized ordinary model p on P1 times P1 in a common positive-lower-volume sector with zero. Its volume is strictly between zero and the smooth background volume A, while all first polar currents vanish on every modification and all-weight multiplier ideals are trivial. Hence p is nonideal, has positive upper-volume distance from zero, and has zero polar pseudodistance from the analytic zero model for every family and choice of forms. This disproves both candidate general separation and exact ideal analytic closure; it is not a closure of full P01/P17.

The local maximum of two diffuse Green potentials has a zero-dimensional joint pole set. Its bounded truncations keep one finite positive top-degree mass supported on levels approaching that set. A small smooth cutoff globalizes it with strict positive curvature and a strict volume deficit. Ordinary projection preserves both volumes. The new Hausdorff trace corollary excludes the polar current away from exceptional curves; the analytic support theorem leaves only those curves. A generic coordinate pullback is a normal power times a unit, and the zero one-variable Lelong number forces every exceptional coefficient to vanish. No exact unbounded divisorial-restriction identity is assumed. Complete proof reads,31 internal checks and final image inspections are recorded in research/editorial/diffuse-product-polar-obstruction-343.md.

Next check the n-fold construction on arbitrary compact Kähler manifolds, then seek richer detectors. Ordinary-model realization of the compatible current limits remains separate and does not restore the separation lost here.

## Arbitrary-dimensional obstruction

Checkpoint 344 generalizes Lemma15.6.8 and Proposition15.6.24 to every compact Kähler manifold of dimension at least two. The local maximum of n curve Green potentials is maximal off K^n, with an explicit zero-dimensional product cover. The covariance rank bound m-1<n replaces the two-branch rank-one argument. Truncations add one constant branch; mixed-product telescoping and strict quadratic comparison give finite positive n-fold mass on deep simultaneous levels. Global strict positivity and ordinary projection give a positive-volume nonideal model with a strict volume deficit.

Fresh complete CADG support Theorems2.10/2.13 and Corollaries2.11/2.14 proofs on actual PDF141–143 justify removing smaller exceptional components and reducing the polar current to divisorial coefficients. Images not contained in the zero-dimensional joint pole set have a regular point where the pulled-back model is bounded. Every other image is a point; transverse coordinate multiplicity and the zero curve Lelong number force its coefficient to vanish. Thus all modifications and all allowed Gauduchon choices remain blind to the model in every such manifold. The earlier343 surface construction retains its historical scope.

This does not close P01/P17 or realize compatible current limits. Next compute exact volume loss along the scaled family using higher-degree closed-current trace growth; that next formula is not asserted by this checkpoint.

## Exact scaled-volume interval

Checkpoint345 extends the Hausdorff trace estimate to closed positive(j,j) currents for1<=j<n. Their weak limits give the zero-dimensional joint pole set no coefficient mass. Bounded closed mixed Stokes, a fixed-parameter finite-degree weak subsequence and the local top mass M give exact NPP loss Mt^n. The zero endpoint is defined separately. Ordinary projection preserves both volumes, and envelope order gives d(p_s,p_t)=M|s^n-t^n|. The parameter Mt^n identifies this restricted family with a complete real interval. All first polar coordinates collapse it, and its positive-parameter members are nonideal. Choosing the endpoint sufficiently small places it in any prescribed cutoff0<delta<A.

No unique top-degree residue distribution, higher-degree all-modification polar invariance, general complete model topology or simultaneous realization is asserted. All full P01/P17 statements stay open. Next check how the local pole loss interacts with lower-degree torsion terms for the same cutoff in a nonclosed Hermitian background.

## Hermitian potential-mass polynomial

Checkpoint346 computes A+sum binomial(n,j)c_j t^j-Mt^n for the displayed cutoff tH in any compact Hermitian background. A local Euclidean closed correction and compactly supported bounded Stokes give uniform traces of every degree. Hausdorff-null coefficient estimates make all lower-degree weak limits unique, so the finite torsion coefficients exist as bounded-truncation limits. The pure top global Hessian has zero integral, while the local top polar mass is exactly Mt^n. The explicit surface formula is A+2t integral H ddc omega-Mt^2. The power identities ddc omega^q=0 remove all lower coefficients.

This is a formula for specified potentials, not invariance over all bounded-equivalent representatives or an ordinary-model volume formula. No unique top residue distribution or higher-degree all-modification invariant is asserted. Full P01/P17 stay open. Next check the bounded-equivalence gap under the Guan–Li power identities.

## Hermitian invariant-mass model interval

Checkpoint347 proves full residual-mass invariance on the zero-dimensional compact common pole set using a decreasing maximum and the compact-set weak-mass bound. The checked Hausdorff-small unbounded-product theorem supplies full products and weighted integrability, distinguished from NPP. For every bounded-equivalent diffuse representative, lower closed powers give zero pole coefficient mass and the top residual is Mt^n. When ddc omega^q=0 for1<=q<n, bounded global mass is A. Subtracting the fixed pole loss proves mass A-Mt^n for every representative and both singularity volumes. Ordinary projection yields the same complete ordered interval, first-polar blindness on all modifications and nonideal positive members as in the Kähler case. Every Gauduchon surface qualifies.

This supersedes the special-regime bounded-equivalence gap recorded at346. Arbitrary Hermitian torsion terms and the complete topology problem remain further tasks. No higher-degree all-modification invariant, general realization or full formal problem closure is asserted.
