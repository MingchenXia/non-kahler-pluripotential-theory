# Current research status — 22 September 2026

The goal remains active and incomplete. Continue after milestones. The user requires continued research and improvement of every existing part for correctness, readability and proof economy. The old research heartbeat remains paused; hourly GitHub synchronization is only a fallback.

## Checkpoint79

The checked book has **701 pages**, 32 chapters and an appendix. Snapshot `output/snapshots/checkpoint-79.pdf` has SHA256 `9d26fb32584ed4bc9e2bbce567993b2d5e8ef7e36fb8f09bafc7f8e02c3eace7` and 3044886 bytes. Every production page text matches the final preview. All eight selected final pages were read, covering every changed aligned raw page and the added final bibliography page. Compilation has no errors, undefined references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. The 17-page companion note remains unchanged from checkpoint58, SHA256 `9181102735342469b023d5fa35fadce29a310598a3ff357f4a8e855e533f13c4`. The 888-file archive rebuilt both outputs from an empty directory, with every page text matching. Details are in `research/audits/source-package-portability-79.json`.

Chapter31 now proves the known strongly Gauduchon existence criterion in both directions. The separating current is shown to have type (1,1), to be positive and to be de Rham exact; the existing d^c primitive is checked. The criterion is also expressed in terms of pseudoeffective Bott--Chern classes with zero de Rham image. The final paragraph uses the earlier balanced lower-mass example to distinguish this condition from full cohomological injectivity and from positive lower Monge--Ampère mass. The definition and Calabi--Eckmann example statements, their labels and the entire example proof are unchanged. The affected-source house audit has zero errors and zero warnings. See `research/editorial/strong-gauduchon-review.md` and its reversible map.

The complete actual report strong_gauduchon_criterion_01 was read: correct, without critical errors or gaps under the stated classical inputs. There are now 166 preserved reports: 158 correct and eight historical adverse reports resolved later. The final application paragraph has a separate primary-agent check; no further Popovici theorem is used.

## Continuing work

The supplied private working reference must be consulted before any use of a result of Popovici, followed by an independent complete-proof check. It is not material to integrate into the book or source package. PLAN.md preserves this standing rule. The two current uses, nef-difference bigness and the strongly Gauduchon criterion, have their exact primary-source proof checks recorded in `research/editorial/popovici-use-review.md`. No other theorem in those papers is certified or adopted.

The focused continuation also reread the Chapter29 main text, the compact pseudoeffective-cone proof, the Bott--Chern b-class construction, the elliptic closed-current/potential/section descent and the balanced metric calculation. These support the stated cohomological comparison; they give no general nonlinear mass estimate. Continue the remaining individual-measure and geometric noncollapse questions alongside the original singularity, trace and Bergman topics. The earlier whole-book passes remain bounded reviews. Preserve the standard ideal-envelope notation and every explicit hypothesis when simplifying proofs.

## Preservation and publication

Checkpoint78 book and `tmp/source-checkpoint-78.zip`, all 29 original SGPT files and the companion note are preserved. Checkpoint78 was remotely verified at 040b5fb200c1e90f08651ca6bb83466a5cb32fc8. Checkpoint79 source reconstruction passed. The authorized commit/push follows after reviewing the complete diff; the Git history and remote-head check record publication. Preserve local history on any network failure. Continue after this milestone; retain the template, upright differential d, standard environments and no formal NUM citation.
