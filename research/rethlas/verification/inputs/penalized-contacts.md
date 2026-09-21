Run_id: penalized_contacts_01

Statement: Audit the smooth proper exponential existence proof, smooth sub/supersolution comparison, and the complete bounded-envelope contact-support reconstruction below. The final result allows ANY smooth semipositive background, without bigness, BMP or PVP. Accepted inputs: standard elliptic Fredholm, Schauder and implicit-function theorems; the higher-estimate/semilinear consequence in book/author/section_smooth_estimates.tex (separately under independent audit smooth_second_estimate_01); bounded smooth strict exact-Hermitian-background decreasing regularization from compactness_regularization_01; canonical qpsh, local envelope theorem, Choquet lemma, bounded Bedford-Taylor calculus and uniform capacity control; bounded strict domination for a strictly positive Hermitian background, proved independently in section_modified_comparison.tex (currently audited as bounded_comparison_01). Continuous obstacle envelopes with Hermitian background are continuous and 1-Lipschitz in sup norm, independently audited in local_contacts_01. All these accepted inputs are explicit. Do NOT import proper exponential existence, penalized convergence, C1,1 regularity of envelopes, or bounded-obstacle contact support. Check the actual proofs, especially signs of subsolution comparison, arbitrary rates of the smooth approximants' minimum determinant, the order of j/beta limits, the lsc obstacle approximation and identification by domination, the elementary decreasing lsc approximation of a bounded quasi-continuous function, and passage to semipositive backgrounds with quasi-continuous test coefficients. Independence of upper mass and bigness must be checked. Source comparison: GL22 Theorem2.3 uses a stronger smooth regularity theorem; our proof replaces that step and must stand on its supplied assumptions. Source /Users/mingchen/Non-Kahler/research/sources/GL22.pdf and GL22.txt. This audit does NOT include unbounded contact reduction, which has already been checked conditionally in local_contacts_01 and will now use the bounded conclusion.

Proof:

\section{The smooth exponential equation}

\begin{theorem}\label{thm:smooth-proper-existence}
For every $\lambda>0$ and every smooth real $F$, there is a unique smooth $u$ with $\omega_u>0$ such that
\[
 \omega_u^n=e^{\lambda u+F}\omega^n.
\]
There is no free additive constant, and
\[
 -\lambda^{-1}\sup_XF\leq u\leq-\lambda^{-1}\inf_XF.
\]
\end{theorem}
\begin{proof}
At a minimum of $u$, the equation gives $\lambda u+F\geq0$; at a maximum it gives $\lambda u+F\leq0$. These inequalities prove the stated bounds.

Consider the equations
\[
 \omega_{u_t}^n=e^{\lambda u_t+tF}\omega^n,\qquad0\leq t\leq1.
\]
At $t=0$, $u_0=0$ is a solution. The linearization in $u$ is $L_u-\lambda$. Its kernel is zero by the maximum principle. Its Fredholm index is zero: deform its positive principal coefficients to those of a fixed Laplacian while keeping the negative zeroth-order term. The latter operator is invertible, and elliptic Fredholm index is constant under this deformation. Thus $L_u-\lambda$ is an isomorphism between the usual H\"older spaces, with bounded inverse by Schauder theory. The implicit function theorem proves openness.

The extrema bounds give $\|u_t\|_\infty\leq\lambda^{-1}\|F\|_\infty$. The semilinear consequence of \cref{thm:hermitian-second-estimate} gives uniform ellipticity and all higher bounds. A subsequence along any converging sequence of solvable parameters therefore converges smoothly to a strictly positive solution at the limit. This proves closedness, and hence existence at $t=1$. Uniqueness is \cref{prop:exp-smooth-unique}.
\end{proof}

\begin{proposition}[Smooth subsolutions and supersolutions]\label{prop:smooth-proper-comparison}
Let $\lambda>0$, let $F$ be smooth, and let $v,w$ be smooth strictly $\omega$-plurisubharmonic functions. If
\[
 \omega_v^n\geq e^{\lambda v+F}\omega^n,
 \qquad \omega_w^n\leq e^{\lambda w+F}\omega^n,
\]
then $v\leq w$.
\end{proposition}
\begin{proof}
If $v-w$ had a positive maximum at $x$, then $\omega_v(x)\leq\omega_w(x)$. Taking determinants and applying the two assumptions would give
$e^{\lambda v(x)+F(x)}\leq e^{\lambda w(x)+F(x)}$, contradicting $v(x)>w(x)$.
\end{proof}

For a fixed smooth obstacle $f$, the choice $\lambda=\beta$ and $F=-\beta f$ gives
\[
 \omega_{u_\beta}^n=e^{\beta(u_\beta-f)}\omega^n.
\]
These equations penalize values above the obstacle. In \cref{prop:smooth-obstacle-support} we use them to construct its envelope and prove contact support. The necessary convergence will use only bounded regularization and the comparison just proved.


