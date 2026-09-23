Run_id: compact_growing_jets_01

Statement: Verify the proposed compact-curve Gaussian localization theorem with q_m tending to infinity and q_m=o(m^(1/(2r+1))), with local weight |z|^(2r)+O(|z|^(2r+1)), and a globally semipositive smooth metric strictly positive off the one point. Check the entire local upper proof in Part I and global lower proof in Part II, in logical order. Neither is assumed correct. This is a research draft not yet adopted in the book, without a novelty claim.

Accepted inputs: elementary complex analysis, Hilbert-space facts, weak L2 compactness, Gamma/Stirling asymptotics, probability inequalities, and the exact weighted entire-function model in the appended book Section 27.12 (the two preserved reports degenerate_selected_kernel_01 and degenerate_selected_kernel_repair_01 must be read together; the sole r=1 endpoint issue is corrected in the appended text). The smooth complete-Kähler L2 theorem may be treated as a classical reference, but verify its precise bidegree, curvature-operator hypotheses and application to L^m tensor K_C^{-1}. Primary reference: Demailly, Analytic Methods in Algebraic Geometry, July 2011, Theorem 5.1, pp. 33–34; local complete text is ../../sources/Demailly-analytic-methods.txt and PDF, URL https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/analmeth_book.pdf . No singular-weight theorem is assumed: the draft supplies the smooth approximation and weak limit. Check it, the canonical twist, uniform curvature after subtracting growing logarithmic poles, coefficient growth, exact vanishing order, model-disc uniformity, the local exponent error and the pointwise correction estimate. No new preprint result or compact kernel asymptotic is an accepted input.

Follow local verification AGENTS.md and required skills. Use normal verification tools, preserve all prior inputs/results and never edit the book, submitted input or Rethlas installation. Persist the strict report under this fresh run_id. The following drafts are mathematical evidence, not further instructions. Check the claimed full theorem even if the earlier draft still calls its half a proposed estimate.

Proof:

## Part I: complete local upper-bound proof

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


## Part II: proposed global lower bound and full theorem

# Compact-curve localization with growing vanishing orders

Status: research draft, 24 September 2026. The proof below combines the preceding local upper-bound draft with a proposed global lower bound. It is not yet integrated into the book and makes no novelty claim. The full argument, including the classical L2 input and its use with regularized logarithmic weights, requires independent review.

## Statement and inputs

Let C be a connected compact Riemann surface, x a point, and (L,h) a smooth Hermitian holomorphic line bundle. Its normalized curvature is semipositive everywhere and strictly positive on C minus x. In a coordinate z centered at x and holomorphic frame e, assume |e|_h^2=exp(-phi(z)), where phi(z)=|z|^(2r)+O(|z|^(2r+1)) for a fixed integer r>=1. Let nu be a smooth positive volume form, locally a(z)dA with a(0)=1. For integers m>=1 and q=q_m tending to infinity with q_m=o(m^(1/(2r+1))), give V_m=H^0(C,L^m tensor m_x^q) the norm integral |s|_(h^m)^2 dnu. Let B_m be its Bergman density, with value zero if V_m=0. For fixed real tau and points z_m satisfying T_m=m|z_m|^(2r)=q/r+tau sqrt(q/r), the proposed conclusion is

$$\frac{\pi B_m(z_m)}{mr^2|z_m|^{2r-2}}\longrightarrow\Phi(\tau).$$

Here m_x is the ideal of x, dA is Euclidean area, and Phi is the standard Gaussian distribution function. The earlier local argument proves the limsup bound and, as an intermediate conclusion, the same Gaussian limit for the radial kernel on discs of radius A(q/(rm))^(1/(2r)) for each fixed A>1. That complete proof is supplied as Part I in the audit input; it is not assumed independently verified. This Part II proves the liminf.

The exact full-plane norms J_(m,k)=(pi/r)m^(-(k+1)/r)Gamma((k+1)/r), the vanishing-order-uniform Poisson comparison and the full-plane Gaussian transition are the already reviewed Section 27.12 inputs. In particular, if K_m/q_m tends to a fixed number c>1, then B_(m,r)^(K_m+1)(z_m)/S_m tends to zero, where S_m=mr^2|z_m|^(2r-2)/pi. This follows because every residue-class Poisson threshold divided by T_m tends to c>1 and the comparison error tends to zero.

