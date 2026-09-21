Run_id: lee_gauduchon_cone_01

Statement: Verify the entire supplied reconstruction of Lee–Gauduchon cone duality and bimeromorphic invariance on a connected compact complex n-manifold, n>=2, with no LCK or bounded mass assumption. Check all definitions, the kernel and lineality, the finite-dimensional image/open-cone argument, the strict dual formula OUTSIDE the kernel, pseudoeffectivity and Bott–Chern injectivity under modifications, the H1 blowup proof, analytic weak factorization, canonical cohomology identifications, and the balanced/Fujiki/Hopf consequences. Do not take the Ornea–Verbitsky duality or invariance theorems as granted: these are the conclusions to reconstruct, and their citations provide attribution only. No novel result is claimed.

Internal proved premises, in /Users/mingchen/Non-Kahler/book/author:
1. chapter_gauduchon.tex: thm:gauduchon gives a conformal Gauduchon metric; prop:gauduchon-trace is the FULL distributional trace identity for unbounded genuine qpsh potentials; thm:lamari says PSH(X,theta) is nonempty iff integral theta wedge gamma^(n-1)>=0 for every Gauduchon gamma, for any smooth real (1,1) background theta. Its proof also supplies the positive (n-1)st-root matrix formula. These inputs impose no BMP and are already reconstructed/audited.
2. chapter_lck.tex: kappa_lambda=dc lambda=-d lambda^c for a smooth closed real one-form, and kappa_(lambda+da)=kappa_lambda-ddc a. For an LCK metric omega with nonzero Lee form, integral kappa_lambda wedge omega^(n-1)=(n-1)integral lambda wedge lambda^c wedge omega^(n-1)>0. The balanced obstruction and ordinary closed-bigness obstruction are proved there.
3. chapter_hopf.tex and chapter_lck.tex: the Hopf threefold is (C^3 minus {0})/(z maps to e^(-1)z), with s=log|z|^2, lambda=-ds, alpha=ddc s>=0, omega=alpha+ds wedge dc s Gauduchon and Vaisman, kappa_lambda=alpha. The underlying smooth product identification follows from radial polar coordinates. BMP fails on this example. The cone proof must not assume that ALL ordinary perturbations remain LCK/Vaisman.
4. Standard inputs permitted, with their exact uses to be checked: de Rham theory/Poincare duality and projection formula for a proper degree-one smooth map; Thom isomorphism/long exact sequence for an oriented smooth normal bundle; general position against analytic strata; finite-dimensional separation of an open convex cone; local ddbar potentials for a smooth closed real (1,1)-form; the psh characterization of distributions with positive complex Hessian; elliptic regularity for a scalar Hermitian trace; the compact Kahler ddbar lemma. These are standard references allowed by the user, not claimed to be reconstructed here.

External reference to verify, NOT to weaken to the algebraic version:
- Abramovich–Karu–Matsuki–Wlodarczyk, Torification and factorization of birational maps, JAMS15(3),531–572 (2002), arXiv:math/9904135v4, Theorem0.3.1, case(2): a bimeromorphic map between compact complex manifolds factors into blowups/blowdowns with smooth centers in that category, preserving a common isomorphism open set. Original source https://arxiv.org/pdf/math/9904135v4 ; archived /Users/mingchen/Non-Kahler/research/sources/AKMW02-factorization.pdf and .txt (Section0.3, page2). Theorem0.1.1 alone is not sufficient because it is algebraic. The source version's theorem locations were independently checked.
Attribution source:
- Ornea–Verbitsky, The Lee–Gauduchon cone on complex manifolds, arXiv:2411.05595v2, Theorems3.11 and4.5, https://arxiv.org/abs/2411.05595v2 ; archived research/sources/OV25-Lee-Gauduchon.pdf and .txt. The present proof uses full-trace positivity and finite-dimensional separation to spell out the kernel in the strict formula. It does not copy the original infinite-dimensional affine separation or universal-cover potential argument as a premise.

Pay particular attention to the dc d sign, full-current versus NPP traces, exclusion of K_X in strict inequalities, openness in W_X rather than the whole de Rham group, nonzero positive current versus zero BC class, genuine local pullback of psh potentials under a modification, distributional pushforward/elliptic smoothing, and natural direction of the Poincare-dual map. The first modification lemma does not assume a pullback operation for arbitrary currents. The space image(j_X) is NOT asserted to equal every de Rham-exact Bott–Chern class. Follow the normal sequential verification and reference workflow; do not edit the staged TeX, manuscript, or previous results. Persist all findings and the final JSON, then stop.

