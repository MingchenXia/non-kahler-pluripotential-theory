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
- **Pending checkpoint30:** four proof drafts under `research/editorial/` develop
  continuous Gauduchon-normalized Bott–Chern representatives, pullback of countable
  divisorial currents, exceptional divisors between trace models, affine class
  identities and compact bases of the pseudoeffective cone. These drafts have not
  replaced the released chapters. The two initial Rethlas runs were interrupted
  by usage exhaustion; neither has a final report. Use the corrected
  `section_trace_exceptional_divisors_v2.tex` for further review, preserving v1.
- **New supplied paper:**
  <https://mingchenxia.github.io/Papers/volinf0_vibe.pdf> claims a compact complex
  threefold with zero lower Hermitian Monge–Ampère mass. It has been downloaded,
  but its full proof has not yet been checked or integrated. Do not describe that
  claim as a verified theorem of this book before completing the review.

## Immediate work

1. Read and audit the new lower-mass counterexample. Track its normalization,
   Gauduchon cone separation, concentration argument and Hermitian Calabi–Yau step.
   Revisit every claim or open problem about universal positive lower mass, and
   retain the precise positivity assumptions needed by equation results.
2. Complete the interrupted checkpoint30 audits through normal authorized Rethlas
   execution. Preserve the audit history and rational-coefficient correction.
   Review the four proof drafts and all affected chapter interfaces.
3. Integrate only appropriately reviewed claims, compile, inspect affected pages,
   and produce a new checked release with reproducible source and audit records.
4. Continue a chapter-by-chapter exposition and proof pass across the entire book.

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
