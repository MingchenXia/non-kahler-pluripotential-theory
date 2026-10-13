# b6b audit report: p6b and p6e (round 6 placement)

## Verdicts
- **p6b: CORRECT AFTER FIXES.** Two small wording fixes; no mathematical problems.
- **p6e: CORRECT AFTER FIXES.** One ambiguous lead-in fixed; no mathematical problems.

## What I checked
- **mathdiff3** against 099fd4b on all 42 files: the p6b and p6e lists, plus section_gauduchon_quotients, section_threshold_divisorial_constraints and section_gauduchon_determinant_concentration (appendix_cotangent_torsors is on the p6b list).
  - Totalled over the files, no label or `\index` entry is lost.
  - The only labels added are the five new ones: cor:exponential-cluster-threshold-subsolutions, cor:gaud-determinant-background-comparison, sec:gaud-volume-bigness-threshold, sec:lower-mass-quotient and sec:primitive-elliptic-lower-mass.
  - The residual math changes are the listed edits.
  - Word-diffs of the old core and the old cotangent block against their new homes show only the reported wording changes.
- **Label graph.** I rebuilt the current and baseline graphs privately and checked forward references from proofs and statements in my 42 files, both outgoing and incoming. Every forward reference the moves removed is gone, and the moves added none.
- **Compile check.** chapcheck b6b on the 9 chapters, run twice before and twice after my edits.
  - No errors and no overfull boxes. The only other box warning is the known Underfull (badness 1783).
  - With wrapped lines joined, the undefined references are all labels in chapters not compiled here, or labels p6g is moving: cor:positive-lower-mass-solvability, ex:gauduchon-current-smoothing-obstruction, lem:nef-blowup-metric, lem:balanced-pluriclosed-closed, thm:parallel-torsion-kahler and thm:pluriclosed-deformation-persistence.
  - The multiply-defined warnings (the continuous-hermitian-fredholm labels and qu:i-good-no-bmp) come from the stale baseline aux. The source has no duplicate labels.

### p6b
- **§2 core (section_gauduchon_quotients).** All symbols and assumptions are available at the new place:
  - pseudoeffective is defined there; thm:lamari, def:gauduchon-metric and thm:gauduchon are in chapter_gauduchon; bigness is in sec:obstacle-envelopes (framework).
  - 𝒫, D_μ, μ, Ω_θ and c_θ(μ) are defined in the section. c_θ(μ)=e^b in the notation of eq:smooth-ma is correct.
  - thm:tw-smooth and the continuity method come earlier; thm:bounded-exact-regularization is in framework; def:bmp, v_± and ex:torus-mass are earlier.
  - b_ω(f) appears only in a prose pointer.
  - "Smooth semipositive" is correct: thm:radial-positive-volume-nonbig says "smooth, semipositive, nef and nonclosed".
  - The smooth_equations opening is accurate: e^{b/n}=λ_μ.
  - The variational chapter's opening recalls what later sections use, except u_θ (fixed below). 𝓜 is recalled wherever it is used.
  - sec:lower-mass-quotient states arbitrary X and a Hermitian ω, and recalls 𝓜.
- **§13 primitive bundles.** I checked the identification of the threefold with the primitive elliptic bundle of O(1)⊠O(−1):
  - the fiber is Hom(ℂz,ℂw); t is the log of the squared norm; g acts as multiplication by q=e^{2π};
  - c=β_B−α_B is primitive, c²=−2α_B∧β_B, T=2log q=4π, A=2, κ=1, eigenvalues ±1 so M_0=1.

  All three corollaries are unchanged and follow:
  - 3TA=24π, and −3·2∫du∧d^cu∧α∧β gives eq:lower-mass-vertical-energy;
  - F(1,4π)=1−1/(3π) since T≥2M, so 24π·(1/(3π))=8, and 3TA(1−(κ/T)∫p²)=6(L−∫p²);
  - c_1=α_B−β_B≠0.
