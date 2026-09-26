# Chapter 8 rewrite — checkpoint152

Baseline: `096b20be297b4e9e99fc0c3b91134b9b2f988585` (checked checkpoint151).

## Scope and reads

The complete chapter is `book/author/chapter_hopf.tex`, with no nested inputs. The whole original was read before editing and saved with its source hash. The complete revision received a first mathematical/editorial read, a build and visual inspection, and a second direct mathematical/editorial read. The bounded layout adjustments are checked at their affected statements and on the rendered pages. No other author input is changed or claimed as newly reviewed in full.

The dependency checks cover the Chapter 2 mass polynomial, Chapter 1 exact bounded regularization and almost-everywhere equality, and the Chapter 7 critical logarithmic weight. The adjoining Chapter 9 opening and the existing historical attribution were checked at their interfaces. This is not a new recursive review of those chapters or the source paper. Both installed writing skills apply. Their existing rules already require uniform constants at a varying-parameter application, single definitions and precise dependency placement; no new skill rule is needed.

## Mathematical and editorial changes

Six sections replace the previous seven. The heat-potential estimates and the square estimate now form one section, explaining why the logarithmic gradient controls the mixed derivative. The mass identity uses the earlier mass polynomial instead of repeating its cancellations. The square estimate explicitly has a constant depending only on the fixed elliptic curve, uniformly in every displayed parameter; its later application with `kappa chi(ax)^2` is pointwise, with the zero-cutoff case handled separately.

The sharp fiber-average inequality now precedes the minimum-mass corollary and supplies its lower bound. This removes the earlier separate bounded-regularization argument and the repeated definition of lower mass. The converse equality argument specifies positivity of the approximating base forms. The distant recap of normalized equation solvability is removed; that theorem remains in its owning chapter. Concise existing introductions, complete calculations, the critical damping application and the actual remaining uncertainty about its optimum are retained.

All thirty original labels and all nine formal result statements remain. No source attribution or bibliography changes; non-book citations remain in Chapter 33. There is no new external result, bibliographic locator, Popovici dependency or independent verifier run.

## Mathematical checks

The torsion identities give `ddc(omega^2)=0` and `ddc omega=-alpha^2`. The probability Haar measure on the elliptic fiber gives total background mass six, and the mass polynomial reduces to six times vertical Dirichlet energy. This identity holds for every smooth real potential, before any positivity restriction. The radial matrix and its Schur complement retain both horizontal positivity conditions and the separate statement at the base origin. Smooth extension requires eventual constancy; the nonconstant base region is allowed to vary with the potential.

The Fourier eigenvalues have least nonzero value `1/4`. Integrating the heat kernel gives the exact heat equation, the logarithmic Hessian bound, energy `2 eta^2 log(1/t)+O(eta^2)` uniformly at small time, and exponential estimates for fixed derivatives at large time. The nearest-lattice-point proof gives the logarithmic-gradient estimate. In all three cases of the square estimate the constant can be chosen independently of `kappa`, which justifies its use with the vanishing cutoff factor wherever that factor is positive.

The exact square completion, small-time and large-time defect bounds, and the changes of variable were checked directly. The initial transition has superpolynomially small time; the middle interval has integrable defect tending to zero; at the final cutoff the exponential error is smaller than the positive background Schur complement. The negative slope is uniformly small. The correction uses a strict smooth majorant whose approximation error may depend on the current support length. Its negative second derivative lies in a fixed interval of uniformly positive Schur complement. Its first derivative remains small, and its eventual constant value need not begin at the heat cutoff. On a fixed base ball the unchanged fiber energy tends to infinity, proving unbounded mass.

Fiber averaging preserves the metric and descends to a base potential. The fiber Poincare constant four, combined with the mass coefficient six, gives the sharp coefficient `2/3`. Exact bounded regularization and dominated convergence pass this inequality to every bounded potential; almost-everywhere equality becomes equality of the quasi-plurisubharmonic functions. Pullbacks of bounded base potentials have mass six by the same regularization, while the lowest nonzero fiber mode proves sharpness. Near-minimal mass controls variation along fibers, not the choice of base potential. The logarithmic damping application keeps `a>1` and does not claim that its optimality is settled.

## Release checks

The changed author input has zero house-audit errors and the same two inherited warnings. Non-book citations remain in Chapter 33. The 804-page book and seventeen-page companion compile without unresolved references/citations, duplicate labels or overfull boxes; the inherited bibliography underfull paragraph remains. All 44 selected final pages pass visual review, with 11 changed images directly inspected and 33 byte-identical to inspected first-output images. Both outputs rebuild from a fresh empty source-package extraction, with every page text matching production. There are 33 active chapters and 216 author inputs; all 190 historical verifier reports and three hidden sources remain unchanged. Exact scopes are recorded in chapter-eight-rewrite-152.md, build-snapshot-152.json and source-package-portability-152.json.

The first selection had 44 pages: 22 were directly inspected on 6 sheets and 22 were byte-identical to the checked checkpoint151 output. Local space reservations keep the heat-potential and square-estimate statements together and keep the energy and scale displays with their lead-ins. The final visual scope covers the complete Chapter 8 and its transitions, front matter and contents, and every other changed body page matched within its chapter while ignoring shifted running page numbers. The final layout refresh was inspected again on every changed image. All thirty original labels remain. The companion is byte-identical to checkpoint144. The final package manuscript and build payloads match those rebuilt; later changes affect only research documentation. An initial reconstruction attempt stopped at citation validation because packaging overlapped a running build and read an incomplete recorder list. After that build finished, the package was regenerated, its full active-source inventory was checked, and both outputs were rebuilt in a new empty directory. The failed temporary extraction was not used for the release. Routine private synchronization follows the checks.

## Continuation

Continue with the complete present Chapter 9 and all its nested inputs, then Chapter 10. The broader writing and research goal remains active and incomplete.
