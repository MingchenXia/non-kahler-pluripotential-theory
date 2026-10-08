# Full original S18 review of the current first-moment-free construction

The current author source controls the claims. Check every A--E claim over the entire declared range 0<alpha<1 and c>=alpha. The older source's alpha<1/2 energy argument is preserved as history, not as a restriction or a proof for the enlarged range. No finite nonlinear first moment is assumed. The exact original task and completion criterion are unchanged; a restricted construction remains progress and cannot close the unrestricted direction.

Reassess all complete proofs, actual rough ordinary-type competitors, genuine canonical functions, finite nonclosed correction terms, local products, gauge and pure-pullback laws, all-test fixed-density formulas, the derivative and the finite improper cost at the nonbig nef endpoint. Imported S11 proofs are supplied throughout their whole support graph for direct reassessment; their candidate flags, PASS reports and root-read records are not proof premises. The unused unresolved general S11 L1 maximal-density coefficient assertion is not part of this construction. Do not infer it from this packet. Credit BGL's established definitions and modification laws and the checked ruled mass and all-test calculation. No priority or arbitrary-upstairs-density equality is claimed.

Return consistent standalone mathematical premises with valid zero-based indexed primary or matching exact task quotations. Each passage must index an existing premise; premises=[] cannot accompany indexed passages. Neither an irrelevant task quote nor a source name alone establishes an external mathematical claim.


## Complete current first-moment-free author source

Path: papers/S18-first-moment-free-nonanalytic-moving-volumes.tex
SHA256: 6292ea5ab345e792151bd1c9d1366e2e52cb2de0e85ba585452d44baee81434e

\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{proposition}{Proposition}
\newcommand{\ddc}{dd^c}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\ext}{\mathrm{ext}}
\newcommand{\PP}{\mathbb P}
\title{Nonanalytic imposed poles and moving volume data on a ruled surface}
\author{}
\date{October 8, 2026}
\begin{document}
\maketitle
\noindent\textbf{Working draft.} The root-developed claims in this document
have not passed independent reconstruction or full native mathematical review.
This source is not a checked publication.

\begin{abstract}
We propose a concrete moving-volume construction on $\PP^1\times\PP^1$
with a positive genuinely nonclosed background and an imposed unbounded
nonanalytic ordinary singularity type. The upper and lower masses optimize
over every potential of that type, including rough fiber-dependent potentials
and references with infinite first moment. The calculation uses closed
ordinary-order comparison in an auxiliary background and requires only
local integrability in its nonclosed correction.
They are distinct from the fixed-density Gauduchon variational volume, whose
full-test infimum and subtraction cost admit explicit formulas. A smooth nef
endpoint gives logarithmic variational degeneration while the upper singularity
mass stays positive. Exact smooth-gauge and pure-pullback laws distinguish
these data from exceptional-curvature subtraction and from arbitrary changes
of the reference density. This is a proposed scoped construction; the general
nonclosed moving-product programme is not resolved.
\end{abstract}

\section{Definitions and proposed results}
Use $\ddc=(i/(2\pi))\partial\bar\partial$ and
$d^c=(i/(4\pi))(\bar\partial-\partial)$. Let $w$ be the Fubini--Study
probability form on $\PP^1$, and write $w_1,w_2$ for its pullbacks to
$X=\PP^1\times\PP^1$. In an affine coordinate,
\[
 w=\frac{i\,dz\wedge d\bar z}{2\pi(1+|z|^2)^2},\qquad
 G_0=\log\frac{|z|^2}{1+|z|^2},\qquad \ddc G_0=[0]-w.
\]
Unitary transport gives $G_p$ for any $p\in\PP^1$, normalized by
$\max G_p=0$. Fix $0<\alpha<1$ and set
\[
 U=1-(1-G_p)^\alpha,\qquad u=\operatorname{pr}_1^*U,
 \qquad D=\{p\}\times\PP^1.
\]
All potentials use their genuine canonical upper representatives. We write
$v\sim u$ for bounded difference, with the inequalities retained at common
poles. For $c\geq\alpha$ and a smooth function $a>0$ on the first factor,
put $\theta=cw_1+aw_2$ and define
\[
 \sigma_-(\theta,u)=\inf_{v\in\PSH(X,\theta),\ v\sim u}
              \MA^{\ext}_\theta(v)(X),\qquad
 \sigma_+(\theta,u)=\sup_{v\in\PSH(X,\theta),\ v\sim u}
              \MA^{\ext}_\theta(v)(X).
\]
The products are the finite-level non-pluripolar products, expanded against
the smooth background. These extrema concern the entire ordinary type. Together with the separately
defined fixed-density variational volume and its minimizing-test cost, they
are the moving data proposed here. The imposed ordinary type is retained
as part of these data: its trivial ideals do not identify it with the
bounded type.

\begin{theorem}\label{thm:mass}
The reference $u$ is $\theta$-psh and has an unbounded nonanalytic pole on
$D$, zero Lelong numbers, and $\mathcal I(tu)=\mathcal O_X$ for every $t>0$.
Every $v\in\PSH(X,\theta)$ with $v\sim u$ has positive finite mass and
\begin{align}
 \MA^{\ext}_\theta(v)(X)
     &=\int_X\theta^2+2\int_Xv\,\ddc\theta,\label{eq:linear-mass}\\
 \sigma_-(\theta,u)&=2c\min a,\qquad
 \sigma_+(\theta,u)=2c\max a.\label{eq:extrema}
\end{align}
Both bounds are approached by actual representatives of that exact type.
When $a$ is nonconstant the smooth positive background is nonclosed.
\end{theorem}

For a smooth positive $m$ on the first factor with $\int m w=1$, let
$\mu=mw_1w_2$. For a smooth positive Gauduchon test $T$ of bidegree $(1,1)$,
so that $\ddc T=0$, define
\[
 D_\mu(T)=\int_X\sqrt{T^2/\mu}\,\mu,\qquad
 \lambda_\mu(\theta)=\inf_T\frac{\int_X\theta\wedge T}{D_\mu(T)},
 \qquad V_\mu(\theta)=\lambda_\mu(\theta)^2.
\]
Every smooth positive Gauduchon test is included in this infimum.

\begin{theorem}\label{thm:dual}
Writing $H=\int_{\PP^1}(m/a)w$, one has
\[
 V_\mu(\theta)=\frac{2c}{H}.
\]
The infimum is attained by the smooth positive closed test
\[
 T=\frac ga w_1+w_2,\qquad g=\frac{V_\mu(\theta)m}{2a}.
\]
The mass extrema in \eqref{eq:extrema} are independent of $m$, whereas
this fixed-density volume can depend on $m$ when $a$ is nonconstant.
\end{theorem}

The full-type mass calculation, the all-test variational formula and the
pure-pullback law agree with the checked ruled construction
\cite{Ruled}, specialized to zero logarithmic divisor coefficient.
They are proved here to fix their actual application to the moving
segment and its limiting cost. Existing ordinary-type volumes and their
pure-modification laws receive their credit in \cite{BGL}.
No literature-priority claim is made.

\section{The imposed type and small-background representatives}
Let $\chi(t)=1-(1-t)^\alpha$ for $t\leq0$. Then
\[
 \chi'(t)=\alpha(1-t)^{\alpha-1},\qquad
 \chi''(t)=\alpha(1-\alpha)(1-t)^{\alpha-2}.
\]
On the punctured curve,
$\ddc U=-\chi'(G_p)w+\chi''(G_p)dG_p\wedge d^cG_p\geq-\alpha w$.
After adding a local potential of $\alpha w$, this is a locally bounded-above
psh function on the punctured disk. Its genuine psh extension has the same
lower curvature bound. Its logarithmic coefficient is zero, since
$U/\log|z-p|\to0$. In particular the positive curve current
$Cw+\ddc U$ has no atom at $p$ for $C\geq1$.
The same local calculation proves $u\in\PSH(X,\theta)$.
Moreover $e^{-tU}$ grows more slowly than every fixed negative power of
$|z-p|$, and hence is locally integrable for every $t>0$. All holomorphic
germs are therefore in $\mathcal I(tu)$. An unbounded analytic singularity
on this smooth divisor has a positive logarithmic coefficient; the imposed
type is thus genuinely nonanalytic.

\begin{lemma}\label{lem:small}
There are $U_L\sim U$ with $\sup U_L=0$,
$\ddc U_L\geq-\varepsilon_Lw$, $\varepsilon_L\to0$, and
$U_L\to0$ in $L^1(\PP^1)$.
\end{lemma}
\begin{proof}
For $L>0$ put $\varepsilon_L=\chi'(-L)$ and define
\[
 \chi_L(t)=
 \begin{cases}
   \chi(t)+C_L,&t<-L,\\
   \varepsilon_Lt,&-L\leq t\leq0,
 \end{cases}\qquad
 C_L=-\varepsilon_LL-\chi(-L).
\]
The two values and first derivatives match. This is convex with
$0\leq\chi_L'\leq\varepsilon_L$. Set $U_L=\chi_L(G_p)$.
The preceding local extension argument, or smooth convex approximation
followed by local decreasing convergence, gives its genuine curvature bound.
Near $p$ the difference $U_L-U$ is the finite constant $C_L$; on the remaining
compact part it is bounded. Thus $U_L\sim U$, including their common pole.
Here $C_L\geq0$: with $x=1+L$, the function
$(1-\alpha)x^\alpha+\alpha x^{\alpha-1}-1$ vanishes at $x=1$ and has
nonnegative derivative for $x\geq1$. On $[-L,0]$, convexity gives
$\chi(t)\leq\chi'(-L)t$. Consequently $U\leq U_L\leq0$.
For each point other than $p$, eventually $U_L=\varepsilon_LG_p\to0$.
Since $U\in L^1$, dominated convergence proves the stated $L^1$ limit.
\end{proof}

This supplies actual small-background representatives without erasing the
pole by a maximum with a bounded function. If a smooth $g$ satisfies
$cw+\ddc g\geq\delta w$, then $g+U_L$ is $cw$-psh for
$\varepsilon_L<\delta$ and remains of the ordinary type $U$.

\section{All rough competitors and the mass extrema}
We use the closed ordinary-singularity comparison of
\cite[Theorem~1.16]{BEGZ}. Its hypotheses are compact K\"ahler ambient,
closed positive currents in common cohomology classes, and small unbounded
locus, meaning local boundedness outside a closed locally complete
pluripolar set. We check each hypothesis and use the comparison in both
ordinary orders and in degrees one and two. No nonclosed comparison
or finite-energy theorem is invoked.

Choose $K=C(w_1+w_2)$, with $C$ sufficiently large that $K\geq\theta$
and $C\geq1$. Write $S_0=K+\ddc u$. Its actual closed products are
\[
 \langle S_0\rangle=S_0,\qquad
 \langle S_0^2\rangle=2C(Cw_1+\ddc u)w_2,
 \qquad\int_X\langle S_0^2\rangle=\int_XK^2=2C^2.
\]
Indeed the curve current has total mass $C$ and no atom at $p$.
On $X\setminus D$ its pulled-back square is zero by dimension.
The displayed positive finite product has zero mass on $D$ and is
exactly the non-pluripolar extension of the bounded local product.

Take any $v\in\PSH(X,\theta)$ with $v\sim u$, and put
$S=K+\ddc v$. Both $S,S_0$ are closed positive currents in the
K\"ahler class $\{K\}$ on the compact K\"ahler surface $X$.
Their potentials are locally bounded off the complete pluripolar divisor
$D$, and have mutual bounded order. The cited theorem, applied in both
orders to a single current and then to the repeated two-current tuples,
gives
\[
 \{\langle S\rangle\}=\{\langle S_0\rangle\}=\{K\},\qquad
 \int_X\langle S^2\rangle=\int_X\langle S_0^2\rangle=\int_XK^2.
\]
Here $\langle S\rangle$ is $S$ restricted off $D$ and extended
by zero. Thus $S-\langle S\rangle=1_DS$ is positive and its trace is
\[
 \int_X(S-\langle S\rangle)\wedge K=0.
\]
A positive current of zero strictly positive trace is zero, as follows
from the local Hermitian matrix inequality for its measure coefficients.
Consequently $\langle S\rangle=S$, including absence of polar trace.
This proves the required first-current identity for every rough competitor;
it does not infer it from vanishing generic divisorial Lelong numbers alone.

Set $R=\theta-K$. The finite-level smooth-background expansion now gives
\[
 \MA_\theta^{\ext}(v)=\langle S^2\rangle+2R\wedge S+R^2.
\]
All terms are finite signed measures, and the left side is positive.
Integrating, using full closed mass and distributional Stokes, gives
\[
 \int K^2+2\int R\wedge K+\int R^2+2\int R\wedge\ddc v
     =\int\theta^2+2\int v\,\ddc\theta.
\]
This proves \eqref{eq:linear-mass}, including for every rough competitor.

Average $v$ over the compact unitary action on the second factor.
The background is invariant. Averaging its current inequality and using
canonical psh representatives gives a genuine invariant potential
$\operatorname{pr}_1^*q$, with $q\sim U$. For completeness, local addition
of a smooth sufficiently positive quadratic makes all translates psh;
their Haar average is locally integrable by Fubini, satisfies the submean
inequality, and has its canonical upper representative. The bounded
inequalities with $u$ pass through the average and then through canonical
regularization. Off $D$ the average is finite, and on $D$ it equals
$-\infty$. Positivity says $cw+\ddc q\geq0$.

Since $\ddc\theta=\ddc a\wedge w_2$, the functional in
\eqref{eq:linear-mass} is unchanged by this averaging, and
\[
 \MA_\theta^{\ext}(v)(X)=2\int_{\PP^1}a(cw+\ddc q).
\]
The measure in parentheses is positive of total mass $c$. This proves both
global bounds and positive finiteness.

To approach either bound, choose a point $x$ attaining the corresponding
extremum of $a$. There are smooth strictly positive curve measures
$\zeta_j$ of total mass $c$ converging weakly to $c\delta_x$; for instance,
combine a smooth approximate identity near $x$ with a small positive
multiple of $w$. Solve $\ddc g_j=\zeta_j-cw$ on the sphere. The smooth
solution exists because the right side has zero integral, either by the
explicit Green kernel or by the zero-mean scalar Poisson equation.
For each $j$ choose $L_j$ so large that
$\varepsilon_{L_j}$ is smaller than half the positive lower bound of
$\zeta_j/w$ and $|\int U_{L_j}\ddc a|<1/j$.
Then $g_j+U_{L_j}$ is an actual $cw$-psh representative of $U$'s type and
\[
 \int a(cw+\ddc(g_j+U_{L_j}))\longrightarrow c a(x).
\]
Pulling back proves both exact extrema in Theorem~\ref{thm:mass}.


\section{An exact first-moment boundary}
The preceding proof holds for every $0<\alpha<1$. For the same closed
reference $K=C(w_1+w_2)$, its first moment has a separate threshold:
\[
 \int_X(-u)\langle (K+\ddc u)^2\rangle<\infty
       \quad\Longleftrightarrow\quad\alpha<\tfrac12.
\]
On a punctured disk put $t=-G_p$. As $t\to\infty$, $-U$ is comparable
to $t^\alpha$ and $\chi''(G_p)$ to $t^{\alpha-2}$.
The angular integral of $dG_p\wedge d^cG_p$ is comparable to $dt$.
The singular contribution to the actual curve moment is therefore
comparable to $\int^\infty t^{2\alpha-2}\,dt$.
The remaining smooth-volume contribution is finite by exponential radial
area decay. The moment is infinite for $1/2\leq\alpha<1$, logarithmically
at equality. This is an actual separated non-pluripolar measure calculation,
not an extra finiteness hypothesis in the nonclosed mass formula.
In particular $\int v\,\ddc\theta$ uses only the local integrability
of $v$ against a smooth form, throughout this enlarged parameter range.

\section{The full Gauduchon formula and its moving cost}
Let $H=\int(m/a)w$, $V=2c/H$ and $g=Vm/(2a)$, so $\int gw=c$.
Choose a smooth $b$ with $\ddc b=(g-c)w$. Then
\[
 \Omega=\theta+\ddc\operatorname{pr}_1^*b=gw_1+aw_2>0,
 \qquad\Omega^2=V\mu.
\]
For every smooth positive Gauduchon test $S$, Stokes and the pointwise
two-dimensional arithmetic--geometric mean inequality give
\[
 \int\theta\wedge S=\int\Omega\wedge S
       \geq\sqrt V\int\sqrt{S^2/\mu}\,\mu=\sqrt V D_\mu(S).
\]
The test $T=\Omega/a=(g/a)w_1+w_2$ is positive and closed, because its
first coefficient depends only on the first curve. Moreover
\[
 \int\theta T=2c,\qquad T^2=\frac{Vm}{a^2}w_1w_2,
 \qquad D_\mu(T)=\sqrt V H.
\]
It attains the lower bound, proving Theorem~\ref{thm:dual} for all tests.

For $c_s=c-sd\geq\alpha$, $a_s=a-sb>0$ on a parameter interval, put
$\theta_s=c_sw_1+a_sw_2$ and $\eta=dw_1+bw_2$. Keep $m$ fixed, and
use the preceding notation with subscript $s$. Direct differentiation gives
\[
 H_s'=\int\frac{bm}{a_s^2}w,\qquad
 \int\eta T_s=d+\frac{V_s}{2}H_s',\qquad
 \frac{d\sqrt{V_s}}{ds}
       =-\frac{\int\eta T_s}{D_\mu(T_s)}.
\]
This is the actual full-test subtraction derivative. Its integral on any
compact positive segment equals the difference of the two endpoint root
volumes. It is separate from the upper and lower singularity masses.

\section{A logarithmic nef endpoint}
Let $c=1$, $m=1$, and
$\tau=(|z|^2-1)/(|z|^2+1)$ on the first sphere. Its distribution under
$w$ is $d\tau/2$ on $[-1,1]$: radial integration gives
$dt/(1+t)^2=d\tau/2$, with $t=|z|^2$. Take $a=2+\tau$ and subtract
$\eta=w_2$. For $0\leq s<1$,
\[
 H_s=\frac12\log\frac{3-s}{1-s},\qquad
 V_s=\frac4{\log((3-s)/(1-s))},\qquad
 \sigma_-(s)=2(1-s),\quad\sigma_+(s)=2(3-s).
\]
At $s=0$ the raw zero-potential mass is $2\int a w=4$, while the lower
mass, upper mass and fixed-density volume are $2$, $6$ and $4/\log3$.
All these backgrounds are genuinely nonclosed. As $s\uparrow1$ the root
volume tends to zero and its derivative is
\[
 -\frac{2}{(1-s)(3-s)[\log((3-s)/(1-s))]^{3/2}}.
\]
The improper integral of the cost is finite, equal to $2/\sqrt{\log3}$.
The upper singularity mass instead tends to $4$.

The endpoint $\theta_1=w_1+(1+\tau)w_2$ is smooth semipositive and nef,
since adding any positive multiple of $w_1+w_2$ makes it positive. Its
all-test root-volume infimum is zero, by nonnegativity and comparison with
$\theta_s$. It is not big. Indeed a strict current would dominate
$\varepsilon(w_1+w_2)$ after changing $\varepsilon>0$. Averaging its
potential over the second sphere preserves that strict inequality and
produces a genuine base potential. Its vertical coefficient is still
$1+\tau$, which would therefore have to be at least $\varepsilon$
almost everywhere. This is impossible near its zero fiber.
The endpoint thus lies outside the big segment; it is not a counterexample
to any asserted equivalence between bigness and positive variational volume.

\section{Smooth gauges and pure pullback}
For smooth real $f$, set $\theta'=\theta+\ddc f$, $u'=u-f$ and $v'=v-f$.
The actual currents coincide, so the finite-level local construction
transports the extended measure and both mass extrema. Against every
Gauduchon test the numerator also coincides by Stokes. A parameter-dependent
smooth gauge contributes $\ddc\dot f_s$ to the derivative and its pairing
with $T_s$ is zero.

\begin{proposition}\label{prop:mod}
For a proper modification $\pi:Y\to X$ between smooth connected compact
complex manifolds and a smooth real background $\theta$, pullback is a
canonical bijection of the genuine $\theta$-psh functions with the genuine
$\pi^*\theta$-psh functions. Ordinary types correspond. For these
potentials,
\[
 \pi_*\MA_{\pi^*\theta}^{\ext}(\pi^*v)=\MA_\theta^{\ext}(v).
\]
Thus the mass extrema are preserved for the pure pullback background and
type whenever the class of competitors is nonempty.
\end{proposition}
\begin{proof}
Let $Z$ be an analytic center containing the non-isomorphism locus.
On a relatively compact coordinate ball choose smooth $\rho$ with
$\ddc\rho\geq\theta$. If $b$ is $\pi^*\theta$-psh, then
$b+\pi^*\rho$ is psh upstairs. Off $Z$ it descends to a psh function;
properness and local upper bounds upstairs give a local upper bound near
$Z$. The removable-singularity theorem \cite[I.5.23--5.24]{Demailly}
gives the unique canonical psh extension. Subtracting $\rho$ gives a genuine
quasi-psh function downstairs. Its sharper $\theta$-positivity holds off
$Z$ and also on $Z$: the added current on $Z$ is positive, whereas the
smooth correction has no mass there. Pullback agrees upstairs off the
exceptional analytic set, hence almost everywhere, and the two genuine
quasi-psh representatives agree canonically. The converse follows from
local psh pullback and the current bound.