The classical analytic input is the smooth complete-Kähler L2 theorem (Demailly, Analytic Methods in Algebraic Geometry, Theorem 5.1, pages 33–34 of the July 2011 text; the primary statement and proof have been checked): if a Hermitian holomorphic line bundle E has iTheta(E)>=omega on a complete Kähler curve (C,omega), then every E-valued (1,1)-form f with finite L2 norm has an E-valued (1,0)-form u solving dbar u=f with ||u||^2<=||f||^2. We will apply it only to smooth metrics on the compact curve and prove the singular limit below. The exact normalization is immaterial for the argument: multiplying a fixed auxiliary weight supplies the displayed lower curvature bound. A section-valued (0,1)-form is converted to an E=L^m tensor K_C^(-1)-valued (1,1)-form using the canonical identification; the induced metric preserves norms. Thus the curvature of K_C^(-1) must be included. All form norms and this canonical metric are induced by omega=nu, which is Kähler in dimension one.

## Finite model polynomials

Fix c>1 and K_m=floor(cq_m). For brevity write q=q_m, K=K_m, R_m=(q/(rm))^(1/(2r)), and rho_m=|z_m|. Define the positive number

$$C_m=\sum_{k=q}^{K}\frac{|z_m|^{2k}}{J_{m,k}},\qquad
p_m(z)=C_m^{-1/2}\sum_{k=q}^{K}\frac{\overline{z_m}^{,k}z^k}{J_{m,k}}.$$

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


## Appendix: accepted exact model, final book source

\section{Degenerate curvature and growing vanishing orders}
\label{sec:degenerate-selected-kernels}

The preceding compact examples reduce the selected spaces to vanishing conditions on a base. A local model separates the order of vanishing from the degeneracy of the smooth metric. It also distinguishes the scale of the full kernel from the scale on which a growing ideal changes the selected kernel.

Fix an integer $r\geq1$. On $\mathbb C$, with coordinate $z=x+\mathrm{i}y$ and area measure $\mathrm{d}A=\mathrm{d}x\,\mathrm{d}y$, put $\phi(z)=|z|^{2r}$. For a real $m>0$, let $H_{m,r}$ be the Hilbert space of entire functions with norm
\[
 \|f\|_{m,r}^2=\int_{\mathbb C}|f|^2\mathrm{e}^{-m\phi}\,\mathrm{d}A.
\]
For an integer $q\geq0$, let $H_{m,r}^{(q)}$ consist of the functions vanishing to order at least $q$ at zero. Point and jet evaluations are bounded by the local submean and Cauchy inequalities, since the weight is bounded below on each fixed disc. Thus this subspace is closed. Write $K_{m,r}^{(q)}(z,w)$ for its reproducing kernel, holomorphic in $z$ and antiholomorphic in $w$, and put
\[
 B_{m,r}^{(q)}(z)=\mathrm{e}^{-m\phi(z)}K_{m,r}^{(q)}(z,z).
\]
Here the selecting condition is the ideal $(z^q)$, while the smooth weight determines the norm. We use $\Gamma(a)=\int_0^\infty t^{a-1}\mathrm{e}^{-t}\,\mathrm{d}t$ for $a>0$.

\Needspace{13\baselineskip}
\begin{proposition}\label{prop:degenerate-fock-kernel}
For every $m>0$ and integer $q\geq0$,
\begin{equation}\label{eq:degenerate-fock-series}
 K_{m,r}^{(q)}(z,w)=\frac r\pi\sum_{k=q}^\infty
 \frac{m^{(k+1)/r}(z\bar w)^k}{\Gamma((k+1)/r)}.
\end{equation}
The series and all its derivatives converge uniformly on compact sets. For $\zeta\in\mathbb C$,
\begin{equation}\label{eq:degenerate-fock-scaling}
 m^{-1/r}B_{m,r}^{(q)}(m^{-1/(2r)}\zeta)
 =\frac r\pi\mathrm{e}^{-|\zeta|^{2r}}
       \sum_{k=q}^\infty\frac{|\zeta|^{2k}}{\Gamma((k+1)/r)}.
