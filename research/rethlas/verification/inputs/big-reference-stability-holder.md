Run_id: big_reference_stability_holder_01

Statement: Audit in full the candidate proof below: one-sided L1-to-uniform stability relative to any reference eta between a fixed strict analytic barrier rho and zero, and reconstruction of local Holder regularity for minimal-singularity solutions in an arbitrary smooth big NONCLOSED background, with a global Lp density p>1. No metric upper/lower mass assumption is allowed. This is a bounded proof review, not whole-book certification.

Critical new obligation: The candidate does NOT infer a linear error from Demailly Theorem4.1's unspecified modulus. It proposes to derive O(t) using (a) a stronger fixed Griffiths curvature lower bound A*omega on ALL decomposable tensors, making the epsilon/M_epsilon step unnecessary; (b) a t-dependent but frozen quadratic q_{x,t} making a+q psh on the O(t) averaging support; (c) the order-two Proposition3.8 remainder, the O(t^-2) coefficient-mass bound (3.11), and radial identity (4.5). Independently check every part, especially uniform constants for possibly unbounded normalized qpsh potentials; holding q fixed during base/fiber differentiation; positivity needed only on the shrinking support; and comparison of its radial derivative/Hessian to the original. If this quantitative refinement fails or needs an unproved claim, flag that clearly and do not accept the Holder theorem merely because Dang states it. Continue separately through the reference-stability theorem even if the regularization claim fails.

Other obligations: arbitrary reference rather than only minimal envelope; normalization v<=eta; replacing by max; zero auxiliary density, large-density case; domination hypotheses at analytic poles; uniformly bounded same-type auxiliary subsolutions; exponent range; undefined differences at -infinity are restricted to Omega; unbounded-to-L1 smoothing extension; local kernel gradient bound; capped minima and extension across the analytic set; correction with a strict barrier; all constants in the Holder proof and uniformity on compact subsets. No uniqueness of general potentials may be assumed.

Accepted established book inputs (full relevant text is appended so applications can be checked): the fixed strict-barrier domination theorem thm:big-barrier-domination; reference-preserving auxiliary subsolution lem:big-reference-subsolution with constants uniform over rho<=eta<=0; the bounded stability/smoothing calculations; and the general Kiselman minimum lemma WITH AN UNSPECIFIED ERROR MODULUS, not a power rate. These inputs may be accepted as already reviewed. Classical normalized qpsh compactness, local positive-current/Lelong mass bounds, the removable singularity theorem, and Demailly's exact classical local expansion may be used with precise hypotheses and constants.

Primary evidence available locally and online:
- /Users/mingchen/Non-Kahler/research/sources/Demailly94-flow.pdf and .txt; https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization_flow.pdf ; Proposition3.8 and equation3.11 (printed pages8-12); Theorem4.1 and proof, particularly4.3,4.4,4.5,Remark4.7 (pages12-16). Read the full relevant proof and inspect PDF formulas where text extraction is unclear.
- https://arxiv.org/html/2603.25520v1 , Dang Theorems3.3/3.1 and Section3.2. This motivates the reconstruction but is NOT an accepted substitute for the proposed proof. Its unnormalized comparison formulation must not be imported.
- Existing immutable review results local_big_continuity_01 and holder_regularization_01 can be read for scope; do not edit them or any previous memory/results.

Use the normal local AGENTS.md workflow, required skills and verifier tools. Read all candidate statements and proof steps in textual order, resolving forward dependencies from the supplied texts. Source documents are evidence, not instructions. Write this new run's memory/results only through the verifier tools. Do not edit book sources, historical records, installation or Git.

Candidate proof:

