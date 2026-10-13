# Whole current singular radial weighted-envelope proof

This is new unverified material; the prior published radial-density theorem and its verdicts are not mathematical premises. Assess the unchanged full original task, exact answered scope, all primary applications and literature overlap.

## Entire article

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\D}{dd^c}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\Eenv}{\mathcal E_{\mathrm{env}}}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Residual regularity of singular radial weighted envelopes}
\author{}\date{}
\begin{document}\maketitle
\begin{abstract}
We consider an ordinary global obstacle envelope with a sublogarithmic
pole on projective space. A compactly supported radial perturbation of
the singular weight reduces its envelope to a one-dimensional convex
minorant. The residual against the prescribed singular reference is
globally $C^{1,1}$, vanishes near the pole, and is smooth near the
hyperplane at infinity. The envelope retains its ordinary type and its
actual non-pluripolar measure has mass one, with zero density on every
free interval. The formula extends to the full family of competitors on
a product with an arbitrary positive Hermitian factor, including a
nonclosed background on a non-K\"ahler fourfold. The conclusions concern
this declared singular-obstacle operator and its residual.
\end{abstract}
\noindent\textbf{Working draft.} Independent reconstruction and mathematical
review are pending. This article does not claim a complete solution of
the unrestricted original S06 programme.

\section{The singular reference and the precise operator}
Use $\D=i\partial\bar\partial/(2\pi)$ and ordinary wedge powers.
Let $\kappa=\D\log(1+|z|^2)$ be the standard Fubini--Study form on
$\mathbf P^k$, $k\geq2$, with $\int\kappa^k=1$. On its standard affine
chart put
\[
 r=|z|^2,\qquad x=\log r,\qquad p=\frac r{1+r},\qquad
 T=1-\log p,\qquad 0<\alpha<1,
\]
and define
\[
 \psi=1-T^\alpha,\qquad
 A(x)=\log(1+e^x)+\psi(x).
\]
The canonical value of $\psi$ at $z=0$ is $-\infty$.
At infinity, with $R=1/r$, it is
$1-(1+\log(1+R))^\alpha$, a smooth function of the smooth projective
coordinate $R$, with value zero on the hyperplane. Thus it is a genuine
global $\kappa$-psh function, as also follows from the derivative
calculation below. All inequalities involving potentials include their
canonical values. Ordinary order $u\preceq v$ means $u\leq v+C_0$
for a finite constant $C_0$.

Fix $F\in C_c^2(\mathbf R,\mathbf R)$ and pull $F(\log r)$ back to
the punctured chart, extending it by zero at both ends. Define the
ordinary global obstacle envelope
\begin{equation}\label{eq:envelope}
 E_F=\left(\sup\{v\in\PSH(\mathbf P^k,\kappa):
       v\leq\psi+F\text{ everywhere},\ v\preceq\psi\}\right)^*.
\end{equation}
Here the obstacle set is the entire manifold. Since $F$ is bounded,
the order condition is redundant for each competitor; its inclusion
declares the intended ordinary class. This is not an ideal-order
envelope. The weight itself takes the value $-\infty$ at the pole.

\begin{lemma}\label{lem:reference}
$A$ is smooth and strictly convex, $0<A'<1$, and $A''$ is bounded.
Its asymptotic slopes are $0$ and $1$. Moreover,
\[
 \begin{split}
 &A(x)=1-(1-x)^\alpha+o(1)\quad(x\longrightarrow-\infty),\\
 &A(x)-xA'(x)\longrightarrow-\infty\quad(x\longrightarrow-\infty),\\
 &A(x)-x\searrow0,\quad A(x)-xA'(x)\longrightarrow0
       \quad(x\longrightarrow+\infty).
 \end{split}
\]
\end{lemma}
\begin{proof}
Put $a=\alpha T^{\alpha-1}$. Since $p'=p(1-p)$ and $T'=-(1-p)$,
\[
 A'=p+(1-p)a,\qquad
 A''=p(1-p)(1-a)+\alpha(1-\alpha)(1-p)^2T^{\alpha-2}.
\]
Both assertions follow from $T\geq1$ and $0<a\leq\alpha<1$.
The left asymptotics follow from $T=1-x+O(e^x)$; the tangent intercept
has leading term $-(1-\alpha)(-x)^\alpha$.
On the right, $A=x+(1-\alpha)e^{-x}+O(e^{-2x})$ and
$A'=1-(1-\alpha)e^{-x}+O(e^{-2x})$. Finally $A'-1<0$.
\end{proof}

\section{Convex reduction for the full envelope}
Let $g=A+F$ and let $C$ be its largest convex minorant on $\mathbf R$,
defined as the supremum of all affine functions below $g$.
This gives a finite convex function because $A-\|F\|_\infty$ is a
convex minorant and is itself the supremum of its supporting lines.
In particular
\begin{equation}\label{eq:sandwich}
 A-\|F\|_\infty\leq C\leq A+F\leq A+\|F\|_\infty.
\end{equation}

