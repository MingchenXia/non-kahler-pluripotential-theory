# Verification: closed_loci_lck_connections_repair_01

## Verdict

Correct. No critical errors or gaps were found in this bounded follow-up.

## Scope and preserved inputs

The submitted proof was checked in textual order, including the locally available `author/section_lck_volume_literature.tex`. The complete Chern–Ricci tensor calculation was used only as the expressly accepted result of `lck_chern_ricci_rigidity_01`; its new strict-LCK interface was checked here. No nonlinear bounded mass property was assumed.

Both prior audit directories, results and memory, are byte-for-byte unchanged across all 16 files recorded in the baseline hash manifest. The earlier wrong verdict is not replaced by this new audit.

## Sequential deductions

### 1. Definition of LCK, strict LCK, and Vaisman

1. The stipulated dλ=0 and dω=λ∧ω define the LCK setting; n>=2 guarantees uniqueness of λ.
2. For a parallel real one-form, its squared norm is constant. If it is df, compactness gives df=0 at a maximum, so it vanishes everywhere on connected X.
3. Strictness excludes λ=0 and all exact Lee forms; therefore a parallel Lee form in this scope is nonzero everywhere and nonexact. The old flat Kähler counterexample is excluded.

Result: pass.

### 2. Lee-form uniqueness and Kähler covering

1. If a∧ω=0, wedge by ω^(n-2) to obtain a∧ω^(n-1)=0. Nondegeneracy of ω makes this map an isomorphism on one-forms.
2. The local primitive f exists by closedness, and d(e^(-f)ω)=e^(-f)(dω-df∧ω)=0.
3. On a connected covering with exact pullback Lee form, a deck transformation preserves dF, hence g*F-F is constant and the displayed positive character follows.
4. Direct differentiation gives λ'=λ+da for ω'=e^aω; exact λ gives a globally conformal Kähler metric.

Result: pass.

### 3. eq:lck-lee-curvature

1. With dc=i/(4π)(bar∂-∂), λc=dc f on primitive charts and dcλ=dc df=-ddc f=-dλc.
2. This globally defined form is real, closed, of type (1,1), and de Rham exact. Local ddbar potentials need not globalize.

Result: pass.

### 4. prop:lck-gauduchon

1. In a local conformal Kähler chart, ω^(n-1)=e^((n-1)f)Ω^(n-1), hence dc(ω^(n-1))=(n-1)λc∧ω^(n-1).
2. The Hermitian star identity is a fixed nonzero scalar multiple of *λ; ddc(ω^(n-1))=0 is equivalent to d*λ=0.
3. Closedness and co-closedness are exactly harmonicity on a compact manifold; conformal Gauduchon existence is the prior internal input.
4. Stokes on d(λc∧ω^(n-1)) gives ∫dλc∧ω^(n-1)=∫λc∧d(ω^(n-1)).
5. Inserting d(ω^(n-1))=(n-1)λ∧ω^(n-1) and swapping λc,λ gives the positive sign in the degree formula.
6. λ∧λc=i λ^(1,0)∧λ^(0,1)/(2π) is semipositive, with positive trace at each nonzero point; a nonzero smooth Lee form is nonzero on an open set, giving strictly positive integral.

Result: pass.

### 5. eq:lck-lee-bc-map and nonvanishing

1. Changing λ by da changes κ by -ddc a, so the map on real de Rham cohomology is linear and well defined in ordinary Bott–Chern cohomology.
2. Pairing with γ^(n-1) is unchanged by ddbar-exact terms because γ is Gauduchon.
3. For strict LCK, the conformal Gauduchon metric has a Lee form in the same nonzero de Rham class. Its pairing is positive by the preceding proposition. Therefore the Bott–Chern class is nonzero, although de Rham exact.

Result: pass.

### 6. cor:lck-no-closed-big-class

1. The external modification criterion is invoked for an ordinary closed big (1,1) class on compact X, yielding a smooth compact Kähler modification Y.
2. Pullback κ is smooth real d-closed of type (1,1) and de Rham exact. The compact Kähler ddbar lemma therefore produces a smooth real h with π*κ=ddc h.
3. For every complementary-degree smooth test form, integration over the biholomorphic locus and measure-zero exceptional sets yields π*π^*κ=κ, where π* here denotes current pushforward.
4. Proper holomorphic pushforward commutes with ddbar, so κ=ddc(π_*h) as distributions.
5. Taking the trace against any smooth positive Hermitian metric gives a scalar elliptic operator applied to the degree-zero distribution π_*h with smooth right-hand side. Elliptic regularity yields smoothness, hence zero ordinary Bott–Chern class.
6. Equivalently, pair the distributional equality directly with a Gauduchon form to obtain zero, contradicting strict positivity.
7. Fujiki class C admits a compact Kähler modification by the same criterion, so the contradiction also excludes class C. No mass bound enters.

