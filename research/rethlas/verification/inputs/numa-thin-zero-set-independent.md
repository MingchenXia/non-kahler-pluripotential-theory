Run_id: numa_thin_zero_set_independent_01

Independence requirement: This is an independent adversarial verification. Do not read another thin-zero-set audit, its results, its memory, or its conclusions. Use only the submitted mathematical proof and the explicitly accepted original NUMA construction. Recompute all ODE identities and both barrier directions yourself. Seek a failure of smooth endpoint extension or global positivity. The draft may be wrong, and the goal is correctness rather than agreement.

Statement: Adversarially audit a proposed COUNTEREXAMPLE to the empty-interior uniqueness question left open in the user-supplied NUMA manuscript. Claim: on P3, a fixed smooth nonclosed Hermitian background and fixed smooth nonnegative density g, whose zero set is exactly two disjoint smooth REAL hypersurfaces (hence empty interior and smooth-volume measure zero), admit uncountably many distinct normalized SMOOTH solutions of MAomega u=g omega_X^3. BMP even holds. This would substantially strengthen the supplied result. Be especially skeptical; do not accept a claimed solution of an open question merely because the derivation sounds plausible. Any gap must give wrong.

Accepted source input only: full construction in /Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex, passed degenerate_nonuniqueness_01. Read exact formulas: rank-one frame on U, r, p beta/2 and q=p', x=p+a,y=p+b,z0>=|q| band; a1,b0,z=q near left -1; a0,b1,z=-q near right+1; omega0 rank1 only on M+- and FS ends; omega=omega0+ddc rho strictly positive smooth nonclosed. The permitted explicit p=C exp(-1/(1-r²)) is used. Full source NUMA-Xia.pdf/.txt archived; last paragraph says empty-interior question unresolved. Do not assume new perturbed-density conclusions from source. No dependence on other new NUMA radial/classification drafts.

Accepted standard inputs: smooth scalar ODE local existence/uniqueness, continuous dependence and continuation on compact subsets of its smooth domain; elementary scalar barrier crossing argument; differentiation/flatness and positive smooth forms. No new PDE or external uniqueness theorem may be imported to validate the construction. If a known theorem seems to contradict it, verify exact hypotheses and identify which proof step fails.

NEW crucial claims to audit individually:
1. For fixed 0<s<1, original smooth trial slope h_s=sp defines fixed g>0 everywhere except M+-.
2. Perturb initial slope BELOW sp0. On a compact [rL,rR] continuous dependence keeps solution admissible. Upper exact solution sp cannot be crossed by uniqueness.
3. LEFT cL p with0<cL<s is a strict SUPERSOLUTION forward, hence LOWER barrier backward, because k_cL>k_s near -1. RIGHT -t p withs<t<1 is strict SUBsolution forward, hence lower barrier forward because k_s>k_-t near+1. Check ALL signs, factors p q and q negative right; no boundedness away from endpoints assumed.
4. These endpoint traps prevent a finite continuation breakdown in (-1,1), and bound h/p in compact subset(-1,1) at each end. Every small positive initial perturbation yields a global interval solution.
5. Smooth FLAT gluing: b=h/p solves b'=(p'/p)(R(p,b)-b), rational R with uniformly bounded derivatives in compact admissible p,b domain. p'/p rational with polynomial endpoint growth. Induct all b derivatives polynomial, then h derivatives p times polynomial ->0. Need every order and proper one-sided extension, not just h->0 or a numerical observation.
6. Primitive constant on projective ends defines global smooth u=G-rho, same fixed MA measure; rank-one frame/normalization constants correct, positivity globally including M+-; eta injection survives supremum normalization; density zero set exactly M+-.

No numerical result is part of this proof. No novelty certification. No book inclusion before independent mathematical audit(s).

Proof:

\section{Nonuniqueness with a zero set of empty interior}
\label{sec:numa-thin-zero-set}

The open zero-density band in the supplied example can be removed. We keep its Hermitian background, change the density, and solve a scalar initial-value problem. The new density vanishes only on the two separating real hypersurfaces $M_-$ and $M_+$. The infinite-order vanishing at those hypersurfaces permits smooth gluing of different solutions.

\begin{theorem}\label{thm:numa-thin-zero-set}
There is a smooth nonclosed Hermitian form $\omega$ on $\mathbb P^3$ and a smooth nonnegative density $g$, positive off two disjoint smooth real hypersurfaces, such that
\[
 \mathrm{MA}_\omega(u)=g\omega_X^3
\]
has uncountably many distinct smooth solutions normalized by $\sup_Xu=0$. Thus a zero set of empty interior, even of smooth-volume measure zero, does not ensure uniqueness of smooth normalized solutions. The background has bounded mass.
\end{theorem}

