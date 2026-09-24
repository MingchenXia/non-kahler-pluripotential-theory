Run_id: smooth_prescribed_masses_01

Statement: Verify the corollary and proof below, including all quantifiers and its two concluding special cases. This is a bounded verification under the stated accepted internal inputs, not a whole-book audit or a novelty claim. Use the normal verification workflow and persist the full final report.

Conventions and accepted earlier inputs:
- X is a connected compact complex manifold of complex dimension n>=1, omega is a smooth positive Hermitian (1,1) form, gamma is a smooth positive Gauduchon form satisfying dd^c gamma^(n-1)=0. dd^c=i/(2 pi) partial bar-partial. dV is a fixed smooth positive probability volume. A smooth real u is omega-psh if omega+dd^c u is nonnegative.
- M=int_X omega wedge gamma^(n-1). For a real (1,1) form T with integrable coefficients, A_T is its Hermitian matrix relative to gamma, |A_T|=(A_T^2)^(1/2), and ||T||_L1(gamma)=(1/n)int_X tr|A_T| gamma^n. For T>=0 this equals int_X T wedge gamma^(n-1). Total variation uses the whole mass of the absolute value measure, not half of it.
- v_+(omega) is the supremum of int_X (omega+dd^c u)^n over bounded omega-psh potentials. The preceding proposition prop:bmp-metric proves that the supremum is unchanged if only smooth potentials are used. Accept this input and check its application.
- The preceding normalized compactness estimate eq:normalized-lone says int_X |u| dV<=K_omega for every genuine omega-psh u with sup_X u=0, with K depending on X,omega,dV only.
- The preceding lemma lem:uniform-exponential says that there are alpha>0 and C<infinity depending on X,omega,dV only, such that int_X exp(-alpha u)dV<=C for all such normalized u. Accept this input and check its application, including the fixed-p quantifier and the same sequence w_j for all p.
- Use integration by parts on compact X, elementary positivity of mixed wedges of smooth nonnegative (1,1) forms, the intermediate value theorem and convexity of the exponential. No equation solvability, nonlinear continuity theorem, Popovici result or additional mass hypothesis is an input.
- In the TeX excerpt, \ddc denotes dd^c and \cref/\eqref refer to the specified internal inputs.

Proof to verify:

The same failure occurs among smooth potentials, with the total masses specified in advance. In the following statement $\mathrm{d}V$ is the fixed smooth positive probability volume chosen above.

\begin{corollary}\label{cor:smooth-prescribed-masses}
Suppose $v_+(\omega)=+\infty$. Let $(\varepsilon_j)_{j\geq1}$ and $(b_j)_{j\geq1}$ be real sequences with $0<\varepsilon_j<1$, $\varepsilon_j\to0$, and $b_j>\int_X\omega^n$. There are smooth potentials $w_j\in\PSH(X,\omega)$ with $\sup_Xw_j=0$ such that
\[
 \omega+\ddc w_j\geq(1-\varepsilon_j)\omega,
 \qquad
 \int_X(\omega+\ddc w_j)^n=b_j,
\]
and
\[
 \|\omega+\ddc w_j-\omega\|_{L^1(\gamma)}
 \leq2M\varepsilon_j.
\]
Moreover, $w_j\to0$ in $L^1(\mathrm{d}V)$ and $\mathrm{e}^{-pw_j}\to1$ in $L^1(\mathrm{d}V)$ for every fixed $p>0$. The full Gauduchon trace measures converge to $\omega\wedge\gamma^{n-1}$ in total variation.
\end{corollary}
\begin{proof}
By \cref{prop:bmp-metric}, choose a smooth $u_j\in\PSH(X,\omega)$ with $\sup_Xu_j=0$ and
\[
 \int_X(\omega+\ddc u_j)^n>\varepsilon_j^{-n}b_j.
\]
Put $T_j=\omega+\ddc u_j$. The polynomial
\[
 F_j(s)=\int_X\bigl((1-s)\omega+sT_j\bigr)^n,
 \qquad 0\leq s\leq\varepsilon_j,
\]
satisfies $F_j(0)<b_j$ and $F_j(\varepsilon_j)>b_j$, the latter by positivity of the mixed terms. The intermediate value theorem gives $s_j\in(0,\varepsilon_j)$ with $F_j(s_j)=b_j$. Set $w_j=s_ju_j$. This proves the normalization, strict positivity and prescribed mass. No monotonicity of $F_j$ is used.

The Gauduchon identity gives $\|T_j\|_{L^1(\gamma)}=\|\omega\|_{L^1(\gamma)}=M$. Hence
\[
 \|\ddc w_j\|_{L^1(\gamma)}
 =s_j\|T_j-\omega\|_{L^1(\gamma)}
 \leq2M\varepsilon_j.
\]
The absolute value of the trace is bounded by the trace of the matrix absolute value, so the same bound holds for the total variation of $\ddc w_j\wedge\gamma^{n-1}$. Also \eqref{eq:normalized-lone} gives $\|w_j\|_{L^1(\mathrm{d}V)}\leq K_\omega\varepsilon_j$.

Let $\alpha,C$ be the constants in \cref{lem:uniform-exponential} for $(X,\omega,\mathrm{d}V)$, and fix $p>0$. For all sufficiently large $j$, one has $ps_j\leq\alpha$. Convexity of the exponential function, applied with weight $ps_j/\alpha$, gives
\[
 0\leq\mathrm{e}^{-pw_j}-1
 \leq\frac{ps_j}{\alpha}\bigl(\mathrm{e}^{-\alpha u_j}-1\bigr).
\]
Integration bounds its $L^1(\mathrm{d}V)$ norm by $pC\varepsilon_j/\alpha$, proving the last convergence.
\end{proof}

Taking $b_j$ constant gives failure of continuity of the total Monge--Amp\`ere mass even along a sequence of uniformly finite mass. Taking $b_j\to+\infty$ gives divergent masses with the same linear and exponential convergence. These conclusions concern manifolds on which bounded mass fails; they do not impose that failure on the general measure construction.
