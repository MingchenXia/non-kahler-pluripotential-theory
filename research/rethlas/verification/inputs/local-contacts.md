Run_id: local_contacts_01

Statement: Audit three precise extensions: (1) ordered-contact inequality for extended MA measures of arbitrary smooth real backgrounds, without finite total mass; (2) continuity and uniform Lipschitz dependence of envelopes of continuous obstacles for a strictly positive Hermitian background; (3) passage from bounded to unbounded quasi-continuous obstacles for semipositive theta, CONDITIONAL ON bounded-obstacle contact support. The third assertion is only a reduction, not an unconditional proof of bounded contact support. Envelopes are defined by the usc-regularized supremum of theta-psh competitors below the obstacle quasi-everywhere (outside a pluripolar set); the pointwise definition is equivalent for usc obstacles. X is connected compact, currents have canonical qpsh representatives, ddc=i/(2pi) partial bar-partial. All extended measures discard poles and may have infinite total mass.

Accepted foundations, all stated separately in the manuscript: bounded local non-closed BT products, positivity when their bounded-potential currents are positive, locality, weak continuity under uniform or bounded capacity convergence, and uniform capacity control for a fixed bounded range; products with a fixed bounded qpsh potential and varying smooth form are polynomial with locally finite-variation coefficients. Arbitrary smooth backgrounds have positive extended measures from restricted signed constant truncations, locally dominated by a larger Hermitian background; smooth-gauge intrinsicness and locality were independently audited in general_background_01. Smooth decreasing exact-background approximation for bounded Hermitian potentials and normalized L1 compactness were independently audited in compactness_regularization_01. The standard local envelope theorem and Choquet extraction hold with polar exceptional sets. Basic Radon measure regularity, weak convergence on compact sets and smooth-form freezing are allowed. Do not import any of the three conclusions. Pay attention to varying neighborhoods as epsilon tends to zero, positivity before using the weak-limit compact-set inequality, quasi-everywhere obstacle conventions and any hidden infinite-minus-infinite subtraction. The later monotonicity/continuity arguments must not use BMP, PVP or implicit bigness. The full source chapters can be read if a cross-reference needs context, but missing hypotheses cannot be inferred from their titles.

Proof:

\begin{proposition}[Ordered contact sets]\label{prop:ordered-contact-general}
Let $\theta$ be any smooth real $(1,1)$-form and let $u,v\in\PSH(X,\theta)$ satisfy $u\leq v$. Then
\[
 \mathbf1_{\{u=v\}}\mathrm{MA}^{\mathrm{ext}}_\theta(u)
 \leq\mathbf1_{\{u=v\}}\mathrm{MA}^{\mathrm{ext}}_\theta(v).
\]
No finiteness of either extended mass is assumed.
\end{proposition}
\begin{proof}
We first prove a local bounded version. Let $a\leq b$ be bounded quasi-plurisubharmonic functions on a coordinate domain and suppose
$\gamma+\ddc a\geq0$ and $\gamma+\ddc b\geq0$ for a smooth form $\gamma$. Set
\[
 m_\delta=\max(a,b-\delta),\qquad \delta>0.
\]
Then $b-\delta\leq m_\delta\leq b$, so the positive bounded-product measures of $m_\delta$ converge weakly on compact subsets to that of $b$. On the plurifine open set $\{a>b-\delta\}$ they agree with that of $a$, by locality. This set contains $\{a=b\}$. Therefore, for every compact $K\subset\{a=b\}$, the upper bound for weak limits on compact sets gives
\[
 \int_K(\gamma+\ddc a)^n
 =\lim_{\delta\downarrow0}\int_K(\gamma+\ddc m_\delta)^n
 \leq\int_K(\gamma+\ddc b)^n.
\]
Inner regularity on any Borel subset of the equality set proves the bounded assertion. This argument uses positivity, so we do not apply it directly to signed global truncation products.

