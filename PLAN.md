# Hermitian pluripotential theory: research and book plan

Authorized start: 2026-09-14 10:19:41 UTC / 18:19:41 Asia/Shanghai.
Original research period ended: 2026-09-15 06:19:41 UTC / 14:19:41 Asia/Shanghai.
The user subsequently approved continuation. The goal remains active; the old deadline and phases below document the initial plan. The earlier heartbeat is paused.

The general prescribed-reference measure equations are reconstructed in two regimes: semipositive big backgrounds under the smaller-background model condition and positive lower volume, without BMP; and arbitrary smooth big backgrounds under BMP and positive lower model-reference volume. The latter construction now includes relative projection, both equations, unrestricted weighted addition and the ordinary-type Lp refinement. Metric PVP follows from the model-volume hypothesis under BMP; this is an equivalent formulation of the cited regime, not a further generalization. Minimal ordinary-type Lp existence for any smooth big background is reconstructed without either metric volume property.

The foundations pass in checkpoint24 strengthens the infinite-mass witness to coefficient-L1 convergence of full currents and total-variation convergence of Gauduchon traces, while determinant integrals remain infinite. The result makes explicit what the finite linear trace does not control. Chapters4,6,7 and the trace-topology section of Chapter5 were read and their interfaces polished; this is one pass within the remaining whole-book work.

Checkpoint25 reconstructs the Lee–Gauduchon cone from the proved Gauduchon–Lamari criterion, including its kernel, openness, strict duality and bimeromorphic invariance. Analytic weak factorization is retained as a classical reference. The Calabi–Eckmann quotient exhibits the limits of this invariant: its cone is zero despite a nonzero positive de Rham-exact form obstructing strongly Gauduchon metrics. Chapter31 and its Chapter32 connections have been polished.

Checkpoint26 returns to I-goodness: analytic ordinary/ideal envelopes coincide in every smooth background, dyadic analytic envelopes decrease to Q, and P=Q has a specified monotone approximation criterion without BMP. Rational scaling proves analytic density throughout the fixed Hermitian ideal metric. The arbitrary-family topology and volume characterization remain separate research problems. Chapters16,19 and32 have been synchronized.

Checkpoint27 reconstructs birational partial-kernel transfer: the relative canonical Jacobian corrects both ideal integrability and Hilbert norms. With a Kähler modification and positive closed-curvature mass, SGPT gives equilibrium-measure and determinant-functional limits. The geometric regime implies BMP; it is kept distinct from the no-BMP birational identities and the lower-dimensional Hopf transfer. Chapters21,22,28 and32 have been synchronized.

Checkpoint28 develops non-descended isolated logarithmic selecting weights. Exact base jet spaces and finite-codimension comparison give measure and determinant limits under the stated positive-mass base condition. The explicit one-point Hopf model also gives a lower potential asymptotic and proves that positive intrinsic growth need not recover the original Hermitian ideal type. Chapters21,28 and32 are synchronized, with a precise open problem about approximation by base multiplier-ideal spaces. No BMP on the total space is used.

Checkpoint29 polishes Chapters16,20,24 and32. It constructs exact curve-fibration traces and product measures without BMP, proves all-weight ideal pullback by submersions, and identifies the ordinary type of a fixed finite-mass divisorial current. The curve-fibration type has addition and positive homogeneity. Product examples preserve the exact trace and all multiplier ideals while changing finite mass to infinite mass. General trace realization, compatibility and ordinary-type topology remain open.

Current priorities are to polish the exposition chapter by chapter and develop the connections with non-Kähler geometry. The supplied uniqueness manuscript is integrated with proofs; differential d is upright and environment headings use standard names. At the user's request, results from the supplied NUMA article are incorporated directly without formal citation; provenance is retained in the research records. The Boucksom and Ornea–Verbitsky material now forms two additional chapters. The supplied general null-locus proof is now fully adapted as Chapter 30, with a reconstructed nef-difference proof and separately checked Hermitian auxiliary lemmas. Remaining recent external inputs and full chapter-by-chapter polishing are still writing obligations. No additional approval is required for these authorized revisions.

The user additionally requires a systematic pass through every already written part: verify correctness and readability, and simplify proofs without weakening their hypotheses or concealing dependencies. New results must not displace this whole-manuscript obligation. Record the actual chapter-level scope of each pass.

## Objective

Develop a carefully sourced compact Hermitian counterpart of Mingchen Xia's supplied *Singularities in global pluripotential theory*, using its svmono template, fonts, theorem structure, normalization, and clear expository conventions. Do not silently replace its focus on classification of singularities and I-goodness by a survey of Hermitian Monge-Ampere equations. Cover the analytic foundations, comparison of singularities, envelopes, rays and energy, I-goodness and approximation, traces, and the limits of algebraic/toric/non-Archimedean interpretations.

