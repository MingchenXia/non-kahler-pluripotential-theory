Run_id: elliptic_gauduchon_limits_01

Statement: Independently verify every assertion in the submitted short supplement, including the interpretation after the proposition. No novelty claim. Use the normal Rethlas sequential, reference and synthesis workflow.

Canonical inputs in /Users/mingchen/Non-Kahler: book/author/section_lower_mass_metric_geometry.tex supplies the quotient forms alpha,beta,D, their rank-one positivity, pairwise squares zero, ddc D=2 alpha wedge beta, omega=alpha+beta+D>0, integral alpha beta D=4pi, and Gauduchon convention ddc(gamma^2)=0. book/author/chapter_gauduchon_variational_volume.tex defines D_mu(gamma)=integral(mu/gamma^3)^(1/3) gamma^3 and proves thm:gaud-volume-dual-formula, including all minimizing Gauduchon metrics. research/editorial/section_elliptic_boundary_volume.tex supplies Omega_epsilon^3=24pi epsilon(a+epsilon)(b+epsilon) mu0 with mu0=omega^3/(24pi); its independent elliptic_boundary_volume_01 audit completed correct and may be inspected. Recheck the short wedge calculation if useful. No current-descent result is required.

Check the Gauduchon calculation, normalization I_epsilon, minimizing assertion, all four C-infinity limits, wedge annihilation, denominator formula and exponent, all coefficient-matrix ranks, the unbounded metric root on an edge, and the distinction between these fixed-density tests and the prior full-cone lower-mass concentration. In particular a rank-two positive (2,2)-form in dimension three need not have a finite semipositive (1,1) square root; verify the eigenvalue argument rather than applying strictly-positive Michelsohn root continuity at the boundary. No claim about arbitrary densities or arbitrary test families is intended.

Write only this run's memory/results and final response; preserve all submitted proofs, book sources, verifier installation and other audit records. Do not run Git. No approval or TLS bypass.

Proof:

\subsection{Limits of the minimizing Gauduchon forms}
\label{sec:elliptic-gauduchon-limits}

The boundary formula also permits an explicit description of its minimizing tests. Their normalized $(2,2)$-forms have smooth limits, although the corresponding metric roots need not remain bounded. We keep the forms and density of \cref{prop:elliptic-boundary-volume}.

\begin{proposition}\label{prop:elliptic-gauduchon-limits}
Let $a,b\geq0$, $\theta=a\alpha+b\beta$ and $\Omega_\epsilon=\theta+\epsilon\omega$. For every $\epsilon>0$, the metric $\Omega_\epsilon$ is Gauduchon. It minimizes the quotient defining $\lambda_{\mu_0}(\Omega_\epsilon)$. Put
\[
 I_\epsilon=8\pi\bigl(ab+2(a+b)\epsilon+3\epsilon^2\bigr),
 \qquad T_\epsilon=\frac{\Omega_\epsilon^2}{I_\epsilon},
 \qquad \gamma_\epsilon=\frac{\Omega_\epsilon}{\sqrt{I_\epsilon}}.
\]
Then $\int_X\omega\wedge T_\epsilon=1$, $\ddc T_\epsilon=0$ and $T_\epsilon=\gamma_\epsilon^2$. As $\epsilon\downarrow0$, the forms $T_\epsilon$ converge smoothly to
\[
 T_0=\begin{cases}
       (4\pi)^{-1}\alpha\wedge\beta,&a,b>0,\\
       (8\pi)^{-1}\alpha\wedge(\beta+D),&a>0,\ b=0,\\
       (8\pi)^{-1}\beta\wedge(\alpha+D),&a=0,\ b>0,\\
       (24\pi)^{-1}\omega^2,&a=b=0.
      \end{cases}
\]
In every case $\theta\wedge T_0=0$. If $q$ is the number of positive coefficients among $a,b$, the denominator of the normalized minimizing test satisfies
\[
 D_{\mu_0}(\gamma_\epsilon)
  =\frac{\bigl(24\pi\epsilon(a+\epsilon)(b+\epsilon)\bigr)^{2/3}}
         {I_\epsilon}
  \asymp\epsilon^{q/3},
\]
where the two comparison constants may depend on the fixed pair $(a,b)$.
\end{proposition}
\begin{proof}
Write $x=a+\epsilon$, $y=b+\epsilon$ and $z=\epsilon$. Since $\alpha^2=\beta^2=D^2=0$,
\[
 \Omega_\epsilon^2
   =2xy\alpha\wedge\beta+2xz\alpha\wedge D+2yz\beta\wedge D.
\]
The forms $\alpha,\beta$ are closed and $\ddc D=2\alpha\wedge\beta$. Applying $\ddc$ to each term makes its last two terms zero because they contain $\alpha^2$ or $\beta^2$. Thus $\ddc(\Omega_\epsilon^2)=0$. The zero potential solves the normalized equation for $\Omega_\epsilon$ and $\mu_0$, so the characterization of minimizing metrics in \cref{thm:gaud-volume-dual-formula} gives the minimizing assertion.

