# Audit a4d (reports r4g20 to r4g24, plus coordinator edits)

## Verdicts
- **r4g20** (Hopf traces, ruled trace masses): EDITS CORRECT.
- **r4g21** (Hessian adjoint bounds, oscillatory example, warped subtraction): EDITS CORRECT.
- **r4g22** (intrinsic profile, fixed determinant data, sharp concentration, ruled residual, small fixes): EDITS CORRECT.
- **r4g23** (LCK least eigenvalue, Kodaira gauges, Chern–Ricci rigidity proof, openings): EDITS CORRECT.
- **r4g24** (countable divisorial positivity, quotient/toric ideals, openings): EDITS CORRECT.
- **Coordinator edits** (opening of the Gauduchon chapter, opening of the radial section): CORRECT AFTER FIXES (3 local precision fixes, listed below).

## Checked
About 44 corrections and 11 renamings, each against the diff from e2cac72 and the current text, with the computations redone:
- **Renamings:** w_j→w_{a,j} and v→g (Hopf); 𝒱_ε→𝒰_ε, "factor"→"multiplier", d→\mathrm d (Hessian); MA^ext→MA, b→ψ, h→g, Z→Y, B→D′, ϵ→ε (r4g24). Each is complete in its scope with no clashes. 𝒰_ε does not occur elsewhere in the chapter, and MA_θ is the convention of chapter_mass_bound_volumes.
- **mathdiff3 on all files:** every display change is either a listed correction or typographic. The two references dropped from the ruled residual file (eq:ruled-logarithmic-moving-volumes, eq:ruled-residual-rough-mass) were replaced by explicit values or pointers, and both labels are still defined.

Items re-derived include:
- P=[0:…:1:0] = L∩B, and I(tU)=I_L^{max(⌊t⌋−d+1,0)};
- the hypotheses of thm:kahler-target-exact-trace with Ω_0=Cκ;
- R quasi-psh via lem:nonclosed-divisorial-removal, and Siu level sets giving zero Lelong number at very general points;
- ε_L<(c−b)/2 needed for u_X∈PSH(X,Θ), and the blowup metric on O(E) of degree −1;
- the adjoint equation from dd^c(ρQ)=0, and m=2n>2;
- the five warped rates, "positive iff r>1", the Morse identity and the example (H(0)=m/(m−1));
- the coordinate formula for Γ_{0,h}, det P_h, and c=V/M;
- a_ε=ε+2(1−ε)s², the 2×2 determinants, mean 1−τ²/2, ξ and dh_τ;
- w_ε''=4π(f_ε−1), Fourier coefficients (1−ε)^{|m|+1}, the ranks of Q for T_0, and Γ_0(T_ε)→0;
- the ruled residual (Ω²=Vμ, the derivative of √V_s, 2/√log3);
- the LCK Stokes identity, Ric^Ch(e^vω)=Ric^Ch(ω)−2dd^c v (n=2), the c^{-1}q scaling, and [J,T]=0 ⇔ S=S^+;
- ∫ℓ_jκ²=−3/2, the tail Lelong bound, the bounded residual via lem:qpsh-almost-everywhere-order, ⟨T_u²⟩=(C−A)², and the final mass ∫(θ−Aκ)²;
- dV_D=|z_1|^{-1/2}|Ω|², the rays of σ (not σ^∨) and w_0=(0,1,1), and the corrected coercivity argument in the convex-cone lemma.

## Problems found and fixed
1. **chapter_gauduchon_variational_volume.tex, opening (coordinator).** "Uniform bounds on the complex Hessian of the solution give uniform bounds for the Gauduchon multiplier" was an overstatement:
   - prop:gaud-hessian-factor-bounds needs two-sided comparability δω≤ω+dd^c v≤Λω, which a bound on |dd^c v| alone does not give;
   - the section assumes n≥3.

   Old → new: "For $n\geq3$, if the solution forms $\omega+\ddc v$ are uniformly comparable to $\omega$, their Gauduchon multipliers and the determinant densities of the corresponding exact maximizing currents are bounded above and below uniformly, without bounds on derivatives of the complex Hessian."
   - Also "When the reference form $\beta$ satisfies" → "When a Hermitian form $\beta$ satisfies". This is the hypothesis of thm:constant-mass-entire-determinant-profile; β was not introduced before.
2. **Same opening.** "Along a path of backgrounds ending at a nef point, a closed nef core …" → "On a compact Kähler manifold, along a path …". The closed nef formula and thm:closed-core-subtraction are stated only on compact Kähler manifolds. The other claims check out:
   - the intrinsic measure (lem:gaud-determinant-measure-intrinsic);
   - the sharp profile (thm:constant-mass-entire-determinant-profile);
   - the torus loss of ellipticity and the concentration;
   - the warped and ruled costs.
3. **section_radial_positive_volume_nonbig.tex, opening (coordinator).** "the same background" was not exact:
   - The warped example has a=x on ℙ^m and an arbitrary curve C; here a=x/t=mx/(m−1) and C=ℙ^1.
   - The warped example itself states the rescaling, which gives H(0)=1 and 𝒱=n.

   New text: "In the example following \cref{thm:warped-endpoint-subtraction}, taken with $C=\mathbb P^1$ and with its coefficient multiplied by $m/(m-1)$, the endpoint is the background $\theta$ defined below, so that theorem already gives the value of its volume; in this section we treat this background directly and construct an explicit bounded potential realizing that value." The next sentence, "In the example, the coefficient …", became "In this background, the coefficient …" so it is not confused with the warped example.
   - Checked: the warped example's non-bigness, and the absence of a closed core, rest only on prop:warped-endpoint-closed-core in the warped section (Stokes and Demailly–Păun). They do not depend on the later radial section. The forward reference to eq:radial-volume-integration in the warped example is elementary polar integration and is not circular.

chapcheck a4d chapter_gauduchon_variational_volume: no errors, no overfull boxes, no undefined references. The only line is the known Underfull (badness 1783).

## Not fixed (minor, no action needed)
- **Hopf, lem:dominant-divisorial-extraction:** it uses the factorization of resolutions from the history.
- **Countable divisorial, r4g24 step:** it uses the factorization of surface modifications into point blowups. This is classical but not proved in the book; the history reference covers it.
