Run_id: exponential_rooftop_barrier_01

Statement: Audit the complete new proposition and class-closure corollary below. Main theory has no BMP. Goal is common lower envelope for an entire sequence under MA(u_j)<=A exp(lambda u_j) MAomega(psi_j) with uniformly bounded psi_j. Either PVP and u_j Ephi, OR each u_j has ordinary type phi with NO PVP. No convergence of psi_j is used. The explicit barrier is q+(1-epsilon)rho+delta psi_j-C_b and theta_s>=delta omega_psij. Check every coefficient, singularity order, contact estimate, finiteness of MA(r_jb), both comparison alternatives, and conversion of uniform barriers for each b to full common h Ephi. This is NOT a claimed capacity-convergence theorem or general nonpluripolar equation theorem.

Accepted prerequisites already written and passed: relative_class_domination_01 (book chapter_relative_finite_measures.tex), singular_domination_01 (section_singular_domination.tex), semipositive contact support and ordered contact for extended measures (local_contacts_01 etc), local positive mixed-product calculus, big background means a genuine rho with theta_rho>=a omega. Convex competitor definition Q_b and upward stability of Ephi accepted. Relative Ephi elements satisfy P[u]=phi but may have infinite mass. Do not assume BMP, PVP in the ordinary-type alternative, finite mass of s_jb, analytic rho, convergence of reference potentials, or uniform ordinary-type constants. Read relevant passed reports and source files as needed. New standalone proof is the authoritative audit target; book read-only. Follow usual bounded verification workflow.

Proof:

\section{Common envelopes from exponential domination}

Exponential domination by bounded Bedford--Taylor measures gives a direct way to prevent a family of relative envelopes from collapsing. The comparison function is built from the smaller-background potential and a strict big potential. This avoids estimating a finite rooftop by the number of its obstacles.

\begin{proposition}\label{prop:exponential-common-rooftop}
Retain the standing semipositive big background and model reference, and let $\omega$ be a Hermitian metric. Suppose $u_j\in\mathcal E_\varphi$, $u_j\leq\varphi+C$, and
\begin{equation}\label{eq:exponential-bounded-reference-domination}
 \mu_{u_j}\leq A e^{\lambda u_j}\omega_{\psi_j}^n,
 \qquad \psi_j\in\PSH(X,\omega),\qquad
 \|\psi_j\|_\infty\leq L,
\end{equation}
where $A,\lambda>0$ and $C,L$ are fixed. Assume either $v_-(\theta)>0$ or $u_j\simeq\varphi$ for every $j$. Then
\[
 h=P_\theta\left(\inf_j u_j\right)\in\mathcal E_\varphi.
\]
No convergence of $\psi_j$ or $u_j$ is required. In the ordinary-type alternative, the constants in $u_j\simeq\varphi$ need not be uniform.
\end{proposition}
\begin{proof}
Translate all $u_j$ by one constant so that $u_j\leq\varphi\leq0$; this changes $A$ by a fixed factor. Translate each $\psi_j$ to lie in $[-2L,0]$, without changing its measure. Let
\[
 q=P_{\varepsilon\theta}(\varphi)\leq\varphi,
 \qquad \rho\leq0,\qquad \theta+\ddc\rho\geq a\omega
\]
for some $a>0$. The first potential is genuine by the model hypothesis, and the second by bigness. Fix $0<\delta<(1-\varepsilon)a$.

For a fixed real $b\geq1$, put $r_{j,b}=Q_b(u_j,\varphi)$. The stretching lemma puts it in $\mathcal E_\varphi$, and $r_{j,b}\leq u_j\leq0$. Contact support and positivity imply
\[
 \mu_{r_{j,b}}
 \leq b^n\mathbf1_{D_{j,b}}\mu_{u_j},
 \qquad
 D_{j,b}=\{b^{-1}r_{j,b}+(1-b^{-1})\varphi=u_j\}.
\]
On this contact set, $u_j\leq r_{j,b}/b$. Thus
\begin{equation}\label{eq:stretched-exponential-domination}
 e^{-\lambda r_{j,b}/b}\mu_{r_{j,b}}
 \leq b^n A\omega_{\psi_j}^n.
