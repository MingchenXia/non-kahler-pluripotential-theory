# Complete new limited S06 A--I final-comparison argument

The prefrozen base below is preserved VERBATIM, with every whole author proof,
earlier original-task report, independent A--H proof, exact printed primary
passage and current known-overlap text. Its former pending-I remarks are
HISTORICAL preparation status. This current document supplies the ENTIRE
completed independent I result after that base, so the earlier warning against
using the base alone is satisfied. Review all current A--I claims and every
actual mathematical dependency. Historical read flags and verdicts are not
mathematical premises. No original unrestricted completion is being asserted.

The earlier A--H result uses local IDs n1--n8. In the later separate I
reconstruction these same eight whole proofs were imported with exact IDs
supplied:n1--supplied:n8, with their internal support edges consistently
renamed. The new I result has its own local IDs n1--n6. They form separate
chains; identical local numbers in different full results are NOT an ID
collision. All imported mathematical bodies were unchanged. The failed
preliminary I campaign produced no public result because its support ID was
unrecognized; it supplies no mathematical premise and is not republished as a
proof. No private worker reasoning or unsubmitted artifact was inspected.

Both cold results keep candidate=false for unrestricted S06, and the original
A--H full assessment remains INCONCLUSIVE. The declared final comparison is
limited to the precise A--I sufficient-condition theorem. The new independent
I reconstruction supplies explicit projective constants and a proved changing
contact-family example in addition to the requested derivative estimates.
The article does not acquire a new sharpness theorem from the unrelated private
sharpness proposal, which remains excluded. Execution/compile success does
not establish mathematical correctness. Exact indispensable primary applications
and the entire source hypotheses must be assessed again for the present claims.

## Verbatim prefrozen complete base

# Unverified complete S06 A--I comparison material, awaiting the separate I result

This prepared base is evidence for a later explicitly limited final comparison;
it is not an accepted theorem or a completed review. The new I independent
reconstruction is still running. The final review must receive its ENTIRE
settled public result in addition to this base. Do not run a final comparison
using this base alone. The historical original-task INCONCLUSIVE and A--H
candidate=false are preserved exactly. No original unrestricted completion,
priority, BMP assertion or equality of representative mass and type volumes
is conferred by these records. Flags and verdicts are provenance, not proofs.

Historical no-author-proof remarks describe only the earlier cold requests.
The current final comparison includes the author's complete proofs explicitly.
The later article replaces the old residual projective-form wording by function
and treats t=1 separately. Those clarifications do not remove historical views.
Target I is substantive new material, requiring independent assessment.
The optional derivative-exponent sharpness proposal is EXCLUDED from this
comparison and the current article. Retrieved printed source passages below
are supplied with exact edition/hash bindings and their limited uses.


## Entire component: papers/S06-singular-radial-weighted-envelope-residuals.tex

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
free interval. Fixed-support bounded obstacle families have a uniform
$C^{1,1}$ residual bound and quantitative $C^{1,\gamma}$ stability for
$0<\gamma<1$, even when the infinity contact moves. The formula extends to the full family of competitors on
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
$1-(1+\log(1+R))^\alpha$, a smooth expression in $R$.
Here $R$ is a smooth projective function near the hyperplane, and the
expression has value zero there. Thus $\psi$ is a genuine global
$\kappa$-psh function, as also follows from the derivative
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

\section{Uniform families and derivative stability}
Fix a finite interval $[a,b]$, $M>0$, and the parameters $k,\alpha$.
Write $\mathcal F_{a,b,M}$ for the real $C^2$ obstacles supported in
$[a,b]$ with $\|F\|_\infty+\|F''\|_\infty\le M$, and let
$R_F$ denote the canonically extended residual $E_F-\psi$.
Norms below are taken in one fixed finite smooth projective atlas.

\begin{theorem}\label{th:uniform}
There is $K=K(k,\alpha,a,b,M)$ such that
\[
 \|R_F\|_{C^{1,1}}\le K\qquad(F\in\mathcal F_{a,b,M}).
\]
For every $0<\gamma<1$ there is $K_\gamma$, with the same fixed
parameter dependence, such that for $F,G\in\mathcal F_{a,b,M}$ and
$\delta=\|F-G\|_\infty\le1$,
\[
 \|R_F-R_G\|_{C^{1,\gamma}}
       \le K_\gamma\delta^{(1-\gamma)/2}.
\]
These bounds include changes between the infinity alternatives in
Theorem~\ref{th:main}. They assume no uniform right contact cutoff.
\end{theorem}
\begin{proof}
The left tangents of $A$ tend uniformly to $-\infty$ on $[a,b]$.
Choose $a_0<a$, depending only on $\alpha,a,b,M$, so that every
tangent at $x<a_0$ lies below $A-M$ on $[a,b]$. It is below
$A+F$ globally and touches $A$ at $x$, where $F=0$.
Thus $C_F=A$ on the same left interval for every $F$ in the family.
All residuals vanish on the same neighborhood of the pole.
The bounds
\[
 |C_F-A|\le M,\quad |C_F'-A'|\le1,\quad
 0\le C_F''\le\|A''\|_\infty+M\quad\hbox{a.e.}
\]
give uniform real Hessian bounds on any fixed compact annulus.

Put $B=\max(b,0)+1$. For $x>B$, the obstacle is $A$.
At contact points $C_F'=A'$. At a free point, the slope is
$A'(d)\ge A'(x)$ if the free interval has a finite right contact
endpoint $d$. An unbounded right free interval has slope one.
Consequently, at every $x>B$,
\[
 0\le1-C_F'(x)\le1-A'(x)\le e^{-x}.
\]
The locally Lipschitz functions $C_F',A'$ agree on the contact set.
A locally Lipschitz function has derivative zero almost everywhere
on its zero set: use its differentiability at density points and
zero-set points approaching them. Hence $C_F''=A''$ almost
everywhere on that contact set, whereas $C_F''=0$ on the free set.
The reference derivative formula now gives
\[
 0\le C_F''(x)\le A''(x)
       \le(1+\alpha(1-\alpha))e^{-x}\quad\hbox{a.e. on }x>B.
\]

In a projective chart $Z_j\ne0$, $j\ge1$, set
$\zeta=Z_0/Z_j$, $y=(Z_i/Z_j)_{i\ge1,i\ne j}$ and
\[
 H(y)=1+\sum|y_i|^2,\qquad R=|\zeta|^2/H(y),\qquad x=-\log R.
\]
On fixed relatively compact chart pieces,
$|\nabla R|\le c\sqrt R$ and $|\nabla^2R|\le c$.
Put $d_F=1-C_F'$ and express the envelope as
$\mathcal E(R)=C_F(-\log R)+\log R-\log(1+R)$ for $R>0$.
Then
\[
 \mathcal E_R=\frac{d_F}{R}-\frac1{1+R},\qquad
 \mathcal E_{RR}=\frac{C_F''-d_F}{R^2}+\frac1{(1+R)^2}
 \quad\hbox{a.e.}
\]
The preceding inequalities give $|\mathcal E_R|\le2$ and
$|\mathcal E_{RR}|\le c_\alpha/R+1$. The real chain rule therefore
bounds $\nabla^2\mathcal E$ uniformly in these projective charts.
Also $\nabla\mathcal E\to0$ as $\zeta\to0$.
The limit $L_F=\lim_{x\to\infty}(C_F(x)-x)$ lies in $[-M,0]$, and
integrating $0\le1-C_F'\le e^{-x}$ yields
$|C_F(x)-x-L_F|\le e^{-x}$.
The value error is thus $O(R)$, so the extended envelope is
differentiable at $\zeta=0$ with derivative zero.

The continuous gradient has a local $W^{1,\infty}$ bound on
coordinate boxes disjoint from $\zeta=0$, hence an actual Lipschitz
representative there by convolution. Subdivide a straight coordinate
segment into such boxes and pass to its possible single crossing of
$\zeta=0$ by gradient continuity. A segment contained in that
hyperplane has zero gradient throughout. This proves a uniform
$C^{1,1}$ bound across infinity. Subtract the fixed smooth $\psi$
there, and combine this bound with the common left cutoff and the
fixed intervening annulus to obtain the global assertion.

Finally $Z=R_F-R_G$ satisfies $\|Z\|_\infty\le\delta$ by
Corollary~\ref{cor:mass} and has a uniform Lipschitz gradient.
On a smaller fixed chart, a real directional increment $h$ gives
\[
 |\partial_e Z|\le2\delta/h+K h.
\]
Choosing $h=\sqrt{\delta/K}$ when within the chart radius, and
enlarging the fixed constant otherwise, gives
$\|\nabla Z\|_\infty\le c\sqrt\delta$.
For points separated by $t$,
\[
 |\nabla Z(x)-\nabla Z(y)|\le
             \min(c\sqrt\delta,2Kt).
\]
Divide by $t^\gamma$ and split at $t=\sqrt\delta$.
A finite atlas gives the stated $C^{1,\gamma}$ estimate.
The case $\delta=0$ follows directly from the uniform value estimate.
No $C^{1,1}$ convergence is inferred.
\end{proof}

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
stretching class $\Eenv(X,H,\psi)$. On any one fixed such product,
the uniform bounds and derivative stability of
Theorem~\ref{th:uniform} hold for the pulled-back residuals.
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
$E_F^H\geq\psi-K_0$. The genuine potential $a_1=E_F^H$ supplies
the defining inequality at $t=1$. For $t>1$, use $a_t=\psi-tK_0$, which satisfies
$t^{-1}a_t+(1-t^{-1})\psi=\psi-K_0\leq E_F^H$.
This proves the exact stretching definition, together with ordinary
order. The reference is genuine; no model-envelope identification
or unbounded-product continuity theorem has been substituted.
The uniform family and derivative estimates pull back to the fixed
smooth product atlas, with constants depending also on that atlas.
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


## Entire component: notes/S06-singular-weighted-exact-slicing-inclusive-full-review-20261007-argument.md

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


## Entire component: notes/S06-singular-radial-weighted-envelope-convex-obstacle-20261007.private-unverified.md

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
slope>1 contradicts g(x)=x+o(1) at +infinity. The sandwich bounds for the
maximal convex minorant C force C's asymptotic slopes to be0 and1.
(Constant affine minorants do not exist, since
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


## Entire component: notes/S06-uniform-family-residual-C11-and-C1gamma-stability-20261007.private-unverified.md

# S06: uniform singular-obstacle residual estimates

Private, unverified additional candidate. This is not part of the frozen A--H
statement-only campaign and has not passed independent reconstruction. It does
not solve the unrestricted original S06 programme. Preserve the current article,
full review, its INCONCLUSIVE original verdict, and the existing cold input.

Fix k>=2, 0<alpha<1 and the exact projective reference psi and total profile A
of the article. Fix a finite interval [a,b] and M>0. Let F range over real
C^2 functions supported in [a,b] with ||F||_infinity+||F''||_infinity<=M.
Write C_F for the full convex minorant already proposed in A--H and
R_F=E_F-psi for its canonically extended residual.

Proposed strengthening I: there is K=K(k,alpha,a,b,M), in any fixed finite
projective coordinate atlas, such that ||R_F||_{C^{1,1}}<=K for this entire
family. In particular a sequence passing through the change between an affine
right tail and an unchanged right tail still has a uniform residual Hessian
bound. This claims no uniform bound on the locations of the right cutoffs.
For every 0<gamma<1 and delta=||F-G||_infinity<=1,

    ||R_F-R_G||_{C^{1,gamma}} <= K_gamma delta^((1-gamma)/2).

The full product residuals satisfy the analogous estimate on any one fixed
product with a smooth positive Hermitian factor. No C^{1,1} convergence for
varying obstacles, regularity of the singular envelope itself, new ideal
operator, prescribed arbitrary-density equation or general obstacle set is
asserted.

## 1. Uniform left end and compact annulus

The exact tangent intercept A(x)-xA'(x) tends to minus infinity as x tends
to minus infinity, whereas A'(x) tends to zero. Hence the tangent
ell_x(y)=A'(x)y+A(x)-xA'(x) tends uniformly to minus infinity for y in [a,b].
There is a left cutoff a_0<a, depending only on alpha,a,b,M, such that every
ell_x with x<a_0 lies below A-M on [a,b]. Outside [a,b] it lies below A=g.
It is therefore a global minorant of g=A+F touching A at x. The inequalities
C<=g give C=A on x<a_0. Thus every residual in this family is zero on the
same actual neighborhood of the pole.

The convex obstacle proof gives |C-A|<=M, |C'-A'|<=1 and

    0<=C''<=sup max(A''+F'',0)<=||A''||_infinity+M

almost everywhere. These are uniform total-profile estimates. On the fixed
compact projective annulus a_0<=x<=max(b,0)+1 they give a uniform real Hessian
bound for C-A by the smooth-coordinate chain rule. No moving end cutoff is
used here.

## 2. Sharper estimates at the right end

Put B=max(b,0)+1. For x>B, g=A and A is strictly convex. At a contact point
C(x)=A(x), differentiability gives C'(x)=A'(x). At a free point in a bounded
free interval (c,d), its right endpoint d is a contact point, so the constant
slope on that interval is A'(d)>=A'(x). If the free interval is unbounded
on the right, the limiting slope of C is one, so its slope is one.
Consequently for EVERY x>B,

    0<=1-C'(x)<=1-A'(x)<=e^(-x).

The last inequality follows exactly from
A'=p+(1-p)alpha T^(alpha-1), p=e^x/(1+e^x), T>=1.

Also C' and A' are locally Lipschitz. On the contact set C'=A'. The derivative
of a locally Lipschitz function is zero almost everywhere on its zero set:
at differentiability and density points, choose zero-set points with relative
distances tending to zero, and use its first-order expansion. Apply this to
C'-A'. On the open free set C''=0. Thus, almost everywhere on x>B,

    0<=C''(x)<=A''(x)
       =p(1-p)(1-alpha T^(alpha-1))
         +alpha(1-alpha)(1-p)^2 T^(alpha-2)
       <=(1+alpha(1-alpha))e^(-x).

These bounds remain uniform when inf(g-x) approaches zero and the unchanged
right tail moves arbitrarily far out.

## 3. Actual projective coordinate bounds across infinity

On a projective chart Z_j!=0, j>=1, write
zeta=Z_0/Z_j and y=(Z_i/Z_j)_{i>=1,i!=j}. Choose finitely many relatively
compact chart pieces covering the hyperplane at infinity. On each piece,

    H(y)=1+sum|y_i|^2,
    R=|zeta|^2/H(y),  x=-log R.

H is bounded above and below, with all needed derivatives bounded. In real
coordinates |grad R|<=c sqrt(R) and |Hess R|<=c. These follow by directly
differentiating the displayed smooth expression; constants depend only on
the chosen pieces.

For R>0 define E(R)=C(-log R)+log R-log(1+R). With d(x)=1-C'(x),

    E_R=d/R-1/(1+R),
    E_RR=(C''-d)/R^2+1/(1+R)^2

almost everywhere. The right-end estimates give |E_R|<=2 and
|E_RR|<=c_alpha/R+1. Hence the real coordinate chain rule gives

    |Hess E(R)| <= |E_RR||grad R|^2+|E_R||Hess R| <= c.

The gradient tends uniformly to zero as zeta tends to zero. The value tends
to the constant L=lim(C(x)-x) in [-M,0]. Indeed C-x is nonincreasing and
sandwiched by A-x-M and A-x+M; since C<=A on the right its limit is at most
zero. The sharper derivative estimate also gives |C(x)-x-L|<=e^(-x), by
integrating 0<=1-C'(x)<=e^(-x) to infinity. Thus the continuous extension is
differentiable across zeta=0 with derivative zero (the value error is O(R)).

The gradient is Lipschitz across the hyperplane as well. Its local
W^{1,infinity} bound on each convex box disjoint from zeta=0 gives its actual
continuous gradient a Lipschitz representative, by ordinary convolution.
On a straight coordinate segment not contained in zeta=0 there is at most
one crossing point; cover each remaining compact subsegment by such boxes,
sum the Lipschitz estimates, and use continuity at the crossing point.
A segment contained in
zeta=0 has constant E and zero gradient. Choose sufficiently small convex
coordinate boxes inside each chart piece. This proves the real C^{1,1}
extension with a uniform bound. Subtracting the fixed smooth psi near this
hyperplane gives the required uniform bound for its residual.

Together with the uniform left end and fixed annulus, this proves the
proposed global estimate, conditional on the complete base A--H convex
envelope theorem. It requires no uniform right-cutoff location.

## 4. Stability of the derivatives

The already proposed competitor translation gives ||R_F-R_G||_infinity<=delta.
Let Z=R_F-R_G. On a fixed smaller coordinate box |Hess Z|<=2K. For a unit
real direction and an increment h staying inside the larger box, Taylor's
formula with the Lipschitz gradient gives

    |partial_e Z| <= 2delta/h+K h.

Take h=sqrt(delta/K) when it lies below the fixed chart radius. When it does
not, the fixed uniform gradient bound enlarges the constant in the same
estimate. Thus ||grad Z||_infinity<=c sqrt(delta), for 0<delta<=1. The
zero-delta case gives equality of the residuals by the C^0 estimate.

For points at distance t in a chart, combine the gradient supremum bound
and the uniform Lipschitz bound:

    |grad Z(x)-grad Z(y)| <= min(c sqrt(delta),2K t).

Dividing by t^gamma and splitting at t=sqrt(delta) gives
[grad Z]_{C^gamma}<=c_gamma delta^((1-gamma)/2). The value and gradient
suprema satisfy the same weaker exponent for delta<=1. A finite atlas and
smooth coordinate transitions prove the displayed global C^{1,gamma}
stability estimate. Pullback to a fixed smooth product preserves it, with
constants depending on that product's fixed charts.

No external regularity theorem or rough linearized Monge-Ampere operator is
being assumed for this argument. The local differentiation, contact-set
argument and finite-difference interpolation are provided here. All existing
foundational envelope/product dependencies remain as in A--H and still need
the independent full reconstruction. This additional I must receive its own
statement-only reconstruction and source/application assessment before any
checked release includes it.


## Entire component: checks/S06-singular-weighted-exact-slicing-full-review-20261007-complete-result.json

{
  "verdict": "INCONCLUSIVE",
  "report": "The declared radial singular-obstacle theorem, its measure formula, and its nonclosed product extension withstand independent reconstruction. No concrete mathematical defect was found in these assertions. They establish a specific compact envelope result, but do not establish completion of the unchanged S06 task: conditions for independently prescribed Monge–Ampère equations in arbitrary ordinary or relative types, general compact obstacle sets, and ideal weighted extremals remain open in the supplied argument.\n\nThe reference calculation is correct. With a=αT^(α−1), the displayed formulas give 0<A′<1 and A″>0, with A″ bounded. The left tangent intercept tends to −∞; the right intercept tends to zero. The pole is genuinely sublogarithmic and unbounded. Near infinity, R=|Z₀|²/(Σⱼ≥1|Zⱼ|²) is smooth, so the asserted extension of ψ is valid. Both κ and H are positive backgrounds and therefore satisfy the task’s bigness definition with potential zero.\n\nThe convex reduction uses the full competitor family correctly. The obstacle supplies local uniform upper bounds, and ψ−‖F‖∞ prevents collapse. Upper regularization preserves the obstacle inequality, including its −∞ value at the pole. Unitary invariance makes the envelope radial without restricting competitors. The radial Hessian calculation gives convexity and nonnegative slope of its total profile. Conversely, the largest convex minorant C has slopes in [0,1], the sandwich bounds force its limiting slopes to be 0 and 1, and local removable-singularity results apply at both projective ends. Thus C−log(1+eˣ) is an admissible global competitor, proving equality and ordinary type retention.\n\nThe regularity proof is valid. Chord replacement proves affineness on every free component. At a contact point, C′₋≥g′≥C′₊, together with convexity, forces differentiability and equality with g′. Moving endpoints through free components then proves 0≤C′(b)−C′(a)≤L₂(b−a), including the unbounded-component cases. The left tangent test proves C=A on an actual left interval. At infinity, all alternatives are covered: an attained L=inf(g−x) gives C=x+L on a right tail; otherwise L=0 and the right tangent test gives C=A there. These exact end formulas justify extension of the residual across the pole and hyperplane. The annular Hessian estimate gives the stated global C¹,¹ conclusion, with constants depending on the constructed cutoffs. It provides no uniform C¹,¹ convergence assertion for varying obstacles.\n\nThe measure normalization is correct for ddᶜ=i∂∂̄/(2π): the smooth radial density is k!π^(−k)(C′)^(k−1)C″r^(−k), whose polar integral is d(C′ᵏ). Even one-dimensional mollification supplies decreasing smooth convex profiles, so bounded Bedford–Taylor continuity applies on annuli. Consequently the annular mass is C′(b)ᵏ−C′(a)ᵏ. Continuity of C′ excludes radial atoms, the non-pluripolar construction excludes pole mass, and smoothness excludes hyperplane mass. Total mass is therefore one. Free intervals have zero top-degree density. The negative bump example really produces an open zero-density tail; for example k=2, α=1/2, x₀=0 and M=1 work because A(0)<log 2<1. The residual stability bound follows directly by translating competitors and extending their finite residuals continuously.\n\nBoth supplied slicing proofs are valid. In the supplementary proof, v+ρ(z)+q(y) has positive complex Hessian because ddᶜρ=κ and ddᶜq≥h₀. Its canonical holomorphic restriction is psh or identically −∞ on every slice. Subtracting q(y₀) and ρ gives exactly κ-psh slices. This establishes the pointwise upper bound for every product competitor; lifting the base envelope establishes equality. The convolution proof in the article also preserves the exact slice bound after its smooth background error tends to zero. No transitive symmetry on Y or generic-slice argument is needed.\n\nAt every bounded truncation, the corrected product expansion has only the term with k base factors and m factor factors. Restriction to strict superlevel sets gives the claimed tensor measure and mass binom(k+m,k)V₀. The explicit restricted masses are bounded, so this particular unbounded construction requires no BMP assumption. The Hopf form is positive, scaling invariant and satisfies dh₀=−ds∧ddᶜs≠0. The quotient is S³×S¹; its odd first Betti number excludes a Kähler metric. The product example is consequently a genuine nonclosed non-Kähler fourfold. The stretching-class assertion uses the correct definition and the explicit witness aₜ=ψ−t‖F‖∞. These are actual representative masses, not lower or upper singularity volumes.\n\nThe private proposal’s multiplier-ideal aside also checks out: for every t>0, sublogarithmic growth makes exp(−tψ) locally integrable, so I(tψ)=O. Its zero-obstacle ordinary model is indeed zero: for any finite x, a tangent to f(x)=log(1+eˣ) lies below A+c for sufficiently large c; the convex minorant of min(f,A+c) then supplies a type-controlled competitor attaining zero there. Upper regularization erases the isolated pole. This does not identify the article’s obstacle envelope with an ideal envelope.\n\nThe indispensable local hypotheses were checked in [Demailly](https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf), [Bedford–Taylor](https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf), and [Boucksom–Guedj–Lu](https://arxiv.org/html/2406.01090v1). The latter is used only for bounded corrected products. Task passages below record canonical-representative and product conventions; those granted conventions are excluded from the external-premise list.\n\nThe literature comparison is accurate for [Ahn’s continuity theorem](https://arxiv.org/html/2604.01885v3), [Ahn’s Hölder theorem](https://arxiv.org/html/2604.01887v3), and [Nguyen’s continuity theorem](https://arxiv.org/pdf/2305.04171): their stated weights are finite and continuous or Hölder, whereas ψ+F has a genuine pole. Here K=X satisfies capacity density. Thus the demonstrated distinction is the singular weight and retained ordinary type, rather than failure of capacity density. This establishes a narrow residual/envelope result beyond the listed logarithmic and minimal examples; source-hypothesis failure alone does not certify broader novelty or resolve the general weighted programme.\n\nHarmless wording corrections: R should be called a smooth projective function, rather than a coordinate. In the private proposal, the assertion that the asymptotic slopes are 0 and 1 should explicitly refer to C with its sandwich bounds; arbitrary affine minorants need not have those limiting slopes. Neither correction changes the proof. No substantial repair is required for the declared theorems. The unresolved issue is their limited coverage of the original completion criteria.",
  "passages": [
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/0",
      "statement": "For a locally uniformly upper-bounded family of plurisubharmonic functions on a complex domain, the upper semicontinuous regularization of its supremum is plurisubharmonic, allowing an identically −∞ component. Demailly, Chapter I, Theorem 5.7.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf#page=39",
      "quote": "is plurisubharmonic",
      "premise": 0
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/1",
      "statement": "A distribution on a complex domain with positive complex Hessian has a unique locally integrable plurisubharmonic representative. Standard radial mollifications of a locally integrable plurisubharmonic function are smooth and plurisubharmonic on smaller domains and decrease pointwise to its canonical values as their radii tend to zero. Demailly, Chapter I, Theorems 5.5 and 5.8.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf#page=40",
      "quote": "there exists a unique function",
      "premise": 1
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/2",
      "statement": "A distribution on a complex domain with positive complex Hessian has a unique locally integrable plurisubharmonic representative. Standard radial mollifications of a locally integrable plurisubharmonic function are smooth and plurisubharmonic on smaller domains and decrease pointwise to its canonical values as their radii tend to zero. Demailly, Chapter I, Theorems 5.5 and 5.8.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf#page=39",
      "quote": "is non decreasing in ε",
      "premise": 1
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/3",
      "statement": "A distribution on a complex domain with positive complex Hessian has a unique locally integrable plurisubharmonic representative. Standard radial mollifications of a locally integrable plurisubharmonic function are smooth and plurisubharmonic on smaller domains and decrease pointwise to its canonical values as their radii tend to zero. Demailly, Chapter I, Theorems 5.5 and 5.8.",
      "url": "urn:xean:task",
      "quote": "All potentials are genuine canonical quasi-psh representatives, with pole values included.",
      "premise": 1
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/4",
      "statement": "If f:X→Y is holomorphic between complex manifolds and u is plurisubharmonic on Y, then u∘f is plurisubharmonic on each component of X or identically −∞. Demailly, Chapter I, Theorem 5.11.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf#page=40",
      "quote": "then v ◦ F ∈ Psh(X).",
      "premise": 2
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/5",
      "statement": "A plurisubharmonic function on X\\A, where A is a closed pluripolar subset of a complex manifold X, extends uniquely plurisubharmonically across A if it is locally bounded above near A. Demailly, Chapter I, Theorem 5.24.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf#page=45",
      "quote": "extends uniquely",
      "premise": 3
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/6",
      "statement": "For locally bounded plurisubharmonic functions on a complex domain, Bedford–Taylor wedge products are closed positive currents and form a symmetric multilinear operator. If each input sequence decreases pointwise to a locally bounded plurisubharmonic limit, its wedge products converge weakly to the wedge product of the limits. Bedford–Taylor, A new capacity for plurisubharmonic functions, Theorem 2.1 and Corollary 2.2.",
      "url": "https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf#page=4",
      "quote": "where the limit is in the weak topology",
      "premise": 4
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/7",
      "statement": "On a compact complex manifold, for smooth real (1,1)-forms θ_i and bounded quasi-psh functions u_i, the products of T_i=θ_i+ddᶜu_i defined by expansion into smooth-background factors and bounded Bedford–Taylor factors are independent of the decompositions, symmetric, multilinear, non-pluripolar and local in the plurifine topology. They are positive when every T_i is positive. This bounded-potential assertion requires no bounded mass property. Boucksom–Guedj–Lu, Section 2.1, Proposition 2.1.",
      "url": "https://arxiv.org/html/2406.01090v1",
      "quote": "acting on tuples of quasi-psh functions bounded on K is local in the plurifine topology.",
      "premise": 5
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/8",
      "statement": "On a compact complex manifold, for smooth real (1,1)-forms θ_i and bounded quasi-psh functions u_i, the products of T_i=θ_i+ddᶜu_i defined by expansion into smooth-background factors and bounded Bedford–Taylor factors are independent of the decompositions, symmetric, multilinear, non-pluripolar and local in the plurifine topology. They are positive when every T_i is positive. This bounded-potential assertion requires no bounded mass property. Boucksom–Guedj–Lu, Section 2.1, Proposition 2.1.",
      "url": "urn:xean:task",
      "quote": "Extended products are non-pluripolar products with smooth-background corrections.",
      "premise": 5
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/9",
      "statement": "Every odd Betti number of a compact Kähler manifold is even. Demailly, Chapter VI, equation 8.12 and its consequence.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf#page=313",
      "quote": "are even.",
      "premise": 6
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/10",
      "statement": "Using ddᶜ=2i∂∂̄, let (X,ω) be a compact Hermitian manifold and K⊂X a compact non-pluripolar set. Define V_{K,w}=sup{u∈PSH(X,ω):u≤w on K} and V_K=V_{K,0}. If w:X→ℝ is continuous and V_K is continuous, then V_{K,w} is continuous. Ahn, arXiv:2604.01885v3, Theorem 1.4(ii).",
      "url": "https://arxiv.org/html/2604.01885v3",
      "quote": "If φ:X→ℝ is continuous and V_K is continuous, then V_{K,φ} is continuous.",
      "premise": 7
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/11",
      "statement": "Using ddᶜ=2i∂∂̄, let (X,ω) be a compact Hermitian manifold and K⊂X a compact non-pluripolar set. Define V_{K,w}=sup{u∈PSH(X,ω):u≤w on K} and V_K=V_{K,0}. If K has uniform density in capacity and both w:X→ℝ and V_K are Hölder continuous, then V_{K,w} is Hölder continuous. Ahn, arXiv:2604.01887v3, Theorem 1.1(ii).",
      "url": "https://arxiv.org/html/2604.01887v3",
      "quote": "If K has a uniform density in capacity and φ:X→ℝ and V_K are Hölder continuous, then V_{K,φ} is Hölder continuous.",
      "premise": 8
    },
    {
      "id": "94060f98-84df-49e5-ad37-b4bf2207fe9c/12",
      "statement": "Let (X,ω) be a compact Kähler manifold and K⊂X a compact non-pluripolar set. For the ordinary weighted extremal V_{K,w}=sup{u∈PSH(X,ω):u≤w on K}, a finite continuous weight w:X→ℝ and continuity of V_{K,0} imply continuity of V_{K,w}. Nguyen, Regularity of the Siciak-Zaharjuta extremal function on compact Kähler manifolds, Theorem 1.1(b).",
      "url": "https://arxiv.org/pdf/2305.04171#page=3",
      "quote": "If V_K is continuous, then V_{K,φ} is continuous.",
      "premise": 9
    }
  ],
  "premises": [
    "For a locally uniformly upper-bounded family of plurisubharmonic functions on a complex domain, the upper semicontinuous regularization of its supremum is plurisubharmonic, allowing an identically −∞ component. Demailly, Chapter I, Theorem 5.7.",
    "A distribution on a complex domain with positive complex Hessian has a unique locally integrable plurisubharmonic representative. Standard radial mollifications of a locally integrable plurisubharmonic function are smooth and plurisubharmonic on smaller domains and decrease pointwise to its canonical values as their radii tend to zero. Demailly, Chapter I, Theorems 5.5 and 5.8.",
    "If f:X→Y is holomorphic between complex manifolds and u is plurisubharmonic on Y, then u∘f is plurisubharmonic on each component of X or identically −∞. Demailly, Chapter I, Theorem 5.11.",
    "A plurisubharmonic function on X\\A, where A is a closed pluripolar subset of a complex manifold X, extends uniquely plurisubharmonically across A if it is locally bounded above near A. Demailly, Chapter I, Theorem 5.24.",
    "For locally bounded plurisubharmonic functions on a complex domain, Bedford–Taylor wedge products are closed positive currents and form a symmetric multilinear operator. If each input sequence decreases pointwise to a locally bounded plurisubharmonic limit, its wedge products converge weakly to the wedge product of the limits. Bedford–Taylor, A new capacity for plurisubharmonic functions, Theorem 2.1 and Corollary 2.2.",
    "On a compact complex manifold, for smooth real (1,1)-forms θ_i and bounded quasi-psh functions u_i, the products of T_i=θ_i+ddᶜu_i defined by expansion into smooth-background factors and bounded Bedford–Taylor factors are independent of the decompositions, symmetric, multilinear, non-pluripolar and local in the plurifine topology. They are positive when every T_i is positive. This bounded-potential assertion requires no bounded mass property. Boucksom–Guedj–Lu, Section 2.1, Proposition 2.1.",
    "Every odd Betti number of a compact Kähler manifold is even. Demailly, Chapter VI, equation 8.12 and its consequence.",
    "Using ddᶜ=2i∂∂̄, let (X,ω) be a compact Hermitian manifold and K⊂X a compact non-pluripolar set. Define V_{K,w}=sup{u∈PSH(X,ω):u≤w on K} and V_K=V_{K,0}. If w:X→ℝ is continuous and V_K is continuous, then V_{K,w} is continuous. Ahn, arXiv:2604.01885v3, Theorem 1.4(ii).",
    "Using ddᶜ=2i∂∂̄, let (X,ω) be a compact Hermitian manifold and K⊂X a compact non-pluripolar set. Define V_{K,w}=sup{u∈PSH(X,ω):u≤w on K} and V_K=V_{K,0}. If K has uniform density in capacity and both w:X→ℝ and V_K are Hölder continuous, then V_{K,w} is Hölder continuous. Ahn, arXiv:2604.01887v3, Theorem 1.1(ii).",
    "Let (X,ω) be a compact Kähler manifold and K⊂X a compact non-pluripolar set. For the ordinary weighted extremal V_{K,w}=sup{u∈PSH(X,ω):u≤w on K}, a finite continuous weight w:X→ℝ and continuity of V_{K,0} imply continuity of V_{K,w}. Nguyen, Regularity of the Siciak-Zaharjuta extremal function on compact Kähler manifolds, Theorem 1.1(b)."
  ],
  "kind": "codex-report",
  "operationId": "94060f98-84df-49e5-ad37-b4bf2207fe9c",
  "reportedAt": "2026-10-07T20:16:23.643Z"
}