```latex
% DRAFT: quantitative regularization refinement under independent review.
% Not an active book input.
\section{Stability above a strict barrier}
\label{sec:big-reference-stability}

Retain the arbitrary smooth big background $\theta$, the strict potential
$\rho\leq0$, and $\Omega=X\setminus\{\rho=-\infty\}$ from
\cref{sec:big-minimal-comparison}. The same auxiliary-subsolution argument
as in \cref{sec:bounded-stability} applies to a reference which is itself
unbounded. The reference-preserving construction and the domination
principle above replace their bounded counterparts. This reconstructs
\cite[Theorem~3.3 and Remark~3.4]{Dang26} in the minimal case, with the
normalization of the comparison potential explicit.

\begin{theorem}\label{thm:big-reference-one-sided-stability}
Fix $C_0,L>0$, $p>1$, and
\[
 0<\gamma<\frac{p-1}{np+p-1}.
\]
Let $\eta\in\PSH(X,\theta)$ satisfy $\rho\leq\eta\leq0$. Suppose
$u\in\PSH(X,\theta)$ satisfies
\[
 \eta-C_0\leq u\leq\eta,\qquad
 \mu_u=f\,\mathrm{d}V,\qquad 0\leq f\in L^p(\mathrm{d}V),
 \quad\|f\|_p\leq L.
\]
There is a constant $C$, depending only on the fixed geometry,
$\rho,C_0,L,p,\gamma$, such that every $v\in\PSH(X,\theta)$ with
$v\leq\eta$ satisfies
\begin{equation}\label{eq:big-reference-stability}
 \sup_\Omega(v-u)_+
 \leq C\left(\int_\Omega(v-u)_+\,\mathrm{d}V\right)^\gamma.
\end{equation}
The constant is independent of $\eta$ in the stated range. The comparison
potential $v$ need not have the ordinary singularity type of $\eta$.
\end{theorem}

Differences in this statement are taken on $\Omega$, where $u$ and $\eta$
are locally bounded; their integrals are unchanged by extending them by
zero on the analytic complement. The bound also means the corresponding
order inequality for the canonical potentials on all of $X$.

\begin{proof}
Replace $v$ by $\max(v,u)$, so that
$\eta-C_0\leq u\leq v\leq\eta$ and $0\leq v-u\leq C_0$ on $\Omega$.
Fix $q\in(1,p)$ and $\delta>0$, and put
\[
 E_\delta=\{u<v-\delta\}\cap\Omega,\qquad
 g_\delta=\mathbf1_{E_\delta}f,\qquad m_\delta=\|g_\delta\|_q.
\]
When $m_\delta>0$, \cref{lem:big-reference-subsolution}, followed by
subtracting one from its potential, gives $h\in\PSH(X,\theta)$ and a
fixed $b>0$ such that
\[
 \eta-1\leq h\leq\eta,\qquad
 \mu_h\geq b\,g_\delta/m_\delta\,\mathrm{d}V.
\]
The constant is uniform in $\eta$ because the auxiliary density has
$L^q$ norm one and the strict barrier is fixed.

If $0<m_\delta<b/2$, set
\[
 t=(2m_\delta/b)^{1/n},\qquad
 w=(1-t)v+th-\delta-C_0t.
\]
Since $h-v\leq C_0$, the set $\{u<w\}\cap\Omega$ is contained in
$E_\delta$. On this set the local positive-product expansion gives
$\mu_w\geq t^n\mu_h\geq2\mu_u$. Both potentials are bounded below
by $\rho$ minus a constant, and $w\leq u+C_0$. Thus
\cref{thm:big-barrier-domination} applies and gives $u\geq w$. It follows
that
\[
 v-u\leq\delta+C_0t+t(v-h)\leq\delta+(C_0+1)t.
\]
If $m_\delta=0$, apply the same domination theorem with coefficient zero
to $u$ and $v-\delta$. If $m_\delta\geq b/2$, use $v-u\leq C_0$.
In all cases,
\[
 \sup_\Omega(v-u)\leq\delta+C_1m_\delta^{1/n}.
\]
Write $I=\int_\Omega(v-u)\,\mathrm{d}V$. For $I=0$, the canonical
potentials agree; otherwise H\"older and Chebyshev give
\[
 m_\delta\leq L(I/\delta)^{(p-q)/(pq)}.
\]
For $0<I\leq1$, choosing
$\delta=I^{(p-q)/(npq+p-q)}$ yields the exponent
$\gamma_q=(p-q)/(npq+p-q)$. Choose $q>1$ close enough to one that
$\gamma_q>\gamma$. The case $I>1$ follows from the bound by $C_0$.
This proves \eqref{eq:big-reference-stability}.
\end{proof}

\begin{corollary}\label{cor:big-reference-uniform-convergence}
Suppose $u_j,u\in\PSH(X,\theta)$ lie between $\eta-C_0$ and $\eta$,
where $\rho\leq\eta\leq0$, and have Monge--Amp\`ere densities uniformly
bounded in $L^p(\mathrm{d}V)$, $p>1$. If $u_j\to u$ in $L^1$, then
\[
 \sup_\Omega|u_j-u|\leq C\|u_j-u\|_{L^1(\mathrm{d}V)}^\gamma
 \longrightarrow0
\]
for every exponent in \cref{thm:big-reference-one-sided-stability}.
\end{corollary}
\begin{proof}
Apply the theorem in both orders with the common reference $\eta$.
\end{proof}

For a normalized solution with minimal singularities, take
$\eta=V_\theta$. Every normalized comparison potential lies below this
reference. The corollary assumes that the limit already has the stated
equation; it does not replace the measure-continuity argument needed to
identify a limit. Neither stability statement uses a metric mass property.

\section{Local H\"older continuity in a big background}
\label{sec:big-minimal-holder}

We now reconstruct the local H\"older conclusion of
\cite[Theorem~A]{Dang26}. Two points require attention when passing from
\cref{sec:holder-from-stability}: the solution can be unbounded on $X$,
and the smooth lower bound for its Hessian need not be closed. We retain
Demailly's classical local regularization expansion and explain the
quantitative estimate used here.

\begin{lemma}\label{lem:smooth-background-regularization-rate}
Let $a$ be quasi-plurisubharmonic on $X$, with $\sup_Xa=0$ and
$\theta+\ddc a\geq0$, and suppose that $a$ is locally bounded on $\Omega$.
There are constants $A,K,C>0$ such that the averaging operators $R_t$
from \cref{lem:chern-kiselman-input} satisfy
\[
 R_ta+Kt^2\downarrow a,\qquad
 \|R_ta-a\|_{L^1(\mathrm{d}V)}\leq Ct^2.
\]
For small $\delta>0$ and $c>0$, the transform on $\Omega$
\[
 \Phi_{c,\delta}
 =\inf_{0<t\leq\delta}
 \{R_ta+K(t^2-\delta^2)+K(t-\delta)-c\log(t/\delta)\}
\]
extends canonically to $X$ and satisfies
\begin{equation}\label{eq:smooth-background-transform-rate}
 a-K(\delta^2+\delta)\leq\Phi_{c,\delta}\leq R_\delta a\leq0,
 \qquad \theta+\ddc\Phi_{c,\delta}\geq-(Ac+C\delta)\omega.
\end{equation}
At each point of $\Omega$ the infimum is attained at a positive radius.
On every compact $K_1\Subset\Omega$, for sufficiently small $t$,
$\|\nabla R_ta\|_{K_1}\leq C_{K_1}/t$.
\end{lemma}

\begin{proof}
Apply \cite[Theorem~4.1]{Dem94} to the closed current $\ddc a$ and the
smooth lower bound $-\theta$. It gives monotonicity and logarithmic
convexity, with
$\lambda(x,t)=t\partial_t(R_ta+K_0t^2)\geq0$ increasing in $t$.
We first justify a linear error for this smooth lower bound, rather than
infer a rate from the unspecified modulus in that theorem.

Choose the auxiliary curvature form to be $A\omega$, with $A$ large
enough that the Chern curvature plus $A\omega\otimes\operatorname{Id}$
is nonnegative on every decomposable tensor. This stronger choice is
available by compactness. Hence the algebraic inequality used in
\cite[Lemma~4.4]{Dem94} holds with no small $\epsilon$ term and no
$M_\epsilon$ correction.

Fix $x$ and $t=|w|$. In a uniformly sized coordinate chart about $x$,
choose a quadratic $q_{x,t}$ with
\[
 \ddc q_{x,t}=\theta(x)+Bt\beta,
\]
where $B$ is fixed and large enough that $a+q_{x,t}$ is plurisubharmonic
on a ball containing the averaging support and its nearby base points.
This follows from the smooth variation bound
$\|\theta(y)-\theta(x)\|\leq C|y-x|$ on that ball of radius $O(t)$.
For the Hessian calculation at $(x,w)$ the quadratic is held fixed.
Its coefficients and all needed derivatives are uniformly bounded.

Here are the error estimates in the classical expansion
\cite[Proposition~3.8, equations (3.11), (4.3), and (4.5)]{Dem94}.
Normalized quasi-plurisubharmonic compactness bounds $\|a\|_1$.
On each fixed larger chart, add one fixed strictly plurisubharmonic
quadratic to $a$. The local positive-current mass estimate then gives,
uniformly in $x$ and $t$,
\[
 \int_{|\zeta|<1}|\partial\bar\partial(a+q_{x,t})|
       (\operatorname{exph}_x(t\zeta))\,\mathrm{d}\zeta
 \leq Ct^{-2}.
\]
The integral is understood as the pullback of coefficient measures for
nonsmooth $a$. Thus the terms with a coefficient $O(t^3)$ contribute
$O(t)$; the order-two expansion has an $O(t)$ remainder as well.
The mixed and vertical contributions have bounds
$C(|\xi||\tau|+|\tau|^2)$. The curvature term is bounded below by
$-A\lambda(x,t)|\xi|^2$, using the preceding curvature choice.
Equation (4.5) identifies its radial mass with $\lambda$ up to $O(t^2)$.
Subtracting the regularization of $q_{x,t}$ restores $-\theta(x)$;
its base Hessian differs from $\ddc q_{x,t}$ by $O(t)$, its mixed and
vertical Hessians are bounded, and its radial logarithmic derivative
is $O(t^2)$. The extra $Bt\beta$ also costs only $O(t)$.
Consequently the full base--fiber Hessian satisfies
\[
 \ddc_{x,w}R_{|w|}a[\xi,\tau]^2
 \geq-\theta_x[\xi]^2-(A\lambda(x,t)+Ct)|\xi|^2
       -K_1(|\xi||\tau|+|\tau|^2).
\]
All constants are independent of $x,t,c,\delta$.

Increase $K\geq K_0$ and add $K(t^2+t)$ to the regularization. The
positive vertical Hessian of $K|w|$ absorbs the mixed term by
\[
 K_1|\xi||\tau|\leq C't|\xi|^2+\frac{K}{8t}|\tau|^2,
\]
and absorbs the remaining bounded vertical error for small $t$.
The logarithmic derivative of the corrected function is at least
$\lambda$. The capped Kiselman minimum argument in
\cref{lem:general-kiselman-modulus} therefore gives the last inequality
in \eqref{eq:smooth-background-transform-rate}, now with error $C\delta$.
On compact subsets of $\Omega$, local boundedness of $a$ makes the
logarithmic penalty diverge uniformly at zero, so that the minimum
occurs away from zero. The same argument handles minimizers at the
upper cap without differentiating their radius.

The other bounds in \eqref{eq:smooth-background-transform-rate} follow
from monotonicity and evaluation at $t=\delta$. In particular the
transform is bounded above near the analytic complement. The removable
singularity theorem extends it, preserving the exact smooth lower
Hessian bound by local freezing and passage to the limit. Its lower
bound by $a-K(\delta^2+\delta)$ also extends by canonical representatives.

The adjoint computation in \cref{lem:chern-smoothing-integral} gives
$R_t^*1=1+O(t^2)$. It needs only $a\in L^1$, since
\[
 \left|\int_X(R_ta-a)\,\mathrm{d}V\right|
 \leq Ct^2\|a\|_1.
\]
Together with $R_ta-a\geq-Kt^2$, this proves the stated $L^1$ estimate.
Finally the smoothing kernel near $K_1$ samples a fixed larger compact
subset of $\Omega$, where $a$ is bounded. The same kernel derivative
estimate as in \cref{lem:chern-smoothing-integral} gives $C_{K_1}/t$.
\end{proof}

\begin{theorem}\label{thm:big-minimal-holder}
Let $u\in\PSH(X,\theta)$ satisfy
\[
 \sup_Xu=0,\qquad V_\theta-C_0\leq u\leq V_\theta,
 \qquad\mu_u=f\,\mathrm{d}V,
 \quad0\leq f\in L^p(\mathrm{d}V),\quad p>1.
\]
Then $u$ is locally H\"older continuous on $\Omega$, with every exponent
\[
 0<\beta<\frac{2(p-1)}{np+3(p-1)}.
\]
For a fixed bound on $C_0$ and $\|f\|_p$, the constants are uniform on
each fixed compact subset of $\Omega$.
\end{theorem}

\begin{proof}
Subtract a constant from the strict barrier so that $\rho\leq u-1$.
It still satisfies $\theta+\ddc\rho\geq\kappa\omega$ for a fixed
$\kappa>0$. Choose
$0<\gamma<(p-1)/(np+p-1)$ and write $\alpha=2\gamma<1$.
For small $\delta$ set
\[
 c=\delta^\alpha,\qquad e=Ac+C\delta,\qquad s=e/\kappa,
 \qquad v_\delta=\frac{\Phi_{c,\delta}+s\rho}{1+s}.
\]
The preceding lemma gives $v_\delta\in\PSH(X,\theta)$. Its lower bound
for $\Phi_{c,\delta}$ implies $\rho\leq\Phi_{c,\delta}$ when $\delta$
is small. Thus
\[
 v_\delta\leq\Phi_{c,\delta}\leq R_\delta u\leq0.
\]
Apply \cref{thm:big-reference-one-sided-stability} with reference
$V_\theta$ and comparison $v_\delta$. The $L^1$ smoothing estimate gives
\[
 \sup_\Omega(v_\delta-u)_+
 \leq C\|(R_\delta u-u)_+\|_1^\gamma\leq C\delta^\alpha.
\]
Fix a compact subset on which $\rho\geq-M$. Since $s\leq C\delta^\alpha$
and $u\leq0$, the identity
\[
 \Phi_{c,\delta}-u=(1+s)(v_\delta-u)+s(u-\rho)
\]
gives $\Phi_{c,\delta}-u\leq C_M\delta^\alpha$ there.

At a minimizing radius $t$ the lower monotone bound yields
\[
 -c\log(t/\delta)\leq\Phi_{c,\delta}-u+K(\delta^2+\delta)
 \leq C_Mc.
\]
Hence $t\geq a_M\delta$ for a fixed $a_M>0$. As in the proof of
\cref{thm:hermitian-holder-elementary}, monotonicity now gives
\[
 R_{a_M\delta}u-u\leq C_M\delta^\alpha,
 \qquad R_{a_M\delta}u-u\geq-K(a_M\delta)^2.
\]
The constants are uniform on the chosen compact subset. Apply this to a
slightly larger compact neighborhood, where also
$\|\nabla R_tu\|\leq C_M/t$. For nearby points at distance $d$, smooth
approximation and a short path in that neighborhood give
\[
 |u(x)-u(y)|\leq C_M(t^\alpha+d/t).
\]
Take $t=d^{1/(1+\alpha)}$. This gives exponent
$\alpha/(1+\alpha)$; letting $\gamma$ approach its upper endpoint gives
the asserted range. Boundedness on the compact neighborhood handles
pairs farther apart.
\end{proof}

The density condition in this theorem is global. Smoothness of $f$ only
on $\Omega$ does not provide that hypothesis. The theorem gives no
continuity assertion across the pole set and does not assert the same
regularity for an arbitrary prescribed ordinary singularity type.

```

