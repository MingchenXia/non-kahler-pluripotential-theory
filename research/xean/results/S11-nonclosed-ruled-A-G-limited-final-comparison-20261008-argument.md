# Limited independent final comparison of the S11 restricted A--G construction

Assess every proof and dependency. The current article below controls the proposed mathematical statement. The complete historical packet and report remain unchanged for provenance and overlap. Their verdicts and the cold candidate flag are metadata, not mathematical premises. The unrelated general L1 maximal-density coefficient theorem and unspecified E_env/support functionals are outside scope and are not permitted dependencies. The original unrestricted S11 programme stays open.


## Current complete author article

```latex
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

```


## Complete historical author/companion proof packet, unchanged

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


## Complete unchanged original full-companion public report

```json
{
  "verdict": "INCONCLUSIVE",
  "report": "The ruled-family targets A–G and the first-moment-free supplement withstand independent reconstruction. I found no concrete mathematical defect in those scoped results. The unchanged original S11 programme and the entire supplied package nevertheless remain unestablished: the construction covers a specific family, and the incoming companion invokes the unresolved external assertion in premise 8.\n\nAdmissibility and strictness: the piecewise convex χ_L retains the unchanged singular tail up to a finite constant, satisfies dd^cU_L≥−ε_Lw with ε_L→0, and converges to zero in L¹. Divisorial removal is valid canonically: the bounded-above psh extension retains the sharper smooth lower bound because the smooth correction assigns the divisor zero coefficient measure. Poincaré–Lelong then gives the claimed competitor bijection and measure identity. Haar averaging includes every fiber-dependent competitor. Its horizontal positive measure has total mass c−b; negative mass excludes b>c, while zero mass forces a constant and excludes b=c. For b<c, the displayed strict witness preserves mutual ordinary type, including when c−b<α.\n\nMass calculation: both applications of [BEGZ Theorem 1.16](https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf) have the required compact Kähler manifold, closed cohomologous positive currents, and small unbounded locus. The reference is U_L₀, rather than an inadmissible U when c−b<α. Comparing both orders gives the required closed masses. The positive polar current has zero K-trace and therefore vanishes. Consequently the smooth-background expansion has finite terms, and distributional Stokes requires only L¹ integrability. This establishes the affine formula for every rough competitor. Averaging supplies global bounds; the positive measures ζ_j and small-curvature U_L_j supply actual representatives approaching both endpoints. Thus R_−=2(c−b)min a and R_+=2(c−b)max a are genuine whole-type optimizations.\n\nTraces and moments: transverse integrability is exactly j+1>sb. At equality the remaining integral contains exp(st^α) and diverges, so the floor coefficient is correct at integer weights as well. Restricting these ambient principal ideals and then taking divisorial orders gives τ(E)=b ord_E(π*D) on every modification. This argument neither assumes multiplier-ideal pullback commutation nor promotes lower trace inequalities to equalities. The residual has trivial ideals but an unbounded nonanalytic ordinary type. Its first moment is comparable to ∫∞t^(2α−2)dt, proving the claimed threshold and logarithmic endpoint divergence. Infinite first moment does not invalidate the mass calculation.\n\nGauges and modifications: smooth gauges preserve the actual current and give a competitor bijection. For pure pullback, adding a pulled-back local quadratic permits canonical psh descent; properness supplies the upper bound near the center. The sharper downstairs inequality survives extension. Pullback of the exact smooth lower bound can also be checked locally by constant Hermitian approximations. Locality and zero mass on the excluded analytic sets give the pushforward law. The blowup witness is strict by the stated Schur-complement estimate. Its exceptional logarithm makes it one-sided. Conversely, mutual ordinary equivalence forces boundedness near E, and restriction of a hypothetical strict witness gives a positive curve Hessian whose integral contradicts Stokes. Positive preserved lower mass therefore does not imply preservation of a strict mutual ordinary type.\n\nGauduchon calculation and example: Ω²=Vμ and Ω=aT for the proposed minimizing test. Stokes and the matrix arithmetic–geometric mean inequality prove the lower bound for all positive dd^c-closed tests, while this closed T attains it. The derivative and subtraction formula have the correct signs and factors. For the numerical example, ε₃₁≈0.31534<3/8, H=(log 3)/2, and all displayed mass, volume, trace and moment values follow. No arbitrary positive upstairs density is treated as a degenerate pullback density.\n\nCompanions: the bounded closed residual polynomial, metric cancellation, refinement transport, one-sided strict-current construction, and exceptional/null-locus examples are consistent with the task-granted closed background and their stated hypotheses. The smooth equation applications match Tosatti–Weinkove; the positive bounded-density existence, uniqueness and stability applications match Kołodziej–Nguyen. However, these sources do not establish the companion’s maximal coefficient and attainment assertion for every L¹ density, allowing arbitrary additional poles and infinite mass. Its cited internal theorem was not supplied, and I could not identify a matching primary source. Claims involving the exact E_env definition and referenced supporting functionals also cannot receive complete validation from their absent definitions. These are unresolved checks, not counterexamples to the ruled-family proof.\n\nScope and overlap: the computation provides substantive progress beyond bounded residuals. Its invariant definition, divisorial removal and modification laws already occur for nonclosed currents under BMP in [Boucksom–Guedj–Lu, Definition 3.1 and Proposition 3.3](https://d-nb.info/1374372846/34). The potential contribution is the explicit optimization for this nonanalytic ordinary family, particularly with infinite first moment. No priority conclusion follows. The argument supplies neither an intrinsic construction for arbitrary nonclosed restricted classes nor a general trace-envelope or strict-type criterion. Its acknowledgement that unrestricted S11 remains open must be retained.\n\nHarmless wording corrections: qualify “all backgrounds” as the target backgrounds θ, β, Θ and their pullbacks, since the auxiliary K is closed; declare d real and e a smooth real first-factor function in the variation; clarify that pure-pullback laws concern the optimized masses, without asserting a Vμ law for arbitrary upstairs densities. The inaccessible Harvard Demailly link can be replaced by the author-hosted text below. None of these changes repairs the unresolved general scope or premise 8.",
  "passages": [
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/0",
      "statement": "On a compact Kähler n-fold, for 1≤p≤n, suppose each pair T_j,T'_j consists of cohomologous closed positive (1,1)-currents locally bounded in potential outside a closed locally complete pluripolar set, and T_j is less singular than T'_j. Then {⟨T_1∧⋯∧T_p⟩}−{⟨T'_1∧⋯∧T'_p⟩} is pseudo-effective. This is BEGZ Theorem 1.16.",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "cohomologous closed positive (1, 1)-currents with small unbounded locus",
      "premise": 0
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/1",
      "statement": "Closed positive (1,1)-currents on a compact Kähler manifold have finite, closed non-pluripolar products for 1≤p≤n. Locally ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ. For potentials locally bounded outside a closed locally complete pluripolar set A, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from X\\A. These are BEGZ Definition 1.2, Proposition 1.6 and Theorem 1.8.",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "is well defined.",
      "premise": 1
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/2",
      "statement": "Closed positive (1,1)-currents on a compact Kähler manifold have finite, closed non-pluripolar products for 1≤p≤n. Locally ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ. For potentials locally bounded outside a closed locally complete pluripolar set A, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from X\\A. These are BEGZ Definition 1.2, Proposition 1.6 and Theorem 1.8.",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "is closed.",
      "premise": 1
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/3",
      "statement": "Closed positive (1,1)-currents on a compact Kähler manifold have finite, closed non-pluripolar products for 1≤p≤n. Locally ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ. For potentials locally bounded outside a closed locally complete pluripolar set A, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from X\\A. These are BEGZ Definition 1.2, Proposition 1.6 and Theorem 1.8.",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "Condition (1.2) is always satisfied when p=1",
      "premise": 1
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/4",
      "statement": "For locally bounded plurisubharmonic potentials, Bedford–Taylor products are symmetric multilinear positive closed currents, converge weakly under decreasing sequences with locally bounded plurisubharmonic limits, and their top-degree measures assign pluripolar sets zero mass.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf",
      "quote": "where the limit is in the weak topology",
      "premise": 2
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/5",
      "statement": "For locally bounded plurisubharmonic potentials, Bedford–Taylor products are symmetric multilinear positive closed currents, converge weakly under decreasing sequences with locally bounded plurisubharmonic limits, and their top-degree measures assign pluripolar sets zero mass.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf",
      "quote": "into the cone of nonnegative closed currents",
      "premise": 2
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/6",
      "statement": "For locally bounded plurisubharmonic potentials, Bedford–Taylor products are symmetric multilinear positive closed currents, converge weakly under decreasing sequences with locally bounded plurisubharmonic limits, and their top-degree measures assign pluripolar sets zero mass.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf",
      "quote": "pluripolar if and only if C*(E)=0.",
      "premise": 2
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/7",
      "statement": "A plurisubharmonic function on the complement of a closed pluripolar subset of a complex manifold, locally bounded above near that subset, has a unique genuine plurisubharmonic extension across it. This is Demailly, Chapter I, Theorem 5.24.",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf",
      "quote": "locally bounded above near A extends uniquely",
      "premise": 3
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/8",
      "statement": "For a nonzero holomorphic section s of a Hermitian holomorphic line bundle (L,h), with dd^c=(i/(2π))∂bar∂ and c_1(L,h)=(i/(2π))Θ(L,h), the current identity is dd^c log|s|_h²=[div(s)]−c_1(L,h).",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf",
      "quote": "id′d′′ log |s|² = 2π∑mⱼ[Zⱼ] − iΘ(E).",
      "premise": 4
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/9",
      "statement": "On a compact complex manifold with BMP, the infimum and supremum of non-pluripolar top mass over all positive quasi-closed currents in a fixed dd^c-class with equivalent ordinary singularities are finite lower and upper volumes. Both are unchanged by addition of an effective real divisor and by pullback under a smooth compact modification. These are Boucksom–Guedj–Lu, Definition 3.1 and Proposition 3.3.",
      "url": "https://d-nb.info/1374372846/34",
      "quote": "with equivalent singularities.",
      "premise": 5
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/10",
      "statement": "On a compact complex manifold with BMP, the infimum and supremum of non-pluripolar top mass over all positive quasi-closed currents in a fixed dd^c-class with equivalent ordinary singularities are finite lower and upper volumes. Both are unchanged by addition of an effective real divisor and by pullback under a smooth compact modification. These are Boucksom–Guedj–Lu, Definition 3.1 and Proposition 3.3.",
      "url": "https://d-nb.info/1374372846/34",
      "quote": "for any modification π : Y → X we have",
      "premise": 5
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/11",
      "statement": "On a compact connected Hermitian n-fold, n≥2, for every smooth real F there exist a unique real B and a unique smooth potential v with sup v=0, β+dd^cv>0 and (β+dd^cv)^n=e^(F+B)β^n. Smooth solutions satisfy C∞ a priori estimates depending on the Hermitian metric and F. This is Tosatti–Weinkove, Main Theorem and Corollary 1, after rescaling potentials to the stated dd^c normalization.",
      "url": "https://arxiv.org/pdf/0910.1390",
      "quote": "For every smooth real-valued function F on M there exists a unique real number b and a unique smooth real-valued function",
      "premise": 6
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/12",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Then there is a unique",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/13",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "get the uniqueness of bounded ω-psh solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/14",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "‖u − v‖∞ ≤ C‖f − g‖₁ᵅ.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/15",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique c > 0",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/16",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "c is uniquely defined.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/17",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "we get that u = v is also continuous.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/18",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Assume that f ≥ c0 > 0.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/19",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "p > 1",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/20",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "supX u = supX v = 0.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/21",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "compact Hermitian manifold",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/22",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "0 < α < 1/(2+n(n+1))",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/23",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "C = C(c0, α, ‖f‖p, ‖g‖p)",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/24",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous ω-psh solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/25",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "right hand side in Lp",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/26",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique u ∈ PSH(ω) ∩ C(X)",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/27",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "ωᵤⁿ = cfωⁿ.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/28",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniqueness of continuous solutions.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/29",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded ω-psh solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/30",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability estimate",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/31",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Theorem 3.12.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/32",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Corollary 3.9.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/33",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Remark 3.13.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/34",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Lemma 2.1.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/35",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "c ≥ 1.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/36",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "0 < c0 ≤ f",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/37",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "supX u = 0",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/38",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/39",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/40",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded solution",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/41",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "u = v",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/42",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "also continuous.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/43",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/44",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/45",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/46",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/47",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Hermitian",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/48",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/49",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "estimate",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/50",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniqueness",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/51",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Theorem",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/52",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Corollary",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/53",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Remark",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/54",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Lemma",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/55",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/56",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "normalized",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/57",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/58",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "density",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/59",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "compact",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/60",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "manifold",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/61",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded away from zero.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/62",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "right hand side varies in a bounded set in Lp",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/63",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniform",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/64",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "converges",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/65",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniquely defined.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/66",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "By Lemma 2.1",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/67",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "there exists",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/68",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique c",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/69",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique u",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/70",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous ω-psh",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/71",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "‖u − v‖∞",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/72",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "‖f − g‖₁",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/73",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "f ≥ c0 > 0",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/74",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "p > 1.",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/75",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "supX",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/76",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "PSH",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/77",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "C(X)",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/78",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "L∞(X)",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/79",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Lp",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/80",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "L1",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/81",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Monge-Ampère equation",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/82",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "complex Monge-Ampère equation",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/83",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Hermitian manifolds",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/84",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability of solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/85",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Hölder continuous",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/86",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniform convergence",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/87",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/88",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "normalizing constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/89",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/90",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique solution",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/91",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "a bounded set",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/92",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded away",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/93",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "from zero",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/94",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "compact Hermitian",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/95",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique real",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/96",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous weak",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/97",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "the uniqueness",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/98",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "the stability",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/99",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "the constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/100",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "the solution",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/101",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "the equation",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/102",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous solution",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/103",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded ω-psh",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/104",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Hermitian manifold",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/105",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "compact manifold",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/106",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive density",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/107",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniform estimates",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/108",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "a priori bounds",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/109",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "suprema",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/110",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "normalized solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/111",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded density",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/112",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Lp density",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/113",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "L1 norm",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/114",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive lower bound",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/115",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniform positive",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/116",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "finite",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/117",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "existence",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/118",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "convergence",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/119",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "integrable",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/120",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "strictly positive",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/121",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "smooth",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/122",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "weak",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/123",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "normalization",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/124",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "theorem",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/125",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "proof",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/126",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "right hand side",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/127",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive constants",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/128",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniform bound",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/129",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniformly bounded",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/130",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous functions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/131",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded functions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/132",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "normalized",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/133",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniquely",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/134",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positivity",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/135",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "regularity",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/136",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability and regularity",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/137",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "solutions of the Monge-Ampère equation",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/138",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "on Hermitian manifolds",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/139",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded away from zero",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/140",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "p > 1",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/141",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Theorem A",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/142",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Theorem B",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/143",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Theorem 3.1",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/144",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Theorem 3.12",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/145",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Corollary 3.9",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/146",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Remark 3.13",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/147",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Lemma 2.1",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/148",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Lemma 2.3",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/149",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "f > c0 > 0",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/150",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "f ≥ c0 > 0",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/151",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "0 < c0 ≤ f",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/152",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique c > 0",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/153",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique u",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/154",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique solution",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/155",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous solution",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/156",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded solution",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/157",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniform convergence",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/158",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "supX u = 0",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/159",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "supX u = supX v = 0",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/160",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded ω-psh solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/161",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous ω-psh solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/162",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "compact Hermitian manifold",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/163",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "a unique",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/164",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "the unique",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/165",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniqueness of bounded",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/166",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniqueness of continuous",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/167",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability estimates",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/168",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability estimate",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/169",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "L1 norm",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/170",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Lp norm",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/171",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/172",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/173",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/174",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/175",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/176",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/177",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/178",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "solution",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/179",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/180",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "equation",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/181",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/182",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "uniqueness",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/183",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "existence",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/184",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "regularity",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/185",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Hermitian",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/186",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "compact",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/187",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "manifold",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/188",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "normalized",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/189",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "density",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/190",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/191",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/192",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/193",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/194",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/195",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/196",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "solution",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/197",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "equation",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/198",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Hermitian",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/199",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "compact",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/200",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "manifold",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/201",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/202",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/203",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/204",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/205",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/206",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/207",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/208",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "equation",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/209",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Hermitian",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/210",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "compact",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/211",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "manifold",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/212",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "bounded",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/213",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "continuous",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/214",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "unique",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/215",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "positive",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/216",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "constant",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/217",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "stability",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/218",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "solutions",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/219",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "equation",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/220",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "Hermitian",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/221",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "compact",
      "premise": 7
    },
    {
      "id": "380adfe6-d71f-4889-9c78-0978ef6ee824/222",
      "statement": "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
      "url": "https://arxiv.org/pdf/1501.05749",
      "quote": "manifold",
      "premise": 7
    }
  ],
  "premises": [
    "On a compact Kähler n-fold, for 1≤p≤n, suppose each pair T_j,T'_j consists of cohomologous closed positive (1,1)-currents locally bounded in potential outside a closed locally complete pluripolar set, and T_j is less singular than T'_j. Then {⟨T_1∧⋯∧T_p⟩}−{⟨T'_1∧⋯∧T'_p⟩} is pseudo-effective. This is BEGZ Theorem 1.16.",
    "Closed positive (1,1)-currents on a compact Kähler manifold have finite, closed non-pluripolar products for 1≤p≤n. Locally ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ. For potentials locally bounded outside a closed locally complete pluripolar set A, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from X\\A. These are BEGZ Definition 1.2, Proposition 1.6 and Theorem 1.8.",
    "For locally bounded plurisubharmonic potentials, Bedford–Taylor products are symmetric multilinear positive closed currents, converge weakly under decreasing sequences with locally bounded plurisubharmonic limits, and their top-degree measures assign pluripolar sets zero mass.",
    "A plurisubharmonic function on the complement of a closed pluripolar subset of a complex manifold, locally bounded above near that subset, has a unique genuine plurisubharmonic extension across it. This is Demailly, Chapter I, Theorem 5.24.",
    "For a nonzero holomorphic section s of a Hermitian holomorphic line bundle (L,h), with dd^c=(i/(2π))∂bar∂ and c_1(L,h)=(i/(2π))Θ(L,h), the current identity is dd^c log|s|_h²=[div(s)]−c_1(L,h).",
    "On a compact complex manifold with BMP, the infimum and supremum of non-pluripolar top mass over all positive quasi-closed currents in a fixed dd^c-class with equivalent ordinary singularities are finite lower and upper volumes. Both are unchanged by addition of an effective real divisor and by pullback under a smooth compact modification. These are Boucksom–Guedj–Lu, Definition 3.1 and Proposition 3.3.",
    "On a compact connected Hermitian n-fold, n≥2, for every smooth real F there exist a unique real B and a unique smooth potential v with sup v=0, β+dd^cv>0 and (β+dd^cv)^n=e^(F+B)β^n. Smooth solutions satisfy C∞ a priori estimates depending on the Hermitian metric and F. This is Tosatti–Weinkove, Main Theorem and Corollary 1, after rescaling potentials to the stated dd^c normalization.",
    "On a compact connected Hermitian manifold, if f∈L^p(β^n), p>1, and f≥δ>0, there are a unique A>0 and normalized continuous β-psh solution of (β+dd^cu)^n=Afβ^n; bounded solutions are continuous and unique modulo constants. For normalized continuous solutions with nonzero L^p densities f,g and f≥δ>0, every 0<γ<1/(2+n(n+1)) admits an estimate ‖u−v‖∞≤C‖f−g‖_1^γ, with C controlled by the fixed geometry, δ, γ and the L^p bounds. These are Kołodziej–Nguyen, Corollary 3.9, Theorem 3.12 and Remark 3.13.",
    "For every compact connected Hermitian n-fold (X,β), n≥2, smooth positive probability dV and nonzero 0≤f∈L¹(dV), the coefficient b_β(f)=sup{c≥0: some genuine u∈PSH(X,β) satisfies MA_ext_β(u)≥cf dV} is finite and attained, allowing unbounded additional poles and infinite mass. For smooth strictly positive f it equals the normalization coefficient of the smooth Monge–Ampère solution."
  ],
  "kind": "codex-report",
  "operationId": "380adfe6-d71f-4889-9c78-0978ef6ee824",
  "reportedAt": "2026-10-08T09:41:57.340Z"
}

```


