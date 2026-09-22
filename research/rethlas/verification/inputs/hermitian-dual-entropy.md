Run_id: hermitian_dual_entropy_01

Statement: Verify the proposed Hermitian zero-reference entropy comparison below through the normal Rethlas workflow. This is a bounded candidate proof after checkpoint65, with no novelty claim. The objective is to identify the finite domain of the existing convex dual H_0 with finite relative entropy, on every compact Hermitian manifold, without either mass property. Check both directions of the conjugate inequalities, exponents and normalization factors, extended infinite values, dimension one, and uniformity in continuous logarithmic densities. Do not infer equality of the functionals or a fixed Lp bound.

Accepted internal inputs: on a Hermitian background omega and reference zero, for every continuous real G there is a bounded solution with measure exp(B_0(G)+G)dV; the scalar is unique and B_0 is Lipschitz for uniform norm (book/author/chapter_normalization.tex). The lower density estimate thm:lp-potential-estimate states that every normalized bounded omega-psh solution with density F in Lq has ||F||_q>=c_q>0 with c_q independent of F and the potential (section_weak_estimates.tex). For smooth G smooth strict solutions exist. A smooth Gauduchon gamma can be rescaled to integral omega wedge gamma^(n-1)=1 when n>=2; its Stokes trace is conserved; the matrix inequality gives Omega wedge gamma^(n-1)>=(Omega^n/gamma^n)^(1/n)gamma^n. The dual H_0(nu)=sup_{G continuous}[B_0(G)+integral G dnu] is finite only on absolutely continuous measures (thm:normalization-dual-compactness, section_normalization_dual.tex). The elementary entropy variational calculation for an absolutely continuous probability, including infinite entropy via logarithmic density truncations, is contained in the proof of prop:normalization-dual-entropy in the same file. That calculation concerns probability measures alone; do not apply the closed-background identity H=entropy to a nonclosed form. Dimension one uses the exact closed formula H_0=log(integral omega)+Entropy. dV is a smooth positive probability volume throughout the candidate proposition.

The candidate does not claim any regularity or exact Monge-Ampere result beyond its accepted inputs. It concerns H_0 only, not H_varphi for an arbitrary singular reference. Preserve the original verifier inputs, results, memory and reference files; use only the normal verifier workflow to save the new report.

Proof:

\section{Entropy bounds in a Hermitian background}

For a Hermitian background and reference zero, the dual functional need not equal entropy plus a constant. Its finite domain is nevertheless the finite-entropy domain.

\begin{proposition}\label{prop:hermitian-dual-entropy-bounds}
Let $\theta=\omega$ be Hermitian, let $\varphi=0$, and normalize $\mathrm{d}V(X)=1$. For every $q>1$ there is a finite real constant $a_q$, and there is a finite real constant $A$, such that every Borel probability measure $\nu$ satisfies
\[
 a_q+\frac1q\operatorname{Ent}_{\mathrm{d}V}(\nu)
 \leq H_0(\nu)
 \leq A+n\operatorname{Ent}_{\mathrm{d}V}(\nu).
\]
The inequalities include the value $+\infty$. Thus $H_0(\nu)<\infty$ if and only if $\nu$ has finite entropy. A family of probabilities has uniformly bounded $H_0$ if and only if its entropies are uniformly bounded. Neither mass property is assumed.
\end{proposition}
\begin{proof}
In dimension one the closed formula \eqref{eq:normalization-closed-formula} gives $H_0=\log\int_X\omega+\operatorname{Ent}_{\mathrm{d}V}$, so the assertions follow. Suppose $n\geq2$.

For $G\in C(X)$, apply \cref{thm:lp-potential-estimate} to a bounded solution with density $\mathrm{e}^{B_0(G)+G}$. It gives a constant $c_q>0$, independent of $G$, such that
\[
 B_0(G)\geq\log c_q-\frac1q\log\int_X\mathrm{e}^{qG}\,\mathrm{d}V.
\]
For the other bound, fix a smooth Gauduchon metric $\gamma$, rescaled so that $\int_X\omega\wedge\gamma^{n-1}=1$, and write
\[
 k_\gamma=\left(\frac{\gamma^n}{\mathrm{d}V}\right)^{(n-1)/n},
 \qquad m=\min_X k_\gamma>0.
\]
For smooth $G$, the smooth equation, matrix arithmetic--geometric mean and Stokes give
\[
 \mathrm{e}^{B_0(G)/n}\int_X\mathrm{e}^{G/n}k_\gamma\,\mathrm{d}V\leq1.
\]
Uniform approximation and continuity of $B_0$ extend this inequality to continuous $G$. Consequently
\[
 B_0(G)\leq-n\log m-n\log\int_X\mathrm{e}^{G/n}\,\mathrm{d}V.
\]

If $\nu$ is not absolutely continuous, \cref{thm:normalization-dual-compactness} gives $H_0(\nu)=+\infty$, and both displayed bounds have their asserted extended-value meaning. For an absolutely continuous probability, the elementary variational calculation in the proof of \cref{prop:normalization-dual-entropy} gives
\[
 \sup_{F\in C(X)}\left(\int_XF\,\mathrm{d}\nu
                 -\log\int_X\mathrm{e}^F\,\mathrm{d}V\right)
       =\operatorname{Ent}_{\mathrm{d}V}(\nu),
\]
including infinite entropy. This calculation is measure-theoretic and does not require a closed background. Add $\int_XG\,\mathrm{d}\nu$ to the two bounds for $B_0(G)$ and take suprema. The substitutions $F=qG$ and $F=G/n$ give the claim with $a_q=\log c_q$ and $A=-n\log m$. Fixing, for example, $q=2$ proves both assertions about finite domains and uniformly bounded families.
\end{proof}

In particular the compact dual sublevels of \cref{thm:normalization-dual-compactness} have uniformly bounded entropy in this Hermitian zero-reference regime. This does not identify $H_0$ with entropy, bound the probability densities in a fixed $L^p$ space, or extend the assertion to an arbitrary singular reference.
