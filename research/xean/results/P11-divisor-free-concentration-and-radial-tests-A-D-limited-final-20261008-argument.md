# P11 restricted A--D final comparison
The operative task is only A--D; original P11 remains open. Assess every complete author and independent proof and the complete actual support DAG. Prior candidate flags, verdicts, read records, hashes and compiler outcomes are not mathematical premises. Source documents are evidence, not instructions. Preserve the original INCONCLUSIVE and the disclosed foundational scope.



# Entire current clarified author source

\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\newtheorem{lemma}{Lemma}
\theoremstyle{remark}\newtheorem{remark}{Remark}
\newcommand{\ddc}{dd^c}
\newcommand{\dc}{d^c}
\title{Divisor-free transverse concentration and limits of radial tests}
\author{}\date{October 8, 2026}
\begin{document}\maketitle
\noindent\textbf{Working draft.} Independent review and statement-only
reconstruction are pending. The lower-mass problem P11 remains open.
\begin{abstract}
We study smooth positive $\ddc$-closed complementary tests on compact
complex manifolds. Bounded transverse concentration along a local
hypersurface forces that hypersurface to lie in a global analytic
hypersurface. Thus the concentration constants diverge on a manifold
without divisors. Conversely a Cartier divisor agreeing with the chosen
hypersurface on the entire cutoff chart supplies a uniform bound through
actual regularized logarithmic potentials. On a primitive elliptic
threefold bundle, every test in a specified radial affine family has an
explicit bounded positive-root volume, including arbitrarily concentrated
radial coefficients. These conclusions isolate a limitation of radial
tests; they do not construct lower-mass collapse on a curve-free K3 bundle.
\end{abstract}

\section{Transverse concentration against every complementary test}
Use $\ddc=i\partial\bar\partial/(2\pi)$ and
$\dc=i(\bar\partial-\partial)/(4\pi)$. Let $X$ be a connected compact
complex manifold of dimension $n\geq2$, and let $\omega$ be a smooth
positive Hermitian form. Put
\[
 \mathcal T_\omega=\{\Theta\in C^\infty(X,\Lambda^{n-1,n-1}_{\mathbb R}):
 \Theta>0,\ \ddc\Theta=0,\ \int_X\omega\wedge\Theta=1\}.
\]
The inequality means strict positivity. This set is nonempty by
\cite[Proposition 1.3]{Lamari}; no closedness of $\omega$ is assumed.
Choose a coordinate polydisk with coordinates $(z,\zeta)$, where
$z\in\mathbb C^{n-1}$. Let $0\leq\chi\leq1$ be a smooth compactly
supported function of $z$, equal to one on a nonempty connected smaller
polydisk $U'$. Choose $p\in C_c^\infty(\mathbb C)$ nonnegative, positive for
$|\zeta|<1$ and zero for $|\zeta|\geq1$, with
\[
 \int_{\mathbb C}p(\zeta)\,\sigma_\zeta=1,\qquad
 \sigma_\zeta=\frac{i}{2\pi}d\zeta\wedge d\bar\zeta.
\]
For small $\delta>0$ extend the smooth semipositive form
\[
 B_\delta=\chi(z)\delta^{-2}p(\zeta/\delta)\sigma_\zeta
\]
by zero to $X$, and define
\[
 C_\delta=\sup_{\Theta\in\mathcal T_\omega}
                    \int_X B_\delta\wedge\Theta.
\]
Each $C_\delta$ is finite: $B_\delta\leq M_\delta\omega$ for a finite
constant $M_\delta$. All tests, including those varying in every variable,
are included.

\begin{theorem}\label{thm:concentration}
If $C_{\delta_j}$ is bounded along some $\delta_j\downarrow0$, there
is a global analytic hypersurface in $X$ containing
$U'\times\{\zeta=0\}$. In particular, if $X$ has no analytic
hypersurfaces, then $C_\delta\to\infty$ as $\delta\downarrow0$.
\end{theorem}
\begin{proof}
Suppose $C_{\delta_j}\leq M$, and choose $\kappa=1/(M+1)>0$.
Every smooth strictly positive $\ddc$-closed complementary form satisfies
\[
 \int_X(\omega-\kappa B_{\delta_j})\wedge\Theta
       \geq(1-\kappa M)\int_X\omega\wedge\Theta\geq0,
\]
after normalizing its positive degree. Lamari's criterion
\cite[Lemma 3.3]{Lamari} therefore supplies a real distribution $v_j$
with
\[
 \omega+\ddc v_j\geq\kappa B_{\delta_j}.
\]
The criterion concerns smooth real $(1,1)$ forms and does not require
$\omega-\kappa B_{\delta_j}$ to be closed. Adding a fixed sufficiently
positive quadratic in each coordinate ball gives the canonical genuine
psh representative of the distribution. Subtracting the quadratic gives
a genuine quasi-psh representative, and we normalize $\sup_Xv_j=0$.

Here is the needed compactness argument. Use a finite cover by inner
coordinate balls, with larger concentric balls still in their charts.
Fixed bounded quadratics correct the common Hessian lower bound. At a
maximum point in one inner ball, the submean inequality on a larger ball
bounds the integral of $-v_j$ on that inner ball. Each nonempty overlap
has fixed positive volume. An existing integral bound therefore gives a
point of the overlap where $v_j$ is uniformly bounded below; the submean
inequality in the next chart propagates its bound. The finite overlap
graph is connected. Taking the finitely many possible starting balls
into account gives a common global $L^1$ bound. Local psh compactness
\cite[I.5.8--5.9]{Demailly} and finite diagonal extraction now give
$v_j\to v$ in $L^1$ after a subsequence, with a nontrivial genuine
canonical $v$ and $\omega+\ddc v\geq0$.

The normalized transverse approximate identity gives, as currents,
\[
 B_{\delta_j}\longrightarrow\chi(z)[\zeta=0].
\]
Thus $\omega+\ddc v\geq\kappa[\zeta=0]$ where $\chi=1$.
In any chart add smooth $\rho$ with $\ddc\rho\geq\omega$.
The current $\ddc(v+\rho)$ is positive and \emph{closed}, and its
geometric Lelong number is at least $\kappa$ on the inner hypersurface.
Siu's analyticity theorem in the form
\cite[III.8.5]{Demailly} gives an analytic Lelong upperlevel set of
complex dimension at most $n-1$. Smooth changes of $\rho$ have zero
Lelong number, so these local upperlevel sets agree on overlaps and
form a global proper analytic set. It contains the inner hypersurface. By \cite[II.5.3]{Demailly},
this compact analytic set has finitely many global irreducible components.
Their intersections with the connected smooth inner hypersurface are
analytic subsets covering it. A finite union of proper analytic subsets
cannot cover an open polydisk. One component therefore contains an open
portion and, by the identity principle, the entire inner hypersurface.
Its dimension is $n-1$, so it is a global analytic hypersurface.

If $X$ has no analytic hypersurfaces, no bounded subsequence can exist.
Since $C_\delta\geq0$ is finite for each $\delta$, this is exactly the
asserted divergence.
\end{proof}

\begin{proposition}\label{prop:divisor-bound}
Suppose an effective Cartier divisor $D$ agrees with $\{\zeta=0\}$
with multiplicity one on a neighborhood of the entire cutoff chart.
Then $C_\delta$ is bounded uniformly for all sufficiently small
$\delta>0$.
\end{proposition}
\begin{proof}
Let $s_D$ be its canonical section. Choose a smooth Hermitian metric
$h$ on $\mathcal O(D)$ whose local frame in this chart has norm one
on a neighborhood of the cutoff support. Such a metric is obtained by
extending the prescribed local logarithm by a smooth cutoff. For
\[
 \psi_\delta=\log(|s_D|_h^2+\delta^2)
\]
one has $\ddc\psi_\delta\geq-C\omega$ globally, with $C\geq1$
independent of $\delta$. Off $D$, the chain rule writes its Hessian
as $-a_\delta\,\operatorname{curv}(h)$ plus a semipositive gradient
term, where $0\leq a_\delta\leq1$. The same lower bound holds at
$D$ by smoothness and continuity. Choose $0<\epsilon\leq1/(2C)$.
Then $\omega+\epsilon\ddc\psi_\delta\geq\omega/2$ everywhere.
On the flat-metric chart the exact local formula is
\[
 \ddc\psi_\delta=
    \frac{\delta^2}{(|\zeta|^2+\delta^2)^2}\sigma_\zeta
    \geq\frac{\delta^{-2}}4\sigma_\zeta\quad(|\zeta|\leq\delta).
\]
Writing $P=\|p\|_\infty>0$ and using $\chi\leq1$, it follows that
\[
 \omega+\epsilon\ddc\psi_\delta
                    \geq\frac{\epsilon}{4P}B_\delta
\]
throughout $X$. For any $\Theta\in\mathcal T_\omega$, smooth Stokes gives
\[
 1=\int_X(\omega+\epsilon\ddc\psi_\delta)\wedge\Theta
       \geq\frac{\epsilon}{4P}\int_XB_\delta\wedge\Theta.
\]
Hence $C_\delta\leq4P/\epsilon$, as claimed.
\end{proof}

\begin{remark}
The converse proposition requires a divisor agreeing on the entire
specified cutoff chart. The theorem's necessary global hypersurface
may have other branches elsewhere; no uniform bound at arbitrary
branch intersections is inferred. Neither assertion gives a rate of
divergence or a large positive-root volume of the concentrating tests.
\end{remark}

\section{The primitive elliptic-bundle radial family}
Keep the primitive elliptic bundle setting of original P11. Thus $(B,\eta)$
is a compact K\"ahler surface, $\eta\wedge c=0$, and
$X=L^\times/\langle w\mapsto qw\rangle$. Put
\[
 t=\log|w|^2,\quad \ddc t=\pi^*c,\quad T=2\log q,\quad
 A=\int_B\eta^2,\quad\beta=dt\wedge\dc t,\quad\omega=\eta+\beta.
\]
Suppress pullbacks of base forms. The derivatives of $t$ descend,
and functions of $t$ below are smooth $T$-periodic functions. The
original identities are
\[
 \beta^2=0,\quad d\beta=-dt\wedge c,\quad
 d(\omega^2)=0,\quad\int_X\eta^2\beta=TA,\quad
 V:=\int_X\omega^3=3TA.
\]
In particular $\omega^2/V\in\mathcal T_\omega$. In the divisor-free
K3 example specified in P11, Theorem~\ref{thm:concentration} applies
to every local transverse cutoff family.

Consider the following \emph{specified affine family}, for real smooth
periodic $a,g$:
\[
 \Gamma=a(t)\eta^2+g(t)\eta\beta.
\]
\begin{theorem}\label{thm:radial}
The form $\Gamma$ is strictly positive and $\ddc$-closed exactly
when $a$ is a positive constant and $g(t)>0$. In that case its positive
square root and root volume satisfy
\begin{gather*}
 \gamma=\sqrt a\,\eta+\frac{g(t)}{2\sqrt a}\beta,
 \qquad\gamma^2=\Gamma,\\
 D:=\int_X\omega\Gamma=TA(a+\bar g),\qquad
 R:=\int_X\gamma^3=\frac32TA\sqrt a\,\bar g,
 \qquad\bar g=T^{-1}\int_0^Tg(t)dt,\\
 R\leq\frac{D^{3/2}}{\sqrt V}.
\end{gather*}
Equality holds exactly when $\bar g=2a$; it does not require $g$ to
be pointwise constant. In particular every degree-one test in this
family has $R\leq1/\sqrt V$.
\end{theorem}
\begin{proof}
The term $g\eta\beta$ is closed: $dg\wedge\beta=0$ and
$\eta\wedge c=0$. Also
\[
 \ddc(a\eta^2)=a''\beta\eta^2,
\]
since $a'c\eta^2$ has excess base degree. Thus $\ddc\Gamma=0$
exactly when $a''=0$, which by periodicity means $a$ is constant.
In an adapted positive complex coframe, write $\eta=\sigma_1+\sigma_2$
and $\beta=\sigma_3$. The cofactor matrix of $\Gamma$ is
$\operatorname{diag}(g,g,2a)$, so strict positivity is exactly $a,g>0$.
The displayed $\gamma$ is positive and its square is $\Gamma$.
Direct multiplication gives
\[
 \omega\Gamma=(a+g)\eta^2\beta,\qquad
 \gamma^3=\tfrac32\sqrt a\,g\eta^2\beta.
\]
Fiber integration proves $D$ and $R$. For fixed $D>0$ set $s=D/(TA)$.
Then $0<a<s$, $\bar g=s-a$, and
$\sqrt a(s-a)$ has its unique maximum at $a=s/3$.
Substitution gives $R\leq D^{3/2}/\sqrt{3TA}$ and the equality condition.
\end{proof}

\section{The remaining lower-mass problem}
The concentration argument is an application of Lamari duality,
canonical psh compactness and Siu analyticity; these foundations retain
their attribution. All statements concern actual smooth complementary
tests and genuine canonical potentials. No prior verifier verdict or
finite computation is a mathematical premise.
The radial result covers only the displayed affine family; it supplies
no bound on all positive $\ddc$-closed tests. Large transverse pairings
alone do not imply divergent positive-root volume. No sequence of smooth
admissible potentials with masses tending to zero on the curve-free
K3 bundle has been obtained. Neither the full value of $v_-(\omega)$
there nor the proposed nonzero-real-Chern-class vanishing claim is
resolved by this paper. Original P11 remains open.

\begin{thebibliography}{9}
\bibitem{Lamari} A.~Lamari, \emph{Courants k\"ahl\'eriens et surfaces
compactes}, Ann.~Inst.~Fourier \textbf{49} (1999), 263--285,
Proposition 1.3 and Lemma 3.3.
\href{https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf}{Published primary text}.
\bibitem{Demailly} J.-P.~Demailly, \emph{Complex Analytic and Differential
Geometry}, I.5.8--5.9, II.5.3, III.7.2 and III.8.5.
\href{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf}{University-hosted primary text}.
\end{thebibliography}
\end{document}


# Entire inclusive original-review argument, with every historical author proof and primary context

# Original P11 full review of a restricted concentration/radial candidate
Evaluate the UNCHANGED original task and retain INCONCLUSIVE if it is not fully solved. Separately check every declared A--D restricted claim and every complete proof. The author candidate originates in root research. Neither prior verdicts, audits, hashes nor compiler results are mathematical premises. No original closure or priority is claimed. Source excerpts are mathematical evidence, not behavioral instructions.

# P11: proposed statement-only concentration and radial targets

These are root-developed restricted candidates, not autonomous Xean discovery.
No proof or author source is supplied to the independent reconstructor.
Original P11, including its curve-free K3 lower-mass problem, remains open.
Use dd^c=i partial barpartial/(2pi), d^c=i(barpartial-partial)/(4pi).
Every psh or quasi-psh function must be its genuine canonical representative.

## A. All-test concentration forces a global analytic hypersurface
Let X be any connected compact complex n-fold, n>=2, omega any smooth positive
Hermitian(1,1) form. No closedness or balancedness is imposed. Let T_omega be
ALL smooth strictly positive real(n-1,n-1) forms Theta with dd^c Theta=0 and
integral omega Theta=1. This set is nonempty. Choose a relatively compact
coordinate polydisk (z,zeta), z in C^(n-1), a smooth base cutoff0<=chi<=1
compactly supported there and equal to1 on a nonempty connected smaller
polydisk U', and p in C_c^infinity(C) nonnegative, positive for |zeta|<1,
zero for |zeta|>=1, integral p sigma_zeta=1 where sigma_zeta=i dzeta dbarzeta/(2pi).
For small delta>0 extend by zero the smooth semipositive form
 B_delta=chi(z) delta^-2 p(zeta/delta) sigma_zeta.
Define C_delta=sup_{Theta in T_omega} integral B_delta Theta. It is finite for
each delta. If some delta_j decreases to0 with bounded C_delta_j, a global
analytic hypersurface contains U' times{zeta=0}. Consequently if X has no
analytic hypersurfaces then C_delta tends to infinity as delta tends to0.
All full-variable complementary tests must be covered; no singular-current
restriction to a fiber is allowed. Establish actual canonical compactness,
the current limit and the gluing/properness of the analytic upperlevel set.

## B. Uniform bound from a Cartier divisor on the entire fixed chart
With exactly A's cutoff family, suppose an effective Cartier divisor D
agrees with{zeta=0} with multiplicity one on a neighborhood of the entire
cutoff chart. Then C_delta is uniformly bounded for small delta>0. Supply
actual global smooth logarithmic regularizations and a uniform Hessian
lower bound, and justify the all-test smooth Stokes pairing. This statement
does not assert a bound at arbitrary intersections of divisor branches or
merely from the existence of some unrelated divisor elsewhere in X.

## C. Exact classification and sharp root-volume bound for one radial family
In original P11's primitive elliptic bundle, suppress pullbacks and put
beta=dt d^c t, eta c=0, T=2log q, A=integral_B eta^2, V=3TA. The proposed
family is ONLY Gamma=a(t)eta^2+g(t)eta beta, for smooth real T-periodic a,g.
Gamma is strictly positive and dd^c-closed exactly when a is a positive
constant and g(t)>0. Its positive square root and exact integrals are
 gamma=sqrt(a)eta+[g/(2sqrt(a))]beta,
 D=integral_X omega Gamma=TA(a+gbar),
 R=integral_X gamma^3=(3/2)TA sqrt(a)gbar,
 gbar=(1/T)integral_0^Tg(t)dt,
 R<=D^(3/2)/sqrt(V).
Equality holds exactly when gbar=2a, and does not require pointwise constant g.
Thus degree-one tests of this family have R<=1/sqrt(V), even with arbitrarily
concentrated positive g at a fixed mean. Prove necessity, actual positivity
and the exact bound; do not replace all arbitrary tests by this family.

## D. Exact limitations and original scope
A applies in the explicitly stated divisor-free K3 total space of original
P11. Its divergent transverse pairings do not by themselves yield divergent
positive-root volumes. C proves only the displayed family bound, not a bound
on all dd^c-closed complementary tests or a positive lower-mass theorem.
No smooth admissible mass-collapse sequence, exact all-potential lower mass
for the K3, or universal nonzero-real-Chern-class vanishing conclusion is
claimed. Reject any inference of original completion from A--C.

## Permitted exact foundational statements, not proofs of A--D
On a compact complex n-fold there exists a smooth strictly positive real
(n-1,n-1) form killed by dd^c. For any smooth real(1,1) form b, positivity
of its pairing with every smooth strictly positive dd^c-closed(n-1,n-1)
form implies the existence of a real distribution q with b+dd^c q>=0.
There is no d-closedness hypothesis on b. These are Lamari,AIF49(1999),
Proposition1.3 and Lemma3.3, printed267--268 and275--276,
https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf. The complete printed
separation proofs and local duality context have been separately read.
The paper's differently normalized dd^c is converted by rescaling q.

