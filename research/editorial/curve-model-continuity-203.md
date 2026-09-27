# Curve model convergence — checkpoint203

Baseline: `f433603652de6fc15dcccd7204547dff8a4f4a02`, including the author's cover-subtitle removal. The last turn rechecked that completed correction without changing manuscript state. This continuation revalidated the pending five-input draft and completed the queued continuity unit. All ten supplied integrations retain their completed scope.

## Mathematics

Section 29.12 now proves that metric convergence of normalized ordinary curve models implies L1 and capacity convergence, including zero-mass limits. At zero mass, full curvature currents converge in total variation with an explicit bound. Chapter 1 supplies the local variation-capacity estimate. Weak curvature convergence is distinguished from capacity convergence, and a moving pole on the projective line gives capacity convergence at constant model distance 2. Chapters 15, 32 and 33 record the implications and proof mechanism.

For the planar estimate, decompose ddc(u-v) into its positive and negative parts on the larger disc. Their negative Dirichlet Green potentials have L1 norms bounded by their masses, uniformly over the pole; the logarithmic kernel proves this directly. The remaining distribution is harmonic. Its interior supremum is bounded by the L1 norm of u-v plus the total variation of its Laplacian. Almost-everywhere order identifies the quasi-subharmonic representatives off polar sets. The weighted Chern–Levine–Nirenberg inequality and bounded test-mass estimate bound the integral of the absolute difference against every capacity test. These test measures charge no polar set. Markov's inequality yields the capacity bound. The constant depends only on the two fixed discs.

For model convergence, the polar classification makes the non-pluripolar masses converge. A positive limit mass gives a common positive lower bound and invokes the existing separation and capacity theorem. At zero limit mass, the limiting polar part is the whole current. The residual positive current of each approximant has mass tending to zero, giving the factor-two total-variation estimate. Normalized compactness and harmonic uniqueness identify every L1 cluster limit; the local estimate and a finite coordinate cover then give capacity convergence.

The weak-convergence distinction uses the area-one finite-atomic construction already proved in Chapter 15, scaled to the chosen area and applied to the zero potential. Its approximants and limit are ideal models. All approximants have zero non-pluripolar measure, so damped capacity continuity rules out capacity convergence to zero. In the moving-pole example, the explicit Fubini–Study potentials have supremum zero and full atomic curvature. They converge uniformly off any small fixed disc around the limiting pole; the capacity-tail bound makes the omitted disc negligible. The two different Dirac masses have total-variation distance 2 at every stage.

## Review scope and source boundary

The complete Section 29.12 and local-capacity input receive two direct mathematical/editorial reads, the second after the first build and visual inspection. The Chapter 29 opening and Chapters 15/32/33 interfaces receive bounded reviews. Three statements and proofs and five labels are added. All forty-nine prior Chapter 29 statements are byte-identical; forty-five prior proofs are byte-identical, and the atomic-completeness proof is clarified to use the sets of atoms instead of the ambiguous word supports. Five author inputs change; all prior labels, the bibliography and input graph remain. No new external premise, full external proof audit, novelty claim or independent verification is introduced. See research/editorial/curve-model-continuity-203.md and research/audits/curve-model-continuity-203.json.

The second pass specifies the weak limit as the current of the proposed limiting potential, states uniformity of the Green-kernel L1 bound in the pole precisely, and separates the harmonic L1 contribution in the introduction. It also clarifies the countable carrier in the old atomic-completeness proof: topological supports of atomic measures need not be countable. The new conclusions keep a fixed smooth positive curve background. Higher-dimensional zero-volume continuity, infinite mass and degeneration remain outside this unit. No new author correction requires a skill change.

The local-capacity input, global-capacity and normalized-compactness arguments, positive-volume capacity proof, atomic model description, finite-atomic L1 approximation and normalized trace interface were consulted at the dependency scopes needed here. The complete damped-continuity input was reread. Existing classical book inputs retain their scope; the bibliography is unchanged. This is not a new whole-Chapter-1 or whole-Chapter-29 audit, and no independent verifier was run.

## Release checks

The 857-page book and seventeen-page companion compile without errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph and template warning remain. The scoped house audit has zero errors and 30 inherited warnings. All 90 selected final pages pass visual review: 4 changed images directly inspected and 86 identical to an inspected preceding render. The first review directly inspects 69 images. The companion is byte-identical to checkpoint202. The 33-chapter, 221-input graph remains unchanged.

The selection covers all of Section 29.12 and its transitions, the complete local-capacity input, bounded interfaces, front matter and every other changed body page. Visual review is carried forward only for byte-identical rendered images. The cover remains without its subtitle.

Both outputs rebuild from a fresh empty source-package extraction, and every page text agrees with production. The final package manuscript and build scripts match that rebuilt payload. All 221 active author inputs are included. The 190 historical verifier reports and three hidden Nakamaye sources remain unchanged; the hidden sources remain excluded. See build-snapshot-203.json and source-package-portability-203.json.

## Continuation

Compare all curve models under changes of smooth positive background, including zero residual mass, and determine which identifications preserve the total-variation metric. The broader writing and research goal remains active and incomplete.
