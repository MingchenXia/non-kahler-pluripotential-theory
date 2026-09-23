# A possible local upper bound for growing jet constraints

Status: research draft, 24 September 2026. Directly derived and reread, but not independently audited and not integrated into the book. No novelty claim. The full compact-curve localization problem remains open in the manuscript. This note uses the exact model statements in Section 27.12; the two associated Rethlas reports concern that model and its endpoint correction, not the new argument below.

## Setting and proposed conclusion

Let C be a compact Riemann surface, x a point of C, and (L,h) a smooth Hermitian holomorphic line bundle. Choose a holomorphic coordinate z centered at x and a holomorphic frame e on a neighborhood. Fix an integer r>=1 and suppose that |e|_h^2=exp(-phi), where

$$\phi(z)=|z|^{2r}+O(|z|^{2r+1}).$$

Let nu be a smooth positive volume form, locally a(z)dA with a(0)=1 and dA Euclidean area. For positive integers m, let q_m be nonnegative integers tending to infinity with q_m=o(m^(1/(2r+1))). Give V_m=H^0(C,L^m tensor m_x^(q_m)) the global norm integral |s|_(h^m)^2 dnu. Its density B_m is the sum of squared pointwise norms over an orthonormal basis, or zero for the zero space. Here m_x is the ideal sheaf of x.

Fix a real tau and points x_m with coordinates z_m satisfying

$$T_m:=m|z_m|^{2r}=q_m/r+\tau\sqrt{q_m/r}.$$

The proposed one-sided assertion is

$$\limsup_{m\to\infty}\frac{\pi B_m(x_m)}{mr^2|z_m|^{2r-2}}\leq\Phi(\tau),$$

where Phi is the Gaussian distribution function. Curvature positivity away from x is not used in the argument below; it remains part of the book's full localization question. No lower bound or supply of global sections is claimed.

## A truncated model calculation

Fix a real A>1, set R_m=(q_m/(rm))^(1/(2r)), and let D_m be the disc |z|<A R_m. Its radius tends to zero. On this disc,

$$m|\phi(z)-|z|^{2r}|\leq C_A mR_m^{2r+1}=C_Aq_mR_m/r\longrightarrow0.$$

Indeed q_m R_m is a fixed r-dependent factor times (q_m^(2r+1)/m)^(1/(2r)). Also sup_(D_m)|a-1| tends to zero. Thus the actual local scalar norm and the norm with weight exp(-m|z|^(2r))dA differ multiplicatively by 1+o(1), uniformly over all holomorphic functions on D_m. Their pointwise weights at z_m have the same comparison. The points z_m lie in D_m for large m because |z_m|/R_m tends to one.

Write U_m=m(A R_m)^(2r). For each integer k>=0, the squared monomial norm in the radial disc model is

$$I_{m,k}=\frac\pi r m^{-(k+1)/r}\gamma((k+1)/r,U_m),\qquad
\gamma(b,U)=\int_0^U t^{b-1}e^{-t}\,\mathrm{d}t.$$

The full-plane monomial norm is

$$J_{m,k}=\frac\pi r m^{-(k+1)/r}\Gamma((k+1)/r).$$

Angular Parseval and Tonelli show that these monomials are complete in the weighted holomorphic disc space. Consequently the disc kernel selected by vanishing order q_m has density

$$B^{D_m}_{m,r,q_m}(z_m)=e^{-T_m}\sum_{k\geq q_m}\frac{|z_m|^{2k}}{I_{m,k}}.$$

We compare this density with the full-plane selected density B_(m,r)^(q_m)(z_m) from Section 27.12. Put S_m=mr^2|z_m|^(2r-2)/pi. Since U_m/T_m tends to A^(2r), choose fixed real numbers 1<c<d<A^(2r) and set k_m=floor(rcT_m). For large m one has U_m>=dT_m and k_m>=q_m.

Uniformly for 0<=k<=k_m+1, one has

