Run_id: big_minimal_measures_01

Statement: Verify all statements and proofs in the submitted TeX: local radial smoothing and moving integrals, compactness of minimal ordinary-type solutions dominated by the smoothed measure, and BOTH general NPP measure equations in the minimal ENVELOPE class for ANY smooth big real theta under BMP and positive lower minimal relative volume. Also verify that BOTH metric volume properties imply this positive lower minimal volume. Potential uniqueness is asserted only for positive exponent; scalar uniqueness only at exponent zero. This is NOT arbitrary-model existence.

Exact legitimate internal premises (do not silently strengthen):
1. Checkpoint20 section_big_minimal_existence.tex, independently passed big_minimal_existence_01 and comparison_01: for ANY smooth big theta and any nonzero nonnegative Lp smooth-volume density p>1, both positive-exponent and normalized equations have solutions in the ORDINARY type of V_theta, without BMP/PVP. Positive-exponent potential and zero-exponent scalar uniqueness.
2. Checkpoint19 section_big_relative_foundations.tex and section_big_relative_energy.tex, independently passed: under BMP and model reference V with ell>0, every E_V member has MA mass in [ell,M]. Strict/zero domination for u in E_V and v preceq V. Fixed-dominator continuity: u_j in E_V, genuine L1 limit u, MAu_j<=one finite NPP measure implies u in E_V, capacity and raw weak convergence. First-moment criterion: u_j in E_V<=fixed w in E_V, uniform integral(w-u_j)MAu_j implies genuine L1 limits in E_V. Self-measure criterion: u_j,u in E_V, L1 convergence and integral|u_j-u|MAu_j ->0 implies capacity convergence (not raw weak without tails).
3. CONDITIONAL PREMISE separately being verified in big_minimal_moments_01: staged /Users/mingchen/Non-Kahler/research/editorial/section_big_minimal_moments.tex. For probability NPP nu with A_theta(nu)=sup_normalized_theta_psh integral(-w)dnu finite, normalized u~V, B=integral(V-u)MAu, N=2n+1, r=1+1/(4N), integral(V-u)^r dnu<=C(1+A)(1+B)^(1+1/N). This gives UI of u because -V in L1(nu). This audit may accept this precise premise conditionally, but should check every application; no moment estimate for arbitrary nu is available.
4. section_relative_compactness.tex lem:fixed-npp-integrals: uniformly bounded qpsh functions with common smooth lower curvature bound converging in smooth L1 converge in L1 of any FIXED finite NPP measure. It does NOT directly apply to unbounded u_j. chapter_damped_measures.tex thm:general-background-damping: capacity convergence in any smooth background, bounded total masses and uniformly vanishing RAW sublevel tails imply weak convergence of extended MA. Constants max(u,-T) need not be theta-psh; use a larger Hermitian background where needed.
5. section_general_measure_minimal.tex lem:bounded-measure-carrier: for any smooth SEMIPOSITIVE big background (in particular a Hermitian metric omega), every finite NPP mu equals f MA_omega(psi), psi bounded omega-psh, f>=0 integrable. No BMP/PVP is needed for this decomposition. The weighted local CLN estimate stated at the start of section_weak_estimates.tex and normalized qpsh compactness are standard inputs.
6. chapter_envelopes.tex thm:volume-monotonicity and prop:volume-addition, previously reconstructed under BMP: for theta1 big<=theta2 and u1 preceq u2, BOTH lower and upper type volumes are ordered. Addition: vol_alpha(u)<=vol_{alpha+eta}(u+v) for big alpha, u alpha-psh, and smooth eta with v eta-psh. Eta itself need not be big. Scaling vol_{a omega}(0)=a^n v_-(omega). Metric PVP is v_-(omega)>0. V_theta model and sup=0.

XL26 Theorems5.2--5.3 https://arxiv.org/abs/2601.13446v1 (archive /Users/mingchen/Non-Kahler/research/sources/P26.txt) are attribution, not a substitute for the submitted proof. The present argument deliberately proves the actual A_theta bound for smoothed measures and bypasses the source's later Lemma5.2 by using the already established fixed-dominator theorem. Verify every step sequentially with the normal Rethlas workflow; do not modify TeX or manuscript. Persist full findings and final JSON and stop. Scope is conditional only on item3, independently audited.

