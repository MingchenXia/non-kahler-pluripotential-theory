Run_id: compactness_regularization_01

Statement: Verify normalized L1 compactness and the full elementary bounded exact-background regularization argument in the supplied chapter. The accepted standard local inputs are the local psh compactness dichotomy, canonical representatives, submean/Poisson inequalities, convolution calculus and basic distributions, as supplied by SGPT/standard potential theory. Do not import global regularization or global compactness: they are being proved here. Pay particular attention to the uniform comparison of local convolutions for bounded discontinuous functions, the gluing with smooth maxima of variable local branches, curvature errors for a non-closed theta, and the decreasing diagonal. Check positivity, monotonicity and signs in the final rescaling. The construction is based on Błocki--Kołodziej 2007; the primary source is /Users/mingchen/Non-Kahler/research/sources/BK07.pdf. Treat that paper as attribution/comparison, not as a substitute for auditing the reconstructed proof. No BMP, PVP, closedness or analytic-singularity regularization is assumed. X is connected and compact.

Proof:

\chapter{Compactness and bounded regularization}
\label{chap:compactness}

Two global facts enter repeatedly in the arguments that follow: normalized potentials have a uniform $L^1$ bound, and bounded potentials for a Hermitian background admit smooth decreasing approximation with that background preserved. Neither assertion involves a Monge--Amp\`ere mass bound. We prove them from local plurisubharmonic compactness, convolution and smooth maxima.

\section{Normalized compactness}

Fix a smooth positive volume form $dV$. We use the standard local compactness theorem from \cite{SGPT}: a sequence of plurisubharmonic functions locally bounded above has a subsequence which either converges in $L^1_{\loc}$ to a plurisubharmonic function or tends locally uniformly to $-\infty$. We also use the local submean inequality and the canonical representative of an $L^1$ plurisubharmonic limit.

\begin{theorem}\label{thm:normalized-compactness}
For any smooth real $(1,1)$-form $\theta$, the family
\[
 \mathcal K_\theta=\{u\in\PSH(X,\theta):\sup_Xu=0\}
\]
is compact in $L^1(X,dV)$. In particular, there is a constant $C_\theta$ such that
\[
 \int_X|u|\,dV\leq C_\theta\quad(u\in\mathcal K_\theta).
\]
The empty family is allowed.
\end{theorem}
\begin{proof}
Let $(u_j)$ be a sequence in this family and choose $x_j$ with $u_j(x_j)=0$. Passing to a subsequence, suppose $x_j\to x$. Cover $X$ by finitely many connected coordinate balls, and on a slightly larger ball choose a fixed smooth correction $r_i$ for which $u_j+r_i$ is plurisubharmonic. Such corrections exist because $\theta$ is smooth. These local functions are uniformly bounded above, since $u_j\leq0$.

On a ball containing $x$ in its interior, the alternative of locally uniform convergence to $-\infty$ is impossible: the values at $x_j$ stay bounded below. Local compactness therefore gives an $L^1$-convergent subsequence on this ball. If a second ball overlaps it, local compactness on the second ball cannot yield convergence to $-\infty$ on compact subsets of the overlap, since the first limit is finite almost everywhere there. Thus a further subsequence converges in $L^1$ on the second ball. The intersection graph of a finite connected open cover of connected $X$ is connected. Repeating along that graph and taking finitely many subsequences gives local $L^1$ convergence everywhere. A partition of unity then gives convergence in $L^1(X)$ to a function $u$.

The inequalities $\ddc u_j\geq-\theta$ pass to distributions. The local canonical representatives of $u+r_i$ are plurisubharmonic and agree on overlaps after subtracting their corrections. They define a global $\theta$-plurisubharmonic representative, still denoted by $u$. Since $u_j\leq0$, it satisfies $u\leq0$.

We check that the supremum has not decreased. For a fixed small radius around $x_j$ inside the first coordinate ball, apply the submean inequality to $u_j+r_i$. Local $L^1$ convergence allows passage to the limit in the ball averages, also as their centers approach $x$: the averages of the differences tend to zero by $L^1$ convergence, and translating the indicator of a fixed ball is continuous for the integral of a fixed $L^1$ function. Letting the radius tend to zero gives
\[
 0+r_i(x)=\lim_j(u_j+r_i)(x_j)\leq(u+r_i)(x).
\]
Thus $u(x)=0$, and the limit belongs to $\mathcal K_\theta$. This proves sequential compactness, which is compactness in the metric space $L^1(X)$.

If the displayed norm bound failed, choose a sequence whose $L^1$ norms tend to infinity. Its convergent subsequence would have bounded norms, a contradiction.
\end{proof}

The connectedness assumption matters. On a disconnected manifold, fixing the maximum on one component leaves the additive constants on other components uncontrolled. Our standing convention that $X$ is connected removes this issue.

\begin{corollary}\label{cor:decreasing-limit}
A decreasing sequence in $\PSH(X,\theta)$ with uniformly bounded $L^1$ norms has a genuine $\theta$-plurisubharmonic limit and converges to it in $L^1$.
\end{corollary}
\begin{proof}
Local decreasing-limit theory gives a quasi-plurisubharmonic limit or the function $-\infty$ on each connected coordinate neighborhood. The $L^1$ bound excludes the latter alternative, by Fatou's lemma applied to the negative parts. The local representatives glue. Finally, the sequence is bounded above by its first member; subtracting the sequence from that member and applying monotone convergence proves $L^1$ convergence.
\end{proof}

\section{Comparing local regularizations}

The elementary bounded case of the regularization argument in \cite{BK07} rests on a useful fact: local convolutions made in different holomorphic coordinates become uniformly close, even when the original bounded potential is not continuous. We include the estimates because ordinary uniform approximation of the potential itself is unavailable.

Let $u$ be a bounded plurisubharmonic function on a Euclidean domain. On a fixed relatively compact subset, for small $\delta>0$ put
\[
 S_\delta u(z)=\sup_{|\zeta-z|\leq\delta}u(\zeta),\qquad
 A_\delta u(z)=\fint_{|\zeta-z|=\delta}u(\zeta)\,d\sigma(\zeta),
 \qquad u_\delta=u*\rho_\delta,
\]
where $\rho$ is a smooth nonnegative radial mollifier of integral one, supported in the unit ball. A fixed larger neighborhood contains all balls below, and $B$ denotes a bound for the oscillation of $u$ there.

\begin{lemma}\label{lem:bounded-local-regularization}
For each fixed $A>1$,
\[
 S_{A\delta}u-S_\delta u\longrightarrow0,
 \qquad S_\delta u-u_\delta\longrightarrow0
\]
uniformly on compact subsets as $\delta\downarrow0$.
\end{lemma}
\begin{proof}
The maximum of a plurisubharmonic function on concentric balls is convex as a function of the logarithm of the radius. This follows by restricting to each complex line through the center and comparing on an annulus with the harmonic function affine in $\log|\zeta|$. For a fixed admissible radius $r>A\delta$, convexity gives
\begin{equation}\label{eq:bounded-log-radius}
 0\leq S_{A\delta}u-S_\delta u
 \leq\frac{B\log A}{\log(r/\delta)}.
\end{equation}
This proves the first assertion.

We compare the maximum with the spherical mean using the Poisson kernel in real dimension $2n$. For a point at distance at most $\delta/2$ from the center, the normalized Poisson kernel of the ball of radius $\delta$ is bounded below by a positive dimensional constant $c_n$. Since $u\leq S_\delta u$, the submean comparison with its harmonic extension gives
\[
 S_\delta u-S_{\delta/2}u
 \geq c_n(S_\delta u-A_\delta u).
\]
These inequalities are valid for bounded plurisubharmonic functions by local smoothing, followed by a decreasing limit. Equation \eqref{eq:bounded-log-radius} shows that $S_\delta u-A_\delta u$ tends uniformly to zero.

For $0<t\leq1$, the spherical mean is increasing with radius, and
\[
 0\leq A_\delta u-A_{t\delta}u
 \leq (S_\delta u-S_{t\delta}u)
                +(S_{t\delta}u-A_{t\delta}u).
\]
The first term is at most
$B\log(1/t)/\log(r/(t\delta))$ by logarithmic convexity of $S$, and the second is at most $C_nB/\log(r/(t\delta))$ by the preceding estimate. Write the radial convolution as an average of $A_{t\delta}u$ with the probability density
$\widehat\rho(t)=|\mathbb S^{2n-1}|t^{2n-1}\rho(t)$. Since
$\int_0^1(1+\log(1/t))\widehat\rho(t)\,dt<\infty$, integration gives
\[
 0\leq A_\delta u-u_\delta
 \leq\frac{C_{n,\rho}B}{\log(r/\delta)}.
\]
Combining the two comparisons proves the second assertion.
\end{proof}

\begin{corollary}\label{cor:coordinate-convolution}
Let $F:U\to V$ be biholomorphic and $u$ bounded and plurisubharmonic on $U$. The difference
\[
 u_\delta-\bigl((u\circ F^{-1})*\rho_\delta\bigr)\circ F
\]
tends locally uniformly to zero as $\delta\downarrow0$.
\end{corollary}
\begin{proof}
On a compact subset, $F$ and its inverse have uniformly bounded first derivatives. Thus, for a fixed $A>1$, the inverse image of a radius-$\delta$ ball about $F(z)$ lies between balls about $z$ of radii $\delta/A$ and $A\delta$. The two supremum regularizations are therefore bounded by one another at these enlarged radii. The first assertion of \cref{lem:bounded-local-regularization} makes their difference uniformly small. Its second assertion compares each of the two convolutions with the corresponding supremum regularization.
\end{proof}

\section{Gluing with a small curvature error}

We use a smooth maximum in finitely many real variables. Choose a smooth even probability density supported in $[-1,1]$, let $Z_1,\ldots,Z_N$ have its product distribution, and define
\[
 M_\tau(t_1,\ldots,t_N)
     =\mathbb E\max_i(t_i+\tau Z_i)\quad(\tau>0).
\]
Convolution makes $M_\tau$ smooth. It is convex, increasing in every argument, and satisfies
\[
 \max_i t_i\leq M_\tau(t)\leq\max_i t_i+\tau,
 \qquad M_\tau(t+c\mathbf1)=M_\tau(t)+c.
\]
If $t_i<\max_{j\ne i}t_j-2\tau$, the $i$th argument can be removed without changing the value. Also $M_\tau(t)$ is nondecreasing in $\tau$: it is a convex even function of $\tau$ because the distribution of $Z$ is symmetric.

If smooth functions $f_i$ satisfy $\ddc f_i\geq-\gamma$ for a common smooth form $\gamma$, then
\begin{equation}\label{eq:smooth-max-curvature}
 \ddc M_\tau(f_1,\ldots,f_N)\geq-\gamma.
\end{equation}
Indeed, the first-derivative coefficients are nonnegative and sum to one, by the translation identity, while the real Hessian of the convex function $M_\tau$ contributes a semipositive $(1,1)$-form in the chain rule. Closedness of $\gamma$ is irrelevant.

\begin{proposition}\label{prop:bounded-almost-regularization}
Let $\theta$ be smooth and real, $\omega$ Hermitian, and
$u\in\PSH(X,\theta)\cap L^\infty(X)$. There are smooth functions $v_j$ and numbers $\varepsilon_j\downarrow0$ such that
\[
 v_j\downarrow u,\qquad
 \theta+\varepsilon_j\omega+\ddc v_j\geq0.
\]
\end{proposition}
\begin{proof}
Fix $\epsilon>0$. By continuity of $\theta$, choose finitely many nested coordinate neighborhoods
$V_i\Subset W_i\Subset U_i$, with the $V_i$ covering $X$, and smooth quadratic functions $r_i$ such that
\[
 0\leq\ddc r_i-\theta\leq\epsilon\omega\quad\hbox{on }U_i.
\]
To make this choice, freeze the coefficients of $\theta$ at the center, add a small positive constant form, and shrink the coordinate neighborhood. Put $p_i=u+r_i$, a bounded plurisubharmonic function, and let $p_{i,\delta}$ be its convolution in $U_i$.

On overlaps of the closures of the $W_i$, \cref{cor:coordinate-convolution} and ordinary smooth approximation of $r_i-r_j$ show that
\begin{equation}\label{eq:overlap-regularization}
 (p_{i,\delta}-r_i)-(p_{j,\delta}-r_j)\longrightarrow0
 \quad\hbox{uniformly}.
\end{equation}
Choose $\eta_i\in C^\infty(U_i,[-1,0])$, zero on $V_i$ and equal to $-1$ near the boundary of $W_i$, and $C\geq1$ with $\ddc\eta_i\geq-C\omega$. Set
\[
 f_{i,\delta}=p_{i,\delta}-r_i+(\epsilon/C)\eta_i
 \quad\hbox{on }W_i.
\]
Each satisfies $\ddc f_{i,\delta}\geq-\theta-2\epsilon\omega$. Near a boundary point of $W_i$, some $V_j$ contains that point. Equation \eqref{eq:overlap-regularization} implies, for all small $\delta$,
\[
 f_{i,\delta}<f_{j,\delta}-\epsilon/(2C)
\]
on a neighborhood of that boundary point. Finiteness of the cover makes this separation uniform.

Take $\tau(\delta)\downarrow0$ as $\delta\downarrow0$, with $\tau(\delta)<\epsilon/(8C)$, and define on each point the smooth maximum of the branches whose $W_i$ contain it. A branch disappears only near the boundary of its $W_i$, where it is below another branch by more than $2\tau$. The removal property of $M_\tau$ therefore proves that these formulas define a global smooth function $\psi_{\epsilon,\delta}$. Equation \eqref{eq:smooth-max-curvature} gives
\[
 \theta+2\epsilon\omega+\ddc\psi_{\epsilon,\delta}\geq0.
\]
At every point there is a branch with $\eta_i=0$, and $p_{i,\delta}\geq p_i$. Hence $\psi_{\epsilon,\delta}\geq u$. For fixed $\epsilon$, the local convolutions decrease with $\delta$, and so does the smooth maximum when both its arguments and $\tau$ decrease. Its pointwise limit is
\[
 \max_{i:x\in W_i}\bigl(u(x)+(\epsilon/C)\eta_i(x)\bigr)=u(x).
\]
Thus $\psi_{\epsilon,\delta}\downarrow u$ as $\delta\downarrow0$, also in $L^1$.

We now choose a decreasing diagonal, rather than assuming that an arbitrary diagonal is decreasing. Take $\epsilon_j\downarrow0$ and put
$v_j=\psi_{\epsilon_j,\delta_j}+2^{-j}$. Choose $\delta_j$ so small that
\[
 \|\psi_{\epsilon_j,\delta_j}-u\|_{L^1}\leq2^{-j},
 \qquad v_j<v_{j-1}\quad(j\geq2).
\]
The second choice is possible because $v_{j-1}\geq u+2^{-j+1}$. More explicitly, the continuous functions
$\psi_{\epsilon_j,\delta}+2^{-j}-v_{j-1}$ decrease pointwise to a function bounded above by $-2^{-j}$. Their nonnegative level sets are decreasing compact sets with empty intersection, so one of them is empty. The resulting sequence decreases, converges to $u$ in $L^1$, and stays above $u$. Its pointwise limit equals $u$ by uniqueness of canonical quasi-plurisubharmonic representatives. Taking $\varepsilon_j=2\epsilon_j$ proves the proposition.
\end{proof}

\section{Preserving a Hermitian background}

\begin{theorem}[Bounded smooth approximation]\label{thm:bounded-exact-regularization}
For $u\in\PSH(X,\omega)\cap L^\infty(X)$ there are smooth functions $u_j\downarrow u$ such that
\[
 \omega+\ddc u_j>0.
\]
The functions $u_j$ are uniformly bounded.
\end{theorem}
\begin{proof}
Subtract a constant so that $u\leq-2$. Apply \cref{prop:bounded-almost-regularization} with $\theta=\omega$. By discarding initial terms, arrange $v_j<0$ everywhere. Write
\[
 u_j=\frac{v_j}{1+2\varepsilon_j}.
\]
Then
\[
 \omega+\ddc u_j
 \geq\frac{\varepsilon_j}{1+2\varepsilon_j}\omega>0.
\]
Because $v_j$ is negative and decreases while the positive denominator decreases to one, $u_j$ also decreases and converges to $u$. It lies between $u$ and its first smooth member, which gives uniform boundedness. Restore the subtracted constant.
\end{proof}

The sign in this rescaling argument is essential: it is what preserves monotonicity when the denominator changes. The use of a positive Hermitian background is equally explicit. For an arbitrary smooth form $\theta$, the preceding proposition gives a small curvature error; this argument does not remove that error while preserving $\theta$.

The full regularization theorem of \cite{BK07} applies more broadly. Only the bounded version proved here is needed for the bounded product and mass arguments in the next chapter. Regularization with analytic singularities is a separate problem and will be treated in the singularity-theoretic part.
