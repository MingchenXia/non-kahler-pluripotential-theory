Run_id: big_weighted_limits_01

Statement: Verify both staged lemmas below: (a) weighted self-error plus a common E_phi lower bound yields capacity convergence even when finite-index potentials need NOT belong to E_phi; (b) identify a weighted equation limit for reference truncations (either/both inputs can be fixed) without assuming the undamped weighted reference measure is finite. BMP and positive lower model-reference volume are explicit. Check genuine envelopes across DIFFERENT ordinary types, every cutoff and all measure inequalities. Raw weak convergence of the uncut approximating MA measures is NOT claimed.

Exact legitimate internal premises in /Users/mingchen/Non-Kahler/book/author, already reconstructed and independently audited:
1. section_big_relative_foundations.tex: ANY smooth big theta, BMP, model phi with ell=lowerVol_theta(phi)>0, M=upperVol_theta(phi)<infinity. Every E_phi member has raw MA mass in [ell,M]. SAME-CLASS finite rooftops stay in E_phi; ordered stretching Q_b(u,w) stays in E_phi for u<=w in this class. Strict/zero domination: u in E_phi, v preceq phi, 1_{u<v}MAu<=c1_{u<v}MAv with c<1 implies u>=v. Upward stability if h in E_phi and h<=a preceq phi. Envelope identity P_theta[u]=phi for u in E_phi gives u-sup u<=phi.
2. section_big_relative_energy.tex: fixed-reference first-moment criterion for u_j in E_phi below fixed w in E_phi, uniform integral(w-u_j)MAu_j gives lower bounds for sup u_j and genuine L1 limits in E_phi. Its variant assumes u_j<=phi+C and uniform integral(w-u_j)_+ MAu_j. Do not apply it with an index-dependent reference. section_big_relative_foundations.tex thm:big-relative-fixed-continuity: if u_j in E_phi has a GENUINE smooth L1 limit and MAu_j<=one fixed finite NPP measure, then limit is in E_phi, capacity and raw weak convergence hold, and after extraction P_theta(inf_j u_j) lies in E_phi. A fixed dominator alone does NOT prevent constant-shift collapse.
3. section_big_general_contact.tex: every genuine envelope of a finite-a.e. quasi-continuous obstacle in any smooth BIG background has extended MA supported on contact. For finite roofs use disjoint first-contact pieces. Nonclosed local bounded positive products, locality, ordered contact and bounded monotone/capacity continuity are proved in chapter_products.tex. Extended measures ignore pluripolar sets. Weighted capacity lower semicontinuity for bounded nonnegative QC weights is lem:big-weighted-lsc in the foundation source. Monotone capacity convergence with a fixed genuine lower bound follows by constant truncation in a larger Hermitian background. A constant truncation need not be theta-psh.
4. section_relative_compactness.tex lem:fixed-npp-integrals: bounded qpsh with common lower curvature bound and smooth L1 convergence converge in L1 of a FIXED finite NPP measure. For upper-bounded theta-psh functions this applies to their positive exponentials, not directly to unbounded potentials. Normalized qpsh compactness, Hartogs lemma, weighted local CLN, local BT calculus, canonical representatives are standard inputs.
5. Under BMP, every theta-psh potential has finite NPP mass; ordinary-type upper/lower volumes and their monotonicity are reconstructed in chapter_envelopes.tex. In particular phi preceq V_theta gives lowerVol(V_theta)>=lowerVol(phi)>0. Different types may have different masses; no cohomological mass equality is available.

These proofs are independent deductions from the stated premises, related to XL26 Proposition6.1 Steps2--4 but not applications of its conclusion. Archive /Users/mingchen/Non-Kahler/research/sources/P26.txt; official text https://arxiv.org/html/2601.13446v1. Follow normal sequential Rethlas workflow, do not edit submitted TeX or manuscript, persist all findings and final JSON and stop.

Proof:

\section{Weighted limits with a common relative lower bound}
\label{sec:big-weighted-limits}