Proof:

\section{Smoothing a non-pluripolar measure}
\label{sec:big-measure-smoothing}

We keep the assumptions and notation of \cref{sec:big-minimal-moments}. The next argument specifies both the smoothing procedure and the convergence needed for the equation. Weak convergence of the smoothed measures alone would not justify multiplying them by a varying exponential.

Choose finitely many coordinate balls $B_a$, smooth functions $\eta_a\geq0$ with compact support in these balls and $\sum_a\eta_a=1$, and inner neighborhoods of their supports whose closures lie in $B_a$. Let $\chi\geq0$ be a smooth radial convolution kernel on the unit ball of $\mathbb C^n$, of integral one. Fix $\epsilon_j\downarrow0$ small enough for every convolution below to stay in the corresponding coordinate ball. Denote convolution of a function in that chart by $S_{a,j}$. For a probability measure $\nu$, define a smooth probability measure $\nu_j$ by convolving each coordinate measure $\eta_a\nu$ and adding its extensions by zero. Its defining dual identity is
\begin{equation}\label{eq:measure-smoothing-duality}
 \int_X F\,\mathrm{d}\nu_j
 =\sum_a\int_X\eta_a S_{a,j}F\,\mathrm{d}\nu.
\end{equation}
The kernel is even, so the same convolution occurs on the right. This identity first holds for nonnegative Borel functions, and then for integrable signed functions. In particular $\nu_j\rightharpoonup\nu$.

\begin{lemma}\label{lem:measure-smoothing-integrals}
If $\nu$ is non-pluripolar and $A_\theta(\nu)<\infty$, then
\[
 \sup_j A_\theta(\nu_j)<\infty.
\]
More generally, let $z_j,z$ be quasi-plurisubharmonic functions with a common upper bound and a common smooth lower curvature bound. Suppose they converge both in $L^1(X)$ and in $L^1(\nu)$. Then
\begin{equation}\label{eq:convolution-moving-integrals}
 \int_X|z_j-z|\,\mathrm{d}\nu_j\longrightarrow0.
\end{equation}
Consequently, for every $\lambda>0$,
\[
 e^{\lambda z_j}\nu_j\rightharpoonup e^{\lambda z}\nu.
\]
\end{lemma}
\begin{proof}
On each coordinate ball choose a fixed smooth function $q_a$ whose Levi form dominates $\theta$. If $w\in\PSH(X,\theta)$ and $\sup_Xw=0$, then $w+q_a$ is plurisubharmonic. The submean inequality gives
\[
 -S_{a,j}w\leq-w+S_{a,j}q_a-q_a\leq-w+C.
\]
The constant is independent of $w$ and $j$. Integrating \eqref{eq:measure-smoothing-duality} proves $A_\theta(\nu_j)\leq A_\theta(\nu)+C$.

For the second assertion start with any subsequence, and extract so that $z_j\to z$ almost everywhere for smooth volume. The upper envelopes
\[
 H_j=\left(\sup_{k\geq j}z_k\right)^*
\]
decrease to $z$ by Hartogs' lemma and this almost-everywhere convergence. Enlarge the fixed corrections $q_a$ so that $H_j+q_a,z_j+q_a,z+q_a$ are all plurisubharmonic. Since $H_j\geq z_j,z$, the dual identity and the submean inequality imply
\[
 \begin{split}
 \int_X|z_j-z|\,\mathrm{d}\nu_j
 &\leq\sum_a\int_X\eta_a S_{a,j}(2H_j-z_j-z)\,\mathrm{d}\nu\\
 &\leq2\sum_a\int_X\eta_a
       \bigl(S_{a,j}(H_j+q_a)-(z+q_a)\bigr)\,\mathrm{d}\nu
       +\int_X(z-z_j)\,\mathrm{d}\nu.
 \end{split}
\]
All integrals are well defined: each function on the left of a submean inequality is bounded above, and its negative part is controlled by that of its integrable unsmoothed counterpart plus a constant.

