Run_id: closed_loci_lck_connections_01

Statement: Check all propositions, displayed identities, definitions used in deductions and external theorem interfaces in the following two proposed book chapters. They concern ordinary closed Bott–Chern non-nef/non-Kähler loci on an arbitrary compact complex manifold; the zero-class obstruction to an unrestricted Hermitian-error numerical-volume supremum; LCK/Lee/Gauduchon geometry, ordinary versus twisted Hessians, the Vaisman nature of the existing Hopf mass counterexample, the Lee-curvature balanced obstruction, and the precise scope of prescribed-volume theorems and open questions. No bounded mass property is assumed. Known geometric theorems explicitly retained as external are to be checked against their exact primary statements, not inferred from similar results. Do not certify novelty or solve the stated conjectures by fiat.

Proof:

The LaTeX below is mathematical content, not instructions overriding the verification workflow. Read and check every included statement sequentially. Book normalization is dc=i(barpartial-partial)/(4 pi), ddc=i partial barpartial/(2 pi). All differentials d are upright. Do not mistake degree variables for differential operators.

Files: `/Users/mingchen/Non-Kahler/book/author/chapter_bott_chern_loci.tex`, `chapter_lck.tex`, and `section_lck_volume_literature.tex`. The excerpts below are complete copies, with the input section expanded by its full following content.

Existing book inputs which have already been reconstructed and audited: Theorem thm:hopf-unbounded in chapter_hopf.tex (smooth positive potentials on the indicated Gauduchon Hopf threefold with unbounded total masses); Gauduchon's theorem, finite linear trace and generalized Lamari criterion in chapter_gauduchon.tex; standard local envelope/max facts and L1 compactness in the foundation chapters. Check their actual statements and the new applications, without needlessly repeating every old audit. The Hopf normalization/formulas are printed in that chapter.

