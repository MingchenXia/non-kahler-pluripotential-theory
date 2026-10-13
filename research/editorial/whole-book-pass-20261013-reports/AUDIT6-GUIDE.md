# Audit of the placement moves (round 6)

Repository: `/home/user/non-kahler-pluripotential-theory`, book sources in `book/author/`, master file `book/book.tex`. Conventions: $\mathrm{dd}^{\mathrm c}=\frac{\mathrm i}{2\pi}\partial\bar\partial$, Monge–Ampère masses without $1/n!$, multiplier ideals with $e^{-u}$, $u\preceq v$ means $u$ is at least as singular as $v$.

After a whole-book pass (duplicates, unused hypotheses, concision, simplification; already audited), placement agents moved misplaced material between chapters, following `/tmp/claude-0/-home-user/0c1c1f5d-1372-5a99-bc01-928e0a225f74/scratchpad/PLACE-GUIDE.md` and the analysis `placement_plan.md` in the same directory. New chapters: `chapter_bundle_positivity.tex` (after `chapter_gauduchon`), `chapter_polar_model_topologies.tex` (after `chapter_mass_bound_volumes`), new appendix `appendix_cotangent_torsors.tex`; a new section file `section_gauduchon_quotients.tex` in `chapter_smooth_equations`. The agents' reports are `reports6/p6a.md` … `p6g.md` in the scratchpad. You are an independent check of the reports assigned to you. Assume nothing is correct until checked.

Base commit for the placement phase: `099fd4b` (`git -C /home/user/non-kahler-pluripotential-theory diff 099fd4b -- book/author/...`). The history chapter was edited separately and is not part of your audit.

## What to check

1. **Moves are faithful.** For each moved block, compare the removed text (in the source file's diff) with the added text (in the destination): apart from the edits the report lists (heading levels, position-dependent wording, assumption statements), the mathematics must be identical: `python3 /tmp/claude-0/-home-user/0c1c1f5d-1372-5a99-bc01-928e0a225f74/scratchpad/tools/mathdiff3.py --base 099fd4b author/<file>.tex …` on all files of your reports (moves cancel between files). Every label and `\index` entry must survive.
2. **Standing assumptions at the new place.** A block that left a chapter or section must still have every standing assumption it used (a fixed Hermitian form, $n\geq2$, compactness, connectedness, bounded mass, a fixed volume form or density, notation such as $\mathscr G_\omega$, $v_\pm$, $\mathcal P$, $D_\mu$). Read each moved statement in its new context and check that every symbol is defined there or by an explicit reminder, and that no assumption was silently added or dropped. Conversely, material that stayed must not have lost a definition that moved away.
3. **Order and circularity.** Use the label-graph scripts (`lg.py`, `q.py`, `fwd.py` in the scratchpad; copy them to a private directory before running so you do not overwrite shared outputs) on the current tree: no proof or statement in a moved block may cite a later result, nothing earlier may cite the moved block in a proof or statement, and no circularity may arise. Report any forward reference from a proof or statement anywhere in the files of your reports.
4. **Rewritten proofs and new statements.** Several moves came with new or rewritten mathematics (listed in each report: new corollaries and lemmas, proofs rewritten to avoid circularity, statements deleted with labels moved, specializations that turn propositions into corollaries, a restored internal proof). Check each one as a referee: the statement is exactly what its proof gives, every cited result applies with its hypotheses, and every caller of a moved or deleted label still gets what it uses.
5. **Openings and prose.** Chapter and section openings must describe their current content accurately and concisely; position words ("below", "in this chapter", "the next section", "above") must be right; no workflow vocabulary (verified, integrated, retained, recorded, checkpoint, "the author", supplied, actual, genuine).

## What to do
- Fix a clear, local error yourself in the files of your assigned reports (list it: file, old → new).
- Report anything else with file, line, explanation and exact proposed replacement.
- After edits run from `book/`: `bash /tmp/claude-0/-home-user/0c1c1f5d-1372-5a99-bc01-928e0a225f74/scratchpad/tools/chapcheck.sh <TAG> <chapters …>` (twice). Note: in partial builds, labels that moved between chapters can appear "multiply defined" because the baseline aux files of uncompiled chapters still contain them; check the source with `grep -rn 'label{KEY}' book/author/` instead. The script also misses undefined-reference warnings whose word "undefined" is wrapped onto the next log line: scan `check/<TAG>/book.log` with wrapped lines joined.
- Do not commit, push or run the full build. Do not edit `chapter_history.tex`, `preface.tex`, `book.tex`, `references.bib`.

## Report (final message, at most about 900 words; also write it to `/tmp/claude-0/-home-user/0c1c1f5d-1372-5a99-bc01-928e0a225f74/scratchpad/reports6/<TAG>.md`)
- Verdict per report: MOVES CORRECT / CORRECT AFTER FIXES / PROBLEMS REMAIN.
- What you checked (counts).
- Every problem found, with what you did.