A distribution with positive complex Hessian has a unique locally integrable
genuine psh representative; local radial convolution decreases to it.
Genuine psh functions not identically minus infinity are locally integrable,
and the cone Psh intersect L1_loc is closed with relatively compact bounded
subsets. These are Demailly,CADG,I.4.17,I.4.20,I.5.8--5.9,
https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf.
Canonical representative proofs and the compactness proposition's printed
statement were read. The proposition's inherited subharmonic compactness
foundation is allowed; no full recursive certification is asserted. Global
normalization, a uniform L1 bound and every application are proof obligations.

For a CLOSED positive current of bidimension(p,p) on a complex manifold,
its geometric Lelong upperlevel sets{x:nu(T,x)>=c},c>0, are analytic sets of
dimension at most p. Lelong numbers are coordinate invariant, are unchanged
by adding a smooth current, and nu([smooth hypersurface],x)=1 on its smooth
locus. These are Demailly,CADG,III.5.9,III.5.11,III.8.5, at the same URL.
The complete printed III.5.11 proof and III.8.5 statement and proof were read;
III.8.4 is its explicitly imported Siu foundation, not a newly recursively
certified theorem. Do not apply Siu directly to the nonclosed current omega+dd^c q.

Elementary positive-current/matrix algebra, smooth local quadratic
corrections, local submean inequalities, compactness of a finite chart cover,
finite-dimensional overlap propagation, approximate identities, smooth
Hermitian metrics on Cartier line bundles, smooth distributional Stokes,
fiber integration and elementary one-variable optimization are allowed.
No conclusion A--D, global nonclosed mass monotonicity, singular-current
fiber restriction or determinant consequence from trace concentration is granted.


# Entire current author source

\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\newtheorem{lemma}{Lemma}
\theoremstyle{remark}\newtheorem{remark}{Remark}
\newcommand{\ddc}{dd^c}
\newcommand{\dc}{d^c}
\title{Divisor-free transverse concentration and limits of radial tests}
\author{}\date{October 8, 2026}
\begin{document}\maketitle
\noindent\textbf{Working draft.} Independent review and statement-only
reconstruction are pending. The lower-mass problem P11 remains open.
\begin{abstract}
We study smooth positive $\ddc$-closed complementary tests on compact
complex manifolds. Bounded transverse concentration along a local
hypersurface forces that hypersurface to lie in a global analytic
hypersurface. Thus the concentration constants diverge on a manifold
without divisors. Conversely a Cartier divisor agreeing with the chosen
hypersurface on the entire cutoff chart supplies a uniform bound through
actual regularized logarithmic potentials. On a primitive elliptic
threefold bundle, every test in a specified radial affine family has an
explicit bounded positive-root volume, including arbitrarily concentrated
radial coefficients. These conclusions isolate a limitation of radial
tests; they do not construct lower-mass collapse on a curve-free K3 bundle.
\end{abstract}

\section{Transverse concentration against every complementary test}
Use $\ddc=i\partial\bar\partial/(2\pi)$ and
$\dc=i(\bar\partial-\partial)/(4\pi)$. Let $X$ be a connected compact
complex manifold of dimension $n\geq2$, and let $\omega$ be a smooth
positive Hermitian form. Put
\[
 \mathcal T_\omega=\{\Theta\in C^\infty(X,\Lambda^{n-1,n-1}_{\mathbb R}):
 \Theta>0,\ \ddc\Theta=0,\ \int_X\omega\wedge\Theta=1\}.
\]
The inequality means strict positivity. This set is nonempty by
\cite[Proposition 1.3]{Lamari}; no closedness of $\omega$ is assumed.
Choose a coordinate polydisk with coordinates $(z,\zeta)$, where
$z\in\mathbb C^{n-1}$. Let $0\leq\chi\leq1$ be a smooth compactly
supported function of $z$, equal to one on a nonempty connected smaller
polydisk $U'$. Choose $p\in C_c^\infty(\mathbb C)$ nonnegative, positive for
$|\zeta|<1$ and zero for $|\zeta|\geq1$, with
\[
 \int_{\mathbb C}p(\zeta)\,\sigma_\zeta=1,\qquad
 \sigma_\zeta=\frac{i}{2\pi}d\zeta\wedge d\bar\zeta.
\]
For small $\delta>0$ extend the smooth semipositive form
\[
 B_\delta=\chi(z)\delta^{-2}p(\zeta/\delta)\sigma_\zeta
\]
by zero to $X$, and define
\[
 C_\delta=\sup_{\Theta\in\mathcal T_\omega}
                    \int_X B_\delta\wedge\Theta.
\]
Each $C_\delta$ is finite: $B_\delta\leq M_\delta\omega$ for a finite
constant $M_\delta$. All tests, including those varying in every variable,
are included.

\begin{theorem}\label{thm:concentration}
If $C_{\delta_j}$ is bounded along some $\delta_j\downarrow0$, there
is a global analytic hypersurface in $X$ containing
$U'\times\{\zeta=0\}$. In particular, if $X$ has no analytic
hypersurfaces, then $C_\delta\to\infty$ as $\delta\downarrow0$.
\end{theorem}
\begin{proof}
Suppose $C_{\delta_j}\leq M$, and choose $\kappa=1/(M+1)>0$.
Every smooth strictly positive $\ddc$-closed complementary form satisfies
\[
 \int_X(\omega-\kappa B_{\delta_j})\wedge\Theta
       \geq(1-\kappa M)\int_X\omega\wedge\Theta\geq0,
\]
after normalizing its positive degree. Lamari's criterion
\cite[Lemma 3.3]{Lamari} therefore supplies a real distribution $v_j$
with
\[
 \omega+\ddc v_j\geq\kappa B_{\delta_j}.
\]
The criterion concerns smooth real $(1,1)$ forms and does not require
$\omega-\kappa B_{\delta_j}$ to be closed. Adding a fixed sufficiently
positive quadratic in each coordinate ball gives the canonical genuine
psh representative of the distribution. Subtracting the quadratic gives
a genuine quasi-psh representative, and we normalize $\sup_Xv_j=0$.

Here is the needed compactness argument. Use a finite cover by inner
coordinate balls, with larger concentric balls still in their charts.
Fixed bounded quadratics correct the common Hessian lower bound. At a
maximum point in one inner ball, the submean inequality on a larger ball
bounds the integral of $-v_j$ on that inner ball. Each nonempty overlap
has fixed positive volume. An existing integral bound therefore gives a
point of the overlap where $v_j$ is uniformly bounded below; the submean
inequality in the next chart propagates its bound. The finite overlap
graph is connected. Taking the finitely many possible starting balls
into account gives a common global $L^1$ bound. Local psh compactness
\cite[I.5.8--5.9]{Demailly} and finite diagonal extraction now give
$v_j\to v$ in $L^1$ after a subsequence, with a nontrivial genuine
canonical $v$ and $\omega+\ddc v\geq0$.

The normalized transverse approximate identity gives, as currents,
\[
 B_{\delta_j}\longrightarrow\chi(z)[\zeta=0].
\]
Thus $\omega+\ddc v\geq\kappa[\zeta=0]$ where $\chi=1$.
In any chart add smooth $\rho$ with $\ddc\rho\geq\omega$.
The current $\ddc(v+\rho)$ is positive and \emph{closed}, and its
geometric Lelong number is at least $\kappa$ on the inner hypersurface.
Siu's analyticity theorem in the form
\cite[III.8.5]{Demailly} gives an analytic Lelong upperlevel set of
complex dimension at most $n-1$. Smooth changes of $\rho$ have zero
Lelong number, so these local upperlevel sets agree on overlaps and
form a global proper analytic set. It contains the inner hypersurface,
and therefore has an analytic hypersurface component containing it.
Indeed locally intersect with the connected smooth inner hypersurface:
a proper analytic subset cannot contain an open subset of it. The
hypersurface component meeting that open subset contains the whole inner
polydisk by the identity principle.

If $X$ has no analytic hypersurfaces, no bounded subsequence can exist.
Since $C_\delta\geq0$ is finite for each $\delta$, this is exactly the
asserted divergence.
\end{proof}

\begin{proposition}\label{prop:divisor-bound}
Suppose an effective Cartier divisor $D$ agrees with $\{\zeta=0\}$
with multiplicity one on a neighborhood of the entire cutoff chart.
Then $C_\delta$ is bounded uniformly for all sufficiently small
$\delta>0$.
\end{proposition}
\begin{proof}
Let $s_D$ be its canonical section. Choose a smooth Hermitian metric
$h$ on $\mathcal O(D)$ whose local frame in this chart has norm one
on a neighborhood of the cutoff support. Such a metric is obtained by
extending the prescribed local logarithm by a smooth cutoff. For
\[
 \psi_\delta=\log(|s_D|_h^2+\delta^2)
\]
one has $\ddc\psi_\delta\geq-C\omega$ globally, with $C\geq1$
independent of $\delta$. Off $D$, the chain rule writes its Hessian
as $-a_\delta\,\operatorname{curv}(h)$ plus a semipositive gradient
term, where $0\leq a_\delta\leq1$. The same lower bound holds at
$D$ by smoothness and continuity. Choose $0<\epsilon\leq1/(2C)$.
Then $\omega+\epsilon\ddc\psi_\delta\geq\omega/2$ everywhere.
On the flat-metric chart the exact local formula is
\[
 \ddc\psi_\delta=
    \frac{\delta^2}{(|\zeta|^2+\delta^2)^2}\sigma_\zeta
    \geq\frac{\delta^{-2}}4\sigma_\zeta\quad(|\zeta|\leq\delta).
\]
Writing $P=\|p\|_\infty>0$ and using $\chi\leq1$, it follows that
\[
 \omega+\epsilon\ddc\psi_\delta
                    \geq\frac{\epsilon}{4P}B_\delta
\]
throughout $X$. For any $\Theta\in\mathcal T_\omega$, smooth Stokes gives
\[
 1=\int_X(\omega+\epsilon\ddc\psi_\delta)\wedge\Theta
       \geq\frac{\epsilon}{4P}\int_XB_\delta\wedge\Theta.
\]
Hence $C_\delta\leq4P/\epsilon$, as claimed.
\end{proof}

\begin{remark}
The converse proposition requires a divisor agreeing on the entire
specified cutoff chart. The theorem's necessary global hypersurface
may have other branches elsewhere; no uniform bound at arbitrary
branch intersections is inferred. Neither assertion gives a rate of
divergence or a large positive-root volume of the concentrating tests.
\end{remark}

\section{The primitive elliptic-bundle radial family}
Keep the primitive elliptic bundle setting of original P11. Thus $(B,\eta)$
is a compact K\"ahler surface, $\eta\wedge c=0$, and
$X=L^\times/\langle w\mapsto qw\rangle$. Put
\[
 t=\log|w|^2,\quad \ddc t=\pi^*c,\quad T=2\log q,\quad
 A=\int_B\eta^2,\quad\beta=dt\wedge\dc t,\quad\omega=\eta+\beta.
\]
Suppress pullbacks of base forms. The derivatives of $t$ descend,
and functions of $t$ below are smooth $T$-periodic functions. The
original identities are
\[
 \beta^2=0,\quad d\beta=-dt\wedge c,\quad
 d(\omega^2)=0,\quad\int_X\eta^2\beta=TA,\quad
 V:=\int_X\omega^3=3TA.
\]
In particular $\omega^2/V\in\mathcal T_\omega$. In the divisor-free
K3 example specified in P11, Theorem~\ref{thm:concentration} applies
to every local transverse cutoff family.

Consider the following \emph{specified affine family}, for real smooth
periodic $a,g$:
\[
 \Gamma=a(t)\eta^2+g(t)\eta\beta.
\]
\begin{theorem}\label{thm:radial}
The form $\Gamma$ is strictly positive and $\ddc$-closed exactly
when $a$ is a positive constant and $g(t)>0$. In that case its positive
square root and root volume satisfy
\begin{gather*}
 \gamma=\sqrt a\,\eta+\frac{g(t)}{2\sqrt a}\beta,
 \qquad\gamma^2=\Gamma,\\
 D:=\int_X\omega\Gamma=TA(a+\bar g),\qquad
 R:=\int_X\gamma^3=\frac32TA\sqrt a\,\bar g,
 \qquad\bar g=T^{-1}\int_0^Tg(t)dt,\\
 R\leq\frac{D^{3/2}}{\sqrt V}.
\end{gather*}
Equality holds exactly when $\bar g=2a$; it does not require $g$ to
be pointwise constant. In particular every degree-one test in this
family has $R\leq1/\sqrt V$.
\end{theorem}
\begin{proof}
The term $g\eta\beta$ is closed: $dg\wedge\beta=0$ and
$\eta\wedge c=0$. Also
\[
 \ddc(a\eta^2)=a''\beta\eta^2,
\]
since $a'c\eta^2$ has excess base degree. Thus $\ddc\Gamma=0$
exactly when $a''=0$, which by periodicity means $a$ is constant.
In an adapted positive complex coframe, write $\eta=\sigma_1+\sigma_2$
and $\beta=\sigma_3$. The cofactor matrix of $\Gamma$ is
$\operatorname{diag}(g,g,2a)$, so strict positivity is exactly $a,g>0$.
The displayed $\gamma$ is positive and its square is $\Gamma$.
Direct multiplication gives
\[
 \omega\Gamma=(a+g)\eta^2\beta,\qquad
 \gamma^3=\tfrac32\sqrt a\,g\eta^2\beta.
\]
Fiber integration proves $D$ and $R$. For fixed $D>0$ set $s=D/(TA)$.
Then $0<a<s$, $\bar g=s-a$, and
$\sqrt a(s-a)$ has its unique maximum at $a=s/3$.
Substitution gives $R\leq D^{3/2}/\sqrt{3TA}$ and the equality condition.
\end{proof}

\section{The remaining lower-mass problem}
The concentration argument is an application of Lamari duality,
canonical psh compactness and Siu analyticity; these foundations retain
their attribution. All statements concern actual smooth complementary
tests and genuine canonical potentials. No prior verifier verdict or
finite computation is a mathematical premise.
The radial result covers only the displayed affine family; it supplies
no bound on all positive $\ddc$-closed tests. Large transverse pairings
alone do not imply divergent positive-root volume. No sequence of smooth
admissible potentials with masses tending to zero on the curve-free
K3 bundle has been obtained. Neither the full value of $v_-(\omega)$
there nor the proposed nonzero-real-Chern-class vanishing claim is
resolved by this paper. Original P11 remains open.

\begin{thebibliography}{9}
\bibitem{Lamari} A.~Lamari, \emph{Courants k\"ahl\'eriens et surfaces
compactes}, Ann.~Inst.~Fourier \textbf{49} (1999), 263--285,
Proposition 1.3 and Lemma 3.3.
\href{https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf}{Published primary text}.
\bibitem{Demailly} J.-P.~Demailly, \emph{Complex Analytic and Differential
Geometry}, I.5.8--5.9 and III.8.5.
\href{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf}{University-hosted primary text}.
\end{thebibliography}
\end{document}


# Entire earlier private unverified proof, its original narrower scope

# P11: divisor-free concentration and the limitation of radial complementary tests

Private root exploration; this is not an accepted theorem, paper or answer
to original P11. The actual original task and the preceding whole affine
closed-form repair classification were read. Its primitive-bundle setting,
balanced metric, and the stated absence of divisors in the particular K3
case are task background. The two observations below do not determine
the infimum over arbitrary bounded omega-psh potentials.

Use the original dd^c=i partial barpartial/(2pi). Write beta=dt wedge d^c t,
omega=eta+beta, T=2 log q, A=integral_B eta^2, V=3TA, and suppress base
pullbacks. Here eta c=0, d(beta)=-dt wedge c, beta^2=0, omega^2 is closed,
and integral_X eta^2 beta=TA. Functions of t mean smooth T-periodic
functions on the circle-valued global coordinate.

## 1. An all-test transverse concentration statement in the divisor-free case

Assume X has no analytic hypersurfaces, as the particular curve-free K3
example is stated to have in the original task. Fix a relatively compact
holomorphic coordinate polydisk with coordinates (x,y,zeta). Choose a
nonnegative smooth base cutoff chi(x,y), compactly supported there and
equal to one on a nonempty smaller product polydisk. Choose a smooth
probability p relative to sigma_zeta=i d zeta wedge dbar zeta/(2pi),
positive on the unit disk and zero outside it. For small delta put

    B_delta=chi(x,y) delta^-2 p(zeta/delta) sigma_zeta,

with smooth extension by zero. Define C_delta as the supremum of
integral_X B_delta Theta over EVERY globally smooth strictly positive
dd^c-closed (2,2) form Theta of integral_X omega Theta=1.

This family is nonempty: omega^2/V is positive, closed, and has degree
one. For fixed delta, a finite pointwise bound B_delta<=M_delta omega
proves C_delta<infinity. In fact

    C_delta -> infinity as delta -> 0.

Here is the complete concentration argument relative to the separately
primary-assessed Lamari criterion, canonical representative/local L1
compactness and Siu analyticity foundations. Suppose C_delta_j<=M along
delta_j->0. Taking kappa=1/(M+1), every positive dd^c-closed test satisfies

    integral (omega-kappa B_delta_j) Theta
      >=(1-kappa M) integral omega Theta>0.

Lamari Lemma3.3, in arbitrary compact complex dimension and without a
closedness hypothesis on the (1,1) background, gives a distribution v_j
with omega+dd^c v_j>=kappa B_delta_j. Local quadratic corrections give
canonical genuine quasi-psh representatives. Normalize sup v_j=0.

For completeness, global normalized L1 compactness follows from local
submean propagation. Cover X by inner coordinate balls of radii r_i,
whose outer balls of radii 4r_i lie in the same charts. Choose bounded
nonnegative quadratics rho_i making v_j+rho_i psh. At a maximum point
of v_j in an inner ball, submean on the radius2r_i ball bounds its
integral of -v_j on that inner ball. Each fixed nonempty overlap has
positive volume, so an existing L1 bound supplies a point on the overlap
with v_j bounded below uniformly. Submean in the next chart gives its
inner-ball bound. The finite overlap graph is connected; propagation
and finitely many possible starting balls give one global bound.
The permitted local L1 compactness and finite diagonal extraction give
a nontrivial canonical limit v with dd^c v>=-omega.

The ordinary normalized approximate identity gives
B_delta_j -> chi [zeta=0] as currents. Therefore, wherever chi=1,

    omega+dd^c v>=kappa [zeta=0].

