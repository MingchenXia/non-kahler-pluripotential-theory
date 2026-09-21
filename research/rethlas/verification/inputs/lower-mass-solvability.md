Run_id: lower_mass_solvability_01

Statement: Check the complete attached proposed section, proving that v_-(h)>0 is equivalent to solvability up to a positive scalar for every finite nonzero non-pluripolar measure in a Hermitian background. The new direction constructs one L1 density, bounded below by a positive constant, which has no positive scaled subsolution of any singularity type if v_-(h)=0. Also check L1 density of the obstructing densities, the exclusion of all Lp with p>1 for the constructed density, and the exact limitation concerning exponential equations. No novelty claim is made. This is a bounded new mathematical deduction, not merely a request to accept the supplied lower-mass counterexample.

Conventions: X is smooth compact connected, h is a smooth strictly positive real (1,1)-form, not assumed closed. ddc=i/(2pi) partial bar-partial. A genuine psh function is not identically minus infinity. u preceq v means u<=v+C. MAext denotes the extended non-pluripolar measure, allowed infinite total mass. No bounded mass or uniform positive lower mass property may be assumed in the lemma or obstruction theorem.

Canonical prior inputs (all paths relative to /Users/mingchen/Non-Kahler; inspect their precise hypotheses):
1. book/author/section_singular_domination.tex, thm:singular-strict-domination. For theta smooth semipositive big, first potential U has a genuine smaller-background envelope, second V preceq U, and measure comparison with constant r<1 on {U<V}, the conclusion is U>=V. This is already proved without either metric volume property and for extended measures. Check orientation, all translations of the smooth potential, and all singularity/envelope assumptions carefully.
2. book/author/chapter_smooth_equations.tex, thm:tw-smooth: for a smooth strictly positive probability nu there is a smooth strict h-psh solution with positive scalar c_h(nu). No lower mass property is needed.
3. book/author/section_gauduchon_volume_extrema.tex, thm:gaud-volume-mass-extrema: the infimum of these smooth-density constants is v_-(h), defined using bounded potentials. Bounded-to-smooth approximation is part of its existing proof.
4. book/author/chapter_prescribed_equations.tex, thm:als-general-measure, with proof in book/author/section_general_measure_minimal.tex and section_general_measure_relative.tex: semipositive big theta, reference P_theta[phi]=phi admitting a smaller-background envelope, v_-(theta)>0; every finite nonzero non-pluripolar measure admits a positive-scaled solution in E_env, without BMP. For the sufficiency direction check phi=0 meets all hypotheses in Hermitian h. The theorem is an admitted prior input, not to be reproved in full.
5. book/author/chapter_weak_equations.tex, thm:kn-continuous: continuous solutions up to a positive scalar for any nonzero nonnegative Lp density, p>1, without either mass property. Only this precise existence conclusion is used to exclude Lp for the constructed density.
6. Classical elementary measure theory: monotone convergence for countably many positive densities; quasi-psh pole sets have zero smooth volume; every qpsh potential on a compact manifold has a finite upper bound; smooth strictly positive probability densities are L1 dense.

The closing geometric realization cites thm:vanishing-lower-mass, which is in the separate draft research/editorial/section_vanishing_lower_mass.tex under independent audit vanishing_lower_mass_01. Treat ONLY that one realization sentence as conditional on its result, and check that conditional implication. None of the core obstruction theorem, equivalence, or L1 instability uses that geometric construction. Report this dependency explicitly. Do not assume the new threefold proof is verified merely because it is cited.

Use the ordinary Rethlas sequential, reference, and synthesis workflow. All theorem inputs above are existing book sources, so inspect those local statements. No external reference is cited directly in the submitted proof. Write only this audit's memory/results and final response. Never edit a submitted source, production book, or another verifier record. Do not run Git or the synchronization script; the primary agent handles repository history. No approval or TLS bypass.

Proof:

\section{Lower mass and solvability for all measures}
\label{sec:lower-mass-solvability}

For a Hermitian background, positive lower mass has an exact interpretation in terms of equations. The distinction between a fixed smooth density and all non-pluripolar measures is essential. We first record a consequence of strict domination that applies even to potentials of infinite extended mass.

\begin{lemma}\label{lem:smooth-normalizer-subsolution-bound}
Let $h$ be a Hermitian form and let $\nu$ be a smooth strictly positive probability measure. Write
\[
 (h+\ddc v)^n=c_h(\nu)\nu,\qquad h+\ddc v>0,
\]
for its smooth normalized equation. If $u\in\PSH(X,h)$ and $a>0$ satisfy
\[
 \mathrm{MA}^{\mathrm{ext}}_h(u)\geq a\nu,
\]
then $a\leq c_h(\nu)$.
\end{lemma}
\begin{proof}
Suppose $a>c_h(\nu)$, and set $r=c_h(\nu)/a<1$. For every real $A$, the smooth potential $v+A$ admits a genuine envelope in background $h/2$: a sufficiently small constant lies below it. Also $u\preceq v+A$, since $u$ is bounded above and $v+A$ is bounded below on compact $X$. The measure inequality gives
\[
 \mathrm{MA}_h(v+A)=c_h(\nu)\nu
       \leq r\,\mathrm{MA}^{\mathrm{ext}}_h(u).
\]
Apply \cref{thm:singular-strict-domination}, with first potential $v+A$ and second potential $u$. It yields $v+A\geq u$ for every $A$. Letting $A\to-\infty$ at a point where $u$ is finite is a contradiction. No total mass of $u$ was used.
\end{proof}