Result: pass.

### 7. Hopf specialization after cor:lck-no-closed-big-class

1. The given previously proved identity κλ=α>=0 supplies a smooth semipositive closed representative and hence nefness.
2. A nef class has empty non-nef locus under the closed-loci definitions. Since the manifold is strictly LCK, the new corollary excludes bigness, so the stated convention makes the non-Kähler locus all of X.
3. The positive nonclosed Hermitian background is a different object from this closed class; no nonlinear mass estimate follows or is used.

Result: pass.

### 8. prop:lck-balanced-obstruction

1. Pseudoeffectivity supplies T=κ+ddc u>=0; nonzero Bott–Chern class forces T nonzero.
2. Both κ and ddcu are de Rham exact currents.
3. Balancedness gives d(b^(n-1))=0, hence distributional Stokes gives zero pairing.
4. Strict positivity of the test form b^(n-1) makes the mass of a nonzero positive (1,1) current strictly positive, a contradiction.

Result: pass.

### 9. conj:lck-lee-psef and Gauduchon duality

1. The conjecture is not used as a theorem. Positivity against the distinguished LCK Gauduchon metric alone does not establish pseudoeffectivity.
2. The internal Lamari criterion requires nonnegative pairing against every Gauduchon metric. This accurately identifies the additional claim; no upper Monge–Ampère mass condition appears.

Result: pass.

### 10. thm:lck-vaisman-volume and symmetry paragraph

1. The repaired strict definition and explicit λ not identically zero supply the two-dimensional canonical foliation excluded in the old Kähler counterexample.
2. The prescribed-volume result is retained as an external existence/uniqueness input; exact source hypotheses are being checked separately.
3. On Vaisman manifolds the Lee and anti-Lee fields commute and preserve the foliation; contraction of a volume invariant under both fields is horizontal and invariant, hence basic.
4. Their Killing property forces volume invariance. The source assertion that their vector fields are determined up to constant scale by complex structure is needed to transfer this necessity across Vaisman metrics.

Result: pass.

### 11. prop:lck-coupled-equation

1. The proposition is conditional on the specified twisted-class identification and A>0; it does not assert existence of u or the identification.
2. Substitute ω2=e^aA: ω2^n=ω1^n is equivalent to A^n=e^(-na)ω1^n.
3. Substitution in the Gauduchon condition gives exactly ddc(e^((n-1)a)A^(n-1))=0, with both implications immediate.

Result: pass.

### 12. Paragraph after prop:lck-coupled-equation and q:lck-gauduchon-volume

1. The direct internal citation now points to thm:stw-volume, whose full statement is supplied below; this resolves the earlier misdirected chapter citation.
2. The ordinary scalar equation and the Gauduchon prescribed-volume equation do not impose the given LCK structure or twisted Bott–Chern class.
3. The uniqueness question is stated as a question. A scalar representative is only determined modulo the kernel of the stated twisted operator; no uniqueness is silently deduced.
4. Counterexamples for ordinary potentials with degenerate density do not answer this metric uniqueness question with smooth positive volume and fixed twisted data.

Result: pass.

### 13. input author/section_lck_volume_literature: prop:lck-basic-uniqueness

1. The read-only local input file repeats the repaired volume theorem and contains this basic uniqueness proof.
2. Subtracting transverse top powers gives ddbar v wedged with the sum of mixed positive powers equal to zero.
3. For m>=1 the mixed (m-1,m-1) form defines a linear elliptic operator on each transverse chart with zero zeroth-order term.
4. A maximum exists by compactness. The strong maximum principle makes v constant on a connected transverse chart; basicness extends this to its foliation chart.
5. The maximum level set is nonempty, open and closed; connectedness makes it the whole manifold, and then eta1=eta0.

Result: pass.

### 14. input author/section_lck_volume_literature: thm:lck-chern-ricci-rigidity and conformal discussion

