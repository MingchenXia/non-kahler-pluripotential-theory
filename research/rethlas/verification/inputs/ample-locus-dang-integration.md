Run_id: ample_locus_dang_integration_01

Statement: Audit the full logical chain integrating the supplied smoothness-on-the-ample-locus theorem and Dang26 Theorem 3.1. All submitted text is below. The compact Hermitian background theta may be nonclosed until the final compact Kahler / closed big class application. No metric mass assumption is imposed for the regularity arguments. Confirm the main theorem for arbitrary big, not necessarily nef, classes; all local/global measure transitions; and the complete Holder-to-smooth bootstrap.

Accepted classical inputs (verify their applicability): Bedford–Taylor local products, mixed inequalities and bounded-envelope contact; local elliptic/ABP/Evans–Krylov/Schauder theory; the smooth Hermitian Dirichlet subsolution theorem; Demailly94 Chern regularization expansion (not an unquantified error substituted for a rate); and BEGZ10 Theorems A/3.1 and B/4.1 for classical full-mass existence/uniqueness/minimal singularities. The chapter's internal non-Kahler-locus theorem provides one strict current with analytic singularities and smooth remainder whose pole set is exactly E_nK. These classical/locus inputs need not be reproved here. The internal Hermitian bounded Lp subsolution lemma used in the supplied reference-preserving construction is accepted; its assertion is that for any nonnegative Lq density of norm bounded by L, q>1, there is -1<=s<=0 in PSH(X,omega) and a uniformly positive m with omega_s^n>=m h dV. Elementary qpsh polynomial moments, canonical representatives, compactness and removable singularities may be used.

Do NOT take Dang's regularity or the submitted interior-smoothness theorem as black boxes: review their provided proofs. In particular audit the smooth-nonclosed curvature-error rate, unbounded L1 smoothing estimate, normalized comparison potential, strict-barrier correction, positive minimizing radius and local Holder interpolation. Check every step of the proper-gap, exact Dirichlet approximation, polynomial boundary trace, subpower localization, gradient interpolation, polynomial Calabi estimate, trace recovery and strong-to-viscosity bootstrap. Earlier focused checks were correct, but this requested review concerns the full assembled chain. The source statement with density smooth only on Omega cannot invoke Dang absent global Lp or an independently known Holder premise; the integrated theorem retains that premise and the main global-volume application discharges it. Dimension one and dd^c=i/(2pi) conventions must remain valid. There is no novelty claim or claim of complete certification of the whole book.

Use the normal local verification instructions and tools. Write only new records for this run; never edit book sources, original references, old verifier records or installation. Finish by saving the normal verification.json report. If a defect is found, continue to review the rest under an explicit corrected premise so the report identifies the full boundary.

Proof:
## book/author/section_ample_locus_smoothness.tex
```latex
\subsection{Smooth equations on the ample locus}
\label{sec:ample-locus-smoothness}

For a big class $\alpha$, write
\[
 \operatorname{Amp}(\alpha)=X\setminus E_{\mathrm{nK}}(\alpha).
\]
By \cref{thm:bc-non-kahler-locus}, this is the locus on which a strict
current with analytic singularities can be smooth. We now assume that
$X$ is K\"ahler. The interior estimates of
\cref{sec:nonclosed-interior-smoothness} give the following application
to an arbitrary big class. The class is not required to be nef.

\begin{theorem}\label{thm:big-class-ample-smoothness}
Let $X$ be a compact K\"ahler manifold, let $\alpha$ be a big real
$(1,1)$-class, and let $\theta$ be a smooth closed representative.
Let $\mu$ be a smooth positive volume form with
$\mu(X)=\operatorname{vol}(\alpha)$. The normalized full-mass solution
$\varphi\in\mathcal E(X,\theta)$ of
\begin{equation}\label{eq:big-class-smooth-volume}
 \bigl\langle(\theta+\ddc\varphi)^n\bigr\rangle=\mu,
 \qquad \sup_X\varphi=0,
\end{equation}
is smooth on $\operatorname{Amp}(\alpha)$. The restriction of
$\theta+\ddc\varphi$ to this locus is a K\"ahler form.
\end{theorem}

Here $\mathcal E(X,\theta)$ is the classical full-mass class:
$\int_X\langle(\theta+\ddc u)^n\rangle=\operatorname{vol}(\alpha)$.
Existence and uniqueness in this statement are the classical theorem
\cite[Theorem~A, equivalently Theorem~3.1]{BEGZ10}.
The nef case of the smoothness conclusion is
\cite[Theorem~C]{BEGZ10}; the following proof uses no nefness.

\begin{proof}
Fix a K\"ahler form $\omega$ and put $f=\mu/\omega^n$.
Compactness and smoothness give $f\in L^p(X,\omega^n)$ for every
finite $p>1$. The minimal-singularity estimate
\cite[Theorem~B, quantitatively Theorem~4.1]{BEGZ10} yields
\begin{equation}\label{eq:ample-solution-minimal-bounds}
 V_\theta-C\leq\varphi\leq V_\theta,
 \qquad
 V_\theta=\left(\sup\{v\in\PSH(X,\theta):v\leq0\}\right)^*.
\end{equation}
The upper bound follows from the normalization.

Choose the strict analytic current of \cref{thm:bc-non-kahler-locus}.
Since its Bott--Chern class is $\alpha$, it has the form
\[
 T=\theta+\ddc\rho\geq\varepsilon\omega,
 \qquad \varepsilon>0,
 \qquad \{\rho=-\infty\}=E_{\mathrm{nK}}(\alpha),
\]
where $\rho$ has analytic singularities with smooth remainder.
Thus $\rho$ is smooth on
$\Omega=\operatorname{Amp}(\alpha)$. Subtract a constant so that
$\rho\leq0$, hence $\rho\leq V_\theta$. By
\eqref{eq:ample-solution-minimal-bounds},
\[
 \rho-C\leq\varphi\leq0.
\]
Consequently $\varphi$ is locally bounded on $\Omega$.
On each relatively compact coordinate ball there, the truncations
which define the non-pluripolar product agree with $\varphi$ for all
sufficiently deep levels. Locality therefore identifies
\eqref{eq:big-class-smooth-volume} with the bounded-potential equation
\[
 (\theta+\ddc\varphi)^n=f\,\omega^n\quad\text{on }\Omega.
\]

Apply \cref{thm:big-minimal-holder}, the reconstructed local H\"older
result of \cite[Theorem~3.1]{Dang26}. Its hypotheses hold for this strict
barrier: the density is globally in $L^p$, and the solution has the
minimal bounds \eqref{eq:ample-solution-minimal-bounds}.
We obtain local H\"older continuity on all of $\Omega$.
\Cref{thm:nonclosed-interior-smoothness} now gives
$\varphi\in C^\infty(\Omega)$, since $f$ is smooth and strictly positive
there. The current $\theta+\ddc\varphi$ is a smooth semipositive form
on $\Omega$ with positive determinant $f\,\omega^n$, so every eigenvalue
is positive. It is closed because $\theta$ is closed. Hence it is a
K\"ahler form on $\Omega$.
\end{proof}

The proof of the H\"older input is given in
\cref{sec:big-reference-stability,sec:big-minimal-holder}, and the local
derivative estimates are proved in \cref{sec:nonclosed-interior-smoothness}.
The global $L^p$ hypothesis is automatic for the volume form in this
theorem. It cannot be replaced in that proof by smoothness only on the
ample locus. No extension of the metric across $E_{\mathrm{nK}}(\alpha)$
or completeness on its complement is asserted.

```

## book/author/section_big_minimal_comparison.tex
```latex
\section{Comparison above a strict singular barrier}
\label{sec:big-minimal-comparison}

Let $\theta$ be an arbitrary smooth big real $(1,1)$-form. Neither semipositivity nor closedness is assumed. There is no bounded mass or uniform positive lower volume hypothesis. Fix a Hermitian form $\omega$ and a strict potential
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

## book/author/section_big_reference_stability.tex
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

\Needspace{15\baselineskip}
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

```

