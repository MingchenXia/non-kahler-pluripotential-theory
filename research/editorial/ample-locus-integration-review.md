# Ample-locus smoothness and the reconstructed Dang theorem

23 September 2026. Checkpoint93. Focused integration and proof review; no whole-book certification or novelty claim.

## Source and resulting book statement

The supplied smoothness-ample-locus-big-classes.tex is integrated as Theorem 28.3.2 in Subsection 28.3.1. On a compact Kähler manifold, for any big real (1,1)-class and a smooth strictly positive global volume form of the correct total mass, the normalized full-mass solution is smooth on the ample locus and defines a Kähler form there. Nefness is not assumed. The entire source and supplied ComplexGeometry 2.bib are preserved; their SHA256 values are recorded in the companion map.

The main proof retains BEGZ Theorems A/3.1 and B/4.1 as explicit classical existence/uniqueness and minimal-singularity inputs. The book's non-Kähler-locus theorem supplies one strict current with analytic singularities and pole set exactly E_nK. Its potential is smooth off that set. Minimality implies local boundedness there. Bounded locality identifies the non-pluripolar equation with the local equation. The global smooth volume form is in every finite Lp, so Theorem 13.21.1 applies; Theorem 13.22.1 then proves smoothness. A semipositive form of positive determinant is positive definite, and closedness of theta gives closedness of the resulting metric. The theorem asserts neither completeness nor extension across E_nK.

## Dang's result and full proof chain

Section 13.21 explicitly credits Dang26 Theorems A and 3.1. Its proof is supplied through the internal reference-preserving subsolution, comparison and one-sided stability in Section 13.19, the Chern-flow regularization lemma and the local interpolation argument. The exponent in the book, any positive beta < 2(p-1)/(np+3(p-1)), is sufficient and is not claimed optimal.

The scalar/local-equation formulation is proved after the theorem: u >= V_theta-C >= rho-C makes u locally bounded on Omega. The analytic complement has zero smooth volume and zero non-pluripolar mass, so an equation there extends globally in the non-pluripolar sense. The theorem applies to cf; a uniform estimate must bound its full Lp norm, including c. Section 13.22 gives the same explicit transition before its smoothness corollary.

Dang's regularity and the submitted interior theorem were not accepted as black boxes in the new verification. The accepted standard inputs are the classical BEGZ results, the local Demailly Chern-regularization expansion, bounded Bedford–Taylor theory, classical ABP/Evans–Krylov/Schauder theory and Guan–Li's local Dirichlet theorem. Explicitly accepted earlier book inputs include the bounded Lp subsolution, the strict current/locus theorem and local envelope/mixed-product tools. The full submitted chain was reviewed under those inputs; there is no assertion of proving those standard theories from first principles.

The source's intermediate local-density-only formulation is not adopted. Smoothness on an open subset does not imply global Lp integrability. The interior theorem keeps its explicit local Holder premise; the global-volume application discharges that premise. Nonminimal types, density zeros and regularity across poles remain outside this argument. No bounded-mass or positive-lower-mass property is invoked by the reconstructed estimates.

## Verification and primary second pass

The normal Rethlas run ample_locus_dang_integration_01 returned correct with no critical errors or gaps, and its complete saved report was read. It audited the full assembled comparison–stability–Holder–interior chain, including normalized comparisons, the O(delta) smooth nonclosed regularization error, the unbounded L1 O(delta^2) estimate, positive minimizing radius, localization, exact Dirichlet approximation, polynomial boundary trace, subpower trace estimate, gradient interpolation, polynomial Chern–Calabi control, nonlinear trace recovery, and the Bellman/ABP strong-to-viscosity passage before Evans–Krylov. Dimension one and the dd^c=i/(2pi) convention were included.

The primary second pass rechecked the strict-current locus interface, the minimal bounds, truncation locality, global integrability, the scalar, analytic null sets, positive definiteness and closedness separately. The corresponding earlier correct stability/Holder and Archive-refinement reports and the original adverse regularity report were reread. The adverse verdict is preserved: it concerns the missing premise in the broader source claim and is not contradicted by this correct bounded report.

Comparison with the previously supplied Archive regularity proof showed that the new local derivative proof has no substantive new step; the book retains its already expanded ABP/Bellman, curvature, cutoff, scaling and dimension-one arguments. All 38 existing formal blocks in the four edited book inputs are byte-identical; the new input adds one theorem. Subsequent edits to the frozen verification submission's presentation only shorten a scope paragraph and split an exposition paragraph. The mathematical statements and proofs reviewed by the run are unchanged.

## Primary references and bibliography

Dang26 was checked against https://arxiv.org/html/2603.25520v1, including the regularization material and Theorems 3.1 and 3.3 and their proofs. The book retains its explicit normalized comparison condition in the stability theorem; an unrestricted additive shift is not silently permitted.

BEGZ was checked in the published author copy https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf, Acta Mathematica 205 (2010), 199–262, DOI 10.1007/s11511-010-0054-7. Theorem A appears on p. 200, Theorems B and C on p. 201, Definition 1.13 and the ample-locus description on p. 213, and the quantitative minimal-singularity estimate in Theorem 4.1 on p. 245. Theorem C has the nef premise; that premise is not imported into the new theorem.

All seven bibliography keys used in the supplied source already have the necessary records: BEGZ10, BT82, Dang26, Dinew09, GT01, TWWY15, and GuanLi10 under the book key GL10. No bibliography entry was overwritten or duplicated. The previously verified Dinew09 v1 Theorem 1.2 locator is retained. The bibliography is byte-identical to checkpoint92. No new Popovici result or NUM citation is introduced.

## Output and preservation

The production book has 716 pages. All 42 selected final pages were rendered and inspected: 27 images are pixel-identical to previously read output, and the other 15 were reread. They cover the new theorem, Holder/scalar exposition, full local derivative proof, surrounding transitions, the research-program update and relevant navigation. Compilation has no errors, unresolved references, duplicate labels or overfull boxes. One inherited bibliography underfull paragraph remains. The five-input house audit has 0 errors and 15 inherited warnings (existing labels, a topology wording flag and existing preprint records).

All 179 historical reports remain unchanged; together with the new report there are 180, of which 171 are correct and nine adverse. All 29 SGPT originals, six supplied source/bibliography originals, checkpoint92 and its archive, the 17-page companion, the three inactive Nakamaye files and the unverified inactive nef-metric draft remain preserved. No verifier memory or prior result was edited. The current proof scope is recorded in the map and build-snapshot-93.json. Clean reconstruction is recorded separately in source-package-portability-93.json and must pass before release checks are complete. The broader book goal remains active and incomplete.
