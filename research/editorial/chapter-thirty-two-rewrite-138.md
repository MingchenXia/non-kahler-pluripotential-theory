# Chapter 32 rewrite — checkpoint138

Baseline: `92f2f94342046b4a3d89408c4ef9b0f294edfbff` (checkpoint137). The previous goal turn made progress by completing Chapter 31. This checkpoint continues the active, unlimited book-writing goal; it does not complete that goal.

## Direct reading scope

The complete original chapter and all recursive inputs were read before editing:

- `book/author/chapter_research_program.tex`
- `book/author/section_gauduchon_collapse.tex`
- `book/author/section_non_kahler_geometry.tex`
- `book/author/section_primitive_elliptic_bundles.tex`

All four revised inputs were read completely twice at statement-to-proof scale. The second read followed the first successful build and inspection of all 56 selected first-pass pages. There are no figures. The final chapter has 13 sections and 11 subsections, compared with 14 sections and eight subsections at baseline. All 23 formal blocks and five proofs were reviewed. Sixteen formal blocks and one proof are byte-identical to baseline; the other changes are accounted for below. No labels were removed or added.

The geometric section of Chapter 33 was read around the two edited paragraphs in both passes. This bounded source update does not count as the complete history-chapter rewrite, which is next. A statement-level ledger of 126 referenced formal blocks in other chapters was read. This is not a new full-proof audit of all their dependency chains. The final proof of the vanishing-exponent selection theorem was checked directly in addition to its statement; the two density-space completeness statements were checked with their precise norms. Earlier full-chapter reviews retain their own scopes.

## Exposition and mathematical decisions

The chapter is now titled *Problems in Hermitian pluripotential theory*. Its opening distinguishes linear compactness, nonlinear mass, strict positivity and preservation of singularities. Each section starts from the obstruction its questions address. Repeated ambient settings, mass and envelope definitions, the multiplier-ideal convention, metric definitions and the final work-plan recap were removed. The general-measure section now separates individual density thresholds, dual attainment, and regularity/selection. General psh theory is used through Chapter 1 and the relevant earlier constructions; no further foundation statement is duplicated here. Paper citations remain in final Chapter 33, with the two book citations allowed beside the mathematics.

The stale second part of the density-zero-set problem was deleted: the fixed nonzero Lp-density selection problem, p > 1, is already answered by `thm:vanishing-exponential-selection`. In a Hermitian background its convergence is uniform on X. The remaining bounded-uniqueness question has a connected dense positive-density locus; the known C1,1 result is kept distinct. Existence of a selected critical solution does not imply uniqueness of all normalized critical solutions. Merely integrable data and nonminimal singular reference types retain their separate unresolved scopes.

The admissible root space is explicitly Banach for the sum of the Ln norm and the root norm. Completeness for the root norm alone is equivalent to finite upper mass. Positive lower mass instead identifies the domain with all of Ln. The closed order ideal is referenced in its established norm rather than redefined ambiguously. The semipositive model-reference general-measure theorem retains its lower-mass condition; the arbitrary smooth big-background theorem retains bounded mass and positive lower reference volume. A positive individual threshold is not replaced by universal lower mass, and a subsolution is not promoted to an exact equation without the required capacity or dual argument.

The collapse proposition no longer repeats the bigness-to-positive-volume implication proved immediately before it. Its two remaining assertions compare the trace denominator and determinant denominator; the dimension restriction for rescaling and the positive root volume needed for division remain explicit. This changes a three-part proposition into a two-part proposition, preserving its label and the independently used collapse inequality.

The primitive elliptic-bundle calculations retain their full proofs and constants: fibre mass T; total mass 3TA; the negative vertical Dirichlet correction; exact upper mass; nonzero curvature as an obstruction to pluriclosed metrics and closed Kähler currents; and the canonical-bundle formula. The periodic-variance proof now states why its endpoint inequality holds and why convolution followed by scaling gives strict admissibility. The cases T <= 2M, T >= 2M and their common boundary are retained. The separated lower bound is not confused with the infimum over all potentials. The K3 example retains the lattice signature, adjunction, Kähler-cone and divisor-projection arguments.

