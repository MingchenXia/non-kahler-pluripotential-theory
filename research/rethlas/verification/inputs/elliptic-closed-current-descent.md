Run_id: elliptic_closed_current_descent_01

Statement: Audit the complete proposed section below. It derives the closed Bott–Chern cone, potential/envelope descent and exact selected-section/kernel identities on the elliptic threefold used in the lower-mass example. No novelty claim. Check every deduction, including distributions rather than just smooth forms. The proof must not assume any lower mass or bounded mass estimate.

Conventions: ddc=i/(2pi) partial bar-partial, dc=i/(4pi)(bar-partial minus partial). Positive currents are real (1,1). X is the compact quotient of P3 minus z=0 and w=0 by [z:w]->[z:e^(2pi)w]. The base is B=P1xP1, and pi([z:w])=([z],[w]); the connected elliptic fiber is C/(2pi Z+2pi i Z). Base Fubini–Study forms have integral one, alpha,beta are their pullbacks, omega=alpha+beta+D, D=dt wedge dc t, t=log(||w||²/||z||²) on the covering space. Smooth connected compact manifolds only. A genuine psh potential is not identically minus infinity. MAext is the extended non-pluripolar measure. P and Q are the ordinary and all-weight multiplier-ideal envelopes defined in the book.

Canonical prior inputs, inspected in their actual local files (relative to /Users/mingchen/Non-Kahler):
1. book/author/section_vanishing_lower_mass.tex supplies only the explicit quotient and local product elliptic fibration. book/author/section_lower_mass_metric_geometry.tex proves ddc omega=2 alpha wedge beta, d(omega²)=0, integral_E D=4pi and no closed Kähler current. Their audits vanishing_lower_mass_01 and lower_mass_metric_geometry_01 are now completed correct. The new descent proof must be independent of their nonlinear lower-mass theorem.
2. book/author/chapter_divisorial_models.tex and section_bott_chern_bclasses.tex: smooth and current descriptions of Bott–Chern cohomology. book/author/section_bott_chern_cone_compactness.tex, prop:psef-cone-compact-base, and following nef-implies-psef proof in chapter_bott_chern_loci.tex. Definitions of nefness and non-nef/non-Kähler loci are in that chapter.
3. book/author/section_curve_fibration_traces.tex, lem:submersion-multiplier-pullback, fully proved for every positive real weight. Ordinary/ideal envelope definitions and projection are in chapter_envelopes.tex and chapter_igood.tex. Check that the non-big semipositive backgrounds in this draft are allowed by those definitions.
4. Standard inputs: positivity matrices for order-zero positive currents; distributional current Stokes against smooth forms; constant-distribution criterion from vanishing coordinate derivatives; harmonic/subharmonic maximum principle on compact connected curves; local psh restriction and local Bedford–Taylor monotone continuity; projective-space cohomology, Kunneth and the Kahler ddbar lemma for P1xP1; bihomogeneous polynomial description of H0(O(am,bm)); fiber integration under a proper smooth submersion. Check exact applicability rather than importing a strong descent theorem.

Key issues: Does vanishing of T wedge alpha wedge beta force all vertical coefficients to vanish as measures? Does closedness then force distributional descent, and do connected fibers ensure global patching? Is Bott–Chern pullback injective by fiber harmonicity? Are both cones exactly the two-dimensional quadrant, without claiming the whole Bott–Chern group is computed? Verify the trace coefficient 8pi and de Rham-exact/non-ddc-exact example. For potentials, handle fibers where u is identically minus infinity, and check usc regularization and ideal inclusion reflection. Verify zero top-degree extended mass using local bounded truncations, not unjustified products of unbounded currents. For sections and kernels, check every weight and pushforward measure, including possibly zero selected spaces. Do not infer three-dimensional positive volume or any I-goodness criterion.

Use the ordinary Rethlas sequential, reference and synthesis workflow. Write only this audit's memory/results and final response. Never edit the manuscript or submitted sources, another audit, verifier installation, or Git history. No approval or TLS bypass. The parent will preserve the result and handle any corrections and integration.

Proof:

\section{Closed currents on the elliptic threefold}
\label{sec:elliptic-closed-current-descent}

The lower-mass example also permits an explicit description of its positive closed currents. This gives a useful comparison between the Hermitian equation and the theory of closed Bott--Chern classes on the same manifold.

