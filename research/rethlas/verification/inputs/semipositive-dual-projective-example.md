Run_id: semipositive_dual_projective_example_01

Statement: Verify two bounded follow-ups frozen in research/editorial/section_semipositive_lp_limit.tex and section_semipositive_projective_example.tex under /Users/mingchen/Non-Kahler. They remain outside checked checkpoint52 until reviewed. No novelty claim. The first is uniform convergence for Lp densities under smooth semipositive dual attainment. The second gives an explicit projective branched-map example separating semipositive from strictly positive smooth maximizers, and global smoothness of a threshold potential from differentiability of the density root.

Accepted internal inputs: read the exact statements of book/author/section_semipositive_dual_attainment.tex (all threshold subsolutions unique modulo constants); book/author/section_symmetric_equation_selection.tex, proposition symmetric-equation-clusters (Lp uniform precompactness and equation identification); book/author/section_individual_exponential_equations.tex (greatest exponential solution agrees with bounded continuous solution for Lp); proposition individual-normalizer-lp (the bounded-equation scalar is the individual threshold); book/author/section_integrable_gauduchon_currents.tex (supremum over all normalized Gauduchon currents equals rho for any nonnegative Ln root); and corollary kahler-smooth-dual-attainment in section_smooth_dual_sharpness.tex. Accept these exact proved internal results, not a broader smooth-attainment theorem. The current normalization and determinant k_T are in section_weak_gauduchon_duality.tex. The new arguments use no external paper theorem.

Check the Lp corollary: the continuous solution is at b, hence equals the normalized threshold solution by the accepted uniqueness. The greatest exponential family equals the bounded one. Apply accepted uniform precompactness with trivial symmetry group; every uniform cluster solves at b and is therefore that same solution. No extra smaller-background hypothesis or BMP is needed in this Lp regime.

Check the explicit example carefully in normalization ddc=i/(2pi) partial barpartial. X=P^n, n>=2, omega=FS with integral omega^n=1, dV=omega^n. F maps homogeneous coordinates to their squares. A=(1/2)F*omega=omega+ddc u with u=(1/2)log sum|Zi|^4-log sum|Zi|^2 smooth global. A>=0 and is strictly positive exactly off the union of coordinate hyperplanes. f=A^n/omega^n is smooth nonnegative; integral f=1 by closed Stokes. T=A^(n-1) is smooth semipositive ddc-closed, integral omega wedge T=1. Every unbounded omega-psh potential has extended mass<=1 by bounded truncation Stokes. Thus b<=1 from the integral of a subsolution inequality, while the smooth u gives b>=1. For this T, k_T=f^((n-1)/n) by the smooth determinant formula extended by continuity. Hence D_froot(T)=1=rho, so T is actually maximizing over ALL normalized Gauduchon currents. Check no circular use of the new example to establish b or rho.

On Z0=1, verify f(z)=2^n product|zi|^2 (1+sum|zi|^2)^(n+1)/(1+sum|zi|^4)^(n+1), including the factor 2^(-n) in A^n and the holomorphic Jacobian of the square map. Near a generic coordinate hyperplane froot=|z1|^(2/n) times a smooth positive factor; it is not differentiable, including n=2. For n>=2 rank deficiency of A implies rank deficiency of its cofactor T, while T>0 off that set. No smooth strictly positive maximizer can exist by the accepted closed-background characterization (continuous f with zeros cannot agree almost everywhere with a smooth strictly positive density). Smooth bounded f gives uniform exponential convergence by the first corollary.

Do not edit frozen inputs, prior reports or verifier memory by hand. Use the normal verification workflow and give an honest verdict.

Proofs:

\begin{corollary}\label{cor:semipositive-dual-lp-limit}
Under the hypotheses of \cref{thm:semipositive-dual-exact-equation}, suppose in addition that $f\in L^p(\mathrm{d}V)$ for some $p>1$. Then the normalized threshold solution $u_0$ is continuous, and the normalized greatest exponential solutions converge uniformly to $u_0$ as the exponent tends to zero.
\end{corollary}
\begin{proof}
The scalar of the continuous equation is $b_\omega(f)$ by \cref{prop:individual-normalizer-lp}. Its normalized solution is therefore $u_0$, by \cref{thm:semipositive-dual-exact-equation}. For $L^p$ data the greatest exponential solution agrees with the bounded solution, as explained after \cref{thm:individual-exponential-subsolution}. Apply \cref{prop:symmetric-equation-clusters} with the trivial group. The normalized family is uniformly precompact, and every cluster limit solves the threshold equation. Uniqueness identifies every such limit with $u_0$, proving convergence of the whole family.
\end{proof}


