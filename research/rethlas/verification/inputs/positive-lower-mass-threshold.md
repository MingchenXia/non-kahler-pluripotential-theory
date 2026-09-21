Run_id: positive_lower_mass_threshold_01

Statement: Check two short internal deductions in the submitted proof: (1) under positive lower mass, the coefficient of an envelope-class solution for any nonzero nonnegative L1 density is the maximal GLOBAL genuine-subsolution coefficient b_h(f), and every L1-convergent subsequence of normalized greatest exponential solutions converges in capacity to an exact solution at that coefficient; (2) a nef effective divisor present in a threshold subsolution for a root in D_omega^0 must have zero fixed-density Gauduchon variational volume. No BMP, uniqueness of zero-exponent potentials, convergence of the whole family without extraction, or equivalence of nef volume with bigness is claimed. No novelty claim is made: these are proposed syntheses and proof simplifications.

Read the precise internal dependencies under /Users/mingchen/Non-Kahler/book/author. For (1), section_general_measure_minimal.tex thm:general-measure-minimal gives both equations under v_-(theta)>0. chapter_relative_finite_measures.tex before thm:relative-finite-domination imposes positive lower mass, and cor:relative-finite-exponential-order permits the SECOND potential to be any genuine PSH more singular than the reference, while the FIRST is in the envelope class with finite measure. chapter_envelopes.tex prop:relative-elementary gives upward stability; do not use a converse from merely P_h[u]=0 outside BMP. section_individual_exponential_equations.tex supplies the greatest genuine subsolution and its already-proved scalar and total-variation limits at b>0. section_dominated_relative_compactness.tex thm:relative-fixed-measure-continuity upgrades L1 convergence under one fixed finite non-pluripolar dominator and positive lower mass. A Hermitian h with reference zero meets the semipositive-big/model/smaller-background standing hypotheses. Check all class and finiteness conditions carefully.

For (2), section_threshold_divisorial_constraints.tex prop:threshold-divisorial-constraint was separately audited by root_tail_divisorial_constraints_01, report research/rethlas/verification/results/root_tail_divisorial_constraints_01/verification.json with SHA25625ceaaa9f588e7e539fd2113c52a2c0000f9a37536fc37e0df41f0b9e6df0fc1. section_threshold_divisorial_geometry.tex cor:semipositive-divisor-exclusion was checked by threshold_divisorial_geometry_02, now correct with no errors/gaps; read the completed report and exact production proof. The checkpoint42 sources have been promoted but final packaging may still be in progress. Both audits completed with normal runner exit0. section_smooth_cone_duality.tex prop:nef-annihilator-determinant supplies determinant vanishing. section_integrable_gauduchon_currents.tex supplies D_p(T)=integral p k_T, with Gamma_0(T)=k_T dV. chapter_gauduchon_volume.tex and its nef-volume inputs define lambda_mu, its nonnegativity for nef backgrounds and invariance under smooth dd^c changes. The Hopf hyperplane class has zero variational volume as proved earlier; check that reference. Do not infer any product of singular currents.

The two proposed sources are research-only and are not included in the production book. Read their exact hypotheses and conclusions independently of generic pending-status descriptions in research/STATUS.md. Preserve every previous source, submission and verifier record. All cited items are internal already-developed results; expand their context and check the deduction, without certifying the entire book.

Proof:

\subsection{The maximal coefficient under positive lower mass}

For a Hermitian background, the preceding existence theorem identifies the scalar threshold introduced in \cref{sec:individual-density-subsolutions}. The comparison uses one solution in the envelope class and an arbitrary genuine subsolution.

\begin{corollary}\label{cor:positive-lower-mass-exact-threshold}
Let $h$ be Hermitian with $v_-(h)>0$, and let $0\leq f\in L^1(\mathrm{d}V)$ be nonzero. There is $v\in\mathcal E_{\mathrm{env}}(X,h,0)$ such that
\[
 \mathrm{MA}^{\mathrm{ext}}_h(v)=b_h(f)f\,\mathrm{d}V.
\]
The number $b_h(f)>0$ is the unique positive scalar for which this equation has a solution in that envelope class.

