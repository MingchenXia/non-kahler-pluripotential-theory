# Whole proposed scoped targets

# Proposed S02 rotational-sector conclusions; all require proof

Keep every convention and measure/capacity definition of original S02.
Let R be the ENTIRE class of normalized genuine omega-psh potentials on the
standard scalar Hopf threefold invariant under (z0,z')->(z0,A z'), A in U(2).
Include bounded and unbounded potentials. No reduction of arbitrary potentials
to R is granted. W is positive C1, nonincreasing and tends to zero. Put
Q(W)=sup_(t>=0)(1+sqrt(2t))W(t) and
Q_T(W)=sup_(t>=T)(1+sqrt(2t))W(t).

A. Every individual nu_W,u for u in R is finite if and only if
sup_(t large) sqrt(t)W(t)<infinity. The same condition is equivalent to
a uniform total-mass bound on R. Prove the actual quantitative upper bound
sup_R nu_W,u(X)<=12 Q(W). If the condition fails, construct ONE actual
genuine normalized invariant potential with infinite weighted measure;
unbounded masses of a sequence alone do not establish this conclusion.

B. Uniform tails on R hold exactly when sqrt(t)W(t)->0. Prove for every
actual bounded or unbounded u in R and every T>=0 the bound
nu_W,u({-u>T})<=12 Q_T(W), with extended interpretation if the bound is
infinite. When the limiting condition fails, give actual admissible
potentials and actual deep-set mass that prevents uniform tail decay.

C. Uniform absolute continuity relative to the ORIGINAL Cap_omega holds
on R exactly when sqrt(t)W(t)->0. Prove the quantitative bound, for every
Borel A and T>=0,
nu_W,u(A)<=W(0)(1+T)^3 Cap_omega(A)+12 Q_T(W).
Construct actual small-capacity sets carrying uniformly positive weighted
mass whenever limsup sqrt(t)W(t)>0; unrelated measures are not a substitute.

D. The map from all of R into finite measures is continuous from original
capacity convergence to weak convergence exactly when sqrt(t)W(t)->0.
When sqrt(t)W(t) is bounded but does not tend to zero, construct an ACTUAL
smooth normalized invariant sequence u_j converging in original capacity
to an ACTUAL genuine normalized invariant g, for which weighted measures
have a finite weak cluster carrying positive mass on an analytic pole
divisor of g while nu_W,g has zero mass there. Prove every product and
capacity limit, including bounded-truncation mass on depth level sets.
When sqrt(t)W(t) is unbounded, A already obstructs a map into finite
measures on all R; do not relabel this as a finite weak-limit example.

E. For eventually decreasing weights (1+t)^(-p)log(e+t)^(-a) tending to
zero, modified smoothly on a compact interval if needed, individual
finiteness and uniform total bounds hold on R exactly for p>1/2 or
p=1/2,a>=0; tails, capacity absolute continuity and capacity-to-weak
continuity hold exactly for p>1/2 or p=1/2,a>0. All necessary obstructions
also apply to the unrestricted original class, but the sufficient
conclusions above are for R ONLY. Original S02 remains incomplete.

Independently reconstruct all A--E and their entire dependency chain,
verifying exact indispensable primary hypotheses, global positivity,
canonical normalization and pole values, actual measures and every limit.
No author proof, prior report or source-application judgment is supplied.
These are proposed theorem conclusions rather than granted lemmas.


## Whole current twelve-page article

