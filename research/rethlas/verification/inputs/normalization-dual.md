Run_id: normalization_dual_01

Statement: Audit the new duality supplement below, step by step, including all conclusions about weak-L1 compactness, measurable equivalence classes and infinite values. Compact connected complex X, theta semipositive big, phi=Ptheta[phi] with genuine smaller-background envelope, dV smooth positive. No BMP or uniform positive lower mass. New H on probability measures is the continuous-test convex dual of the log normalizer B. Claims: attained dual minimum, finite sublevels uniformly absolutely continuous and weak-L1 sequentially compact; existence and stability of supporting measures for bounded measurable logarithmic densities; closed-case entropy formula with nonnormalized dV; change of reference volume. No new global nonlinear PDE input is required.

Accepted inputs: The preceding normalization chapter up to the dual supplement, verified correct in normalization_functional_01: B finite on L-infinity, concave, decreasing, constant-translation rule, supnorm 1-Lipschitz, continuity for uniformly bounded sequences converging in L1(dV); nonempty supporting probability sets on C(X); their finite dual identity can be derived as below. Its PDE prerequisites have separately passed prescribed_lp_existence_01 and supporting audits. Standard compact-space measure regularity, continuous cutoff approximation, Radon-Nikodym, weak compactness of probabilities, Jensen and elementary integration are accepted. The closed Kähler fixed positive ordinary-type mass under the stated hypotheses is an accepted SGPT input. Read book chapter_normalization.tex for definitions, but audit only the supplement below. No novelty or formal certification claim. Check all assumptions and infinite-value conventions. Book source read-only. Save usual report.

Proof:

\section{A convex functional on probability measures}

The scalar functional also has a dual description. This gives a variational problem in the prescribed density and a useful compactness statement for its supporting measures. The variable in this problem is a probability measure.

Let $\mathcal P(X)$ denote the Borel probability measures on $X$. Define
\begin{equation}\label{eq:normalization-dual-definition}
 H_\varphi(\nu)
 =\sup_{G\in C(X)}\left(B_\varphi(G)+\int_XG\,d\nu\right),
 \qquad \nu\in\mathcal P(X).
\end{equation}
The value $+\infty$ is allowed. Taking $G=0$ shows that
$H_\varphi\geq B_\varphi(0)$, so the value $-\infty$ never occurs.

\begin{proposition}\label{prop:normalization-dual}
The functional $H_\varphi$ is convex and weakly lower semicontinuous. For every $F\in C(X)$,
\begin{equation}\label{eq:normalization-dual-minimum}
 B_\varphi(F)
 =\min_{\nu\in\mathcal P(X)}
       \left(H_\varphi(\nu)-\int_XF\,d\nu\right).
\end{equation}
The minimizers are exactly $\mathcal A_\varphi(F)$.
\end{proposition}
\begin{proof}
Every function of $\nu$ in the supremum defining $H_\varphi$ is affine and weakly continuous. Their supremum is convex and lower semicontinuous. The definition gives
$H_\varphi(\nu)-\int_XF\,d\nu\geq B_\varphi(F)$.
Equality holds precisely when
\[
 B_\varphi(G)+\int_XG\,d\nu
 \leq B_\varphi(F)+\int_XF\,d\nu
 \quad\text{for every }G\in C(X).
\]
This is the defining inequality for $\mathcal A_\varphi(F)$. Its nonemptiness, proved in \cref{thm:weak-adjoint-probabilities}, proves attainment.
\end{proof}

\begin{theorem}[Compactness of dual sublevels]\label{thm:normalization-dual-compactness}
For every finite real $L$, the set
\[
 \mathcal K_L=\{\nu\in\mathcal P(X):H_\varphi(\nu)\leq L\}
\]
is weakly compact. Its measures are uniformly absolutely continuous with respect to $dV$: for every $\epsilon>0$ there is a $\delta>0$ such that
\begin{equation}\label{eq:normalization-dual-uniform-ac}
 dV(E)<\delta\quad\Longrightarrow\quad
 \sup_{\nu\in\mathcal K_L}\nu(E)<\epsilon
