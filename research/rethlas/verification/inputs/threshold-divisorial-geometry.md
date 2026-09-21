Run_id: threshold_divisorial_geometry_01

Statement: Verify only the explicit smooth-approximation counterexample and semipositive-divisor exclusion corollary below, including the specialization to every nonnegative nonzero L1 density on the Hopf threefold. No claim that every divisor is semipositive, no all-current positivity for an arbitrary pseudoeffective class, no BMP, no arbitrary singular-current wedge, and no exact rough equation is made.

The immediate divisorial-constraint dependency is research/editorial/section_threshold_divisorial_constraints.tex in /Users/mingchen/Non-Kahler, with the completed bounded report /Users/mingchen/Non-Kahler/research/rethlas/verification/results/root_tail_divisorial_constraints_01/verification.json, SHA256 25ceaaa9f588e7e539fd2113c52a2c0000f9a37536fc37e0df41f0b9e6df0fc1. It returned correct with no errors or gaps. Read that exact report and its proof; the production book is still checkpoint41 and the new dependency is separately audited, not yet promoted. The tail-continuity supplement was checked in that same run but is not needed here.

Earlier production sources in /Users/mingchen/Non-Kahler/book/author: section_weak_gauduchon_duality.tex defines the compact set G_omega, trace measure sigma_T, matrix P_T with trace n, and Gamma_0; section_gauduchon_determinant_integrability.tex proves Gamma_0(T)=k_T dV for every normalized current; section_integrable_gauduchon_currents.tex gives supremum and maximizing-current conclusions on D_omega^0. section_gauduchon_metric_geometry.tex ex:gaud-metric-blowup proves exceptional self-intersection -1; chapter_hopf.tex describes alpha of rank two everywhere and cor:hopf-lower-mass gives positive lower mass; section_root_uniform_tails.tex gives D_omega^0=L^n under that property. section_divisorial_gauduchon_volume.tex provides divisorial removal/feasibility and the smaller coefficients 6(1-a)^2 on the Hopf model.

Check the surface bidegrees, closedness and trace normalization of [C]/integral_C omega; distinguish the smooth pairing beta_C wedge [C] from a product of two singular currents. Positivity of beta_E is essential for its zero total trace to force pointwise matrix degeneracy. Check the argument relative to sigma_T, then the absolute continuity of Gamma_0, and why f vanishing almost everywhere on {beta_E=0} makes p k_T vanish. The exclusion is only at the maximal global coefficient. For the Hopf specialization, verify both rank(alpha)=2 everywhere and PVP so that the root-space restriction is automatic for all L1 densities. Confirm that the previous residual equations at smaller constants do not contradict the exclusion. No novelty claim.

Write only this run's normal verifier memory/results and final report. Preserve original source files, submissions, old reports and verifier installation. No Git, TLS/approval bypass or memory edits.

Proof:

\begin{example}\label{ex:gauduchon-current-smoothing-obstruction}
The weak closure of smooth strictly positive normalized Gauduchon forms can be smaller than $\mathscr G_\omega$, even on a K\"ahler surface. Let $X$ be the blowup of $\mathbb P^2$ at one point and $C$ its exceptional curve. Fix a K\"ahler form $\omega$ and a smooth closed representative $\beta_C$ of $\{C\}$. Then
\[
 T_C=\frac{[C]}{\int_C\omega}\in\mathscr G_\omega,
 \qquad
 \int_X\beta_C\wedge T_C=\frac{-1}{\int_C\omega}<0.
\]
Every smooth strictly positive $T\in\mathscr G_\omega$ instead satisfies
$\int_X\beta_C\wedge T=\int_C T>0$.
\end{example}
\begin{proof}
The integration current $[C]$ is positive and closed, so its normalization belongs to $\mathscr G_\omega$. Its pairing with the smooth form $\beta_C$ is the self-intersection $C^2=-1$, computed in \cref{ex:gaud-metric-blowup}. For smooth $T$, the Poincar\'e--Lelong formula and $\ddc T=0$ give the second identity. The pairing with the fixed smooth $\beta_C$ is continuous under current convergence. It is therefore nonnegative on the weak closure of these smooth tests, which excludes $T_C$.
\end{proof}

\begin{corollary}\label{cor:semipositive-divisor-exclusion}
Assume $p=f^{1/n}\in\mathcal D_\omega^0$. Let $E$ be an effective real divisor whose class has a smooth semipositive representative $\beta_E$. If
\[
 \int_{\{\beta_E=0\}}f\,\mathrm{d}V=0,
\]
no subsolution at the threshold $b_\omega(f)$ satisfies $\omega+\ddc u\geq[E]$.
\end{corollary}
\begin{proof}
If such a subsolution existed, \cref{prop:threshold-divisorial-constraint} would supply a maximizing current $T\in\mathscr G_\omega$ with $\int_X\beta_E\wedge T=0$. In the matrix-density notation of \cref{sec:weak-gauduchon-duality}, write $B$ for the matrix of $\beta_E$. Positivity makes $\operatorname{tr}(BP_T)=0$ for $\sigma_T$-almost every point. Wherever $B\ne0$, this forces $P_T$ to be singular: a positive definite $P_T$ would have strictly positive trace against the nonzero positive semidefinite $B$. Thus $\Gamma_0(T)$ is supported on $\{\beta_E=0\}$. It equals $k_T\,\mathrm{d}V$ by \cref{thm:gaud-determinant-subcritical}. The hypothesis gives $p k_T=0$ almost everywhere, contradicting $D_p(T)=\rho_\omega(p)>0$.
\end{proof}

For example, the hyperplane divisor $H$ on the Hopf threefold has the smooth semipositive representative $\alpha$, which has rank two everywhere. By \cref{cor:hopf-lower-mass,prop:root-uniform-tails}, one has $\mathcal D_\omega^0=L^3$ on this example. Hence, for every nonzero nonnegative $L^1$ density, a threshold subsolution has zero generic divisorial coefficient along $H$. Otherwise divisorial removal, as in \cref{prop:divisorial-gaud-feasibility}, would give $\omega+\ddc u\geq a[H]$ for some $a>0$, contradicting the corollary applied to $aH$. This exclusion uses no bounded mass property. It is stronger here than nonbigness alone: the residual formulas of \cref{prop:hopf-divisorial-threshold} allow a positive coefficient along $H$ at smaller equation constants.
