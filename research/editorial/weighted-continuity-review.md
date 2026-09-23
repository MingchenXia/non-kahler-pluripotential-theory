# Weighted measure continuity — checkpoint87

## Scope

Move the existing arbitrary-background weighted lower-semicontinuity lemma from Chapter 32 into the common-barrier foundations of Chapter 13. Replace the earlier semipositive-only version and keep both stable labels on the single lemma. Chapter 32 cites it without repeating the proof. This consolidates a result already proved in the book; it does not introduce a new equation or extend a mass-dependent continuity theorem.

The lemma assumes a smooth real background, potentials with a common upper bound converging in capacity, and uniformly bounded nonnegative quasi-continuous weights converging in capacity. Either integral can be infinite. Bigness, semipositivity, bounded mass and positive lower mass are unnecessary for this lemma. All 13 other formal statements in the three edited inputs are byte-for-byte unchanged. The bounded-subsolution input receives only a page-space control. The combined label set is unchanged.

## Proof review and second pass

At each fixed truncation level, enlarge the background to a Hermitian metric. The truncated potentials are uniformly bounded in this larger background; the original smooth-background products may be signed. Expanding in the positive Hermitian products bounds every signed term's total variation by bounded mixed measures. The earlier mixed-capacity lemma therefore supplies a bound independent of the sequence index, with the truncation level fixed. Bounded capacity continuity applies term by term.

Separate the moving-weight error from the fixed quasi-continuous weight. Capacity domination controls the first; for the second, remove a set of small capacity, extend the weight continuously from its closed complement, and control the discarded integral. The cutoff vanishes at the truncation level, so locality identifies the resulting measure with the positive extended measure. Its integral is nonnegative, including when it is zero. Monotone convergence then removes the cutoff off the ignored pole set. No subtraction of infinite measures occurs.

The monotone observation retains the earlier necessary repair: a decreasing sequence must have a genuine limit or a known genuine lower bound; an increasing sequence of genuine potentials must have a common upper bound. Truncation in a Hermitian background and capacity decay of the fixed lower bound's deep sublevels prove the asserted convergence. This does not say that a merely upper-bounded decreasing sequence has a genuine limit.

The focused primary reread covers the common-barrier section, the relative dominated and moving-measure arguments, the arbitrary-background weighted limits, and the Chapter 32 foundations and first-moment interface. The bounded-product and damping inputs were checked at the relevant capacity/locality passages; no full new review of Chapters 6–7 is claimed. The second pass clarifies the convergence targets, removes the repeated binomial display, and keeps the lower-barrier proposition and mixed-density lemma statements together. The signed-product caveat remains beside the cutoff operation.

## Existing independent evidence

No new Rethlas run was started. The complete saved reports big_relative_foundations_01, common_barrier_compactness_01 and common_barrier_repair_01 were reread. The first verifies the arbitrary-background cutoff argument under its five stipulated internal premises. The historical common-barrier report has verdict wrong because its standalone monotone observation omitted the genuine-limit hypothesis; its actual barrier applications passed. The later bounded repair checks that hypothesis and its uses under the original accepted inputs. The present text preserves that repair. These reports are evidence for their stated scopes, not a new independent verification of this edit or of the entire book.

No external result or bibliography entry is added. No Popovici result or private-reference content is used. The two existing preprint prompts in the substantive inputs, and the additional existing Nguyen16 prompt in the spacing-only input, are unchanged bibliographic review prompts.

## Validation and preservation

The final preview has 684 pages. The house audit of all three changed inputs has zero errors and three existing preprint warnings. Compilation has no errors, unresolved references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. All 66 first-preview selected pages were rendered and read. After the second pass, all 66 were rendered again: 51 changed images on 13 sheets were read, and 15 were pixel-identical to the first reviewed images. This selection covers all 21 changed page texts relative to checkpoint86.

Every production page text matches the final reviewed preview. Build details and clean source reconstruction are recorded separately in build-snapshot-87.json and source-package-portability-87.json; the latter must pass before the release procedure is complete. Checkpoint86 and its source archive, the unchanged 17-page companion note, all 29 original SGPT files, all 172 saved verifier reports and the three inactive Nakamaye sources are preserved. The source map retains before/after text and hashes. There is no whole-book correctness certification; the general infinite-rooftop, exact-equation and singularity-topology questions retain their recorded status.
