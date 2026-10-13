# Full independent review of the new small-curvature ordinary-type extension

The current source controls A-G. Every theorem conclusion requires proof. The old source and private argument are preserved unchanged; their extra zero-Lelong hypothesis must not be silently inherited in the new B. Review the new E proof and every complete supporting proof directly. Previous candidate or PASS metadata is not mathematical evidence. No general S11 closure, arbitrary singular-curve restriction, smoothing within the type or unproved factorization follows. The unused broad S11 L1 maximal-density coefficient assertion is not a dependency.


## Entire current proposed author source

Path: papers/S11-zero-Lelong-residuals-and-blowups-at-poles.tex
SHA256: 2f658d41bbab3edce3eff40641e4f2faab09fcf58ea529e82006f45cbfa51cf6

\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\ddc}{dd^{\mathrm c}}
\newcommand{\PP}{\mathbb P}
\title{Nearly flat residuals and strict ordinary types\newline
under blowups at poles}
\author{Research manuscript}
\date{October 8, 2026}
\begin{document}
\maketitle
\begin{center}
\small Working draft. Independent mathematical review pending.
\end{center}
\begin{abstract}
We propose a strict-current criterion for ordinary types with an effective
logarithmic divisor and a residual whose ordinary type admits arbitrarily
small negative curvature. A Gauduchon trace estimate shows that its point
Lelong numbers are automatically zero. For a smooth real background, possibly nonclosed,
such a type contains a strict current exactly when the residual background
has a smooth strictly positive representative in its smooth gauge class.
The small-curvature property persists under smooth compact modifications.
The residual leaves every ambient multiplier ideal unchanged; for a normal
crossing logarithmic divisor this gives all intrinsic ideal traces on
every smooth target not contained in that divisor, even when the naive
residual restriction is identically minus infinity.
The necessity uses Demailly's established regularization theorem on the
closed current of the residual Hessian. In a declared nonclosed ruled
family with unbounded nonanalytic residual, this excludes mutual-type
strictness after every nonempty finite composition of point blowups,
including centers in the pole set. A one-sided strict witness persists,
as do the two already computed positive ordinary-type masses. These are
restricted proposed conclusions; the general S11 programme remains open.
\end{abstract}

\section{A precise ordinary-type criterion}
Throughout $\ddc=(i/(2\pi))\partial\bar\partial$. Fix a connected compact
complex manifold $M$ and a Hermitian form $h$. Every quasi-plurisubharmonic
function has its genuine canonical representative. Write $u\sim v$ for
mutual bounded order, including values at poles. A strict current in the
ordinary type $[r]$ for a smooth real $(1,1)$-form $\theta$ means a genuine
$v\sim r$ with $\theta+\ddc v\geq\epsilon h$, $\epsilon>0$.

Let $\Delta=\sum_{j=1}^N a_jD_j$ be a finite effective real divisor,
$a_j\geq0$. Smooth Hermitian metrics on its divisor bundles give a global
logarithmic potential $\ell_\Delta=\sum_j a_j\log\|s_j\|^2$ and a smooth
closed real form $\chi_\Delta$ with
\[
 \ddc\ell_\Delta=[\Delta]-\chi_\Delta.
\]
Zero coefficients contribute the identically zero function, including
on their divisors. For $\Delta=0$, use $\ell_\Delta=\chi_\Delta=0$.

\begin{lemma}\label{lem:automatic}
Let $q$ be a genuine quasi-psh function on $M$. If for every $\delta>0$
its ordinary type contains a genuine $q_\delta$ with
$\ddc q_\delta\geq-\delta h$, then $q$ has zero point Lelong numbers
everywhere.
\end{lemma}
\begin{proof}
Write $n=\dim_{\mathbb C}M$. For $n\geq2$ choose a smooth Gauduchon
metric $\gamma$, with $\ddc\gamma^{n-1}=0$, by
\cite[Theorem~2]{Gauduchon}. That theorem and its proof apply in every
complex dimension; the even-Betti hypothesis of the source's separate
Theorem~1 is not used. For $n=1$ choose any positive $\gamma$, since
$\gamma^0=1$. The current $T_\delta=\ddc q_\delta+\delta h$ is positive,
although it need not be closed. Distributional Stokes gives its exact trace
\[
 \int_M T_\delta\wedge\gamma^{n-1}
       =\delta\int_M h\wedge\gamma^{n-1}.
\]
Fix finitely many coordinate pairs $V_a\Subset U_a$ with the $V_a$
covering $M$. On each $U_a$ take a fixed smooth positive quadratic
$\rho_a$ with $\ddc\rho_a\geq h$, and let $\beta_a$ be the Euclidean
K\"ahler form. Then $p_{\delta,a}=q_\delta+\delta\rho_a$ is a genuine
psh function and its Hessian is a closed positive local current. Uniform
comparison of the smooth metrics on these charts gives
\[
 \int_{U_a}\ddc p_{\delta,a}\wedge\beta_a^{n-1}
 \leq C_a\int_M T_\delta\wedge\gamma^{n-1}+C_a\delta
 \leq C'_a\delta.
\]
Here one can first shrink the larger charts so their closures are compact
in coordinate domains; the quadratics and all comparison constants are
fixed independently of $\delta$ and its representative. Every point of
$V_a$ has a fixed-radius coordinate ball contained in $U_a$.
The local Lelong trace bound
\cite[III.5.5--5.8]{DemaillyBook} for the closed positive Hessian therefore
bounds its point Lelong number by $C''_a\delta$. Smooth additions do not
change a point Lelong number, and mutual bounded order preserves it by
the growth formula \cite[III.6.9(c)]{DemaillyBook}. The source operator is
twice ours; its fixed positive normalization factor is absorbed into the
constants and does not affect vanishing. Thus $0\leq\nu(q,x)\leq C\delta$
for every $x$ and every $\delta>0$. Letting $\delta\downarrow0$ proves
vanishing at every point. We used closedness only for the corrected local
Hessian, not for the global Hermitian form or for $T_\delta$.
\end{proof}

\begin{corollary}\label{cor:all-modifications}
Under the hypothesis of Lemma~\ref{lem:automatic}, let
$\pi:M'\to M$ be any smooth connected compact modification. The genuine
pullback $\pi^*q$ has the same small-curvature ordinary-type property on
$M'$, and zero point Lelong numbers everywhere on $M'$.
\end{corollary}
\begin{proof}
Fix $h'>0$ on $M'$. The smooth semipositive form $\pi^*h$ is bounded
above by $C h'$ for a fixed $C>0$. Genuine quasi-psh pullbacks are
canonical and locally integrable: after a local smooth correction they
are holomorphic pullbacks of psh functions, not identically minus infinity
on an open set since a modification is generically an isomorphism.
Pointwise ordinary inequalities pull back, including their pole values.
Thus $\pi^*q_\delta\sim\pi^*q$ and
$\ddc\pi^*q_\delta\geq-C\delta h'$. Apply
Lemma~\ref{lem:automatic} on $M'$ and let $\delta$ tend to zero.
This proves the assertion for this small-curvature class; it assumes no
general preservation theorem for arbitrary zero-Lelong potentials.
\end{proof}

\section{Ambient ideals and intrinsic traces}
We use precisely $\mathcal I(tu)=\{g:|g|^2e^{-tu}\text{ is locally
integrable}\}$, without an extra factor two.

\begin{lemma}\label{lem:ideal-neutral}
If a genuine quasi-psh function $q$ has zero point Lelong numbers, then
$e^{-s q}$ is locally integrable for every $s>0$. For every genuine
quasi-psh function $v$ and every $t>0$,
\[
 \mathcal I\bigl(t(v+q)\bigr)=\mathcal I(tv).
\]
\end{lemma}
\begin{proof}
Here the needed classical integrability fact follows directly from the
Bergman approximation \cite[Theorem~1.2]{DemaillyBergman}. Locally add
a smooth correction to obtain a psh $\varphi$ with zero point Lelong
numbers on a bounded pseudoconvex coordinate domain. For any $m>0$,
the weighted Bergman potential $\varphi_m$ has
$0\leq\nu(\varphi_m,x)\leq\nu(\varphi,x)=0$.
If every weighted square-integrable holomorphic function vanished at $x$,
the mean-value and Cauchy estimates would give
$\sup_{\|g\|\leq1}|g(z)|\leq C|z-x|$ near $x$.
Then the kernel formula would imply
$\varphi_m(z)\leq m^{-1}\log|z-x|+C$ and
$\nu(\varphi_m,x)\geq m^{-1}$, a contradiction.
An actual weighted holomorphic function is therefore nonzero at $x$.
On a smaller neighborhood it is bounded away from zero, and its defining
weighted norm proves $e^{-2m\varphi}\in L^1$. Smooth corrections do not
change local integrability. Taking $2m=s$ proves the first assertion.

