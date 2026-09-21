Run_id: symmetric_equation_selection_01

Statement: Verify the proposition on uniform compactness and symmetry of the vanishing-positive-exponent equation, and its corollary giving at leastTHREE normalizedboundedsolutions for symmetricNUMAdata, two smoothandthirdHolder. This is a new deduction from manuscript inputs, not a claim that the supplied paper states it. Do not infer convergenceoftheentirefamily or smoothnessofthethirdsolution.

Accepted exact manuscript inputs (read definitions/statements in /Users/mingchen/Non-Kahler/book/author): thm:kn-continuous and thm:nguyen-exp forHermitianbackground fLp p>1nonzero; uniqueSCALARc for zeroexponent, notuniquepotential; prop:vanishing-exponent barriers u+logc/lambda-M <= u_lambda <=u+logc/lambda-m; thm:hermitian-holder-elementary (section_holder_regularization.tex) with UNIFORMHolderconstant for uniformnormalizedC0 andLp densitybound; boundedlocal productcontinuityunderuniformconvergence. StandardArzelaAscoliandpullbackundera biholomorphism.

Conditional prerequisite: fullNUMAconstruction in section_degenerate_nonuniqueness.tex beingauditedasdegenerate_nonuniqueness_01. The bookwillincludeonlyifthat auditpasses. Source userprovidedNUMA_vibe.pdf is /Users/mingchen/Non-Kahler/research/sources/NUMA-Xia.pdf. You mustcheckthesymmetryspecializationafresh: chooseevenkappacutoff, r=>-r, P<->Q,Rfixed, coefficientssymmetric, rhoeven,wodd, A0/B0swap,commoncubeinvariant, potentialsswapandnormalization. The corollaryusesc1andourddcconventioni/(2pi); allsourceformsalreadydivided4pi.

Checkeachdeductionsequentially. Areholderconstantsuniformacrosslambda despitec shift? Is exponentdensityexp(lambda u_lambda)=c exp(lambda w_lambda)? Does preservingtheMEASUREf dV sufficewithoutpreservingdV? Doesuniquenesslambda>0yieldinvariance, anduniformlimitkeepit? Doesa!=u,vfollowfrominvolution? NoothernewexternaltheorembeyondstandardArzelaAscoli. Do notusezerodensitypotentialuniqueness or any generalmassbound.

Proof:

\section{Symmetry and the vanishing-exponent approximation}
\label{sec:symmetric-equation-selection}

The nonuniqueness example does not prevent the positive-exponent equation from producing useful choices of limiting solutions. In particular, uniqueness before taking the limit forces every cluster solution to preserve all symmetries of the data. We give the compactness argument and then apply it to the projective example.

\begin{proposition}\label{prop:symmetric-equation-clusters}
Let $\omega$ be Hermitian, let $dV$ be a smooth positive volume form, and let $0\leq f\in L^p(dV)$, $p>1$, be nonzero. Let $c>0$ be the unique scalar for the bounded equation $\mathrm{MA}_\omega(u)=cf\,dV$. For $\lambda>0$ denote by $u_\lambda$ the unique bounded solution of
\[
 \mathrm{MA}_\omega(u_\lambda)=e^{\lambda u_\lambda}f\,dV,
 \qquad a_\lambda=u_\lambda-\sup_Xu_\lambda.
\]
The family $\{a_\lambda:0<\lambda\leq1\}$ is relatively compact in $C(X)$. Every cluster limit as $\lambda\downarrow0$ is a normalized bounded solution of $\mathrm{MA}_\omega(a)=cf\,dV$.

