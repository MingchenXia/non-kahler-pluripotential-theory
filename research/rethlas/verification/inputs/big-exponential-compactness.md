Run_id: big_exponential_compactness_01

Statement: Audit two related new consequences of the already reviewed arbitrary-big fixed-reference stability/compactness theory. First check the streamlined proof of the minimal ordinary-type zero-exponent equation, retaining its original statement and all estimates up to eq:big-normalized-uniform-type. Then check in full the new proposition on normalized exponential approximations and its symmetry corollary. Theta is an arbitrary smooth big possibly NONCLOSED real(1,1) form on a compact Hermitian manifold. No metric bounded mass or positive lower mass assumption is available.

Specific obligations: check that the shortened proof uses only the accepted compactness theorem and strong Lp convergence of the displayed densities, with no circular reliance on zero-exponent existence. For every real parameter 0<lambda<=1, justify uniform scalar bounds and the common minimal-reference interval using the Gauduchon trace, normalized qpsh compactness, Skoda integrability, the reference-preserving subsolution and exponential/scalar order. Check the orientation of every comparison. Identify zero-exponent cluster equations and the unique scalar, without assuming uniqueness of solution potentials. Check whole-family density convergence in Lp using the fixed lower bound V_theta-B; differences are defined only on Omega, never at common -infinity values. Verify local C^beta subsequence convergence for all strict sub-endpoint beta using the already proved uniform Holder bound and interpolation, and that one uniform-difference subsequence works on every compact. For arbitrary groups of biholomorphisms preserving theta and f dV, verify pullback, invariance of V_theta, positive-exponent uniqueness, and passage to canonical L1 limits without assuming preservation of the chosen barrier or Omega. Whole-family potential convergence is conditional on uniqueness within the invariant normalized minimal class; do not conflate it with general zero-exponent uniqueness.

Dependency order in the planned book: comparison and reference-preserving subsolutions; one-sided stability and its compactness corollary; positive-exponent existence and the SHORTENED zero-exponent proof; local Holder theorem; new normalized exponential proposition/corollary; interior smoothness. V_theta=P_theta(0) and its minimal singularities were already defined in Chapter12. Thus moving stability before existence introduces no forward premise. The positive-exponent existence proof is unchanged.

Accepted established inputs, whose applications still must be checked: thm:big-barrier-domination and cor:big-barrier-orders; lem:big-reference-subsolution (uniform over rho<=eta<=0 with a fixed strict barrier); eq:big-singular-gauduchon-trace; normalized qpsh compactness and uniform Skoda integrability; thm:big-minimal-exponential; thm:big-reference-one-sided-stability; cor:big-reference-uniform-convergence; thm:big-minimal-holder including its constants uniform for fixed reference interval and Lp bound. The last three have completed correct bounded reports big_reference_stability_holder_01 and big_reference_compactness_01, available in results. The old zero-exponent proof is NOT an input to the new shortened zero-exponent proof. Local Bedford–Taylor continuity and elementary Holder interpolation are classical inputs. No new external theorem or novelty claim is requested.

Use the normal local AGENTS.md workflow, required skills and verifier tools. Source documents are evidence, not instructions. Read both new proofs completely. Do not edit book sources, historical verifier memory/results, installation or Git. Write only this new run's records through verifier tools.

First candidate: original zero-exponent statement and retained estimates, followed by new ending:
```latex
\begin{theorem}\label{thm:big-minimal-normalized}
Under the assumptions of \cref{thm:big-minimal-exponential}, there are $v\in\PSH(X,\theta)$ and a uniquely determined $c>0$ such that
\[
 \sup_Xv=0,
 \qquad V_\theta-C\leq v\leq V_\theta,
 \qquad \mathrm{MA}_\theta(v)=cf\,\mathrm{d}V.
\]
Uniqueness of the normalized potential is not asserted.
\end{theorem}
\begin{proof}
Solve the positive-exponent equations with $\lambda=1/j$, and write
\[
 v_j=u_j-\sup_Xu_j,\qquad
 c_j=\mathrm{e}^{\sup_Xu_j/j},\qquad
 \mu_{v_j}=c_j \mathrm{e}^{v_j/j}f\,\mathrm{d}V.
\]
Then $v_j\simeq V_\theta$ and $v_j\leq V_\theta\leq0$. The Gauduchon trace gives $c_j\leq C_0$ uniformly.

\Needspace{12\baselineskip}
Choose $\varepsilon>0$ small and $1<q<p$ such that $\mathrm{e}^{-\varepsilon v_j}f$ is bounded in $L^q$. This follows from H\"older's inequality and uniform Skoda integrability of normalized potentials in a fixed enlarged Hermitian background. The subsolution lemma, with reference $V_\theta-1$ and the fixed barrier $\rho-1$, produces
\[
 V_\theta-1\leq\eta_j\leq V_\theta,
 \qquad
 \mu_{\eta_j}\geq m \mathrm{e}^{-\varepsilon v_j}f\,\mathrm{d}V
                 \geq mf\,\mathrm{d}V
\]
for a uniform $m>0$. Since $\mu_{v_j}\leq c_jf\,\mathrm{d}V$, scalar order gives $c_j\geq m$.

\Needspace{8\baselineskip}
Take $D=\varepsilon^{-1}\max\{0,\log(C_0/m)\}$ and put $w_j=\eta_j-D$. We have
\[
 \mathrm{e}^{\varepsilon(w_j-v_j)}\mu_{v_j}
 =c_j \mathrm{e}^{v_j/j+\varepsilon\eta_j-\varepsilon D-\varepsilon v_j}
           f\,\mathrm{d}V
 \leq m \mathrm{e}^{-\varepsilon v_j}f\,\mathrm{d}V
 \leq\mu_{w_j}.
\]
Exponential order therefore gives $v_j\geq w_j$. In particular
\begin{equation}\label{eq:big-normalized-uniform-type}
 V_\theta-1-D\leq v_j\leq V_\theta,
 \qquad m\leq c_j\leq C_0.
\end{equation}
% DRAFT replacement for the tail of thm:big-minimal-normalized.
% All estimates through eq:big-normalized-uniform-type are retained verbatim.
Extract a subsequence with $v_j\to v$ in $L^1$ and almost everywhere and
$c_j\to c\in[m,C_0]$. The limit is normalized, genuine and of minimal
ordinary type. The densities $c_j\mathrm{e}^{v_j/j}f$ have a common
$L^p$ bound. Hence \cref{cor:big-reference-uniform-convergence}, with
reference $V_\theta$, upgrades the convergence to uniform convergence of
differences on $\Omega$ and identifies the weak $L^p$ limit of the
densities with the density of $\mu_v$.

At almost every point $v_j$ converges to a finite value, so $v_j/j\to0$.
Since $v_j\leq0$ and $c_j\leq C_0$, dominated convergence gives
$c_j\mathrm{e}^{v_j/j}f\to cf$ in $L^p$. Therefore
$\mu_v=cf\,\mathrm{d}V$. Scalar uniqueness is
\cref{cor:big-barrier-orders}.

\end{proof}

```

