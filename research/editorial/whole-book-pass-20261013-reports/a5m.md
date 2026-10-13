# Audit a5m (report r5g02, base cae12da)

## Verdict
r5g02: CORRECT AFTER FIXES. The math is sound. I made two small wording fixes in r5g02's files. Two sentences in chapter_history.tex are now stale; they need a coordinator edit.

## Counts checked
- Hypothesis removals or weakenings: 16.
  - N>=1; m real in the lelong-loss lemma; "positive" for S in lem:divisorial-potential-domination and cor:divisorial-current-ordinary-type; w bounded above; f bounded below; Green-ball m>0.
  - Standing "connected compact" in sec:psh-birational-ideals, with lem:ideal-equivalence-modification restated; compactness in prop:psh-descent-modification and prop:polar-curvature-pushforward.
  - n>=1 and m>=1 in the curve-map lemmas; compact source in cor:restricted-analytic-divisorial-bound; u_lambda ~ phi weakened to u_lambda ⪯ phi; "decrease" replaced by "tend"; non-pluripolarity in the definition of A_theta and in lem:measure-smoothing-integrals; properness in the new remark after lem:bergman-divisorial-error.
- Duplicate removals: 7.
  - Two Skoda citations, the birational re-derivation, the Dini power case, the critical-fiber descent, the envelope regularity paragraph, lem:continuous-potential-smooth-loss.
- Simplified or moved proofs: 5.
- Every caller of each changed label was checked. Mathdiff scan over all 22 files: every math change is one listed in the report.

## Priority items
- **Skoda (DemAM11 Lemma 5.6).** DemAM11 is not in the repository (research/sources has no copy), so this check rests on my own knowledge of the book. Earlier audit notes in research/editorial agree.
  - Demailly's Lemma 5.6(a), for psh phi: if nu_D(phi,x)<1, then e^{-2phi} is integrable near x. Demailly normalizes nu_D(log|z|)=1.
  - The book normalizes nu(log|z|^2)=1 (sec:analytic-types), so nu_book = nu_D/2. Apply the lemma to phi=u/2: then nu_D(u/2)=nu_book(u), and nu_book(u,x)<1 gives e^{-u} integrable. The book's threshold "<1" is therefore exactly right; the factors of 2 cancel.
  - Zero-Lelong lemma: nu(tq,x)=0<1, after a local smooth correction. This gives I(tq)=O, so q ~_I 0, and the addition rule gives v+q ~_I v.
  - Planar lemma: dd^c log|z|^2 is the Dirac mass at 0, so the atom of dd^c u at x equals nu_book(u,x). Hence nu(v,x)=0, and e^{-tv} is integrable for every t>0, as the Hölder step needs.
  - The citation is not circular.
- **Remark after lem:bergman-divisorial-error (properness not used).** Confirmed. The upper estimate pulls back a local Bergman bound on U, whose locally bounded error stays locally bounded on Z. The lower estimate is a change of variables on small patches of Z with relatively compact image; injectivity a.e. gives multiplicity one. No pushforward of measures, fiber finiteness or integral over all of Z is used. F=π∘σ is injective off σ^{-1}(T∪D), which is nowhere dense.
- **lem:continuous-potential-smooth-loss.** prop:bounded-almost-regularization gives smooth v_j decreasing to u with θ+ε_jω+dd^c v_j≥0, ε_j↓0, for bounded u. Dini applies because u and the v_j are continuous on the compact X. The proposition comes earlier in reading order and does not depend on the Chern section, so there is no circularity.
  - The Chern-average argument now in lem:smooth-holder-reference-approximation is complete: convexity in log t, derivative →0, Dini for λ(·,t), uniform convergence of R_t u, then division by 1+ε_j.
  - The callers in section_gauduchon_trace_topology use only the unchanged statement (common bound dd^c a_k ≥ -Cω). They still fit.
