Run_id: smooth_dual_regularity_01

Statement: Verify the local conformal-current regularity lemma and its proposed consequence: in complex dimension n>=2, a smooth strictly positive maximizing normalized Gauduchon current for a nonzero L1 density at positive threshold forces the density root to have a smooth nonnegative representative and every threshold subsolution to be a smooth exact solution, unique modulo constants. No BMP, positive lower mass or root-tail hypothesis is assumed. Do not assume strict positivity of the density in the nonclosed setting. No novelty claim is made.

The source is /Users/mingchen/Non-Kahler/research/editorial/section_smooth_dual_regularity_v2.tex. The earlier unsubmitted v1 remains preserved. The v2 corollary proves the constant-difference conclusion directly so that its future production integration can replace the older rigidity corollary without circular self-reference; it also records the already-proved smooth strictly positive density case. It is an unreviewed research-only supplement outside checkpoint44. Its dependencies are the checked production sources in /Users/mingchen/Non-Kahler/book/author. section_threshold_trace_saturation.tex proves lem:unbounded-gauduchon-trace-density for ALL smooth Hermitian test forms (not only Gauduchon ones), prop:threshold-trace-saturation for a fixed smooth test and every genuine threshold subsolution, and cor:smooth-dual-threshold-rigidity. These were audited in threshold_trace_saturation_02, report SHA25693ee0ce765b295afe55e0cdddd8852ae55f0fd5cde7db12e109239b9212f3bcd. section_integrable_gauduchon_currents.tex thm:integrable-current-attainment gives the supremum formula for every Ln root without tails (tails are only used for general compact attainment). section_integrable_gauduchon_tests.tex defines rho and the smooth test normalization. The attained-threshold theorem thm:individual-density-subsolution supplies a genuine subsolution at b>0. chapter_gauduchon.tex proof of thm:lamari constructs the unique smooth positive (1,1) root of a smooth strictly positive (n-1,n-1) form. section_weak_gauduchon_duality.tex proves the pointwise matrix determinant duality. Expand their exact contexts and verify the dependencies.

The proposed proof deliberately does not identify the determinant of a measurable current matrix with the non-pluripolar product at Sobolev regularity. Trace saturation first gives an absolutely continuous matrix. The all-Hermitian trace inequality, made simultaneous using countably many locally constant matrices extended to global metrics, bounds its pointwise determinant below. Its trace against the maximizing metric gives the opposite AGM bound; equality makes the entire current a times that metric. Closedness of ddc u then yields da=B-aC by wedging with gamma^(n-2) and inverting xi->xi wedge gamma^(n-1). This first-order equation should bootstrap a from L1_loc to all W^{k,1}_loc, and hence smoothness. Elliptic regularity then makes u smooth, after which the exact Monge–Ampere equation is legitimate.

Please scrutinize: the current trace-to-coefficient absolute continuity step; normalization factors in k_T and gamma; countable simultaneous test inequalities; the determinant duality and equality case including a=0; the distributional derivative computation; invertibility and necessity of n>=2; Sobolev bootstrapping and elliptic regularity; and existence/uniqueness conclusions. The optional closed-background observation in smooth-dual-regularity-followup.md is NOT submitted or claimed by the proof below. No arbitrary singular-current wedge is introduced. Preserve all previous submissions and verifier memory/results.

Proof:

\begin{lemma}\label{lem:smooth-conformal-current}
Let $X$ have complex dimension $n\geq2$, let $\theta$ be a smooth real $(1,1)$-form and let $\gamma$ be Hermitian. Suppose $u,a\in L^1_{\mathrm{loc}}(X)$ satisfy
\[
 \theta+\ddc u=a\gamma
\]
as currents. Then $a$ and $u$ are smooth.
\end{lemma}
\begin{proof}
Taking the exterior derivative and multiplying by $\gamma^{n-2}$ gives
\[
 \mathrm{d}a\wedge\gamma^{n-1}
 =\mathrm{d}\theta\wedge\gamma^{n-2}
      -a\,\mathrm{d}\gamma\wedge\gamma^{n-2}.
\]
At each point, $\xi\mapsto\xi\wedge\gamma^{n-1}$ is an isomorphism from real one-forms to real $(2n-1)$-forms, as one sees in a unitary frame. Its inverse depends smoothly on the point. Thus
\[
 \mathrm{d}a=B-aC
\]
in distributions, for smooth real one-forms $B,C$. Since $a\in L^1_{\mathrm{loc}}$, this first gives $a\in W^{1,1}_{\mathrm{loc}}$. Differentiating the equation and using smoothness of its coefficients gives $a\in W^{k,1}_{\mathrm{loc}}$ for every integer $k$. Local Sobolev embedding makes $a$ smooth. Now $\ddc u=a\gamma-\theta$ is smooth; taking its trace in local coordinates and applying elliptic regularity makes $u$ smooth as well.
\end{proof}

