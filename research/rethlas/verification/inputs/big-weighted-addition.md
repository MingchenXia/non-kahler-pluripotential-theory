Run_id: big_weighted_addition_01

Statement: Verify the full four-stage weighted-measure addition theorem below. ANY smooth big real theta, BMP, model phi with positive lower relative volume. For u,v in E_phi assume either v has ORDINARY type phi, or MAv is dominated by A MA_omega(psi) with psi BOUNDED omega-psh and omega Hermitian. Prove unique a in E_phi below u,v with MAa=exp(lambda(a-u))MAu+exp(lambda(a-v))MAv. The unweighted sum exp(-lambda u)MAu+exp(-lambda v)MAv may have infinite total mass. If BOTH inputs have ordinary type phi, output does too. No arbitrary-model finite-measure existence is imported; the four stages construct only this addition result.

Exact legitimate internal premises in /Users/mingchen/Non-Kahler/book/author, already reconstructed and independently audited:
1. section_big_relative_foundations.tex: ANY smooth big theta, BMP, model phi with ell=lowerVol_theta(phi)>0, M=upperVol_theta(phi)<infinity. Every E_phi member has raw MA mass in [ell,M]. SAME-CLASS finite rooftops stay in E_phi; ordered stretching Q_b(u,w) stays in E_phi for u<=w in this class. Strict/zero domination: u in E_phi, v preceq phi, 1_{u<v}MAu<=c1_{u<v}MAv with c<1 implies u>=v. Upward stability if h in E_phi and h<=a preceq phi. Envelope identity P_theta[u]=phi for u in E_phi gives u-sup u<=phi.
2. section_big_relative_energy.tex: fixed-reference first-moment criterion for u_j in E_phi below fixed w in E_phi, uniform integral(w-u_j)MAu_j gives lower bounds for sup u_j and genuine L1 limits in E_phi. Its variant assumes u_j<=phi+C and uniform integral(w-u_j)_+ MAu_j. Do not apply it with an index-dependent reference. section_big_relative_foundations.tex thm:big-relative-fixed-continuity: if u_j in E_phi has a GENUINE smooth L1 limit and MAu_j<=one fixed finite NPP measure, then limit is in E_phi, capacity and raw weak convergence hold, and after extraction P_theta(inf_j u_j) lies in E_phi. A fixed dominator alone does NOT prevent constant-shift collapse.
3. section_big_general_contact.tex: every genuine envelope of a finite-a.e. quasi-continuous obstacle in any smooth BIG background has extended MA supported on contact. For finite roofs use disjoint first-contact pieces. Nonclosed local bounded positive products, locality, ordered contact and bounded monotone/capacity continuity are proved in chapter_products.tex. Extended measures ignore pluripolar sets. Weighted capacity lower semicontinuity for bounded nonnegative QC weights is lem:big-weighted-lsc in the foundation source. Monotone capacity convergence with a fixed genuine lower bound follows by constant truncation in a larger Hermitian background. A constant truncation need not be theta-psh.
4. section_relative_compactness.tex lem:fixed-npp-integrals: bounded qpsh with common lower curvature bound and smooth L1 convergence converge in L1 of a FIXED finite NPP measure. For upper-bounded theta-psh functions this applies to their positive exponentials, not directly to unbounded potentials. Normalized qpsh compactness, Hartogs lemma, weighted local CLN, local BT calculus, canonical representatives are standard inputs.
5. Under BMP, every theta-psh potential has finite NPP mass; ordinary-type upper/lower volumes and their monotonicity are reconstructed in chapter_envelopes.tex. In particular phi preceq V_theta gives lowerVol(V_theta)>=lowerVol(phi)>0. Different types may have different masses; no cohomological mass equality is available.

6. Checkpoint21 section_big_minimal_measures.tex, thm:big-minimal-general-measures: under BMP and positive lower MINIMAL relative volume, every finite positive nonzero NPP measure has a unique positive-exponent solution in E_V for arbitrary smooth big theta. It need NOT have ordinary type V. Ordinary type in Stage1 must follow from the explicitly constructed lower barrier and the envelope upper bound.
7. CONDITIONAL PREMISE independently audited in big_weighted_limits_01: /Users/mingchen/Non-Kahler/research/editorial/section_big_weighted_limits.tex. Common h in E_phi below all a_j, common upper bound, genuine smooth L1 limit a preceq phi, and integral|a_j-a|exp(lambda a)MAa_j->0 imply capacity convergence; finite-index a_j need not be in E_phi. Its second lemma identifies the truncated-input weighted equation if u,v,sigma<=0, u,v preceq phi, truncation levels t_j increase to infinity, each input is fixed or max(input,sigma-t_j), input MA masses uniformly bounded, and h<=a_j<=min(u_j,v_j). It yields a in E_phi, capacity and the equation with finite MAa<=MAu+MAv. It does not assert raw weak convergence of original MAa_j. Check every application; may accept the exact two lemmas conditionally.
8. The weighted local CLN/carrier estimate in the proof of thm:big-minimal-general-measures says sup_normalized_theta_psh integral(-z)MA_omega(psi)<infinity for bounded omega-psh psi. It extends to a family with upper AND lower bounds on sup z by translation; the lower bound must first be established.