## book/author/section_big_minimal_holder.tex
```latex
\section{Local H\"older continuity in a big background}
\label{sec:big-minimal-holder}

We now reconstruct the local H\"older conclusion of
\cite[Theorem~A and Theorem~3.1]{Dang26}. Two points require attention when passing from
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

The strict potential $\rho$ and the open set $\Omega$ are fixed as in
\cref{sec:big-minimal-comparison}; the background $\theta$ may be nonclosed.
The preceding regularization lemma and
\cref{thm:big-reference-one-sided-stability} prove Dang's local
H\"older conclusion with an explicit, nonoptimal exponent.

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

The formulation with a scalar and an equation only on $\Omega$, used in
\cite[Theorem~3.1]{Dang26}, follows as well. Suppose
$\mu_u=cf\,\mathrm{d}V$ on $\Omega$, where $c>0$ and
$0\leq f\in L^p(X,\mathrm{d}V)$, and retain the same minimal bounds.
The lower bound $u\geq V_\theta-C_0\geq\rho-C_0$ makes $u$ locally
bounded on $\Omega$, so its bounded-potential product is $\mu_u$ there.
The analytic complement has zero smooth volume and zero non-pluripolar
mass. Thus the equation holds on $X$, and the theorem applies with
$cf$ in place of $f$. For uniform estimates the density bound is
$\|cf\|_p$, including the scalar.

The proof does not require a recent regularity theorem as an additional
input: the reference-preserving subsolution is constructed in
\cref{lem:big-reference-subsolution}, its comparison step is
\cref{thm:big-barrier-domination}, and the stability and regularization
arguments above supply the H\"older estimate.

The density condition in this theorem is global. Smoothness of $f$ only
on $\Omega$ does not provide that hypothesis. The theorem gives no
continuity assertion across the pole set and does not assert the same
regularity for an arbitrary prescribed ordinary singularity type.

\subsection{Limits of normalized exponential solutions}

The fixed-reference compactness theorem also describes the approximation
used to construct the zero-exponent equation. It controls differences of
potentials uniformly on $\Omega$, even when the potentials themselves
are unbounded near its complement.

\Needspace{21\baselineskip}
\begin{proposition}\label{prop:big-exponential-clusters}
For the family $(v_\lambda,c_\lambda)$ of
\cref{lem:big-exponential-uniform-type}, the normalized potentials
are relatively compact for uniform convergence of
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
\Cref{lem:big-exponential-uniform-type} gives a common reference interval,
and the densities are bounded in $L^p$ by $C\|f\|_p$. Apply
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
bounds for every $\alpha$ below its endpoint. Their uniform limit
inherits those bounds by pointwise convergence. For
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

## book/author/section_nonclosed_interior_smoothness.tex
```latex
% Book adaptation of the supplied nonclosed regularity manuscript.
% Review scope: research/editorial/nonclosed-interior-regularity-review.md.
\section{Interior smoothness on the regular locus}
\label{sec:nonclosed-interior-smoothness}

The existence theorem above concerns the minimal ordinary singularity
type of an arbitrary smooth big background. We now study local
smoothness where the density is smooth and positive. The argument below
assumes local H\"older continuity of the solution. It uses a strict
singular barrier to select a point of the nonregular set and then derives
local derivative estimates for the original background. Neither bounded
mass nor positive lower mass is imposed.

Let $\rho\in\PSH(X,\theta)$ have analytic singularities with smooth
remainder and satisfy
\begin{equation}\label{eq:interior-strict-reference}
 \theta+\ddc\rho\geq\varepsilon\omega_X,
 \qquad \varepsilon>0.
\end{equation}
Write $\Omega=\{\rho>-\infty\}$ and retain the minimal envelope $V_\theta$
from \cref{sec:big-minimal-existence}.

\begin{theorem}\label{thm:nonclosed-interior-smoothness}
Suppose $\varphi\in\PSH(X,\theta)$ has minimal singularities, is locally
H\"older continuous on $\Omega$, and satisfies
\[
 (\theta+\ddc\varphi)^n=cf\,\omega_X^n\quad\text{on }\Omega,
 \qquad c>0,
\]
where $f$ is smooth and strictly positive on $\Omega$. Then
$\varphi\in C^\infty(\Omega)$ and $\theta+\ddc\varphi>0$ there.
\end{theorem}

Subtracting a constant, we may assume $\sup_X\varphi=0$, hence
$V_\theta-C\leq\varphi\leq V_\theta$.
A sufficient condition for the H\"older premise is $0\leq f\in L^p(X,\omega_X^n)$ for some $p>1$, by \cref{thm:big-minimal-holder}. Smoothness of $f$ only on $\Omega$ does not imply its global $L^p$ integrability. The argument below retains local H\"older continuity as an explicit premise, so it also applies when that continuity is known by another argument.

All coordinate balls have compact closure in a larger chart. We use
$\beta=\ddc|z|^2$ with the book's convention
$\ddc=\mathrm{i}\partial\bar\partial/(2\pi)$. Matrix coefficients are
taken relative to $\beta$. Constants absorb this normalization; when an
approximation index or an ellipticity bound varies, their independence
is stated explicitly.

\Needspace{15\baselineskip}
\subsection{The proper barrier}\label{sec:interior-proper}

The singularity type supplies the global compactness needed for the final localization.

\begin{lemma}\label{lem:interior-proper-gap}
After adding a constant to $\rho$, one may assume $\rho\leq0$. Then $\varphi-\rho$ is continuous, bounded below, and proper on $\Omega$, in the sense that all its sublevel sets are compact in $\Omega$.
\end{lemma}

\begin{proof}
Choose $M\geq0$ with $\theta\geq-M\omega_X$. If $a\in(0,1)$ is sufficiently close to one, then
\[
  \theta+\ddc(a\rho)
  =a(\theta+\ddc\rho)+(1-a)\theta
  \geq\bigl(a\varepsilon-(1-a)M\bigr)\omega_X>0.
\]
Thus $a\rho$ is an admissible competitor for $V_\theta$. Minimal singularities and the normalization give
\[
  0\geq\varphi\geq V_\theta-C\geq a\rho-C,
\]
and hence
\begin{equation}\label{eq:interior-gap-proper}
  \varphi-\rho\geq(1-a)(-\rho)-C.
\end{equation}
The assumed local H\"older continuity makes $\varphi$ continuous on $\Omega$; $\rho$ is smooth there because it has analytic singularities. Hence $\varphi-\rho$ is continuous. Since $\rho\to-\infty$ when approaching $X\setminus\Omega$, \eqref{eq:interior-gap-proper} places every sublevel set in a compact superlevel set of $\rho$. The sublevel set is closed in $\Omega$, so it is compact there.
\end{proof}

\subsection{Local bounded-potential calculus}\label{sec:interior-calculus}

Let $U\subset\mathbb C^n$ be open. If $T=\vartheta+\ddc u\geq0$, where $\vartheta$ is smooth and $u$ is locally bounded and quasi-plurisubharmonic, its powers are defined by choosing a quadratic $q$ such that $u+q$ is plurisubharmonic and expanding $T=\ddc(u+q)+(\vartheta-\ddc q)$. Independence of $q$ follows from the Bedford--Taylor calculus. Decreasing regularizations may be chosen using nonnegative radial mollifiers after the quadratic correction. Bedford--Taylor monotone continuity then gives convergence of every term in the expansion; see \cref{thm:bt-input}.

\paragraph{Mixed inequalities}

We shall use Dinew's mixed Monge--Amp\`ere inequality \cite[Theorem~1.2]{Dinew09}: if $a,b$ are locally bounded plurisubharmonic functions and
\[
  (\ddc a)^n\geq A\beta^n,
  \qquad
  (\ddc b)^n\geq B\beta^n,
\]
then, for $0\leq k\leq n$,
\[
  (\ddc a)^k\wedge(\ddc b)^{n-k}
  \geq A^{k/n}B^{(n-k)/n}\beta^n.
\]

\begin{lemma}\label{lem:interior-mixed-background}
Let $T_i=\vartheta_i+\ddc u_i\geq0$, $i=1,2$, where $\vartheta_i$ are smooth real $(1,1)$-forms and $u_i$ are locally bounded. If
\[
  T_i^n\geq F_i\beta^n,
  \qquad F_i\geq0\text{ continuous},
\]
then
\begin{equation}\label{eq:interior-mixed-background}
  T_1^k\wedge T_2^{n-k}
  \geq F_1^{k/n}F_2^{(n-k)/n}\beta^n.
\end{equation}
Consequently, for $a,b\geq0$,
\begin{equation}\label{eq:interior-minkowski-background}
  (aT_1+bT_2)^n
  \geq\bigl(aF_1^{1/n}+bF_2^{1/n}\bigr)^n\beta^n.
\end{equation}
\end{lemma}

\begin{proof}
Fix $W\Subset U$. On a ball $B_r(x)$ choose a constant form
\[
  A_i=\vartheta_i(x)+Cr\beta
\]
so that $S_i=A_i-\vartheta_i$ satisfies $0\leq S_i\leq2Cr\beta$. If $q_i$ is a quadratic potential for $A_i$, then $u_i+q_i$ is plurisubharmonic and
\[
  \bigl(\ddc(u_i+q_i)\bigr)^n=(T_i+S_i)^n\geq F_i\beta^n.
\]
Apply Dinew's inequality to the two closed Hessians. After expansion, every term not equal to $T_1^k\wedge T_2^{n-k}$ contains some $S_i$ and is bounded by $C'r\mu$, where
\[
  \mu=\sum_{a+b\leq n-1}T_1^a\wedge T_2^b\wedge\beta^{n-a-b}
\]
is locally finite. A finite cover and a partition of unity give on $W$
\[
  T_1^k\wedge T_2^{n-k}
  \geq F_1^{k/n}F_2^{(n-k)/n}\beta^n-C'r\mu.
\]
Letting $r\downarrow0$ proves \eqref{eq:interior-mixed-background}; the binomial expansion gives \eqref{eq:interior-minkowski-background}.
\end{proof}

