# a5n audit of r5g22

## Verdict
**r5g22: CORRECT AFTER FIXES.** I made one small fix to the wording of a proof. One coordinator item concerns `chapter_history.tex`. No mathematical error was found.

## What I checked
I read every changed file in full, against the base `1fece9c`, using both the word diff and the math diff. All labels and `\index` entries are the same before and after; `lem:big-model-concave-envelope` now sits on the merged lemma. The compile check `chapcheck.sh a5n ...` gives no errors, no overfull boxes and no undefined references. The only message is the ignorable Underfull (badness 1783) in section_unibranch_nonclosed_cuspidal_products, which is not in this part.

- **7 hypothesis removals or generalizations checked:**
  - "u_j ∈ E_φ" is now "u_j ∈ PSH(X,θ)" in two results: prop:relative-common-envelope-criterion and thm:relative-moving-measure-continuity. Upward stability, from h ≤ u_j ≤ φ+C, gives u_j ∈ E_φ. The second proof only calls the first.
  - lem:big-truncated-addition-limit: the mass bound now comes from prop:bmp-finite. Bounded mass is a standing assumption (chapter_bounded_mass_equations line 9), and the lemma is used only in this chapter.
  - cor:metric-pvp-minimal-volume: "bounded mass" was a restatement of the standing assumption.
  - lem:big-concave-envelope: generalized to u ∈ E_φ.
  - toric subsection: "effective" dropped for the boundary D.
  - appendix: "pure" dropped.
- **13 duplicate removals or proof-by-citation replacements checked.** I went through each cited proof line by line with its stated replacements: thm:big-relative-fixed-continuity (three cited proofs); lem:big-weighted-common-bound; thm:big-minimal-general-measures; thm:big-model-exponential; Step 4 of thm:als-general-measure; thm:big-model-normalized; thm:big-unrestricted-addition; thm:relative-finite-domination; thm:relative-extended-domination; cor:relative-extended-exponential-order; prop:big-model-moment-bound; the merged concave-envelope lemma; thm:cone-bounded-equation.
- **3 simplified proofs checked:** the truncation proof of the merged lemma, the borderline case of the quotient lemma, and a removed remark in prop:big-relative-projection.

## Findings on the priority items
- **Domination theorems (cited proof in chapter_mass_bound_volumes, which comes earlier, so no circularity).**
  - thm:relative-finite-domination: "subtracting finite measures" holds because (1−b⁻¹)ⁿμ_w ≤ μ_u on D_b and μ_u is finite. The collapse step uses thm:normalized-compactness (connected X) and the fact that the extended μ_u is finite and does not charge pluripolar sets. κ replaces ℓ through thm:relative-uniform-mass-lower.
  - thm:relative-extended-domination: comparing on {w>−k}, where μ_w is finite (thm:arbitrary-extended-ma), is correct.
  - cor:relative-extended-exponential-order: the cited proof works with the extended measures.
- **thm:big-relative-fixed-continuity.** None of the cited steps uses θ ≥ 0:
  - rooftop and stretch closure;
  - contact support (thm:big-general-envelope-contact);
  - positivity of mixed products (lem:restricted-positive-product, for any smooth θᵢ);
  - ordered contact (prop:ordered-contact-general);
  - the lemmas fixed-npp, monotone-capacity, weighted-lsc and Hartogs, and thm:general-background-damping, all stated for arbitrary smooth θ.

  The envelope identity, ℓ, and zero domination with v = u ⪯ φ fit exactly where they replace the semipositive versions.
