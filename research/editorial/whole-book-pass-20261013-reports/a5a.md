# Audit a5a (reports r5g03, r5g04; base 1fece9c)

## Verdicts
- **r5g03: CORRECT AFTER FIXES.** One scope change (a narrowing) is restored; everything else checks out.
- **r5g04: EDITS CORRECT.**

## What I checked
- **r5g03:** 12 hypothesis removals, 8 duplicate removals and 3 simplified proofs. I ran the math diff on all 19 files.
- **r5g04:** 15 hypothesis removals or scope extensions, 11 duplicate removals or citations and 5 simplified proofs. I ran the math diff on all 19 files.
- **Priority items** were all checked in full:
  - r5g03: the n=1 cases of thm:mass-invariance-characterization and thm:raw-primitive; cor:surface-mass; cor:comparison-fails.
  - r5g04: lem:continuous-hermitian-fredholm; the ramified-root example; integrated Hermitian curvature for n≥1; prop:shrinking-intermediate-currents.

## Fix made (1)
**File:** subsection_fixed_stein_finsler_hypersurface.tex, line 7.
- **Old:** "In this subsection, $X$ is a smooth projective variety, and $E\to X$ …"
- **New:** "In this subsection, $X$ is a smooth projective variety of dimension $n\geq1$, and $E\to X$ …"
- **Why:** r5g03 deleted "connected … of dimension $n\geq1$", saying it only restated the book's conventions. But chap:gauduchon assumes $n\geq2$ "unless a section specifies another setting". So the deletion silently narrowed thm:fixed-stein-finsler-hypersurface to $n\geq2$. The proof works for $n\geq1$ (with $n=1$ the conclusion is "at most $0$ negative eigenvalues"). "Connected" can stay out, because the global convention covers it.
- **Compile check:** `chapcheck.sh a5a` on chapter_compactness, chapter_damped_measures, chapter_energy, chapter_gauduchon, chapter_mass and chapter_products. No errors, no overfull boxes, no undefined references. The new label eq:infinite-mass-partial-sums resolves on the second run. The only message left is the ignorable Underfull (badness 1783).

## Findings

### r5g03
- **thm:mass-invariance-characterization at n=1.**
  - Condition (1) is Stokes' theorem, (2) is vacuous and (3) vanishes for degree reasons.
  - Step 3 uses thm:bounded-exact-regularization, which has no dimension restriction.
  - Callers that add "or by Stokes when k=1" (section_finite_restricted_invariants, section_resolved_trace_masses, section_uniqueness_bounded_comparison l.43) are now redundant but still correct.
- **thm:raw-primitive at n=1.** dω=0 for degree reasons, and prop:closed-energy has no dimension hypothesis.
- **lem:torsion-polarization.** "Nonempty open set" is correct: the expression is polynomial in A.
- **E_ω on C^∞.** The identities in prop:radial-torsion-defect and prop:radial-surface hold for all smooth u (I checked the expansion of the first identity).
- **cor:surface-mass and cor:comparison-fails.** The new one-line proofs are complete and not circular. Neither result has callers that used the deleted explicit pair.
- **Completion energy.** The deleted flatness claim is exactly (2)⇒(1) of cor:completion-flat-invariant-mass. ex:torus-flat-nonstationary cites the corollary, which still covers it.
- **r=1 in thm:convex-norm-deformation-obstruction.** With r=1, ρ₁=1, D₁G=2G=2a₁ on Σ and I₀=−λ₁∫a₁μ, so the proof holds.
- **k=1 in thm:external-tensor-complement-convexity.** This reduces to cor:positive-mean-complement-convexity; 2^k+k=3 matches cor:hirzebruch-exact-complement-index.
- **Other items, all fine:**
  - lem:closed-submanifold-complement-index-bound: κ≤D holds by definition.
  - prop:gauduchon-amgm: f is forced to be smooth and positive.
  - Hirzebruch Hom splitting via lem:hirzebruch-prioritary-comparison.
  - The polar corollary's "locally strongly convex" step (domination of quadratic forms).
  - The det h curvature identity; the convention tr F_h=∂̄∂ log det M is correct.

