# Optimal oscillation modulus for kernel probabilities — checkpoint433

The linear estimate in Proposition26.5.3 can be sharpened by retaining the probability of a fixed measurable set instead of maximizing the infinitesimal L1 bound first. The same positive coherent-state operator proves an exact logistic comparison. This is a direct consequence of the checked finite reproducing identities; no external premise or novelty claim is made.

## Every measurable set

Keep m>=1 and one nonempty selected space V_m fixed. For real continuous v,w put q=w-v, v_t=v+tq for0<=t<=1, a=m osc(q), mu_t=B_vt nu/N_m and Q_t the positive selfadjoint Markov contraction of Lemma26.5.1. For a Borel set A put p_t=mu_t(A), h_t=(I-Q_t)1_A. Integration against1_A is a bounded linear functional on finite measures with the full total-variation norm. Consequently the total-variation derivative in equation(26.10) gives

    p'_t = -m integral q h_t dmu_t.

The function h_t is nonnegative on A, nonpositive off A and has zero mean. Thus its positive and negative masses both equal

    L_t=p_t-<1_A,Q_t1_A>_mu_t >= 0.

Bounding q between its infimum and supremum on these two pieces gives |integral q h_t|<=osc(q)L_t. Positivity of Q_t on the mean-zero function1_A-p_t gives <1_A,Q_t1_A>>=p_t^2. Hence

    |p'_t| <= a p_t(1-p_t).

This holds for every fixed Borel set, not just the varying positive set of the derivative density. Indicators belong to L2(mu_t); no approximation of an indicator by continuous functions is used in this calculation.

## Endpoints and integration

For every real norm weight the kernel is positive precisely off the common zero locus of V_m, and vanishes on it. Thus all mu_t are mutually absolutely continuous: they have positive densities on the same complement relative to nu. If p_0 is zero or one, p_t is the same endpoint for every t and the comparison is automatic. Otherwise p_t stays in(0,1), so its log odds satisfy

    |d log(p_t/(1-p_t))/dt| <= a.

After integration, write sigma(z)=exp(z)/(1+exp(z)). If p_1>=p_0 and z=log(p_0/(1-p_0)), then

    p_1-p_0 <= sigma(z+a)-sigma(z)
              =sinh(a/2)/[cosh(z+a/2)+cosh(a/2)]
              <=tanh(a/4).

The reverse order follows by swapping the endpoints. The case a=0 gives equality of the probabilities. Since the signed difference has mass zero, its full total-variation norm equals2 sup_A |mu_1(A)-mu_0(A)|. Therefore

    ||mu_w-mu_v||_TV <=2 tanh(m osc(w-v)/4).

The formula is strictly stronger than min(2,m osc(w-v)/2) at every finite positive oscillation. Its small-oscillation slope agrees with the derivative bound. Constants in w-v cancel; both weights use exactly the same selected space, metric and volume. This does not compare jumping multiplier ideals or prove differentiability of a limiting envelope.

## Sharpness within smooth weights

Fix a>0 and m>=1. On P1 take the trivial line bundle with unit metric, selecting potential zero and normalized Fubini--Study area nu. Its selected space is the constants for every degree, of dimension one. For any real continuous norm weight u its kernel probability is exp(-m u)nu/integral exp(-m u)dnu.

Choose a spherical cap A of nu-mass p=1/(1+exp(a/2)); its smooth boundary has area zero. Smooth cutoff functions chi_j in[0,1], equal to one on an inner cap and zero outside an outer cap, can tend to1_A almost everywhere. For sufficiently large j their oscillation is exactly one. Take v=0 and w_j=-a chi_j/m, so m osc(w_j)=a exactly. The kernel probability densities are exp(a chi_j)/Z_j, with Z_j=integral exp(a chi_j)dnu. Bounded convergence yields total-variation convergence to exp(a1_A)nu/Z, where

    Z=1-p+exp(a)p=exp(a/2).

The limiting mass of A is exp(a)p/Z=1-p. The limiting density is greater than one on A and less than one off A. Its full total-variation distance from nu is

    2[(1-p)-p]=2 tanh(a/4).

Normalized densities converge in L1: the unnormalized densities are uniformly bounded and converge almost everywhere, while their positive normalization constants converge. The distance itself therefore converges by the triangle inequality. The bound is optimal as a supremum over smooth weights already in dimension-one section spaces. Exact attainment by a nonconstant smooth weight on a connected manifold is not asserted; the smoothing transition is retained in each approximant. At a=0 the sharp bound is zero by constant invariance.

## Scope and next integration

The complete121-line stability input and285-line partial-kernel root are reused at their actual432 first/second-read scope. Its four direct proofs already supply the positive operator, total-variation derivative and common zero locus. The automatic second complete read of this argument checks arbitrary Borel sets, absolute continuity at the endpoints, the log-odds derivative, logistic identity, full-norm factor two and smooth sharpness sequence. The eight-list literature scan is reused from431; there is no new broad retrieval or historical-gap repair here.

The next revision should strengthen equation(26.11) in its existing proposition and replace only its global-comparison proof paragraph, retaining the infinitesimal argument. A compact sharpness example belongs immediately after it. Keep the rescaled analytic proposition and inverse-degree fiber example intact, distinguish supremal sharpness from attainment and preserve all original open-problem statuses.

All334 book files and1016 proof bodies, both catalogues/manifests,451 protected sources and six incoming author blobs remain exact. Package validation passes with2175 archive entries,2174 checksum-validated current payloads and331 book-source files matching the actual432 empty reconstruction. No new author build, empty reconstruction, native call or publication occurs.