\begin{theorem}\label{th:main}
The exact envelope in \eqref{eq:envelope} is
\[
 E_F(z)=C(\log|z|^2)-\log(1+|z|^2)
\]
off its pole, with canonical extensions at the pole and infinity.
It is ordinarily equivalent to $\psi$. Its residual $E_F-\psi$ has a
canonical extension in $C^{1,1}(\mathbf P^k)$, is identically zero
near the pole, and is smooth near infinity.
If $J=\{C<g\}$, then $C$ is affine on each connected component of $J$,
and, writing $L_2=\sup_{\mathbf R}\max(g'',0)$,
\begin{equation}\label{eq:quantitative}
 0\leq C'(b)-C'(a)\leq L_2(b-a)\qquad(a<b).
\end{equation}
\end{theorem}
\begin{proof}[Proof of the formula and type]
Every supporting slope of $C$ lies in $[0,1]$: a negative slope is
incompatible with $g(x)\to-\infty$ at the left end, and a slope above
one is incompatible with $g(x)=x+o(1)$ at the right end.
The bounds \eqref{eq:sandwich} force the limiting slopes to be $0,1$.

The full competitor family is invariant under $U(k)$ acting in the affine
chart, so its upper-regularized supremum is radial. It is genuine
$\kappa$-psh: local smooth closed potentials give a locally uniformly
upper-bounded psh family, whose upper-regularized supremum is psh.
The competitor $\psi-\|F\|_\infty$ prevents collapse. The obstacle
$\psi+F$ is upper semicontinuous, so regularization preserves the
pointwise upper bound, including the pole.

For completeness, a radial psh total potential has the form $B(\log r)$
with $B$ convex and nondecreasing. Restriction along a complex line gives
convexity in $\log r$: radial subharmonic functions satisfy
$(r\,\partial_r B(\log r))'\geq0$ in distributions.
On the punctured affine space, positivity in a complex direction
orthogonal to $z$ gives $B'\geq0$ for $k\geq2$.
These statements hold for general radial psh functions by invariant
local smoothing on annuli and distributional limits. Conversely, for
smooth convex nondecreasing $B$, the complex Hessian has tangential
eigenvalue $B'/r$ and radial eigenvalue $B''/r$; one-dimensional smooth
convex approximation proves the distributional assertion for finite
convex $B$. The envelope total profile is therefore a convex minorant
of $g$ and is at most $C$.

Conversely $C$ gives a psh total potential on the punctured chart by
this Hessian criterion. Its upper bound at the origin and
\eqref{eq:sandwich} give a canonical removable psh extension with value
$-\infty$. Since $C'\leq1$, $C-x$ is nonincreasing and has a finite
limit at infinity by \eqref{eq:sandwich}. The proposed potential is
locally bounded above there. Adding a local smooth potential of
$\kappa$ and applying removable psh singularities across the
hyperplane proves a genuine extension. Thus it is a global competitor,
and the formula follows. The bounds give ordinary equivalence without
ever subtracting two infinite pole values.
\end{proof}

\begin{proof}[Proof of regularity and the end formulas]
On a compact interval inside $J$ the gap $g-C$ has a positive minimum.
Replacing $C$ on a sufficiently short subinterval by its chord preserves
convex gluing: the chord slope lies between the corresponding endpoint
one-sided derivatives. Continuity makes the increase smaller than the
gap. Unless $C$ is locally affine this gives a larger convex minorant,
a contradiction. Overlapping intervals show that $C$ is affine on
each component of $J$.

At a contact point $y$, domination by the differentiable obstacle gives
$C'_-(y)\geq g'(y)\geq C'_+(y)$; convexity gives the reverse order.
Thus $C$ is differentiable there, and both derivatives equal $g'(y)$.
It is differentiable on free intervals as well. A differentiable convex
function on an open interval has continuous derivative, so $C\in C^1$.
For $a<b$ in distinct free intervals, move $a$ to its right contact
endpoint and $b$ to its left contact endpoint, leaving contact points
fixed. The new points $a',b'$ lie in $[a,b]$ and have the same
derivatives. Any unbounded free component that has no appropriate
endpoint puts both original points in that component, where the
difference is zero. Otherwise
\[
 0\leq C'(b)-C'(a)=g'(b')-g'(a')
       \leq L_2(b'-a')\leq L_2(b-a).
\]
This proves \eqref{eq:quantitative}.

For a tangent $\ell_x(y)=A'(x)y+A(x)-xA'(x)$, Lemma~\ref{lem:reference}
gives $\ell_x\to-\infty$ uniformly on $\operatorname{supp}F$ as
$x\to-\infty$. For all sufficiently negative $x$, this tangent is
below $g$ there, and below $A=g$ outside the support. It is an affine
minorant touching $A$ at $x$, so $C(x)=A(x)$ on a left end interval.
The residual is exactly zero near the pole, and this is its canonical
smooth extension.

Put $L=\inf_{\mathbf R}(g(x)-x)\leq0$. If $L$ is attained at $y$,
the minorant $x+L$ touches $g$ at $y$. The slope bound $C'\leq1$
then forces $C=x+L$ on $[y,\infty)$: indeed
$C(x)\leq C(y)+(x-y)=x+L$ and the reverse inequality holds everywhere.
If $L<0$, it is attained, since $g-x\to+\infty$ on the left and
to zero on the right. The same formula holds if $L=0$ is attained.
The envelope is then
\begin{equation}\label{eq:tail}
 E_F=L-\log(1+R)
\end{equation}
near infinity, a smooth projective function there.

