# a5f audit report (r5g15, r5g16)

## Verdicts
- **r5g15: EDITS CORRECT.**
- **r5g16: EDITS CORRECT.** One hypothesis is kept for a reason that no longer holds (proposal P1). It is not an error.

I made no edits. `chapcheck.sh a5f chapter_envelope_systems chapter_gauduchon_variational_volume` shows only the allowed Underfull (badness 1783), in section_ruled_residual_gauduchon_cost.tex (another part). No `\label` or `\index` entry was lost in any of the 49 files. I read the mathdiff of every changed file: each change is a listed edit or a reformatting.

## Counts checked
- **r5g15:** 5 hypothesis removals, 8 duplicate removals, 5 simplified proofs.
- **r5g16:** 10 hypothesis removals (4 of them restated standing hypotheses, plus the δ_j halving condition), 8 duplicate removals, the same 8 simplified proofs, and the statement reorganizations.

## Priority items (all hold)

**Warped section, m≥2 → m≥1.** I checked every result with m=1. Then B is a curve, n=2, γ = L⁻¹A + w is Kähler and γ^m = L⁻¹A + w.
- thm:warped-gauduchon-volume:
  - The positivity tests use the form κ^{m-1}∧w = w.
  - Ω² = (2b/H)μ.
  - The numerator is n∫A^m = nb^m.
  - D = nb^m/λ = (nb^m/H)^{m/n}H.
  - Conformality of γ to Ω and thm:gaud-volume-dual-formula (n≥2) give the stronger "all minimizers are multiples of γ".
- prop:warped-flat-unit-metric, lem:warped-endpoint-length and both examples are fine; for E^m with m=1, s=1.
- prop:warped-current-cones is fine.
- prop:warped-continuous-endpoint-equation, via uni-thm:GL-intro. Its hypotheses hold:
  - X is connected compact of dimension n≥1 and the form ω = bκ is Hermitian (chap:degenerate-uniqueness).
  - The Guan–Li condition holds because bκ is closed.
  - The density (σ/L_0)/(bκ)^m is in L^p with p>1 and has positive integral.
  - It gives c = b^m/H_0 and a continuous φ.
  - Its own inputs (thm:kn-continuous, the domination principle) are stated for n≥1.
- prop:warped-endpoint-potential-limits, prop:warped-minimizer-trace and prop:warped-normalized-test-limits: for m=1, G_j = σ/(2L_j²) + w and t_j = J_j/2 + 1.
- thm:warped-unit-volume-completion:
  - Non-bigness via prop:warped-current-cones: e=0, or e+cM=0.
  - Volume one via thm:gaud-volume-nef-limit with h=κ+w. This is a forward citation, but its proof uses only prop:gaud-volume-elementary and the dual formula, so it is not circular.

**Other r5g15 items.**
- The removal of n≥3 in sec:gaud-local-adjoint-bounds is correct. For n=2, Ω^{n-1}=Ω, and the I+sQ_0 argument and all the constants work. The standing assumptions n≥2 and "dV a probability" still come from sec:weak-gauduchon-duality, until sec:gaud-volume-nef-limit.
- In cor:smooth-dual-exact-equation, b>0 is a valid conclusion: k_T is bounded, so by eq:integrable-current-supremum ρ_ω(f^{1/n}) = D(T) < ∞. This now happens before prop:threshold-trace-saturation is used, and that proposition needs b>0.
- Each new citation of thm:gaud-volume-dual-formula is used with n≥2:
  - its own proof, via prop:gauduchon-amgm with dV=μ, f=1;
  - prop:parallelizable-gaud-volume: θ_A is its own solution form and is balanced;
  - the warped results.
- The smooth-dual corollaries now cite thm:weak-gaud-compact-duality with F = log f. This is correct: 𝔇_F = D_{f^{1/n}}, and the unique maximizer is smooth.