- **§14.** cor:gaud-determinant-background-comparison is correct: h≥cg gives each quotient ≥c times, so v_-(h)^{1/n}≥c·v_-(g)^{1/n}, and the sup bound follows from thm:gaud-determinant-endpoint. n≥2 and dV are standing assumptions there. All callers get what they use:
  - thm:elliptic-curvature-endpoint (n=3, v_-(g)=V);
  - cor:lower-mass-dimension (applied to h_0≥A^{-1}h);
  - cor:both-mass-properties-fail;
  - the proof of cor:geometric-determinant-bound (the coordinator's edit), including the equality case.
- **Item 4.** The bigness-threshold section states its own X, h and μ. The research-programme remnant is accurate.
- **Other moves.** I also checked the cotangent appendix (23 labels; only users are a pointer and history; the opening's claims match the results), the invariant subsection and cor:elliptic-fivefold-exact-threshold (b_H=10·24π).

### p6e
- **cor:exponential-cluster-threshold-subsolutions:** correct (normalized compactness plus the closure lemma). Both callers are repointed, and the shortened prop:greatest-normalized-threshold has no remaining user of the removed part.
- **lem:bounded-exponential-supersolution:** the hypotheses of cor:singular-exponential-order hold. h is semipositive and big; s⪯t since t is bounded; P_{h/2}(t)≥inf t; and off the pole set e^{−λt}MA(t)≤ν≤e^{−λs}MA^ext(s). The conclusion u≥v is t≥s. The Greatestness argument is the same with H=h_0+κ.
- **Smoothing example and m_h/κ_h paragraph:** both correct. The callers are now backward, and threshold_divisorial_constraints l.38 is fine.
- **Coordination edits (a)–(h), plus the prescribed opening:** all checked.
  - (f): d_ch, G and ω_1=κ (mass one) match section_continuous_potential_product_measures l.6–8, and lem:curve-probability-green-potential with μ=δ_z gives dd^c G=δ_z−ω_1 and mean zero. G(x,[0:1])=log ℓ+1.
  - (h): m≥1 holds, including eq:warped-closed-morse and the Demailly–Păun step.

## Fixes made
1. chapter_gauduchon_variational_volume.tex l.7: "$\Omega_\theta$ and $c_\theta(\mu)$" → "$\Omega_\theta=\theta+\ddc u_\theta$ and $c_\theta(\mu)$". section_gauduchon_volume_hessian l.6 uses u_θ.
2. section_gauduchon_quotients.tex l.80: "a smooth semipositive background" → "a smooth semipositive nonclosed background". This keeps the contrast with closed classes.
3. section_affine_local_strict_weights.tex l.8: "The pluripolar case of the next lemma uses" → "The pluripolar case of \cref{lem:relative-affine-zero-value} below uses". The next lemma is the barrier lemma itself.
4. section_mass_geometry.tex l.4 (the section opening, which did not mention its new last subsection): added "The last subsection applies this criterion to invariant backgrounds on compact quotients of three-dimensional complex Lie groups, where it gives the upper mass."

## Remaining notes (not caused by the moves; no action needed)
- **Forward references that were already in the baseline:**
  - section_invariant_mass_and_reference_densities:74: the statement of thm:iwasawa-fiber-invariant-density cites eq:iwasawa-schur-base-equation from its own proof.
  - subsection_continuous_hessian_adjoints:62 (proof) cites cor:gaud-adjoint-lq.
  - section_divisorial_adjoint_obstruction:34 (proof of lem:divisorial-adjoint-model) cites sec:logarithmic-model-selection and prop/eq:logarithmic-product-model, later in the same chapter.
  - section_warped_gauduchon_completion:180 (proof) cites thm:gaud-volume-nef-limit.
- **Optional wording:**
  - section_primitive_elliptic_bundles l.4 and l.145 both say that a base without curves rules out the curve averages. One of the two could go.
  - The p6e suggestions for chapter_gauduchon (p6g's file) and research_program l.63 remain optional.
- **section_non_kahler_geometry:** the p6b part (sec:primitive-elliptic-lower-mass, the problem and the closing paragraph) is correct. I found nothing to report and edited nothing there.
