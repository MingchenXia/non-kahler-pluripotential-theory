Run_id: trace_additivity_01

Statement: Audit local analytic-minorant product-ideal comparison and exact additivity of restricted-ideal intrinsic trace data on arbitrary compact Hermitian X. No BMP or global closed-positive-current assumption. u,v genericLelong0alongY, allmodificationscompact smooth. Exactbooknormalization ddc=i/(2pi)partialbarpartial, idealexp(-u), approximant(1/m,I(mu)). Cao2015 source usesoppositeorder andprintedBergmanformula1/klogsumwithweighte^-2kphi appearsfactorinconsistent; do NOTcopyit. Check ourresolutionproof directly: Siu splitting c_i=a_i+b_i, localJacobianA_i=ordJ+1, productidealorders>mc_i-2Ai, monomialdivision=>U_m+V_m <=(1-delta_m)s+O1. Boundederrorcan dependonm. RestrictinequalityandtakeLelong toderive tau_u+tau_v>=tau_sum, combinealreadyprovedreverse. Curveordinarytypeaddition alsoasserted, no max equality.

Accepted prerequisites: analytic_approximation_01, intrinsic_trace_data_01, curve_trace_metric_01 allpassed andread; exactidealtypes, validrestriction, fullrealFekete finiteprofilelimit, subadditivityinequality, Greenrealizationandordinarytypeindependence. StandardLOCAL analyticlogresolution,Siu decomposition, multiplierintegrability/holomorphicdivisibility. CheckallNEWproofstepsandnoproperdescentgap. SourceCao15.pdf/.txt localprimarypublishedtext inresearch/sources, DOI10.1016/j.crma.2014.11.004, fullyread. Reconstructratherthanassumehisglobaltheorem applies. Bookread-only; usualworkflow, no noveltyclaim.

Proof:

\section{Addition of the intrinsic trace data}

The addition inequality can be strengthened to equality. The needed approximation comparison is local; the global closed-current notation in which it was originally formulated is not a restriction on this application. We give the calculation in our weight convention. It is the resolution argument underlying Cao's addition theorem \cite{Cao15}.

\begin{lemma}\label{lem:analytic-minorant-product-ideals}
Let $u,v$ be quasi-plurisubharmonic on a compact complex manifold, and let $s$ have analytic singularities. If $u+v\leq s+O(1)$, then for analytic potentials $U_m,V_m$ of types $(1/m,\mathcal I(mu))$, $(1/m,\mathcal I(mv))$, there are numbers $\delta_m\downarrow0$ such that
\[
 U_m+V_m\leq(1-\delta_m)s+O(1)
 \quad\hbox{for all sufficiently large integers }m.
\]
The bounded error may depend on $m$.
\end{lemma}
\begin{proof}
Resolve the ideal of $s$. Locally upstairs,
\[
 s\circ\pi=\sum_i c_i\log|z_i|^2+O(1),\qquad c_i>0.
\]
The assumed inequality gives
$\nu(u\circ\pi,E_i)+\nu(v\circ\pi,E_i)\geq c_i$.
Choose nonnegative $a_i,b_i$ below these respective Lelong numbers with $a_i+b_i=c_i$. Local Siu decomposition, after smooth corrections, implies
\[
 u\circ\pi\leq\sum_i a_i\log|z_i|^2+O(1),\qquad
 v\circ\pi\leq\sum_i b_i\log|z_i|^2+O(1).
\]
Put $A_i=1+\operatorname{ord}_{E_i}\operatorname{Jac}\pi$. Pullback integrability of $f\in\mathcal I(mu)$ and $g\in\mathcal I(mv)$ gives
\[
 \operatorname{ord}_{E_i}(f\circ\pi)+A_i>ma_i,
 \quad \operatorname{ord}_{E_i}(g\circ\pi)+A_i>mb_i,
\]
and hence
\[
 \operatorname{ord}_{E_i}((fg)\circ\pi)>mc_i-2A_i.
\]
Choose $\delta_m=C/m$ with $C\geq\max_i2A_i/c_i$. Holomorphic division by the corresponding coordinate monomials, followed by logarithms of the finite generator norms, gives
\[
 (U_m+V_m)\circ\pi
 \leq(1-\delta_m)\sum_i c_i\log|z_i|^2+O(1).
\]
Proper descent and a finite cover prove the assertion. If the divisor is empty, $s$ is bounded and the conclusion follows from upper bounds for $U_m,V_m$. Smooth local corrections ensure positivity for Siu decomposition; no global closed background is used.
\end{proof}

\begin{theorem}\label{thm:trace-data-additivity}
Let $u,v\in\QPSH(X)$ have zero generic Lelong number along the connected compact submanifold $Y$. Then, on every divisor over $Y$,
\[
 \tau_{Y,u+v}=\tau_{Y,u}+\tau_{Y,v}.
\]
\end{theorem}
\begin{proof}
The inequality $\geq$ was proved in \cref{prop:trace-profile-calculus}. Fix a sufficiently large integer $k$ and let $S_k$ be the global analytic approximant to $u+v$, of type $(1/k,\mathcal I(k(u+v)))$. By \cref{thm:demailly-hermitian-input}, $u+v\leq S_k$. Apply the preceding lemma with $s=S_k$ to the global approximants $U_m,V_m$. Their restrictions and that of $S_k$ are genuine because all three original potentials have zero generic Lelong number along $Y$.

Restrict the resulting ordinary inequality to $Y$, pull back to any fixed smooth compact modification, and take the generic Lelong number along its divisor $E$. This gives
\[
 \frac{\operatorname{ord}_E\mathfrak a_m(u;Y)}m
 +\frac{\operatorname{ord}_E\mathfrak a_m(v;Y)}m
 \geq(1-\delta_m)
       \frac{\operatorname{ord}_E\mathfrak a_k(u+v;Y)}k.
\]
Let $m\to\infty$. Finiteness and the limit formula in \cref{thm:intrinsic-trace-profile} yield
\[
 \tau_{Y,u}(E)+\tau_{Y,v}(E)
 \geq\frac{\operatorname{ord}_E\mathfrak a_k(u+v;Y)}k.
\]
Now let $k\to\infty$. This proves the opposite inequality and hence equality. No convergence of Monge--Amp\`ere masses or of a singularity metric enters the argument.
\end{proof}

For curves, the theorem identifies the atomic measures themselves:
$D_{u+v}=D_u+D_v$. With one fixed nonpositive Green kernel the corresponding Green potentials add, by integration of positive measures. The atomic trace therefore satisfies
\[
 \operatorname{Tr}^{\mathrm{at}}_Y(u+v)
 \simeq\operatorname{Tr}^{\mathrm{at}}_Y(u)
       +\operatorname{Tr}^{\mathrm{at}}_Y(v).
\]
Here the statement is about ordinary singularity types; its Green representatives and their independence were established above. Positive real homogeneity follows in exactly the same way from homogeneity of the trace data. The inequality for maxima in \cref{prop:trace-profile-calculus} remains an inequality; this proof supplies no corresponding equality for maxima.
