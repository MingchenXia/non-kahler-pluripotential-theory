# a5l audit of r5g12 (chapter_igood: analytic limits → curve fibrations)

**Verdict for r5g12: EDITS CORRECT.** I made no edits.

**What I checked.** 6 hypothesis removals or relaxations, 14 duplicate removals (4 moved labels, the new slice lemma replacing 8 copies, the new bounds equation, 6 proofs replaced by citations), and 9 simplified proofs. I read all 15 files in their current state and the full diff against 1fece9c, and ran `mathdiff3.py` on every file. Every math change matches a listed item. All labels and `\index` entries from the base are still there, and only `lem:auxiliary-slice-envelopes`, `eq:fibration-zero-obstacle-bounds` and one index entry are new. `chapcheck.sh a5l chapter_igood`, second run: no errors, no overfull boxes, no undefined references. The only messages are `Underfull \hbox (badness 1783)` in section_small_curvature_strict_types; the first run's `eq:diffuse-residual-local` warnings (section_diffuse_product_polar_obstruction, not this part) were gone on the second run.

## Priority items

- **lem:separated-curve-model-projections → prop:separated-curve-obstacle-projections.** The case σ_i=η_i, F=0 gives P_β[w]=w. Normalization holds because each factor has supremum 0. The ideal identity follows directly. The new "Moreover" claim is proved in the last line: P_γ[u]_I = Σ r_i∘π_i ∼ Σ g_i∘π_i = g. Here dd^c g = Σπ_i^*E_i − (smooth), and the divisors π_i^{-1}(x) are distinct and prime, with finite total mass. This also covers B_i=0 (where g_i=−χ_i) and S=0 (an empty family in lem:divisorial-potential-domination).
  - The `\input` now comes before w is defined, and the order still works. No `\cref` to the old label is left.
- **cor:nonclosed-/degenerate-product-polar-metric → cor:nonclosed-separated-product-metric.** With m=1, C_1=C_0=ℙ¹ and Z=ℙ^k, this is exactly the old setting, so every old conclusion is included.
  - "Positive when f>0" holds: η_i, τ and κ are positive.
  - "Not closed when f is nonconstant" holds: dΘ_f = p^*df ∧ s^*τ.
  - "Θ_0 not big" holds: the test form T pairs to zero with Θ_0 (also when m=1, with a one-factor wedge), and Stokes applies.
  - The 4 index entries were moved. chapter_research_program.tex has already been redirected; chapter_history.tex has no references to these labels.
- **cor:auxiliary-product-all-obstacle-criterion → cor:general-auxiliary-all-obstacle-criterion.** With T=C_0 and α=(f∘π)pr_T^*τ, α is semipositive (f≥0, including f=0) and zero on the slices. Θ_α=Θ_{σ,f} and R=Ψ+Q∘p. The old envelope identities are lem:general-auxiliary-product-projections.
  - The new proof chain holds: lem:product-relative-envelope-classes, then pullback (α≥0), then prop:fibration-relative-envelope-class (connected fibers Z, dim B < dim M), then prop:ideal-obstacle-reprojection with R=P[U]_I.
  - The only external caller, in chapter_research_program, was already updated.
- **lem:auxiliary-slice-envelopes.** The proof is complete:
  - Semipositivity is used only for u∘π ∈ PSH(Γ).
  - Restricting max(v, u∘π − sup u) to the slices gives γ-psh competitors.
  - For the ideal part: D_j×T is prime because T is connected, π^*S has finite mass, lem:divisorial-potential-domination gives v ⪯ g∘π ∼ q∘π, and then P_γ[q]=q by prop:p-below-i.
  - All 5 remaining citing places meet the hypotheses (semipositive, zero on slices, divisorial ideal envelope with g=0 or from the "Moreover" clause): ex:nonclosed-zero-volume-distinct-models (f>0), cor:nonclosed-separated-product-metric, the weighted lemma, the arbitrary lemma, and the general-auxiliary lemma.
