# Placement plan (read-only analysis)

Method: `lg.py` expands book.tex (\include, then nested \input, with comments stripped, so the Nakamaye files are skipped) into 58.8k lines in reading order. It finds 2928 labels and 7780 refs. Each ref is tagged with its context (proof, statement kind, or prose, meaning remarks and running text) and its owner. `q.py analyze(block,dest)` lists the dependencies that fall after the destination and the users that fall before it. Scripts are in the scratchpad (`lg.py`, `q.py`, `fwd.py`). Line numbers come from the 13 Oct 2026 snapshot.

## 1. Vector-bundle positivity → new chapter (DO, with changes)
- **Block.** chapter_gauduchon.tex \input lines 202 (convex_bundle_norm_obstruction, 1487 lines with its 12 subsections), 314 (directional_curvature), 315 (ricci_flat + tangent_complement), 316 (integrated_hermitian + torus_sectional_rigidity), 317 (projective_first_jet) **and 318 (ramified_root_metric_tests)**. The block has 92 labels plus 4 from the ramified file.
- **Dependencies.** Everything comes earlier: framework (lem:qpsh-removable-analytic, lem:smooth-center-multiplier-ideal), lem:ibp, and from chap:gauduchon thm:gauduchon, prop:gauduchon-trace, thm:lamari, eq:linearized-ma and prop:adjoint-gauduchon (l.208/218). The only later target is a prose pointer to sec:history-gauduchon (homogeneous_convex_regularization:8).
- **Users.** section_ramified_root_metric_tests cites the first-jet section in 8 places, including the statement of cor:ramified-positive-untwisted-failure, so it must move too. The other users come later: chapter_sections:90, section_hopf_sections:58 (prose) and history. **No section of chapter_gauduchon after the block cites it**, other than files that move with it.
- **Where the extra files go.** torus_rigidity and flat_restriction_hopf_complements are nested in the block and go with it. horizontal_pluriharmonic_currents stays: it is used by compactness and bott_chern_loci, and is about currents, not bundles. parabolic_entropy and total_variation stay as subsections of "The adjoint measure". continuous_fredholm goes to normalization (see 9).
- **Destination.** New file `author/chapter_bundle_positivity.tex`, "Gauduchon degrees and positivity of vector bundles", \label{chap:gauduchon-bundle-positivity}. \include it after book.tex:49, with the six \input lines in their present order.
- **negative_bundle_logarithmic_weights.** Its proof uses lem:reciprocal-bundle-norm-levi (l.46), so it **cannot go next to section_psh_local_ideals**. It may go to the end of the new chapter; its only user is the prose at convex:171.
- **Hirzebruch subsections as an appendix: DON'T.** They are cited in statements and proofs of three later corollaries (cor:hirzebruch-fixed-stein-hypersurface, cor:hirzebruch-non-two-convex-complement, cor:hirzebruch-exact-complement-index, the last also used in the statement of cor:stable-factor-complement-convexity). They also depend on thm:convex-norm-deformation-obstruction. A final "Hirzebruch surfaces" section is admissible only if it takes these four corollaries along.
- **Text edits.**
  - Move the opening paragraphs chapter_gauduchon.tex:10 and :12 to the new chapter's opening, and copy the standing convention from l.4.
  - Preface l.81 ("Gauduchon traces … complete the foundations"): add bundle positivity.
  - History: create sec:history-bundle-positivity after l.131 out of paragraphs 83–109 and 121–130. Paragraphs 111–119 stay. Repoint homogeneous_convex_regularization:8 to the new section.

