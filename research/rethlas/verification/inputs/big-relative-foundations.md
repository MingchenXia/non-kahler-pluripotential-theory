Run_id: big_relative_foundations_01

Statement: Verify the complete staged manuscript section below, including all its lemmas and theorems, in textual order. X is compact connected Hermitian, theta is ANY smooth big real (1,1)-form, not assumed semipositive or closed. This bounded subtheory explicitly assumes bounded mass and a model phi=P_theta[phi] whose relative lower volume ell is positive; its upper volume M is finite. No separate global metric positive-volume property is assumed or to be inferred. Claims: stretching stays in the relative class, every finite rooftop is genuine and in that class, strict domination, weighted capacity lower semicontinuity for ANY smooth background with extended products, and fixed finite dominating measure gives an extracted common relative lower envelope, membership of the L1 limit, capacity convergence and weak raw-measure convergence. The full Li existence theorem is NOT a premise or claimed as proved.

Legitimate internal premises, all already proved at the indicated precise scope, may be read in the current manuscript at /Users/mingchen/Non-Kahler/book/author/:
1. chapter_envelopes.tex: def:relative-envelope-class defines E_env by all convex competitors A_b, b>=1, AND u preceq phi; thm:relative-equivalence under BMP, arbitrary smooth BIG theta and positive LOWER reference volume identifies it with the UPPER-volume-equality class and proves equality of both volumes for every member. prop:relative-elementary gives convexity, bounded-change and upward stability. prop:relative-envelope-equality gives P_theta[u]=P_theta[phi] for E_env in ANY smooth big theta, without BMP. These exact definitions and results may be treated as established internal premises, not as new claims in this audit. Upper/lower volume are sup/inf of mass over ordinary bounded-difference singularity type, not a fixed mass.
2. section_big_general_contact.tex and chapter_envelopes.tex: genuine envelope contact support for finite-a.e. quasi-continuous obstacles in ANY smooth big background; ordered-contact inequality whenever canonical theta-psh functions are ordered, and positive mixed products on common finite levels. No semipositivity, BMP or positive-volume hypotheses are needed for those premises. Differences at poles are used only through convex inequalities off poles and canonical extension, never by subtracting infinities.
3. Normalized quasi-psh L1 compactness, Hartogs lemma, canonical representatives, bounded Bedford--Taylor capacity continuity, bounded mixed capacity estimates for a Hermitian background (lem:bounded-mixed-capacity in section_relative_compactness.tex), and deep sublevel capacity decay for one genuine quasi-psh function are established standard local/global inputs.
4. lem:fixed-npp-integrals in section_relative_compactness.tex: a uniformly bounded family of quasi-psh functions with common smooth lower curvature bound converging in smooth-volume L1 converges in L1 of every FIXED finite non-pluripolar measure. Applies to e^u after a common upper normalization. This premise does not imply capacity convergence of the original unbounded u.
5. thm:general-background-damping in chapter_damped_measures.tex: for arbitrary smooth theta, capacity convergence of theta-psh potentials plus uniform total mass and uniformly vanishing raw deep-sublevel masses implies weak convergence of extended MA measures and finiteness of the limit. Constant truncations are only Omega-psh for an enlarged Hermitian Omega; their theta products are signed until the cutoff is applied. Do not treat constant truncations as theta-psh.

Audit all new arguments, including finite-family collapse and independent optimization of equivalent representatives, coefficient-one ordered contact in domination, the signed bounded products in the new lower-semicontinuity lemma, disjoint first-contact partitions (no factor N for a fixed dominator), and preservation of all prefix indices in the common-rooftop extraction. The exact staged text follows. XL26 references indicate reconstruction attribution, not imported use of its conclusions. The original source is archived at research/sources/P26.pdf and P26.txt and at https://arxiv.org/abs/2601.13446v1. No assertion about paper novelty is requested. Do not modify the submitted TeX or root manuscript. Follow your normal sequential verification workflow, persist all records and final JSON, and stop after final output.

Proof:

\section{Relative envelopes in a general big background}
\label{sec:big-relative-foundations}

