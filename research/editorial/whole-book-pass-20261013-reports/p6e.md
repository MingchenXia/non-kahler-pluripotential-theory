# p6e report: placement moves §11, §12, §16, §17 and coordination edits

## 1. Moves made

**§11 Cluster limits.** I cut the "Moreover…" sentences from the statement of `prop:greatest-normalized-threshold` and its last proof paragraph (section_threshold_subsolution_envelope). They became a new corollary, `cor:exponential-cluster-threshold-subsolutions`, in section_individual_exponential_equations, right after the proof of `cor:individual-positive-threshold-exponential` and before the paragraph "Since MA(v_λ)=…".
- Statement: for b_h(f)>0, every L¹ limit of v_{λ_j} with λ_j↓0 lies in 𝒮_f and therefore below Φ_f.
- Proof: the moved paragraph, plus one sentence citing `thm:normalized-compactness` for "v is h-psh with sup zero". The old proof had left this implicit.
- Repointed users: semipositive_exponential_limit l.41 and gauduchon_moment_equations l.46 now cite the corollary.
- Dependency check: the corollary cites `prop:greatest-normalized-threshold`, `cor:individual-positive-threshold-exponential`, `lem:density-subsolution-lone-closure` and `thm:normalized-compactness`, all earlier. Its users are both later (gauduchon_variational_volume). The proposition no longer cites anything later; its forward reference to the corollary on the exponential equations is gone.

**§12 Smoothing obstruction.**
- The lead-in sentence, `ex:gauduchon-current-smoothing-obstruction` and its proof (threshold_divisorial_geometry 1–15) moved to the end of section_gauduchon_linear_duality.
  - In the proof, "C²=−1 of \cref{ex:gaud-metric-blowup}" became "C²=−1 of the exceptional curve".
  - The old l.83 and the lead-in were merged into one paragraph that ends "…and the following example separates the two sets by a smooth closed form".
- The m_ω/κ_ω paragraph (16–22) went to section_smooth_cone_duality after m_h≤κ_h, replacing "The inequality can be strict, as … shows".
  - It is now: "The inequality can be strict. Let X, C, β_C and T_C be as in \cref{ex:…}, with the Kähler form there taken as h. Since …", followed by the display with h in place of ω.
  - I dropped its first sentence, which restated the definitions of m and κ already given there, and its closing "Thus extending…" sentence, which repeated "can be strict".
- threshold_divisorial_geometry now opens "The hypotheses of the next two corollaries…" ("We return to the general setting … of this section." removed).
- weak_gauduchon_duality l.88 ("as \cref{ex:…} shows") does not depend on location, so it is unchanged. It now cites backwards.
- Dependency check: the example cites nothing; 𝒢_ω and 𝒞_ω are defined earlier in the same section. Its users are weak_gauduchon_duality:88 (proof), smooth_cone_duality:37 and research_program:114, all later. The moved paragraph cites `ex:…`, `cor:gauduchon-threshold` and `prop:gauduchon-linear-compact-dual`, all earlier.

**§16.** I checked `cor:singular-exponential-order`: θ semipositive and big; v⪯u; u admits a smaller-background envelope; e^{−λu}MA(u) ≤ e^{−λv}MA(v) off the pole sets; conclusion u≥v. With θ=h, u=t, v=s these hypotheses all hold. A bounded t gives s⪯t and P_{h/2}(t) ≥ inf t, and off the pole set of s we have e^{−λt}MA_h(t) ≤ ν ≤ e^{−λs}MA^ext_h(s).
- The proof of `lem:bounded-exponential-supersolution` is now these two sentences plus the citation.
- The section's opening now says "the following case of \cref{cor:singular-exponential-order}" (was "consequence of strict domination").
- In continuous_potential_product_measures (Greatestness, l.236), `cor:singular-exponential-order` is now cited directly with the same short argument (H=h_0+κ is Hermitian).
- The lemma is still used by individual_exponential (twice) and radial_integrable_selection (twice), so it stays.
- None of my files' statements or proofs cites anything later (graph check), so the `\input` order in chapter_prescribed_equations is unchanged.

**§17.** `lem:affine-logarithmic-pole-barrier`, with its lead-in and `\index` entry, moved from affine_polar_obstacles to affine_local_strict_weights, just before `lem:relative-affine-zero-value`. The lead-in now reads "The pluripolar case of the next lemma uses functions of logarithmic growth with poles on a given bounded pluripolar set." It stays in the same subsection, so ℒ_1, θ_1 and χ are still defined. Dependency `lem:affine-projective-growth` comes earlier; its only users are l.25 (later) and history (prose).

## 2. Moves not made
None.