## Entire component: checks/S06-singular-weighted-native-blind-20261007-complete-result.json

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "Primary literature retrieved independently; finite-weight regularity and general nonclosed product theorems do not supply the singular-envelope proof.",
      "detailedSummary": "Records the ordinary psh supremum, restriction and extension tools, Bedford–Taylor continuity, non-pluripolar truncations, and the BMP hypothesis of the general Hermitian product extension. Independently checks Ahn’s finite continuous and Hölder weight hypotheses. Primary passages were saved through the web tool; direct shell downloads failed. No supplied proof or earlier notes were used.",
      "text": "Conventions and independently retrieved primary tools. Throughout D=i∂bar∂/(2π), d^c=i(bar∂−∂)/(4π), so dd^c=D. Wedges are ordinary wedges. Genuine quasi-psh representatives retain their canonical values, including −∞. No supplied or earlier notes existed.\n\nThe following foundational results are used with their stated hypotheses.\n\n1. Demailly, Complex Analytic and Differential Geometry, Chapter I, Theorems 5.5, 5.7, 5.11 and 5.24, author-hosted text: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf . These give psh smoothing, the psh usc supremum for locally uniformly upper-bounded families, holomorphic restriction possibly identically −∞, and canonical extension across closed pluripolar sets under local upper boundedness. The distributional psh criterion applies to the canonical representative. Positive rescaling of D does not change these assertions.\n\n2. Bedford–Taylor, A new capacity for plurisubharmonic functions, Acta Math. 149 (1982), 1–40, Theorem 2.1 and Corollary 2.2: https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf . Locally bounded psh potentials have symmetric multilinear products continuous under decreasing psh approximation. Applications below concern bounded truncations or locally bounded potentials away from the pole.\n\n3. Boucksom–Eyssidieux–Guedj–Zeriahi, Monge–Ampère equations in big cohomology classes, arXiv:0812.3674v2, Section 1.2, Proposition 1.6 and formula (1.7): https://arxiv.org/pdf/0812.3674v2 . Non-pluripolar products use truncation and locality and discard pole sets; compact Kähler backgrounds guarantee finiteness for closed positive currents. Their closed Kähler uniqueness theory is not applied to arbitrary Hermitian products.\n\n4. Boucksom–Guedj–Lu, Volumes of Bott–Chern classes, Sections 2.1–2.2 and Theorem A: https://arxiv.org/html/2406.01090v1 . Bounded products use local psh shifts and smooth-background corrections. Their general global extension for all unbounded quasi-positive, quasi-closed currents requires BMP. Below, BMP is not assumed for arbitrary Y: the particular top-degree truncation limit is explicitly proved finite. Its mass is not identified with an infimum or supremum over an ordinary type.\n\n5. Ahn, Characterization of continuity of Siciak–Zaharjuta extremal functions on compact Hermitian manifolds, arXiv:2604.01885v2, definitions (1.1)–(1.2), Theorem 1.4(ii): https://arxiv.org/html/2604.01885v2 . Weighted continuity assumes a finite continuous weight and continuous unweighted extremal. Ahn, Hölder regularity of Siciak–Zaharjuta extremal functions on compact Hermitian manifolds, arXiv:2604.01887v3, definition (1.2), Theorem 1.1(ii): https://arxiv.org/html/2604.01887v3 . Weighted Hölder regularity assumes finite Hölder weight, Hölder unweighted extremal and uniform density in capacity. Neither theorem applies to the genuine −∞ weight ψ+F or proves regularity of its retained residual. Their operators also do not impose the original question’s ideal order.\n\nEvidence and rerun record. Primary passages were independently retrieved on 2026-10-07 and saved in literature/web1.json through literature/web8.json. The attempted BGL finds in web8 returned mismatched source labels and are not used; direct BGL passages in web5–web7 are used. Run python retrieve.py > literature/retrieval.log to repeat the shell retrieval attempts. All returned 'Operation not permitted', recorded in literature/retrieval.json; full PDFs were not downloaded. The saved web responses contain the retrieved primary evidence. No author argument for A–H was supplied or imported. These tools support the independently reconstructed proofs below. The notes remain unverified drafts.\n\nArtifacts: /workspace/research/native-workers/codex-7EljrU",
      "support": []
    },
    {
      "id": "n2",
      "summary": "A proved: ψ has a genuine sublogarithmic pole and an explicitly strictly convex profile, including both canonical ends.",
      "detailedSummary": "Derives exact first and second derivatives, proves 0<A′<1 and 0<A″≤1/4+α(1−α), and gives left and right asymptotics. Establishes genuine κ-psh extension with ψ(0)=−∞ and ψ=0 at infinity. In fact κ+Dψ≥(1−α)κ.",
      "text": "Proof of A. Fix k≥2 and 0<α<1. On the standard affine chart put r=|z|², x=log r, a(x)=log(1+e^x), p=e^x/(1+e^x), q=1−p and T=1−log p=1+log(1+e^(−x)). The specified standard normalized form is κ=Da(log r). Its normalization is independently checked in n5; no rescaling is introduced.\n\nSince p′=pq and T′=−q, with b=αT^(α−1) we obtain\nψ′=qb,\nA′=p+qb=1−q(1−b),\nA″=pq(1−b)+α(1−α)q²T^(α−2).\nHere 0<b≤α<1. Consequently 0<A′<1, A″>0, and A″≤Bα:=1/4+α(1−α).\n\nAs x→−∞,\nA=1−(1−x)^α+O(e^x),\nA′=α(1−x)^(α−1)+O(e^x),\nA″=α(1−α)(1−x)^(α−2)+O(e^x).\nThese follow from T=1−x+O(e^x) and the derivative identities. Thus A→−∞, A/x→0, A′→0 and ψ/x→0. The pole is unbounded and sublogarithmic.\n\nAt +∞ set σ=e^(−x), t=log(1+σ). Then\nA−x=t+1−(1+t)^α>0,\nA−x=(1−α)σ−(1−α)²σ²/2+O(σ³),\nA′=1−(1−α)σ+O(σ²),\nA″=(1−α)σ+O(σ²).\nStrict positivity follows from strict concavity of (1+t)^α. The defect A−x decreases to zero because A′<1; at the left end it tends to +∞.\n\nFor a smooth radial profile Q, the complex Hessian matrix of Q(log r) is (Q′/r)I+((Q″−Q′)/r²)bar z⊗z. Its eigenvalues are Q′/r with multiplicity k−1 and Q″/r in the radial direction. Therefore DA is positive off 0. The corresponding eigenvalue numerators for κ are p and pq. Since A′≥p and A″≥(1−α)pq, κ+Dψ≥(1−α)κ there.\n\nA is locally bounded above and locally integrable near 0, since powers of |log r| are integrable against r^(k−1)dr. The psh extension theorem in n1 extends it canonically. Its limit is −∞, forcing the genuine value ψ(0)=−∞. Applying the same extension argument after subtracting a local potential of (1−α)κ preserves the strict current inequality across 0.\n\nAt infinity use [Z0:…:Zk], a chart Zj≠0 with j≥1, τ=Z0/Zj, ξi=Zi/Zj for i≠0,j, and S=1+Σ|ξi|². Then σ=1/r=|τ|²/S, and ψ=1−(1+log(1+σ))^α is smooth through τ=0 with value zero. A local total κ-potential is log S+(A−x)(log r). At τ=0 its normal quadratic coefficient is (1−α)/S>0 and its tangential Hessian is that of log S. Positivity extends smoothly there. Thus ψ is a genuine global κ-psh potential with precisely the specified ends; the stronger inequality κ+Dψ≥(1−α)κ holds globally.\n\nArtifacts: /workspace/research/native-workers/codex-7EljrU",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "C and the convex end assertions of D proved for every C² compactly supported F and every free component, including accumulating components.",
      "detailedSummary": "The whole-line convex minorant is finite, lies between A±||F||∞ and has end slopes zero and one. It is affine on every strict-gap component, C¹, and has derivative Lipschitz constant sup max((A+F)″,0). Tangent-line cutoffs prove exact left contact and the unattained-zero right-contact case; an attained infimum forces the stated affine right tail.",
      "text": "Whole-line proof of C and the convex assertions in D. Let f=A+F, mF=||F||∞ and QF=sup_R max(f″,0)<∞. Define C as the supremum of all affine functions below f on the entire line. Tangents of A−mF are admissible, so\nA−mF≤C≤f≤A+mF. (1)\nThus C is finite, convex and continuous. Every finite convex minorant is the supremum of its supporting lines, so it lies below C. This verifies the equivalent definition as largest convex minorant.\n\nBy n2 and (1), C(x)/x→0 at −∞ and →1 at +∞. A negative supporting slope violates the left upper bound; a slope greater than one violates the right upper bound. Hence every subgradient is in [0,1]. Convex difference quotients and the same asymptotics give derivative limits zero and one at the respective ends.\n\nLet J={C<f}. Around x0∈J choose [u,v]⊂J sufficiently small that min(f−C)=δ>0 and osc C<δ on that interval. Replace C there by its chord. Convexity is preserved because the chord slope lies between the right derivative at u and the left derivative at v. The chord exceeds C by less than δ and therefore remains below f. Maximality forces C to equal this chord. Consequently C is locally affine on J and affine on every connected component, including any unbounded component. No finite-component assumption is used.\n\nAt a contact point s, comparison with f for positive and negative increments gives C′_+(s)≤f′(s)≤C′_−(s). Convexity gives the reverse ordering, so all are equal. At gap points C is affine. Hence C is differentiable everywhere; convexity then implies continuity of its derivative, since any derivative discontinuity would be a jump between distinct one-sided derivatives.\n\nFor a<b, if there is no contact in [a,b], the derivative increment is zero. Otherwise let s,t be the first and last contact in [a,b]. Affineness of the intervening end gaps gives C′(a)=C′(s) and C′(b)=C′(t). If s=t the increment is zero; otherwise\n0≤C′(b)−C′(a)=f′(t)−f′(s)=∫_s^t f″≤QF(t−s)≤QF(b−a).\nThis proves exactly the stated estimate and C∈C^{1,1}, with 0≤C″≤QF a.e. Also C′(x)>0 at every finite x: a zero derivative would force C constant on the left ray, contradicting C→−∞. The derivative may equal one on a right ray.\n\nHere are explicit sufficient end-cutoff inequalities. Choose u<v containing supp F. Write ℓ_t(x)=A(t)+A′(t)(x−t). As t→−∞,\nA(t)−tA′(t)=−(1−α)(1−t)^α+O(1),\nso ℓ_t(v)→−∞. Choose t_-<u satisfying ℓ_(t_-)(v)≤min_[u,v] f. For t≤t_- the inequality persists because dℓ_t(v)/dt=A″(t)(v−t)>0 for t<v. Since A′>0, ℓ_t≤f on [u,v]; elsewhere ℓ_t≤A=f. Thus ℓ_t is admissible and C(t)=A(t) for all t≤t_-. This is exact contact on a left end interval.\n\nLet L=inf_R(f−x). It is finite and L≤0 by the end behavior. The line x+L is below f and therefore below C. If L is attained at y, C(y)=f(y)=y+L. Since C′≤1, for x≥y,\nC(x)≤C(y)+x−y=x+L≤C(x).\nThus C=x+L on that entire ray.\n\nIf L<0, it is attained: f−x tends to +∞ at the left end and to zero at the right, so a minimizing sequence stays compact. The only remaining case is L=0 unattained. Then f−x>0 everywhere, and δ=min_[u,v](f−x)>0. As t→+∞, ℓ_t(x)−x→0 uniformly on [u,v], with maximum ℓ_t(u)−u. Choose t_+>v satisfying ℓ_(t_+)(u)−u≤δ. This persists for t≥t_+ because dℓ_t(u)/dt=A″(t)(u−t)<0. Again ℓ_t≤f globally, so C(t)=A(t) for all t≥t_+. These alternatives are exhaustive, including L=0 attained, and establish all claimed end assertions.\n\nArtifacts: /workspace/research/native-workers/codex-7EljrU",
      "support": [
        "n2"
      ]
    },
    {
      "id": "n4",
      "summary": "B, the residual part of D, and F proved for the full ordinary global obstacle over all competitors.",
      "detailedSummary": "The full envelope is psh and U(k)-invariant, so its total radial profile is a convex minorant. The constructed C-profile is a genuine admissible global competitor, forcing equality. The residual is canonically zero near the pole, smooth near infinity and globally C^{1,1}, with explicit annular bounds. Residual sup-norm stability has constant one.",
      "text": "Proof of B over all competitors. Define U=C(log r)−a(log r) off 0. Convexity and C′≥0 make C(log r) psh, using the radial Hessian calculation and convex-profile smoothing for nonsmooth C. By n3, C=A on a left end, so U=ψ there and its canonical pole value is −∞. At infinity either C=A, giving U=ψ, or C=x+L, giving U=L−log(1+σ). The latter is smooth in the infinity coordinates of n2 and has local total κ-potential log S+L. Thus U is a genuine global κ-psh potential.\n\nThe bounds in n3 give |U−ψ|≤mF off the pole, U≤ψ+F everywhere and U≃ψ in ordinary order, with the same genuine pole. Therefore U is an admissible competitor.\n\nLet E be the usc supremum over the entire declared family. It is nonempty because ψ−mF is a competitor. In every κ-potential chart, the local total potentials form a locally uniformly upper-bounded psh family; n1 makes their usc supremum psh. The obstacle ψ+F is usc, has limit −∞ at 0 and is continuous elsewhere. Hence regularization still gives E≤ψ+F everywhere, including the genuine pole. Also E≥ψ−mF.\n\nU(k) acts by [Z0:Z′]↦[Z0:UZ′], preserves κ and the obstacle, and permutes all competitors. Thus E is invariant without restricting the original family. Transitivity on affine spheres gives a finite profile Q(x)=E+a. Its restriction to a complex line is nontrivial by the lower bound A−mF. A radial subharmonic function Q(log|ζ|²) has Q″≥0 distributionally, so Q is convex with its canonical continuous representative. Since Q≤A+F, Q≤C. The competitor U gives the reverse envelope inequality. Consequently\nE_F=C(log r)−log(1+r)\nwith exactly the canonical global extensions stated above. The upper ordinary-order condition is automatic from this particular full obstacle, but retention of the resulting type also uses the lower bound. No ideal condition or quasi-everywhere relaxation is introduced.\n\nResidual and quantitative D. Numerical subtraction of two −∞ values is undefined. Define R_F=E_F−ψ=C−A off 0 and extend it by zero at 0, as forced by equality on a neighborhood. It is exactly zero for x≤t_-. At infinity it is either identically zero or\nR_F=L−[log(1+σ)+1−(1+log(1+σ))^α],\nσ=|τ|²/(1+Σ|ξi|²).\nThis expression is smooth through σ=0. Its infinity value is L in the attained case and zero in the unattained case.\n\nGlobally in x,\n||R_F||∞≤mF, |R_F′|≤1, |R_F″|≤QF+Bα a.e.\nOn a finite closed annulus a0≤log r≤b0, real Euclidean derivatives satisfy\n|∇R_F|≤2e^(−a0/2),\n||∇²R_F||op≤[4(QF+Bα)+2]e^(−a0) a.e. (2)\nIndeed |∇log r|=2/√r and ||∇²log r||op=2/r. Thus every finite annulus, including accumulating free boundaries, has quantitative C^{1,1} control. The exactly zero left end, smooth right end and finite coordinate cover of the remaining annulus prove global C^{1,1} of the retained residual. This proves extension through the pole, not only complement regularity. E_F itself remains unbounded and is not asserted globally Hölder.\n\nProof of F. Set δ=||F−G||∞. The largest-convex-minorant operator is monotone and commutes with addition of constants. From A+F≤A+G+δ and the reverse inequality, |C_F−C_G|≤δ on R. Subtracting A and taking the continuous canonical end extensions gives\nsup_(P^k)|R_F−R_G|≤||F−G||∞.\nBoth residuals vanish at the pole. This is only C⁰ stability; no derivative stability is inferred.\n\nArtifacts: /workspace/research/native-workers/codex-7EljrU",
      "support": [
        "n1",
        "n2",
        "n3"
      ]
    },
    {
      "id": "n5",
      "summary": "E proved: actual non-pluripolar mass is one, annular masses are the stated slope differences, and deep negative bumps force an open affine zero-density tail.",
      "detailedSummary": "Derives the determinant density with the exact D normalization and identifies it with bounded Bedford–Taylor products. Lipschitz C′ eliminates sphere atoms. Truncation discards the genuine pole, while infinity contributes no singular mass. Affine gaps have rank k−1 for positive slope. The bump inequality forces an attained negative L and a strict free right tail.",
      "text": "Proof of E for the actual measure. On a finite annulus the local total κ-potential is C(log r), of class C^{1,1}. Let dλ_2k denote Euclidean volume. The eigenvalues calculated in n2 and ordinary wedge normalization give a.e.\n(κ+DE_F)^k=(k!/π^k)(C′)^(k−1)C″r^(−k)dλ_2k. (3)\nThere is no extra factor two: (i/(2π))dz∧dbar z=(1/π)dx∧dy.\n\nTo identify this with the bounded-potential product, convolve the local psh potential on a slightly larger annulus with radial Euclidean smoothing kernels. These smooth psh potentials decrease to the canonical potential, have uniformly bounded Hessians on smaller annuli, and their Hessians converge at almost every Lebesgue point. Dominated convergence identifies their determinant limit with (3), while Bedford–Taylor continuity identifies it with the local product. This proves absolute continuity and excludes hidden free-boundary contributions.\n\nWith normalized sphere measure dν,\ndλ_2k=[π^k/(k−1)!]r^(k−1)dr dν.\nThe pushforward under x=log r is therefore\nk(C′)^(k−1)C″dx=d((C′)^k).\nSince C′ is Lipschitz, (C′)^k is absolutely continuous. Thus for every finite a<b,\nMA_κ(E_F)({a<log r<b})=C′(b)^k−C′(a)^k, (4)\nand every sphere {log r=a} has zero mass.\n\nGlobally use bounded κ-psh truncations E_j=max(E_F,−j), restrict their products to {E_F>−j}, and take the non-pluripolar limit. On each annulus this agrees with (3); it assigns zero mass to the actual pole. Near infinity E_F is smooth, so its product is a smooth top form and gives the infinity hyperplane zero mass. Taking a→−∞ and b→+∞ in (4) yields total mass 1^k−0^k=1. This proves finiteness and excludes extra end contributions. Applying the same smooth radial calculation to a′=p independently verifies ∫κ^k=1.\n\nOn a free interval C=sx+d, so C″=0 and the top density vanishes. The smooth total Hessian is sDlog r and has rank k−1 when s>0. In fact n3 proves positive slope for every finite gap. This smoothness concerns the open free interval; it does not assert a smooth Hessian at its endpoints.\n\nFor F=−Mχ with χ≥0 smooth compactly supported, χ(x0)=1 and M>A(x0)−x0, one has f(x0)−x0<0. Hence L<0 and is attained at some finite y. By n3, C=x+L for x≥y. Beyond y and supp χ, f=A and A−x>0>L, so C<f strictly on a nonempty open right tail. Its density is identically zero and its Hessian rank is k−1. Near infinity the total local potential log S+L proves the same rank statement across the hyperplane. The residual is smooth there and C^{1,1} at finite free boundaries.\n\nThese are masses of the actual representative. They are not identified with infimum or supremum over an entire ordinary type, particularly in the nonclosed product setting.\n\nArtifacts: /workspace/research/native-workers/codex-7EljrU",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4"
      ]
    },
    {
      "id": "n6",
      "summary": "G proved for every compact positive Hermitian Y and all genuine nonclosed competitors, with exact canonical slices, finite tensor-product measure and stretching witnesses.",
      "detailedSummary": "Adding a vertical quadratic makes each local total potential psh and gives the exact κ-psh slice bound without horizontal error. Every slice is genuine or identically −∞, so every competitor lies below the pullback envelope. Bounded pullback truncations prove the binomial product formula and finiteness without BMP. Direct witnesses establish the supplied unrestricted E_env definition.",
      "text": "Proof of G. Let Y be any connected compact complex m-fold with smooth positive Hermitian form h0. Write X=P^k×Y, π:X→P^k, H=π*κ+pr_Y*h0, N=k+m and V0=∫_Y h0^m. Closedness is not assumed. H is positive and hence big in the exact definition: ρ=0, h=H and ε=1. Define E_F^H using the identical ordinary full obstacle over all genuine H-psh potentials.\n\nExact canonical restriction. For any genuine H-psh v, work on a product coordinate box Uz×Uy. Choose a smooth local κ-potential b(z) and c>0 such that h0≤cD|w|² on Uy. Then\nD[v+b(z)+c|w|²]≥cD|w|²−h0≥0.\nIts genuine representative is psh. Restricting to w=w0 retains the actual values and is psh or identically −∞. The quadratic becomes constant on the slice, yielding exactly κ+D_z v(·,w0)≥0. There is no extra κ multiple or error term and no need for h0 to be closed.\n\nThe local restrictions glue. A slice nontrivial on one box cannot be identically −∞ on an overlapping open box, because a nontrivial psh function is locally integrable and cannot equal −∞ on an open set. Connectedness propagates this across P^k. Thus every slice is globally genuine κ-psh or identically −∞.\n\nFor every obstacle competitor, each genuine slice satisfies the full obstacle everywhere and the ordinary upper order. By n4 it lies below E_F everywhere; identically −∞ slices do also. Therefore every competitor v≤π*E_F. Conversely π*E_F is a genuine admissible H-psh potential since\nH+Dπ*E_F=π*(κ+DE_F)+pr_Y*h0≥0.\nThus E_F^H=π*E_F with its canonical values. No symmetry of Y or reduction of the competitor family is used.\n\nActual extended measure. Away from {0}×Y, bounded local products and ordinary wedge expansion give only the term with k horizontal and m vertical factors:\nMA_ext_H(π*E_F)=binom(N,k)MA_κ(E_F)⊗h0^m. (5)\nTo justify the global finite measure without BMP, take u_j=π*max(E_F,−j), bounded H-psh. Their bounded smooth-background-corrected products satisfy\n(H+Du_j)^N=binom(N,k)(κ+Dmax(E_F,−j))^k⊗h0^m.\nThis follows by local smooth horizontal approximation, wedge expansion, dimensional vanishing of the other terms, and bounded Bedford–Taylor continuity. The vertical factor is smooth; closedness is unnecessary. Restrict to {E_F>−j}×Y and take the non-pluripolar limit. The finite base limit in n5 yields precisely (5), with no mass on {0}×Y. Therefore\n∫_X MA_ext_H(E_F^H)=binom(N,k)V0.\nThis constructs the particular product directly; it invokes no global theorem requiring unverified BMP and asserts no type-volume equality.\n\nIts retained residual is π*R_F, globally C^{1,1}, with the horizontal annular estimates (2), zero vertical derivatives, exact zero near {0}×Y and smooth extension near infinity times Y. The C⁰ stability estimate also pulls back. On free annuli the total Hessian rank is k−1+m=N−1 and the smooth top density vanishes.\n\nFor the exact E_env definition, E_F^H≼ψ and E_F^H≥ψ−mF. At t=1 choose a=E_F^H. For t>1 choose the genuine H-psh potential a_t=ψ−tmF. Then\nt^(−1)a_t+(1−t^(−1))ψ=ψ−mF≤E_F^H.\nAt the pole both coefficients are positive, so the value is −∞. Handling t=1 separately avoids 0·(−∞). These witnesses establish the stretching class directly; envelope equality was not substituted for its definition.\n\nArtifacts: /workspace/research/native-workers/codex-7EljrU",
      "support": [
        "n1",
        "n4",
        "n5"
      ]
    },
    {
      "id": "n7",
      "summary": "H proved directly: the specified Hopf metric is positive, descends and is nonclosed; P² times this Hopf surface is a compact non-Kähler fourfold.",
      "detailedSummary": "Computes h0=iΣdζj∧dbarζj/(2π|ζ|²) and its nonzero derivative. The descended rank-one semipositive exact form Ds contradicts existence of a Kähler metric by Stokes. The fixed normalization gives V0=4 and actual fourfold envelope mass 24. No lower-mass property is claimed.",
      "text": "Proof of H with exact constants. On C²\\{0}, let rY=|ζ1|²+|ζ2|² and s=log rY. Direct differentiation gives\nDs=(i/(2π))Σ[δjl/rY−barζjζl/rY²]dζj∧dbarζl,\nds∧d^cs=(i/(2π))Σ[barζjζl/rY²]dζj∧dbarζl.\nThe second identity follows by expanding the specified d^c. Therefore\nh0=Ds+ds∧d^cs=(i/(2πrY))Σ_(j=1)^2 dζj∧dbarζj.\nIt is smooth positive definite: Ds has rank one perpendicular to ζ and the second term fills the radial direction.\n\nThe deck map ζ↦eζ sends rY↦e²rY and s↦s+2. Hence ds,d^cs,Ds and h0 are invariant and descend. The action is free and properly discontinuous. Writing ζ=Rω identifies log R modulo one, so the quotient is diffeomorphic to S³×(R/Z), connected, compact and smooth, with its inherited complex surface structure.\n\nFor the closed form β=(i/(2π))Σdζj∧dbarζj, h0=rY^(−1)β. Thus\ndh0=−ds∧h0=−ds∧Ds≠0.\nAt ζ=(R,0), R>0, ds=(2/R)dx1 and Ds=(1/(πR²))dx2∧dy2, so dh0=−2/(πR³)dx1∧dx2∧dy2. This proves actual nonclosedness after descent.\n\nThe one-form d^cs descends, making Ds=d(d^cs) globally exact on Y. It is semipositive of rank one everywhere. If Ω were Kähler, Ds∧Ω would be a strictly positive volume form, whereas Stokes gives\n∫_Y Ds∧Ω=∫_Y d(d^cs∧Ω)=0.\nThis contradiction proves Y non-Kähler without a classification theorem. A Kähler form on P²×Y would restrict to a Kähler form on a slice Y, so the product is also non-Kähler. It is a connected compact complex fourfold. H=κ+h0 is positive and nonclosed because its derivative restricts to dh0 on that slice.\n\nThe exact normalization permits a further check. With dλ4 on the cover,\nh0²=2/(π²R⁴)dλ4.\nA radial fundamental domain is 1≤R<e and area(S³)=2π². Hence\nV0=(2/π²)(2π²)∫_1^e dR/R=4.\nBy n6, with k=m=2 the actual envelope mass is binom(4,2)·4=24. This is a representative mass computation; no zero-lower-mass property, general BMP conclusion or acceptance flag is asserted.\n\nArtifacts: /workspace/research/native-workers/codex-7EljrU",
      "support": [
        "n6"
      ]
    },
    {
      "id": "n8",
      "summary": "A–H reconstructed as a limited singular ordinary-envelope theorem with quantitative residual regularity and C⁰ stability; unrestricted S06 remains unresolved.",
      "detailedSummary": "Audits genuine poles, all competitors, ordinary type, canonical residual ends, stretching witnesses and actual masses. Shows the reference has trivial multiplier ideals but is unbounded, ordinarily nonminimal and not a model. K=X has uniform capacity density, so the distinction from Ahn is the singular weight and retained residual. Records reproducible sampled diagnostics and their limitations. No priority or unrestricted completion is claimed.",
      "text": "Hypothesis and scope audit. Notes n2–n7 establish A–H for exactly k≥2, 0<α<1, the standard normalized κ, every real F∈C²_c(R), genuine canonical potentials and the full ordinary global obstacle. G includes every connected compact positive Hermitian Y without closedness or symmetry. H supplies the concrete nonclosed non-Kähler fourfold. The residual extension is forced by the end contact and is not arithmetic subtraction of pole values. The free-boundary argument covers arbitrary and accumulating components. Compact radial C² perturbations and the projective residual geometry are decisive sufficient hypotheses.\n\nThe ordinary prescribed type is nonvacuous. Since ψ is unbounded, it is not ordinarily equivalent to the bounded minimal potential zero. Distinct exponents give distinct types: for 0<α<β<1, ψ_β−ψ_α=−T^β+T^α→−∞, so ψ_α≼ψ_β fails. These types have zero logarithmic coefficient but are unbounded; an analytic logarithmic singularity with zero coefficient is locally bounded. Thus they are not resolved logarithmic types.\n\nUnder the exact exp(−tψ) convention, all multiplier ideals are nevertheless trivial. For fixed t>0 and ε>0, sublogarithmic growth gives exp(−tψ)≤Cεr^(−ε) near zero. Choosing ε<k proves integrability against r^(k−1)dr. Holomorphic germs are bounded on smaller balls, so I(tψ)=O for every real t>0. The same proof applies on the product by integration in z. Ordinary equivalence preserves these ideals while retaining the unbounded type.\n\nThe reference is not an ordinary model. For 0<ε≤1, εlog p is κ-psh because κ+Dlog p=Dlog r≥0 with its genuine extension. Let vε=max(ψ,εlog p). Both branches are ≤0, and εlog p−ψ tends to −∞ at the pole and is bounded above globally. Hence vε≃ψ and is an ordinary zero-obstacle competitor. At every point off zero, vε→0 as ε↓0. After usc regularization, P_κ[ψ]=0, including at zero, rather than ψ. Also P_κ[ψ]_I=0 because zero is ideal-equivalent to ψ and is itself a competitor. Pulled-back competitors give the same conclusion on the positive product background. This explains why the declared singular obstacle preserves the pole without a model assumption or ideal condition.\n\nWhat is answered about density zeros. For this retained ordinary reference and every compact radial C² perturbation, the actual envelope has a globally C^{1,1} residual with the explicit annular estimates (2), exact smooth extension through the pole and smooth extension at infinity. Deep negative bumps produce an open zero-density region with total Hessian rank k−1, or N−1 on the product, and smooth residual there. Residual C^{1,1} control persists through all finite free boundaries; smooth Hessian extension across those boundaries is not claimed. The proof uses convex tangency and end contact, rather than determinant vanishing order or local density smoothness. The constructed density is the envelope’s actual measure, not a theorem for arbitrary independently prescribed right-hand sides.\n\nThis reference also lies outside bounded minimal L^p regularity at its pole. From n2 and (3),\ndMA_κ(ψ)/dλ_2k ∼ [k!α^k(1−α)/π^k]r^(−k)(1−log r)^(kα−k−1).\nThis is integrable but not in L^p for any p>1: in x=log r coordinates the p-th power integral contains exp(−k(p−1)x) as x→−∞, multiplied by a logarithmic power. Any smooth positive probability dV is comparable to coordinate volume near zero, so the same conclusion holds relative to dV and locally on the product. Pole-subtracted regularity therefore does not assert boundedness or regularity of the singular potential itself.\n\nLiterature overlap. Here K is the entire manifold and has uniform density in capacity. The constant test potential zero gives Cap_H(B)≥∫_B H^N≥cr^(2N) on small coordinate balls in a finite atlas. Intersecting with K changes nothing; the base argument uses κ. This is not a capacity-density-failure example. The Ahn results in n1 require finite continuous or Hölder weights, while ψ+F has an actual −∞ pole. The proved conclusion concerns a retained ordinary nonlogarithmic type and its quantified residual. Thus it addresses a singular-weight case beyond that finite-weight hypothesis, without a priority claim. It does not transfer to the different ideal-ordered, quasi-everywhere weighted operator in the original question, to arbitrary compact K, or to arbitrary singular weights.\n\nActual masses have not been relabeled as lower or upper singularity volumes. Those require infimum and supremum over all representatives of the fixed ordinary type and remain separate questions here. BMP and positive lower mass are not conflated. The nonclosed proof uses exact canonical slices and the particular finite product truncations, not closed minimal-type uniqueness or a global extension theorem with an unverified hypothesis. E_env membership uses explicit stretching witnesses, not envelope equality as its definition.\n\nReproducibility and evidence. All files are in /workspace/research/native-workers/codex-7EljrU. input.json contains the supplied statement. Run python compose_notes.py to generate notes.json and proof_notes.txt, and python audit_notes.py > artifacts/audit_output.log to audit artifact integrity and the acyclic earlier-note support graph. The audit passed; it does not verify mathematics. Primary retrieval commands, saved passages and failed shell downloads are described in n1.\n\nRun python verify.py > artifacts/check_output.log for the lightweight diagnostic, using artifacts/check_input.json and producing artifacts/check_output.json. It sampled α=0.6, k=2 and x∈[−80,30] in steps of 0.005, with χ(x)=exp(1−1/(1−x²)) for |x|<1 and zero elsewhere, F=−2χ and G=−2.2χ. Observed A′ ranged from 0.1034563715943573 to 0.9999999999999626; A″ ranged from 3.7392311469375974e−14 to 0.16374798449945155, below the proved bound 0.49. Sampled A(0)=0.3215808133201703 and L_F≈−1.6863431732015037 at x≈0.06. The sampled residual and weight differences were both 0.20000000000000018. These are finite-grid observations with an artificial left endpoint and approximate contacts, not exhaustive results or proofs for general F. Slope discrepancies around 10^−12 are floating-point errors. Hopf mass four and fourfold mass 24 are proved in n7; the program only records their formulas.\n\nartifacts/environment.json records Python 3.12.14, Linux x86_64, the inspected network policy and unavailable facilities. No operator-provided supervised compute service or cloud environment_status tool was exposed, and no resource-heavy computation was attempted. The requested native model configuration was not overridden; no subagents were spawned. There is no independent runtime-model introspection evidence. Commands are retained in artifacts/commands.txt.\n\nThe concrete A–H reconstruction is fulfilled as an unverified draft theorem. Arbitrary prescribed ordinary or relative equation types, independently prescribed degenerate densities, general singular or ideal weighted extremals and unrestricted original S06 remain unresolved. No complete solution of that unrestricted task is claimed; candidate=false.\n\nArtifacts: /workspace/research/native-workers/codex-7EljrU",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "n6",
        "n7"
      ]
    }
  ],
  "candidate": false,
  "workspace": "/workspace/research/native-workers/codex-7EljrU"
}


