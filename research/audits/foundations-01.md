# First mathematical audit: smooth foundations

Date: 2026-09-14. Reviewer: primary research agent. This is a direct mathematical audit, not an independent Rethlas verification or formal proof certification.

## Scope

Three drafted chapters: background forms/local singularities; smooth mass; raw Monge-Ampere one-form. All displayed product calculations are explicitly restricted to smooth functions and forms. No proof of non-pluripolar continuity or unbounded mass invariance is inferred from them.

## Checks completed

- Normalization: dc=i/(4pi)(bar-partial minus partial), ddc=i/(2pi)partial bar-partial agrees with SGPT. Ideal uses exp(-u); polar integral gives floor(lambda), including integer endpoints.
- Canonical representative: local correction starts with a qpsh function, so positivity of the complex Hessian is applied to its canonical representative, not to an arbitrary upper-semicontinuous modification on a null set.
- Positive linear combinations omit zero terms. Ordinary order uses inequalities on pole sets, never undefined minus-infinity differences.
- Smooth gauge change theta'=theta+ddc f maps u to u-f, preserves current, and cannot change dtheta.
- Line-bundle curvature proposition specifies locally integrable weights, ensuring a distributional curvature exists.
- Integration-by-parts sign: integral ddc f wedge T = integral f ddc T, checked by two Stokes identities and dc d = -d dc.
- Leibniz sign: ddc(omega^q)=q omega^(q-1) ddc omega +q(q-1)omega^(q-2)domega wedge dc omega.
- Mass expansion: highest exact wedge integrates to zero; remaining terms integrate one ddc onto the smooth background power. No assertion of uniform boundedness follows.
- Surface mass invariance iff ddc omega=0 follows by the formula and arbitrary small smooth variations. No higher-dimensional converse is claimed.
- Torus example: beta_j=i/(2pi) dz_j wedge dbarz_j; ddc f(x1)=(f''/4)beta1. Positivity holds for |t|<pi^-2. Period averages yield M(t)=(4-pi^2 t)B. Negative t increases mass and gives the stated comparison counterexample after an additive shift.
- Comparison principle implies constant mass: shift to make comparison set all X, then exchange functions. This assumes the principle for all smooth pairs, exactly as stated.
- Smooth upper-mass metric independence: positive forms ordered by C, scale potential by C. No unjustified lower-mass analogue asserted.
- Primitive obstruction: mixed partials on a two-dimensional affine plane; constant tangent direction tests ddc(omega_u^(n-1)). No infinite-dimensional differentiability theorem is needed.
- Closed energy derivative: explicit telescoping after integration by parts against d- and dc-closed mixed powers.
- Surface radial functional: variation of (1/3)integral u(ddc u)^2 has three equal terms; remaining correction is integral v[u ddc omega+du wedge dc omega-dc u wedge domega].

## Remaining mathematical tasks

1. Audit deeper local psh inputs if making the foundations fully self-contained (canonical representative criterion and local ddbar lemma are currently standard stated background).
2. Determine the full primitive criterion. Current necessary condition in the constant direction is deliberately not called sufficient.
3. Relate smooth bounded-mass definition to bounded nonsmooth potential definitions only after a verified approximation argument.
4. Do not infer universal finite mass from the initial varying-mass torus example; audit XZ26 separately.
5. Read the published BGL25 version before citing its theorem numbering; the arXiv download is a 2024 v1.

## Typesetting verification

Initial 25-page PDF compiled successfully. One overfull line was rewritten; final log after that revision had no overfull/underfull boxes, unresolved references or warnings. All 25 pages rendered and viewed in contact sheets; energy proof page also inspected at 140 dpi. The original svmono layout includes recto chapter starts and blank versos. Final wording and PDF metadata revision rebuilt successfully; latest log has no listed warnings or unresolved references. Changed page rendered again for final visual check.
