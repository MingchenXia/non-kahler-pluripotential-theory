# Verification report: Gauduchon surface uniqueness

**Run:** gauduchon_surface_uniqueness_01  
**Verdict:** correct  
**Critical errors:** 0  
**Gaps:** 0

## Scope and method

This is an independent correctness audit of the supplied smooth mixed-form identity, its conditional uniqueness consequence, the compact Gauduchon surface corollary, and every scope assertion in the supplied text. It makes no novelty or solution-existence claim.

The proof was checked in textual order, with 15 structured checks persisted in this run's MCP memory. The required skills were used in order: verify-sequential-statements, check-referenced-statements, and synthesize-verification-report. Independent secondary checks of signs/positivity and dimension/scope agreed with the sequential audit.

Only the accepted inputs are used: elementary smooth differential-form calculus and Stokes on compact manifolds without boundary, Hermitian matrix positivity and diagonalization, connectedness, the specified operators, and the definition of a Gauduchon metric. No external theorem is needed.

The input inspected was [gauduchon-surface-uniqueness.md](../../inputs/gauduchon-surface-uniqueness.md). Limited read-only inspection of the adjacent counterexample inputs confirmed their stated ambient space is projective three-space; their construction is not a premise of this proof. No book file was modified.

## 1. Opening context and hypotheses

The reference to dimension three matches the ambient space stated in the adjacent inputs, including [degenerate-nonuniqueness.md](../../inputs/degenerate-nonuniqueness.md) and [numa-thin-zero-set.md](../../inputs/numa-thin-zero-set.md). No conclusion about a surface follows from those examples. The opening assertion about cancellation on surfaces is justified by the calculations below.

For the proposition, \(X\) is connected and compact, with its complex orientation and no boundary. A Hermitian background is a smooth positive definite real \((1,1)\)-form. Smooth \(\omega\)-plurisubharmonic functions are real valued and satisfy
\[
A=\omega+dd^cu\geq0,\qquad B=\omega+dd^cv\geq0.
\]
Thus \(A,B\) are smooth real semipositive \((1,1)\)-forms, and \(w=u-v\) is smooth real. The equality \(A^n=B^n=f\,dV\), with smooth strictly positive \(dV\), also implies that \(f\) is smooth and nonnegative.

Each summand of
\[
T=\sum_{j=0}^{n-1}A^j\wedge B^{n-1-j}
\]
has bidegree \((n-1,n-1)\) and total degree \(2n-2\). All integrands in the asserted identity are smooth real top-degree forms.

## 2. Difference of powers

Forms of total degree two commute under wedge product. Consequently the ordinary polynomial identity applies:
\[
A^n-B^n=(A-B)\wedge T.
\]
Linearity gives \(A-B=dd^cw\), and the common Monge–Ampère measure therefore gives the pointwise equality
\[
dd^cw\wedge T=0.
\]
No closedness of the background or of \(T\) is used.

## 3. Normalizations, product rule, and reality

With the conventions in the question,
\[
d^c=\frac{i}{4\pi}(\bar\partial-\partial),\qquad
dd^c=d\circ d^c=\frac{i}{2\pi}\partial\bar\partial.
\]
Indeed, \(\partial^2=\bar\partial^2=0\) and
\(\bar\partial\partial=-\partial\bar\partial\). These identities also give
\(d^cd=-dd^c\).

Since \(d^c(w^2)=2w\,d^cw\), the ordinary graded product rule yields
\[
dd^c(w^2)=2w\,dd^cw+2\,dw\wedge d^cw.
\]
The coefficient and sign in the draft are exact.

