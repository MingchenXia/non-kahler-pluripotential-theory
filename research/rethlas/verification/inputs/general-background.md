Run_id: general_background_01

Statement: Verify the self-contained extension of positive extended MA measures to arbitrary smooth real backgrounds, their domination by a larger Hermitian background, intrinsicness, general-background damping/continuity, the raw tail/integrability criteria, and sequential closedness of exponential equations. No bounded-mass property, PVP, bigness, or semipositivity of theta is allowed as an unstated premise. All currents initially have canonical qpsh potentials. Extended positive measures may have infinite mass, are sigma-finite, and must not be treated as global Radon currents before proving finiteness.

Standard hypotheses supplied for this conditional check:
1. Bounded local Bedford--Taylor calculus, including smooth corrections, signed multilinear products, locality on plurifine open Borel sets where bounded potentials agree, mixed positivity for positive factors, local total variation of the coefficients, and the maximum principle for psh functions. Compact Hermitian capacity has countable subadditivity, capacity-zero Borel sets are precisely pluripolar, and qpsh functions are quasi-continuous. Uniformly bounded corrected psh potentials and bounded quasi-continuous coefficients converging in capacity have weakly convergent bounded products. The latter assertion transfers to signed smooth-remainder expansions term by term.
2. For a positive Hermitian background Omega, nonpositive potentials have positive extended measures from compatible constant truncations. Known finite damping and continuity estimates, checked separately: exponential transform and exponential tails, polynomial damping for any specified valid exponent, and weak convergence of the damped measures under capacity convergence. The current stronger numerical exponent r=max(n-2,0) is being separately audited; for the logical implications here one may instead use the already checked weaker exponent r=n. No step in this input is a proof of arbitrary-theta positivity or raw undamped continuity.
3. Every smooth theta has theta<=C omega with C>=1. Distributional Hessian lower bounds, local constant-form freezing, and qpsh local corrections are standard. If two smooth-plus-ddc decompositions give the same current, their potential difference is smooth by elliptic regularity of its scalar Laplacian.
4. Standard finite-measure results: monotone convergence, sigma-finite Tonelli, continuity from above, convergence in measure plus uniform boundedness gives L1 convergence against a finite measure, and total-variation/weak limits agree.

Audit all deductions below sequentially, in particular positivity on D_t despite globally signed truncation products, the epsilon-dependent coordinate neighborhoods and total-variation limit after restriction, intrinsicness under a smooth gauge, fixed-truncation identities with a coefficient vanishing exactly on the cut level, establishing finiteness of the raw limit before removing its tail, and the arbitrary finite NPP reference measure in the PDE passage. Historical BGL citations are attribution only, not premises. Do not turn an assumed capacity convergence into a theorem from L1 convergence. No novelty claim. Ignore editorial cross-reference numbers; named dependencies are included or explicitly stipulated.

Proof:



The construction can be made without semipositivity of $\theta$. The point is to prove positivity only after restricting to the sets where truncation leaves the potential unchanged.

Choose a Hermitian form $\Omega$ with $\theta\leq\Omega$. Every $u\in\PSH(X,\theta)$ belongs to $\PSH(X,\Omega)$. Thus $u_t=\max(u,-t)$ is a bounded quasi-plurisubharmonic function, and the signed product $(\theta+\ddc u_t)^n$ is defined by \cref{prop:bounded-products}. It need not be positive on all of $X$.

