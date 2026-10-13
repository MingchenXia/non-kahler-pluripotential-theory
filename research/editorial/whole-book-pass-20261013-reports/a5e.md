# Audit a5e (reports r5g11, r5g21; base 1fece9c)

## Verdicts
- **r5g11** (chapter_normalization sections, chapter_igood): **EDITS CORRECT**
- **r5g21** (chapter_mass_bound_volumes and its sections): **EDITS CORRECT**

I made no edits. The compile check (`chapcheck.sh a5e chapter_igood chapter_mass_bound_volumes chapter_normalization`, second run) reports no errors, no overfull boxes and no undefined references. The only message is the ignorable Underfull (badness 1783) in section_joint_curve_model_spaces. On the first run there were transient undefined references (`lem:auxiliary-slice-envelopes`, `eq:diffuse-residual-local`). These are new labels in files of r5g12/r5g13, and they resolved on the second run.

## Counts checked
- **r5g11:** 10 hypothesis removals or scope changes, 16 duplicate removals or citation replacements, 3 simplified proofs.
- **r5g21:** 7 hypothesis removals, 9 duplicate removals or recap replacements, 5 simplified proofs.

## r5g11: priority items
- **`lem:divisorial-adjoint-model` and the forward citation of `prop:logarithmic-product-model`.**
  - I checked the identification explicitly. Under w=1/z, ℓ=1/(1+|z|²) becomes r(w). With a=d=1, b=2 and κ=ω₂ we get θ=2ω₁+2ω₂, η=β, K=2, R=1 and C_*=2log2. The case |z|²≤1 gives 0 = W(x)−2χ(x) for x≥0. For x<0 the formula gives −x+2log2−2log(1+e^{−x}) = x+2log2−2χ(x). The smaller-background range (1/2,1) contains 3/4.
  - There is no circularity. The proof of `prop:logarithmic-product-model` uses only curve envelopes, slicing and ordinary-type invariance.
- **Constant b in sec:logarithmic-model-selection.** No proof in that section uses nonconstant b; I checked the proposition, `lem:logarithmic-greatest-solutions`, `thm:moving-logarithmic-selection` and `cor:logarithmic-critical-order`. Nonconstant b is needed only for the non-Gauduchon claim, and it is now stated in subsec:singular-product-adjoints. The example with b=2+t is nonconstant.
- **`cor:logarithmic-critical-order` via `thm:divisorial-type-thresholds`.** The hypotheses hold: θ is Hermitian, the residual η is positive, the section is Z₀ with weight d, sup ψ=0, dV=dW, and f is continuous and positive. `prop:individual-normalizer-lp` gives b_η=c_η, and c_η(f)=c₀ because w₀ is a bounded solution.
- **`prop:divisorial-residual-adjoint`.**
  - `thm:ordinary-divisor-normalization` applies to O(1) with the FS metric (curvature ω₁), weight 1 and residual β>0. It is a forward citation, but not circular.
  - The formula for B is differentiable with derivative −∫G dν_F, so `prop:normalization-directional` gives the singleton.
  - The Gauduchon uniqueness argument (closed form gives a constant multiplier) is correct in all three places it is used.
- **`eq:divisorial-cutoff-bound`.** Its only in-book `\eqref` reads correctly. ψ∈PSH(X,ω) with sup ψ=0, and pole sets may be omitted in capacity convergence.
- **δ>0.** All bounds are uniform in δ: λ∈[0,1), A_δ≥ω₁+ω₂, λ(1−λ)≤1/4. P_δ>0 for δ>1.
- **`prop:normalization-dual-entropy` (now "X Kähler, θ closed").**
  - The new scope is θ closed semipositive big on a Kähler X. Mass constancy on the ordinary type comes from SGPT.
  - The rewritten Jensen and ±th argument is correct, and absolute continuity of A_φ(F) holds by `thm:normalization-measurable-adjoint`.
  - The mass-quotient reuse is fine: with C(X) tests, Riesz representation concludes.
- **dV(X)=1 removal.** Neither the L^q lower bound nor the Gauduchon trace bound, `lem:entropy-variational`, `prop:entropy-mass-extrema` or `prop:normalization-distance-dual` uses it. The n=1 case is handled by Ent ≥ −log dV(X).
- **`thm:divisorial-type-thresholds`.**
  - GT01 Thm 3.5 applies on coordinate balls: the operator is uniformly elliptic, has c=0 and a is C².
  - The sup bound follows from `thm:normalized-compactness` applied to w−sup w.
