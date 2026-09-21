Run_id: trace_model_envelope_01

Statement: Audit new higher-dimensional trace-INEQUALITY envelope, NOT exactrealization. XcompactconnectedHermitian,Ysmoothcompactconnected positive dimension,u genericnuY0. Profiletau finitealreadyproved. NewL1pullback undercompactmodification proof andcompactness givevwithnu(v,E)>=tau(E)forallcompactdivisors, simultaneousglobalvbutnointersectionextraction. ChooseOmega0 boundrestrictedapprox andOmega2Omega0. DefineT largestOmega-psh<=0withallcompactdivisorialinequalities. Showgenuine,retainsinequalities,Ifixed/Pfixed andsmallbg envelope;finitepositiveMAwithoutBMP/PVP. PDEcorollaryappliesearlierfullyprovedprescribedordinarytypeLp theorem. CurveT=P(w)=Q(w); noordinaryequivalenceT~w asserted. Exacthigherdimnumbersstillquestion. CheckLelongsemicontdirection,modificationL1argument,Choquetfamilyandallquantifiers,modelindependenceofmajorantforfixedOmega,backgroundmonotonicity,correctuseofsourceIprojection.

Accepted prerequisites allavailable/passed: analytic_approximation_01,intrinsic_trace_data_01,curve_trace_metric_01; normalizedL1compactness/canonicalqpsh, standardLOCALSiulelongsemicont/maxidentity, compactanalyticexceptionalsetsvolumezero; thm:hermitian-i-projection andcor:ordinary-preserves-i in bookchapter_igood.tex (fromprecisestandardlocalSGPTvaluative/strongopennessinputs, previouslywritten/checked). Semipositivefixedpointcontact finiteMAestimate; smaller-background individualpositivitywithoutv_minus>0 nowalso relative_class_domination_01 correct. PrescribedordinarytypeLp fullyproved earlierprescribed_lp_existence_01, thm:als-prescribed-lp (noBMP/PVP). Readsourceandapplicablepreviousreportsasneeded. No useofpendingtraceadditivity. Checkallnewdeductions; sourcebooklocalfactsacceptednotincorrectglobalextensions. Bookread-only. Usualworkflow/report; no noveltyclaim.

Proof:

\section{An envelope carrying the trace inequalities}

The divisorial data admits a global potential whose Lelong numbers are at least the prescribed numbers. Taking an envelope then produces a distinguished model potential in a chosen sufficiently large Hermitian background on $Y$. This is a construction in every dimension. Exact equality with the prescribed divisorial data will remain a separate question.

\begin{lemma}\label{lem:modification-lone-pullback}
Let $\pi:Z\to Y$ be a smooth compact modification. If $v_j\to v$ in $L^1(Y)$ and all $v_j,v$ belong to $\PSH(Y,\Omega_0)$ for a fixed smooth background, then
\[
 v_j\circ\pi\longrightarrow v\circ\pi\quad\hbox{in }L^1(Z).
\]
\end{lemma}
\begin{proof}
Hartogs' lemma bounds the suprema of $v_j$ from above, and $L^1$ convergence to a genuine potential bounds them from below. Pullback preserves the supremum because $\pi$ is surjective. Choose a Hermitian form $\gamma$ on $Z$ with $\pi^*\Omega_0\leq C\gamma$. The pullbacks are genuine quasi-plurisubharmonic functions with this fixed lower curvature bound. Normalized compactness therefore makes them relatively compact in $L^1(Z)$.

Off the exceptional locus, $\pi$ is a biholomorphism onto its image. On relatively compact subsets there, change of variables gives $L^1$ convergence to $v\circ\pi$. Every global cluster limit consequently equals $v\circ\pi$ outside the exceptional locus, hence almost everywhere, since that analytic locus has smooth volume zero. The cluster limit is unique, proving convergence of the whole sequence.
\end{proof}

\begin{proposition}\label{prop:trace-profile-majorant}
There are a Hermitian form $\Omega_0$ on $Y$ and a potential $v\in\PSH(Y,\Omega_0)$ such that
\[
 \nu(v\circ\pi,E)\geq\tau_{Y,u}(E)
 \quad\hbox{for every divisor }E\hbox{ over }Y.
\]
\end{proposition}
\begin{proof}
Choose $\Omega_0$ dominating the common lower curvature bound of the restricted approximants $u_m|_Y$. They are genuine by \cref{cor:restricted-analytic-divisorial-bound}. Subtract their suprema and extract an $L^1$ limit $v\in\PSH(Y,\Omega_0)$ by normalized compactness.

For each fixed compact modification, \cref{lem:modification-lone-pullback} gives convergence of the pullbacks along that same subsequence. The local upper semicontinuity of Lelong numbers under $L^1$ convergence gives, at every point $z$ of $E$,
\[
 \nu(v\circ\pi,z)
 \geq\limsup_m\nu((u_m|_Y)\circ\pi,z)
 \geq\lim_m\frac{\operatorname{ord}_E\mathfrak a_m(u;Y)}m
 =\tau_{Y,u}(E).
\]
Taking the generic value proves the assertion. No simultaneous extraction over divisors is required: the pullback lemma applies to each modification after the subsequence on $Y$ has been fixed. The Lelong semicontinuity used here is a standard local fact recalled in \cite{SGPT}.
\end{proof}

