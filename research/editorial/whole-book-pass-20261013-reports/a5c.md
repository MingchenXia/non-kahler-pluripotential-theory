# Audit a5c (r5g06, r5g07)

## Verdicts
- **r5g06: CORRECT AFTER FIXES** (one punctuation fix).
- **r5g07: EDITS CORRECT.**

## Scope checked
- **r5g06.** 17 hypothesis removals or weakenings, 9 duplicate removals or citations, 6 simplified proofs. I also checked the statement concisions and the full math diff of all 18 changed files.
- **r5g07.** 10 hypothesis removals, 13 duplicate removals or citations, 4 simplified proofs. I also checked the concisions and the full math diff of all 13 changed files.

For each change I opened the cited targets and every caller.

## Priority items (all correct)

### r5g06
- **thm:lp-uniform-compactness from prop:capacity-square-one-sided-stability.** The proposition is now stated for L^∞ potentials, and that is enough: thin-sublevel-capacity and backwards-capacity are stated for bounded potentials, and every step of the proof is pointwise.
  - The hypotheses hold: sup u_k = 0, −H ≤ u_j ≤ 0, and A = C_p·B comes from cor:lp-capacity-square.
  - The Hölder step ∫|u_j−u_k|F_l ≤ (2H)^{1/p} B ‖·‖_1^{1/p'} is correct, and so is the resulting exponent 1/((6n+1)p').
  - It is not circular: the proposition uses only lemmas of the same section, modified comparison and eq:global-capacity-tail. The section has been reordered, and the citation is now backward.
- **Concave sections.** Removing n ≥ 2 is fine.
  - At n = 1, Γ = (0,∞) and f_∞ = ∞. The Green-kernel and contact-set arguments, thm:tw-smooth, thm:lp-potential-estimate and ρ₀ = 1 all work in that case.
  - Removing f ∈ C⁰(Γ̄) and f = 0 on ∂Γ is fine. The new tangent-line argument at tA_U is valid: tA_U is admissible because Γ is a cone, and F > 0 there. The set K is closed using only continuity of f on Γ.
  - The concave results are not cited outside the two sections; chapter_history makes no n ≥ 2 claim.
- **uni-thm:threshold, now for C^{1,1} potentials.** The only input is uni-thm:anchors, which is stated for C^{1,1} potentials with A, B ≥ 0 almost everywhere and continuous f. The sharpness examples are smooth, so they still apply.

### r5g07
- **The two deleted Sobolev statements, whose labels and index entries now sit on hessian:joint-decreasing-products.** The surviving theorem implies everything the old ones said:
  - with p = 1 and a decreasing weight, it gives the weighted convergence; the trace version follows because T is smooth;
  - with p = 2, it gives symmetry and convergence of D₂, convergence of Q₂, and measure coefficients when m > 2.

  Its proof never used the deleted results. The only remaining caller is chapter_history:322, which still resolves.

  The obstruction example now computes D₂ directly. I checked that computation: dd^c g_δ = ½ g_δ'' α_j, and Θ = dd^c u is d- and d^c-closed, so dd^c(gΘ) = dd^c g ∧ Θ. Q₂ is defined in bounded_currents.
- **hessian:bounded-nonvanishing from hessian:strict-bounded-domination with c = 0.** This is not circular: bounded-nonvanishing is cited nowhere in the book except chapter_history. The citation is forward, and the placement proposal (move it next to strict-bounded-domination) is sound.
- **Merged penalty squeeze (eq:hessian-penalty-squeeze).** The upper-test argument is valid for bounded upper semicontinuous admissible u:
  - x_N exists because u is upper semicontinuous;
  - polarized Gårding positivity gives (N+1)d_N ≥ σ_{m−1} ≥ d_N^{(m−1)/m}, and the bound E_N + 2M_N/N follows.

  Both the squeeze lemma and the continuous obstacle envelope cite it correctly.
