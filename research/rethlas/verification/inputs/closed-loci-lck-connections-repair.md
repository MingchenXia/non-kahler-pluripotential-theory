Run_id: closed_loci_lck_connections_repair_01

Statement: Verify the repaired strict Vaisman scope, the new closed-bigness obstruction for strict LCK manifolds, the precise regularization input and the corrected Gauduchon prescribed-volume reference, including their integration with the already verified Chern–Ricci rigidity proof. This is a bounded follow-up to closed_loci_lck_connections_01, which found a zero-Lee counterexample and a misdirected internal reference. Both older audit records must remain unchanged. The full Chern–Ricci tensor proof has separately passed lck_chern_ricci_rigidity_01; its new interface is the strictly LCK theorem below. No bounded mass property is assumed.

Proof:

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
for a real one-form $\lambda$, called its \emph{Lee form}. It is \emph{strictly LCK} if $\lambda$ is not exact. A strictly LCK metric is \emph{Vaisman} if its Lee form is parallel for its Levi--Civita connection.
\end{definition}

The strictness convention excludes the K\"ahler case from the word Vaisman. On a compact connected manifold a nonzero parallel one-form cannot be exact: the differential of a global potential vanishes at a maximum, and a parallel form has constant length. Thus a nonzero parallel Lee form is automatically nowhere zero and nonexact.

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
\]
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

\begin{corollary}\label{cor:lck-no-closed-big-class}
A compact strictly LCK manifold admits no big ordinary Bott--Chern class. In particular it lies outside Fujiki's class $\mathcal C$.
\end{corollary}
\begin{proof}
If there were a big closed class, the modification criterion recalled in \cref{chap:bott-chern-loci} would give a K\"ahler modification $\pi:Y\to X$. The form $\pi^*\kappa_\lambda$ is closed and de Rham exact. The K\"ahler $\partial\bar\partial$-lemma gives a smooth real function $h$ on $Y$ with $\pi^*\kappa_\lambda=\ddc h$. Push forward this equality as currents. Since $\pi$ has degree one, $\pi_*\pi^*\kappa_\lambda=\kappa_\lambda$, and pushforward commutes with $\ddc$. Thus $\kappa_\lambda=\ddc(\pi_*h)$, so its Bott--Chern class vanishes. One may use currents to compute this class; alternatively, taking the trace of this equation against a smooth metric and using elliptic regularity shows that the distribution $\pi_*h$ is smooth. This contradicts the positive Gauduchon pairing above. The same modification criterion proves the last assertion.
\end{proof}

For the Hopf example below, $\kappa_\lambda=\alpha$ is smooth semipositive and therefore nef. It has empty non-nef locus, whereas its non-K\"ahler locus is all of $X$, by the non-big convention in \cref{chap:bott-chern-loci}. These closed-class statements coexist with the strictly positive nonclosed background $\omega$ used for its Monge--Amp\`ere equations.

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



The Vaisman case has a prescribed-volume theorem, but its symmetry assumptions are essential. We record the precise statement from the original paper \cite[Theorem 4.1]{OV24Vaisman}, rather than the abbreviated statements in Chapter 32 of \cite{OV24LCK}.

\begin{theorem}\label{thm:lck-vaisman-volume}
Let $(X,\omega,\lambda)$ be a compact Vaisman manifold, with $\lambda\not\equiv0$, and let $\mu$ be a smooth positive volume form invariant under both the Lee field $\lambda^\sharp$ and the anti-Lee field $J\lambda^\sharp$. Assume
\[
 \int_X\mu=\int_X\omega^n.
\]
There is a unique Vaisman metric $\omega'$ with Lee class $[\lambda]$ and $(\omega')^n=\mu$.
\end{theorem}

The existence assertion uses the transverse Calabi--Yau theorem for the canonical foliation; we retain that theorem as an external input. The symmetry condition makes contraction of $\mu$ along the two distinguished vector fields into a basic transverse volume form. It cannot be removed: the Lee and anti-Lee fields of a Vaisman metric are Killing and hence preserve its volume, and their directions are determined by the complex structure. Thus an arbitrary smooth positive volume form is not admissible.



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

