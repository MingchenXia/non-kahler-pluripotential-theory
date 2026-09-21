# Verification report: Gauduchon trace coordinates

**Run:** `gauduchon_trace_topology_01`  
**Verdict:** **correct**  
**Critical errors:** 0  
**Gaps:** 0

The full submitted proof passes under the explicitly accepted inputs. The audit checks 14 items, containing 62 small deductions, in the order of the proof, followed by seven groups of reference and definition checks. The theorem applies to every normalized potential in the stated setting, including arbitrary smooth nonclosed backgrounds and potentials with infinite non-pluripolar top-degree mass.

The final curve construction is an existential counterexample in the positive-background setting of the cited curve theorem. It does not claim that a smooth strictly positive target exists for every background, including a zero-mass background. The cited source explicitly constructs its target.

## 1. Scope, definitions, and accepted inputs

The standing assumptions are that \(X\) is a compact connected complex manifold without boundary, \(n\geq1\), \(\theta\) is a smooth real \((1,1)\)-form, \(\gamma\) is a Gauduchon metric, \(\operatorname{PSH}(X,\theta)\neq\varnothing\), and \(dV\) is a smooth strictly positive probability measure.

The book defines a \(\theta\)-psh potential as a canonical quasi-plurisubharmonic function satisfying \(\theta+dd^c u\geq0\) as a current. In particular, its mean is well-defined. No local potential for \(\theta\) is part of this definition. See [the conventions](/Users/mingchen/Non-Kahler/book/author/conventions.tex:3) and [the definition and local correction](/Users/mingchen/Non-Kahler/book/author/chapter_framework.tex:10).

As requested, the audit accepts normalized compactness, conserved Gauduchon trace, the stated elliptic and distributional results, the canonical psh-distribution criterion, elementary measure topology and Arzelà–Ascoli, audited65 curve approximation, and general-background damped capacity continuity. Their applications, hypotheses, and normalization conventions were checked. Their proofs are not reopened as independent research problems.

## 2. The finite trace measure

Write \(T_u=\theta+dd^c u\). Positivity makes \(T_u\wedge\gamma^{n-1}\) a positive measure. The Gauduchon equation is exactly \(dd^c(\gamma^{n-1})=0\), so distributional integration by parts gives

\[
\int_X T_u\wedge\gamma^{n-1}
=\int_X\theta\wedge\gamma^{n-1}
+\langle u,dd^c(\gamma^{n-1})\rangle
=M_{\theta,\gamma}.
\]

This number is finite because the remaining integrand is smooth on compact \(X\), and it is nonnegative because the potential space is nonempty. This uses no closedness of \(\theta\) and no nonlinear mass estimate. When \(n=1\), \(\gamma^0=1\), so the Gauduchon condition is automatic. These uses match [the accepted trace proposition](/Users/mingchen/Non-Kahler/book/author/chapter_gauduchon.tex:61).

## 3. Convexity and mean-normalized compactness

For \(0\leq t\leq1\),

\[
\theta+dd^c(tu+(1-t)v)=tT_u+(1-t)T_v\geq0.
\]

The mean constraint is linear, so the domain is convex. On the accepted compact space \(\mathcal K_\theta=\{v:\sup_Xv=0\}\), define

\[
F(v)=v-\int_Xv\,dV.
\]

Constants preserve the positivity inequality. Since \(dV(X)=1\), \(F(v)\) has zero mean, and

\[
\|F(v)-F(w)\|_{L^1(dV)}\leq2\|v-w\|_{L^1(dV)}.
\]

For any mean-zero \(u\), taking \(v=u-\sup_Xu\) gives \(F(v)=u\). Thus \(F\) is continuous and onto, and its image is compact and nonempty. The accepted compactness statement explicitly permits arbitrary smooth real backgrounds. See [normalized compactness](/Users/mingchen/Non-Kahler/book/author/chapter_compactness.tex:10).

## 4. Continuity and injection

For every smooth test function \(f\),

\[
\int_X f\,d\bigl(\mathcal T_\gamma(u_j)-\mathcal T_\gamma(u)\bigr)
=\langle u_j-u,dd^c(f\gamma^{n-1})\rangle\longrightarrow0
\]

under \(L^1\) convergence. Replacing a continuous test by a smooth uniform approximation incurs an error bounded by \(2M_{\theta,\gamma}\) times its uniform approximation error. Hence distributional convergence upgrades to weak convergence of finite measures.

