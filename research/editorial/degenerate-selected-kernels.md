# Degenerate selected kernels: a model and a conditional transfer

Status: working research note, 24 September 2026, continued at checkpoint96. The elementary one-variable model below is now contained in the more complete book Section 27.12, whose growing-order extension has a full audit and a separately checked endpoint repair; see `degenerate-growing-kernels-review-96.md`. The conditional fixed-jet transfer argument in this note is still independently unaudited and outside the book. Its proposed global hypotheses remain open here. No novelty claim is made and no new arXiv theorem is a proof input.

## A one-variable model

Let $r\geq1$ and $q\geq0$ be integers, let $m>0$, and let $\mathrm{d}A=\mathrm{d}x\,\mathrm{d}y$ be Lebesgue area on $\mathbb C$, where $z=x+\mathrm{i}y$. Let $H_{m,r}$ be the Hilbert space of entire functions with squared norm

$$\|f\|_{m,r}^2=\int_{\mathbb C}|f(z)|^2\mathrm{e}^{-m|z|^{2r}}\,\mathrm{d}A(z).$$

Let $H_{m,r}^{(q)}$ be its closed subspace of functions vanishing to order at least $q$ at zero. Define the Gamma function by $\Gamma(a)=\int_0^\infty t^{a-1}\mathrm{e}^{-t}\,\mathrm{d}t$ for $a>0$. Point and jet evaluations are bounded: on a fixed small disc the weight has a positive lower bound, and the holomorphic submean and Cauchy inequalities bound them by the norm. In particular, the specified subspace is closed and has a reproducing kernel.

For each integer $k\geq0$, polar integration and the substitution $t=m\rho^{2r}$ give

$$\|z^k\|_{m,r}^2=2\pi\int_0^\infty\rho^{2k+1}\mathrm{e}^{-m\rho^{2r}}\,\mathrm{d}\rho=\frac{\pi}{r}m^{-(k+1)/r}\Gamma\!\left(\frac{k+1}{r}\right).$$

Rotational invariance makes distinct monomials orthogonal. They are complete: for the Taylor series $f(z)=\sum_{k\geq0}a_kz^k$, angular Parseval on each circle followed by Tonelli yields $\|f\|_{m,r}^2=\sum_{k\geq0}|a_k|^2\|z^k\|_{m,r}^2$. Thus Taylor partial sums converge in norm whenever the norm is finite. Membership in $H_{m,r}^{(q)}$ is exactly $a_0=\cdots=a_{q-1}=0$.

Consequently its unweighted reproducing kernel, holomorphic in $z$ and antiholomorphic in $w$, is

$$K_{m,r}^{(q)}(z,w)=\frac r\pi\sum_{k=q}^\infty\frac{m^{(k+1)/r}(z\bar w)^k}{\Gamma((k+1)/r)}.$$

The series and all its derivatives converge uniformly on compact subsets; for example Stirling's estimate gives superexponential decay of the reciprocal Gamma coefficients compared with any fixed geometric progression. The diagonal density is $B_{m,r}^{(q)}(z)=\mathrm{e}^{-m|z|^{2r}}K_{m,r}^{(q)}(z,z)$. For $\zeta\in\mathbb C$ one has the exact identity

$$m^{-1/r}B_{m,r}^{(q)}\bigl(m^{-1/(2r)}\zeta\bigr)=\frac r\pi\mathrm{e}^{-|\zeta|^{2r}}\sum_{k=q}^\infty\frac{|\zeta|^{2k}}{\Gamma((k+1)/r)}.$$

For $q=0$, the density at zero is $r m^{1/r}/(\pi\Gamma(1/r))$. For $q>0$ it is zero at the origin and positive away from it. For $r=1,q=0$ the formula reduces to the constant Gaussian density $m/\pi$, checking both normalization factors. The exponent $1/r$ comes from the curvature model, while $q$ changes the limiting profile through section selection.

