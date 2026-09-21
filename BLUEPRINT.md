# Blueprint: singularities in Hermitian pluripotential theory

This is the living research blueprint. `PLAN.md` preserves the original scope and
subsequent user directions; `research/STATUS.md` records exact continuation details;
`CHANGELOG.md` and Git commits preserve changes. The project remains incomplete.

## Aim and conventions

Develop a self-contained compact Hermitian counterpart of Mingchen Xia's
*Singularities in global pluripotential theory*, preserving the supplied template
and style. The main theory must not assume bounded Monge–Ampère mass. Gauduchon
metrics, Monge–Ampère equations and connections to non-Kähler geometry are central,
alongside singularity comparison, envelopes, I-goodness, traces and partial Bergman
kernels. Use standard theorem environments and upright differential d. Clearly
distinguish proved results, external inputs, conditional results and open problems.

## Current manuscript and proof boundary

- **Checked manuscript: checkpoint56.** 687 pages, 32 chapters and an appendix. The first systematic root reread covers every chapter and nested proof input; its revisions are integrated. The PDF is compiled and visually checked, with fresh source reconstruction recorded separately. The root-tail/current/trace and divisorial supplements passed bounded audits; all 154 checkpoint reports retain their scopes. Checkpoint56 adds the finite-divisor parameter-family consequence, shortens the mass-extrema and mass-invariance proofs, and completes the second focused reading of Chapters1–5. The second pass over Chapters29–32 and the appendix was recorded at checkpoint55. This pass is not whole-book certification, and the research remains incomplete.
- Upper bounded mass and positive lower mass are independent. A balanced metric with finite upper mass can have zero lower mass. General measure existence therefore cannot omit all lower-mass or right-hand-side restrictions.
- Positive lower mass characterizes solvability for every finite non-pluripolar measure in a Hermitian background, without BMP. Individual L1 subsolutions now have an exact Gauduchon criterion. Under positive lower mass the equation scalar is exactly the global subsolution threshold, and normalized greatest exponential solutions converge in capacity along every L1-convergent subsequence. Exact equations at positive individual thresholds when lower mass vanishes, and zero-threshold exponential existence, remain open. Fixed-density volume must remain distinct from its density infimum.
- Linear current continuity and exceptional-divisor formulas do not imply nonlinear volume continuity or full higher-dimensional trace realization.

## Immediate work

1. Keep the checked source package and private GitHub history synchronized after significant updates.
2. Continue focused correctness and exposition checks after the completed whole-manuscript pass in `research/editorial/chapter-review-20260921.md`. Preserve exact hypotheses when reusing earlier proofs and keep all singularity, I-goodness, trace and Bergman topics. Prioritize the individual-measure obstruction and geometric noncollapse questions.
3. Section29.7 now treats elliptic current, potential/envelope and selected-section descent, the exact boundary volume and its orders, and minimizing Gauduchon forms with unbounded metric roots. All three bounded audits passed. Use these explicit examples to test further geometric statements; no full Bott–Chern-group computation or general boundary-rank theorem is claimed.
4. Sections 13.23–13.29 identify the attained individual-L1 subsolution threshold, its Gauduchon formula, the complete density-root space and greatest exponential solutions. Root tails give quantitative scalar and total-variation errors. Section 14.8.1 identifies the exact threshold and subsequential capacity limit under positive lower mass. The exact equation at a positive individual threshold when lower mass vanishes remains open in general.

   Section 27.11 attains the compact dual problem under root tails and represents all supporting probabilities. Its smooth-dual theorem instead assumes a smooth strictly positive maximizer: in dimension at least two this forces a smooth exact threshold equation, uniqueness and whole-family uniform convergence of normalized exponential solutions. Closed backgrounds force strict positivity of the density; an explicit nonclosed construction allows an open zero set on every compact complex manifold. A smooth semipositive maximizer strictly positive outside a proper analytic set also gives the exact global equation and local smoothness. A maximum argument makes the possible divisorial differences nonpositive; Gauduchon Stokes then forces them to vanish. All threshold subsolutions are therefore unique modulo constants, without prescribing ideals or assuming independence of divisor classes. The positive pole-divisor classes are linearly independent. Sections27.11.5–27.11.7 also give whole-family normalized exponential L1 convergence, a fixed lower barrier and b<=c_lambda<=b exp(C lambda). The full Gauduchon traces converge at rate O(lambda) in total variation, and full currents at rate O(sqrt(lambda)) in coefficient total variation on compact subsets off the degeneracy set. A genuine smaller-background envelope for the threshold solution additionally gives whole-family capacity convergence; a bounded threshold solution satisfies this condition. For Lp data with p>1 the solution is continuous and the whole exponential family converges uniformly. A projective square-map example has a smooth potential and a density root that is not differentiable on its analytic zero set. Automatic genuineness and global regularity for general L1 data across the degeneracy set remain open here. General singular-current attainment gives none of this regularity by itself.

   Section 29.1.1 gives divisorial coefficient loss and annihilating maximizing-current limits. It distinguishes the smooth-test closure from all currents, excludes suitable semipositive divisors, and forces zero fixed-density volume for a nef divisor present at the threshold. A full divisor realization theorem is still missing. For a finite divisor whose residual background admits a smooth positive representative, and a smooth strictly positive probability measure, Theorem27.19.1 now gives smoothness and uniqueness modulo constants for every threshold subsolution with at least the prescribed divisorial coefficients. Ordinary-type solutions have the same scalar and smooth remainder. General degenerate residual backgrounds and densities pulled back through modifications remain outside this result. Proposition27.19.2 gives smooth dependence of the normalized remainders, capacity and measure convergence, and exact all-model logarithmic coefficients for fixed finite divisor support while the limiting residual background remains positive. Multiplier ideals can still jump at integer coefficients; arbitrary envelope-system recovery remains open.

5. Seek geometric sufficient conditions for positive lower mass and criteria for individual measures when it vanishes. The full Gauduchon determinant endpoint fails on the example; fixed-density maximizers remain a separate family.

## Longer research directions

- Realize arbitrary higher-dimensional trace profiles on all compact models.
  Analytic and curve-fibration cases are established special cases; a fixed-model
  divisorial ordinary type does not recover every exceptional coefficient.
- Develop a topology on ordinary singularity types with a meaningful volume
  interpretation and explicit separation between ordinary and ideal envelopes.
- Extend arbitrary-big model-reference equations beyond bounded mass. Linear
  Gauduchon trace control alone does not give nonlinear mass integrability.
- Study lower partial Bergman asymptotics, positive-volume recovery and the loss
  of singularity information under descent.
- Connect compatible divisorial classes, null/non-Kähler loci, Gauduchon cones,
  bigness and geometric problems without importing Kähler hypotheses silently.

`research/comparison.md`, `research/proof-obligations.md` and
`research/literature.md` give the detailed subject map, proof obligations and
versioned literature evidence. Preserve the full original-book scope while these
priorities evolve.

## Repository workflow

The private repository is
<https://github.com/MingchenXia/non-kahler-pluripotential-theory>.
Substantive changes receive descriptive commits and a short changelog entry.
Pending research is saved with its actual status; a Git commit is not a proof
certification. Commit and push at each significant milestone, with an hourly
synchronization check as a fallback. See `AGENTS.md` and
`scripts/sync-github.py`. Generated PDFs and source archives remain local and can
be rebuilt; downloaded reference texts and raw verifier runtime files are excluded.
