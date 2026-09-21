Run_id: divisorial_residual_families_01

Statement: Verify the finite-divisor parameter-family proposition and following multiplier-ideal calculation in research/editorial/section_divisorial_residual_families.tex. This is a candidate addition after the finite-divisor residual equation, outside checked checkpoint55. Use the normal verification workflow. Do not manually edit any frozen submission, existing result or memory. No novelty or new external-source claim is made.

Context: X is a connected compact complex manifold of dimension n>=1, theta is an arbitrary smooth real(1,1)-form, mu is a fixed smooth strictly positive probability measure. The D_j are finitely many distinct prime divisors, with fixed smooth line-bundle metrics and canonical sections s_j, curvature eta_j, sigma_j=log|s_j|^2, so ddc sigma_j=[D_j]-eta_j. For nonnegative real a_j omit zero terms from sigma_a. A is the part of the nonnegative orthant where beta_a=theta-sum a_j eta_j has a smooth strictly positive representative. The limiting parameter must belong to A. The mean normalization is integral v_a dmu=0, not normalization of the singular u_a. The proposed conclusion concerns the canonical equation family u_a=sigma_a+v_a on a fixed manifold. It makes no assertion about arbitrary envelope systems, arbitrary all-model constraints or a degenerate boundary parameter.

Accepted internal inputs: Read the precise statements and accept their proved scopes. The smooth compact Hermitian equation and smooth uniqueness appear in chapter_smooth_equations.tex; chapter_gauduchon_variational_volume.tex defines the positive cone, proves thm:gaud-volume-dual-formula and prop:gaud-volume-first-variation, whose implicit-function proof includes smooth dependence of normalized potentials and scalars in smooth finite-dimensional families. The finite-divisor notation and Poincare-Lelong formula are in section_divisorial_gauduchon_volume.tex. The local-product locality and vanishing of extended measures on pluripolar sets are in chapter_products.tex. Analytic sets have zero Hermitian capacity and arbitrarily small-capacity open neighborhoods; this local pluripotential fact is accepted from the capacity foundations. The local logarithmic multiplier-ideal integral with exp(-u) normalization is ex:ideal-disc in chapter_framework.tex. Pullback of logarithmic divisor potentials, smooth functions and generic Lelong coefficients is the usual local Poincare-Lelong calculation.

Check that positivity makes the parameter domain open in the full real coefficient space before restricting to the orthant, including zero coefficients and n=1. Verify patching of mean-normalized solution families, compact-parameter C-infinity bounds, locality of extended measures at missing or zero coefficients, L1 and capacity convergence, total variation equality for probability mu, and the all-model finite-sum order formula. Check also that the following local multiplier ideals jump at integer coefficients and that this does not conflict with capacity/measure convergence. This is a bounded audit accepting the named earlier equation and regularity proofs, not a full rereview of those chapters.

Proof:

\subsection{Varying divisorial coefficients}

For fixed divisor support, the residual equation also controls limits while its background stays in the positive cone. Fix distinct prime divisors $D_1,\ldots,D_N$, their metrics and logarithmic potentials $\sigma_j=\log|s_j|^2$, a smooth real background $\theta$, and a smooth strictly positive probability measure $\mu$. For $a\in\mathbb R_{\geq0}^N$ put
\[
 D_a=\sum_j a_jD_j,\qquad
 \sigma_a=\sum_{a_j>0}a_j\sigma_j,\qquad
 \beta_a=\theta-\sum_j a_j\eta_j.
\]
Write $\mathcal A$ for the set of such $a$ for which $\beta_a$ has a smooth positive representative. Zero coefficients are omitted from the logarithmic sum.

