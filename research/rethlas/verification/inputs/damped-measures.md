Run_id: damped_measures_01

Statement: On an arbitrary compact connected complex manifold with a smooth Hermitian form omega, WITHOUT assuming bounded mass, verify the following deductions from standard bounded local Bedford--Taylor inputs: for every nonpositive omega-psh u, its extended non-pluripolar MA measure mu_u has uniformly finite damped measures e^{pu}mu_u (p>0) and (1-u)^{-q}mu_u (q>n), with the stated range, capacity and tail estimates; both damped operators are weakly continuous under capacity convergence of nonpositive potentials. Prove/verify only what is claimed; no novelty claim or global mass-finiteness premise is allowed.

Conventions and standard inputs (hypotheses of this conditional verification):
1. ddc=i/(2pi) partial bar-partial. Omega-psh means canonical quasi-psh u with omega+ddc u>=0. Maxima preserve omega-psh. Local smooth corrections by fixed quadratic q produce psh functions. Bounded local Bedford--Taylor products are positive for positive factors, multilinear, plurifinely local, closed when the factors are closed, and vanish on pluripolar sets. They agree with smooth wedges. Integration by parts against compactly supported smooth test functions and local decreasing regularization are valid. Non-closed bounded products are defined by expanding the smooth remainder from a local psh correction; this expansion is intrinsic and positive when the current factors are positive.
2. The standard bounded BT chain rule is assumed: ddc F(v)=F'(v)ddc v+F''(v)dv wedge dc v. For convex F the last term, and its mixed products with positive bounded BT factors, are nonnegative. The weighted products and positivity inequalities obtained by this chain rule pass through bounded local approximation. This input is only for bounded v. Its use for unbounded u must be justified by the proof's truncations.
3. Define u_t=max(u,-t), D_t={u>-t}. The positive finite measures 1_Dt MA_omega(u_t) increase by locality. Their limit mu_u is a countably additive positive Borel measure, possibly infinite, with zero mass on pluripolar sets. On D_t it agrees with the bounded truncation measure. It is sigma-finite because these D_t exhaust the complement of its measure-zero pole set, and each restriction has finite mass. Thus Tonelli is available with this measure. No Radon assertion is made before a finiteness bound.
4. For Cap_omega(E)=sup_{0<=v<=1, v omega-psh} integral_E MA(v), the standard local capacity calculus is assumed: qpsh quasi-continuity and capacity-zero pole sets; bounded potentials converging in capacity have weakly convergent bounded products. The same holds with uniformly bounded quasi-continuous coefficients converging in capacity. Local smooth corrections transfer this bounded statement to omega. The claimed total finiteness of Cap_omega is not an input: the proof establishes it by the bounded-range cutoff estimate.

The book excerpts below use internal labels. Their only inputs from other chapters are exactly the four standard inputs just stated. The local cutoff estimate, exponential transform, all exponents, constants, capacity scaling, layer-cake and cutoff limits are to be checked here. No theorem from a recent Hermitian paper is an input.

Proof:

\chapter{Finite measures without bounded mass}
\label{chap:damped-measures}

