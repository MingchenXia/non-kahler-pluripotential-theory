Run_id: gauduchon_growth_01

Statement: On an arbitrary compact connected Hermitian n-manifold, check the improved range bound integral_X(omega+ddc v)^n <= C(1+A)^{max(n-2,0)} for bounded omega-psh 0<=v<=A, without bounded mass. Then check all new exponents in the consequences: exponential mass bound C(1+p^-1)^r, shallow mass C(1+t)^r, polynomial damping q>r, tail Cq/(q-r)(1+T)^{r-q}, capacity exponent (q-r)/(q+n-r), continuity with the improved range. Here r=max(n-2,0). No novelty or optimality claim.

Standard inputs: local bounded Bedford--Taylor multilinearity, positivity, Stokes/integration by parts with closed factors, local decreasing continuity and quasi-continuity, fixed smooth correction p=v+q psh, signed products of bounded quasi-psh functions defined by local expansion; canonical multiplication with bounded quasi-continuous potentials in this calculus and local recursion are allowed but the global exact-wedge cancellation must be checked. The uniform Gauduchon trace bound integral_X(omega+ddc v) wedge omega^(n-1)<=C is an input; for n=1 Stokes gives the same bound. Constants comparing smooth positive forms on a fixed finite cover are uniform. The preliminary CLN recursion for a nested cutoff is integral chi (ddc p)^j kappa^(n-j) = integral p ddc chi (ddc p)^(j-1) kappa^(n-j) <= C(A+C) integral_suppchi (ddc p)^(j-1) kappa^(n-j+1). Rethlas damped_measures_01 checked the preceding coarse n-power estimate, bounded exponential transform MA(F_{p/n}(u))>=exp(pu) MA_ext(u), exact capacity bound max(1,n/p)^n Cap_omega, and the cutoff proof of damped continuity, conditional on standard local BT inputs. Treat those as supplied inputs in this supplemental run; audit the stronger range proof and every substituted exponent independently.

Proof of the new range estimate:

\begin{proposition}[The Gauduchon improvement]\label{prop:gauduchon-range-growth}
Put $r_n=\max(n-2,0)$. For every Hermitian metric $\omega$ there is a constant $C_\omega$ such that
\[
 \int_X(\omega+\ddc v)^n\leq C_\omega(1+A)^{r_n}
 \quad\text{if }v\in\PSH(X,\omega),\ 0\leq v\leq A.
\]
\end{proposition}
\begin{proof}
We retain the fixed coordinate balls, $q$, $p=v+q$, and $\kappa$ from the preceding proof. The first local Hessian integral has a bound independent of $A$. Indeed,
\[
 \ddc p=(\omega+\ddc v)+(\ddc q-\omega),
\]
and the integral of the first positive term against $\kappa^{n-1}$ on any one coordinate ball is bounded by a fixed multiple of
\[
 \int_X(\omega+\ddc v)\wedge\omega^{n-1}.
\]
This is uniformly bounded by \cref{cor:trace-bounds}; the smooth second term has fixed mass. For $n=1$ the same assertion follows directly from Stokes' theorem.

Consequently the cutoff recursion can stop at degree one, rather than degree zero. For $j\geq1$ it gives, on a fixed smaller ball,
\[
 \int(\ddc p)^j\wedge\kappa^{n-j}\leq C_j(1+A)^{j-1}.
\]
Expand the positive mixed measures in these local corrected Hessians and sum over the finite cover. With
\[
 M_j(v)=\int_X(\omega+\ddc v)^j\wedge\omega^{n-j},
 \qquad 0\leq j\leq n,
\]
we obtain
\[
 0\leq M_j(v)\leq C_j(1+A)^{\max(j-1,0)}.
\]

There is one more global cancellation. For a bounded quasi-plurisubharmonic function, the signed products $(\ddc v)^j$ are globally defined by the same local Bedford--Taylor expansion. They are closed and satisfy
\[
 (\ddc v)^j=\ddc\bigl(v(\ddc v)^{j-1}\bigr).
\]
These identities follow locally from the bounded Bedford--Taylor recursion after a smooth correction, and hence agree on overlaps. Stokes' theorem therefore gives
\[
 0=\int_X(\ddc v)^n
   =\sum_{j=0}^n(-1)^{n-j}\binom nj M_j(v).
\]
Since all $M_j(v)$ are nonnegative,
\[
 M_n(v)\leq\sum_{j=0}^{n-1}\binom nj M_j(v)
          \leq C_\omega(1+A)^{\max(n-2,0)}.
\]
This proves the proposition, including dimension one.
\end{proof}

The two ingredients are the Gauduchon bound for one positive factor and the cancellation of the globally exact top wedge. Both also appear in the mixed-volume analysis of \cite[Proposition 3.3]{GL22}. The proposition records their quantitative consequence for a bounded range. We do not claim that the exponent $r_n$ is optimal for every metric. In dimensions one and two it is zero, recovering bounded mass in those dimensions.


