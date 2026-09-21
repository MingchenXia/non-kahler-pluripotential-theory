# Review of individual-density stability and exponential equations

22 September 2026. Integration review for checkpoint40. The production baseline is checkpoint39, private head `04a244c8da9fd35b10a6472e0e938c555ef4869e`. Both bounded reviews and the final production build have passed; this file records their exact scope.

## Original proofs and independent review

The first submission, `individual_density_stability_01`, contains upper L1 semicontinuity via tail upper envelopes with infimum densities, finite-sum estimates via the singular mixed inequality, completeness of the norm ||p||_Ln+rho_h(p), greatest exponential solutions from any genuine subsolution, and the zero-exponent scalar limit at positive threshold.

The normal runner exited0 and returned correct, with no errors or gaps. The root read all nine statement records, three reference records, both report records and events; failed_checks is empty. The reference checks include the already reconstructed continuous/exponential Lp results. No uniqueness among arbitrary singular potentials or exact zero-exponent equation is claimed.

The submitted sources and input remain unchanged. They remain a useful independent proof of semicontinuity and addition, even though the final exposition can be shorter after the Gauduchon formula.

## Gauduchon formula and shorter proofs

The second submission, `integrable_gauduchon_tests_01`, concerns the exact formula

    rho_h(p) = sup_gamma integral |p| (dV/gamma^n)^(1/n) gamma^n
                            / integral h wedge gamma^(n-1).

It permits infinite rho and zero b. A fixed test is continuous on Ln; the supremum need not be bounded there. The key passage to bounded measurable roots uses the uniform L^{2n/(2n-1)} bound of the test coefficients, obtained from the lower L2 norm of equation densities. Smooth root approximation in L^{2n} then gives both L2 scalar continuity and uniform convergence of the test suprema. General Ln roots follow by truncation and commuting two suprema. There is no interchange of an infimum with an uncontrolled weak limit.

The formula yields the shorter upper-semicontinuity and triangle proofs. The uniform endpoint coefficient norm would instead be equivalent to positive lower mass, and is explicitly not assumed. Metric comparison shows that the domain of finite rho and the stronger complete norm are independent of the Hermitian metric, up to equivalence. Change of smooth volume is handled by the same measure and the root-density isometry.

The additional root-norm result distinguishes the two mass properties. Finite upper mass bounds ||p||_Ln by v_+^(1/n)rho_h(p), so rho alone is complete. For infinite upper mass, smooth probability equation constants can be arbitrarily large. The chosen positive roots p_j have ||p_j||_Ln=j but rho_h(p_j)<=2^{-j}. Their partial sums are rho-Cauchy, and a fixed positive Gauduchon coefficient makes their limit an L1 function. That function dominates every p_j and thus is not in Ln. No assertion about total mass of an arbitrary singular potential enters the construction.

## Greatest exponential solutions

For f_k=min(f,k), bounded exponential solutions decrease. Strict domination compares the bounded first potential u_k with every genuine subsolution v: on {u_k<v-t}, the ratio is e^{-lambda t}<1. Boundedness supplies both the smaller-background envelope and v-t preceq u_k. A genuine subsolution prevents total collapse. A common upper translation makes the decreasing potentials nonpositive, so the existing exponential closedness theorem applies in capacity. This proves the equation, finite mass and greatestness among all genuine subsolutions. It is not uniqueness among all singularity types.

At b_h(f)>0, a normalized threshold subsolution v gives v+lambda^{-1}log b as an exponential subsolution. Hence c_lambda>=b. The normalized exponential lemma gives g_lambda=e^{lambda v_lambda}f->f in L1, and maximality of b gives c_lambda<=b(g_lambda). Upper semicontinuity forces c_lambda->b, proving total-variation convergence of the equation data. It does not prove capacity convergence of normalized v_lambda. The lower-bound error lambda^{-1}log(c_lambda/b) may be unbounded.

## Editorial interfaces and proof economy

Chapter13 places the Gauduchon tests and stability after the individual subsolution threshold. The exponential theorem appears after the existing closedness theorem and normalized-exponential lemma, so its analytic inputs are already available. Chapter32 now separates the established greatest exponential solutions from the remaining exact threshold equation and the zero-threshold exponential problem. Chapter27 links its smooth variational formula to the integrable-density extension without implying smooth minimizer attainment, extension to arbitrary singular measures, or a birational transformation law.

The smooth Gauduchon formula and mass-extrema identities used from Chapter27 have independent earlier analytic foundations: they use the smooth equation, Gauduchon conformal metric, and bounded exact regularization, not the new threshold topology. The forward references therefore cause no circular proof dependency.

The example table is a direct specialization of the reviewed implications. Corollary `cor:hopf-lower-mass` gives v_-=6 and v_+=infinity on the standard Hopf metric. Proposition `prop:lower-mass-balanced-metric` gives v_+=24pi and v_-=0 on the balanced quotient. Corollary `cor:both-mass-properties-fail` supplies the product cases. Metric comparisons preserve the relevant zero/finiteness properties. The Kähler row follows from cohomological mass. The table is a root-checked interface, not a new source theorem.

The first proposed Gauduchon theorem heading was isolated at the bottom of a page; pagination will keep its statement together. Two duplicated “lemma Lemma” phrases in the exponential draft are removed. The original standard environments, template, and upright differentials remain. No verifier input, memory or result is edited.

## Remaining work

The note `individual-density-next-questions.md` is unaudited research: uniform tails in the root space, the closure of bounded roots, possible stronger conditions for exact equations, and the obstacle to extending a density formula to singular non-pluripolar measures. It is not part of either passed proof or a theorem in the book. No novel-priority claim follows from these bounded audits or the contextual literature search.

## Final checks

The second normal runner exited0 and returned correct, with no errors or gaps. The root read all eight statement records, six reference records and both synthesis/final report records; failed_checks is empty. There are136 completed reports:130 correct and six preserved historical adverse reports whose findings were resolved. Neither these bounded reviews nor the earlier whole-book pass is whole-book certification.

The final production PDF has661 pages and every raw page text matches the inspected preview. Twenty affected/adjacent pages were rendered and read, with a further pass on the table and complete theorem/corollary statements. No errors, undefined references or overfull boxes; the single existing underfull bibliography paragraph remains. Reversible maps preserve the exact audited supplements, including the older longer proofs. The standalone note and all29 original sources are unchanged. Archive reconstruction and private publication are recorded separately.