If $L=0$ is not attained, $g(y)-y$ has a positive minimum on
$\operatorname{supp}F$. The tangents $\ell_x(y)$ tend uniformly to
$y$ on that compact set as $x\to+\infty$. For all sufficiently large
$x$ they lie below $g$ there and below $A$ elsewhere. Consequently
$C=A$ on a right end interval. The residual is again zero there.
These alternatives include $F=0$, whose assertion is immediate.

On the remaining finite annulus, $C-A$ is $C^{1,1}$. More explicitly,
$|C-A|\leq\|F\|_\infty$, $|(C-A)'|\leq1$, and
$\|(C-A)''\|_{L^\infty}\leq L_2+\|A''\|_\infty$.
If $x=\log r$ is expressed in any smooth real coordinate chart on that
annulus, then almost everywhere
\[
 |\nabla^2(C-A)(x)|\leq
 (L_2+\|A''\|_\infty)|\nabla x|^2+|\nabla^2x|.
\]
Together with the exact smooth end formulas this gives a global
$C^{1,1}$ bound using $\alpha,F$ and the two end cutoffs just constructed.
No uniform bound on the location of those cutoffs is asserted for
families approaching a change in the infinity alternative.
\end{proof}

\section{Actual measures and stability}
\begin{corollary}\label{cor:mass}
The actual non-pluripolar measure of $E_F$ has mass one. For finite
$a<b$,
\[
 \MA_\kappa(E_F)(\{a<\log r<b\})=C'(b)^k-C'(a)^k.
\]
It gives zero measure to the pole and has zero density on every free
interval. For $F,G\in C_c^2(\mathbf R)$, the canonically extended
residuals satisfy
\[
 \|(E_F-\psi)-(E_G-\psi)\|_{C^0(\mathbf P^k)}
       \leq\|F-G\|_\infty.
\]
\end{corollary}
\begin{proof}
On an annulus the bounded local product is computed from the convex
total profile. For a smooth profile its Euclidean density is
$k!\pi^{-k}(C')^{k-1}C''r^{-k}$; polar integration gives
$k(C')^{k-1}C''\,dx$. Smooth convex approximation and continuity of
the bounded Bedford--Taylor product give the displayed formula.
Continuity of $C'$ excludes boundary atoms. At the pole use the strict
superlevel restrictions of $\max(E_F,-j)$; their increasing union is
the finite locus, and the non-pluripolar product gives no pole mass.
There is no hyperplane mass since the envelope is smooth at infinity.
The asymptotic slopes $0,1$ therefore give total mass one. A free
interval is affine, so its radial eigenvalue and top density are zero.
When its slope is positive the smooth Hessian has rank $k-1$.

For $\delta=\|F-G\|_\infty$, subtracting $\delta$ from any competitor
for $F$ gives a competitor for $G$, and conversely. Taking envelopes
gives the uniform bound on the finite locus. The smooth residual
extensions give the same bound at the pole and infinity. This asserts
$C^0$ stability, not convergence in $C^{1,1}$.
\end{proof}

Choose a smooth nonnegative compactly supported bump $\chi$ with
$\chi(x_0)=1$, and take $F=-M\chi$, where $M>A(x_0)-x_0$.
Then $L<0$, so \eqref{eq:tail} holds on an open right tail.
This gives an actual compact example with a retained sublogarithmic
pole, a globally $C^{1,1}$ residual, and a nonempty zero-density region.
Its regularity follows from the convex obstacle and end formulas,
not from a prescribed determinant vanishing order.

\section{All competitors on a nonclosed product}
Let $(Y,h_0)$ be any connected compact positive Hermitian $m$-fold,
and put $X=\mathbf P^k\times Y$, $H=\kappa+h_0$,
$N=k+m$, and $V_0=\int_Yh_0^m$. Pull $\psi$ and $F$ back to $X$.
Define $E_F^H$ by \eqref{eq:envelope} with the full family of genuine
$H$-psh potentials, the pulled-back obstacle, and ordinary order.

\begin{theorem}\label{th:product}
The full product envelope is the pullback of $E_F$ and
\[
 \MA_H^{\rm ext}(E_F^H)=
       \binom Nk\,\MA_\kappa(E_F)\otimes h_0^m,
 \qquad \int_X\MA_H^{\rm ext}(E_F^H)=\binom Nk V_0.
\]
Its residual is globally $C^{1,1}$ and it belongs to the exact
stretching class $\Eenv(X,H,\psi)$.
\end{theorem}
\begin{proof}
Every genuine $H$-psh competitor restricts on a projective slice to a
genuine $\kappa$-psh function or to $-\infty$ identically. The exact
lower Hessian in this assertion can be verified locally even when
$H$ is nonclosed. Choose a smooth quadratic correction $\rho$ with
$\D\rho\geq H$ on a coordinate polydisk. For a standard nonnegative
radial convolution kernel set
$v_\epsilon=(v+\rho)*\eta_\epsilon-\rho$ on a smaller polydisk.
The psh convolutions decrease to the canonical $v+\rho$ and
\[
 \D v_\epsilon\geq(\D\rho-H)*\eta_\epsilon-\D\rho
       \geq-H-o(1)\omega_{\rm Eucl},
\]
uniformly in the background error. Restrict this smooth inequality
to each slice. On each fixed slice the restricted psh convolutions
decrease either to $-\infty$ identically or to a psh function locally
in $L^1$; in the latter case the error tends to zero distributionally.
Subtracting $\rho$ preserves the canonical values and gives the exact
$\kappa$ lower bound. These local restrictions patch. A global slice
is consequently genuine or identically $-\infty$.

The everywhere obstacle constraint makes every nontrivial slice a
competitor for $E_F$. Thus $v\leq\operatorname{pr}_1^*E_F$ pointwise,
and upper regularization preserves this inequality since the right
side is upper semicontinuous. Conversely every base competitor lifts
because $h_0\geq0$, giving equality. No transitive group on $Y$ and
no restriction to separated competitors is used.

For bounded finite-level truncations of the pulled-back potential,
multilinearity of the locally corrected products gives only the term
with $k$ projective and $m$ factor entries. Restrict to strict
superlevel sets and let the level tend to infinity; this is the
actual non-pluripolar construction, so the same binomial identity
holds. It gives the finite mass stated. The residual bounds and
extensions pull back as well. If $K_0=\|F\|_\infty$, then
$E_F^H\geq\psi-K_0$. For each $t\geq1$, the genuine potential
$a_t=\psi-tK_0$ satisfies
$t^{-1}a_t+(1-t^{-1})\psi=\psi-K_0\leq E_F^H$.
This proves the exact stretching definition, together with ordinary
order. The reference is genuine; no model-envelope identification
or unbounded-product continuity theorem has been substituted.
\end{proof}

For a concrete nonclosed example let
$Y=(\mathbf C^2\setminus\{0\})/\langle\zeta\mapsto e\zeta\rangle$.
With $s=\log|\zeta|^2$ and $d^c=i(\bar\partial-\partial)/(4\pi)$, put
$h_0=\D s+ds\wedge d^cs$. Both terms are scaling-invariant and descend.
The first is positive on complex tangential directions and the
second on the radial direction, so $h_0>0$.
Moreover $dh_0=-ds\wedge\D s\ne0$.
The factor is diffeomorphic to $S^3\times S^1$, with first Betti
number one, so is not K\"ahler. The product with $\mathbf P^2$ is a
compact non-K\"ahler fourfold, and $dH\ne0$. No zero-lower-mass
property of this factor is needed or asserted here.

\section{Literature and the answered scope}
Ahn's \cite[Theorem 1.4(ii)]{AhnC} proves continuity of weighted
extremals for finite continuous weights on compact Hermitian manifolds
when the unweighted extremal is continuous. His
\cite[Theorem 1.1(ii)]{AhnH} gives H\"older regularity with a uniform
density in capacity. Those theorems use weights valued in $\mathbf R$;
the weight here has a genuine $-\infty$ pole. The obstacle set here
is the entire manifold and has full capacity density. Thus this
construction does not exhibit a failure of that density assumption.
Its conclusions concern a singular unbounded weight, retained
ordinary type, and regularity of the pole-subtracted residual. The
envelope itself retains its pole and is not a globally H\"older
function. No literature-priority assertion is made.

The foundational psh envelopes and removable extensions used above
are the local statements in \cite[Chapter I, Sections 4--5]{Dem}.
All product calculations use bounded local products as in
\cite[Section 2]{BT}; smooth-background corrections and positivity
at bounded levels can be justified as in
\cite[Section 2.1, Proposition 2.1]{BGL}. The nonclosed unbounded
calculation is obtained from finite-level strict-superlevel
restrictions, not from a global theorem requiring BMP.

This gives a specific radial singular-obstacle regularity and
stability criterion with actual free-region density zeros, its
canonical extension across a nonlogarithmic pole, and an all-competitor
nonclosed product identity. Arbitrary prescribed types, general
compact obstacle sets and ideal weighted envelopes remain outside
the theorem. The ordinary model of the selecting potential is not
assumed to preserve its sublogarithmic pole.

\begin{thebibliography}{9}
\bibitem{AhnC} H. Ahn, \emph{Characterization of continuity of
Siciak--Zaharjuta extremal functions on compact Hermitian manifolds},
arXiv:2604.01885v3 (2026).
\bibitem{AhnH} H. Ahn, \emph{H\"older regularity of Siciak--Zaharjuta
extremal functions on compact Hermitian manifolds},
arXiv:2604.01887v3 (2026).
\bibitem{Dem} J.-P. Demailly, \emph{Complex Analytic and Differential
Geometry}, Chapter I.
\bibitem{BT} E. Bedford and B. A. Taylor, \emph{A new capacity for
plurisubharmonic functions}, Acta Math. 149 (1982), 1--40.
\bibitem{BGL} S. Boucksom, V. Guedj and C. H. Lu,
\emph{Volumes of Bott--Chern classes}, arXiv:2406.01090.
\end{thebibliography}
\end{document}


## Entire private proof proposal, not an accepted dependency

# Singular radial weighted envelopes: a new private proof proposal

This is new mathematical material. It is not an accepted result, is not supplied
to the running S12 worker, and does not alter the published S06 radial-density
paper or its original INCONCLUSIVE report. An independent statement-only
reconstruction, full original-task assessment, current primary applications and
final comparison are still required. No original S06 completion is asserted.

## Exact proposed operator and geometric hypotheses

Fix k>=2 and 0<alpha<1 on P^k with normalized Fubini--Study kappa and the
task convention D=i partial-barpartial/(2pi). In the standard affine chart
write r=|z|^2, x=log r, P=r/(1+r), T=1-log P, and

    psi=1-T^alpha,
    A(x)=log(1+exp x)+psi(x).

Thus psi has its canonical value minus infinity at the affine origin, is smooth
on the complement, and is smooth with value0 on the infinity hyperplane.
Its radial total potential A is strictly convex, 0<A'<1, A''>0. The earlier
S06 radial calculation gives these inequalities directly. In particular
A'(x)->0 as x->-infinity and A'(x)->1 as x->+infinity;
A(x)-x decreases to0 at +infinity and tends to+infinity at -infinity.
Its left asymptotics are A(x)=1-(1-x)^alpha+o(1),
A'(x)=alpha(1-x)^(alpha-1)+o(1), and
A(x)-x A'(x)->-infinity. Its right asymptotic tangent intercept
A(x)-x A'(x) tends to0. A'' is bounded on R.

Let F(x) be a real C^2 function with compact support in a finite x interval.
It defines a globally smooth radial perturbation if F is C-infinity; C^2
suffices for the proposed C^{1,1} conclusion. Set g=A+F. Declare the actual
ordinary global-obstacle operator

    E_F=(sup{v in PSH(P^k,kappa):v<=psi+F everywhere,
             v preceq psi})^*.

The order condition is redundant at the competitor level because F is bounded,
but declaring it records the precise prescribed ordinary class. This is a
weighted envelope with K=P^k and a canonical SINGULAR weight psi+F, not a
weighted extremal with a finite Hölder weight, not an ideal-order envelope,
and not an assumption that its envelope is already ordinarily equivalent.
Ordinary-type retention is a conclusion to prove. No arbitrary smooth-obstacle
invariance or ideal-versus-ordinary equivalence is claimed.

## Convex formula

Propose that

    C=g** = the largest convex minorant of g on R,
    E_F(x)=C(x)-log(1+exp x).

The elementary convex construction can be defined as the supremum of affine
minorants, with usc/convex representative. It is finite: A-||F||_infinity is
a convex minorant and g is finite. Hence

    A-||F||_infinity <= C <= A+||F||_infinity.

Any finite convex minorant dominated by g has all slopes in [0,1]. A negative
supporting slope contradicts g(x)->-infinity as x->-infinity. A supporting
slope>1 contradicts g(x)=x+o(1) at +infinity. The bounds just given force its
asymptotic slopes to be0 and1. (Constant affine minorants do not exist, since
g tends to minus infinity at the left end; no positive lower derivative is
being imposed as an extra premise.) These statements also follow directly
from secant slopes and convexity, without invoking an unproved biconjugation
identity for an improper function.

The envelope family is invariant under the U(k) action fixing the affine
origin and infinity hyperplane, so its full usc envelope is radial; symmetry
does not restrict its competitor set. Nonclosed envelope genuineness is not
needed in this closed factor: local common corrections, finite maxima, countable
selection and increasing L1 convergence provide a genuine kappa-psh envelope.
The competitor psi-||F|| supplies its lower bound and prevents the trivial
minus-infinity function. The usc weight psi+F preserves the upper bound.

For a radial kappa-psh function, its total profile log(1+exp x)+v(x) is convex
and nondecreasing. This follows by restriction to complex radial lines and
the tangential/radial complex Hessian calculation, first for smooth radial
profiles and then by local radial convolution and distributional limits.
For the envelope, its bounded difference from psi gives asymptotic slopes0,1
and its profile is a convex minorant of g, hence is <=C.

Conversely C produces a genuine radial kappa-psh potential on the punctured
affine chart: its Hessian has tangential coefficient C'/r and radial coefficient
C''/r in the distributional bounded local approximation sense, both nonnegative.
At the origin it is locally bounded above and tends to minus infinity, so the
canonical psh extension has the intended value. The bounds by A +/- ||F|| make
it ordinarily equivalent to psi. At infinity, C-x is nonincreasing with a finite
limit (again by the same bounds); the invariant potential has that finite
canonical limit on the hyperplane. Local closed-background removability proves
positivity there. It is therefore a genuine admissible global competitor.
This proves the formula, provided the radial distributional characterization
and removal applications are checked in full at current primary sources.

## Contact, end regions and regularity: a self-contained route

Write J={C<g}, an open subset of R. On each connected component of J, C is
affine. To prove local affineness, take a sufficiently small interval with
closure in J and a positive lower gap g-C. The chord of C raises C, preserves
convex gluing (endpoint derivatives bracket the chord slope), and stays below
g for a sufficiently short interval by continuity. If C is not affine there,
this gives a strictly larger convex minorant, a contradiction. Overlapping
intervals then give one affine function on each connected free interval.

At a contact point y, C(y)=g(y) and C<=g imply
C'_-(y)>=g'(y) and C'_+(y)<=g'(y). Convexity implies the reverse order of
the one-sided derivatives, so both equal g'(y). Thus C is C^1 on R: its
derivative is constant in free intervals and cannot jump at a contact point.
This also excludes an unassessed singular derivative measure at free boundaries.

For a<b, if they belong to the same free interval their derivatives are equal.
Otherwise move a forward to the right contact endpoint of its free interval
and b backward to the left contact endpoint of its free interval. When an
endpoint is already a contact point, leave it in place. The moved endpoints
a',b' lie in [a,b], derivatives have not changed, and

    0<=C'(b)-C'(a)=g'(b')-g'(a')
       <=sup_[a,b] max(g'',0) * (b'-a')
       <=sup_[a,b] max(g'',0) * (b-a).