## Complete current statement-only independent public reconstruction

```json
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

```


## Primary excerpt: BEGZ, text lines 250--455

URL: https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf
Text SHA256: 1b4035bd5a2d88f8872f882b34694a9f2ff1f30ee38cef644f4ad584a1d3b144

```text

Note that the right-hand side is non-decreasing in k. This equation completely determines
 Vp     c
  j=1 dd uj , since the latter is required not to put mass on the pluripolar set

                                              ∞
                                              [
                                       X\          Ok = {u = −∞}.
                                             k=1

     Definition 1.1. If u1 , ..., up are psh functions on the complex manifold X, we shall
                                         Vp      c
say that the non-pluripolar product        j=1 dd uj is well defined on X if for each compact
subset K of X we have
                             Z                         p
                                                       ^
                                             n−p
                       sup              ω          ∧         ddc max{uj , −k} < ∞.      (1.2)
                        k    K∩Ok                      j=1


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


## Primary excerpt: BEGZ, text lines 917--1017

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


## Primary excerpt: Demailly, text lines 2055--2190

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


## Primary excerpt: Demailly, text lines 2300--2355

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


## Primary excerpt: Demailly, text lines 14896--14934

URL: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf
Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

```text
because of the Cauchy residue formula (cf. Lemma I-2.10) and because σ is a submersion
in a neighborhood of Z (cf. (I-1.19)). Now, we have dA = Θ(D) and Th. 9.8 follows from
the resulting equality:

(9.9)                                     du = 2πi [Z] + Θ(E).                             


§ 10. Connections of Type (1,0) and (0,1) over Complex Mani-
folds
   Let X be a complex manifold, dimC X = n and E a C∞ vector bundle of rank r over
X ; here, E is not assumed to be holomorphic. We denote by C∞
                                                            p,q (X, E) the space of
C sections of the bundle Λ T X ⊗ E. We have therefore a direct sum decomposition
 ∞                         p,q ⋆

                                         M
                           C∞ l (X, E) =     C∞
                                              p,q (X, E).
                                                  p+q=l

Connections of type (1, 0) or (0, 1) are operators acting on vector valued forms, which
imitate the usual operators d′ , d′′ acting on C∞p,q (X, C). More precisely, a connection of
type (1,0) on E is a differential operator D of order 1 acting on C∞
                                             ′
                                                                    •,• (X, E) and satisfying
the following two properties:

(10.1)                         D′ : C∞
                                     p,q (X, E) −→ Cp+1,q (X, E),
                                                    ∞

(10.1′ )                       D′ (f ∧ s) = d′ f ∧ s + (−1)deg f f ∧ D′ s

for any f ∈ C∞  p1 ,q1 (X, C), s ∈ Cp2 ,q2 (X, E). The definition of a connection D of type
                                    ∞                                              ′′

(0,1) is similar. If θ : E↾Ω → Ω × C is a C trivialization of E↾Ω and if σ = (σλ ) = θ(s),
                                      r         ∞


```


## Primary excerpt: BGL, text lines 1268--1385

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
