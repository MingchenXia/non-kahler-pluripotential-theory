Run_id: reference_comparison_01

Run scope: This is one bounded mathematical verification through the normal Rethlas workflow. The parent process is actively editing and preparing the manuscript release. Restrict your writes to normal verifier runtime, memory and output tools. Leave book files, BLUEPRINT.md, research/STATUS.md, CHANGELOG.md, other editorial files and Git publication to the parent, to avoid concurrent changes. Never rewrite existing reports, frozen inputs or source references.

Statement: Check the proposed ordinary-type monotonicity, the explicit comparison with zero reference, the small-reference supporting-probability limit, and the analytic-envelope example below. This is an unintegrated candidate, with no novelty claim. Preserve all hypothesis boundaries: smooth semipositive big theta; model references with a genuine smaller-background envelope; logarithmic densities continuous; no BMP/PVP, no potential uniqueness assumed. In particular verify the signs of both strict-domination uses and the constant n log(1-epsilon). Check that uniform convergence of scalar functions holds on the entire unbounded Banach space C(X), since the bound is independent of the test function.

Accepted internal inputs:
- chapter_normalization.tex and chapter_prescribed_equations.tex: for every model reference phi=P_theta[phi] with P_{epsilon theta}(phi) genuine for some 0<epsilon<1, every continuous G has an ordinary-type solution with measure exp(B_phi(G)+G)dV and a unique positive scalar. Zero is such a reference for semipositive big theta. B_phi is finite, decreasing, translation covariant B(F+a)=B(F)-a, and one-Lipschitz on C(X). The singular strict-domination theorem is in section_singular_domination.tex. If a has a genuine smaller-background envelope, b preceq a, and MA(a)<=r MA(b) on {a<b}, r<1, then a>=b; arbitrary additive translations are allowed. Ordinary bounded equivalence transfers that envelope property.
- For P_{epsilon theta}(phi)+(1-epsilon)v with v bounded theta-psh, finite truncation levels of the first summand and positivity/homogeneity of the nonclosed bounded products give MA_theta^ext of the sum >= (1-epsilon)^n MA_theta(v) off the first summand's pole set. That pole set has zero smooth volume, sufficient for the claimed density bound. The same finite-level splitting was checked in prescribed_dual_entropy_01, and is proved directly in the earlier prescribed-existence arguments. Extended auxiliary measures may have infinite mass, and no infinite subtraction is allowed.
- section_normalization_dual.tex: H_phi(nu)=sup_G[B_phi(G)+integral G dnu], never minus infinity; at every supporting probability nu in A_phi(G), H_phi(nu)=B_phi(G)+integral G dnu. The supports are nonempty. For each fixed reference, every finite H_phi sublevel is compact for weak convergence of probability measures, its densities are uniformly integrable, and weak convergence on the sublevel also gives weak L1 convergence. This includes reference zero in the semipositive big background theta, and does not require theta to be strictly positive. The comparison corollary uses this H_0 compactness directly and does not require any new assertion about entropy.
- section_analytic_envelope_limits.tex, prop:analytic-envelope-type: if a is theta-psh with analytic singularities in any smooth real background, then a is ordinarily equivalent to P_theta[a]=Q_theta[a]. Ordinary-envelope invariance under bounded changes is elementary and proved in chapter_envelopes.tex. For theta semipositive, ta is theta-psh when 0<t<1, is t theta-psh, and after a<=0 is itself a competitor for P_theta[ta]. Therefore this analytic example, unlike an arbitrary unproved ordinary envelope, has the required model identity.

Check the claimed varying-reference limit only in the zero-reference limit with epsilon_j->0, 0<epsilon_j<1. No statement for arbitrary reference convergence, strong L1 convergence of probability densities, regular currents, uniform convergence of solution potentials, entropy-difference extrema of singular types or extra mass property is asserted. Check the displayed dual-minimization error bounded by delta_j=-n log(1-epsilon_j), the lower-semicontinuity passage, and the direct single-H_0-sublevel bound and the whole-sequence conclusion only under uniqueness of A_0(G).

The analytic example additionally identifies the limit with the smooth Gauduchon adjoint when theta is Hermitian and G is fixed smooth, by the already proved thm:normalization-gauduchon-recovery. This is weak L1 convergence, not strong L1 or total variation.

The analytic example will be placed after the analytic-envelope theorem in Chapter16. The comparison proposition and corollary will be in Chapter15 and use only preceding equation, positivity and dual results. Thus there is no forward circularity from the analytic example.

Proofs:

\subsection{Changing the prescribed singularities}

Keep the semipositive big background $\theta$ fixed, and use $B_0,H_0$ for its zero-reference functionals. A common smaller-background condition controls the change of normalization uniformly over all continuous logarithmic densities.