\begin{lemma}[Positivity on a truncation set]\label{lem:restricted-positive-product}
With $D_t=\{u>-t\}$, one has
\[
 0\leq\mathbf1_{D_t}(\theta+\ddc u_t)^n
 \leq\mathbf1_{D_t}(\Omega+\ddc u_t)^n.
\]
The same local positivity assertion holds for mixed products, on a common set where all the truncations leave their potentials unchanged.
\end{lemma}
\begin{proof}
Work in a coordinate ball with a fixed positive constant form $\kappa$, and fix $\epsilon>0$. Around any point choose a smaller neighborhood and a constant real form $\theta'$ such that
\[
 -\epsilon\kappa\leq\theta-\theta'\leq\epsilon\kappa.
\]
Take a smooth local potential $r$ for $\theta'+\epsilon\kappa$. Then $u+r$ is plurisubharmonic. On a relatively compact smaller neighborhood choose $k>t+\sup|r|$ and set
\[
 h_k=\max(u+r,-k)-r.
\]
It is locally bounded and equals $u_t=u$ on $D_t$. Moreover,
\[
 \theta+\ddc h_k+2\epsilon\kappa
 =\ddc\max(u+r,-k)+(\theta-\theta'+\epsilon\kappa)
\]
is a sum of a positive closed bounded-potential current and a smooth positive form. Its bounded products are positive. Plurifine locality transfers this positivity to the restriction of $(\theta+\ddc u_t+2\epsilon\kappa)^n$ to $D_t$.

These neighborhoods cover the coordinate ball. Let $\epsilon\downarrow0$. The product with the fixed bounded potential $u_t$ is polynomial in $\epsilon$, with coefficients of locally finite variation. Consequently convergence holds in local total variation, also after restriction to $D_t$. This proves the first inequality. Apply the same construction to each factor to obtain mixed positivity.

For the second inequality, expand the difference of the two powers by the telescoping identity, using the smooth positive difference $\Omega-\theta$. Every summand is a mixed product of positive factors on $D_t$, as just proved. The difference is therefore nonnegative there.
\end{proof}

\Needspace{13\baselineskip}
\begin{theorem}\label{thm:arbitrary-extended-ma}
Let $\theta$ be any smooth real $(1,1)$-form and let $u\in\PSH(X,\theta)$. Formula \eqref{eq:extended-ma}, with signed bounded products before restriction, defines a positive non-pluripolar Borel measure. It is independent of additive normalization, is allowed infinite mass, and satisfies
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)
 \leq\mathrm{MA}^{\mathrm{ext}}_\Omega(u)
 \quad\text{whenever }\Omega\text{ is Hermitian and }\theta\leq\Omega.
\]
It is finite on every $D_t$ and is sigma-finite. The construction is intrinsic to the positive current $\theta+\ddc u$.
\end{theorem}
\begin{proof}
The preceding lemma gives positivity and the comparison for every truncation level. Locality gives compatibility of the restrictions as in \cref{prop:extended-measure}. Their increasing limit is therefore a positive measure, and comparison passes to this limit. Each restricted measure has finite mass because it is dominated by a bounded $\Omega$-product. The sets $D_t$ exhaust the complement of the discarded pole set, proving sigma-finiteness.

For intrinsicness, consider another smooth decomposition $\theta'=\theta+\ddc f$, $u'=u-f$. On each set where both potentials are bounded below, sufficiently deep truncations agree with their untruncated potentials. The two bounded-potential currents then agree on that set, and plurifine locality gives equality of the restricted products. Such sets exhaust the complement of the common pole set, since $f$ is smooth and bounded. This proves the assertion; changes of additive normalization are a special case. Any two smooth decompositions of the same current differ in this way by the elliptic-regularity argument in \cref{prop:bounded-products}.
\end{proof}

For finite mass, this is the usual non-pluripolar product. The restricted construction is the mechanism in \cite[Proposition 2.1]{BGL25}. Allowing an extended measure removes the need for a global variation bound at this stage. It does not remove the need for such a bound when a global current is required.




When finite undamped measures are needed, the extra hypothesis can be placed on the sequence under study, rather than on every potential on the manifold. The following criterion makes that distinction precise.