1. The actual included theorem assumes the same compact strictly LCK metric is both Gauduchon and Chern–Ricci flat.
2. The separately accepted audit lck_chern_ricci_rigidity_01 establishes parallelism of its Lee form. Nonexactness excludes the zero form, so the conclusion fits the repaired Vaisman definition.
3. The full tensor proof is used as the explicitly authorized prior input, not rerun or silently strengthened.
4. Vanishing of c1BC gives RicCh(ω)=ddbar h. The determinant conformal formula gives RicCh(e^(h/n)ω)=RicCh(ω)-ddbar h=0.
5. A separate conformal Gauduchon representative need not coincide with this Chern–Ricci-flat representative; no inference to simultaneous solvability is made.
6. The BO25LCK conjecture is accurately framed as existence of a Vaisman metric on the manifold and is not asserted as proved.

Result: pass.

### 15. input author/section_lck_volume_literature: Lee–Gauduchon cone

1. For each Gauduchon gamma, d dc(gamma^(n-1))=0, so the stated real de Rham class exists.
2. Sums and positive multiples of positive ddbar-closed (n-1,n-1) forms have unique positive roots, proving convexity of the image cone.
3. Apply dc-Stokes to λ∧gamma^(n-1): 0=∫dcλ∧gamma^(n-1)-∫λ∧dc(gamma^(n-1)), yielding the displayed sign.
4. The left pairing depends on de Rham classes because both factors are d-closed; the right depends on Bott–Chern and Gauduchon data by ddbar-Stokes.
5. The internal Lamari criterion applies to closed κ and gives precisely the stated pseudoeffectivity equivalence.
6. Bimeromorphic invariance of this linear cone is an external input, not a claim about nonlinear masses.

Result: pass.

### 16. Precise regularization statement

1. The ambient Hermitian form and continuous lower bound are the standard data in Bou04 Theorem 2.1; its two regularizations are distinct sequences.
2. For smooth representatives, continuous λj decrease pointwise to the Lelong function. If all Lelong numbers vanish, the limit is continuous zero on compact X, and Dini gives uniform convergence.
3. Thus C sup λj tends to zero, making the loss uniformly small.
4. For analytic regularization, lower bounds gamma-epsilonj omega and Lelong upper bounds hold in the same ordinary closed class.
5. If T>=delta omega with delta>0, choose epsilonj<delta/2 to retain strict positivity. At a zero-Lelong point, nonnegativity of the approximant Lelong number together with its upper bound forces zero.
6. The thesis and SGPT are supplementary pointers; exact general-Hermitian lower bounds are anchored in Bou04. No mass bound is required.

Result: pass.

### 17. thm:stw-volume

1. The actual internal target exists with exactly the supplied statement in chapter_smooth_equations.tex.
2. STW Theorem 1.4 uses i partialbarpartial v and Re(i partial v wedge barpartial gamma^(n-2)). Setting v=u/(2pi) produces both coefficients in the supplied Gamma_u exactly.
3. The compact connected setting and n>=2 persist from the chapter. gamma0 Hermitian, gamma Gauduchon and real smooth F are sufficient source hypotheses.
4. A strictly positive (n-1,n-1) form has a unique smooth positive root, so the stated root creates no new existence assumption.
5. Uniqueness is for the normalized scalar pair (u,b) in this ansatz. This is not uniqueness among all metrics with the given volume, Lee class, or twisted data.
6. If gamma0 is Gauduchon then the root is Gauduchon; the displayed theorem does not assert that additional property for an arbitrary gamma0. In dimension two the torsion term vanishes as required.

Result: pass.

### 18. Final interface and modification clarifications; assumption-use audit

1. The final explanatory paragraphs agree with the included strict rigidity theorem and the accepted earlier parallelism proof.
2. The exceptional-set integration and scalar-distribution elliptic argument correctly justify the corollary's pushforward step.
3. Compactness is used for extrema, Gauduchon existence, Stokes, Dini, and the modification criterion. Connectedness is used for constant parallel-form norm and basic maximum propagation.
4. n>=2 is used for Lee-form injectivity, positive factor n-1 and the prescribed-volume frameworks. Strictness is essential for nonzero Lee–Bott–Chern pairing and the Vaisman conclusion.
5. Pseudoeffectivity is used only in the conditional balanced obstruction; field invariance and volume normalization are used in the Vaisman external theorem.
6. No bounded mass property is present, inferred from Hopf semipositivity, or imported into the corollary.

Result: pass.

## Reference verification

External statements were searched with `search_arxiv_theorems` first. Where the cited statement did not match, built-in web search was used, followed by comparison with primary texts or the identified local author copies. Internal theorem labels were read directly.

### cor:lck-no-closed-big-class — Kähler-current/modification criterion

