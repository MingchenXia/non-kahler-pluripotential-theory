Run_id: relative_measure_carrier_01

Statement: Audit a representation theorem for finite NPP measures within a prescribed ORDINARY singularity type, without BMP or PVP: theta smooth semipositive big; phi theta-psh with genuine P_(epsilon theta)(phi), epsilon<1; every finite NPP mu=f MA_theta^ext(psi), psi~phi, f integrable. MApsi may have INFINITE mass. This is not an equation existence theorem.

Accepted prerequisites: local positive mixed non-pluripolar products, plurifine locality and positivity on finite truncation levels, quasi-psh maxima/pasting, canonical representatives, smooth strict big potential theta_rho>=a omega, RN theorem for sigma-finite measures. Read exact conventions book/author/chapter_products.tex, chapter_envelopes.tex, and section_exponential_rooftop_barrier.tex. The latter has passed exponential_rooftop_barrier_01 and contains the same theta_s>=delta omega_psi NPP comparison; check usages.

Conditional prerequisite currently audited separately in general_measure_minimal_01: ONLY the LOCAL assertion in lemma bounded-measure-carrier of book/author/section_general_measure_minimal.tex: on a bounded coordinate ball, every compactly supported finite NPP tau is absolutely continuous relative to (ddc v)^n for some bounded local psh v. This follows from Cegrell1998Theorem6.3 when n>=2 and an explicit Green-potential exponential when n1. You may treat this exact local assertion as a conditional input and inspect the proof. Do not assume global representation or any equation existence. Inclusion will wait for BOTH audits. Ceg98 primary in research/sources/Ceg98.pdf physical23; local E0definition physical2. No new external paper is otherwise invoked in this proposition.

Check all small steps, especially stronger singularity s<=phi strict while possibly unbounded; gluing with s rather than phi-m; difference bounds q_im~phi; domination on D_im by bounded local product with s unbounded; finite-point union over m and common nullsets; countable convex sum with weighted bounded RELATIVE differences, genuine monotone limit, fixed-summand decomposition; common-pole-set restriction and extended positivity; SIGMA-finiteness (not finiteness) for Radon-Nikodym. No boundedness of s, q_im, psi may be silently used. phi need not be model; no hidden PVP or BMP. Final paragraph must not overclaim ability to solve equations from this representation.

Proof:

\section{A measure with a prescribed ordinary type}
\label{sec:relative-measure-carrier}

The preceding local patching can retain an unbounded reference's ordinary singularity type. The resulting Monge--Amp\`ere measure need not be finite, so it is essential to keep the integrable density in the conclusion.

\begin{proposition}\label{prop:relative-measure-carrier}
Let $\theta\geq0$ be smooth and big, and let $\varphi\in\PSH(X,\theta)$ admit a genuine $P_{\epsilon\theta}(\varphi)$ for some $0<\epsilon<1$. For every finite non-pluripolar measure $\mu$ there are
\[
 \psi\in\PSH(X,\theta),\qquad\psi\simeq\varphi,
 \qquad 0\leq f\in L^1\bigl(\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)\bigr)
\]
such that
\[
 \mu=f\,\mathrm{MA}^{\mathrm{ext}}_\theta(\psi).
\]
Neither a model fixed-point condition on $\varphi$ nor an upper or lower volume property is assumed. The density is not asserted to be bounded, and the reference measure is allowed to have infinite total mass.
\end{proposition}
\begin{proof}
Translate $\varphi$ below zero. Put $q=P_{\epsilon\theta}(\varphi)\leq\varphi$, and choose a strict big potential $\rho\leq0$ with $\theta+\ddc\rho\geq a\omega$, where $a>0$. Then
\[
 s=q+(1-\epsilon)\rho\leq\varphi,\qquad
 \theta+\ddc s\geq(1-\epsilon)a\omega.
\]
In particular $s$ is genuine. Its pole set is pluripolar, as is that of $\varphi$, so both are negligible for $\mu$.

Choose finitely many compact inner coordinate balls $K_i$ covering $X$, with larger balls $B_i$. Apply the local measure assertion in the proof of \cref{lem:bounded-measure-carrier} to $\mu_i=\mathbf1_{K_i}\mu$. This gives bounded local plurisubharmonic $v_i$, normalized by $1\leq v_i\leq2$, with
\[
 \mu_i\ll\nu_i:=(\ddc v_i)^n.
\]
Take a smooth cutoff $\chi_i$ which is zero near $K_i$ and $-3$ on a boundary collar of $B_i$. Choose $\delta_i>0$ so small that
\[
 \theta+\ddc\bigl(s+\delta_i(v_i+\chi_i)\bigr)
 \geq\tfrac12(1-\epsilon)a\omega+\delta_i\ddc v_i.
\]
Let $S_i$ equal $\max(s,s+\delta_i(v_i+\chi_i))$ on $B_i$ and $s$ elsewhere. The boundary collar makes this a global $\theta$-plurisubharmonic function. Since $\chi_i\leq0$ may be arranged,
\[
 s\leq S_i\leq s+2\delta_i\leq\varphi+2\delta_i.
\]
For every positive integer $m$, set
\[
 q_{i,m}=\max(\varphi-m,S_i)-2\delta_i.
\]
These potentials have the same ordinary type as $\varphi$, and
\begin{equation}\label{eq:relative-carrier-bounds}
 \varphi-m-2\delta_i\leq q_{i,m}\leq\varphi.