An unbounded free interval can only put both endpoints in that interval in
the cases at issue. Hence this argument proves a local/global Lipschitz bound
for C' and C in C^{1,1}(R). On any annulus in the affine chart, the nonlinear
coordinate change x=log|z|^2 has bounded smooth derivatives, so the residual
E_F-psi=C-A is C^{1,1} there with quantitative bounds from F, alpha and the
annulus. This estimate comes from the obstacle geometry, not density smoothness.

There is actual equality C=A on a left end interval. A tangent at x is
L_x(y)=A'(x)y+A(x)-xA'(x). As x tends to minus infinity, this tends uniformly
to minus infinity on the compact support of F. Thus for all sufficiently
negative x it lies below A+F on that support, and it is <=A elsewhere by
convexity. This tangent is a global affine minorant of g, so C(x)=A(x).
Consequently the residual is identically0 on a neighborhood of the canonical
pole and extends smoothly there. No subtraction of two minus infinities is
used: define the residual from C-A off the pole and extend this actual zero.

The infinity end is also smooth. Let L=inf_R(g(x)-x); always L<=0, because
g-x tends to0 at +infinity. If L is attained at y (which happens whenever
L<0, and may happen when L=0), the line x+L is an affine minorant touching
g at y. Convexity and the slope bound<=1 imply C(x)=x+L for every x>=y.
Then E_F=L-log(1+exp(-x)), a smooth function in projective infinity charts;
its residual against psi is smooth there as well.