Radial averages of a plurisubharmonic function decrease when the radius decreases. Therefore $S_{a,j}(H_j+q_a)$ decreases to $z+q_a$ on the support of $\eta_a$. To identify the limit, fix an index $k$, bound $H_j\leq H_k$ for $j\geq k$, let $j\to\infty$ in the radius, and then let $k\to\infty$. The reverse inequality is the submean inequality. The nonnegative difference in the last display is dominated by an integrable constant minus $z$ on this compact support. Thus its integral tends to zero. The final integral tends to zero by $L^1(\nu)$ convergence. The subsequence criterion proves \eqref{eq:convolution-moving-integrals} for the original sequence.

The exponential is Lipschitz on the common upper range, so its moving $L^1$ error also tends to zero. If $\zeta>0$ is smooth, then $\zeta e^{\lambda z}=e^{\lambda z+\log\zeta}$ is bounded and quasi-plurisubharmonic. For any fixed bounded quasi-plurisubharmonic function $F$, the same local submean argument and dominated convergence in \eqref{eq:measure-smoothing-duality} give
\[
 \int_XF\,\mathrm{d}\nu_j\longrightarrow\int_XF\,\mathrm{d}\nu.
\]
Apply this to $F=\zeta e^{\lambda z}$. Subtracting two positive smooth tests proves the required convergence for every smooth test function. Uniformly bounded masses and uniform approximation of continuous functions by smooth ones prove weak convergence.
\end{proof}

\begin{proposition}\label{prop:big-smoothed-measure-continuity}
Let $\nu$ be a non-pluripolar probability measure with $A_\theta(\nu)<\infty$, and let $\nu_j$ be the smooth measures just defined. Suppose
\[
 v_j\simeq V,\qquad \sup_Xv_j=0,\qquad
 \mu_{v_j}\leq C\nu_j,
 \qquad v_j\longrightarrow v\text{ in }L^1(X).
\]
Then $v\in\mathcal E_V$, convergence also holds in $L^1(\nu)$ and in capacity, and
\[
 \mu_{v_j}\rightharpoonup\mu_v.
\]
\end{proposition}
\begin{proof}
The limit is genuine and normalized, and $v_j,v\leq V\leq0$. The smoothing lemma gives the uniform estimate
\begin{equation}\label{eq:smoothed-first-moment}
 \int_X(-v_j)\,\mu_{v_j}
 \leq C\int_X(-v_j)\,\mathrm{d}\nu_j\leq C'.
\end{equation}
In particular the relative first moments $\int_X(V-v_j)\mu_{v_j}$ are bounded. Proposition~\ref{prop:big-relative-first-moment}, with fixed reference $V$, puts $v$ in $\mathcal E_V$.

Proposition~\ref{prop:big-minimal-higher-moment}, applied to the fixed measure $\nu$, gives uniform integrability of $v_j$ with respect to $\nu$. For each fixed $T$, the bounded functions $\max(v_j,-T)$ have a common lower curvature bound in a Hermitian background $\Omega\geq\theta$ and converge in smooth-volume $L^1$ to $\max(v,-T)$. The fixed non-pluripolar integration lemma gives their $L^1(\nu)$ convergence. Uniform integrability, followed by $T\to\infty$, gives $v_j\to v$ in $L^1(\nu)$. The limit is integrable because $A_\theta(\nu)<\infty$. The truncations need not be $\theta$-plurisubharmonic; they are used only in the larger Hermitian background.

The smoothing lemma now yields
\[
 \int_X|v_j-v|\,\mu_{v_j}
 \leq C\int_X|v_j-v|\,\mathrm{d}\nu_j\longrightarrow0.
\]
The self-measure convergence theorem \cref{thm:big-relative-self-measure-convergence} proves convergence in capacity. Finally \eqref{eq:smoothed-first-moment} gives the raw sublevel estimate
\[
 \sup_j\mu_{v_j}(\{v_j\leq-T\})\leq C'/T.
\]
Their masses are bounded by $M$. The undamped continuity theorem \cref{thm:general-background-damping} therefore gives the asserted weak convergence. This last tail check is a separate step after capacity convergence.
\end{proof}

