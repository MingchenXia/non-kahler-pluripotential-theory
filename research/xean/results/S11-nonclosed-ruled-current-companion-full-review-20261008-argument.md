# Original S11 review: nonclosed ruled restricted masses with an unbounded residual

Assess the UNCHANGED original S11 task and every proposed scoped target.
The article is a root-developed candidate, not an accepted theorem. It supplies
an ambient intrinsic trace system with exact all-real-weight ideals, exact
full-variable ordinary-type optimization beyond bounded residuals, and a
strict ordinary-type threshold. Pure pullback preserves optimized masses;
a point blowup away from the poles supplies a one-sided strict current and
obstructs mutual ordinary-type strictness. The residual can have infinite
first moment. No general restricted invariant or unrestricted S11 closure
is claimed. Check adequacy and known overlap as well as correctness.

The prior known ordinary divisorial-removal and exceptional-curve obstruction
are credited background mechanisms. The closed mass comparison foundation is
BEGZ Theorem1.16 applied only with compact Kähler, CLOSED cohomologous positive
currents and small unbounded locus established. No source reading flag, prior
verdict, finite-energy assumption, closed formula transferred to nonclosed
currents or trace lower bound treated as equality may replace proof. Obtain
fresh primary evidence for each indispensable application. Read the whole
article, entire private proof and complete new unaccepted support proof.


## Entire current standalone working article

```tex
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
\small Working draft. Mathematical review and independent reconstruction pending.
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
pulled-back mutual ordinary type. All backgrounds in this example are
genuinely nonclosed; the residual pole has not been replaced by a bounded
or analytic singularity.

\begin{remark}
Positive restricted lower mass supplies a mutual ordinary strict witness
downstairs within this declared family. It is preserved upstairs as a mass
invariant, while Proposition~\ref{prop:blowup} supplies only a one-sided
strict witness. The construction does not furnish a strict-type criterion
for arbitrary Hermitian backgrounds or solve the unrestricted S11 direction.
\end{remark}

\begin{thebibliography}{9}
\bibitem{BEGZ} S.~Boucksom, P.~Eyssidieux, V.~Guedj and A.~Zeriahi,
\emph{Monge--Amp\`ere equations in big cohomology classes},
Acta Math. \textbf{205} (2010), 199--262, especially Definition~1.2,
Proposition~1.6 and Theorem~1.16.
\href{https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf}{Published primary text}.
\bibitem{Demailly} J.-P.~Demailly, \emph{Complex Analytic and Differential
Geometry}, Chapter~I, Theorems~5.23--5.24.
\href{https://people.math.harvard.edu/~siu/2dmml.pdf}{University-hosted primary text}.
\end{thebibliography}
\end{document}

```

## Entire complete private proof

# S11: a proposed nonclosed restricted invariant with unbounded residual

Private root-origin candidate, mathematically unaccepted. No native review,
independent reconstruction, original-task closure or publication has occurred.
This proof uses the complete NEW S18 first-moment-free supplement as an
unaccepted mathematical dependency. Both must be independently reconstructed.
Known ordinary divisorial removal and closed mass comparison are credited as
foundations; no priority claim is made. This is a concrete restricted family,
not an invariant or strict-current theorem for every nonclosed background.

## Setting and the invariant

Use the unchanged original dd^c=i partial barpartial/(2 pi). Let
Y=P^1 x P^1, with probability Fubini--Study forms w1,w2, a point p on the
first curve, D={p} x P^1 and G=log chordal distance squared to p. Thus
dd^c G=[p]-w1 and max G=0. Fix c>0, a smooth strictly positive function a
on the first curve, a real b>=0, and 0<alpha<1. Put

    theta=c w1+a w2, U=1-(1-G)^alpha,
    reference singularity type [r]=[bG+U].

The type is understood through canonical genuine quasi-psh representatives;
the preliminary representative r need not itself be theta-psh. Nonempty
admissibility will be proved, rather than assumed from its curvature bound.
For each NONEMPTY type define the restricted data

    R_minus(Y,theta,[r])=inf_{v theta-psh, v~r} MA_ext_theta(v)(Y),
    R_plus(Y,theta,[r])=sup_{v theta-psh, v~r} MA_ext_theta(v)(Y).

Every full-variable genuine rough competitor is included. The proposed exact
statements are:

1. The type is nonempty if and only if b<c. For every b<c it contains an
   actual strict current, with its mutual ordinary type preserved.
2. Throughout that nonempty range every competitor has positive finite mass,
   and

       R_minus=2(c-b) min a, R_plus=2(c-b) max a.

3. The induced intrinsic ideal traces in the ambient embedding below are
   tau(E)=b ord_E(D) on EVERY smooth compact modification of Y. The residual
   U has an unbounded nonanalytic ordinary type, invisible to these ideal
   orders, and its first moment can be infinite. The stated mass data do not
   purport to determine an ordinary type from its ideal traces.

The background theta is genuinely nonclosed when a is nonconstant, since
d theta=da wedge w2. It is strictly positive and big. This example uses an
unbounded residual, not the known bounded-residual finite-divisor polynomial.
Its formula will be obtained by actual optimization of the whole type.

## 1. Exact ordinary removal with a genuine unbounded residual

For a genuine theta-psh v~bG+U, set q=v-bG off D. Locally choose an equation
z1=0 of D and write G=log|z1|^2-sigma, with dd^c sigma=w1. Choose a smooth
quadratic rho such that dd^c rho>=theta. Then

    v+rho-b log|z1|^2=q+rho-b sigma

is psh off D: log|z1|^2 is pluriharmonic there, and v+rho is psh. It is
locally bounded above, because q<=U+C<=C and the added functions are smooth.
The canonical removable-singularity theorem extends it to a genuine psh
function. Subtracting rho-b sigma gives the canonical quasi-psh q.

The sharper current inequality is retained. Off D the extended psh current
is bounded below by dd^c rho-theta. On D its measure restriction is positive,
while this smooth form has zero measure restriction. Splitting its coefficient
measures into D and its complement therefore proves the same lower bound
globally. Hence

    beta+dd^c q>=0, beta=(c-b)w1+a w2.

The inequalities q~U first hold off D and extend canonically. In particular
the upper inequality forces q=-infinity on D; both sides have the same
canonical pole values. The identity v=bG+q holds almost everywhere, hence
everywhere for genuine quasi-psh representatives. Distributional
Poincare--Lelong now gives the actual current identity

    theta+dd^c v=b[D]+beta+dd^c q.

Conversely, every genuine beta-psh q~U gives the genuine theta-psh
v=bG+q~r by this identity. This is a bijection of the full ordinary classes,
including fiber-dependent competitors, rather than subtraction of infinite
point values on D.

On the locally bounded complement Y\D the two residual measures coincide.
All finite-level non-pluripolar products give zero mass to the analytic
pluripolar divisor; their smooth-background corrections retain this property.
Thus the exact measure identity, not merely a formal mass identity, is

    MA_ext_theta(bG+q)=MA_ext_beta(q).

No nonclosed intersection-invariance theorem or decomposition of an arbitrary
current into a smooth residual has been used.

## 2. Actual type admissibility and strict ordinary representatives

The first-moment-free S18 proof constructs, for every epsilon>0, a genuine
curve potential U_L~U with dd^c U_L>=-epsilon w, and a canonical pole at p.
Its construction is explicit: replace chi(t)=1-(1-t)^alpha on [-L,0] by
the tangent line chi'(-L)t and shift its unchanged left tail by the finite
constant matching the values at -L. Here chi'(-L)->0 and the derivatives
match. This retains its mutual ordinary type and does not truncate its pole.

If b<c, choose L so that epsilon=chi'(-L)<(c-b)/2. Then

    theta+dd^c(bG+U_L)
       >=b[D]+(c-b-epsilon)w1+a w2
       >=min((c-b)/2,min a)(w1+w2).

This is a genuine strict current with a potential ordinarily equivalent to
r. It is more than a one-sided comparison. In particular it supplies an
admissible reference u0=bG+U_L for use in the original S11 setup.

Conversely, any admissible v~r gives the beta-psh q~U above. Haar averaging
over the second P^1 preserves beta and the inequalities with the base U,
and gives a genuine first-factor potential q0~U satisfying

    (c-b)w+dd^c q0>=0.

