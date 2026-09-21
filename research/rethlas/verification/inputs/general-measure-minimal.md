Run_id: general_measure_minimal_01

Statement: Strictly audit the complete proof of a bounded theta-psh carrier for ANY finite non-pluripolar measure on a compact connected manifold with smooth SEMIPOSITIVE BIG theta (no volume properties), and then reconstruction of positive-exponent and zero-exponent equations in the minimal global envelope class E0 assuming v_minus(theta)>0 but NO bounded mass property. Arbitrary prescribed singularity phi is explicitly outside this new reconstruction.

Accepted internal inputs, whose actual statements and uses must be checked:
- book/author/section_bounded_subsolution.tex thm:bounded-subsolution, fully proved and independently audited: for bounded psi theta-psh, bounded nonnegative nonzero f relative to MA_theta(psi), theta semipositive big, unique bounded solution MA_theta u=e^(lambda u) f MA_theta psi for lambda>0.
- book/author/chapter_relative_finite_measures.tex lower-mass theorem, finite-measure exponential order/scalar uniqueness; book/author/section_dominated_relative_compactness.tex thm:relative-fixed-measure-continuity: under PVP and admissible model phi, E_phi potentials with genuine L1 limit and MA bounded by one fixed finite NPP measure converge in capacity and weak MA, with limit in E_phi. These proofs were reconstructed earlier, not relying on general existence.
- book/author/section_relative_compactness.tex lem:fixed-npp-integrals for uniformly bounded qpsh with common curvature lower bound, L1 smoothvolume convergence implies L1 for a fixed finite NPP measure.
- Standard local BT mixed positivity, locality and monotone continuity, canonical qpsh representatives, compactness of normalized qpsh, convex composition, and strict analytic regularization of a big smooth nonclosed background (also explicit in section_big_continuous_contact.tex). These are standard accepted inputs. Do check every use.

NEW external input MUST verify in exact context: Cegrell, Pluricomplex energy (1998), Theorem6.3. Local archived primary PDF research/sources/Ceg98.pdf and txt; physical23 printed209, E0definition physical2 printed188. It says positive compactly supported measure on bounded hyperconvex domain decomposes tau=g(ddc v)^n+tau_s with v in LOCAL E0, bounded negative zero boundary finite mass; g L1, tau_s pluripolar. Standing n>=2. n=1 is separately proved using Green potential and bounded exponential. Primary URL https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6561-11511_2006_Article_BF02392899.pdf ; DOI10.1007/BF02392899. Source normalization can be absorbed in RN density. Do not conflate local energy E0 with global envelope E0.

The proof cites ALS26 Theorem5.8+Cor5.9 solely for historical attribution of the result being reconstructed, NEVER as an existence input. Verify the attribution against research/sources/ALS26.pdf if needed; treat reconstruction independently. No novelty claim.

Critically check local-to-global patching (strict barrier, collar max, truncation, theta nonclosed, arbitrary compact NPP measure); countable uniform convex sum and positive mixed domination; n1 Green chain inequality including polar limits; model0 hypotheses and lower mass; density monotonicity/order direction; genuine noncollapse, fixed-domination all assumptions, TV convergence; zeroexponent bounded comparison normalization sign and positive scalar, chain bounds on e^(v_j/j) across poles, fixed NPP integration. Record any gap instead of importing the target theorem.

Proof:

\section{General measures in the minimal envelope class}
\label{sec:general-measure-minimal}

The bounded subsolution theorem and dominated continuity already give the equation for every finite non-pluripolar measure in the minimal envelope class. The missing link is a bounded reference adapted to the measure and to the same background. Its density need only be integrable. We construct that reference from a standard local decomposition theorem, and then give the limiting argument. This reconstructs the minimal-reference case of \cite[Theorem 5.8 and Corollary 5.9]{ALS26}.