\section{General measures in an arbitrary big background}
\label{sec:big-minimal-general-measures}

We can now reconstruct the minimal-reference equations of \cite[Theorems 5.2--5.3]{XL26}. We first state the precise volume assumptions used by the proof, and then relate them to the metric assumptions in that paper.

\begin{theorem}\label{thm:big-minimal-general-measures}
Let $X$ be a compact connected complex manifold with the bounded mass property. Let $\theta$ be any smooth big real $(1,1)$-form, and assume
\[
 \underline{\operatorname{vol}}_\theta(V_\theta)>0.
\]
For every finite non-pluripolar measure $\mu$ with $\mu(X)>0$, the following assertions hold.
\begin{enumerate}
\item For every $\lambda>0$ there is a unique $u\in\mathcal E_{V_\theta}$ such that
\[
 \mathrm{MA}_\theta(u)=e^{\lambda u}\mu.
\]
\item There are $v\in\mathcal E_{V_\theta}$ with $\sup_Xv=0$ and a unique scalar $c>0$ such that
\[
 \mathrm{MA}_\theta(v)=c\mu.
\]
\end{enumerate}
Uniqueness of the normalized potential in the second assertion is not claimed. The background need be neither closed nor semipositive. Bounded mass is an assumption of this theorem, not of the general framework of the book.
\end{theorem}
\begin{proof}
First suppose $\mu$ is a probability measure and $A_\theta(\mu)<\infty$. Let $\mu_j$ be its smooth probability approximations. The minimal ordinary-type $L^p$ theorems \cref{thm:big-minimal-exponential,thm:big-minimal-normalized} apply to their smooth, nonzero densities.

For the normalized equation they give $v_j\simeq V$, $\sup_Xv_j=0$, with $\mu_{v_j}=c_j\mu_j$. The mass interval gives $\ell\leq c_j\leq M$. Extract $c_j\to c>0$ and $v_j\to v$ in $L^1(X)$. The preceding proposition applies, so $v\in\mathcal E_V$ and $\mu_{v_j}\rightharpoonup\mu_v$. The right sides converge weakly to $c\mu$, proving the equation.

