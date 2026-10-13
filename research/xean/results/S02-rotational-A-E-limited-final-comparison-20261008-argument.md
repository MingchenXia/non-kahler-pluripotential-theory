# Final independent comparison of the restricted S02 rotational A--E theorem

Assess every author proof, every independently reconstructed proof and their complete dependency chain. The current author source controls the proposed statement. The original unrestricted review remains INCONCLUSIVE and its four invalid historical task bindings remain unchanged; create exact new bindings under this limited task. No candidate flag, historical verdict or source-read record is a proof premise. No original S02 completion or unrestricted sufficient square-root theorem follows.

Harmless historical clarification: the old smooth-core note negative-slope expression sup[-(W_eta)_x]_- must read sup[(W_eta)_x]_-. The current article has the correct sign. For the bounded tail proof at T=0 use the total estimate; at T>0 choose0<delta<T. No Q at a negative depth is invoked. Independently check both explanations.


## Complete current author source

```latex
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

```


## Complete historical author proof packet, unchanged

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



## Complete unchanged original-task public review

```json
{
  "verdict": "INCONCLUSIVE",
  "report": "The original unrestricted optimal-damping task is not completed. The independently checked argument establishes A–E on the full declared rotational class R, together with obstructions for the unrestricted class. It supplies no sharp sufficient condition for arbitrary potentials. This is substantial partial progress, not a complete resolution under the supplied completion criterion. No substantive mathematical defect was found in the restricted proof.\n\nThe normalization and smooth formulas check out. Both the Xia–Zhang background and operator are divided by 2π, leaving scalar potentials unchanged. Direct differentiation gives the stated matrix, including the semipositive case without dividing by the vertical coefficient. The normalized radial density and fiber area give MAω(V)=12AΔ dx dΩ dA. The endpoint assumptions of the source's extension lemma are used for the constructed family; the local matrix calculation applies to arbitrary smooth invariant potentials at finite x. [Xia–Zhang](https://arxiv.org/html/2608.21053v1).\n\nThe new upper estimate is valid. Periodic integration gives ∫EΔ=m″+μ(1−μ)−e″/2. Fiber means and vertical Dirichlet integrals are smooth functions on the base, so m′ and e′ tend to zero at both radial ends. Consequently the nonnegative flux integrates to exactly one. Semipositivity gives Vxx≥−1; applying the resulting semiconvex inequality with displacement Vx and using V≤0 proves |Vx|²≤−2V. These facts give precisely 12Q(W) and 12QT(W), without assuming bounded unweighted mass or pointwise fiber constancy at the positive end.\n\nThe faster heat scale is admissible. The square estimate's hypotheses hold on each indicated transport region, including its application with κχ²; χ=0 is handled separately. At the new scale, the integrated defect is O(ℓ)+o(1), rather than o(1), and choosing the fixed c sufficiently small supplies all correction margins. The terminal cutoff error remains smaller than the background radial positivity because ℓ<1/(10e). The correction controls both the radial Schur complement and the tangential coefficient. Smooth extension and normalization follow from the actual endpoint behavior and the fiber mean. On the core, the completed square tends uniformly to one, the other negative terms are controlled, and the exact annular area is 3t/2. Thus the actual smooth measure has mass at least Dη⁻¹ at depths between Aη⁻² and Bη⁻². Matching T=Bη⁻² proves the necessary conditions for general decreasing weights, without regular-variation assumptions.\n\nThe single infinite-measure construction also checks out. Its correction has uniform local derivative control and the required global slope bound. The constant C* can be fixed before choosing scales. All recursive constraints can then be met at arbitrarily large values of √T W(T). Submean propagation through a finite connected chart cover gives the uniform L¹ bound without BMP. The decreasing series therefore has a genuine canonical quasi-psh limit, retaining the current margin 3ω/4. On every chosen core neighborhood, earlier terms are constant and the future series converges smoothly. The determinant inequality gives the actual local measure bound a_j³MAω(u_j). Normalization decreases depths and hence preserves the weighted lower bounds. Disjoint cores contribute at least one each, proving infinite weighted mass for one admissible potential.\n\nThe capacity argument uses the original capacity throughout. Both local comparisons are valid; the gluing parameters can be chosen sufficiently small to obtain a global test in [−1,0]. Compact central group convolution is smooth by transitivity, preserves the current inequality and rotational invariance, and its capacity convergence follows from the stated Markov argument. For bounded products, the telescoping integrals are controlled by mixed positive measures dominated by local capacity. Every lower degree therefore converges. Expanding against the smooth coefficient γ handles the nonclosed background; γ need not be closed. Quasi-continuity and uniform capacity domination justify the continuous depth weights. The foundational hypotheses match [Bedford–Taylor](https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf); their operator differs by the positive factor 4π, which only rescales capacities and constants. The canonical limiting assertions agree with [Demailly](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf).\n\nCanonical truncations and the task-granted compatible measures extend both upper estimates to every unbounded member of R. The capacity bound follows by splitting at depth T. For continuity, the truncation error is at most 24Q_{K−1}(W), including possible bounded-truncation mass on {u=−K}; no boundary-level mass is discarded.\n\nThe critical counterexample is an actual capacity-convergent sequence. The controlled correction masses tend to m=Kℓ>0. Near H, the limiting function has the local form m log|n|²−m log(1+|ζ|²)+constant, with n normal to H. This proves its genuine logarithmic extension and positive divisor current; the established margins control its smooth part, and its supremum is zero. Away from H, the heat exceptional sets shrink into tubes around the analytic section w=0, whose capacities tend to zero. Removing a small-capacity neighborhood of H proves uη→g in the original capacity. At the bounded critical regime, the full weighted measures are uniformly finite and have weak clusters. Their actual core masses force positive cluster mass on H, whereas νW,g(H)=0. When √t W(t) is unbounded, the single infinite measure obstructs a finite-measure map instead.\n\nAccordingly, on R, individual finiteness and uniform total bounds hold exactly when √t W(t) is bounded; tails, uniform capacity absolute continuity and capacity-to-weak continuity hold exactly when √t W(t)→0. The stated power/logarithmic classifications follow. All necessary obstructions extend to the unrestricted class. Unrestricted sufficiency remains the task-granted integral condition, giving p>1 or p=1,a>1 in the power/logarithmic family; the intervening regimes remain unresolved here. The closed-elliptic diagnostic has consistent normalization and energy calculations, but establishes no additional global Hopf conclusion.\n\nHarmless correction: the historical smooth-core note writes sup[−(Wη)x]₋ for the negative-slope bound. It must read sup[(Wη)x]₋. The current article already has the correct sign and proves that bound. Also, the tail passage at T=0 uses the total estimate directly, rather than an undefined Q_{−δ}. Neither correction changes the restricted argument.",
  "passages": [
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/0",
      "statement": "On the scalar Hopf threefold, with dd^c_src=i∂bar∂ and ω_src=i∂bar∂s+i∂s∧bar∂s, s=log|z|², put ξ=z'/z0, w=log z0, x=log|ξ|² and μ=e^x/(1+e^x). For smooth real V(x,w), its local Hermitian matrix in the α_src-unit tangential, α_src-unit radial and ∂/∂w frame is [[(μ+Vx)/μ,0,0],[0,(μ+Vxx)/(μ(1−μ)),(μ+Vxbarw)/sqrt(μ(1−μ))],[0,(μ+Vwx)/sqrt(μ(1−μ)),1+Vwbarw]]. If V is independent of x for sufficiently negative x and constant in x,w for sufficiently positive x, it extends smoothly globally; positivity at ξ=0 is equivalent to 1+Vwbarw>0. Xia–Zhang, Lemma 2.2.",
      "url": "https://arxiv.org/html/2608.21053v1",
      "quote": "1+V_{w\\bar{w}}>0,\\qquad\\mu+V_{x}>0,\\qquad Q[V]\\coloneqq V_{xx}+\\mu-\\frac{|\\mu+V_{x\\bar{w}}|^{2}}{1+V_{w\\bar{w}}}>0.",
      "premise": 0
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/1",
      "statement": "For E=C/(Z+2πiZ), probability Haar area dA=i dw∧dbarw/(4π), k_t(w)=(2/t)Σλ exp(−|w−λ|²/t), and Fη(t,w)=−η∫t∞(k_r(w)−1)dr, 0<η<1/10, one has Fη,t=Fη,wbarw=η(k_t−1), (log k_t)wbarw≥−1/t, and ||∂t^a Fη(t,·)||C^m≤C_a,m ηe^(−t/4) for t≥1 and fixed nonnegative integers a,m, uniformly in η. Xia–Zhang, Lemma 3.1.",
      "url": "https://arxiv.org/html/2608.21053v1",
      "quote": "(F_{\\eta})_{t}=(F_{\\eta})_{w\\bar{w}}=\\eta(k_{t}-1)",
      "premise": 1
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/2",
      "statement": "For k_t(w)=(2/t)Σλ∈Z+2πiZ exp(−|w−λ|²/t), absolute constants C0≥1 and C exist such that tk_t≤C0 exp(−|t∂barw log k_t|²/(C0t)) for 0<t≤1. If 0<κ<1/(200C0), 0<η<1/10, 0<t≤1, 1/2≤μ≤1, σ=sqrt((2κ/η)log(1/(ηt))), h=ηk_t and ζ=(σ/μ)t∂barw log k_t, then κtk_t−μ²(1−η)h|ζ−(1−η)^−1|²/(1−η+h)≤Cκ exp(−1/(Cσ²t)), uniformly in all these parameters and w. Xia–Zhang, Lemmas 3.2–3.3.",
      "url": "https://arxiv.org/html/2608.21053v1",
      "quote": "\\kappa tk_{t}-\\frac{\\mu^{2}(1-\\eta)h}{1-\\eta+h}\\left|\\zeta-\\frac{1}{1-\\eta}\\right|^{2}\\leq C\\kappa\\exp\\left(-\\frac{1}{C\\sigma^{2}t}\\right).",
      "premise": 2
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/3",
      "statement": "For Ω⊂C^n and locally bounded genuine psh p1,…,pk, k≤n, their Bedford–Taylor mixed product is a positive closed current, local and symmetric multilinear in its arguments, and weakly continuous under simultaneous decreasing locally bounded psh limits. Bedford–Taylor, Theorem 2.1 and Corollary 2.2.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf#page=4",
      "quote": "nonnegative closed currents",
      "premise": 3
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/4",
      "statement": "For locally bounded psh p,q on Ω⊂C^n and compactly supported smooth (n−k,n−k)-forms φ, 1≤k≤n, ∫φ[(dd^cp)^k−(dd^cq)^k]=Σl=0^(k−1)∫(p−q)dd^cφ∧(dd^cp)^l∧(dd^cq)^(k−1−l). Bedford–Taylor, Corollary 2.8 and its mixed-degree integration-by-parts consequence.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf#page=10",
      "quote": "holds for smooth u and v",
      "premise": 4
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/5",
      "statement": "For K compactly contained in Ω⊂C^n, bounded psh p1,…,pk, k≤n, and the Euclidean Kähler form β, ∫K dd^cp1∧⋯∧dd^cpk∧β^(n−k)≤C_K,Ω,k∏i||pi||L∞(Ω). Bedford–Taylor, Theorem 2.10.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf#page=10",
      "quote": "Chern-Levine-Nirenberg estimates",
      "premise": 5
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/6",
      "statement": "On a bounded domain Ω⊂C^n, every genuine psh function is quasi-continuous for relative Bedford–Taylor capacity: for each ε>0 there is an open O⊂Ω with C(O,Ω)<ε such that its restriction to Ω minus O is continuous. Bedford–Taylor, Theorem 3.5.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf#page=14",
      "quote": "Hence, u is continuous",
      "premise": 6
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/7",
      "statement": "On a bounded strongly pseudoconvex domain Ω⊂C^n, every locally pluripolar set has zero outer Bedford–Taylor capacity. Bedford–Taylor, Theorem 6.9.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf#page=25",
      "quote": "sets of outer capacity zero",
      "premise": 7
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/8",
      "statement": "On a bounded strongly pseudoconvex Ω⊂C^n, if compact subsets Kj decrease to K, then C(Kj,Ω) decreases to C(K,Ω); also C*(K,Ω)=C(K,Ω). Bedford–Taylor, Proposition 6.4.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf#page=23",
      "quote": "sequence of compact subsets",
      "premise": 8
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/9",
      "statement": "On an open Ω⊂C^n, a decreasing sequence of genuine psh functions has a genuine locally integrable psh pointwise limit whenever the limit is not identically −∞ on any component. A distribution with positive complex Hessian has a unique locally integrable genuine psh representative. The cone Psh(Ω)∩L1_loc(Ω) is closed in L1_loc, and its L1_loc-bounded subsets are relatively compact. Demailly, I.4.17, I.5.4 and I.5.8–5.9.",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=39",
      "quote": "the limit u = lim uk is plurisubharmonic on Ω.",
      "premise": 9
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/10",
      "statement": "On an open Ω⊂C^n, a decreasing sequence of genuine psh functions has a genuine locally integrable psh pointwise limit whenever the limit is not identically −∞ on any component. A distribution with positive complex Hessian has a unique locally integrable genuine psh representative. The cone Psh(Ω)∩L1_loc(Ω) is closed in L1_loc, and its L1_loc-bounded subsets are relatively compact. Demailly, I.4.17, I.5.4 and I.5.8–5.9.",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=40",
      "quote": "there exists a unique function",
      "premise": 9
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/11",
      "statement": "On an open Ω⊂C^n, a decreasing sequence of genuine psh functions has a genuine locally integrable psh pointwise limit whenever the limit is not identically −∞ on any component. A distribution with positive complex Hessian has a unique locally integrable genuine psh representative. The cone Psh(Ω)∩L1_loc(Ω) is closed in L1_loc, and its L1_loc-bounded subsets are relatively compact. Demailly, I.4.17, I.5.4 and I.5.8–5.9.",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=40",
      "quote": "every bounded subset is relatively compact.",
      "premise": 9
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/12",
      "statement": "On an open Ω⊂C^n, a decreasing sequence of genuine psh functions has a genuine locally integrable psh pointwise limit whenever the limit is not identically −∞ on any component. A distribution with positive complex Hessian has a unique locally integrable genuine psh representative. The cone Psh(Ω)∩L1_loc(Ω) is closed in L1_loc, and its L1_loc-bounded subsets are relatively compact. Demailly, I.4.17, I.5.4 and I.5.8–5.9.",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=35",
      "quote": "loc(Ω).",
      "premise": 9
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/13",
      "statement": "On the scalar Hopf threefold, with dd^c_src=i∂bar∂ and ω_src=i∂bar∂s+i∂s∧bar∂s, s=log|z|², put ξ=z'/z0, w=log z0, x=log|ξ|² and μ=e^x/(1+e^x). For smooth real V(x,w), its local Hermitian matrix in the α_src-unit tangential, α_src-unit radial and ∂/∂w frame is [[(μ+Vx)/μ,0,0],[0,(μ+Vxx)/(μ(1−μ)),(μ+Vxbarw)/sqrt(μ(1−μ))],[0,(μ+Vwx)/sqrt(μ(1−μ)),1+Vwbarw]]. If V is independent of x for sufficiently negative x and constant in x,w for sufficiently positive x, it extends smoothly globally; positivity at ξ=0 is equivalent to 1+Vwbarw>0. Xia–Zhang, Lemma 2.2.",
      "url": "urn:xean:task",
      "quote": "These forms descend, omega is positive Hermitian, alpha=pi^*omega_FS for the projectivization pi:X->CP^2, int_CP2 omega_FS^2=1, dd^c beta=-alpha^2, dd^c omega^2=0 and int_X omega^3=6.",
      "premise": 0
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/14",
      "statement": "For Ω⊂C^n and locally bounded genuine psh p1,…,pk, k≤n, their Bedford–Taylor mixed product is a positive closed current, local and symmetric multilinear in its arguments, and weakly continuous under simultaneous decreasing locally bounded psh limits. Bedford–Taylor, Theorem 2.1 and Corollary 2.2.",
      "url": "urn:xean:task",
      "quote": "Define its extended non-pluripolar measure mu_u=MA_ext_omega(u) by the increasing compatible measures 1_{u>-k}(omega+dd^c max(u,-k))^3; the product for bounded quasi-psh functions is the local Bedford--Taylor expansion against the smooth background. The pole set has measure zero, and total mass is allowed to be infinite.",
      "premise": 3
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/15",
      "statement": "On a bounded domain Ω⊂C^n, every genuine psh function is quasi-continuous for relative Bedford–Taylor capacity: for each ε>0 there is an open O⊂Ω with C(O,Ω)<ε such that its restriction to Ω minus O is continuous. Bedford–Taylor, Theorem 3.5.",
      "url": "urn:xean:task",
      "quote": "The known restricted-depth bound is mu_u({u>=-T})<=C(1+T), and mu_u(A intersect {u>=-T})<=(1+T)^3 Cap_omega(A). The general damping theorem therefore gives all four properties when int_0^infinity(1+t)(-W'(t))dt<infinity.",
      "premise": 6
    },
    {
      "id": "9965c975-fe36-4afe-bc4b-6e4497be8235/16",
      "statement": "On a bounded strongly pseudoconvex Ω⊂C^n, if compact subsets Kj decrease to K, then C(Kj,Ω) decreases to C(K,Ω); also C*(K,Ω)=C(K,Ω). Bedford–Taylor, Proposition 6.4.",
      "url": "urn:xean:task",
      "quote": "If only a restricted family or one-sided result is proved, preserve it as partial progress and do not accept it as a complete resolution of the optimal-rate task.",
      "premise": 8
    }
  ],
  "premises": [
    "On the scalar Hopf threefold, with dd^c_src=i∂bar∂ and ω_src=i∂bar∂s+i∂s∧bar∂s, s=log|z|², put ξ=z'/z0, w=log z0, x=log|ξ|² and μ=e^x/(1+e^x). For smooth real V(x,w), its local Hermitian matrix in the α_src-unit tangential, α_src-unit radial and ∂/∂w frame is [[(μ+Vx)/μ,0,0],[0,(μ+Vxx)/(μ(1−μ)),(μ+Vxbarw)/sqrt(μ(1−μ))],[0,(μ+Vwx)/sqrt(μ(1−μ)),1+Vwbarw]]. If V is independent of x for sufficiently negative x and constant in x,w for sufficiently positive x, it extends smoothly globally; positivity at ξ=0 is equivalent to 1+Vwbarw>0. Xia–Zhang, Lemma 2.2.",
    "For E=C/(Z+2πiZ), probability Haar area dA=i dw∧dbarw/(4π), k_t(w)=(2/t)Σλ exp(−|w−λ|²/t), and Fη(t,w)=−η∫t∞(k_r(w)−1)dr, 0<η<1/10, one has Fη,t=Fη,wbarw=η(k_t−1), (log k_t)wbarw≥−1/t, and ||∂t^a Fη(t,·)||C^m≤C_a,m ηe^(−t/4) for t≥1 and fixed nonnegative integers a,m, uniformly in η. Xia–Zhang, Lemma 3.1.",
    "For k_t(w)=(2/t)Σλ∈Z+2πiZ exp(−|w−λ|²/t), absolute constants C0≥1 and C exist such that tk_t≤C0 exp(−|t∂barw log k_t|²/(C0t)) for 0<t≤1. If 0<κ<1/(200C0), 0<η<1/10, 0<t≤1, 1/2≤μ≤1, σ=sqrt((2κ/η)log(1/(ηt))), h=ηk_t and ζ=(σ/μ)t∂barw log k_t, then κtk_t−μ²(1−η)h|ζ−(1−η)^−1|²/(1−η+h)≤Cκ exp(−1/(Cσ²t)), uniformly in all these parameters and w. Xia–Zhang, Lemmas 3.2–3.3.",
    "For Ω⊂C^n and locally bounded genuine psh p1,…,pk, k≤n, their Bedford–Taylor mixed product is a positive closed current, local and symmetric multilinear in its arguments, and weakly continuous under simultaneous decreasing locally bounded psh limits. Bedford–Taylor, Theorem 2.1 and Corollary 2.2.",
    "For locally bounded psh p,q on Ω⊂C^n and compactly supported smooth (n−k,n−k)-forms φ, 1≤k≤n, ∫φ[(dd^cp)^k−(dd^cq)^k]=Σl=0^(k−1)∫(p−q)dd^cφ∧(dd^cp)^l∧(dd^cq)^(k−1−l). Bedford–Taylor, Corollary 2.8 and its mixed-degree integration-by-parts consequence.",
    "For K compactly contained in Ω⊂C^n, bounded psh p1,…,pk, k≤n, and the Euclidean Kähler form β, ∫K dd^cp1∧⋯∧dd^cpk∧β^(n−k)≤C_K,Ω,k∏i||pi||L∞(Ω). Bedford–Taylor, Theorem 2.10.",
    "On a bounded domain Ω⊂C^n, every genuine psh function is quasi-continuous for relative Bedford–Taylor capacity: for each ε>0 there is an open O⊂Ω with C(O,Ω)<ε such that its restriction to Ω minus O is continuous. Bedford–Taylor, Theorem 3.5.",
    "On a bounded strongly pseudoconvex domain Ω⊂C^n, every locally pluripolar set has zero outer Bedford–Taylor capacity. Bedford–Taylor, Theorem 6.9.",
    "On a bounded strongly pseudoconvex Ω⊂C^n, if compact subsets Kj decrease to K, then C(Kj,Ω) decreases to C(K,Ω); also C*(K,Ω)=C(K,Ω). Bedford–Taylor, Proposition 6.4.",
    "On an open Ω⊂C^n, a decreasing sequence of genuine psh functions has a genuine locally integrable psh pointwise limit whenever the limit is not identically −∞ on any component. A distribution with positive complex Hessian has a unique locally integrable genuine psh representative. The cone Psh(Ω)∩L1_loc(Ω) is closed in L1_loc, and its L1_loc-bounded subsets are relatively compact. Demailly, I.4.17, I.5.4 and I.5.8–5.9."
  ],
  "kind": "codex-report",
  "operationId": "9965c975-fe36-4afe-bc4b-6e4497be8235",
  "reportedAt": "2026-10-08T11:09:20.682Z"
}

```


