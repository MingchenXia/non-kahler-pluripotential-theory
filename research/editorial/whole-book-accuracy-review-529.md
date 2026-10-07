# Checkpoint 529 — Second whole-book review: accuracy and clarity

Date: 6 October 2026. Branch: `claude/friendly-fermi-jzw1o1`.

## Request

After the presentation revision (527) and the Oeljeklaus–Toma section (528), the author asked (6 October 2026): “请你再检查一轮全书，确保细节准确无误，表述清晰可读。” (Check the whole book once more; make sure the details are accurate and the exposition clear and readable.)

## How the review was done

The active book (Introduction, Conventions, Chapters 1–33, the problems chapter, the historical notes and Appendix A; 351 files, about 4.2 MB of source) was split into 29 contiguous parts. Each part was read line by line by one reviewer following a common guide. The guide put accuracy first:
- re-derive formulas and short computations;
- open every `\cref`/`\eqref` target and check its hypotheses at the point of use;
- check that each proof proves its statement as stated;
- check symbols against their definitions.

Clarity came second: overlong sentences, ambiguous pronouns, vague pointers, proof architecture, typography and terminology.

Reviewers fixed clear local errors and reported everything else. The coordinator settled cross-chapter items. Separately:
- every SGPT citation was checked against the SGPT text;
- the citations of Demailly's books were checked against their texts;
- six independent auditors re-read every change of this pass against `ee577b3`.

## Mathematical corrections

Each correction is local; no theorem's scope changed except where stated.

**Errors introduced by the previous presentation pass (527), now fixed**
- `chapter_partial_bergman.tex` (opening): the competitors of the partial envelope are *at least* as singular as φ in the sense of multiplier ideals; 527 had written “at most”. The limits are only shown to be at least as singular as φ, not equivalent to it.

**Incorrect or overstated statements**
- Chapter 25 opening:
  - the Riemannian metric is the *negative* Hessian of the logarithm of the root volume;
  - concavity holds for the root λ_μ, the infimum of linear quotients, not for 𝒱_μ = λ^n;
  - the infimum of the threshold quotient is the nth root of b_ω(f).
  - The sign is also corrected in `section_invariant_mass_and_reference_densities.tex`.
- `section_nef_order_modifications.tex`: O(−E)|_E is the *dual* of the tautological bundle (positive on the fibers).
- `section_affine_local_strict_weights.tex`: reduction to small radii holds for local pluriregularity but not for (δ,q)-regularity (two-disk counterexample).
- `section_affine_projective_envelopes.tex`: the envelopes agree outside a pluripolar set, not only almost everywhere. This is needed where K has measure zero.
- `section_normalization_dual.tex`: by Jensen the entropy is at least −log dV(X), so it can be negative only when dV(X) > 1.
- `section_prescribed_radial_density.tex`: the tail is (log L)^{1−d/n}, a negative power of log L, since d > n.
- `section_density_zero_geometry.tex`: the measure (F_k^*h_0)^n is absolutely continuous (its density vanishes along the coordinate divisors), not singular.
- `section_convex_bundle_norm_obstruction.tex`: the support of ρ_s lies within distance 2ε of the unit circle, not ε.
- `chapter_weak_equations.tex`: nonuniqueness needs a smooth density vanishing on an open set; strictly positive smooth densities give uniqueness.
- `section_projective_first_jet_positivity.tex`: Lamari's criterion concerns positivity up to dd^c u, and strict Griffiths positivity is an open-cone condition.
- `section_ramified_root_metric_tests.tex`: the curve is a branched double cover of ℙ¹ (genus 1 when q = 2), not hyperelliptic.
- `section_smooth_cone_duality.tex`: there is no largest admissible a, so “supremum” replaces “largest”.
- `section_nef_projective_integer_cones.tex`: D_μ ≡ 1 only for n = 1.
- `section_finite_restricted_invariants.tex`: the volume of a nef class equals the top intersection number for nef and *big* classes.
- `chapter_rays.tex`: the geodesic envelope exists whenever a common lower potential exists (such a potential need not exist).
- `preface.tex`: mass conservation *can* fail; continuity, not boundedness, of a potential is insufficient.