\begin{lemma}\label{lem:interior-convolution}
Suppose $u$ is continuous, $T=\vartheta+\ddc u\geq0$, and $T^n\geq g^n\beta^n$ with $g\geq0$ continuous. For a nonnegative convolution kernel $\chi_\delta$ of mass one,
\begin{equation}\label{eq:interior-convolution}
  (T*\chi_\delta)^n\geq(g*\chi_\delta)^n\beta^n
\end{equation}
on every smaller domain on which the convolution is defined.
\end{lemma}

\begin{proof}
Approximate the convolution by finite convex combinations of translates and apply \eqref{eq:interior-minkowski-background}. The background forms converge smoothly and the potentials converge uniformly on compact sets. To pass to the limit, add a common quadratic and telescope the difference of two powers. After pairing with a test form, integration by parts bounds each term by the uniform difference of the potentials times a mixed-current mass. Successive integration against nested cutoffs gives a uniform bound for those masses. Thus the bounded-potential products converge and \eqref{eq:interior-convolution} follows.
\end{proof}

\paragraph{Comparison without a closed background}

We first record the one closed-current comparison fact that enters the proof. If $a,b$ are locally bounded plurisubharmonic functions, $E=\{a<b\}\Subset U$, and $S$ is a positive closed $(n-1,n-1)$-current obtained as a product of bounded plurisubharmonic Hessians and smooth closed positive forms, then
\begin{equation}\label{eq:interior-mixed-BT-comparison}
  \int_E\ddc b\wedge S\leq\int_E\ddc a\wedge S.
\end{equation}
Indeed, apply the Bedford--Taylor integration-by-parts formula to $b_\epsilon=\max\{a,b-\epsilon\}$ and let $\epsilon\downarrow0$; monotone continuity gives the limit. Replacing one factor at a time yields, for $P=\ddc a$ and $Q=\ddc b$,
\begin{equation}\label{eq:interior-power-comparison}
  \int_E P^{n-j}\wedge Q^j\leq\int_E P^n,
  \qquad 0\leq j\leq n.
\end{equation}
This is the mixed form of the local Bedford--Taylor comparison principle, as developed in \cite{SGPT}. Notice that only closed Hessians occur in \eqref{eq:interior-mixed-BT-comparison}.

\begin{proposition}\label{prop:interior-comparison}
Let $D\Subset\mathbb C^n$ be a bounded domain and let $\vartheta$ be a smooth real $(1,1)$-form near $\overline D$. Suppose $u,v\in C(\overline D)$ are $\vartheta$-plurisubharmonic,
\[
  (\vartheta+\ddc u)^n\geq F\beta^n,
  \qquad
  (\vartheta+\ddc v)^n\leq F\beta^n,
\]
where $F>0$ is continuous. If $u\leq v$ on $\partial D$, then $u\leq v$ in $D$.
\end{proposition}

\begin{proof}
We first prove the lower-test property for $v$. Suppose that a $C^2$ function $q$ touches $v$ from below at $p$ and, at $p$,
\[
  \vartheta+\ddc q>0,
  \qquad
  \det_\beta(\vartheta+\ddc q)>F.
\]
After replacing $q$ by $q-a|z-p|^2$ and shrinking a ball $B_r(p)$, there are fixed $\lambda,\eta>0$ such that
\[
  A:=\vartheta+\ddc q\geq\lambda\beta,
  \qquad A^n\geq(F+\eta)\beta^n.
\]
Put $\kappa=\sup_{B_r}\lVert\vartheta-\vartheta(p)\rVert_\beta$ and $B_0=\vartheta(p)+\kappa\beta$. Thus $S=B_0-\vartheta$ satisfies $0\leq S\leq2\kappa\beta$. For small $s>0$ the set $E=\{v<q+s\}$ is nonempty and relatively compact in $B_r$. If $Q_0$ is a quadratic potential for $B_0$, then
\[
  P=\ddc(v+Q_0)=\vartheta+\ddc v+S,
  \qquad
  Q=\ddc(q+s+Q_0)=A+S\geq\lambda\beta
\]
are closed positive Hessians. Applying \eqref{eq:interior-power-comparison}, expanding $P$, and using $S\leq2\kappa\beta\leq2\kappa\lambda^{-1}Q$, we obtain
\[
  \int_E P^n\leq\int_E F\beta^n+e_\kappa\int_E P^n,
  \qquad
  e_\kappa=\left(1+\frac{2\kappa}{\lambda}\right)^n-1.
\]
On the other hand, comparison gives
\[
  \int_E P^n\geq\int_E Q^n\geq\int_E(F+\eta)\beta^n.
\]
If $M$ bounds $F$ on the ball, then $(1-e_\kappa)\eta\leq e_\kappa M$, which is impossible after $r$ is decreased because $e_\kappa\to0$. Thus no such lower test exists.

Suppose now that $\max_D(u-v)>0$. For small $t>0$ and $C\geq\sup_D|z|^2$, set
\[
  u_t=u+t(|z|^2-C).
\]
Then $u_t\leq v$ on $\partial D$, the positive maximum persists, and $T_t=\vartheta+\ddc u_t\geq t\beta$. \Cref{lem:interior-mixed-background} gives
\[
  T_t^n\geq(F^{1/n}+t)^n\beta^n.
\]
Choose a relatively compact neighborhood $W$ of the positive maximum set. By \cref{lem:interior-convolution},
\[
  (T_t*\chi_\delta)^n
  \geq\bigl((F^{1/n}+t)*\chi_\delta\bigr)^n\beta^n.
\]
Since
\[
  \vartheta+\ddc(u_t*\chi_\delta)
  =T_t*\chi_\delta+(\vartheta-\vartheta*\chi_\delta),
\]
the convolution satisfies $T_t*\chi_\delta\geq t\beta$. If
$\epsilon_\delta=\|\vartheta-\vartheta*\chi_\delta\|_{C^0(W)}$, then
\[
 \vartheta+\ddc(u_t*\chi_\delta)
 \geq(1-\epsilon_\delta/t)(T_t*\chi_\delta).
\]
For fixed $t>0$, uniform convergence of the convolved density and
$\epsilon_\delta\to0$ show that the left-hand side is positive and has
determinant strictly larger than $F$ for small $\delta$. Uniform convergence preserves an interior maximum of $u_t*\chi_\delta-v$. Subtracting its value produces a forbidden smooth lower test for $v$, a contradiction.
\end{proof}

\subsection{Bounded traces and smoothness}\label{sec:interior-criterion}

The final local bootstrap can be isolated from the approximation argument.

\begin{proposition}\label{prop:interior-criterion}
Let $T=\vartheta+\ddc u\geq0$ on a coordinate ball, where $u$ is continuous and
\begin{equation}\label{eq:interior-local-ma}
  T^n=F\beta^n,
  \qquad F\in C^\infty,\quad F>0.
\end{equation}
At a point $p$, the following are locally equivalent:
\begin{enumerate}
\item $u$ is smooth;
\item $T\geq\delta\beta$ for some $\delta>0$;
\item $\operatorname{tr}_\beta T$ has a locally bounded measure density.
\end{enumerate}
\end{proposition}

\begin{proof}
Choose $C$ so that $v=u+C|z|^2$ is plurisubharmonic, and use nonnegative radial mollifiers for which $v_\eta\downarrow v$. The smooth matrix convolutions $T_\eta=T*\chi_\eta$ can be written as
\[
  T_\eta=(\vartheta*\chi_\eta-C\beta)+\ddc v_\eta.
\]
Bedford--Taylor monotone continuity and smooth convergence of the background imply $T_\eta^k\to T^k$ for every $k$.

Assume (2). For every Hermitian matrix $M\geq\delta I$,
\[
  \det M\geq\delta^{n-1}\bigl(\operatorname{tr} M-(n-1)\delta\bigr).
\]
Apply this to the regularizations and pass to currents. Equation \eqref{eq:interior-local-ma} gives
\[
  \operatorname{tr}_\beta T\leq\delta^{1-n}F+(n-1)\delta,
\]
which is (3).

Conversely assume (3), say $\operatorname{tr}_\beta T\leq L$. Positivity makes every coefficient of the matrix-valued current $T$ a bounded density. Hence the Euclidean Laplacian of $u$ is locally bounded, and interior Poisson estimates give $u\in W^{2,q}_{\mathrm{loc}}$ for every finite $q$. Mollification converges in $W^{2,q}$; taking $q>2n$ identifies the bounded-potential determinant with the ordinary almost-everywhere determinant. Thus $\det_\beta T=F$ almost everywhere. On a smaller ball with $F\geq m>0$, all eigenvalues of $T$ are at most $L$ and their product is at least $m$, so
\[
  \frac{m}{L^{n-1}}I\leq T\leq LI
\]
almost everywhere.

