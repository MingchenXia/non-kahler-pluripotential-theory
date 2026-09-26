# Chapter 16 — Perron interpolation and the geodesic equation, checkpoint161

Baseline: 76d25c4bf1167a3e7b5dca6674d577267f5fd9fb (checkpoint160). The continuing whole-book goal remains active and incomplete.

## Scope and organization

The entire original `book/author/chapter_rays.tex` was read directly before rewriting. It has no nested inputs. The five sections are consolidated into four: subgeodesics and endpoint bounds, Perron segments, the smooth product equation, and the L2 action and torsion. All thirteen original labels and seven formal statements are retained. No general psh result is duplicated or moved out of Chapter 1.

The opening connects endpoint barriers with interpolation and finite-interval replacement, then identifies the torsion obstruction to interpreting this interpolation through the L2 action. Interior continuity and joint boundary control now follow directly after subgeodesic calculus. The product-envelope theorem is used at the supremum construction. The same-type time estimate is proved by explicit convex secant inequalities instead of endpoint derivatives. Repeated endpoint-convergence explanations, settings and transitions are removed. The switch to a Hermitian background remains explicit at the metric definition.

## Dependencies and mathematical review

The current Chapter 1 minimum-principle input was read in full. Targeted reads cover its maximum/gluing lemmas, Chapter 2's integration-by-parts lemma, Chapter 4's Gauduchon persistence proposition and three-torus example, the end of Chapter 15's analytic approximation, and Chapter 17's opening and finite-interval replacement argument. These are bounded dependency and transition checks, not new complete reviews of those chapters. The previous Chapter 16 review at checkpoint122 supplies historical comparison, not a substitute for the current direct review. No external theorem, citation, bibliography entry, source locator or Popovici premise is added. No new independent verifier run is claimed.

- On every compact interior time interval, surrounding-time chords give a constant upper bound and the bounded-interval minimum principle gives a common integrable lower bound. Finite convexity almost everywhere then gives L1 continuity by dominated convergence.
- Endpoint L1 sequences converge almost everywhere along subsequences. Convexity gives the chord bound; canonical almost-everywhere order gives it everywhere. Joint endpoint limits use upper semicontinuity, with arbitrary finite upper bounds at poles.
- The chord is jointly upper semicontinuous and locally bounded above on the product. A competitor makes every slice genuine, and regularization retains imaginary-translation invariance. The explicit L1 squeeze proves endpoint attainment.
- Replacing a path on a smaller interval is justified by joint boundary bounds and the Chapter 1 gluing lemma. When a smaller-interval endpoint equals an original endpoint, the same bound preserves original admissibility. Maximality forces equality with the replacement.
- For same ordinary type, the maximum of the two affine barriers has the required joint boundary bounds and L1 limits. The bounds give the singularity type and all secant slopes between minus C and C, including endpoint cases. Different types retain the distinction between existence of a common lower competitor and endpoint attainment.
- The smooth block matrix uses the column of holomorphic velocity derivatives, its conjugate transpose, and the Schur complement with factors one-half and one-quarter. The wedge identity and matrix trace use the same coefficient ordering. Spatial positivity is retained; the computation makes no nonsmooth homogeneous-equation claim.
- The action variation differentiates the velocity and the volume. Spatial integration by parts acts on the entire form f-squared times T. The product-rule cross terms have the signs d f wedge dc T minus dc f wedge d T, and the Hessian term cancels the time derivative of the volume. Strict positivity on the compact interval allows arbitrary small smooth fixed-endpoint variations.
- Nonzero constant translations attain their endpoints, equal their chords and solve the smooth product equation. Action stationarity is exactly ddc of the (n-minus-one)-st spatial power equal to zero, automatic in dimension one. The existing three-torus perturbation gives the asserted failure of stationarity even for a Gauduchon background. Surface persistence does not remove the remaining first-derivative torsion terms.

## Reading and release checks

The complete chapter has received two direct revised mathematical/editorial reads, with final production and source-reconstruction checks.

All thirteen original labels and seven statement/proof pairs remain. The house audit has zero errors and one inherited chapter-label warning; non-book citations remain in Chapter 33. The 809-page book and seventeen-page companion compile without errors, unresolved references/citations, duplicate labels or overfull boxes; the inherited bibliography underfull paragraph remains. All 31 selected final book pages pass visual review. The companion is byte-identical to checkpoint160. Both outputs rebuild from a fresh empty source-package extraction with identical page text. There are 33 active chapters and 218 author inputs. All 190 historical verifier reports and three hidden sources remain unchanged. Exact scopes are recorded in chapter-sixteen-rewrite-161.md, build-snapshot-161.json and source-package-portability-161.json.

The first selection had 31 pages: 17 changed/new images were directly inspected in 5 sheets, and 14 were byte-identical to inspected checkpoint160 images. The final render had 2 changed images, directly inspected in one sheet, and 29 byte-identical images. The selection covers complete Chapter 16 with adjoining pages, front matter and contents, and every other changed body page compared within its chapter while ignoring shifted running page numbers. The second read removes the auxiliary one-use gradient notation from the Schur proof and places the invariant-equation conclusion before its displayed computation, eliminating a stranded final line. The manuscript and build-script payloads in the final package match the fresh reconstruction; subsequent changes affect only research documentation. Private synchronization follows these checks.

## Continuation

Continue with the complete present Chapter 17 and all its nested inputs, then Chapter 18. The broader writing and research goal remains active and incomplete.
