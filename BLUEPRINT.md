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

- **Checked release: checkpoint30.** 639 pages, 32 chapters and an appendix. The integrated manuscript and inspected PDF include continuous Bott–Chern representatives, exceptional trace divisors, the compact pseudoeffective cone base, the vanishing-lower-mass threefold, its balanced geometry, and the universal-measure solvability criterion. Five bounded audits passed; their dependencies are discharged. A fresh source extraction reconstructed both outputs with identical page text.
- Upper bounded mass and positive lower mass are independent. A balanced metric with finite upper mass can have zero lower mass. General measure existence therefore cannot omit all lower-mass or right-hand-side restrictions.
- Positive lower mass characterizes solvability for every finite non-pluripolar measure in a Hermitian background, without BMP. Individual L1 data and unbounded exponential equations require separate analysis. Fixed-density volume must remain distinct from its density infimum.
- Linear current continuity and exceptional-divisor formulas do not imply nonlinear volume continuity or full higher-dimensional trace realization.

## Immediate work

1. Keep the checked source package and private GitHub history synchronized after significant updates.
2. Continue chapter polishing, preserving all singularity, I-goodness, trace and Bergman topics.
3. Investigate closed-current descent and Bott–Chern cones on the elliptic lower-mass example; keep proposed deductions outside the checked book until their proofs are reviewed.
4. Seek geometric sufficient conditions for positive lower mass and criteria for individual measures when it vanishes. The full Gauduchon determinant endpoint fails on the example; fixed-density maximizers remain a separate family.

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
