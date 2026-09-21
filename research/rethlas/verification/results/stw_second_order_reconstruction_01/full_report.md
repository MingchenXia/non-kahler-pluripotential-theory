# Verification report: STW special second-order reconstruction

Run: `stw_second_order_reconstruction_01`

## Verdict and scope

**Correct, conditional on the precise precursor inputs stipulated in the request.** There are no critical errors or mathematical gaps in the supplied core proof under those inputs. The missing backslash in `sum_kf_k` in the torsion-remainder display is a harmless typographical error.

This verdict depends on `stw_matrix_structure_01` for the six-term torsion formula, all stated missing-gradient and covariant-derivative identities, spectral weights and their comparisons, coercivity, the positive lower bound for the total weight, and the logdet concavity square. It does not certify those precursor assertions independently. In particular, the twice differentiated missing-gradient identities are substantive conditional inputs.

The core proof was checked in textual order. Thirteen statement-check records, with the individual deductions listed within each record, and a source-comparison record are preserved in the run's Rethlas memory. No prior second-order estimate was used, and no book file was edited.

## 1. Hypotheses, normalization, and spectral bounds

The assumptions are: a compact complex manifold without boundary, dimension \(n\geq2\), fixed smooth positive Hermitian forms \(\gamma,\gamma_0\), a smooth real solution \(v\), positivity of \(Q\), and bounded \(C^0(v)\) and \(C^2(h)\) norms. Compactness and background positivity give \(Q_0\geq\tau\gamma\) for a fixed \(\tau>0\); the equation gives the determinant bound \(D=\exp(\sup h)\) needed by the conditional coercivity lemma.

Subtracting \(\sup v\) preserves the equation. One can take \(M\) to be the oscillation of the original function, bounded by twice its original \(C^0\) bound. The formulas

\[
\phi'=\frac1{4K-2s},\qquad \phi''=\frac2{(4K-2s)^2},\qquad
\psi'=-D_1D_2e^{-D_2t},\qquad \psi''=D_1D_2^2e^{-D_2t}
\]

verify all stated signs and scalar bounds. The domain of \(\phi\) contains the full gradient range because \(|\partial v|^2\leq K-1\).

The map \(P\) preserves trace. Thus \(\operatorname{tr}g=\operatorname{tr}Q>0\), and the continuous largest eigenvalue is positive everywhere. The test function is continuous and has a maximum. Ordering gives

\[
\lambda_n>-(n-1)\lambda_1,\qquad |\lambda_i|\leq(n-1)\lambda_1.
\]

Since \(|\chi+W|\leq C\sqrt K\), the assumption \(\lambda\geq K\geq1\) implies \(|v_{i\bar j}|\leq C\lambda\). **This is a mixed-Hessian bound only.** No part of this argument bounds the pure derivatives \(v_{ij}\).

## 2. The perturbation and the eigenvalue calculation

A smooth unitary frame can be chosen with zero Chern connection at the point and uniformly bounded second jets. A constant unitary change aligns it with the eigenbasis of \(g\). Define \(B\) as \(\epsilon_0\) times the orthogonal projection onto the complement of the first frame vector.

This constructs, rather than assumes, a self-adjoint nonnegative \(B\), with \(\nabla B=0\) at the point and bounded second derivatives. At that point the spectrum of \(g-B\) is

\[
\lambda,\quad\lambda_2-\epsilon_0,\ldots,\lambda_n-\epsilon_0.
\]

The top eigenvalue is simple and remains simple locally. Rayleigh monotonicity gives \(\widetilde\lambda\leq\lambda_1(g)\), with equality at the point. Therefore \(\widetilde H\) has a local maximum there. No simplicity of the lower eigenvalues is required.

The simple-eigenvalue formula gives the two squared derivatives appearing in the proof. In a unitary parallel gauge, the diagonal component of the commutator of a differentiated connection matrix with a diagonal endomorphism vanishes. Thus the initial formula with \(\nabla_{\bar k}\nabla_k g_{1\bar1}\) has only the stated bounded perturbation error. There is no missing large error at this stage.

Every gap is positive and at most \(n\lambda+\epsilon_0\leq2n\lambda\). Conversion of the first derivatives inside the squares costs \(O(\lambda)\). Conversion of the second derivative introduces

\[
-2\operatorname{Re}\sum_p\overline{\Gamma^p_{k1}}g_{1\bar p,k}+O(\lambda).
\]