**Missing hypotheses or steps supplied**
- `prop:trace-bott-chern-bclass`: now stated with the weaker hypothesis that θ|_Y is closed, which is all its proof uses.
- `lem:monotone-psh-capacity`: the proof now bounds deep sublevel sets by the global tail estimate instead of tacitly using that pluripolar sets have outer capacity zero.
- `prop:interior-tame-approximants`: the Dirichlet lemma is applied with density F (the old density H solved the wrong equation), after rescaling to the unit ball.
- `cor:common-barrier-continuity` callers: Ω = Aω with w_j = ψ_j/A, since the corollary requires ω-psh barriers.
- `prop:positive-volume-background-comparison`: the mixed-mass estimate is applied in PSH(X,Ω), since 0 need not be θ-psh.
- `thm:fixed-big-analytic-approximation`: the ideal-envelope competitor condition is justified.
- `thm:two-sided-model-transport`: the inequality θ ≤ Ah, used in the proof, is now stated.
- `thm:big-minimal-normalized`: the two-sided bound is derived.
- The exponential comparison in a semipositive big background is justified via `thm:semipositive-bounded-domination` and `prop:big-noncollapsing`.
- Other supplied steps:
  - Reg_Z(T) is positive and closed via its finite partial sums;
  - u_m is defined for large m;
  - the constant ε_0 is defined;
  - uniqueness holds up to constants;
  - an omitted case g_η′ ≥ −m_η appears in the Hopf positivity argument, and constancy of V_η outside U_0;
  - in the threshold divisorial constraint, the supremum over smooth tests is the root functional (`thm:integrable-gauduchon-formula`).
- `section_oeljeklaus_toma.tex`:
  - the constant c_X is fixed before g, and the invariance of dV_0/(y_1y_2) is stated;
  - Au is bounded, as part (3) of the mass proposition requires.
- `section_flow_compatible_incomplete_metric.tex`: the analytic-singularity normalization, the extension across p, and ∫_E Θ_E = −1 are stated in the book's convention.
- `section_completion_energy.tex`: the orthogonality argument is completed (forms of the other factor, Stokes on the same factor).
- `section_trace_product_measures.tex`: the atomic equation is applied to finite atomic measures, and its proof is shown to cover them; the base is connected.

**Settled constant.** The LCK radial flux constant (left open in 527) is 4πn·lF/D = 4πnk with respect to ω^n. It was derived twice by the reviewer and once more by an auditor.

**Problems chapter.** Five problems were partly settled by theorems of the book. They now state what is proved, with a reference, and what remains open: primitive elliptic lower mass, geometric Gauduchon endpoints, balanced plus pluriclosed, Gauduchon metric boundary, and exact trace realization. The scope of the variational-volume and lower-mass statements is corrected.

## Citations

- **SGPT.** All 34 numbered SGPT locators are correct. This includes Lemma 6.2.1 with C_n = 3(n+1)2^{n+2}, which gives the constant 48 used in the curve trace metric.
- **Unnumbered “recalled in SGPT” citations of facts that SGPT does not contain** now cite a book that does:
  - Skoda's integrability lemma: DemAM11 Lemma 5.6;
  - analytic regularization: DemAM11 Corollary 14.13;
  - Lelong monotonicity: DemCADG III (5.7)–(5.8);
  - local compactness and the Bedford–Taylor calculus: GZ17.
- **Demailly–Păun criterion.** It is named in the body, and the historical notes cite DP04 Theorem 0.5. They also explain the converse of the Fujiki-class equivalence through a Kähler modification.
- **Smooth regularization.** It is attributed in the historical notes to Dem92 (see also Dem94 Theorem 4.1). This is the only new citation; the key already existed.
- **Historical notes.** Descriptions are aligned with the body:
  - the order reversal of polar measures;
  - the scope of the positive-volume counterexample;
  - the hypotheses of several attributed results;
  - consistent version locators.
- **Citation placement** passes.

## Clarity and consistency