Fiber integration gives $\int_X\alpha\wedge\beta\wedge D=4\pi$. Hence
\[
 \int_X\omega\wedge\Omega_\epsilon^2
   =8\pi(xy+xz+yz)=I_\epsilon.
\]
This proves the trace normalization. Dividing the three coefficients in the preceding wedge expansion by $I_\epsilon$ gives each displayed limit, with convergence in every smooth norm since the forms are fixed. The identities $\alpha^2=\beta^2=0$ then give $\theta\wedge T_0=0$ in all four cases.

Set $c_\epsilon=24\pi\epsilon(a+\epsilon)(b+\epsilon)$. The equation gives
\[
 \gamma_\epsilon^3
    =\frac{c_\epsilon}{I_\epsilon^{3/2}}\mu_0.
\]
Substitution in the definition of $D_{\mu_0}$ and $\int_X\mu_0=1$ yield $D_{\mu_0}(\gamma_\epsilon)=c_\epsilon^{2/3}/I_\epsilon$. For fixed $(a,b)$ one has
$c_\epsilon\asymp\epsilon^{3-q}$ and $I_\epsilon\asymp\epsilon^{2-q}$. The quotient therefore has order $q/3$, as asserted.
\end{proof}

The limiting positive $(2,2)$-forms have coefficient-matrix ranks $1,2,3$ when $q=2,1,0$, respectively. This follows in a coframe adapted to the three rank-one forms $\alpha,\beta,D$ from the three complementary products in the proof. If $a,b>0$, the metric roots themselves converge smoothly to
\[
 \frac{a\alpha+b\beta}{\sqrt{8\pi ab}}.
\]
If $a>0$ and $b=0$, however, the coefficient of $\alpha$ in $\gamma_\epsilon$ grows as a positive constant times $\epsilon^{-1/2}$, while its other two coefficients tend to zero. Thus the roots are unbounded relative to the fixed metric $\omega$, although their squares converge smoothly. The same statement holds with $\alpha$ and $\beta$ interchanged. A rank-two positive $(2,2)$-form cannot be the square of a finite semipositive $(1,1)$-form in dimension three: the latter's eigenvalues give complementary pairwise products, whose possible nonzero ranks are three or one. At the vertex $a=b=0$, the normalized root instead stays equal to $\omega/\sqrt{24\pi}$.

For a nonzero boundary class, the smooth limiting test annihilates $\theta$ and its determinant denominator vanishes. No concentration of its coefficient measures occurs in this family. This degeneration of fixed-density minimizing tests is different from the sequence of Gauduchon forms used to prove zero lower mass in \cref{lem:lower-mass-unbounded-root}. At the vertex, the denominator remains positive; the order three comes entirely from scaling the background.