\end{equation}
for every Borel set $E$. In particular, writing $d\nu=h_\nu dV$, the densities in this set are uniformly integrable in $L^1(dV)$. On $\mathcal K_L$, weak convergence of measures also implies weak convergence of their densities in $L^1(dV)$.
\end{theorem}
\begin{proof}
Weak compactness follows from lower semicontinuity and compactness of $\mathcal P(X)$. The empty sublevel is harmless; otherwise $L\geq B_\varphi(0)$.
Fix $t>0$. By \cref{thm:normalization-bounded-lone} there is $\delta_t>0$ such that
\[
 0\leq\chi\leq1,\quad \chi\in C(X),\quad
 \int_X\chi\,dV<\delta_t
 \quad\Longrightarrow\quad
 B_\varphi(t\chi)>B_\varphi(0)-1.
\]
Indeed, failure would give a sequence of such $\chi$ tending to zero in $L^1$, contrary to that theorem. For $\nu\in\mathcal K_L$, the defining supremum gives
\[
 t\int_X\chi\,d\nu
 \leq L-B_\varphi(t\chi)
 <L-B_\varphi(0)+1.
\]
Choose $t$ so large that the last numerator divided by $t$ is less than $\epsilon$. If $dV(E)<\delta_t/2$, outer regularity supplies an open neighborhood $O$ of $E$ with $dV(O)<\delta_t$. For any compact $K\subset E$, choose a continuous cutoff equal to one on $K$, between zero and one, and supported in $O$. The last inequality gives $\nu(K)<\epsilon$, uniformly in $\nu$. Inner regularity gives the same bound for $E$, with a non-strict inequality. Choosing $t$ initially with bound $\epsilon/2$ proves \eqref{eq:normalization-dual-uniform-ac} as stated.

This proves absolute continuity of every measure in the sublevel, and the uniform small-set criterion for the densities, whose integrals all equal one. These two facts are exactly uniform integrability on a finite measure space.

Finally suppose $\nu_j\to\nu$ weakly within the sublevel. For a bounded measurable $G$, choose continuous $G_k$ with
$|G_k|\leq\|G\|_\infty$ and $G_k\to G$ in $dV$-measure. Such approximations follow, for example, by approximating simple functions using regularity and continuous cutoffs. Uniform absolute continuity gives
\[
 \sup_{\sigma\in\mathcal K_L}\int_X|G_k-G|\,d\sigma\longrightarrow0.
\]
To see this, split into $\{|G_k-G|\leq a\}$ and its complement; the first integral is at most $a$, and the second is bounded by $2\|G\|_\infty$ times a uniformly small measure. For fixed $k$, weak convergence applies to $G_k$. Passing first $j\to\infty$ and then $k\to\infty$ proves convergence against $G$. This is precisely weak $L^1(dV)$ convergence of the densities. In particular every sequence in the sublevel has a weakly convergent $L^1$ subsequence.
\end{proof}

This compactness is obtained from the continuity of the equation's normalizing constant. It uses no uniform bound on Monge--Amp\`ere masses of arbitrary bounded potentials. It does not give a common $L^p$ bound for the densities, for any $p>1$.

\section{Bounded measurable densities and stability}

The preceding construction extends to the bounded measurable functions on which $B_\varphi$ was originally defined. No finitely additive measures are needed.

\begin{theorem}\label{thm:normalization-measurable-adjoint}
For every $F\in L^\infty(dV)$ there is a nonempty set of absolutely continuous probability measures, again denoted $\mathcal A_\varphi(F)$, characterized by
\begin{equation}\label{eq:measurable-adjoint-support}
 B_\varphi(G)\leq B_\varphi(F)-\int_X(G-F)\,d\nu
 \qquad\text{for every }G\in L^\infty(dV).