## Every complete independently reconstructed public proof and its metadata

```json
{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "For the entire U(2)-invariant class R, a rotational determinant budget proves the exact bounds 12Q(W), 12Q_T(W), and the requested original-capacity estimate. It proves all sufficient directions in A–D, including unbounded potentials. No unrestricted upper bound is established.",
      "detailedSummary": "Derives the positivity matrix and cubic density 12(mu+u_x)D, proves that D has integral 1 for arbitrary smooth invariant endpoint behavior, and bounds mu+u_x by 1+sqrt(2(-u)). Smooth approximation preserving invariance and positivity, bounded Bedford–Taylor convergence, and compatible strict truncations extend the resulting budget to all of R. Retains depth level sets and proves capacity-to-weak continuity when sqrt(t)W(t) tends to zero. States and checks the local primary Bedford–Taylor hypotheses and their transfer to the original Hermitian capacity.",
      "text": "Scope. This proof concerns the ENTIRE U(2)-invariant class R, including unbounded genuine quasi-psh potentials. It does not reduce arbitrary potentials to R.\n\nLocal product and capacity facts. The foundational premises used are local Bedford–Taylor multilinearity, locality, quasicontinuity, and outer-capacity zero of pluripolar sets. The primary source inspected was Bedford–Taylor, A new capacity for plurisubharmonic functions, Acta Math. 149 (1982), 1–40, DOI https://doi.org/10.1007/BF02392348, author copy https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf. The indispensable statements are Theorem 2.1 and Corollary 2.2 for locally bounded psh products, Theorem 3.5 for quasicontinuity, and Theorem 6.9 for outer capacity zero. These are local statements on coordinate balls and require no Kähler assumption on X. Their convention dd^c=2i∂bar∂ changes positive normalization constants, but not capacity zero sets or convergence.\n\nHere are the transfers needed for the ORIGINAL capacity. On a coordinate ball choose ρ=M|z|² with dd^cρ≥ω. For an original competitor −1≤v≤0,\n0≤(ω+dd^cv)³≤(dd^c(v+ρ))³.\nRescaling the bounded local range bounds original capacity by a constant times a finite sum of local capacities on a double cover. Conversely, for a local psh competitor −1≤h≤0, glue λh−a|z|² to a constant by max. Choose a>0 with ω−dd^c(a|z|²)>0 and λ small relative to the annular gap a(R²−r²). The h branch is active on the smaller ball and the constant branch near the outer boundary. The global glued function can be shifted into [−1,0]; its cube dominates λ³(dd^ch)³ on the smaller ball. This gives the reverse local capacity bound. Consequently local quasicontinuity and arbitrarily small-capacity neighborhoods of compact analytic sets hold for Cap_ω.\n\nFor uniformly bounded quasi-psh b_j→b in capacity, add ρ locally. Positive mixed trace measures of their dd^c products are bounded by C times local capacity: include |z|² among the bounded psh summands, expand the cube of their sum, and rescale. Telescope a difference of mixed products and integrate by parts against a smooth test form. Each term is bounded by Cδ+C Cap({|b_j−b|>δ}). This proves weak convergence of mixed products. Expansion against the smooth remainder ω−dd^cρ proves bounded Hermitian-product convergence. If F is a bounded continuous scalar function, F(b_j) also converges in capacity. Approximate the fixed quasicontinuous F(b) continuously outside an open set of small capacity. Uniform capacity domination then proves weighted bounded-product convergence. Uniform boundedness is essential at this step.\n\nRotational coordinates. Off z₀=0 put ξ=z′/z₀, w=log z₀ modulo Z+2πiZ, x=log|ξ|², L=log(1+eˣ), and μ=L′=eˣ/(1+eˣ). Every smooth invariant potential has the form U(x,w); no independence of w or its phase is assumed. With c=i/(2π),\nα=c[μ∂bar∂x+μ(1−μ)∂x∧bar∂x],\nβ=c(dw+μ∂x)∧(dbar w+μbar∂x).\nThe angular coefficient is a=μ+U_x. The remaining radial/fiber block in the coframe (∂x,dw) is\n[[μ+U_xx, μ+U_xbarw],[μ+U_wx, 1+U_wbarw]].\nSet ρ=1+U_wbarw and D=(μ+U_xx)ρ−|μ+U_xbarw|². Positivity gives a≥0, ρ≥0, μ+U_xx≥0, and D≥0.\n\nAfter angular disintegration with probability measure, the exact cubic pushforward density is 12aD dx dA_E. Indeed ω_FS² has radial density 2μμ′dx, β restricts to 2dA_E, and ω³ has density 12μ²(1−μ)dx dA_E. The relative determinant is (a/μ)D/[μ(1−μ)], giving coefficient 12 and background mass 6.\n\nLet E(x)=∫_E|U_w|²dA_E and bar U=∫_EUdA_E. Periodic integration by parts yields\n∫_EDdA_E=μ′+(bar U)″−E″/2.\nThe two quadratic derivative terms combine as ∫U_xxU_wbarw−∫|U_xbarw|²=−E″/2; the remaining fiber derivative terms integrate to zero. At x→−∞, smooth invariance gives U=U₀(w)+O(eˣ), with the required derivatives. At x→+∞, smoothness on z₀=0 and invariance give U=h(x+w+bar w)+O(e^(−x/2)), where h has period 2. Thus (bar U)′ and E′ tend to zero at both ends. Therefore\n∫_{R×E}D dx dA_E=1.  (1)\nSmooth invariant potentials need not be constant at the ends.\n\nNormalization produces the square root. If U≤0 and U_x>0, the inequality U_xx≥−μ≥−1 along the forward x-ray gives\nU(x+h,w)≥U(x,w)+hU_x(x,w)−h²/2.\nTake h=U_x and use U(x+h,w)≤0. Hence U_x≤sqrt(−2U), and always\n0≤a≤1+sqrt(2(−U)).\nCombining this with (1) proves\n∫_X (ω+dd^cU)³/[1+sqrt(2(−U))]≤12.  (2)\n\nExtension to bounded and unbounded R. The compact group G=U(3) times the real scaling circle acts transitively by holomorphic ω-isometries. Average a bounded u against smooth probability approximate identities on G, invariant under conjugation by H=diag(1,U(2)). The averages are smooth, ω-psh, H invariant, and in the same bounded range. Smoothness follows by lifting to G and differentiating the convolution kernel.\n\nThey converge in original capacity. Extend u continuously outside an open set O of small capacity. Translates of O have identical capacity. For every original competitor measure, the integral of the translation error is bounded by the uniform continuous error times its bounded total mass plus 4||u||∞Cap(O). Chebyshev and the supremum over competitors prove capacity convergence of the averages. Their suprema tend to zero: otherwise an L¹-convergent subsequence would have limit ≤−ε almost everywhere, hence everywhere in its canonical representative, contradicting sup u=0. Normalize the averages. Bounded weighted-product convergence passes (2) to every bounded u∈R.\n\nFor unbounded u use u^k=max(u,−k). Restrict (2) to {u>−k}, where u^k=u and the product is the compatible measure specified in the question. Monotone convergence of these restricted measures gives, for EVERY u∈R,\n∫_X dμ_u/[1+sqrt(2(−u))]≤12.  (3)\nThe pole set is excluded as prescribed. No unrestricted full product of an unbounded potential is introduced.\n\nConsequently, for the specified Q and Q_T,\nν_W,u(X)≤12Q(W),\nν_W,u({−u>T})≤12Q_T(W).  (4)\nThese hold for every T≥0, including infinite right sides. Boundedness of sqrt(t)W(t) at infinity makes Q finite; its convergence to zero makes Q_T→0.\n\nDepth levels and capacity. For −K≤v≤0,\nω+dd^cv≤(1+K)(ω+dd^c(v/(1+K))),\nso its cube on A is at most (1+K)³Cap_ω(A). On {u≥−T}, use u^(T+ε): the ENTIRE set, including {u=−T}, lies strictly above its floor. Locality followed by ε↓0 gives\nμ_u(A∩{u≥−T})≤(1+T)³Cap_ω(A).\nSplitting at depth T proves exactly\nν_W,u(A)≤W(0)(1+T)³Cap_ω(A)+12Q_T(W).  (5)\nThus Q_T→0 implies uniform absolute continuity for the original capacity.\n\nContinuity. Suppose sqrt(t)W(t)→0 and u_j→u in original capacity in R. Choose a continuous cutoff χ_T(t), equal to 1 for t≤T and zero for t≥T+1. The measures χ_T(−u_j)W(−u_j)μ_uj are products of max(u_j,−T−2) multiplied by a continuous scalar function vanishing at the truncation floor. Locality therefore handles all intermediate levels, and the bounded weighted convergence proved above applies. The omitted mass is uniformly ≤12Q_T. Letting T→∞ proves ν_W,uj→ν_W,u weakly.\n\nEvidence and artifacts. The full saved note is proof_n1.txt. The light exact symbolic program verify_identities.py checks the completed-square identity used in n2, determinant rewriting, cubic coefficient 12, and fiber-averaged algebra. Rerun: python verify_identities.py > verification_output.txt. All four checks report PASS. They verify algebra, not the analytic proof or its limits. This is an unverified mathematical proof draft; necessity is supplied in n2–n3.\n\nArtifacts: /workspace/research/native-workers/codex-DZRZMb",
      "support": []
    },
    {
      "id": "n2",
      "summary": "Actual smooth invariant potentials have depth comparable to η⁻² and mass at least cη⁻¹ on small-capacity annuli approaching z₀=0. They prove failed tails and absolute continuity, and a finite divisor-charging weak cluster when sqrt(t)W(t) is bounded but nonvanishing.",
      "detailedSummary": "Reconstructs the heat estimates, positivity correction and canonical normalization at the new scale q₀ proportional to η⁻³⁄². Computes actual deep annular Monge–Ampère mass. Proves original-capacity convergence to a genuine normalized radial potential with analytic pole divisor, and computes its extended measure and nonzero bounded-truncation floor mass exactly. These examples establish the necessary directions of B–D; no finite weak cluster is asserted for the unbounded square-root regime.",
      "text": "Uses n1. The primary normalization was checked against Xia–Zhang, https://arxiv.org/html/2608.21053v1, sections 2.1–2.4. Their dd^c=i∂bar∂ and background form are 2π times ours, as is their base Fubini–Study form. Dividing their smooth identity by (2π)³ gives coefficient 6 with our probability fiber area. The following proof reconstructs positivity and weighted depth estimates; BMP failure alone supplies no weighted obstruction.\n\nHeat estimates. For Λ=Z+2πiZ define\nk_t(w)=(2/t)Σ_λ exp(−|w−λ|²/t),\nF_η(t,w)=−η∫_t^∞(k_r(w)−1)dr.\nGaussian unfolding gives ∫_Ek_t dA_E=1. Fourier coefficients are exp(−[π²p²+q²/4]t), so ∂_tk_t=∂_w∂_barw k_t and k_t→1 exponentially in every derivative for t≥1. Hence\nF_t=F_wbarw=η(k_t−1),\n||∂_t^aF||_{C^b}≤C_abηe^(−t/4), t≥1.  (6)\nAll differentiations are justified by Gaussian/Fourier convergence for t≥t₀>0. Differentiating the weighted Gaussian mean gives the variance inequality\n(log k_t)_wbarw≥−1/t.  (7)\nWriting d=dist_E(w,0), uniformly in t>0,\nsup F_η≤Cη,\nF_η(t,w)≥−2ηlog⁺(1/(d²+t))−Cη.  (8)\nFor t≤1, isolate the nearest Gaussian in ∫_t^1k_rdr; the remaining terms contribute O(1), and ∫_t^1r⁻¹e^(−d²/r)dr≤log⁺(1/(d²+t))+C. For t≥1 use (6). Uniformly for 1≤|ζ|≤2 and w=sqrt(t)ζ,\nF_η(t,w)=−2ηlog(1/t)+O(η),\ntk_t(w)=2e^(−|ζ|²)+o(1).  (9)\nDifferentiated estimates also hold; other lattice terms are exponentially small in 1/t.\n\nA necessary Gaussian gradient estimate is\n tk_t≤C₀exp(−|t∂_barw log k_t|²/(C₀t)), 0<t≤1.  (10)\nHere is a proof. Choose a nearest λ₀, d=|w−λ₀|, and s_λ=|w−λ|²−d². Then s_λ≥0 and s_λ≥|λ−λ₀|²/4−C. Thus Σe^(−s_λ/t) and its distance-weighted version are bounded. For d≥1/4 the mean distance is ≤Cd. For d<1/4, all nonnearest terms have a fixed gap and contribute O(e^(−c/t)). Therefore G=|t∂_barw log k_t|≤C(d+e^(−c/t)), while tk_t≤Ce^(−d²/t). If G≤2Ce^(−c/t), G²/t is bounded; otherwise d≥G/(2C). Both cases give (10).\n\nFix κ>0 sufficiently small. For μ∈[1/2,1], q²=log(1/(ηt)), σ=sqrt(2κq²/η), h=ηk_t and ζ=(σ/μ)t∂_barw log k_t, one obtains\nκtk_t−[μ²(1−η)h/(1−η+h)]|ζ−1/(1−η)|²\n≤Cκexp(−1/(Cσ²t)).  (11)\nTo check this, split at σ²t=1/100. Above this threshold use tk_t≤C₀. Below it, when |ζ−1/(1−η)|≥1/4, the square is ≥h/[100(1+h)], while κt(1+h)≤η/400+C₀κη<η/100, using q²>2 and small κ. This absorbs κtk_t. In the remaining case |ζ|≥3/4, so G≥3/(8σ) and (10) gives the exponential bound. The argument also holds for 0<κ′≤κ; κ′=0 is direct.\n\nSharp scale. Choose a smooth nonnegative probability density ψ supported in (−2,−1). Fix ℓ>0 sufficiently small that ℓ<1/(10e), 3ℓ<μ(−2)/4, and 3ℓ||ψ||∞<1/100. Let χ be smooth nondecreasing, zero on (−∞,0], one on [1,∞), with ∫₀¹χ=1/2; a symmetric smooth bump constructs it. Let θ be a smooth flat cutoff from 0 to 1. Put\na_η=sqrt(κ/(2η)), q₀=a_ηℓ/η,\nq(x)=q₀−∫₀^(a_ηx)χ(s)ds, t(x)=η⁻¹e^(−q(x)²),\nb=(q₀−1/2)/a_η, x*= (q₀+1/2)/a_η,\nH_η(x,w)=θ(q(x))F_η(t(x),w).\nThis is independent of x for x≤0 and zero for x≥x*. The sharp scale is b∼ℓ/η and q₀²=κℓ²/(2η³).\n\nPositivity correction. Define Q[V]=V_xx+μ−|μ+V_xbarw|²/(1+V_wbarw). On q≥1 let σ=(log t)_x. Differentiation and completion of a square give the exact identity\nQ[H]=σ²t{h[1+t(log k_t)_wbarw]−η}+σ_xt(h−η)\n +μ(1−μ)−μ²η/(1−η)\n +[μ²(1−η)h/(1−η+h)]|ζ−1/(1−η)|².  (12)\nThis identity is checked symbolically by the saved program. On x≥1/a_η, q≥1, σ=2a_ηq and σ_x=−κ/η. For t≤1, (7), (11), and (12) imply\n[Q[H]]_-≤2η+2κq²t+Cκexp(−η/(Cκq²t)).  (13)\nFor t≥1, (6) gives [Q[H]]_-≤Cκq²t²e^(−t/4). On 0≤x≤1/a_η use κχ² in (11); the additional σ_x term is bounded below by −κqχ′t. Since t≤η⁻¹exp(−(q₀−1/2)²), the negative part there is Cη.\n\nAll error integrals tend to zero at this new scale. Use dx=−dq/a_η. With R=sqrt(log(1/η)), the q²t error integrates to O(sqrt(η)R), from ∫_R^∞q²e^(−q²)dq≤CRe^(−R²). For the exponential error split at 2R: the first part is O(sqrt(η)R), while on the second η²e^(q²)/q²≥e^(q²/4), giving an integrable bound independent of q₀. For t≥1 use dx=sqrt(η/(2κ))dt/(tq), giving O(sqrt(ηlog(1/η))). The initial interval contributes O(η^(3/2)). Only 2η has a nonvanishing integral, ≤2ℓ+o(1). Also sup[H_x]_-≤Csqrt(ηlog(1/η))=o(1).\n\nOn b≤x≤x*, t≥1/(eη). Perturbations of Q[0]=μ(1−μ) are bounded by Ce^(−1/(5eη)). Since x*=ℓ/η+O(sqrt η), they are o(e^(−x*)); thus Q[H]>0 there. For x≤0, μ≤1/2 and 1+H_wbarw≥1−η give Q[H]>0. For x≥x* it is positive automatically. On [−2,−1] it is uniformly ≥2/27 for small η.\n\nLet d_η(x)=max_w[Q[H_η]]_-. Choose a smooth nonnegative majorant r_η, supported in (−1/2,b+1/2), strictly larger than d_η on [0,b], with\nm_η=∫r_ηdx→m=3ℓ,\nand r_η→0 smoothly on compact subintervals of (0,∞). This is a constructive smooth-majorant choice: start with a 3η plateau equal to 3η on [0,b], with bounded-length endpoint ramps. Add smooth majorants of the errors in (13) and the initial interval, of total integral o(1). Local mollification and a small positive bump give strict majorants with arbitrarily close integrals. On fixed positive compact intervals the errors and all derivatives are superpolynomially small, and the majorants can retain this property. Hence m_η=3ηb+o(1)=3ℓ+o(1).\n\nSet\nG_η(x)=∫_−∞^x(x−s)[r_η(s)−m_ηψ(s)]ds,\nV_η=H_η+G_η, v_η=V_η−sup_XV_η.\nThen −m_η≤G_η′≤0, G_η is zero at the negative end and constant at the positive end. Furthermore Q[V_η]=Q[H_η]+r_η−m_ηψ>0: strict majorization handles [0,b], the 2/27 bound handles supp ψ, and the correction elsewhere is nonnegative. The angular inequality μ+V_η,x>0 follows below −2 from the vanishing correction, on [−2,0] from μ≥μ(−2)>m_η, and above zero from μ≥1/2, the o(1) negative slope, and small m_η. Finally 1+V_η,wbarw≥1−η>0. The matrix in n1 proves strict positivity globally. Independence of x at ξ=0 and constancy near z₀=0 give smooth extension across both omitted loci. The functions are genuinely normalized and invariant. Since the negative-end fiber has mean zero and sup F≤Cη, 0≤sup V_η≤Cη.\n\nActual depth and mass. There are fixed 0<c₀<C₀ and c₁>0 such that, for sufficiently small η,\n0≤−v_η≤C₀/η² on X,\nc₀/η²≤−v_η≤C₀/η² on A_η,\nμ_vη(A_η)≥c₁/η,  (14)\nwhere the ACTUAL set A_η is defined by\nb/4≤x≤b/2, sqrt(t(x))≤dist_E(w,0)≤2sqrt(t(x)),\nwith all angular variables allowed. These annuli lie inside the injectivity disk. Here q/q₀ is between 1/2+o(1) and 3/4+o(1), and t is exponentially small in η⁻³. Formula (9) gives depth 2ηq²+O(ηlog(1/η))+O(1/η). The global upper bound follows from (8) and |G_η|≤m_η(b+3)=O(1/η).\n\nWriting w=sqrt(t)ζ on the annulus, H_x=2ησe^(−|ζ|²)(1+o(1)), hence μ+V_η,x≥c/η. Also ρ≥cη/t. In (12), σsqrt(t)→0, μ→1, and Q[H] tends uniformly to 1−2κe^(−|ζ|²), which is ≥1/2. The r correction improves Q and ψ vanishes there. Thus D=ρQ≥cη/t. The actual density 12aD integrates over the annulus of area comparable to t to at least c per unit x. Its x-length is comparable to η⁻¹, proving (14). This calculation does not substitute total mass divergence for deep-set mass.\n\nCapacity limit. A_η⊂{x≥b/4}, so it approaches the analytic divisor D₀={z₀=0}; its ORIGINAL capacity tends to zero by n1. Define H_ψ(x)=∫_−∞^x(x−s)ψ(s)ds and\n g(x)=−mH_ψ(x), g|D₀=−∞, m=3ℓ.  (15)\nIt equals 0 for x≤−2 and −mx+constant for x≥−1. Near D₀ it is −mL plus a smooth function, giving the positive current term m[D₀]. Away from D₀, positivity is the radial criterion a_g=μ+g′≥0 and a_g′=μ′−mψ≥0, ensured by the chosen small ℓ. Thus g is genuine global quasi-psh, canonically −∞ on D₀, and normalized with supremum zero.\n\nOn every compact affine region G_η→g uniformly, while H_η→0 uniformly away from {w=0}. Remove an arbitrarily small original-capacity neighborhood of the compact analytic portion {w=0}, and one of D₀. On the complement v_η→g uniformly. Hence v_η→g in ORIGINAL capacity, including ξ=0. Pointwise divergence at w=0 is not used to modify g’s canonical finite value there.\n\nExact extended product and floor levels. Away from D₀, g is radial and its cube has pushforward density 12a_ga_g′dx dA_E. Therefore μ_g(X)=6(1−m)² and μ_g(D₀)=0. For large k let x_k solve g(x_k)=−k, so x_k>−1. For g^k=max(g,−k), a equals μ−m to the left and μ to the right, with an upward jump m. Smooth convex regularizations of max are positive radial potentials, converge uniformly, and their pushforward cubes are 6d(a²). Bounded BT convergence gives the EXACT boundary mass\n(ω+dd^cg^k)³({x=x_k})=6[μ(x_k)²−(μ(x_k)−m)²].  (16)\nThe floor interior x>x_k has additional mass 6[1−μ(x_k)²]. Thus the entire level {g^k=−k} has mass 6[1−(μ(x_k)−m)²]. In contrast μ_g({g=−k})=0. The compatible strict restriction {g>−k} retains mass 6(μ(x_k)−m)², tending to 6(1−m)². This explicitly accounts for truncation boundary mass.\n\nNecessity in B–D. Given large t choose η=sqrt(C₀/t). Then (14) gives\nν_W,vη(A_η)≥c sqrt(t)W(t),\nand A_η has depth at least (c₀/C₀)t. A positive limsup of sqrt(t)W(t) therefore obstructs uniform tails and original-capacity absolute continuity using actual potentials and sets. If sqrt(t)W(t) is additionally bounded, select t_j along this limsup. The finite ν_W,vη_j have uniformly bounded mass by n1, so a subsequence has a finite weak limit λ. For every closed neighborhood K of D₀, A_η_j⊂K eventually and carries weighted mass ≥c>0. Portmanteau gives λ(K)≥c; decreasing K to D₀ gives λ(D₀)≥c. But ν_W,g(D₀)=0. This proves the required smooth normalized capacity-convergent sequence and finite divisor-charging cluster. No finite cluster is asserted when sqrt(t)W(t) is unbounded.\n\nArtifacts and limitations. The complete saved proof is proof_n2.txt. verify_identities.py verifies identity (12) exactly and reports PASS; its displayed annular limiting Q values exceed 0.999 for κ=1/1000. These observations do not establish the analytic estimates by sampling. This remains an unverified proof draft.\n\nArtifacts: /workspace/research/native-workers/codex-DZRZMb",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "Completes A–E for R: constructs one genuine normalized invariant potential with infinite weighted measure when sqrt(t)W(t) is unbounded, and gives the exact general and power/logarithmic classifications. The unrestricted original S02 remains incomplete.",
      "detailedSummary": "A decreasing sum of the actual smooth examples is chosen at rapidly separated scales along large values of sqrt(t)W(t). Controls all other summands on disjoint annuli, verifies local smoothness and positivity of actual products, and obtains infinite weighted mass. Consequently universal individual finiteness and uniform total bounds have the bounded square-root threshold, whereas tails, original-capacity absolute continuity and capacity-to-weak continuity have the vanishing square-root threshold. Necessary obstructions extend to the unrestricted class, but the sufficient results do not.",
      "text": "Uses n1 and n2. This proves the individual necessity in A; unbounded masses of a sequence alone would not prove it.\n\nAn additional uniform estimate follows from (8) and the correction slope bound. On the affine chart, for w≠0,\n0≤−v_η(x,w)≤C(1+x_+)+Cηlog⁺(1/dist_E(w,0)²).  (17)\nThe v_η have uniformly bounded L¹ norm: the base x-volume decays exponentially at both ends, and the elliptic logarithm is integrable.\n\nAssume sup_{t large}sqrt(t)W(t)=∞. Fix c_j=2^(−j−2), with sum c_j=1/4. Choose η_j rapidly decreasing and t_j=C_*c_j/η_j², where C_* is a sufficiently large fixed constant, to satisfy\nη_j<η_(j−1)/10,\nΣ_{i<j}c_iC₀/η_i²≤c_j/η_j²,\nc_jη_j≤c_(j−1)η_(j−1)/4,\nsqrt(t_j)W(t_j)≥2^j sqrt(C_*)/[c₁c_j^(5/2)].  (18)\nAll preceding restrictions only set lower bounds on t_j. The assumed unboundedness occurs at arbitrarily large t, so this induction is possible even when sqrt(t)W(t) oscillates.\n\nThe partial sums f_N=Σ_{j≤N}c_jv_η_j decrease and are genuine ω-psh because\nω+dd^cf_N=(1−Σ_{j≤N}c_j)ω+Σ_{j≤N}c_j(ω+dd^cv_η_j)≥0.\nTheir uniform L¹ bound prevents an identically −∞ limit. The decreasing limit f is genuine quasi-psh with its canonical upper representative. Set u=f−sup_Xf. Then u∈R and sup u=0. Since sup f≤0, normalization decreases its depth relative to the sum of depths.\n\nThe actual annuli A_j=A_η_j are disjoint because their x intervals separate under the factor-ten decrease. On A_j,\nx≤C/η_j and log⁺(1/dist(w,0)²)≤C/η_j³.\nThe current summand contributes at most C₀c_j/η_j² and earlier summands at most c_j/η_j² by (18). For future summands, (17) yields\nΣ_{i>j}c_i(−v_η_i)\n≤C(1+1/η_j)Σ_{i>j}c_i+Cη_j⁻³Σ_{i>j}c_iη_i\n≤C′c_j/η_j².\nHere Σ_{i>j}c_i=c_j, and the quarter-ratio condition gives Σ_{i>j}c_iη_i≤c_jη_j/3. Taking C_* large enough proves\n0≤−u≤t_j on A_j.  (19)\n\nThe products used next are actual products. On a neighborhood of each A_j, w stays a positive distance from 0 and x lies in a finite positive interval. Future F_η and all their derivatives are bounded by C_{K,r}η, from the Gaussian Green integral off 0. For sufficiently small future η, the majorant correction is 3η up to superpolynomially small errors on that interval; G_η and its derivatives are uniformly bounded there. The series converges smoothly on these neighborhoods. Thus u is smooth there, ω+dd^cu≥c_j(ω+dd^cv_η_j), and positivity of the cubic expansion gives μ_u≥c_j³μ_vη_j on A_j. Monotonicity of W, (14), (18), and (19) imply\nν_W,u(A_j)≥c₁c_j³η_j⁻¹W(t_j)\n=(c₁/sqrt(C_*))c_j^(5/2)sqrt(t_j)W(t_j)≥2^j.\nSumming over disjoint annuli proves ν_W,u(X)=∞. Poles elsewhere have zero assigned weight and extended measure; the lower bound uses locally smooth annuli.\n\nClassification for general decreasing weights. For every positive C¹ nonincreasing W→0, universal individual finiteness on R and a uniform total bound on R are equivalent to boundedness of sqrt(t)W(t) at infinity. The quantitative upper bound is 12Q(W). Uniform tails and uniform absolute continuity for the ORIGINAL capacity hold exactly when sqrt(t)W(t)→0, with bounds 12Q_T(W) and the Borel estimate in n1. The map from ALL of R into finite measures is capacity-to-weak continuous exactly under the same vanishing condition. In the bounded nonvanishing regime n2 gives the finite weak cluster charging the canonical limit’s analytic pole divisor. In the unbounded regime the single u above prevents a map into finite measures on all of R; this is not relabeled as a finite weak-limit example.\n\nPower/logarithmic families. Compact-interval smoothing does not change these thresholds. For eventually decreasing weights (1+t)^(-p)log(e+t)^(-a) tending to zero, sqrt(t)W(t) is asymptotic to t^(1/2−p)(log t)^(-a). Individual finiteness and uniform total bounds on R hold exactly for p>1/2, or p=1/2 and a≥0. Tails, original-capacity absolute continuity and capacity-to-weak continuity hold exactly for p>1/2, or p=1/2 and a>0.\n\nScope limitation. Every necessary obstruction applies to the unrestricted class because the examples belong to that class. The sufficient proof uses U(2) invariance and does not apply to arbitrary potentials. Thus original unrestricted S02 remains incomplete. Its supplied sufficient criterion ∫₀^∞(1+t)(−W′(t))dt<∞ is not sharpened here to a complete unrestricted classification.\n\nArtifacts and evidence. Programs, input, proofs and outputs are retained in the workspace: input.json, proof_n1.txt, proof_n2.txt, proof_n3.txt, verify_identities.py, verification_output.txt, source_receipts.json, environment_and_commands.txt, build_deliverable.py, deliverable.json, and artifact_sha256.json. Rerun python verify_identities.py > verification_output.txt, then python build_deliverable.py. All four symbolic checks passed; packaging checks passed for backward support IDs and saved note contents. Environment: Python 3.12.14, SymPy 1.14.0, Linux x86_64. No resource-heavy computation was launched; no operator supervised compute service or cloud environment_status tool was exposed. Direct curl failed because the configured proxy was unreachable; primary sources were inspected through the available web connector and its receipts retained.\n\nThese are ordinary unverified proof drafts. Symbolic execution verifies the displayed algebra, not mathematical correctness of the analytic proof. The restricted A–E conclusions are reconstructed; the exact unrestricted original task is not solved.\n\nArtifacts: /workspace/research/native-workers/codex-DZRZMb",
      "support": [
        "n1",
        "n2"
      ]
    }
  ],
  "candidate": false,
  "workspace": "/workspace/research/native-workers/codex-DZRZMb"
}

```


