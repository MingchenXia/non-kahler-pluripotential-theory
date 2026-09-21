Run_id: integrable_gauduchon_tests_01

Statement: Independently verify the submitted extension of the smooth Gauduchon variational formula to every nonnegative L1 density, including zero thresholds; metric/volume invariance and endpoint test norms; the resulting shorter semicontinuity and root-space proofs; and the equivalence of completeness for the root norm alone with finite upper mass. This is a research-only replacement exposition, not production content. The older independent upper-envelope and mixed-product proofs are preserved in individual_density_stability_01; do not edit that submission or its records. No novelty claim. Use the normal sequential, reference and synthesis workflow.

Canonical dependencies in /Users/mingchen/Non-Kahler: checkpoint39 book/author/section_individual_density_subsolutions.tex and passed report individual_density_subsolutions_01 establish the truncation threshold, its attained subsolution characterization, and scalar continuity for bounded densities under Lp convergence (proof of thm:smooth-tests-insufficient). book/author/chapter_gauduchon_variational_volume.tex thm:gaud-volume-dual-formula gives equality with the smooth normalization constant, with a smooth positive probability density, and Gauduchon attainment in that regime. book/author/section_gauduchon_volume_extrema.tex thm:gaud-volume-mass-extrema identifies the infimum/supremum of those constants with v_-/v_+, including v_+=infinity, by bounded exact regularization. Its lower-mass Gauduchon formula identifies endpoint coefficient norms. book/author/section_weak_estimates.tex thm:lp-potential-estimate has the uniform positive lower bound ||F||_Lp>=c_p for bounded normalized solutions; it does not assume BMP or positive lower mass. Continuous existence/compactness/scalar uniqueness are reconstructed in that file and chapter_weak_equations.tex. book/author/section_lower_mass_solvability.tex supplies obstructing densities when lower mass vanishes. The proof uses these exact inputs; inspect their hypotheses and existing reports as appropriate.

Pay particular attention to the nonlinear density/root exponents, cancellation of probability normalization, deriving uniform L^{2n/(2n-1)} coefficient bounds from the smooth p=2 density estimate by duality, passage to a bounded measurable root using L^{2n} convergence and L2 scalar continuity, and commuting only two suprema in the final monotone truncation. Do not replace this by a nonexistent uniform endpoint estimate. Check n=1 separately where needed, all zero/infinity conventions, metric comparisons and change of reference volume, lower semicontinuity/completeness of the stronger norm, and the incomplete-root-norm construction when v_+=infinity: positive partial sums Cauchy in rho have an L1 limit whose Ln norm is infinite. No all-class equation uniqueness, exact zero-exponent solution, or novel priority claim is made.

Write only this run's memory/results and final response. Preserve all submitted proofs, production sources, verifier installation and other run records. Do not run Git. No approval or TLS bypass.

Proof:

\section{Gauduchon tests for integrable densities}
\label{sec:integrable-gauduchon-tests}

The normalization constants of bounded truncations have an exact description by Gauduchon metrics. Fix a Hermitian form $h$ and a smooth positive probability volume $\mathrm{d}V$. For a nonnegative function $p$, set
\[
 L_{h,\gamma}(p)=
 \frac{\displaystyle\int_Xp
              (\mathrm{d}V/\gamma^n)^{1/n}\gamma^n}
      {\displaystyle\int_Xh\wedge\gamma^{n-1}},
\]
where $\gamma$ is Gauduchon. In dimension one every Hermitian metric is permitted and this quotient is $\int_Xp\,\mathrm{d}V/\int_Xh$.

For a real $p\in L^n(\mathrm{d}V)$, define
\[
 \rho_h(p)=b_h(|p|^n)^{-1/n}\quad(p\ne0),\qquad \rho_h(0)=0,
\]
with $0^{-1/n}=+\infty$. Each individual Gauduchon test is finite on $L^n$, since its coefficient relative to $\mathrm{d}V$ is smooth. Their supremum need not be finite.

\begin{theorem}\label{thm:integrable-gauduchon-formula}
For every real $p\in L^n(\mathrm{d}V)$,
\begin{equation}\label{eq:integrable-gauduchon-root}
 \rho_h(p)=\sup_{\gamma\text{ Gauduchon}}L_{h,\gamma}(|p|).
\end{equation}
Equivalently, for every nonzero nonnegative $f\in L^1(\mathrm{d}V)$,
\begin{equation}\label{eq:integrable-gauduchon-threshold}
 b_h(f)^{1/n}=
 \inf_{\gamma\text{ Gauduchon}}
 \frac{\displaystyle\int_Xh\wedge\gamma^{n-1}}
      {\displaystyle\int_X(f\,\mathrm{d}V/\gamma^n)^{1/n}\gamma^n}.