For the positive-exponent equation take $u_j\simeq V$ satisfying $\mu_{u_j}=e^{\lambda u_j}\mu_j$. Write $a_j=\sup_Xu_j$ and $v_j=u_j-a_j$. The mass interval and Jensen's inequality give
\[
 \ell\leq e^{\lambda a_j},\qquad
 M\geq e^{\lambda a_j}\int_Xe^{\lambda v_j}\,\mathrm{d}\mu_j
       \geq e^{\lambda a_j-\lambda A_\theta(\mu_j)}.
\]
Thus $a_j$ is bounded above and below. After extraction $a_j\to a$, $v_j\to v$ in $L^1(X)$, and $\mu_{v_j}\leq C\mu_j$. The preceding proposition gives $v\in\mathcal E_V$, convergence in $L^1(\mu)$ and weak convergence of the Monge--Amp\`ere measures. Set $u=v+a$. The smoothing lemma identifies the right sides as $e^{\lambda u}\mu$. This proves the equation and membership in $\mathcal E_V$.

The same conclusions hold for any nonzero finite measure whose normalization has finite $A_\theta$: scaling the measure only changes the positive scalar or translates the positive-exponent solution by a constant.

Now let $\mu$ be an arbitrary finite non-pluripolar measure of positive mass. Choose a Hermitian metric $\omega$. The bounded-carrier decomposition \cref{lem:bounded-measure-carrier}, applied to this metric, writes
\[
 \mu=f\nu,\qquad \nu=\mathrm{MA}_\omega(\psi),\qquad
 \psi\in\PSH(X,\omega)\cap L^\infty(X),\qquad
 0\leq f\in L^1(\nu).
\]
For $\mu_k=\min(f,k)\nu$ one has $\mu_k(X)>0$, and its normalization has finite $A_\theta$. Here is the required estimate. On each larger coordinate ball add fixed smooth corrections to $\psi$ and to a normalized $\theta$-plurisubharmonic function $w$. The first becomes bounded plurisubharmonic; shift the second to be negative plurisubharmonic. The positive bounded measure $\mathrm{MA}_\omega(\psi)$ on the inner ball is bounded above by a fixed multiple of the top power of the corrected Hessian of $\psi$: the correction may be chosen with Levi form at least $\omega$. The weighted local Chern--Levine--Nirenberg estimate of \cref{chap:weak-equations} and normalized $L^1$ compactness then give
\[
 \sup_{\substack{w\in\PSH(X,\theta)\\\sup_Xw=0}}
       \int_X(-w)\,\mathrm{d}\nu<\infty.
\]
Multiplication by the bounded density $\min(f,k)$ proves the claim for each $k$. Uniformity in $k$ is not asserted or needed.

For the normalized equation the preceding case gives $v_k\in\mathcal E_V$, $\sup_Xv_k=0$, and $\mu_{v_k}=c_k\mu_k$, with
\[
 \frac{\ell}{\mu(X)}\leq c_k\leq\frac M{\mu_1(X)}.
\]
Extract $c_k\to c>0$ and a genuine $L^1$ limit $v$ of $v_k$. All their Monge--Amp\`ere measures are bounded by the fixed finite non-pluripolar measure $M\mu/\mu_1(X)$. The fixed-dominator theorem \cref{thm:big-relative-fixed-continuity} gives $v\in\mathcal E_V$ and weak convergence to $\mu_v$. Since $c_k\mu_k\to c\mu$ in total variation, $\mu_v=c\mu$.

For the positive-exponent equation let $u_k\in\mathcal E_V$ solve $\mu_{u_k}=e^{\lambda u_k}\mu_k$. Exponential order gives $u_{k+1}\leq u_k$, because $\mu_k$ increases. Also
\[
 \ell\leq\mu_{u_k}(X)\leq e^{\lambda\sup_Xu_k}\mu(X),
 \qquad \mu_{u_k}\leq e^{\lambda\sup_Xu_1}\mu.
\]
The lower bound on the suprema makes the decreasing limit $u$ genuine. The same fixed-dominator theorem puts it in $\mathcal E_V$ and gives weak convergence of the left sides. Dominated convergence with respect to $\nu$, using the integrable bound $e^{\lambda\sup_Xu_1}f$, gives total-variation convergence of the right sides to $e^{\lambda u}\mu$.

Finally strict domination in \cref{thm:big-relative-domination} gives exponential order and uniqueness for two solutions in $\mathcal E_V$. It also gives uniqueness of the positive scalar: two different scalars would allow strict domination against every constant translate of the other potential. The contradiction proves equality of the scalars, without proving equality of the potentials.
\end{proof}

\begin{corollary}\label{cor:metric-pvp-minimal-volume}
If $X$ has both the bounded mass and positive volume properties, then the preceding theorem applies to every smooth big $\theta$.
\end{corollary}
\begin{proof}
Choose $\rho\in\PSH(X,\theta)$ with $\theta_\rho\geq a\omega$ for some $a>0$ and a Hermitian metric $\omega$. Then $\rho\in\PSH(X,\theta-a\omega)$. Volume addition, followed by monotonicity of singularities, gives
\[
 0<a^n v_-(\omega)
 =\underline{\operatorname{vol}}_{a\omega}(0)
 \leq\underline{\operatorname{vol}}_\theta(\rho)
 \leq\underline{\operatorname{vol}}_\theta(V_\theta).
\]
For the addition step the big background is $a\omega$ and the added positive current is $(\theta-a\omega)_\rho$. Bounded mass supplies finiteness of the upper volume. Thus all hypotheses have been checked.
\end{proof}

The theorem concerns the minimal envelope class, which is larger than the ordinary singularity type of $V_\theta$. Its proof uses higher moments only for measures with finite $A_\theta$, and handles the general measure by a separate density truncation with a fixed dominator. For an arbitrary model reference, the construction of the required supersolutions remains a further step.