- Overlong sentences are split, and vague pointers (“the inequality above”, “the preceding proof”) replaced by references or explicit statements, with new equation labels where needed.
- Undefined terms are defined at first use, among them “model” (smooth compact modification), tr_ω, “determinant measure” and residual measure (now in Chapter 1).
- Local symbol clashes are renamed.
- Book-wide notation and terms:
  - maps are written f\colon X→Y;
  - the Fubini–Study form is written ω_FS;
  - d^c uses the macro;
  - the bounded mass property is a property of X;
  - the terms root functional, subsolution threshold, Gauduchon multiplier, strict barrier and superlevel set are unified;
  - the informal “distributional/closed Stokes” is replaced by Stokes' theorem.

## Checks

1. Every part was compile-checked in isolation and math-diffed against `ee577b3`; no label, reference target or index entry was removed. New labels:
   - `eq:geometric-adjoint-gap`
   - `eq:normalization-distance-gap`
   - `eq:divisorial-trace-loss-bound`
   - `eq:two-sided-transport-form`
2. Six independent audits re-read all changes of this pass (about 400 content changes), re-deriving the main corrections. They found two imprecise wordings, both fixed: an incidence-variety dimension, and a finiteness condition in the scope clause for the volume comparison formula. No reviewer correction was judged wrong.
3. A clean full build has no errors, no overfull boxes and no undefined references: 1520 physical pages, last index page printed as **1492**, 117 bibliography entries and 910 index entries. The only warning is the known underfull line in a bibliography entry. Pages inspected: the notation table, the Chapter 25 opening, the LCK flux statement, the Fujiki-class note and the last index page.
4. Publication: homepage commit `335edc6127716777ba67fe1d3a1cb1baba43511a` on `MingchenXia/mingchenxia.github.io` replaces `Papers/SHPT_vibe.pdf` and the matching description (“A research monograph. 1492 pages. Updated October 6, 2026.”); the remote files were verified by blob hash. The live check is recorded in `research/STATUS.md`.

This is a review and comparison of the text, not a new independent certification of every proof.

## Follow-up 1: mass invariance in closed backgrounds

The author first pointed out (6 October 2026): “‘闭背景下非多极质量只依赖奇异性类型’这只在Kähler的时候成立” (that the non-pluripolar mass in a closed background depends only on the singularity type holds only in the Kähler case). Statements of this invariance made without a hypothesis were restricted to compact Kähler manifolds.

The journal-version check (Follow-up 2) then read Boucksom–Guedj–Lu, Peking Math. J. 2025:
- Their Theorem 2.8 holds on compact complex manifolds with the bounded mass property: if φ ≤ ψ + O(1), then ∫⟨(θ+dd^cφ)^n⟩ ≤ ∫⟨(θ+dd^cψ)^n⟩ + ‖θ‖.
- The defect ‖θ‖ vanishes for closed θ by Stokes' theorem.
- Their Example 3.2 deduces that a closed current has equal lower and upper volumes.

Asked how to state the invariance, the author chose the bounded mass property with a citation of BGL25. The book now says:
- **Chapters 12 and 29 (openings):** the invariance holds on compact Kähler manifolds and, more generally, under the bounded mass property. The claim that it fails without the Kähler hypothesis is removed.
- **Chapter 29 (singularity-volume remark):** cites the classical Kähler case (SGPT) and the general source in the historical notes.
- **Normalization chapter:** states the invariance on compact Kähler manifolds and, more generally, under the bounded mass property.
- **Historical notes:** attribute the invariance to BGL25 (Theorem 2.8 with the vanishing defect (2.7), and Example 3.2) on manifolds with the bounded mass property.

Every use of the invariance in a proof is on a Kähler manifold, or in Chapter 29, which assumes the bounded mass property. No proof changes.

Stokes' theorem for bounded potentials in a closed background (`thm:mass-invariance-characterization`) holds on every compact complex manifold and is unchanged. The rule is recorded in the book-writing skill.

## Follow-up 2: journal versions of cited papers

The author's rule (6 October 2026): “You should always use the journal version when possible.” Eight agents checked the 105 cited papers, excluding books, notes and theses: publication status, bibliographic data, and every locator against the published text when it could be reached. The coordinator applied their patch lists and checked every replaced string for uniqueness.