- **Other changes, all correct:**
  - k≥1 in `ex:projective-divisor-threshold-loss`: the binomial expansion holds for k=1.
  - t_min removed: p_*+δΣ⊂K_t for all t≤t_max, and the derivative bound is monotone on (0,t_max].
  - n≥2 now sits only on the blowup case and the two subsections that use it. The P¹ case is fine: the inradius of δΣ is δ/2.
  - `prop:psh-descent-modification`.
  - `lem:one-sided-divisor-correspondence` in the projective example: earlier in reading order, hypotheses satisfied.
  - `cor:geometric-adjoint-stability` now reduces to `prop:normalization-distance-stability`: the H bound follows from the B bound by taking suprema.
  - `cor:divisorial-envelope-equality`.
  - The BMP wording in chapter_igood (rule 4).

## r5g21: priority items
- **`thm:small-pole-envelope-residual` without positive lower volume.** No step uses it.
  - Step 1 needs only u−sup u ≤ p and p_m↑p, which holds by the definition of the envelope.
  - The remaining steps use the bound J ≤ v₊(ω) from BMP and `lem:small-pole-residual-invariance`.
  - The callers in section_diffuse_product_polar_obstruction use only the residual identity. Line 397 cites `thm:ordinary-envelope-volumes` separately.
- **`prop:model-volume-comparison-modulus` and `prop:model-lower-volume-modulus`.**
  - The stretch lemma needs only the lower volume of the maximum, which is ≥δ by monotonicity, and b^nD ≤ δ/2.
  - The case s=0 works with any t∈(0,1).
  - I checked every caller: the Cauchy and uniqueness consequences (limit in M_δ), `thm:model-volume-cauchy-completeness`, `thm:model-volume-capacity-convergence`, the chain metric, `cor:positive-ideal-metric-completion` (the approximants are ordinary models with L(p_j)→L(p)>0), `thm:analytic-approximation-curvature-error`, and `thm:two-sided-analytic-criterion`.
  - In `thm:two-sided-analytic-criterion`, η_j≤θ+h≤Ω, η_j is big because ε_j<κ/2, and the middle point p_j has L≥2^{−n}δ in both η_j and β_j. Removing the projection to models is valid.
  - The move of `prop:model-lower-volume-modulus` creates no earlier citations, and M is defined in its new section.
- **Ω≥θ+h and Ω₀≥θ₀+h₀.** Every use needs Ω≥β only for β≤θ+h, never for γ: `lem:positive-volume-stretch`, the bounds K on upper volumes, and η_j, β_j≤Ω for ε_j<1. In `lem:nearby-background-volume-comparison`, only vol_β≤v₊(Ω₀) is needed.
- **`cor:mass-bound-exact-trace` with Ω≥2θ|_Y.** This is equivalent to the old (Ω₀, Ω) hypothesis in both directions, regardless of the sign of θ|_Y. The ordinary-model property of q_j follows from `thm:restricted-analytic-envelope-limit` (P=P_I) and `cor:ordinary-preserves-i`.
- **Other changes, all correct:**
  - `prop:positive-volume-smaller-background` without θ≥0, since θ≤Cω for any smooth form.
  - The "as in the proof of `prop:relative-envelope-equality`" / "`lem:relative-obstacle-contact`" citations: the weights vanish on the contact sets, and the competitor combination is valid.
  - `lem:gauduchon-uniform-lelong`: it holds for any smooth form, and A_N>0 because the family is infinite.
  - The curve sections: volumes come from U=A−μ(Y), which holds for both volumes; the polar and atomic closedness arguments are in `cor:curve-model-completeness`; and the proof of `thm:curve-model-capacity-convergence` works for big σ because T_p=σ+dd^c p≥0 has mass A_σ.

## Problems or proposals (none in my files)
1. **Stale history text (chapter_history.tex, to be applied by the coordinator).** These are as proposed in r5g11 §7 and r5g21 §7, and I confirm each one is needed:
   - **l.555:** after the moved label, "alternatively, the cutoff in \eqref{eq:divisorial-cutoff-bound} can be smoothed explicitly, which makes its estimate a direct Stokes calculation for distributions" now points at the capacity-tail display. Replace "; alternatively, the cutoff … for distributions." with ".".
   - **l.569:** "maximality of the coefficient in the full prescribed class follows instead from greatestness of the positive-exponent solutions" → "maximality of the coefficient in the full one-sided class is the case of \cref{thm:divisorial-type-thresholds} with residual form $\eta$".
   - **l.575:** "A uniform submean bound identifies" → "A uniform $L^1$ bound identifies".
   - **l.449:** "When the pole set is compact of Hausdorff dimension zero and the lower volume is positive, \cref{thm:small-pole-envelope-residual} shows" → "When the pole set is compact of Hausdorff dimension zero, \cref{thm:small-pole-envelope-residual} shows".
2. **Observation only, no action needed:** in `countable-divisorial:positive-mass`, the profile ⇒ v∼_I u step now rests only on the external projective valuative characterization (DX22, sourced in history). The deleted in-book route went through `thm:local-i-inputs` and surface blowup factorization. Both routes are valid.
