Run_id: individual_density_stability_01

Statement: Verify every assertion in the two submitted research supplements: upper L1 semicontinuity and relaxation of the individual-density threshold; its root-density triangle inequality, Banach space and lower-mass dichotomy; greatest exponential solutions from any genuine exponential subsolution; and their scalar/measure zero-exponent limits when b_h(f)>0. Use the normal sequential, reference, and synthesis workflow. These are pending drafts, not production book content. No novelty claim.

Canonical dependencies in /Users/mingchen/Non-Kahler: book/author/section_individual_density_subsolutions.tex (checkpoint39, passed audit individual_density_subsolutions_01) proves that b_h(f)=lim c_h(min(f,k)) is the attained maximal coefficient of an extended Monge--Ampere subsolution, with no BMP or lower-mass assumption. It also proves bounded normalizer order and scaling, Lp identification and Kähler normalization. book/author/chapter_weak_equations.tex and section_weak_estimates.tex reconstruct continuous Lp equations, exponential order, scalar uniqueness and uniform compactness. Their smooth Gauduchon bounds pass to a fixed bounded density by that same approximation. book/author/chapter_normalization.tex lemma lem:singular-convex-density is proved on common finite levels in a semipositive big background; h is Hermitian here. It uses section_bounded_subsolution.tex lem:nonclosed-mixed-density. book/author/section_singular_domination.tex thm:singular-strict-domination has first-potential smaller-background and second-potential singularity-order requirements, even for infinite extended measures. book/author/chapter_prescribed_equations.tex supplies thm:exponential-closedness and lem:normalized-exponential-npp; check all hypotheses and the constant translation in applying closedness. book/author/section_lower_mass_solvability.tex supplies the obstructing density and its L1-dense mixtures. book/author/chapter_damped_measures.tex thm:damped-continuity allows infinite undamped mass. These canonical dependencies and their existing bounded reports may be inspected; do not infer a global mass bound or a hidden full-mass assumption.

Check in particular: selection of bounded truncations for moving L1 densities; local uniform upper bounds for their normalizers from Gauduchon trace, including dimension one; infimum densities under upper envelopes and domination in the weighted passage; upper relaxation quantifiers; continuity/discontinuity set at zero lower mass; root-density exponent and convex coefficients; zero/infinite values and signed functions; completeness in the stronger norm, with no claim of bounded-function density in that norm; orientation of exponential comparison with a bounded first potential and arbitrary second potential; greatest among all genuine subsolutions without uniqueness in all singularity classes; common upper translation for closedness; positivity/nonzeroness in the normalized exponential limit; and no claim that scalar convergence gives an exact zero-exponent equation.

Write only this run's memory/results and final response. Preserve the submitted proofs, production book sources, verifier installation and all other audit records. Do not run Git. No approval or TLS bypass.

Proof:

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
We first record the upper bound used in the compactness argument. For $n\geq2$, fix a Gauduchon metric $\gamma$ and put
\[
 A(q)=\int_X(q\,\mathrm{d}V/\gamma^n)^{1/n}\gamma^n,
 \qquad H=\int_Xh\wedge\gamma^{n-1}.
\]
The proof of \cref{thm:kn-continuous}, by smooth approximation of the fixed bounded density $q$, gives
$c_h(q)^{1/n}A(q)\leq H$. Indeed the approximating constants converge to $c_h(q)$ by uniform compactness and uniqueness of the scalar. The inequality
$|s^{1/n}-t^{1/n}|\leq|s-t|^{1/n}$ and H\"older's inequality show that $A$ is continuous in $L^1$. Thus the constants are locally bounded above near any nonzero nonnegative $L^1$ density. For $n=1$, use $c_h(q)\int_Xq\,\mathrm{d}V=\int_Xh$ instead.

Choose sufficiently deep bounded truncations $q_j$ of $f_j$ such that
\[
 \|q_j-f_j\|_1\leq j^{-1},\qquad
 b_h(f_j)\leq c_h(q_j)\leq b_h(f_j)+j^{-1}.
\]
The preceding estimate bounds $c_h(q_j)$. Pass to a subsequence with
$c_h(q_j)\to a=\limsup_jb_h(f_j)$ and $q_j\to f$ almost everywhere. If $a=0$, there is nothing to prove. Otherwise choose continuous solutions
\[
 \mathrm{MA}_h(u_j)=c_h(q_j)q_j\,\mathrm{d}V,
 \qquad \sup_Xu_j=0,
\]
and extract again so that $u_j\to u$ in $L^1$ and almost everywhere, with $u$ genuine.