## Exact primary application context: Xia--Zhang, text lines211--480

URL: https://arxiv.org/html/2608.21053v1
Text SHA256: 7430e311274ea0ef23ed73394951f02095c1da147fe08c0e4b905c8e99343dfb

```text
Thus x is the logarithmic radial coordinate and one has µx = µ(1 − µ). For a smooth real
function V = V (x, w), subscripts denote derivatives.

Lemma 2.2. Let V : R × E → R be smooth, and suppose that V is independent of x for all
sufficiently negative x, and equal to a single constant, independent of both x and w, for all
sufficiently positive x. Then V extends to a smooth function on X, and on ξ ̸= 0 the Hermitian
form ω + ddc V is positive if and only if

                                                                                     |µ + Vxw̄ |2
             1 + Vww̄ > 0,        µ + Vx > 0,             Q[V ] := Vxx + µ −                      > 0.   (2.4)
                                                                                      1 + Vww̄
At ξ = 0, positivity is equivalent to 1 + Vww̄ > 0. Where V is constant, positivity is automatic.

Proof. The hypothesis for x ≪ 0 gives a smooth extension across ξ = 0, while the hypothesis for
x ≫ 0 and Lemma 2.1 extend the function smoothly to all of X. We compute the positivity
condition at a point with ξ ̸= 0. In the trivialization (2.2), using a local lift of w, one has
                                        
            u = w + w̄ + log 1 + |ξ|2 = w + w̄ + log(1 + ex ),                       ∂u = dw + µ ∂x.

Since the local potential of ωFS is log 1 + |ξ|2 , differentiation gives
                                                      


                                            ¯ + iµ(1 − µ) ∂x ∧ ∂x.
                                   α = iµ ∂ ∂x                 ¯                                         (2.5)

We now specify the three tangent vectors used to test positivity. Set
                                       1
                              er := p         (ξ1 ∂/∂ξ1 + ξ2 ∂/∂ξ2 ).
                                     µ(1 − µ)

Then er is an α-unit vector with ∂x(er ) = √ 1                         . Choose an α-unit vector e⊥ in the α-
                                                              µ(1−µ)
orthogonal complement of er in the ξ-coordinate plane. Since the Fubini–Study pairing of
a vector j aj ∂/∂ξj with the radial vector equals (1 + |ξ|2 )−2 j aj ξ¯j , orthogonality forces
           P                                                      P
P      ¯
  j aj ξj = 0, that is, ∂x(e⊥ ) = 0. Finally, ew := ∂/∂w spans the vertical tangent line and has
unit length for the Hermitian metric associated with ω.



                                                          4
  In the ordered frame (e⊥ , er , ew ), the Hermitian matrix of ω + ddc V is

                                      µ + Vx
                                                                                                      
                                     µ                        0                              0        
                                                                                                      
                                                      µ + Vxx                       µ + Vxw̄ 
                                            0                                      p          .
                                                                                               
                                                                                                                            (2.6)
                                    
                                                      µ(1 − µ)                       µ(1 − µ) 
                                                       µ + Vwx
                                                                                                      
                                             0                                          1 + Vww̄
                                                                                                      
                                                      p
                                                        µ(1 − µ)
                                                        ¯ yields
Indeed, substituting (2.5) in the calculation of ω + i∂ ∂V

                            µ + Vx                                    ¯
         ω + ddc V =               α + i µ2 + Vxx − (1 − µ)Vx ∂x ∧ ∂x
                                                                
                              µ
                                                                     ¯ + i(1 + Vww̄ )dw ∧ dw̄.
                            + i(µ + Vxw̄ )∂x ∧ dw̄ + i(µ + Vwx )dw ∧ ∂x

Evaluating this on (e⊥ , er , ew ) gives (2.6); here Vwx = Vxw̄ as V is real. This matrix is block
diagonal, so its positivity is equivalent to the second condition in (2.4), together
                                                                                     with the positive
                                                                             a b
definiteness of the lower-right 2 × 2 block; and a Hermitian matrix b̄ ρ is positive definite if
and only if ρ > 0 and aρ − |b|2 > 0. Here ρ = 1 + Vww̄ and

                                    (µ + Vxx )(1 + Vww̄ ) − |µ + Vxw̄ |2   1 + Vww̄
                   aρ − |b|2 =                                           =          Q[V ],
                                                 µ(1 − µ)                  µ(1 − µ)

so the block is positive definite if and only if 1 + Vww̄ > 0 and Q[V ] > 0. This proves (2.4).
   At ξ = 0, our hypothesis for x ≪ 0 gives V = V− (w) and ∂u = dw. Thus ω + ddc V =
α + i(1 + Vww̄ )dw ∧ dw̄, so positivity is equivalent to 1 + Vww̄ > 0. Finally, where V is constant
we have ω + ddc V = ω > 0.

2.4   The mass identity
Lemma 2.3. For any V ∈ C ∞ (X, R),
                   Z                             Z                 Z                Z                        !
                        (ω + ddc V )3 =              ω 3 + 12π                                    |Vw |2 dAE ωFS
                                                                                                              2
                                                                                                                 (y).       (2.7)
                    X                            X                     P2           π −1 (y)

Proof. Using Stokes’ theorem, d(ddc V ) = 0, and (2.1), one obtains
                        Z                              Z                                      Z
                                c    3                         2                c
                             (dd V ) = 0,                   ω ∧ dd V =                            V ddc (ω 2 ) = 0.
                         X                              X                                     X

Therefore
              Z                          Z              Z                                          Z
                   (ω + ddc V )3 −           ω3 = 3            ω ∧ (ddc V )2 = 3                       V ddc ω ∧ ddc V
               X                         X                 X
                                                           Z                                        XZ

                                                     = −3                   2
                                                                   V α ∧ dd V = 3         c                      ¯ ∧ α2 .
                                                                                                           i∂V ∧ ∂V
                                                            X                                          X

Because α2 = π ∗ ωFS2 already has top degree in the base variables, every component of ∂V

involving dξ1 or dξ2 vanishes after wedging with α2 . On overlaps, the fiber coordinates differ by a
base-dependent holomorphic function, hence ∂/∂w and the fiber integral in (2.7) are globally well
defined. Moreover, i∂V ∧ ∂V¯ ∧ α2 = 4π|Vw |2 dAE ∧ π ∗ ω 2 , so Fubini’s theorem gives (2.7).
                                                          FS




                                                                   5
3     Heat kernel potentials on the elliptic fiber
3.1    The heat kernel and Fourier analysis
For t > 0, define the heat kernel on E by
                                                                            !
                                    2X          |w − λ|2
                          kt (w) :=       exp −                                 ,           Λ := Z + 2πiZ,                     (3.1)
                                    t λ∈Λ          t

the sum being evaluated at any lift of w ∈ E. The series and all its derivatives converge locally
uniformly, and the sum is unchanged when w is replaced by w + λ with λ ∈ Λ; thus kt is well
defined, smooth, and strictly positive. Unfolding a fundamental rectangle and using (2.3),
                                   i        2 −|w|2 /t            1
                 Z                        Z                                             Z
                                                                                                 2       2
                     kt dAE =                 e        dw ∧ dw̄ =                            e−(a +b )/t da db = 1.
                 E                4π      C t                     πt                    R2

    We shall also use Fourier analysis on E. For (p, q) ∈ Z2 , set
                                  iq
                     νp,q = p +      ,          χp,q : E → C,                   χp,q (w) = e2πip Re w+iq Im w ;
                                  2π
each χp,q is Λ-periodic, and {χp,q }(p,q)∈Z2 is an orthonormal basis of L2 (E, dAE ). Writing
∂w = 21 (∂a − i∂b ) and ∂w̄ = 12 (∂a + i∂b ), we have

                    q                                          q
                                                                         
    ∂w χp,q = πip +   χp,q ,                  ∂w̄ χp,q = πip −   χp,q ,                       (χp,q )ww̄ = −π 2 |νp,q |2 χp,q . (3.2)
                    2                                          2
The Fourier coefficients of kt are computed by unfolding:
                          1
       Z                          Z
                                                2   2                                            2 2         2      2     2
           kt χ̄p,q dAE =                 e−(a +b )/t e−i(2πpa+qb) da db = e−tπ p e−tq /4 = e−π |νp,q | t .
         E                πt       R2

This yields the Fourier expansion of kt , using Poisson summation for the lattice Λ:
                                                                        2           2
                                                                   e−π |νp,q | t χp,q (w),
                                                          X
                                          kt (w) =                                                                             (3.3)
                                                        (p,q)∈Z2

the series converging in C ∞ (E) for every t > 0, locally uniformly in t. In particular, by (3.2),

                                                         ∂t kt = ∂w ∂w̄ kt ,                                                   (3.4)

and kt → 1 exponentially fast in C ∞ (E) as t → ∞.

3.2    The fiber potential and its energy
Lemma 3.1. For 0 < η < 1/10, define Fη : (0, ∞) × E → R by
                                                                                                     2       2
                                                                                            e−π |νp,q | t
                                   Z ∞
                                                                           η       X
              Fη (t, w) := −η                 kr (w) − 1 dr = −                                           χp,q (w).            (3.5)
                                      t                                     π 2 (p,q)̸=(0,0) |νp,q |2

Then Fη is smooth and real, and the following hold.
 (1) One has

                      (Fη )t = (Fη )ww̄ = η(kt − 1),                    1 + (Fη )ww̄ = 1 − η + ηkt > 1 − η.                    (3.6)

 (2) One has
                                                                    1
                                              (log kt )ww̄ ≥ −                  on E,         t > 0.                           (3.7)
                                                                    t

                                                                   6
 (3) For 0 < t ≤ 1,
                                                             1
                                    Z
                                                               + O(η 2 ).
                                         |(Fη )w (t, w)|2 dAE = 2η 2 log                                                 (3.8)
                               E                             t
      Here the implicit constant is uniform for 0 < t ≤ 1 and 0 < η < 1/10.
 (4) Fη is exponentially small in the sense that, for all fixed integers a, m ≥ 0 and all t ≥ 1:
                                           ∥∂ta Fη (t, ·)∥C m (E) ≤ Ca,m η e−t/4 .                                       (3.9)

Proof. Since kr − 1 → 0 exponentially fast, the integral in (3.5) converges, and termwise
integration in r gives the stated Fourier series. The series and all its (t, w)-derivatives converge
uniformly on [t0 , ∞) × E for each t0 > 0, so Fη is smooth; it is real because the coefficients are
real and invariant under (p, q) 7→ (−p, −q).
   (1) Differentiating (3.5) in t gives (Fη )t = η(kt − 1); differentiating the Fourier series in w, w̄
and using (3.2) gives
                                                                    2         2
                                                            e−π |νp,q | t χp,q = η(kt − 1).
                                                 X
                          (Fη )ww̄ = η
                                             (p,q)̸=(0,0)

The last inequality in (3.6) holds because kt > 0.
  (2) Fix a lift w and introduce the probability weights
                                                                2
                                             e−|w−λ| /t
                                    Pλ := P       −|w−λ′ |2 /t
                                                               ,                   λ ∈ Λ.
                                           λ′ ∈Λ e
From ∂w̄ |w − λ|2 = w − λ we get
                                                                        X
                                        t ∂w̄ log kt (w) = −                (w − λ) Pλ ,                                (3.10)
                                                                        λ∈Λ
and differentiating once more, now in w, we find
                                                   (                                                           )
                                   1  1             X
                                                                          2
                                                                                   X                       2
                   (log kt )ww̄ = − + 2                     |w − λ| Pλ −                (w − λ)Pλ                  .
                                   t t                 λ                            λ
The bracket is the variance of the C-valued random variable w − λ under the probability
distribution (Pλ ), hence nonnegative. This proves (3.7).
   (3) Parseval’s identity applied to (3.5) yields
                                                                                               2       2
                                                  η2            e−2π |νp,q | t
                                    Z                   X
                                                   2
                       Eη (t) :=   |(Fη )w | dAE = 2                           .                                        (3.11)
                                 E                π (p,q)̸=(0,0) |νp,q |2

Differentiating termwise and comparing with (3.3), we find
                                                                2         2
                      Eη′ (t) = −2η 2                     e−2π |νp,q | t = −2η 2 k2t (0) − 1 .
                                              X                                                            

                                           (p,q)̸=(0,0)

On the other hand, evaluating (3.1) at w = 0 and time 2r, and using |λ| ≥ 1 together with the
                           2                      2
elementary inequality e−|λ| /(2r) ≤ e−1/(4r) e−|λ| /4 for 0 < r ≤ 1, we get
                                                                                               !
                       1                 2
                                                 1                               e−1/(4r)
                                     e−|λ| /(2r) = + O
                               X
             k2r (0) =    1+                                                                       ,       0 < r ≤ 1.
                       r     λ∈Λ\{0}
                                                  r                                  r

The error r−1 e−1/(4r) is integrable on (0, 1], and Eη (1) ≤ Cη 2 by (3.11). Integrating Eη′ over [t, 1]
therefore gives (3.8).
                                                                             ′
   (4) Fix a and m, and abbreviate ν := νp,q . Every derivative ∂ta ∂ m with m′ ≤ m, applied
to the series (3.5), is a sum over (p, q) ̸= (0, 0) of terms bounded by a polynomial in |ν| times
     2  2
ηe−π |ν| t . Writing

```