## 2. Variational-volume core → chapter_smooth_equations (DO)
- **What the proofs use.** The core's proofs use only thm:tw-smooth (setup, l.60), thm:gauduchon, prop:gauduchon-amgm/eq, thm:bounded-exact-regularization and def:bmp. All of these come before l.344 of smooth_equations, and nothing in the core is circular.
- **The citations are not in remarks.** Proofs cite it at lower_mass_solvability:56, density_subsolutions:118, integrable_gauduchon_tests:39 and density_stability:97. Prose cites it at exponential_equations:210 and integrable_tests:4/84. Rephrasing would not help: thm:integrable-gauduchon-formula needs the dual formula itself.
- **Block.**
  - chapter_gauduchon_variational_volume.tex 18–94 (sec, def, prop:gaud-volume-elementary, thm:gaud-volume-dual-formula, cor:gaud-volume-big-positive), plus the first sentence of l.15 (the definition of pseudoeffective).
  - 209–247 (prop:gaud-volume-density-comparison, prop:gaud-volume-density-independence).
  - section_gauduchon_volume_extrema.tex 1–39 (thm:gaud-volume-mass-extrema, eq:gaud-lower-mass-formula). prop:lower-mass-smooth-attainment (41–61) may stay.
- **Destination.** A new `\section{Gauduchon quotients and the normalization constant}` in chapter_smooth_equations.tex after l.342, before sec:hopf-normalization.
- **After the move.** The only later targets are prose pointers: l.82 (sec:individual-density-subsolutions, thm:integrable-gauduchon-formula, sec:weak-gauduchon-duality), l.92 (thm:radial-positive-volume-nonbig) and extrema l.7. The only user before the destination is conventions:43. The move removes 9 forward references.
- **Text edits.**
  - extrema l.7 must define 𝓜 itself (drop "again … as in sec:invariant-mass-reference-densities").
  - The variational chapter's opening (l.7–9 and 15) becomes "recall from Section …".
  - Add a sentence to the smooth_equations opening.
  - Remove no labels; sec:gaud-volume-definition and sec:gaud-volume-positive-cone have no users.