### r5g04
- **lem:continuous-hermitian-fredholm.** The GT01 locators match Gilbarg–Trudinger (2nd ed. and 2001 reprint) as I know the book. I could not confirm them by web search, so they rest on my knowledge of the text.
  - Thm 9.11 is the *interior* W^{2,p} estimate for continuous a^{ij}, with a constant depending on their moduli of continuity. The coordination log suggests "global", but that is Thm 9.13. The text correctly uses interior estimates on a finite cover of coordinate balls, which gives uniformity in s.
  - Thm 9.6 is the strong maximum principle for W^{2,n}_loc (c=0, or c≤0 for a nonnegative maximum). It is applied with real dimension 2n, and p>2n gives W^{2,2n} on balls. The L_s−1 case uses c=−1.
  - Thm 5.2 is the method of continuity. (The Fredholm alternative is Thm 5.3.)
  - The argument is complete.
- **Ramified example on C.**
  - h⁰(C,L^k)=k+1+max(k−q+1,0) is correct. Very ampleness of A=L^q is correct.
  - For j<q−1, p_j=vU_j(π(t)), so ∂_t p_j=0 at a ramification point and r_j(ξ_h)=0. The one- and two-atom witnesses hold.
  - The corollary needs sec:projective-first-jet-positivity for n=1. It now allows n≥1, and nothing in that section uses n≥2. The Gaussian/Taylor replacement for Bernstein polynomials is complete: f has compact support, so f∗G_ε is entire with real Taylor coefficients.
- **Integrated curvature for n≥1.**
  - For n=1, D_{1\bar11\bar1}=0 and T=0, and the four-term identity is trivially consistent.
  - The torus proof with m=1 then gives S=0, hence ∂h=0. The deleted step "H_h=0" was unused.
  - cor:torus-cover: compactness, connectedness and finiteness follow from Z being compact and connected and π being a covering.
- **prop:shrinking-intermediate-currents.** Weak convergence bounds the masses. sup u_j=0 and the fixed b were unused. Both callers in section_hopf_defect_classification satisfy the new hypotheses.
- **Other items, all fine:**
  - prop:ordered-contact-general: the new proof is complete; both sides are identified through thm:arbitrary-extended-ma since D_t⊂{v>−t}.
  - lem:weighted-extended-lsc: the weighted continuity is recalled in sec:psh-local-capacity l.71 and extended to smooth backgrounds in sec:hermitian-capacity l.22.
  - lem:unbounded-gauduchon-trace-density without g∈L¹: monotone convergence and finiteness of the left side give the measure inequality.
  - prop:bmp-metric: proved via prop:smooth-bmp-metric, not circular. prop:bmp-finite without v_+<∞.
  - eq:infinite-mass-partial-sums and its reuse in prop:integrable-infinite-mass.
  - Hopf restructuring: the all-|a_j|≥1 case goes via cor:griffiths-nonpositive-exact-complement-index; the degree sign uses α∧γ^{n−1}>0 pointwise.
  - lem:smooth-hypersurface-current-support at m=1.
  - The n=1 case of sec:continuous-pluriharmonic-traces.
  - thm:damped-continuity with w≥0.
  - cor:gauduchon-parabolic-entropies via thm:mass-invariance-characterization and prop:gauduchon-potential-persistence.
  - Δ_t=L_{u_t} has the same normalization.
  - The Ricci-flat corollary keeps the surface assumption through the section's standing assumption.

## Proposals (no edit; files outside my parts)
- **section_hopf_sections.tex l.58.** It says "In the notation of \cref{ex:hopf-exact-complement-index}". X_q and E_a are now defined in the paragraph before prop:split-hopf-pure-complement-indices, not inside the example. The reference still resolves and the text is correct. Optional wording: "In the notation of \cref{subsec:flat-restriction-hopf-complements}, $L_k$ is the line bundle $E_a$ … so \cref{ex:hopf-exact-complement-index} also gives …".
- **r5g04's proposed chapter_history l.79 text.** The locators are right; keep "interior $L^p$ estimates" (not "global").
- **subsection_fixed_stein_finsler_hypersurface.tex, final TeX comments.** These predate the pass and are not printed. One cites a preprint locator ("Source reconstruction: Liu--Wan …") and one uses workflow wording ("… are not certified here"). The coordinator may delete these four comment lines; I left them, as r5g03 did.