Proof:

\section{The Lee--Gauduchon cone}
\label{sec:lee-gauduchon-cone}

The Lee--Gauduchon cone records all Gauduchon tests in a finite-dimensional cohomology space. Its dual description and bimeromorphic invariance are due to Ornea--Verbitsky \cite[Theorems 3.11 and 4.5]{OV25LeeGauduchon}. We give the arguments, keeping track of the kernel on which every test vanishes. Throughout this section $X$ is a connected compact complex manifold of dimension $n\geq2$; an LCK structure is not required.

Put $V_X=H^1_{\mathrm{dR}}(X,\R)$, and recall the linear map
\[
 j_X:V_X\longrightarrow H^{1,1}_{\mathrm{BC}}(X,\R),
 \qquad j_X([\lambda])=\{\kappa_\lambda\},
 \qquad \kappa_\lambda=\dc\lambda.
\]
Here $\lambda$ is a smooth closed real one-form. Let
\[
 K_X=\ker j_X,\qquad
 W_X=K_X^\perp\subset H^{2n-1}_{\mathrm{dR}}(X,\R),
\]
where the annihilator uses the Poincar\'e pairing
\[
 \langle[\lambda],a\rangle=\int_X\lambda\wedge a.
\]
Finally, let
\[
 \mathcal C_X
 =\{[\lambda]\in V_X:j_X([\lambda])\text{ is pseudoeffective}\}.
\]
This cone concerns the image of $j_X$. We do not identify that image with the entire kernel of the map from Bott--Chern to de Rham cohomology.

\begin{lemma}\label{lem:lee-gauduchon-kernel}
The space $K_X$ consists of the de Rham classes of real parts of closed holomorphic one-forms. Moreover,
\[
 \mathcal C_X\cap(-\mathcal C_X)=K_X.
\]
\end{lemma}
\begin{proof}
If $j_X([\lambda])=0$, write $\dc\lambda=\ddc f$ for a smooth real function $f$. Since $\dc\mathrm{d}=-\mathrm{d}\dc$, the form $\lambda+\mathrm{d}f$ is both $\mathrm{d}$-closed and $\dc$-closed. Its $(1,0)$-part is therefore holomorphic and closed: the two equations separate the $\partial$ and $\bar\partial$ derivatives. Thus $\lambda+\mathrm{d}f$ is the real part of the closed holomorphic form $2(\lambda+\mathrm{d}f)^{1,0}$. Conversely, the real part of a closed holomorphic form is closed for both operators, and its image under $j_X$ is zero.

Suppose $[\lambda]\in\mathcal C_X\cap(-\mathcal C_X)$. There are positive currents
\[
 T_+=\kappa_\lambda+\ddc u\geq0,
 \qquad T_-=-\kappa_\lambda+\ddc v\geq0.
\]
Their sum is $\ddc(u+v)$. Its mass against any fixed Gauduchon form $\gamma^{n-1}$ is zero by distributional integration by parts. Positivity forces $T_++T_-=0$, hence $T_+=T_-=0$. In particular $\kappa_\lambda=-\ddc u$. Taking a smooth Hermitian trace and applying elliptic regularity shows that $u$ is smooth, so $j_X([\lambda])=0$ in smooth Bott--Chern cohomology. The reverse inclusion follows because the zero class is pseudoeffective.
\end{proof}

\begin{definition}
The \emph{Lee--Gauduchon cone} is
\[
 \operatorname{LG}(X)
 =\bigl\{[\dc(\gamma^{n-1})]:
                    \gamma\text{ is a Gauduchon metric on }X\bigr\}.
\]
\end{definition}

For a closed one-form $\lambda$ and any smooth real $(n-1,n-1)$-form $\Gamma$ with $\ddc\Gamma=0$, integration by parts gives
\begin{equation}\label{eq:lck-lee-gauduchon-pairing}
 \int_X\lambda\wedge\dc\Gamma
 =\int_X\kappa_\lambda\wedge\Gamma.
\end{equation}
The form $\dc\Gamma$ is closed, and both sides depend only on the relevant cohomology classes. In particular the class on the left annihilates $K_X$.

