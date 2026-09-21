Run_id: threshold_trace_saturation_01

Statement: Verify the research-only lemma and consequences below: extend the Gauduchon trace density inequality to all genuine Hermitian potentials using only a lower bound on their extended Monge-Ampere measure; prove positive trace-error measures vanish in total variation along smooth maximizing Gauduchon sequences; identify their trace limits under the root-tail hypothesis; and prove uniqueness up to constants of threshold subsolutions when a smooth strictly positive dual maximizer exists. No finite top-degree mass of subsolutions, exact equation for rough densities, regularity of a maximizing current, or wedge with a singular current is presumed.

Dependencies in /Users/mingchen/Non-Kahler: chapter_products.tex bounded positive mixed calculus and genuine truncations; section_bounded_subsolution.tex lem:nonclosed-mixed-density and its local freezing proof; chapter_gauduchon.tex Stokes trace and positive (n-1,n-1)-root; section_individual_density_subsolutions.tex attained threshold and Lp identification; section_integrable_gauduchon_tests.tex exact smooth-Gauduchon rho formula; section_weak_gauduchon_duality.tex current normalization and determinant k_T; research/editorial/section_root_uniform_tails.tex and section_integrable_gauduchon_currents.tex (submitted separately to root_tails_current_attainment_01) only for the last convergence paragraph. Treat those as conditional dependencies unless their separate audit has passed; inspect their exact scope. The trace inequality, total-variation error identity and smooth-dual rigidity do not depend on those new supplements.

The local input is Dinew, An inequality for mixed Monge-Ampere measures, Math. Z. 262 (2009), 1-15, DOI 10.1007/s00209-008-0356-z. Publisher metadata verified at https://link.springer.com/article/10.1007/s00209-008-0356-z (full text subscription only). The theorem locator is explicitly the available author's v1, https://arxiv.org/pdf/0705.0974v1, Theorem 1.2, PDF page2, as already specified in book/references.bib. It treats two bounded local psh functions and measurable Lebesgue densities. The manuscript uses no direct smooth matrix AMGM on an unbounded current; inspect the double freezing and linear weak limit carefully.

Check global/local fixed epsilon coverage, positivity when adding the quadratic corrections, top-degree lower densities, limiting polynomial measures, truncation locality, the pole-set contribution retained on the linear side, integrability of g^(1/n), Stokes normalization, roots and scaling of T, exact total-variation convention, no need for D0 in the error identity, and elliptic regularity for the distribution difference in the rigidity corollary. No novelty claim. Write only this run's verifier memory/results and final response. Preserve original submissions and source files; no Git or TLS/approval bypass.

Proof:

\subsection{Trace inequalities at the subsolution threshold}

