Run_id: big_relative_energy_01

Statement: Verify the complete staged proof below of a first-moment noncollapse/full-mass-limit criterion and the self-measure L1-to-capacity criterion in an arbitrary smooth BIG background theta (not assumed closed or semipositive). X is compact connected Hermitian with BMP; phi=P_theta[phi] has relative lower volume ell>0 and finite upper volume M. No separate global metric PVP is assumed. Main first-moment criterion: u_j,w in E_phi, u_j<=w, sup int(w-u_j)MA(u_j)<infinity implies sup_X u_j uniformly bounded below and any genuine L1 limit stays in E_phi; variant assumes u_j<=phi+C and only the one-sided positive-part integral. Next theorem: u_j,u in E_phi, u_j L1->u, int|u_j-u|MA(u_j)->0 implies capacity convergence and after extraction all tail rooftops lie in E_phi. Full general-measure existence is not claimed or available as a premise.

The manuscript source is /Users/mingchen/Non-Kahler/research/editorial/section_big_relative_energy.tex. Read all mathematical statements and deductions in textual order. The following exact prerequisites from the separate audit big_relative_foundations_01 may be assumed conditionally; do not re-audit that entire submission. Root will include this text only if BOTH reports pass. Prerequisite source: /Users/mingchen/Non-Kahler/research/editorial/section_big_relative_foundations.tex:
- E_phi = E_env = E_vol, ell<=MA(u)(X)<=M, and both singularity-type volumes of any u in E_phi equal those of phi. E_env is defined by u preceq phi AND existence of all convex competitors A_b, not equality of an individual mass. Volume definitions are inf/sup over bounded-difference ordinary type.
- All finite rooftops of members are genuine and remain E_phi. Q_b(u,w) also stays E_phi when u<=w are both in this class.
- Strict domination: u in E_phi, v theta-psh preceq phi and 1_{u<v}MA(u)<=c 1_{u<v}MA(v) with 0<=c<1 implies u>=v.
- Weighted lower semicontinuity for capacity convergent theta-psh potentials with a common upper bound and uniformly bounded nonnegative quasi-continuous capacity-convergent weights, for any smooth theta. Constant truncations are only Omega-psh for a larger Hermitian Omega; their theta-products are signed until cut off. Monotone capacity convergence requires a genuine fixed lower bound.

Already-established independent internal premises in /Users/mingchen/Non-Kahler/book/author/chapter_envelopes.tex: upper/lower volume monotonicity under ordered smooth backgrounds and singularity types (thm:volume-monotonicity); volume addition (prop:volume-addition) and scaling; E_phi bounded-change, convex and upward stability; P_theta[u]=phi for every member and u-sup u<=phi. General genuine envelope contact and ordered-contact inequalities, positive mixed products, normalized quasi-psh compactness/Hartogs lemma, canonical representatives and measures ignoring pluripolar sets are established. Original Li Section4 primary archive research/sources/P26.pdf and .txt supplies attribution only; our proof is to be checked directly, not accepted because it resembles a published proof.

