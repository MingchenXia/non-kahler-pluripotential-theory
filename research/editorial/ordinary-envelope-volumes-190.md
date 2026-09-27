# Ordinary envelopes and singularity volumes — checkpoint190

Baseline: `6f6e185e7855514a353ba082463fe9631e6c1690`. The preceding goal turn completed checkpoint189 and verified its private backup, so it was progress. The checkout was initially clean.

## Mathematics

Chapter 29 Section 29.3 now contains strict domination and its weighted-order corollary, moved with their proofs from Chapter 31. The reference needs positive lower volume; the proof never requires it to be an ordinary envelope fixed point. The normalization is performed in two stages: translate u and v together to put v below the reference, then translate all three to put the reference below zero. Relative full-mass equivalence supplies the positive lower mass used in the collapse contradiction.

Lemma 29.3.1 proves the contact estimate for P_theta[u](w), assuming the initial rooftop is genuine. The moving contact contribution is bounded by the finite tail of MA(u). Weighted lower semicontinuity first gives measure domination and then, using the fixed positive-part weight, support on contact with w. Chapter 31 uses this lemma instead of repeating its definition and proof.

Theorem 29.3.2 proves that the ordinary envelope preserves lower singularity volume. When that lower volume is positive, it also preserves upper volume, gives relative full-mass membership and is an ordinary envelope fixed point. For p=P_theta[u] and any w of ordinary type p, the increasing rooftop limit r satisfies p-K <= r <= w <= p+K. The lower inequality follows from the competitor P_theta(u+C+K,0)-K. Thus r has ordinary type p before volume equality is used. Domination identifies r with w, and lower semicontinuity compares its mass with the upper volume of u. Relative full-mass equivalence gives lower-volume equality. The zero-lower-volume case follows directly from monotonicity.

Corollary 29.3.2 characterizes both relative full-mass classes by ordinary envelope equality for positive-lower-volume model references. Proposition 29.6.1 therefore needs only positive lower volume of the ideal envelope, in the chapter's bounded-mass big-background setting. The former extra relative-class premise is removed. Problem 29.6.1 now asks for positivity criteria in ideal/divisorial terms and for the implications that survive at zero lower volume. This narrows the book's research question without claiming a new literature-wide open problem. Chapter 32 and final historical Chapter 33 are synchronized.

## Sources and review

The complete Chapter 29 input received an original read and two complete direct revised mathematical/editorial reads; the second followed the first build and visual review. The Chapter 31 foundation and projection inputs were read completely at those stages, and the Chapter 32 singularity discussion and Chapter 33 Sections 33.8 and 33.9.3 were read as bounded interfaces. The Chapter 30 opening transition was consulted. The Lp and unrestricted-addition inputs in Chapter 31 were read completely for their changed page breaks; only three spacing commands are added across these two files, with all mathematical text verified unchanged. This is not a complete new Chapter 31 or whole-book review.

Across the seven changed author inputs all old labels remain; three results/proofs/labels are new and two results/proofs move from Chapter 31 to Chapter 29. Chapter 29 grows from eleven to sixteen formal statements and nine to fourteen proofs. Eight of its nine prior proofs retain their mathematical text; the I-envelope proof is shortened through the new characterization. Its model-continuity proof receives only paragraph/spacing changes. The moved weighted-order corollary and the retained fixed-measure continuity theorem and their proofs are unchanged. Four prior formal blocks change as listed in the focused audit; all others remain byte-identical. The bibliography and active input graph are unchanged.

[Li's exact version 1](https://arxiv.org/html/2601.13446v1), Proposition 3.2, Lemma 3.2, Proposition 3.3 and Corollary 3.3, were checked with their complete relevant arguments. The book explicitly supplies the comparison of r with P_theta[u] and uses a fixed positive-part contact weight, repairing the two displayed/wording issues recorded in the focused audit. Proposition 3.4 was consulted, but idempotence here follows from the book's prior relative-envelope equality. Proposition 3.5(i) remains a next-unit lead. This is a scoped source reconstruction, not a fresh full-paper dependency audit. No new external unproved premise, novelty claim, Popovici reliance or independent verifier run is made. Supplied integrations, including Q8.2, remain intact; there was no new author intervention requiring a skill change.

The second pass shortens the I-envelope converse, removes revision-history language from reader-facing discussion and corrects the split model-continuity display and three short Chapter 31 statements. It also eliminates the avoidable final problem-only page of Chapter 29.

## Release checks

Both production outputs compile. The book has 819 pages and the companion seventeen; the companion is byte-identical to checkpoint189. Final logs have no errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph remains. The main house audit has zero errors and 27 warnings, all reproduced in the same-scope baseline; the two additional layout-only inputs have zero errors and zero warnings.

The first selection has 76 pages, with 54 changed images directly inspected and 22 matching the previously inspected render byte for byte. Its layout issues were corrected during the second pass. The intermediate review directly inspected all 52 changed images and identified the final short-statement split, which was then corrected. The final selection has 82 pages, with 2 changed images directly inspected and 80 matching the inspected intermediate render. It covers the complete Chapter 29 and transitions, bounded Chapter 31/32/33 interfaces, contents and every other changed body page. All final selected pages pass. The active graph remains 33 chapters and 221 author inputs.

Both outputs rebuild from a fresh empty source-package extraction, and every page text agrees with production. The final package manuscript and build scripts match that rebuilt payload. All 221 active author inputs are included. The 190 historical verifier reports and three hidden Nakamaye sources remain unchanged; the hidden sources remain excluded. See build-snapshot-190.json and source-package-portability-190.json.

## Continuation

Investigate increasing ordinary-envelope and singularity-volume continuity under positive lower volume, and its consequences for approximation of singularity types; keep arbitrary L1 or divisorial convergence separate. Li Proposition 3.5(i) is a lead. The broader writing and research goal remains active and incomplete.
