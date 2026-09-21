Run_id: quadratic_density_independent_01

Statement: Adversarially verify the attached potentially significant strengthening: a smooth nonclosed Hermitian background on P3 with BMP and smooth density vanishing exactly quadratically on two real hypersurfaces has uncountably many distinct normalized SMOOTH solutions. No finite-order uniqueness theorem is to be assumed. This is NOT a novelty certification. Any mathematical gap requires wrong.

Accepted inputs ONLY: rank-one frame P,Q,R and coordinate r on P(C2+C2), ddcG=G'(P-Q)+G''R, P^2=Q^2=R^2=0 and PQR>0, and FS=(sigma,1-sigma,sigma') in the exact source section /Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex. Standard smooth scalar ODE existence/uniqueness/compact continuous dependence/continuation, elementary calculus, Hermitian matrix positivity and closed bounded Bedford-Taylor/Stokes are permitted. NONE of the new background coefficients, positivity correction, density or ODE steps is accepted in advance. This construction CHANGES the background and is NOT the prior thin-zero-set construction. Check source derivative normalizations exactly. No new PDE theorem or literature premise is used. Read the original frame if necessary, but do not infer this claim from any other submitted new construction or audit.

Independence: This is a blind independent audit. Do not read quadratic_density_nonuniqueness_01, its results or memory, or any other audit of this new quadratic construction. Recompute from the submitted proof and accepted frame only.

Pay particular attention to: (1) global smoothness, x/y/z zeros and strict background correction, (2) exact finite quadratic vanishing of g, (3) both residual limits and barrier directions, (4) common eta interval and finite interior continuation, (5) log(-h) integration sign and exponential decay on BOTH ends despite polynomial p, (6) noncircular all-order derivative induction retaining an exponential factor, and (7) semipositive smooth gluing at rank-TWO interfaces, fixed equation and normalized injection. No numerical evidence. Do not edit the book. Use this run's MCP memory and results only. Save a full readable report and strict JSON with the standard verifier workflow. Ordinary approval only, never unsafe.

Proof:

\section{Nonuniqueness with quadratic vanishing of the density}
\label{sec:quadratic-density-nonuniqueness}

One can also make the density vanish to finite order. The modification is in the background coefficients: retain a strictly positive radial coefficient while a horizontal coefficient vanishes quadratically. The scalar equation then produces differences of potentials which are flat at the hypersurfaces, even though the density is not flat.

\begin{theorem}\label{thm:quadratic-density-nonuniqueness}
On $\mathbb P^3$ there exist a smooth nonclosed Hermitian form $\omega$ and a smooth nonnegative density $g$ such that:
\begin{enumerate}
\item The zero set of $g$ consists of two disjoint smooth real hypersurfaces. Near either hypersurface, $g$ is the square of a smooth defining function times a smooth strictly positive function.
\item The equation $(\omega+\ddc u)^3=g\omega_X^3$ has uncountably many distinct smooth $\omega$-plurisubharmonic solutions normalized by $\sup_Xu=0$.
\end{enumerate}
The fixed background has bounded mass.
\end{theorem}

We use only the rank-one frame $P,Q,R$ and the coordinate $r$ of \cref{sec:degenerate-hermitian-nonuniqueness}; the background coefficients are now different. Recall that
\[
 \ddc G(r)=G'(r)(P-Q)+G''(r)R,\qquad
 \omega_X=\sigma P+(1-\sigma)Q+\sigma'R,
 \qquad \sigma(r)=\frac{e^r}{1+e^r}.
\]
Choose a smooth function $a$ valued in $[0,1]$, equal to one for $r\leq-2/3$ and zero for $r\geq-1/3$, and put $b(r)=a(-r)$. Choose a smooth even cutoff $\chi$ valued in $[0,1]$, zero for $|r|\leq5/4$ and one for $|r|\geq3/2$. Set
\[
 p(r)=(1-r^2)^2,
\]
\begin{equation}\label{eq:quadratic-background}
 \begin{split}
 x&=(1-\chi)(p+a)+\chi\sigma,\\
 y&=(1-\chi)(p+b)+\chi(1-\sigma),\\
 z&=1-\chi+\chi\sigma',\qquad
 \omega_0=xP+yQ+zR.
 \end{split}
