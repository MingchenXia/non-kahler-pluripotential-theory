# Reading the Hermitian manuscript

The book distinguishes a closed background on a compact complex manifold from a nonclosed Hermitian background. The latter already gives new phenomena on a projective manifold. Bounded mass is not a standing assumption.

## Three routes through the book

**For the main framework:** read Chapters 1–8, then 12–14. The sequence is torsion-dependent mass, the conserved Gauduchon trace, extended non-pluripolar measures, finite damping, and the distinction between an envelope class and a finite-mass class. The Hopf example tests every proposed general mass bound. Section6.8 refines the infinite-mass construction: the full current has integrable coefficients and smooth approximants converge in coefficient L1, but their determinant masses diverge. Its small multiples have Gauduchon traces converging in total variation while their extended mass stays infinite. Read this alongside Section7.5, where the same potentials converge in capacity and their finite damped measures converge.

**For equations and Gauduchon metrics:** read Chapters 4, 9–11, 13–15, 27 and 30–31. These cover conformal and adjoint equations, smooth and weak Monge–Ampère solvability, degenerate uniqueness, prescribed singularities, weak supporting probabilities and a finite variational volume. The prescribed Gauduchon-volume equation includes its nonlinear estimates.

**For the SGPT singularity program:** read Chapters 12 and 16–28, then Chapters 29–32 for closed singular loci, the Nakamaye proof, LCK geometry and remaining questions. Ordinary type, envelope equivalence and multiplier-ideal equivalence are kept distinct. Curve traces, explicit fibrations and finite divisorial systems provide test cases; their identities are not asserted in every dimension or background.

## Lower mass, equations and the elliptic example

Read Section13.22 for the exact equivalence between positive lower mass and normalized solvability for every finite non-pluripolar measure. The diagonal-density proof allows arbitrary singular candidates and infinite mass. Its counterexample density has a positive lower bound but belongs to no Lp,p>1; obstructing densities are L1 dense. Smooth and Lp existence, and unbounded exponential solvability, are separate issues.

Section27.16 reconstructs the elliptic threefold with zero lower mass for every Hermitian metric. Its explicit balanced metric has finite upper mass24pi and a vertical Dirichlet formula. The smooth positive ddc-exact(2,2)-form excludes pluriclosed metrics and closed Kähler currents. Compare with the Hopf example to see the independence of the two mass properties. Section32.5 replaces the former universal-positivity problem by sufficient-geometry and fixed-density questions.

For linear geometry, read Sections24.8–24.9, Corollary25.2.1 and Proposition29.1.2. Continuous Gauduchon-normalized representatives control pullback on a fixed modification. Finite exceptional divisors describe the exact change of canonical divisorial ordinary types, including a cocycle and total-variation approximation. The compact cone base is linear; none of these statements asserts nonlinear mass continuity.

## Individual densities: thresholds, equations and limits

Sections13.23–13.25 start with a nonzero nonnegative L1 density f. Its threshold b_h(f) is the largest scaled density dominated by an extended Monge–Ampère measure, and that subsolution threshold is attained. The Gauduchon formula computes it exactly. Positivity of the threshold alone does not yet give a general exact equation when lower mass vanishes.

The root space has two distinct norm components, Ln and rho_h. Positive lower mass makes every Ln root admissible. Finite upper mass makes rho_h control the Ln norm. The closure of bounded roots is characterized by uniform Gauduchon tails. Section27.11 uses those tails for compact current attainment and supporting probabilities; a compact current maximizer need not be smooth.