Bounded inequalities descend off $Z$ and hold everywhere by canonical
recovery of quasi-psh functions from their almost-everywhere values. Thus
ordinary equivalence is preserved in both directions. Off the exceptional
set all finite-level local products transform by the biholomorphism.
Each bounded local product, and then each non-pluripolar product, gives
zero mass to analytic pluripolar sets; this remains true for the
smooth-background expansion. Both extended measures therefore give zero
mass to the respective excluded analytic sets. The equality on their
complements proves the measure identity, even when total mass is infinite.
Taking the full infimum and supremum over the bijective type proves the
last assertion.
\end{proof}

For a point blowup the pullback backgrounds in the positive segment are
also big. One direct justification uses the exceptional divisor $E$.
Choose a smooth curvature $\beta_E$ of $\mathcal O(E)$ whose restriction
to $E$ is the negative Fubini--Study form. For a closed K\"ahler form
$K_0=w_1+w_2$, the form $\pi^*K_0-t\beta_E$ is K\"ahler for sufficiently
small $t>0$. Here is the local positivity check. In finitely many blowup
charts $(x,y)\mapsto(x,xy)$ with $y$ in compact sets, the matrix $P$ of
$\pi^*K_0$ satisfies $P_{x\bar x}\geq c_0>0$,
$|P_{x\bar y}|\leq C|x|$, and its Schur complement is at least
$c_1|x|^2$. For $B=-\beta_E$, shrink a fixed chart neighborhood so that
$B_{y\bar y}\geq b_0>0$, with all entries bounded. The transverse
coefficient of $P+tB$ is at least $c_0/2$ for small $t$, and its Schur
complement is at least
\[
 c_1|x|^2+t b_0-C'\bigl(t|x|+t|x|^2+t^2\bigr).
\]
First fix the neighborhood small enough, then $t$ small enough, to make
the last three terms at most $t b_0/2$. This proves strict positivity on
that fixed neighborhood. On its compact complement, strict positivity
of $\pi^*K_0$ persists under the bounded perturbation. The metric with
the required restriction to $E$ exists because
$\mathcal O(E)|_E=\mathcal O_{\PP^1}(-1)$: extend its negative
Fubini--Study metric smoothly to the line bundle. If $\theta_s\geq a_0K_0$ and
$\ddc\ell_E=[E]-\beta_E$, then
\[
 \pi^*\theta_s+\ddc(a_0t\ell_E)
   \geq a_0(\pi^*K_0-t\beta_E)+a_0t[E]
\]
is an actual strict current. This gives a nonclosed big example upstairs.
Subtracting exceptional curvature is a different background, and is not
covered by Proposition~\ref{prop:mod}'s equality. Nor do we identify an
arbitrary smooth positive upstairs probability with $\pi^*\mu$, which
degenerates on $E$.

The construction does not assert a general nonclosed positive-product
theory, unrestricted birational equality for changed backgrounds,
density-independent Gauduchon volume, or a solution of the general
nef-endpoint bridge. The closed comparison in \cite{BEGZ} supplies only
the precisely checked auxiliary closed foundations. The nonclosed
optimization, full-test formula and limiting subtraction cost have
their stated direct proofs. General S18 remains open.

