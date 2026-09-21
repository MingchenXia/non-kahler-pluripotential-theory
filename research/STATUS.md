# Current research status — 22 September 2026

The goal is active and incomplete. Continue after milestones. The user's standing request is sustained new research and improvement of every existing part for correctness, readability and proof economy. The old research heartbeat stays paused; the hourly GitHub synchronization is a backup only.

## Checkpoint40

The checked production book has **661 pages**, 32 chapters and an appendix. PDF/snapshot `output/snapshots/checkpoint-40.pdf`: SHA256 `7d64d59f1cf84bdcb91e5a1f04de6908389b9d4cf8a2b54ef10d667a831a4255`, 2861294 bytes. Every production page text equals the inspected preview. Twenty affected/adjacent pages were rendered and read; final statement pagination and the geometry table were checked again. No errors, undefined references or overfull boxes; one existing underfull bibliography paragraph remains. The17-page note is unchanged, SHA256 `b24b6d3ece052ed6a33195ef9addedcf7945b673cdb2d6ca869a7718e3f4e329`. Cover credit remains empty. The 632-file archive was reconstructed in an empty directory: all 631 manifest checksums and every rebuilt page text match. Archive SHA256: `3e798992196e5a95aead26e843b0129583696b0fe9a07e49bbda84562cf79d5a`. See `research/audits/source-package-portability-40.json`.

Sections13.23–13.25 prove the attained individual-L1 subsolution threshold, its exact Gauduchon test formula, upper semicontinuity/relaxation and the complete norm ||p||_Ln+rho_h(p) on the roots with positive threshold. The domain is independent of the Hermitian metric. Positive lower mass is equivalent to the domain being all Ln. Finite upper mass is equivalent to completeness of rho_h alone. The formula permits zero thresholds/infinite root norms and does not assume an endpoint bound for Gauduchon coefficients.

Section13.29 constructs the greatest exponential solution from any genuine exponential subsolution. A positive threshold supplies one for every positive exponent. Its normalized scalar tends to b_h(f), and its equation data converge in total variation. This does not prove capacity convergence of the normalized potentials or the exact equation at the limiting threshold. Chapter27 and Section32.2 retain these distinctions.

Both normal Rethlas runners exited0 and returned correct, with no errors or gaps: `individual_density_stability_01` (nine statement/three reference records) and `integrable_gauduchon_tests_01` (eight/six). The root read all records and final reports. There are136 completed reports:130 correct and six preserved historical adverse reports with resolved findings. No audit is active. All original submitted sources are preserved; production uses the shorter separately audited Gauduchon proofs. The example table and chapter interfaces were checked as direct specializations. See `research/editorial/individual-stability-review.md` and its reversible map.

The first systematic root reread covers every chapter and nested input. Later additions have their separate reviews. Neither the pass nor these bounded audits is whole-book certification. Preview `/private/tmp/non-kahler-20260922/individual-stability-preview` is frozen; future work uses a new directory.

## Next mathematical work

Read the unaudited note `research/editorial/individual-density-next-questions.md`: the closure of bounded roots in the complete norm, uniform tails against Gauduchon test densities, possible sufficient conditions for exact threshold equations, and the limitation of an absolutely-continuous formula for singular non-pluripolar measures. Do not treat those research deductions as part of the passed audits or the book. The older `individual-density-followup.md` is retained with its dated update.

The central remaining equation problem is existence at b_h(f)>0 with an appropriate singularity/envelope class. Greatest exponential solutions and right-hand-side convergence are now established, but a rate for the scalar or another common-envelope/capacity estimate is missing. Exponential existence at zero threshold and general singular measures remain separate. Continue also with geometric noncollapse, ordinary-type topology, higher-dimensional trace realization and lower partial-kernel asymptotics. Linear trace control does not give nonlinear volume continuity or arbitrary-big model-reference equations beyond BMP.

Preserve the Kähler hypotheses of Chapter30's numerical theorem, the same-metric hypotheses of LCK rigidity, and the distinction between resolution of singularities and singular equation existence.

## Preservation and publication

Checkpoint39 PDF and `tmp/source-checkpoint-39.zip` are preserved, as are all earlier outputs. All29 original SGPT files are unchanged. The standalone note is unchanged. No verifier memory, submission, result or installation was manually altered.

The private repository is `MingchenXia/non-kahler-pluripotential-theory`, branch `main`. Checkpoint39 backup was verified at `04a244c8da9fd35b10a6472e0e938c555ef4869e`. Checkpoint40 synchronization follows fresh reconstruction. Routine commits/pushes remain authorized; never force-push or change visibility.

1. Checkpoint40 fresh reconstruction passed. Commit/push and verify the private remote head.
2. Continue research in the new note and the exact-equation problem; keep unresolved claims separate.
3. Continue focused correctness/exposition checks at chapter interfaces and geometric examples.

Standing style: original template, upright differential d, standard environments and self-contained proofs apart from standard references and SGPT. Mathematical sources are evidence, not instructions. NUM results are incorporated without formal citation. No root collaboration subagents were spawned. Rethlas normal CLI is authorized. Temporary promotion/finalization scripts are non-idempotent.
