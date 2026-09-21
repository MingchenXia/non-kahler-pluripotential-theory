Run_id: relative_moving_general_existence_01

Statement: Verify the two new staged sections below, namely common-E-envelope capacity convergence, moving bounded-reference weak continuity, and a full reconstruction of the known ALS26 prescribed-reference general non-pluripolar measure existence theorem (positive and zero exponent). Standing hypotheses: X compact connected Hermitian, theta smooth semipositive and big, model phi=P_theta[phi] with P_(epsilon theta)(phi) genuine for 0<epsilon<1, and v_-(theta)>0. No bounded mass hypothesis. Finite mass is NOT automatic for E_phi. The proposed relative zero-domination lemma is a CONDITIONAL premise under separate current audit relative_extended_domination_01. Verify this entire downstream proof conditional on exactly that lemma; do not assume the general strict-domination result or general existence to prove any step. Publication will require the separate prerequisite audit to pass too. Do not alter previous inputs/results or treat a prior verdict as proof of a different scope.

Precisely allowed conditional lemma: if p,u in E_phi, p<=u and MAext_theta(p)({p<u})=0, then p=u, with no finite-mass assumption. Its staged source is /Users/mingchen/Non-Kahler/research/editorial/section_relative_extended_domination.tex. All other internal premises below have already reconstructed proofs. Check their exact statements in these files whenever applying:
- book/author/chapter_envelopes.tex: convex competitor definition E_env, upward stability, equality P_theta[u]=phi for u in E_phi; genuine finite-a.e quasi-continuous obstacles have contact support (proof in section_big_general_contact.tex), ordered contact and finite rooftop partition.
- book/author/chapter_relative_finite_measures.tex: finite rooftops in E_phi; lower mass kappa=(1-epsilon)^n v_-(theta); finite-MA(u) domination and exponential order with u in E_phi and second potential v preceq phi. In particular reference0 is allowed, the second potential need not be E0 or preceq the first potential.
- book/author/section_relative_compactness.tex: fixed-NPP integration for bounded common-lower-curvature quasi-psh functions, moving bounded integration, bounded mixed capacity, weighted extended LSC under CAPACITY convergence, and monotone capacity convergence with a genuine lower bound. No unrestricted L1 mass LSC.
- book/author/section_dominated_relative_compactness.tex: fixed finite non-pluripolar dominator gives E_phi class closure, capacity and weak MA convergence from L1 convergence. Proof is independent of the current conditional zero lemma and general existence.
- book/author/section_exponential_rooftop_barrier.tex: u_j in E_phi, u_j<=phi+C, MA(u_j)<=A exp(lambda u_j) omega_psi_j^n, uniformly bounded psi_j, implies common lower envelope in E_phi under positive lower volume. Does not itself assert capacity or mass convergence.
- book/author/section_general_measure_minimal.tex: bounded omega-carrier for every finite non-pluripolar measure (carrier needs no volume condition); and full general finite-NPP equations in E0 in semipositive big theta under v_-(theta)>0. The minimal-reference theorem was reconstructed earlier using the SAME-theta bounded carrier, bounded subsolution theorem, and fixed-measure continuity. It is noncircular here.
- book/author/section_singular_domination.tex: singular exponential order with FIRST potential admitting a smaller-background envelope, SECOND potential more singular than first, in any semipositive big background, NO uniform lower or upper volume assumption. Thus a bounded first potential in the metric omega is allowed, even if v_-(omega) is not known positive.
- book/author/chapter_prescribed_equations.tex thm:als-prescribed-lp, proved in section_prescribed_existence.tex: ordinary-type u~phi existence for all nonzero Lp smooth-volume data, p>1, in theta semipositive big, phi model with smaller background, without volume properties.
- book/author/chapter_compactness.tex: bounded omega-psh has smooth strictly omega-psh decreasing uniformly bounded approximation.
- book/author/chapter_damped_measures.tex: capacity convergence plus uniform finite total mass and uniformly vanishing raw sublevel tails implies finite limiting MA and weak convergence, including its stated general-background version.

Important scope check: the earlier bounded-subsolution theorem only states a bounded SAME-theta carrier. The new proof does NOT apply it directly to arbitrary bounded omega-carrier measures. Instead it uses the already reconstructed general minimal-reference theorem to construct s in E0 and compares with reference0; s need not be bounded below. Check this explicitly.