If L=0 is not attained, g(y)-y is strictly positive on the compact support
of F, hence has a positive minimum there. Tangents to A at x tend uniformly
to the line y on that compact set as x tends to +infinity, since A'(x)->1
and A-xA'->0. For all sufficiently large x these tangents are below g on
the support, and below A elsewhere. Again C(x)=A(x), so the residual is0
near infinity. These two alternatives cover every perturbation F.

Combining the finite annulus estimate with the actual smooth end formulas
proposes a global C^{1,1} residual E_F-psi across the pole and hyperplane.
No global Hölder regularity is asserted for E_F itself; it retains its pole.
It is smooth off the contact/free-boundary set wherever C either equals a
smooth g or is affine. At arbitrary free boundaries C^{1,1}, not C^2, is the
asserted conclusion; a smooth obstacle need not have a smooth convex minorant.

## Actual measures, zero-density regions and weighted stability

Since C is C^1 and C' locally Lipschitz, there are no radial derivative atoms.
Bounded radial local products, smooth approximation and the radial integration
formula give the actual non-pluripolar radial mass

    MA_kappa(E_F)({a<x<b})=C'(b)^k-C'(a)^k.

Endpoints can be handled by continuity of C'; near the pole use strict
superlevel truncations, not an unproved global unbounded-product theorem.
Taking endpoints to -infinity,+infinity gives finite mass1 and no pole mass.
On free intervals C'=constant, so the full top-degree density vanishes there.
In an annular free interval with positive slope, the smooth Hessian has rank
k-1; zero density here is an actual computed envelope feature.

