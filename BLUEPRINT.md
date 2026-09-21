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

- **Checked manuscript: checkpoint44.** 673 pages, 32 chapters and an appendix. The first systematic root reread covers every chapter and nested proof input; its revisions are integrated. The PDF is compiled and visually checked, with fresh source reconstruction recorded separately. The root-tail/current/trace and divisorial supplements passed bounded audits; all144 checkpoint reports retain their scopes. This pass is not whole-book certification, and the research remains incomplete.
- Upper bounded mass and positive lower mass are independent. A balanced metric with finite upper mass can have zero lower mass. General measure existence therefore cannot omit all lower-mass or right-hand-side restrictions.
- Positive lower mass characterizes solvability for every finite non-pluripolar measure in a Hermitian background, without BMP. Individual L1 subsolutions now have an exact Gauduchon criterion. Under positive lower mass the equation scalar is exactly the global subsolution threshold, and normalized greatest exponential solutions converge in capacity along every L1-convergent subsequence. Exact equations at positive individual thresholds when lower mass vanishes, and zero-threshold exponential existence, remain open. Fixed-density volume must remain distinct from its density infimum.
- Linear current continuity and exceptional-divisor formulas do not imply nonlinear volume continuity or full higher-dimensional trace realization.

## Immediate work

1. Keep the checked source package and private GitHub history synchronized after significant updates.
2. Continue focused correctness and exposition checks after the completed whole-manuscript pass in `research/editorial/chapter-review-20260921.md`. Preserve exact hypotheses when reusing earlier proofs and keep all singularity, I-goodness, trace and Bergman topics. Prioritize the individual-measure obstruction and geometric noncollapse questions.
3. Section29.7 now treats elliptic current, potential/envelope and selected-section descent, the exact boundary volume and its orders, and minimizing Gauduchon forms with unbounded metric roots. All three bounded audits passed. Use these explicit examples to test further geometric statements; no full Bott–Chern-group computation or general boundary-rank theorem is claimed.
4. Sections13.23–13.25 give the attained individual-L1 subsolution threshold, its exact Gauduchon formula, upper semicontinuity and the complete space of admissible density roots. The domain is metric independent. Positive lower mass makes the domain all Ln; finite upper mass makes the root norm alone complete. Section13.29 constructs the greatest exponential solution from any genuine subsolution and gives its zero-exponent scalar limit when the threshold is positive. Under positive lower mass, Section14.8.1 proves the exact threshold equation and capacity convergence along normalized L1-convergent subsequences. The corresponding general problem with vanishing lower mass remains open. Section13.25 identifies the closure of bounded density roots by uniform Gauduchon tails. Section27.11 attains the compact current maximum on that closure, represents all supporting probabilities, and proves threshold trace saturation and rigidity under smooth dual attainment. Neither a singular-current wedge nor exact rough equation existence is inferred. Section27.11.1 characterizes root tails by continuity under bounded logarithmic perturbations in measure. Section29.1.1 bounds the coefficient loss forced by divisors and identifies annihilating maximizing-current clusters. It distinguishes the weak closure of smooth tests from all currents and excludes semipositive divisors whose zero locus carries no density; this applies to every L1 density on the Hopf example. Section13.29.1 now gives a uniform root-tail damping modulus and scalar/total-variation errors, with a separate linear estimate for roots in Lr, r>n. No general capacity conclusion is inferred. A smooth-dual regularity follow-up remains unreviewed. Section14.8.1 identifies the exact threshold and subsequential capacity limit by reusing Chapter14. Section29.1.1 also forces zero fixed-density variational volume for a nef divisor present at the threshold; neither this condition nor the semipositive criterion is a full realization theorem.
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
