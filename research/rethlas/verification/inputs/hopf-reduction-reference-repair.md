Run_id: hopf_reduction_reference_repair_01

Statement: Focused verification of the corrected existence/regularity/uniqueness argument in the reduced Hopf equation. Earlier hopf_reduction_01 report (read it) found ALL geometric/measure/toric proofs correct; only false attribution of continuousLp toSGPT causedwrong. That historicalinput/report remainsunchanged. CurrentreplacementusesALREADYPROVEDBOOK thm:kn-continuous forcontinuousHermitianLp onbaseP^(n-1), thm:tw-smooth forsmoothpositivef, andSGPT ONLY closedfullmassnormalizeduniqueness. No newexternalLp theorem. Check newparagraph andsourcehypotheses, factorsandn2edge. Do notredoallgeometricproofs; acceptearliercorrect deductions including MAomega(pi*v)=n pi*MA_sigma(v)wedgezeta, dV=1/2pi*(sigma^(n-1))zeta, intfiberzeta2, sigmaKahlerunitvolume,n>=2, f>=0Lp p>1 positiveintegral, restrictedboundeddescendedclass. Readinternal thmkn/chapter_weak_equations.tex andthmtw/chapter_smooth_equations.tex withauditedprerequisites weak_lp_existence_01,smooth_second_estimate_01,smooth_czero_01. SourceSGPT author/chapter_envelopes.tex thm:Yau_rel lines1021-1028, inprovidedDownloadsreference. InstantiatecompactKahlerB=P^(n-1),theta=sigma,modelreferencephi0,fullmassmeasureg=f/intf, probability/nonpluripolar, boundedvfullmassviaStokes. StandardlocalBT andclosedmass accepted. Checkreferencesusualworkflow, bookreadonly. No otherrepairneeded unlessnewactualissuefound.

Proof:

\section{A reduced Monge--Amp\`ere equation}

Let $f\geq0$ be in $L^p(\mathbb P^{n-1},\sigma^{n-1})$, $p>1$, with $\int f\sigma^{n-1}>0$. Among potentials $u=\pi^*v$ with bounded $v\in\PSH(\mathbb P^{n-1},\sigma)$, the equation
\begin{equation}\label{eq:hopf-reduced-equation}
 (\omega+\ddc u)^n=c(f\circ\pi)\,dV
\end{equation}
is equivalent to
\[
 (\sigma+\ddc v)^{n-1}=\frac{c}{2n}f\sigma^{n-1}.
\]
Indeed \cref{thm:hopf-descended-hermitian-ma} and $dV=\frac12\pi^*(\sigma^{n-1})\wedge\zeta$ give one implication. For the other, push the measures forward by $\pi$; the common fiber integral is two, so their equality is also necessary. Integrating the base equation fixes
\[
 c=\frac{2n}{\int_{\mathbb P^{n-1}}f\sigma^{n-1}}.
\]
Apply \cref{thm:kn-continuous}, whose proof was given in \cref{chap:weak-equations}, to the Hermitian manifold $(\mathbb P^{n-1},\sigma)$. It gives a continuous $v$ and a positive scalar $a$ with $(\sigma+\ddc v)^{n-1}=af\sigma^{n-1}$. Since $\sigma$ is closed, bounded Stokes gives $a\int f\sigma^{n-1}=1$. Thus $a=c/(2n)$ and $v$ solves the required base equation. Bounded $\sigma$-plurisubharmonic functions are in the full-mass class of the reference potential $0$. The measure $(f/\int f\sigma^{n-1})\sigma^{n-1}$ has mass one and charges no pluripolar set. The normalized uniqueness theorem for that class in \cite[theorem on the relative Monge--Amp\`ere equation]{SGPT} gives uniqueness of $v$ up to constants. Consequently \eqref{eq:hopf-reduced-equation} has a continuous solution unique up to constants within the descended class. For smooth positive $f$, \cref{thm:tw-smooth} on the same base gives smooth $v$, with the same scalar fixed by Stokes. Existence and regularity here use the proofs already supplied in this book; only the stated closed-class uniqueness is imported from \cite{SGPT}.

The same measure calculation, without an existence assertion, transforms a right side $c e^{\lambda u}(f\circ\pi)dV$ into $(c/(2n))e^{\lambda v}f\sigma^{n-1}$. If $f$ depends on the fiber variable, this reduction no longer applies.