The extended Monge--Amp\`ere measure is available on every compact Hermitian manifold, but its total mass can be infinite. We now construct finite measures from it without imposing a bounded mass hypothesis. The construction retains the original measure away from the poles and has a useful continuity property. Its ingredients are bounded local Bedford--Taylor theory and elementary estimates.

Throughout this chapter $\omega$ is an arbitrary Hermitian metric on compact $X$, and potentials are normalized by $u\leq0$. We abbreviate
\[
 \mu_u=\mathrm{MA}^{\mathrm{ext}}_\omega(u).
\]
Every assertion in this chapter holds without bounded mass. The same arguments apply to a fixed semipositive smooth background in place of $\omega$, with a Hermitian metric used to measure capacity.

\section{A local estimate for a bounded range}

\begin{lemma}\label{lem:bounded-range-mass}
There is $C_\omega<+\infty$ such that every $v\in\PSH(X,\omega)$ with $0\leq v\leq A$ satisfies
\[
 \int_X(\omega+\ddc v)^n\leq C_\omega(1+A)^n.
\]
\end{lemma}
\begin{proof}
Choose finitely many coordinate balls with smaller relatively compact balls covering $X$. On each larger ball choose a fixed quadratic function $q$ with $\ddc q\geq\omega$. Then $p=v+q$ is plurisubharmonic, and, after a constant shift of $q$, satisfies $0\leq p\leq A+C$ there. Let $\kappa$ be the Euclidean K\"ahler form.

We recall the cutoff proof of the local estimate. For a cutoff $\chi$ equal to one on a smaller ball, compactly supported in a larger one, and with $|\ddc\chi|\leq C\kappa$, integration by parts gives
\[
 \begin{split}
 \int\chi(\ddc p)^j\wedge\kappa^{n-j}
 &=\int p\,\ddc\chi\wedge(\ddc p)^{j-1}\wedge\kappa^{n-j}\\
 &\leq C(A+C)\int_{\operatorname{supp}\chi}
                  (\ddc p)^{j-1}\wedge\kappa^{n-j+1}.
 \end{split}
\]
Use a nested sequence of cutoffs and repeat $j$ times. This proves a bound $C_j(1+A)^j$ on the smaller ball. The integrations by parts for bounded plurisubharmonic functions follow by local decreasing regularization, or directly from the Bedford--Taylor definition.

Finally expand
\[
 (\omega+\ddc v)^n
 =\sum_{j=0}^n\binom nj(\ddc p)^j\wedge(\omega-\ddc q)^{n-j}.
\]
Each smooth factor has uniformly bounded coefficients on the ball, so its absolute contribution is bounded by a fixed multiple of the corresponding local integral above. Sum over $j$ and the finite cover. This is the usual local Chern--Levine--Nirenberg cutoff estimate, with its dependence on the range retained.
\end{proof}

The constant in this lemma is independent of $v$, but the right-hand side depends on $A$. The bounded mass property would remove this dependence as the range grows. Nothing in the cutoff argument does that.

\section{A bounded convex transform}

For $a>0$ set
\[
 F_a(t)=a^{-1}e^{at}\quad(t\leq0).
\]
Then $0<F_a\leq a^{-1}$, $0<F_a'\leq1$, and $F_a''\geq0$. We set $F_a(-\infty)=0$.

We use the standard bounded Bedford--Taylor chain rule: for a bounded quasi-plurisubharmonic potential $v$ and a smooth convex increasing function $F$,
\[
 \ddc F(v)=F'(v)\ddc v+F''(v)\,dv\wedge\dc v.
\]
The last term and its products with positive bounded Bedford--Taylor factors are nonnegative. These identities are understood by local decreasing regularization; bounded potentials have the local Sobolev regularity needed for the gradient expression. This is a local fact from standard pluripotential theory, not a Hermitian mass theorem. Equivalently, the inequalities below can be obtained by smoothing on coordinate balls, allowing a lower-curvature error tending to zero, and passing to the bounded Bedford--Taylor limits.

\begin{proposition}\label{prop:exponential-transform}
If $u\in\PSH(X,\omega)$ and $u\leq0$, then $F_a(u)$ is a bounded $\omega$-plurisubharmonic function, and
\[
 e^{na u}\mu_u\leq\mathrm{MA}_\omega(F_a(u)).
\]
\end{proposition}
\begin{proof}
First suppose $u$ is bounded. The chain rule gives
\[
 \omega+\ddc F_a(u)
 =e^{au}(\omega+\ddc u)+(1-e^{au})\omega
      +ae^{au}\,du\wedge\dc u.
\]
All three summands are positive. Positivity of their bounded products yields the claimed measure inequality.

For arbitrary $u$, use $u_t=\max(u,-t)$. The bounded potentials $F_a(u_t)$ decrease and lie between zero and $a^{-1}$, so their limit $F_a(u)$ is a bounded $\omega$-plurisubharmonic function. On the plurifine open set $D_t=\{u>-t\}$, it agrees with $F_a(u_t)$. Locality and the bounded case therefore give
\[
 e^{na u}\mathbf1_{D_t}\mu_u
 \leq\mathbf1_{D_t}\mathrm{MA}_\omega(F_a(u)).
\]
Let $t\to+\infty$. The pole set is discarded by $\mu_u$ and has zero mass for the bounded product on the right.
\end{proof}

\begin{theorem}[Uniform exponential damping]\label{thm:exponential-damping}
For every $p>0$, the measure
\[
 \nu_{p,u}:=e^{pu}\mu_u
\]
is finite, non-pluripolar, and satisfies
\[
 \nu_{p,u}(X)\leq C_\omega(1+p^{-1})^n
 \quad\text{for all }u\in\PSH(X,\omega),\ u\leq0.
\]
The constant can be chosen independently of $p$ and $u$ after enlarging it by a dimensional factor.
\end{theorem}
\begin{proof}
Take $a=p/n$ in \cref{prop:exponential-transform} and apply \cref{lem:bounded-range-mass} with $A=n/p$. The measure vanishes on pluripolar sets because $\mu_u$ does.
\end{proof}

Thus every potential has a family of finite damped measures, even when $\mu_u(X)=+\infty$. The original measure can be recovered on the complement of the pole set by multiplication by $e^{-pu}$, with infinite mass allowed. Changing the additive normalization multiplies $\nu_{p,u}$ by the corresponding scalar $e^{pc}$; this dependence is explicit.

\section{Capacity control}

For a Borel set $E\subset X$, put
\[
 \operatorname{Cap}_\omega(E)
 =\sup_{v\in\PSH(X,\omega),\ 0\leq v\leq1}
             \int_E(\omega+\ddc v)^n.
\]
Its total value is finite by \cref{lem:bounded-range-mass}. We use the standard local Bedford--Taylor capacity facts: quasi-plurisubharmonic functions are quasi-continuous, pluripolar sets have capacity zero, and uniformly bounded potentials converging in capacity have weakly convergent bounded products. Their versions in a fixed Hermitian background follow by the local smooth correction in \cref{prop:bounded-products} and a finite coordinate cover. The analogous statement with uniformly bounded quasi-continuous coefficients converging in capacity is used below as well.

\begin{proposition}\label{prop:damped-capacity}
For every Borel set $E$,
\[
 \nu_{p,u}(E)
 \leq\max(1,n/p)^n\operatorname{Cap}_\omega(E).
\]
\end{proposition}
\begin{proof}
Put $A=\max(1,n/p)$ and $v=F_{p/n}(u)$. Then $0\leq v/A\leq1$ and $v/A$ is $\omega$-plurisubharmonic. Moreover
\[
 A(\omega+\ddc(v/A))=(\omega+\ddc v)+(A-1)\omega
 \geq\omega+\ddc v.
\]
Hence $\mathrm{MA}_\omega(v)\leq A^n\mathrm{MA}_\omega(v/A)$. Combine this with \cref{prop:exponential-transform} and the definition of capacity.
\end{proof}

This estimate is uniform over all nonpositive potentials. It controls the concentration of the damped measures without requiring control of the undamped total mass.

\section{Polynomial damping}

\begin{lemma}\label{lem:sublevel-mass-growth}
There is a constant $C$ depending only on $\omega$ such that
\[
 \mu_u(\{u\geq-t\})\leq C(1+t)^n
 \quad(t\geq0, u\in\PSH(X,\omega),\ u\leq0).
\]
\end{lemma}
\begin{proof}
For any $p>0$, the left-hand side is at most $e^{pt}\nu_{p,u}(X)$. Apply \cref{thm:exponential-damping} with $p=(1+t)^{-1}$ and absorb the fixed dimensional constants.
\end{proof}

\begin{theorem}[Uniform polynomial damping]\label{thm:polynomial-damping}
For every $q>n$, the measures
\[
 \sigma_{q,u}:=(1-u)^{-q}\mu_u
\]
have uniformly bounded mass for $u\in\PSH(X,\omega)$, $u\leq0$. More precisely,
\[
 \sigma_{q,u}(\{u<-T\})
 \leq C\frac{q}{q-n}(1+T)^{n-q}\quad(T\geq0).
\]
There is also $C_q$ such that
\[
 \sigma_{q,u}(E)\leq C_q\operatorname{Cap}_\omega(E)^{1-n/q}
\]
for every Borel set $E$.
\end{theorem}
\begin{proof}
Write $s=-u\geq0$. The identity
\[
 (1+s)^{-q}=q\int_s^\infty(1+t)^{-q-1}\,dt
\]
and Tonelli's theorem, valid also for the extended measure $\mu_u$, give the total-mass bound from \cref{lem:sublevel-mass-growth}. Restricting to $\{s>T\}$ gives
\[
 \begin{split}
 \int_{\{s>T\}}(1+s)^{-q}\,d\mu_u
 &\leq q\int_T^\infty(1+t)^{-q-1}\mu_u(\{s\leq t\})\,dt\\
 &\leq C\frac{q}{q-n}(1+T)^{n-q}.
 \end{split}
\]
The possible mass on $\{s=0\}$ is bounded by \cref{lem:sublevel-mass-growth}, so the total bound follows also from this tail estimate.

For the capacity estimate write $\delta=\operatorname{Cap}_\omega(E)$. If $\delta=0$, apply \cref{prop:damped-capacity} on each finite sublevel of $s$ and exhaust the complement of the pole set. Thus $\sigma_{q,u}(E)=0$. If $0<\delta\leq1$, choose $T=\delta^{-1/q}\geq1$. On $\{s\leq T\}$, take $p=(1+T)^{-1}$ and use \cref{prop:damped-capacity} to obtain
\[
 \sigma_{q,u}(E\cap\{s\leq T\})
 \leq\mu_u(E\cap\{s\leq T\})
 \leq C(1+T)^n\delta.
\]
The remaining part is bounded by the preceding tail estimate. Both terms are at most a constant times $\delta^{1-n/q}$. For $\delta>1$, use the uniform total-mass bound.
\end{proof}

The condition $q>n$ is a sufficient exponent furnished by this proof. We do not assert its optimality. The estimate deliberately uses only bounded local products, so improvements arising from Gauduchon identities or special torsion conditions can be studied separately.

\section{Continuity of the damped operators}

\begin{theorem}\label{thm:damped-continuity}
Let $u_j,u\in\PSH(X,\omega)$ be nonpositive, and suppose $u_j\to u$ in capacity. Then, for every $p>0$ and every $q>n$,
\[
 e^{pu_j}\mu_{u_j}\rightharpoonup e^{pu}\mu_u,
 \qquad
 (1-u_j)^{-q}\mu_{u_j}\rightharpoonup(1-u)^{-q}\mu_u.
\]
The undamped measures are allowed to have infinite mass.
\end{theorem}
\begin{proof}
We give the truncation argument explicitly. For $T>1$, choose a continuous function $\chi_T:\R\to[0,1]$ which is zero on $(-\infty,-2T]$ and one on $[-T,+\infty)$. Let $w(t)$ be either $e^{pt}$ or $(1-t)^{-q}$ on $t\leq0$. Plurifine locality gives
\[
 \chi_T(u_j)w(u_j)\mu_{u_j}
 =g_T(\max(u_j,-2T))\,
       \mathrm{MA}_\omega(\max(u_j,-2T)),
\]
where $g_T(t)=\chi_T(t)w(t)$ on $[-2T,0]$ and $g_T(-2T)=0$.
The truncated potentials are uniformly bounded and converge in capacity to the corresponding truncation of $u$, since truncation is Lipschitz. Their coefficients $g_T$ also converge in capacity and are uniformly bounded. Standard bounded Bedford--Taylor continuity therefore gives weak convergence of these truncated weighted measures for each fixed $T$.

It remains to remove the cutoff uniformly in $j$. For exponential damping,
\[
 \int_{\{u_j<-T\}}e^{pu_j}\,d\mu_{u_j}
 \leq e^{-pT/2}\int_Xe^{pu_j/2}\,d\mu_{u_j}
 \leq C_p e^{-pT/2}
\]
by \cref{thm:exponential-damping}. For polynomial damping, use \cref{thm:polynomial-damping}. Both bounds tend to zero and apply also to $u$. Testing against a bounded continuous function, pass first $j\to\infty$ at fixed $T$ and then $T\to\infty$. This proves both assertions.
\end{proof}

The theorem gives a finite and continuous replacement for the unrestricted mass operator. It does not make the equation $\mu_u=\mu$ automatic: recovering the undamped right-hand side still requires tail control. It does, however, provide a setting in which sequences of infinite-mass potentials can be compared without first excluding them from the theory.


Instructions: Follow the Rethlas AGENTS and required verification skills. Check every deduction in order, especially mixed-product inequalities for the bounded transform; unbounded truncation locality; dependence on p and range; the capacity exponent 1-n/q; the sigma-finite layer-cake calculation; the fixed-T weighted bounded-product limit and uniform removal of T. Standard Inputs1-4 are hypotheses, not independently verified theorems in this run. Produce results/damped_measures_01/verification.json. Do not edit the manuscript or files outside this copied verification workspace.