We now allow $\theta$ to be any smooth big real $(1,1)$-form. The assumptions in this section replace the semipositivity and smaller-background hypotheses used earlier in the chapter. We assume bounded mass and fix a model reference $\varphi=P_\theta[\varphi]$ with
\[
 \ell:=\underline{\operatorname{vol}}_\theta(\varphi)>0,
 \qquad M:=\overline{\operatorname{vol}}_\theta(\varphi)<+\infty.
\]
Write $\mathcal E_\varphi$ for either of the equal classes in \cref{thm:relative-equivalence}, and put $\mu_u=\mathrm{MA}_\theta(u)$. Every member satisfies
\begin{equation}\label{eq:big-relative-mass-interval}
 \ell\leq\mu_u(X)\leq M.
\end{equation}
These bounds concern the singularity class. We do not assume separately that every Hermitian metric has positive lower volume. The arguments below reconstruct the relative envelope and domination results of \cite[Sections 3--4]{XL26} in the precise regime just stated. The general-measure existence theorem \cref{thm:li-general-measure} still retains both of its metric volume hypotheses.

\begin{lemma}\label{lem:big-relative-stretch}
If $u,w\in\mathcal E_\varphi$ and $u\leq w$, then $Q_b(u,w)$ is genuine and belongs to $\mathcal E_\varphi$ for every $b\geq1$.
\end{lemma}
\begin{proof}
First translate so that $u,w\leq\varphi$. Put $u_t=Q_t(u,\varphi)$, which is genuine by the definition of the class. If $t>bs$, with $s\geq1$, the defining convex inequality gives
\[
 \frac bt u_t+\left(1-\frac bt\right)\varphi\leq Q_b(u,\varphi),
\]
because the left side is a competitor. Consequently
\[
 \frac{bs}{t}u_t+\left(1-\frac{bs}{t}\right)\varphi
 \leq sQ_b(u,\varphi)-(s-1)\varphi.
\]
This supplies every convex competitor required for $Q_b(u,\varphi)\in\mathcal E_\varphi$. Also
\[
 Q_b(u,\varphi)\leq Q_b(u,w)\leq u\leq\varphi.
\]
Upward stability proves the assertion. The displayed differences are interpreted through convex inequalities, as before. Only convex combinations in the same background have been used; no scaling towards a constant is involved.
\end{proof}