Add on every coordinate ball a smooth rho with dd^c rho>=omega.
The positive CLOSED current dd^c(v+rho) has geometric Lelong number
at least kappa along the indicated local divisor. Smooth changes of
rho alter no geometric Lelong number: their trace mass is O(r^6)
against the r^4 denominator. Siu's theorem for bidimension(2,2)
therefore gives a global proper analytic upperlevel set Z of dimension
at most two, containing an open segment of that complex surface.
Consequently Z has a two-dimensional irreducible component, an analytic
hypersurface in X. This contradicts the explicit divisor-free hypothesis.
No local restriction of a singular current to an elliptic fiber is used.
Thus every bounded subsequence is excluded and C_delta diverges.

The foundations have these exact primary locators: Lamari, AIF49(1999),
Lemma3.3 printed275--276, https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf;
Demailly, Complex Analytic and Differential Geometry,21June2012,
I.5.8--5.9 printed40 and III.8.5 printed174,
https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf.
Their exact relevant proofs were separately read in the P07 source
assessment; their cited foundations were not recursively certified.
This is a new application judgment, not an import of a P07 verdict.
For Demailly's twice-normalized operator the equivalent potential-current
upperlevel is twice ours; we consistently use geometric current numbers.
The absence of hypersurfaces in the specified K3 total space is a task
hypothesis here, not a new primary theorem proved by this note.

## 2. Every radial complementary test in a specified affine family

For arbitrary smooth T-periodic real functions a(t),g(t) put

    Gamma=a(t) eta^2+g(t) eta beta.

The second term is CLOSED for every g, since dg is proportional to dt
and eta c=0. Moreover dd^c(a eta^2)=a'' beta eta^2: the a' c eta^2
term has excess base degree. Since beta eta^2 is strictly positive,
dd^c Gamma=0 if and only if a''=0, equivalently a is constant.
At a point choose a positive adapted complex coframe with
eta=sigma1+sigma2 and beta=sigma3. The cofactor matrix of Gamma is
diag(g,g,2a). Thus Gamma is strictly positive if and only if a>0,g>0.

For constant a>0 and smooth g>0 the unique positive square root is

    gamma=sqrt(a) eta+[g(t)/(2 sqrt(a))] beta,
    gamma^2=Gamma,
    gamma^3=(3/2) sqrt(a) g(t) eta^2 beta.

Let gbar=T^-1 integral_0^T g(t) dt. Fiber integration gives exactly

    D=integral omega Gamma=TA(a+gbar),
    R=integral Gamma^(3/2)=(3/2)TA sqrt(a) gbar.

Holding a and gbar fixed leaves R unchanged by arbitrary concentration
of g. For fixed D>0 set s=D/(TA). Then 0<a<s, gbar=s-a, and elementary
differentiation of sqrt(a)(s-a) gives its unique maximum at a=s/3.
Consequently EVERY such positive dd^c-closed radial test satisfies

    R <= D^(3/2)/sqrt(3TA)=D^(3/2)/sqrt(V).

Equality holds if and only if gbar=2a; it imposes no pointwise constancy
of g. For degree-one tests R is bounded by 1/sqrt(V). Therefore this
entire specified radial family cannot supply the bounded-degree,
diverging-positive-root-volume sequence used in the known zero-mass
construction. This is an exact bound for that family, not a bound for
all dd^c-closed tests, nor a positive lower-mass theorem for omega.

The first observation supplies all-test trace concentration in the
divisor-free K3 case. The second shows why the immediately available
closed radial complementary family cannot finish it. No divergence
rate for C_delta, no suitable nonradial complementary forms, and no
smooth mass-collapse sequence have been proved here. Original P11 and
the nonzero-real-Chern-class vanishing claim remain unresolved.


# Exact primary application judgments, not mathematical acceptance

{
  "recorded_at_utc": "2026-10-08T13:14:24.525965+00:00",
  "label": "P11-divisor-free-concentration-and-radial-tests-20261008",
  "source_sha256": "f25cbc9efdda3feee5d56637aee54772b30d36111af5879eab9dc2758c4f9126",
  "original_task_sha256": "3a5653b4ff85df0dc3fe344471302d66fe51acab59c134ffe48ee98fed560e74",
  "entire_current_source_and_prior_private_note_actually_root_read": true,
  "every_quoted_primary_range_actually_root_read_without_truncation": true,
  "applications": [
    {
      "foundation": "Lamari Proposition1.3",
      "application": "All-test cone nonempty in arbitrary compact dimension; normalize by the strictly positive omega degree. No balancedness or background closedness needed."
    },
    {
      "foundation": "Lamari Lemma3.3",
      "application": "The real smooth background is omega-kappa B_delta, not closed. Uniform all-test C_delta bound gives strictly positive pairing on the entire smooth positive dd^c-closed complementary cone. Canonical distribution potentials must subsequently be established."
    },
    {
      "foundation": "Demailly I.4.17,I.4.20,I.5.8--5.9",
      "application": "Positive local smooth quadratic corrections produce genuine distribution representatives; sup normalization plus explicit finite overlap submean propagation proves a common L1 bound. The compactness proposition is used only after that bound. Its inherited subharmonic compactness theorem is permitted, not recursively certified."
    },
    {
      "foundation": "Demailly III.5.9,III.5.11,III.8.5",
      "application": "Apply only to local CLOSED positive dd^c(v+rho), with dd^c rho>=omega. The current limit dominates kappa[local smooth hypersurface] where chi=1. Geometric Lelong numbers are invariant under smooth differences and glue; p=n-1 gives a proper analytic global upperlevel set and a hypersurface component. III.8.4 remains an imported Siu foundation, not a claimed new recursive certification."
    },
    {
      "foundation": "Elementary Cartier smoothing and smooth Stokes",
      "application": "Require D to equal the multiplicity-one local divisor on the ENTIRE fixed chart. Prescribe the section frame metric flat near the cutoff support. The global smooth log(|s_D|^2+delta^2) has uniform lower Hessian; its transverse Hessian dominates the actual B_delta, and every dd^c-closed test pairs with dd^c psi to zero. No branch-intersection converse."
    },
    {
      "foundation": "Original P11 conventions and elementary matrix/fiber calculation",
      "application": "Classify only Gamma=a(t)eta^2+g(t)eta beta. Primitive eta c=0 kills d(g eta beta); dd^c Gamma=a-double-prime beta eta^2 forces constant a. Cofactor diag(g,g,2a) proves positivity; exact square root and fiber integration yield the sharp fixed-degree maximum, not an all-test lower-mass claim."
    }
  ],
  "primaries": [
    {
      "path": "inputs/primary/Lamari-Kaehler-currents-1999.txt",
      "text_sha256": "1223aa9e5f091d0ef2e99a5a53a5091625e998c8da6d520dcd13331d5be3d3e3",
      "root_read_ranges": [
        [
          100,
          245
        ],
        [
          530,
          577
        ]
      ]
    },
    {
      "path": "inputs/primary/Demailly-author-hosted-S11-full.txt",
      "text_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
      "root_read_ranges": [
        [
          1790,
          1860
        ],
        [
          2055,
          2190
        ],
        [
          8675,
          8745
        ],
        [
          9480,
          9555
        ]
      ]
    }
  ],
  "every_cited_foundation_recursively_certified": false,
  "excluded_evidence": "Historical native stdout accidentally encountered in a broad P07 search is not a premise or a source-read substitute. The exact primary ranges here were independently actually read. Current S18 native stdout and private artifacts have not been read.",
  "independent_review_pending": true,
  "mathematical_acceptance": false,
  "original_P11_completed": false,
  "published": false
}


# Complete primary context: inputs/primary/Lamari-Kaehler-currents-1999.txt, lines 100--245

utile de connaître sur la cohomologie des surfaces complexes compactes.
       Les méthodes présentées ici nous ont aussi permis de caractériser le
cône kàhlérien d'une surface kàhlérienne compacte : une classe de cohomo-
logie réelle a de type (1,1) est kàhlérienne si et seulement si a 2 > 0, a-£J > 0
pour toute courbe E de self-intersection négative, et a-a; > 0 pour au moins
une classe kàhlérienne uj. Ce résultat fera l'objet d'une publication séparée.
             COURANTS KÀHLÉRIENS ET SURFACES COMPACTES                   265


                  1. Courants positifs et dualité.

     Soit X une variété complexe de dimension n.
     On note ^p'9 le faisceau des germes de formes C°° de bidegré (p,ç),
Vpq le faisceau des germes de courants de bidimension (p,ç).

      Si U est un ouvert de X, Pp g (U) est le dual topologique de
Fc^f^' 9 ). Un courant de bidimension (p,q) est de bidegré (n— p,n— q)
et nous noterons P^'5 := V^-r^n-s' Les espaces de formes seront munis de
la topologie C00 et les espaces de courants de la topologie faible.



                         1.1. Courants positifs.

      DÉFINITION 1.1. — Soit F e ^p(U). T est un courant positif si
T A ia\ A ~a\ A • • • A ta? A a? est une mesure positive, pour tout choix de
ai,...,ap dânsE^ÇU).

     Si a est une (p, 0)-forme, la (p,p)-forme uj = ip a A a est positive.
     Les courants positifs sont réels à coefficients mesures.
       On suppose X munie d'une métrique hermitienne et l'on note '0 la
(l,l)-forme positive associée.
     L'ensemble Pp(X) des courants positifs de bidimension (p,p) est un
cône convexe faiblement fermé dans P (X).
      Soit Cp(X) ={T ç Pp{X) \ (^,T) == 1}. Si X est compacte, Cp (X)
est un convexe compact pour la topologie faible des courants ([H77]).
     Nous ne nous intéresserons qu'aux formes et courants de bidegré ou
de bidimension (1,1).
      Une forme a; de bidegré (1,1) (resp. (n—l,n—l)) est strictement
positive si et seulement si (ù;,T) > 0 pour tout courant T ç C\ (resp.
T e C.-i).
    L'ensemble U des formes strictement positives de bidegré (1,1) (resp.
(n—l.n—1)) est un cône convexe ouvert dans E^ÇX) (resp. £^~l'n~l(X)).
266                               AHCÈNE LAMARI


                     1.2. Groupes de cohomologie.

    Pour l'étude des classes de courants d-fermés ou dc^-fermés ("pluri-
harmoniques"), nous serons amenés à utiliser les groupes d'Aeppli :
                    .1,1^ _ {TçV^l(X)\dT^Q}
                    ^R \^)               ^^cT)iQ(Y\
                                         dd^ÇX)
et
          ..,-i,,-i.. __         {^e^-l-n-l{x)\ddcu;=o}
          ^R        ^ ) - 7——_     n-i,n-i—————————————————
                           {o; e ^-^-'(X) 1 3(3^ = 0(3 + 9/3}

    Le faisceau 'HK des germes de fonctions pluriharmoniques réelles
admet deux résolutions fines commençant par
                                            1
               o _ u^ - ^ ^ 4'                           -^ ^
                        [ id        [j            [ j            [ j
                                         < c       1 1
               U --^^ ^
               n      n-/ R --^^ ^D'O
                                    ^     ^
                                         ———>   D'
                                                U^'      -^
                                                         ———>   T)^
                                                                i^^

où j est l'injection des espaces de formes dans les espaces de courants.
      On en déduit que A^'^X) ^ ff^X,?^) et que l'on peut faire le
calcul avec les (1, l)-formes d-fermées.
      On peut démontrer que V^"1'71"1^) peut également se calculer à
l'aide des courants.


                  1.3. Sous-espaces fermés et dualité.

       Si X est compacte, ^(JC,^) et IÇ''1'71"1^) sont de dimension
finie et les sous-espaces suivants sont fermés dans leurs espaces respectifs :
                               dd^WcfR 1 ' 1 ^),
                           dd^WcV^W^
      B^(X) ={Tç V^^ÇX) | 35 e îy71-1^-2^), T = 9S 4- QS},
et
Bi°°i(X) = {T ç ^ n - l ' n - l (X) | 35 € f71-1'71-2^) tel que T = 95+95}.

      Pour Bi^i(X), la démonstration se trouve dans ([HL83], p. 174). Pour
les autres sous-espaces, la démonstration se fait de manière analogue en
utilisant la finitude de groupes de Dolbeault et de De Rham convenables.
           COURANTS KÀHLÉRIENS ET SURFACES COMPACTES                  267


     On en déduit une dualité (algébrique et topologique)
                       H^x^y ^v^-^-^x).
     DÉFINITION 1.2. — Un courant T de bidimension (1,1) est com-
posante d'un bord s'il existe S e /Dfn~l^~2(X) tel que T = 9S + OS.

     Le courant T de la définition est la composante de bidegré (n—1, n—1)
du courant d(S + S). C'est un élément de B^{X).
      On remarquera qu'une (1, l)-forme réelle a est d-fermée si et seule-
ment elle est nulle sur B^i(X) (en tant que forme linéaire continue sur
l'espace des courants de bidimension (1,^)).
      De même, une (n—l,n—l)-forme f3 est dcF-fermée si et seulement si
elle est nulle sur dd^^X).
     La dualité précédente sera utilisée sous l'une des deux formes sui-
vantes :
     (1) Soit T un courant réel de bidegré (1,1).
      Si (r,uj) = 0 pour toute (n-l,n-l)-forme réelle dd° -fermée uj, il
existe \ ç ^'â(X) tel que r = dd°\.
     Si T est (7°°, il en sera de même de \.

     (2) Soit T un courant réel de bidegré (n-l.n-1).
     Si (a,T) = 0 pour toute (l,l)-forme réelle d-fermée a, il existe
S G P771-1'71-2^) tei que T = 9S + 9S.
     Si T est G00, on peut choisir 5' de classe C°°.


                           1.4. Applications.

     La proposition suivante sera utilisée plus loin.

       PROPOSITION 1.3. — Soit X une variété complexe compacte de
dimension n. Il existe sur X des (n-l.n-l) -formes strictement positives
dd° -fermées.

      Démonstration. — C1 = Cn-i est convexe faiblement compact dans
V^ÇX). C1 H dd^'^X) = 0 car T = dd^ > 0 implique r = 0 (^ est
plurisousharmonique donc constante sur X).
268                            AHCÈNE LAMARI


     Le théorème de séparation de Hahn-Banach permet de trouver une
forme f^ de bidegré (n—l,n—l) strictement positive sur C1 et nulle sur
dd^V'^X).

      Une telle forme î7 est dcF-fermée et strictement positive.        D

      Remarque. — D'après Michelsohn ([M83]), toute (n—l,n—l)-forme
Q, strictement positive peut s'écrire de manière unique sous la forme


# Complete primary context: inputs/primary/Lamari-Kaehler-currents-1999.txt, lines 530--577

     L'ensemble U des (n—l,n—l)-formes strictement positives est un
ouvert convexe de f^"1'71"1^). Notons E l'ensemble des (n—l,n—In-
formes réelles dd0-fermées.
      L'intersection V = U F} E est l'ensemble des formes strictement
positives dc^-fermées. Définissons A = {uj ç V \ (^,c<;) = 1} et K =
adhérence faible de A dans P^"1'71"1^).
      L'ensemble K est convexe, faiblement compact.
     D'après Harvey-Lawson [HL83], Bi,i := [T e yn-i^n-i [ ^s,T =
9 S + 9S} est faiblement fermé dans P^"'1'71'"1^).
           COURANTS KÀHLÉRIENS ET SURFACES COMPACTES                          275


    La condition (c) implique KÇ}B\^ = 0. D'après le théorème de Hahn-
