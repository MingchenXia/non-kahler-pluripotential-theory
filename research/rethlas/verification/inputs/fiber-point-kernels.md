Run_id: fiber_point_kernels_01

Statement: Verify BOTH complete supplied sections, in order. They analyze partial kernels selected by NON-DESCENDED isolated logarithmic singularities on a holomorphic submersion. Targets are the finite-codimension kernel/determinant comparison, the EXACT descent to base point-vanishing ideals (ambient dimension in the radial threshold), the O(m^(q-1)) jet-codimension bound, convergence of kernels/determinants using the already proved base equilibrium theorem, construction of small Hermitian-positive point poles without BMP, and exact loss of fiber-position information despite positive q-dimensional growth. The second section reconstructs the single-point Hopf kernel, its explicit binomial potential and total-variation limits, the corresponding envelope and non-pluripolar measure, and the failure to recover the original selecting weight's ideal type or raw Hermitian MA measure. These are mathematical reconstruction and test-case claims, not novelty claims. ALL new formulas and limits are targets; do not assume them.

Conventions: ddc=i/(2pi) partial bar-partial; I(u) means local integrability of |g|^2 exp(-u); a log|z|^2 has Lelong coefficient a. Ideal order means inclusion at EVERY positive real weight, and ordinary order means <= up to a bounded additive constant. All pole coefficients in the supplied sections are positive rational numbers, compatible with the manuscript's analytic-singularity convention. The singular weight ONLY selects the section space; the norm and kernel evaluation use the separate continuous weight. Normalization uses the BASE dimension q, not the ambient n. Never apply a closed-curvature theorem directly to the non-descended selecting weight phi.

Exact internal inputs granted; read the cited book sources and check applicability:
- book/author/chapter_partial_bergman.tex: the finite-dimensional evaluation kernel, mass identity, determinant first variation, and smooth-volume Bernstein–Markov proof. These proofs hold on a fixed subspace of H0, without needing a multiplier-ideal representation. The new codimension comparison itself is NOT granted. prop:partial-kernel-submersion proves unweighted descent of ALL sections of pi^*A^m along a proper holomorphic submersion with compact connected fibers; the same chapter constructs smooth fiber probabilities, the lift of base measures, preservation of mass and weak convergence, and continuous weighted norm identities for descended sections. The new non-descended multiplier-ideal selection formula is NOT granted.
- book/author/section_birational_partial_kernels.tex: thm:fujiki-partial-kernel-limit and cor:fujiki-partial-determinant are proved internal inputs. They give the partial kernel measure and determinant limits on a compact complex manifold admitting a Kähler modification, for a smooth line-bundle curvature theta and psi in PSH(theta) of positive NPP mass, a continuous full-manifold weight and smooth positive probability. Here they are applied only to the KÄHLER BASE using its identity modification. Their proof was audited in birational_partial_kernels_01 with verdict correct. Read the actual statements, not just the verdict. Their source is SGPT final-edition Theorem14.3.1 with exact fixed-auxiliary-bundle and normalization context, already verified; no need to reconstruct that source theorem again unless applicability raises a new issue. The current theorem retains the existence of a positive-mass base psi with specified radial poles.
- book/author/chapter_hopf_reduction.tex: prop:psh-descent-submersion gives PSH(B,theta) = PSH(X,pi^*theta) by pullback for a compact connected-fiber holomorphic submersion. In the Hopf case q=n-1, L_1=pi^*O(1), alpha=pi^*sigma, sigma^q has total mass1, nu_X=omega^n/(2n)=(1/2)alpha^q wedge zeta, and each elliptic fiber has zeta mass2. thm:hopf-descended-hermitian-ma proves MA_ext_omega(v o pi)=n pi^*MA_sigma(v) wedge zeta=2n L(MA_sigma(v)), including general sigma-psh v. This is a defined smooth-fibration lift, not arbitrary measure pullback. Hopf n=3 fails BMP, by the existing reconstructed counterexample.
- book/author/section_analytic_envelope_limits.tex lem:analytic-ideal-dominance: for qpsh u and an analytic singularity a on a compact complex manifold, u preceq_I a implies u<=a+C. Analytic singularities allow a locally bounded remainder. Ordinary domination implies ideal order directly. The new comparison of the upstairs point pole and the entire fiber's pole must still be proved.
- book/author/section_partial_envelopes.tex: the partial ideal envelope is the largest member of its family for a genuine reference in PSH(theta). A continuous obstacle on the whole manifold permits q.e. and everywhere inequalities to agree for canonical qpsh functions. The explicit envelope calculation and any use of a selecting reference NOT in PSH(theta) are new targets; the new statement instead characterizes its competitor family directly.
- book/author/chapter_compactness.tex thm:normalized-compactness: fixed smooth curvature lower bounds and normalized suprema give L1 compactness with genuine canonical limits, without BMP. Do not substitute kernel-measure convergence for potential convergence.