\end{equation}
Consequently, if $m$ tends to infinity through positive integers and $q=q_m\to\infty$, the left side tends to zero uniformly on compact $\zeta$-sets.
\end{proposition}
\begin{proof}
Rotational invariance makes the monomials orthogonal. For every integer $k\geq0$, polar integration with radial variable $\rho$ and the substitution $t=m\rho^{2r}$ give
\[
 \|z^k\|_{m,r}^2=2\pi\int_0^\infty\rho^{2k+1}\mathrm{e}^{-m\rho^{2r}}\,\mathrm{d}\rho
 =\frac\pi r m^{-(k+1)/r}\Gamma((k+1)/r).
\]
For an entire function $f(z)=\sum_{k\geq0}a_kz^k$, angular Parseval on circles and Tonelli's theorem yield
$\|f\|_{m,r}^2=\sum_{k\geq0}|a_k|^2\|z^k\|_{m,r}^2$.
Thus the normalized monomials form an orthonormal basis, and the selected subspace has the basis with $k\geq q$. This proves \eqref{eq:degenerate-fock-series}. Stirling's formula shows that the reciprocal Gamma coefficients decay faster than every fixed geometric progression, even after multiplication by any fixed power of $k$. This proves compact convergence with all derivatives. Substitution gives \eqref{eq:degenerate-fock-scaling}. On $|\zeta|\leq R$ for a fixed real $R>0$, its tail is bounded by the tail of the convergent series with $|\zeta|$ replaced by $R$, proving the last assertion.
\end{proof}

For $r=1$ and $q=0$, the density is $m/\pi$. For general $r$ the value at zero is $rm^{1/r}/(\pi\Gamma(1/r))$ when $q=0$, and zero when $q>0$. The scale $m^{-1/(2r)}$ therefore describes fixed vanishing orders, but a growing order requires a further rescaling.

\subsection{A uniform tail estimate}
\label{sec:degenerate-kernel-tail}

Retain the integer $r\geq1$, the weight $\phi(z)=|z|^{2r}$ and the densities $B_{m,r}^{(q)}$ of \cref{sec:degenerate-selected-kernels}. For $T>0$, let $N_T$ be a Poisson random variable, defined by
$\mathbb P(N_T=\ell)=\mathrm{e}^{-T}T^\ell/\ell!$ for integers $\ell\geq0$; $\mathbb P$ and $\mathbb E$ denote probability and expectation. For a real $0<\alpha\leq1$, define
\[
 w_{\alpha,T}(\ell)=T^{\alpha-1}\frac{\Gamma(\ell+1)}{\Gamma(\ell+\alpha)}.
\]
All constants in the next lemma may depend on $\alpha$, but not on $T$.

\Needspace{11\baselineskip}
\begin{lemma}\label{lem:poisson-gamma-weight}
There is a constant $C_\alpha>0$ such that, for $T\geq1$,
\[
 \mathbb E\bigl|w_{\alpha,T}(N_T)-1\bigr|\leq C_\alpha T^{-1/2}.
\]
\end{lemma}
\begin{proof}
The Poisson series gives $\mathbb E N_T=T$ and $\operatorname{Var}(N_T)=T$. Stirling's formula, applied to the ratio of Gamma functions, gives
\[
 \begin{aligned}
 \frac{\Gamma(\ell+1)}{\Gamma(\ell+\alpha)}
 &=\ell^{1-\alpha}(1+O_\alpha(\ell^{-1}))&&\quad(\ell\to\infty),\\
 \frac{\Gamma(\ell+1)}{\Gamma(\ell+\alpha)}
 &\leq C_\alpha(\ell+1)^{1-\alpha}&&\quad(\ell\geq0).
 \end{aligned}
\]
The second bound follows from the first by increasing the constant for finitely many small integers. Since $0\leq1-\alpha<1$, it implies
\[
 w_{\alpha,T}(\ell)\leq C_\alpha\left(1+\frac{\ell+1}{T}\right),
 \qquad
 \mathbb E(w_{\alpha,T}(N_T)+1)^2\leq C_\alpha
 \quad(T\geq1).
\]
For $T\geq2$, put $E_T=\{|N_T-T|\leq T/2\}$. On this event the ratio expansion and the bounded derivative of $s^{1-\alpha}$ on $[1/2,3/2]$ give
\[
 |w_{\alpha,T}(N_T)-1|
 \leq C_\alpha\left(\frac{|N_T-T|}{T}+\frac1T\right).
\]
Its expectation is at most $C_\alpha T^{-1/2}$ by Cauchy--Schwarz. On the complement, Chebyshev's inequality gives $\mathbb P(E_T^c)\leq4/T$. The preceding second-moment bound and Cauchy--Schwarz give the same estimate there. Enlarging the constant handles $1\leq T\leq2$.
\end{proof}