Banach, il existe (3 e S^W telle que (3 \^> 0 et f3 |^ =0.
     La condition sur B^i équivaut à d/3 = 0.
     La compacité de K et la condition f3 \^> 0 impliquent (/?, T) > C > 0
pour tout T ç K.
     Si ù; (E Y, ^1(^^) e A. D'où (/3,o;) > C(^,uj). On prend a == /3/G.

     (b) => (a) :
     Cette implication résulte du lemme suivant appliqué à 0 := a — '0.

     LEMME 3.3. — Soit 6 une (1,1) -forme. Si (0,c^) > 0 pour toute
(n—l,n—l) -forme positive dd°-fermée a;, il existe \ ç. T>^(X) tel que
0 + dd°\ >_ 0 (au sens des courants).

     Démonstration du lemme. — L'ensemble V est un ouvert convexe
de E. Comme 6 définit une forme linéaire sur £', 0 y> 0 implique

      (1) ou bien il existe UJQ € V telle que (O^ujo) = 0.
     Dans ce cas 0 \
                   1 Ht
                        — 0.
      En effet, soit a une (n—l,n—l)-forme réelle dc^-fermée. Pour t C R,
soit o;t = (1 — t)ujQ + ta et /(t) = (O^t)' f est une fonction affine de t.
Pour t proche de zéro, o^ €V, car Y est ouvert. Il existe donc e > 0 tel que
f(e) >, 0 et f(—e) >: 0. Comme /(O) = ÇO^o) = 0, ceci implique que / est
identiquement nulle sur M, donc (0,a) = /(l) = 0.
     Puisque 0 \^= 0, il existe \ e V^W tel ^ ° = -dd0^. Donc
0 + dd^ = 0.

      (2) ou bien 0 \y> 0.
      Soient G := {uj G y1'71-1^) | (<9,a;) = 0} et F = G H £'. Le
sous-espace -F est un hyperplan fermé de E.
      Nous avons y n I ^ ^ ^ r i J S ' n G ^ y n G ^ O . c a r ^ e s t strictement
positive sur V.
     D'après le théorème de Hahn-Banach, nous pouvons séparer U et F


# Complete primary context: inputs/primary/Demailly-author-hosted-S11-full.txt, lines 1790--1860

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


# Complete primary context: inputs/primary/Demailly-author-hosted-S11-full.txt, lines 2055--2190

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


# Complete primary context: inputs/primary/Demailly-author-hosted-S11-full.txt, lines 8675--8745

dition and let (Ck )k⩾1 be the irreducible components of the point set intersection |Z1 | ∩
. . . ∩ |Zq |. Then there exist integers mk > 0 such that
                                                         X
                                 [Z1 ] ∧ . . . ∧ [Zq ] =   mk [Ck ].

The integer mk is called the multiplicity of intersection of Z1 , . . . , Zq along the compo-
nent Ck .
                   § 5. Generalized Lelong Numbers                                       157

                                                                    S
Proof. The wedge product has bidegree (q, q) and support in C = Ck where codim C =
q, so it must be a sum as above with mk ∈ R+ . We check by induction on q that mk is
a positive integer. If we denote by A some irreducible component of |Z1 | ∩ . . . ∩ |Zq−1 |,
we need only check that [A] ∧ [Zq ] is an integral analytic cycle of codimension q with
positive coefficients on each component Ck of the intersection. However [A] ∧ [Zq ] =
ddc (log |fq | [A]). First suppose that no component of A ∩ fq−1 (0) is contained in the
singular part AsingP  . Then the Lelong-Poincaré equation applied on Areg shows that
   c
dd (log |fq | [A]) =    mk [Ck ] on X r Asing , where mk is the vanishing order of fq along
Ck in Areg . Since C ∩ Asing has codimension q + 1 at least, the equality must hold on
X. In general, we replace fq by fq − ε so that the divisor of fq − ε has no component
contained in Asing . Then ddc (log |fq − ε| [A]) is an integral codimension q cycle with
positive multiplicities on each component of A ∩ fq−1 (ε) and we conclude by letting ε
tend to zero.                                                                            


§ 5. Generalized Lelong Numbers
    The concepts we are going to study mostly concern the behaviour of currents or
plurisubharmonic functions in a neighborhood of a point at which we have for instance
a logarithmic pole. Since the interesting applications are local, we assume from now on
(unless otherwise stated) that X is a Stein manifold, i.e. that X has a strictly plurisubhar-
monic exhaustion function. Let ϕ : X −→ [−∞, +∞[ be a continuous plurisubharmonic
function (in general ϕ may have −∞ poles, our continuity assumption means that eϕ is
continuous). The sets

(5.1)                           S(r) = {x ∈ X ; ϕ(x) = r},
(5.1′ )                         B(r) = {x ∈ X ; ϕ(x) < r},
(5.1′′ )                        B(r) = {x ∈ X ; ϕ(x) ⩽ r}

will be called pseudo-spheres and pseudo-balls associated with ϕ. Note that B(r) is not
necessarily equal to the closure of B(r), but this is often true in concrete situations. The
most simple example we have in mind is the case of the function ϕ(z) = log |z − a| on an
open subset X ⊂ Cn ; in this case B(r) is the euclidean ball of center a and radius er ;
moreover, the forms

                    1 c 2ϕ    i ′ ′′ 2                   i ′ ′′
(5.2)                 dd e =    d d |z| ,      ddc ϕ =     d d log |z − a|
                    2        2π                          π

can be interpreted respectively as the flat hermitian metric on Cn and as the pull-back
over Cn of the Fubini-Study metric of Pn−1 , translated by a.

(5.3) Definition. We say that ϕ is semi-exhaustive if there exists a real number R such
that B(R) ⊂⊂ X. Similarly, ϕ is said to be semi-exhaustive on a closed subset A ⊂ X if
there exists R such that A ∩ B(R) ⊂⊂ X.

   We are interested especially in the set of poles S(−∞) = {ϕ = −∞} and in the
behaviour of ϕ near S(−∞). Let T be a closed positive current of bidimension (p, p) on
X. Assume that ϕ is semi-exhaustive on Supp T and that B(R) ∩ Supp T ⊂⊂ X. Then
158                             Chapter III. Positive Currents and Lelong Numbers

P = S(−∞) ∩ SuppT is compact and the results of §2 show that the measure T ∧ (ddc ϕ)p
is well defined. Following [Demailly 1982b, 1987a], we introduce:

(5.4) Definition. If ϕ is semi-exhaustive on Supp T and if R is such that B(R) ∩
Supp T ⊂⊂ X, we set for all r ∈ ] − ∞, R[
                              Z
                 ν(T, ϕ, r) =        T ∧ (ddc ϕ)p ,
                                B(r)


# Complete primary context: inputs/primary/Demailly-author-hosted-S11-full.txt, lines 9480--9555

Here (ddc log |z|)p is a positive (p, p)-form coming from Pn−1 , hence it has zero contraction
in the radial direction, while the contraction of the form (ddc log |z|)p−1 ∧ d log |z| ∧
dc log |z| by the radial vector field is (ddc log |z|)p−1 . This shows easily that α(z) ⩾ 0 if
and only if u, v ⩾ 0. Next, the closedness condition dα = 0 gives u′ − v = 0. Thus u is
increasing and we define a convex increasing function χ by χ′ = u1/p . Then v = u′ =
pχ′p−1 χ′′ and                                             p
                                    α(z) = ddc χ(log |z|) .
If α is invariant by homotheties, the functions u and v must be constant, thus v = 0 and
α = λ(ddc log |z|)p .                                                                  

(7.11) Corollary (Crofton’s formula). Let dv be the unique U (n)-invariant measure of
mass 1 on the Grassmannian G(p, n) of p-dimensional subspaces in Cn . Then
                             Z
                                           [S] dv(S) = (ddc log |z|)n−p .
                                S∈G(p,n)



Proof. The left hand integral is a closed positive bidegree (n − p, n − p) current which is
invariant by U (n) and by homotheties. By Lemma 7.10, this current must coincide with
the form λ(ddc log |z|)n−p for some λ ⩾ R0. The coefficient λ is the Lelong number at 0.
As ν([S], 0) = 1 for every S, we get λ = G(p,n) dv(S) = 1.                               

    We now recall a few basic facts of slicing theory; see [Federer 1969] for details. Let
σ : M → M ′ be a submersion of smooth differentiable manifolds and let Θ be a locally
flat current on M , that is a current which can be written locally as Θ = U + dV where
                § 7. Comparison Theorems for Lelong Numbers                                  171

U , V have locally integrable coefficients. It can be shown that every current Θ such
that both Θ and dΘ have measure coefficients is locally flat; in particular, closed positive
currents are locally flats. Then, for almost every x′ ∈ M ′ , there is a well defined slice
Θx′ , which is the current on the fiber σ −1 (x′ ) defined by

                                 Θx′ = U↾σ−1 (x′ ) + dV↾σ−1 (x′ ) .

The restrictions of U , V to the fibers exist for almost all x′ by the Fubini theorem. It is
easy to show by a regularization Θε = Θ ⋆ ρε that the slices of a closed positive current
are again closed and positive: in fact Uε,x′ and Vε,x′ converge to Ux′ and Vx′ in L1loc , thus
Θε,x′ converges weakly to Θx′ for almost every x′ . This kind of slicing can be referred
to as parallel slicing (if we think of σ as being a projection map). The kind of slicing we
need (where the slices are taken over linear subspaces passing through a given point) is
of a slightly different nature and is called concurrent slicing.
   The possibility of concurrent slicing is proved as follows. Let T be a closed positive
current of bidimension (p, p) in the ball B(0, R) ⊂ Cn . Let
                                
                          Y = (x, S) ∈ Cn × G(q, n) ; x ∈ S

be the total space of the tautological rank q vector bundle over the Grassmannian G(q, n),
equipped with the obvious projections

                            σ : Y −→ G(q, n),            π : Y −→ Cn .

We set YR = π −1 (B(0, R)) and YR⋆ = π −1 (B(0, R) r {0}). The restriction π0 of π
to YR⋆ is a submersion onto B(0, R) r {0}, so we have a well defined pull-back π0⋆ T
over YR⋆ . We would like to extend it as a pull-back π ⋆ T over YR , so as to define slices
T↾S = (π ⋆ T )↾σ−1 (S) ; of course, these slices can be non zero only if the dimension of S is
at least equal to the degree of T , i.e. if q ⩾ n − p. We first claim that π0⋆ T has locally
finite mass near the zero section π −1 (0) of σ. In fact let ωG be a unitary invariant Kähler
metric over G(q, n) and let β = ddc |z|2 in Cn . Then we get a Kähler metric on Y defined
by ωY = σ ⋆ ωG + π ⋆ β. If N = (q − 1)(n − q) is the dimension of the fibers of π, the
projection formula π⋆ (u ∧ π ⋆ v) = (π⋆ u) ∧ v gives

                             N+p
                                     X N + p                      N+p−k
                        π ⋆ ωY   =                   β k ∧ π⋆ (σ ⋆ ωG     ).
                                               k
                                   1⩽k⩽p

              N+p−k
Here π⋆ (σ ⋆ ωG       ) is a unitary and homothety invariant (p−k, p−k) closed positive form
                             N+p−k
on C r {0}, so π⋆ (σ ⋆ ωG
    n
                                   ) is proportional to (ddc log |z|)p−k . With some constants
λk > 0, we thus get



# Entire immutable original-task public report, all16premises18bindings

{
  "verdict": "INCONCLUSIVE",
  "report": "A–D are established as restricted results, with the minor clarifications below. Neither supplied proof determines the infimum for the curve-free K3 or decides universal vanishing for nonzero real Chern class. The original completion criteria therefore remain unmet; no concrete mathematical defect in the restricted results warrants FAIL.\n\nFor A, the test cone is nonempty, and B_delta≤M_delta omega proves finiteness. A bounded concentration subsequence gives strictly positive pairing of omega−kappa B_delta with every complementary test, so Lamari applies without background closedness. Local quadratic corrections produce canonical representatives that agree pointwise on overlaps by uniqueness. After sup normalization, the compactness argument works explicitly with inner balls of radius r and outer balls of radius 4r: a radius-2r ball centered at a maximum contains the inner ball, and submean bounds its integral of −v_j. A fixed overlap of positive volume supplies a uniformly bounded-below point for the next chart. Connectedness of the finite overlap graph propagates a global L¹ bound. Local compactness then yields a genuine, locally integrable limit.\n\nThe normalized approximate identity converges to chi[ζ=0], preserving the current inequality. Adding rho with dd^c rho≥omega produces local CLOSED positive currents. Smooth differences contribute O(r²) to normalized trace masses, so their Lelong numbers agree. Their analytic upperlevel sets consequently glue globally; dimension at most n−1 makes the resulting set proper. Its finitely many global components cover the connected local hypersurface, so one contains a nonempty open portion and hence the entire inner hypersurface by the identity principle. Excluding every bounded subsequence proves the asserted divergence. This also verifies the earlier private concentration proof.\n\nFor B, the divisor hypothesis supplies a holomorphic frame with s_D=ζ throughout the required chart. Prescribing its metric near the compact cutoff support extends smoothly globally. The actual functions log(|s_D|²_h+delta²) are smooth. Off the divisor their Hessian is a bounded curvature contribution plus a semipositive term, giving a uniform lower bound; continuity extends it across the divisor. Choosing epsilon≤1/(2C) ensures global positivity. The stated transverse Hessian formula and bound on |ζ|≤delta dominate B_delta. Smooth Stokes annihilates its potential term against every dd^c-closed test, giving C_delta≤4||p||∞/epsilon. No branch-intersection extension is used.\n\nFor C, d(g eta beta)=0 follows from primitiveness, and dd^c Gamma=a'' beta eta². Periodicity therefore forces constant a. The complementary matrix diag(g,g,2a) establishes positivity exactly when a,g>0. Direct squaring and multiplication verify the displayed positive root, degree and volume formulas. Fiber integration uses d^c t=dθ/(2π) on each fiber. At fixed s=D/(TA), maximizing sqrt(a)(s−a) gives a=s/3, exactly R≤D^(3/2)/sqrt(V), with equality precisely when gbar=2a. Nonconstant g is allowed. The earlier private radial proof gives the same calculation.\n\nD correctly limits these conclusions: divergent transverse pairings supply no determinant or positive-root-volume divergence, and C controls only its displayed family. No smooth admissible collapse sequence, full K3 lower bound, or counterexample to universal vanishing is supplied. The zero-class value 3TA is expressly granted by the task.\n\nI independently opened and checked the relevant statements and printed arguments in [Lamari](https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf) and [Demailly](https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf); prior verification records were not evidence. The author-hosted Demailly URL failed, so I used the supplied university-hosted copy. Harmless corrections: coordinate invariance is III.7.2; III.8.5 is a corollary; and the component step must say 'contains an open portion,' since merely meeting it is insufficient. Passage index −1 records task-granted background, excluded from the external-premise list.",
  "passages": [
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/0",
      "statement": "On every compact complex n-fold, n≥2, there exists a smooth strictly positive real (n−1,n−1) form Θ satisfying dd^cΘ=0 (Lamari, Proposition 1.3).",
      "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
      "quote": "Il existe sur X des (n-l.n-l) -formes strictement positives",
      "premise": 0
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/1",
      "statement": "Let X be a compact complex n-fold and b a smooth real (1,1) form. If ∫X b∧Θ≥0 for every smooth strictly positive real dd^c-closed (n−1,n−1) form Θ, there exists a real distribution q with b+dd^c q≥0. No d-closedness hypothesis on b is required (Lamari, Lemma 3.3).",
      "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
      "quote": "0 + dd°\\ >_ 0 (au sens des courants).",
      "premise": 1
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/2",
      "statement": "On an open Ω⊂C^n, a real distribution with positive complex Hessian has a unique locally integrable canonical plurisubharmonic representative; convolution with rescaled nonnegative smooth radial probability kernels decreases to it as the scale tends to zero (Demailly I.4.20, I.5.5, I.5.8).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "u ∈ Psh(Ω) locally integrable",
      "premise": 2
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/3",
      "statement": "On connected Ω⊂C^n, a plurisubharmonic function not identically −∞ is locally integrable; Psh(Ω)∩L¹_loc(Ω) is closed in L¹_loc(Ω), and every L¹_loc-bounded subset is relatively compact (Demailly I.4.17, I.5.9).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "every bounded subset is relatively compact.",
      "premise": 3
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/4",
      "statement": "Geometric Lelong numbers of closed positive currents are coordinate invariant, and ν([H],x)=1 at every smooth point of an analytic hypersurface H (Demailly III.5.9, III.7.2).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "independent of the choice",
      "premise": 4
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/5",
      "statement": "Geometric Lelong numbers of closed positive currents are coordinate invariant, and ν([H],x)=1 at every smooth point of an analytic hypersurface H (Demailly III.5.9, III.7.2).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "1 when",
      "premise": 4
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/6",
      "statement": "For a closed positive current S of bidimension (p,p) on a complex manifold, every upperlevel set {x:ν(S,x)≥c}, c>0, is analytic of dimension at most p (Demailly III.8.5).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "analytic subsets of dimension",
      "premise": 5
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/7",
      "statement": "An analytic subset of a complex manifold is a locally finite union of global irreducible analytic components (Demailly II.5.3).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "locally finite family",
      "premise": 6
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/8",
      "statement": "On a compact complex n-fold there exists a smooth strictly positive real (n−1,n−1) form killed by dd^c (Lamari, Proposition 1.3).",
      "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
      "quote": "dd° -fermées.",
      "premise": 7
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/9",
      "statement": "For a compact complex n-fold X and smooth real (1,1) form b, nonnegative pairing with every smooth strictly positive real dd^c-closed (n−1,n−1) form implies the existence of a real distribution q with b+dd^c q≥0, without any d-closedness hypothesis on b (Lamari, Lemma 3.3).",
      "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
      "quote": "formes strictement positives",
      "premise": 8
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/10",
      "statement": "On a compact complex n-fold, the Lamari criterion applies to an arbitrary smooth real (1,1) form b, including a nonclosed one: strictly positive pairing with every smooth strictly positive real dd^c-closed complementary form yields a real distribution q such that b+dd^c q≥0 (Lamari, Lemma 3.3).",
      "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
      "quote": "AT est positif.",
      "premise": 9
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/11",
      "statement": "On a compact complex n-fold X, Lamari's Lemma 3.3 concerns smooth real (1,1) forms without requiring them to be d-closed.",
      "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
      "quote": "Soit 6 une (1,1) -forme.",
      "premise": 10
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/12",
      "statement": "A real distribution on Ω⊂C^n whose complex Hessian is positive has a unique locally integrable genuine plurisubharmonic representative, obtained by decreasing radial convolution regularization (Demailly I.4.20, I.5.8).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "u ∈ Psh(Ω) locally integrable",
      "premise": 11
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/13",
      "statement": "On Ω⊂C^n, the cone Psh(Ω)∩L¹_loc(Ω) is closed in L¹_loc(Ω), and every bounded subset in the L¹_loc topology is relatively compact (Demailly I.5.9).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "every bounded subset is relatively compact.",
      "premise": 12
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/14",
      "statement": "For closed positive currents, geometric Lelong numbers are invariant under coordinate changes, unchanged by smooth-current additions when the resulting currents are positive and closed, and equal to one for the integration current of a smooth hypersurface at its smooth points (Demailly III.5.9, III.7.2).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "independent of the choice",
      "premise": 13
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/15",
      "statement": "For closed positive currents, geometric Lelong numbers are invariant under coordinate changes, unchanged by smooth-current additions when the resulting currents are positive and closed, and equal to one for the integration current of a smooth hypersurface at its smooth points (Demailly III.5.9, III.7.2).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "1 when",
      "premise": 13
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/16",
      "statement": "For a closed positive current T of bidimension (p,p) on a complex manifold, the sets {x:ν(T,x)≥c}, c>0, are analytic and have dimension at most p (Demailly III.8.5).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "analytic subsets of dimension",
      "premise": 14
    },
    {
      "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/17",
      "statement": "Every analytic subset of a complex manifold admits a locally finite family of global irreducible analytic components whose union is the subset (Demailly II.5.3).",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "locally finite family",
      "premise": 15
    }
  ],
  "premises": [
    "On every compact complex n-fold, n≥2, there exists a smooth strictly positive real (n−1,n−1) form Θ satisfying dd^cΘ=0 (Lamari, Proposition 1.3).",
    "Let X be a compact complex n-fold and b a smooth real (1,1) form. If ∫X b∧Θ≥0 for every smooth strictly positive real dd^c-closed (n−1,n−1) form Θ, there exists a real distribution q with b+dd^c q≥0. No d-closedness hypothesis on b is required (Lamari, Lemma 3.3).",
    "On an open Ω⊂C^n, a real distribution with positive complex Hessian has a unique locally integrable canonical plurisubharmonic representative; convolution with rescaled nonnegative smooth radial probability kernels decreases to it as the scale tends to zero (Demailly I.4.20, I.5.5, I.5.8).",
    "On connected Ω⊂C^n, a plurisubharmonic function not identically −∞ is locally integrable; Psh(Ω)∩L¹_loc(Ω) is closed in L¹_loc(Ω), and every L¹_loc-bounded subset is relatively compact (Demailly I.4.17, I.5.9).",
    "Geometric Lelong numbers of closed positive currents are coordinate invariant, and ν([H],x)=1 at every smooth point of an analytic hypersurface H (Demailly III.5.9, III.7.2).",
    "For a closed positive current S of bidimension (p,p) on a complex manifold, every upperlevel set {x:ν(S,x)≥c}, c>0, is analytic of dimension at most p (Demailly III.8.5).",
    "An analytic subset of a complex manifold is a locally finite union of global irreducible analytic components (Demailly II.5.3).",
    "On a compact complex n-fold there exists a smooth strictly positive real (n−1,n−1) form killed by dd^c (Lamari, Proposition 1.3).",
    "For a compact complex n-fold X and smooth real (1,1) form b, nonnegative pairing with every smooth strictly positive real dd^c-closed (n−1,n−1) form implies the existence of a real distribution q with b+dd^c q≥0, without any d-closedness hypothesis on b (Lamari, Lemma 3.3).",
    "On a compact complex n-fold, the Lamari criterion applies to an arbitrary smooth real (1,1) form b, including a nonclosed one: strictly positive pairing with every smooth strictly positive real dd^c-closed complementary form yields a real distribution q such that b+dd^c q≥0 (Lamari, Lemma 3.3).",
    "On a compact complex n-fold X, Lamari's Lemma 3.3 concerns smooth real (1,1) forms without requiring them to be d-closed.",
    "A real distribution on Ω⊂C^n whose complex Hessian is positive has a unique locally integrable genuine plurisubharmonic representative, obtained by decreasing radial convolution regularization (Demailly I.4.20, I.5.8).",
    "On Ω⊂C^n, the cone Psh(Ω)∩L¹_loc(Ω) is closed in L¹_loc(Ω), and every bounded subset in the L¹_loc topology is relatively compact (Demailly I.5.9).",
    "For closed positive currents, geometric Lelong numbers are invariant under coordinate changes, unchanged by smooth-current additions when the resulting currents are positive and closed, and equal to one for the integration current of a smooth hypersurface at its smooth points (Demailly III.5.9, III.7.2).",
    "For a closed positive current T of bidimension (p,p) on a complex manifold, the sets {x:ν(T,x)≥c}, c>0, are analytic and have dimension at most p (Demailly III.8.5).",
    "Every analytic subset of a complex manifold admits a locally finite family of global irreducible analytic components whose union is the subset (Demailly II.5.3)."
  ],
  "kind": "codex-report",
  "operationId": "82c7a934-88f4-422f-bb7e-5d9a23154dc5",
  "reportedAt": "2026-10-08T14:04:19.775Z"
}


# Entire independent statement-only public result, six complete proofs and actual DAG

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "Primary sources verify the permitted Lamari duality, canonical psh compactness, and closed-current Siu premises. Full CADG downloads failed, but exact author-hosted indexed passages were retrieved. No recursive foundational certification is claimed.",
      "detailedSummary": "Lamari Proposition 1.3 and Lemma 3.3 were checked in the primary Numdam PDF, including screenshots of printed pages 275–276. The smooth (1,1) input need not be d-closed. Demailly's canonical representative and local compactness statements, coordinate invariance, closed-current analytic upperlevel theorem, and locally finite global analytic-component theorem were checked through exact passages indexed from the author-hosted book. These are imported foundations, not proofs of A–D. Access limitations and evidence are recorded.",
      "text": "This is an ordinary unverified foundational audit for the restricted A–D assignment. Original P11 remains outside the claimed completion.\n\nThe imported premises are: existence of a smooth strictly positive dd^c-closed complementary form; Lamari's conversion of nonnegative pairings of a smooth real (1,1) form b against all such forms into b+dd^c q>=0 for a distribution q; unique canonical locally integrable psh representatives of distributions with positive complex Hessian; canonical radial convolution recovery; relative compactness of L1_loc-bounded psh families; coordinate invariance of geometric Lelong numbers; analyticity and dimension <=p of their positive upperlevel sets for CLOSED positive currents of bidimension (p,p); and local finiteness of global irreducible analytic components.\n\nThe primary sources are [Lamari, Courants kählériens et surfaces compactes, AIF 49 (1999)](https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf), Proposition 1.3, printed 267–268, Lemma 3.3, printed 275–276, and the preceding duality on printed 267; and [Demailly, Complex Analytic and Differential Geometry](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), I.4.17–4.20, I.5.8–5.9, III.7.2, III.8.5, and II.5.3. The author's [Books/documents page](https://www-fourier.univ-grenoble-alpes.fr/~demailly/documents.html) identifies the book and public PDF.\n\nLamari's primary PDF was successfully opened. Proposition 1.3, its separation argument, the duality context, and Lemma 3.3's printed separation proof were read. Screenshots of printed 275 and 276 confirm the nonnegative-pairing hypothesis, distribution conclusion, and absence of a d-closedness hypothesis on b. Our application has strictly positive pairings. A positive scalar difference in dd^c convention is absorbed by rescaling q.\n\nFull CADG PDF opens timed out, and direct local downloads were denied by the network sandbox. Exact indexed passages from the author-hosted primary book were nevertheless retrieved: I.4.17–4.18, I.4.20 with canonical recovery, I.5.8 with its displayed proof and I.5.9's statement, III.7.2's coordinate-invariance argument, III.8.5's complete statement and short reduction to III.8.4, and II.5.3's global-component statement. III.7.2 is the location actually retrieved for coordinate invariance. We do not claim to have read the entire CADG PDF or recursively certified the permitted subharmonic compactness and Siu foundations.\n\nSmooth perturbation invariance and the hyperplane Lelong normalization are reconstructed directly in n3. Siu is never applied to a nonclosed current.\n\nEvidence is saved in sources/browser_captures.json; primary-source retrieval requests are in source_requests.json. The public download attempt is implemented in fetch_primary_sources.py, with failures recorded in source_download_output.txt. Rerun: python fetch_primary_sources.py > source_download_output.txt. Browser primary-source passages were retrieved despite local download failure. No credentials, other workers' material, or verifier histories were inspected.\n\nArtifacts: /workspace/research/native-workers/codex-kwaUfi",
      "support": []
    },
    {
      "id": "n2",
      "summary": "A fixed Hermitian Hessian lower bound and sup_X u=0 give uniform global L1 bounds and canonical L1 compactness, with normalization retained. No closedness of omega is required.",
      "detailedSummary": "Add nonnegative local quadratics to obtain psh functions. A submean inequality centered where u>=-E bounds the negative integral on an inner chart ball. Positive-volume overlaps propagate bounds along a finite connected cover from a point near the global supremum. Local psh compactness gives a compatible global L1 limit; canonical recovery glues the representatives pointwise. Moving-center submean inequalities at maximizers preserve supremum zero. This supplies A's normalization and compactness obligations.",
      "text": "Let X be connected and compact, omega a fixed smooth positive Hermitian form, lambda>0 fixed, and mu a smooth positive volume form. We prove uniform L1(mu) bounds and relative compactness for genuine quasi-psh u satisfying dd^c u>=-lambda omega and sup_X u=0. The canonical representative and local psh compactness premises are those audited in n1.\n\nChoose finitely many coordinate balls W_i=B(0,4r_i), with closures inside coordinate domains, whose inner balls V_i=B(0,r_i) cover X. Choose rho_i=K_i|z_i|^2 so that dd^c rho_i>=lambda omega on W_i. Then p_i=u+rho_i is genuine psh. Fixed constants satisfy 0<=rho_i<=H_i and dmu<=M_i dLebesgue on W_i. The overlap graph of the V_i is connected, since otherwise their unions would disconnect X.\n\nIf x belongs to V_i and u(x)>=-E, E>=0, the Euclidean ball B(x,2r_i) contains V_i and is contained in W_i. Its volume v_i is independent of x. Submean gives integral_B p_i>=v_i p_i(x)>=-E v_i. Since u<=0,\n integral_{V_i}(-u)dmu<=M_i integral_B(-u)dLebesgue<=M_i v_i(H_i+E).\nDenote this fixed affine bound by F_i(E).\n\nStart at a point where u>-1. If its chart is V_i, the negative integral there is <=F_i(1). For an edge i–k, let m_ik=mu(V_i intersect V_k)>0. If the negative integral on V_i is <=L_i, some point of the overlap satisfies u>=-(L_i+1)/m_ik; otherwise its negative integral would exceed L_i. Apply the submean estimate in V_k to obtain L_k<=F_k((L_i+1)/m_ik). Propagate along a finite spanning tree and maximize over the finitely many possible initial vertices. This bounds every chart integral uniformly, hence ||u||_L1(mu)<=sum_i L_i.\n\nFor a sequence u_j, these bounds make u_j+rho_i L1_loc-bounded psh on W_i. By n1, extract a subsequence converging locally in L1 on every chart to psh representatives p_i. The differences p_i-rho_i agree almost everywhere on overlaps. They agree pointwise as canonical representatives: radial convolution recovers each representative from the same distribution, and convolution of the smooth corrections tends pointwise to those corrections. Thus they glue to a genuine global quasi-psh u. The finite inner cover gives global L1(mu) convergence. Distributional differentiation preserves dd^c u>=-lambda omega. The inequality u<=0 holds almost everywhere, and canonical submean recovery makes it hold everywhere.\n\nNormalization is also preserved. Choose maximizers x_j with u_j(x_j)=0 and pass to x_j->x. In a coordinate neighborhood of x with correction rho, for each sufficiently small fixed r,\n rho(x_j)<=average_{B(x_j,r)}(u_j+rho).\nL1 convergence and continuity of integration of a fixed L1 function over moving balls give rho(x)<=average_{B(x,r)}(u+rho). Let r decrease to zero. Canonical psh ball-average recovery gives u(x)>=0. Together with u<=0, this yields sup_X u=0.\n\nIf one starts with a global distribution q satisfying dd^c q>=-lambda omega, local quadratic corrections and n1 first produce canonical psh representatives q+rho_i. Their differences glue by the same recovery argument. Their global quasi-psh representative has finite supremum and can be normalized before applying the preceding proof.\n\nThis establishes actual canonical compactness and a nontrivial normalized limit. It requires neither closedness of omega nor almost-everywhere modifications. It is a mathematical argument from the stated foundations, not a computational observation.\n\nArtifacts: /workspace/research/native-workers/codex-kwaUfi",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "Target A holds: bounded concentration pairings against ALL normalized smooth positive dd^c-closed complementary tests force a global analytic hypersurface containing U'×{0}. Consequently C_delta tends to infinity on a hypersurface-free X.",
      "detailedSummary": "Lamari applied to lambda omega-B_delta gives distributions with one uniform Hessian lower bound. n2 produces genuine normalized canonical potentials and an L1 limit. Full-variable smooth testing establishes B_delta->chi[H] and lambda omega+dd^c q>=chi[H]. Local quadratic corrections yield CLOSED positive currents whose Lelong numbers agree on overlaps. Siu gives a proper global analytic upperlevel set; its codimension-one components contain the entire patch. No singular fiber restriction or nonclosed Siu application occurs.",
      "text": "We prove A with exactly its cutoff family and all its tests. Write H={zeta=0} in the chosen chart. Extend chi[H] by zero; its support is compactly contained in the chart. It is not asserted to be globally closed.\n\nBy n1, a smooth strictly positive dd^c-closed complementary form exists and can be normalized by its positive degree against omega. Thus T_omega is nonempty. For fixed delta, smoothness, compactness, and positivity of omega give 0<=B_delta<=k_delta omega with finite k_delta. Therefore 0<=C_delta<=k_delta<infinity.\n\nSuppose delta_j decreases to zero and C_delta_j<=M. Put lambda=M+1. For any smooth strictly positive dd^c-closed complementary form Theta, its degree d_Theta=integral omega Theta is positive, and its normalization belongs to T_omega. Hence\n integral (lambda omega-B_delta_j) Theta>=(lambda-M)d_Theta>0.\nLamari's lemma in n1 applies without requiring the smooth form lambda omega-B_delta_j to be closed. It gives a real distribution q_j with\n lambda omega+dd^c q_j>=B_delta_j.\nBy n2 choose its genuine global quasi-psh representative and subtract its supremum. Thus sup_X q_j=0 and dd^c q_j>=-lambda omega, with the same lambda for every j. After extraction, n2 gives global L1 convergence to a genuine normalized q.\n\nFor every smooth full-variable complementary test Xi,\n integral B_delta Xi=integral_C p(xi)sigma_xi integral_z chi(z)i_{delta xi}^*Xi\n tends to integral_z chi(z)i_0^*Xi=<chi[H],Xi>,\nwhere i_s(z)=(z,s). Compact support gives uniform convergence of the smooth coefficients. Components containing d zeta or d bar zeta are annihilated by sigma_zeta; the remaining tangential coefficients retain their full zeta dependence before taking the limit. Only smooth test forms are pulled back. No singular current is restricted to a fiber.\n\nConsequently B_delta converges as a current to chi[H]. L1 convergence gives distributional convergence of dd^c q_j. Testing with arbitrary smooth semipositive complementary forms preserves positivity and yields\n Q:=lambda omega+dd^c q>=chi[H].\nQ is generally nonclosed, since dQ=lambda d omega.\n\nOn each coordinate ball choose a smooth quadratic rho_i with dd^c rho_i>=lambda omega. Then\n S_i:=dd^c(q+rho_i)=Q+(dd^c rho_i-lambda omega)\nis CLOSED and positive. On overlaps S_i-S_k=dd^c(rho_i-rho_k) is smooth. A smooth (1,1) current contributes O(r^{2n}) to its flat complementary mass in a radius-r ball; the Lelong denominator is r^{2n-2}. Its normalized contribution is therefore O(r^2), proving invariance under smooth differences. With coordinate invariance from n1, nu(x):=nu(S_i,x) is globally well defined.\n\nApply Siu only to the closed positive S_i, of bidimension (n-1,n-1). The local sets {nu(S_i,x)>=1} are analytic of dimension <=n-1 and agree on overlaps. They define a global closed analytic subset E. The dimension bound makes E proper.\n\nNear any point of U'×{0}, chi=1, so S_i>=[H]. Both currents are closed there, and their difference is positive. Geometric Lelong numbers respect this inequality by their defining nonnegative ball integrals. The hyperplane normalization follows directly: with sigma=dd^c|Z|^2=i sum dZ_k wedge dbar Z_k/(2pi),\n integral_{H intersect B(0,r)} sigma^{n-1}=r^{2n-2}.\nThus nu([H],x)=1 and U'×{0} is contained in E.\n\nLet D be the union of the global irreducible components of E having dimension n-1. The analytic-component premise checked at Demailly II.5.3 in n1 gives local finiteness; compactness makes this a finite family. Its union is a closed analytic hypersurface. At every point of the patch, the smooth irreducible (n-1)-dimensional hyperplane germ lies in E and therefore in an (n-1)-dimensional component. Components of smaller dimension cannot contain that germ. Hence D contains the whole U'×{0}.\n\nIf X has no analytic hypersurfaces and C_delta failed to tend to infinity, some finite M would bound C_delta at arbitrarily small delta. Choosing a decreasing sequence would give the forbidden D. Therefore C_delta tends to infinity.\n\nThis proves A, including global normalization, canonical compactness, full-variable current convergence, gluing, and properness. It assumes neither closedness nor balancedness of omega. It supplies no determinant estimate or admissible mass-collapse sequence.\n\nArtifacts: /workspace/research/native-workers/codex-kwaUfi",
      "support": [
        "n1",
        "n2"
      ]
    },
    {
      "id": "n4",
      "summary": "Target B holds with actual global smooth logarithmic regularizations and a uniform bound C_delta<=4||p||_infinity K for sufficiently small delta, under its precise whole-chart Cartier hypothesis.",
      "detailedSummary": "Modify a smooth metric on O(D) to make |s|_h^2=|zeta|^2 near every small-delta cutoff support. The globally smooth functions F_epsilon=log(|s|_h^2+epsilon^2) have a uniform Hessian lower bound. Their explicit flat-chart Hessian dominates B_delta. Smooth dd^c Stokes against every normalized complementary test gives the uniform bound. The construction permits other branches elsewhere but requires the specified simple branch throughout the cutoff support.",
      "text": "Let E=O(D) and s its canonical section. The hypothesis implies that e=s/zeta is a nowhere-zero holomorphic frame on the cutoff chart: the branch zeta=0 is simple and there are no other zeros there.\n\nChoose delta_0 so that K_0=supp(chi)×{|zeta|<=delta_0} is compactly contained in this frame domain. Start with any global smooth Hermitian metric h_0. Put ell=log|e|_{h_0}^2 and choose a smooth cutoff alpha equal to one near K_0 and compactly supported in the frame domain. Define\n h=h_0 exp(-alpha ell),\nextending alpha ell by zero. This is a global smooth positive metric with |e|_h^2=1 near K_0. Hence r:=|s|_h^2=|zeta|^2 on a fixed neighborhood of every B_delta support for delta<=delta_0.\n\nThe functions F_epsilon=log(r+epsilon^2) are globally smooth for every epsilon>0. In a local frame with squared metric exp(-phi), off D one has dd^c log r=-kappa, where kappa=dd^c phi is the global smooth curvature. The exact chain rule gives\n dd^c F_epsilon=-[r/(r+epsilon^2)]kappa+[epsilon^2 r/(r+epsilon^2)^2]d log r wedge d^c log r.\nThe second term is semipositive. Choose K>=1 with -K omega<=kappa<=K omega. Since r/(r+epsilon^2) lies in [0,1], dd^c F_epsilon>=-K omega off D. Smoothness extends the inequality to every point of D, including intersections of branches outside the prescribed chart.\n\nOn the fixed flat neighborhood,\n dd^c F_delta=[delta^2/(|zeta|^2+delta^2)^2]sigma_zeta.\nFor |zeta|<=delta this coefficient is >=1/(4delta^2). Set L=4||p||_infinity. Using chi<=1 and the support condition on p gives B_delta<=L dd^c F_delta on its support. Outside that support B_delta=0 and dd^c F_delta+K omega>=0. Therefore globally\n B_delta<=L(dd^c F_delta+K omega).\n\nFor every Theta in T_omega, smooth integration by parts on compact X gives\n integral dd^c F_delta Theta=integral F_delta dd^c Theta=0.\nNo d-closedness of Theta is required. Wedge the global inequality with Theta and use its normalization to obtain\n integral B_delta Theta<=LK.\nTaking the supremum proves C_delta<=4||p||_infinity K uniformly for delta<=delta_0.\n\nThis uses actual global smooth logarithmic regularizations and covers all smooth tests. It gives no corresponding bound merely from an unrelated divisor or from an unspecified chart crossing branch intersections.\n\nThe exact Hessian coefficients were independently checked by verify_algebra.py. algebra_output.txt records delta^2/(delta^2+s)^2, its rescaled coefficient (1+y)^(-2), and the global profile derivatives r/(epsilon^2+r) and epsilon^2 r/(epsilon^2+r)^2. Rerun: python verify_algebra.py > algebra_output.txt. These symbolic checks verify formulas; the global metric construction and Stokes argument supply the proof. Test nonemptiness is imported from n1.\n\nArtifacts: /workspace/research/native-workers/codex-kwaUfi",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n5",
      "summary": "Target C holds exactly for its displayed radial family: positivity requires a,g>0, closure forces constant a, and the asserted root, integrals, sharp bound, and mean-only equality condition are correct.",
      "detailedSummary": "The supplied surface geometry gives dd^c(g beta)=-g' c beta-g c^2 and dd^c Gamma=a'' eta^2 beta; periodicity forces constant a. An adapted coframe proves strict positivity and the unique positive square root. Fiber integration gives D=TA(a+gbar) and R=(3/2)TA sqrt(a)gbar. The bound follows from the exact factorization (a+b)^3-(27/4)ab^2=(b-2a)^2(b+a/4). Positive Fejer profiles attain equality with fixed mean and unbounded peaks. This classifies only the stated family.",
      "text": "Suppress pullbacks in the original primitive elliptic bundle. Local lifts of t differ by integer multiples of T, so dt, d^c t, beta, and smooth periodic coefficient functions descend. Use c=dd^c t, d eta=d c=0, eta c=0, and horizontality over the complex surface.\n\nWith beta=dt wedge d^c t,\n beta=i partial t wedge barpartial t/(2pi), beta^2=0,\n d beta=-dt wedge c, d^c beta=-c wedge d^c t, dd^c beta=-c^2.\nSince d^c(g beta)=-g c wedge d^c t,\n dd^c(g beta)=-g' c beta-g c^2.\nMultiplication by eta kills the first term by primitiveness and the second by horizontal degree. Also\n dd^c(a eta^2)=(a'' beta+a' c)eta^2=a'' eta^2 beta.\nThus dd^c Gamma=a'' eta^2 beta. This top form is everywhere positive. Closure forces a''=0, and periodicity makes a constant. Conversely constant a gives closure for every periodic g.\n\nChoose an adapted coframe with positive rank-one forms E_1,E_2,E_3 satisfying eta=E_1+E_2 and beta=E_3. Then\n Gamma=2a E_1 E_2+g E_1 E_3+g E_2 E_3.\nIts complementary Hermitian matrix is diagonal with coefficients 2a,g,g, so strict positivity is equivalent to a>0 and g>0. Combining this with closure gives exactly a positive constant a and positive periodic g.\n\nSet x=sqrt(a) and y=g/(2sqrt(a)). The genuine positive form gamma=x eta+y beta satisfies gamma^2=Gamma. It is the unique positive square root: the complementary matrix of the square of a positive Hermitian matrix H is twice its cofactor matrix, which determines H uniquely. Here this forces diagonal entries x,x,y.\n\nOn a fiber, t=2 log|w| up to a base-dependent shift, and d^c t=d theta/(2pi). Therefore integral_fiber beta=T, and for periodic h,\n integral_X h(t)eta^2 beta=A integral_0^T h(t)dt=TA hbar.\nThe interval shift is immaterial by periodicity. Since eta^3=0 and beta^2=0,\n omega Gamma=(a+g)eta^2 beta,\n gamma^3=(3/2)sqrt(a)g eta^2 beta.\nWith b=gbar and K=TA this yields D=K(a+b), R=(3/2)K sqrt(a)b, V=3K.\n\nThe sharp inequality is equivalent to\n (a+b)^3-(27/4)ab^2>=0.\nExactly,\n (a+b)^3-(27/4)ab^2=(b-2a)^2(b+a/4).\nHence R<=D^(3/2)/sqrt(V), with equality precisely b=2a. For D=1, the sharp parameters are a=1/(3TA), b=2/(3TA), giving R=1/sqrt(V). Pointwise constancy of g is unnecessary.\n\nAn explicit smooth equality family is\n F_N(theta)=(1/N)|sum_{k=0}^{N-1}exp(i k theta)|^2\n =1+2 sum_{k=1}^{N-1}(1-k/N)cos(k theta),\n g_N(t)=a[1+F_N(2pi t/T)], a=1/(3TA).\nFor N>=2, F_N is smooth, nonnegative, has mean one and peak N. Thus g_N>=a>0, gbar_N=2a, and max g_N=a(N+1) tends to infinity, while D=1 and R=1/sqrt(V) for every N. Away from t=0 modulo T, the sine-quotient formula gives F_N=O(1/N), so its peaks concentrate. These are complementary tests, not admissible Monge–Ampère potentials.\n\nverify_algebra.py independently checks the exterior identities, the positive-root expansion, both integral coefficients, and the polynomial factorization. Its finite Fejer checks N=2,8,32,128 give mean g_N/a=2 and peaks 3,9,33,129. The analytical formulas above prove the all-N statements. algebra_output.txt records Python 3.12.14, SymPy 1.14.0, and successful exact checks. Rerun: python verify_algebra.py > algebra_output.txt. Execution does not certify the mathematical proof.\n\nOnly Gamma=a eta^2+g eta beta is classified. Arbitrary complementary tests are not replaced by this family.\n\nArtifacts: /workspace/research/native-workers/codex-kwaUfi",
      "support": []
    },
    {
      "id": "n6",
      "summary": "The restricted A–D assignment is complete: A and B hold, C has the stated sharp classification, and D's limitations are valid. The specified divisor-free K3 has C_delta->infinity; original P11 and universal nonzero-Chern-class mass vanishing remain open.",
      "detailedSummary": "Apply A to the compact connected divisor-free K3 total space stipulated in the input. Its concentration pairings diverge, but no positive-root volume divergence has been established. C controls only its radial family. A positive-matrix example explains why linear concentration alone supplies no determinant lower bound, without claiming realization by global tests. No smooth admissible collapsing potentials, exact K3 lower mass, or universal nonzero-class conclusion is supplied. Completion and candidate=true concern only the declared restricted assignment.",
      "text": "This last note claims complete resolution of the DECLARED RESTRICTED A–D ASSIGNMENT, using n3, n4, and n5 and their support notes. It does not claim completion of unchanged original P11.\n\nA is reconstructed in n3, including all full-variable smooth tests, normalized canonical compactness, the current limit, locally CLOSED positive currents, and a proper globally glued analytic upperlevel set whose hypersurface part contains the whole patch. B is reconstructed in n4 with a global Cartier metric, actual smooth logarithmic regularizations, a uniform Hessian lower bound, and all-test smooth Stokes. C is reconstructed in n5 with necessity, actual positivity, the unique positive root, exact integrals, the sharp bound, and equality determined solely by gbar=2a. None of A–C is rejected.\n\nFor D, original P11 explicitly stipulates that the K3 total space has no divisors. An analytic hypersurface on a smooth complex manifold gives a divisor, so this input rules out A's hypersurface conclusion. Its X is connected and compact of complex dimension three, and omega is smooth positive. A therefore applies and gives, for every stated cutoff family,\n C_delta=sup_{Theta in T_omega} integral_X B_delta Theta -> infinity.\nThis uses the given no-divisor hypothesis; it is not a newly proved classification of elliptic-bundle divisors. Smooth tests approximating each finite supremum exist by its definition, but their positive-root volumes have not been estimated.\n\nLinear pairing divergence alone supplies no determinant lower bound. Pointwise in dimension three, a positive complementary matrix Q_N=diag(N,N^(-1),N^(-1)) has trace tending to infinity and determinant tending to zero. In the convention Q=2 cof(H) for gamma^2, det H=sqrt(det Q/8), and gamma^3 is proportional to det H. This explains the missing type of estimate. It is not asserted that these matrices realize global dd^c-closed normalized tests.\n\nC's bound covers only Gamma=a eta^2+g eta beta. Its smooth degree-one equality family has arbitrarily high peaks with constant root integral, and C supplies no estimate on other tests. A does not enlarge that classified family, and B requires the exact local divisor branch. Neither an all-test root-volume theorem nor an all-potential lower-mass theorem has been established.\n\nNo genuine smooth admissible mass-collapse sequence is constructed here. No exact K3 v_minus, positive K3 lower bound, or proof or counterexample to universal vanishing for nonzero real Chern class is supplied. The original completion criteria remain open. Restricted completion must not be interpreted as original completion.\n\nThe complete saved deliverable is restricted_notes.json, with individual proof texts notes/n1.md through notes/n6.md. Input is in assignment_input.json. The implementation and exact output are verify_algebra.py and algebra_output.txt. Primary-source access records are sources/browser_captures.json, source_requests.json, fetch_primary_sources.py, and source_download_output.txt. The environment is Python 3.12.14 and SymPy 1.14.0 on Linux 6.18.44 x86_64. Rerun python verify_algebra.py > algebra_output.txt and python check_deliverable.py > deliverable_check_output.txt. The structural checks confirm the six-note support DAG and artifact consistency. No resource-heavy computation was needed.\n\nSuccessful execution does not establish mathematical correctness. These remain ordinary unverified drafts. candidate=true refers solely to the completed restricted A–D assignment.\n\nArtifacts: /workspace/research/native-workers/codex-kwaUfi",
      "support": [
        "n3",
        "n4",
        "n5"
      ]
    }
  ],
  "candidate": true,
  "workspace": "/workspace/research/native-workers/codex-kwaUfi"
}


# Entire independent-result root judgments and actual owner settlement

{
  "recorded_at_utc": "2026-10-08T14:48:42.169644+00:00",
  "label": "P11-divisor-free-concentration-and-radial-tests-20261008-statement-only-cold",
  "actual_owner_session": 63719,
  "actual_owner_exit_code": 0,
  "actual_owner_exit_observed_by_write_stdin": true,
  "actual_exit_response": {
    "chunk_id": "5d70c9",
    "wall_time_seconds": 2.1272e-05,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  },
  "public_status": "completed",
  "completed_all_settled_quiescent": true,
  "complete_result_sha256": "213f53addeeb69c7d71966bcd7852faaccf4758abe23dfdae0a4412c29f94386",
  "complete_result_bytes": 25995,
  "actual_candidate": true,
  "complete_public_note_count": 6,
  "actual_support_DAG": {
    "n1": [],
    "n2": [
      "n1"
    ],
    "n3": [
      "n1",
      "n2"
    ],
    "n4": [
      "n1"
    ],
    "n5": [],
    "n6": [
      "n3",
      "n4",
      "n5"
    ]
  },
  "whole_result_all_six_complete_proofs_summaries_support_and_metadata_actually_root_read": true,
  "actual_entire_untruncated_display_chunk": "581027",
  "actual_display_tokens": 6499,
  "every_complete_proof_and_its_actual_support_chain_root_assessed": true,
  "individual_root_mathematical_judgments": [
    "n1: Lamari applies to arbitrary smooth real backgrounds with every ddclosed positive complementary pairing and no closedness assumption. Canonical recovery and psh compactness are imported at their exact scopes. The independent worker reports full Lamari printed proofs, but only exact indexed CADG primary passages after complete-PDF access failed. Root separately read the complete component and coordinate-invariance printed contexts; no claim of worker-wide full PDF or recursive Siu/subharmonic certification is made.",
    "n2: Inner balls of radiusr cover X; outer radius4r gives the ball2r centered at the point near the supremum. Nonnegative quadratics bound positive terms, and submean bounds negative integrals. Positive-volume overlaps and a finite spanning tree give a common global L1 bound; this global bound also bounds every relatively compact portion of the outer balls, justifying local psh compactness. Canonical representatives glue from their common distribution, and moving-ball submean at maximizers preserves sup0. No minus-infinity or arbitrary a.e. modification is allowed.",
    "n3: The full smooth complementary cone is used before normalization and Lamari. A single lambda=M+1 gives actual canonical potentials. Smooth full-variable testing proves Bdelta->chi[H], and positivity passes with L1 ddc convergence. Siu applies only to locally closed positive dd(q+rho), never to lambda omega+ddq. Smooth-difference normalized mass O(r^2) and coordinate invariance glue the Lelong function. The analytic upperlevel has dimension<=n-1 and contains the patch via the exact hyperplane normalization. The finite global hypersurface-component union contains every patch germ; the current author additionally identifies one containing component by the finite analytic-intersection/identity argument. Both establish the stated global hypersurface. Excluding every bounded subsequence proves the actual delta->0 divergence.",
    "n4: The Cartier branch is simple on the entire fixed chart, so the section frame is nowhere zero after division by zeta. A global smooth metric modification flattens that frame near the complete small-delta support. The actual global log(|s|^2+delta^2) functions have curvature lower bound-Komega, including points of the divisor by smooth extension. Their flat-chart Hessian dominates Bdelta at coefficient1/(4delta^2). The all-test smooth ddc-Stokes pairing gives uniform Cdelta<=4||p||K. There is no inference at arbitrary local branch intersections or from an unrelated divisor.",
    "n5: The exterior identities give ddGamma=a-second-prime eta^2beta because primitive eta c=0 and horizontal surface degree kill the g terms. Periodicity forces constant a, and the exact cofactor diagonal(g,g,2a) forces positive a,g. The displayed positive root, fiber periodT, D and R are exact. The factorization(b-2a)^2(b+a/4) gives the sharp mean-only equality condition. The complete supplemental Fejer family has strictly positive g, fixed mean2a, unbounded peaks and fixed sharp root volume. It is independently assessed but not added as a new theorem to the current author source after full review.",
    "n6: The no-divisor K3 assumption is exactly original-task background, not a new classification theorem. Its ALL-test trace pairings diverge; no corresponding determinant or full-mass assertion is proved. The pointwise diagonal-matrix diagnostic is explicitly not a realization by global normalized ddclosed tests. It diagnoses an absent inference rather than supplying a Hermitian counterexample. No full original completion, K3 lower bound, collapse sequence or universal nonzero-Chern-class conclusion is accepted."
  ],
  "current_author_source_sha256": "be049492e7336afe8815d7fdfc038e2769c1a62a36a3b6b466a3db5b36fd5516",
  "original_full_INCONCLUSIVE_preserved": true,
  "final_comparison_pending": true,
  "mathematical_acceptance": false,
  "original_P11_completed": false,
  "published": false,
  "current_campaign_stdout_or_private_reasoning_or_artifact_trees_read": false,
  "historical_accidental_raw_search_boundary_disclosed": true,
  "no_recursive_certification_of_all_imported_foundations_claimed": true
}


# Exact clarified final-task preparation; original and all targets unchanged

{
  "recorded_at_utc": "2026-10-08T14:30:16.038291+00:00",
  "old_prepared_task": "inputs/P11-divisor-free-concentration-and-radial-tests-A-D-limited-final-20261008-task.prepared.json",
  "old_prepared_task_sha256": "fd0f50479166aa0ca5035f446a21c8770e810ddcf30dc93939787d871df1e326",
  "old_frozen_task_unchanged": true,
  "new_prepared_task": "inputs/P11-divisor-free-concentration-and-radial-tests-A-D-limited-final-20261008-task-foundations-clarified.prepared.json",
  "new_prepared_task_sha256": "39ce558ede64bf15facca583ac81a0b17d7e5902e78c7af9d536c14842b01898",
  "exact_problem_diff": "--- P11-divisor-free-concentration-and-radial-tests-A-D-limited-final-20261008-task.prepared.json\n+++ P11-divisor-free-concentration-and-radial-tests-A-D-limited-final-20261008-task-foundations-clarified.prepared.json\n@@ -92,10 +92,23 @@\n its geometric Lelong upperlevel sets{x:nu(T,x)>=c},c>0, are analytic sets of\n dimension at most p. Lelong numbers are coordinate invariant, are unchanged\n by adding a smooth current, and nu([smooth hypersurface],x)=1 on its smooth\n-locus. These are Demailly,CADG,III.5.9,III.5.11,III.8.5, at the same URL.\n-The complete printed III.5.11 proof and III.8.5 statement and proof were read;\n+locus. These are Demailly,CADG,III.5.9,III.7.2 and III.8.5, at the same URL.\n+The complete printed III.7.2 coordinate-invariance proof and III.8.5\n+statement and printed proof were read; III.5.11 concerns properness in a\n+different Lelong-number discussion and is not the coordinate-invariance locator.\n III.8.4 is its explicitly imported Siu foundation, not a newly recursively\n certified theorem. Do not apply Siu directly to the nonclosed current omega+dd^c q.\n+\n+An analytic set has a unique locally finite family of global irreducible\n+components, each a closed irreducible analytic subset, whose union is that\n+analytic set. On a compact space this family is finite. This is the standard\n+irreducible-component theorem, Demailly,CADG,II.5.3, at the same URL; its\n+complete printed statement and proof were read. The theorem does not grant\n+the target's global hypersurface or its containment of the transverse\n+polydisk. Applying it to the actual proper analytic upperlevel, identifying\n+the containing component and proving its dimension and containment remain\n+proof obligations. No target, current limit or determinant conclusion is\n+added to the imported foundations.\n \n Elementary positive-current/matrix algebra, smooth local quadratic\n corrections, local submean inequalities, compactness of a finite chart cover,\n",
  "operative_A_D_targets_and_completion_criteria_unchanged": true,
  "original_problem_and_criterion_verbatim": true,
  "complete_component_theorem_primary_read_range": {
    "file": "inputs/primary/Demailly-agbook-Harvard.txt",
    "lines": [
      5430,
      5635
    ],
    "actual_read_chunk": "e735d8"
  },
  "complete_coordinate_invariance_primary_read_range": {
    "file": "inputs/primary/Demailly-agbook-Harvard.txt",
    "lines": [
      9070,
      9180
    ],
    "actual_read_chunk": "87978f"
  },
  "native_admitted": false,
  "whole_new_task_root_read_pending": false,
  "final_argument_not_yet_assembled": true,
  "cold_actual_owner_exit_and_whole_public_result_required_before_final_admission": true,
  "mathematical_acceptance": false,
  "original_P11_completed": false,
  "published": false,
  "whole_new_task_root_read_chunk": "84f1bf",
  "source_path_typo_corrected_before_native_admission": true
}


# Entire original-review root binding/application assessment

{
  "recorded_at_utc": "2026-10-08T14:14:08.946915+00:00",
  "label": "P11-divisor-free-concentration-and-radial-tests-20261008-full-original-review",
  "actual_owner_session": 36815,
  "actual_owner_exit_code": 0,
  "actual_owner_exit_observed_by_write_stdin": true,
  "actual_exit_response": {
    "chunk_id": "8d04d2",
    "wall_time_seconds": 2.8202e-05,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  },
  "public_status": "completed",
  "all_calls_settled": true,
  "owner_quiescent": true,
  "complete_result_sha256": "841db6d1bd4fe224dce84abdddf295ed3dbe238720e370380f52e633a8c248a2",
  "complete_result_bytes": 15974,
  "actual_verdict": "INCONCLUSIVE",
  "whole_original_report_all16_premises_all18_bindings_all_metadata_actually_root_read": true,
  "actual_entire_untruncated_display_chunk_id": "856d6d",
  "every_binding_logically_reassessed": true,
  "exact_indexed_primary_applications": [
    {
      "premise_index": 0,
      "statement": "On every compact complex n-fold, n≥2, there exists a smooth strictly positive real (n−1,n−1) form Θ satisfying dd^cΘ=0 (Lamari, Proposition 1.3).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/0",
          "statement": "On every compact complex n-fold, n≥2, there exists a smooth strictly positive real (n−1,n−1) form Θ satisfying dd^cΘ=0 (Lamari, Proposition 1.3).",
          "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
          "quote": "Il existe sur X des (n-l.n-l) -formes strictement positives",
          "premise": 0
        }
      ],
      "root_logical_application": "Lamari1.3 gives strict smooth ddclosed complementary tests in every compact dimensionn>=2; positive omega trace supplies actual normalization.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 1,
      "statement": "Let X be a compact complex n-fold and b a smooth real (1,1) form. If ∫X b∧Θ≥0 for every smooth strictly positive real dd^c-closed (n−1,n−1) form Θ, there exists a real distribution q with b+dd^c q≥0. No d-closedness hypothesis on b is required (Lamari, Lemma 3.3).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/1",
          "statement": "Let X be a compact complex n-fold and b a smooth real (1,1) form. If ∫X b∧Θ≥0 for every smooth strictly positive real dd^c-closed (n−1,n−1) form Θ, there exists a real distribution q with b+dd^c q≥0. No d-closedness hypothesis on b is required (Lamari, Lemma 3.3).",
          "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
          "quote": "0 + dd°\\ >_ 0 (au sens des courants).",
          "premise": 1
        }
      ],
      "root_logical_application": "Lamari3.3 applies to the actual smooth real omega-kappa Bdelta, with all positive ddclosed complementary pairings nonnegative and indeed strict. It requires no closedness. The resulting distribution is corrected locally and recovered canonically.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 2,
      "statement": "On an open Ω⊂C^n, a real distribution with positive complex Hessian has a unique locally integrable canonical plurisubharmonic representative; convolution with rescaled nonnegative smooth radial probability kernels decreases to it as the scale tends to zero (Demailly I.4.20, I.5.5, I.5.8).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/2",
          "statement": "On an open Ω⊂C^n, a real distribution with positive complex Hessian has a unique locally integrable canonical plurisubharmonic representative; convolution with rescaled nonnegative smooth radial probability kernels decreases to it as the scale tends to zero (Demailly I.4.20, I.5.5, I.5.8).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "u ∈ Psh(Ω) locally integrable",
          "premise": 2
        }
      ],
      "root_logical_application": "Demailly canonical distribution representative and decreasing radial convolution concern only genuinely positive local complex Hessians after a fixed positive quadratic. Almost-everywhere equality gives pointwise agreement of the genuine corrected representatives.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 3,
      "statement": "On connected Ω⊂C^n, a plurisubharmonic function not identically −∞ is locally integrable; Psh(Ω)∩L¹_loc(Ω) is closed in L¹_loc(Ω), and every L¹_loc-bounded subset is relatively compact (Demailly I.4.17, I.5.9).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/3",
          "statement": "On connected Ω⊂C^n, a plurisubharmonic function not identically −∞ is locally integrable; Psh(Ω)∩L¹_loc(Ω) is closed in L¹_loc(Ω), and every L¹_loc-bounded subset is relatively compact (Demailly I.4.17, I.5.9).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "every bounded subset is relatively compact.",
          "premise": 3
        }
      ],
      "root_logical_application": "Local psh compactness is used after explicit finite inner/outer ball submean and connected positive-volume overlap propagation of a uniform L1 bound. Sup normalization prevents the minus-infinity alternative; the compactness theorem itself is an imported standard foundation.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 4,
      "statement": "Geometric Lelong numbers of closed positive currents are coordinate invariant, and ν([H],x)=1 at every smooth point of an analytic hypersurface H (Demailly III.5.9, III.7.2).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/4",
          "statement": "Geometric Lelong numbers of closed positive currents are coordinate invariant, and ν([H],x)=1 at every smooth point of an analytic hypersurface H (Demailly III.5.9, III.7.2).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "independent of the choice",
          "premise": 4
        },
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/5",
          "statement": "Geometric Lelong numbers of closed positive currents are coordinate invariant, and ν([H],x)=1 at every smooth point of an analytic hypersurface H (Demailly III.5.9, III.7.2).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "1 when",
          "premise": 4
        }
      ],
      "root_logical_application": "The limit local closed positive ddc(v+rho) dominates kappa[H] where chi=1. Smooth H has geometric Lelong number1, and III.7.1 with its III.7.2 corollary supplies coordinate invariance. Smooth differences have normalized trace O(r^2), so the same Lelong function glues independently of correction.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 5,
      "statement": "For a closed positive current S of bidimension (p,p) on a complex manifold, every upperlevel set {x:ν(S,x)≥c}, c>0, is analytic of dimension at most p (Demailly III.8.5).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/6",
          "statement": "For a closed positive current S of bidimension (p,p) on a complex manifold, every upperlevel set {x:ν(S,x)≥c}, c>0, is analytic of dimension at most p (Demailly III.8.5).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "analytic subsets of dimension",
          "premise": 5
        }
      ],
      "root_logical_application": "III.8.5 applies only to the actual local CLOSED positive current of bidimension(n-1,n-1), and gives analytic upperlevel dimension<=n-1. The inherited Siu theorem is credited and not recursively newly certified.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 6,
      "statement": "An analytic subset of a complex manifold is a locally finite union of global irreducible analytic components (Demailly II.5.3).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/7",
          "statement": "An analytic subset of a complex manifold is a locally finite union of global irreducible analytic components (Demailly II.5.3).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "locally finite family",
          "premise": 6
        }
      ],
      "root_logical_application": "DemaillyII.5.3 applies to the global analytic upperlevel subset of compact X. Locally finite global irreducible components are finite by compactness. Their analytic intersections cover the connected inner hypersurface. A finite union of proper analytic subsets cannot cover it; one contains an open portion, hence the whole inner hypersurface by the identity principle.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 7,
      "statement": "On a compact complex n-fold there exists a smooth strictly positive real (n−1,n−1) form killed by dd^c (Lamari, Proposition 1.3).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/8",
          "statement": "On a compact complex n-fold there exists a smooth strictly positive real (n−1,n−1) form killed by dd^c (Lamari, Proposition 1.3).",
          "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
          "quote": "dd° -fermées.",
          "premise": 7
        }
      ],
      "root_logical_application": "Lamari1.3 gives strict smooth ddclosed complementary tests in every compact dimensionn>=2; positive omega trace supplies actual normalization.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 8,
      "statement": "For a compact complex n-fold X and smooth real (1,1) form b, nonnegative pairing with every smooth strictly positive real dd^c-closed (n−1,n−1) form implies the existence of a real distribution q with b+dd^c q≥0, without any d-closedness hypothesis on b (Lamari, Lemma 3.3).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/9",
          "statement": "For a compact complex n-fold X and smooth real (1,1) form b, nonnegative pairing with every smooth strictly positive real dd^c-closed (n−1,n−1) form implies the existence of a real distribution q with b+dd^c q≥0, without any d-closedness hypothesis on b (Lamari, Lemma 3.3).",
          "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
          "quote": "formes strictement positives",
          "premise": 8
        }
      ],
      "root_logical_application": "Lamari3.3 applies to the actual smooth real omega-kappa Bdelta, with all positive ddclosed complementary pairings nonnegative and indeed strict. It requires no closedness. The resulting distribution is corrected locally and recovered canonically.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 9,
      "statement": "On a compact complex n-fold, the Lamari criterion applies to an arbitrary smooth real (1,1) form b, including a nonclosed one: strictly positive pairing with every smooth strictly positive real dd^c-closed complementary form yields a real distribution q such that b+dd^c q≥0 (Lamari, Lemma 3.3).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/10",
          "statement": "On a compact complex n-fold, the Lamari criterion applies to an arbitrary smooth real (1,1) form b, including a nonclosed one: strictly positive pairing with every smooth strictly positive real dd^c-closed complementary form yields a real distribution q such that b+dd^c q≥0 (Lamari, Lemma 3.3).",
          "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
          "quote": "AT est positif.",
          "premise": 9
        }
      ],
      "root_logical_application": "Lamari3.3 applies to the actual smooth real omega-kappa Bdelta, with all positive ddclosed complementary pairings nonnegative and indeed strict. It requires no closedness. The resulting distribution is corrected locally and recovered canonically.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 10,
      "statement": "On a compact complex n-fold X, Lamari's Lemma 3.3 concerns smooth real (1,1) forms without requiring them to be d-closed.",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/11",
          "statement": "On a compact complex n-fold X, Lamari's Lemma 3.3 concerns smooth real (1,1) forms without requiring them to be d-closed.",
          "url": "https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf",
          "quote": "Soit 6 une (1,1) -forme.",
          "premise": 10
        }
      ],
      "root_logical_application": "Lamari3.3 applies to the actual smooth real omega-kappa Bdelta, with all positive ddclosed complementary pairings nonnegative and indeed strict. It requires no closedness. The resulting distribution is corrected locally and recovered canonically.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 11,
      "statement": "A real distribution on Ω⊂C^n whose complex Hessian is positive has a unique locally integrable genuine plurisubharmonic representative, obtained by decreasing radial convolution regularization (Demailly I.4.20, I.5.8).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/12",
          "statement": "A real distribution on Ω⊂C^n whose complex Hessian is positive has a unique locally integrable genuine plurisubharmonic representative, obtained by decreasing radial convolution regularization (Demailly I.4.20, I.5.8).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "u ∈ Psh(Ω) locally integrable",
          "premise": 11
        }
      ],
      "root_logical_application": "Demailly canonical distribution representative and decreasing radial convolution concern only genuinely positive local complex Hessians after a fixed positive quadratic. Almost-everywhere equality gives pointwise agreement of the genuine corrected representatives.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 12,
      "statement": "On Ω⊂C^n, the cone Psh(Ω)∩L¹_loc(Ω) is closed in L¹_loc(Ω), and every bounded subset in the L¹_loc topology is relatively compact (Demailly I.5.9).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/13",
          "statement": "On Ω⊂C^n, the cone Psh(Ω)∩L¹_loc(Ω) is closed in L¹_loc(Ω), and every bounded subset in the L¹_loc topology is relatively compact (Demailly I.5.9).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "every bounded subset is relatively compact.",
          "premise": 12
        }
      ],
      "root_logical_application": "Local psh compactness is used after explicit finite inner/outer ball submean and connected positive-volume overlap propagation of a uniform L1 bound. Sup normalization prevents the minus-infinity alternative; the compactness theorem itself is an imported standard foundation.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 13,
      "statement": "For closed positive currents, geometric Lelong numbers are invariant under coordinate changes, unchanged by smooth-current additions when the resulting currents are positive and closed, and equal to one for the integration current of a smooth hypersurface at its smooth points (Demailly III.5.9, III.7.2).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/14",
          "statement": "For closed positive currents, geometric Lelong numbers are invariant under coordinate changes, unchanged by smooth-current additions when the resulting currents are positive and closed, and equal to one for the integration current of a smooth hypersurface at its smooth points (Demailly III.5.9, III.7.2).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "independent of the choice",
          "premise": 13
        },
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/15",
          "statement": "For closed positive currents, geometric Lelong numbers are invariant under coordinate changes, unchanged by smooth-current additions when the resulting currents are positive and closed, and equal to one for the integration current of a smooth hypersurface at its smooth points (Demailly III.5.9, III.7.2).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "1 when",
          "premise": 13
        }
      ],
      "root_logical_application": "The limit local closed positive ddc(v+rho) dominates kappa[H] where chi=1. Smooth H has geometric Lelong number1, and III.7.1 with its III.7.2 corollary supplies coordinate invariance. Smooth differences have normalized trace O(r^2), so the same Lelong function glues independently of correction.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 14,
      "statement": "For a closed positive current T of bidimension (p,p) on a complex manifold, the sets {x:ν(T,x)≥c}, c>0, are analytic and have dimension at most p (Demailly III.8.5).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/16",
          "statement": "For a closed positive current T of bidimension (p,p) on a complex manifold, the sets {x:ν(T,x)≥c}, c>0, are analytic and have dimension at most p (Demailly III.8.5).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "analytic subsets of dimension",
          "premise": 14
        }
      ],
      "root_logical_application": "III.8.5 applies only to the actual local CLOSED positive current of bidimension(n-1,n-1), and gives analytic upperlevel dimension<=n-1. The inherited Siu theorem is credited and not recursively newly certified.",
      "mathematically_matches_indexed_premise": true
    },
    {
      "premise_index": 15,
      "statement": "Every analytic subset of a complex manifold admits a locally finite family of global irreducible analytic components whose union is the subset (Demailly II.5.3).",
      "passages": [
        {
          "id": "82c7a934-88f4-422f-bb7e-5d9a23154dc5/17",
          "statement": "Every analytic subset of a complex manifold admits a locally finite family of global irreducible analytic components whose union is the subset (Demailly II.5.3).",
          "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
          "quote": "locally finite family",
          "premise": 15
        }
      ],
      "root_logical_application": "DemaillyII.5.3 applies to the global analytic upperlevel subset of compact X. Locally finite global irreducible components are finite by compactness. Their analytic intersections cover the connected inner hypersurface. A finite union of proper analytic subsets cannot cover it; one contains an open portion, hence the whole inner hypersurface by the identity principle.",
      "mathematically_matches_indexed_premise": true
    }
  ],
  "prior_complete_primary_root_read_record": "checks/P11-divisor-free-concentration-and-radial-tests-20261008-exact-primary-applications.pending.json",
  "additional_primary_complete_ranges_actually_root_read": {
    "Demailly": [
      [
        5430,
        5635
      ],
      [
        9070,
        9180
      ]
    ]
  },
  "correct_locators": [
    "III.7.2 is coordinate-invariance corollary",
    "III.8.5 is the Siu analyticity corollary",
    "II.5.3 is global-component theorem with its complete printed proof"
  ],
  "immutable_report_narrative_metadata_discrepancy": "The report mentions a task passage with index-1, but its actual18 structured passages all have valid nonnegative indices into16 premises. No negative-index passage exists in this payload. All18 actual bindings were assessed; the prose is preserved unchanged.",
  "root_mathematical_assessment": "The all-test transverse concentration implication holds for arbitrary nonclosed omega, and the divisor-free divergence follows by excluding every bounded subsequence. The canonical compactness and gluing steps have actual complete proofs; the global-component step is valid with the accepted open-portion wording now made explicit. The full-chart effective Cartier hypothesis supplies actual uniform smooth regularizations and every-test Stokes domination. All radial affine family classification, root, fixed degree and sharp volume/equality calculations are exact, with nonconstant g allowed. Neither these nor the preserved earlier private proof constructs K3 mass collapse or solves the full nonzero-Chern-class question. Every actual external binding has the matching exact hypotheses; no short quotation, old verdict or private native artifact is used as a source substitute.",
  "original_full_INCONCLUSIVE_preserved": true,
  "mathematical_acceptance": false,
  "independent_statement_only_reconstruction_pending": true,
  "original_P11_completed": false,
  "published": false,
  "current_native_stdout_or_private_artifacts_read": false,
  "historical_accidental_raw_search_boundary_disclosed": true,
  "recursive_certification_of_all_imported_foundations_claimed": false
}