\begin{proposition}\label{prop:lee-gauduchon-open}
The cone $\operatorname{LG}(X)$ is nonempty, convex and open in $W_X$. Its linear span is $W_X$.
\end{proposition}
\begin{proof}
Let $\mathcal Z_X$ be the real vector space of smooth $(n-1,n-1)$-forms $\Gamma$ satisfying $\ddc\Gamma=0$, and set
\[
 q_X(\Gamma)=[\dc\Gamma].
\]
First we show $q_X(\mathcal Z_X)=W_X$. The inclusion into $W_X$ follows from \eqref{eq:lck-lee-gauduchon-pairing}. If $[\lambda]$ annihilates the image of $q_X$, its pairing with every Gauduchon form is zero. The generalized Lamari criterion, \cref{thm:lamari}, implies that both $\kappa_\lambda$ and $-\kappa_\lambda$ have pseudoeffective Bott--Chern classes. By \cref{lem:lee-gauduchon-kernel}, $[\lambda]\in K_X$. Thus the image and $W_X$ have the same annihilator in $V_X$. The finite-dimensional nondegenerate Poincar\'e pairing proves their equality.

Let $\mathcal Z_X^+$ denote the strictly positive forms in $\mathcal Z_X$. Every such form has a unique positive $(n-1)$st root, by the matrix construction used in the proof of \cref{thm:lamari}. This root is Gauduchon. Hence
\[
 \operatorname{LG}(X)=q_X(\mathcal Z_X^+).
\]
Gauduchon's theorem makes $\mathcal Z_X^+$ nonempty. It is convex and stable under positive scaling. Fix $\Gamma_0\in\mathcal Z_X^+$. For every $\Gamma\in\mathcal Z_X$, compactness implies $\Gamma+t\Gamma_0>0$ for large $t$. Thus $\mathcal Z_X^+$ spans $\mathcal Z_X$, proving the span assertion.

To see openness directly, choose forms $\Gamma_1,\ldots,\Gamma_r\in\mathcal Z_X$ whose images form a basis of $W_X$. If $\Gamma\in\mathcal Z_X^+$, then $\Gamma+\sum_i t_i\Gamma_i$ remains strictly positive for all sufficiently small real $t_i$. Its image describes a neighborhood of $q_X(\Gamma)$ in $W_X$. This also covers $W_X=\{0\}$, with the empty basis.
\end{proof}

\begin{theorem}\label{thm:lee-gauduchon-duality}
The cone $\mathcal C_X$ is closed, and
\[
 \mathcal C_X
 =\{\xi\in V_X:\langle\xi,a\rangle\geq0
                         \text{ for every }a\in\operatorname{LG}(X)\}.
\]
Conversely,
\[
 \operatorname{LG}(X)
 =\{a\in W_X:\langle\xi,a\rangle>0
                         \text{ for every }\xi\in\mathcal C_X\setminus K_X\}.
\]
Thus strict positivity is tested only outside the kernel. In particular, it is never required against the zero class.
\end{theorem}
\begin{proof}
The first equality is exactly \cref{thm:lamari} applied to the smooth closed background $\kappa_\lambda$, using \eqref{eq:lck-lee-gauduchon-pairing}. It expresses $\mathcal C_X$ as an intersection of closed half-spaces, so this cone is closed.

If $a=[\dc(\gamma^{n-1})]\in\operatorname{LG}(X)$ and $\xi=[\lambda]\in\mathcal C_X\setminus K_X$, choose $T=\kappa_\lambda+\ddc u\geq0$. This current is nonzero, since otherwise $j_X(\xi)=0$ by elliptic regularity as above. Therefore
\[
 \langle\xi,a\rangle
 =\int_XT\wedge\gamma^{n-1}>0.
\]

For the converse, suppose $a\in W_X\setminus\operatorname{LG}(X)$. Finite-dimensional separation of a point from a nonempty open convex cone gives a nonzero functional $\ell\in W_X^*$ such that
\[
 \ell(a)\leq0,\qquad \ell(b)\geq0
                   \quad(b\in\operatorname{LG}(X)).
\]
Indeed, in the usual separating inequalities the constant can be taken to be zero by scaling elements of the cone. By Poincar\'e duality, $\ell$ is represented by a class $\xi\in V_X$, modulo $K_X$. Its nonzero restriction means $\xi\notin K_X$. The first equality in the theorem implies $\xi\in\mathcal C_X$, contradicting the required strict inequalities for $a$. This proves the second equality. If $\operatorname{LG}(X)=W_X$, there is no point to separate and the same conclusion holds.
\end{proof}

