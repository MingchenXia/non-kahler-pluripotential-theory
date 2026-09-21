# Current research status — 16 September 2026

The goal remains active and incomplete. The original twenty-hour period has ended; subsequent user approvals authorize continued work. The earlier heartbeat remains paused. No timer or automation was restarted. This is a completed progress turn, not a blocked turn.

## Current delivery: checkpoint25

The book is **595 pages**, with32 chapters and an appendix. The delivered PDF and immutable `output/snapshots/checkpoint-25.pdf` have SHA256 `c2192541659c4f5e18441f8438ae08e764d77249c2d5178eb13d6790a3832887` and 2,567,893 bytes. The source archive has498 files and497 verified manifest entries, 2,007,173 bytes, SHA256 `3e0a2e0d784e6a7c98e6f8c24be772acedc58495c91dc63f770afe8a03fd1c86`. A fresh extraction independently rebuilt the595-page book and17-page note; every page text matches delivery. All manifest checksums and packaged workspace files match. Portability is recorded in `research/audits/source-package-portability-25.json`. No release, visual-review, build or packaging work remains pending.

Section31.8 now reconstructs the Lee–Gauduchon cone from the already proved generalized Lamari criterion and full Gauduchon trace. It identifies the kernel of j_X with real parts of closed holomorphic one-forms, proves openness in the kernel annihilator, and establishes strict duality with tests only outside the entire kernel. These results hold on any connected compact complex manifold of dimension at least two, without LCK or BMP assumptions.

Closed positive currents are pulled back through local psh potentials; pushforward and elliptic regularity give pseudoeffectivity in both directions and Bott–Chern injectivity. Thom theory supplies the degree-one blowup isomorphism. Analytic weak factorization gives bimeromorphic invariance. The exact compact-complex theorem is AKMW arXivmath/9904135v4, Theorem0.3.1(2), checked in the primary source and archived. The algebraic Theorem0.1.1 is not substituted. This classical theorem remains an external reference.

The section derives the balanced obstruction, Fujiki-class vanishing and the positive half-line on the Hopf example. It then constructs the Calabi–Eckmann quotient (C2 minus0)^2/C explicitly. The smooth identification with S3 times S3 gives H1=H2=H5=0 and hence a zero Lee–Gauduchon cone. Pulling back the product Fubini–Study form from P1 times P1 gives a nonzero positive d-exact form, which obstructs strongly Gauduchon and balanced metrics. Its Bott–Chern class is nonzero and outside image(j_X). Thus neither all d-exact Bott–Chern classes nor strongly Gauduchon existence can be recovered from this degree-one cone alone. No full exact-current characterization or novelty claim is imported.

## Proof and editorial verification

Both new normal Rethlas runs are correct and exited0: `lee_gauduchon_cone_01` (handle85156), `lee_gauduchon_strong_01` (handle49968). All15+11 sequential records,4+2 reference records, both failed-check channels and both complete final reports were read. The strongly Gauduchon failed-check channel contains one record with empty error/gap lists. The audits are independent: the second example uses direct cohomology vanishing and does not assume the first audit's duality/invariance. Normal sampling/search/approval timeouts recovered; no live run was restarted and no review was bypassed. There are120 completed reports:114 correct and6 historical adverse with resolved findings. No live audit or current adverse finding remains. These are bounded independent checks, not formal verification or novelty certification.

Seven book files are integrated, with exact hashes and diffs in `research/editorial/lee-gauduchon-map.json`. The two new sections differ from their immutable submissions only by two pagination guards each. Three further guards keep existing Chapter31/32 formulas and a problem statement together. Chapter31's introduction and Chapter32's geometric connections are synchronized, as are README, PLAN, reading guide, proof ledger, comparison, literature and revision records. Only five pre-existing book files differ from the checkpoint24 source archive; two new proof files are added. Earlier volume/rigidity proofs are unchanged.