Use the upper-envelope construction in the proof of \cref{thm:individual-density-subsolution}, now with
\[
 w_j=\left(\sup_{\ell\geq j}u_\ell\right)^*,
 \qquad r_j=\inf_{\ell\geq j}c_h(q_\ell)q_\ell.
\]
Define $r_j=0$ on the common null exceptional set. Then $0\leq r_j\nearrow af$ almost everywhere. For each fixed $j$, $u_j\leq w_j\leq0$, and the finite-maximum inequality followed by bounded increasing continuity gives
$\mathrm{MA}_h(w_j)\geq r_j\,\mathrm{d}V$. Also $w_j\searrow u$ in capacity. Damped continuity and dominated convergence, using $r_j\leq af$, yield
\[
 \mathrm{e}^{u}\mathrm{MA}^{\mathrm{ext}}_h(u)
      \geq a\mathrm{e}^{u}f\,\mathrm{d}V.
\]
Divide on $\{u>-N\}$ and exhaust its complement of the pole set. Thus
$\mathrm{MA}^{\mathrm{ext}}_h(u)\geq af\,\mathrm{d}V$, and the maximality in \cref{thm:individual-density-subsolution} gives $a\leq b_h(f)$.

For bounded $q$, $b_h(q)=c_h(q)$. The first assertion therefore bounds the upper limit of $c_h(q_j)$ along every bounded-density approximation $q_j\to f$. Conversely the canonical truncations of $f$ attain $b_h(f)$ in the limit. Local boundedness and these two observations prove \eqref{eq:individual-threshold-relaxation}.
\end{proof}

Consequently $b_h$ is continuous at each density where it vanishes. If $v_-(h)=0$, it is discontinuous at every density where it is positive: normalize the density, use the obstructing mixtures of \cref{cor:lower-mass-lone-instability}, and restore its integral. Thus the zero set is exactly the continuity set in that case. This statement concerns the scalar functional; it supplies neither capacity convergence of the original equation potentials nor equality of their limiting measures.

\subsection{Finite sums of densities}

Order and homogeneity give $b_h(f)\geq b_h(g)$ when $0\leq f\leq g$ and both are nonzero, and $b_h(tf)=t^{-1}b_h(f)$ for $t>0$. To express addition, define for real $p\in L^n(\mathrm{d}V)$
\[
 \rho_h(p)=b_h(|p|^n)^{-1/n}\quad(p\ne0),\qquad \rho_h(0)=0,
\]
with $0^{-1/n}=+\infty$.

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
Homogeneity and order follow from the corresponding properties of $b_h$. For the triangle inequality it suffices to take nonnegative nonzero $p,q$ with finite $a=\rho_h(p)$ and $b=\rho_h(q)$; the other cases follow by order, or have infinite right side. Both $a,b$ are positive, since $b_h$ is finite on nonzero densities. The attained-threshold theorem gives $u,v\in\PSH(X,h)$ with
\[
 \mathrm{MA}^{\mathrm{ext}}_h(u)\geq(p/a)^n\,\mathrm{d}V,
 \qquad
 \mathrm{MA}^{\mathrm{ext}}_h(v)\geq(q/b)^n\,\mathrm{d}V.
\]
Apply \cref{lem:singular-convex-density} with coefficients $a/(a+b)$ and $b/(a+b)$. It gives
\[
 \mathrm{MA}^{\mathrm{ext}}_h\left(\frac{au+bv}{a+b}\right)
       \geq\left(\frac{p+q}{a+b}\right)^n\,\mathrm{d}V.
\]
Hence $\rho_h(p+q)\leq a+b$. For signed functions use $|p+q|\leq|p|+|q|$. Finally $(f+g)^{1/n}\leq f^{1/n}+g^{1/n}$ gives the displayed density inequality.
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

Thus, when lower mass vanishes, the roots of densities admitting positive scaled subsolutions form a proper dense subspace of $L^n$, complete for the stronger displayed norm. Finite addition preserves admissibility. An infinite sum need not: the positive smooth summands in \cref{thm:lower-mass-obstructing-measure} already give an $L^1$ counterexample. Density of bounded functions in the $\mathcal D_h$ norm has not been asserted.


\section{Exponential equations for an individual density}
\label{sec:individual-exponential-equations}

A positive subsolution threshold supplies a fixed lower bound for the bounded approximations to an exponential equation. Their monotonicity then gives the capacity convergence needed in \cref{thm:exponential-closedness}. We continue with a Hermitian background $h$ and a nonzero nonnegative density $f\in L^1(\mathrm{d}V)$.

