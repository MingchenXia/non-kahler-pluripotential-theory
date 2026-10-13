# b6a: audit of p6a, p6d, p6g (+ chapter_gauduchon opening, preface l.81/83)

## Verdicts
- **p6a: MOVES CORRECT.** My only edit in its area is in the coordinator's clause in the chapter_gauduchon opening.
- **p6d: CORRECT AFTER FIXES** (3 small fixes).
- **p6g: CORRECT AFTER FIXES** (2 wording fixes).

## What I checked
- **Math diff.** I ran `mathdiff3 --base 099fd4b` on 71 files: all p6a and p6d files, the p6g files, and the callers. I added up the net diff across files by hand. Every net math change is one of the edits the reports list. No label or `\index` entry was lost; the only additions are the two new labels, sec:balanced-pluriclosed-metrics and the new Cantor index entry.
- **Label graph** (private copies of `lg.py`/`q.py` in `scratchpad/b6a/`): 2941 labels, 0 duplicates, 0 undefined. Tarjan finds 0 cycles in the proof and statement graph. Every moved block cites only earlier labels, and no earlier proof or statement cites a moved label. The one exception is the pre-existing, declared, non-circular case `section_psh_measure_concentration:70 → thm:local-prescribed-excess`; I checked that the theorem's proof does not reach `prop:smooth-dirac-concentration`.
- **Forward references from proofs or statements, all files of my reports.** All are pre-existing:
  - `subsection_continuous_hessian_adjoints:62 → cor:gaud-adjoint-lq` (chapter_gauduchon_variational_volume);
  - `section_big_minimal_existence:41 → thm:hermitian-space-descent` (appendix);
  - `chapter_research_program:356`, problem → appendix.
- **Standing assumptions.** I read every moved statement in its new context.
  - Bundle chapter: ω, n≥2, the n≥1 / noncompact / Kähler-ω setting of the negative-bundle section, the "X=C, n=1" of the ramified section, the projective section, and the Ricci-flat section.
  - Fredholm subsection: X connected, dV; the "next subsection" pointer is right.
  - Concave sections; hessian:bounded-nonvanishing; the products lemma; H^{1,1}_BC; lem:continuous-potential-smooth-loss (θ generic); vague metric; divisorial Sobolev, a `\subsection` inside `\section{Analytic types}`, so the heading level fits.
  - Nothing left in chapter_gauduchon uses the bundle or Fredholm material. I checked with the label graph and by grepping for deg_, RC-, Finsler, K_{ω,h}.
- **Referee checks.**
  - **Deleted thm:hopf-descended-hermitian-ma.** Lemma parts (1) and (3) give exactly what the 5 callers use: partial_bergman:262 (the measure formula, giving 1/(2n)), :268 (MA_{kα}=0), hopf_point_equilibrium:131, and hopf_reduction (twice). The identification π^*ν∧ζ = β_n∧p_n^*ν holds verbatim, given X_n=H_n, π=p_n, ζ=β_n and σ=ω_FS (from section_hopf_sections:6–8).
  - **lem:local-vague-metric.** The proof is self-contained: the bound by εχ_k plus the f_i term, ε≤1, a total of ε(2∫χ_kdα+2), then density with tail 2^{-j}. The theorem's bound d_v ≤ 2/j+2^{-j} is right. Nothing is lost, and background_cluster_sets is still consistent.
  - **lem:polar-cantor-nonatomic-measure.**
    - 2r_{k+1}<r_k because log2 < 3·4^{k+1}, and r_0=e^{-4}<1.
    - u(x) ≤ 2^{-k}·log r_k² = −2^{k+3}.
    - So u=−∞ on K. u is subharmonic and finite off K, so K is (pluri)polar in the book's sense, and the measure has no atoms.
  - **lem:nef-blowup-metric.** The η_D/σ_D lead-in is right: η_D is closed, and Poincaré–Lelong gives ddcσ_D=[D]−η_D. The bigness computation π^*ω+ddcζ = C_0^{-1}(κ+[F]) holds, which gives β+a ddcζ ≥ aC_0^{-1}κ.
  - **cor:hopf-basic-testcurve-pullback.** The model identity gives the envelope condition and P_ω[p^*ψ]=p^*ψ. The shortened proposition keeps everything that its users need.
  - **p6g.** The ω→η rename is complete, with no leftover ω and no clash with η elsewhere. The Stokes lead-in is precise: ∫dξ∧β^{n-1}=±∫ξ∧dβ^{n-1}=0, and the proof makes it pointwise, tr_B a=0. n≥2 now comes from the chapter. The deformation subsection keeps its own M, n≥1 setting.
