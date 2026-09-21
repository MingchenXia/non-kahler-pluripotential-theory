# Verification report: stw_matrix_structure_01

## Verdict

**Correct.** The complete supplied derivation passes. There are no critical errors and no gaps. The conclusions are the stated preparatory algebraic identities and coercivity inequality.

Input: [supplied proof](../../inputs/stw-matrix-structure.md).

All deductions were checked in textual order. Detailed structured checks are in [statement_checks.jsonl](../../memory/stw_matrix_structure_01/statement_checks.jsonl); the external attribution check is in [reference_checks.jsonl](../../memory/stw_matrix_structure_01/reference_checks.jsonl).

## 1. Conventions, inverse map, and admissibility

The assumptions are complex dimension \(n\ge2\), smooth Hermitian metrics \(\gamma,\gamma_0\), a real smooth potential \(v=u/(2\pi)\), and the stipulated normalization
\[
\ddc u=i\partial\bar\partial v,\qquad
\gamma=i\gamma_{i\bar j}dz^i\wedge d\bar z^j,\qquad
\star\gamma^{n-1}=(n-1)!\gamma.
\]
The Hodge star is the complex-linear extension of the real metric Hodge star. The covariant derivatives are Chern derivatives. In holomorphic coordinates, lowering the upper index in the difference of Chern connection coefficients gives exactly
\[
T_{ab\bar c}=\partial_a\gamma_{b\bar c}-\partial_b\gamma_{a\bar c}.
\]

In a unitary frame, \(P(H)=((\operatorname{tr}H)I-H)/(n-1)\) preserves trace. Consequently
\[
P^{-1}(Q)=(\operatorname{tr}Q)I-(n-1)Q.
\]
This proves \(P(\chi)=Q_0\) and \(P(W)=Z\), with the displayed factors. The exterior-algebra identity
\[
\frac{\star(H\wedge\gamma^{n-2})}{(n-1)!}=P(H)
\]
holds for every \((1,1)\)-form \(H\), using the coefficient-matrix identification.

If a positive form \(\omega\) has eigenvalues \(r_i\), the normalized star of \(\omega^{n-1}\) has eigenvalues \(\prod_{j\ne i}r_j\). Its determinant is \((\prod_i r_i)^{n-1}\). This verifies positivity of \(Q_0\) and the exponent \(h=(n-1)(F+b)\) in the matrix version of the volume equation.

The displayed positivity and equation specify the admissible equation under consideration; they do not assert that arbitrary \(v\) solves it. The later calculations use only \(Q=P(g)>0\). For \(n\ge3\), \(g=\operatorname{diag}(2,\ldots,2,-1)\) is an explicit indefinite example with \(P(g)>0\). For \(n=2\), \(P\) interchanges the two eigenvalues and \(P(g)>0\) does force \(g>0\); this special case does not invalidate the general statement that positivity of \(g\) is unnecessary.

## 2. Independent alternating-determinant derivation

### 2.1 The sign in \(\bar\partial\gamma\)

Passing the differentiated antiholomorphic one-form across \(dz^a\) gives
\[
\bar\partial\gamma
=-i\sum_{a,b,c}\partial_{\bar b}\gamma_{a\bar c}\,
 dz^a\wedge d\bar z^b\wedge d\bar z^c.
\]
Antisymmetrizing \(b,c\), and using Hermitian symmetry, gives
\[
\partial_{\bar b}\gamma_{a\bar c}
-\partial_{\bar c}\gamma_{a\bar b}
=\overline{T_{bc\bar a}},
\]
so the stated coefficient is \(-i/2\). Since \(\gamma\) has even degree,
\[
\bar\partial\gamma^{n-2}
=(n-2)\bar\partial\gamma\wedge\gamma^{n-3}.
\]
Multiplication by \(i\partial v\) therefore leaves the positive factor \((n-2)/2\).

### 2.2 Hodge transpose and complementary indices

Write \(E_{i\bar j}=i\,dz^i\wedge d\bar z^j\) and \(dV=\gamma^n/n!\). Under the complex-bilinear metric pairing,
\[
\langle E_{r\bar s},E_{j\bar i}\rangle
=\delta_{ri}\delta_{sj}.
\]
Thus, if \(\star\eta=\sum C_{i\bar j}E_{i\bar j}\), its coefficient is determined by
\[
C_{i\bar j}\,dV=\eta\wedge E_{j\bar i}.
\]
This is the precise reason for the output transpose: the missing holomorphic slot is \(j\), and the missing antiholomorphic slot is \(i\).