\begin{theorem}\label{thm:individual-exponential-subsolution}
Fix $\lambda>0$. Suppose there is $s\in\PSH(X,h)$ such that
\[
 \mathrm{MA}^{\mathrm{ext}}_h(s)\geq\mathrm{e}^{\lambda s}f\,\mathrm{d}V.
\]
Then the equation
\[
 \mathrm{MA}^{\mathrm{ext}}_h(u_\lambda)
       =\mathrm{e}^{\lambda u_\lambda}f\,\mathrm{d}V
\]
has a greatest solution. More precisely, $u_\lambda$ is the greatest genuine $h$-plurisubharmonic subsolution of this equation, and its Monge--Amp\`ere measure is finite. It is the decreasing limit of the continuous solutions for $f_k=\min(f,k)$.
\end{theorem}
\begin{proof}
Let $u_k$ solve the continuous exponential equation for $f_k$, using \cref{thm:nguyen-exp}. The order lemma \cref{lem:exp-order} gives $u_{k+1}\leq u_k$.

Every genuine subsolution $v$ for $f$ lies below each $u_k$. Indeed, for $t>0$, on $\{u_k<v-t\}$ we have
\[
 \mathrm{MA}_h(u_k)=\mathrm{e}^{\lambda u_k}f_k\,\mathrm{d}V
 \leq\mathrm{e}^{-\lambda t}\mathrm{e}^{\lambda v}f\,\mathrm{d}V
 \leq\mathrm{e}^{-\lambda t}\mathrm{MA}^{\mathrm{ext}}_h(v-t).
\]
The first potential $u_k$ is bounded, so $P_{h/2}(u_k)$ is genuine and $v-t\preceq u_k$. Strict domination, \cref{thm:singular-strict-domination}, gives $u_k\geq v-t$. Let $t\downarrow0$.

In particular, $s\leq u_k\leq u_1$. Thus the decreasing limit $u_\lambda$ is genuine. Decreasing convergence is convergence in capacity, by the quasi-continuity and Dini argument used in \cref{thm:individual-density-subsolution}. Choose a common constant $A\geq\sup_Xu_1$. Apply \cref{thm:exponential-closedness} to $u_k-A$, with densities $\mathrm{e}^{\lambda A}f_k\to\mathrm{e}^{\lambda A}f$ in $L^1$. It proves the equation and finiteness of its left side. Finally every subsolution $v$ lies below all $u_k$, hence below $u_\lambda$, which is itself a subsolution.
\end{proof}

The extremal property makes this solution canonical. It does not exclude smaller solutions with other singularities. For $f\in L^p$, $p>1$, it agrees with the continuous solution: that solution gives a bounded lower barrier, and bounded exponential comparison gives uniqueness between the resulting bounded solutions.

\begin{corollary}\label{cor:individual-positive-threshold-exponential}
If $b=b_h(f)>0$, the preceding greatest solution exists for every $\lambda>0$. If $v\in\PSH(X,h)$ has $\sup_Xv=0$ and
$\mathrm{MA}^{\mathrm{ext}}_h(v)\geq bf\,\mathrm{d}V$, then
\[
 u_\lambda\geq v+\lambda^{-1}\log b.
\]
Writing
\[
 M_\lambda=\sup_Xu_\lambda,\qquad
 v_\lambda=u_\lambda-M_\lambda,\qquad
 c_\lambda=\mathrm{e}^{\lambda M_\lambda},
\]
we have
\[
 c_\lambda\longrightarrow b_h(f),\qquad
 \mathrm{e}^{\lambda u_\lambda}f\longrightarrow b_h(f)f
           \quad\text{in }L^1(\mathrm{d}V)
 \quad(\lambda\downarrow0).
\]
\end{corollary}
\begin{proof}
The attained-threshold theorem supplies $v$. Since $v\leq0$, the function $s=v+\lambda^{-1}\log b$ satisfies
\[
 \mathrm{MA}^{\mathrm{ext}}_h(s)\geq bf\,\mathrm{d}V
       \geq\mathrm{e}^{\lambda s}f\,\mathrm{d}V.
\]
The theorem gives $u_\lambda\geq s$, hence $c_\lambda\geq b$.

Set $g_\lambda=\mathrm{e}^{\lambda v_\lambda}f$. The normalized-exponential lemma \cref{lem:normalized-exponential-npp}, applied to the fixed finite measure $f\,\mathrm{d}V$, gives $g_\lambda\to f$ in $L^1$. Each $g_\lambda$ is nonzero, since a genuine quasi-plurisubharmonic function is finite almost everywhere. The equation for $u_\lambda$ implies
\[
 c_\lambda\leq b_h(g_\lambda)
\]
by the maximal subsolution characterization. Upper semicontinuity therefore gives
\[
 b\leq\liminf_{\lambda\downarrow0}c_\lambda
 \leq\limsup_{\lambda\downarrow0}c_\lambda
 \leq b_h(f)=b.
\]
This proves the scalar limit. Since $g_\lambda\to f$ in $L^1$, it also proves $c_\lambda g_\lambda\to bf$ in $L^1$.
\end{proof}

The right-hand-side measures therefore converge in total variation. The argument does not establish capacity convergence of the normalized potentials $v_\lambda$, so it does not yet solve the exact equation at $b_h(f)$. The lower bound becomes
\[
 v_\lambda\geq v-\lambda^{-1}\log(c_\lambda/b_h(f)),
\]
and convergence of $c_\lambda$ alone does not bound this error. Whether an exponential subsolution exists when $b_h(f)=0$ is a separate question; the theorem applies whenever such a subsolution can be constructed.
