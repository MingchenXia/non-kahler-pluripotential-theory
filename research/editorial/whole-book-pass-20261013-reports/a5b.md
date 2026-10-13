# Audit a5b (reports r5g05, r5g14; base 1fece9c)

## Verdicts
- **r5g05**: EDITS CORRECT.
- **r5g14**: CORRECT AFTER FIXES (3 small local fixes, below).

## What I checked
I checked every diff and the full math diff of all 34 files. I reread each changed statement and its whole proof, opened every newly cited target and checked its hypotheses, and grepped all callers of every changed label.

- **r5g05**: 8 hypothesis removals or generalizations, 9 duplicate removals or citation replacements, 3 simplified proofs.
  - **Priority 1: generalized `lem:hopf-small-defect`.** I redid the estimates for all heat times ε ≤ η^{1/η²}.
    - Step 2: λ = log(1/ε) ≥ L/η², and q_0² ≤ 2λ, so q_0²·ε·e^{q_0} ≤ e^{−λ/4}.
    - Step 4: the integrals ∫_{√L}^∞ do not depend on q_0.
    - Step 6: the error Ce^{−1/(5eη)} is below e^{−1/(10eη)}/4 once ηx_* ≤ 1/(10e).
    - The constants depend only on κ, χ, ϑ.
  - **Priority 2: new `lem:hopf-base-correction`.**
    - The formulas for g′ hold on both sides of −1/2.
    - m_0 ≤ μ(−2)/2 ≈ 0.06 < 1/8, which is what the case x ≥ 0 needs.
    - Positivity of Q[V] holds on [0,b], on (−2,−1) and elsewhere.
    - The existence remark is valid: r ≥ 0 because the approximation plus the constant exceeds d_η ≥ 0.
  - **Its three users, rechecked under the new ε:**
    - `thm:hopf-unbounded`: ηx_* = O(√(ηL)).
    - Rotational proof:
      - ε = e^{−cη^{−3}} ≤ η^{1/η²}, and ηb, ηx_* → ℓ.
      - C′ and m_0 do not depend on c.
      - |g| ≤ m(b+5/2).
      - In `thm:rotational-infinite-weighted-measure`, K does not depend on c, so Kℓ < m_0 can be reached by shrinking c. Then m → Kℓ < m_0 also gives μ+g′>0 and g″+μ(1−μ) ≥ 0 in `lem:rotational-critical-concentration`.
    - `thm:hopf-all-dimensional-unbounded`.
  - **Priority 3: `thm:stw-volume` with γ only Hermitian.** No step uses the Gauduchon condition:
    - the C⁰ bound (Fredholm adjoint measure of L);
    - `prop:gaud-volume-linearization`;
    - openness, via `prop:smooth-dependence` with μ_u^γ in place of μ_u;
    - the second-order, Liouville and gradient estimates (already stated for Hermitian γ);
    - `lem:stw-higher-regularity`, the variation results, `ex:gaud-volume-surface` (needs only γ_0 Gauduchon), and the chapter_lck citation.

    The only use was the remark in `prop:gaud-volume-form-adjoint`, which is now restricted correctly.
  - **Priority 4: continuous nonincreasing weights.** Continuity gives quasi-continuity of W(−u) and Θ_{T−δ} → Θ_T. "Tending to zero" and C¹ are used nowhere. √T·W(T) ≤ √T_0·W(0) replaces "finite on compact intervals". The closing sentence about `prop:general-damping-weights` now restores that proposition's own C¹ and limit-zero hypotheses.
  - **Other changes checked:**
    - η > 0 in `lem:hopf-fiber-potential`: everything is linear or quadratic in η, and eq:hopf-vertical-positive still holds.
    - `lem:hopf-basic-potentials`(2) now cites `prop:psh-descent-submersion`; the citation fits.
    - The group G is that of `lem:rotational-capacity-smoothing`, which comes earlier in reading order.
    - The removed v_+(Ω)=+∞ clause is covered by `cor:hopf-all-metrics-unbounded` (n=3, every Hermitian h). Nothing cites the clause.
    - The cuts to `thm:rotational-depth-core` follow from u_η ∈ R and the global bound. They are compatible with its use in `cor:rotational-necessary-weights`.
