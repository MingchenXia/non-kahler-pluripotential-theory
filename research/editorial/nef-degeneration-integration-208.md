# Nef degeneration orders and authorless-paper policy — checkpoint208

Baseline: `7e3517fe1432753164312fefcde3917274883e7c`. The user supplied Q3.6 for integration, then clarified that manually supplied papers without an author need neither citation nor GitHub backup. The ongoing book goal remains active.

## Mathematical integration

Section 25.16 now proves fractional, irrational and unequal degeneration orders on elliptic products, comparison under arbitrary modifications, strict jumps under a single smooth-center blowup, and monotonicity under positive-current subtraction with a nef residual. Explicit examples separate zero order from positive limiting volume and distinguish perturbative minimal multiplicities from the divisor of an actual minimal boundary current. The remaining order question is narrowed to equality and geometric restrictions; Chapters 25 and 32 explain the new boundary.

The elliptic calculation solves a mean-zero scalar Poisson equation and produces a Gauduchon minimizer. Flat coefficients with controlled logarithmic derivatives give genuinely different lower and upper orders. The modification proof first establishes pullback nefness, then repairs a pulled-back test by adding a positive test. Exceptional-divisor curvature bounds the numerator uniformly over the whole downstairs test cone; the cofactor determinant controls the denominator even at the exceptional locus. Both estimates are needed before taking the infimum.

For the strict blowup examples, the existing smooth equation supplies the base metric. Closed Stokes and the radial reference masses determine the constants. The singular integral has power, logarithmic and integrable regimes, giving the stated orders and loss of positive limiting volume. The residual comparison retains nefness on both backgrounds. The two-point surface blowup shows why this condition cannot be omitted. Perturbative minimal divisorial multiplicities vanish for nef backgrounds; the existing unique-current ruled surface instead has a nonzero divisor at the boundary, and removing it changes order one to two.

## Review and dependencies

The complete five-input Section 25.16 receives two revised mathematical/editorial reads, the second after first compilation and visual inspection. Ten results and ten proofs are added; the two original propositions and proofs remain byte-identical. Chapter 25/32/33 interfaces receive bounded reviews, and the neighboring current-test input changes only spacing. This is a section integration, not a whole-Chapter 25 revision.

All six supplied TeX inputs, including every proof, were read. PDF text confirms source numbering; no complete source-PDF visual review or new independent verification is claimed. The archive and member hashes in the audit identify the unchanged local evidence, not a bibliographic citation or a copy of the paper. The main integration dependencies and their exact read scopes are recorded in the accompanying audit. In particular, the existing ruled-surface proof is reused, and the smooth equation is consulted at setup/statement and closure scope rather than newly audited in full.

The analytic domination by smooth-center blowups remains a named classical geometric input. The published AKMW principalization/domination passages (Sections 1.2.3–1.2.4, pp. 538–539) and analytic extension (Section 5.4, p. 564) were checked in the primary author-hosted text. This is not a complete audit of Hironaka resolution or the AKMW factorization theorem. Its citation remains in Chapter 33.

The second read moves pullback nefness before the quotient comparison and makes the return from the elliptic example to arbitrary manifolds explicit. It also clarifies the residual notation. Layout reviews keep displayed calculations, their lead-ins, a proposition and section openings together; the neighboring current-test changes are spacing only.

## Author instruction and skill maintenance

The author's 27 September instruction removes all eleven previously retained bibliography entries for manually supplied authorless papers and omits an entry for the new source. Source-only historical recaps are removed; independently used authored dependencies remain cited. Original papers are local, ignored by Git and excluded from the source archive. The four changed book-skill files are synchronized with the installed copy; both copies pass the official validator, with linked-file and scoped behavioral checks.

The citation exception is confined to manually supplied authorless papers. Retained AKMW and SGPT citations were used as countercases against deleting all source attribution. The project plan and current blueprint state the exception, and the integration queue marks its earlier citation descriptions as historical. Existing Git history and historical verifier reports are preserved. Original source files are neither added to the repository nor included in the source package.

## Release checks

The 870-page book and seventeen-page companion compile without errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph and template warning remain. The scoped house audit has zero errors and one inherited label warning. All 76 selected final pages pass visual review: 3 changed images directly inspected and 73 identical to inspected preceding renders. The companion is byte-identical to checkpoint207. The book retains 33 chapters and now has 225 active author inputs.

The first visual review directly inspects 52 images, the first intermediate review 18 and the second intermediate review 49. Only byte-identical images carry those checks into the final selection. The unchanged cover retains no subtitle. Both outputs rebuild from a fresh empty source extraction, and every page text agrees with production. The final manuscript and build-script payloads match that rebuilt package. All 225 active inputs are included; the 190 historical verifier reports and three hidden Nakamaye sources remain unchanged, with the hidden inputs and supplied original papers excluded. See build-snapshot-208.json and source-package-portability-208.json.

## Continuation

Review and rewrite the complete four-input Chapter 22, reconciling divisorial currents and exceptional-divisor formulas with intrinsic trace-envelope pullback, while distinguishing numerical compatibility from realization of an ordinary type. This integration does not complete that queued chapter or the broader book goal.
