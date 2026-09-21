# Quantitative questions after the root-tail construction

**Update, 22 September2026:** The continuity characterization is now proved and audited in checkpoint42, Section27.11.1. The quantitative scalar-rate proposal below remains unaudited.

22 September 2026. Research-only deductions, not submitted to either bounded audit for the root-tail/current-attainment or trace-saturation supplements. Do not present these as checked book results.

Let p=f^(1/n) belong to D_h^0, be nonnegative and nonzero; write R=rho_h(p)=b_h(f)^(-1/n). Let u_lambda be the greatest positive-exponent solution from checkpoint40, v_lambda=u_lambda-sup u_lambda<=0, and c_lambda=exp(lambda sup u_lambda). The existing theorem gives b<=c_lambda<=b_h(exp(lambda v_lambda)f).

The normalized h-psh family has uniformly bounded L^{2n} norms by lem:uniform-exponential. Since rho_h is bounded by C||.||_{2n}, there is C_h independent of the normalized potential v and lambda>0 such that

    rho_h(p(1-exp(lambda v/n)))
       <= rho_h(p 1_{p>K}) + C_h K lambda.

Indeed split off min(p,K), use 0<=1-exp(lambda v/n)<=lambda(-v)/n on that part, and bound the remaining part by p 1_{p>K}. All terms used as roots are in Ln: the exponential difference is bounded by1; the bounded part times v belongs to L^{2n}. Put eta(lambda)=inf_{K>0}[rho_h(p1_{p>K})+C_h K lambda]. The tail property makes eta(lambda)->0. The triangle inequality then yields

    R-eta(lambda) <= rho_h(p exp(lambda v_lambda/n)) <= R.

Whenever eta(lambda)<R,

    b <= c_lambda <= (R-eta(lambda))^(-n),
    0 <= log(c_lambda/b) <= -n log(1-eta(lambda)/R).

This gives a modulus depending on the root tails. It does not in general make lambda^{-1}log(c_lambda/b) bounded. Thus D_h^0 alone has still not supplied the uniform lower barrier or the appropriate envelope class needed for an exact limiting equation.

If p belongs to L^r for r>n, choose n<s<r. Hölder and the uniform L^{rs/(r-s)} norm of normalized h-psh potentials give

    rho_h(p(-v)) <= C_s ||p(-v)||_s <= C_r'||p||_r,

so eta can be replaced by C_r'||p||_r lambda. This recovers a bounded scalar-shift error in the familiar Lp-density regime, where exact equation existence is already known. The calculation is a consistency check, not a new existence theorem.

A stronger weighted hypothesis would bound rho_h(p(-v)) uniformly over normalized potentials, with the products required to belong to Ln. Whether a useful larger concrete density class satisfies such a condition, and whether it provides the needed singularity/envelope control in addition to a scalar rate, are separate questions.

The proposed trace-saturation result offers another route: for any threshold subsolution, its trace against a smooth maximizing sequence differs from the determinant-weighted density by a positive measure of vanishing total mass. With p in D_h^0 the limiting trace can be identified along a convergent maximizing sequence. A singular maximizing current cannot simply be multiplied by dd^c u. A quantitative ellipticity or regularity statement for these maximizers would be additional input, not a consequence of their weak compactness.

## Exact scope of the tail condition (further unaudited deductions)

For a nonnegative p in D_h, the following should be equivalent: p is in D_h^0; the family p k_T over all normalized Gauduchon currents is uniformly integrable; and F↦log b_h(e^F p^n) is continuous at zero along uniformly bounded measurable F_j→0 in measure.

The forward implications use the proved tail split and dominated convergence in D_h. For uniform integrability implying tails, the sets {p>K} have volume tending to zero, and the supremum of the weighted masses on these sets is exactly rho_h(p1_{p>K}) by the integrable-current supremum formula.

If tails do not vanish, let delta>0 be a uniform lower bound along a sequence K→infinity. Choose A with e^(A/n)delta>2rho_h(p), and let F_K=A1_{p>K}. These perturbations are uniformly bounded and tend to zero in measure, but rho_h(p e^(F_K/n))>=e^(A/n)delta>2rho_h(p), so the logarithmic threshold stays separated from its value at zero. One can try to replace these characteristic functions by continuous cutoffs selected using a near-optimal smooth Gauduchon test for each tail. This continuous-cutoff step needs its own written approximation argument.

No conclusion about existence of a singular supporting probability follows merely from failure of uniform integrability. Weak compactness of a family of absolutely continuous measures and absolute continuity of every weak limit do not by themselves imply uniform integrability. Do not infer a singular adjoint or failure of all weak-current maximizers from this argument.
