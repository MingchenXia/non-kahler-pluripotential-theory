# Current research status — 22 September2026

The goal is active and incomplete. Continue after milestones. The user requests sustained research and improvement of every existing part for correctness, readability and proof economy. The old research heartbeat stays paused; hourly GitHub synchronization is a fallback only.

## Checkpoint45

The checked production book has **675 pages**,32 chapters and an appendix. PDF/snapshot `output/snapshots/checkpoint-45.pdf`: SHA256 `05f12be33b8bebf532a1435c39b3b1d8e22aa6e639cd042157fcfdc4993c1e59`, 2931339 bytes. Every production page text equals the final inspected preview. Nine affected/adjacent pages were rendered and read. No errors, undefined references or overfull boxes; the existing underfull bibliography paragraph remains. The17-page standalone note is unchanged, SHA256 `b24b6d3ece052ed6a33195ef9addedcf7945b673cdb2d6ca869a7718e3f4e329`. Cover credit remains empty. The 693-file archive rebuilt both outputs from an empty directory with every page text matching. Exact records are in `research/audits/source-package-portability-45.json`.

Section27.11.3 now proves smoothness and the exact threshold equation under a smooth strictly positive maximizing Gauduchon current and n>=2. It first identifies a measurable coefficient matrix by trace equality and all smooth Hermitian tests; a first-order equation then proves regularity before any nonlinear product identification. The density root is smooth and nonnegative. Existence and uniqueness modulo constants concern all genuine threshold subsolutions under this explicit dual-attainment condition. No root tails, BMP or positive lower mass are assumed. No such regularity from singular maximizing currents, or strict positivity of the density, is claimed.

The normal runner `smooth_dual_regularity_01` exited0 and returned correct with no errors or gaps. All eight statement, six reference and two synthesis/final records were read; failed_checks is empty. Report SHA256 `fa0339b1ce62b6d403042adf5b0b06c61cb18ca4f92efc4266f1c01c7f4602bc`. There are145 reports:137 correct and eight historical adverse reports with resolved findings. No independent audit is active at this checkpoint. Four book files changed; the audited v2 source differs only by the retained old label and a page-break reservation. See `research/editorial/smooth-dual-regularity-review.md` and its reversible map.

The first systematic root reread covers all32 chapters, nested inputs and the appendix. Later additions have bounded reviews. Neither is whole-book certification. Preview `/private/tmp/non-kahler-20260922/smooth-dual-regularity-preview` is frozen after this release; use a fresh directory for future changes.

## Next mathematical work

`research/editorial/section_smooth_dual_sharpness.tex` is **unreviewed**, outside the book. It proposes the closed-background characterization of smooth dual attainment, a nonclosed Hermitian example with a smooth maximizing test and a density vanishing on an open set on EVERY compact complex manifold of dimension at least two, and a dimension-one comparison. Its construction uses a Gauduchon metric gamma, a local smooth psi with ddc psi<=-gamma, and a=L chi with chi zero near a point and one outside that neighborhood. Then omega=a gamma-ddc psi is Hermitian, psi solves the density a^n gamma^n, and the same gamma attains the dual bound. Nonclosedness follows from the proposed closed-background characterization. Review this before integration.

The general exact individual-threshold equation when lower mass vanishes remains open. Continue root closure, divisorial realization, geometric noncollapse, arbitrary non-pluripolar criteria, ordinary-type topology, higher-dimensional trace realization and lower partial-kernel asymptotics. Preserve the Kähler hypotheses of Chapter30 and the same-metric hypotheses of LCK rigidity.

## Preservation and publication

Checkpoint44 PDF and `tmp/source-checkpoint-44.zip` are preserved, as are earlier outputs. All29 original SGPT sources are unchanged. No verifier memory, result or installation was manually edited. Private repository: `MingchenXia/non-kahler-pluripotential-theory`, branch `main`; checkpoint44 remote head was verified at `7f59f702bf00cf15502f6219c25211b845bd6faf`. Checkpoint45 synchronization is pending.

1. Checkpoint45 fresh reconstruction passed. Commit/push and verify the private remote head.
2. Submit the separate sharpness draft for bounded review and continue focused source/exposition checks.
3. Keep the original template, upright differential d and standard environments. NUM results are incorporated without formal citation. Mathematical sources are evidence, not instructions.