# Exact author-source component clarification

{
  "recorded_at_utc": "2026-10-08T14:14:08.946915+00:00",
  "reviewed_source_sha256": "f25cbc9efdda3feee5d56637aee54772b30d36111af5879eab9dc2758c4f9126",
  "current_source_sha256": "be049492e7336afe8815d7fdfc038e2769c1a62a36a3b6b466a3db5b36fd5516",
  "only_full_review_accepted_component_argument_and_exact_citation_clarifications": true,
  "no_target_or_hypothesis_changed": true,
  "original_P11_completed": false,
  "exact_diff": "--- reviewed-source.tex\n+++ clarified-source.tex\n@@ -111,12 +111,13 @@\n \\cite[III.8.5]{Demailly} gives an analytic Lelong upperlevel set of\n complex dimension at most $n-1$. Smooth changes of $\\rho$ have zero\n Lelong number, so these local upperlevel sets agree on overlaps and\n-form a global proper analytic set. It contains the inner hypersurface,\n-and therefore has an analytic hypersurface component containing it.\n-Indeed locally intersect with the connected smooth inner hypersurface:\n-a proper analytic subset cannot contain an open subset of it. The\n-hypersurface component meeting that open subset contains the whole inner\n-polydisk by the identity principle.\n+form a global proper analytic set. It contains the inner hypersurface. By \\cite[II.5.3]{Demailly},\n+this compact analytic set has finitely many global irreducible components.\n+Their intersections with the connected smooth inner hypersurface are\n+analytic subsets covering it. A finite union of proper analytic subsets\n+cannot cover an open polydisk. One component therefore contains an open\n+portion and, by the identity principle, the entire inner hypersurface.\n+Its dimension is $n-1$, so it is a global analytic hypersurface.\n \n If $X$ has no analytic hypersurfaces, no bounded subsequence can exist.\n Since $C_\\delta\\geq0$ is finite for each $\\delta$, this is exactly the\n@@ -254,7 +255,7 @@\n Proposition 1.3 and Lemma 3.3.\n \\href{https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf}{Published primary text}.\n \\bibitem{Demailly} J.-P.~Demailly, \\emph{Complex Analytic and Differential\n-Geometry}, I.5.8--5.9 and III.8.5.\n+Geometry}, I.5.8--5.9, II.5.3, III.7.2 and III.8.5.\n \\href{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf}{University-hosted primary text}.\n \\end{thebibliography}\n \\end{document}\n"
}


