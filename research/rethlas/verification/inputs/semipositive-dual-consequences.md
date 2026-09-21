Run_id: semipositive_dual_consequences_01

Statement: Verify two short consequences of the already audited smooth semipositive dual theorem: independence of the Bott--Chern classes of divisors with positive generic Lelong number, and whole-family normalized L1 convergence of greatest exponential solutions, with an O(lambda) scalar bound and a common lower barrier. No novelty claim. These drafts are OUTSIDE the checked checkpoint49 book until this separate audit and root review finish.

Sources: research/editorial/section_semipositive_divisors.tex and section_semipositive_exponential_limit.tex under /Users/mingchen/Non-Kahler. They are frozen. The accepted theorem is book/author/section_semipositive_dual_attainment.tex, byte-identical to editorial v2, and its correct reports semipositive_dual_attainment_01 and semipositive_dual_uniqueness_01. Accept that theorem for existence, full exactness, smoothness off Z and uniqueness of ALL threshold subsolutions. It assumes n>=2, b>0 and a SMOOTH semipositive normalized dd^c-closed maximizing T strictly positive off a proper analytic Z. No root-tail, BMP or lower-mass condition is assumed.

Accepted earlier book inputs, whose precise statements should be read: lem:nonclosed-divisorial-removal in chapter_divisorial_models.tex; lem:constant-trace-bc-representative in section_continuous_bc_representatives.tex; lem:uniform-exponential in chapter_products.tex; thm:normalized-compactness in chapter_compactness.tex; cor:individual-positive-threshold-exponential and greatest exponential comparison in section_individual_exponential_equations.tex (locate exact filename if needed); the all-Hermitian trace test in the weak Gauduchon chapter and prop:threshold-trace-saturation. No need to reverify the whole book. Do not edit any source, verifier memory, or existing result.

Check divisors: positive pole divisors form a finite subset of components of Z. Divisorial removal gives a positive residual current even though omega is nonclosed. A real BC relation supplies an L1 real h with dd^c h=sum c_j[D_j]. For sufficiently small nonzero t all adjusted coefficients remain nonnegative; this produces a genuine omega-psh u+t h. Its current and equation agree off Z, and both non-pluripolar measures ignore Z. Uniqueness forces h constant and all c_j zero. No claim about every component of Z or a Zariski decomposition.

Check exponential limit: b^(1/n) p k_T dV is a probability with Ln density. Uniform normalized moments plus Holder give an expectation bound; Jensen applied to the integrated trace inequality yields b<=c_lambda<=b exp(C lambda). Greatest-solution comparison supplies u0-C<=v_lambda<=0. For any L1 cluster, lambda v_lambda tends to zero in measure and the exponential root densities converge in L1. Positive T-trace errors have mass tending to zero. Passing linear currents and all other smooth Hermitian trace inequalities identifies the cluster on X minus Z by the previously proved matrix/regularity argument; do not assume nonlinear MA continuity or that the cluster is a threshold subsolution before this step. Both measures ignore Z; global exactness then follows. Uniqueness with sup0 identifies every cluster. Check all constants, normalizations and the n>=2 Holder endpoint. Only L1 potential convergence is asserted, not capacity or uniform convergence at Z. Strict smooth T already gives uniform convergence by an earlier separate result.

Proofs:

\subsection{The classes of the divisorial components}

The uniqueness theorem has a consequence for the poles of its solution.