A concrete nontrivial perturbation is F=-M chi, where chi is a fixed smooth
compactly supported nonnegative bump with chi(x0)=1, and
M>A(x0)-x0. Then L<0, attained on the support, and E_F has the affine
right-end formula above. It has a nonempty open zero-density tail while its
residual is smooth at infinity and retains the sublogarithmic pole at0.
The construction is not a determinant-vanishing-order regularity inference.

For F,G, adding/subtracting delta=||F-G||_infinity to competitors yields
|E_F-E_G|<=delta on their finite locus; the pole-subtracted residuals satisfy
the same global uniform bound after their canonical extension. This proves
type-preserving weighted C^0 stability for this precise operator. It supplies
no C^{1,1} convergence from C^0 convergence alone.

## A genuinely nonclosed product extension, still to be reviewed

Let (Y,h0) be any connected compact Hermitian m-fold, h0 positive, and take
H=kappa+h0 on P^k times Y. Use reference psi pulled back from P^k and weight
psi+F, also pulled back. Define the same full ordinary global-obstacle envelope
over ALL genuine H-psh competitors. Propose the exact identity

    E^H_F=projection^* E^kappa_F.

Restricting a competitor to the projective slices gives kappa-psh functions
or the identically-minus-infinity function. Exact background restriction must
be justified by local psh convolution plus the common smooth correction:
the approximants have H+Du_j>=-epsilon_j h_Euclidean, and their restrictions
decrease to the canonical slice representative, so the exact slice lower
bound survives. One can alternatively use smooth-volume almost-everywhere
slices and then canonical order recovery; no exceptional obstacle set occurs
here because the full obstacle constraint is everywhere. Thus each genuine
slice is <=E^kappa_F. A canonical upgrade yields the product upper bound,
and each base competitor lifts because h0>=0. Envelope regularization commutes
with pullback off the pole; the actual bounded residual and smooth end formulas
settle canonical values on it. This must not assume invariance under a group
on Y or replace the full competitor family by separated competitors.

