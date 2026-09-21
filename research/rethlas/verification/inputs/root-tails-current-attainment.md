Run_id: root_tails_current_attainment_01

Statement: Independently verify the two research-only supplements below: bounded-root approximation and dominated convergence in D_h; extension of compact Gauduchon-current duality to integrable weights; attainment and uniformly integrable determinant-weighted measures for roots in the closure of bounded functions; and exact representation of the supporting probabilities of the logarithmic maximal subsolution threshold. Use normal sequential, reference and synthesis verification. No novelty claim. Do not assume an exact Monge-Ampere equation for the arbitrary L1 density.

Dependencies: /Users/mingchen/Non-Kahler/book/author/section_integrable_gauduchon_tests.tex and section_individual_density_stability.tex are checkpoint40, audited in integrable_gauduchon_tests_01: smooth Gauduchon supremum equals rho=b(|p|^n)^(-1/n), rho has triangle/solidity and complete Ln+rho norm, with no BMP/PVP hypothesis. section_individual_density_subsolutions.tex prop:individual-normalizer-lp identifies b with c for Lp data, p>1; section_weak_estimates.tex thm:lp-potential-estimate supplies uniform lower c_h(g)||g||Lp. section_weak_gauduchon_duality.tex defines the compact convex trace-normalized current set, the matrix determinant measures, their upper semicontinuity/concavity for positive continuous weights, equality with the smooth Gauduchon supremum, and the near-maximizer weighted-measure/adjoint argument. section_gauduchon_determinant_integrability.tex proves all determinant measures k_T dV are absolutely continuous and uniformly bounded in Lq, 1<q<n/(n-1), without either metric volume property. Inspect exact hypotheses and prior reports as needed.

Check carefully: closure in the stronger norm, not only Ln; signed truncations; convergence in measure dominated by an admissible root; subcritical exponents; extension from positive smooth weights to bounded measurable weights using uniform Lq bounds, not current smoothing; commutation of only suprema for arbitrary Ln weights; uniform tails are used exactly for upper semicontinuity/attainment; no infinity-minus-infinity; determinant concavity for matrix measures; multiplying by an unbounded measurable weight after absolute continuity; two-sign near-maximizer argument with the new class of weights; uniform Taylor remainder; separation direction; all scope boundaries and n=1 exclusion for the current section. No bounded density of all of D_h is asserted, no regular maximizing metric, no exact equation, no weak linearized operator and no prescribed-singularity extension.

Write only this run's verifier memory/results and final response. Preserve sources, immutable submissions and other run results. Do not run Git or use an approval/TLS bypass.

Proof:

\subsection{Approximation by bounded density roots}

The closure of bounded functions in $\mathcal D_h$ is described by a uniform tail condition. Denote this closed subspace by $\mathcal D_h^0$. For every $r>n$, the lower-density estimate in \cref{thm:lp-potential-estimate}, applied with exponent $r/n$, and \cref{prop:individual-normalizer-lp} give
\begin{equation}\label{eq:root-subcritical-bound}
 \rho_h(p)\leq C_r\|p\|_{L^r}\qquad(p\in L^r).
\end{equation}
The constant depends on $h$, the reference volume and $r$, but not on $p$.

\begin{proposition}\label{prop:root-uniform-tails}
For $p\in\mathcal D_h$, the following conditions are equivalent:
\begin{enumerate}
\item $p\in\mathcal D_h^0$;
\item $\rho_h(|p|\mathbf1_{\{|p|>K\}})\to0$ as $K\to\infty$;
\item whenever $|q_j|\leq|p|$ and $q_j\to0$ in measure, one has $\|q_j\|_{\mathcal D_h}\to0$.
\end{enumerate}
Equivalently, the second condition is
\[
 \sup_{\gamma\text{ Gauduchon}}
       L_{h,\gamma}(|p|\mathbf1_{\{|p|>K\}})\longrightarrow0.
\]
The space $\mathcal D_h^0$ is a closed order ideal. It contains $L^r$ for every $r>n$, and smooth functions are dense in it. If $v_-(h)>0$, then $\mathcal D_h^0=\mathcal D_h=L^n$.
\end{proposition}
\begin{proof}
Set $p_K=\operatorname{sgn}(p)\min(|p|,K)$. Then $|p-p_K|=(|p|-K)_+$ and
\[
 (|p|-K)_+\leq |p|\mathbf1_{\{|p|>K\}},\qquad
 |p|\mathbf1_{\{|p|>2K\}}\leq2(|p|-K)_+.
\]
The $L^n$ tails tend to zero. These inequalities show that the second condition is equivalent to $p_K\to p$ in $\mathcal D_h$. Conversely, if $a$ is bounded and $K\geq\|a\|_\infty$, then $(|p|-K)_+\leq|p-a|$. Approximation by bounded $a$ therefore proves the equivalence of the first two conditions.

