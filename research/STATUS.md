# Current research status — 23 September 2026

The goal remains active and incomplete. Continue improving the manuscript after milestones. The old research heartbeat remains paused; hourly GitHub synchronization is a fallback only.

## Checkpoint88

The book has **688 pages**, 33 active chapters and an appendix. Snapshot `output/snapshots/checkpoint-88.pdf` has SHA256 `d18d5a996584516ec0bc858dfac6587ae9f1fe8efd8bbf64642e4ed022f5add2` and 2935143 bytes. Every production page text matches the reviewed preview. All 35 selected production page images are pixel-identical to the rendered and read preview, covering the full new section, its transitions, changed contents, research discussion and bibliography. Compilation has no errors, unresolved references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. See `research/audits/build-snapshot-88.json`.

Section 28.8 (Theorem 28.8.1) integrates the supplied `incomplete_metric.tex`: a big non-nef class on the blow-up of the projective plane has a unique finite-energy solution of a divisorial exponential equation with minimal singularities, whose metric is incomplete on every nonempty connected open subset of its ample locus. The full proof is retained and adapted to the book's dd^c normalization. Chapter 33 distinguishes this negative answer from the remaining nef and flow-compatible questions. Fourteen existing result/problem environments in the edited inputs are unchanged.

The normal Rethlas run `incomplete_divisorial_metric_01` returned correct with no critical errors or gaps under its explicitly listed standard closed-Kähler inputs. There are 173 saved reports:165 correct and eight historical adverse reports resolved later. The original supplied file, 29 SGPT source files, all 172 earlier reports, checkpoint87 and its archive, the 17-page companion note and the three hidden Nakamaye files are preserved. See `research/editorial/incomplete-metric-review.md` for exact scope. No whole-book certification is claimed.

Clean source reconstruction is recorded separately in `research/audits/source-package-portability-88.json`; that record must exist and pass before declaring the release procedure complete. The full book goal remains active and incomplete.

## Checkpoint87

The book remains **684 pages**, 33 active chapters and an appendix. Snapshot `output/snapshots/checkpoint-87.pdf` has SHA256 `73185b9a7522fcf6ac3cb367dad9e46409435e74ac3781717f02ec2e1459e1eb` and 2915779 bytes. Every production page text matches the final reviewed preview. All 66 selected pages were rerendered after the second pass: 51 changed images were read, and 15 were pixel-identical to the already read first preview. The selection covers all 21 changed page texts relative to checkpoint86. There are no errors, unresolved references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. See `research/audits/build-snapshot-87.json`.

The existing arbitrary-background weighted lower-semicontinuity lemma is now in Chapter 13, replacing its earlier semipositive-only version. Chapter 32 cites it instead of repeating its proof. The argument allows infinite total mass and makes explicit the signed-product total-variation bound and the moving quasi-continuous weight passage. The genuine monotone-limit prerequisites are preserved. All 13 other formal statements in the three edited inputs are unchanged; the bounded-subsolution input has only a spacing control.

No new Rethlas run was started. The focused primary review reread the three relevant historical reports, including the adverse common-barrier report and its subsequent successful repair. All 172 saved reports, 29 original SGPT files, checkpoint86 and its source archive, the 17-page companion note and the three inactive Nakamaye sources are preserved. See `research/editorial/weighted-continuity-review.md` for the bounded scope; no new equation-existence theorem or whole-book certification is claimed.

Clean source reconstruction is recorded separately in `research/audits/source-package-portability-87.json`; that record must exist and pass before declaring the release procedure complete. The full book goal remains active and incomplete.

## Checkpoint86

The book remains **684 pages**, 33 active chapters and an appendix. Snapshot `output/snapshots/checkpoint-86.pdf` has SHA256 `c60484232b4802349b0814bd3eec323f5292f8eeeb9f0f224bdd15d5577c60fb` and 2917264 bytes. Every production page text matches the final reviewed preview. The final visual review covers 54 selected physical pages: the last two wording changes were rendered and read, and 52 other selected pages were rerendered and found pixel-identical to previously read images. No errors, unresolved references, duplicate labels or overfull boxes occur; one inherited bibliography underfull paragraph remains. See `research/audits/build-snapshot-86.json`.

Chapter 12 now proves stretching closure, closure under nonempty finite rooftops and equality of ordinary singularity envelopes for an arbitrary smooth background and any genuine reference. The finite-rooftop proof uses one convex average. Chapter 32 replaces two proofs by citations to these general results, retaining all its hypotheses and formal statements. The countable-family warning distinguishes this closure from sequence compactness. The model-reference positivity, measure convergence and equation results retain their additional assumptions.