ALS26 is Alehyane--Lu--Salouf, Monge-Ampere equations with prescribed singularities on compact Hermitian manifolds, arxiv2511.02339v1, local PDF and extracted text in research/sources/ALS26.pdf and ALS26.txt. The only use of its general existence theorem in the new section is identification/attribution of the theorem being proved, never a premise. Standard local Bedford--Taylor calculus, canonical representatives, measure regularity, Egorov, dominated convergence are allowed. Verify mathematical transitions and hypotheses, not typography; no claims of novelty.

Proof:

\section{Moving measures and relative compactness}

A common lower envelope in $\mathcal E_\varphi$ need not have finite mass. The preceding domination lemma nevertheless suffices for the capacity argument. Finiteness of the limiting measure will follow afterwards from control of its tails.

\begin{proposition}\label{prop:relative-common-envelope-criterion}
Suppose $u_j\in\mathcal E_\varphi$ and, for a fixed $h\in\mathcal E_\varphi$ and constant $C$,
\[
 h\leq u_j\leq\varphi+C,\qquad
 u_j\longrightarrow u\in\PSH(X,\theta)\quad\hbox{in }L^1(X).
\]
If
\[
 I_j:=\int_X|e^{u_j}-e^u|\,\mu_{u_j}\longrightarrow0,
\]
then $u\in\mathcal E_\varphi$ and $u_j\to u$ in capacity. No upper mass bound is part of this criterion.
\end{proposition}
\begin{proof}
The bounds pass to $u$ almost everywhere along an extraction and then to canonical representatives. Upward stability gives $u\in\mathcal E_\varphi$. Translate the entire family and its bounds by a common constant to make all potentials nonpositive.

It suffices to obtain capacity convergence along a further extraction of every subsequence. Extract so that $I_j\leq2^{-j}$ and $u_j\to u$ almost everywhere for smooth volume. Form
\[
 p_{j,N}=P_\theta(u_j,\ldots,u_N),\qquad
 p_j=P_\theta\left(\inf_{\ell\geq j}u_\ell\right).
\]
Every envelope lies above $h$ and below $\varphi+C$, so is genuine and belongs to $\mathcal E_\varphi$. For the finite envelope, partition its contact set by the first index $\ell$ with $p_{j,N}=u_\ell$. Ordered contact on each part gives
\[
 \int_X|e^{p_{j,N}}-e^u|\,\mu_{p_{j,N}}
 \leq\sum_{\ell=j}^N I_\ell\leq2^{1-j}.
\]
Only positive integrals are used here, even if a rooftop has infinite mass.

As $N\to\infty$, $p_{j,N}\downarrow p_j$. As $j\to\infty$, the $p_j$ increase to a genuine canonical limit $p$. Both convergences hold in capacity by monotone truncation with the fixed lower bound $h$. Also $h\leq p\leq u\leq\varphi+C$; the upper inequality follows first from almost-everywhere convergence of the extracted $u_j$. Thus $p\in\mathcal E_\varphi$.

Apply \cref{lem:weighted-extended-lsc} first as $N\to\infty$ and then as $j\to\infty$, with the bounded quasi-continuous weights displayed above. The weights converge in capacity because the exponential is Lipschitz on a common upper half-line. We obtain
\[
 \int_X|e^p-e^u|\,\mu_p=0,
 \qquad \mu_p(\{p<u\})=0.
\]
The second equality follows off the poles, which the extended measures ignore. The relative zero-domination lemma gives $p=u$, without a finiteness hypothesis on $\mu_p$.

Finally $U_j=(\sup_{\ell\geq j}u_\ell)^*$ decreases to $u$ by Hartogs' lemma and the almost-everywhere extraction. Monotone capacity convergence applies to $p_j\uparrow u$ and $U_j\downarrow u$. The inequalities $p_j\leq u_j\leq U_j$ prove capacity convergence on this extraction, and hence on the original sequence.
\end{proof}

