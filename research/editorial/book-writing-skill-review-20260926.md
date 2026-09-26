# Book-writing skill — 26 September 2026

The author requested a dedicated skill combining `mingchen-writing` with the experience of this book's revision, maintained as subsequent author interventions improve the book. The new `mingchen-book-writing` skill is installed at `/Users/mingchen/.codex/skills/mingchen-book-writing/`; its five-file maintained source is `research/editorial/skills/mingchen-book-writing/`.

The entrypoint extends the base style rather than copying its assets. Three references cover chapter work, the evidence and scope of editorial lessons, and the specific Hermitian-book policies. The project instructions now route future book work to the skill and require scoped updates when feedback adds or changes reusable guidance. Local typos and already-covered corrections do not require new rules. The parent skill is unchanged.

## Direct review of behavior

All four Markdown documents were reread, together with the UI metadata. This was a direct scenario walkthrough, not an independent-agent test or evidence that a future model will always follow the guidance.

| Scenario checked | Application and countercase |
|---|---|
| Continue this existing book using both skills. | Preserve its monograph template and `book/references.bib`; the base skill's new-paper assets do not trigger an `amsart` or bibliography migration. |
| A section repeats the current setting and a definition. | Delete the repeated setup and point to the definition's home; preserve a later change from a Hermitian form to an arbitrary smooth background. |
| The author rejects a redundant representative or minus-infinity qualification. | Remove it at the introductory definition; retain a necessary check when restricting to a subvariety or taking a degenerate limit. |
| Remove language suggesting global PSH nonemptiness. | State a needed assumption only in the relevant result; do not pretend that an arbitrary background supplies a competitor. |
| A general psh lemma appears inside a later geometric chapter. | Relocate the lemma and proof to the first chapter, repair callers and check the dependency order; leave the specialized geometric application in place. |
| Paper citations must be in final historical notes. | Transfer exact versioned attribution and connect it to the internal result; retain allowed book citations and do not treat every `misc` record as a paper. |
| A proved selection theorem supersedes a research question. | Remove the settled scope and insert its internal reference; do not infer uniqueness of all solutions or erase the remaining integrable-density problem. |
| The author changes an earlier preference. | Update the governing rule and retire the conflicting one; do not append a second incompatible instruction or spread this book's policy to unrelated projects. |
| The requested edit only changes this skill. | Validate and reconcile the skill copies without restarting book compilation, changing chapter completion, creating an automation or widening publication authorization. |

This review prompted an explicit distinction between substantive new guidance and corrections already covered by existing rules, avoiding timestamp-only or rule-accumulation edits. The maintained and installed copies are byte-identical.

## Mechanical checks and limits

The bundled `skill-creator/scripts/quick_validate.py` passes. Its initial missing PyYAML dependency was installed only in the project's ignored temporary directory. The three relative reference links resolve; the UI description has the supported length; the default prompt names `$mingchen-book-writing`; implicit invocation keeps its enabled default. No executable helper was added to the skill.

This is a skill and workflow update, not a new mathematical release. The manuscript, build scripts and chapter queues are unchanged, and both PDFs retain their checkpoint138 hashes. The next whole-chapter target remains Chapter 33. The existing book-writing goal remains active.