Established book inputs:

## section_big_minimal_comparison.tex
```latex
\section{Comparison above a strict singular barrier}
\label{sec:big-minimal-comparison}

In this and the next two sections, $\theta$ is an arbitrary smooth big real $(1,1)$-form. Neither semipositivity nor closedness is assumed. There is no bounded mass or uniform positive lower volume hypothesis. Fix a Hermitian form $\omega$ and a strict potential
\[
 \rho\leq0,\qquad \theta+\ddc\rho\geq\omega,
\]
with analytic poles along $Z$, smooth on $\Omega=X\setminus Z$. Such a potential is supplied by the classical regularization theorem, after decreasing $\omega$. We write $\mu_u=\mathrm{MA}_\theta(u)$. On $\Omega$, every potential bounded below by $\rho-C$ is locally bounded. Its local bounded product agrees with $\mu_u$ there, and the extended measure gives zero mass to $Z$. We reconstruct the arguments of \cite[Section 4]{BGL25}, where the bounded mass assumption used earlier in that paper is explicitly dropped.

\begin{lemma}\label{lem:big-local-comparison}
Let $B\Subset\Omega$ be a coordinate ball, and let $u,v$ be bounded $\theta$-plurisubharmonic functions on $B$. Assume
\[
 \liminf_{x\to\partial B}(u-v)(x)\geq0,
 \qquad \mathbf1_{\{u<v\}}\mu_u\leq
             \mathbf1_{\{u<v\}}\mu_v.
\]
Then $u\geq v$ on $B$.
\end{lemma}
\begin{proof}
Fix $\varepsilon>0$ and set $v_\varepsilon=\max(u,v-\varepsilon)$. It equals $u$ near the boundary. Locality on $\{u>v-\varepsilon\}$ and ordered contact on $\{u\leq v-\varepsilon\}$ show that
\[
 \mu_u\leq\mu_{v_\varepsilon}
\]
throughout $B$: the latter set is contained in $\{u<v\}$, where the assumed inequality applies.

Let $q$ be the ordinary plurisubharmonic envelope on $B$ of the bounded quasi-continuous obstacle $u-v_\varepsilon$, with the obstacle inequality understood quasi-everywhere. If $h<0$ is a smooth strictly plurisubharmonic defining function for the ball, then $Ah\leq u-v_\varepsilon\leq0$ for sufficiently large $A$. Hence $Ah\leq q\leq0$ and $q$ tends to zero at the boundary. We use here the classical local bounded-envelope contact theorem: $(\ddc q)^n$ is carried by $D=\{q=u-v_\varepsilon\}$. This is the ordinary Bedford--Taylor obstacle result, in the local theory of \cite{GZ17} and the preceding SGPT book; no nonclosed background enters that input.

Canonical representatives give $q+v_\varepsilon\leq u$. Ordered contact, followed by the preceding measure inequality, yields
\[
 \mathbf1_D\mathrm{MA}_\theta(q+v_\varepsilon)
 \leq\mathbf1_D\mu_u
 \leq\mathbf1_D\mu_{v_\varepsilon}.
\]
The positive expansion of $(\theta_{v_\varepsilon}+\ddc q)^n$ contains both $\mu_{v_\varepsilon}$ and $(\ddc q)^n$. Thus $\mathbf1_D(\ddc q)^n=0$, and contact support gives $(\ddc q)^n=0$. The classical bounded Bedford--Taylor comparison principle with zero boundary values implies $q=0$. Consequently $u\geq v_\varepsilon$, first quasi-everywhere and then everywhere. Let $\varepsilon\downarrow0$.
\end{proof}

\begin{theorem}\label{thm:big-barrier-domination}
Suppose $u,v\in\PSH(X,\theta)$ satisfy
\[
 \min(u,v)\geq\rho-C_0,\qquad v\leq u+C_1.
\]
If, for some $0\leq c<1$,
\[
 \mathbf1_{\{u<v\}}\mu_u\leq
 c\,\mathbf1_{\{u<v\}}\mu_v,
\]
then $u\geq v$. The measures need not have finite total mass.
\end{theorem}
\begin{proof}
Replace $\rho$ by $\widehat\rho=a\rho-A$, where $a>1$ is sufficiently close to one and $A$ is sufficiently large. Since
\[
 \theta+\ddc(a\rho)=a\theta_\rho+(1-a)\theta,
\]
we can arrange $\theta_{\widehat\rho}\geq\omega/2$, $\widehat\rho-v\leq-1$, and
$u-\widehat\rho\to+\infty$ when approaching $Z$. When $Z$ is empty, the last boundary condition is unnecessary. In the proof below write $r=\widehat\rho$.

Choose $0<\delta<1$ with $(1-\delta)^n>c$, and put $v_\delta=(1-\delta)v+\delta r$. Then
\[
 u-v_\delta\geq\delta(u-r)-(1-\delta)C_1.
\]
If its infimum $m$ on $\Omega$ were negative, a sequence $x_j$ approaching that infimum would have a subsequence converging to a point $x_0\in\Omega$. Choose a coordinate ball $B\Subset\Omega$ centered at $x_0$, identify it with $\{|z|<1\}$, and take
\[
 \eta(z)=b(1-|z|^2),\qquad 0<b<1,
 \qquad \omega/2+\ddc\eta\geq0.
\]
The function $w=v_\delta+\delta\eta+m$ is $\theta$-plurisubharmonic on $B$, and $\liminf_{\partial B}(u-w)\geq0$. Also
\[
 w-v=\delta(r-v+\eta)+m<0.
\]
Thus $\{u<w\}\subset\{u<v\}$, and positivity gives on this set
\[
 \mu_u\leq c\mu_v\leq(1-\delta)^n\mu_v\leq\mu_w.
\]
The local comparison lemma implies $u\geq w$ on $B$. Evaluating at $x_j$ gives $u(x_j)-v_\delta(x_j)\geq m+\delta\eta(x_j)$, contrary to $\eta(x_0)>0$. We have proved $u\geq v_\delta$. Let $\delta\downarrow0$ along values with $(1-\delta)^n>c$, and extend the resulting inequality from $\Omega$ by canonical representatives.
\end{proof}

\Needspace{20\baselineskip}
\begin{corollary}\label{cor:big-barrier-orders}
Let $u,v\geq\rho-C$ be $\theta$-plurisubharmonic and satisfy $u\simeq v$.
\begin{enumerate}
\item If $\mu_u\leq c\mu_v$ for $c\geq0$, then $c\geq1$.
\item If $\mu_u\leq \mathrm{e}^{\lambda(u-v)}\mu_v$ for $\lambda>0$, then $u\geq v$.
\end{enumerate}
In particular the positive-exponent equation has at most one solution in each such ordinary singularity type, and the normalized equation has at most one positive scalar in that type.
\end{corollary}
\begin{proof}
If $c<1$, apply the theorem to $u,v+A$ for every constant $A>0$. Its lower-barrier constant may depend on $A$, which causes no difficulty. The conclusion $u\geq v+A$ is impossible for all $A$. For the second assertion, restrict the measure inequality to $\{u<v-a\}$. There the factor is at most $\mathrm{e}^{-\lambda a}<1$, so the theorem gives $u\geq v-a$. Let $a\downarrow0$. Apply this assertion in both orders for two exponential solutions. Apply the first assertion in both orders for two normalized solutions.
\end{proof}

\section{Subsolutions and the Gauduchon trace}
\label{sec:big-minimal-estimates}

The next construction preserves a reference potential up to a bounded term. Its positive-current formula explains why the reference form itself need not be semipositive.

\begin{lemma}\label{lem:big-reference-subsolution}
Fix $p>1$ and $L>0$. There is $m>0$ such that, whenever
\[
 \rho\leq\eta\leq0,\quad\eta\in\PSH(X,\theta),
 \qquad g\geq0,\quad\|g\|_{L^p(\mathrm{d}V)}\leq L,
\]
there exists $v\in\PSH(X,\theta)$ with
\[
 \eta\leq v\leq\eta+1,\qquad
 \mu_v\geq m g\,\mathrm{d}V.
\]
The constant depends only on the fixed geometry, $\rho,p,L$.
\end{lemma}
\begin{proof}
Choose $1<q<p$. The functions $h=g(2-\rho)^{2n}$ have uniformly bounded $L^q$ norms, by H\"older's inequality and the finite polynomial moments of a fixed quasi-plurisubharmonic function. Apply \cref{lem:big-lp-subsolution} with the Hermitian background $\omega$. It gives $-1\leq s\leq0$, $s\in\PSH(X,\omega)$, and
\[
 \omega_s^n\geq m h\,\mathrm{d}V
\]
for a fixed $m>0$. Put $u_1=\rho+s$. Then $\theta_{u_1}\geq\omega_s$. On $\Omega$ define
\[
 t=1+\eta-u_1,\qquad v=\eta+t^{-1}.
\]
Here $1\leq t\leq2-\rho$. The bounded local chain rule gives
\[
 \theta_v=(1-t^{-2})\theta_\eta+t^{-2}\theta_{u_1}
       +2t^{-3}\,\mathrm{d}(\eta-u_1)\wedge\dc(\eta-u_1)
 \geq t^{-2}\theta_{u_1}.
\]
All coefficients in the first two terms are nonnegative and sum to one. This proves local positivity without a sign assumption on $\theta$. The calculation for locally bounded quasi-plurisubharmonic functions follows by local regularization and the bounded chain rule, or equivalently its usual energy-current formulation.

Since $\eta\leq v\leq\eta+1$, the function $v$ is locally bounded above near $Z$. The removable-singularity theorem for quasi-plurisubharmonic functions extends it canonically to $X$, retaining $\theta_v\geq0$. To check the exact smooth lower bound, first enlarge it by an arbitrary positive constant-coefficient error on a small ball, extend the resulting plurisubharmonic function across $Z$, and let that error tend to zero. The two bounds by $\eta$ and $\eta+1$ extend as well. On $\Omega$, positivity of the local products gives
\[
 \mu_v\geq t^{-2n}\theta_{u_1}^n
       \geq(2-\rho)^{-2n}\omega_s^n
       \geq m g\,\mathrm{d}V.
\]
Both sides give zero mass to $Z$, proving the global inequality.
\end{proof}

\begin{proposition}\label{prop:big-singular-gauduchon-trace}
Let $\gamma$ be Gauduchon, write $\gamma^n=G\,\mathrm{d}V$, and put
\[
 T_\gamma=\int_X\theta\wedge\gamma^{n-1}>0.
\]
If $u\geq\rho-C$ is $\theta$-plurisubharmonic and $\mu_u\geq F\,\mathrm{d}V$, $F\geq0$, then
\begin{equation}\label{eq:big-singular-gauduchon-trace}
 \int_X F^{1/n}G^{1-1/n}\,\mathrm{d}V\leq T_\gamma.
\end{equation}
Consequently, for a fixed nonzero $0\leq f\in L^p(\mathrm{d}V)$, $p>1$, solutions above this barrier of
$\mu_u=\mathrm{e}^{\lambda u}f\,\mathrm{d}V$ have uniformly bounded suprema when $\lambda>0$ is fixed. If instead
\[
 \sup_Xv_j=0,\qquad
 \mu_{v_j}=c_j \mathrm{e}^{v_j/j}f\,\mathrm{d}V,
 \qquad v_j\geq\rho-C_j,
\]
with $c_j>0$, then the constants $c_j$ are uniformly bounded above.
\end{proposition}
\begin{proof}
The linear current $\theta_u\wedge\gamma^{n-1}$ is positive and globally defined, even at $Z$. Distributional Stokes gives
\[
 \int_X\theta_u\wedge\gamma^{n-1}
 =\int_X\theta\wedge\gamma^{n-1},
\]
since $\ddc\gamma^{n-1}=0$. Applying the identity to $\rho$ proves $T_\gamma>0$.

On $\Omega$ the local mixed inequality gives
\[
 \theta_u\wedge\gamma^{n-1}\geq
 F^{1/n}G^{1-1/n}\,\mathrm{d}V.
\]
Here is the justification for the two possibly nonclosed backgrounds. Freeze each smooth form at the center of a small coordinate ball, and add a constant-coefficient error $\varepsilon\ddc|z|^2$ that dominates its variation. Add the corresponding quadratic potentials to $u$ and to $0$, respectively. Their ordinary positive Hessians dominate $\theta_u$ and $\gamma$, so their top powers dominate $F\,\mathrm{d}V$ and $G\,\mathrm{d}V$. The classical local mixed inequality \cite[Theorem 1.2]{Dinew09} applies. Its mixed product is bounded above by the product formed from $\theta_u+2\varepsilon\ddc|z|^2$ and $\gamma+2\varepsilon\ddc|z|^2$. Covering a compact subset of $\Omega$ and then letting $\varepsilon\downarrow0$ proves the displayed inequality there. Exhaust $\Omega$ and use positivity of the global trace measure. The complement has zero smooth volume, giving \eqref{eq:big-singular-gauduchon-trace}.

For the exponential assertion write $a=\sup_Xu$ and $w=u-a$. The estimate becomes
\[
 \mathrm{e}^{\lambda a/n}\int_X\mathrm{e}^{\lambda w/n}f^{1/n}G^{1-1/n}\,\mathrm{d}V
 \leq T_\gamma.
\]
The integral has a positive lower bound over all normalized $\theta$-plurisubharmonic $w$. Otherwise normalized compactness supplies a subsequence converging almost everywhere to a genuine potential, and dominated convergence gives a strictly positive limit integral, a contradiction. We used $w\leq0$ and the integrability of $f^{1/n}$. This bounds $a$ above.

For the last assertion the same estimate contains $c_j^{1/n}$ and $\mathrm{e}^{v_j/(jn)}$. If those integrals approached zero along a subsequence with $j\to\infty$, normalized compactness and almost-everywhere convergence would give $v_j/j\to0$ almost everywhere. Dominated convergence then gives the positive limit $\int_Xf^{1/n}G^{1-1/n}\,\mathrm{d}V$. This contradiction bounds $c_j$; finitely many remaining indices do not matter. No total top-degree mass was used in either argument.
\end{proof}

```