\end{equation}
For continuous $F$, this agrees with the preceding definition. Formula \eqref{eq:normalization-dual-minimum} holds for bounded measurable $F$ as well, with these measures as its minimizers. In that formula the objective is declared to be $+\infty$ whenever $H_\varphi(\nu)=+\infty$; otherwise $\nu$ is absolutely continuous and the integral of the $L^\infty$ class $F$ is well defined.

Suppose $F_j,F$ are uniformly bounded and $F_j\to F$ in $L^1(dV)$. If $\nu_j\in\mathcal A_\varphi(F_j)$, their densities are uniformly integrable. Every weak $L^1$ cluster point belongs to $\mathcal A_\varphi(F)$. If the latter is a singleton, the full sequence converges to it weakly in $L^1(dV)$.
\end{theorem}
\begin{proof}
First, if $H_\varphi(\nu)<\infty$, the measure $\nu$ is absolutely continuous by \cref{thm:normalization-dual-compactness}. A bounded measurable $G$ admits uniformly bounded continuous approximations $G_k\to G$ in $L^1(dV)$. Absolute continuity and the common bound imply $\int_XG_k\,d\nu\to\int_XG\,d\nu$. Together with \cref{thm:normalization-bounded-lone}, this proves
\begin{equation}\label{eq:dual-measurable-tests}
 H_\varphi(\nu)
 =\sup_{G\in L^\infty(dV)}
       \left(B_\varphi(G)+\int_XG\,d\nu\right)
\end{equation}
for such $\nu$. Values of measurable functions are understood modulo $dV$-null sets. The finite-dual measures are absolutely continuous, so their integrals are well defined on these equivalence classes.

Choose continuous $F_j$ with $|F_j|\leq M=\|F\|_\infty$ and $F_j\to F$ in $L^1(dV)$, and choose $\nu_j\in\mathcal A_\varphi(F_j)$. The preceding duality and Lipschitz bound give
\[
 H_\varphi(\nu_j)
 =B_\varphi(F_j)+\int_XF_j\,d\nu_j
 \leq B_\varphi(0)+2M.
\]
Thus a subsequence converges weakly in $L^1$ to a probability measure $\nu$. Uniform absolute continuity gives
\[
 \int_X|F_j-F|\,d\nu_j\longrightarrow0.
\]
Here again one splits at a fixed small positive threshold; the exceptional sets have $dV$-measure tending to zero. Since $F$ is bounded measurable, weak $L^1$ convergence applies to its integral. Lower semicontinuity and continuity of $B_\varphi$ yield
\[
 H_\varphi(\nu)
 \leq\liminf_j H_\varphi(\nu_j)
 =B_\varphi(F)+\int_XF\,d\nu.
\]
The reverse inequality follows from \eqref{eq:dual-measurable-tests}. Equality and that same supremum formula prove \eqref{eq:measurable-adjoint-support} and the minimum formula.

For continuous $F$, every measure in the old supporting set has finite dual value by \cref{prop:normalization-dual}, so \eqref{eq:dual-measurable-tests} extends all its inequalities to bounded measurable tests. This proves agreement of the definitions. Conversely, an absolutely continuous probability satisfying \eqref{eq:measurable-adjoint-support} has finite dual value and achieves the minimum. Hence the characterization is exact.

For the stability assertion, begin with the stated $F_j,\nu_j$ rather than with an approximating construction. The common uniform bound again places all $\nu_j$ in a single finite sublevel of $H_\varphi$. The same compactness and limiting argument show that every weak $L^1$ cluster point achieves the minimum for $F$. If the minimizing set is a singleton, subsequence compactness forces convergence of the full sequence to that measure. No strong $L^1$ convergence is asserted.
\end{proof}

The dual set therefore extends the smooth Gauduchon adjoint to bounded logarithmic densities, with a precise form of stability. Its possible failure to be a singleton remains a separate question.

\section{Entropy in the closed case}

