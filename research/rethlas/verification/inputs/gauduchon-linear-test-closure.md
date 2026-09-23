Run_id: gauduchon_linear_test_closure_01

Statement: Verify the complete elementary current-duality supplement below and its three downstream applications. The setting is a connected compact complex manifold, n>=2 except that the zero-degree lemma explicitly includes n=1. Backgrounds theta may be nonclosed. There is no bounded or positive-lower Monge-Ampere mass assumption. This is a focused check, not a novelty claim or whole-book certification.

Accepted already proved book inputs: the conformal Gauduchon theorem; the root identification of smooth strictly positive (n-1,n-1)-forms with powers of Hermitian metrics for n>=2; generalized Lamari: PSH(X,theta) nonempty iff every smooth strictly positive dd^c-closed (n-1,n-1) form pairs nonnegatively with theta; the threshold corollary kappa_omega(theta)=max{a: theta+dd^c u>=a omega for some qpsh u}, with attainment by a current; and the smooth-cone theorem m_h(theta)=min over all normalized positive dd^c-closed test currents of integral theta wedge T, detecting smooth positivity by m>0 and nefness by m>=0. These internal results are accepted inputs, not external references to be rediscovered. Classical positive-current coefficient measures, weak compactness of finite measures, Hahn-Banach separation and scalar elliptic regularity may be used, but their applications here must be checked explicitly.

Review every statement and deduction: n=1 in the zero-degree lemma; current Stokes and elliptic upgrade; smooth minimizer characterization using the attained primal threshold; compactness/metrizability and convexity of the two current sets; exact weak topology for separation by a smooth real (1,1)-form; the polar characterization involving ALL smooth possibly nonclosed pseudoeffective backgrounds; uniform topology Lipschitz bound and minimizer stability. Do not conflate the closure of smooth positive tests with all positive dd^c-closed currents. Never multiply two nonsmooth currents.

The three downstream applications are: (1) in the variational volume chapter, for pseudoeffective theta with lambda_mu(theta)=0, positivity of its denominator reduces smooth attainment to the zero-degree lemma in every n>=1; (2) m_h(theta)<=kappa_h(theta) because C_h is a subset of G_h; (3) on the blowup of P2 at one point, an exceptional curve C with C^2=-1 and a Kahler omega gives T_C=[C]/integral_C omega in G_omega, pairing with a smooth closed class representative beta_C equal to -1/integral_C omega. Every smooth positive test pairs as integral_C T>0 by Poincare-Lelong. Thus T_C is outside C_omega and m_omega(beta_C)<0<=kappa_omega(beta_C). Check these implications; standard exceptional intersection and Poincare-Lelong are the accepted classical geometric inputs already proved in the book. The existing nonlinear determinant duality is unchanged and is not being reverified.

Use the normal local verification instructions and tools. Write only new records for this run; never edit book sources, original references, old verifier records or installation. Finish by saving the normal verification.json report.

