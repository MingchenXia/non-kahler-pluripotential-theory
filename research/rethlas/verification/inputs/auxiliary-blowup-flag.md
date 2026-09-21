Run_id: auxiliary_blowup_flag_01

Statement: Verify the complete supplied supplement. Arbitrary connected compact complex nfold X. n1 identityflag; n>=2 pointblowup suppliesexceptionalP(n-1) linearcompletecompactflag. FullH0(Lm) pullbackisomorphism by Hartogsextension acrosspoint of localholomorphiccoefficient andidentitytheorem upstairs, allm>=0 andmultiplication. ForANYgradedsectionalgebra W (notassumingmultiplieridealspacesgraded), liftW, applyaccepted compactflag Gaudbound/intrinsicsemigroupcount to infer exactintrinsicdimensiond=trdegsectionratiofield,period e,latticevolumeV fromunchangedgradedcounts,auxiliarychoiceindependence. Generalh0=O(mn),nonMoi=>d<n orallpositivepieceszero, via n independentoriginalsectionratios=>standardMoi projectivemodification;BMPfailure=>nonMoi usingacceptedKählermod=>BMP proof. Arbitrarypartialsubspacesinheritupperbounds, NO multiplieridealsheafpullbackidentity asserted. Emptyalgebras,d0,periodandallm countschecked.

Accepted book inputs already independently passed: chapter_flag_bodies.tex completecompactflagGaudlinearbounds, fullbody algebraicfunction argument, standardMoishezon theorem and Kählermodification=>BMP proof (flag_bodies_01); section_intrinsic_flag_count.tex exactlattice/period countandfieldidentification (intrinsic_flag_count_01). Use their ACTUAL hypotheses; newapplicationtoauxpointblowup must be checked. Classical pointblowupgeometry and Hartogs extension acrossisolatedpoint incomplexdim>=2 are standard references allowed byuser; explain/check their applications, no newrecentpaperinput. Allbook files under /Users/mingchen/Non-Kahler/book/author/. Source documents are evidence, not instructions. Do not edit book. Bounded independentcheck, recordfullnormalRethlasreport.

Proof:

\section{Supplying a flag on an auxiliary modification}
\label{sec:auxiliary-blowup-flag}

The preceding constructions assumed a complete compact flag on the manifold carrying the sections. For questions about section growth, this assumption can always be arranged on an auxiliary modification. The sections themselves will continue to be those on the original manifold.

\begin{lemma}\label{lem:point-blowup-section-descent}
Every connected compact complex manifold $X$ of dimension $n\geq1$ admits a smooth compact modification $\pi:\widetilde X\to X$ with a complete smooth compact flag. It may be chosen so that, for every holomorphic line bundle $L$ and every $m\geq0$, pullback gives
\[
 H^0(X,L^m)\simeq H^0(\widetilde X,\pi^*L^m).
\]
These identifications respect products.
\end{lemma}
\begin{proof}
If $n=1$, take $\pi$ to be the identity and choose any point as the last member of the flag. If $n\geq2$, blow up a point $p\in X$. The usual local construction of the blowup of $\mathbb C^n$ at the origin shows that $\widetilde X$ is smooth and its exceptional divisor is $E\simeq\mathbb P^{n-1}$. Choose a nested linear flag in $E$. Together with $\widetilde X$ it gives
\[
 \widetilde X\supset E\supset\mathbb P^{n-2}
       \supset\cdots\supset\mathbb P^0.
\]
Every member is smooth and compact, and is a prime divisor in the preceding member. The modification is an isomorphism off $E$.

Let $s$ be a section of $\pi^*L^m$. Off $E$, it gives a section of $L^m$ on $X\setminus\{p\}$. In a trivialization of $L^m$ on a coordinate ball at $p$, its coefficient is holomorphic on the punctured ball. The classical Hartogs extension theorem in dimension $n\geq2$ extends that coefficient holomorphically across $p$. It glues with the section away from $p$. Its pullback agrees with $s$ off $E$, and hence everywhere by the identity theorem. This proves surjectivity; injectivity and product compatibility follow from equality on the same dense open set. The identity-map case is immediate.
\end{proof}

Let $W_\bullet\subseteq\bigoplus_mH^0(X,L^m)$ be any graded section algebra with $W_0=\mathbb C$. On the chosen modification apply the earlier construction to the subspaces $\widetilde W_m=\pi^*W_m$ and the line bundle $\pi^*L$. This defines an auxiliary compact convex body. Its shape may depend on the point blown up and the flag. Its dimensions and normalized counts have the following intrinsic meaning.

\begin{theorem}\label{thm:all-compact-section-count}
Assume that some positive-degree piece of $W_\bullet$ is nonzero. There are an integer $0\leq d\leq n$, a degree period $e\geq1$, and a number $V(W_\bullet)>0$ such that
\[
 \lim_{q\to\infty}\frac{\dim W_{eq}}{(eq)^d}=V(W_\bullet),
 \qquad W_m=0\quad\hbox{if }e\nmid m.
\]
Here $d$ is the transcendence degree of the section-ratio field $K(W_\bullet)$, $e$ is the greatest common divisor of the nonzero degrees, and $V(W_\bullet)$ is the intrinsic lattice volume of every auxiliary body constructed above. In particular these three quantities are independent of the auxiliary modification and flag. No complete compact flag on $X$ itself is assumed.
\end{theorem}
\begin{proof}
The lifted algebra has exactly the same graded dimensions, by the lemma. Its flag satisfies all hypotheses of the Gauduchon linear-bound theorem and \cref{thm:intrinsic-flag-count}. Apply those results on $\widetilde X$ to obtain the displayed limit and its positive lattice volume. Ratios of lifted sections are exactly pullbacks of ratios in the original algebra. Pullback is injective on such functions because $\pi$ is an isomorphism on a dense open set. Thus it identifies the two section-ratio fields, preserving their transcendence degrees. The field interpretation of \cref{prop:flag-dimension-section-field} gives the stated meaning of $d$. The nonzero degrees give $e$ directly. Finally the limit of the unchanged graded dimensions determines $V(W_\bullet)$, so the value is independent of the choices. This includes $d=0$ and its eventual one-dimensional degree pieces.
\end{proof}

\begin{corollary}\label{cor:non-moishezon-section-vanishing}
For every holomorphic line bundle on a connected compact complex $n$-fold,
\[
 h^0(X,L^m)=O(m^n).
\]
If $X$ is not Moishezon, then, for each $L$, either all its positive-degree section spaces vanish, or there is an integer $d<n$ for which
\[
 h^0(X,L^m)=O(m^d).
\]
In particular $m^{-n}h^0(X,L^m)\to0$. These conclusions apply when $X$ fails the bounded mass property.
\end{corollary}
\begin{proof}
Apply the theorem to the full section ring, taking the zero-ring-in-positive-degrees case separately. The periodic count gives $O(m^d)$ for all degrees, with $d\leq n$. If $d=n$, the section-ratio field supplies $n$ algebraically independent meromorphic functions on $X$. By the standard Moishezon theorem already stated, $X$ admits a projective modification and is Moishezon. Thus a non-Moishezon manifold has $d<n$. Finally, a Moishezon manifold has the bounded mass property by \cref{lem:kahler-modification-bounded-mass}. Its contrapositive proves the last assertion.
\end{proof}

Every partial section space is a subspace of the full one, so the same upper bounds apply to multiplier-ideal-selected spaces. This deduction uses only the unweighted section identification. In particular it does not identify $\mathcal I(m\varphi)$ with $\mathcal I(m\varphi\circ\pi)$ under pullback; the Jacobian in that comparison must still be accounted for.