Assume the second condition and let $q_j$ be as in the third. Fix $K$. On $\{|p|\leq K\}$, the functions $q_j$ are uniformly bounded and tend to zero in measure, hence in $L^{2n}$. Equation~\eqref{eq:root-subcritical-bound} makes the root norm of this part tend to zero. On the complementary set it is at most $\rho_h(|p|\mathbf1_{\{|p|>K\}})$. Let first $j$ and then $K$ tend to infinity. This proves $\rho_h(q_j)\to0$. The same split, or dominated convergence in measure, gives $\|q_j\|_{L^n}\to0$. Conversely, apply the third condition to $q_j=|p|\mathbf1_{\{|p|>j\}}$.

The Gauduchon version is \eqref{eq:integrable-gauduchon-root}. Solidity transfers the tail condition from $p$ to every function dominated by $|p|$, proving the order-ideal assertion. For $p\in L^r$, its bounded truncations converge in $L^r$, hence in $\mathcal D_h$ by \eqref{eq:root-subcritical-bound}. Bounded functions admit smooth $L^{2n}$ approximations, which converge in $\mathcal D_h$ by the same estimate; smooth functions are thus dense in the closure. Under positive lower mass, \cref{prop:individual-density-banach} identifies the $\mathcal D_h$ and $L^n$ norms up to equivalence, proving the last assertion.
\end{proof}

The metric comparisons in \cref{prop:individual-threshold-backgrounds} identify $\mathcal D_h^0$ for different Hermitian metrics. Its defining closure is therefore intrinsic to the compact complex manifold and the identification of density roots. The tail condition controls the scalar threshold under approximation: if $p_j\to p\ne0$ in $\mathcal D_h$, then
\[
 |\rho_h(p_j)-\rho_h(p)|\leq\rho_h(p_j-p)\longrightarrow0,
 \qquad b_h(|p_j|^n)\longrightarrow b_h(|p|^n)>0.
\]
It does not, by itself, give capacity convergence of equation potentials. When lower mass vanishes, equality of $\mathcal D_h^0$ and $\mathcal D_h$ remains a separate question.


\section{Integrable densities in the compact Gauduchon problem}
\label{sec:integrable-gauduchon-currents}

Retain $n\geq2$, the Hermitian background $\omega$ and the probability volume $\mathrm{d}V$. For $T\in\mathscr G_\omega$, write $\Gamma_0(T)=k_T\,\mathrm{d}V$ as in \cref{thm:gaud-determinant-subcritical}. If $p\geq0$ is measurable, define
\[
 D_p(T)=\int_Xp k_T\,\mathrm{d}V,
\]
allowing $+\infty$. For a smooth positive normalized Gauduchon form this is the test $L_{\omega,\gamma}(p)$. The space $\mathcal D_\omega^0$ from \cref{prop:root-uniform-tails} supplies a class of unbounded weights for which compactness still gives attainment.

\begin{theorem}\label{thm:integrable-current-attainment}
For every nonnegative $p\in L^n$,
\begin{equation}\label{eq:integrable-current-supremum}
 \sup_{T\in\mathscr G_\omega}D_p(T)=\rho_\omega(p),