Its total measure is c-b by distributional Stokes. If b>c this contradicts
positivity. If b=c the measure is zero, so dd^c q0=0 globally; a genuine
distributionally harmonic function on the compact curve is constant. This
contradicts its mutual ordinary type with the unbounded U. Thus the type is
empty for every b>=c. No numerical mass infimum is assigned to an empty type.

## 3. All rough masses and exact residual trace positivity

For b<c put k=c-b>0 and beta=k w1+a w2. Choose L0 with
epsilon_(L0)<k/2 and let u0=U_(L0). The closed-reference mass proof in the
new S18 supplement works with u0 in place of U even when k<alpha: u0 is
k w-psh, has zero Lelong number, is locally bounded off p, and is of the same type U.
For a closed K=C(w1+w2) dominating beta, its separated product has full
mass and its first non-pluripolar current has no polar component.

Any beta-psh q~U is ordinarily equivalent to u0 and locally bounded off D.
Closed small-unbounded-locus mass comparison in both ordinary orders gives
the same closed top mass and the same first-current cohomology class. The
positive polar trace then vanishes. Expanding against beta-K and integrating
by smooth distributional Stokes proves, for EVERY such q,

    MA_ext_beta(q)(Y)=integral beta^2+2 integral q dd^c beta.

The same Haar averaging as above gives a genuine k w-psh q0~U on the first
curve, and this actual mass is 2 integral a(k w+dd^c q0). Therefore

    2k min a <= MA_ext_theta(v)(Y) <= 2k max a.

Both endpoints are approached by actual potentials of the exact type.
Choose smooth strictly positive curve measures zeta_j of mass k converging
to k delta_x, solve dd^c g_j=zeta_j-k w, and choose L_j so that
epsilon_(L_j) is below half the minimum density of zeta_j and
|integral U_(L_j) dd^c a|<1/j. Then

    v_j=bG+g_j+U_(L_j)

is a genuine theta-psh representative of r. Its residual mass tends to
2k a(x). Choosing x at either extremum of a proves the two exact invariant
values. This uses the full global lower and upper bounds first; it does not
replace the full optimization by a separated computation.

An equivalent affine formula records the polar subtraction explicitly:

    MA_ext_theta(v)(Y)
       =integral theta^2-2b a(p)+2 integral v dd^c theta.

Indeed integral G dd^c a=a(p)-integral a w, and q=v-bG in the preceding
formula. The differential background data enter through dd^c theta and the
divisorial restriction a(p); the extrema also require all type representatives.

## 4. An actual ambient intrinsic trace system

Take the smooth threefold Z=Y x P^1 and the smooth target
Y0=Y x {z0}. Put Theta=pr_Y^*theta+w3. The reference
u_Z=pr_Y^*(bG+U_L) is genuine Theta-psh for the chosen L. The ambient
background is strictly positive and genuinely nonclosed whenever a is
nonconstant. The generic Lelong number along Y0 is zero: away from
D x P^1 the reference is locally bounded. Its naive restriction to Y0
is a genuine function, but this is established for this example only.

Near the smooth ambient divisor D_Z=D x P^1, write t=-log|z1|^2. Up to
bounded constants the singularity is b log|z1|^2-t^alpha. For a real
weight s>0 and a holomorphic germ of transverse order j, radial integration
of |f|^2 exp(-s u_Z) is finite exactly when

    j+1>sb.

If j+1<sb, exponential power divergence proves failure. At j+1=sb the
remaining integral is comparable to integral^infinity exp(s t^alpha)dt
and also diverges. If j+1>sb, the sublinear exponent s t^alpha is bounded
by half the positive linear decay exponent for large t, proving integrability.
For a general germ, factor its largest power of z1. A leading coefficient
is nonzero on a positive-measure open set of tangential variables, giving
necessity by Fubini; local bounds on the remaining holomorphic factor give
sufficiency. Thus with the ORIGINAL no-extra-factor-2 convention,

    I(s u_Z)=O_Z(-floor(sb) D_Z),
    I(s u_Z) O_(Y0)=O_(Y0)(-floor(sb) D).

On EVERY smooth compact modification pi:Y'->Y0 and EVERY prime divisor E,
orders of this pulled-back principal ideal are
floor(sb) ord_E(pi^*D). Consequently the intrinsic orders in original S11 are

    tau_(Y0,u_Z)(E)=b ord_E(pi^*D).

They are finite and compatible on every further modification. This statement
concerns restrictions of AMBIENT multiplier ideals as in the task; it does
not assert that multiplier ideals commute with arbitrary pullback or replace
the trace definition by a naive Lelong-number rule.

The ordinary residual is genuinely unbounded and nonanalytic. At a generic
point of D an analytic singularity with divisorial coefficient b differs
from b log|z1|^2 by a bounded function. Our residual instead tends to minus
infinity like -t^alpha. Thus no analytic ordinary type is equivalent to r.
The residual has trivial multiplier ideals at every real weight, and for
alpha>=1/2 its separated closed first moment is infinite, by the exact S18
calculation. This construction is beyond bounded residuals.

## 5. Gauge, declared modifications and Gauduchon subtraction

A smooth gauge theta'=theta+dd^c f, r'=r-f and v'=v-f preserves actual
currents and non-pluripolar measures, hence both optimized data. Multiplier
ideals are unchanged because multiplication by exp(sf) is locally bounded
above and below; the intrinsic all-model trace orders are unchanged too.

For a proper smooth modification of Y use the PURE pullback background
and corresponding ordinary type. The complete canonical descent and
non-pluripolar pushforward proof in the existing S18 article gives a
bijection of the full competitor classes and equality of the two optimized
masses. The imposed trace is transported to the total transform of D.
Exceptional curvature subtraction changes the background and is not included.
For the explicitly declared point blowup, the existing local Schur-complement
argument supplies only a ONE-SIDED strict-current witness. Namely, take the
downstairs residual q=U_L with beta+dd^c q>=delta(w1+w2), and add
delta t ell_E to pi^*q, where dd^c ell_E=[E]-beta_E and t>0 is small.
Then

    pi^*beta+dd^c(pi^*q+delta t ell_E)
       >=delta(pi^*(w1+w2)-t beta_E)+delta t[E]>0.

The actual strict metric on the right is supplied by the old finite-chart
Schur-complement proof. The potential is at most pi^*q plus a finite constant;
its added exceptional pole need not preserve the mutual ordinary type.

