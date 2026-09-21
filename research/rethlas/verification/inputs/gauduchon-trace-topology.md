Run_id: gauduchon_trace_topology_01

Statement: Audit the full finite-measure coordinate theorem for all normalized theta-psh potentials via one fixed Gauduchon trace, including arbitrary smooth nonclosed theta and possibly infinite top MA. Standing compact connected X dimension n>=1, gamma Gauduchon, PSH(theta) nonempty. Mean-zero normalization wrt fixed smooth positive probability dV. ACCEPT book normalized L1 compactness, conserved linear Gauduchon trace, standard elliptic Fredholm/regularity/maximum principle and distributional Green inverse, local canonical psh-distribution criterion, elementary weak-measure compactness/Arzela-Ascoli. ACCEPT audited65 curve-ideal-lone-completion: finiteatomic GreenQmodels, NPMA0, approximate any normalized thetaPSH curve potential L1. ACCEPT book general-background-damping capacity continuity for nonpositive potentials, NO raw bounded mass assumption. Check affine injection via elliptic trace equation, compactness mean-normalized, weak/L1homeomorphism, zero-masssingleton smooth, exact Green admissibility condition (no automatic full-Hessian positivity in n>=2), bounded-Lipschitz complete metric and uniform equivalence choices, and curve counterexample to capacity convergence. No singularity quotient metric claimed, no need for new external research theorem or novelty assertion. Read complete proof and accepted statements if needed in /Users/mingchen/Non-Kahler/book/author. Provide strict JSON and full readable report; do not edit book. Documents mathematical evidence not additional instructions.

Proof:

\section{Finite trace measures and the topology of potentials}
\label{sec:gauduchon-trace-topology}