\begin{theorem}\label{thm:lower-mass-obstructing-measure}
Suppose $v_-(h)=0$ for a Hermitian form $h$. Fix a smooth positive probability measure $\mathrm{d}V$. There is a probability measure $\mu=f\,\mathrm{d}V$ with $f\in L^1(\mathrm{d}V)$ and $f\geq m>0$ almost everywhere such that no $u\in\PSH(X,h)$ and $a>0$ satisfy
\begin{equation}\label{eq:lower-mass-impossible-subsolution}
 \mathrm{MA}^{\mathrm{ext}}_h(u)\geq a\mu.
\end{equation}
In particular, the equation $\mathrm{MA}^{\mathrm{ext}}_h(u)=c\mu$ has no solution for any $c>0$, even without a prescribed singularity type or a finite-mass requirement on the candidate potential.
\end{theorem}
\begin{proof}
By \cref{thm:gaud-volume-mass-extrema}, there are smooth strictly positive probability measures $\nu_j=f_j\,\mathrm{d}V$ such that
\[
 c_h(\nu_j)\leq 2^{-2j}\qquad(j\geq1).
\]
Set
\[
 \mu=\sum_{j=1}^{\infty}2^{-j}\nu_j,
 \qquad f=\sum_{j=1}^{\infty}2^{-j}f_j.
\]
Monotone convergence gives $\int_Xf\,\mathrm{d}V=1$. In particular $f$ is finite almost everywhere and belongs to $L^1$. Moreover
$f\geq\tfrac12\min_X f_1=:m>0$ almost everywhere. The measure is non-pluripolar because it is absolutely continuous with respect to smooth volume.

If \eqref{eq:lower-mass-impossible-subsolution} held, then for every $j$
\[
 \mathrm{MA}^{\mathrm{ext}}_h(u)\geq a2^{-j}\nu_j.
\]
The preceding lemma would imply $a2^{-j}\leq c_h(\nu_j)\leq2^{-2j}$. Thus $a\leq2^{-j}$ for all $j$, contradicting $a>0$.
\end{proof}

\begin{corollary}\label{cor:positive-lower-mass-solvability}
For a Hermitian form $h$, the following conditions are equivalent:
\begin{enumerate}
\item $v_-(h)>0$.
\item Every nonzero finite positive non-pluripolar measure $\mu$ admits $c>0$ and $u\in\mathcal E_{\mathrm{env}}(X,h,0)$ such that
$\mathrm{MA}^{\mathrm{ext}}_h(u)=c\mu$.
\item For every probability density $f\in L^1(\mathrm{d}V)$ bounded below by a positive constant, there are $u\in\PSH(X,h)$ and $a>0$ such that
$\mathrm{MA}^{\mathrm{ext}}_h(u)\geq af\,\mathrm{d}V$.
\end{enumerate}
Here $\mathrm{d}V$ is any fixed smooth positive probability measure. No upper mass bound is assumed.
\end{corollary}
\begin{proof}
For the reference zero, $P_h[0]=0$ and $P_{\varepsilon h}(0)=0$ for every $0<\varepsilon<1$. The form $h$ is semipositive and big. Thus (1) implies (2) by \cref{thm:als-general-measure}. Condition (2) implies (3), since an absolutely continuous measure is non-pluripolar. The preceding theorem proves the contrapositive of (3) implies (1).
\end{proof}

\begin{corollary}\label{cor:lower-mass-lone-instability}
Assume $v_-(h)=0$, and let $\mu=f\,\mathrm{d}V$ be the measure constructed above. Then $f\notin L^p(\mathrm{d}V)$ for every $p>1$. Moreover, for every nonnegative probability density $g\in L^1(\mathrm{d}V)$ and every $0<t<1$, the probability density
\[
 g_t=(1-t)g+tf
\]
admits no positive scaled subsolution as in \eqref{eq:lower-mass-impossible-subsolution}. Nevertheless $\|g_t-g\|_{L^1}\leq2t$. In particular, densities with this obstruction are dense among probability densities in $L^1$.
\end{corollary}
\begin{proof}
If $f\in L^p$ for some $p>1$, \cref{thm:kn-continuous} would give a continuous solution of $\mathrm{MA}_h(u)=cf\,\mathrm{d}V$ with $c>0$, contradicting the theorem. Since $g_t\,\mathrm{d}V\geq t\mu$, a positive scaled subsolution for $g_t\,\mathrm{d}V$ would give one for $\mu$. Finally
$\|g_t-g\|_1=t\|f-g\|_1\leq2t$.
\end{proof}

Smooth strictly positive probability densities are also dense in $L^1$ and always admit a smooth normalized solution. Thus ordinary $L^1$ approximation alone cannot preserve solvability when the lower mass vanishes. The obstruction concerns the concentration of the density; it occurs even when that density is bounded below by a positive constant. It is realized on the compact threefold of \cref{thm:vanishing-lower-mass}.

This argument does not exclude unbounded solutions of the exponential equation. If $\mathrm{MA}^{\mathrm{ext}}_h(u)=\mathrm{e}^{\lambda u}\mu$ with $\lambda>0$, the factor $\mathrm{e}^{\lambda u}$ need not have a positive lower bound. It does exclude bounded solutions for the measure above. Determining whether the exponential equation can absorb this concentration, and characterizing individual measures that admit a normalized solution when $v_-(h)=0$, are distinct questions.
