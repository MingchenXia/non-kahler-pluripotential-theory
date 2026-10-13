# Audit a4a (reports r4g01–r4g06 and coordinator edits)

## Verdicts
- **r4g01:** EDITS CORRECT.
- **r4g02:** EDITS CORRECT.
- **r4g03:** EDITS CORRECT.
- **r4g04:** CORRECT AFTER FIXES (2).
- **r4g05:** EDITS CORRECT.
- **r4g06:** CORRECT AFTER FIXES (2).
- **Coordinator edits 1–3:** CORRECT.

## What was checked
About 50 corrections and 15 renamings, all re-derived against the diff from `e2cac72`, plus a mathdiff3 scan of every file in the six reports.

The renamings were: t→τ; M→m, D→Ω, M→c; Q_T→Θ_T, E_j→S_j, H_r→N, c_1→c′; μ→π, MA^ext→MA; π→p, p→g, ξ,η→ξ₁,ξ₂, q_j→p_j. All are complete, with no leftovers and no new clashes. No labels were lost. Callers of strengthened statements, such as `curve-map:potential-descent` (which now also reflects the order), still have what they need.

## Coordinator edits
1. **`thm:bounded-hermitian-smoothness`: correct.**
   - The lemma applies with v=a_j and M′=sup|u|+sup_jδ_j, because |a_j|≤sup|u|+δ_j and G is smooth on X×ℝ. Both a_j and b_j are smooth with ω_{a_j}, ω_{b_j}>0.
   - The b_j are bounded by |b_j|≤‖G‖_{C^0}, and Δ_g b_j is bounded. The W^{2,q} estimates then give uniform C^{1,α} bounds.
   - G(x,a_j) is uniformly C^{1,α}, so the right-hand side b_j+G(x,a_j) is uniformly C^α.
   - With ε_j=‖G(x,a_j)−G(x,u)‖≤C‖a_j−u‖→0, one has e^{-(b_j+ε_j)}ω^n_{b_j+ε_j} ≤ e^{-u}ω_u^n ≤ e^{-(b_j−ε_j)}ω^n_{b_j−ε_j}. The direction in `cor:bounded-exponential-comparison` (λ=1) then gives |b_j−u|≤ε_j.
   - The Evans–Krylov step uses the estimate with Hölder x-dependence, as `cor:classical-higher-estimate` already does. Arzelà–Ascoli and passing the metric bounds to the limit are fine.
2. **Skoda sentence: correct.** [DemAM11, Lemma 5.6] is Skoda's lemma, cited the same way in four other files. ν(tq)=0<1 gives the integrability.
3. **λ_j absorption: correct.** Demailly's loss is min(λ_k,c)u+ε_kω ≤ (C_0λ_k+ε_k)ω, using λ_k≥ν≥0 and u≤C_0ω. With C≥C_0, the functions λ′_k=λ_k+ε_k/C are continuous, decrease to ν(T,·), and give T_k≥γ−Cλ′_kω. Dini's theorem still applies when ν≡0.

## Problems found and fixed
1. **`section_hopf_rotational_damping.tex` ~l.298 (r4g04).** "Since t≥ε everywhere" is false: for x>(2q_0+½)/a one has |q|>q_0, so t<ε. The original "where the cutoff is nonzero" was right.
   - Fix: "Where the cutoff ϑ(q) is nonzero, 0<q≤q_0, so t≥ε, and … give F_η≥−2cη^{-2}−Cη. Multiplication by ϑ(q)∈[0,1] preserves this lower bound for Z_η, including where F_η is positive, and Z_η=0 where ϑ(q)=0."
2. **`chapter_hopf.tex:6` (r4g04).** "On a threefold it has only a linear and a quadratic term" leaves out the constant ∫ω³ of `eq:mass-expansion`.
   - Fix: "On a threefold, apart from the constant $\int_X\omega^3$, it has only a linear and a quadratic term."
3. **`chapter_rays.tex:8` and `:231` (r4g06).** These now claimed the Hopf CAT(0)/saddle results "on scalar Hopf manifolds of dimension at least three". The book uses that term for general contractions (e.g. X_q in `subsection_flat_restriction_hopf_complements`), but proves the results only for H_n. This widened the scope; the author's original said "the Hopf background".
   - Fix at :8: "On the scalar Hopf manifolds (ℂⁿ∖{0})/⟨z↦e^{-1}z⟩, n≥3, …"
   - Fix at :231: "On the Hopf manifolds H_n, n≥3, of \cref{sec:hopf-all-dimensions}, …"
4. **`section_hopf_basic_perron.tex:145` (r4g06).** "bump function of (y, Re z)": in this section z denotes the coordinates on ℂⁿ, and the strip variable is called s at l.243.
   - Fix: "bump function of y and of the real part of the strip variable".

`chapcheck.sh a4a chapter_hopf chapter_rays`: no errors and no overfull boxes. The only message is the known bibliography `Underfull (badness 1783)`.

## Not edited (predates the review edits)
- **`preface.tex:27`.** "On the scalar Hopf manifolds of dimension at least three, the masses … are unbounded" has the same scope issue, inherited from the author's sentence. `chapter_hopf` now restricts this to e^{-1}. Proposed: "On the scalar Hopf manifolds $(\C^n\setminus\{0\})/\langle z\mapsto\mathrm e^{-1}z\rangle$, $n\geq3$, the masses …".
- **`chapter_trace_data.tex:8`.** "On a scalar Hopf manifold, …" should be checked in the same way. It is not in my files.
