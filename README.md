# Singularities in Hermitian pluripotential theory

Working research manuscript for the compact Hermitian generalization of Mingchen Xia’s *Singularities in global pluripotential theory*. The supplied svmono template, fonts and mathematical conventions are retained. This is an AI-assisted draft for mathematical review; the full project remains in progress.

The checked checkpoint29 manuscript has 621 pages, 32 chapters and an appendix.
Its editable source is in [book/](book/). Run `bash scripts/build-book.sh` to
rebuild the PDF in `output/pdf/`; run `bash scripts/build-numa-note.sh` to rebuild
the 17-page standalone note. These builds require a TeX distribution with
`latexmk`, pdfLaTeX, BibTeX, newtx fonts and the packages in `book/preamble.tex`.
The supplied template is included under `book/style/`.

This is a private source repository. The [blueprint](BLUEPRINT.md) records the
current research priorities, the [changelog](CHANGELOG.md) records significant
updates, and [research/STATUS.md](research/STATUS.md) gives the exact proof and
release status. Pending checkpoint30 drafts are preserved under
`research/editorial/`; they have not replaced the checked book chapters.

Significant updates are committed and pushed automatically under the standing
workflow in [AGENTS.md](AGENTS.md), with an hourly synchronization check as a
fallback. Compiled PDFs, source archives, downloaded reference texts, temporary
previews and raw verifier runtime files are kept out of Git. The checked source
can be built independently; audit metadata retains hashes of the local releases.


Chapters4–7 now sharpen the distinction between the full Gauduchon trace and nonlinear mass. When bounded mass fails, the existing convex-series witness has integrable complex Hessian coefficients and smooth approximants converging in coefficient L1, while their determinant masses diverge. Small multiples have full traces converging in total variation to a smooth trace and still have infinite extended mass. The finite damping theory applies without BMP.

Chapter13 now also reconstructs minimal ordinary-type Lp equations for arbitrary smooth big backgrounds, without BMP or PVP. Strict pole-barrier comparison, resolution and a singular Gauduchon trace estimate are proved; exponent zero has a unique scalar, not necessarily a unique potential.

Chapter14 reconstructs the semipositive prescribed-reference general-measure equations under the stated model condition and positive lower volume, without BMP. For arbitrary smooth big backgrounds, it proves relative envelopes, domination and continuity under BMP and positive lower reference volume. Its later sections now complete general non-pluripolar measure existence for an arbitrary model reference, unrestricted weighted addition, and the ordinary singularity-type conclusion for Lp data. The construction proves the cross-class rooftop before relative projection, then maximizes weighted supersolution mass. Positive lower model volume and BMP imply metric PVP, so omitting a separately listed PVP does not weaken the hypotheses. Positive-exponent potentials and zero-exponent scalars are unique; zero-exponent potentials need not be.

Section16.6 proves that ordinary envelopes of dyadic analytic regularizations decrease to the ideal envelope, without BMP, closedness or bigness. This gives a specific approximation criterion for equality of ordinary and multiplier-ideal envelopes. In a Hermitian background, rational scaling keeps the approximation in the same background and proves analytic density in the entire elementary ideal-type metric space. A topology on arbitrary ordinary singularity types and a general volume characterization remain open.

Sections20.8–20.9 give exact higher-dimensional traces over an ambient curve problem under a smooth connected-fiber holomorphic submersion. A Green pullback realizes every compact-model divisor order and its ordinary type is independent of a sufficiently large background. A product formula for extended Monge–Ampère measures includes infinite total mass and gives separated Lp equations. Products with a factor failing BMP have finite- and infinite-mass representatives with all the same multiplier ideals and exact trace numbers. Corollary24.5.1 combines the Gauduchon mass bound with a smooth residual current to determine a canonical ordinary type on each fixed model; this alone does not recover the trace data on further modifications.

Section28.6 proves exact multiplier-ideal and partial-kernel transformation formulas under a modification, including the relative canonical bundle and its Jacobian metric. Closed-background ideal envelopes and non-pluripolar measures also descend. With a Kähler modification and positive closed-curvature mass, the original SGPT equilibrium theorem gives kernel-measure and determinant-functional limits. This geometric hypothesis implies BMP; the general birational identities require no mass bound. The lower-dimensional Hopf limit and general lower Fubini–Study questions remain distinct.

Sections28.10–28.11 treat non-descended isolated logarithmic selecting weights on fibrations. Exact base point-vanishing spaces differ from base multiplier-ideal spaces by O(m^(q-1)) dimensions, giving kernel and determinant limits under a positive-mass base hypothesis. The one-point Hopf model has explicit binomial kernels, an L1 and local-uniform potential limit, and total-variation measure convergence. Moving the pole along its fiber preserves every selected space, even with positive intrinsic growth; the limit can lose the original ideal type. These arguments require no BMP on the total space.

Chapters 29–31 develop ordinary Bott–Chern loci, the full supplied transcendental Nakamaye proof, and locally conformally Kähler geometry. The new chapter proves the weak nef-difference criterion through Monge–Ampère equations and Gauduchon duality; its two regularization lemmas allow a Hermitian reference metric with a closed background. The main null-locus theorem remains Kähler. Chern–Ricci-flat Gauduchon rigidity is also proved. Section31.8 reconstructs Lee–Gauduchon duality and bimeromorphic invariance, excluding the full kernel from strict tests. Its explicit Calabi–Eckmann example has zero Lee–Gauduchon cone but no strongly Gauduchon or balanced metric. These arguments assume no bounded mass property. Transverse Vaisman existence remains an explicit external input.

The [reading guide](research/READING-GUIDE.md) gives three routes through the book. The [standalone nonuniqueness note source](book/numa-thin-zero-set-note.tex) contains the full construction of a smooth density vanishing exactly quadratically on two real hypersurfaces with uncountably many normalized smooth solutions. It shares its proof source with the main book; rebuild it with `bash scripts/build-numa-note.sh`.

Read [PLAN.md](PLAN.md) for the authorized scope and [research/STATUS.md](research/STATUS.md) for current progress, remaining work, and continuation details. [The literature ledger](research/literature.md) records exact versions and hypotheses; [the comparison matrix](research/comparison.md) preserves the full original-book scope.

Mathematical and build audits are saved in `research/audits/`; bounded independent Rethlas reports are in `research/rethlas/verification/results/`. Their scope and conditional inputs must be respected. Original reference sources and the original Rethlas installation remain unchanged.

A [brief Chinese research report](research/BRIEF.md) summarizes the results, the uniqueness criteria and counterexamples and the remaining proof boundary.
