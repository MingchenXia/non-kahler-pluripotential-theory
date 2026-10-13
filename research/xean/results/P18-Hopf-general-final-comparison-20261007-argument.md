# P18 final comparison of the complete scalar-Hopf sufficient-condition theorem

The review task is byte-for-byte the original P18, including its alternative
completion criterion for new substantive sufficient conditions. Assess that
criterion independently. The proposed article is scoped to projective pullback
ambient data on scalar Hopf manifolds in every dimension n>=3. It does not prove
unrestricted exactness on every compact non-Kahler target failing a mass property.
The fresh statement-only worker gave candidate=false and explicitly left that
unrestricted question open, while supplying complete scoped proofs n1--n8.
Preserve and assess both facts, rather than discarding this negative metadata.

Assess every target A--F and the full supporting chain, including all exact
source hypotheses, known overlaps, actual compact modifications and actual
non-pluripolar measures. Neither a prior PASS nor a root reading flag is a
mathematical premise. The author's extraction argument uses reduced target
blowups and resolution preserving the smooth locus; the cold argument uses
compact smooth-center preparation and source principalization. Judge the
correctness of each argument and whether either needs repair; do not silently
substitute one proof for an unproved step in the other. In particular check the
canonical residual when it is infinite on a divisor, every-real-weight image
ideals, full competitor envelopes, positive-mass hypotheses on the closed base,
and the complete dyadic approximation on all modifications. No theorem requiring
BMP is applied to a Hopf target. Source forms divide by 2pi; scalar potentials
are unchanged.

The sole edit since the first full review is a bibliographic correction from
the historical July18 lecture date to the October4 version independently
retrieved and assessed. Historical bytes remain in the old argument and report.
No mathematical statement has changed. A successful scoped comparison must
state its scope and the remaining unrestricted question explicitly. Do not
infer ordinary background-type independence, all-type extremal volumes, or
literature priority from the stated individual masses and ideal compatibility.