## 3. Hopf transverse recovery → mass_bound_volumes (DO, with changes)
- **Block.** section_hopf_transverse_recovery (\input at chapter_envelope_systems:240; 5 labels).
- **Dependencies.** The proofs cite thm:positive-volume-system-recovery (#52317) and countable-divisorial:positive-mass. The prose pointer is to subsec:countable-divisorial-positivity. The rest is earlier.
- **Users.** Only envelope_systems:8 (chapter opening, prose), the research programme and history.
- **Destination.** countable_divisorial_positivity is a subsection, and lines 1196–1200 belong to the same section. So insert the \input **before chapter_mass_bound_volumes.tex:1202** (\section{Model comparison under background changes}), not right after 1193.
- **Text edits.**
  - Add a sentence: the Hopf threefold lacks bounded mass, and the standing hypothesis is used on the base ℙ².
  - Change the Hopf sentence in envelope_systems:8 to "(in \cref{chap:mass-bound-volumes})".
  - The move removes 2 forward references.

## 4. Invariant mass and reference densities → after mass_geometry (DO)
- **Block.** section_invariant_mass_and_reference_densities (a \subsubsection, \input at parallelizable_gauduchon_cones:256).
- **Dependencies.** The proofs cite thm:threefold-mass-minimizer and eq:threefold-mass-dirichlet (mass_geometry) and thm:gaud-volume-mass-extrema. After the move everything comes earlier.
- **Users.** extrema:7 (prose; fixed under 2), the research programme and history.
- **Destination.** Add `\input` after chapter_gauduchon_variational_volume.tex:250, delete parallelizable:256, and demote \subsubsection→\subsection.

## 5. hessian:bounded-nonvanishing (DO)
- Move section_hessian_bounded_locality.tex 178–190 to after the proof of hessian:strict-bounded-domination (section_hessian_mass_comparison.tex:409).
- No circularity: reach(strict-bounded-domination) does not contain the proposition.
- The only user is history:375. Drop the clause "whose proof does not use the present proposition".

## 6. lem:kahler-modification-bounded-mass (DO)
- Move chapter_flag_bodies.tex 142–161, together with the Moishezon sentence of l.140, to after chapter_products.tex:207 (after the proof of prop:bmp-metric, its only dependency).
- All 6 proof users come later. This removes normalization_mass_quotient:29 → flag_bodies.
- flag_bodies keeps its section with a one-line recall.

## 7. Bott–Chern H^{1,1} (DO WITH CHANGES)
- lem:bc-one-one-current-description's proof uses lem:closed-current-global-potential (section_divisorial_potential_domination.tex:3, framework #2851). So the destination near chapter_framework:103 is too early.
- Put the definition and the lemma (section_bott_chern_bclasses.tex 6–22) right after that lemma's proof (divisorial_potential_domination.tex, before l.23).
- At framework:103 add a pointer. In bott_chern_bclasses and bott_chern_loci:21, "recall".

## 8. Concave equations → end of chapter_hessian_equations (DO)
- Move chapter_weak_equations.tex:215 and :217 to after chapter_hessian_equations.tex:69.
- Dependencies are all earlier (thm:lp-potential-estimate, prop:stw-czero-reconstructed, eq:stw-contact-area, thm:tw-smooth, thm:gauduchon). The only users are history:197–199.
- **Text edits.**
  - Delete the weak_equations opening l.13 ("The final two sections …").
  - Add to the Hessian opening, and note that these sections do not use the fixed 2≤m<n.
  - concave_gap l.4 ("determinant bounds used above") and l.6 ("density fixed at the beginning of the chapter").
  - Move history 197–199 to sec:history-hessian-equations.
- A separate chapter is unnecessary: 309 lines.

## 9. Continuous Fredholm → chapter_normalization (DO)
- No dependencies. Users: continuous_hessian_adjoints:10, 24 (statement), 67, 119.
- Insert `\input{author/section_continuous_hermitian_fredholm}` before chapter_normalization.tex:200, demoted to \subsection. Delete chapter_gauduchon:294 and the last sentence of chapter_gauduchon l.8.
- Move history:79 to sec:history-normalization.

## 10. Cotangent torsors → appendix (DO)
- **Block.** section_nef_flat_divisor_complements.tex 78–710, 22 labels.
- **Dependencies.** Only a prose pointer, cor:flat-divisor-nonstein (l.81).
- **Users.** Only history 728–732.
- **Destination.** New `author/appendix_cotangent_torsors.tex` (a \chapter, "Cotangent torsors on split elliptic ruled surfaces", \label{app:cotangent-torsors}), \include'd after book.tex:93. Promote \subsection→\section. Rewrite l.81 ("The remaining subsections give…") and leave a one-sentence pointer at the end of section_nef_flat_divisor_complements.
- **What stays.** subsec:flat-divisor-complements (1–77) stays: its proof cites thm:flat-anticanonical-neighborhood and it belongs to the nine-point story.
- **Text edits.** Preface l.83: "The appendices …".

## 11. Cluster limits (DO)
- No circularity: reach(cor:individual-positive-threshold-exponential) does not contain the proposition.
- Cut the last two sentences of the statement and the last proof paragraph (section_threshold_subsolution_envelope.tex:16, 23). Make them a new corollary (e.g. cor:exponential-cluster-threshold-subsolutions) after section_individual_exponential_equations.tex:82, before the paragraph at l.84.
- Repoint semipositive_exponential_limit:41 and gauduchon_moment_equations:46. Both come later.

## 12. Smoothing obstruction (DO WITH CHANGES)
- **Example** (section_threshold_divisorial_geometry 1–14).
  - Destination: after section_gauduchon_linear_duality.tex:83, the end of the file. 𝒢_ω and 𝒞_ω are defined there (l.26/31).
  - The proof's only later dependency is ex:gaud-metric-blowup (#37545), used just for C²=−1. Replace that citation with the standard fact.
  - Reword l.83 to "the following example".
  - The weak_gauduchon_duality:88 proof then cites backwards (this removes a forward reference).
- **m_ω/κ_ω paragraph** (16–23).
  - Destination: section_smooth_cone_duality after l.37, replacing "The inequality can be strict…". Write ω as h there.
  - Its dependencies are earlier (eq:gauduchon-linear-minimum, the section itself).
- Reword threshold_divisorial l.25 ("We return…").

## 13. Primitive elliptic bundles (DO WITH CHANGES)
- **Where it sits.** It is \input at section_non_kahler_geometry:69, which is inside chapter_research_program:108. So yes, it puts proved results (5 proofs) in the research programme.
- **Block.** Lines 1–145: setup, prop:primitive-elliptic-metric, lem:periodic-variance-bound, prop:primitive-elliptic-separated and the comparison paragraph.
- **Dependencies.** The proof needs only thm:gaud-volume-mass-extrema. The paragraph at l.143 is prose.
- **Destination.** Insert as \subsection{Primitive elliptic bundles} before chapter_gauduchon_variational_volume.tex:264. The three special propositions then become corollaries by specialization, with q=e^{2π}, A=2, κ=1. Their labels stay because prescribed_equations cites them.
- **The rest.** Also move ex:primitive-elliptic-k3 and prop:primitive-radial-root-volume (146–194); their only later dependency is prose. Keep prob:primitive-elliptic-lower-mass and a lead-in in the research programme. history:68 is unaffected.
- **Same problem elsewhere.** The research programme also proves results in section_parallel_torsion_positivity (thm:parallel-torsion-kahler), section_pluriclosed_deformations (thm:pluriclosed-deformation-persistence) and section_gauduchon_collapse (prop:gaud-positive-volume-collapse).

## 14. One corollary for h≥cg (DO, after 2)
- The corollary needs eq:gaud-lower-mass-formula and thm:gaud-determinant-endpoint.
- thm:gaud-determinant-endpoint itself already cites thm:gaud-volume-mass-extrema forward in the same chapter (determinant_integrability:75). After proposal 2 both come earlier, and the new corollary can follow thm:gaud-determinant-endpoint. Without 2, put it after the extrema subsection.
- Replace lem:determinant-background-transport (whose only user is elliptic_endpoints:97) by a citation. cor:geometric-determinant-bound becomes "combine with mass invariance" and keeps its label (users vanishing_lower_mass:267 and the research programme).

## 15/20/22/23/24. Second half of chapter_igood — one plan
Graph facts:
- (i) sec:ordinary-type-topology is cited in **proofs and statements of chapter_mass_bound_volumes** (curve_ordinary_topology:21/33, curve_all_obstacles:17/26/70), so it must stay before that chapter.
- (ii) The curve-model sections of mass_bound (1578–1889) depend on its main body (cor:full-mass-envelope-characterization, prop:model-volume-separation, thm:model-volume-capacity-convergence, prop:conditional-i-characterization), so they cannot move earlier.
- (iii) The moved block (below) has **no** dependency after the end of mass_bound. Its users before that point are prose only: preface 46/50, all_obstacle:86, mass_bound:11, mass_bound:1199. The one exception is ex:zero-volume-comparison-collapse (mass_bound 735–753), whose proof cites the two zero-volume examples; it moves with them.

**Plan.** New chapter `author/chapter_polar_model_topologies.tex`, "Polar curvature and zero-volume models", \include'd after book.tex:86.
- Opening: chapter_igood.tex 229–262 (it now summarizes earlier results), with its own standing assumptions. It must allow the non-BMP Hopf example.
- §Fibration reduction: section_fibration_obstacle_reduction, with **P24**: move prop:finite-cover-envelope-transport (all_obstacle_topology 90–121; dependencies are framework only) before cor:fibration-component-cover (l.332). This is its only use.
- §Divisorial products and zero volume: section_zero_volume_product_obstacles (\input at all_obstacle:126) with its nested files, and ex:zero-volume-comparison-collapse inserted after ex:nonclosed-zero-volume-distinct-models.
- §Several curve factors (**P22**).
- §Polar currents on modifications: polar_current, gauduchon_polar_comparison and diffuse, plus igood l.269. Promote one level throughout.
- **P23:** move finite-curve:envelope-pullback, finite-curve:model-retraction and finite-curve:averaging-not-nearest (finite_curve_pullback_models 1–131, 170–203) to mass_bound before l.1887 (the end of sec:curve-model-backgrounds). Their dependencies are framework and prop:analytic-envelope-type; their only users are the research programme and history. finite-curve:original-base-subspace stays: it cites fibration:*.
- **P15 reduced:** merge qu:i-good-no-bmp into qu:singularity-topology-program (research_program:232). Its only user is the prose at arbitrary_curve_product_metrics:82. Do not move the overview to the research programme.
- **prop:ordinary-topology-gauge-failure** stays. Its only forward reference (l.159 → ex:diffuse-polar-zero-model) uses just "a polar Cantor set carrying a nonatomic measure". Extract that as a framework lemma in sec:local-polar-parts, cited by both.

**What stays in igood, and why:** §1–§5 and §ordinary topology (analytic closure, separation, obstacle transport, all smooth obstacles, countable-pole obstacles), all foundational and used by mass_bound and trace_data; §small curvature (used by trace_data statements). After the move, igood has only prose forward pointers: igood:196, ordinary_type:6/173, all_obstacle:4/86.

This removes 59 forward references: 55 to mass_bound (including the 4 in the problem and the gauge-failure one), 3 to trace_data and 1 to the Gauduchon volume chapter.

**Text edits.**
- igood opening (no change needed). Preface l.83: add the new chapter to Part mass-bounds.
- mass_bound opening l.11: a pointer.
- Merge or adjust research_program 196–236. History 471–483 is location-neutral.

## 16. continuous_potential_product_measures (DO)
- Move \input chapter_prescribed_equations.tex:208 to after l.280. Both files are \sections.
- Its dependencies are earlier: lem:split-product-normalization, subsec:closed-factor-equations, and lem:bounded-exponential-supersolution (in a proof).
- The only user before the new position is chapter_prescribed_equations:22 (prose).
- Alternative: lem:bounded-exponential-supersolution depends only on thm:singular-strict-domination and could move up instead.

## 17. lem:affine-logarithmic-pole-barrier (DO)
Move section_affine_polar_obstacles.tex 11–17 to section_affine_local_strict_weights before lem:relative-affine-zero-value (l.7). Its dependency lem:affine-projective-growth is earlier, and its only user is l.15.

## 18. lem:nef-blowup-metric (DO)
- It has no external dependencies.
- Move section_nef_order_modifications.tex 8–20 to framework after thm:resolvable-regularization-input (section_psh_analytic_regularization.tex ~l.199, "smooth remainders after resolution"). The appendix would be too late.
- Replace the "We check that β is big" paragraph of lem:big-resolved-equation (big_minimal_existence 22–26) by a citation. finite_restricted_invariants:9 (the Kähler blowup) can cite it too.

## 19. lem:psh-harmonic-slice-persistence (DON'T)
No dependencies and a single use 55 lines later. It is not misplaced.

## 21. Hopf basic Perron (DO WITH CHANGES)
- Only the Legendre sentence of prop:hopf-basic-model-projection (hopf_basic_perron:293 and the corresponding proof paragraph) needs def:hermitian-envelope-testcurve.
- Split it off as a corollary at the end of chapter_testcurves' first section. Moving the whole 306-line section also works, since it has no users before.

## Other admissible fixes (not proposed)
- cor:positive-lower-mass-solvability (lower_mass_solvability:77) → chapter_relative_finite_measures after thm:als-general-measure. Its only user is prose (extrema:38).
- cor:elliptic-fivefold-exact-threshold (zero_lower_mass_product:119) → after sec:lower-mass-metric-geometry. Its users are prose.

## Forward references from proofs/statements to later chapters
There are 97 in all; 11 point at chapter_history ("see sec:history-…" in proofs) and are harmless. Grouped by target. "Removed by …" means a proposal above fixes it; anything not marked stays after all proposals.

- **mass_bound_volumes ← igood**, 55 refs, all removed by 15/20/22 together with the gauge-failure lemma:
  - ex:diffuse-polar-zero-model: ordinary_type:159, zero_volume:72/123, diffuse:21
  - cor:curve-model-completeness: zero_volume:168/177, separated:48, weighted:70, curve_fibration:241, gauduchon_polar:52, igood:272
  - prop:curve-arbitrary-background-models: fibration_reduction:176, arbitrary:55/67, curve_fibration:190(statement)/213/237/248/389
  - cor:curve-arbitrary-background-criterion: fibration_reduction:176, separated_all_obstacles:68, general_auxiliary:72, curve_fibration:265
  - prop:curve-analytic-distance-defect and thm:curve-model-capacity-convergence: zero_volume:177/179, separated:48, weighted:70, gauduchon_polar:52
  - lem:curve-polar-model and thm:curve-model-volume-distance: zero_volume:168, separated:78
  - thm:curve-background-homothety: arbitrary:63
  - def:model-volume-comparison: zero_volume:155(statement), gauduchon_polar:190, diffuse:350
  - thm:positive-model-complete-metric: gauduchon_polar:144(statement), igood:272
  - thm:ordinary-envelope-volumes: diffuse:244/282/320/397
  - thm:small-pole-envelope-residual: diffuse:284/327(statement)/348/397
  - prop:model-volume-separation, eq:volume-comparison-basic, prop:volume-addition: diffuse:244/282/291/299/403
  - sec:model-background-comparison and sec:two-sided-model-backgrounds: igood:272
- **trace_data ← igood**, removed by 22: lem:curve-atomic-ideal-model (zero_volume:177, separated_obstacles:40) and prop:curve-product-extended-ma (fibration_reduction:288).
- **gauduchon_variational_volume ←**
  - thm:gaud-volume-dual-formula and thm:gaud-volume-mass-extrema: lower_mass_solvability:56, density_subsolutions:118, integrable_tests:39, density_stability:97 (removed by 2).
  - thm:vanishing-lower-mass and prop:lower-mass-balanced-metric: zero_lower_mass_product:120(statement)/127 (fixed only by moving that corollary).
  - cor:gaud-adjoint-lq: continuous_hessian_adjoints:62 (stays).
  - cor:lower-mass-dimension: diffuse:250 (removed by 20).
- **mass_bound_volumes ← envelope_systems:** thm:positive-volume-system-recovery (hopf_transverse:79) and countable-divisorial:positive-mass (:138). Removed by 3.
- **bounded_mass_equations, mass_bound, flag_bodies ← normalization:** normalization_mass_quotient:29 cites cor:big-model-lp-type, eq:li-model-condition and lem:kahler-modification-bounded-mass. Only the last is removed (by 6). thm:normalization-mass-quotient is used in a proof at convex_body_reference_stability:125, so it would need restating.
- **relative_finite_measures ←** thm:als-general-measure: lower_mass_solvability:88 (fixed by moving cor:positive-lower-mass-solvability).
- **bott_chern_loci ←** ex:gauduchon-current-smoothing-obstruction: weak_gauduchon_duality:88. Removed by 12.
- **testcurves ←** def:hermitian-envelope-testcurve: hopf_basic_perron:293 (statement). Removed by 21.
- **prescribed_equations ←** thm:big-general-envelope-contact: chapter_envelopes:66, as an alternative ("or"). Stays; harmless.
- **appendix ←** thm:hermitian-space-descent: big_minimal_existence:41 (a genuine dependency on the appendix; stays). Also research_program:356 (problem, stays).

Same-chapter forward references the proposals also fix: determinant_integrability:75 (by 2) and invariant_mass:27/123 (by 4).
