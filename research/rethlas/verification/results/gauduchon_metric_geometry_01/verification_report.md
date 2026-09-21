**Verification report — gauduchon_metric_geometry_01**

**Verdict: correct, under the expressly accepted conditional precursor.** The complete supplied proof was checked in textual order. No critical errors or gaps were found. The radial product, intrinsic distance and completion assertions, blowup cone, intersection numbers, volume normalization, exact Hessian, and finite-distance positive-volume nef boundary are valid. No manuscript was edited.

The precursor's finite-family smoothness, positive degree-one homogeneity, smooth-ddc invariance, and positive definiteness on the quotient were accepted as instructed, without independent re-audit. The smooth TW equation, closed Stokes, and the book's `thm:gaud-volume-dual-formula` were also treated as supplied results. Reading the surrounding manuscript served to confirm definitions and normalizations. This verdict does not certify any additional statement from the precursor or the surrounding book.

**1. Opening setup and the normalized hypersurface.**

Here \(\mathscr P\) means the set of smooth real backgrounds \(\theta\) for which \(\theta+dd^c u>0\) for some smooth real \(u\). This is the relevant smooth-ddc definition, rather than an unspecified numerical positivity condition. If two backgrounds admit such representatives, their convex combinations admit the corresponding convex combinations of potentials. Positive scaling works in the same way. Positivity is open: on compact \(X\), a positive representative has a uniform positive lower bound against a fixed Hermitian form, which survives sufficiently small changes in the finite-dimensional family. Thus \(\mathscr C=V\cap\mathscr P\) is open and convex in \(V\).

The hypothesis \(V\cap dd^c C^\infty(X,\mathbb R)=\{0\}\) makes the map from \(V\) into the specified quotient injective. The accepted quotient Hessian therefore restricts to a smooth positive-definite Riemannian metric on \(\mathscr C\).

Euler's identity gives
\[
D\lambda_\theta(\theta)=\lambda(\theta)>0.
\]
Consequently \(1\) is a regular value and \(\mathscr S\) is a smooth hypersurface. It is nonempty by normalizing any element of \(\mathscr C\). It is also path connected: normalize a line segment in the convex cone. In the possible one-dimensional case it is a singleton. Its intrinsic distance is therefore well defined and finite between any two points.

**2. Proposition: the global product map.**

For every \(\theta\in\mathscr C\), positivity of \(\lambda\) permits
\[
r=\log\lambda(\theta),\qquad q=\frac{\theta}{\lambda(\theta)}.
\]
The cone property gives \(q\in\mathscr C\), and degree-one homogeneity gives \(\lambda(q)=1\). Conversely, \(e^rq\in\mathscr C\) and \(\lambda(e^rq)=e^r\) for \(q\in\mathscr S\). These formulas prove both inverse identities and smoothness. Thus \(\Phi\) is a global diffeomorphism.

Set \(F=\log\lambda\). Differentiating \(DF_\theta(\theta)=1\) gives
\[
D^2F_\theta(\chi,\theta)+DF_\theta(\chi)=0.
\]
The sign in the manuscript is therefore correct:
\[
g_\theta(\theta,\chi)=DF_\theta(\chi),\qquad
g_\theta(\theta,\theta)=1.
\]
Twice differentiating \(F(s\theta)=\log s+F(\theta)\) in affine directions gives
\[
g_{s\theta}(s\chi,s\eta)=g_\theta(\chi,\eta).
\]
For \(\xi\in T_q\mathscr S\), \(D\lambda_q(\xi)=0\), so \(g_q(q,\xi)=0\). Finally,
\[
D\Phi_{(r,q)}(a,\xi)=e^r(aq+\xi).
\]
Expanding the metric on two such vectors proves exactly
\[
\Phi^*g=dr^2+g_{\mathscr S}.
\]
There is no additional factor in the radial term.

**3. Proposition: intrinsic distance, completion, and divergent volume.**

