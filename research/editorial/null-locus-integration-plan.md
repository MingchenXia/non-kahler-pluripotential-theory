# Completed adaptation — 15 September 2026

All ten steps below are implemented in Chapter 30. The Hermitian auxiliary extension also passed its separate mathematical audit. The integration audit accepted the mathematics; its sole stale-checksum finding is resolved in `nakamaye-integration-review.md`. The following text preserves the original plan and must be read as a historical dependency outline.

# Integrating the supplied transcendental Nakamaye proof

The exact supplied 2,046-line source is archived as `research/sources/VX-null-locus.tex`. Its complete audit `transcendental_nakamaye_01` passed. The main agent read the full source, all 46 persisted statement records, all 32 reference records, both the provisional finding and its explicit withdrawal, and the final JSON. This is a source audit, not a completed adaptation or a novelty certification.

The two new Bott–Chern/LCK chapters do not use the supplied main theorem as a premise. The next revision should integrate its proof as a sustained chapter, with the following dependency order.

## Exact regime

The main theorem concerns a pseudoeffective ordinary real Bott–Chern class on a compact connected **Kähler** manifold. Its numerical restricted volume is Collins–Tosatti's smooth-remainder definition. It identifies the non-Kähler locus with the union of positive-dimensional subvarieties having zero numerical restricted volume, first by proving vanishing on irreducible components. It does not say that every subvariety contained in the locus separately has zero restricted volume.

This theorem must not be transferred to arbitrary Hermitian backgrounds. The new zero-class infinite-error-supremum proposition gives a direct obstruction to one naive transfer. Closed bigness on arbitrary compact complex manifolds already forces Fujiki class C, while positive nonclosed backgrounds exist everywhere.

## Chapter structure

1. Recall the numerical restricted-volume definition and the no-isolated-points argument from the new Bott–Chern chapter. State the general theorem, including the non-big convention.
2. State the precise SGPT trace, multiplier-ideal inclusion, P-order rooftop theorem and dS continuity facts in their Kähler regimes. Identify the bridge through CT22's restricted minimal-current non-pluripolar masses; do not identify ac and NPP measures for bounded-remainder potentials.
3. Prove the uniform divisorial-domination lemma: use analytic approximants, nef residual classes on resolutions, a mixed intersection bound computed on the fixed base, Xiao's weak nef-difference criterion, descent and Lelong semicontinuity. Fix the strict-positivity constant before choosing potentials or fine levels.
4. Prove the quantitative regularization lemma with class-independent O(1/m) loss and its **one-sided** multiplier-ideal singularity bound. Keep its conclusion weaker than full analytic type. Explain the holomorphic change of frame, the singular Hörmander correction preserving point evaluation and the cutoff maximum.
5. Prove relative principalization in the explicitly connected ambient setting. Separate image restriction from tensor restriction, use marked ideal order one, and retain the exact transform of the ideal of the submanifold. Prove the small exceptional curvature correction and the collar gluing lemma.
6. Reduce to a smooth component with positive trace mass. Construct the rooftop carrying a uniform positive amount of mass and obtain the strict current on that component.
7. Present the two approximation levels in their actual order: L,C; coarse m; its fixed principalization and correction curvature; then fine dyadic ell and M=C ell; only then the moving modification, exceptional metric and collar constants. A small table of dependencies will help without naming new environments.
8. Prove the multiplier-ideal inclusion by multiplying a locally integrable section and a bounded weighted section. Derive each effective divisor inequality with its correct orientation.
9. Construct the global and local strict currents. Expand the coefficient inequalities that yield an actual bounded-error collar comparison. The comparison is not a consequence of I-equivalence alone.
10. Glue at a smooth point of the component, contradict the modification rule for the non-Kähler locus, and deduce both inclusions of loci, treating non-big classes separately.

## A bounded extension to examine separately

Most of the quantitative regularization proof uses only local geometry and closedness of the background. It is worth checking whether its class-independent O(1/m) lower-bound statement can be proved on an arbitrary compact complex manifold with a Hermitian reference metric. This is a candidate for further verification, not an included theorem. Any use of a local potential for the nonclosed Hermitian error must be replaced by a genuine local quadratic correction; the source's Kähler volume in the Hilbert-space generation statement must also be replaced or compared carefully. A positive answer would extend this auxiliary tool only, not the Kähler trace and numerical-volume machinery or the main Nakamaye theorem.

The original source and all verifier records are unchanged. No result is to be labeled open merely because its proof has not yet been adapted into the book.


15 September, active adaptation: the full chapter and both helper files are now drafted outside the production build. A separate Hermitian regularization audit and a bounded source-to-book integration audit are active. The latter also checks the new self-contained proof of the weak nef-difference criterion through Gauduchon duality. No completed source audit is being rerun.