XL26 Proposition6.1 https://arxiv.org/html/2601.13446v1 (archived P26.txt lines1690--1910) is attribution, not a replacement proof. The submitted last stage replaces the source's Prop4.3 invocation by an additional capped rooftop and the already verified fixed-dominator theorem. Check contact support, cancellation, lack of any factor N in finite roofs, fixed-reference first moments, all subsequence levels, exponent scaling and the potentially infinite weighted measure. Follow normal sequential verification, do not edit TeX/manuscript, persist full findings/final JSON and stop. Scope is conditional only on item7, separately audited.

Proof:

\section{Adding measures in a prescribed class}
\label{sec:big-weighted-addition}

We retain bounded mass, a smooth big real background $\theta$, and a model reference $\varphi$ with positive lower relative volume. The measure
\[
 e^{-\lambda u}\mu_u+e^{-\lambda v}\mu_v
\]
is defined by its finite pointwise weights off the pole sets; it is assigned zero mass on those sets. Its total mass can be infinite. The construction below produces a potential below both $u$ and $v$, making the right side of its equation finite. It reconstructs the four stages of \cite[Proposition 6.1]{XL26}, with the envelope and limiting arguments separated.

\begin{theorem}\label{thm:big-weighted-addition}
Let $u,v\in\mathcal E_\varphi$ and $\lambda>0$. Suppose either $v\simeq\varphi$, or
\[
 \mu_v\leq A\,\mathrm{MA}_\omega(\psi)
\]
for a Hermitian metric $\omega$, a bounded $\omega$-plurisubharmonic function $\psi$, and a finite constant $A>0$. There is a unique $a\in\mathcal E_\varphi$ satisfying
\[
 \mu_a=e^{\lambda(a-u)}\mu_u+e^{\lambda(a-v)}\mu_v.
\]
It satisfies $a\leq\min(u,v)$, and hence $\mu_a\leq\mu_u+\mu_v$. If both $u,v\simeq\varphi$, then also $a\simeq\varphi$.
\end{theorem}
\begin{proof}
It suffices to prove the result for $\lambda=1$. Indeed replace $(\theta,\varphi,u,v)$ by $(\lambda\theta,\lambda\varphi,\lambda u,\lambda v)$. Envelopes and relative classes scale with the potentials, and their volumes and Monge--Amp\`ere measures scale by $\lambda^n$. A bounded-carrier domination remains such a domination after changing its constant. Dividing the resulting solution by $\lambda$ gives the desired equation. A common downward translation of $u,v$ and the solution similarly allows us to assume $u,v\leq\varphi\leq0$; the envelope identity gives this inequality after a sufficiently large common translation. We restore the translation at the end.

Write $V=V_\theta$. Volume monotonicity gives
\[
 \underline{\operatorname{vol}}_\theta(V)
 \geq\underline{\operatorname{vol}}_\theta(\varphi)>0.
\]
Thus the minimal-reference general-measure theorem is available. The finite upper volumes in the ordinary types of $V$ and $\varphi$ will be denoted by $M_V$ and $M$, respectively. No equality of individual masses with these numbers is assumed.

\emph{Ordinary minimal singularities.}
First take $\varphi=V$ and $u,v\simeq V$. Truncate only the weights and define the finite nonzero measures
\[
 \tau_j=e^{-\max(u,-j)}\mu_u+e^{-\max(v,-j)}\mu_v.
\]
The functions $\max(u,-j)$ need not be $\theta$-plurisubharmonic; they occur only as weights in this step. The minimal-reference theorem supplies $a_j\in\mathcal E_V$ with $\mu_{a_j}=e^{a_j}\tau_j$.

Choose $D\geq\tfrac12\|u-v\|_\infty+n\log2$, where the difference is taken off the common poles, and put $w=(u+v)/2-D$. Positivity of mixed products gives
\[
 \mu_w\geq2^{-n}(\mu_u+\mu_v)\geq e^w\tau_j.
\]
Exponential order in $\mathcal E_V$ gives $a_j\geq w$. As $\tau_j$ increases, the same order shows that $a_j$ decreases. The envelope identity gives $a_1\leq V+\sup_Xa_1$, so $a_1\simeq V$ by the lower bound $w$. Consequently
\[
 \mu_{a_j}
 \leq e^{a_1-u}\mu_u+e^{a_1-v}\mu_v
 \leq C(\mu_u+\mu_v).
\]
The decreasing limit $a\geq w$ is genuine and has ordinary type $V$. Fixed-dominator continuity gives weak convergence of the left sides. The right sides converge in total variation by dominated convergence with respect to $\mu_u+\mu_v$. Therefore
\[
 \mu_a=e^{a-u}\mu_u+e^{a-v}\mu_v.
\]
Exponential order, now comparing this equality with each input measure, gives $a\leq u,v$. This order is asserted after passing to the equation; the truncated weights alone would not give it against $u$ and $v$.

\emph{One ordinary model type.}
Suppose $u,v\simeq\varphi$, and put $u_j=\max(u,V-j)$ and $v_j=\max(v,V-j)$. The preceding step gives solutions $a_j\simeq V$ with
\[
 \mu_{a_j}=e^{a_j-u_j}\mu_{u_j}+e^{a_j-v_j}\mu_{v_j},
 \qquad a_j\leq\min(u_j,v_j).
\]
The differences $u_j-v_j$ have the same uniform bound as $u-v$. With $D$ as above, $w_j=(u_j+v_j)/2-D$ satisfies the opposite equation inequality, and exponential order gives
\[
 (u+v)/2-D\leq w_j\leq a_j\leq\min(u_j,v_j).
\]
The fixed lower bound $w=(u+v)/2-D$ has ordinary type $\varphi$, hence lies in $\mathcal E_\varphi$. Extract a genuine $L^1$ limit $a$; it satisfies $w\leq a\leq\min(u,v)$, so $a\simeq\varphi$. The input masses are at most $M_V$. Lemma~\ref{lem:big-truncated-addition-limit}, with truncation reference $V$ and lower bound $w$, proves capacity convergence and the equation. Its use is legitimate although the finite-index solutions have type $V$ and the limit has type $\varphi$.

\emph{One input of ordinary type.}
Now let $u\in\mathcal E_\varphi$ and $v\simeq\varphi$. Set $u_j=\max(u,\varphi-j)$. The second step supplies $a_j\simeq\varphi$ with
\[
 \mu_{a_j}=e^{a_j-u_j}\mu_{u_j}+e^{a_j-v}\mu_v,
 \qquad a_j\leq\min(u_j,v).
\]
We construct a common lower bound in $\mathcal E_\varphi$. Put $\delta=n\log2>0$ and
\[
 s_j=Q_2(a_j,u_j)\in\mathcal E_\varphi,
 \qquad C_j=\{s_j+u_j=2a_j\}.
\]
Stretching and contact give $s_j\leq a_j$ and
\begin{equation}\label{eq:big-addition-stretch-contact}
 2^{-n}\mu_{s_j}+2^{-n}\mathbf1_{C_j}\mu_{u_j}
 \leq\mathbf1_{C_j}\mu_{a_j}.
\end{equation}
On $D_j=\{s_j\leq u-2\delta\}$, contact implies $a_j\leq u_j-\delta$. Since $e^{-\delta}=2^{-n}$, the $\mu_{u_j}$ term cancels in \eqref{eq:big-addition-stretch-contact}. Also $v\geq\varphi-C\geq u_j-C$ for a fixed $C$. Hence
\begin{equation}\label{eq:big-addition-ordinary-tail}
 \mathbf1_{D_j}\mu_{s_j}
 \leq2^n e^C\mathbf1_{D_j\cap C_j}
                e^{(s_j-u_j)/2}\mu_v.
\end{equation}
All measures being subtracted are finite.

For $N\geq1$ form the finite roofs
\[
 R_N=P_\theta(s_1,\ldots,s_N),\qquad q_N=P_\theta(u,R_N).
\]
They belong to $\mathcal E_\varphi$ by the same-class finite-rooftop theorem. On the set $\{R_N\leq u-2\delta\}$, partition contact according to the first index $i$ with $R_N=s_i$. Since $u_i\geq u_N$, \eqref{eq:big-addition-ordinary-tail} gives
\[
 \mathbf1_{\{R_N\leq u-2\delta\}}\mu_{R_N}
 \leq2^n e^C e^{(R_N-u_N)/2}\mu_v.
\]
The contact pieces are disjoint, so there is no factor $N$. On $\{q_N\leq u-2\delta\}$ only the contact part $q_N=R_N$ contributes. Since $u\leq u_N$ and $t e^{-t/2}\leq2/e$ for $t\geq0$, we obtain
\[
 \int_X(u-q_N)\,\mu_{q_N}
 \leq 2\delta M+2^{n+1}e^{C-1}\mu_v(X).
\]
The first term bounds the complementary set, including any contact with $u$. The first-moment criterion, with the fixed reference $u$, implies that the decreasing sequence $q_N$ has a genuine limit $h\in\mathcal E_\varphi$. For each fixed $j$ and every $N\geq j$, $q_N\leq s_j\leq a_j$, so $h\leq a_j$ for every $j$.

The $a_j$ now have a genuine $L^1$ subsequential limit, bounded above by $u,v$. Apply Lemma~\ref{lem:big-truncated-addition-limit}, with reference $\varphi$, fixed second input $v$, and this common lower bound $h$. The input masses are at most $M$. It proves the required equation in $\mathcal E_\varphi$.

\emph{A bounded reference measure for the second input.}
Finally let $u,v\in\mathcal E_\varphi$ and $\mu_v\leq A\nu$, with $\nu=\mathrm{MA}_\omega(\psi)$ and $\psi$ bounded. Again put $u_j=\max(u,\varphi-j)$. By the preceding step, applied with the inputs interchanged, there are $a_j\in\mathcal E_\varphi$ satisfying the same equations and bounds as in the third step.

Let $r=P_\theta(u,v)\in\mathcal E_\varphi$. On $\{a_j<r\}$ one has $r\leq u_j,v$, so $t e^{-t}\leq1/e$ gives
\[
 \int_X(r-a_j)_+\,\mu_{a_j}
 \leq e^{-1}\bigl(\mu_{u_j}(X)+\mu_v(X)\bigr)\leq2M/e.
\]
The one-sided first-moment criterion gives a uniform lower bound for $\sup_Xa_j$, since $a_j\leq\varphi$. The bounded-carrier CLN estimate established in the proof of \cref{thm:big-minimal-general-measures} gives
\[
 \sup_{\substack{z\in\PSH(X,\theta)\\\sup_Xz=0}}
       \int_X(-z)\,\mathrm{d}\nu<\infty.
\]
Applying it to $a_j-\sup_Xa_j$ and using the lower bound for the suprema, we obtain
\begin{equation}\label{eq:big-addition-carrier-moment}
 \sup_j\int_X(u_j-a_j)\,\mu_v
 \leq\sup_j\int_X(-a_j)\,\mu_v<\infty.
\end{equation}

Keep $s_j=Q_2(a_j,u_j)$, $C_j$ and $D_j$ from the third step. The same cancellation in \eqref{eq:big-addition-stretch-contact}, now using only $a_j\leq v$, gives
\[
 \mathbf1_{D_j}\mu_{s_j}
 \leq2^n\mathbf1_{D_j\cap C_j}e^{a_j-v}\mu_v
 \leq2^n\mu_v.
\]
Take one additional rooftop,
\[
 q_j=P_\theta(s_j,u-2\delta)\in\mathcal E_\varphi.
\]
On its contact with $u-2\delta$ its measure is at most $\mu_u$; on its other contact part $q_j=s_j\leq u-2\delta$, the preceding inequality applies. Thus
\begin{equation}\label{eq:big-addition-fixed-roof-measure}
 \mu_{q_j}\leq\mu_u+2^n\mu_v.
\end{equation}
Moreover the energy vanishes on the first contact part. On the other part, the measure is supported on $C_j$, where $u_j-s_j=2(u_j-a_j)$. Therefore
\[
 \int_X(u-2\delta-q_j)\,\mu_{q_j}
 \leq2^{n+1}\int_X(u_j-a_j)\,\mu_v.
\]
This is uniformly bounded by \eqref{eq:big-addition-carrier-moment}. The first-moment criterion with reference $u-2\delta$ prevents collapse of $q_j$. Extract genuine $L^1$ limits of $a_j$ and $q_j$. The fixed-dominator theorem applies to \eqref{eq:big-addition-fixed-roof-measure} and, after a further extraction, gives
\[
 h=P_\theta\left(\inf_jq_j\right)\in\mathcal E_\varphi.
\]
Since $q_j\leq s_j\leq a_j$, this is a common lower bound for the extracted solutions. Lemma~\ref{lem:big-truncated-addition-limit} completes the passage to the equation. Its truncation levels are the original indices of the retained subsequence, not newly assigned levels.

In every stage the solution is at most $u,v$, so its measure is bounded by $\mu_u+\mu_v$. For uniqueness, two solutions $a,b\in\mathcal E_\varphi$ satisfy $\mu_a=e^{a-b}\mu_b$ off the pole sets. Strict domination with constant shifts gives $a=b$. This comparison uses finite Monge--Amp\`ere measures, even if their common exponentially weighted measure has infinite mass. Restoring the common translation and the exponent finishes the proof.
\end{proof}