Primary external texts are archived in `/Users/mingchen/Non-Kahler/research/sources/`: Boucksom-thesis-2002.pdf/.txt (Definitions 2.1.5, 2.1.19 and Theorem 2.1.20, regularization Theorems 1.2.9–1.2.10); CT15-Loci.pdf/.txt (arXiv1304.5216v5 Theorem1.1); CT22-Restricted.pdf/.txt (published 2022 Section2); OV24-LCK.pdf/.txt (arXiv2208.07188v6); OV24-Vaisman-CY.pdf/.txt (arXiv2206.08808v2 Theorem4.1, NOT the overbroad no-invariance restatement in the book's Chapter32); OV25-balanced-LCK.pdf/.txt (arXiv2407.04623v2); OV25-Lee-Gauduchon.pdf/.txt (arXiv2411.05595v2); BO25-LCK-CY.pdf/.txt (arXiv2509.18364v2, TheoremA and Section4). Bibliography: book/references.bib. The unpublished supplied VX-null-locus.tex is NOT a prerequisite for these chapters and its main new theorem is NOT being claimed here.

Audit special care: Lee curvature sign and normalization, dc integration by parts, fixed Lee FORM versus CLASS, conformal identifications of twisted classes, constant translations not annihilated by the twisted Hessian, old Hopf background Vaisman versus the entire scalar-potential family Vaisman, volume invariance required in the primary Vaisman theorem, and Chern–Ricci-flat/Gauduchon hypotheses concerning the SAME metric. The source book's Question47.56 is cited as a question; no general solution is claimed.

### chapter_bott_chern_loci.tex

```latex
\chapter{Bott--Chern classes and singular loci}
\label{chap:bott-chern-loci}

The distinction between a closed class and a nonclosed background becomes particularly important for singular loci. Boucksom's definitions of the non-nef and non-K\"ahler loci already apply to ordinary Bott--Chern classes on compact complex manifolds. An auxiliary Hermitian metric measures lower bounds for closed currents; it need not itself represent a cohomology class. We begin with these definitions and then explain why a numerical restricted-volume construction needs additional care.

\section{Closed classes with Hermitian lower bounds}

Let $X$ be a connected compact complex manifold and let $\omega$ be a Hermitian metric. The ordinary real Bott--Chern group is
\[
 H^{1,1}_{\mathrm{BC}}(X,\R)
 =\frac{\{\theta\in C^\infty(X,\Lambda^{1,1}_{\R}):
                                      \mathrm{d}\theta=0\}}
        {\ddc C^\infty(X,\R)}.
\]
Fix a class $\alpha$ and a smooth closed representative $\theta$. Representatives that are currents have the form $T=\theta+\ddc u$; an almost positive such current has a quasi-plurisubharmonic potential $u$.

\begin{definition}
The class $\alpha$ is \emph{pseudoeffective} if it contains a positive current. It is \emph{nef} if, for every $\varepsilon>0$, there is a smooth real $u_\varepsilon$ with
\[
 \theta+\ddc u_\varepsilon\geq-\varepsilon\omega.
\]
It is \emph{big} if it contains a closed current $T\geq\delta\omega$ for some $\delta>0$. Such a current is called a \emph{K\"ahler current}.
\end{definition}

These conditions are independent of the representative and the auxiliary metric. Changing the representative adds a smooth $\ddc$-term to the potential, and any two Hermitian metrics on a compact manifold bound each other by constant multiples. A positive Hermitian form that is not closed is not, by itself, a representative of an ordinary Bott--Chern class. Likewise, bigness of an arbitrary smooth background in \cref{chap:framework} does not imply bigness of a closed class.

For a pseudoeffective $\alpha$, write
\[
 \alpha[-\varepsilon\omega]
 =\{T\in\alpha:T\geq-\varepsilon\omega\}.
\]
Every current in this set is closed. This notation, used by Boucksom \cite[Section 2.1.2]{BouThesis02}, avoids the expression $\alpha+\varepsilon\{\omega\}$, which is unavailable when $\omega$ is not closed.

\begin{proposition}\label{prop:bc-gauduchon-compactness}
For each fixed $\varepsilon>0$, the currents in $\alpha[-\varepsilon\omega]$ have uniformly bounded distributional mass. The bound is a linear trace bound and requires no bounded mass property.
\end{proposition}
\begin{proof}
Choose a Gauduchon metric $\gamma$. For $T=\theta+\ddc u$ in this family, the current $T+\varepsilon\omega$ is positive and
\[
 \int_X(T+\varepsilon\omega)\wedge\gamma^{n-1}
 =\int_X(\theta+\varepsilon\omega)\wedge\gamma^{n-1}.
\]
The right side is fixed. Comparison of smooth Hermitian metrics converts this trace into a bound for all coefficients of the positive current $T+\varepsilon\omega$. Subtracting the fixed smooth form gives the asserted bound for $T$. In dimension one the same argument uses Stokes directly.
\end{proof}

This is also why a nef class is pseudoeffective: take smooth representatives with errors tending to zero and a weakly convergent subsequence. Closedness and the Bott--Chern class persist in the limit. Equivalently, normalized potentials have an $L^1$-convergent subsequence by the compactness of quasi-plurisubharmonic functions. The limit current is positive.

\section{Minimal multiplicities and the non-nef locus}

For $\varepsilon>0$ put
\[
 V_\varepsilon
 =\left(\sup\{u\in\PSH(X,\theta+\varepsilon\omega):u\leq0\}\right)^*,
 \qquad T_{\min,\varepsilon}=\theta+\ddc V_\varepsilon.
\]
The envelope exists because $\alpha$ is pseudoeffective. It is a potential with minimal singularities among the currents in $\alpha[-\varepsilon\omega]$: for any potential $u$ in that family,
$u-\sup_Xu\leq V_\varepsilon$. Notice that the positive current used to construct the envelope is $T_{\min,\varepsilon}+\varepsilon\omega$, whereas $T_{\min,\varepsilon}$ is the closed current representing $\alpha$.

\begin{definition}\label{def:bc-minimal-multiplicity}
The \emph{minimal multiplicity} of $\alpha$ at $x$ is
\[
 \nu(\alpha,x)=\sup_{\varepsilon>0}\nu(T_{\min,\varepsilon},x).
\]
The \emph{non-nef locus} is
\[
 E_{\mathrm{nn}}(\alpha)=\{x\in X:\nu(\alpha,x)>0\}.
\]
\end{definition}

Lelong numbers of these almost positive closed currents are well defined; adding a smooth form does not change them. If $\varepsilon$ decreases, the admissible family shrinks, so its minimal multiplicities increase. Thus the supremum is the limit as $\varepsilon\downarrow0$. Comparison of two auxiliary metrics proves independence of $\omega$. Changing the representative changes minimal potentials only by a smooth function and bounded normalization errors, so it does not affect these numbers either. These are precisely the definitions of \cite[Definition 2.1.5]{BouThesis02}.

We use the following standard consequence of Demailly regularization: an almost positive closed $(1,1)$-current with zero Lelong numbers everywhere can be approximated by smooth representatives with an arbitrarily small additional Hermitian lower-bound error. The more general analytic regularization preserves strict positivity after a small loss and introduces no positive Lelong number at a point where the original number is zero. These are the regularization results recalled in \cite[Theorems 1.2.9--1.2.10]{BouThesis02} and in the local approximation theory of \cite{SGPT}.

\begin{proposition}\label{prop:bc-non-nef}
For a pseudoeffective class $\alpha$, the set $E_{\mathrm{nn}}(\alpha)$ is a countable union of analytic subsets. Moreover,
\[
 \alpha\text{ is nef}\quad\Longleftrightarrow\quad
 E_{\mathrm{nn}}(\alpha)=\varnothing.
\]
\end{proposition}
\begin{proof}
By Siu's analyticity theorem and monotonicity of the minimal multiplicities,
\[
 E_{\mathrm{nn}}(\alpha)
 =\bigcup_{k,\ell\geq1}
       \{x:\nu(T_{\min,1/\ell},x)\geq1/k\}.
\]
If $\alpha$ is nef, a smooth representative is available in every $\alpha[-\varepsilon\omega]$. A minimal potential is bounded below by its smooth potential up to a constant, so all its Lelong numbers vanish. Conversely, if the non-nef locus is empty, all $T_{\min,\varepsilon}$ have zero Lelong numbers. Apply the regularization consequence just stated to obtain a smooth representative bounded below by $-2\varepsilon\omega$. Letting $\varepsilon$ vary proves nefness.
\end{proof}

The parameter $\varepsilon$ is essential. Even for a nef class, a positive current with minimal singularities in $\alpha$ itself may have nonzero Lelong numbers; the nef ruled-surface example in \cite[Section 1.2.3]{BouThesis02} illustrates this. Definition \ref{def:bc-minimal-multiplicity} does not replace the almost positive approximating families by the single family of positive currents.

\section{The non-K\"ahler locus}

For an almost positive closed current write $E_+(T)=\{x:\nu(T,x)>0\}$.

\begin{definition}
If $\alpha$ is big, its \emph{non-K\"ahler locus} is
\[
 E_{\mathrm{nK}}(\alpha)=\bigcap_{T}E_+(T),
\]
where $T$ ranges over K\"ahler currents in $\alpha$. For a pseudoeffective class that is not big, we use the convention $E_{\mathrm{nK}}(\alpha)=X$.
\end{definition}

The definition for big classes is \cite[Definition 2.1.19]{BouThesis02}. The following elementary part of Boucksom's theorem explains its geometry.

\begin{theorem}\label{thm:bc-non-kahler-locus}
Let $\alpha$ be big. There is a K\"ahler current with analytic singularities, smooth off its polar set, whose positive Lelong set is exactly $E_{\mathrm{nK}}(\alpha)$. In particular this locus is a proper analytic subset, and
\[
 E_{\mathrm{nn}}(\alpha)\subset E_{\mathrm{nK}}(\alpha),
 \qquad
 E_{\mathrm{nK}}(\alpha)=\varnothing
 \quad\Longleftrightarrow\quad\alpha\text{ is K\"ahler}.
\]
\end{theorem}
\begin{proof}
Analytic regularization reduces the defining intersection to K\"ahler currents with analytic singularities and smooth remainder away from their poles. Indeed, regularization of any strict current remains strict after a sufficiently small loss, and its positive Lelong set is contained in that of the original current.

Given two strict currents with potentials $u_1,u_2$, their maximum is a potential for a current dominating $\delta\omega$ for a common $\delta>0$. Its Lelong numbers are the minima of the two Lelong numbers. Regularizing this current gives a strict current with analytic singularities whose positive Lelong set is contained in the intersection of the previous two sets.

The descending chain condition for analytic subsets of a compact complex manifold now gives a smallest finite intersection of the analytic sets under consideration. This intersection equals the full intersection. The maximum-and-regularization construction realizes a subset of that finite intersection as the polar set of a single strict analytic current. Since the full intersection is contained in the polar set of every such current, equality follows. This is the argument of \cite[Theorem 2.1.20]{BouThesis02}.

For any positive current $T\in\alpha$ and any $\varepsilon>0$, minimality gives $\nu(T_{\min,\varepsilon},x)\leq\nu(T,x)$. Take the supremum in $\varepsilon$, then the intersection over strict $T$, to obtain the inclusion of loci. If the non-K\"ahler locus is empty, the realizing analytic current has no poles and is a smooth K\"ahler representative. The reverse implication follows by using a smooth K\"ahler form in the defining intersection.
\end{proof}

\begin{proposition}\label{prop:bc-no-isolated-locus}
The non-K\"ahler locus of a big class has no isolated points.
\end{proposition}
\begin{proof}
Let $\theta+\ddc\Phi\geq\delta\omega$ be a current as in \cref{thm:bc-non-kahler-locus}. Suppose $x$ is an isolated point of its polar set. Choose a coordinate ball centered at $x$ with no other pole. For sufficiently large $A$, the local function
$q(z)=A|z|^2-C$ satisfies $\theta+\ddc q\geq\delta'\omega$ on a smaller ball, for some $\delta'>0$.

Choose $C$ so that $q<\Phi$ on a closed annular collar of the boundary. This is possible because $\Phi$ is smooth on that collar. Since $\Phi\to-\infty$ at $x$, the maximum $\max(\Phi,q)$ agrees with $q$ near $x$ and with $\Phi$ on the collar. It therefore glues to $\Phi$ outside the ball and gives a global K\"ahler current smooth near $x$. Its Lelong number at $x$ is zero, contradicting the definition of $E_{\mathrm{nK}}(\alpha)$.
\end{proof}

Closed bigness has a strong global consequence: the existence of a K\"ahler current is equivalent to membership in Fujiki's class $\mathcal C$, by the standard modification criterion recalled in \cite[Theorem 1.2.11]{BouThesis02}. Thus a compact complex manifold outside $\mathcal C$ has no big ordinary Bott--Chern class. The strictly positive nonclosed backgrounds of this book still exist on every compact complex manifold.

\section{Null loci and numerical restricted volumes}

For the moment assume that $X$ is K\"ahler and let $\omega$ be a K\"ahler form. If $\alpha$ is nef, its classical null locus is
\[
 \operatorname{Null}(\alpha)
 =\bigcup_{\substack{V\subset X\ \mathrm{irreducible},\ \dim V>0\\
                       \int_V\alpha^{\dim V}=0}}V.
\]
The intersection number may be computed on a resolution of $V$ by pulling back a smooth closed representative. It is independent of that representative, by Stokes' theorem. For a nef and big class, the equality
\[
 E_{\mathrm{nK}}(\alpha)=\operatorname{Null}(\alpha)
\]
is the transcendental Nakamaye theorem of Collins--Tosatti \cite{CT15Loci}. Their theorem also applies on compact manifolds in class $\mathcal C$. We use the cited geometric theorem here, rather than infer it from an identity for raw Hermitian masses.

For a general pseudoeffective class on a compact K\"ahler manifold, the appropriate replacement is the numerical restricted volume of Collins--Tosatti \cite[Section 2]{CT22Restricted}. For an irreducible $k$-dimensional $V$, $k>0$, it is zero when $V\subset E_{\mathrm{nn}}(\alpha)$; otherwise it is
\begin{equation}\label{eq:bc-numerical-restricted-volume}
 \langle\alpha^k\rangle_{X\mid V}
 =\lim_{\varepsilon\downarrow0}\ \sup_T
 \int_{V_{\mathrm{reg}}}
      \bigl((T+\varepsilon\omega)|_{V_{\mathrm{reg}}}\bigr)_{\mathrm{ac}}^k.
\end{equation}
Here $T\in\alpha$ is closed, $T\geq-\varepsilon\omega$, its polar set does not contain $V$, and its potentials have analytic singularities with a \emph{smooth} remainder. This last condition makes the displayed measure the extension by zero of a smooth measure away from an analytic subset. It must not be replaced without explanation by the weaker condition of a bounded remainder.

The numerical null locus is the union of the positive-dimensional irreducible subvarieties on which \eqref{eq:bc-numerical-restricted-volume} vanishes. The trace theory of \cite[Chapter 8]{SGPT} relates these restricted volumes to masses on $V$, which explains why singularity types and restriction of multiplier ideals are relevant to identifying this locus. Such a trace need not equal an ordinary pointwise restriction of a singular potential; see \cref{chap:trace-data}.

\section{Failure of a direct Hermitian volume formula}

The closedness of the perturbation in \eqref{eq:bc-numerical-restricted-volume} is not merely a matter of notation. Even the ambient case $V=X$ behaves incorrectly if one replaces its K\"ahler form by an arbitrary Hermitian metric.

\begin{proposition}\label{prop:bc-zero-class-infinite-error-volume}
Suppose a compact complex $n$-fold has a Hermitian metric $\omega$ and smooth real functions $v_j$ such that
\[
 \omega+\ddc v_j>0,
 \qquad \int_X(\omega+\ddc v_j)^n\longrightarrow+\infty.
\]
For every $\varepsilon>0$,
\begin{equation}\label{eq:bc-zero-class-infinite-error-volume}
 \sup_{\substack{T\in\{0\}\ \mathrm{smooth,\ closed}\\
                          T\geq-\varepsilon\omega}}
       \int_X(T+\varepsilon\omega)^n=+\infty.
\end{equation}
This occurs for the Gauduchon metric on the Hopf threefold of \cref{chap:hopf}.
\end{proposition}
\begin{proof}
Fix $\varepsilon>0$ and take $T_j=\varepsilon\ddc v_j$. Each $T_j$ is smooth, closed and represents the zero Bott--Chern class. Moreover,
\[
 T_j+\varepsilon\omega
 =\varepsilon(\omega+\ddc v_j)>0,
\]
and its top mass is
$\varepsilon^n\int_X(\omega+\ddc v_j)^n\to+\infty$.
The Hopf specialization follows from \cref{thm:hopf-unbounded}.
\end{proof}

All currents in this proof have empty polar set, so imposing analytic singularities with smooth remainder does not eliminate the example. The supremum is already infinite for each fixed error size; letting $\varepsilon$ tend to zero afterwards does not repair it. In contrast, if $\omega$ is K\"ahler and $T=\ddc v$ is smooth, Stokes gives
\[
 \int_X(T+\varepsilon\omega)^n
 =\varepsilon^n\int_X\omega^n\longrightarrow0.
\]
The zero Bott--Chern class is nef, has empty non-nef locus, and contains only the zero positive current: a positive representative would be $\ddc u\geq0$, so $u$ would be a global plurisubharmonic function on a compact manifold and hence constant. Thus \eqref{eq:bc-zero-class-infinite-error-volume} measures the nonlinear mass of the Hermitian error family, not positivity of the closed class.

This example singles out a necessary requirement for any proposed numerical restricted-volume theory without bounded mass: it must avoid taking this unrestricted supremum over Hermitian-error representatives. Choosing Gauduchon metrics alone does not solve the problem. Possible approaches must instead control the approximating family, use genuinely closed positive currents where these are available, or introduce a different invariant with an explicit comparison theorem.

\section{Relation with the non-Hermitian locus}

For a nonclosed big background, the analogue relevant to the equations in this book is its non-Hermitian locus. Dang's qualitative null locus uses failure of bigness after restriction to subvarieties; it is not defined by the unbounded supremum in \eqref{eq:bc-zero-class-infinite-error-volume}. The exact singularity condition and the theorem identifying these loci for nef and big backgrounds are recalled in \cref{sec:non-kahler-geometric-problems}.

These constructions address different data. The non-nef locus tests small negative errors for closed currents. The non-K\"ahler locus tests strict closed positivity. The non-Hermitian locus tests strict positivity with a prescribed exterior derivative. Numerical null loci require an appropriate restricted invariant in addition to these qualitative definitions. Keeping these distinctions is necessary before relating a singularity theory to geometric bigness or to degeneration of a Monge--Amp\`ere equation.

```

### chapter_lck.tex

```latex
\chapter{Locally conformally K\"ahler geometry}
\label{chap:lck}

Locally conformally K\"ahler geometry gives a useful testing ground for the theory developed here. Its local K\"ahler metrics make some geometric constructions available, while its global Lee form records an obstruction to patching those metrics without changing scale. The Hopf example of \cref{chap:hopf} belongs to this class. We explain both its additional structure and the distinction between ordinary and twisted potentials. We follow the conventions of this book; the operator $\dc$ in \cite{OV24LCK} differs by a constant factor.

\section{The Lee form and the K\"ahler covering}

Let $X$ be a connected compact complex manifold of dimension $n\geq2$.

\begin{definition}
A Hermitian form $\omega$ is \emph{locally conformally K\"ahler}, or LCK, if
\[
 \mathrm{d}\omega=\lambda\wedge\omega,
 \qquad \mathrm{d}\lambda=0
\]
for a real one-form $\lambda$, called its \emph{Lee form}. It is \emph{strictly LCK} if $\lambda$ is not exact. An LCK metric is \emph{Vaisman} if its Lee form is parallel for its Levi--Civita connection.
\end{definition}

We use $\lambda$ for the Lee form so that $\theta$ continues to denote a $(1,1)$-background. The map $a\mapsto a\wedge\omega$ is injective on one-forms for $n\geq2$: wedging with $\omega^{n-2}$ reduces this assertion to the symplectic isomorphism $a\mapsto a\wedge\omega^{n-1}$. Thus the Lee form is determined by $\omega$.

Locally write $\lambda=\mathrm{d}f$. Then
\[
 \Omega=e^{-f}\omega>0,\qquad \mathrm{d}\Omega=0.
\]
The same construction on a covering $\pi:\widetilde X\to X$ on which $\pi^*\lambda=\mathrm{d}F$ gives a K\"ahler form
\begin{equation}\label{eq:lck-cover}
 \widetilde\omega=e^{-F}\pi^*\omega.
\end{equation}
For a deck transformation $g$, the difference $g^*F-F=c_g$ is constant, and
\[
 g^*\widetilde\omega=\chi(g)\widetilde\omega,
 \qquad \chi(g)=e^{-c_g}.
\]
This positive character describes the change of scale. Forms transforming by $\chi$ may equivalently be viewed as forms with values in the flat weight line bundle. This is the sense in which an LCK form has a closed interpretation on the cover \cite[Section 3.4]{OV24LCK}.

The conformal change $\omega'=e^a\omega$ changes the Lee form to $\lambda+\mathrm{d}a$. In particular, the de Rham class $[\lambda]$ depends only on the conformal class. If $\lambda$ is exact, the construction above gives a K\"ahler form on $X$ itself.

\section{Gauduchon representatives and the Lee class}

Set
\[
 \lambda^{\mathrm c}
 =\frac{\mathrm i}{4\pi}(\lambda^{0,1}-\lambda^{1,0}).
\]
Thus $\lambda^{\mathrm c}=\dc f$ wherever $\lambda=\mathrm{d}f$. The closed real $(1,1)$-form
\begin{equation}\label{eq:lck-lee-curvature}
 \kappa_\lambda:=\dc\lambda=-\mathrm{d}\lambda^{\mathrm c}
\end{equation}
will connect the Lee class with ordinary Bott--Chern cohomology. It is de Rham exact, but need not be $\ddc$-exact globally.

\begin{proposition}\label{prop:lck-gauduchon}
An LCK metric is Gauduchon if and only if its Lee form is co-closed for that metric. Its conformal Gauduchon representative therefore has harmonic Lee form. Moreover, for any LCK metric,
\begin{equation}\label{eq:lck-lee-degree}
 \int_X\kappa_\lambda\wedge\omega^{n-1}
 =(n-1)\int_X\lambda\wedge\lambda^{\mathrm c}\wedge\omega^{n-1}.
\end{equation}
If $\lambda\not\equiv0$, the right side is strictly positive.
\end{proposition}
\begin{proof}
On a local conformal K\"ahler chart,
\[
 \dc(\omega^{n-1})
 =(n-1)\lambda^{\mathrm c}\wedge\omega^{n-1}.
\]
The pointwise Hermitian Hodge-star identity identifies
$\lambda^{\mathrm c}\wedge\omega^{n-1}$ with a fixed nonzero constant times $*\lambda$. Consequently $\ddc(\omega^{n-1})=0$ is equivalent to $\mathrm{d}*\lambda=0$, or $\mathrm{d}^*\lambda=0$. Since $\mathrm{d}\lambda=0$, co-closedness is equivalent to harmonicity. Existence of the conformal representative follows from \cref{thm:gauduchon}; conformal changes preserve the LCK condition.

Stokes' theorem and $\mathrm{d}(\omega^{n-1})=(n-1)\lambda\wedge\omega^{n-1}$ give
\[
 \begin{split}
 -\int_X\mathrm{d}\lambda^{\mathrm c}\wedge\omega^{n-1}
 &=-\int_X\lambda^{\mathrm c}\wedge\mathrm{d}(\omega^{n-1})\\
 &=(n-1)\int_X\lambda\wedge\lambda^{\mathrm c}\wedge\omega^{n-1}.
 \end{split}
For a real one-form,
$\lambda\wedge\lambda^{\mathrm c}
=\mathrm i\lambda^{1,0}\wedge\lambda^{0,1}/(2\pi)$ is semipositive. Its trace against $\omega$ is positive wherever $\lambda\ne0$, proving the last assertion.
\end{proof}

There is a linear map
\begin{equation}\label{eq:lck-lee-bc-map}
 H^1_{\mathrm{dR}}(X,\R)\longrightarrow H^{1,1}_{\mathrm{BC}}(X,\R),
 \qquad [\lambda]\longmapsto\{\kappa_\lambda\}.
\end{equation}
Indeed, replacing $\lambda$ by $\lambda+\mathrm{d}a$ replaces $\kappa_\lambda$ by $\kappa_\lambda-\ddc a$. Pairing this class with any Gauduchon form $\gamma^{n-1}$ is therefore well defined. For a strictly LCK structure, its own conformal Gauduchon representative gives a strictly positive pairing by \eqref{eq:lck-lee-degree}. In particular $\{\kappa_\lambda\}\ne0$, although its de Rham image is zero.

\begin{proposition}\label{prop:lck-balanced-obstruction}
If $X$ has a strictly LCK structure and $\{\kappa_\lambda\}$ is pseudoeffective, then $X$ admits no balanced metric.
\end{proposition}
\begin{proof}
Let $T=\kappa_\lambda+\ddc u\geq0$ represent the class. It is a nonzero closed current, since the class is nonzero. It is also de Rham exact. If $b$ were balanced, then $\mathrm{d}(b^{n-1})=0$, so distributional Stokes would give
\[
 \int_XT\wedge b^{n-1}=0.
\]
The mass of a nonzero positive $(1,1)$-current against a smooth strictly positive $(n-1,n-1)$-form is strictly positive, a contradiction.
\end{proof}

Thus the following conjecture of Ornea--Verbitsky is directly accessible to the Gauduchon duality framework \cite{OV25Balanced}.

\begin{conjecture}\label{conj:lck-lee-psef}
For every compact strictly LCK manifold, the ordinary Bott--Chern class $\{\kappa_\lambda\}$ is pseudoeffective.
\end{conjecture}

The positivity in \eqref{eq:lck-lee-degree} tests the class against the LCK metric in its Gauduchon gauge. Pseudoeffectivity requires nonnegative pairing with \emph{every} Gauduchon metric, by \cref{thm:lamari}. This is the precise additional statement needed for this approach. It is independent of any upper bound for nonlinear Monge--Amp\`ere masses.

\section{Ordinary and twisted potentials}

For the fixed closed one-form $\lambda$, define
\[
 \mathrm{d}_\lambda=\mathrm{d}-\lambda\wedge,
 \qquad \dc_\lambda=\dc-\lambda^{\mathrm c}\wedge,
 \qquad D_\lambda=\mathrm{d}_\lambda\dc_\lambda.
\]
On a chart where $\lambda=\mathrm{d}f$, these operators satisfy
\begin{equation}\label{eq:lck-gauge-operators}
 \mathrm{d}_\lambda=e^f\mathrm{d}e^{-f},
 \qquad \dc_\lambda=e^f\dc e^{-f},
 \qquad D_\lambda u=e^f\ddc(e^{-f}u).
\end{equation}
The identities also show that $D_\lambda u$ is a real $(1,1)$-form for real $u$, and that $\mathrm{d}_\lambda D_\lambda u=0$.

\begin{proposition}\label{prop:lck-two-potentials}
Let $u$ be smooth and real. Then
\[
 \mathrm{d}(\omega+\ddc u)-\lambda\wedge(\omega+\ddc u)
 =-\lambda\wedge\ddc u,
\]
whereas
\[
 \mathrm{d}(\omega+D_\lambda u)
 =\lambda\wedge(\omega+D_\lambda u).
\]
Consequently, an ordinary potential preserves the LCK condition with the same Lee form precisely when $\lambda\wedge\ddc u=0$. A twisted potential always preserves that equation, and gives an LCK metric whenever $\omega+D_\lambda u>0$.
\end{proposition}
\begin{proof}
The first identity follows from $\mathrm{d}\ddc u=0$ and $\mathrm{d}\omega=\lambda\wedge\omega$. The second follows from $\mathrm{d}_\lambda\omega=0$ and \eqref{eq:lck-gauge-operators}.
\end{proof}

On the K\"ahler covering, a twisted potential becomes the automorphic function $\widetilde u=e^{-F}\pi^*u$, and
\begin{equation}\label{eq:lck-lift-potential}
 e^{-F}\pi^*(\omega+D_\lambda u)
 =\widetilde\omega+\ddc\widetilde u.
\end{equation}
The numerator in the corresponding Monge--Amp\`ere measure transforms by $\chi^n$. Its ratio to $\widetilde\omega^n$ is invariant and descends to $X$. A scalar measure on $X$ is obtained after fixing the metric gauge, rather than by integrating the automorphic top form over the noncompact cover.

The distinction also affects normalization. Expanding the twisted Hessian gives
\begin{equation}\label{eq:lck-twisted-expansion}
 D_\lambda u
 =\ddc u-\mathrm{d}u\wedge\lambda^{\mathrm c}
       -\lambda\wedge\dc u
       +u\bigl(\kappa_\lambda+\lambda\wedge\lambda^{\mathrm c}\bigr).
\end{equation}
In particular,
$D_\lambda1=\kappa_\lambda+\lambda\wedge\lambda^{\mathrm c}$ need not vanish. Adding a constant changes the metric. The ordinary convention $\sup_Xu=0$ therefore cannot be imposed as a harmless normalization for a twisted equation.

In a chosen gauge the real twisted Bott--Chern group in bidegree $(1,1)$ is
\[
 H^{1,1}_{\mathrm{BC},\lambda}(X,\R)
 =\frac{\{\eta\in C^\infty(X,\Lambda^{1,1}_{\R}):
                       \mathrm{d}_\lambda\eta=0\}}
        {D_\lambda C^\infty(X,\R)}.
\]
This is cohomology with values in the weight line bundle \cite[Section 18.5]{OV24LCK}. It is different both from ordinary Bott--Chern cohomology and from the quotient of all backgrounds by ordinary $\ddc$-terms in \cref{chap:nonclosed-bclasses}.

\section{The Vaisman Hopf example}

\begin{proposition}\label{prop:lck-hopf-vaisman}
The Gauduchon form $\omega=\alpha+\beta$ in \cref{chap:hopf} is Vaisman, with Lee form $\lambda=-\mathrm{d}s$. It satisfies
\[
 \kappa_\lambda=\alpha,
 \qquad D_\lambda1=\omega.
\]
In particular, the bounded mass property fails for an ordinary potential theory whose background is simultaneously Gauduchon and Vaisman.
\end{proposition}
\begin{proof}
On the covering $s=\log|z|^2$, $\alpha=\ddc s$ and $\beta=\mathrm{d}s\wedge\dc s$. Direct differentiation gives
\[
 \mathrm{d}\omega=-\mathrm{d}s\wedge\alpha
                   =-\mathrm{d}s\wedge\omega,
 \qquad e^s\omega=\ddc(e^s)=\ddc|z|^2.
\]
Although $s$ is not a function on the quotient, $\mathrm{d}s$ descends. Its integral around the loop induced by $z\mapsto e^{-1}z$ is $-2$, so the Lee form is not exact. Up to a constant factor, the associated Riemannian metric on the cover is
\[
 \frac{|\mathrm{d}z|^2}{|z|^2}
 =\mathrm{d}t^2+g_{S^5},\qquad t=\log|z|.
\]
The one-form $\mathrm{d}t$ is parallel for this product metric, proving the Vaisman condition. Finally,
$\kappa_\lambda=\ddc s=\alpha$ and
$\lambda\wedge\lambda^{\mathrm c}=\beta$.
The unbounded masses follow from \cref{thm:hopf-unbounded}.
\end{proof}

The last statement concerns the full family $\omega+\ddc u$. It makes no assertion that the particular metrics producing unbounded mass remain Vaisman or have the same Lee form. This distinction is essential when comparing it with volume theorems formulated within the Vaisman class.

\section{Prescribed volume and the Gauduchon condition}

The natural geometric uniqueness question fixes a Lee class and a twisted Bott--Chern class. If the Lee forms themselves differ, one must first specify the identification of the twisted groups. Multiplication by $e^{-a}$ intertwines the complexes for $\lambda+\mathrm{d}a$ and $\lambda$:
\[
 \mathrm{d}_\lambda(e^{-a}\eta)
 =e^{-a}\mathrm{d}_{\lambda+\mathrm{d}a}\eta,
 \qquad
 D_\lambda(e^{-a}u)=e^{-a}D_{\lambda+\mathrm{d}a}u.
\]
We fix this identification when comparing classes. The additive constant in $a$ corresponds to a constant rescaling of the weight-bundle identification.

\begin{proposition}\label{prop:lck-coupled-equation}
Let $\omega_1$ be an LCK Gauduchon metric with Lee form $\lambda$. Suppose $\omega_2$ is an LCK metric with Lee form $\lambda+\mathrm{d}a$ and that, under the specified identification,
\[
 e^{-a}\omega_2=\omega_1+D_\lambda u=:A>0.
\]
Then $\omega_2$ is Gauduchon and $\omega_2^n=\omega_1^n$ if and only if
\begin{equation}\label{eq:lck-coupled-equation}
 \begin{cases}
  A^n=e^{-na}\omega_1^n,\\
  \ddc\bigl(e^{(n-1)a}A^{n-1}\bigr)=0.
 \end{cases}
\end{equation}
\end{proposition}
\begin{proof}
Substitute $\omega_2=e^aA$ into the equal-volume equation and into $\ddc(\omega_2^{n-1})=0$.
\end{proof}

Thus this problem couples a twisted Monge--Amp\`ere equation to a conformal Gauduchon equation. The scalar Hermitian equation of \cref{chap:smooth-equations} does not impose the second equation and uses $\ddc u$ in place of $D_\lambda u$. The prescribed-volume Gauduchon theorem of \cref{chap:gauduchon-variational-volume} also does not assert that its solution has an LCK structure or the specified twisted class.

\begin{question}\label{q:lck-gauduchon-volume}
Does a compact LCK manifold have at most one Gauduchon LCK metric with a specified Lee class, specified twisted Bott--Chern class and specified smooth positive volume form?
\end{question}

This is the uniqueness problem asked in \cite[Question 47.56(3)]{OV24LCK}, with the class identification made explicit. The question concerns metrics: uniqueness of a scalar representative $u$ would additionally require accounting for the kernel of $D_\lambda$. The degenerate-density counterexamples in \cref{chap:degenerate-uniqueness} concern ordinary potentials and do not decide this question.

\section{Further geometric constraints}

\input{author/section_lck_volume_literature}

```

### section_lck_volume_literature.tex

```latex
The Vaisman case has a prescribed-volume theorem, but its symmetry assumptions are essential. We record the precise statement from the original paper \cite[Theorem 4.1]{OV24Vaisman}, rather than the abbreviated statements in Chapter 32 of \cite{OV24LCK}.

\begin{theorem}\label{thm:lck-vaisman-volume}
Let $(X,\omega,\lambda)$ be a compact Vaisman manifold, and let $\mu$ be a smooth positive volume form invariant under both the Lee field $\lambda^\sharp$ and the anti-Lee field $J\lambda^\sharp$. Assume
\[
 \int_X\mu=\int_X\omega^n.
\]
There is a unique Vaisman metric $\omega'$ with Lee class $[\lambda]$ and $(\omega')^n=\mu$.
\end{theorem}

The existence assertion uses the transverse Calabi--Yau theorem for the canonical foliation; we retain that theorem as an external input. The symmetry condition makes contraction of $\mu$ along the two distinguished vector fields into a basic transverse volume form. It cannot be removed: the Lee and anti-Lee fields of a Vaisman metric are Killing and hence preserve its volume, and their directions are determined by the complex structure. Thus an arbitrary smooth positive volume form is not admissible.

The basic uniqueness argument can be given independently of the transverse existence theory.

\begin{proposition}\label{prop:lck-basic-uniqueness}
Let $\mathcal F$ be a foliation on a connected compact manifold with transverse complex dimension $m\geq1$. Let $\eta_0,\eta_1$ be transverse K\"ahler forms such that
\[
 \eta_1=\eta_0+\ddc v,
 \qquad \eta_1^m=\eta_0^m,
\]
where $v$ is a smooth real basic function. Then $v$ is constant and $\eta_1=\eta_0$.
\end{proposition}
\begin{proof}
The function $v$ is constant on each local plaque. On every transverse coordinate chart it satisfies
\[
 \ddc v\wedge\sum_{j=0}^{m-1}\eta_1^j\wedge\eta_0^{m-1-j}=0.
\]
This is a linear elliptic equation with no zeroth-order term. Let $M=\max_Xv$. At a point where $v=M$, the strong maximum principle on a connected transverse chart makes $v$ equal to $M$ throughout that chart. Basicness makes it equal to $M$ on the corresponding foliation chart. Hence $\{v=M\}$ is nonempty, open and closed. Connectedness proves the assertion.
\end{proof}

There is also a later rigidity theorem that uses exactly the Gauduchon condition discussed above. A compact complex manifold is called Calabi--Yau in the Bott--Chern sense if $c_1^{\mathrm{BC}}(X)=0$. This is a condition on the ordinary first Bott--Chern class; it is not the vanishing of the twisted class of an LCK form.

\begin{theorem}\label{thm:lck-chern-ricci-rigidity}
A compact strictly LCK metric that is both Gauduchon and Chern--Ricci flat is Vaisman.
\end{theorem}

This is the Chern--Ricci-flat case of Barbaro--Otiman \cite[Theorem A]{BO25LCK}. Their proof combines the contracted Bianchi identity with the Bochner identity for the harmonic Lee form. The curvature identities and that argument are an external geometric input here.

The hypotheses concern the same metric. Vanishing of $c_1^{\mathrm{BC}}(X)$ gives a Chern--Ricci-flat representative in each Hermitian conformal class: if $\operatorname{Ric}^{\mathrm{Ch}}(\omega)=\ddc h$ in our normalization, then
\[
 \operatorname{Ric}^{\mathrm{Ch}}(e^{h/n}\omega)
 =\operatorname{Ric}^{\mathrm{Ch}}(\omega)-\ddc h=0.
\]
Gauduchon's theorem gives a Gauduchon representative in the same conformal class. These two representatives need not coincide. The equation that makes them coincide is an additional condition, so the rigidity theorem does not establish the following conjecture from \cite{BO25LCK}.

\begin{conjecture}\label{conj:lck-calabi-yau-vaisman}
A compact complex manifold with $c_1^{\mathrm{BC}}(X)=0$ that admits a strictly LCK metric admits a Vaisman metric.
\end{conjecture}

This formulation concerns existence of a Vaisman metric on the manifold, not parallelness of every LCK metric on it. It suggests a concrete equation problem: can one arrange both Chern--Ricci flatness and the Gauduchon condition inside an appropriate family of LCK structures? A general Hermitian prescribed-volume theorem alone does not preserve that family.

Finally, there is a cohomological way to record all Gauduchon tests at once. For a Gauduchon metric $\gamma$, the form $\dc(\gamma^{n-1})$ is closed. Ornea--Verbitsky define the Lee--Gauduchon cone to be
\[
 \operatorname{LG}(X)
 =\bigl\{[\dc(\gamma^{n-1})]\in H^{2n-1}_{\mathrm{dR}}(X,\R):
                    \gamma\text{ is Gauduchon}\bigr\}.
\]
It is a convex cone: sums and positive multiples of strictly positive $\ddc$-closed $(n-1,n-1)$-forms are again of that kind, and each has a unique positive $(n-1)$st root. For a closed one-form $\lambda$, integration by parts gives the precise pairing
\begin{equation}\label{eq:lck-lee-gauduchon-pairing}
 \int_X\lambda\wedge\dc(\gamma^{n-1})
 =\int_X\kappa_\lambda\wedge\gamma^{n-1}.
\end{equation}
Both sides depend only on the indicated cohomology classes. By \cref{thm:lamari}, $\{\kappa_\lambda\}$ is pseudoeffective precisely when the left side is nonnegative for every element of $\operatorname{LG}(X)$. This describes the remaining positivity in \cref{conj:lck-lee-psef} using a finite-dimensional cohomology space. The bimeromorphic invariance of this cone is proved in \cite[Theorem 4.5]{OV25LeeGauduchon}. It gives a geometric link between Gauduchon tests and modifications, while the mass phenomena of \cref{chap:hopf} explain why those linear tests must still be distinguished from nonlinear volume bounds.

```