# Complete additional Demailly primary context, lines5430--5635

(4.30)                    IA,x = f ∈ OM,x ; δα f ∈ (G1,x , . . . , GN,x ) .
This implies that the sheaf IA is the projection on the first factor of the sheaf of relations
R(δα, G1 , . . . , GN ) ⊂ ON+1
                           ∆   , which is coherent by the Oka theorem; Theorem 4.29 then
follows.
   We first prove that the inclusion IA,x ⊃ {. . .} holds in (4.30). In fact, if δα f ∈
(G1,x , . . . , GN,x ), then f vanishes on A r {δα = 0} in some neighborhood of x. Since
(A ∩ ∆) r {δα = 0} is dense in A ∩ ∆, we conclude that f ∈ IA,x .
    To prove the other inclusion IA,x ⊂ {. . .}, we repeat the proof of Lemma 4.18 with
a few modifications. Let x ∈ ∆ be a given point. At x, the irreducible polynomials
Wu (z ′ ; T ) and Wk (z ′ ; T ) of ũ and z̃k in OM,0 /IA,0 split into
                                                                               
                   Wu (z ′ ; T ) = Wu,x z ′ ; T − u(x′′ ) Qu,x z ′ ; T − u(x′′ ) ,
                    Wk (z ′ ; T ) = Wk,x (z ′ ; T − xk ) Qk,x (z ′ ; T − xk ),
