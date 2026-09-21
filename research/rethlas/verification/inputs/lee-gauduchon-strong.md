Run_id: lee_gauduchon_strong_01

Statement: Verify the whole supplied subsection. It proves zero Lee–Gauduchon class for a strongly Gauduchon metric, a nonzero positive d-exact-current obstruction to such metrics, and the explicit Calabi–Eckmann quotient example with LG={0}, no strongly Gauduchon/balanced metric, and a nonzero pseudoeffective de-Rham-exact Bott–Chern class outside the image of dc:H1->HBC11. Check the complex quotient construction, action properness/freeness, smooth product identification, cohomology, submersion and positive-current obstruction in full. This is a reconstruction of a known example, not a novelty claim.

Independent internal premises:
- chapter_gauduchon.tex thm:gauduchon and prop:gauduchon-trace: every compact complex manifold admits a Gauduchon metric, and integration of ddc f against its full smooth (n-1,n-1) power is zero. Nonzero positive (1,1)-currents have positive mass against a smooth strictly positive complementary form.
- Current chapter_lck.tex and section_lck_volume_literature.tex: dc = i/(4pi)(barpartial-partial); kappa_lambda=dc lambda=-d lambda^c, j_X:H1dR->HBC11, [lambda]->{kappa_lambda}; LG(X)={ [dc gamma^(n-1)] in H^(2n-1)dR : gamma Gauduchon}. K_X=ker j_X and W_X=its annihilator are defined in the separate staged section_lee_gauduchon_cone.tex. This subsection's example proves V=0 and H^(2n-1)=0 directly and uses no unverified cone-duality or invariance conclusion.
- Standard inputs allowed: smooth quotient of a free proper Lie group action, and its local holomorphic slices for a free proper holomorphic action of a complex Lie group; de Rham cohomology/Kunneth for S3 times S3; type decomposition and distributional Stokes; the positive Fubini–Study form on P1 and elementary projectivization/submersion. Check that all their hypotheses hold here. The compact quotient is constructed in the proof, not imported as an unexplained compactness premise.

Attribution/reference source to check by the normal workflow: Ornea–Verbitsky, The Lee–Gauduchon cone on complex manifolds, arXiv2411.05595v2, Remarks5.6–5.8 and Example5.7. Primary https://arxiv.org/abs/2411.05595v2 ; archived /Users/mingchen/Non-Kahler/research/sources/OV25-Lee-Gauduchon.pdf and .txt. Their example is the classical Calabi–Eckmann threefold diffeomorphic to S3 times S3 and fibered over P1 times P1. The present proof supplies that quotient explicitly rather than treating the target example as a premise. The fully general characterization of strongly Gauduchon manifolds by exact currents is NOT being asserted; only the obstruction direction is proved and used.

Pay attention to the factor i/(4pi) and sign in the exact primitive of dc Gamma; free/properness of the complex additive action t.(z,w)=(exp(t)z,exp(i t)w); the role of nonzero vectors; uniqueness and smoothness of the unit-sphere slice; compactness of the quotient; rank two of p*eta; de Rham exactness versus nonzero Bott–Chern class; and exclusion from image(j_X). Do not edit the staged source or manuscript. Persist all findings and final JSON, then stop.

Proof:

\subsection{Strongly Gauduchon metrics}
\label{sec:lee-gauduchon-strong}

Vanishing of the Lee--Gauduchon class is weaker than the strongly Gauduchon condition. We give an explicit example, following the distinction in \cite[Remarks 5.6--5.8]{OV25LeeGauduchon}. It also shows why the image of $j_X$ must not be replaced by all de Rham-exact Bott--Chern classes.

\begin{definition}
A Hermitian metric $\gamma$ is \emph{strongly Gauduchon} if $\gamma^{n-1}$ is the $(n-1,n-1)$-component of a smooth closed real $(2n-2)$-form.
\end{definition}

Writing that form as
\[
 \Theta=\gamma^{n-1}+\beta+\overline\beta,
 \qquad \beta\text{ of type }(n,n-2),
\]
shows that the definition is equivalent to $\partial(\gamma^{n-1})$ being $\bar\partial$-exact: its value is $-\bar\partial\beta$. Conversely, this equation and its conjugate give $\mathrm{d}\Theta=0$, because the remaining types exceed dimension $n$. Applying $\bar\partial$ also shows that $\gamma$ is Gauduchon. Every balanced metric is strongly Gauduchon by taking $\Theta=\gamma^{n-1}$.

