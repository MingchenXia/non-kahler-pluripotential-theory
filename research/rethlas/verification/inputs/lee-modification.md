Run_id: lee_modification_01

Run scope: Bounded verification through the normal Rethlas workflow. The parent owns manuscript edits, build and release. Restrict writes to normal verifier tools, memory and results. Do not alter book/editorial/blueprint/status/changelog files, frozen inputs, original references or historical reports. Do not commit or push.

Statement: Verify the revised proof of degree-one de Rham cohomology invariance for every modification between connected compact complex manifolds, and its application to the known bimeromorphic invariance of the Lee--Gauduchon cone. Also check the shortened span argument: nonempty openness implies that the cone spans its ambient annihilator space. This is a proof revision of known results, not a novelty claim. The degree-one lemma previously treated only blowups; the final cone invariance statement is unchanged. The revised proof replaces analytic weak factorization by a common graph resolution.

Definitions and conventions: X is a connected compact complex n-manifold, n>=2. d^c is the fixed positive multiple of i(bar-partial minus partial), with dd^c=i/(2pi) partial bar-partial; d d^c=-d^c d. V_X=H^1_dR(X,R). A closed real one-form lambda gives a closed real (1,1)-form kappa_lambda=d^c lambda; its de Rham class is zero, but its Bott--Chern class need not vanish. Put j_X([lambda])={kappa_lambda}_BC, K_X=ker j_X, W_X=K_X^perp in H^(2n-1)_dR(X,R) under the integral Poincare pairing. C_X consists of the classes xi for which j_X(xi) is pseudoeffective. LG(X)={[d^c(gamma^(n-1))] : gamma is a Gauduchon metric}. This only tests the image of j_X; it is not identified with the full kernel of BC-to-de-Rham.

Accepted internal/classical inputs:
1. Gauduchon's theorem gives a smooth strictly positive ddc-closed (n-1,n-1)-form on every compact complex manifold. Every strictly positive (n-1,n-1)-form has a unique positive (n-1)st root. The proved Lamari criterion says a smooth closed (1,1)-form represents a pseudoeffective BC class iff it pairs nonnegatively with every such Gauduchon form. The pseudoeffective BC cone contains no nonzero line (the book proves this using a fixed Gauduchon trace). Finite-dimensional separation and Poincare duality are accepted.
2. Proper analytic subsets of a connected complex manifold have locally finite Whitney stratifications with strata of real codimension at least two; if complex codimension is at least two, all strata have real codimension at least four. Relative general position is accepted in its usual smooth-topological form: a finite singular chain can, after subdivision and smoothing, be perturbed to miss strata whose real codimension exceeds the dimension of the chain; the perturbation may fix its boundary when that boundary already misses the closed stratified set. Check carefully how this fact is used to obtain the H_1 surjection/isomorphism and hence the H^1 restriction statements. Real coefficients and the universal coefficient theorem identify cohomology with the dual of homology.
3. A modification to a smooth complex manifold is an isomorphism outside an analytic subset of the target of complex codimension at least two. The source complement of that locus is a proper analytic subset and may contain divisors. A bimeromorphic map of compact complex manifolds admits a smooth compact resolution of its graph, with two proper modifications to the original manifolds. These classical analytic resolution facts are accepted; do not assume a common Kahler resolution or weak factorization.
4. A distribution with positive complex Hessian has a plurisubharmonic representative, and scalar elliptic regularity applies to a distribution with smooth Laplacian. Local ddc potentials exist for smooth closed real (1,1)-forms. Pullback of a closed positive (1,1)-current under a modification is defined through composed local psh potentials; check nontriviality and integrability as included below. Pushforward of currents commutes with d and ddc and preserves positivity. The projection formula and degree-one identity pi_*pi^*theta=theta are accepted with the included explanation off exceptional sets.

Checks of particular importance: Proper analytic complements can contain divisors upstairs, so only injectivity of H^1(Y)->H^1(U) is available directly. Surjectivity on Y comes by extending every class from U to X and pulling it back. Downstairs the codimension-two hypothesis is essential for moving bounding two-chains. No invariance of H^2 or full Bott--Chern cohomology is asserted; only injectivity of BC pullback in (1,1) is used. Holomorphicity implies j_Y pi^*=pi^* j_X. Check the orientation and inverse in the common-resolution identification (q^*)^(-1)p^*:H^1(X)->H^1(Y), its dual, and independence from the resolution via injective restriction. The zero-dimensional space W_X={0} must be included in openness/span and strict duality.

The unchanged kernel, duality and positive-current lemmas are included to make the argument self-contained relative to these inputs. Verify the text sequentially, distinguishing accepted classical inputs from deductions made in the supplied proof.

Proof:

\begin{lemma}\label{lem:lee-gauduchon-kernel}
The space $K_X$ consists of the de Rham classes of real parts of closed holomorphic one-forms. Moreover,
\[
 \mathcal C_X\cap(-\mathcal C_X)=K_X.
\]
\end{lemma}
\begin{proof}
If $j_X([\lambda])=0$, write $\dc\lambda=\ddc f$ for a smooth real function $f$. Since $\dc\mathrm{d}=-\mathrm{d}\dc$, the form $\lambda+\mathrm{d}f$ is both $\mathrm{d}$-closed and $\dc$-closed. Its $(1,0)$-part is therefore holomorphic and closed: the two equations separate the $\partial$ and $\bar\partial$ derivatives. Thus $\lambda+\mathrm{d}f$ is the real part of the closed holomorphic form $2(\lambda+\mathrm{d}f)^{1,0}$. Conversely, the real part of a closed holomorphic form is closed for both operators, and its image under $j_X$ is zero.

