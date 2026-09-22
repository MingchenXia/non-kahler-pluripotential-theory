# Selected Gauduchon sequences and proof reuse

This follow-up concerns Chapter27 and its research-program references in Chapter32. It adds a sufficient condition for one maximizing sequence, rather than claiming uniform control over all normalized Gauduchon currents. The previous root-tail condition remains the hypothesis in the theorem representing all supporting probabilities. No priority claim is made.

## Mathematical check

Let p be a nonzero nonnegative element of the finite root space, and write R=rho_omega(p). For a weakly convergent maximizing sequence T_j, suppose the weighted densities p k_Tj are uniformly integrable. The sets {p>K} have volume tending to zero because p belongs to Ln. Uniform integrability makes their weighted masses uniformly small. For bounded truncations p_K, the already proved upper semicontinuity applies to every bounded measurable weight h p_K with h continuous and nonnegative. The truncation error tends to zero uniformly in j. Thus the upper bound for integrals passes to the unbounded weight along this particular sequence.

Taking h=1 gives D_p(T)>=R, while the global supremum formula gives D_p(T)<=R. For any weak limit mu of the weighted measures, testing all nonnegative continuous h gives mu<=p k_T dV. Their masses are both R, so equality identifies the limit. This proves weak convergence of these measures. It neither uses nor proves unrestricted upper semicontinuity of D_p. Compactness of the current family then gives attainment whenever such a maximizing sequence exists, without p in D_omega^0.

If the normalized determinant-weighted probabilities have uniformly bounded entropy, their high-density tails satisfy integral_{a_j>K} a_j <= (H+1/e)/log K. The 1/e term bounds the possible negative entropy contribution on a probability volume space. This proves uniform integrability. The factors d_j tend to R and are therefore uniformly bounded, so multiplying by d_j preserves this property. The selected-sequence proposition applies. Division by d_j shows convergence of the probabilities to R^(-1) p k_T dV along any convergent current subsequence.

The entropy-to-first-moment calculation from checkpoint64 was also submitted in this check. Truncate a normalized potential before applying the entropy inequality, then use monotone convergence; the desired integrability is not presumed. On passing to the limiting probability, -v is nonnegative and lower semicontinuous, so the lower bound for integrals under weak convergence preserves its first-moment bound. No trace pairing with a singular current is introduced.

## Simplifying an existing proof

The supporting-probability proposition already assumes p in D_omega^0. For fixed F, solidity places p exp(F/n) in that same space, and the preceding theorem gives uniform integrability of its weighted densities. The new proposition therefore supplies the two conclusions formerly proved there with positive and negative continuous perturbations: a near-maximizing weak current limit is a maximizer, and its weighted measures converge. Reusing that proposition removes the repeated limit argument. The determinant concavity, affineness, Taylor expansion and separation steps are unchanged.

The dependency order is noncircular. The new proposition uses only the bounded-weight part and the supremum formula of the earlier integrable-current theorem. The supporting-probability theorem follows afterward and uses it. The full root-tail theorem retains its global upper-semicontinuity assertion and its separate proof.

## Scope of rereading and output checks

The root reread covered the four edited sources and the complete weak-current duality, determinant integrability, root-uniform-tail and normalization chapter sources, as well as the new proposition and entropy paragraphs at statement-to-proof scale. This is a targeted dependency review after the recorded whole-book passes; it is not a third complete pass. The new proposition uses a standard environment without an optional title. Existing theorem statements and labels are preserved. A separated introductory line and its display in the supporting-probability proof were kept together during layout review.

The source map records reversible edits. Compilation, page checks, report counts, source preservation and fresh-package reconstruction are recorded in the checkpoint audits. The independent run selected_gauduchon_limits_01 returned correct, with no critical errors or gaps. It checks the selected-sequence proposition, the entropy-to-moment calculation, the entropy tail bound and the passage of moments to the limiting probability, using the stated accepted inputs. The proof reuse and layout integration were checked directly in this review. Frozen proof drafts, verifier input, result and memory were preserved.

## Remaining questions

Uniform integrability along one maximizing sequence gives no smoothness of its limiting current and no exact equation by itself. Entropy supplies both this condition and the first moments required in the conditional equation theorem, but it supplies no smaller-background envelope of Phi_f. The unrestricted positive-threshold equation problem at zero lower mass, equality of the finite root space with its bounded-root closure, and regularity of singular maximizers remain open here. No necessity of the selected-sequence condition or equivalence with the global tail condition is asserted.