## 3. Coordination edits applied (each checked against the current statements)
- **(a)** chapter_prescribed_equations l.22: "with a projective space of dimension at least two," → "with a projective space,". The setting is Y=ℙ^k with k≥1 (zero_lower_mass_product_equations l.7).
- **(b)** gauduchon_moment l.46: "the additional hypothesis v⪯Φ_f of \cref{prop:lower-barrier-criterion}" → "the hypothesis v⪯Φ_f of \cref{thm:common-barrier-criterion}". semipositive_capacity_limit l.11: "We apply \cref{thm:common-barrier-criterion} …; its hypothesis u⪯φ …".
- **(c)** holder_reference l.38: replaced as proposed. The lemma's constant depends only on a bound for ‖ψ‖_∞, and the \widehat v_l are uniformly bounded.
- **(d)** horizontal_center: the "Assume that B is Kähler." sentence is removed. The proof now opens "Since α is a Kähler form, B is Kähler." Check: θ=c_1(A,h_A) and Θ_Z are closed curvature forms, so α=θ−cΘ_Z is closed and >0 on B.
- **(e)** radial_residual_regularity: the subsection is now titled "Products with a Hermitian factor". There is no label.
- **(f)** logarithmic_model_selection: the definitions of dist_chord and G are replaced by a reminder.
  - Normalizations agree exactly: the same formula |x₀z₁−x₁z₀|/(|x||z|), and ω_1 = κ is the mass-one FS form on ℙ¹. dd^c_xG=δ_z−ω_1 and mean zero are `lem:curve-probability-green-potential` for μ=δ_z, and G(x,[0:1])=log ℓ+1.
  - In the proof, the now-duplicate clause "; the Poincaré–Lelong formula and ∫log ℓ=−1 give its curvature and mean" is removed.
- **(g)** ideal_rounding: verified. For ℓ=(m−α,α), |z^α e^m|²_{h^m}=|Z^ℓ|²/|Z|^{2m}, and σ_0 is the probability FS form, so (projective-monomial-norm) on ℙ¹ gives α!(m−α)!/(m+1)!. The text now derives it from that equation and keeps the label and the beta integral, because x and its beta distribution are used again at l.123. I wrote "on ℙ¹" instead of "q=1" because q is a different parameter in that section.
- **(h)** warped_endpoint: "m≥2" → "m≥1" (l.7), and the example now begins "take m≥2, B=ℙ^m". I rechecked for m=1:
  - the balanced cofactor (γ=L^{-1}A+w, which is closed);
  - prop:warped-subtraction-profiles (points have d=2);
  - prop:warped-endpoint-closed-core (n=2, Demailly–Păun; ζ is a (1,1)-form on the curve);
  - eq:warped-closed-morse (P²−2P∧Q=2a_0W).
  Only the example needs m≥2 (for m=1, H(0)=∞).
- **Coordinator note**, chapter_prescribed_equations opening, checked against `thm:lower-mass-obstructing-measure` and the corollary: "Solvability of MA_h(u)=cμ … Without such a bound," → "If the masses of bounded h-psh functions have no positive lower bound, some probability measure μ with density bounded below by a positive constant admits no solution of MA^ext_h(u)=cμ; with such a bound, every nonzero finite non-pluripolar measure admits one (\cref{cor:positive-lower-mass-solvability} in \cref{chap:relative-finite-measures}). Without such a bound,". I wrote MA^ext because both results are stated with the extended operator for unbounded u.

## 4. Replacements needed in files I do not own
- **section_threshold_divisorial_constraints.tex l.38**: "The statement concerns $\mathscr C_\omega$, which can be strictly smaller than $\mathscr G_\omega$, as the next example shows." → "The statement concerns $\mathscr C_\omega$, which can be strictly smaller than $\mathscr G_\omega$ (\cref{ex:gauduchon-current-smoothing-obstruction})." The example no longer follows.
- **chapter_history.tex l.574**: "The full-product greatestness and coefficient in \cref{thm:continuous-potential-product-threshold} follow from singular strict domination through \cref{lem:bounded-exponential-supersolution}." → "… follow from the singular exponential order of \cref{cor:singular-exponential-order}." No other history sentence names a location I changed; l.150 is being handled by another agent.
- **chapter_gauduchon.tex opening** (optional, since it gains the example): after "although a smooth minimizing metric generally does not exist." add "On the blowup of $\mathbb P^2$ at a point, the normalized integration current along the exceptional curve lies outside this closure."
- **chapter_research_program.tex l.63** (optional): the phrase "their normalized cluster limits lie below … $\Phi_f$ of \cref{prop:greatest-normalized-threshold}" stays correct. It could add "(\cref{cor:exponential-cluster-threshold-subsolutions})".
- book.tex and preface: nothing.

## 5. Checks
- **chapcheck** (p6e, run 3 times on all 7 chapters): no errors, no overfull boxes, and no undefined or multiply defined references from my files. The remaining warnings come from concurrent work in other files: `lem:balanced-pluriclosed-closed` multiply defined, `chap:gauduchon-bundle-positivity` and `lem:nef-blowup-metric` undefined. There is also the ignorable Underfull (badness 1783) in oeljeklaus_toma.
- **Label graph**: rebuilt with a private copy of lg.py. No statement or proof in any of my 19 files cites a later label. The rebuild also reports 35 undefined references in preface, research_program, history and arbitrary_curve_product_metrics, all to labels other agents are moving.
- **mathdiff3**: run against HEAD before the coordinator's snapshot commit 9d04675 absorbed my edits, and against 099fd4b for the later ones.
  - The moved blocks match exactly: removed in envelope / divisorial_geometry / polar_obstacles, added in individual_exponential / gauduchon_linear_duality / smooth_cone (ω→h) / strict_weights.
  - The other math changes are the listed edits:
    - the new lemma proof;
    - the Greatestness argument;
    - the G reminder (dist_chord→d_ch) and the removed ∫log ℓ=−1;
    - "+α" in horizontal_center;
    - m≥1;
    - ℓ=(m−α,α);
    - MA_h→MA^ext_h in the opening.