- **lem:big-weighted-common-bound.** With h in place of p₁, the a_j have a common upper bound by hypothesis, and a ⪯ φ is assumed. Zero domination applies, and the squeeze step goes through.
- **Truncated-density and zero-exponent arguments.** Reference φ or V, exponential order, ℓ, ℓ_V or κ, fixed-dominator continuity and lem:normalized-exponential-npp (any smooth θ) all fit. Step 4 compares u_j ∈ E_φ, which satisfies u_j ⪯ 0, with s + (j−1)max(0, sup s) ∈ E_0, in the correct direction.
- **thm:big-unrestricted-addition.** χ_T = g_T(q) with q ≤ a_j, a, so the truncation at −2T is invisible on {χ_T > 0}. The cited argument applies.
- **Merged lemma.** I checked each step:
  - Lt ≤ χ(t) ≤ t gives Q_L(u,φ) ≤ p ≤ u.
  - τ = χ⁻¹ is C^{1,1} with L⁻¹ ≤ τ' ≤ 1, so lem:bounded-convex-pair applies to the truncations p_m ≤ φ_m.
  - The decreasing limit (G nondecreasing in both variables) and locality on {p > q−m} give μ_w ≥ τ'(p−φ)ⁿμ_p.
  - Ordered contact finishes the proof.

  Both uses check out:
  - χ_s in prop:big-minimal-higher-moment: F_s is bounded and ≥ 1, so 1 ≤ χ_s' ≤ L. The later steps need only p_s ∈ E_V and μ_{p_s}(X) ≥ ℓ_V, not p_s ∼ V.
  - prop:big-model-moment-bound: the Tonelli bound 3max(1,M) over [0,∞) and the Cauchy–Schwarz bound √(KB) hold.
- **Toric subsection with negative a_ρ.**
  - w_D, the order −qa_ρ of B_D, and dV_D = |B_D|^{2/q} need no sign condition.
  - The polar-coordinate integral is ∫exp(2⟨m+w_D,x⟩ − 2g)dx, and the convex-cone lemma is an equivalence for any linear form.
  - Coefficients a_ρ > 1 were already allowed before the pass.
- **Cone at a = 0.** β₀ = β, V = d and c₀ = c_b, as the proof states. P₀ = sR follows from substituting r ↦ sr, and Q₀' = (R−1)/(1−s) = Q'. The relations F' = P and F'' = c k sⁿ(1−s)/P^{n−1}, and Aⁿ = c ν, hold on 0 < s < 1 for a = 0.
- **Appendix.** "Pure" is implied by irreducible. "Independent of the resolution" is implied by "on every resolution". The deleted preview paragraph is contained in the proof of thm:space-extended-measures.

## Fix made (chapter_relative_finite_measures.tex, proof of thm:relative-finite-domination, lines 75 and 80)
The collapse argument cited from thm:big-relative-domination lets b → ∞, so the fixed-measure inequality is needed for every admissible b, not only one fixed value.
- "and fix $b>1$ with $(1-b^{-1})^n>c$." → "and let $b>1$ satisfy $(1-b^{-1})^n>c$."
- "uses \eqref{eq:relative-contact-fixed-measure}, the lower bound" → "uses \eqref{eq:relative-contact-fixed-measure} for all such $b$, the lower bound"

The compile check was rerun after the edit and is clean.

## Coordinator items (not edited)
1. **chapter_history.tex:817.** After "effective" was dropped in the toric subsection, the sentence "here restricted to full-dimensional cones and effective rational boundary" understates the book's statement. Proposed replacement: "here restricted to full-dimensional cones and rational boundary". If the source theorem itself assumes an effective boundary, a better wording is "here restricted to full-dimensional cones; the rational boundary need not be effective".
2. **Optional, predates the pass.** chapter_bounded_mass_equations.tex:57–62 shows that the standing assumptions already imply v₋(ω) > 0. The hypothesis of cor:metric-pvp-minimal-volume is therefore automatic inside this chapter; the corollary has content only when read under bounded mass alone. This matches r5g22's placement proposal. A possible rewording: "Assume only the bounded mass property and $v_-(\omega)>0$."
3. **Cosmetic, no change needed.** section_relative_extended_domination.tex:3 says the general principle follows "from the stretching step in the proof of thm:relative-finite-domination". That proof now only cites thm:big-relative-domination, and the extended proof cites the same step directly. The statement remains correct.