We first prove support for bounded obstacles. The proof follows the approximation structure of \cite[Theorem 2.3]{GL22}; bounded regularization and the smooth exponential equation supply the smooth step directly.

\begin{proposition}[The penalized envelope]\label{prop:smooth-obstacle-support}
Let $\omega$ be Hermitian and $f$ smooth. The solutions
\[
 \omega_{u_\beta}^n=e^{\beta(u_\beta-f)}\omega^n,\qquad\beta>0,
\]
converge uniformly as $\beta\to+\infty$ to $p=P_\omega(f)$. Moreover,
\[
 \mathbf1_{\{p<f\}}\omega_p^n=0.
\]
\end{proposition}
\begin{proof}
Existence is \cref{thm:smooth-proper-existence}. Choose $A\geq0$ with $\ddc f\leq A\omega$. At a maximum of $u_\beta-f$,
\[
 \omega_{u_\beta}\leq\omega+\ddc f\leq(1+A)\omega.
\]
The equation gives
\[
 u_\beta\leq f+\frac{C_f}{\beta},\qquad C_f=n\log(1+A).
\]
Thus $u_\beta-C_f/\beta$ is an envelope competitor, and
$u_\beta\leq p+C_f/\beta$.

The function $p$ is continuous by \cref{prop:continuous-obstacle-envelope}. Choose smooth strictly $\omega$-plurisubharmonic $v_j\downarrow p$ by \cref{thm:bounded-exact-regularization}; convergence is uniform by compactness. For any $\delta>0$, choose $j$ so that
\[
 p\leq v_j\leq p+\delta/2.
\]
Then $v_j-\delta\leq f$. Positivity and compactness give a number $c_j>0$ such that $\omega_{v_j}^n\geq c_j\omega^n$. Put $C_j=\max(0,-\log c_j)$. The function
\[
 w_{j,\beta}=v_j-\delta-C_j/\beta
\]
satisfies
\[
 \omega_{w_{j,\beta}}^n=\omega_{v_j}^n
 \geq e^{-C_j}\omega^n
 \geq e^{\beta(w_{j,\beta}-f)}\omega^n.
\]
Smooth exponential comparison gives $w_{j,\beta}\leq u_\beta$. Consequently
\[
 p-\delta-C_j/\beta\leq u_\beta\leq p+C_f/\beta.
\]
First let $\beta$ tend to infinity with $j$ fixed, and then let $\delta\downarrow0$. This proves uniform convergence. It also gives the uniform boundedness needed for Bedford--Taylor convergence of the measures.

On a compact subset of the open set $\{p<f\}$, uniform convergence gives $u_\beta-f\leq-\epsilon$ for all large $\beta$, with some $\epsilon>0$. There the measures have densities at most $e^{-\beta\epsilon}$. Testing with continuous functions of compact support in that open set and passing to the bounded-product limit gives $\omega_p^n=0$ there.
\end{proof}

Only strict positivity of each fixed $v_j$ is needed. The number $c_j$ can tend to zero arbitrarily fast. No estimate for the derivatives of $u_\beta$ uniform in $\beta$ has been used.

\begin{proposition}[Continuous and lower semicontinuous obstacles]
\label{prop:lsc-obstacle-support}
If $\omega$ is Hermitian and $f$ is bounded and lower semicontinuous, then $P_\omega(f)$ is bounded, lies below $f$ quasi-everywhere, and its measure is concentrated on $\{P_\omega(f)=f\}$.
\end{proposition}
\begin{proof}
Suppose first that $f$ is continuous. Choose smooth $f_j\to f$ uniformly. The envelope Lipschitz bound gives $p_j=P_\omega(f_j)\to p=P_\omega(f)$ uniformly. On every compact subset of $\{p<f\}$, the inequalities $p_j<f_j$ hold on a neighborhood for all large $j$. The preceding proposition and bounded-product convergence then give $\omega_p^n=0$ on $\{p<f\}$.

For lower semicontinuous $f$, choose continuous $f_j\uparrow f$, with common upper and lower bounds. For example, for a fixed compatible distance $d$ one may take
\[
 f_j(x)=\inf_{y\in X}\bigl(f(y)+j d(x,y)\bigr).
\]
These functions are Lipschitz and increase to $f$: if convergence failed at $x$, approximate minimizers would approach $x$, contradicting lower semicontinuity.

The functions $p_j=P_\omega(f_j)$ increase, stay bounded, and have a bounded plurisubharmonic regularized limit $p_\infty=(\lim_jp_j)^*$. A countable union of pluripolar exceptional sets shows that $p_\infty\leq f$ quasi-everywhere. Thus $p_\infty\leq P_\omega(f)$.

