# Verification report: local_big_continuity_01

**Verdict: correct under the accepted manuscript inputs.** The complete submitted proof was checked in textual order. The audit found **zero critical errors and zero gaps**. It covers 16 ordered items with 91 individual checks, followed by four reference records. The manuscript was not edited.

This verdict uses the expressly accepted one-sided stability71, including its constant independent of a possibly unbounded comparison potential, and smoothing73 for the fixed positive normalized formal-exph averaging operator. It also uses the supplied genuine strict barrier and the permitted standard Kiselman principle. It does not independently certify these accepted manuscript inputs.

The conclusion proved is continuity on each open set where the fixed barrier is locally bounded. The error function remains unspecified apart from its limit at zero.

## Exact classical-input comparison

The principal evidence is the supplied [Demailly94 primary PDF](/Users/mingchen/Non-Kahler/research/sources/Demailly94-flow.pdf) and [text](/Users/mingchen/Non-Kahler/research/sources/Demailly94-flow.txt), cross-checked through arxiv-first theorem queries and then web search against the [author-hosted paper](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization_flow.pdf). The exact displayed formulas were also inspected visually on printed pages 12 and 16.

| Source object | Specialization in the submitted proof | Hypothesis check |
| --- | --- | --- |
| Closed real current \(T\) | \(dd^c u\) | Closed by the differential identity, independently of whether \(\theta\) is closed. |
| Smooth closed reference form \(\alpha_D\) | \(0\) | Closed and smooth. |
| Quasi-psh potential \(\psi\) | The bounded solution \(u\) | \(dd^c u\geq-\theta\) with smooth \(\theta\) gives the required local quasi-psh property. |
| Continuous real lower bound \(\gamma\) | \(-\theta\) | The source does not require \(\gamma\) to be closed. |
| Auxiliary smooth semipositive curvature form, called \(u\) in the source | \(A\omega\) | A sufficiently large fixed \(A\geq0\) works by compactness. This form is distinct from the solution \(u\). |
| \(\Psi(z,w)\) of equations (3.1)–(3.2) | \(R_{|w|}u(z)\) | The same fixed positive normalized radial formal-exph averaging is used. Smoothness holds for \(w\ne0\). |
| Source error \(\delta(t)\) | \(\epsilon_0(t)\), then an increasing majorant \(\epsilon(t)\) | Only convergence to zero is used. |

Theorem 4.1 is on printed page 12; its proof establishes the monotonicity and logarithmic convexity on pages 15–16. The formal-exph and averaging definitions are on pages 5–6. The theorem requires a **smooth** auxiliary curvature form; \(A\omega\) satisfies that requirement.

Remark 4.7 on printed page 16 uses
\[
\widetilde\Psi_D=\Psi+|w|,
\qquad
\widetilde\lambda_D=\lambda+t-2K_0t^2.
\]
The submitted proof explicitly uses a different correction and checks it:
\[
H=R_tu+Kt^2+Kt,
\qquad
\widetilde\lambda_H
=\lambda+2(K-K_0)t^2+Kt.
\]
The two derivatives are not identified. The proof's positive vertical contribution and Young inequality establish its variant of the absorption. Adding an \(O(t)\) term to an unspecified source error does not make the entire error \(O(t)\).

