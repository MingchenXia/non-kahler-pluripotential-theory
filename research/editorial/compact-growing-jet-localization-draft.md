# Compact-curve localization with growing vanishing orders

Status: Historical lower-bound derivation, integrated at checkpoint97. The complete upper/lower proof passed the bounded Rethlas audit `compact_growing_jets_01` and is Theorem 27.13.1. The text below preserves its draft wording; use the book for the final formulation. The frozen audit input is unchanged. See `compact-growing-jets-energy-review-97.md` for exact scope and classical inputs. No novelty claim.

## Statement and inputs

Let C be a connected compact Riemann surface, x a point, and (L,h) a smooth Hermitian holomorphic line bundle. Its normalized curvature is semipositive everywhere and strictly positive on C minus x. In a coordinate z centered at x and holomorphic frame e, assume |e|_h^2=exp(-phi(z)), where phi(z)=|z|^(2r)+O(|z|^(2r+1)) for a fixed integer r>=1. Let nu be a smooth positive volume form, locally a(z)dA with a(0)=1. For integers m>=1 and q=q_m tending to infinity with q_m=o(m^(1/(2r+1))), give V_m=H^0(C,L^m tensor m_x^q) the norm integral |s|_(h^m)^2 dnu. Let B_m be its Bergman density, with value zero if V_m=0. For fixed real tau and points z_m satisfying T_m=m|z_m|^(2r)=q/r+tau sqrt(q/r), the proposed conclusion is

$$\frac{\pi B_m(z_m)}{mr^2|z_m|^{2r-2}}\longrightarrow\Phi(\tau).$$

Here m_x is the ideal of x, dA is Euclidean area, and Phi is the standard Gaussian distribution function. The earlier local argument proves the limsup bound and, as an intermediate conclusion, the same Gaussian limit for the radial kernel on discs of radius A(q/(rm))^(1/(2r)) for each fixed A>1. That complete proof is supplied as Part I in the audit input; it is not assumed independently verified. This Part II proves the liminf.

The exact full-plane norms J_(m,k)=(pi/r)m^(-(k+1)/r)Gamma((k+1)/r), the vanishing-order-uniform Poisson comparison and the full-plane Gaussian transition are the already reviewed Section 27.12 inputs. In particular, if K_m/q_m tends to a fixed number c>1, then B_(m,r)^(K_m+1)(z_m)/S_m tends to zero, where S_m=mr^2|z_m|^(2r-2)/pi. This follows because every residue-class Poisson threshold divided by T_m tends to c>1 and the comparison error tends to zero.

The classical analytic input is the smooth complete-Kähler L2 theorem (Demailly, Analytic Methods in Algebraic Geometry, Theorem 5.1, pages 33–34 of the July 2011 text; the primary statement and proof have been checked): if a Hermitian holomorphic line bundle E has iTheta(E)>=omega on a complete Kähler curve (C,omega), then every E-valued (1,1)-form f with finite L2 norm has an E-valued (1,0)-form u solving dbar u=f with ||u||^2<=||f||^2. We will apply it only to smooth metrics on the compact curve and prove the singular limit below. The exact normalization is immaterial for the argument: multiplying a fixed auxiliary weight supplies the displayed lower curvature bound. A section-valued (0,1)-form is converted to an E=L^m tensor K_C^(-1)-valued (1,1)-form using the canonical identification; the induced metric preserves norms. Thus the curvature of K_C^(-1) must be included. All form norms and this canonical metric are induced by omega=nu, which is Kähler in dimension one.

## Finite model polynomials

Fix c>1 and K_m=floor(cq_m). For brevity write q=q_m, K=K_m, R_m=(q/(rm))^(1/(2r)), and rho_m=|z_m|. Define the positive number

$$C_m=\sum_{k=q}^{K}\frac{|z_m|^{2k}}{J_{m,k}},\qquad
p_m(z)=C_m^{-1/2}\sum_{k=q}^{K}\frac{\overline{z_m}^{k}z^k}{J_{m,k}}.$$

