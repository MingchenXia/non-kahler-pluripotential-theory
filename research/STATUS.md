# Current research status — 22 September 2026

The goal remains active and incomplete. Continue after milestones and improve existing proofs and exposition. The old research heartbeat remains paused; hourly GitHub synchronization is only a fallback.

## Checkpoint84

The checked book has **707 pages**, 32 chapters and an appendix. Snapshot `output/snapshots/checkpoint-84.pdf` has SHA256 `0534a638fa40252cc6906e2ccf2b75465aa60f64b226a7080d73490f33ff266e` and 3091493 bytes. Every production page text matches the final preview. All27 selected pages were rendered and read; final reflowed pages were reread and remaining images checked identical. Compilation has no errors, undefined references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. The 17-page companion note is unchanged from checkpoint58, SHA256 `9181102735342469b023d5fa35fadce29a310598a3ff357f4a8e855e533f13c4`. The 916-file archive rebuilt both outputs from an empty directory, with every page text matching. Details are in `research/audits/source-package-portability-84.json`.

Section20.5.1 identifies normalized positive-mass ideal envelopes on a compact curve with positive atomic measures D of mass less than A. The envelope is ordinarily equivalent to its Green representative, with mass A-D(Y). The source metric is bounded below by 1/96 and above by 1/2 times the full total-variation norm of the difference of atomic data. A uniform positive lower mass bound gives completeness, analytic density and failure of total boundedness. The source formulas and proofs were read directly in SGPT. The full actual report curve_atomic_source_topology_01 is correct under the explicitly accepted inputs; no sharpness of constants or capacity-continuity claim is made.

There are171 preserved reports:163 correct and eight historical adverse reports resolved later. All prior source text and labels are preserved. The new curve section and adjacent curve files have no house warnings or errors; Chapter32 retains ten prior warnings. See `research/editorial/curve-atomic-review.md` and its reversible map. The Chapter16 fixed-positive-mass discontinuity for the elementary ideal metric remains distinct from the new source topology.

## Continuing work

Before using any result of Popovici, consult the relevant entries in the supplied private working reference, then independently check the complete proof and its dependencies. Do not integrate that reference into the book or package. PLAN.md preserves this rule; the two existing uses have exact checks in `research/editorial/popovici-use-review.md`. The latest curve arguments use neither result.

The primitive elliptic-bundle calculations and precise K3 example are checked in Section32.5.3. The unrestricted lower mass remains unresolved here. The historical working note's current-descent suggestion is unproved and outside the book. Continue individual-measure equations and geometric noncollapse alongside singularity, trace and Bergman topics.

The curve comparison concerns canonical ideal envelopes, not arbitrary ordinary singularity representatives. A general Hermitian metric, higher-dimensional trace realization and capacity consequences require separate arguments. Continue improving existing parts rather than treating these cases as completion of the general theory.

## Preservation and publication

Checkpoint83 book and `tmp/source-checkpoint-83.zip`, all29 original SGPT files and the companion note are preserved. Checkpoint83 was remotely verified at80e09c565be22cf1a04d9f624ec9098aaf2e8903. Checkpoint84 source reconstruction passed. The authorized commit/push follows after reviewing the complete diff; the Git history and remote-head check record publication. Preserve local history on any network failure. Retain the template, upright differential d, standard environments, standard ideal-envelope notation and no formal NUM citation.
