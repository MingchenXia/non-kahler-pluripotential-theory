# P05: checked divergence and conformal-gauge results

For one compact Chern--Ricci-flat strictly LCK metric, the integrated squared anti-J-invariant Lee derivative equals half the integrated squared Lee divergence. Gauduchon, zero Lee divergence, holomorphic Lee dual and Vaisman are equivalent for that metric. Ordinary Bott--Chern vanishing gives a unique flat conformal gauge up to scale. An explicit fixed Kodaira surface has a flat strict LCK gauge whose conformal class contains no flat Gauduchon representative, while the same complex surface has an explicit Vaisman metric. The arbitrary same-complex-manifold existence question remains unresolved.

The fresh original exploration returned seven complete ordinary notes without claiming original completion. Complete original-task review returned INCONCLUSIVE. A fresh statement-only reconstruction with notes=[] returned five complete proofs, including a distinct exterior-Stokes derivation. Separate scoped final comparison returned PASS. Root read the complete article, all generated proofs, all reports and their exact source applications and compared both full integral derivations. All calls used Xean gpt-6.1-sol xhigh, concurrency one, without arbitrary time or call caps. No full-solver accepted-note graph or original-task closure is asserted.

The final scoped argument has no indispensable external premises: its local connection, Ricci, Bianchi, Bochner and explicit quotient calculations are reconstructed. BO v2 Theorem A requires Gauduchon and flatness of the same metric; its Section4 formulas retain divergence before that specialization. The article uses them for comparison, not to remove the Gauduchon antecedent. Historical conditional finite-cover, homogeneous and potential-subclass notes and all nine deep premises remain preserved but are not accepted dependencies of this release. Historical passage14 is a task quote misbound to an external premise and remains excluded as external evidence. The rejected early integral identity and the reconstruction's failed pointwise diagnostic remain recorded. No general pointwise identity, unrestricted counterexample or priority certification is claimed. The final owner session became unavailable after an environment reset: its actual exit code is unknown, rather than inferred from PASS; its campaign is complete, all calls settled, and the exact campaign process is absent. Native editor/compile requests have no successful response on this host; the four-page PDF is verified by two clean local exports and four actual page views.

## Complete frozen comparison assembly

# Complete scoped P05 final comparison

The original full existence problem remains unresolved. All four limited metric/gauge claims must be compared through the full ordinary proofs below. No verdict, candidate flag, checksum or successful build is mathematical authority. The clarification adds only an explicit d^c definition; the prior source and PDF are frozen in the before-dc snapshot.

## Current complete article

```tex
\documentclass[11pt]{article}
\usepackage[margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newcommand{\ddc}{dd^c}
\newcommand{\Ric}{\operatorname{Ric}}
\newcommand{\vol}{\operatorname{vol}}
\newcommand{\tr}{\operatorname{tr}}
\title{Divergence, rigidity and conformal gauges\newline for Chern--Ricci-flat LCK metrics}
\author{}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{center}\small Working draft: independent mathematical review is pending.\end{center}
\begin{abstract}
For a compact Chern--Ricci-flat locally conformally K\"ahler metric,
the squared $L^2$ norm of the anti-$J$-invariant covariant derivative
of its Lee form equals half the squared norm of its divergence.
This gives equivalent Gauduchon, holomorphic-Lee and Vaisman conditions
for that metric. An explicit fixed Kodaira surface has a strictly LCK
flat conformal gauge which is not Gauduchon, and its conformal class
contains no metric satisfying both conditions. The same complex surface
has an explicit Vaisman metric. These are metric and conformal-class
results; the unrestricted existence question for an arbitrary compact
ordinary Bott--Chern Calabi--Yau LCK manifold remains unresolved.
\end{abstract}

\section{Conventions and scope}
Let $(X,J,g,\omega)$ be connected and compact, of complex dimension
$n\geq2$, with $\omega(X,Y)=g(JX,Y)$. We use
\[
 d^c=\frac{i}{4\pi}(\bar\partial-\partial),
 \qquad \ddc=\frac{i}{2\pi}\partial\bar\partial,
 \qquad J\alpha=-\alpha\circ J
\]
for real one-forms. Thus $dJdf=4\pi\ddc f$. A strictly LCK metric has
$d\omega=\vartheta\wedge\omega$ with $d\vartheta=0$ and nonexact
$\vartheta$. It is Vaisman when $\nabla\vartheta=0$. The Chern--Ricci
form is $\rho(g)=-i\partial\bar\partial\log\det(g)$; its normalized
representative $\rho(g)/(2\pi)$ represents ordinary $c_1^{\rm BC}(T_X)$.
All divergences, norms and integrals below use this same $g$.

The same-metric Gauduchon and Chern--Ricci-flat rigidity theorem is
established in \cite[Theorem A]{BO}. We retain the divergence terms
in its connection, Bianchi and Weitzenb\"ock argument. Ordinary
Bott--Chern vanishing alone does not supply a simultaneous gauge.
No theorem for an already Vaisman manifold is applied to a general
LCK manifold, and no deformation or cover replaces the given complex
structure.

\section{The integral identity and its rigidity consequences}
Set
\[
 A=\vartheta^\sharp,\quad B=JA,\quad T=\nabla\vartheta,\quad
 P(X,Y)=\tfrac12\{T(X,Y)+T(JX,JY)\},\quad T^-=T-P,
\]
\[
 q=d_g^*\vartheta=-\tr_gT,\qquad u=|\vartheta|_g^2.
\]
Closedness of $\vartheta$ makes $T$ symmetric; $P$ and $T^-$ are
orthogonal, so $|T|^2=|P|^2+|T^-|^2$.

\begin{theorem}\label{th:rigidity}
For every compact Chern--Ricci-flat strictly LCK metric,
\begin{equation}\label{eq:identity}
 \int_X|T^-|^2\,d\vol_g=\frac12\int_X|q|^2\,d\vol_g.
\end{equation}
For this fixed metric the following conditions are equivalent:
Gauduchon; $q=0$; $A$ is real holomorphic; and Vaisman.
The equality \eqref{eq:identity} is an integral identity, rather than
an asserted pointwise identity for general metrics.
\end{theorem}

\begin{proof}
Locally $\vartheta=df$ and $\widetilde g=e^{-f}g$ is K\"ahler. Its
Levi--Civita connection is
\[
 D_XY=\nabla_XY-\tfrac12\vartheta(X)Y
                 -\tfrac12\vartheta(Y)X+\tfrac12g(X,Y)A.
\]
The equation $DJ=0$ gives
\begin{equation}\label{eq:nablaJ}
 (\nabla_XJ)Y=\tfrac12\{\vartheta(JY)X-\vartheta(Y)JX
                  -g(X,JY)A+g(X,Y)JA\}.
\end{equation}
Differentiating $J\vartheta=-\vartheta\circ J$ and using symmetry of
$T$ consequently gives
\[
 dJ\vartheta(X,JY)=2P(X,Y)-u g(X,Y)
              +\vartheta(X)\vartheta(Y)+J\vartheta(X)J\vartheta(Y).
\]
Flatness and the local conformal volume change give
$\rho(\widetilde g)=n i\partial\bar\partial f=(n/2)dJ\vartheta$.
Contracting the curvature difference of $D$ and $\nabla$ gives the
real conformal Ricci formula
\[
 \Ric_D=\Ric_g+(n-1)T+\tfrac{n-1}{2}\vartheta\otimes\vartheta
                       +\tfrac12\{-q-(n-1)u\}g.
\]
The K\"ahler Ricci form of $\widetilde g$ equals its real Ricci tensor
paired with $J$. Combining these expressions yields
\begin{equation}\label{eq:Ric}
 R:=\Ric_g=nP-(n-1)T+\tfrac{q-u}{2}g
               +\tfrac12\vartheta\otimes\vartheta
               +\tfrac n2J\vartheta\otimes J\vartheta.
\end{equation}
Its trace is
$s=(n-1)q-(n-1)u/2$. The local formulas agree with
\cite[Section 4, equations (2)--(4)]{BO}; no $q=0$ hypothesis has
been inserted into \eqref{eq:Ric}.

Write $\|\cdot\|$ for the $L^2$ norm and put
$E_A=\int_XT(A,A)d\vol_g$, $E_B=\int_XT(B,B)d\vol_g$.
Since $T(A,A)=A(u)/2$ and $\operatorname{div}A=-q$,
\begin{equation}\label{eq:uq}
 \int_Xuq\,d\vol_g=2E_A.
\end{equation}
Pair the contracted Bianchi identity
$\delta R+ds/2=0$ with $\vartheta$ and integrate. Here $\delta$ is
minus covariant contraction, adjoint to symmetric covariant derivative.
It gives $\int\langle R,T\rangle+\frac12\int s q=0$.
Substitution of \eqref{eq:Ric} and \eqref{eq:uq} gives
\begin{equation}\label{eq:Bianchi}
 0=n\|P\|^2-(n-1)\|T\|^2+\tfrac{n-2}{2}\|q\|^2
                    +\tfrac{4-n}{2}E_A+\tfrac n2E_B.
\end{equation}
The integrated Weitzenb\"ock identity for a closed one-form gives
\[
 \|q\|^2=\|T\|^2+\int_XR(A,A)\,d\vol_g.
\]
Equation \eqref{eq:Ric} has
$R(A,A)=(1-n/2)T(A,A)+(n/2)T(B,B)+qu/2$; hence
\begin{equation}\label{eq:Bochner}
 \|q\|^2=\|T\|^2+\tfrac{4-n}{2}E_A+\tfrac n2E_B.
\end{equation}
Eliminating $E_A,E_B$ between \eqref{eq:Bianchi} and
\eqref{eq:Bochner} proves \eqref{eq:identity}.

For the Gauduchon equivalence, the LCK equation and the Hodge identity
$*\vartheta=J\vartheta\wedge\omega^{n-1}/(n-1)!$ give
\[
 d^c\omega^{n-1}=\frac{n-1}{4\pi}
                       J\vartheta\wedge\omega^{n-1},\qquad
 \ddc\omega^{n-1}=-\frac{n-1}{4\pi n}q\,\omega^n.
\]
Thus Gauduchon is exactly $q=0$. In this case \eqref{eq:identity}
forces $T=P$, so $T(B,B)=T(A,A)$. Equation \eqref{eq:uq} gives
$E_A=E_B=0$, and \eqref{eq:Bochner} forces $T=0$.

Equation \eqref{eq:nablaJ} gives $\nabla_AJ=0$. Let $S$ be the
symmetric endomorphism with $g(SX,Y)=T(X,Y)$. Then
\[
 (\mathcal L_AJ)Y=JSY-SJY.
\]
Consequently $A$ is real holomorphic exactly when $T=P$.
Equation \eqref{eq:identity} then gives $q=0$, hence $T=0$.
Conversely $T=0$ gives both other conditions. Under strictness the
parallel Lee form is nonzero, as required for Vaisman.
\end{proof}

\section{An explicit compact example with incompatible gauges}
\begin{proposition}\label{prop:example}
On one fixed compact complex Kodaira surface there is a strictly LCK
Chern--Ricci-flat metric which is not Gauduchon. Its conformal class
contains no simultaneously Gauduchon and Chern--Ricci-flat metric.
The same surface has an explicit Vaisman metric, so this is not a
counterexample to the unrestricted P05 existence question.
\end{proposition}

\begin{proof}
On $G=\mathbb R^4$ use the multiplication
\[
 (x,y,z,t)(x',y',z',t')=(x+x',y+y',z+z'+xy',t+t').
\]
The integer subgroup $\Gamma=\mathbb Z^4$ is a lattice: its left
action is $(x,y,z,t)\mapsto(x+a,y+b,z+c+ay,t+d)$.
Reduction of $x,y,t$ and then $z$ to unit intervals supplies a compact
fundamental set. Thus $X=\Gamma\backslash G$ is connected and compact.
The global forms
\[
 e^1=dx,\quad e^2=dy,\quad e^3=dz-xdy,\quad e^4=dt
\]
have $de^3=-e^{12}$ and the other derivatives zero. Declare
$\phi^1=e^1+i e^2$, $\phi^2=e^3+i e^4$ to be of type $(1,0)$.
Then $d\phi^1=0$ and
$d\phi^2=-(i/2)\phi^1\wedge\overline{\phi^1}$ have no $(0,2)$
part, so the complex structure is integrable.
$\Sigma=\phi^1\wedge\phi^2$ is closed and nowhere vanishing,
hence holomorphic. The canonical bundle is holomorphically trivial,
which proves ordinary $c_1^{\rm BC}(T_X)=0$.

Take a unit-periodic $f(x)$ with $C=1-f''>0$, and set
\[
 \vartheta_1=-e^4+f'e^1,\quad \eta_1=J\vartheta_1=e^3+f'e^2,
 \quad \omega_1=\vartheta_1\wedge\eta_1+C e^{12}.
\]
This is the positive Hermitian form of
$g_1=\vartheta_1^2+\eta_1^2+C\{(e^1)^2+(e^2)^2\}$.
One has $d\vartheta_1=0$, $d\eta_1=-C e^{12}$ and
$d\omega_1=\vartheta_1\wedge\omega_1$.
The $t$-circle has Lee period $-1$, so the metric is strict.
Its Lee dual is $-\partial_t$. All coefficients are independent of
$t$, making this field Killing; closedness of $\vartheta_1$ makes
$\nabla\vartheta_1$ symmetric and Killing makes it skew. Thus $g_1$
is Vaisman on this fixed complex manifold.

Its volume is $\omega_1^2/2=C e^{1234}$, while
$\Sigma\wedge\overline\Sigma$ has constant density in $e^{1234}$.
Put $h=C^{-1/2}$ and $\omega=h\omega_1$. Then
$\omega^2/2=e^{1234}$, so its Chern--Ricci form is zero. Its Lee form
is $\vartheta=-e^4+d(f+\log h)$, retaining period $-1$.
If $E_i$ are dual to $e^i$, its Lee dual is
\[
 A=h'E_1+(f'h'-h^{-1})E_4.
\]
The metric volume is $dx\,dy\,dz\,dt$. Each $E_i$ has zero
divergence in this volume, hence $\operatorname{div}A=h''$ and
$q=d_g^*\vartheta=-h''$.

For the explicit choice
\[
 f(x)=\frac{\cos(2\pi x)}{16\pi^2},\qquad
 C(x)=1+\tfrac14\cos(2\pi x)\geq\tfrac34,
\]
direct differentiation gives
\[
 q(0)=-\frac{4\sqrt5\pi^2}{25},\qquad
 q(1/2)=\frac{4\sqrt3\pi^2}{9}.
\]
Thus $\omega$ is not Gauduchon, and Theorem~\ref{th:rigidity}
also shows it is not Vaisman.

For any global real $v$,
$\rho(e^v\omega)=\rho(\omega)-n i\partial\bar\partial v$.
Two flat metrics in a single conformal class therefore have a real
pluriharmonic logarithmic ratio, constant on a connected compact
complex manifold by the maximum principle. The only flat metrics
conformal to $\omega$ are its positive constant multiples; constant
scaling cannot make its nonzero $q$ vanish. This proves the asserted
obstruction. The already exhibited $\omega_1$ is a Vaisman and
Gauduchon representative in that class, with generally nonzero
Chern--Ricci form.
\end{proof}

\section{The remaining existence question}
If ordinary $c_1^{\rm BC}(T_X)=0$, write
$\rho(\omega)/(2\pi)=\ddc F$ for a global smooth $F$.
Then $e^{F/n}\omega$ is Chern--Ricci flat and its Lee form is
$\vartheta+dF/n$, still nonexact. This proves existence and
uniqueness up to scale of the flat conformal gauge, rather than
existence of a metric with $q=0$ in it. The explicit example
shows why these assertions cannot be combined with the separate
Gauduchon conformal theorem to supply the same-metric rigidity
hypothesis. It supplies no obstruction to all Vaisman metrics on
$X$, and the arbitrary same-complex-manifold existence problem
remains open in this argument. Independent review, reconstruction,
source assessment and final comparison are pending for this draft.
\begin{thebibliography}{9}
\bibitem{BO} G. Barbaro and A. Otiman,
\emph{Calabi--Yau locally conformally K\"ahler manifolds},
\href{https://arxiv.org/abs/2509.18364v2}{arXiv:2509.18364v2},
Theorem A and Section 4.
\end{thebibliography}
\end{document}
```


## Entire preserved original-task full-review argument

This is the prior whole argument, including the pre-clarification article and ALL seven original exploration notes. Erroneous n3 reasoning was rejected; conditional n4--n7 are unused article dependencies and are not accepted new results. These historical statements must not be substituted for current A--D.

# P05 exact-original review with an explicitly limited current article

The review task is the exact unchanged original P05 task. The current
article only proves A--D below; original_P05_completed is false.
Assess these limited claims and the article while retaining the full
original completion criteria. No candidate flag or earlier verdict is
mathematical authority. Do not infer original completion from a scoped
proof or from the existence of different conformal representatives.

# P05 limited flat-metric and fixed Kodaira targets

The original unrestricted P05 existence question is retained below as
context. These four limited statements do not resolve that question.
All objects here are smooth and the given complex structure is fixed.
Let X be connected compact complex of dimension n>=2. Set
ddc=i partial barpartial/(2pi), J alpha=-alpha composed with J for real
one-forms, and omega(U,V)=g(JU,V). Strict LCK means d omega=theta wedge
omega, d theta=0, and [theta]!=0. Vaisman means nabla theta=0 with
nonzero theta. Chern-Ricci flat means rho(g)=-i partial barpartial
log det(g)=0. Ordinary c1BC(TX) is the class of rho(g)/(2pi).

A. If ordinary c1BC(TX)=0, then every strictly LCK conformal class has
a Chern-Ricci-flat representative, unique up to a positive constant.
More precisely rho(omega)/(2pi)=ddc F gives the flat metric
exp(F/n)omega, with Lee form theta+dF/n still nonexact. No conclusion
that this flat representative is Gauduchon is assumed.

B. For an arbitrary compact Chern-Ricci-flat strictly LCK metric,
put A=theta sharp, T=nabla theta, P(U,V)=(T(U,V)+T(JU,JV))/2,
Tminus=T-P, and q=d*_g theta=-tr_g T. Then the actual integrated
identity is int_X |Tminus|^2 dvol_g = (1/2) int_X q^2 dvol_g.
All norms and the divergence use the same metric. Gauduchon is not
an antecedent, and no pointwise equality is asserted.

C. For that fixed flat metric the following four conditions are
equivalent: ddc omega^(n-1)=0; q=0; A is a real holomorphic vector
field; the metric is Vaisman. Separate conformal representatives do
not supply the antecedents for a same-metric rigidity theorem.