**Bibliography and locators**
- The following entries now cite published versions, and their locators follow the journal numbering and pagination: BEGZ10, Sze18, TW10, TW15, STW17, EGZ09, BT82, DP04, Dem94, KN15, KN19, KN21, KN22, Nguyen16, BBToric13, Chiose14, Pop13SG, CT15Loci, GP04, ADOS24, OV11OT, OV24LCK, OV24Vaisman, OV25LeeGauduchon, OV25Balanced, GL23E, AKMW02, FTWZ16, Siu74, Inoue74, Barlet00 and WalterPrioritary93.
- Papers that appeared after they were first cited: ALS26 (J. Funct. Anal.), FV26 (Proc. Amer. Math. Soc.), DangNull26 (Trans. Amer. Math. Soc., Early View) and DX24 (Trans. Amer. Math. Soc.).
- Remaining arXiv citations name the version used (v1, v2, …).
- Cavalcanti's published paper (Adv. Math. 2020) omits the stability section, so Theorem 8.11 is still cited from arXiv v5, with a note in the bibliography.

**Changes of numbering found**
- **Sze18:** in the journal, Propositions 10 and 11 are swapped relative to arXiv v3.
- **Dem94:** the printed chapter numbers differ from the manuscript: Lemma 4.4 → 4.2, Proposition 3.8 → 3.1, equations (3.11), (4.3), (4.5) → (3.19), (4.21), (4.22), and Remark 4.7 → 4.4.
- **DP04:** the Annals numbering (Theorems 0.5, 0.7, Conjecture 0.8) is confirmed, and the arXiv remark is dropped.
- **Dem92:** the smooth regularization is Main Theorem 1.1.
- **KN22:** the old book title was wrong; the paper is in Springer Proc. Math. Stat. 481 (2025).

**Answers to the author's questions**
- **Ceg98:** Theorem 6.3 holds for compactly supported measures, with n ≥ 2 as the standing hypothesis of its Section 2.
- **BT82:** Theorem 7.4 (p. 27) covers bounded monotone sequences; Theorem 2.1 is on pp. 4–7.
- **DNGL26:** Theorem 3.4 asserts no completeness, and Question 3.5 is an open problem. The book's examples now "answer it negatively".
- **Fu–Ouyang:** Lemma 3.1 and Proposition 3.2 do allow arbitrary approximating forms, so the book's counterexample bears on their conclusion and on (iii)⇒(i).
- **TaylorReg:** the note has a single unnumbered Proposition.

**Descriptions corrected**
- DP04: the converse of the Fujiki-class equivalence.
- Dinew16: Proposition 6.2 is a uniform L¹ bound.
- Dinew09: Theorem 1.2 is Kołodziej's inequality.
- OV11OT: the null leaves are Zariski dense.
- BEGZ10: attainment by minimal singularities holds for big classes.
- Wu: compact bases.
- Liu–Wan Theorem 2.1 is Kobayashi's criterion.
- DangNull26 Theorem 1.1 is Collins–Tosatti's argument without closedness.
- Tosatti26: differences of nef classes.
- BGL25 Lemma 1.15 comes from Hahn–Banach.
- GL22: the range estimate.
- Sze18 §6 has no first-order term.

**Not confirmed against the published text**