\begin{corollary}\label{cor:smooth-dual-exact-equation}
Let $\omega$ be Hermitian on a connected compact complex manifold of dimension $n\geq2$. Let $0\leq f\in L^1(\mathrm{d}V)$ be nonzero and $b=b_\omega(f)>0$. If $D_{f^{1/n}}$ has a smooth strictly positive maximizer $T\in\mathscr G_\omega$, then $f^{1/n}$ agrees almost everywhere with a smooth nonnegative function. Every threshold subsolution is smooth and satisfies
\[
 \mathrm{MA}_\omega(u)=bf\,\mathrm{d}V.
\]
Such a solution exists, and all threshold subsolutions differ by constants. No root-tail or mass-property assumption is required.
\end{corollary}
\begin{proof}
The attained-threshold theorem supplies a genuine threshold subsolution $u$. The following argument applies to every such $u$. Write $T=\gamma^{n-1}$ for its smooth positive Gauduchon root and set
\[
 a=\left(\frac{bf\,\mathrm{d}V}{\gamma^n}\right)^{1/n}.
\]
The normalization of $T$ is $\int_X\omega\wedge T=1$. Since it maximizes, \cref{prop:threshold-trace-saturation} gives the equality
\[
 A\wedge\gamma^{n-1}=a\gamma^n,
 \qquad A=\omega+\ddc u\geq0.
\]
The positive coefficient measures of $A$ are controlled by this trace, which is absolutely continuous. Thus $A$ has an almost-everywhere positive semidefinite matrix density, with coefficients in $L^n$ because $a\in L^n$.

For every smooth Hermitian form $\beta$, \cref{lem:unbounded-gauduchon-trace-density} also gives
\[
 A\wedge\beta^{n-1}
 \geq\left(\frac{bf\,\mathrm{d}V}{\beta^n}\right)^{1/n}\beta^n.
\]
These pointwise matrix inequalities hold simultaneously almost everywhere for all positive definite matrices: on each coordinate chart first use a countable dense family of constant positive matrices, extended to global smooth Hermitian forms on smaller charts, and then use continuity in the matrix. The matrix arithmetic--geometric mean duality therefore yields
\[
 \left(\frac{A^n}{\gamma^n}\right)^{1/n}\geq a
 \quad\text{almost everywhere}.
\]
Here $A^n$ means only the determinant of its measurable coefficient matrix; no equality with a nonlinear current product has yet been used. The trace equality gives the reverse inequality by arithmetic--geometric mean. Equality forces all eigenvalues relative to $\gamma$ to equal $a$, including where $a=0$. Consequently $A=a\gamma$ as currents.

Apply \cref{lem:smooth-conformal-current} with $\theta=\omega$. Both $a$ and $u$ are smooth, and $f^{1/n}=b^{-1/n}a(\gamma^n/\mathrm{d}V)^{1/n}$ has a smooth nonnegative representative. Only now take the smooth top power: $\omega_u^n=a^n\gamma^n=bf\,\mathrm{d}V$. For two threshold subsolutions, the identity $\omega+\ddc u=a\gamma$ has the same right side. Their smooth difference is therefore pluriharmonic and hence constant on connected compact $X$.
\end{proof}

Smooth dual attainment is thus restrictive even before asking for estimates on the potential. The dimension assumption is used when the exterior derivative of $a\gamma$ determines $\mathrm{d}a$. The corollary does not assert smooth attainment for an arbitrary density or any regularity from a singular maximizing current.

If $f$ is smooth and strictly positive, \cref{thm:gaud-volume-dual-formula} supplies a smooth strictly positive maximizing Gauduchon form from the smooth equation. Thus the corollary recovers that case, including constant-difference uniqueness among all genuine threshold subsolutions.