D. The following explicit data give one fixed compact complex Kodaira
surface with ordinary c1BC(TX)=0. Take G=R^4 with multiplication
(x,y,z,t)(x',y',z',t')=(x+x',y+y',z+z'+x y',t+t'), Gamma=Z^4,
and X=Gamma backslash G. The global coframe is e1=dx,e2=dy,
e3=dz-x dy,e4=dt. Declare phi1=e1+i e2 and phi2=e3+i e4 type(1,0).
Let f(x)=cos(2pi x)/(16pi^2), C=1-f''=1+cos(2pi x)/4, h=C^(-1/2),
theta1=-e4+f'e1, eta1=e3+f'e2, omega1=theta1 wedge eta1+C e1 wedge e2,
and omega=h omega1. Prove compactness, integrability, positivity,
strictness of both LCK metrics, and the ordinary Bott-Chern claim.
The metric omega1 is Vaisman on this same X. The metric omega is
Chern-Ricci flat, its Lee form is theta=-e4+d(f+log h), and its
divergence is q=-h''. In particular q(0)=-4sqrt(5)pi^2/25 and
q(1/2)=4sqrt(3)pi^2/9. Thus omega is neither Gauduchon nor Vaisman,
and its conformal class has no metric which is simultaneously
Chern-Ricci flat and Gauduchon. This is a conformal-class obstruction,
not a counterexample to the original existence question, since
omega1 is an explicit Vaisman metric on the same complex manifold.

Reconstruct all four targets from these statements and public
mathematics. No author proof, article, original-worker notes, earlier
report, private campaign material or credentials are supplied to this
blind task. Provide complete ordinary proofs, preserve failed routes,
and judge every indispensable source application with its precise
hypotheses. In particular no theorem for an already Vaisman manifold,
deformation or undescented finite cover proves original P05.

## Entire frozen current article
```latex
\documentclass[11pt]{article}
\usepackage[margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newcommand{\ddc}{dd^c}
\newcommand{\Ric}{\operatorname{Ric}}
\newcommand{\vol}{\operatorname{vol}}
\newcommand{\tr}{\operatorname{tr}}
\title{Divergence, rigidity and conformal gauges\newline for Chern--Ricci-flat LCK metrics}
\author{}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{center}\small Working draft: independent mathematical review is pending.\end{center}
\begin{abstract}
For a compact Chern--Ricci-flat locally conformally K\"ahler metric,
the squared $L^2$ norm of the anti-$J$-invariant covariant derivative
of its Lee form equals half the squared norm of its divergence.
This gives equivalent Gauduchon, holomorphic-Lee and Vaisman conditions
for that metric. An explicit fixed Kodaira surface has a strictly LCK
flat conformal gauge which is not Gauduchon, and its conformal class
contains no metric satisfying both conditions. The same complex surface
has an explicit Vaisman metric. These are metric and conformal-class
results; the unrestricted existence question for an arbitrary compact
ordinary Bott--Chern Calabi--Yau LCK manifold remains unresolved.
\end{abstract}

\section{Conventions and scope}
Let $(X,J,g,\omega)$ be connected and compact, of complex dimension
$n\geq2$, with $\omega(X,Y)=g(JX,Y)$. We use
\[
 \ddc=\frac{i}{2\pi}\partial\bar\partial,
 \qquad J\alpha=-\alpha\circ J
\]
for real one-forms. Thus $dJdf=4\pi\ddc f$. A strictly LCK metric has
$d\omega=\vartheta\wedge\omega$ with $d\vartheta=0$ and nonexact
$\vartheta$. It is Vaisman when $\nabla\vartheta=0$. The Chern--Ricci
form is $\rho(g)=-i\partial\bar\partial\log\det(g)$; its normalized
representative $\rho(g)/(2\pi)$ represents ordinary $c_1^{\rm BC}(T_X)$.
All divergences, norms and integrals below use this same $g$.

The same-metric Gauduchon and Chern--Ricci-flat rigidity theorem is
established in \cite[Theorem A]{BO}. We retain the divergence terms
in its connection, Bianchi and Weitzenb\"ock argument. Ordinary
Bott--Chern vanishing alone does not supply a simultaneous gauge.
No theorem for an already Vaisman manifold is applied to a general
LCK manifold, and no deformation or cover replaces the given complex
structure.

\section{The integral identity and its rigidity consequences}
Set
\[
 A=\vartheta^\sharp,\quad B=JA,\quad T=\nabla\vartheta,\quad
 P(X,Y)=\tfrac12\{T(X,Y)+T(JX,JY)\},\quad T^-=T-P,
\]
\[
 q=d_g^*\vartheta=-\tr_gT,\qquad u=|\vartheta|_g^2.
\]
Closedness of $\vartheta$ makes $T$ symmetric; $P$ and $T^-$ are
orthogonal, so $|T|^2=|P|^2+|T^-|^2$.

\begin{theorem}\label{th:rigidity}
For every compact Chern--Ricci-flat strictly LCK metric,
\begin{equation}\label{eq:identity}
 \int_X|T^-|^2\,d\vol_g=\frac12\int_X|q|^2\,d\vol_g.
\end{equation}
For this fixed metric the following conditions are equivalent:
Gauduchon; $q=0$; $A$ is real holomorphic; and Vaisman.
The equality \eqref{eq:identity} is an integral identity, rather than
an asserted pointwise identity for general metrics.
\end{theorem}

\begin{proof}
Locally $\vartheta=df$ and $\widetilde g=e^{-f}g$ is K\"ahler. Its
Levi--Civita connection is
\[
 D_XY=\nabla_XY-\tfrac12\vartheta(X)Y
                 -\tfrac12\vartheta(Y)X+\tfrac12g(X,Y)A.
\]
The equation $DJ=0$ gives
\begin{equation}\label{eq:nablaJ}
 (\nabla_XJ)Y=\tfrac12\{\vartheta(JY)X-\vartheta(Y)JX
                  -g(X,JY)A+g(X,Y)JA\}.
\end{equation}
Differentiating $J\vartheta=-\vartheta\circ J$ and using symmetry of
$T$ consequently gives
\[
 dJ\vartheta(X,JY)=2P(X,Y)-u g(X,Y)
              +\vartheta(X)\vartheta(Y)+J\vartheta(X)J\vartheta(Y).
\]
Flatness and the local conformal volume change give
$\rho(\widetilde g)=n i\partial\bar\partial f=(n/2)dJ\vartheta$.
Contracting the curvature difference of $D$ and $\nabla$ gives the
real conformal Ricci formula
\[
 \Ric_D=\Ric_g+(n-1)T+\tfrac{n-1}{2}\vartheta\otimes\vartheta
                       +\tfrac12\{-q-(n-1)u\}g.
\]
The K\"ahler Ricci form of $\widetilde g$ equals its real Ricci tensor
paired with $J$. Combining these expressions yields
\begin{equation}\label{eq:Ric}
 R:=\Ric_g=nP-(n-1)T+\tfrac{q-u}{2}g
               +\tfrac12\vartheta\otimes\vartheta
               +\tfrac n2J\vartheta\otimes J\vartheta.
\end{equation}
Its trace is
$s=(n-1)q-(n-1)u/2$. The local formulas agree with
\cite[Section 4, equations (2)--(4)]{BO}; no $q=0$ hypothesis has
been inserted into \eqref{eq:Ric}.

Write $\|\cdot\|$ for the $L^2$ norm and put
$E_A=\int_XT(A,A)d\vol_g$, $E_B=\int_XT(B,B)d\vol_g$.
Since $T(A,A)=A(u)/2$ and $\operatorname{div}A=-q$,
\begin{equation}\label{eq:uq}
 \int_Xuq\,d\vol_g=2E_A.
\end{equation}
Pair the contracted Bianchi identity
$\delta R+ds/2=0$ with $\vartheta$ and integrate. Here $\delta$ is
minus covariant contraction, adjoint to symmetric covariant derivative.
It gives $\int\langle R,T\rangle+\frac12\int s q=0$.
Substitution of \eqref{eq:Ric} and \eqref{eq:uq} gives
\begin{equation}\label{eq:Bianchi}
 0=n\|P\|^2-(n-1)\|T\|^2+\tfrac{n-2}{2}\|q\|^2
                    +\tfrac{4-n}{2}E_A+\tfrac n2E_B.
\end{equation}
The integrated Weitzenb\"ock identity for a closed one-form gives
\[
 \|q\|^2=\|T\|^2+\int_XR(A,A)\,d\vol_g.
\]
Equation \eqref{eq:Ric} has
$R(A,A)=(1-n/2)T(A,A)+(n/2)T(B,B)+qu/2$; hence
\begin{equation}\label{eq:Bochner}
 \|q\|^2=\|T\|^2+\tfrac{4-n}{2}E_A+\tfrac n2E_B.
\end{equation}
Eliminating $E_A,E_B$ between \eqref{eq:Bianchi} and
\eqref{eq:Bochner} proves \eqref{eq:identity}.

For the Gauduchon equivalence, the LCK equation and the Hodge identity
$*\vartheta=J\vartheta\wedge\omega^{n-1}/(n-1)!$ give
\[
 d^c\omega^{n-1}=\frac{n-1}{4\pi}
                       J\vartheta\wedge\omega^{n-1},\qquad
 \ddc\omega^{n-1}=-\frac{n-1}{4\pi n}q\,\omega^n.
\]
Thus Gauduchon is exactly $q=0$. In this case \eqref{eq:identity}
forces $T=P$, so $T(B,B)=T(A,A)$. Equation \eqref{eq:uq} gives
$E_A=E_B=0$, and \eqref{eq:Bochner} forces $T=0$.

Equation \eqref{eq:nablaJ} gives $\nabla_AJ=0$. Let $S$ be the
symmetric endomorphism with $g(SX,Y)=T(X,Y)$. Then
\[
 (\mathcal L_AJ)Y=JSY-SJY.
\]
Consequently $A$ is real holomorphic exactly when $T=P$.
Equation \eqref{eq:identity} then gives $q=0$, hence $T=0$.
Conversely $T=0$ gives both other conditions. Under strictness the
parallel Lee form is nonzero, as required for Vaisman.
\end{proof}

\section{An explicit compact example with incompatible gauges}
\begin{proposition}\label{prop:example}
On one fixed compact complex Kodaira surface there is a strictly LCK
Chern--Ricci-flat metric which is not Gauduchon. Its conformal class
contains no simultaneously Gauduchon and Chern--Ricci-flat metric.
The same surface has an explicit Vaisman metric, so this is not a
counterexample to the unrestricted P05 existence question.
\end{proposition}

\begin{proof}
On $G=\mathbb R^4$ use the multiplication
\[
 (x,y,z,t)(x',y',z',t')=(x+x',y+y',z+z'+xy',t+t').
\]
The integer subgroup $\Gamma=\mathbb Z^4$ is a lattice: its left
action is $(x,y,z,t)\mapsto(x+a,y+b,z+c+ay,t+d)$.
Reduction of $x,y,t$ and then $z$ to unit intervals supplies a compact
fundamental set. Thus $X=\Gamma\backslash G$ is connected and compact.
The global forms
\[
 e^1=dx,\quad e^2=dy,\quad e^3=dz-xdy,\quad e^4=dt
\]
have $de^3=-e^{12}$ and the other derivatives zero. Declare
$\phi^1=e^1+i e^2$, $\phi^2=e^3+i e^4$ to be of type $(1,0)$.
Then $d\phi^1=0$ and
$d\phi^2=-(i/2)\phi^1\wedge\overline{\phi^1}$ have no $(0,2)$
part, so the complex structure is integrable.
$\Sigma=\phi^1\wedge\phi^2$ is closed and nowhere vanishing,
hence holomorphic. The canonical bundle is holomorphically trivial,
which proves ordinary $c_1^{\rm BC}(T_X)=0$.

Take a unit-periodic $f(x)$ with $C=1-f''>0$, and set
\[
 \vartheta_1=-e^4+f'e^1,\quad \eta_1=J\vartheta_1=e^3+f'e^2,
 \quad \omega_1=\vartheta_1\wedge\eta_1+C e^{12}.
\]
This is the positive Hermitian form of
$g_1=\vartheta_1^2+\eta_1^2+C\{(e^1)^2+(e^2)^2\}$.
One has $d\vartheta_1=0$, $d\eta_1=-C e^{12}$ and
$d\omega_1=\vartheta_1\wedge\omega_1$.
The $t$-circle has Lee period $-1$, so the metric is strict.
Its Lee dual is $-\partial_t$. All coefficients are independent of
$t$, making this field Killing; closedness of $\vartheta_1$ makes
$\nabla\vartheta_1$ symmetric and Killing makes it skew. Thus $g_1$
is Vaisman on this fixed complex manifold.

Its volume is $\omega_1^2/2=C e^{1234}$, while
$\Sigma\wedge\overline\Sigma$ has constant density in $e^{1234}$.
Put $h=C^{-1/2}$ and $\omega=h\omega_1$. Then
$\omega^2/2=e^{1234}$, so its Chern--Ricci form is zero. Its Lee form
is $\vartheta=-e^4+d(f+\log h)$, retaining period $-1$.
If $E_i$ are dual to $e^i$, its Lee dual is
\[
 A=h'E_1+(f'h'-h^{-1})E_4.
\]
The metric volume is $dx\,dy\,dz\,dt$. Each $E_i$ has zero
divergence in this volume, hence $\operatorname{div}A=h''$ and
$q=d_g^*\vartheta=-h''$.

For the explicit choice
\[
 f(x)=\frac{\cos(2\pi x)}{16\pi^2},\qquad
 C(x)=1+\tfrac14\cos(2\pi x)\geq\tfrac34,
\]
direct differentiation gives
\[
 q(0)=-\frac{4\sqrt5\pi^2}{25},\qquad
 q(1/2)=\frac{4\sqrt3\pi^2}{9}.
\]
Thus $\omega$ is not Gauduchon, and Theorem~\ref{th:rigidity}
also shows it is not Vaisman.

For any global real $v$,
$\rho(e^v\omega)=\rho(\omega)-n i\partial\bar\partial v$.
Two flat metrics in a single conformal class therefore have a real
pluriharmonic logarithmic ratio, constant on a connected compact
complex manifold by the maximum principle. The only flat metrics
conformal to $\omega$ are its positive constant multiples; constant
scaling cannot make its nonzero $q$ vanish. This proves the asserted
obstruction. The already exhibited $\omega_1$ is a Vaisman and
Gauduchon representative in that class, with generally nonzero
Chern--Ricci form.
\end{proof}

\section{The remaining existence question}
If ordinary $c_1^{\rm BC}(T_X)=0$, write
$\rho(\omega)/(2\pi)=\ddc F$ for a global smooth $F$.
Then $e^{F/n}\omega$ is Chern--Ricci flat and its Lee form is
$\vartheta+dF/n$, still nonexact. This proves existence and
uniqueness up to scale of the flat conformal gauge, rather than
existence of a metric with $q=0$ in it. The explicit example
shows why these assertions cannot be combined with the separate
Gauduchon conformal theorem to supply the same-metric rigidity
hypothesis. It supplies no obstruction to all Vaisman metrics on
$X$, and the arbitrary same-complex-manifold existence problem
remains open in this argument. Independent review, reconstruction,
source assessment and final comparison are pending for this draft.
\begin{thebibliography}{9}
\bibitem{BO} G. Barbaro and A. Otiman,
\emph{Calabi--Yau locally conformally K\"ahler manifolds},
\href{https://arxiv.org/abs/2509.18364v2}{arXiv:2509.18364v2},
Theorem A and Section 4.
\end{thebibliography}
\end{document}

```

## Entire ordinary original-worker submission, provenance and scope
Result SHA256: e581e3c8762433407c2d607df98e0e3dd430fe24a01e96319e104a4949e082ae. Seven ordinary notes follow verbatim.
That fresh worker returned candidate=false on the full original task.
The current paper uses the elementary flat-gauge reduction in n1 and
the explicit example and integrated identity in n2--n3. Notes n4--n7
are retained whole for provenance and comparison, but their finite
cover, symmetrization, perturbation and potential-subclass assertions
are not imported as premises of the current article. Their deeper
source applications remain separate checking obligations. Retain the
failed earlier divergence identity in n3 as a failed calculation.

### Whole note n1
```json
{
  "id": "n1",
  "summary": "Primary-source audit and exact conformal-gauge reduction. Ordinary c1BC=0 supplies a unique Chern-Ricci-flat representative up to scale in each conformal class, but does not supply Gauduchon in that same gauge. The checked Vaisman existence theorems retain additional hypotheses; full P05 remains unsolved.",
  "detailedSummary": "The latest retrieved Barbaro–Otiman version imposes Gauduchon on the same metric in Theorem A and explicitly states the unrestricted existence assertion as a conjecture. Ornea–Verbitsky's prescribed-volume theorem requires an already Vaisman manifold and invariance under both canonical flows. Istrati's canonical-metric theorem also starts with Vaisman. Tsukada's original theorem supplies a convex Lee-class cone only on an already Vaisman manifold. The conformal calculation is reconstructed with the required normalization and proves preservation of strictness and uniqueness of the flat gauge.",
  "text": "The pivotal primary statements have the following scope.\n\n[Barbaro–Otiman, arXiv:2509.18364v2](https://arxiv.org/html/2509.18364v2), Theorem A and Section 4, assumes a compact strictly LCK metric that is both Chern-Ricci flat and Gauduchon; it concludes that metric is Vaisman. The introduction states the general existence assertion as a conjecture. Proposition 3.9 addresses the additional hypothesis of potential.\n\n[Ornea–Verbitsky, arXiv:2206.08808v2](https://arxiv.org/html/2206.08808v2), Theorem 4.1, begins with a compact Vaisman manifold. Its prescribed positive volume must be invariant under the Lee and anti-Lee fields and have the required total volume. The resulting Vaisman metric has the specified Lee class. The invariance produces a basic transverse volume and cannot be omitted.\n\n[Istrati, arXiv:2304.02582v1](https://arxiv.org/pdf/2304.02582v1), Corollary 5.2, begins with a compact Vaisman manifold with ordinary c1BC=0. For a Lee class it supplies a Chern-Ricci-flat Vaisman metric, unique up to scale. Theorem 5.7 says sufficiently small complex deformations of a compact Vaisman Calabi-Yau manifold remain Vaisman Calabi-Yau.\n\n[Tsukada, Compositio Math. 93 (1994)](https://www.numdam.org/article/CM_1994__93_1_1_0.pdf), Theorem 5.1, concerns a compact generalized Hopf manifold, meaning a manifold with nonzero parallel Lee form. Its Lee classes are {t[theta0]+eta: t>0, eta the real class of a closed holomorphic one-form}; the constructive proof gives Vaisman metrics for these classes. This set is convex and excludes zero. Original PDF page 20 was viewed because OCR drops displayed formulas.\n\nHere is the elementary gauge calculation. Write r(omega)=-dd^c log det(g), with dd^c=i partial barpartial/(2pi), for the normalized Chern-Ricci representative of c1BC(T_X). For a global real u,\nr(e^u omega)=r(omega)-n dd^c u,\nd(e^u omega)=(lambda+du) wedge e^u omega.\nOrdinary Bott-Chern vanishing means r(omega)=dd^c F for a global smooth real F. Consequently e^(F/n)omega is Chern-Ricci flat and remains strictly LCK, since its Lee class is [lambda]!=0.\n\nIf two conformal representatives are Chern-Ricci flat, their logarithmic conformal ratio satisfies dd^c u=0. A real pluriharmonic function on a connected compact complex manifold is constant by the maximum principle. Thus the flat representative is unique up to positive scale. Nothing here makes its Lee form co-closed: Gauduchon is a separate differential equation.\n\nThe ordinary-unitary-flat equivalence was also checked in [Tosatti, arXiv:1401.4797v4](https://arxiv.org/pdf/1401.4797v4), Proposition 1.1. No de Rham vanishing, Ricci flatness on the Kähler cover, or twisted LCK Bott-Chern class is substituted for ordinary c1BC(T_X).\n\nRetrieved statements are retained in sources/latest2.json, sources/latest3.json, sources/primary4.json, sources/primary5.json, sources/cone_kernel2.json, sources/potential4.json and sources/versions.json. Reread the public URLs with the web tool's open argument; Tsukada's display uses screenshot with pageno=20. README.md records the resources and environment. This is a source audit and elementary reduction, not a P05 solution.\n\nArtifacts: /workspace/research/native-workers/codex-ObNUfQ",
  "support": []
}
```

### Whole note n2
```json
{
  "id": "n2",
  "summary": "Explicit fixed Kodaira surface with ordinary c1BC=0 and a strictly LCK Chern-Ricci-flat metric that is not Gauduchon. Its conformal class has no simultaneous flat/Gauduchon representative. The surface nevertheless has an explicit Vaisman metric, so this diagnoses the gauge argument rather than disproving P05.",
  "detailedSummary": "On an integer Heisenberg quotient times a circle, fix phi1=e1+i e2 and phi2=e3+i e4 with de3=-e1 wedge e2. For f=cos(2pi x)/(16pi^2), C=1-f''=1+cos(2pi x)/4>0, construct the Vaisman metric omega1=(-dt+df) wedge J(-dt+df)+C e1 wedge e2. Its conformal rescaling omega=C^(-1/2)omega1 has constant canonical volume and zero Chern-Ricci form. The Lee period on the t-circle remains -1, while d*theta=-h'' for h=C^(-1/2) is nonzero. Exact exterior-algebra and independent Koszul-curvature checks passed.",
  "text": "Define G=R^4 with multiplication\n(x,y,z,t)(x',y',z',t')=(x+x',y+y',z+z'+x y',t+t').\nThe integer subgroup Gamma=Z^4 is a lattice. Its left action is\n(x,y,z,t) -> (x+a,y+b,z+c+a y,t+d).\nHence X=Gamma\\G is connected and compact. Define global forms\ne1=dx, e2=dy, e3=dz-x dy, e4=dt.\nThey satisfy de1=de2=de4=0 and de3=-e1 wedge e2.\n\nFix the complex structure with (1,0)-coframe phi1=e1+i e2, phi2=e3+i e4. Since dphi1=0 and dphi2=-(i/2)phi1 wedge bar(phi1) has no (0,2)-part, it is integrable. Sigma=phi1 wedge phi2 is globally defined, nowhere vanishing and closed, hence holomorphic. Thus K_X is holomorphically trivial, proving exactly ordinary c1BC(T_X)=0.\n\nUse Jalpha=-alpha composed with J on real one-forms. Let f(x) be unit-periodic with C=1-f''>0, and put\ntheta1=-e4+f'e1,\neta1=Jtheta1=e3+f'e2,\nomega1=theta1 wedge eta1+C e1 wedge e2.\nThen dtheta1=0, deta1=-C e1 wedge e2 and d(C e1 wedge e2)=0, so domega1=theta1 wedge omega1. Its positive metric is\ng1=theta1^2+eta1^2+C(e1^2+e2^2).\nThe t-circle has integral(theta1)=-1, proving strictness.\n\nThe g1-dual of theta1 is -E4=-partial_t, where E_i is dual to e_i. All coefficients are independent of t, so this field is Killing. Closedness makes nabla theta1 symmetric, and Killing makes it skew-symmetric. Therefore nabla theta1=0: g1 is Vaisman on this fixed X.\n\nIts volume is omega1^2/2=C e1234. Sigma wedge bar(Sigma) has constant density in e1234, giving r(omega1)=-dd^c log C. Set h=C^(-1/2) and omega=h omega1. Then omega^2/2=e1234 and\nr(omega)=-dd^c log C-2 dd^c log h=0.\nThe new Lee form is theta=-e4+d(f+log h), still with period -1.\n\nChoose f=cos(2pi x)/(16pi^2). Then C=1+cos(2pi x)/4>=3/4. The Lee dual for g=h g1 is\nA=h' E1+(f'h'-h^(-1))E4.\nThe volume is e1234=dx dy dz dt, and each E_i has zero divergence in this volume. Thus div A=h'', so q=d_g^*theta=-h''. In particular,\nq(0)=-4 sqrt(5) pi^2/25,\nq(1/2)=4 sqrt(3) pi^2/9.\nDirect differentiation gives dd^c omega=h'' e1234/(4pi)=-(q/(8pi))omega^2. Therefore omega is not Gauduchon and is not Vaisman.\n\nEvery Chern-Ricci-flat metric conformal to omega is a constant multiple, since its logarithmic ratio satisfies dd^c u=0. Constant scaling cannot make its nonzero codifferential vanish. This conformal class therefore contains no simultaneously Gauduchon and Chern-Ricci-flat metric. It does contain the Vaisman/Gauduchon metric omega1, whose Chern-Ricci form generally is nonzero.\n\nRerun the exact checker with:\npython check_kodaira.py > outputs/kodaira.txt\nIt uses a=f', h=C^(-1/2), p=h', r=h'' and a'=1-h^(-2). Final output includes:\nd(theta)=0; d(omega)-theta^omega=0; omega^2/2=e1234: exact PASS\ndet(real metric)=1\nq=d*theta=-r\nu=|theta|^2=(p^2+1)/h\n|T^-|^2=r^2/2\nDirect Koszul curvature agrees with Chern-flat LCK Ricci formula: exact PASS\nThe program also verifies Hermitian symmetry and the quoted values of q. The run used Python 3.12.14 and SymPy 1.14.0.\n\nThe displayed geometric arguments establish compactness, integrability, positivity, strictness and the exact canonical condition; execution alone is not mathematical proof. This is not an exhaustive search and not a counterexample to P05, because g1 is Vaisman on X.\n\nArtifacts: /workspace/research/native-workers/codex-ObNUfQ",
  "support": []
}
```

### Whole note n3
```json
{
  "id": "n3",
  "summary": "General integrated identity for compact Chern-Ricci-flat LCK metrics: ||(nabla lambda)^-||_L2^2=1/2 ||d*lambda||_L2^2. It reconstructs simultaneous-gauge rigidity and identifies the missing divergence condition. A holomorphic Lee dual also suffices, but neither extra condition is supplied by P05.",
  "detailedSummary": "Without Gauduchon, the conformal Kähler connection gives Ric=nP-(n-1)T+(q-u)g/2+lambda tensor lambda/2+n Jlambda tensor Jlambda/2. Contracted Bianchi and integrated Weitzenböck eliminate Lee and anti-Lee derivative terms to give the exact integral identity. If q=0, then T=P, and a further Weitzenböck calculation forces T=0. Holomorphicity of the Lee dual is equivalent to T=P, so Gauduchon, holomorphic Lee dual and Vaisman are equivalent in this flat setting. A failed intermediate divergence extension was rejected and preserved.",
  "text": "Let (X,J,g,omega) be compact LCK of complex dimension n>=2, with closed Lee form theta and zero Chern-Ricci form. Use g and dvol_g for all norms and integrals. Set\nA=theta^sharp, B=JA, T=nabla theta,\nP(X,Y)=(T(X,Y)+T(JX,JY))/2,\nT^-=T-P, q=d^*theta=-tr_g T, u=|theta|^2.\nClosedness makes T symmetric, and |T|^2=|P|^2+|T^-|^2.\n\nLocally theta=df and tilde g=e^(-f)g is Kähler. Its connection is\nD_XY=nabla_XY-theta(X)Y/2-theta(Y)X/2+g(X,Y)A/2.\nSince D preserves J,\n(nabla_X J)Y=[theta(JY)X-theta(Y)JX-g(X,JY)A+g(X,Y)JA]/2.\nDifferentiating Jtheta=-theta composed with J gives\ndJtheta(X,JY)=2P(X,Y)-u g(X,Y)+theta(X)theta(Y)+Jtheta(X)Jtheta(Y).\nThis follows by expanding (nabla_X Jtheta)(JY)-(nabla_(JY)Jtheta)(X).\n\nWrite rho=-i partial barpartial log det(g)=2pi r. Flatness gives rho_(tilde g)=n i partial barpartial f=(n/2)dJtheta. Kähler Chern and Levi-Civita Ricci agree, and the conformal Ricci formula in real dimension 2n gives\nRic_D=Ric_g+(n-1)T+(n-1)theta tensor theta/2+[-q-(n-1)u]g/2.\nConsequently\nR:=Ric_g=nP-(n-1)T+(q-u)g/2+theta tensor theta/2+(n/2)Jtheta tensor Jtheta. (1)\nIts trace is s=(n-1)q-(n-1)u/2. The normalization is consistent with dJdf=4pi dd^c f.\n\nLet E=integral T(A,A), F=integral T(B,B), and let ||.|| denote L2 norm. Metric compatibility gives T(A,A)=A(u)/2, so integration by parts gives integral u q=2E.\n\nPair contracted Bianchi, delta R+ds/2=0, with theta and integrate. Since delta is the adjoint of symmetric nabla,\n0=integral <R,T>+(1/2)integral s q.\nInsert (1), use <g,T>=-q, <P,T>=|P|^2 and integral u q=2E. This yields\n0=n||P||^2-(n-1)||T||^2+(n-2)||q||^2/2+(4-n)E/2+nF/2. (2)\n\nBecause dtheta=0, integrated Weitzenböck gives\n||q||^2=||T||^2+integral R(A,A).\nEquation (1) gives\nR(A,A)=(1-n/2)T(A,A)+(n/2)T(B,B)+qu/2,\nhence\n||q||^2=||T||^2+(4-n)E/2+nF/2. (3)\nEliminating E,F from (2),(3) proves\nintegral |T^-|^2=(1/2)integral |d^*theta|^2. (4)\nThis is an integrated identity, not a general pointwise equality.\n\nFor the Gauduchon condition, use\n*theta=Jtheta wedge omega^(n-1)/(n-1)!,\ndomega^(n-1)=(n-1)theta wedge omega^(n-1).\nWith the specified dd^c convention,\ndd^c omega^(n-1)=-(n-1)q omega^n/(4pi n).\nThus Gauduchon is exactly q=0. Then (4) forces T=P, so T(B,B)=T(A,A). Also E=0 and F=0; (3) forces T=0. Under strictness the resulting parallel Lee form is nonzero.\n\nThere is another equivalent sufficient condition. The LCK formula gives nabla_A J=0. For the symmetric endomorphism S defined by g(SX,Y)=T(X,Y),\n(L_A J)Y=J SY-S JY.\nTherefore A is real holomorphic iff T=P. Equation (4) then forces q=0 and consequently T=0. Conversely parallel Lee implies q=0 and a holomorphic dual. Thus, for a compact Chern-Ricci-flat strictly LCK metric, Gauduchon, holomorphic Lee dual and Vaisman are equivalent.\n\nThe n2 family has q=-h'' and |T^-|^2=(h'')^2/2, so nonzero divergence is compatible with (4). check_kodaira.py computes (1) independently from the Koszul curvature and verifies (4) pointwise for that particular family. Rerun: python check_kodaira.py > outputs/kodaira.txt.\n\nAn incorrect intermediate extension predicted n||T^-||^2=(n+2)||q||^2/2-integral u q. It carried a Gauduchon-only manipulation into the non-Gauduchon setting. Its discrepancy on the n2 family was -r(h r+p^2+1)/h, rather than the claimed total derivative. The failed calculation is preserved in outputs/kodaira_initial_failure.txt and can be reproduced with:\npython failed_extension.py > outputs/failed_extension.txt 2>&1\nExpected exit status is 1 with AssertionError: Expected failure: incorrect divergence extension. This formula is rejected and is diagnostic only. Equations (1)-(3) recompute the omitted trace terms; the corrected checks pass.\n\nThis proves a quantitative identity and restricted rigidity. It does not construct a gauge with q=0 or establish the full existence conjecture.\n\nArtifacts: /workspace/research/native-workers/codex-ObNUfQ",
  "support": [
    "n2"
  ]
}
```

### Whole note n4
```json
{
  "id": "n4",
  "summary": "Normalized flat canonical volume is invariant under every biholomorphism. Using checked Vaisman volume and Lee-class results gives a complete descent proof for finite unramified quotients of Calabi-Yau Vaisman manifolds. P05 does not supply such a cover.",
  "detailedSummary": "Every compact ordinary Bott-Chern Calabi-Yau manifold has a unique normalized positive volume with zero local Chern-Ricci form; uniqueness implies invariance under automorphisms. A holomorphic Lee dual of a Chern-flat LCK metric therefore has zero divergence. For a finite free holomorphic action on a Calabi-Yau Vaisman manifold, average a Lee class in its convex cone and prescribe the invariant flat volume. Uniqueness makes the resulting Vaisman metric group-invariant, so it descends with nonexact Lee form and ordinary c1BC=0 to the original quotient.",
  "text": "The conformal calculation in n1 supplies a positive volume mu with vanishing local Chern-Ricci form whenever c1BC(T_X)=0. Normalize integral mu=1. If nu is another such normalized volume, dd^c log(nu/mu)=0. Compactness forces the ratio to be constant, and normalization makes it one. Thus the normalized flat canonical volume is unique.\n\nFor a biholomorphism phi, phi^*mu is flat with total volume one, hence phi^*mu=mu. Every complete real holomorphic vector field preserves mu. A Chern-Ricci-flat LCK metric has dvol_g proportional to mu. If its Lee dual is holomorphic, it therefore has zero divergence and, by n3, the metric is Vaisman. This supplies an interpretation of the additional holomorphic-Lee condition, not a construction of such a field.\n\nNow suppose Y is compact connected Vaisman with ordinary c1BC(T_Y)=0 and a finite group F acts freely by biholomorphisms. Let X=Y/F. Its Lee-class cone C is the convex open half-space checked in n1, and every class in C is realized by a Vaisman metric. Each group element preserves C by pullback. Therefore, for tau0 in C,\ntau=(1/|F|)sum_(gamma in F)gamma^*tau0\nis in C, is F-invariant and is nonzero.\n\nChoose a Vaisman metric with Lee class tau and rescale it to total volume one. The normalized flat canonical volume mu is invariant under all biholomorphisms, including this metric's Lee and anti-Lee flows. All hypotheses of Ornea–Verbitsky Theorem 4.1 hold. It supplies a unique Vaisman metric g with Lee class tau and volume mu. Its Chern-Ricci form is zero because that form depends only on local volume density.\n\nFor gamma in F, gamma^*g has the same Lee class and the same volume mu. Uniqueness gives gamma^*g=g. Thus g descends to the original quotient X. Parallelness and Chern-Ricci flatness are local conditions and descend through this unramified holomorphic quotient. The descended Lee class cannot be exact, since its pullback is tau!=0. Hence X itself has a strict Vaisman metric and ordinary c1BC(T_X)=0.\n\nFor a nonregular finite unramified cover with Vaisman Calabi-Yau total space, pass to its finite normal closure, pull back the metric, and apply the same argument to the finite deck group. The resulting metric again descends to X.\n\nThe imported cone and prescribed-volume theorems are precisely those audited in n1; invariance, averaging and descent are reconstructed here. This closes descent for this subclass and rules out a counterexample obtained by such a finite quotient. The general P05 assumptions do not provide a finite Vaisman cover. Invariance of a flat volume alone does not authorize the Vaisman volume theorem on an arbitrary LCK manifold.\n\nArtifacts: /workspace/research/native-workers/codex-ObNUfQ",
  "support": [
    "n1",
    "n3"
  ]
}
```

### Whole note n5
```json
{
  "id": "n5",
  "summary": "Averaging proves Vaisman existence on the same compact quotient with invariant complex structure when the given Lee class has a closed left-invariant representative. The original LCK metric may be noninvariant. The representability condition is not established for general P05 data.",
  "detailedSummary": "For X=Gamma\\G with unimodular G and invariant integrable J, conformally make the Lee form invariant and symmetrize the metric. Symmetrization commutes with d, J and dd^c and preserves positivity, yielding invariant strict LCK. Its invariant Chern-Ricci form is dd^c of a global function by ordinary c1BC=0; symmetrization kills that potential and forces Ricci zero. Unimodularity makes its Lee form co-closed, so n3 supplies Vaisman without changing J or taking a cover.",
  "text": "Proposition. Let X=Gamma\\G be a connected compact quotient of a connected unimodular Lie group with integrable left-invariant complex structure J. Assume ordinary c1BC(T_X)=0 and a strictly LCK metric whose Lee class contains a closed left-invariant form theta0. Then the given X admits a strict Vaisman metric with Lee class [theta0].\n\nWrite lambda=theta0+df. The conformal metric omega'=e^(-f)omega satisfies domega'=theta0 wedge omega', with the same nonzero Lee class.\n\nNormalize an invariant volume on X. In the global invariant frame E_i, symmetrize a differential form by integrating its coefficient functions against this volume. This does not require a global holomorphic action of G on Gamma\\G. Unimodularity gives div E_i=-tr(ad E_i)=0, hence integral E_i(f)=0. The frame formula for exterior differentiation then proves that symmetrization S commutes with d. Since J has constant frame coefficients, S commutes with J, type operators and dd^c. For invariant beta, S(beta wedge alpha)=beta wedge S(alpha).\n\nAveraging preserves strict Hermitian positivity: for nonzero invariant v, omega'(v,Jv) is positive everywhere. Thus bar(omega)=S(omega') is positive and invariant, and\nd bar(omega)=theta0 wedge bar(omega).\nIt remains strictly LCK because [theta0]=[lambda]!=0.\n\nThe Chern connection of the lifted invariant Hermitian metric is invariant, so r(bar(omega)) is invariant. Ordinary Bott-Chern vanishing supplies a global F with r(bar(omega))=dd^c F. Therefore\nr(bar(omega))=S(r(bar(omega)))=dd^c S(F)=0,\nsince S(F) is constant. This gives actual Chern-Ricci flatness, rather than de Rham exactness.\n\nIts Lee dual is invariant, so unimodularity also gives d^*theta0=0. The metric is Gauduchon, and n3 forces nabla theta0=0. Its nonzero class guarantees nonzero parallel Lee form, proving the proposition.\n\nA sufficient checkable condition for Lee representability is surjectivity of invariant degree-one de Rham cohomology onto H^1_dR(X). No such surjectivity is assumed for all solvmanifolds, and no invariant model is constructed for general P05 manifolds. Averaging lambda and omega separately would not preserve d omega=lambda wedge omega; the conformal correction to an invariant representative is essential.\n\nThis is a mathematical subclass proof with positivity, strictness and ordinary Bott-Chern vanishing checked throughout. It performs no finite Lie-algebra enumeration and does not solve unrestricted P05.\n\nArtifacts: /workspace/research/native-workers/codex-ObNUfQ",
  "support": [
    "n3"
  ]
}
```

### Whole note n6
```json
{
  "id": "n6",
  "summary": "An ordinary dd^c perturbation of a strict Vaisman metric preserving exactly its Lee form must vanish. This blocks a naive ordinary Hermitian Monge–Ampère prescription; it does not block twisted perturbations or changing the Lee form.",
  "detailedSummary": "If omega'=omega+dd^c phi is positive and LCK with the same Lee form theta as a strict Vaisman metric, then theta wedge dd^c phi=0. Linear algebra forces dd^c phi=a theta wedge Jtheta. Closedness and nondegeneracy of dJtheta on the horizontal distribution force a=0, so phi is constant. The argument applies in every complex dimension at least two and does not require c1BC=0.",
  "text": "Let omega be strict Vaisman on a connected compact complex manifold, with Lee form theta. Suppose omega'=omega+dd^c phi is positive and LCK with the same theta. Since dd^c phi is closed, subtracting the LCK equations gives\ntheta wedge dd^c phi=0. (1)\n\nThe nonzero parallel theta is nowhere zero. A real (1,1)-form beta satisfying theta wedge beta=0 must have the form beta=a theta wedge Jtheta. Indeed beta=theta wedge eta first follows from the wedge condition, and its type forces eta modulo theta to lie in the real span of Jtheta. Thus a is smooth globally.\n\nApply this to beta=dd^c phi. Let u=|theta|^2>0, constant. The LCK connection calculation in n3 with nabla theta=0 gives\ndJtheta=-u omega+theta wedge Jtheta.\nClosedness of beta yields\n0=da wedge theta wedge Jtheta-a theta wedge dJtheta.\nEvaluate on A=theta^sharp and v,w in H=ker theta intersect ker Jtheta. The da term vanishes, and the other term is a u^2 omega(v,w). Since dim_R H=2n-2>=2 and omega restricts nondegenerately to H, a=0. Consequently dd^c phi=0 and compactness makes phi constant.\n\nThus ordinary scalar dd^c metric deformation cannot provide a nontrivial LCK family with the same Lee form starting from a strict Vaisman metric. An ordinary Hermitian prescribed-volume output satisfies d omega'=theta wedge omega, which generally differs from the needed theta wedge omega'.\n\nThis rules out only that ansatz. It does not exclude twisted potentials, changing the Lee form, or the nonconformal changes in n2, and does not prove that arbitrary ordinary Bott-Chern Calabi-Yau LCK manifolds have potential.\n\nArtifacts: /workspace/research/native-workers/codex-ObNUfQ",
  "support": [
    "n2",
    "n3"
  ]
}
```

### Whole note n7
```json
{
  "id": "n7",
  "summary": "Reconstructed same-manifold transfer for the LCK-with-potential subclass in dimension >=3, using the precise isomorphic-approximation theorem, a canonical-degree limit, the Vaisman Bott-Chern kernel and deformation stability. Full P05 still lacks a proof of potential or another general existence mechanism.",
  "detailedSummary": "Primary Ornea–Verbitsky Theorem 7.3 supplies diffeomorphisms nu_i in Diff0 with nu_i(J) converging smoothly to a Vaisman structure. Every approximant is biholomorphic to the original, preserving exact ordinary c1BC=0. Converging Gauduchon metrics pass zero canonical degree to the limit. The limiting de Rham c1 vanishes, and on Vaisman the Bott-Chern kernel is generated by a nonzero semipositive transverse class; zero degree therefore forces ordinary c1BC=0 there. Istrati stability makes nearby approximants Vaisman, and biholomorphic pullback returns a strict Vaisman metric to the original manifold. This uses checked external theorems and the added potential hypothesis; it does not solve arbitrary strict LCK data.",
  "text": "This is a same-manifold partial existence argument with the additional hypothesis of positive automorphic LCK potential and n>=3.\n\n[Ornea–Verbitsky, arXiv:2112.03363v2](https://arxiv.org/pdf/2112.03363v2), Theorem 7.3, states that a compact LCK manifold with potential in complex dimension at least three has a Vaisman-type structure J_infty on the same smooth manifold, together with nu_i in Diff0 such that J_i=nu_i(J) converges to J_infty in C-infinity. Thus every (M,J_i) is biholomorphic to the given X. Original PDF page 17 was viewed to confirm the >=3 inequality lost in OCR. Merely knowing that some deformation is Vaisman would not be enough.\n\nThe same source's Theorem 4.8 allows approximation of improper positive potential by proper-potential LCK structures on the same complex manifold. Ordinary c1BC remains fixed because J remains fixed, and strictness persists: a loop with a nonzero original Lee period retains a nonzero period for sufficiently close forms. The rank-one reduction therefore does not replace X or silently impose a canonical condition.\n\nHere is the transfer argument. Assume c1BC(X)=0. Biholomorphic invariance gives exactly c1BC(M,J_i)=0 for every i. Choose converging J_i-Hermitian background metrics by symmetrizing a positive J_infty-Hermitian metric. Their normalized Gauduchon representatives gamma_i converge to gamma_infty: the factor solves a second-order linear elliptic equation with a simple normalized positive kernel, so elliptic perturbation supplies continuous dependence.\n\nLet r_i be the normalized Chern-Ricci forms of the backgrounds. They converge smoothly to r_infty. Since r_i=dd^c_(J_i)F_i and gamma_i is Gauduchon,\nintegral_M r_i wedge gamma_i^(n-1)=0.\nTherefore\nintegral_M r_infty wedge gamma_infty^(n-1)=0. (1)\nNo bound or convergence of F_i is needed.\n\nAlso c1_dR(M,J_infty)=0: sufficiently close almost complex structures are homotopic and have the same topological first Chern class. The limiting ordinary Bott-Chern class consequently lies in the kernel of HBC^(1,1)->H_dR^2.\n\nFor compact Vaisman this kernel is R[kappa], where kappa=-dJtheta is the nonzero semipositive transverse form of a normalized strict Vaisman metric. The primary calculation is [Istrati–Otiman, arXiv:2206.07312v2](https://arxiv.org/pdf/2206.07312v2), Theorem 4.2 and Corollary 5.1. In its model HB(F) tensor Lambda(u,bar u), du and dbar u are opposite multiples of [kappa]. The only exact total-degree-two class of type (1,1) arising from a degree-one differential is a multiple of [kappa]; it is not Bott-Chern exact because degree zero contains constants. This reconstructs the required kernel consequence.\n\nWrite c1BC(M,J_infty)=a[kappa]. Equation (1) gives\n0=a integral_M kappa wedge gamma_infty^(n-1).\nThe integral is strictly positive because kappa is semipositive of rank n-1 and gamma_infty is positive. Hence a=0: the Vaisman limit satisfies the exact ordinary Bott-Chern condition, without assuming general deformation invariance of that condition.\n\nNow [Istrati, arXiv:2304.02582v1](https://arxiv.org/pdf/2304.02582v1), Theorem 5.7, applies to this compact Vaisman Calabi-Yau limit. All sufficiently small complex deformations remain Vaisman Calabi-Yau. By local completeness of deformation theory, the convergent integrable J_i lie in that neighborhood modulo diffeomorphism for large i. Pulling a resulting Vaisman metric back through the biholomorphism between (M,J) and (M,J_i) gives a metric on the original X. Its nonzero parallel Lee form cannot be exact on a compact manifold, since an exact form vanishes at an extremum of its primitive. The result is strict.\n\nThis reconstructs the transfer underlying [Barbaro–Otiman v2](https://arxiv.org/html/2509.18364v2), Proposition 3.9, using the stronger primary approximation statement. The approximation, cohomology-model and deformation-stability theorems are imported with their stated hypotheses; their complete deep proofs are not newly established here. The displayed reasoning proves the implication conditional on those primary results and the added potential hypothesis.\n\nRetrieved statements are in sources/latest3.json, sources/potential3.json, sources/potential4.json, sources/cone_kernel2.json and sources/potential_rank.json. Reread with open at the public URLs, or screenshot with pageno=17 for the approximation statement. Programs, outputs and environment are recorded in README.md; python validate_notes.py checks the seven-note artifact and dependencies.\n\nThe full unchanged P05 remains unsolved in this exploration. Ordinary c1BC(T_X)=0 makes the canonical bundle unitary flat; LCK potential is governed by a different twisted class. No implication from the former vanishing to positive automorphic potential has been proved, and no compact strictly LCK example with ordinary c1BC=0 and an obstruction to every Vaisman metric has been constructed. These partial results and rejected approaches warrant retained notes, but candidate=false.\n\nArtifacts: /workspace/research/native-workers/codex-ObNUfQ",
  "support": [
    "n1"
  ]
}
```

## Dependency and boundary judgments requested
Check the local conformal Ricci tensor, closed-one-form Weitzenbock
identity, contracted Bianchi identity, J and ddc normalizations, and
every integration by parts. Compare the exact retained q terms with
Barbaro--Otiman arXiv:2509.18364v2 Section4 equations(2)--(4).
Theorem A requires the same metric to be Gauduchon and flat; it is
context and consistency evidence, not a theorem removing Gauduchon.
Its following abstract prescribed-volume example is not used to
establish the present explicit compact lattice construction. The
current paper makes no priority claim, full P05 solution, potential
hypothesis deduction, or classification of all Calabi--Yau LCK X.


## Complete unchanged original-task full review

The verdict remains INCONCLUSIVE. All report premises0--8 concern unused original conditional notes n4/n7; none is needed for the current A--D article. All raw quote bindings remain verbatim, including passage14 task-to-external mismatch, which is EXCLUDED as external evidence.

```json
{
  "verdict": "INCONCLUSIVE",
  "report": "The exact original completion criterion remains unresolved. The frozen article establishes A–D, and the retained notes establish additional conditional results, but neither supplies Vaisman existence for every manifold in P05 nor constructs a manifold admitting no Vaisman metric. I found no concrete defect in the accepted A–D argument. The deliberately rejected calculation in n3 is false, as checked below, but is not used subsequently. Thus the appropriate verdict for the full task is INCONCLUSIVE.\n\nFor A, write r(ω)=ρ(ω)/(2π). The determinant of a Hermitian metric scales by e^(nv), so r(e^vω)=r(ω)−n dd^c v. Ordinary Bott–Chern vanishing means exactly r(ω)=dd^c F for a global real smooth function F. Taking v=F/n therefore gives zero Chern–Ricci form. Moreover, d(e^vω)=(θ+dv)∧e^vω, and [θ+dv]=[θ]≠0. This proves strictness without changing the complex structure. Two flat conformal representatives have dd^c of their logarithmic ratio zero. Taking its Hermitian trace gives an elliptic equation with no zeroth-order term; the maximum principle on connected compact X makes the ratio constant. This proves precisely the asserted uniqueness. The unitary-flat canonical interpretation in n1 also follows directly: a Bott–Chern-exact curvature can be removed by changing the line-bundle metric. It does not imply triviality or torsion of the canonical bundle. This agrees with [Tosatti, Proposition 1.1](https://arxiv.org/pdf/1401.4797v4).\n\nFor B, all tensors and integrations must indeed use g. Closedness gives T symmetric. The involution T↦T(J·,J·) is orthogonal, so T=P+T⁻ is an orthogonal decomposition. Locally θ=df and e^(−f)g is Kähler. The conformal connection difference is D_XY−∇_XY=−θ(X)Y/2−θ(Y)X/2+g(X,Y)A/2. Substitution into DJ=0 gives exactly the displayed formula for ∇J. Differentiating Jθ=−θ∘J and antisymmetrizing then gives dJθ(X,JY)=2P(X,Y)−u g(X,Y)+θ(X)θ(Y)+Jθ(X)Jθ(Y).\n\nThe normalization is correct: with d^c=i(bar∂−∂)/(4π), Jdf=4πd^c f and dJdf=4πdd^c f. Flatness consequently gives ρ(e^(−f)g)=n i∂bar∂f=(n/2)dJθ. In real dimension 2n, contracting the curvature difference of D and ∇ gives Ric_D=Ric_g+(n−1)T+(n−1)θ⊗θ/2−(q+(n−1)u)g/2. Pairing the Kähler Ricci form with J and subtracting this expression yields R=nP−(n−1)T+(q−u)g/2+θ⊗θ/2+n Jθ⊗Jθ/2. In particular, its trace is s=(n−1)q−(n−1)u/2. These are exactly the t=0 specializations of equations (2)–(4) in [Barbaro–Otiman, Section 4](https://arxiv.org/html/2509.18364v2). Their subsequent use of q=0 is not needed for these local formulas.\n\nHere are the integration checks independently. Put E_A=∫T(A,A) and E_B=∫T(B,B). Since A(u)=2T(A,A) and div A=−q, integrating div(uA) gives ∫uq=2E_A. The contracted second Bianchi identity is δR+ds/2=0 with δ the negative covariant contraction. Pairing with θ and integrating gives 0=∫⟨R,T⟩+(1/2)∫sq. Substituting the tensor and scalar formulas gives\n0=n‖P‖²−(n−1)‖T‖²+(n−2)‖q‖²/2+(4−n)E_A/2+nE_B/2.\nFor a closed one-form, commuting covariant derivatives gives Δθ=∇*∇θ+Ric(θ). Taking its integrated pairing with θ gives ‖q‖²=‖T‖²+∫R(A,A). Here R(A,A)=(1−n/2)T(A,A)+(n/2)T(B,B)+qu/2, so\n‖q‖²=‖T‖²+(4−n)E_A/2+nE_B/2.\nElimination gives 0=n(‖P‖²−‖T‖²)+n‖q‖²/2, hence ‖T⁻‖²=‖q‖²/2. No Gauduchon assumption, pointwise equality, or unproved sign of ∫uq was inserted.\n\nFor C, in a positively oriented Hermitian orthonormal frame, *θ=Jθ∧ω^(n−1)/(n−1)!. The LCK equation gives d^cω^(n−1)=(n−1)Jθ∧ω^(n−1)/(4π). Since d*θ=−q dvol, this proves dd^cω^(n−1)=−(n−1)qω^n/(4πn). Thus Gauduchon is equivalent to q=0 for this metric. When q=0, B gives T=P, hence T(B,B)=T(A,A); integration gives E_A=E_B=0, and the closed-one-form identity forces T=0. Conversely T=0 gives q=0. Finally, the local connection formula gives ∇_AJ=0. For g(SX,Y)=T(X,Y), direct expansion of Lie brackets yields (L_AJ)Y=JSY−SJY. Therefore A is real holomorphic exactly when S commutes with J, equivalently T=P. B then forces q=0 and the preceding argument forces T=0. Strictness ensures that this parallel Lee form is nonzero. This proves all four equivalences, including n=2.\n\nFor D, Γ is a subgroup: multiplication and inversion preserve integer coordinates. Its action is free, and proper discontinuity follows by bounding a,b,d and then c whenever a compact set meets one of its translates. Reduction of x,y,t and then z gives a compact fundamental set. The quotient is consequently a connected compact smooth manifold. The stated coframe is invariant under every lattice transformation, and all functions of x used below are periodic.\n\nIntegrability can be checked without relying solely on the absence of a (0,2) component. On G define w=x+iy and v=z+i(t−x²/2). Then dw=φ¹ and dv=φ²−ixφ¹. These are independent complex coordinates for the declared J. The lattice action becomes w↦w+a+ib and v↦v−iaw+c+id−ia²/2, which is holomorphic. Also Σ=φ¹∧φ²=dw∧dv is invariant and nowhere vanishing. Hence the canonical bundle is holomorphically trivial, proving the exact ordinary Bott–Chern condition on this fixed quotient.\n\nWriting a=f′, the forms θ₁=−e⁴+ae¹ and η₁=e³+ae² satisfy η₁=Jθ₁, dθ₁=0 and dη₁=−Ce¹². The coframe θ₁,η₁,e¹,e² is independent. Since C>0, g₁=θ₁²+η₁²+C((e¹)²+(e²)²) is positive Hermitian with fundamental form ω₁. Exterior differentiation gives dω₁=Cθ₁∧e¹²=θ₁∧ω₁. The t-circle has Lee period −1. Its Lee dual is −E₄=−∂t; the coefficients are independent of t, making this field Killing. Closedness makes ∇θ₁ symmetric, while Killing makes it skew, so ∇θ₁=0. This explicitly proves Vaisman existence on the same complex surface.\n\nThe volume calculation gives ω₁²/2=Ce¹²³⁴. Since Σ has constant density in that coframe, ρ(ω₁)=−i∂bar∂log C. For h=C^(−1/2), ω=hω₁ has volume e¹²³⁴ and zero Chern–Ricci form. Its Lee form is θ=−e⁴+d(f+log h), preserving the period −1. The dual frame is E₁=∂x, E₂=∂y+x∂z, E₃=∂z, E₄=∂t. Inverting the metric gives A=h′E₁+(ah′−h^(−1))E₄. Each E_i has zero divergence for the volume dx dy dz dt, so q=−h″. Differentiation of C=1+cos(2πx)/4 gives exactly q(0)=−4√5π²/25 and q(1/2)=4√3π²/9. Consequently ω is neither Gauduchon nor Vaisman. A proves that every flat conformal metric is a constant multiple of ω; its q scales by the inverse constant and cannot become zero. This proves the conformal-class obstruction while also proving why it is not a P05 counterexample.\n\nThe rejected route in n3 can also be falsified independently. Put p=h′ and r=h″. The preceding metric gives u=(p²+1)/h. Using [E₁,E₂]=E₃ and a′=1−h^(−2), direct Lie differentiation gives L_AJ(E₁)=r(E₂−aE₃), L_AJ(E₂)=r(E₁+aE₄), and zero on E₃,E₄. The two horizontal vectors have equal length, so |T⁻|²=|L_AJ|²/4=r²/2. Periodic integration gives ∫uq=−∫(p⁴/3+p²)/h²<0 for this nonconstant h. The rejected identity, specialized to n=2, would require ∫uq=∫q²>0. It is therefore false. Its explicit rejection is mathematically necessary and has been preserved; the corrected proof above does not depend on computational verdicts or unavailable scripts.\n\nThe additional notes retain their stated boundaries. In n4, A constructs a flat positive volume on a Bott–Chern Calabi–Yau manifold, and the same maximum-principle argument proves uniqueness after normalization. Biholomorphic pullback preserves flatness and total volume, proving invariance under every automorphism. Under the explicitly assumed finite free holomorphic action on a Vaisman Calabi–Yau Y, Tsukada’s cone is preserved by pullback. Its convexity and exclusion of zero make the averaged Lee class admissible and nonzero. Choose a Vaisman metric realizing that class. Its Lee and anti-Lee fields are holomorphic, so the flat volume is invariant under both flows. The prescribed-volume theorem therefore applies with all of its antecedents established. Uniqueness makes the resulting metric invariant under the finite group. Parallelness and zero Chern–Ricci curvature descend locally; exactness downstairs would imply exactness of the nonzero Lee class upstairs. A normal closure similarly handles a nonregular finite cover. None of this constructs a finite Vaisman cover from P05.\n\nIn n5, the assumed invariant Lee representative θ₀ permits the essential initial conformal correction. For the invariant volume, unimodularity gives div E_i=0, so coefficient averaging commutes with d. Constant frame coefficients of J make it commute with type decomposition and dd^c. Averaging preserves positivity and gives dS(ω′)=θ₀∧S(ω′). The lifted invariant Hermitian metric has invariant Chern–Ricci form. Applying averaging to r=dd^c F gives r=dd^c S(F)=0 because S(F) is constant. Its invariant Lee dual has zero divergence, so C proves it Vaisman. The proof requires the invariant model and Lee representability; it does not establish either for arbitrary X.\n\nIn n6, subtraction of the two same-Lee LCK equations gives θ∧dd^cφ=0. Linear algebra gives dd^cφ=aθ∧Jθ: the wedge condition first gives θ∧η, and the (1,1) condition also gives Jθ∧dd^cφ=0. For Vaisman, u is a positive constant and dJθ=−uω+θ∧Jθ. Closedness yields 0=da∧θ∧Jθ+a uθ∧ω. Evaluating on A and two horizontal vectors gives a u²ω(v,w)=0. The horizontal form is nondegenerate in every n≥2, so a=0 and φ is constant. This correctly rules out only the ordinary dd^c ansatz with unchanged Lee form.\n\nIn n7, the positive automorphic potential and n≥3 are additional antecedents. The primary approximation theorem has the required ≥3 threshold; the extracted PDF text misreads its inequality, whereas the [primary HTML statement](https://arxiv.org/html/2112.03363v2) retains it correctly. Proper-potential approximation stays on the same complex manifold, and a fixed nonzero Lee period persists under sufficiently small perturbations. The stronger theorem supplies J_i=ν_i(J) converging smoothly to a Vaisman J∞, so ordinary Bott–Chern vanishing holds on every biholomorphic approximant.\n\nThe canonical-degree limit is justified without controlling the potentials F_i. Choose smoothly converging Hermitian backgrounds β_i. The equation dd^c_i(v_iβ_i^(n−1))=0 is linear elliptic in v_i. Its positive kernel is one-dimensional; imposing an integral normalization gives an invertible equation on the complementary subspace. Small operator perturbations and elliptic regularity consequently give converging normalized Gauduchon metrics γ_i. Integration by parts gives ∫r_i∧γ_i^(n−1)=0, and smooth convergence passes this equality to the limit. Nearby almost complex structures are homotopic, so c₁ in real de Rham cohomology also vanishes at the limit.\n\nThe Vaisman Bott–Chern kernel inference needs more than an arbitrary vector-space dimension comparison. It can be verified from the cited harmonic description. For n≥3, a Bott–Chern (1,1) harmonic representative is basic harmonic. If it is de Rham exact, average a primitive over the compact closure of the two Vaisman flows and write that primitive as ζ+aθ+bJθ with ζ basic. Horizontality of its derivative forces da=db=0. Thus its basic class is a multiple of κ=−dJθ; basic Hodge orthogonality gives the same statement for the harmonic representative. The class of κ is nonzero, since κ is semipositive of rank n−1 and has strictly positive integral against every positive Gauduchon (n−1)-power. This proves the required one-dimensional kernel consequence independently of an unstated compatibility of abstract isomorphisms. Zero canonical degree therefore forces c₁^BC(J∞)=0. Istrati’s stability theorem now has its full antecedent. The local Kuranishi parametrization places sufficiently close J_i in its deformation neighborhood modulo diffeomorphism, and biholomorphic pullback returns a Vaisman metric to the original J. Its parallel nonzero Lee form cannot be exact on a compact manifold. This establishes the potential subclass, without proving that P05 manifolds have potential.\n\nThe primary sources retain the restrictions described in n1. [Barbaro–Otiman Theorem A](https://arxiv.org/html/2509.18364v2) requires one metric to be both flat and Gauduchon. [Ornea–Verbitsky Theorem 4.1](https://arxiv.org/html/2206.08808v2) starts with an already Vaisman manifold and requires both flow invariances. [Istrati Corollary 5.2 and Theorem 5.7](https://arxiv.org/html/2304.02582v1) likewise start in the Vaisman setting. No such theorem removes the missing antecedent in the original problem.\n\nTwo harmless clarifications are appropriate: explicitly define d^c=i(bar∂−∂)/(4π) before using it, and translate consistently between a Riemannian volume μ and the prescribed form ω^n=n!μ when applying the volume theorem. Neither changes an argument. No substantial repair of A–D is needed. The missing full-existence mechanism or actual counterexample remains the substantive outstanding work.",
  "passages": [
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/0",
      "statement": "Tsukada, Theorem 5.1 and its constructive proof: Let Y be a connected compact complex manifold of complex dimension at least two carrying a Vaisman metric with nonzero parallel Lee form θ₀. Let H be the real subspace of H¹_dR(Y;R) consisting of classes of real parts of closed holomorphic one-forms. Then H¹_dR(Y;R)=R[θ₀]⊕H, the strictly LCK Lee classes are exactly {t[θ₀]+η:t>0, η∈H}, and every class in this set is realized by a Vaisman metric on the same complex manifold Y.",
      "url": "https://www.numdam.org/article/CM_1994__93_1_1_0.pdf",
      "quote": "We shall show that g is an l.c.K. metric with parallel Lee form",
      "premise": 0
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/1",
      "statement": "Ornea–Verbitsky, Theorem 4.1: Let (Y,ω,θ) be a compact Vaisman manifold of complex dimension n≥2. If V′ is a smooth positive volume form invariant under both θ♯ and Jθ♯ and satisfies ∫Y V′=∫Y ωⁿ, then there exists a unique Vaisman metric ω′ on the same complex manifold with Lee class [θ] and (ω′)ⁿ=V′.",
      "url": "https://arxiv.org/html/2206.08808v2",
      "quote": "a Lee- and anti-Lee-invariant volume form",
      "premise": 1
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/2",
      "statement": "Ornea–Verbitsky, Theorem 4.1: Let (Y,ω,θ) be a compact Vaisman manifold of complex dimension n≥2. If V′ is a smooth positive volume form invariant under both θ♯ and Jθ♯ and satisfies ∫Y V′=∫Y ωⁿ, then there exists a unique Vaisman metric ω′ on the same complex manifold with Lee class [θ] and (ω′)ⁿ=V′.",
      "url": "https://arxiv.org/html/2206.08808v2",
      "quote": "Then there exists a unique Vaisman metric ω′ on M with the same Lee class",
      "premise": 1
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/3",
      "statement": "Istrati, Corollary 5.2: On a compact Vaisman manifold Y with ordinary c₁^BC(T_Y)=0, every Lee class of a Vaisman metric is realized by a Chern–Ricci-flat Vaisman metric, unique up to multiplication by a positive constant.",
      "url": "https://arxiv.org/html/2304.02582v1",
      "quote": "a unique Chern-Ricci flat Vaisman metric",
      "premise": 2
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/4",
      "statement": "Istrati, Theorem 5.7: If Y is a compact Vaisman manifold with ordinary c₁^BC(T_Y)=0, its Kuranishi space is a smooth universal deformation space, and every sufficiently small complex deformation is again Vaisman with ordinary first Bott–Chern class zero.",
      "url": "https://arxiv.org/html/2304.02582v1",
      "quote": "any small deformation of X is again Vaisman Calabi-Yau.",
      "premise": 3
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/5",
      "statement": "Ornea–Verbitsky, Theorem 4.8: A compact LCK structure with an improper positive automorphic LCK potential can be approximated in the C∞ topology, including its metric, Lee form and potential data, by LCK structures with proper potential on the same complex manifold.",
      "url": "https://arxiv.org/html/2112.03363v2",
      "quote": "by an LCK structure with proper LCK potential on the same complex manifold.",
      "premise": 4
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/6",
      "statement": "Ornea–Verbitsky, Theorem 7.3: For a compact complex manifold (M,J) of complex dimension at least three admitting an LCK structure with positive automorphic potential, there exist a Vaisman-type complex structure J∞ on M and diffeomorphisms ν_i∈Diff₀(M) such that ν_i(J) converges to J∞ in the C∞ topology.",
      "url": "https://arxiv.org/html/2112.03363v2",
      "quote": "a sequence of diffeomorphisms",
      "premise": 5
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/7",
      "statement": "Istrati–Otiman, Theorem 4.2 and Corollary 5.1: For a compact Vaisman manifold of complex dimension n≥3, every Bott–Chern (1,1) class has a representative harmonic for the basic cohomology of its canonical foliation. Its de Rham, Dolbeault and Bott–Chern cohomologies are computed by A=H_B(ℱ)⊗Λ(u,ū), with deg u=(1,0), deg ū=(0,1), both differentials zero on H_B(ℱ), ∂u=0, bar∂ū=0 and bar∂u=[κ]=−∂ū, where κ is the transverse Kähler form.",
      "url": "https://arxiv.org/html/2206.07312v2",
      "quote": "model for all three cohomologies of X",
      "premise": 6
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/8",
      "statement": "Gauduchon’s normalized-kernel theorem: For a connected compact Hermitian manifold of complex dimension n≥2, the scalar linear elliptic equation dd^c(vβ^(n−1))=0 has a one-dimensional real kernel generated by a strictly positive smooth function. Consequently its positive conformal Gauduchon factor is unique after an integral normalization.",
      "url": "https://numdam.org/item/AST_1985__126__129_0.pdf",
      "quote": "Le lemme 1 dénontre l'assertion d'unicité du Théorème 2.",
      "premise": 7
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/9",
      "statement": "The local Kuranishi parametrization for a compact complex manifold (M,J₀) has the following property: every sufficiently close integrable complex structure on M is equivalent by a diffeomorphism to a fiber of the Kuranishi family, with the fiber parameter tending to the central parameter as the complex structure tends to J₀. The local construction is described in Kuranishi’s completeness theorem and Meersseman, Section 1, Proposition K1 and the ensuing finite-dimensional parametrization.",
      "url": "https://www.numdam.org/item/10.24033/asens.2148.pdf",
      "quote": "Ξ(α) and α induce isomorphic almost complex structures on Xdiff.",
      "premise": 8
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/10",
      "statement": "The local Kuranishi parametrization for a compact complex manifold (M,J₀) has the following property: every sufficiently close integrable complex structure on M is equivalent by a diffeomorphism to a fiber of the Kuranishi family, with the fiber parameter tending to the central parameter as the complex structure tends to J₀. The local construction is described in Kuranishi’s completeness theorem and Meersseman, Section 1, Proposition K1 and the ensuing finite-dimensional parametrization.",
      "url": "https://www.numdam.org/item/10.24033/asens.2148.pdf",
      "quote": "The Kuranishi space K is the set of integrable structures in W.",
      "premise": 8
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/11",
      "statement": "The local Kuranishi parametrization for a compact complex manifold (M,J₀) has the following property: every sufficiently close integrable complex structure on M is equivalent by a diffeomorphism to a fiber of the Kuranishi family, with the fiber parameter tending to the central parameter as the complex structure tends to J₀. The local construction is described in Kuranishi’s completeness theorem and Meersseman, Section 1, Proposition K1 and the ensuing finite-dimensional parametrization.",
      "url": "https://link.springer.com/chapter/10.1007/978-3-642-48016-4_13",
      "quote": "We are here interested in the local aspect of the theory",
      "premise": 8
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/12",
      "statement": "The local Kuranishi parametrization for a compact complex manifold (M,J₀) has the following property: every sufficiently close integrable complex structure on M is equivalent by a diffeomorphism to a fiber of the Kuranishi family, with the fiber parameter tending to the central parameter as the complex structure tends to J₀. The local construction is described in Kuranishi’s completeness theorem and Meersseman, Section 1, Proposition K1 and the ensuing finite-dimensional parametrization.",
      "url": "https://arxiv.org/html/2304.02582v1",
      "quote": "parametrising all small deformations of J",
      "premise": 8
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/13",
      "statement": "Istrati–Otiman, Theorem 4.2 and Corollary 5.1: For a compact Vaisman manifold of complex dimension n≥3, every Bott–Chern (1,1) class has a representative harmonic for the basic cohomology of its canonical foliation. Its de Rham, Dolbeault and Bott–Chern cohomologies are computed by A=H_B(ℱ)⊗Λ(u,ū), with deg u=(1,0), deg ū=(0,1), both differentials zero on H_B(ℱ), ∂u=0, bar∂ū=0 and bar∂u=[κ]=−∂ū, where κ is the transverse Kähler form.",
      "url": "https://arxiv.org/html/2304.02582v1",
      "quote": "is one-dimensional, generated by the class of a transverse Kähler metric.",
      "premise": 6
    },
    {
      "id": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8/14",
      "statement": "Gauduchon’s normalized-kernel theorem: For a connected compact Hermitian manifold of complex dimension n≥2, the scalar linear elliptic equation dd^c(vβ^(n−1))=0 has a one-dimensional real kernel generated by a strictly positive smooth function. Consequently its positive conformal Gauduchon factor is unique after an integral normalization.",
      "url": "urn:xean:task",
      "quote": "Vanishing c_1^{BC} supplies a Chern-Ricci-flat conformal representative; the conformal Gauduchon theorem separately supplies a Gauduchon representative.",
      "premise": 7
    }
  ],
  "premises": [
    "Tsukada, Theorem 5.1 and its constructive proof: Let Y be a connected compact complex manifold of complex dimension at least two carrying a Vaisman metric with nonzero parallel Lee form θ₀. Let H be the real subspace of H¹_dR(Y;R) consisting of classes of real parts of closed holomorphic one-forms. Then H¹_dR(Y;R)=R[θ₀]⊕H, the strictly LCK Lee classes are exactly {t[θ₀]+η:t>0, η∈H}, and every class in this set is realized by a Vaisman metric on the same complex manifold Y.",
    "Ornea–Verbitsky, Theorem 4.1: Let (Y,ω,θ) be a compact Vaisman manifold of complex dimension n≥2. If V′ is a smooth positive volume form invariant under both θ♯ and Jθ♯ and satisfies ∫Y V′=∫Y ωⁿ, then there exists a unique Vaisman metric ω′ on the same complex manifold with Lee class [θ] and (ω′)ⁿ=V′.",
    "Istrati, Corollary 5.2: On a compact Vaisman manifold Y with ordinary c₁^BC(T_Y)=0, every Lee class of a Vaisman metric is realized by a Chern–Ricci-flat Vaisman metric, unique up to multiplication by a positive constant.",
    "Istrati, Theorem 5.7: If Y is a compact Vaisman manifold with ordinary c₁^BC(T_Y)=0, its Kuranishi space is a smooth universal deformation space, and every sufficiently small complex deformation is again Vaisman with ordinary first Bott–Chern class zero.",
    "Ornea–Verbitsky, Theorem 4.8: A compact LCK structure with an improper positive automorphic LCK potential can be approximated in the C∞ topology, including its metric, Lee form and potential data, by LCK structures with proper potential on the same complex manifold.",
    "Ornea–Verbitsky, Theorem 7.3: For a compact complex manifold (M,J) of complex dimension at least three admitting an LCK structure with positive automorphic potential, there exist a Vaisman-type complex structure J∞ on M and diffeomorphisms ν_i∈Diff₀(M) such that ν_i(J) converges to J∞ in the C∞ topology.",
    "Istrati–Otiman, Theorem 4.2 and Corollary 5.1: For a compact Vaisman manifold of complex dimension n≥3, every Bott–Chern (1,1) class has a representative harmonic for the basic cohomology of its canonical foliation. Its de Rham, Dolbeault and Bott–Chern cohomologies are computed by A=H_B(ℱ)⊗Λ(u,ū), with deg u=(1,0), deg ū=(0,1), both differentials zero on H_B(ℱ), ∂u=0, bar∂ū=0 and bar∂u=[κ]=−∂ū, where κ is the transverse Kähler form.",
    "Gauduchon’s normalized-kernel theorem: For a connected compact Hermitian manifold of complex dimension n≥2, the scalar linear elliptic equation dd^c(vβ^(n−1))=0 has a one-dimensional real kernel generated by a strictly positive smooth function. Consequently its positive conformal Gauduchon factor is unique after an integral normalization.",
    "The local Kuranishi parametrization for a compact complex manifold (M,J₀) has the following property: every sufficiently close integrable complex structure on M is equivalent by a diffeomorphism to a fiber of the Kuranishi family, with the fiber parameter tending to the central parameter as the complex structure tends to J₀. The local construction is described in Kuranishi’s completeness theorem and Meersseman, Section 1, Proposition K1 and the ensuing finite-dimensional parametrization."
  ],
  "kind": "codex-report",
  "operationId": "04f06528-4aa0-4f91-a2ab-8f0130ef7ee8",
  "reportedAt": "2026-10-06T06:37:53.463Z"
}
```


## Complete independent statement-only reconstruction

ALL five ordinary notes follow unchanged. No author proof or prior report was supplied. Native candidate=true concerns only A--D, not original P05. The independent B proof uses exterior Stokes; every step must be compared to the article contracted Bianchi route. Its failed pointwise diagnostic is preserved, not turned into a general pointwise claim. The publicly checked Moroianu2018 theorem is corroborating only; the needed flat implication is independently proved, with no external rigidity theorem left as a premise.

```json
{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "A is proved with the stated normalization: every strict LCK conformal class on compact connected X with ordinary c1BC(TX)=0 has the flat representative exp(F/n)omega, unique up to positive scale. Its Lee class remains nonzero.",
      "detailedSummary": "Ordinary Bott–Chern vanishing gives a global real F with rho(omega)/(2pi)=dd^c F. The conformal determinant formula cancels curvature for exp(F/n)omega. Two flat conformal representatives have a pluriharmonic logarithmic ratio, which is constant on compact connected X. Conformal scaling changes the Lee form by an exact form. No Gauduchon conclusion follows.",
      "text": "Claim A. Use dd^c=i partial barpartial/(2pi), rho(g)=-i partial barpartial log det(g), and ordinary c1BC(TX)=[rho(g)/(2pi)].\n\nVanishing of the ordinary Bott–Chern class means that rho(omega)/(2pi)=dd^c F for a global smooth real function F. A complex potential, if used in defining the group, can be replaced by its real part. With the required normalization, rho(omega)=i partial barpartial F.\n\nFor any global real u, the Hermitian matrix of exp(u)omega is exp(u) times the original matrix. In complex dimension n this gives\n  rho(exp(u)omega)=rho(omega)-n i partial barpartial u.\nTaking u=F/n proves rho(exp(F/n)omega)=0. Direct differentiation gives\n  d(exp(u)omega)=(theta+du) wedge exp(u)omega.\nThus the new Lee form is theta+dF/n, is closed, and has the same nonzero de Rham class. Positivity is preserved.\n\nIf exp(u)omega and exp(v)omega are both flat, partial barpartial(u-v)=0. In every holomorphic coordinate ball, u-v is harmonic for the Euclidean Laplacian. It attains a maximum on compact X. The harmonic mean-value property shows that it is constant near every maximum point: the average of values bounded above by the maximum can equal that maximum only if all the values equal it. The maximum set is therefore open and closed. Connectedness makes u-v constant globally, proving uniqueness up to a positive constant.\n\nThis proves A. It neither assumes nor proves that the flat representative is Gauduchon.\n\nArtifacts: input.json preserves the supplied statement-only input; proof.txt and notes.json contain the assembled arguments. Rerun the supplementary symbolic checks with python verify.py > verification-output.json. The ordinary argument above, rather than program execution, establishes A.\n\nArtifacts: /workspace/research/native-workers/codex-EkrwhP",
      "support": []
    },
    {
      "id": "n2",
      "summary": "B is proved without a Gauduchon assumption: for every compact Chern–Ricci-flat strict LCK metric, int |Tminus|^2=(1/2)int q^2. The proof retains Riemannian curvature and uses Stokes; it asserts no pointwise equality.",
      "detailedSummary": "For s=|theta|^2, eta=Jtheta and p(U,V)=P(JU,V), local conformal Kähler calculations give d eta=2p-s omega+theta wedge eta and Ric_g=nP-(n-1)T+(theta tensor theta)/2+n(eta tensor eta)/2+(q-s)g/2. Closed-form Bochner gives int q^2=int(|T|^2+Ric(A,A)). Stokes applied to eta wedge d eta wedge omega^(n-2) gives int(2|P|^2+2nP(A,A))=int(q^2+(n-2)qs). Integration by parts and substitution prove B, including n=2 and zeros of theta.",
      "text": "Claim B. Fix the compact Chern–Ricci-flat LCK metric g. Let omega(U,V)=g(JU,V), A=theta sharp, T=nabla theta, P(U,V)=(T(U,V)+T(JU,JV))/2, Tminus=T-P, and q=d*_g theta=-tr_g T. Set s=|theta|_g^2, B=JA and eta=Jtheta=g(B,.), with Jalpha=-alpha composed with J. All norms, contractions, divergences and volume measures below use this same g.\n\nBecause dtheta=0, T is symmetric. Averaging by J splits symmetric tensors orthogonally into their J-invariant and J-anti-invariant parts, so\n  |T|^2=|P|^2+|Tminus|^2.\n\nFirst derive the local identities. On a contractible coordinate neighborhood theta=du and g0=exp(-u)g has closed positive fundamental form, hence is Kähler. This implication can be checked in holomorphic coordinates: closedness gives partial_i(g0)_{j bar k}=partial_j(g0)_{i bar k} and their conjugates. The Levi–Civita connection has no mixed Christoffel symbols and preserves the complex type subbundles, so nabla0 J=0.\n\nThe Koszul formula gives\n  nabla0_X Y=nabla_X Y-[theta(X)Y+theta(Y)X-g(X,Y)A]/2.\nSubstituting into nabla0 J=0 yields\n  (nabla_X J)Y=[theta(JY)X-theta(Y)JX+g(X,Y)B-g(X,JY)A]/2.  (1)\nIn particular nabla_A J=0. If S is the self-adjoint endomorphism obtained by raising an index of T, then\n  nabla_X B=JSX+[-sJX+theta(X)B-eta(X)A]/2.\nDefine the real (1,1)-form p(U,V)=P(JU,V). Alternating the preceding identity gives\n  d eta=2p-s omega+theta wedge eta.                         (2)\nIndeed its Hessian term is -T(U,JV)+T(V,JU)=2P(JU,V); the remaining terms give -s omega+theta wedge eta. Flatness was not needed for (1)–(2).\n\nNext derive the Riemannian Ricci tensor. With the specified J convention,\n  dJdu=2i partial barpartial u.\nThe conformal determinant formula and rho(g)=0 give\n  rho(g0)=n i partial barpartial u=(n/2)dJdu.\nFor a Kähler metric, Ric0(U,V)=rho(g0)(U,JV). Its normalization follows from the holomorphic connection Gamma^k_{ij}=(g0)^{k bar l} partial_i(g0)_{j bar l}, whose Ricci components are -partial_i partial_bar_j log det(g0). Since nabla0 J=0,\n  (dJdu)(U,JV)=Hess0 u(U,V)+Hess0 u(JU,JV).\nThe connection change also gives\n  Hess0 u=T+theta tensor theta-(s/2)g.\nConsequently\n  Ric0=nP+(n/2)(theta tensor theta+eta tensor eta)-(ns/2)g.\n\nFor completeness, the real conformal Ricci formula is obtained by contracting a connection difference. If g'=exp(2v)g in real dimension m, then\n  C^k_{ij}=delta^k_i v_j+delta^k_j v_i-g_{ij}v^k.\nThe differentiated terms in the Ricci difference equal -(m-2)Hess v-g Delta v, and the quadratic terms equal (m-2)(dv tensor dv-|dv|^2g). Thus\n  Ric(g')=Ric(g)-(m-2)(Hess v-dv tensor dv)\n                    -(Delta v+(m-2)|dv|^2)g.\nApply this with m=2n and v=-u/2, using Delta u=tr T=-q:\n  Ric0=Ric(g)+(n-1)T+(n-1)(theta tensor theta)/2\n                    +[-q/2-(n-1)s/2]g.\nCombining the two expressions for Ric0 proves\n  Ric(g)=nP-(n-1)T+(theta tensor theta)/2\n                      +n(eta tensor eta)/2+(q-s)g/2.       (3)\nAlthough derived locally, this identity consists entirely of global tensors. Evaluating on A gives\n  Ric(A,A)=nP(A,A)-(n-1)T(A,A)+qs/2.                       (4)\n\nThe required integrated Bochner formula retains this curvature term. In normal coordinates, symmetry of T and commuting covariant derivatives give\n  nabla^i T_{ij}=nabla_j(tr T)+Ric_{jk}A^k\n               =-partial_j q+Ric_{jk}A^k.\nIntegrating nabla_i theta_j T^{ij} by parts on compact X without boundary yields\n  int |T|^2=int <theta,dq>-int Ric(A,A)\n            =int q^2-int Ric(A,A).\nTherefore\n  int q^2=int (|T|^2+Ric(A,A)).                            (5)\nAlso A(s)=2T(A,A) and div_g A=-q. Integrating div_g(sA) gives\n  int T(A,A)=(1/2)int qs.                                 (6)\n\nThe other integrated relation follows from exterior algebra. Write Lambda for contraction with omega, so Lambda omega=n. For real (1,1)-forms alpha,beta,\n  alpha wedge beta wedge omega^(n-2)\n    =[(Lambda alpha)(Lambda beta)-<alpha,beta>]\n        omega^n/[n(n-1)].                                 (7)\nTo verify this, diagonalize a real (1,1)-form in a unitary real frame. If alpha=sum a_j x_j wedge Jx_j, then Lambda alpha=sum a_j and |alpha|^2=sum a_j^2; expanding its square gives (7) when alpha=beta. Polarization gives the mixed formula, without requiring simultaneous diagonalization.\n\nThe relevant contractions are\n  Lambda p=-q/2,              |p|^2=|P|^2/2,\n  Lambda(theta wedge eta)=s,  <theta wedge eta,p>=P(A,A).\nFor the last equality, use a unitary frame with first vector along A when A is nonzero. Then p(A,JA)=P(JA,JA)=P(A,A). At A=0 both sides vanish.\n\nPut beta=2p-s omega. Then d eta=beta+theta wedge eta. Applying Stokes to the global form eta wedge d eta wedge omega^(n-2), and using d omega^(n-2)=(n-2)theta wedge omega^(n-2), gives\n  0=int [d eta wedge d eta+(n-2)theta wedge eta wedge d eta]\n                                                        wedge omega^(n-2)\n   =int [beta wedge beta+n theta wedge eta wedge beta]\n                                                        wedge omega^(n-2). (8)\nFor n=2 the term carrying n-2 simply vanishes.\n\nThe numerators in (7) for these two terms are, respectively,\n  q^2+2(n-1)qs+n(n-1)s^2-2|P|^2,\n  -qs-(n-1)s^2-2P(A,A).\nAdding n times the second numerator to the first cancels s^2. Since omega^n=n! dvol_g, (8) becomes\n  int (2|P|^2+2nP(A,A))=int [q^2+(n-2)qs].                (9)\n\nSubstitute (4) and (6) into (5), and split T orthogonally:\n  int q^2=int [|P|^2+|Tminus|^2+nP(A,A)-(n-2)qs/2].\nEquation (9) replaces int[|P|^2+nP(A,A)] by (1/2)int[q^2+(n-2)qs]. The qs terms cancel, proving\n  int_X |Tminus|^2 dvol_g=(1/2)int_X q^2 dvol_g.\n\nThis is an ordinary integrated proof. It assumes neither Gauduchon nor a unit or nowhere-zero Lee form, and it includes n=2. Stokes and integration by parts provide no pointwise equality.\n\nArtifacts: proof.txt records the derivation. verify.py checks the displayed polynomial cancellations and D's real-frame calculations. Rerun python verify.py > verification-output.json. These symbolic checks corroborate the encoded algebra; the general result rests on the proof above.\n\nArtifacts: /workspace/research/native-workers/codex-EkrwhP",
      "support": []
    },
    {
      "id": "n3",
      "summary": "C is proved for one fixed compact Chern–Ricci-flat strict LCK metric: Gauduchon, q=0, holomorphic Lee vector, and Vaisman are equivalent. Exactly dd^c omega^(n-1)=-(n-1)q omega^n/(4pi n).",
      "detailedSummary": "The Gauduchon-divergence equivalence follows by differentiating d^c omega^(n-1). For every LCK metric, nabla_A J=0 gives L_A J=JS-SJ, so holomorphicity is equivalent to Tminus=0. B then equates holomorphicity and q=0 in the flat case. Once q=0, B gives P=T; the flat Ricci identity gives Ric(A,A)=T(A,A), whose integral vanishes. Bochner therefore forces T=0. Strictness ensures the resulting parallel Lee form is nonzero.",
      "text": "Claim C. Fix the same flat metric throughout, and use the identities proved in n2.\n\nDefine d^c=i(barpartial-partial)/(4pi), so dd^c=i partial barpartial/(2pi). Extend J multiplicatively to forms. On a (k,k)-form sigma, Jd sigma=i(barpartial-partial)sigma. Since Jomega=omega and d omega^(n-1)=(n-1)theta wedge omega^(n-1),\n  d^c omega^(n-1)=(n-1)eta wedge omega^(n-1)/(4pi).\nDifferentiating, with eta wedge theta=-theta wedge eta, gives\n  dd^c omega^(n-1)\n    =(n-1)[d eta+(n-1)theta wedge eta] wedge omega^(n-1)/(4pi).\nBy (2) of n2,\n  Lambda[d eta+(n-1)theta wedge eta]=-q-ns+ns=-q.\nThe elementary identity alpha wedge omega^(n-1)=(Lambda alpha)omega^n/n therefore yields\n  dd^c omega^(n-1)=-(n-1)q omega^n/(4pi n).                 (10)\nSince n>=2 and omega^n is positive, the metric is Gauduchon exactly when q=0. This calculation holds for every LCK metric, without flatness.\n\nLet S be T with one index raised. Formula (1) in n2 gives nabla_A J=0. The torsion-free connection gives\n  (L_A J)Y=(nabla_A J)Y-nabla_{JY}A+J nabla_Y A=JSY-SJY.\nThus A is real holomorphic exactly when S commutes with J, equivalently T(JU,JV)=T(U,V), equivalently Tminus=0.\n\nIf q=0, B gives int|Tminus|^2=0, hence Tminus=0 everywhere. Conversely, holomorphic A implies Tminus=0 and B gives int q^2=0, hence q=0. Smoothness and nonnegativity justify both conclusions.\n\nTo strengthen q=0 to parallelness, we now have P=T. Formula (4) of n2 reduces to\n  Ric(A,A)=nT(A,A)-(n-1)T(A,A)=T(A,A).\nEquation (6) gives int T(A,A)=int qs/2=0. Consequently the closed-one-form Bochner identity becomes\n  0=int |T|^2+int T(A,A)=int |T|^2.\nHence T=nabla theta=0 everywhere. A parallel form on connected X has constant norm, and it cannot be identically zero because [theta] is nonzero. The metric is therefore Vaisman as defined in the question. Conversely, a Vaisman metric has T=0 and q=0.\n\nThis proves the four equivalences for precisely the fixed flat metric. No step combines properties belonging to distinct conformal representatives.\n\nArtifacts: proof.txt and notes.json contain the argument. Rerun the supplementary checks with python verify.py > verification-output.json. No separate rigidity theorem is indispensable: its needed flat-case implication was proved directly.\n\nArtifacts: /workspace/research/native-workers/codex-EkrwhP",
      "support": [
        "n2"
      ]
    },
    {
      "id": "n4",
      "summary": "D is proved on the fixed Kodaira surface: omega1 is strict LCK and Vaisman; omega=C^(-1/2)omega1 is strict LCK and Chern–Ricci flat with q=-h'' and the stated values. Its conformal class has no flat Gauduchon metric, though it contains omega1.",
      "detailedSummary": "The integer subgroup acts freely and properly, and every orbit meets a compact cube. Explicit holomorphic coordinates w=x+iy and v=z+i(t-x^2/2) give integrability, a holomorphic affine lattice action, and invariant canonical form. The positive metric g1=C(e1^2+e2^2)+theta1^2+eta1^2 has Lee vector -E4, whose closed dual and Killing property imply parallelness. Its Hermitian determinant is a constant times C, proving ordinary Bott–Chern vanishing and flatness after scaling by h. The flat volume is dx dy dz dt, and its Lee vector is h'E1+(f'h'-h^(-1))E4, giving q=-h''. A and C establish the same-class obstruction without obstructing Vaisman existence on X.",
      "text": "Claim D. Use exactly the group, lattice, complex structure and functions supplied. Put a=f', C=1-a'=1+cos(2pi x)/4, h=C^(-1/2), and H=log h.\n\nThe compact quotient. Associativity of the multiplication follows by comparing a triple product's z coordinates: both contain the cross terms xy'+xy''+x'y''. The identity is the origin and the inverse of (x,y,z,t) is (-x,-y,-z+xy,-t), so Gamma=Z^4 is a subgroup. Left multiplication by gamma=(m,k,p,l) sends\n  (x,y,z,t) to (x+m,y+k,z+p+my,t+l).\nThe action is free. It is properly discontinuous: intersection of a compact set with its translate bounds m,k,l by the x,y,t coordinates, then bounds p by the z coordinate. Only finitely many lattice elements are possible.\n\nChoose m,k to reduce x,y modulo integers, then p to reduce z+my, and l to reduce t. Every orbit therefore meets the closed cube [0,1]^4. Its image is compact and surjects onto X. The quotient is a smooth connected compact manifold without boundary. The invariant global coframe satisfies\n  e1=dx, e2=dy, e3=dz-xdy, e4=dt,\n  de1=de2=de4=0, de3=-e1 wedge e2.\nAll prescribed functions descend because their x dependence has period one.\n\nIntegrability of the fixed complex structure. On G set\n  w=x+iy, v=z+i(t-x^2/2).\nThis is a smooth diffeomorphism to C^2: recover x=Re w, y=Im w, z=Re v, t=Im v+x^2/2. Its differentials satisfy\n  dw=phi1, dv=phi2-i x phi1.\nThus they span exactly the declared (1,0)-cotangent bundle, proving integrability directly. The lattice action is holomorphic:\n  w maps to w+m+ik,\n  v maps to v-i m w+p+i l-i m^2/2.\nIts complex Jacobian determinant is one. Consequently\n  Omega=dw wedge dv=phi1 wedge phi2\nis a descended nowhere-zero holomorphic (2,0)-form.\n\nThis is the usual primary Kodaira surface model. Projection by w modulo Z+iZ gives a holomorphic principal elliptic bundle over C/(Z+iZ), with fiber v modulo Z+iZ. Changes of local base lift act on fibers by the displayed holomorphic translations. The x and y lattice generators have commutator the central z generator, and the whole commutator subgroup is generated by that element. Thus Gamma_ab=Z^3. Since G is contractible, b1(X)=3. In particular the bundle is topologically nontrivial: a trivial bundle would be a product with abelian fundamental group of rank four. These explicit facts identify the primary Kodaira construction without invoking a classification theorem for the metric claims.\n\nPositivity and strict LCK. The specified convention gives\n  Je1=e2, Je2=-e1, Je3=e4, Je4=-e3,\nso eta1=Jtheta1. Since 3/4<=C<=5/4, the J-paired coframe sqrt(C)e1, sqrt(C)e2, theta1, eta1 is everywhere nonsingular. The associated positive metric is\n  g1=C(e1 tensor e1+e2 tensor e2)\n                   +theta1 tensor theta1+eta1 tensor eta1. (11)\nIts fundamental form is omega1. Scaling by h>0 preserves positivity.\n\nSince theta1=-e4+df, it is closed. The structure equations give\n  d eta1=(-1+f'')e1 wedge e2=-C e1 wedge e2,\n  d(C e1 wedge e2)=0.\nTherefore\n  d omega1=-theta1 wedge d eta1\n           =C theta1 wedge e1 wedge e2=theta1 wedge omega1.\nFor omega=h omega1,\n  d omega=(theta1+dH) wedge omega,\n  theta=theta1+dH=-e4+d(f+log h).\nBoth Lee forms are closed. The t loop from 0 to 1 at fixed (x,y,z) is closed in the quotient, and each Lee form integrates to -1 along it. Both are nonexact, proving strictness.\n\nVaisman on this same X. The global dual frame is\n  E1=partial_x, E2=partial_y+x partial_z,\n  E3=partial_z, E4=partial_t.\nEquation (11) gives g1(-E4,.)=a e1-e4=theta1. Hence the Lee vector is A1=-E4, of norm one. Translation in t preserves the coframe and every metric coefficient, so A1 is Killing. A vector with closed metric dual has symmetric covariant derivative tensor; a Killing vector has skew-symmetric covariant derivative tensor. Both properties force nabla^{g1}theta1=0. Thus omega1 is Vaisman on the given X.\n\nOrdinary Bott–Chern vanishing and flatness. Let\n  mu=e1 wedge e2 wedge e3 wedge e4=dx wedge dy wedge dz wedge dt.\nSquaring gives omega1^2/2=C mu. The determinant can also be seen directly: theta1+i eta1=a phi1+i phi2, so (11) is the Hermitian sum C|phi1|^2+|a phi1+i phi2|^2, whose Hermitian determinant is C up to the fixed component convention. The coframe change dw=phi1, dv=phi2-i x phi1 has complex determinant one. Therefore in holomorphic coordinates det(g1) is a fixed positive constant times C. It follows that\n  rho(g1)=-i partial barpartial log C,\n  rho(g1)/(2pi)=-dd^c log C.\nThe global real function log C proves ordinary c1BC(TX)=0; no cohomology with local coefficients is involved.\n\nIn complex dimension two, multiplying g1 by h multiplies its Hermitian determinant by h^2. Since h^2C=1, g=h g1 has constant Hermitian determinant in these holomorphic coordinates, hence rho(g)=0. Equivalently, n1 with F=-log C gives the flat metric exp(F/2)omega1=h omega1. Its volume form is\n  dvol_g=h^2C mu=mu.                                      (12)\n\nDivergence for this flat metric. In the real coframe, g1 has matrix\n  [ C+a^2   0       0    -a ]\n  [ 0       C+a^2   a     0 ]\n  [ 0       a       1     0 ]\n  [ -a      0       0     1 ].\nThe (E1,E4) block of its inverse is C^(-1)[1 a; a C+a^2]. The Lee form has components (a+H',0,0,-1). Raising them with g=h g1 gives\n  A=(H'/(hC))E1+(aH'/(hC)-1/h)E4\n    =h'E1+(a h'-1/h)E4,                                  (13)\nusing h^2C=1. By (12), divergence is against coordinate volume mu. The coefficients depend only on x, while E1=partial_x and E4=partial_t. Hence\n  div_g A=h'', q=d*_g theta=-h''.                          (14)\nThe sharp operation, flatness and divergence all belong to the same metric.\n\nNow C'=-(pi/2)sin(2pi x), C''=-pi^2 cos(2pi x), and\n  h''=(3/4)C^(-5/2)(C')^2-(1/2)C^(-3/2)C''.\nAt x=0, C=5/4 and C'=0, so\n  q(0)=-4sqrt(5)pi^2/25.\nAt x=1/2, C=3/4 and C'=0, so\n  q(1/2)=4sqrt(3)pi^2/9.\nThus q is nonzero. Formula (10) proves omega is not Gauduchon. A parallel Lee form has zero divergence, so omega is not Vaisman either.\n\nBy n1, every other flat representative in this conformal class is c omega with c>0. In dimension two, dd^c(c omega)=c dd^c omega is nonzero. The class therefore contains no simultaneously Chern–Ricci-flat and Gauduchon metric. Nevertheless it contains omega1=h^(-1)omega, the explicit Vaisman metric on this very same X. This is a conformal-class obstruction, not an existence counterexample to unrestricted P05.\n\nArtifacts: verify.py performs exact Koszul calculations checking nabla theta1=0, (13), q=-h'', Hermitian compatibility, real flat determinant equal to one, and the two exact q values. Rerun python verify.py > verification-output.json. The ordinary proof above does not depend on successful execution.\n\nArtifacts: /workspace/research/native-workers/codex-EkrwhP",
      "support": [
        "n1",
        "n3"
      ]
    },
    {
      "id": "n5",
      "summary": "All limited A–D targets are claimed complete, with ordinary proofs, precise dependency judgments, reproducible symbolic checks, and preserved failed routes. candidate=true refers only to this scoped assignment; unrestricted original P05 remains unresolved.",
      "detailedSummary": "The proofs retain compactness, connectedness, n>=2, the ordinary Bott–Chern normalization, the fixed complex structure, and same-metric contractions. No specialized external theorem is indispensable. An independent public holomorphic-Lee theorem was checked with its exact compact LCK, holomorphic-Lee and same-metric Gauduchon hypotheses, but not used as an unproved premise. Fifteen symbolic checks passed. An attempted pointwise counterexample using D failed because that family itself has pointwise equality; the failure is preserved. Separate conformal gauges, omitted Riemannian curvature, and already-Vaisman volume theorems do not settle unrestricted P05.",
      "text": "Completion claim. Notes n1–n4 provide complete ordinary proofs of all four limited A–D targets, completing the exact scoped reconstruction assignment. The unrestricted original P05 existence question is not solved: original_P05_completed=false. candidate=true refers solely to completion of A–D.\n\nDependency judgments. A uses the definition of ordinary Bott–Chern vanishing, the defining Chern determinant formula, and the harmonic mean-value maximum argument supplied in n1. B uses explicitly derived local Kähler and conformal connection identities, a proved closed-one-form Bochner identity, Stokes on compact X without boundary, and proved unitary-frame wedge algebra. C uses n2 and supplies its own rigidity argument. D uses explicit quotient and holomorphic-coordinate calculations; its same-class obstruction uses n1 and n3. No Gauduchon conformal-existence theorem, Vaisman volume theorem, deformation theorem, undescented finite-cover argument, or surface-classification theorem is indispensable or applied to prove a target.\n\nAn independent public comparison source was checked: Andrei Moroianu, Sergiu Moroianu and Liviu Ornea, “Locally conformally Kähler manifolds with holomorphic Lee field,” Differential Geometry and its Applications 60 (2018), 33–38, Theorem 1(ii): [public preprint](https://arxiv.org/abs/1712.05821) and [primary theorem PDF](https://moroianu.perso.math.cnrs.fr/tex/2018dga.pdf). Its hypotheses are compact LCK, complex dimension at least two, a holomorphic Lee vector, and a Gauduchon metric, equivalently coclosed Lee form, for that same metric. C satisfies these hypotheses only after proving holomorphicity and q=0. The theorem corroborates the implication but is not an unproved premise: n3 proves the needed flat-case rigidity directly. Ordinary c1BC vanishing or unrelated conformal representatives would not supply its hypotheses. No target-author proof or article, private notes, prior report, campaign material, or credentials was used. Search results incidentally surfaced target-topic entries; none was opened or relied upon.\n\nPreserved failed routes:\n1. Ordinary c1BC vanishing does not set q=0 for the flat representative. A supplies flatness, whereas a separately chosen Gauduchon metric may differ. D explicitly separates these properties within one conformal class.\n2. Chern–Ricci flatness is not real Riemannian Ricci flatness. Dropping Ric(A,A) from Bochner is invalid. Equation (3) retains it, and equation (9) accounts for its integral.\n3. B's Stokes argument supplies no pointwise identity. An attempted diagnostic assumed D would disprove pointwise equality at x=1/4; the initial checker stopped with “AssertionError: Expected a nonzero pointwise defect.” The checker was corrected to record the result instead of assuming it. For D's one-variable family, with r=h' and v=h'', its exact generic output is |Tminus|^2=v^2/2, q=-v, |theta|^2=(r^2+1)/h, and |Tminus|^2-q^2/2=0. This family-specific symbolic coincidence neither disproves nor proves a general pointwise statement. The failed diagnostic is preserved in failed-check.txt.\n4. A volume theorem requiring an already Vaisman manifold and Lee/anti-Lee invariance cannot manufacture those missing hypotheses. No such theorem was applied.\n5. D cannot be an unrestricted existence counterexample because omega1 is an explicit Vaisman metric on the same X.\n\nChecks and artifacts. The workspace is /workspace/research/native-workers/codex-EkrwhP. input.json retains the supplied statement-only input. Rerun\n  python verify.py > verification-output.json\nThe successful run reports fifteen PASS checks: J orthogonality; real flat volume determinant; symmetry of T; raised Lee vector; q=-h''; orthogonal T decomposition; both J-type conditions; zero Vaisman covariant derivative; the general Stokes numerator; integrated B cancellation; the C formula; h^2C=1; and both exact q values. The checker permits a,r,v to vanish and assumes only h>0 in its metric parameterization.\n\nThe environment is Python 3.12.14, SymPy 1.14.0, Linux-6.18.44-x86_64-with-glibc2.41. The final symbolic run took about two seconds. These are exact checks of encoded formulas, not exhaustive checks over all metrics or a machine-verified geometric proof.\n\nproof.txt and notes.json contain the assembled proofs and dependencies. verification-output.json records results; public-source-output.json and public-source-requests.json retain public retrieval outputs and exact requests. commands.txt and environment.json record rerun commands and nonsecret environment details. No resource-heavy computation was needed. No operator-provided supervised compute service was discoverable; that would be a missing facility for future heavy work, and no local heavy computation was substituted. The runtime skill's environment_status tool was unavailable; the readable nonsecret local policy snapshot had vpn_configured=false. No credentials were accessed.\n\nThese remain unverified drafts. Execution success checks the encoded algebra but does not establish mathematical correctness by itself. The completion claim rests on the ordinary proofs and their explicit scope.\n\nArtifacts: /workspace/research/native-workers/codex-EkrwhP",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4"
      ]
    }
  ],
  "candidate": true,
  "workspace": "/workspace/research/native-workers/codex-EkrwhP"
}
```


## Exact primary application assessment

These records supply provenance and hypothesis judgments, not mathematical authority; primary statements and ordinary proofs must still be independently checked.

```json
{
  "recorded_at_utc": "2026-10-06T05:35:57.591272+00:00",
  "primary_url": "https://arxiv.org/pdf/2509.18364v2",
  "primary_pdf_sha256": "89589fded9cd8556a74f515d95934654b7fd0c00c630e49e7bdb0e32e1efaa64",
  "current_article_source_sha256": "d1fb3675d8ead5226d5758f46fbf859c73a1461d2d1ea50b2e55537ab332ea32",
  "actually_root_read_text_ranges_this_turn": [
    [
      1,
      160
    ],
    [
      690,
      825
    ]
  ],
  "actually_root_viewed_pdf_pages_this_turn": [
    1,
    12,
    13
  ],
  "all_three_primary_images_actually_viewed": true,
  "application_judgments": [
    "Theorem A is a SAME-METRIC Gauduchon plus flat rigidity statement. The current paper does not remove its Gauduchon antecedent by citing it.",
    "Section4 equations(2)--(4), before the Gauduchon specialization, contain q=d*theta and match the current real Ricci formula with t=0 and the paper J conventions. The new integrated q identity is derived separately using contracted Bianchi and closed-one-form Weitzenbock identities.",
    "The primary following example uses an already Vaisman manifold and an invariant volume theorem. No such volume theorem is needed or imported for the current explicit Gamma backslash G metric construction.",
    "The unrestricted existence conjecture remains separate. Ordinary Bott-Chern flat gauge and Gauduchon gauge cannot be combined without a new same-metric argument."
  ],
  "all_indispensable_applications_independently_reconstructed": false,
  "native_review_pending": true,
  "mathematical_acceptance": false,
  "original_P05_completed": false,
  "published": false
}
```


## Full-report root whole-read and scope assessment

These records supply provenance and hypothesis judgments, not mathematical authority; primary statements and ordinary proofs must still be independently checked.

```json
{
  "recorded_at_utc": "2026-10-06T06:45:14.718881+00:00",
  "complete_result_sha256": "d1a83501c5f558b696cda82aaa8fe9ec75573d9fe5741e082751bfc0466d7b72",
  "verdict": "INCONCLUSIVE",
  "entire_report_and_all_nine_premises_and_all_fifteen_passages_actually_root_read": true,
  "whole_read_output_untruncated": true,
  "invalid_task_to_external_premise_bindings_retained_and_excluded": [
    14
  ],
  "valid_external_quote_indices_for_unaccepted_additional_notes": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13
  ],
  "current_article_A_to_D_report_assessment": "No concrete mathematical defect; all divergence integrals, curvature convention, same-metric holomorphic/Gauduchon/Vaisman equivalences and explicit fixed Kodaira quotient/gauge are independently derived. First erroneous n3 route remains explicitly rejected and unused. Both original existence/counterexample alternatives remain unmet.",
  "unused_deep_external_premises_in_report": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
  ],
  "unused_premise_scope": "All nine schema premises concern retained conditional subclass notes n4/n7. They are preserved for historical audit but are not dependencies of A--D and are not currently independently primary-assessed or accepted as new results. The current article derives its tensor identities directly; its BO crosscheck has a separate actual primary application receipt.",
  "BO_current_exact_application_receipt": "checks/P05-flat-LCK-divergence-exact-primary-root-audit-20261006.pending.json",
  "harmless_clarifications": [
    "Define d^c=i(barpartial-partial)/(4pi) explicitly before use.",
    "The unrelated known Vaisman prescribed-volume theorem uses omega^n=n! times Riemannian volume; retain this conversion if that unaccepted conditional note is ever used."
  ],
  "actual_owner_exit_code": 0,
  "all_calls_settled": true,
  "mathematical_acceptance": false,
  "original_P05_completed": false,
  "published": false
}
```


## Complete independent proof root-read assessment

These records supply provenance and hypothesis judgments, not mathematical authority; primary statements and ordinary proofs must still be independently checked.

```json
{
  "read_completed_at_utc": "2026-10-06T07:02:24.817678+00:00",
  "complete_result_sha256": "ef5f01e42d4dab6ab7ce01ce861236ce389f1503a918ec2c82564f1a91d7cf54",
  "complete_notes": 5,
  "whole_summaries_detailed_summaries_texts_and_supports_actually_root_read": true,
  "actual_untruncated_read_groups": [
    [
      "n1",
      "n2"
    ],
    [
      "n3",
      "n4",
      "n5"
    ]
  ],
  "all_top_level_fields_actually_root_read": true,
  "candidate": true,
  "candidate_refers_only_to_scoped_A_D": true,
  "actual_owner_exit_code": 0,
  "all_calls_settled": true,
  "no_author_proof_or_prior_reports_supplied": true,
  "independent_B_uses_exterior_Stokes_relation_instead_of_author_Bianchi_contraction": true,
  "unused_public_Moroianu2018_comparison_not_imported_as_premise": true,
  "failed_pointwise_D_diagnostic_preserved_without_general_pointwise_claim": true,
  "root_scoped_mathematical_acceptance": false,
  "new_indispensable_external_sources_found": false,
  "original_P05_completed": false,
  "published": false,
  "final_comparison_pending": true
}
```


## Final scope

Only A--D are publication candidates. No unused cover, potential, degeneration, Tsukada-cone or Vaisman-volume theorem is imported into their proofs. The current paper explicitly derives the local conformal Ricci tensor, contracted Bianchi relation and closed-one-form Weitzenbock relation; the independent proof derives the full alternative exterior Stokes identity. BO2509.18364v2 comparison applications were judged using the actual primary text and pages at root. The current single d^c convention clarification changes no hypothesis or mathematical conclusion. Both actual native owners have exited0 and all calls settled. The current local exports are clean and all four pages actually viewed; the native compiler response remains pending, and no compile status is mathematical acceptance. Original P05 remains unresolved. All source imports genuinely used in any target need exact root judgment and valid external quotations.


## Complete scoped final comparison report

PASS applies only to the scoped A–D conclusions and their final comparison. original_P05_completed=false. The unrestricted original-task review remains INCONCLUSIVE: neither a general same-X Vaisman existence proof nor an actual counterexample is supplied. I independently checked the current article, the frozen article, all seven historical exploration notes, the preserved full report, and all five reconstruction notes. Candidate flags, hashes, compilation records and symbolic checks contribute no mathematical authority.

A is correct. In complex dimension n, conformal scaling gives ρ(e^vω)=ρ(ω)−n i∂bar∂v. Thus ρ(ω)/(2π)=dd^cF implies ρ(e^(F/n)ω)=0. Its Lee form is θ+dF/n, so closedness and the nonzero Lee class persist on the same complex manifold. Two flat conformal representatives have a real pluriharmonic logarithmic ratio. Local harmonicity and the maximum principle on connected compact X make that ratio constant. This establishes precisely existence and uniqueness up to positive scale, without establishing Gauduchon in the flat gauge.

The conventions and local curvature calculations are consistent. With d^c=i(bar∂−∂)/(4π) and Jα=−α∘J, one has Jdf=4πd^cf and dJdf=2i∂bar∂f. Locally θ=df and g₀=e^(−f)g is Kähler. The displayed connection difference follows from Koszul; substituting it into D J=0 gives the stated ∇J formula. Differentiating Jθ and alternating gives dJθ(X,JY)=2P(X,Y)−u g(X,Y)+θ(X)θ(Y)+Jθ(X)Jθ(Y).

For completeness, the conformal curvature contraction can be checked directly. For g′=e^(2v)g in real dimension m, the connection difference is C^k_ij=δ^k_i v_j+δ^k_j v_i−g_ij v^k. Its differentiated Ricci terms are −(m−2)Hess v−g Δv, and its quadratic terms are (m−2)(dv⊗dv−|dv|²g). Taking m=2n and v=−f/2 yields the article’s conformal Ricci formula, including the −qg/2 term. Flatness gives ρ(g₀)=(n/2)dJθ, and the Kähler relation Ric₀(X,Y)=ρ(g₀)(X,JY) consequently gives
R=nP−(n−1)T+(q−u)g/2+θ⊗θ/2+nJθ⊗Jθ/2.
Its trace is s=(n−1)q−(n−1)u/2. Chern–Ricci flatness has nowhere been substituted for Riemannian Ricci flatness.

B’s contracted-Bianchi proof is valid in full. Closedness makes T symmetric, and the J-invariant and anti-invariant projections are orthogonal. Write E_A=∫T(A,A), E_B=∫T(JA,JA), and use L² norms for g. Integrating div(uA), with div A=−q and A(u)=2T(A,A), gives ∫uq=2E_A. The contracted Bianchi identity, paired with θ, gives 0=∫⟨R,T⟩+(1/2)∫sq. Substituting the verified curvature and scalar formulas gives
0=n‖P‖²−(n−1)‖T‖²+(n−2)‖q‖²/2+(4−n)E_A/2+nE_B/2.
Commuting covariant derivatives of the closed one-form and integrating gives
‖q‖²=‖T‖²+∫R(A,A).
Here R(A,A)=(1−n/2)T(A,A)+(n/2)T(JA,JA)+qu/2, so
‖q‖²=‖T‖²+(4−n)E_A/2+nE_B/2.
Elimination gives n(‖P‖²−‖T‖²)+n‖q‖²/2=0, hence ∫|T⁻|²=(1/2)∫q². Every integration uses the same metric. No Gauduchon antecedent or sign assumption on ∫uq is inserted.

The independent exterior-Stokes proof of B is also valid. Put η=Jθ and p(U,V)=P(JU,V). The local connection calculation gives dη=2p−uω+θ∧η. The contractions are Λp=−q/2, |p|²=|P|²/2, Λ(θ∧η)=u and ⟨θ∧η,p⟩=P(A,A). The last equality remains valid at zeros of θ; its frame verification does not impose a nowhere-zero Lee form. The unitary-frame identity
α∧β∧ω^(n−2)=[(Λα)(Λβ)−⟨α,β⟩]ω^n/[n(n−1)]
follows by expansion for a diagonal real (1,1)-form and polarization.

Writing β=2p−uω, differentiation of η∧dη∧ω^(n−2) gives the stated positive (n−2)θ∧η∧dη term. Thus Stokes gives ∫[β²+nθ∧η∧β]∧ω^(n−2)=0. The two contraction numerators are respectively
q²+2(n−1)qu+n(n−1)u²−2|P|²
and
−qu−(n−1)u²−2P(A,A).
Adding n times the second cancels u² and yields
∫[2|P|²+2nP(A,A)]=∫[q²+(n−2)qu].
Substitution into the independently derived closed-one-form Bochner relation cancels the remaining qu terms and proves B. For n=2 the term carrying n−2 vanishes, with no exceptional argument required. Both complete derivations therefore establish the same integral identity. Neither establishes a general pointwise equality.

C is correct for the fixed flat metric. The Hodge identity *θ=Jθ∧ω^(n−1)/(n−1)! and the specified d^c convention give
dd^cω^(n−1)=−(n−1)qω^n/(4πn).
Consequently Gauduchon is exactly q=0. If q=0, B forces T=P. Then T(JA,JA)=T(A,A), and ∫uq=2E_A gives E_A=E_B=0. The Bochner relation forces T=0. Equivalently, under P=T and q=0, R(A,A)=T(A,A), whose integral vanishes, giving the same conclusion.

The local connection formula gives ∇_A J=0. If S is obtained by raising an index of T, expansion of the Lie brackets gives (L_AJ)Y=JSY−SJY. Thus A is real holomorphic exactly when T=P. B then forces q=0 and the preceding argument forces parallelness. Conversely T=0 gives both conditions. Strictness excludes the zero parallel Lee form. This proves all four equivalences, including n=2, without combining properties of separate conformal representatives.

D is correct on the fixed compact quotient. The multiplication is associative, its inverse preserves integer coordinates, and Γ is a subgroup. Its left action is free and properly discontinuous: intersections with a compact set first bound the x,y,t translation integers and then the z integer. Reducing those coordinates gives a compact fundamental set. The invariant coframe and all periodic functions descend.

Integrability can be verified directly, independently of an imported integrability theorem. On G set w=x+iy and v=z+i(t−x²/2). These give global complex coordinates for the declared structure because dw=φ¹ and dv=φ²−ixφ¹. For a lattice element (a,b,c,d), the action becomes
w↦w+a+ib,
v↦v−iaw+c+id−ia²/2.
It is holomorphic with complex Jacobian determinant one. Therefore Σ=dw∧dv=φ¹∧φ² descends as a nowhere-zero holomorphic canonical form. This proves exactly ordinary c₁^BC(TX)=0. The resulting elliptic bundle over C/(Z+iZ), with nontrivial central commutator and b₁=3, is the primary Kodaira model; no surface-classification theorem is needed for the metric conclusions.

With a=f′ and C=1−a′>0, η₁=Jθ₁ and the independent J-paired coframe shows that g₁=θ₁²+η₁²+C((e¹)²+(e²)²) is positive Hermitian. The structure equations give dθ₁=0, dη₁=−Ce¹² and dω₁=θ₁∧ω₁. The t-circle has Lee period −1. The g₁-dual of θ₁ is −E₄=−∂t. Translation in t preserves the metric, so this vector is Killing. Closedness makes its covariant derivative symmetric, and Killing makes it skew; hence ∇θ₁=0. This supplies an explicit strict Vaisman metric on this same X.

The volume calculation gives ω₁²/2=Ce¹²³⁴. Moreover θ₁+iη₁=aφ¹+iφ², and the coframe change to dw,dv has determinant one. The Hermitian determinant in holomorphic coordinates is therefore a fixed positive constant times C. Thus ρ(g₁)=−i∂bar∂log C. For h=C^(−1/2), g=hg₁ has constant holomorphic determinant and actual volume dvol_g=e¹²³⁴=dx dy dz dt, proving Chern–Ricci flatness. Its Lee form is θ=−e⁴+d(f+log h), retaining period −1.

Raising this Lee form with that same flat metric gives A=h′E₁+(f′h′−h^(−1))E₄. The dual frame is E₁=∂x, E₂=∂y+x∂z, E₃=∂z, E₄=∂t, and its members have zero divergence for the displayed volume. Consequently q=−h″. Since
h″=(3/4)C^(−5/2)(C′)²−(1/2)C^(−3/2)C″,
the prescribed C gives exactly q(0)=−4√5π²/25 and q(1/2)=4√3π²/9. Thus ω is neither Gauduchon nor Vaisman. By A every flat conformal representative is cω, and its divergence is q/c, so none is Gauduchon. Nevertheless ω₁ belongs to that conformal class and is Vaisman. This is exactly the claimed conformal-class obstruction, not an obstruction to Vaisman existence on X.

The historical failed calculation remains rejected. For this family, putting p=h′ and r=h″ gives u=(p²+1)/h and |T⁻|²=r²/2. Periodic integration gives ∫uq=−∫(p⁴/3+p²)/h²<0. The rejected n3 identity would instead require ∫uq=∫q²>0 when n=2, so it is concretely false. Its rejection does not damage the corrected proof. The reconstruction’s separate attempted pointwise diagnostic also remains a failed diagnostic: this particular family satisfies pointwise equality. That coincidence supplies no general pointwise conclusion.

I opened the primary [BO v2 text](https://arxiv.org/html/2509.18364v2) and its PDF. Section 4 equations (2)–(4) retain d*θ and match the article’s formulas at t=0. The subsequent Bianchi simplification explicitly invokes d*θ=0. Theorem A requires the same metric to be flat and Gauduchon; the article does not use it to remove that antecedent. The unrestricted assertion is separately presented as a conjecture. The article’s general divergence identity is established by its own derivation. The [Moroianu–Moroianu–Ornea primary theorem](https://moroianu.perso.math.cnrs.fr/tex/2018dga.pdf), Theorem 1(ii), likewise requires a holomorphic Lee field and Gauduchon for that metric. It corroborates C only after those conditions are established and is not indispensable.

The preserved historical notes retain their conditional scope. In n4, uniqueness of normalized flat canonical volume and biholomorphic invariance follow from the same compact pluriharmonic-function argument as A. [Tsukada’s Theorem 5.1 and constructive proof](https://www.numdam.org/article/CM_1994__93_1_1_0.pdf) supply the convex positive Lee-class half-space on an already Vaisman manifold. Averaging a class over the finite holomorphic group remains in that half-space. The flat volume is invariant under the selected Vaisman Lee and anti-Lee flows, so the antecedents of [Ornea–Verbitsky Theorem 4.1](https://arxiv.org/html/2206.08808v2) are established. Uniqueness then gives group invariance and genuine descent. Parallelness and flatness descend locally, while exactness downstairs would contradict the nonzero pulled-back Lee class. Normal closure handles the nonregular finite-cover case. P05 supplies no such cover.

Historical n5 correctly requires an invariant complex structure and an invariant representative of the given Lee class. The initial conformal correction is essential. Unimodularity makes invariant-frame coefficient averaging commute with d; constant J coefficients make it commute with type operators and dd^c. Averaging preserves positivity and the invariant-Lee LCK equation. Applying averaging to the ordinary Bott–Chern potential forces the invariant Chern–Ricci form to vanish. The invariant Lee dual has zero divergence, and C then gives Vaisman. None of these antecedents is established for arbitrary P05 data.

Historical n6’s same-Lee perturbation obstruction is also valid. Subtraction gives θ∧dd^cφ=0. The real (1,1) condition forces dd^cφ=aθ∧Jθ. For a nonzero parallel Lee form, u is constant and dJθ=−uω+θ∧Jθ. Closedness, evaluated on A and two horizontal vectors, gives a u²ω(v,w)=0. The horizontal form is nondegenerate for every n≥2, so a=0 and compactness makes φ constant. This excludes only the stated ordinary dd^c ansatz with unchanged Lee form.

Historical n7 retains the additional positive-potential and n≥3 antecedents. [Ornea–Verbitsky Theorems 4.8 and 7.3](https://arxiv.org/html/2112.03363v2) have the required same-complex-manifold approximation and explicit Diff₀ sequence converging to a Vaisman structure. Each approximant is biholomorphic to the original. The normalized Gauduchon factors vary continuously by the simple-kernel elliptic equation, so zero canonical degree passes to the limit without bounds on the Bott–Chern potentials. Nearby almost complex structures have the same topological first Chern class.

The required kernel conclusion is justified by the harmonic description in [Istrati–Otiman Theorem 4.2 and Corollary 5.1](https://arxiv.org/html/2206.07312v2). For n≥3 a Bott–Chern (1,1) harmonic representative is basic harmonic. Averaging a primitive over the compact closure of the Vaisman flows and decomposing it as ζ+aθ+bJθ shows that horizontality forces da=db=0. Basic Hodge orthogonality then identifies the de Rham-exact representative with a multiple of −dJθ. Its positive degree against a Gauduchon metric excludes a nonzero multiple at the limit. Thus ordinary Bott–Chern vanishing is established before applying [Istrati Theorem 5.7](https://arxiv.org/html/2304.02582v1). The [local Kuranishi parametrization](https://www.numdam.org/item/10.24033/asens.2148.pdf), Section 1, then places the close approximants in that deformation neighborhood, and biholomorphic pullback returns a strict Vaisman metric to the original X. This is a conditional potential-subclass argument, not a deduction of potential from P05.

The historical source statements retain their exact restrictions. Istrati Corollary 5.2 starts with a Vaisman Bott–Chern Calabi–Yau manifold. [Gauduchon’s primary proof](https://numdam.org/item/AST_1985__126__129_0.pdf), Theorem 2 and its two kernel lemmas, supplies both one-dimensionality and positivity of the normalized factor. [Tosatti Proposition 1.1](https://arxiv.org/pdf/1401.4797v4) confirms the ordinary unitary-flat canonical interpretation; it does not imply canonical triviality or torsion for arbitrary X.

I checked the preserved quote bindings against their primary contexts. The short excerpts in passages 0–13 require those contexts; passage 11’s generic introductory sentence does not independently establish the Kuranishi conclusion, which is supported by the Meersseman construction. Passage 14 is preserved as supplied: “Vanishing c_1^{BC} supplies a Chern-Ricci-flat conformal representative; the conformal Gauduchon theorem separately supplies a Gauduchon representative.” It is a task quotation and remains excluded as evidence for the stronger external normalized-kernel claim. None of the nine historical deep premises is imported into A–D.

The explicit d^c definition is a harmless clarification and fixes no mathematical defect. The historical prescribed-volume application also requires the harmless conversion V′=n!μ between ω^n and Riemannian volume. No substantial repair of A–D is required. Their proofs are self-contained using routine differential-geometric identities reconstructed above, so premises and passages are empty; the historical supporting notes and corroborating comparisons are not external premises of the accepted scoped argument. No priority certification is made.

## Final standalone source

```tex
\documentclass[11pt]{article}
\usepackage[margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newcommand{\ddc}{dd^c}
\newcommand{\Ric}{\operatorname{Ric}}
\newcommand{\vol}{\operatorname{vol}}
\newcommand{\tr}{\operatorname{tr}}
\title{Divergence, rigidity and conformal gauges\newline for Chern--Ricci-flat LCK metrics}
\author{}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{center}\small Scoped metric and conformal-class results; the general existence question remains open.\end{center}
\begin{abstract}
For a compact Chern--Ricci-flat locally conformally K\"ahler metric,
the squared $L^2$ norm of the anti-$J$-invariant covariant derivative
of its Lee form equals half the squared norm of its divergence.
This gives equivalent Gauduchon, holomorphic-Lee and Vaisman conditions
for that metric. An explicit fixed Kodaira surface has a strictly LCK
flat conformal gauge which is not Gauduchon, and its conformal class
contains no metric satisfying both conditions. The same complex surface
has an explicit Vaisman metric. These are metric and conformal-class
results; the unrestricted existence question for an arbitrary compact
ordinary Bott--Chern Calabi--Yau LCK manifold remains unresolved.
\end{abstract}

\section{Conventions and scope}
Let $(X,J,g,\omega)$ be connected and compact, of complex dimension
$n\geq2$, with $\omega(X,Y)=g(JX,Y)$. We use
\[
 d^c=\frac{i}{4\pi}(\bar\partial-\partial),
 \qquad \ddc=\frac{i}{2\pi}\partial\bar\partial,
 \qquad J\alpha=-\alpha\circ J
\]
for real one-forms. Thus $dJdf=4\pi\ddc f$. A strictly LCK metric has
$d\omega=\vartheta\wedge\omega$ with $d\vartheta=0$ and nonexact
$\vartheta$. It is Vaisman when $\nabla\vartheta=0$. The Chern--Ricci
form is $\rho(g)=-i\partial\bar\partial\log\det(g)$; its normalized
representative $\rho(g)/(2\pi)$ represents ordinary $c_1^{\rm BC}(T_X)$.
All divergences, norms and integrals below use this same $g$.

The same-metric Gauduchon and Chern--Ricci-flat rigidity theorem is
established in \cite[Theorem A]{BO}. We retain the divergence terms
in its connection, Bianchi and Weitzenb\"ock argument. Ordinary
Bott--Chern vanishing alone does not supply a simultaneous gauge.
No theorem for an already Vaisman manifold is applied to a general
LCK manifold, and no deformation or cover replaces the given complex
structure.

\section{The integral identity and its rigidity consequences}
Set
\[
 A=\vartheta^\sharp,\quad B=JA,\quad T=\nabla\vartheta,\quad
 P(X,Y)=\tfrac12\{T(X,Y)+T(JX,JY)\},\quad T^-=T-P,
\]
\[
 q=d_g^*\vartheta=-\tr_gT,\qquad u=|\vartheta|_g^2.
\]
Closedness of $\vartheta$ makes $T$ symmetric; $P$ and $T^-$ are
orthogonal, so $|T|^2=|P|^2+|T^-|^2$.

\begin{theorem}\label{th:rigidity}
For every compact Chern--Ricci-flat strictly LCK metric,
\begin{equation}\label{eq:identity}
 \int_X|T^-|^2\,d\vol_g=\frac12\int_X|q|^2\,d\vol_g.
\end{equation}
For this fixed metric the following conditions are equivalent:
Gauduchon; $q=0$; $A$ is real holomorphic; and Vaisman.
The equality \eqref{eq:identity} is an integral identity, rather than
an asserted pointwise identity for general metrics.
\end{theorem}

\begin{proof}
Locally $\vartheta=df$ and $\widetilde g=e^{-f}g$ is K\"ahler. Its
Levi--Civita connection is
\[
 D_XY=\nabla_XY-\tfrac12\vartheta(X)Y
                 -\tfrac12\vartheta(Y)X+\tfrac12g(X,Y)A.
\]
The equation $DJ=0$ gives
\begin{equation}\label{eq:nablaJ}
 (\nabla_XJ)Y=\tfrac12\{\vartheta(JY)X-\vartheta(Y)JX
                  -g(X,JY)A+g(X,Y)JA\}.
\end{equation}
Differentiating $J\vartheta=-\vartheta\circ J$ and using symmetry of
$T$ consequently gives
\[
 dJ\vartheta(X,JY)=2P(X,Y)-u g(X,Y)
              +\vartheta(X)\vartheta(Y)+J\vartheta(X)J\vartheta(Y).
\]
Flatness and the local conformal volume change give
$\rho(\widetilde g)=n i\partial\bar\partial f=(n/2)dJ\vartheta$.
Contracting the curvature difference of $D$ and $\nabla$ gives the
real conformal Ricci formula
\[
 \Ric_D=\Ric_g+(n-1)T+\tfrac{n-1}{2}\vartheta\otimes\vartheta
                       +\tfrac12\{-q-(n-1)u\}g.
\]
The K\"ahler Ricci form of $\widetilde g$ equals its real Ricci tensor
paired with $J$. Combining these expressions yields
\begin{equation}\label{eq:Ric}
 R:=\Ric_g=nP-(n-1)T+\tfrac{q-u}{2}g
               +\tfrac12\vartheta\otimes\vartheta
               +\tfrac n2J\vartheta\otimes J\vartheta.
\end{equation}
Its trace is
$s=(n-1)q-(n-1)u/2$. The local formulas agree with
\cite[Section 4, equations (2)--(4)]{BO}; no $q=0$ hypothesis has
been inserted into \eqref{eq:Ric}.

Write $\|\cdot\|$ for the $L^2$ norm and put
$E_A=\int_XT(A,A)d\vol_g$, $E_B=\int_XT(B,B)d\vol_g$.
Since $T(A,A)=A(u)/2$ and $\operatorname{div}A=-q$,
\begin{equation}\label{eq:uq}
 \int_Xuq\,d\vol_g=2E_A.
\end{equation}
Pair the contracted Bianchi identity
$\delta R+ds/2=0$ with $\vartheta$ and integrate. Here $\delta$ is
minus covariant contraction, adjoint to symmetric covariant derivative.
It gives $\int\langle R,T\rangle+\frac12\int s q=0$.
Substitution of \eqref{eq:Ric} and \eqref{eq:uq} gives
\begin{equation}\label{eq:Bianchi}
 0=n\|P\|^2-(n-1)\|T\|^2+\tfrac{n-2}{2}\|q\|^2
                    +\tfrac{4-n}{2}E_A+\tfrac n2E_B.
\end{equation}
The integrated Weitzenb\"ock identity for a closed one-form gives
\[
 \|q\|^2=\|T\|^2+\int_XR(A,A)\,d\vol_g.
\]
Equation \eqref{eq:Ric} has
$R(A,A)=(1-n/2)T(A,A)+(n/2)T(B,B)+qu/2$; hence
\begin{equation}\label{eq:Bochner}
 \|q\|^2=\|T\|^2+\tfrac{4-n}{2}E_A+\tfrac n2E_B.
\end{equation}
Eliminating $E_A,E_B$ between \eqref{eq:Bianchi} and
\eqref{eq:Bochner} proves \eqref{eq:identity}.

For the Gauduchon equivalence, the LCK equation and the Hodge identity
$*\vartheta=J\vartheta\wedge\omega^{n-1}/(n-1)!$ give
\[
 d^c\omega^{n-1}=\frac{n-1}{4\pi}
                       J\vartheta\wedge\omega^{n-1},\qquad
 \ddc\omega^{n-1}=-\frac{n-1}{4\pi n}q\,\omega^n.
\]
Thus Gauduchon is exactly $q=0$. In this case \eqref{eq:identity}
forces $T=P$, so $T(B,B)=T(A,A)$. Equation \eqref{eq:uq} gives
$E_A=E_B=0$, and \eqref{eq:Bochner} forces $T=0$.

Equation \eqref{eq:nablaJ} gives $\nabla_AJ=0$. Let $S$ be the
symmetric endomorphism with $g(SX,Y)=T(X,Y)$. Then
\[
 (\mathcal L_AJ)Y=JSY-SJY.
\]
Consequently $A$ is real holomorphic exactly when $T=P$.
Equation \eqref{eq:identity} then gives $q=0$, hence $T=0$.
Conversely $T=0$ gives both other conditions. Under strictness the
parallel Lee form is nonzero, as required for Vaisman.
\end{proof}

\section{An explicit compact example with incompatible gauges}
\begin{proposition}\label{prop:example}
On one fixed compact complex Kodaira surface there is a strictly LCK
Chern--Ricci-flat metric which is not Gauduchon. Its conformal class
contains no simultaneously Gauduchon and Chern--Ricci-flat metric.
The same surface has an explicit Vaisman metric, so this is not a
counterexample to the unrestricted P05 existence question.
\end{proposition}

\begin{proof}
On $G=\mathbb R^4$ use the multiplication
\[
 (x,y,z,t)(x',y',z',t')=(x+x',y+y',z+z'+xy',t+t').
\]
The integer subgroup $\Gamma=\mathbb Z^4$ is a lattice: its left
action is $(x,y,z,t)\mapsto(x+a,y+b,z+c+ay,t+d)$.
Reduction of $x,y,t$ and then $z$ to unit intervals supplies a compact
fundamental set. Thus $X=\Gamma\backslash G$ is connected and compact.
The global forms
\[
 e^1=dx,\quad e^2=dy,\quad e^3=dz-xdy,\quad e^4=dt
\]
have $de^3=-e^{12}$ and the other derivatives zero. Declare
$\phi^1=e^1+i e^2$, $\phi^2=e^3+i e^4$ to be of type $(1,0)$.
Then $d\phi^1=0$ and
$d\phi^2=-(i/2)\phi^1\wedge\overline{\phi^1}$ have no $(0,2)$
part, so the complex structure is integrable.
$\Sigma=\phi^1\wedge\phi^2$ is closed and nowhere vanishing,
hence holomorphic. The canonical bundle is holomorphically trivial,
which proves ordinary $c_1^{\rm BC}(T_X)=0$.

Take a unit-periodic $f(x)$ with $C=1-f''>0$, and set
\[
 \vartheta_1=-e^4+f'e^1,\quad \eta_1=J\vartheta_1=e^3+f'e^2,
 \quad \omega_1=\vartheta_1\wedge\eta_1+C e^{12}.
\]
This is the positive Hermitian form of
$g_1=\vartheta_1^2+\eta_1^2+C\{(e^1)^2+(e^2)^2\}$.
One has $d\vartheta_1=0$, $d\eta_1=-C e^{12}$ and
$d\omega_1=\vartheta_1\wedge\omega_1$.
The $t$-circle has Lee period $-1$, so the metric is strict.
Its Lee dual is $-\partial_t$. All coefficients are independent of
$t$, making this field Killing; closedness of $\vartheta_1$ makes
$\nabla\vartheta_1$ symmetric and Killing makes it skew. Thus $g_1$
is Vaisman on this fixed complex manifold.

Its volume is $\omega_1^2/2=C e^{1234}$, while
$\Sigma\wedge\overline\Sigma$ has constant density in $e^{1234}$.
Put $h=C^{-1/2}$ and $\omega=h\omega_1$. Then
$\omega^2/2=e^{1234}$, so its Chern--Ricci form is zero. Its Lee form
is $\vartheta=-e^4+d(f+\log h)$, retaining period $-1$.
If $E_i$ are dual to $e^i$, its Lee dual is
\[
 A=h'E_1+(f'h'-h^{-1})E_4.
\]
The metric volume is $dx\,dy\,dz\,dt$. Each $E_i$ has zero
divergence in this volume, hence $\operatorname{div}A=h''$ and
$q=d_g^*\vartheta=-h''$.

For the explicit choice
\[
 f(x)=\frac{\cos(2\pi x)}{16\pi^2},\qquad
 C(x)=1+\tfrac14\cos(2\pi x)\geq\tfrac34,
\]
direct differentiation gives
\[
 q(0)=-\frac{4\sqrt5\pi^2}{25},\qquad
 q(1/2)=\frac{4\sqrt3\pi^2}{9}.
\]
Thus $\omega$ is not Gauduchon, and Theorem~\ref{th:rigidity}
also shows it is not Vaisman.

For any global real $v$,
$\rho(e^v\omega)=\rho(\omega)-n i\partial\bar\partial v$.
Two flat metrics in a single conformal class therefore have a real
pluriharmonic logarithmic ratio, constant on a connected compact
complex manifold by the maximum principle. The only flat metrics
conformal to $\omega$ are its positive constant multiples; constant
scaling cannot make its nonzero $q$ vanish. This proves the asserted
obstruction. The already exhibited $\omega_1$ is a Vaisman and
Gauduchon representative in that class, with generally nonzero
Chern--Ricci form.
\end{proof}

\section{The remaining existence question}
If ordinary $c_1^{\rm BC}(T_X)=0$, write
$\rho(\omega)/(2\pi)=\ddc F$ for a global smooth $F$.
Then $e^{F/n}\omega$ is Chern--Ricci flat and its Lee form is
$\vartheta+dF/n$, still nonexact. This proves existence and
uniqueness up to scale of the flat conformal gauge, rather than
existence of a metric with $q=0$ in it. The explicit example
shows why these assertions cannot be combined with the separate
Gauduchon conformal theorem to supply the same-metric rigidity
hypothesis. It supplies no obstruction to all Vaisman metrics on
$X$, and the arbitrary same-complex-manifold existence problem
remains open in this argument.
\begin{thebibliography}{9}
\bibitem{BO} G. Barbaro and A. Otiman,
\emph{Calabi--Yau locally conformally K\"ahler manifolds},
\href{https://arxiv.org/abs/2509.18364v2}{arXiv:2509.18364v2},
Theorem A and Section 4.
\end{thebibliography}
\end{document}
```