\begin{thebibliography}{9}
\bibitem{BEGZ} S.~Boucksom, P.~Eyssidieux, V.~Guedj and A.~Zeriahi,
\emph{Monge--Amp\`ere equations in big cohomology classes},
Acta Math. \textbf{205} (2010), 199--262.
\href{https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf}{Author-hosted published primary text}.
\bibitem{Demailly} J.-P.~Demailly, \emph{Complex Analytic and Differential
Geometry}, Chapter~I, Theorems~5.23--5.24.
\href{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf}{University-hosted primary text}.
\bibitem{BGL} S.~Boucksom, V.~Guedj and C.~H.~Lu,
\emph{Volumes of Bott--Chern classes}, Peking Math.~J. (2025),
Definition~3.1 and Proposition~3.3.
\href{https://d-nb.info/1374372846/34}{Published primary text}.
\bibitem{Ruled} \emph{Restricted masses and ordinary strict-current types
on a nonclosed ruled surface}, checked restricted construction, October~2026,
Sections~2 and~5.
\href{https://github.com/MingchenXia/non-kahler-pluripotential-theory/blob/2ec45dec6172ced6e2af18b2b5fe657c07aeee9e/research/papers/S11-nonclosed-ruled-restricted-masses-and-strict-types.tex}{Retained checked source}.
\end{thebibliography}
\end{document}


## Complete private unverified first-moment-free proof supplement

Path: notes/S18-zero-energy-assumption-ordinary-type-mass-20261007.private-unverified.md
SHA256: 6ac8ac272b90fed81b7b73036441bc0f78765275818c1925a6902b4d5d014474

# S18: ordinary-type mass without a finite first moment

Root-origin proposed supplement. Native mathematical review, independent
reconstruction, exact-task acceptance and publication are pending. This is a
new proof and an enlargement of the old parameter range, not a correction of
the frozen article. The existing article and statement-only inputs stay exact.
No priority claim is made. The general nonclosed moving-product direction
remains open.

## Proposed statement

Keep the exact normalization, ruled surface and notation of the existing S18
article: X=P^1 x P^1, probability Fubini--Study forms w_1,w_2,
G_p=log chordal distance squared to p, D={p} x P^1,

    U=1-(1-G_p)^alpha, u=pr_1^*U,
    theta=c w_1+a w_2,

where a is smooth and strictly positive on the first curve. The article's
mass and full-test Gauduchon conclusions should hold for every 0<alpha<1 and
c>=alpha, including alpha>=1/2. In particular, over ALL genuine theta-psh
v ordinarily equivalent to u,

    MA_ext_theta(v)(X)=integral theta^2+2 integral v dd^c theta,
    inf_v MA_ext_theta(v)(X)=2c min a,
    sup_v MA_ext_theta(v)(X)=2c max a.

These measures are positive and finite for every competitor. The result
includes rough and fiber-dependent competitors. No assumption of finite
Aubin--Mabuchi energy or finite first moment is needed. The old proof's
first-moment estimate remains correct within its old alpha<1/2 range.

## 1. Closed reference products

The function chi(t)=1-(1-t)^alpha is increasing and convex on t<=0,
with 0<chi'<=alpha and chi'(-infinity)=0. The punctured-disk curvature
calculation and genuine psh extension therefore give dd^c U>=-alpha w
for every alpha in (0,1). Its Lelong number is zero, its canonical value at
p is -infinity, and it is smooth elsewhere. The measure Cw+dd^c U has no
atom at p and total mass C for every C>=alpha.

Choose C large enough that K=C(w_1+w_2)>=theta and C>=alpha. Then K is a
CLOSED strictly positive form. Put S_0=K+dd^c u. On X\D the ordinary
locally bounded products, trivially extended across D, give

    <S_0>=S_0,
    <S_0^2>=2C (Cw_1+dd^c u) wedge w_2,
    integral <S_0^2>=2C^2=integral K^2.

The first equality follows because the first-factor curve measure has no
atom at p. For the second, the square of a pulled-back curve current is zero
on X\D; the formula is positive, finite and has zero mass on D. It is
precisely the non-pluripolar extension of the bounded local product.

## 2. Every ordinary-equivalent rough competitor

Take any genuine v in PSH(X,theta) with v~u, and set S=K+dd^c v.
Then S is a CLOSED positive current in the same Kähler class as S_0.
The potentials v and u have bounded difference. Both are locally bounded
off the closed complete pluripolar divisor D. Thus they have small unbounded
locus in the exact sense of BEGZ Definition 1.2, not merely zero Lelong
numbers or a comparison of multiplier ideals.

Apply BEGZ Theorem 1.16 twice, in both ordinary orders, first with p=1
and then with p=2 and each tuple equal to its repeated current. All its
currents are closed and positive, their respective classes agree, the
ambient manifold is compact Kähler, and every unbounded locus is contained
in D. Consequently their non-pluripolar cohomology classes coincide:

    {<S>}={<S_0>}={K},
    integral <S^2>=integral <S_0^2>=integral K^2.

These equalities use the CLOSED background K only. They make no claim of
nonclosed mass invariance and do not transfer a closed intersection formula
directly to theta.

The first non-pluripolar current is the restriction of S off D, extended by
zero. Thus S-<S>=1_D S is a positive current. Its trace against the strictly
positive K is

    integral (S-<S>) wedge K=integral K^2-integral K^2=0.

A positive current with zero strictly positive trace is zero, by the local
Hermitian matrix inequality for its measure coefficients. Hence <S>=S.
In particular there is no unproved assertion that zero generic divisorial
Lelong numbers alone imply disappearance of an arbitrary polar measure.

## 3. The actual nonclosed measure

Write R=theta-K. On X\D, v is locally bounded. The ordinary local
Bedford--Taylor polynomial expansion gives

    (theta+dd^c v)^2=S^2+2R wedge S+R^2.

Each term extends as a finite measure across D: <S^2> is finite by the
closed comparison above, R wedge S is finite since R is smooth and S has
finite trace, and R^2 is smooth. Their trivial extensions agree with the
finite-level smooth-background non-pluripolar expansion. Since <S>=S,
the actual extended positive measure is therefore

    MA_ext_theta(v)=<S^2>+2R wedge S+R^2.

Its integrated value equals

    integral K^2+2 integral R wedge K+integral R^2
        +2 integral R wedge dd^c v
      =integral theta^2+2 integral v dd^c theta.

The last pairing uses distributional Stokes with smooth R. Every genuine
quasi-psh v is L^1; no integration of v against its nonlinear measure
appears here. This is precisely why an infinite first moment causes no
obstruction to the formula.

The unchanged Haar averaging argument in the old article turns the last
expression into 2 integral a(cw+dd^c q), for a genuine cw-psh q~U on the
first curve. This curve measure is positive with total mass c. Hence the
bounds 2c min a and 2c max a hold for every original competitor and give
strictly positive finiteness.

## 4. Attainment by limits of actual type representatives

The old piecewise convex chi_L construction works for every alpha<1,
because epsilon_L=alpha(1+L)^(alpha-1) tends to zero. It gives U_L~U,
dd^c U_L>=-epsilon_L w and U_L->0 in L^1, with canonical poles retained.
Given a smooth strictly positive curve measure zeta_j of total mass c
approaching c delta_x, solve dd^c g_j=zeta_j-cw. Choose L_j so that
epsilon_(L_j) is below half the minimum density of zeta_j and
|integral U_(L_j) dd^c a|<1/j. Then g_j+U_(L_j) is an actual cw-psh
representative of the exact ordinary type U. Its integral against a tends
to c a(x). Choosing x at either extremum proves both exact mass extrema.
No energy estimate is used in this construction either.

The full-test Gauduchon formula V_mu(theta)=2c/integral(m/a)w, its actual
closed minimizing test, moving subtraction derivative, smooth gauges and
pure-pullback laws remain the same proofs under the enlarged range. The
specific old logarithmic endpoint example keeps c=1, so c>=alpha remains
valid for all alpha<1. Every such application must nevertheless be assessed
in the subsequent native review of the combined proof.

## 5. Explicit infinite first moments in the enlarged range

On a punctured disk put t=-G_p. As t->infinity,

    -U is comparable to t^alpha,
    chi''(G_p) is comparable to t^(alpha-2).

Moreover dG_p wedge d^c G_p, after angular integration, is comparable to dt
there. The singular contribution to the first moment of Cw+dd^c U is
therefore comparable to integral^infinity t^(2alpha-2) dt. The remaining
smooth-volume contribution is finite. Thus

    integral_X (-u)<S_0^2> < infinity exactly when alpha<1/2,
    integral_X (-u)<S_0^2> = infinity when 1/2<=alpha<1.

The divergence at alpha=1/2 is logarithmic. These are actual separated
closed non-pluripolar measures, not formal energy identities. They show
directly that the enlarged nonclosed finite-mass result covers references
with infinite first moment. No new assertion of weighted continuity or
finite energy in the divergent range is made.

## Exact primary application and verification boundary

The root read the complete printed statement and proof of BEGZ Theorem 1.16
(published pages 217--218; local extraction lines 932--993), Definition 1.2,
the first-current restriction identity, Proposition 1.6's complete proof,
and Theorem 1.8 with its Lemma 1.9 proof. The downloaded published primary
file is inputs/primary/BEGZ-native-2010.pdf, SHA256
7f1f53e505113fc8856f3f364f6f565592a608e43b7743003eb2b79961cdc919;
its text SHA256 is
1b4035bd5a2d88f8872f882b34694a9f2ff1f30ee38cef644f4ad584a1d3b144.

No unproved arbitrary-unbounded-locus monotonicity is used. The source's
normalization rescales the currents and products by positive fixed factors;
the comparison and equality assertions are invariant under this convention
change, and our numeric masses are computed with the original S18 forms.
Proposition 1.4(c)'s source omits its proof; this supplement instead needs
only the finite polynomial identity on the locally bounded complement,
followed by the just established finite trivial extensions.

This is a private proposed strengthening, pending an independent proof of
every implication. The full original S18 request and all prior frozen
inputs remain unchanged. Known background mass comparison is credited to
BEGZ; a fresh literature/known-overlap assessment is still required before
any article release or novelty claim.


## Entire older finite-first-moment source, unchanged historical range only

Path: papers/S18-nonanalytic-ruled-moving-volumes.tex
SHA256: 330d782496d3f57bbab2646c4c2afb102b89622f81d41cf9b98e042af7e03011

\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{proposition}{Proposition}
\newcommand{\ddc}{dd^c}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\ext}{\mathrm{ext}}
\newcommand{\PP}{\mathbb P}
\title{Nonanalytic imposed poles and moving volume data on a ruled surface}
\author{}
\date{4 October 2026}
\begin{document}
\maketitle
\noindent\textbf{Working draft.} The root-developed claims in this document
have not passed independent reconstruction or full native mathematical review.
This source is not a checked publication.

\begin{abstract}
We propose a concrete moving-volume construction on $\PP^1\times\PP^1$
with a positive genuinely nonclosed background and an imposed unbounded
nonanalytic ordinary singularity type. The upper and lower masses optimize
over every potential of that type, including rough fiber-dependent potentials.
They are distinct from the fixed-density Gauduchon variational volume, whose
full-test infimum and subtraction cost admit explicit formulas. A smooth nef
endpoint gives logarithmic variational degeneration while the upper singularity
mass stays positive. Exact smooth-gauge and pure-pullback laws distinguish
these data from exceptional-curvature subtraction and from arbitrary changes
of the reference density. This is a proposed scoped construction; the general
nonclosed moving-product programme is not resolved.
\end{abstract}

\section{Definitions and proposed results}
Use $\ddc=(i/(2\pi))\partial\bar\partial$ and
$d^c=(i/(4\pi))(\bar\partial-\partial)$. Let $w$ be the Fubini--Study
probability form on $\PP^1$, and write $w_1,w_2$ for its pullbacks to
$X=\PP^1\times\PP^1$. In an affine coordinate,
\[
 w=\frac{i\,dz\wedge d\bar z}{2\pi(1+|z|^2)^2},\qquad
 G_0=\log\frac{|z|^2}{1+|z|^2},\qquad \ddc G_0=[0]-w.
\]
Unitary transport gives $G_p$ for any $p\in\PP^1$, normalized by
$\max G_p=0$. Fix $0<\alpha<1/2$ and set
\[
 U=1-(1-G_p)^\alpha,\qquad u=\operatorname{pr}_1^*U,
 \qquad D=\{p\}\times\PP^1.
\]
All potentials use their genuine canonical upper representatives. We write
$v\sim u$ for bounded difference, with the inequalities retained at common
poles. For $c\geq\alpha$ and a smooth function $a>0$ on the first factor,
put $\theta=cw_1+aw_2$ and define
\[
 \sigma_-(\theta,u)=\inf_{v\in\PSH(X,\theta),\ v\sim u}
              \MA^{\ext}_\theta(v)(X),\qquad
 \sigma_+(\theta,u)=\sup_{v\in\PSH(X,\theta),\ v\sim u}
              \MA^{\ext}_\theta(v)(X).
\]
The products are the finite-level non-pluripolar products, expanded against
the smooth background. These extrema concern the entire ordinary type.

\begin{theorem}\label{thm:mass}
The reference $u$ is $\theta$-psh and has an unbounded nonanalytic pole on
$D$, zero Lelong numbers, and $\mathcal I(tu)=\mathcal O_X$ for every $t>0$.
Every $v\in\PSH(X,\theta)$ with $v\sim u$ has positive finite mass and
\begin{align}
 \MA^{\ext}_\theta(v)(X)
     &=\int_X\theta^2+2\int_Xv\,\ddc\theta,\label{eq:linear-mass}\\
 \sigma_-(\theta,u)&=2c\min a,\qquad
 \sigma_+(\theta,u)=2c\max a.\label{eq:extrema}
\end{align}
Both bounds are approached by actual representatives of that exact type.
When $a$ is nonconstant the smooth positive background is nonclosed.
\end{theorem}

For a smooth positive $m$ on the first factor with $\int m w=1$, let
$\mu=mw_1w_2$. For a smooth positive Gauduchon test $T$ of bidegree $(1,1)$,
so that $\ddc T=0$, define
\[
 D_\mu(T)=\int_X\sqrt{T^2/\mu}\,\mu,\qquad
 \lambda_\mu(\theta)=\inf_T\frac{\int_X\theta\wedge T}{D_\mu(T)},
 \qquad V_\mu(\theta)=\lambda_\mu(\theta)^2.
\]
Every smooth positive Gauduchon test is included in this infimum.

\begin{theorem}\label{thm:dual}
Writing $H=\int_{\PP^1}(m/a)w$, one has
\[
 V_\mu(\theta)=\frac{2c}{H}.
\]
The infimum is attained by the smooth positive closed test
\[
 T=\frac ga w_1+w_2,\qquad g=\frac{V_\mu(\theta)m}{2a}.
\]
The mass extrema in \eqref{eq:extrema} are independent of $m$, whereas
this fixed-density volume can depend on $m$ when $a$ is nonconstant.
\end{theorem}

\section{The imposed type and small-background representatives}
Let $\chi(t)=1-(1-t)^\alpha$ for $t\leq0$. Then
\[
 \chi'(t)=\alpha(1-t)^{\alpha-1},\qquad
 \chi''(t)=\alpha(1-\alpha)(1-t)^{\alpha-2}.
\]
On the punctured curve,
$\ddc U=-\chi'(G_p)w+\chi''(G_p)dG_p\wedge d^cG_p\geq-\alpha w$.
After adding a local potential of $\alpha w$, this is a locally bounded-above
psh function on the punctured disk. Its genuine psh extension has the same
lower curvature bound. Its logarithmic coefficient is zero, since
$U/\log|z-p|\to0$. In particular the positive curve current
$Cw+\ddc U$ has no atom at $p$ for $C\geq1$.
The same local calculation proves $u\in\PSH(X,\theta)$.
Moreover $e^{-tU}$ grows more slowly than every fixed negative power of
$|z-p|$, and hence is locally integrable for every $t>0$. All holomorphic
germs are therefore in $\mathcal I(tu)$. An unbounded analytic singularity
on this smooth divisor has a positive logarithmic coefficient; the imposed
type is thus genuinely nonanalytic.

\begin{lemma}\label{lem:small}
There are $U_L\sim U$ with $\sup U_L=0$,
$\ddc U_L\geq-\varepsilon_Lw$, $\varepsilon_L\to0$, and
$U_L\to0$ in $L^1(\PP^1)$.
\end{lemma}
\begin{proof}
For $L>0$ put $\varepsilon_L=\chi'(-L)$ and define
\[
 \chi_L(t)=
 \begin{cases}
   \chi(t)+C_L,&t<-L,\\
   \varepsilon_Lt,&-L\leq t\leq0,
 \end{cases}\qquad
 C_L=-\varepsilon_LL-\chi(-L).
\]
The two values and first derivatives match. This is convex with
$0\leq\chi_L'\leq\varepsilon_L$. Set $U_L=\chi_L(G_p)$.
The preceding local extension argument, or smooth convex approximation
followed by local decreasing convergence, gives its genuine curvature bound.
Near $p$ the difference $U_L-U$ is the finite constant $C_L$; on the remaining
compact part it is bounded. Thus $U_L\sim U$, including their common pole.
Here $C_L\geq0$: with $x=1+L$, the function
$(1-\alpha)x^\alpha+\alpha x^{\alpha-1}-1$ vanishes at $x=1$ and has
nonnegative derivative for $x\geq1$. On $[-L,0]$, convexity gives
$\chi(t)\leq\chi'(-L)t$. Consequently $U\leq U_L\leq0$.
For each point other than $p$, eventually $U_L=\varepsilon_LG_p\to0$.
Since $U\in L^1$, dominated convergence proves the stated $L^1$ limit.
\end{proof}

This supplies actual small-background representatives without erasing the
pole by a maximum with a bounded function. If a smooth $g$ satisfies
$cw+\ddc g\geq\delta w$, then $g+U_L$ is $cw$-psh for
$\varepsilon_L<\delta$ and remains of the ordinary type $U$.

\section{All rough competitors and the mass extrema}
We use the closed K\"ahler energy foundations of \cite{BEGZ},
Definitions~2.7 and~2.9 and Propositions~2.8, 2.10 and~2.11. Finite
Aubin--Mabuchi energy is stable under making a potential less singular and
under finite constants, and implies full closed top mass. For a full-mass
potential it is equivalent to a finite first moment against its closed
Monge--Amp\`ere measure. These statements are applied only to a closed
strict K\"ahler form, not to $\theta$.

Choose $K=C(w_1+w_2)$, with $C$ sufficiently large that $K\geq\theta$
and $C\geq1$. The separated closed product of $u$ is
\[
 \MA_K^{\ext}(u)=2C(Cw_1+\ddc u)w_2.
\]
The curve current has total mass $C$ by distributional Stokes and no atom
at $p$ by its zero logarithmic coefficient. Thus this product has full
mass $\int K^2=2C^2$. Its first moment is finite: near $p$, writing
$t=-G_p$, the singular part of the curve integral is bounded by a constant
times $\int^\infty t^{2\alpha-2}\,dt$, which converges for $\alpha<1/2$;
the smooth-volume part is integrable as well. Hence $u$ has finite $K$-energy.

Now take any $v\in\PSH(X,\theta)$ with $v\sim u$. It is $K$-psh and
$v\geq u-A$ for a finite $A$, so it too has finite $K$-energy and full
closed top mass. After subtracting a constant assume $v\leq0$. Then
$v/2\geq v$ also has finite energy and full mass. Both are locally bounded
on $X\setminus D$. Write $S=K+\ddc v$ and $J=(S+K)/2$. Local
Bedford--Taylor expansion on this complement, and trivial extension over
the pluripolar divisor, give
\[
 \langle J^2\rangle=\tfrac14\langle S^2\rangle
                   +\tfrac12\langle S\wedge K\rangle+\tfrac14K^2.
\]
The first, second and last top masses are $\int K^2$. Consequently
$\int\langle S\wedge K\rangle=\int K^2=\int S\wedge K$.
Since the first non-pluripolar current is $S$ restricted off $D$, this says
that the positive trace measure $S\wedge K$ has zero mass on $D$.
Strict positivity of $K$ implies $1_DS=0$, and hence $\langle S\rangle=S$.
This argument supplies the required first-current identity without a
divisorial decomposition assumption.

Set $R=\theta-K$. The finite-level smooth-background expansion now gives
\[
 \MA_\theta^{\ext}(v)=\langle S^2\rangle+2R\wedge S+R^2.
\]
All terms are finite signed measures, and the left side is positive.
Integrating, using full closed mass and distributional Stokes, gives
\[
 \int K^2+2\int R\wedge K+\int R^2+2\int R\wedge\ddc v
     =\int\theta^2+2\int v\,\ddc\theta.
\]
This proves \eqref{eq:linear-mass}, including for every rough competitor.

Average $v$ over the compact unitary action on the second factor.
The background is invariant. Averaging its current inequality and using
canonical psh representatives gives a genuine invariant potential
$\operatorname{pr}_1^*q$, with $q\sim U$. For completeness, local addition
of a smooth sufficiently positive quadratic makes all translates psh;
their Haar average is locally integrable by Fubini, satisfies the submean
inequality, and has its canonical upper representative. The bounded
inequalities with $u$ pass through the average and then through canonical
regularization. Off $D$ the average is finite, and on $D$ it equals
$-\infty$. Positivity says $cw+\ddc q\geq0$.

Since $\ddc\theta=\ddc a\wedge w_2$, the functional in
\eqref{eq:linear-mass} is unchanged by this averaging, and
\[
 \MA_\theta^{\ext}(v)(X)=2\int_{\PP^1}a(cw+\ddc q).
\]
The measure in parentheses is positive of total mass $c$. This proves both
global bounds and positive finiteness.

To approach either bound, choose a point $x$ attaining the corresponding
extremum of $a$. There are smooth strictly positive curve measures
$\zeta_j$ of total mass $c$ converging weakly to $c\delta_x$; for instance,
combine a smooth approximate identity near $x$ with a small positive
multiple of $w$. Solve $\ddc g_j=\zeta_j-cw$ on the sphere. The smooth
solution exists because the right side has zero integral, either by the
explicit Green kernel or by the zero-mean scalar Poisson equation.
For each $j$ choose $L_j$ so large that
$\varepsilon_{L_j}$ is smaller than half the positive lower bound of
$\zeta_j/w$ and $|\int U_{L_j}\ddc a|<1/j$.
Then $g_j+U_{L_j}$ is an actual $cw$-psh representative of $U$'s type and
\[
 \int a(cw+\ddc(g_j+U_{L_j}))\longrightarrow c a(x).
\]
Pulling back proves both exact extrema in Theorem~\ref{thm:mass}.

\section{The full Gauduchon formula and its moving cost}
Let $H=\int(m/a)w$, $V=2c/H$ and $g=Vm/(2a)$, so $\int gw=c$.
Choose a smooth $b$ with $\ddc b=(g-c)w$. Then
\[
 \Omega=\theta+\ddc\operatorname{pr}_1^*b=gw_1+aw_2>0,
 \qquad\Omega^2=V\mu.
\]
For every smooth positive Gauduchon test $S$, Stokes and the pointwise
two-dimensional arithmetic--geometric mean inequality give
\[
 \int\theta\wedge S=\int\Omega\wedge S
       \geq\sqrt V\int\sqrt{S^2/\mu}\,\mu=\sqrt V D_\mu(S).
\]
The test $T=\Omega/a=(g/a)w_1+w_2$ is positive and closed, because its
first coefficient depends only on the first curve. Moreover
\[
 \int\theta T=2c,\qquad T^2=\frac{Vm}{a^2}w_1w_2,
 \qquad D_\mu(T)=\sqrt V H.
\]
It attains the lower bound, proving Theorem~\ref{thm:dual} for all tests.

For $c_s=c-sd\geq\alpha$, $a_s=a-sb>0$ on a parameter interval, put
$\theta_s=c_sw_1+a_sw_2$ and $\eta=dw_1+bw_2$. Keep $m$ fixed, and
use the preceding notation with subscript $s$. Direct differentiation gives
\[
 H_s'=\int\frac{bm}{a_s^2}w,\qquad
 \int\eta T_s=d+\frac{V_s}{2}H_s',\qquad
 \frac{d\sqrt{V_s}}{ds}
       =-\frac{\int\eta T_s}{D_\mu(T_s)}.
\]
This is the actual full-test subtraction derivative. Its integral on any
compact positive segment equals the difference of the two endpoint root
volumes. It is separate from the upper and lower singularity masses.

\section{A logarithmic nef endpoint}
Let $c=1$, $m=1$, and
$\tau=(|z|^2-1)/(|z|^2+1)$ on the first sphere. Its distribution under
$w$ is $d\tau/2$ on $[-1,1]$: radial integration gives
$dt/(1+t)^2=d\tau/2$, with $t=|z|^2$. Take $a=2+\tau$ and subtract
$\eta=w_2$. For $0\leq s<1$,
\[
 H_s=\frac12\log\frac{3-s}{1-s},\qquad
 V_s=\frac4{\log((3-s)/(1-s))},\qquad
 \sigma_-(s)=2(1-s),\quad\sigma_+(s)=2(3-s).
\]
At $s=0$ the raw zero-potential mass is $2\int a w=4$, while the lower
mass, upper mass and fixed-density volume are $2$, $6$ and $4/\log3$.
All these backgrounds are genuinely nonclosed. As $s\uparrow1$ the root
volume tends to zero and its derivative is
\[
 -\frac{2}{(1-s)(3-s)[\log((3-s)/(1-s))]^{3/2}}.
\]
The improper integral of the cost is finite, equal to $2/\sqrt{\log3}$.
The upper singularity mass instead tends to $4$.

The endpoint $\theta_1=w_1+(1+\tau)w_2$ is smooth semipositive and nef,
since adding any positive multiple of $w_1+w_2$ makes it positive. Its
all-test root-volume infimum is zero, by nonnegativity and comparison with
$\theta_s$. It is not big. Indeed a strict current would dominate
$\varepsilon(w_1+w_2)$ after changing $\varepsilon>0$. Averaging its
potential over the second sphere preserves that strict inequality and
produces a genuine base potential. Its vertical coefficient is still
$1+\tau$, which would therefore have to be at least $\varepsilon$
almost everywhere. This is impossible near its zero fiber.
The endpoint thus lies outside the big segment; it is not a counterexample
to any asserted equivalence between bigness and positive variational volume.

\section{Smooth gauges and pure pullback}
For smooth real $f$, set $\theta'=\theta+\ddc f$, $u'=u-f$ and $v'=v-f$.
The actual currents coincide, so the finite-level local construction
transports the extended measure and both mass extrema. Against every
Gauduchon test the numerator also coincides by Stokes. A parameter-dependent
smooth gauge contributes $\ddc\dot f_s$ to the derivative and its pairing
with $T_s$ is zero.

\begin{proposition}\label{prop:mod}
For a proper modification $\pi:Y\to X$ between smooth connected compact
complex manifolds and a smooth real background $\theta$, pullback is a
canonical bijection of the genuine $\theta$-psh functions with the genuine
$\pi^*\theta$-psh functions. Ordinary types correspond. For these
potentials,
\[
 \pi_*\MA_{\pi^*\theta}^{\ext}(\pi^*v)=\MA_\theta^{\ext}(v).
\]
Thus the mass extrema are preserved for the pure pullback background and
type whenever the class of competitors is nonempty.
\end{proposition}
\begin{proof}
Let $Z$ be an analytic center containing the non-isomorphism locus.
On a relatively compact coordinate ball choose smooth $\rho$ with
$\ddc\rho\geq\theta$. If $b$ is $\pi^*\theta$-psh, then
$b+\pi^*\rho$ is psh upstairs. Off $Z$ it descends to a psh function;
properness and local upper bounds upstairs give a local upper bound near
$Z$. The removable-singularity theorem \cite[I.5.23--5.24]{Demailly}
gives the unique canonical psh extension. Subtracting $\rho$ gives a genuine
quasi-psh function downstairs. Its sharper $\theta$-positivity holds off
$Z$ and also on $Z$: the added current on $Z$ is positive, whereas the
smooth correction has no mass there. Pullback agrees upstairs off the
exceptional analytic set, hence almost everywhere, and the two genuine
quasi-psh representatives agree canonically. The converse follows from
local psh pullback and the current bound.

Bounded inequalities descend off $Z$ and hold everywhere by canonical
recovery of quasi-psh functions from their almost-everywhere values. Thus
ordinary equivalence is preserved in both directions. Off the exceptional
set all finite-level local products transform by the biholomorphism.
Each bounded local product, and then each non-pluripolar product, gives
zero mass to analytic pluripolar sets; this remains true for the
smooth-background expansion. Both extended measures therefore give zero
mass to the respective excluded analytic sets. The equality on their
complements proves the measure identity, even when total mass is infinite.
Taking the full infimum and supremum over the bijective type proves the
last assertion.
\end{proof}

For a point blowup the pullback backgrounds in the positive segment are
also big. One direct justification uses the exceptional divisor $E$.
Choose a smooth curvature $\beta_E$ of $\mathcal O(E)$ whose restriction
to $E$ is the negative Fubini--Study form. For a closed K\"ahler form
$K_0=w_1+w_2$, the form $\pi^*K_0-t\beta_E$ is K\"ahler for sufficiently
small $t>0$. Here is the local positivity check. In finitely many blowup
charts $(x,y)\mapsto(x,xy)$ with $y$ in compact sets, the matrix $P$ of
$\pi^*K_0$ satisfies $P_{x\bar x}\geq c_0>0$,
$|P_{x\bar y}|\leq C|x|$, and its Schur complement is at least
$c_1|x|^2$. For $B=-\beta_E$, shrink a fixed chart neighborhood so that
$B_{y\bar y}\geq b_0>0$, with all entries bounded. The transverse
coefficient of $P+tB$ is at least $c_0/2$ for small $t$, and its Schur
complement is at least
\[
 c_1|x|^2+t b_0-C'\bigl(t|x|+t|x|^2+t^2\bigr).
\]
First fix the neighborhood small enough, then $t$ small enough, to make
the last three terms at most $t b_0/2$. This proves strict positivity on
that fixed neighborhood. On its compact complement, strict positivity
of $\pi^*K_0$ persists under the bounded perturbation. The metric with
the required restriction to $E$ exists because
$\mathcal O(E)|_E=\mathcal O_{\PP^1}(-1)$: extend its negative
Fubini--Study metric smoothly to the line bundle. If $\theta_s\geq a_0K_0$ and
$\ddc\ell_E=[E]-\beta_E$, then
\[
 \pi^*\theta_s+\ddc(a_0t\ell_E)
   \geq a_0(\pi^*K_0-t\beta_E)+a_0t[E]
\]
is an actual strict current. This gives a nonclosed big example upstairs.
Subtracting exceptional curvature is a different background, and is not
covered by Proposition~\ref{prop:mod}'s equality. Nor do we identify an
arbitrary smooth positive upstairs probability with $\pi^*\mu$, which
degenerates on $E$.

The construction does not assert a general nonclosed positive-product
theory, unrestricted birational equality for changed backgrounds,
density-independent Gauduchon volume, or a solution of the general
nef-endpoint bridge. The closed energy results in \cite{BEGZ} supply only
the stated closed foundations; the nonclosed optimization and full-test
calculation have their separate proofs above.

\begin{thebibliography}{9}
\bibitem{BEGZ} S.~Boucksom, P.~Eyssidieux, V.~Guedj and A.~Zeriahi,
\emph{Monge--Amp\`ere equations in big cohomology classes},
Acta Math. \textbf{205} (2010), 199--262.
\href{https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf}{Author-hosted published primary text}.
\bibitem{Demailly} J.-P.~Demailly, \emph{Complex Analytic and Differential
Geometry}, Chapter~I, Theorems~5.23--5.24.
\href{https://people.math.harvard.edu/~siu/2dmml.pdf}{University-hosted primary text}.
\end{thebibliography}
\end{document}


## Entire checked S11 companion source; mathematical applications require reassessment

Path: papers/S11-nonclosed-ruled-restricted-masses-and-strict-types.tex
SHA256: 792430edafae59f6c159735db721d80f10b8a58ec199d6050ca0524d5be3e4dd

\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\ddc}{dd^{\mathrm c}}
\newcommand{\dc}{d^{\mathrm c}}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\PP}{\mathbb P}
\title{Restricted masses and ordinary strict-current types\newline
on a nonclosed ruled surface}
\author{Research manuscript}
\date{October 7, 2026}
\begin{document}
\maketitle
\begin{center}
\small Checked restricted construction. General S11 remains open.
\end{center}
\begin{abstract}
We propose restricted mass data for a concrete nonclosed background on a
ruled surface, with a logarithmic imposed divisor and an unbounded
nonanalytic residual. We optimize over every rough representative of the
ordinary singularity type and compute all intrinsic ideal trace orders in
a declared ambient embedding. The admissible type contains a strict current
exactly below an explicit divisorial threshold. Its two optimized masses
are preserved by pure pullback, whereas blowing up a point away from the
poles obstructs a strict current in the pulled-back ordinary type. A
one-sided strict witness still exists. The Gauduchon subtraction cost of
the residual background is computed separately. This is a proposed
restricted construction; the general Hermitian restricted-positivity
programme remains open.
\end{abstract}

\section{The construction}
Use $\ddc=(i/(2\pi))\partial\bar\partial$ and
$\dc=(i/(4\pi))(\bar\partial-\partial)$. Let $w$ be the probability
Fubini--Study form on $\PP^1$, and let $w_1,w_2$ denote its pullbacks to
$Y=\PP^1\times\PP^1$. For $p\in\PP^1$ let $G_p\leq0$ be the canonical
Green potential with $\ddc G_p=[p]-w$ and $\max G_p=0$. Write
\[
 D=\{p\}\times\PP^1,\qquad
 U=1-(1-G_p)^\alpha,\qquad
 r=bG_p+U,\qquad 0<\alpha<1,
\]
and pull these functions to $Y$. Fix $c>0$, $b\geq0$, and a smooth
strictly positive function $a$ on the first curve. Put
\[
 \theta=cw_1+aw_2.
\]
This background is strictly positive and is nonclosed when $a$ is
nonconstant. All functions use genuine canonical quasi-psh representatives.
When $b=0$, the function $bG_p$ is identically zero, including at $p$.
Ordinary equivalence $v\sim r$ means bounded difference, with the
inequalities retained at common poles. The function $r$ specifies a type;
its admissibility is a conclusion rather than an assumption.

For a nonempty admissible type define
\[
 R_-(\theta,[r])=\inf_{\substack{v\in\PSH(Y,\theta)\\v\sim r}}
                   \MA^{\rm ext}_\theta(v)(Y),\qquad
 R_+(\theta,[r])=\sup_{\substack{v\in\PSH(Y,\theta)\\v\sim r}}
                   \MA^{\rm ext}_\theta(v)(Y).
\]
The products are the finite-level non-pluripolar products with the smooth
background expansion. Every full-variable competitor is included.

\newpage
\begin{theorem}\label{thm:mass}
The specified ordinary type is nonempty precisely when $b<c$. In that
range it contains a genuine potential $v$ with
$\theta+\ddc v\geq\varepsilon(w_1+w_2)$ for some $\varepsilon>0$.
Every competitor has positive finite extended mass, and
\begin{align}
 \MA^{\rm ext}_\theta(v)(Y)
   &=\int_Y\theta^2-2b a(p)+2\int_Yv\,\ddc\theta,\label{eq:affine}\\
 R_-(\theta,[r])&=2(c-b)\min a,\qquad
 R_+(\theta,[r])=2(c-b)\max a.\label{eq:extrema}
\end{align}
Both extremal values are approached by actual representatives of that
ordinary type. No finite first-moment hypothesis is required.
\end{theorem}

This is an unbounded residual construction. It uses closed mass comparison
within its compact K\"ahler hypotheses \cite{BEGZ}; it does not assert
intersection invariance for the nonclosed form $\theta$.
The ordinary-type volume definitions and divisor and pure-pullback laws
under bounded mass are established background
\cite[Definition~3.1 and Proposition~3.3]{BGL}. Our purpose is their explicit
optimization in the declared nonanalytic family, including infinite first
moments. The companion manuscript \cite{Companion} records bounded-residual
trace formulas, divisorial normalization, residual Gauduchon calculations
and the local exceptional-curve obstruction. Their mechanisms retain their
existing credit; the obstruction below applies where our residual is bounded
near the chosen blowup center. No priority claim is made.

\section{Retaining the unbounded residual}
Let $\chi(t)=1-(1-t)^\alpha$ for $t\leq0$. Then
\[
 0<\chi'(t)=\alpha(1-t)^{\alpha-1}\leq\alpha,
 \qquad \chi''(t)=\alpha(1-\alpha)(1-t)^{\alpha-2}>0.
\]
The punctured-disk calculation gives
$\ddc U\geq-\alpha w$. The canonical removable-singularity theorem
\cite[I.5.23--5.24]{Demailly} extends this inequality across $p$.
The Lelong number is zero, since $U/\log|z-p|\to0$.

\begin{lemma}\label{lem:small}
There are genuine $U_L\sim U$ with $\sup U_L=0$,
$\ddc U_L\geq-\varepsilon_Lw$, $\varepsilon_L\to0$, and $U_L\to0$
in $L^1(\PP^1)$.
\end{lemma}
\begin{proof}
Put $\varepsilon_L=\chi'(-L)$ and
\[
 \chi_L(t)=
 \begin{cases}
  \chi(t)+C_L,&t<-L,\\
  \varepsilon_Lt,&-L\leq t\leq0,
 \end{cases}
 \qquad C_L=-\varepsilon_LL-\chi(-L).
\]
The values and derivatives match; $\chi_L$ is convex and increasing,
with $0\leq\chi_L'\leq\varepsilon_L$. The same curvature and canonical
extension argument applies to $U_L=\chi_L(G_p)$. Near $p$, $U_L-U=C_L$;
elsewhere the difference is bounded. Thus the mutual type and pole persist.
Writing $x=1+L$ gives
$C_L=(1-\alpha)x^\alpha+\alpha x^{\alpha-1}-1\geq0$.
Convexity also gives $\chi(t)\leq\varepsilon_Lt$ for $t\in[-L,0]$.
Hence $U\leq U_L\leq0$, and $U_L\to0$ pointwise off $p$.
Dominated convergence proves the $L^1$ assertion.
\end{proof}

\begin{lemma}\label{lem:remove}
Subtraction of the divisorial potential gives a canonical bijection
\[
 \{v\in\PSH(Y,\theta):v\sim r\}
 \longleftrightarrow
 \{q\in\PSH(Y,\beta):q\sim U\},\qquad
 \beta=(c-b)w_1+aw_2,
\]
and
\[
 \theta+\ddc(bG_p+q)=b[D]+\beta+\ddc q,
 \qquad \MA^{\rm ext}_\theta(bG_p+q)=\MA^{\rm ext}_\beta(q).
\]
\end{lemma}
\begin{proof}
Initially set $q=v-bG_p$ off $D$. In a chart write
$G_p=\log|z_1|^2-\sigma$, $\ddc\sigma=w_1$, and choose a quadratic
$\rho$ with $\ddc\rho\geq\theta$. The function
$v+\rho-b\log|z_1|^2=q+\rho-b\sigma$ is psh off $D$ and locally
bounded above, because $q\leq U+C$. Extend it canonically across $D$.
Its current retains the sharper lower bound $\ddc\rho-\theta$:
off $D$ that bound holds, and on $D$ its coefficient measures are positive
while the smooth correction has zero measure restriction. Subtracting
$\rho-b\sigma$ yields $\beta+\ddc q\geq0$.
The ordinary inequalities extend canonically; the upper bound forces the
same pole on $D$. Poincar\'e--Lelong gives the current identity. Conversely
that identity proves admissibility of $bG_p+q$. The two genuine functions
coincide canonically when they coincide almost everywhere.
Off $D$ their locally bounded residual products agree. Both non-pluripolar
products, including their smooth-background expansions, vanish on $D$.
This proves the measure identity.
\end{proof}

If $b<c$, choose $L$ with $\varepsilon_L<(c-b)/2$. Then
\[
 \theta+\ddc(bG_p+U_L)
 \geq b[D]+(c-b-\varepsilon_L)w_1+aw_2
 \geq\min((c-b)/2,\min a)(w_1+w_2).
\]
This is a strict witness in the mutual ordinary type. Conversely, average
the residual $q$ in Lemma~\ref{lem:remove} over the unitary group of the
second sphere. The background is invariant. Canonical Haar averaging gives
a genuine first-factor potential $q_0\sim U$ with
$(c-b)w+\ddc q_0\geq0$. Its total measure is $c-b$. Positivity excludes
$b>c$. If $b=c$, the measure is zero and the genuine harmonic $q_0$ is
constant on the compact curve, contradicting $q_0\sim U$.

\section{The full rough-class mass computation}
Suppose $k=c-b>0$ and put $\beta=kw_1+aw_2$. Choose $L_0$ with
$\varepsilon_{L_0}<k/2$, and use $u_0=U_{L_0}$ as an admissible residual
reference. Choose $C$ large enough that the closed K\"ahler form
$K=C(w_1+w_2)$ dominates $\beta$. The separated current
$S_0=K+\ddc u_0$ has no measure component on $D$: the first-factor
measure has zero atom at $p$. Consequently
\[
 \langle S_0\rangle=S_0,\qquad
 \langle S_0^2\rangle=2C(Cw_1+\ddc u_0)w_2,
 \qquad\int_Y\langle S_0^2\rangle=\int_YK^2.
\]
Now let $q\in\PSH(Y,\beta)$ be any competitor with $q\sim U$, and put
$S=K+\ddc q$. Both currents are closed and positive in the same K\"ahler
class. Their potentials have bounded difference and are locally bounded
off the closed complete pluripolar divisor $D$. BEGZ Theorem~1.16 applied
in both ordinary orders, for $p=1$ and $p=2$, gives
\[
 \{\langle S\rangle\}=\{K\},\qquad
 \int_Y\langle S^2\rangle=\int_YK^2.
\]
The positive polar current $S-\langle S\rangle=1_DS$ has zero trace
against $K$, and therefore vanishes. This proves $\langle S\rangle=S$.
All uses of closed cohomology concern $K$, rather than $\beta$.

Write $R=\beta-K$. Local bounded Bedford--Taylor expansion off $D$,
followed by finite trivial extension, gives
\[
 \MA^{\rm ext}_\beta(q)=\langle S^2\rangle+2R\wedge S+R^2.
\]
The terms are finite: the first has the closed mass just computed, the
second pairs a smooth form with a current of finite trace, and the last
is smooth. Distributional Stokes thus proves
\[
 \MA^{\rm ext}_\beta(q)(Y)=\int_Y\beta^2+2\int_Yq\,\ddc\beta.
\]
This pairing needs only $q\in L^1$, rather than a first moment against
its nonlinear measure. Haar averaging on the second factor preserves the
last expression and yields
\[
 \MA^{\rm ext}_\beta(q)(Y)=2\int_{\PP^1}a(kw+\ddc q_0).
\]
The curve measure is positive of total mass $k$, proving both bounds in
\eqref{eq:extrema} for every original competitor.

For exact extremizing sequences choose smooth strictly positive measures
$\zeta_j$ of mass $k$ converging to $k\delta_x$, and solve
$\ddc g_j=\zeta_j-kw$ on the sphere. Choose $L_j$ with
$\varepsilon_{L_j}$ below half the minimum density of $\zeta_j$ and
$|\int U_{L_j}\ddc a|<1/j$. Then $bG_p+g_j+U_{L_j}$ is a genuine
admissible representative of $r$, and its mass tends to $2k a(x)$.
Choosing $x$ at either extremum proves the formulas. Finally
$\int G_p\ddc a=a(p)-\int aw$ yields \eqref{eq:affine}.

The residual reference has infinite closed first moment when
$\alpha\geq1/2$. Indeed near $p$, writing $t=-G_p$,
$-U_{L_0}\asymp t^\alpha$ and
$\chi''(G_p)\asymp t^{\alpha-2}$. Angular integration of
$dG_p\wedge\dc G_p$ is comparable to $dt$. Its singular first moment
is comparable to $\int^\infty t^{2\alpha-2}\,dt$, finite exactly for
$\alpha<1/2$. The full mass proof above covers the divergent range too.

\section{Intrinsic ambient traces}
Embed the target as $Y_0=Y\times\{z_0\}$ in $Z=Y\times\PP^1$.
Use the strictly positive background
$\Theta=\operatorname{pr}_Y^*\theta+w_3$ and the genuine reference
$u_Z=\operatorname{pr}_Y^*(bG_p+U_L)$ chosen above.
Its generic Lelong number along $Y_0$ is zero. For the ambient divisor
$D_Z=D\times\PP^1$ and every real $s>0$,
\[
 \mathcal I(su_Z)=\mathcal O_Z(-\lfloor sb\rfloor D_Z),\qquad
 \mathcal I(su_Z)\mathcal O_{Y_0}
       =\mathcal O_{Y_0}(-\lfloor sb\rfloor D).
\]
To check the convention, factor a germ's largest transverse power
$z_1^j$. With $t=-\log|z_1|^2$, its radial integral has exponential
factor $\exp(-(j+1-sb)t+st^\alpha)$, up to bounded factors.
It converges exactly when $j+1>sb$, including divergence at equality.
A nonzero leading tangential coefficient gives necessity by Fubini;
local holomorphic bounds give sufficiency. No extra factor $2$ occurs
in the definition $|f|^2e^{-su_Z}$.

For every prime divisor $E$ on every smooth compact modification
$\pi:Y'\to Y_0$, orders of these restricted ambient principal ideals are
$\lfloor sb\rfloor\operatorname{ord}_E(\pi^*D)$. The intrinsic trace is
therefore
\[
 \tau_{(Y_0,u_Z)}(E)=b\operatorname{ord}_E(\pi^*D).
\]
This is the task's ambient-ideal definition. It asserts no commutation of
multiplier ideals with arbitrary pullback. The residual has trivial ideals
at every weight and is unbounded. At a generic point of $D$, an analytic
singularity of coefficient $b$ differs from $b\log|z_1|^2$ by a bounded
function; our residual diverges like $-t^\alpha$. Hence its ordinary type
is genuinely nonanalytic and is not determined by these ideal orders.

\section{Pure pullback and the strict-type obstruction}
Smooth gauges $(\theta,r,v)\mapsto(\theta+\ddc f,r-f,v-f)$ preserve
the actual currents, measures and both optimized masses. They preserve
multiplier ideals, since $e^{sf}$ is locally bounded above and below.

For a proper modification $\pi:Y'\to Y$, genuine
$\pi^*\theta$-psh functions descend canonically. Here is the precise
argument used for pure pullback. Add downstairs a local quadratic
$\rho$ with $\ddc\rho\geq\theta$. A potential upstairs plus
$\pi^*\rho$ is psh. Off the center it descends; properness gives a local
upper bound near the center, so canonical removability extends it.
Subtracting $\rho$ retains the sharper $\theta$ inequality: smooth
corrections have no measure restriction to the analytic center.
Pullback agrees almost everywhere, hence canonically. Ordinary bounded
inequalities descend in the same way. Off the exceptional set local
products agree by biholomorphism; non-pluripolar products vanish on the
excluded analytic sets. Thus
\[
 \pi_*\MA^{\rm ext}_{\pi^*\theta}(\pi^*v)=\MA^{\rm ext}_\theta(v).
\]
The full competitor bijection preserves both $R_-$ and $R_+$.
Exceptional curvature subtraction is a different background operation.
These are laws for the two ordinary-type masses; no invariance of
$V_\mu$ for arbitrary smooth positive upstairs probabilities is asserted.

\begin{proposition}\label{prop:blowup}
Blow up a point $y\notin D$. The pulled-back lower mass is positive and
there is a strict-current witness at most $\pi^*r$ plus a constant.
There is no strict-current witness ordinarily equivalent to $\pi^*r$.
\end{proposition}
\begin{proof}
Choose $q=U_L$ with $\beta+\ddc q\geq\delta(w_1+w_2)$.
For the exceptional divisor $E$, choose curvature $\beta_E$ of
$\mathcal O(E)$ restricting to negative Fubini--Study curvature on $E$.
For small $t>0$, $\pi^*(w_1+w_2)-t\beta_E$ is strictly positive.
For completeness, in finitely many blowup charts
$(x,y)\mapsto(x,xy)$ the pullback matrix $P$ has
$P_{x\bar x}\geq c_0$, $|P_{x\bar y}|\leq C|x|$, and Schur complement
at least $c_1|x|^2$. For $B=-\beta_E$ the vertical coefficient is
$B_{y\bar y}\geq b_0>0$ near $E$ and all entries are bounded.
The Schur complement of $P+tB$ is at least
\[
 c_1|x|^2+tb_0-C'(t|x|+t|x|^2+t^2).
\]
Fix the neighborhood small, then $t$ small, to bound the last terms by
$tb_0/2$. On the compact complement positivity persists under a small
bounded perturbation. The curvature metric extends smoothly from
$\mathcal O(E)|_E=\mathcal O_{\PP^1}(-1)$.
With $\ddc\ell_E=[E]-\beta_E$, the genuine potential
$\pi^*(bG_p+q)+\delta t\ell_E$ gives the strict lower bound
\[
 b[\pi^*D]+\delta(\pi^*(w_1+w_2)-t\beta_E)+\delta t[E].
\]
It is at most $\pi^*r$ plus a constant, but its exceptional pole changes
the ordinary type. The lower mass remains positive by pure pullback.

If $v'\sim\pi^*r$, it is locally bounded near $E$, since $y\notin D$.
Suppose $\ddc v'\geq\varepsilon h'-\pi^*\theta$ for some $h'>0$.
At each point of $E$ approximate the smooth lower bound from below by
a constant Hermitian form on a small adapted chart, with sufficiently
small scalar error. Its tangent coefficient is strictly positive, since
$\pi^*\theta|_E=0$. Subtracting a quadratic with this Hessian from $v'$
gives a genuine psh function. It restricts genuinely to $E$ because $v'$
is locally bounded. Adding back the quadratic proves that $v'|_E$ has
a strictly positive curve Hessian locally. A finite cover gives a positive
global lower bound against a probability form on $E$, contradicting
$\int_E\ddc(v'|_E)=0$. This proves the obstruction.
\end{proof}

\section{The separate Gauduchon cost}
Let $m>0$ be smooth on the first curve, $\int mw=1$, and put
$\mu=mw_1w_2$, $H=\int(m/a)w$. For all smooth positive tests $T$ with
$\ddc T=0$, set $D_\mu(T)=\int\sqrt{T^2/\mu}\,\mu$.
For $\beta=kw_1+aw_2$, $k=c-b>0$, the all-test volume is
\[
 V_\mu(\beta)=\left(\inf_T\frac{\int\beta T}{D_\mu(T)}\right)^2
      =\frac{2k}{H}.
\]
Indeed put $V=2k/H$ and $g=Vm/(2a)$, so $\int gw=k$. Solve
$\ddc f=(g-k)w$. Then $\Omega=gw_1+aw_2=\beta+\ddc f>0$ and
$\Omega^2=V\mu$. Stokes and the pointwise matrix arithmetic--geometric
mean inequality give $\int\beta T\geq\sqrt V D_\mu(T)$ for every test.
The closed positive test $T=(g/a)w_1+w_2$ attains it:
\[
 \int\beta T=2k,\qquad D_\mu(T)=\sqrt V H.
\]
This volume depends on $m$, whereas $R_\pm$ do not. It generally differs
from $R_+$; the original background has the separate volume $2c/H$.

Fix a real constant $d$ and a smooth real first-factor function $e$.
For $c_s=c-sd>b$, $a_s=a-se>0$, with fixed $b,m$, set
$k_s=c_s-b$, $H_s=\int(m/a_s)w$, $V_s=2k_s/H_s$ and use the preceding
minimizer $T_s$. Differentiation gives
\[
 H_s'=\int\frac{em}{a_s^2}w,\qquad
 \int(d w_1+e w_2)T_s=d+\frac{V_s}{2}H_s',\qquad
 \frac{d\sqrt{V_s}}{ds}
   =-\frac{\int(d w_1+e w_2)T_s}{D_\mu(T_s)}.
\]
Integration on every compact positive segment gives the actual residual
Gauduchon subtraction cost. It is not a derivative of $R_+$, and no
arbitrary smooth upstairs density is identified with a degenerate pullback.

\section{A concrete nonclosed example}
Let $\tau=(|z|^2-1)/(|z|^2+1)$ be the standard height on the first
sphere, with distribution $d\tau/2$ under $w$. Take
\[
 c=1,\qquad b=\frac14,\qquad \alpha=\frac34,\qquad
 a=2+\tau,\qquad m=1.
\]
For example $L=31$ gives
$\varepsilon_L=(3/4)32^{-1/4}<3/8$, so $bG_p+U_{31}$ is an actual
strict representative of the required nonanalytic type. Its residual has
infinite closed first moment. The full optimized masses and residual
Gauduchon volume are
\[
 R_-=\frac32,\qquad R_+=\frac92,\qquad
 H=\frac12\log3,\qquad V_\mu(\beta)=\frac3{\log3}.
\]
The original background instead has $V_\mu(\theta)=4/\log3$.
The ambient intrinsic orders are
$\tau(E)=\tfrac14\operatorname{ord}_E(\pi^*D)$ on every modification.
Blowing up any point outside $D$ preserves $R_-=3/2$ and $R_+=9/2$,
while Proposition~\ref{prop:blowup} excludes a strict current in the
pulled-back mutual ordinary type. The target backgrounds $\theta$, $\beta$,
$\Theta$ and their pure pullbacks are genuinely nonclosed; the auxiliary
$K$ is closed. The residual pole has not been replaced by a bounded or
analytic singularity.

\begin{remark}
Positive restricted lower mass supplies a mutual ordinary strict witness
downstairs within this declared family. It is preserved upstairs as a mass
invariant, while Proposition~\ref{prop:blowup} supplies only a one-sided
strict witness. The construction does not furnish a strict-type criterion
for arbitrary Hermitian backgrounds or solve the unrestricted S11 direction.
\end{remark}

\begin{thebibliography}{9}
\bibitem{BGL} S.~Boucksom, V.~Guedj and C.~H.~Lu,
\emph{Volumes of Bott--Chern Classes}, Peking Mathematical Journal (2025),
\href{https://doi.org/10.1007/s42543-025-00105-2}{doi:10.1007/s42543-025-00105-2},
especially Definition~3.1 and Proposition~3.3.
\href{https://d-nb.info/1374372846/34}{Published primary text}.
\bibitem{BEGZ} S.~Boucksom, P.~Eyssidieux, V.~Guedj and A.~Zeriahi,
\emph{Monge--Amp\`ere equations in big cohomology classes},
Acta Math. \textbf{205} (2010), 199--262, especially Definition~1.2,
Proposition~1.6 and Theorem~1.16.
\href{https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf}{Published primary text}.
\bibitem{Demailly} J.-P.~Demailly, \emph{Complex Analytic and Differential
Geometry}, Chapter~I, Theorems~5.23--5.24.
\href{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf}{Author-hosted primary text}.
\bibitem{Companion} \emph{Non-K\"ahler pluripotential theory}, companion
manuscript: resolved trace masses, divisorial normalization and type
thresholds, divisorial Gauduchon volume and residual families.
\href{https://github.com/MingchenXia/non-kahler-pluripotential-theory/tree/1ff73204b833e197437c62dbe172815cb417bf7b/book/author}{Retained source version}.
\end{thebibliography}
\end{document}


## Every complete S11 ordinary unverified independent proof and support metadata

Path: checks/S11-nonclosed-ruled-current-statement-only-cold-20261008-complete-result.json
SHA256: aeac7d4e0dca66cbc5171b944f7bfb6487dcdbeaa076afca5da9c6a0dea49dd9

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "A proved throughout the declared parameter range: the ordinary type is admissible exactly when b<c. A shifted Green power supplies an actual strict witness in mutual ordinary type, including when c-b<alpha.",
      "detailedSummary": "Set t=c-b and q_L=L^alpha-(L-G_p)^alpha. Then q_L~U and dd^c q_L>=-alpha L^(alpha-1)w1, with no point atom. Choosing L sufficiently large gives the strict representative bG_p+q_L. Conversely, canonically removing bG_p from any hypothetical competitor gives a positive residual current whose horizontal average is a positive measure of total mass t. Negative t is impossible, and t=0 contradicts the unbounded averaged residual. The residual type is unbounded and nonanalytic. Empty types receive no numeric mass infimum.",
      "text": "This is an unverified mathematical proof of A and the elementary local facts used below. Throughout dd^c=i∂∂bar/(2π), d^c=i(∂bar-∂)/(4π), and dd^c log|z|²=[0]. Put ω=w1+w2, t=c-b, β=t w1+a w2, and λ=w1∧w2. The target is Y=P1×P1, initially with identity resolution and background θ=c w1+a w2. For b=0, bG_p denotes the genuine identically zero function, including on D; no product 0·(-∞) is used. Competitors are the entire ordinary type, without normalization or a model-envelope restriction.\n\nFirst establish the local smooth-background facts. If B+dd^c f>=0 for a smooth real form B, choose locally a smooth strictly psh potential k with dd^c k>=B. Then f+k is psh. On smaller balls its radial convolutions decrease to its canonical representative. For f_ε=(f+k)*ρ_ε-k,\nB+dd^c f_ε=(B+dd^c f)*ρ_ε+B-B*ρ_ε>=-o(1)h.\nConsequently holomorphic pullback preserves the current inequality whenever the pulled-back psh function is not identically -∞. This follows by decreasing psh convergence and distributional convergence. In particular a locally bounded potential restricts canonically to a curve with the pulled-back inequality. For bounded potentials, Bedford–Taylor decreasing continuity gives the products with smooth-background corrections. Adding o(1)h before taking products proves their positivity; the errors vanish because local current masses remain bounded.\n\nA removal fact will be useful. Suppose f is defined off a closed analytic set A, is locally bounded above, and B+dd^c f>=0 there. Choose a local closed positive form K=dd^c k>=B. The psh function f+k extends canonically across A by the permitted removable-singularity theorem. Thus S=K+dd^c f is positive globally. The smooth signed form B-K has no coefficient-measure mass on A. On the complement S+B-K is positive by hypothesis; on A its matrix of coefficient measures is that of S and is positive. Hence B+dd^c f>=0 globally. Canonical quasi-psh functions agreeing almost everywhere agree everywhere: after adding a common smooth potential, their values are recovered by limits of ball averages. The same argument extends inequalities from the complement of an analytic set.\n\nPlace p at z=0 by an FS isometry. Then\nw=dd^c log(1+|z|²), G_p=log(|z|²/(1+|z|²)), T=-G_p>=0.\nFor L>=1 define\nq_L=L^α-(L-G_p)^α=L^α-(L+T)^α, η_L=αL^(α-1).\nConcavity shows q_L-U is bounded; its limit at T=∞ is L^α-1. The function q_L is smooth off p and has canonical value -∞ at p. Off p,\ndd^c q_L=-α(L-G_p)^(α-1)w+α(1-α)(L-G_p)^(α-2)dG_p∧d^cG_p.\nTherefore dd^c q_L>=-η_L w.\n\nThere is no hidden point atom. The boundary flux is O(T^(α-1)), which tends to zero; boundary terms involving a smooth test-function derivative vanish because |z|T^α tends to zero. More explicitly, angular integration gives the pushforward identities\nw=e^(-T)dT,\ndG_p∧d^cG_p=(1-e^(-T))dT.\nFor F_L(T)=α(L+T)^(α-1)(1-e^(-T)), the off-point pushforward of dd^c q_L is -F_L'(T)dT. Both endpoint values of F_L are zero. Its integral is therefore zero, agreeing with distributional Stokes. In particular Cw+dd^c q_L is a positive finite measure of mass C and has no atom whenever C>=η_L. These calculations require no first moment.\n\nIf t>0, choose L large enough that η_L<t. The actual genuine potential\nr0=bG_p+q_L\nis mutually ordinarily equivalent to r=bG_p+U, and Poincaré–Lelong gives\nθ+dd^c r0=b[D]+β+dd^c q_L\n>= (t-η_L)w1+(min a)w2\n>= εω,\nwhere ε=min(t-η_L,min a)>0. This proves sufficiency for every 0<α<1, even when t<α. The background θ itself is strictly positive and thus big in the stipulated nonclosed sense.\n\nConversely, suppose a genuine θ-psh v~r exists. Off D put q=v-bG_p. Mutual comparison gives |q-U|<=M there, and v is locally bounded outside D. Off D,\nβ+dd^c q=θ+dd^c v>=0.\nTake C>max(0,t,max a,α) and K=Cω. Since K>=β, canonical removal extends q across D. Its value there is -∞ because q~U uniformly. The removal fact gives R=β+dd^c q>=0 globally. Both q and G_p are locally integrable, and v=bG_p+q holds distributionally and with the genuine pole values.\n\nLet qbar(x)=∫q(x,y)w(y), interpreted in L1. Off p, |qbar-U|<=M. Fiber integration of R∧w2 gives the positive measure\nσ=t w+dd^c qbar\non the first sphere, whose total mass is t by distributional Stokes. Thus t>=0. If t=0, σ=0 and qbar is a harmonic distribution, hence a smooth harmonic function and constant on the sphere. This contradicts qbar~U and its divergence to -∞ near p. Therefore b<c is necessary. For b>=c the type is empty, and no numeric infimum or supremum is assigned.\n\nFinally q_L is unbounded but has zero transverse logarithmic coefficient: q_L/log|z|² tends to zero. An analytic singularity on a transverse disc is either bounded or has a positive logarithmic coefficient, by factoring the least vanishing order of its holomorphic generators. Neither possibility is ordinarily equivalent to U. Thus the residual ordinary type is unbounded and nonanalytic. The same transverse argument excludes analytic singularities for the full type after its coefficient b is removed.\n\nArtifacts: artifacts/proof_notes.md and artifacts/notes.json retain the proof. Later checks can be rerun with python artifacts/check_s11.py > artifacts/check_output.json; no computational observation is needed for A.\n\nArtifacts: /workspace/research/native-workers/codex-yZnZLs",
      "support": []
    },
    {
      "id": "n2",
      "summary": "B proved over every rough competitor. Closed comparison establishes canonical divisorial removal and full auxiliary closed mass without energy assumptions. Exact optimization gives R_minus=2(c-b)min a and R_plus=2(c-b)max a.",
      "detailedSummary": "For every v~r, write v=bG_p+q canonically. In the closed K=C(w1+w2) class, q and q_L have mutual ordinary order and analytic small unbounded locus D. The permitted BEGZ comparison, checked against its printed primary source, applies in degrees one and two. It proves that S=K+dd^c q has no coefficient-measure mass on D and that its non-pluripolar square has full mass. Smooth corrections yield the actual finite positive nonclosed measure and its integral. Fiber averaging reduces every mass to 2∫aσ, where σ is positive of mass c-b. Actual potentials with increasingly small singular tails concentrate σ at either extremum of a.",
      "text": "This is an unverified proof of B using n1. Assume t=c-b>0. Every competitor is a genuine θ-psh v~r, including arbitrary rough fiber-dependent competitors. Canonical removal gives v=bG_p+q, q~U, q=-∞ exactly on D, local boundedness off D, and R=β+dd^c q>=0.\n\nThe sole non-elementary comparison used is expressly permitted in the assignment. Its exact public primary source was independently opened: Boucksom–Eyssidieux–Guedj–Zeriahi, Monge–Ampère equations in big cohomology classes, Acta Math. 205 (2010), 199–262, DOI 10.1007/s11511-010-0054-7, https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf . Theorem 1.16 and its printed proof occur on pp.217–218, zero-based PDF pages 18–19; Definition 1.2 occurs on p.204. The theorem compares non-pluripolar cohomology classes under ordinary order for cohomologous CLOSED positive currents with small unbounded locus on a compact Kähler manifold. A positive change of dd^c convention is absorbed by inverse rescaling of potentials, leaving the actual currents and their products unchanged. No source comparison for nonclosed currents is invoked.\n\nChoose L with η_L<t and C>max(t,max a,η_L). Set K=Cω, S=K+dd^c q, S0=K+dd^c q_L. These are globally closed positive currents on the compact Kähler surface Y, cohomologous to K, with mutual ordinary order. Their small unbounded locus is the closed analytic divisor D, locally the complete pluripolar set {log|z|²=-∞}. They are locally bounded outside D. All comparison hypotheses are thereby verified.\n\nFor the separated reference, bounded locality away from D and the curve computation in n1 give the actual product\n⟨S0²⟩=2C(Cw1+dd^c q_L)∧w2.\nIts mass is 2C²=∫K². Its order-one current has no mass on D because the first-factor measure has no atom.\n\nApply the permitted comparison in degree one to S and S0 in both orders, then pair with K. This gives\n∫⟨S⟩∧K=∫S0∧K=∫K².\nOrder-one locality gives ⟨S⟩=1_(Y\\D)S. Since ∫S∧K=∫K² by distributional Stokes, the positive defect 1_D S has zero pairing with the strictly positive form K and must vanish. Thus S has no coefficient-measure mass on D. This establishes the needed divisorial-removal assertion without invoking a Siu decomposition or imposing an energy condition.\n\nApply the same comparison in degree two, with both entries equal to S and both reference entries equal to S0, again in both orders. It yields\n∫⟨S²⟩=2C².\nThese comparisons involve only closed currents, never R or θ+dd^c v.\n\nPut B=β-K. On Y\\D, bounded products with smooth corrections give\nMA_ext,β(q)=⟨S²⟩+2S∧B+B².                 (1)\nThe right side is a finite signed measure globally: its first term has mass 2C², S has finite coefficient masses, and B is smooth. Every term puts no mass on D. Off D it is positive by the local approximation in n1. Consequently it is a positive global measure, and locality identifies it with the actual extended non-pluripolar product. This also proves existence, finiteness, and independence of C. On Y\\D the currents θ+dd^c v and β+dd^c q coincide; their non-pluripolar products both vanish on D. Their extended measures are therefore equal.\n\nIntegrating (1), using the full closed mass and distributional Stokes, gives\nM(v)=∫β²+2∫dd^c q∧(β-K)\n=2t∫a w+2∫q dd^c a∧w2.                  (2)\nOnly the L1 function q is integrated against smooth forms. No first moment against S or its Monge–Ampère measure appears.\n\nWith qbar and σ=t w+dd^c qbar from n1, formula (2) becomes\nM(v)=2∫a σ.                              (3)\nThe measure σ is positive, has total mass t, and has no atom at p by the no-D-mass conclusion. Hence every mass is positive and finite, and\n2t min a<=M(v)<=2t max a.                  (4)\nThis applies to all rough competitors through their actual fiber averages.\n\nThe requested original-background formula follows from dd^c θ=dd^c a∧w2 and\n∫G_p dd^c θ=a(p)-∫a w.\nSubstituting v=bG_p+q into (2) yields\nM(v)=∫θ²-2b a(p)+2∫v dd^c θ.\nIts last integral is finite by local integrability of v and smoothness of the coefficient density. It generally depends on v; no nonclosed intersection invariance is asserted.\n\nTo prove exactness of the extrema, choose any first-factor point x0 and smooth strictly positive probability forms ξ_j converging weakly to δ_x0. Choose L_j tending to infinity with η_j=αL_j^(α-1)<t and η_j tending to zero. Define the smooth global Green potential\nh_j(x)=(t-η_j)∫G_z(x)ξ_j(z).\nThe locally integrable logarithmic kernel and its smooth right-hand side give smoothness, and Poincaré–Lelong gives dd^c h_j=(t-η_j)(ξ_j-w). Set q_j=q_(L_j)+h_j and v_j=bG_p+q_j. Each q_j~U and\n t w+dd^c q_j=(t-η_j)ξ_j+(η_j w+dd^c q_(L_j))>=0.\nThe second positive summand has mass η_j and tends weakly to zero. Thus the horizontal measures converge to tδ_x0. The potentials v_j are actual θ-psh competitors in the exact ordinary type: their residual currents have the displayed nonnegative horizontal part and the positive vertical part a w2. By (3), their masses tend to 2t a(x0). Selecting minimizing and maximizing points proves\nR_minus=2(c-b)min a,\nR_plus=2(c-b)max a.\nThe ordinary-equivalence constants may depend on j; uniform constants are not part of optimization over an entire fixed type.\n\nArtifacts: sources/verification.md records the public-source audit and the failed direct PDF download. artifacts/proof_notes.md and artifacts/notes.json retain the proof. Neither finite energy nor a finite first moment is a hypothesis.\n\nArtifacts: /workspace/research/native-workers/codex-yZnZLs",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "C proved for the actual product embedding. The exact ambient ideals are O(-floor(sb)(D×P1)), including integer boundary weights, and every intrinsic trace is b ord_E(pi*D).",
      "detailedSummary": "Use r0=bG_p+q_L from n1 and the smooth target Y0=Y×{z0} in Z=Y×P1. The ambient potential is genuinely admissible and has generic Lelong number zero along Y0. A transverse germ of order k is integrable precisely when k+1>sb; equality fails because of the positive sublinear exponential. Restricting the resulting ambient coherent ideal and pulling back that invertible ideal gives the exact traces on every modification. The residual has trivial ideals at all real weights despite its unbounded nonanalytic ordinary type.",
      "text": "This is an unverified proof of C using n1. Assume b<c and select L with η_L<c-b. Put r0=bG_p+q_L,\nZ=Y×P1, Y0=Y×{z0}, Θ=pr_Y^*θ+w3, u_Z=pr_Y^*r0.\nThe background is smooth and strictly positive, and\nΘ+dd^c u_Z=pr_Y^*(θ+dd^c r0)+w3>=0.\nThus this is an actual admissible ambient representative. If a is nonconstant, dΘ=pr_Y^*(da∧w2) is nonzero. The initial target resolution is the identity, with Θ|Y0=θ and u_Z|Y0=r0. At a generic point of Y0 the potential is smooth, so its generic Lelong number along Y0 is zero. Smooth positive volume densities are locally comparable, and their choice does not change integrability ideals.\n\nNear D take a transverse coordinate z and T0=-log|z|². Since G_p=log|z|²+O(1), and bounded changes of the argument of x^α change it by a bounded amount for α<1,\nu_Z=b log|z|²-T0^α+O(1).\nFor a nonzero holomorphic germ with transverse vanishing order k, write f=z^k F. The function F is bounded above on a smaller polydisc and bounded below on some open set of the remaining variables near z=0. Fubini therefore gives the exact integrability criterion from\n∫_0^ε r^(2k-2sb+1)exp(s(-log r²)^α)dr\n=(1/2)∫_(Tε)^∞ exp(-(k+1-sb)T+sT^α)dT.\nBecause T^α=o(T), this is finite exactly when k+1>sb. At equality the integrand is exp(sT^α) and diverges. Hence the least allowed nonnegative integer k is floor(sb). In particular, at sb=N an integer, order N-1 fails at the exact boundary and order N succeeds. This proves the normalization directly with |f|²exp(-su), without an additional factor 2.\n\nAway from D×P1 the potential is locally bounded. The local calculations glue to\nI(su_Z)=O_Z(-floor(sb)(D×P1))\nfor every real s>0. Boundedly equivalent representatives have the same ideals because their exponential factors are comparable above and below.\n\nNow restrict this actual ambient coherent ideal. Its local divisor equation remains the equation of D on Y0, so\nI(su_Z)O_Y0=O_Y0(-floor(sb)D).\nFor every smooth compact modification π:Y'→Y0 and every prime divisor E on Y', the invertible restricted ideal has order\nfloor(sb)ord_E(π^*D).\nThe divisor multiplicity is a finite nonnegative integer. Dividing by s and taking the prescribed limit gives\nτ_(Y0,u_Z)(E)=b ord_E(π^*D).\nThis includes all prime divisors on all smooth compact modifications and does not require a normal-crossings total transform. Total transforms and their orders are compatible with composition. No equality is inferred from trace-envelope lower inequalities, and the restriction of the ambient ideal has not been replaced by a multiplier ideal of a pulled-back potential.\n\nWith b=0, the same integral is finite for k=0 at every real s>0. Therefore I(sq_L)=O_Y at every weight, and likewise on the ambient product. Nevertheless q_L is unbounded and its ordinary type is nonanalytic by n1. Ideal equality does not give ordinary equivalence and does not record α.\n\nArtifacts: artifacts/proof_notes.md and artifacts/notes.json contain the argument. The integer-boundary assertion is an analytic proof, not a numerical observation.\n\nArtifacts: /workspace/research/native-workers/codex-yZnZLs",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n4",
      "summary": "D proved for an actual admissible shifted residual and a closed dominating K. The separated product has full mass; its first moment is finite exactly for alpha<1/2, with logarithmic divergence at alpha=1/2.",
      "detailedSummary": "The explicit angular density of Cw+dd^c q_L is (C-alpha(L+T)^(alpha-1))e^(-T)+alpha(1-alpha)(L+T)^(alpha-2)(1-e^(-T)). It has mass C and no atom, giving actual closed top mass 2C². Multiplication by -q_L produces a positive tail asymptotic to 2C alpha(1-alpha)T^(2alpha-2). This proves the finiteness threshold and divergence rates. A–C impose no finite-energy or first-moment condition.",
      "text": "This is an unverified proof of D. Assume b<c, choose L with η_L<c-b, and take the actual β-psh residual q0=q_L~U. Choose C>max(c-b,max a,η_L) and K=C(w1+w2). The form K is closed and dominates β; it is an auxiliary Kähler form, not a replacement of the nonclosed target background.\n\nBy the separated curve computation of n1, the actual product is\nMA_K(q0)=⟨(K+dd^c q0)²⟩=2C(Cw1+dd^c q_L)∧w2.\nIt has mass 2C²=∫K², so it has full closed mass.\n\nUnder T=-G_p, the angular pushforward of the positive first-factor measure has density\nA(T)=(C-α(L+T)^(α-1))e^(-T)\n+α(1-α)(L+T)^(α-2)(1-e^(-T)).\nIts mass is C and it has no atom. Since -q0=(L+T)^α-L^α, the actual extended nonnegative first moment is\n∫Y(-q0)MA_K(q0)\n=2C∫_0^∞[(L+T)^α-L^α]A(T)dT.\nIt is finite on bounded intervals. Its exponentially decaying part is integrable for every 0<α<1. The remaining positive tail is asymptotic, with ratio tending to one, to\n2Cα(1-α)T^(2α-2)dT.\nComparison with power integrals proves finiteness exactly when α<1/2. At α=1/2 the truncation at T=R diverges as (C/2)log R. For α>1/2 it diverges as\n[2Cα(1-α)/(2α-1)]R^(2α-1).\nThe logarithm refers to the T cutoff; for a radius cutoff this is a double logarithm.\n\nTogether with n1–n3, this establishes that all their admissibility, mass, and ideal conclusions hold throughout 0<α<1, including these actual infinite-moment examples. The closed full-mass comparison in n2 did not assume a finite moment.\n\nObservational evidence is reproducible with python artifacts/check_s11.py > artifacts/check_output.json. For C=4,L=16, truncated moments at R=100,10^4,10^6 were approximately (1.034980,1.174376,1.197483) for α=1/4; (5.214753,12.805760,21.869063) for α=1/2; and (21.669737,279.770695,2976.274596) for α=3/4. These observations illustrate, but do not prove, the analytic tail laws. No resource-heavy computation was needed.\n\nArtifacts: /workspace/research/native-workers/codex-yZnZLs",
      "support": [
        "n1",
        "n2",
        "n3"
      ]
    },
    {
      "id": "n5",
      "summary": "E proved: smooth gauges and pure modifications preserve competitors, actual non-pluripolar pushforward, optimized masses and intrinsic trace transport. A point blowup outside D has an explicit one-sided strict witness and no mutual-type strict witness.",
      "detailedSummary": "Canonical descent across the analytic exceptional image gives an inverse to pullback for the entire competitor family. Locality on the biholomorphic complements and zero non-pluripolar mass on analytic sets prove the actual pushforward law, upstairs finiteness, and equality of both optimized masses. Trace transport uses total transforms of the original restricted ambient ideals. On a point blowup outside D, adding a small cutoff logarithmic pole to the pullback of r0 yields a smooth positive residual form plus an exceptional divisor. A mutual-type witness would be bounded near the exceptional curve, whose canonical restriction contradicts Stokes because the pure background restricts to zero.",
      "text": "This is an unverified proof of E using n1–n3. Assume b<c. On a smooth modification π:Y'→Y, the declared target is Y' with PURE background π^*θ and ordinary type [π^*r]. Pullback means the actual canonical holomorphic pullback, including pole values.\n\nFor a real smooth f, set θ'=θ+dd^c f, r'=r-f, v'=v-f. This is a bijection of competitor families preserving ordinary comparisons, and θ'+dd^c v'=θ+dd^c v. Bounded products and their non-pluripolar extensions give the same actual extended measures, hence identical infima and suprema. The factor exp(sf) is locally bounded above and below by positive constants, so all real-weight ideals, their ambient restrictions, and intrinsic traces are unchanged. On the product ambient space use the gauge pr_Y^*f. Big positivity is preserved by the current equality.\n\nFor pure modifications, choose proper closed analytic sets A⊂Y and A'⊂Y' such that π is biholomorphic between their complements. These may include all exceptional sets. Pullback preserves smooth-background current positivity by the local approximation in n1 and preserves the two ordinary inequalities.\n\nConversely, let v' be any genuine π^*θ-psh potential with v'~π^*r. Descend it on Y\\A using the biholomorphism. Its ordinary bounds against r make it locally bounded above near A. Add a local smooth potential of a closed positive form dominating θ, and extend the resulting psh function canonically across A. The extensions agree on overlaps by almost-everywhere equality and canonicity. The removal argument of n1 proves θ+dd^c v>=0 globally. Both ordinary inequalities extend using ball averages after adding a common smooth potential to v and r. Thus v~r with the genuine values at poles. Its canonical pullback agrees almost everywhere with v', hence everywhere. Pullback and descent are inverse bijections, even before quotienting by constants. No factorization of the modification or Kähler assumption on Y' was used.\n\nOn the biholomorphic complements, bounded products with smooth corrections commute with coordinate changes, and non-pluripolar locality passes this to the actual measures. These products put no mass on proper analytic sets: off the poles this follows from bounded Bedford–Taylor products, and at the poles from the non-pluripolar construction. Smooth corrections have the same property. Therefore the upstairs measure has no mass on A', and its mass on the complement equals the downstairs mass on Y\\A. The latter is finite by n2, which also proves global finiteness upstairs. Consequently the actual Borel-measure identity is\nπ_*MA_ext,π^*θ(π^*v)=MA_ext,θ(v).\nThe competitor bijection now gives\nR_minus(π^*θ,[π^*r])=2(c-b)min a,\nR_plus(π^*θ,[π^*r])=2(c-b)max a.\n\nFor trace transport, the original restricted ambient ideals of n3 are O_Y(-floor(sb)D). Their total transforms on Y' are O_Y'(-floor(sb)π^*D). Thus for every further modification ρ:Y''→Y' and prime F,\nτ(F)=b ord_F(ρ^*π^*D).\nThis is the same intrinsic system indexed by divisors over Y. It does not assert I(sπ^*r0)=π^*I(sr0), nor replace the original ambient restricted ideals by new pulled-back multiplier ideals. Exceptional curvature subtraction is a different background operation, across which no equality is asserted. No invariance of V_μ for arbitrary upstairs densities is claimed.\n\nNow declare π:Bl_yY→Y to be the point blowup at y∈Y\\D, with exceptional curve E. Its lower optimized mass is positive by the preceding calculation. An actual one-sided strict witness can be constructed as follows.\n\nTake r0 from n1 with θ+dd^c r0>=εω. Choose a coordinate ball about y whose closure misses D and a smooth radial cutoff χ equal to one on a smaller ball and zero outside a larger one. Define\nh=χ log(|z1|²+|z2|²), h(y)=-∞,\nextended by zero outside the chart. It is a genuine global quasi-psh function, bounded above. Its negative curvature is confined to the cutoff annulus and bounded below by -Mω. In the inner ball its logarithm is psh.\n\nLet H=π^*h. In the blowup chart z1=s,z2=sξ near E,\nH=log|s|²+log(1+|ξ|²),\ndd^c H=[E]+η,\nη=dd^c log(1+|ξ|²).\nGlobally η=dd^c H-[E] is a smooth closed form. On E it is the positive FS form. At E, π^*ω is positive in the normal direction and zero in the tangent direction. Therefore ε π^*ω+δη is strictly positive at E for every δ>0. In the inner ball away from E it is positive because the logarithmic curvature is nonnegative and π^*ω is positive. On the cutoff annulus η>=-Mπ^*ω, so 0<δ with δM<ε ensures positivity there. Outside the chart it equals ε π^*ω. Hence\nA_δ=ε π^*ω+δη\nis an actual smooth strictly positive form on the blowup. The genuine potential\nw=π^*r0+δH\nsatisfies\nπ^*θ+dd^c w>=A_δ+δ[E]>=A_δ.\nSince H is bounded above and r0~r, w<=π^*r+C. Its added exceptional pole prevents claiming mutual comparison, and it is not asserted to have the original exact ideal trace at E.\n\nSuppose instead that a genuine strict witness v'~π^*r existed, with π^*θ+dd^c v'>=ε' h' for ε'>0 and a smooth Hermitian h'. Because r is smooth near y, mutual comparison makes v' bounded near E. Its canonical restriction to E is finite and bounded. The restriction argument of n1 gives\ndd^c(v'|E)>=ε' h'|E,\nsince π^*θ|E=0. Distributional Stokes gives zero total integral on the left and a positive one on the right, a contradiction. Thus every mutual-type strict witness is excluded.\n\nArtifacts: artifacts/proof_notes.md and artifacts/notes.json retain the proof and cutoff construction. No mutual strict-type preservation on arbitrary modifications is asserted.\n\nArtifacts: /workspace/research/native-workers/codex-yZnZLs",
      "support": [
        "n1",
        "n2",
        "n3"
      ]
    },
    {
      "id": "n6",
      "summary": "F proved for the explicitly declared all-test normalization: V_mu(beta)=2(c-b)/H with actual attainment. The derivative and integrated subtraction identity use the actual minimizer and are separate from R_plus.",
      "detailedSummary": "Define D_mu(T)=∫sqrt(T²/mu)mu and V_mu(B)=inf(∫B∧T/D_mu(T))² over all smooth positive dd^c-closed tests. Fiber integration makes the averaged vertical coefficient a positive constant k. With A=∫a x, determinant positivity and Cauchy–Schwarz give D²<=2AkH, while the numerator is tk+A. The identity (tk+A)²-4tkA=(A-tk)² proves the all-test bound. The specified positive closed test attains every equality. Differentiating the exact formula proves the claimed subtraction pairing and its integrated identity on any compact positive segment, for constant d and smooth first-factor e.",
      "text": "This is an unverified proof of F. Since V_μ and D_μ were not otherwise defined in the input, declare their all-test normalization explicitly:\nD_μ(T)=∫Y sqrt(T²/μ)μ,\nV_μ(B)=inf_(T smooth real (1,1), T>0, dd^c T=0)(∫Y B∧T/D_μ(T))².\nHere T²/μ is the positive density ratio, with no inserted factorial. These are the functional and normalization for which F's formulas are proved. No PDE normalization or separated-test restriction is assumed.\n\nPut t=c-b>0, μ=mλ, ∫m w=1, H=∫(m/a)w. Take any allowed test T. In local product-unitary frames write its Hermitian matrix as [[x,z],[conjugate(z),y]], so x,y>0 and\nT²=2(xy-|z|²)λ.\nThe coefficients x,y and |z|² are globally well-defined. The smooth function k(x1)=∫y(x1,x2)w(x2) is the fiber integral of T. Differentiation under the integral and Stokes give dd^c k=0 from dd^c T=0. Thus k is a positive constant. This applies to arbitrary mixed and fiber-dependent tests.\n\nSet A=∫a x λ>0. The numerator is N=tk+A. Determinant positivity and Cauchy–Schwarz give\nD_μ(T)=∫sqrt(2m(xy-|z|²))λ\n<=sqrt(2)∫sqrt(a x)sqrt(m y/a)λ,\nD_μ(T)²<=2A∫(m y/a)λ=2AkH.\nConsequently\nN²/D_μ(T)²>=(tk+A)²/(2AkH)>=2t/H,\nwhere the last inequality is (A-tk)²>=0. This proves the lower bound for every allowed test.\n\nLet V=2t/H and define\ng=Vm/(2a), T0=(g/a)w1+w2=(Vm/(2a²))w1+w2.\nThis test is smooth and strictly positive. It is actually closed because its first coefficient depends only on the first factor. It has k=1, z=0 and A=(V/2)H=t. Also\nT0²/μ=V/a²,\nD_μ(T0)=sqrt(V)H,\n∫β∧T0=2t.\nIt attains the bound. Therefore V_μ(β)=2(c-b)/H. The identical argument with t replaced by c gives V_μ(θ)=2c/H.\n\nFor nonconstant a, replacing m=1 by m_ε=1+ε(1/a-∫(1/a)w), for sufficiently small nonzero ε, preserves positivity and normalization while changing H by ε times the positive variance of 1/a. Hence V_μ can depend on μ. The optimized masses in n2 do not. For strictly positive m and nonconstant a,\n1/max a<H<1/min a,\nso R_minus<V_μ(β)<R_plus. For constant a these residual values coincide.\n\nFix b,m, a real constant d, and a fixed smooth real first-factor function e. On any compact segment where t_s=c-sd-b>0 and a_s=a-se>0 everywhere, put\nH_s=∫m/a_s w, V_s=2t_s/H_s,\nT_s=(V_s m/(2a_s²))w1+w2.\nThis is the actual attaining test at every s. Differentiation is justified by uniform positivity on the compact segment. With J_s=∫m e/a_s² w,\nH_s'=J_s, t_s'=-d,\n(d/ds)sqrt(V_s)=-[d+(V_s/2)J_s]/[sqrt(V_s)H_s].\nBut\n∫(d w1+e w2)∧T_s=d+(V_s/2)J_s,\nD_μ(T_s)=sqrt(V_s)H_s.\nThus the claimed identity holds with the actual minimizer:\n(d/ds)sqrt(V_μ(β_s))=-∫(d w1+e w2)∧T_s/D_μ(T_s).\nIntegrating from s0 to s1 gives\nsqrt(V_μ(β_s0))-sqrt(V_μ(β_s1))\n=∫_(s0)^(s1)[∫(d w1+e w2)∧T_s/D_μ(T_s)]ds.\nIt is a signed subtraction identity for the allowed signed d,e; it is nonnegative for pointwise nonnegative subtraction. It is not a derivative of R_plus and makes no assertion about arbitrary positive upstairs densities.\n\nRerun python artifacts/check_s11.py > artifacts/check_output.json for the symbolic derivative and algebraic square certificate. For t_s=0.75-0.1s, a_s=2+τ-s(0.2+0.05τ), m=1, 0<=s<=1, both numerical sides of the subtraction identity were 0.20207339476407357738172422814152303. The segment has t_s>=0.65 and a_s>=0.85. Numerical agreement is observational evidence, not the proof of the all-test inequality.\n\nArtifacts: /workspace/research/native-workers/codex-yZnZLs",
      "support": [
        "n2"
      ]
    },
    {
      "id": "n7",
      "summary": "Complete unverified restricted A–G result with an actual genuinely nonclosed example: r0=G_p/4+8-(16-G_p)^(3/4), R_minus=3/2, R_plus=9/2, V_beta=3/log3, V_theta=4/log3 and all traces (1/4)ord_E(pi*D). Unrestricted S11 remains open.",
      "detailedSummary": "The specified representative is strict in mutual ordinary type with epsilon=3/8. The height distribution gives H=(log3)/2 and the exact claimed numerical values. Its residual has an infinite first moment for the auxiliary closed K=4(w1+w2), although all target-background optimized masses remain finite. Pure point blowup preserves both optimized masses, admits the explicit one-sided cutoff-log strict witness, and excludes mutual ordinary strictness. Notes n1–n6 prove every restricted target throughout its declared domain, including all rough competitors and all Gauduchon tests. No criterion for arbitrary nonclosed restricted masses or solution of unrestricted S11 is claimed.",
      "text": "This final note claims a complete unverified solution of the restricted A–G assignment, with the all-test normalization explicitly declared in n6. It does not claim a solution of unrestricted original S11.\n\nDeclare c=1, b=1/4, α=3/4, a=2+τ, m=1 on Y=P1×P1, where the spherical height τ has distribution dτ/2 on [-1,1]. Take D={p}×P1, θ=w1+(2+τ)w2, β=(3/4)w1+(2+τ)w2, and μ=w1∧w2. The genuine ambient embedding is Y0=Y×{z0} in Z=Y×P1, with Θ=pr_Y^*θ+w3. Use the identity resolution initially and pure backgrounds on modifications. Since dτ∧w2 is not identically zero, θ, β and Θ are genuinely nonclosed, as are their pure pullbacks on the dense biholomorphic locus. None is identified with line-bundle curvature.\n\nThe actual potentials\nq16=8-(16-G_p)^(3/4),\nr0=(1/4)G_p+8-(16-G_p)^(3/4)\nhave η16=(3/4)16^(-1/4)=3/8. By n1,\nθ+dd^c r0>=(3/8)w1+(2+τ)w2>=(3/8)(w1+w2).\nTheir genuine pole values on D are -∞, and r0 is mutually ordinarily equivalent to the specified r. This is an actual strict-current witness.\n\nSince min a=1 and max a=3, n2 gives the exact entire-type optimized masses\nR_minus=2(3/4)·1=3/2,\nR_plus=2(3/4)·3=9/2.\nThese are not identified with the mass of the single displayed representative. All rough competitors have positive finite masses, and actual same-type sequences approach both bounds.\n\nThe declared height distribution gives\nH=(1/2)∫_(-1)^1(2+τ)^(-1)dτ=(log3)/2.\nTherefore the attained all-test values of n6 are\nV_μ(β)=3/log3,\nV_μ(θ)=4/log3.\nFor u_Z=pr_Y^*r0, the exact ambient-ideal calculation of n3 gives\nτ_(Y0,u_Z)(E)=(1/4)ord_E(π^*D)\non every prime divisor on every smooth compact modification π of Y0.\n\nChoose the auxiliary CLOSED form K=4(w1+w2), which dominates β. By n4 the actual separated closed product of q16 has full mass 32 but\n∫(-q16)MA_K(q16)=∞.\nIts tail is asymptotic to (3/2)T^(-1/2)dT, so the truncation grows as 3sqrt(R). This auxiliary K is expressly separate from the genuinely nonclosed target backgrounds.\n\nFor any declared point blowup π:Bl_yY→Y with y outside D, n5 preserves both optimized masses, 3/2 and 9/2. It gives the actual one-sided strict potential\nw=π^*r0+δπ^*(χ log(|z1|²+|z2|²)),\nwith a chart missing D and sufficiently small positive δ. Its current dominates the explicit smooth positive form constructed in the blowup charts, and w<=π^*r+C. No mutually equivalent strict potential exists, by canonical restriction to the exceptional curve and Stokes. The new witness's added exceptional singularity is not asserted to have the original exact trace on that divisor.\n\nThe restricted invariant is the pair of existing whole-ordinary-type optimized masses of this actual target restriction. Here it is finite, gauge invariant, pure-modification invariant and positive precisely in the admissible unbounded family b<c. Its proved relation to the intrinsic data is τ(D)=b and the formulas 2(c-τ(D))min a and 2(c-τ(D))max a. It is not a complete trace invariant: fixing b and the background while varying α gives mutually inequivalent unbounded residual ordinary types with identical all-weight residual ideals, intrinsic traces and optimized mass pairs. No trace-envelope exactness or universal ambient/restricted mass equality has been assumed.\n\nCoverage is complete within the restricted assignment: n1 proves A for every b>=0 and 0<α<1, including c-b<α and empty-type exclusion; n2 proves B over all rough competitors; n3 proves C from actual ambient ideal restrictions on every modification; n4 proves D without an energy hypothesis; n5 proves the gauges, pure-pullback laws and both distinct blowup strictness conclusions; n6 proves the all-test lower bound, attainment and actual subtraction formula; this note proves G and assembles the result.\n\nReproducibility: the unchanged input is input.json. The full proof artifacts are artifacts/proof_notes.md and artifacts/notes.json; the exact public-source audit is sources/verification.md. Run python artifacts/check_s11.py > artifacts/check_output.json. The checks used Python 3.12.14, SymPy 1.14.0 and mpmath 1.3.0 on Linux x86_64. All script assertions passed. They verified the symbolic derivative and algebraic square identity, computed H=0.54930614433405484569762261846126285, V_beta≈2.73071767988051218 and V_theta≈3.64095690650734957, checked truncated curve masses against exact boundary-flux corrections, and reported the moment and subtraction observations in n4 and n6. artifacts/deliverable_audit.json records an acyclic support graph and input SHA-256 a1ed701818e86136072573a753f624c09a43dff76c5a6ab347a09ec5eed3f89c. These computations are observations and algebra checks, not exhaustive enumerations or mathematical certification. No resource-heavy computation was launched.\n\nUnrestricted S11 remains open for arbitrary nonclosed backgrounds, singular targets and general intrinsic trace systems. This family does not establish a general strict-current criterion from positive nonclosed restricted mass. No priority claim is made for the known definitions, divisorial principles or pure-pullback laws.\n\nArtifacts: /workspace/research/native-workers/codex-yZnZLs",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "n6"
      ]
    }
  ],
  "candidate": true,
  "workspace": "/workspace/research/native-workers/codex-yZnZLs"
}


## Entire S11 restricted final public review, never a proof premise

Path: checks/S11-nonclosed-ruled-A-G-limited-final-comparison-20261008-complete-result.json
SHA256: 321b22161b7c61e30530597f8759ce192e054c93fb84efc84317147a67464d15

{
  "verdict": "PASS",
  "report": "PASS applies solely to the complete restricted A–G theorem. I independently checked the current article, the historical restricted proof and first-moment-free supplement, and every reconstruction note n1–n7. No restricted proof depends on the excluded general L¹ coefficient theorem, unspecified E_env definitions, historical verdicts, candidate flags, or computational artifacts. The historical full-companion INCONCLUSIVE remains unchanged, and unrestricted S11 remains open.\n\nA. Both residual constructions work. The article’s piecewise χ_L is increasing, convex and C¹ at its joining point; its unchanged singular tail differs from U by a finite constant. It satisfies dd^c U_L≥−ε_Lw, where ε_L→0, and U≤U_L≤0 with L¹ convergence to zero. The reconstruction’s q_L=L^α−(L−G_p)^α has the same ordinary type and curvature bound −αL^(α−1)w. The transverse boundary flux tends to zero, so these residuals have no point atom. Choosing the curvature loss below c−b supplies the displayed mutual-type strict witness even when c−b<α.\n\nCanonical divisorial removal is valid for every rough competitor. Off D, subtracting bG_p leaves q~U. After adding a local quadratic, the bounded-above psh function extends canonically. The sharper nonclosed inequality survives: the extended positive Hessian has positive coefficient measures on D, whereas the smooth correction assigns D zero measure. Thus θ+dd^c v=b[D]+β+dd^c q, with β=(c−b)w1+aw2. Canonical equality follows from almost-everywhere equality; no subtraction of infinite pole values is used. Fiber averaging gives a positive curve measure (c−b)w+dd^c q̄ of total mass c−b. Negative mass excludes b>c; zero mass forces q̄ constant and contradicts q̄~U, excluding b=c. Empty types receive no numerical volume. The sublogarithmic residual is unbounded and cannot have an analytic ordinary type.\n\nB. The calculation covers every rough fiber-dependent competitor. Set k=c−b>0 and choose the admissible reference U_L₀ with ε_L₀<k/2. For a closed K=C(w1+w2) dominating β, S=K+dd^c q and S₀=K+dd^c U_L₀ are closed positive cohomologous currents on the compact Kähler surface Y. Their potentials have bounded difference and are locally bounded outside the closed locally complete pluripolar divisor D. Consequently every hypothesis of the permitted comparison is established in degrees one and two and in both ordinary orders. It is never applied to a nonclosed current.\n\nThe separated reference has ⟨S₀²⟩=2C(Cw1+dd^c U_L₀)∧w2 and mass 2C². Degree-one comparison gives the full K-trace of ⟨S⟩. Since S−⟨S⟩=1_D S is positive and has zero strictly positive K-trace, it vanishes. Degree-two comparison gives ∫⟨S²⟩=∫K². With B=β−K, the actual extended measure is ⟨S²⟩+2B∧S+B². Each term is finite and has zero mass on D; bounded locality identifies the expression off D, hence globally. Distributional Stokes yields M(v)=∫β²+2∫q dd^cβ=2∫aσ, where σ=kw+dd^c q̄ is positive of mass k. This proves positive finite masses and both global bounds. It uses only L¹ pairing with smooth forms, not a nonlinear first moment.\n\nBoth extremizing constructions are actual same-type potentials. In the article, smooth positive ζ_j of mass k are paired with sufficiently small-curvature U_L_j. In n2, σ_j=(k−η_j)ξ_j+(η_jw+dd^c q_L_j), where the second positive summand has mass η_j→0. Thus σ_j→kδ_x and M(v_j)→2ka(x), including when x=p. Taking x at the extrema proves R_−=2k min a and R_+=2k max a. Finally ∫G_p dd^c a=a(p)−∫aw gives exactly the asserted original-background affine formula. The historical supplement’s raw-U range c≥α is respected; its application when k<α uses the admissible U_L₀ reference, whose hypotheses were checked separately.\n\nC. The chosen r₀ is genuinely admissible, so its product pullback gives the claimed Θ-psh ambient potential. Θ is strictly positive, and dΘ≠0 when a is nonconstant. The generic Lelong number along Y₀ is zero because the reference is locally bounded on its generic locus. Near D_Z, u_Z=b log|z|²−T^α+O(1), with T=−log|z|². A germ of transverse order j has radial integral comparable to ∫exp(−(j+1−sb)T+sT^α)dT. It converges precisely when j+1>sb. At equality it diverges, so the coefficient is floor(sb), including every integer boundary weight with the stipulated no-extra-factor-2 convention. Factoring a general germ and using a nonzero leading tangential coefficient establishes both necessity and sufficiency.\n\nRestricting these actual ambient principal ideals gives O_Y₀(−floor(sb)D). Their orders on every smooth compact modification are floor(sb)ord_E(π*D); the defining limit therefore equals b ord_E(π*D). This establishes the entire intrinsic trace system through ambient ideal restrictions. It does not assert multiplier-ideal pullback commutation. The residual has trivial ideals at all real weights while remaining unbounded.\n\nD. For q_L, angular integration with T=−G_p gives w=e^(−T)dT and dG_p∧d^cG_p=(1−e^(−T))dT. The positive curve measure Cw+dd^c q_L has density (C−α(L+T)^(α−1))e^(−T)+α(1−α)(L+T)^(α−2)(1−e^(−T)), mass C and no atom. Thus its actual separated closed square has full mass 2C². Multiplication by −q_L gives the positive first-moment tail 2Cα(1−α)T^(2α−2)dT. Finiteness is exactly α<1/2; at α=1/2 the divergence is (C/2)log R for a T-cutoff R. The article’s shifted tail has the same threshold. No energy or first-moment hypothesis enters A–C.\n\nE. Smooth gauges preserve actual currents, finite-level products and their extensions, competitor classes, and all real-weight ideals. For a pure modification, adding a pulled-back local quadratic makes the upstairs potential psh. Descent on the biholomorphic complement has a local upper bound by properness; canonical removal and the coefficient-measure argument retain the exact downstairs smooth-background inequality. Ordinary comparisons extend canonically. Pullback and descent are inverse, including pole values. For modifications, the sharper pullback inequality follows by the same extension argument; n1 also supplies a valid decreasing local approximation proof. Locality on the biholomorphic complements and zero mass on analytic sets prove the actual pushforward law, upstairs finiteness, and equality of both optimized masses. Intrinsic trace transport means total transforms of the original restricted ambient ideals, followed by composition of modifications.\n\nBoth point-blowup witnesses are valid. The author’s negative exceptional curvature has the required vertical sign; the displayed Schur-complement estimate proves positivity after choosing the neighborhood and then the parameter small. In n5, the cutoff logarithm pulls back near E to log|s|²+log(1+|ξ|²), so its Hessian is [E]+η with η smooth and positive tangentially on E. The form επ*ω+δη is strictly positive near E, remains positive in the inner punctured region, and is positive on the cutoff annulus for δM<ε. The resulting genuine witness is at most π*r plus a constant and acquires an exceptional pole.\n\nConversely, mutual ordinary equivalence forces boundedness near E. A hypothetical strict witness can be restricted genuinely to E: subtract local quadratics whose constant Hessians lie below the smooth lower bound, with positive tangent coefficient. The restricted curve Hessian is then strictly positive, contradicting its zero integral by Stokes. Thus positive preserved lower mass supplies no mutual strict witness on this blowup. Exceptional curvature subtraction and invariance for arbitrary upstairs Gauduchon densities are not asserted.\n\nF. Both independent all-test proofs are sound with D_μ(T)=∫sqrt(T²/μ)μ and V_μ equal to the square of the infimum quotient. In the article, Poisson solvability gives Ω=gw1+aw2=β+dd^c f with Ω²=Vμ. Stokes and matrix arithmetic–geometric mean prove the lower bound for every positive dd^c-closed test. The closed positive T=Ω/a attains it. In n6, fiber integration of an arbitrary mixed test gives a positive constant vertical average κ; determinant positivity and Cauchy–Schwarz give D²≤2AκH, while the numerator is kκ+A. The identity (A−kκ)²≥0 proves the same unrestricted bound. Both give V_μ(β)=2k/H, separately from V_μ(θ)=2c/H. The dependence on m and distinction from R_+ follow directly.\n\nFor fixed real d and smooth first-factor e, H_s′=∫em/a_s² and D_μ(T_s)=sqrt(V_s)H_s. Direct differentiation gives (sqrt(V_s))′=−[d+(V_s/2)H_s′]/[sqrt(V_s)H_s], exactly the claimed minimizing-test pairing. Uniform positivity on each compact segment justifies differentiation and integration. With signed d,e this is a signed subtraction identity; it is not a derivative of R_+.\n\nG. The author’s U_31 has ε_31≈0.315336<3/8. The reconstruction’s alternative q_16=8−(16−G_p)^(3/4) has curvature loss exactly 3/8 and gives a strict lower bound (3/8)(w1+w2). Both are valid mutual-type references. The height distribution gives min a=1, max a=3 and H=(log 3)/2. Hence R_−=3/2, R_+=9/2, V_μ(β)=3/log 3 and V_μ(θ)=4/log 3, with every trace equal to (1/4)ord_E(π*D). The residual first moment is infinite. The point-blowup conclusions follow from E. The target backgrounds are genuinely nonclosed; the auxiliary K is closed.\n\nDependency audit: the supplied note graph is acyclic: n1 has no note parents; n2←n1; n3←n1; n4←n1,n2,n3; n5←n1,n2,n3; n6←n2; n7←n1,…,n6. Every listed parent is available and checked; some edges are unnecessary but harmless. At the mathematical level, canonical local arguments use premise 2 and permitted elementary foundations; B additionally uses premises 0,1,3,4; C uses A and transverse integrability; D uses the separated reference; E uses canonical arguments, B and C; F uses only permitted sphere Poisson solvability, Stokes and matrix inequalities; G uses A–F. Premise 5 concerns attribution, not an indispensable calculation dependency.\n\nFresh primary checks confirm the auxiliary product facts in [BEGZ](https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf). Existing definitions and divisorial/modification laws retain [BGL’s credit](https://d-nb.info/1374372846/34). Companion bounded-residual trace constructions, floor ideals, subtraction mechanisms and the local exceptional-curve obstruction also retain their stated credit. Their unrelated coefficient and envelope assertions are outside this proof graph. The historical report’s verdict and repeated short evidence fragments are not adopted as proof; its unresolved full scope remains unresolved.\n\nHarmless wording corrections are already incorporated in the current version: b=0 denotes the identically zero divisorial term, only the target backgrounds are described as nonclosed, d and e are declared, and pure-pullback claims are confined to the stated masses and trace transport. Logarithmic moment divergence refers to the T-cutoff. No substantial repair of an A–G proof was required. This restricted PASS establishes no priority claim, unrestricted S11 completion, general Hermitian strict-type criterion, exceptional-subtraction invariance, or multiplier-ideal pullback theorem.",
  "passages": [
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/0",
      "statement": "On a compact Kahler manifold, the non-pluripolar product of finitely many closed positive (1,1) currents of total degree at most the dimension is well defined and has finite mass.",
      "url": "urn:xean:task",
      "quote": "On a compact Kahler manifold, the non-pluripolar product of finitely many closed positive (1,1) currents of total degree at most the dimension is well defined and has finite mass.",
      "premise": 0
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/1",
      "statement": "On a compact Kahler manifold, two tuples of cohomologous closed positive (1,1) currents with small unbounded locus satisfy the ordinary-singularity-order comparison of the cohomology classes of their non-pluripolar products: if every current of the first tuple is less singular, its product class minus the second product class is pseudoeffective. Small unbounded locus means local boundedness outside a closed locally complete pluripolar set.",
      "url": "urn:xean:task",
      "quote": "On a compact Kahler manifold, two tuples of cohomologous closed positive (1,1) currents with small unbounded locus satisfy the ordinary-singularity-order comparison of the cohomology classes of their non-pluripolar products: if every current of the first tuple is less singular, its product class minus the second product class is pseudoeffective. Small unbounded locus means local boundedness outside a closed locally complete pluripolar set.",
      "premise": 1
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/2",
      "statement": "For a closed pluripolar set A in a complex manifold, a psh function on its complement which is locally bounded above near A extends uniquely to a genuine canonical psh function. Genuine psh functions have positive distributional complex Hessian, and their pullbacks under holomorphic maps are psh, possibly identically minus infinity on a component.",
      "url": "urn:xean:task",
      "quote": "For a closed pluripolar set A in a complex manifold, a psh function on its complement which is locally bounded above near A extends uniquely to a genuine canonical psh function. Genuine psh functions have positive distributional complex Hessian, and their pullbacks under holomorphic maps are psh, possibly identically minus infinity on a component.",
      "premise": 2
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/3",
      "statement": "A well-defined non-pluripolar product of closed positive (1,1)-currents on a complex manifold is closed (BEGZ Theorem 1.8).",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "is closed.",
      "premise": 3
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/4",
      "statement": "Locally, ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ for psh φ; for locally bounded potentials off a closed locally complete pluripolar set, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from its complement (BEGZ §1.2).",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "hddcui = 1{u>−∞} ddcu.",
      "premise": 4
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/5",
      "statement": "Locally, ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ for psh φ; for locally bounded potentials off a closed locally complete pluripolar set, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from its complement (BEGZ §1.2).",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "but the trivial extension",
      "premise": 4
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/6",
      "statement": "On a compact complex manifold with BMP, the lower and upper volumes of a quasi-closed positive (1,1)-current are the finite top-mass infimum and supremum in its dd^c-class and ordinary singularity type. Effective real divisor addition and smooth compact modification pullback preserve both volumes (BGL, Definition 3.1; Proposition 3.3).",
      "url": "https://d-nb.info/1374372846/34",
      "quote": "with equivalent singularities.",
      "premise": 5
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/7",
      "statement": "On a compact complex manifold with BMP, the lower and upper volumes of a quasi-closed positive (1,1)-current are the finite top-mass infimum and supremum in its dd^c-class and ordinary singularity type. Effective real divisor addition and smooth compact modification pullback preserve both volumes (BGL, Definition 3.1; Proposition 3.3).",
      "url": "https://d-nb.info/1374372846/34",
      "quote": "for any modification π : Y → X we have",
      "premise": 5
    }
  ],
  "premises": [
    "On a compact Kahler manifold, the non-pluripolar product of finitely many closed positive (1,1) currents of total degree at most the dimension is well defined and has finite mass.",
    "On a compact Kahler manifold, two tuples of cohomologous closed positive (1,1) currents with small unbounded locus satisfy the ordinary-singularity-order comparison of the cohomology classes of their non-pluripolar products: if every current of the first tuple is less singular, its product class minus the second product class is pseudoeffective. Small unbounded locus means local boundedness outside a closed locally complete pluripolar set.",
    "For a closed pluripolar set A in a complex manifold, a psh function on its complement which is locally bounded above near A extends uniquely to a genuine canonical psh function. Genuine psh functions have positive distributional complex Hessian, and their pullbacks under holomorphic maps are psh, possibly identically minus infinity on a component.",
    "A well-defined non-pluripolar product of closed positive (1,1)-currents on a complex manifold is closed (BEGZ Theorem 1.8).",
    "Locally, ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ for psh φ; for locally bounded potentials off a closed locally complete pluripolar set, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from its complement (BEGZ §1.2).",
    "On a compact complex manifold with BMP, the lower and upper volumes of a quasi-closed positive (1,1)-current are the finite top-mass infimum and supremum in its dd^c-class and ordinary singularity type. Effective real divisor addition and smooth compact modification pullback preserve both volumes (BGL, Definition 3.1; Proposition 3.3)."
  ],
  "kind": "codex-report",
  "operationId": "a2042535-13db-4932-b9e8-bed722d56bc2",
  "reportedAt": "2026-10-08T10:31:12.747Z"
}


## Complete primary application context: BEGZ, lines 270--455

URL: https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf
Text SHA256: 1b4035bd5a2d88f8872f882b34694a9f2ff1f30ee38cef644f4ad584a1d3b144

```text

     Here ω is an auxiliary (strictly) positive (1, 1)-form on X with respect to which
masses are being measured, the condition being of course independent of ω. When (1.2)
                                                                      Vp       c
is satisfied, equation (1.1) indeed defines a positive (p, p)-current   j=1 dd uj on X.
We will show below that it is automatically closed (Theorem 1.8).
     Condition (1.2) is always satisfied when p=1, and in fact it is not difficult to show
that
                                 hddc ui = 1{u>−∞} ddc u.

There are however examples where non-pluripolar products are not well defined as soon
as p⩾2. This is most easily understood in the following situation.

     Definition 1.2. A psh function u on X will be said to have small unbounded locus
if there exists a (locally) complete pluripolar closed subset A of X outside which u is
locally bounded.

     Assume that u1 , ..., up have small unbounded locus, and let A be a closed complete
pluripolar subset of X such that each uj is locally bounded outside A (recall that complete
                                                             Vp      c
pluripolar subsets are stable under finite unions). Then      j=1 dd uj is well defined if
                                          Vp
and only if the Bedford–Taylor product j=1 ddc uj , which is defined on the open subset
                                                                   Vp       c
X \A, has locally finite mass near each point of A. In that case      j=1 dd uj is nothing
                              Vp     c
but the trivial extension of j=1 dd uj to X.

      Example 1.3. Consider Kiselman’s example (see [28])

                                 u(x, y) := (1−|x|2 )(− log |y|)1/2
                 monge–ampère equations in big cohomology classes                              205


for (x, y)∈C2 near 0. The function u is psh near 0, it is smooth outside the y=0 axis,
but the smooth measure (ddc u)2 , defined outside y=0, is not locally finite near any point
of y=0. This means that the positive Borel measure h(ddc u)2 i is not locally finite.
    We now collect some basic properties of non-pluripolar products.
    Proposition 1.4. Let u1 , ..., up be psh functions on X.
    (a) The operator
                                              ^p         
                          (u1 , ..., up ) 7−!      ddc uj
                                                            j=1

is local in the plurifine topology whenever it is well defined.
                         Vp       c
      (b) The current       j=1 dd uj and the fact that it is well defined , both only depend
                     c
on the currents dd uj , not on the specific potentials uj .
      (c) Non-pluripolar products, which are obviously symmetric, are also multilinear in
the following sense: if v1 is another psh function, then
                            ^p                  ^p                    ^p       
              c        c           c         c           c           c           c
          (dd u1 +dd v1 )∧      dd uj = dd u1 ∧        dd uj + dd v1 ∧         dd uj ,
                             j=2                                j=2                       j=2

in the sense that the left-hand side is well defined if and only if both terms in the right-
hand side are, and equality holds in this case.
     Proof. (a) If uj and vj are psh functions on X such that uj =vj on a given plurifine
open subset O, then the locally bounded psh functions max{uj , −k} and max{vj , −k}
also coincide on O. If we set
                                       p
                                       \                        p
                                                                \
                              Ek :=         {uj > −k}∩              {vj > −k},
                                      j=1                   j=1

then we infer that
                        p
                        ^                                             p
                                                                      ^
                1O∩Ek         ddc max{uj , −k} = 1O∩Ek                      ddc max{vj , −k}.
                        j=1                                           j=1

Hence in the limit
                                     p
                                    ^                          p
                                                                ^            
                              1O            ddc uj       = 1O           ddc vj ,
                                      j=1                         j=1

as desired by Lemma 1.5 below.
    (b) Let wj be pluriharmonic on X, and let K be a compact subset. We can find
C >0 such that wj ⩽C on an open neighborhood V of K. On the plurifine open subset
                             p
                             \                                   p
                                                                 \
                     Ok :=         {uj +wj > −k}∩V ⊂                  {uj > −k−C}∩V
                             j=1                                j=1
206                     s. boucksom, p. eyssidieux, v. guedj and a. zeriahi


the following locally bounded psh functions coincide:

              max{uj +wj , −k} = max{uj , −wj −k}+wj = max{uj , −k−C}+wj .

Since ddc wj =0, it follows that

      Z               p
                      ^
            ω n−p ∧         ddc max{uj +wj , −k}
       Ok             j=1
                                             Z                     p
                                                                   ^
                                         =          ω n−p ∧             ddc max{uj , −k−C}
                                               Ok                 j=1
                                             Z                                            p
                                                                                          ^
                                                                                n−p
                                         ⩽     Tp
                                                                            ω         ∧         ddc max{uj , −k−C},
                                                 j=1 {uj >−k−C}∩V                         j=1


which is uniformly bounded in k by assumption, and the second point is proved.
      The proof of (c) is similarly easy but tedious and will be left to the reader.
                                                                                          Vp      c
    Lemma 1.5. Assume that the non-pluripolar product                                       j=1 dd uj    is well defined.
Then for every sequence of Borel subsets Ek such that

                                                            p
                                                            \
                                                 Ek ⊂             {uj > −k}
                                                            j=1

            S∞
and X \      k=1 Ek is pluripolar , we have

                                         p
                                         ^                                     p
                                                                              ^                  
                                                    c                                       c
                               lim 1Ek         dd max{uj , −k} =                          dd uj
                              k!∞
                                         j=1                                     j=1


against all bounded measurable functions.

      Proof. This follows by dominated convergence from

                                          p                                 p
                                                                           ^      
                                         ^             c                       c
               1T p
                  j=1 {uj >−k}
                                 −1Ek            dd max{uj , −k} ⩽ (1−1Ek )   dd uj .
                                          j=1                                                     j=1


    A crucial point for what follows is that non-pluripolar products of globally defined
currents are always well defined on compact Kähler manifolds.

     Proposition 1.6. Let T1 , ..., Tp be closed positive (1, 1)-currents on a compact
Kähler manifold X. Then their non-pluripolar product hT1 ∧...∧Tp i is well defined.
                      monge–ampère equations in big cohomology classes                                         207


     Proof. Let ω be a Kähler form on X. In view of Proposition 1.4 (c), upon adding
a large multiple of ω to the Tj ’s, we may assume that their cohomology classes are
Kähler classes. We can thus find Kähler forms ωj and ωj -psh functions ϕj such that
Tj =ωj +ddc ϕj . Let U be a small open subset of X on which ωj =ddc ψj , where ψj ⩽0 is
a smooth psh function on U , so that Tj =ddc uj on U with uj :=ψj +ϕj . The bounded
psh functions on U ,
                                ψj +max{ϕj , −k}         and       max{uj , −k}

coincide on the plurifine open subset {uj >−k}⊂{ϕj >−k}, thus we have

```


## Complete primary application context: BEGZ, lines 450--630

URL: https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf
Text SHA256: 1b4035bd5a2d88f8872f882b34694a9f2ff1f30ee38cef644f4ad584a1d3b144

```text
Tj =ωj +ddc ϕj . Let U be a small open subset of X on which ωj =ddc ψj , where ψj ⩽0 is
a smooth psh function on U , so that Tj =ddc uj on U with uj :=ψj +ϕj . The bounded
psh functions on U ,
                                ψj +max{ϕj , −k}         and       max{uj , −k}

coincide on the plurifine open subset {uj >−k}⊂{ϕj >−k}, thus we have
   Z                            p
                                ^
    Tp
                      ω n−p ∧         ddc max{uj , −k}
       j=1 {uj >−k}             j=1
                                                  Z                                  p
                                                                                     ^
                                                                           n−p
                                              =    Tp
                                                                       ω         ∧         (ωj +ddc max{ϕj , −k})
                                                      j=1 {uj >−k}                   j=1
                                                  Z              p
                                                                 ^
                                              ⩽        ω n−p ∧         (ωj +ddc max{ϕj , −k}).
                                                   X             j=1


But the latter integral is computed in cohomology, and hence is independent of k. This
shows that (1.2) is satisfied on U .

      Remark 1.7. The same property extends to the case where X is a compact complex
manifold in the Fujiki class, i.e. bimeromorphic to a compact Kähler manifold. Indeed
there exists in that case a modification µ: X 0 !X with X 0 compact Kähler. Since µ is an
isomorphism outside closed analytic (hence pluripolar) subsets, it is easy to deduce that
hT1 ∧...∧Tp i is well defined on X from the fact that hµ∗ T1 ∧...∧µ∗ Tp i is well defined on
X 0 , and in fact
                                    hT1 ∧...∧Tp i = µ∗ hµ∗ T1 ∧...∧µ∗ Tp i.

On the other hand, it seems to be unknown whether finiteness of non-pluripolar products
holds on arbitrary compact complex manifolds.

     Building on the proof of the Skoda–El Mir extension theorem, we will now prove the
less trivial closedness property of non-pluripolar products.

   Theorem 1.8. Let T1 , ..., Tp be closed positive (1, 1)-currents on a complex manifold
X whose non-pluripolar product is well defined. Then, the positive (p, p)-current

                                                  hT1 ∧...∧Tp i

is closed.
208              s. boucksom, p. eyssidieux, v. guedj and a. zeriahi


    Proof. The result is of course local, and we can assume that X is a small neighbor-
hood of 0∈Cn . The proof will follow rather closely Sibony’s proof of the Skoda–El Mir
theorem [35], cf. also [18, pp. 159–161]. Let uj ⩽0 be a local potential of Tj near 0∈Cn ,
and for each k consider the closed positive current of bidimension (1, 1),
                                           p
                                           ^
                                Θk := %∧         ddc max{uj , −k}
                                           j=1


and the plurifine open subset
                                             p
                                             \
                                    Ok :=         {uj > −k}
                                            j=1

so that 1Ok Θk converges towards

                                      %∧hT1 ∧...∧Tp i

by (1.1). Here % is a positive (n−p−1, n−p−1)-form with constant coefficients, so that
Θk has bidimension (1, 1). It is enough to show that

                                     lim d(1Ok Θk ) = 0
                                    k!∞

for any choice of such a form %.
                  Pp
     Let also u:= j=1 uj , so that u⩽−k outside Ok , and set

                                      wk := χ(eu/k ),

where χ(t) is a smooth convex and non-decreasing function of t∈R such that χ(t)=0 for
t⩽ 12 and χ(1)=1. We thus see that 0⩽wk ⩽1 is a non-decreasing sequence of bounded
psh functions defined near 0∈Cn with wk =0 outside Ok and wk !1 pointwise outside
the pluripolar set {u=−∞}. Finally let 0⩽θ(t)⩽1 be a smooth non-decreasing function
of t∈R such that θ(t)=0 for t⩽ 21 and θ≡1 near t=1. The functions θ(wk ) are bounded,
non-decreasing in k and we have
                                      θ(wk ) ⩽ 1Ok

since θ(wk )⩽1 vanishes outside Ok . Note also that θ0 (wk ) vanishes outside Ok , and
converges to 0 pointwise outside {u=−∞}.
     Our goal is to show that
                                   lim d(1Ok Θk ) = 0.
                                    k!∞

But we have
                     0 ⩽ (1Ok −θ(wk ))Θk ⩽ (1−θ(wk ))hT1 ∧...∧Tp i,
                  monge–ampère equations in big cohomology classes                                  209


and the latter converges to 0 by dominated convergence since θ(wk )!1 pointwise outside
the polar set of u, which is negligible for hT1 ∧...∧Tp i. It is thus equivalent to show that

                                        lim d(θ(wk )Θk ) = 0.
                                        k!∞

Since wk is a bounded psh function, Lemma 1.9 below shows that the chain rule applies,
that is
                            d(θ(wk )Θk ) = θ0 (wk ) dwk ∧Θk .

Recall that dwk ∧Θk has order 0 by the Bedford–Taylor theorem, so that the right-hand
side makes sense. Now let ψ be a given smooth 1-form compactly supported near 0 and
let τ ⩾0 be a smooth cut-off function with τ ≡1 on the support of ψ. The Cauchy–Schwarz
inequality implies that
       Z                        2       Z                        Z                        
              0                                        c                  0    2
             θ (wk )ψ∧dwk ∧Θk       ⩽           τ dwk ∧d wk ∧Θk          θ (wk ) ψ∧ ψ∧Θk .
         X                                  X                        X

But we have
      Z                    Z                 Z                 Z
    2   τ dwk ∧dc wk ∧Θk ⩽   τ ddc wk2 ∧Θk =   wk2 ddc τ ∧Θk =                     wk2 ddc τ ∧Θk ,
        X                        X                         X                  Ok

since wk vanishes outside Ok , and the last integral is uniformly bounded, as 0⩽wk ⩽1
and 1Ok Θk has uniformly bounded mass by (1.2). On the other hand, we have

                    θ0 (wk )2 Θk = θ0 (wk )2 1Ok Θk ⩽ θ0 (wk )2 hT1 ∧...∧Tp i,

since θ0 (wk ) also vanishes outside Ok , and we conclude that
                                        Z
                                lim          θ0 (wk )2 ψ∧ ψ∧Θk = 0
                                k!∞      X

by dominated convergence as θ0 (wk )!0 pointwise outside the polar set of u, which is
negligible for hT1 ∧...∧Tp i. The proof is thus complete.

     Lemma 1.9. Let Θ be a closed positive (p, p)-current on a complex manifold X, f
be a smooth function on R and v be a bounded psh function. Then we have

                                     d(f (v)Θ) = f 0 (v) dv∧Θ.

    Proof. This is a local result, and we can thus assume that Θ has bidimension (1, 1)
by multiplying it by constant forms as above. The result is of course true when v is
smooth. As we shall see the result holds true in our case basically because v belongs
210                 s. boucksom, p. eyssidieux, v. guedj and a. zeriahi


to the Sobolev space L21 (Θ), in the sense that dv∧dc v∧Θ is well defined. Indeed the
result is standard when Θ=[X], and proceeds by approximation. Here we let vk be a
decreasing sequence of smooth psh functions converging pointwise to v. We then have
f (vk )θ!f (v)Θ by dominated convergence. Thus it suffices to show that
                                lim f 0 (vk ) dvk ∧Θ = f 0 (v) dv∧Θ.
                               k!∞

We write
          f 0 (vk ) dvk ∧Θ−f 0 (v) dv∧Θ = (f 0 (vk )−f 0 (v)) dvk ∧Θ+f 0 (v)(dvk −dv)∧Θ.
Let ψ be a test 1-form and τ ⩾0 be a smooth cut-off function with τ ≡1 on the support
of ψ. The Cauchy–Schwarz inequality implies that
  Z                           2  Z                          Z                  
       0       0                        0       0    2                      c
     (f (vk )−f (v))ψ∧dvk ∧Θ ⩽        (f (vk )−f (v)) ψ∧ ψ∧Θ        τ dvk ∧d vk ∧Θ .
   X                                       X                              X
                                                c                          c
The second factor is bounded since dvk ∧d vk ∧Θ converges to dv∧d v∧Θ by Bedford–
Taylor’s monotone convergence theorem, and the first one converges to 0 by dominated
convergence. We similarly have
   Z                        2  Z                  Z                          
      f 0 (v)(dvk −dv)∧ψ∧Θ ⩽        f 0 (v)2 ψ∧ ψ∧Θ     τ d(vk −v)∧dc (vk −v)∧Θ ,
      X                                X                       X
where now the first factor is bounded while the second one tends to 0 by Bedford–Taylor’s
theorem once again, and the proof is complete.
    Remark 1.10. Injecting as above Lemma 1.9 in the proof of Skoda–El Mir’s extension
theorem presented in [18, pp. 159–161] shows that Skoda–El Mir’s result remains true for
complete pluripolar subsets that are not necessarily closed, in the following sense: let Θ
be a closed positive (p, p)-current and let A be a complete pluripolar subset of X. Then
1X\A Θ and thus also 1A Θ are closed.
     We conclude this section with a log-concavity property of non-pluripolar products.

```


## Complete primary application context: BEGZ, lines 917--1017

URL: https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf
Text SHA256: 1b4035bd5a2d88f8872f882b34694a9f2ff1f30ee38cef644f4ad584a1d3b144

```text
                                   (k)   (k)
assumption, it follows that uk :=ϕ1 −ϕ2 can be taken to be uniformly bounded with
respect to k. We can thus assume that 0⩽uk ⩽C for all k.
    Now the formula ddc v 2 =2v ddc v+2 dv∧dc v and Bedford–Taylor’s continuity theo-
rem imply by polarization identities that

                                         (k)         (k)
                               lim dϕi ∧dc ϕj ∧Θ = dϕi ∧dc ϕj ∧Θ
                              k!∞


weakly on U for any two indices i and j. Hence also

                                     duk ∧dc uk ∧Θ ! du∧dc u∧Θ
                 monge–ampère equations in big cohomology classes                            217


weakly on U . We thus get
                      Z                                      Z
                                       c
                              du∧d u∧Θ ⩽ lim inf                     duk ∧dc uk ∧Θ,
                          U                      k!∞             X

and our goal is to show that the right-hand integrals are uniformly bounded. Now Stokes’
theorem yields
     Z                      Z                  Z                   Z
                 c                   c                  c (k)                 (k)
         duk ∧d uk ∧Θ = −       uk dd uk ∧Θ =     uk dd ϕ2 ∧Θ−        uk ddc ϕ1 ∧Θ.
        X                         X                          X                            X

For each i=1, 2 we have
                                                 (k)                         (k) 
                           0 ⩽ uk ω+ddc ϕi               ⩽ C ω+ddc ϕi                 .

Hence                          Z                                         Z
                                                    (k) 
                          0⩽           uk ω+ddc ϕi           ∧Θ ⩽ C           ω∧Θ
                                   X                                      X

so that                    Z               Z                                  Z
                                                       (k)
                                                         c
                      −C          ω∧Θ ⩽         uk dd ϕi ∧Θ ⩽ C                    ω∧Θ
                              X             X                                  X

                                                           duk ∧dc uk ∧Θ follows.
                                                   R
for all k, and the uniform boundedness of              X

     The following crucial result shows that non-pluripolar masses are basically non-
increasing with singularities, at least for currents with small unbounded locus.

      Theorem 1.16. For j =1, ..., p, let Tj and Tj0 be two cohomologous closed positive
(1, 1)-currents with small unbounded locus, and assume also that Tj is less singular than
Tj0 . Then the cohomology classes of their non-pluripolar products satisfy

                                  {hT1 ∧...∧Tp i} ⩾ {hT10 ∧...∧Tp0 i}

in H p,p (X, R), with ⩾ meaning that the difference is pseudo-effective, i.e. representable
by a closed positive (p, p)-current.

     The statement of course makes sense for arbitrary closed positive (1, 1)-currents,
and we certainly expect it to hold true in general, but we are only able for the moment
to prove it in the special case of currents with small unbounded locus.

    Proof. By duality, this is equivalent to showing that
                       Z                      Z
                              T1 ∧...∧Tp ∧τ ⩾      T10 ∧...∧Tp0 ∧τ
                           X\A                               X\A

for every positive smooth ddc -closed (n−p, n−p)-form τ , where A is a closed complete
pluripolar set outside of which all currents Ti and Ti0 have locally bounded potentials.
218                s. boucksom, p. eyssidieux, v. guedj and a. zeriahi


Replacing successively Ti by Ti0 , we can assume that Ti =Ti0 for i>1. The bidimension-
(1, 1) current
                                    Θ := hT2 ∧...∧Tp i∧τ

is ddc -closed and positive. Writing T1 =θ+ddc ϕ and T10 =θ+ddc ϕ0 , where θ is a smooth
form in their common cohomology class, we are reduced to showing that
                              Z             Z
                                      c
                                   dd ϕ∧Θ ⩾        ddc ϕ0 ∧Θ
                               X\A                 X\A

if ϕ⩾ϕ0 are quasi-psh functions on X, locally bounded on X \A, and Θ is a ddc -closed
positive bidimension-(1, 1) current on X. Let ψ be a quasi-psh function such that A=
{ψ=−∞}. Replacing ϕ0 by ϕ0 +εψ and letting ε!0 in the end, we may further assume
that ϕ0 −ϕ!−∞ near A. For each k the function ψk :=max{ϕ0 , ϕ−k} thus coincides
with ϕ−k in some neighborhood of A, so that
                             Z               Z
                                     c
                                  dd ψk ∧Θ =      ddc ϕ∧Θ
                               X\A                  X\A

by Stokes’ theorem, since (the trivial extension of) ddc (ϕ−ψk )∧Θ is the exterior deriv-
ative of a current with compact support on X \A. On the other hand


```


## Complete primary application context: Demailly, lines 2055--2190

URL: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf
Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

```text
                                        2π     0

An integration of (5.2) over ξ ∈ S(0, r) yields u(a) ⩽ µS (u ; a, r), therefore

(5.3)                                    Psh(Ω) ⊂ Sh(Ω).

The following results have already been proved for subharmonic functions and are easy
to extend to the case of plurisubharmonic functions:

(5.4) Theorem. For any decreasing sequence of plurisubharmonic functions uk ∈
Psh(Ω), the limit u = lim uk is plurisubharmonic on Ω.

(5.5) Theorem. Let u ∈ Psh(Ω) be such that u 6≡ −∞ on every connected component
of Ω. If (ρε ) is a family of smoothing kernels, then u ⋆ ρε is C∞ and plurisubharmonic
on Ωε , the family (u ⋆ ρε ) is non decreasing in ε and limε→0 u ⋆ ρε = u.

(5.6) Theorem. Let u1 , . . . , up ∈ Psh(Ω) and χ : Rp −→ R be a convex function such
that χ(t1 , . . . , tp ) is non decreasing in each tj . Then χ(u1 , . . . , up ) is plurisubharmonic on
Ω. In particular u1 +· · ·+up , max{u1 , . . . , up }, log(eu1 +· · ·+eup ) are plurisubharmonic
on Ω.

(5.7) Theorem. Let {uα } ⊂ Psh(Ω) be locally uniformly bounded from above and
u = sup uα . Then the regularized upper envelope u⋆ is plurisubharmonic and is equal to
u almost everywhere.
Proof. By Choquet’s lemma, we may assume that (uα ) is countable. Then u is a Borel
function which clearly satisfies (5.2), and thus u ⋆ ρε also satisfies (5.2). Hence u ⋆
ρε is plurisubharmonic. By Proposition 4.24, u⋆ = u almost everywhere and u⋆ is
subharmonic, so
                              u⋆ = lim u⋆ ⋆ ρε = lim u ⋆ ρε
40                      Chapter I. Complex Differential Calculus and Pseudoconvexity

is plurisubharmonic.                                                                      

   If u ∈ C 2 (Ω, R), the subharmonicity of restrictions of u to complex lines, C ∋ w 7−→
u(a + wξ), a ∈ Ω, ξ ∈ Cn , is equivalent to

                   ∂2                    X        ∂ 2u
                       u(a + wξ) =                        (a + wξ) ξj ξ k ⩾ 0.
                  ∂w∂w                           ∂zj ∂z k
                                       1⩽j,k⩽n

                                                     P 2
Therefore, u is plurisubharmonic on Ω if and only if  ∂ u/∂zj ∂z k (a) ξj ξ k is a semiposi-
tive hermitian form at every point a ∈ Ω. This equivalence is still true for arbitrary
plurisubharmonic functions, under the following form:

(5.8) Theorem. If u ∈ Psh(Ω), u 6≡ −∞ on every connected component of Ω, then for
all ξ ∈ Cn
                                  X    ∂ 2u
                      Hu(ξ) :=                 ξj ξ k ∈ D′ (Ω)
                                      ∂zj ∂z k
                                     1⩽j,k⩽n

is a positive measure. Conversely, if v ∈ D′ (Ω) is such that Hv(ξ) is a positive measure
for every ξ ∈ Cn , there exists a unique function u ∈ Psh(Ω) locally integrable on Ω such
that v is the distribution associated to u.
Proof. If u ∈ Psh(Ω), then Hu(ξ) = weak lim H(u ⋆ ρε )(ξ) ⩾ 0. Conversely, Hv ⩾ 0
implies H(v ⋆ ρε ) = (Hv) ⋆ ρε ⩾ 0, thus v ⋆ ρε ∈ Psh(Ω), and also ∆v ⩾ 0, hence (v ⋆ ρε )
is non decreasing in ε and u = limε→0 v ⋆ ρε ∈ Psh(Ω) by Th. 5.4.                      

(5.9) Proposition. The convex cone Psh(Ω) ∩ L1loc (Ω) is closed in L1loc (Ω), and it has
the property that every bounded subset is relatively compact.

§ 5.B. Relations with Holomorphic Functions
   In order to get a better geometric insight, we assume more generally that u is a C 2
function on a complex n-dimensional manifold X. The complex Hessian of u at a point
a ∈ X is the hermitian form on TX defined by
                                     X        ∂ 2u
(5.10)                    Hua =                       (a) dzj ⊗ dz k .
                                             ∂zj ∂z k
                                   1⩽j,k⩽n


If F : X −→ Y is a holomorphic mapping and if v ∈ C 2 (Y, R), we have d′ d′′ (v ◦ F ) =
F ⋆ d′ d′′ v. In equivalent notations, a direct calculation gives for all ξ ∈ TX,a
                                       
                          X ∂ 2 v F (a) ∂Fl a) ∂Fm a)                       
         H(v ◦ F )a (ξ) =                     ξj      ξk = HvF (a) F ′ (a).ξ .
                              ∂zl ∂z m   ∂zj     ∂zk
                        j,k,l,m