| Additional hypothesis | Proved conclusion |
|---|---|
| f belongs to Lp, p>1 | A continuous exact equation with scalar b_h(f); normalized positive-exponent solutions are uniformly precompact. Uniqueness of their limits needs a further argument. |
| Positive lower mass | An exact threshold equation in the minimal envelope class for every such L1 density. Section14.8.1 gives capacity convergence along each normalized L1-convergent subsequence. |
| Uniform root tails, in dimension at least two | Attainment in the compact Gauduchon current problem. Section13.29.1 gives scalar and total-variation errors for exponential damping, without a general capacity conclusion. |
| A smooth strictly positive current maximizer, in dimension at least two | Every genuine threshold subsolution is smooth and exact, with uniqueness modulo constants. The whole normalized positive-exponent family converges uniformly. |
| A smooth semipositive maximizer positive off a proper analytic set, in dimension at least two | The exact threshold solution is unique modulo constants and smooth off that set. The whole normalized exponential family converges in L1 with a fixed lower barrier and b<=c_lambda<=b exp(C lambda). |

The smooth-attainment rows use the trace equality and a local first-order regularity argument, not a mass bound. In a Kähler background, smooth strict positivity of the density is equivalent to smooth strictly positive dual attainment. A nonclosed background can behave differently: Example27.11.1 constructs, on every compact complex manifold of dimension at least two, a Hermitian background and a density vanishing on an open set with a smooth strictly positive maximizing test. Read this with the Chapter11 nonuniqueness examples; the zero set alone does not decide uniqueness.

## Analytic approximation and I-goodness

Read Section16.5 for the elementary ideal metric and its curve completion, then Section16.6 for what dyadic approximation preserves. Local analytic domination and the discrepancy estimate give monotone ordinary-envelope convergence to Q without BMP or bigness. The equality P=Q is equivalent to convergence of these envelopes to P. Rational scaling in a Hermitian background gives analytic density in the entire ideal metric, so that density alone is not the source characterization. Chapter19 states the exact global regularization input; Section16.7 and Section32.9 distinguish this proved criterion from a convergence theory for arbitrary ordinary types.

## Partial kernels and their growth dimension

Chapter28 separates the ideal selecting a section space from the continuous weight in its norm. Read the general upper envelope bound and finite determinant calculus first. Section28.6 reconstructs the adjoint multiplier-ideal transformation, all-weight ideal-order invariance, closed-background envelope descent and the exact kernel-measure pushforward formula. The fixed auxiliary bundle is the relative canonical bundle, with a metric defined from the two smooth volumes.

A Kähler modification then allows SGPT Theorem14.3.1 to give the full-dimensional equilibrium-measure and determinant limits. That geometric assumption implies BMP; only the preceding birational identities are unrestricted. Sections28.7–28.9 use a different mechanism: smooth submersion and fiber probabilities, with the intrinsic lower growth dimension. In the Hopf example all potentials positive against the closed line-bundle curvature already descend; weights positive only against the Hermitian form may vary on fibers. Neither measure theorem alone proves the general lower Fubini–Study bound.

Sections28.10–28.11 then allow non-descended isolated logarithmic poles. Read the exact radial integrability threshold, base point-vanishing formula and jet quotient estimate before the kernel limit. The base positive-mass reference remains a hypothesis. The one-point Hopf calculation proves potential convergence separately by binomial entropy bounds and identifies the envelope by a complex-line maximum principle. Its figure compares finite kernels and potentials with the explicit limits. Pole positions within a fiber can be lost despite positive intrinsic growth. Problem32.12.2 asks for geometric criteria giving base multiplier-ideal approximations with codimension o(m^q); neither this approximation nor potential convergence is asserted for arbitrary selectors.

Sections20.8–20.9 give exact higher-dimensional traces over an ambient curve problem under a smooth connected-fiber holomorphic submersion. A Green pullback realizes every compact-model divisor order and its ordinary type is independent of a sufficiently large background. A product formula for extended Monge–Ampère measures includes infinite total mass and gives separated Lp equations. Products with a factor failing BMP have finite- and infinite-mass representatives with all the same multiplier ideals and exact trace numbers. Corollary24.5.1 combines the Gauduchon mass bound with a smooth residual current to determine a canonical ordinary type on each fixed model; this alone does not recover the trace data on further modifications.

Read the divisorial-domination lemma before the fibration theorem: smooth residual curvature makes ordinary domination follow from the divisor coefficients. The multiplier-ideal pullback proof uses local Taylor coefficients and Krull intersection. The product proof first treats bounded potentials, then increasing plurifine rectangles and sigma-finite measures. A bound for top-degree mass is never substituted for these arguments.

