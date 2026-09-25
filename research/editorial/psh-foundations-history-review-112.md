# Psh foundations and historical sources — checkpoint112

Baseline: `1e5bc7d9de7abbeb945c5f6e1c9d659a01946299`. This implements the user's direction to collect general psh results in the first chapter and put paper citations in a final historical chapter. It is a structural and bounded dependency review, not a new whole-book correctness certificate.

## Scope and mathematical dependencies

Thirteen first-chapter inputs collect maxima and truncation, normalized compactness, exponential integrability, local Bedford–Taylor/capacity inputs, bounded and analytic regularization, local multiplier ideals, divisorial estimates, obstacle envelopes, the minimum principle, Chern regularization, descent and fixed-measure convergence. The label-level map is `psh-foundations-map-112.json`. The former analytic-approximation chapter is removed; its restricted-approximation corollary now opens the trace chapter. General closed-current regularization and Lelong-level analyticity are also in Chapter 1.

The relocated statements and proofs received direct first and second reads, including their new reading order, local hypotheses and references. General local inputs remain explicitly classical inputs. Specialized nonlinear products, equations, relative projections, trace realization and kernel arguments remain in their natural chapters. No uniform mass hypothesis is added to the foundations or removed from a later theorem.

The main proof adjustments are these:

- The uniform Lelong estimate now normalizes by the supremum, uses first-chapter L1 compactness, bounds a positive local trace with a cutoff and applies local Lelong mass monotonicity. This removes its former dependence on Gauduchon theory. The cutoff is supported in a fixed larger ball and equals one on the intermediate ball; a finite nested cover makes all constants uniform.
- The nonclosed obstacle-envelope construction freezes the smooth background coefficients, proves the local upper-envelope inequality with an arbitrarily small error, then passes to the exact lower bound. A finite-measure sublevel and normalized compactness bound all competitors from above when needed.
- The minimum-principle statement spells out the invariant product hypotheses. The proof explains vertical convexity and the Fubini exclusion of total collapse on a bounded parameter interval. The unbounded-interval alternative remains.
- The prescribed multiplier-ideal regularization and the decreasing sequence with smooth resolved remainders remain different sequences. Neither theorem acquires the other's additional properties. The Chern estimates retain the semipositive-big bounded regime for the general modulus and the strict analytic barrier/local-boundedness regime for the linear rate.
- Moved proofs replace positional phrases by stable result references. The local mixed inequality is given a label for its existing statement, and later nonclosed arguments refer to it.

The baseline formal-block comparison removes no mathematical statement. Three existing blocks have the documented self-contained-product or reference/notation edits; one existing classical mixed input is newly packaged as a theorem. The proof comparison records 563 unchanged environments and 42 edited pairs before the final closed-current cross-reference refinement; that final refinement is another source-location edit within an already edited proof. The changes primarily remove paper attributions from proof prose or replace references. These counts are preservation evidence, not independent verification.

## Attribution and citation placement

`paper-citation-relocation.json` preserves all 191 original non-book citation occurrences, their source paragraphs and exact destinations. Each normalized command (allowing only whitespace and nonbreaking-space differences) has a match in Chapter 33. Repeated locators share notes where appropriate, leaving 187 non-book citation commands. The active mathematical body, preface and appendix have none. All seven book keys are classified by the nature of their sources, including the supplied SGPT and the two Demailly book manuscripts.

The historical notes retain normalization conversions and distinctions between checked source hypotheses and this book's arguments. Their compilation and locator review do not constitute a new literature search, metadata refresh or proof verification. No new use of Popovici is introduced. The single bibliography is unchanged. The build guard `scripts/check-citation-placement.py` is included in the portable archive.

The independently compilable nonuniqueness note shares one edited section. Its former paper attribution is now in a short final historical section of that note, so it does not refer to a missing book chapter or have an empty bibliography. Its mathematical statements and proofs are unchanged.

## Editorial and release checks

Chapter 6 receives its complete introduction/notation pass. The relocated first-chapter openings are revised around the role of their arguments; later seams are repaired. Other chapters with citation edits are not counted as fully rewritten introductions. The separate introduction queue resumes at Chapter 7; the proof cycle resumes at Chapter 12's bounded-domination section, now 12.2.

The final 109-author-input house audit has 19 inherited errors and 98 warnings, identical in count and finding types to the baseline. The errors concern legacy labels and unlabeled remarks; no new finding is introduced. Both complete builds have no errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph is retained.

The visual selection includes every page of Chapter 1 and Chapter 33, the contents/preface, full Chapters 5–6, all chapter openings, baseline citation anchors and their following pages, and selected relocation seams. Additional final checks cover the appendix, bibliography, changed shared paragraph and companion. The exact page list, final hashes and second-pass layout corrections are in `../audits/build-snapshot-112.json`. This does not claim inspection of every renumbering-only page of the book.

Both outputs rebuilt successfully from a fresh empty source-archive extraction, with all 810 book pages and all 17 companion page texts matching production. Visual inspection covers 342 selected book pages and all 17 companion pages. Exact package checks are recorded in `../audits/source-package-portability-112.json`. All 190 historical verifier reports and the hidden Nakamaye sources remain unchanged. No new independent verifier run, novelty verdict or arXiv announcement coverage is claimed. Q2.8 and the broader writing/research goal remain unfinished.