If $\theta$ is K\"ahler, the ordinary type $\varphi$ has a fixed non-pluripolar mass $m_\varphi>0$ under the standing hypotheses, by the closed-background theory of \cite{SGPT}. Integrating the equation gives
\begin{equation}\label{eq:normalization-closed-formula}
 B_\varphi(F)=\log m_\varphi-\log\int_Xe^F\,dV,
 \qquad
 \mathcal A_\varphi(F)
 =\left\{\frac{e^F\,dV}{\int_Xe^F\,dV}\right\}.
\end{equation}
The second identity follows by differentiating in bounded directions and testing the supporting inequality with both signs of the parameter.

For a probability measure $\nu=h\,dV$, define
\[
 \operatorname{Ent}_{dV}(\nu)=\int_Xh\log h\,dV,
 \qquad 0\log0=0,
\]
and set its entropy to $+\infty$ if it is not absolutely continuous. This entropy may be negative when $dV(X)\ne1$, but its negative part is finite since $h\log h\geq-e^{-1}$.

\begin{proposition}\label{prop:normalization-dual-entropy}
In the closed case,
\[
 H_\varphi(\nu)=\log m_\varphi+\operatorname{Ent}_{dV}(\nu).
\]
Thus the minimum formula becomes the usual entropy variational formula for the logarithmic integral in \eqref{eq:normalization-closed-formula}.
\end{proposition}
\begin{proof}
If $\nu$ is singular with respect to $dV$ in the sense that it is not absolutely continuous, \cref{thm:normalization-dual-compactness} gives $H_\varphi(\nu)=+\infty$. Suppose $d\nu=h\,dV$. For finite entropy, Jensen's inequality for the concave logarithm, with probability measure $\nu$, gives for bounded $F$
\[
 \int_X F\,d\nu-\int_Xh\log h\,dV
 =\int_{\{h>0\}}\log\frac{e^F}{h}\,d\nu
 \leq\log\int_{\{h>0\}}e^F\,dV
 \leq\log\int_Xe^F\,dV.
\]
An approximation proves the same inequality if a logarithm is initially unbounded. If entropy is infinite, the resulting upper bound for $H_\varphi$ is automatic. Taking the supremum yields
$H_\varphi(\nu)\leq\log m_\varphi+\operatorname{Ent}_{dV}(\nu)$.

For the reverse inequality, put
\[
 F_k=\log\bigl(\max\{k^{-1},\min\{h,k\}\}\bigr),\qquad k\geq1.
\]
Then $\int_Xe^{F_k}\,dV\to\int_Xh\,dV=1$ by truncation in $L^1$. Also
$\int_XF_k\,d\nu\to\int_Xh\log h\,dV$, with the value $+\infty$ allowed: the positive part increases to the positive part of $h\log h$, and the negative part converges by domination by its integrable negative part. For each fixed $k$, approximate $F_k$ by continuous functions with the same bounds in $L^1(dV+\nu)$. Their exponential integrals and their $\nu$-integrals converge to those of $F_k$. Therefore the continuous supremum defining $H_\varphi$ is at least
\[
 \log m_\varphi-\log\int_Xe^{F_k}\,dV+\int_XF_k\,d\nu.
\]
Letting $k\to\infty$ proves the reverse inequality, including infinite entropy.
\end{proof}

The reference volume is part of this dual functional. If it is replaced by $dV'=e^a dV$ for a continuous real $a$, then
\[
 B'_\varphi(F)=B_\varphi(F+a),\qquad
 H'_\varphi(\nu)=H_\varphi(\nu)-\int_Xa\,d\nu.
\]
The first identity follows from the equation; the second follows by the change of variable $G=F+a$ in the defining supremum. The displayed identity for the dual is valid with infinite values as well. In a nonclosed background, $H_\varphi$ is still defined by the same supremum, but total mass need not be fixed on an ordinary type, so the entropy computation does not determine it.