For any piecewise smooth product path, apply the integral triangle inequality in \(\mathbb R^2\) to the vector \((r',|q'|_{g_{\mathscr S}})\). If \(L_q\) is the projected path length, this gives
\[
L\geq\sqrt{(r_1-r_0)^2+L_q^2}
\geq\sqrt{(r_1-r_0)^2+d_{\mathscr S}(q_0,q_1)^2}.
\]
The signed first component integrates to \(r_1-r_0\); the nonnegative second component integrates to \(L_q\). Thus the stated lower bound remains valid even when the radial coordinate reverses direction.

For the upper bound choose paths in \(\mathscr S\) with lengths tending to its intrinsic distance, use arc-length parametrization on a fixed interval, and take the radial coordinate to vary linearly. Their product lengths are \(\sqrt{(r_1-r_0)^2+L_q^2}\). A constant projected path covers the zero-length case. Taking the infimum proves the exact distance formula. This argument needs neither a minimizing geodesic in \(\mathscr S\) nor its completeness.

The formula implies that a sequence is Cauchy precisely when its two coordinate sequences are Cauchy. It also identifies the metric completion explicitly:
\[
\widehat{\mathscr C}\cong\mathbb R\times\widehat{\mathscr S},
\qquad
\widehat d^2=|r_1-r_0|^2+\widehat d_{\mathscr S}^{\,2}.
\]
Since \(\mathbb R\) is complete, the claimed equivalence follows in both directions. If “complete” is read as geodesic completeness, it agrees with metric completeness for these connected finite-dimensional Riemannian manifolds.

Length dominates the absolute change of \(r=\log\lambda\) on every subinterval. Consequently any path along which \(\lambda\to0\) or \(\lambda\to\infty\) has infinite length. The same reasoning, using partitions, applies to a general rectifiable path.

**4. The following positive-ray assertion.**

The curve \(t\mapsto e^t\theta\) has product coordinates
\[
\left(t+\log\lambda(\theta),\frac{\theta}{\lambda(\theta)}\right).
\]
It has speed one, and its endpoint distance is \(|t_1-t_0|\), equal to its length on that interval. It is therefore minimizing as claimed. This calculation concerns the radial factor and imposes no completeness condition on the other factor.

**5. Blowup example: incidence model, cone, and exact directions.**

