# Exact P21 original-request completion review

## Original catalogue evidence

2.21    P21: Approximation of ﬁber-selected sections by a base singularity
Status: open in the stated generality. Book locator: Problem 32.9.2, printed p. 897.
Setup and scope. The complete statement below ﬁxes every geometric datum. The descent
H 0 (X, π ∗ Am ) = H 0 (B, Am ) uses compact connected ﬁbers. Its selected subspaces can nevertheless
record singularities upstairs that are not pullbacks of any one base potential.
Full problem statement. Let π : X → B be a surjective holomorphic submersion of connected
compact complex manifolds with connected ﬁbers, where B is Kähler of dimension q ≥ 1. Fix a
Hermitian form ω on X, a holomorphic line bundle A with a smooth Hermitian metric h on B, and
φ ∈ PSH(X, ω). Set θ = c1 (A, h). For positive integers m, identify
                                    (                   )
                          Vm = H 0 X, π ∗ Am ⊗ I(mφ) ⊆ H 0 (B, Am )

by holomorphic descent. Find geometric or analytic conditions that produce ψ ∈ PSH(B, θ) of
positive non-pluripolar mass such that, for all suﬃciently large m,
                                          (                 )
                               Wm = H 0 B, Am ⊗ I(mψ) ⊆ Vm ,
                                     dim Vm − dim Wm = o(mq ).

Determine which features of the singularities of φ along the ﬁbers suﬃce for this approximation.
State of the art. When the selecting data descend, the base equilibrium theorem gives a precise
limit. For isolated point constraints upstairs, ﬁberwise integrability yields base vanishing conditions;
the resulting codimension is lower order and kernel diﬀerences have vanishing normalized mass.
Horizontal projective regimes also have lower asymptotics stable under intermediate section spaces.
Remaining gap. Find ﬁberwise singularity or integrability hypotheses yielding one θ-psh ψ of
positive mass and the stated o(mq ) defect. A ﬁnite-codimension comparison is useful only after
constructing the base ideal series. The requested ψ must retain the positive-mass premise needed
for the base limit.
Sources.    Book, Proposition 26.8.1, Theorem 26.6.1; Chapter 26’s ﬁber and horizontal kernel
sections.



## Current standalone article

```tex
\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,amsthm,mathtools}
\usepackage[margin=1in]{geometry}
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{corollary}{Corollary}
\newtheorem{example}{Example}
\newcommand{\ddc}{dd^c}
\newcommand{\cI}{\mathcal I}
\newcommand{\cO}{\mathcal O}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\ord}{\operatorname{ord}}
\newcommand{\PP}{\mathbb P}
\title{Fiber integrability and base multiplier-ideal approximation}
\author{}
\date{3 October 2026}
\begin{document}
\maketitle
\begin{abstract}
For a compact holomorphic submersion with connected fibers, we give sufficient
conditions under which sections selected by an upstairs singularity are
approximated by the multiplier ideals of one base potential of positive mass.
A global logarithmic lower bound and one anisotropic upper-bound chart place
the descended section spaces between divisorial series whose vanishing orders
differ by a bounded amount. Their dimension defect is $O(m^{q-1})$ on a base
of dimension $q$. Exact local models give the selected series explicitly,
with fiber-integrability gain $p\sum_j b_j^{-1}$. Product examples show that
the selecting singularity can be supported on a proper subset of each fiber.
The result answers the request for sufficient conditions in catalogue P21;
it gives no necessity-and-sufficiency classification for arbitrary selectors.
\end{abstract}

\section{The approximation question}
Let $\pi:X\to B$ be a surjective holomorphic submersion of connected compact
complex manifolds with connected fibers. Suppose that $B$ is K\"ahler, and
put $q=\dim B\geq1$ and $f=\dim X-q\geq1$. Fix a Hermitian form $\omega$
on $X$, a holomorphic line bundle $A$ with smooth Hermitian metric $h$ on
$B$, and $\varphi\in\PSH(X,\omega)$. Write $\theta=c_1(A,h)$.
We use $\ddc=\frac{i}{2\pi}\partial\bar\partial$ and define $\cI(tu)$ by
local integrability of $|g|^2e^{-tu}$ for holomorphic germs $g$.

The spaces in P21 of the attached catalogue~\cite{catalogue} are
\[
 V_m=H^0(X,\pi^*A^m\otimes\cI(m\varphi))\subset H^0(B,A^m).
\]
The identification follows from compact connected fibers. The question asks
for conditions producing $\psi\in\PSH(B,\theta)$ of positive
non-pluripolar mass such that
\[
 W_m=H^0(B,A^m\otimes\cI(m\psi))\subset V_m,
 \qquad \dim V_m-\dim W_m=o(m^q).
\]
No section norm is part of this assertion.

The isotropic section-over-divisor result is already proved in
Theorem 26.10.1 of Xia's working monograph~\cite{book}. Its error order and
sharp product example are established background. Here only one chart is
needed to detect the leading base vanishing order. Separate powers in that
chart measure the bounded relaxation supplied by fiber integration. A global
lower bound ensures that stronger selecting conditions elsewhere do not
destroy the base inclusion.

\section{A bounded divisorial band}
Let $D\subset B$ be a nonempty smooth connected reduced effective divisor.
Choose a smooth metric $H_D$ on $\cO(D)$, let $s_D$ be its defining section,
and write $\eta=c_1(\cO(D),H_D)$.

\begin{theorem}\label{thm:criterion}
Assume that there are $c>0$ and $u\in C^\infty(B,\mathbb R)$ such that
\begin{equation}\label{eq:positive}
 \beta=\theta+\ddc u-c\eta>0.
\end{equation}
Suppose that for some constant $C$ one has
\begin{equation}\label{eq:global}
 \varphi\geq c\log\|\pi^*s_D\|^2-C
 \quad\hbox{on }X,
\end{equation}
where the divisor norm uses the pulled-back metric $H_D$ and the inequality
is interpreted for extended-real values.

Suppose further that one coordinate polydisc on $X$ has submersion
coordinates
\[
 \pi(z,t,w,v)=(z,t),\quad D=\{z=0\},\quad
 t\in\mathbb C^{q-1},\ w\in\mathbb C^r,\ v\in\mathbb C^{f-r},
\]
with $1\leq r\leq f$, and throughout this polydisc
\begin{equation}\label{eq:witness}
 \varphi\leq\frac cp\log\left(|z|^{2p}+
                  \sum_{j=1}^r|w_j|^{2b_j}\right)+C'
\end{equation}
for positive integers $p,b_1,\ldots,b_r$. The chart lies over a nonempty
open subset of $D$.

Set
\[
 a=p\sum_{j=1}^r b_j^{-1},\qquad
 L_m=\lfloor mc\rfloor,\qquad
 K_m=\max\{\lfloor mc-a\rfloor,0\}.
\]
Then
\begin{equation}\label{eq:reference}
 \psi=u+c\log\|s_D\|^2\in\PSH(B,\theta),\qquad
 \int_B\langle(\theta+\ddc\psi)^q\rangle=\int_B\beta^q\in(0,\infty).
\end{equation}
For every positive integer $m$,
\begin{equation}\label{eq:band}
 W_m=H^0(B,A^m(-L_mD))\subset V_m
                  \subset H^0(B,A^m(-K_mD)),
\end{equation}
and
\begin{equation}\label{eq:defect}
 0\leq\dim V_m-\dim W_m=O(m^{q-1})=o(m^q).
\end{equation}
When $q=1$, the defect is at most $\lceil a\rceil$.
\end{theorem}

The positivity condition constructs the base reference. The two singularity
bounds then compare its ideal series with the selected series. The upper
bound needs neither a global section over $D$ nor a global normal-coordinate
splitting.

\subsection{Two elementary estimates}
\begin{lemma}\label{lem:integral}
Let $p,b_1,\ldots,b_r$ be positive integers, $P>0$, and $\ell\geq0$ an
integer. Near the origin in $\mathbb C^{r+1}$,
\[
 |z|^{2\ell}\left(|z|^{2p}+\sum_{j=1}^r|w_j|^{2b_j}\right)^{-P}
 \in L^1_{\rm loc}
 \quad\Longleftrightarrow\quad
 \frac{\ell+1}{p}+\sum_{j=1}^r\frac1{b_j}>P.
\]
Equality of the two sides in the last inequality gives logarithmic divergence.
\end{lemma}
\begin{proof}
Integrate the angular variables and put
$x_0=|z|^{2p}$ and $x_j=|w_j|^{2b_j}$. Up to positive constants the integral
becomes
\[
 \int (x_0+\cdots+x_r)^{-P}
 x_0^{(\ell+1)/p-1}\prod_{j=1}^r x_j^{1/b_j-1}\,dx_0\cdots dx_r.
\]
A small simplex $\sum x_j<\delta$ is contained in the integration box, and
the box is contained in a larger simplex. On either simplex use
$\rho=\sum x_j$ and $x_j=\rho y_j$. The angular simplex integral is finite
and positive since all its exponents are greater than $-1$. The radial
integral is
\[
 \int_0^\delta\rho^{(\ell+1)/p+\sum b_j^{-1}-P-1}\,d\rho.
\]
This proves the assertion and the equality endpoint. Additional tangential
variables on bounded polydiscs, bounded remainders in the weight, and a
holomorphic unit multiplying $z^\ell$ do not change local integrability.
\end{proof}

\begin{lemma}\label{lem:dimension}
Let $Y$ be a compact complex manifold of dimension $s$ and let $E,F$ be
fixed holomorphic line bundles. Uniformly for integers $j,k$,
\[
 h^0(Y,E^j\otimes F^k)=O((1+|j|+|k|)^s).
\]
Consequently, if $0\leq K_m\leq L_m=O(m)$ and $L_m-K_m$ is bounded, then
\[
 h^0(B,A^m(-K_mD))-h^0(B,A^m(-L_mD))=O(m^{q-1}).
\]
\end{lemma}
\begin{proof}
Choose smooth bundle metrics, a smooth positive volume, and finitely many
coordinate charts and frames with smaller charts covering $Y$. Put
$N=1+|j|+|k|$. All second derivatives of the metric weight of
$E^j\otimes F^k$ are $O(N)$. At a point in a smaller chart, a holomorphic
affine exponential change of frame removes the constant and real-linear
terms of that weight. The new weight is uniformly bounded on a ball of
radius $\epsilon N^{-1/2}$ about the point. Submean therefore gives
\[
 |\sigma(y)|^2\leq C N^s\|\sigma\|_{L^2}^2.
\]
For an orthonormal basis, the sum of the squared evaluations is the squared
operator norm of evaluation into a one-dimensional fiber. It is thus at
most $CN^s$. Integrating the sum bounds the dimension. In dimension zero
the assertion follows from the finite number of points.

For the second assertion use the restriction sequences
\[
 0\longrightarrow A^m(-(j+1)D)\longrightarrow A^m(-jD)
 \longrightarrow A^m(-jD)|_D\longrightarrow0
\]
for $K_m\leq j<L_m$. Each successive dimension difference is at most
$h^0(D,A^m(-jD)|_D)$. Apply the first assertion on the compact complex
$(q-1)$-fold $D$ with $j=O(m)$, and sum over the bounded number of steps.
No surjectivity of restriction or cohomology vanishing is required. If
$q=1$, the connected smooth divisor is one point and each restriction space
has dimension one.
\end{proof}

\subsection{Proof of the criterion}
\begin{proof}[Proof of Theorem \ref{thm:criterion}]
In a local frame of $A$, a section of $\pi^*A^m$ is a holomorphic function
on each compact connected fiber, and is consequently constant there. Local
holomorphic right inverses of the submersion show that its descended
coefficient is holomorphic. These coefficients glue, giving
\[
 H^0(X,\pi^*A^m)=H^0(B,A^m).
\]

Poincar\'e--Lelong gives
$\theta+\ddc\psi=\beta+c[D]\geq0$. Off $D$ the current is $\beta$.
The non-pluripolar construction discards the locus $\psi=-\infty$, which
is $D$, so its top product is the extension of $\beta^q$ from $B\setminus D$.
Since a smooth volume gives $D$ zero measure, that extension is $\beta^q$.
Strict positivity and compactness prove \eqref{eq:reference}, including
when $q=1$.

Locally $\psi=c\log|z|^2+O(1)$. For a germ of divisor order $\ell$,
one-variable integrability requires $\ell+1>mc$. Thus
\[
 \cI(m\psi)=\cO(-\lfloor mc\rfloor D).
\]
In particular, if $mc$ is an integer, order $mc-1$ fails and order $mc$
succeeds. The bounded function $u$ and \eqref{eq:global} give
$\varphi\geq\pi^*\psi-C''$. In submersion coordinates, integrability
on the base implies integrability of the pullback on a bounded fiber
polydisc. Therefore $W_m\subset V_m$ for every $m$.

Take a nonzero descended section $\sigma\in V_m$ and put
$\ell=\ord_D(\sigma)$. Since the smooth connected divisor is irreducible,
in the witness chart its coefficient is $z^\ell g(z,t)$ with $g(0,t)$
not identically zero. Otherwise the identity theorem on $D$ would increase
its divisor order. Choose a smaller chart where $g$ is a unit.
The upper bound \eqref{eq:witness} implies that integrability of
$|\pi^*\sigma|^2e^{-m\varphi}$ requires integrability of
\[
 |z|^{2\ell}\left(|z|^{2p}+\sum|w_j|^{2b_j}\right)^{-mc/p}.
\]
Lemma \ref{lem:integral} gives $\ell+1>mc-a$. For integer $\ell\geq0$
this is exactly $\ell\geq\max\{\lfloor mc-a\rfloor,0\}=K_m$.
When $q=1$ the coefficient $g$ has no $t$ variables and its leading value
is nonzero. This proves the upper inclusion of \eqref{eq:band}.

Finally
\[
 0\leq L_m-K_m\leq\lceil a\rceil,
\]
by the elementary floor inequality and truncation at zero. Both orders
are $O(m)$. Lemma \ref{lem:dimension} and \eqref{eq:band} give
\eqref{eq:defect}. Its dimension-zero restriction argument also proves the
stated bound when $q=1$.
\end{proof}

\section{Exact models and non-descended examples}
\begin{corollary}\label{cor:exact}
Retain \eqref{eq:positive}. Suppose $Z\subset\pi^{-1}D$ is a nonempty
compact smooth submanifold projecting submersively onto $D$, and that near
each point of $Z$ there are the submersion coordinates above with
\[
 Z=\{z=w_1=\cdots=w_r=0\},\qquad
 \varphi=\frac cp\log\left(|z|^{2p}+\sum_{j=1}^r|w_j|^{2b_j}\right)+O(1),
\]
with fixed $p,b_j,c$. Suppose $\varphi$ is locally bounded outside $Z$.
Then the conclusions of Theorem \ref{thm:criterion} hold and, for every $m$,
\[
 V_m=H^0(B,A^m(-K_mD)).
\]
\end{corollary}
\begin{proof}
The local model dominates $c\log|z|^2$ up to a constant. Away from $Z$,
local boundedness gives the same lower bound near $\pi^{-1}D$, and outside
$\pi^{-1}D$ both functions are locally bounded. A finite covering of
compact $X$ proves \eqref{eq:global}. The upper witness is immediate.

For the remaining inclusion, a section divisible by $z^{K_m}$ has a bounded
holomorphic residual coefficient in every pole chart. The strict inequality
$K_m+1>mc-a$ and Lemma \ref{lem:integral} imply local integrability there.
Outside $Z$ the weight is locally bounded. Thus every section of
$H^0(B,A^m(-K_mD))$ belongs to $V_m$.
\end{proof}

For a nonempty family, take $X=B\times(\PP^1)^f$ with a projective base,
an ample $A$, and the divisor $D$ above. In the first $r$ fiber factors mark
points $o_j$ and let $E_j$ be their inverse-image divisors. Choose smooth
metrics on the corresponding divisor bundles and set
\[
 Q=\|\pi^*s_D\|^{2p}+\sum_{j=1}^r\|s_{E_j}\|^{2b_j},\qquad
 \varphi=\lambda\log Q,\qquad c=p\lambda.
\]
The common zero set is
$D\times\{o_1\}\times\cdots\times\{o_r\}\times(\PP^1)^{f-r}$.
Near it, smooth positive metric factors give the exact model of
Corollary \ref{cor:exact}; elsewhere the function is smooth.
The inequality $Q\geq\|\pi^*s_D\|^{2p}$ gives \eqref{eq:global}.

There is a constant $C_0$ with $\ddc\log Q\geq-C_0\omega$. Indeed, $Q$
is the squared norm of a holomorphic section of the direct sum of the
divisor line bundles with powers $p,b_j$. Locally the log-sum-exp Hessian
is a weighted average of their smooth negative curvatures plus a positive
variance term. A local quadratic correction gives a psh function away from
the component zeros, and the locally bounded-above psh extension preserves
the inequality across the common zero set. Compactness makes $C_0$ uniform.
Thus $\lambda C_0\leq1$ ensures $\varphi\in\PSH(X,\omega)$ for the
fixed Hermitian background. A positive metric on $A$ differs smoothly from
the prescribed $h$. Choose $u$ giving its curvature; for sufficiently small
$c=p\lambda$, \eqref{eq:positive} holds as well. Both smallness conditions
can be imposed simultaneously.

These potentials are singular on a proper subset of each fiber over $D$ and
finite elsewhere on that fiber. Hence they cannot be pullbacks of a base
potential up to bounded difference.

\begin{example}\label{ex:explicit}
Let $B=\PP^q$, let $D$ be a hyperplane, take $A=\cO(1)$, and put
$X=B\times\PP^1$. Use Fubini--Study divisor metrics and choose a point
$o\in\PP^1$. Set
\[
 \varphi=\tfrac14\log\bigl(\|s_D\|^4+\|s_o\|^6\bigr),\qquad
 p=2,\quad b_1=3,\quad c=\tfrac12.
\]
For $\omega=\omega_B+\omega_F$, the curvature estimate just used gives
$\ddc\varphi\geq-\frac12\omega_B-\frac34\omega_F$, so the selector
is admissible. The residual is $\beta=\frac12\omega_B$, with mass $2^{-q}$
when $\int_B\omega_B^q=1$.

Here $a=2/3$, $L_m=\lfloor m/2\rfloor$, and
$K_m=\max\{\lfloor m/2-2/3\rfloor,0\}$. For $m=1$ both selected
spaces are $H^0(\cO(1))$. For every $m\geq2$, $K_m=L_m-1$, and
\[
 V_m=H^0(\PP^q,\cO(m-L_m+1)),\qquad
 W_m=H^0(\PP^q,\cO(m-L_m)).
\]
Consequently
\[
 \dim V_m-\dim W_m
 =\binom{\lceil m/2\rceil+q}{q-1}
 \sim\frac{2^{1-q}}{(q-1)!}m^{q-1}.
\]
For $q=1$ the defect is exactly one for $m\geq2$. Thus the error order
is sharp in this anisotropic class.
\end{example}

The common horizontal coefficient $c$, a witness over an open part of $D$,
and the finite weighted transverse gain $p\sum b_j^{-1}$ suffice for the
approximation. The global lower bound excludes additional constraints that
would obstruct the inclusion. With $p=b_j=1$ and $r=f$, the exact order is
$\max\{\lfloor mc\rfloor-f,0\}$, recovering the established isotropic
section-over-divisor case. Separate powers, positive-dimensional pole sets
inside the fibers, and the one-chart sandwich criterion extend that regime.

If the fibers have dimension zero, the connected-fiber submersion is a
biholomorphism. When the descended selector itself is $\theta$-psh of finite
positive mass, taking it as $\psi$ gives $V_m=W_m$. The examples above concern
the additional integrability supplied by positive-dimensional fibers.

The positivity assumption cannot simply be omitted. If $A$ is trivial with
flat metric, global plurisubharmonic functions on compact connected $B$
are constant and have zero non-pluripolar top mass. The theorem provides
explicit sufficient conditions for P21 and leaves arbitrary singularities,
more general base images, and necessity questions open.

\begin{thebibliography}{9}
\bibitem{catalogue}
\emph{Open problems in non-K\"ahler pluripotential theory: full statements,
known results, and remaining gaps}, catalogue accompanying Mingchen Xia's
monograph, 2 October 2026, supplied as \texttt{document.pdf}, P21.
\bibitem{book}
M. Xia, \emph{Singularities in Hermitian pluripotential theory}, public
working manuscript, \url{https://mingchenxia.github.io/Papers/SHPT_vibe.pdf},
Lemma 26.10.1, Theorem 26.10.1, and Example 26.10.1.
\end{thebibliography}
\end{document}
```