## Entire component: notes/S06-singular-weighted-final-current-known-overlap-20261007.md

# Current scope for the limited S06 final comparison

This is evidence and a scope assessment, not an acceptance verdict. The original
S06 task, its full-review INCONCLUSIVE, and the A--H statement-only candidate=false
remain unchanged. Any eventual checked release concerns the explicitly declared
ordinary everywhere singular-obstacle envelope only. Arbitrary prescribed
equations, ideal weighted envelopes and general compact obstacle sets stay open.

The entire current 323-line author section_radial_residual_regularity.tex was
actually root-read, including its whole density criterion, sharpness examples,
flat-error theorem, zero-density annulus, and nonclosed zero-lower-mass product.
It already fixes the same sublogarithmic projective ordinary reference, exact
radial flux normalization, non-Lp density, prescribed density inverse, residual
derivative thresholds and canonical crossing of the pole. These reference and
measure mechanisms receive their existing credit. Source includes and named
dependencies do not constitute a claim of a new whole-book read.

The current proposed weighted construction takes a singular weight psi+F,
uses the ENTIRE ordinary obstacle competitor family, and obtains its envelope
and free set from the full convex minorant. The density is then its actual
measure, rather than independently prescribed density data. Every compact C2
radial perturbation is covered, with canonical residual regularity, zero free
density, actual tensor product measures, and all nonclosed product competitors.
The newly declared I concerns uniform residual Hessian bounds over fixed-support
bounded-C2 obstacle families and quantitative derivative stability through
moving infinity contact; it requires its own independent reconstruction and
must not be inferred merely from the earlier finite-annulus bound.

The original explicit article used a convolution slicing proof. Its supplemental
proof and the independent n6 give the exact closed-horizontal and vertical
quadratic proof for every actual canonical slice, including identically minus
infinity. Both routes must be assessed with the smooth nonclosed background
unchanged. The particular finite tensor measure uses bounded-level products
and strict superlevels, without a general BMP-dependent unbounded theorem.

Ahn's quoted continuity and Holder results concern finite real weights. Their
capacity hypothesis is satisfied for K=X here. Thus the relevant distinction
is the genuine singular weight and retained residual, not a failure of capacity
density or a new ideal-order conclusion. The independent A--H cold run retrieved
the continuity v2 statement; the current article cites v3, whose exact theorem
and full printed application were separately read by the root. No assertion
that all editions or all cited foundational dependencies were recursively
certified is made. No literature-priority claim is asserted.

The later source wording calls R a smooth projective function. The explicit
stretching proof now treats t=1 separately and uses the old witness for t>1,
as done in the independent n6. These are harmless clarifications. By contrast,
I is a substantive added theorem and must be reviewed as a new statement.


## Entire component: checks/S06-singular-weighted-A-I-final-primary-applications-20261007.pending.json

