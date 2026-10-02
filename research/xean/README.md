# Sequential open-problem research with Xean

Requested by the author on 2 October 2026: use [chaoxu/xean](https://github.com/chaoxu/xean), `gpt-6.1-sol` and `xhigh`, trying the book's open problems one by one. Status: prepared, not executed. The workspace has recovered and the checked checkpoint294 source has been reconciled and synchronized. Runtime qualification is recorded in [runtime-qualification-20261002.md](runtime-qualification-20261002.md): installed and deterministic runs checked; exact Pi model/effort validated; native model authentication failed401. No Xean campaign has run.

## Execution and evidence

Use a separate Xean checkout at a recorded exact source commit, its frozen lockfile and Bun 1.4.2, following its README, AGENTS.md, philosophy and solver guide. The documentation/configuration inspected for this preparation correspond to current source `7f3eaeb7f997d14a3f6bc7b9ed80b13b145545e7`. Do not vendor Xean, its dependencies or campaign databases into the book source repository. Keep campaigns in an ignored writable directory with one owner process and one active problem campaign.

The author subsequently requested the local Codex subscription allowance. [settings.codex-subscription.json](settings.codex-subscription.json) is now the preferred configuration: every Pi role uses `openai-codex`, `gpt-6.1-sol` and `xhigh`, while native Codex source checking and independent review retain the same model and effort. [run-codex-subscription.ts](run-codex-subscription.ts) reads the native ChatGPT login and passes the access token to the child process in memory. It preserves the existing native Codex home and uses neither an OpenAI API key nor a copied credential in this repository. Run it with the separately installed Bun runtime and ordinary Xean CLI arguments; use the subscription settings when initializing a campaign. `--check-auth` checks only credential format and expiry, without calling a model. `XEAN_CHECKOUT_DIR` can identify a different separately qualified Xean checkout.

The mounted native login is reported as ChatGPT, but its access token cannot be parsed by the native subscription provider and is byte-identical to the prior credential that failed401. The launcher therefore exits before any model call. The author reports that local re-login is complete, but a fresh check finds the cloud credential mount unchanged. The current chat does not expose a usable credential export to the subprocess. Updated valid native credentials must become available to this execution environment. After that, verify the actual served model and structured role submission with a small `gpt-6.1-sol`/`xhigh` smoke run, and separately qualify native Codex retrieval. No successful subscription call or campaign acceptance is yet recorded. The public-API [settings.template.json](settings.template.json) remains an unused alternative; it is not the author's current requested path. Do not silently substitute another model or effort.

Before initializing each campaign, refresh the problem and all of its mathematical definitions and referenced theorem statements against the polished manuscript. The task payload has only `problem` and `completionCriteria`; catalogue labels, source revisions, provider settings and requester metadata belong outside that payload. Expand the internal references so the solver receives an exact understandable task. The [first task draft](tasks/01-i-good-no-bmp.draft.json) preserves the current statement; its internal references still require this expansion before initialization.

Record useful lemmas, failed approaches, counterexamples, exact hypotheses, dependencies and unresolved gaps in durable notes. A solver verdict or finished worker is not proof of completion: inspect the accepted argument and all generated supporting proofs. Only Xean's `campaign.status: completed` establishes its exact-task acceptance; independent mathematical review and closing or refining the book question remain separate checks. Preserve conditional or partial results as such. Incorporate checked results through the book's ordinary two-read, build, visual, publication and source-reconstruction workflow.

## Queue in book order

These are the 23 active formal questions at checkpoint293, sorted by their book numbers. Labels and exact statements are preserved. Refresh locations after manuscript revisions. The two topology questions overlap; successful work may be reused only after checking both exact completion criteria.

| Order | Baseline number | Label | Source | Status |
|---|---|---|---|---|
| 1 | 15.6.1 | `qu:i-good-no-bmp` | [chapter_igood.tex](../../book/author/chapter_igood.tex) | queued |
| 2 | 25.16.1 | `qu:nef-degeneration-exponent` | [section_nef_degenerations.tex](../../book/author/section_nef_degenerations.tex) | queued |
| 3 | 28.2.1 | `conj:lck-lee-psef` | [chapter_lck.tex](../../book/author/chapter_lck.tex) | queued |
| 4 | 28.4.1 | `q:lck-gauduchon-volume` | [chapter_lck.tex](../../book/author/chapter_lck.tex) | queued |
| 5 | 28.5.1 | `conj:lck-calabi-yau-vaisman` | [section_lck_volume_literature.tex](../../book/author/section_lck_volume_literature.tex) | queued |
| 6 | 29.8.1 | `qu:hermitian-i-characterization` | [chapter_mass_bound_volumes.tex](../../book/author/chapter_mass_bound_volumes.tex) | queued |
| 7 | 32.1.1 | `qu:individual-equation-threshold` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 8 | 32.2.1 | `conj:nef-gaud-volume-big` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 9 | 32.3.1 | `qu:closed-nef-gaud-bridge` | [section_non_kahler_geometry.tex](../../book/author/section_non_kahler_geometry.tex) | queued |
| 10 | 32.3.2 | `qu:geometric-gaud-endpoint` | [section_non_kahler_geometry.tex](../../book/author/section_non_kahler_geometry.tex) | queued |
| 11 | 32.3.3 | `prob:primitive-elliptic-lower-mass` | [section_primitive_elliptic_bundles.tex](../../book/author/section_primitive_elliptic_bundles.tex) | queued |
| 12 | 32.3.4 | `qu:chern-ricci-gaud-singularities` | [section_non_kahler_geometry.tex](../../book/author/section_non_kahler_geometry.tex) | queued |
| 13 | 32.3.5 | `qu:balanced-pluriclosed-program` | [section_non_kahler_geometry.tex](../../book/author/section_non_kahler_geometry.tex) | queued |
| 14 | 32.3.6 | `qu:hermitian-morse-program` | [section_non_kahler_geometry.tex](../../book/author/section_non_kahler_geometry.tex) | queued |
| 15 | 32.5.1 | `qu:gaud-metric-boundary` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 16 | 32.6.1 | `conj:continuous-gaud-adjoint` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 17 | 32.7.1 | `qu:singularity-topology-program` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 18 | 32.8.1 | `qu:exact-trace-program` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 19 | 32.8.2 | `qu:positive-system-recovery` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 20 | 32.9.1 | `qu:partial-kernel-lower-program` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 21 | 32.9.2 | `qu:fiber-selected-approximation` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 22 | 32.9.3 | `prob:growing-jets-localization` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |
| 23 | 32.10.1 | `qu:singular-space-equations-program` | [chapter_research_program.tex](../../book/author/chapter_research_program.tex) | queued |

Advance one campaign at a time. The author further instructed: “你用xean解决的每个问题都整合进书里，解决完所有问题之前你不许停下”. Stay with the current problem until its exact task is resolved, unless the author changes the order. Integrate every checked solution and complete proof into the manuscript, reconcile affected questions and claims, and complete the two-read, rebuild, publication and source-reconstruction release before advancing. Preserve unresolved gaps and durable campaign state; never mark the overall goal complete while any problem remains unresolved. Narrative questions require a separate inventory after the formal queue.
