**Verification report — quadratic_density_nonuniqueness_01**

**Verdict: correct.** The construction establishes the stated existence theorem. The sequential verification found no critical errors and no mathematical gaps. In particular, the density has exact quadratic zeros, while the singular scalar equation produces smooth solutions whose radial slopes vanish to infinite order at the interfaces.

This is a correctness verification, not a novelty certification. The submitted proof was checked in textual order. All new coefficients, positivity corrections, density formulas, ODE arguments, and global deductions were recomputed. No previous NUMA audit or other submitted new construction was used. Two independent supplementary reviews checked the ODE lemma and the geometry/final deductions; their conclusions agree with this verification. No numerical evidence was used, and the book was not edited.

The permitted inputs were the original rank-one frame and coordinate, its stated chain rule and Fubini–Study coefficients, smooth scalar ODE existence/uniqueness/compact continuous dependence/continuation, elementary calculus, Hermitian matrix positivity, and closed bounded Bedford–Taylor/Stokes. No finite-order uniqueness theorem or new PDE or literature premise was invoked.

**1. Target and source normalization**

The target requires one fixed smooth, strictly positive, nonclosed Hermitian form on \(\mathbb P^3\), bounded mass for its bounded plurisubharmonic class, a fixed smooth nonnegative density vanishing exactly quadratically along two disjoint smooth real hypersurfaces, and an uncountable family of distinct smooth solutions after supremum normalization.

The frame and derivative conventions were checked against [the specified source](/Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex:15), especially its original frame subsection. It uses

\[
r=\log\frac{|A|^2}{|B|^2},\qquad
P=dd^c\log|A|^2,\quad Q=dd^c\log|B|^2,\quad
R=dr\wedge d^cr.
\]

The source explains that its original \(2i\partial\bar\partial\) convention is converted to the book convention by dividing all relevant forms by \(4\pi\), without changing scalar functions. Thus the submitted identity is exact:

\[
dd^cG(r)=G'(r)(P-Q)+G''(r)R.
\]