It remains to regularize a strong solution. Let $P(M)$ be the complex Hessian associated with a real symmetric Hessian $M$, and let $\Theta(x)$ be the matrix of $\vartheta$. With $\delta=mL^{1-n}$, define the concave extension
\[
  G(x,M)=\inf_{\delta I\leq A\leq LI}
  \left\{\log\det A+\operatorname{tr}\!\left[A^{-1}\bigl(\Theta(x)+P(M)-A\bigr)\right]\right\}-\log F(x).
\]
For fixed $A$, write $\mathcal E_A(x,M)$ for the expression in braces
minus $\log F(x)$. The tangent-plane formula for $\log\det$ gives
\[
  G(x,D^2u)=0\quad\text{almost everywhere}.
\]
The operator $G$ is concave and uniformly elliptic on real symmetric matrices. The affine operators $\mathcal E_A$ have constant principal matrices with eigenvalues bounded above and below in terms of $\delta$ and $L$. Their $x$-dependence is smooth uniformly in $A$, so $G$ has a uniform local Lipschitz modulus in $x$.

We verify that the strong solution is a viscosity solution. Suppose that a smooth function $p$ touches $u$ from above at $x_0$ and that $G(x_0,D^2p)<0$. Some fixed matrix $A$ then satisfies $\mathcal E_A(x,D^2p)<-\eta$ on a small ball. Since $G(x,D^2u)=0$ almost everywhere, $\mathcal E_A(x,D^2u)\geq0$ there. Thus $u-p$ has an interior maximum and satisfies
\[
  \operatorname{tr}\!\left(A^{-1}P(D^2(u-p))\right)\geq\eta
  \quad\text{almost everywhere}.
\]
After a small quadratic perturbation makes the contact strict, this contradicts the Aleksandrov maximum principle \cite[Chapter~9, Theorem~9.1]{GT01}. If instead $p$ touches $u$ from below and $G(x_0,D^2p)>0$, then $\mathcal E_A(x,D^2p)>\eta$ for every admissible $A$ on a small ball. At almost every point choose an admissible $A(x)$ with $\mathcal E_{A(x)}(x,D^2u)<\eta/2$. A measurable choice is obtained by taking the first qualifying element of a countable dense family. The function $p-u$ then violates the same maximum principle for the measurable uniformly elliptic coefficients $A(x)^{-1}$. Hence $u$ is a viscosity solution of $G(x,D^2u)=0$.

The variable-coefficient Evans--Krylov theorem \cite[Definition~3.2, Theorem~3.4, and the paragraph following it]{TWWY15} gives $u\in C^{2,\alpha}_{\mathrm{loc}}$. The original equation is now uniformly elliptic with smooth data. Difference quotients satisfy linear equations whose principal coefficients are averages of inverse matrices along positive definite segments. Interior Schauder estimates first give $u\in C^{3,\alpha}_{\mathrm{loc}}$ and then, by iteration, $u\in C^\infty$. This proves (3)$\Rightarrow$(1). Finally, (1) and $F>0$ imply that the smooth semipositive matrix $T$ is positive definite, giving (2) and (3).
\end{proof}

\subsection{Smooth exact approximants}\label{sec:interior-approximants}

We construct local smooth solutions for the original background.

For smooth positive $F$ and smooth boundary data, the proof of
\cref{lem:ball-smooth-dirichlet} applies without change to
$(\vartheta+\ddc u)^n=F\beta^n$. Indeed, a smooth extension of the boundary
values plus a sufficiently large multiple of $|z|^2-R^2$ is a strict
subsolution. We use precisely the same classical input
\cite[Theorem~1.1]{GL10}; for $n=1$ this is the Poisson Dirichlet problem.
The following estimates keep track of the boundary-data dependence.

\Needspace{20\baselineskip}
\begin{lemma}\label{lem:interior-trace-peak}
Let $B$ be a coordinate ball, let $\vartheta$ and $F>0$ be smooth near $\overline B$, and let $q$ be smooth with $R=\vartheta+\ddc q\geq\varepsilon\beta$. Fix $L<\infty$. If $u\in C^\infty(B)$ satisfies
\[
  T=\vartheta+\ddc u>0,
  \qquad T^n=F\beta^n,
  \qquad |u-q|\leq L,
\]
put $S=\operatorname{tr}_\beta T$, $v=u-q$, and
\[
  Q_A=\log S-Av+\mathrm{e}^{-v}.
\]
There are $A_0,C$, depending only on the fixed data and $L$, such that at every interior local maximum of $Q_A$, with $A\geq A_0$,
\begin{equation}\label{eq:interior-trace-peak}
  S\leq C\sqrt A.
\end{equation}
No gradient bound for $u$ is assumed.
\end{lemma}

\begin{proof}
At the point in question make a constant unitary change of coordinates so that the matrix of $T$ is diagonal, with eigenvalues $\lambda_i$. Write
\[
  \Delta_T=\sum_i\lambda_i^{-1}\partial_i\partial_{\bar i},
  \qquad H=\operatorname{tr}_T\beta.
\]
Differentiating $\log\det T=\log F$ and commuting derivatives gives
\begin{equation}\label{eq:interior-trace-differentiation}
  \Delta_TS=\Delta_\beta\log F+P+E_0,
  \quad
  P=\sum_{k,i,j}\frac{|\partial_kT_{i\bar j}|^2}{\lambda_i\lambda_j},
  \quad |E_0|\leq C_0H.
\end{equation}
The non-closedness of $\vartheta$ enters through the bounded vector
\[
  E_p=\sum_k(\partial_p\vartheta_{k\bar k}-\partial_k\vartheta_{p\bar k}).
\]
Since $\partial_pS-E_p=\sum_k\partial_kT_{p\bar k}$, weighted Cauchy--Schwarz gives $|\partial S-E|_T^2\leq SP$. From \eqref{eq:interior-trace-differentiation},
\begin{equation}\label{eq:interior-log-trace}
  \Delta_T\log S
  \geq-\frac{C_0(1+H)}S-
  \frac2S\operatorname{Re}\langle\partial\log S,E\rangle_T.
\end{equation}

Set $g_A(s)=-As+\mathrm{e}^{-s}$. At a local maximum of $Q_A$, $\partial\log S=-g_A'(v)\partial v$ and $\Delta_Tv=n-\operatorname{tr}_TR$. Combining these identities with \eqref{eq:interior-log-trace}, then completing the square in $\partial v$, yields
\begin{equation}\label{eq:interior-peak-inequality}
  0\geq
  \left[\varepsilon A-\frac{C_2}{S}-\frac{C_2(A+1)^2}{S^2}\right]H
  -C_3(A+1)-\frac{C_2}{S}.
\end{equation}
Here $|E|_T^2\leq CH$ and the bounds for $v$ have been used. If $S\geq K\sqrt A$ and $K$ is large, the bracket is at least $\varepsilon A/2$. Thus $H\leq C$ independently of $A$ and $u$. The determinant upper bound then gives $S\leq C'$. Enlarging $K$ makes this incompatible with $S\geq K\sqrt A$, proving \eqref{eq:interior-trace-peak}.
\end{proof}

We shall also use the following gradient-controlled variant. If $|\nabla(u-q)|_\beta$ is bounded, then at an interior maximum of $\log S-A(u-q)$ the trace is bounded independently of $A$ for all large $A$. Indeed, at the maximum $\partial\log S=A\partial(u-q)$, and \eqref{eq:interior-log-trace} gives
\[
  0\geq\left[A\varepsilon-\frac CS-\frac{CA}{S}\right]H-nA-\frac CS.
\]
For $S$ larger than a fixed constant the bracket is at least $A\varepsilon/2$; the determinant again controls $S$.

\paragraph{A polynomial boundary trace estimate}

The next estimate records quantitative dependence on the boundary data.

\begin{proposition}\label{prop:interior-global-trace}
Let $B$ be the unit ball. Fix smooth $\vartheta$, smooth $F>0$ near $\overline B$, and $M<\infty$. There are $C,N<\infty$, depending only on these fixed data, such that every smooth solution
\[
  T=\vartheta+\ddc u>0,
  \qquad T^n=F\beta^n,
  \qquad \lVert u\rVert_{L^\infty(B)}\leq M,
  \qquad u|_{\partial B}=g,
\]
satisfies
\begin{equation}\label{eq:interior-polynomial-global-trace}
  \sup_{\overline B}\operatorname{tr}_\beta T
  \leq C\bigl(1+\lVert g\rVert_{C^4(\partial B)}\bigr)^N.