**r5g16 items.**
- thm:warped-endpoint-subtraction: the parameter translation is right. With α in place of bκ, b^m becomes W, L = a+ε > 0, and σ and w are probability forms. The cited paragraph uses neither ∫κ^m=1 (that is replaced by W) nor nonconstancy or min/max of a.
- thm:radial-positive-volume-nonbig:
  - θ_ε = θ_{1,1,ε} with κ=ω (∫ω^m=1), σ=ω^m, a=x/t (nonconstant, min 0).
  - H(1,ε) = H_ε by eq:radial-volume-integration.
  - The A_ε of the lemma is the A of the theorem (A^m is the same, and the Calabi–Yau solution is unique up to constants).
  - Non-bigness: prop:warped-endpoint-closed-core with a(p)=0.
- thm:rank-two-dual-smooth-extension: u_0 is well defined by the uniqueness in thm:semipositive-dual-exact-equation. γ>0 on U because γ^{n-1}=T>0 there. r = a, as in the semipositive proof. The ending and the two examples are correct.
- lem:determinant-background-transport: the deleted paragraph (metric independence) is not used anywhere else. The new proof is complete:
  - h ≥ cg makes each quotient in eq:gaud-lower-mass-formula for h at least c times the one for g, so v_-(h) ≥ c³V. That formula is in the earlier sec:gaud-volume-extrema, valid for any Hermitian form.
  - thm:gaud-determinant-endpoint applied to h gives the norm bound.
- prop:local-mass-extremum-necessary for n=2: ddc(Ω⁰)=0 and the second variation vanishes; this is consistent with the surface remark.
- lem:nef-uniform-pairing with semipositive Ψ: only positivity of p*Ψ and ddc p*Ψ = 0 are used. Its caller uses Ψ = γ^{n-1}.
- prop:closed-core-differential-cost: only ddc B ≥ -C_Bκ_0² is used (u_0 ≤ 0, and S is strongly positive). ∫κ_0²∧S = (n-1)V_0, and the normalization by κ_0² is correct. The proposition has no other caller.
- thm:semipositive-dual-exact-equation, b>0 as a conclusion: k_T = f_0^{1-n}(det P')^{1/n} is bounded. The dropped "finite mass" follows from the equation. All callers (exponential limit, Lp limit, divisors, envelope extension, projective example) are fine.
- thm:gauduchon-moment-threshold: the citation of the proof of cor:semipositive-dual-capacity-limit puts Φ_f in the role of the barrier φ and v in the role of the L¹ limit. The hypotheses of prop:lower-barrier-criterion hold: φ−C ≤ v_λ ≤ 0, the error term I_k → 0, v ⪯ Φ_f, and P_{δω}(Φ_f) is not −∞.
- thm:constant-mass-entire-determinant-profile, upper bound: v_-(β)=V by mass invariance, then thm:gaud-determinant-endpoint (not circular) and Hölder. The label eq:constant-mass-determinant-dual is kept, and its later users (sharp concentration, fixed-determinant sections) still read correctly.

## Problems and proposals (no edit made)

**P1 (r5g16 part, optional scope relaxation).** In section_warped_endpoint_subtraction.tex, line 7, the standing assumption m≥2 is no longer needed: r5g16 kept it "because the cited thm:warped-gauduchon-volume needs it", but that theorem now holds for m≥1. Every result in the section works for m=1 (I checked the cost formula, the five rates, closed-core/Demailly–Păun and eq:warped-closed-morse). Only the example needs m≥2: for m=1, H(0)=∞.

Proposed replacements:
- l.7: "of dimension $m\geq2$, put $W$" → "of dimension $m\geq1$, put $W$"
- l.123: "For example, take $B=\mathbb P^m$," → "For example, take $m\geq2$, $B=\mathbb P^m$,"

**P2 (coordinator, research program, optional).** chapter_research_program.tex l.59: "Let $f$ be a nonzero density with $b_h(f)>0$. If" → "Let $f$ be a nonzero density. If". The statement stays true either way, since b>0 is now a conclusion of cor:smooth-dual-exact-equation. The "For n≥3" at l.168 has already been fixed concurrently.

**P3 (coordinator, already END items).** chapter_history.tex still has the stale text that r5g15 §7 names: l.684 ("arithmetic–geometric mean inequality for matrices then determines…") and l.688 (it cites thm:kn-continuous and invariance of the mass). r5g15's proposed replacements there are correct.