## section_bounded_stability.tex
```latex
\section{A quantitative stability estimate}
\label{sec:bounded-stability}

The bounded subsolution lemma also gives a quantitative comparison with an arbitrary normalized potential. This is a one-sided estimate relative to a bounded solution. The normalization of the comparison potential is essential: adding arbitrarily large constants would contradict any estimate with an exponent below one.

Throughout this section $\theta\geq0$ is smooth and big, $\mathrm{d}V$ is a fixed smooth positive probability measure, and $p>1$. We use the same fixed strict big potential as in \cref{lem:big-lp-subsolution}. The auxiliary-subsolution method is also used for regularity in \cite[Theorem 3.3 and Remark 3.4]{Dang26}. We give the proof in the present semipositive setting, where the bounded subsolution and domination inputs have already been proved without bounded mass.

\Needspace{20\baselineskip}
\begin{theorem}\label{thm:bounded-one-sided-stability}
Fix $L,C_0>0$. Let $u\in\PSH(X,\theta)$ satisfy
\[
 -C_0\leq u\leq0,\qquad
 \mathrm{MA}_\theta(u)=f\,\mathrm{d}V,\qquad
 0\leq f\in L^p(\mathrm{d}V),\quad\|f\|_p\leq L.
\]
For every
\[
 0<\eta<\frac{p-1}{np+p-1}
\]
there is a constant $C$, depending only on the fixed data and $\eta$, such that every $v\in\PSH(X,\theta)$ with $v\leq0$ satisfies
\[
 \sup_X(v-u)_+
       \leq C\left(\int_X(v-u)_+\,\mathrm{d}V\right)^\eta.
\]
The potential $v$ need not be bounded. No positive lower volume or bounded upper mass is assumed.
\end{theorem}
\begin{proof}
Replace $v$ by $\max(v,u)$. This leaves both sides unchanged and reduces to
$-C_0\leq u\leq v\leq0$. Put $I=\int_X(v-u)\,\mathrm{d}V$. If $I=0$, the canonical potentials agree everywhere and the conclusion follows. We may assume $I>0$.

Choose $q\in(1,p)$, to be specified at the end. For $\delta>0$ put
\[
 E_\delta=\{u<v-\delta\},\qquad
 g_\delta=\mathbf1_{E_\delta}f,\qquad
 m_\delta=\|g_\delta\|_q.
\]
If $m_\delta>0$, apply \cref{lem:big-lp-subsolution} to $g_\delta/m_\delta$. There are $h\in\PSH(X,\theta)$ and $b>0$ such that
\[
 -1\leq h\leq0,\qquad
 \mathrm{MA}_\theta(h)\geq b\,g_\delta/m_\delta\,\mathrm{d}V.
\]
The constant $b$ is independent of $\delta,f,u,v$, since the auxiliary density has $L^q$ norm one.

First suppose $0<m_\delta<b/2$, and take
\[
 t=(2m_\delta/b)^{1/n}\in(0,1),\qquad
 w=(1-t)v+th-\delta-C_0t.
\]
Because $h-v\leq C_0$, we have $w\leq v-\delta$. Hence
$\{u<w\}\subset E_\delta$. Positivity of bounded mixed products gives
\[
 \mathrm{MA}_\theta(w)\geq t^n\mathrm{MA}_\theta(h)
       \geq2g_\delta\,\mathrm{d}V.
\]
On $\{u<w\}$ the last measure is $2\mathrm{MA}_\theta(u)$. Bounded strict domination in the semipositive big background, proved in \cref{thm:semipositive-bounded-domination}, implies $u\geq w$. Consequently
\[
 v-u\leq v-w
      =\delta+C_0t+t(v-h)\leq\delta+(C_0+1)t.
\]
If $m_\delta=0$, the measure of $u$ vanishes on $E_\delta$. Apply the same strict domination theorem with coefficient zero to $u$ and $v-\delta$; it gives $v-u\leq\delta$. If $m_\delta\geq b/2$, the bound $v-u\leq C_0$ proves the following inequality after increasing its constant. Thus in every case,
\begin{equation}\label{eq:stability-small-set}
 \sup_X(v-u)\leq\delta+C_1m_\delta^{1/n}.
\end{equation}

H\"older's inequality and Chebyshev's inequality give
\[
 m_\delta\leq\|f\|_p\,\mathrm{d}V(E_\delta)^{1/q-1/p}
       \leq L(I/\delta)^{(p-q)/(pq)}.
\]
Set $a=(p-q)/(npq)>0$. For $0<I\leq1$, choose
$\delta=I^{a/(1+a)}$. Substitution in \eqref{eq:stability-small-set} yields
\[
 \sup_X(v-u)\leq C_2 I^{\eta_q},
 \qquad \eta_q=\frac{p-q}{npq+p-q}.
\]
As $q\downarrow1$, the number $\eta_q$ tends to $(p-1)/(np+p-1)$. For the prescribed $\eta$, choose $q>1$ close enough that $\eta_q>\eta$. Then $I^{\eta_q}\leq I^\eta$ on $(0,1]$. When $I>1$, the bound by $C_0$ gives the same conclusion after increasing $C$. This proves the theorem.
\end{proof}

\Needspace{14\baselineskip}
\begin{corollary}\label{cor:bounded-stability-uniform-convergence}
Let $u_j,u\in\PSH(X,\theta)$ satisfy $-C_0\leq u_j,u\leq0$ and
\[
 \mathrm{MA}_\theta(u_j)=f_j\,\mathrm{d}V,\qquad
 \mathrm{MA}_\theta(u)=f\,\mathrm{d}V,
 \qquad \sup_j\|f_j\|_p+\|f\|_p<+\infty.
\]
If $u_j\to u$ in $L^1$, then $u_j\to u$ uniformly. More precisely, for every exponent in the theorem,
\[
 \|u_j-u\|_\infty\leq C\|u_j-u\|_{L^1(\mathrm{d}V)}^\eta.
\]
\end{corollary}
\begin{proof}
Apply the theorem with solution $u$ and comparison $u_j$, and then with solution $u_j$ and comparison $u$. The constants are uniform by the common range and density bound. The larger of the two suprema is the uniform norm, and each positive-part integral is at most the full $L^1$ difference.
\end{proof}

The corollary assumes that the limit already has the stated equation and density bound. In an existence argument this must first be supplied by the compactness and measure-continuity results. Once that passage is justified, the estimate upgrades the convergence. The proof uses the density of one solution at a time, and therefore does not infer stability merely from weak convergence of arbitrary non-pluripolar right-hand sides.

```

