# Whole-book pass — 13 October 2026 (review branch)

Request (13 October 2026): “重复论证都删掉。全书没有用到的假设都删掉，核对一下。然后表述要简洁且严格。能够简化的证明和构造也去简化。位置你觉得不合适的内容你自己搬去合适的位置” — delete duplicated arguments; delete every unused hypothesis, and check this; concise and rigorous statements; simplify proofs and constructions; move misplaced content to its proper place.

Work branch: `claude/friendly-fermi-jzw1o1`. The author's `main` is not modified. Base of the pass: `1fece9c` (framework sections: `cae12da`).

## 1. Method

- **Parts.** The book was divided into 23 parts with disjoint files (guide `REVIEW5-GUIDE.md`). Each agent read every line of its part. A similarity index of all 1498 numbered statements and their proofs gave each part a list of candidate duplicate pairs. Within a part a duplicate was removed by keeping the natural home and moving the label and index entries onto it. Across parts the later copy was replaced by a citation.
- **Audits.** Fifteen independent audits (`AUDIT5-GUIDE.md`) rechecked every removed hypothesis in its enlarged scope (including the extreme cases), every citation replacing a proof (hypotheses, circularity), every moved label and every caller.
- **Placement.** A label-graph analysis of the whole book (reading order through `\include` and nested `\input`; 2928 labels, 7780 references with their contexts) checked 24 proposed moves for dependencies and forward references (`placement_plan.md`). Seven agents then carried out the admissible moves (`PLACE-GUIDE.md`), and three independent audits checked them (`AUDIT6-GUIDE.md`).
- **Historical notes.** These were synchronized twice: once with the pass, and once with the moves, which also restored the order of the chapters.

The reports, guides and coordination log are in `whole-book-pass-20261013-reports/`.

## 2. Results

Book sources changed: 358 files, about 6,200 lines removed and 3,800 added. No theorem was found false.

### Duplicated arguments removed (examples)
- Statements that were special cases of others were deleted, and their labels and index entries moved onto the general statement:
  - the classical scalar uniqueness (onto `prop:vanishing-exponent`);
  - the Gauduchon-surface uniqueness;
  - two Hessian convergence results (onto `hessian:joint-decreasing-products`);
  - the lower-barrier criterion (onto `thm:common-barrier-criterion`);
  - the maximum-rank comparison (onto `lem:nef-logarithmic-rank-comparison`);
  - the crossing and semipositive fiber bands (onto one theorem for divisors with simple normal crossings);
  - the zero-background cluster sets;
  - the four-point conic degeneration;
  - the Kähler diffuse-model statements;
  - three curve-product corollaries;
  - two concave-envelope lemmas;
  - the descended Hopf Monge–Ampère theorem (onto `lem:hopf-basic-potentials`).
- Repeated arguments are now proved once and cited. New shared lemmas:
  - `lem:hopf-basic-potentials`, from the recommendation phase;
  - `lem:split-product-normalization`, in its general form;
  - `lem:bounded-exponential-supersolution`;
  - `lem:diffuse-cutoff-polar-blindness`;
  - `lem:auxiliary-slice-envelopes`, which replaces eight copies;
  - `prop:descended-kernel-limit`;
  - `lem:small-pole-full-measures`;
  - `cor:gaud-determinant-background-comparison`.
- Re-derivations of results proved elsewhere are replaced by citations:
  - Skoda's theorem (DemAM11);
  - the weighted decreasing limit (GZ17, Theorem 3.18);
  - the dual formula and first variation of the variational volume;
  - the Gauduchon uniqueness;
  - the strong maximum principle (GT01, Theorem 3.5);
  - the bounded mass property for finite measures.
- Recaps of notation from earlier chapters are now short reminders.

### Unused hypotheses removed (examples)
- **Dimension:**
  - $n\geq2$ in the mass-invariance characterization and the raw primitive;
  - $n\geq3$ in the local adjoint bounds and the Hopf Perron sections;
  - $k\geq2$ in the radial sections;
  - $m\geq2$ in the warped results;
  - $q\geq2$ in the anisotropic jets.
- **Closedness or Kähler hypotheses:**
  - the smooth boundary-trace regularity now holds in any smooth background, by a local comparison principle valid for every smooth form;
  - the birational partial envelopes and the normalization dual entropy no longer need them.
- **Positivity, boundedness, regularity:**
  - strict positivity becomes semipositivity with positive top integral in the fiber bands;
  - local boundedness replaces boundedness in the prescribed-excess theorems;
  - zero one-dimensional Hausdorff measure replaces Hausdorff dimension zero for the small pole products;
  - other cases include $C^{1,1}$ for $C^2$, $L^\infty$ for $C^0$, and a real exponent for an integer one.