\end{equation}
\end{proposition}

\begin{proof}
Put $L=1+\lVert g\rVert_{C^4}$. Extend $g$ to $G$ on $\overline B$ with $\lVert G\rVert_{C^4}\leq CL$. For $A=CL$ large enough,
\[
  \underline u=G+A(|z|^2-1),
  \qquad
  \underline T=\vartheta+\ddc\underline u\geq K\beta,
  \qquad
  \underline T^n\geq F\beta^n.
\]
\Cref{prop:interior-comparison} gives $\underline u\leq u$. If $h$ solves $\Delta_\beta h=-C_\vartheta$ with $h=g$ on $\partial B$ and $C_\vartheta\geq\sup\operatorname{tr}_\beta\vartheta$, then $u\leq h$. Boundary differentiation of these barriers gives
\begin{equation}\label{eq:interior-first-boundary}
  |\partial_\nu u|+|\nabla_{\tan}u|\leq CL
  \quad\text{on }\partial B.
\end{equation}

Let $H=\operatorname{tr}_T\beta$, $\mathcal L=\operatorname{tr}_T\ddc$, and $w=u-\underline u\geq0$. Taking $K$ fixed and sufficiently large gives
\begin{equation}\label{eq:interior-w-barrier}
  \mathcal Lw=n-\operatorname{tr}_T\underline T\leq-(1+H).
\end{equation}
Let $E=\sum_k(z_k\partial_{z_k}+\bar z_k\partial_{\bar z_k})$ be the real radial field. Differentiating $\log\det T=\log F$ and commuting $E$ with complex second derivatives yields
\[
  \mathcal L(Eu)=E(\log F)+2n-\operatorname{tr}_T(E\Theta+2\Theta),
\]
where $\Theta$ is the matrix of $\vartheta$. Hence $|\mathcal L(Eu)|\leq C(1+H)$. The same estimate holds for $Zu$ when $Z$ is an infinitesimal unitary rotation. Applying the minimum principle to $CL+C'w\pm Yu$, with $Y=E$ or $Z$, gives
\begin{equation}\label{eq:interior-first-fields}
  |Eu|+|Zu|\leq CL\quad\text{on }B.
\end{equation}

For a rotation $Z$, the function $R_Z=Z(u-G)$ vanishes on $\partial B$ and satisfies $|\mathcal LR_Z|\leq CL(1+H)$. The barriers $CLw\pm R_Z$ and \eqref{eq:interior-w-barrier} imply $|\partial_\nu R_Z|\leq CL^2$ on the boundary. Rotations span its real tangent space, so all real mixed normal--tangential second derivatives are $O(L^2)$. Pure tangential second derivatives are $O(L)$ by differentiating $u=g$ twice and using \eqref{eq:interior-first-boundary}. Thus all complex Hessian entries except the complex normal--normal entry are $O(L^2)$.

It remains to bound the tangential block from below. For $n\geq2$, let
\[
  \lambda_0=\min\{T_p(\xi,\bar\xi):p\in\partial B,
  \ \xi\in T_p^{1,0}(\partial B),\ |\xi|_\beta=1\}.
\]
Choose a minimizing pair $(p,\xi)$ and extend $\xi$ to a smooth unit tangential field near $p$, with uniformly bounded derivatives. On the sphere, any smooth function vanishing there satisfies
\[
  \ddc(u-G)(\xi,\bar\xi)=\frac12E(u-G).
\]
Define
\[
  a(z)=(\vartheta+\ddc G)_z(\xi(z),\overline{\xi(z)})-\frac12EG(z),
  \qquad
  P=a+\frac12Eu-\lambda_0.
\]
Then $P\geq0$ on the nearby spherical boundary and $P(p)=0$.
The boundary first-derivative bound also gives $\lambda_0\leq CL$ by
the displayed tangential identity. Consequently
\[
  |P|\leq CL,
  \qquad
  |\mathcal LP|\leq CL(1+H).
\]
On a fixed cap $D=B\cap B_r(p)$ consider
\[
  \Psi=P+C_1Lw+C_2L|z-p|^2.
\]
Choose $C_2$ so that $\Psi\geq0$ on the interior spherical part of $\partial D$, and then $C_1$ so that $\mathcal L\Psi\leq0$ by \eqref{eq:interior-w-barrier}. The minimum principle yields $\Psi\geq0$. At $p$ the normal derivative of $|z-p|^2$ vanishes, and therefore
\[
  \partial_\nu P+C_1L\partial_\nu w\leq0.
\]
Equations \eqref{eq:interior-first-boundary}--\eqref{eq:interior-first-fields} now give $D^2u(\nu,\nu)(p)\leq CL^2$, hence $\operatorname{tr}_\beta T(p)\leq CL^2$. Positivity and $\det_\beta T=F$ imply
\begin{equation}\label{eq:interior-tangential-lower}
  \lambda_0\geq cL^{-2(n-1)}.
\end{equation}

At any boundary point write
\[
  T=\begin{pmatrix}B_0&b\\ b^*&d\end{pmatrix}
\]
in tangential--normal blocks. We have $|b|\leq CL^2$ and $B_0\geq\lambda_0I$. The determinant equation and the Schur complement give
\[
  d=\frac{F}{\det B_0}+b^*B_0^{-1}b
  \leq(\sup F)\lambda_0^{-(n-1)}+CL^4\lambda_0^{-1},
\]
which is polynomial in $L$. For $n=1$, the trace is $F$ and this argument is unnecessary.

Finally, choose a fixed quadratic $q$ with $\vartheta+\ddc q\geq\varepsilon\beta$. Apply \cref{lem:interior-trace-peak} with one fixed $A$. At an interior maximum of its auxiliary function the trace is uniformly bounded, while at a boundary maximum the preceding estimate applies. Since the remaining terms are uniformly bounded, \eqref{eq:interior-polynomial-global-trace} follows.
\end{proof}

\paragraph{Exact approximation}

\begin{proposition}\label{prop:interior-tame-approximants}
Let $B\Subset\Omega$ be a coordinate ball with closure in a larger coordinate chart, and put
\[
  F=\frac{cf\,\omega_X^n}{\beta^n}.
\]
There are $a>0$, $b,C<\infty$, and $u_j\in C^\infty(\overline B)$ such that
\begin{equation}\label{eq:interior-exact-approximants}
  \theta+\ddc u_j>0,
  \qquad
  (\theta+\ddc u_j)^n=F\beta^n,
\end{equation}
and
\begin{equation}\label{eq:interior-tame-rates}
  \lVert u_j-\varphi\rVert_{L^\infty(B)}\leq Cj^{-a},
  \qquad
  \sup_{\overline B}\operatorname{tr}_\beta(\theta+\ddc u_j)\leq Cj^b.
\end{equation}
\end{proposition}

\begin{proof}
Local H\"older continuity of $\varphi$ gives smooth boundary approximations $g_j$ with
\[
  \lVert g_j-\varphi\rVert_{L^\infty(\partial B)}\leq Cj^{-a},
  \qquad
  \lVert g_j\rVert_{C^4(\partial B)}\leq Cj^4.
\]
Choose a fixed quadratic $q$ with $\eta=\theta+\ddc q>0$ near $\overline B$. Extend $g_j$ smoothly to $G_j$. For a sufficiently large, polynomially bounded $A_j$, the function
\[
  \underline w_j=G_j-q+A_j(|z|^2-R^2)
\]
has boundary value $g_j-q$ and satisfies
\[
  \eta+\ddc\underline w_j
  =\theta+\ddc G_j+A_j\beta>0,
  \qquad
  (\eta+\ddc\underline w_j)^n\geq F\beta^n.
\]
Apply the smooth Dirichlet theorem just recalled with density $H=F\beta^n/\eta^n$ to obtain a solution $w_j$ for the Hermitian background $\eta$; put $u_j=w_j+q$. Comparing $u_j$ with $\varphi\pm\lVert g_j-\varphi\rVert_\infty$ by \cref{prop:interior-comparison} proves the first bound in \eqref{eq:interior-tame-rates}. The functions $u_j$ are therefore uniformly bounded. \Cref{prop:interior-global-trace} and the polynomial $C^4$ boundary norm give the second bound.
\end{proof}

\subsection{Localization near the nonregular set}\label{sec:interior-localization}

\begin{proposition}\label{prop:interior-subpower}
Let $B=B_R(0)$, let $\vartheta$ and $F>0$ be smooth, and let $u\in C(\overline B)$. Suppose $q$ is smooth and $\vartheta+\ddc q\geq\varepsilon\beta$. Put $v=u-q$. Let $\mathcal S\subset\overline B$ be closed, contain $0$, and satisfy
\begin{equation}\label{eq:interior-quadratic-separation}
  v(0)=m,
  \qquad
  v(z)\geq m+\kappa|z|^2\quad(z\in\mathcal S).
