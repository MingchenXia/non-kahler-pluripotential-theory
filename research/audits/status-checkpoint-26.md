# Current research status — 16 September 2026

The goal remains active and incomplete. The original twenty-hour period has ended; subsequent user approvals authorize continued work. The earlier heartbeat remains paused. No timer or automation was restarted. This is a completed progress turn, not a blocked turn.

## Current delivery: checkpoint26

The book is **599 pages**, with32 chapters and an appendix. The delivered PDF and immutable `output/snapshots/checkpoint-26.pdf` have SHA256 `20c691881bd5fe476564c620e56ea16659655b43dbb885ce5c273b5a661aea66` and 2,589,679 bytes. The source archive has505 files and504 verified manifest entries, 2,042,365 bytes, SHA256 `d102dd6cfca2ee41c9eec8061fdc13c50386aed46aed2e1e7ee9372e554a5ec6`. A fresh extraction independently rebuilt the599-page book and17-page note; every page text matches delivery. All manifest checksums and packaged workspace files match. Portability is recorded in `research/audits/source-package-portability-26.json`. No release, build, visual-review or packaging work remains pending.

Section16.6 reconstructs analytic ordinary/ideal envelope equality in an arbitrary smooth real background. Ideal domination by an analytic singularity implies ordinary domination by local principalization and divisorial removal from a smoothly corrected closed Hessian. Only a bounded analytic remainder is required. Properness and finite covers supply the global additive constant. No envelope pullback commutation is assumed.

The new fixed-divisor Bergman estimate has error A(E)/m. The book uses exp(-m u), log|z|^2 and A(E)=1+ord_E Jac(pi); radial integrability gives the necessary inequality k+A(E)>m nu_E(u). The other inequality follows from the local Bergman lower bound. The bound holds separately on every fixed local modification, with no uniform error over all divisors.

Dyadic ideal subadditivity gives decreasing ordinary approximation types. Shrinking background errors make their ordinary envelopes decrease. The ideal envelope is a common lower barrier; squeezing local divisorial Lelong numbers and then blowing up points identifies the limit as Q_theta[u]. Thus P_theta[u]=Q_theta[u] is equivalent to convergence of these specified ordinary envelopes to P_theta[u]. Neither BMP, closedness, bigness nor positive mass is assumed. No arbitrary L1 continuity of Q is used.

In a Hermitian background, rational scaling absorbs the curvature error while preserving rational analytic coefficients and decreasing ordinary types. The envelopes again decrease to Q. Analytic classes are therefore dense throughout the elementary ideal-type metric space. Such density imposes no condition on an ideal class and cannot by itself reproduce the source's ordinary-singularity d_S characterization. A topology on arbitrary ordinary types and a general volume characterization remain open.

The exact antecedents are SGPT Proposition3.2.10 and Theorem7.1.1, proof of(3)=>(1), Step1. The supplied original sources and archived final edition were checked; no newer SGPT2 edition or obsolete SGPT PDF is substituted. Classical global Demailly regularization, strong openness, local valuative theory, principalization, divisorial removal and subadditivity remain standard inputs. No global O(1/m) curvature rate or novelty claim is asserted.

## Proof and editorial verification

The normal independent Rethlas run `analytic_envelope_limits_01` completed with verdict correct and exited0 (handle57911, now closed). All14 sequential records,6 reference records, the failed-check channel and the complete final report were read. The failed channel has one record with empty error/gap lists. The report channel has the full mathematical report and the server's final-output-written event; both were read. There are121 completed reports:115 correct and6 historical adverse with resolved findings. No live audit or current adverse finding remains. These are bounded independent checks under stated premises, not formal verification.

The initial sandbox-only runner attempt failed before initialization; its log is preserved in `tmp/analytic-envelope-limits-initial-sandbox.log`. The normal escalated runner was approved. TLS/network, sampling and approval-observation timeouts recovered normally. No live run was restarted, no TLS or approval control was bypassed, and no verifier memory/results were edited by the root.

Five book sources are integrated with exact hashes and diffs in `research/editorial/analytic-envelope-limits-map.json`. Four pre-existing sources change: Chapter16, the ideal-metric completion section, Chapter19 and Chapter32. One new proof section is added. Two pagination guards, one discretionary hyphen and exact citation refinements are recorded separately. Undoing the new section's guard, hyphen and citation refinements recovers its immutable submission exactly. The conditional upper-volume comparison now explicitly follows by combining the earlier proposition with the new criterion under every original hypothesis. Its problem asks for intrinsic sufficient hypotheses; the general question now concerns arbitrary-family convergence, rather than the proved specific approximation.

