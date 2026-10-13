# a5o audit of r5g23 (base 1fece9c)

## Verdict
r5g23: **EDITS CORRECT**. I found no errors introduced by the pass. I applied the two coordinator edits in chapter_research_program.tex; both are listed below.

Checked: 12 hypothesis removals, about 20 duplicate removals, 7 simplified proofs or constructions. I also checked every changed \cref in chapter_research_program.tex, including all merged labels, against the current target statements, and scanned the mathdiff of all nine files. Parallel-torsion and pluriclosed-deformation files: no change.

## Priority items
- **Descent via thm:hermitian-space-descent** (curve theorem, density endpoint, cuspidal downstairs). The hypotheses hold.
  - A resolution in the appendix is a proper bimeromorphic map from a compact manifold. π: E→X (resp. Y→X) is finite, bijective and biholomorphic off a finite set (resp. off the singular divisor), so it is one.
  - The standing assumptions also hold: reduced, irreducible (connected and unibranch with connected normalization) and unibranch. The background h is a smooth real (1,1)-form.
  - The theorem's bijection PSH(X,h)→PSH(E,β) gives exactly what is used: u = (U−S)∘π⁻¹ and ψ are in PSH(X,h), and w∘π ∈ PSH(E,β), as is u'∘π.
  - Resolution independence via thm:space-extended-measures: that theorem states that the measure is the same for every resolution. The type is defined on X, so it does not depend on the resolution either.
- **Radial primitive.** (i/2π)dz∧dz̄ = dA/π and β₀ = dA/V, so f_γβ₀ = (πC₀/V) r⁻²t^{-γ}(i/2π)dz∧dz̄. With C₀ → πC₀/V, P_b of eq:curve-log-primitive becomes exactly eq:unibranch-density-primitive, in both cases γ≠2 and γ=2.
  - The derived properties are all covered by the statement or proof of thm:curve-products (earlier in reading order): ∂∂̄P = P''/(4r²) = C₀r⁻²t^{-b}, flux → 0 for b>1, |P|/t → 0 (zero Lelong number), mass finite iff b>1, no L^p for p>1.
  - Non-Hölder tail: v_γ − v_γ(q) = c_γP_γ + (R − R(q)), with c_γP_γ a nonzero multiple of t^{2−γ}. Correct.