\subsection{A branched projective example}

A smooth semipositive maximizer need not be strictly positive, even when the threshold solution is smooth. The following example also shows why smoothness of the density root was asserted only off the degeneracy set.

\begin{example}\label{ex:semipositive-projective-maximizer}
For every $n\geq2$, there is a smooth nonnegative density $f$ on $\mathbb P^n$, vanishing precisely on the coordinate hyperplanes, such that $b_\omega(f)=1$ and $D_{f^{1/n}}$ has a smooth semipositive maximizer strictly positive off those hyperplanes. Here $\omega$ is the Fubini--Study form, normalized by $\int_{\mathbb P^n}\omega^n=1$, and $\mathrm{d}V=\omega^n$. The threshold solution is smooth, but $f^{1/n}$ is not differentiable at a general point of any coordinate hyperplane. There is no smooth strictly positive maximizing form. The normalized greatest exponential solutions converge uniformly to the normalized threshold solution.
\end{example}
\begin{proof}
Let
\[
 F[Z_0:\cdots:Z_n]=[Z_0^2:\cdots:Z_n^2],\qquad
 A=\tfrac12F^*\omega.
\]
The homogeneous formula
\[
 u=\tfrac12\log\!\left(\sum_{i=0}^n|Z_i|^4\right)
       -\log\!\left(\sum_{i=0}^n|Z_i|^2\right)
\]
defines a smooth function on projective space, and $A=\omega+\ddc u$. This form is semipositive and is strictly positive exactly where every homogeneous coordinate is nonzero. Define
\[
 f=A^n/\omega^n,\qquad T=A^{n-1}.
\]
Closed Stokes gives $\int f\omega^n=\int\omega\wedge T=1$. Thus $T\in\mathscr G_\omega$. Every genuine $\omega$-plurisubharmonic potential has extended mass at most one: each bounded truncation has mass one, and restriction away from its truncation level can only decrease that mass. Consequently an inequality $\mathrm{MA}^{\mathrm{ext}}_\omega(v)\geq c f\omega^n$ forces $c\leq1$. The smooth solution $u$ gives the reverse bound, so $b_\omega(f)=1$.

The determinant formula for smooth semipositive forms gives
\[
 k_T=f^{(n-1)/n},\qquad
 D_{f^{1/n}}(T)=\int_{\mathbb P^n}f\omega^n=1.
\]
By \eqref{eq:integrable-current-supremum} and $\rho_\omega(f^{1/n})=b_\omega(f)^{-1/n}=1$, this is a maximizer. Its strict positivity away from the coordinate hyperplanes follows from that of $A$; on a hyperplane $A$ has deficient rank, and so does its cofactor matrix.

For the density root, use the chart $Z_0=1$ with coordinates $z_1,\ldots,z_n$. Pulling back the Fubini--Study volume by $(z_1,\ldots,z_n)\mapsto(z_1^2,\ldots,z_n^2)$ and including the factor $2^{-n}$ gives
\[
 f(z)=2^n\left(\prod_{i=1}^n|z_i|^2\right)
       \frac{(1+\sum_i|z_i|^2)^{n+1}}
            {(1+\sum_i|z_i|^4)^{n+1}}.
\]
Near a point of $\{z_1=0\}$ with all the other coordinates nonzero, its $n$th root is $|z_1|^{2/n}$ times a smooth strictly positive function. Restriction to a real line transverse to that hyperplane proves nondifferentiability, including the absolute-value case $n=2$. Coordinate symmetry gives the same conclusion on every component. The absence of a smooth strictly positive maximizer follows from \cref{cor:kahler-smooth-dual-attainment}, since $f$ has zeros. Finally $f$ is bounded, so \cref{cor:semipositive-dual-lp-limit} gives the uniform exponential limit.
\end{proof}
