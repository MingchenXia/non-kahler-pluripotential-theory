Run_id: integrable_infinite_mass_01

Statement: Verify the entire staged section on integrable complex Hessians and infinite Monge–Ampere mass. If BMP fails, the previously constructed convex series of smooth nonpositive omega-psh potentials has a positive current with L1 coefficients, smooth decreasing approximating currents converging in coefficient L1 with an explicit rate, infinite integral of its POINTWISE measurable determinant, and infinite extended MA. Verify domination of the pointwise determinant measure using only bounded truncations, not an assumed equality with the NPP measure. Verify the small strictly positive perturbation corollary, total-variation convergence of full Gauduchon traces and trivial multiplier ideals. No claim about real W2,1 regularity, equality of determinant and NPP measures, novelty, or smooth-mass monotonicity is permitted.

Already reconstructed and independently audited internal premises in /Users/mingchen/Non-Kahler/book/author:
1. chapter_products.tex, thm:infinite-mass-witness and its proof: failure of v_+(omega)<infinity supplies smooth omega-psh u_j<=0, sup u_j=0, with integral T_j^n >= 2^{j(n+1)}. For a_j=2^{-j}, U_N=sum_{j<=N} a_j u_j decreases to a genuine U in PSH(X,omega), in smooth-volume L1; integral exp(-pU) dV<infinity for EVERY p>0. The argument establishes extended MA(U)(X)=infinity and trivial multiplier ideals. The remaining tail has curvature lower bound -delta_N omega with delta_N=2^{-N}.
2. chapter_gauduchon.tex, prop:gauduchon-trace: for every genuine omega-psh potential v and fixed Gauduchon gamma, the FULL current trace (omega+ddc v) wedge gamma^{n-1} is a positive finite measure of the fixed mass M=int omega wedge gamma^{n-1}. This is not the degree-one NPP restriction. Smooth potentials in particular have this trace mass. Gamma exists by the earlier conformal theorem (dimension one is vacuous for failure of BMP).
3. chapter_products.tex: bounded products of positive smooth-background currents with bounded qpsh potentials are positive, multilinear and plurifinely local. The extended NPP measure is the increasing limit of 1_{v>-t}(omega+ddc max(v,-t))^n, with zero mass on every pluripolar set, possibly infinite total mass. If v is delta omega-psh with delta>0, max(v,-t) remains so. Smooth volume ignores pluripolar sets. Cor:bmp-characterization already proves MA_ext(omega,epsilon U)>=epsilon^n MA_ext(omega,U) using constant truncation and positive mixed products, with 0<epsilon<=1.
4. Standard elementary inputs: the order/norm/determinant properties of positive Hermitian matrices, monotone convergence for positive measures including extended measures, and distributional convergence under L1 convergence of potentials.

This is a deduction from internal proved results, not an application of a new external theorem. Check the exact factor 1/n in the coefficient norm, identification of the pointwise matrix sum with the full distributional current, L1 tail estimates, positivity of the delta_N background, the direction V_N>=U on the untruncated set, exhaustion past poles, determinant monotonicity/measure domination on Borel sets, and the quantifiers N>=j proving divergence without monotonicity. Follow the normal sequential Rethlas workflow. Do not edit the staged TeX or manuscript. Persist all findings and the final verification JSON, then stop.

Proof:

\section{Integrable Hessians and infinite mass}
\label{sec:integrable-infinite-mass}

The construction in \cref{thm:infinite-mass-witness} has a stronger linear convergence property. Its limiting current has integrable coefficients, and the smooth approximating currents converge in the coefficient $L^1$ norm. Nevertheless their determinant masses tend to infinity. Thus the obstruction is already present for an ordinary measurable matrix of integrable coefficients.

Fix a Gauduchon metric $\gamma$ and put
\[
 M=\int_X\omega\wedge\gamma^{n-1}.
\]
For a real $(1,1)$-form $T$ with measurable coefficients, let $A_T$ be its Hermitian matrix relative to $\gamma$, and use the norm
\[
 \|T\|_{L^1(\gamma)}
 =\frac1n\int_X\operatorname{tr}|A_T|\,\gamma^n.
\]
For $T\geq0$ this equals $\int_XT\wedge\gamma^{n-1}$. Any smooth background norm gives the same space of integrable coefficients on compact $X$. We write $\det_\gamma T=\det A_T$, defined almost everywhere when the coefficients are integrable.

\begin{proposition}\label{prop:integrable-infinite-mass}
Suppose $v_+(\omega)=+\infty$. The potential $U$ and smooth decreasing approximants $U_N$ in the proof of \cref{thm:infinite-mass-witness} satisfy the following additional conclusions. The positive current $T=\omega+\ddc U$ has integrable coefficients, and
\[
 \|\omega+\ddc U_N-T\|_{L^1(\gamma)}
 \leq2^{1-N}M.
\]
Its pointwise determinant satisfies
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(U)
 \geq (\det_\gamma T)\gamma^n,
 \qquad
 \int_X(\det_\gamma T)\gamma^n=+\infty.