For all large m, z_m is nonzero and K>=q, so C_m>0. Orthogonality gives ||p_m||_(m,r)=1, and

$$e^{-T_m}|p_m(z_m)|^2
=B_{m,r}^{(q)}(z_m)-B_{m,r}^{(K+1)}(z_m)
=(\Phi(\tau)+o(1))S_m.$$

The phase of the point z_m is arbitrary. All norm estimates below are independent of that phase.

Choose a coordinate disc |z|<delta<1/2 on which phi(z)>=(1-epsilon)|z|^(2r), with a fixed 0<epsilon<1/2, and a(z) bounded above. We claim that for a sufficiently large fixed A>1,

$$\int_{A R_m<|z|<\delta}|p_m|^2e^{-m\phi}a\,dA=o(1).$$

To prove this, write p_m=sum_(k=q)^K b_(m,k)z^k, so sum |b_(m,k)|^2 J_(m,k)=1. Put beta=1-epsilon. Radial domination, angular orthogonality and polar integration give an upper bound by a fixed constant times

$$\sum_{k=q}^{K}|b_{m,k}|^2J_{m,k}\,
\beta^{-(k+1)/r}
\mathbb P\{G_{(k+1)/r}\geq\beta A^{2r}q/r\},$$

where G_b is the Gamma variable with density t^(b-1)e^(-t)/Gamma(b). Its moment E exp(G_b/2)=2^b yields

$$\beta^{-b}\mathbb P\{G_b\geq U\}
\leq\exp[-U/2+b\log(2/\beta)].$$

For q<=k<=K, b<=(cq+1)/r. Choose A so that beta A^(2r)/2>c log(2/beta)+1. The preceding bound is O(exp(-q/r)), uniformly in k. This proves the claim. Inside |z|<=A R_m, m|phi-|z|^(2r)|=o(1) and a=1+o(1) uniformly, by the assumed growth range. Consequently any fixed smooth cutoff chi with 0<=chi<=1, support inside |z|<delta, and chi=1 on a smaller neighborhood of zero, satisfies

$$\|\chi p_m e^{\otimes m}\|_{h^m,\nu}^2\leq1+o(1).$$

The cutoff section is extended by zero to C. The constants delta, epsilon, A and chi are fixed before m tends to infinity. Their allowed dependence is on the fixed geometric data, r and c; the convergence estimates may also depend on tau, never on k or the phase of z_m.

## A correction preserving the growing vanishing order

Set f_m=dbar(chi p_m e^(tensor m)), supported in a fixed closed annulus away from zero. On that annulus phi is bounded below by a fixed positive number. The normalized coefficient identity above and Cauchy--Schwarz give, on |z|<delta<1,

$$|p_m(z)|^2\leq\sum_{k=q}^{K}\frac{|z|^{2k}}{J_{m,k}}
\leq C(K+1)m^{(K+1)/r}.$$

Indeed Gamma(b) has a positive lower bound on b>=1/r. Since q log m=o(m), the exponential decay exp(-m phi) dominates this coefficient bound on the fixed annulus.

We need the same conclusion after imposing logarithmic integrability at x. Choose a smooth cutoff eta supported in the coordinate disc and equal to one on a neighborhood of x. Require 0<=eta<=1 and choose t_0>0 small enough that |z|^2+t_0^2<1 throughout its support. For 0<t<=t_0 define a global smooth function

$$\ell_t(z)=\eta(z)\log(|z|^2+t^2),$$

extended by zero off the coordinate disc. It is nonpositive. Near x its dd^c is nonnegative; on the fixed transition annulus its derivatives are uniformly bounded as t decreases to zero. Therefore dd^c ell_t>=-C_0 omega globally, with all its negative part confined to a fixed compact subset of C minus x.

Choose a fixed smooth real function psi equal to a sufficiently large positive multiple of |z|^2 near x and cut off in the coordinate chart. It can be chosen so that

$$i\Theta(K_C^{-1})+i\partial\bar\partial\psi\geq2\omega$$