The same formula also proves a limitation. If the integers $q_m$ tend to infinity, the normalized densities at this scale tend to zero uniformly on every compact $\zeta$-set: dominate the tail by the convergent series with $|\zeta|$ replaced by the compact set's radius. This conclusion holds for any rate of growth of $q_m$ and does not describe the density on moving, larger scales. In particular, the multiplier ideals of $m\lambda\log|z|^2$ with fixed $\lambda>0$ impose $q_m=\lfloor m\lambda\rfloor$; their behavior cannot be represented by the fixed-$q$ profile.

## Transfer under fixed jet constraints

For positive integers $m$, let $\Omega_m\subset\mathbb C$ be open neighborhoods that eventually contain every compact subset of $\mathbb C$. Let $\mathcal H_m$ be Hilbert spaces of holomorphic functions on $\Omega_m$ with bounded point and jet evaluations and reproducing kernels $\widehat K_m$. Assume these kernels converge in $C^\infty$ on compact subsets of $\mathbb C\times\mathbb C$ to $K_{1,r}^{(0)}$ from the preceding model, for a fixed integer $r\geq1$. Fix an integer $q\geq1$, independent of $m$, and define $J_m:\mathcal H_m\to\mathbb C^q$ by

$$J_m f=(f(0),f'(0),\ldots,f^{(q-1)}(0)).$$

Use the usual Hermitian inner product on $\mathbb C^q$ and denote the Hilbert adjoint by $J_m^*$. The matrix $G_m=J_mJ_m^*$ consists of the corresponding mixed jet derivatives of $\widehat K_m$ at $(0,0)$. Kernel convergence implies matrix convergence to a diagonal matrix with entries

$$\frac{r(j!)^2}{\pi\Gamma((j+1)/r)},\qquad 0\leq j<q.$$

Every entry is positive. Hence $G_m$ is invertible for all sufficiently large $m$, with uniformly bounded inverse. The operator

$$P_m=I-J_m^*G_m^{-1}J_m$$

where $I$ is the identity of $\mathcal H_m$, is the orthogonal projection onto $\ker J_m$: its correction term is self-adjoint and idempotent, its range is the range of $J_m^*$, and $J_mP_m=0$, while it acts as the identity on $\ker J_m$.

Apply $P_m$ to the evaluation representer $\widehat K_m(\cdot,w)$. This gives the reproducing kernel of $\ker J_m$. The subtracted term is a finite sum of products of jet derivatives of $\widehat K_m$, with coefficients from $G_m^{-1}$. Each factor converges in $C^\infty$ on compact sets. The projected kernels therefore converge in the same topology to the kernel obtained by imposing the first $q$ vanishing jets on the limiting model. By the first calculation that kernel is exactly $K_{1,r}^{(q)}$.

This is a conditional transfer lemma. It assumes convergence of the full off-diagonal kernels with jet control. An upper bound for the diagonal densities alone does not imply its hypothesis. When coordinates or bundle frames are rescaled, apply the hypothesis to the unweighted scalar kernel in that fixed frame; the diagonal metric weight is inserted only afterwards. The jet order is fixed, so inversion is in a fixed finite dimension. The proof gives no uniform estimate when $q=q_m\to\infty$.

## Questions for the book

In the compact setting, let $(L,h)$ be a holomorphic line bundle with smooth semipositive curvature and let $x$ be a point where that curvature has finite-order degeneracy. Can a verified full-kernel local theorem give the hypothesis of the transfer lemma for the spaces of sections vanishing to a fixed order at $x$? The local jet condition is precise; any further global ideal conditions would define a different space and require additional analysis.

For the actual partial kernels in Chapter 27, the selecting ideals depend on the degree. The exact model now has a q-uniform Poisson comparison and Gaussian transition at radius (q_m/(rm))^(1/(2r)). Determine which growth regimes permit a compact localization theorem, and control the smallest eigenvalue of the corresponding growing jet Gram matrix or find a method avoiding that inversion. The first model shows why a fixed-order asymptotic cannot settle this question. A successful local theorem would then have to be reconciled with the chapter's intrinsic section-growth normalization and fibration identities.

Chiang's arXiv:2609.24869v1 is a reading candidate for the full-kernel hypothesis. Its complete Kähler adjoint theorem and its general spectral-gap theorem have different premises. No theorem from it has been invoked above; the complete proof, convention conversion and actual geometric applicability remain to be checked.
