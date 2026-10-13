# a5h audit report (r5g18, r5g20)

## Verdicts
- **r5g18** (chapter_partial_bergman, 19 files): **EDITS CORRECT**. I made no edits. One redundant hypothesis remains (item 1 below), and two history sentences now read oddly (item 2).
- **r5g20** (chapter_bott_chern_loci, chapter_lck, 15 files): **EDITS CORRECT**. I made no edits.

## What was checked
- **r5g18**: 14 hypothesis removals, 9 duplicate removals, 5 simplified proofs.
  - Hypotheses: θ closed (birational envelopes); B connected and q≥1; a_j rational→real; rationality of a (Hopf point); θ>0, B Kähler and r≥1 (horizontal center); β>0→β≥0 with ∫β^q>0 (merged band theorem, modified base, exact corollary); B Kähler and f≥1 (band); polydisk avoiding the other divisors (band, modified base); e≥1→e≥0; r≥1 in thm:optimal-growing-jet-range.
- **r5g20**: 3 statements with 7 removed hypotheses, 7 duplicate removals, 5 simplified proofs.
  - cor:divisorial-exponential-completeness (4 hypotheses); torus 0≤r≤n; thm:lck-vaisman-volume normalization.

## Priority items (all correct)
**prop:descended-kernel-limit.** The proof is complete:
- isometric descent of the norms and Gram matrices;
- lem:kernel-codimension-comparison for the TV identity and the bound on the functionals;
- thm:fujiki-partial-kernel-limit and cor:fujiki-partial-determinant on B with the identity modification. Their hypotheses (B compact, connected and Kähler, q≥1 from sec:partial-submersion, θ=c_1(A,h_A), positive mass of ψ) are all in force;
- continuity of lifting.

Both applications satisfy its hypotheses:
- thm:isolated-pole-kernel-limit: W_m is identified by lem:smooth-center-multiplier-ideal, which holds for real coefficients, and the defect is O(m^{q-1}).
- cor:horizontal-center-kernel-limit: thm:horizontal-center-descent gives the mass and the defect.

There is no forward or circular citation.

**Merged band theorem.** I checked every step for N divisors:
- the ideal is O(-ΣL_{m,i}D_i), by SNC coordinates, Fubini and generic points;
- the lower inclusion;
- the upper inclusion: one polydisk per divisor suffices, because shrinking around a point where g(0,t)≠0 makes the coefficient a unit;
- the restriction chain, with lem:linear-range-section-bound applied with F_j=O(-D_j)|_{D_i} and 0≤n_j≤mc_j;
- the case q=1.

Every \cref of thm:fiber-integrability-band, thm:crossing-fiber-integrability-band, cor:semipositive-fiber-band, lem:finite-family-section-bound and lem:linear-range-section-bound still reads correctly in the section files: crossing, modified base, semipositive, exceptional, two_point and horizontal center. The coordinator has already updated chapter_research_program (current l.324–330, including the old "all three band criteria" sentence). The history file is in item 2.

**β≥0 with ∫β^q>0.** Strict positivity was used only for the mass. MA_θ(ψ)=β^q follows from locality and the fact that the non-pluripolar product puts no mass on divisors, and it needs neither Kähler B nor β>0. The only remaining strict positivity is in the r<f construction, which assumes it explicitly. The examples with β≥0 (exceptional, two_point) satisfy the new hypotheses.

**Hopf point.** Rationality is now used only through lem:analytic-ideal-dominance in the two envelope identities. The binomial kernel, the potential limit and both measure formulas hold for all real 0<a<1.

**Birational envelopes with θ not closed.** prop:psh-descent-modification, thm:hermitian-partial-i-envelope (defined for any smooth θ) and thm:arbitrary-extended-ma all apply. The MA^ext pushforward is correct. Both callers (thm:fujiki and the modified base) have finite mass.

**e=0.** I rechecked: Hartogs, the orders j, ψ_d with d=δ=c, the residual (k-c)α+cγ, and the mass k^q−c^q.