Consequences to check, using the bounded exponential transform as input:

\begin{theorem}[Uniform exponential damping]\label{thm:exponential-damping}
For every $p>0$, the measure
\[
 \nu_{p,u}:=e^{pu}\mu_u
\]
is finite, non-pluripolar, and satisfies
\[
 \nu_{p,u}(X)\leq C_\omega(1+p^{-1})^{r_n}
 \quad\text{for all }u\in\PSH(X,\omega),\ u\leq0.
\]
The constant can be chosen independently of $p$ and $u$ after enlarging it by a dimensional factor.
\end{theorem}
\begin{proof}
Take $a=p/n$ in \cref{prop:exponential-transform} and apply \cref{prop:gauduchon-range-growth} with $A=n/p$. The measure vanishes on pluripolar sets because $\mu_u$ does.
\end{proof}

Thus every potential has a family of finite damped measures, even when $\mu_u(X)=+\infty$. The original measure can be recovered on the complement of the pole set by multiplication by $e^{-pu}$, with infinite mass allowed. Changing the additive normalization multiplies $\nu_{p,u}$ by the corresponding scalar $e^{pc}$; this dependence is explicit.

\section{Capacity control}

For a Borel set $E\subset X$, put
\[
 \operatorname{Cap}_\omega(E)
 =\sup_{v\in\PSH(X,\omega),\ 0\leq v\leq1}
             \int_E(\omega+\ddc v)^n.
\]
Its total value is finite by \cref{lem:bounded-range-mass}. We use the standard local Bedford--Taylor capacity facts: quasi-plurisubharmonic functions are quasi-continuous, Borel sets have capacity zero precisely when they are pluripolar, and uniformly bounded potentials converging in capacity have weakly convergent bounded products. Their versions in a fixed Hermitian background use local comparison of capacities, the smooth correction in \cref{prop:bounded-products}, and a finite coordinate cover. The analogous statement with uniformly bounded quasi-continuous coefficients converging in capacity is used below as well.

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
 \mu_u(\{u\geq-t\})\leq C(1+t)^{r_n}
 \quad(t\geq0, u\in\PSH(X,\omega),\ u\leq0).
\]
\end{lemma}
\begin{proof}
For any $p>0$, the left-hand side is at most $e^{pt}\nu_{p,u}(X)$. Apply \cref{thm:exponential-damping} with $p=(1+t)^{-1}$ and absorb the fixed dimensional constants.
\end{proof}

\begin{theorem}[Uniform polynomial damping]\label{thm:polynomial-damping}
For every $q>r_n=\max(n-2,0)$, the measures
\[
 \sigma_{q,u}:=(1-u)^{-q}\mu_u
\]
have uniformly bounded mass for $u\in\PSH(X,\omega)$, $u\leq0$. More precisely,
\[
 \sigma_{q,u}(\{u<-T\})
 \leq C\frac{q}{q-r_n}(1+T)^{r_n-q}\quad(T\geq0).
\]
There is also $C_q$ such that
\[
 \sigma_{q,u}(E)\leq C_q\operatorname{Cap}_\omega(E)^{(q-r_n)/(q+n-r_n)}
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
 &\leq C\frac{q}{q-r_n}(1+T)^{r_n-q}.
 \end{split}
\]
The possible mass on $\{s=0\}$ is bounded by \cref{lem:sublevel-mass-growth}, so the total bound follows also from this tail estimate.

For the capacity estimate write $\delta=\operatorname{Cap}_\omega(E)$. If $\delta=0$, apply \cref{prop:damped-capacity} on each finite sublevel of $s$ and exhaust the complement of the pole set. Thus $\sigma_{q,u}(E)=0$. If $0<\delta\leq1$, choose $T=\delta^{-1/(q+n-r_n)}\geq1$. On $\{s\leq T\}$, take $p=(1+T)^{-1}$ and use \cref{prop:damped-capacity} to obtain
\[
 \sigma_{q,u}(E\cap\{s\leq T\})
 \leq\mu_u(E\cap\{s\leq T\})
 \leq C(1+T)^n\delta.
\]
The remaining part is bounded by the preceding tail estimate. Since $T^n\delta=T^{r_n-q}=\delta^{(q-r_n)/(q+n-r_n)}$, both terms have the claimed bound. For $\delta>1$, use the uniform total-mass bound.
\end{proof}

For $n\geq2$, the capacity exponent is $1-n/(q+2)$, and the sufficient damping condition is $q>n-2$. Without the Gauduchon improvement, the initial local estimate would give only $q>n$ and capacity exponent $1-n/q$. Thus the conserved linear mass has a concrete effect on the treatment of arbitrarily singular potentials. Further improvements under special torsion conditions remain possible.

\section{Continuity of the damped operators}

\begin{theorem}\label{thm:damped-continuity}
Let $u_j,u\in\PSH(X,\omega)$ be nonpositive, and suppose $u_j\to u$ in capacity. Then, for every $p>0$ and every $q>r_n$,
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