Suppose a group $G$ of biholomorphisms of $X$ preserves $\omega$ and the measure $f\,dV$. Then every $a_\lambda$ and every such cluster limit is $G$-invariant. In particular, the zero-exponent equation has a $G$-invariant normalized solution. No bounded mass hypothesis is needed.
\end{proposition}
\begin{proof}
Choose one continuous solution $u$ of the zero-exponent equation using \cref{thm:kn-continuous}, and put $m=\inf_Xu$, $M=\sup_Xu$. The barriers in \cref{prop:vanishing-exponent} give, with
\[
 w_\lambda=u_\lambda-\frac{\log c}{\lambda},
\]
the uniform bounds
\[
 u-M\leq w_\lambda\leq u-m.
\]
Consequently $|w_\lambda|\leq M-m$ and $a_\lambda=w_\lambda-\sup_Xw_\lambda$ is uniformly bounded between $-2(M-m)$ and zero. Its measure is
\[
 \mathrm{MA}_\omega(a_\lambda)
       =c e^{\lambda w_\lambda}f\,dV.
\]
The densities on the right have a uniform $L^p$ bound for $0<\lambda\leq1$. After normalizing $dV$ if necessary, \cref{thm:hermitian-holder-elementary} gives a uniform H\"older bound with any one fixed exponent in its stated range. The Arzel\`a--Ascoli theorem proves relative compactness in $C(X)$.

If $\lambda_j\downarrow0$ and $a_{\lambda_j}\to a$ uniformly, then $a$ is $\omega$-psh and $\sup_Xa=0$. The bounds for $w_\lambda$ give $e^{\lambda w_\lambda}\to1$ uniformly, hence the densities tend to $cf$ in $L^p$. Bounded local product continuity under uniform convergence identifies the limiting measure with $\mathrm{MA}_\omega(a)$, proving its equation.

For each $g\in G$, pullback of the positive-exponent equation shows that $u_\lambda\circ g$ solves the same equation. Its uniqueness gives $u_\lambda\circ g=u_\lambda$. Surjectivity of $g$ preserves the supremum, so $a_\lambda\circ g=a_\lambda$. Uniform convergence preserves these equalities for every $g$. Compactness supplies at least one cluster limit as $\lambda\downarrow0$, yielding the invariant solution.
\end{proof}

\begin{corollary}\label{cor:numa-third-solution}
The data in \cref{thm:degenerate-hermitian-nonuniqueness} can be chosen so that the same zero-exponent equation has at least three distinct normalized bounded solutions. Two are smooth, and a third is H\"older continuous and fixed by the involution $\iota[A:B]=[B:A]$.
\end{corollary}
\begin{proof}
Choose the cutoff $\kappa$ in that construction even; all its required support and plateau properties are preserved by this choice. Then $\rho$ is even, while $w=F(r)$ is odd. The involution sends $r$ to $-r$, interchanges $P,Q$, and fixes $R$. The coefficient identities $x(-r)=y(r)$ and $z(-r)=z(r)$ show that $\iota^*\omega_0=\omega_0$. Thus $\iota^*\omega=\omega$, and $\iota^*\omega_X=\omega_X$.

Since $\iota^*H=-H$, the involution interchanges $A_0$ and $B_0$. Their cubes are equal, so $f\omega_X^3$ is invariant. It also interchanges $\widetilde u=-w/2-\rho$ and $\widetilde v=w/2-\rho$. These functions therefore have the same supremum, and the normalized solutions $u,v$ are interchanged. They are distinct, so neither is invariant.

Apply \cref{prop:symmetric-equation-clusters} to the group generated by $\iota$. Here $c=1$, as the two constructed solutions already have that scalar. An invariant cluster solution $a$ cannot equal either $u$ or $v$. Its H\"older regularity follows from the uniform estimate used in the proposition, or from its bounded equation with smooth density. This gives a third solution; smoothness of that third solution is not asserted.
\end{proof}

The corollary is a consequence of the supplied counterexample and the approximation theory proved here. It does not identify the invariant solution explicitly, and it does not prove that all cluster limits agree. The latter is a selection problem for a fixed approximation procedure, separate from uniqueness of all solutions of the limiting equation.


Follow AGENTS.md: initialize memory, sequentialeverydeduction, exact references as needed, persistallfindingsandfullreadablereport. Write results/symmetric_equation_selection_01/verification.json viaMCP. Correctiffzerogaps/errorsundertheacceptedinputs. Do noteditbook. Boundedconditionalreview,notformalverification.
