# P08 radial counterexample: independent intake review — checkpoint435

The author commit9e0d478ef870b095614ef41c9d97a7a3c4a771ef supplies the anonymous267-line article `research/papers/P08-projective-radial-counterexample.tex`. Its complete first and automatic second source reads pass. The original article and authored review/report blobs are preserved; historical verifier verdicts are provenance, not premises, and no verifier runtime is used.

## Global radial construction

Put n=m+1 with m>=2, t=(m-1)/m, B=P^m and X=B times P1. Normalize the Fubini--Study forms by integral omega^m=integral w=1. The projective function x=sum(j>=1)|Zj|^2/sum(j>=0)|Zj|^2 is global smooth, zero only at p=[1:0:...:0] and one on the infinity hyperplane. Put a=x/t, h=omega+w, mu=omega^m wedge w and theta=omega+a w. Pullbacks are implicit. The background is semipositive, nef and nonclosed: theta+eta h>0 and dtheta=da wedge w is nonzero.

For radial integrable b, direct polar integration gives integral_B b(x)omega^m=m integral_0^1 b(y)y^(m-1)dy. Hence integral_B omega^m/a=mt/(m-1)=1. For epsilon>0 let H_epsilon=m integral_0^1 y^(m-1)/(y/t+epsilon)dy and define

    q_epsilon(x)^m=(m/H_epsilon) integral_0^x y^(m-1)/(y/t+epsilon)dy,
    phi_epsilon(x)=integral_0^x [q_epsilon(y)-y]/[y(1-y)]dy.

The positive root is used. At zero q_epsilon=x times the positive smooth root of (m/H_epsilon)integral_0^1 u^(m-1)/(xu/t+epsilon)du. At one q_epsilon(1)=1. Both derivative singularities of phi_epsilon are removable, so phi_epsilon(x) is global smooth. In the affine chart s=|z|^2, sF'_epsilon=q_epsilon for F_epsilon=log(1+s)+phi_epsilon(s/(1+s)). Its tangential and radial eigenvalues are q_epsilon/s and dq_epsilon/ds, both positive. The smooth closed form A_epsilon=omega+ddc phi_epsilon satisfies

    A_epsilon^m/omega^m=q_epsilon^(m-1)q'_epsilon/x^(m-1)
                             =1/[H_epsilon(a+epsilon)].

At infinity the global smooth form is semipositive by limiting its positive affine matrices; the extended determinant is strictly positive, so every eigenvalue is positive. This checks every infinity chart, rather than extrapolating only the affine calculation. At p the smooth factorization gives strict positivity directly.

## Canonical bounded endpoint

Monotone convergence gives H_epsilon->1 and q_epsilon(x)->x^t for x>0. A decreasing weight relative to density m y^(m-1) shifts normalized cumulative mass upwards; an increasing ratio y/(y+t epsilon) relative to density (m-1)y^(m-2) shifts it downwards. Splitting either probability at x proves these comparisons. Therefore x<=q_epsilon(x)<=x^t.

The function phi(x)=integral_0^x (y^t-y)/[y(1-y)]dy is bounded continuous, since t>0; its derivative extends smoothly at one and it is smooth off p. The displayed comparison supplies an integrable derivative majorant, so dominated convergence gives uniform convergence phi_epsilon->phi on all B. Distributional convergence makes A=omega+ddc phi positive and closed. Local potentials are continuous uniform limits of genuine psh functions, with the canonical value phi(p)=0. Off p, A is smooth strictly positive and A^m/omega^m=t/x=1/a, also at infinity. No singular endpoint power is required for the following argument.

## Every Gauduchon test and explicit minimizing metrics

The positive current Omega=A+a w equals theta+ddc phi. Off Z={p} times P1, it is smooth strictly positive with Omega^n=n mu. For every smooth positive Gauduchon gamma, distributional Stokes replaces theta by Omega in the numerator. Matrix AM--GM on X minus Z gives the pointwise lower bound n^(1/n)(mu/gamma^n)^(1/n)gamma^n. Z has zero smooth volume; the positive numerator measure on Z cannot lower the integral. Thus the bound lambda_mu(theta)>=n^(1/n) holds for every original test, including tests with no symmetry.