\end{equation}
These forms extend by $\omega_X$ across the two omitted projective lines. The coefficient $z$ is strictly positive. Both $x,y$ are strictly positive except that $y(-1)=0$ and $x(1)=0$. Thus $\omega_0$ is positive off $M_\pm=\{r=\pm1\}$ and has rank two there.

Choose the same kind of correction as before,
\[
 \rho=\varepsilon(r^2-1)\kappa(r),\qquad
 \kappa\in C_c^\infty((-2,2)),\quad
 \kappa=1\text{ on }[-3/2,3/2],\qquad
 \omega=\omega_0+\ddc\rho.
\]
For sufficiently small $\varepsilon>0$, $\omega$ is strictly positive. Indeed, on the central interval its coefficients are $x+2\varepsilon r$, $y-2\varepsilon r$, $z+2\varepsilon$. For $r\geq0$ the first is positive; on $[-3/2,0]$, $x$ has a positive minimum, so it remains positive for small $\varepsilon$. Reflection proves the second assertion, and the third is immediate. On $3/2\leq|r|\leq2$, the original form is strictly positive on a compact set and the correction is $O(\varepsilon)$. Near the projective ends there is no correction. At zero, $x'=y'=0$ and $z=1$, so
\[
 d\omega=dr\wedge\bigl((x'-z)P+(y'+z)Q\bigr)\ne0.
\]

