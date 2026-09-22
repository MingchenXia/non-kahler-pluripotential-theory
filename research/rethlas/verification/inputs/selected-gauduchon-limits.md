Run_id: selected_gauduchon_limits_01

Statement: Check the new selected-sequence proposition and the entropy consequences below through the normal Rethlas workflow. No novelty claim is made. This bounded verification concerns only these elementary additions after checkpoint64, not the entire manuscript.

Accepted inputs with exact scope: the normalized positive dd^c-closed (n-1,n-1) current family G_omega is compact in the weak topology of currents, agreeing on this bounded set with convergence against continuous coefficient forms (book/author/section_weak_gauduchon_duality.tex). Every such current has determinant measure k_T dV with uniformly bounded subcritical Lq norms, 1<q<n/(n-1) (section_gauduchon_determinant_integrability.tex). For every nonnegative p in Ln, sup over all normalized currents D_p(T)=rho_omega(p), and the same supremum is obtained on smooth positive normalized forms. For every bounded measurable nonnegative weight q, T->D_q(T) is weakly upper semicontinuous; this was proved by L^(2n) approximation and the uniform subcritical estimate (section_integrable_gauduchon_currents.tex). D_omega means p in Ln with rho_omega(p)<infinity, and D_omega^0 is the norm closure of bounded roots. Nonzero nonnegative p has rho>0. Do NOT assume D_p itself is upper semicontinuous without the extra tail hypothesis. Uniform exponential integrability gives alpha>0 and A<infinity with integral exp(-alpha v)dV<=A for all normalized omega-psh v; dV(X)=1. Standard weak compactness of finite measures, monotone convergence, and the nonnegative lower-semicontinuous integral inequality for weak measure convergence are accepted.

In the entropy paragraphs, T_j are smooth positive maximizing tests, d_j=D_p(T_j)->R, nu_j=d_j^-1 p k_Tj dV is a probability, a_j is its density, and integral a_j log a_j dV<=H. These paragraphs supply the first-moment condition of the existing moment theorem; they do not reprove its other hypotheses or infer a genuine smaller-background envelope. The last cluster-limit probability is R^-1 p k_T dV. Check tail estimates, the bounded measurable truncation step, both directions of the maximum argument, weak identification of weighted measures, normalizations, entropy negative part, integrability before using Jensen/Gibbs, and passage of moments to the limit. No smoothness, strong convergence, exact Monge-Ampere equation, whole-family limit or equality D_omega=D_omega^0 is claimed.

Proof:

To obtain a single maximizer, it suffices to control one maximizing sequence. The hypothesis controls only the chosen sequence, with no uniform bound over the entire current family.

\begin{proposition}\label{prop:selected-gauduchon-attainment}
Let $0\leq p\in\mathcal D_\omega$ be nonzero and put $R=\rho_\omega(p)$. Suppose $T_j\in\mathscr G_\omega$ converge weakly to $T$ and satisfy $D_p(T_j)\to R$. If the densities $p k_{T_j}$ are uniformly integrable, then
\[
 D_p(T)=R,\qquad
 p k_{T_j}\,\mathrm{d}V\rightharpoonup p k_T\,\mathrm{d}V.
\]
Consequently, a uniformly integrable maximizing sequence has a maximizing current among its weak cluster limits. No assumption $p\in\mathcal D_\omega^0$ is needed.
\end{proposition}
\begin{proof}
Put $p_K=\min(p,K)$. Since $p$ is finite almost everywhere, uniform integrability gives
\[
 \varepsilon_K:=\sup_j\int_{\{p>K\}}p k_{T_j}\,\mathrm{d}V
       \longrightarrow0.
\]
For every nonnegative continuous $h$, the weight $hp_K$ is bounded and measurable. The bounded-weight upper semicontinuity proved in \cref{thm:integrable-current-attainment} therefore gives
\[
 \limsup_j\int_Xhp k_{T_j}\,\mathrm{d}V
 \leq \int_Xhp_K k_T\,\mathrm{d}V
                   +\|h\|_\infty\varepsilon_K.
\]
Let $K\to\infty$. For $h=1$ this yields $R\leq D_p(T)$; the supremum formula \eqref{eq:integrable-current-supremum} gives the reverse inequality. If $\mu$ is a weak cluster limit of $p k_{T_j}\,\mathrm{d}V$, the same estimate for all nonnegative continuous $h$ gives $\mu\leq p k_T\,\mathrm{d}V$. Both measures have mass $R$, so they agree. Their bounded masses give weak compactness, and every cluster limit has now been identified. The final assertion follows from compactness of $\mathscr G_\omega$.
\end{proof}

This criterion gives convergence of determinant-weighted measures at the chosen maximum. It supplies neither smoothness of the current nor an exact Monge--Amp\`ere equation.

The moment condition is automatic if the densities of $\nu_j$ are uniformly bounded in $L^q(\mathrm{d}V)$ for some $q>1$, by H\"older and the uniform finite moments of normalized quasi-plurisubharmonic functions. More generally, a uniform entropy bound suffices. Write $a_j=\mathrm{d}\nu_j/\mathrm{d}V$ and suppose $\int_Xa_j\log a_j\,\mathrm{d}V\leq H$. Choose $\alpha>0$ and $A$ from \cref{lem:uniform-exponential}, so that $\int_X\mathrm{e}^{-\alpha v}\,\mathrm{d}V\leq A$ for every normalized $v$. The elementary entropy inequality, first for $v_T=\max(v,-T)$, gives
\[
 \alpha\int_X(-v_T)a_j\,\mathrm{d}V
 \leq \int_Xa_j\log a_j\,\mathrm{d}V
             +\log\int_X\mathrm{e}^{-\alpha v_T}\,\mathrm{d}V
 \leq H+\log A.
\]
For completeness, apply $t\log t-t+1\geq0$ to $t=a_j/q$, integrate against the probability density $q=\mathrm{e}^{-\alpha v_T}/\int_X\mathrm{e}^{-\alpha v_T}\,\mathrm{d}V$, and rearrange. Monotone convergence as $T\to\infty$ proves \eqref{eq:maximizing-gauduchon-moments} with $C=(H+\log A)/\alpha$.

The same entropy bound also gives dual attainment along this sequence. Indeed $t\log t\geq-\mathrm{e}^{-1}$ and, for $K>1$,
\[
 \int_{\{a_j>K\}}a_j\,\mathrm{d}V
       \leq\frac{H+\mathrm{e}^{-1}}{\log K}.
\]
This proves uniform integrability of $a_j$. Since $d_j\to R>0$, it also proves uniform integrability of $p k_{T_j}=d_ja_j$. By \cref{prop:selected-gauduchon-attainment}, every weak current cluster limit maximizes $D_p$, and along a convergent current subsequence the probabilities converge to $R^{-1}p k_T\,\mathrm{d}V$. For each normalized $v$, the function $-v$ is nonnegative and lower semicontinuous. The lower bound for integrals under weak convergence of measures therefore passes the moment bound to this limiting probability. No regularity of $T$ follows from these conclusions.