- **"ν non-pluripolar".** This follows because MA^ext gives zero mass to locally pluripolar sets (thm:space-extended-measures) and c > 0. No caller uses the deleted sentences.
- **"c' > 0" dropped.** Every member of the type has mass M, and the mass of c'ν is c'ν(X). So c' = M/ν(X) = c for every real c'. The same holds for the density endpoint (c = M/F_γ = c_γ) and for the cuspidal case, where lem:cuspidal-bounded-mass is applied to u'∘π − v₀ ∈ PSH(Y,k) and (k+dd^c(u'∘π−v₀))ⁿ = (H+dd^c(u'∘π))ⁿ.
- **s ≥ n+3 → s > n.** Y = (C/Z[i])ⁿ has real dimension d = 2n, with m ∈ Z^{2n}, and Σ(1+|m|²)^{-s} < ∞ iff 2s > 2n.
  - Under s > n, H^s is an algebra; this was already stated before the pass.
  - Summability also gives absolute convergence of the Fourier series of all derivatives of order ≤ 2 of w ∈ H^{s+2}, so H^{s+2} ⊂ C² with the sup bound D.
  - Later uses need only C² (V_j → V in C², continuous densities of B_jⁿ) or C¹ (Hölder 1/3), and f ∈ H^s ⊂ C⁰.
- **lem:cuspidal-bounded-mass.** The first proof is complete: (dd^cU)^{r−1} is a closed current of order zero, and dd^cU∧T = dd^c(UT). So the "Alternatively" proof was redundant. The H-version was used only at the place now rewritten.
- **prop:cuspidal-nonclosed-repair.** An A with ∂A(z₀) = 0 and ∂∂̄A(z₀) ≠ 0 off q exists (for example χ|z−z₀|²), and a real nonconstant B has ∂B ≠ 0 somewhere. At such a point ∂α = ∂∂̄A∧∂B ≠ 0. I rechecked the formula ∂α = −∂A∧∂∂̄B + ∂∂̄A∧∂B. Reality and dd^cα = 0 are also correct.
- **D_μ ≤ λ_μ(h)⁻¹A_h.** This is eq:gaud-collapse-basic with θ = h, which is pseudoeffective, and λ_μ(h) > 0 by cor:gaud-volume-big-positive (h is big). Correct.
- **Programme references, all correct.**
  - Fiber bands: thm:fiber-integrability-band now carries the crossing and semipositive labels. Its hypotheses are SNC divisors, β ≥ 0 with ∫β^q > 0, and one chart per divisor, matching l.324. The wording of l.326–334 is consistent with it, and thm:modified-base-fiber-band also has a semipositive residual.
  - Diffuse models: the l.224–226 statements match the current prop:all-modifications-diffuse-polar-blindness (= old two-mass prop), cor:diffuse-hermitian-model-interval, cor:diffuse-product-exact-volume (= diffuse-mass-invariant-models), prop:diffuse-representative-mass (= mass-polynomial), cor:diffuse-surface-mass-invariance, prop:disjoint-diffuse-scalar-obstruction and prop:equal-residual-anisotropic-models. That includes the hypotheses 0 < v₋ ≤ v₊ < ∞ and dd^c(ω^q) = 0.
  - Obstacle criterion: cor:general-auxiliary-all-obstacle-criterion (unit divisor, arbitrary compact T, semipositive α vanishing on slices, no bounded mass).
  - Product polar metric: cor:nonclosed-separated-product-metric covers both merged labels.
  - Other results: thm:smooth-boundary-trace-regularity (locally bounded, any smooth θ); thm:gaud-local-adjoint-endpoint (no n ≥ 3 left in its section); thm:hopf-projective-exact-trace (Ω ≥ aα); thm:zero-lower-mass-product-equation and cor:radial-residual-nonclosed-product (H nonclosed with v₋(H) = 0 if v₋(h₀) = 0); prop:small-curvature-intrinsic-traces (Y in no D_j).
  - No problem statement asks for something the book proves. qu:gaud-metric-boundary now excludes the Iwasawa fiber-invariant case.
- **Growing-jets summary.** It describes thm:optimal-growing-jet-range (range o(m^{1/(r+1)}), uniform in direction, criterion eq:fixed-weight-jet-criterion), thm:curvature-boundary-jets (argument 2√(mρ)·d, so scale 1/(2√(mρ))) and the flat example of sec:growing-jet-corrections accurately. The label prob:growing-jets-localization is unreferenced.
- **Other items.**
  - "surjective" dropped in qu:fiber-selected-approximation: a submersion is open and X is compact, so its image is all of the connected B. Correct.
  - The standing data dropped from the problems are all fixed at section or chapter level (l.7, l.15, l.57, l.132; the non-Kähler section).
  - Dimension one (l.100) matches def:gaud-variational-volume and cor:gauduchon-threshold.
  - The primitive-elliptic specialization holds: c = β−α, A = 2, κ = 1, M₀ = 1, T = 4π, and 24π(1 − F(1,4π)) = 8.

## Edits made (coordinator notes), chapter_research_program.tex
1. l.41: "and bounded comparison extends greatestness to unbounded competitors" → "and singular strict domination extends greatestness to unbounded competitors". Checked: the greatestness step of thm:continuous-potential-product-threshold applies lem:bounded-exponential-supersolution, which is proved from thm:singular-strict-domination and applies to arbitrary s ∈ PSH(X,H).
2. l.59: "Let $f$ be a nonzero density with $b_h(f)>0$. If $D_{f^{1/n}}$ has … maximizer, then $f^{1/n}$ is smooth" → "Let $f$ be a nonzero density. If $D_{f^{1/n}}$ has … maximizer, then $b_h(f)>0$, $f^{1/n}$ is smooth". Checked: cor:smooth-dual-exact-equation assumes only that f is nonzero and concludes b > 0. D_{f^{1/n}} is defined for f^{1/n} ∈ Lⁿ, so the sentence stays meaningful; I added the conclusion b_h(f) > 0.

chapcheck (chapter_research_program, appendix_hermitian_spaces): no errors, no overfull boxes, no undefined references; only the ignorable Underfull (badness 1783).

## Remaining notes (not edited)
- chapter_history.tex l.819 still says "descent through disks … obtained directly". Descent now comes from thm:hermitian-space-descent. r5g23's proposal stands: replace "descent through disks" with "descent through the normalization".
- Optional, no error: qu:exact-trace-program (l.245) dropped "For general data,". The surrounding paragraphs (l.241, l.257) say which cases are settled, so it reads as the general question.