\end{equation}
Assume that smooth exact solutions $u_j$, $j\geq2$, satisfy
\begin{align}
  \lVert u_j-u\rVert_\infty&\leq Cj^{-a}, \label{eq:interior-localization-a}\\
  \sup_{\overline B}\operatorname{tr}_\beta(\vartheta+\ddc u_j)&\leq Cj^b, \label{eq:interior-localization-b}\\
  \sup_j\sup_K\operatorname{tr}_\beta(\vartheta+\ddc u_j)&<\infty
  \quad\text{for every }K\Subset\overline B\setminus\mathcal S. \label{eq:interior-localization-c}
\end{align}
Then for every $\gamma>0$ there are a neighborhood $U_\gamma$ of $0$ and $C_\gamma$ such that
\begin{equation}\label{eq:interior-subpower-trace}
  \operatorname{tr}_\beta(\vartheta+\ddc u_j)\leq C_\gamma j^\gamma
  \quad\text{on }U_\gamma.
\end{equation}
Consequently $u\in C^{1,\alpha}$ near $0$ for every $0<\alpha<1$.
\end{proposition}

\begin{proof}
Write $e_j=Cj^{-a}$. Fix small $\eta>0$. For small $\delta>0$, the neighborhood
\[
  W_\delta=\{z\in B:\operatorname{dist}(z,\mathcal S)<\delta\}
\]
contains $0$, has $v\geq m-\eta$ on its closure, and satisfies $v\geq m+d$ on $\partial B\cap\overline W_\delta$ for some fixed $d>0$. This follows from \eqref{eq:interior-quadratic-separation}, continuity, and compactness. The other boundary portion is a compact subset of $\overline B\setminus\mathcal S$, where \eqref{eq:interior-localization-c} applies.

Choose $D>(b+1)/d$ and set $A_j=D\log j$. Apply the maximum principle on $\overline W_\delta$ to
\[
  Q_j=\log\operatorname{tr}_\beta(\vartheta+\ddc u_j)-A_j(u_j-q)+\mathrm{e}^{-(u_j-q)}.
\]
At an interior maximum \cref{lem:interior-trace-peak} gives $\log\operatorname{tr}_\beta(\vartheta+\ddc u_j)\leq C+\frac12\log A_j$. On the boundary away from $\mathcal S$ there is a fixed trace bound. On the outer boundary, \eqref{eq:interior-localization-b} and the gap $d$ give
\[
  Q_j\leq C+b\log j-A_j(m+d-e_j),
\]
which is suppressed by the choice of $D$. Hence throughout $W_\delta$,
\[
  Q_j\leq C_\delta+\tfrac12\log A_j-A_j(m-\eta-e_j).
\]
On a small ball about $0$ where $v\leq m+\eta$, this implies
\[
  \log\operatorname{tr}_\beta(\vartheta+\ddc u_j)
  \leq C_\delta+\tfrac12\log A_j+A_j(2\eta+2e_j).
\]
Choose $\eta$ so that $2D\eta<\gamma/2$; the logarithmic factor and $A_je_j$ are absorbed into the remaining power. This proves \eqref{eq:interior-subpower-trace}.

On a smaller ball, the real Laplacian of $u_j$ is bounded by $Cj^\gamma$. Interior Poisson estimates and Sobolev embedding give, for every finite $q_0$ and every $\sigma<1$ obtainable by taking $q_0$ large,
\[
  \lVert u_j\rVert_{W^{2,q_0}}+\lVert u_j\rVert_{C^{1,\sigma}}
  \leq Cj^\gamma.
\]
For $d_k=u_{2^{k+1}}-u_{2^k}$,
\[
  \lVert d_k\rVert_\infty\leq C2^{-ka},
  \qquad
  \lVert d_k\rVert_{C^{1,\sigma}}\leq C2^{k\gamma}.
\]
If $\alpha<\sigma$ and $t=(1+\alpha)/(1+\sigma)$, H\"older interpolation gives
\[
  \lVert d_k\rVert_{C^{1,\alpha}}
  \leq C2^{k[-a(1-t)+\gamma t]}.
\]
Since $\gamma$ may be arbitrarily small, the exponent can be made negative. The dyadic series converges in $C^{1,\alpha}$ to its uniform limit $u$.
\end{proof}

\begin{proposition}\label{prop:interior-regular-stability}
Suppose $u_j$ solve the same smooth equation as in \cref{prop:interior-subpower}, satisfy \eqref{eq:interior-localization-a}--\eqref{eq:interior-localization-b}, and $u$ is smooth with $\vartheta+\ddc u>0$ on an open set $O\subset B$. Then, for every $K\Subset O$,
\begin{equation}\label{eq:interior-regular-stability}
  \sup_j\sup_K\operatorname{tr}_\beta(\vartheta+\ddc u_j)<\infty.
\end{equation}
\end{proposition}

\begin{proof}
For $p$ in a fixed compact subset of $O$, take a uniformly sized ball $B_r(p)\Subset O$ and set
\[
  q_p(z)=u(z)-\kappa|z-p|^2
\]
with $\kappa>0$ small, so $\vartheta+\ddc q_p\geq\varepsilon\beta$. If $e_j=Cj^{-a}$ and $v_{j,p}=u_j-q_p$, then
\[
  v_{j,p}\geq-e_j,
  \quad v_{j,p}(p)\leq e_j,
  \quad v_{j,p}\geq\kappa r^2-e_j\text{ on }\partial B_r(p).
\]
With $A_j=D\log j$ and $D\kappa r^2>b+1$, the same maximum argument as above gives
\begin{equation}\label{eq:interior-sqrtlog-trace}
  \operatorname{tr}_\beta(\vartheta+\ddc u_j)(p)\leq C\sqrt{\log j}.
\end{equation}
The constants are uniform on compact subsets of $O$.

Put $w_j=u_j-u$. On slightly larger compact sets, \eqref{eq:interior-sqrtlog-trace} bounds $|\Delta w_j|$ by $C\sqrt{\log j}$. Poisson estimates and Sobolev embedding give
\[
  \lVert w_j\rVert_{C^{1,\sigma}}\leq C_\sigma\sqrt{\log j},
  \qquad \sigma<1.
\]
Interpolating with $\lVert w_j\rVert_\infty\leq Cj^{-a}$ shows $\nabla w_j\to0$ uniformly on smaller compact sets. The gradients of $v_{j,p}$ are therefore uniformly bounded. Repeat the maximum argument with $\log\operatorname{tr}_\beta T_j-A_jv_{j,p}$ and use the gradient-controlled version of \cref{lem:interior-trace-peak}. Its interior trace bound is now independent of $A_j$, while the boundary term is suppressed as before. Evaluation at $p$ gives
\[
  \operatorname{tr}_\beta T_j(p)\leq C\exp(2A_je_j)\leq C,
\]
proving \eqref{eq:interior-regular-stability}.
\end{proof}

\begin{proposition}\label{prop:interior-uniform-c1a}
Under the hypotheses of \cref{prop:interior-subpower}, for every $0<\alpha<1$ there is a neighborhood $U$ of $0$ such that
\[
  \sup_j\lVert u_j\rVert_{C^{1,\alpha}(U)}<\infty.
\]
After slightly lowering $\alpha$, the full sequence converges to $u$ in that norm.
\end{proposition}

\begin{proof}
Choose $\alpha<\sigma<1$. \Cref{prop:interior-subpower}, Poisson estimates, and Sobolev embedding give on a small ball
\[
  \lVert u_j\rVert_{C^{1,\sigma}}\leq Cj^\gamma,
\]
where $\gamma>0$ can be chosen arbitrarily small by shrinking the ball. With $t=(1+\alpha)/(1+\sigma)$, choose $\gamma$ so that $-a(1-t)+\gamma t<0$. Interpolation makes the dyadic differences summable in $C^{1,\alpha}$. If $2^k\leq j<2^{k+1}$, interpolation applied to $u_j-u_{2^k}$ gives the same uniform conclusion for the full sequence. Restricting to a smaller ball removes boundary effects.
\end{proof}

\Needspace{24\baselineskip}
\subsection{Derivative estimates and bounded traces}\label{sec:interior-calabi}

The next estimate needs no K\"ahler identity. Its purpose is quantitative: all dependence on the ellipticity ratio is polynomial.

\begin{proposition}\label{prop:interior-calabi}
Fix smooth $\vartheta$ and smooth $F>0$ near the closed unit ball. There are $C,N<\infty$, depending only on finitely many derivatives of the fixed data, such that any smooth solution
\[
  g=\vartheta+\ddc u,
  \qquad g^n=F\beta^n,
  \qquad M^{-1}\beta\leq g\leq M\beta,
  \qquad M\geq1,
\]
satisfies
\begin{equation}\label{eq:interior-calabi-polynomial}
  \sup_{B_{1/2}}|\partial g|_\beta\leq CM^N.