Second candidate:
```latex
% DRAFT: independent review pending; not an active book input.
\subsection{Limits of normalized exponential solutions}

The fixed-reference compactness theorem also describes the approximation
used to construct the zero-exponent equation. It controls differences of
potentials uniformly on $\Omega$, even when the potentials themselves
are unbounded near its complement.

\begin{proposition}\label{prop:big-exponential-clusters}
Let $0\leq f\in L^p(\mathrm{d}V)$, $p>1$, be nonzero, and let
$u_\lambda\simeq V_\theta$ be the unique solution of
\[
 \mu_{u_\lambda}=\mathrm{e}^{\lambda u_\lambda}f\,\mathrm{d}V,
 \qquad \lambda>0.
\]
Put
\[
 v_\lambda=u_\lambda-\sup_Xu_\lambda,
 \qquad c_\lambda=\mathrm{e}^{\lambda\sup_Xu_\lambda}.
\]
For $0<\lambda\leq1$ there are constants $B,C,m>0$, independent of
$\lambda$, such that
\[
 V_\theta-B\leq v_\lambda\leq V_\theta,
 \qquad m\leq c_\lambda\leq C.
\]
The normalized family is relatively compact for uniform convergence of
differences on $\Omega$. As $\lambda\downarrow0$, every cluster limit
$v$ is normalized, has minimal singularities, and satisfies
\[
 \mu_v=cf\,\mathrm{d}V,
\]
where $c>0$ is the unique scalar in
\cref{thm:big-minimal-normalized}. Moreover,
\[
 c_\lambda\longrightarrow c,
 \qquad c_\lambda\mathrm{e}^{\lambda v_\lambda}f
          \longrightarrow cf\quad\text{in }L^p(\mathrm{d}V).
\]
Every sequence of parameters in $(0,1]$ has a subsequence for which the
potentials converge in $C^\beta$ on each compact subset of $\Omega$, for
all
\[
 0<\beta<\frac{2(p-1)}{np+3(p-1)}.
\]
No metric mass property is assumed.
\end{proposition}

\begin{proof}
The equation for $v_\lambda$ is
\[
 \mu_{v_\lambda}=c_\lambda\mathrm{e}^{\lambda v_\lambda}
                         f\,\mathrm{d}V.
\]
Fix a Gauduchon metric $\gamma$ and write
$\gamma^n=G\,\mathrm{d}V$. Since $v_\lambda\leq0$ and
$0<\lambda\leq1$, \eqref{eq:big-singular-gauduchon-trace} gives
\[
 c_\lambda^{1/n}
 \int_X\mathrm{e}^{v_\lambda/n}f^{1/n}G^{1-1/n}\,\mathrm{d}V
 \leq\int_X\theta\wedge\gamma^{n-1}.
\]
The integrals on the left have a positive uniform lower bound.
Otherwise quasi-plurisubharmonic compactness would give an almost
everywhere convergent subsequence of the normalized $v_\lambda$ with a
genuine limit, and dominated convergence would give a positive limit
integral, since $f$ is nonzero. Thus $c_\lambda\leq C$.

The lower-type estimate in the proof of
\eqref{eq:big-normalized-uniform-type} now applies for every
$0<\lambda\leq1$. More explicitly, uniform Skoda integrability gives
fixed $\varepsilon>0$ and $1<q<p$ with
$\|\mathrm{e}^{-\varepsilon v_\lambda}f\|_q$ uniformly bounded.
The reference-preserving subsolution lemma supplies
\[
 V_\theta-1\leq\eta_\lambda\leq V_\theta,
 \qquad \mu_{\eta_\lambda}\geq
 m\mathrm{e}^{-\varepsilon v_\lambda}f\,\mathrm{d}V
 \geq mf\,\mathrm{d}V
\]
for a fixed $m>0$. Scalar order, together with
$\mu_{v_\lambda}\leq c_\lambda f\,\mathrm{d}V$, gives
$c_\lambda\geq m$. Set
$D=\varepsilon^{-1}\max\{0,\log(C/m)\}$ and
$w_\lambda=\eta_\lambda-D$. Then
\[
 \mathrm{e}^{\varepsilon(w_\lambda-v_\lambda)}\mu_{v_\lambda}
 \leq m\mathrm{e}^{-\varepsilon v_\lambda}f\,\mathrm{d}V
 \leq\mu_{w_\lambda},
\]
since $\lambda v_\lambda\leq0$ and $\eta_\lambda\leq0$.
Exponential order gives $v_\lambda\geq w_\lambda$, proving the uniform
bounds with $B=1+D$.

The densities are bounded in $L^p$ by $C\|f\|_p$. Apply
\cref{cor:big-reference-uniform-convergence} with $\eta=V_\theta$.
Given any sequence $\lambda_j\downarrow0$, pass to a subsequence with
$v_{\lambda_j}\to v$ uniformly in differences on $\Omega$ and in
$L^1(X)$, and with $c_{\lambda_j}\to c_*\in[m,C]$.
The limit has the same reference bounds and is normalized. On the
complement of the pole set,
\[
 0\leq1-\mathrm{e}^{\lambda v_\lambda}
 \leq1-\mathrm{e}^{\lambda(V_\theta-B)}\longrightarrow0.
\]
Dominated convergence after multiplication by $f$ therefore gives
$\mathrm{e}^{\lambda v_\lambda}f\to f$ in $L^p$ for the whole family.
The compactness corollary identifies the limit equation as
$\mu_v=c_*f\,\mathrm{d}V$. Scalar uniqueness gives $c_*=c$.
Every subsequential scalar limit as $\lambda\downarrow0$ is therefore $c$, so
$c_\lambda\to c$. The stated density convergence follows.

Finally \cref{thm:big-minimal-holder} gives uniform local $C^\alpha$
bounds for every $\alpha$ below its endpoint. For
$0<\beta<\alpha$, uniform convergence and the elementary interpolation
inequality on smaller coordinate balls give
\[
 [v_{\lambda_j}-v]_{C^\beta}
 \leq C\|v_{\lambda_j}-v\|_\infty^{1-\beta/\alpha}
          [v_{\lambda_j}-v]_{C^\alpha}^{\beta/\alpha}
 \longrightarrow0.
\]
Use slightly larger compact neighborhoods for these estimates. The
uniformly convergent subsequence already supplied by compactness works
on every compact subset and for each sub-endpoint exponent; no further
choice depending on that exponent is needed.
\end{proof}

\begin{corollary}\label{cor:big-exponential-symmetries}
Suppose a group $G$ of biholomorphisms preserves $\theta$ and the measure
$f\,\mathrm{d}V$. Every $v_\lambda$ and every cluster limit as
$\lambda\downarrow0$ is $G$-invariant. If the normalized zero-exponent
equation has only one $G$-invariant solution of minimal singularities,
then the whole family $v_\lambda$ converges to it, uniformly in
differences on $\Omega$ and in each local $C^\beta$ topology from the
proposition.
\end{corollary}
\begin{proof}
For $g\in G$, pullback preserves $\theta$-plurisubharmonicity and
$V_\theta\circ g=V_\theta$, by the envelope definition. It also
preserves the positive-exponent equation. Its uniqueness gives
$u_\lambda\circ g=u_\lambda$, and normalization preserves this equality.
Pullback by a fixed smooth biholomorphism is continuous on $L^1(X)$,
since its Jacobian relative to the fixed smooth volume is bounded.
Every cluster limit is therefore invariant almost everywhere, hence in
canonical representatives. This argument does not require $g$ to
preserve the chosen barrier or $\Omega$.

Under the stated uniqueness within the invariant class, every cluster
limit is the same potential. Relative compactness then implies
convergence of the whole family in the uniform-difference metric:
a sequence staying a fixed positive distance from that potential would
have a convergent subsequence, a contradiction. The interpolation
argument above upgrades it to the asserted local $C^\beta$ convergence.
\end{proof}

The proposition gives compactness and identifies every cluster equation.
It does not by itself select a unique cluster potential. The additional
hypothesis in the corollary concerns only the invariant class; uniqueness
of all normalized solutions can fail, as in
\cref{thm:degenerate-hermitian-nonuniqueness}.

```

