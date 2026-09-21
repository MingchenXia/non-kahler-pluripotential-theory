# Current research status — 22 September2026

The goal is active and incomplete. Continue after milestones. The user requests sustained research and improvement of every existing part for correctness, readability and proof economy. The old research heartbeat stays paused; hourly GitHub synchronization is a fallback only.

## Checkpoint49

The checked book has **681 pages**,32 chapters and an appendix. Snapshot `output/snapshots/checkpoint-49.pdf` has SHA256 `2ec5bda18570320d88a738a20e7ed3f89d3d637c29f4e78d00320ba27f59af7f` and 2952448 bytes. All production page text equals the final preview. All21 affected/adjacent pages were rendered and read. No errors, undefined references or overfull boxes; the existing underfull bibliography paragraph remains. The17-page standalone note is unchanged, SHA256 `b24b6d3ece052ed6a33195ef9addedcf7945b673cdb2d6ca869a7718e3f4e329`. Cover credit remains empty. The 718-file archive rebuilt both outputs from an empty directory with every page text matching. Exact records are in `research/audits/source-package-portability-49.json`.

Section27.11.4 now gives uniqueness modulo constants for ALL threshold subsolutions under the same smooth semipositive maximizing-form hypothesis. The maximum is a threshold subsolution by extended ordered contact. Its difference with either input has nonpositive divisorial coefficients; Gauduchon Stokes forces them all to vanish. This shortens the proof and removes the ideal-class and divisor-independence conditions. Local smoothness off the proper analytic set and the exact global finite-mass equation remain unchanged. No global smoothness or exponential convergence is inferred.

The normal audit `semipositive_dual_uniqueness_01` exited0 and returned correct. All5 statement,1 reference,1 failed-check and2 synthesis/final records were read. No mathematical error or gap. The failed-check record concerns an arXiv no-match for textbook corollaries, resolved by official-PDF web verification. Report SHA256 `f28ad7827c0290fc9613ebeb6cd3dc2af7f370c79a22ea5d0280814fe9c5cbad`. The148 historical reports comprise140 correct verdicts and eight adverse reports whose findings were resolved in later preserved submissions. This is a bounded audit, not whole-book certification.

Three book files change. The theorem is identical to frozen v2; Chapter16's now unnecessary ideal-class bridge is removed and Chapter32 states the stronger conclusion. The exploratory polytope draft is preserved outside the book and is superseded by uniqueness. See `research/editorial/semipositive-dual-uniqueness-review.md` and its reversible map. Preview `/private/tmp/non-kahler-20260922/semipositive-uniqueness-preview` is frozen after release.

## Next work

A draft in `/private/tmp/section_semipositive_exponential_limit.tex` proposes whole-family normalized L1 convergence under the same semipositive smooth-dual hypothesis. The probability b^(1/n)p k_T dV has an Ln density, so normalized moments and Jensen give b<=c_lambda<=b exp(C lambda) and a fixed lower barrier. Passing the linear trace inequalities to any L1 cluster should give the same local conformal current, hence exactness and identification by uniqueness. This draft is not audited or integrated. It does not claim capacity or uniform convergence across the analytic set.

Continue correctness, readability and proof-economy work in every part. The general positive-threshold exact equation when lower mass vanishes, root-closure equality, singular-current regularity, unrestricted divisor realization, geometric noncollapse and higher-dimensional trace problems remain open. Preserve the full original I-goodness, trace and partial-kernel scope.

## Preservation and publication

Checkpoint48 PDF and `tmp/source-checkpoint-48.zip` are preserved. All29 original SGPT sources are unchanged. No verifier memory, result or installation was manually edited. Private repository `MingchenXia/non-kahler-pluripotential-theory`, main: checkpoint48 remote head verified at `2f97d8efd957c0ef4923b57e88b4778b1caadd9f`. Checkpoint49 synchronization is pending.

1. Checkpoint49 fresh reconstruction passed. Commit/push and verify the private remote head.
2. Continue mathematical and editorial work after this milestone; the exponential-limit draft needs its own bounded audit.
3. Retain the original template, upright differential d, standard environments and no formal NUM citation.
