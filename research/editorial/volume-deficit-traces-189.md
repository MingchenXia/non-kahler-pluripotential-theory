# Volume deficits and exact traces — checkpoint189

Baseline: `67771f7eda4b0340e152c7b2dec3cb1b18dadd1e`. The preceding goal turn completed checkpoint188 and verified its private backup, so it was progress. The checkout was initially clean.

## Mathematics

Chapter 29 separates the quantitative stretching argument from its zero-deficit full-mass consequence. If u is more singular than v, delta is the positive lower volume of v, and D is the difference of their upper volumes, every stretch b greater than one with b^n D less than delta has a genuine envelope. A representative of u whose mass is sufficiently close to its upper volume supplies the strict deficit. If the truncated stretching envelopes collapsed, their contact support would put their masses below this deficit, contradicting their common lower-volume bound.

Proposition 29.2.1 combines this construction with Chapter 1's uniform Lelong estimate. The Lelong difference is at most C_pi min(1,(D/delta)^(1/n)), uniformly at every point of each fixed smooth compact modification. The constant depends on that modification and the background; it is not asserted uniform over all models. The cases D=0 and D at least delta are included. The former yields the previous full-mass theorem, with its statement unchanged and its duplicate collapse argument removed.

For decreasing ordinary model potentials with a limit of positive lower volume, the upper volumes are Cauchy. Applying the deficit lemma to two terms and taking ordinary envelopes normalizes the auxiliary potentials. Compactness then passes the convex comparisons to the limit. Monotonicity, addition and homogeneity squeeze both volumes to their limiting values. The quantitative estimate gives uniform pointwise Lelong convergence on each fixed compact model. This proves Theorem 29.3.1 in a fixed smooth big background.

Corollary 29.3.1 applies on Y to ambient trace data. Assume bounded mass on Y and choose Omega at least twice a Hermitian Omega0 above the restricted ambient background, with v_-(Omega)>0. Every representative ordinarily equivalent to the trace envelope admits a half-background competitor, giving lower volume at least 2^(-dim Y) v_-(Omega). The restricted dyadic analytic envelopes decrease to it, so the model theorem identifies every limiting divisor order with the prescribed trace number. The ambient manifold remains arbitrary. The substantial mass hypotheses remain in their designated part of the book. Chapter 18 points forward, and Problem 32.8.1 now concerns failure of at least one mass property. Arbitrary-background ordinary-type compatibility and realization outside the established regimes remain unresolved.

## Sources and review

The complete Chapter 29 input received an original read and two complete direct revised mathematical/editorial reads. The second revised read followed the first build and visual review. Bounded revised interfaces are Chapter 18's final discussion, Chapter 32's trace question and recovery transition, and Chapter 33 Section 33.8. Earlier internal inputs were consulted at the scopes recorded in the focused audit. This is not a fresh whole-book proof audit or independent verification.

All seven prior Chapter 29 formal statements and all eleven old labels remain. Four statements/proofs and four labels are added, giving eleven formal statements and nine proofs. Four of five old proofs are byte-identical; the relative full-mass converse is shortened through the new lemma. Five sections replace four. Chapter 32's one narrowed question is the only changed prior formal statement. Only four author inputs change; the bibliography and input graph are unchanged. The second pass makes the big-background contact dependency explicit, shortens the model-continuity introduction and compactness passage, and removes a repeated trace-setting reference.

[Li's exact version 1](https://arxiv.org/html/2601.13446v1), Lemma 3.1 and the fixed-background positive-lower-volume part of Proposition 3.5(ii), were read with their complete relevant proofs. They supply the source comparison for the internally reconstructed arguments. The changing-background reduction, adjacent ordinary-envelope claims and later singularity-distance statements are leads rather than newly accepted premises. The source check changed the initial plan: volume continuity is now proved in the fixed-background model regime, so the trace result is not left conditional on that continuity. Earlier accepted dependencies keep their original scope. No novelty claim, new Popovici reliance, bibliography addition or new independent verifier run is made. Supplied integrations, including Q8.2, remain intact; no new author intervention calls for a skill change.

## Release checks

Both production outputs compile. The book has 819 pages and the companion seventeen; the companion is byte-identical to checkpoint188. Final logs have no errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph remains. The house audit has zero errors and 28 warnings, all reproduced by the same-scope baseline audit.

The first selection has 40 pages, with 22 changed images directly inspected and 18 matching the previously inspected render byte for byte. The final selection has 40 pages, with 3 changed images directly inspected and 37 matching the inspected first render. It covers all Chapter 29 pages and transitions, the bounded interfaces, contents and every other changed body page. The active graph remains 33 chapters and 221 author inputs.

Both outputs rebuild from a fresh empty source-package extraction, and every page text agrees with production. The final package manuscript and build scripts match that rebuilt payload. All 221 active author inputs are included. The 190 historical verifier reports and three hidden Nakamaye sources remain unchanged; the hidden sources remain excluded. See build-snapshot-189.json and source-package-portability-189.json.

## Continuation

Examine preservation of singularity volumes by the ordinary envelope and the extra relative-class assumption in the I-envelope characterization, reconstructing the required domination and projection steps. Li Lemma 3.2 is a lead. In particular the identification of the relative obstacle envelope with its target must be justified without assuming the volume equality being proved. The broader writing and research goal remains active and incomplete.