\begin{proposition}\label{prop:big-relative-finite-rooftops}
For $u_1,\ldots,u_p\in\mathcal E_\varphi$, the envelope $P_\theta(u_1,\ldots,u_p)$ is genuine and belongs to $\mathcal E_\varphi$.
\end{proposition}
\begin{proof}
Normalize $\varphi\leq0$. Suppose first that the envelope is not genuine. This remains true if each $u_i$ is replaced by any $u_i'\simeq u_i$: a common constant translation converts a competitor for one finite family into a competitor for the other. Translate the $u_i'$ so that $u_i'\leq\varphi$, and define
\[
 v_{i,k}=\max(u_i',\varphi-k),\qquad
 p_k=P_\theta(v_{1,k},\ldots,v_{p,k}).
\]
Then $\varphi-k\leq p_k\leq\varphi$, so $p_k\simeq\varphi$. The decreasing sequence has no genuine limit; hence $\sup_Xp_k\to-\infty$. For $k>s>0$ and then $k$ sufficiently large, contact support and ordered contact give
\[
 \begin{split}
 \ell\leq\mu_{p_k}(X)
 &\leq\sum_{i=1}^p\mu_{v_{i,k}}(\{v_{i,k}\leq-s\})\\
 &\leq\sum_{i=1}^p
       \left(M-\mu_{u_i'}(\{u_i'>-s\})\right).
 \end{split}
\]
For the last inequality, $v_{i,k}\simeq\varphi$, while on $\{u_i'>-s\}$ one has $u_i'>\varphi-k$ and locality applies. Let $s\to\infty$. All measures are finite and ignore poles, so
\[
 \ell\leq pM-\sum_{i=1}^p\mu_{u_i'}(X).
\]
For each $i$, the supremum of these masses over $u_i'\simeq u_i$ is $M$. Taking these suprema independently contradicts $\ell>0$. The envelope is therefore genuine.

For class membership translate so that $u_i\leq\varphi$. The preceding lemma puts $Q_b(u_i,\varphi)$ in $\mathcal E_\varphi$. Their finite rooftop $r_b$ is genuine by what we have just proved. If $p=P_\theta(u_1,\ldots,u_p)$, then
\[
 b^{-1}r_b+(1-b^{-1})\varphi\leq p,
\]
since the left side is a $\theta$-plurisubharmonic competitor below every $u_i$. This verifies every defining envelope condition for $p$; also $p\preceq\varphi$.
\end{proof}

\begin{theorem}\label{thm:big-relative-domination}
Let $u\in\mathcal E_\varphi$, $v\in\PSH(X,\theta)$ with $v\preceq\varphi$, and $0\leq c<1$. If
\[
 \mathbf1_{\{u<v\}}\mu_u\leq c\,\mathbf1_{\{u<v\}}\mu_v,
\]
then $u\geq v$.
\end{theorem}
\begin{proof}
Replace $v$ by $\max(u,v)$. Locality preserves the hypothesis and upward stability puts the new $v$ in $\mathcal E_\varphi$. A common translation gives $u\leq v\leq\varphi\leq0$. Set
\[
 q_b=Q_b(u,v),\qquad
 D_b=\{b^{-1}q_b+(1-b^{-1})v=u\}.
\]
The preceding stretching lemma gives $q_b\in\mathcal E_\varphi$ and $q_b\leq u$. Contact support and positivity of the mixed products give
\[
 b^{-n}\mu_{q_b}+(1-b^{-1})^n\mathbf1_{D_b}\mu_v
 \leq\mathbf1_{D_b}\mu_u.
\]
Here $\mu_{q_b}$ is supported on $D_b$. Choose $b$ so large that $(1-b^{-1})^n>c$. Subtracting finite measures on $D_b\cap\{u<v\}$ shows that $\mu_{q_b}$ vanishes there. Thus it is supported on $D_b\cap\{u=v\}\subset\{q_b=u\}$. Since $q_b\leq u$, ordered contact with coefficient one now gives
\begin{equation}\label{eq:big-domination-fixed-tail}
 \ell\leq\mu_{q_b}(X)\leq\mu_u(\{q_b=u\}).
\end{equation}

If $u<v$ anywhere, there is $\delta>0$ such that $\{u<v-\delta\}$ has positive smooth volume. Indeed, the contrary would give $u\geq v$ almost everywhere and then everywhere for canonical quasi-plurisubharmonic representatives. On this set
$q_b\leq u-(b-1)\delta$. The family $q_b$ decreases in $b$ and is bounded above by $u$. A genuine limit could not be $-\infty$ on a set of positive smooth volume. Hence its limit is identically $-\infty$, and Hartogs' lemma gives $\sup_Xq_b\to-\infty$. The sets $\{q_b=u\}$ then have $\mu_u$-mass tending to zero by dominated convergence off the pole set of $u$. This contradicts \eqref{eq:big-domination-fixed-tail}.
\end{proof}

The exponential order and uniqueness of the positive scalar follow exactly by applying this theorem to $v-\delta$ and then letting $\delta\downarrow0$, or by applying it to all constant translates of $v$, respectively. Thus the third regime in \cref{thm:relative-domination} now has an internal proof. Potential uniqueness for the equation without an exponential does not follow.

\section{Capacity and measures in a general big background}
\label{sec:big-relative-continuity}

We keep the hypotheses of \cref{sec:big-relative-foundations}. To use capacity arguments, one must first justify the cutoff calculation when a constant truncation is not $\theta$-plurisubharmonic.

\begin{lemma}\label{lem:big-weighted-lsc}
Let $\theta$ be any smooth real $(1,1)$-form. Suppose $u_j,u\in\PSH(X,\theta)$ have a common upper bound and converge in capacity. If nonnegative uniformly bounded quasi-continuous functions $a_j,a$ also converge in capacity, then
\[
 \int_Xa\,\mathrm{MA}^{\mathrm{ext}}_\theta(u)
 \leq\liminf_j\int_Xa_j\,\mathrm{MA}^{\mathrm{ext}}_\theta(u_j).
\]
No mass or bigness assumption is needed for this lemma.
\end{lemma}
\begin{proof}
Translate the potentials below zero and choose a Hermitian metric $\Omega\geq\theta$. Let $g_T$ be a continuous nondecreasing cutoff, zero on $[-\infty,-2T]$, one on $[-T,0]$, increasing to one at finite points. Put $v_j=\max(u_j,-2T)$ and $v=\max(u,-2T)$. These are uniformly bounded $\Omega$-plurisubharmonic functions and converge in capacity. Expand their bounded signed products as
\[
 (\theta+\ddc v_j)^n
 =\sum_{k=0}^n\binom nk
       (\Omega+\ddc v_j)^k\wedge(\theta-\Omega)^{n-k}.
\]
The total variations of these terms are uniformly bounded by a constant times the bounded mixed measures with background $\Omega$. These measures satisfy a common capacity estimate. Bounded Bedford--Taylor continuity therefore applies with the bounded quasi-continuous weights $a_jg_T(v_j)$: remove a set of arbitrarily small capacity to use continuous weights, control its error by the capacity bound, and then restore it. Locality and the vanishing cutoff on the truncation level give
\[
 \begin{split}
 \int_Xa_jg_T(u_j)\,\mathrm{MA}^{\mathrm{ext}}_\theta(u_j)
 &=\int_Xa_jg_T(v_j)(\theta+\ddc v_j)^n\\
 &\longrightarrow
 \int_Xag_T(u)\,\mathrm{MA}^{\mathrm{ext}}_\theta(u).
 \end{split}
\]
The first integral is positive and bounded above by the corresponding uncut integral, although the bounded product before multiplication may be signed. Let $T\to\infty$ and use monotone convergence. This also explains the general-background version of the cutoff argument in \cref{thm:general-background-damping}.
\end{proof}

Monotone capacity convergence with a fixed genuine lower bound transfers to this setting by the same choice of $\Omega$. Truncate in the $\Omega$ background, apply bounded monotone convergence, and control the discarded set by the deep sublevels of that fixed lower bound. No assertion of positivity for the uncut $\theta$-product is required.

\begin{theorem}\label{thm:big-relative-fixed-continuity}
Suppose $u_j\in\mathcal E_\varphi$, $u_j\to u\in\PSH(X,\theta)$ in $L^1(X)$, and $\mu_{u_j}\leq\nu$ for one finite non-pluripolar measure $\nu$. There is a subsequence with
\[
 h=P_\theta\left(\inf_j u_j\right)\in\mathcal E_\varphi.
\]
For the original sequence,
\[
 u\in\mathcal E_\varphi,\qquad
 u_j\longrightarrow u\text{ in capacity},\qquad
 \mu_{u_j}\rightharpoonup\mu_u\leq\nu.
\]
\end{theorem}
\begin{proof}
The envelope identity $P_\theta[u_j]=\varphi$ and Hartogs' lemma give $u_j\leq\varphi+C$ uniformly. After a common translation, suppose $u_j\leq\varphi\leq0$, hence $u\leq\varphi$. The fixed non-pluripolar integration lemma applies to the bounded quasi-plurisubharmonic functions $e^{u_j},e^u$, after enlarging a Hermitian background. Extract once so that $u_j\to u$ almost everywhere for smooth volume and
\[
 I_j:=\int_X|e^{u_j}-e^u|\,\mu_{u_j}\leq2^{-j}.
\]
Put $p_{j,N}=P_\theta(u_j,\ldots,u_N)$. The finite-rooftop proposition puts these potentials in $\mathcal E_\varphi$. Partition the contact set by the first index realizing the minimum. The pieces are disjoint, so ordered contact gives
\begin{equation}\label{eq:big-finite-roof-domination}
 \mu_{p_{j,N}}\leq\nu,\qquad
 \int_X|e^{p_{j,N}}-e^u|\,\mu_{p_{j,N}}\leq2^{1-j}.
\end{equation}
There is no factor equal to the number of obstacles in the first bound.

Fix $B\geq1$ and put $r_{j,N}=Q_B(p_{j,N},\varphi)$. Stretching preserves the class, and contact support gives
\[
 \mu_{r_{j,N}}\leq B^n\nu,\qquad
 \mu_{r_{j,N}}(X)\geq\ell.
\]
On its contact set one has
$p_{j,N}=B^{-1}r_{j,N}+(1-B^{-1})\varphi\leq B^{-1}r_{j,N}$.
It follows that
\[
 \int_Xe^u\,\mu_{r_{j,N}}
 \leq B^n2^{1-j}+B^n\nu(X)e^{\sup_Xr_{j,N}/B}.
\]
Choose $K>0$ with $B^n\nu(\{u\leq-K\})<\ell/2$. The same integral is at least $e^{-K}\ell/2$. For $j$ sufficiently large the preceding inequality therefore bounds $\sup_Xr_{j,N}$ from below independently of $N$. Since $r_{j,N}$ decreases in $N$ and is at most $\varphi$, it has a genuine limit $R\leq\varphi$, satisfying
\[
 B^{-1}R+(1-B^{-1})\varphi\leq u_k\qquad(k\geq j).
\]

For any $b\geq1$ use this construction with $B=2b$. Set
$S=Q_{2b}(P_\theta(u_1,\ldots,u_{j-1}),\varphi)$ if $j>1$, and $S=\varphi$ otherwise. This is genuine and $S\leq\varphi$. Then $H=(R+S)/2$ satisfies
\[
 b^{-1}H+(1-b^{-1})\varphi\leq u_k\qquad(k\geq1).
\]
For a tail index use the inequality for $R$ and $S\leq\varphi$; for an earlier index use the inequality for $S$ and $R\leq\varphi$. The case $b=1$ proves that $h=P_\theta(\inf_k u_k)$ is genuine. Every $b$ supplies its defining convex competitor. Thus $h\in\mathcal E_\varphi$. The inequalities $h\leq u\leq\varphi$ also give $u\in\mathcal E_\varphi$ by upward stability.

Set $p_j=P_\theta(\inf_{k\geq j}u_k)$ and $p=(\lim_jp_j)^*$. The limits $p_{j,N}\downarrow p_j$ and $p_j\uparrow p$ have the fixed lower bound $h$, so hold in capacity. Every potential belongs to $\mathcal E_\varphi$, and $p\leq u$. Applying \cref{lem:big-weighted-lsc} to \eqref{eq:big-finite-roof-domination}, first in $N$ and then in $j$, gives
\[
 \int_X|e^p-e^u|\,\mu_p=0.
\]
The measures ignore poles, so $\mu_p(\{p<u\})=0$. The general big-background domination theorem with coefficient zero yields $p=u$. The upper tail envelopes $(\sup_{k\geq j}u_k)^*$ decrease to $u$ by Hartogs' lemma and the almost-everywhere extraction. Squeezing $u_j$ between these and $p_j$ proves capacity convergence along the extracted sequence.

Finally
\[
 \mu_{u_j}(\{u_j\leq-T\})\leq\nu(\{h\leq-T\})\longrightarrow0
\]
uniformly in $j$. The general-background undamped tail theorem proves weak convergence to $\mu_u$, and weak limits preserve domination by $\nu$. Starting with an arbitrary original subsequence gives a further subsequence with these same conclusions. Hence capacity and weak convergence hold for the original sequence.
\end{proof}

The upper volume bound enters the construction of finite rooftops. Their stretched versions then have the positive lower mass $\ell$, which prevents collapse. The fixed measure controls the tails only after a common lower envelope has been constructed. These are different uses of the hypotheses. This proves the fixed-measure continuity statement of \cite[Theorem 4.2]{XL26}; the construction of solutions to the general big-background equation is a further step.