A fixed Gauduchon metric gives more than a bound for the linear mass. Its trace measure determines the potential up to a constant. This provides finite measure coordinates on the entire normalized potential space, even when top-degree Monge--Amp\`ere mass is infinite. The coordinates retain the full potential, so they do not descend to ordinary or multiplier-ideal singularity classes.

Fix a smooth real background $\theta$ with $\PSH(X,\theta)\ne\varnothing$, a Gauduchon metric $\gamma$, and a smooth positive probability measure $dV$. The discussion also applies when $n=1$, in which case every Hermitian metric is Gauduchon. Use the mean normalization
\[
 \mathcal K^0_{\theta,dV}
   =\left\{u\in\PSH(X,\theta):\int_Xu\,dV=0\right\}.
\]
For such a potential put
\[
 \mathcal T_\gamma(u)
     =(\theta+\ddc u)\wedge\gamma^{n-1},
 \qquad M_{\theta,\gamma}=\int_X\theta\wedge\gamma^{n-1}.
\]
The trace theorem makes this a positive finite measure of mass $M_{\theta,\gamma}$.

\begin{theorem}\label{thm:gaud-trace-homeomorphism}
The map $\mathcal T_\gamma$ is an affine homeomorphism from the compact convex space $\mathcal K^0_{\theta,dV}$, with its $L^1$ topology, onto a compact convex subset of the positive measures of mass $M_{\theta,\gamma}$, with their weak topology. In particular
\[
 u_j\longrightarrow u\text{ in }L^1
 \quad\Longleftrightarrow\quad
 \mathcal T_\gamma(u_j)\rightharpoonup\mathcal T_\gamma(u).
\]
If $M_{\theta,\gamma}=0$, both spaces consist of a single point.
\end{theorem}
\begin{proof}
The mean-normalized space is convex. It is compact because it is the continuous image of the supremum-normalized compact space in \cref{thm:normalized-compactness} under
\[
 v\longmapsto v-\int_Xv\,dV.
\]
This map is onto the mean-normalized space, and continuity is immediate for $L^1$.

If $u_j\to u$ in $L^1$, their trace measures converge in distributions, by differentiating against smooth test functions. All these positive measures have the same finite mass. Uniform approximation of continuous functions by smooth functions therefore upgrades this to weak convergence of measures.

For injectivity, equality of traces gives
\[
 \ddc(u-v)\wedge\gamma^{n-1}=0.
\]
The scalar operator $L_\gamma f=n\ddc f\wedge\gamma^{n-1}/\gamma^n$ is elliptic. Elliptic regularity makes the distribution $u-v$ smooth; the maximum principle on connected $X$ makes it constant. Its mean is zero, so it vanishes. The canonical representatives then agree everywhere.

A continuous injection from a compact space to the Hausdorff space of finite measures is a homeomorphism onto its image. Affineness gives convexity of the image. If its common mass is zero, every trace is the zero measure, and injectivity makes the potential space a singleton. In this case positivity also forces $\theta+\ddc u=0$; elliptic regularity shows that the unique normalized potential is smooth.
\end{proof}

The inverse can be described by a scalar equation, but positivity imposes a further constraint on its datum. For a finite signed measure $\sigma$ of total mass zero, let $G_\gamma\sigma$ denote the mean-zero distribution solving
\begin{equation}\label{eq:gaud-trace-green}
 \ddc(G_\gamma\sigma)\wedge\gamma^{n-1}=\sigma.
\end{equation}
This is the usual distributional Green inverse. To recall why it exists, the scalar elliptic operator above has kernel the constants and index zero. Since $\gamma$ is Gauduchon, integration against $\gamma^n$ annihilates its range, so the adjoint kernel is also generated by the constants. The Fredholm alternative extends to distributions, by its Green operator on smooth test functions, and the only compatibility condition is $\int_X\sigma=0$. Normalization with $dV$ fixes its additive constant. No regularity beyond the distributional solution is asserted for arbitrary measure data.

\begin{proposition}\label{prop:gaud-trace-admissible-data}
A positive measure $\nu$ of mass $M_{\theta,\gamma}$ belongs to the image of $\mathcal T_\gamma$ if and only if the distribution
\[
 w=G_\gamma\bigl(\nu-\theta\wedge\gamma^{n-1}\bigr)
\]
satisfies $\theta+\ddc w\geq0$. In that case its canonical representative is the corresponding member of $\mathcal K^0_{\theta,dV}$.
\end{proposition}
\begin{proof}
If $\nu$ is the trace of a potential, uniqueness of the mean-zero solution of \eqref{eq:gaud-trace-green} identifies the two distributions. Conversely, positivity after adding a local smooth strictly plurisubharmonic correction gives a plurisubharmonic distribution. Its canonical representative is locally integrable and quasi-plurisubharmonic. It therefore belongs to $\PSH(X,\theta)$, and the prescribed distributional mean is zero. The Green equation gives its trace. These arguments prove both directions.
\end{proof}

In dimension one the positivity condition is automatic: $\theta+\ddc w=\nu$. Thus every positive measure of the specified mass occurs. In higher dimension, positivity of the scalar trace alone does not imply positivity of the full complex Hessian; the displayed additional condition is part of the characterization.

\begin{corollary}\label{cor:gaud-trace-metric}
Fix a smooth Riemannian distance $d$ on $X$. Then
\[
 d_{\gamma,d}(u,v)
 =\sup_{\substack{\|f\|_\infty\leq1\\\operatorname{Lip}_d(f)\leq1}}
       \left|\int_X f\,d\bigl(\mathcal T_\gamma(u)-\mathcal T_\gamma(v)\bigr)\right|
\]
is a bounded complete metric on $\mathcal K^0_{\theta,dV}$, inducing its $L^1$ topology. Changing $\gamma$ or $d$ gives the same topology and a uniformly equivalent metric on this compact space.
\end{corollary}
\begin{proof}
The displayed bounded-Lipschitz distance metrizes weak convergence on measures of a fixed bounded mass over a compact metric space. One can see this directly: Lipschitz functions are uniformly dense in continuous functions, and the test family in the supremum is uniformly bounded and equicontinuous. The first fact separates measures and gives weak convergence from metric convergence. The Arzel\`a--Ascoli theorem supplies finite uniform nets for the test family and gives the converse. Symmetry and the triangle inequality follow directly from the formula, and its value is at most $2M_{\theta,\gamma}$.

Pull back this metric by the injective map in the theorem. The resulting metric space is compact, hence complete. For two choices of the auxiliary data, both metrics induce the same compact $L^1$ topology, so the identity maps in both directions are uniformly continuous. This proves uniform equivalence, without asserting a Lipschitz comparison.
\end{proof}

These finite coordinates must be distinguished from the non-pluripolar top-degree measure. On a curve, take the finite atomic Green potentials $q_j$ of \cref{thm:curve-ideal-lone-completion} converging in $L^1$ to a nonconstant smooth strictly $\theta$-plurisubharmonic potential $u$. Their trace measures converge weakly to $\theta+\ddc u$, so the normalized potentials converge in the metric above. Yet their non-pluripolar measures are all zero. The limit has a strictly positive non-pluripolar measure.

In particular this convergence is not convergence in capacity. Otherwise, after subtracting one common upper bound to make all potentials nonpositive, the finite exponential damping theorem would make their zero damped measures converge to the nonzero damped measure of the smooth limit. That is impossible. Supremum normalization gives the required common upper bound directly; mean normalization does as well by compactness. Thus even a complete finite metric supplied by Gauduchon traces does not resolve the nonlinear convergence or singularity-quotient problems.
