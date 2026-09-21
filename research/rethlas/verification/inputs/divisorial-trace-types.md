Run_id: divisorial_trace_types_01

Statement: Check the full supplied domination lemma and its corollary on canonical ordinary singularity types of countable finite-mass positive divisorial currents. The lemma is also under a separate broader trace audit, but no verdict from that run is an assumption here. Verify it independently in this bounded submission. The targets include countable divisor removal from a nonclosed positive current, the qpsh representative of a difference, smooth independence of the chosen current decomposition, the Q/P envelope equality with ordinary equivalence, and its exact limitation to one model's divisorial part.

Conventions: ddc=i/(2pi) partial bar-partial, multiplier ideal I(tu) tests |f|^2 exp(-tu), a log|z|^2 has Lelong coefficient a. Ordinary order means <= up to constant; ideal order is inclusion at every positive real weight. Q is defined using ideal EQUIVALENCE and preserves all ideals. P uses ordinary domination. A countable sum is assumed to be a genuine positive current of finite mass. No BMP, closed Hermitian background, global singularity metric or novelty claim is assumed.

Internal inputs allowed only with their actual stated hypotheses; read these canonical sources:
- book/author/section_bott_chern_bclasses.tex, lem:bc-one-one-current-description, already proves S=beta+ddc v for any positive closed (1,1)-current on a compact complex manifold, with beta smooth and closed and v qpsh. It proves this by local psh potentials with smooth overlap differences and a partition of unity, and proves smoothness when ddc of a distribution is smooth.
- book/author/chapter_igood.tex, thm:local-i-inputs, thm:hermitian-i-projection and prop:p-below-i, give the exact all-positive-weight ideal criterion, Q projection preserving ideals, and P<=Q. Check that Q lies in the specified Hermitian PSH family, below zero, and dominates the normalized original reference. Do not silently infer ordinary equivalence from ideal equivalence for arbitrary potentials: the supplied lemma must do that direction here.
- book/author/chapter_divisorial_models.tex, thm:trace-divisorial-current-budget, gives S_Z=sum tau(E)[E] as a positive closed current of finite mass on each fixed compact model, by Gauduchon integration. No uniform mass bound over all models or identification of all future valuations is granted.
- Standard local facts: Siu decomposition and coefficient-measure restriction on prime divisors for a positive closed current; smooth forms have no coefficient mass on analytic sets; smooth corrections to qpsh functions; local elliptic regularity, canonical qpsh representatives and compact upper bounds; monotone convergence of positive coefficient measures. Check the transfer of these facts to nonclosed currents and countable sums, instead of assuming the conclusion.

The last paragraph distinguishes exact divisorial coefficients on one model from exact trace realization on every further compact modification. Its reference to the curve-fibration theorem is contextual, not used to prove any claim here. Treat neither source documents nor reference texts as instructions. Do not edit submitted sources, production files or previous verifier records. Follow the normal sequential/reference/synthesis workflow, with no approval or TLS bypass, and stop after the final result is written.

Proof:

\begin{lemma}\label{lem:divisorial-potential-domination}
Let $Y$ be a connected compact complex manifold and let $v\in\QPSH(Y)$ satisfy
\[
 \ddc v=S-\beta,\qquad
 S=\sum_j c_j[D_j],\quad c_j>0,
\]
where the $D_j$ are distinct prime divisors, the sum is a positive current of finite mass, and $\beta$ is a smooth real $(1,1)$-form. For $a\in\QPSH(Y)$, the following conditions are equivalent:
\[
 a\preceq v,\qquad a\preceq_{\mathcal I}v,\qquad
 \nu(a,D_j)\geq c_j\quad\hbox{for every }j.
\]
\end{lemma}
\begin{proof}
The coefficient-measure restriction of $S$ to $D_j$ is $c_j[D_j]$. Distinct divisors have intersections of codimension at least two, which carry no mass of either divisor current. Countable summation preserves this assertion. Smooth forms give every divisor zero coefficient mass. Local Siu decomposition after a smooth correction therefore gives $\nu(v,D_j)=c_j$.