on a fixed neighborhood of x where eta=1. On the complement, the curvature iTheta(L,h) has a fixed positive lower bound relative to omega. Since q=o(m), for all sufficiently large m and every 0<t<=t_0 the smooth metric

$$H_{m,t}=h^m\otimes h_{K_C^{-1}}\,e^{-\psi-q\ell_t}
\quad\hbox{on }E_m=L^m\otimes K_C^{-1}$$

satisfies iTheta(E_m,H_(m,t))>=omega. This follows by adding the four curvature terms: m iTheta(L,h), iTheta(K_C^(-1)), i partial barpartial psi and q i partial barpartial ell_t. Near x the first and fourth are nonnegative and the middle two dominate 2omega; away from x the first term absorbs the O(q)+O(1) negative bound. Compactness supplies uniform constants. No inverse of the degenerate curvature of h is taken.

On the support of f_m, ell_t is bounded below uniformly in t, so exp(-q ell_t)<=exp(C_1q). The fixed derivatives of chi, metric comparisons and the polynomial estimate thus show that for some a_0>0, independent of m and t,

$$\int_C |f_m|_{h^m,\omega}^2e^{-\psi-q\ell_t}\,\nu
\leq e^{-a_0m}$$

for all large m. The bidegree-converted data are automatically dbar-closed on a curve. The smooth complete-Kähler L2 theorem gives a section-valued weak solution u_(m,t) to dbar u_(m,t)=f_m with the same weighted bound (or a fixed multiple, absorbed by reducing a_0).

For each fixed m, let t decrease to zero. Since ell_t<=0 and psi is fixed bounded, the solutions are bounded in the original L2 norm. Take a weakly convergent subsequence with limit u_m. Distributional continuity gives dbar u_m=f_m. For a fixed t'>0 and t<t', one has ell_t<=ell_(t'), hence the same bound holds in the smooth weighted space with weight exp(-psi-q ell_(t')). Weak lower semicontinuity in this fixed equivalent Hilbert norm, followed by monotone convergence as t' decreases to zero, gives

$$\int_C |u_m|_{h^m}^2e^{-\psi-q\ell}\,\nu\leq e^{-a_0m},
\qquad \ell=\eta\log|z|^2.$$

In particular ||u_m||_(h^m,nu)^2<=C exp(-a_0m). Near x, f_m=0, so the distributional Cauchy--Riemann equation makes u_m holomorphic in the frame. Its weighted integrability against |z|^(-2q) implies vanishing order at least q: a holomorphic function of order j has finite such integral exactly when j-q>-1, equivalently j>=q for integers. The smooth factors in the integrand are bounded above and below near x for each fixed m. Thus the global holomorphic section

$$s_m=\chi p_m e^{\otimes m}-u_m$$

belongs to V_m and satisfies ||s_m||<=1+o(1).

## Pointwise comparison and conclusion

For all large m the shrinking disc |z|<A R_m lies where chi=1 and f_m=0. The function representing u_m there is holomorphic and vanishes to order at least q. Local comparison of actual and radial norms and pointwise weights, followed by the disc kernel estimate from Part I, gives

$$|u_m(z_m)|_{h^m}^2
\leq(1+o(1))B^{D_m}_{m,r,q}(z_m)
             \|u_m\|_{h^m,\nu}^2
\leq C S_m e^{-a_0m}.$$

Here D_m is the shrinking disc from Part I. Since the actual pointwise metric factor differs from exp(-T_m) by 1+o(1), the polynomial calculation and the triangle inequality imply

$$|s_m(z_m)|_{h^m}^2\geq(\Phi(\tau)+o(1))S_m.$$

The number Phi(tau) is strictly positive for every fixed real tau. The extremal characterization of B_m and ||s_m||<=1+o(1) give liminf B_m(z_m)/S_m>=Phi(tau). Part I gives the reverse limsup, proving the proposed limit. In particular the constructed s_m is nonzero for large m. This proves only the stated small-growth range; it does not settle larger growing orders, uniformity over unbounded tau, or higher-dimensional non-Kähler localization.
