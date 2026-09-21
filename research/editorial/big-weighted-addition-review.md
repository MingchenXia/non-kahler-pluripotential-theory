# Weighted limits and addition in a prescribed class

## Scope and proof boundary

The two sections treat an arbitrary smooth big real theta under BMP and a model reference phi with positive lower relative volume. They allow nonclosed, nonsemipositive backgrounds. The book's general framework continues to have no standing BMP assumption. These results belong to an explicitly restricted regime.

The first lemma proves capacity convergence from a weighted self-error and a common lower bound in E_phi. The approximants need not belong to E_phi. The second identifies an addition equation after truncating either or both input potentials, without requiring the undamped weighted measure to have finite mass. The addition theorem constructs a unique a in E_phi below both inputs when one input has ordinary type phi or its MA is dominated by a bounded Hermitian carrier. Two inputs of ordinary type phi produce an output of that ordinary type.

This completes the weighted-addition step associated with Li arXiv:2601.13446v1 Proposition6.1, not yet the arbitrary-model finite-measure existence theorem. Supersolutions, the relative projection argument and the ordinary-type Lp refinement remain to be reconstructed. The imported theorem in Chapter13 retains BOTH metric volume properties. Working proposals for these remaining arguments are saved separately in `big-model-existence-next.md`; they are not proved book results and are not included in the release archive.

## Main checks

Finite rooftops in the common-bound lemma are genuine because of a fixed competitor. Only their infinite-tail limits, bounded above by the target limit, are claimed to belong to E_phi. Disjoint first-contact pieces control the weighted error without a factor equal to the number of inputs. Bounded quasi-continuous weights and monotone capacity convergence justify both lower-semicontinuity passages. Zero domination and upper tail envelopes give capacity convergence.

The truncated-equation lemma bounds the error outside strict locality sets by an exponentially small quantity times the uniformly bounded input masses. On the strict sets the fixed measure is MAu+MAv. Convergence of bounded exponentials against this finite NPP measure precedes convergence in measure of the potentials. Fixed cutoffs of the common lower bound identify the equation: constant truncations are taken in a larger Hermitian background, and the uncut theta product is expanded as a signed bounded product before inserting the cutoff. No weak convergence of the original uncut approximating measures is asserted. Original truncation levels are retained after subsequence extraction.

The addition proof has four stages. Ordinary minimal-type inputs are first handled by truncating weights only. A fixed lower barrier and the envelope upper bound prove ordinary type for the first solution; a fixed finite dominator then permits the decreasing limit. Only after obtaining the limiting equation is the order below each input asserted. For ordinary model-type inputs the approximating solutions have minimal ordinary type; the common lower bound justifies the change of singularity type in the limit.

For one ordinary-type input, stretched contact cancels a finite input measure on the tail set. Disjoint contact pieces preserve the exponential bound uniformly in finite rooftops. The first-moment reference is fixed. For a bounded-carrier input, a separate first moment bounds solution suprema before applying the normalized carrier estimate. Capped stretched rooftops have both a uniform first moment and the fixed finite dominator MAu+2^n MAv. Genuine L1 limits are obtained before applying fixed-dominator continuity. This supplies a common lower envelope for the final equation limit, replacing the additional external continuity input in the source proof.

## Audit and source relation

Rethlas runs `big_weighted_limits_01` and `big_weighted_addition_01` both report correct under the stated internal premises. All16+21 sequential checks,5+3 reference checks, failed-check channels and full final reports have been read. Both failed-check channels are empty. The addition audit's sole conditional dependency consists of the exact two lemmas independently discharged by the limits audit. No mathematical adverse finding remains. Audit scope is bounded proof review, not formal verification or novelty certification.

The submitted sources remain unchanged under `research/editorial/`. Production contains only these wording clarifications, plus three pagination guards in the addition source: (1) replace the ambiguous fixed-input sentence by “Either or both inputs may be fixed”; (2) explicitly discard a finite prefix to arrange nonnegative truncation levels; (3) use the nonzero set of the cutoff instead of its topological support; (4) call the second proof stage “Two inputs of the same ordinary type.” Each point is already addressed in the audit's sequential checks and changes no inference. The source map records exact submitted and integrated hashes.

## Release checks

Both audit runners exited0. All full records have been read; the limits audit discharges the addition audit dependency. There are113 completed reports:107 correct and6 historical adverse, whose findings were resolved at earlier checkpoints. The five integrated sources match the source map. Final layout, production and archive checks are recorded below after the build.


The final book is570 pages, with32 chapters and an appendix. All9 initial new/interface pages,27 grouped-preview contents/chapter-interface/research/bibliography pages, and4 final regrouped pages were rendered and viewed. The last pagination change affected only physical304–307; all other page text is identical to the previously reviewed grouped preview. The production PDF has identical full per-page text to the reviewed private final. No errors, undefined references or overfull boxes occur; the existing underfull bibliography line was visually reviewed.

Removing three pagination guards and undoing the four recorded wording clarifications exactly recovers the submitted sources. Allfive integration hashes and both submitted hashes match. All29 original SGPT sources, checkpoint21 and the17-page standalone note are unchanged. The immutable release record is `research/audits/build-snapshot-22.json`. Independent source-package validation is recorded separately in `research/audits/source-package-portability-22.json`.
