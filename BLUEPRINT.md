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

- **Checked manuscript: checkpoint33.** 651 pages,32 chapters and an appendix. Chapters1–12 have completed the first systematic root reread and their revisions are integrated. The earlier elliptic results retain their three bounded audits. The PDF is compiled and visually checked; fresh source reconstruction is recorded separately. The full book review and research remain incomplete.
- Upper bounded mass and positive lower mass are independent. A balanced metric with finite upper mass can have zero lower mass. General measure existence therefore cannot omit all lower-mass or right-hand-side restrictions.
- Positive lower mass characterizes solvability for every finite non-pluripolar measure in a Hermitian background, without BMP. Individual L1 data and unbounded exponential equations require separate analysis. Fixed-density volume must remain distinct from its density infimum.
- Linear current continuity and exceptional-divisor formulas do not imply nonlinear volume continuity or full higher-dimensional trace realization.

## Immediate work

1. Keep the checked source package and private GitHub history synchronized after significant updates.
2. Carry out the systematic whole-manuscript correctness, readability and proof-simplification pass in `research/editorial/chapter-review-20260921.md`. Chapters1–12 have completed this root pass and the revisions are integrated. Continue the partially read Chapter13. Preserve all singularity, I-goodness, trace and Bergman topics.
3. Section29.7 now treats elliptic current, potential/envelope and selected-section descent, the exact boundary volume and its orders, and minimizing Gauduchon forms with unbounded metric roots. All three bounded audits passed. Use these explicit examples to test further geometric statements; no full Bott–Chern-group computation or general boundary-rank theorem is claimed.
4. A research-only note tests individual L1 densities against smooth normalizers. It gives a necessary obstruction and a bounded Kähler example showing that the test need not recover the equation scalar; no sufficiency is asserted.
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
