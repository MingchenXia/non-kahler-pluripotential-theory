Run_id: gauduchon_trace_quantitative_01

Statement: Audit the quantitative Gauduchon trace metric proposition, its proof and both sharp exponent assertions below, in order. This is a bounded verification, not a whole-book or novelty claim. Use the normal verification workflow and persist the full report.

Conventions and accepted internal/classical inputs:
- X is a connected compact complex manifold of complex dimension n>=1. dd^c=i/(2 pi) partial bar-partial. theta is a smooth real (1,1) form with nonempty PSH(X,theta), gamma is a smooth positive Gauduchon metric (dd^c gamma^(n-1)=0), dV is a smooth positive probability volume, d is a smooth Riemannian distance.
- K^0 consists of genuine theta-psh u with mean zero against dV. T_gamma(u)=(theta+dd^c u) wedge gamma^(n-1) is a positive measure of common finite mass M=int theta wedge gamma^(n-1). This map is an affine homeomorphism from K^0 with L1 topology to its image with weak topology, is injective, and if M=0 K^0 is a singleton. No Monge-Ampere mass bound is a premise.
- d_gamma,d(u,v)=sup |int f d(T_gamma(u)-T_gamma(v))| over real f with sup norm<=1 and Lip_d<=1. It is a complete metric; at most 2M. dV is fixed for all L1 norms.
- Accept classical scalar elliptic Fredholm theory on a smooth compact connected manifold without boundary, the strong maximum principle for an elliptic operator without zero-order term, global W^{2,p} estimates on a complement to the kernel, and the Sobolev embedding W^{2,p} into C^1 for p greater than the real dimension. A scalar operator with positive definite principal symbol has index zero. Verify the use and normalization of these inputs; do not reprove them.
- The book's eq:gaud-trace-green is the unique mean-zero distribution G_gamma sigma solving dd^c G_gamma sigma wedge gamma^(n-1)=sigma for finite signed sigma of total mass zero, obtained by the same scalar elliptic theory. The Green result is motivation, not an additional estimate to assume.
- No other mathematical result from another manuscript or a private source is a premise. In the TeX excerpt, \ddc means dd^c and \cref/\eqref denote the internal inputs specified above.

Proof to verify:

The equivalence with the $L^1$ topology admits quantitative bounds. In the following statement all $L^1$ norms are taken with respect to the fixed probability volume $\mathrm{d}V$.

\begin{proposition}\label{prop:gaud-trace-quantitative}
With $X,\theta,\gamma,\mathrm{d}V$ and $d$ as above, there is a constant $C\geq1$, depending only on these data, such that
\[
 C^{-1}\|u-v\|_{L^1}
 \leq d_{\gamma,d}(u,v)
 \leq C\|u-v\|_{L^1}^{1/2}
 \qquad(u,v\in\mathcal K^0_{\theta,\mathrm{d}V}).
\]
\end{proposition}
\begin{proof}
Put $w=u-v$, $\sigma=\mathcal T_\gamma(u)-\mathcal T_\gamma(v)$ and $M=M_{\theta,\gamma}$. Then $\int_Xw\,\mathrm{d}V=0$, $\sigma=\ddc w\wedge\gamma^{n-1}$ and $\|\sigma\|_{\mathrm{TV}}\leq2M$. If $M=0$, \cref{thm:gaud-trace-homeomorphism} gives $u=v$, so both estimates hold.

