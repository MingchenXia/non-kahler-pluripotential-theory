# Chapter 10 rewrite — checkpoint154

Baseline: `c0dd234fdffeb1ca56cf2fe58347cd3a35c9a7c4` (checked checkpoint153).

## Scope and reads

The complete unit is `book/author/chapter_weak_equations.tex` and its three inputs, `section_modified_comparison.tex`, `section_weak_estimates.tex` and `section_classical_scalar_uniqueness.tex`. All four original inputs (568 lines) were read and saved with hashes before editing. All four revised inputs received a complete first mathematical/editorial read, a build and visual inspection, and a complete second direct read. Subsequent bounded wording and layout changes were read at their affected passages. The layout-only contents reservation at the start of `appendix_hermitian_spaces.tex` was checked in context; its unchanged mathematical content is not part of the whole-chapter reread. No other chapter is claimed as newly read in full.

Dependency checks concern the Chapter 1 compactness, exponential-integrability and capacity statements, the Chapter 4 Gauduchon trace inequality, the Chapter 8 mass and averaging identities, the Chapter 9 smooth existence statements, the Chapter 11 opening and callers, and the Chapter 33 attribution. They retain their previous proof-review scopes. Both writing skills apply. Existing skill rules already cover the changes; no new author intervention calls for another skill rule.

## Changes

Six sections replace nine. The capacity estimate and its uniform-compactness consequence form one argument. Both constructions of continuous solutions share a section with exponential order and the continuity of bounded solutions. Scalar uniqueness and the vanishing-exponent cluster equation stay together; the elementary classical proof follows them. The main existence theorems retain their opening section and all thirty original labels remain without duplicates.

The chapter uses the existing perturbed-form notation, the Chapter 1 compactness theorem and the Chapter 9 smooth existence theorem. Repeated settings, root inequalities, roadmaps and the closing recap are removed. The sublevel constants now state their separate dependencies, and the mixed-product exponent is named `r` to avoid reusing the fixed density exponent `p`. Concise openings that already explain their proofs remain.

The vanishing-exponent paragraph gives the oscillation bound, strong Lp convergence of the densities and the equation of every normalized cluster limit, without claiming potential uniqueness or a selected limit. In the classical proof, positivity of the comparison form at the chosen maximum justifies division by its determinant; positivity of the other form is unnecessary. The Hopf specialization states the change of volume form once and uses measure invariance directly before fiber averaging. Strong convergence of potentials and weak convergence of densities remain distinct.

## Mathematical checks

The contact inequality has the sign needed to estimate the difference of sublevel mixed masses. Integration by parts is justified by the already established bounded regularization and convergence results. With `r=n-k-1`, the torsion coefficients are `k(k-1)`, `k(1+2r)` and `r^2`, each at most `n^2`; the recurrence closes because `1+q^-1+q^-2<4`. Negative powers with zero coefficients are absent, and dimension one has no torsion terms. Strict domination keeps epsilon fixed before shrinking the sublevel, whose positive smooth volume supplies the contradiction. This gives positivity for each bounded potential, not a uniform positive lower mass over all potentials.

The capacity test stays within the convex range and places its comparison set between the two stated sublevels. The backwards iteration first proves that each new height is positive; monotonicity of capacity then suffices for the contradiction. Its lower capacity bound combines with the Chapter 1 tail estimate to give the potential bound and the lower density norm. In the compactness argument, epsilon and the sublevel height are fixed independently of the sequence indices. Chebyshev and Holder turn L1 Cauchy convergence into the contradiction. No uniqueness of zero-exponent potentials is used.

The Gauduchon root integrals converge to a positive number under the specified Lp convergence, giving upper scalar bounds. The lower density norm gives positive lower scalar bounds. For the exponential equation, the weighted probability has denominator bounded away from zero; the conjugate exponent `np/(np-1)` is finite even when `n=1`. Normalized exponential integrability controls its mean. Uniform convergence and Lp convergence of the densities identify the limiting bounded products. The proper comparison theorem gives uniqueness among bounded solutions and continuity of bounded Lp solutions.

The two constant translates have the required comparison directions. They give `|lambda u_lambda-log c| <= lambda osc(u)` and an oscillation bound `2 osc(u)`. Every normalized cluster limit has density `cf`; the uniqueness claim concerns `c`. At a maximum in the classical proof, `A+epsilon omega <= (1+epsilon)B` makes `B` positive, so determinant monotonicity gives the claimed bound for `c`; reversing the potentials gives the other inequality.

On the Hopf threefold the mass is `6 c_f I_f` and the averaging constant is four. Equality gives a continuous base potential by local sections. Haar averaging is applied to identities of measures, followed by Fubini and Jensen. In the converse, mass invariance on the projective base identifies its scalar, and bounded-product continuity passes the smooth cube formula through local trivializations. Near equality, reflexivity is used only for finite `p>1`; the two whole-sequence conclusions follow by a subsequence contradiction with a fixed dual test for weak convergence. The oscillating family has uniformly positive coefficients, unit normalized density, scalar `1+a^2/(2 pi^2 m^2)` and a positive limiting L1 distance `2a/pi` from its fiber average. It therefore excludes a stronger density conclusion.

There is no new external theorem, bibliography or locator, Popovici dependency, or independent verifier run. Paper citations remain in Chapter 33.

## Release checks

All four author inputs have zero house-audit errors and the same three inherited warnings. Non-book citations remain in Chapter 33. The 806-page book and seventeen-page companion compile without unresolved references/citations, duplicate labels or overfull boxes; the inherited bibliography underfull paragraph remains. All 48 selected final pages pass visual review, with 20 changed images directly inspected and 28 byte-identical to inspected first-output images. Both outputs rebuild from a fresh empty source-package extraction, with every page text matching production. There are 33 active chapters and 216 author inputs; all 190 historical verifier reports and three hidden sources remain unchanged. Exact scopes are recorded in chapter-ten-rewrite-154.md, build-snapshot-154.json and source-package-portability-154.json.

The first selection had 66 pages: 54 were directly inspected on 14 sheets and 12 were byte-identical to checked checkpoint153 images. Local space reservations keep formula lead-ins and section openings with the text they introduce. The final visual scope covers the complete Chapter 10 and its transitions, front matter and contents, and every other changed body page matched within its chapter while ignoring shifted running page numbers. Every changed image in the final layout refresh was directly reinspected. All 30 original labels remain. The companion is byte-identical to checkpoint144. The contents reservation keeps the appendix entries with the final bibliography entry. The final package manuscript and build payloads match those rebuilt; later changes affect only research documentation. Routine private synchronization follows the checks.

## Continuation

Continue with the complete present Chapter 11 and all its nested inputs, then Chapter 12. The broader writing and research goal remains active and incomplete.
