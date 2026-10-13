# a5i audit of r5g10 (base 1fece9c)

## Verdict
**r5g10: CORRECT AFTER FIXES.** I made one substantive fix (a citation to a deleted remark) and one punctuation fix. Everything else checks out.

## What I checked
- **10 hypothesis removals or scope changes:**
  - Y=P^k generalized to an arbitrary closed Kähler factor, and the lemma now allows every g in L^1;
  - the standing v_-(h_0)=0 in sec:zero-lower-mass;
  - v_-(h_0)=0 and k≥2 in the radial selection section;
  - k≥2 in the residual section (standing assumption and prop:radial-zero-annulus);
  - k≥2 in the singular-obstacle section;
  - v_-(h_0)=0 in cor:radial-residual-nonclosed-product;
  - the normalization in thm:continuous-potential-curve-exponential;
  - h+dd^c u≥h/2 dropped from thm:logarithmic-critical-density;
  - the trimmed conclusion of thm:power-capacity-critical-equation.
- **6 duplicate removals:**
  - the split-product facts, 4 copies plus the full-product copy;
  - lem:bounded-exponential-supersolution and its 5 uses;
  - lem:radial-nonlogarithmic-type;
  - the envelope-class proofs, now cited from prop:relative-elementary;
  - the mass collapse, now cited from cor:individual-positive-threshold-exponential;
  - Step 4, now cited from thm:lower-mass-obstructing-measure.
- **4 simplified proofs:**
  - the KN-plus-Stokes scalar in lem:split-product-normalization;
  - Steps 2 and 3 of the power-capacity theorem;
  - b_h(f)=1 in thm:logarithmic-critical-density.
- I also read the full math diff and the concision edits, including the deleted remarks and their callers.

## Priority items
- **lem:split-product-normalization is correct.**
  - (1) holds for every v in PSH(Y,κ): the binomial expansion leaves only the j=k term, and passing through truncations gives the extended measure.
  - (2) In the bounded case, thm:kn-continuous applies on Y: Y is connected, κ is Hermitian, the reference volume κ^k is smooth and positive, and a bounded nonzero g is in L^p. Stokes for bounded potentials and closed κ gives c=1/M_g, then (1) and uniqueness of the scalar (prop:vanishing-exponent) give c_H. The truncation sandwich and the direction of the monotonicity are correct.
  - (3) is correct.
- **Callers of the lemma all fit:**
  - Steps of thm:zero-lower-mass-product-equation, including ∫f dV=1;
  - thm:closed-factor-integrable-equation and prop:closed-factor-density-roots (g=|ξ|^N);
  - eq:singular-curve-product-identity (k=1, C=N);
  - the radial selection section (W_j, the limit w, the corollary);
  - cor:radial-residual-nonclosed-product;
  - prop:singular-radial-full-product (factors renamed, C=binom(N,k)).
- **Nothing cites the deleted Steps.** After "Until subsec:closed-factor-equations, let Y=P^k", every later user states Y=P^k or Y=P^1 explicitly.
- **lem:bounded-exponential-supersolution is correct.**
  - Hypotheses: λ>0 is needed for e^{λt}≤e^{λ(s−ε)} on {t<s−ε}. ν may be any positive measure (non-pluripolarity follows automatically). h is Hermitian, hence semipositive and big as thm:singular-strict-domination requires. P_{h/2}(t)≥inf t, s−ε⪯t, and competitors may be unbounded with infinite mass.
  - All three replaced arguments are covered, including unbounded competitors in thm:continuous-potential-product-threshold. In lem:positive-exponent-uniform-upper-barrier the inequality MA(t_τ)≤e^{λt_τ}f dV holds for every λ≥τ because t_τ≥0. The two uses in lem:radial-greatest-separated are also correct (ν=q_jκ^k on Y, ν=q_αμ on X).
  - The forward reference from sec:continuous-potential-product-measures is not circular: the lemma uses only thm:singular-strict-domination, which is the first section of the chapter.
- **k=1 in the radial sections works:**
  - the profile is nondecreasing because the total potential is bounded above at o;
  - the flux formula and the k-th roots hold;
  - the moment boundary is α<1/2;
  - closed-class uniqueness is trivial on curves;
  - the tangential real Hessian direction exists in real dimension 2;
  - trivial ideals hold.
  - The deleted claim B'≥0 is not needed: a finite convex minorant of g lies below C_F, and supporting slopes are in (0,1] because g→−∞ on the left and g=x+o(1) on the right.
