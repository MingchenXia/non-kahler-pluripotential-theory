Run_id: semipositive_dual_current_rate_01

Statement: Check the quantitative current-convergence supplement frozen in research/editorial/section_semipositive_trace_rate.tex under /Users/mingchen/Non-Kahler. It proposes a global O(lambda) total-variation estimate for the full Gauduchon trace measure, and local O(sqrt(lambda)) coefficient-total-variation convergence of the full currents off the analytic degeneracy set. No novelty claim. This is OUTSIDE checked checkpoint50 until separately checked.

Accepted sources: book/author/section_semipositive_dual_attainment.tex (correct reports semipositive_dual_attainment_01 and semipositive_dual_uniqueness_01), and book/author/section_semipositive_exponential_limit.tex (correct report semipositive_dual_consequences_01). Accept their exact hypotheses and conclusions. The latter supplies c_lambda>=b, uniform nu-moments of -v_lambda, the common lower barrier, and L1 convergence. The former supplies A0=a gamma and nu=A0 wedge T on X minus Z, with global trace equality. Read the exact all-Hermitian trace inequality in section_threshold_trace_saturation.tex and the measurable-matrix argument in section_smooth_dual_regularity.tex. The new proof cites only these internal results and elementary linear algebra. Do not edit frozen sources, any previous result or verifier memory.

Check especially: q_lambda nu <= A_lambda wedge T, both trace probabilities mass one, and the exact total-variation estimate by twice the negative density discrepancy. There is no cancellation of infinite masses. c_lambda>=b bounds (1-q_lambda)_+ by 1-exp(lambda v_lambda/n), and 1-exp(-x)<=x gives the uniform O(lambda) estimate from the existing moment. Separately control both the positive residual mass and the root-density L1 difference.

On U=X minus Z, decompose the positive (1,1)-current into its ac matrix density relative to gamma and a positive singular matrix measure. Passing the all-Hermitian tests to the ac part gives det(B)^(1/n)>=alpha=q a. The trace error controls delta=tr(B)/n-alpha and the singular trace. Check every n factor. For eigenvalues l_i>=0 with geometric mean>=alpha, AM-GM gives sum sqrt(l_i)>=n sqrt(alpha); hence sum(sqrt(l_i)-sqrt(alpha))^2<=n(s-alpha), and Cauchy--Schwarz gives sum|l_i-alpha|<=2n sqrt(s(s-alpha)). Integrate using integral s gamma^n<=1 and integral delta gamma^n=O(lambda). Control the singular part by n times its trace mass. The alpha-a term has integral O(lambda) by nu=a gamma^n on U. Compare gamma and the fixed metric only on K compactly contained in U. No global coefficient norm estimate across Z is claimed. No potential rate, MA density rate, capacity convergence or nonlinear current-product continuity is asserted.

Proof:

\subsection{Quantitative convergence of the currents}

The same trace error controls more than the scalar. Here total variation of the coefficients of a current is measured in any fixed smooth Hermitian metric; on a relatively compact coordinate chart this is equivalent to the sum of the total variations of its coefficient measures.

