# Model-reference equations: integration review

Checkpoint23 completes the arbitrary-model equation reconstruction in Chapter14. Its setting is an arbitrary smooth big real background, BMP and a model reference with positive lower relative volume. Closedness and semipositivity of the background are not imposed. The main theory of the book continues without a standing BMP assumption.

## Mathematical scope and dependencies

Four separately scoped Rethlas audits passed:

| Submission | Audit | Detailed records read |
|---|---|---|
| `section_big_relative_projection.tex` | `big_relative_projection_01` | 5 sequential, 3 reference |
| `section_big_model_measures.tex` | `big_model_measures_01` | 12 sequential, 4 reference |
| `section_big_unrestricted_addition.tex` | `big_unrestricted_addition_01` | 15 sequential, 2 reference |
| `section_big_model_lp.tex` | `big_model_lp_01` | 4 sequential, 3 reference |

All final reports and failed-check channels were read. No mathematical error or gap was found within their stated premises. Allfour runners exited0. The projection audit's initial failed reference retrieval was resolved by the primary official web source; the channel explicitly records that resolution. The other failed-check channels record no mathematical findings. A delayed persistence of the model-measure audit's sixth sequential record was retried through the normal verifier tools; the record includes its correct logical position. The root agent did not edit verifier memory or results. Transport and review timeouts recovered through the normal authorized runner; no unresolved approval rejection remains.

The dependency chain is acyclic. Relative projection produces the supersolution used by the model-measure existence proof. That existence proof uses the previously audited restricted addition theorem, not the new unrestricted theorem. Once existence is established, the unrestricted theorem follows. The concave-envelope lemma and relative moment estimate are independent of new existence; only their final Lp existence corollary uses the general-measure theorems. All conditional dependencies are discharged by the corresponding passed audits. The audits are bounded mathematical checks, not formal verification or novelty certification.

## Points requiring care

Positive lower ordinary-type volume first gives a genuine stretched envelope near slope one. The mixed-mass estimate uses positive products in a dominating Hermitian background, including a constant-truncation argument for unbounded averages. Interpolation then controls upper volume. The cross-class rooftop between the model and a minimal-class solution is constructed from these stretched competitors; same-class rooftop closure is not applied to different classes. Relative projection uses a contact tail and fixed quasi-continuous weights.

The model-measure proof maximizes the mass of weighted supersolutions between a nonzero lower measure and the prescribed finite measure. Genuine potential limits are established before fixed-dominator continuity is invoked. Weak convergence of the weighted measures is combined with fixed-measure L1 convergence of bounded exponentials and continuous L1 approximation. This identifies the weighted limiting measure before a residual supersolution is added. Density truncation gives general finite non-pluripolar data. At exponent zero the subsequence retains its original reciprocal exponents; the scalar is unique, while the normalized potential need not be.

For unrestricted addition, only the datum weights are initially truncated. A first moment with one fixed rooftop gives a genuine limit in the relative class. A second rooftop, involving that limit and both inputs, localizes the equation before the input order is known. Bounded products in a dominating positive background are expanded before the cutoff, retaining the signed smooth factors. Monotone convergence then removes the cutoff. Strict domination gives the input order and uniqueness afterwards. The undamped exponentially weighted measure may have infinite mass. Its addition law is commutative and associative because the weighted-measure map is injective; no identity element is asserted.

The relative boundedness estimate begins with a potential in the envelope class, not with ordinary reference type. Local bounded truncations in the exact background justify the inverse convex chain without assuming any open set where the model is locally bounded. A concave weight with bounded slope is chosen for each finite depth. Its slope bound may depend on that depth; the moment and envelope-normalization estimates do not. An absolutely continuous scalar differential inequality bounds the depth, including the initially infinite-depth case. The proof uses a uniform unrooted moment of order m>2n+1. Li's Theorem5.1 assumes ordinary type in advance and uses m>n; that theorem is method attribution, not an input supplying the desired ordinary type.

## Equivalent volume hypotheses

The book does not claim a stronger version of Li's theorem by deleting metric PVP. Under BMP, choose C>0 with theta<=C omega. The already proved lower-volume monotonicity, with the big first background theta and phi preceq0, gives

    0 < lowerVol_theta(phi) <= lowerVol_(C omega)(0) = C^n v_-(omega).

Thus the model's positive lower volume already implies metric PVP. Listing BMP and the positive-volume model is an equivalent organization of the cited regime once that reference is fixed. Chapter13 explains this implication directly; Chapter14's opening and Chapter32 point back to it. This does not establish an arbitrary-big-background model-reference equation without BMP. The earlier minimal ordinary-type Lp theorem already has neither metric volume assumption, and the separate semipositive general-measure construction has no BMP assumption.

## Source integration

The four staged mathematical sources remain unchanged. Production adds five pagination guards: two in the projection section, two in the model-measure section and one before the Lp section. The model-measure closing paragraph is shortened to a forward reference to the Lp estimate; the theorem statements and proofs are unchanged. Removing those guards and restoring the recorded paragraph recovers allfour submissions exactly.

The other five integrated sources are Chapter13, Chapter14's input list, Chapter32, the earlier relative-foundations section and the minimal-measures section. Their changes remove obsolete missing-proof labels, explain the equivalent volume hypotheses and point to the completed arguments. The map `big-model-equations-map.json` records before/after hashes and exact differences for those existing sources, as well as all submitted hashes. No standard environment or differential convention is changed.

The current README, plan, comparison, reading guide, literature ledger and proof obligations are synchronized. Historical checkpoint records and historical literature notes retain their original status statements. The source package includes the four submissions, their bounded audit reports and this integration record. The release and independent portability checks are recorded below once completed.


## Completed release checks

The final book has582 pages,32 chapters and an appendix. All32 initial preview pages,13 grouped/hypothesis pages,14 final prose/grouping pages and9 last regrouped pages were rendered and viewed. The last pagination adjustment changed only physical311–319; all other page text matches the previously reviewed final preview. The complete production page text equals the reviewed private final. All new theorem statements remain grouped; no overflow, clipping or missing content was found. The log contains no errors, undefined references or overfull boxes. Its one existing underfull bibliography line was visually reviewed.

Allten integration hashes and allfour staged hashes match. Removing five pagination guards and restoring the shortened transition exactly recovers the submissions. All29 original SGPT source files, checkpoint22 and the17-page standalone note remain unchanged. There are117 completed bounded audit reports:111 correct and6 historical adverse with resolved findings. No current audit or adverse finding remains. The immutable snapshot and metadata are `output/snapshots/checkpoint-23.pdf` and `research/audits/build-snapshot-23.json`. Independent source-package checks are recorded separately in `research/audits/source-package-portability-23.json`.


The first independent source build exposed a reproducibility issue confined to the standalone note: its dynamic title date changed from September15 to September16. Every other page was identical. The note source now fixes September15,2026, matching the delivered version. This adds a tenth mapped source change and leaves the delivered note PDF byte-identical. A fresh package and fresh independent builds verify this correction; no mathematical source changed. The initial failed comparison was not treated as a pass.