- **r5g14**: 5 hypothesis removals, 12 duplicate or recap removals, 5 simplified proofs.
  - **Priority 1: `thm:hopf-projective-exact-trace` for every smooth Ω ≥ aα.**
    - q*w_a ∈ PSH(Y,aα) by `lem:hopf-basic-potentials`(1) with b=0. It is a competitor for every such Ω, so the family is nonempty.
    - The hypothesis of `thm:restricted-analytic-envelope-limit` holds anyway, because Ω ≥ aα ≥ Cα = θ|_Y with θ = p*(Cω_FS).
    - The reordered invariance argument now uses q*w_a only after it has been shown to be a competitor.
    - C>0 suffices for `thm:kahler-target-exact-trace` (Ω_0 = Cκ Hermitian).
    - In `ex:hopf-point-trace` with a=1, the residual form is η, η^d = 0, and the formula gives 0, consistently.
  - **Priority 2: shortened `prop:original-background-trace-majorant`.** With Ω=θ|_Y, h=ω|_Y and δ_m=ε_m, the hypothesis holds. Both callers read correctly; in chapter_nonclosed_bclasses, "with Θ in place of θ" gives T_{Θ|_Y} = T_θ.
  - **Priority 3: `prop:envelope-system-raw-volume-failure`.** The zero system does not depend on h, so "for every h" holds.
  - **Priority 4: Moishezon clause in `lem:kahler-modification-bounded-mass`.** It is correct (X connected, hence irreducible). Both proofs that cite it are fine.
  - **Priority 5: `prop:ruled-intrinsic-ideal-orders`.**
    - The small-curvature hypothesis holds via U_{L′}∘pr_Y.
    - σ_Δ = bG_p∘pr_Y.
    - Y ⊄ D_X.
    - The citation comes earlier in reading order.
  - **Priority 6: `sec:gauduchon-section-degree`.** See fix 3.
  - **Simplified proofs:**
    - ⟨S⟩=S: q ∼ u_0 with pole set D, and 1_D S_0 = 0.
    - The blowup compactness argument is valid: E is a curve, ker π*h = TE, and −η > 0 on TE.
    - BC Step 3: B−B′ ∈ H_γ has the two decompositions (B−B′)+dd^c0 and 0+dd^c(f−mean); uniqueness uses the Gauduchon integration.
    - The forward transform is already usc by `thm:hermitian-legendre-usc`.
    - The Cartier step needs no positivity on Z′.
    - `lem:curvature-rank-fixed-line-twist`: the smooth irreducible H_j are connected.
    - `ex:exceptional-trace-with-exact-potential`: C ≥ a.

## Problems found and fixed (all in r5g14 files)
1. **section_nonclosed_ruled_trace_masses.tex**, proof of `prop:ruled-intrinsic-ideal-orders`. The text cited "the formula I(sσ_Δ)=O_X(−⌊sb⌋D_X) from its proof", meaning the proof of `prop:small-curvature-intrinsic-traces`. That proof only gives O(−⌈sb⌉D) ⊆ I ⊆ O(−⌊sb⌋D), which is not equality when sb is not an integer.
   - Old: "Its first identity and the formula $\mathcal I(s\sigma_\Delta)=\mathcal O_X(-\lfloor sb\rfloor D_X)$ from its proof give the ambient ideals,"
   - New: "Its first identity and $\mathcal I(s\sigma_\Delta)=\mathcal O_X(-\lfloor sb\rfloor D_X)$, which is \cref{lem:smooth-center-multiplier-ideal} in codimension one near each point of $D_X$ when $b>0$ and is trivial when $b=0$, give the ambient ideals,"
2. **chapter_divisorial_models.tex**, proof of `thm:trace-divisorial-current-budget`. Deleting the sentence that cited the corollary left "as in the proof of that corollary" without an antecedent.
   - Old: "as in the proof of that corollary"
   - New: "as in the proof of \cref{cor:restricted-analytic-divisorial-bound}"
3. **chapter_sections.tex**, `sec:gauduchon-section-degree`. The new reminder points to `sec:convex-bundle-norm-obstruction`, but chapter_gauduchon assumes n ≥ 2 there, while this section explicitly allows curves.
   - Old: "of \cref{sec:convex-bundle-norm-obstruction}; it does not depend on the smooth metric on $L$."
   - New: "of \cref{sec:convex-bundle-norm-obstruction}, with $\gamma^0=1$ when $n=1$; as there, Stokes' theorem shows that it does not depend on the smooth metric on $L$."

## For the coordinator (not edited)
- **STW attribution.** I checked STW17 (arXiv 1503.04491), Theorem 1.4: it assumes "a Hermitian metric α0 and a Gauduchon metric α". The book's `thm:stw-volume` now states more than the attributed theorem, so r5g05's proposed addition to chapter_history.tex:178 is needed: "The proof given here does not use that the auxiliary form $\gamma$ is Gauduchon."
- **Outdated history sentences.**
  - chapter_history.tex:59 ("The faster initial time … proved at that scale") and :635 ("in degrees one and two"; "transverse radial integral") are now inaccurate.
  - I endorse the replacements proposed in r5g05 §7 and r5g14 §7.
  - For :635 the replacement could add "with \cref{lem:smooth-center-multiplier-ideal}".
- **Cross-part duplicates.** The duplicates and placement items listed by both reports are plausible. I made no changes for them.

## Compile check
`chapcheck.sh a5b` on the 9 chapters, after the fixes: no errors, no overfull boxes, no undefined references. The only message is the allowed Underfull (badness 1783) in section_hopf_transverse_recovery.