For the first estimate, consider the scalar elliptic operator
\[
 A\phi=\frac{\ddc\phi\wedge\gamma^{n-1}}{\mathrm{d}V}
\]
and its formal adjoint $A^*$ with respect to $\mathrm{d}V$. The kernel of $A$ consists of constants by the maximum principle. The Gauduchon identity gives $A^*1=0$; since the scalar elliptic operator has index zero, the adjoint kernel also consists of constants. Thus, for a smooth real function $g$, the equation
\[
 A^*\phi=g-\int_Xg\,\mathrm{d}V,\qquad
 \int_X\phi\,\mathrm{d}V=0
\]
has a unique smooth solution. Fix $p>2n$. The global elliptic $W^{2,p}$ estimate on the mean-zero subspace and the Sobolev embedding into $C^1$ give
\[
 \|\phi\|_\infty+\operatorname{Lip}_d(\phi)
 \leq C\|g\|_\infty.
\]
This is the scalar elliptic theory used for \eqref{eq:gaud-trace-green}, applied to the adjoint. Pairing the distributional equation $Aw\,\mathrm{d}V=\sigma$ with $\phi$ yields
\[
 \left|\int_Xwg\,\mathrm{d}V\right|
 =\left|\int_X\phi\,\mathrm{d}\sigma\right|
 \leq C\|g\|_\infty d_{\gamma,d}(u,v).
\]
Taking the supremum over smooth real $g$ with $\|g\|_\infty\leq1$ gives $\|w\|_{L^1}$ and proves the first estimate.

For the second estimate, let $f$ be any test function in the definition of $d_{\gamma,d}$. A fixed finite coordinate cover, smooth partition of unity and convolution at scale $0<\epsilon<\epsilon_0$ give smooth functions $f_\epsilon$ satisfying
\[
 \|f-f_\epsilon\|_\infty\leq C\epsilon,
 \qquad \|A^*f_\epsilon\|_\infty\leq C\epsilon^{-1}.
\]
The constants are uniform over this test family. To see the second bound, localize $f$ by the fixed partition. The localized functions have uniformly bounded values and first weak derivatives. In each second derivative of their convolution, move one derivative onto the mollifier; its $L^1$ norm is $O(\epsilon^{-1})$. The lower-order terms of $A^*$ have fixed smooth coefficients and satisfy the same bound. Hence
\[
 \left|\int_Xf\,\mathrm{d}\sigma\right|
 \leq C\bigl(M\epsilon+\epsilon^{-1}\|w\|_{L^1}\bigr).
\]
If $0<\|w\|_{L^1}<\epsilon_0^2$, choose $\epsilon=\|w\|_{L^1}^{1/2}$. For larger norms use $d_{\gamma,d}(u,v)\leq2M$, and for $w=0$ use injectivity. Taking the supremum over $f$ proves the asserted bound.
\end{proof}

\begin{example}\label{ex:gaud-trace-sharp-exponents}
Let $X=\mathbb C/(\mathbb Z+\mathrm{i}\mathbb Z)$, with $z=x+\mathrm{i}y$, $\theta=\gamma=\eta=(\mathrm{i}/2)\mathrm{d}z\wedge\mathrm{d}\bar z$, $\mathrm{d}V=\eta$ and the flat distance $d$. For integers $k\geq1$, set
\[
 u_k=\frac{\cos(2\pi kx)}{2\pi k^2}.
\]
These are smooth mean-zero potentials, and our normalization gives
\[
 \theta+\ddc u_k=\left(1-\frac12\cos(2\pi kx)\right)\eta>0,
 \qquad \|u_k\|_{L^1}=\frac1{\pi^2k^2}.
\]
The function $f_k=\cos(2\pi kx)/(2\pi k)$ has supremum norm at most one and Lipschitz constant at most one. It follows that
\[
 d_{\gamma,d}(u_k,0)
 \geq\left|\int_Xf_k\,\ddc u_k\right|
 =\frac1{8\pi k}.
\]
Consequently, the exponent $1/2$ in \cref{prop:gaud-trace-quantitative} cannot be replaced by any larger exponent, even for smooth strictly positive potentials on a fixed curve. The exponent one in the reverse estimate is also optimal: for $0<t\leq1$, both $\|tu_1\|_{L^1}$ and $d_{\gamma,d}(tu_1,0)$ equal $t$ times their positive values at $t=1$.
\end{example}