\end{equation}
with $+\infty$ allowed. If $p\in\mathcal D_\omega^0$, the functional $D_p$ is finite, concave and weakly upper semicontinuous on $\mathscr G_\omega$. Its maximum is attained, and the measures $p k_T\,\mathrm{d}V$, as $T$ ranges over this set, have uniformly integrable densities.
\end{theorem}
\begin{proof}
For a smooth strictly positive $p$, \cref{thm:weak-gaud-compact-duality} applied to $F=n\log p$ proves \eqref{eq:integrable-current-supremum}. By \cref{thm:gaud-determinant-subcritical}, for every $r>n$,
\begin{equation}\label{eq:current-root-test-bound}
 \sup_{T\in\mathscr G_\omega}\int_X|q| k_T\,\mathrm{d}V
       \leq C_r\|q\|_{L^r}.
\end{equation}
Approximate a bounded nonnegative $p$ in $L^{2n}$ by smooth strictly positive functions. This estimate and \eqref{eq:root-subcritical-bound} give uniform convergence of the current functionals and convergence of the root norms. Thus the supremum formula holds for bounded $p$. Their current functionals are also upper semicontinuous and concave, by \cref{lem:weak-gaud-determinant-dual} and uniform convergence. For general $p\in L^n$, monotone truncation gives
\[
 \sup_T D_p(T)=\sup_T\sup_K D_{\min(p,K)}(T)
       =\sup_K\rho_\omega(\min(p,K))=\rho_\omega(p).
\]
Only two suprema have been interchanged; this step alone gives no attainment.

Now suppose $p\in\mathcal D_\omega^0$. By the supremum formula applied to the tail,
\[
 0\leq D_p(T)-D_{\min(p,K)}(T)
 \leq \rho_\omega(p\mathbf1_{\{p>K\}})\longrightarrow0
\]
uniformly in $T$. Hence $D_p$ is finite and a uniform limit of upper semicontinuous concave functionals. Compactness of $\mathscr G_\omega$ gives a maximizer. Finally, fix $1<q<n/(n-1)$. For every measurable $E$,
\[
 \sup_T\int_Ep k_T\,\mathrm{d}V
 \leq\rho_\omega(p\mathbf1_{\{p>K\}})
       +K C_q\,\mathrm{d}V(E)^{1-1/q}.
\]
Choosing first $K$ and then the volume of $E$ proves uniform absolute continuity. The total masses are bounded by $\rho_\omega(p)$, so the densities are uniformly integrable.
\end{proof}

