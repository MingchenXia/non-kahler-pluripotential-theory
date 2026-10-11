# Reader preparation during unavailable execution — 11 October 2026

This is a research-only snapshot of completed baseline reading, bound to private source commit `0646d2cf9d9bb10e15bc357305cce3c58ecb4741`. It is not checkpoint 685 or a checked manuscript release. The latest private checked release remains checkpoint 684. No mathematical statement, proof, problem status or reader-facing source is changed by this snapshot.

The exact GitHub source and Git blob SHA of each file are recorded in the [machine-readable inventory](remote-reader-preparation-20261011.json). Chapter 12 is read recursively in full: 14 files and 75 proof environments. Chapter 13 is also read recursively in full: 10 files and 39 proof environments. Chapter 14 is only partly read: its root and 23 inputs, with 72 proof environments. Its unread input list is explicit; further descendants of those unread files have not yet been inventoried. Counts describe reading scope, not independent proof certification.

Every listed source was read at the fixed commit. Two long Chapter 12 inputs were read in contiguous ranges covering the whole file. Recursive input closure was checked from the fetched source for Chapters 12 and 13. Local byte comparison, final revision, the second complete reading, output inspection and compilation remain pending. The original Chapter 12 local baseline inventory has 3751 lines; no comparison with the currently unavailable local files is claimed.

## Chapter 12: complex Hessian equations

The reader path begins with the admissible cone and its coefficient estimates, passes through Euclidean Liouville and derivative estimates, then constructs smooth proper equations and admissible approximations. Continuous products, obstacle envelopes and domination precede the continuous regularity theorem. Bounded products require a separate passage through coefficient measures, Sobolev estimates, local Hessian capacities, weighted convergence, symmetry and locality.

A revision must preserve these boundaries. The chapter setting is `2 <= m < n`, although some cone algebra also applies to the determinant degree and the Euclidean Liouville argument also permits degree one. The normalized Hessian root and the unnormalized symmetric polynomial are different operators. Uniform control of the complex Hessian does not assert a uniform bound on the full real Hessian. The trace estimate must keep the fixed comparator's C2 dependence separate from independence of derivatives of the varying prescribed potential.

The raw recursive product at degree m is initially a distribution. Positivity of the shifted top product after wedging with the background produces a measure; this cannot be silently transferred to the unshifted product. Sobolev capacity controls the first Hessian and the two-factor argument, while the codimension-two example explains why the higher products need Hessian capacity. Joint weighted limits justify symmetry before varying-set locality and contact inequalities are used.

The final comparison arguments retain all torsion terms. Invariant mass is a condition on the indicated background powers. On arbitrary Hermitian backgrounds, modified comparison controls torsion only in the stated small-sublevel range and with its stated error. Bounded proper solvability and regularity remain within the specified constant barriers. A closing transition to Chapter 13 may explain the role of relative envelopes; it must not assert unrestricted nonproper degenerate Hessian solvability.

## Chapter 13: relative envelopes and singularity types

The chapter passes from bounded contact support to arbitrary singularities, model envelopes, singularity volumes and the relative envelope class. The positivity assumptions on the background vary with the result. Extended Monge--Ampere mass may be infinite, and individual mass must remain distinct from the lower and upper volumes of an ordinary singularity type.

The affine/projective passage keeps the logarithmic growth allowance matched to both the projective background and the shifted obstacle. Raw contact of the pointwise supremum and contact after upper semicontinuous regularization are different. Quasi-everywhere obstacle constraints preserve the regularized envelope, and they are essential in the supporting-probability tests. Replacing them by pointwise constraints admits a point mass that hides the regularization defect.

Growth derivatives are described by active supporting pairs; changes of the weight test their probability component. Local pluriregularity implies persistent contact for the stated upper semicontinuous weights under raw contact. For a global strictly plurisubharmonic weight near the point, the local relative extremal function gives a quantitative defect. Mere non-thinness does not suffice, as the transverse-disk example shows.

The modification identities concern the exact pullback background. They do not compare singularity volumes for an independently chosen Hermitian metric upstairs. Shortening the introduction or improving transitions must retain these distinctions and all lower-mass hypotheses.