100                                 Chapter II. Coherent Sheaves and Analytic Spaces

where Wu,x (z ′ ; T ) and Wk,x (z ′ ; T ) are Weierstrass polynomials in T and Qu,x (x′ , 0) 6= 0,
Qk,x (x′ , 0) 6= 0. For all z ′ ∈ ∆′ , the roots of Wu (z ′ ; T ) are the values u(z ′′ ) at all points
z ∈ A ∩ π −1 (z ′ ). As A is closed, any point z ∈ A ∩ π −1 (z ′ ) with z ′ near x′ has to be in a
small neighborhood of one of the points y ∈ A ∩ π −1 (x′ ). Choose cd+1 , . . . , cn such that
the linear form u(z ′′ ) separates all points in the fiber A ∩ π −1 (x′ ). Then, for a root u(z ′′ )
of Wu,x z ′ ; T − u(x′′ ) , the point z must be in a neighborhood of y = x, otherwise u(z ′′ )
would be near u(y ′′ ) 6= u(x′′ ) and the Weierstrass polynomial Wu,x (z ′ ; T ) would have a
root away from 0, in contradiction          with (4.10). Conversely, if z ∈ A ∩ π −1 (z ′ ) is near
x, then Qu,x z ; u(z ) − u(x ) 6= 0 and u(z ′′ ) is a root of Wu,x z ′ ; T − u(x′′ ) . From
                   ′    ′′           ′′

