# Whole-book pass: duplicates, unused hypotheses, concision, simplification, placement

## The book and the request

Repository: `/home/user/non-kahler-pluripotential-theory`. The book *Singularities in Hermitian pluripotential theory* (Springer `svmono`, about 1770 printed pages) lives in `book/`; `book/book.tex` includes the chapters from `book/author/`, and chapters `\input` section files. Some files use one paragraph per source line, some are hard-wrapped: keep each file's style. Global normalizations: $\mathrm{dd}^{\mathrm c}=\frac{\mathrm i}{2\pi}\partial\bar\partial$, $\mathrm d^{\mathrm c}=\frac{\mathrm i}{4\pi}(\bar\partial-\partial)$, multiplier ideals with $e^{-u}$, Monge–Ampère masses without $1/n!$, $u\preceq v$ means $u$ is at least as singular as $v$. Notation table at the end of `author/conventions.tex`.

The book has been proofread for accuracy several times. The author now asks (13 October 2026, verbatim): “重复论证都删掉。全书没有用到的假设都删掉，核对一下。然后表述要简洁且严格。能够简化的证明和构造也去简化。位置你觉得不合适的内容你自己搬去合适的位置” — delete all duplicated arguments; delete every hypothesis that is not used, and check this; statements must be concise and rigorous; simplify the proofs and constructions that can be simplified; move content that is in the wrong place.

You are one of about 23 agents, each with a disjoint part of the book. Edit **only** your assigned files. Read your whole part in reading order (`\input` order), every statement and every proof. Correctness has absolute priority over brevity: every change must leave a correct, complete argument, and an independent audit will recheck every mathematical change you make.

## Your five tasks

### 1. Duplicated arguments
A duplicated argument is a result, lemma, computation or proof step that is established twice in the book (possibly with different notation or in a special case of another statement).
- Look for duplicates inside your part as you read. Also run `python3 /tmp/claude-0/-home-user/0c1c1f5d-1372-5a99-bc01-928e0a225f74/scratchpad/dup/mypairs.py <file> <file> ...` with your file names (without `.tex`): it lists candidate pairs found by textual similarity of statements and proofs across the whole book. Most candidates are not duplicates (a corollary next to its theorem, two different examples with similar wording); check each one that involves your files by reading both items.
- **Inside your part:** keep the argument at its natural home (usually the first occurrence in reading order, or the more general statement) and replace the other by a citation. If a whole statement is a duplicate, delete it and put its `\label` (and `\index` entries) on the surviving statement, so that every reference still resolves; adjust a sentence that cited it if the wording no longer fits. If a statement is a special case of a more general one in your part, keep it only if it is used often or motivates a method, and then give it a one-line proof from the general result.
- **Across parts:** the owner of the copy that comes **later** in reading order acts: replace its proof by a citation of the earlier result (stating briefly how the earlier statement applies, e.g. parameter values or notation translation), and shorten the statement if it is identical. Do not delete a cross-part duplicate statement yourself; list it in your report as "label X duplicates label Y" and the coordinator will remove it and redirect the references at the end. If the later copy is more general and the earlier one should be replaced by it, or if both should be replaced by a common lemma, do not edit the earlier file: report it with a proposal.
- Repeated *definitions* and *recaps* of notation from earlier chapters count as duplicates too: replace them by a short reminder in words with `\cref`.

### 2. Hypotheses that are not used
For every theorem, proposition, lemma and corollary in your part, and for every standing assumption ("Throughout this section …", "Assume …", "Fix …") of your sections, check whether each hypothesis is actually used: in a step of the proof, in a cited result whose hypotheses must be verified, or to make the statement meaningful (for example a definition that needs it). Typical candidates: dimension restrictions ($n\geq2$, $n\geq3$), compactness or connectedness, Kähler versus Hermitian, closedness, smoothness or strict positivity of a form or density, boundedness, integrability exponents, normalization conditions, "for all" where "for some" suffices.
- If a hypothesis is not used, remove it, and recheck **every** step of the proof and **every** cited result in the enlarged scope (open the targets with `grep -rn 'label{KEY}' author/`). If the statement then becomes more general, make sure the conclusion still holds in the new cases (try the extreme cases: $n=1$, a zero form, an empty pole set, a nonclosed form).
- A hypothesis needed by a cited result, by a later example, or because without it the statement is false or meaningless stays. If it stays only because a cited result needs it, that is fine; do not add commentary.
- When you remove a standing assumption of a section, check every result of the section, not only the one that prompted it.
- Hypotheses restated in files outside your part (chapter openings of other chapters, `chapter_research_program.tex`, `chapter_history.tex`, other sections) are reported to the coordinator with the exact replacement; do not edit them.

