# Vaisman prescribed volume — checkpoint183

Baseline: `9b15c6af1dc9c961e64a6090628564956bc79756`. The preceding turn completed and privately synchronized the source/proof reconciliation, so it was progress. The checked manuscript baseline is checkpoint181; checkpoint182 changed research records only.

## Mathematical change

Theorem 28.4.1 now has an internal existence and uniqueness proof. Its statement is unchanged: the original metric is strictly Vaisman by the chapter's definition, the prescribed smooth positive volume is invariant under both distinguished flows, and its integral agrees with the original volume. No new case or novelty claim is added.

The proof uses the smooth Hermitian equation already proved as `thm:tw-smooth`. Pullback by either flow preserves the normalized equation, so uniqueness makes its potential basic. With `eta = kappa_lambda`, the difference of two transverse top powers is an exact form after wedging with `lambda wedge lambda^c`: the extra Stokes term has transverse degree greater than the transverse dimension. This fixes the normalization scalar.

The new Lee form is `lambda - du`. Its curvature is `eta + ddc u`; adjoining its positive leafwise term produces the required Hermitian metric and preserves the volume pointwise. Its Lee form is closed and its metric dual is Killing. Symmetry and skew-symmetry of the covariant derivative then prove parallelness directly.

For uniqueness, exact semipositive transverse forms have the same one-dimensional complex kernel: otherwise their sum has positive top power somewhere, contradicting its zero integral. The corresponding holomorphic fields differ by a constant complex multiplier. Cohomology of the Lee forms and boundedness along their complete flows determine that multiplier and make their difference potential basic. The contraction formula retains the candidate metric's scale. Transverse integration determines that scale before the basic maximum principle identifies the metrics.

The factor is `tau = |lambda|_g^2/(4 pi)` in this book's convention. The Hopf identity `omega = kappa_lambda + lambda wedge lambda^c` gives `|lambda|_g^2 = 4 pi`, agreeing with the general formula. Scaling both the background and prescribed volume at the start is distinct from assuming that every candidate metric has the same Lee length.

The conformal connection identity is moved from the later rigidity proof to the Lee-cover section, with its local derivation. Both arguments now refer to that identity. A pagination guard keeps the Lee–Gauduchon cone definition with its display; its mathematics is unchanged.

## Sources and dependency scope

The complete mathematical text of Ornea–Verbitsky, arXiv:2206.08808v2, was reread, including Proposition 3.1, Theorem 4.1 and Lemmas 4.2–4.4 with their proofs. The local PDF SHA-256 is `1df9af465ad8f49bc0d1567e7fc13e67fc2364874eb63ccf78943e0b90e3820f`. The published entry remains in the bibliography. Access to its DOI endpoint returned HTTP 403, so the historical paragraph explicitly identifies the arXiv locators actually read.

The source's transverse Calabi–Yau, basic Hodge-theory and holomorphic-flow reconstruction inputs are not new premises here. The book instead supplies the reduction above from its existing smooth equation, the conformal connection formula, Stokes and the maximum principle. The source's displayed contraction is read with its binomial coefficient and metric normalization explicit. This is a direct proof reconstruction, not an independent verifier run or a fresh audit of every classical dependency of the source. El Kacimi-Alaoui's classical paper was located and downloaded during the source investigation but is not invoked by the new proof.

## Review scope

The original and revised `chapter_lck.tex`, `section_lck_volume_literature.tex` and `section_lck_chern_ricci_proof.tex` were read in full. Both revised reads cover these three files, with the second after the first build and visual inspection. The final history paragraph and the cone-definition pagination change receive bounded direct reads. The internal smooth-equation statement and uniqueness proof were consulted; this does not enlarge their earlier whole-chapter verification scope. The unchanged cone and strongly Gauduchon proofs are not claimed to have a fresh full mathematical review.

The first pass made the constant Lee norm and the basic function explicit. The second kept the contraction with its introductory sentence, corrected a sentence about the global tensor identity, and shortened the historical proof description. All old labels and the Vaisman theorem statement remain. Six labels are added; one new proof replaces the external-input paragraph. The bibliography, source inclusion graph, hidden sources and historical verifier reports remain unchanged.

Build, visual and fresh source-reconstruction evidence is recorded in `research/audits/build-snapshot-183.json` and `research/audits/source-package-portability-183.json`. The source package contains this review and the focused mathematical audit. No new Popovici reliance or skill change is introduced.

## Continuation

The next writing unit is the imported parabolic maximal-time theorem used by `cor:chern-ricci-current-lifetime`. The singularity/I-goodness, trace and geometric research obligations remain active; completing this proof does not complete the book.
