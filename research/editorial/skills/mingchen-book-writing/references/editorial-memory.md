# Editorial memory and feedback

This file records why an active rule exists and how far it applies. It is not a transcript or a catalog of forbidden phrases. The initial entries were distilled on 26 September 2026 from the author's interventions and the recorded chapter revisions. Exact manuscript locations and current progress remain in the project, not this skill.

## Direct author instructions

| Evidence | Active rule | Scope and boundary |
|---|---|---|
| “你要一章一章改写，按照前面的标准” | Finish the requested chapter, all nested inputs and its review before advancing. | Whole-chapter assignments; a later local-edit request remains local. |
| “每一章每一节的introduction都太差了” | Explain the mathematical problem, construction and reason for the next argument. | Book and section openings. Do not replace every opening with a uniform rhetorical template. |
| “Sec 2.4你又重复了之前的定义，把这种都删掉” | Give each definition a natural home and use internal references thereafter. Carry the setting through the chapter. | Supersedes the earlier demand to restate every section's setup; genuinely new objects and changed assumptions remain explicit. |
| “ddc的convention只要声明一次” | Declare global normalization once. | Keep a source-specific conversion only where a calculation needs it. |
| “without boundary完全不需要提” | Omit default boundary qualifications in ordinary manifold settings. | Do not remove a real boundary condition from a boundary-value problem. |
| The introductory “with its upper semicontinuous representative” and “and is not identically -infty” were rejected as redundant. | Remove qualifications whose content is already supplied at that point. | This does not authorize a global deletion in distributional identifications, restrictions or degenerate limits. |
| The sentence about nonemptiness “太有歧义了，仿佛你总做这个假设一样”. | State nonemptiness only in the assertion that requires it; avoid wording suggesting a standing global assumption. | Preserve any genuine existence hypothesis or proof obligation. |
| “Sec2.5的标题也很奇怪” | Name the actual mathematical subject or mechanism in a heading. | The general criterion is an editorial inference from the complaint and base style; no exact replacement title was dictated by that remark alone. |
| “general results about psh functions should all be put in the first chap” | Give general psh results and their proofs a single home in Chapter 1. | Confirmed policy of this pluripotential book; retain specialized geometric and equation arguments in their own chapters. |
| “The cited papers (other than the books) should be put in a final chap about history” | Put exact paper citations and attribution in final historical notes, linked to the body results. | Confirmed policy of this book. Books may remain in the body; metadata type alone does not determine whether a work is a book. |
| 26 September 2026: create a book skill and improve it as the author intervenes. | Maintain this skill as part of subsequent substantive feedback work. | Changes should be supported by actual feedback or a demonstrated failure, with their scope recorded. No new scheduled automation is implied. |

## Lessons derived from completed revisions

These are review methods, not additional user quotations or new mathematical premises.

- **Keep the open-problem chapter synchronized.** Checkpoint138 found a selection question already answered by the book's Chapter 14 theorem. Search later questions and introductory claims when a result is added or strengthened. Remove only the settled scope; selection need not imply uniqueness of every solution.
- **Attach analytic assertions to their exact structures.** Checkpoint138 clarified sum-norm completeness, root-norm completeness and equality of the domain with all of Ln. A statement that a space is Banach is incomplete if its norm is ambiguous. Carry the actual norm and hypotheses into comparisons.
- **Keep quantifiers visible across reorganizations.** The revisions distinguish individual density thresholds, model-reference volume assumptions and metric-wide upper/lower mass properties. Moving conditional theory into a separate part does not justify removing its conditions.
- **Match the review claim to the work.** The Chapter 32 record distinguishes complete recursive chapter reads from statement-level dependency checks and bounded external locator checks. A report must not inflate any of these into a full external proof reconstruction.
- **Recheck after pagination changes.** The same review caught a proposition whose conclusion moved to the next page after an earlier spacing repair. Inspect the final changed pages, not only the first successful build.

Evidence for these examples is in the repository's `research/editorial/chapter-thirty-two-rewrite-138.md`, with earlier chapter records for relocated foundations. The records describe the state at their own checkpoint; consult the live manuscript before repeating mathematical claims.

## How to maintain this memory

For a new intervention, capture only what changes future decisions:

> Date and evidence; explicit instruction or derived lesson; scope; rule changed; old rule superseded if any; corrected example; a neighboring case where the rule must not be applied; checks performed.

First revise the operative instruction where it already lives. Then update or consolidate the corresponding entry here. Do not append another “always” rule for a single local preference, turn an unverified source claim into a house policy, or preserve two contradictory active rules. Keep tentative interpretations labeled as such until the author's direction or actual use supports them.

Before installation, reread the changed rule with its neighboring rules and the base style. Check that it has not accidentally required repeated settings, erased hypotheses, forced an article template onto a book, or moved all mathematics into preliminaries. Run the skill validator and verify its linked files and UI metadata. Behavioral review is additional to schema validation: use the actual corrected passage and a countercase, not a test that merely searches for the preferred wording.

For this project, edit the versioned skill source at `research/editorial/skills/mingchen-book-writing/` and synchronize it with the installed skill. Compare both copies before changing them. Preserve independent edits and use the repository history to resolve divergence. Keep the existing book release and chapter progress unchanged for a skill-only revision; record the skill update separately in the project history.