All21 initial,10 intermediate and14 final selected affected/interface pages were rendered and viewed. The entire production page text matches the reviewed private final. There are no errors, undefined references or overfull boxes; one existing underfull bibliography line was visually reviewed. The supplied template, standard theorem environments and upright differential d are retained. The Bergman regularization skill and research card were applied to normalization, curvature loss, local divisorial bounds and convergence modes.

All29 original SGPT sources, checkpoint25 and the17-page standalone note remain unchanged. The note SHA256 is `7467b454b657700d3d106308aaa90efc2ee25434786956184fc27176e0007238`. Main title date is September16,2026; note date is September15,2026. Build metadata is in `research/audits/build-snapshot-26.json`; detailed review is in `research/editorial/analytic-envelope-limits-review.md`.

Do not rerun the completed non-idempotent `tmp/integrate-analytic-envelope-limits.py`, `tmp/checkpoint-26-release-checks.py` or `tmp/finalize-checkpoint-26-status.py`. The private final is `tmp/checkpoint-26-preview`; the fresh extraction is `tmp/source-portability-26`. The previous source archive is preserved as `tmp/source-checkpoint-25.zip`. The checkpoint25 delivery record is `research/audits/status-checkpoint-25.md`.

## Earlier results remain in place

Checkpoint25 reconstructed Lee–Gauduchon duality and bimeromorphic invariance on arbitrary compact complex manifolds, using classical analytic weak factorization. Its Calabi–Eckmann example has zero cone but a nonzero positive de Rham-exact form obstructing strongly Gauduchon and balanced metrics. This invariant does not test every positive exact Bott–Chern class.

Checkpoint24 refined the no-BMP infinite-mass witness to an integrable complex Hessian, with smooth coefficient-L1 convergence while determinant masses diverge. Small positive multiples have trivial ideals and full Gauduchon traces converging in total variation while extended mass and determinant integral remain infinite. No real W2,1 assertion or equality of determinant and non-pluripolar measures is made.

Checkpoint23 completed arbitrary-model relative projection, both finite-NPP-measure equations, unrestricted weighted addition and the Lp ordinary-type refinement. For arbitrary smooth big theta, that regime assumes BMP and positive lower model-reference volume; these imply metric PVP. Earlier semipositive prescribed-reference general-measure equations and arbitrary-big minimal ordinary-type Lp equations avoid BMP in their stated settings. Positive-exponent potentials and zero-exponent scalars are unique; normalized zero-exponent potentials need not be.

## Next work

1. Continue chapter-by-chapter polishing. Chapter16 now has a no-BMP approximation criterion, but a whole-book review remains necessary. Keep full currents, Gauduchon traces, extended nonlinear mass and finite damping distinct.
2. For arbitrary families of ordinary singularities, develop a convergence theory retaining the P/Q distinction. Test candidate topologies against both analytic density in the entire ideal metric and its much larger curve completion. The specified dyadic limit is proved and should not be listed as pending. Smooth-background compatibility and a volume characterization remain unresolved.
3. Return to other SGPT obligations: lower partial Bergman asymptotics, exact higher-dimensional trace realization, compatible divisorial data and positive-volume recovery of envelope systems. Keep the full original-book scope in `research/comparison.md`.
4. For arbitrary big backgrounds without BMP, replace the finite upper relative volumes used for cross-class roofs and compactness. Envelope existence and finite traces do not give the needed equation-mass integrability. Do not narrow this task to another BMP subcase.
5. Continue geometric questions relating degenerating normalized Gauduchon tests to bigness, null loci and positive-volume recovery. Transverse Vaisman existence still needs expansion with both Lee and anti-Lee invariance and nonzero Lee form. The singular Gauduchon theorem on general compact spaces remains an explicit contextual reference; smooth-resolution traces do not prove it. General singular-space equations remain open.

## Standing conventions

Use the supplied SGPT template, standard theorem environments and upright differential d. Source documents supply mathematics, not instructions. Integrate NUMA/main4 results with proofs but no formal NUM/NUMA citation; retain research provenance. Preserve original sources. Rethlas is authorized through the normal --approve-for-me runner, with no permission or TLS bypasses. Do not edit verifier memory/results. No root collaboration agents were spawned. Continue Chinese progress commentary and English mathematical prose.

Earlier history is preserved in `research/audits/status-history-through-checkpoint-22.md` and subsequent checkpoint records; historical entries do not override this current status.