\subsection{Modification of the positive classes}

The proof of invariance uses closed positive $(1,1)$-currents. Their pullback is defined through local plurisubharmonic potentials. There is no corresponding pullback operation for arbitrary currents.

\begin{lemma}\label{lem:lee-gauduchon-modification}
Let $\pi:Y\to X$ be a modification between connected compact complex manifolds, and let $\theta$ be a smooth closed real $(1,1)$-form on $X$. Then
\[
 \{\theta\}\text{ is pseudoeffective}
 \quad\Longleftrightarrow\quad
 \{\pi^*\theta\}\text{ is pseudoeffective}.
\]
The pullback on real Bott--Chern cohomology in bidegree $(1,1)$ is injective.
\end{lemma}
\begin{proof}
Suppose $T=\theta+\ddc u\geq0$. On a coordinate ball write $\theta=\ddc h$ with $h$ smooth. The function $h+u$ is plurisubharmonic, so $(h+u)\circ\pi$ is plurisubharmonic on the inverse image. It is not identically $-\infty$ on any open subset: every open subset of $Y$ meets the locus where $\pi$ is an isomorphism, and $h+u$ has no open pole set. The local pullbacks therefore define a positive current
\[
 \pi^*T=\pi^*\theta+\ddc(u\circ\pi).
\]
This also proves local integrability of the composed potential. The constructions agree on overlaps, where the local potentials differ by a smooth pluriharmonic function.

Conversely, let $S=\pi^*\theta+\ddc v\geq0$. Pushforward preserves positivity and commutes with differentiation, giving
\[
 \pi_*S=\theta+\ddc(\pi_*v)\geq0.
\]
Here $\pi_*v$ initially denotes a scalar distribution. The identity $\pi_*\pi^*\theta=\theta$ follows by integration on the isomorphism locus: the exceptional sets have smooth volume zero, and $\pi$ has degree one. Locally, the distribution $\pi_*v+h$ has positive complex Hessian and hence a plurisubharmonic representative. Thus $\pi_*v$ is represented by a genuine quasi-plurisubharmonic function, proving pseudoeffectivity downstairs.

Finally, if $\pi^*\theta=\ddc f$ for a smooth real $f$, pushforward gives $\theta=\ddc(\pi_*f)$. Taking a smooth elliptic trace shows that the scalar distribution $\pi_*f$ is smooth. Hence $\{\theta\}=0$, proving injectivity.
\end{proof}

We recall the degree-one topological fact needed for a blowup, including its short proof.

\begin{lemma}\label{lem:lee-gauduchon-blowup-cohomology}
If $\pi:Y\to X$ is the blowup of a smooth center, then
\[
 \pi^*:H^1_{\mathrm{dR}}(X,\R)\longrightarrow
                    H^1_{\mathrm{dR}}(Y,\R)
\]
is an isomorphism. Its Poincar\'e dual is the isomorphism
$\pi_*:H^{2n-1}_{\mathrm{dR}}(Y,\R)\to H^{2n-1}_{\mathrm{dR}}(X,\R)$.
\end{lemma}
\begin{proof}
A blowup along a divisor is an isomorphism. Otherwise let $Z$ be the center, of complex codimension $r\geq2$, and $E$ the exceptional divisor. Identify
$U=X\setminus Z=Y\setminus E$. By the Thom isomorphism and the long exact sequence of the pair,
\[
 H^k(X,U;\R)=H^{k-2r}(Z;\R)=0\quad(k=1,2).
\]
Hence restriction $H^1(X,\R)\to H^1(U,\R)$ is an isomorphism. On $Y$, the same argument gives $H^1(Y,U;\R)=H^{-1}(E;\R)=0$, so restriction $H^1(Y,\R)\to H^1(U,\R)$ is injective. It is also surjective: every class on $U$ extends to $X$, and its pullback extends it to $Y$. Commutativity of restrictions proves the first assertion. For a disconnected center the argument applies to each disjoint component. Poincar\'e duality and the projection formula give the second assertion.
\end{proof}

