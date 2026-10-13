# p6g: parallel torsion and pluriclosed deformations moved to chap:gauduchon

## 1. Moves made

**Where the new section goes.** The section "The Gauduchon criterion for positivity" does not end in `chapter_gauduchon.tex`. It continues for 22 lines into `section_gauduchon_linear_duality.tex` (lem:zero-gauduchon-degree and the attainment paragraph), and that file is not mine. Directly after it comes a run of sections on Gauduchon currents: duality, transverse concentration, pluriharmonic currents. Putting the theorems right after lem:balanced-pluriclosed-closed would push a long digression into §1, between Gauduchon's theorem and the trace-mass section the chapter is built around. So the new section goes after the pluriharmonic-currents block and before "The adjoint measure of the linearization".

**chapter_gauduchon.tex**
- New `\section{Balanced and pluriclosed metrics}` with a new label `sec:balanced-pluriclosed-metrics`, after `\input{author/section_horizontal_pluriharmonic_currents}`.
- It has a lead-in paragraph: lem:balanced-pluriclosed-closed covers a single metric; the first subsection treats two different metrics when a parallel-torsion connection exists; the second covers deformations with constant $h_A^{1,1}$.
- Then come `\input{author/section_parallel_torsion_positivity}` and `\input{author/section_pluriclosed_deformations}`. Both `\input` lines are cut from `section_non_kahler_geometry.tex`, so the files move whole, with every label and `\index` entry.
- Opening, one sentence added before "Applied to $\omega_u$": "A manifold carrying a balanced metric, a pluriclosed metric and a connection with parallel torsion that preserves a Hermitian metric and the complex structure is Kähler, and pluriclosed metrics persist under deformations of the complex structure with constant Aeppli number $h_A^{1,1}$."

**section_parallel_torsion_positivity.tex** (lem:parallel-positive-projection, thm:parallel-torsion-kahler, two equations)
- New heading `\subsection{Parallel torsion}`.
- The first sentence referred back to the research-programme prose ("the integral constraint of a balanced trace"). It now has its own antecedent: "For a balanced metric $\beta$, Stokes' theorem shows that the closed form $\beta^{n-1}$ pairs to zero with every exact real two-form. Parallel torsion gives a setting in which this integral constraint becomes pointwise."
- "Suppose $n\geq2$," is deleted, because $n\geq2$ is the standing assumption of chap:gauduchon.
- In the proof, the pluriclosed metric $\omega$ is renamed $\eta$, giving $P=S\eta$, so that it does not clash with the chapter's fixed Hermitian form $\omega$.
- The closing remark (the pointwise trace, why a general family gives no such control) moves, adapted, to the research programme.
- Setting: $X$ compact and connected (book convention), $n\geq2$ (chapter standing assumption), $g$ and $D$ introduced in the text. The chapter's $\omega$ is not used.

**section_pluriclosed_deformations.tex** (sec:pluriclosed-deformations, lem:aeppli-smooth-projection, thm:pluriclosed-deformation-persistence, three equations)
- Still a `\subsection`, now the second subsection of the new section.
- Its setting is stated explicitly in its first paragraph: $M$ a compact smooth manifold of real dimension $2n$, $n\geq1$, with a family $J_t$. This is "a section specifies another setting" under the chapter's assumption.
- The last sentence, a prose pointer to qu:balanced-pluriclosed-program, moves to the research programme. That removes a forward reference.

**Dependency check** (copies of lg.py and q.py run on the tree after the edits; 0 undefined references, 0 duplicate labels)
- Parallel-torsion block: its only outside dependency is lem:balanced-pluriclosed-closed, from the proof. It is at chapter_gauduchon:57, earlier in reading order.
- Deformation block: no outside dependencies.
- The new lead-in cites only lem:balanced-pluriclosed-closed, which is earlier.
- Implicit inputs: def:balanced-pluriclosed is at chapter_gauduchon:14 (earlier); Aeppli cohomology is defined inside the subsection.
- Users of either block: section_non_kahler_geometry (the prose and the statement of qu:balanced-pluriclosed-program) and chapter_history 840/846. All are later. No earlier proof or statement cites the moved material, so there is no circularity.