\begin{proposition}\label{prop:reference-normalization-comparison}
Let $\varphi,\psi$ satisfy \eqref{eq:normalization-reference}. If $\varphi\preceq\psi$, then $B_\varphi\leq B_\psi$ and $H_\varphi\leq H_\psi$. Moreover, if $P_{\varepsilon\theta}(\varphi)$ is genuine for $0<\varepsilon<1$, then
\[
 B_0(G)+n\log(1-\varepsilon)
       \leq B_\varphi(G)\leq B_0(G)
       \qquad(G\in C(X)),
\]
and
\[
 H_0(\nu)+n\log(1-\varepsilon)
       \leq H_\varphi(\nu)\leq H_0(\nu)
       \qquad(\nu\in\mathcal P(X)).
\]
The dual inequalities include infinite values.
\end{proposition}
\begin{proof}
Fix $G$, and let $u_\varphi,u_\psi$ solve the two ordinary-type equations, with scalars $c_\varphi,c_\psi$. Then $u_\varphi\preceq u_\psi$. If $c_\varphi>c_\psi$, singular strict domination applied to $u_\psi$ and $u_\varphi+t$ would give $u_\psi\geq u_\varphi+t$ for every real $t$, a contradiction at a common finite point. This proves the monotonicity of $B$, and its defining supremum gives the monotonicity of $H$. Since $\varphi\preceq0$, it also proves both upper bounds.

For the lower bound, let $v$ be the bounded solution for $G$, with scalar $c_0$, and put
\[
 h=P_{\varepsilon\theta}(\varphi)+(1-\varepsilon)v.
\]
The two currents in this sum have backgrounds $\varepsilon\theta$ and $(1-\varepsilon)\theta$, respectively. Positivity and homogeneity give
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(h)
       \geq(1-\varepsilon)^n\mathrm{MA}_\theta(v)
       =(1-\varepsilon)^nc_0\mathrm{e}^G\,\mathrm{d}V.
\]
As in the lower-density lemma, the inequality is justified first on finite levels and then off the pole set of $P_{\varepsilon\theta}(\varphi)$, which has zero smooth volume. Also $h\preceq u_\varphi$. If $c_\varphi<(1-\varepsilon)^nc_0$, strict domination would force $u_\varphi\geq h+t$ for every $t$. Thus $c_\varphi\geq(1-\varepsilon)^nc_0$. Taking logarithms proves the scalar bound; taking the defining suprema proves the dual bound.
\end{proof}

\begin{corollary}\label{cor:small-reference-adjoint-limits}
Let the model references $\varphi_j$ satisfy $P_{\varepsilon_j\theta}(\varphi_j)\not\equiv-\infty$, where $0<\varepsilon_j<1$ and $\varepsilon_j\to0$. Then $B_{\varphi_j}\to B_0$ uniformly on $C(X)$. If $G_j\to G$ uniformly and $\nu_j\in\mathcal A_{\varphi_j}(G_j)$, every weak cluster point belongs to $\mathcal A_0(G)$. The densities of $\nu_j$ are uniformly integrable, and weak convergence of a subsequence also holds weakly in $L^1(\mathrm{d}V)$. If $\mathcal A_0(G)$ is a singleton, the full sequence converges to it in these two senses.
\end{corollary}
\begin{proof}
Put $\delta_j=-n\log(1-\varepsilon_j)\to0$. The proposition gives $|B_{\varphi_j}-B_0|\leq\delta_j$ on all of $C(X)$. Its dual inequality and the supporting identity give
\[
 0\leq H_0(\nu_j)-\int_XG_j\,\mathrm{d}\nu_j-B_0(G_j)
       \leq\delta_j.
\]
Choose $M$ with $\|G_j\|_\infty\leq M$. This implies $H_0(\nu_j)\leq B_0(0)+2M+\delta_j$, so all $\nu_j$ lie in one compact dual sublevel. If a subsequence converges weakly to $\nu$, lower semicontinuity, uniform convergence of $G_j$ and continuity of $B_0$ give
\[
 H_0(\nu)-\int_XG\,\mathrm{d}\nu-B_0(G)\leq0.
\]
The dual minimum formula gives the opposite inequality and identifies equality with $\nu\in\mathcal A_0(G)$. The common-sublevel theorem \cref{thm:normalization-dual-compactness} also gives uniform integrability and weak $L^1$ convergence. Compactness and uniqueness of the limiting supporting probability give the last assertion.
\end{proof}

Analytic example:

If $\theta$ is also semipositive and big, this gives an explicit family to which \cref{prop:reference-normalization-comparison,cor:small-reference-adjoint-limits} apply. Normalize an analytic $a\in\PSH(X,\theta)$ by $a\leq0$, and set
\[
 \varphi_t=P_\theta[ta],\qquad 0<t<1.
\]
The proposition gives $\varphi_t\simeq ta$, so invariance under bounded changes gives $P_\theta[\varphi_t]=\varphi_t$. Moreover $ta\in\PSH(X,t\theta)$ and $ta\leq\varphi_t$, hence $P_{t\theta}(\varphi_t)$ is genuine. Consequently
\[
 \sup_{G\in C(X)}|B_{\varphi_t}(G)-B_0(G)|
       \leq-n\log(1-t)\longrightarrow0
       \qquad(t\downarrow0).
\]
The supporting probabilities have the limiting property stated in the corollary. When $\theta$ is Hermitian and $G$ is fixed and smooth, every choice in $\mathcal A_{\varphi_t}(G)$ therefore converges weakly in $L^1$ to the smooth Gauduchon adjoint probability, by \cref{thm:normalization-gauduchon-recovery}. This conclusion uses the proved model property of these analytic envelopes; no such property is presumed for an arbitrary ordinary envelope.
