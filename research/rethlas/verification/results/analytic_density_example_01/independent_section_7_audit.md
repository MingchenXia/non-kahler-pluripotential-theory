# Independent audit of section 7

Run: `analytic_density_example_01`. This supporting audit follows the supplied section 7 in textual order. It uses the displayed convention for `dd^c`, elementary calculations and the stated definitions, and does not assume any theorem from sections 1–6 or any previous construction. No critical error or substantive gap was found in this section.

## 1. Rank-one projective frame and differential identities

On a block chart with \(Z_1W_1\ne0\), take holomorphic coordinates

\[
\zeta=Z_2/Z_1,\qquad \xi=W_2/W_1,\qquad \lambda=Z_1/W_1\ne0.
\]

Then

\[
r=\log|\lambda|^2+\log(1+|\zeta|^2)-\log(1+|\xi|^2),
\quad P=dd^c\log(1+|\zeta|^2),\quad Q=dd^c\log(1+|\xi|^2).
\]

The positive rank-one forms \(P,Q\) use independent covectors \(d\zeta,d\xi\), while \(\partial r\) has nonzero \(d\lambda/\lambda\) component. In the manuscript's normalization,

\[
R=dr\wedge d^cr=\frac{i}{2\pi}\partial r\wedge\bar\partial r.
\]

Thus \(P,Q,R\) form an independent positive rank-one frame, their squares vanish, and \(PQR>0\). The cube of a diagonal linear combination is \(6xyzPQR\), and coefficient nonnegativity/positivity is precisely equivalent to semipositivity/positivity.

