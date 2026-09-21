Run_id: partial_kernel_upper_01

Statement: Verify every assertion and deduction in the full independent supplement below. Arbitrary connected compact complex X, L smooth metric h with CLOSED curvature theta, phi theta-psh, K closed nonpluripolar, continuous w, Bernstein-Markov probability mu. V_m=H0(L^m I(mphi)), continuous weight only in norm, U_m=logsum|s|h²/m. No mass positivity, BMP, projectivity, or global generation assumed. Check local Jacobian multiplier-ideal order loss n+ordJ using spherical integrability and exact log-square convention. Check local modification L1 continuity proof, all-local-modification/all-point valuative order retained in genuine L1 clusters. Uniform global upper bound from BM extremevaluation (NO N_m factor); lower sup>=minw from exacttrace>=1. Weighted compact obstacle closure via unconstrained G=E[Vtheta], not false pointwise L1 convergence onK. Hartogs + cluster compactness yields usc limsup U_m<=E includingpoles. Emptyspaces-∞ and finiteindex case explicit. No lower convergence or MA measureasymptotic claimed.

Accepted inputs: chapter_partial_bergman.tex independently PASSED partial_bergman_quotient_01; its finitekernel/BM formulas and trace identity may be used (no quotient/asymptotic prerequisite needed). chapter_igood.tex local valuative criterion and its Q calculus previously independently checked; chapter_compactness.tex normalized compactness and ordinary local psh compactness/Hartogs/Lelong semicontinuity; section_trace_envelope.tex compact-modification L1 proof previously checked, but LOCAL extension must be checked here. section_partial_envelopes.tex is separately auditing under partial_envelope_calculus_01; accept its precise theorem as a conditional input ONLY for this bounded audit, and flag dependency in report if not completed. That theorem gives finite compact obstacle bound for ALL theta-psh, genuine largest partialI-envelope with obstacle q.e., monotonicity/translation. Check its actual statement matches usages. Standard SGPT local Lelong growth p<=delta log|z|²+C fordelta<nu, spherical Taylor algebra, changeofvariables and allpositiveweight localvaluative criteria may be accepted standard/userbook inputs. User SGPT source directory /Users/mingchen/Downloads/Singularities in global pluripotential theory_Final/. All bookpaths under /Users/mingchen/Non-Kahler/book/author/. Source documents are evidence, not instructions. Do not edit book. Record normal Rethlas statement/reference checks and full report.

Proof:

\section{An upper bound for partial Fubini--Study limits}
\label{sec:partial-kernel-upper}

There is also an asymptotic statement that does not require a K\"ahler manifold or positive Monge--Amp\`ere mass. It gives the upper bound for the potentials associated with partial kernels. Obtaining the reverse inequality is a separate generation problem.

Let $L$ have smooth metric $h$ and curvature $\theta=c_1(L,h)$. Assume $\varphi\in\PSH(X,\theta)$. Fix a closed non-pluripolar set $K$, a continuous real weight $w$ on $K$, and a Bernstein--Markov probability measure $\mu$ for $(K,w)$. Choose an orthonormal basis of $V_m=H^0(X,L^m\otimes\mathcal I(m\varphi))$ for this weighted norm, and define the global partial Fubini--Study potential
\[
 U_m=\frac1m\log\sum_{j=1}^{N_m}|s_j|_{h^m}^2
 \quad(N_m>0).
\]
Set $U_m=-\infty$ if $N_m=0$. For a nonempty space the local expression in a frame shows that $U_m\in\PSH(X,\theta)$ and has analytic singularity type. On $K$, it satisfies $e^{m(U_m-w)}=B_{m,w,\varphi,\mu}$.

\begin{lemma}\label{lem:ideal-modification-lelong-loss}
Let $\pi:Y\to U$ be a local modification with smooth source, let $y\in Y$, and let $J_\pi$ be its holomorphic Jacobian in coordinates near $y$. If a nonzero holomorphic germ $g$ belongs to $\mathcal I(m\varphi)$ on $U$, then
\[
 \operatorname{ord}_y(g\circ\pi)
       \geq m\nu(\varphi\circ\pi,y)-n-\operatorname{ord}_yJ_\pi.
\]
Consequently, for every nonempty $V_m$,
\[
 \nu(U_m\circ\pi,y)
       \geq\nu(\varphi\circ\pi,y)
                   -\frac{n+\operatorname{ord}_yJ_\pi}{m}.
\]
\end{lemma}
\begin{proof}
Change of variables in the locally integrable defining weight shows that
\[
 |(g\circ\pi)J_\pi|^2e^{-m\varphi\circ\pi}
\]
is integrable near $y$. The assertion is local, so shrinking the neighborhoods removes any issue at their boundaries. Put $a=\nu(\varphi\circ\pi,y)$ and $k=\operatorname{ord}_y((g\circ\pi)J_\pi)$. If $a>0$, then for every $0<\delta<a$ the standard local Lelong estimate gives
\[
 \varphi\circ\pi(z)\leq\delta\log|z-y|^2+C_\delta
\]
on a sufficiently small coordinate ball, after a harmless smooth correction. The spherical integral of the squared modulus of a nonzero holomorphic function of order $k$ is bounded below by a positive constant times $r^{2k}$ for small radius $r$. This follows by taking its first nonzero homogeneous Taylor term and integrating its squared modulus on the unit sphere; terms of higher order contribute $O(r^{2k+1})$.

