# a5g audit report (r5g17, r5g19; base 1fece9c)

## Verdicts
- **r5g17: EDITS CORRECT.**
- **r5g19: CORRECT AFTER FIXES.** One citation fix: a proof cited the history section for a theorem that the main text also states.

## Counts checked
- **r5g17:**
  - 7 hypothesis changes: flat-divisor curvature (any S), flat-divisor order (dim n), and in the merged lemma constant rank → max rank, "θ nef" dropped and the singular-potential lower bound narrowed; also Hopf δ and the n=1 sentence.
  - 8 duplicate removals: the merged lemma, the two fixed-cone proofs, the zero-ruling ring, U non-splitting, the two ruled-residual proofs, the closing remark.
  - 3 simplified proofs.
- **r5g19:**
  - 13 hypothesis changes: ν probability; q≥2; unequal r_j; t_j→0; Σα_j=1; psef in α[-εω]; >0→≥0 twice; a,b≥0; the Kähler form in F^*[ω_Y]; "positive off D"; "semipositively".
  - 6 duplicate removals and 3 simplified proofs.

## Priority items, r5g17 (all checked)
- **Merged lemma.** `lem:nef-logarithmic-rank-comparison` now also carries `prop:nef-maximum-rank-comparison`, and the proof is complete.
  - k(B+εΩ) ≤ θ+εh ≤ K(B+εΩ) holds pointwise, so `prop:gaud-volume-elementary` gives the quotient comparison: the differences are semipositive, hence psef.
  - The closed nef formula applied to the Kähler form B+εΩ gives Σ_{j≤R} C(n,j) ε^{n-j} ∫B^j∧Ω^{n-j}, with a positive leading coefficient.
  - The modification part is fine: the rank-R set is open, so it meets the set where π is biholomorphic.
  - The edge cases B=0 and n=1 are fine.
- **Singular-potential form.** Before the pass, only the old fixed-cone proofs used it. I grepped every `\cref` of both labels, of the equation labels inside them, and of ψ_E, across the whole book including chapter_history and chapter_research_program. No current user needs it:
  - cor:flat-divisor-variational-order and cor:nef-variable-semipositive-generators need only (min f)B ≤ fB ≤ (max f)B;
  - history line 724 (rank-one bounds) needs the same;
  - the example uses only dd^cψ_E = [E] − H + Q.
- **History line 722** still describes the removed logarithm/constant-rank argument. I endorse r5g17's proposed replacement paragraph (report section 7) for the coordinator.
- **Fixed cones.**
  - cB_θ ≤ θ ≤ CB_θ holds, because each occurring coefficient a_i+b_if_i or c_i+d_ig_i lies in a compact subset of (0,∞) and absent ones vanish identically.
  - Ranks add over the factors. On a blown-up factor, H_i has rank m_i off E_i (less on E_i), κ_i = H_i+Q_i is Kähler (rank m_i everywhere), and Q_i has rank r_i.
  - So max rank B_θ = R(θ), attained off all E_i. Only the maximum is needed.
  - prop:nef-projective-modification-equality correctly applies the lemma's last assertion.
- **Zero-ruling ring.** The proof of thm:elliptic-extension-polynomial-ring uses the fiber-ring lemma only through:
  - the presentation (Step 1: the injectivity of c_+ ↦ P/c_- needs only P ≠ 0 in a domain);
  - the lattice action (c_± ↦ b_λ^{±1}c_±, h and w fixed, u ↦ u+m(q_0h+Kw)).
  
  lem:elliptic-zero-ruling-quadric states exactly the same action, with P = h². Steps 2–3 use only q_0 ≠ 0 and the U-lemmas. So the citation is valid.
- **U non-splitting.** The new j-step argument (a′_{j-1} constant → zero → contradiction, using d>0 and a_j ≠ 0) is complete, and s=1 excludes a section with u-coefficient 1.
- **Ruled residual.**
  - Ω = β+dd^c f > 0 with Ω² = Vμ, so thm:gaud-volume-dual-formula gives V_μ(β) = V.
  - T = a^{-1}Ω is closed because g/a lives on the curve factor, hence it is the conformal Gauduchon metric.
  - d/ds β_s = −(dw_1+ew_2), and prop:gaud-volume-first-variation (n=2, β_s ∈ 𝒫) gives the stated sign.
- **Flat divisors in dim n.**
  - ∫_S B∧κ^{n-1} = ∫_D κ^{n-1} > 0, because B ∈ c_1(O(D)) and κ is closed. So B ≢ 0 and max rank = 1.
  - Rank ≤ 1 gives B² = 0, hence V_μ(B+εκ) = nε^{n-1}∫_Dκ^{n-1} + ε^n∫κ^n.
  - The bounds are ε^{n-1} from the lemma with R=1.
  - "fB not closed" needs ker B ≠ 0, which requires n ≥ 2, and that is stated.
  - The cutoff construction does not depend on dimension.