\end{equation}
In particular $\mu_{r_{j,b}}$ is finite: the right side has uniformly bounded mass by \cref{lem:bounded-mixed-capacity}, and $r_{j,b}\leq0$. Weighted inequalities are interpreted off the pluripolar sets.

Choose $C_b\geq0$ so large that
\[
 \delta^n\exp(\lambda C_b/b)\geq b^n A,
\]
and define
\[
 s_{j,b}=q+(1-\varepsilon)\rho+\delta\psi_j-C_b.
\]
This is a genuine $\theta$-plurisubharmonic function, since
\[
 \begin{split}
 \theta+\ddc s_{j,b}
 &= (\varepsilon\theta+\ddc q)
      +(1-\varepsilon)(\theta+\ddc\rho)
      +\delta\ddc\psi_j\\
 &\geq \delta\omega_{\psi_j}.
 \end{split}
\]
Consequently $\mu_{s_{j,b}}\geq\delta^n\omega_{\psi_j}^n$. This inequality follows first away from the poles by the local positive product inequality, and then globally because the bounded reference measure does not charge pluripolar sets. Also $s_{j,b}\leq-C_b$ and $s_{j,b}\preceq\varphi$. We conclude
\[
 e^{-\lambda s_{j,b}/b}\mu_{s_{j,b}}
 \geq b^n A\omega_{\psi_j}^n
 \geq e^{-\lambda r_{j,b}/b}\mu_{r_{j,b}}.
\]

If $v_-(\theta)>0$, apply \cref{cor:relative-finite-exponential-order} with first potential $r_{j,b}$ and second potential $s_{j,b}$. Its finiteness hypothesis was checked in \eqref{eq:stretched-exponential-domination}; no finiteness of $\mu_{s_{j,b}}$ is needed. It gives $r_{j,b}\geq s_{j,b}$.

In the ordinary-type alternative, $r_{j,b}\simeq\varphi$: if $u_j\geq\varphi-K_j$, the potential $\varphi-bK_j$ is a competitor for $r_{j,b}$. The smaller-background envelope of $r_{j,b}$ is therefore genuine, and $s_{j,b}\preceq r_{j,b}$. The same conclusion follows instead from \cref{cor:singular-exponential-order}, without a lower-volume hypothesis.

The bound $\psi_j\geq-2L$ now supplies one genuine lower bound, independent of $j$:
\[
 H_b=q+(1-\varepsilon)\rho-2\delta L-C_b
 \leq r_{j,b}.
\]
The potential $H_b$ is $\theta$-plurisubharmonic. Therefore
\[
 b^{-1}H_b+(1-b^{-1})\varphi\leq u_j
 \quad\hbox{for every }j.
\]
For $b=1$ this proves that the infimum envelope $h$ is genuine. For general $b$, the left side is a competitor for $h$, so it also lies below $h$. This is a competitor for every defining stretched-envelope condition of $h$. Since $h\leq\varphi$, we obtain $h\in\mathcal E_\varphi$. Restore the common translation to finish.
\end{proof}

\begin{corollary}\label{cor:exponential-relative-class-closure}
Under the hypotheses of \cref{prop:exponential-common-rooftop}, if $u_j\to u\in\PSH(X,\theta)$ in $L^1(X)$, then $u\in\mathcal E_\varphi$.
\end{corollary}
\begin{proof}
The common envelope gives $h\leq u_j\leq\varphi+C$. Pass to an almost-everywhere convergent subsequence and then to canonical representatives to get $h\leq u\leq\varphi+C$. Upward stability gives the conclusion.
\end{proof}

The proposition supplies the envelope noncollapse needed in the first alternative of \cite[Lemma 4.2]{ALS26}. It also gives this conclusion without a positive lower volume when the approximants have the reference's ordinary type. It does not by itself prove convergence in capacity or identify the limiting Monge--Amp\`ere measure. Those assertions require a separate argument; a common lower envelope in $\mathcal E_\varphi$ may itself have infinite mass.