## Complete ordinary generated note w7-1/n1

{
  "id": "w7-1/n1",
  "summary": "Two proved tools: anisotropic logarithmic integrability has the strict threshold (k+1)/p+Σ1/b_j>mλ, hence minimal base vanishing max(0,floor(pmλ-pΣ1/b_j)); bounded-width divisorial bands have O(m^{q-1}) section defect on any compact complex base, including O(1) when q=1. The dimension bound does not require projectivity.",
  "detailedSummary": "For p,b_j positive integers, the integral of |z|^{2k}(|z|^{2p}+Σ|w_j|^{2b_j})^{-mλ} is finite exactly when (k+1)/p+Σ1/b_j>mλ. Equality diverges logarithmically, so the minimal nonnegative k is max(0,floor(pmλ-pΣ1/b_j)). The proof uses x_0=|z|^{2p}, x_j=|w_j|^{2b_j} and simplex radial integration. Separately, on a compact complex manifold Y of dimension t, fixed line bundles F,G satisfy h^0(Y,F^a⊗G^b)≤C(1+|a|+|b|)^t. A local submean estimate on radius N^{-1/2}, after a holomorphic gauge cancels the linear part of the metric weight, bounds the evaluation operator and hence the Bergman function by CN^t. Consequently, for a smooth divisor D on a compact q-fold and vanishing orders K_m≤L_m=O(m) with bounded difference, h^0(A^m(-K_mD))-h^0(A^m(-L_mD))=O(m^{q-1}); for a connected divisor on a curve the defect is at most L_m-K_m.",
  "text": "## 1. Anisotropic integrability lemma\nLet p,b_1,...,b_r be positive integers, λ>0, m≥1, and k≥0 an integer. Put S=Σ_{j=1}^r 1/b_j. Near the origin in C^{r+1},\n\nI=∫ |z|^{2k} (|z|^{2p}+Σ_j |w_j|^{2b_j})^{-mλ} dV(z,w)\n\nis finite if and only if\n\n(k+1)/p+S>mλ.                                             (1)\n\nThe same assertion holds after adding auxiliary complex variables ranging in a polydisc. Replacing the logarithmic weight by that weight plus a bounded function does not change integrability for any fixed m. Multiplying z^k by a holomorphic unit also does not change the criterion.\n\nProof. Integrate out the arguments of z,w_j and set x_0=|z|^{2p}, x_j=|w_j|^{2b_j}. Up to positive constants the integral becomes\n\n∫ (x_0+...+x_r)^{-mλ} x_0^{(k+1)/p-1} Π_{j=1}^r x_j^{1/b_j-1} dx_0...dx_r.\n\nAll exponents a_0=(k+1)/p and a_j=1/b_j are positive. A sufficiently small simplex {Σx_i<δ} lies inside the integration box, and the box lies in a larger simplex. With t=Σx_i and x_i=t u_i, the simplex integral is a finite positive beta-integral in u times\n\n∫_0^δ t^{Σa_i-1-mλ}dt.\n\nThe beta-integral is finite because every a_i>0. Thus finiteness is exactly (1). Equality in (1) replaced by equality of the two sides gives logarithmic divergence.\n\nEquivalently, with c=pλ and a=pS, the condition on k is k+1>mc-a. Therefore the smallest nonnegative permissible integer is\n\nK_m=max{0,floor(mc-a)}.                                   (2)\n\nThis formula includes integer endpoints: if mc-a is an integer N≥0, k=N-1 fails and k=N succeeds.\n\n## 2. Uniform dimension bound without projectivity\nLet Y be a compact complex manifold of dimension t, and let F,G be fixed holomorphic line bundles. There is a constant C such that, for all integers a,b,\n\nh^0(Y,F^a⊗G^b)≤C(1+|a|+|b|)^t.                           (3)\n\nProof for t≥1. Choose smooth Hermitian metrics on F,G and a smooth positive volume form on Y. Use finitely many coordinate charts, with relatively compact smaller charts covering Y, and holomorphic frames for F,G. Write N=1+|a|+|b|. In such frames the logarithm of the metric on F^a⊗G^b has all real second derivatives bounded in absolute value by C_0N, uniformly on the charts.\n\nAt any point y in a smaller chart, multiply the frame by a nonvanishing holomorphic exponential of an affine-linear function. Normalize its length at y to one and cancel the real linear term of its log metric there. Every real linear function of complex coordinates is the real part of a holomorphic affine-linear function, so this is possible. Taylor's theorem then shows that the metric in this frame is bounded above and below by uniform positive constants on the Euclidean ball centered at y of radius R=cN^{-1/2}, with c fixed sufficiently small.\n\nFor a holomorphic section s=f e in this frame, the Euclidean submean inequality and equivalence of the volume forms give\n\n|s(y)|^2≤C_1N^t ∫_Y |s|^2 dV.                            (4)\n\nEquip the finite-dimensional space H^0(Y,F^a⊗G^b) with this L^2 inner product. Evaluation at y is a linear map to a one-dimensional Hermitian space. Its squared operator norm equals Σ_i |s_i(y)|^2 for any orthonormal basis {s_i}; (4) consequently bounds this sum by C_1N^t, not by C_1N^t times the dimension. Integrating over Y gives\n\nh^0(Y,F^a⊗G^b)=∫_Y Σ_i |s_i(y)|^2dV≤C_1 Vol(Y)N^t.\n\nFor t=0 the manifold is a finite set of points and the assertion is immediate. This proves (3). The auxiliary L^2 norm is used only to estimate a dimension; no section space is defined by a norm.\n\n## 3. Bounded divisorial bands\nLet B be a compact complex manifold of dimension q≥1, D a smooth connected effective divisor, and A a fixed line bundle. Suppose integers 0≤K_m≤L_m satisfy L_m=O(m) and L_m-K_m≤M for a fixed M. Then\n\n0≤h^0(B,A^m(-K_mD))-h^0(B,A^m(-L_mD))=O(m^{q-1}).         (5)\n\nIndeed, for each integer j between K_m and L_m-1 the exact sequence\n\n0→A^m(-(j+1)D)→A^m(-jD)→A^m(-jD)|_D→0\n\ngives a bound on the successive dimension difference by h^0(D,A^m(-jD)|_D). Apply (3) on D, of dimension q-1, to F=A|_D and G=O(-D)|_D. Since j=O(m), this bound is O(m^{q-1}), uniformly in the band, and there are at most M steps. When q=1, a smooth connected divisor is a single point, each restriction space has dimension one, and the defect is at most L_m-K_m.",
  "support": [],
  "revision": 0,
  "imported": false,
  "verified": true,
  "dead": false,
  "accepted": false,
  "candidate": false
}