\begin{theorem}\label{thm:relative-moving-measure-continuity}
Under the geometric and common-envelope hypotheses of \cref{prop:relative-common-envelope-criterion}, suppose
\[
 \mu_{u_j}\leq A\omega_{\psi_j}^n+\nu,
\]
where $A\geq0$ is fixed, $\nu$ is a fixed finite non-pluripolar measure, and $\psi_j\in\PSH(X,\omega)$ are uniformly bounded and converge in capacity to a bounded $\psi$. Then $u\in\mathcal E_\varphi$, $u_j\to u$ in capacity, $\mu_u$ is finite, and
\[
 \mu_{u_j}\rightharpoonup\mu_u.
\]
\end{theorem}
\begin{proof}
Translate so that $u_j,u\leq0$. The functions $e^{u_j},e^u$ are uniformly bounded quasi-plurisubharmonic functions with a common lower curvature bound. They converge in smooth-volume $L^1$, since the exponential is Lipschitz on $(-\infty,0]$. The moving bounded integration lemma and the fixed non-pluripolar integration lemma give
\[
 \int_X|e^{u_j}-e^u|\,\omega_{\psi_j}^n\longrightarrow0,
 \qquad
 \int_X|e^{u_j}-e^u|\,\mathrm{d}\nu\longrightarrow0.
\]
Therefore $I_j\to0$, and the preceding proposition proves capacity convergence and class membership.

The bounded reference measures have uniformly bounded mass and satisfy a common capacity estimate by \cref{lem:bounded-mixed-capacity}. For a constant $B$ independent of $j,T$,
\[
 \mu_{u_j}(\{u_j<-T\})
 \leq B\operatorname{Cap}_\omega(\{h<-T\})
       +\nu(\{h<-T\})\longrightarrow0
\]
uniformly in $j$. The first term tends to zero because $h$ is a genuine quasi-plurisubharmonic function, and the second because $\nu$ is finite and ignores its pole set. The total masses are uniformly bounded by the assumed domination. The undamped tail theorem, in its general-background form, now gives finiteness of $\mu_u$ and the asserted weak convergence.
\end{proof}

In particular, the common envelope supplied by \cref{prop:exponential-common-rooftop} is sufficient whenever its bounded reference potentials converge in capacity. The proof never estimates the mass of a finite rooftop by a bound independent of the number of obstacles. The relative zero-domination lemma replaces that unnecessary intermediate estimate.


\section{General measures with prescribed reference singularities}
\label{sec:general-measure-relative}

We can now reconstruct the general prescribed-reference theorem stated in \cref{thm:als-general-measure}. Its hypotheses remain semipositivity, bigness, the displayed model condition and positive lower volume. The solution belongs to the relative envelope class; its difference from the reference need not be bounded. The proof follows the density approximations of \cite[Theorem 5.8 and Corollary 5.9]{ALS26}, with the required capacity convergence supplied by the preceding section.

\begin{proof}[of \cref{thm:als-general-measure}]
Let $\mu$ be the given nonzero finite non-pluripolar measure. Fix a Hermitian metric $\omega\geq\theta$. Apply \cref{lem:bounded-measure-carrier} to the big background $\omega$ to write
\[
 \mu=f\nu,\qquad \nu=\omega_\psi^n,\qquad
 \psi\in\PSH(X,\omega)\cap L^\infty(X),\qquad
 0\leq f\in L^1(\nu).
\]
No lower volume condition on $\omega$ is required for this representation. Recall the uniform positive bound
\[
 \mu_a(X)\geq\kappa=(1-\varepsilon)^n v_-(\theta)>0
 \qquad(a\in\mathcal E_\varphi).
\]
Also, by \cref{prop:relative-envelope-equality}, every such $a$ satisfies
\begin{equation}\label{eq:relative-normalized-model-bound}
 a-\sup_Xa\leq P_\theta[a]=\varphi.
\end{equation}
The inequality follows because $a-\sup_Xa$ is a normalized competitor for its singularity envelope.

\emph{Positive continuous density.} Fix $\lambda>0$ and first suppose $f$ is continuous and strictly positive. Choose smooth strictly $\omega$-plurisubharmonic $\psi_j\downarrow\psi$ by \cref{thm:bounded-exact-regularization}. These potentials are uniformly bounded; write $\|\psi_j\|_\infty\leq L$ and $\nu_j=\omega_{\psi_j}^n$. Their masses are bounded by a common constant $B$, and $\nu_j\rightharpoonup\nu$ by bounded Bedford--Taylor continuity. The prescribed ordinary-type theorem \cref{thm:als-prescribed-lp} supplies $u_j\simeq\varphi$ with
\[
 \mu_{u_j}=e^{\lambda u_j}f\nu_j.
\]
Indeed $f\nu_j$ has a continuous positive density relative to smooth volume, hence belongs to every finite $L^p$ space.

