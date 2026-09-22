# Entropy variational formula and comparison of scalar functionals

Focused review for checkpoint70, based on checkpoint69 commit efb87324eb0bb6e434acca68505a5ae13281e11a. This is not whole-book certification.

## Correction found during continuing review

Chapter19 uses the source book's convention that an analytic singularity has a positive rational logarithmic coefficient. The new example in checkpoint69 had allowed arbitrary real t in P_theta[ta] while invoking the analytic-envelope theorem. Its bounded Rethlas report accepted the indicated inputs and had not audited that convention. The parent found the mismatch by rereading the definition and analytic-type calculus. The current revision restricts t to rational numbers in (0,1), so the invoked theorem applies literally. The limit in this example is along rational t. General smaller-background parameters epsilon and the scalar comparison theorem remain real.

The prior report, its input, its submitted draft and checkpoint69 are preserved, with this correction recorded separately. No assertion of analytic-envelope equivalence for arbitrary real scaling is inferred here. The related real-parameter Bergman terminology is identified for a further focused review in the continuation notes; the real-parameter divisorial estimate should be preserved.

## Mathematical and editorial changes

A standalone measure-theoretic lemma proves the entropy variational identity for all probabilities and every smooth positive finite reference volume, including infinite entropy. A compact null set and continuous cutoffs treat non-absolute-continuity. Jensen and clipped logarithms treat the absolutely continuous case. Continuous approximation uses the finite measure dV+nu, keeping uniform bounds; the negative part of h log h is integrable. The proof does not use a closed-background scalar formula or later entropy bounds.

The closed-case entropy proposition now follows by direct substitution. Both the Hermitian entropy bounds and their prescribed-reference counterpart cite this lemma directly. The lower/upper changes of variables have coefficients 1/q and n, respectively. The former arguments extracting a measure identity from a closed-case proof and separately treating singular probabilities are removed. All their formal statements remain unchanged.

The finite quantity Delta(phi,psi)=sup_G|B_phi(G)-B_psi(G)| is a pseudometric on the admitted references. Finiteness follows from each reference's comparison with B_0; no family-wide smaller-background parameter is assumed. Its exact dual formula uses only the common finite-entropy domain, so no infinite dual values are subtracted. The reverse inequality tests the dual minimum with a support for the other reference. Fixed-pair bounded L1 continuity extends the scalar supremum to all bounded measurable tests. The existing volume transformation proves reference-volume independence.

If Delta(phi_j,phi) tends to zero, supporting probabilities for uniformly bounded G_j converging in L1 have a dual-minimization gap at most 2 Delta(phi_j,phi). One Delta comes from the scalar comparison and one from the dual comparison. A fixed H_phi sublevel supplies uniform integrability and weak L1 compactness. This justifies the varying-test integrals and identifies all cluster points with supports at the limiting reference. Whole-sequence convergence requires uniqueness of that support. The earlier zero-reference corollary keeps its complete statement and uses this general proposition in a short proof; it now follows the general result, so there is no forward dependency.

The projective example computes mass (1-t)^n for a rationally weighted hyperplane, proving sharpness of n log(1-t). On the projective line, distinct pole locations with the same coefficient have equal positive mass and Delta zero but distinct ordinary and multiplier-ideal types. The multiplier normalization is exp(-u), giving floor(mt), and the ideals differ once mt>=1. The example therefore states the precise failure of separation rather than presenting Delta as a singularity metric.

## Checks

Rethlas normalization_distance_01 returned correct with no critical errors or gaps; its actual full report was read. It explicitly checks the rational-scaling repair, entropy identity, common finite domain, measurable stability, sharpness and failure of separation, and the proposed proof reuse. No frozen verifier text or result was edited.

The new candidate texts receive only small editorial changes: a redundant sentence in the entropy statement is removed, the introduction matches the new ordering, and the mass formula stays with its explanatory sentence. Every existing formal statement block and label in the nine edited book files is preserved. The analytic example's parameter restriction is separately recorded. The reversible map contains each exact edit.

All selected output pages were rendered and read. The final build has no errors, undefined references, duplicate labels or overfull boxes; the inherited bibliography underfull paragraph and chapter-label audit warning remain. Exact hashes, counts and visual page scope are in build-snapshot-70.json. The source archive is rebuilt in an empty directory and compared page by page in source-package-portability-70.json. Original sources, checkpoint69 and its archive, and the companion note remain unchanged.

## Remaining boundary

The background is still semipositive and big and every reference satisfies the model and genuine smaller-background hypotheses. Delta convergence is a sufficient functional condition; a general geometric or ideal-theoretic criterion for it is not supplied. No potential convergence, strong L1 convergence of densities, total variation statement, completeness or separation of singularity types is claimed. Singular-reference entropy-difference extrema and the other open geometric and individual-measure questions remain open in this manuscript.