Standard local inputs allowed with exact hypotheses: compact-fiber maximum principle; local product coordinates for a holomorphic submersion; holomorphic Taylor expansion and sphere integrals; finite jets in a regular local ring; elementary linear algebra, dominated convergence, Chebyshev's inequality, and ordinary subharmonic maximum/removability principles; local Bedford–Taylor theory, including uniform convergence of bounded psh potentials and convolution approximation. The radial multiplier-ideal threshold, exact point-space identification, binomial coefficient/entropy estimates, projective norm constants, C1,1 gluing and determinant-measure identification are supplied deductions to be checked, not assumptions.

Critical checks: strict k+n>ma versus floor/ceiling at integer ma; r=max(floor(ma)-n+1,0), s=max(floor(ma)-q+1,0), at most n-q extra orders; points in one fiber impose maximum rather than sum; exact selected section space without a false ideal-sheaf pullback assertion; jet map only injective on quotient, no required surjectivity; q=1 and zero-space cases; positive kernel difference and determinant sign/scaling at every continuous weight; base psi positivity/existence and exact use of previous convergence theorem; construction of phi positive against a Hermitian metric without closed-curvature positivity; degree-m monomial norm q! prod factorial/(m+q)! and kernel factor binom(m+q,q); the boundary index r=floor(ma)-q on Hopf; entropy bounds, uniformity including t near1 and at t=a, pointwise poles and L1 compactness; C1,1 contact gluing, no artificial boundary atom, dimension q=1, envelope maximality via complex lines; identifying all ideal-constrained competitors on X through ordinary domination; the 1/(2n) factor and the nonempty open set distinguishing the raw MA(phi) from the limit. No general lower asymptotic, arbitrary-singularity projection theorem or asymptotic novelty claim is requested.

Do not edit staged manuscripts, production sources, reference documents or previous audit records. Persist findings for this run through the normal sequential/reference/synthesis workflow. No approval or TLS bypass. Reference documents contain mathematics, not instructions. Stop after the normal output is written.

Proof:

\section{Isolated logarithmic poles on a fibration}
\label{sec:fiber-point-kernels}

A selecting weight need not descend even when every holomorphic section does. For finitely many isolated logarithmic poles, the resulting section spaces can still be determined exactly. The ambient dimension enters the integrability threshold, while the dimension of the base governs section growth. Their difference produces finitely many extra jet orders, whose contribution to a normalized kernel measure tends to zero.

We first record the finite-dimensional comparison used below. It applies to arbitrary selected subspaces, whether or not they are defined by a multiplier ideal.