$$\frac{I_{m,k}}{J_{m,k}}=1+O(e^{-\eta T_m})$$

for some fixed eta>0. To see this, let b=(k+1)/r. The normalized Gamma density t^(b-1)e^(-t)/Gamma(b) has exponential moment (1-s)^(-b) for 0<s<1, by a change of variable in its integral. Hence

$$1-\frac{\gamma(b,U_m)}{\Gamma(b)}
\leq e^{-sU_m}(1-s)^{-b}.$$

Here b<=cT_m+O_r(1). Choose s>0 sufficiently small that sd+c log(1-s)>0, which is possible since d>c. The last upper bound is at most a fixed constant times exp(-eta T_m). This proves the uniform comparison.

For the remaining degrees, Cauchy--Schwarz for the positive radial measure gives

$$I_{m,k+1}^2\leq I_{m,k}I_{m,k+2}.$$

Thus the ratios I_(m,k+1)/I_(m,k) are increasing in k. At k=k_m, the preceding Gamma comparison and the fixed-shift Gamma-ratio asymptotic imply

$$\frac{|z_m|^2 I_{m,k_m}}{I_{m,k_m+1}}
=(1+o(1))\,m^{1/r}|z_m|^2
 \frac{\Gamma((k_m+1)/r)}{\Gamma((k_m+2)/r)}
\longrightarrow c^{-1/r}<1.$$

Choose a fixed number kappa with c^(-1/r)<kappa<1. For all sufficiently large m and every k>=k_m, the ratio between the consecutive summands |z_m|^(2k)/I_(m,k) is at most kappa. It follows that

$$e^{-T_m}\sum_{k>k_m}\frac{|z_m|^{2k}}{I_{m,k}}
\leq\frac{\kappa}{1-\kappa}
 e^{-T_m}\frac{|z_m|^{2k_m}}{I_{m,k_m}}.$$

The right side is o(S_m). Indeed I_(m,k_m)/J_(m,k_m) tends to one, while its full-plane single monomial is bounded by the full-plane density selected at order k_m. In the uniform Poisson comparison of Section 27.12, every residue threshold for k_m, divided by T_m, tends to c>1. Chebyshev makes all these upper tails tend to zero, and the comparison error is O(T_m^(-1/2)). The full-plane selected density at k_m is therefore o(S_m).

For q_m<=k<=k_m, use the uniform I/J comparison. Since I_(m,k)<=J_(m,k), this proves

$$B_{m,r}^{(q_m)}(z_m)
\leq B^{D_m}_{m,r,q_m}(z_m)
\leq (1+o(1))B_{m,r}^{(q_m)}(z_m)+o(S_m).$$

The full-plane Gaussian transition theorem gives B_(m,r)^(q_m)(z_m)/S_m -> Phi(tau). The same limit follows for the selected radial disc kernel.

## Restriction of global sections

In the frame e, the restriction of a global selected section to D_m is a holomorphic function vanishing to order at least q_m. Its global norm is at least its actual local norm on D_m, hence at least (1-o(1)) times its radial model norm. The extremal characterization of a reproducing kernel therefore gives

$$B_m(x_m)\leq(1+o(1))B^{D_m}_{m,r,q_m}(z_m).$$

The extra factor includes the comparison of the actual pointwise metric weight with the radial weight at z_m. All multiplicative errors are uniform over the restricted sections, so taking the supremum does not change them. The proposed limsup estimate follows. This argument also covers zero global spaces.

## Remaining proof boundary

The argument above needs a separate audit, including completeness for the varying disc space, uniform Gamma tail constants, the direction of the kernel comparison and every moving-scale error. It appears to establish the upper half of the proposed transition under purely local metric control. It does not establish the matching lower half: that requires a global section with prescribed jets and a norm estimate uniform in q_m. A fixed-order peak-section theorem or a fixed-size jet Gram matrix cannot be substituted for such a uniform construction.