The chain rule gives \(dd^cG(r)=G'(P-Q)+G''R\). Writing a local Fubini–Study potential as \(\log|W|^2+\log(1+e^r)\) gives

\[
\Omega=\sigma P+(1-\sigma)Q+\sigma'R,
\qquad \Omega^3=6(\sigma')^2PQR.
\]

Finally \(dP=dQ=0\) and \(dR=-dr\wedge(P-Q)\), proving the displayed formula for \(d(xP+yQ+zR)\), including both signs.

## 2. Prescribed determinant and divided differences

The integral formulas for \(k_-,k_+\) are smooth and strictly positive for every finite real \(r\), since \(\sigma'>0\). The fundamental theorem of calculus gives both divided-difference identities, even at \(r=\pm1\). Consequently

\[
d_*=f_*(\sigma)(\sigma')^2=(1-r^2)^2H_*^2,
\qquad H_*=k_-k_+\sigma'>0.
\]

The identities \(b=1-a\) and \(\sigma(-r)=1-\sigma(r)\) make \(d_*\) even. Positivity makes \(H_*\) the unique positive square root of \(d_* /(1-r^2)^2\) away from the endpoints, so it is even there and, by continuity, at the endpoints too.

The flat bump is smooth globally; differentiating on its support gives
\(q=-2rp/(1-r^2)^2\). The exponential dominates every inverse power near each endpoint, so \(p,q\) and their relevant derivatives extend by zero smoothly.

## 3. Both radicands and positivity

The first radicand \(q^2+2H_*^2\) is strictly positive everywhere, hence \(z_b\) is smooth and \(z_b>|q|\). The second radicand is

\[
r^2+4p^2+2z_b(1-r^2)^2.
\]

For \(r\ne0\), its first term is positive; at \(r=0\), \(p(0)=e^{-1}>0\). Thus the second square root is also a single smooth positive function everywhere, including both endpoints.

Direct multiplication yields

\[
x_b-y_b=-r,\qquad x_by_b=p^2+\tfrac12z_b(1-r^2)^2.
\]

Since \(S_*\ge|r|\), the two coefficients are nonnegative. Equality occurs only at \(r=\pm1\), where their values are respectively \((1,0)\) and \((0,1)\). Elsewhere both are positive. On the band \(|r|<1\),

\[
S_*^2-(2p+|r|)^2
=2z_b(1-r^2)^2-4p|r|
=2(1-r^2)^2(z_b-|q|)>0.
\]

This proves \(x_b>p,y_b>p\), while \(z_b>|q|\) proves positivity of every coefficient of both perturbed triples. At the endpoints, \(p=q=0\), and each triple has exactly one zero coefficient and two positive coefficients.

## 4. Determinant cancellation

For \(D=x_by_b-p^2\) and \(E=p(x_b-y_b)=-rp\), one has

\[
D=\tfrac12z_b(1-r^2)^2,\qquad qD=z_bE.
\]

The transverse coefficient products are exactly \(D+E\) and \(D-E\). Therefore

\[
(D+E)(z_b-q)=(D-E)(z_b+q)
=Dz_b-Eq
=\frac D{z_b}(z_b^2-q^2)
=(1-r^2)^2H_*^2=d_*.
\]

Division by \(z_b\) is safe everywhere. On the tails \(p=q=0\), the same equality follows directly from the formulas. At the endpoints both sides vanish. There is no missing factor of two, wedge-factorial, or normalization constant: the factor six matches that of \(\Omega^3\).

## 5. Global smooth patch and projective extension

A smooth even cutoff with the specified nested plateaux exists. In the outer region \(|r|>5/4\), the prescribed density, both baseline horizontal coefficients, and the comparison coefficients are strictly positive. Their convex combinations \(x,y\) are strictly positive, and \(z=d_* /(xy)\) is smooth positive.

On the overlap \(5/4<|r|<3/2\), the cutoff equals one and \(p=q=0\); hence \(z=z_b\) exactly, so all derivatives agree automatically. On \(|r|\ge2\),

\[
xy=\kappa^2\sigma',\qquad z=\frac{f_*(\sigma)(\sigma')^2}{\kappa^2\sigma'}=\kappa\sigma'.
\]

Thus the patched form is exactly \(f_*(t)^{1/3}\Omega\) in neighborhoods of the two omitted projective lines. Since \(f_*(0)=f_*(1)=a^2b^2>0\), this is smooth and positive across those lines. A cube root is never taken across a zero of the density in this patch.

The potential \(F=2\int_0^r p\) is constant on each tail, so it too extends smoothly across both lines. It is nonconstant because \(F'=2p>0\) on the middle band. Its half-Hessian is exactly \(p(P-Q)+qR\). This proves the equality of the two global top powers, their rank-two degeneracies, and positivity elsewhere. Evenness of all required ingredients gives \(x(-r)=y(r)\) and \(z(-r)=z(r)\).

## 6. Positive correction and nonclosedness

The correction potential \(h=(r^2-1)\eta\) has compact support in the block set, so extension by zero is smooth. In the central region, \(h'=2r\), \(h''=2\). For \(0\le r\le3/2\), \(x+2\varepsilon r>0\): at \(r=0\), \(x>0\); for \(r>0\) the added term is positive, including the sole zero \(r=1\). On the other half-interval, \(x\) has a positive minimum and the negative correction has magnitude at most \(3\varepsilon\). The stated restriction on \(\varepsilon\) therefore suffices. Reflection proves the second coefficient positive, and the radial coefficient is \(z+2\varepsilon>0\).

All baseline coefficients have a strictly positive minimum on the compact transition annuli. The stated bound involving \(m_1\) and \(M_1\) preserves positivity there. Beyond the support the background is already positive. Thus there is a single strictly positive \(\varepsilon\) satisfying every requirement, and the global corrected background is smooth positive.

The correction is \(dd^c\)-exact, so it does not change \(d\omega\). At \(r=0\), evenness of \(S_*\) gives \(x'=-1/2\), \(y'=1/2\), and hence

\[
d\omega=(z_b(0)+1/2)dr\wedge(Q-P).
\]

This form is nonzero: its wedge with \(P\) and \(d^cr\) is the nonzero top form \(PQR\), up to a nonzero scalar. The local evaluation lies entirely inside the baseline region, so no cutoff term enters it.

The potentials \(-F/2-\rho\) and \(F/2-\rho\) cancel the correction exactly, leaving the two verified semipositive solution forms. Subtracting their respective suprema changes neither Hessian and cannot turn their nonconstant difference \(-F\) into a constant.

## 7. Analytic zeros and higher-dimensional normalization

The projective function \(t\) is globally real analytic, and its only density zeros occur at the two distinct interior values \(a,b\). The block-frame computation proves \(dr\ne0\), and \(dt=\sigma' dr\ne0\), so the two levels are regular real analytic hypersurfaces. Their description as \((S^3\times S^3)/S^1\) proves connectedness; they are compact and have zero smooth volume. At each level the other density factor stays nonzero, giving a strictly positive smooth factor times the square of a transverse coordinate.

On the product of dimensions \(3\) and \(n-3\), positivity is the direct-sum positivity of the two factors. In an \(n\)-fold top power, all terms except the term with three factors from the first component vanish by dimension. The factor \(\binom n3\) occurs in both the solution volume and \(\Omega_n^n\), so the prescribed density is exactly the pullback of \(f_*\), with no extra factor. The singular rank is \(2+(n-3)=n-1\). Supremum normalization, distinctness, analyticity, and connectedness of the product hypersurfaces persist. Pullback to a slice detects the original nonzero \(d\omega\), proving nonclosedness.

## 8. Sublevels, inverse powers, and the closing remark

Near either compact hypersurface, \(c s^2\le f_*\le C s^2\) in a real transverse coordinate, with smooth volume uniformly comparable to product coordinate volume. A finite tubular cover gives the upper sublevel bound \(O(\sqrt\tau)\); any nonempty chart on one hypersurface gives a matching lower bound. Outside these neighborhoods the density has a positive minimum. Thus \(\operatorname{Vol}\{f_*\le\tau\}\asymp\sqrt\tau\).

The same coordinates reduce integrability to \(\int_0^\delta s^{-2\alpha}\,ds\), finite exactly when \(\alpha<1/2\). This proves both directions, including divergence at the endpoint. Smooth positive changes of reference volume and the compact product factor do not change the conclusion.

The middle band has connected fibers over an interval and is connected. Each outer region is connected and includes its limiting projective line; scaling the vanishing block to zero also gives a direct deformation into that line. These give exactly three components of \(U\). For smooth coefficients, local uniform positivity of \(A+B\) agrees with pointwise positive definiteness. Since \(A+B=2\omega_0\), its positivity locus is exactly \(U\); at a zero level, continuity rules out even an almost-everywhere uniform lower bound in a neighborhood. The outer component closures lie in \(t\le a\) and \(t\ge b\), respectively, and are disjoint. Because \(F\) is strictly increasing in the middle and constant on the tails, the potential difference attains its two extremes on the opposite outer regions. These assertions are checked directly, without invoking the positive uniqueness results.

## Conclusion

The entire section 7 construction, its product normalization, the sharpness claims, and the final geometric remark pass this independent audit. This note does not audit any section 8 external statement; that requires the separate primary-source reference check.