We first give a common upper bound. Choose $K$ with
$e^{-\lambda(\psi_j+K)}\leq\min_Xf$ for all $j$. Since $\omega\geq\theta$, positivity of extended mixed products gives
\[
 e^{-\lambda(\psi_j+K)}\omega_{\psi_j+K}^n
 \leq f\nu_j
 =e^{-\lambda u_j}\mu_{u_j}
 \leq e^{-\lambda u_j}\mathrm{MA}^{\mathrm{ext}}_\omega(u_j).
\]
Apply \cref{cor:singular-exponential-order} in background $\omega$, with first potential $\psi_j+K$ and second potential $u_j$. The first is bounded and admits a smaller-background envelope, and $u_j\preceq\psi_j+K$. Thus $u_j\leq\psi_j+K\leq L+K=:C$. This application requires no volume condition on $\omega$.

For $M_j=\sup_Xu_j$, the lower mass estimate gives
\[
 \kappa\leq e^{\lambda M_j}\|f\|_\infty B.
\]
Their suprema are therefore bounded below as well as above. Compactness yields, after extraction, a genuine $L^1$ limit $u$. By \eqref{eq:relative-normalized-model-bound}, $u_j\leq\varphi+C$. The exponential common-envelope proposition gives a single $h\in\mathcal E_\varphi$ below all $u_j$, since
\[
 \mu_{u_j}\leq\|f\|_\infty e^{\lambda u_j}\omega_{\psi_j}^n.
\]
The moving-measure theorem now applies: $\psi_j\to\psi$ in capacity, $\mu_{u_j}\leq e^{\lambda C}\|f\|_\infty\nu_j$, and the common envelope is available. It gives $u\in\mathcal E_\varphi$, capacity convergence and $\mu_{u_j}\rightharpoonup\mu_u$.

The right-hand sides converge weakly to $e^{\lambda u}f\nu$. To see this, $e^{\lambda u_j}-e^{\lambda u}\to0$ in capacity with a common bound, so its integral against $\nu_j$ tends to zero by their uniform capacity estimate. The fixed function $e^{\lambda u}$ is bounded and quasi-continuous. Approximate it by a continuous function outside an open set of arbitrarily small capacity; bounded product continuity and the same capacity bound allow this fixed weight in $\nu_j\rightharpoonup\nu$. Multiplication by the continuous $f$ and a continuous test function preserves both estimates. Hence $\mu_u=e^{\lambda u}f\nu$.

\emph{Bounded measurable density.} Suppose next $0\leq f\in L^\infty(\nu)$ and $\int_Xf\,\mathrm{d}\nu>0$. Choose positive continuous $f_j$, uniformly bounded by a constant $F$, with $f_j\to f$ almost everywhere for $\nu$. Such a sequence follows from density of continuous functions in $L^1(\nu)$, clipping to a common interval, adding positive constants tending to zero and extracting a summably convergent subsequence.

There is a bounded nonnegative $g$, nonzero as a measure, such that $g\leq f_j$ for all $j$. Indeed, choose $a>0$ with $\nu(\{f\geq2a\})>0$. Egorov's theorem gives a measurable subset $E$ of positive measure on which the convergence is uniform. For some $N$, $f_j\geq a$ on $E$ for $j\geq N$. The finitely many remaining positive continuous functions have positive minima on $X$. Their minima and $a$ have a positive lower bound $b$, so $g=b\mathbf1_E$ works.

By the first step, let $u_j\in\mathcal E_\varphi$ solve $\mu_{u_j}=e^{\lambda u_j}f_j\nu$. The already proved minimal-reference theorem \cref{thm:general-measure-minimal}, applied to the finite nonzero measure $g\nu$, gives $s\in\mathcal E_0$ satisfying
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(s)=e^{\lambda s}g\nu.
\]
Its measure is finite, since $s$ is bounded above. Apply \cref{cor:relative-finite-exponential-order} with reference zero, first potential $s\in\mathcal E_0$ and second potential $u_j\preceq0$. The measure inequality is $g\nu\leq f_j\nu$, so $u_j\leq s$. This application does not require $u_j\preceq s$. With $C=\sup_Xs$ we have
\[
 \mu_{u_j}\leq e^{\lambda C}F\nu,
 \qquad
 \kappa\leq e^{\lambda\sup_Xu_j}F\nu(X).
\]
The two bounds on the suprema give a genuine $L^1$ convergent subsequence. The fixed-measure continuity theorem puts its limit $u$ in $\mathcal E_\varphi$ and identifies the weak limit as $\mu_u$.