A smooth Gauduchon test pairs with the full positive current $\omega+\ddc u$, even when the extended Monge--Amp\`ere mass of $u$ is infinite. The mixed inequality relates this finite linear pairing to the density threshold.

\begin{lemma}\label{lem:unbounded-gauduchon-trace-density}
Let $u\in\PSH(X,\omega)$ and $0\leq g\in L^1(\mathrm{d}V)$ satisfy
$\mathrm{MA}^{\mathrm{ext}}_\omega(u)\geq g\,\mathrm{d}V$. For every smooth Hermitian form $\gamma$,
\[
 (\omega+\ddc u)\wedge\gamma^{n-1}
       \geq(g\,\mathrm{d}V/\gamma^n)^{1/n}\gamma^n.
\]
The left side is the ordinary current paired with a smooth form; it retains any trace mass on the pole set of $u$.
\end{lemma}
\begin{proof}
We first verify the bounded version with two different smooth backgrounds. Suppose $w$ is bounded and $\mathrm{MA}_\omega(w)\geq q\,\mathrm{d}V$. On a sufficiently small coordinate ball centered at $x$, let $\kappa$ be the Euclidean form and put $\beta=\omega(x)$, $\eta=\gamma(x)$. Given $\varepsilon>0$, shrink the ball so that
\[
 \omega\leq\beta+\varepsilon\kappa\leq\omega+2\varepsilon\kappa,
 \qquad
 \gamma\leq\eta+\varepsilon\kappa\leq\gamma+2\varepsilon\kappa.
\]
Add to $w$ a quadratic potential of $\beta+\varepsilon\kappa$, and take a quadratic potential of $\eta+\varepsilon\kappa$. Both are bounded plurisubharmonic functions on the ball. Their top-degree measures dominate $q\,\mathrm{d}V$ and $\gamma^n$, respectively. The local mixed inequality used in \cref{lem:nonclosed-mixed-density}, namely \cite[Theorem 1.2]{Dinew09}, gives
\[
 (\omega_w+2\varepsilon\kappa)\wedge
             (\gamma+2\varepsilon\kappa)^{n-1}
 \geq(q\,\mathrm{d}V/\gamma^n)^{1/n}\gamma^n.
\]
For each $\varepsilon$ the small balls cover a fixed coordinate chart. The displayed measures depend polynomially on $\varepsilon$, with coefficients of locally finite variation. Let $\varepsilon\downarrow0$ to obtain the bounded inequality.

Translate $u$ to be nonpositive and put $u_k=\max(u,-k)$. By locality and positivity,
$\mathrm{MA}_\omega(u_k)\geq\mathbf1_{\{u>-k\}}g\,\mathrm{d}V$. Apply the bounded inequality to $u_k$. These functions converge to $u$ in $L^1$, so the linear currents $\omega+\ddc u_k$ converge to $\omega+\ddc u$, and their wedges with the fixed smooth $\gamma^{n-1}$ converge weakly. The right sides tend in $L^1$ to the asserted density: the pole set has zero smooth volume, and $g^{1/n}$ is integrable. Passing to the measure inequality proves the result. No convergence of the undamped top-degree measures was used.
\end{proof}

\begin{proposition}\label{prop:threshold-trace-saturation}
Let $0\leq f\in L^1$ be nonzero and $b=b_\omega(f)>0$, and write $p=f^{1/n}$. Suppose $u\in\PSH(X,\omega)$ satisfies $\mathrm{MA}^{\mathrm{ext}}_\omega(u)\geq bf\,\mathrm{d}V$. For every smooth strictly positive $T\in\mathscr G_\omega$, the measure
\[
 R_{u,T}=(\omega+\ddc u)\wedge T-b^{1/n}p k_T\,\mathrm{d}V
\]
is positive and has mass
\[
 R_{u,T}(X)=1-b^{1/n}D_p(T).
\]
In particular, if $(T_j)$ is a smooth maximizing sequence for $D_p$, then $\|R_{u,T_j}\|_{\mathrm{TV}}\to0$, uniformly over all such threshold subsolutions $u$.

If also $p\in\mathcal D_\omega^0$ and $T_j\to T$ as currents, then $T$ maximizes $D_p$ and
\[
 (\omega+\ddc u)\wedge T_j
       \rightharpoonup b^{1/n}p k_T\,\mathrm{d}V.
\]
This limiting probability depends on the chosen current limit $T$, but is independent of the threshold subsolution $u$ along the same sequence.
\end{proposition}
\begin{proof}
A smooth strictly positive $T$ is $\gamma^{n-1}$ for a Gauduchon metric $\gamma$. The normalization is $\int_X\omega\wedge T=1$. The preceding lemma proves positivity of $R_{u,T}$; distributional Stokes gives $(\omega+\ddc u)\wedge T(X)=1$. This proves the mass formula. Since $\rho_\omega(p)=b^{-1/n}$, a maximizing sequence makes this nonnegative mass tend to zero. It equals the total variation norm and is independent of $u$.

Under the tail hypothesis, the near-maximizer argument in the proof of \cref{prop:integrable-threshold-adjoints}, with $F=0$, gives
$p k_{T_j}\,\mathrm{d}V\rightharpoonup p k_T\,\mathrm{d}V$ and shows that $T$ maximizes. Add the error measures, which tend to zero in total variation. The resulting probability is $\nu_{T,0}$ of that proposition.
\end{proof}

The limiting formula is stated along smooth maximizing sequences. It does not define the product $(\omega+\ddc u)\wedge T$ for an arbitrary singular current $T$, or assert independence of the chosen maximizing current.

\begin{corollary}\label{cor:smooth-dual-threshold-rigidity}
If $D_{f^{1/n}}$ has a smooth strictly positive maximizer in $\mathscr G_\omega$, all subsolutions at the threshold $b_\omega(f)>0$ differ by constants. In particular, when $f$ is smooth and strictly positive, every threshold subsolution is a constant translate of the smooth solution of
$\mathrm{MA}_\omega(v)=b_\omega(f)f\,\mathrm{d}V$.
\end{corollary}
\begin{proof}
For a smooth strictly positive maximizing $T$, the preceding error measure has mass zero and therefore vanishes. Two threshold subsolutions $u,v$ satisfy $\ddc(u-v)\wedge T=0$. This is a homogeneous scalar elliptic equation with smooth coefficients. Elliptic regularity makes $u-v$ smooth, and the maximum principle on the connected compact manifold makes it constant. If $f$ is smooth and strictly positive, \cref{thm:gaud-volume-dual-formula} supplies the required maximizing Gauduchon form from the smooth solution. That solution is a threshold subsolution by \cref{prop:individual-normalizer-lp}.
\end{proof}