\end{equation}
The formulas allow $\rho_h(p)=+\infty$ and $b_h(f)=0$. No attainment of the infimum for a nonsmooth density is asserted.
\end{theorem}
\begin{proof}
It suffices to prove \eqref{eq:integrable-gauduchon-root} for $p\geq0$, since both sides depend only on $|p|$; the case $p=0$ is immediate. If $p$ is smooth and strictly positive, the smooth Gauduchon formula \cref{thm:gaud-volume-dual-formula}, with the density $p^n$ divided by its integral, gives
\[
 c_h(p^n)^{-1/n}=\sup_\gamma L_{h,\gamma}(p).
\]
The integral normalization cancels by homogeneity. Also $b_h(p^n)=c_h(p^n)$.

We need uniformity in $\gamma$ before approximating a measurable density. The lower-density estimate in \cref{thm:lp-potential-estimate}, with exponent two, gives a constant $a_h>0$ such that
\[
 c_h(p^n)\|p^n\|_{L^2}\geq a_h
\]
for smooth strictly positive $p$. Therefore
\begin{equation}\label{eq:gauduchon-test-uniform-bound}
 L_{h,\gamma}(p)\leq a_h^{-1/n}\|p\|_{L^{2n}}
 \quad\text{for every }\gamma.
\end{equation}
Positive smooth approximation and duality show that the smooth coefficient of each $L_{h,\gamma}$ has $L^{2n/(2n-1)}$ norm at most $a_h^{-1/n}$. In particular, the supremum of these functionals is Lipschitz on the positive cone of $L^{2n}$, with that same bound.

Now let $p\geq0$ be bounded and nonzero. Approximate it in $L^{2n}$ by smooth strictly positive $p_j$. Then $p_j^n\to p^n$ in $L^2$. The normalization constants converge:
\[
 c_h(p_j^n)\longrightarrow c_h(p^n)>0.
\]
Here the scalar continuity is the one proved at the start of \cref{thm:smooth-tests-insufficient}: the Gauduchon upper bound and the lower-density estimate bound the scalars above and away from zero, and uniform compactness followed by scalar uniqueness identifies their limit. The uniform bound \eqref{eq:gauduchon-test-uniform-bound} also gives
\[
 \sup_\gamma L_{h,\gamma}(p_j)
       \longrightarrow\sup_\gamma L_{h,\gamma}(p).
\]
The formula follows for bounded $p$.

For general nonnegative $p\in L^n$, put $p_k=\min(p,k)$. The definition of $b_h$ gives
\[
 \rho_h(p)=\lim_{k\to\infty}c_h(p_k^n)^{-1/n}
          =\sup_k\sup_\gamma L_{h,\gamma}(p_k).
\]
For each fixed $\gamma$, monotone convergence gives
$\sup_kL_{h,\gamma}(p_k)=L_{h,\gamma}(p)$. The two suprema commute, proving \eqref{eq:integrable-gauduchon-root}. Every denominator in \eqref{eq:integrable-gauduchon-threshold} is positive; taking reciprocals proves that formula, including the zero endpoint.
\end{proof}

For $n\geq2$, write $L_{h,\gamma}(p)=\int_Xp\,a_\gamma\,\mathrm{d}V$. Its coefficient satisfies
\[
 \|a_\gamma\|_{L^{n/(n-1)}}
 =\frac{(\int_X\gamma^n)^{(n-1)/n}}
        {\int_Xh\wedge\gamma^{n-1}}.
\]
Thus \cref{thm:gaud-volume-mass-extrema} identifies positive lower mass with a uniform bound for these endpoint norms. The weaker bound used above is available on every compact Hermitian manifold. It suffices to pass from smooth tests to bounded densities; monotone truncation then treats all integrable densities.

\begin{proposition}\label{prop:individual-threshold-backgrounds}
If $h_1,h_2$ are Hermitian and $m h_1\leq h_2\leq M h_1$ for positive constants $m,M$, then
\[
 m^n b_{h_1}(f)\leq b_{h_2}(f)\leq M^n b_{h_1}(f),
 \qquad
 M^{-1}\rho_{h_1}(p)\leq\rho_{h_2}(p)\leq m^{-1}\rho_{h_1}(p).
\]
If $h_2-h_1=\ddc a$ for a smooth real function $a$, their thresholds agree.
\end{proposition}
\begin{proof}
For every Gauduchon metric the numerators in \eqref{eq:integrable-gauduchon-threshold} satisfy the same bounds with factors $m,M$; the denominators agree. Taking the infimum and then the $n$th power proves the threshold bounds. Taking reciprocals gives the bounds for $\rho$, with the stated conventions at zero and infinity. In the last assertion, distributional Stokes makes the numerators equal.
\end{proof}