Put theta_epsilon=omega+(a+epsilon)w, Omega_epsilon=A_epsilon+(a+epsilon)w and c_epsilon=n/H_epsilon. These satisfy Omega_epsilon^n=c_epsilon mu. The actual smooth positive metric gamma_epsilon=(a+epsilon)^(-1/m)Omega_epsilon has

    T_epsilon=gamma_epsilon^m=(a+epsilon)^(-1)A_epsilon^m
                                  +m A_epsilon^(m-1) wedge w.

Its first term is a base top-degree form and its second is closed, so dT_epsilon=0. Smooth Stokes gives integral theta_epsilon wedge T_epsilon=n; the denominator is c_epsilon^(m/n)H_epsilon. The quotient equals c_epsilon^(1/n), and AM--GM gives the matching all-test lower bound. Consequently V_mu(theta_epsilon)=n/H_epsilon. The same tests have unperturbed quotient at most c_epsilon^(1/n), so V_mu(theta)=n. The original theta+eta h regularization agrees: monotonicity gives one inequality and each fixed test gives the reverse limit before taking its infimum. Endpoint smooth attainment is not asserted.

## Independent nonbigness proof

A direct closed test simplifies the article's valid Haar-averaging argument. Suppose theta+ddc v>=delta h for a global quasi-psh v and delta>0. Choose a nonzero smooth f>=0 on B supported where a<delta. The pullback S=f omega^m is smooth semipositive of bidegree(n-1,n-1) and closed by base top degree. Distributional Stokes and positivity would give

    0<=integral_X (theta+ddc v-delta h) wedge S
      =integral_B f(a-delta)omega^m<0.

This contradiction excludes every quasi-psh strict representative. Compact equivalence of Hermitian metrics makes this fixed h test sufficient for bigness. S is a semipositive closed test, not a smooth positive Gauduchon metric; its use here does not enlarge or replace the volume's test family. Neither proof restricts a singular current to a fiber.

## Scope, placement and migration

The counterexample disproves original unrestricted P08 in every n>=3. Bigness still implies positive volume. Positivity for other smooth probability densities follows from the already proved density comparison, although the exact value n refers to the displayed mu. The surface question, closed non-Kahler classes, flow endpoints and geometric criteria remain separate; this is not a novelty, classification or dimension-two claim. Current local-integrability, distributional Stokes, positive-current smooth wedges and uniform psh limits are accepted book foundations, not newly certified external proof trees. No fresh Demailly retrieval or external primary theorem is adopted.

Placement reads cover the complete277-line Chapter25 root, complete159-line closed-core subsection, complete48-line collapse input and Chapter32 root1--110, with the existing history seam285--306. They distinguish the all-test volume from the bigness threshold and identify the obsolete conjecture and Chapter25 open-converse sentence. These are scoped reads, not fresh whole-recursive Chapters25/32/33 certification. The new radial section belongs after the closed-core subsection. Integration must replace the settled universal conjecture, keep the original catalogue statement historically intact, and update P12/P14's conditional discussions without claiming their specialized questions solved. The introduction's corresponding assertion also needs a fresh source check.

Next: integrate complete proofs in Chapter25, make P08's negative resolution explicit and migrate both catalogues to39 open original directions. At this research-only checkpoint the book and both catalogue files still retain checkpoint434 verbatim; their stored count remains40 pending that migration. No author build, native catalogue call, new public release or new arXiv scan occurs.

All334 book files and1017 proof bodies, both catalogue files and original manifests, and451 protected sources remain exact. Five immutable P10 blobs and all six P08 intake blobs match their author commits; the shared author README advances only with the new P08 commit. Package validation passes with2181 archive entries,2180 current checksum-validated payloads and331 book-source files identical to the actual434 empty reconstruction. Original supplied papers/reports receive no additional source-package copy. No new author build, reconstruction, native call or publication occurs.
