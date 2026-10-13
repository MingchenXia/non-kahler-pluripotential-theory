# Audit a4c (reports r4g14–r4g19 and three coordinator edits)

## Verdicts
- **r4g14: EDITS CORRECT.** I checked the following:
  - The Hölder reference regularity proof: A₀ and K are the constants of `lem:chern-kiselman-input` with C₀=M, and H=M+B+1 is a valid lower bound in `prop:capacity-square-one-sided-stability`.
  - The explicit choices in `lem:thin-sublevel-capacity`/`lem:backwards-capacity` (u=φ_l, v=0, H=1, ε=1/2, s=t=D).
  - The closed-factor Steps 1–3, the recovery of CV₀ for g=q_α, and the remark on 240π.
  - The renames h→g and b→ψ in the product-measures section (the envelope-class step via A_t(p,0) is correct), and w→ρ in the exceptional section. All three renames are complete and cause no clashes.
  - The roadmap sentences against `thm:holder-reference-homogeneous-equation`, `thm:closed-factor-integrable-equation` (k≥2), `thm:continuous-potential-product-threshold`, `prop:closed-factor-density-roots`, `thm:power-capacity-critical-equation` (n≥3), `thm:logarithmic-critical-density`, the three greatest-exponential propositions and `thm:radial-integrable-selection`.
- **r4g15: EDITS CORRECT.** I checked the following:
  - In the flux ODE, m→ρ′ and r→σ; σ is not used for anything else in the section.
  - T>1, as required by `eq:global-capacity-tail`.
  - In the jump proof, α,β→a₁,a₂ and m→ℓ; the jump sum is bounded by I(a₂)−I(a₁).
  - A=max R, now cited once with the data.
  - B_r is defined and f∈L¹.
  - ρ_h(g^{1/n})=b_h(g)^{-1/n} is by definition.
  - The elimination giving c_j^{1+α}(∫g_j)^α≥c.
  - The radial density constant δⁿn!αⁿ(α+1)/πⁿ, the ball mass, and the capacity-split and root-tail exponents.
- **r4g16: EDITS CORRECT.** I checked the following:
  - With dist=|x₀z₁−x₁z₀|/(|x||z|), the identity G(x,[0:1])=log ℓ+1 holds and ℓ is uniform for ω₁, so the mean is zero.
  - d_min is now defined.
  - N→n is complete and agrees with dim X=k+1.
  - F_j→q_j, with q_j=A_j−a_j−A₀+a.
  - The 𝒜→𝒞 rename is complete; no other file uses the old names.
  - The theorem statement "solution u∼φ" is proved by φ+w.
  - In the corollary, Poincaré–Lelong gives [E]=γ_E+dd^cℓ_E, and the chain b_θ≤c_{θ−γ_E}<c_θ holds.
  - The alternative proof via `thm:divisorial-type-thresholds` works, because MA_η(w₀)=c₀f dW.
  - L_σ=tr_σ dd^c, with F_t−F=t·L_σh+O(t²), and p=4n+1 gives q<n/(n−1).
  - In the Hopf computation, dd^cβ=−α², so κ is Gauduchon.
  - The n≥2 added in `section_divisorial_normalization_stability` is correct.
  - The chapter-opening additions are accurate. They omit n≥2, but both statements also hold for n=1, so this is harmless.
- **r4g17: EDITS CORRECT.** I checked the following:
  - ρΩ²=(A/a)dW=ν₀, since A=aH/m.
  - The heat-operator rename H_t→e^{tΔ}.
  - In the obstacles section, min(2c√δ,2Kt) is right, since ∇Z is bounded by c√δ and has Lipschitz constant 2K.
  - p→P, together with the recomputation of A′ and A″.
  - L_F=lim(C_F−x)=inf(g−x)∈[−M,0].
  - The free-interval case analysis for the slope bound.
  - The example moments (mass 4 and 5/24), P_δ/ω₁=4δ/((1+δ)+(1−δ)t)², and dd^cθ=−2t dW.
