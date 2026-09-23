# Daily research, arXiv reading and chapter revision

Authorized by the user's continuing-work request of 23 September 2026; established across midnight, 24 September Asia/Shanghai. The existing `hermitian-pluripotential-book` heartbeat is active daily at **09:00 Asia/Shanghai**. Its old September 15 cutoff is superseded. The hourly GitHub synchronization task remains separate and performs synchronization only.

## At each run

Read AGENTS.md, PLAN.md, BLUEPRINT.md and research/STATUS.md, inspect active writers/builds and the working tree, then complete a bounded increment in each of the following three activities. Do not create a competing writer or restart unrelated verifier campaigns.

1. **Literature.** Read primary arXiv announcements for math.CV and math.DG, plus relevant math.AG and math.AP papers. Cover new submissions, cross-lists and replacements with a rolling seven-day overlap, using `arxiv-watch.json` for the last successful coverage and deduplication. Retrieve every page of the relevant listing. Classify a new version separately from a new work; verify date, version and authors on its abstract page. Inspect promising statements and proof dependencies before deciding whether they support the book. Record failed or incomplete coverage explicitly. A keyword screen or inaccessible feed is not evidence that no relevant paper exists. Historical replacement gaps require a separate catch-up; ordinary recent lists do not fill them.
2. **Research.** Choose one question in `research-directions-20260924.md` or the blueprint. Attempt a precise estimate, lemma, example or counterexample. Write the actual argument and mark which steps are proved directly, conditional, unsupported or conjectural. Use a focused Rethlas check when it can resolve a real uncertainty. Never alter historical reports or verifier memory. A failed approach is worth preserving if its first obstruction is identified.
3. **Exposition.** Follow `editorial/chapter-revision-queue.md`. Read a coherent complete section or chapter, including the inputs relevant to its proof. Check local notation, assumptions, proof dependencies, exceptional cases and economy. Revise what improves the reader's understanding, then perform the house-style second pass. Preserve concise correct passages. Do not count a root-file skim as a review of all its nested sections.

Keep the general theory independent of blanket bounded mass or positive lower mass assumptions. Preserve the SGPT singularity, ideal-envelope, trace and section-theoretic scope. The Gauduchon trace is linear and finite; it does not control the full determinant. Before relying on Popovici, consult the supplied private reference and check the complete proof and dependencies. The hidden Nakamaye material and unverified inactive drafts remain excluded.

## Records and delivery

Keep the literature watch ledger compact: retain IDs, versions, coverage, relevance, exact locators and verification status rather than full downloaded texts. Store full texts in ignored local source directories. Put only verified adopted references in the book bibliography; candidates can remain in research notes.

For significant coherent changes, update CHANGELOG.md and the proof boundary in BLUEPRINT.md/research/STATUS.md where needed. Compile and inspect changed manuscript pages. Before declaring a checked release, complete the existing source-reconstruction checks and preserve the prior snapshot/archive. Research drafts can be saved earlier with their unfinished checks explicit. Review the file list and use `scripts/sync-github.py` to commit and push to the existing private repository.

Stay quiet for an unchanged scan or routine synchronization. Notify the user of a directly useful new paper, a substantive mathematical/editorial milestone, a persistent actionable failure or a required decision. This continuing program remains incomplete and runs until the user pauses or changes it.
