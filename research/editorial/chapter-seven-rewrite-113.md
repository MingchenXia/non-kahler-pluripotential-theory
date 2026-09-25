# Chapter 7 rewrite — checkpoint113

Baseline: `579dc9c63e6b0d8b54baaeac86b4fe6c50cb1ed5`. This continues the user's chapter-by-chapter rewriting instruction, with Chapter 7 and its nested general-weight input treated as one complete unit. Earlier structural edits in other chapters do not count as their completed rewrite.

## Argument and exposition

The chapter is now *Weighted Monge–Ampère measures*. Its seven sections develop bounded-range mass growth, exponential damping, capacity bounds, polynomial damping, capacity continuity, the uniform-tail criterion and smooth backgrounds. Each opening explains the next mathematical step. The ambient manifold and metric are carried forward; the abbreviations for the extended measure and range exponent occur once. Repeated capacity and product definitions, repeated qualifications about bounded mass, and recaps that only restated a result are removed. The nested general-weight discussion retains its logarithmic endpoint example and sufficient integral condition.

The existing example following damped continuity said that epsilon U had infinite mass for every epsilon>0, and referred to a witness before identifying the stronger coefficient-integrable construction needed for its current convergence. The revised passage explicitly chooses the witness used in the strong-linear-convergence corollary and keeps 0<epsilon<1, exactly as in that corollary. No theorem is strengthened or weakened by this correction to the application.

## General inputs and reading order

The bounded products with smooth backgrounds, including their full positivity proof, move from the start of Chapter 6 to Chapter 1. The bounded convex chain rule moves from Chapter 7 to the same first-chapter input. The local cutoff calculation is recorded once in the local capacity section, including its degree-one stopping form. Chapter 7 applies that inequality with the global Gauduchon trace bound and the exact top-wedge cancellation.

The Hermitian capacity definition moves from Chapter 7 to Chapter 1. The general volume–capacity and normalized-sublevel estimates, with the Lp density corollary and their complete proofs, move from Chapter 10 to Chapter 1. Bounded smooth-background products precede their use in the capacity definition, so no backward dependency on the measure or equation chapters is introduced. Local-to-global capacity comparison, capacity convergence and bounded-product continuity are placed beside that definition. Later bounded-product references are repaired. Those six later inputs are reviewed only at the changed dependencies, not as whole chapters.

There remain 33 active chapters; the first chapter has 23 sections, Chapter 6 has five and Chapter 10 has ten. There are 209 active author inputs. Paper citations remain confined to the historical chapter. Only the already used books support the relocated classical calculus; no paper metadata or source-verification status is changed.

## Direct mathematical checks

Both full direct reads of Chapter 7 and its nested input are complete. The review checks the Gauduchon trace estimate, the degree-one local cutoff bound, the exact top-wedge cancellation, positive convex composition, removal of pole sets, uniform exponential and polynomial tails, capacity domination of truncated products, and the order of the fixed-truncation and infinite-level limits. It also checks the construction of an increasing integrability weight, the projective-line counterexample, the common subsequence for every fixed shallow level in the smooth mass-defect example, and signed theta-products on truncations formed in the larger positive background.

The moved bounded-product and capacity arguments received first/second direct reads in their new order. The cutoff functions, their ranges and support, fixed constants, normalized L1 input and positivity of the compared products remain explicit. The general-weight condition is sufficient; no necessity or optimal endpoint is added.

Across the 13 changed author inputs, 61 of 66 labeled formal blocks are unchanged. Five have only the documented explicit range quantifier, shortened constant dependence or removal of repeated definitions/qualifications. No formal block is removed or added. Of 57 proof environments, 51 are unchanged and six replace a relocated calculation by its internal reference, update a dependency, or remove a stage-direction sentence. These comparisons support preservation; they are not independent verification.

## Release checks and remaining work

The expanded house-audit baseline and final audit both have eight inherited label/remark errors and eighteen warnings. The Chapter 7 pair alone has no errors and only the existing chapter-label warning. No new finding is introduced. The final book has 810 pages. Compilation has no errors, unresolved references/citations, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. All 106 selected book pages passed visual inspection. The 17-page companion is byte-identical to checkpoint112. Both outputs rebuilt in a fresh empty extraction, with every reconstructed page text matching production. Exact output hashes, page selection and reconstruction checks are recorded in build-snapshot-113.json and source-package-portability-113.json.

The independent proof queue remains at Section 12.2; the chapter-rewrite queue advances to Chapter 8. Q2.8 and the broader research/writing goal remain unfinished. All 190 historical verifier reports and all hidden Nakamaye sources are unchanged; no new verifier run, literature coverage or novelty judgment is claimed.