\end{equation}
If only $\sup_B\operatorname{tr}_\beta g\leq L$ is given, the same bound holds with a fixed power of $1+L$. On a ball of radius $r\leq1$,
\begin{equation}\label{eq:interior-gradient-trace-scaled}
  \sup_{B_{r/2}}|\nabla\operatorname{tr}_\beta g|_\beta
  \leq Cr^{-1}(1+L)^N.
\end{equation}
\end{proposition}

\begin{proof}
Use the flat connection of $\beta$ and the Chern connection $\nabla$ of $g$. Their difference is
\[
  \Psi^k_{ij}=g^{k\bar\ell}\partial_i g_{j\bar\ell},
  \qquad \mathcal R=|\Psi|_g^2.
\]
The lowered torsion tensor is determined by the fixed background. Put
\begin{equation}\label{eq:interior-torsion-background}
  C_{ij\bar\ell}
  =\partial_i\vartheta_{j\bar\ell}-\partial_j\vartheta_{i\bar\ell},
  \qquad
  \mathcal T^k_{ij}=g^{k\bar\ell}C_{ij\bar\ell}.
\end{equation}
Consequently, for a fixed integer $N$,
\begin{align}
  |\mathcal T|&\leq CM^N,\nonumber\\
  |\nabla\mathcal T|+|\bar\nabla\mathcal T|
  &\leq CM^N(1+\sqrt{\mathcal R}),\label{eq:interior-torsion-derivatives}\\
  |\nabla^2\mathcal T|+|\nabla\bar\nabla\mathcal T|+|\bar\nabla^2\mathcal T|
  &\leq CM^N(1+\mathcal R+|\nabla\Psi|+|\bar\nabla\Psi|).\nonumber
\end{align}
Every factor here is either a fixed derivative of $\vartheta$, a connection factor $\Psi$, or a factor of $g^{\pm1}$; this explains the polynomial dependence.

For tensor fields, use $\Delta_g=g^{p\bar q}\nabla_p\nabla_{\bar q}$.
We record the curvature identities used in the estimate. With
\[
  \operatorname{Rm}^k{}_{i\bar j l}=-\partial_{\bar j}\Psi^k_{il},
  \qquad
  \operatorname{Rm}_{i\bar j l\bar k}=g_{m\bar k}\operatorname{Rm}^m{}_{i\bar j l},
\]
set
\[
  \operatorname{Ric}^{(2)}_{l\bar k}=g^{i\bar j}\operatorname{Rm}_{i\bar j l\bar k},
  \qquad
  \operatorname{Ric}^{(1)}_{l\bar k}=g^{i\bar j}\operatorname{Rm}_{l\bar k i\bar j}
  =-\partial_l\partial_{\bar k}\log F.
\]
The two curvature interchanges are
\begin{align*}
  \operatorname{Rm}_{i\bar j l\bar k}-\operatorname{Rm}_{l\bar j i\bar k}
  &=-\nabla_{\bar j}C_{il\bar k},\\
  \operatorname{Rm}_{i\bar j l\bar k}-\operatorname{Rm}_{i\bar k l\bar j}
  &=-\nabla_i\overline{C}_{\bar j\bar k l}.
\end{align*}
They follow by differentiating the torsion identity and its conjugate. Successive interchange and contraction give
\begin{equation}\label{eq:interior-ricci-contraction}
  \operatorname{Ric}^{(2)}_{l\bar k}
  =\operatorname{Ric}^{(1)}_{l\bar k}
  -g^{i\bar j}\bigl(
    \nabla_l\overline C_{\bar j\bar k i}
    +\nabla_{\bar j}C_{il\bar k}
  \bigr).
\end{equation}
Metric compatibility, \eqref{eq:interior-torsion-derivatives}, and the fixed smooth formula for $\operatorname{Ric}^{(1)}$ imply
\begin{equation}\label{eq:interior-ricci2}
  |\operatorname{Ric}^{(2)}|\leq CM^N(1+\sqrt{\mathcal R}),
  \qquad
  |\nabla\operatorname{Ric}^{(2)}|
  \leq CM^N(1+\mathcal R+|\nabla\Psi|+|\bar\nabla\Psi|).
\end{equation}
Moreover,
\[
  \nabla_{\bar q}\Psi^k_{ij}=-\operatorname{Rm}^k{}_{i\bar q j},
\]
and the Chern--Bianchi identity, including its torsion term, is
\[
  \nabla_p\operatorname{Rm}^k{}_{i\bar q j}-\nabla_i\operatorname{Rm}^k{}_{p\bar q j}
  =-\mathcal T^r_{pi}\operatorname{Rm}^k{}_{r\bar q j}.
\]
Consequently,
\begin{equation}\label{eq:interior-laplacian-connection-difference}
  \Delta_g\Psi^k_{ij}
  =-\nabla_i(\operatorname{Ric}^{(2)})^k{}_j
  +g^{p\bar q}\mathcal T^r_{pi}\operatorname{Rm}^k{}_{r\bar q j}.
\end{equation}
If $A^k{}_l=(\operatorname{Ric}^{(2)})^k{}_l$, define its action on a tensor of type $(1,2)$ by
\[
  (A\mathbin{\cdot}\Psi)^k_{ij}
  =A^k{}_l\Psi^l_{ij}-A^l{}_i\Psi^k_{lj}-A^l{}_j\Psi^k_{il}.
\]
Differentiating the squared norm and using metric compatibility gives
\begin{equation}\label{eq:interior-laplacian-calabi-norm}
  \Delta_g\mathcal R
  =|\nabla\Psi|^2+|\bar\nabla\Psi|^2
   +2\operatorname{Re}\langle\Delta_g\Psi,\Psi\rangle
   -\operatorname{Re}\langle A\mathbin{\cdot}\Psi,\Psi\rangle.
\end{equation}
There is no mixed torsion term because the Chern torsion has type $(2,0)$. Using \eqref{eq:interior-torsion-derivatives}, \eqref{eq:interior-ricci2}, and \eqref{eq:interior-laplacian-connection-difference} in \eqref{eq:interior-laplacian-calabi-norm}, Young's inequality absorbs the products of $\sqrt{\mathcal R}$ with $|\nabla\Psi|+|\bar\nabla\Psi|$. We obtain
\begin{equation}\label{eq:interior-calabi-differential}
  \Delta_g\mathcal R\geq-CM^N(\mathcal R^{3/2}+1).
\end{equation}
No closedness of $\vartheta$ has entered.

Let $s=\operatorname{tr}_\beta g$. Direct differentiation as in \eqref{eq:interior-trace-differentiation} gives
\begin{equation}\label{eq:interior-trace-calabi-coupling}
  \Delta_gs\geq M^{-1}\mathcal R-CM,
  \qquad
  |\partial s|_g^2\leq nM^2\mathcal R.
\end{equation}
Take a cutoff $\zeta$ supported in $B$, equal to one on $B_{1/2}$, set $\eta=\zeta^2$ and $h=2nM-s$, so $nM\leq h\leq2nM$, and maximize
\[
  Q=\frac{\eta\mathcal R}{h}.
\]
At a positive interior maximum of $Q$, the identity
$\partial\mathcal R/\mathcal R=\partial h/h-\partial\eta/\eta$ gives
\[
 \begin{split}
 0\geq\frac{\Delta_gQ}{Q}
 &=\frac{\Delta_g\mathcal R}{\mathcal R}
   +\frac{\Delta_g\eta}{\eta}-\frac{\Delta_gh}{h}
   -\frac{2|\partial\eta|_g^2}{\eta^2}
   +\frac{2\operatorname{Re}\langle\partial\eta,\partial h\rangle_g}{\eta h}.
 \end{split}
\]
We have $|\partial\eta|_g^2\leq CM\eta$,
$|\Delta_g\eta|\leq CM$ and
$|\partial h|_g\leq\sqrt n M\sqrt{\mathcal R}$.
Insert \eqref{eq:interior-calabi-differential} and
\eqref{eq:interior-trace-calabi-coupling} and multiply by $\eta Q$.
The positive term is $M^{-1}Q^2$. The two terms involving
$\sqrt{\mathcal R}$ are bounded in absolute value by a fixed power of
$M$ times $Q^{3/2}$, since $\mathcal R=hQ/\eta$ and $h\leq2nM$.
The remaining cutoff terms are bounded by $CM^N(Q+1)$. Therefore
\[
 0\geq M^{-1}Q^2-CM^N(Q^{3/2}+Q+1).
\]
Thus $Q$, and then $\mathcal R$ on $B_{1/2}$, are bounded by a fixed polynomial in $M$. Since $|\partial g|_\beta^2\leq M^3\mathcal R$, this proves \eqref{eq:interior-calabi-polynomial}.

