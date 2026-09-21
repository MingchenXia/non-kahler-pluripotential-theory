Run_id: normalization_functional_01

Statement: Audit the complete chapter below, including every proof. Geometry: compact connected complex X, theta>=0 big in genuine strict-current sense, phi=Ptheta[phi] with genuine P_epsilon theta(phi), dV smoothpositive. B_phi(F)=log unique normalizing scalar in MAext(u)=c exp(F)dV,u~phi,F real boundedmeasurable. Targets: order/translation/supnormLip; singular convex density inequality from local bounded mixed inequality using finitelevels; concavity; boundedL1(dV) continuity of B; existence/compactness/absolutecontinuity of supporting probabilities A_phi(F) onC(X); stability, exact one-sided derivative formulas, differentiability iff singleton; recovery ofGauduchon adjoint for smoothHermitian background; closedKahler formula. NoBMP/PVP; no uniquenessofpotential assumed. Be especially critical of the absolutecontinuity inference and subgradient existence in infinite dimension, and signs/orientations.

Accepted inputs: prescribed ordinarytype Lp normalized existence and scalaruniqueness thm:als-prescribed-lp (prescribed_lp_existence_01 active, acceptconditionally ifreportpending); relativeuniformestimate(relative_lp_barriers_01); commonbarrierdominatedcapacity/rawweak continuity andfixedNPPexp(common_barrier_compactness_01 main deductions passed, sole standalone monotone overstatement corrected and under common_barrier_repair_01); singularstrictdomination(singular_domination_01); bounded nonclosed mixed density lemma(nonclosed-mixed-density in bounded_subsolution_01 passed); canonicalqpshcompactness, plurifine locality, ordinaryclassboundedstability, standardmeasure/HB/Riesz/RN,BanachAlaoglu on compactX. Smoothnormalizedsolvability andGaudadjoint derivative(thm:b-derivatives) alreadyproved/auditedgauduchon_duality_01/smooth_czero_01 etc; readbookexact hypotheses. ClosedKahler ordinarytype nonpluripolarmass invariance/finite fromSGPT accepted. Do not re-audit earlier deep inputs, checktheirscope anduse. The referenceCollins21iscontextonly, notusedasaninput; no claimnovelty. Questions are proposed, no claimofverifiedopenstatus. No assertionofdistributionalweakadjointidentity, noenergyprimitiveclaim. Book read-only. Saveusualreport.

Proof:

\chapter{Normalization and weak adjoint measures}
\label{chap:normalization}