- **Standing assumptions** that no result of the section used were deleted, for example $v_-(h_0)=0$ and $\mathrm{d}V(X)=1$.
- **Conclusions instead of hypotheses.** Some hypotheses turned out to be conclusions. Examples: $b>0$ in the smooth and semipositive dual exact equations, and the Kähler class of the pullback in `prop:finite-map-zero`.

### Placement
- **New chapter "Gauduchon degrees and positivity of vector bundles"** (after the Gauduchon chapter). It contains the convex and Finsler norms, the Hirzebruch and Hopf complements, directional and integrated curvature, first-jet positivity and the ramified tests. The later chapters cite it only in prose.
- **Gauduchon chapter.** The core of the variational volume (definition, dual formula, dependence on the measure, mass extrema) now forms a section of the chapter on smooth equations. Five sections of the prescribed-equations and normalization chapters use it. A new section on balanced and pluriclosed metrics takes the parallel-torsion and deformation theorems from the research programme.
- **Variational-volume chapter.** It now receives:
  - the primitive elliptic bundles, from the research programme; the three earlier threefold propositions become corollaries of them;
  - the bigness-threshold proposition, from the research programme;
  - the invariant-mass subsection, now after the mass-geometry section.
- **New chapter "Polar curvature and zero-volume models"** (after the mass-bound chapter). It takes from the igood chapter the fibration reduction, the zero-volume products, the several-curve products and the polar currents on modifications, which depend on the curve-model theory of the mass-bound chapter. The Hopf transverse recovery moves into the mass-bound chapter.
- **New appendix "Cotangent torsors on split elliptic ruled surfaces".**
- **Smaller moves:**
  - the continuous Fredholm theory into the normalization chapter;
  - the concave equations to the end of the Hessian chapter;
  - Bott–Chern $H^{1,1}$ and the nef blowup metric into the framework chapter;
  - the bounded-mass lemma for Kähler modifications into the products chapter;
  - an example to where it is first cited;
  - several lemmas to just before their first use.
  
  Forward references from proofs and statements to later material went from 116 to about 40. Most of the remainder are within a chapter, or to the appendix, and none is circular.
- **Historical notes.** They follow the new chapter order, with new sections for bundle positivity, bounded-mass equations and cotangent torsors.
- **Preface.** The roadmap is updated.

### Errors found by the audits and corrected
- A narrowed scope ($n\geq1$ dropped with a section's setting) was restored.
- A deleted step that gave the bounded mass property was restored.
- A citation of a deleted remark was replaced by a direct argument.
- An ideal equality claimed "from the proof" now has its own justification.
- A main-text proof that cited the historical notes now cites the recalled theorem in the main text.
- Two undefined symbols and several position words in moved material were fixed.
- An internal proof route (through `thm:local-i-inputs`) replaces a reliance on an external characterization.
- The attribution of three theorems in the historical notes is narrowed to what the source proves: Qin's Theorem B is for bounded potentials, STW17 Theorem 1.4 for Gauduchon $\gamma$, and ALS26 for semipositive backgrounds.

## 3. Items for the author's decision
- **Forward references that remain** (none circular):
  - `cor:gaud-adjoint-lq` cited in the continuous Hessian adjoints;
  - `thm:hermitian-space-descent` (appendix) cited in the big minimal existence;
  - two same-chapter citations in the normalization and variational-volume chapters;
  - `thm:normalization-mass-quotient`, which cites results of the bounded-mass chapters.
- **Unused material, kept:**
  - the $L^2$ ideal-distance subsections of the framework (cited only in the historical notes);
  - two conclusions of `lem:four-point-family-adjoint-vanishing`;
  - a few alias labels with no users.
- **Proposals not carried out:**
  - one Liouville theorem for a class of cones;
  - a common domination lemma for the extended and finite relative theories;
  - deriving the quotient-surface example of the appendix from the toric statement (it would not shorten anything).
- **Historical attributions not checked against the sources:**
  - whether Seo's theorem assumes an effective boundary (the wording is true either way);
  - the exact form of Nguyen's global Chern–Levine–Nirenberg inequality;
  - the hypotheses of Guo–Song for the concave sections, which are now more general than before.

## 4. Other requests of 13 October
- **Workflow.** The repository workflow is updated: PLAN.md, the section "Review branches" of AGENTS.md, the book-writing skill and the editorial memory.
- **Pull requests and branches.** There are no open pull requests. Apart from `main`, only the review branch exists, and it is needed until the author merges it.
- **Bibliography.** The two entries for the author's SGPT lecture notes are merged into one.
- **GZ17.** The author's copy of GZ17 (in `research/sources/`) and the erratum were used to give locators for all GZ17 citations; no cited statement is affected by the erratum.

## 5. Build and publication
(See below.)