All Hermitian metrics on compact $X$ are comparable. Thus positivity of the individual threshold and the set of admissible density roots are independent of the chosen Hermitian metric. If the reference volume is replaced by $\mathrm{d}V'=a\,\mathrm{d}V$ with $a>0$ smooth, the same measure has density $f'=f/a$. The maximal-subsolution characterization gives $b'_h(f')=b_h(f)$, and $p\mapsto a^{-1/n}p$ preserves both the root functional and the $L^n$ norm. This identifies the construction under a change of reference volume.


\section{Stability of the subsolution threshold}
\label{sec:individual-density-stability}

Fix the Hermitian form $h$ and smooth positive probability volume $\mathrm{d}V$ as in \cref{sec:individual-density-subsolutions}. The threshold $b_h$ is upper semicontinuous for $L^1$ convergence. This gives a one-sided stability statement even when positive lower mass fails. Applied to the $n$th root of a density, it also defines a norm on the data admitting a positive scaled subsolution.

\begin{theorem}\label{thm:individual-threshold-semicontinuity}
Suppose $f_j,f$ are nonzero nonnegative $L^1$ densities and $f_j\to f$ in $L^1(\mathrm{d}V)$. Then
\[
 \limsup_{j\to\infty}b_h(f_j)\leq b_h(f).
\]
Moreover,
\begin{equation}\label{eq:individual-threshold-relaxation}
 b_h(f)=\lim_{\delta\downarrow0}\sup\{c_h(q):q\in L^\infty,\ q\geq0,\ q\not\equiv0,
                                      \ \|q-f\|_1<\delta\}.
\end{equation}
The suprema are finite for sufficiently small $\delta$.
\end{theorem}
\begin{proof}
Write $A_\gamma(f)=\int_X(f\,\mathrm{d}V/\gamma^n)^{1/n}\gamma^n$. For each fixed $\gamma$, H\"older's inequality and
$|s^{1/n}-t^{1/n}|\leq|s-t|^{1/n}$ show that $A_\gamma$ is continuous in $L^1$. It is positive at every nonzero nonnegative density. By \cref{thm:integrable-gauduchon-formula}, $b_h^{1/n}$ is the infimum of the continuous positive quotients $\int_Xh\wedge\gamma^{n-1}/A_\gamma(f)$. It is therefore upper semicontinuous. Testing one fixed $\gamma$ also bounds it above on an $L^1$ neighborhood of $f$.

For bounded $q$, $b_h(q)=c_h(q)$. The first assertion therefore bounds the upper limit of $c_h(q_j)$ along every bounded-density approximation $q_j\to f$. Conversely the canonical truncations of $f$ attain $b_h(f)$ in the limit. Local boundedness and these two observations prove \eqref{eq:individual-threshold-relaxation}.
\end{proof}

Consequently $b_h$ is continuous at each density where it vanishes. If $v_-(h)=0$, it is discontinuous at every density where it is positive: normalize the density, use the obstructing mixtures of \cref{cor:lower-mass-lone-instability}, and restore its integral. Thus the zero set is exactly the continuity set in that case. This statement concerns the scalar functional; it supplies neither capacity convergence of the original equation potentials nor equality of their limiting measures.

\subsection{Finite sums of densities}

Order and homogeneity give $b_h(f)\geq b_h(g)$ when $0\leq f\leq g$ and both are nonzero, and $b_h(tf)=t^{-1}b_h(f)$ for $t>0$. The root functional $\rho_h$ from \cref{sec:integrable-gauduchon-tests} expresses finite addition.

\begin{proposition}\label{prop:individual-root-triangle}
The functional $\rho_h$ is homogeneous, satisfies
$\rho_h(p)\leq\rho_h(q)$ whenever $|p|\leq|q|$, and obeys
\[
 \rho_h(p+q)\leq\rho_h(p)+\rho_h(q).
\]
In particular, if $b_h(f),b_h(g)>0$, then
\[
 b_h(f+g)\geq
       \bigl(b_h(f)^{-1/n}+b_h(g)^{-1/n}\bigr)^{-n}>0.
\]
\end{proposition}
\begin{proof}
The representation \eqref{eq:integrable-gauduchon-root} is a supremum of positive linear tests applied to $|p|$. It gives homogeneity, order, and the triangle inequality by $|p+q|\leq|p|+|q|$. Finally
$(f+g)^{1/n}\leq f^{1/n}+g^{1/n}$ gives the displayed density inequality.

\end{proof}

\begin{proposition}\label{prop:individual-density-banach}
The real vector space
\[
 \mathcal D_h=\{p\in L^n(\mathrm{d}V):\rho_h(p)<+\infty\}
\]
is complete for the norm $\|p\|_{\mathcal D_h}=\|p\|_{L^n}+\rho_h(p)$. It is an order ideal in $L^n$: if $q\in\mathcal D_h$ and $|p|\leq|q|$, then $p\in\mathcal D_h$. It contains $L^\infty$ and is therefore dense in $L^n$ for the $L^n$ norm.