In particular Hua does not depend on the choice of coordinates (z1 , . . . , zn ) on X, and
Hva ⩾ 0 on Y implies H(v ◦ F )a ⩾ 0 on X. Therefore, the notion of plurisubharmonic
function makes sense on any complex manifold.

(5.11) Theorem. If F : X −→ Y is a holomorphic map and v ∈ Psh(Y ), then v ◦ F ∈
Psh(X).
                      § 5. Plurisubharmonic Functions                                            41

Proof. It is enough to prove the result when X = Ω1 ⊂ Cn and X = Ω2 ⊂ Cp are
open subsets . The conclusion is already known when v is of class C 2 , and it can be
extended to an arbitrary upper semicontinuous function v by using Th. 5.4 and the fact
that v = lim v ⋆ ρε .                                                               

(5.12) Example. By (3.22) we see that log |z| is subharmonic on C, thus log |f | ∈
Psh(X) for every holomorphic function f ∈ O(X). More generally
                                                     
                        log |f1 |α1 + · · · + |fq |αq ∈ Psh(X)
for every fj ∈ O(X) and αj ⩾ 0 (apply Th. 5.6 with uj = αj log |fj | ).

§ 5.C. Convexity Properties
    The close analogy of plurisubharmonicity with the concept of convexity strongly sug-