Apply this to
\[
\eta=dz^p\wedge dz^a\wedge d\bar z^b\wedge d\bar z^c
\wedge\gamma^{n-3}.
\]
Expansion of \(\gamma^{n-3}\) produces \((n-3)!\) for each set of remaining paired indices. The signed matching of the complementary triples is exactly
\[
\delta^{paj}_{bci}.
\]
The positive sign can be fixed directly on \(p=b=1,a=c=2,i=j=3\): the four-form \(dz^1\wedge dz^2\wedge d\bar z^1\wedge d\bar z^2\) is \(E_{1\bar1}\wedge E_{2\bar2}\). Antisymmetry then gives every other nonzero matching; repeated indices give zero. Hence, in every dimension \(n\ge3\),
\[
\star\eta=(n-3)!\sum_{i,j}\delta^{paj}_{bci}E_{i\bar j}.
\]
It follows that
\[
A_{i\bar j}
=\frac{(n-2)(n-3)!}{2(n-1)!}
\sum_{p,a,b,c}v_p\overline{T_{bc\bar a}}\,\delta^{paj}_{bci}
=\frac1{2(n-1)}
\sum_{p,a,b,c}v_p\overline{T_{bc\bar a}}\,\delta^{paj}_{bci}.
\]
There is no omitted \(i\), sign, factorial, or index transposition.

### 2.3 All six determinant terms

The determinant expands as
\[
\begin{aligned}
\delta^{paj}_{bci}
={}&\delta_{pb}\delta_{ac}\delta_{ji}
 +\delta_{pc}\delta_{ai}\delta_{jb}
 +\delta_{pi}\delta_{ab}\delta_{jc}\\
 &-\delta_{pb}\delta_{ai}\delta_{jc}
 -\delta_{pc}\delta_{ab}\delta_{ji}
 -\delta_{pi}\delta_{ac}\delta_{jb}.
\end{aligned}
\]
Put
\[
S=\sum_{p,k}v_p\overline{T_{pk\bar k}},\quad
U_j=\sum_k\overline{T_{jk\bar k}},\quad
R_{i\bar j}=\sum_kv_k\overline{T_{kj\bar i}}.
\]
In the displayed order, contraction of the six terms gives
\[
\delta_{ij}S,\quad -R_{i\bar j},\quad -v_iU_j,\quad
-R_{i\bar j},\quad \delta_{ij}S,\quad -v_iU_j.
\]
The sum is twice the three-term bracket in the proof.

### 2.4 Real part and conjugations

For a complex \((1,1)\)-form represented by \(A\), form conjugation represents the adjoint matrix \(A^*\), because conjugating \(i\) and reversing \(d\bar z^i\wedge dz^j\) supply cancelling minus signs. The real Hodge star commutes with conjugation. Thus \(Z=(A+A^*)/2\).

The reality of \(v\) gives \(\overline{v_p}=v_{\bar p}\). Taking the adjoint of the three-term formula produces precisely
\[
\delta_{ij}\sum_{p,k}v_{\bar p}T_{pk\bar k}
-v_{\bar j}\sum_kT_{ik\bar k}
-\sum_kv_{\bar k}T_{ki\bar j}.
\]
Together with the holomorphic three terms, this proves the supplied \(2(n-1)Z_{i\bar j}\) identity with every conjugation and factor checked.

### 2.5 Dimension two and forbidden coefficients

For \(n=2\), \(\bar\partial\gamma^0=0\), so \(A=Z=0\). Independently, every three-index alternating determinant vanishes in dimension two, so the expanded formulas vanish as well. No use of the nonexistent factorial \((-1)!\) is made.

For \(i\ne j\), the coefficient of \(v_j\) is zero: the trace term vanishes, the explicit \(v_i\) term has a different index, and the remaining coefficient contains \(T_{jj\bar i}=0\). Taking the adjoint proves absence of \(v_{\bar i}\).

For \(i=j\), the middle term removes all \(p=i\) contributions from the trace sum, and the last term removes all \(k=i\) contributions. Their intersection already vanishes by skew symmetry. The result is exactly the sum over \(p\ne i,k\ne i\), including its conjugate half. In dimension two its remaining indices necessarily coincide, so it is zero.

## 3. Covariant derivative exclusions

The complete six-term expression is a tensor contraction using the metric and torsion. Metric compatibility and preservation of complex type allow covariant differentiation of this identity. Skew symmetry in the two torsion slots remains true for every covariant derivative of the torsion.