\end{equation}

On a neighborhood of $K_i$, $S_i=s+\delta_i v_i$ away from the pole set of $s$. Let
\[
 D_{i,m}=\{s+\delta_i v_i>\varphi-m\}
\]
in that neighborhood, restricting to points where the potentials are finite. This is a plurifinely open set there. Locality and positive mixed products give
\begin{equation}\label{eq:relative-carrier-local-domination}
 \mathbf1_{D_{i,m}}\mathrm{MA}^{\mathrm{ext}}_\theta(q_{i,m})
 \geq\delta_i^n\mathbf1_{D_{i,m}}\nu_i.
\end{equation}
Here no boundedness of $s$ is being assumed. After a local smooth correction, the positive product inequality holds at every common finite truncation level of $s$ and the bounded potential $v_i$. Exhaust the complement of the pole set of $s$. The measure $\nu_i$ is non-pluripolar, so it loses no mass in that exhaustion. Then restrict the resulting inequality by plurifine locality. This proves \eqref{eq:relative-carrier-local-domination} for the extended measures.

For $\mu_i$-almost every point of $K_i$, both $s$ and $\varphi$ are finite, and hence that point belongs to $D_{i,m}$ for some $m$. Consequently, a Borel set which is null for every $\mathrm{MA}^{\mathrm{ext}}_\theta(q_{i,m})$ is null for every $\mu_i$, and therefore for $\mu$.

Enumerate the countable family $q_{i,m}$ as $q_k$, and write its bounds as
$\varphi-C_k\leq q_k\leq\varphi$ with $C_k<\infty$. Choose positive $t_k$ such that
\[
 \sum_k t_k<1,\qquad B:=\sum_k t_kC_k<\infty.
\]
The finite convex combinations
\[
 \psi_N=\sum_{k=1}^N t_kq_k
               +\left(1-\sum_{k=1}^N t_k\right)\varphi
\]
decrease and lie between $\varphi-B$ and $\varphi$. Their genuine limit $\psi$ is $\theta$-plurisubharmonic and satisfies $\psi\simeq\varphi$. For any fixed $k$, separate its summand to write
\[
 \psi=t_kq_k+(1-t_k)w_k,
 \qquad w_k\in\PSH(X,\theta),\qquad w_k\simeq\varphi.
\]
The remainder is obtained by the same decreasing convex-sum construction. Positive non-pluripolar mixed products give
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(\psi)
       \geq t_k^n\mathrm{MA}^{\mathrm{ext}}_\theta(q_k).
\]
This is valid also for infinite measures: first restrict away from the common pole set, which is the pole set of $\varphi$ by the ordinary-type bounds, and then exhaust by finite truncations. All measures ignore that pole set. The preceding null-set conclusion now gives
$\mu\ll\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)$.

The latter extended measure is $\sigma$-finite. Indeed, its restriction to each set $\{\psi>-j\}$ is the restriction of a bounded truncation product, hence has finite mass on compact $X$; the pole set has measure zero. The Radon--Nikodym theorem applies to this $\sigma$-finite measure and the finite $\mu$. It gives a nonnegative density $f$ with
\[
 \int_X f\,\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)=\mu(X)<\infty,
\]
as claimed. If $\mu=0$, one may simply take $\psi=\varphi$ and $f=0$.
\end{proof}

This proposition concerns representation of measures, not solution of an equation. Even though $\psi-\varphi$ is bounded, $\psi$ itself need not be bounded. Thus the bounded subsolution theorem cannot be applied to it as stated. Moreover, truncating $f$ does not ensure that $\min(f,j)\mathrm{MA}^{\mathrm{ext}}_\theta(\psi)$ has the same ordinary-type solution as $\psi$. A proof of general prescribed-singularity existence must supply that existence step or an appropriate compactness construction. The representation isolates it without assuming bounded mass.


Follow AGENTS.md. All book source paths under /Users/mingchen/Non-Kahler/book/author. Persist full sequential/reference/failed checks, full readable verification_report.md and final results/relative_measure_carrier_01/verification.json via MCP. Never edit book/prior results. Correct iff no critical errors/gaps under explicit prerequisites.
