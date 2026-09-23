# Reference stability and local Holder reconstruction

23 September 2026. Bounded mathematical review for checkpoint90; not whole-book certification or a novelty claim.

## Scope and dependencies

Sections 13.20–13.21 add a normalized one-sided stability theorem for arbitrary references rho<=eta<=0, compactness in a fixed reference interval with uniformly Lp-bounded densities, and local Holder continuity for minimal-singularity solutions of an arbitrary smooth big (possibly nonclosed) background. No uniform upper or lower metric mass property is used. The interior smoothness proof remains intact; its global Lp corollary now uses the internal Holder theorem. Classical local regularization, Bedford–Taylor calculus, quasi-psh compactness, local Lelong estimates and removable singularities remain standard inputs.

The stability proof uses the already checked reference-preserving subsolution construction and domination above a strict barrier. Their complete texts were supplied to the core verifier. The reference interval and normalization v<=eta are essential; the comparison potential need not have the same singularity type. In the compactness corollary both sequences lie in the same reference interval. Pairwise stability proves uniform Cauchy convergence first, and the limit equation is then identified using local uniform Bedford–Taylor continuity and weak Lp convergence. This does not assume uniqueness of the solution potential.

## Primary-source review

The full relevant proof of Demailly94-flow, Proposition 3.8, equation 3.11 and Theorem 4.1 through Remark 4.7, was read. PDF pages 8, 11–16 were rendered and inspected. The theorem alone supplies an unspecified curvature modulus. The book derives a linear error by choosing A omega to bound curvature on all decomposable tensors, eliminating the epsilon/M_epsilon step of Lemma 4.4; freezing a quadratic q_(x,t) with Hessian theta(x)+Bt beta on the O(t) averaging neighborhood; bounding scaled coefficient mass by O(t^-2); and using the order-two expansion and radial identity 4.5. The quadratic is held fixed during differentiation. The positive mass estimate uses a fixed psh correction on a larger chart, so its constants do not depend on the shrinking neighborhood. Smooth quadratic subtraction has only O(t) base error and O(t^2) logarithmic radial error. The vertical |w| correction absorbs mixed terms at O(t) base cost.

The old general-modulus proof is retained and is not retrospectively described as quantitative. The new lemma extends the L1 smoothing estimate to normalized unbounded quasi-psh potentials using the adjoint identity and uniform L1 compactness. Local boundedness supplies the compact-set gradient bound and attainment of the capped Kiselman infimum. The strict barrier corrects the negative curvature loss; stability then controls the minimizing radius. The elementary gradient interpolation gives the explicit nonoptimal exponent beta<2(p-1)/(np+3(p-1)).

Dang26 v1 Section 3.2 was read in full. The theorem is credited, while the proof is reconstructed against the classical expansion. Its printed stability statement lacks an upper comparison normalization, which the book explicitly includes. Neither the source's displayed linear loss nor its theorem statement is used as a substitute for the reconstructed argument. Global Lp density remains a hypothesis; merely local smooth positive density supplies no such global integrability.

## Independent reviews and second pass

The normal Rethlas run `big_reference_stability_holder_01` returned **correct**, with no critical errors or gaps under its explicitly accepted established book inputs. It independently checked the entire stability argument, the quantitative nonclosed regularization refinement, local Holder proof and uniform constants. It consulted Demailly's primary formulas and Dang's source. Its frozen input contains the initial, weaker convergence corollary.

A later second pass strengthened that corollary to compactness of the entire fixed-reference Lp family and identification of the limit density. This exact stronger statement and proof were separately submitted as `big_reference_compactness_01`, which returned **correct**, accepting the one-sided stability theorem conditionally. The first completed report discharges that condition. The second report checks canonical representatives across the analytic set, local product continuity for nonclosed backgrounds, sequential and metric compactness, and weak convergence of the whole density sequence. No uniqueness of equation potentials enters.

The second pass also expanded the already audited regularization argument by displaying the full curvature bound, defining beta explicitly, spelling out the fixed larger-chart positive current and coefficient-mass estimate, and explaining the uniform vertical constant. These are primary-checked explanations of steps already checked in the core report, not stronger conclusions. No verifier memory or result was edited.

The source introduction, earlier qualitative-continuity section and Chapter 33 now point to the internal results. Existing theorem/problem hypotheses remain unchanged. The adverse report for the original broad interior-smoothness statement remains untouched: proving the global Lp case does not justify the original local-density-only statement. No Popovici result is added or used.

## Remaining scope and release checks

Local-density-only regularity, regularity for arbitrary nonminimal types, behavior across poles and density-zero regularity are not claimed. The uniform-difference compactness theorem has fixed reference bounds and a global density bound; it does not follow from arbitrary weak convergence of measures. The separate nef incomplete-metric draft remains explicitly unverified and inactive, and the three Nakamaye files remain excluded.

The final preview has 710 pages. Thirty-three selected pages cover the full new sections, their transitions, chapter introduction, qualitative-continuity cross-reference, global Lp corollary, research discussion and contents. They were rendered and read; the last wording polish is checked again before production comparison. The house audit of the five affected inputs reports 0 errors and 15 inherited warnings. Exact final production, preservation and clean-source reconstruction checks are recorded separately in `../audits/build-snapshot-90.json` and `../audits/source-package-portability-90.json`. Those checks must pass before declaring a checked release.