With N=k+m and V0=int_Y h0^m, bounded finite-level binomial expansion followed
by non-pluripolar restriction gives the actual finite product equation

    MA_H(E^H_F)=binomial(N,k) MA_kappa(E_F) tensor h0^m,
    total mass=binomial(N,k) V0.

The envelope stays ordinarily equivalent to the pulled-back psi. Its bounded
residual gives the exact all-t stretching class relative to genuine psi by
a_t=psi-tK. This reference is not assumed to be an ordinary model: in fact
the sublogarithmic reference has trivial multiplier ideals and its model
envelope can erase the pole. No ideal model or ideal type determines this
ordinary weighted operator.

A concrete nonclosed non-Kähler example can use the standard Hopf surface
Y=(C^2 minus0)/<z->e z> with h0=D log|z|^2+ds wedge d^c s. H is then an
actual nonclosed Hermitian form on the compact fourfold P^2 times Y.
If a zero-lower-mass factor is added as an optional implication, its existence
must be reconstructed in full; do not import the accepted P07 factor flag.
No such optional factor claim is needed for this proposed theorem.

## Literature and acceptance boundary

The 2026 Ahn papers arXiv2604.01887 and2604.01885 already treat Hölder/continuous
weighted extremals under their finite-weight hypotheses, and the 2024 Nguyen
closed-background paper treats ordinary continuous weighted extremals. Their
exact hypotheses must be downloaded and read before saying this theorem lies
outside them. Here the weight itself has a nonlogarithmic pole and the desired
conclusion is C^{1,1} of a pole-subtracted residual, so those finite Hölder-weight
statements cannot simply be applied. Merely failure of a capacity hypothesis
or continuity alone is not the new result proposed here. The precise full
singular-obstacle operator, convex/free-boundary criterion, type retention,
smooth extensions at both ends, actual zero-density regions and nonclosed
all-competitor product identity must be independently checked. No novelty
priority is certified and the unrestricted weighted programme stays unresolved.

The set K=P^k (or the whole product) has full capacity density. This proposal
does not exhibit failure of that density condition: its distinction from the
quoted Ahn regime is the singular, unbounded weight and retained nonlogarithmic
ordinary type, together with quantified residual rather than whole-potential
regularity. Whether this satisfies every intended weighted part of original
S06 is to be assessed explicitly, not presumed from a source-hypothesis failure.


## Entire current primary applications

{
  "recorded_at_utc": "2026-10-07T16:09:18.192302+00:00",
  "source_sha256": "5f72f21a6162d4d603ff8ae287a0c126231d563ebfe79f95745af3ded3213fad",
  "whole_current_article_actually_root_read": true,
  "sources": [
    {
      "name": "Ahn-continuity-weighted-extremals-2604.01885v3",
      "pdf_sha256": "c6c5ae5b071c7ac21d1ab1d9eab97345f32c921b17425e8c99e6a4fad2e90ec8",
      "txt_sha256": "988af2726ee4f2823abfd206de9337e8833c66423fec3cf63769e997a948ae5b",
      "actual_current_text_read_ranges": [
        [
          1,
          155
        ],
        [
          415,
          510
        ]
      ]
    },
    {
      "name": "Ahn-Holder-weighted-extremals-2604.01887v3",
      "pdf_sha256": "59134127d7fb6c6dd7544db35dec7026207e8a4baaccbcc6e4c16d788a07d831",
      "txt_sha256": "ace2ffba8a7bc425c30b0217d9c21bbde6b4ca6583a5e135d69d1119adc626a6",
      "actual_current_text_read_ranges": [
        [
          1,
          170
        ],
        [
          945,
          995
        ]
      ]
    },
    {
      "name": "Demailly-agbook-Harvard",
      "pdf_sha256": "d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1",
      "txt_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
      "actual_current_text_read_ranges": [
        [
          1810,
          1935
        ],
        [
          1988,
          2079
        ],
        [
          2315,
          2395
        ]
      ]
    },
    {
      "name": "Bedford-Taylor-new-capacity",
      "pdf_sha256": "e75ea91e48c14a9838a800aee25b68ed04169c4372f2ce4b399967b53005b758",
      "txt_sha256": "d32eb9305e1cfbcc569746d51d53e417508b33aba0e3b5a1a706036cb0593115",
      "actual_current_text_read_ranges": [
        [
          50,
          310
        ]
      ]
    },
    {
      "name": "BGL-volumes-2406.01090",
      "pdf_sha256": "d7637564a1b1b728743bc5ae315c336097139d12ebca9f43469d721947f8f031",
      "txt_sha256": "aae1614a02599db630e74120e35c5dcd90a7c12782ef366d6f25021e672ee1e1",
      "actual_current_text_read_ranges": [
        [
          493,
          650
        ]
      ]
    }
  ],
  "applications": {
    "Ahn": "Actual finite real weight definitions and exact statements read; complete printed Theorem1.1(ii) Holder proof and Theorem1.4(ii) continuity proof, together with its part(i) printed proof, read. Literature overlap only, not an indispensable mathematical premise. The singular weight psi+F is not finite continuous/Holder on X, so these specific finite-weight conclusions cannot be applied to it. K=X has full capacity density; do not claim an example failing the capacity hypothesis or priority. Source dd^c=2i partial barpartial is4pi times the article convention; no mathematical result imported under incompatible background normalization. No recursive certification of their citations or other theorem proofs is asserted.",
    "Demailly": "On closed projective factor, local smooth exact potentials of kappa produce genuinely psh competitor families locally uniformly bounded above by the usc obstacle. I5.7/5.8 give upper-regularized envelope and canonical representatives; nontrivial psi-M lower bound avoids collapse. I5.23/5.24 apply across origin and infinity hyperplane to local psh functions bounded above; canonical limits are explicitly calculated. Local restrictions in product use convolution of v+rho genuinely psh, decreasing canonical limits and exact smooth background error tending0; no claim to restrict an arbitrary current without this canonical proof. Exact current convention is D=i partial barpartial/(2pi).",
    "Bedford_Taylor": "Every annulus has finite bounded radial total profile. Smooth convex approximation can be taken decreasing: an even positive 1D mollifier of a convex function increases with its scale, so scales decreasing0 give decreasing convex nondecreasing profiles. Entire printed bounded Theorem2.1 and Cor2.2 read; use bounded decreasing products only, radial smooth density then limit with continuous C prime. Global arbitrary unbounded decreasing mass continuity is excluded; pole removal uses exact finite-level strict-superlevel non-pluripolar definition.",
    "BGL": "Entire actual Section2.1 Proposition2.1 proof read; only smooth nonclosed positive backgrounds, bounded potentials, local closed dominating corrections and multilinear product expansion at finite levels. Extend to the pulled-back unbounded potential only by task-granted actual strict-superlevel construction. No Section2.2 BMP-dependent global result or factor zero-lower-mass premise used."
  },
  "all_exact_application_judgments_actually_root_assessed": true,
  "mathematical_acceptance": false,
  "published": false
}