The local upper bound on $q$ gives
$\mathcal I(t(v+q))\subset\mathcal I(tv)$.
For the converse let $g\in\mathcal I(tv)$ at a point. Smooth local
corrections make $v$ and $q$ psh without changing any ideal. Strong
openness \cite[Corollary~2.3]{DemaillyBergman} supplies $p>1$ with
$|g|^2e^{-ptv}\in L^1$ on a smaller neighborhood.
Set $p'=p/(p-1)$. The first assertion and local boundedness of $g$ give
$|g|^2e^{-p'tq}\in L^1$. H\"older applied to the exact factorization
\[
 |g|^2e^{-t(v+q)}
   =\bigl(|g|^2e^{-ptv}\bigr)^{1/p}
      \bigl(|g|^2e^{-p'tq}\bigr)^{1/p'}
\]
proves the required inclusion. These are applications of established
Bergman approximation and strong openness, with their cited foundations;
no new integrability or openness theorem is claimed.
\end{proof}

\begin{theorem}\label{thm:intrinsic-trace}
Suppose $q$ has the small-curvature property of Lemma~\ref{lem:automatic}.
For any finite effective divisor $\Delta$, every $t>0$ satisfies
\[
 \mathcal I\bigl(t(\ell_\Delta+q)\bigr)
       =\mathcal I(t\ell_\Delta).
\]
Assume in addition that $\Delta=\sum_j a_jD_j$ has simple normal crossings.
Let $Y\subset M$ be a smooth connected compact submanifold contained in
none of the $D_j$ with $a_j>0$. For every smooth connected compact
modification $\rho:Z\to Y$ and every prime divisor $E\subset Z$, the
original intrinsic ideal trace is finite and equals
\[
 \tau_{Y,\ell_\Delta+q}(E)
 =\lim_{t\to\infty}\frac1t
   \operatorname{ord}_E\bigl(\mathcal I(t(\ell_\Delta+q))\mathcal O_Y\bigr)
 =\sum_{j:a_j>0} a_j\operatorname{ord}_E\rho^*(D_j|_Y).
\]
The assertion uses ambient ideals and imposes no nontriviality on the
naive restriction $q|_Y$.
\end{theorem}
\begin{proof}
Lemma~\ref{lem:automatic} and Lemma~\ref{lem:ideal-neutral} give the
first equality of sheaves, for arbitrary $\Delta$.
For the trace formula, normal crossing coordinates and one-variable
polar integrability give
\[
 \mathcal I(t\ell_\Delta)
       =\mathcal O_M\left(-\sum_j\lfloor t a_j\rfloor D_j\right).
\]
Indeed a holomorphic germ must vanish along each coordinate divisor to
order at least $\lfloor t a_j\rfloor$; after division by these powers,
all remaining exponents are strictly greater than $-2$ and the product
weight is integrable. At integer $t a_j$ the next smaller vanishing order
has exponent $-2$ and diverges. Smooth metric factors do not affect this.
Restriction to $Y$ is the principal ideal locally generated by
$\prod_{j:a_j>0}(g_j|_Y)^{\lfloor t a_j\rfloor}$. Zero coefficients
are omitted before restricting equations or taking orders. Every nonzero restricted
equation pulls back to a nonzero holomorphic equation on $Z$.
Its order $N_{j,E}$ along $E$ is a finite nonnegative integer.
Thus the exact order is $\sum_j\lfloor t a_j\rfloor N_{j,E}$.
Division by $t$ and convergence of the finitely many coefficients prove
the formula. No assertion that lower order constraints automatically
give an exact envelope trace is used.
\end{proof}

\section{The strict-current criterion continued}
\begin{theorem}\label{thm:criterion}
Let $q$ be a genuine quasi-psh function. Suppose that for every
$\delta>0$ there is a genuine $q_\delta\sim q$ with
$\ddc q_\delta\geq-\delta h$.
Put $B=\theta-\chi_\Delta$. Then the ordinary type
$[\ell_\Delta+q]$ contains a strict $\theta$-current if and only if
there is a smooth real $f$ with $B+\ddc f>0$.
\end{theorem}

Lemma~\ref{lem:automatic} supplies the zero-Lelong property from the
specified ordinary-type hypothesis. This does not assert that a smooth
approximation stays in $[q]$. The small-curvature representatives are
used separately for sufficiency. The regularization mechanism for necessity is established
background \cite{Demailly92}, rather than a new smoothing theorem.

\begin{lemma}\label{lem:smooth}
If $q'$ has zero point Lelong numbers and
$B+\ddc q'\geq\epsilon h$, there is a smooth real $f$ such that
$B+\ddc f\geq\epsilon h/2$.
\end{lemma}
\begin{proof}
Apply \cite[Main Theorem~1.1]{Demailly92} to the closed almost positive
current $T=\ddc q'$, its global smooth representative $0$, and the
continuous real lower bound $\gamma=\epsilon h-B$. Closedness of
$\gamma$ is not a hypothesis. The source writes
$T=(i/\pi)\partial\bar\partial\psi$, so take $\psi=q'/2$.
For any fixed attenuation parameter $s>0$, it produces global potentials
$\psi_{s,k}$ smooth off $E_s(T)$ with
\[
 \frac{i}{\pi}\partial\bar\partial\psi_{s,k}
 \geq\gamma-\min\{\lambda_k,s\}u-\epsilon_k h.
\]
Here $\lambda_k$ are continuous, decrease pointwise to the Lelong function,
and $\epsilon_k\downarrow0$. A fixed smooth tangent metric has uniformly
bounded curvature on compact $M$, so $u=Ch$ can satisfy the stronger
Griffiths curvature hypothesis used in the source's Section~2 proof.
All Lelong level sets $E_s(T)$ are empty. Dini's theorem therefore gives
$\lambda_k\to0$ uniformly. For a sufficiently large $k$, the curvature
loss is at most $\epsilon h/2$. With $f=2\psi_{s,k}$ this proves the claim.
Continuous intermediate approximants, rather than the original unbounded
$q'$, are the objects to which the source applies Richberg smoothing.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:criterion}]
First suppose that $v\sim\ell_\Delta+q$ is strict. Off the support
$A$ of $\Delta$, set $q'=v-\ell_\Delta$. In a local trivialization write
$\ell_\Delta=\sum_j a_j\log|g_j|^2-\sigma$, where
$\ddc\sigma=\chi_\Delta$. Choose a smooth local quadratic $\rho$
with $\ddc\rho\geq\theta$. Then
\[
 v+\rho-\sum_j a_j\log|g_j|^2=q'+\rho-\sigma
\]
is psh off $A$ and locally bounded above, since $q'\leq q+C$ and
$q$ is locally bounded above. Canonical pluripolar removability
\cite[I.5.23--5.24]{DemaillyBook} extends it across $A$.
The sharper smooth lower bound
$\ddc\rho-\theta+\epsilon h$ is retained: off $A$ it holds, while
on $A$ the coefficient matrix of the extended positive Hessian has positive
measure restriction and the smooth correction has zero restriction.
Thus the resulting global canonical residual satisfies
\[
 B+\ddc q'\geq\epsilon h.
\]
The mutual inequalities $q'\sim q$ extend canonically, by adding common
local smooth corrections and using uniqueness of psh representatives.
Lemma~\ref{lem:automatic} and bounded difference give zero point Lelong
numbers for $q'$. Lemma~\ref{lem:smooth} now gives the required smooth $f$.

Conversely, compactness gives $B+\ddc f\geq\epsilon h$ for some
$\epsilon>0$. Choose $q_\delta$ with $\delta<\epsilon/2$ and set
$v=\ell_\Delta+q_\delta+f$. The sum is a genuine quasi-psh function
and $v\sim\ell_\Delta+q$. Poincar\'e--Lelong gives
\[
 \theta+\ddc v=[\Delta]+B+\ddc f+\ddc q_\delta
                \geq\epsilon h/2.
\]
This proves sufficiency in the specified ordinary type.
\end{proof}

\section{An unbounded residual on a nonclosed ruled surface}
Let $Y=\PP^1\times\PP^1$ with probability Fubini--Study forms $w_1,w_2$.
Take $G_p\leq0$ with $\ddc G_p=[p]-w$ and $\max G_p=0$ on the first
sphere, and write
\[
 D=\{p\}\times\PP^1,\quad U=1-(1-G_p)^\alpha,\quad
 r=bG_p+U,\quad \theta=cw_1+aw_2,
 \qquad 0<\alpha<1,\quad 0\leq b<c.
\]
Here $a>0$ is smooth on the first sphere; nonconstant $a$ makes $\theta$
nonclosed. The declared residual background is
$\beta=(c-b)w_1+aw_2>0$. The already checked family \cite{Ruled}
has the two full ordinary-type masses
\[
 R_-(\theta,[r])=2(c-b)\min a,
 \qquad R_+(\theta,[r])=2(c-b)\max a.
\]
These optimize over all rough competitors; they are distinct from a
Gauduchon variational volume with a prescribed probability.

For completeness the required small-curvature property has an explicit
construction. Put $\chi(t)=1-(1-t)^\alpha$, $\eta_L=\chi'(-L)$, and
\[
 \chi_L(t)=
 \begin{cases}
 \chi(t)-\eta_LL-\chi(-L),&t<-L,\\
 \eta_Lt,&-L\leq t\leq0.
 \end{cases}
\]
Values and derivatives agree at $-L$, and $\chi_L$ is convex increasing
with $0\leq\chi_L'\leq\eta_L\to0$. Hence the genuine function
$U_L=\chi_L(G_p)$ satisfies $U_L\sim U$ and
$\ddc U_L\geq-\eta_Lw_1$. The inequality extends canonically across
$D$. Thus $bG_p+U_L$ is an actual strict downstairs representative once
$\eta_L<c-b$.

\begin{lemma}\label{lem:pullback}
For a finite composition $\pi:Y'\to Y$ of point blowups,
$\pi^*U$ has zero point Lelong numbers everywhere, and its ordinary type
has arbitrarily small negative curvature on $Y'$.
\end{lemma}
\begin{proof}
The actual pullbacks $\pi^*U_L$ have bounded difference from $\pi^*U$,
including their poles. Fix $h'>0$ on $Y'$. Since the smooth semipositive
$\pi^*w_1$ is bounded by $C h'$, their Hessians are at least
$-C\eta_Lh'$.
To check all point Lelong numbers directly, write locally
$\pi^*G_p=\log|g|^2-\sigma$, where $g$ is a nonzero holomorphic
equation for the total transform of $D$. At a point of this divisor,
the germ has finite order $N$. Choose a direction $\xi$ with leading
homogeneous term $g_N(\xi)\ne0$; then
$g(t\xi)=t^N(g_N(\xi)+O(t))$. Along this direction $\pi^*U$ is
bounded below by $-C|\log|t||^\alpha-C$. Its spherical supremum has
the same lower bound. After a smooth local psh correction, the Lelong
growth quotient is therefore zero, since $\alpha<1$. Away from the
divisor the function is smooth. This argument concerns the specified
holomorphic-logarithm family and makes no assertion about pullbacks of
all zero-Lelong quasi-psh functions.
\end{proof}

\begin{theorem}\label{thm:blowup}
For every nonempty finite composition of point blowups $\pi:Y'\to Y$,
including centers in the pole set or an earlier exceptional divisor,
there is no strict $\pi^*\theta$-current with potential ordinarily
equivalent to $\pi^*r$. There is a strict witness
$v'\leq\pi^*r+C$. The two ordinary-type masses remain the displayed
positive values.
\end{theorem}
\begin{proof}
Apply Theorem~\ref{thm:criterion} with logarithmic divisor
$b\pi^*D$, residual $\pi^*U$ and background $\pi^*\theta$.
The resulting smooth residual background is $\pi^*\beta$.
The last exceptional curve $E\simeq\PP^1$ is contracted by the
composite $\pi$. If $\pi^*\beta+\ddc f>0$ for smooth $f$, restriction
to $E$ gives $\ddc(f|_E)>0$, because $\pi^*\beta|_E=0$.
Its integral is zero by curve Stokes, a contradiction. This proves the
mutual-type obstruction even when the original potential has a pole on
$E$: only the smooth $f$ has been restricted.

Construct a one-sided strict witness inductively. Suppose $v_j$ is strict
with lower Hermitian bound $\delta_jh_j$ on the current surface. For the
next point blowup $\pi_{j+1}$ with exceptional divisor $E_{j+1}$, choose
curvature $B_{E_{j+1}}$ of $\mathcal O(E_{j+1})$ negative on its vertical
tangent and a genuine $\ell_{E_{j+1}}$ with
$\ddc\ell_{E_{j+1}}=[E_{j+1}]-B_{E_{j+1}}$.
For sufficiently small $t_j>0$,
$\pi_{j+1}^*h_j-t_jB_{E_{j+1}}>0$.
Indeed in blowup charts $(x,y)\mapsto(x,xy)$ the pullback has a positive
horizontal coefficient, mixed coefficient $O(|x|)$ and Schur complement
at least $C_1|x|^2$. The added vertical curvature is at least $t_jC_2$;
its bounded mixed errors are $O(t_j|x|+t_j|x|^2+t_j^2)$.
Choose the exceptional neighborhood small, then $t_j$ small. On its
compact complement positivity persists under a bounded small perturbation.
Thus
\[
 v_{j+1}=\pi_{j+1}^*v_j+\delta_jt_j\ell_{E_{j+1}}
\]
has a strict current. Start with $v_0=bG_p+U_L$ as above. Genuine
quasi-psh pullbacks and their sums are locally integrable and canonical,
including over pole centers. The divisor logarithms are globally bounded
above, so induction gives $v'\leq\pi^*r+C$. The first part of the
theorem excludes mutual ordinary equivalence for this witness.

Finally, use the checked pure-pullback competitor bijection and actual
non-pluripolar pushforward identity of \cite{Ruled}. The bijection concerns
every competitor in the pulled-back ordinary type, and products carry no
mass on exceptional analytic sets. It preserves both infimum and supremum
of mass. The exceptional logarithms in the one-sided witness specify a
different ordinary type; their mass is not substituted for this optimization.
\end{proof}

\begin{remark}
The new proposed extension removes the outside-pole hypothesis in the
checked blowup obstruction of \cite{Ruled}, within the explicitly finite
point-blowup class. It supplies neither a factorization theorem for arbitrary
maps nor a strict-type criterion for every Hermitian ordinary singularity.
The small-curvature ordinary-type hypothesis implies zero point Lelong
numbers by the trace argument above; no additional zero-Lelong assumption
is imposed. General S11 remains open.
\end{remark}

\begin{thebibliography}{9}
\bibitem{Demailly92} J.-P.~Demailly,
\emph{Regularization of closed positive currents and Intersection Theory},
J.~Algebraic Geom. \textbf{1} (1992), 361--409,
Main Theorem~1.1 and Section~2.
\href{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization.pdf}{Author-hosted primary text}.
\bibitem{DemaillyBook} J.-P.~Demailly,
\emph{Complex Analytic and Differential Geometry}, I.5.23--5.24, III.5.5--5.8 and III.6.9.
\href{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf}{Author-hosted primary text}.
\bibitem{DemaillyBergman} J.-P.~Demailly,
\emph{On the cohomology of pseudoeffective line bundles},
arXiv:1401.5432v2, Theorem~1.2 and Section~2, especially Corollary~2.3.
Strong openness is due to Guan--Zhou; the supplied proof follows Hiep
and imports Ohsawa--Takegoshi and standard basis theory.
\href{https://arxiv.org/abs/1401.5432}{Primary text}.
\bibitem{Gauduchon} P.~Gauduchon,
\emph{Les m\'etriques standard d'une surface complexe compacte \`a premier
nombre de Betti pair}, Ast\'erisque \textbf{126} (1985), 129--135,
Theorem~2 and its proof, pp.~132--133.
\href{https://www.numdam.org/item/AST_1985__126__129_0/}{Published primary text}.
\bibitem{Ruled} \emph{Restricted masses and ordinary strict-current types
on a nonclosed ruled surface}, checked restricted construction, October~2026,
Sections~2 and~5. General S11 remains open.
\href{https://github.com/MingchenXia/non-kahler-pluripotential-theory/blob/2ec45dec6172ced6e2af18b2b5fe657c07aeee9e/research/papers/S11-nonclosed-ruled-restricted-masses-and-strict-types.tex}{Retained checked source}.
\end{thebibliography}
\end{document}


## Entire prior private proposed proof; zero-Lelong hypothesis retained historically

Path: notes/S11-zero-Lelong-residual-obstruction-at-pole-centers-20261008.private-unverified.md
SHA256: 4f55010cd7e3aadcdd59e089b3d06800d6b9ecedebcf539d2a03e6b4f09ddec1

# S11: a proposed extension to blowup centers in the pole set

Private unverified research, 8 October 2026. This is not part of the frozen
restricted A--G task or the checked paper at commit
2ec45dec6172ced6e2af18b2b5fe657c07aeee9e. No native review, statement-only
reconstruction or final comparison has been admitted for this extension. General
S11 remains open. The global regularization mechanism below is established
Demailly background; no priority is claimed for it.

Use dd^c = i partial barpartial/(2 pi). Keep the checked ruled family
Y = P1 x P1, D = {p} x P1, theta = c w1 + a w2,
r = b Gp + U_alpha, U_alpha = 1-(1-Gp)^alpha, 0<alpha<1,
a>0 smooth on the first factor, and 0<=b<c. Put
beta = (c-b) w1 + a w2. All representatives are genuine canonical quasi-psh
functions. A composition of point blowups is the specified class of
modifications here, not an assertion about every possible modification without
checking factorization.

## 1. The precise standard regularization input

Demailly, Regularization of closed positive currents and Intersection Theory,
J. Algebraic Geometry 1 (1992), 361--409, Main Theorem 1.1, author-hosted full
primary text:
https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization.pdf.

The actual full PDF was retrieved successfully with curl (actual process 2962,
actual exit 0). The PDF SHA256 is
3dbc4cb1d915168cfc00d23da74acf1a53fdc1c0ed4a2d7ede85e2b6d159dc90.
The extracted text SHA256 is
98781e21d86b8407941e7427297c3c6b7bde63ef415b6709d0f97295c4667217.
The complete printed main statement and context (lines 1--118), reduction
(275--287), complete stronger-Griffiths-bound proof in Section 2 (275--640), and
the closing general proof/application organization (1638--1740) were actually
root-read. The Section 2 smoothing lemma has a printed proof sketch; its
application here is only to the continuous intermediate regularizations.
No direct Richberg smoothing of the original unbounded q is asserted. Imported
Kiselman and continuous Richberg foundations are not recursively certified.

For a closed almost positive current T = alpha + (i/pi) partial barpartial psi
on a compact Hermitian manifold, T>=gamma with gamma continuous real (1,1),
the theorem produces potentials psi_(s,j), smooth off the Lelong level set
E_s(T), with the same global dd^c class. The curvature loss is bounded by
min(lambda_j,s) u + epsilon_j h, where lambda_j are continuous, decrease to
the pointwise Lelong function, and epsilon_j->0. Gamma need not be closed.
For the Section 2 proof one may choose u=C h, because the curvature of a fixed
smooth Hermitian tangent metric is uniformly bounded on the compact manifold.
The stronger Griffiths lower-bound hypothesis is therefore available here.

## 2. A necessary consequence for a nonclosed smooth background

Proposed lemma: If B is smooth real (1,1) on compact M, q is genuine quasi-psh,
all its point Lelong numbers are zero, and B+dd^c q>=epsilon h with h>0 and
epsilon>0, then there exists a smooth real f with B+dd^c f>=epsilon h/2.

Apply the preceding theorem to the CLOSED current T=dd^c q, with alpha=0,
psi=q/2 (the original theorem uses i/pi), and gamma=epsilon h-B.
T is almost positive and gamma is a continuous real form. Since all Lelong
numbers are zero, E_s(T) is empty for any fixed s>0, so the produced potentials
are smooth everywhere. On compact M, Dini's theorem makes lambda_j->0 uniformly;
also u<=C h. Thus, for some j,
min(lambda_j,s)u+epsilon_j h<=epsilon h/2. Set f=2 psi_(s,j).
Then dd^c f>=epsilon h/2-B, as required. The approximants need not be
ordinarily equivalent to q, and the lemma asserts no converse for a prescribed
ordinary type. In particular, no regularization is applied directly to the
nonclosed current B+dd^c q.

If pi:M->Y contracts a smooth compact curve E, the smooth background
B=pi^*beta cannot have such an f: restricting the smooth strict inequality to
E gives dd^c(f|E)>=epsilon h|E/2, whereas pi^*beta|E=0. Compact curve Stokes
contradicts this. The curve restriction is of a smooth f, not of q, which may be
identically minus infinity on E.

## 3. Removing the logarithmic divisor at every center

Suppose pi is any finite composition of point blowups and v' is a strict
pi^*theta-psh function ordinarily equivalent to pi^*r. Write D'=pi^*D as the
effective total-transform divisor, including its multiplicities. Off D', set
q'=v'-b pi^*Gp. The ordinary inequalities say q'~pi^*U_alpha there.

Locally pi^*Gp=log|g|^2-sigma, where g is a holomorphic local equation for D'
and dd^c sigma=pi^*w1. Add a smooth local quadratic rho dominating pi^*theta.
Then q'+rho-b sigma is psh off D', locally bounded above because
q'<=pi^*U_alpha+C, and has Hessian lower bound
dd^c rho-pi^*theta+epsilon h'. Canonical pluripolar extension produces a
genuine residual q'. To retain this sharper bound across D', decompose the
coefficient measures into restrictions off D' and on D': the latter matrix is
positive, and the smooth bound has zero restriction to the analytic set. Hence
pi^*beta+dd^c q'>=epsilon h' holds globally. Both ordinary inequalities extend
canonically, so q'~pi^*U_alpha. This is the same coefficient-measure argument
as in the checked divisor-removal proof; no restriction of v' or q' to D' is
performed. The b=0 case is canonical without any 0 times minus infinity.

Every point Lelong number of pi^*U_alpha is zero. At a point of D', the local
equation g is nonzero as a holomorphic germ and has some finite order N. Along
a complex direction where its leading homogeneous term is nonzero,
g(t xi)=t^N(g_N(xi)+O(t)). Consequently U_alpha composed with pi is bounded
below there by -C |log|t||^alpha-C. Its spherical supremum has the same lower
bound. Since 0<alpha<1, the Lelong growth quotient tends to zero. The function
is quasi-psh (add a smooth local correction), so its Lelong number is nonnegative;
therefore it is exactly zero. Away from D' it is smooth. Bounded difference
then gives nu(q',x)=0 everywhere. This proof is for the explicit holomorphic
logarithm-squared family; it does not assert that pullback preserves zero Lelong
numbers for every arbitrary quasi-psh function.

## 4. Proposed stronger obstruction and the one-sided witness

Any nonempty finite composition of point blowups has a smooth last exceptional
P1 contracted by the composite pi. Sections 2--3 would exclude EVERY strict
representative v'~pi^*r, including when a center belongs to D or to an earlier
exceptional divisor. This avoids the bounded-near-E condition in the checked
paper. The currently published proposition applies only to centers outside D;
this new claim is not silently substituted into that proposition.

A strict one-sided witness still has a direct recursive construction. Start
with the actual downstairs v0=b Gp+U_L, where its curvature lower bound is
delta0(w1+w2)>0. For a point blowup pi1 with exceptional E1, choose curvature
B_E1 of O(E1) with negative Fubini--Study restriction to E1. The same finite
chart Schur-complement argument as in the checked paper makes
pi1^*h0-t1 B_E1 positive for sufficiently small t1>0. With
dd^c ell_E1=[E1]-B_E1, the genuine function
v1=pi1^*v0+delta0 t1 ell_E1 gives a strict current and v1<=pi1^*r+C.
This works even if v0 is minus infinity at the center: its pullback is a genuine
quasi-psh function off and across the exceptional set, not identically minus
infinity on the whole connected source. The sum is locally integrable and
canonical. Repeat with the actual strict Hermitian lower bound at each stage.
The final vj is <=pi^*r+C. By the preceding obstruction it cannot be ordinarily
equivalent to pi^*r.

The checked pure-pullback competitor bijection and non-pluripolar pushforward
law still give R_-=2(c-b)min a and R_+=2(c-b)max a for these backgrounds and
pulled-back ordinary types. Those are already checked laws, not new assertions
about arbitrary upstairs-density Gauduchon volume. The added exceptional poles
in the one-sided witness belong to a different ordinary type.

## Unfinished verification boundary

This is a full proposed argument, not an accepted result. The exact uniform
regularization application, every canonical lower-bound step and all blowup
centers need independent native review and statement-only reconstruction.
No analytic factorization theorem is required for the explicitly finite
point-blowup class. No classification or strict-type criterion for arbitrary
Hermitian backgrounds follows. The current S02 owner remains the sole native
mathematical owner. The already checked S11 article and its frozen evidence are
unchanged.


## Entire preserved prior draft before the new E proof

Path: checks/S11-zero-Lelong-pole-center-before-small-curvature-lemma-20261008-source.tex
SHA256: 9ad469dadc99eb22120d4d5f28241467d7ce005ff95a12900e408d9f27d6e47a

\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,hyperref}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\hypersetup{hidelinks}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\ddc}{dd^{\mathrm c}}
\newcommand{\PP}{\mathbb P}
\title{Zero-Lelong residuals and strict ordinary types\newline
under blowups at poles}
\author{Research manuscript}
\date{October 8, 2026}
\begin{document}
\maketitle
\begin{center}
\small Working draft. Independent mathematical review pending.
\end{center}
\begin{abstract}
We propose a strict-current criterion for ordinary types with an effective
logarithmic divisor and a zero-Lelong residual whose type admits arbitrarily
small negative curvature. For a smooth real background, possibly nonclosed,
such a type contains a strict current exactly when the residual background
has a smooth strictly positive representative in its smooth gauge class.
The necessity uses Demailly's established regularization theorem on the
closed current of the residual Hessian. In a declared nonclosed ruled
family with unbounded nonanalytic residual, this excludes mutual-type
strictness after every nonempty finite composition of point blowups,
including centers in the pole set. A one-sided strict witness persists,
as do the two already computed positive ordinary-type masses. These are
restricted proposed conclusions; the general S11 programme remains open.
\end{abstract}

\section{A precise ordinary-type criterion}
Throughout $\ddc=(i/(2\pi))\partial\bar\partial$. Fix a connected compact
complex manifold $M$ and a Hermitian form $h$. Every quasi-plurisubharmonic
function has its genuine canonical representative. Write $u\sim v$ for
mutual bounded order, including values at poles. A strict current in the
ordinary type $[r]$ for a smooth real $(1,1)$-form $\theta$ means a genuine
$v\sim r$ with $\theta+\ddc v\geq\epsilon h$, $\epsilon>0$.

Let $\Delta=\sum_{j=1}^N a_jD_j$ be a finite effective real divisor,
$a_j\geq0$. Smooth Hermitian metrics on its divisor bundles give a global
logarithmic potential $\ell_\Delta=\sum_j a_j\log\|s_j\|^2$ and a smooth
closed real form $\chi_\Delta$ with
\[
 \ddc\ell_\Delta=[\Delta]-\chi_\Delta.
\]
Zero coefficients contribute the identically zero function, including
on their divisors. For $\Delta=0$, use $\ell_\Delta=\chi_\Delta=0$.

\begin{theorem}\label{thm:criterion}
Let $q$ be a genuine quasi-psh function with zero point Lelong numbers
everywhere. Suppose that for every $\delta>0$ there is a genuine
$q_\delta\sim q$ with $\ddc q_\delta\geq-\delta h$.
Put $B=\theta-\chi_\Delta$. Then the ordinary type
$[\ell_\Delta+q]$ contains a strict $\theta$-current if and only if
there is a smooth real $f$ with $B+\ddc f>0$.
\end{theorem}

This does not assert that a smooth approximation stays in $[q]$.
The small-curvature representatives are a separate type hypothesis used
for sufficiency. The regularization mechanism for necessity is established
background \cite{Demailly92}, rather than a new smoothing theorem.

\begin{lemma}\label{lem:smooth}
If $q'$ has zero point Lelong numbers and
$B+\ddc q'\geq\epsilon h$, there is a smooth real $f$ such that
$B+\ddc f\geq\epsilon h/2$.
\end{lemma}
\begin{proof}
Apply \cite[Main Theorem~1.1]{Demailly92} to the closed almost positive
current $T=\ddc q'$, its global smooth representative $0$, and the
continuous real lower bound $\gamma=\epsilon h-B$. Closedness of
$\gamma$ is not a hypothesis. The source writes
$T=(i/\pi)\partial\bar\partial\psi$, so take $\psi=q'/2$.
For any fixed attenuation parameter $s>0$, it produces global potentials
$\psi_{s,k}$ smooth off $E_s(T)$ with
\[
 \frac{i}{\pi}\partial\bar\partial\psi_{s,k}
 \geq\gamma-\min\{\lambda_k,s\}u-\epsilon_k h.
\]
Here $\lambda_k$ are continuous, decrease pointwise to the Lelong function,
and $\epsilon_k\downarrow0$. A fixed smooth tangent metric has uniformly
bounded curvature on compact $M$, so $u=Ch$ can satisfy the stronger
Griffiths curvature hypothesis used in the source's Section~2 proof.
All Lelong level sets $E_s(T)$ are empty. Dini's theorem therefore gives
$\lambda_k\to0$ uniformly. For a sufficiently large $k$, the curvature
loss is at most $\epsilon h/2$. With $f=2\psi_{s,k}$ this proves the claim.
Continuous intermediate approximants, rather than the original unbounded
$q'$, are the objects to which the source applies Richberg smoothing.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:criterion}]
First suppose that $v\sim\ell_\Delta+q$ is strict. Off the support
$A$ of $\Delta$, set $q'=v-\ell_\Delta$. In a local trivialization write
$\ell_\Delta=\sum_j a_j\log|g_j|^2-\sigma$, where
$\ddc\sigma=\chi_\Delta$. Choose a smooth local quadratic $\rho$
with $\ddc\rho\geq\theta$. Then
\[
 v+\rho-\sum_j a_j\log|g_j|^2=q'+\rho-\sigma
\]
is psh off $A$ and locally bounded above, since $q'\leq q+C$ and
$q$ is locally bounded above. Canonical pluripolar removability
\cite[I.5.23--5.24]{DemaillyBook} extends it across $A$.
The sharper smooth lower bound
$\ddc\rho-\theta+\epsilon h$ is retained: off $A$ it holds, while
on $A$ the coefficient matrix of the extended positive Hessian has positive
measure restriction and the smooth correction has zero restriction.
Thus the resulting global canonical residual satisfies
\[
 B+\ddc q'\geq\epsilon h.
\]
The mutual inequalities $q'\sim q$ extend canonically, by adding common
local smooth corrections and using uniqueness of psh representatives.
Bounded difference preserves point Lelong numbers. Lemma~\ref{lem:smooth}
now gives the required smooth $f$.

Conversely, compactness gives $B+\ddc f\geq\epsilon h$ for some
$\epsilon>0$. Choose $q_\delta$ with $\delta<\epsilon/2$ and set
$v=\ell_\Delta+q_\delta+f$. The sum is a genuine quasi-psh function
and $v\sim\ell_\Delta+q$. Poincar\'e--Lelong gives
\[
 \theta+\ddc v=[\Delta]+B+\ddc f+\ddc q_\delta
                \geq\epsilon h/2.
\]
This proves sufficiency in the specified ordinary type.
\end{proof}

\section{An unbounded residual on a nonclosed ruled surface}
Let $Y=\PP^1\times\PP^1$ with probability Fubini--Study forms $w_1,w_2$.
Take $G_p\leq0$ with $\ddc G_p=[p]-w$ and $\max G_p=0$ on the first
sphere, and write
\[
 D=\{p\}\times\PP^1,\quad U=1-(1-G_p)^\alpha,\quad
 r=bG_p+U,\quad \theta=cw_1+aw_2,
 \qquad 0<\alpha<1,\quad 0\leq b<c.
\]
Here $a>0$ is smooth on the first sphere; nonconstant $a$ makes $\theta$
nonclosed. The declared residual background is
$\beta=(c-b)w_1+aw_2>0$. The already checked family \cite{Ruled}
has the two full ordinary-type masses
\[
 R_-(\theta,[r])=2(c-b)\min a,
 \qquad R_+(\theta,[r])=2(c-b)\max a.
\]
These optimize over all rough competitors; they are distinct from a
Gauduchon variational volume with a prescribed probability.

For completeness the required small-curvature property has an explicit
construction. Put $\chi(t)=1-(1-t)^\alpha$, $\eta_L=\chi'(-L)$, and
\[
 \chi_L(t)=
 \begin{cases}
 \chi(t)-\eta_LL-\chi(-L),&t<-L,\\
 \eta_Lt,&-L\leq t\leq0.
 \end{cases}
\]
Values and derivatives agree at $-L$, and $\chi_L$ is convex increasing
with $0\leq\chi_L'\leq\eta_L\to0$. Hence the genuine function
$U_L=\chi_L(G_p)$ satisfies $U_L\sim U$ and
$\ddc U_L\geq-\eta_Lw_1$. The inequality extends canonically across
$D$. Thus $bG_p+U_L$ is an actual strict downstairs representative once
$\eta_L<c-b$.

\begin{lemma}\label{lem:pullback}
For a finite composition $\pi:Y'\to Y$ of point blowups,
$\pi^*U$ has zero point Lelong numbers everywhere, and its ordinary type
has arbitrarily small negative curvature on $Y'$.
\end{lemma}
\begin{proof}
The actual pullbacks $\pi^*U_L$ have bounded difference from $\pi^*U$,
including their poles. Fix $h'>0$ on $Y'$. Since the smooth semipositive
$\pi^*w_1$ is bounded by $C h'$, their Hessians are at least
$-C\eta_Lh'$.
To check all point Lelong numbers directly, write locally
$\pi^*G_p=\log|g|^2-\sigma$, where $g$ is a nonzero holomorphic
equation for the total transform of $D$. At a point of this divisor,
the germ has finite order $N$. Choose a direction $\xi$ with leading
homogeneous term $g_N(\xi)\ne0$; then
$g(t\xi)=t^N(g_N(\xi)+O(t))$. Along this direction $\pi^*U$ is
bounded below by $-C|\log|t||^\alpha-C$. Its spherical supremum has
the same lower bound. After a smooth local psh correction, the Lelong
growth quotient is therefore zero, since $\alpha<1$. Away from the
divisor the function is smooth. This argument concerns the specified
holomorphic-logarithm family and makes no assertion about pullbacks of
all zero-Lelong quasi-psh functions.
\end{proof}

\begin{theorem}\label{thm:blowup}
For every nonempty finite composition of point blowups $\pi:Y'\to Y$,
including centers in the pole set or an earlier exceptional divisor,
there is no strict $\pi^*\theta$-current with potential ordinarily
equivalent to $\pi^*r$. There is a strict witness
$v'\leq\pi^*r+C$. The two ordinary-type masses remain the displayed
positive values.
\end{theorem}
\begin{proof}
Apply Theorem~\ref{thm:criterion} with logarithmic divisor
$b\pi^*D$, residual $\pi^*U$ and background $\pi^*\theta$.
The resulting smooth residual background is $\pi^*\beta$.
The last exceptional curve $E\simeq\PP^1$ is contracted by the
composite $\pi$. If $\pi^*\beta+\ddc f>0$ for smooth $f$, restriction
to $E$ gives $\ddc(f|_E)>0$, because $\pi^*\beta|_E=0$.
Its integral is zero by curve Stokes, a contradiction. This proves the
mutual-type obstruction even when the original potential has a pole on
$E$: only the smooth $f$ has been restricted.

Construct a one-sided strict witness inductively. Suppose $v_j$ is strict
with lower Hermitian bound $\delta_jh_j$ on the current surface. For the
next point blowup $\pi_{j+1}$ with exceptional divisor $E_{j+1}$, choose
curvature $B_{E_{j+1}}$ of $\mathcal O(E_{j+1})$ negative on its vertical
tangent and a genuine $\ell_{E_{j+1}}$ with
$\ddc\ell_{E_{j+1}}=[E_{j+1}]-B_{E_{j+1}}$.
For sufficiently small $t_j>0$,
$\pi_{j+1}^*h_j-t_jB_{E_{j+1}}>0$.
Indeed in blowup charts $(x,y)\mapsto(x,xy)$ the pullback has a positive
horizontal coefficient, mixed coefficient $O(|x|)$ and Schur complement
at least $C_1|x|^2$. The added vertical curvature is at least $t_jC_2$;
its bounded mixed errors are $O(t_j|x|+t_j|x|^2+t_j^2)$.
Choose the exceptional neighborhood small, then $t_j$ small. On its
compact complement positivity persists under a bounded small perturbation.
Thus
\[
 v_{j+1}=\pi_{j+1}^*v_j+\delta_jt_j\ell_{E_{j+1}}
\]
has a strict current. Start with $v_0=bG_p+U_L$ as above. Genuine
quasi-psh pullbacks and their sums are locally integrable and canonical,
including over pole centers. The divisor logarithms are globally bounded
above, so induction gives $v'\leq\pi^*r+C$. The first part of the
theorem excludes mutual ordinary equivalence for this witness.

Finally, use the checked pure-pullback competitor bijection and actual
non-pluripolar pushforward identity of \cite{Ruled}. The bijection concerns
every competitor in the pulled-back ordinary type, and products carry no
mass on exceptional analytic sets. It preserves both infimum and supremum
of mass. The exceptional logarithms in the one-sided witness specify a
different ordinary type; their mass is not substituted for this optimization.
\end{proof}

\begin{remark}
The new proposed extension removes the outside-pole hypothesis in the
checked blowup obstruction of \cite{Ruled}, within the explicitly finite
point-blowup class. It supplies neither a factorization theorem for arbitrary
maps nor a strict-type criterion for every Hermitian ordinary singularity.
The zero-Lelong condition and the small-curvature type hypothesis retain
their separate roles. General S11 remains open.
\end{remark}

\begin{thebibliography}{9}
\bibitem{Demailly92} J.-P.~Demailly,
\emph{Regularization of closed positive currents and Intersection Theory},
J.~Algebraic Geom. \textbf{1} (1992), 361--409,
Main Theorem~1.1 and Section~2.
\href{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization.pdf}{Author-hosted primary text}.
\bibitem{DemaillyBook} J.-P.~Demailly,
\emph{Complex Analytic and Differential Geometry}, I.5.23--5.24.
\href{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf}{Author-hosted primary text}.
\bibitem{Ruled} \emph{Restricted masses and ordinary strict-current types
on a nonclosed ruled surface}, checked restricted construction, October~2026,
Sections~2 and~5. General S11 remains open.
\href{https://github.com/MingchenXia/non-kahler-pluripotential-theory/blob/2ec45dec6172ced6e2af18b2b5fe657c07aeee9e/research/papers/S11-nonclosed-ruled-restricted-masses-and-strict-types.tex}{Retained checked source}.
\end{thebibliography}
\end{document}


## Entire credited checked ruled-family source

Path: papers/S11-nonclosed-ruled-restricted-masses-and-strict-types.tex
SHA256: 792430edafae59f6c159735db721d80f10b8a58ec199d6050ca0524d5be3e4dd

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
\small Checked restricted construction. General S11 remains open.
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


## Every complete ruled-family reconstruction and support DAG

Path: checks/S11-nonclosed-ruled-current-statement-only-cold-20261008-complete-result.json
SHA256: aeac7d4e0dca66cbc5171b944f7bfb6487dcdbeaa076afca5da9c6a0dea49dd9

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


## Entire credited ruled-family final public report, not a proof premise

Path: checks/S11-nonclosed-ruled-A-G-limited-final-comparison-20261008-complete-result.json
SHA256: 321b22161b7c61e30530597f8759ce192e054c93fb84efc84317147a67464d15

{
  "verdict": "PASS",
  "report": "PASS applies solely to the complete restricted A–G theorem. I independently checked the current article, the historical restricted proof and first-moment-free supplement, and every reconstruction note n1–n7. No restricted proof depends on the excluded general L¹ coefficient theorem, unspecified E_env definitions, historical verdicts, candidate flags, or computational artifacts. The historical full-companion INCONCLUSIVE remains unchanged, and unrestricted S11 remains open.\n\nA. Both residual constructions work. The article’s piecewise χ_L is increasing, convex and C¹ at its joining point; its unchanged singular tail differs from U by a finite constant. It satisfies dd^c U_L≥−ε_Lw, where ε_L→0, and U≤U_L≤0 with L¹ convergence to zero. The reconstruction’s q_L=L^α−(L−G_p)^α has the same ordinary type and curvature bound −αL^(α−1)w. The transverse boundary flux tends to zero, so these residuals have no point atom. Choosing the curvature loss below c−b supplies the displayed mutual-type strict witness even when c−b<α.\n\nCanonical divisorial removal is valid for every rough competitor. Off D, subtracting bG_p leaves q~U. After adding a local quadratic, the bounded-above psh function extends canonically. The sharper nonclosed inequality survives: the extended positive Hessian has positive coefficient measures on D, whereas the smooth correction assigns D zero measure. Thus θ+dd^c v=b[D]+β+dd^c q, with β=(c−b)w1+aw2. Canonical equality follows from almost-everywhere equality; no subtraction of infinite pole values is used. Fiber averaging gives a positive curve measure (c−b)w+dd^c q̄ of total mass c−b. Negative mass excludes b>c; zero mass forces q̄ constant and contradicts q̄~U, excluding b=c. Empty types receive no numerical volume. The sublogarithmic residual is unbounded and cannot have an analytic ordinary type.\n\nB. The calculation covers every rough fiber-dependent competitor. Set k=c−b>0 and choose the admissible reference U_L₀ with ε_L₀<k/2. For a closed K=C(w1+w2) dominating β, S=K+dd^c q and S₀=K+dd^c U_L₀ are closed positive cohomologous currents on the compact Kähler surface Y. Their potentials have bounded difference and are locally bounded outside the closed locally complete pluripolar divisor D. Consequently every hypothesis of the permitted comparison is established in degrees one and two and in both ordinary orders. It is never applied to a nonclosed current.\n\nThe separated reference has ⟨S₀²⟩=2C(Cw1+dd^c U_L₀)∧w2 and mass 2C². Degree-one comparison gives the full K-trace of ⟨S⟩. Since S−⟨S⟩=1_D S is positive and has zero strictly positive K-trace, it vanishes. Degree-two comparison gives ∫⟨S²⟩=∫K². With B=β−K, the actual extended measure is ⟨S²⟩+2B∧S+B². Each term is finite and has zero mass on D; bounded locality identifies the expression off D, hence globally. Distributional Stokes yields M(v)=∫β²+2∫q dd^cβ=2∫aσ, where σ=kw+dd^c q̄ is positive of mass k. This proves positive finite masses and both global bounds. It uses only L¹ pairing with smooth forms, not a nonlinear first moment.\n\nBoth extremizing constructions are actual same-type potentials. In the article, smooth positive ζ_j of mass k are paired with sufficiently small-curvature U_L_j. In n2, σ_j=(k−η_j)ξ_j+(η_jw+dd^c q_L_j), where the second positive summand has mass η_j→0. Thus σ_j→kδ_x and M(v_j)→2ka(x), including when x=p. Taking x at the extrema proves R_−=2k min a and R_+=2k max a. Finally ∫G_p dd^c a=a(p)−∫aw gives exactly the asserted original-background affine formula. The historical supplement’s raw-U range c≥α is respected; its application when k<α uses the admissible U_L₀ reference, whose hypotheses were checked separately.\n\nC. The chosen r₀ is genuinely admissible, so its product pullback gives the claimed Θ-psh ambient potential. Θ is strictly positive, and dΘ≠0 when a is nonconstant. The generic Lelong number along Y₀ is zero because the reference is locally bounded on its generic locus. Near D_Z, u_Z=b log|z|²−T^α+O(1), with T=−log|z|². A germ of transverse order j has radial integral comparable to ∫exp(−(j+1−sb)T+sT^α)dT. It converges precisely when j+1>sb. At equality it diverges, so the coefficient is floor(sb), including every integer boundary weight with the stipulated no-extra-factor-2 convention. Factoring a general germ and using a nonzero leading tangential coefficient establishes both necessity and sufficiency.\n\nRestricting these actual ambient principal ideals gives O_Y₀(−floor(sb)D). Their orders on every smooth compact modification are floor(sb)ord_E(π*D); the defining limit therefore equals b ord_E(π*D). This establishes the entire intrinsic trace system through ambient ideal restrictions. It does not assert multiplier-ideal pullback commutation. The residual has trivial ideals at all real weights while remaining unbounded.\n\nD. For q_L, angular integration with T=−G_p gives w=e^(−T)dT and dG_p∧d^cG_p=(1−e^(−T))dT. The positive curve measure Cw+dd^c q_L has density (C−α(L+T)^(α−1))e^(−T)+α(1−α)(L+T)^(α−2)(1−e^(−T)), mass C and no atom. Thus its actual separated closed square has full mass 2C². Multiplication by −q_L gives the positive first-moment tail 2Cα(1−α)T^(2α−2)dT. Finiteness is exactly α<1/2; at α=1/2 the divergence is (C/2)log R for a T-cutoff R. The article’s shifted tail has the same threshold. No energy or first-moment hypothesis enters A–C.\n\nE. Smooth gauges preserve actual currents, finite-level products and their extensions, competitor classes, and all real-weight ideals. For a pure modification, adding a pulled-back local quadratic makes the upstairs potential psh. Descent on the biholomorphic complement has a local upper bound by properness; canonical removal and the coefficient-measure argument retain the exact downstairs smooth-background inequality. Ordinary comparisons extend canonically. Pullback and descent are inverse, including pole values. For modifications, the sharper pullback inequality follows by the same extension argument; n1 also supplies a valid decreasing local approximation proof. Locality on the biholomorphic complements and zero mass on analytic sets prove the actual pushforward law, upstairs finiteness, and equality of both optimized masses. Intrinsic trace transport means total transforms of the original restricted ambient ideals, followed by composition of modifications.\n\nBoth point-blowup witnesses are valid. The author’s negative exceptional curvature has the required vertical sign; the displayed Schur-complement estimate proves positivity after choosing the neighborhood and then the parameter small. In n5, the cutoff logarithm pulls back near E to log|s|²+log(1+|ξ|²), so its Hessian is [E]+η with η smooth and positive tangentially on E. The form επ*ω+δη is strictly positive near E, remains positive in the inner punctured region, and is positive on the cutoff annulus for δM<ε. The resulting genuine witness is at most π*r plus a constant and acquires an exceptional pole.\n\nConversely, mutual ordinary equivalence forces boundedness near E. A hypothetical strict witness can be restricted genuinely to E: subtract local quadratics whose constant Hessians lie below the smooth lower bound, with positive tangent coefficient. The restricted curve Hessian is then strictly positive, contradicting its zero integral by Stokes. Thus positive preserved lower mass supplies no mutual strict witness on this blowup. Exceptional curvature subtraction and invariance for arbitrary upstairs Gauduchon densities are not asserted.\n\nF. Both independent all-test proofs are sound with D_μ(T)=∫sqrt(T²/μ)μ and V_μ equal to the square of the infimum quotient. In the article, Poisson solvability gives Ω=gw1+aw2=β+dd^c f with Ω²=Vμ. Stokes and matrix arithmetic–geometric mean prove the lower bound for every positive dd^c-closed test. The closed positive T=Ω/a attains it. In n6, fiber integration of an arbitrary mixed test gives a positive constant vertical average κ; determinant positivity and Cauchy–Schwarz give D²≤2AκH, while the numerator is kκ+A. The identity (A−kκ)²≥0 proves the same unrestricted bound. Both give V_μ(β)=2k/H, separately from V_μ(θ)=2c/H. The dependence on m and distinction from R_+ follow directly.\n\nFor fixed real d and smooth first-factor e, H_s′=∫em/a_s² and D_μ(T_s)=sqrt(V_s)H_s. Direct differentiation gives (sqrt(V_s))′=−[d+(V_s/2)H_s′]/[sqrt(V_s)H_s], exactly the claimed minimizing-test pairing. Uniform positivity on each compact segment justifies differentiation and integration. With signed d,e this is a signed subtraction identity; it is not a derivative of R_+.\n\nG. The author’s U_31 has ε_31≈0.315336<3/8. The reconstruction’s alternative q_16=8−(16−G_p)^(3/4) has curvature loss exactly 3/8 and gives a strict lower bound (3/8)(w1+w2). Both are valid mutual-type references. The height distribution gives min a=1, max a=3 and H=(log 3)/2. Hence R_−=3/2, R_+=9/2, V_μ(β)=3/log 3 and V_μ(θ)=4/log 3, with every trace equal to (1/4)ord_E(π*D). The residual first moment is infinite. The point-blowup conclusions follow from E. The target backgrounds are genuinely nonclosed; the auxiliary K is closed.\n\nDependency audit: the supplied note graph is acyclic: n1 has no note parents; n2←n1; n3←n1; n4←n1,n2,n3; n5←n1,n2,n3; n6←n2; n7←n1,…,n6. Every listed parent is available and checked; some edges are unnecessary but harmless. At the mathematical level, canonical local arguments use premise 2 and permitted elementary foundations; B additionally uses premises 0,1,3,4; C uses A and transverse integrability; D uses the separated reference; E uses canonical arguments, B and C; F uses only permitted sphere Poisson solvability, Stokes and matrix inequalities; G uses A–F. Premise 5 concerns attribution, not an indispensable calculation dependency.\n\nFresh primary checks confirm the auxiliary product facts in [BEGZ](https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf). Existing definitions and divisorial/modification laws retain [BGL’s credit](https://d-nb.info/1374372846/34). Companion bounded-residual trace constructions, floor ideals, subtraction mechanisms and the local exceptional-curve obstruction also retain their stated credit. Their unrelated coefficient and envelope assertions are outside this proof graph. The historical report’s verdict and repeated short evidence fragments are not adopted as proof; its unresolved full scope remains unresolved.\n\nHarmless wording corrections are already incorporated in the current version: b=0 denotes the identically zero divisorial term, only the target backgrounds are described as nonclosed, d and e are declared, and pure-pullback claims are confined to the stated masses and trace transport. Logarithmic moment divergence refers to the T-cutoff. No substantial repair of an A–G proof was required. This restricted PASS establishes no priority claim, unrestricted S11 completion, general Hermitian strict-type criterion, exceptional-subtraction invariance, or multiplier-ideal pullback theorem.",
  "passages": [
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/0",
      "statement": "On a compact Kahler manifold, the non-pluripolar product of finitely many closed positive (1,1) currents of total degree at most the dimension is well defined and has finite mass.",
      "url": "urn:xean:task",
      "quote": "On a compact Kahler manifold, the non-pluripolar product of finitely many closed positive (1,1) currents of total degree at most the dimension is well defined and has finite mass.",
      "premise": 0
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/1",
      "statement": "On a compact Kahler manifold, two tuples of cohomologous closed positive (1,1) currents with small unbounded locus satisfy the ordinary-singularity-order comparison of the cohomology classes of their non-pluripolar products: if every current of the first tuple is less singular, its product class minus the second product class is pseudoeffective. Small unbounded locus means local boundedness outside a closed locally complete pluripolar set.",
      "url": "urn:xean:task",
      "quote": "On a compact Kahler manifold, two tuples of cohomologous closed positive (1,1) currents with small unbounded locus satisfy the ordinary-singularity-order comparison of the cohomology classes of their non-pluripolar products: if every current of the first tuple is less singular, its product class minus the second product class is pseudoeffective. Small unbounded locus means local boundedness outside a closed locally complete pluripolar set.",
      "premise": 1
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/2",
      "statement": "For a closed pluripolar set A in a complex manifold, a psh function on its complement which is locally bounded above near A extends uniquely to a genuine canonical psh function. Genuine psh functions have positive distributional complex Hessian, and their pullbacks under holomorphic maps are psh, possibly identically minus infinity on a component.",
      "url": "urn:xean:task",
      "quote": "For a closed pluripolar set A in a complex manifold, a psh function on its complement which is locally bounded above near A extends uniquely to a genuine canonical psh function. Genuine psh functions have positive distributional complex Hessian, and their pullbacks under holomorphic maps are psh, possibly identically minus infinity on a component.",
      "premise": 2
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/3",
      "statement": "A well-defined non-pluripolar product of closed positive (1,1)-currents on a complex manifold is closed (BEGZ Theorem 1.8).",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "is closed.",
      "premise": 3
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/4",
      "statement": "Locally, ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ for psh φ; for locally bounded potentials off a closed locally complete pluripolar set, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from its complement (BEGZ §1.2).",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "hddcui = 1{u>−∞} ddcu.",
      "premise": 4
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/5",
      "statement": "Locally, ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ for psh φ; for locally bounded potentials off a closed locally complete pluripolar set, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from its complement (BEGZ §1.2).",
      "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
      "quote": "but the trivial extension",
      "premise": 4
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/6",
      "statement": "On a compact complex manifold with BMP, the lower and upper volumes of a quasi-closed positive (1,1)-current are the finite top-mass infimum and supremum in its dd^c-class and ordinary singularity type. Effective real divisor addition and smooth compact modification pullback preserve both volumes (BGL, Definition 3.1; Proposition 3.3).",
      "url": "https://d-nb.info/1374372846/34",
      "quote": "with equivalent singularities.",
      "premise": 5
    },
    {
      "id": "a2042535-13db-4932-b9e8-bed722d56bc2/7",
      "statement": "On a compact complex manifold with BMP, the lower and upper volumes of a quasi-closed positive (1,1)-current are the finite top-mass infimum and supremum in its dd^c-class and ordinary singularity type. Effective real divisor addition and smooth compact modification pullback preserve both volumes (BGL, Definition 3.1; Proposition 3.3).",
      "url": "https://d-nb.info/1374372846/34",
      "quote": "for any modification π : Y → X we have",
      "premise": 5
    }
  ],
  "premises": [
    "On a compact Kahler manifold, the non-pluripolar product of finitely many closed positive (1,1) currents of total degree at most the dimension is well defined and has finite mass.",
    "On a compact Kahler manifold, two tuples of cohomologous closed positive (1,1) currents with small unbounded locus satisfy the ordinary-singularity-order comparison of the cohomology classes of their non-pluripolar products: if every current of the first tuple is less singular, its product class minus the second product class is pseudoeffective. Small unbounded locus means local boundedness outside a closed locally complete pluripolar set.",
    "For a closed pluripolar set A in a complex manifold, a psh function on its complement which is locally bounded above near A extends uniquely to a genuine canonical psh function. Genuine psh functions have positive distributional complex Hessian, and their pullbacks under holomorphic maps are psh, possibly identically minus infinity on a component.",
    "A well-defined non-pluripolar product of closed positive (1,1)-currents on a complex manifold is closed (BEGZ Theorem 1.8).",
    "Locally, ⟨dd^cφ⟩=1_{φ>−∞}dd^cφ for psh φ; for locally bounded potentials off a closed locally complete pluripolar set, a well-defined non-pluripolar product is the trivial extension of the bounded Bedford–Taylor product from its complement (BEGZ §1.2).",
    "On a compact complex manifold with BMP, the lower and upper volumes of a quasi-closed positive (1,1)-current are the finite top-mass infimum and supremum in its dd^c-class and ordinary singularity type. Effective real divisor addition and smooth compact modification pullback preserve both volumes (BGL, Definition 3.1; Proposition 3.3)."
  ],
  "kind": "codex-report",
  "operationId": "a2042535-13db-4932-b9e8-bed722d56bc2",
  "reportedAt": "2026-10-08T10:31:12.747Z"
}


## Demailly 1992, actual LF lines1--118

Text SHA256: 98781e21d86b8407941e7427297c3c6b7bde63ef415b6709d0f97295c4667217

                         Regularization of closed positive currents
                                 and Intersection Theory

                                                       Jean-Pierre Demailly
                                                       Université de Grenoble I,
                                                       Institut Fourier, BP 74,
                                                       URA 188 du C.N.R.S.,
                                                       F-38402 Saint-Martin d’Hères


Abstract. — Let X be a compact complex manifold and let T be a closed positive
current of bidegree (1, 1) on X. It is shown that T is the weak limit of a sequence
(Tk ) of smooth closed real (1, 1)-currents with small negative part. The negative
part of the Tk ’s can be bounded in terms of the Lelong numbers of T , once a lower
bound for the curvature of the tangent bundle T X is known. Moreover, Kiselman’s
procedure for killing Lelong numbers of a plurisubharmonic function is extended
to manifolds by an alternative method based on Hörmander’s L2 estimates for ∂.
These results are then applied to derive various results concerning divisors or
intersection theory in the context of analytic geometry. Especially, we obtain a
relation between effective and numerically effective divisors on arbitrary compact
manifolds, and we show that every manifold X in the Fujiki class C with nef
tangent bundle is Kähler. If D is an effective divisor in a Kähler manifold, we
also obtain a general self-intersection inequality giving a bound of the degrees of
the constant multiplicity strata of D, in terms of a polynomial in the cohomology
class {D} ∈ H 2 (X, IR).


Contents
1. Introduction and main results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . p. 2
2. Kiselman’s singularity attenuation technique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . p. 6
3. Approximation of psh functions by logarithms of holomorphic functions . . . . . . . . . . . . . . . p. 13
4. Construction of hermitian metrics by L2 techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . p. 17
5. An alternative singularity attenuation technique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . p. 23
6. Application to numerically effective divisors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . p. 31
7. Application to self-intersection inequalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . p. 35
A. Appendix: basic results on L2 estimates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . p. 38
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . p. 40



Key words: Closed positive current, plurisubharmonic function, Lelong number,
L2 estimates for ∂, effective and numerically effective divisors, Fujiki class C,
intersection theory, self-intersection inequality.

A.M.S. Classification: 32J25, 32C30, 32C40


                                                                                    1
                       1. Introduction and main results

        Let X be a compact complex manifold of dimension n. According        to [Le 57],
a current T of bidimension (p, p) that is, of bidegree (n − p, n − p) over X is
said to be positive if T ∧ iα1 ∧ α1 ∧ . . . αp ∧ αp is a positive measure for all smooth
(1, 0)-forms α1 , . . . , αp on X. We say that T is almost positive if there exists
a smooth form v of bidegree (n − p, n − p) such that T + v ≥ 0. Similarly, a
function ϕ on X is said to be almost psh if ϕ is locally equal to the sum of a
psh (plurisubharmonic) function and of a smooth function; then the (1, 1)-current
i∂∂ϕ is almost positive; conversely, if a locally integrable function ϕ is such that
i∂∂ϕ is almost positive, then ϕ is equal a.e. to an almost psh function. If T is
closed and almost positive, the Lelong numbers (or density numbers) ν(T, x) are
well defined, since the negative part always contributes for zero. For every c > 0,
we introduce the Lelong number upperlevel sets
                                       
                              Ec (T ) = x ∈ X ; ν(T, x) ≥ c .
A well-known theorem of Siu [Siu 74] asserts that Ec (T ) is an analytic subset of X.
Our main result is the following approximation-regularization theorem:

        Main Theorem 1.1. — Let T be a closed almost positive (1, 1)-current
and let α be a smooth real (1, 1)-form in the same ∂∂-cohomology class as T , i.e.
T = α + πi ∂∂ψ where ψ is an almost psh function. Let γ be a continuous real
(1, 1)-form such that T ≥ γ. Suppose that OT X (1) is equipped with a smooth
hermitian metric such that the Chern curvature form satisfies
                                            ⋆
                             c OT X (1) + πX   u≥0
with πX : P (T ⋆ X) → X and with some nonnegative smooth (1, 1)-form u on X.
Fix a hermitian metric ω on X. Then for every c > 0, there is a sequence of closed
almost positive (1, 1)-currents Tc,k = α + πi ∂∂ψc,k such that ψc,k is smooth on
X \ Ec (T ) and decreases to ψ as k tends to +∞ (in particular, the current Tc,k is
smooth on X \ Ec (T ) and converges weakly to T on X), and such that
   (i) Tc,k ≥ γ − min{λk , c}u − εk ω    where:
  (ii) λk (x) is a decreasing sequence of continuous functions on X such that
       limk→+∞ λk (x) = ν(T, x) at every point,
 (iii) εk is positive decreasing and limk→+∞ εk = 0,
                                
 (iv) ν(Tc,k , x) = ν(T, x) − c + at every point x ∈ X.

       Here OT X (1) is the tautological line bundle associated to the tangent bundle
T X over the projectivized hyperplane bundle P (T ⋆ X). Observe that the theorem
gives in particular approximants Tc,k which are smooth everywhere on X if we take
c > maxx∈X ν(T, x). Such a regularization result was already proved in [De 82]
under somewhat stronger curvature hypotheses (namely, X has a Kähler metric
for which the induced metric on OT X (1) satisfies the above curvature assumption).
Properties (i) and (ii) show that the presence of positive Lelong numbers is

                                           2
an obstruction to smoothing when no loss of positivity is admitted; the old
regularization theorem of Richberg [Ri 68] precisely solved the special case when
the potential ψ is finite and continuous (the Lelong numbers are then always zero).
For a general choice of the constant c, the inequalities (iv) tell us that the procedure
kills all Lelong numbers that are ≤ c and shifts all others by −c. Thus we obtain an
analogue over arbitrary manifolds of Kiselman’s procedure [Ki 78] for killing Lelong
numbers (here we assumed X compact only for the sake of simplicity; our method
can be easily extended to noncompact manifolds, but uniform estimates only hold
on relatively compact subsets). Unfortunately, Kiselman’s method, which depends
on the Legendre transformation for psh functions, only works with the stronger
curvature assumption c(T X) + u ⊗ IdT X ≥ 0 in the sense of Griffiths. Since
this method is simpler and more natural, we first explain it in Section 2. With
the OT X (1) lower bound assumption (which is much better from the point of
view of algebraic geometry), we have to use more complicated arguments based
on a combination of different types of L2 estimates for ∂, due chronologically to
Hörmander [Hö 66], Skoda [Sk 72b] and Ohsawa-Takegoshi [OT 87, Oh 88]. The
proof occupies Sections 3,4,5. Hörmander’s estimates are used in Section 4 to
construct hermitian metrics on high symmetric powers S m T X and S m T ⋆ X, when
starting from a metric on OT X (1). The Ohsawa-Takegoshi estimates are needed to
approximate psh functions locally by logarithms of holomorphic functions, while
Skoda’s L2 estimates are used in the gluing process, to compare the size of high
order jets of functions produced in different coordinate patches.
       The Main Theorem can be applied in many ways to get interesting results


## Demailly 1992, actual LF lines275--640

Text SHA256: 98781e21d86b8407941e7427297c3c6b7bde63ef415b6709d0f97295c4667217

        Now, let X be a compact n-dimensional complex manifold and let T be a
closed almost positive current of bidegree (1, 1) on X. We select a smooth closed
(1, 1)-form α representing the same ∂∂-cohomology class as T and an almost psh
function ψ on X such that T = α + πi ∂∂ψ. Such a decomposition exists even
when X is non-Kähler, since we can always find an open coveringP (Uj ) of X such
that T = πi ∂∂ψj over Uj , and construct a global function ψ =     θj ψj by means
of a partition of unity (θj ) subordinate to Uj (observe that ψ − ψk is smooth
on Uk because all differences ψj − ψk are smooth in the intersections Uj ∩ Uk ).
By replacing T with T − α and γ with γ − α in the Main Theorem, we can
suppose without loss of generality that {T } = 0, i.e. that T = πi ∂∂ψ with an
almost psh function ψ on X. Thus we have to devise a singularity attenuation
technique for almost psh functions. We first describe Kiselman’s method [Ki 78].
An alternative method working under slightly more general hypotheses will be
explained in section 5.
      Local procedure. — To begin with, let ϕ be a psh function on an open
set U ⊂ Cn . Suppose that the trivial vector bundle E = U × Cn is equipped with a
smooth hermitian metric ||ξ||z for ξ ∈ {z} × Cn (later on, the hermitian structure
of U × Cn will come from a trivialization of T X`| U ). For w ∈ C, we set
(2.2)                     Φ∞ (z, w) = sup ϕ(z + ew ξ).
                                       ||ξ||z ≤1

Clearly Φ∞ (z, w) depends only on the real part Re w and is defined on the open
set Ω of points (z, w) ∈ U × C such that Re w < log dz (z, ∂U ), where dz denotes
euclidean distance with respect to || ||z . Moreover Φ∞ (z, w) is a convex increasing
function of Re w by the well known properties of plurisubharmonic functions. Next,
for (z, w) ∈ Ω, we introduce the Legendre transform
(2.3)               Φc (z, w) = inf Φ∞ (z, w + t) − ct,   c > 0.
                               t≤0


                                          6
It is easy to see that the family (Φc ) is increasing in c and that
(2.4)                 lim Φc (z, w) = ϕ(z),     lim Φc = Φ∞ .
                      c→0                      c→+∞

When ||ξ||z is taken to be a constant metric, we know by Kiselman [Ki 78] that
Φ∞ and Φc are plurisubharmonic functions of the pair (z, w), and that the Lelong
numbers of Φc (•, w) are given by
                                             
(2.5)             ν Φc (•, w), z = ν(ϕ, z) − c + , ∀(z, w) ∈ Ω.
In general, Φ∞ is continuous on Ω and its right derivative ∂Φ∞ (z, w)/∂Re w+
is upper semicontinuous; indeed,
                                   this partial derivative is the decreasing limit
of Φ∞ (z, w + t) − Φ∞ (z, w) /t as t ↓ 0+ . It follows that Φc is continuous on
Ω \ (Ec (ϕ) × C): in fact, we have ν(ϕ, z) = limt→−∞ ∂Φ∞ (z, t)/∂t+ < c on every
compact set K ⊂ Ω \ (Ec (ϕ) × C), so by the upper semicontinuity there is a
constant t0 such that ∂Φ∞ (z, w + t)/∂t+ < c for (z, w) ∈ K and t < t0 . Therefore
                    Φc (z, w) = inf Φ∞ (z, w + t) − ct        on K,
                                t0 ≤t≤0

and this infimum with compact range is continuous. Our first goal is to investigate
the plurisubharmonicity of Φc when ||ξ||z is a variable hermitian metric.

      Proposition 2.6. — Suppose that the Chern curvature of the hermitian
metric on E = U × Cn satisfies c(E) + u ⊗ IdE ≥ 0 in the sense of Griffiths, for
some nonnegative (1, 1)-form u on X. Then
   (i) For all v ≥ 0, we have
                                                       ∂Φ∞ (z, w) o
                    Φc (z, w − v) ≥ Φc (z, w) − min               , c v;
                                                         ∂Re w−

  (ii) For (ζ, η) ∈ T U × C and c ∈ ]0, +∞], the Hessian of Φc satisfies
                    i                             n ∂Φ (z, w) o
                                                      ∞
                      ∂∂(Φc )(z,w) (ζ, η) ≥ − min            , c uz (ζ).
                    π                                ∂Re w+


        Proof. — (i) For v ≥ 0 and t ≤ 0, we have
                                                         ∂Φ∞ (z, w + t)
                Φ∞ (z, w + t − v) ≥ Φ∞ (z, w + t) − v
                                                           ∂Re w−
by convexity of Φ∞ (z, w) in Re w. As ∂Φ∞ (z, w)/∂Re w− is increasing in Re w,
the infimum of both sides minus ct gives
                                                      ∂Φ∞ (z, w)
                      Φc (z, w − v) ≥ Φc (z, w) − v              .
                                                       ∂Re w−
On the other hand, the change of variables t = t′ + v yields
           Φc (z, w − v) ≥ ′inf Φ∞ (z, w + t′ ) − c(t′ + v) ≥ Φc (z, w) − cv
                            t ≤−v

and (i) follows. The proof of (ii) requires the following simple lemma.

                                          7
       Lemma 2.7. — Let z0 ∈ U be fixed and let v be the hermitian quadratic
function with constant Hessian πi ∂∂v = uz0 . Then there is a holomorphic n × n
matrix g(z) near z0 such that g(z0 ) = Id and
                                                                            3
                           ||g(z) · ξ||z ≤ ||ξ||z0 ev(z−z0 )+O(|z−z0 | ) .


         Proof. — Without loss of generality, we may suppose that z0 = 0 and that
||ξ||z0 is given by the unit hermitian matrix (otherwise take any orthonormal basis
(eλ ) as the new basis of Cn ). We have a Taylor expansion
                    X              X
          ||ξ||2z =      |ξλ |2 +       (ajλµ zj + ajµλ z j )ξλ ξ µ + O(|z|2 |ξ|2 )
                1≤λ≤n               1≤j,λ,µ≤n

at first order. We can get rid of the first order terms by setting
                                           X
                         g1 (z) · ξ = ξ −      ajλµ zj ξλ eµ .
                                                   j,λ,µ
                                                          P
A simple calculation shows indeed that ||g1 (z) · ξ||2z =    |ξλ |2 + O(|z|2 |ξ|2 ). We
then look at the second order terms in the Taylor expansion
                              X          X
           ||g1 (z) · ξ||2z =   |ξλ |2 +   (ajkλµ zj zk + ajkµλ z j z k )ξλ ξ µ
                                λ              j,k,λ,µ
                                                X
                                           +             bjkλµ zj z k ξλ ξ µ + O(|z|3 |ξ|2 )
                                               j,k,λ,µ

and kill the coefficients ajkλµ by setting
                                                       X
                      g(z) · ξ = g1 (z) · ξ −                 ajkλµ zj zk ξλ eµ .
                                                    j,k,λ,µ

The remaining coefficients (bjkλµ ) cannot be killed and are related to the curvature
tensor c(E) by cjkλµ = − π1 bjkλµ . If we write vjk = ∂ 2 v/∂zj ∂z k (0), we have
          P
u(0) = πi    vjk dzj ∧ dz k and the curvature assumption c(E) + u ⊗ IdE ≥ 0 at the
origin implies
                   X                           X            X
                        −bjkλµ zj z k ξλ ξ µ +   vjk zj z k   |ξλ |2 ≥ 0.
                 j,k,λ,µ                             j,k               λ

Therefore we get
                               X                X
            ||g(z) · ξ||2z =        |ξλ |2 +             bjkλµ zj z k ξλ ξ µ + O(|z|3 |ξ|2 )
                                λ              j,k,λ,µ
                                                           
                            ≤ ||ξ||20   1 + v(z) + O(|z|3 ) .
The asserted inequality 2.7 is equivalent to this.

      Proof of 2.6 (ii). — Fix (z0 , w0 ) ∈ Ω and an arbitrary quadratic function
v such that πi ∂∂v > uz0 . Then Lemma 2.7 yields an invertible matrix g(z) such

                                                   8
that ||g(z) · ξ||z ≤ ||ξ||z0 ev(z−z0 ) near z0 . A change of variable ξ 7→ g(z) · ξ in (2.2)
implies
            Φ∞ (z, w) =        sup          ϕ(z + ew g(z) · ξ)
                           ||g(z)·ξ||z ≤1

                       ≥          sup            ϕ(z + ew g(z) · ξ)       near (z0 , w0 ),
                           ||ξ||z0 ≤e−v(z−z0 )

with the inequality being an equality for z = z0 . The function
                           h(z, w) =          sup ϕ(z + ew g(z) · ξ)
                                            ||ξ||z0 ≤1

is plurisubharmonic and, if hc is its Legendre transform, we obtain successively
                                                        
                       Φ∞ (z, w) ≥ h z, w − v(z − z0 ) ,
                                                         
                         Φc (z, w) ≥ hc z, w − v(z − z0 )
near (z0 , w0 ), with equality for z = z0 . For small (ζ, η) ∈ T U × C, we combine
this with the mean value inequality to get
    Z 2π                                   Z 2π
                                      dθ                                         dθ
          Φc (z0 + eiθ ζ, w0 + eiθ η)    ≥      hc z0 + eiθ ζ, w0 + eiθ η − v(ζ)
     0                                2π    0                                     2π
                                                                                 
                                         ≥ hc z0 , w0 − v(ζ) = Φc z0 , w0 − v(ζ) .
This inequality is still valid at points (z, w) near (z0 , w0 ), provided that uz < πi ∂∂v
and that |ζ|2 + |η|2 < rz,w2
                               is small enough. By 2.6 (i), we get the inequality
       Z 2π                                                   n ∂Φ (z, w) o
                                      dθ                           ∞
            Φc (z + eiθ ζ, w + eiθ η)    ≥ Φc (z, w) − min                  , c v(ζ)
        0                             2π                          ∂Re w+
near (z0 , w0 ). For A > ∂Φ∞ (z0 , w0 )/∂Re w+ , we still have A > ∂Φ∞ (z, w)/∂Re w+
in a neighborhood by the upper semicontinuity, and we conclude that the function
Φc (z, w) + min{A, c}v(z) satisfies the mean value inequality near (z0 , w0 ). Hence
Φc (z, w) + min{A, c}v(z) is psh near (z0 , w0 ) and (ii) is proved.
        Gluing process. — The next step is to describe a gluing process for the
construction of global regularizations of almost psh functions. We suppose that
X is equipped with a hermitian metric ω such that its Chern curvature satisfies
c(T X) + u ⊗ IdT X ≥ 0 in the sense of Griffiths, where u is a smooth semipositive
(1, 1)-form on X. Let T = πi ∂∂ψ where ψ is an almost psh function on X, and
let γ be a real continuous (1, 1)-form such that T ≥ γ. We select a finite covering
(Wν ) of X with open coordinate charts. Given δ > 0, we take in each Wν a
maximal family of points with (coordinate) distance to the boundary ≥ 3δ and
mutual distance ≥ δ. In this way, we get for δ > 0 small a finite covering of
X by open balls Uj′ of radius δ, such that the concentric ball Uj of radius 2δ is
relatively compact in the corresponding chart Wν . Let τj : Uj −→ B(aj , 2δ) be the
isomorphism given by the coordinates of Wν . Let ε(δ) be a modulus of continuity
for γ on the sets Uj , such that limδ→0 ε(δ) = 0 and γx − γx′ ≤ 12 ε(δ) ωx for all
x, x′ ∈ Uj . We denote by γj the (1, 1)-form with constant coefficients on B(aj , 2δ)
such that τj⋆ γj coincides with γ − ε(δ) ω at τj−1 (aj ). Then we have
(2.8)                        0 ≤ γ − τj⋆ γj ≤ 2ε(δ) ω            on Uj′

                                                     9
for δ > 0 small. We set ψj = ψ ◦ τj−1 on B(aj , 2δ) and let e    γj be the homogeneous
quadratic function in z − aj such that πi ∂∂e    γj = γj on B(aj , 2δ). Finally, we set
(2.9 a)                  ϕj (z) = ψj (z) − γ
                                           ej (z) on B(aj , 2δ).
Then ϕj is plurisubharmonic, since
                       i
                         ∂∂(ϕj ◦ τj ) = T − τj⋆ γj ≥ γ − τj⋆ γj ≥ 0.
                      π
Let ||ξ||j,z be the metric induced by ω at a point z ∈ B(aj , 2δ) in the trivialization
dτj : T X`| Uj → B(aj , 2δ) × Cn . We combine (2.2) and (2.3) to define functions
                                                                        √
(2.9 b) Φj,c (z, w) = inf       sup ϕj (z + ew+t ξ) − ct , z ∈ B(aj , 2 δ),
                               t≤0       ||ξ||j,z ≤1
                                                                                              √
                                    γj (z) − δ|z − aj |2 ,
(2.9 c) Ψj,c (z, w) = Φj,c (z, w) + e                                               z ∈ B(aj , 2 δ),

(2.9 d)    Ψc (x, w) = sup Ψj,c (τj (x), w),                      x ∈ X,
                               Uj′′ ∋x
                            √
where Uj′′ = τj−1 (B(aj , 2 δ)). Note that Uj′ ⊂⊂ Uj′′ ⊂⊂ Uj by construction
and that there
           √       exists w0 = log δ − C1 < 0 such that z + ew+t ξ ∈ B(aj , 2δ) when
z ∈ B(aj , 2 δ) and Re w < w0 . Then Ψc (x, w) is well defined on X×{Re w < w0 }.
We have to check that the sup used in the definition of Ψc does not create
discontinuities when x passes through a boundary ∂Uj′′ . For this, we must compare
Ψk,c (z, w) and Ψj,c (τjk (z), w) for z ∈ τk (Uj′′ ∩ Uk′′ ), where τjk = τj ◦ τk−1 . By
(2.9 a,b) there is a uniform estimate
                                                          
          Φj,c (z, w) = inf     sup ψj (z + ew+t ξ) − ct − γ   ej (z) + O(|ew |),
                               t≤0       ||ξ||j,z ≤1

therefore (2.9 c) gives
                                                                           
(2.10)     Ψj,c (z, w) = inf                 sup        ψj (z + ew+t ξ) − ct − δ|z − aj |2 + O(|ew |).
                                t≤0       ||ξ||j,z ≤1

The error terms O(|ew |) come from the variation of the quadratic function γ
                                                                           ej (z)
when z is replaced by z + ew+t ξ. This variation is bounded by C2 |ew | with a
constant C2 independent of δ.
         When we make the substitution z 7→ τjk (z), the trivialization of the tangent
bundle is submitted to a corresponding transformation ξ 7→ dτjk (z)·ξ, in particular
||ξ||k,z = ||dτjk (z) · ξ||j,τjk (z) . As ψk = ψj ◦ τjk , we get
(2.11k )             sup         ψk (z + ew+t ξ) =             sup        ψj ◦ τjk (z + ew+t ξ),
                  ||ξ||k,z ≤1                               ||ξ||k,z ≤1
to be compared with
                                                                                                             
(2.11j )    sup    ψj (τjk (z) + ew+t ξ) =                          sup        ψj τjk (z) + ew+t dτjk (z) · ξ .
           ||ξ||j,τjk (z) ≤1                                     ||ξ||k,z ≤1

However τjk (z + ξ) − [τjk (z) + dτjk (z) · ξ] = O(|ξ|2 ), thus if Bj (z, r) denotes the
euclidean ball of center z and radius r with respect to || ||j,z , there is a constant
C3 > 0 such that
           Bj (τjk (z), r − C3 r2 ) ⊂ τjk (Bk (z, r)) ⊂ Bj (τjk (z), r + C3 r2 )

                                                            10
for all j, k and r < r0 . By taking r = |ew+t |, these inclusions show that
                                                                                      
  |(2.11j ) − (2.11k )| ≤ Ψj,∞ τjk (z), log(r + C3 r2 ) − Ψj,∞ τjk (z), log(r − C3 r2 )
                                                              
                        ≤ C4 log(r + C3 r2 ) − log(r − C3 r2 ) ≤ C5 |ew+t |,
because ∂Ψj,∞ (z, w)/∂w+ is uniformly bounded on Uj × ] − ∞, w0 [ (the bound is
independent of δ). Therefore (2.10) implies
         Ψj,c (τjk (z), w) − Ψk,c (z, w) = δ(|z − ak |2 − |τjk (z) − aj |2 ) + O(|ew |).
Now, if x ∈ X, there exists by construction an index k such that x ∈ Uk′ , i.e.
z = τk (x) ∈ B(ak , δ). If x ∈ Uj′′ tends to a point in the boundary ∂Uj′′ , then
                        √
|τjk (z) − aj | tends to 2 δ and
  Ψj,c (τjk (z), w) − Ψk,c (z, w) −→ δ(|z − ak |2 − 2δ 2 ) + O(|ew |) ≤ −δ 3 + O(|ew |).
This implies that formula (2.9 d) does not involve values of Ψj,c near ∂Uj′′ when
w ≤ w1 = 3 log δ − C6 . In particular Ψc is continuous on X \ Ec (T ), since each
function Ψj,c has this property. Also, by Kiselman’s result 2.5, we get
                                                                       
(2.12)    ν Ψc (•, w), x = ν Φj,c (•, w), x = ν(ϕ, x) − c + = ν(ψ, x) − c +
when x ∈ Uj′ . Clearly Ψc (x, w) is convex and increasing in w, for each function
Φj,c has this property. Finally, let x ∈ X with x ∈ Uk′′ , let z = τk (x) and let
vk be a positive quadratic function on B(ak , 2δ) with πi ∂∂vk > (τk−1 )⋆ ux . As
τjk (z + eiθ ζ) = τjk (z) + eiθ dτjk (z) · ζ + O(|ζ|2 ), the definition of Φj,c , Ψj,c in
(2.9 b,c) and the mean value argument used in the proof of 2.6 imply
 Z 2π
                                        dθ                           
       Φj,c τjk (z + eiθ ζ), w + eiθ η      ≥ Φj,c τjk (z), w − vk (ζ) ,
   0                                     2π
 Z 2π
                                        dθ                           
       Ψj,c τjk (z + eiθ ζ), w + eiθ η      ≥ Φj,c τjk (z), w − vk (ζ)
  0                                      2π
(2.13)       +γ                 γj (dτjk (z) · ζ) − O(|ζ|3 ) − δ|τjk (z) − aj |2 − O(δ)|ζ|2
              ej (τjk (z)) + i∂∂e
for every j such that Uj′′ ∋ x ; here we use the fact that for a suitable quadratic
function vj on B(aj , x) approximating closely (τj−1 )⋆ ux (more accurately than vk
did), we have                                         
                        vj eiθ dτjk (z) · ζ + O(|ζ|2 ) ≤ vk (ζ)
for ζ small. Since πi ∂∂e γj ◦ τj = τj⋆ γj ≥ γ − 2ε(δ)ω by construction, we find
                   i                                                    
                       γj (dτjk (z) · ζ) ≥ (γx − 2ε(δ)ωx ) dτk−1 (z) · ζ .
                     ∂∂e
                   π
When we take the supremum over j in (2.13) and use definition (2.9 d), we get
Z 2π
                                   dθ                                                  
     Ψc τk−1 (z +eiθ ζ), w+eiθ η         ≥ Ψc (x, w−vk (ζ) +π(γx − εe(δ)ωx ) dτk−1 (z)·ζ
 0                                   2π
with εe(δ) = 2ε(δ) + O(δ). By the arguments already explained in the proof of
2.6 (ii), we infer
          i                               n ∂Ψ (x, w) o
                                               ∞
(2.14)      ∂∂(Ψc )(x,w) (ξ, η) ≥ − min                , c ux (ξ) + γx (ξ) − εe(δ)ωx (ξ)
          π                                  ∂Re w+

                                               11
when w < w1 (δ) = 3 log δ − C6 . Finally, we obtain the sequence ψc,k needed in
the Main Theorem by setting
                                            1
                   ψc,k (x) = Ψc (x, wk ) +     with δ = δk := 2−k
                                            k
and with a rapidly decreasing sequence wk → −∞. The covering (Uj ) changes
with the parameter δ when δ tends to 0, so it is not a priori clear that ψc,k is
decreasing; this is the reason why we introduced the additional term 1/k ; the
change of covering between ψc,k and ψc,k+1 can only modify our functions by
terms of order of magnitude δk2 = 2−2k (coming from the change of quadratic
functions) and |ewk | (coming from the change of chart in the definition of Φj,c ).
These terms are negligible with respect to 1/k − 1/(k + 1) if we take for instance
wk ≤ −3k ≤ 4 log δk . Property (2.12) shows that ν(ψc,k , x) = (ν(ψ, x) − c)+ at
every point. Moreover, (2.14) implies
             i                     n ∂Ψ (x, w ) o
                                          ∞    k
               ∂∂ψc,k (x) ≥ − min                 , c ux + γx − εe(δk )ωx .
             π                          ∂Re w+
Since ∂Ψ∞ (x, w)/∂Re w+ is upper semi-continuous and converges to ν( πi ∂∂ψ, x)
for each δ fixed, the following claim is easy to show: given any strictly decreasing
sequence of continuous functions λk ≥ 0 on X such that lim λk (x) = ν( πi ∂∂ψ, x),
there is a choice of wk such that ∂Ψ∞ (x, wk )/∂Re w+ ≤ λk (x) for δ = δk .
Therefore the currents Tc,k = πi ∂∂ψc,k satisfy all properties 1.1 (i)-(iv).
        Our construction only showed a priori that Tc,k is continuous on X \ Ec (T ).
In fact Tc,k can be made smooth on X \Ec (T ) by Richberg’s approximation theorem
                                                                      ′
[Ri 68]: by Lemma 2.15 below, there are smooth approximants ψc,k          of ψc,k on
                     ′
X \ Ec (T ) with |ψc,k  − ψc,k | < 2−k and with an arbitrary small loss of positivity
on the continuous lower bound of the Hessian, say a loss ≤ 2−k ω. It is then clear
        ′
that ψc,k   extends to an almost psh function on X and that Tc,k  ′
                                                                     = α + πi ∂∂ψc,k
                                                                                  ′

satisfies essentially the same estimates as Tc,k . Theorem 1.1 is thus proved under
the more restrictive condition that c(T X) + u ⊗ IdT X ≥ 0 in the sense of Griffiths.

        Lemma 2.15 (Richberg [Ri 68], Greene-Wu [GW 75]). — Let ψ be a quasi
psh function on a complex manifold M such that i∂∂ψ ≥ γ where γ is a continuous
(1, 1)-form. For any hermitian metric ω and any continuous function δ > 0 on M ,
there is a smooth function ψ ′ such that ψ < ψ ′ < ψ + δ and i∂∂ψ ≥ γ − δ ω on M .

       Sketch of proof. — Take a locally finite covering (Bj ) of M by open balls
and take a convolution ψ ⋆ ρεj by a regularizing kernel on a neighborhood of
each B j . Let z j be a local coordinate identifying Bj to the ball B(0, rj ). The
smoothing process consists in gluing the functions ψ ⋆ ρεj (z) + ηj (rj2 − |z j |2 ) by
taking the maximum with respect to all overlapping balls at the given point z.
A smooth function can be obtained by means of regularized max functions. For
a suitable choice of εj ≪ inf Bk ∩Bj 6=∅ ηk , the boundary values of the functions do
not contribute to the maximum. The estimates are then clearly satisfied if the εj ’s
and ηj ’s are small enough.



                                          12
           3. Approximation of plurisubharmonic functions by
                  logarithms of holomorphic functions

       Let T be a closed almost positive current of bidegree (1, 1) on a compact
complex manifold X. We write T = α + πi ∂∂ψ with an almost psh function ψ
on X. The first step in the proof of Th. 1.1 consists in showing that ψ can be


## Demailly 1992, actual LF lines1638--1740

Text SHA256: 98781e21d86b8407941e7427297c3c6b7bde63ef415b6709d0f97295c4667217

                       mpc + 1 2n         1                          
             ν(ψ, x) −         −     ≤        ν(wj , x) ≤ ν(ψ, x) − c +
                          mp      m     2mp

                                               29
and (iv) is proved.

    Proof of Theorem 1.1. — We use Lemma P      3.5 to glue the functions wj of
Lemma 5.12 into a single function w = log θj2 ewj , by means of cut-off functions
                                                  (4)
θj such that θj = 1 on Uj′ and Supp θj ⊂ Uj . We then have a loss of positivity
−C11 (δ)ω in the Hessian of w with respect to 5.12 (i). Since the differences |wj −wk |
                                               (4)
are bounded, we get ν(w, x) = ν(wj , x) on Uj . Also, the obvious inequalities

                 wj (x) ≤ w(x) ≤ sup wk (x) + log N (δ)             on Uj′
                                     (4)
                                    Uk ∋x

                                                              (4)
(with N (δ) = maximal number of overlapping sets Uk ) show that 5.12 (ii) is
                                                                   1
essentially preserved for p ≫ log N (δ). Therefore Ψc,δ,m,p := 2mp   w satisfies on X
the global estimates
             i                             p
(5.13 i)       ∂∂Ψc,δ,m,p ≥ γ − c u − 2C6 ε(δ) ω,
             π
                                                       | log r|     
(5.13 ii)   ψ(x) ≤ Ψc,δ,m,p(x) ≤ sup ψ(z) + C7                   +r+δ ,
                                   |z−x|<r                 m
                            2n + 1                                   
(5.13 iv)      ν(ψ, x) − c −            ≤ ν(Ψc,δ,m,p , x) ≤ ν(ψ, x) − c +
                               m      +

when p ≫ m ≫ 1/δ. Moreover Ψc,δ,m,p has the same singularities as the logarithm
of a sum of squares of holomorphic functions, thus Ψc,δ,m,p is smooth on X \ Ec (ψ).
        In order to complete the proof of Theorem 1.1, we still have to organize
the functions Ψc,δ,m,p into a decreasing sequence (ψc,k )k≥1 converging to ψ and
satisfying properties 1.1 (i,ii) (which are stronger than inequality (5.13 i)). The
arguments are almost purely formal. We first note that for given δ, m, p there
is a choice of (η) which works for all c′ ∈ [0, c] and q ′ = ⌈mpc′ ⌉ ≤ q. Then
by construction, we see that wj , w and Ψc′ ,δ,m,p are increasing in c′ . Fix a
strictly decreasing sequence of continuous functions λk > 0 on X such that
limk→+∞ λk (x) = ν(ψ, x) at every point. We select inductively a sequence δℓ ↓ 0
and strictly increasing sequences (mℓ ), (pℓ ) such that the above estimates (5.13)
are satisfied and such that for all k = 1, . . . , ℓ
                                             1                           1
(5.14)   Ψ(1−k/(ℓ+1))c,δℓ+1 ,mℓ+1 ,pℓ+1 +       < Ψ(1−k/ℓ)c,δℓ ,mℓ ,pℓ +     on Ak,ℓ ,
                                            ℓ+1                          ℓ
                                    
where Ak,ℓ := λℓ−1 [0, (1 − k/ℓ)c] . This is actually possible by Dini’s lemma,
because Ak,ℓ is a compact set contained in X \ E(1−k/ℓ)c (ψ): thus, the right hand
side of (5.14) is smooth and ≥ ψ + 1/ℓ on Akℓ , whereas the left hand side converges
to the smaller limit ψ + 1/(ℓ + 1) as δℓ+1 → 0 and mℓ+1 , pℓ+1 → +∞. For a reason
that will be apparent later, we also take mℓ ≥ (2n + 1)ℓ/c. We claim that the
(upper semi-continuous) regularized upper envelope
                                                         1 ⋆
                        ψc,k = sup Ψ(1−k/ℓ)c,δℓ ,mℓ ,pℓ +
                                 ℓ≥k                      ℓ

                                             30
has all required properties. In fact, it is clear that the sequence (ψc,k )k≥1 is
decreasing and (5.13 ii) shows that it converges to ψ. Now, we have by definition
ψc,k ≥ Ψ(1−k/ℓ)c,δℓ ,mℓ ,pℓ and therefore
                                                                          
          ν(ψc,k , x) ≤ ν(Ψ(1−k/ℓ)c,δℓ ,mℓ ,pℓ , x) ≤ ν(ψ, x) − (1 − k/ℓ)c +
for all ℓ ≥ k. This implies ν(ψc,k , x) ≤ (ν(ψ, x) − c)+ when ℓ tends to +∞. On
the other hand, all terms in the supremum have Lelong numbers at least equal to
                                    k     2n + 1
                    ν(ψ, x) − 1 −       c−         ≥ ν(ψ, x) − c
                                     ℓ       mℓ
thanks to our choice (2n + 1)/mℓ ≤ c/ℓ. By standard arguments, we get therefore
the converse inequality ν(ψc,k , x) ≥ ν(ψ, x)− c. The monotonicity condition (5.14)
implies
                                                     1
                   ψc,k = sup Ψ(1−k/ℓ)c,δℓ ,mℓ ,pℓ +     on Ak,s
                          k≤ℓ≤s                      ℓ
                                                S
(note that Ak,ℓ is increasing in ℓ and that ℓ Ak,ℓ = X \ Ec (ψ) ). Therefore
the Hessian of ψc,k satisfies the weakest bound valid for each term in this finite
envelope, namely
    i                                   p
      ∂∂ψc,k ≥ γ − (1 − k/s)c u − 2C6 ε(δk )ω on {λs < (1 − k/s)c} ⊂ A◦k,s
    π
thanks to (5.13 i). If x ∈ X with λk (x) < c is given, we select the smallest s > k
such that λs (x) < (1 − k/s)c. Then (1 − k/(s − 1))c ≤ λs−1 (x) and we see that
               (1 − k/s)c ≤ λs−1 (x) + kc/s(s − 1) < λk (x) + c/k.
We infer from this
            i                                p
              ∂∂ψc,k ≥ γ − (λk + c/k)u − 2C6 ε(δk )ω on {λk < c}.
            π
                                                                        p
However, all terms in ψc,k have a Hessian bounded below by γ − c u − 2C6 ε(δk )ω,
so we get in all cases
         i                                  p               
           ∂∂ψc,k ≥ γ − min{λk , c}u − 2C6 ε(δk ) + O(1/k) ω on X.
         π                                                               S
Finally, as ψc,k is a finite supremum on each set Ak,ℓ in X \ Ec (ψ) = ℓ Ak,ℓ ,
we conclude that ψc,k is continuous on X \ Ec (ψ). Richberg’s theorem 2.15 can
be applied to make ψc,k smooth on X \ Ec (ψ). Theorem 1.1 is thus completely
proved.

       Remark 5.15. — By a further application of Proposition 3.7 to each func-


## Demailly canonical extension, Lelong trace and growth, actual LF lines2055--2190

Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

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
                            |wj |⩽1

are upper semicontinuous, satisfy the mean value inequality, and depend only on Re zj ∈
]0, log Rj [. Therefore µ     f are convex. Cor. 5.14 follows from the equalities
                        e and M
                                                      e(log r1 , . . . , log rn ),
                            µ(u ; r1 , . . . , rn ) = µ
                                                     e
                           m(u ; r1 , . . . , rn ) = m(log r1 , . . . , log rn ).                
42                     Chapter I. Complex Differential Calculus and Pseudoconvexity

§ 5.D. Pluriharmonic Functions
   Pluriharmonic functions are the counterpart of harmonic functions in the case of
functions of complex variables:

(5.15) Definition. A function u is said to be pluriharmonic if u and −u are plurisub-
harmonic.

   A pluriharmonic function is harmonic (in particular smooth) in any C-analytic coor-
dinate system, and is characterized by the condition Hu = 0, i.e. d′ d′′ u = 0 or

                             ∂ 2 u/∂zj ∂z k = 0     for all j, k.

If f ∈ O(X), it follows that the functions Re f, Im f are pluriharmonic. Conversely:
                                                     1
(5.16) Theorem. If the De Rham cohomology group HDR     (X, R) is zero, every pluri-
harmonic function u on X can be written u = Re f where f is a holomorphic function
on X.
                      1
Proof. By hypothesis HDR (X, R) = 0, u ∈ C∞ (X) and d(d′ u) = d′′ d′ u = 0, hence there
exists g ∈ C (X) such that dg = d′ u. Then dg is of type (1, 0), i.e. g ∈ O(X) and
            ∞


              d(u − 2 Re g) = d(u − g − g) = (d′ u − dg) + (d′′ u − dg) = 0.

Therefore u = Re(2g + C), where C is a locally constant function.                      

§ 5.E. Global Regularization of Plurisubharmonic Functions
    We now study a very efficient regularization and patching procedure for continuous


## Demailly canonical extension, Lelong trace and growth, actual LF lines2300--2355

Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

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
Proof. If Ω r A (resp. X r A) is a disjoint union Ω1 ∪ Ω2 of non empty open subsets, the
function defined by f ≡ 0 on Ω1 , f ≡ 1 on Ω2 would have a harmonic (resp. holomorphic)
extension through A, a contradiction.                                                 



## Demailly canonical extension, Lelong trace and growth, actual LF lines14896--14934

Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

    Our goal here is to extend the Lelong-Poincaré equation III-2.15 to any meromorphic
section of a holomorphic line bundle.

(13.1) Definition. A meromorphic section of a bundle E → X is a section s defined
on an open dense subset of X, such that for every trivialization θα : E↾Vα → Vα × Cr the
components of σ α = θα (s) are meromorphic functions on Vα .

    Let E be a hermitian line bundle, s a meromorphic section which does not vanish
on any component of X and σ = θ(s) the corresponding meromorphic function in a
trivialization θ : E↾Ω → Ω × C. The divisor of s is the current onPX defined by div s↾Ω =
div σ for all trivializing open sets Ω. One can write div s =       mj Zj , where the sets
Zj are the irreducible components of the sets of zeroes and poles of s (cf. § II-5). The
Lelong-Poincaré equation (II-5.32) gives
                                 i ′ ′′          X
                                   d d log |σ| =   mj [Zj ],
                                 π
and from the equalities |s|2 = |σ|2 e−ϕ and d′ d′′ ϕ = Θ(E) we get
                                               X
(13.2)                   id′ d′′ log |s|2 = 2π   mj [Zj ] − i Θ(E).

This equality can be viewed as a complex analogue of (9.9) (except that here the hyper-
surfaces Zj are not necessarily smooth). In particular, if s is a non vanishing holomorphic
section of E↾Ω , we have

(13.3)                        i Θ(E) = −id′ d′′ log |s|2    on Ω.

(13.4) Theorem. Let E → X be a line bundle and let s be a meromorphic
                                                               P           section of E
which does not vanish identically on any component of X. If      mj Zj is the divisor of
s, then                            nX           o
                         c1 (E)R =      mj [Zj ] ∈ H 2 (X, R).

Proof. Apply Formula (13.2) and Th. 9.5, and observe that the bidimension (1, 1)-current
id′ d′′ log |s|2 = d id′′ log |s|2 has zero cohomology class.                              
                                  P
(13.5) Example. If ∆ =              mj Zj is an arbitrary divisor on X, we associate to ∆ the
sheaf O(∆) of germs of meromorphic functions f such that div(f ) + ∆ ⩾ 0. Let (Vα ) be
a covering of X and uα a meromorphic function on Vα such that div(uα ) = ∆ on Vα .
Then O(∆)↾Vα = u−1     α O, thus O(∆) is a locally free O-module of rank 1. This sheaf can be


## Demailly canonical extension, Lelong trace and growth, actual LF lines8546--8745

Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

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
                              Z
                   ν(T, ϕ) =           T ∧ (ddc ϕ)p = lim ν(T, ϕ, r).
                                  S(−∞)                   r→−∞


The number ν(T, ϕ) will be called the (generalized) Lelong number of T with respect to
the weight ϕ.

    If we had not required T ∧ (ddc ϕ)p to be defined pointwise on ϕ−1 (−∞), the assump-
tion that X is Stein could have been dropped: in fact, the integral over B(r) always
makes sense if we define
                               Z
                                                        p
                  ν(T, ϕ, r) =       T ∧ ddc max{ϕ, s}       with s < r.
                                 B(r)

Stokes’ formula shows that the right hand integral is actually independent of s. The
example given after (4.1) shows however that T ∧ (ddc ϕ)p need not exist on ϕ−1 (−∞) if
ϕ−1 (−∞) contains an exceptional compact analytic subset. We leave the reader consider
by himself this more general situation and extend our statements by the max{ϕ, s}
technique. Observe that r 7−→ ν(T, ϕ, r) is always an increasing function of r. Before
giving examples, we need a formula.

(5.5) Formula. For any convex increasing function χ : R −→ R we have
                   Z
                         T ∧ (ddc χ ◦ ϕ)p = χ′ (r − 0)p ν(T, ϕ, r)
                         B(r)

where χ′ (r − 0) denotes the left derivative of χ at r.
Proof. Let χε be the convex function equal to χ on [r − ε, +∞[ and to a linear function
of slope χ′ (r − ε − 0) on ] − ∞, r − ε]. We get ddc (χε ◦ ϕ) = χ′ (r − ε − 0)ddc ϕ on B(r − ε)
and Stokes’ theorem implies
                     Z                        Z
                                   c      p
                           T ∧ (dd χ ◦ ϕ) =         T ∧ (ddc χε ◦ ϕ)p
                      B(r)                     B(r)
                                              Z
                                            ⩾          T ∧ (ddc χε ◦ ϕ)p
                                               B(r−ε)

                                           = χ (r − ε − 0)p ν(T, ϕ, r − ε).
                                               ′


                  eε equal to χ on ] − ∞, r − ε] and linear on [r − ε, r], we obtain
Similarly, taking χ
      Z                          Z
                      c      p
               T ∧ (dd χ ◦ ϕ) ⩽        T ∧ (ddc χ
                                                eε ◦ ϕ)p = χ′ (r − ε − 0)p ν(T, ϕ, r).
        B(r−ε)                      B(r)
                     § 5. Generalized Lelong Numbers                                                     159

The expected formula follows when ε tends to 0.                                                            
                       R
  We get in particular B(r) T ∧ (ddc e2ϕ )p = (2e2r )p ν(T, ϕ, r), whence the formula
                                                     Z           1            p
                                           −2pr                         c 2ϕ
(5.6)                     ν(T, ϕ, r) = e                    T∧        dd e          .
                                                     B(r)         2

   Now, assume that X is an open subset of Cn and that ϕ(z) = log |z − a| for some
a ∈ X. Formula (5.6) gives
                                                 Z                 i                    p
                                           −2p                              ′ ′′     2
                      ν(T, ϕ, log r) = r                     T∧            d d |z|            .
                                                  |z−a|<r             2π

                             1
                                                                   P
The positive measure σT = p!   T ∧ ( 2i d′ d′′ |z|2 )p = 2−p            TI,I . in dz1 ∧ . . . ∧ dz n is called
the trace measure of T . We get
                                                                        
                                                  σT B(a, r)
(5.7)                            ν(T, ϕ, log r) =
                                                   π p r 2p /p!

and ν(T, ϕ) is the limit of this ratio as r → 0. This limit is called the (ordinary) Lelong
number of T at point a and is denoted ν(T, a). This was precisely the original definition
of Lelong, see [Lelong 1968]. Let us mention a simple but important consequence.
                                          
(5.8) Consequence. The ratio σT B(a, r) /r 2p is an increasing function of r. More-
over, for every compact subset K ⊂ X and every r0 < d(K, ∂X) we have
                                 
                       σT B(a, r) ⩽ Cr 2p                for a ∈ K and r ⩽ r0 ,
                          
where C = σT K + B(0, r0 ) /r02p .

   All these results are particularly interesting when T = [A] is the current
                                                                            of integration
over an analytic subset A ⊂ X of pure dimension p. Then σT B(a, r) is the euclidean
area of A ∩ B(a, r), while π p r 2p /p! is the area of a ball of radius r in a p-dimensional
subspace of Cn . Thus ν(T, ϕ, log r) is the ratio of these areas and the Lelong number
ν(T, a) is the limit ratio.

(5.9) Remark. It is immediate to check that
                                    
                                        0 for x ∈
                                                / A,
                      ν([A], x) =
                                        1 when x ∈ A is a regular point.

We will see later that ν([A], x) is always an integer (Thie’s theorem 8.7).

(5.10) Remark.
             R     When X = Cn , ϕ(z) = log |z − a| and A = X (i.e. T = 1), we obtain
in particular B(a,r) (ddc log |z − a|)n = 1 for all r. This implies

                                    (ddc log |z − a|)n = δa .
160                            Chapter III. Positive Currents and Lelong Numbers

This fundamental formula can be viewed as a higher dimensional analogue of the usual
formula ∆ log |z − a| = 2πδa in C.                                                

   We next prove a result which shows in particular that the Lelong numbers of a closed
positive current are zero except on a very small set.

(5.11) Proposition. If T is a closed positive current of bidimension (p, p), then for each
c > 0 the set Ec = {x ∈ X ; ν(T, x) ⩾ c} is a closed set of locally finite H2p Hausdorff
measure in X.
                                                             
Proof. By (5.7), we infer ν(T, a) = limr→0 σT B(a, r) p!/π p r 2p . The function a 7→
            
σT B(a, r) is clearly upper semicontinuous. Hence the decreasing limit ν(T, a) as r
decreases to 0 is also upper semicontinuous in a. This implies that Ec is closed. Now,
let K be a compact subset in X and let {aj }1⩽j⩽N , N = N (ε), be a maximal collection
of points in Ec ∩ K such that |aj − ak | ⩾ 2ε for j 6= k. The balls B(aj , 2ε) cover Ec ∩ K,
whereas the balls B(aj , ε) are disjoint. If Kc,ε is the set of points which are at distance
⩽ ε of Ec ∩ K, we get
                                  X                
                     σT (Kc,ε ) ⩾     σT B(aj , ε) ⩾ N (ε) cπ p ε2p /p!,

since ν(T, aj ) ⩾ c. By the definition of Hausdorff measure, we infer
                                          X                 
                  H2p (Ec ∩ K) ⩽ lim inf diam B(aj , 2ε) 2p
                                   ε→0
                                                         p!42p
                               ⩽ lim inf N (ε)(4ε)2p ⩽         σT (Ec ∩ K).               
                                   ε→0                    cπ p

   Finally, we conclude this section by proving two simple semi-continuity results for
Lelong numbers.

(5.12) Proposition. Let Tk be a sequence of closed positive currents of bidimension
(p, p) converging weakly to a limit T . Suppose that there is a closed set A such that
Supp Tk ⊂ A for all k and such that ϕ is semi-exhaustive on A with A ∩ B(R) ⊂⊂ X.
Then for all r < R we have
           Z                          Z
                        c  p
                 T ∧ (dd ϕ) ⩽ lim inf       Tk ∧ (ddc ϕ)p
            B(r)               k→+∞    B(r)
                                       Z                   Z
                                                     c   p
                             ⩽ lim sup      Tk ∧ (dd ϕ) ⩽       T ∧ (ddc ϕ)p .
                                k→+∞     B(r)                    B(r)

When r tends to −∞, we find in particular


## Demailly canonical extension, Lelong trace and growth, actual LF lines8833--9175

Text SHA256: 894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de

§ 6. The Jensen-Lelong Formula
    We assume in this section that X is Stein, that ϕ is semi-exhaustive on X and
that B(R) ⊂⊂ X. We set for simplicity ϕ⩾r = max{ϕ, r}. For every r ∈ ] − ∞, R[,
the measures ddc (ϕ⩾r )n are well defined. By Cor. 3.6, the map r 7−→ (ddc ϕ⩾r )n is
continuous on ] − ∞, R[ with respect to the weak topology. As (ddc ϕ⩾r )n = (ddc ϕ)n on
X \ B(r) and as ϕ⩾r ≡ r, (ddc ϕ⩾r )n = 0 on B(r), the left continuity implies (ddc ϕ⩾r )n ⩾
1lX\B(r) (ddc ϕ)n . Here 1lA denotes the characteristic function of any subset A ⊂ X.
According to the definition introduced in [Demailly 1985a], the collection of Monge-
Ampère measures associated with ϕ is the family of positive measures µr such that

(6.1)              µr = (ddc ϕ⩾r )n − 1lX\B(r) (ddc ϕ)n ,    r ∈ ] − ∞, R[.

The measure µr is supported on S(r) and r 7−→ µr is weaklyR continuous on the left by the
bounded convergence theorem. Stokes’ formula shows that B(s) (ddc ϕ⩾r )n −(ddc ϕ)n = 0
for s > r, hence the total mass µr (S(r)) = µr (B(s)) is equal to the difference between
the masses of (ddc ϕ)n and 1lX\B(r) (ddc ϕ)n over B(s), i.e.
                                             Z
                                         
(6.2)                          µr S(r) =          (ddc ϕ)n .
                                               B(r)


(6.3) Example. When (ddc ϕ)n = 0 on X \ ϕ−1 (−∞), formula (6.1) can be simplified
into µr = (ddc ϕ⩾r )n . This is so for ϕ(z) = log |z|. In this case, the invariance of ϕ under
unitary transformations implies that µr is also invariant. As the total mass of µr is equal
to 1 by 5.10 and (6.2), we see that µr is the invariant measure of mass 1 on the euclidean
sphere of radius er .

(6.4) Proposition. Assume that ϕ is smooth near S(r) and that dϕ 6= 0 on S(r), i.e.
r is a non critical value. Then S(r) = ∂B(r) is a smooth oriented real hypersurface and
the measure µr is given by the (2n − 1)-volume form (ddc ϕ)n−1 ∧ dc ϕ↾S(r) .
Proof. Write max{t, r} = limk→+∞ χk (t) where χ is a decreasing sequence of smooth
convex functions with χk (t) = r for t ⩽ r − 1/k, χk (t) = t for t ⩾ r + 1/k. Theorem 3.6
shows that (ddc χk ◦ ϕ)n converges weakly to (ddc ϕ⩾r )n . Let h be a smooth function h
with compact support near S(r). Let us apply Stokes’ theorem with S(r) considered as
the boundary of X \ B(r) :
        Z                       Z
                c     n
            h(dd ϕ⩾r ) = lim        h(ddc χk ◦ ϕ)n
          X               k→+∞
                                ZX
                        = lim       −dh ∧ (ddc χk ◦ ϕ)n−1 ∧ dc (χk ◦ ϕ)
                           k→+∞    X
                    § 6. The Jensen-Lelong Formula                                      163
                                      Z
                        = lim      −χ′k (ϕ)n dh ∧ (ddc ϕ)n−1 ∧ dc ϕ
                          k→+∞ X
                          Z
                        =         −dh ∧ (ddc ϕ)n−1 ∧ dc ϕ
                           X\B(r)
                          Z                         Z
                                   c   n−1     c
                        =     h (dd ϕ)     ∧d ϕ+            h (ddc ϕ)n−1 ∧ ddc ϕ.
                            S(r)                                   X\B(r)


Near S(r) we thus have an equality of measures

                  (ddc ϕ⩾r )n = (ddc ϕ)n−1 ∧ dc ϕ↾S(r) + 1lX\B(r) (ddc ϕ)n .              


(6.5) Jensen-Lelong formula. Let V be any plurisubharmonic function on X. Then
V is µr -integrable for every r ∈ ] − ∞, R[ and
                                 Z                           Z r
                                                c    n
                     µr (V ) −              V (dd ϕ) =             ν(ddc V, ϕ, t) dt.
                                     B(r)                     −∞



Proof. Proposition 3.11 shows that V is integrable with respect to the measure (ddc ϕ⩾r )n ,
hence V is µr -integrable. By definition
                                        Z
                             c
                        ν(dd V, ϕ, t) =        ddc V ∧ (ddc ϕ)n−1
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

with γ = ν(ddc V, a), and ν(ddc V, a) is the largest constant γ which satisfies this inequa-
lity. Thus ν(ddc V, a) = γ is equivalent to V having a logarithmic pole of coefficient γ.


§ 6.10. Special case. Take in particular V = log |f | where f is a holomorphic function
                                                            c
on X. The P Lelong-Poincaré formula shows that dd log |f | is equal−1to the zero divisor
[Zf ] =     mj [Hj ], where Hj are the irreducible components of f (0) and mj is the
                                           1
multiplicity of f on Hj . The trace 2π       ∆ log |f | is then the euclidean area measure of
Zf (with corresponding multiplicities mj ). By Formula (6.9 c), we see that the Lelong
number ν([Zf ], a) is equal to the vanishing order orda (f ), that is, the smallest integer m
such that DαP f (a) 6= 0 for some multiindex α with |α| = m. In dimension n = 1, we have
 1
2π ∆  log f =    mj δaj . Then (6.9 a) is the usual Jensen formula
                                                    Z r
                                                             dt X            r
                µ log |f |, S(0, r) − log |f (0)| =      ν(t) =       mj log
                                                      0        t             |aj |
where ν(t) is the number of zeros aj in the disk D(0, t), counted with multiplicities mj .

(6.11) Example. Take ϕ(z) = log max |zj |λj where λj > 0. Then B(r) is the polydisk
of radii (er/λ1 , . . . , er/λn ). If some coordinate zj is non zero, say z1 , we can write ϕ(z) as
                                                                                      λ /λ
λ1 log |z1 | plus some function depending only on the (n − 1) variables zj /z1 1 j . Hence
(ddc ϕ)n = 0 on Cn \ {0}. It will be shown later that

(6.11 a)                                  (ddc ϕ)n = λ1 . . . λn δ0 .

We now determine the measures µr . At any point z where not all terms |zj |λj are equal,
the smallest one can be omitted without changing ϕ in a neighborhood of z. Thus ϕ
depends only on (n − 1)-variables and (ddc ϕ⩾r )n = 0, µr = 0 near z. It follows that µr
is supported by the distinguished boundary |zj | = er/λj of the polydisk B(r). As ϕ is
invariant by all rotations zj 7−→ eiθj zj , the measure µr is also invariant and we see that
µr is a constant multiple of dθ1 . . . dθn . By formula (6.2) and (6.11 a) we get

(6.11 b)                          µr = λ1 . . . λn (2π)−n dθ1 . . . dθn .

In particular, the Lelong number ν(ddc V, ϕ) is given by
                                       Z
           c               λ1 . . . λn                                                dθ1 . . . dθn
      ν(dd V, ϕ) = lim                           V (er/λ1 +iθ1 , . . . , er/λn +iθn )               .
                    r→−∞        r       θj ∈[0,2π]                                      (2π)n
166                              Chapter III. Positive Currents and Lelong Numbers

These numbers have been introduced and studied by [Kiselman 1986]. We call them
directional Lelong numbers with coefficients (λ1 , . . . , λn ). For an arbitrary current T , we
define
                                                                    
(6.11 c)                 ν(T, x, λ) = ν T, log max |zj − xj |λj .

The above formula for ν(ddc V, ϕ) combined with the analogue of Harnack’s inequality
(6.9 d) for polydisks gives
                                           Z
               c               λ1 . . . λn                                           dθ1 . . . dθn
           ν(dd V, x, λ) = lim                V (r 1/λ1 eiθ1 , . . . , r 1/λn eiθn )
                           r→0   log r                                                 (2π)n
                               λ1 . . . λn
(6.11 d)                 = lim               sup V (r 1/λ1 eiθ1 , . . . , r 1/λn eiθn ).
                           r→0   log r θ1 ,...,θn




§ 7. Comparison Theorems for Lelong Numbers
   Let T be a closed positive current of bidimension (p, p) on a Stein manifold X equipped
with a semi-exhaustive plurisubharmonic weight ϕ. We first show that the Lelong num-
bers ν(T, ϕ) only depend on the asymptotic behaviour of ϕ near the polar set S(−∞).
In a precise way:

(7.1) First comparison theorem. Let ϕ, ψ : X −→ [−∞, +∞[ be continuous plurisub-
harmonic functions. We assume that ϕ, ψ are semi-exhaustive on Supp T and that

                            ψ(x)
             ℓ := lim sup        < +∞       as x ∈ Supp T and ϕ(x) → −∞.
                            ϕ(x)

Then ν(T, ψ) ⩽ ℓp ν(T, ϕ), and the equality holds if ℓ = lim ψ/ϕ.
Proof. Definition 6.4 shows immediately that ν(T, λϕ) = λp ν(T, ϕ) for every scalar
λ > 0. It is thus sufficient to verify the inequality ν(T, ψ) ⩽ ν(T, ϕ) under the hypothesis
lim sup ψ/ϕ < 1. For all c > 0, consider the plurisubharmonic function

                                     uc = max(ψ − c, ϕ).

Let Rϕ and Rψ be such that Bϕ (Rϕ ) ∩ Supp T and Bψ (Rψ ) ∩ Supp T be relatively
compact in X. Let r < Rϕ and a < r be fixed. For c > 0 large enough, we have uc = ϕ
on ϕ−1 ([a, r]) and Stokes’ formula gives

                              ν(T, ϕ, r) = ν(T, uc , r) ⩾ ν(T, uc ).

The hypothesis lim sup ψ/ϕ < 1 implies on the other hand that there exists t0 < 0 such
that uc = ψ − c on {uc < t0 } ∩ Supp T . We infer

                              ν(T, uc ) = ν(T, ψ − c) = ν(T, ψ),

hence ν(T, ψ) ⩽ ν(T, ϕ). The equality case is obtained by reversing the roles of ϕ and ψ
and observing that lim ϕ/ψ = 1/l.                                                      
                § 7. Comparison Theorems for Lelong Numbers                                         167

    Assume in particular that z k = (z1k , . . . , znk ), k = 1, 2, are coordinate systems centered
at a point x ∈ X and let
                                                                                       1/2
                            ϕk (z) = log |z k | = log |z1k |2 + . . . + |znk |2               .

We have limz→x ϕ2 (z)/ϕ1 (z) = 1, hence ν(T, ϕ1 ) = ν(T, ϕ2 ) by Th. 7.1.

(7.2) Corollary. The usual Lelong numbers ν(T, x) are independent of the choice of
local coordinates.                                                              

  This result had been originally proved by [Siu 1974] with a much more delicate proof.
Another interesting consequence is:

(7.3) Corollary. On an open subset of Cn , the Lelong numbers and Kiselman numbers
are related by                                             
                           ν(T, x) = ν T, x, (1, . . . , 1) .

Proof. By definition, the Lelong number ν(T, x) is associated with the weight ϕ(z) =
log |z −x| and the Kiselman number ν T, x, (1, . . . , 1) to the weight ψ(z) = log max |zj −
xj |. It is clear that limz→x ψ(z)/ϕ(z) = 1, whence the conclusion.                        

   Another consequence of Th. 7.1 is that ν(T, x, λ) is an increasing function of each
variable λj . Moreover, if λ1 ⩽ . . . ⩽ λn , we get the inequalities

                                  λp1 ν(T, x) ⩽ ν(T, x, λ) ⩽ λpn ν(T, x).

These inequalities will be improved in section 7 (see Cor. 9.16). For the moment, we just
prove the following special case.

(7.4) Corollary. For all λ1 , . . . , λn > 0 we have
                                    n            X         n
             ddc log max |zj |λj = ddc log           |zj |λj    = λ1 . . . λn δ0 .
                            1⩽j⩽n
                                                                 1⩽j⩽n


Proof. In fact, our measures vanish on Cn r {0} by the arguments explained in exam-
ple 6.11. Hence they are equal to c δ0 for some constant c ⩾ 0 which is simply the Lelong
number of the bidimension (n, n)-current T = [X] = 1 with the corresponding weight.
The comparison theorem shows that the first equality holds and that
                          X             n              X             n
                   ddc log       |zj |λj    = ℓ−n ddc log      |zj |ℓλj
                                 1⩽j⩽n                                         1⩽j⩽n

for all ℓ > 0. By taking ℓ large and approximating ℓλj with 2[ℓλj /2], we may assume
that λj = 2sj is an even integer. Then formula (5.6) gives
         Z                   X             n        Z           X            n
                         c              2sj       −2n            c          2sj
           P          dd log      |zj |        =r      P      dd      |zj |
             |zj |2sj <r2                                                 |zj |2sj <r2
                                    Z                       i                 n
              = s1 . . . sn r −2n P                   2n         d′ d′′ |w|2        = λ1 . . . λn
                                         |wj |2 <r2         2π
168                                Chapter III. Positive Currents and Lelong Numbers

                                                                    s
by using the s1 . . . sn -sheeted change of variables wj = zj j .                               

    Now, we assume that T = [A] is the current of integration over an analytic set
A ⊂ X of pure dimension p. The above comparison theorem will enable us to give a


## Gauduchon all-dimensional standard-metric theorem and complete printed proof, actual LF lines1--257

Text SHA256: fe5f0da186bc24ef80a6bc3cdc4a097a63c4b5e86165ca9d5ac62250615b600d

    Astérisque

PAUL G AUDUCHON
Les métriques standard d’une surface complexe
compacte a premier nombre de Betti pair
Astérisque, tome 126 (1985), p. 129-135
<http://www.numdam.org/item?id=AST_1985__126__129_0>




    © Société mathématique de France, 1985, tous droits réservés.
    L’accès aux archives de la collection « Astérisque » (http://smf4.emath.fr/
    Publications/Asterisque/) implique l’accord avec les conditions générales d’uti-
    lisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou
    impression systématique est constitutive d’une infraction pénale. Toute copie
    ou impression de ce fichier doit contenir la présente mention de copyright.




                      Article numérisé dans le cadre du programme
                    Numérisation de documents anciens mathématiques
                                 http://www.numdam.org/
                                 EXPOSÉ      XI



                    LES MÉTRIQUES STANDARD D'UNE SURFACE
              COMPLEXE COMPACTE A PREMIER NOMBRE DE BETTI PAIR


                               Paul GAUDUCHON


    Les deux exposés qui suivent sont consacrés à la démonstration du fait
 que toutes les surfaces K3 sont kahlériennes. L'objet de cet exposé est de
 démontrer le résultat suivant, qui fournit l'ingrédient technique essentiel :

 Théorème 1. Toute métrique hermitienne sur une surface complexe compacte à
 premier nombre de Betti pair est conforme à une métrique hermitienne, unique
 à homothétie près, dont la forme de Kahler est la partie de type (1,1) d'une
 2^-forme réelle fermée.

           Nous déduirons ce Théorème 1 d'un résultat général de géométrie
 hermitienne, le Théorème 2, et de la structure de Hodge particulière, déter-
 minée par K. Kodaira, d'une surface complexe compacte à b^ pair.
       Avant d'énoncer et de démontrer le Théorème 2 nous introduisons quel-
 ques éléments indispensables de géométrie hermitienne.


1. NOTATIONS ET DEFINITIONS
        Nous désignons par (M,J) une variété presque complexe de dimension
 n = 2m , TM le fibre tangent de M , A M le fibre des r-formes extérieures
 (réelles), r = 0 , . . . , n , A M = 2 A M le fibre des formes extérieures.

        Une métrique hermitienne est une métrique riemannienne g telle que
 l'opérateur presque complexe J soit une isométrie de l'espace tangent en
 tout point de M .
        La forme de Kahler de g est la 2-forme réelle de type (1,1) u> défi-
 nie en un point x de M pour tous vecteurs X,Y de T^M par
                  w(X,Y) = g(JX,Y) .


                                       129
                                   P. GAUDUCHON


         L'operateur J s'étend, par dualité métrique, au fibre A M des
formes extérieures. En fait, cette extension, encore notée J , ne dépend pas
de la métrique hermitienne g et est définie pour Xj,...,X £ T M et
H A ^ M par
          J9(X1,...,Xr) = (-l)r ^(JX1,...,JXr)



         A coté de la différentielle extérieure          d nous définissons 1'Opéra-
      ÇJ
teur d par la formule
                              dC = - J"1 d J .
                                 t                                       c
         Nota. Lorsque J est integrable, les opérateurs            d et d se décom-
posent, à la manière usuelle, en

                     d = d' + d"        ,          dC = i(d" - d') .

         Le produit scalaire ponctuel (resp. global) de deux champs de vec-
teurs ou de deux formes extérieures est noté ( , ) (resp. < , >).

          En particulier, la trace t r 9 d'une 2-forme        9 est le produit sca-
laire (<P,UJ) de 9 et de la forme de KMhler w .
                                       c                 c
         Les adjoints formels de d et d sont notes ô et 5 respective-
ment (ôC = - J"16 J).

           L'opérateur -ft de Hodge est défini, à la manière usuelle, pour 9 et
 >f| dans Ax M, par
                       <PA(*    = (9,vj/).v
                                            g
où vg 3: —m1—
            i üüm est la forme volume de g° .
         On a          ô = - *d*    ,             6C = - *dC* .

         Si n = 4 , l'opérateur # de Hodge induit une involution sur le fibre
A M . Les 2-formes -^-invariantes (resp. ^-anti-invariantes) sont dites auto-
duales (resp. anti-auto-duales). Le fibre A+M des 2-formes autoduales est
engendré, en chaque point de M , par la forme de KHhler U) et les formes
réelles de type (2,0) Q (0,2), tandis que le fibre A~M des 2-formes anti-
autoduales s'identifie à celui des 2-formes (réelles) primitives (= de trace
nulle) de type (l ,1) .

                                            130
         MÉTRIQUES STANDARD D'UNE SURFACE COMPLEXE COMPACTE A b¡ PAIR



         Le laplacien riemannien ôd + dô est noté A • Nous introduisons
le japlacien complexe L et le laplacien complexe adjoint L* définis par

(1)                    L(f) = - (ddCf,tf>) = - tr(ddCf)
(2)                    L*(f) = ôôC(f.u>) .

                              •H*    *
Les trois laplaciens A,L et L ont même symbole principal mais sont distincts
en général. Leur différence est mesurée par la 1-forme 8 = - ô°m . Plus pré-
cisément, on a
(3)                     L(f) = à(f) - (9,df)
 (4)                     L*(f)= A(f) + (9,df) - 60.f

(la vérification de ces deux relations est facile ;l'une et l'autre valent
que J soit integrable ou non).

         Une métrique hermitienne telle que £ et L coïncident ,c'est-à-dire
telle que la forme de K&hler soit co-fermée, est dite co-symplectique (semi-
kghléVienne si J est integrable). Ceci équivaut à dire que L est auto-
adjoint.

         Définition. Une métrique hermitienne est standard si la 1-forme 0
est co-fermée.
De façon équivalente,
      . le terme d'ordre zéro de L est nul (L (l) =0) ;
      . la forme de KHhler OJ est annulée par 66° ;
      . tu"1""1 est ddC-fermée.

Si n = 4 (m=2), une métrique hermitienne standard est une métrique hermitien-
ne dont la forme de K^hler est dd°-fermée.

2. RAPPELS SUR LES OPERATEURS ELLIPTIQUES
     Rappelons l'énoncé du principe du maximum pour les opérateurs elliptiques
du second ordre, dû à E. Hopf [3] :

 Proposition. Soient M une variété différentielle, m un point de M et
A:(3°°(M,]R)   > (3°°(M,P)         un opérateur "di f f érenti el elliptique du se-
 cond ordre, sans terme d'ordre zéro.Soit f une fonction admettant un maximum
relatif en m et telle que A(f) £ 0 au voisinage de m. Alors f est constante
au voisinage de m.


                                        131
                                  P. GAUDUCHON



          Par opérateur elliptique on entend ici un opérateur (du 2 ordre)
dont le symbole est positif non dégénéré (si 1'on a, dans un système de coor-
données locales,

                 A = 2 aij(x) ^$r.+         2 bi(x) 3I7 •

le symbole de A en m est la forme quadratique a (m,§) = £ a. .(m)§. Ç.).
                                                  ^           x3    1 j
          Dans le cas compact, on déduit immédiatement du principe du maxi-
mum le résultat suivant :

Corollaire 1. Supposons de plus M compacte connexe. Alors toute fonction
f sur M telle que A(f) ^ 0 est constante (et A(f) est nulle).

          La conséquence suivante a été observée par T. Aubin [ l ] :

Corollaire 2. Soient M une variété différentielle connexe, et A un opé-
rateur elliptique (réel) du second ordre. Soit f une fonction positive
sur M , non identiquement nulle, telle que A(f) = 0 . Alors f ne s'annule
en aucun point de M .

          Supposons en effet que f s'annule en un point m de M . Choisis-
sons un système de coordonnées locales (x^,...,x ) en m , et considérons une
forme linéaire Ç en les x^ . Soit A^ l'opérateur elliptique défini par

                      A§(g) = A(e<§'X>g) - g A(e<§'X>) .

                     -<§ x>
La fonction g^ = e      '   f satisfait a
                      Aç(gç) = - gç A(e<5'X>) = - f P(x,§) ,

où P(x,5) est un polynôme de degré < 2 en §> , dont la partie homogène de de-
gré 2 est le symbole a ^ x , ^ ) . Puisque A est elliptique, on a pour § assez
grand P(m,§) > 0 , d'où Ag(gg) ^ 0 dans un voisinage de m . La fonction g^
admettant un minimum relatif en m , on conclut de la proposition (appliquée
à ~ g^) Que f s'annule dans un voisinage de m , d'où le corollaire. •

3,LE THÉORÈME DES METRIQUES HERMITIENNES STANDARDS

Théorème 2 [2]. Toute métrique hermitienne sur une variété presque complexe


                                       132
       MÉTRIQUES STANDARD D'UNE SURFACE COMPLEXE COMPACTE A b¡ PAIR



compacte de dimension 2m est conforme à une métrique bermitienne standard « uni -
que à homothétie près.

Preuve. Soit g une métrique hermitienne quelconque sur M ; considérons
une métrique conforme ^ = e ^ g , où a est une fonction réelle. Le lapla-
cien complexe L et le laplacien complexe adjoint 'L* relatifs à g' s'écri-
vent pour toute fonction scalaire f .

            f(f) = e'2a L(f)   1*(f)    = e-2n,a L*(e2(m-'l)0 f)



Comme g est standard si et seulement si L (l) est nul, nous sommes ainsi
ramenés à montrer que L a une solution strictement positive 9 , unique
à un facteur constant positif près. La métrique standard sera alors égale à
  1
9    g .

Lemme 1. Le noyau Ker L** est de dimension 1 .
          En effet l'indice de L , égal à celui de A puisque L et A ont
même partie principale, est nul puisque A est autoadjoint. Ainsi Ker L
et Ker L ont même dimension ; mais le Cor.l au principe du maximum entraîne
que Ker L est réduit aux fonctions constantes, donc de dimension un. •
          Le lemme 1 dénontre l'assertion d'unicité du Théorème 2.
L'existence résulte du lemme suivant :

Lemme 2. Ker L     est engendré par une fonction      9 strictement positive
en tout point.
          En vertu de la théorie de Hodge pour l'opérateur elliptique L ,
l'espace <3 (M,K) se décompose en somme directe orthogonale

                         C°(M,I* ) = Ker L* 0 Im L .
           Soit 9 un élément non nul de Ker L ; alors la fonction 9 est
de signe constant sur M . Dans le cas contraire, en effet, i l existerait une
fonction de classe C positive, non identiquement nulle, orthogonale à 9 ,
donc aussi à Ker L* = B 9 et appartenant de ce fait à l'image de L . Or
ceci est exclu par le Cor.l au principe du maximum. On peut donc supposer
9 positive, et le Cor. 2 au principe du maximum permet de conclure que <P
est strictement positive en tout point. •


                                       133
                                  P. GAUDUCHON






# Additional actual continuous Richberg primary proof

Proof. By hypothesis HDR (X, R) = 0, u ∈ C∞ (X) and d(d′ u) = d′′ d′ u = 0, hence there
exists g ∈ C (X) such that dg = d′ u. Then dg is of type (1, 0), i.e. g ∈ O(X) and
            ∞


              d(u − 2 Re g) = d(u − g − g) = (d′ u − dg) + (d′′ u − dg) = 0.

Therefore u = Re(2g + C), where C is a locally constant function.                      

§ 5.E. Global Regularization of Plurisubharmonic Functions
    We now study a very efficient regularization and patching procedure for continuous
plurisubharmonic functions, essentially due to [Richberg 1968]. The main idea is con-
tained in the following lemma:

(5.17) Lemma. Let uα ∈ Psh(Ωα ) where Ωα ⊂⊂ X is a locally finite open covering
of X. Assume that for every index β

                              lim sup uβ (ζ) < max {uα (z)}
                                ζ→z               Ωα ∋z


at all points z ∈ ∂Ωβ . Then the function

                                   u(z) = max uα (z)
                                            Ωα ∋z


is plurisubharmonic on X.
Proof. Fix z0 ∈ X. Then the indices β such that z0 ∈ ∂Ωβ or z0 ∈
                                                               / Ωβ do not contribute
to the maximum in a neighborhood of z0 . Hence
                                             T there is a a finite set I of indices α
such that Ωα ∋ z0 and a neighborhood V ⊂ α∈I Ωα on which u(z) = maxα∈I uα (z).
Therefore u is plurisubharmonic on V .                                              

   The above patching procedure produces functions which are in general only continu-
ous. When smooth functions are needed, one has to use a regularized max function. Let
                              § 5. Plurisubharmonic Functions                                                                43
                                                                                                                R
θ∈C ∞
   R (R, R) be a nonnegative function with support in [−1, 1] such that                                          R
                                                                                                                     θ(h) dh = 1
and R hθ(h) dh = 0.

(5.18) Lemma. For arbitrary η = (η1 , . . . , ηp ) ∈ ]0, +∞[p , the function
                                      Z                                                  Y
           Mη (t1 , . . . , tp ) =           max{t1 + h1 , . . . , tp + hp }                    θ(hj /ηj ) dh1 . . . dhp
                                        Rn                                              1⩽j⩽n


possesses the following properties:

a) Mη (t1 , . . . , tp ) is non decreasing in all variables, smooth and convex on Rn ;
b) max{t1 , . . . , tp } ⩽ Mη (t1 , . . . , tp ) ⩽ max{t1 + η1 , . . . , tp + ηp } ;
c) Mη (t1 , . . . , tp ) = M(η1 ,...,ηbj ,...,ηp ) (t1 , . . . , tbj , , . . . , tp )
   if tj + ηj ⩽ maxk6=j {tk − ηk } ;
d) Mη (t1 + a, . . . , tp + a) = Mη (t1 , . . . , tp ) + a,                     ∀a ∈ R ;
e) if u1 , . . . , up are plurisubharmonic and satisfy H(uj )z (ξ) ⩾ γz (ξ) where z 7→ γz is a
   continuous hermitian form on TX , then u = Mη (u1 , . . . , up ) is plurisubharmonic and
   satisfies Huz (ξ) ⩾ γz (ξ).

Proof. The change of variables hj 7→ hj − tj shows that Mη is smooth. All properties
are immediate consequences of the definition, except perhaps e). That Mη (u1 , . . . , up ) is
plurisubharmonic follows from a) and Th. 5.6. Fix a point z0 and ε > 0. All functions
u′j (z) = uj (z) − γz0 (z − z0 ) + ε|z − z0 |2 are plurisubharmonic near z0 . It follows that

                                 Mη (u′1 , . . . , u′p ) = u − γz0 (z − z0 ) + ε|z − z0 |2

is also plurisubharmonic near z0 . Since ε > 0 was arbitrary, e) follows.                                                     

(5.19) Corollary. Let uα ∈ C∞ (Ωα ) ∩ Psh(Ωα ) where Ωα ⊂⊂ X is a locally finite open
covering of X. Assume that uβ (z) < max{uα (z)} at every point z ∈ ∂Ωβ , when α runs
over the indices such that Ωα ∋ z. Choose a family (ηα ) of positive numbers so small that
uβ (z) + ηβ ⩽ maxΩα ∋z {uα (z) − ηα } for all β and z ∈ ∂Ωβ . Then the function defined by
                                                              
                               e(z) = M(ηα ) uα (z)
                               u                                     for α such that Ωα ∋ z

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


# Current precise root source applications; not independent acceptance

{
  "recorded_at_utc": "2026-10-08T16:59:10.378258+00:00",
  "historical_unadmitted_argument_preserved": "notes/S11-small-curvature-pole-center-extension-20261008-inclusive-review-argument.md",
  "historical_argument_sha256": "bd9b6b1850c4b83340ae5f7873fb21e8f5771ed89efb4b4e33df606fedee2f87",
  "current_unadmitted_argument": "notes/S11-small-curvature-pole-center-extension-20261008-inclusive-review-argument-LF-corrected.md",
  "current_argument_sha256": "e699a94aeaca0da4f24c0d5074f3ba29badedff8b8b8bba7c0616391e7d02962",
  "current_argument_bytes": 211070,
  "whole_six_complete_author_and_public_support_components_unchanged": true,
  "task_and_cold_targets_and_notes_unchanged": true,
  "scoped_A_E_task_not_byte_identical_original": true,
  "cold_nested_original_task_remains_unchanged": true,
  "actual_primary_LF_contexts": [
    {
      "path": "inputs/primary/Demailly-regularization-1992-S11-extension.txt",
      "source_sha256": "98781e21d86b8407941e7427297c3c6b7bde63ef415b6709d0f97295c4667217",
      "actual_LF_range": [
        1,
        118
      ],
      "historical_full_body_matched_exactly": true,
      "actual_full_byte_comparison_with_sed": true,
      "historical_body_sha256": "9e25e759d762edc5adaa63950e09df749292542befeb5e42e5df44137b512092",
      "actual_body_sha256": "865471ce28a18f076c330ecb35ae70fe54b224c2c643c6d94202fac80e2a4b00",
      "whole_current_actual_LF_context_root_read_pending": false,
      "actual_entire_current_context_root_read_chunks": [
        "fb919c"
      ]
    },
    {
      "path": "inputs/primary/Demailly-regularization-1992-S11-extension.txt",
      "source_sha256": "98781e21d86b8407941e7427297c3c6b7bde63ef415b6709d0f97295c4667217",
      "actual_LF_range": [
        275,
        640
      ],
      "historical_full_body_matched_exactly": true,
      "actual_full_byte_comparison_with_sed": true,
      "historical_body_sha256": "889accdac2892fbc881b48a913d24aa16180799a6330173940815776c8cc5331",
      "actual_body_sha256": "53a1199cc7c7c3aad29889fcc526c79d56224257286a8b54bf00f1a711130ad1",
      "whole_current_actual_LF_context_root_read_pending": false,
      "actual_entire_current_context_root_read_chunks": [
        "844157",
        "b42fb9"
      ]
    },
    {
      "path": "inputs/primary/Demailly-regularization-1992-S11-extension.txt",
      "source_sha256": "98781e21d86b8407941e7427297c3c6b7bde63ef415b6709d0f97295c4667217",
      "actual_LF_range": [
        1638,
        1740
      ],
      "historical_full_body_matched_exactly": true,
      "actual_full_byte_comparison_with_sed": true,
      "historical_body_sha256": "73e160c63995d4dd01e0d2706ea64f983b608beefcb4015b1ee9ff0398999f85",
      "actual_body_sha256": "9b325140d53ae5acdf675ced3526cc27273df32cdc15bfd33f2473f42a57a2e2",
      "whole_current_actual_LF_context_root_read_pending": false,
      "actual_entire_current_context_root_read_chunks": [
        "1df2b3"
      ]
    },
    {
      "path": "inputs/primary/Demailly-author-hosted-S11-full.txt",
      "source_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
      "actual_LF_range": [
        2055,
        2190
      ],
      "historical_full_body_matched_exactly": true,
      "actual_full_byte_comparison_with_sed": true,
      "historical_body_sha256": "9c2511ca6e8d1a3cefb66bb6790339d60a49b8157adb6ab86e2f89d44a4b28ae",
      "actual_body_sha256": "354ba1101136013ccbf1e0090fd14aa919ad8a5d0f4ca726d24f2f00e9379f78",
      "whole_current_actual_LF_context_root_read_pending": false,
      "actual_entire_current_context_root_read_chunks": [
        "68c61a"
      ]
    },
    {
      "path": "inputs/primary/Demailly-author-hosted-S11-full.txt",
      "source_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
      "actual_LF_range": [
        2300,
        2355
      ],
      "historical_full_body_matched_exactly": true,
      "actual_full_byte_comparison_with_sed": true,
      "historical_body_sha256": "711beafef4e9d6d2ab874fd503e2c18d044d0aad2c4e4e69a5b36f3c0b248349",
      "actual_body_sha256": "43ec101293456a7a47cbe228e38220bc045b91d71d15e16d23fe8f01fe411e04",
      "whole_current_actual_LF_context_root_read_pending": false,
      "actual_entire_current_context_root_read_chunks": [
        "75e2ce"
      ]
    },
    {
      "path": "inputs/primary/Demailly-author-hosted-S11-full.txt",
      "source_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
      "actual_LF_range": [
        14896,
        14934
      ],
      "historical_full_body_matched_exactly": true,
      "actual_full_byte_comparison_with_sed": true,
      "historical_body_sha256": "3618f3fc1da2777079df5e691134b20ccb0d44b5d7dd130ee413809293ffa93c",
      "actual_body_sha256": "3cc1f14f0214dd693eca67a4bc8f4b67c15c036e8c86676e07371e08796f0296",
      "whole_current_actual_LF_context_root_read_pending": false,
      "actual_entire_current_context_root_read_chunks": [
        "18f20a"
      ]
    },
    {
      "path": "inputs/primary/Demailly-author-hosted-S11-full.txt",
      "source_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
      "actual_LF_range": [
        8546,
        8745
      ],
      "historical_full_body_matched_exactly": true,
      "actual_full_byte_comparison_with_sed": true,
      "historical_body_sha256": "02bae8f103d1702cec42f1517b24ad6c1593992875a6bc249535896418f917eb",
      "actual_body_sha256": "adb8224683d546b7d542a0d847a006ec64387ad864f8748892dfca5d4e514c49",
      "whole_current_actual_LF_context_root_read_pending": false,
      "actual_entire_current_context_root_read_chunks": [
        "013209"
      ]
    },
    {
      "path": "inputs/primary/Demailly-author-hosted-S11-full.txt",
      "source_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
      "actual_LF_range": [
        8833,
        9175
      ],
      "historical_full_body_matched_exactly": true,
      "actual_full_byte_comparison_with_sed": true,
      "historical_body_sha256": "257ed93a29b19da99dee446a9c8242a195c48a1ac5d8b1b1d8b349f5d3ffcb0a",
      "actual_body_sha256": "961d87af8473d3367a89df8f931ba7af78c575d2a845716f73893d1fd113a57e",
      "whole_current_actual_LF_context_root_read_pending": false,
      "actual_entire_current_context_root_read_chunks": [
        "e8c25d",
        "f3080a"
      ]
    },
    {
      "path": "inputs/primary/Gauduchon-torsion-1985.txt",
      "source_sha256": "fe5f0da186bc24ef80a6bc3cdc4a097a63c4b5e86165ca9d5ac62250615b600d",
      "actual_LF_range": [
        1,
        257
      ],
      "historical_full_body_matched_exactly": true,
      "actual_full_byte_comparison_with_sed": true,
      "historical_body_sha256": "fc9080a0f64f8b0d463054ba601bb96bdb8d5bd8a0dd366395352a13edd8f39a",
      "actual_body_sha256": "8e289c460feee3799a00ac1489060579756d43d41be911d8a05619037de8b7be",
      "whole_current_actual_LF_context_root_read_pending": false,
      "actual_entire_current_context_root_read_chunks": [
        "092134"
      ]
    }
  ],
  "whole_current_context_reads_pending": false,
  "new_exact_application_record_pending": false,
  "historical_blanket_assembled_primary_excerpt_read_claim_not_reused": true,
  "precise_boundary": "Actual source proofs must be read and their exact new applications assessed before future admission. Old splitlines-derived excerpt bodies are not credited as their claimed LF locators. The six full author and completed public proof components are preserved; no aggregate whole argument display is claimed.",
  "native_admission": false,
  "current_native_owner": 65313,
  "mathematical_acceptance": false,
  "original_S11_completed": false,
  "published": false,
  "all_nine_current_actual_LF_contexts_wholly_root_read": true,
  "partial_display_boundary": "844157 had a 54-token aggregate truncation around the gluing introduction. Actual LF425--470 was wholly re-read in b42fb9; those two observations together cover the entire current LF275--640 context. The scoped-task display896663 was truncated and is not credited; complete task a0d76f was then read.",
  "whole_current_article_root_read_chunk": "87628b",
  "whole_scoped_task_root_read_chunk": "a0d76f",
  "whole_statement_only_input_root_read_chunk": "e093a6",
  "updated_at_utc": "2026-10-08T17:11:17.955446+00:00",
  "exact_new_application_judgments": [
    {
      "target": "A: closed-current attenuation and global smooth positivity",
      "assessment": "Apply Demailly to T=dd^c q prime, which is CLOSED, with smooth closed representative zero and source potential psi=q prime/2. The lower bound gamma=epsilon*h-B is smooth real, and the source does not require gamma closed. On compact M, the selected smooth tangent metric has Griffiths curvature bounded below by -C*h tensor Id; choose the source u=C*h. Every positive Lelong level is empty. Continuous lambda_k decrease to zero; Dini makes the loss uniform. Together with epsilon_k decreasing to zero this gives the actual positive margin for a global smooth f=2*psi_(s,k).",
      "Richberg_boundary": "The continuous attenuated intermediate is smoothed. The printed1992 Lemma2.15 uniform-approximation statement is not credited for arbitrary pole-bearing quasi-psh functions. The actual Richberg theorem I.5.21 explicitly assumes continuity, and its full printed proof with regularized-max Lemma5.18 was read in ea796f+c9a491. The stronger-curvature Section2 attenuation/gluing application is the route used. Smooth f is not asserted ordinarily equivalent to the original q prime.",
      "inherited_boundary": "Kiselman minimum principles and classical psh/Richberg foundations are imported with attribution. The supplied Section5 proof-end context is wholly read but is not represented as a recursive reading of every preceding L2 lemma."
    },
    {
      "target": "E: arbitrarily small curvature in the SAME ordinary type implies zero point Lelong numbers",
      "assessment": "Gauduchon Theorem2 supplies a smooth positive gamma with dd^c gamma^(n-1)=0 in every n>=2; its separate even-Betti Theorem1 is excluded. In dimension one gamma^0=1 suffices. For each actual same-type q_delta, the positive GLOBAL current T_delta=dd^c q_delta+delta*h has exact total gamma-trace delta*int(h gamma^(n-1)) by distributional Stokes, despite being nonclosed. Add the fixed delta-quadratic on finitely many nested charts to get genuine psh CLOSED local Hessians. Uniform comparisons bound their local trace by C*delta. Fixed-radius Lelong trace monotonicity then bounds every point value by C*delta. Mutual bounded order and smooth additions preserve point Lelong numbers by the actual logarithmic growth formula. The source operator is twice the task operator; the positive constant is absorbed in C. Sending delta to zero proves the conclusion without a smooth representative in the type.",
      "source_application": "Actual complete Gauduchon proof and III.5.5--5.8 and III.6.8--6.9 growth/comparison proof contexts were read. Only closed LOCAL corrected Hessians receive the closed-current trace theorem."
    },
    {
      "target": "B: canonical divisor removal and both strictness directions",
      "assessment": "Off the effective divisor subtract its holomorphic logarithms from the strict potential and add a common local quadratic. The result is psh and locally bounded above because the residual is bounded above by q plus a constant. Canonical pluripolar removability yields its genuine extension. Its positive Hessian has positive coefficient-matrix measure on the divisor, whereas the smooth lower bound has zero restriction there; therefore the sharp nonclosed lower bound extends. Both bounded inequalities extend by canonical psh recovery, so the residual remains in [q]. E supplies zero point Lelong numbers, and A supplies a smooth positive gauge representative. Conversely choose the actual same-type q_delta with delta below the smooth positivity margin; Poincare-Lelong adds the positive divisor and gives a strict current. Delta=0 and zero coefficients are treated canonically.",
      "restriction_boundary": "No singular current or pole-bearing residual is restricted to an exceptional curve. I.5.23 removability and the normalization-compatible Poincare-Lelong application are the precise imported foundations."
    },
    {
      "target": "C: explicit pole residual after all stated finite point blowups",
      "assessment": "The piecewise convex chi_L matches value and derivative at -L and has derivative between zero and eta_L tending to zero. Its composition with G_p has the actual lower curvature -eta_L*w1 and bounded difference from U, including the common poles. Pullback to any finite point-blowup tower retains genuine canonical functions and this inequality; the fixed smooth pi*w1 is bounded by C*h prime. At each total-transform point, a direction with nonzero leading homogeneous term of its finite-order holomorphic equation gives a spherical supremum at least -C*abs(log r)^alpha-C. The actual growth formula with alpha<1 proves zero Lelong number. This is an explicit logarithmic family, not a universal zero-Lelong pullback theorem."
    },
    {
      "target": "D: pole-center obstruction, genuine recursive one-sided strict witness and mass-law application",
      "assessment": "Apply B to divisor b*pi*D and residual pi*U. The last exceptional curve is contracted by the composite. Only a proposed SMOOTH f is restricted; pi*beta vanishes there and curve Stokes excludes dd^c f strictly positive on it. For a one-point blowup, choose O(E) curvature negative on the exceptional vertical tangent. Along the exceptional curve pullback h has positive horizontal coefficient and zero vertical coefficient, so adding -t*B_E gives a positive matrix for small t; the horizontal/vertical Schur estimate extends over a fixed exceptional neighborhood, and compactness controls its complement. At each finite stage the actual logarithmic potential with positive coefficient therefore restores a uniform positive Hermitian lower bound. Its global bounded-above logarithm preserves the one-sided upper order, including poles. Repeating finitely many times yields the genuine witness. It cannot be mutually equivalent by the first obstruction. Separately credited full-type descent and actual non-pluripolar pushforward laws preserve the original ordinary-type infimum/supremum; the new exceptional-log type is not substituted into that optimization.",
      "support_boundary": "The previously checked complete ruled source, independent proof notes and final report remain the supplied established mass-law proofs. Their whole components were previously read; no historical optional-artifact verdict or unrelated broad L1-density grant is used. No factorization of arbitrary modifications or arbitrary upstairs-volume law is inferred."
    }
  ],
  "additional_continuous_Richberg_primary_context": {
    "path": "inputs/primary/Demailly-author-hosted-S11-full.txt",
    "source_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
    "actual_LF_range": [
      2180,
      2310
    ],
    "actual_full_byte_comparison_with_sed": true,
    "whole_relevant_printed_proof_root_read_chunks": [
      "ea796f",
      "c9a491"
    ],
    "exact_hypothesis": "Continuous psh inputs; not arbitrary pole-bearing quasi-psh uniform approximation."
  }
}


# Current exact A--G statements, supplied as evidence

# Restricted S11 extension A--G: statements without author proofs

Use dd^c=i partial barpartial/(2 pi), genuine canonical quasi-psh functions,
mutual bounded ordinary equivalence, and the original extended non-pluripolar
products. General original S11 remains open. Prove or reject all targets with
complete ordinary unverified notes and a valid support DAG.

## A. Precise necessary smoothing consequence

On a connected compact complex manifold M with h>0, let B be any smooth real
(1,1) form, not necessarily closed, and let q' be genuine quasi-psh with zero
point Lelong numbers everywhere. If B+dd^c q'>=epsilon h for epsilon>0,
there is a smooth real f with B+dd^c f>=epsilon h/2. Prove the application of
the permitted closed-current regularization theorem with the exact source
normalization, every curvature hypothesis, actual smoothness on all M and a
uniform curvature loss. Do not claim that f~q' or apply regularization directly
to the nonclosed current B+dd^c q'. Credit the known regularization mechanism.

## B. A strict ordinary-type criterion

Let Delta=sum_(j=1)^N a_j D_j be any finite effective real divisor, a_j>=0,
with global logarithmic potential ell_Delta and smooth closed curvature
chi_Delta satisfying dd^c ell_Delta=[Delta]-chi_Delta. Zero coefficients mean
the zero function even on their divisors. Let q be genuine quasi-psh. Assume that for every delta>0 there is
q_delta~q with dd^c q_delta>=-delta h. For arbitrary smooth real theta, put
B=theta-chi_Delta. There is a strict theta-current in [ell_Delta+q] if and
only if B has a smooth strictly positive gauge representative B+dd^c f.
Prove canonical divisor removal, the retained sharp nonclosed lower bound,
both bounded inequalities at poles and actual same-type sufficiency. Do not
assume an arbitrary pole-bearing current can be restricted to a divisor.

## C. The explicit residual after every finite point-blowup composition

Let Y=P1 x P1 with probability Fubini--Study forms w1,w2, D={p} x P1,
Gp<=0, dd^c Gp=[p]-w and max Gp=0 on the first factor. Put
U=1-(1-Gp)^alpha, 0<alpha<1. For every finite composition pi:Y'->Y of
point blowups, pi^*U has zero point Lelong numbers at EVERY point and its
ordinary type admits arbitrarily small negative curvature relative to any
fixed smooth h'>0. Give genuine same-type representatives, including every
pole, and check the Lelong growth at all infinitely near points. The targets
do not grant that arbitrary pullbacks preserve zero Lelong numbers.

## D. Blowup centers in the poles and recursive one-sided witnesses

Fix c>0, 0<=b<c, a>0 smooth on the first P1, theta=cw1+a w2,
beta=(c-b)w1+a w2 and r=bGp+U. For every NONEMPTY finite composition of
point blowups pi:Y'->Y, including centers in D and on earlier exceptional
divisors, no strict pi^*theta-current can have a potential mutually
ordinarily equivalent to pi^*r. There is nevertheless an ACTUAL strict
potential v'<=pi^*r+C. Using the established mass laws explicitly declared
below, the full pulled-back ordinary-type infimum and supremum remain
2(c-b)min a and 2(c-b)max a. Distinguish the one-sided witness's new type from
the optimized pulled-back type. Prove strictness for arbitrary finite stages,
all pole centers and actual Hermitian lower bounds. Restrict only an object
whose restriction is justified. No general modification factorization or
arbitrary upstairs-density Gauduchon volume invariance is a target.

## E. Automatic zero point Lelong numbers from the ordinary-type hypothesis

On every connected compact complex manifold M of positive dimension with h>0,
let q be a genuine quasi-psh function. Assume that for EVERY delta>0 there is
an ACTUAL genuine q_delta in the SAME ordinary type [q] with
dd^c q_delta>=-delta h. Then q has zero point Lelong numbers at EVERY point.
Prove the full statement. Smooth approximations that change the ordinary
type do not establish its antecedent. This conclusion is not granted, and
B must now be proved without an additional zero-Lelong assumption. A alone
continues to assume zero Lelong numbers as its explicit conditional antecedent.
No statement about arbitrary pullbacks of zero-Lelong functions is granted.

## F. Small-curvature ordinary types under all smooth compact modifications

Under EXACTLY the small-curvature SAME ordinary-type hypothesis in E, every
smooth connected compact modification pi:M'->M has a genuine canonical
pullback pi^*q whose SAME ordinary type admits arbitrarily small negative
curvature relative to any chosen Hermitian h'>0. Its point Lelong numbers
vanish everywhere on M'. Prove actual canonical pullback, ordinary inequalities
including pole values, and the curvature bound. No factorization into blowups,
and no theorem for pullbacks of all arbitrary zero-Lelong functions, is granted.

## G. Residual neutrality for every ambient ideal and exact intrinsic traces

If q is genuine quasi-psh and has zero point Lelong numbers everywhere, then
exp(-s q) is locally integrable for EVERY s>0 and, for EVERY genuine quasi-psh
v and EVERY real t>0, I(t(v+q))=I(tv), using |g|^2 exp(-t u) with no extra2.
Prove both statements and every integrability/exponent step; neither is granted.
In particular, under E and for ANY finite effective real Delta,
I(t(ell_Delta+q))=I(t ell_Delta) for every real t>0.

If Delta=sum a_j D_j has SIMPLE NORMAL CROSSINGS and Y is smooth connected
compact, contained in NONE of the positive-coefficient D_j, prove for EVERY
smooth connected compact modification rho:Z->Y and EVERY prime divisor E on Z
the original finite intrinsic AMBIENT ideal trace is

 tau_(Y,ell_Delta+q)(E)
 = lim_(t->infinity) t^(-1) ord_E(I(t(ell_Delta+q)) O_Y)
 = sum_(j:a_j>0) a_j ord_E rho^*(D_j|Y).

All intrinsic sums and products omit ZERO coefficients before restricting
equations or taking orders; zero times an infinite order is never used.

Check all integer coefficient endpoints and nonzero restricted equations.
The naive restriction q|Y may be identically minus infinity. Do not replace
ambient restricted ideals by the multiplier ideal of that naive restriction.
Do not claim exactness of an envelope trace merely from lower inequalities.
No formula for arbitrary non-SNC Delta is requested for the last displayed
trace; the ambient ideal equality itself does cover arbitrary Delta.

## Permitted exact background and its separate credit

Canonical psh removability across closed pluripolar sets for locally
upper-bounded functions, positivity of their distributional Hessian,
holomorphic pullback of genuine psh functions, Poincare--Lelong, distributional
Stokes, point-blowup charts and the exceptional bundle O(-1) are permitted
standard foundations. Their exact new applications must be justified.

Demailly, Regularization of closed positive currents and Intersection Theory,
J. Algebraic Geometry 1 (1992), 361--409, Main Theorem 1.1 and its Section 2
stronger-curvature proof are allowed background. Precisely, on compact
Hermitian M a closed almost positive current T=alpha+(i/pi)partial barpartial
psi, with alpha smooth closed real, psi genuine quasi-psh, and T>=gamma for
arbitrary continuous real gamma, has for each fixed s>0 global potentials
psi_(s,k) smooth on M minus E_s(T), where E_s(T)={x:nu(T,x)>=s}, with
T_(s,k)=alpha+(i/pi)partial barpartial psi_(s,k) and
T_(s,k)>=gamma-min(lambda_k,s)u-epsilon_k h. Here lambda_k are continuous,
decrease pointwise to nu(T,x), and epsilon_k>0 decreases to zero. This is
available under the stronger sufficient condition that the Chern curvature
of the selected smooth tangent metric satisfies c(TM)+u tensor Id>=0 in
the Griffiths sense, with u smooth semipositive. The primary theorem's
lower bound gamma is not required to be closed. All hypotheses and the
source-to-task factor conversion must be checked. Primary text:
https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization.pdf.
No target A or B is directly granted.

The ordinary-type mass definitions and the following ruled-family mass
laws are established input, not new targets to be claimed with priority:
for b<c every rough theta-psh v~r has finite positive extended mass and the
infimum/supremum are 2(c-b)min a and 2(c-b)max a. For a proper smooth compact
modification pi, genuine pi^*theta-psh potentials descend canonically; this
gives a bijection of the entire pulled-back ordinary type with the downstairs
type, and actual non-pluripolar pushforward preserves their extended top
mass. These statements are proved in Sections 2--5 of the retained paper
Restricted masses and ordinary strict-current types on a nonclosed ruled
surface, source at commit 2ec45dec6172ced6e2af18b2b5fe657c07aeee9e:
https://github.com/MingchenXia/non-kahler-pluripotential-theory/blob/2ec45dec6172ced6e2af18b2b5fe657c07aeee9e/research/papers/S11-nonclosed-ruled-restricted-masses-and-strict-types.tex.
Only the exact application of these specified mass laws is needed in D;
no numerical result boolean or optional artifact is a proof premise.


Additional precisely permitted established foundations for the new E:
Gauduchon's standard-metric theorem: every Hermitian metric on a compact
complex manifold of dimension n>=2 is conformal to a smooth Hermitian
gamma satisfying dd^c gamma^(n-1)=0, unique up to a positive scalar.
Theorem2 and its complete proof, not the separate even-Betti Theorem1, in
P. Gauduchon, Les metriques standard d'une surface complexe compacte a
premier nombre de Betti pair, Asterisque126 (1985), pp132-133:
https://www.numdam.org/item/AST_1985__126__129_0/.
For a local closed positive current T of bidimension(p,p), the normalized
trace mass of T on B(x,r), divided by r^(2p), is nondecreasing in r and
its limit is the point Lelong number up to its fixed stated normalization.
For a genuine psh function v the point Lelong number of dd^c v equals
the limiting logarithmic spherical-supremum growth quotient, so it is
unchanged by smooth additions or mutual bounded difference. These are
Demailly, Complex Analytic and Differential Geometry, III.5.5-5.8 and
III.6.8-6.9, at the university-hosted primary text
https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf.
These exact local foundations do not grant E, a global curvature-to-Lelong
estimate, any smoothing in an ordinary type, or any of the A-D targets.
Check every actual local and global application and dimension, including n=1.
Return consistent indexed evidence for every actual external premise.


Additional precisely imported foundations for the new F--G:
Demailly, On the cohomology of pseudoeffective line bundles, arXiv1401.5432v2,
Theorem1.2: for psh phi on a bounded pseudoconvex domain, every m>0 gives
the weighted Bergman potential phi_m=(1/(2m))log(sum|g_(m,l)|^2); its kernel
is the squared norm of evaluation on the weighted Hilbert unit ball and
nu(phi,x)-n/m<=nu(phi_m,x)<=nu(phi,x). The entire printed proof is read;
it imports Ohsawa--Takegoshi. This does NOT grant zero-Lelong integrability G.
On the same primary, Section2 Corollary2.3 (Guan--Zhou strong openness, with
the supplied Hiep proof), if |g|^2 exp(-2c phi) is locally integrable for a
psh phi, some c'>c preserves that local integrability after shrinking.
The complete printed Section2 proof chain is read; it imports
Ohsawa--Takegoshi and standard-basis/analytic division foundations, not
recursively certified. Source factor2 must be converted to the task weight.
Elementary Holder, mean-value and holomorphic Cauchy estimates, local
normal-crossing polar integrals and exact divisorial order of a nonzero
holomorphic equation are permitted. No F or G conclusion, intrinsic-trace
formula, residual-neutrality equality or modified-source acceptance is granted.


# Complete new private unverified author proof

# S11: nearly flat ordinary residuals and their exact ambient ideal traces

Private unverified research, 8 October 2026. Added before any native admission
of the S11 small-curvature/pole-center extension. The old source, arguments,
targets and read records are preserved. These proofs are not accepted and the
general S11 programme remains open. No priority is claimed for the classical
Bergman, zero-Lelong integrability or strong-openness mechanisms.

Let M be connected compact complex, h smooth positive, and q genuine quasi-psh.
For every delta>0 assume an ACTUAL q_delta~q with dd^c q_delta>=-delta h.
The current author's Gauduchon trace/local fixed-radius Lelong argument proves
nu(q,x)=0 at every point. That entire source was root-read in543d61 (and earlier
87628b), with every primary application separately assessed.

F. For ANY smooth connected compact modification pi:M'->M, choose h'>0 and a
fixed C with pi^*h<=C h'. Genuine holomorphic psh pullback after smooth local
correction is locally integrable and canonical: generically pi is an
isomorphism and the pullback is not identically minus infinity on any open set.
The pointwise inequalities q_delta~q pull back including poles. Therefore
pi^*q_delta~pi^*q, dd^c pi^*q_delta>=-C delta h'. The SAME small-curvature
property holds upstairs and the author's trace lemma applied on M' gives zero
point Lelong numbers everywhere. This covers all smooth compact modifications
without a factorization theorem or a general zero-Lelong pullback grant.

G1. Zero point Lelong numbers of a quasi-psh q give exp(-s q) locally integrable
for every s>0. A direct proof from an exactly imported Bergman foundation is:
add a smooth local correction to q to obtain psh phi on a bounded pseudoconvex
coordinate ball. Demailly1401.5432v2 Theorem1.2(b), with its kernel formula,
gives 0<=nu(phi_m,x)<=nu(phi,x)=0 for EVERY m>0. If all holomorphic functions
in H_Omega(m phi) vanished at x, the weighted norm controls their local C1
norms by unweighted mean-value/Cauchy estimates since phi is bounded ABOVE on
a slightly larger compact neighborhood. For its entire unit ball this gives
|f(z)|<=C|z-x|. The evaluation-norm kernel then gives
phi_m(z)<=(1/m)log|z-x|+C and hence nu(phi_m,x)>=1/m, contradiction.
Some ACTUAL weighted holomorphic f is nonzero at x. Shrinking around x makes
|f| bounded below, so its finite weighted integral proves exp(-2m phi) locally
integrable there. Set2m=s; bounded smooth corrections preserve this property.
No restriction of a singular current to a submanifold is made.

G2. For EVERY genuine quasi-psh v and every real t>0,
I(t(v+q))=I(tv), with the task weight |g|^2 exp(-t u), NO extra factor2.
The local upper bound on q gives the first inclusion. For g in I(tv), add
bounded smooth local corrections to v and q to make them psh. Strong openness
(Demailly Section2, Corollary2.3) gives p>1 with |g|^2 exp(-p t v) integrable
on a smaller neighborhood. The primary uses exp(-2c phi), so here c=t/2 and
the multiplier p is unchanged. Setp'=p/(p-1). G1 and bounded g give
|g|^2 exp(-p' t q) integrable. Holder on the exact factorization

 |g|^2 exp(-t(v+q))
 = (|g|^2 exp(-p t v))^(1/p) (|g|^2 exp(-p' t q))^(1/p')

gives the reverse inclusion. Equality of every local stalk gives the sheaf
identity, and bounded smooth corrections undo exactly. This classical
zero-Lelong neutrality mechanism is not claimed as a new theorem.

G3. Setv=ell_Delta for a finite effective real divisor. Then ALL ambient ideals
of ell_Delta+q equal those of ell_Delta. If Delta=sum a_j D_j is SNC and
Y is smooth connected compact, contained in none of the positive-coefficient
D_j, normal crossing polar integrability gives
I(t ell_Delta)=O(-sum floor(t a_j)D_j).
The minimum holomorphic order is floor(t a_j): any smaller order leaves an
exponent<=-2; at integer coefficient the forbidden order has EXACT exponent
-2 and diverges. Dividing by the allowed powers leaves every product exponent
strictly>-2. Restriction to Y is the locally principal product of NONZERO
equations (g_j|Y)^floor(t a_j). On ANY smooth compact modification rho:Z->Y,
the orders N_j,E of these equations along any prime E are finite. Exact
restricted ideal order is sum floor(t a_j)N_j,E, so its limit divided by t is
sum a_j N_j,E. This is the original intrinsic AMBIENT-ideal trace, even when
q|Y is identically minus infinity. It neither uses a naive restriction nor
turns lower envelope inequalities into equality. Generic point Lelong along
Y is zero under these assumptions, as required by the original trace setup.

New primary read boundary: Demailly1401.5432v2 actual LF285--390 is the ENTIRE
Theorem1.2 proof, root-read310b60 (previousP06 b5c643). Actual LF665--1040
contains the strong-openness statement and ENTIRE printed Section2 proof:
cfa861 LF665--840 plus334820 LF840--1040; proof ends before the Section3
heading at1043. Printed Corollary2.3 is obtained from2.2(ii) with
psi=(1+delta)phi, with harmless bounded constants making phi<=0. The proof
imports Ohsawa--Takegoshi and standard-basis/analytic division theory, which
are not recursively certified. Printed2.11 wording 'uniformly bounded' is
used only as local uniform bounds ABOVE; the proof works with pole-bearing
psh weights. The displayed Fj,l=1 in the paragraph of2.11(ii) has the
immediate fl counterpart in Lemma2.9 and later decomposition; it is a printed
typographical issue, not an assumption that every fl is1. ActualLF565--625
7a2676 is an ancillary Bergman integrability lemma and INCOMPLETECor1.12
proof; it is not a complete proof of strong openness and is not the G1 route.

These complete author proofs and all exact new primary applications must
be included in updated scoped full review and statement-only targets BEFORE
admission. Historical A--E inputs and old c6c94f source remain preserved;
no completed native result or checked article is changed. Native S10 final
owner71162 continues unchanged. General S11 and all-original closure false.

# Complete actual LF primary context: Demailly-Bergman-1401.5432v2-P18-final.txt, 285--390

```text

1. Approximation of psh functions and of closed (1,1)-currents
   We first recall here the basic result on the approximation of psh functions by psh functions
with analytic singularities. The main idea is taken from [Dem92] and relies on the Ohsawa-
Takegoshi extension theorem, For other applications to algebraic geometry, see [Dem93b] and
Demailly-Kollár [DK01]. Let ϕ be a psh function on an open set Ω ⊂ Cn . Recall that the
Lelong number of ϕ at a point x0 ∈ Ω is defined to be
                                                 ϕ(z)           supB(x0 ,r) ϕ
(1.1)                  ν(ϕ, x0 ) = lim inf                = lim               .
                                    z→x0     log |z − x0 | r→0+    log r
In particular, if ϕ = log |f | with f ∈ O(Ω), then ν(ϕ, x0 ) is equal to the vanishing order
                        ordx0 (f ) = sup{k ∈ N ; Dα f (x0 ) = 0, ∀|α| < k}.

1.2. Theorem. Let ϕ be a plurisubharmonic function on a bounded pseudoconvex open set
Ω ⊂ Cn . For everyR    m > 0, let HΩ (mϕ) be the Hilbert spaceP     of holomorphic functions f
                       2 −2mϕ                                1
on Ω such that Ω |f | e       dV2n < +∞ and let ϕm = 2m log |gm,ℓ |2 where (gm,ℓ ) is an
orthonormal basis of HΩ (mϕ). Then there are constants C1 , C2 > 0 independent of m such
that
             C1                              1    C2
(a) ϕ(z) −       ≤ ϕm (z) ≤ sup ϕ(ζ) +         log n for every z ∈ Ω and r < d(z, ∂Ω). In
              m              |ζ−z|<r        m      r
     particular, ϕm converges to ϕ pointwise and in L1loc topology on Ω when m → +∞ and
              n
(b) ν(ϕ, z) −    ≤ ν(ϕm , z) ≤ ν(ϕ, z) for every z ∈ Ω.
              m
                      P
Proof. (a) Note that       |gm,ℓ(z)|2 is the square of the norm of the evaluation linear form
evz : f 7→ f (z) on HΩ (mϕ), since gm,ℓ (z) = evz (gm,ℓ ) is the ℓ-th coordinate of evz in the
orthonormal basis (gm,ℓ ). In other words, we have
                                  X
                                      |gm,ℓ (z)|2 = sup |f (z)|2
                                                      f ∈B(1)

where B(1) is the unit ball of HΩ (mϕ) (The sum is called the Bergman kernel associated with
HΩ (mϕ)). As ϕ is locally bounded from above, the L2 topology is actually stronger P   than the
topology of uniform convergence on compact subsets of Ω. It follows that the series      |gm,ℓ |2
converges uniformly on Ω and that its sum is real analytic. Moreover, by what we just explained,
we have
                                        1                       1
                     ϕm (z) = sup         log |f (z)|2 = sup      log |f (z)|.
                               f ∈B(1) 2m               f ∈B(1) m

For z0 ∈ Ω and r < d(z0 , ∂Ω), the mean value inequality applied to the psh function |f |2 implies
                                     Z
                         2      1
                |f (z0 )| ≤ n 2n               |f (z)|2 dV2n (z)
                            π r /n! |z−z0 |<r
                                1                            Z
                           ≤ n 2n    exp 2m sup ϕ(z)               |f |2 e−2mϕ dV2n .
                            π r /n!           |z−z0 |<r          Ω
             1. Approximation of psh functions and of closed (1,1)-currents                    7

If we take the supremum over all f ∈ B(1) we get

                                                                   1       1
                             ϕm (z0 ) ≤          sup     ϕ(z) +      log n 2n
                                             |z−z0 |<r            2m    π r /n!

and the second inequality in (a) is proved – as we see, this is an easy consequence of the mean
value inequality. Conversely, the Ohsawa-Takegoshi extension theorem ([OT87]) applied to the
0-dimensional subvariety {z0 } ⊂ Ω shows that for any a ∈ C there is a holomorphic function f
on Ω such that f (z0 ) = a and
                                Z
                                        |f |2 e−2mϕ dV2n ≤ C3 |a|2 e−2mϕ(z0 ) ,
                                    Ω

where C3 only depends on n and diam Ω. We fix a such that the right hand side is 1. Then
kf k ≤ 1 and so we get

                                        1                 1                      C3
                       ϕm (z0 ) ≥         log |f (z0 )| =   log |a| = ϕ(z) − log    .
                                        m                 m                      m

The inequalities given in (a) are thus proved. Taking r = 1/m, we find that

                                           lim         sup   ϕ(ζ) = ϕ(z)
                                         m→+∞ |ζ−z|<1/m


                                                                             1
by the upper semicontinuity of ϕ, and therefore lim ϕm (z) = ϕ(z), since lim m log(C2 mn ) = 0.

(b) The above estimates imply

                                    C1                           1    C2
                 sup       ϕ(z) −      ≤ sup ϕm (z) ≤ sup ϕ(z) +   log n .
               |z−z0 |<r            m   |z−z0 |<r    |z−z0 |<2r  m    r

After dividing by log r < 0 when r → 0, we infer

                              1
         sup|z−z0 |<2r ϕ(z) + m log C2
                                    rn
                                         sup|z−z0 |<r ϕm (z)   sup|z−z0 |<r ϕ(z) − Cm1
                                       ≤                     ≤                         ,
                      log r                    log r                     log r

and from this and definition (1.1), it follows immediately that

                                                  n
                                    ν(ϕ, x) −       ≤ ν(ϕm , z) ≤ ν(ϕ, z).                     
                                                  m


    Theorem 1.2 implies in a straightforward manner the deep result of [Siu74] on the analyticity
```


# Complete actual LF primary context: Demailly-Bergman-1401.5432v2-P18-final.txt, 665--1040

```text
threshold of ϕ with weight f at z0
                        
         cf,z0 (ϕ) = sup c > 0 : |f |2 e−2c ϕ is L1 on a neighborhood of z0 ∈ ]0, +∞].