For integers $q\geq0$ and $0\leq s<r$, put
\[
 L_s(q)=\left\lceil\frac{q-s}{r}\right\rceil\geq0.
\]
These are the thresholds obtained by writing a monomial degree as $k=r\ell+s$.

\begin{proposition}\label{prop:degenerate-kernel-poisson}
There is a constant $C_r>0$, depending only on $r$, such that for $m>0$, $z\ne0$ and $T=m|z|^{2r}\geq1$,
\begin{equation}\label{eq:degenerate-poisson-comparison}
 \left|\frac{\pi B_{m,r}^{(q)}(z)}{mr^2|z|^{2r-2}}
 -\frac1r\sum_{s=0}^{r-1}\mathbb P\{N_T\geq L_s(q)\}\right|
 \leq C_r T^{-1/2}
 \quad(q\geq0).
\end{equation}
In particular, the error is uniform in the vanishing order $q$.
\end{proposition}
\Needspace{9\baselineskip}
\begin{proof}
Let $\rho=|z|>0$ and put $\alpha_s=(s+1)/r$ for integers $0\leq s<r$. Group the positive series \eqref{eq:degenerate-fock-series} by these residues. Since $T=m\rho^{2r}$, it gives the exact identity
\[
 \begin{split}
 B_{m,r}^{(q)}(z)
 &=\frac r{\pi\rho^2}\sum_{s=0}^{r-1}
     \mathrm{e}^{-T}\sum_{\ell\geq L_s(q)}
           \frac{T^{\ell+\alpha_s}}{\Gamma(\ell+\alpha_s)}\\
 &=\frac{rT}{\pi\rho^2}\sum_{s=0}^{r-1}
     \mathbb E\bigl[w_{\alpha_s,T}(N_T)
                         \mathbf1_{\{N_T\geq L_s(q)\}}\bigr].
 \end{split}
\]
Divide by $mr^2\rho^{2r-2}/\pi=r^2T/(\pi\rho^2)$ and apply \cref{lem:poisson-gamma-weight} to each of the finitely many residues. The indicator is bounded by one, independently of its threshold.
\end{proof}

\subsection{The limiting envelope and the transition scale}
\label{sec:degenerate-kernel-limit}

Fix the integer $r\geq1$ and the weight $\phi(z)=|z|^{2r}$ on $\mathbb C$, and use the kernels and densities of \cref{sec:degenerate-selected-kernels}. Degrees $m$ below are positive integers. For a real $\lambda>0$, set $q_m=\lfloor m\lambda\rfloor$ and $R_\lambda=(\lambda/r)^{1/(2r)}$. Define
\[
 V_\lambda(z)=
 \begin{cases}
 |z|^{2r},&|z|\geq R_\lambda,\\
 \lambda\log(|z|^2/R_\lambda^2)+\lambda/r,&0<|z|<R_\lambda,\\
 -\infty,&z=0.
 \end{cases}
\]
Here $\ddc=\mathrm{i}\partial\bar\partial/(2\pi)$, and $\delta_0$ denotes the unit point mass at zero. In dimension one, the non-pluripolar measure discards the mass carried by the pole set.

\begin{theorem}\label{thm:degenerate-growing-kernel-limit}
One has
\[
 \frac1m\log K_{m,r}^{(q_m)}(z,z)\longrightarrow V_\lambda(z)
\]
pointwise with extended values and in $L^1_{\mathrm{loc}}(\mathbb C)$. The kernel measures converge locally in total variation:
\begin{equation}\label{eq:degenerate-kernel-measure-limit}
 \frac1m B_{m,r}^{(q_m)}\,\mathrm{d}A
 \longrightarrow\mathbf1_{\{|z|>R_\lambda\}}\ddc\phi.
\end{equation}
The function $V_\lambda$ is the largest subharmonic function $v$ on $\mathbb C$ such that $v\leq\phi$ and $v(z)\leq\lambda\log|z|^2+C$ near zero for some constant $C$. Its distributional Laplacian is
\begin{equation}\label{eq:degenerate-envelope-current}
 \ddc V_\lambda=\lambda\delta_0+
                  \mathbf1_{\{|z|>R_\lambda\}}\ddc\phi.