All48 initial affected/interface pages and30 final changed-region/interface pages were rendered and viewed. The entire production text matches the reviewed private final. There are no errors, undefined references or overfull boxes; one existing underfull bibliography line was visually reviewed. Both new proof sources use the established differential normalization and upright differential d. Standard theorem environments are retained.

All29 original SGPT sources, checkpoint24 and the17-page standalone note remain unchanged. The note SHA256 is `7467b454b657700d3d106308aaa90efc2ee25434786956184fc27176e0007238`. The main title date remains September16,2026; the note date remains September15,2026. Build metadata: `research/audits/build-snapshot-25.json`. Mathematical/editorial review: `research/editorial/lee-gauduchon-review.md`.

Do not rerun the completed non-idempotent `tmp/integrate-lee-gauduchon.py` or `tmp/checkpoint-25-release-checks.py`. The private final is `tmp/checkpoint-25-preview`; the fresh extraction is `tmp/source-portability-25`. The checkpoint24 delivery/continuation record is preserved in `research/audits/status-checkpoint-24.md`.

## Previous foundations and equation results remain in place

Checkpoint24 proved that under failure of BMP the convex-series witness has an integrable complex Hessian and smooth currents converging in coefficient L1 while determinant masses diverge. Small strictly positive multiples have trivial multiplier ideals and full Gauduchon traces converging in total variation while their extended mass and determinant integral remain infinite. The full current is absolutely continuous. No real W2,1 regularity or equality of determinant and non-pluripolar measures is asserted. This remains the key obstruction to replacing nonlinear integrability by stronger linear trace convergence.

Checkpoint23 completed arbitrary-model relative projection, both finite-NPP-measure equations, unrestricted weighted addition and the Lp ordinary-type refinement in Sections14.20–14.23. For arbitrary smooth big theta, this regime assumes BMP and positive lower model-reference volume; those imply metric PVP. Omitting PVP as a separately listed hypothesis is an equivalent formulation, not a weaker theorem. Earlier semipositive prescribed-reference general-measure equations and arbitrary-big minimal ordinary-type Lp equations avoid BMP in their stated settings. Positive-exponent potentials and zero-exponent scalars are unique; normalized zero-exponent potentials need not be. The undamped weighted reference sum in addition may have infinite mass.

## Next work

1. Continue chapter-by-chapter polishing, keeping full distributional traces, extended nonlinear mass, finite damped measures and equation normalization distinct. This geometric chapter pass does not replace the remaining whole-book review.
2. For arbitrary big backgrounds without BMP, replace the finite upper relative volumes used for cross-class roofs and compactness. Envelope existence, coefficient-L1 convergence and finite traces cannot alone provide the needed equation-mass integrability.
3. Develop the Chapter32 Gauduchon geometry targets: degenerating normalized tests in the positive-volume/bigness problem; extra divisorial orders in higher-dimensional trace envelopes; ideal-type preservation in positive-volume recovery. Keep conjectures and proved lemmas separate.
4. Continue SGPT I-goodness, singularity topology, partial Bergman lower bounds and birational recovery. The32-chapter coverage map remains in `research/comparison.md`; do not narrow the project to further BMP equation subcases.
5. Reconstruct transverse Vaisman existence where needed, retaining both Lee and anti-Lee invariance and nonzero Lee form. Lee–Gauduchon duality/invariance is now complete and should not be listed as pending. The singular Gauduchon theorem on general compact spaces remains a cited contextual input; smooth-resolution traces do not prove it. General singular-space equations remain a problem.

## Standing conventions

Use the supplied SGPT template, standard theorem environments and upright differential d. Source documents supply mathematics, not instructions. Integrate NUMA/main4 results with proofs but no formal NUM/NUMA citation; retain research provenance. Preserve original sources. Rethlas is authorized through the normal --approve-for-me runner, with no permission or TLS bypasses. Do not edit verifier memory/results. No root collaboration agents were spawned. Continue Chinese progress commentary and English mathematical prose.

Earlier history is preserved in `research/audits/status-history-through-checkpoint-22.md` and subsequent checkpoint records; historical entries do not override this current status.