Moreover, $\mathcal D_h=L^n$ if and only if $v_-(h)>0$. In that case its norm is equivalent to the $L^n$ norm. If $h$ is K\"ahler, then
\[
 \rho_h(p)=\left(\int_Xh^n\right)^{-1/n}\|p\|_{L^n}.
\]
\end{proposition}
\begin{proof}
The preceding proposition proves that $\mathcal D_h$ is a vector space and that the displayed expression is a norm. It also proves the order-ideal assertion. Bounded functions belong to $\mathcal D_h$ by continuous equation existence.

If $p_j\to p$ in $L^n$, then $|p_j|^n\to|p|^n$ in $L^1$. Upper semicontinuity of $b_h$ gives
\[
 \rho_h(p)\leq\liminf_j\rho_h(p_j).
\]
This includes $b_h(|p|^n)=0$, when the right side must be infinite; for $p=0$ the inequality follows from nonnegativity. Now let $(p_j)$ be Cauchy in $\mathcal D_h$. It converges in $L^n$ to some $p$. Lower semicontinuity, applied first to $p_j$ and then to $p_j-p_k$ as $k\to\infty$, gives $p\in\mathcal D_h$ and
\[
 \rho_h(p_j-p)\leq\liminf_{k\to\infty}\rho_h(p_j-p_k)\longrightarrow0.
\]
Together with $L^n$ convergence, this proves completeness.

If $v_-(h)>0$, \cref{prop:individual-normalizer-lp} gives
$\rho_h(p)\leq v_-(h)^{-1/n}\|p\|_{L^n}$, proving equality of the spaces and equivalence of the norms. If $v_-(h)=0$, take the obstructing density $f$ from \cref{thm:lower-mass-obstructing-measure}. Its root $f^{1/n}$ belongs to $L^n$ but not to $\mathcal D_h$. The K\"ahler formula follows from the same normalization proposition.
\end{proof}

Thus, when lower mass vanishes, the roots of densities admitting positive scaled subsolutions form a proper dense subspace of $L^n$, complete for the stronger displayed norm. Finite addition preserves admissibility. An infinite sum need not: the positive smooth summands in \cref{thm:lower-mass-obstructing-measure} already give an $L^1$ counterexample. Density of bounded functions in the $\mathcal D_h$ norm has not been asserted. The metric comparisons in \cref{prop:individual-threshold-backgrounds} show that this space is independent of $h$ and that its norms for different Hermitian metrics are equivalent.


\begin{proposition}\label{prop:individual-root-completeness}
The norm $\rho_h$ alone is complete on $\mathcal D_h$ if and only if $v_+(h)<+\infty$. When upper mass is finite,
\[
 \|p\|_{L^n}\leq v_+(h)^{1/n}\rho_h(p),
\]
so $\rho_h$ and $\|\cdot\|_{\mathcal D_h}$ are equivalent norms.
\end{proposition}
\begin{proof}
If $v_+(h)<+\infty$, every continuous solution for a bounded density $q$ satisfies
$c_h(q)\int_Xq\,\mathrm{d}V\leq v_+(h)$. Apply this to the truncations of $|p|^n$ and let the truncation level increase. It gives the displayed bound. Completeness follows from \cref{prop:individual-density-banach}.

Suppose instead that $v_+(h)=+\infty$. By \cref{thm:gaud-volume-mass-extrema}, the constants of smooth positive probability densities are unbounded above. For each $j$, choose such a density $f_j$ with
\[
 c_h(f_j)\geq(j2^j)^n,
 \qquad p_j=jf_j^{1/n}.
\]
Then $\|p_j\|_{L^n}=j$ and $\rho_h(p_j)\leq2^{-j}$. The positive partial sums $P_N=\sum_{j\leq N}p_j$ are Cauchy for $\rho_h$.

A fixed Gauduchon test has a smooth strictly positive coefficient, so \eqref{eq:integrable-gauduchon-root} gives $\rho_h(p)\geq c\|p\|_{L^1}$ with a constant $c>0$. Thus $\sum_jp_j$ converges in $L^1$ to a nonnegative function $P$. Were $P_N$ to converge for $\rho_h$ to an element of $\mathcal D_h$, that element would equal $P$ almost everywhere. But $P\geq p_j$ for all $j$, so $\|P\|_{L^n}\geq j$ for all $j$. This contradicts membership in $L^n$. Therefore $\rho_h$ is not complete.
\end{proof}

The two mass properties have separate roles: positive lower mass makes every $L^n$ root admissible, whereas finite upper mass makes the root norm control the $L^n$ norm. The norm $\|\cdot\|_{\mathcal D_h}$ is complete without either assumption.