We return to a model reference $\varphi=P_\theta[\varphi]$ for an arbitrary smooth big real background $\theta$. Throughout this section $X$ has bounded mass and $\underline{\operatorname{vol}}_\theta(\varphi)>0$. We use the notation and relative class of \cref{sec:big-relative-foundations}. In particular every member of $\mathcal E_\varphi$ has mass in a fixed interval $[\ell,M]$. The next criterion allows the approximating potentials to have different singularity types. Their common lower bound, rather than membership of every approximant in $\mathcal E_\varphi$, supplies the required envelopes.

\begin{lemma}\label{lem:big-weighted-common-bound}
Let $a_j\in\PSH(X,\theta)$ have a common upper bound and converge in $L^1(X)$ to a genuine $a\preceq\varphi$. Suppose there is $h\in\mathcal E_\varphi$ such that $h\leq a_j$ for every $j$. If, for some $\lambda>0$,
\[
 \int_X|a_j-a|e^{\lambda a}\,\mu_{a_j}\longrightarrow0,
\]
then $a\in\mathcal E_\varphi$ and $a_j\to a$ in capacity. The approximants need not lie in $\mathcal E_\varphi$.
\end{lemma}
\begin{proof}
The order passes to the canonical limit, so $h\leq a\preceq\varphi$. Upward stability gives $a\in\mathcal E_\varphi$.
Start with any subsequence and extract again so that the displayed integrals are at most $2^{-j}$ and smooth-volume almost-everywhere convergence holds. The finite roofs
\[
 p_{j,N}=P_\theta(a_j,\ldots,a_N)
\]
are genuine because $h$ is a competitor. Disjoint first-contact pieces give
\[
 \int_X\min(1,|p_{j,N}-a|)e^{\lambda a}\,\mu_{p_{j,N}}
 \leq\sum_{k=j}^N\int_X|a_k-a|e^{\lambda a}\,\mu_{a_k}
 \leq2^{1-j}.
\]
No relative-class assertion about these finite roofs is needed. Their decreasing limits $p_j=P_\theta(\inf_{k\geq j}a_k)$ are genuine and at least $h$. Almost-everywhere convergence gives $p_j\leq a$. Hence $p_j$ and their increasing canonical limit $p$ lie in $\mathcal E_\varphi$.

The limits in $N$ and then in $j$ converge in capacity, using the genuine lower bound $h$. Apply weighted lower semicontinuity \cref{lem:big-weighted-lsc} twice to the bounded weights
$\min(1,|p_{j,N}-a|)e^{\lambda a}$ and their limits. They converge in capacity: discard deep sublevels of $h$ and $a$, then use continuity on the remaining finite ranges. We obtain
\[
 \int_X\min(1,|p-a|)e^{\lambda a}\,\mu_p=0.
\]
The exponential is positive off a pluripolar set, which $\mu_p$ ignores. Zero domination therefore gives $p=a$. The upper tail envelopes $(\sup_{k\geq j}a_k)^*$ decrease to $a$. Squeezing proves capacity convergence along this extraction. The subsequence criterion gives it for the original sequence.
\end{proof}

We next identify a limit equation whose undamped reference measure can have infinite mass. We state the argument for exponent one; rescaling the background and potentials gives the general exponent, as explained in the next section.