Put the blown-up point at \(p=[1:0:0]\). The surface
\[
\{([x_0:x_1:x_2],[u:v])\in\mathbb P^2\times\mathbb P^1:
x_1v=x_2u\}
\]
is the asserted incidence model. Away from \(p\), the second coordinate is uniquely \([x_1:x_2]\). Near \(p\), the two charts are the usual blowup charts \(y=xt\) and \(x=sy\). They are smooth and replace the origin by the direction line \(\mathbb P^1\). This verifies the embedding \((\pi,f)\) and the extension of the pencil map. The same affine model is given in [Vakil's Intersection Theory Class 8, section 1.1, Example 1](https://math.stanford.edu/~vakil/245/245class8.pdf), and explicitly in [his Foundations of Algebraic Geometry Classes 49 and 50, section 5.1](https://math.stanford.edu/~vakil/0506-216/216class4950.pdf).

A fiber \(F\) of \(f\) is the strict transform of a line through \(p\), so its divisor class is \(L=H-E\). The restriction of \(f\) to \(E\) is an isomorphism to \(\mathbb P^1\), whereas \(\pi\) contracts \(E\).

The precise normalization of the forms is
\[
\int_{\mathbb P^1\subset\mathbb P^2}\omega_{\mathrm{FS},2}=1,
\qquad \int_{\mathbb P^1}\omega_{\mathrm{FS},1}=1.
\]
In particular \(\int_{\mathbb P^2}\omega_{\mathrm{FS},2}^2=1\). With \(h=\pi^*\omega_{\mathrm{FS},2}\) and \(\ell=f^*\omega_{\mathrm{FS},1}\), their classes are \(H\) and \(L\). For \(a>b>0\), the form \((a-b)h+b\ell\) is the pullback of a positive product form by an embedding, so it is positive. A nonzero tangent vector cannot be killed by both projections. Its class is exactly \(aH-bE\).

The curve integrals are

| Curve | \(\int h\) | \(\int\ell\) | \(\int((a-b)h+b\ell)\) |
|---|---:|---:|---:|
| Exceptional curve \(E\) | 0 | 1 | \(b\) |
| Pencil fiber \(F\) | 1 | 0 | \(a-b\) |

Every positive smooth representative has strictly positive integrals over both curves. This proves necessity and hence the exact cone description. It is sufficient to test these two curves because the positive representatives have already been constructed for every point satisfying the two inequalities.

For an explicit eligible space of forms take \(e=h-\ell\) and \(V=\operatorname{span}_{\mathbb R}\{h,e\}\). These are closed smooth representatives of \(H,E\). If \(ah-be\) is smoothly dd-c exact, Stokes on the two curves gives \(b=0\) and \(a-b=0\). Thus there is no nonzero exact direction. This construction also avoids silently replacing smooth-ddc equivalence by a different cohomological equivalence.

**6. Blowup example: intersection and volume normalizations.**

Two generic lines avoiding \(p\) give \(H^2=1\); such a pullback line misses \(E\), giving \(H\cdot E=0\). The exceptional normal bundle is \(\mathcal O_{\mathbb P^1}(-1)\), hence \(E^2=-1\). This normal-bundle statement is confirmed in [Vakil, Classes 49 and 50, section 4.4](https://math.stanford.edu/~vakil/0506-216/216class4950.pdf), with the same smooth surface and reduced point hypotheses.

Independently, the fiber description gives \(H\cdot L=1\) and \(L^2=0\), since \(\ell\) is pulled back from a curve. Substituting \(E=H-L\) reproduces the other intersection numbers, including their signs.

For the fixed closed representative \(\theta=ah-be\), the accepted smooth equation and probability normalization imply
\[
\lambda_\mu(\theta)^2
=\int_X(\theta+dd^c u)^2
=\int_X\theta^2
=a^2-b^2.
\]
The middle equality is closed Stokes; both cross and pure dd-c terms integrate to zero. The book defines \(\mathcal V_\mu=\lambda_\mu^n\), with no division by \(n!\). Since \(n=2\) and \(\lambda_\mu>0\), this proves exactly
\[
\mathcal V_\mu=a^2-b^2,\qquad \lambda_\mu=\sqrt{a^2-b^2},
\]
independently of the smooth positive probability measure. Closedness is used here specifically; this step makes no claim for arbitrary nonclosed forms.

**7. Blowup example: the Hessian and global Euclidean coordinates.**

Let \(\Delta=a^2-b^2\). For \(F=\frac12\log\Delta\),
\[
F_a=\frac a\Delta,\quad F_b=-\frac b\Delta,\quad
F_{aa}=F_{bb}=-\frac{a^2+b^2}{\Delta^2},\quad
F_{ab}=\frac{2ab}{\Delta^2}.
\]
Thus \(g=-D^2F\) is precisely the displayed quadratic differential. Its off-diagonal matrix entry is \(-2ab/\Delta^2\), so its cross term is \(-4ab\,da\,db/\Delta^2\). Both signs and the factor two are correct.

The coordinate change satisfies
\[
\Delta=e^{2r},\qquad da=a\,dr+b\,ds,\qquad db=b\,dr+a\,ds.
\]
Substitution gives coefficient one in both diagonal terms and zero mixed coefficient, hence \(g=dr^2+ds^2\). Its inverse is
\[
r=\tfrac12\log(a^2-b^2)=\log\lambda,\qquad
s=\operatorname{artanh}(b/a)>0.
\]
The exact domain is \(\mathbb R\times(0,\infty)\). In particular, using \(\log\mathcal V\) in place of \(\log\lambda\) would change the radial coefficient; the manuscript uses the correct variable.

The open half-plane is Euclidean convex, so its intrinsic distance equals ordinary Euclidean distance. Its completion is exactly \(\mathbb R\times[0,\infty)\). Neither infinite \(r\) nor infinite \(s\) produces an additional finite-distance completion point.

**8. Blowup example: nef boundary and its positive volume.**

At fixed finite \(r\), taking \(s\downarrow0\) sends the class to \(e^rH\). The representative \(h\) is semipositive. Taking the positive closed form \(\kappa=h+\ell\), the forms \(h+\varepsilon\kappa\) are positive for every \(\varepsilon>0\). This verifies precisely the book's nef condition. The classes \(H-\delta E\), \(0<\delta<1\), also approach \(H\) from inside the displayed cone.

Since \(H\cdot E=0\), no representative of \(H\) can be positive: positivity would force a strictly positive integral over \(E\). The same holds for every positive multiple of \(H\). Its square is one, and the corresponding multiple has square \(e^{2r}\).

The volume remains exactly \(e^{2r}\) along the fixed-\(r\) path to the boundary, whose length from \(s_0\) to zero is \(s_0\). This already proves finite-distance incompleteness at positive limiting volume. The value of the book's variational volume at the boundary agrees as well, by the following elementary expansion of its defining infimum.

For a Gauduchon metric \(\gamma\), put
\[
A_\gamma=\frac{\int_Xh\wedge\gamma}{D_\mu(\gamma)},\qquad
B_\gamma=\frac{\int_X\kappa\wedge\gamma}{D_\mu(\gamma)}>0.
\]
Interchanging two infima gives
\[
\lambda_\mu(h)
=\inf_\gamma A_\gamma
=\inf_{\varepsilon>0}\inf_\gamma(A_\gamma+\varepsilon B_\gamma)
=\inf_{\varepsilon>0}\lambda_\mu(h+\varepsilon\kappa).
\]
Here \(h+\varepsilon\kappa\) has class \((1+2\varepsilon)H-\varepsilon E\), so the explicit positive-cone formula yields
\[
\lambda_\mu(h)=\inf_{\varepsilon>0}\sqrt{1+4\varepsilon+3\varepsilon^2}=1.
\]
Homogeneity proves \(\mathcal V_\mu(e^rH)=e^{2r}\). No limiting smooth solution, minimizing boundary metric, or general boundary regularity theorem enters this calculation. These details clarify the boundary normalization; they do not introduce an extra hypothesis or repair a gap.

**9. Final comparison and assumption audit.**

The preceding \(\mathbb P^1\times\mathbb P^1\) example has \(\alpha^2=\beta^2=0\) and \(\int\alpha\wedge\beta=1\). Consequently its volume is \(2ab\), its root is \(\sqrt{2ab}\), and its metric is
\[
\frac12\left(\frac{da^2}{a^2}+\frac{db^2}{b^2}\right).
\]
The coordinates \((\log a/\sqrt2,\log b/\sqrt2)\) identify the positive quadrant with all of Euclidean \(\mathbb R^2\), confirming the completeness comparison. Only this explicit example was checked from the preceding section; the conditional precursor was not re-audited.

Finite dimension ensures an ordinary Riemannian setting; the absence of exact directions ensures nondegeneracy; nonemptiness and positivity permit normalization; smoothness permits differentiating homogeneity; homogeneity fixes the radial coefficient; the fixed probability measure fixes the equation's scalar normalization; closedness and the intersection numbers give the example's volume. No suspiciously unused hypothesis conceals an additional required argument.

Every metric and completion assertion is intrinsic to the indicated finite-dimensional family. The proof establishes no distance claim for paths permitted to leave that family. No BMP hypothesis, general boundary theorem, or novelty claim is used.

**10. References, persisted findings, and strict decision.**

The supplied proof contains no external-paper citation requiring an arXiv theorem match. The required reference-checking skill was applied: internal dependencies were classified as explicitly accepted, their definitions and downstream applications were checked, and the permitted elementary blowup facts were verified directly and corroborated by the primary lecture notes linked above. The arXiv-first rule for external-paper citations therefore had no applicable reference to query.

Ten sequential statement records and four reference records are saved in `memory/gauduchon_metric_geometry_01/`, together with the run metadata and channel records. All local deductions, including the short computations expanded above, pass. Critical errors: none. Gaps: none. Under the required strict decision rule the verdict is **correct**, and `repair_hints` is the empty string.