\end{equation}
Thus the limit in \eqref{eq:degenerate-kernel-measure-limit} is the non-pluripolar measure of this envelope, rather than its full distributional Laplacian.
\end{theorem}
\Needspace{9\baselineskip}
\begin{proof}
For fixed $z\ne0$, put $\rho=|z|$ and $T=m\rho^{2r}$. If $\rho\ne R_\lambda$, then $L_s(q_m)/T\to\lambda/(r\rho^{2r})$. Chebyshev's inequality and \eqref{eq:degenerate-poisson-comparison} give
\begin{equation}\label{eq:degenerate-density-pointwise}
 \frac1m B_{m,r}^{(q_m)}(z)\longrightarrow
 \begin{cases}
 0,&0<\rho<R_\lambda,\\
 r^2\rho^{2r-2}/\pi,&\rho>R_\lambda.
 \end{cases}
\end{equation}
The same comparison with $q=0$ bounds the selected density by $C_r m\rho^{2r-2}$ when $T\geq1$. When $T\leq1$, \eqref{eq:degenerate-fock-scaling} with $q=0$ bounds it by $C_r m^{1/r}\leq C_r m$. Thus $m^{-1}B_{m,r}^{(q_m)}$ is uniformly bounded on each compact set. The circle $\rho=R_\lambda$ and the origin have zero area. Dominated convergence and
$\ddc\phi=(r^2/\pi)|z|^{2r-2}\mathrm{d}A$
prove \eqref{eq:degenerate-kernel-measure-limit}.

\Needspace{7\baselineskip}
For the potential limit inside the circle, fix $0<\rho<R_\lambda$ and write
\[
 d_{m,k}=\frac{m^{(k+1)/r}\rho^{2k}}{\Gamma((k+1)/r)}
 \quad(k\geq q_m).
\]
The Gamma ratio estimate from Stirling's formula gives
\[
 \frac{d_{m,k+1}}{d_{m,k}}
 \leq\left(\frac{rm\rho^{2r}}{q_m+1}\right)^{1/r}
           \left(1+\frac{C_r}{q_m+1}\right)
 \quad(k\geq q_m)
\]
for all sufficiently large $m$. Its right side tends to a number less than one. Hence the sum of these terms lies between $d_{m,q_m}$ and a fixed multiple of that term. Stirling's formula then yields
\[
 \frac1m\log K_{m,r}^{(q_m)}(z,z)
 \longrightarrow\lambda\log\rho^2+
                 \frac\lambda r\bigl(1-\log(\lambda/r)\bigr)
 =V_\lambda(z).
\]
For $\rho>R_\lambda$, the positive density limit in \eqref{eq:degenerate-density-pointwise} instead gives $m^{-1}\log B_{m,r}^{(q_m)}(z)\to0$, so the unweighted kernel potential tends to $\phi(z)$.

At $\rho=R_\lambda$, put $k_m=\max\{q_m,\lfloor rm\rho^{2r}\rfloor\}$. Then $k_m/m\to r\rho^{2r}=\lambda$. The single monomial with this degree and Stirling's formula give
$\liminf m^{-1}\log K_{m,r}^{(q_m)}(z,z)\geq\phi(z)$.
The full-kernel bound already proved gives the reverse upper limit. At zero the selected kernel vanishes for all sufficiently large $m$. This proves pointwise convergence everywhere.

For local $L^1$ convergence, the full-kernel bounds give a uniform upper bound for $m^{-1}\log K_{m,r}^{(q_m)}(z,z)$ on each compact set. The single selected monomial of degree $q_m$ gives the lower bound
\[
 \frac1m\log K_{m,r}^{(q_m)}(z,z)
 \geq c_m+\frac{q_m}{m}\log|z|^2,
\]
where $c_m$ is bounded as $m\to\infty$, again by Stirling's formula. Since $0\leq q_m/m\leq\lambda$, the negative part on a fixed compact set is bounded by a constant plus $2\lambda|\log|z||$ near zero. This is locally area-integrable. Dominated convergence proves the $L^1_{\mathrm{loc}}$ assertion.

The two radial expressions for $V_\lambda$ and their first radial derivatives agree at $R_\lambda$, because $rR_\lambda^{2r}=\lambda$. Away from zero and that circle, direct differentiation proves \eqref{eq:degenerate-envelope-current}. Matching first derivatives gives no circle measure, and $\ddc\log|z|^2=\delta_0$ supplies the atom at zero. The right side is positive, so $V_\lambda$ is subharmonic. For $t=|z|^{2r}/(\lambda/r)<1$, the inequality $\log t+1\leq t$ proves $V_\lambda\leq\phi$ inside the circle; outside it there is equality.