The phrase “a unitary frame parallel at the point” is valid: it does not require holomorphic coordinates with all Chern connection coefficients zero. For the second derivative, the tensor Leibniz rule is used; a frame parallel to second order is unnecessary.

For \(p,k\ne1\), set \(C_{pk}=\overline{T_{pk\bar k}}\). The holomorphic half of the first derivative has terms
\[
(\nabla_1v_p)C_{pk}+v_p\nabla_1C_{pk}.
\]
The antiholomorphic half is
\[
(\nabla_1v_{\bar p})T_{pk\bar k}
+v_{\bar p}\nabla_1T_{pk\bar k}.
\]
The second line is the derivative of the conjugate summand in direction \(1\); it is not obtained by conjugating the entire first derivative, which would conjugate its differentiation direction too.

The four terms after the further \(\bar1\) derivative of the holomorphic half are
\[
\begin{aligned}
&(\nabla_{\bar1}\nabla_1v_p)C_{pk}
+(\nabla_1v_p)\nabla_{\bar1}C_{pk}\\
&\quad+(\nabla_{\bar1}v_p)\nabla_1C_{pk}
+v_p\nabla_{\bar1}\nabla_1C_{pk}.
\end{aligned}
\]
The antiholomorphic half has the identical pattern with \(v_{\bar p}\) and \(T\). Every differentiated potential retains \(p\ne1\). Consequently the stated pure Hessian and third-derivative components are absent, including in terms where differentiation hits a coefficient. These are statements about the ordered covariant derivatives stipulated in the proof; no commuting of derivatives is used.

## 4. Linearized weights

Hermitian diagonalization of \(g\) is valid without positivity of \(g\). Positivity of \(P(g)\) gives \(\mu_i>0\), and
\[
\mu_j-\mu_i=\frac{\lambda_i-\lambda_j}{n-1}.
\]
Thus the \(\mu_i\) increase, the \(t_i=1/\mu_i\) decrease, and
\[
f_i=\frac{\mathcal F-t_i}{n-1}
\]
increase. Each \(t_i\) appears \(n-1\) times when the \(f_i\) are summed, proving \(\mathcal F=\sum_i t_i\).

The weights really are the linearization:
\[
D\Phi_g(H)=\operatorname{tr}(Q^{-1}P(H))
=\operatorname{tr}(P(Q^{-1})H).
\]
At a diagonal matrix \(g\), \(P(Q^{-1})=\operatorname{diag}(f_i)\).

Exchanging the finite sums gives
\[
\sum_i f_i\lambda_i
=\sum_jt_j\frac{\sum_{i\ne j}\lambda_i}{n-1}
=\sum_jt_j\mu_j=n.
\]
No sign assumption on \(\lambda_i\) enters this calculation.

For \(k>1\), the sum defining \(f_k\) includes \(t_1\ge\mathcal F/n\), so
\[
\frac{\mathcal F}{n(n-1)}\le f_k\le\frac{\mathcal F}{n-1}.
\]
Also \((n-1)f_1=\sum_{i>1}t_i\), proving the stated individual \(t_i\) bounds, and \(f_n\ge\mathcal F/n\) follows from maximality. Every bound has the asserted index range.

## 5. Explicit coercivity

For the matrix trace pairing,
\[
\operatorname{tr}(C P(H))
=\frac{(\operatorname{tr}C)(\operatorname{tr}H)-\operatorname{tr}(CH)}{n-1}
=\operatorname{tr}(P(C)H).
\]
Therefore
\[
\sum_i f_i\chi_{i\bar i}
=\operatorname{tr}(Q^{-1}Q_0)
\ge\tau\mathcal F.
\]
Neither positivity of \(\chi\) nor simultaneous diagonalization of \(g\) and \(Q_0\) is needed.

Let \(S=\sum_i\lambda_i=\sum_i\mu_i>0\). Since \(\lambda_1\) is maximal, \(\lambda_1\ge S/n>0\). Moreover
\[
S-\lambda_1=(n-1)\mu_1>0.
\]
Hence
\[
n\mu_n\ge S>\lambda_1.
\]
The determinant bound and ordering give
\[
\mu_1^{n-1}\mu_n\le\prod_i\mu_i=\det Q\le D,
\]
and consequently
\[
\mathcal F\ge\frac1{\mu_1}
\ge\left(\frac{\lambda_1}{nD}\right)^{1/(n-1)}.
\]
An explicit sufficient threshold is
\[
\boxed{L=nD\left(\frac{2n}{\tau}\right)^{n-1}.}
\]
For \(\lambda_1\ge L\), \(\mathcal F\ge2n/\tau\), and Euler's identity yields
\[
\sum_i f_i(\chi_{i\bar i}-\lambda_i)
\ge\tau\mathcal F-n
\ge\frac{\tau}{2}\mathcal F.
\]
Finally, AM-GM on positive \(t_i\) gives
\[
\boxed{\mathcal F\ge n(\det Q)^{-1/n}\ge nD^{-1/n}.}
\]