\begin{proposition}\label{prop:lee-strong-obstruction}
A strongly Gauduchon metric has zero Lee--Gauduchon class. If a connected compact complex manifold admits a nonzero positive de Rham-exact $(1,1)$-current, it has no strongly Gauduchon metric, and hence no balanced metric.
\end{proposition}
\begin{proof}
Put $\Gamma=\gamma^{n-1}$ and use $\beta$ as above. In our normalization,
\[
 \dc\Gamma
 =\frac{\mathrm i}{4\pi}
       (\bar\partial\beta-\partial\overline\beta)
 =\mathrm{d}\!\left(\frac{\mathrm i}{4\pi}
                              (\beta-\overline\beta)\right).
\]
Thus $[\dc\Gamma]=0$.

For the obstruction, suppose $T=\mathrm{d}S\geq0$ is nonzero and $\Theta$ is a closed real form with strictly positive $(n-1,n-1)$-part $\Gamma$. Type considerations and distributional Stokes give
\[
 \int_XT\wedge\Gamma
 =\int_XT\wedge\Theta=0.
\]
The first integral is strictly positive because $T\ne0$ and $\Gamma>0$, a contradiction. The argument uses the full current and a smooth test form; it does not involve a non-pluripolar product.
\end{proof}

\begin{example}\label{ex:lee-calabi-eckmann}
There is a connected compact complex threefold $X$ with
\[
 \operatorname{LG}(X)=\{0\},\qquad V_X=K_X=W_X=0,
\]
but with no strongly Gauduchon metric. Moreover, $X$ has a nonzero pseudoeffective Bott--Chern class whose de Rham image is zero and which is not in the image of $j_X$.
\end{example}
\begin{proof}
Consider the holomorphic action of the additive group $\C$ on
\[
 \widetilde X=(\C^2\setminus\{0\})\times(\C^2\setminus\{0\}),
 \qquad
 t\cdot(z,w)=(e^t z,e^{\mathrm i t}w).
\]
The action is free. Indeed, $e^t=e^{\mathrm i t}=1$ forces $t=0$. It is proper: if both $(z,w)$ and $t\cdot(z,w)$ range in compact subsets of $\widetilde X$, the norms of all four vector components are bounded above and away from zero. Writing $t=a+\mathrm i b$, the ratios of the norms bound $e^a$ and $e^{-b}$ above and away from zero. Thus $a$ and $b$ stay bounded, which proves properness. The free proper holomorphic action has local holomorphic slices and a Hausdorff complex quotient $X$ of dimension three.

Every orbit meets $S^3\times S^3$ exactly once. The required group element is determined by
\[
 a=-\log|z|,\qquad b=\log|w|.
\]
These expressions are smooth, so the slice identifies the quotient smoothly with $S^3\times S^3$. In particular $X$ is compact and connected, and
\[
 H^1_{\mathrm{dR}}(X,\R)=H^2_{\mathrm{dR}}(X,\R)
 =H^5_{\mathrm{dR}}(X,\R)=0.
\]
It follows directly that $V_X=K_X=W_X=0$ and $\operatorname{LG}(X)=\{0\}$: the latter cone is nonempty by Gauduchon's theorem and lies in the zero group $H^5_{\mathrm{dR}}(X,\R)$.

Projectivizing both vector components descends to a holomorphic submersion
\[
 p:X\longrightarrow\mathbf P^1\times\mathbf P^1.
\]
Its differential is surjective because the product projectivization on $\widetilde X$ is a submersion and the group orbits lie in its fibers. Let $\eta$ be the sum of the Fubini--Study forms on the two factors. The smooth form
\[
 \alpha=p^*\eta
\]
is closed, semipositive and of rank two everywhere. It is nonzero and de Rham exact, since $H^2_{\mathrm{dR}}(X,\R)=0$. By \cref{prop:lee-strong-obstruction}, it obstructs a strongly Gauduchon metric.

Its Bott--Chern class is nonzero. Otherwise $\alpha=\ddc f$ for a smooth real function $f$, and integration against any Gauduchon form would give zero, contradicting positivity and $\alpha\ne0$. The class is pseudoeffective because it has the positive representative $\alpha$. Finally $j_X$ has zero domain, so this class is not in its image.
\end{proof}

The example distinguishes two linear obstructions. The Lee--Gauduchon cone detects positive classes obtained from closed one-forms by $j_X$. Strongly Gauduchon metrics are obstructed by every nonzero positive de Rham-exact $(1,1)$-current. The latter family can be larger, even when the first cohomology vanishes. Thus the bimeromorphic invariant above is useful without being a complete test for balanced or strongly Gauduchon geometry.