\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\ddc}{\mathrm{d}\mathrm{d}^{\mathrm c}}
\newcommand{\dc}{\mathrm{d}^{\mathrm c}}
\newcommand{\C}{\mathbb C}
\newcommand{\R}{\mathbb R}
\newcommand{\Pp}{\mathbb P}
\newcommand{\FS}{\mathrm{FS}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\negpart}[1]{[#1]_-}
\title{Sharp damping thresholds for rotationally invariant\newline
potentials on a Hopf threefold}
\author{Research manuscript}
\date{October 7, 2026}
\begin{document}
\maketitle
\begin{center}
\small Working draft. Mathematical review and independent reconstruction pending.
\end{center}
\begin{abstract}
On the standard Hopf threefold we determine the damping thresholds in the
full class of normalized potentials invariant under the unitary rotations
of the last two coordinates. Every individual weighted non-pluripolar
measure is finite exactly when $\sqrt t\,W(t)$ is bounded; this also gives
a uniform mass bound. Uniform tails, uniform capacity absolute continuity
and capacity-to-weak continuity instead require $\sqrt t\,W(t)\to0$.
An exact positive fiber flux and a pointwise semiconvex depth estimate prove
sufficiency for all bounded and unbounded potentials in this class. A
faster-scale heat construction gives the necessary conditions, a single
infinite measure, and an actual capacity-convergent sequence whose weighted
measures charge a pole divisor in the limit at the critical regime.
The unrestricted damping problem remains open.
\end{abstract}

\section{The statement and its scope}
Let
\[
 X=(\C^3\setminus\{0\})/\langle z\mapsto \mathrm e^{-1}z\rangle,
 \qquad \ddc=\frac{\mathrm i}{2\pi}\partial\bar\partial,
 \qquad \dc=\frac{\mathrm i}{4\pi}(\bar\partial-\partial).
\]
On the cover put $s=\log|z|^2$, $\alpha=\ddc s$,
$\beta=\mathrm ds\wedge\dc s$, and $\omega=\alpha+\beta$.
Then $\alpha=\pi^*\omega_{\FS}$ for projectivization
$\pi:X\to\Pp^2$, with $\int_{\Pp^2}\omega_{\FS}^2=1$ and
$\int_X\omega^3=6$. All potentials below are genuine quasi-plurisubharmonic
functions with their canonical upper representatives. For a smooth bounded
potential the extended non-pluripolar product is its ordinary smooth product.

\begin{theorem}\label{thm:core}
There are $A,B,D,\eta_0>0$ such that for every $0<\eta<\eta_0$ there exist
$u_\eta\in C^\infty(X,\R)$ and a measurable $K_\eta\subset X$ satisfying
\begin{gather*}
 \sup_Xu_\eta=0,\qquad \omega+\ddc u_\eta>0,
 \qquad 0\leq-u_\eta\leq B\eta^{-2}\quad\text{on }X,\\
 A\eta^{-2}\leq-u_\eta\leq B\eta^{-2}\quad\text{on }K_\eta,
 \qquad
 \int_{K_\eta}(\omega+\ddc u_\eta)^3\geq D\eta^{-1}.
\end{gather*}
\end{theorem}

\begin{corollary}\label{cor:weights}
Let $W:[0,\infty)\to(0,\infty)$ be nonincreasing. A uniform bound for the
weighted masses
\[
 \int_X W(-u)\MA^{\rm ext}_\omega(u)
\]
over all normalized $\omega$-psh potentials requires
\[
 \sup_{T\gg1}\sqrt T\,W(T)<\infty.
\]
Uniform deep tails over that class require $\sqrt T\,W(T)\to0$.
Consequently, for eventually decreasing weights
$W_{p,a}(T)=(1+T)^{-p}[\log(\mathrm e+T)]^{-a}$ tending to zero,
uniform mass bounds fail when $p<1/2$, or when $p=1/2$ and $a<0$.
Uniform deep tails also fail when $p=1/2$ and $a=0$.
\end{corollary}

\begin{theorem}\label{thm:individual}
Suppose $W$ is positive and nonincreasing, finite on compact intervals, and
\[
 \sup_{T\gg1}\sqrt T W(T)=\infty.
\]
Then there is a single genuine normalized $\omega$-psh potential $U$ such that
\[
 \int_XW(-U)\MA^{\rm ext}_\omega(U)=\infty.
\]
Thus universal individual finiteness fails in the same power/logarithmic
regimes where Corollary~\ref{cor:weights} gives unbounded uniform masses.
\end{theorem}

Changing a weight on a fixed compact interval does not affect these
obstructions. The heat construction is credited to Xia--Zhang; the faster
scale, correction and limiting arguments are proved below rather than
importing their final construction at a different parameter.

Let $\mathcal R$ denote the \emph{entire} class of normalized genuine
$\omega$-psh potentials invariant under
\[
 (z_0,z')\longmapsto(z_0,Az'),\qquad A\in U(2),\quad z'=(z_1,z_2).
\]
This is a globally defined holomorphic symmetry preserving $\omega$.
No reduction of arbitrary potentials to $\mathcal R$ is assumed. Write
$\mu_u=\MA^{\rm ext}_\omega(u)$ and
$\nu_{W,u}=W(-u)\mu_u$, with zero measure on the pole set.
The capacity in this paper is exactly
\[
 \operatorname{Cap}_\omega(B)=
 \sup_{-1\leq v\leq0,\ \omega+\ddc v\geq0}
       \int_B(\omega+\ddc v)^3.
\]
For a positive $C^1$ nonincreasing $W$ tending to zero put
\[
 Q(W)=\sup_{t\geq0}(1+\sqrt{2t})W(t),\qquad
 Q_T(W)=\sup_{t\geq T}(1+\sqrt{2t})W(t).
\]

\begin{theorem}\label{thm:sharp}
Within $\mathcal R$ the following assertions hold.
\begin{enumerate}
\item Every individual $\nu_{W,u}$ is finite if and only if
$\sup_{t\gg1}\sqrt t\,W(t)<\infty$. This is also equivalent to a uniform
total-mass bound. In this case
\[
 \sup_{u\in\mathcal R}\nu_{W,u}(X)\leq12Q(W).
\]
If the condition fails there is one $u\in\mathcal R$ with infinite measure.
\item Uniform deep tails hold if and only if $\sqrt t\,W(t)\to0$.
For all $u\in\mathcal R$ and $T\geq0$,
\[
 \nu_{W,u}(\{-u>T\})\leq12Q_T(W).
\]
The inequality is understood in the extended sense when its right side
is infinite.
\item Uniform absolute continuity relative to $\operatorname{Cap}_\omega$
holds if and only if $\sqrt t\,W(t)\to0$.
\item The assignment $u\mapsto\nu_{W,u}$ is a map into finite measures
and is continuous from capacity convergence in $\mathcal R$ to weak
measure convergence if and only if $\sqrt t\,W(t)\to0$.
When $\sqrt t\,W(t)$ is bounded but does not tend to zero, there are
actual smooth $u_j\in\mathcal R$ converging in capacity to an actual
$g\in\mathcal R$, whose weighted measures have a weak cluster measure
charging the pole divisor of $g$.
\end{enumerate}
For eventually decreasing power/logarithmic weights, modified smoothly
on a compact interval if necessary, finiteness and uniform total bounds
hold exactly for $p>1/2$ or $p=1/2,a\geq0$. The other three properties
hold exactly for $p>1/2$ or $p=1/2,a>0$.
\end{theorem}

The unrestricted sufficient condition
$\int_0^\infty(1+t)(-W'(t))\,\mathrm dt<\infty$ remains known background.
Theorem~\ref{thm:sharp} improves it on the declared invariant class only.
The general optimal-rate question and the interval between the necessary
square-root scale and existing unrestricted sufficient scales remain open.

\section{Heat estimates and the local positivity test}
On the affine chart $U_0\simeq\C^2$ write
$\xi_j=z_j/z_0$ and $w=\log z_0$ modulo
$\Lambda=\mathbb Z+2\pi\mathrm i\mathbb Z$.
The fibers are $E=\C/\Lambda$, with probability area
$\mathrm dA=\mathrm i\,\mathrm dw\wedge\mathrm d\bar w/(4\pi)$.
For $\xi\ne0$ set
\[
 x=\log|\xi|^2,\qquad \mu=\frac{\mathrm e^x}{1+\mathrm e^x},
 \qquad \mu_x=\mu(1-\mu).
\]
For a smooth real $V(x,w)$ independent of $x$ at the negative end and
constant in both variables at the positive end, smooth global extension
holds. The positivity test of \cite[Lemma 2.2]{XZ} is
\begin{equation}\label{eq:test}
 1+V_{w\bar w}>0,\qquad \mu+V_x>0,\qquad
 Q[V]:=V_{xx}+\mu-
          \frac{|\mu+V_{x\bar w}|^2}{1+V_{w\bar w}}>0.
\end{equation}
At $\xi=0$ only the first condition remains. Indeed, the matrix of
$2\pi(\omega+\ddc V)$ in the horizontal tangential, radial, and vertical
frame used there is
\[
 \begin{pmatrix}
 (\mu+V_x)/\mu&0&0\\
 0&(\mu+V_{xx})/[\mu(1-\mu)]&
                      (\mu+V_{x\bar w})/\sqrt{\mu(1-\mu)}\\
 0&(\mu+V_{wx})/\sqrt{\mu(1-\mu)}&1+V_{w\bar w}
 \end{pmatrix}.
\]
The Schur complement gives \eqref{eq:test}. Our $\omega$ and $\ddc$ are
both the source's divided by $2\pi$; scalar potentials and positivity are
therefore unchanged.

Define the fiber heat kernel and potential by
\begin{equation}\label{eq:heat}
 k_t(w)=\frac2t\sum_{\lambda\in\Lambda}\mathrm e^{-|w-\lambda|^2/t},
 \qquad
 F_\eta(t,w)=-\eta\int_t^\infty(k_r(w)-1)\,\mathrm dr.
\end{equation}
Unfolding gives $\int_Ek_t\,\mathrm dA=1$.
Its Fourier coefficients are
$\exp(-\pi^2|p+\mathrm iq/(2\pi)|^2t)$, so
\begin{gather}
 (F_\eta)_t=(F_\eta)_{w\bar w}=\eta(k_t-1),\qquad
 (\log k_t)_{w\bar w}\geq-1/t,\label{eq:heatfacts}\\
 \|\partial_t^aF_\eta(t,\cdot)\|_{C^m(E)}
       \leq C_{a,m}\eta\mathrm e^{-t/4}\quad(t\geq1).
 \label{eq:largetime}
\end{gather}
The logarithmic Hessian equals $-1/t$ plus the variance of $w-\lambda$,
under the Gaussian lattice weights, divided by $t^2$.
The smallest nonzero Fourier eigenvalue is $1/4$, proving the last bound.

\begin{lemma}\label{lem:values}
Uniformly in $\eta$ and $w$,
$F_\eta(t,w)\leq C\eta$ for $t>0$, and
$F_\eta(t,w)\geq-2\eta\log(1/t)-C\eta$ for $0<t\leq1$.
Uniformly on $\sqrt t\leq|w|\leq2\sqrt t$ near the origin of $E$, as $t\to0$,
\begin{align*}
 F_\eta(t,w)&=2\eta\log t+O(\eta),\\
 t k_t(w)&=2\mathrm e^{-|w|^2/t}+O(\mathrm e^{-1/(Ct)}),\\
 t\partial_{\bar w}\log k_t(w)&=-w+O(\mathrm e^{-1/(Ct)}).
\end{align*}
\end{lemma}
\begin{proof}
For the upper bound use $k_r\geq0$ on $(0,1]$ and \eqref{eq:largetime}.
The nonnegative Fourier coefficients imply $k_r(w)\leq k_r(0)$, and Gaussian
summation gives
$k_r(0)\leq2/r+C r^{-1}\mathrm e^{-1/(2r)}$ for $r\leq1$.
Its integrable error proves the lower bound.
On the indicated annulus the nonzero-lattice terms and their derivatives
are exponentially small relative to the zero-lattice term, proving the last
two identities. For the first, split the defining integral at a fixed small
$r_0$. On $[t,r_0]$ the nonzero-lattice contributions have bounded integral,
and the difference between $(2/r)\mathrm e^{-|w|^2/r}$ and $2/r$ has integral
at most $2|w|^2/t\leq8$. The remaining integral is uniformly bounded.
\end{proof}

We also use \cite[Lemmas 3.2--3.3]{XZ}. For fixed
$0<\kappa<1/(200C_0)$, $0<\eta<1/10$, $0<t\leq1$, $1/2\leq\mu\leq1$, and
\[
 \sigma^2=\frac{2\kappa}{\eta}\log\frac1{\eta t},\quad
 h=\eta k_t,\quad
 \zeta=\frac\sigma\mu t\partial_{\bar w}\log k_t,
\]
their estimate is
\begin{equation}\label{eq:square}
 \kappa tk_t-
 \frac{\mu^2(1-\eta)h}{1-\eta+h}
       |\zeta-(1-\eta)^{-1}|^2
 \leq C\kappa\exp\left(-\frac1{C\sigma^2t}\right).
\end{equation}
It follows from
$tk_t\leq C_0\exp(-|t\partial_{\bar w}\log k_t|^2/(C_0t))$.
To recall its application, for a nearest lattice point with distance $d$,
Gaussian summation bounds $tk_t$ by $C\mathrm e^{-d^2/t}$ and
$|t\partial_{\bar w}\log k_t|$ by $C(d+\mathrm e^{-1/(Ct)})$.
This proves the latter estimate. If $\sigma^2t\geq1/100$, \eqref{eq:square}
is immediate after enlarging $C$. Otherwise the square absorbs $\kappa tk_t$
when $|\zeta-(1-\eta)^{-1}|\geq1/4$, using
$\kappa t(1+h)<\eta/100$. In the remaining case $|\zeta|\geq3/4$ and the
Gaussian estimate applies. Constants are uniform for smaller positive
$\kappa$, which will be used below.

\section{The faster scale and global positivity}
Fix $\kappa$ as above, also with $\kappa<1/100$. Choose a small fixed $c>0$
later and set
\begin{gather*}
 \varepsilon=\mathrm e^{-c\eta^{-3}},\qquad
 q_0=\sqrt{c\eta^{-3}+\log(1/\eta)},\qquad
 a=\sqrt{\kappa/(2\eta)},\\
 q(x)=q_0-\int_0^{ax}\chi(s)\,\mathrm ds,\qquad
 t(x)=\eta^{-1}\mathrm e^{-q(x)^2},\\
 b=(q_0-1/2)/a,\qquad x_*=(q_0+1/2)/a,\qquad
 Z_\eta(x,w)=\vartheta(q(x))F_\eta(t(x),w).
\end{gather*}
Here $\chi$ is a fixed smooth nondecreasing cutoff from zero to one on
$[0,1]$, with $\int_0^1\chi=1/2$; $\vartheta$ is another fixed smooth cutoff
from zero to one on $[0,1]$. Then $Z_\eta=F_\eta(\varepsilon,\cdot)$ for
$x\leq0$, $Z_\eta=0$ for $x\geq x_*$, and
\[
 \eta b,\eta x_*\longrightarrow\ell:=\sqrt{2c/\kappa},\qquad
 1+(Z_\eta)_{w\bar w}>1-\eta.
\]
The source uses a different initial heat time. We recheck the positivity
estimates at this new scale rather than import its final proposition.

On $[0,b]$ we have $\vartheta=1$.
With $\sigma=(\log t)_x$, direct differentiation gives the source's exact
square identity
\begin{equation}\label{eq:identity}
\begin{split}
 Q[Z_\eta]={}&\sigma^2t\{h[1+t(\log k_t)_{w\bar w}]-\eta\}
       +\sigma_xtF_t+\mu(1-\mu)-\frac{\mu^2\eta}{1-\eta}\\
 &+\frac{\mu^2(1-\eta)h}{1-\eta+h}
             |\zeta-(1-\eta)^{-1}|^2.
\end{split}
\end{equation}
The contribution involving $h[1+t(\log k_t)_{w\bar w}]$ is nonnegative.
On $[0,a^{-1}]$,
\[
 \sigma=2aq\chi(ax),\quad
 \sigma_x=-\frac\kappa\eta\chi(ax)^2+\frac\kappa\eta q\chi'(ax),
 \quad t\leq\varepsilon\mathrm e^{q_0}.
\]
This upper bound for $t$ is smaller than every power of $\eta$.
Thus $\kappa q\chi't\leq\eta$ and $\sigma^2t\leq\eta^2$.
Use \eqref{eq:square} with $\kappa\chi^2$ where $\chi>0$, and $F_t\geq-\eta$
for the $\chi'$ term. It follows that $\negpart{Q[Z_\eta]}\leq C\eta$.
Where $\chi=0$ also $\chi'=0$, and
$Q[Z_\eta]=\mu-\mu^2/(1-\eta+h)>0$, since $x\leq a^{-1}=o(1)$.

On $[a^{-1},b]$, $\sigma=2aq$, $\sigma_x=-\kappa/\eta$,
$\mathrm dx=-\mathrm dq/a$. For $t\leq1$, \eqref{eq:identity} and
\eqref{eq:square} give
\[
 \negpart{Q[Z_\eta]}\leq
 2\eta+2\kappa q^2t+C\kappa\exp\left(-\frac\eta{C\kappa q^2t}\right).
\]
For $t\geq1$, \eqref{eq:largetime} gives instead
$\negpart{Q[Z_\eta]}\leq C\kappa q^2t^2\mathrm e^{-t/4}$.
Put $L=\log(1/\eta)$. Integrating the $q^2t$ term uses
$\int_{\sqrt L}^\infty q^2\mathrm e^{-q^2}\,\mathrm dq\leq C\sqrt L\eta$.
For the exponential term split at $2\sqrt L$: the initial interval has
length $O(\sqrt L)$, and on the rest
$\eta^2\mathrm e^{q^2}/q^2\geq\mathrm e^{q^2/4}$ for small $\eta$.
Its remaining integral is uniformly bounded even with upper endpoint infinity.
For large time use
$\mathrm dx=\sqrt{\eta/(2\kappa)}\,\mathrm dt/(tq)$,
$q\leq\sqrt L$, and the integrability of $t\mathrm e^{-t/4}$.
Including the constant term and initial interval yields
\begin{equation}\label{eq:defect}
 \int_0^b\max_{w\in E}\negpart{Q[Z_\eta](x,w)}\,\mathrm dx
       \leq C\eta b+C\sqrt{\eta L}\leq C\ell+o(1).
\end{equation}
All constants here are independent of $q_0,c,\eta$ with fixed $\kappa$.
The bound is small after choosing $c$, although it need not tend to zero.

Also $\sup\negpart{(Z_\eta)_x}=O(\sqrt{\eta L})$:
for $t\leq1$ use $F_t\geq-\eta$ and
$t\sqrt{L+\log(1/t)}\leq\sqrt L$; for $t\geq1$ use \eqref{eq:largetime}.
On $[b,x_*]$, $0\leq q\leq1$ and $(\mathrm e\eta)^{-1}\leq t\leq\eta^{-1}$,
so differentiated cutoffs and \eqref{eq:largetime} give
\[
 \sup_w\bigl(|(Z_\eta)_x|+|Q[Z_\eta]-Q[0]|\bigr)
       \leq C\mathrm e^{-1/(5\mathrm e\eta)}.
\]
Choose $c$ so that $\ell<1/(10\mathrm e)$. Since
$Q[0]=\mu(1-\mu)\geq\mathrm e^{-x_*}/4$ here, this implies $Q[Z_\eta]>0$
on the cutoff interval. For $x\leq0$ use
$Q[Z_\eta]\geq\mu(1-\mu/(1-\eta))>0$, and for $x\geq x_*$ use $Z_\eta=0$.
On $[-2,-1]$ the same formula gives $Q[Z_\eta]\geq2/27$.

The continuous defect $d_\eta(x)=\max_w\negpart{Q[Z_\eta]}$ is therefore
supported in $[0,b]$. Choose a smooth nonnegative $r_\eta$, supported in
$(-1/2,b+1/2)$, with $r_\eta>d_\eta$ on $[0,b]$ and
$m_\eta:=\int r_\eta\leq\int d_\eta+\eta$.
Uniform approximation and a positive bump give this choice for each fixed
$\eta$; no uniform derivative bound is needed.
Fix a smooth probability bump $\psi$ supported in $(-2,-1)$ and put
\[
 g_\eta(x)=\int_{-\infty}^x(x-s)(r_\eta(s)-m_\eta\psi(s))\,\mathrm ds,
 \qquad V_\eta=Z_\eta+g_\eta.
\]
The support order implies $-m_\eta\leq g_\eta'\leq0$;
$g_\eta=0$ at the negative end and is constant at the positive end.
Furthermore $g_\eta\leq0$ and $|g_\eta|\leq m_\eta(b+3)=O_c(\eta^{-1})$.
Shrink the fixed $c$ so that \eqref{eq:defect} ensures
\[
 m_\eta<\min\{\mu(-2)/2,\,1/8,\,1/(27\|\psi\|_\infty)\}
\]
for all sufficiently small $\eta$.
Now $Q[V_\eta]=Q[Z_\eta]+r_\eta-m_\eta\psi>0$ everywhere:
use the majorant on $[0,b]$, the margin $2/27$ on $(-2,-1)$, and the
established positivity elsewhere.
The vertical coefficient is above $1-\eta$. For the horizontal coefficient,
derivatives vanish for $x\leq-2$; on $[-2,0]$ use $\mu\geq\mu(-2)>m_\eta$;
on $[0,\infty)$ use $\mu\geq1/2$ and $(Z_\eta)_x\geq-o(1)$.
Thus \eqref{eq:test} gives a smooth globally strictly positive potential.

On $x<-3$, $V_\eta=F_\eta(\varepsilon,\cdot)$ has fiber mean zero, so
$0\leq\sup_XV_\eta\leq C\eta$ by Lemma~\ref{lem:values} and $g_\eta\leq0$.
Set $u_\eta=V_\eta-\sup_XV_\eta$.
Where the cutoff is nonzero $t\geq\varepsilon$, giving
\begin{equation}\label{eq:globaldepth}
 0\leq-u_\eta\leq2c\eta^{-2}+O_c(\eta^{-1})+O(\eta).
\end{equation}
Multiplication by a cutoff between zero and one preserves this lower bound
for $Z_\eta$, including where $F_\eta$ is positive.

\section{Mass at the asserted depth}
Let $K_\eta$ consist of all radial angular directions and
\[
 q_0/2\leq q(x)\leq3q_0/4,\qquad
 \sqrt{t(x)}\leq|w|\leq2\sqrt{t(x)},
\]
using the small lift near zero in $E$.
This lies in the linear transport region, with $\vartheta=1$,
$x\asymp_c\eta^{-1}\to\infty$, $\sigma=2aq\asymp_c\eta^{-2}$, and
superexponentially small $t$. Lemma~\ref{lem:values} gives, uniformly,
\[
 0<c_1\leq tk_t\leq3,\quad h\to\infty,\quad
 \zeta\to0,\quad \eta\sigma^2t\to0,\quad \mu\to1.
\]
In \eqref{eq:identity} the first $h$ contribution is nonnegative,
$\sigma_xtF_t=-\kappa t(k_t-1)\geq-3\kappa$, and the completed square
tends to one. Its other negative terms tend to zero.
Thus $Q[Z_\eta]\geq1/4$ for small $\eta$. On the core $\psi=0$ and
$g_\eta''=r_\eta\geq0$, so $Q[V_\eta]\geq1/4$. Also
\[
 \mu+(V_\eta)_x\geq c_2\eta\sigma,\qquad
 1+(V_\eta)_{w\bar w}\geq c_1\eta/t.
\]
Indeed $(Z_\eta)_x=\eta\sigma(tk_t-t)$ and $\mu+g_\eta'>0$ here;
the vertical inequality follows from $1-\eta+\eta k_t$.

Let $\mathrm d\Omega$ denote probability angular area in $\C^2$.
The radial Fubini--Study measure has ball mass $\mu^2$, hence
$\omega_{\FS}^2=2\mu^2(1-\mu)\,\mathrm dx\,\mathrm d\Omega$.
Since $\omega^3=6\omega_{\FS}^2\mathrm dA$, the determinant of the displayed
positivity matrix gives the exact density
\begin{equation}\label{eq:density}
 (\omega+\ddc V)^3
 =12(\mu+V_x)(1+V_{w\bar w})Q[V]\,
           \mathrm dx\,\mathrm d\Omega\,\mathrm dA.
\end{equation}
The fiber annulus has area $3t/2$.
Integrating the preceding lower bounds and using
$\sigma\,\mathrm dx=-2q\,\mathrm dq$ yields
\[
 \int_{K_\eta}(\omega+\ddc u_\eta)^3
 \geq c_3\eta^2\int_{q_0/2}^{3q_0/4}2q\,\mathrm dq
 =c_4\eta^2q_0^2\geq c_5\eta^{-1}.
\]
This places actual mass on the core; no inference from total energy alone
or limiting unbounded product is used.
The annular value estimate also gives
\[
 -u_\eta=2\eta q^2+O_c(\eta^{-1})+O(\eta\log(1/\eta)).
\]
As $\eta q_0^2=c\eta^{-2}+\eta\log(1/\eta)$, this is bounded above and below
by fixed positive multiples of $\eta^{-2}$ on the core.
Together with \eqref{eq:globaldepth} this proves Theorem~\ref{thm:core}.
All these potentials are bounded: truncations beyond their individual depth
equal them everywhere, so the defining extended product equals
\eqref{eq:density} exactly.

\begin{proof}[Proof of Corollary~\ref{cor:weights}]
On $K_\eta$, monotonicity of $W$ gives
\[
 \int_XW(-u_\eta)\MA^{\rm ext}_\omega(u_\eta)
       \geq D\eta^{-1}W(B\eta^{-2}).
\]
Every sufficiently large $T$ equals $B\eta^{-2}$ for some sufficiently small
$\eta$, proving the necessary bound.
Also $K_\eta\subset\{-u_\eta>A\eta^{-2}/2\}$, so uniform deep tails force
this lower bound to tend to zero. The power and logarithmic conclusions
follow from $\sqrt T W_{p,a}(T)\sim T^{1/2-p}(\log T)^{-a}$.
\end{proof}

\section{A single infinite weighted measure}
\begin{proof}[Proof of Theorem~\ref{thm:individual}]
First select the correction with additional local control. Put
\[
 x_{\rm pre}=(q_0+1/2-2\sqrt L)/a.
\]
Then $t(x_{\rm pre})=\eta^3$, $x_{\rm pre}\to\infty$, and
$b-x_{\rm pre}=O(\sqrt{\eta L})\to0$.
For a fixed large $K$ the preceding defect estimates give
$d_\eta\leq(K/2)\eta$ on $[0,x_{\rm pre}]$:
on the linear portion $q^2t\leq4L\eta^3$, and the exponential error is
$O(\exp(-1/(C\kappa\eta^2L)))=o(\eta)$.
On the initial portion use the previously proved $C\eta$ bound.
The integral of $d_\eta$ on $[x_{\rm pre},b]$ tends to zero by the same
integrated estimates and this interval's length.

Choose a fixed left cutoff, zero for $x\leq-1/2$ and one for $x\geq-1/4$,
and a translated right cutoff, one for $x\leq x_{\rm pre}$ and zero for
$x\geq x_{\rm pre}+1/4$.
Let $r^0_\eta$ be $K\eta$ times their product. It strictly exceeds $d_\eta$
on $[0,x_{\rm pre}]$. The continuous function
$e_\eta=\max(d_\eta-r^0_\eta,0)$ is supported in $[x_{\rm pre},b]$.
Add a smooth nonnegative majorant $s_\eta>e_\eta$ on that interval,
supported in $(x_{\rm pre}-1/4,b+1/2)$, with
$\int s_\eta\leq\int e_\eta+\eta$.
Set $r_\eta=r^0_\eta+s_\eta$. Then
\[
 r_\eta>d_\eta\quad\text{on }[0,b],\qquad
 m_\eta=\int r_\eta\leq K\eta b+O(\sqrt{\eta L})+O(\eta).
\]
After shrinking the fixed $c$, this is bounded by a fixed $m_0$ within all
the positivity tolerances above. The construction and smooth-core theorem
therefore hold for this choice, with fixed $A,B,D$.
On every fixed compact interval $I\Subset(0,\infty)$, for sufficiently small
$\eta$ we have $r_\eta=K\eta$ and exactly
\begin{equation}\label{eq:localcorrection}
 g_\eta(x)=-m_\eta(x-\mu_\psi)
              +K\eta(x^2/2+b_0x+b_1),\qquad
 \mu_\psi=\int s\psi(s)\,\mathrm ds.
\end{equation}
Here $b_0,b_1$ depend only on the fixed left cutoff.
Globally $0\leq-g_\eta(x)\leq m_0(x+2)$ for $x\geq0$.

Let $G(w)=-\int_0^\infty(k_r(w)-1)\,\mathrm dr$ for $w\ne0$ on $E$.
Gaussian integration gives the uniform bound
\begin{equation}\label{eq:offpolevalue}
 -F_\eta(t,w)\leq
 C\eta\bigl(1+\log^+(1/\operatorname{dist}_E(w,0)^2)\bigr),\quad t>0.
\end{equation}
Indeed the nearest Gaussian has integral bounded by
$C+2\log^+(1/\operatorname{dist}_E(w,0)^2)$ on $(0,1]$;
the other lattice terms have bounded integral and large times decay.
The same bound applies after the cutoff.
On a fixed $I\Subset(0,\infty)$, $\vartheta=1$ for small $\eta$ and
$t_\eta(x)\leq\exp(-c/(2\eta^3))$.
Every fixed $x$ derivative of $t_\eta$ has this bound times a polynomial
in $\eta^{-1}$. On compact fiber sets away from zero,
\[
 F_\eta(t_\eta(x),w)/\eta\longrightarrow G(w)
                   \quad\text{in }C^\ell\text{ for every fixed }\ell.
\]
To verify derivatives, subtract $G$ from $G_t=F_\eta(t,\cdot)/\eta$:
$G_t-G=\int_0^t(k_r-1)\,\mathrm dr=-t+O(\exp(-d^2/(Ct)))$ when
$d$ stays positive. Differentiated Gaussian errors have only polynomial
factors in $t^{-1}$, and repeated $x$ differentiation preserves their decay.
Together with \eqref{eq:localcorrection} and $0\leq\sup V_\eta\leq C\eta$,
this gives uniform $C^\ell$ bounds for $u_\eta$ on each such fixed compact
product set, for all sufficiently small $\eta$. The threshold may depend
on the set and derivative order.

Fix $a_j=2^{-j-2}$, $j\geq1$, so $\sum a_j=1/4$.
Choose scales $\eta_j\downarrow0$ recursively and write
$u_j=u_{\eta_j}$, $K_j=K_{\eta_j}$.
Require the minimum $x$ on $K_j$ to exceed every earlier $x_{*,i}$ by two.
Choose a relatively compact product neighborhood $O_j$ of $K_j$, with
positive $x$ interval and fiber closure away from zero, on which the earlier
$u_i$ are constant. The $K_j$ are pairwise disjoint.
With $E_j=\sum_{i<j}a_i\|u_i\|_\infty$, impose
\begin{gather*}
 E_j\leq a_j\eta_j^{-2},\qquad \eta_j\leq a_j,\\
 a_j\eta_j\leq2^{-j}a_i\eta_i\quad(i<j).
\end{gather*}
For each earlier $O_i$, require the preceding uniform derivative bounds to
hold for $u_j$ through order $j$. All are finite constraints at stage $j$,
achievable by making $\eta_j$ smaller. They ensure that the future series
$\sum_{k>i}a_ku_k$ converges in $C^\infty$ on compact subsets of $O_i$:
for every fixed derivative order the sufficiently late terms have a uniform
bound there, and $\sum a_k<\infty$.

These constraints also give $\sum_{k>j}a_k\eta_k\leq a_j\eta_j$.
On $K_j$ the coordinate and distance estimates are
\[
 x\leq C_c\eta_j^{-1},\qquad
 \log^+(1/\operatorname{dist}_E(w,0)^2)\leq C_c\eta_j^{-3}.
\]
Using \eqref{eq:offpolevalue}, the global slope bound on $g_k$, and the
supremum constants, the future depth is at most
\[
 C_c\eta_j^{-3}\sum_{k>j}a_k\eta_k
       +C_c\eta_j^{-1}\sum_{k>j}a_k
 \leq C_c a_j\eta_j^{-2}+C_c\eta_j^{-1}/4.
\]
The last term is at most a fixed multiple of $a_j\eta_j^{-2}$ since
$\eta_j\leq a_j$. Including the earlier and current terms, there is a fixed
$C_*>0$, independent of the scales, such that
\begin{equation}\label{eq:sumdepth}
 -\sum_i a_iu_i\leq C_*a_j\eta_j^{-2}\quad\text{on }K_j.
\end{equation}
Fix this constant before the scale choice. Since $\sqrt T W(T)$ is unbounded,
at each stage choose arbitrarily large $T_j$ such that
\[
 \frac D{\sqrt{C_*}}a_j^{5/2}\sqrt{T_j}W(T_j)\geq1,
 \qquad \eta_j=\sqrt{C_*a_j/T_j},
\]
and so small a scale that all finite preceding constraints hold.
Such values occur arbitrarily far out because $W$ is finite on compact
intervals. Thus the recursive choice is possible.

The smooth nonpositive partial sums $v_N=\sum_{j\leq N}a_ju_j$ decrease, and
\[
 \omega+\ddc v_N
 =(1-\sum_{j\leq N}a_j)\omega
       +\sum_{j\leq N}a_j(\omega+\ddc u_j)\geq\tfrac34\omega.
\]
Normalized $\omega$-psh potentials have a uniform $L^1$ bound on compact
connected $X$: add fixed local quadratic potentials, apply submean at a
maximum point in one inner coordinate ball, and propagate the bound along
a finite connected ball cover using the positive volumes of its overlaps.
This argument uses no mass bound. Hence $\int(-v_N)\leq C\sum a_j<\infty$.
The decreasing limit $v$ is $L^1$ finite and not identically $-\infty$.
Locally, after adding the same quadratic potential, the decreasing limit is
genuine psh; it retains its canonical upper representative.
Distributional positivity passes to the limit with margin $3\omega/4$.
Its supremum is finite and nonpositive.

On $O_j$ the earlier terms are constant and the future series converges
smoothly. Thus $v$ is smooth there and
$\omega+\ddc v\geq a_j(\omega+\ddc u_j)$ pointwise.
The determinant inequality for positive Hermitian matrices gives on $K_j$
\[
 \MA^{\rm ext}_\omega(v)\geq a_j^3(\omega+\ddc u_j)^3.
\]
This is an actual local smooth product: on a compact neighborhood of $K_j$
all sufficiently deep canonical truncations equal $v$.
Set $U=v-\sup_Xv$. Since $\sup v\leq0$, $-U\leq-v$, and its local currents
are unchanged. Monotonicity of $W$ and \eqref{eq:sumdepth} give
\[
 \int_{K_j}W(-U)\MA^{\rm ext}_\omega(U)
 \geq D a_j^3\eta_j^{-1}W(C_*a_j\eta_j^{-2})
 =\frac D{\sqrt{C_*}}a_j^{5/2}\sqrt{T_j}W(T_j)\geq1.
\]
The disjoint $K_j$ prove infinite total mass for this single potential.
They lie in its smooth locus, so no mass is assigned to poles.
\end{proof}

\section{Positive fiber flux and the weighted upper estimate}
We now work with an arbitrary smooth $V\in\mathcal R$, with $V\leq0$.
In the affine chart it has the form $V(x,w)$. The matrix calculation above
applies at every finite $x$, without assuming the special endpoint behavior
of the heat family. Put
\[
 A_V=\mu+V_x,\quad B_V=1+V_{w\bar w},\quad
 R_V=\mu+V_{xx},\quad C_V=\mu+V_{x\bar w},\quad
 \Delta_V=B_VR_V-|C_V|^2.
\]
Semipositivity gives $A_V,B_V,R_V,\Delta_V\geq0$ and, without dividing
by $B_V$,
\begin{equation}\label{eq:general-density}
 \MA_\omega(V)=12 A_V\Delta_V\,
       \mathrm dx\,\mathrm d\Omega\,\mathrm dA.
\end{equation}
The omitted divisor charts have zero mass for a smooth top form.

\begin{lemma}\label{lem:flux}
For every smooth invariant genuine $\omega$-psh potential,
\[
 \int_{\R\times E}\Delta_V\,\mathrm dx\,\mathrm dA=1.
\]
If in addition $V\leq0$, then
\[
 |V_x|^2\leq-2V,\qquad 0\leq A_V\leq1+\sqrt{-2V}.
\]
\end{lemma}
\begin{proof}
Set $m(x)=\int_EV\,\mathrm dA$ and
$e(x)=\int_E|V_w|^2\,\mathrm dA$.
Periodic integration by parts gives
\[
 \begin{split}
 \int_E V_{w\bar w}V_{xx}\,\mathrm dA
    &=-\operatorname{Re}\int_EV_{\bar w}V_{xxw}\,\mathrm dA,\\
 e''&=2\int_E|V_{xw}|^2\,\mathrm dA
       +2\operatorname{Re}\int_EV_{\bar w}V_{xxw}\,\mathrm dA.
 \end{split}
\]
The mean of every fiber derivative vanishes. Expanding $\Delta_V$ yields
\[
 \int_E\Delta_V\,\mathrm dA
   =m''+\mu(1-\mu)-\tfrac12e''.
\]
Thus $f(x)=\log(1+\mathrm e^x)+m(x)-e(x)/2$ is convex.

Both $m$ and $e$ are smooth global functions on the projective base:
local fiber coordinates change by holomorphic translations, preserving
fiber Haar area, the vertical derivative and the Dirichlet integral.
They are $U(2)$-invariant. Smoothness and radial invariance at $\xi=0$
give $m',e'\to0$ at the negative end. At the positive end use a normal
coordinate $z_0/z_1$ to the hyperplane $H=\{z_0=0\}$ on the base.
The invariant base functions are constant along this hyperplane and
smooth across it; their $x$ derivatives tend to zero. This does not
require that the pointwise potential be constant on its elliptic fibers
at that end. Consequently $f'(-\infty)=0$ and $f'(+\infty)=1$.
Integrating the nonnegative $f''$ proves the flux identity.

For each fixed $w$, $R_V\geq0$ implies $V_{xx}\geq-1$ on all of $\R$.
Hence for every real $h$,
\[
 V(x+h,w)\geq V(x,w)+hV_x(x,w)-h^2/2.
\]
Taking $h=V_x(x,w)$ and using $V\leq0$ proves the derivative bound.
Finally $\mu\leq1$ proves the bound for $A_V$.
\end{proof}

Combining the positive density with Lemma~\ref{lem:flux} proves
\begin{equation}\label{eq:smooth-upper}
 \int_XW(-V)\MA_\omega(V)\leq12Q(W),\qquad
 \int_{\{-V>T\}}W(-V)\MA_\omega(V)\leq12Q_T(W).
\end{equation}
The same argument works for any nonnegative continuous weight with finite
$Q$, without its monotonicity. There is no bound on unweighted mass in
this argument; the positive flux supplies the finite reference integral.

\section{Bounded approximation in the original capacity}
We give the passage to all genuine bounded potentials and the local
product argument explicitly. Only bounded local Bedford--Taylor products,
integration by parts, quasi-continuity and polar-set capacity zero are
used from \cite{BT}; no global unbounded Hopf product theorem is invoked.

\begin{lemma}\label{lem:capacity}
The original capacity is locally comparable, on a finite cover by inner
coordinate balls, with relative bounded-psh Bedford--Taylor capacities on
larger balls. Every bounded genuine $u\in\mathcal R$ with $-L\leq u\leq0$
has smooth genuine invariant approximants $u_\epsilon$ with the same
bounds converging in $\operatorname{Cap}_\omega$. If uniformly bounded
genuine potentials converge in that capacity, their bounded products,
and those products multiplied by continuous functions of their depths,
converge weakly.
\end{lemma}
\begin{proof}
For the upper capacity comparison add a fixed positive quadratic $\rho$
with $\ddc\rho\geq\omega$ to every global test $v\in[-1,0]$.
The closed positive cube of $\ddc(v+\rho)$ dominates
$(\omega+\ddc v)^3$. Normalize its bounded local potential range to
$[0,1]$ and use the relative capacity definition.
For the reverse comparison take a local psh test $w\in[-1,0]$ on the
larger ball of radius $R$, and an inner radius $r<R$.
Choose $a>0$ small so $a\ddc|z|^2\leq\omega$, then
$0<\epsilon<a(R^2-r^2)$ small. Select $-1<C_0<0$ with
\[
 -aR^2<C_0<-\epsilon-ar^2.
\]
The potential $\max(\epsilon w-a|z|^2,C_0)$ equals the constant near
the outer boundary and the first branch on the inner ball. Extend by
$C_0$ globally. It is a genuine global test in $[-1,0]$ and its current
on the inner ball dominates $\epsilon\ddc w$. This proves the reverse
comparison with the fixed factor $\epsilon^{-3}$. These comparisons
transfer local quasi-continuity and polar-set capacity zero to the
original capacity.

The compact group $G=U(3)\times(\R/\mathbb Z)$ acts transitively and
holomorphically on $X$ by unitary transformations and positive scalar
multiplication. It preserves $\omega$. With a nonnegative smooth central
approximate identity $\rho_\epsilon$ on $G$, put
\[
 u_\epsilon(x)=\int_Gu(gx)\rho_\epsilon(g)\,\mathrm dg.
\]
Transitive compact-group convolution is smooth, averaging preserves the
current inequality, and centrality makes convolution commute with the
$U(2)$ action. Thus $u_\epsilon\in\mathcal R$ except that its supremum
need only be nonpositive; \eqref{eq:smooth-upper} requires only this.
The original capacity is $G$-invariant by transporting its genuine
bounded tests and local products.

Choose an open $O$ of arbitrarily small capacity such that $u$ is
continuous on compact $X\setminus O$. For $g$ close to the identity,
$u(gx)$ and $u(x)$ are uniformly close whenever both points are outside
$O$. Write $P_\epsilon1_O(x)=\int_G1_O(gx)\rho_\epsilon(g)\,\mathrm dg$.
For small kernel support, outside $O$ the set
$\{|u_\epsilon-u|>\delta\}$ is contained in
$\{P_\epsilon1_O>\delta/(4L)\}$. Markov and invariance give
\[
 \operatorname{Cap}_\omega
    \{P_\epsilon1_O>\delta/(4L)\}
 \leq\frac{4L}{\delta}
       \sup_v\int_XP_\epsilon1_O\,\MA_\omega(v)
 \leq\frac{4L}{\delta}\operatorname{Cap}_\omega(O).
\]
Together with $\operatorname{Cap}_\omega(O)$ this proves capacity
convergence. If $L=0$, the assertion is immediate.

Here is the product passage for any uniformly bounded sequence $u_j$.
In a corrected relatively compact chart put $p_j=u_j+\rho$ and
$p=u+\rho$, genuine uniformly bounded local psh functions. The capacity
comparisons give local capacity convergence. For every compactly supported
smooth test form, telescoping the closed products and bounded integration
by parts express their difference as a sum of integrals of
\[
 (p_j-p)\ddc(\text{test})\wedge
          (\ddc p_j)^l\wedge(\ddc p)^{k-1-l}.
\]
Their absolute values are bounded by $\int|p_j-p|\,\mathrm d\lambda_j$,
where positive mixed measures $\lambda_j$ include fixed Euclidean
quadratic factors. They have uniformly bounded total masses and
$\lambda_j(A)\leq C\operatorname{Cap}_{\rm loc}(A)$ on the support.
Indeed each mixed product occurs with a positive coefficient in the
top power of the sum of its bounded psh potentials and the quadratics;
normalize that sum to $[0,1]$. Splitting at $|p_j-p|\leq\delta$ proves
convergence in every mixed degree.

Write $\omega+\ddc u_j=\ddc p_j-\gamma$ with the fixed smooth
semipositive $\gamma=\ddc\rho-\omega$. Expanding the cube proves
bounded nonclosed product convergence. The form $\gamma$ need not be
closed; its powers are smooth test coefficients in the closed-product
argument. At bounded depth these positive top measures obey the original
bound $(1+L)^3\operatorname{Cap}_\omega(A)$.
A continuous depth weight is uniformly continuous on $[0,L]$, so its
varying error vanishes by capacity domination. For a fixed
quasi-continuous weight, extend its restriction outside an open set of
small capacity to a bounded continuous function; domination bounds the
error. Weak convergence against this continuous extension completes the
weighted product passage.
\end{proof}

The total estimate in \eqref{eq:smooth-upper} now holds for every bounded
invariant $u\leq0$. For its tail estimate take continuous depth cutoffs
majorizing $1_{\{-u>T\}}$, supported in $\{-u>T-\delta\}$, apply the
bounded weighted passage and the smooth estimate, then let
$\delta\downarrow0$. Continuity of $(1+\sqrt{2t})W(t)$ gives
$Q_{T-\delta}(W)\to Q_T(W)$.

\section{Unbounded potentials, uniform tails and continuity}
For every $u\in\mathcal R$ the canonical $u^K=\max(u,-K)$ is bounded,
genuine, invariant and has supremum zero. On $\{u>-K\}$ locality of
bounded products identifies its measure with the compatible finite
level defining $\mu_u$. The restricted measures increase to $\mu_u$.
Their weights agree with $W(-u)$ on these sets. Monotone convergence
therefore extends both estimates in \eqref{eq:smooth-upper} to every
unbounded $u\in\mathcal R$, with the same constants. This proves the
sufficient total and tail assertions.

For every Borel set $B$, splitting at depth $T$ and using the original
restricted-depth capacity estimate gives
\begin{equation}\label{eq:uniform-ac}
 \nu_{W,u}(B)\leq W(0)(1+T)^3\operatorname{Cap}_\omega(B)
                                      +12Q_T(W).
\end{equation}
If $\sqrt t\,W(t)\to0$, first take $T$ large and then capacity small;
this proves uniform absolute continuity.

Suppose $u_j\to u$ in capacity within $\mathcal R$. Fixed bounded
truncations $u_j^K$ converge in capacity to $u^K$. Their weighted
measures converge weakly by Lemma~\ref{lem:capacity}. To remove
truncation, outside $\{u\leq-K\}$ finite-level locality identifies
$\nu_{W,u^K}$ and $\nu_{W,u}$, while
\[
 \nu_{W,u^K}(\{u\leq-K\})\leq12Q_{K-1}(W),\qquad
 \nu_{W,u}(\{u\leq-K\})\leq12Q_{K-1}(W).
\]
The inequalities use the tail sets of $u^K$ and $u$, respectively,
and include possible bounded-truncation mass on $\{u=-K\}$.
Thus the total variation error is at most $24Q_{K-1}(W)$, uniformly
in all potentials. Letting $K\to\infty$ proves weighted weak
continuity when $\sqrt t\,W(t)\to0$.

\section{Capacity concentration and the critical discontinuity}
The core potentials depend only on $x,w$, and the decreasing sum used
for Theorem~\ref{thm:individual} preserves this invariance. Consequently
the single infinite measure and the necessary mass and tail conditions
already hold within $\mathcal R$.

The cores have $x\geq c_1/\eta$ for a fixed $c_1>0$, hence lie in
shrinking neighborhoods of the analytic hyperplane $H=\{z_0=0\}$.
It has zero original capacity by Lemma~\ref{lem:capacity}, and closed
neighborhoods of it have capacity tending to zero. If
$\limsup\sqrt t\,W(t)>0$, select $\eta$ so that
$D\eta^{-1}W(B\eta^{-2})$ is bounded below. The actual weighted
core masses violate uniform capacity absolute continuity. This also
covers unbounded $\sqrt t\,W(t)$.

For the failure of weak continuity in the bounded critical regime,
use the \emph{controlled} correction chosen in the individual-measure
proof. Its plateau and its late supplement satisfy
\[
 \int r^0_\eta=K\eta x_{\rm pre}+O(\eta),\qquad
 \int s_\eta=O(\sqrt{\eta L})+O(\eta),\qquad
 \eta x_{\rm pre}\to\ell.
\]
Therefore $m_\eta\to m:=K\ell>0$. Shrink the fixed $c$ so that $m$
satisfies all the established positivity margins. On each fixed finite
$x$ interval, $r_\eta$ and all its derivatives tend to zero; the late
supplement escapes the interval. Thus $g_\eta$ converges smoothly there to
\[
 g(x)=-m\int_{-\infty}^x(x-s)\psi(s)\,\mathrm ds.
\]
It is zero for $x\leq-2$ and equals $-m(x-\mu_\psi)$ for $x\geq-1$.
The same margins give $\mu+g'>0$ and
$g''+\mu(1-\mu)\geq0$ at finite $x$.
Its base extension at infinity is a canonical logarithmic pole $mH$.
It is therefore an actual normalized genuine $\omega$-psh potential
in $\mathcal R$.

The uniform heat bound \eqref{eq:offpolevalue} and the upper bound
$F_\eta\leq C\eta$ imply that, on compact base sets away from $H$,
fixed-depth exceptional sets lie in exponentially shrinking tubes about
the local holomorphic zero section $w=0$. Finite coordinate covers,
polar-set capacity zero and Lemma~\ref{lem:capacity} give capacity
tending to zero for these tubes. The corrections converge uniformly on
these base compact sets, and their supremum normalization is $O(\eta)$.
Remove an arbitrarily small capacity neighborhood of $H$. These
statements prove the actual convergence $u_\eta\to g$ in original
capacity, rather than convergence of formal energy profiles.

Assume $\sqrt t\,W(t)$ is bounded but does not tend to zero. Choose
the preceding sequence of cores with weighted mass bounded below by
$c_0>0$. The proved upper bound makes their full weighted measures
uniformly finite, so a subsequence has a weak cluster measure $\nu$.
For each fixed closed neighborhood $H_r$ of $H$, all sufficiently late
cores lie in $H_r$. Portmanteau gives $\nu(H_r)\geq c_0$; decreasing
continuity of the finite measure gives $\nu(H)\geq c_0$.
But $\nu_{W,g}(H)=0$ by its defining non-pluripolar truncation.
Thus weighted weak continuity fails for this actual capacity-convergent
sequence. If instead $\sqrt t\,W(t)$ is unbounded,
Theorem~\ref{thm:individual} already prevents a finite-measure map on
all of $\mathcal R$. These necessity arguments, the flux estimate and
the truncation passage complete Theorem~\ref{thm:sharp}.

\begin{remark}
The theorem treats every genuine potential in the stated symmetry class,
including unbounded ones; the counterexamples also obstruct the full
unrestricted class. Angular averaging alone supplies no upper bound for
the quadratic fiber energy of an arbitrary potential. No unrestricted
reduction or full solution of original S02 follows. All new conclusions
in this working article await independent mathematical review and
reconstruction. No literature-priority assertion is made.
\end{remark}

\begin{thebibliography}{9}
\bibitem{XZ}
M.~Xia and K.~Zhang,
\emph{A counterexample to the bounded mass property},
arXiv:2608.21053v1 (2026),
\url{https://arxiv.org/abs/2608.21053v1}.
\bibitem{BT}
E.~Bedford and B.~A.~Taylor,
\emph{A new capacity for plurisubharmonic functions},
Acta Math. 149 (1982), 1--40.
\end{thebibliography}
\end{document}


## Whole new flux, capacity and critical-limit proof

# S02: proposed sharp damping in the full rotational sector

Root-origin private candidate. Native review, independent reconstruction,
original-task acceptance and publication are pending. The theorem below is
restricted to U(2)-invariant genuine potentials on the standard Hopf threefold,
including unbounded ones. It does NOT establish these thresholds for all
potentials in original S02. The existing unrestricted necessary-condition
article, inputs and records remain unchanged. The closed-curve diagnostic
shows why fiber compactness alone would not prove the new estimate.

## Proposed conclusions and exact restriction

Use all original S02 conventions. Let R be the genuine normalized omega-psh
potentials invariant under (z0,z') -> (z0,A z'), A in U(2), on
X=(C^3\{0})/<z->exp(-1)z>. This is a global holomorphic symmetry preserving
omega; it does not assert that arbitrary potentials can be reduced to R.
For W positive C1 nonincreasing with W(t)->0, put

    Q(W)=sup_(t>=0) (1+sqrt(2t))W(t),
    Q_T(W)=sup_(t>=T) (1+sqrt(2t))W(t).

Proposed exact classification WITHIN R:

A. Every individual weighted extended measure is finite if and only if
   sup_(t large) sqrt(t)W(t)<infinity. This is also exactly the condition
   for a uniform total-mass bound; the proposed bound is 12 Q(W).
B. Uniform deep tails hold if and only if sqrt(t)W(t)->0, with bound
   12 Q_T(W) on {-u>T}.
C. Uniform absolute continuity with respect to the ORIGINAL Cap_omega
   holds if and only if sqrt(t)W(t)->0.
D. Capacity convergence in R gives weak convergence of the weighted
   finite measures if sqrt(t)W(t)->0. If sup sqrt(t)W(t)<infinity but
   sqrt(t)W(t) does not tend to zero, an actual R-sequence converges in
   capacity to an actual R-potential while its weighted measures have
   positive limiting mass on a pole divisor and fail weak continuity.
   If sup sqrt(t)W(t)=infinity, there is already an individual infinite
   measure and hence no map into finite measures on all of R.

In the eventually decreasing power/log families this means A exactly for
p>1/2 or p=1/2,a>=0; B--D exactly for p>1/2 or p=1/2,a>0.
These proposed thresholds are for R only. The original unrestricted
thresholds and the gap from 1/2 to the known sufficient exponent 1 remain open.

## 1. Exact smooth flux identity

On the affine base C^2 use x=log|xi|^2 and fiber
w=log z0 modulo Z+2 pi i Z. A smooth invariant potential is V(x,w).
Set

    mu=exp(x)/(1+exp(x)), a=mu+V_x,
    tau=1+V_wbarw, r=V_xx+mu, c=mu+V_xbarw,
    Delta=tau r-|c|^2.

The exact original-normalization positivity matrix, already derived in
the complete S02 smooth-core proof from Xia--Zhang's matrix, gives

    a>=0, tau>=0, r>=0, Delta>=0,
    MA_omega(V)=12 a Delta dx dOmega dA_E.

Here dOmega is the probability angular measure. No division by tau is used,
so the formula and inequalities cover smooth semipositive currents as well
as strictly positive ones. The divisor charts excluded by x and w have zero
mass for a smooth top form.

Let m(x)=integral_E V(x,w)dA_E and e(x)=integral_E |V_w|^2 dA_E.
Periodic fiber integration gives

    integral_E Delta dA_E
       =m''+mu(1-mu)-e''/2.

Indeed integral V_wbarw V_xx=-Re integral V_barw V_xxw,
whereas e''=2 integral |V_xw|^2+2Re integral V_barw V_xxw.
The mean of each fiber derivative, including the cross term 2mu V_xbarw,
vanishes. Thus f=log(1+exp(x))+m-e/2 satisfies f''=integral Delta>=0.

Both m and e are globally smooth functions on the projective base: they
are fiber means with respect to its invariant flat area and Dirichlet
structure. They are U(2)-invariant. At both ends m',e' tend to zero.
Near xi=0 this follows from smoothness in xi and radial invariance. Near
the hyperplane z0=0, use a local base normal coordinate z0/z1; a smooth
U(2)-invariant base function approaches a constant on that hyperplane,
and its x derivative tends to zero. Fiber changes are holomorphic
translations and preserve the two fiber integrals. No assertion that the
pointwise V is constant at the positive end is required.

Consequently f'(-infinity)=0 and f'(+infinity)=1, and the EXACT flux is

    integral_R integral_E Delta dA_E dx=1.

This identity concerns a full smooth global invariant potential, not only
the particular heat family. It replaces any presumed bounded total mass.

## 2. The depth-dependent pointwise derivative bound

For a fixed fiber point w, r>=0 gives V_xx>=-mu>=-1 for ALL real x.
Since V<=0 after global normalization, semiconvexity yields, for every h,

    V(x+h,w)>=V(x,w)+h V_x(x,w)-h^2/2.

Take h=V_x(x,w). The left side is at most zero, so

    |V_x(x,w)|^2<=-2V(x,w),
    0<=a<=1+sqrt(-2V).

This is a POINTWISE depth estimate, not a bound using only the global
oscillation. Combining it with the positive exact flux gives

    integral W(-V) MA_omega(V)<=12 Q(W).

The same positive integral restricted to {-V>T} is at most 12 Q_T(W).
More generally any continuous nonnegative weight with finite Q has this
upper bound; its monotonicity is not needed in this smooth estimate.

## 3. Exact smoothing and capacity passage for bounded R-potentials

Use the compact group G=U(3) x (R/Z) acting by unitary transformations and
real scalar multiplication. It acts transitively and holomorphically on X
and preserves omega. Take a smooth nonnegative central approximate identity
rho_epsilon on G and convolve a bounded genuine u in R:

    u_epsilon(x)=integral_G u(gx)rho_epsilon(g)dg.

This is smooth by transitivity and standard compact-group convolution.
Every translate is omega-psh, so the average is omega-psh. Centrality makes
convolution commute with the U(2) subgroup, retaining R. If -T<=u<=0 then
the SAME inequalities hold for u_epsilon. The pointwise derivative estimate
uses only u_epsilon<=0, so no changing supremum normalization is needed.

For precision the ORIGINAL global capacity is invariant under G. This
follows by transporting its bounded test potentials and actual local
products under a holomorphic omega-preserving map.

The global capacity is comparable with standard local bounded psh capacities
on a finite coordinate-ball cover. For its upper comparison add a fixed
positive quadratic rho with dd^c rho>=omega to every global test in [-1,0]
and rescale its bounded local range: its closed local cube dominates the
test cube. For the reverse comparison on an inner ball, let w be a local
psh test in [-1,0] on an outer ball. Choose a>0 small and epsilon>0 still
smaller and glue

    max(epsilon w-a|z|^2,C0)

to the constant C0 outside the ball, where C0 is below its inner-ball values
and above its boundary values. Such choices use the fixed gap between the
inner and outer radii, with a dd^c|z|^2<=omega and -1<C0<0. This is a
global test in [-1,0]; on the inner ball its current dominates epsilon dd^c w.
It proves the reverse local-capacity bound with a fixed factor epsilon^-3.
These comparisons also transfer local quasi-continuity and analytic-set
capacity zero to the capacity specified in the original task.

Here is a direct capacity proof for group smoothing. For arbitrarily small
capacity choose an open O such that u is continuous on compact X\O.
For group elements near the identity, u(gx) and u(x) are uniformly close
whenever both points are outside O. If u_epsilon-u differs by more than
delta outside O, then P_epsilon 1_O(x)>delta/(4T), once the kernel support
is sufficiently small. Markov and the capacity definition give

    Cap_omega({P_epsilon 1_O>delta/(4T)})
      <=(4T/delta) sup_test integral P_epsilon 1_O MA_omega(test)
      <=(4T/delta) Cap_omega(O),

using G-invariance for every translated O. Together with Cap(O), this proves
u_epsilon->u in the ORIGINAL capacity. The case T=0 is constant and trivial.

Here is the bounded product passage, including the local hypotheses rather
than a global theorem for the Hopf manifold. In a relatively compact chart
choose a fixed positive quadratic rho with dd^c rho>=omega. Put p_j=u_j+rho
and p=u+rho. These are uniformly bounded genuine local psh functions, and
p_j->p in local capacity by the comparisons above. On the support of a
compactly supported smooth test form, the telescoping identity for closed
products and bounded Bedford--Taylor integration by parts express their
difference as a sum of

    integral (p_j-p) dd^c(test) wedge
             (dd^c p_j)^l wedge (dd^c p)^(k-1-l).

Absolute values of these integrals are bounded by integral |p_j-p| dmu_j,
where each positive mixed measure mu_j includes the necessary fixed
Euclidean quadratic factors. Their total masses are uniformly bounded,
and mu_j(A)<=C Cap_local(A) on that compact support. Indeed all the mixed
factors appear with positive coefficients in the top power of the sum of
their uniformly bounded local psh potentials and the fixed quadratics;
normalize the bounded range of that sum to [0,1] and use the local capacity
definition. Splitting where |p_j-p|<=delta proves the integrals tend to zero.
This handles every mixed degree, not just the top one.

Now write omega+dd^c u_j=dd^c p_j-gamma, with
gamma=dd^c rho-omega a fixed smooth semipositive form. Expanding its ordinary
cube gives convergence of the actual bounded nonclosed products. Gamma
need not be closed: it is a smooth test coefficient in the preceding
closed-product argument. These top measures also obey the original
bounded-depth capacity domination from the task. Since W is uniformly
continuous on [0,T], W(-u_j)->W(-u) in capacity. The difference of the
weights contributes a vanishing integral by that domination. To pass a
fixed quasi-continuous weight against the weakly convergent measures,
extend its restriction outside an open set of arbitrarily small capacity
to a continuous bounded function by the usual compact-space extension
theorem; uniform capacity domination bounds the error. This proves the
required weighted weak convergence. Its foundational local product,
multilinearity, integration-by-parts and quasi-continuity applications
still require fresh native assessment of the exact primary passages.

Hence the total weighted estimate passes to every bounded u in R. For tails
first use continuous depth cutoffs majorizing 1_{-u>T} with support in
{-u>T-delta}, then let delta down to zero. This gives the proposed bound
12 Q_T(W); the same argument handles nonnegative continuous auxiliary weights.

## 4. Every unbounded R-potential and sufficiency

For u in R use the canonical u^K=max(u,-K). It is bounded, genuine and still
in R, with sup zero. On {u>-K} its local product equals the defining finite
level of the extended measure. The compatible restricted measures increase,
and the weight agrees with W(-u) there. Monotone convergence of these actual
measures therefore gives the total estimate 12 Q(W) and the tail estimate
12 Q_T(W) for EVERY unbounded u in R as well.

If Q(W)<infinity every measure is finite and the bound is uniform. If
sqrt(t)W(t)->0, Q_T(W)->0 and the tails vanish uniformly. For any Borel A,
split at depth T. The original task's bounded-depth capacity estimate gives

    nu_W,u(A)<=W(0)(1+T)^3 Cap_omega(A)+12 Q_T(W).

Thus these finite measures are uniformly capacity absolutely continuous.
For a sequence u_j->u in capacity in R, truncate at a fixed large depth.
The bounded truncations converge in capacity, their local products with
continuous bounded weights converge weakly, and the uniform tail estimate
removes the truncation. This proves the weak continuity implication.

## 5. Necessary mass conditions and a single infinite measure

The complete existing faster-scale heat construction provides smooth
normalized U(2)-invariant u_eta and cores K_eta of depth between
A eta^-2 and B eta^-2 with actual mass at least D eta^-1. It proves
the necessary condition sup sqrt(t)W(t)<infinity for a uniform bound and
sqrt(t)W(t)->0 for uniform tails, with every large t=B eta^-2 represented.

The complete existing single-measure construction uses a decreasing weighted
sum of these SAME invariant functions. Thus its canonical unbounded limit
is also in R. When sup sqrt(t)W(t)=infinity, its disjoint smooth core
neighborhoods give actual infinite weighted measure for one u in R.
This establishes the necessary condition for universal individual finiteness
too. No divergence of a mere sequence is substituted for that theorem.
Both earlier proofs are unaccepted dependencies requiring independent review;
no prior verdict or task-granted assertion supplies their conclusions.

## 6. Necessary capacity absolute continuity

The heat cores have x>=c1/eta with c1>0 and therefore lie in shrinking
neighborhoods of the analytic hyperplane H={z0=0}. Its original capacity
is zero by the local comparisons above; those neighborhoods have capacity
tending to zero. If limsup sqrt(t)W(t)>0, choose eta along large depths
where D eta^-1 W(B eta^-2) stays bounded below. These ACTUAL weighted
core masses violate uniform capacity absolute continuity. This includes
unbounded limsup. Thus the proposed condition is necessary as well.

## 7. An actual failure of weak continuity at the bounded critical regime

Use the CONTROLLED correction family from the existing individual-measure
proof, rather than an arbitrary earlier smooth correction. It has
r_eta=r0_eta+s_eta, r0_eta=K eta on [0,x_pre], a translated fixed right
cutoff, and integral s_eta=O(sqrt(eta log(1/eta)))+O(eta). The constant K is
fixed independently of eta; choose the original fixed c small enough for all
the positivity margins. With ell=sqrt(2c/kappa), x_pre~ell/eta,

    m_eta=integral r_eta->m:=K ell>0.

On each fixed finite x-interval, r_eta and all its derivatives tend to zero;
the late supplement has escaped that interval. Thus the correction tends
smoothly there to

    g(x)=-m integral_(-infinity)^x (x-s)psi(s)ds.

It is zero for x<=-2 and equals -m(x-mu_psi) for x>=-1. The old positivity
margins ensure mu+g'>0 and g''+mu(1-mu)>=0 on finite x. At infinity it
extends canonically as a base logarithmic pole mH. Consequently g is a
genuine omega-psh normalized invariant potential on X. The chosen m is below
1/8 and the original bump tolerances. This is an actual potential, not a
formal limiting energy profile.

The heat term tends to zero in capacity away from H. Indeed its uniform
value bound is

    -F_eta(t,w)<=C eta(1+log^+(1/dist_E(w,0)^2)),
    F_eta(t,w)<=C eta.

On each compact base set away from H the exceptional set for a fixed depth
delta lies in exponentially shrinking tubes around w=0 in holomorphic
fiber charts. Each such local zero section is analytic; a finite chart cover
and the capacity comparisons make those tubes' capacities tend to zero.
The correction converges uniformly on these base compact sets, and the
supremum normalization is O(eta). Finally remove a small neighborhood of H
of arbitrarily small capacity. Therefore the actual smooth u_eta converge
to the actual g in Cap_omega.

Suppose Q(W)<infinity but limsup sqrt(t)W(t)>0. Select eta as in section6.
The total weighted measures are uniformly bounded by section4 and hence
have weak cluster measures on compact X. Their positive weighted core mass
is supported in shrinking closed neighborhoods of H and stays bounded below.
Portmanteau on each closed neighborhood, followed by decreasing continuity
of a finite cluster measure, implies that every such cluster has positive
mass on H. The actual nu_W,g has zero mass on H by non-pluripolarity.
Thus these capacity-convergent normalized invariant potentials fail weighted
weak continuity. No unbounded-product limit has been assumed to prove it.

## Scope and remaining audits

The positivity matrix and density must be independently verified against the
Xia--Zhang normalization and our direct density calculation. The exact fiber
integration, global endpoint smoothness of m and e, compact-group smoothing,
both local/global capacity comparisons, all bounded product-continuity
applications, every canonical truncation and the controlled critical limit
need full native review and reconstruction. The old complete heat-core and
individual proofs remain necessary unaccepted dependencies.

This proposed result resolves all four damping distinctions only on the
FULL declared U(2)-invariant class R. Angular averaging decreases the quadratic
fiber energy; it provides no upper estimate for an arbitrary original
potential. No reduction of unrestricted S02 to R, no unrestricted sharp
sufficient theorem and no original S02 closure is claimed.


## Whole historical unrestricted obstruction argument and supporting components

# S02: smooth cores and one infinite weighted measure, complete candidate

Review the proposed A--D restricted necessary-condition theorem under the unchanged original definitions. The original optimal-rate completion criterion is preserved and is not claimed satisfied. No native verdict is supplied as authority. The earlier smooth-only note is included unchanged; its then-unresolved individual construction is supplied by the full new supplement. Mathematical acceptance is pending. The prior heat method is credited to Xia--Zhang.

## Entire unchanged root smooth-core construction

# A smooth square-root depth obstruction on the Hopf threefold

Root-origin candidate, mathematically unaccepted. This is a necessary-condition
result for uniform weighted bounds and uniform weighted tails. It does not solve
the optimal S02 question, establish universal individual finiteness, or assert
capacity continuity or its failure. No native model has reviewed this note.

## Exact claim

Use the Hopf threefold and the normalization in the original S02 task:
dd^c = i partial barpartial/(2 pi), omega = alpha + beta, and integral omega^3=6.
There are constants A,B,D>0 and, for every sufficiently small eta>0, a smooth
normalized genuine omega-psh function u_eta, with omega+dd^c u_eta strictly
positive, and a measurable set K_eta such that

    A eta^(-2) <= -u_eta <= B eta^(-2) on K_eta,
    0 <= -u_eta <= B eta^(-2) on all X,
    integral_{K_eta} (omega+dd^c u_eta)^3 >= D eta^(-1).

In particular any decreasing positive weight W must satisfy

    sup_{t large} sqrt(t) W(t) < infinity

if the weighted masses are uniformly bounded over all normalized potentials.
Uniform deep weighted tails necessarily require

    sqrt(t) W(t) -> 0.

These are necessary conditions only. The gap between them and the known
integral sufficient condition from the original task remains open. In
particular no borderline sufficiency claim is made.

## Primary source and the changed parameter

The primary source is Xia--Zhang, arXiv:2608.21053v1, downloaded earlier at
inputs/primary/Xia-Zhang-2608.21053v1.pdf. Its complete extracted text, 902
lines, was read again in this continuation, in ranges 1--300,301--610,611--902.
Its Lemmas 2.2 and 3.1--3.3 and the exact identity (4.2) are used with their
actual hypotheses checked below. The article uses dd^c_src=i partial barpartial.
Both its omega and dd^c_src are 2 pi times the present ones, so its positivity
matrix and scalar potential are unchanged. Its total-mass constants are not
imported; the present density is computed directly below.

The source's epsilon=eta^(1/eta^2) is replaced by

    epsilon = exp(-c eta^(-3)),

where c>0 is a sufficiently small fixed constant. This is a mathematical
change requiring the complete positivity check below; the source's
Proposition 4.1 is not cited as already proving this changed-scale statement.

## Heat estimates

Let E=C/(Z+2 pi i Z), dA=i dw wedge dbarw/(4 pi), and

    k_t(w)=(2/t) sum_{lambda in Lambda} exp(-|w-lambda|^2/t),
    F_eta(t,w)=-eta integral_t^infinity (k_r(w)-1) dr.

The Gaussian sum has integral one and solves k_t,t=k_t,wbarw. Its Fourier
series has coefficients exp(-pi^2 |p+iq/(2pi)|^2 t). Thus

    F_t=F_wbarw=eta(k_t-1),
    (log k_t)_wbarw >= -1/t,
    ||partial_t^a F(t,.)||_{C^m} <= C_{a,m} eta exp(-t/4), t>=1.

For the logarithmic Hessian, use the Gaussian probability weights P_lambda.
The derivative is -1/t plus the variance of w-lambda divided by t^2. For
large time, integrate the nonconstant Fourier coefficients and note that the
least positive eigenvalue is 1/4. Both assertions hold uniformly in eta.

We also need two value estimates not supplied merely by the energy formula:

    F_eta(t,w) <= C eta for all t>0,w in E,
    F_eta(t,w) >= -2 eta log(1/t)-C eta, 0<t<=1.

Indeed k_r>=0 on r<=1, while the integral of |k_r-1| on [1,infinity) is
uniformly bounded. This gives the upper bound. At r<=1, the periodic Gaussian
has maximum at a lattice point: this also follows from its nonnegative
Fourier coefficients. Consequently k_r(w)<=k_r(0)<=2/r+C r^(-1)exp(-1/(2r))
after enlarging C (the Gaussian lattice tail has an integrable bound of this
form). Integrating proves the lower bound. At t>=1 use the Fourier estimate.

Uniformly when sqrt(t)<=|w|<=2sqrt(t), using the small lift at the origin,

    F_eta(t,w)=2 eta log t+O(eta), t->0,
    t k_t(w)=2 exp(-|w|^2/t)+O(exp(-1/(C t))),
    t partial_barw log k_t(w)=-w+O(exp(-1/(C t))).

For the first identity split the integral at a fixed small r0. On [t,r0],
the nonzero-lattice terms have bounded integral, uniformly for |w|<=2sqrt(t),
and the zero-lattice term is (2/r)exp(-|w|^2/r). Its difference from 2/r has
integral at most integral_t^r0 2|w|^2/r^2 dr <=8. On [r0,infinity) use uniform
boundedness. The other two identities follow by termwise differentiation of
the lattice sum: nonzero-lattice Gaussian terms and their derivatives are
exponentially small relative to the zero-lattice term on this annulus. All
constants are uniform in its annular parameter.

The additional heat estimate from source Lemma 3.2 is

    t k_t <= C0 exp(-|t partial_barw log k_t|^2/(C0 t)), 0<t<=1.

Here is the needed source application. Choose a nearest lattice point lambda0,
d=|w-lambda0|, and s_lambda=|w-lambda|^2-d^2>=0. Gaussian summation gives
sum (1+|w-lambda|) exp(-s_lambda/t)<=C and t k_t<=C exp(-d^2/t).
The weighted derivative has absolute value at most C(d+exp(-1/(Ct))): when
d>=1/4 use the first bound, and when d<1/4 use
s_lambda>=|lambda-lambda0|^2/2 for lambda!=lambda0. If the derivative exceeds
twice its exponentially small error, d bounds it from below. Otherwise its
square divided by t is bounded. This proves the displayed estimate.

For fixed 0<kappa<1/(200C0), 0<eta<1/10, 0<t<=1 and 1/2<=mu<=1, put

    sigma^2=(2 kappa/eta) log(1/(eta t)),
    h=eta k_t,
    zeta=(sigma/mu)t partial_barw log k_t.

Source Lemma 3.3 then gives, uniformly,

    kappa t k_t - mu^2(1-eta)h/(1-eta+h)
                 |zeta-(1-eta)^(-1)|^2
      <= C kappa exp(-1/(C sigma^2 t)).

For completeness, if sigma^2 t>=1/100 enlarge C and use t k_t<=C0.
Otherwise, when the square's absolute factor is at least 1/4, its coefficient
makes the square at least h/[100(1+h)]. The defining sigma relation and
log(1/(eta t))>2 imply kappa t(1+h)<eta/100, so the left side is nonpositive.
In the remaining case |zeta|>=3/4, giving
|t partial_barw log k_t|>=3/(8sigma), and the previous Gaussian estimate
proves the assertion. This proof also applies uniformly with any smaller
positive kappa, as needed for the initial transport cutoff.

## Global positive potentials at the faster scale

Fix kappa as above and also kappa<1/100. Let chi be a fixed smooth
nondecreasing cutoff, zero on (-infinity,0], one on [1,infinity), with
integral_0^1 chi=1/2. Let theta be a fixed smooth cutoff, zero on
(-infinity,0], one on [1,infinity), between zero and one. Set

    a=sqrt(kappa/(2eta)),
    q0=sqrt(log(1/(eta epsilon)))=sqrt(c eta^(-3)+log(1/eta)),
    q(x)=q0-integral_0^{a x} chi(s) ds,
    t(x)=eta^(-1) exp(-q(x)^2),
    b=(q0-1/2)/a, xstar=(q0+1/2)/a,
    W_eta(x,w)=theta(q(x)) F_eta(t(x),w).

Thus W_eta=F_eta(epsilon,.) for x<=0, W_eta=0 for x>=xstar, and

    eta b, eta xstar -> sqrt(2c/kappa)=:ell,
    1+(W_eta)_wbarw >1-eta.

Use x=log|xi|^2, mu=exp(x)/(1+exp(x)) on the affine base C^2. The exact
positivity conditions are

    1+V_wbarw>0, mu+V_x>0,
    Q[V]=V_xx+mu-|mu+V_xbarw|^2/(1+V_wbarw)>0.

They follow by writing the Hermitian matrix of 2pi(omega+dd^c V) in one
horizontal tangential, one radial, and one vertical vector. Its entries are
the source matrix (2.6). At xi=0 the only changed coefficient is vertical.
Functions independent of x at the negative end and constant in both variables
at the positive end extend smoothly over all X.

We verify the entire altered-scale defect estimate. On [0,b] theta=1 and,
with sigma=(log t)_x and zeta as above, direct differentiation and completion
of the square give

    Q[W_eta]
      =sigma^2 t {h[1+t(log k_t)_wbarw]-eta}
       +sigma_x t F_t+mu(1-mu)-mu^2 eta/(1-eta)
       +mu^2(1-eta)h/(1-eta+h)|zeta-(1-eta)^(-1)|^2.

The h term in braces is nonnegative. On [0,a^(-1)] we have

    sigma=2 a q chi(ax),
    sigma_x=-(kappa/eta)chi(ax)^2+(kappa/eta)q chi'(ax),
    q0-1/2<=q<=q0, t<=epsilon exp(q0).

The last expression decays faster than any power of eta, even with this
larger q0. In particular kappa q chi' t<=eta and sigma^2t<=eta^2 for small
eta. Apply the square estimate with kappa chi^2 in place of kappa where
chi>0. The chi' term is at least -eta because F_t>=-eta. All remaining
negative terms are O(eta), and the exponential error is O(eta). Hence the
negative part is at most C eta on this initial interval. Where chi=0 its
derivative vanishes and Q=mu-mu^2/(1-eta+h)>0, since x<=a^(-1)=o(1).

On [a^(-1),b], sigma=2 a q and sigma_x=-kappa/eta. For t<=1 the same exact
identity and square estimate give

    [Q[W_eta]]_- <=2eta+2 kappa q^2 t
                      +C kappa exp(-eta/(C kappa q^2 t)).

For t>=1, direct Fourier derivative bounds and the denominator 1-eta+h give

    [Q[W_eta]]_- <= C kappa q^2 t^2 exp(-t/4).

The constants are independent of q0,c,eta once kappa and the cutoffs are fixed.
To integrate, use dx=-dq/a and, on the linear part,
dx=sqrt(eta/(2kappa)) dt/(t q). Put L=log(1/eta). The q^2t term is bounded by
C sqrt(eta L) using integral_{sqrt L}^infinity q^2 exp(-q^2)dq.
For the exponential term split the q-integral at 2sqrt L. The first part has
length O(sqrt L); on the rest eta^2 exp(q^2)/q^2>=exp(q^2/4) for small eta.
The remaining integral is uniformly bounded even when extended to infinity.
Its prefactor is O(sqrt eta). For large time use q<=sqrt L and the integrable
function t exp(-t/4). These contributions are O(sqrt(eta L)). The constant
term and the initial interval contribute at most C eta b. Consequently

    integral_0^b max_w [Q[W_eta](x,w)]_- dx
      <= C eta b+C sqrt(eta L)
      <= C ell+o(1).

This is a small fixed bound after choosing c, rather than the source's o(1).
The negative slope satisfies sup[-(W_eta)_x]_-=O(sqrt(eta L)) as in the source:
for t<=1 use F_t>=-eta and the increasing function
t sqrt(L+log(1/t)); for t>=1 use the Fourier derivative estimates.

On [b,xstar], q is between zero and one and t is between (e eta)^(-1) and
eta^(-1). All scale derivatives and cutoff derivatives have at most polynomial
growth in eta^(-1), hence

    sup_w (|(W_eta)_x|+|Q[W_eta]-Q[0]|)
      <= C exp(-1/(5e eta)).

Here Q[0]=mu(1-mu)>=exp(-xstar)/4. Choose c so that
ell<1/(10e). Then the error is o(exp(-xstar)), and Q[W_eta]>0 on this entire
cutoff interval. For x<=0 the formula
Q[W_eta]>=mu(1-mu/(1-eta))>0 applies since mu<=1/2. For x>=xstar positivity
is automatic. On [-2,-1] specifically Q[W_eta]>=2/27. Thus the continuous
function d_eta(x)=max_w[Q[W_eta]]_- has support in [0,b].

Let psi>=0 be smooth, supported in (-2,-1), with integral one. Take a smooth
nonnegative r_eta, supported in (-1/2,b+1/2), strictly above d_eta on [0,b]
and with m_eta=integral r_eta<=integral d_eta+eta. Its existence follows from
uniform approximation and a positive bump, with approximation tolerance
chosen after fixing eta and b. No uniform derivative bound is asserted.
Choose the fixed c even smaller so that, for small eta,

    m_eta < min{mu(-2)/2, 1/8, 1/(27||psi||_infinity)}.

This is possible from m_eta<=C ell+o(1). Define

    g_eta(x)=integral_{-infinity}^x (x-s)(r_eta(s)-m_eta psi(s)) ds,
    V_eta=W_eta+g_eta.

Because the negative term lies to the left and the two integrals agree,
-m_eta<=g_eta'<=0, g_eta=0 for x<=-2, and g_eta is constant for x>=b+1/2.
Moreover g_eta<=0 and |g_eta|<=m_eta(b+3)=O_c(eta^(-1)). We have
Q[V_eta]=Q[W_eta]+r_eta-m_eta psi, strictly positive on [0,b], positive on
(-2,-1) by its margin 2/27, and positive elsewhere by the established endpoint
estimates. The vertical coefficient is above 1-eta. For x<=-2, both x
derivatives vanish; for -2<=x<=0, mu>=mu(-2)>m_eta; and for x>=0,
mu>=1/2 and (W_eta)_x>=-o(1). Thus mu+(V_eta)_x>0 everywhere. V_eta extends
to a smooth real function on X with omega+dd^c V_eta strictly positive.

On x<-3, V_eta=F_eta(epsilon,.), whose fiber mean is zero. Therefore
0<=sup_X V_eta<=C eta: the lower bound follows from this fiber mean, and the
upper bound from F_eta<=C eta and g_eta<=0. Normalize

    u_eta=V_eta-sup_X V_eta.

The heat lower bound, t>=epsilon wherever theta is nonzero, and the bound
on g_eta give 0<=-u_eta<=2c eta^(-2)+O_c(eta^(-1))+O(eta) on X. Where
theta is between zero and one the same lower bound holds, since a negative
F multiplied by theta increases, and a positive F stays nonnegative.
Thus the asserted global bound follows for sufficiently small eta.

## A genuine Monge--Ampere core

Let K_eta consist, in the above affine trivialization, of all radial angular
directions with

    q0/2 <= q(x) <= 3q0/4,
    sqrt(t(x)) <= |w| <= 2sqrt(t(x)),

using the lift near 0 in E. For small eta this lies strictly inside the linear
transport region: x=(q0+1/2-q)/a, tends uniformly to infinity at order
eta^(-1), and theta=1. On it sigma=2a q is between two positive multiples of
eta^(-2), t is superexponentially small, and the heat annular estimates imply

    t k_t >= c1>0, t k_t<=3,
    h=eta k_t -> infinity,
    zeta=(sigma/mu)t partial_barw log k_t ->0,
    eta sigma^2 t ->0, mu->1.

All limits are uniform on this moving core. In the exact square identity the
first h contribution is nonnegative, sigma_x tF_t=-kappa t(k_t-1)>=-3kappa,
and the completed square tends to 1 uniformly. The terms
-eta sigma^2 t and -mu^2 eta/(1-eta) vanish. Hence Q[W_eta]>=1/4 on K_eta for
small eta, since kappa<1/100; there psi=0 and g_eta''=r_eta>=0, so Q[V_eta]>=1/4.
Furthermore

    mu+(V_eta)_x=mu+eta sigma(t k_t-t)+g_eta'
       >= c2 eta sigma,
    1+(V_eta)_wbarw=1-eta+eta k_t>=c1 eta/t.

For the first inequality, eta sigma tends to infinity; t k_t>=c1 and t->0,
whereas mu+g_eta'>0 by the already proved global positivity margin.

Here is the exact density in the current normalization. Let dOmega be the
probability angular measure on the radial spheres in C^2. The radial
Fubini--Study measure is

    kappa_FS^2=2 mu^2(1-mu) dx dOmega.

This follows either by differentiating its ball mass mu^2, or directly from
det(kappa_FS) proportional to (1+|xi|^2)^(-3) and the normalized radial
integration. Since omega^3=6 kappa_FS^2 dA, and the ratio of determinants in
the positivity matrix is

    (mu+V_x)(1+V_wbarw)Q[V]/[mu^2(1-mu)],

the actual smooth positive Monge--Ampere measure is

    (omega+dd^c V)^3
       =12(mu+V_x)(1+V_wbarw)Q[V] dx dOmega dA.

No energy identity alone is used to place this mass. The annulus in E has
area (3/2)t, since dA is ordinary planar area divided by 2pi. Integrating
the pointwise lower density just proved yields

    integral_{K_eta}(omega+dd^c u_eta)^3
      >=c3 eta^2 integral_{q0/2}^{3q0/4}2q dq
      =c4 eta^2 q0^2 >=c5 eta^(-1).

Normalization does not change this measure. Its extended non-pluripolar
product equals the actual smooth product: u_eta is bounded, so for all
truncation levels exceeding ||u_eta||_infinity the defining measure is the
untruncated one on the entire manifold.

On the core the annular value estimate gives

    F_eta(t,w)=-2eta q^2-2eta log eta+O(eta),
    -u_eta=2eta q^2+O_c(eta^(-1))+O(eta log(1/eta)).

Since q is between q0/2 and 3q0/4 and eta q0^2=c eta^(-2)+eta log(1/eta),
the depth is between fixed positive multiples of eta^(-2). This proves all
three claimed inequalities with fixed constants A,B,D, after decreasing the
eta range. There is no limiting unbounded potential or hidden exchange of
Monge--Ampere limits in this result.

## Consequences and precise limitations

Let W be any positive nonincreasing weight. On K_eta, W(-u_eta)>=W(B eta^(-2)).
Therefore

    integral_X W(-u_eta) MA_ext_omega(u_eta)
      >=D eta^(-1) W(B eta^(-2)).

Every sufficiently large t equals B eta^(-2) for some sufficiently small eta.
A uniform total weighted bound therefore forces sqrt(t)W(t) bounded.
Also K_eta is contained in {-u_eta>A eta^(-2)/2}. A uniform deep-tail limit
forces the displayed lower bound to tend to zero, and hence
sqrt(t)W(t)->0. The inequalities are exact necessary implications for all
normalized potentials, because the constructed smooth ones belong to that
class with their canonical continuous representatives.

For W_p,a(t)=(1+t)^(-p)[log(e+t)]^(-a), where the parameters make the weight
positive decreasing and tending to zero (or after a harmless change on a
fixed compact interval), this gives:

- p<1/2: uniform weighted masses are unbounded for every a.
- p=1/2 and a<0: uniform weighted masses are unbounded.
- p=1/2 and a<=0: uniform deep weighted tails fail.

For p=1/2,a=0 these arguments do not determine a uniform total bound.
For p>1/2 they impose no new obstruction. The known sufficient regime
integral (1+t)(-W'(t))dt<infinity is unchanged, and no assertion settles the
interval from 1/2 to 1, including the logarithmic boundaries. The construction
also does not settle individual finiteness: each u_eta is smooth, so every
one of its weighted masses is finite even when their supremum is infinite.
Capacity absolute continuity, capacity-to-weak continuity, summing these
potentials into an individual infinite weighted example, and optimal decay
remain separate open obligations.


## Entire new individual-measure construction

# S02: a single infinite weighted measure from the smooth cores

Root-origin candidate supplement. No native mathematical acceptance, original
closure or publication. The preceding frozen smooth-core note and five-page
draft remain unchanged historical records. This supplement makes a further
mathematical claim and must undergo full review and independent reconstruction.

Proposed additional theorem: if W is positive nonincreasing, finite on compact
intervals, and sup_{T large} sqrt(T)W(T)=infinity, there is one genuine
supremum-normalized omega-psh potential U for which

    integral_X W(-U) MA_ext_omega(U)=infinity.

In particular universal individual finiteness fails for every eventually
decreasing power/log weight with p<1/2, and for p=1/2,a<0. Borderline individual
finiteness and sharp sufficiency remain open. No capacity-continuity claim is
made. The proof uses actual classical measures on disjoint smooth open sets
of the single potential, rather than passage to a limit of total masses.

## 1. A controlled choice of the correction

Keep the fixed kappa,c, cutoffs and faster scale of the complete smooth-core
note. We may further shrink c once. Put L=log(1/eta) and

    x_pre=(q0+1/2-2 sqrt(L))/a.

For small eta this is in the linear transport region, x_pre->infinity,
t(x_pre)=eta^3, and b-x_pre=(2sqrt(L)-1)/a=O(sqrt(eta L))->0.
There is a fixed K>0 such that d_eta(x)<= (K/2)eta for 0<=x<=x_pre.
On the initial interval use the preceding C eta estimate. On the rest, t<=eta^3
and q^2t=t log(1/(eta t)) is increasing in this range, so q^2t<=4L eta^3.
The exponential defect term is bounded by
C kappa exp(-1/(C kappa eta^2 L)), and hence is o(eta). The other terms are
2eta+O(eta^3 L). This proves the uniform assertion by choosing K large enough.
Moreover the integral of d_eta over [x_pre,b] is O(sqrt(eta L))+o(1), using
the same small/large-time integrals as before and the short interval length.

Fix a smooth left cutoff tau, zero for x<=-1/2 and one for x>=-1/4. Choose
a smooth right cutoff equal to one for x<=x_pre and zero for x>=x_pre+1/4,
obtained by translating a fixed cutoff. Let r0_eta be K eta times their product.
Then r0_eta=K eta on [0,x_pre], strictly above d_eta there; its integral is
at most K eta(x_pre+1). For small eta b<x_pre+1/4.

The continuous e_eta=max(d_eta-r0_eta,0) is supported in [x_pre,b]. Choose
smooth s_eta>=0 supported in (x_pre-1/4,b+1/2), strictly above e_eta on
[x_pre,b], with integral s_eta<=integral e_eta+eta. A uniform approximation
with tolerance depending on eta and a positive bump proves existence.
Set r_eta=r0_eta+s_eta. Then r_eta>d_eta on [0,b], its support lies in
(-1/2,b+1/2), and

    m_eta:=integral r_eta <= K eta b+O(sqrt(eta L))+O(eta).

This is bounded by a fixed small m0 after choosing c. Choose m0 within all
the positivity tolerances in the original correction proof. That proof works
unchanged with this r_eta, except the mass tolerance there is replaced by the
explicit new bound. Therefore all the smooth-core conclusions with fixed
A,B,D remain valid for this chosen family.

This r_eta has an additional local property: on every fixed compact interval
I contained in (0,infinity), r_eta=K eta for all sufficiently small eta.
Indeed x_pre-1/4 eventually exceeds the upper endpoint of I. With the same
fixed negative bump psi, the correction g_eta therefore has, on I,

    g_eta(x)=-m_eta(x-mu_psi)
               +K eta (x^2/2+b0 x+b1),
    mu_psi=integral s psi(s) ds,

where b0,b1 are fixed constants determined only by the left cutoff. The
formula follows by integrating the two terms from the negative end; s_eta
and the right cutoff have not yet entered that interval. In particular all
derivatives of g_eta of order at least three vanish there. Globally
0<=-g_eta(x)<=m0(x+2) for x>=0, since g_eta(-2)=0 and -m0<=g_eta'<=0.

## 2. Uniform control away from the fiber pole

Let G(w)=-integral_0^infinity(k_r(w)-1)dr on E\{0}. It is smooth there and
the Gaussian calculation gives

    |G(w)| <= C(1+log^+(1/dist_E(w,0)^2)).

For example split at a small fixed time. The nearest Gaussian contributes
integral_0^1 (2/r) exp(-d^2/r)dr <=C+2log^+(1/d^2); the remaining lattice
terms have bounded integral, and large times decay. The same calculation
gives for every t>0

    -F_eta(t,w) <= C eta(1+log^+(1/dist_E(w,0)^2)).

This lower value bound does not require t small compared with the distance.
It also applies after multiplying by a cutoff between zero and one.

On a fixed compact I in (0,infinity), q(x)->infinity and theta=1.
We have t_eta(x)<=exp(-c/(2eta^3)) for small eta, because on I
q(x)=q0+1/2-a x and the cross term is only O_I(eta^-2).
Every fixed x derivative of t is a polynomially bounded factor in eta^-1
times this superexponentially small quantity. On a fixed compact fiber set
away from zero,

    F_eta(t_eta(x),w)/eta -> G(w) in C^ell

for every fixed ell. To see this, subtract G and use
G_t-G=integral_0^t(k_r-1)dr=-t+O(exp(-d^2/(Ct))) on such a fiber set.
All fiber derivatives of its Gaussian error have the same exponential decay
times powers of t^-1. Repeated x differentiation brings derivatives of t
just bounded above and hence still gives convergence. These are estimates
of the explicit Gaussian sum, not a claim of uniform convergence near its pole.

Together with the exact local polynomial for g_eta and 0<=sup V_eta<=C eta,
this implies that on each fixed such product open set the smooth u_eta have
uniform C^ell bounds, for all sufficiently small eta. The bounds for ell=0,1
include m0 times a fixed interval constant; higher derivative bounds are a
fixed constant times eta. For each compact set and each finite derivative
order, the threshold in eta is allowed to depend on that set and order.

## 3. Recursive choice of scales

Fix a_j=2^(-j-2), j>=1, so sum a_j=1/4. Select a decreasing sequence eta_j
recursively and use the above chosen u_j=u_eta_j and smooth cores K_j.
Require that the minimum x on K_j exceeds every earlier xstar_i by two.
Thus the K_j are disjoint, and on a small relatively compact product
neighborhood O_j of K_j every earlier u_i is constant. Choose O_j with its
x interval in (0,infinity) and its fiber closure away from zero; for fixed j
the moving annulus forming K_j is compact and separated from zero.

Require, with E_j=sum_{i<j} a_i ||u_i||_infinity,

    E_j <= a_j eta_j^-2, eta_j <= a_j,
    a_j eta_j <=2^-j a_i eta_i for each i<j.

The last inequality gives sum_{k>j}a_k eta_k<=a_j eta_j.
For each earlier O_i also require the uniform C^ell bounds in the previous
section to hold for u_j, for every ell<=j. These are finitely many conditions
at the jth stage and hold when eta_j is sufficiently small. They imply
C^infinity convergence of the future weighted series on each O_i: for any
fixed ell, all sufficiently late j have the stated uniform bound there, and
sum a_j<infinity. The finitely many intervening terms are smooth.

There is a fixed Cstar>0, independent of j, such that these conditions imply

    -sum_i a_i u_i <= Cstar a_j eta_j^-2 on K_j.

The earlier contribution is at most E_j. The current one is at most
B a_j eta_j^-2. On K_j we have x<=C_c eta_j^-1 and
log^+(1/dist_E(w,0)^2)<=C_c eta_j^-3, directly from its annular definition.
The uniform value estimate and the global slope bound for the correction
therefore give for the future contribution

    sum_{k>j} a_k(-u_k)
       <= C_c eta_j^-3 sum_{k>j} a_k eta_k
          +C_c eta_j^-1 sum_{k>j} a_k
       <= C_c a_j eta_j^-2+C_c eta_j^-1/4.

Since eta_j<=a_j, the second term also is at most a fixed multiple of
a_j eta_j^-2. This proves the uniform Cstar assertion. Supremum constants
of each u_k contribute at most C eta_k and are absorbed in the same estimate.
Choose Cstar once using these uniform estimates, before choosing the scales
by the weight below.

If sqrt(T)W(T) is unbounded, at each stage choose an arbitrarily large T_j
with

    (D/sqrt(Cstar)) a_j^(5/2) sqrt(T_j)W(T_j) >=1,
    eta_j=sqrt(Cstar a_j/T_j),

and with eta_j sufficiently small to meet every finite preceding condition.
This is possible because W is finite on compact intervals, so its unbounded
sqrt(T)W(T) values occur arbitrarily far out. The choice is not circular:
Cstar,A,B,D,c,m0 and a_j are fixed before the recursive scales.

## 4. One canonical potential and its actual infinite measure

Put v_N=sum_{j<=N} a_j u_j. These are smooth nonpositive omega-psh functions,
and

    omega+dd^c v_N
      =(1-sum_{j<=N}a_j)omega
          +sum_{j<=N}a_j(omega+dd^c u_j) >=(3/4)omega.

All normalized genuine omega-psh functions have a uniform L1 bound on the
compact connected X. This uses only local submean and a finite connected
coordinate-ball cover: a maximum point first bounds the integral of -u on
one inner ball after adding a fixed local quadratic potential; a point of
bounded -u on each positive-volume overlap propagates the bound along a
finite spanning tree. No Monge--Ampere mass bound or BMP is used. This is
also the precise canonical-compactness application of Demailly I.4.17,
I.4.20--4.21 and I.5.8--5.9 used in the separate P07 factor supplement;
the complete local-primary proofs have been root-read.

Thus integral(-v_N)<=C sum a_j<=C/4. The decreasing limit v=sum a_j u_j is
L1 finite, not identically minus infinity. Locally add a fixed quadratic
potential dominating omega. Decreasing limits of genuine psh functions that
are not identically minus infinity are genuine psh with their canonical
representatives. This gives the pointwise canonical quasi-psh v globally.
The distributional inequality passes to the L1 limit, retaining the strict
margin (3/4)omega. Since v is upper semicontinuous on compact X and is not
identically minus infinity, sup_X v is a finite real number <=0.

On every O_j the earlier terms are constant, the current term is smooth,
and the future series converges in C^infinity by construction. Hence v is
smooth there, and positivity of the current series gives pointwise

    omega+dd^c v >= a_j(omega+dd^c u_j) on O_j.

Taking determinants of positive Hermitian matrices proves the actual
measure inequality on K_j

    MA_ext_omega(v) >= a_j^3(omega+dd^c u_j)^3.

This use of the extended product needs no global unbounded continuity
theorem: v is bounded on a compact neighborhood of K_j inside O_j, so all
sufficiently deep canonical truncations equal v there and its defining
non-pluripolar measure is precisely the classical smooth local cube.

Normalize U=v-sup_X v. This is a genuine omega-psh potential with sup U=0,
with the same actual local currents. Because sup v<=0, -U<=-v, so monotonicity
of W and the proven upper depth on K_j imply

    integral_{K_j} W(-U) MA_ext_omega(U)
       >= D a_j^3 eta_j^-1 W(Cstar a_j eta_j^-2)
       =(D/sqrt(Cstar))a_j^(5/2) sqrt(T_j)W(T_j) >=1.

The pairwise disjoint K_j consequently give infinite total weighted mass
for this single canonical potential. Poles are not counted: the potential
is smooth on each O_j. Nothing is inferred merely from divergence along
the original bounded family.

The resulting individual obstruction is a necessary decay condition only.
It does not establish finiteness when sqrt(T)W(T) is bounded, separate the
remaining sharp thresholds, or settle capacity continuity. If W decays to
zero as in S02, the construction also shows the unweighted measure may have
infinite total mass, which is allowed by the original extended-product
definition. No assertion is made about limits of the original smooth
weighted measures or about an exponent-zero Monge--Ampere equation.


## Complete elementary canonical compactness argument at the scope used

# P07: canonical compactness and exact analytic-level application

UNVERIFIED root proof supplement; no model review, acceptance or publication.
This supplies exact applications for the named factor's existing proof. It
does not use a verdict as a mathematical premise. The author source is frozen.

## Normalized compactness from local primary compactness

Fix the compact connected X0, the smooth positive omega and a fixed C>0.
If distributions v_l satisfy dd^c v_l>=-C omega, add on each coordinate
ball a fixed smooth rho_i=K_i|z|^2 with dd^c rho_i>=C omega. Demailly
I.5.8 (printed40) gives the unique genuine locally integrable psh
representative of v_l+rho_i. Subtracting rho_i gives canonical quasi-psh
representatives, which agree on overlaps by uniqueness. Normalize sup v_l=0.

Choose finitely many coordinate inner balls B_i of radii r_i covering X0,
whose concentric outer balls of radii4r_i lie in their coordinate charts.
Choose rho_i>=0 there and let M_i be its upper bound. The intersection
graph of the inner-ball cover is connected: otherwise the unions in its
two graph components would be disjoint nonempty open subsets of X0.
Every nonempty intersection has positive coordinate volume. Fix a spanning
tree of this finite graph and all its positive intersection volumes.

Each v_l attains its supremum at a point p_l, which belongs to some B_i.
The ball of radius2r_i centered at p_l lies in the outer chart and contains
B_i. Submean for the psh v_l+rho_i at p_l gives

 integral_(B(p_l,2r_i)) (-v_l)
   <= integral rho_i - volume(B(p_l,2r_i))*rho_i(p_l)
   <= M_i volume(B(p_l,2r_i)).

Because -v_l>=0, this bounds its integral on B_i uniformly. Suppose its
integral on B_i is bounded and B_i meets B_j. Coordinate volumes on the
fixed overlap are uniformly comparable. There is a point q in that open
overlap, finite for v_l, with v_l(q)>=-A for one fixed A obtained from
the overlap volume and the preceding integral bound. Apply submean to
v_l+rho_j in the ball B(q,2r_j). It is inside the outer chart and contains
B_j. This bounds the integral of -v_l on B_j by
(M_j+A) volume(B(q,2r_j)). Propagate along the finite tree. There are only
finitely many choices of the initial ball containing p_l, so all constants
can be chosen independently of l. This proves a global uniform L1 bound.

Demailly I.5.9 follows from I.4.21 and positivity of the complex Hessian.
The complete proof of I.4.21 is printed36--37, using weak compactness
of positive Laplacian measures, local Newton kernels and the harmonic
remainder. Apply it to v_l+rho_i on each outer-chart compact subset;
the same submean propagation works on any additional relatively compact
ball in the chart. A finite diagonal extraction gives L1 convergence
on the whole compact manifold to a distribution v. Positivity passes
to the limit, so v again has its canonical C omega-psh representative.
It is not identically minus infinity because it is a finite L1
distribution. Its supremum need not be inferred merely from L1
convergence; nontriviality is all the concentration contradiction uses.

All these are applications of local submean and primary local compactness,
not an assertion that an arbitrary family of test currents is compact.



This complete compactness excerpt is used only for the local-submean uniform L1 bound and canonical representatives. Its original Siu and Lamari applications are not used, and no prior P07 verdict is imported. The new decreasing series retains a strict current margin and its canonical pointwise limit; all infinite mass is shown on its actual smooth open neighborhoods by determinant inequalities and truncation locality, not by a global unbounded-product continuity theorem.

## Entire current seven-page standalone article

```tex
\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\ddc}{\mathrm{d}\mathrm{d}^{\mathrm c}}
\newcommand{\dc}{\mathrm{d}^{\mathrm c}}
\newcommand{\C}{\mathbb C}
\newcommand{\R}{\mathbb R}
\newcommand{\Pp}{\mathbb P}
\newcommand{\FS}{\mathrm{FS}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\negpart}[1]{[#1]_-}
\title{A square-root depth obstruction to uniform damping\newline
on a Hopf threefold}
\author{Research manuscript}
\date{October 5, 2026}
\begin{document}
\maketitle
\begin{center}
\small Working draft. Mathematical review and independent reconstruction pending.
\end{center}
\begin{abstract}
We adapt the heat transport construction of Xia--Zhang to a faster initial
scale. The resulting smooth strictly positive potentials have depth of order
$T$ and at least a constant times $\sqrt T$ of Monge--Amp\`ere mass at that
depth. Thus uniform weighted mass bounds require $\sqrt T W(T)$ to be bounded,
and uniform weighted tails require it to tend to zero. A controlled choice of
the correction also produces a single infinite weighted measure whenever
$\sqrt T W(T)$ is unbounded. Sharp sufficient conditions remain open.
\end{abstract}

\section{The statement and its scope}
Let
\[
 X=(\C^3\setminus\{0\})/\langle z\mapsto \mathrm e^{-1}z\rangle,
 \qquad \ddc=\frac{\mathrm i}{2\pi}\partial\bar\partial,
 \qquad \dc=\frac{\mathrm i}{4\pi}(\bar\partial-\partial).
\]
On the cover put $s=\log|z|^2$, $\alpha=\ddc s$,
$\beta=\mathrm ds\wedge\dc s$, and $\omega=\alpha+\beta$.
Then $\alpha=\pi^*\omega_{\FS}$ for projectivization
$\pi:X\to\Pp^2$, with $\int_{\Pp^2}\omega_{\FS}^2=1$ and
$\int_X\omega^3=6$. All potentials below are genuine quasi-plurisubharmonic
functions with their canonical upper representatives. For a smooth bounded
potential the extended non-pluripolar product is its ordinary smooth product.

\begin{theorem}\label{thm:core}
There are $A,B,D,\eta_0>0$ such that for every $0<\eta<\eta_0$ there exist
$u_\eta\in C^\infty(X,\R)$ and a measurable $K_\eta\subset X$ satisfying
\begin{gather*}
 \sup_Xu_\eta=0,\qquad \omega+\ddc u_\eta>0,
 \qquad 0\leq-u_\eta\leq B\eta^{-2}\quad\text{on }X,\\
 A\eta^{-2}\leq-u_\eta\leq B\eta^{-2}\quad\text{on }K_\eta,
 \qquad
 \int_{K_\eta}(\omega+\ddc u_\eta)^3\geq D\eta^{-1}.
\end{gather*}
\end{theorem}

\begin{corollary}\label{cor:weights}
Let $W:[0,\infty)\to(0,\infty)$ be nonincreasing. A uniform bound for the
weighted masses
\[
 \int_X W(-u)\MA^{\rm ext}_\omega(u)
\]
over all normalized $\omega$-psh potentials requires
\[
 \sup_{T\gg1}\sqrt T\,W(T)<\infty.
\]
Uniform deep tails over that class require $\sqrt T\,W(T)\to0$.
Consequently, for eventually decreasing weights
$W_{p,a}(T)=(1+T)^{-p}[\log(\mathrm e+T)]^{-a}$ tending to zero,
uniform mass bounds fail when $p<1/2$, or when $p=1/2$ and $a<0$.
Uniform deep tails also fail when $p=1/2$ and $a=0$.
\end{corollary}

\begin{theorem}\label{thm:individual}
Suppose $W$ is positive and nonincreasing, finite on compact intervals, and
\[
 \sup_{T\gg1}\sqrt T W(T)=\infty.
\]
Then there is a single genuine normalized $\omega$-psh potential $U$ such that
\[
 \int_XW(-U)\MA^{\rm ext}_\omega(U)=\infty.
\]
Thus universal individual finiteness fails in the same power/logarithmic
regimes where Corollary~\ref{cor:weights} gives unbounded uniform masses.
\end{theorem}

Changing such a weight on a fixed compact interval does not affect these
obstructions. The known sufficient condition
$\int_0^\infty(1+T)(-W'(T))\,\mathrm dT<\infty$ from the original damping
problem is not improved here. In particular this paper does not determine
the optimal thresholds or sufficient conditions for individual finiteness,
capacity absolute continuity, or capacity-to-weak continuity.

\section{Heat estimates and the local positivity test}
On the affine chart $U_0\simeq\C^2$ write
$\xi_j=z_j/z_0$ and $w=\log z_0$ modulo
$\Lambda=\mathbb Z+2\pi\mathrm i\mathbb Z$.
The fibers are $E=\C/\Lambda$, with probability area
$\mathrm dA=\mathrm i\,\mathrm dw\wedge\mathrm d\bar w/(4\pi)$.
For $\xi\ne0$ set
\[
 x=\log|\xi|^2,\qquad \mu=\frac{\mathrm e^x}{1+\mathrm e^x},
 \qquad \mu_x=\mu(1-\mu).
\]
For a smooth real $V(x,w)$ independent of $x$ at the negative end and
constant in both variables at the positive end, smooth global extension
holds. The positivity test of \cite[Lemma 2.2]{XZ} is
\begin{equation}\label{eq:test}
 1+V_{w\bar w}>0,\qquad \mu+V_x>0,\qquad
 Q[V]:=V_{xx}+\mu-
          \frac{|\mu+V_{x\bar w}|^2}{1+V_{w\bar w}}>0.
\end{equation}
At $\xi=0$ only the first condition remains. Indeed, the matrix of
$2\pi(\omega+\ddc V)$ in the horizontal tangential, radial, and vertical
frame used there is
\[
 \begin{pmatrix}
 (\mu+V_x)/\mu&0&0\\
 0&(\mu+V_{xx})/[\mu(1-\mu)]&
                      (\mu+V_{x\bar w})/\sqrt{\mu(1-\mu)}\\
 0&(\mu+V_{wx})/\sqrt{\mu(1-\mu)}&1+V_{w\bar w}
 \end{pmatrix}.
\]
The Schur complement gives \eqref{eq:test}. Our $\omega$ and $\ddc$ are
both the source's divided by $2\pi$; scalar potentials and positivity are
therefore unchanged.

Define the fiber heat kernel and potential by
\begin{equation}\label{eq:heat}
 k_t(w)=\frac2t\sum_{\lambda\in\Lambda}\mathrm e^{-|w-\lambda|^2/t},
 \qquad
 F_\eta(t,w)=-\eta\int_t^\infty(k_r(w)-1)\,\mathrm dr.
\end{equation}
Unfolding gives $\int_Ek_t\,\mathrm dA=1$.
Its Fourier coefficients are
$\exp(-\pi^2|p+\mathrm iq/(2\pi)|^2t)$, so
\begin{gather}
 (F_\eta)_t=(F_\eta)_{w\bar w}=\eta(k_t-1),\qquad
 (\log k_t)_{w\bar w}\geq-1/t,\label{eq:heatfacts}\\
 \|\partial_t^aF_\eta(t,\cdot)\|_{C^m(E)}
       \leq C_{a,m}\eta\mathrm e^{-t/4}\quad(t\geq1).
 \label{eq:largetime}
\end{gather}
The logarithmic Hessian equals $-1/t$ plus the variance of $w-\lambda$,
under the Gaussian lattice weights, divided by $t^2$.
The smallest nonzero Fourier eigenvalue is $1/4$, proving the last bound.

\begin{lemma}\label{lem:values}
Uniformly in $\eta$ and $w$,
$F_\eta(t,w)\leq C\eta$ for $t>0$, and
$F_\eta(t,w)\geq-2\eta\log(1/t)-C\eta$ for $0<t\leq1$.
Uniformly on $\sqrt t\leq|w|\leq2\sqrt t$ near the origin of $E$, as $t\to0$,
\begin{align*}
 F_\eta(t,w)&=2\eta\log t+O(\eta),\\
 t k_t(w)&=2\mathrm e^{-|w|^2/t}+O(\mathrm e^{-1/(Ct)}),\\
 t\partial_{\bar w}\log k_t(w)&=-w+O(\mathrm e^{-1/(Ct)}).
\end{align*}
\end{lemma}
\begin{proof}
For the upper bound use $k_r\geq0$ on $(0,1]$ and \eqref{eq:largetime}.
The nonnegative Fourier coefficients imply $k_r(w)\leq k_r(0)$, and Gaussian
summation gives
$k_r(0)\leq2/r+C r^{-1}\mathrm e^{-1/(2r)}$ for $r\leq1$.
Its integrable error proves the lower bound.
On the indicated annulus the nonzero-lattice terms and their derivatives
are exponentially small relative to the zero-lattice term, proving the last
two identities. For the first, split the defining integral at a fixed small
$r_0$. On $[t,r_0]$ the nonzero-lattice contributions have bounded integral,
and the difference between $(2/r)\mathrm e^{-|w|^2/r}$ and $2/r$ has integral
at most $2|w|^2/t\leq8$. The remaining integral is uniformly bounded.
\end{proof}

We also use \cite[Lemmas 3.2--3.3]{XZ}. For fixed
$0<\kappa<1/(200C_0)$, $0<\eta<1/10$, $0<t\leq1$, $1/2\leq\mu\leq1$, and
\[
 \sigma^2=\frac{2\kappa}{\eta}\log\frac1{\eta t},\quad
 h=\eta k_t,\quad
 \zeta=\frac\sigma\mu t\partial_{\bar w}\log k_t,
\]
their estimate is
\begin{equation}\label{eq:square}
 \kappa tk_t-
 \frac{\mu^2(1-\eta)h}{1-\eta+h}
       |\zeta-(1-\eta)^{-1}|^2
 \leq C\kappa\exp\left(-\frac1{C\sigma^2t}\right).
\end{equation}
It follows from
$tk_t\leq C_0\exp(-|t\partial_{\bar w}\log k_t|^2/(C_0t))$.
To recall its application, for a nearest lattice point with distance $d$,
Gaussian summation bounds $tk_t$ by $C\mathrm e^{-d^2/t}$ and
$|t\partial_{\bar w}\log k_t|$ by $C(d+\mathrm e^{-1/(Ct)})$.
This proves the latter estimate. If $\sigma^2t\geq1/100$, \eqref{eq:square}
is immediate after enlarging $C$. Otherwise the square absorbs $\kappa tk_t$
when $|\zeta-(1-\eta)^{-1}|\geq1/4$, using
$\kappa t(1+h)<\eta/100$. In the remaining case $|\zeta|\geq3/4$ and the
Gaussian estimate applies. Constants are uniform for smaller positive
$\kappa$, which will be used below.

\section{The faster scale and global positivity}
Fix $\kappa$ as above, also with $\kappa<1/100$. Choose a small fixed $c>0$
later and set
\begin{gather*}
 \varepsilon=\mathrm e^{-c\eta^{-3}},\qquad
 q_0=\sqrt{c\eta^{-3}+\log(1/\eta)},\qquad
 a=\sqrt{\kappa/(2\eta)},\\
 q(x)=q_0-\int_0^{ax}\chi(s)\,\mathrm ds,\qquad
 t(x)=\eta^{-1}\mathrm e^{-q(x)^2},\\
 b=(q_0-1/2)/a,\qquad x_*=(q_0+1/2)/a,\qquad
 Z_\eta(x,w)=\vartheta(q(x))F_\eta(t(x),w).
\end{gather*}
Here $\chi$ is a fixed smooth nondecreasing cutoff from zero to one on
$[0,1]$, with $\int_0^1\chi=1/2$; $\vartheta$ is another fixed smooth cutoff
from zero to one on $[0,1]$. Then $Z_\eta=F_\eta(\varepsilon,\cdot)$ for
$x\leq0$, $Z_\eta=0$ for $x\geq x_*$, and
\[
 \eta b,\eta x_*\longrightarrow\ell:=\sqrt{2c/\kappa},\qquad
 1+(Z_\eta)_{w\bar w}>1-\eta.
\]
The source uses a different initial heat time. We recheck the positivity
estimates at this new scale rather than import its final proposition.

On $[0,b]$ we have $\vartheta=1$.
With $\sigma=(\log t)_x$, direct differentiation gives the source's exact
square identity
\begin{equation}\label{eq:identity}
\begin{split}
 Q[Z_\eta]={}&\sigma^2t\{h[1+t(\log k_t)_{w\bar w}]-\eta\}
       +\sigma_xtF_t+\mu(1-\mu)-\frac{\mu^2\eta}{1-\eta}\\
 &+\frac{\mu^2(1-\eta)h}{1-\eta+h}
             |\zeta-(1-\eta)^{-1}|^2.
\end{split}
\end{equation}
The contribution involving $h[1+t(\log k_t)_{w\bar w}]$ is nonnegative.
On $[0,a^{-1}]$,
\[
 \sigma=2aq\chi(ax),\quad
 \sigma_x=-\frac\kappa\eta\chi(ax)^2+\frac\kappa\eta q\chi'(ax),
 \quad t\leq\varepsilon\mathrm e^{q_0}.
\]
This upper bound for $t$ is smaller than every power of $\eta$.
Thus $\kappa q\chi't\leq\eta$ and $\sigma^2t\leq\eta^2$.
Use \eqref{eq:square} with $\kappa\chi^2$ where $\chi>0$, and $F_t\geq-\eta$
for the $\chi'$ term. It follows that $\negpart{Q[Z_\eta]}\leq C\eta$.
Where $\chi=0$ also $\chi'=0$, and
$Q[Z_\eta]=\mu-\mu^2/(1-\eta+h)>0$, since $x\leq a^{-1}=o(1)$.

On $[a^{-1},b]$, $\sigma=2aq$, $\sigma_x=-\kappa/\eta$,
$\mathrm dx=-\mathrm dq/a$. For $t\leq1$, \eqref{eq:identity} and
\eqref{eq:square} give
\[
 \negpart{Q[Z_\eta]}\leq
 2\eta+2\kappa q^2t+C\kappa\exp\left(-\frac\eta{C\kappa q^2t}\right).
\]
For $t\geq1$, \eqref{eq:largetime} gives instead
$\negpart{Q[Z_\eta]}\leq C\kappa q^2t^2\mathrm e^{-t/4}$.
Put $L=\log(1/\eta)$. Integrating the $q^2t$ term uses
$\int_{\sqrt L}^\infty q^2\mathrm e^{-q^2}\,\mathrm dq\leq C\sqrt L\eta$.
For the exponential term split at $2\sqrt L$: the initial interval has
length $O(\sqrt L)$, and on the rest
$\eta^2\mathrm e^{q^2}/q^2\geq\mathrm e^{q^2/4}$ for small $\eta$.
Its remaining integral is uniformly bounded even with upper endpoint infinity.
For large time use
$\mathrm dx=\sqrt{\eta/(2\kappa)}\,\mathrm dt/(tq)$,
$q\leq\sqrt L$, and the integrability of $t\mathrm e^{-t/4}$.
Including the constant term and initial interval yields
\begin{equation}\label{eq:defect}
 \int_0^b\max_{w\in E}\negpart{Q[Z_\eta](x,w)}\,\mathrm dx
       \leq C\eta b+C\sqrt{\eta L}\leq C\ell+o(1).
\end{equation}
All constants here are independent of $q_0,c,\eta$ with fixed $\kappa$.
The bound is small after choosing $c$, although it need not tend to zero.

Also $\sup\negpart{(Z_\eta)_x}=O(\sqrt{\eta L})$:
for $t\leq1$ use $F_t\geq-\eta$ and
$t\sqrt{L+\log(1/t)}\leq\sqrt L$; for $t\geq1$ use \eqref{eq:largetime}.
On $[b,x_*]$, $0\leq q\leq1$ and $(\mathrm e\eta)^{-1}\leq t\leq\eta^{-1}$,
so differentiated cutoffs and \eqref{eq:largetime} give
\[
 \sup_w\bigl(|(Z_\eta)_x|+|Q[Z_\eta]-Q[0]|\bigr)
       \leq C\mathrm e^{-1/(5\mathrm e\eta)}.
\]
Choose $c$ so that $\ell<1/(10\mathrm e)$. Since
$Q[0]=\mu(1-\mu)\geq\mathrm e^{-x_*}/4$ here, this implies $Q[Z_\eta]>0$
on the cutoff interval. For $x\leq0$ use
$Q[Z_\eta]\geq\mu(1-\mu/(1-\eta))>0$, and for $x\geq x_*$ use $Z_\eta=0$.
On $[-2,-1]$ the same formula gives $Q[Z_\eta]\geq2/27$.

The continuous defect $d_\eta(x)=\max_w\negpart{Q[Z_\eta]}$ is therefore
supported in $[0,b]$. Choose a smooth nonnegative $r_\eta$, supported in
$(-1/2,b+1/2)$, with $r_\eta>d_\eta$ on $[0,b]$ and
$m_\eta:=\int r_\eta\leq\int d_\eta+\eta$.
Uniform approximation and a positive bump give this choice for each fixed
$\eta$; no uniform derivative bound is needed.
Fix a smooth probability bump $\psi$ supported in $(-2,-1)$ and put
\[
 g_\eta(x)=\int_{-\infty}^x(x-s)(r_\eta(s)-m_\eta\psi(s))\,\mathrm ds,
 \qquad V_\eta=Z_\eta+g_\eta.
\]
The support order implies $-m_\eta\leq g_\eta'\leq0$;
$g_\eta=0$ at the negative end and is constant at the positive end.
Furthermore $g_\eta\leq0$ and $|g_\eta|\leq m_\eta(b+3)=O_c(\eta^{-1})$.
Shrink the fixed $c$ so that \eqref{eq:defect} ensures
\[
 m_\eta<\min\{\mu(-2)/2,\,1/8,\,1/(27\|\psi\|_\infty)\}
\]
for all sufficiently small $\eta$.
Now $Q[V_\eta]=Q[Z_\eta]+r_\eta-m_\eta\psi>0$ everywhere:
use the majorant on $[0,b]$, the margin $2/27$ on $(-2,-1)$, and the
established positivity elsewhere.
The vertical coefficient is above $1-\eta$. For the horizontal coefficient,
derivatives vanish for $x\leq-2$; on $[-2,0]$ use $\mu\geq\mu(-2)>m_\eta$;
on $[0,\infty)$ use $\mu\geq1/2$ and $(Z_\eta)_x\geq-o(1)$.
Thus \eqref{eq:test} gives a smooth globally strictly positive potential.

On $x<-3$, $V_\eta=F_\eta(\varepsilon,\cdot)$ has fiber mean zero, so
$0\leq\sup_XV_\eta\leq C\eta$ by Lemma~\ref{lem:values} and $g_\eta\leq0$.
Set $u_\eta=V_\eta-\sup_XV_\eta$.
Where the cutoff is nonzero $t\geq\varepsilon$, giving
\begin{equation}\label{eq:globaldepth}
 0\leq-u_\eta\leq2c\eta^{-2}+O_c(\eta^{-1})+O(\eta).
\end{equation}
Multiplication by a cutoff between zero and one preserves this lower bound
for $Z_\eta$, including where $F_\eta$ is positive.

\section{Mass at the asserted depth}
Let $K_\eta$ consist of all radial angular directions and
\[
 q_0/2\leq q(x)\leq3q_0/4,\qquad
 \sqrt{t(x)}\leq|w|\leq2\sqrt{t(x)},
\]
using the small lift near zero in $E$.
This lies in the linear transport region, with $\vartheta=1$,
$x\asymp_c\eta^{-1}\to\infty$, $\sigma=2aq\asymp_c\eta^{-2}$, and
superexponentially small $t$. Lemma~\ref{lem:values} gives, uniformly,
\[
 0<c_1\leq tk_t\leq3,\quad h\to\infty,\quad
 \zeta\to0,\quad \eta\sigma^2t\to0,\quad \mu\to1.
\]
In \eqref{eq:identity} the first $h$ contribution is nonnegative,
$\sigma_xtF_t=-\kappa t(k_t-1)\geq-3\kappa$, and the completed square
tends to one. Its other negative terms tend to zero.
Thus $Q[Z_\eta]\geq1/4$ for small $\eta$. On the core $\psi=0$ and
$g_\eta''=r_\eta\geq0$, so $Q[V_\eta]\geq1/4$. Also
\[
 \mu+(V_\eta)_x\geq c_2\eta\sigma,\qquad
 1+(V_\eta)_{w\bar w}\geq c_1\eta/t.
\]
Indeed $(Z_\eta)_x=\eta\sigma(tk_t-t)$ and $\mu+g_\eta'>0$ here;
the vertical inequality follows from $1-\eta+\eta k_t$.

Let $\mathrm d\Omega$ denote probability angular area in $\C^2$.
The radial Fubini--Study measure has ball mass $\mu^2$, hence
$\omega_{\FS}^2=2\mu^2(1-\mu)\,\mathrm dx\,\mathrm d\Omega$.
Since $\omega^3=6\omega_{\FS}^2\mathrm dA$, the determinant of the displayed
positivity matrix gives the exact density
\begin{equation}\label{eq:density}
 (\omega+\ddc V)^3
 =12(\mu+V_x)(1+V_{w\bar w})Q[V]\,
           \mathrm dx\,\mathrm d\Omega\,\mathrm dA.
\end{equation}
The fiber annulus has area $3t/2$.
Integrating the preceding lower bounds and using
$\sigma\,\mathrm dx=-2q\,\mathrm dq$ yields
\[
 \int_{K_\eta}(\omega+\ddc u_\eta)^3
 \geq c_3\eta^2\int_{q_0/2}^{3q_0/4}2q\,\mathrm dq
 =c_4\eta^2q_0^2\geq c_5\eta^{-1}.
\]
This places actual mass on the core; no inference from total energy alone
or limiting unbounded product is used.
The annular value estimate also gives
\[
 -u_\eta=2\eta q^2+O_c(\eta^{-1})+O(\eta\log(1/\eta)).
\]
As $\eta q_0^2=c\eta^{-2}+\eta\log(1/\eta)$, this is bounded above and below
by fixed positive multiples of $\eta^{-2}$ on the core.
Together with \eqref{eq:globaldepth} this proves Theorem~\ref{thm:core}.
All these potentials are bounded: truncations beyond their individual depth
equal them everywhere, so the defining extended product equals
\eqref{eq:density} exactly.

\begin{proof}[Proof of Corollary~\ref{cor:weights}]
On $K_\eta$, monotonicity of $W$ gives
\[
 \int_XW(-u_\eta)\MA^{\rm ext}_\omega(u_\eta)
       \geq D\eta^{-1}W(B\eta^{-2}).
\]
Every sufficiently large $T$ equals $B\eta^{-2}$ for some sufficiently small
$\eta$, proving the necessary bound.
Also $K_\eta\subset\{-u_\eta>A\eta^{-2}/2\}$, so uniform deep tails force
this lower bound to tend to zero. The power and logarithmic conclusions
follow from $\sqrt T W_{p,a}(T)\sim T^{1/2-p}(\log T)^{-a}$.
\end{proof}

\section{A single infinite weighted measure}
\begin{proof}[Proof of Theorem~\ref{thm:individual}]
First select the correction with additional local control. Put
\[
 x_{\rm pre}=(q_0+1/2-2\sqrt L)/a.
\]
Then $t(x_{\rm pre})=\eta^3$, $x_{\rm pre}\to\infty$, and
$b-x_{\rm pre}=O(\sqrt{\eta L})\to0$.
For a fixed large $K$ the preceding defect estimates give
$d_\eta\leq(K/2)\eta$ on $[0,x_{\rm pre}]$:
on the linear portion $q^2t\leq4L\eta^3$, and the exponential error is
$O(\exp(-1/(C\kappa\eta^2L)))=o(\eta)$.
On the initial portion use the previously proved $C\eta$ bound.
The integral of $d_\eta$ on $[x_{\rm pre},b]$ tends to zero by the same
integrated estimates and this interval's length.

Choose a fixed left cutoff, zero for $x\leq-1/2$ and one for $x\geq-1/4$,
and a translated right cutoff, one for $x\leq x_{\rm pre}$ and zero for
$x\geq x_{\rm pre}+1/4$.
Let $r^0_\eta$ be $K\eta$ times their product. It strictly exceeds $d_\eta$
on $[0,x_{\rm pre}]$. The continuous function
$e_\eta=\max(d_\eta-r^0_\eta,0)$ is supported in $[x_{\rm pre},b]$.
Add a smooth nonnegative majorant $s_\eta>e_\eta$ on that interval,
supported in $(x_{\rm pre}-1/4,b+1/2)$, with
$\int s_\eta\leq\int e_\eta+\eta$.
Set $r_\eta=r^0_\eta+s_\eta$. Then
\[
 r_\eta>d_\eta\quad\text{on }[0,b],\qquad
 m_\eta=\int r_\eta\leq K\eta b+O(\sqrt{\eta L})+O(\eta).
\]
After shrinking the fixed $c$, this is bounded by a fixed $m_0$ within all
the positivity tolerances above. The construction and smooth-core theorem
therefore hold for this choice, with fixed $A,B,D$.
On every fixed compact interval $I\Subset(0,\infty)$, for sufficiently small
$\eta$ we have $r_\eta=K\eta$ and exactly
\begin{equation}\label{eq:localcorrection}
 g_\eta(x)=-m_\eta(x-\mu_\psi)
              +K\eta(x^2/2+b_0x+b_1),\qquad
 \mu_\psi=\int s\psi(s)\,\mathrm ds.
\end{equation}
Here $b_0,b_1$ depend only on the fixed left cutoff.
Globally $0\leq-g_\eta(x)\leq m_0(x+2)$ for $x\geq0$.

Let $G(w)=-\int_0^\infty(k_r(w)-1)\,\mathrm dr$ for $w\ne0$ on $E$.
Gaussian integration gives the uniform bound
\begin{equation}\label{eq:offpolevalue}
 -F_\eta(t,w)\leq
 C\eta\bigl(1+\log^+(1/\operatorname{dist}_E(w,0)^2)\bigr),\quad t>0.
\end{equation}
Indeed the nearest Gaussian has integral bounded by
$C+2\log^+(1/\operatorname{dist}_E(w,0)^2)$ on $(0,1]$;
the other lattice terms have bounded integral and large times decay.
The same bound applies after the cutoff.
On a fixed $I\Subset(0,\infty)$, $\vartheta=1$ for small $\eta$ and
$t_\eta(x)\leq\exp(-c/(2\eta^3))$.
Every fixed $x$ derivative of $t_\eta$ has this bound times a polynomial
in $\eta^{-1}$. On compact fiber sets away from zero,
\[
 F_\eta(t_\eta(x),w)/\eta\longrightarrow G(w)
                   \quad\text{in }C^\ell\text{ for every fixed }\ell.
\]
To verify derivatives, subtract $G$ from $G_t=F_\eta(t,\cdot)/\eta$:
$G_t-G=\int_0^t(k_r-1)\,\mathrm dr=-t+O(\exp(-d^2/(Ct)))$ when
$d$ stays positive. Differentiated Gaussian errors have only polynomial
factors in $t^{-1}$, and repeated $x$ differentiation preserves their decay.
Together with \eqref{eq:localcorrection} and $0\leq\sup V_\eta\leq C\eta$,
this gives uniform $C^\ell$ bounds for $u_\eta$ on each such fixed compact
product set, for all sufficiently small $\eta$. The threshold may depend
on the set and derivative order.

Fix $a_j=2^{-j-2}$, $j\geq1$, so $\sum a_j=1/4$.
Choose scales $\eta_j\downarrow0$ recursively and write
$u_j=u_{\eta_j}$, $K_j=K_{\eta_j}$.
Require the minimum $x$ on $K_j$ to exceed every earlier $x_{*,i}$ by two.
Choose a relatively compact product neighborhood $O_j$ of $K_j$, with
positive $x$ interval and fiber closure away from zero, on which the earlier
$u_i$ are constant. The $K_j$ are pairwise disjoint.
With $E_j=\sum_{i<j}a_i\|u_i\|_\infty$, impose
\begin{gather*}
 E_j\leq a_j\eta_j^{-2},\qquad \eta_j\leq a_j,\\
 a_j\eta_j\leq2^{-j}a_i\eta_i\quad(i<j).
\end{gather*}
For each earlier $O_i$, require the preceding uniform derivative bounds to
hold for $u_j$ through order $j$. All are finite constraints at stage $j$,
achievable by making $\eta_j$ smaller. They ensure that the future series
$\sum_{k>i}a_ku_k$ converges in $C^\infty$ on compact subsets of $O_i$:
for every fixed derivative order the sufficiently late terms have a uniform
bound there, and $\sum a_k<\infty$.

These constraints also give $\sum_{k>j}a_k\eta_k\leq a_j\eta_j$.
On $K_j$ the coordinate and distance estimates are
\[
 x\leq C_c\eta_j^{-1},\qquad
 \log^+(1/\operatorname{dist}_E(w,0)^2)\leq C_c\eta_j^{-3}.
\]
Using \eqref{eq:offpolevalue}, the global slope bound on $g_k$, and the
supremum constants, the future depth is at most
\[
 C_c\eta_j^{-3}\sum_{k>j}a_k\eta_k
       +C_c\eta_j^{-1}\sum_{k>j}a_k
 \leq C_c a_j\eta_j^{-2}+C_c\eta_j^{-1}/4.
\]
The last term is at most a fixed multiple of $a_j\eta_j^{-2}$ since
$\eta_j\leq a_j$. Including the earlier and current terms, there is a fixed
$C_*>0$, independent of the scales, such that
\begin{equation}\label{eq:sumdepth}
 -\sum_i a_iu_i\leq C_*a_j\eta_j^{-2}\quad\text{on }K_j.
\end{equation}
Fix this constant before the scale choice. Since $\sqrt T W(T)$ is unbounded,
at each stage choose arbitrarily large $T_j$ such that
\[
 \frac D{\sqrt{C_*}}a_j^{5/2}\sqrt{T_j}W(T_j)\geq1,
 \qquad \eta_j=\sqrt{C_*a_j/T_j},
\]
and so small a scale that all finite preceding constraints hold.
Such values occur arbitrarily far out because $W$ is finite on compact
intervals. Thus the recursive choice is possible.

The smooth nonpositive partial sums $v_N=\sum_{j\leq N}a_ju_j$ decrease, and
\[
 \omega+\ddc v_N
 =(1-\sum_{j\leq N}a_j)\omega
       +\sum_{j\leq N}a_j(\omega+\ddc u_j)\geq\tfrac34\omega.
\]
Normalized $\omega$-psh potentials have a uniform $L^1$ bound on compact
connected $X$: add fixed local quadratic potentials, apply submean at a
maximum point in one inner coordinate ball, and propagate the bound along
a finite connected ball cover using the positive volumes of its overlaps.
This argument uses no mass bound. Hence $\int(-v_N)\leq C\sum a_j<\infty$.
The decreasing limit $v$ is $L^1$ finite and not identically $-\infty$.
Locally, after adding the same quadratic potential, the decreasing limit is
genuine psh; it retains its canonical upper representative.
Distributional positivity passes to the limit with margin $3\omega/4$.
Its supremum is finite and nonpositive.

On $O_j$ the earlier terms are constant and the future series converges
smoothly. Thus $v$ is smooth there and
$\omega+\ddc v\geq a_j(\omega+\ddc u_j)$ pointwise.
The determinant inequality for positive Hermitian matrices gives on $K_j$
\[
 \MA^{\rm ext}_\omega(v)\geq a_j^3(\omega+\ddc u_j)^3.
\]
This is an actual local smooth product: on a compact neighborhood of $K_j$
all sufficiently deep canonical truncations equal $v$.
Set $U=v-\sup_Xv$. Since $\sup v\leq0$, $-U\leq-v$, and its local currents
are unchanged. Monotonicity of $W$ and \eqref{eq:sumdepth} give
\[
 \int_{K_j}W(-U)\MA^{\rm ext}_\omega(U)
 \geq D a_j^3\eta_j^{-1}W(C_*a_j\eta_j^{-2})
 =\frac D{\sqrt{C_*}}a_j^{5/2}\sqrt{T_j}W(T_j)\geq1.
\]
The disjoint $K_j$ prove infinite total mass for this single potential.
They lie in its smooth locus, so no mass is assigned to poles.
\end{proof}

\begin{remark}
At $p=1/2,a=0$ uniform tails fail, but this proof does not determine a uniform
total-mass bound. Each constructed weighted measure has finite mass because
its potential is smooth. The single-potential obstruction above is proved
separately and still gives no individual-finiteness conclusion at this
borderline. Sufficiency and the remaining optimal damping thresholds stay
open. The heat method is credited to Xia--Zhang; no priority assertion is
made for this parameter refinement.
\end{remark}

\begin{thebibliography}{1}
\bibitem{XZ}
M.~Xia and K.~Zhang,
\emph{A counterexample to the bounded mass property},
arXiv:2608.21053v1 (2026),
\url{https://arxiv.org/abs/2608.21053v1}.
\end{thebibliography}
\end{document}
```

## Exact statement-only A--D targets and delimited foundations

# Proposed S02 necessary-condition theorem, statements only

This is a proposed restricted answer to the exact original optimal damping
question. Its full optimal-rate completion criterion is unchanged and remains
open unless separately established. No original proof or construction is
supplied. No previously accepted assertion about a new scale is granted.

A. On the original standard Hopf threefold and its exact background omega,
there are fixed A,B,D,eta0>0 and, for each 0<eta<eta0, a globally smooth real
u_eta with canonical representative, sup_X u_eta=0, omega+dd^c u_eta strictly
positive, and a measurable K_eta such that globally
0<=-u_eta<=B eta^-2, on K_eta A eta^-2<=-u_eta<=B eta^-2, and the actual
extended non-pluripolar mass of K_eta is at least D eta^-1. Prove global
admissibility, the exact nonclosed product and normalization, and the depth
and local mass statements together. An energy integral without locating
actual Monge--Ampere mass at the claimed depth does not establish A.

B. For any positive nonincreasing weight W, a uniform total weighted bound
over all normalized omega-psh potentials necessarily implies
sup_{T large} sqrt(T)W(T)<infinity. Uniform deep weighted tails necessarily
imply sqrt(T)W(T)->0. These are claimed only as necessary implications.

C. For eventually decreasing weights tending to zero of the form
W_{p,a}(T)=(1+T)^(-p)[log(e+T)]^(-a), uniform masses are unbounded if p<1/2
(any a), or p=1/2,a<0. Uniform deep tails fail also at p=1/2,a=0.
Modification on a fixed compact interval is allowed to make the weight
globally decreasing. A family of finite smooth weighted measures must not
be promoted to an individual infinite weighted measure. No sufficiency at
p=1/2, no optimal threshold, and no capacity-continuity claim is included.

Ordinary smooth differential calculus, Gaussian lattice/Fourier calculations,
Stokes, Fubini and the canonical quasi-psh definitions in the unchanged task
are permitted foundations. Xia--Zhang arXiv:2608.21053v1 is primary evidence
for the already known Hopf construction; its exact lemmas may be independently
verified and correctly applied, with its dd^c=i partial barpartial convention
converted. Its old-scale conclusion does not grant the new target A.
Any additional indispensable premise must be identified precisely, checked
against primary evidence, and reported unresolved if it cannot be established.

D. For every positive nonincreasing weight W, finite on compact intervals, for which sup_{T large} sqrt(T)W(T)=infinity, there is one genuine canonical supremum-normalized omega-psh potential U with integral_X W(-U) MA_ext_omega(U)=infinity. Prove the actual single potential and its defining non-pluripolar measure, including all canonical limiting and normalization requirements. Infinite weighted mass along a bounded family alone does not prove D. Thus universal individual finiteness fails for the power/logarithmic regimes in C with unbounded sqrt(T)W(T). No sufficiency at bounded sqrt(T)W(T), sharp threshold or capacity-continuity result is proposed. Ordinary local submean, elementary decreasing psh limits, local bounded Bedford--Taylor locality and smooth positive determinant inequalities are permitted foundations, with their exact applications to the new construction to be proved. This paragraph gives statements only; no construction, scales, summation prescription or smoothing mechanism is supplied.


## Primary application boundary

Xia--Zhang2608.21053v1 Lemma2.2 supplies the exact matrix after simultaneous background/ddc division by2pi. Lemma3.1 supplies Gaussian/Fourier heat derivatives, and Lemmas3.2--3.3 the square bound with uniformly smaller kappa. Equation4.2 is the exact algebraic identity on the actual transport region. The original Proposition4.1 is not imported for the changed exp(-c eta^-3) scale. Every altered endpoint, defect integral, fixed-small correction, depth and mass placement is proved anew. The new correction is deliberately chosen with exact plateaus on fixed finite positive intervals; its remaining unrestricted derivatives are only in a region escaping to infinity. All recursive bounds, canonical L1 finiteness, actual smooth-core product and weight normalization are included. Demailly I.4.17,4.20--4.21 and I.5.8--5.9 printed35--41 are exact primary evidence for the elementary compactness application if needed; these do not assume BMP. Independently obtain primary evidence, assess every new application, bind all indispensable uncertain premises with valid nonnegative indices and retain any gap. No optimal sufficiency, capacity continuity or original closure is asserted.


## Exact new primary applications; not accepted facts

{
  "recorded_at_utc": "2026-10-07T20:20:40.494465+00:00",
  "article_sha256": "df20e26a68d5f12f9dcb19f2c38482d62396daac825afba06cafca91d763ed4f",
  "whole_current_925_line_source_actually_root_read": true,
  "actual_source_read_ranges": [
    [
      1,
      230
    ],
    [
      231,
      460
    ],
    [
      461,
      695
    ],
    [
      696,
      925
    ]
  ],
  "whole_new_private_proof_and_new_bounded_product_passage_actually_root_read": true,
  "new_exact_applications": [
    {
      "source": "Bedford--Taylor, A new capacity for plurisubharmonic functions, Acta Math149 (1982)",
      "pdf": "inputs/primary/Bedford-Taylor-new-capacity.pdf",
      "text": "inputs/primary/Bedford-Taylor-new-capacity.txt",
      "actual_complete_passages_read": [
        [
          125,
          299
        ],
        [
          388,
          434
        ],
        [
          550,
          625
        ],
        [
          950,
          1135
        ]
      ],
      "exact_application": "Use local bounded psh products only. The complete Theorem2.1 proof and Corollary2.2 support actual closed mixed products, positivity and multilinearity; Corollary2.8 and its whole proof support telescoping with compactly supported test forms. The bounded proof of Theorem3.5 supplies quasi-continuity. Proposition6.4 and its whole printed proof give continuity for decreasing compact neighborhoods, and Theorem6.9 with its full printed proof, supported by the read section6 propositions and Josefson proof, gives zero outer capacity for local analytic pole sets. Fixed quadratic correction turns every bounded genuine omega-psh into a bounded local psh. Mixed products including Euclidean quadratics are dominated by a normalized bounded psh top cube, giving uniform local-capacity domination. Splitting the telescoping difference at |p_j-p|<=delta proves capacity product continuity directly, including every lower mixed degree. The nonclosed background gamma is a smooth test coefficient, not a falsely closed form. Genuine global test gluing proves the reverse local-capacity comparison; upper comparison follows by adding rho. Uniform bounded-depth original capacity domination passes continuous depth weights using quasi-continuity and compact-space extension. No global Hopf unbounded convergence or BMP theorem is imported.",
      "pdf_sha256": "e75ea91e48c14a9838a800aee25b68ed04169c4372f2ce4b399967b53005b758",
      "text_sha256": "d32eb9305e1cfbcc569746d51d53e417508b33aba0e3b5a1a706036cb0593115"
    },
    {
      "source": "Xia--Zhang, arXiv2608.21053v1",
      "pdf": "inputs/primary/Xia-Zhang-2608.21053v1.pdf",
      "text": "inputs/primary/Xia-Zhang-2608.21053v1.txt",
      "actual_complete_passages_read_again": [
        [
          211,
          305
        ],
        [
          484,
          570
        ]
      ],
      "exact_application": "The complete local matrix proof of Lemma2.2 applies at every finite radial x to arbitrary smooth invariant V; its endpoint assumptions are needed only for the special family extension, not for that local differentiation. Multiply the original forms and operator by1/(2pi) and keep scalar potentials unchanged. The actual determinant and normalized radial and fiber densities give12 A Delta, also for semipositive matrices without division. Lemmas3.2 and3.3 and their whole proofs give the Gaussian/completed-square inequality uniformly for the specified eta, kappa, mu and t. The new epsilon=exp(-c eta^-3), nonvanishing limiting correction mass, core-depth estimate, single infinite measure and critical capacity limit are proved in full in the article; the source final Proposition4.1 at its different heat scale is NOT imported as a theorem at this new scale.",
      "pdf_sha256": "0c39d024097dae97940403328cf6f8fb39fe3e21270edd02449948ea17303baa",
      "text_sha256": "7430e311274ea0ef23ed73394951f02095c1da147fe08c0e4b905c8e99343dfb"
    }
  ],
  "elementary_new_proof_steps_not_external_black_boxes": [
    "Periodic integration gives positive flux1; global fiber means and Dirichlet integrals are smooth on the base, with zero radial derivative at both ends.",
    "Semiconvexity V_xx>=-1 and V<=0 imply |V_x|^2<=-2V pointwise.",
    "Compact central group convolution preserves the exact symmetry and current bound; a Markov/capacity-invariance argument proves original-capacity convergence.",
    "Canonical truncation locality, actual compatible measure monotonicity and uniform tail errors handle all unbounded potentials.",
    "Controlled plateau mass tends to K sqrt(2c/kappa); actual heat exceptional tubes have capacity0 in the limit, giving u_eta->g and actual pole mass in finite weak clusters."
  ],
  "source_claims_are_assumptions_subject_to_independent_application_review": true,
  "recursive_all_cited_foundations_certified": false,
  "mathematical_acceptance": false,
  "original_S02_completed": false,
  "published": false
}


## Whole closed-fiber diagnostic; not a Hopf counterexample

# S02: fiber compactness alone does not bound depth energy

Private diagnostic, not an accepted theorem or an original S02 solution.
It rules out an insufficient argument for a proposed square-root upper bound.
It constructs functions on ONE CLOSED elliptic curve, not global genuine
potentials on the nontrivial Hopf fibration. No Hopf weighted-mass failure
or new sharp exponent follows from it. The current Hopf obstruction and its
original sharpness gap remain unchanged.

## The tempting but insufficient implication

Normalized quasi-psh L1 compactness and nonatomic limiting fiber curvature
measures do not themselves imply that vertical Dirichlet energy is small
compared with depth. Small individual atom weights can occur at many very
deep separated wells. A quantitative global horizontal-curvature condition
would be needed to exclude this phenomenon in the Hopf problem.

## An explicit closed-curve counterexample to that implication

Use E=C/(Z+2 pi i Z) with probability flat form
kappa=i dw wedge dbarw/(4 pi) and the original dd^c=i partial barpartial/(2 pi).
Let k_t be its normalized heat kernel from the complete S02 proof:

    k_t(w)=(2/t) sum_(lambda in Lambda) exp(-|w-lambda|^2/t),
    integral k_t kappa=1, (k_t)_t=(k_t)_wbarw.

Define the mean-zero smooth Green regularization

    g_epsilon(w)=-(1/2) integral_epsilon^infinity (k_t(w)-1)dt.

Direct differentiation gives

    dd^c g_epsilon=(k_epsilon-1)kappa.

The factor 1/2 is required by the ORIGINAL operator and probability form.
The positive Fourier coefficients put the minimum of g_epsilon at 0.
The same Gaussian and large-time Fourier bounds as in the S02 full proof give

    min g_epsilon=log epsilon+O(1),
    0<=sup g_epsilon<=C,
    integral |g_epsilon| kappa<=C,

with constants independent of small epsilon. The L1 bound can also be
seen directly from mean zero and the uniform upper bound.

Heat convolution and smooth Stokes give the exact Dirichlet expression

    integral dg_epsilon wedge d^c g_epsilon
      =-integral g_epsilon (k_epsilon-1)kappa
      =(1/2) integral_epsilon^infinity (k_(t+epsilon)(0)-1)dt
      =log(1/epsilon)+O(1).

For the last estimate k_s(0)=2/s+O(s^-1 exp(-1/(Cs))) at small time,
and the nonconstant Fourier modes decay integrably at large time. These
are smooth finite identities; no singular-energy limiting theorem is used.

For an integer M>=1 let [M]:E->E be multiplication by M. It has degree
M^2 and [M]^*kappa=M^2 kappa. Put epsilon_M=exp(-M^4) and

    v_M=(g_(epsilon_M) composed with [M]-sup g_(epsilon_M))/M^2.

These are smooth canonical potentials, sup v_M=0, and

    kappa+dd^c v_M=(1/M^2)[M]^*(k_(epsilon_M)kappa)>0.

Haar invariance under the finite covering proves

    ||v_M||_L1<=C/M^2,
    depth_M:=||v_M||_infinity=M^2+O(M^-2).

The energy transforms as

    integral dv_M wedge d^c v_M
       =(1/M^4) integral [M]^*(dg_epsilon wedge d^c g_epsilon)
       =(1/M^2) integral dg_epsilon wedge d^c g_epsilon
       =M^2+O(M^-2).

Thus v_M->0 in L1, their positive curvature probabilities converge weakly
to the smooth nonatomic kappa, but energy_M/depth_M->1. In particular
energy is not O(sqrt(depth)) in this closed-curve setting. The measure
convergence follows distributionally from L1 convergence and then weakly
as positive probabilities of fixed mass.

## What is and is not ruled out

This invalidates a proof based only on fiberwise canonical compactness,
weak curvature convergence, or absence of atoms in its limiting measure.
It does NOT disprove a square-root depth bound for the global Hopf class:
the fiber multiplication and the Green wells have not been made into global
functions respecting the nontrivial bundle transitions and all horizontal
positivity inequalities. That full coupled admissibility is the unresolved
mathematical requirement. No publication, native admission, sharp sufficient
condition or original S02 closure is recorded for this diagnostic.


## Known-overlap and original scope

# Known overlap and scope

The source Xia--Zhang heat transport, smooth mass identity and original
threefold BMP failure are credited inputs. The existing general layer-cake
damping theorem and its bounded-weighted-product/truncation argument are known
background, reproduced completely below. The original task already grants its
restricted-depth estimates. Those facts are not new sharp sufficient conditions.
The proposed new scope is the full declared U(2)-invariant class, the positive
flux/depth upper estimate and its sharp classifications and genuine critical
discontinuity. All old heat refinement and single-measure proofs are unaccepted
dependencies to assess anew, not granted results. The closed elliptic diagnostic
is a caution about fiber-only estimates; it is not a global Hopf counterexample
and supplies no dependency for the new theorem. No literature priority or
unrestricted original completion is claimed.


## Whole known general damping source

\Needspace{17\baselineskip}
\begin{theorem}\label{thm:damped-continuity}\index{Damping!capacity continuity}\label{prop:general-damping-weights}\index{Damping!general weights}
Let $w:[0,+\infty)\to(0,+\infty)$ be continuously differentiable and nonincreasing, with $w(t)\to0$ as $t\to+\infty$. For $T\geq0$ define
\[
 B_w(T)=\int_T^\infty(1+t)^{r_n}(-w'(t))\,\mathrm{d}t.
\]
Assume $B_w(0)<+\infty$. For nonpositive $u\in\PSH(X,\omega)$, the damped measures
$\nu_{w,u}=w(-u)\mu_u$ satisfy
\[
 \nu_{w,u}(X)\leq C_\omega B_w(0),\qquad
 \nu_{w,u}(\{u<-T\})\leq C_\omega B_w(T).
\]
For every Borel set $E$ and $T\geq0$,
\[
 \nu_{w,u}(E)\leq
 w(0)(1+T)^n\operatorname{Cap}_\omega(E)+C_\omega B_w(T).
\]
In particular, these measures are uniformly absolutely continuous with respect to capacity. If nonpositive $u_j,u\in\PSH(X,\omega)$ satisfy $u_j\to u$ in capacity, then $\nu_{w,u_j}\rightharpoonup\nu_{w,u}$.
\end{theorem}
\Needspace{6\baselineskip}
\begin{proof}
Write $s=-u$. Since $w(s)=\int_s^\infty(-w'(t))\,\mathrm{d}t$ for finite $s$, and since $\mu_u$ does not charge the pole set $\{s=+\infty\}$, Tonelli's theorem and \cref{lem:sublevel-mass-growth} give
\[
 \int_X w(s)\,\mathrm{d}\mu_u
 =\int_0^\infty(-w'(t))\mu_u(\{s\leq t\})\,\mathrm{d}t
 \leq C_\omega B_w(0).
\]
Restricting the integral to $\{s>T\}$ gives the same bound with $B_w(T)$ in place of $B_w(0)$, since the inner set is then $\{T<s\leq t\}$, which is empty unless $t>T$.

For the capacity bound, the second estimate in \eqref{eq:restricted-mass-growth} gives
\[
 \int_{E\cap\{s\leq T\}}w(s)\,\mathrm{d}\mu_u
 \leq w(0)(1+T)^n\operatorname{Cap}_\omega(E).
\]
Adding the tail estimate for $\{s>T\}$ proves the asserted bound. Since $B_w(T)\to0$, choosing first $T$ large and then the capacity small gives uniform absolute continuity.

To prove continuity, fix a continuous nonincreasing $\eta:[0,+\infty)\to[0,1]$, equal to one on $[0,1]$ and zero on $[2,+\infty)$, and put $\eta_T(s)=\eta(s/T)$. For fixed $T>0$, set $v_{j,T}=\max(u_j,-2T)$ and $g_T(t)=\eta_T(-t)w(-t)$ on $[-2T,0]$. Since $g_T(-2T)=0$, locality gives
\begin{equation}\label{eq:weighted-truncation-identity}
 \eta_T(-u_j)w(-u_j)\mu_{u_j}
 =g_T(v_{j,T})\,\mathrm{MA}_\omega(v_{j,T}).
\end{equation}
Truncation preserves convergence in capacity. The functions $g_T(v_{j,T})$ are uniformly bounded and quasi-continuous, and they converge in capacity to the corresponding function for $u$. The weighted continuity of bounded products in \cref{sec:psh-local-capacity,sec:hermitian-capacity} therefore gives weak convergence of the measures in \eqref{eq:weighted-truncation-identity} for each fixed $T$. The measure $(1-\eta_T(-u_j))\nu_{w,u_j}$ is carried by $\{u_j<-T\}$, so by the tail bound its integral against a continuous test function $f$ is at most $C_\omega B_w(T)\|f\|_\infty$, uniformly in $j$; the same holds for $u$. Letting $T\to\infty$ completes the proof.
\end{proof}

For $w(t)=\mathrm{e}^{-pt}$, $p>0$, the integral $B_w(0)$ is finite because the exponential dominates the polynomial factor. Thus the exponentially damped measures of \cref{thm:exponential-damping} are continuous under convergence in capacity. By that theorem, their tails also satisfy
\[
 \nu_{p,u}(\{u<-T\})
 \leq\mathrm{e}^{-pT/2}\nu_{p/2,u}(X)
 \leq C_p\mathrm{e}^{-pT/2}.
\]
For polynomial weights, the general estimate takes the following explicit form.