\begin{theorem}\label{thm:lee-gauduchon-bimeromorphic}
Let $X$ and $Y$ be bimeromorphic connected compact complex manifolds. Under the natural identification of $H^1_{\mathrm{dR}}$ and its Poincar\'e-dual identification of $H^{2n-1}_{\mathrm{dR}}$, their spaces $K_X,W_X$ and cones $\mathcal C_X,\operatorname{LG}(X)$ agree.
\end{theorem}
\begin{proof}
First suppose $\pi:Y\to X$ is a blowup with smooth center. Holomorphic pullback commutes with $\dc$, so
\[
 j_Y(\pi^*\xi)=\pi^*j_X(\xi).
\]
By \cref{lem:lee-gauduchon-modification}, membership in $\mathcal C_X$ is equivalent to membership of the pullback in $\mathcal C_Y$, and membership in $K_X$ is likewise preserved in both directions. By \cref{lem:lee-gauduchon-blowup-cohomology}, every degree-one class upstairs occurs in this way. Thus the degree-one isomorphism identifies the two cones and kernels. Its dual identifies $W_Y$ with $W_X$, and \cref{thm:lee-gauduchon-duality} gives
\[
 \pi_*\operatorname{LG}(Y)=\operatorname{LG}(X).
\]

For a general bimeromorphic map, use the standard analytic weak factorization theorem: it factors into blowups and blowdowns along smooth centers between compact complex manifolds \cite[Theorem 0.3.1, analytic case]{AKMW02}. Apply the preceding argument at every step. These degree-one identifications are the natural ones and do not depend on the chosen factorization. Indeed, they agree on a common open set where the bimeromorphic map is an isomorphism, and restriction to such a set is injective in degree one: one-dimensional cycles can be moved off the strata of its analytic complement, each of real codimension at least two. The dual identifications are consequently canonical as well.
\end{proof}

\subsection{Geometric consequences and the mass obstruction}

\begin{corollary}\label{cor:lee-gauduchon-zero}
The following conditions are equivalent:
\[
 0\in\operatorname{LG}(X),\qquad
 \operatorname{LG}(X)=W_X,\qquad
 \mathcal C_X=K_X.
\]
A balanced metric implies these conditions. On a manifold in Fujiki's class $\mathcal C$, one has $W_X=\{0\}$ and $\operatorname{LG}(X)=\{0\}$.
\end{corollary}
\begin{proof}
An open cone in a finite-dimensional vector space that contains zero is the entire space: scale a neighborhood of zero to reach any point. The two dual descriptions in \cref{thm:lee-gauduchon-duality} now prove the equivalences, including the case $W_X=\{0\}$. If $b$ is balanced, its form $b^{n-1}$ is closed and of pure type, hence also $\dc$-closed. It is Gauduchon and represents zero in $\operatorname{LG}(X)$.

On a compact K\"ahler manifold the $\partial\bar\partial$-lemma gives $j_X=0$: every $\kappa_\lambda$ is closed and de Rham exact. Thus $K_X=V_X$ and $W_X=0$. Nonemptiness gives $\operatorname{LG}(X)=\{0\}$. Bimeromorphic invariance extends this conclusion to Fujiki's class $\mathcal C$.
\end{proof}

Consequently, a nonzero pseudoeffective class in the image of $j_X$ obstructs balanced metrics throughout the bimeromorphic class. For an LCK Lee class, this recovers the mechanism of \cref{prop:lck-balanced-obstruction}. Its known positive pairing against its own Gauduchon metric does not establish pseudoeffectivity: the latter still requires all Gauduchon tests, as stated in \cref{conj:lck-lee-psef}.

For the Hopf threefold of \cref{chap:hopf}, the covering description identifies the underlying manifold with $S^1\times S^5$, so $V_X=\R[\lambda]$. The class $j_X([\lambda])=\{\alpha\}$ is nonzero by \eqref{eq:lck-lee-degree}, and is pseudoeffective because $\alpha\geq0$. Negative multiples are not pseudoeffective, since their pairing against the fixed Gauduchon metric is negative. Thus
\[
 K_X=0,\qquad \mathcal C_X=\R_{\geq0}[\lambda],\qquad
 \operatorname{LG}(X)=\{a\in H^5_{\mathrm{dR}}(X,\R):
                                  \langle[\lambda],a\rangle>0\}.
\]
This explicit invariant is compatible with the failure of bounded Monge--Amp\`ere mass on the same manifold. The cone records linear cohomological tests. It supplies neither an upper mass bound nor the nonlinear tail estimates needed for equation limits.
