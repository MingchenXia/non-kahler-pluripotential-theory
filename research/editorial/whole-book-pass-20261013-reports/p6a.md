# p6a: placement report (bundle positivity, continuous Fredholm, balanced–pluriclosed)

## 1. Moves made

**(a) Plan §1. Vector-bundle positivity → new chapter `chapter_bundle_positivity.tex`** ("Gauduchon degrees and positivity of vector bundles", `chap:gauduchon-bundle-positivity`, already `\include`d after chapter_gauduchon).
- I moved these `\input` lines out of chapter_gauduchon in their present order: section_convex_bundle_norm_obstruction (with its nested subsections), section_gauduchon_directional_curvature, section_ricci_flat_surface_curvature (+ tangent complement), section_integrated_hermitian_curvature (+ torus rigidity), section_projective_first_jet_positivity, section_ramified_root_metric_tests. Their headings are unchanged.
- **subsection_negative_bundle_logarithmic_weights**: I took its `\input` out of section_convex_bundle_norm_obstruction and put it last in the new chapter. Its heading went from `\subsection` to `\section`. The label `subsec:negative-bundle-logarithmic-weights` is kept. "In this subsection the base X need not be compact" now reads "In this section the base X has dimension n≥1 and need not be compact": the chapter's standing n≥2 would otherwise add a hypothesis the section never uses. I also deleted the sentence about this material from the overview paragraph of section_convex_bundle_norm_obstruction (l.171), since that material is no longer in that section. The new chapter's opening describes it instead.
- **New chapter opening.** It states the standing conventions: ω is a fixed Hermitian form on X (used by the directional-curvature section, through K_{ω,h}), and n≥2 unless a section specifies another setting. n≥2 is needed for the Gauduchon roots Θ=γ^{n-1} and for thm:gauduchon. The subsections that work with n≥1, n=1 or n=2, a projective X, a Kähler ω, or a noncompact base already say so. The opening names the inputs from `\cref{chap:gauduchon}`: thm:gauduchon, the trace identity, the root calculation before the proof of thm:lamari, and prop:adjoint-gauduchon. It then gives the two old paragraphs from chapter_gauduchon l.10 and l.12, adapted to the new position ("the same scalar equation" became "the compatibility condition for the scalar trace equation"). I added one clause on the ramified double cover and one sentence on negative bundles.
- **chapter_gauduchon opening rewritten.** l.10 and l.12 were moved out, and the Fredholm sentence (last sentence of l.8) was deleted. I added one sentence on positive pluriharmonic currents, the section that stays (`section_horizontal_pluriharmonic_currents`), and a closing pointer to `\cref{chap:gauduchon-bundle-positivity}`. The standing convention at l.4 is unchanged.
- **Dependency check** (with `lg.py`/`q.py` run on the edited tree, using a private copy in `scratchpad/p6a/`):
  - Everything the new chapter cites comes earlier: lem:qpsh-removable-analytic and lem:smooth-center-multiplier-ideal (framework), lem:ibp (mass), and thm:gauduchon, prop:gauduchon-trace, thm:lamari, eq:linearized-ma and prop:adjoint-gauduchon (chap:gauduchon).
  - The only later target is the prose pointer to sec:history-gauduchon.
  - The negative-bundle section now comes after its dependencies (lem:reciprocal-bundle-norm-levi, subsec:concave-neighbourhood-dual-norms, subsec:projective-complement-curvature-index).
  - Inside the new chapter, every forward reference is prose and was already there.
  - **Nothing left in chapter_gauduchon cites the moved block**, in a proof, a statement or prose; the one exception is the new prose pointer to the chapter. The only later users are prose: chapter_sections:90, section_hopf_sections:58 and history.
  - No cycles among the 113 labels in the moved blocks.

**(b) Plan §9. section_continuous_hermitian_fredholm → chapter_normalization.** I inserted its `\input` just before `\input{author/subsection_continuous_hessian_adjoints}`, inside "Supporting probability measures", after the Gauduchon adjoints subsection, and demoted it to `\subsection`. The label `sec:continuous-hermitian-fredholm` is kept. Its forward `\cref` to thm:continuous-hessian-adjoint-uniqueness now reads "in the next subsection". I added one clause to the normalization opening saying that the continuous-Hessian result uses this Fredholm theory.
- **Check:** the block has no dependencies other than GT01. All its users (continuous_hessian_adjoints:10, :24 in a statement, :67 and :119 in proofs) now come after it.
- subsection_continuous_hessian_adjoints names no old location, so I left it unchanged.

**(c) lem:balanced-pluriclosed-closed → chapter_gauduchon.**
- **Admissible.** Its proof is pointwise linear algebra of primitive forms and cites nothing.
- **Where it went.** I placed it after the remark paragraph that follows the proof of thm:gauduchon ("A Kähler form … is both balanced and pluriclosed …"), with the lead-in "The first statement has a converse." I did not put it directly after def:balanced-pluriclosed: there it would split the definition from Gauduchon's theorem, which follows it at once.
- **Old place.** I deleted the lead-in sentence in section_parallel_torsion_positivity ("…the fact, mentioned above, …"). The proof of thm:parallel-torsion-kahler still cites the lemma explicitly, so no further lead-in is needed.
- **Users** (section_non_kahler_geometry:104 in prose, parallel_torsion:95 in a proof, history) all come later.

## 2. Moves not made
- Hirzebruch subsections as an appendix: not done, as instructed.
- I kept the pointer at subsection_homogeneous_convex_regularization:8 on `sec:history-gauduchon`. `sec:history-bundle-positivity` does not exist yet, and repointing to it now would leave an undefined reference (see §4).

