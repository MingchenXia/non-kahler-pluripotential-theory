# p6d report: placement moves 5, 6, 7, 8, 18, 21 and coordination items

Note: the WIP snapshots 9d04675 and 666ef1e already contain my edits, so the diffs below are against 099fd4b.

## 1. Moves made (each checked with a private copy of lg.py/q.py)
- **hessian:bounded-nonvanishing** (§5): moved from the end of section_hessian_bounded_locality to just after the proof of hessian:strict-bounded-domination (section_hessian_mass_comparison). Dropped "whose proof does not use the present proposition". Its only dependency is the theorem directly above it. The only user is history:371 (prose). The chapter opening already says "strict domination, hence nonvanishing".
- **lem:kahler-modification-bounded-mass + the Moishezon paragraph** (§6): moved from chapter_flag_bodies to chapter_products, after the proof of prop:bmp-metric. The history pointer now reads `sec:history-products`. "of def:bmp" was dropped (def:bmp is just above). flag_bodies keeps its section with a one-sentence recall. Products opening: added "it holds whenever X has a modification from a compact Kähler manifold, in particular when X is Moishezon". Dependencies: prop:bmp-metric only. All 6 proof users come later; the forward reference normalization_mass_quotient:29 is gone.
- **H^{1,1}_BC definition + lem:bc-one-one-current-description** (§7): moved to section_divisorial_potential_domination, right after the proof of lem:closed-current-global-potential, its only dependency. The section's intro sentence now mentions this. Pointers added:
  - chapter_framework:103 now names H^{1,1}_BC and adds "(lem:bc-one-one-current-description)", a prose forward pointer.
  - section_bott_chern_bclasses has a one-sentence recall; "by the lemma" became "Thus" / an explicit cref.
  - chapter_bott_chern_loci:21 now reads "Recall from sec:psh-divisorial-estimates … and from sec:bc-closed-currents that a class is pseudoeffective". All users are later.
- **Concave sections** (§8): moved the two `\input`s from chapter_weak_equations to the end of chapter_hessian_equations. Opening edits:
  - The weak_equations sentence "The final two sections …" is deleted.
  - The Hessian opening gains a paragraph: these sections do not use m, n≥1 is arbitrary, σ_m^{1/m} on Γ_m is an example, plus a summary.
  - concave_gap l.4: "determinant bounds used above" → "determinant bounds used for the Monge–Ampère equation in chap:weak-equations".
  - concave_gap l.6 now states the standing data: X connected compact of dimension n≥1, ω Hermitian, χ fixed, m plays no role; f, F and "admissible" refer to the concave data, not to σ_m^{1/m} and the cone of sec:hessian-cone.

  Dependencies: thm:gauduchon, thm:tw-smooth, prop:stw-czero-reconstructed, eq:stw-contact-area, thm:lp-potential-estimate, sec:hessian-cone. All are earlier. Users: history only.
- **Legendre corollary** (§21): new **cor:hopf-basic-testcurve-pullback** at the end of the first section of chapter_testcurves. Statement: pullback maps envelope test curves on (Y,κ) with initial ψ (P_κ[ψ]=ψ) to ones on (X,ω) with initial p^*ψ, and commutes with both transforms. The proof is the former proof paragraph, citing the model identity of prop:hopf-basic-model-projection. The sentence and its proof paragraph are removed from the proposition, and the section intro now points to the corollary (prose). The testcurves opening got one sentence. Dependencies are earlier; the forward reference hopf_basic_perron:293 → def:hermitian-envelope-testcurve is gone.
- **lem:nef-blowup-metric** (§18): moved to section_psh_analytic_regularization after the remark following thm:resolvable-regularization-input. A lead-in now defines η_D=Σa_jη_j and σ_D, notes that η_D is closed, and states Poincaré–Lelong; the statement says "a curvature form η_D as above".
  - big_minimal_existence: the bigness paragraph is replaced by a citation (κ=C_0π^*ω−η_F, ζ=C_0^{-1}σ_F, π^*ω+ddcζ=C_0^{-1}(κ+[F]), so β+a ddcζ ≥ aC_0^{-1}κ). The proof now says π is a sequence of blowups with smooth centers.
  - finite_restricted_invariants:9 cites the lemma, with the closed form C_0p^*h_X−η_D.

  The statement covers both uses: smooth hypersurface blowups are isomorphisms and are omitted; the Poincaré–Lelong potential σ_F comes from the metrics; η_D is closed. The lemma has no dependencies; its 3 users come later.