\begin{proposition}\label{prop:semipositive-dual-current-rate}
Under the hypotheses and notation of \cref{prop:semipositive-dual-exponential-limit}, put
\[
 A_\lambda=\omega+\ddc v_\lambda,\qquad
 A_0=\omega+\ddc u_0.
\]
There is a constant $C$ such that
\[
 \|A_\lambda\wedge T-A_0\wedge T\|_{\mathrm{TV}}
       \leq C\lambda\qquad(\lambda>0).
\]
For each $K\Subset X\setminus Z$, there is a constant $C_K$ such that
\[
 \|A_\lambda-A_0\|_{\mathrm{TV}(K)}
       \leq C_K\sqrt\lambda\qquad(0<\lambda\leq1).
\]
\end{proposition}
\begin{proof}
Use the probability $\nu=A_0\wedge T=b^{1/n}p k_T\,\mathrm{d}V$ from the preceding limit proof, and set
\[
 q_\lambda=(c_\lambda/b)^{1/n}\mathrm{e}^{\lambda v_\lambda/n},
 \qquad R_\lambda=A_\lambda\wedge T-q_\lambda\nu\geq0.
\]
The same proof gives $c_\lambda\geq b$ and $\int_X(-v_\lambda)\,\mathrm{d}\nu\leq C_0$. Therefore
\[
 (1-q_\lambda)_+\leq1-\mathrm{e}^{\lambda v_\lambda/n},
 \qquad
 \int_X(1-q_\lambda)_+\,\mathrm{d}\nu\leq C_0\lambda/n.
\]
Since $A_\lambda\wedge T$ and $\nu$ both have mass one,
\[
 \|A_\lambda\wedge T-\nu\|_{\mathrm{TV}}
 \leq R_\lambda(X)+\int_X|q_\lambda-1|\,\mathrm{d}\nu
 =2\int_X(1-q_\lambda)_+\,\mathrm{d}\nu.
\]
This proves the first estimate and also gives
$R_\lambda(X)\leq C_0\lambda/n$ and
$\int_X|q_\lambda-1|\,\mathrm{d}\nu\leq2C_0\lambda/n$.

On $U=X\setminus Z$, write $T=\gamma^{n-1}$ and $A_0=a\gamma$ as in the exactness theorem. Put $\alpha_\lambda=q_\lambda a$. Decompose the positive current $A_\lambda$ into its absolutely continuous matrix density $B_\lambda$ relative to $\gamma$ and its positive singular part. The all-Hermitian trace inequalities imply
\[
 (\det B_\lambda)^{1/n}\geq\alpha_\lambda
 \quad\text{almost everywhere on }U.
\]
This is a matrix determinant statement; no nonlinear product of coefficient measures is involved. Put $s_\lambda=\operatorname{tr}B_\lambda/n$ and $\delta_\lambda=s_\lambda-\alpha_\lambda\geq0$. The trace error has absolutely continuous part $\delta_\lambda\gamma^n$, and its singular part is the trace of the singular part of $A_\lambda$. Thus
\[
 \int_U s_\lambda\gamma^n\leq1,\qquad
 \int_U\delta_\lambda\gamma^n\leq C_0\lambda/n,
\]
and the singular trace mass on $U$ has the same upper bound.

For nonnegative eigenvalues $\ell_1,\ldots,\ell_n$ with geometric mean at least $\alpha\geq0$ and arithmetic mean $s$, arithmetic--geometric mean and Cauchy--Schwarz give
\[
 \sum_i(\sqrt{\ell_i}-\sqrt\alpha)^2\leq n(s-\alpha),
 \qquad
 \sum_i|\ell_i-\alpha|\leq2n\sqrt{s(s-\alpha)}.
\]
Indeed $\sum_i\sqrt{\ell_i}\geq n\sqrt\alpha$, while
$\sum_i(\sqrt{\ell_i}+\sqrt\alpha)^2\leq4ns$.
Apply this to $B_\lambda$ and integrate, using Cauchy--Schwarz once more. The absolutely continuous part of $A_\lambda-\alpha_\lambda\gamma$ has integrated matrix trace norm at most $2n\sqrt{C_0\lambda/n}$. Its singular part has norm at most $C_0\lambda$ in the same metric. Finally
\[
 \int_U|\alpha_\lambda-a|\gamma^n
   =\int_U|q_\lambda-1|\,\mathrm{d}\nu
   \leq2C_0\lambda/n.
\]
These estimates give the second conclusion after comparing $\gamma$ with the fixed metric on $K$ and using $\lambda\leq\sqrt\lambda$.
\end{proof}

The second estimate is local away from the degeneracy set. Neither estimate gives a rate for the potentials or for their Monge--Amp\`ere measures, or proves capacity convergence across $Z$.
