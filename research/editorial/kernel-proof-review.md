# Simpler partial-kernel proofs

Focused primary-agent review for checkpoint73, based on checkpoint72 commit 5f32a7f50b6d14bf83885625c284eb4cab3b65c4. The revision changes exposition and the zero-space convention in a displayed definition, not a formal theorem. No new Rethlas run is claimed.

## Scope and mathematical checks

The pass reads Chapters21,22 and28 and all their nested inputs: weighted spaces, trace section obstructions and Hopf sections; intrinsic flag counts, the auxiliary point blowup and Hopf flag; partial envelopes, the Fubini--Study upper bound, birational kernels, isolated-pole kernels and the Hopf point equilibrium. This is a bounded reread using the previously documented standard local and source-book inputs. It does not replace their existing verification records.

The initial kernel extremal formula is now a supremum over the Hilbert unit ball. When the selected space is zero its only competitor is the zero section, so the formula literally gives zero. When the space is nonzero, homogeneity gives the same quotient supremum as before. The change is compatible with the later Bernstein--Markov estimate, which takes a supremum over one section and introduces no dimension factor. The later compactness and ideal-order proof still separates nonempty indices and retains the thin-set obstacle argument.

For strict concavity of the determinant functional, equality in the sum of squared projection errors implies that multiplication by the real continuous function f maps the selected space into itself. Equality in L2 is equality everywhere because the difference is continuous and the volume is strictly positive. Choose a nonzero section s and its holomorphic product representative s-tilde. On a ball where s is nonzero, s-tilde/s=f is real and holomorphic, hence constant. The identity theorem on the connected manifold extends s-tilde=c s globally, and continuity gives f=c everywhere. This removes the characteristic-polynomial argument. It does not assume that the complement of the section's divisor is connected. The nonempty-space hypothesis remains essential and unchanged.

For the Hopf point model, 0<=r_m<=m means that the j=m term occurs in every binomial sum. Hence t^m<=P_m(t)<=1. Since D_m>=1 and log(D_m)/m is uniformly bounded, U_m lies between log(t composed with pi) and one fixed constant away from the pole fiber. In local submersion coordinates, log(t composed with pi)=log|z|^2+O(1); this is integrable in every positive transverse complex dimension. The already proved pointwise limit and this single integrable majorant prove whole-sequence L1 convergence directly. No compactness extraction or mass estimate is needed. Extended values on the pole fiber and the independently proved total-variation measure convergence remain as before.

The remaining checks preserve the distinction between line-bundle curvature and an arbitrary nonclosed background; between singular selecting weights and continuous norm weights; between the original multiplier ideal and its Jacobian-corrected birational transform; and between necessary section obstructions and existence. The lattice period, intrinsic lattice normalization, dimension-zero count, and auxiliary unweighted section identification retain their hypotheses. The Kähler modification and positive-mass hypotheses remain in the imported equilibrium limit. The general lower Fubini--Study asymptotic is still not asserted.

## Preservation and output

All eight complete prior formal statements and all labels in the edited files are unchanged. The reversible map records the three proof/definition changes and pagination adjustments. The short zero-scale corollary remains with its proof, and the direct logarithmic L1 estimate remains with its integrability explanation.

The house audit has zero errors and two inherited chapter/figure-label warnings. Rephrasing the equality case resolves the earlier generic continuity warning; no new diagnosis is introduced. The final book build, rendered page inspection, page-text comparison and source reconstruction have their exact scopes in build-snapshot-73.json and source-package-portability-73.json. The original SGPT files, checkpoint72 book and archive, companion note, and all verifier records remain preserved. No independent verification is claimed for these elementary proof simplifications.

Continue improving the existing manuscript and researching the unresolved equation, singularity and geometry questions after this checkpoint.