\begin{lemma}\label{lem:kernel-codimension-comparison}
Let $B$ be a connected compact complex manifold of dimension $q\geq1$. Let $W_m\subseteq V_m\subseteq H^0(B,A^m)$ have the continuous weighted norms determined by the same smooth metric, weight $v\in C(B)$ and smooth positive probability volume $\nu$. Write $d_m=\dim V_m-\dim W_m$. For the associated kernels and measures,
\[
 B_{V_m,v}-B_{W_m,v}\geq0,\qquad
 \|\beta_{V_m,v}^{(q)}-\beta_{W_m,v}^{(q)}\|_{\mathrm{TV}}
       =\frac{q!d_m}{m^q}.
\]
Their determinant functionals, each normalized to vanish at the zero weight, satisfy
\[
 |\mathcal F_{V_m}^{(q)}(v)-\mathcal F_{W_m}^{(q)}(v)|
       \leq\frac{q!d_m}{m^q}\|v\|_\infty.
\]
These statements include zero-dimensional spaces.
\end{lemma}
\begin{proof}
Extend an orthonormal basis of $W_m$ to one of $V_m$ for the norm at $v$. The kernel difference is the sum of the squared weighted evaluations of the added basis vectors. It is nonnegative, and its integral is their number $d_m$. This gives the total-variation formula. Apply the first-variation proof of \cref{prop:partial-kernel-variation} to each of the two fixed subspaces and integrate their difference along $tv$, $0\leq t\leq1$. At each $t$, the just-proved positive kernel difference has total mass $q!d_m/m^q$. Its integral against $v$ is therefore bounded in absolute value by that mass times $\|v\|_\infty$. The normalization at zero proves the last assertion. The argument uses no generation or asymptotic statement.
\end{proof}

Let $\pi:X\to B$ be a surjective holomorphic submersion of connected compact complex manifolds with connected fibers. Put $n=\dim X$, $q=\dim B\geq1$, and $f=n-q$. Let $A$ be a holomorphic line bundle on $B$ and $L=\pi^*A$. Fix distinct points $p_1,\ldots,p_N$ on $X$ and positive rational numbers $a_1,\ldots,a_N$. Suppose $\varphi\in\QPSH(X)$ is locally bounded away from these points and, in local coordinates $x$ centered at $p_j$, has the form
\begin{equation}\label{eq:isolated-selecting-poles}
 \varphi(x)=a_j\log|x|^2+O(1).
\end{equation}
No positivity against the closed curvature of $L$ is assumed. Write
\[
 Z=\{\pi(p_1),\ldots,\pi(p_N)\},\qquad
 a_b=\max_{\pi(p_j)=b}a_j\quad(b\in Z).
\]
For an integer $m\geq1$, set
\[
 r_{m,b}=\max\{\lfloor ma_b\rfloor-n+1,0\},\qquad
 s_{m,b}=\max\{\lfloor ma_b\rfloor-q+1,0\}.
\]
Here $\mathfrak m_b$ denotes the ideal sheaf of the point $b$, with zeroth power $\mathcal O_B$.

\begin{proposition}\label{prop:isolated-pole-section-descent}
Pullback identifies the selected space on $X$ with
\[
 V_m=H^0\left(B,A^m\otimes
                       \bigcap_{b\in Z}\mathfrak m_b^{r_{m,b}}\right).
\]
If
\[
 W_m=H^0\left(B,A^m\otimes
                       \bigcap_{b\in Z}\mathfrak m_b^{s_{m,b}}\right),
\]
then $W_m\subseteq V_m$ and
\[
 0\leq\dim V_m-\dim W_m
 \leq\sum_{b\in Z}\sum_{j=r_{m,b}}^{s_{m,b}-1}
                         \binom{j+q-1}{q-1}
 =O(m^{q-1}).
\]
An empty inner sum is zero. The constants depend on the fixed point data, not on $m$.
\end{proposition}
\begin{proof}
For a radial logarithmic pole $a\log|x|^2+O(1)$ in dimension $n$, the multiplier ideal at weight $m$ is
\[
 \mathfrak m_0^{\max\{\lfloor ma\rfloor-n+1,0\}}.
\]
Indeed, a nonzero holomorphic germ of order $k$ has spherical squared integral comparable to $r^{2k}$ for small $r$. Its first nonzero homogeneous Taylor term gives the positive leading coefficient. The bounded remainder in the weight changes the integral by bounded positive factors. Radial integrability is therefore equivalent to
\[
 \int_0^\epsilon r^{2k-2ma+2n-1}\,\mathrm{d}r<+\infty,
 \quad\hbox{or equivalently }k+n>ma.
\]
The smallest nonnegative integer $k$ satisfying this strict inequality is the displayed exponent. Away from the specified points the multiplier ideal is the full structure sheaf.

