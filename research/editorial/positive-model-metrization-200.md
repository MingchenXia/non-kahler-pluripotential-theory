# Positive-volume model metrization — checkpoint200

Baseline: `e322be41bda8b8a699641ed442055d72e393511a`. The preceding goal turn completed checkpoint199 and private synchronization, so it was progress. All ten supplied integrations remain complete. This continuation completes the queued triangle and metrization unit.

## Mathematics

New Section 29.11 gives a triangle-inequality counterexample for the upper-volume formula using intersecting divisors on the projective plane. It proves lower-volume continuity and constructs a complete compatible metric on all positive-lower-volume ordinary models. A sequence is Cauchy for the new metric precisely when it is Cauchy for the upper-volume comparison and its reciprocal lower volumes form a Cauchy sequence. On every fixed closed positive-lower-volume sector the comparisons are uniformly equivalent. Positive-volume ideal models are a closed complete subspace and the metric completion of positive-volume analytic ordinary models. Bounded mass and a fixed smooth big background remain assumed. Chapters 15 and 32 narrow the remaining topology questions; Chapter 33 distinguishes the original comparison from the new compatible metric.

For the counterexample, rational 0<a<1/2 gives u=a log(|Z0|^2/|Z|^2), v=a log(|Z1|^2/|Z|^2), w=u+v. Their masses are (1-a)^2, (1-a)^2 and (1-2a)^2. The maximum has an isolated singularity at the intersection point; it is not bounded there. On the blowup, its residual form is (1-a)pi*theta+a f*omega_1, whose square integrates to 1-a^2. Thus d(u,v)=4a-4a^2 exceeds d(u,w)+d(w,v)=4a-6a^2 by 2a^2. Ordinary projection preserves these comparisons and analytic types. All three models retain positive lower volume.

Finite-deficit stretching in both directions gives the lower-volume modulus. At an arbitrary positive ordinary-model limit, stretching first derives an eventual common lower bound; no uniform lower bound on the input sequence is assumed. This supplies continuity before the metric construction.

The complete metric uses symmetric pair sets defined by reciprocal normalized lower-volume differences and comparison thresholds epsilon_k min(m(p),m(q))^a_k. The recurrence a_(k+1)=n a_k+1 cancels the lower-volume denominator in the three-point modulus. Reciprocal control along a three-edge chain bounds all four lower volumes by a common factor of their minimum. Choosing the epsilon sequence small enough proves triple composition. The finite-chain cost is the sum of dyadic edge weights. Induction on the number of edges, splitting at the first crossing of a half-dyadic threshold, proves the two-sided inclusions needed for separation and topology. Concatenation gives the triangle inequality for this new metric, not for the original volume formula.

Metric Cauchy sequences have bounded reciprocal lower volumes and hence a tail in a fixed closed positive sector. The earlier Cauchy-completeness theorem supplies their limit; lower-volume continuity converts this to metric convergence. Conversely, upper-volume-comparison Cauchy sequences with Cauchy reciprocal lower volumes satisfy every pair threshold. The lower-volume modulus makes the two comparisons uniformly equivalent on fixed positive sectors. The earlier ideal-model closure and analytic approximation identify the complete analytic closure. No canonical metric values, zero-volume extension or whole-book completion are claimed.

## Sources and review scope

The complete new Section 29.11 receives two direct mathematical/editorial reads, the second after the first build and visual inspection. The Chapter 29 opening/comparison transition and Chapters 15/32/33 interfaces receive bounded reviews. Four statements, four proofs and ten labels are new; two questions are narrowed. All forty previous Chapter 29 statements and thirty-seven proofs are byte-identical. Four author inputs change; all prior labels, the bibliography and input graph remain. Li version 1 explicitly allows failure of the triangle inequality; the relevant statement context is rechecked. The finite-chain argument is proved internally. No new external premise, complete source-proof audit, novelty claim or independent verification is introduced. See research/editorial/positive-model-metrization-200.md and research/audits/positive-model-metrization-200.json.

Before drafting, the comparison and Cauchy arguments, the analytic criterion, the bounded-residual mass polynomial/change-of-variables argument and the projective normalization examples were read at their dependency scopes. The source statement check uses XL26 Section 4.2, arXiv:2601.13446v1: the source already describes its function as a semi-metric that may fail the triangle inequality. This example is not presented as a correction to a source triangle claim. The previous recorded proof-reconstruction scope is retained. A search for the historical Frink paper did not obtain primary full-text access; no unchecked citation locator was adopted. The standard chain argument is included in full, without a novelty or independent-verification claim.

The second pass sharpens the positive-volume qualifier in the analytic-density statement, keeps the example lead-in with its display, and then keeps the complete metric statement on one page. No substantive author correction requires a skill change in this continuation. Unchanged chapter material is not represented as newly reviewed.

## Release checks

The 851-page book and seventeen-page companion compile without errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph remains. The house audit has zero errors and 29 inherited warnings. All 45 selected final pages pass visual review: 3 changed images directly inspected and 42 identical to an inspected preceding render. The first and intermediate reviews directly inspect 26 and 5 images respectively. The companion is byte-identical to checkpoint199. The 33-chapter, 221-input graph remains unchanged.

The selected pages cover the entire new section and its transitions, the Chapter 29 opening and changed comparison transition, front matter, bounded Chapter 15/32/33 interfaces and all other changed body pages. Exact image equality carries prior visual review; page-text matching alone does not.

Both outputs rebuild from a fresh empty source-package extraction, and every page text agrees with production. The final package manuscript and build scripts match that rebuilt payload. All 221 active author inputs are included. The 190 historical verifier reports and three hidden Nakamaye sources remain unchanged; the hidden sources remain excluded. See build-snapshot-200.json and source-package-portability-200.json.

## Continuation

Analyze the zero-lower-volume boundary on curves: determine which ordinary models it contains and whether the upper-volume topology and analytic-completion criterion extend to it. The broader writing and research goal remains active and incomplete.
