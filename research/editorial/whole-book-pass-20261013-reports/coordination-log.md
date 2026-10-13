# Coordination items, whole-book pass (round 6)
## r5g03
- XDUP: prop:bmp-metric (chapter_products) first assertion duplicates prop:smooth-bmp-metric (chapter_mass) once its own second assertion is in place -> r5g04 owns chapter_products (later) -> check r5g04 report; else coordinator.
- XDUP: sec:gauduchon-section-degree (chapter_sections) redefines deg_gamma L and repeats metric-independence; replace by reminder citing sec:convex-bundle-norm-obstruction -> r5g14 owns chapter_sections.
- PLACE: sec:convex-bundle-norm-obstruction + 12 subsections (+ directional curvature, Ricci-flat surface, integrated curvature, first-jet positivity) -> new chapter "Gauduchon degrees and positivity of vector bundles" after chap:gauduchon; Hirzebruch subsections as appendix of it.
- PLACE: subsec:negative-bundle-logarithmic-weights -> end of new chapter or next to section_psh_local_ideals.
- TeX comment "% ... are not certified here" in subsection_fixed_stein_finsler_hypersurface (workflow wording, unprinted) -> coordinator remove.
## r5g08
- END: history l.146 and l.156 replacements (see report r5g08 §7).
- END: section_gauduchon_moment_equations l.52 and section_semipositive_capacity_limit l.11: prop:lower-barrier-criterion -> thm:common-barrier-criterion wording (labels resolve already).
- XDUP: prop:ruled-pullback-ordinary-volumes duplicates prop:singularity-volumes-modification (volume identities) -> owner of ruled file.
- XDUP (low): prop:symmetric-equation-clusters = Hermitian case of prop:big-exponential-clusters + cor:big-exponential-symmetries.
- XDUP/PLACE: bigness step in proof of lem:big-resolved-equation duplicates lem:nef-blowup-metric; move lemma earlier (framework/appendix) and cite from both.
- PLACE: lem:affine-logarithmic-pole-barrier -> section_affine_local_strict_weights (its only user).
## r5g05
- AUDIT PRIORITY: merged rotational heat construction into generalized lem:hopf-small-defect (all heat times) + new lem:hopf-base-correction; thm:stw-volume now for Hermitian gamma (not Gauduchon); rotational weights continuous nonincreasing.
- XDUP: hessian:hessian-cone-stability vs lem:cone-maximal-stability-comparison; Liouville gap/directional cases vs thm:stw-cone-liouville -> sent to r5g07.
- END: history hist:hopf-rotational-damping replacement; history l.178 STW17 Thm 1.4 Gauduchon? (check STW17) -> history sync.
## r5g15
- PLACE: section_hopf_transverse_recovery (ch.25) depends on ch.30 results -> move to chapter_mass_bound_volumes after section_countable_divisorial_positivity.
- PLACE (major): core of variational volume (def:gaud-variational-volume, prop:gaud-volume-elementary, thm:gaud-volume-dual-formula, thm:gaud-volume-mass-extrema) cited by five sections of ch.14 -> move before ch.14 (e.g. after thm:tw-smooth).
- PLACE: sec:invariant-mass-reference-densities uses later sections -> after section_mass_geometry.
- research_program l.170 -> sent to r5g23. semipositive_dual_attainment b>0 -> sent to r5g16.
- END: history l.688, l.684 replacements (report r5g15 §7).
- Overfull 10.46pt in section_warped_endpoint_subtraction 45--47 (other agent) -> check at end.
## r5g07
- AUDIT PRIORITY: deleted hessian:bounded-linear-weighted-convergence and hessian:bounded-two-factor-convergence (labels moved to hessian:joint-decreasing-products); bounded-nonvanishing now from strict-bounded-domination (non-circularity claimed); merged penalty squeeze; smooth-torsion case merge; Liouville via STW with cone property list.
- Hessian chapter intro -> sent to r5g06.
- END: history Sobolev paragraph + nonvanishing sentence (report r5g07 §7).
- PLACE: hessian:bounded-nonvanishing -> after hessian:strict-bounded-domination in section_hessian_mass_comparison (coordinator move).
- PROPOSAL: one Liouville theorem for a class of cones in sec:stw-liouville cited from both (coordinator consider).
## r5g14
- XDUP (coordinator option): thm:hopf-descended-hermitian-ma duplicates lem:hopf-basic-potentials(1),(3); kept statement (cited by partial_bergman, hopf_point_equilibrium) -> coordinator may remove and redirect.
- AUDIT: thm:hopf-projective-exact-trace strengthened (every smooth Omega >= a alpha); prop:original-background-trace-majorant shortened; prop:envelope-system-raw-volume-failure "there is" -> "for every" h.
- PLACE: lem:kahler-modification-bounded-mass -> chapter_products after prop:bmp-metric.
- PLACE (opt): H^{1,1}_BC definition and lem:bc-one-one-current-description -> chapter_framework near Bott--Chern remark (~l.103).
- END: history l.635 replacements; research_program l.265 (optional) -> r5g23 running: send.
## r5g06
- END: git rm author/section_classical_scalar_uniqueness.tex (now a comment, not input).
- END: optional remove alias labels prop:classical-scalar-uniqueness, cor:gauduchon-surface-uniqueness (unreferenced) -- keep (harmless) unless clean-up.
- AUDIT: thm:lp-uniform-compactness now derived from prop:capacity-square-one-sided-stability (reordered input); hypothesis removals in concave sections (n>=2, f in C^0, f=0 on boundary), uni-thm:threshold C^{1,1}.
- PLACE: sec:concave-strict-gap-stability and sec:concave-gradient -> chap:hessian-equations or own chapter.
- symmetric_equation_selection replacement -> sent to r5g09.
## r5g04
- AUDIT: lem:continuous-hermitian-fredholm now via GT01 Thms 9.11, 9.6, 5.2 (check GT01 locators!); ramified root example now on the curve C (no P^{n-1}); integrated Hermitian curvature n>=1; prop:shrinking-intermediate-currents hypotheses dropped.
- END: history l.79, l.126, l.128 replacements (report r5g04 §7).
- PLACE (opt): sec:continuous-hermitian-fredholm -> before thm:continuous-hessian-adjoint-uniqueness (ch. normalization).
## r5g21
- AUDIT PRIORITY: thm:small-pole-envelope-residual lost "positive lower singularity volume"; model-volume moduli hypotheses changed, prop:model-lower-volume-modulus moved and strengthened; background-change standing setting Omega>=theta+h; cor:mass-bound-exact-trace hypothesis Omega>=2theta|_Y.
- XDUP (later owner r5g22): cor:relative-extended-exponential-order vs cor:big-relative-orders; thm:relative-extended-domination vs thm:big-relative-domination (different regimes; later may cite).
- END: history l.449 replacement.
## r5g17
- AUDIT PRIORITY: prop:nef-maximum-rank-comparison merged into lem:nef-logarithmic-rank-comparison (label moved; lemma narrowed to pointwise cB<=theta, singular-potential lower bound dropped -- check no user needs it); fixed-cone proofs now apply lemma; zero-ruling ring proof cites thm:elliptic-extension-polynomial-ring with P=h^2; U non-splitting from s=1; ruled residual via thm:gaud-volume-dual-formula + prop:gaud-volume-first-variation; flat-divisor results generalized to dim n (V=n eps^{n-1}int_D kappa^{n-1}+eps^n int kappa^n).
- END: history l.722 replacement (report r5g17 §7); l.724 cref optional.
- PLACE: cotangent-torsor subsections (subsec:elliptic-affine-quotients .. end of section_nef_flat_divisor_complements, ~650 lines) -> appendix chapter or own section; optionally subsec:flat-divisor-complements with them.
## r5g09
- AUDIT: lem:numa-radial-flux extended to lambda>=0; prop:fixed-spherical-reference carries bound; thm:smooth-boundary-trace-regularity drops closedness/local potentials/barrier/minimal sing (new proof via lem:ball-smooth-dirichlet + lem:big-local-comparison -- check lem:big-local-comparison proof local & no closedness!); semipositive-degeneration rho analytic-sing -> Z closed, rho smooth off Z; thm:nonclosed-interior-smoothness c absorbed.
- END: section_big_minimal_comparison lem:big-local-comparison hypothesis B⋐Omega -> B⊂X any smooth theta (owner r5g08 done; coordinator, verify proof), then delete r5g09's clause in local_density_boundary.
- END: research_program l.75 replacement (r5g23 running -> send); history l.806, l.808 replacements.
- END: section_numa_radial prop:numa-radial-continuum "If the cutoff kappa ... is chosen even" -> kappa is even now (r5g06 file, done).
- END (opt): lem:bounded-reference-trace: state C_psi depends only on ||psi||_inf and fixed data.
- XDUP (minor): last sentence of thm:gaud-volume-nef-limit restates thm:semipositive-smooth-degeneration monotonicity -> optional cite.
- PLACE: last assertion of prop:greatest-normalized-threshold (cluster limits in S_f) -> separate corollary after cor:individual-positive-threshold-exponential (section_individual_exponential_equations, r5g10).
## r5g19
- AUDIT: prop:finite-map-zero lost hypothesis "F^*[omega_Y] contains Kahler form" (now via prop:restricted-mass-bigness + Collins-Tosatti recalled in sec:history-closed-loci + thm:bc-non-kahler-locus -- CHECK: citing history section as math support? and CT needs Kahler X); prop:exceptional-density-obstruction smooth only; anisotropic q>=1; def alpha[-eps omega] no psef.
- PLACE: ex:gauduchon-current-smoothing-obstruction (section_threshold_divisorial_geometry l.1-22) cited earlier -> after l.83 of section_gauduchon_linear_duality; m_omega/kappa_omega paragraph -> section_smooth_cone_duality after m_h<=kappa_h.
## r5g18
- AUDIT PRIORITY: thm:crossing-fiber-integrability-band merged with thm:fiber-integrability-band (both labels on one); cor:semipositive-fiber-band deleted (label on thm:fiber-integrability-band) -> resolves multiply-defined; new prop:descended-kernel-limit; lem:finite-family-section-bound generalized; beta>0 -> beta>=0 with int beta^q>0; hopf_point rationality of a only for envelope identities; birational partial envelopes theta not closed (MA^ext).
- XDUP (opt): eq:fs-monomial-beta-norm (section_ideal_rounding_kernel_limits, r5g19 done) = q=1 case of eq:projective-monomial-norm -> optional cite.
- END: research_program l.332, 334, 336 (r5g23 running -> send); history l.654/658 merge sentences.
## r5g16
- AUDIT: thm:warped-endpoint-subtraction/thm:radial-positive-volume-nonbig cite thm:warped-gauduchon-volume; thm:rank-two-dual-smooth-extension uses u_0; lem:determinant-background-transport first paragraph removed; prop:local-mass-extremum-necessary n>=3 -> n>=2; lem:nef-uniform-pairing semipositive Psi; prop:closed-core-differential-cost normalization kappa_0^2.
- Overfull in warped section fixed by r5g16.
- XDUP/PLACE: section_primitive_elliptic_bundles (later, general) re-proves prop:lower-mass-balanced-metric, prop:elliptic-radial-mass, prop:lower-mass-no-pluriclosed (case B=P1xP1) -> proposal: general results move to sec:lower-mass-metric-geometry, earlier props become corollaries; or later cites.
- PLACE: corollary "h>=cg => v_-(h)>=c^n v_-(g), sup||k_T||<=..." after thm:gaud-determinant-endpoint (section_gauduchon_determinant_integrability), cited by lem:determinant-background-transport and cor:geometric-determinant-bound.
## r5g11
- AUDIT: lem:divisorial-adjoint-model now FORWARD-cites prop:logarithmic-product-model (check no circularity; "nonconstant b" moved out of standing hyp of sec:logarithmic-model-selection); prop:divisorial-residual-adjoint cites thm:ordinary-divisor-normalization + prop:normalization-directional; eq:divisorial-cutoff-bound label moved to capacity display; prop:normalization-dual-entropy "theta Kahler" -> "X Kahler, theta closed"; dV(X)=1 removed in entropy bounds; thm:divisorial-type-thresholds max principle -> GT01 Thm 3.5; sup bound via thm:normalized-compactness.
- XDUP: qu:i-good-no-bmp (chapter_igood) ~ qu:singularity-topology-program (research program) -> proposal delete qu:i-good-no-bmp, move label (coordinator).
- PLACE: chapter_igood "Complete model topologies" overview + qu -> research program next to qu:singularity-topology-program.
- END: history l.555, l.569, l.575 replacements (report r5g11 §7).
## r5g20
- AUDIT: lem:four-point-conic-degeneration deleted (label -> lem:four-point-variable-conics a=2); thm:four-point-semipositive-metric-nonextension now from cor:four-point-least-singular-extendable (file reordered); min-Lee examples now on H_n of sec:hopf-all-dimensions (scaling e^{-2}, Lee period 2); ex:lee-calabi-eckmann generalized to all X_tau with A<0<B_0 citing prop:calabi-eckmann-endpoint; cor:divisorial-exponential-completeness hypotheses removed (u smooth on M, q,a,b real); torus 0<=r<=n; thm:lck-vaisman-volume any invariant mu.
- END: history l.759 replacement (report r5g20 §7).
- OPT: lem:four-point-family-adjoint-vanishing conclusions unused (keep).
- PLACE (low): lem:psh-harmonic-slice-persistence -> framework psh sections.
## r5g10
- AUDIT PRIORITY: lem:split-product-normalization rebuilt (arbitrary closed Kahler factor (Y,kappa), 3 parts; b_H(Rg)=CV_0/M_g for g in L^1, c_H for bounded g; scalar via thm:kn-continuous + Stokes); new lem:bounded-exponential-supersolution (from thm:singular-strict-domination) replacing 3 arguments incl. greatestness in thm:continuous-potential-product-threshold; v_-(h_0)=0 and k>=2 removed in radial sections (k=1 checks); thm:power-capacity-critical-equation Step 3 via continuity of bounded products under capacity convergence; thm:logarithmic-critical-density b_h(f)=1 from remark after lem:bounded-normalizer-subsolution; thm:continuous-potential-curve-exponential normalization now consequence.
- XDUP: section_logarithmic_model_selection (r5g11 done) redefines chordal distance and G=log dist^2+1 -> replace by reminder + cref to defs before eq:curve-measure-green-potential, lem:curve-probability-green-potential (coordinator).
- END: chapter_prescribed_equations.tex l.22 "on products with a projective space of dimension at least two," -> "on products with a projective space,"; research_program l.93 (-> r5g23); history l.557, l.578, l.186 (report r5g10 §7).
- PLACE: \input section_continuous_potential_product_measures after section_individual_exponential_equations (forward ref to lem:bounded-exponential-supersolution).
## r5g13
- AUDIT PRIORITY: new lem:diffuse-cutoff-polar-blindness (5 copies merged); prop:diffuse-hermitian-mass-polynomial merged into prop:diffuse-representative-mass (both labels; new eq:diffuse-residual-local); prop:all-modifications-diffuse-polar-blindness label -> prop:diffuse-two-mass-model-obstruction; cor:diffuse-product-exact-volume label -> cor:diffuse-mass-invariant-models; prop:small-curvature-intrinsic-traces SNC removed (ideal sandwich via lem:smooth-center-multiplier-ideal + factoriality); Hopf section and chapter_rays intro n>=3 -> n>=2; prop:closed-pole-compatible-limits weakened hyp; family R no identity.
- XDUP: Step 2 of thm:small-pole-envelope-residual (later, r5g21 done) duplicates first part of prop:diffuse-representative-mass -> if igood block moved after it, state Step 2 as lemma (coordinator).
- XDUP: first assertion of prop:original-background-trace-majorant (chapter_divisorial_models, r5g14 done) duplicates prop:trace-profile-majorant -> later should cite (coordinator).
- PLACE: chapter_igood "Complete model topologies" subsection (~l.232-277, inputs polar-current + Gauduchon + diffuse subsubsections) -> end of chapter_mass_bound_volumes after section_joint_curve_model_spaces (depends on that chapter throughout). [conflicts/combines with r5g11 proposal]
- PLACE (opt): sec:hopf-basic-models uses def:hermitian-envelope-testcurve (next chapter) -> end of chapter_testcurves.
- END: research_program l.120, l.230, l.232 (-> r5g23); history l.54, l.471, l.630.
## r5g01 (base cae12da)
- AUDIT PRIORITY: thm:zero-local-cluster-sets deleted (label -> thm:bounded-background-cluster-sets, b=0); prop:smooth-dirac-concentration forward one-line proof from thm:local-prescribed-excess; lem:weighted-decreasing-products via GZ17 Thm 3.18 (T=1, dd^c twice); lem:psh-liouville via GZ17 Lemma 2.28; b locally bounded in local prescribed excess results (u_j-b bounded); Hausdorff dim 0 -> H^1(S)=0 in thm:small-pole-local-products, lem:small-pole-residual-invariance (DemCADG needs H^{2n-2m+1}=0); lem:bounded-reference-trace theta>=0 dropped; eq:global-capacity-tail t>0; added "connected" in lem:local-holder-exponential-tails.
- XDUP: lem:continuous-potential-smooth-loss (section_psh_chern_regularization, r5g02 running) duplicates prop:bounded-almost-regularization + Dini -> send r5g02.
- XDUP: prop:gauge unreferenced; restated at chapter_mass_bound_volumes.tex:1221 and section_ordinary_type_topology.tex:117 -> could cite (coordinator / r5g22?).
- END: history l.823, l.43, l.41 (Qin hypotheses check!), l.29.
- END (from r5g09): lem:bounded-reference-trace: C_psi depends only on ||psi||_inf and fixed data.
- PLACE: lem:local-vague-metric (+ def M_+(Omega), remark) before thm:local-prescribed-excess; \input section_psh_divisorial_sobolev -> end of sec:analytic-types after section_psh_strict_lelong_levels.
## r5g12
- AUDIT PRIORITY: lem:separated-curve-model-projections deleted (label -> prop:separated-curve-obstacle-projections); cor:nonclosed-product-polar-metric + cor:degenerate-product-polar-metric deleted (labels -> cor:nonclosed-separated-product-metric, m>=1); cor:auxiliary-product-all-obstacle-criterion label -> cor:general-auxiliary-all-obstacle-criterion; new lem:auxiliary-slice-envelopes (8 copies); new eq:fibration-zero-obstacle-bounds; prop:ordinary-topology-gauge-failure mass one dropped (scaling); m>=2 -> m>=1 several-curve setup; fibration reduction H empty allowed; prop:divisorial-product-obstacles continuous F; thm:all-obstacle-analytic-closure via prop:ordered-ideal-envelope-convergence eps_j=0; cor:fibration-obstacle-equality new decreasing-compact-sets argument.
- END: research_program two passages (report r5g12 §7) -> r5g23.
- PLACE: (a) prop:finite-cover-envelope-transport -> subsec:fibration-obstacle-reduction before cor:fibration-component-cover; (b) polar-metric material subsec:zero-volume-product-obstacles .. subsec:hopf-surface-fibration depends on chap:mass-bound-volumes -> after sec:curve-model-backgrounds; (c) finite-curve:envelope-pullback, finite-curve:model-retraction, finite-curve:averaging-not-nearest -> sec:curve-model-backgrounds.
- PROPOSAL: prop:curve-arbitrary-background-models could state for arbitrary sigma the convex ideal subspace etc.
- prop:gauge note sent to r5g12 (resumed).
## r5g02 (base cae12da)
- AUDIT PRIORITY: Skoda re-proofs in lem:zero-lelong-ideal-neutrality and lem:planar-multiplier-ideal replaced by DemAM11 Lemma 5.6 (check locator and normalization e^{-u}); lem:bergman-divisorial-error remark: properness unused (holomorphic map same dim injective off analytic subset); lem:continuous-potential-smooth-loss proof = prop:bounded-almost-regularization + Dini; lem:smooth-holder-reference-approximation now contains the Chern-average curvature-loss argument; sec:psh-birational-ideals "connected compact" dropped (any modification); prop:psh-descent-modification, prop:polar-curvature-pushforward compactness dropped; prop:singular-no-uniform-limit u_lambda ~ phi -> u_lambda ⪯ phi; A_theta definition non-pluripolar dropped; lem:compact-obstacle-upper-bound w bounded above; lem:big-pointwise-competitor f bounded below; cor:dini-distance-rates power case removed.
- XDUP: section_big_minimal_moments.tex l.9-13 redisplays the definition of A_theta(nu) -> owner replace by reminder.
- END: history ~l.615 and l.21 replacements (report r5g02 §7).
- PLACE: L^2 distance subsections (subsec:psh-quantitative-ideals, subsec:psh-planar-ideal-distance, subsec:psh-hyperplane-ideal-distance) used only by history -> chapter_sections or appendix (keep lem:planar-multiplier-ideal); lem:closed-current-global-potential after prop:local-correction (opt); lem:continuous-potential-smooth-loss right after prop:bounded-almost-regularization.
# AUDITS
## a5g (r5g17 CORRECT; r5g19 CORRECT AFTER FIXES)
- fixed: new label sec:bc-null-loci (chapter_bott_chern_loci), prop:finite-map-zero proof now cites it instead of sec:history-closed-loci.
- END opt: history sec:history-closed-loci CT15Loci sentence could name prop:finite-map-zero. history l.722 replacement endorsed.
## r5g22
- AUDIT PRIORITY: lem:big-concave-envelope + lem:big-model-concave-envelope merged (general, at section_big_minimal_moments; both labels); many proofs now "cite the proof of" with replacements (thm:big-relative-fixed-continuity, lem:big-weighted-common-bound, thm:general-measure-minimal holds the truncated-density and zero-exponent arguments once; thm:als-general-measure Step 4; thm:big-model-normalized; thm:big-unrestricted-addition; thm:relative-extended-domination via thm:big-relative-domination; thm:relative-finite-domination via thm:big-relative-domination (ch.30, r5g21 file audited by a5e -> recheck if a5e changes it); cor:relative-extended-exponential-order); hypotheses: u_j in E_phi -> PSH; lem:big-truncated-addition-limit masses bound via prop:bmp-finite; toric D not effective; thm:cone-bounded-equation = logarithmic data a=0.
- PROPOSAL: common domination lemma in chapter_envelopes after thm:relative-uniform-mass-lower (optional).
- PLACE: paragraph "standing assumptions also give v_-(omega)>0" in chapter_bounded_mass_equations unused -> after cor:metric-pvp-minimal-volume or delete; lem:big-weighted-common-bound -> section_big_relative_energy before thm:big-relative-self-measure-convergence; toric subsection before quotient example (quotient lemma = toric case).
## r5g23
- AUDIT PRIORITY: thm:unibranch-torus-curve-equation, thm:unibranch-curve-density-endpoint, thm:nonclosed-cuspidal-downstairs: descent via thm:hermitian-space-descent, resolution independence via thm:space-extended-measures, density primitive via eq:curve-log-primitive + proof of thm:curve-products (C_0 -> pi C_0/V); "c'>0" dropped (mass comparison); cuspidal s>=n+3 -> s>n (Sobolev algebra/embedding H^{s+2} in C^2 need sum (1+|m|^2)^{-s}<inf); lem:cuspidal-bounded-mass second proof deleted, variant use via k-version on u'∘pi - v_0; prop:cuspidal-nonclosed-repair rigor fix (A with critical point where ddbar A≠0, B nonconstant); prob:growing-jets-localization replaced by summary (label on subsection heading); research programme replacements from r5g09/10/12/13/14/15/18 applied (l.334 handled differently).
- END: history l.819 "descent through disks" -> "descent through the normalization".
- PLACE: section_primitive_elliptic_bundles results -> main text after sec:lower-mass-metric-geometry; prop:gaud-positive-volume-collapse (+A_theta, A_h, eq:gaud-collapse-basic) -> chapter_gauduchon_variational_volume after cor:gaud-volume-big-positive (cited from main text section_radial_gauduchon_test_limits); lem:balanced-pluriclosed-closed -> chapter_gauduchon after def:balanced-pluriclosed.
## a5h (r5g18 CORRECT; r5g20 CORRECT)
- END: cor:horizontal-center-kernel-limit (section_horizontal_center_constraints l.111): drop "Assume that $B$ is K\"ahler." (alpha closed >0 => B Kahler), proof prefix "Since $\alpha$ is a K\"ahler form, $B$ is K\"ahler.".
- END: history l.654/658 exact replacements (a5h report item 2); l.759 r5g20 replacement endorsed.
## a5e (r5g11 CORRECT; r5g21 CORRECT)
- END: history l.555, l.569, l.575, l.449 confirmed.
- CHECK: countable-divisorial:positive-mass step now rests only on external DX22 valuative characterization (history) after deleting internal route via thm:local-i-inputs + surface blowup factorization -> consider restoring internal route (self-contained).
## a5i (r5g10 CORRECT AFTER FIXES)
- fixed: section_logarithmic_critical_density l.69 cited deleted remark -> direct argument via thm:singular-strict-domination; punctuation in power-capacity display.
- OPT: lem:bounded-exponential-supersolution = special case of cor:singular-exponential-order (proof one line; cite corollary directly in section_continuous_potential_product_measures l.236 to remove forward ref).
- END: chapter_prescribed_equations l.22; history l.581 "It assumes zero lower mass of the factor and makes no assertion" -> "Only its last assertion assumes zero lower mass of the factor, and it makes no assertion"; research_program l.41 "bounded comparison extends greatestness" -> "singular strict domination extends greatestness"; subsection title "Products with a zero-lower-mass factor" -> "Products with a Hermitian factor" (section_radial_residual_regularity).
## a5f (r5g15 CORRECT; r5g16 CORRECT)
- OPT P1: section_warped_endpoint_subtraction l.7 m>=2 -> m>=1; l.123 "For example, take $B=\mathbb P^m$," -> "For example, take $m\geq2$, $B=\mathbb P^m$," (a5f checked all results for m=1).
- OPT P2: research_program l.59 "Let $f$ be a nonzero density with $b_h(f)>0$. If" -> "Let $f$ be a nonzero density. If".
- END: history l.684, l.688 (r5g15) confirmed.
## a5d (r5g08 CORRECT; r5g09 CORRECT AFTER FIXES)
- fixed: lem:big-local-comparison now "theta may be any smooth real (1,1)-form", B⊂X; local_density_boundary clause simplified.
- END: history l.146, l.156, l.806, l.808 confirmed; gauduchon_moment l.46 + semipositive_capacity_limit l.11 wording -> thm:common-barrier-criterion.
## a5a (r5g03 CORRECT AFTER FIXES; r5g04 CORRECT)
- fixed: subsection_fixed_stein_finsler_hypersurface l.7 restored "of dimension n>=1" (chap:gauduchon assumes n>=2 by default).
- END: history l.79 keep "interior L^p estimates" (GT01 9.11 interior, 9.6 strong max principle W^{2,n}_loc, 5.2 method of continuity).
- OPT: section_hopf_sections l.58 wording "In the notation of \cref{subsec:flat-restriction-hopf-complements}, ..."; delete 4 TeX comment lines at end of subsection_fixed_stein_finsler_hypersurface (preprint locator + "not certified here").
## a5b (r5g05 CORRECT; r5g14 CORRECT AFTER FIXES)
- fixed: prop:ruled-intrinsic-ideal-orders ideal equality via lem:smooth-center-multiplier-ideal codim one; chapter_divisorial_models dangling "that corollary"; chapter_sections section degree n=1 gamma^0=1.
- END: history l.178 STW17 Thm 1.4 assumes Gauduchon alpha -> add "The proof given here does not use that the auxiliary form gamma is Gauduchon."; l.59 and l.635 replacements endorsed (l.635 may add lem:smooth-center-multiplier-ideal).
## a5j (r5g13 CORRECT AFTER FIXES)
- fixed: prop:equal-residual-anisotropic-models restored v_-=v_+=A (BMP needed by ch.30 results); fixed constant C after lem:diffuse-cutoff-polar-blindness.
- END: history l.631 "The normal crossing ideal formula" -> "The ideal bounds" (h5 has it).
## a5c (r5g06 CORRECT AFTER FIXES; r5g07 CORRECT)
- fixed: section_modified_comparison l.92 punctuation.
- END: history l.311, 320-323, 374-376 (r5g07 §7) (h5 has it); git rm section_classical_scalar_uniqueness.tex.
## a5k (r5g01 CORRECT AFTER FIXES)
- fixed: lem:bounded-reference-trace constant depends only on bound for ||psi||_inf (statement + proof).
- END: section_holder_reference_equation l.38 "The trace bound in \cref{lem:bounded-reference-trace} is uniform for references with a fixed supremum norm, as its proof shows." -> "By \cref{lem:bounded-reference-trace}, the trace bound is uniform for references with a common bound on their supremum norms."
- END: history l.41 Qin Theorem B hypotheses unchecked.
## a5m (r5g02 CORRECT AFTER FIXES)
- fixed: section_psh_local_ideals last paragraph scope (connected compact source); "proper" -> "nowhere dense analytic subset" in divisorial_estimates remark and psh_descent.
- END: history l.21 and l.615-618 replacements (a5m report) -> h5.
## a5l (r5g12 CORRECT)
- OPT: section_ordinary_type_topology l.44 wording; countable_pole_obstacles l.86 note.
## a5o (r5g23 CORRECT) - applied research_program l.41, l.59.
- END: history l.819 "descent through disks" -> "descent through the normalization".
## a5n (r5g22 CORRECT AFTER FIXES)
- fixed: thm:relative-finite-domination "for all such b".
- END: history l.817 toric "effective rational boundary" wording.
- OPT: cor:metric-pvp-minimal-volume "Assume only the bounded mass property and v_-(omega)>0." (with placement of v_-(omega)>0 paragraph).
# PLACEMENT PHASE: stubs created (chapter_bundle_positivity, chapter_polar_model_topologies, appendix_cotangent_torsors) + book.tex includes; git rm section_classical_scalar_uniqueness.tex done.
## p6f done: v_-(omega)>0 paragraph -> after cor:metric-pvp-minimal-volume ("Assume only BMP and v_->0"); lem:big-weighted-common-bound -> section_big_relative_energy (proof written out; theorem now applies it with h=p_1); cor:positive-lower-mass-solvability -> chapter_relative_finite_measures after thm:als-general-measure. Toric reorder not done (no gain).
- forwarded: chapter_prescribed_equations opening -> p6e; extrema l.38 -> p6b. OPT history l.526.
## h5 done: history synchronized (+67/-71). Unsettled: l.817 Seo effective (safe wording), l.186 Nguyen16 Prop 1.1, l.197 GS26 hypotheses (concave sections now more general).
## p6a done: chapter_bundle_positivity filled (6 inputs + negative bundles last); Fredholm -> chapter_normalization subsection; lem:balanced-pluriclosed-closed -> chapter_gauduchon; comments removed; hopf_sections l.58.
- H6: new history section sec:history-bundle-positivity (p6a report §4 exact paragraphs); Fredholm paragraph -> sec:history-normalization; then subsection_homogeneous_convex_regularization l.8 -> sec:history-bundle-positivity.
- PREFACE: l.81 append sentence on chap:gauduchon-bundle-positivity.
## p6e done: new cor:exponential-cluster-threshold-subsolutions; ex:gauduchon-current-smoothing-obstruction -> end of section_gauduchon_linear_duality; m/kappa paragraph -> smooth_cone_duality; lem:bounded-exponential-supersolution via cor:singular-exponential-order; affine barrier moved; all coordination edits a-h applied + prescribed opening.
- DONE by coordinator: threshold_divisorial_constraints l.38 cref.
- H6: history l.574 "follow from singular strict domination through lem:bounded-exponential-supersolution" -> "follow from the singular exponential order of cor:singular-exponential-order".
- OPT: chapter_gauduchon opening sentence on blowup example (p6a done, file free) ; research_program l.63 cref.
## p6d done: hessian nonvanishing moved; lem:kahler-modification-bounded-mass -> chapter_products; H^{1,1}_BC -> divisorial_potential_domination; concave sections -> end of Hessian chapter; new cor:hopf-basic-testcurve-pullback in testcurves; lem:nef-blowup-metric -> framework; divisorial Sobolev input moved; lem:continuous-potential-smooth-loss moved; lem:local-vague-metric moved (self-contained proof); new lem:polar-cantor-nonatomic-measure; thm:hopf-descended-hermitian-ma deleted (label -> lem:hopf-basic-potentials).
- H6: history l.197, l.199 concave paragraphs -> end of sec:history-hessian-equations; Moishezon/GL22 sentences from sec:history-sections (l.636) -> sec:history-products (REQUIRED; exact text in p6d §4).
- OPT: partial_bergman:262/268, hopf_point_equilibrium:131 cref -> lem:hopf-basic-potentials(3).
- NOTE: section_psh_measure_concentration:70 cites thm:local-prescribed-excess forward in a proof (pre-existing, not circular).
## p6b done: new section_gauduchon_quotients in chapter_smooth_equations (core); invariant masses after mass_geometry; primitive elliptic bundles -> main text (3 props now corollaries); prop:gaud-positive-volume-collapse -> new sec:gaud-volume-bigness-threshold; new cor:gaud-determinant-background-comparison (lem:determinant-background-transport label moved); cotangent torsors -> appendix; fivefold cor -> end of lower-mass geometry. Forward refs 116 -> 41 book-wide.
- END: determinant_concentration proof of cor:geometric-determinant-bound replacement (p6b §4).
- H6: history l.676 replacement; l.680 opt split; l.724-728 -> new last section sec:history-cotangent-torsors; l.710 opt.
- PREFACE: l.83 two appendices; l.61 opt.
- OPT: conventions l.43 row order.
- PLACE (new): thm:parallel-torsion-kahler, thm:pluriclosed-deformation-persistence -> chapter_gauduchon section "Balanced and pluriclosed metrics".
## p6c done: chapter_polar_model_topologies filled; finite-curve props -> mass_bound sec:curve-model-backgrounds; Hopf recovery -> mass_bound; qu:i-good-no-bmp label -> qu:singularity-topology-program; new lem:small-pole-full-measures; countable-divisorial internal route restored; prop:gauge reminder; Cantor lemma cited.
- END: section_curve_ordinary_topology:65 -> lem:polar-cantor-nonatomic-measure.
- H6: history l.439 replacement; l.467 Cantor cref; 467-471 -> new subsection "Zero-volume models and polar currents" of sec:history-volumes; opt l.432 sentence; l.600 move after l.439 + wording.
- PREFACE l.83: Part mass-bounds sentence with chap:polar-model-topologies.
- NOTE: chapcheck misses wrapped "undefined" warnings; multiply-defined in partial builds are artifacts of baseline aux (source has no duplicate labels).
## p6g done: new sec:balanced-pluriclosed-metrics in chapter_gauduchon (parallel torsion + pluriclosed deformations subsections); research programme keeps problems with lead-ins.
- H6: history l.840 (Chen-Zheng) and l.846 (pluriclosed persistence) -> sec:history-gauduchon after horizontal descent paragraph; delete \enlargethispage l.844; opt l.838 pointer.
## b6b (p6b CORRECT AFTER FIXES; p6e CORRECT AFTER FIXES): fixes: variational opening u_theta; quotients "semipositive nonclosed"; affine lead-in cref; mass_geometry opening sentence.
- remaining same-chapter forward refs (not circular): iwasawa statement->own proof eq; continuous_hessian_adjoints:62 -> cor:gaud-adjoint-lq (later chapter!); divisorial_adjoint_obstruction:34 -> prop:logarithmic-product-model; warped_completion:180 -> thm:gaud-volume-nef-limit.
## b6c (p6c CORRECT AFTER FIXES; p6f CORRECT): fixes: polar section fixes X; finite_curve "this section" wording; hopf_transverse recovery recall of S_{a,c}, E, R; cor:positive-lower-mass-solvability density wording.
- history l.439, 467, 600 with h6.
## h6 done: history reorganized in chapter order (new sec:history-bundle-positivity, sec:history-cotangent-torsors, sec:history-bounded-mass-equations; envelopes and volumes sections moved; subsection zero-volume models).
- DONE: homogeneous_convex_regularization l.8 -> sec:history-bundle-positivity.