Every section of $L^m$ descends to $B$, by the compact-fiber argument in \cref{prop:partial-kernel-submersion}. Near $p_j$, choose submersion coordinates $(z,\tau)$ with $\pi(z,\tau)=z$. A pulled-back section has a local coefficient $g(z)$ independent of $\tau$. Its order at $(0,0)$ equals its order at $z=0$. The conditions from points in the same fiber are thus the same kind of point-vanishing condition, and their maximum is $r_{m,b}$. This proves the exact space identification.

For the dimension bound, send a section of $V_m$ to its germs modulo $\mathfrak m_b^{s_{m,b}}$ at the finitely many points $b$. The kernel is $W_m$. Local trivializations of $A^m$ therefore give an injection
\[
 V_m/W_m\hookrightarrow
       \bigoplus_{b\in Z}\mathfrak m_b^{r_{m,b}}/
                                      \mathfrak m_b^{s_{m,b}}.
\]
No surjectivity of a jet-evaluation map is required. In dimension $q$, the degree-$j$ homogeneous monomials number $\binom{j+q-1}{q-1}$. They compute the displayed quotient dimensions. Finally $0\leq s_{m,b}-r_{m,b}\leq f$ and $s_{m,b}=O(m)$, proving the bound, also when $q=1$ or $f=0$.
\end{proof}

Equip $A$ with a smooth metric $h_A$ and put $\theta=c_1(A,h_A)$. Choose a smooth positive probability volume $\nu_B$, smooth fiber probabilities as in the preceding sections, and their smooth positive lift $\nu_X=\mathcal L\nu_B$. Use the pullback metric on $L$. For $v\in C(B)$, use $v\circ\pi$ in the continuous norm on $X$.

\begin{theorem}\label{thm:isolated-pole-kernel-limit}
Assume $B$ is K\"ahler and there is $\psi\in\PSH(B,\theta)$ of positive non-pluripolar mass, locally bounded off $Z$, with
\[
 \psi(z)=a_b\log|z-b|^2+O(1)\quad\hbox{near each }b\in Z.
\]
Let $E(v)=E_{\theta,B}[\psi]_{\mathcal I}(v)$. For the selecting weight $\varphi$ in \eqref{eq:isolated-selecting-poles},
\[
 \beta_{X,m,v\circ\pi,\varphi}^{(q)}
      \rightharpoonup\mathcal L\bigl(\mathrm{MA}_\theta(E(v))\bigr).
\]
More precisely, its total-variation distance from the lift of the base partial kernel measure selected by $\psi$ is $O(m^{-1})$. Its determinant functionals satisfy
\[
 \mathcal F_{X,m}^{(q)}(v\circ\pi)\longrightarrow
 \int_0^1\!\left(\int_B
           v\,\mathrm{d}\mathrm{MA}_\theta(E(tv))\right)\mathrm{d}t.
\]
The normalized dimensions converge to the finite positive equilibrium mass. If $n>q$, normalization by $n!/m^n$ gives zero kernel measures in total variation.
\end{theorem}
\begin{proof}
The radial integrability calculation in dimension $q$ identifies the base multiplier-ideal-selected space with $W_m$ in the proposition. Corresponding sections in $V_m$ and on $X$ have equal continuous norms, since the pointwise norm and continuous weight descend and every fiber probability has mass one. The same orthonormal-basis argument as in \cref{prop:partial-kernel-submersion} gives the exact lift of the kernel associated with $V_m$ on $B$.

By \cref{lem:kernel-codimension-comparison,prop:isolated-pole-section-descent}, the normalized kernel difference between $V_m$ and $W_m$ is positive with total mass $O(m^{-1})$. Its lift remains positive with the same mass. Apply \cref{thm:fujiki-partial-kernel-limit} to $B$, using the identity modification: all its closed K\"ahler and positive-mass hypotheses are among the assumptions here. It gives the base $W_m$ convergence, and the vanishing kernel difference proves the asserted limit on $X$.

The determinant comparison bounds the difference of the two functionals by $O(m^{-1})\|v\|_\infty$. The exact norm identification and \cref{cor:fujiki-partial-determinant} on $B$ give the displayed limit. Testing one proves the dimension assertion. The $q$-normalized masses are bounded, so multiplication by $(n!/q!)m^{q-n}$ proves the last assertion.
\end{proof}

