# Current research status — 22 September 2026

The goal remains active and incomplete. Continue after milestones. The user requires continued research and improvement of every existing part for correctness, readability and proof economy. The old research heartbeat remains paused; hourly GitHub synchronization is only a fallback.

## Checkpoint76

The checked book has **701 pages**, 32 chapters and an appendix. Snapshot `output/snapshots/checkpoint-76.pdf` has SHA256 `e4666da27e8fbfdd33e7611eb1694c84c979d51d0f79d7f6ca7ed901e4461632` and 3040903 bytes. Every production page text matches the preview, and all 12 selected pages were rendered and read. Compilation has no errors, undefined references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. The 17-page companion note remains unchanged from checkpoint58, SHA256 `9181102735342469b023d5fa35fadce29a310598a3ff357f4a8e855e533f13c4`. The 874-file archive rebuilt both outputs from an empty directory, with every page text matching. Details are in `research/audits/source-package-portability-76.json`.

The Chapter30 nef-difference theorem now gives Popovici's known coefficient k. Cauchy--Schwarz replaces the level-set estimate in its proof; the domination constant choice changes from 8k to 2k. The other 14 formal statements in the two edited files remain unchanged. The numerical constants are fixed before the arbitrary Gauduchon test, by closedness. This remains a compact Kähler argument and is not an unrestricted Hermitian bigness criterion.

The normal Rethlas run `nef_schwarz_01` returned correct; its full actual report was read. All 164 reports are preserved: 156 correct and eight historical adverse reports resolved later. No original input, verifier memory or report was manually edited. All labels are preserved. The raw house audit has the same 48 errors and 122 warnings as the baseline: the errors concern the inherited nk: label namespace, not missing statements or compilation failures. See `research/editorial/nef-schwarz-review.md` and its reversible map.

## Continuing work

The latest user direction is to replace the multiplier-ideal envelope shorthand Q_theta[u] by P_theta[u]_{I} throughout the book. The occurrence inventory is prepared outside production; perform this notation revision next, preserving unrelated matrix and convex-envelope Q notation.

The focused Chapter30 reread covers the domination, relative principalization, exceptional-metric, gluing, trace-approximation and rooftop arguments. The earlier whole-book first and second focused passes remain bounded reviews, not a certification of every dependency. Continue individual-measure equations, geometric noncollapse and the original-book topics. Selected integrability gives a maximizing current but no regularity or exact equation. Do not infer nonlinear volume continuity from linear trace control or identify the two Gauduchon optimization families.

A further reread has begun in Chapter31 and its nested Lee--Gauduchon sections. Consider replacing the use of weak factorization in degree-one invariance by a direct modification argument and a common resolution; this is an unintegrated editorial direction, with no new result or completed check claimed here. The LCK rigidity proof remains to be reread in this pass.

## Preservation and publication

Checkpoint75 book and `tmp/source-checkpoint-75.zip`, all 29 original SGPT files and the companion note are preserved. Checkpoint76 source reconstruction passed. Two synchronization attempts failed at the GitHub privacy query (EOF, then TLS handshake timeout), before staging. The checked changes are committed locally; retry the normal synchronization command when connectivity recovers. Checkpoint76 is not yet verified remotely. Continue after this milestone; retain the template, upright differential d, standard environments and no formal NUM citation.
