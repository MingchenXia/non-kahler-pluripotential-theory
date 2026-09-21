Run_id: semipositive_dual_capacity_limit_01

Statement: Check the short conditional capacity-convergence corollary frozen in research/editorial/section_semipositive_capacity_limit.tex in /Users/mingchen/Non-Kahler. It is not yet integrated into checked checkpoint51 and makes no novelty claim. It assumes the preceding smooth semipositive dual exponential-limit theorem AND a genuine smaller-background envelope P_{delta omega}(u0) for some 0<delta<1. The new corollary must not be read as establishing that extra hypothesis automatically.

Accepted internal inputs: read the precise statements/proofs in book/author/section_semipositive_exponential_limit.tex (correct report semipositive_dual_consequences_01) and book/author/section_relative_compactness.tex, specifically proposition lower-barrier-criterion and theorem common-barrier-criterion, whose exact conclusions are accepted. The first supplies u0-C<=v_lambda<=0, full-family L1 convergence to u0, b<=c_lambda<=b exp(C lambda), and MAext(v_lambda)=c_lambda exp(lambda v_lambda) f dV with f in L1 nonnegative. The latter criterion has semipositive big background theta, smaller-background genuineness for phi, lower barrier phi-C, uniform upper bound, L1 limit u with u preceq phi, and vanishing self-measure exponential discrepancy. It implies capacity convergence without BMP or positive lower mass. Here omega is a Hermitian metric, hence semipositive and big, and phi=u=u0. No claim about the proof of the accepted criterion is submitted for a new whole-book audit.

Check the exact application: for lambda<=1 the equation measures are bounded by the fixed finite absolutely continuous measure b exp(C) f dV. Uniformly bounded differences |exp(v_lambda)-exp(u0)| tend to zero in smooth-volume measure by L1 convergence of normalized nonpositive potentials. Fixed f in L1 then gives convergence of their integrals (absolute continuity/truncation of f). This is the required self-measure error. Limit ordinary type is automatic since it equals phi. A sequence criterion gives convergence of the whole family. If u0 is bounded, a constant below it is a delta omega-plurisubharmonic competitor, so the envelope is genuine. Check pole values, constants and all assumptions. Do not import a local capacity theorem with unstated boundary hypotheses. Do not edit frozen sources, prior reports or verifier memory. Use only the normal verification workflow; record an honest verdict.

Proof:

\begin{corollary}\label{cor:semipositive-dual-capacity-limit}
Under the hypotheses of \cref{prop:semipositive-dual-exponential-limit}, suppose in addition that $P_{\delta\omega}(u_0)$ is genuine for some $0<\delta<1$. Then $v_\lambda\to u_0$ in capacity as $\lambda\downarrow0$. In particular this holds if the threshold solution $u_0$ is bounded.
\end{corollary}
\begin{proof}
Fix a sequence $\lambda_j\downarrow0$. Proposition~\ref{prop:semipositive-dual-exponential-limit} gives $u_0-C\leq v_{\lambda_j}\leq0$ and $v_{\lambda_j}\to u_0$ in $L^1$. For all large $j$,
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(v_{\lambda_j})
   =c_{\lambda_j}\mathrm{e}^{\lambda_jv_{\lambda_j}}f\,\mathrm{d}V
   \leq b\mathrm{e}^{C}f\,\mathrm{d}V.
\]
The bounded functions $|\mathrm{e}^{v_{\lambda_j}}-\mathrm{e}^{u_0}|$ tend to zero in smooth-volume measure. Since $f\in L^1$, their integrals against $f\,\mathrm{d}V$ tend to zero. Thus the self-measure error in \eqref{eq:common-barrier-self-error} vanishes. Apply \cref{prop:lower-barrier-criterion} with $\theta=\omega$ and $\varphi=u_0$; its additional limit-type hypothesis is automatic because the limit is $u_0$ itself. This proves capacity convergence along every sequence and hence for the family. If $u_0$ is bounded, a constant below it is a competitor for $P_{\delta\omega}(u_0)$, so that envelope is genuine.
\end{proof}

The smaller-background condition is an additional hypothesis. Its validity for an arbitrary threshold solution in this semipositive dual setting is not established here.
