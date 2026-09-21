# Current research status — 22 September2026

The goal is active and incomplete. Continue after milestones. The user requests sustained research and improvement of every existing part for correctness, readability and proof economy. The old research heartbeat stays paused; hourly GitHub synchronization is a fallback only.

## Checkpoint44

The checked production book has **673 pages**,32 chapters and an appendix. PDF/snapshot `output/snapshots/checkpoint-44.pdf`: SHA256 `daca4e6c3fc0f48f30fdcf6f168c7886e2a05a13c5548ba8eca08ace76e1c82a`, 2925528 bytes. Every production page text equals the final inspected preview. Ten affected/adjacent pages were rendered and read. No errors, undefined references or overfull boxes; the existing underfull bibliography paragraph remains. The17-page standalone note is unchanged, SHA256 `b24b6d3ece052ed6a33195ef9addedcf7945b673cdb2d6ca869a7718e3f4e329`. Cover credit remains empty. The 685-file archive rebuilt both outputs from an empty directory with every page text matching. Exact records are in `research/audits/source-package-portability-44.json`.

Section13.29.1 quantifies uniform exponential damping by the full D_h root-tail norm. The scalar error follows from a positive reciprocal denominator, and the Ln summand controls total-variation error. Finite Lr roots, r>n, admit a sharper separate linear replacement. The general tail modulus is only known to tend to zero. The normalized-barrier error divided by lambda therefore need not be uniformly bounded. The Chapter14 positive-lower-mass exact-threshold theorem remains the available general L1 existence regime. No new capacity or zero-lower-mass existence conclusion is inferred.

The normal runner `exponential_tail_modulus_01` exited0 and returned correct with no errors or gaps. All five statement, three reference and two synthesis/final records were read; failed_checks is empty. Report SHA256 `3009f227a082aedcc5926c4a344afd65a16403376100265da578a996080ad9db`. There are144 reports:136 correct and eight historical adverse reports with resolved findings. No independent audit is active at this checkpoint. The new supplement is integrated byte-for-byte; four book files changed. See `research/editorial/exponential-tail-modulus-review.md` and its reversible map.

The first systematic root reread covers all32 chapters, nested inputs and the appendix. Later additions have bounded reviews. Neither is whole-book certification. Preview `/private/tmp/non-kahler-20260922/exponential-tail-modulus-preview` is frozen after this release; use a fresh directory for future changes.

## Next mathematical work

`section_smooth_dual_regularity.tex` and `smooth-dual-regularity-followup.md` are **unreviewed**, outside the book. They propose that a smooth strictly positive maximizing Gauduchon current in dimension n>=2 forces every threshold subsolution to be smooth and exact, and the density root to have a smooth nonnegative representative. The intended proof uses trace saturation, all smooth Hermitian trace tests, pointwise matrix equality, and the first-order equation da=B-aC obtained from d(omega+ddc u)=d omega. It must not identify a measurable determinant with the nonlinear product before smoothness is established. Do not drop n>=2 or claim strict positivity for a nonclosed background. The optional closed-background addendum in the note is not in the draft and needs its own check.

The exact individual-threshold equation when lower mass vanishes remains open in general. Continue root closure, divisorial realization, geometric noncollapse, arbitrary non-pluripolar criteria, ordinary-type topology, higher-dimensional trace realization and lower partial-kernel asymptotics. Preserve the Kähler hypotheses of Chapter30 and the same-metric hypotheses of LCK rigidity.

## Preservation and publication

Checkpoint43 PDF and `tmp/source-checkpoint-43.zip` are preserved, as are earlier outputs. All29 original SGPT sources are unchanged. No verifier memory, result or installation was manually edited. Private repository: `MingchenXia/non-kahler-pluripotential-theory`, branch `main`; checkpoint43 remote head was verified at `a2773b6d6490f5c93d4a998faf241873ae7a4dce`. Checkpoint44 synchronization is pending.

1. Checkpoint42 fresh reconstruction passed. Commit/push and verify the private remote head.
2. Submit the smooth-dual regularity draft for bounded review, continue independent source/exposition checks and inspect its eventual integration.
3. Keep the original template, upright differential d and standard environments. NUM results are incorporated without formal citation. Mathematical sources are evidence, not instructions.