\begin{lemma}[A bounded reference for a measure]\label{lem:bounded-measure-carrier}
Let $\theta\geq0$ be smooth and big, and let $\mu$ be a finite non-pluripolar measure on $X$. There are a bounded $\psi\in\PSH(X,\theta)$ and a nonnegative
$f\in L^1(\mathrm{MA}_\theta(\psi))$ such that
\[
 \mu=f\,\mathrm{MA}_\theta(\psi).
\]
No upper or lower volume property is assumed.
\end{lemma}
\begin{proof}
We first specify the local input. Cegrell's decomposition theorem \cite[Theorem 6.3]{Ceg98} says that a positive compactly supported measure $\tau$ on a bounded hyperconvex domain in $\mathbb C^n$, $n\geq2$, is
\[
 \tau=g(\ddc v)^n+\tau_s,
 \qquad v\in\mathcal E_0,\qquad
 0\leq g\in L^1((\ddc v)^n),
\]
where $\tau_s$ is carried by a pluripolar set. Here the local class $\mathcal E_0$ consists of bounded negative plurisubharmonic functions with zero boundary values and finite total Monge--Amp\`ere mass. This local notation is different from the global envelope class $\mathcal E_0$ in this chapter. If $\tau$ is non-pluripolar, $\tau_s=0$, so $\tau\ll(\ddc v)^n$. A change in the normalization of $\ddc$ only changes $g$ by a positive constant.

For completeness the required local assertion on a disk also follows from the Green potential. Let $a\leq0$ be the Green potential of a finite compactly supported non-polar measure $\tau$, normalized by $\ddc a=\tau$. Then $v=e^a$ is bounded and subharmonic, and
\[
 \ddc v\geq e^a\tau.
\]
To justify the inequality, set $a_M=\max(a,-M)$. The bounded subharmonic chain rule gives
$\ddc e^{a_M}\geq e^{a_M}\ddc a_M$, which on $\{a>-M\}$ is at least $e^a\tau$. Let $M\to\infty$, using decreasing convergence of the bounded subharmonic functions $e^{a_M}$ and monotone convergence on the right. Since $\{a=-\infty\}$ is polar, $e^a>0$ almost everywhere for $\tau$. Thus $\tau\ll\ddc v$. The bounded chain inequality itself follows by local convolution and passage to the distributional limit. We use only this absolute continuity assertion in every dimension.

Choose a strict potential $\rho$ with analytic singularities, smooth off its analytic pole set $Z$, and
\[
 \theta+\ddc\rho\geq\kappa\omega,\qquad\kappa>0.
\]
Such a potential is available by strict regularization. Cover $X\setminus Z$ by countably many compact inner coordinate balls $K_i$, with larger coordinate balls $B_i\Subset X\setminus Z$. Apply the local assertion to $\mu_i=\mathbf1_{K_i}\mu$ on $B_i$. After a positive affine change of its bounded local potential, we obtain $v_i\in\PSH(B_i)$ with
\[
 1\leq v_i\leq2,\qquad
 \mu_i\ll(\ddc v_i)^n.
\]
Zero pieces may be omitted. Pick a smooth $\chi_i$ on $B_i$ which is zero near $K_i$ and $-3$ near $\partial B_i$. For a sufficiently small $\epsilon_i>0$,
\[
 \theta+\ddc\bigl(\rho+\epsilon_i(v_i+\chi_i)\bigr)
 \geq\tfrac\kappa2\omega+\epsilon_i\ddc v_i.
\]
Inside $B_i$ take the maximum of this potential with $\rho$, and extend it by $\rho$ outside $B_i$. The two pieces glue because $v_i+\chi_i\leq-1$ on a boundary collar. Finally take the maximum with $-C_i$, where $C_i$ is large enough that this last maximum does not change the function near $K_i$. Constants are $\theta$-plurisubharmonic since $\theta\geq0$. We have obtained a global bounded $q_i\in\PSH(X,\theta)$ which agrees with $\rho+\epsilon_i v_i$ near $K_i$. Positivity of bounded mixed products therefore gives
\[
 \mathrm{MA}_\theta(q_i)\geq\epsilon_i^n(\ddc v_i)^n
 \quad\hbox{near }K_i,
 \qquad \mu_i\ll\mathrm{MA}_\theta(q_i).
\]

Translate each $q_i$ so that $q_i\leq0$, and choose positive numbers $t_i$ with
\[
 \sum_i t_i<1,\qquad
 \sum_i t_i\|q_i\|_\infty<\infty.
\]
The uniformly convergent sum $\psi=\sum_i t_iq_i$ is bounded and $\theta$-plurisubharmonic. For a fixed index $i$ it is a convex combination
$\psi=t_iq_i+(1-t_i)w_i$ with a bounded $w_i\in\PSH(X,\theta)$: use the remaining terms and the unused weight on the constant zero potential. Hence
\[
 \mathrm{MA}_\theta(\psi)\geq t_i^n\mathrm{MA}_\theta(q_i).
\]
Every $\mu_i$ is absolutely continuous with respect to this single finite measure. The sets $K_i$ cover $X\setminus Z$, and $\mu(Z)=0$. Thus $\mu\ll\mathrm{MA}_\theta(\psi)$. The Radon--Nikodym theorem supplies the asserted integrable density. If $\mu=0$, simply take $\psi=0$ and $f=0$.
\end{proof}

\Needspace{15\baselineskip}
\begin{theorem}\label{thm:general-measure-minimal}
Let $\theta\geq0$ be smooth and big, and assume $v_-(\theta)>0$. Let $\mu$ be a finite non-pluripolar measure with $\mu(X)>0$.
For every $\lambda>0$ there is a unique $u\in\mathcal E_0$ satisfying
\[
 \mathrm{MA}_\theta^{\mathrm{ext}}(u)=e^{\lambda u}\mu.
\]
There also exist $v\in\mathcal E_0$, normalized by $\sup_Xv=0$, and a unique positive scalar $c$ such that
\[
 \mathrm{MA}_\theta^{\mathrm{ext}}(v)=c\mu.
\]
The second assertion does not claim uniqueness of the normalized potential. No bounded mass property is assumed.
\end{theorem}
\begin{proof}
The reference $0$ is model because $\theta\geq0$, and $P_{\epsilon\theta}(0)=0$ for every $\epsilon>0$. Every bounded $\theta$-plurisubharmonic function belongs to $\mathcal E_0$, since a sufficiently negative constant is a competitor for each of its stretched envelopes. The lower estimate of \cref{thm:relative-uniform-mass-lower}, with $\epsilon\downarrow0$, gives
\begin{equation}\label{eq:minimal-lower-mass}
 \mathrm{MA}^{\mathrm{ext}}_\theta(w)(X)\geq v_-(\theta)
 \qquad(w\in\mathcal E_0).
\end{equation}

\emph{Positive exponent.} Write $\mu=f\nu$ by the preceding lemma, with $\nu=\mathrm{MA}_\theta(\psi)$ and $\psi$ bounded. Let $f_j=\min(f,j)$ for positive integers $j$. These densities are bounded and nonzero as measures. The bounded subsolution theorem gives bounded $u_j$ with
\[
 \mathrm{MA}_\theta(u_j)=e^{\lambda u_j}f_j\nu.
\]
Exponential order shows that $u_j$ decreases, because $f_j$ increases. In particular $u_j\leq u_1$. On the other hand
\[
 v_-(\theta)\leq\mathrm{MA}_\theta(u_j)(X)
       \leq e^{\lambda\sup_Xu_j}\mu(X).
\]
Thus their suprema have a common lower bound. The decreasing limit $u$ is a genuine $\theta$-plurisubharmonic function, and convergence holds in $L^1(X)$. Moreover
\[
 \mathrm{MA}_\theta(u_j)\leq e^{\lambda\sup_Xu_1}\mu.
\]
The fixed-measure continuity theorem \cref{thm:relative-fixed-measure-continuity} applies with reference zero. It gives $u\in\mathcal E_0$ and weak convergence of the Monge--Amp\`ere measures to $\mathrm{MA}^{\mathrm{ext}}_\theta(u)$. The right sides converge in total variation to $e^{\lambda u}f\nu$: the functions $e^{\lambda u_j}f_j$ converge almost everywhere for $\nu$ and are bounded by $e^{\lambda\sup_Xu_1}f\in L^1(\nu)$. This proves the equation. Its measure is finite, so \cref{cor:relative-finite-exponential-order} gives uniqueness.

\emph{Zero exponent.} For each positive integer $j$, let $u_j\in\mathcal E_0$ be the just-constructed solution with exponent $1/j$. We first bound the normalization. Let $h$ be the bounded solution of
\[
 \mathrm{MA}_\theta(h)=e^h\min(f,1)\nu,
\]
supplied by the bounded subsolution theorem. Set $H=\|h\|_\infty$ and $w_j=h+(j-1)H$. Then $w_j/j\geq h$, and
\[
 e^{-w_j/j}\mathrm{MA}_\theta(w_j)
 \leq e^{-h}\mathrm{MA}_\theta(h)
 \leq\mu
 =e^{-u_j/j}\mathrm{MA}^{\mathrm{ext}}_\theta(u_j).
\]
Exponential order, now with exponent $1/j$, gives $u_j\leq w_j$. Put
\[
 M_j=\sup_Xu_j,\qquad v_j=u_j-M_j,
 \qquad c_j=e^{M_j/j}.
\]
Then $\sup_Xv_j=0$ and $0<c_j\leq e^H$. Equation \eqref{eq:minimal-lower-mass} also gives
\[
 v_-(\theta)\leq c_j\int_X e^{v_j/j}\,d\mu
                 \leq c_j\mu(X),
\]
so $c_j\geq v_-(\theta)/\mu(X)>0$. After extraction, compactness of normalized potentials gives $v_j\to v$ in $L^1(X)$, with $v$ genuine and normalized, and $c_j\to c>0$.

The normalized $L^1$ bound gives $v_j/j\to0$ in $L^1$ for smooth volume. The functions $a_j=e^{v_j/j}$ lie between zero and one and have a common lower curvature bound. Indeed, after choosing a Hermitian $\Omega\geq\theta$, the convex chain rule yields
\[
 \ddc a_j\geq-\frac1j a_j\theta\geq-\Omega.
\]
The inequality is valid across poles by bounded truncation; take $e^{-\infty}=0$. Also $|1-a_j|\leq|v_j|/j$ almost everywhere for smooth volume. Thus $a_j\to1$ in smooth-volume $L^1$. The fixed non-pluripolar integration lemma \cref{lem:fixed-npp-integrals} now gives $a_j\to1$ in $L^1(\mu)$. Consequently
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(v_j)=c_ja_j\mu
       \longrightarrow c\mu
 \quad\hbox{in total variation},\qquad
 \mathrm{MA}^{\mathrm{ext}}_\theta(v_j)\leq e^H\mu.
\]
Apply \cref{thm:relative-fixed-measure-continuity} again. It gives $v\in\mathcal E_0$ and identifies the limit as $\mathrm{MA}^{\mathrm{ext}}_\theta(v)$. The scalar assertion in \cref{cor:relative-finite-exponential-order}, applied in both directions to two solutions, proves uniqueness of $c$.
\end{proof}

The argument uses only bounded reference potentials in the same background, followed by domination by one fixed finite measure. Its first limit is decreasing. In the second limit, the vanishing exponent is controlled by integration against that fixed measure. These are the two compactness mechanisms needed here. A prescribed singular reference $\varphi$ requires further work: the bounded local patching above does not construct a carrier with that singularity, and the resulting solutions are in $\mathcal E_0$. The general prescribed-reference theorem remains a separate result.


Follow AGENTS.md strictly. Read source files from /Users/mingchen/Non-Kahler/book/author and /Users/mingchen/Non-Kahler/research/sources. Check each deduction in textual order, exact hypotheses and references, no hidden BMP or circular use of general existence. Persist full step/reference records and all failures. Write a full readable report and final results/general_measure_minimal_01/verification.json through MCP. Do not edit book, prior results or source papers. Correct iff zero critical errors and gaps.