The hypothesis on $\psi$ is a geometric constraint on the projected point data. It is not automatic for arbitrarily large coefficients. For an ample bundle with a positive smooth curvature form $\theta$, it holds when the finitely many coefficients are sufficiently small. Here is a direct construction. On disjoint coordinate balls choose smooth cutoffs equal to one near their centers. Each cutoff times $\log|z-b|^2$, extended by zero, has complex Hessian bounded below by $-C_b\theta$: near the center it is plurisubharmonic, and on the intervening annulus it is smooth. If $\sum_b a_bC_b<1$, their weighted sum is $\theta$-plurisubharmonic and has precisely the prescribed poles. Off the poles its curvature dominates $\epsilon\theta$ for some $\epsilon>0$, so its non-pluripolar mass is positive. It is finite by the closed K\"ahler theory.

The identical cutoff construction on $X$, with any fixed Hermitian metric $\omega$, produces $\varphi\in\PSH(X,\omega)$ for sufficiently small coefficients. It uses only a smooth curvature lower bound, not BMP. If $f>0$ and the pole set is nonempty and finite, this $\varphi$ cannot descend: it is finite at other points of a fiber containing a pole.

The exact section formula also explains a failure of singularity recovery. Moving an isolated pole within its fiber does not change any selected section space. Adding finitely many poles in that same fiber does not change the spaces when the maximal coefficient there is unchanged. For fixed $h,v,\nu_X$, all kernels and determinant functionals are then exactly the same in every degree. The multiplier-ideal types on $X$ are nevertheless different: at sufficiently large weight one ideal is proper at a point where the other is the full local ring. Under the theorem's hypotheses this loss of information coexists with a positive $q$-dimensional growth limit. Closed-curvature positivity of the selecting potential, present in the source theory, cannot be replaced merely by positivity against a Hermitian background.


\section{A point pole on the Hopf manifold}
\label{sec:hopf-point-equilibrium}

The one-point case on the Hopf manifold admits an explicit calculation of both the kernel measure and its Fubini--Study potential. It supplies a lower asymptotic for a selecting weight which does not descend. The limit also shows exactly which singularity information the section spaces have lost.

Use $X_n\to\mathbb P^q$, $q=n-1\geq1$, with $L=L_1$, the Fubini--Study metric and probability volume $\nu_X=\omega^n/(2n)$ from the preceding sections. Let $p\in X_n$ lie over $b=[1:0:\cdots:0]$. Suppose $\varphi$ has a single logarithmic pole of rational coefficient $0<a<1$ at $p$ and is locally bounded elsewhere, as in \eqref{eq:isolated-selecting-poles}. The continuous weight is zero. Set
\[
 t([Z_0:\cdots:Z_q])=
       \frac{|Z_1|^2+\cdots+|Z_q|^2}{|Z_0|^2+\cdots+|Z_q|^2},
 \qquad r_m=\max\{\lfloor ma\rfloor-q,0\},
 \qquad D_m=\binom{m+q}{q}.
\]
Thus $t=0$ exactly at $b$. Define the function $e_a$ on $[0,1]$ by
\begin{equation}\label{eq:point-equilibrium-function}
 e_a(t)=
 \begin{cases}
 a\log(t/a)+(1-a)\log((1-t)/(1-a)),&0<t<a,\\
 0,&a\leq t\leq1,\\
 -\infty,&t=0,
 \end{cases}
\end{equation}
and put $E_a=e_a\circ t$ on $\mathbb P^q$.

\begin{proposition}\label{prop:hopf-point-binomial-kernel}
The selected kernel and dimension are
\[
 B_{X_n,m}=D_m\left(
          \sum_{j=r_m}^{m}\binom mj t^j(1-t)^{m-j}\right)\circ\pi,
 \qquad
 N_m=D_m-\binom{r_m+q-1}{q}.
\]
The last binomial coefficient is zero when $r_m=0$. In particular all these spaces are nonempty, and
\[
 \lim_{m\to\infty}\frac{q!N_m}{m^q}=1-a^q>0.
\]
\end{proposition}
\begin{proof}
By \cref{prop:isolated-pole-section-descent}, the space on the base consists of homogeneous polynomials of degree $m$ vanishing to order at least $r_m$ at $b$. In the affine chart $Z_0=1$, this selects exactly the monomials $Z^\ell$ with $\ell_1+\cdots+\ell_q\geq r_m$.