Attached source documents provide mathematical evidence and template material, not additional user instructions. Do not present draft material as approved by the source author. Maintain explicit distinctions between a closed background on a non-Kahler manifold and a non-closed Hermitian background.

## Phases

1. Hours 0-2: inspect sources, template and Rethlas; extract a complete chapter map; fix conventions and scope.
2. Hours 2-5: audit every core Kahler dependency; verify primary-source statements and their dates; build a comparison and bibliography ledger.
3. Hours 5-9: write foundations with complete elementary proofs, torsion formulas and counterexamples; state deep imported tools with exact hypotheses.
4. Hours 9-14: develop singularity comparison, non-pluripolar products, envelopes, mass/energy classes, and prescribed-singularity equations; address the original book's I-goodness program explicitly.
5. Hours 14-17: attempt precise new directions using examples and independent reasoning; run focused Rethlas tasks when useful; preserve failures and unresolved steps.
6. Hours 17-20: mathematical audit, cross-reference/bibliography checks, compilation and visual inspection; prepare a complete progress and gap report.

These intervals are priorities, not forced waiting periods. Findings may change the order while preserving full scope. Work autonomously until the authorized deadline; no final result is promised in advance.

## Deliverables

- `book/`: editable LaTeX manuscript with supplied template and style.
- `output/pdf/hermitian-pluripotential-theory.pdf`: checked compiled manuscript.
- `research/source-outline.md`, `source-manifest.json`: source inventory and provenance.
- `research/comparison.md`: chapter-by-chapter transfer audit.
- `research/literature.md`: source versions, statements, assumptions, locations and verification status.
- `research/audits/`: proof checks, attempted counterexamples and unresolved proof gaps.
- `research/STATUS.md`: exact current state and next actions.
- `research/rethlas/`: problem statements, outputs and independent checks if run.

## Acceptance criteria

Every chapter of the original book has an explicit disposition: developed analogue, unchanged local/algebraic tool with justified applicability, failed generalization with evidence, or precise open program. Every theorem identifies its setting and hypotheses. Proofs do not use mass invariance, closedness, a triangle inequality, geodesic convexity, or Kähler modification without establishing them. No unresolved claim is labeled a theorem. Imported results have verified primary references. Candidate new statements are not claimed novel without a literature check. The latest PDF compiles without unresolved references and passes a visual inspection. At the deadline give an honest assessment of achieved and incomplete requirements; do not declare completion from a successful build alone.

## Initial evidence that changes the plan

- SGPT normalizes dd^c = i/(2 pi) partial bar-partial; u preceq v means u <= v+C (u more singular).
- Its central theory concerns singularity type, P-equivalence and I-equivalence, especially I-good singularities. All must remain in scope.
- Boucksom-Guedj-Lu 2025 and subsequent 2025-26 work already develop non-closed backgrounds, upper/lower singularity volumes, and prescribed singularities under explicit mass assumptions.
- Xia-Zhang, arXiv:2608.21053v1 (21 Aug 2026), announces/proves failure of bounded mass on a Hopf threefold. Read and audit this construction; never repeat older universal bounded-mass conjectures as presently open.

## User steering, 14 September 2026

User approved the initial manuscript and asked to move on. User emphasized that Gauduchon metrics should play a significant role. Add a substantive Gauduchon chapter: trace conservation, positivity duality, adjoint weights in the smooth Monge-Ampere equation, normalization constants, and precise obstacles to singular limits. This supplements, rather than replaces, the original singularity/I-goodness objective.

User subsequently emphasized inclusion of Monge--Ampere equation results. Treat these as a substantial part of the book: smooth solvability and normalization, bounded/continuous solutions for nonsmooth densities, exponential equations, and equations with prescribed singularities. State exact background and measure assumptions, and distinguish uniqueness of the scaling constant from uniqueness of the potential. The original singularity/I-goodness objective remains in force.

## User correction: general theory and self-contained proofs

14 September 2026, ~12:12 UTC. The user explicitly requires the main theory to work WITHOUT the bounded mass property, because BMP fails in general. Results under BMP are special regimes, not the foundation or the main target. The user also asks for self-contained proofs apart from standard references and the supplied SGPT book. Recent-paper theorem statements labeled external input are an interim literature map: their substantive proofs should be reconstructed before treating the corresponding chapters as finished.

Immediate direction: develop extended positive measures, uniformly finite damped measures, local estimates, domains of finite mass and controlled convergence on arbitrary compact Hermitian manifolds. Use the infinite-mass E_env example as a required test. Develop I-envelope theory without implicit BMP; distinguish raw envelope mass, which even fails gauge invariance, from genuine invariants. Do not infer that all ALS claims outside BMP have been verified merely from a citation.