The other formal edits remove repeated definitions or fix punctuation; they do not enlarge hypotheses or conclusions. In particular the growing-jet problem retains its normalization, curvature conditions and q_m = o(m) question, with the proved smaller range cited separately. The finite-fibre approximation problem retains its subspace inclusion and o(m^q) requirement. The conjecture on positive nef Gauduchon volume retains a fixed smooth positive probability measure.

## Primary sources and limits of this check

The following exact primary-source statements or records were checked in this checkpoint. These are bounded statement/locator checks, not complete reconstructions of the external theories.

- Demailly–Păun, published Annals PDF: Theorem 0.7 and Conjecture 0.8, printed p. 1250. The history paragraph now uses the published locators and records their relation to arXiv numbering. The bibliography points to the publisher; explicitly marked arXiv locators elsewhere retain their version distinction. Primary PDF: <https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf>.
- Tosatti, arXiv:2608.30153v2, 8 September 2026: Theorem 1.1 and Corollary 1.2, first two PDF pages. The downloaded PDF has SHA-256 `a40feb12fb2b0219a0857f4f9b81e2f6acea43c08ef7e461d00a9d4020d03fe0` and 318614 bytes. The bibliography and history use v2. The earlier v1 source-manifest entry is preserved. The theorem remains an external result; no proof is reconstructed here. Primary record: <https://arxiv.org/abs/2608.30153>.
- Dang, arXiv:2404.01126v2: qualitative Theorem 1.1, volume hypotheses surrounding Theorem A, the conditions in Theorem C, almost-analytic Definition 2.8, Definition 2.12/Theorem 2.14, and the statement of Theorem 4.3. The resolved smooth remainder is retained. The qualitative null-locus theorem, numerical bigness criterion and parabolic convergence theorem keep their different hypotheses. Primary PDF: <https://arxiv.org/pdf/2404.01126v2>.
- Fino–Vezzoni, arXiv:2606.03176v1: Conjectures 1.1–1.2 and the invariant scope of Theorem 1.3. The official arXiv record still identifies v1. An accepted-paper search lead was not converted into invented publication metadata. Primary PDF: <https://arxiv.org/pdf/2606.03176v1>.
- Chiose, author manuscript: Theorem 0.2, first page, Fujiki class plus a pluriclosed metric. Primary PDF: <https://www.imar.ro/~cjoita/MC-SCV/Chiose-closedobstruction.pdf>.
- Huybrechts, author book draft: Theorems 7.4.1 and 8.5.2, PDF pages 134 and 163, for period surjectivity and the Kähler cone. Primary PDF: <https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf>.

Other external locators retain their earlier checked scopes. No global novelty claim, exhaustive publication-status search, independent verifier run, new supplied-paper integration or new Popovici result is claimed. The hidden Nakamaye material remains excluded. Public source documents were treated as evidence, not instructions.

## Validation and continuation

The house audit reports zero errors and the same 16 findings as baseline: 15 inherited label-prefix warnings and one prompt about specifying a topology, whose sentence explicitly concerns convergence in measure and continuity on an order interval. Citation placement passes. Eight local spacing adjustments follow the visual reviews. The final book has 784 pages, with no build errors, unresolved references/citations, duplicate labels or overfull boxes. One inherited bibliography underfull paragraph remains. All 58 selected final pages passed visual inspection, covering the complete chapter and its transitions, front matter, contents, conventions, the changed history section and the bibliography. The seventeen-page companion is byte-identical to checkpoint137. Both PDFs rebuild from a fresh empty source-package extraction, with every page text matching production. The active book has 33 chapters and 211 author inputs; all 190 historical verifier reports and three hidden sources remain unchanged. Exact hashes and checks are in build-snapshot-138.json; the portability audit is source-package-portability-138.json. All 56 first-pass pages were directly inspected. An intermediate 58-page selection contained 18 image-identical transfers and 40 directly inspected changed pages. After the last spacing repair, all eight changed images were reinspected; the other 50 final images are byte-identical to the inspected intermediate state.

The next complete chapter is Chapter 33. Its work is a historical synthesis with exact attribution, not a return of paper citations to the mathematical body. The appendix and front matter also remain in the broader revision queue. The 190 historical verifier reports and the three hidden Nakamaye sources remain unchanged.