For fixed $k$, the set $\{p_\infty<f_k\}$ is open. If $j\geq k$, then $p_j\leq p_\infty<f_k\leq f_j$ there, so the continuous-obstacle case gives zero measure on that open set. Increasing bounded Bedford--Taylor convergence and the weak-limit inequality for open sets yield
\[
 \omega_{p_\infty}^n(\{p_\infty<f_k\})=0.
\]
Taking the union over $k$ gives zero measure on $\{p_\infty<f\}$, hence also on $\{p_\infty<P_\omega(f)\}$ outside a pluripolar set. By bounded domination, \cref{thm:bounded-strict-domination}, $p_\infty\geq P_\omega(f)$. They are therefore equal, and the assertion follows.
\end{proof}

\begin{lemma}[Approximation outside small exceptional sets]
\label{lem:quasicont-lsc-approximation}
Every bounded quasi-continuous function $f$ admits bounded lower semicontinuous functions $f_j$ with common bounds such that $f_j\downarrow f$ quasi-everywhere and $f_j\to f$ in capacity.
\end{lemma}
\begin{proof}
Choose open sets $O_j$ with capacity at most $2^{-j}$ such that $f$ is continuous on $X\setminus O_j$, and set $G_j=\bigcup_{k\geq j}O_k$. Then $G_j$ decreases, its capacity tends to zero, and $f$ is continuous on its closed complement. Choose $M\geq\sup_Xf$ and define
\[
 f_j=f\ \hbox{on }X\setminus G_j,\qquad f_j=M\ \hbox{on }G_j.
\]
At a boundary point of $G_j$, limits from the closed complement give $f$, while values from inside are at least that value. Thus $f_j$ is lower semicontinuous. The functions decrease to $f$ outside $\bigcap_jG_j$, a capacity-zero set. Their difference from $f$ is supported in $G_j$, which also proves convergence in capacity.
\end{proof}

\begin{theorem}[Bounded contact support]\label{thm:bounded-contact-support}
Let $\theta\geq0$ be smooth and let $f$ be bounded and quasi-continuous. Then $p=P_\theta(f)$ is bounded, $p\leq f$ quasi-everywhere, and
\[
 \mathbf1_{\{p<f\}}\mathrm{MA}_\theta(p)=0.
\]
No bigness or bounded mass hypothesis is required.
\end{theorem}
\begin{proof}
First suppose $\theta=\omega$ is Hermitian. Choose $f_j\downarrow f$ quasi-everywhere as in \cref{lem:quasicont-lsc-approximation}. The bounded functions $p_j=P_\omega(f_j)$ decrease to $p$. Indeed their limit is a competitor for $p$, since it lies below $f$ quasi-everywhere; the reverse inequality follows from monotonicity.

For fixed $k$, put $H_k=\min\{1,(f-p_k)_+\}$. It is bounded and quasi-continuous. Where $H_k>0$ and $j\geq k$, we have $p_j\leq p_k<f\leq f_j$, outside a pluripolar set. The lower semicontinuous case therefore gives
\[
 \int_X H_k\,\omega_{p_j}^n=0.
\]
Bounded-product convergence remains valid against this fixed quasi-continuous coefficient. To see this, remove a set of small capacity on which $H_k$ may be discontinuous. The uniformly bounded potentials give uniform capacity control of their measures; on the compact complement, extend the continuous coefficient and use weak convergence. Let the removed capacity tend to zero. Thus
$\int_XH_k\,\omega_p^n=0$. The sets $\{p_k<f\}$ increase to $\{p<f\}$, proving support.

For general semipositive $\theta$, set $\theta_j=\theta+j^{-1}\omega$ with $\omega$ Hermitian. The functions $p_j=P_{\theta_j}(f)$ have the common bounds $\inf_Xf\leq p_j\leq\sup_Xf$ and decrease. Their limit is $\theta$-plurisubharmonic by distributional convergence, lies below $f$ quasi-everywhere, and hence equals $p=P_\theta(f)$. For each fixed $k$, the same coefficient $H_k=\min\{1,(f-p_k)_+\}$ gives
\[
 \int_XH_k\,\mathrm{MA}_{\theta_j}(p_j)=0\qquad(j\geq k).
\]
All $p_j$ are bounded potentials for the fixed Hermitian form $\theta+\omega$. Expand the products with $\theta_j$ against that fixed background. Bounded-product convergence and uniform capacity control pass the displayed identity to $\mathrm{MA}_\theta(p)$, including its quasi-continuous coefficient. Exhausting $\{p<f\}$ as before completes the proof.
\end{proof}