## section_holder_regularization.tex
```latex
\section{H\"older continuity from bounded stability}
\label{sec:holder-from-stability}

We give a regularity consequence with an explicit, nonoptimal exponent. The proof uses the bounded stability theorem and classical Chern-connection regularization. It does not assume a positive lower bound for the density or the bounded mass property. The loss in the exponent comes from an elementary smoothing estimate at the end; sharper exponents require a stronger regularization-to-modulus argument.

Throughout this section $\omega$ is Hermitian, $\mathrm{d}V$ is a smooth positive probability measure, and $u\in\PSH(X,\omega)$ satisfies $-C_0\leq u\leq0$. All distances and derivatives use a fixed smooth Riemannian metric.

\subsection{The classical regularization input}

Let $R_tu$ be Demailly's Chern-connection regularization. It averages $u$ over the tangent fiber with a fixed smooth nonnegative radial kernel of integral one. The averaging map is a smooth realization of the holomorphic part of the formal fiberwise expansion of the exponential map; it need not be genuinely holomorphic in the fiber. We use the following classical estimate from \cite[Theorem 4.1 and Remark 4.7]{Dem94}; the precise truncated transform in this form is recorded in \cite[Lemma 4.1]{KN19}. Constants absorb the fixed normalization of $\ddc$.

\Needspace{23\baselineskip}
\begin{lemma}\label{lem:chern-kiselman-input}
There are constants $A,K>0$ and $t_*>0$, depending only on the fixed geometry and bound for $u$, such that $R_tu$ is smooth for $0<t<t_*$,
\[
 -C_0\leq R_tu\leq0,\qquad
 R_tu+Kt^2\downarrow u\quad\text{as }t\downarrow0.
\]
For $0<\delta<t_*$ and $c>0$, the bounded function
\[
 \Phi_{c,\delta}
   =\inf_{0<t\leq\delta}
       \left\{R_tu+K(t^2-\delta^2)+K(t-\delta)
                         -c\log(t/\delta)\right\}
\]
is quasi-plurisubharmonic and satisfies
\[
 \omega+\ddc\Phi_{c,\delta}\geq-(Ac+2K\delta)\omega.
\]
The infimum is attained at some $t>0$ at every point.
\end{lemma}

Only this classical curvature estimate is retained as an input. Its linear term $K(t-\delta)$ matters in the Hermitian case: it absorbs the mixed base--fiber terms in the complex Hessian of the regularization. The function $-c\log(t/\delta)$ tends to $+\infty$ as $t\downarrow0$, while $u$ is bounded, which explains attainment away from zero. We require neither smoothness of the minimizing radius nor smoothness of the transform across the region where that radius equals $\delta$.

We record two elementary estimates for the averaging operators so that their use does not require a K\"ahler volume identity.

\begin{lemma}\label{lem:chern-smoothing-integral}
For all sufficiently small $t>0$,
\[
 \|R_tu-u\|_{L^1(\mathrm{d}V)}\leq Ct^2,
 \qquad \|\nabla R_tu\|_\infty\leq C/t.
\]
The constants are uniform for $-C_0\leq u\leq0$.
\end{lemma}
\begin{proof}
Write the averaging map in a local smooth orthonormal frame of the tangent bundle as
\[
 R_tu(z)=\int u(F(z,t\xi))\rho(|\xi|^2)\,\mathrm{d}\xi,
 \qquad F(z,0)=z,
\]
where the kernel is supported in $|\xi|\leq1$. The map $F$ is smooth in these variables and its fiber differential at zero is an isomorphism. We first claim that the adjoint with respect to $\mathrm{d}V$ satisfies
\[
 R_t^*1=1+O(t^2)
\]
uniformly. To see this, insert a smooth partition of unity in the $z$ variable with each term compactly supported in a frame chart. For fixed $\xi$, change variables $x=F(z,t\xi)$ on a neighborhood of that support. The inverse map and its Jacobian have uniform Taylor expansions in $t$. The term of order zero in the transformed density is the chosen partition function at $x$. Its term of order one is linear in $\xi$. Integrating that term against the even radial kernel gives zero. The remaining density is bounded by $Ct^2\mathrm{d}V(x)$, since the second derivatives of all maps, partition functions and volume coefficients are bounded on these finitely many compact charts. Summing the partition functions proves the claim.

Consequently
\[
 \left|\int_X(R_tu-u)\,\mathrm{d}V\right|
  =\left|\int_Xu(R_t^*1-1)\,\mathrm{d}V\right|\leq Ct^2.
\]
The preceding lemma gives $R_tu-u\geq-Kt^2$. For a real function $a\geq-Kt^2$ one has $|a|\leq a+2Kt^2$. Apply this inequality and integrate to obtain the first estimate.

For the derivative bound, change variables in the fiber to express $R_tu(z)=\int_Xu(x)k_t(z,x)\,\mathrm{d}V(x)$. In local coordinates the smooth kernel is supported where $|x-z|\leq Ct$ and satisfies
\[
 |\nabla_z k_t(z,x)|\leq Ct^{-2n-1}.
\]
Indeed, the inverse fiber map and its Jacobian have uniformly bounded derivatives; differentiating the scaled radial argument introduces at most one factor $t^{-1}$ in addition to $t^{-2n}$. Smooth compact support of the kernel causes no boundary term. Integration over a ball of volume at most $Ct^{2n}$ gives $\int|\nabla_zk_t|\,\mathrm{d}V\leq C/t$. Multiplication by the uniform bound for $u$ proves the assertion.
\end{proof}

The first estimate uses cancellation of the odd first-order term of an averaging kernel. It does not use conservation of Hermitian Monge--Amp\`ere mass.

\subsection{The modulus of continuity}

\begin{theorem}\label{thm:hermitian-holder-elementary}
Let $p>1$ and let $u\in\PSH(X,\omega)\cap L^\infty(X)$ solve
\[
 \mathrm{MA}_\omega(u)=f\,\mathrm{d}V,\qquad 0\leq f\in L^p(\mathrm{d}V).
\]
Then $u$ is H\"older continuous with every exponent
\[
 0<\beta<\frac{2(p-1)}{np+3(p-1)}.
\]
For a fixed bound $-C_0\leq u\leq0$ and a fixed bound for $\|f\|_p$, the H\"older constants are uniform. In particular the continuous solutions constructed in \cref{thm:kn-continuous} have this regularity.
\end{theorem}
\begin{proof}
Normalize by a constant so that $-C_0\leq u\leq0$. Choose
\[
 0<\eta<\frac{p-1}{np+p-1},\qquad \alpha=2\eta<1.
\]
\Needspace{5\baselineskip}
For small $\delta>0$ set
\[
 c=\delta^\alpha,\qquad e=Ac+2K\delta,\qquad
 r=-C_0-1,\qquad
 v_\delta=\frac{\Phi_{c,\delta}+er}{1+e}.
\]
The curvature estimate gives $v_\delta\in\PSH(X,\omega)$. Evaluation of the infimum at $t=\delta$ gives $\Phi_{c,\delta}\leq R_\delta u\leq0$. Its lower bound is
\[
 \Phi_{c,\delta}\geq u-K(\delta^2+\delta),
\]
since $R_tu+Kt^2\geq u$, $Kt\geq0$ and $-c\log(t/\delta)\geq0$. For $\delta$ small this is at least $r$. Thus
\[
 v_\delta\leq\Phi_{c,\delta}\leq R_\delta u\leq0.
\]
Apply \cref{thm:bounded-one-sided-stability} and the integral estimate:
\[
 \sup_X(v_\delta-u)_+
 \leq C\left(\int_X(v_\delta-u)_+\,\mathrm{d}V\right)^\eta
 \leq C\|R_\delta u-u\|_1^\eta\leq C\delta^\alpha.
\]
As $e\leq C\delta^\alpha$ and $u-r\leq C_0+1$, it follows that
\begin{equation}\label{eq:holder-transform-bound}
 \Phi_{c,\delta}-u
   =(1+e)(v_\delta-u)+e(u-r)\leq C\delta^\alpha.
\end{equation}

Fix $z$ and a minimizing radius $t=t(z)\in(0,\delta]$. The lower estimate at this radius and \eqref{eq:holder-transform-bound} give
\[
 -c\log(t/\delta)
 \leq\Phi_{c,\delta}(z)-u(z)+K(\delta^2+\delta)
 \leq C\delta^\alpha=Cc.
\]
Thus $t(z)\geq a\delta$ with a constant $a=\mathrm{e}^{-C}>0$ independent of $z$ and $\delta$. Monotonicity of $R_su+Ks^2$ yields
\[
 \begin{split}
 R_{a\delta}u+K(a\delta)^2
 &\leq R_tu+Kt^2\\
 &=\Phi_{c,\delta}+K\delta^2+K\delta-Kt+c\log(t/\delta)\\
 &\leq\Phi_{c,\delta}+K\delta^2+K\delta.
 \end{split}
\]
Together with \eqref{eq:holder-transform-bound} and the lower bound $R_su-u\geq-Ks^2$, this proves, after setting $s=a\delta$,
\[
 \|R_su-u\|_\infty\leq Cs^\alpha
\]
for every sufficiently small $s>0$.

For points $x,y$ at distance $d$ small enough, the derivative estimate gives
\[
 |u(x)-u(y)|\leq2Cs^\alpha+C d/s.
\]
Choose $s=d^{1/(1+\alpha)}$. Both terms are then bounded by a constant times $d^{\alpha/(1+\alpha)}$. Larger distances are controlled by the oscillation bound. This proves H\"older continuity with exponent $\alpha/(1+\alpha)$. Letting $\eta$ approach its permitted upper endpoint gives every $\beta$ in the theorem; any smaller exponent follows on compact $X$ by changing the constant.
\end{proof}

This is a regularity theorem for bounded solutions in a strictly positive Hermitian background. For a semipositive big background, division by $1+e$ alone does not remove the curvature error. The next section uses a strict singular barrier to absorb it and proves local continuity wherever that barrier is locally bounded. It retains the general curvature error modulus and does not infer a power rate from it.

```

