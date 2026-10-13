# Proofreading of the author's new material — 13 October 2026 (review branch)

Request (13 October 2026): “I updated the book, please try to proofread the new version and continue to edit the book.”

Work branch: `claude/friendly-fermi-jzw1o1`. The author's `main` is not modified.

## 1. Reconciliation with the author's main

- The author's `main` (299cecc, 201 new commits since 29c89a3) was merged into the review branch (merge commit 0d590ec). It brought about 12,800 new source lines: the chapter on complex Hessian equations and new sections in most chapters, including the author's own integration of S04, S05, P05 and S07.
- The review branch's duplicate integration of S04/S05/P05/S07 was withdrawn before the merge (fe5b74a), in favour of the author's.
- Conflicts (68 hunks) were resolved by keeping the author's text and porting onto it the corrections of the review branch that were not yet in `main`: the checkpoint-529 accuracy review, the parts of the third review completed on 7–8 October, the journal-version locators and the checks against publisher texts. The historical notes were rebuilt from the author's version, with the review branch's paragraph-level corrections applied.
- Small fixes after the merge (e2cac72): “least smooth convexity index”; the linear-algebra construction precedes the proof of the Gauduchon criterion; “determinant measure”; TWWY15 journal pages. The SGPT bibliography entries no longer print “supplied by the author”.

## 2. Proofreading

The new material was divided into 26 parts (r4g01–r4g26, guide as in the earlier reviews: accuracy of details first, then clarity; base commit e2cac72). Every line of every new file and every changed paragraph of the changed files was read. Four independent audits (a4a–a4d) then rechecked every listed mathematical correction and renaming.

No theorem of the new material was found false. The corrections below are the substantive ones; the reports list all edits.

### Gaps repaired
- `thm:bounded-hermitian-smoothness`: the Evans–Krylov estimate was applied to a limit known only as a viscosity solution. The proof now solves a second approximation with the first approximants as prescribed potentials, so that the right-hand sides are uniformly Hölder, and applies the classical estimate to these smooth solutions.
- Hessian chapter, smooth proper existence: the uniformity of the trace estimate in the continuity parameter now follows from the statement of the estimate (fixed data, constant prescribed potential); a wrong reference (gradient bound only) and a wrong justification of $(N+1)d_N\ge d_N^{(m-1)/m}$ (maximum principle and Maclaurin) were corrected.
- Finite-curve envelope pullback: the converse half of the ideal-order comparison was missing.
- Small-curvature strict types: the proof relied on hypotheses of Demailly's regularization theorem that the book never states; it now uses the form recalled in the framework chapter.
- Curve-map descent: the descent now “preserves and reflects” the ordinary order (a caller needs reflection); holomorphy of the component identification and the fiber-maximum value at branch points are proved.
- Countable divisorial positivity: the step from global to local modifications in the ideal profile is now supported by the valuative criterion of the book.
- Transverse concentration, Fredholm lemma, Hopf rotational damping, Hopf Perron descent and transverse recovery, Hölder references, Sobolev capacity (gluing of mollifications), smooth capacity (hypotheses made explicit), bounded currents, mass comparison: missing justifications supplied, implicit hypotheses stated.

### Errors corrected
- Hopf projective traces: the point $P$ of the example was not on $B$; the Siu remainder is quasi-plurisubharmonic, not plurisubharmonic.
- Hopf chapter introduction: the all-dimensional construction concerns only the quotients by $z\mapsto e^{-1}z$; the corollary on unbounded masses is a statement about the manifold (no bounded mass property), as the definition requires.
- Warped subtraction: positivity holds exactly when $r>1$.
- Logarithmic model selection: the normalization of the chordal distance in the Green kernel was missing (the mean-zero claim depends on it).
- Variational volume: a non sequitur in the fixed-determinant remark; the determinant integrated in the nonclosed example; the Fourier data of the concentrating densities.
- Mass chapter: the Hopf example satisfies the second condition of the mass-invariance characterization for its own metric.
- Historical notes: locators corrected for BT82, KNHolder18, DP04 journal pages, Nguyen16 journal pages, TW10, WN19, DemCohomology15, Gauduchon85, KNHessian16, DKHessian17, GLHessian25, Fang, Chiose16 and Sze18 (journal version); four descriptions corrected (closed-factor roots, power-capacity equation, the two-curve adjoint case, the Hopf corollary); workflow vocabulary removed.