- **r4g18: EDITS CORRECT.** I checked the following:
  - The indexing j≥1, with Σe_j=1/4.
  - h→ω is complete, with no stray h.
  - The explicit inequality −L^{β′}≤−bL^β+M_b gives w−M_bS∈𝒜_b(u,0).
  - The citation of `prop:ideal-obstacle-reprojection` is valid, since q=P_ω[u]_𝓘=0.
  - The fibration edits: semipositive background, h→g, μ→π in the Hopf threefold, the openness argument and the moved identity p*T_v.
  - In ideal_envelope_modifications, μ→π.
  - The chapter_igood roadmap sentence against `thm:small-curvature-strict-type`.
- **r4g19: EDITS CORRECT.** I checked the following:
  - The added ideal half of the finite-curve proof is valid: v∘r⪯_𝓘h⪯_𝓘m_h∘r, then reflection via `curve-map:lelong-pullback`.
  - The rewritten regularization proof agrees with the statement recalled in `subsec:psh-closed-regularization`.
  - The definition of strict current, the derivation of ν(v,D_j)=a_j, and the converse with δ<ε/2.
  - ρ→π, the borderline case k+1=ta_j, and the trace limit ⌊ta_j⌋/t→a_j.
  - The curvature-rank Hessian at the maximum, the twist M^{m}(D), P(E*) with π_*𝒪(1)=E, and the Serre-duality step.
  - The chapter openings of chapter_trace_data and chapter_flag_bodies.

Coordinator edits:
- (1) **Correct.** Ω_j=A_jω₁+bω₂ has multiplier proportional to 1/b, which is not constant, and `prop:singular-product-adjoint-approximation` proves recovery for it. The qualification is therefore needed.
- (3) **Correct.**
- (2) **Not quite right; see Problem 1.**

**Counts:** about 40 mathematical corrections, scope changes and added justifications checked, and 15 renamings checked (h→g, b→ψ, w→ρ, m→ρ′, r→σ, α,β→a₁,a₂, m→ℓ, N→n, F_j→q_j, 𝒜→𝒞, w→ω₁, H_t→e^{tΔ}, p→P, h→ω, μ/ρ→π). mathdiff3 was run on every file and every removed or added display was inspected; no unintended formula change was found.

## Problems found (none fixed; no edits made, so no compile was needed)
1. **Coordinator edit (2): `author/section_ordinary_type_topology.tex`, line 6, "in positive volume".**
   - **What is proved.** `thm:countable-pole-stretching` gives ω+dd^c u≥¾ω. So the mass of u, and hence the *upper* volume of its type, is at least (¾)ⁿ∫ωⁿ>0. `prop:countable-pole-all-obstacles` does give equality below every continuous obstacle.
   - **What is not proved.** The subsection explicitly allows ω with zero lower mass. Nothing shows that the *lower* volume of the type is positive; the reference q=P_ω[u]_𝓘=0 then has lower volume v₋(ω)=0.
   - **Why it misleads.** The same paragraph uses "positive volume" for the complete topologies of `thm:positive-model-complete-metric`, which concern positive *lower* volume.
   - **Proposed replacement:** "…, and potentials with prescribed countable pole sets and strictly positive curvature, hence of positive upper volume, give equality below every continuous obstacle (\cref{subsec:countable-pole-obstacles})."
2. **Pre-existing, minor: `author/section_continuous_potential_product_measures.tex`, line 6.** The chordal distance d_ch has no stated normalization. The proof's claims (t=d_ch² uniform on [0,1], mean zero, K=1−G≥0) need antipodal distance 1, which is the normalization r4g16 made explicit in `section_logarithmic_model_selection`.
   - **Proposed replacement:** "For the chordal distance $d_{\mathrm{ch}}$, normalized so that antipodal points have distance one, put".