- **section_psh_divisorial_sobolev input** (item 8): moved to the end of sec:analytic-types, after strict_lelong_levels. Dependencies: lem:qpsh-removable-analytic (#371) and sec:psh-compactness (#402), both earlier. Users: history only.
- **lem:continuous-potential-smooth-loss** with its lead-in sentence (item 9): moved to right after prop:bounded-almost-regularization. Users: gauduchon_trace_topology (chapter_compactness, later) and history.
- **𝓜_+(Ω), lem:local-vague-metric and its remark** (item 10): moved to just before thm:local-prescribed-excess, its first proof use. The lemma's proof is now self-contained: the construction of (f_i), the coordinates generating the vague topology, the metric, and density of finite rational atomic measures, which the statement now states explicitly. The theorem's first paragraph and the atomic-approximation justification are replaced by "Let (f_i), d_v be as in lem; density gives ν_j …". The end becomes "Hence d_v(…)≤2/j+2^{-j}, and lem gives the vague limit". There is no circularity: the lemma cites nothing. background_cluster_sets ("(f_i) and d_v as in the lemma, j-th step of the proof") stays consistent.

New lemma (item 7): **lem:polar-cantor-nonatomic-measure**, at the end of sec:local-polar-parts. "Every nonempty open subset of a Riemann surface contains a compact polar set carrying a probability measure without atoms." Proof: a binary Cantor set in [0,1] with r_k=exp(−4^{k+1}) and the coin-tossing measure (mass 2^{-k} per level-k interval); u=∫log|z−y|²dσ ≤ 2^{1−k}log r_k=−2^{k+3} on K. Index: Pluripolar set!Cantor set with a nonatomic measure. No dependencies.

## 2. Moves not made
- Item 11(d): the L² distance subsections stay where they are. They are local multiplier-ideal results; nothing later uses them and they motivate nothing later. No appendix of that kind exists, and moving them would also mean splitting off lem:planar-multiplier-ideal (used by partial_bergman and the appendix) and lem:planar-global-ideal-sum. If an appendix of non-load-bearing material is ever created, these three files fit there; lem:planar-multiplier-ideal is self-contained and could then go into sec:psh-local-ideals after lem:smooth-center-multiplier-ideal.

## 3. Coordination edits
- (a) Verified: thm:hopf-descended-hermitian-ma is lem:hopf-basic-potentials (1),(3) with S a point and (a,b)=(1,1) or (k,0) (X_n=H_n, π=p_n, ζ=β_n, σ=ω_FS by sec:hopf-homogeneous-sections). Every caller gets what it uses:
  - partial_bergman:262/268 use the measure formula and MA_{kα}=0.
  - hopf_point_equilibrium:131 uses the measure formula.
  - hopf_reduction:91 uses the measure formula.

  The theorem is deleted. Its label and `\index{Hopf manifold!descended equation}` now sit on lem:hopf-basic-potentials. chapter_hopf_reduction keeps the π^*ν∧ζ notation, identifies it with β_n∧p_n^*ν, and restates the two consequences in prose with one display. Mass sentence: "so its Hermitian mass is at most 2n"; l.91 now cites "the measure formula above".
- (b) Verified: r5g14 had already removed the first assertion. The proof correctly cites thm:restricted-analytic-envelope-limit, since the envelope T itself must be a competitor, which prop:trace-profile-majorant does not give. Only change: "proves the second assertion" → "proves the assertion".
- (c) Verified: the proof of prop:ruled-pullback-ordinary-volumes is already a one-line citation of prop:singularity-volumes-modification. No change. Its gauge sentence is cited nowhere. The proposition could be deleted by moving its label onto prop:singularity-volumes-modification, which is read-only for me; the only user is l.209 of the same file.

## 4. Replacements needed in files I do not own
- **chapter_history.tex**:
  1. Move the two paragraphs "For fully nonlinear concave equations, the uniform estimate …" and "The gradient estimate in \cref{sec:concave-gradient} is Guo and Song's …" (now l.197, l.199, in sec:history-smooth-equations) to the end of sec:history-hessian-equations (after "…are separate from this argument.", before `\section{Volumes under mass bounds}`).
  2. **Required**, because chapter_products now points to sec:history-products. In sec:history-sections (l.636), delete "The form of Moishezon's theorem used in \cref{chap:flag-bodies} is stated in \cite[Introduction, p.~1332]{Moi67}; it is used as a classical geometric input. A K\"ahler modification also gives the bounded mass conclusion of \cref{lem:kahler-modification-bounded-mass}, by Guedj and Lu's argument pulling back upper volumes \cite[Lemma 3.6]{GL22}." The remaining sentence can join the next paragraph. Add to sec:history-products, after the prop:bmp-metric paragraph: "The form of Moishezon's theorem used in \cref{lem:kahler-modification-bounded-mass} is stated in \cite[Introduction, p.~1332]{Moi67}; it is used as a classical geometric input. The bounded mass conclusion for a K\"ahler modification is Guedj and Lu's argument pulling back upper volumes \cite[Lemma 3.6]{GL22}."
- **preface.tex**: no change needed. "the Hessian chapter examines how these arguments change when positivity is weakened" still fits.
- Optional, cosmetic: in chapter_partial_bergman:262/268 and section_hopf_point_equilibrium:131, `\cref{thm:hopf-descended-hermitian-ma}` could become `\cref{lem:hopf-basic-potentials}(3)`. The label now resolves to the lemma.
- For the agent citing lem:polar-cantor-nonatomic-measure: the statement is exactly the one above. The proof contains the explicit construction (r_k, mass 2^{-k}), so section_diffuse_product_polar_obstruction:21 can refer to "the Cantor set in the proof of lem:polar-cantor-nonatomic-measure".
- Pre-existing, not mine: section_psh_measure_concentration:70 cites thm:local-prescribed-excess (later) inside a proof ("whose proof does not use the proposition"). That is still true, and the theorem's proof now cites only prop:local-one-atom-addition and lem:local-vague-metric.

## 5. Checks
- chapcheck (15 assigned chapters plus chapter_smooth_equations, run twice): nothing from my files; only the ignorable Underfull 1783. Remaining warnings come from concurrent work by others:
  - multiply defined labels of section_primitive_elliptic_bundles (input twice) and prop:gaud-positive-volume-collapse / eq:gaud-collapse-basic;
  - app:cotangent-torsors, undefined in the partial build.

  Without chapter_smooth_equations, the gaud-volume labels moved there show as undefined.
- Label graph: every moved or new block cites only earlier labels in proofs and statements, and no earlier proof or statement cites a moved label. The only forward reference from my files is the pre-existing big_minimal_existence:41 → thm:hermitian-space-descent (appendix). The new prose forward pointers are framework:103, hopf_basic_perron:285 and the Hessian opening.
- mathdiff3 --base 099fd4b over my 32 files: the moves cancel. The net math changes are exactly these coordination and rewrite edits:
  - Hopf theorem → prose recall;
  - bigness paragraph;
  - the Kähler-blowup sentence;
  - η_D/σ_D notation;
  - vague-metric proof;
  - Cantor lemma;
  - the corollary (P_κ[ψ]=ψ);
  - Hessian/concave standing data (n≥1, σ_m^{1/m}, Γ_m, H^{1,1}_BC in pointers).

  New labels: cor:hopf-basic-testcurve-pullback and lem:polar-cantor-nonatomic-measure. No label or index entry was lost.