\begin{corollary}\label{cor:semipositive-dual-divisor-independence}
Under the hypotheses of \cref{thm:semipositive-dual-exact-equation}, let $u$ be its threshold solution and let $D_1,\ldots,D_k$ be the prime divisors with $\nu(u,D_j)>0$. Then the classes $\{D_j\}$ are linearly independent in $H^{1,1}_{\mathrm{BC}}(X,\mathbb R)$. In particular their number is at most $\dim_{\mathbb R}H^{1,1}_{\mathrm{BC}}(X,\mathbb R)$.
\end{corollary}
\begin{proof}
Smoothness off $Z$ shows that these divisors are among its finitely many divisorial components. Put $a_j=\nu(u,D_j)>0$. By \cref{lem:nonclosed-divisorial-removal},
\[
 R=\omega+\ddc u-\sum_j a_j[D_j]\geq0.
\]
Suppose $\sum_j c_j\{D_j\}=0$. Fix a Gauduchon metric $\eta$ and apply \cref{lem:constant-trace-bc-representative} to the integration currents. The linearity of its smooth representative on Bott--Chern classes gives
\[
 h=\sum_j c_j v_\eta([D_j])\in L^1(X),\qquad
 \ddc h=\sum_j c_j[D_j].
\]
Choose $t\ne0$ sufficiently small that $a_j+tc_j\geq0$ for every $j$. The distribution $u_t=u+th$ satisfies
\[
 \omega+\ddc u_t=R+\sum_j(a_j+tc_j)[D_j]\geq0,
\]
so it has a genuine $\omega$-plurisubharmonic representative. On $X\setminus Z$, the function $h$ is smooth and pluriharmonic. Thus $u_t$ has the same Monge--Amp\`ere measure as $u$ there. Both extended measures ignore $Z$, so $u_t$ is another threshold solution. Uniqueness makes $th=u_t-u$ constant. Hence $\sum_jc_j[D_j]=0$, and testing at a generic point of each distinct divisor gives $c_j=0$.
\end{proof}

The conclusion concerns divisors on which the solution has positive generic Lelong number. It imposes no independence condition on the other divisorial components of the degeneracy set.


\subsection{The limit of the exponential equations}

A smooth semipositive maximizing form also identifies the normalized exponential limit. The argument passes the linear trace inequalities to the limit before using the local regularity proof.

\begin{proposition}\label{prop:semipositive-dual-exponential-limit}
Assume the hypotheses of \cref{thm:semipositive-dual-exact-equation}, and let $u_0$ be its unique threshold solution with $\sup_Xu_0=0$. Let $u_\lambda$ be the greatest exponential solution of \cref{cor:individual-positive-threshold-exponential}, and put
\[
 v_\lambda=u_\lambda-\sup_Xu_\lambda,\qquad
 c_\lambda=\mathrm{e}^{\lambda\sup_Xu_\lambda}.
\]
There is a constant $C$ independent of $\lambda>0$ such that
\[
 b\leq c_\lambda\leq b\,\mathrm{e}^{C\lambda},\qquad
 u_0-C\leq v_\lambda\leq0.
\]
Moreover $v_\lambda\to u_0$ in $L^1(X)$ as $\lambda\downarrow0$.
\end{proposition}
\begin{proof}
Write $p=f^{1/n}$ and introduce the probability measure
\[
 \mathrm{d}\nu=b^{1/n}p k_T\,\mathrm{d}V.
\]
It has mass one because $T$ maximizes. Its density belongs to $L^n$, since $p\in L^n$ and the smooth semipositive form $T$ has bounded determinant density $k_T$. By \cref{lem:uniform-exponential}, normalized $\omega$-plurisubharmonic functions have uniformly bounded moments of every finite order. H\"older's inequality with exponents $n$ and $n/(n-1)$ therefore gives
\[
 \int_X(-v_\lambda)\,\mathrm{d}\nu\leq C.
\]
Here $n\geq2$ is used.

Apply the trace inequality to $u_\lambda$, or equivalently to $v_\lambda$, and pass from positive regularizations of $T$ to $T$ as in the preceding proof. After integration,
\[
 1\geq(c_\lambda/b)^{1/n}
       \int_X\mathrm{e}^{\lambda v_\lambda/n}\,\mathrm{d}\nu
 \geq(c_\lambda/b)^{1/n}\mathrm{e}^{-C\lambda/n},
\]
where the last step is Jensen's inequality. This proves the upper scalar bound. The lower bound and the comparison
\[
 v_\lambda\geq u_0-\lambda^{-1}\log(c_\lambda/b)
\]
are \cref{cor:individual-positive-threshold-exponential}, giving the asserted common lower barrier.

Take any sequence $\lambda_j\downarrow0$ and an $L^1$-convergent subsequence $v_{\lambda_j}\to v$, supplied by \cref{thm:normalized-compactness}. Its limit has supremum zero. The normalized $L^1$ bound implies $\lambda v_\lambda\to0$ in measure. Since $v_\lambda\leq0$ and $p\in L^1$, it follows that
\[
 c_\lambda^{1/n}\mathrm{e}^{\lambda v_\lambda/n}p
       \longrightarrow b^{1/n}p
       \quad\text{in }L^1(\mathrm{d}V).
\]
Put $A_\lambda=\omega+\ddc v_\lambda$. The positive trace errors
\[
 A_\lambda\wedge T
   -c_\lambda^{1/n}\mathrm{e}^{\lambda v_\lambda/n}p k_T\,\mathrm{d}V
\]
have masses tending to zero, since the two terms have total masses tending to one. The $L^1$ convergence of the potentials gives weak convergence of their linear currents. Consequently
\[
 (\omega+\ddc v)\wedge T=b^{1/n}p k_T\,\mathrm{d}V.
\]
For every smooth Hermitian form $\beta$, the all-Hermitian trace inequality passes to the same limit and gives
\[
 (\omega+\ddc v)\wedge\beta^{n-1}
   \geq(bf\,\mathrm{d}V/\beta^n)^{1/n}\beta^n.
\]
The local matrix and regularity argument in the proof of \cref{thm:semipositive-dual-exact-equation} now applies on $X\setminus Z$: it gives $\omega+\ddc v=a\gamma$, then smoothness, and then the exact equation there. Both extended measures ignore $Z$, so $v$ is a global threshold solution. Uniqueness and normalization give $v=u_0$.

Every sequence tending to zero has a subsequence with this same $L^1$ limit. Normalized compactness therefore proves convergence of the whole family.
\end{proof}

The conclusion is $L^1$ convergence with a fixed lower barrier. It does not assert capacity convergence or uniform convergence across the analytic degeneracy set. If the maximizing form is strictly positive everywhere, \cref{cor:smooth-dual-exponential-limit} already gives uniform convergence.