this, we infer that every polynomial P (z ′ ; T ) ∈ O∆′ ,x′ [T ] such that P z ′ ; u(z ′′ ) = 0 on
(A, x) is a multiple of Wu,x z ′ ; T − u(x′′ ) , because the roots of the latter polynomial
are simple for z ′ in the dense set (∆′ r S, x). In particular deg P < deg Wu,x implies
P = 0 and                                                                          
                              δ(z ′ )q Wk,x z ′ ; Bk (z ′ ; u(z ′′ ))/δ(z ′ ) − xk
                                          
is a multiple of Wu,x z ′ ; T −u(x′′ ) . If we replace Wu , Wk by Wu,x , Wk,x respectively, the
proof of Lemma 4.18 shows that for every f ∈ OM,x there is a polynomial R ∈ O∆′ ,x′ [T ]
of degree deg R < deg Wu,x such that
                                                       
                     δ(z ′ )m f (z) = R z ′ ; u(z ′′ )       modulo the ideal
                                                                                    
                       Wu,x z ′ ; u(z ′′ ) − u(x′′ ) , δ(z ′ )zk − Bk z ′ ; u(z ′′ ) ,
and f ∈ IA,x implies R = 0. Since Wu,x differs from Wu only by an invertible element
in OM,x , we conclude that
                     X         
                           δα cα IA,x = δ m IA,x ⊂ (G1,x , . . . , GN,x ).

This is true for a dense open set of coefficients
                                         P        cd+1 , . . . , cn , therefore by expressing the
coefficients δα through interpolation of    δα cα at suitable points c we infer
                             δα IA,x ⊂ (G1,x , . . . , GN,x )     for all α.                          

(4.31) Theorem. Asing is an analytic subset of A.
Proof. The statement is local. Assume first that (A, 0) is an irreducible germ in Cn . Let
g1 , . . . , gN be generators of the sheaf IA on a neighborhood Ω of 0. Set d = dim A. In a
neighborhood of every point x ∈ Areg ∩ Ω, A can be defined by holomorphic equations
u1 (z) = . . . = un−d (z) = 0 such that du1 , . . . , dun−d are linearly independant. As
u1 , . . . , un−d are generated by g1 , . . . , gN , one can extract a subfamily gj1 , . . . , gjn−d that
has at least one non zero Jacobian determinant of rank n − d at x. Therefore Asing ∩ Ω
is defined by the equations
                ∂g 
                   j
          det         j∈J = 0,    J ⊂ {1, . . . , N }, K ⊂ {1, . . . , n}, |J| = |K| = n − d.
                 ∂zk k∈K
                                  S
Assume now that (A, 0) = (Al , 0) with (Al , 0) irreducible. The germ of an analytic
set at a regular point is irreducible, thus every point which belongs simultaneously to at
least two components is singular. Hence
                                          [                  [
                           (Asing , 0) = (Al,sing , 0) ∪        (Ak ∩ Al , 0),
                                                           k6=l
                           § 5. Complex Spaces                                                  101

and Asing is analytic.                                                                           

   Now, we give a characterization of regular points in terms of a simple algebraic pro-
perty of the ring OA,x .

(4.32) Proposition. Let (A, x) be a germ of analytic set of dimension d and let mA,x ⊂
OA,x be the maximal ideal of functions that vanish at x. Then mA,x cannot have less
than d generators and mA,x has d generators if and only if x is a regular point.

Proof. If A ⊂ Cn is a d-dimensional submanifold in a neighborhood of x, there are local
coordinates centered at x such that A is given by the equations zd+1 = . . . = zn near
z = 0. Then OA,x ≃ Od and mA,x is generated by z1 , . . . , zd . Conversely, assume that
mA,x has s generators g1 (z), . . . , gs (z) in OA,x = OCn ,x /IA,x . Letting x = 0 for simplicity,
we can write
                   X
           zj =           ujk (z)gk (z) + fj (z),   ujk ∈ On , fj ∈ IA,0 , 1 ⩽ j ⩽ n.
                  1⩽k⩽s

                     P
Then we  find dzj =    cjk (0)dgk (0)+dfj (0), so that the rank of the system of differentials
 dfj (0) 1⩽j⩽n is at least equal to n − s. Assume for example that df1 (0), . . . , dfn−s (0)
are linearly independent. By the implicit function theorem, the equations f1 (z) = . . . =
fn−s (z) = 0 define a germ of submanifold of dimension s containing (A, 0), thus s ⩾ d
and (A, 0) equals this submanifold if s = d.                                                 

(4.33) Corollary. Let A ⊂ M be an analytic set of pure dimension d and let B ⊂ A
be an analytic subset of codimension ⩾ p in A. Then, as an OA,x -module, the ideal IB,x
cannot be generated by less than p generators at any point x ∈ B, and by less than p + 1
generators at any point x ∈ Breg ∩ Asing .

Proof. Suppose that IB,x admits s-generators (g1 , . . . , gs ) at x. By coherence of IB
these germs also generate IB in a neighborhood of x, so we may assume that x is a
regular point of B. Then there are local coordinates (z1 , . . . , zn ) on M centered at x
such that (B, x) is defined by zk+1 = . . . = zn = 0, where k = dim(B, x). Then the
maximal ideal mB,x = mA,x /IB,x is generated by z1 , . . . , zk , so that mA,x is generated
by (z1 , . . . , zk , g1 , . . . , gs ). By Prop. 4.32, we get k + s ⩾ d, thus s ⩾ d − k ⩾ p, and we
have strict inequalities when x ∈ Asing .                                                          


§ 5. Complex Spaces
    Much in the same way a manifold is constructed by piecing together open patches
isomorphic to open sets in a vector space, a complex space is obtained by gluing together
open patches isomorphic to analytic subsets. The general concept of analytic morphism
(or holomorphic map between analytic sets) is first needed.
§ 5.1. Morphisms and Comorphisms
    Let A ⊂ Ω ⊂ Cn and B ⊂ Ω′ ⊂ Cp be analytic sets. A morphism from A to B is by
definition a map F : A −→ B such that for every x ∈ A there is a neighborhood U of x
and a holomorphic map F̃ : U −→ Cp such that F̃↾A∩U = F↾A∩U . Equivalently, such a
102                            Chapter II. Coherent Sheaves and Analytic Spaces

morphism can be defined as a continuous map F : A −→ B such that for all x ∈ A and
g ∈ OB,F (x) we have g ◦ F ∈ OA,x . The induced ring morphism
(5.1)                      Fx⋆ :   OB,F (x) ∋ g 7−→ g ◦ F ∈ OA,x
is called the comorphism of F at point x.
§ 5.1. Definition of Complex Spaces

(5.2) Definition. A complex space X is a locally compact Hausdorff space, countable
at infinity, together with a sheaf OX of continuous functions on X, such that there exists
an open covering (Uλ ) of X and for each λ a homeomorphism Fλ : Uλ −→ Aλ onto
an analytic set Aλ ⊂ Ωλ ⊂ Cnλ such that the comorphism Fλ⋆ : OAλ −→ OX ↾Uλ is an
isomorphism of sheaves of rings. OX is called the structure sheaf of X.

   By definition a complex space X is locally isomorphic to an analytic set, so the
concepts of holomorphic function on X, of analytic subset, of analytic morphism, etc . . .
are meaningful. If X is a complex space, Th. 4.31 implies that Xsing is an analytic subset
of X.

(5.3) Theorem and definition. For every complex space X, the set Xreg is a dense
open subset of X, and consists of a disjoint union of connected complex manifolds Xα′ .
Let Xα be the closure
                S     of Xα′ in X. Then (Xα ) is a locally finite family of analytic subsets
of X, and X = Xα . The sets Xα are called the global irreducible components of X.



                                                       Γ

                                            A1
                           (−1, 0)            (0, 0)
                                            A2




                 Fig. II-2 The irreducible curve y 2 = x2 (1 + x) in C2 .

Observe that the germ at a given point of a global irreducible component can be reducible,
                                                 2      2
as shows the example of the √ cubic curve Γ : y = x (1 + x) ; the germ (Γ, 0) has two
analytic branches y = ±x 1 + x, however Γ r {0} is easily seen to be a connected
smooth Riemann surface (the real points of γ corresponding to −1 ⩽ x ⩽ 0 form a path
connecting the two branches). This example shows that the notion of global irreducible
component is quite different from the notion of local irreducible component introduced
in (4.4).
Proof. By definition of Xreg , the connected components Xα′ are (disjoint) complex man-
                                               ′
ifolds. Let us show that the germ of Xα = X α at any point x ∈ X is analytic. We may
                        § 5. Complex Spaces                                                  103

assume that (X, x) is a germ of analytic set A in an open subset of Cn . Let (Al , x),
1 ⩽ l ⩽ N , be theS irreducible components of this germ and U a neighborhood of x such
that X ∩ U = Al ∩ U . Let Ωl ⊂ U be a neighborhood of x such that Al,reg ∩ Ωl
                                                                 ′
is connected and  S dense in Al ∩ Ωl (Prop. 4.24). Then Al := Xreg ∩ Al ∩ Ωl equals
(Al,reg ∩ Ωl ) r k6=l Al,reg ∩ Ωl ∩ Ak . However, Al,reg ∩ Ωl ∩ Ak is an analytic subset
of Al,reg ∩ Ωl , distinct from Al,reg ∩ Ωl , otherwise Al,reg ∩ Ωl would be contained in Ak ,
                                                                    ′
thus (Al , x) ⊂ (Ak , x) by density. Remark    T 4.2 implies that Al is connected and dense
in Al,reg ∩ Ωl , hence in Al ∩ Ωl . Set Ω = Ωl and let (Xα )α∈J be the familySof global
components which meet Ω (i.e. such that Xα′ ∩ Ω 6= ∅ ). As Xreg ∩ Ω =                    A′l ∩ Ω,
each Xα′ , α ∈ J, meets at least one set A′l , and as A′l ⊂ Xreg is connected, we have in
fact A′l ⊂ SXα′ . It follows that there exists a partition (Lα )α∈J of {1, . . . , N } such that
Xα′ ∩ Ω = l∈Lα A′l ∩ Ω, α ∈ J. Hence J is finite, card J ⩽ N , and
                                    ′         [       ′         [
                      Xα ∩ Ω = X α ∩ Ω =             Al ∩ Ω =          Al ∩ Ω
                                              l∈Lα              l∈Lα

is analytic for all α ∈ J.                                                                     

(5.4) Corollary. If A, B are analytic subsets in a complex space X, then the closure
A r B is an analytic subset, consisting of the union of all global irreducible components
Aλ of A which are not contained in B.
                 S
Proof. Let C = Aλ be the union of these S      components. Since (Aλ ) is locally finite,
C is analytic. Clearly A r B = C r B = Aλ r B. The regular part A′λ of each
Aλ is a connected manifold and A′λ ∩ B is a proper analytic subset (otherwise A′λ ⊂ B
                                ′       ′                     ′
         S Aλ ⊂ B). Thus Aλ r (Aλ ∩ B) is dense in Aλ which is dense in Aλ , so
would imply
A r B = Aλ = C.                                                                        



# Complete additional Demailly primary context, lines9070--9180

                                                ϕ(z)<t

and the Fubini theorem gives
             Z r                     ZZ
                      c
                  ν(dd V, ϕ, t) dt =            ddc V (z) ∧ (ddc ϕ(z))n−1 dt
              −∞                       ϕ(z)<t<r
                                     Z
(6.6)                              =      (r − ϕ)ddc V ∧ (ddc ϕ)n−1 .
                                              B(r)

We first show that Formula 6.5 is true when ϕ and V are smooth. As both members
of the formula are left continuous with respect to r and as almost all values of ϕ are
non critical by Sard’s theorem, we may assume r non critical. Formula 3.1 applied with
f = (r − ϕ)(ddc ϕ)n−1 and g = V shows that integral (6.6) is equal to
         Z                         Z                          Z
                    c   n−1   c              c   n
               V (dd ϕ)     ∧d ϕ−       V (dd ϕ) = µr (V ) −        V (ddc ϕ)n .
          S(r)                               B(r)                               B(r)

Formula 6.5 is thus proved when ϕ and V are smooth. If V is smooth and ϕ merely
continuous and finite, one can write ϕ = lim ϕk where ϕk is a decreasing sequence
of smooth plurisubharmonic functions (because X is Stein). Then ddc V ∧ (ddc ϕk )n−1
converges weakly to ddc V ∧(ddc ϕ)n−1 and (6.6) converges, since 1lB(r) (r−ϕ) is continuous
with compact support on X. The left hand side of Formula 6.5 also converges because
the definition of µr implies
                          Z                 Z
                                   c    n
                                                                             
              µk,r (V ) −     V (dd ϕk ) =      V (ddc ϕk,⩾r )n − (ddc ϕk )n
                          ϕk <r                          X
164                                Chapter III. Positive Currents and Lelong Numbers

and we can apply again weak convergence on a neighborhood of B(r).    R If ϕ takes −∞
values, replace ϕ by ϕ⩾−k where k → +∞. Then µr (V ) is unchanged, B(r) V (ddc ϕ⩾−k )n
               R
converges to B(r) V (ddc ϕ)n and the right hand side of Formula 6.5 is replaced by
Rr
 −k
    ν(ddc V, ϕ, t) dt. Finally, for V arbitrary, write V = lim ↓ Vk with a sequence of
smooth functions Vk . Then ddc Vk ∧ (ddc ϕ)n−1 converges weakly to ddc V ∧ (ddc ϕ)n−1 by
Prop. 4.4, so the integral (6.6) converges to the expected limit and the same is true for
the left hand side of 6.5 by the monotone convergence theorem.                         

      For r < r0 < R, the Jensen-Lelong formula implies
                                      Z                                    Z r
                                                                 c    n
(6.7)          µr (V ) − µr0 (V ) +                     V (dd ϕ) =                  ν(ddc V, ϕ, t) dt.
                                          B(r0 )\B(r)                          r0


(6.8) Corollary. Assume that (ddc ϕ)n = 0 on X \S(−∞). Then r 7→ µr (V ) is a convex
increasing function of r and the lelong number ν(ddc V, ϕ) is given by

                                                             µr (V )
                                   ν(ddc V, ϕ) = lim                 .
                                                        r→−∞    r


Proof. By (6.7) we have
                                                        Z r
                              µr (V ) = µr0 (V ) +               ν(ddc V, ϕ, t) dt.
                                                            r0


As ν(ddc V, ϕ, t) is increasing and nonnegative, it follows that r 7−→ µr (V ) is convex and
increasing. The formula for ν(ddc V, ϕ) = limt→−∞ ν(ddc V, ϕ, t) is then obvious.          

(6.9) Example. Let X be an open subset of Cn equipped with the semi-exhaustive
function ϕ(z) = log |z − a|, a ∈ X. Then (ddc ϕ)n = δa and the Jensen-Lelong formula
becomes                                    Z r
                         µr (V ) = V (a) +     ν(ddc V, ϕ, t) dt.
                                                        −∞

As µr is the mean value measure on the sphere S(a, er ), we make the change of variables
r 7→ log r, t 7→ log t and obtain the more familiar formula
                                                             Z r
                                                                                       dt
(6.9 a)                  µ(V, S(a, r)) = V (a) +                     ν(ddc V, a, t)
                                                                 0                     t

where ν(ddc V, a, t) = ν(ddc V, ϕ, log t) is given by (5.7):
                                                                          Z
                          c                             1                             1
(6.9 b)              ν(dd V, a, t) =                                                    ∆V.
                                           π n−1 t2n−2 /(n − 1)!              B(a,t) 2π


In this setting, Cor. 6.8 implies
                                                   
                          c           µ V, S(a, r)         supS(a,r) V
(6.9 c)              ν(dd V, a) = lim                = lim             .
                                  r→0    log r         r→0    log r
                       § 6. The Jensen-Lelong Formula                                                   165

To prove the last equality, we may assume V ⩽ 0 after subtraction of a constant. In-
equality ⩾ follows from the obvious estimate µ(V, S(a, r)) ⩽ supS(a,r) V , while inequality
⩽ follows from the standard Harnack estimate
                                                  1−ε                   
(6.9 d)                          sup V ⩽                   µ V, S(a, r)
                                S(a,εr)        (1 + ε)2n−1

when ε is small (this estimate follows easily from the Green-Riesz representation formula
1.4.6 and 1.4.7). As supS(a,r) V = supB(a,r) V , Formula (6.9 c) can also be rewritten
ν(ddc V, a) = lim inf z→a V (z)/ log |z − a|. Since supS(a,r) V is a convex (increasing) func-
tion of log r, we infer that

(6.9 e)                              V (z) ⩽ γ log |z − a| + O(1)