## Complete checks and independent proof for w7-1/n1

{
  "noteId": "w7-1/n1",
  "imported": false,
  "checks": [
    {
      "noteId": "w7-1/n1",
      "correctness": {
        "verdict": "PASS",
        "report": "All three arguments are established. The simplex substitution gives precisely the strict integrability threshold, including logarithmic divergence at equality and the stated floor formula. The holomorphic frame normalization removes the linear metric term without changing its Hessian; the resulting evaluation-operator estimate proves the uniform dimension bound. Applying it to the divisor restriction sequences gives the bounded-band estimate, including the zero-dimensional restriction spaces when q=1. Both summaries accurately preserve the hypotheses, endpoint conventions, and quantitative conclusions.",
        "premises": []
      },
      "source": {
        "verdict": "PASS",
        "report": "The correctness check identified no nonroutine external premise."
      },
      "reconstruction": {
        "verdict": "PASS",
        "report": "The original arguments and independent reconstruction establish all three claims. Polar coordinates and simplex integration give the stated strict anisotropic threshold, with logarithmic divergence at equality and the correct truncated-floor formula. Bounded perturbations, units, and auxiliary variables preserve integrability as stated.\n\nThe original metric-gauge/submean argument correctly bounds the evaluation operator, hence the Bergman function and section dimension; it does not introduce an erroneous dimension factor. The independent jet argument also establishes the uniform bound without projectivity or Kähler assumptions. Divisor restriction sequences then give the bounded-band estimate, including the sharper pointwise bound when q=1.\n\nThe extracted statement and both summaries faithfully reflect the hypotheses and quantitative conclusions. No correction is needed.",
        "statement": "1. Anisotropic integrability. Let p,b_1,...,b_r be positive integers, let λ>0, and let m≥1 and k≥0 be integers. Set S=Σ_{j=1}^r 1/b_j. The local integral near the origin of C^{r+1}\n\n∫ |z|^{2k} (|z|^{2p}+Σ_{j=1}^r |w_j|^{2b_j})^{-mλ} dV(z,w)\n\nis finite if and only if\n\n(k+1)/p+S>mλ.\n\nAt equality the integral diverges logarithmically. The same criterion holds after adjoining any finite number of auxiliary complex variables ranging in a polydisc. For each fixed m, adding a bounded function to the logarithmic weight λ log(|z|^{2p}+Σ_j|w_j|^{2b_j}), or multiplying z^k by a holomorphic unit, does not change integrability. With c=pλ and a=pS, the criterion is k+1>mc-a, and the smallest permissible nonnegative integer is\n\nK_m=max{0,floor(mc-a)}.\n\nIn particular, if mc-a=N is a nonnegative integer, k=N-1 fails the strict inequality and k=N satisfies it; the formula also covers negative values of mc-a.\n\n2. Uniform section-dimension bound. Let Y be a compact complex manifold of complex dimension t≥0, and let F,G be fixed holomorphic line bundles on Y. There is a constant C, independent of a,b, such that for all integers a,b,\n\nh^0(Y,F^a⊗G^b)≤C(1+|a|+|b|)^t.\n\nFor t=0 this is a uniform constant bound. No projectivity or Kähler hypothesis is required.\n\n3. Bounded divisorial bands. Let B be a compact complex manifold of dimension q≥1, let D⊂B be a smooth connected effective divisor, and let A be a fixed holomorphic line bundle. Let K_m,L_m be integer sequences indexed by positive integers m such that 0≤K_m≤L_m, L_m=O(m), and L_m-K_m≤M for a fixed finite constant M. Then\n\n0≤h^0(B,A^m(-K_mD))-h^0(B,A^m(-L_mD))=O(m^{q-1}).\n\nWhen q=1, D is a single point and the sharper bound is\n\n0≤h^0(B,A^m(-K_mD))-h^0(B,A^m(-L_mD))≤L_m-K_m≤M.\n\nThese are bounds for the ordinary, norm-independent spaces of holomorphic sections.",
        "proof": "1. Anisotropic integral and integer thresholds.\nPut α₀=(k+1)/p and αⱼ=1/bⱼ for 1≤j≤r. Polar coordinates, followed by x₀=|z|^{2p} and xⱼ=|wⱼ|^{2bⱼ}, transform the integral over a sufficiently small polydisc, up to a positive constant, into\n∫ (x₀+⋯+xᵣ)^{-mλ} ∏_{j=0}^r xⱼ^{αⱼ-1} dx₀⋯dxᵣ\non a rectangle in the positive orthant. All αⱼ are positive. The part where x₀+⋯+xᵣ is bounded below is finite, since each factor xⱼ^{αⱼ-1} is integrable at zero.\n\nFor a sufficiently small ε>0, the rectangle contains {xⱼ≥0, ρ:=Σxⱼ<ε}. On this region use xⱼ=ρξⱼ, where ξⱼ≥0 and Σξⱼ=1. The integral is a positive constant times\n∫₀^ε ρ^{α₀+⋯+αᵣ-mλ-1} dρ.\nThe constant is the simplex integral of ∏ξⱼ^{αⱼ-1}; it is positive and finite. This follows, for example, by successive one-variable beta integrals, whose endpoint exponents are all greater than −1. Consequently the original integral is finite exactly when\n(k+1)/p+Σⱼ1/bⱼ>mλ.\nAt equality the radial integral is ∫₀^ε dρ/ρ, giving logarithmic divergence. Below equality it also diverges.\n\nAuxiliary variables on a polydisc contribute only its finite positive volume. Smooth positive volume densities are locally comparable to Euclidean volume. A bounded perturbation of the weight multiplies the integrand, for each fixed m, by a factor bounded above and below by positive constants. A holomorphic unit has the same effect through its squared modulus. Thus none changes the criterion.\n\nWriting c=pλ and a=pΣⱼ1/bⱼ, the criterion becomes k+1>mc−a. For any real x, the smallest nonnegative integer satisfying k+1>x is max{0,⌊x⌋}. Therefore K_m=max{0,⌊mc−a⌋}. If mc−a=N≥1 is an integer, k=N−1 gives equality and fails, while k=N succeeds. If N=0, the formal failing order −1 is not admissible, and the minimum admissible order is 0. Negative values of mc−a likewise give K_m=0.\n\n2. Uniform section bound on an arbitrary compact complex manifold.\nWe give an elementary analytic jet argument; in particular, no positivity, projectivity, or Kähler metric is needed. First suppose Y is connected and t≥1. Fix smooth Hermitian metrics on F and G, and set N=1+|a|+|b|. Choose a finite collection of relatively compact coordinate balls, with slightly larger coordinate neighborhoods on which both bundles have holomorphic frames. These smaller balls cover Y. On every such neighborhood the norm of the frame of F^a⊗G^b, and its reciprocal, are bounded by exp(CN), with a fixed C. The same bounds hold for transition functions between the finitely many frames. This includes negative a and b, since the original frame norms and transition functions are bounded away from zero on the relevant compact sets.\n\nHere is the propagation estimate used below. Fix a small coordinate ball P and a frame on a larger ball containing it. For a section s, let M=max_Y|s| in the induced smooth metric and μ=max_P|s|. There is a constant C_P, independent of a,b,s, such that\nμ≥exp(−C_P N)M.                                    (∗)\nIt suffices to establish this for nonzero s. To see it, recall the three-radius estimate for a holomorphic function on a coordinate ball:\nM_f(2ρ)≤M_f(ρ)^{1/2}M_f(4ρ)^{1/2}.\nIt follows by applying the maximum principle to log|f| on annuli in each complex line through the center; more generally, any three fixed radii give an exponent strictly between zero and one. If two centers are at distance at most ρ, the radius-ρ ball about the second is contained in the radius-2ρ ball about the first. The displayed inequality therefore propagates a small supremum to the next ball, using the larger supremum as a bound.\n\nBy connectedness, choose paths from P to the balls of the finite cover. Subdivide each path into finitely many such coordinate-ball steps, keeping the enlarged balls inside trivializing coordinate neighborhoods. At a change of chart, first choose a ball compactly contained in the overlap, restrict the current bound to it, change frame, and then continue the same three-radius argument. All these choices are fixed, independent of a,b,s. Each step uses an outer coefficient bound exp(CN)M; changing frames costs another exp(CN). Iterating gives, for each target ball, a bound\nmax_target|s|≤exp(C_i N)M^{1−δ_i}μ^{δ_i},\nwhere δ_i>0 and C_i are fixed. With δ=min δ_i>0 and C=max C_i, and using μ≤M, the finite cover gives\nM≤exp(CN)M^{1−δ}μ^δ.\nThis proves (∗). If μ=0, the same propagation proves s=0, so no exception is needed.\n\nNow take P=B(x,ρ), with B(x,2ρ) contained in its trivializing neighborhood. If s vanishes to order k at x, its coefficient f in that frame vanishes to order at least k along every complex line through x. The one-variable Schwarz estimate on those lines yields\nsup_{B(x,ρ)}|f|≤2^{-k}sup_{B(x,2ρ)}|f|.\nMetric-frame comparisons imply μ≤exp(CN)2^{-k}M. Combining with (∗) gives k≤C′N for a fixed C′. Thus the map taking a section to its Taylor jet at x of orders less than J_N:=⌊C′N⌋+1 is injective. The target has dimension\nbinom(t+J_N−1,t)=O(N^t).\nHence h⁰(Y,F^a⊗G^b)≤C(1+|a|+|b|)^t.\n\nA compact manifold has finitely many connected components, so the same conclusion follows by summing the componentwise bounds. For t=0 it is a finite set of points, and each line-bundle fiber has dimension one. This proves the claimed uniform constant bound in that case as well.\n\n3. Bounded divisorial bands.\nFor each integer j≥0 the smooth effective divisor D gives the exact sequence\n0→A^m(−(j+1)D)→A^m(−jD)→(A^m(−jD))|_D→0.\nTaking global sections shows that the decrease in h⁰ at this step is nonnegative and at most\nh⁰(D,(A|_D)^m⊗(O_B(D)|_D)^{−j}).\nApply part 2 to the compact complex manifold D of dimension q−1 and the two fixed bundles A|_D and O_B(D)|_D. For K_m≤j<L_m, the hypothesis L_m=O(m) makes this upper bound O(m^{q−1}), uniformly over the band. There are at most M steps. Summing proves\n0≤h⁰(B,A^m(−K_mD))−h⁰(B,A^m(−L_mD))=O(m^{q−1}).\nIf q=1, smoothness and connectedness make D one reduced point. Each restriction term is a one-dimensional vector space, giving the sharper bound by L_m−K_m≤M. All arguments concern ordinary spaces of holomorphic sections and make no choice of an L² norm."
      }
    }
  ]
}