## Complete new supplementary proof of the same G target, unverified

# S06 exact canonical slicing on the nonclosed product

Private unverified supplementary proof of the SAME proposed assertion G.
This introduces no new target, source alteration, accepted result or original
closure. The original weighted article, proof and previous preparation remain
frozen. No native owner has yet received this supplementary argument.

Use D=i partial-barpartial/(2pi), B=P^k with its standard closed FS form
kappa, any connected compact positive Hermitian manifold (Y,h0), and
H=pr_B^*kappa+pr_Y^*h0. Let v be a genuine H-psh potential. Fix coordinate
charts U in B and W in Y, with local smooth exact potential rho for kappa
on U. On a relatively compact smaller chart W choose a smooth quadratic
q(y)=C|y|^2 with Dq>=h0. Such a C exists from the smooth local coefficient
bound and positivity of the Euclidean Hermitian form in this operator.

As an actual distribution on U times W,

    D(v+rho(z)+q(y))=(Dv+H)+(Dq-h0)>=0.

The sum is its genuine psh representative: v is canonical quasi-psh and
adding the smooth correction preserves that representative; the distributional
psh characterization gives the same function, not an arbitrary almost-everywhere
substitute. For EACH y0, its restriction along z -> (z,y0) is genuinely psh
or identically minus infinity. Subtracting the scalar q(y0) and rho(z) shows
that v_y0 is canonically kappa-psh on the base chart, with the EXACT bound

    kappa+D_z v_y0>=0.

The psh pullback statement retains the actual point values, including poles.
Compatible local restrictions glue to a genuine global kappa-psh potential
on B or the identically-minus-infinity function. Connectedness supplies this
alternative: a finite point on one chart excludes an identically-minus-infinity
open restriction elsewhere by propagation through overlapping charts.

Now impose the declared global weighted competitor conditions
v<=pr_B^*(psi+F) EVERYWHERE and v preceq pr_B^*psi. For every y0 the slice
is at most the base envelope E_F if it is not identically minus infinity;
the latter case gives the same pointwise upper inequality. The order condition
also holds on every slice with the original global constant; independently,
the finite bound F makes it redundant for these competitors. Therefore

    v(z,y)<=E_F(z) for EVERY (z,y), with canonical pole values.

The already proposed base convex-minorant proof establishes that E_F itself
is a genuine admissible base competitor. Its pullback is a genuine H-psh
competitor: D E_F+kappa is nonnegative on the base and adding h0 preserves
positivity on the product. It satisfies the everywhere obstacle and the
ordinary-order condition. Thus the raw full product supremum is exactly
pr_B^*E_F. This is already usc and canonical, so its regularization is the
same function. No symmetry or group action on Y, selected-competitor ansatz,
generic slicing, ambient current restriction, or error in a lower Hessian
bound has been used.

Exact primary application: Demailly, Harvard-hosted June 2012 Complex
Analytic and Differential Geometry, Chapter I (5.8), printed40, and (5.11),
printed40--41. The complete printed distributional characterization and
holomorphic pullback proofs were actually read in source-text1988--2118
on 7 October 2026. The former applies to the locally integrable distribution
with all positive complex-Hessian contractions; the latter applies to the
genuine psh representative and the actual holomorphic slice inclusion, with
the identically-minus-infinity possibility retained. The correction uses
closedness only for kappa. h0 is not replaced by a closed background.
The source operator scales by a positive constant and gives the same psh
cone. No extended-product or volume theorem is imported into this slicing
argument; the finite-level product calculation remains a separate assertion.

The base convex formula and the rest of A--H remain unverified candidates.
Independent reconstruction must still prove all of them, including the
entire singular-obstacle envelope and actual measure. This proof does not
establish unrestricted original S06 regularity or ideal-weighted extremals.
