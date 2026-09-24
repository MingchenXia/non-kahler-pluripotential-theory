# Hopf normalization and smooth equations — checkpoint103

24 September 2026. This bounded increment reads all nine Chapter 9 inputs in a first correctness/writing pass. The complete second pass covers `chapter_smooth_equations.tex`, `section_smooth_estimates.tex` and `section_stw_gradient.tex`, including the new Section 9.9. The other six inputs remain in the second-pass queue; this is not a completed whole-chapter revision or whole-book certification.

## Proved model deduction

On the fixed Hopf threefold of Chapter 8, use the probability volume nu=omega^3/6 and Haar fiber average A. For smooth real F, write u_F for the mean-zero solution and b(F) for its scalar. Proposition 9.9.1 proves

    D(F) = b(F) + log integral_X exp(F) dnu,
    exp(D(F)) = 1 + integral_X |(u_F)_w|^2 dnu,
    ||u_F-Au_F||^2 <= 4(exp(D(F))-1).

D(F) is nonnegative, and vanishes exactly when F is a smooth base pullback. For a positive density of integral one, this characterizes equality in b(log f)>=0. The proof integrates the smooth mass formula and applies Proposition 8.7.1. Zero energy gives fiberwise constancy; the complementary base/vertical directions give a positive base potential. Conversely the smooth equation on the projective base and uniqueness on the total space recover the solution and its scalar. Every numerical coefficient uses the book's dd^c convention.

Corollary 9.9.1 lets v solve L_0v=G-integral Gdnu with mean zero and proves D'(0)=0 and D''(0)[G,G]=2 integral |v_w|^2dnu. The normalized Gauduchon adjoint identifies v with the derivative of u_{tG}; the smooth energy identity then gives the second variation directly. Wedge expansion shows that its kernel is exactly the smooth base-pullback functions. No general convexity or density-norm coercivity is asserted. Continuous or singular density equality remains a separate next test.

The normal Rethlas run `hopf_normalization_defect_01` completed with return code zero and verdict correct, with no critical errors or gaps. Its complete final report was read. Three explicit internal inputs are accepted: smooth solvability, uniqueness, dependence and adjoints; the Hopf geometry and smooth mass formula; and the bounded fiber-average estimate. The report verifies the deductions from those inputs, not all prerequisites afresh. Frozen submission and report are preserved. Production changes only mathematical exposition, declarations and pagination. No novelty claim is made.

## Existing arguments and second pass

The first pass follows the weighted torsion recurrence, Sobolev iteration, uniqueness, local implicit-function theorem, ellipticity, continuity method, exponential equation and normalization derivatives, then all STW inputs. The second pass rereads the root file, full trace calculation and ellipticity proof, and the gradient blow-up reduction. It checks their stated dependencies and preserves their hypotheses. The local implicit-function argument now explicitly starts at a given positive solution, so openness does not presuppose global existence. The weighted indices, logarithmic density, unknown scalar/function types and final Lp volume are declared before use. The inherited corollary label is corrected; references resolve. One display's trailing comma is corrected, and several result/formula page breaks are improved.

Across the nine inputs there are 29 previous formal blocks: 26 are byte-for-byte unchanged, while three differ only by an explicit density declaration, explicit unknown types, or the corollary label. A normalized comparison verifies all previous hypotheses and conclusions. There are two new untitled formal results. The remaining second-pass files are `section_stw_czero.tex`, `section_gauduchon_volume_adjoint.tex`, `section_stw_structure.tex`, `section_stw_second_order.tex`, `section_stw_liouville.tex` and `section_stw_continuity.tex`. Historical reports were consulted selectively; no claim is made to have freshly read every complete historical report.

## Sources and boundaries

STW17 now cites Acta Mathematica 219 (2017), no.1,181–211, DOI 10.4310/ACTA.2017.v219.n1.a6. The publisher archive and author's list agree. Theorem 1.4 on printed p.184, Section 3 starting p.191 and Section 4 pp.207–209 support the three active locators. The theorem page was rendered; n>=2 and the exact hypotheses were checked. This is a statement/locator/formula comparison, not a new full external proof audit. MathSciNet/current publisher failures and the TW10 check are recorded in the literature ledger. No new Popovici premise is introduced.

The same-day CV availability probe still returns September 23. It adds no September 24 coverage. Existing rolling coverage, candidate histories and historical replacement gaps are retained, with no new adoption or negative-scan claim. Fixed-region mass-defect localization, support and pluripolar charging remain unresolved. The general theory retains its mass-independent scope and the hidden Nakamaye chapter remains excluded.

## Validation

The book has 782 pages. The final build has no errors, unresolved references/citations, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. All 26 selected final pages were reviewed: ten last-reflow images were reread, and sixteen match the preceding render, with all sixteen read at one of the review stages. The selection covers the revised sections, their transitions, contents and bibliography; it does not cover the whole 44-page chapter. The three-input house audit improves from one error/six warnings to zero errors/five warnings.

Preservation checks cover the other 187 active author inputs, 29 SGPT originals, six supplied originals, all 188 historical reports and tracked verifier records, hidden sources, styles, checkpoint102 PDF/archive and unchanged 17-page companion. There are now 189 reports:179 correct and ten historical adverse; no historical verdict is changed. See `research/audits/build-snapshot-103.json`. Clean source reconstruction is recorded separately in `research/audits/source-package-portability-103.json` and must pass before release checks are complete. The broad book goal remains active and incomplete.