## Chapter 14: partial preparation

The root and 23 inputs have been read, through prescribed-type existence, minimal-singularity existence and regularity, interior smoothness, semipositive degeneration, nodal metric comparison and invariant projective selection. The remaining local examples, resolved ordinary equations, general-measure and critical-density inputs have not been read in this snapshot.

The partial reading checks the dependency order from smaller-background domination and a bounded subsolution to bounded exponential and normalized existence, stability, regularity, contact support and compactness. A density-dependent subsolution is not a lower-mass theorem for the entire admissible class. The normalized equation generally determines only its positive scalar, whereas a positive exponent gives uniqueness of the potential in the stated ordinary type.

Stability requires the limiting potential to have an equation with a controlled density before it can turn L1 convergence into uniform convergence. Common-barrier compactness first identifies capacity convergence from the self-measure error; domination then supplies finite mass and uniform control of deep sublevels. At a positive limiting exponent, exponential decay supplies such tail control. It is lost at exponent zero. No new solvability, regularity or open-problem conclusion is adopted.


The bounded-subsolution proof allows the reference density to vanish. Its upper normalization bound uses smooth-volume mixed approximants and a fixed-reference trace, rather than a uniform positive lower bound for the density. Weighted addition permits growing truncation masses: a polynomial range bound is paired with a decaying exponential error, and lower-barrier cutoffs identify the equation before any global weak convergence is claimed. The relative lower-density lemma bounds the Lq norm, not total mass.

For arbitrary big backgrounds, a strict analytic barrier supplies comparison and reference subsolutions. Pairwise stability identifies uniform limits of differences before their density is recovered from local products. Resolved analytic approximants use the exact residual background and Jacobian. The interior smoothness proof requires smooth positivity on the whole regular locus and uses the global proper barrier gap, exact Dirichlet approximants, localization of trace growth, C1alpha interpolation, a polynomial Calabi estimate with Chern torsion, and nonlinear trace iteration. Local nonsmooth examples remain a different setting.

The degeneration section declares new barrier data. Its normalizing constants have a perturbation-independent limit, while closedness supplies the mass identity and energy uniqueness in the nodal application. The pushed-forward density has sharp p<3 integrability and a weak L3 endpoint; descent asserts boundedness, not continuity at nodes. Metric convergence needs both shrinking approximating tubes and shrinking limiting punctured neighborhoods. Curve area alone requires an upper metric bound to control diameter, and a fixed-volume surface family separates the two neighborhood conditions.

The projective selection proof defines the full group generated by block unitary transformations and block exchange. A distributional radial flux justifies the reduction for bounded invariant solutions before the scalar equation is solved; its jump exclusion and the bounded projective ends are essential. On the zero-density band, the positive-exponent solution has the same slope as the selected limit and the same failure of C2 regularity at the transition hypersurfaces.

## Recovery and release boundary

The execution environment has not recovered. Its failure and subsequent queued startup are infrastructure observations, not a completed restart performed by the assistant. Terminal access and environment-restart controls were unavailable. The user explicitly authorized restarting the cloud environment whenever needed, without further confirmation; this authorization does not supply an absent runtime control. This snapshot is saved through the existing GitHub connection under the standing private-backup authorization, with a normal fast-forward and an expected-head check. It does not recover or back up the inaccessible uncommitted Chapter 11 files.

On recovery, inspect the saved local Chapter 11 work before changing it. Reconcile this research-only commit normally; preserve the pending source edits. Finish Chapter 11, including both complete revised reads, the full affected output, neighbors, contents, index, dated covers, native catalogue diagnostics and the source-package reconstruction. Before superseding its first public build, verify the served PDF and matching description for that exact publication commit. The next full author build must carry the actual current date on the cover, including the companion cover, and must update and verify the public PDF and homepage under the existing procedure.

Then use the source-bound preparation above for Chapters 12 and 13, complete Chapter 14's recursive baseline reading, and continue the whole-book and recent-primary-paper queues. Xean remains withdrawn. The whole-book writing and polishing goal remains incomplete.