The published text was paywalled or unreachable. Each of these locators is supported only by the final arXiv or author version, or by later citations:
- FV26: Conjectures 1.1–1.2.
- DangNull26: statement numbers. (DX24 now has no locator: at the author's request of 6 October 2026, the published version is not consulted for now, and the statement used is cited from SGPT Proposition 3.1.12, (3.23)–(3.24).)
- OV24Vaisman: Theorem 4.1 and Lemmas 4.2–4.4.
- Dem94: Remark 4.4 and equation (4.22).
- Dem92: Main Theorem 1.1.
- DPS94: Example 1.7.
- WalterPrioritary93: the page of Proposition 2.

Items removed on 7 October 2026 after the checks in Follow-ups 3–5: TWWY15, Dinew09, CT15Loci, GP04, BG18, OV25LeeGauduchon, OV24LCK, ALS26, OV25Balanced, Nguyen16, KN19, Collins21, FTWZ16, GL23E and DDNL21.

## Follow-up 3: publisher texts supplied by the author

On 7 October 2026 the author supplied 19 PDFs, downloaded through a university VPN: seven publisher versions, eleven arXiv versions and Demailly's manuscript of Dem94. The files are evidence for this check only and are not added to the repository. Every citation site of the seven publisher texts was compared with the published statement.

**Confirmed against the published text; journal pages added**
- **TWWY15** (Calc. Var. 54, 2015): Definition 3.2 and Theorem 3.4 on pp. 444–445. The paragraph after Theorem 3.4 derives it from Caffarelli's theorem and extends it to viscosity solutions. The STW paragraph now says "in the form stated by" TWWY15 and names Caffarelli.
- **Dinew09** (Math. Z. 262, 2009): Theorem 1.2 on p. 2. It assumes bounded plurisubharmonic functions and nonnegative densities in L¹(dλ). The historical note now states these hypotheses and adds that the inequality is local, so the hypotheses of `thm:local-mixed-input` (locally bounded functions, measurable densities) reduce to them on relatively compact subdomains.
- **CT15Loci** (Invent. Math. 202, 2015): Theorem 1.1 on p. 1168, stated on manifolds in Fujiki's class C, as the book says.
- **BG18** (Calc. Var. 58, 2019, Paper 184): Proposition 2.4 (the exterior-ball step) on p. 7 and Theorem 2.5 (propagation of maxima) on p. 8.
- **OV25LeeGauduchon**: Theorem 3.11 on p. 243 (the dual description of the Lee–Gauduchon cone) and Remark 5.6 on p. 245. Theorem 4.5 (p. 244) and Example 5.7 and Remark 5.8 (p. 246) had already been seen in a preview; the locators now carry pp. 243–244 and 245–246.
- **OV24LCK**: Question 47.56(3) on p. 665: Gauduchon metrics with the same Lee class and twisted Bott–Chern class; does ω₁ⁿ = ω₂ⁿ imply ω₁ = ω₂? This matches Problem `q:lck-gauduchon-volume`. The page is added in Chapter 25.

**Corrected wording**
- **GP04** (Comm. Math. Phys. 251, 2004): Section 2 (pp. 69–71) constructs principal torus bundles M_{P,Q} from two closed 2-forms with integral periods. Their fiber is always the square torus ("principal T²-bundles for the standard complex structure on T²", p. 66). The book's bundle L^×/⟨w ↦ qw⟩ has fiber ℂ*/q^ℤ, which is square only when log q = 2π. The old sentence, "are special cases of the torus bundles", was therefore true only for q = e^{2π}. It now says: for q = e^{2π} the bundles are GP torus bundles, built from the Chern connection of the chosen metric, with forms a constant multiple of c and 0; other values of q change only the modulus of the fiber. The identification was checked by comparing the vertical (1,0)-forms: GP's iρ = −dy + i dx + α′ with the book's d(t/2) + i dx + α′, modulo pull-backs of (1,0)-forms, under y = −t/2.

**No new confirmation of journal numbering**
- The arXiv files (ALS26, OV24Vaisman, OV25Balanced, Nguyen16, KN19, GL23E, FTWZ16, Collins21, DDNL21, DangNull26, FV26) are the versions already checked. Their locators stay on the list above.
- The Dem94 manuscript uses the manuscript numbering (Remark 4.7, equation (4.5)), not the printed one. Remark 4.4 and (4.22) on printed p. ~121 therefore stay unconfirmed.
- The TWWY15 bibliography note "Theorem locations refer to the published version" is removed. The book's general statement on journal versions covers it.

Build: clean, 1520 physical / 1492 printed pages. Publication: website commit c08c0f5 with the remote blobs verified; the live GitHub Pages PDF matches SHA-256 `a71352bf…` and the homepage shows "1492 pages. Updated October 7, 2026".

## Follow-up 4: second set of publisher texts

Later on 7 October 2026 the author supplied six more publisher PDFs: ALS26, Nguyen16, KN19, FTWZ16, Collins21 and OV25Balanced. As before, they are evidence only and are not added to the repository. Every citation site was compared with the published statement; ALS26 was read by an independent checker against both the journal text and arXiv v1, and its findings were rechecked on the published pages before editing.

**Confirmed, with journal pages added**
- **Nguyen16** (Adv. Math. 286, 2016): Theorem 0.1 (p. 241), Corollary 0.2 (p. 242), Lemma 1.9 (p. 255), Lemma 2.3 (p. 256) and Proposition 2.5 (p. 258). The weighted mean of Proposition 2.5 is the book's (eq:gauduchon-exponential-mean).
- **KN19** (Adv. Math. 346, 2019): Corollary 3.9 (p. 287), Remark 3.13 (p. 289) and Lemma 4.1 (p. 294). The proof of Lemma 4.1 cites "[10, Remark 4.7]" of Demailly's manuscript for the extra term K(t−δ); this agrees with the earlier finding that manuscript Remark 4.7 is printed Remark 4.4 of Dem94.
- **FTWZ16** (J. Funct. Anal. 271, 2016): Section 2 (pp. 3166–3178). The T³-fibration with dense leaves and the Tricerri metric with Ric(ω_T) = −α are on pp. 3166–3167. Lemma 2.1 is on p. 3167, and the Liouville argument for bounded harmonic functions is in its proof on p. 3168.
- **Collins21** (Pure Appl. Math. Q. 17, 2021): Theorem 2.13 on p. 1068. Its second proof, with a Gauduchon rescaling of the linearized metric, is on p. 1069; the book's sentence about "the concavity argument with Gauduchon metrics" cites it.

**ALS26 (J. Funct. Anal. 291, 2026, 111608): renumbering and wording**
- The journal version inserts a new Lemma 2.5 (p. 9). Everything after it in Section 2 shifts by one: v1 Lemma 2.5 → 2.6, Propositions 2.10–2.12 → 2.11–2.13, Definition 2.13 → 2.14. The locators are corrected. All other cited numbers are unchanged, and pages are added to every ALS26 locator.
- **Theorem 2.2 (p. 8).** The journal version adds a paragraph: the envelope's measure may have infinite mass, and the statement follows by monotone convergence over {P_θ(h) > −C}. The book had claimed that its extension removed "a uniform mass assumption"; that claim is dropped. The book now says that ALS remark the envelope may have infinite mass, and that the book's passage to unbounded potentials removes the bigness assumption.
- **Proposition 2.13 (p. 14)** covers the case P_θ[u] = u, under ALS's standing hypothesis of semipositive big θ. The book's `prop:fixed-point-finite` assumes only semipositivity, and the note now says "the fixed-point case of …, stated there for semipositive big backgrounds".
- **Positivity of individual masses (line 141).** The discussion after Definition 2.14 gives positivity only for potentials of the ordinary type of ϕ; positivity for every u ∈ ℰ(X,θ,ϕ) is Remark 3.9 (p. 20), now cited too.
- **Theorem 3.14 (p. 22)** assumes v₋(θ) > 0, the standing hypothesis of the book's Chapter 30, and either of two finiteness conditions. The book's theorem is now described as "the case of finite μ_u".
- **Lemma 4.2 (p. 24).** It now has two bullets. Condition (1) includes u_j ≃ ϕ and needs no v₋(θ) > 0; condition (2) requires v₋(θ) > 0. The book's statement that, for approximants of the ordinary type, "this alternative needs no assumption of positive lower mass" is now ALS's own published statement. The note now cites the first assertion with that content and adds that `prop:exponential-common-rooftop` also allows other singularity types under v₋(θ) > 0. The remark on condition (2) (positive lower mass prevents collapse; no upper bound on mass is used) is unchanged and correct.
- **Not cited by the book.** Theorem 5.11 (p. 41) is now stated under v₋(θ) > 0 and v₊(θ) < +∞. The proof of Lemma 4.2(2) passes to a subsequence; the book's `lem:dominated-relative-rooftop-extraction` already states that version.

**OV25Balanced (IMRN 2025, no. 3, rnaf014): wording**
- Conjecture 4.14 (p. 7) asserts deg_u θ > 0 for every Gauduchon metric u, which is strictly stronger than pseudoeffectivity of {d^c θ}. Remark 4.16 (p. 8) relates the two. The book's `conj:lck-lee-psef` is the pseudoeffective version. The historical note used to say that the book's conjecture "is formulated in terms of Gauduchon degrees by Ornea and Verbitsky". It now states their conjecture and adds that, by `thm:lamari`, it implies the weaker `conj:lck-lee-psef` used in the book.

**Still not obtained**
DangNull26 and FV26 (AMS member access only), OV24Vaisman (International Press, purchase only), GL23E and DDNL21 (De Gruyter pages did not load through the VPN), Dem94 (subscription preview only), Dem92 and DPS94 (no scan of J. Algebraic Geom. 1992/1994 found), and WalterPrioritary93 (print volume). Their locators remain on the list in Follow-up 2.

Build: clean, 1520 physical / 1492 printed pages. Publication: website commit 7df5ee1 with the remote blob verified; the live GitHub Pages PDF matches SHA-256 `604c576c…`.

## Follow-up 5: the two Crelle papers

The author then supplied the published PDFs of GL23E and DDNL21. They are evidence only and are not added to the repository.

- **GL23E** (J. Reine Angew. Math. 800, 2023): **renumbered.**
  - The journal version has no Lemma 3.3; Section 3.1 has Corollary 3.3 (bounds for the normalizing constant).
  - arXiv v1 Lemma 3.3 (a bounded subsolution with −1 ≤ u ≤ 0, for ω big or v₋(ω) > 0) is split in print. The big case is Lemma 2.1 (pp. 270–271); the case v₋(ω) > 0 is Lemma 2.5 (p. 274).
  - The book's `lem:big-lp-subsolution` is the big case, with the same (−ρ)^{2n} f construction. The locator is now Lemma 2.1, pp. 270–271.
  - Theorem 3.4 (p. 279) is unchanged and matches `thm:big-bounded-exponential`.
  - The earlier "confirmation" of Lemma 3.3 rested on a later paper's citation of that number. It evidently referred to the preprint, so such citations are not evidence for journal numbering.
- **DDNL21** (J. Reine Angew. Math. 771, 2021): Lemma 4.3 is unchanged, on p. 154: P(bu + (1−b)v) is θ-psh when bⁿ∫uⁿ > (b−1)ⁿ∫vⁿ. This is the small convex correction the book uses. The page is added.

Build: clean, 1520 physical / 1492 printed pages. Publication: website commit 9339368 with the remote blob verified; the live GitHub Pages PDF matches SHA-256 `ac7cad6d…`.

The author has no access to the remaining seven publisher texts (DangNull26, FV26, OV24Vaisman, Dem94, Dem92, DPS94, Walter). Their locators stay as they are, supported by the evidence listed in Follow-up 2, and remain open items.

## Deferred items (no change made)

- `thm:small-pole-envelope-residual` assumes positive lower singularity volume, which its proof uses only for a side remark.
- Some hypotheses are stronger than their proofs need (for example `cor:i-envelope-finite`, `birational_partial_kernels`, `section_bounded_connected_uniqueness`); they are kept.
- `thm:flat-anticanonical-neighborhood`: Step 2 of Lemma 2 is only outlined; an expert check is advisable.
- The locators not confirmed against the published text are listed in Follow-up 2, as reduced by Follow-ups 3–5. The claims about DNGL26, Fu–Ouyang, BT82, TaylorReg and the BEGZ10 versions, deferred earlier, are resolved there.
- The hidden Nakamaye chapter cites CT22 Lemma 4.2 for arbitrary modifications; the lemma assumes compositions of blowups with smooth centers. Hidden files are not edited.
- Local reuse of letters across sections (Ω, r versus f for fiber dimension, L in Section 27.19) is declared locally and kept.