Define the density before constructing further solutions by
\[
 g\omega_X^3=\omega_0^3.
\]
It is smooth and positive exactly off $M_-\cup M_+$. Near either hypersurface, $xyz=(1+p)p$ and
\[
 g(r)=\frac{(1+p(r))(1-r^2)^2}{\sigma(r)(1-\sigma(r))\sigma'(r)}.
\]
The denominator is smooth and strictly positive at $\pm1$. This proves the asserted quadratic vanishing. The potential $-\rho$ is one smooth solution.

\begin{lemma}\label{lem:quadratic-density-trapping}
For every sufficiently small $\eta>0$, the equation
\begin{equation}\label{eq:quadratic-density-ode}
 h'=\frac{xyz}{(x+h)(y-h)}-z,\qquad h(0)=-\eta
\end{equation}
has a smooth solution on $(-1,1)$ with $-x<h<y$ and $h<0$. For some fixed $0<c<1$, on fixed neighborhoods of both endpoints one has
\[
 -cp<h<0.
\]
Every such solution extends by zero to a smooth function on $\mathbb R$, flat at $\pm1$.
\end{lemma}
\begin{proof}
The right side $F(r,h)$ is smooth on $-x<h<y$, and $h=0$ is an exact solution. Near $-1$, $(x,y,z)=(1+p,p,1)$; near $1$, $(x,y,z)=(p,1+p,1)$. Fix $0<c<1$. For the trial function $-cp$, at the left endpoint
\[
 F(r,-cp)+cp'
 =\frac{1+p}{(1+(1-c)p)(1+c)}-1+cp'
 \longrightarrow-\frac{c}{1+c}<0,
\]
whereas at the right endpoint
\[
 F(r,-cp)+cp'
 =\frac{1+p}{(1-c)(1+(1+c)p)}-1+cp'
 \longrightarrow\frac{c}{1-c}>0.
\]
Here $p,p'\to0$ at both endpoints. The strict inequalities hold on fixed endpoint neighborhoods. They give a lower barrier backwards on the left and forwards on the right.

Choose a compact middle interval with endpoints in those neighborhoods. Continuous dependence around the exact solution zero supplies one $\eta_0>0$ such that all $0<\eta<\eta_0$ give a solution on that interval, in the smooth domain, and above $-cp$ at its endpoints. Scalar uniqueness gives $h<0$. The strict crossing arguments then give $-cp<h<0$ at both ends. On each compact subinterval of $(-1,1)$ the trapped graph stays a positive distance from both horizontal boundaries; hence ordinary continuation excludes any finite interior endpoint. This proves existence throughout $(-1,1)$.

We prove flatness separately. The equation factors exactly as
\begin{equation}\label{eq:quadratic-density-logarithm}
 h'=h\,L(r,h),\qquad
 L(r,h)=\frac{z(x-y+h)}{(x+h)(y-h)}.
\end{equation}
Since $h<0$, $(\log(-h))'=L(r,h)$. Near the left endpoint, the trapping bounds and the exact coefficients imply
\[
 L(r,h)=\frac{1+h}{(1+p+h)(p-h)}\geq\frac{C_1}{p}
\]
after shrinking that neighborhood, with $C_1>0$. Near the right endpoint they give
\[
 L(r,h)=\frac{-1+h}{(p+h)(1+p-h)}\leq-\frac{C_2}{p},
 \qquad C_2>0.
\]
For example on the left $1+h\geq1-cp\geq1/2$ and the denominator is at most $(1+p)(1+c)p$. On the right the numerator is at most $-1$, and the denominator is at most $p(1+(1+c)p)$. Because $p$ is comparable to the square of the endpoint distance $d=1-|r|$, integrating these inequalities backwards on the left and forwards on the right gives, for some $A>0$,
\begin{equation}\label{eq:quadratic-density-exponential}
 |h(r)|\leq C e^{-A/d}
\end{equation}
near either endpoint. Constants may depend on the solution; uniformity in $\eta$ is not needed for smooth extension.

It remains to control every derivative. On the trapped graph, all partial derivatives in $(r,h)$ of the rational function $L$ have at most polynomial growth in $d^{-1}$. Indeed, near an endpoint $x,y$ are polynomials in $r$, $z=1$, $h$ is bounded, and the two denominator factors are bounded below by a positive constant and by $(1-c)p$, in the appropriate order. Repeated quotient differentiation therefore only introduces finite powers of $p^{-1}$.

Inductively, for every $j\geq0$ there are constants $C_j,N_j$ with
\[
 |h^{(j)}(r)|\leq C_j e^{-A/d}d^{-N_j}.
\]
The case $j=0$ is \eqref{eq:quadratic-density-exponential}. Differentiate $h'=hL(r,h(r))$ $j$ times. Every term has a derivative of the explicit factor $h$, of order at most $j$, and a derivative of the composite $L$. The latter uses only partial derivatives of $L$ and derivatives of $h$ of order at most $j$, all polynomially bounded by the induction hypothesis. The explicit factor retains the exponential bound, proving the next case. All derivatives therefore tend to zero. Extending them by zero and applying the mean value theorem to endpoint difference quotients proves that the zero extension is smooth and flat.
\end{proof}

\begin{proof}[Proof of \cref{thm:quadratic-density-nonuniqueness}]
For each $0<\eta<\eta_0$, take a primitive $G_\eta$ of the smooth zero extension of $h_\eta$. It is constant near each projective end and therefore defines a global smooth function. The potential $u_\eta=G_\eta(r)-\rho$ has solution form
\[
 \omega+\ddc u_\eta
 =(x+h_\eta)P+(y-h_\eta)Q+(z+h_\eta')R.
\]
Inside the band the first two coefficients are positive and the equation gives
\[
 z+h_\eta'=\frac{xyz}{(x+h_\eta)(y-h_\eta)}>0.
\]
Outside the band the form is $\omega_0$, and at the two boundary hypersurfaces flatness gives the same rank-two form $\omega_0$. Thus it is globally semipositive and has cube exactly $\omega_0^3=g\omega_X^3$. Different initial slopes give potentials which do not differ by constants, so supremum normalization preserves an uncountable family. Finally $\omega\leq C\omega_X$ on compact $\mathbb P^3$; the positive mixed expansion and closed bounded Stokes give the same uniform bounded-mass estimate as before.
\end{proof}

This example shows that even quadratic vanishing along a smooth real hypersurface need not restore uniqueness. The flat objects in the construction are differences of solutions, produced by the singular scalar equation. The density itself has finite vanishing order. The positive-density set still has three components; the construction makes no assertion about uniqueness when that set is connected.
