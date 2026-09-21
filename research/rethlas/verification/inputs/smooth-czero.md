Run_id: smooth_czero_01

Statement: Audit the complete pointwise torsion estimate, weighted gradient estimate (especially the finite recurrence replacing the original induction), Sobolev iteration and normalized C0 bound in the following proof. Fix a connected compact Hermitian manifold, ddc=i/(2pi) partial bar-partial. The only global assumptions on u are smoothness, strict omega-psh positivity, sup_X u=0, and MA_omega(u)<=Lambda omega^n. No BMP, PVP, positive lower density or closedness is assumed. Accepted inputs: usual fixed-metric Sobolev inequality; the normalized L1 bound for omega-psh potentials, proved and independently audited in compactness_regularization_01; Stokes and elementary linear algebra. In particular, DO NOT import the Cherrier/Tosatti-Weinkove gradient estimate or C0 estimate: the supplied reconstruction must prove them. Check every sign, derivative of a mixed non-closed wedge, Young-inequality coefficient and all absorptions as p grows. The n=1 and n=2 empty-sum cases are included. The source TW10 is available at /Users/mingchen/Non-Kahler/research/sources/TW10.pdf and TW10.txt for attribution; its normalization differs. The proof's finite recurrence is written differently from the source and needs its own check. No higher-order estimate or continuity-method existence assertion is part of this bounded audit.

Proof:



The essential global estimate only needs an upper bound for the density. We follow the weighted integration method of Cherrier and Tosatti--Weinkove \cite{Cherrier87,TW10}. A finite recurrence will absorb the torsion terms. The normalized compactness theorem then finishes the argument after Sobolev iteration.

\begin{lemma}[A pointwise torsion estimate]\label{lem:pointwise-torsion-estimate}
There is a constant $C$ depending on $\omega$ such that, for every positive $(1,1)$-form $\eta$, every smooth real $f$, every $\delta>0$, and $0\leq k\leq n-2$,
\[
 \begin{split}
 |\dc f\wedge d\omega\wedge\eta^k\wedge\omega^{n-k-2}|
 \leq{}&\frac C\delta\,df\wedge\dc f\wedge\eta^k\wedge\omega^{n-k-1}\\
 &+C\delta\,\eta^k\wedge\omega^{n-k}.
 \end{split}
\]
The absolute value means that of the coefficient relative to the positive volume form $\omega^n$.
\end{lemma}
\begin{proof}
At the point in question choose an $\omega$-unitary frame in which $\eta$ is diagonal, with positive eigenvalues $\lambda_1,\ldots,\lambda_n$. Expand $\eta^k$ as a sum over $k$-element subsets $I$, with coefficient a positive dimensional multiple of $\lambda_I=\prod_{i\in I}\lambda_i$. A surviving coefficient from $\dc f\wedge d\omega$ has the form of a bounded coefficient of $d\omega$ times one first derivative $f_a$, where $a\notin I$. Young's inequality bounds its absolute value by
\[
 C\lambda_I|f_a|\leq (C/\delta)\lambda_I|f_a|^2
                              +C\delta\lambda_I.
\]
The sum of the first terms is bounded by a fixed multiple of the first positive form in the assertion: its diagonal expansion contains precisely the terms $\lambda_I|f_a|^2$ with $a\notin I$. The second positive form contains all the $\lambda_I$. Finitely many indices and the uniform bound for $d\omega$ give a uniform $C$. The normalization of $\dc$ changes only this constant.
\end{proof}

\begin{lemma}[Weighted gradient estimate]\label{lem:cherrier-gradient}
Suppose $u$ is smooth, $\eta=\omega+\ddc u>0$, and
$\eta^n\leq\Lambda\omega^n$ for a fixed $\Lambda>0$. There are constants $p_0\geq1$ and $C$ depending only on $\omega$ and $\Lambda$ such that
\[
 \int_Xd(e^{-pu/2})\wedge\dc(e^{-pu/2})\wedge\omega^{n-1}
 \leq Cp\int_Xe^{-pu}\omega^n\quad(p\geq p_0).
\]
\end{lemma}
\begin{proof}
For a fixed $p\geq1$, abbreviate
\[
 M_k=\int_Xe^{-pu}\eta^k\wedge\omega^{n-k},\qquad
 J_k=\int_Xe^{-pu}du\wedge\dc u\wedge\eta^k\wedge\omega^{n-k-1},
 \quad J=\sum_{k=0}^{n-1}J_k.
\]
All these numbers are nonnegative. Let
$T=\sum_{k=0}^{n-1}\eta^k\wedge\omega^{n-k-1}$. Since $d\eta=d\omega$, differentiation gives
\[
 dT=n\sum_{k=0}^{n-2}\eta^k\wedge\omega^{n-k-2}\wedge d\omega.
\]
The sum is empty when $n=1$. Stokes' theorem gives the exact identity
\[
 \begin{split}
 \int_Xe^{-pu}(\eta^n-\omega^n)
 &=\int_Xe^{-pu}\ddc u\wedge T\\
 &=pJ+\int_Xe^{-pu}\dc u\wedge dT.
 \end{split}
\]
The density assumption bounds the left side above by $(\Lambda+1)M_0$. Apply \cref{lem:pointwise-torsion-estimate} to the last integral, and choose $\delta=K/p$ for a sufficiently large fixed $K$. The contribution proportional to $J/\delta$ is then at most $pJ/2$. After absorption we obtain
\begin{equation}\label{eq:weighted-first-bound}
 pJ\leq CM_0+\frac Cp\sum_{k=0}^{n-2}M_k.