If $s\leq L$, the determinant lower bound gives $\lambda_{\min}(g)\geq(\inf F)L^{1-n}$, so $M$ is a fixed power of $1+L$. For a ball $B_r(p)$, set $u_r(z)=r^{-2}u(p+rz)$ and use the
coefficient matrices $\vartheta_r(z)=\vartheta(p+rz)$,
$g_r(z)=g(p+rz)$ and $F_r(z)=F(p+rz)$. Then
$g_r=\vartheta_r+\ddc u_r$ in the unit coordinates and
$\det g_r=F_r$. For $r\leq1$ the derivatives of the fixed data remain
uniformly bounded. The unit-ball estimate for $\nabla g_r$ gives the
factor $r^{-1}$ in \eqref{eq:interior-gradient-trace-scaled}.
\end{proof}

\Needspace{12\baselineskip}
\begin{proposition}\label{prop:interior-c1a-to-trace}
There is $\alpha_*<1$, depending only on $n$ and the exponent $N$ in \cref{prop:interior-calabi}, with the following property. Let $u_j$ be smooth exact solutions on a ball $B_0$. If
\[
  \sup_j\lVert u_j\rVert_{C^{1,\alpha}(B_0)}<\infty
  \qquad\text{for some }\alpha_*<\alpha<1,
\]
then $\operatorname{tr}_\beta(\vartheta+\ddc u_j)$ is uniformly bounded on every smaller ball.
\end{proposition}

\begin{proof}
Put $s_j=\operatorname{tr}_\beta(\vartheta+\ddc u_j)$ and
\[
  M_j(r)=1+\sup_{B_r}s_j.
\]
For concentric balls $B_r\Subset B_R\Subset B_0$, $d=R-r\leq1$, \cref{prop:interior-calabi} gives
\begin{equation}\label{eq:interior-trace-gradient-M}
  |\nabla s_j|\leq Cd^{-1}M_j(R)^N
  \quad\text{on }B_{r+d/2}.
\end{equation}
Let $\chi_h$ be a nonnegative mollifier of radius $h\leq d/4$. Since
\[
  s_j=\operatorname{tr}_\beta\vartheta+\Delta_\beta u_j,
\]
integration by parts, after subtracting the constant vector $\nabla u_j(p)$, gives
\[
  (s_j*\chi_h)(p)\leq C(1+h^{\alpha-1}).
\]
Equation \eqref{eq:interior-trace-gradient-M} gives
\[
  |s_j(p)-(s_j*\chi_h)(p)|
  \leq Cd^{-1}M_j(R)^Nh.
\]
Choose
\[
  h=\frac d4M_j(R)^{-N/(2-\alpha)}.
\]
After absorbing fixed powers of $d^{-1}$, we obtain
\begin{equation}\label{eq:interior-nonlinear-iteration}
  M_j(r)\leq Cd^{-1}M_j(R)^q,
  \qquad
  q=\frac{N(1-\alpha)}{2-\alpha}.
\end{equation}
Choose $\alpha_*$ so close to one that $q<1$ for $\alpha>\alpha_*$. Let $r_k\uparrow R_0$ with $r_{k+1}-r_k=(R_0-r_0)2^{-k-1}$. Iterating \eqref{eq:interior-nonlinear-iteration} gives
\[
  M_j(r_0)
  \leq
  \prod_{k=0}^{m-1}\left[C(r_{k+1}-r_k)^{-1}\right]^{q^k}
  M_j(r_m)^{q^m}.
\]
The infinite product converges because $\sum q^k(1+k)<\infty$. For each fixed $j$, the final factor tends to one as $m\to\infty$. The resulting bound is independent of $j$.
\end{proof}

\Needspace{8\baselineskip}
\subsection{Proof of the main theorem}\label{sec:interior-main-proof}

\begin{proof}[of \cref{thm:nonclosed-interior-smoothness}]
If $n=1$, the equation is the linear identity
\[
  \ddc\varphi=cf\,\omega_X-\theta
  \quad\text{on }\Omega.
\]
Its right-hand side is smooth, so interior elliptic regularity gives $\varphi\in C^\infty(\Omega)$, and the original equation gives $\theta+\ddc\varphi=cf\,\omega_X>0$. We henceforth assume $n\geq2$.


Let
\[
  \mathcal S=\{p\in\Omega:\varphi\text{ is not smooth on any neighborhood of }p\}.
\]
This is closed in $\Omega$. Suppose $\mathcal S\neq\varnothing$. By \cref{lem:interior-proper-gap}, the restriction of $\varphi-\rho$ to $\mathcal S$ attains its minimum $m$ at some $p\in\mathcal S$.

Choose nested coordinate balls
\[
  B\Subset B_0\Subset\Omega
\]
centered at $p$. On $B_0$, \cref{prop:interior-tame-approximants} gives smooth exact Dirichlet solutions $u_j$ converging uniformly to $\varphi$ at a polynomial rate and having polynomial global trace growth.

On the regular set $\mathcal R=\Omega\setminus\mathcal S$, the function $\varphi$ is smooth. There $\theta+\ddc\varphi$ is semipositive and has positive determinant, hence is positive definite. \Cref{prop:interior-regular-stability} therefore gives a uniform trace bound for the $u_j$ on every compact subset of $\mathcal R\cap B_0$.

In coordinates centered at $p$, take $\kappa>0$ small and set
\[
  q(z)=\rho(z)-\kappa|z|^2.
\]
After shrinking $B$, \eqref{eq:interior-strict-reference} gives $\theta+\ddc q>0$. If $v=\varphi-q$, then the minimizing property of $p$ gives
\[
  v(p)=m,
  \qquad
  v(z)=(\varphi-\rho)(z)+\kappa|z|^2
  \geq m+\kappa|z|^2
  \quad(z\in\mathcal S\cap\overline B).
\]
Thus \cref{prop:interior-subpower} applies on $B$ with the closed set $\mathcal S\cap\overline B$: the approximation rate and global polynomial trace bound come from \cref{prop:interior-tame-approximants}, and the bound away from $\mathcal S$ comes from \cref{prop:interior-regular-stability}. \Cref{prop:interior-uniform-c1a} then gives, for every $0<\alpha<1$, a neighborhood of $p$ on which the approximants have a uniform $C^{1,\alpha}$ bound.

Choose $\alpha>\alpha_*$ as in \cref{prop:interior-c1a-to-trace}. That proposition yields
\[
  \sup_j\operatorname{tr}_\beta(\theta+\ddc u_j)<\infty
\]
on a still smaller neighborhood of $p$. Since $u_j\to\varphi$ uniformly, $\ddc u_j\to\ddc\varphi$ as currents. The trace bound passes to the limit, so $\operatorname{tr}_\beta(\theta+\ddc\varphi)$ has a bounded density near $p$. \Cref{prop:interior-criterion} now implies that $\varphi$ is smooth near $p$, contradicting $p\in\mathcal S$.

Hence $\mathcal S=\varnothing$ and $\varphi\in C^\infty(\Omega)$. The form $\theta+\ddc\varphi$ is smooth and semipositive there, while
\[
  (\theta+\ddc\varphi)^n=cf\,\omega_X^n>0.
\]
Its nonnegative eigenvalues have positive product, so every eigenvalue is positive. Therefore $\theta+\ddc\varphi>0$ on $\Omega$.
\end{proof}

\begin{remark}\label{rem:interior-local-nature}
Two inputs enter the localization: local H\"older continuity supplies polynomial boundary approximation, and the proper gap $\varphi-\rho$ selects a point of the nonregular locus with quadratic separation. Every derivative estimate is local and is performed for the original non-closed form $\theta$.
\end{remark}


\begin{corollary}\label{cor:big-lp-interior-smoothness}
Let $0\leq f\in L^p(X,\omega_X^n)$, $p>1$, be smooth and strictly positive
on $\Omega$. Every minimal-singularity solution of
$(\theta+\ddc\varphi)^n=cf\,\omega_X^n$, $c>0$, is smooth and strictly
$\theta$-plurisubharmonic on $\Omega$.
\end{corollary}
\begin{proof}
The analytic complement of $\Omega$ has zero mass for both measures,
so it suffices to know the equation in the bounded-potential sense on
$\Omega$. Apply \cref{thm:big-minimal-holder} with density $cf$ to obtain
local H\"older continuity. All hypotheses of
\cref{thm:nonclosed-interior-smoothness} are now satisfied.
The existence of a normalized minimal-singularity solution is already
proved in \cref{thm:big-minimal-normalized}.
\end{proof}

This assertion concerns interior regularity. It gives no regularity
across the pole set of the chosen strict barrier, and it does not address
zeros of the density. In particular the degeneracy examples earlier in
this chapter retain their stated scope.

For a smooth closed big representative on a compact K\"ahler manifold,
\cref{thm:big-class-ample-smoothness} applies this conclusion to the
classical full-mass solution and identifies the regular open set with
the ample locus.

```