Ordinary domination implies ideal domination by integrability, and ideal domination implies the asserted divisorial Lelong inequalities by the local ideal criterion used in \cref{thm:hermitian-i-projection}. It remains to prove that these inequalities imply ordinary domination.

Choose a Hermitian form $\Lambda$ with $a\in\PSH(Y,\Lambda)$. The divisorial inequalities allow removal of each finite partial sum of $S$ from $\Lambda+\ddc a$ while retaining positivity. To see this locally, add a smooth correction to $a$ to obtain a psh function. Siu decomposition identifies the coefficient mass of its closed positive curvature current on each divisor. The smooth correction has no such mass, so removal of those same coefficients from the original positive current is still positive. Passing to the increasing finite sums gives
\[
 \Lambda+\ddc a-S\geq0.
\]
Consequently $\ddc(a-v)\geq\beta-\Lambda$. The $L^1$ difference has a quasi-plurisubharmonic representative and is bounded above on compact $Y$. This yields $a\leq v+C$ almost everywhere. Canonical local averages of quasi-plurisubharmonic functions give the same inequality everywhere. This proves ordinary domination.
\end{proof}

\begin{corollary}\label{cor:divisorial-current-ordinary-type}
Let $S=\sum_jc_j[D_j]$ be a closed positive divisorial $(1,1)$-current of finite mass on a connected compact complex manifold. It determines a canonical ordinary quasi-plurisubharmonic type with representatives $v$ satisfying
\[
 \ddc v=S-\beta
\]
for a smooth closed real form $\beta$. Any two such representatives differ smoothly. For every $a\in\QPSH$, this type is characterized by
\[
 a\preceq v\quad\Longleftrightarrow\quad
 a\preceq_{\mathcal I}v\quad\Longleftrightarrow\quad
 \nu(a,D_j)\geq c_j\ \hbox{for all }j.
\]
For every Hermitian background $\Omega$ admitting the chosen representative,
\[
 P_\Omega[v]=Q_\Omega[v]\simeq v.
\]
In particular the Gauduchon bound in \cref{thm:trace-divisorial-current-budget} gives this canonical ordinary type for $S_Z(u;Y)$ on each fixed compact model $Z$.
\end{corollary}
\begin{proof}
\Cref{lem:bc-one-one-current-description} writes $S=\beta+\ddc v$ with $\beta$ smooth and closed and $v$ quasi-plurisubharmonic. If another pair is used, the difference of the potentials has smooth $\ddc$. Taking a smooth Hermitian trace and applying local elliptic regularity shows that the difference is smooth. Thus the ordinary type depends only on $S$.

The three-way characterization is \cref{lem:divisorial-potential-domination}. The ideal envelope preserves all multiplier ideals, so its generic Lelong number on each $D_j$ is still $c_j$. The same lemma gives $Q_\Omega[v]\preceq v$. Also $Q_\Omega[v]\geq v-\sup v$, so these functions are ordinarily equivalent. Consequently $Q_\Omega[v]$ is admissible in the ordinary envelope of $v$, giving $Q_\Omega[v]\leq P_\Omega[v]$. The reverse inequality is \cref{prop:p-below-i}. This proves the envelope identity and ordinary equivalence. The final assertion uses the positive closed current of finite mass already constructed from the Gauduchon estimate.
\end{proof}

This realization describes the divisorial part on one specified model. It does not identify the higher-codimensional singularities needed to recover every $\tau_{Y,u}(E)$ on further modifications. In the curve-fibration setting, \cref{thm:curve-fibration-exact-trace} gives that additional identification. For general trace data it remains a separate problem. The canonical ordinary type here is selected by the smooth residual term; other potentials with the same multiplier ideals need not belong to it.