A Gauduchon metric enters the smooth Monge--Amp\`ere equation through the derivative of its normalizing constant. We now recover part of this construction from the weak equation itself. The variable will be the logarithm of the prescribed density. Concavity gives supporting probability measures, even when the solution is singular and its linearized operator has not been defined.

Throughout this chapter, $\theta$ is semipositive and big, $dV$ is a smooth positive volume form, and $\varphi$ is a model potential satisfying
\begin{equation}\label{eq:normalization-reference}
 P_\theta[\varphi]=\varphi,\qquad
 P_{\varepsilon\theta}(\varphi)\not\equiv-\infty
 \quad\text{for some }0<\varepsilon<1.
\end{equation}
No bounded mass or uniform positive lower mass hypothesis is imposed. The existence theorem of the preceding chapter supplies the only global equation input. The arguments below are consequences of that theorem, singular domination and the local mixed inequality. We make no novelty claim for these deductions.

\section{The scalar functional}

For a bounded real measurable function $F$, \cref{thm:als-prescribed-lp} gives $u\simeq\varphi$ and a unique $c_\varphi(F)>0$ such that
\begin{equation}\label{eq:relative-normalization}
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)
       =c_\varphi(F)e^F\,dV.
\end{equation}
Define
\[
 B_\varphi(F)=\log c_\varphi(F).
\]
Functions equal $dV$-almost everywhere are identified. This definition uses uniqueness of the scalar, not uniqueness of the normalized potential. The condition $u\simeq\varphi$ shows that the scalar is attached to the ordinary singularity type being prescribed.

\begin{proposition}\label{prop:relative-normalization-order}
The functional $B_\varphi$ is decreasing, and for every constant $a\in\R$,
\[
 B_\varphi(F+a)=B_\varphi(F)-a.
\]
Consequently
\begin{equation}\label{eq:relative-normalization-lipschitz}
 -\mathop{\rm ess\,sup}_X(G-F)
 \leq B_\varphi(G)-B_\varphi(F)
 \leq-\mathop{\rm ess\,inf}_X(G-F),
\end{equation}
and $|B_\varphi(G)-B_\varphi(F)|\leq\|G-F\|_\infty$.
\end{proposition}
\begin{proof}
Suppose $F\leq G$ almost everywhere and, to obtain a contradiction, $c_\varphi(F)<c_\varphi(G)$. Let $u,v\simeq\varphi$ solve the two equations. Then, for every constant $a$,
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)
 \leq\frac{c_\varphi(F)}{c_\varphi(G)}
             \mathrm{MA}^{\mathrm{ext}}_\theta(v+a).
\]
The ratio is strictly less than one. Bounded equivalence transfers the genuine smaller-background envelope from $\varphi$ to $u$, and $v+a\preceq u$. Singular strict domination gives $u\geq v+a$ for every $a$. This is impossible at any point where both potentials are finite. Thus $B_\varphi(F)\geq B_\varphi(G)$.

Replacing $F$ by $F+a$ and the constant by $e^{-a}c_\varphi(F)$ leaves the right side of \eqref{eq:relative-normalization} unchanged. Scalar uniqueness proves the translation rule. Apply monotonicity to the two constant translates of $F$ bounding $G$ to obtain \eqref{eq:relative-normalization-lipschitz}.
\end{proof}

The functional is also unchanged by a smooth change of representative when the solution problem is transported with it: replacing $\theta$ by $\theta+\ddc h$ and every potential by $u-h$ preserves the current and the prescribed ordinary type. This observation describes transport of a solvable problem. It does not assert a new existence theorem for an arbitrary nonsemipositive background.

\section{Concavity from mixed products}

We need a consequence of the bounded mixed inequality for unbounded potentials. It is useful to prove it directly on finite levels, without presuming that their total masses are finite.

\begin{lemma}\label{lem:singular-convex-density}
Suppose $u,v\in\PSH(X,\theta)$ and
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)\geq f\,dV,
 \qquad \mathrm{MA}^{\mathrm{ext}}_\theta(v)\geq g\,dV,
 \qquad f,g\geq0.
\]
For $0\leq t\leq1$ we have
\begin{equation}\label{eq:singular-convex-density}
 \mathrm{MA}^{\mathrm{ext}}_\theta(tu+(1-t)v)
 \geq\bigl(tf^{1/n}+(1-t)g^{1/n}\bigr)^n\,dV.
\end{equation}
\end{lemma}
\begin{proof}
The endpoints are immediate. For $0<t<1$, translate $u,v$ to be nonpositive and put $u_k=\max(u,-k)$ and $v_k=\max(v,-k)$. Semipositivity of $\theta$ makes these bounded $\theta$-plurisubharmonic functions. By locality,
\[
 \mathrm{MA}_\theta(u_k)\geq\mathbf1_{\{u>-k\}}f\,dV,
 \qquad
 \mathrm{MA}_\theta(v_k)\geq\mathbf1_{\{v>-k\}}g\,dV.
\]
Apply \cref{lem:nonclosed-mixed-density} to each mixed term in the positive expansion of $\theta_{tu_k+(1-t)v_k}^{,n}$. On
$E_k=\{u>-k\}\cap\{v>-k\}$ this gives exactly the density on the right of \eqref{eq:singular-convex-density}. On the same set, plurifine locality identifies the left side with the extended measure of $tu+(1-t)v$. Let $k\to\infty$. The sets $E_k$ exhaust the complement of the two pole sets, which have zero smooth volume. The asserted measure inequality follows by monotone convergence on Borel sets. No weak convergence of the unrestricted truncation measures was used.
\end{proof}

\begin{theorem}\label{thm:relative-normalization-concavity}
The functional $B_\varphi$ is concave on the real space $L^\infty(dV)$:
\[
 B_\varphi(tF+(1-t)G)
 \geq tB_\varphi(F)+(1-t)B_\varphi(G),\qquad0\leq t\leq1.
\]
\end{theorem}
\begin{proof}
Let $u,v\simeq\varphi$ solve the equations for $F,G$. Put
$H=tF+(1-t)G$ and $D=c_\varphi(F)^t c_\varphi(G)^{1-t}$. The preceding lemma and the arithmetic--geometric mean inequality give
\[
 \begin{split}
 \mathrm{MA}^{\mathrm{ext}}_\theta(tu+(1-t)v)
 &\geq\bigl(t(c_\varphi(F)e^F)^{1/n}
       +(1-t)(c_\varphi(G)e^G)^{1/n}\bigr)^n\,dV\\
 &\geq D e^H\,dV.
 \end{split}
\]
The averaged potential has ordinary type $\varphi$. If $c_\varphi(H)<D$, its measure dominates that of a solution for $H$ by a factor strictly greater than one. Apply singular strict domination to that solution and every constant translate of the averaged potential, as in the proof of \cref{prop:relative-normalization-order}. The same contradiction gives $c_\varphi(H)\geq D$. Taking logarithms proves concavity.
\end{proof}

This proof does not differentiate a weak solution. In the smooth Hermitian case it agrees with the differential calculation of \cref{thm:b-derivatives}. The Gauduchon method for smooth elliptic normalization constants also appears in \cite{Collins21}; the singular argument here instead uses the preceding existence and domination results.

\section{Continuity for bounded densities}

Uniform continuity alone would produce supporting measures on continuous functions, but would not exclude concentration on a set of zero volume. A stronger continuity statement excludes that concentration.

\begin{theorem}\label{thm:normalization-bounded-lone}
If $F_j,F$ are uniformly bounded and $F_j\to F$ in $L^1(dV)$, then
\[
 B_\varphi(F_j)\longrightarrow B_\varphi(F).
\]
\end{theorem}
\begin{proof}
Choose solutions $u_j\simeq\varphi$ normalized by $\sup_Xu_j=0$, and write $c_j=c_\varphi(F_j)$. If $|F_j|\leq M$, order and translation give
\[
 e^{-M}c_\varphi(0)\leq c_j\leq e^M c_\varphi(0).
\]
In particular their Monge--Amp\`ere measures are dominated by a fixed multiple of $dV$. The relative uniform estimate gives a constant $C$ such that
\[
 \varphi-C\leq u_j\leq\varphi.
\]
From any subsequence extract $c_j\to c>0$ and $u_j\to u$ in $L^1(X)$. The common-barrier continuity theorem gives convergence in capacity, $u\simeq\varphi$, and raw weak convergence of their measures. On the other hand, boundedness makes the exponential Lipschitz on the common range, so $c_je^{F_j}\to ce^F$ in $L^1(dV)$. Therefore
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)=ce^F\,dV.
\]
Scalar uniqueness gives $c=c_\varphi(F)$. Every subsequence has a further subsequence with this scalar limit, proving convergence of the full sequence and then of its logarithms.
\end{proof}

Only the measures of this particular family of solutions were bounded. Their domination and common barriers came from the equation and the relative estimate. There was no bound on masses of all bounded $\theta$-plurisubharmonic functions.

\section{Supporting probability measures}

Restrict $B_\varphi$ to the real Banach space $C(X)$, equipped with the uniform norm. For $F\in C(X)$, let $\mathcal A_\varphi(F)$ be the set of Borel probability measures $\nu$ satisfying
\begin{equation}\label{eq:adjoint-probability-set}
 B_\varphi(G)\leq B_\varphi(F)-\int_X(G-F)\,d\nu
 \qquad\text{for every }G\in C(X).
\end{equation}
These are the negatives of the supergradients of the concave functional. The notation denotes a set of measures; uniqueness is not part of the definition.

\begin{theorem}\label{thm:weak-adjoint-probabilities}
For every $F\in C(X)$, the set $\mathcal A_\varphi(F)$ is nonempty, convex and weakly compact. Every one of its measures is absolutely continuous with respect to $dV$.
\end{theorem}
\begin{proof}
We include the functional analysis. Write $C_\varphi=-B_\varphi$, a convex Lipschitz function. For a fixed $F$, the limit
\[
 p(h)=\lim_{t\downarrow0}
        \frac{C_\varphi(F+th)-C_\varphi(F)}{t}
\]
exists and is finite: convexity makes the difference quotients monotone in $t>0$, and their absolute values are at most $\|h\|_\infty$. Positive homogeneity is immediate. Applying convexity at the midpoint of $F+2th$ and $F+2tk$ and then letting $t\downarrow0$ gives $p(h+k)\leq p(h)+p(k)$. Thus $p$ is sublinear.

Hahn--Banach extends the zero functional on $\{0\}$ to a linear functional $\ell\leq p$. Since $p(h)\leq\|h\|_\infty$, application to $h$ and $-h$ makes $\ell$ continuous. The monotonicity of the convex difference quotients gives
\[
 C_\varphi(F+h)\geq C_\varphi(F)+\ell(h).
\]
The translation identity, tested with positive and negative constants, implies $\ell(1)=1$. If $h\geq0$, monotonicity gives
$C_\varphi(F-th)\leq C_\varphi(F)$ for $t>0$, whereas the supporting inequality gives the reverse lower bound $C_\varphi(F)-t\ell(h)$. Hence $\ell(h)\geq0$. By the Riesz representation theorem, $\ell(h)=\int_Xh\,d\nu$ for a positive probability measure $\nu$. This is exactly \eqref{eq:adjoint-probability-set}, proving nonemptiness. Each inequality in that definition specifies a weakly closed half-space in the compact space of probability measures. Their intersection is closed and convex, hence weakly compact.

It remains to prove absolute continuity. Let $K$ be compact with $dV(K)=0$. Choose continuous functions $0\leq\chi_j\leq1$ equal to one on $K$, whose supports have volumes tending to zero. For any $\nu\in\mathcal A_\varphi(F)$, the supporting inequality with $G=F+\chi_j$ gives
\[
 0\leq\nu(K)\leq\int_X\chi_j\,d\nu
 \leq B_\varphi(F)-B_\varphi(F+\chi_j).
\]
The right side tends to zero by \cref{thm:normalization-bounded-lone}. Thus $\nu(K)=0$. Inner regularity of a finite Borel measure on the compact manifold proves the same for every Borel set of zero volume. The Radon--Nikodym theorem now gives $d\nu=h_\nu dV$ with $h_\nu\geq0$ and $\int_Xh_\nu dV=1$.
\end{proof}

No bound for the densities $h_\nu$ in $L^p$, $p>1$, has been proved here. Even absolute continuity uses the bounded-$L^1$ continuity of the normalization functional; it would not follow just from its uniform Lipschitz bound.

\begin{proposition}[Stability of the supporting measures]
\label{prop:weak-adjoint-stability}
If $F_j\to F$ uniformly and $\nu_j\in\mathcal A_\varphi(F_j)$, every weak cluster point of $\nu_j$ belongs to $\mathcal A_\varphi(F)$. In particular, if the latter set consists of a single measure, $\nu_j$ converges to it.
\end{proposition}
\begin{proof}
Take a weakly convergent subsequence and fix $G\in C(X)$. In
\[
 B_\varphi(G)\leq B_\varphi(F_j)-\int_X(G-F_j)\,d\nu_j,
\]
uniform continuity of $B_\varphi$, uniform convergence of $F_j$ and weak convergence of the probabilities allow passage to the limit. The resulting inequality holds for every $G$, so the limiting measure is in $\mathcal A_\varphi(F)$. If that set is a singleton, every convergent subsequence has the same limit; compactness proves the final assertion.
\end{proof}

\section{Directional derivatives and the smooth identification}

The possible lack of uniqueness has an exact scalar meaning. For $F,G\in C(X)$, write $D^+B_\varphi(F)[G]$ and $D^-B_\varphi(F)[G]$ for the limits of the difference quotient as $t\downarrow0$ and $t\uparrow0$, respectively.

\begin{proposition}\label{prop:normalization-directional}
The one-sided derivatives exist, and
\begin{align*}
 D^+B_\varphi(F)[G]&=-\max_{\nu\in\mathcal A_\varphi(F)}\int_XG\,d\nu,\\
 D^-B_\varphi(F)[G]&=-\min_{\nu\in\mathcal A_\varphi(F)}\int_XG\,d\nu.
\end{align*}
Consequently $B_\varphi$ is G\^ateaux differentiable at $F$ if and only if $\mathcal A_\varphi(F)$ is a singleton. Its derivative is then $G\mapsto-\int_XG\,d\nu$.
\end{proposition}
\begin{proof}
Existence and finiteness of the one-sided limits follow from concavity and the Lipschitz bound. For $t>0$, every supporting measure at $F$ gives
\[
 \frac{B_\varphi(F+tG)-B_\varphi(F)}{t}
 \leq-\int_XG\,d\nu.
\]
Conversely choose $\nu_t\in\mathcal A_\varphi(F+tG)$ and apply its supporting inequality to $F$. This gives the lower bound $-\int_XG\,d\nu_t$ for the same quotient. Along a sequence $t\downarrow0$, extract a weak limit of $\nu_t$. It belongs to $\mathcal A_\varphi(F)$ by \cref{prop:weak-adjoint-stability}. The two bounds identify the right derivative with the negative maximum. Apply this identity to $-G$ to obtain the left derivative.

If the set is a singleton, the two derivatives coincide for every $G$ and equal the displayed continuous linear functional. Conversely, equality of the two one-sided derivatives for every $G$ forces all supporting probabilities to have identical integrals against every continuous function. The Riesz theorem makes them identical.
\end{proof}

\begin{theorem}[Recovery of the Gauduchon adjoint]
\label{thm:normalization-gauduchon-recovery}
Let $\theta=\omega$ be Hermitian, let $\varphi=0$, and let $F$ be smooth. If $u$ is the smooth normalized solution of \eqref{eq:relative-normalization}, then
\[
 \mathcal A_0(F)=\{\mu_u\},\qquad
 d\mu_u=\rho_u\omega_u^n,\quad
 \ddc(\rho_u\omega_u^{n-1})=0,\quad\mu_u(X)=1.
\]
For $n=1$ the same assertion uses $\mu_u=\omega_u/\int_X\omega_u$.
\end{theorem}
\begin{proof}
In dimensions at least two, \cref{thm:b-derivatives} shows that for every smooth real $G$,
\[
 \left.\frac{d}{dt}\right|_{t=0}B_0(F+tG)
 =-\int_XG\,d\mu_u.
\]
Scalar uniqueness identifies its normalizing constant with the present $B_0$. For any $\nu\in\mathcal A_0(F)$, testing the supporting inequality at $F+tG$ for both signs of $t$ gives equality of the integrals of $G$ against $\nu$ and $\mu_u$. Smooth functions are uniformly dense in $C(X)$, so $\nu=\mu_u$. Nonemptiness proves the assertion. In dimension one Stokes gives
$c_0(F)=\int_X\omega/\int_Xe^F dV$, whose logarithmic derivative gives the stated measure directly.
\end{proof}

Thus for a continuous $F$ in the Hermitian case, smooth approximations $F_j\to F$ uniformly produce Gauduchon adjoint probabilities whose weak cluster points all belong to $\mathcal A_0(F)$ and are absolutely continuous. If $\mathcal A_0(F)$ is a singleton, the weak limit is independent of this approximation. This is a conditional answer to the question in \cref{chap:gauduchon}, for approximations controlled through the logarithmic density.

\section{The closed case and the remaining questions}

When $\theta$ is K\"ahler, the ordinary singularity type $\varphi$ has a fixed non-pluripolar mass
$m_\varphi>0$ under the hypotheses above, by the closed-background theory of \cite{SGPT}. Integrating the equation gives
\[
 B_\varphi(F)=\log m_\varphi-\log\int_Xe^F\,dV,
 \qquad
 \mathcal A_\varphi(F)
 =\left\{\frac{e^F\,dV}{\int_Xe^F\,dV}\right\}.
\]
The formula follows by differentiation, or by the supporting inequalities and the two-sided derivative argument. In the Hermitian case the total Monge--Amp\`ere mass need not be fixed on an ordinary type, so this computation does not determine $B_\varphi$.

The first remaining question is whether $\mathcal A_\varphi(F)$ is a singleton for every continuous $F$ under \eqref{eq:normalization-reference}. Equivalently, is $B_\varphi$ G\^ateaux differentiable everywhere on $C(X)$? We have proved this for smooth data in a Hermitian background and for continuous data in the closed K\"ahler case. The arguments above do not prove it for a degenerate background or a singular reference.

A second question concerns the geometric interpretation of a supporting probability. Can one define a linearized operator at an appropriate weak solution so that its adjoint annihilates this probability? The smooth expression $\ddc(\rho\theta_u^{n-1})$ cannot simply be written with an arbitrary $L^1$ density $\rho$ and an unbounded product: existence of the product and its compatibility with approximation must first be proved. A third question is how the sets $\mathcal A_\varphi(F)$ vary when the prescribed singularity type changes.

These are proposed research questions, without a claim that they are new. The proved construction assigns supporting probabilities through the scalar equation. It does not furnish a primitive of the raw Monge--Amp\`ere one-form on potentials: \cref{chap:energy} identifies a separate differential obstruction to that primitive.