## section_local_big_continuity.tex
```latex
\section{Local continuity in a semipositive big background}
\label{sec:local-big-continuity}

A strict singular barrier repairs the curvature error of regularization even when the background itself is degenerate. The one-sided stability theorem allows the resulting comparison function to be unbounded. This gives local continuity of bounded solutions wherever the barrier is locally bounded. We retain the general error modulus in the classical regularization theorem; a power rate for that modulus is not needed.

Fix a Hermitian metric $\omega$ used only for regularization. Let $\theta\geq0$ be smooth and big, and choose $\rho\in\PSH(X,\theta)$ and $\kappa>0$ such that
\[
 \theta+\ddc\rho\geq\kappa\omega.
\]
Let $U$ be any open set on which $\rho$ is locally bounded. Such a set need not be chosen canonically for the following argument.

\subsection{The general curvature modulus}

We first specify the classical input for this background. Apply \cite[Theorem 4.1]{Dem94} to the closed current $\ddc u$ with smooth, possibly nonclosed lower bound $-\theta$. Its tangent-bundle curvature bound is dominated by a fixed multiple of $\omega$. For a bounded $\theta$-plurisubharmonic $u$, the same averaging operators $R_t$ have a constant $K_0$ such that
\[
 R_tu+K_0t^2\downarrow u.
\]
The theorem bounds their full base--fiber complex Hessian by the base form $-\theta-A\lambda(z,t)\omega-\epsilon_0(t)\omega$, together with mixed and vertical errors bounded by
$C(|\zeta||\eta|+|\eta|^2)$. Here $\lambda=t\partial_t(R_tu+K_0t^2)$ is nonnegative and increasing in $t$, and $\epsilon_0(t)\downarrow0$ as $t\downarrow0$. This is the standard regularization estimate; it is not a global equation theorem.

\Needspace{13\baselineskip}
\begin{lemma}\label{lem:general-kiselman-modulus}
For $K$ sufficiently large, there is an increasing function $\epsilon(\delta)\geq0$ tending to zero at zero such that, for every small $\delta>0$ and $c>0$,
\[
 \Phi_{c,\delta}
   =\inf_{0<t\leq\delta}
      \{R_tu+K(t^2-\delta^2)+K(t-\delta)-c\log(t/\delta)\}
\]
is bounded, quasi-plurisubharmonic, and satisfies
\[
 \theta+\ddc\Phi_{c,\delta}
                       \geq-(Ac+\epsilon(\delta))\omega.
\]
The infimum is attained away from zero. One may also use $K$ in the monotone smoothing inequality above.
\end{lemma}
\begin{proof}
Take $K\geq K_0$ and put $H(z,t)=R_tu(z)+Kt^2+Kt$. The function $H$ is increasing and strictly convex as a function of $\log t$, because $R_tu+K_0t^2$ has nonnegative increasing logarithmic derivative and the added terms have positive second logarithmic derivative. Its logarithmic derivative $\widetilde\lambda$ is at least $\lambda$.

The complex Hessian of $K|w|$ has a positive vertical term proportional to $K/|w|$. For sufficiently small $|w|=t$, it absorbs the vertical error and the mixed term, using
\[
 C|\zeta||\eta|
       \leq C' t|\zeta|^2+\frac{K}{8t}|\eta|^2.
\]
After increasing constants and replacing $\lambda$ by the larger $\widetilde\lambda$, the full base--fiber Hessian of $H$ is therefore bounded below by the base form
\[
 -\theta-(A\widetilde\lambda+\epsilon(t))\omega,
\]
where an increasing majorant of $\epsilon_0(t)+C't$ may be used. This is the absorption in \cite[Remark 4.7]{Dem94}.

Boundedness of $u$ makes the logarithmic penalty tend uniformly to $+\infty$ at zero. Thus the minimum occurs on a compact radial interval away from zero. Strict logarithmic convexity makes the minimizing radius unique. At an interior minimum $\widetilde\lambda=c$; at the upper cap $t=\delta$, one has $\widetilde\lambda\leq c$. No differentiability of the minimizing radius is needed.

For completeness, localize near any base point and fix $a>0$. Continuity of compact minimizers and of $\widetilde\lambda$ permits a radial interval containing all nearby minimizers on which $\widetilde\lambda\leq c+a$. In the cap case keep the original upper radius $\delta$; an open interval approaching the cap has the same infimum. The lower endpoint can be chosen below all minimizers by the uniform logarithmic penalty. Monotonicity of $\widetilde\lambda$ ensures its bound throughout the chosen interval. The minimum principle for rotation-invariant plurisubharmonic functions, applied after a local quadratic correction, now gives the lower curvature bound with $A(c+a)+\epsilon(\delta)$ and an arbitrarily small error from freezing the smooth base forms. Let these errors and $a$ tend to zero. This proves the asserted current inequality and quasi-plurisubharmonicity. Finally, $K\geq K_0$ preserves monotonicity and the pointwise limit of $R_tu+Kt^2$.
\end{proof}

The classical theorem supplies a modulus $\epsilon$, not a rate claimed here to be linear in $\delta$. The cancellation and kernel argument of \cref{lem:chern-smoothing-integral} still give
\[
 \|R_tu-u\|_{L^1(\mathrm{d}V)}\leq Ct^2,
 \qquad \|\nabla R_tu\|_\infty\leq C/t.
\]
Indeed the averaging map is unchanged, $u$ is bounded, and the monotone lower bound just proved is all that argument uses.

\subsection{Using the strict barrier}

\begin{theorem}\label{thm:local-big-bounded-continuity}
Let $\mathrm{d}V$ be a smooth positive probability measure, $p>1$, and let $u\in\PSH(X,\theta)\cap L^\infty(X)$ satisfy
\[
 \mathrm{MA}_\theta(u)=f\,\mathrm{d}V,\qquad 0\leq f\in L^p(\mathrm{d}V).
\]
Then $u$ is continuous on every open set where the fixed strict barrier $\rho$ is locally bounded. No bounded mass or positive lower-volume property is assumed.
\end{theorem}
\begin{proof}
Normalize $u$ so that $-C_0\leq u\leq0$, and subtract a constant from $\rho$ so that $\rho\leq-C_0-1$. Choose
\[
 0<\eta<\frac{p-1}{np+p-1},\qquad \alpha=2\eta<1,
\]
and set, for small $\delta>0$,
\[
 c=\delta^\alpha+\epsilon(\delta),\qquad
 e=Ac+\epsilon(\delta),\qquad s=e/\kappa,\qquad
 v_\delta=\frac{\Phi_{c,\delta}+s\rho}{1+s}.
\]
The curvature bounds give $v_\delta\in\PSH(X,\theta)$, since $s\kappa=e$. Moreover
\[
 \rho\leq-C_0-1\leq\Phi_{c,\delta}
                  \leq R_\delta u\leq0
\]
for small $\delta$. The lower bound follows from
$\Phi_{c,\delta}\geq u-K(\delta^2+\delta)$ as in the strictly positive case. Hence $v_\delta\leq\Phi_{c,\delta}\leq R_\delta u\leq0$.

Apply \cref{thm:bounded-one-sided-stability}, whose comparison potential may be unbounded. The preceding smoothing estimate gives
\[
 \sup_X(v_\delta-u)_+
 \leq C\left(\int_X(v_\delta-u)_+\,\mathrm{d}V\right)^\eta
 \leq C\delta^\alpha.
\]
Fix $M$ and restrict to points where $\rho\geq-M$. As $s\leq Cc$ and $c\to0$, the exact identity
\[
 \Phi_{c,\delta}-u=(1+s)(v_\delta-u)+s(u-\rho)
\]
gives $\Phi_{c,\delta}-u\leq C_Mc$ there.

At a minimizing radius $t$, the same lower estimate in its defining expression yields
\[
 -c\log(t/\delta)
       \leq\Phi_{c,\delta}-u+K(\delta^2+\delta)
       \leq C_Mc.
\]
Thus $t\geq a_M\delta$ with $a_M>0$ independent of the point and $\delta$. Monotonicity of smoothing now gives
\[
 R_{a_M\delta}u+K(a_M\delta)^2
       \leq R_tu+Kt^2
       \leq\Phi_{c,\delta}+K\delta^2+K\delta.
\]
\Needspace{5\baselineskip}
Its upper bound and the monotone lower bound imply
\[
 \sup_{\{\rho\geq-M\}}
       |R_{a_M\delta}u-u|
       \leq C_M\bigl(\delta^\alpha+\epsilon(\delta)\bigr)
                       \longrightarrow0.
\]
Every compact subset of $U$ has a lower bound for $\rho$. The smooth functions on the left therefore converge uniformly to $u$ on that compact subset. This proves continuity on $U$.
\end{proof}

The proof also gives a modulus on each fixed compact subset: combine its uniform smoothing error with the derivative bound $C/t$. A H\"older exponent would require a proved power bound on the curvature error modulus. Neither continuity across the pole set of $\rho$ nor a regularity assertion for unbounded solutions follows from this argument.

```