The fixed non-pluripolar integration lemma gives $e^{\lambda u_j}\to e^{\lambda u}$ in $L^1(\nu)$. Also $f_j\to f$ in $L^1(\nu)$ by dominated convergence. Since both factors have uniform bounds,
\[
 e^{\lambda u_j}f_j\longrightarrow e^{\lambda u}f
 \quad\hbox{in }L^1(\nu).
\]
Thus the right-hand sides converge in total variation, proving the equation for $f$.

\emph{Integrable density.} For general $f\in L^1(\nu)$, apply the second step to $f_j=\min(f,j)$ and obtain $u_j\in\mathcal E_\varphi$ with $\mu_{u_j}=e^{\lambda u_j}f_j\nu$. The finite-measure exponential order gives $u_{j+1}\leq u_j$, because $f_j\leq f_{j+1}$. Furthermore
\[
 \kappa\leq e^{\lambda\sup_Xu_j}\mu(X),
 \qquad \mu_{u_j}\leq e^{\lambda\sup_Xu_1}\mu.
\]
The decreasing limit is genuine, and the fixed-measure continuity theorem gives $u\in\mathcal E_\varphi$ and $\mu_{u_j}\rightharpoonup\mu_u$. Dominated convergence gives $e^{\lambda u_j}f_j\to e^{\lambda u}f$ in $L^1(\nu)$, so $\mu_u=e^{\lambda u}\mu$. Its measure is finite since $u$ is bounded above. Finite-measure exponential order in both directions proves uniqueness.

\emph{Zero exponent.} For each positive integer $j$, solve the equation just proved with exponent $1/j$, obtaining $u_j\in\mathcal E_\varphi$ with $\mu_{u_j}=e^{u_j/j}\mu$. By the minimal-reference theorem, choose $s\in\mathcal E_0$ solving
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(s)=e^s\mu.
\]
Put $H=\max(0,\sup_Xs)$ and $w_j=s+(j-1)H$. Then $w_j/j\geq s$, whence
\[
 e^{-w_j/j}\mathrm{MA}^{\mathrm{ext}}_\theta(w_j)
 \leq\mu
 =e^{-u_j/j}\mu_{u_j}.
\]
As in the bounded-density step, finite-measure exponential order applies with reference zero, first potential $w_j\in\mathcal E_0$ and second potential $u_j\preceq0$. It gives $u_j\leq w_j\leq jH$. Only an upper bound for $s$ is needed; its mass is finite by its equation.

Set $M_j=\sup_Xu_j$, $v_j=u_j-M_j$ and $c_j=e^{M_j/j}$. Then
\[
 \sup_Xv_j=0,\qquad
 \frac{\kappa}{\mu(X)}\leq c_j\leq e^H,\qquad
 \mu_{v_j}=c_je^{v_j/j}\mu\leq e^H\mu.
\]
The lower bound follows from $\mu_{v_j}(X)\geq\kappa$ and $v_j\leq0$. Extract so that $v_j\to v$ in $L^1(X)$ and $c_j\to c>0$. The limit $v$ is genuine and normalized.

The normalized $L^1$ estimate gives $v_j/j\to0$ in smooth-volume $L^1$. The functions $a_j=e^{v_j/j}$ lie in $[0,1]$, converge to one in that space, and satisfy $\ddc a_j\geq-\omega$ by the bounded convex chain rule. The fixed non-pluripolar integration lemma gives $a_j\to1$ in $L^1(\mu)$. Consequently $\mu_{v_j}=c_ja_j\mu\to c\mu$ in total variation. The fixed-measure continuity theorem gives $v\in\mathcal E_\varphi$ and identifies $\mu_v=c\mu$. Finally, applying the scalar assertion of \cref{cor:relative-finite-exponential-order} in both directions proves that $c$ is unique. It gives no uniqueness assertion for $v$ modulo constants.
\end{proof}

This proves both equations for every finite non-pluripolar measure under the stated semipositive hypotheses. Positive lower volume prevents collapse in the approximations. Capacity convergence identifies the nonlinear operator, and finite domination or capacity bounds control its tails. None of these steps requires a uniform upper bound on the masses of all bounded potentials.