**Four-point file.**
- The new order has no forward reference and no circularity: the restriction-image theorem and its corollary do not use the nonextension theorem.
- The coefficient comparison is right. In the frame w^{-1}s_ℓ⊗f^*e_B we have ψ_*=log|w|^2+O(1). Together with φ_0=½log|w|^2+O(1) this gives ½log|w|^2≤log|w|^2+O(1), which fails as w→0.
- lem:four-point-variable-conics at a=2 gives everything the deleted lemma stated: the equation, the determinant −a(a−1)t/4 and the charts.

**Min-Lee examples on H_n.**
- Φ, dd^cρ and Ψ all scale by e^{-2} under z↦e^{-1}z, and the Lee period is −Δlog Φ=2.
- e^{-u}ω=dd^cρ/ρ=α_n+β_n=ω_n.
- The spectra do not depend on the scaling.
- The radial subsection is consistent with sec:hopf-all-dimensions: r is defined modulo 2, the fiber β-area is 2, ∫α^m∧β=2, and the identities dβ and d^cβ check out.

**ex:lee-calabi-eckmann.**
- prop:calabi-eckmann-endpoint, which comes earlier in the book, gives a compact threefold X_τ diffeomorphic to S^3×S^3 with a principal elliptic fibration π. Hence H^1=H^2=H^5=0, and α=π^*(ω_1+ω_2) is nonzero, semipositive and exact.
- prop:lee-strong-obstruction then applies.
- The family A<0<B_0 no longer contains the old τ=i (A=0). The example now asserts the properties for the proposition's family, and both callers still read correctly.

**cor:divisorial-exponential-completeness.** The proof uses only the equation on M and the three bounds; prop:divisorial-normal-length needs only a smooth positive T on M with p≤2. Its callers are ex:critical-complete-divisor, which states L^1 and q>1 itself, and section_non_kahler_geometry l.100.

**Torus, 0≤r≤n.**
- r=0: K=V and H=X. The Fourier argument gives u constant, and the diameter √t·diam(X,κ) tends to 0.
- r=n: K=0 and H is a point, and the nonrigidity and no-collapse arguments work.
- The boundary-of-the-nef-cone claim is now stated only for r<n.

**thm:lck-vaisman-volume for any invariant μ.** cω has the same Levi-Civita connection and Lee form, its Lee and anti-Lee fields are scaled by c^{-1} (so invariance is unchanged), and τ↦τ/c. Both rescalings preserve the hypotheses and map solutions bijectively. Uniqueness does not use the normalization. The statement "Killing dual implies parallel" placed after def:lck is correct.

## Problems and proposals (not edited)
1. **Redundant hypothesis.** `section_horizontal_center_constraints.tex` l.111, cor:horizontal-center-kernel-limit. α=θ−cΘ_Z is closed and >0, so B is automatically Kähler.
   - Proposed: "Assume that $B$ is K\"ahler. Then $\varphi$ satisfies" → "Then $\varphi$ satisfies";
   - and in the proof, prefix "Since $\alpha$ is a K\"ahler form, $B$ is K\"ahler.".
2. **`chapter_history.tex`.** Both labels now point to the same theorem cited at l.652.
   - l.654: "\Cref{thm:crossing-fiber-integrability-band} extends this argument to finite families of divisors with simple normal crossings. The calculation of the ideal on the base uses separated normal coordinates, and" → "For finite families of divisors with simple normal crossings, the calculation of the ideal on the base in \cref{thm:crossing-fiber-integrability-band} uses separated normal coordinates, and".
   - l.658: "\Cref{cor:semipositive-fiber-band} separates the curvature requirements in these proofs:" → "In \cref{cor:semipositive-fiber-band,thm:modified-base-fiber-band} the curvature requirements are separated:".
3. **`chapter_history.tex` l.759** (r5g20). I endorse r5g20's proposed replacement (deduction from thm:four-point-metric-restriction-image and lem:four-point-variable-conics); I checked that it is accurate.
4. **Minor, pre-existing.** lem:kernel-codimension-comparison now admits q=0, while sec:partial-selected-space defines the normalization only for r≥1. It is harmless, because every use has q≥1.

## Compile check
`chapcheck.sh a5h chapter_bott_chern_loci chapter_lck chapter_partial_bergman` (second run): no errors, no overfull boxes and no undefined references. The only message is the ignorable Underfull (badness 1783) at lines 759–763. The first run showed prop:descended-kernel-limit undefined only because my private copy was fresh.