Thus this problem couples a twisted Monge--Amp\`ere equation to a conformal Gauduchon equation. The scalar Hermitian equation of \cref{chap:smooth-equations} does not impose the second equation and uses $\ddc u$ in place of $D_\lambda u$. The prescribed-volume Gauduchon theorem, \cref{thm:stw-volume}, also does not assert that its solution has an LCK structure or the specified twisted class.

\begin{problem}\label{q:lck-gauduchon-volume}
Does a compact LCK manifold have at most one Gauduchon LCK metric with a specified Lee class, specified twisted Bott--Chern class and specified smooth positive volume form?
\end{problem}

This is the uniqueness problem asked in \cite[Question 47.56(3)]{OV24LCK}, with the class identification made explicit. The question concerns metrics: uniqueness of a scalar representative $u$ would additionally require accounting for the kernel of $D_\lambda$. The degenerate-density counterexamples in \cref{chap:degenerate-uniqueness} concern ordinary potentials and do not decide this question.

\section{Further geometric constraints}

\input{author/section_lck_volume_literature}


The precise regularization statement used in the closed-loci chapter is:

We use two standard forms of Demailly regularization, with the precise lower bounds of \cite[Theorem 2.1]{Bou04Zariski}. If $T\geq\gamma$ is closed and almost positive, smooth representatives $\theta_j\in\{T\}$ satisfy $\theta_j\geq\gamma-C\lambda_j\omega$, where the continuous functions $\lambda_j$ decrease pointwise to $\nu(T,\cdot)$. When all Lelong numbers vanish, Dini's theorem makes this loss uniformly small. Analytic regularization gives currents $T_j\in\{T\}$ with $T_j\geq\gamma-\varepsilon_j\omega$, $\varepsilon_j\downarrow0$, and $\nu(T_j,x)\leq\nu(T,x)$. Thus it preserves strict positivity after a small loss and introduces no positive Lelong number at a point where the original number is zero. These are also the regularization principles recalled in \cite[Theorems 1.2.9--1.2.10]{BouThesis02} and in \cite{SGPT}.



The actual internal Gauduchon theorem cited above is:

\begin{theorem}[Sz\'ekelyhidi--Tosatti--Weinkove]
\label{thm:stw-volume}
Assume $n\geq2$. Fix a Hermitian form $\gamma_0$, a Gauduchon form $\gamma$, and smooth real $F$. There is a unique pair $(u,b)$ with $u$ smooth and $\sup_Xu=0$ such that the positive $(n-1,n-1)$-form
\[
 \Gamma_u=\gamma_0^{n-1}+\ddc u\wedge\gamma^{n-2}
 +\operatorname{Re}\left(
     \frac{\mathrm i}{2\pi}\partial u\wedge\bar\partial(\gamma^{n-2})
   \right)
\]
has a positive root $\eta_u^{n-1}=\Gamma_u$ satisfying
\[
 \eta_u^n=e^{F+b}\gamma^n.
\]
\end{theorem}

The separately reconstructed Chern–Ricci proof concludes that the Lee form is parallel. Its theorem assumes a compact STRICTLY LCK metric, both Gauduchon and Chern–Ricci flat; strictness ensures the Lee form cannot vanish identically. The conclusion therefore satisfies the repaired definition of Vaisman. No conclusion is asserted for arbitrary representatives of the same conformal class.

The new corollary uses only the standard Kähler ddbar lemma and the Kähler-current/modification criterion as external inputs. On a degree-one modification, pushforward of the pullback of a smooth form equals that form because the equality holds off the exceptional set and can also be tested by integration; the smooth forms on the source give no mass to the analytic exceptional set. The scalar elliptic trace operator applies to degree-zero distributions, giving smoothness of pi_*h from its smooth ddbar. The Hopf specialization uses the already proved identity kappa_lambda=alpha>=0 and does not infer a nonlinear mass bound.
