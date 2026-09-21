Run_id: big_unrestricted_addition_01

Statement: Verify the unrestricted weighted addition theorem and its associative/commutative operation corollary in the staged section below. ANY two u,v in E_phi, without ordinary-type or bounded-carrier assumptions. Background theta is smooth big and may be nonclosed/nonsemipositive; BMP and positive lower model-reference volume are explicit. The undamped weighted measure can have infinite mass. Conditional only on the exact general-measure positive-exponent existence theorem being audited separately. Check the weighted first moment, genuine decreasing relative-class limit, the EXTRA roof q=P_theta(a,u,v) before the order a<=u,v is known, the signed cutoff product limit, removing cutoffs for a possibly infinite measure, then the finite-measure domination and algebraic identities.

Exact legitimate internal premises in /Users/mingchen/Non-Kahler/book/author, already reconstructed and independently audited:
1. section_big_relative_foundations.tex and chapter_envelopes.tex: E_phi, under BMP and positive lower model-relative volume ell, has masses in [ell,M], is invariant under constants, and P_theta[w]=phi for its members, with w-sup w<=phi. SAME-CLASS finite rooftops are genuine and remain in E_phi, including three inputs. Strict domination for u in E_phi, v preceq phi and 1_{u<v}MAu<=c1_{u<v}MAv with c<1 gives u>=v. Exponential order and uniqueness follow by constant shifts using finite raw measures. Background/potential scaling multiplies MA by lambda^n.
2. section_big_relative_energy.tex prop:big-relative-first-moment: for a FIXED w in E_phi, u_j in E_phi with common upper bound u_j<=phi+C and uniform integral(w-u_j)_+ MAu_j, the suprema are bounded below; any genuine smooth L1 limit belongs to E_phi. The reference cannot vary with j. Normalized qpsh compactness and Hartogs lemma are standard.
3. Monotone theta-psh sequences with one fixed genuine lower bound converge in capacity. For constant truncations choose Hermitian Omega>=theta: max(a_j,-T) is bounded Omega-psh, and its theta product must be expanded into bounded positive Omega products with smooth signed factors. At a fixed truncation level these variations are uniformly controlled by capacity, and bounded capacity convergence applies against bounded fixed QC weights. Locality on strict untruncated sets and all NPP measures ignoring every pluripolar set are available. No raw weak MA convergence from capacity alone is a premise.
4. CONDITIONAL premise: thm:big-model-exponential in /Users/mingchen/Non-Kahler/research/editorial/section_big_model_measures.tex, being audited in big_model_measures_01. Every nonzero finite NPP datum tau admits a unique a in E_phi with MAa=e^a tau under exactly these hypotheses. Only FINITE data existence may be assumed. No weighted infinite-data theorem or ordinary-type Lp result is a premise.

Source attribution XL26 Theorem6.3, https://arxiv.org/html/2601.13446v1; archived /Users/mingchen/Non-Kahler/research/sources/P26.txt. Its conclusion may not be imported. The submitted proof replaces the source's intermediate comparison argument by the extra SAME-CLASS roof q and identifies the equation first. Follow normal sequential Rethlas workflow. Do not edit submitted TeX or manuscript. Persist every finding and final JSON, then stop.

Proof:

\section{Arbitrary weighted sums}
\label{sec:big-unrestricted-addition}

Once general-measure existence has been proved, the extra hypothesis on one input in \cref{thm:big-weighted-addition} can be removed. We retain the same smooth big background, bounded mass and positive lower model-reference volume. The earlier restricted addition theorem was used to establish existence; the result below is a consequence of that completed construction.

\begin{theorem}\label{thm:big-unrestricted-addition}
For every $u,v\in\mathcal E_\varphi$ and $\lambda>0$, there is a unique $a\in\mathcal E_\varphi$ satisfying
\[
 \mu_a=e^{\lambda(a-u)}\mu_u+e^{\lambda(a-v)}\mu_v.
\]
Moreover $a\leq\min(u,v)$ and $\mu_a\leq\mu_u+\mu_v$. No ordinary-type or bounded-carrier hypothesis on either input is imposed.
\end{theorem}
\begin{proof}
It suffices to take $\lambda=1$, by the scaling already used in \cref{thm:big-weighted-addition}. Let
\[
 \tau_j=e^{-\max(u,-j)}\mu_u+e^{-\max(v,-j)}\mu_v.
\]
These are nonzero finite non-pluripolar measures, and they increase with $j$. Only the weights are truncated; their truncations are not asserted to be $\theta$-plurisubharmonic. Theorem~\ref{thm:big-model-exponential} gives $a_j\in\mathcal E_\varphi$ with $\mu_{a_j}=e^{a_j}\tau_j$. Exponential order implies that $a_j$ decreases.