\]
Moreover,
\[
 \int_X(\omega+\ddc U_N)^n\longrightarrow+\infty.
\]
The determinant measure in the statement is allowed infinite mass; equality with the non-pluripolar measure is not required.
\end{proposition}
\begin{proof}
Use the notation of that construction:
\[
 a_j=2^{-j},\quad T_j=\omega+\ddc u_j\geq0,\quad
 U_N=\sum_{j\leq N}a_ju_j\downarrow U,\quad
 \int_XT_j^n\geq2^{j(n+1)}.
\]
Every $u_j$ is smooth and nonpositive. Put
\[
 S_N=\sum_{j\leq N}a_jT_j,\qquad
 \delta_N=\sum_{j>N}a_j=2^{-N}.
\]
The smooth positive matrices $S_N$ increase pointwise. The Gauduchon identity gives
\[
 \int_XS_N\wedge\gamma^{n-1}=(1-\delta_N)M.
\]
Monotone convergence of their traces shows that the matrix series has a finite positive limit $S$ almost everywhere. Its coefficients are integrable: in a $\gamma$-unitary frame the absolute value of every coefficient is bounded by the trace. Positivity and the same trace identity give
\[
 \|S-S_N\|_{L^1(\gamma)}=\delta_N M.
\]
Thus $S_N\to S$ also in distributions. Since
\[
 \omega+\ddc U_N=S_N+\delta_N\omega
 \longrightarrow\omega+\ddc U
\]
in distributions by $L^1$ convergence of the potentials, we obtain $T=S$. The triangle inequality now gives
\[
 \|\omega+\ddc U_N-T\|_{L^1(\gamma)}
 \leq\|S_N-S\|_{L^1(\gamma)}
       +\delta_N\|\omega\|_{L^1(\gamma)}
 =2\delta_N M.
\]

We next compare the non-pluripolar measure with the pointwise determinant, using only bounded products. Fix $N$ and set $V_N=U-U_N$. The remaining partial sums show that
\[
 \delta_N\omega+\ddc V_N\geq0,\qquad V_N\leq0.
\]
For $t>0$, define
\[
 W_{N,t}=U_N+\max(V_N,-t).
\]
It is bounded, and its current is the sum of two positive factors:
\[
 \omega+\ddc W_{N,t}
 =S_N+\bigl(\delta_N\omega+\ddc\max(V_N,-t)\bigr).
\]
On $D_t=\{U>-t\}$, the inequality $U_N\leq0$ gives $V_N\geq U>-t$. Consequently $W_{N,t}=U=\max(U,-t)$ there. Locality and positivity of bounded products imply
\[
 \mathbf1_{D_t}\mathrm{MA}^{\mathrm{ext}}_\omega(U)
 \geq\mathbf1_{D_t}S_N^n.
\]
The smooth measure $S_N^n$ ignores the pluripolar pole set of $U$. Letting $t\to\infty$ proves
$\mathrm{MA}^{\mathrm{ext}}_\omega(U)\geq S_N^n$.
The positive matrices $S_N$ increase to $T$ almost everywhere, so their determinants increase to $\det_\gamma T$. Monotone convergence on every Borel set gives the asserted determinant-measure inequality. This does not presume that either limiting measure is locally finite.

For every $N\geq j$, positivity gives $S_N\geq a_jT_j$. Hence both the measurable limit and the smooth approximating current satisfy
\[
 \int_X(\det_\gamma T)\gamma^n
 \geq a_j^n\int_XT_j^n\geq2^j,
 \qquad
 \int_X(\omega+\ddc U_N)^n
 \geq a_j^n\int_XT_j^n\geq2^j.
\]
The first inequality holds for every $j$, so the integral is infinite. For the second, every $N\geq j$ obeys the bound; this proves divergence of the full sequence, without claiming that its masses are monotone.
\end{proof}

\begin{corollary}\label{cor:strong-linear-infinite-mass}
If bounded mass fails, there are nonpositive potentials $w_\varepsilon\in\PSH(X,\omega)$, $0<\varepsilon<1$, such that
\[
 \omega+\ddc w_\varepsilon\geq(1-\varepsilon)\omega,
 \qquad
 \mathcal I(pw_\varepsilon)=\mathcal O_X\quad(p>0),
\]
and both the pointwise determinant integral and the extended Monge--Amp\`ere mass are infinite. As $\varepsilon\downarrow0$, the potentials converge to zero in $L^1$ and their currents converge to $\omega$ in the coefficient $L^1$ norm. Their full Gauduchon trace measures converge to $\omega\wedge\gamma^{n-1}$ in total variation.
\end{corollary}
\begin{proof}
Take $w_\varepsilon=\varepsilon U$. Its current is
\[
 T_\varepsilon=(1-\varepsilon)\omega+\varepsilon T.
\]
The lower bound and the two $L^1$ convergence assertions follow immediately. The full trace measures have integrable densities, and their total-variation distance is at most
\[
 \varepsilon\|T-\omega\|_{L^1(\gamma)}.
\]
Every multiplier ideal is trivial by the exponential integrability already proved for $U$. Since $T_\varepsilon\geq\varepsilon T$ almost everywhere, its determinant integral is at least $\varepsilon^n$ times that of $T$, hence infinite. For the extended measure, constant truncation and mixed positivity give
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(\varepsilon U)
 \geq\varepsilon^n\mathrm{MA}^{\mathrm{ext}}_\omega(U),
\]
as in \cref{cor:bmp-characterization}. Its mass is therefore infinite as well.
\end{proof}

In this construction the full current, and therefore every smooth trace of it, is absolutely continuous with respect to smooth volume. The failure of top-degree integrability does not arise from mass of that current on a pluripolar set. Linear trace control, even with total-variation convergence and trivial multiplier ideals, must still be supplemented by nonlinear estimates.