We retain $p,q,x,y,z,P,Q,R,\omega_0,\rho$ from \cref{sec:degenerate-hermitian-nonuniqueness}. Choose the specific permitted bump
\[
 p(r)=C\exp\!\left(-\frac1{1-r^2}\right),\qquad -1<r<1,
 \qquad \int_{-1}^1p(r)\,dr=1,
\]
extended by zero, so $q=p'$. Fix once and for all a scalar $0<s<1$, and set
\[
 k_s(r)=(x(r)+sp(r))(y(r)-sp(r))(z(r)+sq(r)).
\]
For $|r|>1$ this is $xyz$. The smooth potential with slope $sp$ has solution form $\omega_0+sH$, where $H=p(P-Q)+qR$. It is strictly positive for $-1<r<1$, since
\[
 x+sp=a+(1+s)p>0,\quad
 y-sp=b+(1-s)p>0,\quad
 z_0+sq\geq(1-s)z_0>0.
\]
It is also strictly positive outside the closed band. At $r=\pm1$ it equals the rank-one form $\omega_0$. Consequently
\begin{equation}\label{eq:numa-thin-density}
 g\omega_X^3=(\omega_0+sH)^3
\end{equation}
defines a smooth density positive exactly off $M_-\cup M_+$. Those hypersurfaces have measure zero and empty interior. This defines the data before constructing any further solution.

\begin{lemma}[Trapping the scalar solutions]\label{lem:numa-thin-trapping}
There exists $\eta_0>0$ such that for every $0<\eta<\eta_0$ the initial-value problem
\begin{equation}\label{eq:numa-thin-ode}
 h'=\frac{k_s(r)}{(x(r)+h)(y(r)-h)}-z(r),
 \qquad h(0)=sp(0)-\eta,
\end{equation}
has a smooth solution on $(-1,1)$ with $-x<h<y$ and $h<sp$. Moreover, on some fixed endpoint neighborhoods there are constants $0<c_L<s<t<1$, independent of $\eta$, such that
\[
 c_Lp<h<sp\quad\hbox{near }-1,
 \qquad -tp<h<sp\quad\hbox{near }1.
\]
\end{lemma}
\begin{proof}
The function $h_s=sp$ is a solution of \eqref{eq:numa-thin-ode} and lies strictly between $-x$ and $y$ throughout $(-1,1)$. Write $F_s(r,h)$ for that equation's smooth right side on the open domain $-x(r)<h<y(r)$.

Near $-1$ the coefficients are exactly
\[
 x=1+p,\qquad y=p,\qquad z=q>0.
\]
For a constant $c\in(-1,1)$ the measure coefficient of the trial slope $cp$ is
\[
 k_c=(1-c^2)\bigl(1+(1+c)p\bigr)pq.
\]
Fix $c_L\in(0,s)$. At $p=0$ the difference of the two factors preceding $pq$ for $c=c_L$ and $c=s$ is $s^2-c_L^2>0$. Thus, on a sufficiently small fixed left endpoint neighborhood, $k_{c_L}>k_s$ and
\begin{equation}\label{eq:numa-left-trap}
 F_s(r,c_Lp)-(c_Lp)'=
 \frac{k_s-k_{c_L}}{(x+c_Lp)(y-c_Lp)}<0.
\end{equation}
This is the lower barrier when the equation is followed backwards.

Near $1$ the exact coefficients are
\[
 x=p,\qquad y=1+p,\qquad z=-q>0,
\]
and the trial slope $cp$ has coefficient
\[
 k_c=(1-c^2)\bigl(1+(1-c)p\bigr)p(-q).
\]
Fix $s<t<1$. The difference of the factors for $c=s$ and $c=-t$ is positive at $p=0$, namely $t^2-s^2$. On a sufficiently small fixed right endpoint neighborhood, $k_s>k_{-t}$, so
\begin{equation}\label{eq:numa-right-trap}
 F_s(r,-tp)-(-tp)'=
 \frac{k_s-k_{-t}}{(x-tp)(y+tp)}>0.
\end{equation}
This is a lower barrier for forward evolution.

Choose $r_L<0<r_R$ within these respective neighborhoods. The graph of $h_s$ on $[r_L,r_R]$ is a compact subset of the smooth domain of $F_s$. Existence and continuous dependence for smooth ordinary differential equations therefore give $\eta_0>0$ such that every initial value $sp(0)-\eta$, $0<\eta<\eta_0$, has a solution throughout that interval, still in the domain, and
\[
 h(r_L)>c_Lp(r_L),\qquad h(r_R)>-tp(r_R).
\]
Two solutions of the scalar equation cannot cross, by local uniqueness. Since $h(0)<h_s(0)$, we have $h<h_s$ wherever the solution exists.

Follow the solution backwards from $r_L$. It cannot cross $c_Lp$. At a first crossing, the difference $h-c_Lp$ would be zero and positive immediately to its right; its right derivative there would be nonnegative. Formula \eqref{eq:numa-left-trap} gives a strictly negative derivative instead. Thus $c_Lp<h<sp$ on its leftward interval of existence. Likewise \eqref{eq:numa-right-trap} prevents a first downward crossing of $-tp$ in forward time from $r_R$, giving $-tp<h<sp$ to the right.

