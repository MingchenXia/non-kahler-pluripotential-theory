# STW continuity reconstruction — full verification report

Run: `stw_continuity_reconstruction_01`

## Verdict and scope

**Correct under the explicitly stipulated conditional inputs.** No critical errors or gaps were detected in the supplied proof. The audit independently verifies the implication from the stipulated estimates to higher regularity, continuity closure, existence, and uniqueness. It does not independently establish the special second-order estimate or the detailed matrix-structure precursor. No STW existence theorem is used.

## Dependency status

Status checked at **2026-09-14 23:09 UTC**.

| Input | Recorded status | Role in this audit |
| --- | --- | --- |
| `stw_czero_01` | Correct; accepted by the user | Uniform potential and scalar bounds |
| `stw_gradient_reduction_01` | Correct as a conditional implication; accepted by the user | Converts the assumed special Hessian estimate to gradient and complex Hessian bounds |
| Cone Liouville 60: `stw_cone_liouville_01` | Correct | Accepted prerequisite of the gradient reduction |
| Matrix structure 62: `stw_matrix_structure_01` | Final verdict correct | Separate audit; not independently reverified here |
| Second order 63: `stw_second_order_reconstruction_01` | **Pending: no final verification.json at status check** | The target estimate remains an explicitly conditional input |

The absence of a completed verdict for dependency 63 is not a gap in the implication the user asked to check: that estimate was explicitly authorized as a conditional hypothesis. This report must not be cited as an unconditional independent proof of that estimate.

## Summary

The supplied higher-regularity, continuity, and uniqueness argument is correct under the expressly accepted conditional inputs. All 78 sequential deductions, two final reference-resolution checks, and four reference checks pass; no critical errors or gaps were found. [Full report](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/stw_continuity_reconstruction_01/fullreport.md).

Dependency 62 (stw_matrix_structure_01) has completed with verdict correct. Dependency 63 (stw_second_order_reconstruction_01) still had no final verification.json at the final status check, 2026-09-14 23:09 UTC. Its special complex-Hessian estimate is assumed conditionally here. Neither dependency's estimate is independently verified by this audit, and no STW existence theorem is imported.

The conventions agree: v=u/(2pi), the normalized Hodge map includes 1/(n-1)!, and det Q=exp((n-1)(F+b)). An upper eigenvalue bound M and determinant lower bound d give Q>=d/M^(n-1) I. Fixed scalar W2p estimates yield C1,alpha control and hence a uniform Calpha bound for the frozen R=Q0+Z(Dv).