### Consistency
- Hessian chapter conventions fixed once ($\alpha^j\wedge\omega^{n-j}=\sigma_j(\lambda)\omega^n$, cones $\Gamma_m$, $\Gamma_m(\omega)$, $C_{n,m}$, admissible and strictly admissible, $H_m$ for smooth, continuous and bounded potentials).
- Chapter openings now describe the new sections (Gauduchon, prescribed equations, normalization, I-good, trace, variational volume, LCK, mass-bound volumes, appendix, rays, envelope systems, framework).
- Notation clashes removed by local renamings (listed in the reports and checked by the audits).

## 3. Items for the author's decision

- **Duplicated arguments.** The Hopf descent is proved in four places with four notations (`prop:hopf-basic-descent`, `thm:hopf-descended-hermitian-ma`, `prop:hopf-basic-mass`, the proof of `prop:hopf-fiber-ideal-envelope`). `thm:bounded-two-factor-convergence` is the case $p=2$ of `hessian:joint-decreasing-products`; `lem:gaud-determinant-measure-intrinsic` also follows from `lem:weak-gaud-determinant-dual`; the value of `thm:radial-positive-volume-nonbig` also follows from the warped example (now said in the text).
- **Placement.** `section_radial_residual_regularity` and `section_singular_radial_obstacles` use no normalization scalar or adjoint measure; they would fit the prescribed-equations and envelopes chapters.
- **Unused hypotheses** (statements narrower than their proofs): $n\geq3$ in the power-capacity theorem, $k\geq2$ in the closed-factor theorem, $n\geq2$ in the divisorial thresholds, $n\geq3$ in the Hessian multiplier bounds.
- **Unused lemma.** `lem:fixed-trace-gradient-interpolation` is cited only in the historical notes.
- **Classical inputs used without proof** (attributed in the historical notes): the factorization of modifications of surfaces into point blowups; resolution of singularities in the Hopf extraction lemma; the viscosity version of the Evans–Krylov–Caffarelli estimate in the Hessian chapter.
- **Citations whose journal text could not be checked** (locators name the arXiv version): KNHessian16, DKHessian17, GLHessian25, DNHolder14, DNSModerate10, KN15, DarvasCompletion17, DinewUniqueness08 (bibliography now J. Funct. Anal. 256), DemCohomology15 (bibliography now Abel Symposia 10). The citation of GZ17 for the global extremal function and Alexander–Taylor capacity has no locator.
- **Ongoing author passes.** The author's own reader pass continues with Chapter 12 (complex Hessian equations), which this review edited; the two should be reconciled when merging.

## 4. Audits, build and publication

- **Audits.** Four independent audits (a4a–a4d) rechecked about 190 listed corrections and 50 renamings, the coordinator's edits and a math diff of every edited file. They found no reviewer correction wrong. They fixed one reintroduced false claim (“$t\geq\varepsilon$ everywhere” in the rotational-damping depth bound), a missing constant term in a chapter opening, three widened Hopf scopes, one notation clash, and three overstatements in sentences written by the coordinator (variational-volume opening: Hessian multiplier bounds need $n\geq3$ and uniformly comparable solution forms, subtraction cost stated on compact Kähler manifolds; radial nonbig opening: the warped example matches only for $C=\mathbb P^1$ and a rescaled coefficient; countable poles give positive *upper* volume). The reports are in `proofreading-20261013-reports/`.
- **Checks.** Citation placement passes; no standalone paper, file or workflow is cited or mentioned; map typography and banned vocabulary were scanned book-wide.
- **Build.** Clean: 1798 physical / 1768 printed pages, no errors, no overfull boxes, no undefined references (one underfull line in a bibliography entry).
- **Publication.** Website commit 24475d2 (`Papers/SHPT_vibe.pdf` and `readme.md` only), PDF SHA-256 `79ae403f…`, homepage “A research monograph. 1768 pages. Updated October 13, 2026.”