## Whole corrected current author article

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\ord}{\operatorname{ord}}
\newcommand{\PP}{\mathbb P}
\newcommand{\I}{\mathcal I}
\newcommand{\cO}{\mathcal O}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Exact intrinsic traces on scalar Hopf manifolds\newline
and unbounded mass in every dimension at least three}
\author{}
\date{}
\begin{document}
\maketitle
\noindent\textbf{Working draft.} Mathematical review, independent
reconstruction and final comparison are pending. The unrestricted
non-K\"ahler trace problem remains open.
\begin{abstract}
For every scalar Hopf manifold of dimension at least three, we extend
the original smooth Xia--Zhang threefold construction to obtain
unbounded Monge--Amp\`ere mass. An exact comparison of angularly
integrated densities supplies the extension. On these targets, ambient
potentials pulled back from projective space nevertheless have exact
intrinsic traces on every smooth compact modification. The full trace
envelope descends to a closed trace on the projective base. A finite
divisorial extraction argument works in arbitrary base dimension:
blow up each divisor image and resolve the target without changing its
smooth locus, while the order of a pulled-back top form decreases.
We prove ideal-type compatibility, addition and analytic approximation,
and compute positive finite individual masses. These conclusions treat
the specified pullback data; unrestricted non-K\"ahler exactness and
ordinary-type independence are not claimed.
\end{abstract}

We use $d^c=\frac{i}{4\pi}(\bar\partial-\partial)$ and
$\ddc=\frac{i}{2\pi}\partial\bar\partial$.
Potentials have their genuine canonical representatives.
The ideal $\I(tu)$ is defined by local integrability of
$|g|^2e^{-tu}$, with no additional factor two.
An ideal restricted to a submanifold always means its coherent image
ideal. Non-pluripolar products with nonclosed smooth backgrounds use
bounded local products with smooth corrections and truncation
\cite[Section 2.1]{BGL}.

\section{Geometry and statement}
Fix an integer $n\ge3$ and put $d=n-1$. Let
\[
 M=(\mathbb C^{n+1}\setminus\{0\})/\langle z\mapsto ez\rangle,
 \qquad
 Y=H_n=(\mathbb C^n\setminus\{0\})/\langle z\mapsto ez\rangle.
\]
The inclusion of the first $n$ coordinates identifies $Y$ with a
linear submanifold of $M$. Projectivization gives the commuting square
\[
 \begin{matrix}Y&\longrightarrow&M\\
 q\downarrow&&\downarrow p\\
 B=\PP^d&\longrightarrow&\PP^n.
 \end{matrix}
\]
Both vertical maps are holomorphic submersions with connected elliptic
fiber $E=\mathbb C/(\mathbb Z+2\pi i\mathbb Z)$.
Normalize the Fubini--Study form $\kappa$ on $B$ by
$\int_B\kappa^d=1$. On $Y$, put
\[
 r=\log\|z\|^2\pmod 2,
 \quad \alpha=q^*\kappa=\ddc r,
 \quad \beta=dr\wedge d^cr,
 \quad \Omega_{a,b}=a\alpha+b\beta \quad(a,b>0).
\]
The differential of $r$ is global. The form $\beta$ has rank one,
is positive along the fibers, and $\int_E\beta=2$.
Thus $\Omega_{a,b}$ is Hermitian, $\int_Y\Omega_{a,b}^n=2nba^d$,
and $d\Omega_{a,b}=-b\,dr\wedge\alpha\ne0$.
The target is non-K\"ahler, since its first Betti number is one.
Section~\ref{sec:bmp} proves that it fails BMP for every $n\ge3$,
using the original threefold family of \cite{XZ}.

Let $U$ be genuine quasi-psh on $\PP^n$ with $\nu(U,B)=0$,
and let $u=p^*U$. Set
\[
 \mathfrak b_t=\I(tU)\cO_B,
 \qquad \mathfrak a_t=\I(tu)\cO_Y.
\]
These image ideals are nonzero. For a prime divisor $F$ over $B$,
write
\[
 \tau_B(F)=\lim_{t\to\infty}t^{-1}\ord_F\mathfrak b_t;
\]
define $\tau_Y$ from $\mathfrak a_t$ in the same way.
For any sufficiently large background $\Theta$, let
$T_\Theta$ denote the usc supremum of all $\Theta$-psh potentials
$v\le0$ satisfying $\nu(v,F)\ge\tau(F)$ on every smooth compact
modification. The definition includes all competitors.

\begin{theorem}\label{thm:main}
There is $a_0>0$, depending on the ambient curvature bound for $U$,
such that for $a\ge a_0$ and every $b>0$,
\[
 T_{\Omega_{a,b}}(u;Y)=q^*T_{a\kappa}(U;B).
 \tag{1}
\]
For every smooth compact modification $\pi:Z\to Y$ and every prime
divisor $D$ on $Z$, simultaneously,
\[
 \nu(T_{\Omega_{a,b}}(u;Y)\circ\pi,D)=\tau_Y(D).
 \tag{2}
\]
Equality (2) also holds for the trace in any Hermitian background
$\Omega\ge\Omega_{a,b}$. In the backgrounds in (1), the trace has
positive finite individual non-pluripolar mass and
\[
 \int_Y\MA_{\Omega_{a,b}}(T_{\Omega_{a,b}})
   =2nb\int_B\MA_{a\kappa}(T_{a\kappa}),
 \qquad
 2nb(a/2)^d\le\int_Y\MA_{\Omega_{a,b}}(T_{\Omega_{a,b}})
   \le2nba^d.
 \tag{3}
\]
The ideal class of the traces in (1) is independent of $a,b$ within
this range, is additive and positively homogeneous in the ambient
ideal trace data, and admits the dyadic analytic approximation
described below.
\end{theorem}

\section{Unbounded mass in all Hopf dimensions}\label{sec:bmp}
\begin{proposition}\label{prop:bmp}
For every $n\ge3$, $H_n$ fails the bounded mass property.
There are globally smooth $V_\eta$ with
$\alpha+\beta+\ddc V_\eta>0$ and total mass tending to infinity.
\end{proposition}
\begin{proof}
Use the original Xia--Zhang family, with its original heat scale
$\varepsilon_\eta=\eta^{1/\eta^2}$, not a new transport family.
Write $\xi\in\mathbb C^d$, $x=\log|\xi|^2$,
$w=\log z_0\pmod{\mathbb Z+2\pi i\mathbb Z}$ and
$\mu=e^x/(1+e^x)$ on the projective affine chart. Then
$r=w+\bar w+\log(1+e^x)$.
There are $n-2$ angular directions orthogonal to the radial direction.
Differentiating in these directions gives the identical angular
entries $A=(\mu+V_x)/\mu$. The radial/fiber block, in the frame
of \cite[Lemma 2.2]{XZ}, is
\[
 K_V=\begin{pmatrix}
 (\mu+V_{xx})/[\mu(1-\mu)]&
 (\mu+V_{x\bar w})/\sqrt{\mu(1-\mu)}\\
 (\mu+V_{wx})/\sqrt{\mu(1-\mu)}&1+V_{w\bar w}
 \end{pmatrix}.
\]
The background block has determinant one. The differential-form
expansion contains $-(1-\mu)V_x$, but its radial contribution
cancels that of the angular prefactor, giving exactly this block.
Thus the positivity conditions in every dimension are
\[
 1+V_{w\bar w}>0,\qquad \mu+V_x>0,\qquad
 Q[V]=V_{xx}+\mu-\frac{|\mu+V_{x\bar w}|^2}{1+V_{w\bar w}}>0.
\]
The source operator is $i\partial\bar\partial$; dividing both
source background forms by $2\pi$ gives ours with the same
numerical potential and these same ratios.

Normalize angular contact measure by mass one and write $dA_E$
for Haar probability measure on the elliptic fiber. The radial
Fubini--Study density on $\PP^d$ is
$d\mu^{d-1}\mu'\,dx=d\mu^d(1-\mu)\,dx$.
Since the fiber mass is two, the angularly integrated background
volume density is $2nd\mu^d(1-\mu)\,dx\,dA_E$.
Let $J_n(V;x,w)$ denote the angularly integrated smooth
Monge--Amp\`ere density. Multiplying by $A^{n-2}\det K_V$ gives
\[
 J_n(V;x,w)=\frac{n(n-1)}6(\mu+V_x)^{n-3}J_3(V;x,w).
 \tag{7}
\]
This compares integrated densities; the angular spheres in the
different dimensions each have their own probability normalization.

The original family is $V_\eta=W_\eta+g_\eta$.
It has all three strict positivity inequalities, is independent
of $x$ at the negative end, and is one constant at the positive end
\cite[Proposition 4.1]{XZ}. These endpoint properties give the
same global smooth extension with $\xi\in\mathbb C^d$.
Its construction also gives
\[
 \begin{gathered}
 \sup[W_{\eta,x}]_-=o(1),\qquad
 -m_\eta\le g_\eta'\le0,\qquad m_\eta=o(1),\\
 g_\eta''=r_\eta-m_\eta\psi,\qquad
 \int r_\eta=m_\eta,\quad\int\psi=1.
 \end{gathered}
\]
Here $r_\eta,\psi\ge0$ and $g_\eta=0$ on $x\le-2$.
Consequently $\mu+V_{\eta,x}\ge1/4$ for $x\ge0$ and small $\eta$.

The source proves $\int J_3(V_\eta)\to\infty$. To localize this
divergence, on $x<0$ one has
$W_\eta=F_\eta(\varepsilon_\eta,w)$, with no $x$ derivatives.
Since $\int_EF_{w\bar w}\,dA_E=0$, exact fiber integration gives
\[
 \int_E J_3(V_\eta;x,w)\,dA_E
   =12(\mu+g_\eta')[g_\eta''+\mu(1-\mu)].
\]
Use $0<\mu+g_\eta'\le\mu$ and
$\int|g_\eta''|\le2m_\eta$. The total mass on $x<0$ is at most
$12\int_{-\infty}^0\mu^2(1-\mu)\,dx+24m_\eta
=3/2+24m_\eta$.
The high amplitude of $F_{w\bar w}$ has been integrated exactly;
no uniform derivative bound is needed there.
It follows that $\int_{x\ge0}J_3(V_\eta)\to\infty$.
Equation (7) now gives
\[
 \int_{H_n}(\alpha+\beta+\ddc V_\eta)^n
 \ge\frac{n(n-1)}6\,4^{-(n-3)}\int_{x\ge0}J_3(V_\eta)
 \longrightarrow\infty.
\]
Every other Hermitian form $h$ dominates $c(\alpha+\beta)$
for some $c>0$. The potentials $cV_\eta$ have strictly positive
perturbed $h$, and their smooth masses dominate $c^n$ times
the preceding divergent masses. This proves BMP failure.
\end{proof}

\section{Divisorial extraction in arbitrary dimension}
\begin{lemma}\label{lem:extract}
Let $f:Z\to B$ be a dominant holomorphic map of connected smooth
compact complex manifolds, with $\dim B=d$, and let $D$ be a prime
divisor on $Z$. Either $f(D)=B$, or there is a smooth compact
modification $\sigma:B'\to B$ such that $f$ lifts holomorphically
near generic $D$ and $D$ dominates a prime divisor $F$ on $B'$.
For an integer $e\ge1$, every nonzero coherent ideal $\mathfrak b$
and every genuine quasi-psh $w$ on $B$ satisfy
\[
 \ord_D f^*\mathfrak b=e\ord_F\sigma^*\mathfrak b,
 \qquad \nu(w\circ f,D)=e\nu(w\circ\sigma,F).
 \tag{8}
\]
In the horizontal case both orders and generic Lelong numbers are zero.
\end{lemma}
\begin{proof}
Maintain a compact analytic graph proper over $Z$ which is an
isomorphism near generic $D$, with a dominant map to a smooth
compact modified base. The graph may be singular away from this
unchanged neighborhood. The divisor image $S$ is irreducible
analytic by the proper mapping theorem
\cite[Chapter II, Theorem 8.8]{Dem}.
Near generic $D$, define $J_D(f)$ as the minimum order of the
coefficients of $f^*(dy_1\wedge\cdots\wedge dy_d)$ in a smooth
source frame. Dominance gives a finite nonnegative integer,
independent of the local smooth coordinate choices.

If $S$ has codimension $c\ge2$, blow up its reduced coherent ideal.
The blowup can be singular globally, but it is smooth over the
smooth part of $S$. There use $S=\{y_1=\cdots=y_c=0\}$ and let
$m=\min_{i\le c}\ord_D f^*y_i\ge1$.
Choose $y_1$ of least order and shrink at generic $D$ so its
leading coefficient is a unit. All ratios $f^*y_i/f^*y_1$ are
holomorphic there, giving a lift to the smooth blowup chart
\[
 (y_1,\ldots,y_c)=(s,st_2,\ldots,st_c).
\]
Take the main graph of this lift. Resolve the target blowup using
a proper resolution which is an isomorphism on its whole smooth
locus \cite[Theorem 2.0.1]{Wlo}. The new target is smooth and
compact. The lift at generic $D$ is preserved, since its image
lies in that smooth locus. Taking the main graph of the resulting
meromorphic lift again preserves the generic source neighborhood.

The smooth-center Jacobian identity is
\[
 dy_1\wedge\cdots\wedge dy_d
   =s^{c-1}ds\wedge dt_2\wedge\cdots\wedge dt_c
                  \wedge dy_{c+1}\wedge\cdots\wedge dy_d.
\]
The target resolution is locally an isomorphism here. Therefore
\[
 J_D(f_{\rm new})=J_D(f)-(c-1)m\ge0.
\]
Each step strictly decreases $J$. After finitely many steps the
image has codimension one; it cannot dominate the target if its
original image was proper. This proves extraction without a
resolution of the source graphs that might change generic $D$.
Generic ideal generators along $F$ are powers of its equation
times a unit ideal, giving the first equality in (8).

At generic smooth points, tangential dominance $D\to F$ gives
rank $d-1$. Absorb a unit into a local normal coordinate using
an $e$-th root, and use the tangential base coordinates as source
coordinates. The exact local form is
\[
 (z_1,z_2,\ldots,z_d,z')\longmapsto(z_1^e,z_2,\ldots,z_d).
\]
After a smooth local correction, divisorial Siu removal writes
$w\circ\sigma=c\log|y_1|^2+R$, with $R$ psh and generic
Lelong number zero on $F$
\cite[Chapter III, (8.15)--(8.16)]{Dem}.
At a very general point of $F$ its full point Lelong number is zero.
Skoda's lemma gives integrability of $e^{-tR}$ for each $t>0$
\cite[Lemma 5.6(a)]{DemAM}.
For $e>1$ choose $1<p<e/(e-1)$. The ramification density
$|y_1|^{2/e-2}$ lies in $L^p$, so change of variables and
H\"older, using Skoda for $tp'R$, give
\[
 \int e^{-tR(z_1^e,z_2,\ldots,z_d)}dV_z
 =C_e\int e^{-tR(y)}|y_1|^{2/e-2}dV_y<\infty.
\]
Free variables contribute a harmless product factor. For $e=1$
use Fubini. A positive generic divisor coefficient $c'$ of the
residual pullback would force nonintegrability when $tc'\ge1$.
Its coefficient is therefore zero, and the logarithm gives $ec$.
This proves the Lelong equality, including when $R|_F\equiv-\infty$.
In the horizontal case $D\to B$ is a submersion at very general
points. Skoda and Fubini give zero generic coefficient; every
nonzero ideal is generically a unit there.
\end{proof}

\section{Ideal pullback and the full envelope}
\begin{lemma}\label{lem:ideals}
For a holomorphic submersion $q$ and a genuine quasi-psh potential
$v$ on its base, $\I(tq^*v)=q^*\I(tv)$ for every real $t>0$.
In the geometry above, $\mathfrak a_t=q^*\mathfrak b_t$ and
$\nu(u,Y)=0$.
\end{lemma}
\begin{proof}
Use local product coordinates $(x,y)$. The inclusion of the extended
base ideal follows by Fubini. For the reverse inclusion expand an
integrable holomorphic germ as $g(x,y)=\sum_\gamma g_\gamma(x)y^\gamma$.
The fiber coefficient estimate for holomorphic functions bounds
$|g_\gamma(x)|^2$ by a constant times the fiber integral of $|g|^2$.
Each coefficient therefore lies in $\I(tv)$ at the selected base point.
Every finite Taylor truncation belongs to its extended ideal $J$,
so $g\in J+(y)^N$ for all $N$. Krull intersection in the Noetherian
local analytic ring modulo $J$ gives $g\in J$. Smooth corrections
do not affect integrability. Apply the result to $p$ and restrict
the ideal to $Y$. Local submersion coordinates also preserve the
generic Lelong number along the inverse image of $B$.
\end{proof}

For clarity, recall the supplied closed-target trace construction.
Choose $a\kappa$ at least twice an admissible Hermitian background on
$B$ and discard finitely many indices of the ambient analytic
regularization $U_m$. The normalized ordinary analytic models
\[
 w_j=P_{a\kappa}[U_{2^j}|_B]
\]
decrease to $w=T_{a\kappa}(U;B)$.
The trace majorant lies in $\PSH(B,a\kappa/2)$ and is below $w$.
Closed mass monotonicity and the smaller-background expansion give
$\int_B\MA_{a\kappa}(w)\ge(a/2)^d$, while the closed upper bound is
$a^d$. The decreasing positive-mass model theorem
\cite[Proposition 3.1.12]{SGPT} now gives, for every divisor $F$ over $B$,
\[
 \nu(w,F)=\lim_j\nu(w_j,F)
  =\lim_j2^{-j}\ord_F\mathfrak b_{2^j}=\tau_B(F).
 \tag{6}
\]
The model and positive-mass hypotheses are essential; arbitrary
decreasing quasi-psh convergence would not imply this equality.
The closed-target construction and analytic envelope properties are
the known trace background, rather than conclusions imported to $Y$.

\begin{proof}[Proof of Theorem \ref{thm:main}]
Apply Lemma \ref{lem:extract} to $q\circ\pi$ for every target
modification $\pi:Z\to Y$. Equations (8), (6) and Lemma
\ref{lem:ideals} give
$\nu(q^*w\circ\pi,D)=\tau_Y(D)$ for each divisor, so $q^*w$ is
an exact competitor.

The compact elliptic group acts along the fibers, preserving
$\alpha,\beta$ and every $\mathfrak a_t$. It consequently preserves
the full trace competitor family, including its constraints on all
modifications. Its usc envelope is invariant and descends to a
genuine quasi-psh potential on $B$ by local sections. For a basic
potential $q^*v$, the background inequality is equivalent to
$a\kappa+\ddc v\ge0$. Indeed wedge the background inequality
with the smooth semipositive $\beta$ and push forward by $q$.
Since $\beta^2=0$ and its fiber integral is two, the resulting
positive current is $2(a\kappa+\ddc v)$. Conversely add $b\beta\ge0$.

Every base modification $B'\to B$ lifts to the smooth compact
modification $Y\times_B B'\to Y$. The inverse image of a prime divisor
$F$ is prime, since the elliptic fibers are connected; at generic
points its multiplicity is one. Thus the descended trace envelope
satisfies every base constraint, and is at most $w$. The opposite
inequality follows from the exact competitor $q^*w$. This proves
(1) and (2). For $\Omega\ge\Omega_{a,b}$ the same exact competitor
lies below $T_\Omega$, so
$\tau_Y(D)\le\nu(T_\Omega,D)\le\nu(q^*w,D)=\tau_Y(D)$.

For $v_j=\max(v,-j)$ on the base, actual bounded local products give
\[
 (\Omega_{a,b}+\ddc q^*v_j)^n
   =nb\,\beta\wedge q^*(a\kappa+\ddc v_j)^d,
\]
since the horizontal current has rank at most $d$ and $\beta^2=0$.
Multiply by $\mathbf1_{\{v>-j\}}$ and pass to the non-pluripolar
limit. Integrating over the fibers gives the factor $2nb$ in (3).
The closed-base bounds above give its two inequalities.
These are individual masses, not extremal volumes of all ordinary
representatives.

Different sufficiently large base backgrounds produce potentials
with the same numbers (6); the closed K\"ahler ideal criterion
\cite[Proposition 3.2.1]{SGPT} gives the same ideals at every real
weight. Lemma \ref{lem:ideals} transfers this to (1).
Intrinsic trace data are additive and positively homogeneous.
On the base, the sum of two exact realizers has the sum of their
divisorial numbers. The same criterion identifies its ideal class
with the trace for $U_1+U_2$, in a background with sufficient
curvature room. Positive scaling is identical. Pull back to $Y$.
This uses the ideal criterion on the projective base, and does not
assume a global valuative criterion on an arbitrary non-K\"ahler target.
\end{proof}

\section{Approximation and a point trace}
For the dyadic $w_j$ above, put $v_j=q^*w_j$. Compact elliptic
invariance applied to the full ordinary obstacle envelopes shows,
for $h\in\PSH(B,a\kappa)$,
\[
 P_{\Omega_{a,b}}[q^*h]=q^*P_{a\kappa}[h].
\]
At each finite obstacle level the competitor family is invariant;
its full supremum descends, and ordinary order is equivalent on
the base by surjectivity. Thus $v_j$ are the full ordinary analytic
models of the pulled-back restricted approximants. They decrease
to (1) in $L^1(Y)$: decreasing quasi-psh convergence is genuine,
or one can integrate a fixed invariant volume along the fibers.
For every divisor $D$ over $Y$, (6) and (8) yield
\[
 \nu(v_j,D)\longrightarrow\tau_Y(D).
\]
The same potentials pulled back to any target modification converge
in $L^1$ there, by quasi-psh compactness and uniqueness off the
exceptional set. This assertion supplies no convergence theorem
for extremal non-K\"ahler singularity volumes or capacities.

A concrete trace involving exceptional divisors is obtained from
\[
 U([z_0:\cdots:z_n])
  =\log\frac{\sum_{i=0}^{n-2}|z_i|^2}{\sum_{i=0}^{n}|z_i|^2},
 \qquad B=\{z_n=0\}.
\]
Its generic number along $B$ is zero, and its restricted image
ideals are
\[
 \mathfrak b_t=\mathfrak m_P^{\max(\lfloor t-d+1\rfloor,0)},
 \qquad P=[0:\cdots:0:1]\in B.
\]
The formula follows from the normal radial integrability condition
$k>t-d$ in $d$ normal coordinates to the ambient singular line.
Consequently $\tau_Y(D)=\ord_Dq^*\mathfrak m_P$ on every model.
The genuine potential $q^*(U|_B)$ is an explicit exact realizer,
singular along the elliptic fiber over $P$. For $a>1$,
\[
 \int_Y\MA_{\Omega_{a,b}}(q^*(U|_B))=2nb(a^d-1).
\]
On the point blowup the horizontal current, after removing the
exceptional divisor $F$, has class $aH-F$ and smooth semipositive
representative $(a-1)\sigma^*\kappa+\eta$. Here $\eta$ is the
pullback of the Fubini--Study form by the resolved projection to
$\PP^{d-1}$. The mixed intersections of $H$ and $F$ vanish,
$H^d=1$ and $F^d=(-1)^{d-1}$, giving $(aH-F)^d=a^d-1$.
Its smooth product off $F$ is the pullback of the actual
non-pluripolar product, and a smooth measure charges no divisor.
The displayed potential need not equal the normalized trace envelope.

\begin{remark}
The theorem treats arbitrary genuine ambient $U$ with the stated
generic condition, including nonanalytic data and cases where
$U|_B$ is identically $-\infty$; image ideals, not naive restriction,
define the trace. The base has arbitrary dimension $d\ge2$. No finite selection
of exceptional divisors replaces the simultaneous constraint.
Ideal-type compatibility is asserted for the invariant backgrounds
in (1). Exactness in larger arbitrary backgrounds follows by the
sandwich argument, but ordinary-type independence is not claimed.
\end{remark}

\begin{thebibliography}{9}
\bibitem{BGL} S. Boucksom, V. Guedj and C. H. Lu,
\emph{Volumes of Bott--Chern classes}, arXiv:2406.01090.
\bibitem{Dem} J.-P. Demailly, \emph{Complex Analytic and Differential
Geometry}, Harvard-hosted June 2012 manuscript.
\bibitem{DemAM} J.-P. Demailly, \emph{Analytic Methods in Algebraic
Geometry}, Surveys of Modern Mathematics 1, 2012.
\bibitem{SGPT} M. Xia, \emph{Singularities in global pluripotential
theory}, lecture manuscript, October 4, 2026 version,
\url{https://mingchenxia.github.io/Lectures/SGPT_final.pdf}.
\bibitem{Wlo} J. W\l{}odarczyk,
\emph{Resolution of singularities of analytic spaces},
Proceedings of the 15th G\"okova Geometry--Topology Conference
(2008), 31--63, published 2009,
\url{https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf}.
\bibitem{XZ} M. Xia and K. Zhang,
\emph{A counterexample to the bounded mass property},
arXiv:2608.21053v1.
\end{thebibliography}
\end{document}


## Whole historical author argument and all its proof components

# Complete new P18 general-dimensional root candidate

PRIVATE, UNVERIFIED. No native mathematical acceptance or publication. The frozen surface inputs remain unchanged.

## Exact original task

{
  "problem": "All manifolds are connected and compact. Write dd^c=(i/(2 pi))partial barpartial. Use genuine canonical quasi-psh representatives. For a smooth real (1,1) form theta, PSH(X,theta) means theta+dd^c u>=0. Ordinary order u preceq v means u<=v+C and equivalence means mutual order, including the canonical values at common poles. Extended products mean non-pluripolar Monge-Ampere products with smooth-background corrections. A big background admits a genuine strict current theta+dd^c u>=epsilon h for some Hermitian h and epsilon>0. BMP means v_+(h)<infinity, where v_+(h) and v_-(h) are the supremum and infimum of integral(h+dd^c u)^n over all bounded h-psh u. Positive lower mass means v_-(h)>0; it is distinct from BMP. Define I(tu) by local integrability of |g|^2 exp(-tu), with no extra factor 2. Ideal equivalence means equality at every real t>0. P_theta[u]_I is the usc supremum of theta-psh v<=0 ideal-equivalent to u. P_theta[u] is the ordinary singularity envelope, the usc supremum of theta-psh v<=0 with v preceq u. The lower and upper singularity volumes are the infimum and supremum of the extended mass over all v ordinarily equivalent to u in the specified background, not the raw mass of one representative. Let Y be a connected positive-dimensional compact complex submanifold of X, and u quasi-psh on X with generic Lelong number nu(u,Y)=0. The restricted ideal a_t=I(tu)O_Y is the image ideal, which is coherent and nonzero. A divisor over Y is a prime divisor E on any connected smooth compact modification pi:Z->Y. Define tau_(Y,u)(E)=lim_(t->infinity)ord_E(a_t)/t; the finite limit equals the supremum over t>0 and the integer limit. These intrinsic data depend only on the ambient ideal class and are additive and positively homogeneous. A naive restriction u|Y can be identically minus infinity; it is not the definition of these data. For a sufficiently large Hermitian Omega on Y, define T_Omega(u;Y) as the usc supremum of Omega-psh v<=0 with nu(v composed pi,E)>=tau_(Y,u)(E) on every such modification. Original P18: when Y fails at least one of BMP and positive lower mass, can Omega be chosen so that equality holds simultaneously for every prime divisor on every modification? After exactness, determine a background-compatible ordinary or ideal type, with addition and analytic approximation properties. Known background: a common competitor, the trace envelope, ideal/ordinary fixedness, convergence of restricted analytic envelopes, and pulled-background modification compatibility already hold without either mass property. Their Lelong conclusions are only lower inequalities. Doubling an admissible background gives positive finite individual envelope mass and prescribed-type Lp equations, but does not already prove exact trace numbers. Exact realization on curves, on Kahler targets in a sufficiently large closed background, under both mass properties, and for specified curve-fibration trace data is already known. A single model divisor current cannot encode all exceptional orders, and exact divisorial data alone does not determine top mass. No new realization, geometry, criterion or proof is supplied.",
  "completionCriteria": "Resolve simultaneous exactness in the stated generality by proof or an actual counterexample, then state and prove the compatible type, addition and approximation conclusions actually available. Alternatively give new substantive sufficient conditions on a genuinely non-Kahler target failing a mass property, beyond the listed curve and fibration cases. Do not mistake curvature room, individual envelope mass, a lower Lelong inequality or exactness on a single model for simultaneous exactness. A restricted theorem remains explicitly scoped. Verify exact indispensable external claims at primary sources and independently reconstruct the full argument."
}


## Full private mathematical note: notes/Hopf-all-dimensions-unbounded-mass.private-unverified.md

# Candidate: unbounded Monge--Ampere mass on every diagonal Hopf manifold of dimension at least three

PRIVATE, UNVERIFIED ROOT CANDIDATE. No mathematical acceptance, native review, independent reconstruction, publication or full catalogue closure is claimed. The frozen P18 six-page article and review/reconstruction inputs are unchanged. This is a separate extension proposal using the ORIGINAL Xia--Zhang smooth construction, not the unaccepted S02 heat-scale modification.

## Proposed theorem

For every integer n>=3, H_n=(C^n\{0})/<z->ez> fails BMP. Use our dd^c=i/(2 pi) partial barpartial, k=n-1, projectivization q_n:H_n->P^k, alpha_n=q_n^*omega_FS with integral_Pk omega_FS^k=1, r=log||z||^2 modulo two, beta_n=dr wedge d^c r, h_n=alpha_n+beta_n. The smooth potentials from the actual Xia--Zhang original transport construction on H_3 can be put on H_n using exactly the same radial/fiber function. Their positivity inequalities are dimension independent, and their positive-side annular masses compare from below by a fixed multiple of the threefold annular mass.

## Actual local matrices and angular integration

In the chart z0!=0 write xi=(z1/z0,...,zk/z0), x=log|xi|^2, and w=log z0 modulo Z+2 pi i Z. Put L=log(1+exp x), mu=exp x/(1+exp x). Then r=w+bar w+L and alpha=dd^c L.

For any real smooth V(x,w) with the original source's endpoint extensions, the matrix of h_n+dd^c V in the source's angular/radial/fiber frame (scaled for our normalization) has:

- k-1=n-2 identical angular eigenvalues A=(mu+V_x)/mu;
- the same radial/fiber two-by-two block as the threefold source (its dimension does not change).

Source normalization: dd^c_source=i partial barpartial=2 pi times ours. Both source alpha and beta divide by 2 pi to give ours, and the same numerical V gives h_n+dd^c_ours V=(h_n_source+dd^c_source V)/(2 pi). Thus the positivity ratios below use the exact numerical derivatives of the source V, with no potential rescaling.

Let

    Q[V]=V_xx+mu-|mu+V_(x bar w)|^2/(1+V_(w bar w)).

The positivity conditions, for every n>=3, are exactly

    1+V_(w bar w)>0, mu+V_x>0, Q[V]>0.

More explicitly the common radial/fiber block is

    [ (mu+V_xx)/(mu(1-mu)),
      (mu+V_(x bar w))/sqrt(mu(1-mu));
      (mu+V_(w x))/sqrt(mu(1-mu)), 1+V_(w bar w) ].

Its determinant equals (1+V_(w bar w))Q[V]/(mu(1-mu)). The background radial/fiber block has determinant one, so these determinants also give the relative volume factor. These are actual smooth matrices, not formal unbounded currents. The apparent -(1-mu)V_x term in the source's differential-form expansion cancels the radial contribution of its angular prefactor; it is absent from the evaluated radial matrix entry.

Normalize the angular contact measure on S^(2k-1) by mass one. The base Fubini--Study volume has radial density

    k mu^(k-1) mu' dx = k mu^k(1-mu) dx.

The vertical part of beta has fiber mass two. Consequently the angularly integrated smooth h_n^n volume has radial/fiber density 2n k mu^k(1-mu) dx dA_E, where dA_E is normalized Haar probability measure. The mixed base components of beta vanish after wedging with the top base form. Multiplication by the actual determinant above gives the smooth MA density.

Let J_3(V;x,w) denote the corresponding angularly integrated threefold MA density, including its h_3^3 radial/fiber volume density 12 mu^2(1-mu). The exact identity is

    J_n(V;x,w)=[n(n-1)/6] (mu+V_x)^(n-3) J_3(V;x,w).

Indeed the higher-dimensional determinant contributes A^(n-3), while the normalized radial/fiber background volume contributes [n(n-1)/6] mu^(n-3). This identity is independent of a changed angular sphere dimension because each contact sphere has been integrated with its own normalized probability measure. It gives an identity of integrated densities, not a pointwise identification of different manifolds.

## Apply the unchanged source family

The original source constructs V_eta=W_eta+g_eta, with W_eta=theta(q(x))F_eta(t(x),w), epsilon_eta=eta^(1/eta^2), all three strict positivity conditions, W_eta=F_eta(epsilon_eta,w) on x<=0 and constant at the positive end after adding g. It proves

    sup_(x,w) [W_(eta,x)]_- = o(1),
    -m_eta<=g_eta'<=0, m_eta=o(1),
    g_eta''=r_eta-m_eta psi,
    integral r_eta=m_eta, integral psi=1,

with psi supported in (-2,-1), r_eta supported in (-1/2,b_eta+1/2), and g_eta=0 on x<=-2. Thus for x>=0 and all sufficiently small eta,

    mu+V_(eta,x) >= 1/2-o(1) >=1/4.

The same V_eta is a smooth global potential on H_n: on the negative end it is independent of the singular radial coordinate and is smooth in the actual holomorphic fiber coordinate over xi=0; on the positive end it is one constant, independent of w and the base. The source's compact-chart extension proof applies with xi in C^k. Each angular eigenvalue is positive and the common two-by-two block is positive, so h_n+dd^c V_eta>0.

## Threefold mass cannot escape entirely to the negative side

The source gives integral_H3 MA_h3(V_eta)->infinity. It remains to show that the part x<0 is uniformly bounded; then the exact density comparison forces higher-dimensional divergence.

For x<0 the heat term W_eta=F_eta(epsilon_eta,w) has no x derivative. The only x derivatives are g',g''. Hence V_(x bar w)=0, and the fiber integral of F_(w bar w) is zero. The exact angular/fiber-averaged threefold MA density on x<0 therefore is

    12 (mu+g') [g''+mu(1-mu)].

Here -m_eta<=g'<=0 and mu+g'>0. On x<=-2 it equals the background density 12 mu^2(1-mu), which is integrable from minus infinity. On [-2,0], mu is bounded away from zero, |g'|<=m_eta, and

    integral_R |g''| <= integral r_eta + m_eta integral psi =2m_eta.

Since 0<mu+g'<=mu<=1, the integral of the displayed density over x<0 is at most the background contribution on x<0 plus 24m_eta, hence uniformly bounded. The possibly very high amplitude of F_(w bar w) causes no hidden bound problem: it has been integrated exactly and has zero fiber integral, while all remaining factors on x<0 are independent of w.

It follows that integral_(x>=0) J_3(V_eta;x,w) dx dA_E ->infinity. On that region the exact density formula yields

    integral_Hn MA_hn(V_eta)
      >= [n(n-1)/6] 4^(-(n-3)) integral_(x>=0) J_3(V_eta)
      ->infinity.

All potentials are smooth and globally strictly positive. Any other Hermitian metric H on H_n dominates c h_n for some c>0. Then H+dd^c(c V_eta)>=c(h_n+dd^c V_eta)>0 and its smooth mass is at least c^n times the displayed divergent mass. Therefore BMP fails for every Hermitian metric on H_n.

## Remaining checks and scope

The source identity integral_H3 MA->infinity, exact original endpoint descriptions, negative-slope estimate and correction integral are taken from Xia--Zhang arXiv:2608.21053v1, Theorem 1.1, Lemmas 2.1--2.3 and Proposition 4.1. Root has read its complete 902-line extraction and relevant actual pages for other exact applications; this new all-dimensions application must itself be assessed with the primary. The angular multiplicity, normalized radial measures, exact density ratio and negative-side estimate are new root calculations and still require independent reconstruction.

This candidate would allow a P18 projective-base extension to arbitrary higher-dimensional Hopf targets if a separately checked general-dimensional extraction lemma is supplied. It does not alter the current surface-base P18 candidate, prove sharp damping in original S02, prove positive lower mass in any dimension, determine all ordinary singularity volumes, or solve the unrestricted original catalogue.


## Full private mathematical note: notes/P18-general-divisorial-extraction.private-unverified.md

# Candidate: divisorial extraction for proper dominant maps in arbitrary dimension

PRIVATE, UNVERIFIED ROOT CANDIDATE. This note makes a new mathematical application of analytic resolution. No independent mathematical acceptance, native review, reconstruction, publication or original P18 closure is claimed. The frozen six-page surface-base P18 manuscript and its full-review and statement-only inputs remain unchanged.

## Exact proposed lemma

Let f:Z->B be a proper dominant holomorphic map of connected smooth compact complex manifolds, dim B=d>=1, and let E be a prime divisor on Z. If f(E)=B, every nonzero coherent ideal b on B satisfies ord_E(f^*b)=0, and every genuine quasi-psh w on B satisfies nu(w composed f,E)=0.

If f(E) is proper, there exist a smooth compact modification sigma:B'->B, a prime divisor F on B', a compact irreducible analytic graph G proper and bimeromorphic over Z, and a holomorphic map f':G->B', with the following properties. The projection G->Z is an isomorphism near the generic point of E. Its strict transform E' is a prime divisor there, f'(E')=F, and, for one integer e>=1,

    ord_E(f^*b)=e ord_F(sigma^*b)
    nu(w composed f,E)=e nu(w composed sigma,F).

The identities hold for every nonzero coherent ideal b and every genuine quasi-psh w. The graph need not be smooth away from the generic divisor. Its singularities away from that divisor are irrelevant to both identities. Every target B' is globally smooth and compact. No finite family of models replaces the quantifier over all original E.

## Finite construction using the order of a pulled-back top form

Start with G=Z and B'=B. At every stage retain the actual original smooth coordinate neighborhoods near a dense open subset of E; the projection to Z is an isomorphism there. The resulting G is a compact irreducible analytic space proper over Z, with a dominant holomorphic map f' to a smooth compact B'. The closure of the generic divisor is compact and irreducible, and its image S in B' is a compact irreducible analytic subset by the proper mapping theorem.

Near a smooth point of S where E maps generically, let y1,...,yd be coordinates of B'. Define J_E(f') as the minimum order along E of the coefficients of the nonzero d-form

    f'^*(dy1 wedge ... wedge dyd)

in a smooth local d-form frame on the retained neighborhood of E. Dominance makes this form nonzero. Thus J is a finite nonnegative integer. Changing smooth local coordinates multiplies the target volume form by a holomorphic unit and changes the source coefficient frame by an invertible holomorphic matrix; J does not change. There is no global volume-form requirement.

If S is already a divisor, stop. Otherwise c=codim S>=2. Blow up the coherent ideal of the reduced analytic subset S in B'. This blow-up is a proper compact analytic space T and is bimeromorphic over B'. It can be singular globally. Over the smooth part of S it is exactly the blow-up of a smooth center and is smooth.

At a generic point of E mapping to the smooth part of S, choose coordinates with S={y1=...=yc=0}. Let

    m=min_{1<=i<=c} ord_E(f'^*yi)>=1.

After choosing the least-order coordinate, say y1, and shrinking about a generic point of E, write f'^*y1=z1^m u, where u is a holomorphic unit. Every quotient f'^*yi/f'^*y1 is holomorphic there. The map therefore lifts holomorphically to the y1-chart of T on this neighborhood. This chart has coordinates

    s=y1, t2=y2/y1,...,tc=yc/y1,y_(c+1),...,yd.

It is smooth, including its exceptional divisor. Its map to B' satisfies the exact identity

    dy1 wedge ... wedge dyd
      =s^(c-1) ds wedge dt2 wedge ... wedge dtc
         wedge dy_(c+1) wedge ... wedge dyd.

Take the main component of the graph of this meromorphic lift; it is proper over the compact G and is an isomorphism on the displayed neighborhood of the generic E. Now resolve T by a proper bimeromorphic map rho:T_tilde->T which is an isomorphism over the entire smooth part of T. The new target T_tilde is smooth and compact. Near the generic image of E, rho is an isomorphism, so the same local lift persists. Take the main graph of the resulting meromorphic lift to T_tilde. Its projection again preserves the generic neighborhood of E. Composition with the old target modification gives a smooth compact modification of B.

The resolution introduces no change at the generic E image, because that image lies in the smooth blow-up chart. Pulling back the displayed Jacobian identity yields

    J_new=J_old-(c-1)m.

The new map is holomorphic on the retained smooth neighborhood, so J_new>=0. Each step with codim S>=2 strictly decreases the nonnegative integer J. Therefore the procedure terminates after at most the initial J such steps. The terminal image cannot be the whole target if the original image was proper: composition to B would otherwise make f(E)=B. Thus the terminal image is a prime divisor F.

This argument imports proper analytic blow-up, the proper mapping theorem, and resolution preserving the smooth locus. It proves its own termination and generic-lift assertions. It does not appeal to an unproved global lifting of Z or to resolution of a graph that might alter the generic E.

## Ideal orders and the ramification normal form

At a very general smooth point of E mapping to a smooth point of F, the map E->F has tangential rank d-1. This follows from dominance in characteristic zero; its critical values lie in a proper analytic subset. Write y1=0 for F. Then f'^*y1=z1^e u with e>=1 and u a holomorphic unit. Absorb a local e-th root of u into z1. Taking f'^*y2,...,f'^*yd as d-1 source coordinates gives the exact local normal form

    f'(z1,z2,...,zd,z')=(z1^e,z2,...,zd).

The extra coordinates z' may be absent. For an ideal sigma^*b of generic order a along F, one local generator has form y1^a times a unit at a generic point of F and all generators are divisible by y1^a. Pullback then has order ea along E. This proves the ideal identity. No finite generation or uniform very-general point across infinitely many ideals is required: the identity is assessed for each ideal separately.

## Lelong identity, including a residual potential infinite on F

Add a smooth local function to w composed sigma so that it is psh. Let a be its generic Lelong number along F. By divisorial Siu decomposition, locally

    w composed sigma = a log|y1|^2 + R + smooth,

where R is psh and its generic Lelong number along F is zero. Our convention is dd^c=i/(2 pi) partial barpartial, and log|y1|^2 has divisor coefficient one. The generic value zero means that the full point Lelong number of R is zero at very general points of F, after discarding the countable union of its positive Lelong level sets intersected with F. This does not require R restricted to F to be finite.

Fix such a point of F and any t>0. Skoda local integrability makes exp(-t R) locally integrable for every fixed t. In the above ramification normal form, the pushforward of smooth volume under z1->z1^e has a constant multiple of the normal weight

    |y1|^(2/e-2).

For e>1 this weight lies locally in L^p for every 1<p<e/(e-1); for e=1 it is bounded. Choose one such p. Holder's inequality and Skoda applied to tp' R imply that exp(-t R composed f') is locally integrable for every t>0. Integration in the free coordinates only contributes a bounded smooth factor on a product neighborhood.

If R composed f' had positive generic divisor coefficient a'>0 along E, its Siu decomposition would bound it above by a' log|z1|^2 plus a locally bounded-above residual psh function. The exponential exp(-t R composed f') would then be nonintegrable in the normal variable whenever t a'>=1. This contradiction proves nu(R composed f',E)=0. Hence the full pulled-back generic Lelong number is ea. The possible condition R|F identically minus infinity is handled by integrability and is not silently excluded.

In the horizontal case f(E)=B, near a very general point of E the restriction E->B is a submersion. Extend its coordinates to a source chart. The pulled-back potential depends on the base coordinates and has no divisor coefficient along the independent normal coordinate of E. Alternatively the same Skoda/submersion argument gives zero. Every ideal is a unit at a generic base point, giving order zero.

## Apply independently to every divisor in the Hopf trace problem

For n>=3 let q:H_n->P^(n-1) be the scalar Hopf elliptic bundle. Given any smooth compact modification pi:Y'->H_n and prime E on Y', the map f=q composed pi is proper and dominant. Apply the lemma to this individual E. If its image is proper it becomes a multiple e of a divisor F on one smooth compact modification of the projective base, giving both the ideal and Lelong identities above. If its image dominates the base both values are zero.

Consequently a closed-base exact trace w with nu(w composed sigma,F)=tau_B(F) on all base models pulls back to a genuine Hopf potential with simultaneous exact coefficients tau_Hn(E) on all Hopf models, provided the actual multiplier-ideal submersion identity b_t pulled back = a_t has independently been established. Taking limits of ideal orders preserves the factor e because e is fixed for the chosen E. This is a candidate extension of the current surface extraction step, not a grant of the rest of original P18.

The full invariant trace-envelope descent and ideal-type/addition/analytic-model conclusions would follow by revisiting all the surface article's other steps in dimension n-1. The finite-level actual mass formula should become 2n b times the closed-base non-pluripolar mass, and a closed-base smaller-background majorant should give the bounds

    2n b (a/2)^(n-1) <= integral MA_(a alpha+b beta)(q^*w)
                          <= 2n b a^(n-1).

These are proposed higher-dimensional applications, not yet a fully assembled or independently reviewed manuscript. The separate all-dimensional BMP candidate is needed to certify that every proposed H_n target fails bounded mass. No positive-lower-mass claim or original P18 closure is made.

## Exact new primary application

Jaroslaw Wlodarczyk, Resolution of singularities of analytic spaces, Proceedings of the 15th Gokova Geometry-Topology Conference 2008, pp.31-63, published 2009. Primary publisher PDF: https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf . Local PDF SHA256 10072416e96eec62fb3bbca78e4bc9dc9efea364b4335126a22c17416aab222a.

Theorem 2.0.1 on printed p.34 (PDF p.4) supplies exactly a proper bimeromorphic resolution which is an isomorphism on the nonsingular part. Apply it to the reduced main analytic blow-up T, not directly to the source Z. Compactness of the resolved target follows from properness over compact T. The analytic theorem applies even if T is not projective or Kahler; neither property is needed for extraction or base closed-positive-current pullback.

Root read the complete exact statements at text lines149-275; the germ statements and full resolution-principle and gluing arguments at465-746; the full displayed marked-ideal algorithm proof at1232-1575; and the full final strengthening argument at1575-1645. Actual PDF pages4,5,11,12,13,14,15,30,31 were rendered and viewed. This does not claim that all preceding lemmas in the 33-page source or all its cited premises have been recursively verified. The source resolution theorem is an explicit supporting assumption subject to native independent source review.

Demailly's proper mapping theorem, smooth-center blow-up charts, Siu divisorial decomposition and Skoda integrability are the exact already-read primary statements recorded for the frozen surface article. Their application here is new, particularly the codimension-c Jacobian decrease and the source with generic smoothness only. They need new application judgments, not automatic reuse of the surface audit's acceptance.


## Entire current seven-page working manuscript

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\ord}{\operatorname{ord}}
\newcommand{\PP}{\mathbb P}
\newcommand{\I}{\mathcal I}
\newcommand{\cO}{\mathcal O}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Exact intrinsic traces on scalar Hopf manifolds\newline
and unbounded mass in every dimension at least three}
\author{}
\date{}
\begin{document}
\maketitle
\noindent\textbf{Working draft.} Mathematical review, independent
reconstruction and final comparison are pending. The unrestricted
non-K\"ahler trace problem remains open.
\begin{abstract}
For every scalar Hopf manifold of dimension at least three, we extend
the original smooth Xia--Zhang threefold construction to obtain
unbounded Monge--Amp\`ere mass. An exact comparison of angularly
integrated densities supplies the extension. On these targets, ambient
potentials pulled back from projective space nevertheless have exact
intrinsic traces on every smooth compact modification. The full trace
envelope descends to a closed trace on the projective base. A finite
divisorial extraction argument works in arbitrary base dimension:
blow up each divisor image and resolve the target without changing its
smooth locus, while the order of a pulled-back top form decreases.
We prove ideal-type compatibility, addition and analytic approximation,
and compute positive finite individual masses. These conclusions treat
the specified pullback data; unrestricted non-K\"ahler exactness and
ordinary-type independence are not claimed.
\end{abstract}

We use $d^c=\frac{i}{4\pi}(\bar\partial-\partial)$ and
$\ddc=\frac{i}{2\pi}\partial\bar\partial$.
Potentials have their genuine canonical representatives.
The ideal $\I(tu)$ is defined by local integrability of
$|g|^2e^{-tu}$, with no additional factor two.
An ideal restricted to a submanifold always means its coherent image
ideal. Non-pluripolar products with nonclosed smooth backgrounds use
bounded local products with smooth corrections and truncation
\cite[Section 2.1]{BGL}.

\section{Geometry and statement}
Fix an integer $n\ge3$ and put $d=n-1$. Let
\[
 M=(\mathbb C^{n+1}\setminus\{0\})/\langle z\mapsto ez\rangle,
 \qquad
 Y=H_n=(\mathbb C^n\setminus\{0\})/\langle z\mapsto ez\rangle.
\]
The inclusion of the first $n$ coordinates identifies $Y$ with a
linear submanifold of $M$. Projectivization gives the commuting square
\[
 \begin{matrix}Y&\longrightarrow&M\\
 q\downarrow&&\downarrow p\\
 B=\PP^d&\longrightarrow&\PP^n.
 \end{matrix}
\]
Both vertical maps are holomorphic submersions with connected elliptic
fiber $E=\mathbb C/(\mathbb Z+2\pi i\mathbb Z)$.
Normalize the Fubini--Study form $\kappa$ on $B$ by
$\int_B\kappa^d=1$. On $Y$, put
\[
 r=\log\|z\|^2\pmod 2,
 \quad \alpha=q^*\kappa=\ddc r,
 \quad \beta=dr\wedge d^cr,
 \quad \Omega_{a,b}=a\alpha+b\beta \quad(a,b>0).
\]
The differential of $r$ is global. The form $\beta$ has rank one,
is positive along the fibers, and $\int_E\beta=2$.
Thus $\Omega_{a,b}$ is Hermitian, $\int_Y\Omega_{a,b}^n=2nba^d$,
and $d\Omega_{a,b}=-b\,dr\wedge\alpha\ne0$.
The target is non-K\"ahler, since its first Betti number is one.
Section~\ref{sec:bmp} proves that it fails BMP for every $n\ge3$,
using the original threefold family of \cite{XZ}.

Let $U$ be genuine quasi-psh on $\PP^n$ with $\nu(U,B)=0$,
and let $u=p^*U$. Set
\[
 \mathfrak b_t=\I(tU)\cO_B,
 \qquad \mathfrak a_t=\I(tu)\cO_Y.
\]
These image ideals are nonzero. For a prime divisor $F$ over $B$,
write
\[
 \tau_B(F)=\lim_{t\to\infty}t^{-1}\ord_F\mathfrak b_t;
\]
define $\tau_Y$ from $\mathfrak a_t$ in the same way.
For any sufficiently large background $\Theta$, let
$T_\Theta$ denote the usc supremum of all $\Theta$-psh potentials
$v\le0$ satisfying $\nu(v,F)\ge\tau(F)$ on every smooth compact
modification. The definition includes all competitors.

\begin{theorem}\label{thm:main}
There is $a_0>0$, depending on the ambient curvature bound for $U$,
such that for $a\ge a_0$ and every $b>0$,
\[
 T_{\Omega_{a,b}}(u;Y)=q^*T_{a\kappa}(U;B).
 \tag{1}
\]
For every smooth compact modification $\pi:Z\to Y$ and every prime
divisor $D$ on $Z$, simultaneously,
\[
 \nu(T_{\Omega_{a,b}}(u;Y)\circ\pi,D)=\tau_Y(D).
 \tag{2}
\]
Equality (2) also holds for the trace in any Hermitian background
$\Omega\ge\Omega_{a,b}$. In the backgrounds in (1), the trace has
positive finite individual non-pluripolar mass and
\[
 \int_Y\MA_{\Omega_{a,b}}(T_{\Omega_{a,b}})
   =2nb\int_B\MA_{a\kappa}(T_{a\kappa}),
 \qquad
 2nb(a/2)^d\le\int_Y\MA_{\Omega_{a,b}}(T_{\Omega_{a,b}})
   \le2nba^d.
 \tag{3}
\]
The ideal class of the traces in (1) is independent of $a,b$ within
this range, is additive and positively homogeneous in the ambient
ideal trace data, and admits the dyadic analytic approximation
described below.
\end{theorem}

\section{Unbounded mass in all Hopf dimensions}\label{sec:bmp}
\begin{proposition}\label{prop:bmp}
For every $n\ge3$, $H_n$ fails the bounded mass property.
There are globally smooth $V_\eta$ with
$\alpha+\beta+\ddc V_\eta>0$ and total mass tending to infinity.
\end{proposition}
\begin{proof}
Use the original Xia--Zhang family, with its original heat scale
$\varepsilon_\eta=\eta^{1/\eta^2}$, not a new transport family.
Write $\xi\in\mathbb C^d$, $x=\log|\xi|^2$,
$w=\log z_0\pmod{\mathbb Z+2\pi i\mathbb Z}$ and
$\mu=e^x/(1+e^x)$ on the projective affine chart. Then
$r=w+\bar w+\log(1+e^x)$.
There are $n-2$ angular directions orthogonal to the radial direction.
Differentiating in these directions gives the identical angular
entries $A=(\mu+V_x)/\mu$. The radial/fiber block, in the frame
of \cite[Lemma 2.2]{XZ}, is
\[
 K_V=\begin{pmatrix}
 (\mu+V_{xx})/[\mu(1-\mu)]&
 (\mu+V_{x\bar w})/\sqrt{\mu(1-\mu)}\\
 (\mu+V_{wx})/\sqrt{\mu(1-\mu)}&1+V_{w\bar w}
 \end{pmatrix}.
\]
The background block has determinant one. The differential-form
expansion contains $-(1-\mu)V_x$, but its radial contribution
cancels that of the angular prefactor, giving exactly this block.
Thus the positivity conditions in every dimension are
\[
 1+V_{w\bar w}>0,\qquad \mu+V_x>0,\qquad
 Q[V]=V_{xx}+\mu-\frac{|\mu+V_{x\bar w}|^2}{1+V_{w\bar w}}>0.
\]
The source operator is $i\partial\bar\partial$; dividing both
source background forms by $2\pi$ gives ours with the same
numerical potential and these same ratios.

Normalize angular contact measure by mass one and write $dA_E$
for Haar probability measure on the elliptic fiber. The radial
Fubini--Study density on $\PP^d$ is
$d\mu^{d-1}\mu'\,dx=d\mu^d(1-\mu)\,dx$.
Since the fiber mass is two, the angularly integrated background
volume density is $2nd\mu^d(1-\mu)\,dx\,dA_E$.
Let $J_n(V;x,w)$ denote the angularly integrated smooth
Monge--Amp\`ere density. Multiplying by $A^{n-2}\det K_V$ gives
\[
 J_n(V;x,w)=\frac{n(n-1)}6(\mu+V_x)^{n-3}J_3(V;x,w).
 \tag{7}
\]
This compares integrated densities; the angular spheres in the
different dimensions each have their own probability normalization.

The original family is $V_\eta=W_\eta+g_\eta$.
It has all three strict positivity inequalities, is independent
of $x$ at the negative end, and is one constant at the positive end
\cite[Proposition 4.1]{XZ}. These endpoint properties give the
same global smooth extension with $\xi\in\mathbb C^d$.
Its construction also gives
\[
 \begin{gathered}
 \sup[W_{\eta,x}]_-=o(1),\qquad
 -m_\eta\le g_\eta'\le0,\qquad m_\eta=o(1),\\
 g_\eta''=r_\eta-m_\eta\psi,\qquad
 \int r_\eta=m_\eta,\quad\int\psi=1.
 \end{gathered}
\]
Here $r_\eta,\psi\ge0$ and $g_\eta=0$ on $x\le-2$.
Consequently $\mu+V_{\eta,x}\ge1/4$ for $x\ge0$ and small $\eta$.

The source proves $\int J_3(V_\eta)\to\infty$. To localize this
divergence, on $x<0$ one has
$W_\eta=F_\eta(\varepsilon_\eta,w)$, with no $x$ derivatives.
Since $\int_EF_{w\bar w}\,dA_E=0$, exact fiber integration gives
\[
 \int_E J_3(V_\eta;x,w)\,dA_E
   =12(\mu+g_\eta')[g_\eta''+\mu(1-\mu)].
\]
Use $0<\mu+g_\eta'\le\mu$ and
$\int|g_\eta''|\le2m_\eta$. The total mass on $x<0$ is at most
$12\int_{-\infty}^0\mu^2(1-\mu)\,dx+24m_\eta
=3/2+24m_\eta$.
The high amplitude of $F_{w\bar w}$ has been integrated exactly;
no uniform derivative bound is needed there.
It follows that $\int_{x\ge0}J_3(V_\eta)\to\infty$.
Equation (7) now gives
\[
 \int_{H_n}(\alpha+\beta+\ddc V_\eta)^n
 \ge\frac{n(n-1)}6\,4^{-(n-3)}\int_{x\ge0}J_3(V_\eta)
 \longrightarrow\infty.
\]
Every other Hermitian form $h$ dominates $c(\alpha+\beta)$
for some $c>0$. The potentials $cV_\eta$ have strictly positive
perturbed $h$, and their smooth masses dominate $c^n$ times
the preceding divergent masses. This proves BMP failure.
\end{proof}

\section{Divisorial extraction in arbitrary dimension}
\begin{lemma}\label{lem:extract}
Let $f:Z\to B$ be a dominant holomorphic map of connected smooth
compact complex manifolds, with $\dim B=d$, and let $D$ be a prime
divisor on $Z$. Either $f(D)=B$, or there is a smooth compact
modification $\sigma:B'\to B$ such that $f$ lifts holomorphically
near generic $D$ and $D$ dominates a prime divisor $F$ on $B'$.
For an integer $e\ge1$, every nonzero coherent ideal $\mathfrak b$
and every genuine quasi-psh $w$ on $B$ satisfy
\[
 \ord_D f^*\mathfrak b=e\ord_F\sigma^*\mathfrak b,
 \qquad \nu(w\circ f,D)=e\nu(w\circ\sigma,F).
 \tag{8}
\]
In the horizontal case both orders and generic Lelong numbers are zero.
\end{lemma}
\begin{proof}
Maintain a compact analytic graph proper over $Z$ which is an
isomorphism near generic $D$, with a dominant map to a smooth
compact modified base. The graph may be singular away from this
unchanged neighborhood. The divisor image $S$ is irreducible
analytic by the proper mapping theorem
\cite[Chapter II, Theorem 8.8]{Dem}.
Near generic $D$, define $J_D(f)$ as the minimum order of the
coefficients of $f^*(dy_1\wedge\cdots\wedge dy_d)$ in a smooth
source frame. Dominance gives a finite nonnegative integer,
independent of the local smooth coordinate choices.

If $S$ has codimension $c\ge2$, blow up its reduced coherent ideal.
The blowup can be singular globally, but it is smooth over the
smooth part of $S$. There use $S=\{y_1=\cdots=y_c=0\}$ and let
$m=\min_{i\le c}\ord_D f^*y_i\ge1$.
Choose $y_1$ of least order and shrink at generic $D$ so its
leading coefficient is a unit. All ratios $f^*y_i/f^*y_1$ are
holomorphic there, giving a lift to the smooth blowup chart
\[
 (y_1,\ldots,y_c)=(s,st_2,\ldots,st_c).
\]
Take the main graph of this lift. Resolve the target blowup using
a proper resolution which is an isomorphism on its whole smooth
locus \cite[Theorem 2.0.1]{Wlo}. The new target is smooth and
compact. The lift at generic $D$ is preserved, since its image
lies in that smooth locus. Taking the main graph of the resulting
meromorphic lift again preserves the generic source neighborhood.

The smooth-center Jacobian identity is
\[
 dy_1\wedge\cdots\wedge dy_d
   =s^{c-1}ds\wedge dt_2\wedge\cdots\wedge dt_c
                  \wedge dy_{c+1}\wedge\cdots\wedge dy_d.
\]
The target resolution is locally an isomorphism here. Therefore
\[
 J_D(f_{\rm new})=J_D(f)-(c-1)m\ge0.
\]
Each step strictly decreases $J$. After finitely many steps the
image has codimension one; it cannot dominate the target if its
original image was proper. This proves extraction without a
resolution of the source graphs that might change generic $D$.
Generic ideal generators along $F$ are powers of its equation
times a unit ideal, giving the first equality in (8).

At generic smooth points, tangential dominance $D\to F$ gives
rank $d-1$. Absorb a unit into a local normal coordinate using
an $e$-th root, and use the tangential base coordinates as source
coordinates. The exact local form is
\[
 (z_1,z_2,\ldots,z_d,z')\longmapsto(z_1^e,z_2,\ldots,z_d).
\]
After a smooth local correction, divisorial Siu removal writes
$w\circ\sigma=c\log|y_1|^2+R$, with $R$ psh and generic
Lelong number zero on $F$
\cite[Chapter III, (8.15)--(8.16)]{Dem}.
At a very general point of $F$ its full point Lelong number is zero.
Skoda's lemma gives integrability of $e^{-tR}$ for each $t>0$
\cite[Lemma 5.6(a)]{DemAM}.
For $e>1$ choose $1<p<e/(e-1)$. The ramification density
$|y_1|^{2/e-2}$ lies in $L^p$, so change of variables and
H\"older, using Skoda for $tp'R$, give
\[
 \int e^{-tR(z_1^e,z_2,\ldots,z_d)}dV_z
 =C_e\int e^{-tR(y)}|y_1|^{2/e-2}dV_y<\infty.
\]
Free variables contribute a harmless product factor. For $e=1$
use Fubini. A positive generic divisor coefficient $c'$ of the
residual pullback would force nonintegrability when $tc'\ge1$.
Its coefficient is therefore zero, and the logarithm gives $ec$.
This proves the Lelong equality, including when $R|_F\equiv-\infty$.
In the horizontal case $D\to B$ is a submersion at very general
points. Skoda and Fubini give zero generic coefficient; every
nonzero ideal is generically a unit there.
\end{proof}

\section{Ideal pullback and the full envelope}
\begin{lemma}\label{lem:ideals}
For a holomorphic submersion $q$ and a genuine quasi-psh potential
$v$ on its base, $\I(tq^*v)=q^*\I(tv)$ for every real $t>0$.
In the geometry above, $\mathfrak a_t=q^*\mathfrak b_t$ and
$\nu(u,Y)=0$.
\end{lemma}
\begin{proof}
Use local product coordinates $(x,y)$. The inclusion of the extended
base ideal follows by Fubini. For the reverse inclusion expand an
integrable holomorphic germ as $g(x,y)=\sum_\gamma g_\gamma(x)y^\gamma$.
The fiber coefficient estimate for holomorphic functions bounds
$|g_\gamma(x)|^2$ by a constant times the fiber integral of $|g|^2$.
Each coefficient therefore lies in $\I(tv)$ at the selected base point.
Every finite Taylor truncation belongs to its extended ideal $J$,
so $g\in J+(y)^N$ for all $N$. Krull intersection in the Noetherian
local analytic ring modulo $J$ gives $g\in J$. Smooth corrections
do not affect integrability. Apply the result to $p$ and restrict
the ideal to $Y$. Local submersion coordinates also preserve the
generic Lelong number along the inverse image of $B$.
\end{proof}

For clarity, recall the supplied closed-target trace construction.
Choose $a\kappa$ at least twice an admissible Hermitian background on
$B$ and discard finitely many indices of the ambient analytic
regularization $U_m$. The normalized ordinary analytic models
\[
 w_j=P_{a\kappa}[U_{2^j}|_B]
\]
decrease to $w=T_{a\kappa}(U;B)$.
The trace majorant lies in $\PSH(B,a\kappa/2)$ and is below $w$.
Closed mass monotonicity and the smaller-background expansion give
$\int_B\MA_{a\kappa}(w)\ge(a/2)^d$, while the closed upper bound is
$a^d$. The decreasing positive-mass model theorem
\cite[Proposition 3.1.12]{SGPT} now gives, for every divisor $F$ over $B$,
\[
 \nu(w,F)=\lim_j\nu(w_j,F)
  =\lim_j2^{-j}\ord_F\mathfrak b_{2^j}=\tau_B(F).
 \tag{6}
\]
The model and positive-mass hypotheses are essential; arbitrary
decreasing quasi-psh convergence would not imply this equality.
The closed-target construction and analytic envelope properties are
the known trace background, rather than conclusions imported to $Y$.

\begin{proof}[Proof of Theorem \ref{thm:main}]
Apply Lemma \ref{lem:extract} to $q\circ\pi$ for every target
modification $\pi:Z\to Y$. Equations (8), (6) and Lemma
\ref{lem:ideals} give
$\nu(q^*w\circ\pi,D)=\tau_Y(D)$ for each divisor, so $q^*w$ is
an exact competitor.

The compact elliptic group acts along the fibers, preserving
$\alpha,\beta$ and every $\mathfrak a_t$. It consequently preserves
the full trace competitor family, including its constraints on all
modifications. Its usc envelope is invariant and descends to a
genuine quasi-psh potential on $B$ by local sections. For a basic
potential $q^*v$, the background inequality is equivalent to
$a\kappa+\ddc v\ge0$. Indeed wedge the background inequality
with the smooth semipositive $\beta$ and push forward by $q$.
Since $\beta^2=0$ and its fiber integral is two, the resulting
positive current is $2(a\kappa+\ddc v)$. Conversely add $b\beta\ge0$.

Every base modification $B'\to B$ lifts to the smooth compact
modification $Y\times_B B'\to Y$. The inverse image of a prime divisor
$F$ is prime, since the elliptic fibers are connected; at generic
points its multiplicity is one. Thus the descended trace envelope
satisfies every base constraint, and is at most $w$. The opposite
inequality follows from the exact competitor $q^*w$. This proves
(1) and (2). For $\Omega\ge\Omega_{a,b}$ the same exact competitor
lies below $T_\Omega$, so
$\tau_Y(D)\le\nu(T_\Omega,D)\le\nu(q^*w,D)=\tau_Y(D)$.

For $v_j=\max(v,-j)$ on the base, actual bounded local products give
\[
 (\Omega_{a,b}+\ddc q^*v_j)^n
   =nb\,\beta\wedge q^*(a\kappa+\ddc v_j)^d,
\]
since the horizontal current has rank at most $d$ and $\beta^2=0$.
Multiply by $\mathbf1_{\{v>-j\}}$ and pass to the non-pluripolar
limit. Integrating over the fibers gives the factor $2nb$ in (3).
The closed-base bounds above give its two inequalities.
These are individual masses, not extremal volumes of all ordinary
representatives.

Different sufficiently large base backgrounds produce potentials
with the same numbers (6); the closed K\"ahler ideal criterion
\cite[Proposition 3.2.1]{SGPT} gives the same ideals at every real
weight. Lemma \ref{lem:ideals} transfers this to (1).
Intrinsic trace data are additive and positively homogeneous.
On the base, the sum of two exact realizers has the sum of their
divisorial numbers. The same criterion identifies its ideal class
with the trace for $U_1+U_2$, in a background with sufficient
curvature room. Positive scaling is identical. Pull back to $Y$.
This uses the ideal criterion on the projective base, and does not
assume a global valuative criterion on an arbitrary non-K\"ahler target.
\end{proof}

\section{Approximation and a point trace}
For the dyadic $w_j$ above, put $v_j=q^*w_j$. Compact elliptic
invariance applied to the full ordinary obstacle envelopes shows,
for $h\in\PSH(B,a\kappa)$,
\[
 P_{\Omega_{a,b}}[q^*h]=q^*P_{a\kappa}[h].
\]
At each finite obstacle level the competitor family is invariant;
its full supremum descends, and ordinary order is equivalent on
the base by surjectivity. Thus $v_j$ are the full ordinary analytic
models of the pulled-back restricted approximants. They decrease
to (1) in $L^1(Y)$: decreasing quasi-psh convergence is genuine,
or one can integrate a fixed invariant volume along the fibers.
For every divisor $D$ over $Y$, (6) and (8) yield
\[
 \nu(v_j,D)\longrightarrow\tau_Y(D).
\]
The same potentials pulled back to any target modification converge
in $L^1$ there, by quasi-psh compactness and uniqueness off the
exceptional set. This assertion supplies no convergence theorem
for extremal non-K\"ahler singularity volumes or capacities.

A concrete trace involving exceptional divisors is obtained from
\[
 U([z_0:\cdots:z_n])
  =\log\frac{\sum_{i=0}^{n-2}|z_i|^2}{\sum_{i=0}^{n}|z_i|^2},
 \qquad B=\{z_n=0\}.
\]
Its generic number along $B$ is zero, and its restricted image
ideals are
\[
 \mathfrak b_t=\mathfrak m_P^{\max(\lfloor t-d+1\rfloor,0)},
 \qquad P=[0:\cdots:0:1]\in B.
\]
The formula follows from the normal radial integrability condition
$k>t-d$ in $d$ normal coordinates to the ambient singular line.
Consequently $\tau_Y(D)=\ord_Dq^*\mathfrak m_P$ on every model.
The genuine potential $q^*(U|_B)$ is an explicit exact realizer,
singular along the elliptic fiber over $P$. For $a>1$,
\[
 \int_Y\MA_{\Omega_{a,b}}(q^*(U|_B))=2nb(a^d-1).
\]
On the point blowup the horizontal current, after removing the
exceptional divisor $F$, has class $aH-F$ and smooth semipositive
representative $(a-1)\sigma^*\kappa+\eta$. Here $\eta$ is the
pullback of the Fubini--Study form by the resolved projection to
$\PP^{d-1}$. The mixed intersections of $H$ and $F$ vanish,
$H^d=1$ and $F^d=(-1)^{d-1}$, giving $(aH-F)^d=a^d-1$.
Its smooth product off $F$ is the pullback of the actual
non-pluripolar product, and a smooth measure charges no divisor.
The displayed potential need not equal the normalized trace envelope.

\begin{remark}
The theorem treats arbitrary genuine ambient $U$ with the stated
generic condition, including nonanalytic data and cases where
$U|_B$ is identically $-\infty$; image ideals, not naive restriction,
define the trace. The base has arbitrary dimension $d\ge2$. No finite selection
of exceptional divisors replaces the simultaneous constraint.
Ideal-type compatibility is asserted for the invariant backgrounds
in (1). Exactness in larger arbitrary backgrounds follows by the
sandwich argument, but ordinary-type independence is not claimed.
\end{remark}

\begin{thebibliography}{9}
\bibitem{BGL} S. Boucksom, V. Guedj and C. H. Lu,
\emph{Volumes of Bott--Chern classes}, arXiv:2406.01090.
\bibitem{Dem} J.-P. Demailly, \emph{Complex Analytic and Differential
Geometry}, Harvard-hosted June 2012 manuscript.
\bibitem{DemAM} J.-P. Demailly, \emph{Analytic Methods in Algebraic
Geometry}, Surveys of Modern Mathematics 1, 2012.
\bibitem{SGPT} M. Xia, \emph{Singularities in global pluripotential
theory}, lecture manuscript, July 18, 2026 version,
\url{https://mingchenxia.github.io/Lectures/SGPT_final.pdf}.
\bibitem{Wlo} J. W\l{}odarczyk,
\emph{Resolution of singularities of analytic spaces},
Proceedings of the 15th G\"okova Geometry--Topology Conference
(2008), 31--63, published 2009,
\url{https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf}.
\bibitem{XZ} M. Xia and K. Zhang,
\emph{A counterexample to the bounded mass property},
arXiv:2608.21053v1.
\end{thebibliography}
\end{document}


## Whole root primary application audit, not an independent acceptance

{
  "created_utc": "2026-10-05T08:57:11.208665+00:00",
  "status": "root-primary-applications-assessed-native-gates-pending",
  "article_source": "papers/P18-Hopf-all-dimensions-exact-projective-traces.tex",
  "article_source_sha256": "151c057261d563a73ade3ce0b56b9b434d64d0d9a2ae61861f64aded27c5c422",
  "article_entire_root_read": true,
  "all_seven_actual_pdf_pages_viewed": true,
  "notes_entire_root_read": true,
  "native_mathematics_started": false,
  "independent_mathematical_acceptance": false,
  "original_fully_closed": false,
  "publication_called": false,
  "frozen_surface_input_hashes_unchanged": {
    "papers/P18-Hopf-threefold-exact-surface-traces.tex": "2fea6343489bf45080f8fcf14e9a98492b459ade346cf8e06849e9e75a98a9f3",
    "notes/P18-Hopf-surface-native-full-review-argument.md": "03a75fd10cc8ec0d002b56c0eb1f43a1b404e14a26caf54c1df29ef1f87ed89c",
    "inputs/P18-Hopf-surface-native-blind-reconstruction-input.json": "23971239a9f48cfe96a9165d1cfa25ca312c6735d626bf1864278bc9bfd95b86"
  },
  "new_resolution_application": {
    "source_url": "https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf",
    "source": "inputs/primary/Wlodarczyk-resolution-analytic-2009.pdf",
    "sha256": "10072416e96eec62fb3bbca78e4bc9dc9efea364b4335126a22c17416aab222a",
    "exact_statement": "Theorem 2.0.1, printed34/PDF4: proper bimeromorphic resolution is an isomorphism on the entire nonsingular part.",
    "whole_text_ranges_read": [
      [
        149,
        275
      ],
      [
        465,
        746
      ],
      [
        1232,
        1575
      ],
      [
        1575,
        1645
      ]
    ],
    "actual_pages_viewed": [
      4,
      5,
      11,
      12,
      13,
      14,
      15,
      30,
      31
    ],
    "application": "Resolve the reduced main blow-up of the target image. It is compact and smooth over generic smooth center. Properness preserves compactness; preservation of the smooth locus preserves the generic divisor lift. Source graph resolution is not assumed.",
    "root_new_jacobian_calculation": "J_new=J_old-(codim S-1)*min ord_D(f^*I_S); nonnegative J proves finite termination.",
    "recursive_verification_of_all_source_dependencies": false
  },
  "new_all_dimensional_mass_application": {
    "source": "inputs/primary/Xia-Zhang-2608.21053v1.pdf",
    "sha256": "0c39d024097dae97940403328cf6f8fb39fe3e21270edd02449948ea17303baa",
    "source_operator": "i partial barpartial = 2pi ours; divide source background by2pi, preserve numerical potentials.",
    "whole_text_ranges_read_this_application": [
      [
        1,
        126
      ],
      [
        215,
        320
      ],
      [
        600,
        875
      ]
    ],
    "source_entire_902_line_text_read_prior_unchanged": true,
    "actual_pages_fresh_viewed": [
      4,
      5,
      10,
      11,
      12
    ],
    "application": "Use unchanged original smooth heat family and original epsilon=eta^(1/eta^2), endpoint charts, strict three scalar inequalities, sup negative Wx=o(1), correction derivative [-m,0] and integral |gpp|<=2m.",
    "root_new_calculations": [
      "n-2 identical angular entries and unchanged 2x2 block",
      "Normalized radial FS density d mu^d(1-mu)",
      "Jn=n(n-1)/6*(mu+Vx)^(n-3)*J3",
      "Exact negative-side fiber average12(mu+gp)[gpp+mu(1-mu)] and total<=3/2+24m",
      "Positive-side lower bound mu+Vx>=1/4 yields divergence every n>=3"
    ],
    "uses_unaccepted_S02_new_heat_scale": false
  },
  "reassessed_other_primary_applications": [
    "Demailly proper mapping applies to each compact analytic graph and its strict divisor; smooth-center charts give exact codimension-c Jacobian factor.",
    "Siu generic/divisorial removal and Skoda zero-point-Lelong integrability apply in any dimension; Holder normal ramification weight is Lp for1<p<e/(e-1), with free variables integrated by Fubini.",
    "Closed-base SGPT3.1.12 decreasing ordinary models have positive actual closed mass from the smaller-background majorant in arbitrary dimension d. Each modified divisor is assessed separately.",
    "Closed Kahler base SGPT3.2.1 gives equality of ideals at every real weight. Actual submersion ideal identity pulls this to the Hopf target; no unrestricted non-Kahler valuative criterion is imported.",
    "BGL Section2.1 bounded locality and smooth-background corrections suffice at each truncation. Horizontal degree d and beta square zero give nb times pullback mass, fiber integral2; no BMP-dependent unbounded theorem used.",
    "Point blowup class aH-F has top intersection a^d-1. Ambient codimension-d integrability gives the exact real-weight image ideal exponents."
  ],
  "primary_bytes_and_old_exact_locators": "checks/P18-Hopf-surface-root-primary-application.pending.json; old source bytes and statements reused only, no automatic new mathematical acceptance.",
  "all_primary_premises_recursively_certified": false
}


## Pure statement-only reconstruction targets

# P18 general-dimensional scoped statement-only targets A--F

Retain every convention and the exact original task. These are requested
conclusions, not granted lemmas, source judgments or author proof steps.
The unrestricted original remains open; independently judge scoped adequacy.

A. For each integer n>=3 the scalar Hopf manifold
H_n=(C^n\{0})/<z->ez> fails BMP: for every Hermitian h there are
globally smooth real potentials with h+dd^c V>0 and total mass tending
to infinity. Verify the actual higher-dimensional positivity and mass,
using indispensable ordinary primary literature independently. The original
threefold theorem may be used only after exact source application checking.
No new heat-scale construction, pending S02 result or mere dimension analogy
is granted.

B. If f:Z->B is a dominant holomorphic map of connected smooth compact
complex manifolds of arbitrary base dimension d>=1 and D is a prime source
divisor, either f(D)=B and all nonzero coherent base ideal pullback orders
and genuine quasi-psh generic pullback Lelong numbers are zero, or there is
a smooth compact modification sigma:B'->B and a prime divisor F on B',
dominated by D under a holomorphic lift near generic D, and an integer e>=1
such that for every nonzero coherent ideal b and every genuine quasi-psh w,
ord_D(f^*b)=e ord_F(sigma^*b) and
nu(w composed f,D)=e nu(w composed sigma,F).
Prove existence, finiteness, all compact analytic auxiliary identifications
and both identities, including residual potentials infinite on F. No
extraction argument, termination invariant or finite-family shortcut is
granted. Any indispensable resolution or proper-mapping theorem requires
exact independent primary application verification.

C. Fix n>=3,d=n-1, M=H_(n+1), Y=H_n linearly embedded as the first
n coordinates. Projectivization gives p:M->P^n and q:Y->B=P^d,
where B is the linear hyperplane z_n=0. For any genuine quasi-psh U on
P^n with nu(U,B)=0, put u=p^*U. Prove nu(u,Y)=0 and
I(tu)O_Y=q^*(I(tU)O_B) for every real t>0, using actual image ideals.
Prove the submersion multiplier-ideal identity at every real weight.

D. Normalize kappa=FS on B by integral kappa^d=1, and set
r=log||z||^2 modulo two, alpha=q^*kappa, beta=dr wedge d^c r,
Omega_(a,b)=a alpha+b beta. Prove that there is a0 depending on ambient
curvature room such that for all a>=a0 and b>0 the FULL intrinsic envelope
T_Omega(u;Y)=q^*T_(a kappa)(U;B), and its generic Lelong numbers equal
every intrinsic tau_(Y,u)(D) on every smooth compact target modification.
Exactness also holds in every Hermitian Omega>=Omega_(a,b). Verify every
competitor and every exceptional divisor, not only selected modifications.
The targets are genuinely non-Kahler and fail BMP by A.

E. In the invariant backgrounds in D, prove positive finite INDIVIDUAL
trace mass, the actual formula integral_Y MA_Omega(T)=
2nb integral_B MA_(a kappa)(T_base), and bounds
2nb(a/2)^d<=integral_Y MA_Omega(T)<=2nb a^d.
Prove independence of the IDEAL class across these large invariant
backgrounds, addition and positive homogeneity with appropriate curvature
room. Prove full ordinary obstacle-envelope pullback for basic potentials,
and full dyadic restricted analytic model approximants decreasing in L1
on Y and every modification, whose generic Lelong numbers converge to
each intrinsic order. Do not infer ordinary-type independence or extremal
ordinary singularity volumes from these individual masses. Do not apply
a BMP-dependent unbounded product theorem on a target failing BMP.

F. For U=log(sum_(i=0)^(n-2)|z_i|^2 / sum_(i=0)^n|z_i|^2) on P^n
and B={z_n=0}, prove the image ideals are
b_t=m_P^max(floor(t-d+1),0), P=[0:...:0:1] in B, and the profile on Y
is ord_D(q^*m_P) for every prime divisor on every target modification.
The genuine potential q^*(U|B) is an exact realizer with actual mass
2nb(a^d-1) for a>1. Equality of this potential with the normalized full
trace envelope is not requested.

Independently verify all indispensable primary claims and each application.
Produce full ordinary proof notes with valid earlier-note support references
and retain all genuine gaps. The requested model is gpt-6.1-sol xhigh.



## Whole initial full review; verdict is not a mathematical premise

{
  "verdict": "PASS",
  "report": "PASS for the explicitly scoped sufficient-condition alternative: projective pullback trace data on scalar Hopf manifolds H_n, for every n≥3. The argument does not resolve unrestricted P18. Its substantive extensions are the all-dimensional BMP counterexample and extraction of every exceptional divisor over an arbitrary-dimensional projective base. The conclusions remain restricted to the stated ambient pullback data.\n\n1. The higher-dimensional mass calculation is correct. Direct differentiation gives n−2 angular entries (μ+V_x)/μ and the displayed radial/fiber block. Its determinant is (1+V_{w bar w})Q[V]/(μ(1−μ)); the background block has determinant one. Thus the three positivity inequalities are dimension independent. Dividing the Xia–Zhang background and operator by 2π preserves the numerical potentials. Angular integration gives background density 2n(n−1)μ^(n−1)(1−μ), hence J_n=[n(n−1)/6](μ+V_x)^(n−3)J_3. These are independently verified calculations, not dimension analogy. The required original family and endpoint properties are present in [Xia–Zhang, Lemmas 2.1–2.3 and Proposition 4.1](https://arxiv.org/pdf/2608.21053v1).\n\nOn x<0, W has no x derivatives, so exact fiber integration removes F_{w bar w} and yields 12(μ+g′)[g″+μ(1−μ)]. Since 0<μ+g′≤μ and ∫|g″|≤2m, its integral is at most 3/2+24m. Consequently the threefold divergence occurs on x≥0, where μ+V_x≥1/4 for small η. The density identity then proves divergence in every n≥3. The endpoint descriptions give genuine smooth global potentials in all these dimensions. For any Hermitian h≥c(α+β), the potentials cV_η are admissible and their masses dominate c^n times this divergent mass. This establishes BMP failure for every Hermitian metric, without asserting anything about positive lower mass.\n\n2. Divisorial extraction terminates as claimed. At each stage the auxiliary graph can be represented by the main component of a proper fiber product; it is compact and retains the original smooth neighborhood of generic D. Its divisor image is analytic. At a smooth generic center S of codimension c≥2, a least-order coordinate has pullback z_1^m times a unit, so the displayed coordinate ratios are holomorphic. The target blowup is smooth in that chart. The resolution theorem preserves this entire smooth locus, hence preserves the generic lift. The Jacobian identity gives J_new=J_old−(c−1)m, with J_new≥0. Therefore the process stops after finitely many steps, at a divisor image. These applications use [analytic blowups](https://arxiv.org/pdf/1501.01129), [proper mapping](https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf), and [smooth-locus-preserving resolution](https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf) with their hypotheses satisfied.\n\nThe terminal normal form (z_1,…,z_d,z′)↦(z_1^e,z_2,…,z_d) proves the ideal-order identity. For Lelong numbers, remove the generic divisorial logarithm. The residual has zero point Lelong number at very general points of F. Applying Skoda to every positive multiple, then Hölder with the ramification weight |y_1|^(2/e−2), proves exponential integrability of its pullback at every weight. A positive residual divisor coefficient would contradict this integrability when t times that coefficient is at least one. Thus the residual coefficient is zero, including when its restriction to F is identically −∞. The horizontal case follows from generic submersion coordinates. This checks both identities for every ideal and potential individually; no common finite selection of models is assumed.\n\n3. The multiplier-ideal submersion proof is valid at every real weight. Fiber coefficient estimates put each Taylor coefficient in the base ideal. Finite Taylor truncations lie in its extended ideal, and Krull intersection supplies membership of the full germ. The other inclusion is Fubini. Restricting this identity gives the actual image ideal a_t=q* b_t. Local product coordinates also establish ν(p*U,Y)=0. Neither step uses the potentially undefined naive restriction U|B.\n\n4. The closed-base exactness argument establishes its essential positive-mass antecedent. After choosing sufficient curvature room, the supplied restricted analytic models decrease to w. A common aκ/2-psh competitor z lies below w. Expanding its closed-background product gives mass(z in aκ)≥(a/2)^d; closed mass monotonicity transfers this lower bound to w, while comparison with zero gives mass(w)≤a^d. Thus the positive-mass model result applies. Together with preservation of each finite analytic singularity type, it gives ν(w,F)=lim_j 2^(−j)ord_F(b_(2^j))=τ_B(F). The relevant statements were checked in [Xia’s lecture manuscript](https://mingchenxia.github.io/Lectures/SGPT_final.pdf); the comparison is confined to the Kähler base, using [closed mass monotonicity](https://arxiv.org/pdf/1705.05796). Arbitrary decreasing quasi-psh convergence is not substituted for the model theorem.\n\nFor each divisor D on each Y-modification, extraction applied to q∘π gives the same factor e in the ideal and Lelong identities. Therefore the single potential q*w realizes all τ_Y(D) simultaneously. Horizontal divisors have both quantities zero. The quantifier over all modifications is retained throughout.\n\n5. Full envelope descent is valid. The elliptic group preserves the background, the image ideals, and the entire constraint family. Its usc envelope is invariant and descends through local sections. For basic potentials, wedging with β and pushing forward proves equivalence of Ω_(a,b)-positivity and aκ-positivity on the base. Every base modification lifts to the smooth compact fiber product; the inverse image of its prime divisor is irreducible with generic multiplicity one. Hence the descended envelope satisfies every base constraint and is bounded above by w. The exact competitor gives the reverse inequality. In a larger arbitrary background Ω≥Ω_(a,b), the sandwich τ_Y(D)≤ν(T_Ω,D)≤ν(q*w,D)=τ_Y(D) proves exactness, without asserting descent or type independence there.\n\n6. The mass and type conclusions have the correct scope. At bounded truncation level, horizontal degree and β²=0 give (Ω_(a,b)+dd^c q*v_j)^n=nb β∧q*(aκ+dd^c v_j)^d. Restricting to {v>−j} and taking the non-pluripolar limit yields the actual factor 2nb, since ∫_Eβ=2. This proves the stated positive finite individual mass and bounds. Only bounded local products from [BGL §2.1](https://arxiv.org/pdf/2406.01090) are needed; the BMP-dependent global unbounded-product theorem is not applied on H_n.\n\nEqual base divisorial profiles identify ideals at every real weight; submersion pullback transfers this to the invariant Hopf backgrounds. Addition and positive homogeneity concern ideal classes, with backgrounds large enough to contain the summed or scaled potentials. They do not assert equality of normalized envelopes under addition. The full ordinary obstacle envelopes descend by the same invariance argument, with ordinary order equivalent by surjectivity. Their dyadic analytic models decrease to the trace. Pullback to each modification remains genuine and is bounded below by the limiting pullback; decreasing convergence therefore gives L¹ convergence there. Extraction also gives the claimed divisorial limits. No ordinary-type independence, extremal singularity-volume convergence, or capacity convergence is inferred.\n\n7. The point example is correct, including the real-weight endpoints. In d normal variables, a term of degree k is integrable exactly when k>t−d, producing m_P^max(floor(t−d+1),0). Its asymptotic profile is ord_D(q*m_P). On the point blowup, the residual positive current has class aH−F and smooth semipositive representative (a−1)σ*κ+η. Mixed H/F intersections vanish, H^d=1 and F^d=(−1)^(d−1), so its top mass is a^d−1. The smooth product charges no exceptional divisor, giving the stated non-pluripolar mass 2nb(a^d−1). This example requires exceptional orders and is not merely exactness on one selected model.\n\nThe Hopf geometry and fiber normalization also check: H_n is diffeomorphic to S^(2n−1)×S¹, so b₁=1; it is non-Kähler. The form β has fiber mass two, Ω_(a,b) is Hermitian, and dΩ_(a,b)=−b dr∧α.\n\nHarmless bibliographic correction: the live SGPT PDF retrieved for this audit is dated October 4, 2026, rather than July 18. The required statements are present in that retrieved version. Its nonstandard use of “modification” was checked against the appendix’s realization of arbitrary prime divisors. The private audit assertions, file hashes, prior readings, and requested reconstruction targets were not treated as mathematical evidence or granted assumptions.",
  "passages": [
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/0",
      "statement": "Xia–Zhang, arXiv:2608.21053v1, Theorem 1.1, Lemmas 2.1–2.3 and Proposition 4.1: on scalar H₃, with source operator i∂bar∂ and source background α_src+β_src, the original family V_η=W_η+g_η using ε_η=η^(1/η²) extends smoothly, is strictly admissible, and has total Monge–Ampère mass tending to infinity. In its (x,w) coordinates, μ=e^x/(1+e^x), 1+V_(w bar w)>0, μ+V_x>0, and Q[V]>0. For x≤0, W_η=F_η(ε_η,w); V_η is constant at the positive end. Moreover sup[W_(η,x)]_−=o(1), −m_η≤g′_η≤0, m_η=o(1), g″_η=r_η−m_ηψ, r_η,ψ≥0, ∫r_η=m_η, ∫ψ=1, and g_η=0 on x≤−2.",
      "url": "https://arxiv.org/pdf/2608.21053v1",
      "quote": "does not satisfy the bounded mass property.",
      "premise": 0
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/1",
      "statement": "Xia–Zhang, arXiv:2608.21053v1, Theorem 1.1, Lemmas 2.1–2.3 and Proposition 4.1: on scalar H₃, with source operator i∂bar∂ and source background α_src+β_src, the original family V_η=W_η+g_η using ε_η=η^(1/η²) extends smoothly, is strictly admissible, and has total Monge–Ampère mass tending to infinity. In its (x,w) coordinates, μ=e^x/(1+e^x), 1+V_(w bar w)>0, μ+V_x>0, and Q[V]>0. For x≤0, W_η=F_η(ε_η,w); V_η is constant at the positive end. Moreover sup[W_(η,x)]_−=o(1), −m_η≤g′_η≤0, m_η=o(1), g″_η=r_η−m_ηψ, r_η,ψ≥0, ∫r_η=m_η, ∫ψ=1, and g_η=0 on x≤−2.",
      "url": "https://arxiv.org/pdf/2608.21053v1",
      "quote": "gη = 0 at the negative end and is constant at the positive end.",
      "premise": 0
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/2",
      "statement": "Barlet, Some examples due to H. Hironaka, §2: a coherent ideal on a reduced complex space whose zero set has empty interior admits a proper bimeromorphic analytic blowup, locally given by the closure of the generator graph; over a smooth center its usual blowup charts are smooth.",
      "url": "https://arxiv.org/pdf/1501.01129",
      "quote": "the blow-up exists and is unique.",
      "premise": 1
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/3",
      "statement": "Włodarczyk, Theorems 2.0.1–2.0.2: a reduced complex analytic space admits a proper bimeromorphic resolution by a manifold that is an isomorphism over its entire nonsingular locus; embedded analytic resolution produces a smooth strict transform and a simple-normal-crossing exceptional divisor.",
      "url": "https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf",
      "quote": "is an isomorphism over the nonsingular part",
      "premise": 2
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/4",
      "statement": "Remmert’s proper mapping theorem: the image of a complex analytic space under a proper holomorphic map is an analytic subset of the target.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "an analytic subset of Y",
      "premise": 3
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/5",
      "statement": "Siu’s generic-Lelong and divisorial decomposition theorems: for a closed positive current, its point Lelong number on an irreducible analytic subset equals its generic number outside countably many proper analytic subsets; subtracting the generic coefficient of a prime divisor leaves a positive current with zero generic coefficient there.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "T − mA[A] is positive.",
      "premise": 4
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/6",
      "statement": "Skoda integrability: if a psh function R has zero point Lelong number at x, then exp(−tR) is locally integrable near x for every finite t>0.",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/analmeth_book.pdf",
      "quote": "is integrable in a neighborhood of x",
      "premise": 5
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/7",
      "statement": "Krull intersection: for a finitely generated module F over a Noetherian local ring with maximal ideal m, and a submodule J, ∩_(k>0)(J+m^kF)=J.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "⋂_{k>0}(E + m^kF) = E.",
      "premise": 6
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/8",
      "statement": "Darvas–Di Nezza–Lu, Theorem 1.1: on a compact Kähler manifold, for smooth closed real backgrounds θ_i and θ_i-psh potentials u_i,v_i with u_i≥v_i−C_i, the total mixed non-pluripolar mass of the u_i is at least that of the v_i.",
      "url": "https://arxiv.org/pdf/1705.05796",
      "quote": "uj is less singular than vj for all j",
      "premise": 7
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/9",
      "statement": "Xia, SGPT Proposition 3.1.12: for a closed big background θ on compact Kähler (X,ω), ε_j↓0, and decreasing (θ+ε_jω)-psh ordinary model potentials φ_j with limit φ of positive θ-Monge–Ampère mass, ν(φ_j,E)→ν(φ,E) for every prime divisor E over X.",
      "url": "https://mingchenxia.github.io/Lectures/SGPT_final.pdf",
      "quote": "lim_{i∈I} ν(φ_i,E) = ν(φ,E).",
      "premise": 8
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/10",
      "statement": "Xia, SGPT Proposition 3.2.1: on a connected compact Kähler manifold, two genuine quasi-psh potentials have equal multiplier ideals at every real positive weight exactly when their generic Lelong numbers agree at every prime divisor over the manifold.",
      "url": "https://mingchenxia.github.io/Lectures/SGPT_final.pdf",
      "quote": "I(λφ) = I(λψ);",
      "premise": 9
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/11",
      "statement": "Demailly’s dyadic analytic regularization, stated in SGPT Theorem 1.6.2: for closed θ on compact Kähler X, every θ-psh φ admits decreasing analytic approximants tending to φ, with curvature losses ε_jω→0 and analytic singularity type (2^(−j), I(2^jφ)), using I(v) defined by exp(−v).",
      "url": "https://mingchenxia.github.io/Lectures/SGPT_final.pdf",
      "quote": "of type (2^−j, I(2^jφ))",
      "premise": 10
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/12",
      "statement": "Demailly’s dyadic analytic regularization, stated in SGPT Theorem 1.6.2: for closed θ on compact Kähler X, every θ-psh φ admits decreasing analytic approximants tending to φ, with curvature losses ε_jω→0 and analytic singularity type (2^(−j), I(2^jφ)), using I(v) defined by exp(−v).",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/dps5.pdf",
      "quote": "Subadditivity of the approximating sequence",
      "premise": 10
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/13",
      "statement": "Xia, SGPT Proposition 3.2.10: for an analytic θ-psh potential φ in a closed big background on a compact Kähler manifold, φ, P_θ[φ], and P_θ[φ]_I are ordinarily equivalent.",
      "url": "https://mingchenxia.github.io/Lectures/SGPT_final.pdf",
      "quote": "φ ∼ Pθ[φ] ∼ Pθ[φ]I.",
      "premise": 11
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/14",
      "statement": "Xia, SGPT Corollary B.1.1: every prime divisor over an irreducible compact complex space is realizable on a smooth model obtained by finitely many blowups with smooth centers.",
      "url": "https://mingchenxia.github.io/Lectures/SGPT_final.pdf",
      "quote": "can be realized as a prime divisor on Y.",
      "premise": 12
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/15",
      "statement": "Every odd Betti number of a compact Kähler manifold is even.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "are even.",
      "premise": 13
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/16",
      "statement": "The reduced ideal sheaf of an analytic subset of a complex manifold is coherent.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "a coherent analytic sheaf.",
      "premise": 14
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/17",
      "statement": "A dominant holomorphic map of irreducible reduced complex spaces has maximal differential rank equal to the target dimension on the smooth loci.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "dim Y = ρ(F).",
      "premise": 15
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/18",
      "statement": "BGL §2.1: products of currents with bounded quasi-psh potentials and arbitrary smooth backgrounds are defined by multilinearity with smooth corrections, are plurifine local and non-pluripolar, and are positive when the currents are positive; this bounded construction does not require BMP.",
      "url": "https://arxiv.org/pdf/2406.01090",
      "quote": "by forcing multilinearity",
      "premise": 16
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/19",
      "statement": "BGL §2.1: products of currents with bounded quasi-psh potentials and arbitrary smooth backgrounds are defined by multilinearity with smooth corrections, are plurifine local and non-pluripolar, and are positive when the currents are positive; this bounded construction does not require BMP.",
      "url": "https://arxiv.org/pdf/2406.01090",
      "quote": "is still local in the plurifine topology.",
      "premise": 16
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/20",
      "statement": "Włodarczyk, Theorems 2.0.1–2.0.2: a reduced complex analytic space admits a proper bimeromorphic resolution by a manifold that is an isomorphism over its entire nonsingular locus; embedded analytic resolution produces a smooth strict transform and a simple-normal-crossing exceptional divisor.",
      "url": "https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf",
      "quote": "the strict transform",
      "premise": 2
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/21",
      "statement": "Włodarczyk, Theorems 2.0.1–2.0.2: a reduced complex analytic space admits a proper bimeromorphic resolution by a manifold that is an isomorphism over its entire nonsingular locus; embedded analytic resolution produces a smooth strict transform and a simple-normal-crossing exceptional divisor.",
      "url": "https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf",
      "quote": "is smooth",
      "premise": 2
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/22",
      "statement": "Siu’s generic-Lelong and divisorial decomposition theorems: for a closed positive current, its point Lelong number on an irreducible analytic subset equals its generic number outside countably many proper analytic subsets; subtracting the generic coefficient of a prime divisor leaves a positive current with zero generic coefficient there.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "countable family",
      "premise": 4
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/23",
      "statement": "Demailly’s dyadic analytic regularization, stated in SGPT Theorem 1.6.2: for closed θ on compact Kähler X, every θ-psh φ admits decreasing analytic approximants tending to φ, with curvature losses ε_jω→0 and analytic singularity type (2^(−j), I(2^jφ)), using I(v) defined by exp(−v).",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/dps5.pdf",
      "quote": "is a decreasing sequence.",
      "premise": 10
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/24",
      "statement": "Skoda integrability: if a psh function R has zero point Lelong number at x, then exp(−tR) is locally integrable near x for every finite t>0.",
      "url": "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/analmeth_book.pdf",
      "quote": "If ν(ϕ, x) < 1",
      "premise": 5
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/25",
      "statement": "Barlet, Some examples due to H. Hironaka, §2: a coherent ideal on a reduced complex space whose zero set has empty interior admits a proper bimeromorphic analytic blowup, locally given by the closure of the generator graph; over a smooth center its usual blowup charts are smooth.",
      "url": "https://arxiv.org/pdf/1501.01129",
      "quote": "its projection on U is a proper modification of U.",
      "premise": 1
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/26",
      "statement": "Xia, SGPT Corollary B.1.1: every prime divisor over an irreducible compact complex space is realizable on a smooth model obtained by finitely many blowups with smooth centers.",
      "url": "https://mingchenxia.github.io/Lectures/SGPT_final.pdf",
      "quote": "smooth",
      "premise": 12
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/27",
      "statement": "Every odd Betti number of a compact Kähler manifold is even.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "b2k+1",
      "premise": 13
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/28",
      "statement": "Remmert’s proper mapping theorem: the image of a complex analytic space under a proper holomorphic map is an analytic subset of the target.",
      "url": "urn:xean:task",
      "quote": "Known background: a common competitor, the trace envelope, ideal/ordinary fixedness, convergence of restricted analytic envelopes, and pulled-background modification compatibility already hold without either mass property.",
      "premise": 3
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/29",
      "statement": "Xia, SGPT Proposition 3.2.1: on a connected compact Kähler manifold, two genuine quasi-psh potentials have equal multiplier ideals at every real positive weight exactly when their generic Lelong numbers agree at every prime divisor over the manifold.",
      "url": "urn:xean:task",
      "quote": "These intrinsic data depend only on the ambient ideal class and are additive and positively homogeneous.",
      "premise": 9
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/30",
      "statement": "Xia, SGPT Proposition 3.1.12: for a closed big background θ on compact Kähler (X,ω), ε_j↓0, and decreasing (θ+ε_jω)-psh ordinary model potentials φ_j with limit φ of positive θ-Monge–Ampère mass, ν(φ_j,E)→ν(φ,E) for every prime divisor E over X.",
      "url": "urn:xean:task",
      "quote": "Exact realization on curves, on Kahler targets in a sufficiently large closed background, under both mass properties, and for specified curve-fibration trace data is already known.",
      "premise": 8
    },
    {
      "id": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257/31",
      "statement": "Xia–Zhang, arXiv:2608.21053v1, Theorem 1.1, Lemmas 2.1–2.3 and Proposition 4.1: on scalar H₃, with source operator i∂bar∂ and source background α_src+β_src, the original family V_η=W_η+g_η using ε_η=η^(1/η²) extends smoothly, is strictly admissible, and has total Monge–Ampère mass tending to infinity. In its (x,w) coordinates, μ=e^x/(1+e^x), 1+V_(w bar w)>0, μ+V_x>0, and Q[V]>0. For x≤0, W_η=F_η(ε_η,w); V_η is constant at the positive end. Moreover sup[W_(η,x)]_−=o(1), −m_η≤g′_η≤0, m_η=o(1), g″_η=r_η−m_ηψ, r_η,ψ≥0, ∫r_η=m_η, ∫ψ=1, and g_η=0 on x≤−2.",
      "url": "urn:xean:task",
      "quote": "Alternatively give new substantive sufficient conditions on a genuinely non-Kahler target failing a mass property, beyond the listed curve and fibration cases.",
      "premise": 0
    }
  ],
  "premises": [
    "Xia–Zhang, arXiv:2608.21053v1, Theorem 1.1, Lemmas 2.1–2.3 and Proposition 4.1: on scalar H₃, with source operator i∂bar∂ and source background α_src+β_src, the original family V_η=W_η+g_η using ε_η=η^(1/η²) extends smoothly, is strictly admissible, and has total Monge–Ampère mass tending to infinity. In its (x,w) coordinates, μ=e^x/(1+e^x), 1+V_(w bar w)>0, μ+V_x>0, and Q[V]>0. For x≤0, W_η=F_η(ε_η,w); V_η is constant at the positive end. Moreover sup[W_(η,x)]_−=o(1), −m_η≤g′_η≤0, m_η=o(1), g″_η=r_η−m_ηψ, r_η,ψ≥0, ∫r_η=m_η, ∫ψ=1, and g_η=0 on x≤−2.",
    "Barlet, Some examples due to H. Hironaka, §2: a coherent ideal on a reduced complex space whose zero set has empty interior admits a proper bimeromorphic analytic blowup, locally given by the closure of the generator graph; over a smooth center its usual blowup charts are smooth.",
    "Włodarczyk, Theorems 2.0.1–2.0.2: a reduced complex analytic space admits a proper bimeromorphic resolution by a manifold that is an isomorphism over its entire nonsingular locus; embedded analytic resolution produces a smooth strict transform and a simple-normal-crossing exceptional divisor.",
    "Remmert’s proper mapping theorem: the image of a complex analytic space under a proper holomorphic map is an analytic subset of the target.",
    "Siu’s generic-Lelong and divisorial decomposition theorems: for a closed positive current, its point Lelong number on an irreducible analytic subset equals its generic number outside countably many proper analytic subsets; subtracting the generic coefficient of a prime divisor leaves a positive current with zero generic coefficient there.",
    "Skoda integrability: if a psh function R has zero point Lelong number at x, then exp(−tR) is locally integrable near x for every finite t>0.",
    "Krull intersection: for a finitely generated module F over a Noetherian local ring with maximal ideal m, and a submodule J, ∩_(k>0)(J+m^kF)=J.",
    "Darvas–Di Nezza–Lu, Theorem 1.1: on a compact Kähler manifold, for smooth closed real backgrounds θ_i and θ_i-psh potentials u_i,v_i with u_i≥v_i−C_i, the total mixed non-pluripolar mass of the u_i is at least that of the v_i.",
    "Xia, SGPT Proposition 3.1.12: for a closed big background θ on compact Kähler (X,ω), ε_j↓0, and decreasing (θ+ε_jω)-psh ordinary model potentials φ_j with limit φ of positive θ-Monge–Ampère mass, ν(φ_j,E)→ν(φ,E) for every prime divisor E over X.",
    "Xia, SGPT Proposition 3.2.1: on a connected compact Kähler manifold, two genuine quasi-psh potentials have equal multiplier ideals at every real positive weight exactly when their generic Lelong numbers agree at every prime divisor over the manifold.",
    "Demailly’s dyadic analytic regularization, stated in SGPT Theorem 1.6.2: for closed θ on compact Kähler X, every θ-psh φ admits decreasing analytic approximants tending to φ, with curvature losses ε_jω→0 and analytic singularity type (2^(−j), I(2^jφ)), using I(v) defined by exp(−v).",
    "Xia, SGPT Proposition 3.2.10: for an analytic θ-psh potential φ in a closed big background on a compact Kähler manifold, φ, P_θ[φ], and P_θ[φ]_I are ordinarily equivalent.",
    "Xia, SGPT Corollary B.1.1: every prime divisor over an irreducible compact complex space is realizable on a smooth model obtained by finitely many blowups with smooth centers.",
    "Every odd Betti number of a compact Kähler manifold is even.",
    "The reduced ideal sheaf of an analytic subset of a complex manifold is coherent.",
    "A dominant holomorphic map of irreducible reduced complex spaces has maximal differential rank equal to the target dimension on the smooth loci.",
    "BGL §2.1: products of currents with bounded quasi-psh potentials and arbitrary smooth backgrounds are defined by multilinearity with smooth corrections, are plurifine local and non-pluripolar, and are positive when the currents are positive; this bounded construction does not require BMP."
  ],
  "kind": "codex-report",
  "operationId": "1c2e0f88-0c2e-45b4-a161-d6ebd3ee5257",
  "reportedAt": "2026-10-07T17:34:14.037Z"
}


## Whole independent statement-only result and support graph

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "Independently checked primary inputs; analytic comparison and all-real ideal characterization on compact manifolds.",
      "detailedSummary": "Identifies exact primary resolution, proper-image, divisorial subtraction, Bergman approximation, subadditivity, strong-openness, Kähler model-convergence, and local product inputs. Proves analytic ordinary comparison through global ideal resolution and proves equality of all compact divisorial Lelong numbers iff equality of every real-weight multiplier ideal. External deep theorems remain mathematical inputs, not formally certified results.",
      "text": "Verified primary inputs and analytic comparison lemmas.\n\nUse d^c=i(barpartial-partial)/(4 pi), so dd^c=i partial barpartial/(2 pi) and dd^c log|s|^2=[s=0]. All functions mean their genuine canonical quasi-psh representatives, including values at poles.\n\nThe indispensable primary inputs were opened independently:\n\n(i) [Bierstone–Milman, Invent. Math. 128 (1997), 207–302](https://www.mahalex.net/teaching/seminars/gabber/Bierstone-Milman%20Canonical%20desingularization%20in%20characteristic%20zero.pdf): complex-analytic category (0.1)(2), compact embedded resolution Theorem 1.6, coherent ideal principalization Theorem 1.10, and compact abstract resolution Theorem 13.2. Compactness gives finite sequences. The published full article, rather than its earlier abbreviated draft, is used.\n\n(ii) [Grauert, Publ. Math. IHES 5 (1960)](https://www.numdam.org/item/PMIHES_1960__5__5_0.pdf), section 7, Satz 1, printed p.60: proper images of reduced complex spaces are analytic. Its primary proof identifies the image with the support of the coherent direct image of the structure sheaf.\n\n(iii) [Siu, Invent. Math. 27 (1974)](https://people.math.harvard.edu/~siu/siu_reprints/siu_analyticity_lelong_set_invent1974.pdf): the introduction and scanned printed pp.71–75 were inspected, including Theorem 2.12(iii), Proposition 3.2 and Theorem 3.4. These give analyticity of positive Lelong level sets and divisorial subtraction: the part of a positive closed (1,1) current on a smooth prime hypersurface is its generic coefficient times that hypersurface, and subtracting it leaves a positive closed current.\n\n(iv) [Demailly, arXiv:1401.5432v2](https://arxiv.org/pdf/1401.5432v2), Theorems 1.2 and 1.6, Remark 1.4, Lemma 1.10, Corollary 1.12 and Theorem 4.1.5: compact Hermitian Bergman approximation, analytic local ideal types, dyadic monotonicity, and I(lambda' w_m) contained in I(lambda w) for lambda'>lambda and sufficiently large m. The construction uses exp(-2m phi); substituting phi=w/2 gives the task’s I(mw) and coefficient m^{-1}log(sum|generators|^2). Smooth corrections do not change ideals.\n\n(v) [Demailly–Ein–Lazarsfeld](https://arxiv.org/pdf/math/0002035v2), analytic Theorem 2.6(ii): I(phi+psi) is contained in I(phi)I(psi). It applies locally to quasi-psh functions after bounded smooth correction and at arbitrary real weights.\n\n(vi) [Guan–Zhou, Ann. Math. 182 (2015), 605–616](https://annals.math.princeton.edu/wp-content/uploads/annals-v182-n2-p05-p.pdf), Theorem 1.1: a germ in I(tw) belongs to I(t'w) for some t'>t on a smaller neighborhood. Its convention is exp(-w).\n\n(vii) [Darvas–Xia, arXiv:2403.08259v2](https://arxiv.org/pdf/2403.08259v2), Proposition 2.1, pp.6–7: decreasing ordinary model potentials in closed backgrounds on a compact Kähler manifold have convergent non-pluripolar masses; positive limit mass implies convergence of generic Lelong numbers on every divisor over that manifold. The statement and proof were inspected. Theorem 2.2(iv) also verifies the exact dyadic ideal coefficient. This convergence proposition is used only on P^d below.\n\n(viii) [Bedford–Taylor, Acta Math. 149 (1982)](https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf), section 2, Theorem 2.1, Corollaries 2.2 and 2.8, and Theorem 6.9: bounded local products, multilinearity, integration by parts, and zero capacity of pluripolar sets. [BEGZ](https://arxiv.org/pdf/0812.3674v2), section 1.1, formula (1.1) and Proposition 1.4: local non-pluripolar truncation and locality. The local facts are used on Hopf charts; global Kähler finiteness is not transferred to Hopf manifolds.\n\n(ix) [Xia–Zhang, arXiv:2608.21053v1](https://arxiv.org/html/2608.21053v1), Theorem 1.1, Proposition 4.1 and its full proof: the radial family V_eta is constant at the positive end, has V_x=0 for x<=-2, has inf V_x>=-delta_eta with delta_eta tending to zero, satisfies its three positivity inequalities, and has threefold mass tending to infinity. The slope estimate follows from (4.3) and -m_eta<=g_eta'<=0 with m_eta=o(1). Their dd^c is i partial barpartial. Divide their background forms by 2 pi and KEEP the scalar potentials unchanged: omega+dd^c V=(omega_source+dd^c_source V)/(2 pi). Thus the threefold mass is divided by (2 pi)^3. No higher-dimensional assertion is imported.\n\nAnalytic comparison lemma. Let phi have a global coherent analytic singularity type on a compact manifold. If a genuine quasi-psh v satisfies nu(v composed pi,E)>=nu(phi composed pi,E) for every prime on every compact smooth modification, then v preceq phi. Resolve phi’s coherent ideal by (i). On the compact resolution, phi=L+O(1), where L is the smooth-metric logarithm of a finite effective real divisor. By (iii), subtracting its coefficients from the local positive current of v leaves a quasi-psh residual v composed pi-L with a fixed smooth lower Hessian bound. This residual is bounded above on the compact resolution. Hence v<=phi+C, including canonical pole values. Ordinary order conversely implies the Lelong inequalities.\n\nIf phi is theta-psh, P_theta[phi] is ordinarily equivalent to phi. The lower bound follows by normalizing phi. For the upper bound uniformly over competitors v<=0, use the same resolution. R_v=v composed pi-L has a common lower Hessian bound and satisfies R_v<=-L almost everywhere. Its positive part has uniformly bounded integral. Local submean estimates on finitely many charts bound sup R_v uniformly. Thus P_theta[phi]<=phi+C. The envelope has analytic singularity type and is ordinary model.\n\nDivisorial characterization of the ideal class. For any smooth compact modification pi and prime E put A_pi(E)=1+ord_E(Jac pi). Bergman approximation gives\n\nnu(w composed pi,E)-A_pi(E)/m <= ord_E I(mw)/m <= nu(w composed pi,E).\n\nFor the upper bound, the local extension estimate in the verified Bergman construction gives w<=w_m+O(1). For the lower bound, pull back integrability of a generator g. At generic E write g composed pi=s^r times a unit, Jac pi=s^{A-1} times a unit, and w composed pi=alpha log|s|^2+rho. The residual rho is locally bounded above after a smooth correction. The radial integral forces r-m alpha+A>0; equality already diverges. Taking the minimum generator order proves the bound. Consequently these ideal slopes converge to the generic Lelong number.\n\nSuppose nu(v,E)>=nu(w,E) on every compact smooth modification. Resolve I(mw) globally. Since nu(w_m,E)<=nu(w,E), analytic comparison gives v preceq w_m for each m. Given a germ g in I(tv), strong openness supplies t'>t with g in I(t'v). Thus g lies in I(t'w_m), and for sufficiently large m in I(tw) by (iv). Therefore I(tv) is contained in I(tw) at every real t>0. Conversely ideal inclusions imply the divisorial inequalities through the slope bounds. Equality of all compact divisorial numbers is therefore equivalent to equality of all real-weight multiplier ideals, also on compact non-Kähler manifolds. This argument does not presume that arbitrary local modifications globalize.\n\nThese are mathematical deductions using independently checked standard primary theorems; they are not formal proofs of those external theorems. Detailed source applications are retained in source_audit.txt, retrieval responses in sources/*.json, and the full note in notes/n1.txt. Rerun public-source download attempts with python fetch_sources.py.\n\nArtifacts: /workspace/research/native-workers/codex-EezmdX",
      "support": []
    },
    {
      "id": "n2",
      "summary": "A: every scalar Hopf H_n, n>=3, fails BMP for every Hermitian form, through the verified threefold family and an all-dimensional determinant comparison.",
      "detailedSummary": "Computes the full positive matrix and actual mass 2n(n-1) integral A^(n-2)Delta. The primary construction’s uniform negative-slope estimate bounds the extra angular factors below on the divergence region. Masses therefore diverge in every dimension n>=3, and scaling transfers the construction to every Hermitian background.",
      "text": "A: failure of BMP on every scalar Hopf H_n, n>=3.\n\nLet d=n-1 and E=C/(Z+2 pi i Z). On the affine projectivization chart write z=exp(w)(1,xi), xi in C^d. Set x=log|xi|^2 and mu=exp(x)/(1+exp(x)). Let alpha=dd^c log||z||^2 and beta=d log||z||^2 wedge d^c log||z||^2. They descend because log||ez||^2 changes by 2. Alpha is normalized FS pulled back from P^d, and beta has rank one and is positive on the vertical line. Thus omega=alpha+beta is Hermitian.\n\nUse exactly the primary radial functions V_eta verified in n1, with v_eta=V_eta. The background and dd^c operator are both the source’s ones divided by 2 pi; the scalar potential is unchanged. No new heat construction is introduced. The additional estimates give V_x=0 on x<=-2 and V_x>=-delta_eta everywhere, delta_eta tending to zero. Independence of x at the negative end and constancy in both variables at the positive end extend these functions smoothly across xi=0 and the hyperplane at infinity in every dimension.\n\nHere is the higher-dimensional positivity calculation. Since r=w+bar w+log(1+exp x), partial r=dw+mu partial x and\n\nalpha=(i/(2 pi))[mu partial barpartial x+mu(1-mu) partial x wedge barpartial x],\n\nchoose a radial vector in the xi-coordinate plane unit for 2 pi alpha, namely (mu(1-mu))^{-1/2} sum xi_j partial/partial xi_j, together with d-1 angular vectors unit for 2 pi alpha and annihilated by partial x, and the vertical vector partial/partial w. The radial vector is not the connection-horizontal lift. The matrix of 2 pi(omega+dd^c V_eta) has angular eigenvalue A/mu of multiplicity d-1, where A=mu+V_x, and radial/vertical block\n\n[(mu+V_xx)/(mu(1-mu)), (mu+V_x barw)/sqrt(mu(1-mu));\n (mu+V_wx)/sqrt(mu(1-mu)), 1+V_w barw].\n\nThe source inequalities are exactly A>0, B=1+V_w barw>0, and Q=mu+V_xx-|mu+V_x barw|^2/B>0. Hence the complete matrix is positive for every d>=2. At xi=0 the additional horizontal derivatives vanish and B>0 gives positivity; where V is constant positivity is immediate.\n\nPut Delta=(mu+V_xx)(1+V_w barw)-|mu+V_x barw|^2=BQ>0. The normalized FS radial probability density on C^d is d mu^(d-1)mu_x dx: FS^d has Lebesgue density d!/pi^d*(1+|xi|^2)^(-d-1), and spherical integration followed by |xi|^2=exp x gives the assertion. The determinant ratio to the background is (A/mu)^(d-1)Delta/mu_x. On the elliptic fiber beta has integral 2: w=s+it has periods 1 and 2 pi, and beta=ds wedge dt/pi. Angular integration is normalized to one. Thus the actual mass is\n\nM_n(V_eta)=2 n d integral_(R x E) A^(d-1)Delta dx dA_E,\n\nwhere dA_E is Haar probability measure. For V=0 this gives 2n, agreeing with integral omega^n.\n\nFor n=3,d=2, the independently verified source theorem and normalization give M_3(V_eta) tending to infinity, and integral A Delta=M_3/12. On x<=-2, all x derivatives of V vanish. Periodicity gives integral_E V_w barw=0. Therefore\n\nintegral_(-infinity,-2) integral_E A Delta dA_E dx=mu(-2)^2/2,\n\nindependently of eta. Set c0=mu(-2)/2>0. For sufficiently small eta, A>=c0 on x>=-2 by the uniform slope estimate. Hence\n\nM_n(V_eta)>=2 n d c0^(d-2)[M_3(V_eta)/12-mu(-2)^2/2],\n\nwhich tends to infinity for every n>=3. This verifies actual divergence rather than using a dimensional analogy.\n\nFor an arbitrary Hermitian h, compactness gives c>0 with h>=c omega. Then h+dd^c(c V_eta)>=c(omega+dd^c V_eta)>0, and monotonicity of smooth positive matrix determinants gives mass at least c^n M_n(V_eta). These are globally smooth real potentials. Thus v_+(h)=infinity for every h.\n\nThe source input is three-dimensional and is verified in n1; the full matrix, radial density and comparison are deductions here. verify_formulas.py checks determinants for n=3,...,8, FS densities for d=2,...,8, and normalization. These finite exact checks supplement the general proof. Evidence is in artifacts/formula_checks.json; rerun with python verify_formulas.py. Full note: notes/n2.txt.\n\nArtifacts: /workspace/research/native-workers/codex-EezmdX",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "B: finite compact analytic extraction for arbitrary-dimensional bases, with every ideal and quasi-psh pullback identity, including infinite residuals.",
      "detailedSummary": "A finite nonnegative order of the pulled top differential decreases by (codimension-1)e whenever the smooth image center is blown up. Compact resolution and source principalization supply the required global auxiliary spaces and lifts. Termination produces a base prime F; a generic ramified normal form proves both identities for every ideal and potential with the same F and e.",
      "text": "B: finite compact analytic extraction and pullback identities.\n\nLet f:Z->B be dominant between connected smooth compact manifolds, dim Z=m and dim B=d>=1, and let D be prime. All centers have reduced analytic structure. The proper-image theorem verified in n1 applies to the reduced compact D, so S=f(D) is compact irreducible analytic. Dominance makes the top differential nonzero.\n\nIf S=B, every nonzero coherent base ideal is a unit at generic B, so its pullback order along D is zero. The dominant restriction D->B has rank d at generic smooth D, making f a submersion there. Positive Lelong level sets of a genuine base quasi-psh function are proper analytic subsets. Dominance prevents D from lying in any of their pullbacks. Submersion preserves point Lelong numbers, so the generic pullback Lelong number along D is zero. This includes functions with poles.\n\nSuppose S is proper. At each stage take a smooth compact base B_j and a holomorphic lift f_j from a smooth compact modification Z_j of Z that is unchanged near generic D. Write D_j for the strict prime. Define k_j as the order along D_j of the nonzero section f_j^*(dx_1 wedge ... wedge dx_d) of Omega^d_(Z_j): it is the minimum coefficient order in a smooth source frame. It is finite and nonnegative. A base coordinate change multiplies by a unit, so k_j is intrinsic near the generic image.\n\nIf S_j=f_j(D_j) has codimension one, stop. Otherwise resolve S_j inside B_j by the compact embedded theorem of n1. The resulting smooth compact B_j^r has smooth strict center S_j^r of the same codimension c>=2 and is unchanged over generic smooth S_j. Each target blowup admits a global lift after principalizing the pulled coherent center ideal on the source. The ideal is nonzero by dominance. At generic D it is already (s^e) times a unit; any source blowup affecting the whole generic divisor is a divisor blowup and hence an isomorphism. Thus the source principalization is unchanged near generic D. In target blowup charts, divide pulled generators by one of minimum order, whose quotient is a unit near generic D. This supplies the holomorphic generic lift, and the strict D dominates the strict S_j^r.\n\nBlow up the entire smooth compact S_j^r. Let e>=1 be the order of its pulled ideal along D. With normal center coordinates x_1,...,x_c, a blowup chart has x_1=y_1, x_i=y_1 y_i for 2<=i<=c. Consequently\n\ndx_1 wedge ... wedge dx_d=y_1^(c-1)dy_1 wedge ... wedge dy_d,\n\nand k_new=k_old-(c-1)e. Preparation over the singular locus has zero Jacobian order at generic D; more generally every target blowup with a holomorphic generic lift only decreases k by its nonnegative Jacobian order. Each codimension-at-least-two round therefore decreases a finite nonnegative integer by at least one. There are at most k_0 rounds. If k reaches zero, another such round is impossible. For d=1 a proper image is already a divisor.\n\nAll spaces are compact because the operations are proper; their dominating smooth components are connected. Each subsequent strict-divisor image is compact analytic by proper mapping. We obtain a finite smooth compact modification sigma:B'->B and a prime F dominated by D under a holomorphic generic lift. No global algebraic function-field identification or nonproper local-image closure is used.\n\nAt generic smooth D over generic smooth F, pull back a local equation x of F. It is s^e times a unit. Dominance D->F supplies d-1 independent tangential coordinates y. Absorbing an e-th root of the unit into s and completing source coordinates gives the normal form\n\n(s,y,z)->(s^e,y).\n\nAn ideal sigma^*b of generic order r on F factors as x^r times an ideal with a generator nonzero generically on F. Its pullback stays nonzero generically on D. Therefore ord_D(f^*b)=e ord_F(sigma^*b) for EVERY nonzero coherent b. The extracted F and e do not depend on the test ideal.\n\nFor a genuine quasi-psh w, divisorial subtraction from n1 gives, up to smooth correction,\n\nw composed sigma=alpha log|x|^2+rho,\n\nwhere alpha=nu(w composed sigma,F) and rho has generic Lelong number zero on F. The residual may be identically minus infinity on F; no restriction rho|F is taken. At very general F its point Lelong number is zero, by Siu’s analytic level sets. The normal form sends a source ball of radius r onto a set containing a base ball of radius c r^e. Thus sup_(source ball r)(rho composed f_lift)>=sup_(base ball c r^e)rho. Dividing by the negative log r^2 and using maximum-growth characterization gives nu(rho composed f_lift)<=e nu(rho,base point)=0. Nonnegativity gives zero generic residual coefficient. The logarithmic term contributes e alpha, proving\n\nnu(w composed f,D)=e nu(w composed sigma,F).\n\nThis proves both alternatives in arbitrary base dimension, including residual potentials infinite on F. Resolution and proper-image applications are independently checked in n1; the termination invariant and identities are proved here. Full note: notes/n3.txt.\n\nArtifacts: /workspace/research/native-workers/codex-EezmdX",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n4",
      "summary": "C: submersion multiplier ideals at every real weight and the actual restricted image-ideal identity.",
      "detailedSummary": "Fubini, fiber Taylor estimates and Krull intersection in the convergent local ring prove the submersion identity without an integer-weight shortcut. Hopf projectivization then gives nu(u,Y)=0 and I(tu)O_Y=q^*(I(tU)O_B), even if U|B is identically minus infinity.",
      "text": "C: exact submersion multiplier pullback and actual image ideals.\n\nFor a holomorphic submersion f and genuine quasi-psh W on its base, product coordinates f(x,z)=x give\n\nI(t(W composed f))=I(tW)O_source\n\nfor every real t>0. For one inclusion, express a member of the extended ideal as a finite sum of base generators times holomorphic coefficients bounded on a smaller product; Fubini proves integrability. Conversely expand an integrable holomorphic germ G(x,z) in fiber variables. Cauchy/submean estimates bound the square of each Taylor coefficient by a constant times the fiber integral of |G|^2. Since the weight depends only on x, Fubini puts every coefficient in I(tW). For each N, the finite Taylor polynomial belongs to the extended ideal and the remainder to (z)^N. Krull intersection in the Noetherian convergent local ring, applied to the quotient by the extended ideal, gives intersection_N(I(tW)O+(z)^N)=I(tW)O. Thus G belongs to the actual extended ideal, not merely its completion. Bounded smooth corrections do not affect this proof.\n\nProjectivization p:H_(n+1)->P^n and q:H_n->B=P^(n-1) are holomorphic submersions with connected elliptic fibers, and Y=p^{-1}(B). Product-ball comparison preserves point Lelong numbers under a submersion. Taking generic points over B gives nu(p^*U,Y)=nu(U,B)=0. This uses ambient Lelong numbers and does not require U|B to exist as a genuine quasi-psh function.\n\nPut b_t=I(tU)O_B, the image under the quotient to O_B. Apply the submersion identity to p and then take the quotient defining Y. Local generators g_i pull back as g_i(x), and their images on Y are exactly q^*(g_i|B). Hence\n\nI(t p^*U)O_Y=q^*b_t\n\nfor every real t>0, as actual coherent image ideals. Their nonzero property under nu(U,B)=0 is part of the task’s conventions. The expression is not substituted by I(t(U|B)); it remains meaningful when U|B is identically minus infinity.\n\nThis proves C directly. Full note: notes/n4.txt.\n\nArtifacts: /workspace/research/native-workers/codex-EezmdX",
      "support": []
    },
    {
      "id": "n5",
      "summary": "D base step: full projective trace envelope, simultaneous divisorial exactness, and positive mass with explicit curvature room.",
      "detailedSummary": "Restricted dyadic analytic ideals give decreasing ordinary model envelopes in a fixed a FS background. Analytic comparison identifies their limit with the full profile envelope. Resolving analytic types proves masses at least (a-K)^d; the verified Kähler model-convergence theorem then gives every divisorial equality. For a>=2K the base mass lies between (a/2)^d and a^d.",
      "text": "D, base step: full projective envelope and simultaneous exactness.\n\nLet B=P^d with normalized kappa and let U on P^(d+1) satisfy nu(U,B)=0. Write b_t=I(tU)O_B. Choose c with dd^c U>=-c FS. The verified dyadic Bergman approximation in n1 supplies analytic U_k whose local type is 2^{-k}log(sum|generators of I(2^k U)|^2), with uniform lower curvature bounds. Discard finitely many terms and choose K>0 such that dd^c U_k>=-K FS. Restrict the analytic potentials: phi_k=U_k|B is genuine because b_(2^k) is nonzero, satisfies dd^c phi_k>=-K kappa, and has exactly the b_(2^k) type with coefficient 2^{-k}. U itself is not restricted.\n\nFor m=2^k, subadditivity followed by the actual quotient gives b_(2m) contained in b_m^2. Generator logarithms imply phi_(k+1) preceq phi_k.\n\nFix a>K and put W_k=P_(a kappa)[phi_k]. By n1, W_k is ordinarily equivalent to phi_k and is ordinary model. Thus W_(k+1)<=W_k. Each has supremum zero: a negative supremum would allow a positive constant to be added while preserving admissibility. The compact nonempty sets {W_k=0} are nested, so their intersection is nonempty. The decreasing limit W is therefore not identically minus infinity. It is genuine a kappa-psh and W_k->W in L1.\n\nFor any compact smooth modification sigma and prime F,\n\nnu(W_k composed sigma,F)=ord_F(sigma^*b_(2^k))/2^k=:tau_k(F).\n\nSubadditivity makes these numbers increasing, and the task’s intrinsic slope limit gives tau_k(F)->tau_(B,U)(F). On the fixed modification the genuine pullbacks decrease to W composed sigma, which is nontrivial by dominance, and converge in L1 with a common smooth lower Hessian bound. Lelong upper semicontinuity gives nu(W composed sigma,F)>=tau(F).\n\nIf v<=0 is any a kappa-psh competitor satisfying ALL intrinsic inequalities, then its numbers dominate those of phi_k on every compact modification. Analytic comparison in n1 yields v preceq phi_k, hence v<=W_k for every k and v<=W. Conversely W satisfies every constraint. Thus W is the FULL base envelope T_(a kappa)(U;B), before exactness is established.\n\nThe positive-mass hypothesis is verified next. An analytic potential and its ordinary envelope have the same mass in this closed background. Resolve the coherent ideal globally. Write the pullback as L+R, where L is a smooth-metric divisor logarithm and R is bounded. Removing the divisor current leaves gamma+dd^c R for fixed smooth closed gamma. The envelope has another bounded residual in the same gamma. Bounded Bedford–Taylor products give no mass to the divisor, and compact integration by parts makes either total mass integral gamma^d. The resolution can be chosen by blowups of the projective base and is Kähler; local addition and algebraic cancellation of a positive smooth form handles gamma if needed.\n\nOutside the analytic polar set, a kappa+dd^c phi_k>=(a-K)kappa. Consequently\n\nintegral_B MA_(a kappa)(W_k)=integral_B MA_(a kappa)(phi_k)>=(a-K)^d.\n\nEvery a kappa-psh potential has mass at most a^d: bounded truncations max(w,-j) have total mass a^d by Stokes, and their non-pluripolar restrictions have at most this mass.\n\nApply the independently verified Darvas–Xia Proposition 2.1 from n1 ONLY on the compact Kähler B, with theta=a kappa, zero background errors, and decreasing ordinary models W_k. Its mass conclusion gives integral MA(W)>=(a-K)^d>0. Its positive-mass conclusion now applies and gives, for EVERY prime F over B,\n\nnu(W composed sigma,F)=lim_k nu(W_k composed sigma,F)=tau_(B,U)(F).\n\nThus equality does not follow merely from upper semicontinuity. For a>=a0=2K,\n\n(a/2)^d<=integral_B MA_(a kappa)(W)<=a^d.\n\nThe room K depends on the ambient curvature bound and the analytic approximation. No mass theorem is applied on a Hopf manifold or an arbitrary non-Kähler modification. Full argument: notes/n5.txt; exact primary applications: source_audit.txt.\n\nArtifacts: /workspace/research/native-workers/codex-EezmdX",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n6",
      "summary": "D: full Hopf-envelope pullback and exactness on every modification and larger Hermitian background; targets are non-Kähler and fail BMP.",
      "detailedSummary": "General extraction checks every target prime, and smooth compact fiber products check every base prime. Elliptic fiber maxima handle all competitors and prove the normalized full envelope equals the pulled projective envelope. Exactness extends to every Hermitian background dominating a sufficiently large invariant one. The theorem remains scoped to scalar Hopf geometry and the basic data in C.",
      "text": "D: full invariant envelope and every modified divisor.\n\nUse C with n>=3,d=n-1. On Y=H_n let r=log||z||^2 modulo 2. Its differentials dr,d^c r are global. Set alpha=q^*kappa and beta=dr wedge d^c r. Their kernels are complementary, so Omega_(a,b)=a alpha+b beta is Hermitian for a,b>0. The compact connected elliptic group G=C^*/<e> acts by scalar multiplication, preserves these forms, and is transitive on each fiber. Invariant genuine potentials are precisely q^*psi.\n\nFor genuine base psi,\n\nOmega_(a,b)+dd^c q^*psi=q^*(a kappa+dd^c psi)+b beta,\n\nand positivity is equivalent to a kappa+dd^c psi>=0. To prove the reverse implication for currents, use a local trivialization r=w+bar w+f(x) and test on smooth horizontal vector fields (xi,-partial f(xi)). These annihilate partial r and project arbitrarily to the base. Integrating against a nonnegative vertical test measure proves positivity of the base current.\n\nFix ANY smooth compact target modification pi:Z->Y and prime D. Apply n3 to f=q composed pi. By n4, pulled target image ideals are f^*b_t. Horizontal primes have all orders and basic Lelong numbers zero. Otherwise n3 supplies a compact smooth base modification sigma, prime F and integer e>=1, independent of t and psi, with\n\ntau_(Y,u)(D)=e tau_(B,U)(F),\nnu(q^*psi composed pi,D)=e nu(psi composed sigma,F).\n\nThe first follows by dividing the identity for every b_t by t; the second includes residuals infinite on F. Every base competitor therefore pulls back to a target competitor with EVERY target divisor checked.\n\nConversely, for any compact smooth sigma:B'->B form Y'=Y x_B B'. It is smooth because q is a submersion, compact, and connected because its base and elliptic fibers are connected. Its proper map to Y is a modification, being an isomorphism over the dense open locus of sigma. The inverse image of a prime F has a unique prime dominating F: over smooth F it is a locally trivial connected elliptic bundle, whose closure is irreducible. That prime has e=1 and detects precisely the base orders and Lelong numbers. Thus every basic target competitor gives a base competitor on every base modification.\n\nNow handle ALL target competitors. For normalized v define vhat(x)=max_(g in G)v(gx). Compactness makes it upper semicontinuous; the locally bounded-above supremum theorem makes it Omega_(a,b)-psh. It is basic and dominates v. Every translate preserves the constraints: g composed pi is another permitted modification and q composed g=q leaves every pulled b_t unchanged. Finite maxima preserve the lower divisor coefficients, and so does their increasing canonical limit. On each fixed modification, an increasing Choquet sequence of finite maxima has a common genuine lower bound and smooth lower Hessian bound. Its L1 limit agrees with the canonical pullback off the exceptional set and hence everywhere. Subtracting each prescribed coefficient leaves a positive local current in the limit. This verifies every constraint without a finite-family shortcut or BMP.\n\nWrite vhat=q^*psi. Positivity and the fiber-product argument make psi a full base competitor. Hence every v is bounded above by q^*T_(a kappa)(U;B). Conversely that pullback is a target competitor. For all a>=a0 from n5 and b>0,\n\nT_(Omega_(a,b))(u;Y)=q^*T_(a kappa)(U;B)\n\nas FULL normalized envelopes. Combining n3 and exactness in n5 gives every intrinsic target number on every target modification, including every exceptional prime.\n\nFor any Hermitian Omega>=Omega_(a,b), the exact pullback is an Omega-psh competitor. Thus T_Omega dominates it, giving nu(T_Omega composed pi,D)<=tau(D). The increasing-maxima argument retains all lower constraints for T_Omega, using this common genuine competitor. Equality follows simultaneously for all pi,D.\n\nFinally H_n is diffeomorphic to S^(2n-1) x S^1, so H^2(H_n,R)=0 for n>=2. A Kähler form would be exact and have zero top integral by Stokes, contradicting positivity. The targets are therefore genuinely non-Kähler; n2 proves failure of BMP for every Hermitian form when n>=3. This supplies a sufficient condition with projective base dimension d>=2, beyond curve and curve-fibration cases. Its scope remains the basic data and scalar Hopf geometry in C.\n\nFull note: notes/n6.txt.\n\nArtifacts: /workspace/research/native-workers/codex-EezmdX",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4",
        "n5"
      ]
    },
    {
      "id": "n7",
      "summary": "E: individual mass formula and bounds, compatible ideal type and algebra, full ordinary pullback, and dyadic convergence on every modification.",
      "detailedSummary": "Direct bounded truncation gives mass 2nb times the base mass. Exact divisorial data imply all-real ideal-class independence and model fixedness. Addition requires compatible curvature room; scaling gives homogeneity. Fiber maxima prove full ordinary envelope pullback. The entire dyadic tail decreases in L1 on Y and every modification, with convergence of every divisorial number. No extremal volumes or ordinary background-type independence are inferred.",
      "text": "E: individual mass, compatible type, addition, pullback and approximation.\n\nLet W=T_(a kappa)(U;B) and T=q^*W, with a>=2K,b>0. For ANY genuine a kappa-psh psi, put psi_j=max(psi,-j). Bounded local multilinearity, beta^2=0 and d=n-1 give\n\n(Omega_(a,b)+dd^c q^*psi_j)^n=nb beta wedge q^*((a kappa+dd^c psi_j)^d).\n\nThis also holds for extended products with smooth-background corrections: locally add a smooth closed positive form, apply bounded multilinearity, then cancel it algebraically. Omega need not be closed. Restrict to {q^*psi>-j} and pass to the local non-pluripolar limit. Thus\n\nMA_(Omega_(a,b))(q^*psi)=nb beta wedge q^*MA_(a kappa)(psi).\n\nOn E, w=s+it has periods 1 and 2 pi; r=2s+constant and d^c r=dt/(2 pi). Therefore beta=ds wedge dt/pi and q_*beta=2. Consequently\n\nintegral_Y MA_(Omega_(a,b))(T)=2nb integral_B MA_(a kappa)(W),\n\nand n5 gives\n\n2nb(a/2)^d<=integral_Y MA_(Omega_(a,b))(T)<=2nb a^d.\n\nThese are positive finite INDIVIDUAL masses. No BMP-dependent unbounded product theorem is applied on Y.\n\nCompatible type. Every envelope in the invariant backgrounds and larger backgrounds of n6 has the same intrinsic divisorial profile. By n1 their multiplier ideals agree at EVERY real weight. The resulting ideal class depends only on the ambient ideal class, since that class fixes every image ideal b_t. This proves ideal-class independence within the stated large backgrounds.\n\nIn each fixed background the envelope is both ordinary model and ideal model. Any ordinary competitor for P_Omega[T] has divisorial numbers at least those of T and hence belongs to the full profile family, so is <=T. T itself is a competitor. Any ideal-equivalent competitor for P_Omega[T]_I has exactly the same numbers by n1, giving the same conclusion. Thus P_Omega[T]=P_Omega[T]_I=T. Ordinary equivalence between different backgrounds is not established.\n\nAddition. Let U_1,U_2 have zero generic Lelong number on B. Choose sufficient room for each and their sum, with Omega_i=a_i alpha+b_i beta admissible as in n6. Then T_1+T_2 is (Omega_1+Omega_2)-psh, normalized <=0, and has exact profile tau_1+tau_2=tau_(Y,u_1+u_2), by generic Lelong additivity and the task’s intrinsic additivity. In any sufficiently large admissible Omega dominating Omega_1+Omega_2, the full sum envelope dominates T_1+T_2 and has the same exact profile. By n1 it is ideal-equivalent to T_1+T_2 at every real weight. This states addition with the necessary curvature room.\n\nFor lambda>0, the bijection v->lambda v between normalized competitors, together with background and profile scaling, gives the actual equality\n\nT_(lambda Omega)(lambda u;Y)=lambda T_Omega(u;Y).\n\nIn other permitted large backgrounds this gives equality of ideal classes.\n\nFull ordinary pullback. For any genuine a kappa-psh phi, a competitor v<=0 with v preceq q^*phi can be replaced by its fiber maximum. The same ordinary comparison constant works for every translate because q^*phi is invariant, including at common poles. The resulting vhat=q^*psi has psi<=0, a kappa-psh and psi preceq phi. Every base competitor conversely pulls back. Therefore\n\nP_(Omega_(a,b))[q^*phi]=q^*P_(a kappa)[phi].\n\nWith pointwise comparison against a basic obstacle f, the same proof gives P_(Omega_(a,b))(q^*f)=q^*P_(a kappa)(f) whenever a genuine competitor exists. Both statements concern all competitors.\n\nFull dyadic approximation. Use U_k and phi_k from n5. By n4, p^*U_k has analytic type governed by I(2^k u), and its restriction is q^*phi_k. Define\n\nPsi_k=P_(Omega_(a,b))[q^*phi_k]=q^*W_k.\n\nThe equality follows from full ordinary pullback. Each Psi_k is an ordinary model of analytic singularity type. The entire dyadic tail decreases to T and converges in L1 on Y.\n\nOn ANY compact smooth modification pi:Z->Y, the genuine pullbacks decrease to T composed pi. The limit is nontrivial because q composed pi is dominant. Quasi-psh integrability and domination of the differences by Psi_(k0) composed pi-T composed pi give L1 convergence against any smooth volume on Z. For ANY prime D, use the extraction of n3 for q composed pi, independent of k. Horizontal numbers vanish; otherwise\n\nnu(Psi_k composed pi,D)=e ord_F(sigma^*b_(2^k))/2^k\n=ord_D(pi^*(I(2^k u)O_Y))/2^k -> tau_(Y,u)(D).\n\nThus every modified generic number converges, as well as the full potentials in L1. This uses actual image ideals and base model convergence, not individual target mass as a substitute for exactness.\n\nFull note: notes/n7.txt. Formula evidence: artifacts/formula_checks.json; rerun python verify_formulas.py. No ordinary-type background independence, extremal ordinary singularity volumes or BMP-dependent target product theorem is claimed.\n\nArtifacts: /workspace/research/native-workers/codex-EezmdX",
      "support": [
        "n1",
        "n3",
        "n4",
        "n5",
        "n6"
      ]
    },
    {
      "id": "n8",
      "summary": "F: exact all-real point image ideals and all-divisor profile; the genuine basic potential has actual mass 2nb(a^d-1).",
      "detailedSummary": "Radial integrability gives b_t=m_P^max(floor(t-d+1),0), including boundary weights. Every modified prime has profile ord_D(q^*m_P), realized by q^*(U|B). Resolving the point ideal and computing exceptional intersections gives base mass a^d-1, hence target mass 2nb(a^d-1) for a>1. Equality with the normalized envelope is not asserted.",
      "text": "F: point image ideals, every modified order and actual mass.\n\nLet n>=3,d=n-1 and U=log[(sum_(i=0)^(n-2)|z_i|^2)/(sum_(i=0)^n|z_i|^2)]. This is genuine FS-psh with analytic singularities on the line where z_0,...,z_(n-2) vanish. B={z_n=0} is not contained in that line, so nu(U,B)=0. Its intersection with B is P=[0:...:0:1] in B’s coordinates.\n\nNear P use z_(n-1)=1, x=(z_0,...,z_(n-2)) in C^d and y=z_n. Then U=log|x|^2-log(1+|x|^2+|y|^2). The second term is smooth and bounded. A holomorphic germ with first nonzero homogeneous x-degree k is integrable against exp(-tU) precisely when integral_0^epsilon rho^(2k-2t+2d-1)d rho is finite, equivalently k>t-d. Sufficiency follows from a bound C|x|^k. Necessity follows from spherical orthogonality and the positive square integral of the first nonzero homogeneous term. A coefficient that vanishes at y=0 but is nonzero as a y-germ still has positive square integral on a smaller y-ball and gives the same divergence.\n\nThus the ambient ideal is (x)^k(t), where k(t)=max(floor(t-d+1),0). The strict inequality includes the logarithmically divergent boundary t=k+d. Taking the actual quotient y=0 gives globally on B\n\nb_t=I(tU)O_B=m_P^max(floor(t-d+1),0)\n\nfor EVERY real t>0.\n\nBy n4, a_t=q^*m_P^k(t). For every smooth compact target modification pi and prime D its order is k(t)ord_D(pi^*q^*m_P). Since k(t)/t tends to 1,\n\ntau_(Y,u)(D)=ord_D(pi^*q^*m_P).\n\nThis includes every exceptional prime. Here W=U|B is genuine, kappa-psh and logarithmic of m_P. Thus q^*W is Omega_(a,b)-psh for a>=1,b>0. At generic D its pulled ideal is s^r times a tuple with a nonzero component, so q^*W composed pi=r log|s|^2+bounded. Its generic Lelong number is r, giving an exact realizer on every modification.\n\nFor its actual mass let mu:Bl_P B->B have exceptional E, and let rho:Bl_P B->P^(d-1) extend projection from P. Put H=mu^*kappa and gamma=rho^*FS. Factoring x by the exceptional coordinate in blowup charts gives\n\ndd^c(W composed mu)=[E]+gamma-H.\n\nThe numerator contributes the exceptional logarithm and the FS potential of the x-directions; the denominator contributes -H. Off E the pulled a kappa-current is the smooth form (a-1)H+gamma, positive for a>1, with no bounded-product mass on E. The non-pluripolar total mass is therefore\n\nintegral_B MA_(a kappa)(W)=integral_(Bl_P B)((a-1)H+gamma)^d=(aH-E)^d.\n\nH^d integrates to 1 because mu has degree one. H restricts to zero on E because mu|E is constant, so mixed H^(d-k)E^k integrate to zero for 0<k<d. Blowup charts identify O(E)|E=O_(P^(d-1))(-1), giving integral E^d=(-1)^(d-1). Hence (aH-E)^d=a^d-1.\n\nThe direct local fiber formula in n7 applies to this W, yielding\n\nintegral_Y MA_(Omega_(a,b))(q^*W)=2nb(a^d-1), a>1,b>0.\n\nEquality of this potential with the normalized full trace envelope is not claimed. Nor does this computation determine extremal masses over its ordinary class.\n\nverify_formulas.py checks 49 rational threshold cases, including boundary weights, and the intersection polynomial for d=2,...,8; all passed. The written radial and intersection arguments establish the general formulas, rather than extrapolating these finite checks. Full note: notes/n8.txt. Rerun: python verify_formulas.py.\n\nArtifacts: /workspace/research/native-workers/codex-EezmdX",
      "support": [
        "n1",
        "n4",
        "n6",
        "n7"
      ]
    },
    {
      "id": "n9",
      "summary": "A–F scoped proof drafts and reproducible evidence retained; unrestricted P18 remains open and candidate=false.",
      "detailedSummary": "Records the precise Hopf/basic-data scope, verified primary dependencies, artifacts, commands, 22 symbolic identities and 49 finite threshold cases in 23 check groups, and execution limitations. No heavy computation was launched. Requested root-model identity cannot be attested with exposed tools. Neither unrestricted exactness nor an unrestricted counterexample is claimed.",
      "text": "Scope, reproducibility and remaining gaps.\n\nNotes n1–n8 supply scoped independent proof drafts of A–F using the identified, independently inspected primary theorems. They include the all-dimensional Hopf BMP construction, arbitrary-base-dimensional finite extraction, every-real-weight submersion identity, every modified divisorial order, full normalized envelopes, actual individual masses, compatible ideal type and algebra, full ordinary pullback and full dyadic convergence.\n\nThe exactness theorem is restricted to scalar Hopf targets and the basic ambient data in C, with projective base dimension d>=2. The targets are proved non-Kähler and fail BMP. This gives a sufficient condition beyond the listed curve and curve-fibration cases.\n\nUnrestricted P18 remains OPEN here. These notes supply neither simultaneous realization on every compact non-Kähler target lacking a mass property nor an actual counterexample to that unrestricted statement. Ordinary-type independence between backgrounds and extremal ordinary singularity volumes are not established. The positive finite masses are individual envelope or realizer masses. Deep primary theorems remain mathematical inputs; source/application inspection and successful execution are not formal correctness certificates. These are unverified drafts.\n\nArtifacts are retained in /workspace/research/native-workers/codex-EezmdX. The supplied input is input.json. Full note files are notes/n1.txt through notes/n9.txt. source_audit.txt records primary editions, numbered results, hypotheses and applications; sources/*.json retain public retrieval responses, including failed and unused searches. No private candidate notes, candidate article, author source-application audits, previous native reports or credentials were read.\n\nThe public-source downloader is fetch_sources.py. Its actual command python fetch_sources.py > artifacts/source_download.stdout stopped after its first PDF request reported “Operation not permitted”; artifacts/source_download_log.json records the URL and error. An earlier shell request failed to connect to the configured proxy. No bypass was attempted. Primary web retrieval succeeded, including inspection of scanned Siu pages. Rerun downloads with python fetch_sources.py when permitted.\n\nThe lightweight checks are in verify_formulas.py. Rerun with python verify_formulas.py > artifacts/formula_checks.stdout. artifacts/formula_checks.json records 23 passing check groups: 22 exact symbolic identities and all 49 finite rational threshold cases. These are finite observations, not exhaustive tests of the analytic heat family. General positivity, radial density, divergence and all-real-weight conclusions are proved in the notes. A draft Hopf potential-rescaling error was caught and corrected before delivery: only the source forms are divided by 2 pi, while scalar potentials remain unchanged.\n\nartifacts/environment.txt records Python 3.12.14, SymPy 1.14.0, Linux 6.18.44 x86_64/glibc 2.41, network failures and execution limits. The requested runtime was gpt-6.1-sol xhigh; no exposed root-model attestation or switching facility permitted independent certification of that identity. No supervised heavy-compute service was available, and no resource-heavy computation was launched.\n\nThe complete machine-readable artifact is result.json. Rerun assembly and earlier-support validation with python assemble_result.py. The support graph is valid; filenames and commands occur in note text rather than support arrays. The last note does not claim unrestricted P18 solved, so candidate=false.\n\nArtifacts: /workspace/research/native-workers/codex-EezmdX",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "n6",
        "n7",
        "n8"
      ]
    }
  ],
  "candidate": false,
  "workspace": "/workspace/research/native-workers/codex-EezmdX"
}


## Whole statement-only input; proposed conclusions, not granted facts

{
  "task": {
    "problem": "All manifolds are connected and compact. Write dd^c=(i/(2 pi))partial barpartial. Use genuine canonical quasi-psh representatives. For a smooth real (1,1) form theta, PSH(X,theta) means theta+dd^c u>=0. Ordinary order u preceq v means u<=v+C and equivalence means mutual order, including the canonical values at common poles. Extended products mean non-pluripolar Monge-Ampere products with smooth-background corrections. A big background admits a genuine strict current theta+dd^c u>=epsilon h for some Hermitian h and epsilon>0. BMP means v_+(h)<infinity, where v_+(h) and v_-(h) are the supremum and infimum of integral(h+dd^c u)^n over all bounded h-psh u. Positive lower mass means v_-(h)>0; it is distinct from BMP. Define I(tu) by local integrability of |g|^2 exp(-tu), with no extra factor 2. Ideal equivalence means equality at every real t>0. P_theta[u]_I is the usc supremum of theta-psh v<=0 ideal-equivalent to u. P_theta[u] is the ordinary singularity envelope, the usc supremum of theta-psh v<=0 with v preceq u. The lower and upper singularity volumes are the infimum and supremum of the extended mass over all v ordinarily equivalent to u in the specified background, not the raw mass of one representative. Let Y be a connected positive-dimensional compact complex submanifold of X, and u quasi-psh on X with generic Lelong number nu(u,Y)=0. The restricted ideal a_t=I(tu)O_Y is the image ideal, which is coherent and nonzero. A divisor over Y is a prime divisor E on any connected smooth compact modification pi:Z->Y. Define tau_(Y,u)(E)=lim_(t->infinity)ord_E(a_t)/t; the finite limit equals the supremum over t>0 and the integer limit. These intrinsic data depend only on the ambient ideal class and are additive and positively homogeneous. A naive restriction u|Y can be identically minus infinity; it is not the definition of these data. For a sufficiently large Hermitian Omega on Y, define T_Omega(u;Y) as the usc supremum of Omega-psh v<=0 with nu(v composed pi,E)>=tau_(Y,u)(E) on every such modification. Original P18: when Y fails at least one of BMP and positive lower mass, can Omega be chosen so that equality holds simultaneously for every prime divisor on every modification? After exactness, determine a background-compatible ordinary or ideal type, with addition and analytic approximation properties. Known background: a common competitor, the trace envelope, ideal/ordinary fixedness, convergence of restricted analytic envelopes, and pulled-background modification compatibility already hold without either mass property. Their Lelong conclusions are only lower inequalities. Doubling an admissible background gives positive finite individual envelope mass and prescribed-type Lp equations, but does not already prove exact trace numbers. Exact realization on curves, on Kahler targets in a sufficiently large closed background, under both mass properties, and for specified curve-fibration trace data is already known. A single model divisor current cannot encode all exceptional orders, and exact divisorial data alone does not determine top mass. No new realization, geometry, criterion or proof is supplied.\n\n# P18 general-dimensional scoped statement-only targets A--F\n\nRetain every convention and the exact original task. These are requested\nconclusions, not granted lemmas, source judgments or author proof steps.\nThe unrestricted original remains open; independently judge scoped adequacy.\n\nA. For each integer n>=3 the scalar Hopf manifold\nH_n=(C^n\\{0})/<z->ez> fails BMP: for every Hermitian h there are\nglobally smooth real potentials with h+dd^c V>0 and total mass tending\nto infinity. Verify the actual higher-dimensional positivity and mass,\nusing indispensable ordinary primary literature independently. The original\nthreefold theorem may be used only after exact source application checking.\nNo new heat-scale construction, pending S02 result or mere dimension analogy\nis granted.\n\nB. If f:Z->B is a dominant holomorphic map of connected smooth compact\ncomplex manifolds of arbitrary base dimension d>=1 and D is a prime source\ndivisor, either f(D)=B and all nonzero coherent base ideal pullback orders\nand genuine quasi-psh generic pullback Lelong numbers are zero, or there is\na smooth compact modification sigma:B'->B and a prime divisor F on B',\ndominated by D under a holomorphic lift near generic D, and an integer e>=1\nsuch that for every nonzero coherent ideal b and every genuine quasi-psh w,\nord_D(f^*b)=e ord_F(sigma^*b) and\nnu(w composed f,D)=e nu(w composed sigma,F).\nProve existence, finiteness, all compact analytic auxiliary identifications\nand both identities, including residual potentials infinite on F. No\nextraction argument, termination invariant or finite-family shortcut is\ngranted. Any indispensable resolution or proper-mapping theorem requires\nexact independent primary application verification.\n\nC. Fix n>=3,d=n-1, M=H_(n+1), Y=H_n linearly embedded as the first\nn coordinates. Projectivization gives p:M->P^n and q:Y->B=P^d,\nwhere B is the linear hyperplane z_n=0. For any genuine quasi-psh U on\nP^n with nu(U,B)=0, put u=p^*U. Prove nu(u,Y)=0 and\nI(tu)O_Y=q^*(I(tU)O_B) for every real t>0, using actual image ideals.\nProve the submersion multiplier-ideal identity at every real weight.\n\nD. Normalize kappa=FS on B by integral kappa^d=1, and set\nr=log||z||^2 modulo two, alpha=q^*kappa, beta=dr wedge d^c r,\nOmega_(a,b)=a alpha+b beta. Prove that there is a0 depending on ambient\ncurvature room such that for all a>=a0 and b>0 the FULL intrinsic envelope\nT_Omega(u;Y)=q^*T_(a kappa)(U;B), and its generic Lelong numbers equal\nevery intrinsic tau_(Y,u)(D) on every smooth compact target modification.\nExactness also holds in every Hermitian Omega>=Omega_(a,b). Verify every\ncompetitor and every exceptional divisor, not only selected modifications.\nThe targets are genuinely non-Kahler and fail BMP by A.\n\nE. In the invariant backgrounds in D, prove positive finite INDIVIDUAL\ntrace mass, the actual formula integral_Y MA_Omega(T)=\n2nb integral_B MA_(a kappa)(T_base), and bounds\n2nb(a/2)^d<=integral_Y MA_Omega(T)<=2nb a^d.\nProve independence of the IDEAL class across these large invariant\nbackgrounds, addition and positive homogeneity with appropriate curvature\nroom. Prove full ordinary obstacle-envelope pullback for basic potentials,\nand full dyadic restricted analytic model approximants decreasing in L1\non Y and every modification, whose generic Lelong numbers converge to\neach intrinsic order. Do not infer ordinary-type independence or extremal\nordinary singularity volumes from these individual masses. Do not apply\na BMP-dependent unbounded product theorem on a target failing BMP.\n\nF. For U=log(sum_(i=0)^(n-2)|z_i|^2 / sum_(i=0)^n|z_i|^2) on P^n\nand B={z_n=0}, prove the image ideals are\nb_t=m_P^max(floor(t-d+1),0), P=[0:...:0:1] in B, and the profile on Y\nis ord_D(q^*m_P) for every prime divisor on every target modification.\nThe genuine potential q^*(U|B) is an exact realizer with actual mass\n2nb(a^d-1) for a>1. Equality of this potential with the normalized full\ntrace envelope is not requested.\n\nIndependently verify all indispensable primary claims and each application.\nProduce full ordinary proof notes with valid earlier-note support references\nand retain all genuine gaps. The requested model is gpt-6.1-sol xhigh.\n",
    "completionCriteria": "Resolve simultaneous exactness in the stated generality by proof or an actual counterexample, then state and prove the compatible type, addition and approximation conclusions actually available. Alternatively give new substantive sufficient conditions on a genuinely non-Kahler target failing a mass property, beyond the listed curve and fibration cases. Do not mistake curvature room, individual envelope mass, a lower Lelong inequality or exactness on a single model for simultaneous exactness. A restricted theorem remains explicitly scoped. Verify exact indispensable external claims at primary sources and independently reconstruct the full argument. Independently reconstruct all A--F, including the actual all-dimensional BMP construction, general divisorial extraction, every modified order, full envelope and every actual mass and type conclusion. Keep unrestricted P18 open."
  },
  "notes": [],
  "assignment": "Statement-only independent reconstruction of the exact original task and A--F. Do not read or use either private surface or general candidate proof notes, candidate articles, author source-application audits, previous native reports or credentials. Ordinary primary literature is allowed and must be verified independently. No author proof steps, extraction invariant, angular density identity, earlier reconstruction or source judgment is granted. Produce complete ordinary proof notes with valid earlier-note support references and retain all gaps. Use the configured gpt-6.1-sol xhigh native runtime. A candidate flag is not acceptance or unrestricted original closure."
}


## Whole new primary application judgments, not accepted results

{
  "recorded_at_utc": "2026-10-07T18:19:13.649710+00:00",
  "review_result_sha256": "f64e557a3c9e7058762728b7fc629b5cf5caa1fc9d5fb4e8efa28c735fb00cdd",
  "new_applications": [
    {
      "source": "Barlet, Some examples due to H. Hironaka, arXiv1501.01129v2, section2",
      "pdf": "inputs/primary/Barlet-Hironaka-blowups-1501.01129.pdf",
      "text": "inputs/primary/Barlet-Hironaka-blowups-1501.01129.txt",
      "whole_actually_read_ranges": [
        [
          1,
          335
        ]
      ],
      "exact_application": "The reduced image ideal of the proper analytic center is coherent and has no interior on the smooth irreducible target. The graph closure in the finite projective generator bundle is analytic, proper and bimeromorphic. Over the generic smooth center, the explicit least-order ratio chart is smooth. The main reduced component of the source-target fiber product is analytic and proper and contains the existing smooth generic lift. These hypotheses are applied at every extraction step; no compact graph closure is inferred for an arbitrary transcendental map. Section2 includes its generator graph construction and the complete strict-fiber-product discussion. This use does not require the later Hironaka deformation examples.",
      "pdf_sha256": "2b4a0e6277e2bb249264f7eb26ee5bc88848a03bd59ae6276b1cf73bbef5353d",
      "text_sha256": "ccd668d66a95ab5fcf8624e60c9367c6aec66bcc2c603c3f9ee60512732a3f8b"
    },
    {
      "source": "Xia, Singularities in global pluripotential theory, October4 2026 version retrieved October7",
      "pdf": "inputs/primary/Xia-SGPT-final-retrieved-20261007.pdf",
      "text": "inputs/primary/Xia-SGPT-final-retrieved-20261007.txt",
      "whole_actually_read_ranges": [
        [
          4990,
          5092
        ],
        [
          6440,
          6475
        ],
        [
          6671,
          6712
        ],
        [
          2042,
          2190
        ],
        [
          25050,
          25170
        ]
      ],
      "exact_application": "The whole current Proposition3.1.12 proof is read: the decreasing ordinary models in the closed big a*kappa background have positive mass from the smaller-background competitor, so its positive-mass divisorial conclusion applies to each divisor individually. Proposition3.2.1 and its whole printed proof identify ideal classes on the compact Kahler base at every real weight. Proposition3.2.10 and its whole proof identify finite analytic ordinary/ideal envelopes with the original analytic type. Theorem1.6.2 retains the exact dyadic ideal type and quasi-equisingular approximation hypotheses; it refers the proof to Demailly/DPS, whose exact earlier application records remain separately assessed, not recursively certified by reading this statement. AppendixB.1.1 and its complete printed proof realize arbitrary prime divisors, with Hironaka Chow lemma and smooth resolution as explicitly imported foundations. Only the bibliographic date differs from the frozen July18 author source. Old source bytes, frozen article and both native inputs are unchanged.",
      "pdf_sha256": "0fd575dc57ee9030de2bc6005fc5a8be5e24e8d1ed73d233e400330d503d2e61",
      "text_sha256": "0ec77e50871bd84ee57e3d5d779960287016b6be86646339eaf624d42ca5f139"
    }
  ],
  "mathematical_acceptance": false,
  "original_P18_completed": false,
  "published": false,
  "whole_frozen_report_and_all_17_premises_32_bindings_actually_read": true,
  "task_URN_bindings_excluded_from_external_evidence": [
    28,
    29,
    30,
    31
  ],
  "recursive_all_cited_foundations_certified": false
}


## Current known-overlap assessment

# Current known overlap and proof boundary

The current author's curve-fibration theorem, general trace-envelope limit,
modification compatibility, fixedness, positive individual masses and intrinsic
additivity are known background. So are exactness on a sufficiently enlarged
closed Kahler target and analytic exact realizers with exceptional coefficients
on non-BMP products. These are reproduced in full below and must be credited.
The point-ideal floor exponents and blowup intersection are explicit calculations,
not priority claims. The Xia--Zhang threefold BMP counterexample is a primary
input, not a result originating here.

The proposed sufficient condition concerns all genuine projective ambient
potentials with zero generic number on the hyperplane, including nonanalytic
data and the case of an identically-infinite naive restriction; the projective
base has every dimension d>=2. Its novel scope and adequacy must be assessed
against the preceding known cases. It needs the finite extraction lemma for
arbitrary base dimension, full elliptic-fiber competitor argument, exactness
on every target divisor, and actual all-dimensional Hopf BMP proof. Any
deduction already covered by the known trace background must be credited
as such rather than counted as a separate new result.


## Whole current known author source: section_curve_fibration_traces.tex

\section{Exact traces over a curve}
\label{sec:curve-fibration-traces}

An exact representative on a curve also gives higher-dimensional examples by pullback. Multiplier ideals commute with pullback by a submersion, so the trace data on a modification is given by the trace data on the curve, multiplied by the multiplicities of the pulled-back fibers. The pulled-back Green potential has exactly these divisorial Lelong numbers, and its domination property identifies the ordinary type of the trace envelope.

In this section, $p:X\to M$ is a surjective holomorphic submersion of connected compact complex manifolds with connected fibers. Let $C\subset M$ be a connected compact smooth curve, put $Y=p^{-1}(C)$, and write $q=p|_Y:Y\to C$; then $Y$ is a connected compact submanifold of $X$. Take $U\in\QPSH(M)$ with $\nu(U,C)=0$, and set $u=U\circ p$. The generic Lelong number of $u$ along $Y$ is zero, since in local product coordinates it equals that of $U$ along $C$. Write $\tau_{C,U}$ for the trace data of $U$ along $C$, defined as in \cref{sec:restricted-ideals} with $(M,C,U)$ in place of $(X,Y,u)$, and let
\[
 D=\sum_{b\in C}\tau_{C,U}(b)\,\delta_b,
 \qquad \delta=D(C)<+\infty.
\]
Choose a smooth positive form $\eta$ of integral one on $C$ and a nonpositive Green kernel for $\eta$. The construction in the proof of \cref{thm:curve-trace-realization} gives $w\in\QPSH(C)$, not identically $-\infty$, with
\[
 \ddc w=D-\delta\eta.
\]
\Needspace{9\baselineskip}
For $b\in C$, put $Y_b=q^{-1}(b)$, and let $[Y_b]$ be its current of integration. Set $v=w\circ q$. Pullback of distributions by a submersion is defined by duality with integration along the fibers; it commutes with differentiation and, in the present situation, with positive sums, so
\begin{equation}\label{eq:curve-fiber-divisorial-current}
 \ddc v=\sum_{b\in C}\tau_{C,U}(b)[Y_b]-\delta q^*\eta.
\end{equation}
Each fiber is a smooth connected prime divisor, and the sum is a positive closed current of finite mass, as also follows locally from the positivity of $\ddc(w\circ q)+\delta q^*\eta$.

\Needspace{24\baselineskip}
\begin{theorem}\label{thm:curve-fibration-exact-trace}\index{Trace!curve fibration}
The potential $v$ realizes the entire divisorial trace data of $u$ along $Y$:
\[
 \nu(v\circ\pi,E)=\tau_{Y,u}(E)
\]
for every prime divisor $E$ on every smooth compact modification $\pi:Z\to Y$. More explicitly, write $h=q\circ\pi$. If $h(E)=C$, both sides are zero. If $h(E)=\{b\}$, choose a local coordinate $t_b$ on $C$ vanishing at $b$; then both sides equal
\[
 \operatorname{ord}_E(t_b\circ h)\,\tau_{C,U}(b).
\]

Choose any Hermitian form $\Omega_0$ with $v\in\PSH(Y,\Omega_0)$, and set $\Omega=2\Omega_0$. Then
\begin{equation}\label{eq:curve-fibration-trace-envelope}
 \mathcal T_\Omega(u;Y)=P_\Omega[v]=P_\Omega[v]_{\mathcal I}\sim v.
\end{equation}
The envelope has positive finite extended mass, and the conclusions of \cref{cor:trace-envelope-prescribed-equation} on equations in its ordinary type hold. Its ordinary type does not depend on the choice of the Green kernel, of the form $\eta$, or of the sufficiently large background $\Omega$.
\end{theorem}
\begin{proof}
\Cref{lem:submersion-multiplier-pullback} and restriction to $Y$ give
\[
 \mathfrak a_t(u;Y)=\mathfrak a_t(U;C)\mathcal O_Y.
\]
The nonzero coherent ideal $\mathfrak a_t(U;C)$ on the smooth curve is generated near $b$ by $t_b^{k_t(b)}$, where $k_t(b)=\operatorname{ord}_b\mathfrak a_t(U;C)$. For a divisor $E$ with $h(E)=\{b\}$, the order along $E$ of the extended ideal is therefore $k_t(b)\operatorname{ord}_E(t_b\circ h)$. For a divisor dominating $C$, the generic order is zero, since the ideal on the curve has only finitely many zeros. Dividing by $t$ and letting $t\to\infty$ gives exactly the stated formula for $\tau_{Y,u}(E)$.

For the Lelong numbers of $v\circ\pi$, suppose first that $h(E)=\{b\}$. At a general point of $E$, a local equation $z_1=0$ of $E$ satisfies $t_b\circ h=z_1^k g$ with $g$ holomorphic and nonvanishing, and $k=\operatorname{ord}_E(t_b\circ h)$. Replacing $z_1$ by $z_1g^{1/k}$ for a local holomorphic $k$th root, we may assume $t_b\circ h=z_1^k$. The Lelong number of the one-variable function $w(z_1^k)$ at $0$ is $k\nu(w,b)=k\tau_{C,U}(b)$, as follows from the definition through circular means, and this is also the generic Lelong number of $v\circ\pi$ along $E$ in these product coordinates. If $h(E)=C$, the regular locus of $E$ contains a point mapped to a point where $w$ is finite, because the nonconstant holomorphic map from that locus to $C$ has open image; the pullback is finite there, so its generic Lelong number along $E$ is zero. This proves exact realization on every compact model.

By \cref{lem:divisorial-potential-domination} and \eqref{eq:curve-fiber-divisorial-current}, a quasi-plurisubharmonic function $a$ on $Y$ satisfies $a\preceq v$ if and only if $\nu(a,Y_b)\geq\tau_{C,U}(b)$ for every $b$ with $\tau_{C,U}(b)>0$. These fiber inequalities are among the trace inequalities, and conversely domination by $v$ implies all trace inequalities on modifications, by the exact formula just proved. Thus the trace competitors for $\Omega$ are exactly the competitors for the ordinary envelope of $v$, and $\mathcal T_\Omega(u;Y)=P_\Omega[v]$.

For $\psi=P_\Omega[v]_{\mathcal I}$, the Lelong numbers along the fibers are those of $v$, since $\psi$ and $v$ have the same multiplier ideals, and the same domination lemma gives $\psi\preceq v$. Hence
\[
 v-\sup_Yv\leq P_\Omega[v]\leq\psi\preceq v.
\]
Since $\psi\leq0$, it is a competitor for the ordinary envelope of $v$, so $\psi\leq P_\Omega[v]$. This proves \eqref{eq:curve-fibration-trace-envelope}.

The potential $v-\sup_Yv$ is a competitor for $P_{\Omega/2}(P_\Omega[v])$. The contact estimate for envelope fixed points, \cref{prop:fixed-point-finite}, gives finite mass, and \cref{lem:smaller-background-mass-lower} gives strict positivity. The two envelope properties give the model condition \eqref{eq:als-model-condition}, so \cref{thm:als-prescribed-lp} gives the stated equations.

Two Green constructions on $C$ differ by a smooth function, by the Poisson argument in the proof of \cref{thm:curve-trace-realization}, so their pullbacks have the same ordinary type. Every background in the statement gives an envelope ordinarily equivalent to this pullback. This proves the asserted independence, at the level of ordinary types rather than of normalized potentials.
\end{proof}

The same construction respects sums and multiplication by positive real numbers at the level of ordinary types. Indeed, the trace measures on the curve add by \cref{thm:trace-data-additivity}, their Green representatives add for a fixed kernel, and pullback preserves sums. Each envelope in a sufficiently large background represents the corresponding ordinary type.


## Whole current known author source: section_trace_envelope.tex

\section{The trace envelope}\label{sec:trace-envelope}

We return to the general setting, in which $Y\subset X$ has arbitrary positive dimension. The curvature errors of the restricted approximants tend to zero, so normalized compactness gives a limit potential in the original background $\theta|_Y$, whose divisorial Lelong numbers dominate the trace data. These inequalities define an envelope, and comparison with the resolved restricted ideals identifies it as the limit of the restricted analytic envelopes.

\begin{proposition}\label{prop:trace-profile-majorant}
There is a potential $v\in\PSH(Y,\theta|_Y)$ such that
\[
 \nu(v\circ\pi,E)\geq\tau_{Y,u}(E)
 \quad\hbox{for every divisor }E\hbox{ over }Y.
\]
In particular, $v\in\PSH(Y,\Omega_0)$ for every Hermitian form $\Omega_0\geq\theta|_Y$.
\end{proposition}
\begin{proof}
The restrictions $u_m|_Y$ have a common smooth lower bound for their curvature. After subtracting their suprema, normalized compactness gives a subsequence converging in $L^1$ to some $v$. The inequalities $(\theta+\epsilon_m\omega)|_Y+\ddc(u_m|_Y)\geq0$ pass to the limit as $\epsilon_m\to0$, giving $\theta|_Y+\ddc v\geq0$.

\Needspace{8\baselineskip}
For each fixed compact modification $\pi:Z\to Y$, \cref{lem:modification-lone-pullback} gives $L^1$ convergence of the pullbacks along the same subsequence, and \cref{lem:lelong-lone-semicontinuity} gives, at every point $z$ of a prime divisor $E\subset Z$,
\[
 \nu(v\circ\pi,z)
 \geq\limsup_m\nu((u_m|_Y)\circ\pi,z)
 \geq\lim_m\frac{\operatorname{ord}_E\mathfrak a_m(u;Y)}m
 =\tau_{Y,u}(E).
\]
Taking the generic value along $E$ proves the assertion. No diagonal extraction over divisors is needed, since the pullback lemma applies to each modification once the subsequence on $Y$ has been fixed.
\end{proof}

\Needspace{10\baselineskip}
For a smooth real $(1,1)$-form $\Omega$ on $Y$ for which the following family is nonempty, define
\begin{equation}\label{eq:trace-profile-envelope}
 \begin{split}
 \mathcal T_\Omega(u;Y):=\Bigl(\sup\{a\in\PSH(Y,\Omega):\ &a\leq0,\\
 &\nu(a\circ\pi,E)\geq\tau_{Y,u}(E)\
 \text{ for every }E\}\Bigr)^*.
 \end{split}
\end{equation}
Here $E$ ranges over all divisors over $Y$, and we call the members of this family \emph{trace competitors} for $\Omega$. By the preceding proposition, $v-\sup_Yv$ is a trace competitor for $\Omega=\theta|_Y$ and for every larger background. The envelope $\mathcal T_\Omega(u;Y)$ depends only on $\Omega$ and on the multiplier-ideal class of $u$ on $X$.

\subsection{Limits of restricted analytic envelopes}

On a log resolution of $\mathfrak a_m(u;Y)$, the trace inequalities dominate every coefficient of the restricted analytic singularity, so each trace competitor is at least as singular as $u_m|_Y$. This gives a common lower barrier for the analytic envelopes. Semicontinuity of Lelong numbers puts every cluster point back into the family of trace competitors, where maximality identifies it.

\begin{theorem}\label{thm:restricted-analytic-envelope-limit}\index{Trace!envelope limit}
Let $\Omega$ be a smooth real $(1,1)$-form on $Y$, let $h$ be a Hermitian form on $Y$, and let $\delta_m\geq0$ be numbers tending to zero such that, for all sufficiently large $m$,
\[
 a_m:=u_m|_Y\in\PSH(Y,\Omega+\delta_m h).
\]
Then the family of trace competitors for $\Omega$ is nonempty, $T=\mathcal T_\Omega(u;Y)$ belongs to $\PSH(Y,\Omega)$, and
\begin{equation}\label{eq:restricted-analytic-envelope-limit}
 q_m:=P_{\Omega+\delta_m h}[a_m]
     =P_{\Omega+\delta_m h}[a_m]_{\mathcal I}
       \longrightarrow T\quad\text{in }L^1(Y).
\end{equation}
If $\delta_{2^j}$ decreases in $j$, then $q_{2^j}\searrow T$ pointwise. The limit depends only on $\Omega$ and the multiplier-ideal class of $u$ on $X$. Moreover,
\[
 P_\Omega[T]_{\mathcal I}=P_\Omega[T]=T.
\]
\end{theorem}
\begin{proof}
\emph{Step 1: $T$ is the largest trace competitor.} The argument of \cref{prop:trace-profile-majorant}, applied with the assumed curvature bounds, gives a normalized $\Omega$-plurisubharmonic limit $v$ of a subsequence of the $a_m$, whose divisorial Lelong numbers dominate $\tau_{Y,u}$. Hence the family defining $T$ is nonempty, and its supremum lies between $v$ and zero. The family is stable under finite maxima, since the Lelong number of a maximum is the minimum of the two Lelong numbers, also after pullback. By Choquet's lemma and finite maxima, there is an increasing sequence of trace competitors whose limit has upper semicontinuous regularization $T$. Convergence of the pullbacks and semicontinuity of Lelong numbers show that $T$ satisfies every defining inequality. Thus $T$ is itself a trace competitor, and it is the largest one.

\emph{Step 2: a common lower barrier.} Fix $m$, and let $\pi:Z\to Y$ be a log resolution of $\mathfrak a_m(u;Y)$. For each prime component $E$ of the resulting divisor, \eqref{eq:trace-profile} gives
\[
 \nu(T\circ\pi,E)\geq\tau_{Y,u}(E)
       \geq\frac1m\operatorname{ord}_E\mathfrak a_m(u;Y)
       =\nu(a_m\circ\pi,E).
\]
The criterion of \cref{lem:analytic-ideal-dominance}, which involves only these finitely many divisors, gives $T\preceq a_m$. Since $T\leq0$ and $\delta_m\geq0$, the function $T$ is a competitor for $q_m$. Moreover, \cref{prop:analytic-envelope-type} identifies the two envelopes in \eqref{eq:restricted-analytic-envelope-limit} and gives $q_m\sim a_m$. Therefore
\[
 T\leq q_m\leq0,\qquad
 \nu(q_m\circ\pi,E)=\frac1m\operatorname{ord}_E\mathfrak a_m(u;Y)
\]
for every divisor over $Y$.

\emph{Step 3: convergence.} All $q_m$ have supremum zero and a common smooth lower bound for their curvature. Let $q$ be any $L^1$ cluster point. It belongs to $\PSH(Y,\Omega)$, lies between $T$ and zero, and satisfies
\[
 \nu(q\circ\pi,E)\geq\limsup_m\nu(q_m\circ\pi,E)
       =\tau_{Y,u}(E)
\]
along the convergent subsequence, by the pullback and semicontinuity argument of \cref{prop:trace-profile-majorant} on each fixed compact modification. Thus $q$ is a trace competitor, so $q\leq T$, and hence $q=T$. Normalized compactness now gives $L^1$ convergence of the whole sequence.

\emph{Step 4: monotonicity and the fixed-point identities.} Subadditivity gives $\mathfrak a_{2m}(u;Y)\subseteq\mathfrak a_m(u;Y)^2$, hence $a_{2m}\preceq a_m$. When the backgrounds $\Omega+\delta_{2^j}h$ decrease, this implies $q_{2^{j+1}}\leq q_{2^j}$. The lower bound by $T$ shows that the pointwise limit is not identically $-\infty$, and since it agrees with $T$ almost everywhere by $L^1$ convergence, it equals $T$ everywhere. The family defining $T$ depends only on $\Omega$ and on the multiplier ideals of $u$, which proves the asserted independence.

Finally, $P_\Omega[T]_{\mathcal I}$ has the same multiplier ideals as $T$, hence the same divisorial Lelong numbers, so it is a trace competitor. Maximality and the inequality $P_\Omega[T]_{\mathcal I}\geq T$ give $P_\Omega[T]_{\mathcal I}=T$, and the identity $P_\Omega[T]=T$ follows from \cref{cor:ordinary-preserves-i}.
\end{proof}

Taking $\Omega=\theta|_Y$, $h=\omega|_Y$ and $\delta_m=\epsilon_m$ gives the limit in the original restricted background; along dyadic indices, the errors can be enlarged to a decreasing sequence with limit zero. In a fixed, sufficiently large Hermitian background one can take $\delta_m=0$.

Inclusion of the families of trace competitors also orders the trace envelopes: increasing the prescribed data decreases $\mathcal T_\Omega$, whereas enlarging the background increases it whenever both envelopes are defined.

\subsection{Envelopes on modifications}

Let $\pi:Z\to Y$ be a modification of connected compact complex manifolds. Extend the restricted ideals to $Z$ by taking the ideals $\mathfrak a_t(u;Y)\mathcal O_Z$ generated by their pullbacks. For a divisor $F$ on a further modification $\rho:W\to Z$, their asymptotic order is $\tau_{Y,u}(F)$, computed on $\pi\circ\rho:W\to Y$. For a smooth real $(1,1)$-form $\Gamma$ on $Z$, write $\mathcal T^\pi_\Gamma(u;Y)$ for the envelope on $Z$ defined as in \eqref{eq:trace-profile-envelope}, with background $\Gamma$ and the inequalities $\nu(a\circ\rho,F)\geq\tau_{Y,u}(F)$ for all divisors $F$ over $Z$. Thus the trace data still comes from the multiplier ideals of $u$ on $X$.

For the pulled-back background $\pi^*\Omega$, every competitor descends to $Y$, and a common refinement of two models identifies the divisorial inequalities on them.

\begin{theorem}\label{thm:trace-envelope-modification}\index{Trace!modification compatibility}
Suppose $\Omega$ is a smooth real $(1,1)$-form on $Y$ for which $T=\mathcal T_\Omega(u;Y)$ is defined, and let $h$ be a Hermitian form on $Z$. Then
\begin{equation}\label{eq:trace-envelope-modification}
 \mathcal T^\pi_{\pi^*\Omega}(u;Y)=T\circ\pi,
 \qquad
 \mathcal T^\pi_{\pi^*\Omega+\varepsilon h}(u;Y)
       \searrow T\circ\pi\quad(\varepsilon\downarrow0).
\end{equation}
The convergence is pointwise and in $L^1(Z)$, and the limit is independent of $h$.

Let $\delta_m\geq0$ tend to zero and suppose, for all sufficiently large $m$, that
\[
 b_m:=(u_m|_Y)\circ\pi\in\PSH(Z,\pi^*\Omega+\delta_m h).
\]
Then
\[
 P_{\pi^*\Omega+\delta_m h}[b_m]
 =P_{\pi^*\Omega+\delta_m h}[b_m]_{\mathcal I}
 \longrightarrow T\circ\pi\quad\text{in }L^1(Z).
\]
If $\delta_{2^j}$ decreases, these envelopes decrease pointwise to $T\circ\pi$ along the dyadic indices.
\end{theorem}
\begin{proof}
For any nonempty family of trace competitors, the argument with finite maxima and semicontinuity in Step 1 of the proof of \cref{thm:restricted-analytic-envelope-limit} shows that the envelope is its largest member. By \cref{prop:psh-descent-modification}, every $\pi^*\Omega$-plurisubharmonic function is uniquely of the form $a\circ\pi$ with $a\in\PSH(Y,\Omega)$, and since $\pi$ is surjective, $a\leq0$ if and only if $a\circ\pi\leq0$. If $a$ satisfies all trace inequalities over $Y$, then $a\circ\pi$ satisfies those over $Z$, since every modification of $Z$, composed with $\pi$, is a modification of $Y$.

Conversely, suppose that $a\circ\pi$ satisfies the inequalities over $Z$. Let $E$ be a prime divisor on a smooth compact modification $V\to Y$. Resolving the graph of the bimeromorphic map between $V$ and $Z$ gives a smooth compact modification $W$ dominating both. The map $W\to V$ is an isomorphism near the generic point of $E$, so the strict transform $F$ of $E$ has the same ideal orders and generic Lelong numbers as $E$, and the inequality at $F$ over $Z$ is exactly the required inequality at $E$. Thus the two families of competitors correspond under pullback, and the largest member on $Z$ is $T\circ\pi$. This proves the first identity.

For $\varepsilon>0$, the pullback $T\circ\pi$ is still a competitor for $\mathcal T^\pi_{\pi^*\Omega+\varepsilon h}(u;Y)$. These envelopes lie between $T\circ\pi$ and zero and decrease as $\varepsilon\downarrow0$, so their limit $S$ satisfies $S\geq T\circ\pi$ and is $\pi^*\Omega$-plurisubharmonic. The $L^1$ convergence of pullbacks and semicontinuity of Lelong numbers preserve every trace inequality, so $S$ belongs to the unperturbed family. Maximality gives $S\leq T\circ\pi$, hence equality. Since the lower bound $T\circ\pi$ is integrable on $Z$, dominated convergence gives $L^1$ convergence.

For the final assertion, denote the analytic envelope in the statement by $q_m$. The proof of \cref{thm:restricted-analytic-envelope-limit} applies to the global coherent ideals $\mathfrak a_m(u;Y)\mathcal O_Z$: resolving each of them and applying \cref{lem:analytic-ideal-dominance} gives $T\circ\pi\preceq b_m$. Hence
\[
 T\circ\pi\leq q_m\leq0,\qquad
 \nu(q_m\circ\rho,F)
 =\frac1m\operatorname{ord}_F\mathfrak a_m(u;Y)
\]
for every divisor $F$ over $Z$, where ordinary and ideal envelopes agree by \cref{prop:analytic-envelope-type}. Every $L^1$ cluster point is $\pi^*\Omega$-plurisubharmonic and satisfies all trace inequalities, so the first identity in \eqref{eq:trace-envelope-modification} identifies it with $T\circ\pi$, and compactness gives convergence of the whole sequence. Subadditivity orders the dyadic analytic types, decreasing dyadic backgrounds then order the envelopes, and their pointwise limit is the same $L^1$ limit.
\end{proof}

For $\Omega=\theta|_Y$, the last hypothesis holds with $\delta_m=C\epsilon_m$, where the constant $C$ satisfies $\pi^*(\omega|_Y)\leq Ch$. Thus the restricted analytic envelopes converge to the same pulled-back trace envelope on every compact model. Formula \eqref{eq:trace-envelope-modification} also gives compatibility under successive modifications.

For arbitrary changes of background, inclusion of the families of competitors orders the envelopes. Equality of their ordinary types would require a reverse bound on the singularities. For curve fibrations, the fixed divisorial potential of \cref{thm:curve-fibration-exact-trace} gives this bound in every sufficiently large background.

\subsection{Exact realization on a K\"ahler submanifold}

By \cref{thm:restricted-analytic-envelope-limit}, semicontinuity of Lelong numbers gives $\nu(\mathcal T_\Omega(u;Y)\circ\pi,E)\geq\tau_{Y,u}(E)$. When $Y$ is K\"ahler, positive mass in a sufficiently large closed background strengthens this to equality: for decreasing sequences of model potentials whose limit has positive mass, the divisorial Lelong numbers converge. The envelope obtained in this way then gives the reverse inequality in every larger background.

\begin{theorem}\label{thm:kahler-target-exact-trace}
Suppose $Y$ is K\"ahler. Choose a Hermitian form $\Omega_0\geq\theta|_Y$ and a K\"ahler form $\kappa\geq2\Omega_0$ on $Y$. For every Hermitian form $\Omega\geq\kappa$,
\[
 \nu\bigl(\mathcal T_\Omega(u;Y)\circ\pi,E\bigr)
       =\tau_{Y,u}(E)
\]
for every prime divisor $E$ on every smooth compact modification $\pi:Z\to Y$.
\end{theorem}
\begin{proof}
The curvature errors $\epsilon_m$ tend to zero, so $u_m|_Y\in\PSH(Y,\kappa)$ for all sufficiently large $m$. By \cref{thm:restricted-analytic-envelope-limit}, applied with $\Omega=\kappa$ and $\delta_m=0$, the envelope fixed points
\[
 q_j=P_\kappa[u_{2^j}|_Y]
\]
decrease to $T=\mathcal T_\kappa(u;Y)$, after discarding finitely many indices. The normalized potential $v$ of \cref{prop:trace-profile-majorant} belongs to $\PSH(Y,\Omega_0)\subset\PSH(Y,\kappa/2)$ and satisfies $v\leq T$, so $P_{\kappa/2}(T)\not\equiv-\infty$. Thus \cref{lem:smaller-background-mass-lower} and Stokes' theorem give, with $r=\dim Y$,
\[
 \int_Y\mathrm{MA}_\kappa(T)
       \geq2^{-r}\int_Y\kappa^r>0.
\]
For a decreasing sequence of envelope fixed points in a closed background, positive mass of the limit implies convergence of every divisorial Lelong number \cite[Proposition~3.1.12]{SGPT}. Applied on $Y$, this yields
\[
 \nu(T\circ\pi,E)
 =\lim_j\nu(q_j\circ\pi,E)
 =\lim_j2^{-j}\operatorname{ord}_E\mathfrak a_{2^j}(u;Y)
 =\tau_{Y,u}(E).
\]
Here the middle equality uses the ordinary equivalence of each $q_j$ with $u_{2^j}|_Y$.

\Needspace{7\baselineskip}
If $\Omega\geq\kappa$, then $T$ is a trace competitor for $\Omega$, so $T\leq T_\Omega=\mathcal T_\Omega(u;Y)$. Together with the defining inequalities of $T_\Omega$, this gives
\[
 \tau_{Y,u}(E)\leq\nu(T_\Omega\circ\pi,E)
                 \leq\nu(T\circ\pi,E)=\tau_{Y,u}(E).
\]
This proves the assertion for every such $\Omega$.
\end{proof}

Only $Y$ is required to be K\"ahler here; the closed theory is applied on $Y$. If $Y$ has the bounded mass property, \cref{cor:mass-bound-exact-trace} gives the same exactness in a sufficiently large Hermitian background with positive lower mass. For a general non-K\"ahler $Y$, the envelope limit gives only the lower bound on its divisorial Lelong numbers.

\subsection{Positive mass and prescribed equations}

If a Hermitian background admits a trace competitor, then in the doubled background the same competitor lies in the half-sized background. This gives the trace envelope positive mass and the model condition needed for equations in its ordinary type.

\begin{theorem}\label{thm:trace-profile-model-envelope}
Choose $\Omega_0$ and $v$ as in \cref{prop:trace-profile-majorant} and set $\Omega=2\Omega_0$. Then $T=\mathcal T_\Omega(u;Y)$ belongs to $\PSH(Y,\Omega)$ and satisfies all the divisorial inequalities in \eqref{eq:trace-profile-envelope}. Moreover,
\[
 P_\Omega[T]_{\mathcal I}=T,\qquad P_\Omega[T]=T,
 \qquad P_{\Omega/2}(T)\not\equiv-\infty.
\]
Writing $r=\dim Y$, its extended measure satisfies
\[
 0<\int_Y\mathrm{MA}^{\mathrm{ext}}_\Omega(T)<+\infty,
 \qquad
 \mathrm{MA}^{\mathrm{ext}}_\Omega(T)
 \leq\mathbf1_{\{T=0\}}\Omega^r.
\]
\end{theorem}
\begin{proof}
Since $\theta|_Y+\epsilon_m\omega|_Y\leq\Omega$ for all sufficiently large $m$, the restricted approximants belong to $\PSH(Y,\Omega)$. \Cref{thm:restricted-analytic-envelope-limit}, applied with $\delta_m=0$, gives $T$, its defining inequalities and both fixed-point identities.

Normalize $v$ so that $\sup_Yv=0$. Since $v\in\PSH(Y,\Omega/2)$ is a trace competitor, it lies below $T$ and is a competitor for $P_{\Omega/2}(T)$. The contact estimate for envelope fixed points, \cref{prop:fixed-point-finite}, applied on $Y$, gives the bound for the measure and its finiteness, and \cref{lem:smaller-background-mass-lower} gives strict positivity.
\end{proof}

\Needspace{13\baselineskip}
\begin{corollary}\label{cor:trace-envelope-prescribed-equation}
Let $\Omega$ and $T$ be as in \cref{thm:trace-profile-model-envelope}, let $\mathrm{d}V$ be a smooth positive volume form on $Y$, and let $0\leq f\in L^p(\mathrm{d}V)$, $p>1$, with $\int_Y f\,\mathrm{d}V>0$. For every $\lambda>0$ there is a unique $a\in\PSH(Y,\Omega)$ with $a\sim T$ and
\[
 \mathrm{MA}^{\mathrm{ext}}_\Omega(a)=\mathrm{e}^{\lambda a}f\,\mathrm{d}V.
\]
There are also a constant $c>0$ and $a\in\PSH(Y,\Omega)$ with $a\sim T$ and $\mathrm{MA}^{\mathrm{ext}}_\Omega(a)=cf\,\mathrm{d}V$, and the constant $c$ is unique.
\end{corollary}
\begin{proof}
By \cref{thm:trace-profile-model-envelope}, $T$ satisfies both parts of the model condition \eqref{eq:als-model-condition} for the Hermitian background $\Omega$ on $Y$, so \cref{thm:als-prescribed-lp} applies.
\end{proof}

On a curve, \cref{lem:divisorial-potential-domination} shows that the trace inequalities are equivalent to domination by the Green representative $w$ in the ordinary sense. Thus
\[
 \mathcal T_{A\eta}(u;Y)=P_{A\eta}[w]=P_{A\eta}[w]_{\mathcal I}
\]
for every $A>0$ with $A\geq D_u(Y)$. The last equality, and the fact that the envelope has exactly the prescribed Lelong numbers, follow from \cref{lem:curve-atomic-ideal-model}, also when the residual mass $A-D_u(Y)$ is zero.


## Whole current known author source: section_trace_additivity.tex

Inclusions of ideals give monotonicity and homogeneity of the trace data directly. For sums, subadditivity of multiplier ideals gives one inequality; for the reverse inequality, an analytic approximant of the sum controls sufficiently fine approximants of both summands.

\Needspace{14\baselineskip}
\begin{proposition}\label{prop:trace-profile-calculus}\label{thm:trace-data-additivity}
Let $v\in\QPSH(X)$ also have zero generic Lelong number along $Y$, and recall that $u\preceq_{\mathcal I}v$ means $\mathcal I(ku)\subseteq\mathcal I(kv)$ for every real $k>0$ (\cref{sec:psh-singularity-types}). Then, as functions on divisors over $Y$,
\begin{enumerate}
\item $u\preceq_{\mathcal I}v$ implies $\tau_{Y,u}\geq\tau_{Y,v}$;
\item $\tau_{Y,au}=a\tau_{Y,u}$ for every $a>0$;
\item $\tau_{Y,u+v}=\tau_{Y,u}+\tau_{Y,v}$;
\item $\tau_{Y,\max(u,v)}\leq\min\{\tau_{Y,u},\tau_{Y,v}\}$.
\end{enumerate}
\end{proposition}
\begin{proof}
The inclusions of ideals defining $\preceq_{\mathcal I}$ persist after restriction and reverse the vanishing orders, which proves (1). Replacing $t$ by $at$ in \eqref{eq:trace-profile} proves (2). Moreover,
\[
 \mathcal I(tu)+\mathcal I(tv)\subseteq\mathcal I(t\max(u,v)).
\]
Since the order of a sum of ideals is the minimum of their orders, restriction and passage to the limit prove (4); note that $\max(u,v)$ also has zero generic Lelong number along $Y$. Generic Lelong numbers of sums add, so $u+v$ has zero generic Lelong number along $Y$ as well.

For (3), subadditivity of multiplier ideals gives $\tau_{Y,u+v}\geq\tau_{Y,u}+\tau_{Y,v}$. For the reverse inequality, fix a sufficiently large integer $k$ and the analytic approximant $S_k$ of $u+v$ given by \cref{thm:demailly-hermitian-input}, of analytic type $(1/k,\mathcal I(k(u+v)))$; that theorem gives $u+v\leq S_k$. Let $U_m,V_m$ be the corresponding approximants of $u$ and $v$. \Cref{lem:analytic-minorant-product-ideals} gives
\[
 U_m+V_m\leq(1-\delta_m)S_k+O(1),\qquad\delta_m\downarrow0.
\]
Here both $\delta_m$ and the bounded error may depend on the fixed $k$. The restrictions of $U_m$, $V_m$ and $S_k$ to $Y$ are not identically $-\infty$ by \cref{cor:restricted-analytic-divisorial-bound}. Restricting, pulling back to a fixed modification and taking the generic Lelong number along a divisor $E$ on it, we obtain
\[
 \frac{\operatorname{ord}_E\mathfrak a_m(u;Y)}m
 +\frac{\operatorname{ord}_E\mathfrak a_m(v;Y)}m
 \geq(1-\delta_m)
       \frac{\operatorname{ord}_E\mathfrak a_k(u+v;Y)}k.
\]
Letting first $m\to\infty$, with $k$ fixed, and then $k\to\infty$, the finite limits of \cref{thm:intrinsic-trace-profile} give the reverse inequality.
\end{proof}


## Whole current known author source: section_trace_exceptional_divisors.tex

\section{Exceptional divisors between trace models}
\label{sec:trace-exceptional-divisors}

We return to the trace data fixed at the beginning of the chapter, with $\dim Y=r$, and write $S_Z=S_Z(u;Y)$. By \cref{cor:countable-divisorial-pullback}, the full trace current can now be pulled back under a modification $g:Z'\to Z$. The pullback is bounded above by the trace current on $Z'$, with equal coefficients along strict transforms, so the difference is a finite effective divisor supported on the exceptional locus. Its logarithmic potential measures the change in the ordinary singularity types of the divisorial parts.

\begin{theorem}\label{thm:trace-exceptional-difference}\index{Exceptional divisor!trace correction and cocycle}
For a smooth compact modification $g:Z'\to Z$ over $Y$, there is a unique finite effective real divisor $E_g$ supported on the exceptional locus of $g$ such that
\begin{equation}\label{eq:trace-exceptional-difference}
 S_{Z'}=g^*S_Z+[E_g].
\end{equation}
For a further smooth compact modification $h:Z''\to Z'$, these divisors satisfy
\begin{equation}\label{eq:trace-exceptional-cocycle}
 E_{g\circ h}=E_h+h^*E_g.
\end{equation}
Their coefficients are additive and positively homogeneous in the ambient potential $u$.

For every $m$, the analytic-ideal divisors on the two models differ by a finite effective divisor $E_{m,g}$ supported on the exceptional locus:
\[
 [E_{m,g}]=D_{m,Z'}-g^*D_{m,Z}.
\]
\Needspace{5\baselineskip}
For every Gauduchon metric $\gamma'$ on $Z'$, the measures
\[
 [E_{m,g}]\wedge(\gamma')^{r-1}
     \longrightarrow [E_g]\wedge(\gamma')^{r-1}
\]
converge in total variation.
\end{theorem}
\begin{proof}
\emph{Step 1: the exceptional divisor.} Enumerate the prime divisors on $Z$ with positive trace coefficient. By \cref{thm:trace-divisorial-model-compatibility}, the pullback of every finite partial sum of $S_Z$ is at most $S_{Z'}$, and \cref{cor:countable-divisorial-pullback} identifies the increasing limit of these pullbacks with $g^*S_Z$. Thus $S_{Z'}-g^*S_Z$ is a positive closed divisorial current. The two currents have equal coefficients along the strict transform of every prime divisor on $Z$, because these coefficients are computed by the same valuation. Every other prime divisor on $Z'$ is exceptional for $g$, and the exceptional analytic set has only finitely many irreducible components on the compact manifold $Z'$. Hence the difference is the integration current of a finite effective real divisor $E_g$ supported on its divisorial components, and the coefficients of integration currents determine $E_g$ uniquely.

\emph{Step 2: the cocycle identity.} Pullback of positive closed $(1,1)$-currents is functorial, since it is defined by composing local plurisubharmonic potentials. Using \eqref{eq:trace-exceptional-difference} for $h$ and for $g$ gives
\[
 S_{Z''}=h^*S_{Z'}+[E_h]
        =(g\circ h)^*S_Z+[h^*E_g]+[E_h],
\]
and uniqueness gives \eqref{eq:trace-exceptional-cocycle}. Additivity and positive homogeneity follow from the same properties of the trace coefficients and the linearity of pullback.

\Needspace{10\baselineskip}
\emph{Step 3: approximation.} For fixed $m$, apply \eqref{eq:trace-ideal-model-inequality} to the finitely many prime divisors in the support of the image ideal on $Z$. After division by $m$, it gives $D_{m,Z'}-g^*D_{m,Z}\geq0$. The coefficients along strict transforms vanish, so this difference is the integration current of an effective real divisor $E_{m,g}$ supported on the exceptional locus.

Choose also a Gauduchon metric $\gamma$ on $Z$. By \cref{thm:trace-divisorial-current-budget}, the currents $S_Z-D_{m,Z}$ and $S_{Z'}-D_{m,Z'}$ are positive, and their trace masses tend to zero. Subtracting the two identities for the exceptional currents gives
\[
 [E_{m,g}]-[E_g]
   =-(S_{Z'}-D_{m,Z'})+g^*(S_Z-D_{m,Z}),
\]
where both $S_{Z'}-D_{m,Z'}$ and $g^*(S_Z-D_{m,Z})$ are positive. By \eqref{eq:modification-linear-mass-bound}, the total variation of the signed measure $([E_{m,g}]-[E_g])\wedge(\gamma')^{r-1}$ is therefore at most
\[
 \int_{Z'}(S_{Z'}-D_{m,Z'})\wedge(\gamma')^{r-1}
 +C_g\int_Z(S_Z-D_{m,Z})\wedge\gamma^{r-1}.
\]
Both terms tend to zero, which proves convergence in total variation.
\end{proof}

For a modification $g:Z'\to Z$ as in the theorem, the coefficient of $E_g$ along an exceptional prime divisor $F\subset Z'$ is
\begin{equation}\label{eq:trace-exceptional-coefficient}
 \tau_{Y,u}(F)
  -\sum_{D\subset Z}\tau_{Y,u}(D)\operatorname{ord}_F(g^*D),
\end{equation}
where $D$ ranges over the prime divisors on $Z$ with positive trace coefficient. This countable sum converges: it is the coefficient of $g^*S_Z$ along $F$ in the positive divisorial series of \cref{cor:countable-divisorial-pullback}, and it is at most $\tau_{Y,u}(F)$. The same current identity compares the ordinary singularity types attached to $S_Z$ and $S_{Z'}$ by \cref{cor:divisorial-current-ordinary-type}.

\Needspace{14\baselineskip}
\begin{corollary}\label{cor:trace-model-ordinary-comparison}\index{Divisorial current!ordinary types under pullback}
Choose decompositions $S_Z=B_Z+\ddc v_Z$ and $S_{Z'}=B_{Z'}+\ddc v_{Z'}$ with smooth closed forms $B_Z,B_{Z'}$, as in \cref{cor:divisorial-current-ordinary-type}. Let $\rho_{E_g}$ be a global logarithmic potential of $E_g$, that is, a quasi-plurisubharmonic function on $Z'$ such that $\ddc\rho_{E_g}-[E_g]$ is smooth. Then
\[
 v_{Z'}-(v_Z\circ g)-\rho_{E_g}
\]
is represented by a smooth function. In particular,
\[
 v_{Z'}\preceq v_Z\circ g
\]
in the sense of \cref{def:singularity-order}, and the two ordinary singularity types are equal if and only if $E_g=0$.
\end{corollary}
\begin{proof}
Global logarithmic potentials exist: choose smooth Hermitian metrics on the line bundles of the prime components of $E_g$, let $\alpha_{E_g}$ be the corresponding weighted sum of their curvature forms, and let $\rho_{E_g}$ be the weighted sum of the logarithms of the squared norms of the canonical sections. Then
\[
 \ddc\rho_{E_g}=[E_g]-\alpha_{E_g},
\]
and any two global logarithmic potentials differ by a smooth function, by \cref{lem:closed-current-global-potential}. We may therefore use this choice. The function $\rho_{E_g}$ is quasi-plurisubharmonic and bounded above on the compact manifold $Z'$.

\Needspace{10\baselineskip}
The chosen decompositions and \eqref{eq:trace-exceptional-difference} give
\[
 \ddc\bigl(v_{Z'}-v_Z\circ g-\rho_{E_g}\bigr)
       =g^*B_Z+\alpha_{E_g}-B_{Z'},
\]
which is smooth. By \cref{lem:closed-current-global-potential}, this difference of locally integrable functions is represented by a smooth function. The resulting equality of quasi-plurisubharmonic functions extends from almost everywhere to everywhere by \cref{lem:qpsh-almost-everywhere-order}. Since $\rho_{E_g}$ is bounded above, this gives the ordinary domination.

If $E_g=0$, the smooth difference gives ordinary equivalence. Conversely, ordinary equivalence would give equal generic Lelong numbers along every prime divisor of $Z'$, whereas the identity just proved shows that along a prime component of $E_g$ these numbers differ by its positive coefficient. Hence ordinary equivalence forces $E_g=0$.
\end{proof}

When $\theta$ is closed, the positive residual currents $R_Z$ constructed in the proof of \cref{prop:trace-bott-chern-bclass}, and their Bott--Chern classes, satisfy
\[
 \begin{split}
 R_{Z'}&=g^*R_Z-[E_g],\\
 \mathbb A_{Z'}(u;Y,\theta)
       &=g^*\mathbb A_Z(u;Y,\theta)-\{[E_g]\}_{\mathrm{BC}}.
 \end{split}
\]
Indeed, the smooth background and the common trace potential pull back, while \eqref{eq:trace-exceptional-difference} gives the change in the subtracted divisorial current. The correction $\{[E_g]\}_{\mathrm{BC}}$ accounts for the additional divisorial vanishing prescribed on the higher model. This is consistent with the exact pullback of the trace envelope in \cref{thm:trace-envelope-modification}, since the envelope imposes the trace inequalities on all models at once. The following example shows that the correction can be nonzero even when the trace data are realized exactly by a potential.

\Needspace{9\baselineskip}
\begin{example}\label{ex:exceptional-trace-with-exact-potential}
Let $Y=\mathbb P^2$ with homogeneous coordinates $[t_0:t_1:t_2]$, let $\sigma$ be the Fubini--Study form normalized by $\int_Y\sigma^2=1$, and choose $a\in\mathbb Q_{>0}$. Put
\[
 u=a\log\frac{|t_1|^2+|t_2|^2}
                   {|t_0|^2+|t_1|^2+|t_2|^2},
\]
and take the ambient manifold to be $Y$ itself. Then $u\in\PSH(Y,a\sigma)$. It has analytic singularities, with its only pole at $p=[1:0:0]$, and zero generic Lelong number on $Y$. By \cref{prop:trace-naive-comparison}, its trace data are given by the generic Lelong numbers of its pullbacks: $\tau_{Y,u}(E)=\nu(u\circ\pi,E)$ for every prime divisor $E$ on a smooth compact modification $\pi$ of $Y$. Since $u$ has no divisorial poles on $Y$, we have $S_Y=0$, whose canonical ordinary type is that of a smooth function. If $\pi:\widetilde Y\to Y$ is the blowup at $p$ with exceptional curve $F$, then
\[
 S_{\widetilde Y}=a[F],\qquad E_\pi=aF.
\]
Indeed, on either standard chart of the blowup, the numerator is the squared modulus of the exceptional coordinate times a smooth positive function, so the pole order is $a$ along $F$ and zero along every other prime divisor. Thus the trace data are realized exactly by $u$, although $E_\pi\neq0$. The exceptional difference does not obstruct exact realization; it prevents the identification of the realizing potential with the canonical ordinary type of the divisorial part on the original model, which here is smooth.

\Needspace{8\baselineskip}
The same phenomenon occurs on a manifold without the bounded mass property. Let $(W,\omega_W)$ be a compact Hermitian manifold of dimension $k$ that fails the bounded mass property, such as the Hopf threefold of \cref{thm:hopf-unbounded}, and pull $u$ back to $Y\times W$; take both the ambient manifold and the submanifold to be $Y\times W$. The pole set of the pullback is $\{p\}\times W$, of codimension two, and the modification $\widetilde Y\times W\to Y\times W$ has exceptional coefficient $a$ along $F\times W$. Analytic restriction again shows that the trace data are realized exactly. Let $\operatorname{pr}_Y$ and $\operatorname{pr}_W$ be the two product projections.

\Needspace{9\baselineskip}
Choose smooth $\omega_W$-plurisubharmonic functions $H_j$ whose masses tend to infinity. For the Hermitian form $\Omega=\operatorname{pr}_Y^*\sigma+\operatorname{pr}_W^*\omega_W$, the pullbacks of the $H_j$ have masses
\[
 \binom{k+2}{2}\left(\int_Y\sigma^2\right)
          \left(\int_W(\omega_W+\ddc H_j)^k\right)\longrightarrow+\infty,
\]
by the binomial expansion of smooth forms and the dimensions of the two factors. Hence the product also fails the bounded mass property. The pulled-back potential belongs to $\PSH(Y\times W,C\Omega)$ for every $C\geq\max\{a,1\}$, since its curvature is bounded below by $-a\operatorname{pr}_Y^*\sigma$. Scaling the smooth functions $H_j$ by $C$ shows that $C\Omega$ also has unbounded mass.
\end{example}


## Whole historical exact source-application record; applications require judgment

{
  "recorded_utc": "2026-10-05T08:19:34.515407+00:00",
  "candidate": "P18 simultaneous exact surface-base intrinsic traces on a non-Kahler Hopf threefold failing BMP",
  "paper": "papers/P18-Hopf-threefold-exact-surface-traces.tex",
  "paper_sha256": "2fea6343489bf45080f8fcf14e9a98492b459ade346cf8e06849e9e75a98a9f3",
  "proof_note": "notes/P18-Hopf-surface-base-traces.private-unverified.md",
  "proof_note_sha256": "f7b682dd8fdb23b25bcf33e06d7b55e59e748429acc7fc3ff5978e0e52d4c706",
  "build": "checks/P18-Hopf-corrected-draft-build.json",
  "current_pages": 6,
  "source_applications": [
    {
      "source": "inputs/primary/Demailly-agbook-Harvard.pdf",
      "application": "Proper image analyticity on possibly singular compact graph sources; explicit smooth point-blowup charts; generic Siu divisorial removal.",
      "whole_text_passages_actually_read": [
        [
          6332,
          6484
        ],
        [
          6784,
          6920
        ],
        [
          9845,
          9948
        ],
        [
          19645,
          19850
        ]
      ],
      "normalization": "Source dd^c is twice ours. The numerical potential residual R-a log|y1|^2 is unchanged after converting source current coefficients by two.",
      "sha256": "d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1"
    },
    {
      "source": "inputs/primary/Demailly-analytic-methods.pdf",
      "application": "Lemma 5.6(a), including its proof, gives all finite exponential weights for a zero point-Lelong residual. Lemma 5.6 and ideal definitions checked through printed pages 35--37.",
      "whole_text_passages_actually_read": [
        [
          1880,
          2030
        ],
        [
          1090,
          1151
        ]
      ],
      "normalization": "Source uses exp(-2phi) and phi/log|z|. Apply its zero-Lelong integrability result to phi=(t/2)R; our divisorial divergence threshold is proved directly from |z1|^(-2tc).",
      "sha256": "6f4682f322d6ae0c0ce3feae4964792c473a3d9051fe01288ef9017ca341d009"
    },
    {
      "source": "inputs/primary/Xia-SGPT-final.pdf",
      "application": "Proposition 3.1.12 with theta=a kappa, epsilon=0, decreasing ordinary models, and positive limit mass; Proposition 3.2.1 only on the compact Kahler base P2 for ideals at every positive real weight.",
      "whole_text_passages_actually_read": [
        [
          4960,
          5100
        ],
        [
          6420,
          6477
        ],
        [
          1610,
          1762
        ],
        [
          2235,
          2278
        ],
        [
          9970,
          10030
        ],
        [
          25225,
          25335
        ]
      ],
      "normalization": "Same dd^c and exp(-tu) conventions. The known closed-target trace construction supplies the models and smaller-background majorant; no closed-background theorem is applied on the Hopf target.",
      "sha256": "c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706"
    },
    {
      "source": "inputs/primary/Xia-Zhang-2608.21053v1.pdf",
      "application": "Theorem 1.1 on the identical diagonal Hopf threefold, using the original published heat scale and actual positivity/energy construction. No unaccepted S02 scale change is needed.",
      "whole_text_passages_actually_read": [
        [
          1,
          902
        ]
      ],
      "normalization": "Source dd^c=i partial barpartial=2 pi times ours; normalize the source Hermitian form by 2 pi and retain the same potentials. The divergent masses are divided by (2 pi)^3. The groups generated by e and e^-1 are identical.",
      "sha256": "0c39d024097dae97940403328cf6f8fb39fe3e21270edd02449948ea17303baa"
    },
    {
      "source": "inputs/primary/BGL-volumes-2406.01090.pdf",
      "application": "Only bounded Section 2.1 equations 2.1--2.3 and Proposition 2.1 locality/positivity are used at actual canonical truncation levels. The particular unbounded pullback product is obtained directly from these equalities and the finite closed-base non-pluripolar measure.",
      "whole_text_passages_actually_read": [
        [
          534,
          715
        ]
      ],
      "Section_2_2_BMP_theorem_not_imported": true,
      "normalization": "Bounded multilinear identities are invariant under positive dd^c scaling with corresponding potential scaling.",
      "sha256": "d7637564a1b1b728743bc5ae315c336097139d12ebca9f43469d721947f8f031"
    }
  ],
  "actual_primary_page_views": {
    "Xia-SGPT-final-112": {
      "path": "checks/P18-Hopf-primary-pages/Xia-SGPT-final-p112.png",
      "sha256": "6762a1bb82ef06eaeab50d67a0a64a4377018a4f95c3512c5ab48ea69181287d",
      "actually_viewed": true
    },
    "Xia-SGPT-final-113": {
      "path": "checks/P18-Hopf-primary-pages/Xia-SGPT-final-p113.png",
      "sha256": "cfc43d617dfeb9af4a9667c3135410302d8b25500e762a186eb42dbe0a3f1f81",
      "actually_viewed": true
    },
    "Xia-SGPT-final-138": {
      "path": "checks/P18-Hopf-primary-pages/Xia-SGPT-final-p138.png",
      "sha256": "749d84b23b243a175c73356d4dc4f79780d66c1674655d6716d8d010b96f86d1",
      "actually_viewed": true
    },
    "Xia-SGPT-final-139": {
      "path": "checks/P18-Hopf-primary-pages/Xia-SGPT-final-p139.png",
      "sha256": "913d6dab1b389430c1cfd0abd3258790a8811661b84aafe3995c75a2b2307231",
      "actually_viewed": true
    },
    "Demailly-analytic-methods-035": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-analytic-methods-p035.png",
      "sha256": "803bc990da778c4ae089c51ec3f93aed61b4d707ac549d71c10b232983083f4d",
      "actually_viewed": true
    },
    "Demailly-analytic-methods-036": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-analytic-methods-p036.png",
      "sha256": "8921adcb2d6f736d9e1dd39a5724c911c78aeb55c788d8d8f03e4f79dfe294d1",
      "actually_viewed": true
    },
    "Demailly-analytic-methods-037": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-analytic-methods-p037.png",
      "sha256": "6fa8fc6c04454e2c428080f74c7ab93246f7db9454a2225108c2276e0c6837c5",
      "actually_viewed": true
    },
    "Demailly-agbook-Harvard-118": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-agbook-Harvard-p118.png",
      "sha256": "e03a51cb9697981d60ecabd802ae0e4fd92dc0354821db99ed40df834893a551",
      "actually_viewed": true
    },
    "Demailly-agbook-Harvard-119": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-agbook-Harvard-p119.png",
      "sha256": "8b80f9d2db4478c6d8b0081ae85c42cdb8693105a4409cb0079d0f77727506b1",
      "actually_viewed": true
    },
    "Demailly-agbook-Harvard-120": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-agbook-Harvard-p120.png",
      "sha256": "3d1ef6b0a618f1009375d2f61034bc1d3cb92b58b3a9e71e95ba16abf4b15e77",
      "actually_viewed": true
    },
    "Demailly-agbook-Harvard-121": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-agbook-Harvard-p121.png",
      "sha256": "29139bdacaf2096330d9330b4ba8c482e74e2bda0a9ab85a3d8662ce5b716a67",
      "actually_viewed": true
    },
    "Demailly-agbook-Harvard-180": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-agbook-Harvard-p180.png",
      "sha256": "c68a3b14b27d4c73abed26411e49a4bf18580ca837552b80246677a5534cb153",
      "actually_viewed": true
    },
    "Demailly-agbook-Harvard-181": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-agbook-Harvard-p181.png",
      "sha256": "bbc1c8c73f77eb2077eb4b14c8e6202e55ab4a4e0d202122d01e45f14b47533c",
      "actually_viewed": true
    },
    "Demailly-agbook-Harvard-355": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-agbook-Harvard-p355.png",
      "sha256": "b44f4a71b95be111aae874c44dde78d22b0b9899e6c60d3010c8f4d0467766a9",
      "actually_viewed": true
    },
    "Demailly-agbook-Harvard-356": {
      "path": "checks/P18-Hopf-primary-pages/Demailly-agbook-Harvard-p356.png",
      "sha256": "c2ac44753d42dfad9772d3d70fb631dfcdb77410ad7112d31db13524201721e1",
      "actually_viewed": true
    },
    "Xia-Zhang-2608.21053v1-001": {
      "path": "checks/P18-Hopf-primary-pages/Xia-Zhang-2608.21053v1-p001.png",
      "sha256": "8fba930daf879a683410d25036c938d96721cc3856fe2c19cfa91dbdf0a75e13",
      "actually_viewed": true
    },
    "Xia-Zhang-2608.21053v1-002": {
      "path": "checks/P18-Hopf-primary-pages/Xia-Zhang-2608.21053v1-p002.png",
      "sha256": "0d63cf2e15db08e951f996bd6421f70df852199fd1f7d80e24aeddfbb27a8fee",
      "actually_viewed": true
    },
    "Xia-Zhang-2608.21053v1-004": {
      "path": "checks/P18-Hopf-primary-pages/Xia-Zhang-2608.21053v1-p004.png",
      "sha256": "005a15aa06cd780975fd7d4d9d5727045039030d7f0bf890773c3d98991b8920",
      "actually_viewed": true
    },
    "Xia-Zhang-2608.21053v1-005": {
      "path": "checks/P18-Hopf-primary-pages/Xia-Zhang-2608.21053v1-p005.png",
      "sha256": "a24933a19c865192ccbcaca1133239acdff8b1408e0524dc0fe6577cffb05f32",
      "actually_viewed": true
    },
    "Xia-Zhang-2608.21053v1-012": {
      "path": "checks/P18-Hopf-primary-pages/Xia-Zhang-2608.21053v1-p012.png",
      "sha256": "c1a19ef081bc7cb00c9d14f43fd656f78dd67d8c1f0688ab5a00b1f59509f39a",
      "actually_viewed": true
    },
    "BGL-volumes-2406.01090-012": {
      "path": "checks/P18-Hopf-primary-pages/BGL-volumes-2406.01090-p012.png",
      "sha256": "826e938f58ccf78097904dffbb4f4c5cf150eb3253712ea60b5607ce0e6ae9d1",
      "actually_viewed": true
    },
    "BGL-volumes-2406.01090-013": {
      "path": "checks/P18-Hopf-primary-pages/BGL-volumes-2406.01090-p013.png",
      "sha256": "820ce8f334fb332695349edd2176796c85f410d9857deaf8ab26478ee9dceeb4",
      "actually_viewed": true
    },
    "BGL-volumes-2406.01090-014": {
      "path": "checks/P18-Hopf-primary-pages/BGL-volumes-2406.01090-p014.png",
      "sha256": "519ea7187592c6bcad777064117aa0454e2779a3b58745f1f823158ee2531789",
      "actually_viewed": true
    }
  },
  "original_task_and_private_note_entire_saved_root_read": true,
  "entire_current_saved_article_root_read": false,
  "active_proof_scope": "Only the surface extraction refinement and current article are active claims. The earlier general-dimensional extraction discussion remains unused and unverified.",
  "direct_root_candidate_checks": [
    "Finite point-blowup extraction on compact possibly singular main graphs; each generic source neighborhood is unchanged and J_new=J_old-m with m>=1.",
    "Exact generic ramification coordinates, Skoda/Holder pullback of zero-Lelong residuals, and horizontal zero cases.",
    "Every-real-weight multiplier ideal pullback by fiber coefficient estimates, Fubini and Krull intersection.",
    "Full envelope elliptic invariance and descent; reverse constraints use all base modifications via smooth compact fiber products.",
    "Actual nonclosed bounded product and canonical truncation, with fiber factor 6b and individual mass bounds.",
    "Ideal type, sums and positive scaling use the criterion only on projective P2, then actual ideal pullback; arbitrary larger backgrounds have exactness by sandwich only.",
    "Dyadic analytic full ordinary models, all modified Lelong convergence, genuine L1 pullback on target modifications.",
    "Explicit point image ideal floor(t-1), exceptional all-order profile, and actual mass 6b(a^2-1)."
  ],
  "recursive_certification_of_all_source_cited_dependencies": false,
  "source_assessment_is_not_a_granted_verdict": true,
  "scope_adequacy_against_original_completion_criteria_pending": true,
  "native_review_started": false,
  "native_blind_started": false,
  "mathematical_acceptance": false,
  "original_fully_closed": false,
  "publication_called": false
}