For real \(w\), put \(\alpha=\partial w\), so that
\(\bar\partial w=\bar\alpha\). Then
\[
Q:=dw\wedge d^cw
=\frac{i}{4\pi}(\alpha+\bar\alpha)\wedge(\bar\alpha-\alpha)
=\frac{i}{2\pi}\alpha\wedge\bar\alpha.
\]
The squares of the individual one-forms vanish. Hence \(Q\) is of pure bidegree \((1,1)\), and complex conjugation leaves it unchanged. Its Hermitian matrix is
\[
\frac{1}{2\pi}(w_j\overline{w_k})_{j,k},
\]
which is positive semidefinite. Equivalently, for a real tangent vector \(\xi\),
\[
Q(\xi,J\xi)=
\frac{dw(\xi)^2+dw(J\xi)^2}{4\pi}\geq0.
\]
As a direct sign check, \(w=x\) in one coordinate \(z=x+iy\) gives
\(Q=(4\pi)^{-1}dx\wedge dy\).

## 4. Both Stokes signs and all bidegrees

Let \(\phi\) be any smooth function. The form
\(\bar\partial\phi\wedge T\) has bidegree \((n-1,n)\), so its
\(\bar\partial\)-derivative vanishes by dimension. Ordinary Stokes gives
\[
0=\int_X\partial(\bar\partial\phi\wedge T)
=\int_X\partial\bar\partial\phi\wedge T
-\int_X\bar\partial\phi\wedge\partial T.
\]
The minus sign comes from the total degree one of \(\bar\partial\phi\).

Next, \(\phi\,\partial T\) has bidegree \((n,n-1)\), so its
\(\partial\)-derivative vanishes by dimension. A second use of Stokes gives
\[
0=\int_X\bar\partial(\phi\,\partial T)
=\int_X\bar\partial\phi\wedge\partial T
+\int_X\phi\,\bar\partial\partial T.
\]
Combining these equalities and using
\(\bar\partial\partial T=-\partial\bar\partial T\) yields
\[
\int_X\partial\bar\partial\phi\wedge T
=\int_X\phi\,\partial\bar\partial T.
\]
Multiplication by \(i/(2\pi)\) proves
\[
\boxed{\int_Xdd^c\phi\wedge T=\int_X\phi\,dd^cT.}
\]

The resulting sign is positive. No hypothesis \(dT=0\), \(d^cT=0\), or \(dd^cT=0\) is needed for this integration identity. Compactness, absence of boundary, and smoothness justify the two applications of Stokes.

## 5. The mixed-form defect identity

Taking \(\phi=w^2\), the product rule gives
\[
\int_Xw^2dd^cT
=2\int_Xw\,dd^cw\wedge T+2\int_XQ\wedge T.
\]
The first integral is zero because \(dd^cw\wedge T=0\) pointwise. Thus
\[
\boxed{\int_Xdw\wedge d^cw\wedge T
=\frac12\int_Xw^2dd^cT.}
\]
The displayed identity in the proof is correct, including its factor \(1/2\).

## 6. Mixed positivity and zero integral

Diagonalization expresses a semipositive \((1,1)\)-form as a nonnegative sum of rank-one forms \(i\beta\wedge\bar\beta\). Expanding the mixed wedge products shows that each \(A^j\wedge B^{n-1-j}\) is strongly positive or zero. Wedging with the semipositive rank-one form \(Q\) therefore produces a nonnegative top-degree form. This verifies the exact positivity needed in the draft.

If \(dd^cT=0\), the defect identity gives \(\int_XQ\wedge T=0\). Write
\(Q\wedge T=h\,dV\), where \(h\) is smooth and nonnegative. If \(h\) were positive at any point, continuity would give a nonempty open neighborhood of positive integral. Hence \(h=0\) everywhere.

Moreover, the sum
\[
Q\wedge T=\sum_{j=0}^{n-1}Q\wedge A^j\wedge B^{n-1-j}
\]
has nonnegative summands. Its pointwise vanishing forces every summand to vanish, in particular \(Q\wedge B^{n-1}=0\).

## 7. Strict positivity and detection of \(dw\)

At a point where \(f>0\), the equality \(B^n=f\,dV>0\) says that the determinant of the semipositive Hermitian matrix of \(B\) is positive. All its eigenvalues are nonnegative, so every eigenvalue must be strictly positive. Thus \(B\) is positive definite; the same argument applies to \(A\).