## 3. Coordination edits
- **(a)** section_hopf_sections:58: "In the notation of \cref{ex:hopf-exact-complement-index}, $L_k$ is … $E_a$ … so that example also gives" → "In the notation of \cref{subsec:flat-restriction-hopf-complements}, $L_k$ is … $E_a$ … so \cref{ex:hopf-exact-complement-index} also gives". I checked that L_k is E_a on X_q with q=e^{-1} and a=e^{-k}.
- **(b)** I deleted every unprinted comment that was a preprint locator or workflow note:
  - subsection_fixed_stein_finsler_hypersurface: 4 lines ("Source reconstruction: Liu--Wan …" through "… are not certified here").
  - subsection_hirzebruch_stable_extensions: 1 line ("Stable-extension attribution …").
  - subsection_hirzebruch_stable_ample_deformations: 3 lines ("Exact inputs: Walter …", "Approximation: …", "Curvature conclusion: …").
  - subsection_concave_neighbourhood_dual_norms: 2 lines ("Exact primary: Liu--Wan …").
  - None of my other files has comments.
- **(c)** chapter_sections:90 cites `sec:convex-bundle-norm-obstruction` and names no chapter, so no change is needed. No owned file says "in \cref{chap:gauduchon}" about the moved material. chapter_mass:148 (not mine) refers to Gauduchon metrics, which correctly stay in chap:gauduchon.

## 4. Replacements needed in files I do not own
- **book.tex:** none; the stub is already included.
- **chapter_history.tex** (line numbers are from the current working tree):
  - **New section.** Add `\section{Gauduchon degrees and positivity of vector bundles}\label{sec:history-bundle-positivity}` directly after the remaining paragraphs of sec:history-gauduchon, that is, before `\section{Bounded products and extended measures}` (l.132). Move into it, in this order:
    1. l.83–103 (eleven paragraphs, unchanged order), from "The deformation obstruction for convex norms in \cref{thm:convex-norm-deformation-obstruction}" to "The case of positive mean curvature in \cref{thm:bundle-curvature-complement-convexity,…".
    2. l.107 "Suppose that, for a holomorphic bundle $F$ of rank $r$ …" and l.109 "For external tensor products, …".
    3. l.121 "The mean-curvature criterion for RC-positivity …" and l.123 "The RC-positive tangent metrics on Ricci-flat surfaces …".
    4. l.125–126, the `\label{hist:integrated-hermitian-curvature}` line together with "The symmetrized sectional-curvature average …".
    5. l.128 "The first-jet characterization of Griffiths positivity …" and l.130 "The double cover in \cref{sec:ramified-root-section-tests} …".
    6. Last, l.105 "The negative-bundle weight in \cref{prop:negative-bundle-logarithmic-weight} …", which now matches the last section of the chapter.
  - **What stays in sec:history-gauduchon:** l.77 "Gauduchon metrics replace …", l.81 "The trace identity has a dual form …", and l.111–119 ("For the logarithmic parabolic …", "The calculation of the total variation …", "The support lemma for currents …", "The smoothing of positive pluriharmonic forms …", "The descent of horizontal currents …"). Optional: put l.115–119 before l.111–113, to follow chapter order, and retitle the section "Gauduchon metrics and linear mass" (keeping the label).
  - **Fredholm paragraph.** Move l.79 "\Cref{lem:continuous-hermitian-fredholm} combines the interior $L^p$ estimates …" into sec:history-normalization, directly before the paragraph "The continuous-Hessian extension in \cref{thm:continuous-hessian-adjoint-uniqueness} uses …".
- **Once that label exists**, in subsection_homogeneous_convex_regularization.tex l.8, replace "see \cref{sec:history-gauduchon} for attribution" with "see \cref{sec:history-bundle-positivity} for attribution". I own this file, but I did not make the change because the label does not exist yet.
- **preface.tex l.81:** "… and Gauduchon traces, non-pluripolar products and the Hopf construction complete the foundations." → "… and Gauduchon traces, non-pluripolar products and the Hopf construction complete the foundations. \Cref{chap:gauduchon-bundle-positivity} applies Gauduchon degrees to the curvature of vector bundles; the later chapters do not depend on it." The label graph confirms the last claim: the only later citations are prose.
- **chapter_research_program / section_non_kahler_geometry:** none (l.104 cites lem:balanced-pluriclosed-closed without naming a place).

## 5. Checks
- **chapcheck.sh** (`p6a`: chapter_gauduchon, chapter_bundle_positivity, chapter_normalization, chapter_sections, chapter_research_program), run twice and again after the final wording edits: no errors, no overfull boxes, and no undefined or multiply defined references. The only message is the ignorable `Underfull \hbox (badness 1783)` in section_pluriclosed_deformations. `lg.py` reports 0 undefined references and 0 duplicate labels.
- **mathdiff3 --base HEAD:**
  - The lemma's math is removed from section_parallel_torsion_positivity and added to chapter_gauduchon, and the two sides match.
  - New math: the chapter opening (ω, n≥2, (n-1,n-1), ddc, X), `n\geq1` in the negative-bundle setting, and `\ddc` in the new pluriharmonic sentence of chapter_gauduchon.
  - All other changes are reference changes (the new `subsec:flat-restriction-hopf-complements` reference, the removed pointers) and comment deletions. No other math changed.
- Inside the moved files, the only edits are the comment deletions, the negative-bundle heading and setting sentence, the removed `\input` line and overview sentence in section_convex_bundle_norm_obstruction, and the Fredholm heading and pointer.