- [Demailly–Păun, Numerical characterization of the Kähler cone, Theorem 3.4, pp.1263–1264](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### Precise regularization paragraph: Bou04Zariski Theorem 2.1

- [Theorem 2.1, printed p. 50; cohomology convention in §2.1, p. 47](https://www.numdam.org/article/ASENS_2004_4_37_1_45_0.pdf)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### cor:lck-no-closed-big-class — compact Kähler ddbar lemma

- [Tosatti, KAWA lecture notes on the Kähler-Ricci flow, Lemma 2.1](https://arxiv.org/html/1508.04823)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### thm:lck-vaisman-volume

- [Theorem 4.1, p. 7; Remarks 2.5–2.6, p. 4](https://arxiv.org/pdf/2206.08808v2)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### Paragraph following thm:lck-vaisman-volume: symmetry necessity

- [Remark 2.5, p. 4; Proposition 3.1, pp. 6–7](https://arxiv.org/pdf/2206.08808v2)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### Paragraph following thm:lck-vaisman-volume: transverse Calabi–Yau input

- [Lemma 4.2, pp. 7–8; proof of Theorem 4.1, p. 9](https://arxiv.org/pdf/2206.08808v2)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### q:lck-gauduchon-volume and attribution to OV24LCK Question 47.56(3)

- [Question 47.56(3), pp. 683–684](https://arxiv.org/pdf/2208.07188v6)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### thm:stw-volume and its use after prop:lck-coupled-equation

- [Theorem 1.4 and formula (1.6), p. 4](https://arxiv.org/abs/1503.04491)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### Precise regularization paragraph: SGPT supplementary citation

- [Definition 1.4.1 and Remark 1.4.1; Definition 1.6.1; Definition 1.6.4 and Theorem 1.6.2; Theorem 11.1.1 Step 3; Corollary 11.1.5](https://mingchenxia.github.io/Lectures/SGPT_final.pdf)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### thm:lck-chern-ricci-rigidity and conj:lck-calabi-yau-vaisman — repaired strict interface and BO25LCK attribution

- [Barbaro–Otiman, Calabi–Yau locally conformally Kähler manifolds, arXiv:2509.18364v2, Introduction Theorem A and Conjecture; Preliminaries](https://arxiv.org/html/2509.18364v2)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### cor:lck-no-closed-big-class — internal route through chap:bott-chern-loci to BouThesis02 Theorem 1.2.11

- [Boucksom, Cônes positifs des variétés complexes compactes (2002), Theorem 1.2.11, p.31](https://www-fourier.univ-grenoble-alpes.fr/~demailly/theses/boucksom_these_2002.pdf)
- [Demailly–Păun, Theorem3.4, independently retrieved primary statement](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### Precise regularization paragraph: BouThesis02 Theorems 1.2.9–1.2.10

- [§1.2.5, Theorems 1.2.9–1.2.10, printed p. 30](https://sebastien.boucksom.perso.math.cnrs.fr/publis/these.pdf)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### Kähler covering and OV24LCK Section 3.4

- [Remark 3.20, Definitions 3.21 and 3.25–3.27, Claim 3.28; pages 49–51](https://arxiv.org/pdf/2208.07188v6)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### conj:lck-lee-psef and OV25Balanced

- [Abstract; Section 3 strict-LCK convention; Conjecture 4.14 and Remark 4.16](https://arxiv.org/html/2407.04623v2)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### input section_lck_volume_literature: OV25LeeGauduchon Theorem 4.5

- [Definitions 3.3 and 3.5; Corollary 4.4 and Theorem 4.5](https://arxiv.org/html/2411.05595v2)

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

### Internal thm:gauduchon and thm:lamari interfaces

- Internal source: /Users/mingchen/Non-Kahler/book/author/chapter_gauduchon.tex:17
- Internal source: /Users/mingchen/Non-Kahler/book/author/chapter_gauduchon.tex:128

Result: matched in the stated scope. Full contextual comparison is stored in `reference_checks.jsonl`.

## Secondary-source distinctions

The precise general-Hermitian regularization bounds come from Boucksom 2004, Theorem 2.1. The thesis uses a different smooth-bound presentation and omits the general lower-bound term in its printed analytic theorem. SGPT recalls related principles in its Kähler setting and distinguishes analytic singularities with bounded remainder from those with smooth remainder. These supplementary citations are not used to replace the exact Boucksom 2004 input.

The STW theorem allows Hermitian gamma0. Its solution is Gauduchon when gamma0 is Gauduchon; the displayed theorem does not promise that property for arbitrary gamma0. Uniqueness concerns its normalized scalar ansatz.

## Findings

- Critical errors: none.
- Gaps: none.
- Repair hints: none.
