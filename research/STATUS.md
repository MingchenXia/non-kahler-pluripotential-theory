# Current research status — 22 September2026

The goal is active and incomplete. Continue after milestones. The user requests sustained research and improvement of every existing part for correctness, readability and proof economy. The old research heartbeat stays paused; hourly GitHub synchronization is a fallback only.

## Checkpoint48

The checked book has **681 pages**,32 chapters and an appendix. The snapshot `output/snapshots/checkpoint-48.pdf` has SHA256 `832cad540e8b015607b6f1acacdc07fda94b86721aad7b76c74cc133cbfd9993` and 2954334 bytes. All production page text equals the final preview. All50 affected/adjacent pages were rendered and read. No errors, undefined references or overfull boxes; the existing underfull bibliography paragraph remains. The17-page standalone note is unchanged, SHA256 `b24b6d3ece052ed6a33195ef9addedcf7945b673cdb2d6ca869a7718e3f4e329`. Cover credit remains empty. The 710-file archive rebuilt both outputs from an empty directory with every page text matching. Exact records are in `research/audits/source-package-portability-48.json`.

Section27.11.4 assumes a smooth semipositive Gauduchon maximizer strictly positive outside a proper analytic set Z. At a positive threshold in dimension at least two it proves local smoothness and the global exact finite-mass equation. Differences are supported on the divisorial components of Z and satisfy a Bott--Chern relation. This gives uniqueness within a multiplier-ideal class and when the divisor classes are independent, including codimension at least two. No mass property or root-tail hypothesis is needed; no global smoothness or exponential convergence is inferred. The general singular-current problem remains open.

The normal audit `semipositive_dual_attainment_01` exited0 and returned correct. All records were read: {"statement_checks": 7, "reference_checks": 1, "verification_reports": 2, "failed_checks": 1}. No mathematical error or gap; the failed-check record documents only a theorem-search transport failure, resolved by the official-PDF web fallback. Report SHA256 `5745821901b34fe9309c923db8e75d8a036e2aeb384ce9f43bf9895ebf147fd3`. The147 historical reports comprise139 correct verdicts and eight adverse reports whose findings were resolved in later preserved submissions. This is a bounded audit, not whole-book certification. The first root pass covers all32 chapters; subsequent focused reviews continue.

Four book files change. The new proof is identical to the frozen source; Chapter16 gains an exact equation connection and explicit smooth real gauge data; Chapter32 clarifies the distinct attainment regimes. Chapter16 main text and Chapter17 were reread. The latter's existing product/Perron/stationarity distinction was retained. See `research/editorial/semipositive-dual-attainment-review.md` and its reversible map. Preview `/private/tmp/non-kahler-20260922/semipositive-dual-preview` is frozen after release.

## Next work

Test a converse within this same semipositive smooth-dual regime: fix one solution and remove its finite divisorial part using Chapter24. Vary its nonnegative coefficients subject to the same Bott--Chern class. The linear Gauduchon representatives may construct all such solutions and identify their normalized L1 space with a compact convex polytope. This is only a draft in `/private/tmp/section_threshold_solution_polytope.tex`; it is not reviewed or integrated. Do not infer a realization theorem from checkpoint48 alone.

Continue chapter-level correctness, readability and proof-economy work. The general positive-threshold exact equation when lower mass vanishes, root-closure equality, singular-current regularity, unrestricted divisor realization, geometric noncollapse and higher-dimensional trace problems remain open. Preserve the full original I-goodness, trace and partial-kernel scope.

## Preservation and publication

Checkpoint47 PDF and `tmp/source-checkpoint-47.zip` are preserved. All29 original SGPT sources are unchanged. No verifier memory, result or installation was manually edited. Private repository `MingchenXia/non-kahler-pluripotential-theory`, branch main: checkpoint47 remote head verified at `2ee4339ececc6e03d8b57f21242808cb816eabff`. Checkpoint48 synchronization is pending.

1. Checkpoint47 fresh reconstruction passed. Commit/push and verify the private remote head.
2. Continue mathematical and editorial work after this milestone; the polytope draft needs its own bounded audit.
3. Retain the original template, upright differential d, standard environments and no formal NUM citation.