### 3. Concise and rigorous statements
Statements must say exactly what is proved, with every object and quantifier defined, in as few words as clarity allows. Remove repeated conditions, redundant qualifications, commentary inside statements (move necessary commentary after the statement), and phrases that restate the definition of a term. Keep regimes visibly distinct (bounded mass, positive lower mass, closed classes, one density versus all densities, scalar versus potential uniqueness, ordinary versus ideal type). Prose around statements should also be concise: delete recaps, ceremonial transitions and repeated motivation; keep the explanation of why the next argument is needed.

### 4. Simpler proofs and constructions
Where a proof can be shortened without loss of rigor, shorten it: cite a result of the book (or of the allowed books) instead of re-deriving it, remove unnecessary cases or steps, merge repeated estimates, use a more direct argument. Where an example or construction can be replaced by a simpler one with the same properties, simplify it, but only if you have checked every property the text claims for it and every later use of it (grep its label and its notation). Do not shorten a proof by hiding a step that a reader needs.

### 5. Placement
If a result, definition or section is clearly not in its natural home (it belongs to a different chapter's theory, or it is needed earlier than where it appears, or it interrupts an argument), do not move it across files: report it with the proposed destination and the reason. Within one of your files you may reorder material if no dependency breaks.

## Binding rules
1. Notation is defined once, at its natural first use; elsewhere a short reminder in words plus `\cref`.
2. Do not write "without boundary"; do not add "with its upper semicontinuous representative" or "not identically $-\infty$" to introductory definitions; never make nonemptiness of $\mathrm{PSH}(X,\theta)$ sound like a standing assumption. The multiplier-ideal envelope is $P_\theta[u]_{\mathcal I}$.
3. Citations: outside `chapter_history.tex`, only the books `SGPT, DemAM11, DemCADG, GZ17, OV24LCK, HuyK3, GT01` may be cited; do not add citations or bibliography entries. Results that are original to the book are never attributed to any file, preprint without authors, solver or workflow.
4. Mass invariance under bounded changes of the potential in a closed background holds under the bounded mass property (in particular on compact Kähler manifolds), not on every compact complex manifold; Stokes' theorem for bounded potentials in a closed background holds on every compact complex manifold.
5. Labels: never rename a label; remove one only by moving it onto the surviving statement as described in task 1. Never remove an `\index` entry (move it with the label). Keep theorem environment names.
6. Do not touch `chapter_history.tex`, `chapter_research_program.tex` (unless assigned), the hidden Nakamaye files (`chapter_transcendental_nakamaye.tex`, `section_nakamaye_*.tex`), `book/style/`, `references.bib`, `preamble.tex`, `book.tex`.
7. No workflow vocabulary (verified, integrated, retained, recorded, checkpoint, "the author", supplied, actual, genuine) and no hype words.

## Tools (do not run the full build)
Run from `/home/user/non-kahler-pluripotential-theory/book`, with `S=/tmp/claude-0/-home-user/0c1c1f5d-1372-5a99-bc01-928e0a225f74/scratchpad`.
- Compile check: `bash $S/tools/chapcheck.sh <YOUR_TAG> chapter_a [chapter_b ...]` (the `\include`d chapter names of your part). Final state: no errors, no overfull boxes, no undefined references (a new label is undefined only on the first run; ignore `Underfull \hbox (badness 1783)`). Other agents edit other chapters concurrently; if an error comes from a file that is not yours, mention it and ignore it.
- Math diff: `python3 $S/tools/mathdiff3.py --base BASE author/f.tex ...` with the base commit given in your assignment. Every math change must be one of your listed changes or a harmless reformatting.
- Do not commit or push.

## Report (final message, at most about 1200 words; also write it to `$S/reports6/<YOUR_TAG>.md`)
1. Files read (confirm every line).
2. **Duplicates**: removed (what, where, which label moved where); cross-part duplicates for the coordinator ("X duplicates Y", with the action you took on your copy).
3. **Hypotheses removed**: statement, hypothesis, and why the proof works without it; hypotheses examined and kept because they are needed (brief).
4. **Simplified proofs and constructions**: what and why it is still complete.
5. **Concision**: main kinds of edits (no full list).
6. **Placement** proposals (item, destination, reason).
7. Exact replacements proposed for files outside your part.
8. Compile check and mathdiff summary.