## The general-measure proof

In Chapter13, Sections13.17–13.19 treat arbitrary smooth big backgrounds without BMP or PVP. Read local comparison and strict pole-barrier domination, then the reciprocal subsolution and singular Gauduchon trace. Resolution reduces the approximate equations to the already proved semipositive bounded case. The final envelope argument establishes minimal ordinary-type Lp existence for both positive and zero exponents. The normalized equation has a unique positive scalar; its potential may fail to be unique.

Chapter14 now proves both equations for arbitrary reference singularities satisfying the stated model condition, in a semipositive big background with positive lower volume. Start with finite-measure domination, then read the auxiliary-envelope proof of zero-domination without a finite-mass assumption. This supplies the common-envelope capacity criterion. Moving bounded reference measures, the minimal-reference equation and three density approximations complete the proof. The zero-exponent conclusion gives a unique positive scalar, not a unique normalized potential.

Sections14.12–14.14 allow a non-semipositive big background under BMP and positive lower reference volume, proving finite rooftops, domination, fixed-measure continuity and the first-moment and self-measure capacity criteria. Sections14.15–14.17 then prove higher moments, local radial smoothing, and both general NPP measure equations for the minimal reference. Read the moving-integral and raw-tail steps separately. Both metric volume properties imply the required positive lower minimal volume.

Sections14.18–14.19 prove weighted limits with a common relative lower bound and then addition in an arbitrary prescribed class. Follow the four stages: minimal ordinary type, prescribed ordinary type, one ordinary-type input, and bounded-carrier domination. The undamped weighted measure may have infinite mass.

Sections14.20–14.23 complete the arbitrary-model proof: first construct a rooftop across reference classes and a relative projection, then maximize weighted supersolution mass. General-measure existence in turn removes the addition theorem's input restrictions. Finally a concave-envelope moment estimate starts in E_phi and proves ordinary type for Lp data. Throughout this part BMP and positive lower model volume remain in force. These imply metric PVP by lower-volume monotonicity; its omission as a separate assumption is not a stronger theorem.

## Closed classes and LCK geometry

Chapter 29 develops Boucksom’s ordinary Bott–Chern non-nef and non-Kähler loci, including attainment and the absence of isolated non-Kähler points. It states the classical and numerical null-locus definitions in their exact regimes. A direct Hermitian-error volume supremum is infinite even in the zero class on the Gauduchon Hopf example.

Chapter 31 starts with Lee forms and the Kähler covering, proves the Gauduchon harmonicity and degree identities, and separates ordinary from twisted potentials. It shows that the Hopf background is Vaisman and that strict LCK manifolds have no big ordinary Bott–Chern class. Its equation part retains the Lee/anti-Lee symmetry and nonzero-Lee assumptions of the Vaisman volume theorem. The Chern–Ricci-flat Gauduchon rigidity proof is supplied in full. Section31.8 derives the Lee–Gauduchon cone from Gauduchon–Lamari tests, proves its bimeromorphic invariance, and computes the positive half-line on the Hopf example. Read its last subsection for the limitation: an explicitly constructed Calabi–Eckmann threefold has zero cone but a positive de Rham-exact form obstructing strongly Gauduchon and balanced metrics. The kernel in the duality formula and the smaller image of j_X are essential. Lee-curvature positivity, twisted-volume uniqueness and the Calabi–Yau/Vaisman existence conjecture remain explicit questions.

Chapter 30 develops the supplied Vu–Xia proof in full. Its main theorem concerns ordinary pseudoeffective Bott–Chern classes on compact connected Kähler manifolds. Read the strategy and dependency table before the two-level ideal construction. A self-contained weak nef-difference argument explains how the smooth Monge–Ampère equation and Gauduchon duality supply bigness. The quantitative regularization and global ideal-potential lemmas hold with a Hermitian reference metric; the background in the former is still closed, and its singularity estimate is one-sided. The final section locates each remaining Kähler dependence.

