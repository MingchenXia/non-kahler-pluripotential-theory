Run_id: smooth_dual_sharpness_01

Statement: Verify the uniform zero-exponent convergence consequence under smooth dual attainment, the closed-background characterization of smooth strictly positive Gauduchon dual attainment, the explicit nonclosed Hermitian example with smooth maximizing test and density vanishing on an open set on every connected compact complex manifold of dimension at least two, and the dimension-one comparison. These are sharpness/exposition supplements to checkpoint45, not claims of novelty. Source: /Users/mingchen/Non-Kahler/research/editorial/section_smooth_dual_sharpness_v2.tex.

Accepted checked internal inputs: the local conformal-current lemma and smooth-dual exact-equation corollary in book/author/section_smooth_dual_regularity.tex, audited by smooth_dual_regularity_01 with report SHA256 fa0339b1ce62b6d403042adf5b0b06c61cb18ca4f92efc4266f1c01c7f4602bc; the proof gives omega+ddc u=a gamma with a smooth nonnegative and the first-order equation da=B-aC. When d omega=0, B=0. The integrable Gauduchon formula is in section_integrable_gauduchon_tests.tex, the maximal subsolution characterization and Kahler scalar formula in section_individual_density_subsolutions.tex, and the classical smooth strict-positive-density converse in chapter_gauduchon_variational_volume.tex. Check their exact scope and normalization. Gauduchon's theorem applies to every compact complex manifold, not just Kahler ones. The uniform compactness and cluster equation for Lp densities, p>1, are proved in section_symmetric_equation_selection.tex, prop:symmetric-equation-clusters; use its trivial-group case. Check that smooth dual attainment makes f smooth/nonnegative and hence bounded before invoking it, and that uniqueness of all threshold subsolutions then identifies every cluster limit. No convergence of the unnormalized family or rate is claimed.

Please check every item in source order. In particular, verify positivity propagation along paths from da=-aC; the existence of a smooth local negative Hessian cutoff extended to X; the two-region proof that omega=L chi gamma-ddc psi is strictly positive globally; nonzero f and vanishing on an open set; Stokes using ONLY ddc gamma^(n-1)=0; b>=1 from the explicit smooth subsolution and b<=1 from the same Gauduchon test; normalization of the current maximizer; the noncircular deduction of nonclosedness from the preceding closed-background characterization; and the degree-zero current comparison on a compact connected curve. There is no bounded mass or positive lower mass assumption. Do not import closedness of gamma in the example. Preserve all previous submissions, memory and results.

Proof:

\begin{corollary}\label{cor:smooth-dual-exponential-limit}
Under the hypotheses of \cref{cor:smooth-dual-exact-equation}, let $u$ be the threshold solution with $\sup_Xu=0$. If $u_\lambda$ is the unique bounded solution of
\[
 \mathrm{MA}_\omega(u_\lambda)=\mathrm{e}^{\lambda u_\lambda}f\,\mathrm{d}V,
 \qquad\lambda>0,
\]
then $u_\lambda-\sup_Xu_\lambda\to u$ uniformly as $\lambda\downarrow0$.
\end{corollary}
\begin{proof}
The preceding regularity corollary makes $f$ equal almost everywhere to a smooth function, so it belongs to $L^p$ for every finite $p$. The scalar of the bounded equation is $b_\omega(f)$ by \cref{prop:individual-normalizer-lp}. Thus \cref{prop:symmetric-equation-clusters}, with the trivial symmetry group, gives uniform precompactness and identifies every cluster limit as a normalized solution at this scalar. Each cluster limit is a threshold subsolution and hence equals $u$ by \cref{cor:smooth-dual-exact-equation}. If the whole family failed to converge uniformly, a sequence staying a fixed positive uniform distance from $u$ would have a convergent subsequence, a contradiction.
\end{proof}