gests that there are deeper connections between these notions. We describe here a few
elementary facts illustrating this philosophy. Another interesting connection between
plurisubharmonicity and convexity will be seen in § 7.B (Kiselman’s minimum princi-
ple).

(5.13) Theorem. If Ω = ω + iω ′ where ω, ω ′ are open subsets of Rn , and if u(z) is a
plurisubharmonic function on Ω that depends only on x = Re z, then ω ∋ x 7−→ u(x) is
convex.
Proof. This is clear when u ∈ C 2 (Ω, R), for ∂ 2 u/∂zj ∂z k = 41 ∂ 2 u/∂xj ∂xk . In the general
case, write u = lim u ⋆ ρε and observe that u ⋆ ρε (z) depends only on x.                     

(5.14)
Q      Corollary. If u is a plurisubharmonic function in the open polydisk D(a, R) =
  D(aj , Rj ) ⊂ Cn , then
                                        Z 2π
                                     1
         µ(u ; r1 , . . . , rn ) =           u(a1 + r1 eiθ1 , . . . , an + rn eiθn ) dθ1 . . . dθn ,
                                   (2π)n 0
        m(u ; r1 , . . . , rn ) = sup u(z1 , . . . , zn ),   rj < R j
                               z∈D(a,r)

are convex functions of (log r1 , . . . , log rn ) that are non decreasing in each variable.
Proof. That µ is non decreasing follows from the subharmonicity of u along every coor-
dinate axis. Now, it is easy to verify that the functions
                                     Z 2π
                                 1
         e(z1 , . . . , zn ) =
         µ                         n
                                          u(a1 + ez1 eiθ1 , . . . , an + ezn eiθn ) dθ1 . . . dθn ,
                               (2π) 0
         e 1 , . . . , zn ) = sup u(a1 + ez1 w1 , . . . , an + ezn wn )
        m(z

```


## Complete primary application context: Demailly, lines 2300--2355

URL: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf
Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

```text
is smooth and plurisubharmonic on X.                                                                                          

(5.20) Definition. A function u ∈ Psh(X) is said to be strictly plurisubharmonic if
u ∈ L1loc (X) and if for every point x0 ∈ X there exists aPneighborhood Ω of x0 and c > 0
such that u(z) − c|z|2 is plurisubharmonic on Ω, i.e.       (∂ 2 u/∂zj ∂z k )ξj ξ k ⩾ c|ξ|2 (as
                                  n
distributions on Ω) for all ξ ∈ C .

(5.21) Theorem ([Richberg 1968]). Let u ∈ Psh(X) be a continuous function which is
strictly plurisubharmonic on an open subset Ω ⊂ X, with Hu ⩾ γ for some continuous
positive hermitian form γ on Ω. For any continuous function λ ∈ C 0 (Ω), λ > 0, there
                                   e in C 0 (X) ∩ C∞ (Ω) such that u ⩽ u
exists a plurisubharmonic function u                                   e ⩽ u + λ on Ω
44                       Chapter I. Complex Differential Calculus and Pseudoconvexity

    e = u on X rΩ, which is strictly plurisubharmonic on Ω and satisfies H u
and u                                                                        e ⩾ (1−λ)γ.
               e can be chosen strictly plurisubharmonic on X if u has the same property.
In particular, u
Proof. Let (Ωα ) be a locally finite open covering of Ω by relatively compact open balls
contained in coordinate patches of X. Choose concentric balls Ω′′α ⊂ Ω′α ⊂ Ωα of respec-
tive radii rα′′ < rα′ < rα and center z = 0 in the given coordinates z = (z1 , . . . , zn ) near
Ωα , such that Ω′′α still cover Ω. We set

                       uα (z) = u ⋆ ρεα (z) + δα (rα′2 − |z|2 )   on Ωα .

For εα < εα,0 and δα < δα,0 small enough, we have uα ⩽ u + λ/2 and Huα ⩾ (1 − λ)γ
on Ωα . Set
                        ηα = δα min{rα′2 − rα′′2 , (rα2 − rα′2 )/2}.
Choose first δα < δα,0 such that ηα < minΩα λ/2, and then εα < εα,0 so small that
                                                                                          ′′
u ⩽ u ⋆ ρεα < u + ηα on Ωα . As δα (r ′2 − |z|2 ) is ⩽ −2ηα on ∂Ωα and > ηα on Ωα , we
                                                      ′′
have uα < u − ηα on ∂Ωα and uα > u + ηα on Ωα , so that the condition required in
Corollary 5.19 is satisfied. We define
                                  
                                     u            on X r Ω,
                              e=
                              u
                                     M(ηα ) (uα ) on Ω.

By construction, ue is smooth on Ω and satisfies u ⩽ u     e ⩽ u + λ, Hu ⩾ (1 − λ)γ thanks to
                                 e is plurisubharmonic on X, observe that u
5.18 (b,e). In order to see that u                                            e is the uniform
         eα with
limit of u
                                                                    [
                   eα = max u , M(η1 ...ηα ) (u1 . . . uα )
                   u                                          on        Ωβ
                                                                   1⩽β⩽α

    eα = u on the complement.
and u                                                                                          

§ 5.F. Polar and Pluripolar Sets.

```


## Complete primary application context: BGL, lines 1268--1385

URL: https://d-nb.info/1374372846/34
Text SHA256: df45fb022db336d6adab01896ebb65a80cb8e378303145eb7170d94c247e582c

```text

                                                                                           123
                                                                              S. Boucksom et al.


(ii) If Pθ (min(u, v)) ∈ PSH(θ ), (θ + dd c u)n ≤ F(u)μ, and (θ + dd c v)n ≤ F(v)μ,
     then
                     (θ + dd c Pθ (min(u, v)))n ≤ F(Pθ (min(u, v)))μ.
Proof We will only prove the second statement since the first one follows from the
same argument. By Corollary 2.12, we have

      (θ + dd c P θ (min{u, v}))n
        ≤ 1 { P θ (min{u,v})=v≤u} (θ + dd c v)n + 1 { P θ (min{u,v})=u<v} (θ + dd c u)n
        ≤ 1 { P θ (min{u,v})=v≤u} F(v)μ + 1 { P θ (min{u,v})=u<v} F(u)μ
        = 1 { P θ (min{u,v})=v≤u} F( P θ (min{u, v}))μ
           + 1 { P θ (min{u,v})=u<v} F( P θ (min{u, v}))μ
        = F( P θ (min{u, v}))μ.

                                                                                             
                                                                                             


3 The Lower and Upper Volume of a dd c -Class

As above, X denotes an n-dimensional compact complex manifold, assumed through-
out this section to have the bounded mass property. We introduce and study the notion
of lower and upper volume of a dd c -class.

3.1 The Lower and Upper Volume of a Current

Extending [22, Definition 3.1], we introduce:
Definition 3.1 The lower volume and upper volume of a quasi-closed positive (1, 1)-
current T ≥ 0 are defined as
                                                         
                    vol(T ) := inf   S n , vol(T ) := sup   Sn ,
                                  S   X                     S    X

where S ranges over all quasi-closed positive (1, 1)-currents in the same dd c -class as
T and with equivalent singularities.
   Writing T = θ + dd c ϕ with θ smooth and ϕ ∈ PSH(θ ), we equivalently have
                                                     
          vol(T ) = inf (θ + dd c ψ)n , vol(T ) = sup (θ + dd c ψ)n         (3.1)
                      ψ    X                                ψ    X

where ψ ranges over all θ -psh functions such that ψ = ϕ + O(1).
   By definition, the upper and lower volumes of T only depend on its dd c -class and
singularity class, and satisfy

                               0 ≤ vol(T ) ≤ vol(T ) < ∞,

123
Volumes of Bott–Chern Classes


see Lemma 2.4. Note also that

                                     T > 0 ⇒ vol(T ) > 0.                         (3.2)

The analogous result for vol(T ) is unclear in general, even when T is smooth
(see §3.2.3). As a consequence of Theorem 2.8, we have:

Example 3.2 If T is closed, then vol(T ) = vol(T ) =          X T
                                                                    n.


   We first collect a few simple properties:

Proposition 3.3 Pick a quasi-closed current T ≥ 0. Then:
  (i) for all t ∈ R>0 we have

                           vol(t T ) = t n vol(T ), vol(t T ) = t n vol(T );

 (ii) for any quasi-closed current T  ≥ 0 and ε ∈ [0, 1], we have

                                    vol(T + εT  ) ≤ vol(T ) + Cε                  (3.3)

      for a constant C > 0 only depending on {T }, {T  };
(iii) for any effective R-divisor E we have

                      vol(T + [E]) = vol(T ), vol(T + [E]) = vol(T );

(iv) for any modification π : Y → X we have

                           vol(π  T ) = vol(T ), vol(π  T ) = vol(T ).

Proof (i) is obvious from the definition. Pick T  ≥ 0 quasi-closed and 0 ≤ S ∈ {T }
with singularities equivalent to T . Then 0 ≤ S + εT  ∈ {T + εT  } has singularities
equivalent to T + εT  , and hence X (S + εT  )n ≥ vol(T + εT  ). For j = 0, . . . , n,
            n− j is further bounded in terms of {S} = {T } and {T  }, by Lemma 2.4.
 X S ∧T
     j

Thus                       
                      S ≥ (S + εT  )n − Cε ≥ vol(T + εT  ) − Cε
                        n
                     X          X
for a constant C > 0 only depending on {T }, {T  }. Taking the infimum over S yields
(ii).
    Next pick an effective R-divisor E, and note that any 0 ≤ S ∈ {T } satisfies
S + [E] ∈ {T + [E]} and X S n = X (S + [E])n . To prove (iii), it is thus enough
to show that S → S + [E] sets a 1–1 correspondence between positive currents in
{T } with the same singularities as T and positive currents in {T + [E]} with the same
singularities as T + [E]. One direction is clear. Conversely, pick 0 ≤ S  ∈ {T + [E]}
with the same singularities as T + [E]. Write

             T = θ + dd c ψ, [E] = θ E + dd c ψ E , S  = θ + θ E + dd c ϕ 

                                                                               123
                                                                             S. Boucksom et al.


with θ, θ E smooth and ψ ∈ PSH(θ ), ψ E ∈ PSH(θ E ), ϕ  ∈ PSH(θ + θ E ). By assump-
tion we have ϕ  = ψ + ψ E + O(1). In particular, ϕ  − ψ E is θ -psh on X \ supp E
and bounded above, and hence uniquely extends to a θ -psh function ϕ on X , which
satisfies ϕ = ψ + O(1). This shows that S := θ + dd c ϕ ≥ 0 lies in {T }, has the same

```