\begin{lemma}\label{lem:big-truncated-addition-limit}
Let $u,v,\sigma\in\PSH(X,\theta)$ be nonpositive, with $u,v\preceq\varphi$, and let $t_j\uparrow\infty$. Each of $u_j,v_j$ is either the fixed corresponding potential or its truncation
\[
 u_j=\max(u,\sigma-t_j),\qquad
 v_j=\max(v,\sigma-t_j).
\]
At least one may be fixed. Suppose their Monge--Amp\`ere masses are uniformly bounded, and suppose
\[
 \mu_{a_j}=e^{a_j-u_j}\mu_{u_j}+e^{a_j-v_j}\mu_{v_j},
 \qquad h\leq a_j\leq\min(u_j,v_j),
\]
where $h\in\mathcal E_\varphi$ is fixed. If $a_j\to a$ in $L^1(X)$, then $a\in\mathcal E_\varphi$, convergence holds in capacity, and
\[
 a\leq\min(u,v),\qquad
 \mu_a=e^{a-u}\mu_u+e^{a-v}\mu_v.
\]
The measure on the right is finite, even when $e^{-u}\mu_u+e^{-v}\mu_v$ has infinite total mass.
\end{lemma}
\begin{proof}
The bounds give $h\leq a\leq\min(u,v)\preceq\varphi$, so $a\in\mathcal E_\varphi$. All potentials $a_j,a$ are nonpositive. Let $E_j$ be the intersection of the strict sets $\{u>\sigma-t_j\}$ and $\{v>\sigma-t_j\}$ for those potentials that are actually truncated. A fixed potential imposes no condition. On $E_j$ locality gives $\mu_{u_j}=\mu_u$ and $\mu_{v_j}=\mu_v$. Since $a,a_j\leq u_j,v_j$, we have
\[
 e^a\mu_{a_j}
 \leq e^{(a+a_j)/2}(\mu_{u_j}+\mu_{v_j}).
\]
If $x\notin E_j$, one truncated input and its limit are at most $-t_j$, so both $a_j(x),a(x)\leq-t_j$. Also $|a_j-a|e^{(a+a_j)/4}$ is bounded by an absolute constant, since $a_j,a\leq0$. Thus
\begin{equation}\label{eq:big-addition-weighted-error}
 \int_X|a_j-a|e^a\,\mu_{a_j}
 \leq\int_X|a_j-a|e^{(a+a_j)/2}(\mu_u+\mu_v)
       +C e^{-t_j/2}.
\end{equation}
Here the assumed uniform mass bound is used only in the last term. The fixed measure $\mu_u+\mu_v$ is finite by bounded mass. The fixed non-pluripolar integration lemma applied to $e^{a_j},e^a$ gives convergence in measure of $a_j$ to $a$ for that measure, since $a$ is finite almost everywhere. The first integrand in \eqref{eq:big-addition-weighted-error} is uniformly bounded and tends to zero in measure. Its integral tends to zero. The preceding lemma now proves capacity convergence. Truncation levels $t_j$ are retained when a subsequence is taken.

To identify the equation, put $\chi_T=g_T(h)$, where $g_T$ is continuous and nondecreasing, zero on $[-\infty,-2T]$ and one on $[-T,0]$, with $g_T\uparrow1$ at finite points. We have $h\leq u,v$ by passing to the limit in the upper bounds. On the support of $\chi_T$, both $u$ and $v$ exceed $-2T$. Therefore, once $t_j>2T$, every truncated input agrees there with its limit, and
\[
 \chi_T\mu_{a_j}
 =\chi_Te^{a_j}(e^{-u}\mu_u+e^{-v}\mu_v).
\]
Choose a Hermitian form $\Omega\geq\theta$. On the left replace $a_j$ by $\max(a_j,-2T)$ and expand the bounded product as
\[
 (\theta+\ddc\max(a_j,-2T))^n
 =\sum_{k=0}^n\binom nk
   (\Omega+\ddc\max(a_j,-2T))^k\wedge(\theta-\Omega)^{n-k}.
\]
The cutoff vanishes at the truncation level. Bounded capacity continuity with the fixed quasi-continuous weight $\chi_T$ therefore gives convergence to $\chi_T\mu_a$, after testing against a continuous function. The uncut product may be signed; its terms have uniformly capacity-controlled total variations.

On the right, $\chi_T e^{-u}$ and $\chi_T e^{-v}$ are bounded by $e^{2T}$. Fixed-measure exponential convergence gives convergence in total variation to
$\chi_Te^a(e^{-u}\mu_u+e^{-v}\mu_v)$. Let $T\to\infty$. The limiting right side is at most $\mu_u+\mu_v$, because $a\leq u,v$. Both sides ignore the polar set of $h$, so the cutoff identities prove the global equation and its finiteness. No raw weak convergence of the uncut approximating measures was asserted in this argument.
\end{proof}
