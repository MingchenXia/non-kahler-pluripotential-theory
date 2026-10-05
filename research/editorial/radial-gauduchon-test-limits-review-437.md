# Radial Gauduchon test limits — research437

The projective counterexample admits two explicit types of balanced test. The metrics minimizing the perturbed volume also minimize the endpoint volume asymptotically. In dimension three their trace-normalized powers converge to the degenerate fiber. In dimensions at least four these same metrics have a positive limiting bigness-threshold quotient; a different localized family approaches the zero threshold. This distinction makes the denominator collapse of Section32.2.1 concrete without changing any original problem status.

Use exactly the data of Section25.12: m>=2, n=m+1, t=(m-1)/m, a=x/t, h=omega+w, mu=omega^m wedge w, theta=omega+a w. Write A_epsilon and H_epsilon for Lemma25.12.1, gamma_epsilon for (25.41), and T_epsilon=gamma_epsilon^m. Introduce

\[
 I_\epsilon=\int_B(a+\epsilon)^{-2}\omega^m
 =m t^2\int_0^1\frac{x^{m-1}}{(x+t\epsilon)^2}\,\mathrm{d}x.
\]

The exact trace, background pairing and determinant denominator are

\[
 M_\epsilon:=\int_Xh\wedge T_\epsilon=m+I_\epsilon/H_\epsilon,
 \quad \int_X\theta\wedge T_\epsilon=n-\epsilon I_\epsilon/H_\epsilon,
 \quad D_\mu(\gamma_\epsilon)=(n/H_\epsilon)^{m/n}H_\epsilon.
\]

Indeed, the horizontal part of T_epsilon is omega^m/[H_epsilon(a+epsilon)^2], while its other part is m A_epsilon^(m-1) wedge w. Closed Stokes gives the latter's h-trace m because A_epsilon and omega are cohomologous. The perturbed background has pairing n, and subtracting epsilon w removes precisely epsilon I_epsilon/H_epsilon. The denominator was calculated in Theorem25.12.1.

For m=2, t=1/2. With q=epsilon/2, direct integration gives

\[
 I_\epsilon=\tfrac12\left(\log\frac{1+q}{q}+\frac q{1+q}-1\right),
 \qquad H_\epsilon=1-q\log\frac{1+q}{q}.
\]

Thus I_epsilon is asymptotic to one half log(1/epsilon), H_epsilon tends to one and epsilon I_epsilon tends to zero. Normalize by g_epsilon=M_epsilon^(-1/m)gamma_epsilon, so integral h wedge g_epsilon^m=1. Both linear pairing and D_mu scale by M_epsilon^(-1). In dimension three,

\[
 \int_X\theta\wedge g_\epsilon^2\sim\frac6{\log(1/\epsilon)},
 \qquad D_\mu(g_\epsilon)\sim\frac{2\,3^{2/3}}{\log(1/\epsilon)}.
\]

Their volume quotient tends to 3^(1/3), whereas their threshold quotient tends to zero. Moreover, g_epsilon^2 converges weakly to [Z], Z={p} times the projective line. The mixed positive term has h-trace exactly two and disappears after division by M_epsilon. The normalized horizontal probability (a+epsilon)^(-2)omega^2/I_epsilon concentrates at p: outside each fixed neighborhood of p its density is uniformly bounded, whereas I_epsilon diverges. Integrating any smooth (1,1)-test form along the projective-line fiber reduces the remaining current convergence to this elementary probability convergence. Since integral_Z h=1, the limit has the correct trace normalization. No endpoint nonlinear current power or singular wedge product is needed.

For m>=3, monotone convergence gives

\[
 I_\epsilon\longrightarrow I_0=\frac{m t^2}{m-2}
 =\frac{(m-1)^2}{m(m-2)},
 \qquad M_\epsilon\longrightarrow M_0=m+I_0.
\]

The endpoint volume quotient of the original gamma_epsilon still tends to n^(1/n), because epsilon I_epsilon tends to zero and its determinant denominator tends to n^(m/n). But its bigness-threshold quotient tends to n/M_0>0. The normalized determinant denominator tends to n^(m/n)/M_0>0. These volume-minimizing metrics therefore do not approach the zero bigness threshold when n>=4. No uniqueness or explicit limit current of this family is claimed in those dimensions.

There are nevertheless explicit smooth balanced threshold-minimizing metrics in every n>=3. For 0<rho<1 choose nonzero smooth f_rho>=0 on B, supported where x<rho and normalized by integral_B f_rho omega^m=1. Put

\[
 \Gamma_\rho=f_\rho\omega^m+\rho h^m,
 \qquad \widehat\Gamma_\rho=\Gamma_\rho/(1+n\rho).
\]

The first summand is closed by top base degree, and the second is closed and strictly positive. The smooth positive root argument accompanying Theorem4.3.1 supplies a unique metric b_rho with b_rho^m=widehatGamma_rho; closedness makes it balanced. It has h-trace one and

\[
 0\leq\int_X\theta\wedge b_\rho^m
 \leq\frac{\rho/t+\rho C_\theta}{1+n\rho}\longrightarrow0,
 \qquad C_\theta=\int_X\theta\wedge h^m<\infty.
\]

The already proved lower bound lambda_mu(theta)=n^(1/n) implies D_mu(b_rho)<=n^(-1/n) integral theta wedge b_rho^m, hence the determinant denominator also tends to zero. The normalized powers converge weakly to [Z]: the f_rho probabilities concentrate at p and the rho h^m term vanishes. Thus [Z] lies in the weak closure of actual smooth balanced normalized tests, annihilates theta, and has zero determinant-weighted measure by Proposition25.19.1. This is an explicit instance of the general collapse criterion, with actual smoothing at the stated model, not a general current-smoothing theorem.

Dependencies are the complete136-line radial proof, complete48-line collapse criterion and the exact smooth-root, threshold and annihilator arguments freshly read at their stated seams. No additional external theorem, primary retrieval, native verification report or novelty claim is used. Both catalogues and all original directions retain checkpoint436 status: P08/P22/S13 resolved,39 remaining. The numerical expressions and weak convergence concern these two explicitly specified families only. The higher-dimensional volume-minimizer limit, universal closed/surface criteria and geometric flow endpoints remain separate.

Placement: add a short subsection at the end of Section25.12, after its original density/scope paragraph. The dimension-three calculation and higher-dimensional distinction belong beside the actual radial metrics; link the localized tests from Section32.2.1. Do not duplicate the general collapse proposition or infer a new original-problem resolution. Whole-recursive chapters and fresh arXiv coverage are not claimed by this review.

Complete67-line independent reconstruction first and automatic second reads, with the corrected smooth-root locator sentence freshly reread. Complete136-line radial input and48-line collapse input reads reused from436; smooth-root/threshold and annihilator proof seams freshly read. No fresh whole-recursive chapters, primary-paper retrieval or arXiv recheck. All335 book files,1019 proof bodies, both catalogues/manifests and451 protected sources remain exact, with five immutable P10 and six P08 intake blobs. The live436 release remains1215 printed pages; no author build, native call or publication is made here. Package validation passes with2188 archive entries,2187 current checksum payloads and332 book-source files matching the actual436 empty-source reconstruction. There is no new full reconstruction at437. Finalized metadata is repackaged and rechecked before synchronization.