If two traces agree, their potential difference satisfies \(L_\gamma(u-v)=0\). The operator has positive definite scalar principal symbol. Accepted elliptic regularity makes the difference smooth; the maximum principle on connected compact \(X\) makes it constant. Its zero mean makes the constant zero. Equality of distributions then gives equality of canonical quasi-psh representatives everywhere.

Consequently the continuous map is injective. Compactness of the domain and the Hausdorff weak topology give a homeomorphism onto its compact image. Its displayed affine formula makes this image convex. Both directions of the claimed convergence equivalence follow.

## 5. Zero mass

If \(M_{\theta,\gamma}=0\), every positive trace is zero. Nonemptiness and injectivity therefore give exactly one normalized potential.

The stronger conclusion \(T_u=0\) also follows: a positive current with zero trace against a strictly positive metric is zero. Locally, its nonnegative diagonal coefficient measures have zero sum; positivity forces its off-diagonal coefficients to vanish as well. Taking the elliptic trace of \(dd^c u=-\theta\) gives a smooth right-hand side, so accepted elliptic regularity makes \(u\) smooth. This argument remains valid for an initially arbitrary nonclosed background; existence of this zero-mass case itself forces \(\theta=-dd^c u\).

## 6. Distributional Green inverse

The kernel of \(L_\gamma\) consists of constants. The accepted Fredholm index-zero statement makes the adjoint kernel one-dimensional. Here the formal adjoint is taken relative to \(\gamma^n\), because

\[
\int_X L_\gamma f\,\gamma^n
=n\int_Xdd^c f\wedge\gamma^{n-1}=0.
\]

Thus the adjoint kernel is also the constants. The scalar right-hand side associated with the top-degree measure \(\sigma\) is \(n\sigma/\gamma^n\); its compatibility condition is precisely \(n\int_X\sigma=0\). The accepted distributional Green inverse supplies a solution unique modulo constants.

Pairing the resulting distribution with the smooth probability density \(dV\) fixes its constant. This use of \(dV\) does not replace \(\gamma^n\) in the adjoint calculation. The proof correctly refrains from assuming full-Hessian positivity for arbitrary scalar data.

## 7. Exact admissibility condition

For a positive measure \(\nu\) of mass \(M_{\theta,\gamma}\), the signed datum \(\nu-\theta\wedge\gamma^{n-1}\) has total mass zero. If \(\nu\) is the trace of a normalized potential, uniqueness of the normalized Green solution proves necessity of \(\theta+dd^c w\geq0\).

Conversely, suppose that inequality holds for the Green distribution. On a relatively compact coordinate ball choose \(\rho=A|z|^2\) with \(dd^c\rho\geq\theta\). Then

\[
dd^c(w+\rho)
=(\theta+dd^c w)+(dd^c\rho-\theta)\geq0.
\]

The accepted canonical criterion produces a locally integrable psh representative of \(w+\rho\). Subtracting \(\rho\) gives a quasi-psh representative of \(w\). The local representatives glue because they represent the same distribution and canonical representatives equal almost everywhere coincide. Positivity, zero mean, and the prescribed trace are retained. The correction only dominates \(\theta\); it does not require \(\theta=dd^c\rho\).

For \(n=1\), the scalar equation is the full equation \(\theta+dd^c w=\nu\), so admissibility is automatic. For \(n\geq2\), a positive trace does not force a Hermitian matrix to be positive: \(\operatorname{diag}(-1,2,1,\ldots,1)\) illustrates the distinction. The proposition correctly keeps the full current inequality as an additional condition.

## 8. Bounded-Lipschitz metric

The displayed supremum is finite and bounded by \(2M_{\theta,\gamma}\); symmetry and the triangle inequality hold test by test. Any Lipschitz function can be scaled into the test class. Uniform density of Lipschitz functions in continuous functions therefore proves separation of measures and the implication from metric convergence to weak convergence.

For the converse, Arzelà–Ascoli gives a finite uniform \(\varepsilon\)-net \(f_1,\ldots,f_N\) for the bounded-Lipschitz test family. For measures of mass \(M\),

\[
d_{\rm BL}(\nu_j,\nu)
\leq\max_i\left|\int_X f_i\,d(\nu_j-\nu)\right|+2M\varepsilon.
\]

Weak convergence first sends the finite maximum to zero; then let \(\varepsilon\) tend to zero. This proves the claimed topology.

Pullback by the injective trace map gives a genuine metric on normalized potentials. Its topology is the compact \(L^1\) topology, so it is complete. When \(M=0\), the identically zero distance on the singleton is a valid metric. Changing the Gauduchon metric or the Riemannian distance gives the same compact topology, hence uniform continuity of both identity maps. This proves uniform equivalence without any bi-Lipschitz assertion.