Let $u_\lambda$ be the greatest exponential solution from \cref{thm:individual-exponential-subsolution}, and set $v_\lambda=u_\lambda-\sup_Xu_\lambda$. Each $u_\lambda$ belongs to $\mathcal E_{\mathrm{env}}(X,h,0)$. If $\lambda_j\downarrow0$ and $v_{\lambda_j}\to v$ in $L^1$, then the convergence holds in capacity, $v$ belongs to the same envelope class and satisfies the displayed equation.
\end{corollary}
\begin{proof}
By \cref{thm:general-measure-minimal}, there are $c>0$ and $w\in\mathcal E_{\mathrm{env}}(X,h,0)$ with $\mathrm{MA}^{\mathrm{ext}}_h(w)=cf\,\mathrm{d}V$. If $s\in\PSH(X,h)$ satisfies $\mathrm{MA}^{\mathrm{ext}}_h(s)\geq af\,\mathrm{d}V$ with $a>0$, then
\[
 \mathrm{MA}^{\mathrm{ext}}_h(w)
       \leq\frac ca\,\mathrm{MA}^{\mathrm{ext}}_h(s).
\]
The first measure is finite, and every genuine $h$-plurisubharmonic $s$ satisfies $s\preceq0$. Thus the scalar assertion of \cref{cor:relative-finite-exponential-order}, with reference zero, gives $c/a\geq1$. Maximizing over subsolution coefficients yields $b_h(f)\leq c$. The reverse inequality holds because $w$ is itself a subsolution. The same argument identifies the scalar of every solution in this envelope class.

For $\lambda>0$, \cref{thm:general-measure-minimal} supplies an exponential solution $s_\lambda$ in the envelope class. The greatest-solution property gives $s_\lambda\leq u_\lambda$. Upward stability, \cref{prop:relative-elementary}, places $u_\lambda$ and its constant translate $v_\lambda$ in that class. Both $h$ and reference zero satisfy the hypotheses of the relative theory, since $P_{\varepsilon h}(0)=0$ for every $0<\varepsilon<1$.

Write $c_\lambda=\exp(\lambda\sup_Xu_\lambda)$. By \cref{cor:individual-positive-threshold-exponential}, $c_\lambda\to b_h(f)>0$ and
\[
 \mathrm{MA}^{\mathrm{ext}}_h(v_\lambda)
       =c_\lambda\mathrm{e}^{\lambda v_\lambda}f\,\mathrm{d}V
       \longrightarrow b_h(f)f\,\mathrm{d}V
       \quad\text{in total variation}.
\]
Since $v_\lambda\leq0$ and $c_\lambda$ stays bounded for small $\lambda$, these measures are dominated by one finite non-pluripolar measure $C f\,\mathrm{d}V$. Apply \cref{thm:relative-fixed-measure-continuity} to the stated $L^1$ convergent sequence. It gives class membership, capacity convergence and the displayed equation for its limit.
\end{proof}

Normalized compactness supplies such convergent subsequences. This does not assert uniqueness of the normalized zero-exponent potential or convergence of the whole family without extraction. It settles the exact threshold equation under positive lower mass, including the Hopf example without bounded mass. When $v_-(h)=0$, a positive individual threshold alone remains a different hypothesis.


\begin{corollary}\label{cor:nef-divisor-threshold-volume}
Let $0\leq f\in L^1(\mathrm{d}V)$ be nonzero, with $f^{1/n}\in\mathcal D_\omega^0$. Suppose a subsolution at $b_\omega(f)$ satisfies $\omega+\ddc u\geq[E]$ for an effective real divisor $E$ whose Bott--Chern class is nef. Then
\[
 \lambda_\mu(\beta_E)=0
\]
for every smooth positive probability measure $\mu$, where $\beta_E$ is any smooth closed representative of that class.
\end{corollary}
\begin{proof}
By \cref{prop:threshold-divisorial-constraint}, there is a maximizing current $T\in\mathscr G_\omega$ with $\int_X\beta_E\wedge T=0$. If $\lambda_\mu(\beta_E)>0$, \cref{prop:nef-annihilator-determinant} gives $\Gamma_0(T)=0$. It follows that $D_{f^{1/n}}(T)=0$, contradicting its positive maximal value. Since nefness gives $\lambda_\mu(\beta_E)\geq0$, the conclusion follows for each $\mu$.
\end{proof}

This criterion uses nefness and the variational volume, without requiring a smooth semipositive representative. It complements \cref{cor:semipositive-divisor-exclusion}: the Hopf hyperplane class has zero variational volume, yet its nowhere vanishing semipositive representative excludes a component at the threshold. Neither argument identifies positive nef volume with bigness or classifies all possible divisorial components.