Coordinate circle invariance makes distinct monomials orthogonal. Their squared norms for $\sigma^q$ are
\[
 \int_{\mathbb P^q}\frac{|Z^\ell|^2}{|Z|^{2m}}\,\sigma^q
       =\frac{q!\,\ell_0!\cdots\ell_q!}{(m+q)!},
 \qquad |\ell|=m.
\]
For completeness, integrate $|z^\ell|^2e^{-|z|^2}$ over $\mathbb C^{q+1}$ in two ways. Product integration gives $\pi^{q+1}\prod_i\ell_i!$; radial integration separates a sphere average and the factor $(m+q)!$. Dividing by the same computation for $\ell=0$ gives the displayed normalized sphere average. Its projective pushforward is $\sigma^q$, since both are the invariant probability under the unitary group. This proves the norm formula.

The reciprocal squared norm is $D_m m!/(\ell_0!\cdots\ell_q!)$. Sum first over the monomials with $\ell_1+\cdots+\ell_q=j$. The multinomial formula gives
\[
 D_m\binom mj t^j(1-t)^{m-j}.
\]
The norms and kernels lift exactly to $X_n$, proving the first formula. There are $\binom{j+q-1}{q-1}$ monomials of affine degree $j$. Summing the excluded degrees $0\leq j<r_m$ gives $\binom{r_m+q-1}{q}$. Since $r_m/m\to a$ and $0\leq r_m\leq m$, this proves the dimension formula, nonemptiness and the limit.
\end{proof}

\begin{theorem}\label{thm:hopf-point-potential-limit}
Let $U_m=m^{-1}\log B_{X_n,m}$ be the global partial Fubini--Study potential for the zero continuous weight. Then
\[
 U_m\longrightarrow E_a\circ\pi
\]
in $L^1(X_n)$, pointwise with extended values, and locally uniformly off the fiber $\pi^{-1}(b)$. The normalized measures converge in total variation:
\[
 \frac{q!}{m^q}B_{X_n,m}\,\nu_X
       \longrightarrow
       \mathbf1_{\{t\circ\pi>a\}}\nu_X.
\]
\end{theorem}
\begin{proof}
Write the sum in the proposition as $P_m(t)$. For fixed $0<t<1$, it is the probability that a binomial random variable of parameters $(m,t)$ is at least $r_m$. Its variance is $mt(1-t)$. Chebyshev's inequality and $r_m/m\to a$ imply
\[
 P_m(t)\longrightarrow
 \begin{cases}0,&t<a,\\1,&t>a.\end{cases}
\]
The pushforward of $\sigma^q$ by $t$ is $q t^{q-1}\,\mathrm{d}t$. One can see this directly in the affine chart: the Fubini--Study radial density is
$2q r^{2q-1}(1+r^2)^{-q-1}\,\mathrm{d}r$, and $t=r^2/(1+r^2)$. In particular the level $t=a$ has measure zero. Now $0\leq P_m\leq1$ and $q!D_m/m^q\to1$. Dominated convergence gives convergence of the densities in $L^1(\sigma^q)$, hence also in $L^1(\nu_X)$ after lifting. This is exactly the asserted total-variation convergence. Its limiting mass is $\int_a^1 qt^{q-1}\,\mathrm{d}t=1-a^q$.

To compute the potential, put
\[
 H(s)=-s\log s-(1-s)\log(1-s),\qquad 0\leq s\leq1,
\]
with $0\log0=0$. The elementary binomial bounds are
\[
 \frac{e^{mH(j/m)}}{m+1}\leq\binom mj
                   \leq e^{mH(j/m)}\quad(0\leq j\leq m).
\]
Indeed the $j$th probability for parameters $(m,j/m)$ is at most one and at least $1/(m+1)$. For the latter assertion, the ratio of neighboring probabilities shows that the $j$th term is a largest term; the $m+1$ terms sum to one. The endpoint cases have probability one.