## Uniqueness, counterexamples and selection

Chapter 11 collects positive uniqueness results and counterexamples. Read their hypotheses separately:

| Regularity or background | Sufficient condition or result |
|---|---|
| C1,1 potentials, continuous density | Extrema localization; uniqueness if the positive-density region is connected. |
| C2 potentials | Weighted cofactor identities and propagation. On every Hermitian surface, uniqueness for continuous density positive on a dense set. |
| W2,n potentials, n = 2 or 3 | Integrated rigidity for density positive almost everywhere; an additional torsion sign is required in dimension three. |
| C2 potentials, C1,1 density | A square-root sublevel criterion; inverse square-root integrability is sufficient. |
| Guan–Li equation background | Bounded uniqueness for nonzero nonnegative Lp density, p > 1. |
| Genuine threshold subsolutions, dimension at least two | A smooth strictly positive Gauduchon current maximizer forces smoothness and uniqueness modulo constants; see Section27.11.3. |
| Genuine threshold subsolutions, dimension at least two, smooth semipositive maximizer positive off a proper analytic set | Section27.11.4 gives the exact equation, smoothness off that set and uniqueness modulo constants for all threshold subsolutions. The proof uses maxima, the current support theorem and Gauduchon Stokes. Sections27.11.5–27.11.6 give the normalized exponential L1 limit and independence of positive pole-divisor classes. |

Smooth densities with infinite-order or exactly quadratic zeros on two real hypersurfaces admit uncountably many normalized smooth solutions. A further construction prescribes a real analytic density with two distinct smooth solutions in every dimension at least three. It proves sharpness of the inverse-power threshold; its positive-density region has three components.

Chapter 14 puts the analytic-density example in the minimal envelope class, with positive lower and finite upper volume. The scaling constant is still unique. Thus this envelope condition does not ensure uniqueness of the normalized potential.

The standalone note in `output/pdf/numa-thin-zero-set-note.pdf` includes the full smooth background construction and both hypersurface extensions. The analytic-density example and broader positive criteria are in the book. The supplied results are incorporated directly with proofs, without formal citation to the supplied manuscripts; provenance remains in the research records.

For the **original symmetric density**, Chapter 13 proves that the whole normalized positive-exponent family converges uniformly to an explicit symmetric C1,1 solution. The positive-exponent solutions fail to be C2 at two transition hypersurfaces inside the zero-density band. This selection theorem has not been extended to the modified densities.

## Four distinctions to retain

| Statements that can be confused | What the manuscript establishes |
|---|---|
| Finite trace and finite top-degree mass | Even coefficient-L1 convergence of full currents and total-variation convergence of their Gauduchon traces can coexist with infinite determinant integral and infinite extended Monge–Ampère mass. |
| Uniqueness of a scalar and of a potential | The zero-exponent scaling constant can be unique even when normalized smooth solutions are not. |
| Measure representation and equation existence | A prescribed-type carrier represents a finite measure with an integrable density, but the carrier can be unbounded and have infinite mass. The bounded subsolution theorem cannot simply be applied to it. |
| Known theorem and open problem | Both stated prescribed-reference general-measure regimes are reconstructed, including arbitrary big backgrounds under BMP and positive lower model volume. The general extension beyond BMP, arbitrary higher-dimensional trace realization and general I-goodness equivalences require further mathematical work. |

## Remaining work

Chapter 32 relates analytic questions to bigness, the Fujiki class, null loci, Chern–Ricci flow, balanced and pluriclosed metrics, and Morse inequalities. The open uniqueness question now concerns extension of the connected-positive-region criterion to bounded potentials. General selection is also unresolved.

`proof-obligations.md` gives the proof boundary; `comparison.md` maps the original book's subjects; `literature.md` records primary versions and assumptions. The first systematic root reread covers all32 chapters, their nested inputs and the appendix. Subsequent additions have focused reviews, whose exact scope is recorded in research/editorial/chapter-review-20260921.md and the individual review files. This is not a claim of whole-book certification; correctness and exposition work continue.
