# Gauduchon normalization of polar trace data

Research continuation after manuscript checkpoint 336, based on private source `452b5c0e23ef40ea40f494cf106eb5d9d7cb8de3`.

Status: the elementary comparison, analytic-model separation, curve reduction, raw gauge identity and ambient completeness are integrated in manuscript continuation 337, Propositions 15.6.20 and 15.6.21. The book writes this comparison as \(\delta_\omega^{\mathrm{pol}}\). General separation, realization of limits, analytic closure and compatibility with the established higher-dimensional topology are unresolved. The comparison does not solve P01/P17. No novelty claim or independent external certification is made.

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

For each coordinate, total variation is a norm on finite signed measures. Dividing by the fixed positive \(A_\pi\) preserves symmetry and the triangle inequality. Taking the supremum preserves both. Consequently \(D_\omega\) is a bounded pseudometric. A proof of separation on all ordinary models is still needed; the formula is not called a metric there.

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

This proves separation on analytic ordinary models. It uses the manuscript's existing analytic-resolution and divisorial-restriction inputs, not a fresh external proof audit. For arbitrary ordinary models, scalar traces could lose information carried by the coefficient measures; that issue remains part of the separation question.

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

Exact smooth-gauge transport also holds on genuine potentials. If \(\omega'=\omega+\operatorname{dd}^{\mathrm c}f\) and \(u'=u-f\), then their pulled-back curvature currents and pole sets agree. Distributional Stokes gives \(A_{\pi,\omega'}=A_{\pi,\omega}\), using the same Gauduchon forms. Thus their coordinate comparisons agree. Transport followed by normalized ordinary-model projection is a separate operation. Its effect on these polar traces has not been proved in general.

## Remaining obligations before a topology claim

1. Prove separation on every normalized ordinary model, or find two different models with identical scalar polar traces on all modifications.
2. Prove that limits in the complete ambient coordinate space are simultaneously realized by ordinary models. Coordinatewise positive measures and preserved carriers are insufficient.
3. Identify the closure of analytic models and prove that it is exactly the ideal-model locus.
4. Compare this pseudometric with the established complete topology under bounded mass and positive lower volume.
5. Control ordinary-model projection under smooth gauges and two-sided background changes, and handle degeneration of the background normalization.

In dimension at least two, the manuscript's prescribed-countable-modification obstruction is respected: replacing \(\mathscr R\) by any fixed countable family leaves some analytic ideal models indistinguishable. The present construction uses a collection containing common resolutions and does not reduce that requirement to countably many fixed detectors.