The logarithm of a sum of at most $m+1$ nonnegative terms differs from the largest logarithm by at most $\log(m+1)$. It follows that $m^{-1}\log P_m(t)$ differs by at most $\log(m+1)/m$ from
\[
 \max_{r_m\leq j\leq m}
 \left\{H(j/m)+(j/m)\log t+(1-j/m)\log(1-t)\right\}.
\]
On compact subintervals of $(0,1)$, uniform continuity and $r_m/m\to a$ make these maxima converge uniformly to the maximum over $a\leq s\leq1$. Differentiation in $s$ shows that the maximum is zero when $t\geq a$ and equals the first expression in \eqref{eq:point-equilibrium-function} when $t<a$. Thus the limit is $e_a(t)$, including at $t=a$.

There is also uniform convergence near $t=1$. Choose $c$ with $a<c<1$. The same variance estimate gives $P_m(t)\geq1-C/m$ uniformly for $c\leq t\leq1$ and large $m$; hence $m^{-1}\log P_m\to0$ uniformly there. Together with the preceding compact-interval argument and $m^{-1}\log D_m\to0$, this proves local uniform convergence off $t=0$. At $t=0$, eventually $r_m>0$, so $P_m(0)=0$ and the extended pointwise limit is $-\infty$.

Finally $U_m\in\PSH(X_n,\alpha)$ by its holomorphic sum-of-squares expression, and
\[
 \sup_{X_n}U_m=\frac{\log D_m}{m},
\]
because $P_m\leq1$ and $P_m(1)=1$. \Cref{thm:normalized-compactness} for potentials with a fixed smooth curvature lower bound supplies $L^1$ cluster limits and excludes collapse. Each cluster limit agrees almost everywhere with $E_a\circ\pi$, by the local uniform convergence off the analytic fiber. Every subsequence has the same cluster limit, proving convergence of the whole sequence in $L^1$. This uses compactness of quasi-plurisubharmonic functions, not a nonlinear mass bound.
\end{proof}

The formula for $E_a$ has an intrinsic envelope interpretation. Set $\psi_a=a\log t$ on $\mathbb P^q$. This is $\sigma$-plurisubharmonic for $0<a<1$: away from $b$, its curvature is the convex combination of $\sigma$ and the semipositive form induced by the projection $[Z_0:Z']\mapsto[Z']$. For $q=1$, the second form is zero. The local logarithmic expression gives the positive extension at $b$.

\begin{proposition}\label{prop:hopf-point-envelope}
The function $E_a$ belongs to $\PSH(\mathbb P^q,\sigma)$ and
\[
 E_a=E_{\sigma,\mathbb P^q}[\psi_a]_{\mathcal I}(0),
 \qquad
 \mathrm{MA}_\sigma(E_a)=\mathbf1_{\{t>a\}}\sigma^q.
\]
Moreover, $E_a\circ\pi$ is the largest $u\in\PSH(X_n,\alpha)$ satisfying $u\leq0$ and $u\preceq_{\mathcal I}\varphi$. Thus
\[
 \mathbf1_{\{t\circ\pi>a\}}\nu_X
       =\frac1{2n}\mathrm{MA}^{\mathrm{ext}}_\omega(E_a\circ\pi).
\]
\end{proposition}
\begin{proof}
In the chart $Z_0=1$, write $z=Z'/Z_0$ and $R^2=a/(1-a)$. For $|z|<R$, the local potential of $\sigma+\ddc E_a$ is
\[
 \log(1+|z|^2)+E_a
       =a\log|z|^2-a\log a-(1-a)\log(1-a).
\]
Its complex Hessian is positive and has rank $q-1$ away from zero. For $|z|>R$, the form is $\sigma$. The two expressions for $E_a$ have equal values and equal first derivatives at $|z|=R$. They therefore glue as a $C^{1,1}$ function near the interface, with no hypersurface term in its distributional Hessian. Near $b$ it has the logarithmic pole of coefficient $a$. This proves global $\sigma$-plurisubharmonicity and $E_a\simeq\psi_a$.