## 6. Exact complex concavity square

The Hessian of the real function on Hermitian matrices has its canonical complex-bilinear extension to all complex matrix directions. Differentiate the inverse:
\[
D(Q^{-1})[C]=-Q^{-1}P(C)Q^{-1}.
\]
Since \(P(B^*)=P(B)^*\), this gives
\[
\begin{aligned}
-D^2\Phi_g(B,B^*)
&=\operatorname{tr}(Q^{-1}P(B)Q^{-1}P(B)^*)\\
&=\left\|Q^{-1/2}P(B)Q^{-1/2}\right\|_{\rm HS}^2.
\end{aligned}
\]
There is no factor two in this bilinear evaluation. At diagonal \(Q\) the full expression is
\[
\frac1{(n-1)^2}\left[
\sum_i\frac{\left|\sum_{j\ne i}B_{j\bar j}\right|^2}{\mu_i^2}
+\sum_{i\ne j}\frac{|B_{i\bar j}|^2}{\mu_i\mu_j}
\right].
\]
The off-diagonal sum is over ordered pairs. For a general complex matrix the entries \(B_{k\bar1}\) and \(B_{1\bar k}\) are independent. Thus the supplied coefficient of \(|B_{k\bar1}|^2\) is exactly correct; combining a Hermitian pair would be a different way of grouping terms.

Finally,
\[
f_k-f_1
=\frac{\mu_k-\mu_1}{(n-1)\mu_1\mu_k}
=\frac{\lambda_1-\lambda_k}{(n-1)^2\mu_1\mu_k}.
\]
Division is valid when \(\lambda_k<\lambda_1\); at coincidence the coefficient has continuous value \(1/((n-1)^2\mu_1^2)\).

## 7. External-reference audit

The required full-statement arXiv-theorem search was performed first. It returned one related formula in a different paper and four unrelated results; none was accepted as the exact STW citation. The web fallback located the original STW paper. The supplied local PDF was inspected visually on pages 26–27, and Section 2 was read from the accompanying text.

The dictionary is: STW \(\alpha=\gamma\), STW potential \(u=v\), STW \(\widetilde\chi=Q_0\), and STW \(\widetilde g=P_\gamma(g)\). The bars and factors in (4.3), the following unnumbered diagonal formula, and the differentiated diagonal formula agree. Section 2 supplies the same inverse \(P\) and coefficient structure. These source checks corroborate the independent derivation above. [STW, Sections 2 and 4](https://arxiv.org/pdf/1503.04491).

The paper's global Gauduchon and existence hypotheses are not being transferred to these local algebraic calculations. The supplied proof does not invoke the general subsolution theorem, establish a full second-order estimate, or establish existence.

## 8. Independent computational corroboration and artifacts

The [audit script](exterior_audit.py) starts with real \(dx^r,dy^r\), represents \(dz^r=dx^r+i\,dy^r\), and uses \(\gamma=2\sum_r dx^r\wedge dy^r\). For the corresponding real metric \(2I\), the Hodge star on degree \(k\) forms is \(2^{n-k}\) times the Euclidean star. The program forms wedges and takes real-basis complementary stars before comparing with the claimed complex-index determinant.

All arithmetic in these dimensions consists of exactly representable Gaussian integers and dyadic numbers; comparisons use equality, with no numerical tolerance. The general-dimensional proof is given in Section 2 above; the finite checks provide independent corroboration.

| Dimension | Hodge monomials | \(P\)-basis forms | Torsion coefficient checks | Vanishing checks |
|---|---:|---:|---:|---:|
| 2 | Not needed: \(Z=0\) | 4 | 16 | 16 |
| 3 | 81 | 9 | 243 | 162 |
| 4 | 256 | 16 | 1,536 | 768 |
| 5 | 625 | 25 | 6,250 | 2,500 |
| 6 | 1,296 | 36 | 19,440 | 6,480 |
| Total | 2,258 | 90 | 27,485 | 9,926 |

Every check passed. Results are recorded in [exterior_audit.json](exterior_audit.json). The strict final verdict is stored in [verification.json](verification.json).

## Findings

Critical errors: none.

Gaps: none.

Repair hints: none required.