## Complete ordinary generated note w7-1/n2

{
  "id": "w7-1/n2",
  "summary": "Complete sufficient-condition answer. A positive smooth residual curvature θ+dd^c u-cη_D, global domination φ≥c log||π*s_D||²-C, and one anisotropic fiber-singularity chart with upper model (c/p)log(|z|^{2p}+Σ|w_j|^{2b_j}) yield ψ=u+c log||s_D||², mass ∫β^q>0, inclusion for every m, and O(m^{q-1}) defect. Exact models determine V_m exactly. Explicit small-coefficient product examples are genuinely non-descended; isotropic section-over-divisor is only the p=b_j=1,r=fiber-dimension specialization.",
  "detailedSummary": "In the original compact connected submersion setup, assume a smooth connected divisor D on the Kähler base, c>0, a metric of O(D) with curvature η, and a smooth u such that β=θ+dd^c u-cη is Kähler. Assume φ globally dominates c log||π*s_D||² up to a constant, and on one adapted chart over a nonempty open part of D has an upper bound by (c/p)log(|z|^{2p}+Σ_{j=1}^r|w_j|^{2b_j})+C, with r≥1 fiber directions and positive integers p,b_j. Then ψ=u+c log||s_D||² belongs to PSH(B,θ), its non-pluripolar product is β^q, and its mass is finite and positive. Set L_m=floor(mc), a=pΣ1/b_j, K_m=max(0,floor(mc-a)). For every positive integer m, W_m=H^0(A^m(-L_mD))⊂V_m⊂H^0(A^m(-K_mD)). Since L_m-K_m≤ceil(a), the supported dimension lemma gives defect O(m^{q-1})=o(m^q). For q=1 the defect is at most ceil(a). An exact bounded-error anisotropic model at all points of a fiberwise smooth singular locus, bounded elsewhere, gives V_m=H^0(A^m(-K_mD)). A product X=B×(P^1)^d supplies genuine non-descended analytic selectors φ=λ log(||π*s_D||^{2p}+Σ||s_{E_j}||^{2b_j}), with λ small enough for ω-psh and positive residual base curvature, c=pλ. Their singular locus meets only a proper subset of each fiber over D, unlike a pullback singularity. The proof identifies the horizontal slope c, finite weighted transverse volume S=Σ1/b_j, global exclusion of stronger unrelated constraints, and a local witness detecting c as sufficient features, without a necessity-and-sufficiency claim. Integer thresholds and the curve case are explicitly checked; arbitrary data are not claimed to admit a reference, as A trivial already obstructs positive mass.",
  "text": "# A sufficient anisotropic criterion, with genuinely non-descended examples\n\nWrite d=dim X-dim B. The following gives sufficient conditions on the fixed data in the question. It does not assert that arbitrary selecting weights admit a base reference.\n\n## The criterion\nAssume the following additional conditions.\n\n**Base positivity.** There is a nonempty smooth connected effective divisor D⊂B, with defining section s_D of O(D) and a smooth Hermitian metric H_D. Write η=c_1(O(D),H_D). There are a real number c>0 and a smooth real function u on B such that\n\nβ=θ+dd^c u-cη\n\nis a Kähler form. This is a geometric positivity condition on the residual class c_1(A)-c{D}. On a Kähler base the condition that this class be Kähler also gives such a u by the dd^c lemma. In particular, if A is ample, it holds for every sufficiently small c>0: choose a positive metric on A, compare it with the fixed metric h to obtain u, and then subtract the sufficiently small smooth form cη.\n\n**No stronger unrelated selecting singularities.** For some constant C,\n\nφ≥c log||π^*s_D||^2-C                                   (6)\n\non X, with the inequality interpreted in the extended-real sense.\n\n**One anisotropic fiber witness.** There is an adapted coordinate polydisc in X, with coordinates\n\n(z,t_1,...,t_{q-1},w_1,...,w_r,v_1,...,v_{d-r}),\n\nwhere 1≤r≤d, π(z,t,w,v)=(z,t), and D is {z=0} in the base chart. For positive integers p,b_1,...,b_r and a constant C', throughout this polydisc,\n\nφ≤(c/p) log(|z|^{2p}+Σ_{j=1}^r|w_j|^{2b_j})+C'.          (7)\n\nThe upper-bound chart need only lie over a nonempty open part of D. Neither a global section nor a global normal-coordinate splitting is required for this criterion.\n\nDefine\n\nψ=u+c log||s_D||^2,\nS=Σ_j 1/b_j,  a=pS,\nL_m=floor(mc),  K_m=max{0,floor(mc-a)}.\n\nThen, for every positive integer m,\n\nW_m=H^0(B,A^m(-L_mD)) ⊂ V_m ⊂ H^0(B,A^m(-K_mD)).         (8)\n\nMoreover,\n\nψ∈PSH(B,θ),\n∫_B ⟨(θ+dd^cψ)^q⟩=∫_B β^q∈(0,∞),\n0≤dim V_m-dim W_m=O(m^{q-1})=o(m^q).                     (9)\n\nThus the requested inclusion actually holds for all m, not merely for sufficiently large m.\n\n## Proof\n### Holomorphic descent and the meaning of the spaces\nA holomorphic function on a compact connected fiber is constant. Locally trivialize A on B. A section of π^*A^m then has a holomorphic coefficient on the inverse image which is constant on every fiber. A holomorphic submersion has local holomorphic sections, so the descended coefficient is holomorphic on the base. Surjectivity gives uniqueness, and these coefficients glue. Hence\n\nH^0(X,π^*A^m)=H^0(B,A^m),\n\nand V_m is exactly the subspace of descended sections whose pullbacks are locally integrable against e^{-mφ}. Smooth local metrics and smooth positive volume forms do not change local integrability. No choice of an L^2 norm changes V_m or W_m.\n\n### Positivity and mass of the base potential\nWith the convention in the question, Poincaré–Lelong reads\n\ndd^c log||s_D||^2=[D]-η.\n\nTherefore\n\nθ+dd^cψ=β+c[D]≥0.\n\nThe displayed ψ is upper semicontinuous and quasi-psh, so ψ∈PSH(B,θ). Off D the current is the smooth form β. The non-pluripolar product discards the locus where ψ=-∞, namely D, and therefore is the extension by zero of β^q from B\\D. Since a smooth volume form gives D zero measure, this is just β^q on all of B. Consequently its mass is ∫_Bβ^q, which is finite by compactness and strictly positive because β is Kähler. This argument also applies when q=1: the non-pluripolar part is β, not β+c[D].\n\n### The base multiplier ideal and the first inclusion\nNear D, ψ=c log|z|^2 plus a smooth function. A holomorphic germ having order k in z is locally integrable against e^{-mψ} precisely when\n\nk+1>mc.\n\nThus\n\nI(mψ)=O_B(-floor(mc)D).                                  (10)\n\nAt an integer endpoint mc=N, order N-1 is not integrable, whereas order N is. In particular (10) has the floor, with no endpoint adjustment.\n\nBecause u is bounded on compact B, (6) gives φ≥π^*ψ-C'' for another constant. For each fixed m,\n\n|π^*f|^2e^{-mφ}≤e^{mC''}|π^*f|^2e^{-mπ^*ψ}\n\nalmost everywhere. In local submersion coordinates, local integrability of the right-hand side follows from local integrability on the base and integration over a bounded fiber polydisc. Therefore W_m⊂V_m for every m.\n\n### The witness gives the second inclusion\nTake a nonzero descended section s∈V_m and let k be its vanishing order along the connected smooth divisor D. In the witness chart its local coefficient can be written z^k g(z,t), where g(0,t) is not identically zero on D in that chart. Indeed, otherwise the identity theorem on the connected smooth divisor would contradict the definition of k. Choose a point in this chart where g(0,t)≠0 and shrink around it, so that g is a unit. When q=1 there are no t variables, and the leading coefficient is already nonzero.\n\nBy (7), integrability of this pulled-back section implies integrability of\n\n|z|^{2k}(|z|^{2p}+Σ_j|w_j|^{2b_j})^{-mc/p}.\n\nThe anisotropic lemma proved in n1 says this requires\n\n(k+1)/p+S>mc/p,\n\nor k+1>mc-pS. Its smallest permissible nonnegative integer is K_m. Thus every section in V_m vanishes at least to order K_m along D, proving the second inclusion in (8). Only a witness over an open part of D was needed to detect this divisorial order.\n\n### The dimension defect\nSince a=pS>0,\n\n0≤L_m-K_m≤ceil(a).                                      (11)\n\nIndeed, floor(x)-floor(x-a)≤ceil(a), and truncating the second floor at zero can only decrease this difference when x=mc≥0. Both orders are O(m). By (8),\n\n0≤dim V_m-dim W_m\n ≤h^0(B,A^m(-K_mD))-h^0(B,A^m(-L_mD)).\n\nThe bounded-divisorial-band estimate proved in n1 gives O(m^{q-1}). This estimate requires no projectivity assumption: its proof bounds sections on the smooth compact (q-1)-fold D by local submean estimates for metrics whose weights have second derivatives O(m).\n\nFor q=1, D is one point, every successive restriction space has dimension one, and the sharper bound is\n\n0≤dim V_m-dim W_m≤L_m-K_m≤ceil(a).\n\nThis is O(1)=o(m). All formulas remain valid when mc or mc-a is an integer. In the anisotropic condition equality k+1=mc-a diverges logarithmically, which is exactly accounted for by K_m=max(0,floor(mc-a)). This proves (9).\n\n## Exact local models give an exact description of V_m\nHere is a useful stronger geometric version. Suppose Z⊂π^{-1}(D) is a compact smooth submanifold projecting submersively onto D, and at each point of Z there are adapted coordinates as above in which\n\nZ={z=w_1=...=w_r=0},\nφ=(c/p)log(|z|^{2p}+Σ_j|w_j|^{2b_j})+O(1),               (12)\n\nwith the same p,b_j,c. Suppose φ is locally bounded outside Z. Then (6) follows by a finite covering of compact X, because the model in (12) dominates c log|z|^2 up to a constant; (7) is immediate. Furthermore,\n\nV_m=H^0(B,A^m(-K_mD))                                   (13)\n\nfor every m. To prove the reverse inclusion in (13), a section vanishing to order at least K_m has coefficient z^{K_m} times a bounded holomorphic function near every point of Z. The anisotropic lemma gives local integrability there. Outside Z, the weight is locally bounded. The other inclusion was already proved. Thus the transverse weighted dimension produces a bounded, explicitly computed relaxation of the base vanishing order.\n\n## A nonempty family of genuinely non-descended selectors\nTake a projective Kähler base B, an ample A with the given arbitrary smooth metric h, and a smooth connected effective divisor D. Let\n\nX=B×(P^1)^d,   d≥1,\n\nand let π be the first projection. Choose 1≤r≤d and in the first r fiber factors choose marked points o_j. Let E_j be the divisor where the j-th fiber coordinate equals o_j, with defining section s_{E_j} and a smooth metric. Give O(D) a smooth metric as well. For any positive integers p,b_1,...,b_r put\n\nQ=||π^*s_D||^{2p}+Σ_{j=1}^r||s_{E_j}||^{2b_j},\nφ=λ log Q,   c=pλ.                                     (14)\n\nThe common zero locus is\n\nZ=D×{o_1}×...×{o_r}×(P^1)^{d-r}.\n\nOutside Z, φ is smooth. Near Z, smooth positive metric factors show\n\nφ=λlog(|z|^{2p}+Σ_j|w_j|^{2b_j})+O(1).\n\nAlso Q≥||π^*s_D||^{2p}, so (6) holds with C=0.\n\nFor completeness, φ can be made ω-psh for the fixed arbitrary Hermitian form ω on X. View Q as the squared norm of a holomorphic section of the direct sum of the line bundles π^*O(pD), O(b_1E_1),...,O(b_rE_r), with the direct-sum metric. There is a constant C_0 such that\n\ndd^c log Q≥-C_0ω.\n\nOne way to check this is to use local metric weights ρ_j: away from component zeros the log-sum-exp Hessian of Σ|f_j|^2e^{-ρ_j} is a weighted average of -dd^cρ_j plus a nonnegative variance term. The finitely many smooth curvature forms have a uniform lower bound by -C_0ω. The same inequality extends across individual zeros by continuity and across common zeros by the locally bounded-above psh extension after adding a sufficiently positive local quadratic function. Thus choosing λC_0≤1 gives ω+dd^cφ≥0.\n\nChoose a positive metric on A and let u be the smooth comparison function with the fixed h. For λ>0 small enough, c=pλ is also small enough that β=θ+dd^c u-cη is Kähler. Both required smallness conditions can be imposed simultaneously. Equations (9) and (13) consequently apply to (14).\n\nThese selectors are genuinely non-descended even at the level of singularity type. Over a point of D, φ is -∞ on a proper subset of the fiber and finite on its complement. A pullback base weight, even after adding a bounded function, cannot have this behavior: an infinite base singularity is infinite on the entire fiber, while a finite base value plus a bounded function is finite everywhere on the fiber.\n\nFor a completely explicit nonempty family in every base dimension q≥1, take B=P^q, A=O(1), and D a hyperplane (a point when q=1). Use Fubini–Study for the positive comparison metric and for O(D). Then β=(1-c)ω_FS for 0<c<1, and the base mass is (1-c)^q under the normalization ∫ω_FS^q=1. The given metric h is accommodated by u, and the given ω on the product is accommodated by taking λ sufficiently small.\n\n## What features of the fiber singularities are sufficient?\nThe proof isolates the following sufficient features, rather than a classification.\n\n1. **A common horizontal logarithmic slope c.** Global domination (6) means vanishing with the base multiplier-ideal order always suffices upstairs; it excludes unrelated stronger constraints.\n2. **A singularity of that slope visible over an open part of D.** The upper witness (7) detects the leading divisorial order. A singularity at merely an isolated exceptional base point would not supply this divisorial detection argument.\n3. **Finite weighted transverse volume.** For the model, the transverse fiber quantity is S=Σ1/b_j. Integrating in these fiber directions changes the required order by the constant a=pS, not by another term linear in m. This bounded rebate is why the difference of section spaces lives in only finitely many divisorial layers and has O(m^{q-1}) dimension.\n4. **Control of any remaining singularities.** The global lower bound suffices for the sandwich theorem. For exact equality (13), boundedness away from Z and the bounded-error local model ensure that no additional constraints remain. Bounded perturbations of these weights do not affect the conclusions.\n\nThe isotropic section-over-divisor model is the specialization p=b_1=...=b_r=1 and r=d, with Z a section over D. Its order is max(0,floor(mc-d)). The anisotropic result here permits different powers p,b_j, and also r<d; its order is max(0,floor(mc-pΣ1/b_j)). It is therefore not merely a restatement of the isotropic model. No necessity-and-sufficiency assertion is made for arbitrary fiber singularities.\n\nIf d=0, the connected-fiber submersion is a biholomorphism and no genuinely non-descended weight can exist. Descended weights, or bounded perturbations of them, give the familiar exact equality of multiplier-ideal section spaces whenever their base potential satisfies the required positivity. The genuinely non-descended family above applies whenever fiber directions are present.\n\nFinally, additional positivity hypotheses are indispensable in some form. For example, if A is trivial with its flat metric, then θ=0. A nontrivial member of PSH(B,0) on compact connected B is constant by the maximum principle, and its current has zero top mass for q≥1. Thus arbitrary data in the question cannot always yield a positive-mass base reference, regardless of the upstairs selector. The result proved above is a complete sufficient-condition answer, not a claim of universal approximation.",
  "support": [
    "w7-1/n1"
  ],
  "revision": 0,
  "imported": false,
  "verified": true,
  "dead": false,
  "accepted": true,
  "candidate": true
}