- **smooth-torsion case merge.** hessian:deleted-newton applies for 1 ≤ q ≤ m−1 ≤ n−2 (the chapter fixes m < n). At q = 0, B_ij = D_i = 1. The identity ΣD_i = (n−q)S_q holds for every q.
- **Liouville via thm:stw-cone-liouville.** I went through every step of the STW proof with C_{n,m} in place of the STW cone, and each step goes through:
  - unitary invariance and translations;
  - A_ε ∈ C_{n,m}, because v_ε H(v_ε) lies in the cone and convolution keeps it there;
  - A_ε + B_ε − cI lies in the cone, because the cone is stable under adding nonnegative matrices;
  - h is admissible on D by convexity;
  - h_δ has Hessian in the interior;
  - the base case is n = m (plurisubharmonic), and dimension reduction uses S_j(A⊕0) = S_j(A).

  The cited section is in chapter_smooth_equations, which comes earlier in the book.

## Other checks (all correct)
- **r5g06.**
  - The label moved from prop:classical-scalar-uniqueness lands on prop:vanishing-exponent, which covers the old statement: the density f = Bⁿ/dV is continuous and nonzero by cor:bounded-mass-positive.
  - The deleted Gauduchon-surface corollary is covered by uni-cor:dense-lowdim.
  - The Hopf proofs now cite lem:hopf-basic-potentials(3), and the n = 3, a = b = 1 case matches chapter_hopf's ω = α + β; the factor 6 is correct.
  - The positivity argument for the background ω₀ + dd^c ρ in subsec:numa-positive-background lists the properties it uses. Those properties are satisfied in the quadratic and analytic examples; in the analytic one, x(−r) = y(r) holds because f_*(1−t) = f_*(t) and S_* is even.
  - The converse in the Guan–Li equivalence now goes through prop:comparison-forces-mass and thm:mass-invariance-characterization.
  - B₀ > 0 and the removal of "F bounded" are fine: finiteness of ω_uⁿ is enough to subtract in the localization step.
  - Making κ even matches cor:numa-third-solution, which already reads correctly.
- **r5g07.**
  - The merged absorption lemma: I recomputed its constants (7/8, 84, q²/4) and they are right.
  - M, B > 0 and δ > 0 are enough; τ = (M+1)^{-1} works for any M.
  - Step 1 of thm:mass-invariance-characterization with j = n−q gives (2)⇒(1) of hessian:global-comparison-characterization.
  - The Green-kernel citation for eq:hessian-normalized-l1 is valid.
  - The new hessian-nonvanishing proof: the inequality (1 − mCs)Σ ≤ 0 is correct.
  - Further checks:
    - the CLN citation in local-smooth-bounds (its proof is local to U);
    - proper-variable-existence and proper-bounded-stability, with κ and L obtained by compactness;
    - the identity bounded = continuous measure via hessian:bounded-shifted-positive;
    - the torus example's mass formula n!(2 − mπ²t/(2n))B_n;
    - the definition of non-collapsing already contains θ ≥ 0.
- **Compile and vocabulary.** chapcheck.sh a5c on the four chapters is clean: no errors, no overfull boxes, no undefined references. The first run showed eq:hessian-penalty-squeeze undefined only because my private copy had not yet seen the new label. The only remaining warning is the allowed Underfull (badness 1783) in section_singularity_volumes_modifications, which is not one of these files. No workflow vocabulary appears in the assigned files.

## Problems found
1. **Fixed: section_modified_comparison.tex, proof of thm:bounded-strict-domination (line 92).** When r5g06 deleted "omitting the second restriction if v=0.", the display was left ending with a comma before "Let $m_\varepsilon$…". Change: `2\varepsilon\|v\|_\infty<-m/4,` → `2\varepsilon\|v\|_\infty<-m/4.`

## Notes for the coordinator (no error)
- chapter_history.tex still describes the deleted arguments at lines 311, 320–323 (the two-factor Sobolev argument) and 374–376 (bounded-nonvanishing via truncation). The replacements r5g07 proposed in its section 7 are accurate and should be applied.
- hessian:bounded-sobolev-quasicontinuity is now cited nowhere. This is harmless.
- The orphan file section_classical_scalar_uniqueness.tex can be removed. The alias labels prop:classical-scalar-uniqueness and cor:gauduchon-surface-uniqueness are not referenced anywhere.