## Exact primary application context: Xia--Zhang, text lines480--570

URL: https://arxiv.org/html/2608.21053v1
Text SHA256: 7430e311274ea0ef23ed73394951f02095c1da147fe08c0e4b905c8e99343dfb

```text
ηe−π |ν| t . Writing
                            2   2                      2    2                              2       2
                        e−π |ν| t = e−t/4 e−(π |ν| −1/4)t ≤ e−t/4 e−(π |ν| −1/4)
for t ≥ 1, and noting that
                                P                     −(π 2 |ν|2 −1/4) < ∞, we obtain (3.9).
                                ν̸=0 polynomial(|ν|) e


                                                                7
3.3    A heat-kernel estimate
Lemma 3.2. There is an absolute constant C0 ≥ 1 such that, for 0 < t ≤ 1 and w ∈ E,
                                                                                   !
                                                  |t ∂w̄ log kt (w)|2
                               tkt (w) ≤ C0 exp −                                      .           (3.12)
                                                          C0 t

Proof. Fix a lift of w, choose a nearest lattice point λ0 , and put

                               d := |w − λ0 |,             sλ := |w − λ|2 − d2 .

The number d is uniformly bounded, sλ ≥ 0, and the triangle inequality gives
                                                       |λ − λ0 |2
                                           sλ ≥                   − C.
                                                           4
For all sufficiently large |λ − λ0 |, the right-hand side is at least |λ − λ0 |2 /8; the remaining lattice
points form a fixed finite set. Since sλ ≥ 0 and d is bounded, there is an absolute constant
C0 ≥ 1 such that, uniformly for 0 < t ≤ 1,

                                       e−sλ /t +         |w − λ|e−sλ /t ≤ C0 .
                                 X                 X

                                 λ∈Λ               λ∈Λ

Consequently
                                                   2                               2
                               tkt (w) = 2 e−d /t             e−sλ /t ≤ C0 e−d /t .
                                                         X

                                                        λ∈Λ

For the gradient, the probability weights used in (3.10) satisfy Pλ ≤ e−sλ /t , and hence

                                                                   |w − λ|e−sλ /t .
                                                            X
                                 t ∂w̄ log kt ≤ d +
                                                           λ̸=λ0

If d ≥ 1/4, the preceding uniform bound makes the right-hand side at most C0 d. If d < 1/4,
             ̸ λ0 , sλ ≥ |λ − λ0 | |λ − λ0 | − 2d ≥ |λ−λ  0|
                                                  
then, for λ =                                            2 , and summation over the lattice gives
                 −sλ /t ≤ C e−1/(C0 t) . Thus, in both cases,
   λ̸=λ0 |w − λ|e
P
                           0
                                                                                      
                             G := t ∂w̄ log kt (w) ≤ C0 d + e−1/(C0 t) .

If G > 2C0 e−1/(C0 t) , then d ≥ G/(2C0 ), and the estimate for tkt proves (3.12). Otherwise G2 /t is
uniformly bounded for 0 < t ≤ 1, and the same conclusion follows from tkt ≤ C0 , after increasing
the absolute constant.
                                                       1              1
Lemma 3.3. There exists C > 0 such that, for 0 < κ < 200C 0
                                                            , 0 < η < 10 , 0 < t ≤ 1, 12 ≤ µ ≤ 1,
and                     s
                          2κ    1                             σ
                  σ :=       log ,       h := ηkt ,    ζ := t ∂w̄ log kt ,
                           η    ηt                            µ
we have, pointwise on E,
                              µ2 (1 − η)h     1 2             1
                                                                                          
                       κtkt −             ζ−      ≤ Cκ exp −        .                              (3.13)
                              1−η+h          1−η             Cσ 2 t
Proof. Let C0 ≥ 1 be the constant in (3.12), and take any κ > 0 with C0 κ < 1/200. If
σ 2 t ≥ 1/100, the left-hand side of (3.13) is at most κtkt ≤ C0 κ. Increasing C gives the assertion.
    Suppose next that σ 2 t < 1/100 and |ζ − (1 − η)−1 | ≥ 1/4. Since µ ≥ 1/2 and η < 1/10, the
                                   h
subtracted square is at least 100(1+h)  . Moreover, log(1/(ηt)) > 2, tkt ≤ C0 , and the definition of
σ give
                                              η             3η      η
                               κt(1 + h) ≤        + C0 κη ≤     <
                                             400            400    100

                                                          8
by the choice of κ. Since h = ηkt , this is equivalent to κtkt ≤ h/(100(1 + h)); hence the left-hand
side of (3.13) is nonpositive.
   It remains to consider σ 2 t < 1/100 and |ζ − (1 − η)−1 | < 1/4. Then |ζ| ≥ 3/4, so
                                                                     µ|ζ|    3
                                                 t ∂w̄ log kt =           ≥    .

```


