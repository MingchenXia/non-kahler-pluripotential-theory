# Further questions after the Gauduchon threshold formula

22 September 2026. Working note, not in the book; none of the proposed further implications below has been independently audited. The two checkpoint40 submissions have their own exact scopes. Preserve this separation.

## The order-continuous part of the root space

Let D_h have its complete norm N_h(p)=||p||_Ln+rho_h(p), assuming the submitted Gauduchon formula. Let D_h^0 be the N_h closure of bounded functions. The following functional-analytic deductions should be checked before use:

- For p>=0 in D_h, bounded truncations tend to p in N_h if and only if rho_h(p 1_{p>K})->0. One implication follows from (p-K)_+<=p1_{p>K}; the reverse follows from p1_{p>2K}<=2(p-K)_+ and order. L^n tails always vanish.
- This is also a criterion for p to belong to D_h^0: bounded approximants a give (p-K)_+ <= |p-a| for K>=||a||_infinity, and solidity transfers the norm estimate. Signed functions reduce to their absolute values using bounded signed truncations.
- The exact Gauduchon representation makes the condition uniform integrability of p against the family of normalized Gauduchon test densities: sup_gamma integral_{p>K} p a_gamma dV ->0. Thus bounded-function density in D_h is a geometric uniform-tail question, not a consequence of L^n density.
- If p lies in L^r for some r>n, the lower L^{r/n} density estimate gives rho_h(p)<=C_r||p||_Lr. Hence such p lie in D_h^0. If v_->0, D_h=D_h^0=L^n with equivalent norms. The zero-lower-mass case remains to be characterized.

Potential equation question: does a positive density whose root lies in D_h^0 admit an exact equation at b_h(f), and is this condition enough to get capacity convergence of the normalized exponential solutions? No proof is presently claimed. The tail criterion only gives subsolutions for small residual densities; it does not itself put the needed common roofs in a full-mass class.

## The zero-exponent obstruction

At b=b_h(f)>0, let u_lambda be the greatest exponential solution and v_lambda its sup-normalization. The checked candidate argument gives c_lambda=e^{lambda sup u_lambda}->b and a lower bound

    v_lambda >= v - lambda^{-1} log(c_lambda/b)

for one normalized threshold subsolution v. Convergence c_lambda->b alone does not bound the error; a rate O(lambda) for log(c_lambda/b), a common-envelope estimate, and/or an independent capacity compactness theorem would be additional input. A finite L1 limiting potential and total-variation convergence of equation data are not sufficient by themselves.

The Gauduchon formula suggests testing quantitative near-minimizers for f, but their normalized coefficients may become unbounded at the endpoint. No uniform estimate is inferred from a fixed smooth-density minimizer or from the subcritical coefficient bound.

## General measures

The density-root formula involves f=dmu/dV and does not directly extend to singular non-pluripolar measures. Inserting only the absolutely continuous part would discard singular mass, even in the Kähler setting where the equation normalization depends on the entire finite measure. A general-measure analogue needs a different pairing or approximation theorem; weak convergence of measures is not an authorized replacement for L1 convergence of densities.

## Literature check

A primary-source search located Lu–Phung, On uniqueness of solutions to complex Monge–Ampere mean field equations, Bulletin of the London Mathematical Society 57 (2025), 3163–3180, DOI https://doi.org/10.1112/blms.70149. Read the publisher's Section4 and its displayed equation(4.1): that section treats Lp data, p>1, and the mean-field sign is exp(-gamma u). Its bounded local maximal-subsolution lemma is not a proof of the unrestricted genuine-subsolution theorem here. This check gives context only and is not a literature-priority claim or a new proof dependency.