## 9. The curve example exists in the cited setting

The accepted [curve completion theorem](/Users/mingchen/Non-Kahler/book/author/section_ideal_lone_completion.tex:32) assumes a compact connected curve and a smooth positive background of total mass one. Its [explicit construction of the target](/Users/mingchen/Non-Kahler/book/author/section_ideal_lone_completion.tex:62) chooses a nonconstant smooth real \(f\) and sufficiently small \(\varepsilon>0\), then sets

\[
u=\varepsilon f-\sup_X(\varepsilon f),
\qquad \theta+dd^c u>0.
\]

It also supplies finite atomic Green potentials \(q_j\) with supremum zero, \(q_j\to u\) in \(L^1\), and zero non-pluripolar measure. Thus the example's existence is supported by its citation; no strict potential for an arbitrary zero-mass background is being assumed.

For the present mean-normalized space use \(q_j^0=F(q_j)\) and \(u^0=F(u)\). Continuity of \(F\) gives \(q_j^0\to u^0\) in \(L^1\). Constant shifts preserve both trace and non-pluripolar measures. These shifted functions need not remain supremum-normalized ideal envelopes, and that property is not used in the trace argument.

The atomic traces converge weakly to the smooth curvature of \(u\), and the trace metric converges accordingly. The non-pluripolar measures discard the approximants' pole-supported curvature, so they are zero. The smooth limit has the strictly positive measure \(\theta+dd^c u\).

## 10. Failure of capacity convergence

The normalization detail in the last paragraph is valid. For supremum-normalized potentials, zero is a common upper bound. For mean-normalized potentials, the accepted bound on \(\mathcal K_\theta\) gives

\[
\sup_XF(v)=-\int_Xv\,dV=\int_X|v|\,dV\leq C_\theta.
\]

Thus one constant \(C\) makes the entire mean-normalized sequence and its limit nonpositive. A common shift preserves capacity convergence and the curvature measure.

The accepted [damped continuity theorem](/Users/mingchen/Non-Kahler/book/author/chapter_damped_measures.tex:238), in its [general-background form](/Users/mingchen/Non-Kahler/book/author/chapter_damped_measures.tex:376), would imply, if capacity convergence held,

\[
0=e^{p(q_j^0-C)}\operatorname{MA}^{\rm ext}_\theta(q_j^0-C)
\rightharpoonup
e^{p(u^0-C)}(\theta+dd^c u^0),\qquad p>0.
\]

The right side is a nonzero positive measure. Testing with the constant function one gives a contradiction. The accepted continuity statement explicitly permits infinite undamped mass; no raw mass bound is inserted into this application.

The example therefore disproves the implication from trace-metric convergence to capacity convergence in general. It is compatible with the theorem's zero-mass singleton case.

## 11. Singularity classes and assumptions

The coordinates retain canonical potentials after removal of additive constants. In the positive curve setting, distinct smooth normalized potentials have the same ordinary singularity type and trivial multiplier ideals. Injectivity distinguishes their traces, so these coordinates do not in general factor through either equivalence relation. The proof asserts no singularity-quotient metric.

Every substantive standing assumption has a role. Connectedness reduces the elliptic kernel to one constant; compactness supports normalized compactness, the maximum principle, finite coefficient bounds, and the metric arguments; the Gauduchon equation supplies conserved mass and compatibility; smoothness of \(\theta\) supplies local corrections and smooth forcing in the zero-mass case; nonemptiness guarantees an actual domain and nonnegative mass; and the positive probability volume supplies continuous mean normalization. Closedness of \(\theta\) and finiteness of top-degree mass are not assumptions used by the proof.

## 12. Reference audit and persisted output

All references in the submitted proof are internal book results or explicitly accepted standard facts. Their statements, definitions, and downstream applications were checked locally. There is no external-paper theorem in the submitted proof requiring the arXiv-then-web search procedure. Citations within the proofs of accepted inputs were not promoted into new audit obligations.

No critical error or gap was found in the full proof. Accordingly the strict verdict is **correct**, with empty repair hints.

- [Strict JSON result](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/gauduchon_trace_topology_01/verification.json)
- [Sequential deduction records](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/gauduchon_trace_topology_01/statement_checks.jsonl)
- [Reference records](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/gauduchon_trace_topology_01/reference_checks.jsonl)

The book was read without modification. Persistence uses the repository's `memory_init`, `memory_append`, `validate_verification_output`, and `write_verification_output` implementations. The initial MCP memory request timed out during automatic approval review; the same local persistence functions completed successfully.