## Exact primary application context: Bedford--Taylor, text lines1--48

URL: https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf
Text SHA256: d32eb9305e1cfbcc569746d51d53e417508b33aba0e3b5a1a706036cb0593115

```text
       A new capacity for plurisubharmonic functions

                                                        by

                                ERIC BEDFORD(l) and B. A. TAYLOR(z)
    Princeton University, Princeton, N J, U.S.AI                   University of Michigan, Ann Arbor, MI, U.S.A.
                         and
Institute for Advanced Study, Princeton, N J, U.S.A.




                                                 1. Introduction

If f2 is a complex manifold, let P(f2) denote the plurisubharmonic functions on Q. Each
u 6 P(f~) is subharmonic with respect to every operator Aa which in local coordinates
may be written in the form
                                                              a2
                                                ma =   2aa~/ OziOZj

where a=(ao.) is a nonnegative Hermitian matrix. We wish here to exploit the fact that
plurisubharmonic functions are simultaneously subharmonic with respect to several
Laplacians to obtain some results on their local behavior which are stronger than those
known for subharmonic functions. We are motivated by the equation

                            ( det         Ozj_1])1/"=linf{A"u:det[aO']=l)n
                                    L[02//0zi                                                             (1.1)


for u fiP(Q)nCZ(~2) (c.f. Gaveau [15]); this quantity, in some sense, estimates the
extent to which u lies in the interior of P(Q). Because of the geometric nature of the
cone P(f~), it seems that a "potential theory" which can describe the properties of
P(Q) must necessarily be nonlinear.
      The operator dd~=2iOj and its exterior powers (ddC)j a r e invariant under holomor-
phic mappings. It is easily seen that in local coordinates

                                      (ddCu)n = Cn det [] Ozi
                                                           OZu
                                                             OZj]dV(z).
                                                                J                                         (1.2)



(') Sloan Foundation Fellow
(2) Research supported in part by a grant from the National Science Foundation
                               E. BEDFORD AND B. A, TAYLOR


```


