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

- **Checked release: checkpoint29.** The 621-page book has 32 chapters and an
  appendix. Its source is in `book/`. Compilation and independent reconstruction
  are recorded in `research/audits/build-snapshot-29.json` and
  `research/audits/source-package-portability-29.json`.
  The 21 September cover correction removes the two-line preparer credit; all
  body pages are unchanged. Its checks are in
  `research/audits/cover-revision-2026-09-21.json`.
- **Pending checkpoint30:** continuous Bott–Chern representatives and corrected
  exceptional-divisor/affine-class/compact-cone drafts have passed their bounded
  independent audits. Their exact hypotheses and the rational analytic coefficient
  correction are preserved. They await integration and final output inspection.
- **New lower-mass material:** the supplied counterexample has a complete
  reconstruction under independent review. Two additional drafts develop the
  equivalence between positive lower mass and universal non-pluripolar solvability,
  and the quotient metric's balanced property, finite upper mass and geometric
  obstructions. The latter deductions have their own bounded reviews. None has
  replaced the checked release. Correct the original Siu locator to Main Theorem,
  p.53, using the verified published scan; preserve the original submission.

## Immediate work

1. Complete and read the three lower-mass audits. Verify the measure-diagonal
   argument for arbitrary singular candidates, every normalization in the geometric
   example, and the balanced/upper-mass calculation. Keep conditional dependencies
   explicit until each premise is reviewed.
2. Replace the obsolete universal positive-lower-volume question by questions
   about sufficient geometry, admissible individual measures, and unbounded
   exponential equations. Keep fixed-density volume separate from its density
   infimum. The preliminary preview already contains the corresponding interfaces.
3. Inspect the combined preview, integrate reviewed statements, compile and
   reconstruct the source archive before declaring checkpoint30 checked.
4. Continue the chapter-by-chapter proof and exposition pass with the entire SGPT
   singularity, I-goodness, trace and Bergman scope retained.

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