Proof:
```latex
The next observation also holds in dimension one, with $\gamma^{n-1}=1$.

\begin{lemma}\label{lem:zero-gauduchon-degree}
Let $\theta$ be a smooth real $(1,1)$-form with $\PSH(X,\theta)\ne\varnothing$.
If
\[
 \int_X\theta\wedge\gamma^{n-1}=0
\]
for one Gauduchon metric $\gamma$, then $\theta=\ddc f$ for a smooth real
function $f$. Conversely, a smoothly $\ddc$-exact form has zero degree
against every Gauduchon metric.
\end{lemma}
\begin{proof}
Choose $u\in\PSH(X,\theta)$ and set $S=\theta+\ddc u\geq0$.
Current Stokes gives $\int_XS\wedge\gamma^{n-1}=0$.
The trace measure of a positive current controls all its coefficient
measures, so $S=0$. Thus $\ddc u=-\theta$ is smooth. Taking the trace
with a fixed Hermitian metric gives a scalar elliptic equation with
smooth right-hand side. Elliptic regularity makes $u$ smooth, and
$f=-u$ has the required property. The converse is Stokes' theorem.
For $n=1$, the trace measure is simply $S$ itself and the same proof applies.
\end{proof}

Put $a=\kappa_\omega(\theta)$. By \cref{cor:gauduchon-threshold},
$\theta-a\omega$ admits a positive current. Hence
\cref{lem:zero-gauduchon-degree} shows that the infimum defining
$\kappa_\omega(\theta)$ is attained by a smooth Gauduchon metric if and
only if
\[
 \theta-a\omega=\ddc f\quad\text{for some }f\in C^\infty(X,\mathbb R).
\]
In that case every Gauduchon metric attains it. The positive current at
the threshold always exists; a smooth minimizing test is much more restrictive.

\section{Compactness of normalized tests}
\label{sec:gauduchon-linear-duality}

Fix a Hermitian form $\omega$ and let
\[
 \mathscr G_\omega=
 \left\{T\geq0:\ T\text{ has bidegree }(n-1,n-1),\quad
       \ddc T=0,\quad\int_X\omega\wedge T=1\right\}.
\]
These are the normalized Gauduchon currents. Let $\mathscr C_\omega$
be the weak closure of the smooth strictly positive members of
$\mathscr G_\omega$. The root calculation in the proof of
\cref{thm:lamari} identifies those members with normalized powers of
Gauduchon metrics. All pairings below involve a current and a smooth
form; no product of two currents is used.

\begin{proposition}\label{prop:gauduchon-linear-compact-dual}
The sets $\mathscr G_\omega$ and $\mathscr C_\omega$ are nonempty,
compact and convex. For every smooth real $(1,1)$-form $\theta$,
\begin{equation}\label{eq:gauduchon-linear-minimum}
 \kappa_\omega(\theta)
   =\min_{T\in\mathscr C_\omega}\int_X\theta\wedge T.
\end{equation}
Moreover, for $T\in\mathscr G_\omega$, membership in
$\mathscr C_\omega$ is equivalent to
\begin{equation}\label{eq:gauduchon-linear-polar}
 \int_X\theta\wedge T\geq0
 \quad\text{for every smooth real }\theta
       \text{ with }\PSH(X,\theta)\ne\varnothing.
\end{equation}
\end{proposition}
\begin{proof}
Gauduchon's theorem supplies a smooth positive member after normalization.
The fixed trace mass bounds the total variation of all coefficient
measures in finitely many local frames. Weak compactness of finite
measures therefore gives compactness of the family of positive currents
with this trace. Positivity, the trace normalization and $\ddc T=0$
pass to limits. On this bounded set, testing against smooth forms or
against continuous coefficient forms gives the same topology, by
uniform approximation. It is metrizable since the continuous test
space is separable. Thus the compactness can also be used sequentially.
The defining conditions of $\mathscr G_\omega$ are convex. Its smooth
strictly positive members form a convex set, so their closure
$\mathscr C_\omega$ is compact and convex as well.

Pairing with a fixed smooth $\theta$ is continuous. Its minimum on the
closure of the smooth tests is therefore their infimum, proving
\eqref{eq:gauduchon-linear-minimum}. The Lamari criterion shows that
\eqref{eq:gauduchon-linear-polar} holds for every smooth positive test,
and hence for every member of its weak closure.

Conversely, if $T\notin\mathscr C_\omega$, separate this point from the
compact convex set $\mathscr C_\omega$ in the weak space of currents.
A continuous linear functional for that weak topology is evaluation
against a smooth form. After changing its sign if necessary, there is
a smooth real $(1,1)$-form $\beta$ such that
\[
 \int_X\beta\wedge T
 <\min_{R\in\mathscr C_\omega}\int_X\beta\wedge R
 =\kappa_\omega(\beta).
\]
By \cref{cor:gauduchon-threshold}, the smooth form
$\beta-\kappa_\omega(\beta)\omega$ admits a positive current.
Its pairing with $T$ is negative because $\int_X\omega\wedge T=1$.
This contradicts \eqref{eq:gauduchon-linear-polar} and proves the converse.
\end{proof}

\begin{corollary}\label{cor:gauduchon-threshold-continuity}
The function $\kappa_\omega$ is concave, positively homogeneous and
invariant under addition of $\ddc f$ for smooth real $f$. If
$-\varepsilon\omega\leq\theta-\eta\leq\varepsilon\omega$, then
\[
 |\kappa_\omega(\theta)-\kappa_\omega(\eta)|\leq\varepsilon.
\]
If smooth forms $\theta_j$ converge uniformly to a smooth form $\theta$
and $T_j\in\mathscr C_\omega$ minimize their pairings, every weak
cluster point of $(T_j)$ minimizes the pairing with $\theta$.
\end{corollary}
\begin{proof}
Formula \eqref{eq:gauduchon-linear-minimum} is an infimum of linear
functionals, which proves concavity and positive homogeneity.
Gauge invariance follows from $\ddc T=0$. The normalized trace gives
\[
 \left|\int_X(\theta-\eta)\wedge T\right|\leq\varepsilon
 \quad(T\in\mathscr C_\omega),
\]
and taking infima proves the estimate. For the last assertion, pass to
a subsequence $T_j\rightharpoonup T\in\mathscr C_\omega$.
The estimate and uniform convergence of the backgrounds give
\[
 \int_X\theta\wedge T
 =\lim_j\int_X\theta_j\wedge T_j
 =\lim_j\kappa_\omega(\theta_j)=\kappa_\omega(\theta).
\]
Thus $T$ is a minimizer.
\end{proof}

The closure $\mathscr C_\omega$ cannot in general be replaced by all of
$\mathscr G_\omega$. The exceptional-curve example in
\cref{ex:gauduchon-current-smoothing-obstruction} separates the two
sets by a smooth closed form. Testing against all of $\mathscr G_\omega$
will instead detect smooth positivity and nefness in
\cref{thm:smooth-cone-current-duality}. These compactness statements
control linear current masses and require no Monge--Amp\`ere mass bound.

```
