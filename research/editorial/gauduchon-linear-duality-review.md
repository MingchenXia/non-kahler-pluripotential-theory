# Compact Gauduchon tests and linear thresholds

23 September 2026. Checkpoint92. Focused mathematical and exposition review, not a whole-book certification or a novelty claim.

## Scope and dependencies

Chapter 4 now contains the common zero-Gauduchon-degree lemma and Section 4.4 on the compact weak closure C_omega of smooth strictly positive normalized Gauduchon tests. It proves the exact linear minimum for kappa, its polar characterization using every smooth possibly nonclosed pseudoeffective background, order-norm Lipschitz continuity, and stability of minimizing tests under uniform changes of the background. Smooth attainment is characterized by smooth dd^c-exactness at the threshold.

The inputs are the internally proved Gauduchon and generalized Lamari theorems and attained linear threshold, classical elliptic regularity, compactness of finite measures, and Hahn–Banach separation. No Monge–Ampere mass property, current-current product or new Popovici input is used. The zero-degree lemma explicitly applies in dimension one; the compact/polar section retains Chapter 4's n>=2 convention.

Chapter 26 reuses the compact current set and the zero-degree lemma. The nonlinear determinant duality remains over the entire current set G_omega: equality of its value with the smooth supremum follows from the smooth equation and density approximation, not a false assertion that smooth positive Gauduchon forms approximate every current. The smooth-positivity/nefness criterion retains all dimensions. Its dimension-one current set is explicitly the singleton {1/integral h}, by elliptic regularity and the maximum principle. Only the new comparison with kappa is stated for n>=2. Chapter 28 adds the strict threshold comparison furnished by its existing exceptional-curve example. The old example and the smooth-cone theorem and proofs are unchanged.

## Verification and second pass

Normal Rethlas run gauduchon_linear_test_closure_01 returned correct, with no critical errors or gaps, under the listed accepted inputs. The complete saved report was read. It verifies the zero-degree and smooth-attainment assertions, compactness/metrizability/convexity, separation in the weak current topology, the correct polar domain, threshold continuity, minimizer stability, and three specified applications. This does not independently certify all earlier chapter results or nonlinear equation arguments.

The primary pass reread Chapter 4 and the relevant energy/compactness interfaces, the Chapter 26 weak-current duality and zero-attainment proofs, the smooth-cone/flow section, and Chapter 28's exceptional-curve and divisorial-test interfaces. In the polar converse, the separating test is a smooth form beta-kappa(beta)omega; no pairing between two nonsmooth currents occurs. Positivity and fixed trace bound all coefficients, so weak convergence against smooth tests agrees with convergence against continuous coefficient forms on the compact family. The metric root argument is used only for n>=2. The final dimension-one clarification prevents the moved compactness reference from narrowing the pre-existing theorem. All 27 earlier formal blocks in the five edited inputs are identical; three new blocks are added.

The primary second pass retained the exact statements and clarified the dimension-one reuse. Final visual review placed the short threshold inequality inline and kept the comparison paragraph together. The final page-break polish changes only physical pages 530–531; both were rendered and reread. The other 69 selected images match the read preview pixel for pixel. All 71 selected pages cover the complete Chapter 4, all changed substantive page texts, cross-references, the affected Chapter 26/28 transitions and bibliography. This is a focused visual and proof pass, not a new complete audit of every chapter touched by citation reflow.

## Published references

GL22 now uses Algebraic Geometry 9(6)(2022),688–713, DOI 10.14231/AG-2022-021. Its existing cited Theorem 1.5 (pp. 693–694), Theorem 2.3 (p. 695), Proposition 2.8 (pp. 698–699), Proposition 3.3 (p. 700), Lemma 3.6 (p. 703), Theorem 4.9 (p. 708) and Theorem 4.12 (p. 709) were checked in the journal PDF. Their numbers and the cited assertion scopes agree. This is a citation-version check, not a new complete proof audit of that paper.

Collins21 now uses Pure and Applied Mathematics Quarterly 17(3)(2021),1061–1082, DOI 10.4310/PAMQ.2021.v17.n3.a10. Theorem 2.13 and its full Gauduchon alternative proof on pp. 1068–1069 were read in the publisher PDF; the adjacent setup and Remark 2.14 were also checked. The locators are unchanged. The book continues to reconstruct the smooth calculation internally. Publication metadata were checked from the journal copies; no MathSciNet metadata were inferred. Both downloaded journal copies have distinct names and appended manifest entries; earlier source copies are preserved.

Primary journal PDFs: https://content.algebraicgeometry.nl/2022-6/2022-6-021.pdf and https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806163826494091265-1806163826494091265-bedcecbd6bce0caa95aa288f19fdf8da.pdf .

## Build, preservation and remaining boundary

The 714-page production build has no errors, unresolved references, duplicate labels or overfull boxes. One inherited bibliography underfull paragraph remains. The six-input house audit has 0 errors and 4 inherited warnings: chapter-label conventions and the recognized Gauduchon/Lamari titles. All 178 earlier reports, 29 SGPT originals, four supplied source/bibliography originals, checkpoint91 and its source archive, the 17-page companion and the three inactive Nakamaye files remain unchanged. The original adverse regularity report remains adverse; the inactive nef incomplete-metric draft remains explicitly unverified.

See gauduchon-linear-duality-map.json and ../audits/build-snapshot-92.json for hashes and scope. Clean archive reconstruction is recorded separately in ../audits/source-package-portability-92.json and must pass before calling this a checked release. Linear compactness does not imply nonlinear mass control or regularity of a minimizing current. The broader book goal remains active and incomplete.
