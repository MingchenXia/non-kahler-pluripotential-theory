# Analytic approximation and ideal-envelope volumes — checkpoint197

Baseline: `2de39d477d25343669f6904164e74f4885198e16`. The preceding goal turn completed checkpoint196 and its private synchronization, so it was progress. All ten supplied integrations, including Q8.2 in Sections 14.8–14.10, remain complete. This continuation completes the queued analytic-approximation and upper-volume unit.

## Mathematics

Corollary 29.8.1 computes the ideal-envelope lower volume as a decreasing limit of the dyadic analytic volumes, including zero. Its upper-volume conclusion retains positive lower volume of the ideal envelope. The analytic approximants and their ordinary envelopes have the same two volumes because they have the same bounded-difference type.

Theorem 29.8.1 constructs analytic potentials in any fixed smooth big background. A fixed strict analytic potential rho and rational curvature bounds give rational convex coefficients c_j tending to one; b_j = c_j a_j + (1-c_j) rho is theta-plurisubharmonic and converges to the original u in L1. The corrected ordinary models r_j are bounded below by c_j P[u]_I + (1-c_j) rho. Above, r_j/c_j is a competitor for the analytic model t_j in the larger background theta + (1+A/kappa) epsilon_j h. This background both dominates the regularization background and satisfies theta <= c_j times that larger background. Those two distinct comparisons are checked explicitly. Homogeneity, addition and volume monotonicity squeeze both volumes of r_j and max(r_j,P[u]_I). Decreasing-model continuity then gives convergence for d_theta to the ideal envelope. Its positive lower volume gives L1 and capacity convergence. Comparison with the original potential tends exactly to the upper-volume excess. The existing conditional criterion identifies its vanishing with ordinary/ideal-envelope equality.

Theorem 29.8.2 proves the converse for arbitrary analytic ordinary-model approximations, and more generally closure of ideal-envelope models at an ordinary-model limit of positive lower volume. The deficit stretch supplies a convex inequality. Applying ideal-envelope concavity replaces its two inputs by canonical ideal representatives. The resulting lower-volume estimate gives a common positive lower bound along the sequence, even though none was assumed. The existing L1 comparison bound and the uniform normalized L1 bound on the auxiliary ideal models force the limiting model to equal its ideal envelope. Thus ideal models inherit Cauchy completeness inside every fixed closed positive lower-volume sector. Analytic density is not claimed inside that exact same sector at its boundary.

The two formal topology questions in Chapters 15 and 32 now ask for the extension beyond the proved mass regime, background compatibility and metric properties. The positive-volume part is no longer left as an unresolved question. The zero-lower-volume positivity and equality question in Section 29.8 remains.

## Sources and review scope

The complete Section 29.8 received its original and two complete direct revised mathematical/editorial reads, the second after the first build and visual inspection. The Chapter 29 opening and preceding transition, Section 15.5.3, Section 32.7 and the final Section 33.8 paragraph received bounded direct reads. This is a scoped extension, not a fresh whole-Chapter-29 rewrite. The complete unchanged Section 15.5 analytic-envelope input was read as a dependency, together with the specific regularization, envelope-operation, stretching and volume-continuity dependencies. No new source, citation locator, Popovici reliance, unproved external premise, full source audit, novelty claim or independent verifier run is introduced. Existing classical regularization and local ideal inputs retain their prior recorded scope.

All 30 previous Chapter 29 formal statements and 27 proofs are byte-identical. Three statements and three proofs are added; five labels are new. Two interface problems are narrowed. Four author inputs change; all prior labels, the bibliography and input graph remain. The second pass identifies the deficit lemma explicitly, removes an unused equation number and keeps both new corollary conclusions together. No new author correction requires a skill change.

## Release checks

The 841-page book and seventeen-page companion compile without errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph remains. The house audit has zero errors and 29 inherited warnings. The companion is byte-identical to checkpoint196. The first visual review directly inspects 28 images. All 47 selected final pages pass: 4 changed images directly inspected and 43 identical to the inspected first render. Selection includes the complete Section 29.8 and its transitions, the Chapter 29 opening, front matter, bounded Chapter 15/32/33 interfaces and every other changed body page. Image equality, not only matching text, carries prior visual review.

Both outputs rebuild from a fresh empty source-package extraction, and every page text agrees with production. The final package manuscript and build scripts match that rebuilt payload. All 221 active author inputs are included. The 190 historical verifier reports and three hidden Nakamaye sources remain unchanged; the hidden sources remain excluded. See build-snapshot-197.json and source-package-portability-197.json.

## Continuation

Establish compatibility of the upper-volume comparison and the analytic approximation criterion with smooth changes of representative and controlled changes of background, keeping the zero-lower-volume boundary separate. The broader writing and research goal remains active and incomplete.