The special case f = 1 yields the usual log canonical threshold cz0 (ϕ) that was defined in the
introduction. The openness conjectures can be stated as follows.

2.1. Conjectures.
(a) (openness conjecture, [DK01])
    The set {c > 0 : e−2c ϕ is L1 on a neighborhood of z0 equals the open interval ]0, cz0 (ϕ)[.
(b) (strong openness conjecture, [Dem00])
    The set {c > 0 : |f |2 e−2c ϕ is L1 on a neighborhood of z0                 equals the open inter-
    val ]0, cf,z0 (ϕ)[.

   The openness conjecture 2.1 (a) was first established by Favre and Jonsson ([FJ05] in di-
mension 2 (see also [JM12], [JM14]), and 8 years later by Berndtsson [Bern13] in arbitrary
dimension. The strong form 2.1 (b), which is equivalent to Cor. 0.10, was settled very recently
by Guan and Zhou [GZ13]. Their proof uses a sophisticated version of the L2 -extension theo-
rem of Ohsawa and Takegoshi in combination with the curve selection lemma. They have also
obtained related semi-continuity statements in [GZ14a] and “effective versions” in [GZ14b].
A simplified proof along the same lines has been given by Lempert in [Lem14].
   Here, we follow Pham Hoang Hiep’s approach [Hiep14], which is more straightforward and
avoids the curve selection lemma. It is based on the original version [OT87] of the L2 -extension
theorem, applied to members of a standard basis for a multiplier ideal sheaf of holomorphic
functions associated with a plurisubharmonic function ϕ. In this way, by means of a simple
induction on dimension, one can obtain the strong openness conjecture, and give simultaneously
an effective version of the semicontinuity theorem for weighted log canonical thresholds. The
main results are contained in the following theorem.

2.2. Theorem. ([Hiep14]) Let f be a holomorphic function on an open set Ω in Cn and let ϕ
be a psh function on Ω.
                                               R
(i) (“Semicontinuity theorem”) Assume that Ω′ e−2c ϕ dV2n < +∞ on some open subset Ω′ ⊂ Ω
     and let z0 ∈ Ω′ . Then there exists δ = δ(c, ϕ, Ω′ , z0 ) > 0 such that for every ψ ∈ PSH(Ω′ ),
     kψ −ϕkL1 (Ω′ ) ≤ δ implies cz0 (ψ) > c. Moreover, as ψ converges to ϕ in L1 (Ω′ ), the function
     e−2c ψ converges to e−2c ϕ in L1 on every relatively compact open subset Ω′′ ⋐ Ω′ .
                                                  R
(ii) (“Strong effective openness”) Assume that Ω′ |f |2 e−2c ϕ dV2n < +∞ on some open subset
     Ω′ ⊂ Ω. When ψ ∈ PSH(Ω′ ) converges to ϕ in L1 (Ω′ ) with ψ ≤ ϕ, the function |f |2 e−2c ψ
     converges to |f |2 e−2c ϕ in L1 norm on every relatively compact open subset Ω′′ ⋐ Ω′ .

2.3. Corollary. (“Strong openness”). For any plurisubharmonic function ϕ on a neighborhood
of a point z0 ∈ Cn , the set {c > 0 : |f |2 e−2c ϕ is L1 on a neighborhood of z0 } is an open
interval (0, cf,z0 (ϕ)).
        2. Semi-continuity of psh singularities and proof of the strong openness conjecture                13

2.4. Corollary. (“Convergence from below”). If ψ ≤ ϕ converges to ϕ in a neighborhood of
z0 ∈ Cn , then cf,z0 (ψ) ≤ cf,z0 (ϕ) converges to cf,z0 (ϕ).

    In fact, after subtracting a large constant to ϕ, we can assume ϕ ≤ 0 in both corollaries.
Then Cor. 2.3 is a consequence of assertion (ii) of the main theorem when we take Ω′ small
enough and ψ = (1 + δ)ϕ with δ ց 0. In Cor. 2.4, we have by definition cf,z0 (ψ) ≤ cf,z0 (ϕ)
for ψ ≤ ϕ, but again (ii) shows that cf,z0 (ψ) becomes ≥ c for any given value c ∈ (0, cf,z0 (ϕ)),
whenever kψ − ϕkL1 (Ω′ ) is sufficiently small.

2.5. Remark. One cannot remove condition ψ ≤ ϕ in assertion (ii) of the main theorem.
Indeed, choose f (z) = z1 , ϕ(z) = log |z1 | and ϕj (z) = log |z1 + zj2 |, for j ≥ 1.One has ϕj → ϕ
in L1loc (Cn ), however cf,0 (ϕj ) = 1 < cf,0 (ϕ) = 2 for all j ≥ 1. On the other hand, condition (i)
of Theorem 2.2 does not require any given inequality between ϕ and ψ. Modulo Berndtsson’s so-
lution of the openness conjecture, (i) follows from the effective semicontinuity result of [DK01],
but (like Guan and Zhou) Hiep’s technique will reprove both by a direct and easier method.

2.6. A few preliminaries. According to standard techniques in the theory of Gröbner bases,
one equips the ring OCn ,0 of germs of holomorphic functions at 0 with the homogeneous lexi-
cographic order of monomials z α = z1α1 . . . znαn , that is, z1α1 . . . znαn < z1β1 . . . znβn if and only if
|α| = α1 +. . .+αn < |β| = β1 +. . .+βn or |α| = |β| and αi < βi for the first index i with αi 6= βi .
                          1        2                                           1        2
For each f (z) = aα1 z α + aα2 z α + . . . with aαj 6= 0, j ≥ 1 and z α < z α < . . . , we define
the initial coefficient, initial monomial and initial term of f to be respectively IC(f ) = aα1 ,
             1                  1                                                     1       2
IM(f ) = z α , IT(f ) = aα1 z α , and the support of f to be SUPP(f ) = {z α , z α , . . .}. For any
ideal I of OCn ,0 , we define IM(I) to be the ideal generated by {IM(f )}{f ∈I} . First, we recall
the division theorem of Hironaka and the concept of standard basis of an ideal.

2.7. Theorem. (Division theorem of Hironaka, [Gal79], [Bay82], [BM87], [BM89], [Eis95]) Let
f, g1 , . . . , gk ∈ OCn ,0 . Then there exist h1 , . . . , hk , s ∈ OCn ,0 such that

                                       f = h1 g1 + . . . + hk gk + s,

and SUPP(s)∩hIM(g1 ), . . . , IM(gk )i = ∅, where hIM(g1 ), . . . , IM(gk )i denotes the ideal generated
by the family (IM(g1 ), . . . , IM(gk )).

2.8. Standard basis of an ideal. Let I be an ideal of OCn ,0 and let g1 , . . . , gk ∈ I be such
that IM(I) = hIM(g1 ), . . . , IM(gk )i. Take f ∈ I. By the division theorem of Hironaka, there
exist h1 , . . . , hk , s ∈ OCn ,0 such that

                                       f = h1 g1 + . . . + hk gk + s,

and SUPP(s) ∩ IM(I) = ∅. On the other hand, since s = f − h1 g1 + . . . + hk gk ∈ I, we have
IM(s) ∈ IM(I). Therefore s = 0 and the gj ’s are generators of I. By permuting the gj ’s and
performing ad hoc subtractions, we can always arrange that IM(g1 ) < IM(g2 ) < . . . < IM(gk ),
and we then say that (g1 , . . . , gk ) is a standard basis of I.

Th. 2.2 will be proved by induction on dimension n. All statements are trivial for n = 0.
Assume that the theorem holds for dimension n − 1. Thanks to the L2 -extension theorem of
Ohsawa and Takegoshi ([OT87]), one obtains the following key lemma.
14                 Jean-Pierre Demailly, On the cohomology of pseudoeffective line bundles

2.9. Lemma. Let ϕ ≤ 0 be a plurisubharmonic function and f be a holomorphic function on
the polydisc ∆nR of center 0 and (poly)radius R > 0 in Cn , such that for some c > 0
                              Z
                                   |f (z)|2 e−2c ϕ(z) dV2n (z) < +∞.
                                     ∆n
                                      R


Let ψj ≤ 0, j ≥ 1, be a nequence of plurisubharmonic functions on ∆nR with ψj → ϕ in
L1loc (∆nR ), and assume that either f = 1 identically or ψj ≤ ϕ for all j ≥ 1. Then for
every r < R and ε ∈ (0, 12 r], there exist a value wn ∈ ∆ε r {0}, an index j0 , a constant
c̃ > c and a sequence of holomorphic
                           P                functions Fj on ∆nr , j ≥ j0 , such that IM(Fj ) ≤ IM(f ),
Fj (z) = f (z) + (zn − wn ) aj,α z α with |wn ||aj,α | ≤ r −|α| ε for all α ∈ Nn , and
                     Z
                                                             ε2
                         |Fj (z)|2 e−2c̃ ψj (z) dV2n (z) ≤        < +∞, ∀j ≥ j0 .
                      ∆n
                       r
                                                           |wn |2

Moreover, one can choose wn in a set of positive measure in the punctured disc ∆ε r {0} (the
index j0 = j0 (wn ) and the constant c̃ = c̃(wn ) may then possibly depend on wn ).
Proof. By Fubini’s theorem we have
               Z Z                                                  
                                ′       2 −2c ϕ(z ′ ,zn )          ′
                           |f (z , zn )| e                dV2n−2 (z ) dV2 (zn ) < +∞.
                             n−1
                    ∆R      ∆R

Since the integral extended to a small disc zn ∈ ∆η tends to 0 as η → 0, it will become smaller
than any preassigned value, say ε20 > 0, for η ≤ η0 small enough. Therefore we can choose a
set of positive measure of values wn ∈ ∆η r {0} such that
                    Z
                               ′       2 −2c ϕ(z ′ ,wn )          ′     ε20     ε20
                          |f (z , wn )| e                dV2n−2 (z ) ≤      <        .
                      n−1
                     ∆R                                                πη 2   |wn |2

Since the main theorem is assumed to hold for n − 1, for any ρ < R there exist j0 = j0 (wn ) and
c̃ = c̃(wn ) > c such that
                   Z
                                                      ′                        ε20
                          |f (z ′ , wn )|2 e−2c̃ ψj (z ,wn ) dV2n−2 (z ′ ) <        , ∀j ≥ j0 .
                      n−1
                     ∆ρ                                                      |wn |2

(For this, one applies part (i) in case f = 1, and part (ii) in case ψj ≤ ϕ, using the fact that
ψ = cc̃ ψj converges to ϕ as c̃ → c and j → +∞). Now, by the L2 -extension theorem of Ohsawa
and Takegoshi (see [OT87]), there exists a holomorphic function Fj on ∆n−1                  ρ    × ∆R such that
Fj (z ′ , wn ) = f (z ′ , wn ) for all z ′ ∈ ∆n−1
                                               ρ    , and
      Z                                                       Z
                                                                                            ′
                              2 −2c̃ ψj (z)                 2
                    |Fj (z)| e              dV2n (z) ≤ Cn R     |f (z ′ , wn )|2 e−2c̃ ψj (z ,wn ) dV2n−2 (z ′ )
        n−1                                                  n−1
       ∆ρ   ×∆R                                             ∆ρ

                                                    Cn R2 ε20
                                                ≤             ,
                                                     |wn |2
where Cn is a constant which only depends on n (the constant is universal for R = 1 and is
rescaled by R2 otherwise). By the mean value inequality for the plurisubharmonic function
|Fj |2 , we get
                                                        Z
                     2                1
             |Fj (z)| ≤ n           2                 2
                                                                                        |Fj |2 dV2n
                       π (ρ − |z1 |) . . . (ρ − |zn |) ∆ρ−|z | (z1 )×...×∆ρ−|zn | (zn )
                                                                    1

                                    Cn R2 ε20
                      ≤ n                                       ,
                       π (ρ − |z1 |)2 . . . (ρ − |zn |)2 |wn |2
         2. Semi-continuity of psh singularities and proof of the strong openness conjecture          15

where ∆ρ (z) is the disc of center z and radius ρ. Hence, for any r < R, by taking ρ = 21 (r + R)
we infer
                                                                1
                                                         2n Cn2 Rε0
(2.10)                               kFj kL∞ (∆nr ) ≤ n                 .
                                                     π 2 (R − r)n |wn |

Since Fj (z ′ , wn ) − f (z ′P
                             , wn ) = 0, ∀z ′ ∈ ∆n−1
                                                 r   , we can write Fj (z) = f (z) + (zn − wn )gj (z) for
                                          α        n−1
some function gj (z) = α∈Nn aj,α z on ∆r × ∆R . By (2.10), we get

                                                 1                                     
               kgj k∆nr = kgj k∆rn−1 ×∂∆r ≤              kFj kL∞ (∆nr ) + kf kL∞ (∆nr )
                                              r − |wn |
                                                                  1
                                                 1          2n Cn2 Rε0                     
                                            ≤              n                +  kf k L (∆r ) .
                                                                                     ∞    n
                                              r − |wn | π 2 (R − r)n |wn |

Thanks to the Cauchy integral formula, we find
                                                                1
                           kgj k∆nr         1             2n Cn2 Rε0                    
                 |aj,α | ≤          ≤                    n                + kf kL∞ (∆nr ) .
                             r |α|    (r − |wn |)r |α| π 2 (R − r)n |wn |

We take in any case η ≤ ε0 ≤ ε ≤ 21 r. As |wn | < η ≤ 12 r, this implies
                                                   1
                                          2  2n Cn2 Rε0                        
                     |wn ||aj,α | r |α| ≤     n          + kf k L ∞ (∆n ) |wn |   ≤ C ′ ε0 ,
                                          r π 2 (R − r)n              r



for some constant C ′ depending only on n, r, R and f . This yields the estimates of Lemma 2.9
for ε0 := C ′′ ε with C ′′ sufficiently small. Finally, we prove that IM(Fj ) ≤ IM(f ). Indeed, if
IM(gj ) ≥ IM(f ), since |wn kaj,α | ≤ r −|α| ε, we can choose ε small enough such that IM(Fj ) =
            IC(Fj )
IM(f ) and            ∈ ( 21 , 2). Otherwise, if IM(gj ) < IM(f ), we have IM(Fj ) = IM(gj ) < IM(f ).
             IC(f )


2.11. Proof of Theorem 2.2. By well-known properties of (pluri)potential theory, the L1
convergence of ψ to ϕ implies that ψ → ϕ almost everywhere, and the assumptions guarantee
that ϕ and ψ are uniformly bounded on every relatively compact subset of Ω′ . In particular,
after shrinking Ω′ and subtracting constants, we can assume that ϕ ≤ 0 on Ω. Also, since the
L1 topology is metrizable, it is enough to work with a sequence (ψj )j≥1 converging to ϕ in
L1 (Ω′ ). Again, we can assume that ψj ≤ 0 and that ψj → ϕ almost everywhere on Ω′ . By a
trivial compactness argument, it is enough to show (i) and (ii) for some neighborhood Ω′′ of a
given point z0 ∈ Ω′ . We assume here z0 = 0 for simplicity of notation, and fix a polydisc ∆nR of
center 0 with R so small that ∆nR ⊂ Ω′ . Then ψj (•, zn ) → ϕ(•, zn ) in the topology of L1 (∆n−1R )
for almost every zn ∈ ∆R .
                                                                                   R
2.11 (i). Proof of statement (i) in Theorem 2.2. We have here ∆n e−2c ϕ dV2n < +∞
                                                                                     R
for R > 0 small enough. By Lemma 2.9 with f = 1, for every r < R and ε > 0, there exist
wn ∈ ∆ε r {0}, an index j0 , a number c̃ > P          c and a sequence of holomorphic functions Fj on
∆r , j ≥ j0 , such that Fj (z) = 1 + (zn − wn ) aj,α z α , |wn ||aj,α | r −|α| ≤ ε and
  n

                        Z
                                                                  ε2
                              |Fj (z)|2 e−2c̃ ψj (z) dV2n (z) ≤        , ∀j ≥ j0 .
                          ∆nr
                                                                |wn |2

For ε ≤ 12 , we conclude that |Fj (0)| = |1−wn aj,0 | ≥ 21 hence c0 (ψj ) ≥ c̃ > c and the first part of
(i) is proved. In fact, after fixing such ε and wn , we even obtain the existence of a neighborhood
16                     Jean-Pierre Demailly, On the cohomology of pseudoeffective line bundles
                                                                                    R
Ω′′ of 0 on which |Fj | ≥ 14 , and thus get a uniform bound                             Ω′′
                                                                                              e−2c̃ ψj (z) dV2n (z) ≤ M < +∞.
The second assertion of (i) then follows from the estimate
         Z                                              Z
               −2c ψj (z)       −2c ϕ(z)
               e            −e             dV2n (z) ≤                           e−2c ψj (z) − e−2c ϕ(z) dV2n (z)
         Ω′′                                                Ω′′ ∩{|ψ   j |≤A}
                                                                Z
                                                            +                           e−2c ϕ(z) dV2n (z)
                                                                    Ω′′ ∩{ψj <−A}
                                                                                Z
                                                                 −2(c̃−c)A
                                                            +e                                         e−2c̃ ψj (z) dV2n (z).
                                                                                 Ω′′ ∩{ψ      j <−A}



In fact the last two terms converge to 0 as A → +∞, and, for A fixed, the first integral in
the right hand side converges to 0 by Lebesgue’s bounded convergence theorem, since ψj → ϕ
almost everywhere on Ω′′ .
2.11 (ii). Proof of statement (ii) in Theorem 2.2. Take f1 , . . . , fk ∈ OCn ,0 such that
(f1 , . . . , fk ) is a standard basis of I(c ϕ)0 with IM(f1 ) < . . . < IM(fk ), and ∆nR a polydisc so
small that                   Z
                                 |fl (z)|2 e−2c ϕ(z) dV2n (z) < +∞, l = 1, . . . , k.
                               ∆n
                                R


Since the germ of f at 0 belongs to the ideal (f1 , . . . , fk ), we can essentially argue with the fl ’s
instead of f . By Lemma 2.9, for every r < R and εl > 0, there exist wn,l ∈ ∆εl r {0}, an index
j0 = j0 (wn,l ), a number c̃ = c̃(wn,l ) > c and
                                              P a sequence        of holomorphic functions Fj,l on ∆nr ,
j ≥ j0 , such that Fj,l (z) = 1 + (zn − wn,l ) aj,l,α z α , |wn,l ||aj,l,α | r −|α| ≤ εl and
                   Z
                                                                  ε2l
(2.12)                   |Fj,l (z)|2 e−2c̃ ψj (z) dV2n (z) ≤             ,      ∀l = 1, . . . , k, ∀j ≥ j0 .
                   ∆n
                    r
                                                                |wn,l |2

Since ψj ≤ ϕ and c̃ > c, we get Fj,l ∈ I(c̃ ψj )0 ⊂ I(c ϕ)0 . The next step of the proof consists
in modifying (Fj,l )1≤l≤k in order to obtain a standard basis of I(c ϕ)0 . For this, we proceed
by selecting successively ε1 ≫ ε2 ≫ . . . ≫ εk (and suitable wn,l ∈ ∆εl r {0}). We have
IM(Fj,1 ), . . . , IM(Fj,k ) ∈ IM(I(c ϕ)0 , in particular IM(Fj,1 ) is divisible by IM(fl ) for some l =
1, . . . , k. Since IM(Fj,1 ) ≤ IM(f1 ) < . . . < IM(fk ), we must have IM(Fj,1 ) = IM(f1 ) and
                                                                              IC(Fj,1 )
thus IM(gj,1 ) ≥ IM(f1 ). As |wn,1 ||aj,1,α| ≤ ε1 , we will have                        ∈ ( 12 , 2) for ε1 small
                                                                               IC(f1 )
enough. Now, possibly after changing ε2 to a smaller value, we show that there exists a
polynomial Pj,2,1 such that the degree and coefficients of Pj,2,1 are uniformly bounded, with
                                          | IC(Fj,2 − Pj,2,1 Fj,1 )|
IM(Fj,2 − Pj,2,1 Fj,1 ) = IM(f2 ) and                                ∈ ( 21 , 2). We consider two cases:
                                                 | IC(f2 )|

Case 1: If IM(gj,2 ) ≥ IM(f2 ), since |wn,2 ||aj,2,α | ≤ r −|α| ε2 , we can choose ε2 so small that
                        | IC(Fj,2 )|
IM(Fj,2 ) = IM(f2 ) and              ∈ ( 12 , 2). We then take Pj,2,1 = 0.
                         | IC(f2 )|

Case 2: If IM(gj,2 ) < IM(f2 ), we have IM(gj,2 ) = IM(Fj,2 ) ∈ IM(I(c ϕ)0 ). Hence IM(gj,2 ) is
divisible by IM(fl ) for some l = 1, . . . , k. However, since IM(gj,2 ) < IM(f2 ) < . . . < IM(fk ),
the only possibility is that IM(gj,2 ) be divisible by IM(f1 ). Take b ∈ C and β, γ ∈ Nn such that
IT(gj,2 ) := aj,2,γ z γ = bz β IT(Fj,1 ). We have z β ≤ z γ = IM(gj,2 ) < IM(f2 ) and

                                                 | IC(gj,2 )|   2|wn,2 ||aj,2,γ |   2r −|γ| ε2
                          |wn,2 ||b| = |wn,2 |                ≤                   ≤
                                                 | IC(Fj,1 )|     | IC(f1 )|        | IC(f1 )|
                 3. Hard Lefschetz theorem for pseudoeffective line bundles                                                   17

                                                                                          P
can be taken arbitrarily small. Set g̃j,2 (z) = gj,2 (z) − bz β Fj,1 (z) =                    ãj,2,α z α and

               F̃j,2 (z) = f2 (z) + (zn − wn,2 )g̃j,2 (z) = Fj,2 (z) − b(zn − wn,2 )z β Fj,1 (z).

We have IM(g̃j,2 ) > IM(gj,2 ). Since |wn,2 ||b| = O(ε2 ) and |wn,2 ||aj,2,α | = O(ε2 ), we get
|wn,2 ||ãj,2,α| = O(ε2 ) as well. Now, we consider two further cases. If IM(g̃j,2 ) ≥ IM(f2 ), we can
                                                                             | IC(F̃j,2 )|
again change ε2 for a smaller value so that IM(F̃j,2 ) = IM(f2 ) and                       ∈ ( 21 , 2). Other-
                                                                               | IC(f2 )|
wise, if IM(g̃j,2 ) < IM(f2 ), we have IM(Fj,2 ) = IM(gj,2 ) < IM(F̃j,2 ) = IM(g̃j,2 ) < IM(f2 ). No-
tice that {z γ : z γ < IM(f2 )} is a finite set. By using similar arguments a finite number of times,
we                         find                     ε2                       so                          small
                                                | IC(Fj,2 − Pj,2,1 Fj,1 )|     1
that IM(Fj,2 − Pj,2,1 Fj,1 ) = IM(f2 ) and                                 ∈ ( 2 , 2) for some polynomial
                                                       | IC(f2 )|
Pj,2,1 . Repeating the same arguments for Fj,3 , . . . , Fj,k , we select inductively εl , l = 1, . . . , k,
and construct linear combinations
                                                     X
                                      ′                              ′
                                    Fj,l = Fj,l −           Pj,l,m Fj,m
                                                       1≤m≤l−1


with polynomials Pj,l,m , 1 ≤ m < l ≤ k, possessing uniformly bounded coefficients and degrees,
                                                  ′
                                           | IC(Fj,l )|
such that IM(Fj,l    ′
                         ) = IM(fl ) and                ∈ ( 21 , 2) for all l = 1, . . . , k and j ≥ j0 . This implies
                                            | IC(fl )|
        ′              ′
that (Fj,1 , . . . , Fj,k  ) is also a standard basis of I(c ϕ)0 . By Theorem 1.2.2 in [Gal79], we can
find ρ, K > 0 so small that there exist holomorphic functions hj,1 , . . . , hj,k on ∆nρ with ρ < r,
such that
                                            ′           ′                     ′
                                 f = hj,1 Fj,1 + hj,2 Fj,2 + . . . + hj,k Fj,k     on ∆nρ
and khj,l kL∞ (∆nρ ) ≤ Kkf kL∞ (∆nr ) , for all l = 1, . . . , k (ρ and K only depend on f1 , . . . , fk ). By
(2.12)), this implies a uniform bound
                             Z
                                  |f (z)|2 e−2c̃ ψj (z) dV2n (z) ≤ M < +∞
                                   ∆n
                                    ρ



for some c̃ > c and all j ≥ j0 . Take Ω′′ = ∆nρ . We obtain the L1 convergence of |f |2 e−2c ψj to
|f |2 e−2c ϕ almost exactly as we argued for the second assertion of part (i), by using the estimate
    Z                                           Z
             2 −2c ψj (z)   −2c ϕ(z)
         |f | e           −e         dV2n (z) ≤            |f |2 e−2c ψj (z) − e−2c ϕ(z) dV2n (z)
     Ω′′                                               Ω′′ ∩{|ψj |≤A}
                                                            Z
                                                        +                          |f |2 e−2c ϕ(z) dV2n (z)
                                                                Ω′′ ∩{ψ   j <−A}
                                                                            Z
                                                            −2(c̃−c)A
                                                        +e                                     |f |2 e−2c̃ ψj (z) dV2n (z).
                                                                             Ω′′ ∩{ψj <−A}


```

# Exact new primary applications and source/input boundaries

```json
{
  "recorded_at_utc": "2026-10-08T17:56:52.553274+00:00",
  "current_source": "papers/S11-zero-Lelong-residuals-and-blowups-at-poles.tex",
  "current_source_sha256": "a5765fc8c763ba6fe284f710a335454cd6ff2deadff4727e2cf411e12de4b490",
  "entire_current_source_actually_root_read_chunk": "019e8a",
  "old_source_preserved": "checks/S11-small-curvature-before-ideal-trace-strengthening-20261008-source.tex",
  "old_source_sha256": "c6c94f9d74b02b6db9e86be419364385e95173df381ca07123da641ee22ec840",
  "old_argument_preserved": "notes/S11-small-curvature-pole-center-extension-20261008-full-review-LF-and-applications-argument.md",
  "old_argument_sha256": "e52f694bf3d98b4f0ba44f5ba386ba1ac53bb4f096ab8cea2b1ab2d668827444",
  "current_scoped_task": "inputs/S11-small-curvature-ideal-traces-20261008-scoped-full-review-task.json",
  "current_scoped_task_sha256": "cbb6eae3df4d37d43a42ecb78e9308f88271a33f12910ca1d149e31361351018",
  "current_cold_input": "inputs/S11-small-curvature-ideal-traces-20261008-statement-only-input.json",
  "current_cold_input_sha256": "d1a1b3d050c88f7a41098f96089459314760f922d2b1d73a5d3e6b7c9909d531",
  "whole_current_task_and_cold_input_root_read_pending": true,
  "cold_notes_empty_and_nested_original_exactly_unchanged": true,
  "scoped_A_G_task_not_byte_identical_original": true,
  "actual_primary_contexts": [
    {
      "path": "inputs/primary/Demailly-Bergman-1401.5432v2-P18-final.txt",
      "source_sha256": "0422606a9759a972825839c865bce72241b063bc6261276f862497e628a80dd6",
      "actual_LF_range": [
        285,
        390
      ],
      "actual_full_byte_comparison_with_sed": true,
      "entire_current_context_root_read_chunks": [
        "310b60"
      ],
      "whole_context_root_read_pending": false
    },
    {
      "path": "inputs/primary/Demailly-Bergman-1401.5432v2-P18-final.txt",
      "source_sha256": "0422606a9759a972825839c865bce72241b063bc6261276f862497e628a80dd6",
      "actual_LF_range": [
        665,
        1040
      ],
      "actual_full_byte_comparison_with_sed": true,
      "entire_current_context_root_read_chunks": [
        "cfa861",
        "334820"
      ],
      "whole_context_root_read_pending": false
    }
  ],
  "individual_new_application_assessment": {
    "F": "The positive smooth pullback pi*h is bounded above by C*h prime on compact source; actual quasi-psh pullbacks are nontrivial canonical functions. Pointwise same-type inequalities pull back including poles. Choosing delta arbitrarily small gives the exact same-type hypothesis upstairs. Apply the previously authored E, not a generic pullback zero-Lelong theorem.",
    "G_integrability": "Apply exact Bergman Theorem1.2 to a local corrected psh phi, every m>0, not a global nonclosed current. Zero point Lelong forces the weighted Hilbert evaluation nonzero; its unit-ball derivative bound follows from phi bounded ABOVE and standard mean-value/Cauchy. The actual nonvanishing weighted function gives exp(-2m phi) integrable near the point. Set2m=s. No kernel positivity or arbitrary pole restriction is presumed.",
    "G_ideal_neutrality": "Strong openness applies to the corrected psh v and fixed holomorphic germ g. The source parameter c=t/2 gives p>1 with exp(-p t v) weighted integrability. With p conjugate p prime, the exact two factors each carry |g|^2, producing |g|^2 after Holder. The second factor is integrable from G integrability and bounded g. Local upper q proves the other inclusion. Every smooth correction is bounded on the shrunken domain.",
    "G_intrinsic_trace": "Ambient ideal equality is first proved for all divisors. ONLY the explicit SNC trace formula uses the normal-crossing monomial calculation. Minimum order floor(t*a) has strict exponent>-2, with integer boundary failure at the next smaller order. Y contained in no positive component makes each relevant local restricted equation nonzero, hence finite orders after every smooth compact modification. The finite sum of floors divided by t has the exact stated limit. Ambient-ideal restriction is used even if the naive q restriction is minus infinity.",
    "inherited_boundary": "Complete printed Theorem1.2 and Section2 proof chains were actually read; Ohsawa--Takegoshi and standard-basis/analytic division theory remain attributed imported foundations, not recursively certified. Printed2.11 uniform bounds are used ABOVE; its displayed1 in Fj,l is the fl of Lemma2.9 and subsequent decomposition. Ancillary incomplete Cor1.12 context is not a strong-openness proof grant."
  },
  "all_prior_six_complete_support_components_preserved_except_disclosed_current_source": true,
  "whole_aggregate_argument_display_claimed": false,
  "current_build": "checks/S11-small-curvature-ideal-traces-strengthened-20261008-build.json",
  "all_current_pages_root_view_pending": true,
  "native_compiler_actual_cell": "738",
  "native_compilation_verified": false,
  "native_admission": false,
  "native_owner_unchanged": 71162,
  "mathematical_acceptance": false,
  "original_S11_completed": false,
  "published": false
}
```

# Explicit zero-coefficient convention

Only positive-coefficient divisor components enter the restricted equations and intrinsic-order sums. This avoids restricting an unused equation that may vanish identically on Y, and never uses zero times an infinite order. All earlier unadmitted source and inputs are preserved.
