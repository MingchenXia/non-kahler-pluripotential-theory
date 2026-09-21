# Whole-manuscript correctness and exposition pass

Started21 September2026 following the user's explicit request to optimize every already written part. The table records this new systematic pass, not the older targeted proof audits. “Read” means a full statement-to-proof root pass of the named chapter; it is not a mathematical guarantee or an independent audit. Chapters1–5 revisions are integrated in checkpoint31 after compilation and visual checks. The rest of this systematic pass remains incomplete.

| Chapter | Scope in this pass | Status |
|---|---|---|
| 1 | `author/chapter_framework.tex` (`chap:framework`) | Read every result and proof; align positive real ideal weights with Chapter16, clarify convention lambda>=0, remove repeated introduction. |
| 2 | `author/chapter_mass.tex` (`chap:mass`) | Read all smooth identities, signs, n=1/2 cases and torus constants; distinguish trace measures from conserved total trace; make determinant monotonicity explicit. |
| 3 | `author/chapter_energy.tex` (`chap:energy`) | Read formal-adjoint symmetry, local jet realization, polarization and radial defect; retain necessary linear algebra, reuse the symmetry lemma in the telescoping proof; verify YiLi10 Equation(1.18)/Theorem1.2 as contextual input. |
| 4 | `author/chapter_gauduchon.tex` (`chap:gauduchon`) | Read the entire chapter and prior gauduchon_duality_01 result; retain Hahn–Banach/right-inverse proof, shorten repeated adjoint Fredholm argument by citing the proved conformal theorem. |
| 5 | `author/chapter_compactness.tex` and `section_gauduchon_trace_topology.tex` (`chap:compactness`) | Read every statement and proof, including local logarithmic-radius/Poisson estimates, coordinate overlap, branch removal, decreasing diagonal and exact rescaling; preserve necessary steps. Make eventual negativity and the mean-normalized uniform upper bound explicit. |
| 6 | `author/chapter_products.tex` (`chap:products`) | Pending full reread. |
| 7 | `author/chapter_damped_measures.tex` (`chap:damped-measures`) | Pending full reread. |
| 8 | `author/chapter_hopf.tex` (`chap:hopf`) | Pending full reread. |
| 9 | `author/chapter_smooth_equations.tex` (`chap:smooth-equations`) | Pending full reread. |
| 10 | `author/chapter_weak_equations.tex` (`chap:weak-equations`) | Pending full reread. |
| 11 | `author/chapter_degenerate_uniqueness.tex` (`chap:degenerate-uniqueness`) | Pending full reread. |
| 12 | `author/chapter_envelopes.tex` (`chap:envelopes`) | Pending full reread. |
| 13 | `author/chapter_prescribed_equations.tex` (`chap:prescribed-equations`) | Pending full reread. |
| 14 | `author/chapter_relative_finite_measures.tex` (`chap:relative-finite-measures`) | Pending full reread. |
| 15 | `author/chapter_normalization.tex` (`chap:normalization`) | Pending full reread. |
| 16 | `author/chapter_igood.tex` (`chap:hermitian-igood`) | Pending full reread. |
| 17 | `author/chapter_rays.tex` (`chap:hermitian-rays`) | Pending full reread. |
| 18 | `author/chapter_testcurves.tex` (`chap:hermitian-testcurves`) | Pending full reread. |
| 19 | `author/chapter_analytic_approximation.tex` (`chap:analytic-approximation`) | Pending full reread. |
| 20 | `author/chapter_trace_data.tex` (`chap:trace-data`) | Pending full reread. |
| 21 | `author/chapter_sections.tex` (`chap:sections`) | Pending full reread. |
| 22 | `author/chapter_flag_bodies.tex` (`chap:flag-bodies`) | Pending full reread. |
| 23 | `author/chapter_hopf_reduction.tex` (`chap:hopf-reduction`) | Pending full reread. |
| 24 | `author/chapter_divisorial_models.tex` (`chap:divisorial-models`) | Pending full reread. |
| 25 | `author/chapter_nonclosed_bclasses.tex` (`chap:nonclosed-bclasses`) | Pending full reread. |
| 26 | `author/chapter_envelope_systems.tex` (`chap:hermitian-envelope-systems`) | Pending full reread. |
| 27 | `author/chapter_gauduchon_variational_volume.tex` (`chap:gauduchon-variational-volume`) | Pending full reread. |
| 28 | `author/chapter_partial_bergman.tex` (`chap:partial-bergman`) | Pending full reread. |
| 29 | `author/chapter_bott_chern_loci.tex` (`chap:bott-chern-loci`) | Targeted elliptic additions and adjacent loci interfaces; three independent audits passed, including the Gauduchon limits. Full reread of the remaining chapter pending. |
| 30 | `author/chapter_transcendental_nakamaye.tex` (`chap:transcendental-nakamaye`) | Pending full reread. |
| 31 | `author/chapter_lck.tex` (`chap:lck`) | Pending full reread. |
| 32 | `author/chapter_research_program.tex` (`chap:research-program`) | Targeted interfaces only: ideal/ordinary topics retained, degeneration examples synchronized, nonnegative trace distinguished from strictly positive Hermitian trace. Full reread pending. |
| Appendix | `author/appendix_hermitian_spaces.tex` | Pending full reread. |

## Specific checks and boundaries

The basic proofs in Chapters1–4 were checked from their displayed formulas: local smooth correction, nonnegative sums with zero terms omitted, ordinary/ideal order, one-variable integrability endpoint, line-bundle transition laws; d/dc signs in the mass polynomial and its variations; pointwise realization of arbitrary small Hermitian Hessians; formal symmetry and nondegenerate wedge pairings; Fredholm positivity, the zero-degree Hahn–Banach case, continuity of the right inverse and the current Stokes pairing. No new theorem or stronger conclusion is introduced by these edits.

The original Chapter1 paragraph used positive integer weights although Chapter16 and all envelope/trace applications use positive real weights. The revision states the latter convention directly; it does not silently claim an integer-to-real equivalence. The original Chapter2 transition could blur ordinary-type invariance with linear trace control. The revision distinguishes the trace measure from its conserved total.

The external contextual Yi Li citation was rechecked at https://arxiv.org/html/1004.0553v1, Equation(1.18) and Theorem1.2 (n>=3). It is a modified path functional, not a primitive of the raw one-form. The primary abstract and author institutional listing distinguish the general-manifold preprint from the published surface paper; the general-dimensional reference is retained. No theorem in Chapters1–4 relies on that paper. The TW10 and BGL25 local locators retain their recorded primary-source verification in `research/literature.md`; the new pass does not reconstruct all classical elliptic theory.

Next: Chapter6. The first five chapters passed final integration and visual review. Continue through every chapter and appendix; a targeted audit or clean compile does not discharge the whole-manuscript obligation.