## Exact primary application context: Bedford--Taylor, text lines125--299

URL: https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf
Text SHA256: d32eb9305e1cfbcc569746d51d53e417508b33aba0e3b5a1a706036cb0593115

```text
results on the " t h i n " points of sets.

                                 2. The operators (dd~) k and 5fk
Throughout the paper we use the notion of positive differential forms, or positive
currents, as presented in Lelong [18]. This notion was first defined and used by Lelong
4                                          E. B E D F O R D A N D B. A. T A Y L O R



in [21]. If ~0 is a positive current of bidegree (p, p), then ~0 is a distribution of order zero.
Thus, if g0 is a positive current of bidegree (1, 1) with smooth coefficients, then ~ ^ ~ is
well defined and is also a positive current. However, we need to use an extension of
this multiplication of positive currents.
       Recall that given v I . . . . . v k E P ( f 2 ) N L = ( f L I o c ) we may define the positive current
d ~ v ~ ^ ... ^ ddCv k (inductively) as a distribution if we give its action on a test form ~p
of bidegree ( n - k , n - k ) as


                          fQ
                           ddCv' A ... ^ dd~vk ^ ~O= ( vlddCv2 ^ ... ^ d ~ v k ^ ddC~O
                                                               dfl
                                                                                                                   (2.1)


(see [4]). The main result of this section shows that (dd~) k is continuous under
decreasing limits. Thus, the definition is justified as an extension of the operator on
smooth functions, and, therefore, retains the usual algebraic properties of the operator
on smooth functions.

       THEOREM ,2.1. L e t {v)} . . . . . {v~} be d e c r e a s i n g s e q u e n c e s o f f u n c t i o n s in P(ff2)f)
L=(ff~, loc) a n d a s s u m e that f o r all z E f2,

                                 !imv~= v i E p ( ~ ) f ) L = ( Q , l o c ) ,   1 <~i<~k.

Then

                                !im ddCv) ^ ... ^ d ~ v ~ = ddCo I A ... A ddCv k


w h e r e the limit is in the w e a k t o p o l o g y on Mk, k(Q), the currents o f b i d e g r e e (k, k) on if2
o f order zero; i.e. w h i c h are r e p r e s e n t e d by integration (see e.g. [18] or [15]).
       An immediate consequence of Theorem 2.1 is

       COROLLARY 2.2. The m a p ( v 1 . . . . . v~)~--~dd~v ~ ^ ,.. ^ dcl~v k is a s y m m e t r i c , multi-
linear m a p o f [P(~)NL~(s                      k into the c o n e o f n o n n e g a t i v e c l o s e d currents o f
b i d e g r e e (k, k).
       For the proof of Theorem 2. I and many other results of this paper, it is convenient
to introduce the classes

                                               P* = P*(f~, K, O, A , B)                                            (2.2)

where f~ is a bounded, strongly pseudoconvex subset of C n, K is a compact subset of
f~, 0 is a strictly plurisubharmonic function on ~ which is a defining function for
                      A N E W CAPACITY FOR P L U R I S U B H A R M O N I C F U N C T I O N S



f~ = {Q<0}, and A, B are constants with A>0. A function u 6 P(f~) tqL=(f2, loc) belongs
to P* if

                                     u(z) = AO(z)+B,           z E ~\K.

We will usually not display the lengthy list o f parameters Q, K, ~, A, B.
    The use of the classes P* is easily seen. Note that the assertion of T h e o r e m 2. l is a
local result. Also, if the functions v~are changed outside a relatively compact open set
t o c Q , the convergence in ~o will not be changed. Now, if the relatively compact open
set ~o is specified and if the vj converge as in the hypotheses of T h e o r e m 2.1 we can
always find constants A, B > 0 and a compact set K so that all the functions

                                -i      ~max(v~(z),ap(z)+B),                z6K
                                v)(z) = I.ap(z)+B, z 6 Q \ K

belong to P* and Oj(z)=vj(z) for z fi w. Thus, in proving a local convergence result like
T h e o r e m 2.1, we can always assume the functions are smooth outside a compact subset
of Q.

    Proof o f Theorem 2. I. The p r o o f is by induction on k. For k = l, the assertion is
well known [18]. Assuming the result for values up to k, we will prove that

              lim ( v~ d~v) ^ ... ^ d~v~ ^ d ~ V = (v~                      A ... A ddCvk ^ ddCv      (2.3)
                                                              3~

for all test forms q, on Q. By (2.1), this implies ddCv~                                       converges in
Mk+ ,. k+l(g2) 9 And, following our remarks concerning P* (see (2.2)), we can assume that
v~6 P * = P * ( Q , K, •, A, B). By adding a constant to the v's, we may assume that B=O.
     N o w we will p r o v e (2.3) for ( n - k - 1 , n - k - 1 )      forms q5 which have the following
properties:

                                dd~q~>0 is a positive current on Q,
                                 is smooth in a neighborhood o f ~ ,                                  (2.4)

                                             and ~ = 0 on aft.

This will suffice to complete the proof, for given any compactly supported test form V,
we may choose e small enough that

                                            = -o(dd~Q)"-k-I+e~p
                                  E. BEDFORD A N D B. A. T A Y L O R



will satisfy (2.4). Now (2.3) will hold for V) and -o(dcPo) n-k-I, and thus it will hold for
~p=e-l(~+p(dd~Q)n-k-J), which is what we wanted.
    The first step in the proof of (2.3) is the inequality ~< which is a simple consequence
of the uppersemicontinuity of v~ For later reference we will state it in a slightly more
general form. No proof is given, since this is a well known property of weakly
convergent nonnegative measures.

     LEMMA 2.3. Let vj be a sequence o f upper semicontinuous functions which either
increase or decrease almost everywhere to an upper semicontinuous function
v E P ( ~ ) n L = ( Q , l o c ) . Let p and pj be nonnegative measures all supported on a
compact set Kcs with ttg---~tt. Then




    Notice that the lemma (with vj=v~                      ^ .../x ddCvf ^ ddCy) proves that
holds in (2.3) with dd~y replaced by any ( n - k , n - k ) form Z which is positive on the
compact set K for which v~C P*(Q, K, p, A, B). This is because Z can be split up into two
parts, X=Z1 +Z2 by a partition of unity, where ZI1>0 and support Z 2 c Q \ K . We get the
inequality ~ in (2.3) for Z1, by the lemma. The terms involving Z2 all converge because
v~=Ap on the support of Z2.
    To prove the other inequality in (2.3), first assume that all the approximants vjare
smooth on Q. Then


                                          +fo  \K

        ~fKV~176


       = fno~        A ... ^ d f v k A dd~o+ fn\K(O~176                ^ ... ^ ddCvk ^ d~q;.


The last integral vanishes because v ~ v~             on ~ \ K .   Using (2.1), the first integral is
equal to

      l v'ddcv~    d d C v 2 A "'" A ddCvkA ddr     <~( v ) ddCv~ ddr           ddevkA d d~~fl
      J~                                              [
                                                      d~

                         =
                             foov) d~v) , ^ dd~v z ^ ... ^ d ~ v k ^ ddC~.
                           A NEW CAPACITY FOR PLURISUBHARMONIC FUNCTIONS



Repeating the argument k - 1 more times gives


                 fo   v~      A ... /x dd~v k ^ ddCga <-

Lettingj-+~ in (2.5) gives the other inequality in (2.3).
                                                           fov~ ddCp) A ... ^ ddCv) /x ddCga.        (2.5)


    If the v~ are not smooth, then note first that it follows from the case just proved
that

       a-+olimfa(v~)add~(v))aA ... /x ddC(v~)a ^ dd~p = f a 4 dd~v) ^ .../x d ~ v ~ /x d ~ f l ,


where (v)a=v-x-~oa denotes a usual regularization of the plurisubharmonic function v
(see [18]). Thus, by a diagonalization process, we can choose 63---+0 so that 0j=(vj)aJ
decreases to v; and for all test forms ~p

          !im ( v~ d + v ) ^ ... ^ ddCv~ ^ d d ~ : lim ((6~                  ^ ... ^ dd~O~ A dd%p.
          J--+~ J ~                                       J-+~JQ

By the case just proved, the last limit equals f v ~ d d C v l ^ ... ^ dd~vkA dd~v2. This
completes the proof.

```