By \cref{prop:psef-cone-compact-base}, the pseudoeffective Bott--Chern cone contains no nonzero line. Thus $j_X(\xi)$ and $-j_X(\xi)$ are both pseudoeffective exactly when $j_X(\xi)=0$. This is the asserted identity $\mathcal C_X\cap(-\mathcal C_X)=K_X$.
\end{proof}

\begin{definition}\label{def:lee-gauduchon-cone}
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
Gauduchon's theorem makes $\mathcal Z_X^+$ nonempty. It is convex and stable under positive scaling.

To see openness directly, choose forms $\Gamma_1,\ldots,\Gamma_r\in\mathcal Z_X$ whose images form a basis of $W_X$. If $\Gamma\in\mathcal Z_X^+$, then $\Gamma+\sum_i t_i\Gamma_i$ remains strictly positive for all sufficiently small real $t_i$. Its image describes a neighborhood of $q_X(\Gamma)$ in $W_X$. This also covers $W_X=\{0\}$, with the empty basis. Since a nonempty open subset spans its ambient vector space, the span assertion follows.
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

If $a=[\dc(\gamma^{n-1})]\in\operatorname{LG}(X)$ and $\xi=[\lambda]\in\mathcal C_X\setminus K_X$, choose $T=\kappa_\lambda+\ddc u\geq0$. This current is nonzero because it represents the nonzero class $j_X(\xi)$. Therefore
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

The degree-one cohomology can be compared directly under a modification.

\begin{lemma}\label{lem:lee-gauduchon-blowup-cohomology}
If $\pi:Y\to X$ is a modification between connected compact complex manifolds, then
\[
 \pi^*:H^1_{\mathrm{dR}}(X,\R)\longrightarrow
                    H^1_{\mathrm{dR}}(Y,\R)
\]
is an isomorphism. Its Poincar\'e dual is the isomorphism
$\pi_*:H^{2n-1}_{\mathrm{dR}}(Y,\R)\to H^{2n-1}_{\mathrm{dR}}(X,\R)$.
\end{lemma}
\begin{proof}
For a proper analytic subset $A$ of a connected complex manifold $M$, restriction
$H^1(M,\R)\to H^1(M\setminus A,\R)$ is injective, and is an isomorphism
if $A$ has complex codimension at least two. Indeed, choose a Whitney
stratification of $A$. General position moves every one-cycle off its
strata, which have real codimension at least two. If those codimensions
are at least four, it also moves every bounding two-chain off the strata,
relative to its boundary. Thus the map on first homology is surjective
in the first case and bijective in the second. Dualizing over $\R$ gives
the asserted restriction statements.

Since $X$ is smooth, there is an analytic subset $A\subset X$ of complex
codimension at least two such that $\pi$ is an isomorphism over
$U=X\setminus A$. Restriction from $X$ to $U$ is therefore an isomorphism,
whereas restriction from $Y$ to $\pi^{-1}U$ is injective. Every class on
$\pi^{-1}U\simeq U$ extends to $X$ and hence pulls back to a class on $Y$.
The commutative restriction diagram proves that $\pi^*$ is an isomorphism.
Poincar\'e duality and the projection formula give the assertion for $\pi_*$.
\end{proof}

\Needspace{10\baselineskip}
\begin{theorem}\label{thm:lee-gauduchon-bimeromorphic}
Let $X$ and $Y$ be bimeromorphic connected compact complex manifolds. Under the natural identification of $H^1_{\mathrm{dR}}$ and its Poincar\'e-dual identification of $H^{2n-1}_{\mathrm{dR}}$, their spaces $K_X,W_X$ and cones $\mathcal C_X,\operatorname{LG}(X)$ agree.
\end{theorem}
\begin{proof}
First let $\pi:Y\to X$ be a modification. Holomorphic pullback commutes with $\dc$, so
\[
 j_Y(\pi^*\xi)=\pi^*j_X(\xi).
\]
By \cref{lem:lee-gauduchon-modification}, membership in $\mathcal C_X$ is equivalent to membership of the pullback in $\mathcal C_Y$, and membership in $K_X$ is likewise preserved in both directions. By \cref{lem:lee-gauduchon-blowup-cohomology}, every degree-one class upstairs occurs in this way. Thus the degree-one isomorphism identifies the two cones and kernels. Its dual identifies $W_Y$ with $W_X$, and \cref{thm:lee-gauduchon-duality} gives
\[
 \pi_*\operatorname{LG}(Y)=\operatorname{LG}(X).
\]

For a bimeromorphic map between $X$ and $Y$, resolve its graph to obtain
modifications $p:Z\to X$ and $q:Z\to Y$ from one smooth compact manifold.
The preceding argument applies to both maps and identifies the cones and
kernels via $(q^*)^{-1}p^*$ and its Poincar\'e dual. These identifications
are independent of the resolution: they agree on a common open set where
the original map is an isomorphism, and the injectivity of degree-one
restriction proved above determines each class uniquely. The dual
identifications are consequently canonical as well.
\end{proof}