Choose a complex coframe with
\[
B=i\sum_k\theta^k\wedge\bar\theta^k,
\qquad \partial w=\sum_k a_k\theta^k.
\]
Direct expansion gives
\[
Q\wedge B^{n-1}
=\frac{\sum_k|a_k|^2}{2\pi n}\,B^n.
\]
Off-diagonal terms vanish, and the diagonal terms have the factor
\((n-1)!/n!=1/n\). Because \(B^n>0\), vanishing of this summand forces every \(a_k\) to be zero. Then \(\partial w=0\); reality gives \(\bar\partial w=0\), hence \(dw=0\).

The proof needs just the \(B^{n-1}\) term. Its additional observation that \(A\) is positive definite is true and harmless.

## 8. Exact role of dense positivity and connectedness

The preceding step proves \(dw=0\) on \(\{f>0\}\). Smoothness makes \(dw\) continuous. If the positive locus is dense, its vanishing extends to every point of \(X\).

A function with zero differential is locally constant, and connectedness makes it a single constant on all of \(X\). This proves the proposition's uniqueness consequence.

The argument requires no positive uniform lower bound for \(f\), no connectedness of the positive locus, and no measure-zero hypothesis on the zero set. Empty interior of the zero set can coexist with positive measure; density and continuity still suffice. Without density, this proof does not automatically control the differential inside an open zero-density region.

## 9. The surface corollary

The fixed smooth strictly positive \(dV\) is inherited from the proposition. The two solutions use the same \(c>0\), so their top powers agree with common density \(F=cf\).

For \(n=2\),
\[
T=A+B=2\omega+dd^c(u+v).
\]
The identities \(\partial^2=\bar\partial^2=0\) give
\(dd^c(dd^cu)=dd^c(dd^cv)=0\). Consequently
\[
dd^cT=2dd^c\omega.
\]
The Gauduchon condition \(dd^c\omega^{n-1}=0\) is exactly
\(dd^c\omega=0\) in dimension two. Thus \(dd^cT=0\).

For nonnegative \(f\), \(\{f>0\}=X\setminus\{f=0\}\). The assumption
\(\operatorname{int}\{f=0\}=\varnothing\) is precisely the density of this complement. Since \(c>0\), the positive loci of \(cf\) and \(f\) coincide. Every hypothesis of the proposition now holds, so \(u-v=C\).

“Normalized” has its usual meaning: both potentials satisfy the same normalization fixing additive constants. For example,
\(\sup_Xu=\sup_Xv=0\) gives \(C=0\). A common mean-zero normalization also suffices. No particular such choice is required for the proof. Specifying one explicitly would be an optional editorial clarification, not a gap.

The corollary asserts uniqueness of solutions that exist, and proves no existence statement.

## 10. Smoothness, arbitrary backgrounds, and conformal changes

All operations in the proof are classical smooth operations, including the pointwise continuous differential \(dw\). The argument supplies no extension to all bounded solutions.

An arbitrary Hermitian surface metric need not have \(dd^c\omega=0\); the cancellation used above therefore cannot be inferred for every Hermitian background.

If \(\widetilde\omega=e^\psi\omega\), then
\[
(\widetilde\omega+dd^cu)^2
=e^{2\psi}\omega^2+2e^\psi\omega\wedge dd^cu+(dd^cu)^2.
\]
The original square is \(\omega^2+2\omega\wedge dd^cu+(dd^cu)^2\), so the conformal replacement generally changes the equation. In general even multiplying the original volume form by \(e^{2\psi}\) would not align all terms. A solution for the original fixed background is therefore not automatically a solution for the conformal representative. No conformal existence theorem is used as a premise; the scope statement is an elementary comparison of the equations.

## 11. Why higher-dimensional Gauduchon alone is insufficient

Let \(a=dd^cu\) and \(b=dd^cv\). These are both \(\partial\)- and
\(\bar\partial\)-closed. In dimension three,
\[
T=3\omega^2+3\omega\wedge(a+b)+(a^2+a\wedge b+b^2).
\]
It follows that
\[
dd^cT=3dd^c(\omega^2)+3dd^c\omega\wedge(a+b).
\]
The Gauduchon condition cancels the first term. It does not automatically cancel the second term.