{
  "recorded_at_utc": "2026-10-07T21:28:16.695993+00:00",
  "purpose": "Additional exact primary application and direct proof boundary for S06 final A-I comparison",
  "current_article_sha256": "2d83712903095ee765f732b697598695513e69ab36bb9ddf3cc5f9631d1b039a",
  "whole_current_article_actually_root_read": true,
  "earlier_exact_primary_application_records": [
    "checks/S06-singular-radial-weighted-envelope-current-primary-applications-20261007.pending.json",
    "checks/S06-singular-weighted-exact-slicing-inclusive-preparation-20261007.pending.json"
  ],
  "additional_exact_primary_applications": [
    {
      "pdf": "inputs/primary/Demailly-agbook-Harvard.pdf",
      "pdf_sha256": "d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1",
      "text_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
      "whole_actual_source_text_read_ranges": [
        [
          17245,
          17352
        ],
        [
          17350,
          17428
        ]
      ],
      "statement": "Compact Kahler odd Betti numbers are even; whole printed Hodge decomposition, its metric-independence lemma and the 8.12 consequence read.",
      "application": "The actual Hopf surface is S3 times S1 and has b1=1, excluding a Kahler metric; the product slice gives the fourfold obstruction. Cold n7 separately supplies the full exact semipositive-form Stokes obstruction without importing Hodge theory.",
      "recursive_verification_of_Hodge_and_elliptic_foundations": false
    }
  ],
  "I_new_external_regularity_theorem_imported": false,
  "I_author_proof": "Explicit derivative contact-set comparison, projective-coordinate chain rule, continuous gradient crossing and finite-difference interpolation are supplied; independent reconstruction pending. No undefined rough linearized operator is used.",
  "cold_Demailly_author_host_and_root_Harvard_host_distinguished": true,
  "cold_Ahn_continuity_v2_and_current_article_v3_distinguished": true,
  "general_BMP_dependent_unbounded_product_not_used": true,
  "all_type_volumes_kept_distinct_from_actual_representative_mass": true,
  "mathematical_acceptance": false,
  "original_S06_completed": false,
  "published": false
}


## Entire current known manuscript radial section, credited background

\section{Residual regularity in radial singularity types}
\label{sec:radial-residual-regularity}

Subtracting a prescribed singularity separates regularity of the residual from the pole of the solution. On projective space, central radial mass gives an exact inverse for the equation. A relative density error then controls the residual through two derivatives, even when the density is merely integrable at the pole. The inverse also permits smooth crossing of density zeros away from it. The pole is the one used in \cref{lem:projective-sublogarithmic-density}; here its ordinary type is fixed while the density varies.

\subsection{The prescribed ordinary type}
Let $k\geq2$, let $\kappa$ be the Fubini--Study form on $\mathbb P^k$ with $\int\kappa^k=1$, and put $o=[1:0:\cdots:0]$. On the chart $Z_0\ne0$ write $z_i=Z_i/Z_0$ and set
\[
 r=\sum_{j=1}^k|z_j|^2,\qquad P=\frac r{1+r},\qquad
 T=1-\log P,
 \qquad u_\alpha=1-T^\alpha\quad(0<\alpha<1).
\]
The ratio $P=\sum_{i=1}^k|Z_i|^2/\sum_{i=0}^k|Z_i|^2$ is global. Give $u_\alpha$ its canonical value $-\infty$ at $o$ and value zero on the hyperplane $Z_0=0$. Primes denote differentiation in $r$, and $b_\alpha=k(1-\alpha)>0$ throughout this section.

\Needspace{12\baselineskip}
\begin{lemma}\label{lem:radial-nonlogarithmic-type}\index{Singularity type!radial nonlogarithmic pole}
The canonical $u_\alpha$ is $\kappa$-plurisubharmonic and smooth off $o$. Its non-pluripolar measure has a positive density $q_\alpha$ of mass one, in $L^1$ and in no $L^p$, $p>1$. Distinct $\alpha$ give distinct ordinary types, although all their multiplier ideals are trivial.
\end{lemma}
\begin{proof}
Plurisubharmonicity, smoothness off the pole, unit mass and the $L^p$ assertions are those of \cref{lem:projective-sublogarithmic-density}. To fix the profile used in the inverse below, put
\begin{equation}\label{eq:radial-residual-baseline}
 \Phi_\alpha=\log(1+r)+u_\alpha,\qquad
 Q_\alpha=r\Phi_\alpha'=P+\alpha(1-P)T^{\alpha-1}.
\end{equation}
The tangential and radial eigenvalues are $Q_\alpha/r$ and $Q_\alpha'$, both positive. Radial determinant integration, with the constant fixed by $\Phi=\log(1+r)$, gives
\begin{equation}\label{eq:radial-residual-flux}
 \int_{a<|z|^2<b}(\ddc\Phi)^k=Q(b)^k-Q(a)^k,
 \qquad Q=r\Phi'.
\end{equation}
Since $Q_\alpha(0)=0$ and $Q_\alpha(\infty)=1$, the density is
\begin{equation}\label{eq:radial-residual-baseline-density}
 q_\alpha=\frac{(Q_\alpha^k)'}{(P^k)'}>0.
\end{equation}
Smoothness on the hyperplane and the exclusion of the canonical
pole in the product leave no further measure. Near $r=0$, with
$L=1-\log r$, direct differentiation gives
\begin{align}\label{eq:radial-residual-asymptotics}
 Q_\alpha&\sim\alpha L^{\alpha-1},&
 Q_\alpha'&\sim\frac{\alpha(1-\alpha)}rL^{\alpha-2},\\
 (Q_\alpha^k)'&\sim
 \frac{k\alpha^k(1-\alpha)}rL^{-1-k(1-\alpha)}.\nonumber
\end{align}
In particular $q_\alpha\sim\alpha^k(1-\alpha)r^{-k}L^{-1-b_\alpha}$; the radial volume has order $r^{k-1}\,\mathrm{d}r$, recovering these integrability assertions.

The types for different $\alpha$ are ordinarily distinct, since
their difference is unbounded at $o$. Yet every $\mathcal I(tu_\alpha)$
is trivial for finite $t>0$: integrability of the constant function
reduces near $o$ to
$\int^\infty \mathrm{e}^{-kL+tL^\alpha}\,\mathrm{d}L<\infty$.
Ordinary type information here is strictly finer than this ideal
information.
\end{proof}

\Needspace{14\baselineskip}
\subsection{Density criterion and exact inverse}
Here ``radial'' means depending only on $r$ in the displayed chart.
The smoothness assumption along the hyperplane includes a smooth profile in $t=1/r$ near $t=0$.

\begin{theorem}\label{thm:radial-residual-regularity}\index{Regularity!radial singular residual}
Let $q\ge0$ be radial, smooth on $\mathbb P^k\setminus\{o\}$, including
the hyperplane at infinity, and satisfy $\int q\kappa^k=1$.
Suppose that for some $\delta,A,r_0>0$,
\begin{equation}\label{eq:radial-residual-density-error}
 \left|\frac{q(r)}{q_\alpha(r)}-1\right|\le Ar^\delta
 \quad(0<r<r_0).
\end{equation}
Then there is a genuine radial $\kappa$-psh potential $U$, normalized
to have value zero on the hyperplane, with
\[
 \mathrm{MA}_\kappa(U)=q\kappa^k,
 \qquad U\sim u_\alpha.
\]
Its residual $R=U-u_\alpha$ off $o$ extends continuously
across $o$, with value $R_0$, and for small $r$ satisfies
\begin{equation}\label{eq:radial-residual-estimates}
 \begin{aligned}
 |R-R_0|&\le Cr^\delta L^{\alpha-2},\\
 |R'|&\le Cr^{\delta-1}L^{\alpha-2},\qquad
 |R''|\le Cr^{\delta-2}L^{\alpha-2}.
 \end{aligned}
\end{equation}
It is locally $C^{0,\min\{1,2\delta\}}$.
For $\delta\ge\frac12$ it extends $C^1$ with zero gradient at $o$;
for $\delta\ge1$ it extends $C^2$ with zero Hessian at $o$.
No derivative hypothesis on the error in \eqref{eq:radial-residual-density-error} is needed
for these conclusions.
The potential and its residual are smooth on $\mathbb P^k\setminus\{o\}$,
including every density zero there. The tail condition ensures positive
cumulative central mass; local density smoothness alone is not the criterion.
\end{theorem}

\begin{proof}
Let
\begin{equation}\label{eq:radial-residual-inverse}
 \begin{aligned}
 M(r)&=\int_{|z|^2<r}q\kappa^k,& Q(r)&=M(r)^{1/k},\\
 U'(r)&=\frac{Q(r)-P(r)}r,& U(\infty)&=0.
 \end{aligned}
\end{equation}
The tail condition makes $q$ positive near $o$, so $M(r)>0$ for every
$r>0$. One has $M'=q(P^k)'\ge0$, $Q'\ge0$ and $M(\infty)=1$.
Thus the positive root defining $Q$ is smooth for every finite $r>0$,
even where $q$ vanishes. This proves smoothness across all finite density
zeros without a vanishing-order assumption.
In $t=1/r$, the tail $1-M$ is the integral from $0$ to $t$ of the smooth density profile times $-\mathrm{d}(1+t)^{-k}/\mathrm{d}t$. Thus $M$ and $Q$ are smooth there, with $Q(0)=1$ in that coordinate. The equation
$\mathrm{d}U/\mathrm{d}t=-(Q-P)/t$ is smooth there, since $Q-P$ vanishes at
$t=0$. This both defines the normalization and proves smoothness
along the full hyperplane.

From \eqref{eq:radial-residual-density-error} and
\eqref{eq:radial-residual-asymptotics},
\begin{equation}\label{eq:radial-residual-tail}
 |M-Q_\alpha^k|
 \le C\int_0^r s^{\delta-1}(1-\log s)^{-1-b_\alpha}\,\mathrm{d}s
 \le Cr^\delta L^{-1-b_\alpha}.
\end{equation}
The last inequality follows by writing $s=r\mathrm{e}^{-y}$ and bounding
$\int_0^\infty \mathrm{e}^{-\delta y}(L+y)^{-1-b_\alpha}\,\mathrm{d}y$.
Dividing by $Q_\alpha^k\asymp L^{-b_\alpha}$ shows that $Q/Q_\alpha$
tends to one; the mean value theorem for the positive $k$th root
then gives
\begin{equation}\label{eq:radial-residual-flux-error}
 |Q-Q_\alpha|\le Cr^\delta L^{\alpha-2}.
\end{equation}
Moreover the exact identity
\[
 \frac{Q'}{Q_\alpha'}=
 \frac q{q_\alpha}\left(\frac{Q_\alpha}{Q}\right)^{k-1}
\]
gives $|Q'-Q_\alpha'|\le Cr^{\delta-1}L^{\alpha-2}$.
Since $R'=(Q-Q_\alpha)/r$, integration to the origin gives a finite
$R_0$ and the first two inequalities in \eqref{eq:radial-residual-estimates}.
Differentiating this formula gives the last inequality.

The local potential $\Phi=\log(1+r)+U$ has semipositive
Hessian away from $o$ because $Q/r>0$ and $Q'\ge0$. Also
$U=u_\alpha+R_0+o(1)$ near $o$, so $\Phi$ tends to $-\infty$.
The local profile has nonnegative increasing slope in $\log r$, so its maxima with its value at $r=\varepsilon$ are plurisubharmonic. They decrease to the locally integrable profile; the local decreasing-limit property gives its genuine plurisubharmonic extension with the canonical pole retained. Thus $U$ is globally
$\kappa$-psh. Formula~\eqref{eq:radial-residual-flux} or the local determinant
ratio gives its measure $q\kappa^k$ away from $o$; the defining
non-pluripolar truncations exclude $o$ and are locally identical
to this smooth product elsewhere. The measure has exactly total
mass one. The bounded global residual proves the ordinary type.

In real coordinates, with $\rho=|z|=\sqrt r$,
\[
 |\nabla R|\le C\rho^{2\delta-1}L^{\alpha-2},
 \qquad |\nabla^2R|\le C\rho^{2\delta-2}L^{\alpha-2}.
\]
For $2\delta<1$, integration along radial radii bounds differences
by $C|\rho_1-\rho_2|^{2\delta}$ and hence by
$C|z_1-z_2|^{2\delta}$. For $2\delta\ge1$ the gradient is bounded,
giving local Lipschitz regularity. At $\delta=\frac12$ its bound
tends to zero and $R-R_0=o(\rho)$, which give the claimed $C^1$
extension. At $\delta=1$, the Hessian bound tends to zero and
$\nabla R=o(\rho)$, giving the $C^2$ extension. Larger $\delta$
only improves these bounds. These arguments justify crossing the
pole for $R$; they do not assign a finite value to $U(o)$.
\end{proof}

Among radial genuine solutions smooth off $o$
with this density, no central flux and no hyperplane singularity,
the potential is unique up to constants: its flux satisfies
$Q^k=M$, and \eqref{eq:radial-residual-inverse} then fixes its derivative.
No nonsymmetric uniqueness is asserted.

Relative envelope-class membership follows from an explicit stretching family. If
$a_* =\inf R$, the genuine $\kappa$-psh functions
$v_t=u_\alpha+t a_*$ satisfy, for every $t\ge1$,
\[
 t^{-1}v_t+(1-t^{-1})u_\alpha=u_\alpha+a_*\le U.
\]
At $t=1$ the term with zero coefficient is omitted, as in \cref{def:relative-envelope-class}. Hence
$U\in \mathcal E_{\mathrm{env}}(\mathbb P^k,\kappa,u_\alpha)$ in the
stretching definition, canonically at the common pole.