## Exact primary application context: Bedford--Taylor, text lines388--460

URL: https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf
Text SHA256: d32eb9305e1cfbcc569746d51d53e417508b33aba0e3b5a1a706036cb0593115

```text

        P r o o f . I f p=5~k(V', V~ Vz . . . . . Vk) and v is any weak limit of 5fk(V), V~ V2 . . . . . V~) then
kt~>v (by L e m m a 2.3), p = v outside of K, (since we can assume vj E P*). Further, on test
forms of the form ddC~p, ~ k is symmetric in v ~. . . . . v k. Thus, L e m m a 2.5 guarantees
convergence for the ~k no matter the order o f the sequences when n > k . The case n = k
follows exactly as in the proof of Theorem 2.4.
        An important corollary of Theorems 2. l, 2.4 is the following.

        THEOREM 2.7. I f f 2 = C "             a n d {uj}, {wj), {v)) ..... {v~} are d e c r e a s i n g s e q u e n c e s o f
functions         in P(f2)nL~176                      and      i f the      corresponding            limits        u , w , v I . . . . . v~E
P(Q) n L~176 loc), t h e n

     lim duj ^ ~ w j ^ dd~v 1 ^ ... ^ d d ~ v ~ = d u ^ dew ^ ddCv ~ ^ ... ^ ddr                              in Mk+l.k+l(f2).
     j--~ oo



        P r o o f . By polarization in the symmetric forms du ^ f w                              and dd~v ~ ^ ... ^ ddCv k, it
is      no      loss      of     generality          to       assume        that       u j = w ~ a n d vj=vj, l<~i<~k.                   Also
assume u~>0. Then we have the identity

                       -~dclCu~ A (ddCvj) k = ujddCuj ^ (ddCvj)k+duj ^ dCuj ^ (ddCvj) k


(which also serves as the weak definition of the last term). Since the left hand side and
the first term of the right hand side converge as j---~+o,, by Theorems 2.1 and 2.4, so
10                                      E. BEDFORD AND B. A. T A Y L O R



does the last term. The general case follows by applying this argument to u j + C for a
suitable large constant C.
     Note the following typical, simple algebraic formulas which hold as a consequence
of Theorems 2.1, 2.4, 2.7.

     COROLLARY 2.8. I f u, v f P ( f 2 ) nL~(f2,1oc) a n d q~r                               then Scp[(dd~u) " -
(dd~v)n]=J" (u-v)ddCq) ^ O, w h e r e

                          0 = (dd~u) "-I +(dd~u) "-2 ^ ddCv+ ... +(ddCv) "-l.

     Proof. The equation holds for smooth u and v so the result follows from Theorem
2.1 by approximating u, v by decreasing limits of smooth plurisubharmonic functions.

     COROLLARY 2.9. I f u, v, w fi P* =P*(f2, K, O, A, B), then


                         fn(u-v) (dc~w)'=- fnd(u-v) ^ d~w^ (dd~w)"-'.
     Proof. We can select uj-, vj, wj smooth plurisubharmonic functions in a class P*
(with possibly different K, A, B) which decrease to u, v, w on a neighborhood of K.
Then convergence follows from Theorem 2.4 for the left side and Theorem 2.7 for the
right side.
     Finally, for later reference, we record the Chern-Levine-Nirenberg estimates for
(ddC) ~ on bounded plurisubharmonic functions (c.f. [11] or [4]).

     THEOREM 2.10. I f v ~. . . . . v k f i P ( f 2 ) n L ~ ( Q ) , Q c C ~, a n d if K is a c o m p a c t s u b s e t
o f f 2 , then there is a c o n s t a n t C = C ( K , f2) such that


       (i)     KdCFv'^ ... ^ ddCv k ^ fl,-k <- CIIv'll ... Ilvkll


      (ii)     KV~        ^ . . . / x ddCv k/x fln-k <~ CIIv~ .., Ilvkll


     (iii)    [ dv ~ ^ dCv ' /x ddCv 2 ^ . . . / ~ ddCv k A fl~-k <~ Cllv~ ... LLvkLL
              dK


w h e r e fl,_k=fl~-k/(n--k)!, fl= 89 E dzy ^ d~i is the Kiihler f o r m , a n d

                                          Ilvil{ = sup {Ivi(z)[: z 6 Q }.


```


## Exact primary application context: Bedford--Taylor, text lines550--625

URL: https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf
Text SHA256: d32eb9305e1cfbcc569746d51d53e417508b33aba0e3b5a1a706036cb0593115

```text
tion 2.10. Another integration by parts then yields

                                        C       (uFu) ^ (d          v) ~    ^ da      (.j-u)
                       Jq

Thus, the power of ddCv has been reduced to n - 1 in the term on the right hand side of
(3.2).
     We would like to repeat this argument n - 1 more times, but there is one problem.
Namely, when we integrate by parts to obtain


         ((Uj--U) (ddCu) n-' ^ ddC(uj-u) .~- - - ( d ( u j - I ~ ) ^ (leo ^ (ddCo) n-2 ^ ddC(Idj-u).
         Jn                                               3

The Schwarz inequality cannot be applied directly to the right hand side because the
( n - l , n - l ) current (dd~v) n-2 ^ ddC(uFu) need not be positive. However, it suffices to
estimate the integral obtained by replacing ddC(uFu) by ddr                                        This term can then
be estimated by the Schwarz inequality and the Chern-Levine-Nirenberg estimate,
exactly as before.
     Continuing in this manner, we finally obtain that fq(dd~v) n is dominated by a
finite number (2n) of terms of the form




where each of the functions w ~.... ,w ~ is either equal to uj or u. The constant C
depends on sup {luj{z)l: z E f~, j = l , 2 .... }, which is finite since ui decreases to u in P*.
According to Theorem 2.4, each integral of the form (3.3) converges to 0 as j---~+~.
Thus,




which completes the proof.

      THEOREM 3.5. L e t f2 be a bounded open set in C n and uEP(ff2). Then for each
e>0, there is an open subset • o f Q such that C(O, ~2)<e and a is continuous on f 2 \ ( 7 .


2-822906 A c t a Mathematica 149
14                               E. B E D F O R D A N D B. A. T A Y L O R



     To minimize technical problems, we give the proof here only for

                                           u 6 P(ff2) n L~(ff2, loc).

     The full result will be immediate after we have shown that

                                    lim C { z 6 if2: u(z) < - j } = 0                    (3.4)
                                    j---~ oo



in Section 6. Only the bounded case of Theorem 3.5 is used in the arguments leading to
(3.4).

     Proof of Theorem 3.5 for P(Q) nL=(f2, loc). Because of (2) and (3) of Proposition
3.2, we can assume that Q is strictly pseudoconvex, or even a small ball, and u is
plurisubharmonic and bounded on a neighborhood of (2. Let u] be a sequence of
smooth plurisubharmonic functions which decrease to u on a neighborhood of (2. By
shrinking if2 and replacing uj, u by max(uj, Ao+B), we see that it is also no loss of
generality to assume that

                                uj, uEP* = P*(ff2,K,Q,A,B).

Then by Theorem 3.4, there exists an integer jr and an open set




such thatC(~t,Q)<2-t. IfGk-Llt>kGt,
               t                m                r
                                                     then the functions uj decrease to u uni-

```


## Exact primary application context: Bedford--Taylor, text lines950--1135

URL: https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf
Text SHA256: d32eb9305e1cfbcc569746d51d53e417508b33aba0e3b5a1a706036cb0593115

