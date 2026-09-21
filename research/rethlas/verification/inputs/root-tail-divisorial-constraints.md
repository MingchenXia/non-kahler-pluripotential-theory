Run_id: root_tail_divisorial_constraints_01

Statement: Strictly verify the two supplements below. The first proves equivalence of the bounded-root closure, uniform integrability of all determinant-weighted Gauduchon tests, and sequential threshold continuity under every uniformly bounded smooth logarithmic perturbation converging in measure. It constructs smooth perturbations with an L1 density limit and a fixed threshold gap when tails fail. The second derives the quantitative coefficient loss c <= b(1-kappa)^n from a divisorial component, and describes annihilating smooth-test cluster currents at the maximal global threshold. Check claims as written without adding geometric realizability, exact-equation existence or unrestricted singular-current products.

The current production manuscript is checkpoint41,665 pages. Dependencies have completed bounded audits. Read their actual source hypotheses and reports; prior negative trace run01 is preserved and has been resolved by run02 on the identical mathematical payload, not treated as a pending dependency.

/Users/mingchen/Non-Kahler/research/rethlas/verification/results/root_tails_current_attainment_01/verification.json
SHA256 488d1ce7c37d28a181a8cd4f6f86ad3215a9a87ad5e1c6e166d74df478b79461
/Users/mingchen/Non-Kahler/research/rethlas/verification/results/threshold_trace_saturation_02/verification.json
SHA256 93ee0ce765b295afe55e0cdddd8852ae55f0fd5cde7db12e109239b9212f3bcd

Internal sources in /Users/mingchen/Non-Kahler/book/author:
- section_individual_density_subsolutions.tex: attained threshold and maximal genuine-subsolution coefficient;
- section_integrable_gauduchon_tests.tex: exact smooth-Gauduchon supremum for every nonnegative Ln root;
- section_individual_density_stability.tex and section_root_uniform_tails.tex: norm, order ideal, closure and dominated-convergence criterion;
- section_integrable_gauduchon_currents.tex: extended current supremum, UI on the bounded-root closure, and near-maximizer convergence;
- section_threshold_trace_saturation.tex: full-current trace inequality for genuine potentials, smooth-test error mass and limit;
- chapter_gauduchon.tex cor:gauduchon-threshold: kappa_omega(theta) is the infimum over smooth normalized Gauduchon tests and is positive precisely for big backgrounds;
- section_weak_gauduchon_duality.tex: compact convex current set and determinant weights; it does not presume smooth density of every current;
- chapter_bott_chern_loci.tex: ordinary closed class versus nonclosed background and bigness.

Pay attention to the order of the quantifiers on the perturbations (arbitrary fixed uniform bounds, not a predetermined small bound), selection of near-optimal SMOOTH tests for tails, regularity of the finite p k_T measure, compact sets inside measurable tails and small-volume open neighborhoods, smooth cutoffs, zero sets of p, and L1 convergence of the actual densities. For divisors use only pairing with smooth tests or a fixed smooth Chern representative; justify the additive trace mass on the smooth-volume-null divisor and every distributional Stokes application. Prove 0<=kappa<1 before taking powers. The face is deliberately only in the weak closure of smooth normalized Gauduchon forms, and only at c=b where nonemptiness is proved. Do not silently replace that closure by the full current set or infer that every maximizer is annihilating. No BMP or positive lower mass is assumed. No novelty claim.

Write only this run's normal verifier memory/results and final report. Preserve source files, original submissions, prior reports and the Rethlas installation. No Git, TLS bypass or memory editing.

Proof:

\subsection{The tail condition and perturbations of the density}

The tail condition also characterizes continuity under bounded multiplicative perturbations. This gives a converse to the uniform-integrability assertion in \cref{thm:integrable-current-attainment}.