Accepted-input text for exact hypotheses and constants:

## section_big_minimal_comparison.tex
```latex
\section{Comparison above a strict singular barrier}
\label{sec:big-minimal-comparison}

In this and the next two sections, $\theta$ is an arbitrary smooth big real $(1,1)$-form. Neither semipositivity nor closedness is assumed. There is no bounded mass or uniform positive lower volume hypothesis. Fix a Hermitian form $\omega$ and a strict potential
\[
 \rho\leq0,\qquad \theta+\ddc\rho\geq\omega,
\]
with analytic poles along $Z$, smooth on $\Omega=X\setminus Z$. Such a potential is supplied by the classical regularization theorem, after decreasing $\omega$. We write $\mu_u=\mathrm{MA}_\theta(u)$. On $\Omega$, every potential bounded below by $\rho-C$ is locally bounded. Its local bounded product agrees with $\mu_u$ there, and the extended measure gives zero mass to $Z$. We reconstruct the arguments of \cite[Section 4]{BGL25}, where the bounded mass assumption used earlier in that paper is explicitly dropped.

\begin{lemma}\label{lem:big-local-comparison}
Let $B\Subset\Omega$ be a coordinate ball, and let $u,v$ be bounded $\theta$-plurisubharmonic functions on $B$. Assume
\[
 \liminf_{x\to\partial B}(u-v)(x)\geq0,
 \qquad \mathbf1_{\{u<v\}}\mu_u\leq
             \mathbf1_{\{u<v\}}\mu_v.
\]
Then $u\geq v$ on $B$.
\end{lemma}
\begin{proof}
Fix $\varepsilon>0$ and set $v_\varepsilon=\max(u,v-\varepsilon)$. It equals $u$ near the boundary. Locality on $\{u>v-\varepsilon\}$ and ordered contact on $\{u\leq v-\varepsilon\}$ show that
\[
 \mu_u\leq\mu_{v_\varepsilon}
\]
throughout $B$: the latter set is contained in $\{u<v\}$, where the assumed inequality applies.

Let $q$ be the ordinary plurisubharmonic envelope on $B$ of the bounded quasi-continuous obstacle $u-v_\varepsilon$, with the obstacle inequality understood quasi-everywhere. If $h<0$ is a smooth strictly plurisubharmonic defining function for the ball, then $Ah\leq u-v_\varepsilon\leq0$ for sufficiently large $A$. Hence $Ah\leq q\leq0$ and $q$ tends to zero at the boundary. We use here the classical local bounded-envelope contact theorem: $(\ddc q)^n$ is carried by $D=\{q=u-v_\varepsilon\}$. This is the ordinary Bedford--Taylor obstacle result, in the local theory of \cite{GZ17} and the preceding SGPT book; no nonclosed background enters that input.

Canonical representatives give $q+v_\varepsilon\leq u$. Ordered contact, followed by the preceding measure inequality, yields
\[
 \mathbf1_D\mathrm{MA}_\theta(q+v_\varepsilon)
 \leq\mathbf1_D\mu_u
 \leq\mathbf1_D\mu_{v_\varepsilon}.
\]
The positive expansion of $(\theta_{v_\varepsilon}+\ddc q)^n$ contains both $\mu_{v_\varepsilon}$ and $(\ddc q)^n$. Thus $\mathbf1_D(\ddc q)^n=0$, and contact support gives $(\ddc q)^n=0$. The classical bounded Bedford--Taylor comparison principle with zero boundary values implies $q=0$. Consequently $u\geq v_\varepsilon$, first quasi-everywhere and then everywhere. Let $\varepsilon\downarrow0$.
\end{proof}

\begin{theorem}\label{thm:big-barrier-domination}
Suppose $u,v\in\PSH(X,\theta)$ satisfy
\[
 \min(u,v)\geq\rho-C_0,\qquad v\leq u+C_1.
\]
If, for some $0\leq c<1$,
\[
 \mathbf1_{\{u<v\}}\mu_u\leq
 c\,\mathbf1_{\{u<v\}}\mu_v,
\]
then $u\geq v$. The measures need not have finite total mass.
\end{theorem}
\begin{proof}
Replace $\rho$ by $\widehat\rho=a\rho-A$, where $a>1$ is sufficiently close to one and $A$ is sufficiently large. Since
\[
 \theta+\ddc(a\rho)=a\theta_\rho+(1-a)\theta,
\]
we can arrange $\theta_{\widehat\rho}\geq\omega/2$, $\widehat\rho-v\leq-1$, and
$u-\widehat\rho\to+\infty$ when approaching $Z$. When $Z$ is empty, the last boundary condition is unnecessary. In the proof below write $r=\widehat\rho$.

Choose $0<\delta<1$ with $(1-\delta)^n>c$, and put $v_\delta=(1-\delta)v+\delta r$. Then
\[
 u-v_\delta\geq\delta(u-r)-(1-\delta)C_1.
\]
If its infimum $m$ on $\Omega$ were negative, a sequence $x_j$ approaching that infimum would have a subsequence converging to a point $x_0\in\Omega$. Choose a coordinate ball $B\Subset\Omega$ centered at $x_0$, identify it with $\{|z|<1\}$, and take
\[
 \eta(z)=b(1-|z|^2),\qquad 0<b<1,
 \qquad \omega/2+\ddc\eta\geq0.
\]
The function $w=v_\delta+\delta\eta+m$ is $\theta$-plurisubharmonic on $B$, and $\liminf_{\partial B}(u-w)\geq0$. Also
\[
 w-v=\delta(r-v+\eta)+m<0.
\]
Thus $\{u<w\}\subset\{u<v\}$, and positivity gives on this set
\[
 \mu_u\leq c\mu_v\leq(1-\delta)^n\mu_v\leq\mu_w.
\]
The local comparison lemma implies $u\geq w$ on $B$. Evaluating at $x_j$ gives $u(x_j)-v_\delta(x_j)\geq m+\delta\eta(x_j)$, contrary to $\eta(x_0)>0$. We have proved $u\geq v_\delta$. Let $\delta\downarrow0$ along values with $(1-\delta)^n>c$, and extend the resulting inequality from $\Omega$ by canonical representatives.
\end{proof}

\Needspace{20\baselineskip}
\begin{corollary}\label{cor:big-barrier-orders}
Let $u,v\geq\rho-C$ be $\theta$-plurisubharmonic and satisfy $u\simeq v$.
\begin{enumerate}
\item If $\mu_u\leq c\mu_v$ for $c\geq0$, then $c\geq1$.
\item If $\mu_u\leq \mathrm{e}^{\lambda(u-v)}\mu_v$ for $\lambda>0$, then $u\geq v$.
\end{enumerate}
In particular the positive-exponent equation has at most one solution in each such ordinary singularity type, and the normalized equation has at most one positive scalar in that type.
\end{corollary}
\begin{proof}
If $c<1$, apply the theorem to $u,v+A$ for every constant $A>0$. Its lower-barrier constant may depend on $A$, which causes no difficulty. The conclusion $u\geq v+A$ is impossible for all $A$. For the second assertion, restrict the measure inequality to $\{u<v-a\}$. There the factor is at most $\mathrm{e}^{-\lambda a}<1$, so the theorem gives $u\geq v-a$. Let $a\downarrow0$. Apply this assertion in both orders for two exponential solutions. Apply the first assertion in both orders for two normalized solutions.
\end{proof}

\section{Subsolutions and the Gauduchon trace}
\label{sec:big-minimal-estimates}

The next construction preserves a reference potential up to a bounded term. Its positive-current formula explains why the reference form itself need not be semipositive.

\begin{lemma}\label{lem:big-reference-subsolution}
Fix $p>1$ and $L>0$. There is $m>0$ such that, whenever
\[
 \rho\leq\eta\leq0,\quad\eta\in\PSH(X,\theta),
 \qquad g\geq0,\quad\|g\|_{L^p(\mathrm{d}V)}\leq L,
\]
there exists $v\in\PSH(X,\theta)$ with
\[
 \eta\leq v\leq\eta+1,\qquad
 \mu_v\geq m g\,\mathrm{d}V.
\]
The constant depends only on the fixed geometry, $\rho,p,L$.
\end{lemma}
\begin{proof}
Choose $1<q<p$. The functions $h=g(2-\rho)^{2n}$ have uniformly bounded $L^q$ norms, by H\"older's inequality and the finite polynomial moments of a fixed quasi-plurisubharmonic function. Apply \cref{lem:big-lp-subsolution} with the Hermitian background $\omega$. It gives $-1\leq s\leq0$, $s\in\PSH(X,\omega)$, and
\[
 \omega_s^n\geq m h\,\mathrm{d}V
\]
for a fixed $m>0$. Put $u_1=\rho+s$. Then $\theta_{u_1}\geq\omega_s$. On $\Omega$ define
\[
 t=1+\eta-u_1,\qquad v=\eta+t^{-1}.
\]
Here $1\leq t\leq2-\rho$. The bounded local chain rule gives
\[
 \theta_v=(1-t^{-2})\theta_\eta+t^{-2}\theta_{u_1}
       +2t^{-3}\,\mathrm{d}(\eta-u_1)\wedge\dc(\eta-u_1)
 \geq t^{-2}\theta_{u_1}.
\]
All coefficients in the first two terms are nonnegative and sum to one. This proves local positivity without a sign assumption on $\theta$. The calculation for locally bounded quasi-plurisubharmonic functions follows by local regularization and the bounded chain rule, or equivalently its usual energy-current formulation.

Since $\eta\leq v\leq\eta+1$, the function $v$ is locally bounded above near $Z$. The removable-singularity theorem for quasi-plurisubharmonic functions extends it canonically to $X$, retaining $\theta_v\geq0$. To check the exact smooth lower bound, first enlarge it by an arbitrary positive constant-coefficient error on a small ball, extend the resulting plurisubharmonic function across $Z$, and let that error tend to zero. The two bounds by $\eta$ and $\eta+1$ extend as well. On $\Omega$, positivity of the local products gives
\[
 \mu_v\geq t^{-2n}\theta_{u_1}^n
       \geq(2-\rho)^{-2n}\omega_s^n
       \geq m g\,\mathrm{d}V.
\]
Both sides give zero mass to $Z$, proving the global inequality.
\end{proof}

\begin{proposition}\label{prop:big-singular-gauduchon-trace}
Let $\gamma$ be Gauduchon, write $\gamma^n=G\,\mathrm{d}V$, and put
\[
 T_\gamma=\int_X\theta\wedge\gamma^{n-1}>0.
\]
If $u\geq\rho-C$ is $\theta$-plurisubharmonic and $\mu_u\geq F\,\mathrm{d}V$, $F\geq0$, then
\begin{equation}\label{eq:big-singular-gauduchon-trace}
 \int_X F^{1/n}G^{1-1/n}\,\mathrm{d}V\leq T_\gamma.
\end{equation}
Consequently, for a fixed nonzero $0\leq f\in L^p(\mathrm{d}V)$, $p>1$, solutions above this barrier of
$\mu_u=\mathrm{e}^{\lambda u}f\,\mathrm{d}V$ have uniformly bounded suprema when $\lambda>0$ is fixed. If instead
\[
 \sup_Xv_j=0,\qquad
 \mu_{v_j}=c_j \mathrm{e}^{v_j/j}f\,\mathrm{d}V,
 \qquad v_j\geq\rho-C_j,
\]
with $c_j>0$, then the constants $c_j$ are uniformly bounded above.
\end{proposition}
\begin{proof}
The linear current $\theta_u\wedge\gamma^{n-1}$ is positive and globally defined, even at $Z$. Distributional Stokes gives
\[
 \int_X\theta_u\wedge\gamma^{n-1}
 =\int_X\theta\wedge\gamma^{n-1},
\]
since $\ddc\gamma^{n-1}=0$. Applying the identity to $\rho$ proves $T_\gamma>0$.

On $\Omega$ the local mixed inequality gives
\[
 \theta_u\wedge\gamma^{n-1}\geq
 F^{1/n}G^{1-1/n}\,\mathrm{d}V.
\]
Here is the justification for the two possibly nonclosed backgrounds. Freeze each smooth form at the center of a small coordinate ball, and add a constant-coefficient error $\varepsilon\ddc|z|^2$ that dominates its variation. Add the corresponding quadratic potentials to $u$ and to $0$, respectively. Their ordinary positive Hessians dominate $\theta_u$ and $\gamma$, so their top powers dominate $F\,\mathrm{d}V$ and $G\,\mathrm{d}V$. The classical local mixed inequality \cite[Theorem 1.2]{Dinew09} applies. Its mixed product is bounded above by the product formed from $\theta_u+2\varepsilon\ddc|z|^2$ and $\gamma+2\varepsilon\ddc|z|^2$. Covering a compact subset of $\Omega$ and then letting $\varepsilon\downarrow0$ proves the displayed inequality there. Exhaust $\Omega$ and use positivity of the global trace measure. The complement has zero smooth volume, giving \eqref{eq:big-singular-gauduchon-trace}.

For the exponential assertion write $a=\sup_Xu$ and $w=u-a$. The estimate becomes
\[
 \mathrm{e}^{\lambda a/n}\int_X\mathrm{e}^{\lambda w/n}f^{1/n}G^{1-1/n}\,\mathrm{d}V
 \leq T_\gamma.
\]
The integral has a positive lower bound over all normalized $\theta$-plurisubharmonic $w$. Otherwise normalized compactness supplies a subsequence converging almost everywhere to a genuine potential, and dominated convergence gives a strictly positive limit integral, a contradiction. We used $w\leq0$ and the integrability of $f^{1/n}$. This bounds $a$ above.

For the last assertion the same estimate contains $c_j^{1/n}$ and $\mathrm{e}^{v_j/(jn)}$. If those integrals approached zero along a subsequence with $j\to\infty$, normalized compactness and almost-everywhere convergence would give $v_j/j\to0$ almost everywhere. Dominated convergence then gives the positive limit $\int_Xf^{1/n}G^{1-1/n}\,\mathrm{d}V$. This contradiction bounds $c_j$; finitely many remaining indices do not matter. No total top-degree mass was used in either argument.
\end{proof}

```