Set $r=P_\theta(u,v)\in\mathcal E_\varphi$. On $\{a_j<r\}$, one has $r\leq u,v$ and
\[
 (r-a_j)e^{a_j-\max(u,-j)}\leq(r-a_j)e^{a_j-r}\leq e^{-1},
\]
with the same inequality for $v$. Consequently
\[
 \int_X(r-a_j)_+\,\mu_{a_j}
 \leq e^{-1}\bigl(\mu_u(X)+\mu_v(X)\bigr).
\]
Also $a_j\leq a_1\leq\varphi+\sup_Xa_1$. The one-sided first-moment criterion, with fixed reference $r$, bounds $\sup_Xa_j$ below. Thus the decreasing sequence has a genuine $L^1$ limit $a$, and the same criterion puts $a$ in $\mathcal E_\varphi$.

We identify the equation before comparing $a$ with the inputs. The same-class rooftop
\[
 q=P_\theta(a,u,v)\in\mathcal E_\varphi
\]
lies below $a_j,a,u,v$. Let $\chi_T$ be a continuous nondecreasing cutoff of $q$, zero for $q\leq-2T$, one for $q\geq-T$, and increasing to one as $T\to\infty$ off the pole set. On $\{\chi_T>0\}$ both inputs exceed $-2T$. Hence, for $j>2T$,
\begin{equation}\label{eq:unrestricted-addition-cutoff}
 \chi_T\mu_{a_j}
 =\chi_T e^{a_j}(e^{-u}\mu_u+e^{-v}\mu_v).
\end{equation}
The factors $\chi_Te^{-u}$ and $\chi_Te^{-v}$ are bounded by $e^{2T}$. Since $a_j\downarrow a$ and $a_j\leq\sup_Xa_1$, dominated convergence against the fixed measure $\mu_u+\mu_v$ gives total-variation convergence of the right sides to the corresponding expression with $a$.

For the left side, $a_j\to a$ in capacity by monotone convergence with the genuine lower bound $a$. Choose a Hermitian $\Omega\geq\theta$ and replace $a_j$ by $b_j=\max(a_j,-2T)$ before forming bounded products. The functions $b_j$ are uniformly bounded $\Omega$-plurisubharmonic functions and converge in capacity. The expansion
\[
 (\theta+\ddc b_j)^n
 =\sum_{k=0}^n\binom nk(\Omega+\ddc b_j)^k
                         \wedge(\theta-\Omega)^{n-k}
\]
and bounded capacity continuity apply against the fixed quasi-continuous weight $\chi_T$. On its nonzero set no potential is truncated, so locality gives convergence to $\chi_T\mu_a$. This treats the possibly signed bounded product before inserting the cutoff.

Thus \eqref{eq:unrestricted-addition-cutoff} holds in the limit. Let $T\to\infty$. Both sides ignore the poles of $q$, so monotone convergence gives
\[
 \mu_a=e^{a-u}\mu_u+e^{a-v}\mu_v.
\]
This also proves finiteness of the weighted right side, since $a\in\mathcal E_\varphi$. Finiteness of $e^{-u}\mu_u+e^{-v}\mu_v$ has not been assumed.

For $\varepsilon>0$, the equation implies
\[
 \mathbf1_{\{u<a-\varepsilon\}}\mu_u
 \leq e^{-\varepsilon}\mathbf1_{\{u<a-\varepsilon\}}\mu_a.
\]
Strict domination gives $u\geq a-\varepsilon$, and then $u\geq a$. The same argument gives $v\geq a$, so $\mu_a\leq\mu_u+\mu_v$. For two solutions $a,b$, their finite Monge--Amp\`ere measures satisfy $\mu_a=e^{a-b}\mu_b$ off poles. Strict domination with constant shifts proves uniqueness. This reconstructs \cite[Theorem 6.3]{XL26}; the additional rooftop $q$ permits the cutoff argument before the comparison with $u,v$.
\end{proof}

\begin{corollary}\label{cor:weighted-addition-algebra}
For fixed $\lambda>0$, write $u\star_\lambda v$ for the solution in the theorem. This operation on $\mathcal E_\varphi$ is commutative and associative, and for $c\in\mathbb R$,
\[
 (u+c)\star_\lambda(v+c)=(u\star_\lambda v)+c,
 \qquad
 u\star_\lambda u=u-\lambda^{-1}\log2.
\]
\end{corollary}
\begin{proof}
Assign zero measure on poles and put $F_\lambda(u)=e^{-\lambda u}\mu_u$. The theorem says
$F_\lambda(u\star_\lambda v)=F_\lambda(u)+F_\lambda(v)$.
Equality of two such weighted measures implies equality of their potentials by strict domination of the finite raw measures. Commutativity and associativity therefore follow from addition of positive measures, including measures of infinite total mass. Finally,
$F_\lambda(u+c)=e^{-\lambda c}F_\lambda(u)$ gives both displayed identities and uniqueness identifies the potentials.
\end{proof}