There is no extra factor in either scalar derivative. With \(\sigma=e^r/(1+e^r)\), one has \(\sigma(-r)=1-\sigma(r)\) and \(\sigma'=e^r/(1+e^r)^2>0\), so the source Fubini–Study coefficients agree exactly with the submission.

The independent semipositive rank-one frame gives

\[
(xP+yQ+zR)^3=6xyz\,P\wedge Q\wedge R.
\]

For nonnegative coefficients, rank is the number of positive coefficients; all three positive coefficients give strict positivity. Also \(P,Q\) are closed and

\[
dR=-dr\wedge dd^cr=-dr\wedge(P-Q),
\quad
d(xP+yQ+zR)=dr\wedge((x'-z)P+(y'+z)Q).
\]

Finally, \(R\ne0\) implies \(dr\ne0\) throughout the frame domain \(U\). Consequently \(r=\pm1\) are disjoint regular levels. Their finite nonzero norm ratios keep them away from the omitted projective lines, so they are compact smooth real hypersurfaces.

**2. Cutoffs, coefficient zeros, and global smoothness**

The specified smooth plateau cutoffs exist by elementary smooth bump constructions. Neither monotonicity of \(a\) nor an additional sign restriction on \(\kappa\) is needed in the proof.

The polynomial \(p=(1-r^2)^2\) is nonnegative and vanishes only at \(\pm1\). Wherever \(\chi>0\), the strictly positive Fubini–Study contribution makes each horizontal coefficient positive. Wherever \(\chi=0\), a zero of \(x=p+a\) requires both \(p=0\) and \(a=0\). At \(-1\), \(a=1\); at \(1\), \(a=0\). Thus \(x\) vanishes exactly at \(1\). Reflection gives that \(y\) vanishes exactly at \(-1\).

The radial coefficient \(z=(1-\chi)+\chi\sigma'\) is strictly positive everywhere, being a convex combination of two positive numbers. On fixed neighborhoods of the interfaces, the plateaus give exactly

\[
(x,y,z)=(1+p,p,1)\quad\text{near }-1,
\qquad
(x,y,z)=(p,1+p,1)\quad\text{near }1.
\]

In particular, the interface triples are \((1,0,1)\) and \((0,1,1)\), each of rank two. The parity relations give \(y(r)=x(-r)\) and even \(z\).

For \(|r|\ge3/2\), the form is exactly \(\omega_X\). This equality on actual neighborhoods of the omitted lines proves the global smooth extension of \(\omega_0\). There is no need to extend the individual coefficient functions as scalar functions of a singular coordinate at those lines.

**3. Strict background correction and nonclosure**

The function \(\rho=\varepsilon(r^2-1)\kappa\) has compact support in the finite \(r\)-region and extends smoothly by zero at the projective ends. On \(|r|\le3/2\), its derivatives are exactly \(\rho'=2\varepsilon r\), \(\rho''=2\varepsilon\). The corrected coefficients are therefore precisely those stated.

For \(r>0\), \(x+2\varepsilon r>0\), including the former zero at \(r=1\); at \(r=0\), \(x=1\). On \([-3/2,0]\), let \(m=\min x>0\). Then

\[
x+2\varepsilon r\ge m-3\varepsilon>0
\]

for sufficiently small positive \(\varepsilon\). Because \(y(r)=x(-r)\), the same estimate proves \(y-2\varepsilon r>0\) on the entire central interval. Also \(z+2\varepsilon>0\).

On the compact annuli \(3/2\le|r|\le2\), the original coefficients are the positive Fubini–Study coefficients. Explicitly,

\[
\rho'=\varepsilon[2r\kappa+(r^2-1)\kappa'],\qquad
\rho''=\varepsilon[2\kappa+4r\kappa'+(r^2-1)\kappa''].
\]

Their absolute values are bounded by fixed constants times \(\varepsilon\). One further shrinking preserves all three positive coefficients there. Outside the support there is no correction. Hence one fixed sufficiently small \(\varepsilon>0\) produces a global smooth Hermitian background.

Since \(d(dd^c\rho)=0\), the correction does not affect nonclosure. At zero the cutoffs \(a,b,\chi\) are locally constant, \(p'(0)=0\), and \(z(0)=1\). Thus

\[
d\omega\big|_{r=0}=dr\wedge(Q-P)\ne0.
\]

The nonvanishing is certified by wedging with \(P\) and then \(d^cr\), which yields \(P\wedge Q\wedge R>0\). This excludes a possible cancellation of the displayed three-form.

**4. Fixed density and exact quadratic order**

Define \(g\) by the global quotient of the smooth top-degree forms \(\omega_0^3\) and \(\omega_X^3\); the latter is nowhere zero. This gives a smooth nonnegative function, equal to one near the projective ends. Its only zeros are the two checked coefficient zeros.

The common factor \(6PQR\) cancels, giving

\[
g=\frac{xyz}{D(r)},\qquad D(r)=\sigma(r)(1-\sigma(r))\sigma'(r)>0.
\]

Near either interface \(xyz=(1+p)p\). For \(r_0\in\{-1,1\}\), this gives the exact factorization

\[
g(r)=(r-r_0)^2 H_{r_0}(r),\qquad
H_{r_0}(r)=\frac{(1+p(r))(r+r_0)^2}{D(r)}.
\]

The second factor is smooth and strictly positive near \(r_0\), with \(H_{r_0}(r_0)=4/D(r_0)>0\). Since \(dr\ne0\), \(r-r_0\) is a defining function. In particular,

\[
\frac{d^2g}{dr^2}(r_0)=\frac8{D(r_0)}>0,
\]

so the order is exactly two, not infinite or merely bounded below by two. The baseline potential \(-\rho\) is global smooth and has solution form \(\omega_0\), hence already solves the prescribed equation.

**5. ODE domain, residuals, and barrier directions**

On \((-1,1)\), \(\chi=0\), \(p>0\), \(x,y>0\), and \(z=1\). Consequently the vector field is smooth on

\[
\mathcal D=\{(r,h):-1<r<1,\ -x(r)<h<y(r)\},
\]

and \(h=0\) is an exact solution. Fix any one \(c\in(0,1)\). The graph \(B=-cp\) lies inside this domain on both endpoint neighborhoods.

The relevant residual is \(F(r,B)-B'=F(r,-cp)+cp'\), not its negative. Direct substitution gives

\[
F(r,-cp)+cp'
=\frac{1+p}{(1+(1-c)p)(1+c)}-1+cp'
\longrightarrow-\frac{c}{1+c}
\]

on the left, and

\[
F(r,-cp)+cp'
=\frac{1+p}{(1-c)(1+(1+c)p)}-1+cp'
\longrightarrow\frac{c}{1-c}
\]

on the right. Here \(p'=-4r(1-r^2)\to0\). Both limits and their signs are correct.

At a contact with the barrier, \((h-B)'\) is negative on the left and positive on the right. The first sign prevents a crossing from above when time is followed backwards; the second prevents a crossing from above when time is followed forwards. Thus the stated backward left and forward right lower barriers have the correct directions. Strictness holds on fixed neighborhoods, chosen independently of the initial parameter.

**6. Common parameter interval and finite interior continuation**

Choose fixed \(\ell<0<t\) in the two barrier neighborhoods. The zero solution on \([\ell,t]\) is a compact graph inside \(\mathcal D\); its horizontal distance to the two forbidden boundaries has a positive lower bound. Choose a tube narrower than half that lower bound and also narrower than \(cp(\ell)\) and \(cp(t)\).

The permitted compact continuous-dependence theorem provides a single \(\eta_0>0\) such that every initial value \(h(0)=-\eta\), \(0<\eta<\eta_0\), gives a solution throughout \([\ell,t]\) inside that tube. In particular its values at both middle endpoints lie strictly above \(-cp\). Uniqueness prevents any interior contact with the zero solution, so \(h<0\) on its maximal interval.

The barrier argument then traps the solution as far as it exists into each endpoint neighborhood. The denominator factors satisfy, on the left,

\[
x+h\ge1+(1-c)p,\qquad y-h\ge p,
\]

and, on the right,

\[
x+h\ge(1-c)p,\qquad y-h\ge1+p.
\]

If a maximal endpoint lay strictly between \(-1\) and \(1\), \(p\) would remain bounded below by a positive number on a compact neighborhood of that endpoint. The trapped graph, including its closure, would then lie in a compact subset of the smooth ODE domain. Ordinary continuation rules out such an endpoint. This argument does not assume the desired existence up to the singular ends. It proves existence on the full interval, with the same \(c\), neighborhoods, middle interval, and \(\eta_0\) for the whole family.

**7. Exact logarithmic factorization and decay at both ends**

Expanding the denominator gives

\[
(x+h)(y-h)=xy+(y-x)h-h^2,
\]

so \(F=hL\) with exactly the stated \(L\). Because \(h<0\),

\[
(\log(-h))'=\frac{h'}h=L.
\]

On the left,

\[
L=\frac{1+h}{(1+p+h)(p-h)}\ge\frac{C_1}{p}>0.
\]

Indeed \(1+h\ge1-cp\ge1/2\) after shrinking, while the positive denominator is at most \((1+p)(1+c)p\). On the right,

\[
L=\frac{-1+h}{(p+h)(1+p-h)}\le-\frac{C_2}{p}<0.
\]

Here the numerator is at most \(-1\) and the denominator is at most \(p(1+(1+c)p)\). Using this upper denominator bound with the negative numerator gives precisely the claimed inequality direction.

The integrations are, explicitly,

\[
\log(-h(r))\le\log(-h(\ell))-C_1\int_r^\ell\frac{ds}{p(s)}
\quad (r<\ell),
\]

\[
\log(-h(r))\le\log(-h(t))-C_2\int_t^r\frac{ds}{p(s)}
\quad (r>t).
\]

Both are decay estimates. At either end set \(d=1-|r|\). Then \(p=d^2(2-d)^2\), in particular \(p\le4d^2\). Each relevant integral is bounded below by

\[
\frac14\left(\frac1d-\frac1{d_{\mathrm{anchor}}}\right).
\]

Taking a common positive \(A\), for example \(\min(C_1,C_2)/4\), and adjusting the multiplicative constant yields \(|h|\le C e^{-A/d}\) at both ends. Polynomial vanishing of \(p\) supplies the divergent reciprocal integral that produces the exponential estimate. Uniformity of the multiplicative constant in \(\eta\) is unnecessary for the claimed individual smoothness.

**8. Noncircular all-order estimates and smooth zero extension**

Near each endpoint the functions \(x,y\) are polynomials, \(z=1\), and \(h\) is bounded. The denominator factors of \(L\) are bounded below by \(1\) and \((1-c)p\), in the appropriate order. Repeated partial differentiation in \((r,h)\) therefore gives bounded numerators divided by finite powers of these factors. Every such partial derivative along the trapped graph has at most polynomial growth in \(d^{-1}\).

Assume the exponential-times-polynomial estimates through order \(j\). Leibniz differentiation gives

\[
h^{(j+1)}=\sum_{k=0}^j\binom jk h^{(k)}
\frac{d^{j-k}}{dr^{j-k}}[L(r,h(r))].
\]

Each composite derivative uses partial derivatives of \(L\) and derivatives of \(h\) of order at most \(j-k\le j\). Thus no unknown \(h^{(j+1)}\) occurs on the right. Discarding exponential factors within the composite gives a polynomial bound for that factor. The explicit \(h^{(k)}\) outside it retains \(e^{-A/d}\). Consequently the next estimate holds with the same positive \(A\) and possibly a larger finite inverse power of \(d\).

This proves the induction without circularity or loss of the exponential factor. Every derivative tends to zero; moreover \(h^{(j)}/d\to0\). Extending the derivatives by zero therefore gives continuous functions whose endpoint difference quotients are zero. Applying this at every order proves that the zero extension is smooth and flat at both endpoints.

**9. Global primitives, rank-two gluing, and one fixed equation**

The smooth zero extension of \(h_\eta\) has support in \([-1,1]\). A primitive \(G_\eta\) is smooth and constant separately on \(( -\infty,-1]\) and \([1,\infty)\). The two constants need not agree. Each omitted projective line has a neighborhood on which the corresponding primitive is constant, which proves its global smooth extension.

For \(u_\eta=G_\eta-\rho\), the exact chain rule gives the claimed three coefficients. Inside the band the first two are positive, and the ODE gives

\[
z+h_\eta'=\frac{xyz}{(x+h_\eta)(y-h_\eta)}>0.
\]

Their product is \(xyz\), so the cube is \(\omega_0^3\). Outside the band \(h_\eta=h_\eta'=0\), giving \(\omega_0\) itself. The same equality holds at the interfaces by flatness. The glued form is smooth and semipositive, and its interface ranks are exactly two. No division at an interface is needed: the interior identity extends there as an equality of smooth forms.

The choices of \(\omega\), \(\rho\), and \(g\) precede the parameter \(\eta\) and are fixed. Hence every member solves exactly the same equation globally.

**10. Normalized injection**

Each smooth potential on the compact manifold has a finite supremum. Subtracting it preserves smoothness, its Hessian, semipositivity, and the equation. If two normalized potentials agreed, their unnormalized versions would differ by a constant. Differentiation on an \(r\)-transverse curve at \(r=0\) would give

\[
h_\eta(0)=h_\theta(0),\qquad -\eta=-\theta.
\]

Thus the family remains injectively parametrized by the uncountable interval \((0,\eta_0)\) after normalization. No parameter regularity of the supremum is required.

**11. Bounded mass for the entire bounded class**

Compactness gives a finite \(C\) with \(B=C\omega_X-\omega\ge0\). For any bounded \(\omega\)-psh potential \(v\), set

\[
T=\omega+dd^cv\ge0,\qquad S=C\omega_X+dd^cv=T+B\ge0.
\]

The form/current \(S\) is closed positive with locally bounded plurisubharmonic potentials. The positive mixed expansion gives \(T^3\le S^3\). To check the bounded version within the permitted tools, convolve \(S\) and the smooth form \(B\) locally with the same standard kernel. Then \(T_\epsilon=S_\epsilon-B_\epsilon\) is the convolution of the positive current \(T\), and \(B_\epsilon\ge0\). The smooth positive mixed expansion gives \(T_\epsilon^3\le S_\epsilon^3\).

Closed Bedford–Taylor convergence for powers of \(S_\epsilon\), together with smooth convergence of \(B_\epsilon\), passes this inequality to the bounded products, using the expansion of \((S-B)^3\). Closed bounded Stokes applies to \(S\) and gives

\[
0\le\int_X(\omega+dd^cv)^3
\le\int_X(C\omega_X+dd^cv)^3
=C^3\int_X\omega_X^3.
\]

This bound is independent of \(v\). The final sentence of the submitted proof therefore establishes BMP for the full bounded class, not just for its constructed smooth solutions. Stokes is applied to the closed comparison form, not directly as a closed-form identity for \(\omega\). No earlier construction is needed for this deduction.

**12. Closing observations and terminology**

There are exactly three positive-density components: the lower region with its projective end, the middle band, and the upper region with its projective end. For a fixed finite \(r\), representatives with fixed positive norms give a quotient of \(S^3\times S^3\) by diagonal \(S^1\), hence a connected level. Varying the norm ratio in any interval preserves connectedness, and adding the limiting line to each outer region preserves it. The proof makes no claim about connected positive-density sets.

One wording clarification is appropriate. The precise zero-jet flat functions are \(h_\eta\), their differences, and the primitive differences after subtraction of their respective constant interface values. A potential difference has all positive-order derivatives zero at each interface, but its values at the two interfaces need not agree. Indeed, ODE uniqueness orders different slopes throughout the band, so their difference has a nonzero integral between the ends. One global additive constant generally cannot make that potential difference vanish at both interfaces.

Thus the prose about “flat differences of potentials” is understood as flatness relative to the constant value at each interface. This is consistent with the proof's explicit use of primitives constant separately at the two ends. The theorem and all gluing deductions require only the flatness actually proved; none assumes zero potential values at both interfaces. This is a terminology clarification, not a mathematical gap in the construction.

**13. Reference checks and strict aggregation**

The internal frame reference matches the specified source exactly, including the derivative normalization. The phrases comparing the correction and bounded-mass argument with earlier work were checked directly from their present formulas; they supply no unverified premise. The standard ODE and closed bounded Bedford–Taylor/Stokes facts are expressly permitted inputs, and their hypotheses were checked at each use.

There is no cited external-paper theorem in the submitted argument requiring an arXiv theorem search or subsequent web fallback. No literature statement was imported. All allowed assumptions have a verified role, and no suspiciously unused hypothesis hides a missing argument.

The run contains 13 ordered statement-check records and three reference-check records. Two initial statement-memory writes reported tool errors and were successfully replayed; their explicit `order` fields preserve the logical textual order. A later reference-memory query timed out in automatic permission review; the already saved reference records were read locally and remain complete. These are persistence/query events, not mathematical findings.

Critical errors: none. Mathematical gaps: none. Under the required strict rule, the verdict is **correct**, and `repair_hints` is the empty string.