\begin{proposition}\label{prop:finite-divisorial-equation-limits}
There are uniquely normalized smooth functions $v_a$, $a\in\mathcal A$, such that
\[
 \int_Xv_a\,\mathrm{d}\mu=0,\qquad
 \Omega_a=\beta_a+\ddc v_a>0,\qquad
 \Omega_a^n=c(a)\mu,
 \quad c(a)=\mathcal V_\mu(\beta_a)>0.
\]
The maps $a\mapsto v_a$ and $a\mapsto c(a)$ are smooth, with bounds for every smooth norm of $v_a$ on compact subsets of $\mathcal A$. Here smoothness at a zero coefficient means restriction of a smooth family from an open neighborhood in $\mathbb R^N$.

Set $u_a=\sigma_a+v_a$. If $a^{(k)}\in\mathcal A$ and $a^{(k)}\to a\in\mathcal A$, then $u_{a^{(k)}}\to u_a$ in $L^1$ and in capacity, and smoothly on compact subsets of $X\setminus\bigcup_jD_j$. Moreover,
\[
 \bigl\|\mathrm{MA}^{\mathrm{ext}}_\theta(u_{a^{(k)}})
       -\mathrm{MA}^{\mathrm{ext}}_\theta(u_a)\bigr\|_{\mathrm{TV}}
       =|c(a^{(k)})-c(a)|\longrightarrow0.
\]
For every modification $\pi:Y\to X$ with smooth source and every prime divisor $E\subset Y$,
\[
 \nu(u_a\circ\pi,E)=\sum_j a_j\operatorname{ord}_E(\pi^*D_j).
\]
In particular the limit has exactly the prescribed divisorial ordinary type; no additional singularity occurs in this finite family.
\end{proposition}
\begin{proof}
The set of parameters in $\mathbb R^N$ for which $\beta_a$ has a smooth positive representative is open. The smooth equation gives $v_a$ and $c(a)$ there. With the fixed mean normalization, the implicit-function argument in \cref{prop:gaud-volume-first-variation} gives their smooth dependence on this finite-dimensional family. Smooth uniqueness makes the local solution families agree. A finite covering of any compact parameter set then gives all the asserted smooth bounds.

The Poincar\'e--Lelong identity gives
\[
 \theta+\ddc u_a=[D_a]+\Omega_a.
\]
Thus $u_a\in\PSH(X,\theta)$. Its extended measure equals $\Omega_a^n=c(a)\mu$ off the divisor union, and both measures vanish on that union. This also treats $D_a=0$. Each fixed $\sigma_j$ is locally integrable, so coefficient convergence and smooth convergence of $v_a$ give the $L^1$ limit. Off the fixed divisor union every $\sigma_j$ is smooth, which gives the asserted smooth convergence. For capacity convergence, remove an open neighborhood of that analytic set of arbitrarily small Hermitian capacity. On its compact complement the convergence is uniform. This proves capacity convergence, since the divisor union has capacity zero. The equality of total-variation distances follows from the equation and $\mu(X)=1$.

Finally, after pullback the logarithmic potential $\sigma_j\circ\pi$ has generic coefficient $\operatorname{ord}_E(\pi^*D_j)$, whereas $v_a\circ\pi$ is smooth. Additivity for the finite logarithmic sum proves the displayed formula on every model. Since $v_a$ is smooth also at the limiting parameter, $u_a$ has the ordinary type of $\sigma_a$.
\end{proof}

The positive-cone hypothesis is imposed at the limit as well as along the sequence. The statement concerns equation solutions with finitely many prescribed divisors on a fixed manifold. It does not prove recovery for arbitrary envelope systems or supply estimates uniform over all modifications.

Multiplier ideals need not be eventually constant in this family. At a smooth point of $D_j$ outside the other divisors, take a coordinate $z_1$ defining $D_j$. There $u_a=a_j\log|z_1|^2+O(1)$, so
\[
 \mathcal I(u_a)=(z_1^{\lfloor a_j\rfloor})
\]
by the one-variable integral in \cref{ex:ideal-disc} and Fubini's theorem. Thus, if the parameter stays in $\mathcal A$ while $a_j$ increases to an integer from below, this local ideal jumps at the limit. Exactness of the limiting logarithmic coefficients does not mean eventual equality of the multiplier ideals.