The normal Rethlas run `general_relative_envelopes_01` terminated successfully and returned correct with no critical errors or gaps, under its three explicitly accepted elementary analytic inputs. There are 172 saved reports:164 correct and eight historical adverse reports resolved later. The previous 171 reports and 29 original SGPT files are unchanged. Checkpoint85 and its source archive, the 17-page companion note, and the three hidden Nakamaye files are preserved. The exact scope is in `research/editorial/general-envelope-review.md`; no whole-book certification or new equation-existence theorem is claimed.

Clean source reconstruction is recorded separately in `research/audits/source-package-portability-86.json`; that record must exist and pass before declaring the release procedure complete. The full book goal and the continuing-work list below remain active.

## Checkpoint85

The reorganized book has **684 pages**, 33 active chapters and an appendix. Snapshot `output/snapshots/checkpoint-85.pdf` has SHA256 `31c1369eadcd2d885001c24e1ee58d3011314b37fe53cc2b450b8da22cb89bdb` and 2920891 bytes. Every production page text matches the reviewed final preview. All82 first-final selected pages and27 supplement pages were rendered and read; the supplement covers all14 subsequently changed page texts, and71 unchanged selected pages were rerendered and found pixel-identical. These are focused structural/layout checks, not whole-book mathematical certification. Compilation has no errors, unresolved references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. See `research/audits/build-snapshot-85.json`.

Part XII separates Chapter30, Volumes under bounded mass; Chapter31, Relative equations under positive lower mass (without BMP); and Chapter32, Big backgrounds under bounded mass and positive lower reference volume. The main sequence keeps extended measures and volumes, general envelopes, both measure representations, ordinary-type Lp equations and individual-density criteria. Characterizations and counterexamples to uniform mass properties also remain in the main sequence. Definitions, hypotheses and proofs are preserved; the envelope/volume class definition is split with identical formulas. The exact source/context review is in `research/editorial/mass-structure-review.md` and its reversible map.

The former Chapter30, A transcendental Nakamaye theorem, and its two inputs are excluded from the active book but remain unchanged in the repository. Active promises and references to those proofs have been removed. The ordinary Bott–Chern loci and LCK chapters remain, now28–29, including the previously checked strongly Gauduchon criterion. Historical audit numbers still refer to their original releases. The current reading guide and blueprint use the new structure.

The17-page companion note is unchanged from checkpoint58, SHA256 `9181102735342469b023d5fa35fadce29a310598a3ff357f4a8e855e533f13c4`. All29 original SGPT files, checkpoint84 and `tmp/source-checkpoint-84.zip` are preserved. All171 bounded verifier reports are unchanged (163 correct and eight historical adverse reports resolved later). No new verifier run was started for this structural revision. Portable reconstruction and final archive checks are recorded in `research/audits/source-package-portability-85.json`; that record must exist and pass before declaring the release procedure complete.

## Continuing work

Continue focused correctness and readability reviews under the new chapter structure, preserving the full scope of the source book. The moved statements have no stronger conclusions. The main/conditional distinction should remain visible in every future addition; a hypothesis on one datum or reference is not a uniform mass property.

Before using any result of Popovici, consult the supplied private working reference, then independently check the complete proof and dependencies. Do not integrate that reference into the book or package. The historical uses and exact proof checks are in `research/editorial/popovici-use-review.md`; the former Nakamaye use is now inactive.

The individual-density subsolution threshold, Gauduchon duality and exponential approximations remain central in Chapters13 and26. Positive threshold alone is not known here to give a general exact equation when lower mass vanishes. Keep the additional moment, envelope and smooth-dual assumptions explicit. Chapter14's functional convergence does not imply recovery of the full singularity type.

Chapter19's curve source metric compares with total variation of atomic data under positive mass. This remains distinct from the elementary ideal metric and its Chapter15 mass discontinuity. General Hermitian ordinary-type topology, higher-dimensional all-model trace realization and lower partial Bergman asymptotics remain open. Chapter33's primitive elliptic bundles and K3 test retain their checked metric and restricted-mass calculations; unrestricted lower mass in the K3 example remains unresolved. The historical current-descent suggestion is unproved and outside the book.

## Preservation and publication

Checkpoint86 was remotely verified at `9a50334b1e982ef853107aff2b8b63bcd4780053`. Review the full eligible diff and run the authorized private synchronization command after the release checks. Git history and an exact remote-head check record backup; do not infer successful publication merely from a local commit. Keep the original template, upright differential d, standard environments, standard ideal-envelope notation and no formal NUM citation. Never edit verifier records.