Check the mass inequality for max(a,w'-t), especially the equality-set allocation. Check that optimization is a SUPREMUM over ordinary-type representatives w'<=w, even though the left endpoint ell is a lower volume; no conserved mass is available. Check conversion of collapse of Q_b(u,w) to uniform collapse of h_j by L1 compactness and convex inequalities, class membership using upper volumes, the unordered positive-part reduction, and bounded truncated weights in capacity passages. No source or manuscript modification is requested; use the normal verification workflow and persist final JSON plus all checks.

Proof:

\section{A relative first-moment estimate}
\label{sec:big-relative-first-moment}

We continue under the hypotheses of \cref{sec:big-relative-foundations}. The following estimate explains why control of energy relative to a fixed full-mass potential prevents loss of singularity type. The proof must use the upper volume of an ordinary singularity type, rather than replace all masses by one cohomological number.

\begin{proposition}\label{prop:big-relative-first-moment}
Fix $w\in\mathcal E_\varphi$. Suppose $u_j\in\mathcal E_\varphi$, $u_j\leq w$, and
\[
 K:=\sup_j\int_X(w-u_j)\,\mu_{u_j}<+\infty.
\]
Then $\sup_Xu_j$ is bounded below. If $u_j\to u\in\PSH(X,\theta)$ in $L^1(X)$, then $u\in\mathcal E_\varphi$.

The same conclusions hold if $u_j\leq w$ is replaced by a common upper bound $u_j\leq\varphi+C$ and the integral is replaced by $\int_X(w-u_j)_+\,\mu_{u_j}$.
\end{proposition}
\begin{proof}
We first treat $u_j\leq w$. Choose any $w'\simeq w$ with $w'\leq w$, and let $p_j=P_\theta(u_j,w')$. These envelopes belong to $\mathcal E_\varphi$. Contact support and ordered contact imply
\begin{equation}\label{eq:big-energy-roof-bound}
 \int_X(w'-p_j)\,\mu_{p_j}
 \leq\int_X(w-u_j)\,\mu_{u_j}\leq K.
\end{equation}
Indeed, the integrand vanishes on the contact part $\{p_j=w'\}$, and on the remaining contact part $p_j=u_j<w'\leq w$.

We will use a consequence of the maximum principle. If $a\in\mathcal E_\varphi$, $a\leq w'$, and $t>0$, then
\begin{equation}\label{eq:big-energy-max-bound}
 \mu_a(\{a>w'-t\})
 \leq \mu_{w'}(\{a>w'-t\})+M-\mu_{w'}(X).
\end{equation}
To see this, put $m=\max(a,w'-t)$. Its ordinary singularity type is that of $w'$, so $\mu_m(X)\leq M$. On $\{a>w'-t\}$ locality gives $\mu_m=\mu_a$. On the complementary set, ordered contact with $w'-t\leq m$ gives $\mu_m\geq\mu_{w'}$. Integration proves the formula, including the equality set in the latter part.

If a subsequence had $\sup_Xu_j\to-\infty$, then also $\sup_Xp_j\to-\infty$. Splitting the mass of $p_j$ at $w'-s$ and using \eqref{eq:big-energy-roof-bound} and \eqref{eq:big-energy-max-bound}, we obtain
\[
 \ell\leq\mu_{p_j}(X)
 \leq\frac Ks+\mu_{w'}(\{p_j>w'-s\})+M-\mu_{w'}(X).
\]
For fixed $s$, the middle term tends to zero, since $w'$ is finite off a pluripolar set and $\mu_{w'}$ is finite and non-pluripolar. Let $j\to\infty$ and then $s\to\infty$. This gives $\ell\leq M-\mu_{w'}(X)$ for every $w'\simeq w$ lying below $w$. Constant translations do not change mass, so the supremum of these masses is $\overline{\operatorname{vol}}_\theta(w)=M$. This contradicts $\ell>0$ and proves the first assertion.

Now suppose $u_j\to u$ in $L^1$. Then $u\leq w\preceq\varphi$. Fix $b>1$ and suppose that $Q_b(u,w)$ is not genuine. Replacing $w$ by any boundedly equivalent $w'$ cannot change nonemptiness of its convex competitor family: a constant translation of a competitor compensates for the bounded change. Keep $p_j=P_\theta(u_j,w')$ and set
\[
 h_j=Q_b(p_j,w')\in\mathcal E_\varphi.
\]
We claim that $\sup_Xh_j\to-\infty$. Otherwise, since $h_j\leq p_j\leq w'$, quasi-plurisubharmonic compactness would give a subsequence with a genuine $L^1$ limit $h$. Passing to the limit in
\[
 b^{-1}h_j+(1-b^{-1})w'\leq p_j\leq u_j
\]
first almost everywhere and then by canonical representatives gives a competitor for $Q_b(u,w')$, a contradiction.

On the contact set of $h_j$ one has
$p_j=b^{-1}h_j+(1-b^{-1})w'$. Thus $h_j\leq w'-bs$ implies $p_j\leq w'-s$ there. Contact and \eqref{eq:big-energy-roof-bound} imply
\[
 \mu_{h_j}(\{h_j\leq w'-bs\})\leq b^nK/s.
\]
Apply \eqref{eq:big-energy-max-bound} with $a=h_j$ and $t=bs$ to the complementary set. We obtain
\[
 \ell\leq b^nK/s+
     \mu_{w'}(\{h_j>w'-bs\})+M-\mu_{w'}(X).
\]
The same successive limits and optimization over $w'\simeq w$ give a contradiction. Therefore $Q_b(u,w)$ is genuine for every $b>1$. The resulting convex inequalities and \cref{thm:volume-monotonicity,prop:volume-addition} give
\[
 (1-b^{-1})^n M\leq\overline{\operatorname{vol}}_\theta(u)\leq M.
\]
Let $b\to\infty$. The upper volumes are equal, hence $u\in\mathcal E_\varphi$.

For the last assertion put $q_j=P_\theta(u_j,w)$. Contact gives
\[
 \int_X(w-q_j)\,\mu_{q_j}
 \leq\int_X(w-u_j)_+\,\mu_{u_j}\leq K.
\]
The ordered case bounds $\sup_Xq_j$ from below and therefore also $\sup_Xu_j$. If $u_j\to u$ in $L^1$, extract a genuine $L^1$ limit $q$ of the $q_j$, using $q_j\leq w$. The ordered case gives $q\in\mathcal E_\varphi$. Since $q\leq u\leq\varphi+C$, upward stability gives $u\in\mathcal E_\varphi$ as well.
\end{proof}

In particular the estimate need not make $u_j-w$ bounded. It controls the negative part only through its integral against the moving measure $\mu_{u_j}$. This is the mechanism in \cite[Proposition 4.2]{XL26}, now with the optimization over equivalent reference potentials written explicitly.

\begin{theorem}\label{thm:big-relative-self-measure-convergence}
Let $u_j,u\in\mathcal E_\varphi$, with $u_j\to u$ in $L^1(X)$. If
\[
 \int_X|u_j-u|\,\mu_{u_j}\longrightarrow0,
\]
then $u_j\to u$ in capacity. After extraction, $P_\theta(\inf_{k\geq j}u_k)$ belongs to $\mathcal E_\varphi$ for every $j$.
\end{theorem}
\begin{proof}
Start with any subsequence and extract again so that the displayed integrals are at most $2^{-j}$ and $u_j\to u$ almost everywhere for smooth volume. The model envelope identity and Hartogs' lemma give $u_j,u\leq\varphi+C$ uniformly. For $N\geq j$ let $p_{j,N}=P_\theta(u_j,\ldots,u_N)$. Disjoint first-contact pieces give
\begin{equation}\label{eq:big-self-measure-roofs}
 \int_X|p_{j,N}-u|\,\mu_{p_{j,N}}\leq2^{1-j}.
\end{equation}
Apply the first-moment proposition with reference $u$ and its one-sided version. It bounds $\sup_Xp_{j,N}$ from below independently of $N$. Consequently the decreasing sequence has a genuine limit
\[
 p_j=P_\theta\left(\inf_{k\geq j}u_k\right),
\]
and the same proposition puts $p_j$ in $\mathcal E_\varphi$. Its increasing canonical limit $p$ belongs to that class by upward stability, since $p_1\leq p\leq u\preceq\varphi$. The inequality $p\leq u$ follows from the almost-everywhere convergence of the extracted sequence.

Both $p_{j,N}\downarrow p_j$ and $p_j\uparrow p$ converge in capacity with the genuine lower bound $p_1$. Apply \cref{lem:big-weighted-lsc} to \eqref{eq:big-self-measure-roofs}, using the bounded weights $\min(1,|p_{j,N}-u|)$ and then $\min(1,|p_j-u|)$. Their capacity convergence follows by first discarding deep sublevels of $p_1$ and $u$ and then using the Lipschitz function $\min(1,|x-y|)$ on finite values. The result is
\[
 \int_X\min(1,|p-u|)\,\mu_p=0.
\]
Zero domination gives $p=u$. The upper tail envelopes $(\sup_{k\geq j}u_k)^*$ decrease to $u$. Squeezing the extracted $u_j$ between these envelopes and $p_j$ proves capacity convergence. Applying this to every initial subsequence proves the conclusion for the original sequence.
\end{proof}

The conclusion stated here is convergence in capacity. To apply the undamped continuity theorem, one must also verify its tail condition; the example in \cref{ex:p1-raw-tail} shows why capacity convergence alone does not suffice. In the fixed-dominator situation that verification used the common lower envelope and the finite dominating measure.