\begin{corollary}\label{cor:kahler-smooth-dual-attainment}
Let $\omega$ be K\"ahler on a connected compact complex manifold of dimension $n\geq2$. For a nonzero nonnegative $f\in L^1(\mathrm{d}V)$, the functional $D_{f^{1/n}}$ has a smooth strictly positive maximizer in $\mathscr G_\omega$ if and only if $f$ agrees almost everywhere with a smooth strictly positive function.
\end{corollary}
\begin{proof}
The K\"ahler formula in \cref{prop:individual-normalizer-lp} makes $b_\omega(f)>0$. If a smooth strictly positive maximizer exists, the proof of \cref{cor:smooth-dual-exact-equation} gives
\[
 \omega+\ddc u=a\gamma,
 \qquad a\geq0,
\]
with $a,u$ smooth and $a\not\equiv0$. Since $\mathrm{d}\omega=0$, the first-order equation in \cref{lem:smooth-conformal-current} becomes $\mathrm{d}a=-aC$ for a smooth one-form $C$. Along any smooth path $\sigma$, this is the scalar equation
\[
 (a\circ\sigma)'=-(a\circ\sigma)C(\dot\sigma).
\]
Its solution is the initial value multiplied by a positive exponential. Connectedness therefore gives $a>0$ everywhere, and $f=b_\omega(f)^{-1}a^n\gamma^n/\mathrm{d}V$ is smooth and strictly positive. Conversely, the smooth equation and \cref{thm:gaud-volume-dual-formula} supply the maximizing Gauduchon form.
\end{proof}

The conclusion about strict positivity changes for a nonclosed background, even on a K\"ahler manifold.

\begin{example}\label{ex:nonclosed-dual-zero-density}
On every connected compact complex manifold of dimension $n\geq2$, there is a nonclosed Hermitian form $\omega$ and a nonzero smooth nonnegative density $f$ vanishing on an open set such that $b_\omega(f)=1$ and $D_{f^{1/n}}$ has a smooth strictly positive maximizer.
\end{example}
\begin{proof}
Fix a Gauduchon metric $\gamma$ and a point $x$. Choose a smooth real function $\psi$ such that $\ddc\psi\leq-\gamma$ on a coordinate neighborhood $U$ of $x$. One obtains it by multiplying $-M|z|^2$ by a cutoff that equals one near $x$, with $M$ large enough, and then shrinking $U$.

Choose a smooth function $\chi\geq0$ which vanishes on a smaller neighborhood of $x$, equals one outside $U$, and has values at most one. Since $X$ is compact, for sufficiently large $L>0$ the form
\[
 a=L\chi,\qquad \omega=a\gamma-\ddc\psi
\]
is strictly positive: on $U$ the second term is at least $\gamma$, and outside $U$ the term $L\gamma$ dominates $\ddc\psi$. Set $f=a^n\gamma^n/\mathrm{d}V$. The smooth potential $\psi$ satisfies $\omega+\ddc\psi=a\gamma\geq0$ and $\mathrm{MA}_\omega(\psi)=f\,\mathrm{d}V$, so $b_\omega(f)\geq1$.

Stokes and $\ddc\gamma^{n-1}=0$ give
\[
 \int_X\omega\wedge\gamma^{n-1}
 =\int_Xa\gamma^n
 =\int_X(f\,\mathrm{d}V/\gamma^n)^{1/n}\gamma^n.
\]
The Gauduchon formula \cref{thm:integrable-gauduchon-formula} gives the opposite inequality $b_\omega(f)\leq1$. The displayed test thus attains equality, and its normalized current is a smooth strictly positive maximizer. If $\omega$ were closed, the preceding corollary would force $f$ to be strictly positive, contrary to its vanishing on an open set. Thus $\omega$ is nonclosed.
\end{proof}

The restriction $n\geq2$ in \cref{cor:smooth-dual-exact-equation} is also necessary. On a compact connected Riemann surface, a normalized Gauduchon current has degree zero and is the constant $(\int_X\omega)^{-1}$: the equation $\ddc T=0$ makes it smooth and harmonic. This single smooth strictly positive current maximizes for every nonzero nonnegative $L^1$ density, which need not have a smooth representative.

In \cref{ex:nonclosed-dual-zero-density}, every genuine threshold subsolution is consequently a constant translate of $\psi$, and the normalized positive-exponent solutions converge uniformly to $\psi-\sup_X\psi$. Thus vanishing on an open set does not by itself force nonuniqueness or failure of this approximation.