A maximizing current is a finite positive $\ddc$-closed current. The theorem asserts neither a smooth minimizing Gauduchon metric nor an exact Monge--Amp\`ere solution at the subsolution threshold. These are different attainment questions.

\subsection{Supporting probabilities for an integrable density}

Let $f\in L^1$ be nonzero and nonnegative, and assume $p=f^{1/n}\in\mathcal D_\omega^0$. For a continuous real $F$, set
\[
 B_f(F)=\log b_\omega(e^Ff)
       =-n\log\rho_\omega(p e^{F/n}),\qquad
 M_f(F)=\rho_\omega(p e^{F/n}).
\]
Both quantities are finite and $M_f(F)>0$, by the order-ideal property. Let $\mathscr M_f(F)$ be the currents maximizing $D_{p e^{F/n}}$, and put
\[
 \nu_{T,F}=\frac{p e^{F/n} k_T}{M_f(F)}\,\mathrm{d}V
 \quad(T\in\mathscr M_f(F)).
\]
These are probability measures. Define $\mathcal A_f(F)$ to be all Borel probability measures satisfying
\begin{equation}\label{eq:integrable-threshold-support}
 B_f(G)\leq B_f(F)-\int_X(G-F)\,\mathrm{d}\nu
 \qquad(G\in C(X,\mathbb R)).
\end{equation}

\begin{proposition}\label{prop:integrable-threshold-adjoints}
The functional $B_f$ is concave, decreasing and $1$-Lipschitz for the uniform norm, and $B_f(F+a)=B_f(F)-a$ for constants $a$. Moreover,
\[
 \mathcal A_f(F)=\{\nu_{T,F}:T\in\mathscr M_f(F)\}.
\]
This set is nonempty, convex and weakly compact. Its measures are absolutely continuous. For each $R>0$, their densities, with $\|F\|_\infty\leq R$, are uniformly integrable. For $H\in C(X,\mathbb R)$, its one-sided derivatives satisfy
\[
 (B_f)'_+(F;H)=-\max_{\nu\in\mathcal A_f(F)}\int_XH\,\mathrm{d}\nu,
 \qquad
 (B_f)'_-(F;H)=-\min_{\nu\in\mathcal A_f(F)}\int_XH\,\mathrm{d}\nu.
\]
\end{proposition}
\begin{proof}
For each $T$, H\"older's inequality makes $F\mapsto\int_Xp e^{F/n}k_T\,\mathrm{d}V$ logarithmically convex. Taking suprema preserves the inequality defining logarithmic convexity. Thus $B_f=-n\log M_f$ is concave. Order and homogeneity give the translation rule and, by comparison with constant translates, the Lipschitz estimate.

We check the compactness needed to identify all supporting measures. Suppose $T_j\to T$ and $D_{p e^{F/n}}(T_j)\to M_f(F)$. Upper semicontinuity makes $T$ a maximizer. For a continuous real $H$, choose $\varepsilon>0$ with $1\pm\varepsilon H>0$. The weights $p e^{F/n}(1\pm\varepsilon H)$ lie in $\mathcal D_\omega^0$. Apply the preceding theorem to both weights and pass to any weak cluster point of $p e^{F/n}k_{T_j}\,\mathrm{d}V$. Its mass is $M_f(F)$, so the two signs force its integral against $H$ to equal that of $p e^{F/n}k_T\,\mathrm{d}V$. Hence the weighted measures converge. Matrix determinant concavity gives
\[
 p e^{F/n}k_{tT_1+(1-t)T_2}\,\mathrm{d}V
 \geq t p e^{F/n}k_{T_1}\,\mathrm{d}V
       +(1-t)p e^{F/n}k_{T_2}\,\mathrm{d}V.
\]
For two maximizing currents, equal total masses turn this into equality. The set $\mathscr N_f(F)$ of displayed probabilities is therefore nonempty, compact and convex.

A maximizing $T$ gives
\[
 M_f(G)\geq M_f(F)\int_Xe^{(G-F)/n}\,\mathrm{d}\nu_{T,F}.
\]
Jensen's inequality proves \eqref{eq:integrable-threshold-support}, so $\mathscr N_f(F)\subset\mathcal A_f(F)$. For the reverse inclusion, the derivative argument of \cref{thm:gaud-current-all-adjoints} applies with the finite measure $p k_T\,\mathrm{d}V$ in place of $k_T\,\mathrm{d}V$. Explicitly, uniform Taylor expansion gives
\[
 D_{p e^{(F+tH)/n}}(T)
 =D_{p e^{F/n}}(T)+\frac tn\int_X H p e^{F/n} k_T\,\mathrm{d}V+O(t^2),
\]
where the error is uniform in $T$ since $D_{p e^{F/n}}(T)\leq M_f(F)$. Testing maximizers at $F$ bounds the right derivative from below. Maximizers at $F+tH$ are near-maximizers at $F$, by the uniform multiplicative bounds, so the preceding convergence of weighted measures gives the reverse bound. Consequently
\[
 (B_f)'_+(F;H)=-\max_{\nu\in\mathscr N_f(F)}\int_XH\,\mathrm{d}\nu.
\]
Every $\nu\in\mathcal A_f(F)$ satisfies
$\int_XH\,\mathrm{d}\nu\leq\max_{\sigma\in\mathscr N_f(F)}\int_XH\,\mathrm{d}\sigma$ for all continuous $H$, by its supporting inequality. Separation from a compact convex set yields $\nu\in\mathscr N_f(F)$. Replacing $H$ by $-H$ proves the left-derivative formula.

Finally $M_f(F)\geq e^{-R/n}\rho_\omega(p)$ when $\|F\|_\infty\leq R$. Thus the displayed probability densities are at most $e^{2R/n}\rho_\omega(p)^{-1}p k_T$. The uniform integrability in the preceding theorem proves all the stated absolute-continuity assertions.
\end{proof}

When $f=1$, this is the zero-reference construction of \cref{chap:normalization}. For general $f$, the functional is defined by the maximal subsolution coefficient; it does not presume exact equation existence. No prescribed-singularity analogue is inferred from this Hermitian-background argument. Under positive lower mass, every nonnegative $L^1$ density satisfies the root-space hypothesis. Without that property, the uniform tail condition gives an explicit sufficient hypothesis for this compact dual description.