To verify the envelope bound, let $w\in\PSH(\mathbb P^q,\sigma)$ satisfy $w\leq0$ and $w\preceq_{\mathcal I}\psi_a$. By \cref{lem:analytic-ideal-dominance}, $w\leq\psi_a+C$. Fix a complex line through zero in the affine chart. If the restriction of $w+\log(1+|z|^2)$ is identically $-\infty$, there is nothing to prove on that line. Otherwise it is subharmonic. On its punctured disk of radius $R$, subtract $a\log|z|^2$. The result is subharmonic and bounded above near zero by the ordinary singularity inequality, so it extends subharmonically across zero. On the boundary its value is at most $\log(1+R^2)-a\log R^2$. The maximum principle gives exactly $w\leq E_a$ in the disk. Every point with $|z|<R$ lies on such a line; outside this ball $w\leq0=E_a$. Since $E_a$ itself is an admissible competitor, it is the stated envelope. Continuous zero obstacles make the quasi-everywhere and everywhere inequalities equivalent, as proved earlier.

On the complement of $b$, the local potentials are $C^{1,1}$. Their Bedford--Taylor top products are the almost-everywhere determinants of their complex Hessians: local convolution gives uniformly bounded Hessians converging almost everywhere, and dominated convergence identifies the determinant limit with the locally uniform Bedford--Taylor limit. The rank computation makes this determinant zero for $t<a$ and equal to $\sigma^q$ for $t>a$. The interface has smooth volume zero, and a $C^{1,1}$ local potential adds no measure there. The non-pluripolar measure gives $b$ zero mass. This proves the measure formula.

For the assertion on $X_n$, every $\alpha$-plurisubharmonic function is $u=w\circ\pi$ by \cref{prop:psh-descent-submersion}. Since $\varphi$ has analytic singularities, $u\preceq_{\mathcal I}\varphi$ implies $u\preceq\varphi$ by \cref{lem:analytic-ideal-dominance}. In product coordinates $(z,\tau)$ at $p$, restrict this inequality to $\tau=0$. It yields $w(z)\leq a\log|z|^2+C$, and hence $w\preceq\psi_a$ globally. Conversely, $w\preceq\psi_a$ gives
\[
 w(z)\leq a\log|z|^2+C
             \leq a\log(|z|^2+|\tau|^2)+C
\]
near $p$. Away from $p$, local boundedness of $\varphi$ and compactness make the upper inequality global. Thus $w\circ\pi\preceq\varphi$, which implies the ideal order. Applying analytic ideal domination on the base as well shows that the two ideal-constrained competitor families are exactly those already considered. Their largest members therefore agree under pullback. Finally \cref{thm:hopf-descended-hermitian-ma} and the base measure formula give the last identity.
\end{proof}

For sufficiently small rational $a$, the cutoff construction in the preceding section makes $\varphi\in\PSH(X_n,\omega)$ with its only pole at $p$. The theorem consequently applies on the Hopf threefold where BMP fails, and gives a nonzero limit with the intrinsic normalization $2/m^2$. The limiting potential has a pole on the whole elliptic fiber over $b$. At other points of that fiber the input $\varphi$ is locally bounded, whereas the limiting potential has a nontrivial multiplier ideal at sufficiently large weight. Thus even this positive-growth limit does not recover the multiplier-ideal type of an arbitrary Hermitian-positive selecting weight.

The measure limit is also different from the raw Hermitian Monge--Amp\`ere measure of $\varphi$. Choose its cutoff support in a small neighborhood of $p$. There is a nonempty open set outside that support with $t\circ\pi<a$: take a neighborhood of another point of the same elliptic fiber. On this open set $\varphi=0$, so locality gives $\mathrm{MA}^{\mathrm{ext}}_\omega(\varphi)=\omega^n$, while the limiting kernel measure is zero. The equality above concerns the projected equilibrium potential $E_a\circ\pi$, whose construction and singularity type have been identified, not the original selecting weight.