### Explicit compact example, even with equal positive densities

Take the complex three-torus
\[
X=(\mathbb C/(\mathbb Z+i\mathbb Z))^3,
\qquad e_j=i\,dz_j\wedge d\bar z_j,
\qquad x_j=\operatorname{Re}z_j.
\]
Set
\[
h=2+\cos(2\pi x_1),\qquad
\omega=e_1+h e_2+h^{-1}e_3.
\]
The coefficients are smooth periodic and positive. Further,
\[
\omega^2=2h e_1e_2+2h^{-1}e_1e_3+2e_2e_3.
\]
Differentiating the first two coefficients by \(dd^c\) contributes \(e_1\), which repeats an existing factor; the last coefficient is constant. Therefore \(dd^c\omega^2=0\), so \(\omega\) is Gauduchon.

For a function of one real coordinate the normalization gives
\[
dd^c\phi(x_j)=\frac{\phi''(x_j)}{8\pi}e_j.
\]
Choose
\[
u=v=\frac{1}{4\pi}\cos(2\pi x_2),\qquad
a=dd^cu=-\frac18\cos(2\pi x_2)e_2.
\]
Then \(A=B=\omega+a>0\): the \(e_2\) coefficient is at least \(7/8\), and the other two are positive. With \(dV=e_1e_2e_3\),
\[
A^3=B^3=f\,dV,\qquad
f=6\,\frac{h-\frac18\cos(2\pi x_2)}{h}>0.
\]
Thus all equal-density conditions hold. Nevertheless,
\[
T=3A^2,\qquad dd^cT=6dd^c\omega\wedge a.
\]
At \(x_1=x_2=0\), one has
\[
(h^{-1})''=\frac{4\pi^2}{9},\qquad
[dd^c\omega]_{e_1e_3}=\frac{\pi}{18},\qquad a=-\frac18e_2,
\]
hence
\[
\boxed{dd^cT=-\frac{\pi}{24}e_1e_2e_3\ne0.}
\]

This directly verifies the failure of the implication from higher-dimensional Gauduchon to \(dd^cT=0\), including in the setting of equal Monge–Ampère measures. It is not a uniqueness counterexample, since \(u=v\). The right side of the audited identity is the exact scalar integration defect; for particular \(w\), that integral may vanish even when \(dd^cT\) is not the zero form.

## 12. Assumption ledger

| Assumption | Exact use |
| --- | --- |
| Compact, no boundary | Both Stokes integrals have zero boundary contribution. |
| Smooth real potentials and forms | Classical derivatives, reality/positivity of \(Q\), pointwise wedge identities, and continuity of \(dw\). |
| \(\omega\)-plurisubharmonicity | Supplies \(A,B\geq0\) and positivity of mixed products. |
| Same Monge–Ampère measure | Gives \(dd^cw\wedge T=0\). |
| Strictly positive \(dV\) | Converts \(f>0\) to a positive determinant and supports the zero-integral argument. |
| \(dd^cT=0\) | Makes the nonnegative energy integral zero. |
| Dense positive locus | Extends vanishing of \(dw\) to every point. |
| Connectedness | Turns local constancy into one global constant. |
| Surface dimension and Gauduchon | Together give \(dd^cT=2dd^c\omega=0\). |
| Same \(c>0\) | Gives equal top powers and preserves the positive locus. |
| Common normalization | Removes the remaining additive constant. |

The restriction \(n\geq2\) is harmless: the proposition's calculation also works in dimension one with \(T=1\). Smoothness of \(f\) is automatic if smooth solutions exist; the zero-set argument itself uses nonnegativity and empty interior. These are genuine redundancies, not omitted necessary steps.

## 13. Reference checks and strict conclusion

The external-reference inventory is empty. Stokes, Hermitian linear algebra, connectedness, operator definitions, and the Gauduchon definition are expressly accepted inputs. The contextual conformal mention is not used to invoke an external theorem. Accordingly no arXiv or web theorem search was required.

Every mathematical check passed. There are no critical errors and no gaps. Under the strict verdict rule, the supplied proof is **correct**, and repair hints are empty.