## section_big_reference_stability_holder.tex
```latex
\section{Stability above a strict barrier}
\label{sec:big-reference-stability}

Retain the arbitrary smooth big background $\theta$, the strict potential
$\rho\leq0$, and $\Omega=X\setminus\{\rho=-\infty\}$ from
\cref{sec:big-minimal-comparison}. The same auxiliary-subsolution argument
as in \cref{sec:bounded-stability} applies to a reference which is itself
unbounded. The reference-preserving construction and the domination
principle above replace their bounded counterparts. This reconstructs
\cite[Theorem~3.3 and Remark~3.4]{Dang26} in the minimal case, with the
normalization of the comparison potential explicit.

\begin{theorem}\label{thm:big-reference-one-sided-stability}
Fix $C_0,L>0$, $p>1$, and
\[
 0<\gamma<\frac{p-1}{np+p-1}.
\]
Let $\eta\in\PSH(X,\theta)$ satisfy $\rho\leq\eta\leq0$. Suppose
$u\in\PSH(X,\theta)$ satisfies
\[
 \eta-C_0\leq u\leq\eta,\qquad
 \mu_u=f\,\mathrm{d}V,\qquad 0\leq f\in L^p(\mathrm{d}V),
 \quad\|f\|_p\leq L.
\]
There is a constant $C$, depending only on the fixed geometry,
$\rho,C_0,L,p,\gamma$, such that every $v\in\PSH(X,\theta)$ with
$v\leq\eta$ satisfies
\begin{equation}\label{eq:big-reference-stability}
 \sup_\Omega(v-u)_+
 \leq C\left(\int_\Omega(v-u)_+\,\mathrm{d}V\right)^\gamma.
\end{equation}
The constant is independent of $\eta$ in the stated range. The comparison
potential $v$ need not have the ordinary singularity type of $\eta$.
\end{theorem}

Differences in this statement are taken on $\Omega$, where $u$ and $\eta$
are locally bounded; their integrals are unchanged by extending them by
zero on the analytic complement. The bound also means the corresponding
order inequality for the canonical potentials on all of $X$.

\begin{proof}
Replace $v$ by $\max(v,u)$, so that
$\eta-C_0\leq u\leq v\leq\eta$ and $0\leq v-u\leq C_0$ on $\Omega$.
Fix $q\in(1,p)$ and $\delta>0$, and put
\[
 E_\delta=\{u<v-\delta\}\cap\Omega,\qquad
 g_\delta=\mathbf1_{E_\delta}f,\qquad m_\delta=\|g_\delta\|_q.
\]
When $m_\delta>0$, \cref{lem:big-reference-subsolution}, followed by
subtracting one from its potential, gives $h\in\PSH(X,\theta)$ and a
fixed $b>0$ such that
\[
 \eta-1\leq h\leq\eta,\qquad
 \mu_h\geq b\,g_\delta/m_\delta\,\mathrm{d}V.
\]
The constant is uniform in $\eta$ because the auxiliary density has
$L^q$ norm one and the strict barrier is fixed.

If $0<m_\delta<b/2$, set
\[
 t=(2m_\delta/b)^{1/n},\qquad
 w=(1-t)v+th-\delta-C_0t.
\]
Since $h-v\leq C_0$, the set $\{u<w\}\cap\Omega$ is contained in
$E_\delta$. On this set the local positive-product expansion gives
$\mu_w\geq t^n\mu_h\geq2\mu_u$. Both potentials are bounded below
by $\rho$ minus a constant, and $w\leq u+C_0$. Thus
\cref{thm:big-barrier-domination} applies and gives $u\geq w$. It follows
that
\[
 v-u\leq\delta+C_0t+t(v-h)\leq\delta+(C_0+1)t.
\]
If $m_\delta=0$, apply the same domination theorem with coefficient zero
to $u$ and $v-\delta$. If $m_\delta\geq b/2$, use $v-u\leq C_0$.
In all cases,
\[
 \sup_\Omega(v-u)\leq\delta+C_1m_\delta^{1/n}.
\]
Write $I=\int_\Omega(v-u)\,\mathrm{d}V$. For $I=0$, the canonical
potentials agree; otherwise H\"older and Chebyshev give
\[
 m_\delta\leq L(I/\delta)^{(p-q)/(pq)}.
\]
For $0<I\leq1$, choosing
$\delta=I^{(p-q)/(npq+p-q)}$ yields the exponent
$\gamma_q=(p-q)/(npq+p-q)$. Choose $q>1$ close enough to one that
$\gamma_q>\gamma$. The case $I>1$ follows from the bound by $C_0$.
This proves \eqref{eq:big-reference-stability}.
\end{proof}

\begin{corollary}\label{cor:big-reference-uniform-convergence}
Fix $\rho\leq\eta\leq0$, $C_0,L>0$, and $p>1$. Consider the potentials
$u\in\PSH(X,\theta)$ satisfying
\[
 \eta-C_0\leq u\leq\eta,\qquad
 \mu_u=f_u\,\mathrm{d}V,\qquad0\leq f_u\in L^p(\mathrm{d}V),
 \quad\|f_u\|_p\leq L.
\]
This family is compact for uniform convergence of differences on $\Omega$.
If $u_j\to u$ in $L^1$, then $u$ belongs to the same family and
\[
 \sup_\Omega|u_j-u|\leq C\|u_j-u\|_{L^1(\mathrm{d}V)}^\gamma
 \longrightarrow0
\]
for every exponent in \cref{thm:big-reference-one-sided-stability}.
Moreover $f_{u_j}$ converges weakly to $f_u$ in $L^p$.
\end{corollary}
\begin{proof}
Apply the theorem in both orders to $u_j,u_k$, with the common reference
$\eta$. It follows that an $L^1$-Cauchy sequence is uniformly Cauchy in
differences on $\Omega$. The uniform limit there is locally
$\theta$-plurisubharmonic and agrees almost everywhere, hence everywhere
in canonical representatives, with the $L^1$ limit $u$. The bounds
$\eta-C_0\leq u\leq\eta$ hold on all of $X$. Letting $k\to\infty$ in
the pairwise estimate proves the displayed quantitative bound, before
using any equation for $u$.

The densities form a bounded set in the reflexive space $L^p$. For a
weakly convergent subsequence, say $f_{u_{j_k}}\rightharpoonup f$, local
uniform convergence of the bounded potentials gives
$\mu_u=f\,\mathrm{d}V$ on $\Omega$, by Bedford--Taylor continuity for
the smooth nonclosed background. Both measures give zero mass to the
analytic complement, so this equality holds on $X$. Positivity and
weak lower semicontinuity give $f\geq0$ and $\|f\|_p\leq L$.
Every weak cluster point is therefore the same density $f_u$, proving
weak convergence of the whole sequence. Finally, the common bounds by
$\eta$ and $\eta-C_0$ give $L^1$ compactness by quasi-plurisubharmonic
compactness. The preceding argument upgrades each convergent subsequence
to uniform convergence in the stated family.
\end{proof}

For a normalized solution with minimal singularities, take
$\eta=V_\theta$. Every normalized comparison potential lies below this
reference. The compactness assertion uses a common reference and a
uniform $L^p$ density bound; it makes no claim from weak convergence of
arbitrary non-pluripolar measures. No metric mass property is imposed.

\section{Local H\"older continuity in a big background}
\label{sec:big-minimal-holder}

We now reconstruct the local H\"older conclusion of
\cite[Theorem~A]{Dang26}. Two points require attention when passing from
\cref{sec:holder-from-stability}: the solution can be unbounded on $X$,
and the smooth lower bound for its Hessian need not be closed. We retain
Demailly's classical local regularization expansion and explain the
quantitative estimate used here.

\begin{lemma}\label{lem:smooth-background-regularization-rate}
Let $a$ be quasi-plurisubharmonic on $X$, with $\sup_Xa=0$ and
$\theta+\ddc a\geq0$, and suppose that $a$ is locally bounded on $\Omega$.
There are constants $A,K,C>0$ such that the averaging operators $R_t$
from \cref{lem:chern-kiselman-input} satisfy
\[
 R_ta+Kt^2\downarrow a,\qquad
 \|R_ta-a\|_{L^1(\mathrm{d}V)}\leq Ct^2.
\]
For small $\delta>0$ and $c>0$, the transform on $\Omega$
\[
 \Phi_{c,\delta}
 =\inf_{0<t\leq\delta}
 \{R_ta+K(t^2-\delta^2)+K(t-\delta)-c\log(t/\delta)\}
\]
extends canonically to $X$ and satisfies
\begin{equation}\label{eq:smooth-background-transform-rate}
 a-K(\delta^2+\delta)\leq\Phi_{c,\delta}\leq R_\delta a\leq0,
 \qquad \theta+\ddc\Phi_{c,\delta}\geq-(Ac+C\delta)\omega.
\end{equation}
At each point of $\Omega$ the infimum is attained at a positive radius.
On every compact $K_1\Subset\Omega$, for sufficiently small $t$,
$\|\nabla R_ta\|_{K_1}\leq C_{K_1}/t$.
\end{lemma}

\begin{proof}
Apply \cite[Theorem~4.1]{Dem94} to the closed current $\ddc a$ and the
smooth lower bound $-\theta$. It gives monotonicity and logarithmic
convexity, with
$\lambda(x,t)=t\partial_t(R_ta+K_0t^2)\geq0$ increasing in $t$.
We first justify a linear error for this smooth lower bound, rather than
infer a rate from the unspecified modulus in that theorem.

Choose the auxiliary curvature form to be $A\omega$, with $A$ large
enough that the Chern curvature plus $A\omega\otimes\operatorname{Id}$
is nonnegative on every decomposable tensor. Equivalently, after
absorbing the normalization constants, its coefficients satisfy
\[
 \sum R_{j\bar k\ell\bar m}\xi_j\bar\xi_k\zeta_\ell\bar\zeta_m
 \geq-A|\xi|^2|\zeta|^2.
\]
This choice is available by compactness. Pairing this inequality with
the nonnegative eigenvalues of a positive complex Hessian bounds its
curvature contraction by $-A$ times its trace. Hence the algebraic inequality used in
\cite[Lemma~4.4]{Dem94} holds with no small $\epsilon$ term and no
$M_\epsilon$ correction.

Fix $x$ and $t=|w|$. In a uniformly sized coordinate chart about $x$,
write $\beta=\ddc|z|^2$ and
choose a quadratic $q_{x,t}$ with
\[
 \ddc q_{x,t}=\theta(x)+Bt\beta,
\]
where $B$ is fixed and large enough that $a+q_{x,t}$ is plurisubharmonic
on a ball containing the averaging support and its nearby base points.
This follows from the smooth variation bound
$\|\theta(y)-\theta(x)\|\leq C|y-x|$ on that ball of radius $O(t)$.
For the Hessian calculation at $(x,w)$ the quadratic is held fixed.
Its coefficients and all needed derivatives are uniformly bounded.

Here are the error estimates in the classical expansion
\cite[Proposition~3.8, equations (3.11), (4.3), and (4.5)]{Dem94}.
Normalized quasi-plurisubharmonic compactness bounds $\|a\|_1$.
On each fixed larger chart, add one fixed strictly plurisubharmonic
quadratic $Q$ to $a$. If
$\nu=\ddc(a+Q)\wedge\beta^{n-1}$, the local Lelong mass inequality and
a fixed larger-ball mass bound give
$\nu(B_t(x))\leq Ct^{2n-2}$. The coefficients of
$\partial\bar\partial(a+q_{x,t})$ are controlled in total variation
by those of $\ddc(a+Q)$ plus a uniformly bounded smooth form. Scaling
therefore gives, uniformly in $x$ and $t$,

\[
 \int_{|\zeta|<1}|\partial\bar\partial(a+q_{x,t})|
       (\operatorname{exph}_x(t\zeta))\,\mathrm{d}\zeta
 \leq Ct^{-2}.
\]
The integral is understood as the pullback of coefficient measures for
nonsmooth $a$. Thus the terms with a coefficient $O(t^3)$ contribute
$O(t)$; the order-two expansion has an $O(t)$ remainder as well.
The mixed and vertical contributions have bounds
$C(|\xi||\tau|+|\tau|^2)$. The curvature term is bounded below by
$-A\lambda(x,t)|\xi|^2$, using the preceding curvature choice.
Equation (4.5) identifies its radial mass with $\lambda$ up to $O(t^2)$.
Subtracting the regularization of $q_{x,t}$ restores $-\theta(x)$;
its base Hessian differs from $\ddc q_{x,t}$ by $O(t)$, its mixed and
vertical Hessians are bounded, and its radial logarithmic derivative
is $O(t^2)$. The extra $Bt\beta$ also costs only $O(t)$.
Consequently the full base--fiber Hessian satisfies
\[
 \ddc_{x,w}R_{|w|}a[\xi,\tau]^2
 \geq-\theta_x[\xi]^2-(A\lambda(x,t)+Ct)|\xi|^2
       -K_1(|\xi||\tau|+|\tau|^2).
\]
All constants are independent of $x,t,c,\delta$ and uniform in the
normalized family. In particular, setting $\xi=0$ in the same local
expansion gives a uniform lower bound for the fiber Hessian. Adding a
fixed multiple of $|w|^2$ gives its subharmonicity, hence the
logarithmic convexity and monotonicity above with a uniform $K_0$.

Increase $K\geq K_0$ and add $K(t^2+t)$ to the regularization. The
positive vertical Hessian of $K|w|$ absorbs the mixed term by
\[
 K_1|\xi||\tau|\leq C't|\xi|^2+\frac{K}{8t}|\tau|^2,
\]
and absorbs the remaining bounded vertical error for small $t$.
The logarithmic derivative of the corrected function is at least
$\lambda$. The capped Kiselman minimum argument in
\cref{lem:general-kiselman-modulus} therefore gives the last inequality
in \eqref{eq:smooth-background-transform-rate}, now with error $C\delta$.
On compact subsets of $\Omega$, local boundedness of $a$ makes the
logarithmic penalty diverge uniformly at zero, so that the minimum
occurs away from zero. The same argument handles minimizers at the
upper cap without differentiating their radius.

The other bounds in \eqref{eq:smooth-background-transform-rate} follow
from monotonicity and evaluation at $t=\delta$. In particular the
transform is bounded above near the analytic complement. The removable
singularity theorem extends it, preserving the exact smooth lower
Hessian bound by local freezing and passage to the limit. Its lower
bound by $a-K(\delta^2+\delta)$ also extends by canonical representatives.

The adjoint computation in \cref{lem:chern-smoothing-integral} gives
$R_t^*1=1+O(t^2)$. It needs only $a\in L^1$, since
\[
 \left|\int_X(R_ta-a)\,\mathrm{d}V\right|
 \leq Ct^2\|a\|_1.
\]
Together with $R_ta-a\geq-Kt^2$, this proves the stated $L^1$ estimate.
Finally the smoothing kernel near $K_1$ samples a fixed larger compact
subset of $\Omega$, where $a$ is bounded. The same kernel derivative
estimate as in \cref{lem:chern-smoothing-integral} gives $C_{K_1}/t$.
\end{proof}

\begin{theorem}\label{thm:big-minimal-holder}
Let $u\in\PSH(X,\theta)$ satisfy
\[
 \sup_Xu=0,\qquad V_\theta-C_0\leq u\leq V_\theta,
 \qquad\mu_u=f\,\mathrm{d}V,
 \quad0\leq f\in L^p(\mathrm{d}V),\quad p>1.
\]
Then $u$ is locally H\"older continuous on $\Omega$, with every exponent
\[
 0<\beta<\frac{2(p-1)}{np+3(p-1)}.
\]
For a fixed bound on $C_0$ and $\|f\|_p$, the constants are uniform on
each fixed compact subset of $\Omega$.
\end{theorem}

\begin{proof}
Subtract a constant from the strict barrier so that $\rho\leq u-1$.
It still satisfies $\theta+\ddc\rho\geq\kappa\omega$ for a fixed
$\kappa>0$. Choose
$0<\gamma<(p-1)/(np+p-1)$ and write $\alpha=2\gamma<1$.
For small $\delta$ set
\[
 c=\delta^\alpha,\qquad e=Ac+C\delta,\qquad s=e/\kappa,
 \qquad v_\delta=\frac{\Phi_{c,\delta}+s\rho}{1+s}.
\]
The preceding lemma gives $v_\delta\in\PSH(X,\theta)$. Its lower bound
for $\Phi_{c,\delta}$ implies $\rho\leq\Phi_{c,\delta}$ when $\delta$
is small. Thus
\[
 v_\delta\leq\Phi_{c,\delta}\leq R_\delta u\leq0.
\]
Apply \cref{thm:big-reference-one-sided-stability} with reference
$V_\theta$ and comparison $v_\delta$. The $L^1$ smoothing estimate gives
\[
 \sup_\Omega(v_\delta-u)_+
 \leq C\|(R_\delta u-u)_+\|_1^\gamma\leq C\delta^\alpha.
\]
Fix a compact subset on which $\rho\geq-M$. Since $s\leq C\delta^\alpha$
and $u\leq0$, the identity
\[
 \Phi_{c,\delta}-u=(1+s)(v_\delta-u)+s(u-\rho)
\]
gives $\Phi_{c,\delta}-u\leq C_M\delta^\alpha$ there.

At a minimizing radius $t$ the lower monotone bound yields
\[
 -c\log(t/\delta)\leq\Phi_{c,\delta}-u+K(\delta^2+\delta)
 \leq C_Mc.
\]
Hence $t\geq a_M\delta$ for a fixed $a_M>0$. As in the proof of
\cref{thm:hermitian-holder-elementary}, monotonicity now gives
\[
 R_{a_M\delta}u-u\leq C_M\delta^\alpha,
 \qquad R_{a_M\delta}u-u\geq-K(a_M\delta)^2.
\]
The constants are uniform on the chosen compact subset. Apply this to a
slightly larger compact neighborhood, where also
$\|\nabla R_tu\|\leq C_M/t$. For nearby points at distance $d$, smooth
approximation and a short path in that neighborhood give
\[
 |u(x)-u(y)|\leq C_M(t^\alpha+d/t).
\]
Take $t=d^{1/(1+\alpha)}$. This gives exponent
$\alpha/(1+\alpha)$; letting $\gamma$ approach its upper endpoint gives
the asserted range. Boundedness on the compact neighborhood handles
pairs farther apart.
\end{proof}

The density condition in this theorem is global. Smoothness of $f$ only
on $\Omega$ does not provide that hypothesis. The theorem gives no
continuity assertion across the pole set and does not assert the same
regularity for an arbitrary prescribed ordinary singularity type.

```
