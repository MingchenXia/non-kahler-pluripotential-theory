Run_id: general_damping_weights_01

Statement: Verify the proposition and logarithmic critical-power example in research/editorial/section_general_damping_weights.tex using the normal Rethlas workflow. This is a candidate addition beyond checkpoint56; do not manually modify frozen sources, existing results or verifier memory. No novelty claim or external citation is made.

Context: X is a compact complex manifold of dimension n>=1, omega an arbitrary Hermitian metric, r_n=max(n-2,0). All potentials u are omega-psh and nonpositive. mu_u=MA_ext_omega(u) is the positive extended Borel measure, sigma-finite, zero on every pluripolar set, but its total mass may be infinite. Do not assume BMP, positive lower mass or a uniform bound for the undamped masses.

Accepted inputs, with their precise proved scopes to be read in book/author/chapter_damped_measures.tex and chapter_products.tex: prop:gauduchon-range-growth bounds the mass of a bounded potential of range [0,A] by C(1+A)^r_n; lem:sublevel-mass-growth bounds mu_u({u>=-t}) by C(1+t)^r_n; bounded products are positive and local on plurifine opens. The Hermitian capacity uses all omega-psh 0<=v<=1. Uniformly bounded omega-psh potentials converging in capacity have weakly convergent products, also with bounded quasicontinuous continuous-function coefficients converging in capacity. thm:damped-continuity supplies the fixed truncation argument using chi_T=0 on (-infinity,-2T], 1 on [-T,infinity), and its identity with the bounded max(u,-2T) product. The sublevel bound itself also follows directly from v_t=max(u,-t-1)+t+1, range [0,t+1], whose measure equals mu_u on {u>=-t}; this direct proof is proposed as an exposition simplification and should be checked.

Check the infinite-measure Tonelli argument, poles, atoms at s=0 and the strict tail {s>T}; all constants independent of u; the positivity rescaling in the capacity estimate at T=0 as well as T>0; the fixed-cutoff continuity argument and uniform tail removal; the logarithmic example including the derivative, integrability and stated tail bound; r_n=0. Check that the later arbitrary-smooth-background extension uses domination by a fixed larger Hermitian background for bounds and bounded signed-product truncations for continuity, and therefore applies to this proposition as well. This is a bounded audit of this short addition, accepting the named earlier inputs, not recertification of the entire book.

Proof:

The same truncation argument applies to a general decreasing weight. The sufficient condition below permits logarithmic damping at the critical power $r_n$.

\begin{proposition}\label{prop:general-damping-weights}
Let $w:[0,+\infty)\to(0,+\infty)$ be continuously differentiable and nonincreasing, with $w(t)\to0$. Put
\[
 B_w(T)=\int_T^\infty(1+t)^{r_n}(-w'(t))\,\mathrm{d}t,
 \qquad B_w(0)<+\infty.
\]
For nonpositive $u\in\PSH(X,\omega)$, the measures
$\nu_{w,u}=w(-u)\mu_u$, with weight zero on the pole set, satisfy
\[
 \nu_{w,u}(X)\leq C_\omega B_w(0),\qquad
 \nu_{w,u}(\{u<-T\})\leq C_\omega B_w(T).
\]
For every Borel set $E$ and $T\geq0$,
\[
 \nu_{w,u}(E)\leq
 w(0)(1+T)^n\operatorname{Cap}_\omega(E)+C_\omega B_w(T).
\]
In particular they are uniformly absolutely continuous with respect to capacity. If $u_j\to u$ in capacity, then $\nu_{w,u_j}\rightharpoonup\nu_{w,u}$.
\end{proposition}
\begin{proof}
Write $s=-u$. Since $w(s)=\int_s^\infty(-w'(t))\,\mathrm{d}t$, Tonelli's theorem and \cref{lem:sublevel-mass-growth} give
\[
 \int_X w(s)\,\mathrm{d}\mu_u
 =\int_0^\infty(-w'(t))\mu_u(\{s\leq t\})\,\mathrm{d}t
 \leq C_\omega B_w(0).
\]
This identity includes the set $\{s=0\}$; the pole set has zero $\mu_u$-mass. Restricting the integral to $\{s>T\}$ gives the same bound with $B_w(T)$, since the inner set is then $\{T<s\leq t\}$ and $t\geq T$.

On $\{s\leq T\}$ use $v_T=\max(u,-T-1)+T+1$. It has range $[0,T+1]$, and $v_T/(T+1)$ is an admissible capacity test. Positivity and locality imply
\[
 \mu_u(E\cap\{s\leq T\})
 \leq\int_E(\omega+\ddc v_T)^n
 \leq(1+T)^n\operatorname{Cap}_\omega(E).
\]
Multiply this by $w(0)$ and add the tail estimate. To obtain uniform absolute continuity, first choose $T$ so that $B_w(T)$ is small, then let the capacity of $E$ tend to zero.

For continuity, insert the fixed cutoff $\chi_T(u_j)$ used in \cref{thm:damped-continuity}. The coefficient $\chi_T(t)w(-t)$ is continuous on $[-2T,0]$ and vanishes at $-2T$, so the same bounded-product argument gives convergence at each fixed $T$. The errors are at most $C_\omega B_w(T)$ times the supremum norm of the test function, uniformly in $j$ and for $u$. Letting $T\to\infty$ proves weak convergence.
\end{proof}

For $n\geq3$ and $a>1$, take
\[
 w(t)=(1+t)^{-(n-2)}[\log(\mathrm{e}+t)]^{-a}.
\]
Indeed, writing $r=n-2>0$, differentiation gives
\[
 (1+t)^r(-w'(t))
 =\frac{r}{(1+t)[\log(\mathrm{e}+t)]^a}
  +\frac{a}{(\mathrm{e}+t)[\log(\mathrm{e}+t)]^{a+1}}.
\]
Both terms are integrable at infinity and
$B_w(T)\leq C_{n,a}[\log(\mathrm{e}+T)]^{1-a}$. Thus the measures
\[
 (1-u)^{-(n-2)}[\log(\mathrm{e}-u)]^{-a}\mu_u
\]
have uniformly bounded mass, the displayed logarithmic tail bound and capacity continuity. In dimensions one and two, $r_n=0$ and $B_w(T)=w(T)$, so every weight satisfying the stated monotonicity and vanishing conditions works. The condition is sufficient; no necessity or optimal endpoint is asserted.
