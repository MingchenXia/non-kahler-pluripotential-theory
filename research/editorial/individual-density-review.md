# Individual L1 densities: integration review

22 September 2026. Checkpoint39 adds Section13.23 and refines the individual equation problem in Section32.2. The prior whole-manuscript root pass is complete; the new section has its own bounded mathematical review. No novelty claim is made.

## Mathematical result

For a Hermitian form h and a nonzero nonnegative L1 density f relative to a smooth positive volume, let c_h(q) be the normalization constant for the continuous equation with bounded density q, without normalizing the integral of q. The decreasing limit b_h(f)=lim c_h(min(f,k)) is the maximum coefficient a>=0 for which some genuine h-psh potential has extended Monge–Ampère measure at least a f dV. The maximum is attained. The potential may be unbounded and may have infinite undamped mass. The result assumes neither BMP nor positive lower mass.

The bounded-comparison lemma extends the previous smooth comparison by checking exactly what that proof uses: its first potential is bounded, so every translate has a smaller-background envelope; the arbitrary candidate is more singular. Zeros of the bounded test density are permitted. Strict domination gives the necessary inequality with the correct orientation. It also proves monotonicity and inverse homogeneity of the scalar.

For sufficiency, continuous equations for the truncations supply normalized potentials. The tail upper envelope of an L1-convergent subsequence is bounded for each fixed tail, but there is no uniform bound over the tails. Finite maxima preserve the lower density bound by ordered contact. Bounded increasing continuity then gives the inequality for each tail envelope. The tail envelopes decrease to the genuine limit; quasi-continuity and Dini imply capacity convergence. Exponential damping gives a finite weak limit, and dominated convergence handles the weighted right side. Division occurs first on {u>-N}, followed by exhaustion. This only proves an inequality, as required.

The threshold agrees with the continuous equation scalar for Lp data, p>1, by the existing uniform compactness theorem. It is bounded below by lower mass divided by the integral of f. For a Kähler background it is exactly the cohomological volume divided by that integral. These conclusions use bounded Stokes or the stated Lp theorem, not an assertion that all unbounded potentials have conserved mass.

## Why the older smooth test is insufficient

The counterexample assumes v_-(h)=0. It first selects smooth probability densities of arbitrarily small scalar. L2 continuity of the scalar permits each to be cut down to a closed nowhere dense set while retaining its small scalar. The positive summation weights are chosen recursively after the earlier sets: their future total is smaller than a specified fraction of the volume left in each of finitely many basis open sets.

This order of choices is essential. A fixed arbitrary diagonal sum would not ensure an essential lower value on every open set. Here Markov's inequality leaves positive volume where every finite initial sum is zero and the remaining tail is arbitrarily small. Thus Q has essential infimum zero in every nonempty open set, while 1+Q dominates all the small-scalar tests. Normalizing f=(1+Q)/M gives b_h(f)=0 by the bounded-comparison lemma.

Any smooth g dominated by R f almost everywhere must be bounded by R/M everywhere. Otherwise continuity creates an open set contradicting the essential lower-value property. Scalar order and homogeneity give R c_h(g)>=M c_h(1); the constant g=1 attains equality. Hence the old smooth-test quantity is strictly positive. This settles negatively the positivity question in the earlier research note. It does not disprove sufficiency of the new bounded-test criterion for subsolutions, which is proved in the preceding theorem.

## Review evidence and editorial changes

The normal Rethlas run `individual_density_subsolutions_01` returned `correct`, with no critical errors or gaps and normal runner exit 0. The root read all 16 statement records, six reference records, the no-failed-checks record, final reports and verdict. The complete source, immutable submission and final result remain separate from the production source. There are now 134 completed bounded reports: 128 correct and six preserved historical adverse reports whose findings were resolved. A bounded audit is not whole-book certification.

The audited section received only three editorial changes: a shorter subsection heading, replacing “bounded normalizers” by “normalization constants for bounded densities,” and a pagination guard keeping the definition of M with its following inequality. Exact changes and hashes are in `individual-density-map.json`. No mathematical hypothesis or conclusion changed.

Chapter13 includes the section immediately after the universal lower-mass obstruction. Chapter32 records the established subsolution criterion and asks whether the exact equation at b_h(f) exists, with its appropriate singularity/envelope class. The Lp special case follows from the new proposition and the already proved continuous equation. The Kähler case follows from the standard full-mass existence theorem in SGPT and the cohomological formula. These editorial interfaces were checked by the root separately from the Rethlas submission.

The 653-page preview was compiled without errors, undefined references or overfull boxes; the existing underfull bibliography paragraph remains. The new section, its neighboring transitions, the contents entry and the revised research-program pages were rendered and read. Final production comparison and clean reconstruction are recorded in build-snapshot39 and the portability audit.

## What remains open

The proof supplies a maximal scaled subsolution coefficient, not an exact equation theorem at that coefficient. It does not prescribe the ordinary or ideal type of the maximizing potential, prove that its undamped mass is finite, or supply capacity convergence for the original normalized equation solutions. Arbitrary non-pluripolar measures still require an extension beyond smooth-volume densities.

`individual-density-followup.md` records root deductions about upper L1 semicontinuity, relaxation and finite sums, conditional on this threshold result. Those deductions have not yet received a bounded independent review and are not included in the book. They must not be treated as part of the passed audit.

An exploratory primary-source check also located the March2026 preprint arXiv:2603.26406v1, *Continuity of the complex Monge–Ampère operator on compact Hermitian manifolds*, and its publisher record. Its abstract discusses continuity and a smooth-subsolution application; it is not used as proof of the present arbitrary-L1 threshold. The proof here uses the precise reconstructed dependencies listed in the submission. No broad literature-priority conclusion follows from that search.