- **Power-capacity Step 3.** sec:psh-local-capacity states weak convergence of products for uniformly bounded psh functions converging in capacity. sec:hermitian-capacity transfers this to smooth backgrounds. Here −M≤φ_j≤0 and the convergence is uniform, so the citation applies.
- **Power-capacity Step 2.** The lower bound on Cap_h(U_D) from the first estimate of Step 1 (c_j≤c_1, D fixed) combined with eq:global-capacity-tail gives M.
- **thm:continuous-potential-curve-exponential:** Stokes on P^1 gives the normalization, so uniqueness and the barrier arguments still hold.
- **Step 4 citation:** correct and earlier in reading order.
- **h+dd^c u≥h/2 and f≥c:** no caller used either. Positivity of ∫f still follows from eq:logarithmic-density-radial.

## Problems found and fixed
1. **section_logarithmic_critical_density.tex, l.69.** The new proof of b_h(f)=1 cited "lem:bounded-normalizer-subsolution and the remark following it". r5g09 deleted that remark from section_lower_mass_solvability.tex, so the citation pointed at nothing.
   - **Old:** "Since $u$ is bounded and … the remark following it, applied with $g=f$ and $c=1$, show that … satisfy $a\leq1$; the potential $v=u$ attains $a=1$. Hence …"
   - **New:** "Suppose that $v\in\PSH(X,h)$ and $a>1$ satisfy $\mathrm{MA}^{\mathrm{ext}}_h(v)\geq af\,\mathrm dV$. For every real $A$, the bounded potential $u+A$ satisfies $\mathrm{MA}_h(u+A)=f\,\mathrm dV\leq a^{-1}\mathrm{MA}^{\mathrm{ext}}_h(v)$, $P_{h/2}(u+A)\geq\inf_Xu+A$ and $v\preceq u+A$. \Cref{thm:singular-strict-domination}, with $\delta=1/2$ and $c=a^{-1}$, gives $v\leq u+A$, which fails for sufficiently negative $A$ at a point where $v$ is finite. Hence every subsolution coefficient is at most $1$, and $u$ attains $1$, so $b_h(f)=1$ by \cref{thm:individual-density-subsolution}."
   - The cited theorem is in the first section of the chapter, so there is no forward reference.
2. **section_power_capacity_threshold_equation.tex, l.21.** The display eq:power-capacity-exact-threshold ended with "." and was followed by "where $b_h(f)>0$." I changed the "." to ",".

Compile check (`chapcheck.sh a5i chapter_prescribed_equations chapter_normalization`, two runs): no errors, no overfull boxes, no undefined references. The only message is the allowed Underfull 1783 in subsection_singular_product_adjoints (not one of my files).

## Proposals (not edited)
- **section_individual_exponential_equations.tex, l.15–21 (optional).** lem:bounded-exponential-supersolution is a special case of cor:singular-exponential-order (sec:singular-domination). Off the pole set of s, e^{−λt}MA_h(t)≤ν≤e^{−λs}MA^ext_h(s). Proposed proof: "Off the pole set of $s$, $\mathrm e^{-\lambda t}\mathrm{MA}_h(t)\leq\nu\leq\mathrm e^{-\lambda s}\mathrm{MA}^{\mathrm{ext}}_h(s)$. The bounded $t$ admits a smaller-background envelope and $s\preceq t$, so \cref{cor:singular-exponential-order} gives $s\leq t$." Citing that corollary directly in section_continuous_potential_product_measures.tex l.236 would also remove the forward reference.
- **chapter_prescribed_equations.tex, l.22.** I agree with r5g10: "on products with a projective space of dimension at least two," → "on products with a projective space,".
- **chapter_history.tex, l.581.** "It assumes zero lower mass of the factor and makes no assertion" → "Only its last assertion assumes zero lower mass of the factor, and it makes no assertion".
- **chapter_research_program.tex, l.41.** "and bounded comparison extends greatestness to unbounded competitors" → "and singular strict domination extends greatestness to unbounded competitors".
- **r5g10's other proposals** (research_program l.93; history l.186, 557, 578): checked, and accurate.
- **section_radial_residual_regularity.tex, subsection title "Products with a zero-lower-mass factor" (cosmetic).** The corollary now covers any Hermitian factor. Optional new title: "Products with a Hermitian factor".