There is an explicit failure of mutual preservation in this very family.
Blow up a point y outside D. The pulled-back reference pi^*r is bounded
on a neighborhood of E. Every potential v' ordinarily equivalent to it is
therefore locally bounded near E. If pi^*theta+dd^c v'>=epsilon h' held
for some Hermitian h'>0, its genuine restriction v'|E would be strictly
subharmonic on the compact curve E, because pi^*theta|E=0. Here is a local
justification retaining the genuine restriction and sharp-enough lower bound.
At each point of E choose a sufficiently small chart. The smooth form
epsilon h'-pi^*theta has a strictly positive coefficient on TE there.
Approximate its value at that point from below by a constant Hermitian form
with arbitrarily small scalar error, valid on the small chart by continuity.
Choose a quadratic with that constant complex Hessian. Subtracting this
quadratic from v' gives a genuine psh function. Its restriction to E is
genuine and finite, since v' is locally bounded. Adding back the quadratic
proves a strictly positive distributional curve Hessian on a neighborhood
of the point. Finitely many such neighborhoods give a positive lower bound
against any fixed smooth probability form on E. Global Stokes on E would
then give 0=integral_E dd^c(v'|E)>0, a contradiction.

Thus R_minus stays equal to the positive downstairs value after pure
pullback, and there is an actual one-sided strict witness, but no strict
current in the specified pulled-back mutual ordinary type. This is an
unbounded nonanalytic residual example with a genuinely nonclosed background,
not a use of positive top mass as a complete strict-type criterion.

For a strictly positive smooth m on the first curve with integral m w=1,
mu=m w1 w2, the residual background beta has the full all-test formula

    V_mu(beta)=2(c-b)/H, H=integral (m/a)w.

It is attained by the closed positive test ((g/a)w1+w2), where
g=V_mu(beta)m/(2a). The pointwise matrix lower bound and actual minimizing
test are the complete S18 proof, with c replaced by k=c-b. This value differs
in general from R_plus=2(c-b) max a. It depends on m whereas both R's do not.
For a fixed imposed coefficient b and a smooth positive segment
c_s=c-s d>b, a_s=a-s e>0, define beta_s=(c_s-b)w1+a_s w2. Then

    d sqrt(V_mu(beta_s))/ds
       =-integral (d w1+e w2) T_s / D_mu(T_s).

Its integrated quotient is the ACTUAL Gauduchon cost of the residual segment,
not a derivative of the upper singularity volume. The original background
theta_s has its different full-test volume 2c_s/H_s. Every denominator uses
all tests as specified in the original task. No arbitrary upstairs density
is equated with a degenerate pulled-back probability.

## Proof boundary

An explicit numerical instance is c=1, b=1/4, alpha=3/4, a=2+tau with
the standard spherical height tau, and m=1. Choose L=31: then
epsilon_L=(3/4)32^(-1/4)<3/8. The actual strict representative is
bG+U_31, its residual first moment is infinite, the full mass extrema
are R_minus=3/2 and R_plus=9/2, H=(log 3)/2, the residual all-test volume
is 3/log 3 and the original background volume is 4/log 3. The ambient
intrinsic orders are (1/4)ord_E(pi^*D) on every modification. A point
blowup outside D keeps these two positive optimized masses while excluding
mutual ordinary strict-current preservation.

The new S18 comparison and every application to u0, including the k<alpha
case, still require independent mathematical review. The precise external
foundations are BEGZ closed products and Theorem1.16 with small unbounded
locus, local bounded Bedford--Taylor products, Demailly's canonical removable
singularities and ordinary distributional Poincare--Lelong. This proof does
not assume a general Hermitian singularity mass invariance or an analytic
model for its unbounded residual.

The all-model trace data, the one-sided blowup bigness witness and mutual
ordinary strict-current witness downstairs are distinct assertions. Positive
R_minus supplies the explicit mutual witness only within this family. This
does not resolve the unrestricted original S11 programme or infer strict
currents from an arbitrary nonclosed restricted mass.


## Entire new unaccepted first-moment-free supporting proof

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


## All exact statement-only targets, not granted conclusions

# S11: proposed restricted targets, without proofs

Use the exact original definitions and dd^c=i partial barpartial/(2 pi).
All functions have their genuine canonical representatives. Let
Y=P^1 x P^1, with probability Fubini--Study forms w1,w2, a point p on
the first factor, D={p} x P^1, G_p<=0 with dd^c G_p=[p]-w and max G_p=0.
Fix c>0, b>=0, 0<alpha<1 and a smooth strictly positive first-factor
function a. Put theta=cw1+a w2 and U=1-(1-G_p)^alpha, pulled to Y.
The ordinary type [r] is [bG_p+U]; its admissibility must be proved.
No proof, draft article, private argument or prior result is supplied.
The unrestricted original S11 direction remains open.

## A. Exact type threshold and mutual strict-current witness

There exists a genuine theta-psh v~r if and only if b<c. In that range
there exists such a v with theta+dd^c v>=epsilon(w1+w2), epsilon>0,
in the MUTUAL ordinary type. The residual type is unbounded and nonanalytic.
For b>=c the specified unbounded ordinary type is empty; no numeric mass
infimum is assigned to an empty type. Prove this for all real b,alpha
in the declared ranges, including c-b<alpha.

## B. Exact optimization over the whole rough ordinary type

For b<c define R_minus and R_plus as the infimum and supremum of the
extended top mass over EVERY genuine theta-psh v~r, including rough
fiber-dependent competitors. Every mass is positive and finite, and

  MA_ext_theta(v)(Y)=integral theta^2-2b a(p)+2 integral v dd^c theta,
  R_minus=2(c-b) min a, R_plus=2(c-b) max a.

Both bounds are approached by actual potentials in that exact type.
Every canonical divisorial-removal, finite measure, closed comparison and
smooth-background passage must be justified. No nonclosed intersection
invariance or finite first-moment assumption is permitted.

## C. Genuine ambient embedding and every intrinsic ideal trace

There is an actual admissible representative r0~r on Y. Embed the target
Y0=Y x {z0} in Z=Y x P^1 and take Theta=pr_Y^*theta+w3 and
u_Z=pr_Y^*r0. The background is smooth strictly positive and nonclosed if
a is nonconstant. The generic Lelong number along Y0 is zero.
The reference can be chosen so that for every real s>0,

  I(s u_Z)=O_Z(-floor(sb)(D x P^1)),
  I(s u_Z) O_Y0=O_Y0(-floor(sb)D).

Consequently the task's intrinsic ambient-ideal traces are

  tau_(Y0,u_Z)(E)=b ord_E(pi^*D)

on EVERY prime divisor on EVERY smooth compact modification pi:Y'->Y0.
Prove the exact boundary integrability at integer sb with the original
|f|^2 exp(-su) convention. Do not replace restrictions of ambient ideals
by multiplier ideals of a pulled-back potential. The residual has trivial
ideals at every real weight but remains unbounded in its ordinary type.

## D. Actual infinite first moments within finite nonclosed mass types

For a suitably chosen admissible residual representative q0~U and a closed
K=C(w1+w2) dominating the residual background (c-b)w1+a w2, its actual
separated closed product has full mass. The first moment
integral_Y(-q0) MA_K(q0) is finite exactly for alpha<1/2 and is infinite
for 1/2<=alpha<1, with logarithmic divergence at alpha=1/2. Targets A--C
still hold throughout alpha in (0,1); neither finite energy nor a finite
first moment may be inserted as a hypothesis.

## E. Smooth gauges, pure pullback and failure of strict mutual type

Smooth gauges theta'=theta+dd^c f, r'=r-f, v'=v-f preserve actual
currents and extended measures, both R's and all intrinsic ideal traces.
For every proper modification pi:Y'->Y between smooth connected compact
complex manifolds, PURE pullback background and type give a canonical
bijection of competitor classes, the actual non-pluripolar pushforward
law, and equality of the two optimized masses. The trace system transports
to the total transform of D. Exceptional curvature subtraction is a
different operation and no equality across it is asserted.

For the declared point blowup at y outside D, the pulled-back lower mass
is still positive. There exists a genuine strict-current witness at most
pi^*r plus a constant, but NO strict-current witness ordinarily equivalent
to pi^*r. Prove both assertions for the actual background and canonical
restriction to the exceptional curve. The added exceptional singularity
of the one-sided witness is not claimed to have the original exact ideal
trace on that new divisor. No mutual strict-type preservation is asserted
on arbitrary modifications.

## F. Distinct all-test Gauduchon volume and actual subtraction

For m>0 smooth on P1 with integral mw=1 set mu=m w1w2, H=integral(m/a)w,
beta=(c-b)w1+a w2. Using ALL smooth positive dd^c-closed (1,1) tests,

  V_mu(beta)=2(c-b)/H,
  T=(g/a)w1+w2 attains the infimum, g=V_mu(beta)m/(2a).

The value can depend on m, whereas both R's do not. It generally differs
from R_plus; V_mu(theta)=2c/H is separate. For fixed imposed coefficient b
and fixed m, along c_s=c-sd>b, a_s=a-se>0, let beta_s=(c_s-b)w1+a_s w2.
For the actual minimizing T_s,

  d sqrt(V_mu(beta_s))/ds
    =-integral (d w1+e w2)T_s / D_mu(T_s).

Integration gives the actual residual subtraction cost on every compact
positive segment. Prove the lower bound for all tests and actual attainment;
an assumed PDE normalization or a chosen test subfamily is insufficient.
Do not equate this derivative with a derivative of R_plus or identify an
arbitrary strictly positive upstairs probability with a degenerate pullback.

## G. Nonvacuous genuinely nonclosed numerical instance

With c=1, b=1/4, alpha=3/4, a=2+tau and m=1, where tau is standard
spherical height with distribution d tau/2 on [-1,1], give an actual strict
ordinary-type representative and verify

  R_minus=3/2, R_plus=9/2,
  V_mu(beta)=3/log3, V_mu(theta)=4/log3,
  tau(E)=(1/4)ord_E(pi^*D).

The residual first moment is infinite. A point blowup outside D preserves
the positive mass values but excludes mutual ordinary strict-current type.
Its one-sided strict witness must still be actual. This does not prove a
strict-current criterion for arbitrary nonclosed restricted masses.

## Permitted exact foundational scope

Standard local bounded Bedford--Taylor products, their decreasing continuity,
non-pluripolar locality, canonical psh removable singularities across closed
pluripolar sets and distributional Poincare--Lelong are allowed foundations.
External applications must still be checked in their exact normalization.
On a compact Kähler manifold, cohomologous CLOSED positive currents with
small unbounded locus satisfy the ordinary-order comparison of their
non-pluripolar cohomology classes (BEGZ Theorem1.16, Acta Math.205(2010),
printed217--218). Small unbounded locus means local boundedness outside a
closed locally complete pluripolar set. This is allowed only with every
hypothesis proved, not for nonclosed currents or arbitrary unbounded loci.
The complete printed proof has been separately root-read. No source theorem
directly granting any target or prior mathematical verdict is supplied.



## Entire current known-overlap assessment

# S11: current known overlap and precise review boundary

Private scope assessment; no mathematical acceptance, original closure,
publication or priority claim. The proposed current six-page S11 article
must be assessed together with this note. Its original task stays exact.

The root read the entire current saved modules at author repository main
00a5044d04fa050adfc3969583c482fc78d092e2:

- book/author/section_resolved_trace_masses.tex;
- book/author/section_divisorial_normalization_stability.tex;
- book/author/section_divisorial_gauduchon_volume.tex;
- book/author/section_divisorial_residual_families.tex.

These are whole direct files. The Gauduchon file also names nested inputs;
this entry does not claim a fresh complete read of every nested input.

Known results and mechanisms must receive their existing credit:

1. Ordinary divisorial removal and the actual measure correspondence are
   already available for finite logarithmic types with bounded residuals;
   the general lower-Lelong divisorial subtraction is also known. Our local
   canonical removal with an unbounded sublogarithmic residual is an exact
   application/proof of that mechanism, not a newly discovered mechanism.
2. The closed bounded-residual restricted mass polynomial, pure resolution
   transport and one-sided strict-current implication are existing results.
   They do not themselves calculate our optimization over all rough ordinary
   representatives in a genuinely nonclosed background with unbounded residual.
3. The exceptional-curve obstruction to a strict current in bounded ordinary
   type is already an explicit book example. In the new example the global
   residual is unbounded and nonanalytic, but is bounded near the exceptional
   curve blown up away from D. The same known LOCAL obstruction applies.
   Do not credit its underlying Stokes argument as new.
4. The divisorial Gauduchon subtraction quotient, smooth positive residual
   variations, real-weight floor ideals and all-modification finite-divisor
   coefficients are known within their stated hypotheses. The new ambient
   intrinsic trace system must still be proved using restricted ambient ideals,
   with the sublogarithmic term and integer-weight boundary checked; no new
   general multiplier-ideal pullback theorem is asserted.
5. BEGZ's compact-Kähler closed mass comparison is a credited foundation.
   The proposed first-moment-free mass calculation uses it with a closed
   dominating K and small unbounded locus. It is not an extension of that
   source theorem to arbitrary nonclosed backgrounds.

The proposed construction to assess as a whole comprises an exact ordinary
admissibility/strict threshold b<c; two separately optimized finite positive
nonclosed masses for ALL rough fiber-dependent ordinary competitors; an
unbounded nonanalytic residual, including actual infinite first moments;
an actual ambient intrinsic all-model ideal trace; exact gauge and pure
pullback mass laws; a distinction between preserved positive lower mass,
one-sided bigness and failure of mutual strict-type preservation; and the
distinct all-test residual Gauduchon volume and subtraction derivative.

No claim of novelty or adequate original-task completion follows from writing
this construction. The full native review must assess mathematical correctness,
whether the construction supplies substantive progress beyond the declared
known cases, and any remaining scope gaps. Preserve the original S11 task
and all existing frozen material. The unrestricted direction remains open.


## Incoming author scope update, replacing the old current-view date only

# S11: incoming one-sided divisor threshold comparison

Private scope update only. Preserve the exact original S11 task, six-page
article, all previous arguments and their pending status. No new acceptance,
original closure, independent verification or priority claim is made.

At author repository head 3083ec715057e9875bd5c7256715bd417c5accd8 the root read
the entire current direct section_divisorial_normalization_stability.tex and
the entire new subsection_divisorial_type_thresholds.tex. The new subsection
was also read completely before the P18 release. Incoming author commits are
preserved; they are evidence of known scope, not new instructions.

The current author theorem identifies the maximal coefficient over all
one-sided logarithmic divisor classes with the residual metric coefficient,
including additional poles and infinite mass for L1 data. Smooth positive
data have attained ordinary and exact stretching-class coefficients. The
nonzero divisor gives strict loss, and the example fixes the standard FS
background. This is already known here and must receive its existing credit.
The current direct section adds its link and the corresponding model-reference
condition. The existing divisorial-removal mechanism and the use of a bounded
logarithmic residual are not to be credited as a new S11 mechanism.

The proposed S11 family has the fixed nonanalytic unbounded residual U_alpha
and optimizes two actual nonclosed mass endpoints over every rough ordinary
representative of bG+U_alpha, even when its first moment is infinite. Its
admissibility and mutual strict-current threshold b<c must be assessed in
that exact type. The all-model intrinsic ambient ideals, gauge laws, pure
pullback masses and distinct Gauduchon cost must still be proved. The familiar
blowup obstruction away from the singular fiber stays a credited local
obstruction. The new author subsection does not itself prove this entire
unbounded ordinary-type optimization or a general nonclosed restricted
invariant.

Supply both complete current direct files to the forthcoming full review,
alongside every previous argument and the earlier known-overlap assessment.
The three other directly assessed author modules are unchanged by incoming
commits. Nested inputs are not implicitly claimed to have been read. The
native reviewer must judge whether the exact proposed construction adds
substantive scoped progress beyond all of this known material.


## Entire current author module: section_divisorial_normalization_stability.tex

```latex
\section{Divisorial types and moving sections}\label{sec:divisorial-normalization-stability}

For a reference given by logarithms of holomorphic sections, removing its divisorial part identifies its ordinary singularity type with the bounded potentials of the residual background. The normalization scalar therefore depends only on the residual form, whereas convergence of the full potentials also requires control of the sections defining the divisors.

\Needspace{10\baselineskip}
In this section, $\theta$ is a smooth real $(1,1)$-form on $X$. Fix finitely many holomorphic line bundles $L_r$ on $X$ with smooth Hermitian metrics $h_r$, nonzero holomorphic sections $s_r$, and weights $t_r>0$. Put
\[
 \varphi=\sum_r t_r\log|s_r|_{h_r}^2,\qquad
 \Gamma=\sum_r t_r\operatorname{div}(s_r),\qquad
 \beta=\theta-\sum_r t_rc_1(L_r,h_r),
\]
where $c_1(L_r,h_r)$ is the Chern curvature form, and assume that the residual form $\beta$ is positive. The empty family is allowed, with $\varphi=0$ and $\beta=\theta$.

\begin{theorem}\label{thm:ordinary-divisor-normalization}
The ordinary singularity type of $\varphi$ is described by
\[
 \{u\in\PSH(X,\theta):u\sim\varphi\}
 =\{\varphi+w:w\in\PSH(X,\beta)\cap L^\infty(X)\},
\]
and for each such $w$,
\begin{equation}\label{eq:ordinary-divisor-measure}
 \mathrm{MA}^{\mathrm{ext}}_\theta(\varphi+w)=(\beta+\ddc w)^n.
\end{equation}
For every bounded measurable $F$, the equation \eqref{eq:relative-normalization} in this ordinary type has a unique constant and a solution unique modulo constants. Its normalization scalar $B_{\theta,[\varphi]}$ satisfies
\[
 B_{\theta,[\varphi]}(F)=B_\beta(F),
\]
so its dual functional and supporting sets coincide with $H_\beta$ and $\mathcal A_\beta$.
\end{theorem}
\begin{proof}
The Poincar\'e--Lelong formula gives $\theta+\ddc\varphi=[\Gamma]+\beta$, so every function on the right is $\theta$-plurisubharmonic and has the type of $\varphi$. Conversely, let $u\in\PSH(X,\theta)$ with $u\sim\varphi$. Then $u$ has the same generic Lelong numbers as $\varphi$ along the components of $\Gamma$, namely the coefficients of $\Gamma$, and \cref{lem:nonclosed-divisorial-removal} gives
\[
 \theta+\ddc u-[\Gamma]\geq0.
\]
The locally integrable difference $w=u-\varphi$ therefore has a $\beta$-plurisubharmonic representative. It is bounded off the divisor because $u\sim\varphi$, and the local submean property preserves both bounds across the divisor. Since $u$ and $\varphi+w$ agree almost everywhere, they are equal as quasi-plurisubharmonic functions.

Off the divisor, the currents $\theta+\ddc(\varphi+w)$ and $\beta+\ddc w$ agree, and locality identifies their Monge--Amp\`ere products there. The extended measure on the left gives the divisor zero mass, and so does the bounded product on the right, which is finite and charges no analytic set by \cref{sec:psh-bounded-products}. This proves \eqref{eq:ordinary-divisor-measure}. In the background $\beta$, the equation with bounded density has a continuous solution and a unique constant by \cref{thm:kn-continuous,prop:vanishing-exponent}. The density $\mathrm{e}^F$ is bounded above and below by positive constants, so \cref{cor:bounded-positive-density-uniqueness} gives uniqueness modulo constants. The correspondence transfers these assertions to the whole ordinary type and identifies the functionals.
\end{proof}

In particular, the comparison of backgrounds and the stability of supporting probabilities in \cref{thm:geometric-normalization-comparison,cor:geometric-adjoint-stability} apply whenever the positive residual forms satisfy the two-sided inequalities there; the location of the divisors does not enter these estimates. This statement concerns ordinary types. To interpret it in terms of model references, one also needs the envelope $P_\theta[\varphi]$ to differ from $\varphi$ by a bounded function. For a Hermitian $\theta$, \cref{lem:one-sided-divisor-correspondence} below proves this bounded difference and the smaller-background model condition.

For a fixed positive residual $\beta$, uniformly bounded $F_j\to F$ in $L^1$ give uniform convergence of the residual solutions normalized by $\sup_Xv_j=0$. Indeed, continuity of the scalar gives uniformly bounded densities $\mathrm{e}^{B_\beta(F_j)+F_j}$ converging in every $L^p$, $p<\infty$. The compactness theorem \cref{thm:lp-uniform-compactness} gives uniform convergence of subsequences, continuity of bounded products identifies the limiting equation, and \cref{cor:bounded-positive-density-uniqueness} identifies every limit. Subtracting the means gives the same conclusion for solutions normalized to have mean zero.

\begin{theorem}\label{thm:moving-divisorial-potential-stability}\index{Divisor!moving sections}
Keep the line bundles and metrics fixed. Let nonzero sections $s_{jr}$ converge to $s_r\ne0$ in the finite-dimensional spaces of global sections, and let positive weights satisfy $t_{jr}\to t_r>0$. Given Hermitian forms $\beta_j$, define $\varphi_j$ and $\theta_j=\beta_j+\sum_rt_{jr}c_1(L_r,h_r)$ by the preceding formulas. Suppose either that $\beta_j\to\beta$ in $C^\infty$ for a Hermitian form $\beta>0$ and $F_j\to F$ in $C^\infty$, or that $\beta_j=\beta$ for all $j$ and the tests $F_j$ converge to $F$ in $L^1$ with a common $L^\infty$ bound. Then $\varphi_j\to\varphi$ in $L^1$, and the solutions $u_j\sim\varphi_j$ for $(\theta_j,F_j)$, normalized by $\sup_Xu_j=0$, converge in $L^1$ to the similarly normalized solution $u\sim\varphi$. For the residual solutions $v_j$ normalized to have mean zero, one also has
\[
 \sup_X(\varphi_j+v_j)\longrightarrow\sup_X(\varphi+v).
\]
The residuals converge smoothly in the first regime and uniformly in the second.
\end{theorem}
\begin{proof}
The convergence of the residual solutions follows from \cref{prop:smooth-background-potential-stability} in the first case and from the preceding compactness argument in the second. The fixed metrics and bounded weights give a common smooth lower bound for $\ddc\varphi_j$. The convergent sections give a common upper bound for $\varphi_j$ and convergence at a point outside all limiting divisors, so the suprema of the $\varphi_j$ are bounded above and below. By \cref{thm:normalized-compactness}, every subsequence has a further subsequence converging in $L^1$. Off the limiting divisors, convergence of the sections and weights gives local uniform convergence to $\varphi$; since those divisors have zero volume, every $L^1$ cluster point equals $\varphi$. Thus $\varphi_j\to\varphi$ in $L^1(X)$.

Put $C_j=\sup_X(\varphi_j+v_j)$ and $C=\sup_X(\varphi+v)$. The sums converge in $L^1$ and have a common smooth lower bound for their complex Hessians, since $\ddc v_j\geq-\beta_j$ and the residual forms are uniformly bounded. Applying \cref{lem:qpsh-hartogs} at maximum points gives $\limsup_jC_j\leq C$. A maximum point of $\varphi+v$ lies off the poles of $\varphi$, and evaluation there, using local uniform convergence, gives $\liminf_jC_j\geq C$.

It follows that $u_j=\varphi_j+v_j-C_j\to\varphi+v-C=u$ in $L^1$. For an empty family of divisors, the assertion reduces to the convergence of the residual solutions and of their suprema.
\end{proof}

\input{author/subsection_divisorial_type_thresholds}

```


## Entire current author module: subsection_divisorial_type_thresholds.tex

```latex
\subsection{One-sided divisorial classes and sharp thresholds}
\label{subsec:divisorial-type-thresholds}

The ordinary-type correspondence extends to potentials with additional poles. It then identifies the largest subsolution coefficient in the whole one-sided class, even for merely integrable data. For smooth positive data, the prescribed divisor causes a strict loss relative to the global coefficient.

Keep the divisorial setting above, assume also that $\theta$ is a Hermitian form and $n\ge2$, and subtract a constant from $\varphi$ so that $\sup_X\varphi=0$. Write $S=\operatorname{Supp}\Gamma$ and $\psi=P_\theta[\varphi]$. For a nonempty class $\mathcal A\subset\PSH(X,\theta)$ and nonzero $0\le f\in L^1(\mathrm dV)$, define
\[
 b_{\theta,\mathcal A}(f)=\sup\{c\ge0:\text{some }u\in\mathcal A
          \text{ satisfies }\mathrm{MA}^{\mathrm{ext}}_\theta(u)
                                      \ge cf\,\mathrm dV\}.
\]
The three classes considered here are
\[
 \begin{aligned}
 \mathcal A_{\preceq}&=\{u\in\PSH(X,\theta):u\preceq\varphi\},\\
 \mathcal A_{\sim}&=\{u\in\PSH(X,\theta):u\sim\varphi\},\\
 \mathcal A_{\mathrm{env}}&=\mathcal E_{\mathrm{env}}(X,\theta,\psi).
 \end{aligned}
\]
The following lemma supplies the genuine reference $\psi$ used in the last definition.

\Needspace{12\baselineskip}
\begin{lemma}\label{lem:one-sided-divisor-correspondence}
The map $w\mapsto\varphi+w$ is a bijection from $\PSH(X,\beta)$ onto $\mathcal A_{\preceq}$, and
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(\varphi+w)
                         =\mathrm{MA}^{\mathrm{ext}}_\beta(w).
\]
Its bounded members correspond to $\mathcal A_{\sim}$. The envelope $\psi$ is genuine, satisfies $\varphi\le\psi\le\varphi+K$ for some finite $K$, meets the model condition \eqref{eq:als-model-condition}, and
\[
 \mathcal A_{\sim}\subset\mathcal A_{\mathrm{env}}
                         \subset\mathcal A_{\preceq}.
\]
\end{lemma}
\begin{proof}
If $u\preceq\varphi$, its generic Lelong numbers dominate the coefficients of $\Gamma$. By \cref{lem:nonclosed-divisorial-removal},
$\theta+\ddc u-[\Gamma]\ge0$. The locally integrable distribution $w=u-\varphi$ therefore has a canonical $\beta$-psh representative. Off $S$ it equals the difference and is bounded above. The identity $u=\varphi+w$ holds almost everywhere, hence everywhere for the canonical quasi-psh functions. Conversely, $w\in\PSH(X,\beta)$ has finite supremum, and
\[
 \theta+\ddc(\varphi+w)=\beta+\ddc w+[\Gamma]\ge0,
 \qquad \varphi+w\preceq\varphi.
\]
These maps are inverse. The bounded correspondence is \cref{thm:ordinary-divisor-normalization}. Off $S$ the currents agree; locality of the extended products identifies their measures there. Both measures give the analytic set $S$ zero mass by \cref{thm:arbitrary-extended-ma}, even when $w$ has additional poles or infinite mass. This proves the measure identity on $X$ without subtracting infinite pointwise values.

\Needspace{10\baselineskip}
For an envelope competitor $v\le0$ with $v\preceq\varphi$, the corresponding $w=v-\varphi$ satisfies $w\le-\varphi$ off $S$. Hence
\[
 \int_Xw^+\,\mathrm dV\le\int_X(-\varphi)\,\mathrm dV<\infty,
\]
uniformly in $v$. On a fixed finite cover by inner and outer coordinate balls, add smooth quadratic corrections making $w$ locally psh. Submean at a point attaining $\sup_Xw$, with uniform correction and volume-ratio bounds, gives
$\sup_Xw\le C_1\int_Xw^+\,\mathrm dV+C_2\le K$.
Thus $v\le\varphi+K$ canonically. The function $\varphi$ itself is a competitor, so the ordinary envelope construction gives a genuine $\theta$-psh function between $\varphi$ and $\varphi+K$. The upper bound survives upper regularization because $\varphi+K$ is upper semicontinuous. Ordinary equivalence gives $P_\theta[\psi]=P_\theta[\varphi]=\psi$. For $\varepsilon<1$ sufficiently close to one, $\beta-(1-\varepsilon)\theta>0$, so $\varphi$ is an $\varepsilon\theta$-psh competitor below $\psi$. Hence $P_{\varepsilon\theta}(\psi)$ is not identically $-\infty$, as required in \eqref{eq:als-model-condition}.

If $u\sim\varphi\sim\psi$, choose $K_u\ge0$ with $\psi-K_u\le u$. For each $t\ge1$, the $\theta$-psh function $a_t=\psi-tK_u$ obeys
\[
 t^{-1}a_t+(1-t^{-1})\psi=\psi-K_u\le u.
\]
This proves relative envelope-class membership in \cref{def:relative-envelope-class}, including the convention at $t=1$ and common poles. The other containment follows from its defining order $u\preceq\psi\sim\varphi$.
\end{proof}

\Needspace{12\baselineskip}
\begin{theorem}\label{thm:divisorial-type-thresholds}\index{Subsolution!prescribed divisorial threshold}
For every nonzero nonnegative $f\in L^1(\mathrm dV)$,
\[
 b_{\theta,\mathcal A_{\preceq}}(f)=b_\beta(f),
\]
and this coefficient is attained. If $f$ is smooth and strictly positive, then
\[
 b_{\theta,\mathcal A_{\sim}}(f)
 =b_{\theta,\mathcal A_{\mathrm{env}}}(f)
 =b_{\theta,\mathcal A_{\preceq}}(f)=c_\beta(f),
\]
with an exact finite equation attained in the ordinary type of $\varphi$. If also $\Gamma\ne0$, then
\[
 0<c_\beta(f)<c_\theta(f)=b_\theta(f).
\]
\end{theorem}
\begin{proof}
The correspondence lemma and \cref{thm:individual-density-subsolution} for the Hermitian form $\beta$ prove the first assertion, including attainment. This assertion allows additional poles and excess or infinite mass.
For smooth positive $f$, \cref{thm:tw-smooth} gives a smooth $w$ with $\beta+\ddc w>0$ and
$(\beta+\ddc w)^n=c_\beta(f)f\,\mathrm dV$.
The potential $\varphi+w$ belongs to the ordinary type and hence to all three classes. The class containments and the first assertion give equality of their coefficients; bounded-data normalization identifies $b_\beta(f)=c_\beta(f)$. The exact measure is finite.

It remains to prove strictness. Let $v$ be the smooth solution for $\theta$, and put
$\sigma=\theta+\ddc v$, $\eta=\beta+\ddc w$.
The one-sided subsolution gives $c_\beta(f)\le b_\theta(f)=c_\theta(f)$. If equality held, then on $X\setminus S$ the smooth function $a=\varphi+w-v$ would satisfy
\[
 \ddc a=\eta-\sigma,\qquad
 \ddc a\wedge Q=0,\qquad
 Q=\sum_{j=0}^{n-1}\eta^j\wedge\sigma^{n-1-j}.
\]
The form $Q$ is smooth and strictly positive, so it defines a real second-order operator $L$ with positive definite principal matrix and no zeroth-order term. Also $a\to-\infty$ near $S$, so its maximum is attained inside a component $U$ of $X\setminus S$. The strong maximum principle makes $a$ constant on $U$. To recall its local argument, put $z=\max_Ua-a\ge0$. If a positive region of $z$ had a boundary zero inside $U$, choose a ball in that region touching the zero set, with closure in a coordinate chart. On its outer half-annulus, the barrier
$e^{-A|x-y|^2}-e^{-AR^2}$ has strictly positive $L$ for large $A$. A sufficiently small multiple lies below $z$ on the two boundary spheres. A negative interior minimum of the difference would have nonnegative $L$, whereas its equation gives strictly negative $L$. Thus the comparison holds throughout the annulus and gives a positive inward derivative at the touching zero, contradicting $\nabla z=0$. Connectedness propagates the zero set to all of $U$.
The boundary of $U$ is nonempty and lies in $S$: otherwise $U$ would be both open and closed in connected $X$, although $S\ne\varnothing$. Constancy then contradicts $a\to-\infty$ at that boundary. This proves strictness; no semipositivity of the divisor's smooth curvature representative is required.
\end{proof}

\begin{corollary}\label{cor:critical-no-divisor}\index{Divisor!exclusion at the smooth threshold}
For smooth strictly positive $f$, no threshold subsolution has a nonzero divisorial component in $\theta+\ddc u$.
\end{corollary}
\begin{proof}
If such a component existed, retain a sufficiently small positive multiple $E$ of it. Choose a canonical logarithm $\ell_E$ and a smooth closed representative $\gamma_E$ with $[E]=\gamma_E+\ddc\ell_E$. The multiple can be chosen so that $\theta-\gamma_E>0$. Divisorial removal gives a canonical $(\theta-\gamma_E)$-psh representative of $u-\ell_E$, whose finite supremum implies $u\preceq\ell_E$. The preceding theorem would then give
\[
 b_\theta(f)\le c_{\theta-\gamma_E}(f)
                         <c_\theta(f)=b_\theta(f),
\]
a contradiction.
\end{proof}
The later rigidity result \cref{cor:smooth-dual-exact-equation} strengthens this obstruction by determining every smooth-data threshold subsolution through the maximizing Gauduchon form.

\Needspace{15\baselineskip}
\begin{example}\label{ex:projective-divisor-threshold-loss}
Let $(X_0,h_0)$ be a connected compact Hermitian $m$-fold, let $k\ge2$, and let $\kappa$ be the mass-one Fubini--Study form on $\mathbb P^k$. On $X_0\times\mathbb P^k$, choose a smooth positive volume form $\mathrm dV$. With pullbacks implicit, put
\[
 \begin{aligned}
 N&=m+k,& C&=\binom Nm,& V_0&=\int_{X_0}h_0^m,\\
 H&=h_0+\kappa,& \mu&=(h_0^m/V_0)\wedge\kappa^k,& R&=\mu/\mathrm dV.
 \end{aligned}
\]
For $D=\{Z_0=0\}$ pulled back to the product, take $E=\lambda D$, $0<\lambda<1$, with
\[
 \ell_E=\lambda\log\frac{|Z_0|^2}{\sum_{i=0}^k|Z_i|^2},
 \qquad H_E=h_0+(1-\lambda)\kappa.
\]
The global threshold of $R$ is $CV_0$, while its ordinary, relative envelope and one-sided thresholds prescribed by $E$ are all $CV_0(1-\lambda)^k$, attained by $\ell_E$. If $v_-(h_0)=0$, both $H$ and $H_E$ are nonclosed and have zero lower mass.
\end{example}
\begin{proof}
The Poincar\'e--Lelong formula gives $[D]=\kappa+\ddc(\ell_E/\lambda)$. Dimensions and the mass-one projective factor give
\[
 H^N=CV_0R\,\mathrm dV,\qquad
 H_E^N=CV_0(1-\lambda)^kR\,\mathrm dV.
\]
Thus the zero residual solves each smooth positive equation and fixes its unique scalar. The theorem identifies all three restricted coefficients, and the correspondence gives
$\mathrm{MA}^{\mathrm{ext}}_H(\ell_E)=H_E^N$.
Under the factor hypothesis, pullbacks of bounded $h_0$-psh potentials with mass tending to zero have masses multiplied respectively by $C$ and $C(1-\lambda)^k$. Bounded submersion pullback and the product expansion therefore give zero lower mass for both backgrounds. A closed positive $h_0$ would instead have every bounded mass equal to $V_0$ by Stokes, so both backgrounds are nonclosed.
\end{proof}

```


# Current incoming companion layout change, independently assessed

At eabd76d382a47a4fec8f89eb3f0545fb2a4dca99, section_resolved_trace_masses.tex differs from its complete earlier supplied and root-read proof only by a Needspace layout command before the bounded ordinary-type blowup obstruction. All mathematical statements and proofs of the five direct companion sections are unchanged. The exact latest whole section is included below for current overlap assessment; no incoming audit flag or former verifier verdict is a mathematical premise. The unrestricted original S11 programme remains open.

\section{Divisorial traces with bounded remainder}
\label{sec:resolved-trace-masses}

The invariant $\mathcal R(a;Y)$ is a supremum over all positive currents in a class. The trace of a given potential on $Y$, on the other hand, carries a specified singularity, and its non-pluripolar mass can be smaller. Suppose that on a resolution the trace becomes a divisorial logarithmic term plus a bounded remainder. The non-pluripolar product then ignores the divisor and sees only the residual current, which has bounded potentials. The class of this residual current is nef, and its top intersection number computes the mass.

We keep the assumption that $X$ belongs to class $\mathcal C$. Let $Y\subset X$ be an irreducible reduced subvariety of dimension $k>0$, let $\alpha_0$ be a smooth closed real $(1,1)$-form on $X$, and let $u\in\PSH(X,\alpha_0)$ be such that its pointwise restriction $v=u|_Y$ is not identically $-\infty$. On a K\"ahler resolution $\pi:Z\to Y$, with $f=j\circ\pi:Z\to X$ as in \cref{sec:finite-restricted-invariants}, put $\alpha_Z=f^*\alpha_0$ and $v_\pi=u\circ f$. When $Y$ is smooth, one may instead start from a smooth closed real $(1,1)$-form $\alpha_Y$ on $Y$ and $v\in\PSH(Y,\alpha_Y)$, and put $\alpha_Z=\pi^*\alpha_Y$ and $v_\pi=v\circ\pi$. In both cases $v_\pi$ is the composition of a given potential with a map; the intrinsic multiplier-ideal trace of \cref{chap:trace-data} is a different construction.

Suppose that on one such resolution
\begin{equation}\label{eq:resolved-trace-decomposition}
 v_\pi=\ell+w,
 \qquad \ell=\sum_{j=1}^N c_j\log|s_j|_{h_j}^2,
 \qquad w\text{ bounded},
\end{equation}
where $c_j>0$, the $D_j$ are prime divisors on $Z$, $s_j$ is the canonical section of $\mathcal O(D_j)$, and $h_j$ is a smooth Hermitian metric on $\mathcal O(D_j)$; the empty sum $\ell=0$ is allowed. Write $\Gamma=\sum_jc_jD_j$ and $\gamma_j=c_1(\mathcal O(D_j),h_j)$ for the curvature forms, and define the \emph{residual form} and the \emph{residual class}
\begin{equation}\label{eq:resolved-trace-residual-class}
 \eta_v=\alpha_Z-\sum_jc_j\gamma_j,
 \qquad b_v=\{\eta_v\}=\{\alpha_Z\}-\{[\Gamma]\}.
\end{equation}
For singular $Y$, all assertions below are made on its resolutions.

\begin{lemma}\label{lem:bounded-residual-mass-polynomial}\index{Residual class!mass on a resolution}
The current $R_v=\eta_v+\ddc w$ is positive and has bounded local potentials, and its class $b_v$ is nef. Moreover,
\begin{equation}\label{eq:resolved-trace-mass}
 \int_Z\langle(\alpha_Z+\ddc v_\pi)^k\rangle
       =\int_ZR_v^k
       =\int_Zb_v^k
       =\mathcal R_Z(b_v).
\end{equation}
\Needspace{7\baselineskip}
If $v_1,\ldots,v_k$ satisfy the same conditions on $Z$, possibly for different closed backgrounds, then
\begin{equation}\label{eq:resolved-trace-mixed-mass}
 \int_ZR_{v_1}\wedge\cdots\wedge R_{v_k}
       =\int_Zb_{v_1}\wedge\cdots\wedge b_{v_k}.
\end{equation}
\end{lemma}
\begin{proof}
Off the support $|\Gamma|$, we have $\ddc\ell=-\sum_jc_j\gamma_j$, so the current $\alpha_Z+\ddc v_\pi$ equals $\eta_v+\ddc w$ there and is positive. After the addition of a smooth local potential for $\eta_v$, the bounded function $w$ is plurisubharmonic off $|\Gamma|$. By \cref{lem:qpsh-removable-analytic}, it extends across the divisor as a bounded plurisubharmonic function that agrees almost everywhere with the original one; we use this extension to represent $w$. Thus $R_v\geq0$ on $Z$, and the Poincar\'e--Lelong formula gives
\[
 \alpha_Z+\ddc v_\pi=[\Gamma]+R_v.
\]
Since $w$ is bounded, $b_v$ is nef by \cref{lem:bounded-closed-potential-nef}. The non-pluripolar measure on the left of \eqref{eq:resolved-trace-mass} agrees with $R_v^k$ off the divisor, and neither measure charges the divisor. This gives the first equality.

Fix a K\"ahler form $\kappa$ on $Z$. For all sufficiently large real $t$, the smooth closed form $\eta_v+t\kappa$ is K\"ahler, and $w$ is a bounded potential for it. Therefore
\[
 \int_Z(R_v+t\kappa)^k=\int_Z(\eta_v+t\kappa)^k
\]
by \cref{thm:mass-invariance-characterization}, or by Stokes' theorem when $k=1$. Both sides are polynomials in $t$, so their constant coefficients agree; this gives $\int_ZR_v^k=\int_Zb_v^k$. The last equality in \eqref{eq:resolved-trace-mass} is \eqref{eq:nef-restricted-mass}. Applying the same polynomial argument to positive linear combinations of the $R_{v_i}$ and comparing coefficients gives \eqref{eq:resolved-trace-mixed-mass}.
\end{proof}

We denote the common value in \eqref{eq:resolved-trace-mass} by $\mathfrak r(v;Y)$ and call it the \emph{trace mass} of $v$ on $Y$.
When $Y$ is smooth, it is also the non-pluripolar mass of the trace current on $Y$ itself:
\[
 \mathfrak r(v;Y)=\int_Y\langle(\alpha_Y+\ddc v)^k\rangle,
\]
where $\alpha_Y=\alpha_0|_Y$ when $v$ is a restriction. Indeed, the currents on $Z$ and on $Y$ correspond on the locus where $\pi$ is an isomorphism, and their non-pluripolar measures give no mass to its analytic complement. A change of variables therefore identifies the total masses.

\begin{theorem}\label{thm:resolved-trace-invariance}\index{Restricted volume!resolution independence}
The number $\mathfrak r(v;Y)$ does not depend on the divisor metrics or on the K\"ahler resolution carrying \eqref{eq:resolved-trace-decomposition}. If two potentials in the same closed background have the same ordinary singularity type and each has a decomposition of the form \eqref{eq:resolved-trace-decomposition}, then their residual classes agree on a common refinement, and in particular their trace masses are equal. Residual classes add when the traces and their backgrounds are added, and their mixed masses are given by \eqref{eq:resolved-trace-mixed-mass}.
\end{theorem}
\begin{proof}
Changing a divisor metric changes $\ell$ by a smooth function, $w$ by its negative, and $\eta_v$ by the corresponding $\ddc$-term. Thus $R_v$ is unchanged. The same cancellation occurs when a smooth change of the background is accompanied by the opposite change of the potential.

Let $\rho:W\to Z$ be a modification with $W$ K\"ahler. Pulling back the decomposition, with the total divisor $\rho^*\Gamma$ including all exceptional coefficients, gives a decomposition on $W$ with bounded remainder $w\circ\rho$, residual current $\rho^*R_v$ and nef residual class $\rho^*b_v$. Its mass is
\[
 \int_W(\rho^*b_v)^k=\int_Zb_v^k.
\]
For two decompositions on different resolutions, pass to a common K\"ahler refinement and pull both back in this way. At a generic smooth point of a prime component of the union of the two divisors, the difference of the logarithmic terms is $(a_1-a_2)\log|t|^2+O(1)$, where $t$ is a local defining coordinate of the component and $a_1,a_2$ are its two coefficients. The two potentials have bounded difference, and the resulting pair of inequalities forces $a_1=a_2$. Hence the total divisors coincide, and so do the residual classes in the common background. Finally, adding two decompositions adds both the divisors and the bounded remainders. The residual class of the sum is therefore the sum of the nef residual classes, and \eqref{eq:resolved-trace-mixed-mass} computes its mixed terms.
\end{proof}

\begin{proposition}\label{prop:resolved-trace-strict-current}
Suppose that $\mathfrak r(v;Y)>0$. Then the class $\{\alpha_Z\}$ contains a K\"ahler current $\alpha_Z+\ddc p$ whose potential satisfies $p\leq v_\pi+A$ for some constant $A$. If $b_v$ has a smooth positive representative on a resolution carrying \eqref{eq:resolved-trace-decomposition}, then on that resolution $p$ can be chosen with $p\sim v_\pi$, that is, with $p-v_\pi$ bounded. When $Y$ is smooth, the K\"ahler current and the corresponding inequalities between potentials descend to $Y$.
\end{proposition}
\begin{proof}
Positive trace mass means $\int_Zb_v^k>0$. Since $b_v$ is nef, \eqref{eq:normalized-diagonal-current} gives a current $K=\eta_v+\ddc a\geq\delta\kappa$ in $b_v$, where $\kappa$ is a K\"ahler form and $\delta>0$. The current
\[
 [\Gamma]+K=\alpha_Z+\ddc(\ell+a)
\]
is then a K\"ahler current. Since $a$ is bounded above on $Z$ and $w$ is bounded below, its potential $p=\ell+a$ satisfies $p\leq\ell+w+A=v_\pi+A$ for a constant $A$. If $b_v$ has a smooth positive representative, $a$ can be chosen smooth, and then $p-v_\pi=a-w$ is bounded.

For smooth $Y$, take $\alpha_Y=\alpha_0|_Y$ when $v$ is a restriction. By \cref{prop:psh-descent-modification}, $p=q\circ\pi$ for some $q\in\PSH(Y,\alpha_Y)$. The current $\alpha_Y+\ddc q$ is strict by \eqref{eq:strict-current-pushforward}, and since $\pi$ is surjective, each inequality between potentials descends. The hypothesis of a smooth positive representative refers to the specified resolution: the pullback of a K\"ahler class under a further blowup need not be K\"ahler.
\end{proof}

The trace mass can vanish even when the restricted class is big, because the non-pluripolar product ignores the divisorial part of the trace.

\begin{example}\label{ex:divisorial-trace-zero-mass}
Let $k\geq1$, let $Y\simeq\mathbb P^k$ be a hyperplane in $X=\mathbb P^{k+1}$, and let another hyperplane $H_X\subset X$ cut out $H=H_X\cap Y$. Let $\omega_{\mathrm{FS}}$ be the Fubini--Study form, normalized by $\int_Y\omega_{\mathrm{FS}}^k=1$, and let $s_{H_X}$ be a section of $\mathcal O(1)$ defining $H_X$, measured with the Fubini--Study metric. For $c>0$ and $d\geq0$, take $\alpha_0=(c+d)\omega_{\mathrm{FS}}$ on $X$ and $u=c\log|s_{H_X}|^2$. The restriction $v=u|_Y$ is not identically $-\infty$, and
\[
 \alpha_0|_Y+\ddc v=c[H]+d\omega_{\mathrm{FS}}|_Y,
 \qquad \mathfrak r(v;Y)=d^k,
 \qquad \mathcal R(\{\alpha_0\};Y)=(c+d)^k.
\]
Thus for $d=0$ the trace mass is zero, although the restricted invariant is positive. The divisor $c[H]$ is a nonzero part of the trace current, but the non-pluripolar top product discards it.
\end{example}

The next example shows that the inequality $p\leq v_\pi+A$ in \cref{prop:resolved-trace-strict-current} cannot in general be improved to $p\sim v_\pi$, even for a bounded trace.

\Needspace{14\baselineskip}
\begin{example}\label{ex:positive-trace-bounded-type-obstruction}
Let $\mu:Y\to\mathbb P^2$ be the blowup of a point, with exceptional curve $E$, let $\omega_{\mathrm{FS}}$ be the Fubini--Study form on $\mathbb P^2$ with total volume one, and put $\alpha_Y=\mu^*\omega_{\mathrm{FS}}$ and $v=0$. The decomposition \eqref{eq:resolved-trace-decomposition} holds on $Z=Y$ with no divisor, the residual class $\{\alpha_Y\}$ is nef and big, and
\[
 \mathfrak r(0;Y)=\mathcal R(\{\alpha_Y\};Y)=1.
\]
Nevertheless, there is no bounded $q\in\PSH(Y,\alpha_Y)$ for which $\alpha_Y+\ddc q\geq\delta\kappa$ with $\delta>0$ and $\kappa$ K\"ahler. Indeed, since $q$ is bounded, its restriction to $E$ is defined, and the disk criterion of \cref{lem:smooth-disk-criterion} gives
\[
 \ddc(q|_E)\geq\delta\kappa|_E,
\]
because $\alpha_Y|_E=0$. Integration over the compact curve $E$ contradicts Stokes' theorem. Thus positive trace mass gives the one-sided comparison of \cref{prop:resolved-trace-strict-current}, but a K\"ahler current in the class may need additional singularities.
\end{example}

A subvariety contained in the null locus can nevertheless have positive restricted invariant; the union in \eqref{eq:finite-restricted-null-union} is needed to recover the locus.

\begin{example}\label{ex:positive-restriction-inside-null-locus}
Let $\mu:X\to\mathbb P^3$ be the blowup along a line $L$, and set $a=\mu^*\{\omega_{\mathrm{FS}}\}$, where $\omega_{\mathrm{FS}}$ has total volume one; the class $a$ is nef and $\int_Xa^3=1$. Since $N_{L/\mathbb P^3}\simeq\mathcal O(1)\oplus\mathcal O(1)$, the exceptional divisor is
$E=\mathbb P(N_{L/\mathbb P^3})\simeq\mathbb P^1\times\mathbb P^1$, and on $E$ the map $\mu$ is the projection to $L$. Hence $\int_Ea^2=0$, whereas a section $Y$ of $E\to L$ satisfies $\int_Ya=1$. Every irreducible subvariety not contained in $E$ has positive intersection number, because $\mu^*\omega_{\mathrm{FS}}$ is positive on its nonempty open part outside $E$. By \cref{cor:finite-restricted-null-union},
\[
 E_{\mathrm{nK}}(a)=E,
 \qquad \mathcal R(a;E)=0,
 \qquad \mathcal R(a;Y)=1.
\]
The union of the subvarieties with zero invariant is the whole null locus $E$, although the curve $Y\subset E$ has positive invariant. Positivity along one subvariety does not place it outside the null locus.
\end{example}
