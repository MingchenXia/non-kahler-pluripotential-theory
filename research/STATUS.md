# Current research status — 23 September 2026

The goal remains active and incomplete. Continue improving the manuscript after milestones. The old research heartbeat remains paused; hourly GitHub synchronization is a fallback only.

## Current revision under review

A whole-book notation-scope review is in progress at the user's request. Every active section and subsection must declare or precisely recall its objects and hypotheses before using them, including proof-local notation. The first reported instance is Definition 1.1.1. The mingchen-writing skill has been updated with the rule and the manual coverage audit. The first complete-text notation pass covers all 33 active chapters, their nested inputs, the appendix and front matter (188 files). The full draft compiles to 762 pages; its house-audit diagnostics exactly match the same baseline93 scope. The second pass, final visual inspection and source reconstruction remain pending. Progress is recorded in `editorial/notation-before-use-review.md` and its file map. Checkpoint93 remains the latest checked release until these checks finish.

## Checkpoint93

The book has **716 pages**, 33 active chapters and an appendix. Snapshot `output/snapshots/checkpoint-93.pdf` has SHA256 `7c56f0b9a0a9ee549307f0b5edbc8ee9a1b38f31e2c6aa27f6edf3c5516d95f7` and 3066250 bytes. All 42 selected final pages were rendered and inspected: 27 match previously read images pixel for pixel, and the other 15 were reread. Compilation has no errors, unresolved references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. See `research/audits/build-snapshot-93.json`.

Theorem 28.3.2 integrates the supplied smoothness result for every big closed class on a compact Kähler manifold and a smooth strictly positive global volume form. No nefness is imposed. Section 13.21 explicitly reconstructs Dang26 Theorem 3.1, including its scalar/local-equation formulation, through the internal stability and regularization proofs. Section 13.22 supplies the complete local derivative argument. Classical BEGZ existence and minimal-singularity results remain explicit standard inputs. Local smoothness of the density alone is not substituted for global Lp or the interior theorem's Holder premise.

The normal Rethlas run `ample_locus_dang_integration_01` reviewed the full assembled chain and returned correct under its listed classical/internal inputs, with no critical errors or gaps. The complete report and primary second-pass scope are recorded in `editorial/ample-locus-integration-review.md`. There are 180 reports: 171 correct and nine adverse. All 38 previous formal blocks in the edited inputs are unchanged; one theorem is added. All needed bibliography entries already existed; the bibliography is unchanged.

All 179 historical reports, 29 SGPT originals, six supplied original files, checkpoint92 and its archive, the 17-page companion and the three inactive Nakamaye files are preserved. The nef incomplete-metric draft remains unverified and inactive. The five-input house audit has 0 errors and 15 inherited warnings. No whole-book certification or novelty claim is made.

Clean source reconstruction is recorded separately in `research/audits/source-package-portability-93.json`; it must pass before declaring the release procedure complete. The full book goal remains active and incomplete.

## Checkpoint92

The book has **714 pages**, 33 active chapters and an appendix. Snapshot `output/snapshots/checkpoint-92.pdf` has SHA256 `b430f35e621e9b8e88bec603d8245aa31f881cdb3a191deed6e2980b7f401f46` and 3057650 bytes. All 71 selected pages were rendered and read; the final page-break polish changes only pages 530–531, which were reread, and the other 69 images are pixel-identical to the reviewed preview. Compilation has no errors, unresolved references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. See `research/audits/build-snapshot-92.json`.

Section 4.4 proves compact linear duality, a polar characterization and uniform stability for the Gauduchon positivity threshold. A zero-degree lemma gives the precise smooth-attainment condition and shortens a later proof. Chapters 26 and 28 distinguish smooth-test closure from the entire current family, with the exceptional-curve strict comparison. Neither mass property is imposed; nonlinear determinant duality retains its own domain and proof. Dimension-one reuse is explicit.

The normal Rethlas run `gauduchon_linear_test_closure_01` is correct under its accepted inputs; the full report and primary second-pass scope are recorded in `editorial/gauduchon-linear-duality-review.md`. There are 179 reports: 170 correct and nine adverse. All 27 earlier formal blocks in the edited inputs are unchanged; three are added. GL22 and Collins21 now cite verified journal editions with unchanged theorem locators.

All 178 earlier reports, 29 SGPT originals, four supplied original files, checkpoint91 and its archive, the 17-page companion and the three inactive Nakamaye files are preserved. The nef incomplete-metric draft remains unverified and inactive. The six-input house audit has 0 errors and 4 inherited warnings. No whole-book certification or novelty claim is made.

Clean source reconstruction is recorded separately in `research/audits/source-package-portability-92.json`; it must pass before declaring the release procedure complete. The full book goal remains active and incomplete.

## Checkpoint91

The book has **712 pages**, 33 active chapters and an appendix. Snapshot `output/snapshots/checkpoint-91.pdf` has SHA256 `8fc7c65be0ddd2fef0cf405e942c98f5a75c2e69ee84ef17cb55c935739a4228` and 3048360 bytes. All 46 selected pages were rendered and read. The final affine-operator definition changes physical pages 268–269, which were reread; the other 44 selected images are pixel-identical to the reviewed preceding production. The build has no errors, unresolved references, duplicate labels or overfull boxes, with one inherited bibliography underfull paragraph. See `research/audits/build-snapshot-91.json`.

Sections 13.19–13.21 now place fixed-reference compactness before existence, shorten the zero-exponent existence proof, and give normalized exponential compactness with whole-family scalar and strong Lp density convergence. Potential convergence remains subsequential unless the stated invariant-class uniqueness holds. Section 13.22 incorporates the updated Archive proof details while retaining the explicit local Holder premise and the internally proved global Lp corollary. Local-density-only, nonminimal and pole-set regularity remain outside the asserted conclusions. Neither metric mass property is imposed.