\subsection{Smooth residuals from flat errors}
\begin{proposition}\label{prop:radial-flat-residual}
Under the hypotheses of Theorem~\ref{thm:radial-residual-regularity}, suppose
$g=q/q_\alpha-1$ satisfies
\[
 (r\partial_r)^jg=O(r^N)
 \quad\text{for every }N,j\ge0.
\]
Then $R-R_0$ extends smoothly across $o$, with every derivative
zero there.
\end{proposition}
\begin{proof}
Put $x=-\log r$, $a(x)=Q_\alpha(\mathrm{e}^{-x})^k$ and
$E(x)=M(\mathrm{e}^{-x})-a(x)$. The exact central integral is
\[
 E(x)=\int_x^\infty g(\mathrm{e}^{-y})[-a'(y)]\,\mathrm{d}y,
 \qquad E'(x)=g(\mathrm{e}^{-x})a'(x).
\]
Every derivative of $a$ has at most polynomial growth in $1+x$,
and $a\asymp(1+x)^{-b_\alpha}$. The integral bounds $E$ by an
exponential of arbitrarily large rate. Repeated differentiation of
$E'$ expresses each derivative as a finite Leibniz sum of flat
derivatives of $g$ and polynomially bounded derivatives of $a$;
all derivatives of $E$ are therefore exponentially flat.
Every derivative of $1/a$ has at most polynomial growth, by
\eqref{eq:radial-residual-baseline}. Thus $E/a$ has the same flatness. Applying
smooth composition near one to
\[
 Q-Q_\alpha=Q_\alpha\bigl[(1+E/a)^{1/k}-1\bigr]
\]
proves flatness of every $x$ derivative of $Q-Q_\alpha$.
Since $\mathrm{d}R/\mathrm{d}x=-(Q-Q_\alpha)$, integration from $x$ to infinity
proves the same for $R-R_0$, including its zeroth derivative.
An ordinary $j$th derivative in $r$ is $r^{-j}$ times a polynomial
in $\partial_x$; arbitrarily strong exponential decay absorbs that
factor. All ordinary derivatives extend continuously as zero at
$r=0$, and repeated one-dimensional integration verifies smoothness
there. Composition with $r=|z|^2$ gives the conclusion.
\end{proof}

\Needspace{19\baselineskip}
\subsection{Compact examples and sharp derivative thresholds}
\begin{proposition}\label{prop:radial-residual-sharpness}
The $C^1$ threshold $\delta=1/2$ and $C^2$ threshold $\delta=1$ are sharp. When $2\delta<1$, the stated H\"older exponent is also sharp. Nontrivial probability-density perturbations with smoothly flat residuals exist.
\end{proposition}
\begin{proof}
Choose smooth nonnegative radial cutoffs $\chi_0,\chi_1$ with
disjoint supports: $\chi_0=1$ near $r=0$ and vanishes outside a
finite small ball; $\chi_1$ is nonzero in a finite annulus. Put
\begin{equation}\label{eq:radial-residual-sharp-examples}
 B=\frac{\int r^\delta\chi_0q_\alpha\kappa^k}
          {\int\chi_1q_\alpha\kappa^k},\qquad
 q_c=q_\alpha\bigl[1+c(r^\delta\chi_0-B\chi_1)\bigr].
\end{equation}
For sufficiently small $c>0$, $q_c$ is positive, smooth off $o$
and along the hyperplane, and has total mass exactly one. It is
comparable to $q_\alpha$ near $o$, hence is in no $L^p$, $p>1$.
Theorem~\ref{thm:radial-residual-regularity} gives a compact solution in
the prescribed ordinary type. Near $o$ its central flux difference is
exactly $c\int_0^r s^\delta(Q_\alpha^k)'\,\mathrm{d}s$.
The substitution $s=r\mathrm{e}^{-y}$ and dominated convergence give
\[
 \int_0^r s^{\delta-1}(1-\log s)^{-1-b_\alpha}\,\mathrm{d}s
 \sim\delta^{-1}r^\delta L^{-1-b_\alpha}.
\]
Using \eqref{eq:radial-residual-asymptotics} and the $k$th-root expansion yields
\begin{align*}
 R_c'(r)&\sim\frac{c\alpha(1-\alpha)}\delta
                  r^{\delta-1}L^{\alpha-2},\\
 R_c(r)-R_c(0)&\sim\frac{c\alpha(1-\alpha)}{\delta^2}
                  r^\delta L^{\alpha-2}.
\end{align*}
For $\delta<\frac12$, the radial gradient
$2\sqrt r\,R_c'$ diverges, ruling out $C^1$ extension. For
$\delta<1$, a tangential real Hessian eigenvalue $2R_c'$ diverges,
ruling out $C^2$ extension. The annular compensation changes no
central flux. For $2\delta<1$ the displayed asymptotic also rules
out any larger H\"older exponent. The critical derivative thresholds
in Theorem~\ref{thm:radial-residual-regularity} are therefore sharp for this family.

Replacing $r^\delta\chi_0$ in \eqref{eq:radial-residual-sharp-examples} by
$\mathrm{e}^{-1/r}\chi_0$ and adjusting $B$ by the same integral formula
gives a nonzero mass-preserving perturbation satisfying every
flat-error hypothesis. Proposition~\ref{prop:radial-flat-residual} then supplies
a smoothly flat residual across the pole.
\end{proof}

\subsection{Smooth residuals with an open density-zero annulus}
\begin{proposition}\label{prop:radial-zero-annulus}
For every $k\ge2$ and $0<\alpha<1$, there is a nonnegative radial
probability density $q_0$, smooth off $o$ and along the hyperplane,
which equals $q_\alpha$ near $o$ and vanishes on a nonempty open
annulus. Its solution has ordinary type $u_\alpha$ and a
globally smooth residual, constant near $o$.
\end{proposition}
\begin{proof}
Choose a smooth radial $h$ with $0\le h\le1$, equal to zero on
a nonempty finite annulus and equal to one near $o$ and outside
a larger finite annulus. Choose a nonzero nonnegative smooth radial
cutoff $\chi$ supported in a disjoint finite annulus where $h=1$.
Set
\[
 C=\frac{\int(1-h)q_\alpha\kappa^k}{\int\chi q_\alpha\kappa^k}>0,
 \qquad q_0=q_\alpha(h+C\chi).
\]
This is nonnegative and has integral one. It is smooth at every
point off $o$, including the hyperplane, and equals $q_\alpha$
near $o$. It vanishes on the chosen open annulus and is still in
no $L^p$, $p>1$. Theorem~\ref{thm:radial-residual-regularity} applies, with
zero relative density error on a neighborhood of $o$. There the
exact central fluxes agree, so $Q=Q_\alpha$ and $R'=0$.
Hence $R$ is constant near $o$ and extends smoothly across it.
It is smooth everywhere else by the positive-root inverse, including
the entire zero annulus. The solution retains its genuine pole;
this smoothness assertion concerns the residual.
\end{proof}

\subsection{Products with a zero-lower-mass factor}
Let $(X_0,h_0)$ be any connected compact Hermitian $m$-fold with
$v_-(h_0)=0$, and write $V_0=\int_{X_0}h_0^m>0$.
On $X=X_0\times\mathbb P^k$ put $N=m+k$ and
$H=\operatorname{pr}_0^*h_0+\operatorname{pr}_Y^*\kappa$, where $\operatorname{pr}_0$ and $\operatorname{pr}_Y$ are the two projections. In the product formulas below, $U$ and $R$ denote their pullbacks.
\begin{corollary}\label{cor:radial-residual-nonclosed-product}
The pullback of $U$ has the pulled-back ordinary type and relative envelope-class membership. Its residual retains the proved regularity across $X_0\times\{o\}$, and its finite Monge--Amp\`ere mass is $\binom Nm V_0$. The background $H$ is nonclosed and $v_-(H)=0$.
\end{corollary}
\begin{proof}
The pullback of $U$ obeys
\[
 \mathrm{MA}_H(U)=\binom Nm\operatorname{pr}_0^*(h_0^m)
                 \wedge\operatorname{pr}_Y^*(q\kappa^k),
 \qquad \int_X\mathrm{MA}_H(U)=\binom Nm V_0.
\]
Indeed the bounded truncation $\max\{U,-j\}$ is a pullback.
The bounded corrected-product expansion of \cref{prop:bounded-products,lem:bounded-products-submersion} leaves only the displayed
binomial term by dimensions; multiplication by $1_{\{U>-j\}}$
and increasing $j$ give the exact formula and finite mass.
The residual is the pullback of $R$, so its proved regularity
extends across $X_0\times\{o\}$. It is ordinarily equivalent to the
pullback of $u_\alpha$ and belongs to the corresponding relative
stretching class by the same explicit $v_t$.

Also $v_-(H)=0$: bounded $h_0$-psh potentials with masses tending
to zero have pullbacks of mass $\binom Nm$ times those masses.
The background is genuinely nonclosed, since a closed positive
$h_0$ would have all bounded masses equal to $V_0>0$ by Stokes.
The zero-lower-mass conclusion retains the stated factor hypothesis; the calculation does not determine an individual density threshold.
\end{proof}


## Exact retrieved printed primary passages: Ahn-continuity-weighted-extremals-2604.01885v3

Text SHA256: 988af2726ee4f2823abfd206de9337e8833c66423fec3cf63769e997a948ae5b; corresponding PDF SHA256: c6c5ae5b071c7ac21d1ab1d9eab97345f32c921b17425e8c99e6a4fad2e90ec8.


### Actual text lines 1--155

                                                   CHARACTERIZATION OF CONTINUITY OF
                                           SICIAK-ZAHARJUTA EXTREMAL FUNCTIONS ON COMPACT
                                                         HERMITIAN MANIFOLDS


                                                                                  HYUNSOO AHN
arXiv:2604.01885v3 [math.CV] 6 May 2026




                                                   Abstract. For a compact subset in a compact Hermitian manifold, we prove
                                                   that the continuity of the extremal function at a given point in the set is a
                                                   local property and that the continuity of a weighted extremal function follows
                                                   from the continuities of the extremal function and the weight function. These
                                                   results are generalizations of the results of Nguyen [Ng24] on compact Kähler
                                                   manifolds. Moreover, for a compact subset in a compact Hermitian manifold,
                                                   at the point level and accordingly at the global level, we characterize the conti-
                                                   nuity of the extremal function via the local L-regularity, which is equivalent to
                                                   the weak local L-regularity. We also show that the L-regularity of a compact
                                                   subset in Cn at a star center implies the local L-regularity. Consequently, a
                                                   convex compact L-regular subset in Cn is locally L-regular.




                                                                                1. Introduction
                                              Background. The Siciak-Zaharjuta extremal function was historically defined
                                          first using polynomials by Siciak in 1962 and subsequently characterized using
                                          plurisubharmonic functions by Zaharjuta in the 1970s. It is considered as an ex-
                                          tension of one-dimensional Green function with a logarithmic pole at infinity to
                                          higher-dimensional complex spaces using plurisubharmonic (psh for short) func-
                                          tions rather than just subharmonic functions.
                                              For a subset E in Cn , the classical Siciak-Zaharjuta extremal function of E
                                          introduced in [Si62, Si81, Za76] is defined on Cn by
                                                              LE (z) := sup{u(z) : u ∈ L, u|E ≤ 0},             z ∈ Cn ,
                                          where the Lelong class L is
                                          L := {u ∈ P SH(Cn ) : for some constant cu , u(z) ≤ max{0, log ∥z∥} + cu , z ∈ Cn }.
                                          The regularity of the extremal function of a set gives geometric information about
                                          the set itself. For example, E is pluripolar if and only if L∗E ≡ ∞, where ∗ denotes
                                          the upper semicontinuous regularization, and E is non-pluripolar if and only if
                                          L∗E ∈ L.
                                             We recall the notions of L-regularity and local L-regularity of a subset in Cn . We
                                          denote the open Euclidean ball of center a ∈ Cn and radius r ∈ (0, ∞] by B(a, r)
                                          and its closure by B̄(a, r).
                                          Definition 1.1. Let E be a subset in Cn and a ∈ Ē. We say
                                              (i) E is L-regular at a if LE is continuous at a, or equivalently, L∗E (a) = 0.
                                             (ii) E is locally L-regular at a if LE∩B̄(a,r) is continuous at a for each r ∈ (0, ∞].

                                             Key words and phrases. extremal function, Hermitian manifold, continuous, locally L-regular,
                                          weakly locally L-regular.
                                                                                           1
2                                    HYUNSOO AHN


    (iii) E is L-regular if LE is continuous at every point of Ē.
    (iv) E is locally L-regular if it is locally L-regular at every point of Ē.
    The equivalence in (i) is due to the non-negativity of LE . In (ii), LE is locally
L-regular at a if and only if LE∩B̄(a,r) is continuous at a for small r > 0. This
equivalence follows from the the monotonicity of extremal functions with respect to
the set inclusion. By the same reason, E is locally L-regular at a if and only if LE∩S
is continuous at a for each neighborhood S ⊂ Cn of a. About (iii), L-regularity of a
compact set F ⊂ Cn implies the continuity of LF on Cn since the extremal function
of a compact subset in Cn is lower semicontinuous as the supremum of a family of
smooth functions (see [Kl91, Corollary 5.1.3] for the proof) and L-regularity of F
gives the upper semicontinuity of LF = L∗F from the fact that L∗F = 0 on F .
    Local L-regularity of a set in Cn implies L-regularity by monotonicity, but the
converse is not true. Sadullaev in [Sa16] gives a counterexample F0 := {z ∈ C :
|z| = 1} ∪ {0}. LF0 (z) = LB̄(0,1) (z) = log+ |z|. Thus F0 is L-regular, but it is
not locally L-regular at 0 as LF0 ∩B̄(0,1/2) (z) = L{0} (z) is 0 at z = 0 and ∞ at
z ̸= 0. However, Cegrell in [Ce82] proved that L-regularity and local L-regularity
are equivalent for a compact subset in Rn as a subset of Cn .
    Local L-regularity is related to the continuity of weighted extremal functions.
For a real-valued function ϕ on E, the weighted extremal function LE,ϕ for (E, ϕ)
is
                  LE,ϕ (z) := sup{u(z) : u ∈ L, u|E ≤ ϕ}, z ∈ Cn .
Siciak [Si81, Proposition 2.12] proved that for a compact subset F ⊂ Cn and a
bounded lower semicontinuous function ψ : F → R, LF,ψ is also lower semicon-
tinuous as the supremum of a family of smooth functions. Therefore, if LF,ψ is
continuous on F (continuous at each point in F ), then L∗F,ψ |F = LF,ψ |F ≤ ψ,
LF,ψ = L∗F,ψ is continuous on Cn . Furthermore, LF,ψ is continuous if ψ is continu-
ous and F is locally L-regular by [Si81, Proposition 2.16].
   Results. Throughout this article, (X, ω) is a compact Hermitian manifold of com-
plex dimension n. A function ϕ : X → R ∪ {−∞} is called quasi-plurisubharmonic
(quasi-psh for short) if ϕ ̸≡ −∞ and ϕ is locally written as the sum of a smooth
function and a psh function. For the real differential operators d := ∂ + ∂¯ and
dc := i(∂¯ − ∂), the family of ω-psh functions on X is defined by
        P SH(X, ω) := {v : X → R ∪ {−∞} : v is quasi-psh, ω + ddc v ≥ 0}.
We also write ωv = ω + ddc v for an ω-psh function v. If ϕ : X → R ∪ {−∞} is
quasi-psh, then there exists a constant c > 0 such that ddc ϕ + cω ≥ 0, since X is
compact and P SH(X, c1 ω) ⊂ P SH(X, c2 ω) for 0 < c1 < c2 < ∞.
  The extremal function VE = Vω;E of a subset E in X is defined by
(1.1)      VE (x) = Vω;E (x) := sup{v(x) : v ∈ P SH(X, ω), v|E ≤ 0},        x ∈ X.
For a weight function ϕ : E → R, the weighted extremal function of (E, ϕ) is
(1.2)    VE,ϕ (x) = Vω;E,ϕ (x) := sup{v(x) : v ∈ P SH(X, ω), v|E ≤ ϕ},       x ∈ X.
When the domain of a real-valued function ψ contains E, we write VE,ψ|E as VE,ψ
for convenience. There is a bijection between P SH(CPn , ωF S ) and the Lelong class
L ([GZ17, Chapter 8]). When ϕ is a continuous function on a compact subset of
X, we can extend ϕ to a continuous function on X with the same supremum norm
by Tietze’s extension theorem.
                        CONTINUITY OF EXTREMAL FUNCTIONS                                3


Definition 1.2 (local L-regularity in a complex manifold). Let Y be a complex
manifold. Let E be a subset of Y and a ∈ Ē. We say
    (i) E is locally L-regular at a if for every R ∈ (0, ∞] and every holomorphic
        coordinate ball (Ω, τ ) in Y centered at a of radius R, τ (E ∩τ −1 (B̄(0, R/2)))
        is locally L-regular at 0, or equivalently, τ (E ∩ Ω) is locally L-regular at 0.
        Equivalently, we say E is locally L-regular at a if for every holomorphic
        chart (O, g) in Y containing a, g(E ∩ O) is locally L-regular at g(a).
   (ii) E is weakly locally L-regular at a if for some R ∈ (0, ∞] and some holo-
        morphic coordinate ball (Ω, τ ) in Y centered at a of radius R, τ (E ∩ Ω) is
        locally L-regular at 0. Equivalently, we say E is weakly locally L-regular
        at a if for some holomorphic chart (O, g) in Y containing a, g(E ∩ O) is
        locally L-regular at g(a).
  (iii) E is locally L-regular if it is locally L-regular at every point of Ē.
  (iv) E is weakly locally L-regular if it is weakly locally L-regular at every point
        of Ē.
   In this definition, the first equivalence in (i) is due to the fact that both the
intersection of τ (E ∩ τ −1 (B̄(0, R/2))) with B̄(0, r) and the intersection of τ (E ∩ Ω)
with B̄(0, r) are equal to τ (E ∩ τ −1 (B̄(0, r))) for each r ∈ (0, R/2]. The reason for
the second equivalence in (i) is that, for some R0 ∈ (0, ∞), B(g(a), R0 ) ⊂ g(O),
         L∗g(E∩O)∩B̄(g(a),r) (g(a)) = L∗g0 (E∩O0 )∩B̄(0,r) (0) = 0,   r ∈ (0, R0 /2],
for the coordinate ball (O0 , g0 ) := (g −1 (B(g(a), R0 )), g|O0 − g(a)) centered at a.
The equivalence in (ii) holds for the same reason as the second equivalence in (i).
Remark 1.3. In Definition 1.2, let (Ω∞ , τ∞ ) be a holomorphic coordinate ball
in Y centered at a with infinite radius as τ∞ (Ω∞ ) = Cn . Then (Ω2 , τ2 ) :=
   −1
(τ∞   (B(0, 2)), τ∞ |Ω2 ) is a holomorphic coordinate ball in Y centered at a of fi-
nite radius, and τ∞ (E ∩ Ω∞ ) ∩ B̄(0, r) = τ2 (E ∩ Ω2 ) ∩ B̄(0, r) for each r ∈ (0, 1].
Therefore, E is locally L-regular at a ∈ Ē if and only if for every holomorphic co-
ordinate ball (Ω, τ ) in Y centered at a of finite radius, τ (E ∩ Ω) is locally L-regular
at 0. By the same reason, E is weakly locally L-regular at a ∈ Ē if and only if for
some holomorphic coordinate ball (Ω, τ ) in Y centered at a of finite radius, τ (E ∩Ω)
is locally L-regular at 0.
  We get the following main results.
Theorem 1.4. Let K be a compact subset of a compact Hermitian manifold X and
a ∈ K. Let B̄(a, r) be a closed holomorphic coordinate ball in X with the center
a ∈ K and the finite radius r > 0. Then the following items hold:
    (i) VK is continuous at a if and only if VK∩B̄(a,r) is continuous at a.
   (ii) If ϕ : X → R is continuous and VK is continuous, then VK,ϕ is continuous.
   Theorem 1.4-(i) is used to prove the following characterizations of the continuity
of VK .
Theorem 1.5. Let K be a compact subset of a compact Hermitian manifold X and
a ∈ K. Then the following items are equivalent.
     (i) VK continuous at a.
    (ii) K is locally L-regular at a.
   (iii) K is weakly locally L-regular at a.
4                                   HYUNSOO AHN


Consequently, the continuity of VK , local L-regularity of K and weak local L-


### Actual text lines 415--510

                ∗
if and only if VK,ϕ  ≤ ϕ on K.                                                         □
                         CONTINUITY OF EXTREMAL FUNCTIONS                              9


2.2. Continuity of extremal functions on a compact Hermitian manifold.

Proof of Theorem 1.4. (i) Let E be a subset of X and b ∈ E. If VE is continuous
at b, then VE∗ (b) = VE (b) = 0. Conversely, VE∗ (b) = 0 implies
            lim sup VE (z) = 0 = lim inf VE (z),     lim VE (z) = 0 = VE (b).
              z→b                  z→b              z→b

Therefore, VE is continuous at b if and only if VE∗ (b) = 0.
  If VK∩B̄(a,r) is continuous at a, then VK is continuous at a since
                    0 ≤ VK∗ (a) ≤ VK∩
                                   ∗
                                      B̄(a,r) (a) = 0,    VK∗ (a) = 0.
                                                                     ∗
  Conversely, assume VK is continuous at a. It is enough to show VK∩    B̄(a,r)
                                                                                (a) = 0.
          ∞
Take ψ ∈ C (R, [0, 1]) supported on [−1, 1] with ψ(0) = 1 and the chart (U, f ) of
X with U ⊃ B̄(a, r) = f −1 (B̄(f (a), r)). They induce χr ∈ C ∞ (X, [0, 1]) defined as
                           (
                              1 − ψ(∥f (x) − f (a)∥/r), x ∈ U,
                 χr (x) :=
                              1, x ∈ X \ B̄(a, r).

χr (a) = 0 and χr ≡ 1 on X \ B̄(a, r). Its C 1 -norm and C 2 -norm are bounded by
(2.8)                 ∥χr ∥C 1 (X) ≤ c1 /r,   ∥χr ∥C 2 (X) ≤ c2 /r2 .
Here, c1 > 0 and c2 > 0 are constants independent of a and r, but they depend on
the choice of the holomorphic coordinate chart (U, f ). Accordingly, since ω > 0,
−ddc χr ≥ −(c′2 /r2 )ω for some constant c′2 ≥ 1 depending only on (U, f ). Then for
εr := min{r2 /c′2 , 1}/2, the function −εr χr belongs to P SH(X, ω/2).
    Let v ∈ P SH(X, ω), v ≤ 1 and v ≤ 0 on K ∩ B̄(a, r). By the choice of χr and εr ,
εr (v − χr ) ≤ 0 on K and εr + 1/2 ≤ 1. These imply εr (v − χr ) ≤ VK . Accordingly,
(2.9)                         εr h∗K∩B̄(a,r) − εr χr ≤ VK∗ .

(2.9) and VK∗ (a) = 0 = χr (a) give h∗K∩B̄(a,r) (a) = 0, h∗K∩B̄(a,r) ̸≡ 1. By Lemma 2.11,
K ∩ B̄(a, r) is not pluripolar and Capω (K ∩ B̄(a, r)) > 0. By (2.6),
                         ∗
                    sup VK∩ B̄(a,r) ≤ A/Capω (K ∩ B̄(a, r)) < ∞.
                     X
            ∗                     ∗
By (2.2), VK∩ B̄(a,r)
                      (a) ≤ supX VK∩        h∗
                                     B̄(a,r) K∩B̄(a,r)
                                                                        ∗
                                                       (a). Therefore, VK∩ B̄(a,r)
                                                                                   (a) =
0.
                                                                                   ∗
   (ii) By Lemma 2.13, to prove the continuity of VK,ϕ , it is enough to show VK,ϕ     ≤
                            ′                                    ′
ϕ on K. Let b ∈ K and ε > 0. We have ϕ|B̄(b,r) ≤ ϕ(b) + ε for small r > 0. By
(2.7),
          VK,ϕ ≤ VK∩B̄(b,r),ϕ ≤ VK∩B̄(b,r),ϕ(b)+ε′ = ϕ(b) + ε′ + VK∩B̄(b,r) .
                                       ∗
Since VK is assumed to be continuous, VK∩ B̄(b,r)
                                                  (b) = 0 by Theorem 1.4-(i). Thus,
  ∗                 ′          ′     +            ∗
VK,ϕ (b) ≤ ϕ(b) + ε . Letting ε → 0 gives VK,ϕ       (b) ≤ ϕ(b). Since b ∈ K was
            ∗
arbitrary, VK,ϕ ≤ ϕ on K.                                                        □

   We have a partial converse of Theorem 1.4-(ii) with appropriately scaled quasi-
psh continuous weight functions on compact Hermitian manifolds. Nguyen in [Ng24]
proved this partial converse on compact Kähler manifolds.
10                                     HYUNSOO AHN


Corollary 2.14. Let K be a compact subset of X and ϕ be a quasi-psh continuous
real-valued function on X with constants c > 0 and c′ > 0 such that cω +ddc ϕ ≥ c′ ω
as currents. If VK,ϕ/c is continuous. Then VK is continuous. In particular, if
ψ : X → R is smooth with a constant c′′ > 0 such that c′′ ω + ddc ψ > 0 and VK,ψ/c′′
is continuous, then VK is continuous.

Proof. Let θ := cω + ddc ϕ ≥ c′ ω as currents. Define Capθ (·) as Capω (·), us-
ing θ instead of ω. Let ∥ϕ∥X be the supremum norm of ϕ on X. Finiteness
of Capcc′ ω/(1+2∥ϕ∥X ) (X) implies finiteness of Capθ (X). For any locally defined
smooth potential functions ρ1 and ρ2 satisfying ddc ρ1 ≤ ω ≤ ddc ρ2 , we have
ddc (c′ ρ1 ) ≤ θ ≤ ddc (cρ2 + ϕ) as currents. Accordingly, not only Capω (·) but also
                                       PN
Capθ (·) is bi-Lipschitz equivalent to j=1 Cap(· ∩ Uj,δ , Uj ) by the same proof used
for Lemma 2.11. The continuous local potential cρ2 +ϕ with θ ≤ ddc (cρ2 +ϕ) and the
boundedness of ϕ implies that θn (X) is finite and {ψ ∈ P SH(X, θ) : supX ψ = 0}
is bounded in L1 (X, θn ), by the same reasoning for a smooth Hermitian case. Then
by the same proof used for the second inequality in (2.6), there exists a uniform
constant Aθ > 0 such that, for each non-pluripolar compact set F1 in X,
                                                   Aθ
                                  sup Vθ;F1 ≤               .
                                   X             Capθ (F1 )

   By Lemma 2.11 and the comparability of Capω (·) and Capθ (·), for each compact


## Exact retrieved printed primary passages: Ahn-Holder-weighted-extremals-2604.01887v3

Text SHA256: ace2ffba8a7bc425c30b0217d9c21bbde6b4ca6583a5e135d69d1119adc626a6; corresponding PDF SHA256: 59134127d7fb6c6dd7544db35dec7026207e8a4baaccbcc6e4c16d788a07d831.


### Actual text lines 1--170

                                           HÖLDER REGULARITY OF SICIAK-ZAHARJUTA EXTREMAL
                                              FUNCTIONS ON COMPACT HERMITIAN MANIFOLDS


                                                                                   HYUNSOO AHN
arXiv:2604.01887v3 [math.CV] 6 May 2026




                                                   Abstract. For a compact subset in a compact Hermitian manifold, we prove
                                                   that the Hölder continuity of the extremal function at a given point in the set is
                                                   a local property and that the Hölder continuity of a weighted extremal function
                                                   follows from the Hölder continuities of the extremal function and the weight
                                                   function with a uniform density in capacity. The second result can be seen as
                                                   an extension of a result of Lu, Phung and Tô [LPT21]. Moreover, for a compact
                                                   subset in a compact Hermitian manifold, we prove that, both at the point level
                                                   and at the global level, the Hölder continuity of the extremal function with
                                                   the uniform density in capacity is equivalent to the local Hölder continuity
                                                   property, which is also equivalent to the weak local Hölder continuity property.
                                                   These results are generalizations of the results of Nguyen [Ng24] on compact
                                                   Kähler manifolds. We also show that the µ-Hölder continuity property of a
                                                   convex compact subset in Cn and of a compact subset in Cn at a star center
                                                   imply the local µ-Hölder continuity property of order µ of the convex compact
                                                   subset and of the compact subset at the point, respectively.




                                                                                1. Introduction
                                             Background. Complex Monge-Ampère equations are essential for the classifica-
                                          tion of complex surfaces and in solving geometric flow problems [PSS12]. Solving
                                          complex Monge-Ampère equations on compact Hermitian manifolds is important in
                                          pluripotential theory because it generalizes Kähler geometry to broader non-Kähler
                                          settings and provides a framework for analyzing degenerate equations [GZ17]. Sta-
                                          bility and the Hölder regularity of the solutions to the equations on compact Her-
                                          mitian manifolds are obtained in [KN18].
                                             The Hölder continuity of the solution to the complex Monge-Ampère equations
                                          is the best global regularity when the density is in Lp with p > 1. (Let ∥ · ∥ be
                                          the standard Euclidean norm on Cn . For each p ∈ (1, 2) and β ∈ (2 − 2/p, 1),
                                          u(z) := ∥z∥β has Lp -density, but u is not Lipschitz continuous at 0.) Kolodziej
                                          [Ko08] first proved the Hölder continuity. After that, Demailly, Dinew, Guedj,
                                          Pham, Kolodziej and Zeriahi in [DDGHKZ] showed it with an explicit exponent on
                                          compact Kähler manifolds. After that, Kolodziej and Nguyen in [KN19] showed the
                                          Hölder continuity on compact Hermitian manifolds with strictly positive density.
                                          Also, Kolodziej and Nguyen in [KN18] showed it on compact Hermitian manifolds
                                          with non-negative density.
                                             In fact, Kolodziej and Nguyen showed more than that. They [KN18] proved
                                          that on a compact Hermitian manifold (X, ω), complex Monge-Ampère equations
                                          with finite Borel measures, dominated by complex Monge-Ampère measures of ω-
                                          plurisubharmonic Hölder continuous functions (in other words, admitting global

                                             Key words and phrases. extremal function, Hermitian manifold, Hölder continuous, uniform
                                          density in capacity, HCP, local Hölder continuity property.
                                                                                           1
2                                 HYUNSOO AHN


Hölder continuous subsolutions), have Hölder continuous solutions. Lu, Phung and
Tô in [LPT21] showed a nearly optimal Hölder exponent of the solutions to the
equations in compact Hermitian manifolds, as in compact Kähler manifolds.
   The Siciak-Zaharjuta extremal function can serve as such a subsolution when it is
Hölder continuous. Lu, Phung and Tô in [LPT21] also showed that for a Hölder con-
tinuous weight function on a compact Hermitian manifold, its ω-plurisubharmonic
envelope becomes an ω-plurisubharmonic Hölder continuous function. One of our
results extends this result of [LPT21] for general compact subsets of compact Her-
mitian manifolds.
   Recall that the Lelong class L is defined by
L := {u ∈ P SH(Cn ) : for some constant cu , u(z) ≤ max{0, log ∥z∥} + cu , z ∈ Cn }.
For a subset E in Cn , the classical Siciak-Zaharjuta extremal function of E intro-
duced in [Si62, Si81, Za76] is defined on Cn by
                 LE (z) := sup{u(z) : u ∈ L, u|E ≤ 0},     z ∈ Cn .
The regularity of the extremal function of a set gives geometric information about
the set itself. For example, E is pluripolar if and only if L∗E ≡ ∞, where ∗ denotes
the upper semicontinuous regularization, and E is non-pluripolar if and only if
L∗E ∈ L. For a real-valued function ϕ on E, the weighted extremal function LE,ϕ
is defined by
                 LE,ϕ (z) := sup{u(z) : u ∈ L, u|E ≤ ϕ},   z ∈ Cn .
   Results. Throughout this article, (X, ω) is a compact Hermitian manifold of com-
plex dimension n. A function ϕ : X → R ∪ {−∞} is called quasi-plurisubharmonic
(quasi-psh for short) if ϕ ̸≡ −∞ and ϕ is locally written as the sum of a smooth
function and a psh function. For the real differential operators d := ∂ + ∂¯ and
dc := i(∂¯ − ∂), the family of ω-plurisubharmonic (ω-psh for short) functions on X
is defined by
        P SH(X, ω) := {v : X → R ∪ {−∞} : v is quasi-psh, ω + ddc v ≥ 0}.
If ϕ : X → R ∪ {−∞} is quasi-psh, then there exists a constant c > 0 satisfying
ddc ϕ + cω ≥ 0, since X is compact and P SH(X, c1 ω) ⊂ P SH(X, c2 ω) for 0 < c1 <
c2 < ∞.
   The extremal function VE = Vω;E of a subset E in X is defined by
(1.1)     VE (x) = Vω;E (x) := sup{v(x) : v ∈ P SH(X, ω), v|E ≤ 0},     x ∈ X.
For a weight function ϕ : E → R, the weighted extremal function of (E, ϕ) is
(1.2)   VE,ϕ (x) = Vω;E,ϕ (x) := sup{v(x) : v ∈ P SH(X, ω), v|E ≤ ϕ},    x ∈ X.
When the domain of a real-valued function ψ contains E, we write VE,ψ|E as VE,ψ for
convenience. There is a bijection between the Lelong class L and P SH(CPn , ωF S )
([GZ17, Chapter 8]). When ϕ is a continuous function on a compact subset of X,
we can extend ϕ to a continuous function on X with the same supremum norm by
Tietze’s extension theorem. An extension of a Hölder continuous function from a
compact subset to X is also possible with the same Hölder exponent and the same
Hölder constant by Mcshane’s extension [Mc34].
   Our main theorems are about the Hölder continuity of extremal functions for
non-pluripolar compact sets in X. Lu, Phung and Tô in [LPT21] proved that for
a given Hölder continuous real-valued function ϕ on X with a Hölder exponent
                 HÖLDER REGULARITY OF EXTREMAL FUNCTIONS                            3

                           ∗
α ∈ (0, 1), the envelope VX,ϕ  is also Hölder continuous with the same exponent α.
                                                                           ∗
VX,ϕ is continuous by [Ah26] since VX ≡ 0 and ϕ are continuous, thus VX,ϕ     = VX,ϕ .
However, the Hölder exponent or even Hölder continuity of the weighted extremal
functions for a general non-pluripolar compact subset is not always preserved. We
need an additional condition, called the uniform density in capacity [Ng24].
   Let Ω be a smoothly bounded strictly pseudoconvex domain in Cn . Bedford and
Taylor in [BT82] first studied the relative capacity of a Borel subset E in Ω, defined
by                               Z
             Cap(E, Ω) := sup{        (ddc u)n : u ∈ P SH(Ω), 0 ≤ u ≤ 1}.
                                  E
We denote the Euclidean open ball of center a ∈ Cn and radius r ∈ (0, ∞] by B(a, r)
and its closure by B̄(a, r). Let F be a compact subset of Cn . We say that F has
a uniform density in capacity if there exist constants q > 0, κ > 0, δ > 0 and a
Euclidean bounded open ball O in Cn such that B̄(F, δ) is contained in O and for
each b ∈ F ,
                                Cap(F ∩ B̄(b, r), O)
(1.3)                       inf                      ≥ κ.
                          0<r≤δ        rq
We say that F has a uniform density in capacity at b ∈ F if (1.3) holds. Recall
that the global Bedford-Taylor capacity of a Borel subset E in X is defined as
                          Z
(1.4)     Capω (E) := sup{ (ω + ddc v)n : v ∈ P SH(X, ω), 0 ≤ v ≤ 1}.
                             E
   By [DK12, Proposition 2.3], Capω (X) < ∞. The property of the uniform density
in capacity of a compact subset in X is defined in Section 3 using the global Bedford-
Taylor capacity, similarly as that of a compact subset in Cn .
   Our main results are about the Hölder continuity of extremal functions on X.
Theorem 1.1. Let K be a compact subset of a compact Hermitian manifold X and
a ∈ K. Let B̄(a, r) be a closed holomorphic coordinate ball in X with the center
a ∈ K and the finite radius r > 0. Then the following items hold:
    (i) Let µ ∈ (0, 1]. VK is µ-Hölder continuous at a if and only if VK∩B̄(a,r) is
        µ-Hölder continuous at a.
   (ii) If K has a uniform density in capacity and ϕ : X → R and VK are Hölder
        continuous, then VK,ϕ is Hölder continuous.
Theorem 1.2. Let K be a compact subset of a compact Hermitian manifold X and
a ∈ K. Then the following three items are equivalent.
     (i) VK is Hölder continuous at a and K has a uniform density in capacity at
         a.
    (ii) K has local Hölder continuity property at a.
   (iii) K has weak local Hölder continuity property at a.
Also, the following three items are equivalent.
   (iv) VK is Hölder continuous and K has a uniform density in capacity.
    (v) K has local Hölder continuity property.
   (vi) K has weak local Hölder continuity property.
   In Theorem 1.2, the equivalence of (iv), (v) and (vi) does not directly comes
from that of (i), (ii) and (iii). The proof of Theorem 1.1-(i) gives Corollary 5.1,
which is used for the proofs of Theorem 1.1-(ii) and Theorem 1.2. The local Hölder
4                                   HYUNSOO AHN


continuity property and the weak local Hölder continuity property in Theorem 1.2
are introduced in Section 3. Theorem 1.1-(ii) is a generalization of the above-
mentioned result of [LPT21] to a general weighted extremal function, with the
additional condition uniform density in capacity. However, unlike the envelopes,
the Hölder exponent becomes smaller: if VK and ϕ are µ-Hölder continuous for
µ ∈ (0, 1] and K has a uniform density in capacity of order q ∈ (0, ∞), then VK,ϕ is
µ2 /(µ + q + 2)-Hölder continuous. N. C. Nguyen in [Ng24] proved Theorem 1.1 and
some analogue of Theorem 1.2 for compact Kähler manifolds, and we generalize his
results to compact Hermitian manifolds.
   Let 0 < µ, ν ≤ 1 and 0 < q, q0 be constants. In Theorem 1.2, the weak local
µ-Hölder continuity property of order q implies the uniform density in capacity


### Actual text lines 945--995

is non-pluripolar, Capω (K ∩ B̄jb (b, rb )) > 0, so Capω (K ∩ Dλ ) > 0. Therefore,
                                 η
               Capω (K ∩ B̄ja (a, )) ≥ Capω (K ∩ Dλa )
                                 l1
                                       ≥ min Capω (K ∩ Dλ ) =: c
                                              λ:K∩Dλ ̸=∅
                                           > 0.
Then the inclusion K ⊃ K ∩ B̄ja (a, η/l1 ) and (5.2) with η/l1 ≤ r0 gives
                                               Ã η −2 µ
                        VK (x) ≤ VK∩B̄ja (a, lη ) (x) ≤
                                                  ( ) δ .
                                                c l1
                                                  1


This inequality and Lemma 4.3 prove the µ-Hölder continuity of VK .                      □
     With this corollary, we can prove Theorem 1.1-(ii).
Proof of Theorem 1.1-(ii). We want to show the Hölder continuity of V := VK,ϕ .
By taking the minimum of Hölder exponents of VK and ϕ, we can assume that VK
and ϕ are Hölder continuous with the same Hölder exponent 0 < µ ≤ 1.
  Let b ∈ K and ε′ > 0. ϕ|B̄(b,r) ≤ ϕ(b) + ε′ for small r > 0. By (2.6),
             V ≤ VK∩B̄(b,r),ϕ ≤ VK∩B̄(b,r),ϕ(b)+ε′ = ϕ(b) + ε′ + VK∩B̄(b,r) .
                         ∗
By Theorem 1.1-(i), VK∩    B̄(b,r)
                                   (b) = 0. Then V ∗ (b) ≤ ϕ(b) + ε′ . ε′ → 0+ gives
  ∗                             ∗
V (b) ≤ ϕ(b). Accordingly, V |K ≤ ϕ|K , V is continuous by Lemma 2.11. To prove
the Hölder continuity of V , by Proposition 4.4, it is enough to show that there exist
constants C > 0, µ′ > 0 and δ0 > 0 satisfying
                                              ′
                      V (x) ≤ ϕ(x) + Cδ µ ,           dω (x, K) ≤ δ ≤ δ0 .
    Since X is compact, it has a finite cover {(Ωj , τj )}j∈Λ of holomorphic balls
τj (Ωj ) = B(0, 5) ⊂ Cn with the refined cover {(τj−1 (B(0, 1)), τj )}j∈Λ . Denote
                   HÖLDER REGULARITY OF EXTREMAL FUNCTIONS                                         19


B̄j (b, r) := τj−1 (B̄(τj (b), r)). By Remark 3.5, there exist positive constants 0 < l1 ≤
1 ≤ l2 such that for each j ∈ Λ and p, p′ ∈ τj−1 (B̄(0, 4)),
                  l1 ∥τj (p) − τj (p′ )∥ ≤ dist(p, p′ ) ≤ l2 ∥τj (p) − τj (p′ )∥.
   Set δ1 := (l2 )−1 ≤ 1. Let x ∈ X with dω (x, K) ≤ δ ≤ δ1 . Pick bx ∈ K of
                                         −1
dω (x, bx ) = dω (x, K). Then bx ∈ τj(b    x)
                                              (B(0, 1)) for some j(bx ) ∈ Λ. Let r ∈ (0, δ1 ]
be determined later. By Hölder continuity, |ϕ(w) − ϕ(bx )| ≤ c0 (l2 r)µ for each
w ∈ B̄j(bx ) (bx , r), where c0 is a Hölder coefficient of ϕ. By the monotonicity (2.6),
        V (x) ≤ VK∩B̄j(bx ) (bx ,r),ϕ (x) ≤ VK∩B̄j(bx ) (bx ,r),ϕ(bx )+c0 l2µ rµ (x)
(5.3)                                      = ϕ(bx ) + c0 l2µ rµ + VK∩B̄j(bx ) (bx ,r) (x)
                                           ≤ ϕ(x) + c0 δ µ + c0 l2µ rµ + VK∩B̄j(bx ) (bx ,r) (x).

   Corollary 5.1-(i) and a uniform density in capacity of K give constants 0 < δ2 ≤


## Exact retrieved printed primary passages: Demailly-agbook-Harvard

Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de; corresponding PDF SHA256: d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1.


### Actual text lines 1810--1935

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
from its validity for u ⋆ ρε and from the monotone convergence theorem.                     

(4.19) Corollary. If u ∈ Sh(Ω) is such that u 6≡ −∞ on each connected component of
Ω, then ∆u computed in the sense of distribution theory is a positive measure.

    Indeed ∆(u ⋆ ρε ) ⩾ 0 as a function, and ∆(u ⋆ ρε ) converges weakly to ∆u in D′ (Ω).
Corollary 4.19 has a converse, but the correct statement is slightly more involved than
for the direct property:
36                       Chapter I. Complex Differential Calculus and Pseudoconvexity

(4.20) Theorem. If v ∈ D′ (Ω) is such that ∆v is a positive measure, there exists a
unique function u ∈ Sh(Ω) locally integrable such that v is the distribution associated to
u.

   We must point out that u need not coincide everywhere with v, even when v is a
locally integrable upper semicontinuous function: for example, if v is the characteristic
function of a compact subset K ⊂ Ω of measure 0, the subharmonic representant of v is
u = 0.

Proof. Set vε = v ⋆ ρε ∈ C∞ (Ωε , R). Then ∆vε = (∆v) ⋆ ρε ⩾ 0, thus vε ∈ Sh(Ωε ).
Arguments similar to those in the proof of Th. 4.18 show that (vε ) is non decreasing
in ε. Then u := limε→0 vε ∈ Sh(Ω) by Th. 4.15. Since vε converges weakly to v, the
monotone convergence theorem shows that
                                Z                   Z
                hv, f i = lim           vε f dλ =       u f dλ,         ∀f ∈ D(Ω),      f ⩾ 0,
                         ε→0        Ω               Ω

which concludes the existence part. The uniqueness of u is clear from the fact that u
must satisfy u = lim u ⋆ ρε = lim v ⋆ ρε .                                         

   The most natural topology on the space Sh(Ω) of subharmonic functions is the topo-
logy induced by the vector space topology of L1loc (Ω) (Fréchet topology of convergence
in L1 norm on every compact subset of Ω).

(4.21) Proposition. The convex cone Sh(Ω) ∩ L1loc (Ω) is closed in L1loc (Ω), and it has
the property that every bounded subset is relatively compact.

Proof. Let (uj ) be a sequence in Sh(Ω) ∩ L1loc (Ω). If uj → u in L1loc (Ω) then ∆uj → ∆u
in the weak topology of distributions, hence ∆u ⩾ 0 and u can be represented by a
subharmonic function thanks to Th. 4.20. Now, suppose that kuj kL1 (K) is uniformly
bounded for every compact subset K of Ω. Let µj = ∆uj ⩾ 0. If ψ ∈ D(Ω) is a test
function equal to 1 on a neighborhood ω of K and such that 0 ⩽ ψ ⩽ 1 on Ω, we find
                                Z                       Z
                   µj (K) ⩽             ψ ∆uj dλ =              ∆ψ uj dλ ⩽ Ckuj kL1 (K ′ ) ,
                                Ω                           Ω


where K ′ = Supp ψ, hence the sequence of measures (µj ) is uniformly bounded in mass
on every compact subset of Ω. By weak compactness, there is a subsequence (µjν ) which
converges weakly to a positive measure µ on Ω. We claim that f ⋆ (ψµjν ) converges to
f ⋆(ψµ) in L1loc (Rm ) for every function f ∈ L1loc (Rm ). In fact, this is clear if f ∈ C∞ (Rm ),
and in general we use an approximation of f by a smooth function g together with the
estimate

          k(f − g) ⋆ (ψµjν )kL1 (A) ⩽ k(f − g)kL1 (A+K ′ ) µjν (K ′ ),                  ∀A ⊂⊂ Rm

to get the conclusion. We apply this when f = N is the Newton kernel. Then hj =
uj − N ⋆ (ψµj ) is harmonic on ω and bounded in L1 (ω). As hj = hj ⋆ ρε for any
smoothing kernel ρε , we see that all derivatives Dα hj = hj ⋆ (Dα ρε ) are in fact uniformly
locally bounded in ω. Hence, after extracting a new subsequence, we may suppose that
                        § 4. Subharmonic Functions                                           37

hjν converges uniformly to a limit h on ω. Then ujν = hjν + N ⋆ (ψµjν ) converges to
u = h + N ⋆ (ψµ) in L1loc (ω), as desired.                                        
  We conclude this subsection by stating a generalized version of the Green-Riesz for-
mula.

(4.22) Proposition. Let u ∈ Sh(Ω) ∩ L1loc (Ω) and B(0, r) ⊂ Ω.

a) The Green-Riesz formula still holds true for such an u, namely, for every x ∈ B(0, r)
                    Z                               Z
            u(x) =        ∆u(y) Gr (x, y) dλ(y) +          u(y) Pr (x, y) dσ(y).
                           B(0,r)                                  S(0,r)


### Actual text lines 1988--2118

                                               u = sup uα

need not be upper semicontinuous, so we consider its upper semicontinuous regulariza-
tion:
                            u⋆ (z) = lim sup u ⩾ u(z).
                                               ε→0 B(z,ε)

It is easy to check that u⋆ is the smallest upper semicontinuous function which is ⩾ u.
Our goal is to show that u⋆ can be computed with a countable subfamily of (uα ). Let
B(zj , εj ) be a countable basis of the topology of Ω. For each j, let (zjk ) be a sequence
of points in B(zj , εj ) such that

                                    sup u(zjk ) =         sup u,
                                     k                  B(zj ,εj )


and for each pair (j, k), let α(j, k, l) be a sequence of indices α ∈ I such that u(zjk ) =
supl uα(j,k,l) (zjk ). Set
                                       v = sup uα(j,k,l) .
                                                j,k,l

Then v ⩽ u and v ⋆ ⩽ u⋆ . On the other hand

             sup v ⩾ sup v(zjk ) ⩾ sup uα(j,k,l) (zjk ) = sup u(zjk ) =     sup u.
           B(zj ,εj )    k               k,l                         k    B(zj ,εj )


As every ball B(z, ε) is a union of balls B(zj , εj ), we easily conclude that v ⋆ ⩾ u⋆ , hence
v ⋆ = u⋆ . Therefore:

(4.23) Choquet’s lemma. Every family (uα ) has a countable subfamily (vj ) = (uα(j) )
such that its upper envelope v satisfies v ⩽ u ⩽ u⋆ = v ⋆ .                       

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



### Actual text lines 2315--2395


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
   Polar and pluripolar sets are sets of −∞ poles of subharmonic and plurisubharmonic
functions. Although these functions possess a large amount of flexibility, pluripolar sets
have some properties which remind their loose relationship with holomorphic functions.

(5.22) Definition. A set A ⊂ Ω ⊂ Rm (resp. A ⊂ X, dimC X = n) is said to be polar
(resp. pluripolar) if for every point x ∈ Ω there exist a connected neighborhood W of x and
u ∈ Sh(W ) (resp. u ∈ Psh(W )), u 6≡ −∞, such that A ∩ W ⊂ {x ∈ W ; u(x) = −∞}.

   Theorem 4.17 implies that a polar or pluripolar set is of zero Lebesgue measure. Now,
we prove a simple extension theorem.

(5.23) Theorem. Let A ⊂ Ω be a closed polar set and v ∈ Sh(Ω r A) such that v is
bounded above in a neighborhood of every point of A. Then v has a unique extension
ve ∈ Sh(Ω).
Proof. The uniqueness is clear because A has zero Lebesgue measure. On the other hand,
every point of A has a neighborhood W such that

               A ∩ W ⊂ {x ∈ W ; u(x) = −∞},              u ∈ Sh(W ),   u 6≡ −∞.
               § 6. Domains of Holomorphy and Stein Manifolds                            45

After shrinking W and subtracting a constant to u, we may assume u ⩽ 0. Then for
every ε > 0 the function vε = v + εu ∈ Sh(W r A) can be extended as an upper
semicontinuous on W by setting vε = −∞ on A ∩ W . Moreover, vε satisfies the mean
value inequality vε (a) ⩽ µS (vε ; a, r) if a ∈ W r A, r < d(a, A ∪ ∁W ), and also clearly
if a ∈ A, r < d(a, ∁W ). Therefore vε ∈ Sh(W ) and ve = (sup vε )⋆ ∈ Sh(W ). Clearly ve
coincides with v on W r A. A similar proof gives:

(5.24) Theorem. Let A be a closed pluripolar set in a complex analytic manifold X.
Then every function v ∈ Psh(X rA) that is locally bounded above near A extends uniquely
into a function ve ∈ Psh(X).                                                         

(5.25) Corollary. Let A ⊂ X be a closed pluripolar set. Every holomorphic function
f ∈ O(X rA) that is locally bounded near A extends to a holomorphic function fe ∈ O(X).
Proof. Apply Th. 5.24 to ± Re f and ± Im f . It follows that Re f and Im f have pluri-
harmonic extensions to X, in particular f extends to fe ∈ C∞ (X). By density of X r A,
d′′ fe = 0 on X.                                                                    

(5.26) Corollary. Let A ⊂ Ω (resp. A ⊂ X) be a closed (pluri)polar set. If Ω (resp. X)
is connected, then Ω r A (resp. X r A) is connected.


### Actual text lines 17245--17428

                                   =−                   ω ∧       .
                                              ∂z k           ∂zk
                                         k

           ∂
Clearly             ω = −idzk , so
          ∂z k
                                                       X              ∂u
                                    [d′′⋆ , L] u = i          dzk ∧       = id′ u.                         
                                                                      ∂zk
                                                          k



   We are now ready to derive the basic commutation relations in the case of an arbitrary
Kähler manifold (X, ω).

(6.4) Theorem. If (X, ω) is Kähler, then

                                    [d′′⋆ , L]= id′ ,            [d′⋆ , L]= −id′′ ,
                                    [Λ, d′′ ] = −id′⋆ ,          [Λ, d′ ] = id′′⋆ .


Proof. It is sufficient to verify the first relation, because the second one is the conjugate
of the first, and the relations of the second line are the adjoint of those of the first line.
If (zj ) is a geodesic coordinate system at a point x0 ∈ X, then for any (p, q)-forms u, v
with compact support in a neighborhood of x0 , (4.9) implies
                                    Z    X                      X                       
                      hhu, vii =                   uIJ v IJ +             aIJKL uIJ v KL dV,
                                     M       I,J                I,J,K,L


with aIJKL (z) = O(|z|2 ) at x0 . An integration by parts as in (3.12) and (6.2′′ ) yields
                           X ∂uI,J ∂                                      X
           d′′⋆ u = −                               (dzI ∧ dz J ) +             bIJKL uIJ dzK ∧ dz L ,
                              ∂zk ∂z k
                           I,J,k                                      I,J,K,L
306                                                  Chapter VI. Hodge Theory

where the coefficients bIJKL are obtained by derivation of the aIJKL ’s. Therefore
bIJKL = O(|z|). Since ∂ω/∂zk = O(|z|), the proof of Lemma 6.3 implies here [d′′⋆ , L]u =
id′ u + O(|z|), in particular both terms coincide at every given point x0 ∈ X.         

(6.5) Corollary. If (X, ω) is Kähler, the complex Laplace-Beltrami operators satisfy

                                                          1
                                           ∆′ = ∆′′ =       ∆.
                                                          2

Proof. It will be first shown that ∆′′ = ∆′ . We have
                                                                       
                                 ∆′′ = [d′′ , d′′⋆ ] = −i d′′ , [Λ, d′ ] .

Since [d′ , d′′ ] = 0, Jacobi’s identity (5.7) implies
                                                               
                                 − d′′ , [Λ, d′ ] + d′ , [d′′ , Λ] = 0,
                           
hence ∆′′ = d′ , −i[d′′ , Λ] = [d′ , d′⋆ ] = ∆′ . On the other hand

                  ∆ = [d′ + d′′ , d′⋆ + d′′⋆ ] = ∆′ + ∆′′ + [d′ , d′′⋆ ] + [d′′ , d′⋆ ].

Thus, it is enough to prove:

(6.6) Lemma. [d′ , d′′⋆ ] = 0, [d′′ , d′⋆ ] = 0.
                                             
Proof. We have [d′ , d′′⋆ ] = −i d′ , [Λ, d′ ] and (5.7) implies
                                                                   
                         − d′ , [Λ, d′ ] + Λ, [d′ , d′ ] + d′ , [d′ , Λ] = 0,
                     
hence −2 d′ , [Λ, d′ ] = 0 and [d′ , d′′⋆ ] = 0. The second relation [d′′ , d′⋆ ] = 0 is the adjoint
of the first.                                                                                     

(6.7) Theorem. ∆ commutes with all operators ⋆, d′ , d′′ , d′⋆ , d′′⋆ , L, Λ.

Proof. The identities [d′ , ∆′ ] = [d′⋆ , ∆′ ] = 0, [d′′ , ∆′′ ] = [d′′⋆ , ∆′′ ] = 0 and [∆, ⋆] = 0 are
immediate. Furthermore, the equality [d′ , L] = d′ ω = 0 together with the Jacobi identity
implies                                                       
                 [L, ∆′ ] = L, [d′ , d′⋆ ] = − d′ , [d′⋆ , L] = i[d′ , d′′ ] = 0.
By adjunction, we also get [∆′ , Λ] = 0.                                                            

§ 6.2. Commutation Relations on Hermitian Manifolds
   We are going to extend the commutation relations of § 6.1 to an arbitrary hermitian
manifold (X, ω). In that case ω is no longer tangent to a constant metric, and the
commutation relations involve extra terms arising from the torsion of ω. Theorem 6.8
below is taken from [Demailly 1984], but the idea was already contained in [Griffiths 1966].

(6.8) Theorem. Let τ be the operator of type (1, 0) and order 0 defined by τ = [Λ, d′ ω].
Then
                       § 6. Commutation Relations                                                   307

a)     [d′′⋆ , L]= i(d′ + τ ),
b)     [d′⋆ , L] = −i(d′′ + τ ),
c)     [Λ, d′′ ] = −i(d′⋆ + τ ⋆ ),
d)     [Λ, d′ ] = i(d′′⋆ + τ ⋆ ) ;
d′ ω will be called the torsion form of ω, and τ the torsion operator.
Proof. b) follows from a) by conjugation, whereas c), d) follow from a), b) by adjunction.
It is therefore enough to prove relation a).
   Let (zj )1⩽j⩽n be complex coordinates centered at a point x0 ∈ X, such that the n-
tuple (∂/∂z1 , . . . , ∂/∂zn ) is an orthonormal basis of Tx0 X for the metric ω(x0 ). Consider
the metric with constant coefficients
                                              X
                                       ω0 = i      dzj ∧ dz j .
                                                1⩽j⩽n

The metric ω can then be written
                                  ω = ω0 + γ with γ = O(|z|).
Denote by h , i0 , L0 , Λ0 , d′⋆   ′′⋆
                              0 , d0 the inner product and the operators associated to
the constant metric ω0 , and let dV0 = ω0n /2n n!. The proof of relation a) is based on a
Taylor expansion of L, Λ, d′⋆ , d′′⋆ in terms of the operators with constant coefficients
L0 , Λ0 , d′⋆   ′′⋆
           0 , d0 .

(6.9) Lemma. Let u, v ∈ C∞ (X, Λp,q TX
                                     ⋆
                                       ). Then in a neighborhood of x0
                          hu, vi dV = hu − [γ, Λ0 ]u, vi0 dV0 + O(|z|2 ).

Proof. In a neighborhood of x0 , let
                           X                 ⋆
                     γ=i          γj ζj⋆ ∧ ζ j ,            γ1 ⩽ γ2 ⩽ · · · ⩽ γn ,
                                1⩽j⩽n

be a diagonalization of the (1,1)-form γ(z) with respect to an orthonormal basis (ζj )1⩽j⩽n
of Tz X for ω0 (z). We thus have
                                               X              ⋆
                                ω = ω0 + γ = i     λj ζj⋆ ∧ ζ j

with λj = 1 + γj and γj = O(|z|). Set now

              J = {j1 , . . . , jp },     ζJ⋆ = ζj⋆1 ∧ · · · ∧ ζj⋆p ,     λJ = λj1 · · · λjp ,
                              X                  ⋆              X                  ⋆
                     u=             uJ,K ζJ⋆ ∧ ζ K ,      v=          vJ,K ζJ⋆ ∧ ζ K
where summations are extended to increasing multi-indices J, K such that |J| = p,
|K| = q. With respect to ω we have hζj⋆ , ζj⋆ i = λ−1
                                                   j , hence
                    X
        hu, vi dV =   λ−1  −1
                        J λK uJ,K v J,K λ1 · · · λn dV0
                       J,K
                       X         X            X             X        
                   =         1−         γj −         γj +           γj uJ,K v J,K dV0 + O(|z|2 ).
                       J,K        j∈J          j∈K          1⩽j⩽n
308                                                Chapter VI. Hodge Theory

Lemma 6.9 follows if we take Prop. 5.8 into account.                                    
                                         
(6.10) Lemma. d′′⋆ = d′′⋆           ′′⋆
                         0 + Λ0 , [d0 , γ] at point x0 , i.e. at this point both operators
have the same formal expansion.
Proof. Since d′′⋆ is an operator of order 1, Lemma 6.9 shows that d′′⋆ coincides at point
x0 with the formal adjoint of d′′ for the metric
                                        Z
                            hhu, vii1 =   hu − [γ, Λ0 ]u, vi0 dV0 .
                                            X

For any compactly supported u ∈ C∞ (X, Λp,q TX       ⋆
                                                       ), v ∈ C∞ (X, Λp,q−1 TX   ⋆
                                                                                   ) we get by
definition
                       Z                             Z
               ′′                         ′′
         hhu, d vii1 =   hu − [γ, Λ0 ]u, d vi0 dV0 =     hd′′⋆    ′′⋆
                                                           0 u − d0 [γ, Λ0 ]u, vi0 dV0 .
                         X                                 X

Since ω and ω0 coincide at point x0 and since γ(x0 ) = 0 we obtain at this point
                                                                 ′′⋆            
                 d′′⋆ u = d′′⋆
                           0   u − d ′′⋆
                                     0   [γ, Λ0 ]u  = d ′′⋆
                                                        0   u −  d 0  , [γ, Λ0 ]  u;
                    ′′⋆    ′′⋆
                                   ′′⋆           
                   d = d0 − d0 , [γ, Λ0 ] .

We have [Λ0 , d′′⋆     ′′     ⋆              ′′
               0 ] = [d , L0 ] = 0 since d ω0 = 0. The Jacobi identity (5.7) implies
                               ′′⋆                       
                                d0 , [γ, Λ0] + Λ0 , [d′′⋆
                                                      0 , γ] = 0,


## Exact retrieved printed primary passages: Bedford-Taylor-new-capacity

Text SHA256: d32eb9305e1cfbcc569746d51d53e417508b33aba0e3b5a1a706036cb0593115; corresponding PDF SHA256: e75ea91e48c14a9838a800aee25b68ed04169c4372f2ce4b399967b53005b758.


### Actual text lines 50--310

The operators (1.1) and (1.2) are clearly related, but the complex Monge-Amp~re
operator (ddr " seems better suited to the purpose of potential theory. In fact, the
Dirichlet problem was shown in [4] to be well posed for (ddC) " and examples were
given to show certain difficulties with (1.1). Here, we will use the operator (dd~)~ to
replace the Laplacian and prove, in the category of complex analysis, the analogues of
some well known results of classical real potential theory. Since our arguments
completely avoid the explicit use of kernels and convolutions, they may in some cases
also give new proofs to classical results in the case n= 1.
    As in [4], we may define

                           (dd~)": P(g2) n L=(~, loc)---~ M,,,(f2)

where M,,,(f2) denotes the space of (n, n) forms on Q with (Bored measure coeffi-
cients, with the usual topology of weak convergence of measures. Our first main result,
Theorem 2.1, shows that this is actually an extension of the operator (ddC) ~ on smooth
functions. The case n=2 was proved differently in [5]. It is known [27] that the operator
(da~)" cannot be defined as an element of M , , , ( ~ ) for all u6P(~2). The "correct"
domain of definition for (daY)" still seems not to be known.
     Several capacities have been introduced in connection with various problems of
analytic function theory (see e.g., [1], [10], [22], [25], [26], [28]). And it seems, in
contrast to the case of C ~, that there may be a large number of different capacities,
each arising naturally from a different problem. For the situation at hand, the natural
capacity is

                    C(K,fZ)=sup{f,(d,ev)":vEP(g2), 0 < v < 1}                       (1.3)


where K c s   is compact. This has the property of decreasing under holomorphic
mappings; i.e. iff." f21-->Q2 is holomorphic, then

                                 C(K, g2~) >i C(f(K), ~')2)"

Our second main result, Theorem 3.5, is that every u EP(ff2) is quasicontinuous with
respect to this capacity. That is, for each ufiP(Q) and each e>0, there is an open set
Ocg2 such that C(C, f2)<e and u is continuous on the complement of G. For subhar-
monic functions, this theorem is due to H. Cartan [9].
   The usefulness of (ddC)" in replacing the Laplacian is reflected in the comparison
theorems we may obtain using it. For instance, we derive a domination principle,
Corollary 4.5, analogous to the one known in classical potential theory.
                   A N E W CAPACITY FOR P L U R I S U B H A R M O N I C F U N C T I O N S



  We also consider the capacitary plurisubharmonic function u~:, the upper semicon-
tinuous regularization of the envelope

                        UE=sup{v: vfiP(Q), v < 0 , v~<--I on E}.
The extremal function u~: is used to give the connection between the capacity C(E, if2)
and the pluripolar sets; i.e. sets which are locally contained in sets of the form {v = - ~ }
for some plurisubharmonic function v. With Theorems 2. I and 3.5 it is possible to give
a simpler proof of the characterization given in [2] and [3],

                                       C(K, if2)= f (ddCu~:)"                                     (1

for K a compact subset of if2. For (1.4), we assume there is a Stein manifold M with
ff2={Q<0}9      for some strictly plurisubharmonic ~) on M. However, since all the
interesting aspects of our work are local, we will assume that if2 is a bounded, strongly
pseudoconvex domain in C n. In fact, we may always take ~2={z6C": M<R}. The
corresponding statements for Stein manifolds will be obvious, and they are omitted.
    We also extend the arguments of [2] and [3] to show in Theorem 6.9 that the sets of
outer capacity zero are precisely the pluripolar sets. This then gives another proof of
Josefson's theorem [17] on the equivalence of locally and globally pluripolar sets.
     We consider also the so-called negligible sets, which are those of the form

                                             N={w<w*}
where w=supau~ is the upper envelope of an arbitrary family of plurisubharmonic
functions locally bounded above, and w*(z)=lim supr                       w(~) is its upper semicontin-
uous regularization.      In    [2] and        [3] it was          shown that 2r is pluripolar if
{u~} cP(Q) n C(f2). Here we extend this result to the general case and show in Theorem
7.1 that the negligible sets are pluripolar. As a consequence, we find that the capacity
defined in (1.3) satisfies the hypotheses of a generalized capacity, and so by Choquet's
theorem the Y{-analytic sets are capacitable. Another consequence is that monotone
sequences in P(Q) are "quasi-uniform" (Theorem 7.2). These results are then applied
to some questions of stability i n the interior Dirichlet problem for (ddC)", and to give
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
    The operators
                                    ~Lt'k:[P(Q) fl L=(f2, loc)] k+L-+Mk. k(f2)
given by
                                  ~k(V ~ V1..... Vk) = v~          ^ ... ^ ddCv k

which appeared in the proof of Theorem 2.1 are equally as important as (ddC) k. Of
course, from (2.1), convergence of the currents d d ~ v~ ^ ... ^ ddCv~ is equivalent to the
convergence of ~k(V ~ . . . . . V~) on test forms of the type dd~0. However, the 5fk'S
themselves also converge under decreasing limits and this was, essentially, already
shown in the proof of Theorem 2.1.



## Exact retrieved printed primary passages: BGL-volumes-2406.01090

Text SHA256: aae1614a02599db630e74120e35c5dcd90a7c12782ef366d6f25021e672ee1e1; corresponding PDF SHA256: d7637564a1b1b728743bc5ae315c336097139d12ebca9f43469d721947f8f031.


### Actual text lines 493--650

Definition 1.18. We define the upper volume of ωX as
                                    ˆ
                     vol(ωX ) := sup (ωX + ddc φ)n ∈ [0, +∞],
                                       φ    X

where φ ranges over all smooth ωX -psh functions.
                             VOLUMES OF BOTT–CHERN CLASSES                                  11

   The above supremum is unchanged if φ ranges instead over all bounded ωX -psh functions,
since any such φ is a decreasing limit of smooth ωX -psh functions φj (by Theorem 1.8), and
                             ˆ                   ˆ
                                (ω + ddc φj )n →   (ω + ddc φ)n
                              X                         X
by continuity of Bedford–Taylor products along decreasing sequences.
                                ′ satisfies C −1 ω     ′
  Any other Hermitian form ωX                     X ≤ ωX ≤ CωX for some C > 0, which
         −1                    ′
implies C PSH(ωX ) ⊂ PSH(ωX ) ⊂ C PSH(ωX ), and hence
                                                ′
                           C −n vol(ωX ) ≤ vol(ωX ) ≤ C n vol(ωX ).
We may thus introduce:
Definition 1.19. Let X be compact complex manifold. We say that X has the bounded
mass property if vol(ωX ) is finite for some (hence any) Hermitian form ωX .
  The following properties are straightforward:
                                                      p
     • the bounded mass property holds whenever ddc ωX  = 0 for all p (which, as is well-
       known, follows from the case p = 1, 2);
     • it is inherited by any holomorphic image of X.
In particular, the bounded mass property holds whenever n ≤ 2 (using a Gauduchon met-
ric ωX ), and also when X is a Fujiki manifold (i.e. bimeromorphic to a compact Kähler
manifold).
   By [AGL23, Theorem A] and [GL22, Theorem 3.7], we further have:
Proposition 1.20. The bounded mass property is inherited by complex submanifolds, and
is bimeromorphically invariant.
   In dimension n = 3, the bounded mass property is known to hold in the following cases
(see [AGL23]):
     • there exists a Hermitian form ωX with ddc ωX ≥ 0;
     • for ‘most’ complex nilmanifolds;
     • for the twistor space of a compact antiselfdual 4-manifold.
At the time of this writing, we do not know any example where the bounded mass property
fails, and it is an intriguing problem whether it always holds. For instance:
Example 1.21. Does the Hopf manifold X = (Cn \ {0})/2Z of dimension n ≥ 3 have the
bounded mass property? See [AGL23, §3.4.2] for a discussion.

                              2. Non-pluripolar products
  As before, X denotes a compact complex manifold, of complex dimension n, endowed
with a reference Hermitian form ωX . We show that the bounded mass property yields a
notion of non-pluripolar products of quasi-closed, quasi-positive currents, and extend to this
context some basic properties of non-pluripolar masses.

2.1. Products of currents with bounded potentials. For any p = 1, . . . , n, the classical
work of Bedford–Taylor [BT87] extends the operator
                             (φ1 , . . . , φp ) 7→ ddc φ1 ∧ · · · ∧ ddc φp
12                 SÉBASTIEN BOUCKSOM, VINCENT GUEDJ, AND CHINH H. LU

from tuples of (locally defined) smooth psh functions to bounded ones, with values in closed
positive (p, p)-currents that are nonpluripolar, in the sense that they put no mass on pluripo-
lar sets. This operator is symmetric and multilinear, continuous along decreasing sequences,
and further has the key property of being local in the plurifine topology (see §1.2).
   Since any quasi-psh function is locally the sum of a psh function and a smooth function,
these results readily extend to tuples of bounded quasi-psh functions φ1 , . . . , φp , the closed
(p, p)-current ddc φ1 ∧ · · · ∧ ddc φp being now merely of order 0 (i.e. with signed measures as
local coefficients), and still nonpluripolar.
   More generally, given arbitrary (1, 1)-forms θ1 , . . . , θp , we define an operator
                                                         ^
                                    (φ1 , . . . , φp ) 7→ (θi + ddc φi )                     (2.1)
                                                        i
on tuples of bounded quasi-psh functions by forcing multilinearity, i.e.
                          p
                          ^                           X         ^          ^
                              (θi + ddc φi ) :=                     θi ∧         ddc φi .     (2.2)
                          i=1                     I⊂{1,...,p} i∈I          i∈I
                                                                            /

This formula shows that the operator (2.1) is still local in the plurifine topology. As the
notation suggests, one easily checks that (2.2) only depends on the currents Ti = θi + ddc φi ,
and yields a symmetric, multilinear pairing
                                   (T1 , . . . , Tp ) 7→ T1 ∧ · · · ∧ Tp                      (2.3)
from tuples of quasi-closed, quasi-positive currents with bounded potentials to nonpluripolar
(p, p)-currents. We next extend this as follows:
Proposition 2.1. For any compact subset K ⊂ X, there exists a unique symmetric, multi-
linear pairing
                                 (T1 , . . . , Tp ) 7→ 1K T1 ∧ · · · ∧ Tp
defined on tuples of quasi-closed, quasi-positive currents with bounded potentials on K and
with values in nonpluripolar (p, p)-currents, such that:
     (i) when the Ti ’s have bounded potentials, the pairing is compatible with (2.3);
    (ii) for any tuple of (1, 1)-forms θ1 , . . . , θp , the operator
                                                          ^
                                (φ1 , . . . , φp ) 7→ 1K (θi + ddc φi ),
                                                            i
      acting on tuples of quasi-psh functions bounded on K is local in the plurifine topology.
Moreover, the construction is compatible with restriction, i.e.
                            1L T1 ∧ · · · ∧ Tp = 1L (1K T1 ∧ · · · ∧ Tp )                     (2.4)
for any compact subset L ⊂ K, and we further have
                            T1 , . . . , Tp ≥ 0 =⇒ 1K T1 ∧ · · · ∧ Tp ≥ 0.                    (2.5)
  We emphasize that the notation 1K T1 ∧ · · · ∧ Tp above should be taken as a whole, i.e.
we do not try to make sense of T1 ∧ · · · ∧ Tp itself (see however Theorem 2.2 below).
Proof. Pick (1, 1)-forms θ1 , . . . , θp and quasi-psh functions φ1 , . . . , φp that are bounded on
K. The latter is then contained in the plurifine open subset
                                               \
                                          O := {φi > −t0 }
                                                  i
                                   VOLUMES OF BOTT–CHERN CLASSES                                                    13

for some t0 . For any t ≥ t0 and i = 1, . . . , p, the bounded quasi-psh function max{φi , −t}
coincides with φi on O. By (i), (ii), we thus necessarily have
                        ^                         ^
                     1K (θi + ddc φi ) = 1K (θi + ddc max{φi , −t}),                     (2.6)
                              i                            i
for t large enough, where the right-hand side was defined above (in the sense of Bedford–
Taylor). This proves uniqueness. To get existence, we use (2.6) as a definition, and first
check that it only depends on the quasi-closed, quasi-positive currents Ti = θi + ddc φi ,
i = 1, . . . , p. Any other decomposition of Ti is of the form
                                     Ti = (θi + ddc τi ) + ddc (φi − τi )
with τi ∈ C ∞ (X) (see Lemma 1.4). For t large enough, the bounded quasi-psh functions
                                  max{φi − τi , −t},           max{φi , −t} − τi
are both equal to φi − τi on the plurifine open O. By plurifine locality, this yields
   ^                                                ^
1K    ((θi + ddc τi ) + ddc max{φi − τi , −t}) = 1K   ((θi + ddc τi ) + ddc (max{φi , −t} − τi )) ,
    i                                                     i
                                                     c
                                       V
which coincides in turn with 1K            i (θi + dd max{φi , −t}). By (2.6) we infer
                     ^                                        ^
                  1K    ((θi + ddc τi ) + ddc (φi − τi )) = 1K (θi + ddc φi ),
                          i                                                 i
which proves, as desired, that this current only depends on the Ti ’s. Similar considerations
shows that 1K T1 ∧ · · · ∧ Tp is a multilinear function of the Ti . Symmetry is trivial, and (2.4)
holds by uniqueness.
  The proof of (2.5) is slightly more involved. Assume Ti ≥ 0 for all i. Since
                                            1K T1 ∧ · · · ∧ Tp ≥ 0
is a local property, it is enough to argue in a small open neighborhood Ω of a given point of
X, on which we can thus find a Kähler form ω = ddc ρ with ρ smooth and bounded. Pick
ε > 0. By Lemma 1.5, each point of Ω admits an open neighborhood U ⊂ Ω (depending on
ε) and closed (1, 1)-forms θi′ on U such that −εω ≤ θi − θi′ ≤ εω on U . After shrinking U ,
we further assume θi′ = ddc τi with τi smooth and bounded on U . Then
                     ddc (τi + ερ + φi ) = θi′ + εω + ddc φi ≥ θi + ddc φi ≥ 0,
and hence τi + ερ + φi is psh on U . For each t > 0, max{τi + ερ + φi , −t} is thus psh
and bounded on U , and it further coincides with the bounded quasi-psh function τi + ερ +
max{φi , −t} on the plurifine open O ∩U for t large enough. By plurifine locality of Bedford–
Taylor products, we get for each I ⊂ {1, . . . , p}
                  ^                                 ^
                       θi′ + εω + ddc φi = 1K∩U       ddc (τi + ερ + max{φi , −t})
                                        
            1K∩U
                    i∈I                                        i∈I
                                        ^
                              = 1K∩U          ddc max{τi + ερ + φi , −t} ≥ 0.
                                        i∈I
Since θi + εω ≥ θi′ on U , we infer
        p
        ^                                X                 ^                              ^
 1K∩U       (θi + 2εω + ddc φi ) =                  1K∩U         (θi′ + εω + ddc φi ) ∧         (θi + εω − θi′ ) ≥ 0.
        i=1                           I⊂{1,...,p}          i∈I                            i∈I
                                                                                           /


## ENTIRE settled public independent I reconstruction

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "Uniform pole contact and exact right-end geometry: moving contacts still give |R_sigma|<=1 and |sigma R_sigmasigma|<=5/4.",
      "detailedSummary": "For every allowed obstacle, one left cutoff depends only on alpha,a,b,M. On x>b the gap is empty, one tangent segment ending at t, or one affine slope-one tail. The finite-contact slope defect is q B'(q), q=exp(-t). Explicit scalar formulas and weighted derivative bounds cover arbitrarily large t and changes between the right-end alternatives. These are analytic proofs using the imported full-envelope and convex-profile results.",
      "text": "Uniform radial lemmas for target I. Preserve D=i partial barpartial/(2pi), the standard normalized Fubini--Study kappa, genuine canonical potentials, and the FULL ordinary everywhere obstacle envelope. Write a0(x)=log(1+exp x), A=a0+psi, f_F=A+F, and C_F for the whole-line largest convex minorant. Imported supplied:n2 gives 0<A'<1, A''>0 and A''<=B_alpha=1/4+alpha(1-alpha), with the stated canonical ends. Imported supplied:n3 gives C_F in C^{1,1}, 0<=C_F'<=1 and 0<=C_F''<=sup max(f_F'',0) almost everywhere. Imported supplied:n4 identifies the envelope over all competitors with C_F-a0 and its genuine residual off the pole with R_F=C_F-A. The original competitor family is not restricted to radial functions.\n\nAssume a<b; if a=b, a continuous function supported at that point is zero and I is immediate. The family condition implies ||F||_infinity<=M and ||F''||_infinity<=M. Therefore\n|R_F|<=M, |R_F'|<=1, |R_F''|<=W:=2B_alpha+M almost everywhere. (1)\nThese are x derivatives. The first bound follows from A-||F||<=C_F<=A+F; the derivative bounds follow from the imported convex estimates. No third derivative bound is used.\n\nChoose once t_-<min(a,0) such that\nA(t_-)+A'(t_-)(b-t_-)<=A(a)-M. (2)\nSuch a choice exists: the left asymptotics give A(t)-tA'(t)=-(1-alpha)(1-t)^alpha+O(1), while bA'(t) tends to zero. For t<=t_-, the tangent ell_t(x)=A(t)+A'(t)(x-t) satisfies ell_t(b)<=ell_{t_-}(b), because differentiation in t gives A''(t)(b-t)>0 for t<b. On [a,b], ell_t(x)<=ell_t(b)<=A(a)-M<=A(x)+F(x). Outside [a,b], ell_t<=A=f_F by convexity. Thus ell_t is a whole-line admissible affine minorant. Since F(t)=0, C_F(t)=A(t) for every t<=t_-. Consequently every residual is exactly zero on one common neighborhood of the genuine pole. This cutoff depends only on alpha,a,b,M.\n\nClassify the right region x>b, where f_F=A. Every strict-gap component is affine, and finite endpoints are contact points with matching derivatives. A finite gap with both endpoints >=b would be the chord of strictly convex A and hence strictly above A internally, a contradiction. An infinite gap with left endpoint >=b would have slope one by the end slope, contradicting derivative matching with A'<1. There cannot be two components meeting (b,infinity), since the later one would have left endpoint >=b. Therefore either C_F=A throughout (b,infinity), or the gap there is (b,t) for some finite t>b followed by C_F=A, or the gap is all of (b,infinity) and C_F=x+L. In the last case L=inf(f_F-x), with -M<=L<=0, by supplied:n3. In the finite case the affine segment is tangent to A at t. No assumption about the number of other free intervals is needed.\n\nSet sigma=exp(-x) and\nB(sigma)=log(1+sigma)+1-(1+log(1+sigma))^alpha,\nso A(x)=x+B(exp(-x)). B is smooth on [0,infinity), B(0)=0 and B'(0)=1-alpha. With u=1+sigma and T=1+log u, direct differentiation gives\nB'=(1-alpha T^{alpha-1})/u,\nB''=(-1+alpha T^{alpha-1}+alpha(1-alpha)T^{alpha-2})/u^2.\nThe numerator of B'' lies between -1 and -(1-alpha)^2. Hence\n0<B'<=1/u<=1, -1/u^2<=B''<0, sigma|B''|<=1/4. (3)\nAlso sigma B'(sigma)=1-A'(-log sigma) is strictly increasing: its derivative is A''(-log sigma)/sigma>0.\n\nFor a finite contact t let q=exp(-t) and d=1-A'(t)=qB'(q). The actual extended residual on 0<=sigma<exp(-b) is\nR_F(sigma)=0 for 0<=sigma<=q,\nR_F(sigma)=B(q)+d log(sigma/q)-B(sigma) for q<sigma<exp(-b). (4)\nValues and first derivatives match at q. This follows directly from the tangent A(t)+A'(t)(x-t), with x-t=log(q/sigma). In the affine-tail case,\nR_F(sigma)=L-B(sigma), including sigma=0. (5)\nIn the no-gap case it is zero.\n\nOn the free part of (4), monotonicity of sigma B' gives 0<=d/sigma<=B'(sigma). Thus\nR_sigma=d/sigma-B'(sigma),\nsigma R_sigmasigma=-d/sigma-sigma B''(sigma).\nTogether with (3), all alternatives satisfy\n|R_sigma|<=1, |sigma R_sigmasigma|<=5/4 almost everywhere. (6)\nThe contact part is zero; (5) satisfies these bounds with d=0. Each scalar residual is C^1 through its finite cutoff. Its infinity value R_infinity is zero in (4) and L in (5), and integration gives\n|R_F(sigma)-R_infinity|<=sigma. (7)\nThese weighted scalar estimates control projective derivatives without bounding the contact location or R_sigmasigma itself. They include the L=0 attained transition.\n\nArtifacts are in /workspace/research/native-workers/codex-lLr5le. input.json contains the exact assignment; imported_notes.md preserves the supplied texts. Run python compose_notes.py to regenerate notes.json and proof_notes.md. This argument is analytic and uses no numerical output. It remains an unverified proof draft.\n\nArtifacts: /workspace/research/native-workers/codex-lLr5le",
      "support": [
        "supplied:n2",
        "supplied:n3",
        "supplied:n4"
      ]
    },
    {
      "id": "n2",
      "summary": "Target I's uniform global C^{1,1} bound proved in a fixed projective atlas, including explicit derivative bounds through both ends.",
      "detailedSummary": "A fixed chart norm admits K=M+U+H with explicit constants depending only on the prescribed parameters. The infinity Hessian is bounded by 22 on the larger charts independently of contact locations. Normal gradients vanish uniformly at infinity, tangential gradients vanish quadratically, and the residual is zero on a common pole neighborhood. Weak Hessian bounds give the global Lipschitz-gradient estimate.",
      "text": "Uniform global C^{1,1} proof. Use n1 with W=2B_alpha+M and its fixed t_-. Specify the atlas and norm. In projective chart Z_j!=0 let W_j be the coordinate polydisc where every ratio Z_i/Z_j, i!=j, has modulus <2. Let V_j have all these moduli <3/2. The V_j cover P^k, since choosing a largest homogeneous coordinate makes every ratio <=1. Their closures lie in W_j. Use real Euclidean gradient norms and Hessian operator norms, and define\n||u||_{C^{1,1}}=||u||_infinity+max_j sup_{V_j}|Du_j|+max_j Lip_{V_j}(Du_j). (8)\nOther fixed finite smooth projective atlas norms differ by fixed comparison constants. We establish bounds on the larger W_j.\n\nOn W_0 use z_i=Z_i/Z_0 and x=log|z|^2. Every residual is exactly zero for x<=t_-, including z=0. For x>t_-,\n|Dx|=2/|z|<=2 exp(-t_-/2), ||D^2x||=2/|z|^2<=2 exp(-t_-).\nThe chain rule and n1(1) give\n|DR_F|<=U_0:=2 exp(-t_-/2),\n||D^2R_F||<=H_0:=(4W+2)exp(-t_-) almost everywhere. (9)\nThe zero extension crosses the genuine pole without subtracting two infinite values.\n\nFor j>=1 write tau=Z_0/Z_j, xi=(Z_i/Z_j)_{i!=0,j}, and S=1+|xi|^2. Away from tau=0,\nx=log S-log|tau|^2, sigma=|tau|^2/S.\nWhere x<=b, |tau|^2>=S exp(-b), and real block differentiation gives\n|Dx|^2=4/|tau|^2+4|xi|^2/S^2<=4exp(b)+1,\n||D^2x||<=2 max(exp(b),1).\nConsequently\n|DR_F|<=U_c:=sqrt(4exp(b)+1),\n||D^2R_F||<=H_c:=W(4exp(b)+1)+2 max(exp(b),1) almost everywhere. (10)\nThese estimates include arbitrary finite free boundaries, including accumulating components, through the uniform Lipschitz bound of C_F'. They do not assert continuous second derivatives at a free boundary.\n\nWhere x>b, use n1(6). On W_j, |tau|<2 and sigma<=4. Direct differentiation gives\n|D sigma|^2=4sigma/S+4sigma^2|xi|^2/S^2<=4sigma+sigma^2<=8sigma,\n||D^2 sigma||<=12. (11)\nFor the latter bound put g=1/S. Its real gradient has norm <=1 and its real Hessian has norm <=2: the tangential eigenvalue is -2/S^2 and the radial eigenvalue is (-2+6|xi|^2)/S^3, both bounded in absolute value by 2. The tau-tau block of D^2sigma has norm <=2, the xi-xi block <=2|tau|^2<=8, and the cross block <=2|tau|<=4. The diagonal matrix has norm <=8 and the off-diagonal matrix <=4, proving 12.\n\nThus\n|DR_F|<=sqrt(8sigma)<=2sqrt(2)|tau|<=U_infinity:=4sqrt(2),\n||D^2R_F||<=12+8(5/4)=H_infinity:=22 almost everywhere. (12)\nThese constants contain no contact location or inverse contact radius. More precisely,\n|D_tau R_F|<=2|tau|/S<=2|tau|,\n|D_xi R_F|<=2sigma|xi|/S<=sigma,\n|R_F-R_infinity|<=sigma<=|tau|^2. (13)\nAll first derivatives therefore extend continuously as zero on the infinity hyperplane.\n\nEach individual residual is smooth near infinity. In the finite-contact or no-gap case it is zero there. In the affine-tail case it is L-B(|tau|^2/S). At tau=0 its real normal Hessian is exactly -2(1-alpha)S^{-1}I_2, and its tangential and mixed Hessian blocks are zero. In the other alternative every block is zero. Both obey (12). At the pole every derivative is zero on the common neighborhood.\n\nSet\nU=max(U_0,U_c,4sqrt(2)),\nH=max(H_0,H_c,22),\nK=M+U+H. (14)\nThe canonical formulas and profile regularity in n1 give a continuous, locally Lipschitz gradient. Equations (9)--(12) uniformly bound its weak Hessian almost everywhere on each convex W_j. A continuous locally Lipschitz field with weak derivative norm <=H on a convex domain is H-Lipschitz: mollify around a compact segment, integrate the derivative estimate along that segment, and pass to the continuous limit. This avoids exceptional-line issues with almost-everywhere Hessians. Therefore Lip_{W_j}DR_F<=H, and (8) yields ||R_F||_{C^{1,1}}<=K for every allowed F.\n\nAll constants are finite and depend only on alpha,a,b,M through n1's fixed choice of t_-. Dependence on k or another fixed atlas enters only through fixed norm comparisons. There is no uniform right cutoff assumption, no third derivative hypothesis, and no closed minimal-type uniqueness argument. This proves the first assertion of I globally.\n\nArtifacts: notes.json and proof_notes.md contain the proof and constants. Run python compose_notes.py to regenerate them, and python verify.py for the separate finite diagnostics in artifacts/check_output.json. The bound 22 is analytic, not fitted from those diagnostics.\n\nArtifacts: /workspace/research/native-workers/codex-lLr5le",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "Target I's C^{1,gamma} stability proved with exponent (1-gamma)/2 for every 0<gamma<1.",
      "detailedSummary": "Constant-one C^0 stability combines with the uniform Hessian bound on larger charts. Taylor's formula gives a gradient bound proportional to sqrt(delta). Interpolation between gradient amplitude and Lipschitz bounds gives the stated Hölder exponent with an explicit K_gamma. Both end-alternative transitions and canonical extensions are included; C^{1,1} convergence is not inferred.",
      "text": "Global interpolation proof. Let u=R_F-R_G and delta=||F-G||_infinity<=1. Imported supplied:n4 gives ||u||_infinity<=delta for the actual canonically extended residuals, including their pole and infinity values. Its whole-line convex-minorant proof uses monotonicity and commutation with constants, and applies to every pair in this family. If delta=0, the residuals coincide.\n\nUse the larger W_j and smaller V_j of n2, with H from n2(14). The chart gradient of u has Lipschitz constant <=2H on W_j. If p belongs to V_j, e is a real unit vector, and 0<h<=r_0:=1/4, the segment p+[0,h]e lies in W_j. Taylor's formula gives\n|u(p+he)-u(p)-h Du(p).e|<=Hh^2.\nBoth function values have absolute value <=delta, hence\n|Du(p).e|<=2delta/h+Hh.\nChoose h=r_0 sqrt(delta) and maximize over e:\nsup_{V_j}|Du|<=A_*sqrt(delta), A_*:=8+H/4. (15)\nThe chart margin makes this valid even near the boundaries of V_j.\n\nFor p,q in V_j, convexity and the Lipschitz-gradient bound yield\n|Du(p)-Du(q)|<=min(2A_*sqrt(delta),2H|p-q|).\nSince min(s,t)<=s^{1-gamma}t^gamma for positive s,t and 0<gamma<1,\n[Du]_{C^{0,gamma}(V_j)}<=(2A_*)^{1-gamma}(2H)^gamma delta^{(1-gamma)/2}. (16)\nDefine the fixed-atlas C^{1,gamma} norm as sup|u| plus the maximum chart gradient sup and maximum chart gradient gamma seminorm. Because delta<=1, delta and sqrt(delta) are each <=delta^{(1-gamma)/2}. Thus\nK_gamma=1+A_*+(2A_*)^{1-gamma}(2H)^gamma (17)\nsatisfies\n||R_F-R_G||_{C^{1,gamma}}<=K_gamma delta^{(1-gamma)/2}.\nA different fixed finite smooth projective atlas introduces only fixed norm-comparison constants. The parameter dependence is exactly the allowed dependence on k,alpha,a,b,M and gamma, with the atlas fixed.\n\nThe argument uses actual global C^0 and C^{1,1} bounds, so it includes crossing the genuine pole and infinity hyperplane and every change of right-end alternative. No contact cutoff appears. It proves the second assertion of I for every pair and every 0<gamma<1. Uniform Hessian boundedness does not imply small Hessian differences, so C^{1,1} convergence is not claimed.\n\nArtifacts: regenerate notes.json and proof_notes.md with python compose_notes.py. This interpolation proof uses no numerical observations.\n\nArtifacts: /workspace/research/native-workers/codex-lLr5le",
      "support": [
        "n2",
        "supplied:n4"
      ]
    },
    {
      "id": "n4",
      "summary": "Both estimates extend to the full ordinary envelope on every fixed compact positive Hermitian product, including nonclosed examples.",
      "detailedSummary": "A vertical quadratic gives canonical slice restrictions with the exact horizontal kappa bound. Thus all H-psh competitors lie below the pulled-back base envelope, without Y symmetry or closedness. The residual is the pullback of R_F, with zero vertical derivatives and controlled extension across the pole fiber and infinity divisor. Product charts retain the bounds; other fixed atlases add geometry constants.",
      "text": "Product extension of I. Fix any connected compact complex m-fold Y with smooth positive Hermitian form h0. Put X=P^k times Y and H=pi^*kappa+pr_Y^*h0. This is positive and big in the exact definition, with rho=0, epsilon=1 and h=H. Closedness is not assumed. Pull back the stated reference and each allowed F, and retain the full everywhere ordinary obstacle operator.\n\nThese hypotheses match supplied:n6. The canonical restriction argument also checks the indispensable all-competitor condition directly. For a genuine H-psh competitor v, choose a product coordinate box, a smooth local kappa-potential b(z), and vertical coordinates w. Choose c>0 with h0<=cD|w|^2 there. Then the genuine representative v+b(z)+c|w|^2 is psh, since\nD[v+b+c|w|^2]>=cD|w|^2-h0>=0.\nCanonical holomorphic restriction of psh functions, from supplied:n1, gives a psh restriction to w=w0 or the identically minus-infinity restriction. The vertical quadratic becomes constant, leaving exactly kappa+D_z v(.,w0)>=0. There is no horizontal error and no local potential for nonclosed h0 is needed. The local restrictions glue; connectedness propagates the genuine or identically minus-infinity alternative across P^k.\n\nEvery nontrivial slice satisfies v(.,w0)<=psi+F everywhere and v(.,w0) preceq psi with the inherited order constant. It is therefore a competitor for the full base envelope and lies below E_F pointwise, including canonical pole values. Identically minus-infinity slices do also. Thus every product competitor is <=pi^*E_F. Conversely pi^*E_F is genuine and admissible because\nH+D pi^*E_F=pi^*(kappa+DE_F)+pr_Y^*h0>=0,\nand it satisfies the obstacle and ordinary order. Hence E_F^H=pi^*E_F with the canonical global representatives, as in supplied:n6.\n\nThe retained residual is R_F^H=pi^*R_F, with its forced value zero on {0} times Y. Choose a fixed finite smooth atlas of Y with nested precompact domains and form product charts with n2's W_j,V_j. Vertical first and second derivatives vanish; horizontal derivatives are exactly those of R_F. The C^{1,1} estimate of n2 therefore holds in product chart norms. For n3's Hölder seminorm, product Euclidean distance is at least horizontal distance, so vertical changes cannot enlarge it. Both estimates hold with the same constants in these product norms. Any other fixed atlas or metric introduces only fixed geometry constants, as allowed in I.\n\nThere is a common neighborhood {x<=t_-} times Y where every residual and all its derivatives vanish. Across the infinity hyperplane times Y, the actual value is R_infinity, every first derivative vanishes, vertical derivatives vanish, and the horizontal derivative estimates and Hessian alternatives are exactly n2(12)--(13). This establishes actual crossing of both geometric sets for the full nonclosed operator.\n\nIn particular the conclusion applies to P^2 times the standard Hopf surface from supplied:n7, whose specified h0 is positive and nonclosed and whose product is non-Kahler. No lower-mass property, BMP, Y symmetry or closed-class uniqueness is used. Existing actual-mass results are unchanged. The exact stretching certificate can also be retained: handle t=1 separately with a=E_F^H, avoiding 0 times minus infinity. For t>1 choose a_t=psi-t||F||_infinity. Then t^{-1}a_t+(1-t^{-1})psi=psi-||F||_infinity<=E_F^H with genuine pole values. These are direct witnesses for the supplied E_env definition.\n\nArtifacts: python compose_notes.py regenerates proof_notes.md and notes.json. input.json contains the imported canonical-slice and Hopf proofs. The new derivative estimates follow analytically from n2 and n3.\n\nArtifacts: /workspace/research/native-workers/codex-lLr5le",
      "support": [
        "n1",
        "n2",
        "n3",
        "supplied:n1",
        "supplied:n6",
        "supplied:n7"
      ]
    },
    {
      "id": "n5",
      "summary": "One controlled family provably has contact cutoffs tending to infinity and changes its right-end alternative; lightweight numerical diagnostics are consistent with the formulas.",
      "detailedSummary": "The C^2 bump chi=(1-x^2)^3 on [-1,1] satisfies ||chi||+||chi''||=7. A critical lambda_c in (0,1) separates zero-unattained L, zero-attained L, and negative L. Finite right contacts tend to infinity below the critical value, while above it an actual affine zero-density tail occurs. Numerical estimates for alpha=0.6 illustrate this behavior but are uncertified observations.",
      "text": "A changing-end family inside fixed parameters. Fix any 0<alpha<1 and k>=2, take [a,b]=[-1,1] and M=7, and define chi(x)=(1-x^2)^3 for |x|<1 and zero otherwise. Let F_lambda=-lambda chi, 0<=lambda<=1. The boundary values of chi, chi' and chi'' vanish, so chi is C^2 with the required support. Internally chi''=-6+36x^2-30x^4, whose minimum is -6 and maximum 24/5. Therefore ||chi||=1, ||chi''||=6 and ||F_lambda||+||F_lambda''||=7lambda<=7.\n\nUsing B from n1, define the exact number lambda_c=min_{-1<x<1} B(exp(-x))/chi(x). The positive ratio tends to infinity at both endpoints, so its minimum is attained at an interior y and is positive. At x=0 the ratio is B(1)<log 2<1, hence 0<lambda_c<1. For lambda<lambda_c, f_lambda-x is strictly positive everywhere and tends to zero at plus infinity: L=0 is unattained. At lambda=lambda_c it is nonnegative and vanishes at y: L=0 is attained. For lambda>lambda_c it is negative at y: L<0 is attained. Thus all right-end alternatives occur in this one controlled family. Supplied:n3 gives C_c(x)=x for x>=y and an affine right tail above the critical value. Supplied:n5 identifies an open part of that latter tail as an actual zero-density region. The uniform residual estimates apply there and through its finite free boundaries.\n\nThe finite right cutoff tends to infinity as lambda increases to lambda_c from below. Supplied:n4 gives ||C_lambda-C_c||_infinity<=lambda_c-lambda. For any fixed T>1, A(T)-T=B(exp(-T))>0. If 0<lambda_c-lambda<B(exp(-T)), then C_lambda(T)<=T+(lambda_c-lambda)<A(T). Thus T belongs to the right gap. The zero-unattained alternative supplies a finite right cutoff t_lambda, and n1's classification gives t_lambda>T. Since T is arbitrary, t_lambda tends to infinity. This analytic example verifies that the difficult family quantifier is nonvacuous.\n\nReproducible observations: run python verify.py > artifacts/check_output.log. The standard-library script saves exact inputs to artifacts/check_input.json and outputs to artifacts/check_output.json. It evaluated 4,413 floating-point samples with alpha in {0.15,0.6,0.95}, sigma logarithms from -700 to 20 in steps of 0.5, contact locations {2,10,50,300,700}, and the recorded profile ratios. Observed maxima were B'=0.85, sigma|B''|=0.213998752835, |R_sigma|=0.849999998248, |sigma R_sigmasigma|=0.85, and absolute real normal Hessian at xi=0 of 3.4. The proved comparison bounds are respectively consistent with these observations; the samples do not establish universal quantifiers.\n\nFor alpha=0.6, grid-assisted minimization estimated lambda_c=0.30466208659381455 at y=0.13399532502391714. For numerical differences lambda_c-lambda of 10^-2,10^-4,10^-6,10^-8,10^-10, estimated contact locations were 5.6114102779,10.8055658048,15.7648322127,20.6264453867,25.4334615962. Corresponding slope defects were approximately 1.46022e-3,8.11445e-6,5.69482e-8,4.40665e-10,3.60121e-12. Numerical clearance residuals were below 4e-18. These use uncertified finite-grid-assisted scalar minimization and floating-point bisection; they are not exhaustive envelope calculations or mathematical certificates. The exact existence and divergent-cutoff claims are proved above independently of these decimals.\n\nFor the sampled alpha=0.6,a=-1,b=1,M=7, the sufficient common-pole-cutoff search chose t_-=-256. Its tangent value at b was -10.1691433607, below A(a)-M=-7.34073585155. This is sufficient, not optimal.\n\nAll files are in /workspace/research/native-workers/codex-lLr5le. Rerun python verify.py > artifacts/check_output.log, python compose_notes.py, and python audit_notes.py > artifacts/audit_output.log. Successful execution establishes reproducibility, not mathematical correctness. No resource-heavy computation was used.\n\nArtifacts: /workspace/research/native-workers/codex-lLr5le",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4",
        "supplied:n3",
        "supplied:n4",
        "supplied:n5"
      ]
    },
    {
      "id": "n6",
      "summary": "Additional target I is reconstructed in full as an unverified proof draft; unrestricted S06 remains INCONCLUSIVE and candidate=false.",
      "detailedSummary": "The proof covers every obstacle in the controlled family, both projective ends, every 0<gamma<1, changing right-end alternatives, escaping cutoffs, and all competitors on each fixed positive Hermitian product. Deliverables and reproducible checks are saved. The result concerns the retained singular ordinary type and its residual, and does not establish general equations, ideal operators, general obstacle sets or unrestricted S06.",
      "text": "Completion and scope audit. Notes n1--n4 reconstruct the complete new limited target I as an unverified analytic proof draft. For every k>=2, 0<alpha<1, finite fixed [a,b] and M>0, they prove a fixed-atlas uniform bound ||R_F||_{C^{1,1}}<=K(k,alpha,a,b,M) for every real C^2 obstacle supported in [a,b] with ||F||+||F''||<=M. For every 0<gamma<1 they prove ||R_F-R_G||_{C^{1,gamma}}<=K_gamma||F-G||^{(1-gamma)/2} when ||F-G||<=1. The arguments include arbitrary finite free boundaries, a common exact-zero pole neighborhood, the entire infinity hyperplane, all L alternatives, and contacts escaping to infinity. Note n5 proves these changing alternatives and escaping contacts occur within one fixed controlled family.\n\nThe operator remains the ordinary EVERYWHERE full global-obstacle envelope over all genuine kappa-psh v<=psi+F with v preceq psi. Its convex-profile identification is imported from supplied:n4 under exactly matching hypotheses. The reference remains the specified unbounded sublogarithmic genuine psi with its canonical minus-infinity pole; no model or ideal-order condition is added. The pole residual is the forced zero extension from a common neighborhood. The standard normalized Fubini--Study form and D convention from supplied:n2 are unchanged. New scalar derivatives, right-gap classification, projective bounds and interpolation are derived here. The estimates concern the residual, not global Hölder regularity of the singular potential.\n\nFor every fixed product from G, n4 checks canonical slicing with the exact horizontal kappa bound for every competitor, then transfers both estimates to the actual pulled-back residual. This includes the supplied nonclosed non-Kahler fourfold. Constants may depend on fixed product geometry. No BMP, positive lower mass, Y symmetry, closed minimal-type uniqueness or type-volume identification is required. Direct witnesses preserve the exact stretching-class definition.\n\nThe result is type-sensitive and nonvacuous. Imported supplied:n8 establishes that this psi is unbounded, ordinarily nonminimal and nonlogarithmic, with different alpha giving different ordinary types despite trivial multiplier ideals. The added family hypotheses yield uniform global pole-subtracted regularity and quantitative derivative stability within that retained type. At the actual zero-density tails of n5, regularity follows from convex geometry and residual estimates, not density smoothness or determinant vanishing order. Across finite free boundaries only C^{1,1} residual regularity is asserted. Crossing the pole uses exact reference agreement; crossing infinity uses explicit projective derivatives.\n\nK is the whole manifold with full capacity density. The distinction from the imported finite-weight continuity and Hölder background is the unbounded singular weight, retained ordinary nonlogarithmic type, and quantified residual estimates. No capacity-density failure or priority claim is made. The proof does not address a new ideal operator, arbitrary compact obstacle sets or singular weights, independently prescribed arbitrary-density equations, arbitrary ordinary or relative equation types, C^{1,1} convergence, or unrestricted S06.\n\nDeliverables are saved in /workspace/research/native-workers/codex-lLr5le. input.json is the supplied assignment; imported_notes.md preserves all eight supplied notes with their exact IDs. Programs are compose_notes.py, verify.py and audit_notes.py. Proof outputs are notes.json and proof_notes.md. Diagnostic and audit outputs are artifacts/check_input.json, artifacts/check_output.json, artifacts/check_output.log, artifacts/audit_output.log, artifacts/environment.json and artifacts/manifest.json. Run python verify.py > artifacts/check_output.log, then python compose_notes.py, then python audit_notes.py > artifacts/audit_output.log. artifacts/commands.txt records these commands. The artifact/dependency audit passed for six local notes, eight imports, 27 declared edges and 13 hashed files. It checks schema, dependency order, preservation of imported texts and artifact integrity; it is not a proof checker. The finite observations and uncertified-minimization limitations are recorded in n5. No exhaustive computational result is used in the proof.\n\nThe imported notes are background, not an author proof or method for I. No fresh primary-source retrieval or access to their old artifact directory is claimed. Support arrays retain exact supplied IDs and only earlier local IDs.\n\nEnvironment evidence records Python 3.12.14 on Linux x86_64, platform Linux-6.18.44-x86_64-with-glibc2.41. The requested configuration was gpt-6.1-sol with xhigh reasoning; no subagents or model overrides were issued. No runtime-model introspection facility was exposed, so the record cannot independently attest the active model identifier or reasoning setting. Network access was restricted and no network requests were made. No operator-provided supervised compute service was exposed; none was needed for these small diagnostics, and no resource-heavy work was launched.\n\nThe additional I assignment is fulfilled by the explicit proof deliverable and reproducible limited checks. Mathematical correctness remains unverified by an external proof checker or reviewer. The original unrestricted S06 remains INCONCLUSIVE, and candidate=false is preserved. This note does not claim a complete solution of that unrestricted task.\n\nArtifacts: /workspace/research/native-workers/codex-lLr5le",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "supplied:n2",
        "supplied:n4",
        "supplied:n8"
      ]
    }
  ],
  "candidate": false,
  "workspace": "/workspace/research/native-workers/codex-lLr5le"
}