Let $X$ be the threefold of \cref{sec:vanishing-lower-mass}, and let
\[
 \pi:X\longrightarrow B=\mathbf P^1\times\mathbf P^1
\]
be its elliptic fibration. Write $\sigma_1,\sigma_2$ for the integral-one Fubini--Study forms from the two factors, so $\alpha=\pi^*\sigma_1$ and $\beta=\pi^*\sigma_2$. The product coordinates used in that construction show that $\pi$ is locally a holomorphic product with the connected elliptic curve $E$. We retain its balanced metric $\omega$, for which
\[
 \alpha\wedge\beta=\tfrac12\ddc\omega.
\]
The argument below uses this identity, not the value of the lower Monge--Amp\`ere mass.

\subsection{Descent of positive closed currents}

\begin{lemma}\label{lem:elliptic-positive-current-descent}
Every positive closed real $(1,1)$-current $T$ on $X$ has the form
\[
 T=\pi^*S
\]
for a unique positive closed $(1,1)$-current $S$ on $B$. Pullback here is the ordinary pullback by a smooth holomorphic submersion.
\end{lemma}
\begin{proof}
The measure $T\wedge\alpha\wedge\beta$ is positive. Current Stokes gives
\[
 \int_XT\wedge\alpha\wedge\beta
   =\tfrac12\int_X\omega\wedge\ddc T=0.
\]
Thus this measure is zero. All products in this identity pair a current with smooth forms.

In local product coordinates $(z_1,z_2,\zeta)$, write the coefficient measures of $T$ as densities $p_{j\bar k}$ of a positive Hermitian matrix relative to their trace measure. The smooth form $\alpha\wedge\beta$ is a strictly positive volume form in the two base directions. Its wedge with $T$ is a positive smooth factor times the vertical diagonal coefficient. That coefficient therefore vanishes. Positivity of the matrix and
$|p_{j\bar\zeta}|^2\leq p_{j\bar j}p_{\zeta\bar\zeta}$ then make its entire vertical row and column zero. Consequently $T$ has only terms of the form
\[
 \frac{\mathrm{i}}{2\pi}\,t_{j\bar k}(z,\zeta),
       \mathrm{d}z_j\wedge\mathrm{d}\bar z_k,
       \qquad 1\leq j,k\leq2,
\]
where the coefficients are distributions of order zero.

The equations $\partial T=\bar\partial T=0$ imply
\[
 \partial_\zeta t_{j\bar k}
       =\partial_{\bar\zeta}t_{j\bar k}=0
\]
in the sense of distributions: these derivatives are exactly the coefficients of the terms containing one vertical differential. A distribution on a product whose derivatives in both real fiber directions vanish is pulled back from the base. For completeness, convolve it on a smaller product polydisk. The convolutions have both fiber derivatives zero and are independent of the fiber variable. Testing them against a fixed fiber test function of integral one gives distributions on the base; passage to the limit identifies the original distribution with their pullback. Independence on overlapping fiber disks and connectedness of the fiber extend this conclusion across the whole local product $U\times E$.

We therefore have $T|_{\pi^{-1}(U)}=\pi^*S_U$. Positivity and closedness of $S_U$ follow by testing the coefficient distributions against a nonnegative fiber test function of integral one and using the horizontal equations. Pullback on distributions is injective in a product, by the same test. Hence the $S_U$ agree on overlaps and define the required positive closed current $S$. Injectivity also proves uniqueness.
\end{proof}

\begin{proposition}\label{prop:elliptic-bott-chern-cones}
Pullback
\[
 \pi^*:H^{1,1}_{\mathrm{BC}}(B,\mathbb R)
           \longrightarrow H^{1,1}_{\mathrm{BC}}(X,\mathbb R)
\]
is injective. The pseudoeffective and nef cones on $X$ coincide and are
\[
 \operatorname{Psef}(X)=\operatorname{Nef}(X)
 =\{a\{\alpha\}_{\mathrm{BC}}+b\{\beta\}_{\mathrm{BC}}:
                                           a,b\geq0\}.
\]
Its trace-one base for the Gauduchon metric $\omega$ is the line segment $a+b=(8\pi)^{-1}$. Every class in this cone has a smooth semipositive representative, and none is big. The real form $\beta-\alpha$ is de Rham exact but represents a nonzero Bott--Chern class.
\end{proposition}
\begin{proof}
Suppose a smooth closed real form $\tau$ on $B$ satisfies $\pi^*\tau=\ddc u$ with $u$ smooth on $X$. Restriction to each compact connected elliptic fiber makes $u$ harmonic, hence constant there. Local holomorphic sections show that $u=v\circ\pi$ for a smooth function $v$ on $B$. Thus $\pi^*(\tau-\ddc v)=0$, which implies $\tau=\ddc v$ because $\pi$ is a submersion. This proves injectivity.

The standard cohomology calculation for $\mathbf P^1\times\mathbf P^1$, together with the K\"ahler $\partial\bar\partial$ lemma, gives
\[
 H^{1,1}_{\mathrm{BC}}(B,\mathbb R)
       =\mathbb R\{\sigma_1\}\oplus\mathbb R\{\sigma_2\},
 \qquad \int_B\sigma_1\wedge\sigma_2=1,
 \qquad \sigma_1^2=\sigma_2^2=0.
\]
These are the usual projective-space and product computations recalled in the closed theory. If $S$ is positive and closed, its two class coefficients are
\[
 a=\int_BS\wedge\sigma_2\geq0,
 \qquad b=\int_BS\wedge\sigma_1\geq0.
\]
The current description of Bott--Chern cohomology and the preceding lemma show that every pseudoeffective class on $X$ is therefore in the displayed cone. Conversely every such class has the smooth semipositive representative $a\alpha+b\beta$, and is nef. A nef class is pseudoeffective by the compactness argument following \cref{prop:psef-cone-compact-base}. This proves the equality of cones. It does not require a calculation of the whole Bott--Chern group of $X$.

Since $\omega^2=2\alpha\wedge\beta+2(\alpha+\beta)\wedge D$ and $\int_E D=4\pi$, fiber integration gives
\[
 \int_X(a\alpha+b\beta)\wedge\omega^2=8\pi(a+b).
\]
This proves the assertion about the trace-one base. No closed K\"ahler current exists on $X$, by \cref{prop:lower-mass-no-pluriclosed}, so none of these classes is big. Finally, the globally defined one-form $\dc t$ satisfies
\[
 \mathrm{d}(\dc t)=\beta-\alpha.
\]
The class of $\sigma_2-\sigma_1$ on $B$ is nonzero, and injectivity makes its pullback nonzero in Bott--Chern cohomology. Thus de Rham exactness does not imply $\ddc$-exactness on this example.
\end{proof}

In particular, every pseudoeffective class on this threefold has empty non-nef locus, whereas its non-K\"ahler locus is all of $X$ under the convention for non-big classes. The example does not contradict a nef-and-big theorem: no closed nef class here has positive top self-intersection. Indeed $(a\alpha+b\beta)^3=0$.

\subsection{Potentials and envelopes from the base}

\begin{proposition}\label{prop:elliptic-potential-descent}
Let $a,b\geq0$, put $\theta_B=a\sigma_1+b\sigma_2$ and $\theta=\pi^*\theta_B$. Pullback is a bijection
\[
 \PSH(B,\theta_B)\longrightarrow\PSH(X,\theta),\qquad v\longmapsto v\circ\pi.
\]
It preserves ordinary singularity order and equivalence, and ideal singularity order and equivalence. For every $v\in\PSH(B,\theta_B)$,
\[
 P_\theta[v\circ\pi]=P_{\theta_B}[v]\circ\pi,
 \qquad Q_\theta[v\circ\pi]=Q_{\theta_B}[v]\circ\pi.
\]
Nevertheless, every $u\in\PSH(X,\theta)$ satisfies
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)=0.
\]
\end{proposition}
\begin{proof}
Pullback preserves the curvature inequality, and a genuine potential stays genuine because $\pi$ is surjective. Conversely, restrict a $\theta$-plurisubharmonic function $u$ to an elliptic fiber. Locally a smooth potential for $\theta_B$ makes $u$ plurisubharmonic after pullback correction. The restriction is therefore subharmonic or identically $-\infty$. Since the correction is constant along the fiber, $u$ itself is subharmonic there. Compactness and connectedness imply that it is constant, allowing the value $-\infty$.

Thus $u=v\circ\pi$ for a function $v$ on $B$. On each base coordinate patch a holomorphic section identifies $v$ with the restriction of $u$ to that section. The corrected restriction is plurisubharmonic and cannot be identically $-\infty$ on an open patch: that would make $u$ identically $-\infty$ on an open subset of $X$. Hence $v$ is a genuine $\theta_B$-plurisubharmonic function. Surjectivity of $\pi$ gives uniqueness and preservation of ordinary order, with exactly the same constants.

By \cref{lem:submersion-multiplier-pullback}, for every $s>0$,
\[
 \mathcal I(sv\circ\pi)=\mathcal I(sv)\mathcal O_X.
\]
Extension by a product submersion preserves and reflects inclusion of ideals. To see reflection, compose local generators with a local holomorphic section: a pulled-back germ in the extended ideal restricts to a germ in the original ideal. Thus the all-weight ideal orders and equivalences correspond exactly.

The competitors defining both envelopes correspond under this bijection, including the bound by zero and the required ordinary or ideal condition. Their pointwise suprema commute with pullback. Upper semicontinuous regularization also commutes with pullback in a product chart, since a base neighborhood is obtained from every sufficiently small product neighborhood and local sections give the reverse comparison. This proves the two envelope identities.

Finally, $u_j=\max\{u,-j\}$ descends to $v_j=\max\{v,-j\}$. The semipositivity of $\theta_B$ makes these admissible bounded potentials. On a product chart add a local smooth potential for $\theta_B$ and approximate the resulting bounded plurisubharmonic function on the base by smooth plurisubharmonic functions decreasing on smaller charts. Their pulled-back complex Hessians have at most two complex directions, so their cubes vanish. Bedford--Taylor monotone continuity gives $(\theta+\ddc u_j)^3=0$. The increasing truncation definition of the extended non-pluripolar measure now proves the last assertion.
\end{proof}

Thus equality of the two envelopes in these backgrounds is exactly the corresponding equality on the base, while every three-dimensional Monge--Amp\`ere measure is zero. A positive-volume criterion from the big closed theory cannot be applied to these non-big classes. The strictly Hermitian background $\omega$ belongs to a different theory: its smooth positive-density equations are solvable, even though its infimum of masses is zero.

\subsection{Selected sections and their growth}

\begin{proposition}\label{prop:elliptic-selected-section-descent}
Let $a,b$ be positive integers, let $L_B=\mathcal O_B(a,b)$ and $L=\pi^*L_B$. For every quasi-plurisubharmonic $v$ on $B$ and positive integer $m$, pullback gives an isomorphism
\[
 H^0\bigl(B,L_B^m\otimes\mathcal I(mv)\bigr)
   \longrightarrow
 H^0\bigl(X,L^m\otimes\mathcal I(mv\circ\pi)\bigr).
\]
For $v=0$ these spaces have dimension $(am+1)(bm+1)$.

Equip $L_B$ with a smooth Hermitian metric, choose a continuous real function $\varphi$ on $B$, and put $\nu=\pi_*\mathrm{d}V_X$ for a smooth positive volume form on $X$. Use the norms
\[
 \|s\|_B^2=\int_B|s|^2\mathrm{e}^{-m\varphi}\,\mathrm{d}\nu,
 \qquad
 \|\pi^*s\|_X^2=\int_X|\pi^*s|^2
                \mathrm{e}^{-m\varphi\circ\pi}\,\mathrm{d}V_X.
\]
The isomorphism is isometric. If $K_{m,B}$ and $K_{m,X}$ are the corresponding pointwise squared-norm sums over orthonormal bases, including the displayed continuous weight, then
\[
 K_{m,X}=K_{m,B}\circ\pi,
 \qquad \pi_*(K_{m,X}\,\mathrm{d}V_X)=K_{m,B}\,\mathrm{d}\nu.
\]
\end{proposition}
\begin{proof}
A local frame of $L_B^m$ pulls back to a frame on $\pi^{-1}(U)$. The coefficient of a holomorphic section on this set is constant on each compact connected elliptic fiber, by the maximum principle. Local holomorphic sections of $\pi$ show that this coefficient descends holomorphically. These descended sections patch uniquely. Membership in the selecting ideals descends as well, by the ideal identity and reflection of membership proved above. This proves the isomorphism. For $v=0$, the usual bihomogeneous polynomial basis on $\mathbf P^1\times\mathbf P^1$ has $(am+1)(bm+1)$ elements.

Integration along the fibers of the proper submersion shows that $\nu$ is a smooth positive volume form. Its defining integration identity proves equality of the two norms. Pull back an orthonormal basis and compare its pointwise norms to obtain the first kernel identity; applying the same integration identity proves the second. The assertions include a zero-dimensional selected space, for which both kernels vanish.
\end{proof}

Even without a singular selecting weight, the growth is quadratic:
\[
 \lim_{m\to\infty}m^{-2}h^0(X,L^m)=ab,
 \qquad \lim_{m\to\infty}m^{-3}h^0(X,L^m)=0.
\]
The exact identities retain the base singularity information and the base kernel problem. A Hermitian metric on the threefold does not change this algebraic growth into cubic growth. This model links the closed-class cone, the descent of singularities and the lower-dimensional kernel theory, while leaving the nonlinear Hermitian equation distinct.