\begin{proposition}\label{prop:root-tail-continuity}
Let $0\leq p\in\mathcal D_\omega$ be nonzero. The following are equivalent:
\begin{enumerate}
\item $p\in\mathcal D_\omega^0$;
\item the densities $p k_T$, for $T\in\mathscr G_\omega$, are uniformly integrable;
\item whenever $F_j$ are smooth real functions, uniformly bounded and tending to zero in measure, one has
\[
 b_\omega(\mathrm{e}^{F_j}p^n)\longrightarrow b_\omega(p^n).
\]
\end{enumerate}
If the first condition holds, the convergence in the third also holds for bounded measurable $F_j$ with the same uniform bound and convergence in measure. If it fails, there are smooth $F_j\geq0$, uniformly bounded and tending to zero in measure, such that
\[
 \mathrm{e}^{F_j}p^n\longrightarrow p^n\quad\text{in }L^1,
 \qquad
 b_\omega(\mathrm{e}^{F_j}p^n)\leq2^{-n}b_\omega(p^n).
\]
\end{proposition}
\begin{proof}
The first condition implies the second by \cref{thm:integrable-current-attainment}. Conversely, $\mathrm{d}V(\{p>K\})\to0$, so uniform integrability and \eqref{eq:integrable-current-supremum} give
\[
 \rho_\omega(p\mathbf1_{\{p>K\}})
 =\sup_{T\in\mathscr G_\omega}\int_{\{p>K\}}p k_T\,\mathrm{d}V
 \longrightarrow0.
\]
This is the first condition by \cref{prop:root-uniform-tails}.

If $p\in\mathcal D_\omega^0$ and $|F_j|\leq A$, then $p(\mathrm{e}^{F_j/n}-1)$ tends to zero in measure and its absolute value is at most $(\mathrm{e}^{A/n}+1)p$. The dominated-convergence criterion of \cref{prop:root-uniform-tails} makes its root norm tend to zero. The triangle inequality gives $\rho_\omega(p\mathrm{e}^{F_j/n})\to\rho_\omega(p)>0$. Taking negative $n$th powers proves the third condition, including measurable perturbations.

Suppose now that the tails do not tend to zero, and put $R=\rho_\omega(p)>0$. The smooth Gauduchon formula yields $\delta>0$, numbers $K_j\to\infty$ and smooth strictly positive $T_j\in\mathscr G_\omega$ such that
\[
 \int_{\{p>K_j\}}p k_{T_j}\,\mathrm{d}V>\delta.
\]
The finite measure $p k_{T_j}\,\mathrm{d}V$ is regular. Choose a compact set $C_j\subset\{p>K_j\}$ whose mass exceeds $\delta/2$, and an open neighborhood $O_j$ with
$\mathrm{d}V(O_j)\leq\mathrm{d}V(\{p>K_j\})+1/j$. Take a smooth cutoff $0\leq\chi_j\leq1$ that equals one on $C_j$ and is supported in $O_j$. Choose a fixed $A>0$ with $\mathrm{e}^{A/n}\delta/2>2R$, and set $F_j=A\chi_j$. Then $F_j\to0$ in measure, while
\[
 \rho_\omega(p\mathrm{e}^{F_j/n})
 \geq\int_Xp\mathrm{e}^{F_j/n}k_{T_j}\,\mathrm{d}V
 >2R.
\]
The threshold formula gives the asserted uniform gap. Finally,
$|\mathrm{e}^{F_j}-1|p^n\leq(\mathrm{e}^A-1)p^n\mathbf1_{O_j}$, whose integral tends to zero by absolute continuity of the integral. This proves the last assertion and the converse to the third condition.
\end{proof}

The criterion concerns all determinant-weighted Gauduchon tests. Failure of the tail condition does not, by itself, imply that a particular current maximum fails to exist or that a supporting probability is singular.


\subsection{Divisorial components of threshold subsolutions}