These bounds also prevent a finite endpoint of either interval of existence inside $(-1,1)$. On any compact subinterval approaching such a proposed endpoint, both horizontal factors are bounded away from zero, the slope remains bounded, and $F_s$ and its derivatives are bounded on a compact neighborhood of the graph. The ordinary continuation theorem extends the solution across that endpoint. It therefore exists on the entire interval $(-1,1)$ with the claimed bounds.
\end{proof}

\begin{lemma}[Flat extension at the endpoints]\label{lem:numa-thin-flat-extension}
Every solution furnished by \cref{lem:numa-thin-trapping}, extended by zero outside $(-1,1)$, is smooth on $\mathbb R$ and vanishes to infinite order at $\pm1$.
\end{lemma}
\begin{proof}
On either endpoint neighborhood put $b=h/p$. The trapping bounds place $b$ in a fixed compact subinterval of $(-1,1)$. Since $p>0$ there, this quotient is smooth in the open interval. The explicit endpoint formulas for the equation give
\[
 h'=q\,R_L(p,b)\quad\hbox{on the left},\qquad
 h'=q\,R_R(p,b)\quad\hbox{on the right},
\]
where
\[
 R_L(p,b)=
 \frac{(1-s^2)(1+(1+s)p)}{(1+(1+b)p)(1-b)}-1,
\]
\[
 R_R(p,b)=1-
 \frac{(1-s^2)(1+(1-s)p)}{(1+b)(1+(1-b)p)}.
\]
Both rational functions are smooth, with all derivatives bounded, on a fixed neighborhood of the relevant compact set with $p\geq0$. Thus
\begin{equation}\label{eq:numa-scaled-ode}
 b'=\frac{p'}p\bigl(R_{L/R}(p,b)-b\bigr).
\end{equation}
For the chosen bump,
\[
 \frac{p'}p=-\frac{2r}{(1-r^2)^2}.
\]
This rational function and each of its derivatives grow at most as a power of the inverse distance to the endpoint. The same holds for every derivative of $p$, and more precisely each derivative of $p$ is $p$ times such a rational function.

An induction using \eqref{eq:numa-scaled-ode} shows that every derivative $b^{(j)}$ grows at most polynomially in the inverse distance to the endpoint. The starting bound is the trapping bound on $b$. For the induction step, differentiate the right side $j$ times: every term is a product of a derivative of $p'/p$, a bounded partial derivative of $R_{L/R}$, and derivatives of $p$ and of $b$ of order at most $j$. All of these have the required polynomial bound by the induction hypothesis. This proves it for $b^{(j+1)}$.

Leibniz' rule for $h=pb$ now gives, for each $j$, constants $C_j,N_j$ such that
\[
 |h^{(j)}(r)|\leq C_j p(r)(1-|r|)^{-N_j}
\]
near the endpoints. The right side tends to zero because of exponential flatness of $p$. Thus all one-sided derivatives tend to zero, and extension by zero is smooth and flat, as asserted.
\end{proof}

\begin{proof}[Proof of \cref{thm:numa-thin-zero-set}]
For each $0<\eta<\eta_0$, extend $h_\eta$ by zero using the preceding lemma, and take a smooth primitive $G_\eta$. It is constant on each end of the real line, so $G_\eta(r)$ extends smoothly to all of $\mathbb P^3$, including the two omitted projective lines. Set
\[
 \widetilde u_\eta=G_\eta(r)-\rho.
\]
On the open band its solution form is
\[
 \omega+\ddc\widetilde u_\eta
 =(x+h_\eta)P+(y-h_\eta)Q+(z+h_\eta')R.
\]
The horizontal coefficients are strictly positive by trapping and continuation, while the equation gives
\[
 z+h_\eta'=\frac{k_s}{(x+h_\eta)(y-h_\eta)}>0.
\]
Outside the band the form is $\omega_0$. At the two boundary hypersurfaces, flatness gives the same rank-one form $\omega_0$. It is therefore globally semipositive, and its smooth cube equals the measure in \eqref{eq:numa-thin-density} everywhere. Normalize by subtracting $\sup_X\widetilde u_\eta$.

Distinct values of $\eta$ have different slopes at zero. The corresponding potentials cannot differ by a constant, so their normalized versions remain distinct. This gives an uncountable family. The strict Hermitian background is exactly the one constructed earlier and still satisfies $\omega\leq C'\omega_X$ for a fixed $C'$. The bounded mass argument in \cref{thm:degenerate-hermitian-nonuniqueness} applies unchanged.
\end{proof}

The density degenerates to infinite order on the two hypersurfaces. The complement has three components, and different solutions can be constant translates of one another on the two exterior components with different translation constants. The scalar equation on the middle component joins these constants smoothly across the degenerate hypersurfaces. This is why ellipticity at every point of the positive-density set does not give a global maximum-principle argument across its boundary.


Follow AGENTS.md strictly, persist EVERY deduction/reference/failure, full readable report and final results/numa_thin_zero_set_independent_01/verification.json via MCP. Do not edit book or previous results. Correct iff no errors/gaps under exact prerequisites.