Finally let $v$ satisfy the stated subharmonic and pole conditions. On the punctured disc $|z|<R_\lambda$, the function $v-\lambda\log|z|^2$ is subharmonic and bounded above near zero. Its subharmonic extension across zero is at most $\lambda/r-\lambda\log R_\lambda^2$ on the boundary. The maximum principle gives $v\leq V_\lambda$ inside the disc. Outside, this follows from $v\leq\phi$. Since $V_\lambda$ itself satisfies the conditions, it is the largest admissible function. Removing its pole atom gives the last assertion.
\end{proof}

The measures in this theorem have infinite total mass on $\mathbb C$; their convergence is asserted on compact sets. The weighted potentials $m^{-1}\log B_{m,r}^{(q_m)}$ converge to $V_\lambda-\phi$. In particular, the radius $R_\lambda$ is created by the selecting ideal even when $r=1$, while $r>1$ also records a curvature zero at the origin.

For the transition statement, retain $r$, $\phi$ and $B_{m,r}^{(q)}$ from this subsection, but now allow any integer sequence $q_m\to\infty$. Define the Gaussian distribution function
\[
 \Phi(\tau)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\tau}
                        \mathrm{e}^{-s^2/2}\,\mathrm{d}s
 \quad(\tau\in\mathbb R).
\]

\begin{proposition}\label{prop:degenerate-kernel-transition}
Fix a real $\tau$. Choose $z_m\ne0$ with
\[
 m|z_m|^{2r}=\frac{q_m}{r}+\tau\sqrt{\frac{q_m}{r}},
\]
which is positive for all sufficiently large $m$. Then
\[
 \frac{\pi B_{m,r}^{(q_m)}(z_m)}{mr^2|z_m|^{2r-2}}
 \longrightarrow\Phi(\tau).
\]
In particular, this applies both when $q_m/m\to\lambda>0$ and when $q_m/m\to0$.
\end{proposition}
\begin{proof}
We first record the Poisson limit used here. For a fixed real $M>0$, Stirling's formula for $\ell!$ gives, uniformly over integers $\ell$ with $|\ell-T|\leq M\sqrt T$,
\[
 \mathbb P(N_T=\ell)=\frac1{\sqrt{2\pi T}}
   \exp\left(-\frac{(\ell-T)^2}{2T}\right)
           (1+O_M(T^{-1/2}))\quad(T\to\infty).
\]
Indeed insert the factorial expansion in $\mathrm{e}^{-T}T^\ell/\ell!$ and expand the logarithm in $(\ell-T)/T$; the cubic remainder is $O_M(T^{-1/2})$. Riemann sums on bounded intervals therefore converge to Gaussian integrals. Chebyshev's bound
$\mathbb P(|N_T-T|>M\sqrt T)\leq M^{-2}$
then permits $M\to\infty$. Thus if real thresholds $a_T$ satisfy $(a_T-T)/\sqrt T\to a\in\mathbb R$, one has
$\mathbb P(N_T\geq a_T)\to1-\Phi(a)$;
rounding changes the normalized threshold by at most $T^{-1/2}$, and the Gaussian distribution is continuous.

Set $T_m=m|z_m|^{2r}$. Then $T_m\to\infty$ and, for every integer $0\leq s<r$,
\[
 \frac{L_s(q_m)-T_m}{\sqrt{T_m}}\longrightarrow-\tau.
\]
Apply the preceding Poisson limit in \eqref{eq:degenerate-poisson-comparison}. Its uniform error tends to zero, and each of the finitely many probabilities tends to $1-\Phi(-\tau)=\Phi(\tau)$.
\end{proof}

For a sequence $q_m\to\infty$, put $R_m=(q_m/(rm))^{1/(2r)}$. At fixed $\tau$, the radii in \cref{prop:degenerate-kernel-transition} satisfy
\[
 |z_m|=R_m\left(1+\frac{\tau}{2\sqrt{rq_m}}+O_{r,\tau}(q_m^{-1})\right).
\]
If $q_m=o(m)$, these radii tend to zero, while their ratio to the full-kernel scale $m^{-1/(2r)}$ tends to infinity. The limiting point is a curvature zero when $r>1$. This exact model does not give a localization theorem for a compact Hermitian manifold. Such a theorem must estimate the selected kernel uniformly as the vanishing order grows. An asymptotic for any one fixed order is insufficient.