The \(p=1\) term is retained as \(C|g_{1\bar1,k}|\); the other terms are absorbed into the positive squares. Starting from \(1/(2n\lambda)\), one may retain \(1/(4n\lambda)\) after converting squares and \(1/(8n\lambda)\) after this absorption. This verifies the eigenvalue-basic inequality with the advertised constant.

## 3. Differentiation of the test function

The first derivative is exactly

\[
\frac{a_k}{\lambda}=-\phi'V_k-\psi'v_k.
\]

Differentiating \(\gamma^{p\bar q}v_pv_{\bar q}\) gives the stated bound for \(V_k\). Its second derivative has the exact positive contribution

\[
\sum_p(|v_{pk}|^2+|v_{p\bar k}|^2)
\]

and the displayed third derivatives. Metric first derivatives cost \(C\sqrt K\) times the linear Hessian terms; metric second derivatives cost \(CK\). After multiplication by \(\phi'\), Young's inequality can spend \(1/(20K)\) of the Hessian squares. Since \(\phi'\geq1/(4K)\), the remaining coefficient is \(1/(5K)\), and the remaining error is a background constant. Pure Hessians are retained in these squares.

## 4. First differentiated equation: explicit weight routing

Metric compatibility gives

\[
\sum_k f_k\nabla_p g_{k\bar k}=h_p,
\qquad
\sum_k f_k\nabla_p W_{k\bar k}=\sum_i t_i\nabla_p Z_{i\bar i}.
\]

These are contractions with weights evaluated at the point, not derivatives of weighted sums. The same observation applies to the second-derivative contraction.

For every \(i>1\) and every column \(k\),

\[
t_i\leq(n-1)f_1\leq(n-1)f_k.
\]

In the \(t_1\) term, each gradient index \(q\) is greater than one. Consequently

\[
t_1\leq\mathcal F\leq n(n-1)f_q\quad(q>1).
\]

For a fixed differentiation index \(p\), the pure term \(t_1|v_{qp}|\) moves to column \(q\) by \(v_{qp}=v_{pq}\). A mixed term is already in that column or can be put there by Hermitian conjugation. Covariant-to-partial conversion of a gradient derivative costs only \(C\sqrt K\).

The connection term from differentiating the diagonal \(g\) is bounded by \(C\sum_kf_k|\lambda_k|\). Here it is essential to use

\[
\sum_k f_k|\lambda_k|\leq\sum_k f_k|v_{k\bar k}|+C\sqrt K\mathcal F,
\]

rather than replace it prematurely by \(C\lambda\mathcal F\). It is then part of \(S+C\sqrt K\mathcal F\). Bounded \(h_p\) is absorbed using the stipulated lower bound on \(\mathcal F\). Conjugating proves the antiholomorphic version. This checks the weighted-third-bound for every \(p\).

## 5. Twice differentiated equation and the conjugated connection

For each \(k\), Chern tensor calculus gives

\[
\begin{aligned}
\nabla_{\bar1}\nabla_1g_{k\bar k}
={}&g_{k\bar k,1\bar1}
-\sum_q\Gamma^q_{1k}g_{q\bar k,\bar1}
-\sum_q\overline{\Gamma^q_{1k}}g_{k\bar q,1}+O(\lambda)\\
={}&g_{k\bar k,1\bar1}
-2\operatorname{Re}\sum_q\overline{\Gamma^q_{1k}}g_{k\bar q,1}+O(\lambda).
\end{aligned}
\]

The conjugation is necessary. It is present in the supplied proof. The chain rule and metric compatibility give

\[
\sum_k f_k\nabla_{\bar1}\nabla_1g_{k\bar k}=h_{1\bar1}+\mathcal C.
\]

Commuting scalar partial derivatives first exchanges the two diagonal Hessian derivatives. Next, for every \(k,q\),

\[
g_{k\bar q,1}=g_{1\bar q,k}+W_{k\bar q,1}-W_{1\bar q,k}+O(1).
\]

The terms \(g_{1\bar q,k}\), \(q>1\), have precisely the weight \(f_k\) of the available eigenvalue squares. Their absorption costs \(C\lambda\mathcal F\). The \(q=1\) terms leave \(C\sum_kf_k|g_{1\bar1,k}|\).

The term \(W_{1\bar q,k}\) has pure derivatives \(v_{pk}\), hence the correct column weight \(f_k\). Mixed derivatives cost \(C\lambda\mathcal F\). One must not estimate \(W_{k\bar q,1}\) in the same way. Instead the exact identity

\[
2\operatorname{Re}\sum_q\overline{\Gamma^q_{1k}}W_{k\bar q,1}
=W_{k\bar k,1\bar1}-\nabla_{\bar1}\nabla_1W_{k\bar k}+O(\sqrt K)
\]

cancels the partial \(-W_{k\bar k,1\bar1}\) term. This is the cancellation used in the proof, and it is valid before any pure-Hessian bound is attempted.

## 6. The two torsion remainders

In the negative remainder \(\sum_it_i\nabla_{\bar1}\nabla_1Z_{i\bar i}\), the conditional exclusions restrict the \(t_1\)-weighted third derivatives to \(v_{q1\bar1}\) and their conjugates, with \(q>1\). Then

\[
v_{q1\bar1}=v_{1\bar1,q}
=g_{1\bar1,q}-\chi_{1\bar1,q}-W_{1\bar1,q}.
\]

The weight \(t_1\) is controlled by \(Cf_q\). The pure derivatives in \(W_{1\bar1,q}\) have column \(q\). Terms with \(i>1\) carry \(t_i\leq Cf_1\), which can be assigned to any derivative column. In particular a remaining pure \(v_{11}\) has only the weight \(Cf_1\).

The relevant gradient formulas, with the \(r\) sums explicit, are

\[
\begin{aligned}
\nabla_{\bar1}\nabla_1v_q
&=v_{q1\bar1}-\sum_r\Gamma^r_{1q}v_{r\bar1}
-\sum_r(\partial_{\bar1}\Gamma^r_{1q})v_r,\\
\nabla_{\bar1}\nabla_1v_{\bar q}
&=v_{1\bar q\bar1}-\sum_r\overline{\Gamma^r_{1q}}v_{1\bar r}.
\end{aligned}
\]

Their additional second derivatives are mixed. The differentiated coefficient terms use the stipulated coefficient exclusions; pure \(v_{q1}\), \(q>1\), can be moved to column \(q\). This proves the claimed negative-remainder bound without a large weight on \(v_{11}\).

For the positive remainder, expand the fixed coefficients of \(W_{1\bar1}\) before differentiating. Its leading terms are exactly the weighted third derivatives from Section 4. First coefficient derivatives multiply Hessians in column \(k\); second coefficient derivatives multiply gradients. Bounding only the mixed Hessians by \(C\lambda\) gives the asserted estimate.

In the gradient portion of the test function, commute the third derivatives to \(v_{k\bar k p}\) and \(v_{k\bar k\bar p}\), then use \(\phi'|\partial v|\leq C/\sqrt K\). All linear Hessian errors are bounded by \(CS/\sqrt K\), since \(\lambda\geq K\). Weighted Cauchy-Schwarz gives

\[
S^2\leq 2n\mathcal F E.
\]

Young's inequality can therefore spend a total of \(E/(30K)\), leaving \(1/5-1/30=1/6\). This establishes the key maximum inequality with constants independent of \(D_1,D_2,K\).

## 7. Case 1: splitting and concavity

If \(\lambda_n\geq-\delta\lambda\), the set \(I=\{k:f_k>f_1/\delta\}\) excludes 1. For its complement,

\[
\sum_{k\notin I}f_k|v_k|^2\leq\delta^{-1}f_1K.
\]

Thus there is no missing factor of \(n\) in the displayed coefficient 2. Applying \(|A+B|^2\leq2|A|^2+2|B|^2\) also proves the coefficient \(4\delta\) in the second split inequality.

For \(k\in I\), \(f_k>f_1\) implies \(\lambda_k<\lambda\), so the concavity denominator is nonzero. The inequalities

\[
\lambda-\lambda_k\leq(1+\delta)\lambda,\quad
f_k-f_1>(1-\delta)f_k,\quad
\frac{1-\delta}{1+\delta}\geq1-2\delta
\]

give exactly the required comparison. Combining the squares produces \(1-2\delta\) times the derivative difference. This factor is between zero and one, so using the full error allowance of the cancellation lemma is legitimate. The unused \(\phi''\) term is nonnegative.

## 8. The derivative-cancellation lemma

For \(k>1\), let \(e_k=\nabla_1g_{k\bar1}-a_k\). Commuting partial derivatives gives

\[
e_k=W_{k\bar1,1}-W_{1\bar1,k}+O(\lambda).
\]

The missing \(v_1\) coefficient of \(Z_{k\bar1}\) prevents a pure \(v_{11}\) in \(W_{k\bar1,1}\). Differentiating the off-diagonal metric factor contributes only \(O(\sqrt K)\). The pure terms of \(W_{1\bar1,k}\) contain the index \(k>1\). Consequently

\[
|e_k|\leq C(\lambda+U),\qquad U=\sum_{p>1,q}|v_{pq}|.
\]

The scalar identity

\[
|a+e|^2-|a|^2=2\operatorname{Re}(a\bar e)+|e|^2\geq-2|a||e|
\]

is valid and removes the need for a separate negative \(|e|^2\) term. For \(k>1\), the first-maximum identity gives

\[
\frac{|a_k|}{\lambda}\leq C\left(\frac{U+H_k}{\sqrt K}+1\right)+|\psi'||v_k|,
\qquad H_k=\sum_p|v_{p\bar k}|.
\]

Multiplication by \(C(1+U/\lambda)\), using \(H_k\leq C\lambda\) and \(\lambda\geq K\), gives all six terms in the supplied proof.

The quadratic weight comparison is explicit:

\[
\begin{aligned}
\mathcal F U^2
&\leq n(n-1)\mathcal F\sum_{p>1,q}|v_{pq}|^2\\
&\leq n^2(n-1)^2\sum_{p>1,q}f_p|v_{qp}|^2
\leq n^2(n-1)^2E.
\end{aligned}
\]

The omitted \(v_{11}\) is exactly the entry for which this argument would fail.

The two linear Hessian terms each cost an arbitrarily small fixed fraction of \(E/K\) plus \(C\mathcal F\). The other two Hessian costs are

\[
\frac{CE}{\lambda\sqrt K},\qquad\frac{C|\psi'|E}{\lambda}.
\]

Their ratios to \(E/K\) are bounded by \(C/(\lambda/K)\) and \(C\sup|\psi'|/(\lambda/K)\), respectively. They are small after imposing a fixed lower threshold for \(\lambda/K\). The remaining scalar inequalities can be taken as

\[
|v_k|\leq\varepsilon+\frac{|v_k|^2}{4\varepsilon},\qquad
|v_k|U\leq|v_k|^2+U^2.
\]

For example, allocating \(1/48\) of \(E/K\) to each of the four Hessian costs proves the total \(E/(12K)\) allowance. No choice here depends on \(K\).

## 9. Case 1 closure and constants

The remaining linear \(g\)-derivative error is bounded using \(g_{1\bar1,k}=a_k+O(\lambda)\), the first-maximum identity and Young's inequality with budget \(E/(60K)\).

The zeroth-order torsion contraction is also correctly weighted: in \(t_1Z_{1\bar1}\) every gradient index is \(p>1\), so \(t_1|v_p|\leq Cf_p|v_p|\); all other \(t_i\) are bounded by \(Cf_1\leq Cf_p\). Hence its bound by \(C\sum_pf_p|v_p|\) is valid.

The sign in the closure is correct because

\[
\psi'\sum_k f_kv_{k\bar k}
=|\psi'|\sum_kf_k(\chi_{k\bar k}-\lambda_k)
+|\psi'|\sum_kf_kW_{k\bar k}.
\]

The positive-square remainder is \(E/(15K)\), which may be reduced to \(E/(20K)\). Since

\[
|v_{1\bar1}|^2\geq\frac{\lambda^2}{2}-CK,
\]

this gives \(f_1\lambda^2/(40K)-C\mathcal F\), as claimed.

The constants have a noncircular choice. First take \(\varepsilon C_0<\tau/4\). Then take \(D_2>2C_\varepsilon\), since \(\psi''/|\psi'|=D_2\). Next take \(D_1D_2\tau/4>C_0\), using \(\min|\psi'|=D_1D_2\). Finally, a sufficient choice is

\[
0<\delta<\min\left\{\frac12,\frac{e^{-D_2M}}{8D_1}\right\}.
\]

It implies \(4\delta(\psi')^2\leq\psi''/2\) throughout the interval. All thresholds for \(\lambda/K\) can now be fixed. Coercivity gives the final bound

\[
\lambda^2\leq80\delta^{-1}\sup_{[-M,0]}|\psi'|^2K^2.
\]

## 10. Case 2 and global propagation

If \(\lambda_n<-\delta\lambda\), then

\[
\frac E{6K}\geq\frac{f_n}{6K}|v_{n\bar n}|^2
\geq\frac{\delta^2\lambda^2}{12nK}\mathcal F-C\mathcal F.
\]

After \(\psi\) is fixed, the linear \(\psi'\)-term costs \(C\lambda\mathcal F\). The remaining \(g\)-derivative error costs at most half of the negative square plus \(C\mathcal F\), leaving coefficient \(-3/2\).

The scalar inequality used to cancel this term is exact:

\[
2|A|^2+6|B|^2-\frac32|A+B|^2=\frac12|A-3B|^2\geq0.
\]

With \(A=\phi'V_k\), \(B=\psi'v_k\), the first term is precisely \(\phi''|V_k|^2\). The other cost is \(CK\mathcal F\). Since \(\lambda\geq K\), division by the positive quantity \(\lambda\mathcal F\) yields \(\lambda/K\leq C\).

For the maximum point \(x_0\) and any \(x\),

\[
\log\frac{\lambda_1(x)}{\lambda_1(x_0)}
\leq\frac12\log2+D_1(e^{D_2M}-1).
\]

Thus \(\lambda_1\leq CK\) globally. Combining the spectral lower bound with \(|\chi+W|\leq C\sqrt K\) proves the asserted mixed complex Hessian estimate.

All assumptions have accounted-for roles. No step uses the Gauduchon condition, and no hidden bound on the pure Hessian is needed.

## 11. Numerical ledger

| Stage | Verified allocation |
|---|---|
| Gradient norm differentiation | \(1/4-1/20=1/5\) |
| Third derivatives and linear torsion Hessians | \(1/5-1/30=1/6\) |
| Derivative-cancellation lemma | At most \(1/12\), e.g. four allocations of \(1/48\) |
| Remaining linear eigenvalue derivative | At most \(1/60\) |
| Residual positive Hessian budget | \(1/6-1/12-1/60=1/15\) |
| Coefficient retained for closure | \(1/20<1/15\) |
| Diagonal mixed-Hessian lower bound | \((1/20)(1/2)=1/40\) |
| Case 1 final coefficient | \(40\cdot2=80\) |
| Case 2 | \((1/6)(1/2)(1/n)=1/(12n)\) |

## 12. External reference audit and formula comparison

The required theorem search was performed first, with the full statement and the conversion formula. Its five results were unrelated. Built-in web search with the same statement then identified the primary source, [STW, arXiv:1503.04491v2](https://arxiv.org/abs/1503.04491), revised 8 December 2017.

The local `STW17.txt` was read for the Section 2 context and Section 3 calculations. The PDF was rendered and pages 7, 15, 16, 22, 23, 24 and 25 were visually inspected. The key source is :codex-file-citation{path="/Users/mingchen/Non-Kahler/research/sources/STW17.pdf" purpose="source"}.

The PDF confirms the conjugated connection in (3.17) and (3.20), the mixed-Hessian bar before (3.24), and the mixed entry in the lower bound after (3.55). These features are obscured in text extraction. The supplied proof matches them. The source uses a different perturbation and a weaker initial square expansion; the reconstruction's replacements were verified directly above. Its Case 2 coefficient \(1/(12n)\) is weaker than the source's \(1/(10n)\) and suffices. These comparisons are evidence of formula agreement, not an invocation of the source's full estimate. [STW, Section 3](https://arxiv.org/pdf/1503.04491).

The source's general subsolution theorem is not used: the conditional positive-background coercivity supplies the needed alternative directly. Likewise, its existence theorem and subsequent gradient and regularity estimates play no role here.

## 13. Findings and artifacts

- Critical errors: **none**.
- Mathematical gaps: **none within the stated conditional scope**.
- Cosmetic issue: the missing TeX backslash in `sum_kf_k` does not change the intended sum.
- Conditional dependency: `stw_matrix_structure_01`, exactly as specified in the request.
- Final machine-readable output: `verification.json` in this directory.
- Detailed structured audit: `audit_details.json` in this directory.
- Rethlas records: `memory/stw_second_order_reconstruction_01/` relative to the verification workspace.

If the precursor's independently audited identities change, the uses of those identities must be revisited; this verdict establishes the core implication under the supplied identities.