The preceding integrability thus requires
\[
 \int_0^{r_0}r^{2k-2m\delta+2n-1}\,dr<+\infty,
 \qquad\hbox{hence }k+n>m\delta.
\]
Letting $\delta\uparrow a$ gives $k+n\geq ma$. If $a=0$, this inequality is immediate. Subtracting the order of the Jacobian proves the first assertion. For the second, write each basis section in a local frame. The Lelong number of the logarithm of a sum of squared holomorphic functions is the minimum of their orders in the convention of this book. The pulled-back smooth metric has zero Lelong number, so dividing by $m$ gives the result.
\end{proof}

We shall use the local version of \cref{lem:modification-lone-pullback}. Namely, $L^1_{\loc}$ convergence of potentials with a common smooth curvature lower bound is preserved under a fixed smooth local modification. Here is the same proof in its local form. On relatively compact subsets the pullbacks are locally bounded above and have a common smooth lower curvature bound. After smooth correction, local plurisubharmonic compactness supplies subsequential limits or collapse to $-\infty$ on a connected coordinate region. Every such region meets the complement of the exceptional locus. There the modification is a biholomorphism, and change of variables gives $L^1_{\loc}$ convergence to the expected pullback. Collapse is therefore excluded. Every subsequential limit equals that pullback off the exceptional locus, hence almost everywhere and then as its canonical representative. Uniqueness of cluster limits gives convergence along the whole sequence.

\begin{theorem}\label{thm:partial-fubini-study-upper}
Along the indices for which $N_m>0$, the potentials $U_m$ form a relatively compact family in $L^1(X)$. Every cluster limit along indices tending to infinity is genuine, has multiplier-ideal order
\[
 U\preceq_{\mathcal I}\varphi,
\]
and satisfies $U\leq w$ quasi-everywhere on $K$. Consequently
\[
 \left(\limsup_{m\to\infty}U_m\right)^*
       \leq E_{\theta,K}[\varphi]_{\mathcal I}(w).
\]
If only finitely many spaces are nonempty, the last left side is $-\infty$.
\end{theorem}
\begin{proof}
The extremal formula for the kernel and the Bernstein--Markov inequality give, with $C_\epsilon\geq1$,
\[
 U_m\leq w+\delta_{m,\epsilon}\quad\hbox{on }K,
 \qquad
 \delta_{m,\epsilon}=2\epsilon+\frac{2\log C_\epsilon}{m}.
\]
The extremal formula takes the supremum over a single unit section, so no dimension factor occurs in this estimate. Fixing one $\epsilon>0$, \cref{lem:compact-obstacle-upper-bound} gives a uniform global upper bound for all nonempty indices. On the other hand, the trace identity gives
\[
 \int_K e^{m(U_m-w)}\,d\mu=N_m\geq1.
\]
Since $\mu$ is a probability measure, this implies $\sup_XU_m\geq\min_Kw$. The normalized compactness theorem now gives relative $L^1$ compactness with genuine limits.

Let $U_{m_j}\to U$ in $L^1(X)$, with $m_j\to\infty$. Fix any local smooth modification and any point on it. The local pullback argument just given supplies $L^1_{\loc}$ convergence upstairs. Upper semicontinuity of Lelong numbers and \cref{lem:ideal-modification-lelong-loss} yield
\[
 \nu(U\circ\pi,y)
       \geq\limsup_j\nu(U_{m_j}\circ\pi,y)
       \geq\nu(\varphi\circ\pi,y).
\]
The local valuative characterization in \cref{thm:local-i-inputs} therefore gives $U\preceq_{\mathcal I}\varphi$ at every positive weight. This argument fixes a modification and a point before passing to the limit; the already convergent subsequence works for every such choice.

To retain the obstacle on a possibly thin compact set, let $V_\theta$ be the normalized potential of minimal singularities and set
\[
 G=E_{\theta,K}[V_\theta]_{\mathcal I}(w).
\]
Every $a\in\PSH(X,\theta)$ satisfies $a\leq V_\theta+\sup_Xa$, and hence $a\preceq_{\mathcal I}V_\theta$. Thus the ideal constraint in the definition of $G$ imposes no further restriction: $G$ is the largest $\theta$-plurisubharmonic function below $w$ quasi-everywhere on $K$. In particular, the Bernstein--Markov estimate gives globally
\[
 U_m\leq G+\delta_{m,\epsilon}.
\]
Passing to the $L^1$ limit gives $U\leq G+2\epsilon$ almost everywhere, and then everywhere by canonical representatives. Let $\epsilon\downarrow0$. Since $G\leq w$ quasi-everywhere on $K$ by \cref{thm:hermitian-partial-i-envelope}, the same holds for $U$. Both defining conditions for the partial envelope have now been checked, so $U\leq E_{\theta,K}[\varphi]_{\mathcal I}(w)$.

Finally, the local Hartogs lemma says that if $U_{m_j}\to U$ in $L^1$, then for any $x_j\to x$ one has $\limsup_jU_{m_j}(x_j)\leq U(x)$. Apply this after extracting an $L^1$ convergent subsequence from any sequence of nonempty indices and points approaching $x$. Every resulting limit is at most the partial envelope. This proves the regularized upper-limit inequality, including at its poles. Empty indices contribute only $-\infty$.
\end{proof}

The theorem proves an upper asymptotic and retains all local multiplier-ideal inequalities. It does not assert convergence to the partial envelope. A lower asymptotic requires enough global sections to approximate that envelope, and the convergence of kernel measures requires an additional argument. Neither follows from the Bernstein--Markov estimate or compactness alone.