**section_non_kahler_geometry.tex**
- The parallel-torsion `\input` is replaced by a lead-in to the problem: "For a connection with parallel torsion that preserves a Hermitian metric and the complex structure, the proof of \cref{thm:parallel-torsion-kahler} obtains such a bound. Averaging over the holonomy replaces the two metrics by parallel forms, and along parallel directions of variation the trace constraint holds pointwise; the positive slice of fixed trace is then compact, and the volume vanishes on its boundary. For a general family, the conserved balanced trace gives no such control."
- The deformation `\input` is replaced by: "\Cref{thm:pluriclosed-deformation-persistence} provides pluriclosed metrics along a deformation of the complex structure with constant Aeppli number $h_A^{1,1}$, while the balanced metric required in \cref{qu:balanced-pluriclosed-program} remains a separate geometric condition."
- The problem qu:balanced-pluriclosed-program is unchanged; its citation of thm:parallel-torsion-kahler now points backward.

## 2. Moves not made
None.

## 3. Coordination edits
None were assigned.

## 4. Replacements needed in files I do not own

**chapter_history.tex**
- (a) Move the paragraph "The case of parallel torsion, \cref{thm:parallel-torsion-kahler}, is a theorem of Chen and Zheng … is a separate ingredient." (now l.840, in sec:history-geometry) into sec:history-gauduchon. Put it right after the paragraph "The descent of horizontal currents in \cref{lem:horizontal-pluriharmonic-descent} … Bott--Chern cone." (now about l.119) and before the Chou–Wu RC paragraph. That matches the chapter order (pluriharmonic currents, then balanced and pluriclosed metrics). Replace its first sentence by: "The Kähler criterion under parallel torsion, \cref{thm:parallel-torsion-kahler}, is a theorem of Chen and Zheng \cite[v1, Theorem~1.2, pp.~2 and~8]{CZParallel26}; it settles a case of the conjecture of Fino and Vezzoni recalled in \cref{sec:history-geometry}." The rest of the paragraph stays as it is.
- (b) Move the paragraph "The persistence of pluriclosed metrics under deformations, \cref{thm:pluriclosed-deformation-persistence}, … transverse cohomology." (now l.846) to directly after (a), without changing its wording.
- (c) Delete `\enlargethispage{4\baselineskip}` (now l.844). It was a page fix for the old position of (b).
- (d) The Fino–Vezzoni/Chiose paragraph (l.838) and the Conjecture 1.2 paragraph (l.842) stay in sec:history-geometry, and their pointers to sec:non-kahler-geometric-problems remain correct. Optional: append to l.838 "Its case of parallel torsion is discussed in \cref{sec:history-gauduchon}."

**chapter_research_program.tex, book.tex, preface.tex:** no edit needed. The preface does not describe these results; the research-programme chapter's opening and section texts do not mention them.

## 5. Compile check and math diff
- `chapcheck.sh p6g chapter_gauduchon chapter_research_program`, run twice from a fresh private copy: no errors and no overfull boxes. Only the ignorable underfull box (badness 1783) appears. All new labels resolve.
- The remaining warnings are not from my files. They come from other agents' moves into chapters outside this `\includeonly`, whose baseline aux files predate those moves. The targets all exist in the current tree:
  - undefined: chap:gauduchon-bundle-positivity, eq:gaud-collapse-basic, sec:primitive-elliptic-bundles, prop:primitive-elliptic-metric, ex:primitive-elliptic-k3;
  - multiply defined: qu:i-good-no-bmp (in the stale igood aux and in the research programme).
- Math diff: the WIP snapshot commit c5daea5 already contains part of my edits, so the base is bf394d3 (`mathdiff3.py --base bf394d3`).
  - chapter_gauduchon: +2× $h_A^{1,1}$ (prose), + label sec:balanced-pluriclosed-metrics, + reference lem:balanced-pluriclosed-closed.
  - parallel_torsion: −$n\geq2$ (standing assumption); $\omega\to\eta$ and $P=S\omega\to P=S\eta$; +$\beta$ and $\beta^{n-1}$ (new lead-in sentence).
  - pluriclosed_deformations: − reference qu:balanced-pluriclosed-program.
  - non_kahler_geometry: + $h_A^{1,1}$, + references thm:pluriclosed-deformation-persistence and qu:balanced-pluriclosed-program.
  - No other math changed. Because the files moved through their `\input` lines, the moved blocks do not show up as removed and re-added.