- **sec:psh-birational-ideals with noncompact π.**
  - lem:adjoint-ideal-transform is local: properness gives compact fibers, and Hartogs extends across S, which has codimension ≥2 for any proper bimeromorphic map onto a manifold.
  - lem:birational-ideal-order and lem:ideal-equivalence-modification are local. The ideal relations are defined on any manifold (chapter_framework, line 180).
  - The callers in appendix_hermitian_spaces and section_ideal_envelope_modifications still apply.
  - prop:psh-descent-modification and prop:polar-curvature-pushforward use only properness.
  - cor:restricted-analytic-divisorial-bound: the source Z is automatically compact and connected, as lem:gauduchon-uniform-lelong needs.
- **Other weakenings.**
  - Every weakened hypothesis was used only in the weaker form: only u_λ≤φ+C; only sup_K w; only ρ≤inf f; m>0 real throughout the Green-ball subsection; λ_j→0.
  - A_θ(ν) and non-pluripolarity: the smoothing lemma's proof works for all ν, because H_j↓z everywhere and the dominated convergence is pointwise. Users that need a non-pluripolar ν state it themselves (prop:big-smoothed-measure-continuity, the moment estimate). In big backgrounds, A_θ(ν)<∞ forces ν to be non-pluripolar anyway.
  - "S has finite mass": S=Σc_j[D_j] with c_j>0 is a series of positive currents. Finite mass means the series converges, and the limit is positive and closed, as the corollary's proof now says.
- **cor:dini-distance-rates.** No caller used the power case. chapter_history.tex line 779 mentions only logarithmic rates, so it stays correct.

## Fixes made (in r5g02 files)
1. section_psh_local_ideals.tex, last paragraph. The pass had widened the scope of a pointer to curve-map:ideal-types, which is proved only for compact connected sources (it fails, for example, for a disconnected source with a component mapped to a point).
   - Old: "For maps with connected fibers onto a compact Riemann surface"
   - New: "For maps with connected fibers from a connected compact manifold onto a compact Riemann surface"
2. section_psh_divisorial_estimates.tex, line 104 (the new remark). Z need not be connected, and on a component contained in the exceptional set the lemma has no meaning.
   - Old: "injective off a proper analytic subset of $Z$"
   - New: "injective off a nowhere dense analytic subset of $Z$"
   - Matching change in section_psh_descent.tex, line 196 (proof of lem:birational-ideal-order): "injective off a nowhere dense analytic subset of $Z$".

## Proposed (not edited): chapter_history.tex
- **Line 21.** It says the Chern averages give lem:continuous-potential-smooth-loss; that is no longer true. Replace the first three sentences with:
  "For a continuous potential, the logarithmic derivative of the Chern averages tends to zero; together with Dini's theorem and uniform continuity, this gives the vanishing curvature loss used in \cref{lem:smooth-holder-reference-approximation}. For a H\"older reference these averages keep a common H\"older bound, and division by $1+\varepsilon_j$ makes them $\omega$-plurisubharmonic. The uniform approximation of continuous potentials in \cref{lem:continuous-potential-smooth-loss} follows from \cref{prop:bounded-almost-regularization} and Dini's theorem."
- **Lines 615–618.** They describe the old Bergman proof of the zero-Lelong lemma. Replace them with:
  "The ideal neutrality of \cref{lem:zero-lelong-ideal-neutrality} combines Skoda's integrability theorem \cite[Lemma~5.6]{DemAM11} with the local ideal-addition calculus; the strong openness used there is stated in \cite[arXiv~v2, Corollary~2.3, p.~12]{DemCohomology15}."
  - Please confirm against the source that Corollary 2.3, not Theorem 1.2, is the strong-openness locator. I inferred this from the order of the original sentence.

## Compile
`chapcheck.sh a5m chapter_framework`: no errors, no overfull boxes, no undefined references. The only message is the permitted Underfull (badness 1783).