\begin{theorem}[Control of the deep sublevels]\label{thm:undamped-tail-continuity}
Let $u_j,u\in\PSH(X,\omega)$ be nonpositive and suppose $u_j\to u$ in capacity. Assume
\[
 \sup_j\mu_{u_j}(X)<+\infty,\qquad
 \lim_{T\to\infty}\sup_j\mu_{u_j}(\{u_j<-T\})=0.
\]
Then $\mu_u$ is finite and $\mu_{u_j}\rightharpoonup\mu_u$. No bounded mass property of $X$ is assumed.
\end{theorem}
\begin{proof}
Choose a continuous nonincreasing function $\eta:[0,+\infty)\to[0,1]$, equal to one on $[0,1]$ and zero on $[2,+\infty)$. Put $\eta_T(s)=\eta(s/T)$. The fixed-truncation argument in \cref{thm:damped-continuity}, now with coefficient $\eta_T(-u_j)$, gives
\[
 \eta_T(-u_j)\mu_{u_j}\rightharpoonup\eta_T(-u)\mu_u
 \quad\text{for every fixed }T>0.
\]
The integrals on the left are bounded by the assumed uniform total mass. Since $\eta_T(-u)$ increases to one off the pole set as $T\to\infty$, monotone convergence proves $\mu_u(X)<+\infty$.

For a continuous test function $f$, the error made by inserting $\eta_T(-u_j)$ is at most
$\|f\|_\infty\mu_{u_j}(\{u_j<-T\})$, uniformly small for large $T$. For the limit potential the corresponding error tends to zero because $\mu_u$ is finite and its pole set has zero mass. Pass first $j\to\infty$ with $T$ fixed, and then $T\to\infty$.
\end{proof}

