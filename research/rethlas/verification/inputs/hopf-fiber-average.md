Run_id: hopf_fiber_average_01

Statement: Verify the complete proposition and proof below, including the optimal numerical constant, global fiber averaging, bounded descent and the pointwise equality characterization. This is a bounded manuscript check, not a novelty claim or whole-book certification.

Accepted internal inputs (check every application, do not reopen their proofs):
1. Hopf geometry and smooth mass identity, prop:hopf-mass: X=(C^3 minus0)/<z -> exp(-1)z>, pi:X->P^2. ddc=i partial bar-partial/(2pi); s=log|z|², alpha=ddc s=pi*omega_FS, beta=ds wedge dc s, omega=alpha+beta>0. alpha³=beta²=0; integral_P² omega_FS²=1. Fibers are E=C/(Z+2pi i Z), with Haar area dA_E=i dw wedge dbarw/(4pi), mass1; beta|fiber=2dA_E. For all smooth real u, integral_X (omega+ddc u)^3=6+6 integral_P² integral_fiber |u_w|² dA_E omega_FS². Fiber coordinate changes are translations by holomorphic base functions. The complete earlier chapter audit hopf_counterexample_01 passed.
2. Bounded exact regularization, thm:bounded-exact-regularization: for every bounded omega-psh function on a compact complex manifold with positive Hermitian background, smooth strictly positive approximants decrease to it and are uniformly bounded. This applies also to the Kähler base P² with omega_FS.
3. Bounded Bedford–Taylor continuity for decreasing uniformly bounded potentials in a smooth Hermitian background. Canonical quasi-psh representatives equal a.e. are equal everywhere. Decreasing bounded PSH limits preserve the background inequality.

Classical inputs: Fourier series/Parseval on the fixed flat torus, Fubini and dominated convergence. Verify the E-action invariance, horizontal-kernel positivity, fiber measure normalization, eigenvalue 1/4 and constant2/3, smooth pullback positivity, pointwise bounded descent and sharp example. Do not assume a general energy identity for nonsmooth potentials. No Popovici or new external theorem input. Do not edit the manuscript, old inputs, verifier memory or old outputs; use the normal bounded verifier workflow for this new run only.

Full LaTeX statement and proof:

The mass identity also measures the distance from a potential to its fiber average. Let $E=\mathbb C/(\mathbb Z+2\pi\mathrm{i}\mathbb Z)$ act on $X$ by scalar multiplication: for $a\in E$, the map $\tau_a:X\to X$ sends $[z]$ to $[\mathrm{e}^a z]$. This is well defined and preserves $\alpha$, $\beta$ and $\omega$. With the probability Haar measure $\mathrm{d}A_E$ of the preceding construction, set
\[
 \mathrm{d}\nu=\frac{\omega^3}{6}=\frac12\alpha^2\wedge\beta,
 \qquad
 Au(p)=\int_Eu(\tau_a(p))\,\mathrm{d}A_E(a)
 \quad(p\in X)
\]
for every bounded Borel function $u:X\to\mathbb R$. Thus $Au$ is constant on each fiber, and $\nu$ is a probability measure whose fiber measures are $\mathrm{d}A_E$ and whose base measure is $\omega_{\FS}^2$.

\begin{proposition}\label{prop:hopf-fiber-average}
For every $u\in\PSH(X,\omega)\cap L^\infty(X)$, the average $Au$ is the pullback of a bounded $\omega_{\FS}$-plurisubharmonic function on $\mathbb P^2$, and
\begin{equation}\label{eq:hopf-average-mass}
 \|u-Au\|_{L^2(X,\nu)}^2
 \leq\frac23\left(\int_X(\omega+\ddc u)^3-6\right).
\end{equation}
The coefficient $2/3$ is optimal, even among smooth strictly positive potentials. Moreover,
\[
 \int_X(\omega+\ddc u)^3=6
 \quad\Longleftrightarrow\quad
 u=\pi^*v\quad\text{for some }
 v\in\PSH(\mathbb P^2,\omega_{\FS})\cap L^\infty(\mathbb P^2).
\]
\end{proposition}
\begin{proof}
First suppose that $u$ is smooth and $\omega+\ddc u>0$. Averaging the positive forms $\tau_a^*(\omega+\ddc u)$ gives $\omega+\ddc Au>0$. Write $Au=\pi^*v$. At each point, the kernel of $\partial s$, where $s=\log|z|^2$ on the cover, maps isomorphically to the tangent space of the base. Restricting $\pi^*(\omega_{\FS}+\ddc v)+\beta$ to this kernel shows that $\omega_{\FS}+\ddc v>0$.

For a smooth function $f:E\to\mathbb R$, the Fourier characters in \eqref{eq:hopf-heat-fourier} have nonzero eigenvalues
$\pi^2p^2+q^2/4\geq1/4$ for $-\partial_w\partial_{\bar w}$. Parseval's identity therefore gives
\[
 \int_E\left|f-\int_Ef\,\mathrm{d}A_E\right|^2\mathrm{d}A_E
 \leq4\int_E|f_w|^2\,\mathrm{d}A_E.
\]
Apply this inequality on every fiber and integrate against $\omega_{\FS}^2$. The mass identity \eqref{eq:hopf-mass} gives \eqref{eq:hopf-average-mass}.

For bounded $u$, choose smooth $u_j\downarrow u$ with $\omega+\ddc u_j>0$ by \cref{thm:bounded-exact-regularization}. The sequence is uniformly bounded. Its averages decrease pointwise to $Au$ by dominated convergence. The corresponding smooth base potentials $v_j$ decrease to a bounded $\omega_{\FS}$-plurisubharmonic function $v$, so $Au=\pi^*v$. Dominated convergence gives $u_j\to u$ and $Au_j\to Au$ in $L^2(X,\nu)$, while bounded Bedford--Taylor continuity gives convergence of the total masses. Thus \eqref{eq:hopf-average-mass} passes to $u$.

If the mass is $6$, the inequality gives $u=Au$ almost everywhere. Both functions are quasi-plurisubharmonic, so uniqueness of their canonical representatives gives equality everywhere. Conversely, if $u=\pi^*v$ with bounded $v\in\PSH(\mathbb P^2,\omega_{\FS})$, choose smooth strictly positive $v_j\downarrow v$ on the base using \cref{thm:bounded-exact-regularization}. The pullbacks decrease to $u$ and are uniformly bounded. Their vertical derivatives vanish, so \eqref{eq:hopf-mass} gives mass $6$ for each of them. Bounded Bedford--Taylor continuity gives the same mass for $u$.

To check the constant, choose a nonzero real $\rho\in C_c^\infty(U_0)$ and use the trivialization $\pi^{-1}(U_0)=U_0\times E$. The function
\[
 u(\xi,w)=\delta\rho(\xi)\cos(\operatorname{Im}w)
\]
extends by zero to a smooth function on $X$. For sufficiently small nonzero real $\delta$, it satisfies $\omega+\ddc u>0$. Its fiber average is zero, and its only fiber frequencies are $(p,q)=(0,\pm1)$, with eigenvalue $1/4$. Equality holds in the fiber inequality and hence in \eqref{eq:hopf-average-mass}, with nonzero left side. No smaller coefficient can hold.
\end{proof}

In particular, for any sequence of bounded potentials whose masses tend to $6$, the differences from their fiber averages tend to zero in $L^2(X,\nu)$. This conclusion controls fiber variation; the averaged potentials still vary in the bounded potential space of the base.