- **eq:fibration-zero-obstacle-bounds** (proved in Step 2). Since 0̂ ≥ L, translating competitors by L shows the lower bound. Since sup b ≤ K_0 for every competitor below 0̂, the upper bound follows. Both work for ordinary and ideal competitors.
  - prop:fibration-relative-envelope-class: q_M = Ψ + b∘p with b ∼ q_Y, then prop:relative-elementary. Correct.
  - The curve case of cor:fibration-obstacle-equality is also correct.
  - Dropping "nonempty" is safe. With H=∅ we get Ψ=0, L=0, Z=∅ and 0̂=0, and Steps 1–6, the relative-class proposition, the corollary (with G_j=B) and cor:fibration-component-cover all still work.
- **New Dini argument in cor:fibration-obstacle-equality.** It holds. The q_j decrease pointwise to r=q_B everywhere, and r ≤ q_B ≤ r. The sets {q_j − B ≥ ε} are closed (q_j is usc, B is continuous), decreasing, and have empty intersection, so by compactness they are eventually empty.
- **Gauge failure without "mass one".** σ_s∘Γ_F = Γ_{sF}∘σ_s. Here sθ' = sθ + dd^c(sF) > 0, sF is still nonconstant, and the scaling maps τ_{θ,0}→τ_{sθ,0} and τ_{θ,F}→τ_{sθ,sF} by prop:ordinary-topology-background-transport. The remark now says "mass 1−c when ∫θ=1", which is correct.
- **Other scope changes.**
  - m≥1: one factor is the base of the induction, and the test forms L_i and T work with one factor.
  - "Every sufficiently large m": the proof takes the liminf in j, then lets m→∞ and δ→0. The only external caller (chapter_research_program) still reads correctly.
  - prop:divisorial-product-obstacles with continuous F: the fibration reduction allows F ∈ C(M), and Z=∅ here, so F̂ is finite.
- **Simplified proofs.**
  - thm:all-obstacle-analytic-closure: the transported competitor families are correct. prop:ordered-ideal-envelope-convergence allows ε_j ≥ 0, so ε_j = 0 is fine. θ_F is an arbitrary smooth form, which the chapter's standing assumption allows. The divisorial estimate is local.
  - thm:countable-pole-stretching: lem:qpsh-removable-analytic, in r5g01's wording (closed locally pluripolar Z, in particular a nowhere dense analytic subset), applies to the point z_j. The function is nonpositive, so it is bounded above there, and the upper-limit extension takes the value −∞.
  - Weighted lemma: setting σ_i = a_iη_i (or 0) is admissible. The scaling in prop:i-envelope-operations covers it, and so does the case J(a)=∅.
  - prop:arbitrary-curve-product-metric: Λ_σ is a bijective isometry coordinate by coordinate, and it commutes with atomic projection. Noncompactness is in prop:weighted-product-metric-comparison, and L¹ convergence is in prop:curve-arbitrary-background-models.
  - "Analytic ⇒ ideal" via prop:analytic-envelope-type holds in any smooth background.
  - cor:general-auxiliary-background-boundaries with h≥0: non-closedness needs only dh≠0, and bigness needs h>0. Both apply to T=C_0 and to the Hopf example.
  - ex:whole-fiber-incidence-envelope via the fibration reduction (β=σ_2, w=0, 0̂=G): correct.

## Notes (no errors; no edits made)

1. `section_arbitrary_curve_product_metrics.tex:31` cites cor:general-auxiliary-background-boundaries, which comes later in reading order. This is not circular: that proof uses only descent, Stokes and lem:curve-background-area, and nothing relies on this remark before that point.
2. `section_countable_pole_obstacles.tex:86` (optional). It relies on the reader noticing that the smooth-F nonseparation proof works for continuous F, which is true. P_{ω,F}[0]_I = P_ω(F) follows from P_{ω,F}[0] ≤ P_{ω,F}[0]_I ≤ P_ω(F).
3. `section_ordinary_type_topology.tex:44` (optional). "They contain the diagonal because multiplier ideals decrease…" gives a reason that applies only to 𝒰(t,a). A possible wording: "They contain the diagonal; for $\mathcal U(t,a)$ this holds because multiplier ideals decrease as the weight increases, …".
