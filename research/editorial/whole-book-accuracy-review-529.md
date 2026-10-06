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
- ALS26: 19 statement numbers.
- FV26: Conjectures 1.1–1.2.
- DangNull26: statement numbers. (DX24 now has no locator: at the author's request of 6 October 2026, the published version is not consulted for now, and the statement used is cited from SGPT Proposition 3.1.12, (3.23)–(3.24).)
- OV24Vaisman: Theorem 4.1 and Lemmas 4.2–4.4.
- OV25Balanced: Conjecture 4.14 and Remark 4.16.
- OV25LeeGauduchon: Remark 5.6 and Theorem 3.11.
- OV24LCK: Question 47.56(3).
- Dem94: Remark 4.4 and equation (4.22).
- Dem92: Main Theorem 1.1.
- Nguyen16: Corollary 0.2 and Proposition 2.5.
- KN19: Remark 3.13.
- Collins21: Theorem 2.13.
- TWWY15: Definition 3.2 and Theorem 3.4.
- GL23E: Lemma 3.3 and Theorem 3.4.
- Dinew09: Theorem 1.2.
- FTWZ16: Lemma 2.1.
- CT15Loci: Theorem 1.1.
- GP04: Section 2.
- DPS94: Example 1.7.
- DDNL21: Lemma 4.3.
- BG18: Proposition 2.4 and Theorem 2.5.
- WalterPrioritary93: the page of Proposition 2.

## Deferred items (no change made)

- `thm:small-pole-envelope-residual` assumes positive lower singularity volume, which its proof uses only for a side remark.
- Some hypotheses are stronger than their proofs need (for example `cor:i-envelope-finite`, `birational_partial_kernels`, `section_bounded_connected_uniqueness`); they are kept.
- `thm:flat-anticanonical-neighborhood`: Step 2 of Lemma 2 is only outlined; an expert check is advisable.
- The locators not confirmed against the published text are listed in Follow-up 2. The claims about DNGL26, Fu–Ouyang, BT82, TaylorReg and the BEGZ10 versions, deferred earlier, are resolved there.
- The hidden Nakamaye chapter cites CT22 Lemma 4.2 for arbitrary modifications; the lemma assumes compositions of blowups with smooth centers. Hidden files are not edited.
- Local reuse of letters across sections (Ω, r versus f for fiber dimension, L in Section 27.19) is declared locally and kept.