```text


                                          cl '

a contradiction unless C(K)=0. This completes the proof of Step 2.
22                               E. BEDFORD    AND   B. A. TAYLOR




     Proof of Step 3. By Theorem 3.5 we can choose an open set G c Q such that uj-, u
are continuous on f 2 \ G = F and C(G, Q)<e. We claim~that there exist countably many
compact sets K F F such that

                                          NcG     U [UKj]                           (5.6)

where C(Kj)=0. If this is proved, then by Proposition 3.2, C(N)<.C(G)+Z C(Kj)<e, so
C(N)=0 and the proposition is proved. Clearly, NcGU[(Fn{u<u*})]. B u t , if
Ka~={z 6 F : u(z)~a<fl<~u*(z)}, then K ~ c F is compact because u* is upper semicon-
tinuous and u is lower semicontinuous on F. It is also clear that Fn {u<u*)=kJK~/3
where the union is over the countably many pairs of rational numbers (a, fl) with a<fl.
Thus, we only have to prove that C ( K ~ ) = 0 . By subtracting a real constant, we may
assume that uj, u < 0 on if2. Multiplying by another constant, we may set a = - 1 . Thus
u~q~u*>--l=a on K ~ . Consequently, C(K,~)=0 by Proposition 5.3, and the proof
is complete.



                                         6. Pluripolar sets
In this section we give the basic connections between pluripolar sets, the extremal
functions u~:, and the outer capacity C* obtained from C. The standard construction of
outer capacity is

                    C*(E) = C*(E, f~) = inf{C((7): (7~E, t~ open in f~}.            (69

Let us remark that if C 9     is an open set, and if KjcK2c ... is a sequence of compact
sets such that UKj=r      then llmj~
                                9     ,__   --
                                     UKi--Uc--U ~. It follows from Theorem 2.1 and Pro-
position 5.3 then, that


                                     c(<        = f(dd ucr                         (6.2)


for open sets ff~f~.
     First, some elementary properties of the outer capacity 9

     PROPOSITION 6.1. If g) is bounded in C", then
      (i) C*(EI)<~C*(E2) if ElcEzcff2;
     (ii) C*(E, f~)~C(E, Q) if Ecf21cQ;
     (iii) C*(tJEj., f~)<~ZjC*(Ej, Q).
                   A N E W CAPACITY F O R P L U R I S U B H A R M O N I C F U N C T I O N S     23

    Proof. These follow immediately from the corresponding properties for C(E, f2)
(see Proposition 3.2).
     Next, some elementary properties ot the extremal functions.

    PROPOSITION 6.2, If Q is bounded in C", then
      (i) u~ >-u* if ElcE2cff2;
     (ii) u~(z, f21)>>-u~(z,~2) if Ecf21cf2;
    (iii) if u~j=--O, and E=jU=IEj, then u~-O.

In addition, if • is strongly pseudoconvex and E is relatively compact in ~2, then
    (iv) u~(z)~O as z ~ a f ~ .

    Proof. Parts (i), (ii) are obvious. So is part (iv), since O~u~>>-AQfor some A>0,
where f2={Q<0}, Q a plurisubharmonic defining frunction for Q. To prove (iii), note
the following equivalence which is a direct consequence of Choquet's lemma.

               u~:-0 if and only if there exists a sequence of functions
           VI<~V2<~.... vj6P(~2), vj<O on f2, Vj<~--I o n E, and fQIvjI~2 -j.                 (6.3)

Thus, if vj is ~<-1 onEj, vj<O on f2, and flvjl<.e2 -j, then v=Evj6P(f2), v<0, v<~-I on
kJEj and J" {v{<.e. Hence, u~:-0.
    We also record another consequence of (6.3).

    PROPOSITION 6,3. Let if2 be bounded in C". Then u~=-Oif and only if there exists
v6P(f2), v<O on g2 and Ec{zfi g2: v ( z ) = - ~ } .

        Proof. If u~=0 and the vj are as in (&3), then v=EvjfiP(~2) and E c { z 6 Q :
 v ( z ) = - ~ } . Conversely, E c { v = - ~ } , where v<0, vEP(C2) implies UE>~sup{v/j:
j = 1,2 .... }, SO UE=Oon the complement of a set of measure zero. Hence, u~--0.

    PROPOSITION 6.4. Let ~9         be strongly pseudoconvex. Let K1~K2~ ,..be a
sequence of compact subsets of if2, and let K = n Kj. Then
      (i) (limj_~= u~j)*=u~:,
     (ii) limj_.= C(Kj)=C(K),
     (iii) C*(K)=C(K).

    Proof. Assertion (i) is well-known and may be found, for instance, in [28], Lemma
1. It is a consequence of Dini's theorem and the !ower semicontinuity of the negative of
24                               E. B E D F O R D   A N D B. A. T A Y L O R



the characteristic function of K. Assertion (ii) then follows directly from (i) by Proposi-
tions 5.2 and 5.3. Assertion (iii) follows from (ii) if we take Ks= {z E f2: distance from z
to K ~< l/j}.

       PROPOSITION 6.5. Let ff2~C ~ be strongly pseudoconvex. If E~g2, then

                                       C*(E) = ~ (dd~u~)
                                                      * ".
                                                      Jo
       Proof. First, we note from Corollary 4.3 and (6.2) that if E=~7~g2, (7 an open set,
then




Thus,


                                       S (dd .D" <<.C*(a.
     For the other inequality, it suffices to show there exist open sets ~1=6z= ... such
that f2=D~j.=E and (limj.__,=u6)*~*--ue.* For then, by Proposition 5.2,


                       C*(E) ~< lim. C(~-) = lim. (dd~u~)" = [(dd~u~) ".
                               3--->~        j--->~          J

By Choquet's lemma there exists an increasing sequence (off =P(g2) NL=(~) such that
vi(z)---~O as z---~af2 and limj-~= oj=ue almost everywhere on f2. If ~ = {(1 + 1/j)o~<" 1},
then E=~- and vj<<.u~j<<.ue.Thus limj-_,~ouc=ue a.e., which completes the proof.

       Remark. It follows that uE-*-uc* where G= N~j..

    COROLLARY 6.6. Let ff29 n be strongly pseudoconvex. If E c Q , then C*(E)=0 if
and only/f u~:=0.

       Proof. If E~g2, then the assertion is a direct consequence of Proposition 6.4 and
the uniqueness result of Corollary 4.4. The general case follows from the countable
subadditivity of C* (Proposition 6.1) and the corresponding property for u~ (Proposi-
tion 6.2).

    Definition 6.7. A set E in C n is pluripolar if for each z EE there is an open set q / 3 z
and uEP(~ such that EN ~ c { u = - ~ } .
                     A NEW CAPACITY FOR PLURISUBHARMONIC FUNCTIONS                                  25

     Using the results obtained so far, we can give a simple proof of the following
important theorem of Josefson [16]. The argument given here was given in [2] for the
case n=2, and it works without change in C ", given the relevant properties of C*. We
include the argument only for the convenience of the reader. Sadullaev [24] has
indicated how one may modify the arguments of [2] to give another proof of Josefson's
theorem without using the continuity of (ddC)'', n>~2. As was noted in ([3], Remark 1),
Josefson's theorem automatically covers the case where C" is replaced by an irreduci-
ble Stein space.(l)

   THEOREM 6.8 (Josefson). l f E c C ~ is pluripolar then there exists uCP(C") with
E={u=-~}.

      Proof. Since E is pluripolar, we can find sets Ej, ~j with E j ~ f 2 ~ C ~ such that
LI~.=jEj=E, each f2j is strictly pseudoconvex, and, by Proposition 6.3, u*(Ej, ff2j)=O.
Let il,i2 ..... be a listing of the positive integers so that each one appears infinitely
often. For a sequence cj<c2< .... qi--~+oo, set Mj={zEC": Iz[<Q}. We can choose
ci large enought that s        i and [ z [ - c j < - I on Ei/
      It then follows from Propositions 6.1, 6.3 and Corollary 6.6 and u*(Ei~, if2()--0, that
u*(E(i, Mj)= O. Then, by (6.3), there exists hjEP(Mj) with hi<0 on Mj, hj~<-I on E(~,
and fMj [hi[ dV<2 -J. If we set
                                       ~max (hj(z), [z[-cj),      z e Mj
                              &(z) = (Izl-ej,       z     C~
then p~ E P(C ~) and pj~<- 1 on El; Further
                                                     or



                                           p(z) =         pi(z)
                                                    j=l


is a plurisubharmonic function on C n with p = - ~ on E because the sum converges in
LI(C n, loc), the partial sums are eventually decreasing on each compact subset of C ~,
and each Ej appears infinitely often in the sequence E/; This completes the proof.
     We now prove the main result of this section, the characterization of pluripolar
sets as sets of outer capacity zero.

    THEOREM 6.9. Let ~)~C ~ be strongly pseudoconvex. Then E=g2 is pluripolar if
and only if C*(E)=0.

(1) Added in proof. A result which generalizes Josefson's theorem was given by the first author in "The
operator (daVy' on complex spaces", to appear in S6minaire Lelong-Skoda.

```


## Exact primary application context: Demailly, text lines1790--1860

URL: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf
Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

```text
k tends to +∞.                                                                        

§ 4.C.2. Basic Properties. Here is a short list of the most basic properties.

(4.15) Theorem. For any decreasing sequence (uk ) of subharmonic functions, the limit
u = lim uk is subharmonic.
Proof. A decreasing limit of upper semicontinuous functions is again upper semicontin-
uous, and the mean value inequalities 4.12 remain valid for u by Lebesgue’s monotone
convergence theorem.                                                                

(4.16) Theorem. Let u1 , . . . , up ∈ Sh(Ω) and χ : Rp −→ R be a convex function such
that χ(t1 , . . . , tp ) is non decreasing in each tj . If χ is extended by continuity into a
function [−∞, +∞[p −→ [−∞, +∞[, then
                                      χ(u1 , . . . , up ) ∈ Sh(Ω).
In particular u1 + · · · + up , max{u1 , . . . , up }, log(eu1 + · · · + eup ) ∈ Sh(Ω).
Proof. Every convex function is continuous, hence χ(u1 , . . . , up ) is upper semicontinuous.
One can write
                                    χ(t) = sup Ai (t)
                                                    i∈I

where Ai (t) = a1 t1 + · · · + ap tp + b is the family of affine functions that define supporting
hyperplanes of the graph of χ. As χ(t1 , . . . , tp ) is non-decreasing in each tj , we have
aj ⩾ 0, thus
           X                             X                                                   
                aj uj (x) + b ⩽ µB           aj uj + b ; x, r ⩽ µB χ(u1 , . . . , up ) ; x, r
           1⩽j⩽p
                            § 4. Subharmonic Functions                                           35

for every ball B(x, r) ⊂ Ω. If one takes the supremum of this inequality over all the
Ai ’s , it follows that χ(u1 , . . . , up ) satisfies the mean value inequality 4.12 c). In the last
example, the function χ(t1 , . . . , tp ) = log(et1 + · · · + etp ) is convex because

                            X      ∂ 2χ               X                X        2
                                          ξj ξk = e−χ   ξj2 etj − e−2χ   ξj etj
                                  ∂tj ∂tk
                        1⩽j,k⩽p

      P            2       P 2 tj  χ
and       ξj etj        ⩽    ξj e e by the Cauchy-Schwarz inequality.                            

(4.17) Theorem. If Ω is connected and u ∈ Sh(Ω), then either u ≡ −∞ or u ∈ L1loc (Ω).

Proof. Note that a subharmonic function is always locally bounded above. Let W be the
set of points x ∈ Ω such that u is integrable in a neighborhood of x. Then W is open
by definition and u > −∞ almost everywhere on W . If x ∈ W , one can choose a ∈ W
such that |a − x| < r = 12 d(x, ∁Ω) and u(a) > −∞. Then B(a, r) is a neighborhood of
x, B(a, r) ⊂ Ω and µB (u ; a, r) ⩾ u(a) > −∞. Therefore x ∈ W , W is also closed. We
must have W = Ω or W = ∅ ; in the last case u ≡ −∞ by the mean value inequality. 

(4.18) Theorem. Let u ∈ Sh(Ω) be such that u 6≡ −∞ on each connected component of
Ω. Then

a) r 7−→ µS (u ; a, r), r 7−→ µB (u ; a, r) are non decreasing functions in the interval
   ]0, d(a, ∁Ω)[ , and µB (u ; a, r) ⩽ µS (u ; a, r).
b) For any family (ρε ) of smoothing kernels, u ⋆ ρε ∈ Sh(Ωε ) ∩ C∞ (Ωε , R), the family
   (u ⋆ ρε ) is non decreasing in ε and limε→0 u ⋆ ρε = u.

Proof. We first verify statements a) and b) when u ∈ C 2 (Ω, R). Then ∆u ⩾ 0 and
µS (u ; a, r) is non decreasing in virtue of (4.10). By (4.9), we find that µB (u ; a, r) is also
non decreasing and that µB (u ; a, r) ⩽ µS (u ; a, r). Furthermore, Formula (4.11) shows
that ε 7−→ u ⋆ ρε (a) is non decreasing (provided that ρε is radially symmetric).
   In the general case, we first observe that property 4.12 c) is equivalent to the inequality

                                      u ⩽ u ⋆ µr   on Ωr ,    ∀r > 0,

where µr is the probability measure of uniform density on B(0, r). This inequality implies
u ⋆ ρε ⩽ u ⋆ ρε ⋆ µr on (Ωr )ε = Ωr+ε , thus u ⋆ ρε ∈ C∞ (Ωε , R) is subharmonic on Ωε . It
follows that u ⋆ ρε ⋆ ρη is non decreasing in η ; by symmetry, it is also non decreasing in ε,
and so is u⋆ρε = limη→0 u⋆ρε ⋆ρη . We have u⋆ρε ⩾ u by (4.19) and lim supε→0 u⋆ρε ⩽ u
by the upper semicontinuity. Hence limε→0 u ⋆ ρε = u. Property a) for u follows now

```


## Exact primary application context: Demailly, text lines2020--2190

URL: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf
Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

```text

(4.24) Proposition. If all uα are subharmonic, the upper regularization u⋆ is subhar-
monic and equal almost everywhere to u.
Proof. By Choquet’s lemma we may assume that (uα ) is countable. Then u = sup uα is a
Borel function. As each uα satisfies the mean value inequality on every ball B(z, r) ⊂ Ω,
we get
                  u(z) = sup uα (z) ⩽ sup µB (uα ; z, r) ⩽ µB (u ; z, r).
The right-hand side is a continuous function of z, so we infer

                             u⋆ (z) ⩽ µB (u ; z, r) ⩽ µB (u⋆ ; z, r)

and u⋆ is subharmonic. By the upper semicontinuity of u⋆ and the above inequality we
find u⋆ (z) = limr→0 µB (u ; z, r), thus u⋆ = u almost everywhere by Lebesgue’s lemma.
                                                                                      
                      § 5. Plurisubharmonic Functions                                               39

§ 5. Plurisubharmonic Functions
§ 5.A. Definition and Basic Properties
    Plurisubharmonic functions have been introduced independently by [Lelong 1942] and
[Oka 1942] for the study of holomorphic convexity. They are the complex counterparts
of subharmonic functions.

(5.1) Definition. A function u : Ω −→ [−∞, +∞[ defined on an open subset Ω ⊂ Cn is
said to be plurisubharmonic if

a) u is upper semicontinuous ;
b) for every complex line L ⊂ Cn , u↾Ω∩L is subharmonic on Ω ∩ L.
The set of plurisubharmonic functions on Ω is denoted by Psh(Ω).

   An equivalent way of stating property b) is: for all a ∈ Ω, ξ ∈ Cn , |ξ| < d(a, ∁Ω),
then
                                              Z 2π
                                         1
(5.2)                            u(a) ⩽              u(a + eiθ ξ) dθ.
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