For a Hermitian form $\Omega$ for which the following family is nonempty, define
\begin{equation}\label{eq:trace-profile-envelope}
 \mathcal T_\Omega(u;Y)
 :=\left(\sup\left\{a\in\PSH(Y,\Omega):a\leq0,
       \ \nu(a\circ\pi,E)\geq\tau_{Y,u}(E)
       \text{ for every divisor }E\text{ over }Y\right\}\right)^*.
\end{equation}
The choice of $\Omega$ is part of this notation. The definition refers only to the intrinsic trace data, and therefore to the ambient multiplier-ideal class of $u$.

\begin{theorem}\label{thm:trace-profile-model-envelope}
Choose $\Omega_0,v$ as in \cref{prop:trace-profile-majorant} and set $\Omega=2\Omega_0$. Then $T=\mathcal T_\Omega(u;Y)$ is genuine and satisfies all the divisorial inequalities in \eqref{eq:trace-profile-envelope}. Moreover,
\[
 Q_\Omega[T]=T,\qquad P_\Omega[T]=T,
 \qquad P_{\Omega/2}(T)\not\equiv-\infty.
\]
Writing $r=\dim Y$, its extended measure satisfies
\[
 0<\int_Y\mathrm{MA}^{\mathrm{ext}}_\Omega(T)<+\infty,
 \qquad
 \mathrm{MA}^{\mathrm{ext}}_\Omega(T)
 \leq\mathbf1_{\{T=0\}}\Omega^r.
\]
No bounded mass or positive lower volume property of $Y$ is assumed.
\end{theorem}
\begin{proof}
Normalize $v\leq0$. It is a competitor, so the family is nonempty and its supremum lies between $v$ and zero. It is stable under finite maxima: Lelong numbers of a maximum are the minima of the two Lelong numbers, also after pullback. Choquet extraction and finite maxima give an increasing sequence of competitors with canonical limit $T$. It converges in $L^1(Y)$. Apply \cref{lem:modification-lone-pullback} and local Lelong semicontinuity, for each divisor, to see that $T$ retains every defining inequality. Thus $T$ is itself a competitor and is the largest one.

The multiplier-ideal envelope preserves all multiplier ideals and hence all divisorial Lelong numbers, by \cref{thm:hermitian-i-projection} and the local valuative criterion used there. Since $T\leq0$, the potential $Q_\Omega[T]$ is also a competitor in \eqref{eq:trace-profile-envelope}. Maximality gives $Q_\Omega[T]\leq T$, while the reverse inequality follows because $T$ is admissible in its own multiplier-ideal envelope. Thus $Q_\Omega[T]=T$. The model consequence in \cref{cor:ordinary-preserves-i} gives $P_\Omega[T]=T$.

The original $\Omega_0$-plurisubharmonic $v$ is below $T$, so it supplies a competitor for $P_{\Omega/2}(T)$. The fixed-point contact estimate \cref{prop:fixed-point-finite}, applied on $Y$, gives the displayed measure bound and finiteness. The smaller-background individual positivity in \cref{lem:smaller-background-mass-lower} gives strict positivity. That assertion is individual and requires no positive infimum over all bounded potentials.
\end{proof}

This construction is independent of the extracted majorant: the supremum in \eqref{eq:trace-profile-envelope}, once $\Omega$ is fixed, does not refer to it. Increasing the prescribed trace data decreases $\mathcal T_\Omega$. Increasing the background increases it whenever both envelopes are defined. These facts follow from inclusion of the competitor families; they do not assert independence from the background.

\begin{corollary}\label{cor:trace-envelope-prescribed-equation}
For the chosen $\Omega$ and $T$, let $dV$ be a smooth positive volume form on $Y$ and let $0\leq f\in L^p(dV)$, $p>1$, with $\int_Y f\,dV>0$. For every $\lambda>0$ there is a unique $a\simeq T$ in $\PSH(Y,\Omega)$ with
\[
 \mathrm{MA}^{\mathrm{ext}}_\Omega(a)=e^{\lambda a}f\,dV.
\]
There is also a positive scalar $c$ and $a\simeq T$ with $\mathrm{MA}^{\mathrm{ext}}_\Omega(a)=cf\,dV$; the scalar is unique.
\end{corollary}
\begin{proof}
The preceding theorem checks both parts of the model condition \eqref{eq:als-model-condition} on the compact Hermitian manifold $Y$. Apply the prescribed ordinary-type theorem \cref{thm:als-prescribed-lp}. Its proof requires neither bounded mass nor a positive lower volume hypothesis. No uniqueness of the zero-exponent potential is asserted here.
\end{proof}

On a curve this model construction can be compared more precisely with the atomic trace. Take $\Omega=A\eta$ as in \cref{prop:curve-trace-source-distance}, and let $w$ be its Green representative. Every competitor $a$ in \eqref{eq:trace-profile-envelope} has a curvature measure with atoms at least $D_u$. Hence
\[
 \ddc(a-w)=(A\eta+\ddc a)-D_u-(A-D_u(Y))\eta
\]
has a smooth lower bound. The difference is a genuine quasi-plurisubharmonic function and is bounded above on the compact curve, so $a\preceq w$. Conversely $a\preceq w$ implies all the required Lelong inequalities. Thus the defining competitor family is exactly the ordinary singularity-envelope family, and
\[
 \mathcal T_{A\eta}(u;Y)=P_{A\eta}[w]=Q_{A\eta}[w].
\]
The last equality follows from the $\mathcal I$-goodness proved in \cref{prop:curve-trace-source-distance}. In particular the model envelope has exactly the prescribed curve Lelong numbers. In higher dimension the construction so far proves inequalities, and possible strict inequalities must still be studied.