- **Smaller items checked:** prop:nef-strict-blowup-orders without γ_* (no later reference to γ_* or attainment), the Hopf δ ≤ 1−a with a ≥ 0, the n=1 case of the integer jumps, the holomorphic-convexity and projectivization moves (now defined before their first use), the flow notation (t from the radial section; flow time s), and all deleted remarks (none cited).

## Priority items, r5g19
- **prop:finite-map-zero (section_density_zero_geometry.tex).**
  - The deduction is mathematically correct. F|_V is finite, hence of generic maximal rank, so ∫_V(F^*ω_Y)^{dim V} > 0 for every V. Then prop:restricted-mass-bigness (X compact Kähler, class nef) gives bigness, Null = ∅, and Collins–Tosatti gives E_nK = ∅; thm:bc-non-kahler-locus then makes the class Kähler.
  - (a) Collins–Tosatti is not part of thm:bc-non-kahler-locus. It is, however, stated in the main text: chapter_bott_chern_loci.tex, section "Null loci and numerical restricted volumes", where the display E_nK(α) = Null(α) is given for nef and big classes on Kähler X as a recalled classical theorem. The main text already relies on it in eq:finite-restricted-null-union (section_finite_restricted_invariants.tex).
  - (b) Its hypotheses hold: X is compact Kähler and the class is nef and big.
  - So I did not restore the hypothesis. But the proof cited the history section directly, so I redirected it to the main-text statement:
    - **Fixed:** in chapter_bott_chern_loci.tex, I added `\label{sec:bc-null-loci}` after `\section{Null loci and numerical restricted volumes}`. This is a new label; nothing was renamed.
    - **Fixed:** in section_density_zero_geometry.tex (proof of prop:finite-map-zero), "By the theorem on nef and big classes discussed in \cref{sec:history-closed-loci}, its non-K\"ahler locus is empty" → "By the equality of the non-K\"ahler locus and the null locus of a nef and big class on a compact K\"ahler manifold, recalled in \cref{sec:bc-null-loci}, its non-K\"ahler locus is empty".
  - Optional for the coordinator: the history sentence in sec:history-closed-loci ending "uses the theorem \cite[Theorem 1.1]{CT15Loci} recalled above" could also name \cref{prop:finite-map-zero}.
- **prop:exceptional-density-obstruction.** "S is a smooth form" suffices. Off E, S = θ+dd^c u ≥ 0, so S is semipositive everywhere by continuity. With a bounded residual potential, S has no mass on E, so the new wording is equivalent to the old "extends smoothly".
- **Anisotropic, q ≥ 1 and unequal r_j dropped.** The q=1 case is fine (N_m = dm+1−k_m; the half-space reduces to a ray), and prop:anisotropic-homogeneous-center does not need unequal r_j.
  - t_j → 0 follows from H_j(t_j) = μ_j/m → 0 and H_j strictly increasing from 0.
  - Σα_j = 1 follows from V ~ Σ r_jμ_j ≍ k_m.
  - lem:smooth-center-multiplier-ideal (d=0, k=n, c = k_m+n−1) gives m_p^{k_m}.
  - prop:partial-kernel-submersion (ψ=0) applies: the base is connected and the fibers are compact and connected.
- **α[-εω] without psef.** prop:bc-gauduchon-compactness needs nothing (an empty family is trivially bounded), the nef ⇒ psef paragraph is now consistent, and the minimal-multiplicity section keeps its own psef assumption.
- **Others checked:**
  - Step 1 via prop:bmp-finite with C=1 (v_+(λ) = ∫λ^k by Chiose's theorem, or Stokes for k=1);
  - Cκ−η ≥ 0 (Step 2 needs only A ≥ 0);
  - ω+dd^c v_j ≥ 0;
  - a,b ≥ 0 in the elliptic section ring ("at most quadratic");
  - "positive off D" (det > 0 plus semipositive);
  - κ_ω through smooth strictly positive T ∈ 𝒢_ω (equal to Gauduchon powers, n ≥ 2);
  - W rational from Q rational;
  - the pencil shell remark;
  - ν(P²) in the tail bound.

## Compile and math diff
- `chapcheck.sh a5g chapter_bott_chern_loci chapter_gauduchon_variational_volume chapter_partial_bergman`, second run: only the ignorable Underfull 1783 (section_oeljeklaus_toma).
  - The first run showed `sec:bc-null-loci`, which is new, and `prop:descended-kernel-limit`, another agent's new label, as undefined; both resolved on the second run.
- `mathdiff3.py` over all changed files of both parts: every removed or added display is one of the listed changes; no factor, exponent or inequality was altered unintentionally.
