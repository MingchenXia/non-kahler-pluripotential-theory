# Current research status — 22 September 2026

The goal remains active and incomplete. Continue after milestones. The user requires continued research and improvement of every existing part for correctness, readability and proof economy. The old research heartbeat remains paused; hourly GitHub synchronization is only a fallback.

## Checkpoint81

The checked book has **701 pages**, 32 chapters and an appendix. Snapshot `output/snapshots/checkpoint-81.pdf` has SHA256 `c5eaa4e7cc1ee21b5de3600af4d0a1a47e772434ec6c5c9d485e1e7f4fe92b1a` and 3055420 bytes. Every production page text matches the final preview. All 18 selected pages were rendered and read, covering all 16 changed aligned raw pages. Compilation has no errors, undefined references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. The 17-page companion note remains unchanged from checkpoint58, SHA256 `9181102735342469b023d5fa35fadce29a310598a3ff357f4a8e855e533f13c4`. The 899-file archive rebuilt both outputs from an empty directory, with every page text matching. Details are in `research/audits/source-package-portability-81.json`.

Chapter27 now proves the exact restricted mass infimum 8 on the elliptic lower-mass example for smooth strictly admissible potentials f(t)+pi^*v. Positivity and the two base rulings force the same amplitude bound even with arbitrary smooth v. A one-dimensional endpoint inequality proves the strict lower bound; periodic convolution gives a sharp smooth sequence. The unrestricted lower mass remains zero. All previous source text, both original propositions and their labels are preserved. The shortened exposition keeps the main inequality with its explanation. The affected-source house audit has zero errors and zero warnings. See `research/editorial/elliptic-radial-review.md` and its reversible map.

The complete actual report elliptic_radial_mass_01 was read: correct, without critical errors or gaps under its stated inputs. There are now 168 preserved reports: 160 correct and eight historical adverse reports resolved later. This report does not cover the broader primitive-bundle calculations.

## Continuing work

Before any use of a result of Popovici, consult the relevant entries in the supplied private working reference and independently check the whole proof and its dependencies. Do not integrate that reference into the book or package. PLAN.md preserves the rule. The two present uses, nef-difference bigness and the strongly Gauduchon criterion, have exact checks in `research/editorial/popovici-use-review.md`. The latest radial calculation uses neither result.

`research/editorial/primitive-elliptic-bundles-working.md` remains unintegrated. It now contains a proposed general lower bound for separated potentials, a sharper purely radial formula, and the primary-source relation with the one-flat-circle specialization of Goldstein--Prokushkin's torus-bundle construction. The general proof and normalizations require their own bounded check. A canonical-bundle calculation and a conditional K3 base without curves suggest a further geometric test; the precise K3 existence reference remains to be checked. No general lower-mass vanishing or globally open status is claimed. Do not use the pending formulas as manuscript premises.

Continue individual-measure equations and geometric noncollapse alongside the original singularity, trace and Bergman topics. The adjacent late-Chapter27 sections were reread with unchanged hypotheses. All earlier whole-book passes remain bounded reviews. Preserve the standard ideal-envelope notation and explicit assumptions when simplifying proofs.

## Preservation and publication

Checkpoint80 book and `tmp/source-checkpoint-80.zip`, all 29 original SGPT files and the companion note are preserved. Checkpoint80 was remotely verified at b5f7c9e618c053a18c2838152f631e719d4eab26. Checkpoint81 source reconstruction passed. The authorized commit/push follows after reviewing the complete diff; the Git history and remote-head check record publication. Preserve local history on any network failure. Continue after this milestone; retain the template, upright differential d, standard environments and no formal NUM citation.