\end{equation}
This estimate alone is not enough, because the mixed weighted masses on the right have not been bounded.

For $1\leq k\leq n-2$, a second integration by parts gives
\begin{equation}\label{eq:weighted-recurrence}
 M_k-M_{k-1}=pJ_{k-1}+R_k,
 \qquad
 R_k=\int_Xe^{-pu}\dc u\wedge
                d(\eta^{k-1}\wedge\omega^{n-k}).
\end{equation}
The derivative in $R_k$ has two terms, with coefficients $k-1$ and $n-k$. Apply the pointwise estimate with $\delta=1/p$ to each of them. Omitting nonexistent negative indices yields
\[
 |R_k|\leq Cp(J_{k-2}+J_{k-1})
                   +\frac Cp(M_{k-2}+M_{k-1}),
 \qquad M_{-1}=J_{-1}=0.
\]
Consequently, for $p\geq1$,
\[
 M_k\leq C(M_{k-1}+M_{k-2}+pJ).
\]
Induction over the finitely many values of $k$ proves
\[
 \sum_{k=0}^{n-2}M_k\leq C(M_0+pJ).
\]
For $n=2$ this is immediate, and for $n=1$ the sum is empty. Inserting this bound in \eqref{eq:weighted-first-bound} gives
$pJ\leq CM_0+C'J$. Taking $p\geq2C'$ absorbs the last term and proves $pJ\leq CM_0$.

Finally,
\[
 \int_Xd(e^{-pu/2})\wedge\dc(e^{-pu/2})\wedge\omega^{n-1}
 =\frac{p^2}{4}J_0\leq\frac{p^2}{4}J\leq CpM_0.
\]
Every integration is between smooth forms, and the only derivatives of the background were estimated explicitly.
\end{proof}

\begin{theorem}[An upper density controls the potential]\label{thm:smooth-czero}
For each $\Lambda>0$ there is $C_\Lambda$ such that every smooth $u$ with
\[
 \omega+\ddc u>0,\qquad \sup_Xu=0,\qquad
 (\omega+\ddc u)^n\leq\Lambda\omega^n
\]
satisfies $\|u\|_\infty\leq C_\Lambda$.
\end{theorem}
\begin{proof}
Let $d\mu=\omega^n/\int_X\omega^n$. The usual Sobolev inequality for the fixed Riemannian metric of $\omega$ gives, for some $\beta>1$,
\[
 \left(\int_X |w|^{2\beta}\,d\mu\right)^{1/\beta}
 \leq C\left(\int_Xdw\wedge\dc w\wedge\omega^{n-1}
                         +\int_X|w|^2\,d\mu\right).
\]
We may take $\beta=n/(n-1)$ if $n\geq2$, and for example $\beta=2$ if $n=1$. Apply this to $w=e^{-pu/2}$ and use \cref{lem:cherrier-gradient}. With $Z=e^{-u}$ we get
\[
 \|Z\|_{L^{p\beta}(\mu)}\leq(Cp)^{1/p}\|Z\|_{L^p(\mu)}
 \quad(p\geq p_0).
\]
Iterate at $p=p_0\beta^j$. The product of the constants is finite because
$\sum_j(1+\log(p_0\beta^j))/(p_0\beta^j)<\infty$. Hence, for a uniform $C_1\geq1$ and $m=\inf_Xu$,
\begin{equation}\label{eq:near-minimum-integral}
 e^{-p_0m}\leq C_1\int_Xe^{-p_0u}\,d\mu.
\end{equation}
This still involves the unknown potential on the right. Divide by $e^{-p_0m}$ and set $A=p_0^{-1}\log(2C_1)$. The integrand $e^{-p_0(u-m)}$ is at most one everywhere and at most $(2C_1)^{-1}$ outside $S=\{u\leq m+A\}$. Therefore \eqref{eq:near-minimum-integral} implies
\[
 \mu(S)\geq\frac1{2C_1}=:\delta>0.
\]
By \cref{thm:normalized-compactness}, $\int_X(-u)\,d\mu\leq C_0$. On $S$ we have $-u\geq-m-A$, so
\[
 C_0\geq\int_X(-u)\,d\mu\geq\delta(-m-A)
\]
when $-m\geq A$; otherwise the desired bound is immediate. Thus $-m\leq A+C_0/\delta$, proving the theorem.
\end{proof}

Neither the gradient estimate nor its consequence uses a uniform upper bound for the masses of all potentials. The density bound applies to the particular solutions being studied. This is why the estimate remains compatible with \cref{thm:hopf-unbounded}.