Both new focused Rethlas reports are correct under their accepted inputs. There are 178 reports:169 correct and nine adverse. The original adverse interior-regularity report is unchanged. The exact scopes and primary second-pass checks are in `editorial/big-exponential-compactness-review.md` and `editorial/nonclosed-archive-integration-review.md`. All 47 earlier formal blocks in the affected inputs are preserved, including the interior section's fifteen result statements and one remark; three blocks are added. No whole-book certification or novelty claim is made.

All 176 earlier reports, 29 original SGPT files, four supplied original source/bibliography files, checkpoint90 and its archive, the 17-page companion, and the three inactive Nakamaye files are preserved. The separate nef incomplete-metric draft remains unverified and inactive. The seven-input house audit reports 0 errors and 16 inherited warnings.

Clean source reconstruction is recorded separately in `research/audits/source-package-portability-91.json`; that record must exist and pass before declaring the release procedure complete. The full book goal remains active and incomplete.

## Checkpoint90

The book has **710 pages**, 33 active chapters and an appendix. Snapshot `output/snapshots/checkpoint-90.pdf` has SHA256 `b5613523672dfddefa9f6281c52179aa41c07fd9cfcccc2d8fa47ff82a2cb34c` and 3038625 bytes. Every production page text matches the reviewed final preview. All 33 selected pages were rendered and read; after the last wording polish, the two changed pages were read again and the other 31 images were pixel-identical. Every selected production image matches that final preview. Compilation has no errors, unresolved references, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. See `research/audits/build-snapshot-90.json`.

Sections 13.20–13.21 prove one-sided stability above a strict barrier, compactness for a fixed reference interval under uniform Lp density bounds, and local Holder continuity for minimal-singularity solutions in an arbitrary smooth big background. The linear curvature error for the smooth nonclosed lower form is reconstructed from Demailly’s classical expansion. Section 13.22 now proves its global Lp interior-smoothness corollary using this internal theorem, while retaining the broader local theorem’s explicit Holder premise. Neither metric mass property is imposed. Local-density-only, nonminimal and pole-set regularity remain outside the asserted result.

Both normal Rethlas runs, `big_reference_stability_holder_01` and `big_reference_compactness_01`, returned correct with no critical errors or gaps under their stated accepted inputs. The core report verifies the stability theorem assumed by the separate compactness audit. There are 176 reports: 167 correct and nine adverse. The original interior-regularity adverse report remains unchanged; the global Lp reconstruction does not validate the broader source statement. The exact two-audit and second-pass scopes are in `research/editorial/big-reference-stability-holder-review.md`.

All 174 earlier reports, 29 original SGPT files, both supplied original TeX files, checkpoint89 and its archive, the 17-page companion and the three inactive Nakamaye sources are preserved. The separate nef incomplete-metric draft remains unverified and inactive. The house audit of the five affected inputs reports 0 errors and 15 inherited warnings. No whole-book certification or novelty claim is made.

Clean source reconstruction is recorded separately in `research/audits/source-package-portability-90.json`; that record must exist and pass before declaring the release procedure complete. The full book goal remains active and incomplete.

## Checkpoint89

The book has **704 pages**, 33 active chapters and an appendix. Snapshot `output/snapshots/checkpoint-89.pdf` has SHA256 `3129e87155064e59fea7e218aa84b51b231118a0a23933af7cf5ec3ef191defd` and 3011303 bytes. Every production page text matches the reviewed preview. All 37 selected page images, covering the complete added section, transitions, chapter introduction, contents, research discussion and bibliography, were rendered and read; production images are pixel-identical. Compilation has no errors, unresolved references, duplicate labels or overfull boxes. One inherited bibliography underfull paragraph remains. See `research/audits/build-snapshot-89.json`.

Section 13.20 integrates the supplied nonclosed regularity proof after correcting its premise. Theorem 13.20.1 proves interior smoothness for locally Holder minimal-singularity solutions where a chosen strict analytic-singularity barrier is smooth and the density is smooth positive. Corollary 13.20.1 supplies the global Lp case using the explicitly identified Dang26 Holder input, whose proof is not reconstructed here. Neither mass property, closedness, semipositivity nor nefness is assumed. Chapter 33 retains the precise unresolved regimes.

The normal Rethlas report `nonclosed_interior_regularity_01` is **wrong for the original statement**, which lacked the global integrability needed to invoke Dang. Its requested continuation accepts the complete remaining proof with explicit local Holder continuity and finds no further gaps. This adverse report is not relabelled. There are 174 reports:165 correct and nine adverse (eight historical, plus this original-statement defect handled by narrowing the integrated theorem). The full primary review and proof expansions are recorded in `research/editorial/nonclosed-interior-regularity-review.md`.

All 173 earlier reports, 29 original SGPT files, both supplied original TeX files, checkpoint88 and its archive, the unchanged 17-page companion note and the three hidden Nakamaye sources are preserved. A separate nef incomplete-metric calculation remains an explicitly unverified, unintegrated research draft. No whole-book certification or novelty claim is made.

Clean source reconstruction is recorded separately in `research/audits/source-package-portability-89.json`; that record must exist and pass before declaring the release procedure complete. The full book goal remains active and incomplete.

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

Checkpoint90 was remotely verified at `0f3dfa696032aa543352acb019836de7547e4da5`. Review the full eligible diff and run the authorized private synchronization command after the release checks. Git history and an exact remote-head check record backup; do not infer successful publication merely from a local commit. Keep the original template, upright differential d, standard environments, standard ideal-envelope notation and no formal NUM citation. Never edit verifier records.