## Complete checks and independent proof for w7-1/n2

{
  "noteId": "w7-1/n2",
  "imported": false,
  "checks": [
    {
      "noteId": "w7-1/n2",
      "correctness": {
        "verdict": "PASS",
        "report": "The sufficient-condition theorem is valid, using the declared support w7-1/n1 and the external facts listed below. Poincaré–Lelong gives the positive current β+c[D]; non-pluripolar locality and avoidance of pluripolar sets give exactly β^q as its top product. The global lower bound gives W_m⊂V_m for every m. Connectedness and smoothness of D ensure that the leading divisorial coefficient is nonzero somewhere in the witness chart, so the anisotropic threshold applies and gives the upper inclusion. The bounded-width estimate from n1 then proves O(m^{q-1}), with the stated constant bound for q=1. Both integer endpoint formulas are correct.\n\nThe exact-model variant excludes additional integrability constraints and establishes the claimed equality. The product construction has the specified local models, admits a uniform curvature lower bound, and allows λ to satisfy both positivity requirements simultaneously. Its singular locus meets only a proper subset of each relevant fiber, proving genuine non-descent even up to bounded perturbation. The dimension-zero fiber case and the trivial-bundle obstruction are correctly qualified. Both summaries are consistent with the full note: these are sufficient conditions, not universal existence or a necessary-and-sufficient classification, and the anisotropic extension is distinguished from the isotropic specialization.",
        "premises": [
          "Let L be a holomorphic line bundle on a complex manifold Y with a smooth Hermitian metric H, and let s be a holomorphic section not identically zero on any connected component. With dd^c=(i/(2π))∂bar∂, the current identity dd^c log||s||_H^2=[div(s)]-c_1(L,H) holds, with divisor multiplicities included.",
          "On a compact Kähler manifold Y, every smooth real d-exact (1,1)-form γ is dd^c u for some smooth real function u, where dd^c=(i/(2π))∂bar∂.",
          "An ample holomorphic line bundle L on a compact complex manifold Y, where ample means that some positive tensor power is very ample, admits a smooth Hermitian metric whose Chern curvature c_1(L,H) is a Kähler form.",
          "On a compact Kähler manifold Y of complex dimension q≥1, the non-pluripolar top product of a positive closed (1,1)-current T assigns zero mass to pluripolar sets and, on every open subset where T is smooth, agrees with the ordinary wedge product T^q.",
          "Let U be a connected domain in C^n and E a proper closed analytic subset of U. If v is plurisubharmonic on U\\E and is locally bounded above near E, its extension obtained by taking the upper limit from U\\E at points of E is plurisubharmonic on U."
        ]
      },
      "source": {
        "verdict": "PASS",
        "report": "All five supplied premise strings are established. [Andersson, §1](https://arxiv.org/pdf/math/0412446) gives Poincaré–Lelong with divisor multiplicities; his operator is twice the task’s operator, giving exactly the stated squared-norm formula. [Tosatti, Lemma 2.1](https://arxiv.org/pdf/1508.04823) covers real d-exact (1,1)-forms; rescaling its potential gives the requested normalization. [Demailly, §3.15](https://arxiv.org/pdf/alg-geom/9410022) uses the same definition of ampleness and supplies positive smooth curvature. [BEGZ, §1.1](https://arxiv.org/pdf/0812.3674) establishes non-charging and locality, supporting the mass calculation for β+c[D], including q=1. [Demailly, Theorem 5.24](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf) supplies the removable-singularity theorem: proper analytic subsets are locally pluripolar, and the unique extension has the stated upper-limit values. The note’s additional positivity and selector bounds remain explicit hypotheses.",
        "passages": [
          {
            "id": "086b9803-0d94-4236-a06f-3c8b897a87e3/0/0",
            "statement": "Let L be a holomorphic line bundle on a complex manifold Y with a smooth Hermitian metric H, and let s be a holomorphic section not identically zero on any connected component. With dd^c=(i/(2π))∂bar∂, the current identity dd^c log||s||_H^2=[div(s)]-c_1(L,H) holds, with divisor multiplicities included.",
            "url": "https://arxiv.org/pdf/math/0412446",
            "quote": "The Poincar´e-Lelong formula states that\nddclog(1/|f|) = c1(DL) − [Z],",
            "premise": 0
          },
          {
            "id": "086b9803-0d94-4236-a06f-3c8b897a87e3/0/1",
            "statement": "Let L be a holomorphic line bundle on a complex manifold Y with a smooth Hermitian metric H, and let s be a holomorphic section not identically zero on any connected component. With dd^c=(i/(2π))∂bar∂, the current identity dd^c log||s||_H^2=[div(s)]-c_1(L,H) holds, with divisor multiplicities included.",
            "url": "https://arxiv.org/pdf/math/0412446",
            "quote": "ddc =\ni\nπ\n∂\n¯∂ = 2ℵ∂¯∂.",
            "premise": 0
          },
          {
            "id": "086b9803-0d94-4236-a06f-3c8b897a87e3/0/2",
            "statement": "On a compact Kähler manifold Y, every smooth real d-exact (1,1)-form γ is dd^c u for some smooth real function u, where dd^c=(i/(2π))∂bar∂.",
            "url": "https://arxiv.org/pdf/1508.04823",
            "quote": "Then there exists ϕ ∈ C∞(X, R), unique up to addition\nof a constant, such that\nα =\n√\n−1∂∂ϕ.",
            "premise": 1
          },
          {
            "id": "086b9803-0d94-4236-a06f-3c8b897a87e3/0/3",
            "statement": "An ample holomorphic line bundle L on a compact complex manifold Y, where ample means that some positive tensor power is very ample, admits a smooth Hermitian metric whose Chern curvature c_1(L,H) is a Kähler form.",
            "url": "https://arxiv.org/pdf/alg-geom/9410022",
            "quote": "every ample line bundle F has\na smooth hermitian metric with positive definite curvature form",
            "premise": 2
          },
          {
            "id": "086b9803-0d94-4236-a06f-3c8b897a87e3/0/4",
            "statement": "On a compact Kähler manifold Y of complex dimension q≥1, the non-pluripolar top product of a positive closed (1,1)-current T assigns zero mass to pluripolar sets and, on every open subset where T is smooth, agrees with the ordinary wedge product T^q.",
            "url": "https://arxiv.org/pdf/0812.3674",
            "quote": "puts no mass on pluripolar subsets.",
            "premise": 3
          },
          {
            "id": "086b9803-0d94-4236-a06f-3c8b897a87e3/0/5",
            "statement": "On a compact Kähler manifold Y of complex dimension q≥1, the non-pluripolar top product of a positive closed (1,1)-current T assigns zero mass to pluripolar sets and, on every open subset where T is smooth, agrees with the ordinary wedge product T^q.",
            "url": "https://arxiv.org/pdf/0812.3674",
            "quote": "is local in the plurifine topology whenever well-defined.",
            "premise": 3
          },
          {
            "id": "086b9803-0d94-4236-a06f-3c8b897a87e3/0/6",
            "statement": "On a compact Kähler manifold Y of complex dimension q≥1, the non-pluripolar top product of a positive closed (1,1)-current T assigns zero mass to pluripolar sets and, on every open subset where T is smooth, agrees with the ordinary wedge product T^q.",
            "url": "https://arxiv.org/pdf/0812.3674",
            "quote": "hddcui = 1{u>−∞}ddcu.",
            "premise": 3
          },
          {
            "id": "086b9803-0d94-4236-a06f-3c8b897a87e3/0/7",
            "statement": "Let U be a connected domain in C^n and E a proper closed analytic subset of U. If v is plurisubharmonic on U\\E and is locally bounded above near E, its extension obtained by taking the upper limit from U\\E at points of E is plurisubharmonic on U.",
            "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf",
            "quote": "Then every function v ∈ Psh(XrA) that is locally bounded above near A extends uniquely\ninto a function ve ∈ Psh(X).",
            "premise": 4
          }
        ],
        "premises": [
          "Let L be a holomorphic line bundle on a complex manifold Y with a smooth Hermitian metric H, and let s be a holomorphic section not identically zero on any connected component. With dd^c=(i/(2π))∂bar∂, the current identity dd^c log||s||_H^2=[div(s)]-c_1(L,H) holds, with divisor multiplicities included.",
          "On a compact Kähler manifold Y, every smooth real d-exact (1,1)-form γ is dd^c u for some smooth real function u, where dd^c=(i/(2π))∂bar∂.",
          "An ample holomorphic line bundle L on a compact complex manifold Y, where ample means that some positive tensor power is very ample, admits a smooth Hermitian metric whose Chern curvature c_1(L,H) is a Kähler form.",
          "On a compact Kähler manifold Y of complex dimension q≥1, the non-pluripolar top product of a positive closed (1,1)-current T assigns zero mass to pluripolar sets and, on every open subset where T is smooth, agrees with the ordinary wedge product T^q.",
          "Let U be a connected domain in C^n and E a proper closed analytic subset of U. If v is plurisubharmonic on U\\E and is locally bounded above near E, its extension obtained by taking the upper limit from U\\E at points of E is plurisubharmonic on U."
        ],
        "kind": "codex-report",
        "operationId": "086b9803-0d94-4236-a06f-3c8b897a87e3",
        "reportedAt": "2026-10-03T20:34:02.477Z"
      },
      "requirements": {
        "verdict": "PASS",
        "report": "The argument establishes every completion criterion under its explicit sufficient conditions. Poincaré–Lelong gives θ+dd^cψ=β+c[D], whose non-pluripolar top product is β^q and hence has finite positive mass. Global domination proves W_m⊂V_m for every m. The anisotropic witness, together with smoothness and connectedness of D, detects every nonzero section’s divisorial order and yields V_m⊂H^0(A^m(-K_mD)). The established support lemma applies with K_m=max(0,floor(mc-pΣ1/b_j)) and L_m=floor(mc); their bounded difference gives O(m^{q-1})=o(m^q), including O(1) when q=1. Strict integrability thresholds and integer endpoints are correctly handled.\n\nThe exact-model conclusion includes the necessary boundedness away from the singular locus. The product examples satisfy these hypotheses: sufficiently small positive λ simultaneously ensures ω-plurisubharmonicity and Kähler residual base curvature. Their singularities occupy only a proper subset of fibers over D, proving genuine non-descent even modulo bounded perturbations.\n\nHolomorphic descent, norm independence, the zero-dimensional-fiber case, and the obstruction for a trivial base bundle are correctly treated. The summaries consistently describe the conditional result, quantitative guarantees, exact-model specialization, and limitations. The anisotropic extension is distinguished from the isotropic section-over-divisor model, without asserting a universal or necessary-and-sufficient classification."
      },
      "reconstruction": {
        "verdict": "PASS",
        "report": "All claims are established under their stated additional hypotheses, using w7-1/n1 and the recorded external premises. Compact connected fibers and local holomorphic sections justify descent. Poincaré–Lelong gives the positive current β+c[D]; the non-pluripolar product is exactly β^q, with finite positive mass.\n\nGlobal domination proves W_m⊂V_m for every m. The anisotropic witness detects divisorial vanishing on an open part of D, and connectedness propagates it globally. The resulting truncated-floor orders differ by at most ceil(pΣ1/b_j), giving O(m^{q−1}) defect, including O(1) for q=1 and the correct integer endpoints.\n\nThe exact-model claim properly uses bounded-error models throughout Z and local boundedness outside Z. The product examples satisfy these conditions; the curvature bound and simultaneous smallness choices accommodate the fixed ω and h. Their fiberwise −∞ loci prove genuine non-descent even modulo bounded functions.\n\nThe extracted statement and both summaries preserve conditionality and scope, distinguish the anisotropic extension from the isotropic specialization, and make no universal or necessary-and-sufficient claim. No correction is needed.",
        "statement": "Let π:X→B be a surjective holomorphic submersion of connected compact complex manifolds with connected fibers. Assume B is Kähler of dimension q≥1, and put d=dim X-q. Fix a Hermitian form ω on X, a holomorphic line bundle A on B with a smooth Hermitian metric h, θ=c_1(A,h), and φ∈PSH(X,ω). Use dd^c=(i/(2π))∂bar∂, PSH(Y,α)={upper-semicontinuous quasi-psh u: α+dd^c u≥0}, and the multiplier-ideal convention that g∈I(tu) precisely when |g|²exp(-tu) is locally integrable. Holomorphic descent gives a natural isomorphism H^0(X,π^*A^m)=H^0(B,A^m) for every positive integer m. Under this identification set\n\nV_m=H^0(X,π^*A^m⊗I(mφ))⊂H^0(B,A^m).\n\nThese spaces are defined by local integrability, independently of auxiliary smooth volume forms, smooth local norms, or any choice of an L² norm.\n\nSufficient anisotropic criterion. Assume the following additional hypotheses:\n\n(a) There is a nonempty smooth connected effective divisor D⊂B, with defining section s_D of O(D) and a smooth Hermitian metric H_D. Write η=c_1(O(D),H_D). There are c>0 and a smooth real function u on B such that\n\nβ=θ+dd^c u-cη\n\nis a Kähler form.\n\n(b) There is a finite constant C such that, on all of X,\n\nφ≥c log||π^*s_D||²-C,\n\nwhere the norm is the pullback of H_D and the inequality is interpreted in the extended-real sense.\n\n(c) There is an adapted coordinate polydisc in X with coordinates\n\n(z,t_1,...,t_{q-1},w_1,...,w_r,v_1,...,v_{d-r}),\n\nwhere 1≤r≤d, π(z,t,w,v)=(z,t), and D is given by z=0 in the base chart. There are positive integers p,b_1,...,b_r and a finite constant C′ such that throughout this polydisc,\n\nφ≤(c/p) log(|z|^{2p}+Σ_{j=1}^r|w_j|^{2b_j})+C′.\n\nThe chart need only be over a nonempty open part of D. Neither a global section of π nor a global normal-coordinate splitting is assumed. When q=1 the t variables are absent.\n\nDefine\n\nψ=u+c log||s_D||²,  S=Σ_{j=1}^r 1/b_j,  a=pS,\nL_m=floor(mc),  K_m=max{0,floor(mc-a)}.\n\nThen ψ∈PSH(B,θ),\n\nθ+dd^cψ=β+c[D],\n⟨(θ+dd^cψ)^q⟩=β^q,\n0<∫_B⟨(θ+dd^cψ)^q⟩=∫_Bβ^q<∞.\n\nFor every positive integer m,\n\nI(mψ)=O_B(-L_mD),\nW_m:=H^0(B,A^m⊗I(mψ))=H^0(B,A^m(-L_mD)),\nW_m⊂V_m⊂H^0(B,A^m(-K_mD)).\n\nMoreover,\n\n0≤L_m-K_m≤ceil(a),\n0≤dim V_m-dim W_m=O(m^{q-1})=o(m^q).\n\nThus the requested inclusion holds for every m, not just for sufficiently large m. When q=1,\n\n⟨θ+dd^cψ⟩=β,\n0≤dim V_m-dim W_m≤L_m-K_m≤ceil(a)=O(1)=o(m).\n\nThe order conditions are strict: the base logarithmic model requires k+1>mc, and the anisotropic model requires k+1>mc-a. Equality in either integrability condition is divergent. In particular, if mc=N is an integer with N≥1, order N-1 fails and order N succeeds. The displayed floor and maximum formulas apply without any adjustment when mc or mc-a is an integer.\n\nBase-positivity conditions. On the Kähler base, hypothesis (a) is equivalent to the residual real (1,1)-class c_1(A)-c{D} being Kähler. If A is ample, then for the fixed metric h and any fixed smooth metric H_D there is a smooth real u such that θ+dd^c u is Kähler and θ+dd^c u-cη is Kähler for every sufficiently small c>0.\n\nExact local models. Under the same ambient and base-positivity hypotheses, conditions (b) and (c) are automatic under the following stronger selector assumptions. There is a compact smooth submanifold Z⊂π^{-1}(D) such that π|_Z:Z→D is a surjective submersion. At every point of Z there are adapted coordinates of the type in (c), with the same fixed c,p,b_1,...,b_r and 1≤r≤d, such that\n\nZ={z=w_1=...=w_r=0},\nφ=(c/p)log(|z|^{2p}+Σ_{j=1}^r|w_j|^{2b_j})+O(1).\n\nAssume also that φ is locally bounded on X\\Z. Then all conclusions of the criterion hold and, for every positive integer m,\n\nV_m=H^0(B,A^m(-K_mD)).\n\nReplacing φ by another member of PSH(X,ω) differing from it by a globally bounded function leaves every V_m unchanged and preserves these conclusions for the same ψ.\n\nNonempty family of genuinely non-descended selectors. Let B be a connected projective Kähler manifold, let A be ample with any fixed smooth Hermitian metric h, and let D⊂B be a nonempty smooth connected effective divisor. For any d≥1 take\n\nX=B×(P¹)^d,\n\nwith π the first projection and any fixed Hermitian form ω on X. Choose 1≤r≤d and marked points o_j in the first r fiber factors. Let E_j be the divisor where the j-th fiber coordinate equals o_j, let s_{E_j} be its defining section, and fix smooth Hermitian metrics on O(E_j) and O(D). For arbitrary positive integers p,b_1,...,b_r, set\n\nQ=||π^*s_D||^{2p}+Σ_{j=1}^r||s_{E_j}||^{2b_j},\nφ_λ=λ log Q,  c=pλ.\n\nThere is a finite constant C_0>0 such that\n\ndd^c log Q≥-C_0ω.\n\nConsequently φ_λ∈PSH(X,ω) whenever λ>0 and λC_0≤1. For every sufficiently small λ>0, both this condition and base positivity with c=pλ hold simultaneously. The singular locus is\n\nZ=D×{o_1}×...×{o_r}×(P¹)^{d-r}.\n\nThe weight is smooth outside Z, satisfies φ_λ≥c log||π^*s_D||², and near every point of Z satisfies\n\nφ_λ=λlog(|z|^{2p}+Σ_{j=1}^r|w_j|^{2b_j})+O(1).\n\nThus the exact-model conclusions apply, including the positive finite base mass, W_m⊂V_m for every m, the O(m^{q-1}) defect, and V_m=H^0(B,A^m(-K_mD)). For every b∈D, φ_λ is −∞ on a nonempty proper subset of π^{-1}(b) and finite on its complement. Hence it is not the pullback of a base weight, even modulo a bounded function.\n\nIn particular, for every q≥1 and d≥1, take B=P^q, A=O(1), and D a hyperplane, which is a point when q=1. With the Fubini–Study comparison metric on A and the Fubini–Study metric on O(D), choose u to accommodate the given metric h. For all sufficiently small λ>0, with c=pλ<1,\n\nβ=(1-c)ω_FS,\n∫_B⟨(θ+dd^cψ)^q⟩=(1-c)^q,\n\nwhere ∫_{P^q}ω_FS^q=1. Such λ can be chosen for any fixed Hermitian form ω on the product.\n\nSufficient singularity features and scope. The criterion requires a common horizontal logarithmic slope c, global domination excluding stronger unrelated selecting constraints, and an anisotropic singularity of that slope visible over an open part of D. The fixed finite transverse quantity S=Σ_j1/b_j contributes the m-independent correction a=pS to the required base vanishing order, without changing its linear coefficient c. Auxiliary fiber directions v and bounded errors do not alter the threshold. The global lower bound suffices for the inclusion and dimension-defect conclusions; the exact local models together with local boundedness outside Z suffice for the exact description of V_m. These are sufficient conditions, not a necessary-and-sufficient classification of arbitrary fiber singularities.\n\nThe isotropic section-over-divisor model is the specialization p=b_1=...=b_r=1, r=d, with Z a section over D; its order is max{0,floor(mc-d)}. The anisotropic result allows unequal powers p,b_j and r<d, and instead has order max{0,floor(mc-pΣ_j1/b_j)}.\n\nIf d=0, π is a biholomorphism and no genuinely non-descended weight exists. In this case, if ψ∈PSH(B,θ) has positive non-pluripolar mass and φ differs from π^*ψ by a bounded function, then V_m=H^0(B,A^m⊗I(mψ)) for every positive integer m.\n\nThe ambient assumptions alone do not guarantee a positive-mass base reference. For example, if A is trivial with its flat metric, then θ=0; every ψ∈PSH(B,0) that is not identically −∞ is constant, and its current has zero non-pluripolar top mass for q≥1. Thus no universal approximation assertion for arbitrary data or arbitrary upstairs selectors is made.",
        "proof": "We use the three results of w7-1/n1, proved first in this batch. All additional hypotheses in the criterion and in the exact-model assertion are assumed when proving their respective conclusions; their existence is established separately by the product examples below.\n\n1. Descent and the meaning of the spaces.\nThe map π is proper because X is compact. Each fiber is a connected compact complex manifold, so every holomorphic function on it is constant by the maximum principle. On an open set U⊂B trivializing A^m, a section of π* A^m is a holomorphic coefficient function on π^{-1}(U); it is constant on every fiber. The resulting function on U is holomorphic: through any point of a fiber, the holomorphic submersion theorem supplies a local holomorphic section of π, on which the coefficient can be evaluated. These descended functions glue with the transition functions of A^m. This proves H⁰(X,π* A^m)=H⁰(B,A^m), naturally and for every m.\n\nMultiplier-ideal membership is local integrability of the coefficient against exp(−mφ). Changing a smooth positive volume density, a smooth local bundle norm, or a holomorphic frame changes this test only by locally bounded positive factors with locally bounded reciprocals. Thus V_m and all other section spaces here are independent of auxiliary norms. In submersion coordinates, pullbacks of locally integrable base functions are locally integrable, by Fubini and comparison with product Euclidean volume.\n\n2. Construction, positivity, and mass of the base reference.\nAssume (a)–(c), and let ℓ=log||s_D||². The defining section is not identically zero, so the supplied Poincaré–Lelong identity applies:\ndd^cℓ=[D]−η.\nThe function ψ=u+cℓ is upper semicontinuous and quasi-psh, including its value −∞ on D. Hence\nθ+dd^cψ=θ+dd^cu−cη+c[D]=β+c[D]≥0.\nThus ψ∈PSH(B,θ).\n\nOn B\\D this current is the smooth form β. The analytic divisor D is pluripolar, so the supplied properties of the non-pluripolar product show that its top product agrees with β^q off D and gives no mass to D. The smooth measure β^q also gives no mass to D. Consequently, as measures on B,\n⟨(θ+dd^cψ)^q⟩=β^q.\nSince β is Kähler and B is a nonempty compact manifold of dimension q≥1,\n0<∫_Bβ^q<∞.\nThis establishes finite positive non-pluripolar mass, not merely positivity of the current.\n\n3. Base multiplier ideals and the lower inclusion.\nIn coordinates (z,t) in which D={z=0}, smoothness of the metrics and u gives ψ=c log|z|²+O(1), with a locally bounded error. For a holomorphic coefficient z^k times a unit, integrability in the z direction is equivalent to\n∫₀^ε r^{2k−2mc+1}dr<∞, i.e. k+1>mc.\nThus the minimum permissible nonnegative integer is L_m=⌊mc⌋. This also proves the ideal equality for arbitrary germs: divisibility by z^{L_m} is sufficient; if a germ has smaller z-order, its first nonzero coefficient in its z-expansion is nonzero on an open set of t-values arbitrarily close to the point, and the integral diverges on a smaller product neighborhood of such values. When q=1 there are no t variables. Away from D the weight is smooth. It follows that\nI(mψ)=O_B(−L_mD),\nW_m=H⁰(B,A^m(−L_mD)).\n\nBecause u is smooth on compact B, hypothesis (b) implies, with a finite constant C₁,\nφ≥π*ψ−C₁.\nIf a descended section belongs to W_m, the function |g|²exp(−mψ) is locally integrable downstairs. Its pullback is locally integrable upstairs, and almost everywhere\n|π*g|²exp(−mφ)≤exp(mC₁)|π*g|²exp(−mπ*ψ).\nTherefore W_m⊂V_m for every positive integer m. No uniform bound in m on this comparison constant is required for an equality or inclusion of these integrability-defined spaces.\n\n4. The anisotropic upper constraint.\nWrite S=Σ_{j=1}^r1/b_j and a=pS. In the chart of (c), a descended coefficient g depends only on (z,t). Let\nK_m=max{0,⌊mc−a⌋}.\nWe prove that membership in V_m forces divisibility by z^{K_m} in this base chart. There is nothing to prove if K_m=0. Otherwise, if divisibility fails, write g=z^k h(z,t) with k<K_m and h(0,t) not identically zero. Choose a t-value where h(0,t)≠0 and shrink the z,t domains so |h| is bounded below by a positive constant. If q=1 this simply uses the nonzero leading coefficient. The estimate in (c) gives\n|g|²exp(−mφ)≥C_m |z|^{2k} (|z|^{2p}+Σ_j|w_j|^{2b_j})^{-mc/p}\non this smaller chart. The v and t variables are auxiliary variables ranging over sets of positive finite volume. Part 1 of w7-1/n1 says that this integral is finite exactly when\nk+1>mc−pΣ_j1/b_j=mc−a.\nBy the definition of K_m it is not finite for k<K_m, contradicting membership in V_m.\n\nThus every section in V_m vanishes to order at least K_m along a nonempty open part of D. This propagates to all of the connected divisor D by the holomorphic identity theorem. More explicitly, its restriction to D vanishes on that open part and hence everywhere; after factoring once by the defining divisor section, restrict the resulting section to D and repeat. Induction gives the global divisibility of order K_m. This argument also covers q=1, where D is one point. We have proved\nW_m⊂V_m⊂H⁰(B,A^m(−K_mD))\nfor every m≥1, using only one adapted chart for the upper constraint.\n\n5. The dimension defect and the endpoints.\nPut x=mc>0. Since a>0,\n0≤K_m=max{0,⌊x−a⌋}≤L_m=⌊x⌋.\nAlso\nL_m−K_m≤⌊x⌋−⌊x−a⌋≤⌈a⌉.\nWe have L_m=O(m). Part 3 of w7-1/n1, applied with this fixed divisor and these two sequences, therefore gives\n0≤dim V_m−dim W_m\n≤h⁰(B,A^m(−K_mD))−h⁰(B,A^m(−L_mD))\n=O(m^{q−1})=o(m^q).\nFor q=1 the same supporting result gives the sharper bound\n0≤dim V_m−dim W_m≤L_m−K_m≤⌈a⌉=O(1)=o(m).\nIn that dimension the mass identity reads ⟨θ+dd^cψ⟩=β.\n\nBoth integrability inequalities are strict. If mc=N≥1 is an integer, base order N−1 gives logarithmic divergence, whereas N is integrable. If mc−a=N≥1 is an integer, the anisotropic integral similarly diverges at order N−1 and is finite at N. When mc−a=0 the formal equality order −1 is not a nonnegative order and K_m=0; if mc−a<0, order 0 is also allowed. These observations explain why the displayed floors and maximum need no endpoint adjustment.\n\n6. Geometric ways to ensure base positivity.\nThe form θ−cη is smooth, real, and closed, and represents c₁(A)−c{D}. If (a) holds, β is a Kähler representative of that class. Conversely, if the residual real (1,1)-class is Kähler, choose a Kähler representative κ. The difference κ−(θ−cη) is a smooth real d-exact (1,1)-form on the compact Kähler manifold B. The supplied dd^c lemma gives a smooth real u with κ=θ+dd^cu−cη, which is precisely (a).\n\nIf A is ample, the supplied ample-metric premise gives a Kähler curvature form κ in c₁(A). Applying the same dd^c lemma to κ−θ gives a smooth real u with θ+dd^cu=κ. On compact B, the fixed smooth form η satisfies η≤Cκ for some finite C>0 after enlarging C if needed. Thus κ−cη is positive for every sufficiently small c>0. This gives one u working for all these c, with the given metrics h and H_D unchanged.\n\n7. Exact local models.\nNow assume the stronger hypotheses involving the compact smooth Z, the submersion Z→D, the fixed exponents, the exact bounded-error models at every point of Z, and local boundedness on X\\Z.\n\nNear Z the lower half of the bounded-error equality gives\nφ≥(c/p)log(|z|^{2p}+Σ_j|w_j|^{2b_j})−C_loc\n≥c log|z|²−C_loc.\nThe norm of π*s_D differs from |z| by a smooth positive factor in each such chart. Thus this is the lower bound in (b), locally near Z. Finitely many of these neighborhoods cover compact Z. On the compact complement of a smaller union of such neighborhoods, local boundedness of φ supplies a uniform lower bound after taking a finite cover; log||π*s_D||² has a finite global upper bound. Combining the two regions proves (b) with one finite global constant. The upper half of the model gives (c) in any one such chart. These charts exist over D because Z→D is surjective. Hence all the conclusions already proved apply.\n\nFor the reverse inclusion giving the exact formula, let g∈H⁰(B,A^m(−K_mD)). In every adapted chart at Z its pullback is z^{K_m} times a holomorphic bounded coefficient on a smaller chart. The lower half of the exact model bounds its integrability test above by a constant times\n|z|^{2K_m} (|z|^{2p}+Σ_j|w_j|^{2b_j})^{-mc/p}.\nThis is integrable by w7-1/n1, since K_m+1>mc−a. Auxiliary t,v variables do not change that fact. Away from Z, φ is locally bounded and imposes no condition on a holomorphic section. Therefore this section belongs to V_m, and\nV_m=H⁰(B,A^m(−K_mD))\nfor every m≥1.\n\nIf φ′∈PSH(X,ω) is boundedly equivalent to φ, the inequalities φ−C≤φ′≤φ+C imply that the two integrability tests differ by factors between exp(−mC) and exp(mC), for each m. Hence all V_m remain unchanged. The same lower and upper hypotheses remain true after changing constants, so the conclusions hold with the same ψ.\n\n8. Actual non-descended examples, including arbitrary anisotropic exponents.\nTake the projective Kähler B, ample A, smooth connected nonempty D, and product X=B×(P¹)^d specified in the note. This X is connected and compact, and its first projection is a holomorphic submersion with connected fibers. Fix the indicated smooth metrics and sections, choose 1≤r≤d, and define\nQ=||π*s_D||^{2p}+Σ_{j=1}^r||s_{E_j}||^{2b_j}.\nIts common zero set is exactly\nZ=D×{o₁}×⋯×{oᵣ}×(P¹)^{d−r}.\nThis is a compact smooth submanifold, and Z→D is a surjective submersion.\n\nWe verify the asserted uniform lower curvature bound, rather than assume log Q is quasi-psh. In a local holomorphic trivialization, write\nQ=Σ_{j=0}^r |f_j|²e^{-ρ_j},\nwhere f₀ is the p-th power of the local defining function of π^{-1}(D), f_j is the b_j-th power of a defining function of E_j, and the ρ_j are smooth real metric weights. On a relatively compact coordinate neighborhood choose a smooth quadratic function v=A|ξ|² with A so large that dd^c(v−ρ_j)≥0 for every j. For ε>0, each function\nv−ρ_j+log(|f_j|²+ε)\nis smooth plurisubharmonic. The log-sum-exponential of finitely many smooth psh functions is psh: differentiating shows its complex Hessian is the weighted sum of their Hessians plus a positive semidefinite covariance term. Accordingly\nv+log(Σ_j(|f_j|²+ε)e^{-ρ_j})\nis psh. On compact subsets outside Z these functions converge in C∞, as ε decreases to zero, to v+log Q. Thus v+log Q is psh there. It is locally bounded above near the proper analytic set Z. Moreover Q tends to zero at Z, so its upper-limit extension there is −∞. The supplied psh extension premise applies and proves that v+log Q is psh on the whole coordinate neighborhood.\n\nIt follows locally that dd^c log Q≥−dd^cv. On the smaller neighborhood, dd^cv≤C_iω because ω is a smooth positive Hermitian form. A finite cover of compact X gives a finite C₀>0 with\ndd^c log Q≥−C₀ω\nas currents on X. Consequently φ_λ=λ log Q satisfies\nω+dd^cφ_λ≥(1−λC₀)ω≥0\nwhenever λ>0 and λC₀≤1. It is upper semicontinuous and quasi-psh by the local construction, so φ_λ∈PSH(X,ω).\n\nNear any point of Z, use a base coordinate z defining D and fiber coordinates w_j defining the marked points, with t and v the remaining coordinates. Smooth metric factors are bounded above and below by positive constants on a smaller chart. Hence Q is comparable to |z|^{2p}+Σ_j|w_j|^{2b_j}, giving\nφ_λ=λ log(|z|^{2p}+Σ_j|w_j|^{2b_j})+O(1).\nIt is smooth outside Z, and the global inequality Q≥||π*s_D||^{2p} gives\nφ_λ≥pλ log||π*s_D||².\nThus the exact-model assumptions hold with c=pλ. By part 6, base positivity holds for all sufficiently small c; choose λ>0 sufficiently small to satisfy both that restriction and λC₀≤1. All the claimed conclusions, including the exact formula for V_m, now follow from parts 2–7.\n\nFor every b∈D, the −∞ locus of φ_λ in its fiber is precisely the nonempty proper subset\n{o₁}×⋯×{oᵣ}×(P¹)^{d−r};\nφ_λ is finite elsewhere in that fiber. A pullback base weight is either finite on the entire fiber or −∞ on the entire fiber. Bounded equivalence preserves the −∞ locus. Hence these selectors are not descended, even modulo a bounded function.\n\nFor completely explicit examples in every q≥1 and d≥1, take B=P^q, A=O(1), and D a hyperplane (one point when q=1). Give O(D) its Fubini–Study metric, so η=ω_FS. With the prescribed metric h on A, part 6 supplies u satisfying θ+dd^cu=ω_FS. Thus, for sufficiently small λ>0 with c=pλ<1,\nβ=(1−c)ω_FS,\n∫_B⟨(θ+dd^cψ)^q⟩=(1−c)^q,\nusing the normalized Fubini–Study curvature ∫_{P^q}ω_FS^q=1. The curvature-bound argument works for any fixed Hermitian form ω on the product.\n\n9. Precisely what the fiber singularities contribute, and the scope.\nThe lower bound (b) excludes any stronger unrelated global selecting constraints and proves the lower inclusion. The upper model (c), required only over a nonempty open part of the connected D, proves the upper inclusion. Together they suffice for the bounded-band approximation; exact models on all of Z and boundedness off Z are not required for that approximation. In this context, (b) is the only global singularity-control hypothesis needed for the dimension-defect argument. The lower bound alone, without (c), would give only W_m⊂V_m and is not asserted to imply a small defect.\n\nThe transverse exponents contribute S=Σ_j1/b_j through the transverse integration, and thereby the fixed correction a=pS. The linear coefficient of the required base vanishing remains c; the correction is independent of m. Unused fiber directions v, extra base directions t, holomorphic units, and bounded errors do not affect the threshold. Exact bounded-error models everywhere on Z together with local boundedness away from Z upgrade the sandwich to an exact description of V_m. These are sufficient features, not a necessary-and-sufficient classification of arbitrary upstairs selectors.\n\nThe section-over-divisor isotropic model is the specialization p=b₁=⋯=bᵣ=1, r=d, with Z a section over D. Then a=d and the order is max{0,⌊mc−d⌋}. The anisotropic assertion proved here genuinely allows unequal p,b_j and r<d, replacing d by pΣ_j1/b_j, and the criterion requires neither a global section nor a global splitting of normal coordinates.\n\nFinally, if d=0, the connected zero-dimensional fibers are single points. The submersion is then a bijective local biholomorphism, hence a biholomorphism. Every upstairs function descends. If φ is boundedly equivalent to π*ψ for a θ-psh ψ of positive mass, the same integrability comparison under this biholomorphism proves V_m=H⁰(B,A^m⊗I(mψ)) for every m.\n\nThe original ambient assumptions do not ensure the existence of any positive-mass base reference. Indeed, for trivial A with its flat metric, θ=0. A non-identically −∞ globally psh function on connected compact B attains its maximum and is constant by the strong maximum principle. Its current dd^cψ is zero and has zero non-pluripolar top mass for q≥1. Thus the sufficient hypotheses above are genuine extra hypotheses, and no universal approximation or classification is claimed."
      }
    }
  ]
}