One can express these sequence assumptions by a single integrability condition. Let $\chi:[0,+\infty)\to[1,+\infty)$ be continuous, increasing and unbounded. For a nonpositive potential define
\[
 J_{\chi,\omega}(u)=\int_X\chi(-u)\,d\mu_u,
\]
with the value $+\infty$ allowed. This is an integrability functional. We do not assert that it is a primitive of the Monge--Amp\`ere operator or that its finite locus has all the convexity properties of the closed finite-energy classes.

\begin{corollary}\label{cor:integrability-continuity}
If $u_j\to u$ in capacity and $\sup_jJ_{\chi,\omega}(u_j)\leq C$, then
\[
 J_{\chi,\omega}(u)\leq C,\qquad
 \mu_{u_j}\rightharpoonup\mu_u.
\]
\end{corollary}
\begin{proof}
Since $\chi\geq1$, the total masses are at most $C$, and
\[
 \mu_{u_j}(\{u_j<-T\})\leq C/\chi(T).
\]
Thus \cref{thm:undamped-tail-continuity} applies. For the integrability assertion, use its fixed-truncation argument with the bounded continuous coefficient
$\chi(-u_j)\eta_T(-u_j)$. Its integral converges at each fixed $T$ and is at most $C$. Let $T\to\infty$ by monotone convergence.
\end{proof}

\begin{proposition}\label{prop:tail-integrability-equivalence}
For a family of nonpositive potentials, the two uniform conditions in \cref{thm:undamped-tail-continuity} are equivalent to a uniform bound on $J_{\chi,\omega}$ for some continuous increasing unbounded $\chi\geq1$.
\end{proposition}
\begin{proof}
One implication was proved in the preceding corollary. For the other choose numbers $T_k\to+\infty$, with $T_{k+1}>T_k+1$, such that the mass of $\{-u_j>T_k\}$ is at most $2^{-k}$ for every member of the family. Let $r_k$ be a continuous nondecreasing function, zero on $[0,T_k]$ and one on $[T_k+1,+\infty)$. Define
\[
 \chi(s)=1+\sum_{k\geq1}r_k(s).
\]
The sum is locally finite, so $\chi$ is continuous, increasing and unbounded. Tonelli's theorem gives
\[
 J_{\chi,\omega}(u_j)
 \leq\mu_{u_j}(X)+\sum_{k\geq1}\mu_{u_j}(\{-u_j>T_k\})
 \leq\sup_j\mu_{u_j}(X)+1.
\]
\end{proof}

These results identify the estimate needed in a general existence proof: obtain compactness of the potentials in capacity and prevent undamped mass from accumulating at their increasingly deep sublevels. A geometric bounded mass property is one possible source of some estimates, but it is not part of the statements or proofs above.

\section{Extension to general backgrounds}

\begin{theorem}\label{thm:general-background-damping}
Let $\theta$ be any smooth real $(1,1)$-form. For nonpositive $u\in\PSH(X,\theta)$ put $\mu_{\theta,u}=\mathrm{MA}^{\mathrm{ext}}_\theta(u)$. The finite damping, capacity estimates and capacity-continuity statements of this chapter hold for these measures, with constants depending on $\theta$ and a fixed Hermitian metric. In particular, for $p>0$ and $q>r_n$,
\[
 \int_Xe^{pu}\,d\mu_{\theta,u}
 \leq C(1+p^{-1})^{r_n},\qquad
 \int_X(1-u)^{-q}\,d\mu_{\theta,u}\leq C_q.
\]
The undamped tail criterion and the integrability criterion also hold with $\mu_{\theta,u}$ in place of $\mu_u$.
\end{theorem}
\begin{proof}
Choose $C_0\geq1$ such that $\theta\leq\Omega:=C_0\omega$. Then $u\in\PSH(X,\Omega)$ and \cref{thm:arbitrary-extended-ma} gives
\[
 0\leq\mu_{\theta,u}\leq\mathrm{MA}^{\mathrm{ext}}_\Omega(u).
\]
All the mass, tail and capacity bounds follow from the already proved estimates for $\Omega$. To express them in the original capacity, note that
\[
 \operatorname{Cap}_\omega(E)
 \leq\operatorname{Cap}_\Omega(E)
 \leq C_0^n\operatorname{Cap}_\omega(E).
\]
The first inequality follows by inclusion of the test potentials and positivity of the added background. For the second, if $0\leq v\leq1$ is $\Omega$-plurisubharmonic, then $v/C_0$ is an admissible $\omega$-test potential and
$(\Omega+\ddc v)^n=C_0^n(\omega+\ddc(v/C_0))^n$.

For continuity, the same fixed-truncation identity as in \cref{thm:damped-continuity} applies. The truncated potentials are bounded and $\Omega$-plurisubharmonic. Their products with background $\theta$ may be signed before multiplication by the cutoff, but their local expansions in bounded plurisubharmonic Hessians and fixed smooth forms are continuous under capacity convergence. The coefficient vanishes on the truncation level, so the identity with the restricted positive measure is exact. Uniform tails, already obtained by domination, then remove the cutoff. The proof of the undamped criterion uses only this fixed-truncation continuity and its stated mass and tail assumptions. Its integrability corollaries are purely measure-theoretic and therefore transfer as well.
\end{proof}

No bigness, semipositivity, bounded mass, or positive lower volume is imposed on $\theta$ in this theorem. Nonemptiness of the potential space is expressed by the given potentials themselves. What is unavailable for a general background is positivity of every constant truncation before restriction; the proof never uses that assertion.



The estimates in \cref{chap:damped-measures} give a passage to the limit that requires neither bounded mass nor a positive lower volume. Its hypothesis is convergence in capacity. Establishing that convergence in an existence argument remains a separate task.

\begin{lemma}\label{lem:npp-uniform-capacity}
Let $\mu$ be a finite non-pluripolar Borel measure on $X$. Then
\[
 \lim_{\delta\downarrow0}\sup\{\mu(E):E\text{ Borel},\
                      \operatorname{Cap}_\omega(E)\leq\delta\}=0.
\]
Consequently, capacity convergence implies convergence in $\mu$-measure.
\end{lemma}
\begin{proof}
If the first assertion failed, there would be $\epsilon>0$ and Borel sets $E_j$ with capacity at most $2^{-j}$ and $\mu(E_j)\geq\epsilon$. Countable subadditivity of capacity gives
\[
 \operatorname{Cap}_\omega\left(\limsup_j E_j\right)=0.
\]
The limsup is therefore pluripolar and has zero $\mu$-measure. On the other hand, finiteness of $\mu$ and continuity from above applied to $\bigcup_{j\geq k}E_j$ show that the limsup has measure at least $\epsilon$, a contradiction. Apply the first assertion to the sets on which the difference of two converging potentials exceeds a fixed positive number to get the consequence.
\end{proof}

\Needspace{15\baselineskip}
\begin{theorem}[Sequential closedness for exponential equations]\label{thm:exponential-closedness}
Fix a Hermitian metric on $X$, let $\theta$ be any smooth real $(1,1)$-form, and let $\mu$ be a finite non-pluripolar measure. Suppose $f_j\geq0$, $f_j\to f$ in $L^1(\mu)$, and $\lambda_j>0$ with $\lambda_j\to\lambda>0$. Let $u_j,u\in\PSH(X,\theta)$ be nonpositive, suppose $u_j\to u$ in capacity, and assume
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u_j)
     =e^{\lambda_j u_j}f_j\,\mu.
\]
Then $\mathrm{MA}^{\mathrm{ext}}_\theta(u)$ is finite and
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)=e^{\lambda u}f\,\mu.
\]
The measures on the left converge weakly; the right-hand sides converge in total variation.
\end{theorem}
\begin{proof}
Discard finitely many indices so that $\lambda_j\geq\lambda/2$. Their masses are at most $\|f_j\|_{L^1(\mu)}$, hence uniformly bounded. On a deep sublevel,
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u_j)(\{u_j<-T\})
 \leq e^{-\lambda T/2}\|f_j\|_{L^1(\mu)}.
\]
The tail criterion \cref{thm:undamped-tail-continuity}, in its general-background form \cref{thm:general-background-damping}, shows that the limiting Monge--Amp\`ere measure is finite and that the left-hand sides converge weakly to it.

It remains to identify this weak limit. By \cref{lem:npp-uniform-capacity}, $u_j\to u$ in $\mu$-measure. The functions $e^{\lambda u_j}$ are bounded by one and converge in $\mu$-measure to $e^{\lambda u}$. The change of exponent is uniform for nonpositive arguments, because the mean-value theorem gives
\[
 \sup_{t\leq0}|e^{\lambda_jt}-e^{\lambda t}|
 \leq |\lambda_j-\lambda|
       \sup_{s\geq0}s e^{-(\lambda/2)s}\longrightarrow0.
\]
Thus $e^{\lambda_j u_j}\to e^{\lambda u}$ in $\mu$-measure and, by absolute continuity, in $f\mu$-measure as well. Boundedness by one and finiteness of $f\mu$ give convergence in $L^1(f\mu)$. Therefore
\[
 \begin{split}
 \int_X|e^{\lambda_j u_j}f_j-e^{\lambda u}f|\,d\mu
 &\leq\|f_j-f\|_{L^1(\mu)}\\
 &\quad+\int_X|e^{\lambda_j u_j}-e^{\lambda u}|f\,d\mu
 \longrightarrow0.
 \end{split}
\]
This proves total-variation convergence and identifies the equation for $u$.
\end{proof}

Normalizing constants can be absorbed into $f_j$ whenever the resulting densities converge in $L^1(\mu)$. The theorem does not assert that an arbitrary $L^1$-convergent sequence converges in capacity or stays in a prescribed envelope class.

This argument also pinpoints the difficulty as $\lambda_j\downarrow0$: the tail bound $e^{-\lambda_jT}\|f_j\|_1$ no longer tends to zero uniformly in $j$ as $T\to\infty$. A zero-exponent approximation needs another source of uniform tail control, such as the integrability condition in \cref{cor:integrability-continuity}. Global bounded mass would not by itself supply that missing tail estimate.