- **Openings and preface.**
  - The bundle-chapter opening is accurate, including its list of inputs; the root calculation does come before the proof of thm:lamari.
  - The products, testcurves, Hessian and normalization openings are accurate.
  - **Preface l.81:** accurate. The only later uses are prose: chapter_sections:90 restates the degree with its own display, and hopf_sections:58 is an aside.
  - **Preface l.83:** accurate for chap:polar-model-topologies (it does not assume BMP; mass bounds appear only where stated) and for the cotangent-torsor appendix.
  - No workflow vocabulary in any added lines.
- **History.** h6 has meanwhile moved the Moishezon/GL22 sentences to sec:history-products (history l.142), so chapter_products:209 now points correctly. sec:history-bundle-positivity now exists (l.94).
- **Compile check.** I ran `chapcheck.sh b6a` with the 16 listed chapters twice after my last edit: no errors, no overfull boxes. The only message is the known Underfull 1783.
  - Remaining warnings come from the partial build. Multiply defined: bc-one-one, nef-blowup and qu:i-good-no-bmp, which come from stale baseline aux files; each label is defined once in the source.
  - Undefined, with wrapped log lines joined: chap:polar-model-topologies, gaud-collapse/bigness-threshold and the primitive-elliptic labels. All of them exist in chapters that were not compiled.

## Fixes made (file: old → new)
1. **chapter_gauduchon.tex, opening (the coordinator's blowup clause).** As written, the clause attached the blowup example to the nonexistence of a smooth minimizer and did not say what the current is.
   - Old: "…attained by a potential; a minimizing test exists … does not exist; on the blowup of $\mathbb P^2$ at a point, the normalized integration current along the exceptional curve lies outside the closure of the smooth tests."
   - New: "…attained by a potential, and a minimizing test exists … does not exist. This closure can be smaller than the set of all normalized positive $\ddc$-closed $(n-1,n-1)$-currents: on the blowup of $\mathbb P^2$ at a point, the normalized integration current along the exceptional curve lies outside it."
   - This matches ex:gauduchon-current-smoothing-obstruction: T_C∈𝒢_ω∖𝒞_ω.
2. **chapter_gauduchon.tex, opening and the lead-in of sec:balanced-pluriclosed-metrics.**
   - "persist under deformations" → "persist under small deformations", in both places; the theorem is for small t.
   - "maximizes the volume on a compact slice" → "on a bounded slice".
3. **section_non_kahler_geometry.tex:127.** "the positive slice of fixed trace is then compact" → "…is then bounded". The open slice is bounded and its closure is compact, as in the proof.
4. **section_finite_restricted_invariants.tex:9.** The old sentence applied the lemma to "a Kähler form $h_X$", but X is the class-𝒞 manifold of that section and the base here is Z_1×Z_2.
   - Old: "Such a sequence $p$ of blowups is again K\"ahler: … applied to a K\"ahler form $h_X$, gives the closed positive form $C_0p^*h_X-\eta_D$."
   - New: "For such a sequence $p$ of blowups, … applied to a K\"ahler form $h$ on $Z_1\times Z_2$, gives the K\"ahler form $C_0p^*h-\eta_D$ on the blown-up manifold."
5. **section_concave_strict_gap_stability.tex:94.** The section no longer has a standing dV (the old chapter fixed one).
   - "with $p=2$ and background $\alpha$" → "with $p=2$, background $\alpha$ and volume form $\alpha^n$".
6. **section_hopf_basic_perron.tex:282.** The test-curve content has moved to chapter_testcurves.
   - `\section{Model projection and test curves}` → `\section{Model projection and Perron segments}`.

## Remaining (for the coordinator; optional)
- subsection_homogeneous_convex_regularization:8: sec:history-bundle-positivity now exists, so the planned repointing can be done.
- section_concave_strict_gap_stability l.61, 63, 70: the proof sets "$m=\min_Xw$" right after the section says the chapter's degree m plays no role. Suggest renaming it to $w_0$ in all three places.
- section_pluriclosed_deformations: ω_0 and ω_t (on M) sit next to the chapter's ω and ω_u. They are defined locally, so no fix is needed. Renaming them to η_0, η_t would match p6g's rename in the parallel-torsion proof.
- Cosmetic, from the p6d report: partial_bergman:262/268 and hopf_point_equilibrium:131 could cite `lem:hopf-basic-potentials` directly. The old label now renders as "Lemma …" and resolves correctly.