## Root exact primary applications

{
  "recorded_at_utc": "2026-10-07T09:12:12.945196+00:00",
  "unchanged_original_task_matches_accepted_result": true,
  "whole_two_generated_notes_and_both_full_independent_reconstructions_actually_root_read": true,
  "all_correctness_source_requirements_reports_and_all_five_premises_and_eight_passages_actually_root_read": true,
  "whole_current_standalone_source_actually_root_read": true,
  "source_sha256": "7904f540e8c6b52fed8f103d786d23af19ebf416125e23ea3b77166f9f7f8c11",
  "applications": [
    {
      "premise": 0,
      "pdf": "P21-Andersson-Poincare-Lelong-0412446.pdf",
      "text": "P21-Andersson-Poincare-Lelong-0412446.txt",
      "actually_root_read_lines": [
        [
          1,
          65
        ]
      ],
      "judgment": "The primary operator is i/pi times partial barpartial. Its log inverse norm formula yields exactly the task i/(2pi) squared-norm formula; D is a reduced divisor of a nonzero defining section. Demailly agbook equation13.2 independently corroborates normalization.",
      "pdf_sha256": "8feb2abf34ced44a6961b0ab5bf80a2b3a09aa40a85c0a0cdbaf2e3eb4a84715",
      "text_sha256": "f1f3ca0ea6a31f4070fe57568a604ad530827ac92685dc71be7583bc103eddf2"
    },
    {
      "premise": 1,
      "pdf": "P21-Tosatti-ddc-lemma-1508.04823.pdf",
      "text": "P21-Tosatti-ddc-lemma-1508.04823.txt",
      "actually_root_read_lines": [
        [
          155,
          235
        ]
      ],
      "judgment": "Lemma2.1 is for an exact smooth real(1,1) form on a compact Kahler manifold. u=2pi times its potential converts normalization. This proves the residual Kahler-class equivalence in the accepted note; the current paper assumes the actual positive residual and uses the smooth metric ratio for examples.",
      "pdf_sha256": "898475fc61323c7632f8c96baed381d611b412154c263f4757c4ea668adbc453",
      "text_sha256": "65dfe6cfb02ac2732184d434b47a0032c3272eb7a0f98a1f273cfb42b6bce105"
    },
    {
      "premise": 2,
      "pdf": "P21-Demailly-ample-9410022.pdf",
      "text": "P21-Demailly-ample-9410022.txt",
      "actually_root_read_lines": [
        [
          1390,
          1450
        ]
      ],
      "judgment": "Section3.15 takes ample to mean a positive tensor power very ample and constructs the positive metric by pulling back Fubini-Study and taking its tensor root. This is the exact premise; its converse Kodaira assertion is unused. The primary self-reference to Example3.15 is a harmless typo for preceding Example3.14.",
      "pdf_sha256": "8896b6856b2380a53ce725714e9358007cc82b3d0523efba651565bf8ad559e2",
      "text_sha256": "0d94cbc745d888d8dac0e4e15ef85b482267ed0998f07d52367bd51e235ee2d9"
    },
    {
      "premise": 3,
      "pdf": "BEGZ-Monge-Ampere-big-classes-0812.3674.pdf",
      "text": "BEGZ-Monge-Ampere-big-classes-0812.3674.txt",
      "actually_root_read_lines": [
        [
          165,
          260
        ]
      ],
      "judgment": "The defining truncation measure is local, discards the pole locus, and for small unbounded locus equals extension of the ordinary wedge off it when that mass is locally finite. Here off D the wedge is the smooth beta^q with finite mass, so the product is well-defined and equals beta^q, including q1 formula229. No arbitrary singular finite-mass assertion is imported.",
      "pdf_sha256": "43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd",
      "text_sha256": "9d52c95247fd7f69194c84df01ef54b4cd98b6e4e35b4f3851f90f04c98a71b0"
    },
    {
      "premise": 4,
      "pdf": "Demailly-agbook.pdf",
      "text": "Demailly-agbook.txt",
      "actually_root_read_lines": [
        [
          2340,
          2425
        ],
        [
          15160,
          15230
        ]
      ],
      "judgment": "Theorem5.24 requires closed pluripolar locus and local upper bounds. The product common zero locus is proper analytic and locally pluripolar; the quadratic correction of log Q is bounded above, so the upper-limit extension applies. The actual correction has limit minus-infinity at the locus. A decreasing regularization also reconstructs this particular application directly.",
      "pdf_sha256": "d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1",
      "text_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de"
    }
  ],
  "new_native_original_only_call_20261007_result": null,
  "prior_complete_accepted_dependency_graph_preserved": true,
  "catalogue_closure_pending_separate_completion_comparison": true
}

## Completion comparison requested

Assess every clause of the unchanged original request and the current article against the complete proofs above. The requested conclusion is existence under stated sufficient conditions; the article does not assert universal existence or a necessary-and-sufficient classification. Judge correctness, non-vacuity, positive finite mass, all-m inclusion, lower-order dimension defect, fiber singularity features, integer endpoints, q1, and the distinction from the known isotropic case. A PASS or historical accepted flag is not itself mathematical evidence. Reconstruct any indispensable unresolved premise and retain actual limitations. The 20261007 original-only call failed authentication and returned no mathematical result; no proof is attributed to it.