The linear Gauduchon threshold of \cref{cor:gauduchon-threshold} controls how much a divisorial component lowers the coefficient in a Monge--Amp\`ere inequality. Fix a Hermitian form $\omega$ on a connected compact complex manifold of dimension $n\geq2$, a smooth probability volume $\mathrm{d}V$, and a nonzero $0\leq f\in L^1(\mathrm{d}V)$. Write $p=f^{1/n}$ and $b=b_\omega(f)$.

\begin{proposition}\label{prop:threshold-divisorial-constraint}
Suppose $u\in\PSH(X,\omega)$ satisfies
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(u)\geq c f\,\mathrm{d}V,
 \qquad \omega+\ddc u\geq[E],
\]
where $c>0$ and $E$ is an effective real divisor. Let $\beta_E$ be a smooth closed representative of its Bott--Chern class, and put $\kappa=\kappa_\omega(\beta_E)$. Then $b>0$, $0\leq\kappa<1$ and
\begin{equation}\label{eq:divisorial-coefficient-loss}
 c\leq b(1-\kappa)^n.
\end{equation}
If $c=b$, every smooth maximizing sequence $(T_j)$ for $D_p$ satisfies
\[
 \int_X\beta_E\wedge T_j=\int_X[E]\wedge T_j\longrightarrow0.
\]
Every weak cluster current $T$ therefore satisfies $\int_X\beta_E\wedge T=0$, and the class of $E$ is not big. If also $p\in\mathcal D_\omega^0$, each such cluster current maximizes $D_p$.
\end{proposition}
\begin{proof}
The subsolution characterization gives $b\geq c>0$. For a smooth strictly positive normalized Gauduchon form $T$, \cref{lem:unbounded-gauduchon-trace-density} shows that
\[
 R=(\omega+\ddc u)\wedge T-c^{1/n}p k_T\,\mathrm{d}V
\]
is positive, with mass $1-c^{1/n}D_p(T)$. The density term gives no mass to the support of $E$, whereas $[E]\wedge T$ is supported there. Restricting the positive measure $R$ to that support and using $\omega+\ddc u\geq[E]$ gives
\[
 \int_X[E]\wedge T\leq R(X)=1-c^{1/n}D_p(T).
\]
Write $[E]=\beta_E+\ddc\ell_E$ by the Poincar\'e--Lelong formula. Since $\ell_E$ is locally integrable and $T$ is smooth and $\ddc$-closed, distributional Stokes identifies the left side with $\int_X\beta_E\wedge T$. It is nonnegative for every such test, so $\kappa\geq0$. Also $D_p(T)>0$, which gives $\kappa<1$. Taking the supremum of $D_p(T)$ and using $\rho_\omega(p)=b^{-1/n}$ proves \eqref{eq:divisorial-coefficient-loss}.

If $c=b$ and $(T_j)$ is maximizing, the right side of the preceding measure bound tends to zero. Pairing with the fixed smooth form $\beta_E$ is continuous under current convergence, proving the cluster assertion. Equation~\eqref{eq:divisorial-coefficient-loss} forces $\kappa=0$, so \cref{cor:gauduchon-threshold} excludes bigness. Under the tail hypothesis, the near-maximizer statement in \cref{prop:integrable-threshold-adjoints} makes every cluster a maximizing current.
\end{proof}

At the threshold $c=b$, if $E\ne0$, the vanishing pairing defines a nonempty proper exposed face of the weak closure of smooth strictly positive normalized Gauduchon forms. Indeed, this closure is compact and convex; the pairing with $\beta_E$ is continuous and nonnegative there, and it is strictly positive on every smooth strictly positive member. The proposition places every cluster of a smooth maximizing sequence on this face. This assertion concerns that closure; it does not assert that every normalized Gauduchon current is a limit of smooth ones. Nor does the smooth pairing $\int_X\beta_E\wedge T$ define $[E]\wedge T$ for a singular $T$.

These are necessary conditions on divisorial singularities at the maximal global coefficient. They do not apply unchanged to a smaller coefficient or to a threshold defined within a prescribed singularity type. Determining which annihilating currents occur, and whether these conditions can be supplemented to characterize the possible divisorial components, remains a geometric realization problem. No identification with a null locus or a non-K\"ahler locus is asserted.