To treat $u,v$, fix a coordinate ball with a constant positive form $\kappa$, a level $t>0$, and $\epsilon>0$. On smaller neighborhoods freeze $\theta$ to a constant form $\theta'$ with
$-\epsilon\kappa\leq\theta-\theta'\leq\epsilon\kappa$. Choose a quadratic function $r$ with
$\ddc r=\theta'+\epsilon\kappa$. Then $u+r$ and $v+r$ are plurisubharmonic. For a large integer $k$ put
\[
 a_k=\max(u+r,-k)-r,\qquad
 b_k=\max(v+r,-k)-r.
\]
They are bounded on relatively compact neighborhoods, satisfy $a_k\leq b_k$, and
\[
 \theta+2\epsilon\kappa+\ddc a_k
 =\ddc\max(u+r,-k)+(\theta-\theta'+\epsilon\kappa)\geq0,
\]
with the same inequality for $b_k$. Apply the bounded assertion with
$\gamma=\theta+2\epsilon\kappa$.

On $D_t=\{u>-t\}$, both $u$ and $v$ are above $-t$. Taking $k>t+\sup|r|$ makes $a_k=u$ and $b_k=v$ on $D_t$. Restrict the bounded inequality to $\{u=v\}\cap D_t$ and use locality. It gives the desired contact inequality for background $\theta+2\epsilon\kappa$ on that set. The smaller neighborhoods cover the original ball, so the restricted inequality holds throughout it.

Now choose a larger Hermitian background $\Omega\geq\theta$ and fixed bounded truncations $u_t=\max(u,-t)$, $v_t=\max(v,-t)$. On $D_t$, the products just used equal the restrictions of
$(\theta+\ddc u_t+2\epsilon\kappa)^n$ and
$(\theta+\ddc v_t+2\epsilon\kappa)^n$. These are polynomials in $\epsilon$ whose coefficients have locally finite variation. They converge in local total variation as $\epsilon\downarrow0$, including after restriction to $\{u=v\}\cap D_t$. This proves the inequality for background $\theta$ on each finite level. Finally let $t\to+\infty$. The common pole set has zero extended mass, and the levels exhaust its complement in the equality set.
\end{proof}


\begin{proposition}[Continuous obstacles for a Hermitian form]
\label{prop:continuous-obstacle-envelope}
If $f$ is continuous and $\omega$ is Hermitian, then $P_\omega(f)$ is continuous. Moreover,
\[
 \|P_\omega(f)-P_\omega(g)\|_\infty\leq\|f-g\|_\infty
 \quad(f,g\in C^0(X)).
\]
\end{proposition}
\begin{proof}
The constant $\min_Xf$ is a competitor, so $p=P_\omega(f)$ is bounded. The local envelope theorem gives $p\leq f$ quasi-everywhere, and continuity of $f$ makes this inequality pointwise. Choose smooth $v_j\downarrow p$ by \cref{thm:bounded-exact-regularization}. For every $\epsilon>0$, the continuous functions $v_j-f$ decrease to a function at most zero. Compactness shows that $v_j\leq f+\epsilon$ everywhere for all large $j$: otherwise their decreasing compact $\epsilon$-superlevel sets would have nonempty intersection. Hence $v_j-\epsilon$ is a competitor and
\[
 p\leq v_j\leq p+\epsilon.
\]
Thus $v_j\to p$ uniformly, proving continuity. The last inequality follows directly from the competitors and
$P_\omega(g+c)=P_\omega(g)+c$ for constants $c$.
\end{proof}


\begin{proposition}[Removing the lower bound on the obstacle]
\label{prop:unbounded-contact-reduction}
Let $\theta\geq0$ be smooth. Assume that the contact-support assertion is known for every bounded quasi-continuous obstacle. Then it holds for every quasi-continuous obstacle $f$ for which $p=P_\theta(f)$ is a genuine potential. This implication requires no upper mass bound.
\end{proposition}
\begin{proof}
The local envelope theorem and a countable Choquet family give $p\leq f$ outside a pluripolar set. Choose $M>\sup_Xp$ and replace $f$ by $\min(f,M)$. This does not change its envelope: $p$ itself is a competitor for the smaller obstacle. It suffices to prove support on the contact set for this smaller obstacle, because $p<M$ and therefore it has the same contact set as the original one.

Set $f_j=\max(f,-j)$ and $p_j=P_\theta(f_j)$. The constants $-j$ are admissible, so $p_j$ is bounded. The assumed bounded theorem gives $p_j\leq f_j$ quasi-everywhere and
\[
 \mathbf1_{\{p_j<f_j\}}\mathrm{MA}_\theta(p_j)=0.
\]
The sequence $p_j$ decreases and stays above $p$. Its limit is a genuine $\theta$-plurisubharmonic function, lies below $f$ quasi-everywhere, and is therefore a competitor for $p$. Hence $p_j\downarrow p$.

Fix $k$ and $C>0$. Define the bounded nonnegative quasi-continuous function
\[
 H_{k,C}=\min\{1,(f-p_k)_+\}\,
                  \min\{1,(p+C)_+\},
 \qquad a_+=\max(a,0).
\]
Values on pluripolar exceptional sets are immaterial. Where this coefficient is positive, $p_k<f$ and $p>-C$. For $j\geq k$, we then have
$p_j\leq p_k<f\leq f_j$ and $p_j\geq p>-C$. Locality and the bounded support assertion imply
\[
 \int_X H_{k,C}\,
       \mathrm{MA}_\theta(\max(p_j,-C))=0.
\]
The truncated potentials are uniformly bounded and decrease to $\max(p,-C)$. Their measures converge weakly by bounded Bedford--Taylor continuity. They also have uniform local capacity bounds, so the same convergence holds against the fixed bounded quasi-continuous coefficient $H_{k,C}$: remove a set of small capacity, approximate on its complement by a continuous function, and then let that capacity tend to zero. Consequently,
\[
 \int_X H_{k,C}\,
       \mathrm{MA}_\theta(\max(p,-C))=0.
\]
By locality this says that the extended measure of $p$ vanishes on
$\{p_k<f\}\cap\{p>-C\}$. These sets increase to $\{p<f\}$ off the pole set when first $k$ and then $C$ tend to infinity. Continuity from below of positive measures proves the assertion, even if the total extended mass is infinite.
\end{proof}