The tangent infimum is finite and concave on all real symmetric matrices and equals logdet Q on actual solution matrices. Positivity and trace preservation by P_n, together with real-to-complex trace comparison, give uniform real ellipticity. Its spatial modulus is C|x-y|^alpha(1+||A||), and its value at A=0 is uniformly bounded. These match the general real local estimate in [Tosatti–Wang–Weinkove–Yang, Definition 3.2 and Theorem 3.4](https://arxiv.org/pdf/1402.0554), verified by theorem search followed by web fallback. No prior real Hessian bound or differentiability of the extension is required. Differentiating the original smooth equation then gives the asserted Schauder bootstrap, including drift.

The path starts at u=b=0 for F0=log(gamma0^n/gamma^n). Mean normalization, the positive adjoint, index zero, and the exact range condition justify openness. The determinant linearization is Lw-(n-1)c, with c=-(n-1)^(-1) integral f dmu. Uniform smooth bounds and strict spectral positivity prove closedness and thus conditional global existence. At extrema, gradient terms cancel and Hessian order gives equality of the two scalar constants. Linearizing along the positive affine segment and applying the strong maximum principle proves uniqueness of the normalized potential. The final Aeppli conclusion has the required gamma0-Gauduchon qualification. The book was not edited.

## Sequential deduction checks

The following 17 groups contain 78 deductions, ordered as in the supplied text. A further two checks resolve the regularity reference after external-source review.

### 1. Scope, conventions, and conditional inputs

Status: checked conditionally.

1. The setting is a connected compact complex manifold without boundary, n>=2, with fixed smooth positive gamma0 and fixed smooth Gauduchon gamma; F is smooth and real. These standing assumptions were confirmed in conventions.tex and thm:stw-volume.
2. The task expressly accepts the C0/b estimate stw_czero_01 and conditional gradient reduction stw_gradient_reduction_01, whose Liouville dependency stw_cone_liouville_01 has verdict correct. The uniform estimate |ddc u|<=C(1+sup|partial u|^2) is a conditional input, not proved by this audit.
3. At initial status check, matrix-structure dependency 62 (stw_matrix_structure_01) already has a final correct verdict; dependency 63 (stw_second_order_reconstruction_01) has ongoing memory records and no final verification.json. The present conclusion remains conditional on the target estimate of 63. No STW existence theorem is imported.

### 2. lem:stw-higher-regularity: rescaling and determinant normalization

Status: checked conditionally.

1. With ddc=i/(2pi) partial barpartial and v=u/(2pi), ddc u=i partial barpartial v; the first-order term becomes Re(i partial v wedge barpartial gamma^(n-2)).
2. The normalized Hodge map q(Gamma)=star_gamma Gamma/(n-1)! sends gamma^(n-1) to gamma, represented by I in a gamma-unitary frame. Wedging a (1,1)-form with gamma^(n-2) gives P_n(H)=((tr H)I-H)/(n-1).
3. Z in the v notation includes this same rescaling, as explicitly defined in section_stw_structure.tex. It is real linear in Dv with fixed smooth coefficients; there is no missing factor of 2pi.
4. If eta has gamma-eigenvalues lambda_i, Q has eigenvalues product_{j!=i}lambda_j. Thus det Q=(eta^n/gamma^n)^(n-1)=exp((n-1)(F+b)). The log determinant is relative to gamma, or equivalently taken in a unitary frame.

### 3. lem:stw-higher-regularity: uniform spectral compactness

Status: checked conditionally.

1. The accepted conditional gradient reduction turns the assumed special Hessian estimate into uniform gradient and complex Hessian bounds; rescaling by 2pi changes only fixed constants.
2. Smooth fixed Q0, linear Z(Dv), and the complex Hessian bound give ||Q||<=M, uniformly over the prescribed family.
3. The equation and uniform ||F||infinity+|b| give det Q>=d>0. Since Q is positive, each eigenvalue satisfies lambda_i=det Q/product_{j!=i}lambda_j>=d/M^(n-1).
4. Choose a strictly smaller positive a and a strictly larger b0 than these bounds. Then aI<=Q<=b0I uniformly in every unitary frame. The spectral box is fixed across the family, not chosen separately for each solution.

### 4. lem:stw-higher-regularity: fixed trace estimates and freezing the gradient

Status: checked.

1. Delta_gamma v=tr_gamma(i partial barpartial v) is a fixed smooth scalar real uniformly elliptic operator; bounded complex Hessian bounds its right-hand side in Linfinity.
2. Interior W2p estimates on nested holomorphic charts bound ||v||W2p by ||Delta_gamma v||Lp+||v||Lp. A finite cover and bounded v make the constants uniform for each finite p.
3. For real dimension m=2n choose p>m and 0<alpha<1-m/p. Sobolev-Morrey embedding yields a uniform C1,alpha bound, without assuming a bound on the full real Hessian.
4. The components of partial v in a fixed smooth local frame are Calpha. Multiplying them by the fixed smooth coefficients of Z and adding Q0 gives a uniform Calpha matrix R.
5. Freezing means treating this already bounded R(x) as a coefficient in an equation for this given smooth v. Constants in the ensuing estimate depend only on its uniform Calpha norm, so no circular regularity assumption is introduced.

### 5. lem:stw-higher-regularity: the real-to-Hermitian Hessian map

Status: checked.

1. On a holomorphic coordinate ball the coefficient matrix v_i barj is real linear in the real symmetric matrix D2_R v. Evaluation in a smooth gamma-unitary frame is a smooth complex congruence of that matrix; it does not differentiate the frame or introduce a first-order term.
2. For N>=0, its complex mixed projection H_C(N) is positive semidefinite, since evaluation is one quarter of the sum of N on a real vector and its complex rotation. In Euclidean coordinates tr_C H_C(N)=tr_R N/4.
3. Congruence by the smooth uniformly invertible frame preserves positivity. On a relatively compact ball, c_H tr_R N<=tr H_x(N)<=C_H tr_R N with c_H>0. The statement does not require a lower bound H_x(N)>=cN.
4. The map H_x is real linear and its operator norm and spatial derivatives are uniformly bounded by the fixed geometry.

### 6. lem:stw-higher-regularity: global real concave extension and equality

Status: checked.

1. The admissible tangent matrices B are all Hermitian matrices with aI<=B<=b0I in one fixed local trivialization. This set is nonempty, compact, and independent of x and of A.
2. Every tangent expression is finite affine in the real symmetric variable A. Compactness of B and a>0 ensure the infimum is finite for every A. The infimum of affine functions is concave, and its slopes are uniformly bounded.
3. For any positive Hermitian M, concavity of logdet gives logdet M<=logdet B+tr(B^-1(M-B)). If M belongs to the box, setting B=M achieves equality.
4. For the actual Hessian A=D2_R v, M=R(x)+P_n(H_x(A))=Q lies in the box, so the extension equals logdet Q exactly. No logarithm is taken of an indefinite matrix away from the solution, and no differentiability of the extension is asserted.

### 7. lem:stw-higher-regularity: uniform real ellipticity

Status: checked.

1. For Hermitian S>=0, P_n(S)>=0 because its eigenvalues are (sum_{j!=i}s_j)/(n-1); n>=2 is essential. Its trace is exactly tr S.
2. With T=P_n(H_x(N))>=0 and b0^-1 I<=B^-1<=a^-1 I, b0^-1 tr T<=tr(B^-1 T)<=a^-1 tr T. This trace bound holds without commutativity of B and T.
3. Consequently each tangent increment for N>=0 lies between lambda tr_R N and Lambda tr_R N, where lambda=c_H/b0>0 and Lambda=C_H/a.
4. The same lower and upper bounds hold for the difference of the infima at A+N and A, since the bounds are uniform in B and the index set is fixed. Thus the extension is globally uniformly elliptic on all real symmetric matrices, despite the complex Hessian projection having a kernel.

### 8. lem:stw-higher-regularity: spatial modulus and the local C2,beta estimate

Status: checked; reference subsequently confirmed.

1. For fixed B, subtraction at x,y cancels logdet B-tr(B^-1B); the remaining terms are bounded by C(||R(x)-R(y)||+||H_x-H_y|| ||A||). Taking suprema of this difference bounds the difference of the infima.
2. The Calpha bound for R and Lipschitz bound for H_x give |Phi(A,x)-Phi(A,y)|<=C|x-y|^alpha(1+||A||) on a fixed bounded ball, for every real symmetric A. In particular Phi(0,x) is uniformly bounded and Calpha.
3. The smooth given v solves Phi(D2_R v,x)=h=(n-1)(F+b), with uniform ||v||infinity and ||h||Calpha. The frozen coefficient problem has no remaining independent gradient argument.
4. The needed standard theorem is the variable-coefficient concave uniformly elliptic interior C2,beta theorem, allowing globally Lipschitz, possibly nondifferentiable dependence on A and the stated linear-growth Holder modulus in x. Choose beta below alpha and the universal constant-coefficient Evans-Krylov exponent, if necessary.
5. Applying that theorem on smaller nested balls and a finite cover gives a uniform bound on the full real C2,beta norm. Reference matching is recorded separately before final acceptance.

### 9. lem:stw-higher-regularity: linear Schauder bootstrap

Status: checked.

1. Return to the original smooth function G(x,p,A)=logdet(Q0(x)+Z_x(p)+P_n(H_x(A))) on the open positive matrix locus; do not differentiate the possibly nonsmooth extension.
2. The matrices along the solution stay in the fixed positive box. G_A is real uniformly elliptic by the same trace pairing; G_p includes exactly the drift from Z, with no zeroth-order coefficient.
3. Differentiating in a real coordinate r gives G_A^{ij} partial_ij(v_r)+G_p^j partial_j(v_r)=partial_r h-G_xr, where G_xr holds p,A fixed. G_xr contains only derivatives of fixed coefficient fields multiplied by Dv or D2v, not third derivatives of v.
4. Uniform C2,beta control gives Calpha with exponent beta for all these coefficients and the right side, with uniform bounds. Linear interior Schauder on smaller balls bounds v_r in C2,beta and hence v in C3,beta.
5. Induction differentiates the original smooth positive-matrix equation further; inverse-matrix derivatives are bounded by the positive spectral margin, and the assumed bounds on all derivatives of F give every Ck bound. Constants are uniform for the prescribed family; b itself is already bounded.

### 10. thm:stw-volume closure: starting point and normalization

Status: checked.

1. F0=log(gamma0^n/gamma^n) is smooth and real because both fixed forms are positive. At u=0, Gamma=gamma0^(n-1), its unique positive root is gamma0, and b=0 solves both the volume and determinant equations.
2. Ft=(1-t)F0+tF is smooth and uniformly bounded in every Ck norm on [0,1].
3. Adding a constant to u changes neither ddc u nor partial u, hence leaves Gamma, Q and b unchanged. Mean-zero normalization defines a closed complement of the constant kernel, and supremum normalization can be restored at the end.

### 11. thm:stw-volume closure: linearization, kernel, and adjoint

Status: checked.

1. For unscaled u, Lw=tr(Q_u^-1[P_n((ddc w)_gamma)+Z_gamma(partial w)]); equivalently the principal term has the additional positive fixed factor 1/(2pi) in real coordinates.
2. The coefficients are smooth at a smooth solution; the principal matrix is uniformly positive on compact X by the trace calculation. The operator has drift, no zeroth-order term, and annihilates constants.
3. The strong maximum principle on connected compact X gives ker L=R. This conclusion is for real functions, as required by the real equation.
4. The book's prop:gaud-volume-linearization is stated on the entire open set Gamma_u>0. Its operator mathcal L differentiates log(eta_u^n/gamma^n). Since logdet Q=(n-1)log(eta_u^n/gamma^n), L=(n-1)mathcal L; thus it has exactly the same adjoint probability.
5. The adjoint construction uses index zero, the maximum principle, elliptic regularity, and the strong minimum principle; it does not use solvability of the nonlinear STW equation. The source's introductory existence wording is not used as an assumption.

### 12. thm:stw-volume closure: index zero and exact range

Status: checked.

1. For any fixed 0<theta<1, L:C2,theta(X)->C0,theta(X) is Fredholm on the compact boundaryless manifold. Joining its principal coefficients to those of a fixed scalar Laplacian through positive coefficients and removing drift preserves ellipticity and index.
2. The Laplacian has index zero, hence so does L. Since the kernel has dimension one, the cokernel also has dimension one.
3. A nonzero smooth adjoint density rho has nonzero total mass: if its mass vanished, Fredholm would place the constant function 1 in the range of L, contradicting the maximum principle. Normalize the mass to one.
4. If rho were negative somewhere, choose a nonnegative smooth g supported there with integral g rho<0. Then f=g-integral g rho is strictly positive and has integral f rho=0, again contradicting the maximum principle and Fredholm. Hence rho>=0.
5. In a positive reference volume the adjoint has real uniformly elliptic principal part and smooth lower terms. Subtracting the positive part of its zeroth coefficient makes rho a nonnegative supersolution with nonpositive zeroth coefficient; the strong minimum principle gives rho>0.
6. Consequently dmu=rho dV is a smooth positive probability, and Lw=f is solvable exactly when integral f dmu=0. The same range statement holds in the Holder spaces by elliptic regularity.

### 13. thm:stw-volume closure: scalar sign and implicit function theorem

Status: checked.

1. Use the map (t,u,b)->logdet Q_u-(n-1)(Ft+b) from the open positive subset of [mean-zero C2,theta] times R to C0,theta. Smoothness follows from affine dependence of Q on derivatives and smoothness of logdet on positive matrices.
2. Its derivative in (u,b) is Lw-(n-1)c. To solve it equal to f, integrate against mu: -(n-1)c=integral f dmu, so c=-(n-1)^-1 integral f dmu. The sign in the proof is correct.
3. Then f+(n-1)c=f-integral f dmu has zero mu-mean. Fredholm provides w, and subtracting its gamma^n mean makes it uniquely mean zero. The full derivative is injective by the same calculation and the constant-kernel result.
4. This is a bounded bijective linear map between Banach spaces; the bounded inverse theorem, or Schauder estimates on the mean-zero complement, supplies a bounded inverse.
5. Strict positivity is open in C2,theta because X is compact. The Banach implicit function theorem gives local solution parameters, and standard smooth-equation Schauder bootstrap makes the resulting C2,theta solutions smooth for smooth Ft. Thus the set of smooth solution parameters is relatively open in [0,1].

### 14. thm:stw-volume closure: closedness and existence

Status: checked conditionally.

1. For any sequence of solution parameters tj converging to t, apply the accepted potential estimate after subtracting sup uj. It gives uniform oscillation and |bj| bounds.
2. The target estimate from dependency 63 together with the accepted gradient reduction gives uniform gradient and complex Hessian bounds, and the preceding verified regularity implication gives every higher derivative bound.
3. Subtracting the gamma^n mean preserves the equation and all derivatives; for a supremum-normalized function in [-C,0], its mean lies in [-C,0], so the resulting mean-zero potential is uniformly bounded.
4. Compact embeddings and a diagonal Arzela-Ascoli subsequence give convergence of mean-zero uj in every finite smooth order, with a further subsequence bj->b. Passing to the equation yields the prescribed limiting Ft.
5. Uniform Q upper bounds and det Q>=d give Q>=aI before passage to the limit, so Q_limit>=aI. The limiting ansatz remains strictly positive and has a smooth positive root; mere nonnegative determinant continuity is not being substituted for this argument.
6. Thus the solution parameter set is nonempty, relatively open and relatively closed in the connected interval [0,1], and is all of [0,1]. This establishes global existence conditional on the stipulated a priori estimates. No existence statement in the source book is invoked.

### 15. thm:stw-volume closure: uniqueness of the scalar

Status: checked.

1. Here v denotes a second unscaled potential, not the temporary rescaled v in the previous lemma; both solutions use the same ansatz and dd^c convention.
2. At a maximum of u-v, D(u-v)=0 and its real Hessian is nonpositive, so ddc(u-v)<=0. Thus the first-order Z terms agree and Q_u-Q_v=P_n((ddc(u-v))_gamma)<=0.
3. For positive matrices determinant is order preserving: conjugating by Q_v^-1/2 gives eigenvalues at most one, so logdet Q_u<=logdet Q_v. The common F and positive n-1 imply b<=c.
4. At a minimum all these inequalities reverse, giving b>=c. Hence b=c exactly, without assuming any integral normalization or Gauduchon volume conservation.

### 16. thm:stw-volume closure: uniqueness of the potential

Status: checked.

1. For us=(1-s)v+su, affine dependence gives Q_us=(1-s)Q_v+sQ_u>0. Positivity along the entire segment follows directly, even before knowing us solves any equation.
2. For this pair of fixed smooth solutions, compactness of X times [0,1] gives uniform positive lower and finite upper eigenvalue bounds on the segment.
3. The fundamental theorem of calculus gives 0=logdet Q_u-logdet Q_v=(integral_0^1 L_us ds)(u-v), since b=c.
4. Each L_us has a uniformly positive real principal symbol on the compact segment, a smooth drift, and no zeroth-order term. Its average therefore has those same properties.
5. The strong maximum principle on connected compact X makes u-v constant. Equal supremum-zero normalization makes the constant zero. This proves uniqueness in the scalar ansatz, not among all metrics in an Aeppli class.

### 17. Final Aeppli statement and assumption-use audit

Status: checked.

1. The accepted book identity is Gamma_u-gamma0^(n-1)=partial xi_u+barpartial conjugate(xi_u), xi_u=i barpartial u wedge gamma^(n-2)/(4pi), compatible with ddc=i/(2pi)partial barpartial.
2. The difference is partial-barpartial closed, so if gamma0 is Gauduchon, then eta_u is Gauduchon and the (n-1)st powers have the same Aeppli class. The qualification on gamma0 is necessary and present.
3. Connectedness is used for the constant kernel, strict adjoint positivity, and uniqueness. Compactness without boundary is used for extrema, a finite cover, Fredholm, and convergence. n>=2 is used by P_n and the determinant/scalar factors.
4. Fixed smooth geometry supplies coefficient regularity and uniform chart constants; smooth data bounds of every order supply the bootstrap. Gamma>0 is essential for logdet and ellipticity.
5. The Gauduchon condition on the fixed auxiliary gamma is a standing hypothesis of the target problem and accepted estimates; the local regularity and Fredholm closure themselves need only smooth positivity. Its absence from these individual deductions is harmless redundancy, not an unproved inference.
6. The whole supplied text has been checked in its written order. Pending dependency 63 is outside the claim independently audited here by the user's explicit conditional-input instruction.

## Reference resolution

1. The external reference comparison confirms every required hypothesis of the exact standard real variable-coefficient concave estimate. The earlier status checked_pending_reference_confirmation is resolved with no critical error or gap.
2. No bound on the full real Hessian, derivatives of the frozen gradient, smoothness of the concave extension, or similarity to ordinary complex Monge-Ampere is silently assumed. The bound on Phi(0,0), sometimes omitted when summarizing the theorem, follows directly from the compact tangent box and bounded R.

## Reference checks

### 1. lem:stw-higher-regularity: variable-coefficient concave interior regularity

Source: [Tosatti–Wang–Weinkove–Yang, Definition 3.2 and Theorem 3.4, arXiv v2 pp. 15–18 (especially p. 16)](https://arxiv.org/pdf/1402.0554).

The required theorem search returned five nonmatching results. The closest, arXiv:1205.1266 Theorem 3.2, depends on an a priori real C2 norm and derivatives of F, so it cannot justify this step. Web fallback used the same full statement and located the exact general real theorem.

Definition 3.2 requires concavity on all Sym(2n), ellipticity for every positive semidefinite increment, and |Phi(N,x)-Phi(N,y)|/(1+||N||)<=K|x-y|^gamma. Theorem 3.4 gives an interior C2,alpha bound for C2 solutions with Holder right side, depending on ellipticity, Holder data, ||u||infinity and Phi(0,0). Matrix differentiability is not required.

Here m=2n, Phi is the constructed tangent infimum, and h=(n-1)(F+b). The independently checked trace-form ellipticity implies the source's operator-norm convention because ||N||<=tr N<=m||N|| for N>=0. The global spatial modulus and bounded Phi(0,0) were proved above. R is uniformly Holder after the fixed W2p step, so its dependence on the particular solution introduces no uncontrolled constant. This uses the general real theorem only; no geometric existence or specialized nonlinear estimate is imported.

### 2. lem:stw-higher-regularity: scalar W2p, embedding, and Schauder

These standard local elliptic estimates are expressly allowed by the user and are not attributed in the proof to an external paper. The fixed operator has smooth coefficients, the trace right side is bounded, the domains are nested charts, and the potential is uniformly bounded. After C2,beta regularity, differentiation of the original equation gives precisely a linear uniformly elliptic operator with Cbeta coefficients and right side.

### 3. thm:stw-volume closure: internal adjoint reference

Source: [prop:gaud-volume-linearization, lines 15–49](/Users/mingchen/Non-Kahler/book/author/section_gauduchon_volume_adjoint.tex).

The proposition assumes a given positive Gamma_u and does not require existence of solutions for all prescribed densities. Its operator contains the first-order correction in D_gamma. For the current logarithmic determinant, L=(n-1)mathcal L_u, which preserves the adjoint kernel and its normalization.

The proof's Fredholm homotopy and positive-density construction were checked directly. No later statement about the globally defined normalization functional, and no imported STW existence, is used. The mean-zero domain uses gamma^n whereas the range obstruction uses mu; constants connect the two normalizations correctly.

### 4. Source ansatz, normalizations, and Aeppli identity

Sources:

- [conventions.tex](/Users/mingchen/Non-Kahler/book/author/conventions.tex)
- [chapter_smooth_equations.tex](/Users/mingchen/Non-Kahler/book/author/chapter_smooth_equations.tex)
- [section_stw_gradient.tex](/Users/mingchen/Non-Kahler/book/author/section_stw_gradient.tex)
- [section_stw_structure.tex](/Users/mingchen/Non-Kahler/book/author/section_stw_structure.tex)

The supplied proof, current book definitions, and accepted stw_czero_01/stw_gradient_reduction_01 audits agree on v=u/(2pi), normalized Hodge star 1/(n-1)!, P_n, the rescaled Z, and determinant exponent n-1. The Aeppli identity preceding the estimates uses xi=i barpartial u wedge gamma^(n-2)/(4pi).

The theorem label in the source is used only to identify the target equation and fixed forms. Its external existence statement is excluded. Detailed torsion exclusions and the special Hessian estimate are not independently audited in this run.

## Findings and repair hints

- Critical errors: none.
- Gaps: none.
- Repair hints: none required for this conditional closure argument.

## Persisted audit artifacts

- [Statement checks](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/stw_continuity_reconstruction_01/statement_checks.jsonl)
- [Reference checks](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/stw_continuity_reconstruction_01/reference_checks.jsonl)
- [Events](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/stw_continuity_reconstruction_01/events.jsonl)
- [Final JSON](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/stw_continuity_reconstruction_01/verification.json)

The book was read as evidence and was not edited. This is a mathematical verification; no numerical experiment or implementation-mirroring test was used as a substitute for a proof check.