For the allowed minimum principle, arxiv theorem search returned a restricted smooth subequation statement requiring interior attainment; that result was not used. Web checking found the full tube and Reinhardt formulations in [Deng–Wang–Zhang–Zhou, Theorems 1.1–1.2](https://arxiv.org/pdf/1810.12733). These require a pseudoconvex total domain, connected fibers, and the appropriate invariance, but no attained interior infimum. The coordinate-ball times strip localization satisfies these hypotheses.

## Sequential deduction audit

Each item below follows the proof's order. The derivations explain why the submitted text passes; they do not replace its argument with a different proof.

### 1. Opening setup and standing assumptions

1. The proof text is usable and is read in its displayed order.
2. The strict genuine barrier is an accepted input, not inferred merely from an ambiguous definition of bigness.
3. ddc u is closed even if theta is nonclosed; theta-psh bounded u gives ddc u>=-theta.
4. Compactness allows uniform Hermitian curvature constants and normalization of the upper bounds of u and rho.
5. U is arbitrary subject to local boundedness of rho; no analytic or canonical description of U is required.

**Finding:** checked; no critical error or gap.

### 2. The general curvature modulus — classical input

1. Use Demailly's notation psi=u, alpha_D=0, T=ddc u, gamma=-theta; gamma is only required to have continuous real coefficients, whereas closedness is required of T and alpha_D.
2. Because theta is smooth, ddc u>=-theta makes u locally the sum of a psh function and a smooth function, as required by the source.
3. Take the source's auxiliary curvature form B=A omega with A>=0 large: compactness bounds the negative Chern bisectional curvature, so in particular the required bound on orthogonal pairs holds.
4. The source's equations (3.1)-(3.2) use the same positive normalized radial formal-exph averaging. They are smooth in (z,w) for w nonzero; no continuity of u is required.
5. Theorem 4.1 provides the full Hessian estimate, not merely a base Hessian estimate. Numerical ddc normalization factors are absorbed in fixed constants.
6. The source states lambda=t partial_t(R_t u+K0 t^2) is nonnegative and increasing; its proof gives logarithmic convexity. Monotone convergence to the genuine quasi-psh representative yields R_t u+K0 t^2>=u pointwise.
7. The source's error function tends to zero; no linear or power rate is assumed. Exact reference confirmation is recorded separately.

**Finding:** checked; no critical error or gap.

### 3. Lemma general-kiselman-modulus — H and logarithmic convexity

1. Set H=R_t u+K t^2+K t for K>=K0 with K>0, as allowed by 'sufficiently large'.
2. Its logarithmic derivative is tilde-lambda=lambda+2(K-K0)t^2+Kt>=lambda.
3. Its second logarithmic derivative is partial_logt lambda+4(K-K0)t^2+Kt>0. Hence H is strictly logarithmically convex and increasing. This uses the actual source assertion about lambda, not an inference from monotonicity alone.

**Finding:** checked; no critical error or gap.

### 4. Lemma general-kiselman-modulus — mixed and vertical error absorption

1. For w nonzero, partial_w partial_barw |w|=1/(4|w|); the dd^c factor only changes fixed constants.
2. The term K|w| therefore supplies a positive vertical coefficient comparable to K/t. K|w|^2 supplies another nonnegative vertical coefficient.
3. Young's inequality bounds C|zeta||eta| by C't|zeta|^2+K|eta|^2/(8t), where C' is fixed once K is fixed.
4. For all sufficiently small t, the remaining positive vertical coefficient absorbs the fixed C|eta|^2 error as well.
5. The remaining negative base form is -theta-(A lambda+epsilon0(t)+C't)omega.
6. Since A>=0 and tilde-lambda>=lambda, replacing lambda by tilde-lambda weakens this lower bound in the valid direction.
7. An increasing nonnegative majorant epsilon(t) of epsilon0(t)+C't tends to zero and is independent of c and delta. This is the absorption mechanism of Remark 4.7, with the explicitly justified larger correction used in this proof.

**Finding:** checked; no critical error or gap.

### 5. Lemma general-kiselman-modulus — boundedness and minimizing radii

1. Positivity and normalization of R_t give inf_X u<=R_t u<=sup_X u, uniformly in z and t.
2. For fixed c>0 and delta>0, the expression tends uniformly to +infinity as t decreases to zero. Thus all minimizers lie in one compact interval [b,delta] with b>0.
3. The objective is smooth for t>0, continuous in (z,t), and strictly convex in log t after subtracting the linear logarithmic term. It therefore has exactly one minimizing radius.
4. The interior stationarity condition is tilde-lambda=c. At t=delta the left derivative of the convex objective is <=0, so tilde-lambda<=c; the boundary sign is correct.
5. The minimum value is finite and continuous in z by minimization over the fixed compact interval. The unique minimizer is continuous by the same compactness argument, without assuming continuity of u.
6. The estimate R_t u+Kt^2>=u gives Phi>=u-K(delta^2+delta), since Kt>=0 and -c log(t/delta)>=0. Evaluation at t=delta gives Phi<=R_delta u. In particular Phi is bounded.

**Finding:** checked; no critical error or gap.

### 6. Lemma general-kiselman-modulus — localization and capped minimum

1. Fix z0 and a>0. If t*(z0)<delta, choose an upper radius r+ with t*(z0)<r+<delta and tilde-lambda(z0,r+)<c+a, using continuity and tilde-lambda(z0,t*)=c.
2. After shrinking to a coordinate ball V around z0, continuity of t* keeps every nearby minimizer below r+, and continuity of tilde-lambda preserves its bound at r+.
3. If t*(z0)=delta, keep r+=delta. The inequality tilde-lambda(z0,delta)<=c and continuity ensure tilde-lambda(z,delta)<c+a on a smaller V.
4. In either case choose a fixed lower radius r_- > 0 below all nearby minimizers. Monotonicity of tilde-lambda bounds it by c+a on the whole radial interval (r-,r+).
5. When a minimizing radius equals the cap, continuity at t=delta shows that the infimum over t<delta equals the closed-cap minimum. Kiselman's principle does not require attainment in the open interval.
6. The logarithmic substitution w=exp(tau) gives the product V times the strip log r-<Re tau<log r+, which is pseudoconvex after taking V to be a ball and has connected convex real fibers.
7. Radial invariance gives independence of Im tau. The penalty -c Re tau is pluriharmonic on the strip and does not alter the Hessian inequality.

**Finding:** checked; no critical error or gap.

### 7. Lemma general-kiselman-modulus — smooth-form freezing and current bound

1. On the localized product the full Hessian of the objective is bounded below by -B(z), where B(z)=theta(z)+(A(c+a)+epsilon(delta))omega(z).
2. No local potential for nonclosed theta is assumed. In a chart, freeze B at z0 and choose a real quadratic q with dd^c q=B(z0)+h beta, where beta is the Euclidean positive form and h>0.
3. Continuity of the coefficients and shrinking V ensure B(z)<=B(z0)+h beta. Hence the corrected objective is genuinely plurisubharmonic on the whole product.
4. The allowed Kiselman principle gives that Phi+q is psh on V; the fiber infimum is finite and continuous, so no representative ambiguity arises.
5. The resulting inequality dd^c Phi>=-B(z0)-h beta implies dd^c Phi>=-B(z)-2h beta on a further shrink. Covering by these neighborhoods, converting beta to a uniform local multiple of omega, and letting h decrease to zero gives the desired continuous-form current inequality for fixed a.
6. Letting a decrease to zero gives theta+dd^c Phi>=-(Ac+epsilon(delta))omega. The local psh correction also proves quasi-plurisubharmonicity.
7. Finally R_t u+Kt^2=(R_t u+K0t^2)+(K-K0)t^2 remains increasing in t and tends pointwise to u.

**Finding:** checked; no critical error or gap.

### 8. Paragraph after general-kiselman-modulus — smoothing estimates

1. The curvature-modulus estimate has not changed the averaging operator.
2. Boundedness of u and R_t u-u>=-Kt^2 are exactly the accepted smoothing73 hypotheses.
3. Therefore the accepted adjoint-cancellation argument gives ||R_t u-u||_L1(dV)<=Ct^2 and ||grad R_t u||_infinity<=C/t.
4. No estimate for epsilon(t) is used to derive these two bounds, and no prior continuity of u is used.

**Finding:** checked; no critical error or gap.

### 9. Theorem local-big-bounded-continuity — normalization and exponents

1. Adding constants leaves ddc u and its Monge–Ampere measure unchanged, so u can be normalized to [-C0,0].
2. A genuine quasi-psh rho has finite supremum on compact X; subtracting a constant gives rho<=-C0-1 without changing strictness.
3. The allowed stability range is nonempty for p>1. For n>=1, (p-1)/(np+p-1)<1/2, so choosing eta in this range gives 0<alpha=2eta<1.
4. Set c=delta^alpha+epsilon(delta)>0; then c tends to zero and epsilon(delta)<=c.
5. With e=Ac+epsilon(delta), s=e/kappa is nonnegative, tends to zero, satisfies s kappa=e, and obeys s<=(A+1)c/kappa.

**Finding:** checked; no critical error or gap.

### 10. Theorem local-big-bounded-continuity — barrier correction and ordering

1. The affine-current identity is theta+dd^c v=[theta+dd^c Phi+s(theta+dd^c rho)]/(1+s).
2. Its numerator is bounded below by (-e+s kappa)omega=0; the identity works for nonclosed theta.
3. Phi is bounded quasi-psh and rho is genuine theta-psh, so the affine combination is a genuine theta-psh function, possibly unbounded below.
4. For delta sufficiently small K(delta^2+delta)<=1. The lemma's lower bound gives Phi>=u-1>=-C0-1>=rho.
5. At the cap Phi<=R_delta u, and positivity of the normalized average gives R_delta u<=0.
6. Since rho<=Phi and s>=0, v<=Phi<=R_delta u<=0. No boundedness below of v is asserted or required.

**Finding:** checked; no critical error or gap.

### 11. Theorem local-big-bounded-continuity — one-sided stability

1. The target u is bounded in the accepted interval, solves MA_theta(u)=f dV with f nonnegative in Lp, and the comparison v is theta-psh and <=0.
2. The accepted stability71 expressly permits this possibly unbounded comparison potential and has a constant independent of it.
3. Pointwise (v-u)_+ <= (R_delta u-u)_+ <= |R_delta u-u|, including points where v=-infinity.
4. Consequently its integral is at most C delta^2 and stability gives sup_X(v-u)_+<=C delta^(2eta)=C delta^alpha, uniformly in delta.

**Finding:** checked; no critical error or gap.

### 12. Theorem local-big-bounded-continuity — local bound for Phi-u

1. At rho>=-M all terms in Phi-u=(1+s)(v-u)+s(u-rho) are finite.
2. The equality follows by multiplying the definition of v by 1+s and subtracting u; its sign is correct.
3. Here v-u<=C delta^alpha, u<=0 implies u-rho<=M, and 1+s is bounded for small delta.
4. Thus Phi-u<=C delta^alpha+C_M s<=C_M c. The constant is uniform on {rho>=-M} for fixed M.

**Finding:** checked; no critical error or gap.

### 13. Theorem local-big-bounded-continuity — lower bound for minimizing radius

1. At the minimizing t, solve the defining identity for -c log(t/delta).
2. Using R_t u+Kt^2>=u and Kt>=0 gives -c log(t/delta)<=Phi-u+K(delta^2+delta).
3. For 0<delta<1 and alpha<1, delta^2+delta<=2 delta^alpha<=2c; hence the right side is <=C_M c.
4. Divide by positive c to obtain log(delta/t)<=C_M and t>=a_M delta with a_M=exp(-C_M)>0, decreased to at most 1 if necessary.
5. The constant a_M is independent of delta and the base point in {rho>=-M}; no power rate for epsilon is needed.

**Finding:** checked; no critical error or gap.

### 14. Theorem local-big-bounded-continuity — uniform convergence

1. Since a_M delta<=t, monotonicity gives R_(a_M delta)u+K(a_M delta)^2<=R_t u+Kt^2.
2. Rearranging the minimum identity gives R_t u+Kt^2=Phi+Kdelta^2+Kdelta-Kt+c log(t/delta)<=Phi+Kdelta^2+Kdelta.
3. Combine with Phi-u<=C_M c and delta<=c to get R_(a_M delta)u-u<=C_M c.
4. The monotone lower estimate gives R_(a_M delta)u-u>=-K(a_M delta)^2, also controlled by c.
5. Together these prove the displayed uniform absolute error bound C_M(delta^alpha+epsilon(delta)) on {rho>=-M}, tending to zero.
6. Every compact subset of U has a uniform lower bound for rho by a finite cover from its local boundedness.
7. Choose that fixed M and a_M. A sequence delta_j decreasing to zero gives smooth functions R_(a_M delta_j)u converging uniformly to u on the compact subset.
8. Applying this to compact neighborhoods contained in U proves continuity at every point of U. No continuity across the complement of U is inferred.

**Finding:** checked; no critical error or gap.

### 15. Closing paragraph — continuity modulus and scope

1. For a compact K subset U, the uniform error bound and global gradient bound give |u(x)-u(y)|<=2C_M(delta^alpha+epsilon(delta))+C d_omega(x,y)/(a_M delta) for x,y in K.
2. Taking delta comparable to the square root of d_omega(x,y), for instance, makes both terms tend to zero and yields a modulus with no assumed power bound on epsilon.
3. The proof does not claim a Holder exponent from an unspecified epsilon. Its statement that a Holder conclusion by this argument needs a proved power control is appropriately limited to this argument.
4. Boundedness of u was used in the smoothing input, uniform exclusion of t=0, normalization, and accepted stability; the argument does not establish regularity for unbounded solutions.
5. The barrier lower bound was used only on fixed superlevel sets {rho>=-M}; the proof does not establish continuity at its poles.

**Finding:** checked; no critical error or gap.

### 16. Full-proof hypothesis-use audit

1. Compactness supplies uniform regularization constants, finite suprema for normalization, and the global setting of the accepted stability input.
2. Hermitian omega is only a regularization metric and a comparison form for strictness.
3. Theta smoothness supplies a continuous lower bound for Demailly and permits freezing; closedness of theta is never needed.
4. Theta semipositivity and the stated big setting are inherited in the accepted manuscript inputs. Once the genuine strict rho is explicitly assumed, no further numerical use of bigness is needed; this redundancy is harmless, not an omitted existence argument.
5. The strict positive kappa is used exactly in s kappa=e. Local boundedness of rho is used exactly for compact-set uniform convergence.
6. The Lp hypothesis, p>1, and equation for u enter the accepted one-sided stability estimate and the admissible eta. The smoothing argument uses the accepted positive smooth measure dV.
7. Connectedness is part of the accepted compact setting and is not separately needed in the elementary local argument; no contradiction follows from this harmless redundancy.
8. No BMP/PVP assumption, KN19 substitution, uniform convergence deduced from Dini before continuity, unproved power modulus, or prior continuity of u has been introduced.

**Finding:** checked; no critical error or gap.

## Bounds and dependencies retained in the conclusion

For a fixed barrier bound \(M\), the proof gives a fixed \(a_M>0\) and
\[
\sup_{\{\rho\geq-M\}}|R_{a_M\delta}u-u|
\leq C_M\bigl(\delta^\alpha+\epsilon(\delta)\bigr)\longrightarrow0.
\]
The choice \(c=\delta^\alpha+\epsilon(\delta)\) controls both the curvature error and the linear radial penalty: \(s=O(c)\) and \(\delta\leq\delta^\alpha\leq c\) for small \(\delta\). This is why the radius lower bound is uniform without any rate for \(\epsilon\).

As a direct expansion of the proof's final sentence, for \(x,y\) in a fixed compact subset of \(U\),
\[
|u(x)-u(y)|
\leq 2C_M\bigl(\delta^\alpha+\epsilon(\delta)\bigr)
+\frac{C\,d_\omega(x,y)}{a_M\delta}.
\]
Choosing \(\delta=\sqrt{d_\omega(x,y)}\) for sufficiently close points gives a modulus tending to zero. This does not assert a power bound for the term containing \(\epsilon\), or a Hölder exponent.

## Findings and persistence

Critical errors: none.

Gaps: none.

Repair hints: empty, as required for a correct verdict.

The audit records are saved in the run's statement_checks and reference_checks memory channels. Their sequence fields preserve proof order. One statement record was persisted on a successful retry after a permission-review timeout; no mathematical check was omitted. The first Theorem 4.1 search likewise succeeded on its single retry. Primary-PDF web fetch failures were resolved for evidentiary purposes by the supplied local PDF, exact text, rendered page inspection, and matching indexed author-hosted web evidence.

The supplied PDF has SHA-256:
`c2f6c33a5e02518a76991a2fe86558ace8b8bf874d3e24348e27ba447884cded`.

Files for this run:

- [Final verification JSON](verification.json)
- [Detailed structured audit and reference evidence](audit_details.json)
- [Theorem 4.1 page image](source_evidence/Demailly94-page-12.png)
- [Remark 4.7 page image](source_evidence/Demailly94-page-16.png)

No BMP/PVP assumption, KN19 replacement theorem, continuity across the barrier's poles, or regularity result for unbounded solutions was added.

