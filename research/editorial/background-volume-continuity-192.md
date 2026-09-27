# Background variation and singularity volumes — checkpoint192

Baseline: `2d00c1cd74e91e51486655ed9410532b3de09aed`. The previous goal turn completed checkpoint191 and verified its private backup, so it was progress. The checkout was initially clean.

## Mathematics

Chapter 29 Section 29.4 now collects positive-volume strict barriers. The complete small-stretch lemma and strict-barrier corollary move here from Chapter 31, with stable labels. The mixed-mass error remains explicit. The smaller-background proposition now follows directly by subtracting a sufficiently small multiple of the background from the strict current; its statement is unchanged.

Proposition 29.4.2 gives a quantitative comparison for both singularity volumes. If u has positive lower volume and theta <= eta <= theta + epsilon omega, a fixed strict lower potential supplies delta > 0 such that vol_theta(u) <= vol_eta(u) <= (1 + epsilon/delta)^n vol_theta(u). Addition and background/potential monotonicity prove the estimate for the upper and lower volume separately.

Section 29.5 is Monotone limits. Theorem 29.5.2 now allows smooth backgrounds theta_j decreasing in form order and converging uniformly to the smooth big limiting background theta. For decreasing ordinary model potentials q_j with positive-lower-volume limit q, both singularity volumes decrease to those of q, which is an ordinary model in theta. The proof first retains the fixed-background deficit and compactness argument. A strict potential w <= q, convex corrections f_j, upper-regularized tail suprema F_j and ordinary projections r_j give a decreasing family of theta-model potentials between q and q_j. Their fixed-background continuity squeezes the varying-background volumes. Background comparison then makes the volume deficit tend to zero, giving uniform Lelong convergence on each fixed smooth compact modification.

Proposition 29.5.1 likewise extends the decreasing-sequence criterion: under the same background and positive-lower-volume hypotheses, ordinary-envelope convergence is equivalent to upper-volume convergence. Then lower volumes and Lelong numbers converge too. Corollary 29.5.1 treats a fixed potential and proves ordinary-envelope and both-volume continuity under decreasing backgrounds. The increasing theorem and exact-trace corollary keep their previous mathematical scopes. Chapter 31 reuses the relocated lemma. Chapters 32 and 33 record the exact conclusions and source distinctions.

## Sources and direct review

The complete Chapter 29 input and complete Chapter 31 relative-projection input received an original read and two direct revised mathematical/editorial reads. The second revised read followed the first build and visual review. The Chapter 32 singularity-topology section and trace transition, and Chapter 33 Section 33.8, subsection 33.9.3 and their adjoining transitions received bounded reads. Earlier internal dependencies were consulted at the relevant complete proof scopes; this is not a new whole-book review.

Chapter 29 grows from eighteen formal statements and sixteen proofs to twenty-two statements and twenty proofs: two statements/proofs are relocated and two are new. Two earlier Chapter 29 statements are strengthened to allow decreasing backgrounds. The relocated strict-barrier statement deletes the redundant word relative but changes no hypothesis. Thirteen of sixteen old Chapter 29 proofs are byte-identical; the other three are the two extended arguments and the shortened smaller-background proof. The strict-barrier proof is unchanged. The small-stretch proof expands notation inherited from its old chapter and reformats its mixed estimate. The Chapter 31 relative-projection input keeps three statements, with two retained proofs byte-identical and the cross-class rooftop proof using explicit references to the relocated lemma. All prior labels remain; three labels are added. Four author inputs change. The bibliography, 33-chapter structure and 221-input graph are unchanged.

[Li's version 1](https://arxiv.org/html/2601.13446v1), Proposition 3.1 and Proposition 3.5, were read with their complete relevant statements and proofs. The new adoption is the positive-lower-volume part of 3.5(ii)--(iii). The source states backgrounds theta + epsilon_j omega; the book's strict-correction and tail-envelope construction proves the ordered uniform-background version directly and does not rely on the source's Dini reduction. The zero-lower-volume assertion and its additional BGL dependency are not adopted. Existing references retain their recorded source scopes. No new unproved external premise, novelty claim, Popovici reliance or independent verifier run is made. All supplied integrations, including Q8.2 in Sections 14.8–14.10, remain intact. No new author intervention requires a skill change.

The second pass makes the almost-everywhere-to-pointwise order for tail envelopes explicit, removes one redundant word, repairs the mixed-product display and adjusts the section, trace-statement and Chapter 31 proof breaks. These local adjustments preserve the mathematical argument.

## Release checks

The 823-page book and seventeen-page companion compile without errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph remains. The companion is byte-identical to checkpoint191. The house audit has zero errors and 27 warnings, all reproduced in the same-scope baseline. Paper citations remain confined to final Chapter 33.

The first selection has 68 pages: 44 changed images were directly inspected and 24 matched the inspected checkpoint191 images. An intermediate inspection directly checked 9 changed images and found two remaining breaks. The final selection has 68 pages: 7 changed images were directly inspected and 61 match the inspected intermediate render. It covers all of Chapter 29 and its transitions, the relocated material and changed Chapter 31 pages, bounded Chapter 32/33 interfaces, contents, and every other changed body page. All final selected pages pass.

Both outputs rebuild from a fresh empty source-package extraction, and every page text agrees with production. The final package manuscript and build scripts match that rebuilt payload. All 221 active author inputs are included. The 190 historical verifier reports and three hidden Nakamaye sources remain unchanged; the hidden sources remain excluded. See build-snapshot-192.json and source-package-portability-192.json.

## Continuation

Investigate the zero-lower-volume boundary of decreasing-model lower-volume continuity, reconstructing the specific mass semicontinuity input before extending Chapter 29; keep upper-volume and envelope equality as separate obligations. Li Proposition 3.5(ii) and its cited mass input are leads, not imported zero-volume conclusions. The broader writing and research goal remains active and incomplete.
