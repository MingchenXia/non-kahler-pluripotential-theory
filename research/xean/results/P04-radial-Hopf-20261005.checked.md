# P04: checked radial Gauduchon LCK theorem

On H_n=(C^n minus 0)/<z maps to e z>, n>=2, every positive smooth two-periodic radial volume F and negative Lee period determine exactly one Gauduchon LCK metric C(r)alpha+D(r)beta in the entire stated radial family. It has an explicit positive global actual twisted potential and zero weighted Bott-Chern class. Every nonconstant F gives a non-Vaisman metric. Exact gauge covariance and both original coupled equations yield uniqueness for radial candidates even with a nonradial difference potential. General original P04 is not solved.

Root-developed proof, complete native original-task review, statement-only independent reconstruction with notes=[] yielding seven complete ordinary notes, and a separate scoped final comparison all use Xean gpt-6.1-sol xhigh, concurrency one. The original-task review remains INCONCLUSIVE because unrestricted criteria are unanswered; the scoped comparison is PASS. All complete reports, independent notes and final source were actually read. Their full mathematical chains were separately assessed, including opposite sign conventions for the ODE parameter. No verdict, candidate flag or computational observation supplies mathematical authority. No accepted-note full-solver graph is claimed.

Exact primary documentary applications of Ornea-Verbitsky 2206.08808v2 Definition 2.3 and 2208.07188v6 Definition 18.34 and Question 47.56(3) were separately assessed against the actual statements. The invariant-volume Vaisman theorem is background comparison only. All needed radial arguments are supplied directly. Broader bibliography in reconstruction note 6 is observational, not an indispensable premise or priority certification. No unequal metric counterexample or unrestricted uniqueness is asserted. Model-assisted checking is not journal peer review.

## Complete frozen comparison assembly

# P04 full comparison of the restricted radial Hopf theorem

The review object is the complete restricted A--F theorem, not unrestricted original P04. The exact original context and frozen root argument are retained below unchanged. All seven independent ordinary notes and the current scope-qualified article follow. Historical pending labels record chronology. No prior report, verdict or candidate flag is supplied as authority.

## Whole unchanged root assembly and original context

# P04 complete restricted radial Hopf argument

Independently check every claim and the entire article. Assess the specified radial theorem separately from original requirements: unrestricted P04 closure remains false. No earlier review, verdict or accepted companion paper is a mathematical premise.

## Exact unchanged original task

{
  "problem": "Let X be a connected compact complex manifold of dimension n>=2. A smooth positive real (1,1) form omega is locally conformally Kahler (LCK) if d omega=lambda wedge omega for a smooth closed real one-form lambda. A metric is Gauduchon if dd^c(omega^(n-1))=0. Use d^c=(i/(4 pi))(barpartial-partial), so dd^c=(i/(2 pi))partial barpartial, and for a real one-form put lambda^c=(i/(4 pi))(lambda^(0,1)-lambda^(1,0)). For closed lambda define d_lambda=d-lambda wedge, d_lambda^c=d^c-lambda^c wedge and D_lambda=d_lambda d_lambda^c. Locally lambda=df gives D_lambda u=e^f dd^c(e^(-f)u). The real twisted Bott-Chern group is the space of smooth real d_lambda-closed (1,1) forms modulo D_lambda of smooth real functions.\nFix a Lee de Rham class, a chosen gauge identification of the twisted groups for its different representatives, and a smooth strictly positive volume form. If two candidate metrics have Lee forms lambda and lambda+da, identify the groups by multiplication by e^(-a). Equality of their twisted classes means\n omega_2=e^a A, A=omega_1+D_lambda u>0\nfor a smooth real u. The additive constant in a is fixed as part of the chosen identification. Suppose omega_1 is Gauduchon and LCK, and a,u are smooth real functions satisfying the exact coupled system\n A^n=e^(-n a)omega_1^n,\n dd^c(e^((n-1)a)A^(n-1))=0.\nThen omega_2 is a Gauduchon LCK metric with the specified class data and exactly the same smooth strictly positive volume as omega_1.\nQuestion: must omega_2=omega_1 for every compact LCK manifold and these fixed class data? Equivalently, prove uniqueness of the metric for specified Lee class, identified twisted Bott-Chern class and smooth positive volume, or give an exact compact counterexample satisfying both equations and the actual class identification. The case with nonexact Lee form is essential. The target is metric uniqueness, not uniqueness of the scalar u: the kernel of D_lambda and conformal compensation can represent the same metric in different ways. D_lambda1 need not vanish, so adding a constant to u is not a harmless normalization.\nThe ordinary Hermitian Monge-Ampere uniqueness theorem uses dd^c instead of D_lambda and does not impose the Gauduchon equation. Counterexamples with a degenerate density or ordinary potentials do not answer this question. The prescribed-volume result for Vaisman metrics and volumes invariant under both Lee and anti-Lee fields is only a restricted background result and does not settle arbitrary Gauduchon LCK metrics.\nPrimary question: Ornea-Verbitsky, Principles of Locally Conformally Kahler Geometry, arXiv:2208.07188v6, Question47.56(3), printed683-684. No candidate proof, construction or extra geometric hypothesis is supplied.",
  "completionCriteria": "Resolve the complete metric-uniqueness question with the original smooth positive and coupled twisted hypotheses. A positive answer proves equality e^a(omega_1+D_lambda u)=omega_1 for every permissible pair, including non-Vaisman metrics and noninvariant volumes, without replacing the coupled problem by ordinary Hermitian Monge-Ampere uniqueness. A negative answer explicitly exhibits the compact complex manifold, LCK Gauduchon forms, closed cohomologous Lee forms, fixed twisted-class identification, smooth potentials a,u, the exact common strictly positive volume, and unequal metrics satisfying both equations. Merely adding a constant to a potential, changing the class identification or using kernel representatives of the same metric is not a counterexample. Verify every imported premise against primary sources and independently reconstruct the entire proof. Restricted Vaisman results alone do not suffice."
}

## Complete standalone article

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\PP}{\mathbb P}
\newcommand{\D}{D_\lambda}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Prescribed radial volumes for Gauduchon LCK metrics\newline
on scalar Hopf manifolds}
\author{}
\date{}
\begin{document}
\maketitle
\noindent\textbf{Working draft.} Independent mathematical review,
reconstruction and final comparison are pending. The unrestricted
Gauduchon LCK uniqueness problem remains open.
\begin{abstract}
On every scalar Hopf manifold of complex dimension at least two,
a strictly positive smooth radial volume and a negative Lee period
determine exactly one radial Gauduchon locally conformally K\"ahler
metric. A periodic scalar equation gives existence, while a strict
ordering of its solutions gives uniqueness. Every resulting metric has
an explicit positive twisted potential and zero twisted Bott--Chern
class in the actual Lee gauge. A nonconstant radial volume always
produces a non-Vaisman metric. The conclusion concerns the stated
radial family and does not assert uniqueness among all LCK metrics.
\end{abstract}

\section{Forms, class data and statement}
Use $d^c=\frac{i}{4\pi}(\bar\partial-\partial)$ and
$\ddc=\frac{i}{2\pi}\partial\bar\partial$. Put $m=n-1$, where
$n\ge2$, and set
\[
 H_n=(\mathbb C^n\setminus\{0\})/\langle z\mapsto ez\rangle,
 \qquad q:H_n\longrightarrow\PP^m.
\]
Let $\kappa$ be the Fubini--Study form with $\int_{\PP^m}\kappa^m=1$.
The circle-valued function $r=\log\|z\|^2\pmod2$ has a global
differential, and
\[
 \alpha=q^*\kappa=\ddc r,
 \qquad \beta=dr\wedge d^cr.
\]
Here $\alpha$ is closed, semipositive and of rank $m$; $\beta$ is
semipositive of rank one and positive in the complex radial direction.
Their kernels are complementary. Direct differentiation gives
\begin{equation}\label{eq:forms}
 \alpha^n=\beta^2=0,\qquad
 d\beta=-dr\wedge\alpha,\qquad
 d^c\beta=-\alpha\wedge d^cr,\qquad
 \ddc\beta=-\alpha^2.
\end{equation}
On a fiber, $d^cr=d\arg z/(2\pi)$ and $r$ has period two;
therefore $\int_{q^{-1}(x)}\beta=2$ and
$\int_{H_n}\alpha^m\wedge\beta=2$.

Consider precisely the metrics
\begin{equation}\label{eq:radial}
 \omega=C(r)\alpha+D(r)\beta,
 \qquad C,D\in C^\infty(\mathbb R/2\mathbb Z),\quad C,D>0.
\end{equation}
Every such form is LCK, with actual closed Lee form
\begin{equation}\label{eq:lee}
 \lambda=l(r)\,dr,\qquad l=\frac{C'-D}{C},
 \qquad d\omega=\lambda\wedge\omega.
\end{equation}
The Lee form is unique since wedging one-forms with a positive
$(1,1)$ form is injective in complex dimension at least two.
Its period is
\begin{equation}\label{eq:period}
 L=\int_0^2l(r)\,dr=-\int_0^2\frac{D(r)}{C(r)}\,dr<0.
\end{equation}
Thus the Lee form is nonexact. Two radial Lee forms have the same
de Rham class exactly when their periods agree: their difference is
the differential of a smooth periodic function in that case, and the
radial circle detects the period in the converse direction.

For a closed real one-form $\lambda$, use
$d_\lambda=d-\lambda\wedge$,
$d_\lambda^c=d^c-\lambda^c\wedge$ and
$D_\lambda=d_\lambda d_\lambda^c$, where
$\lambda^c=\frac{i}{4\pi}(\lambda^{0,1}-\lambda^{1,0})$.
Locally, $\lambda=df$ gives
$D_\lambda u=e^f\ddc(e^{-f}u)$.
The real twisted Bott--Chern group is the space of smooth real
$d_\lambda$-closed $(1,1)$ forms modulo the image of $D_\lambda$
on smooth real functions. This is the normalized convention for the
weighted group of \cite[Definition 18.34]{OVbook}.

\begin{theorem}\label{thm:main}
For every positive smooth two-periodic function $F$ and every
$L_0<0$, there is exactly one metric of the form \eqref{eq:radial}
which is Gauduchon, has volume
\[
 \omega^n=nF(r)\alpha^m\wedge\beta,
\]
and has Lee period $L_0$. Its actual Lee form admits a positive
smooth global function $U$ such that $\omega=D_\lambda U$.
In particular its twisted Bott--Chern class is zero. If $F$ is
nonconstant, the resulting metric is not Vaisman.
\end{theorem}

Theorem~\ref{thm:main} proves uniqueness within the entire stated
radial family without assuming equality of twisted classes.
It consequently applies to radial candidates satisfying the fixed
class identification of \cite[Question 47.56(3)]{OVbook}.
That question has no radial assumption and remains unanswered here.
The known Vaisman prescribed-volume theorem assumes invariance
under the Lee and anti-Lee fields \cite[Theorem 4.1]{OV24}; the
present scalar argument does not invoke that theorem.

\section{The exact periodic equation}
For any smooth two-periodic scalar $G$, the chain rule and
\eqref{eq:forms} give
\begin{equation}\label{eq:scalar}
 \ddc G=G'\alpha+G''\beta,
 \qquad
 \ddc(G\beta)=-G'\alpha\wedge\beta-G\alpha^2.
\end{equation}
Indeed $d^c(G\beta)=-G\alpha\wedge d^cr$, since
$d^cG\wedge\beta=0$. Taking $d$ proves the second formula with
both displayed signs. Expanding the penultimate and top powers gives
\begin{align*}
 \omega^m&=C^m\alpha^m+mC^{m-1}D\alpha^{m-1}\wedge\beta,\\
 \omega^n&=nC^mD\alpha^m\wedge\beta.
\end{align*}
Consequently
\[
 \ddc(\omega^m)=
 \bigl[(C^m)''-m(C^{m-1}D)'\bigr]\alpha^m\wedge\beta.
\]
The Gauduchon condition is equivalent to
\begin{equation}\label{eq:k}
 C^{m-1}(C'-D)=k
\end{equation}
for a real constant $k$. With $F=C^mD$ fixed, this is the equation
\begin{equation}\label{eq:ode}
 C^mC'=kC+F(r),\qquad D=\frac{F}{C^m}.
\end{equation}
Integration over a period yields
\begin{equation}\label{eq:integral}
 k\int_0^2C\,dr+\int_0^2F\,dr=0,
\end{equation}
so $k<0$. Equations \eqref{eq:lee} and \eqref{eq:k} also give
\begin{equation}\label{eq:L}
 l=kC^{-m},\qquad
 L(C)=-\int_0^2\frac{F(r)}{C(r)^n}\,dr.
\end{equation}

\begin{lemma}\label{lem:order}
For fixed $F$, positive periodic solutions of \eqref{eq:ode}
are unique for a fixed $k<0$. If $k_2>k_1$, their solutions satisfy
$C_2>C_1$ everywhere and $L(C_2)>L(C_1)$.
\end{lemma}
\begin{proof}
At any zero of $R=C_2-C_1$, the equation gives
$R'=(k_2-k_1)C_1^{1-m}>0$. Every zero would thus be a strict
upward crossing. A differentiable periodic function cannot have
only such crossings: their nonzero derivatives make the zeros
isolated, compactness makes their number finite, and a return around
the circle requires a downward crossing. Hence $R$ has constant
strict sign. Equation~\eqref{eq:integral} gives
$\int C_i=-\int F/k_i$ and fixes that sign as positive.
Equation~\eqref{eq:L} now gives the strict inequality of periods.

For equal $k$, initial-value uniqueness for the smooth equation
$C'=kC^{1-m}+FC^{-m}$ on $C>0$ identifies solutions which meet.
Solutions which never meet are strictly ordered, contradicting their
equal integrals in \eqref{eq:integral}. This proves uniqueness.
\end{proof}

\section{Existence and prescribed Lee period}
Fix $k<0$, put $c=-k$, and set $f_0=\min F>0$, $f_1=\max F$.
The equation $C'=C^{-m}(F-cC)$ points inward or tangentially at
both ends of the positive interval
\[
 I_k=[f_0/c,f_1/c].
\]
Its forward flow exists on this compact interval throughout one
period. The time-two map is a continuous self-map of $I_k$;
the intermediate value theorem applied to its difference from the
identity gives a fixed point. This includes the degenerate interval
when $f_0=f_1$. The associated positive solution is two-periodic,
and all derivatives agree at the endpoints by the smooth periodic
equation. Lemma~\ref{lem:order} makes this solution $C_k$ unique.

In particular,
\begin{equation}\label{eq:barriers}
 \frac{f_0}{-k}\le C_k(r)\le\frac{f_1}{-k}.
\end{equation}
The function $L(k)=-\int F/C_k^n$ is strictly increasing by
Lemma~\ref{lem:order}. It is continuous: on a compact neighborhood
of any $k_0<0$, the barriers are uniformly positive and finite;
the equation then bounds all derivatives uniformly. Compactness
gives subsequential limits as $k\to k_0$, and the equation and
uniqueness identify every limit as $C_{k_0}$. Thus $C_k\to C_{k_0}$
uniformly and the integral is continuous. The same barriers imply
\[
 \lim_{k\uparrow0}L(k)=0,
 \qquad \lim_{k\to-\infty}L(k)=-\infty.
\]
Every $L_0<0$ therefore selects exactly one $k$. With
$D=F/C_k^m$, equations \eqref{eq:ode}--\eqref{eq:L} verify every
volume, Lee and Gauduchon requirement in
Theorem~\ref{thm:main}. This is uniqueness among all positive
periodic solutions of the radial equation.

\section{Actual twisted potentials and gauge identification}
For this metric let $l=kC^{-m}<0$ and
$f(r)=\int_0^rl(s)\,ds$ on the real radial cover. Thus
$f(r+2)=f(r)+L_0$. The solution of
\begin{equation}\label{eq:U}
 U'-lU=C
\end{equation}
with
\[
 U(0)=\frac{e^{L_0}}{1-e^{L_0}}
       \int_0^2e^{-f(s)}C(s)\,ds,
 \qquad
 U(r)=e^{f(r)}\left[U(0)+\int_0^re^{-f(s)}C(s)\,ds\right]
\]
is strictly positive on $[0,2]$ and satisfies $U(2)=U(0)$.
Periodicity of the equation makes all derivatives match, so $U$
is a global smooth positive function on $H_n$. Directly, in the
task's exact twisted convention,
\begin{align*}
 D_\lambda U
 &= (U'-lU)\alpha+
    \bigl[U''-2lU'+(l^2-l')U\bigr]\beta\\
 &=C\alpha+(C'-lC)\beta=\omega.
\end{align*}
This verifies the actual zero twisted class without any assertion
about ordinary Bott--Chern exactness.

If $\lambda_2=\lambda_1+da$ has the same radial period,
$a$ is a smooth periodic function, with its additive constant fixed
by the chosen class identification. The exact covariance formula is
\[
 e^{-a}D_{\lambda_2}U_2=D_{\lambda_1}(e^{-a}U_2).
\]
Thus the two identified classes are indeed zero and the class
difference has the genuine potential $e^{-a}U_2-U_1$.
No addition of a constant to a twisted potential is used as a
normalization. For two radial metrics with the same volume and Lee
class, the preceding uniqueness proof already gives equal metrics.

\section{Non-Vaisman volumes and an explicit family}
The squared dual norm of $dr$ for \eqref{eq:radial} is $K/D$,
where $K>0$ is a fixed constant determined by our differential
normalization. Indeed the radial complex line is orthogonal to
$\ker dr\cap\ker d^cr$, and its metric is $D\beta$.
Equation~\eqref{eq:L} therefore gives
\[
 |\lambda|_\omega^2=Kk^2\frac{C^{-2m}}{D}.
\]
A Vaisman Lee form is parallel \cite[Definition 2.3]{OV24},
so its norm is constant. Since $k\ne0$, this would imply
$D=Q C^{-2m}$ for a constant $Q>0$. At both a maximum and a
minimum of $C$, equation~\eqref{eq:k} would then give
\[
 kC^{m+1}+Q=0.
\]
This has only one positive root. The maximum and minimum of $C$
would coincide, forcing $C,D,F$ constant. Every nonconstant $F$
thus gives a non-Vaisman metric, completing the theorem.

For an explicit family take
\[
 C=1+\varepsilon\cos(\pi r),\qquad
 D=C'+C^{1-m},\qquad k=-1,
\]
where
\[
 0<\varepsilon<\min\left\{\tfrac12,
                 \frac{(3/2)^{1-m}}{4\pi}\right\}.
\]
Then $D\ge(3/2)^{1-m}-\pi\varepsilon>
\tfrac34(3/2)^{1-m}>0$. Its exact Lee form and volume density are
\[
 \lambda=-C^{-m}dr,
 \qquad F=C^mC'+C>0.
\]
The Gauduchon identity holds with $k=-1$. Moreover
$F(0)=1+\varepsilon$, $F(1)=1-\varepsilon$ and
$\frac12\int_0^2F\,dr=1$. With
$dV=\frac12\alpha^m\wedge\beta$, a positive probability measure,
the exact volume is $\omega^n=2nF\,dV$.

Its volume is not invariant under the radial Lee translation of
the standard Vaisman metric $\alpha+\beta$, since $F$ is
nonconstant. This distinguishes the prescribed data from the
invariance hypotheses in \cite[Theorem 4.1]{OV24}. It does not
assert noninvariance under the new metric's own Lee field:
its radial volume flux is $lF/D=-1$, consistently with its
Gauduchon condition. The example is an admissible non-Vaisman
member of the radial uniqueness theorem, not an unequal pair
answering the unrestricted question negatively.

\begin{thebibliography}{9}
\bibitem{OV24} L. Ornea and M. Verbitsky,
\emph{A Calabi--Yau theorem for Vaisman manifolds},
Communications in Analysis and Geometry \textbf{32} (2024),
no. 10, 2889--2900. Primary version:
\href{https://arxiv.org/abs/2206.08808v2}{arXiv:2206.08808v2},
Definition 2.3 and Theorem 4.1 with its proof and footnote 5.
\bibitem{OVbook} L. Ornea and M. Verbitsky,
\emph{Principles of Locally Conformally K\"ahler Geometry},
\href{https://arxiv.org/abs/2208.07188v6}{arXiv:2208.07188v6},
Definition 18.34 and Question 47.56(3), pp. 263 and 683--684.
\end{thebibliography}
\end{document}


## Exact proposed targets

# Proposed P04 statement-only radial Hopf targets

These are proposed statements to prove, not imported theorems. No author
article, original proof, private calculation, prior report or proof strategy
is supplied. They concern a restricted family; original P04 remains open.

A. Fix n>=2, m=n-1, and H_n=(C^n minus {0})/<z maps to e z>.
Let q:H_n -> P^m be the projective map and normalize Fubini--Study kappa
by integral kappa^m=1. Use the original dd^c=i partial barpartial/(2pi).
The circle-valued function r=log norm(z)^2 modulo2 has a global differential.
The forms alpha=q^*kappa=dd^c r and beta=dr wedge d^c r descend and are
semipositive of complementary ranks m and1. The latter has fiber integral2.
For every pair of strictly positive smooth two-periodic functions C,D,
omega=C(r)alpha+D(r)beta is an actual smooth positive LCK metric, with
lambda=[(C'-D)/C]dr and period L=-integral_0^2 D/C<0. Two such radial Lee
forms are cohomologous precisely when their periods agree. Retain these
exact form, fiber, volume and Lee normalizations in all later assertions.

B. For EVERY strictly positive smooth two-periodic F and EVERY L0<0,
there exists exactly one metric in the ENTIRE radial family A which is
Gauduchon, has exact volume omega^n=nF(r)alpha^m wedge beta, and has
Lee period L0. This is metric existence and uniqueness, not just a
numerically selected solution, fixed-parameter family or same-potential
description. Reconstruct existence and compare all positive periodic
solutions. No equality of twisted classes is needed for this restricted
uniqueness. Nonexact Lee classes, nonconstant volumes and all n>=2 matter.

C. Every B metric has an actual global smooth STRICTLY POSITIVE function
U on H_n satisfying omega=D_lambda U, in the original normalized twisted
convention. Thus its actual twisted Bott--Chern class is zero. For two
such metrics with lambda2=lambda1+da, and ANY fixed additive constant in
the original gauge identification, verify
e^(-a)D_lambda2 U2=D_lambda1(e^(-a)U2), and exhibit the actual potential
of the identified class difference. No ordinary dd^c normalization or
addition of a constant to a twisted potential may replace this check.

D. If F is nonconstant, the B metric is NOT Vaisman. This must be shown
for every nonconstant F in this family, not only the example below.
The exact Vaisman definition needed is that the actual Lee form is
parallel for the metric. This definition supplies no other rigidity
theorem. Reconstruct the necessary metric norm calculation and conclusion.

E. For 0<epsilon<min(1/2,(3/2)^(1-m)/(4pi)), put
C=1+epsilon cos(pi r), D=C'+C^(1-m), and F=C^m C'+C.
These give an actual smooth positive Gauduchon LCK metric with
lambda=-C^(-m)dr, nonexact Lee form, positive NONCONSTANT F of period
average1, zero actual twisted class with a positive twisted potential,
and a non-Vaisman metric. For the smooth positive probability volume
dV=(1/2)alpha^m wedge beta, its exact volume is omega^n=2nF dV.
The density is noninvariant under the Lee translations of the STANDARD
Vaisman metric alpha+beta. Do not replace that specified field by the
new metric's own Lee field: its radial volume flux is constant.

F. For TWO actual radial candidates satisfying ALL original coupled
equations, strict positive volume, equal Lee class and fixed class
identification, the equality of metrics follows from B. There is no
unequal pair or unrestricted uniqueness theorem supplied by A--E.
The original P04 without a radial hypothesis remains unresolved by these
claims. The known Vaisman volume theorem requiring both Lee and anti-Lee
invariance is not a premise of their proof. No literature priority is
asserted. Assess whether the new restricted theorem is already known.

Permitted elementary foundations: smooth normalized Fubini--Study and
scalar Hopf geometry, the original definitions, exterior calculus,
positivity and smooth metric dual norms, elementary periodic real ODE
existence and uniqueness, and the intermediate value theorem. Prove
the applications and all needed formulas rather than treating the
conclusions as foundations. Independently assess the source definition
of Vaisman and identify every indispensable uncertain imported premise.


## Root source application and independent evidence

The complete primary Ornea--Verbitsky arXiv2206.08808v2 paper (518 extracted text lines) was read; actual printed pages4,6,7,8,9 were viewed. Definition2.3 on page4 supplies only parallel Lee form as the Vaisman definition. Theorem4.1 on page7 and its complete proof on pages8--9, including footnote5, explicitly require Lee and anti-Lee invariance for the prescribed volume. That theorem is background, not a proof premise of the new radial theorem. The book arXiv2208.07188v6 Definition18.34 on printed263 and Question47.56(3) on printed683--684 were read and their actual pages viewed. They identify the twisted convention and the unrestricted question. No unrestricted existence premise from the book, whose summary formulations omit the author theorem's invariance hypothesis, is used. All new radial proof steps are displayed in the article. No recursive certification of every citation in those primary sources is claimed. Obtain your own fresh primary evidence and assess every exact new application.

Every returned source passage must have a nonnegative valid premise index; do not append a minus-one sentinel for task-granted background. Every external premise needs accurate fresh primary evidence.


## Complete independent statement-only reconstruction

All seven ordinary notes retain their text, summaries, support and IDs unchanged. They are candidate proofs to assess, not trusted premises.

### n1

Summary: Target A proved with the exact normalizations: positive radial pairs define compact Hopf LCK metrics, beta has fiber integral 2, the volume is n C^m D alpha^m wedge beta, and Lee classes agree exactly when their negative periods agree. The radial Gauduchon first integral is also derived.

Detailed summary: For m=n-1, put t=dr and s=d^c r. Local coordinates give alpha=ds=q* kappa and beta=t wedge s, with complementary positive ranks. On a projective fiber s=dtheta/(2pi), giving integral beta=2 and integral alpha^m wedge beta=2. Exterior calculus gives lambda=((C'-D)/C)t, L=-integral D/C<0, and dd^c omega^m=m[C^(m-1)(C'-D)]' alpha^m wedge beta. Thus Gauduchon is equivalent to C^(m-1)(D-C')=k, necessarily k>0.

Support: []

This note proves A and the exterior-calculus reduction needed for B. All scalar functions below are smooth and 2-periodic. Every operator uses d^c=i(barpartial-partial)/(4pi).

The dilation z -> e z acts freely and properly discontinuously on C^n minus {0}. The map (r,xi) -> e^(r/2)xi, with xi in S^(2n-1), identifies its quotient smoothly with (R/2Z) times S^(2n-1). Thus H_n is a connected compact complex manifold of dimension n. The projective map q([z])=[z] is a holomorphic submersion. The function log|z|^2 changes by 2 under the generator, so r is circle-valued and t=dr, s=d^c r are global. Define alpha=ds and beta=t wedge s.

To check the Fubini--Study normalization, in a projective chart write z=w(1,zeta), w nonzero. Then r=log|w|^2+log(1+|zeta|^2), and dd^c log|w|^2=0. Therefore alpha=q* kappa for kappa=i partial barpartial log(1+|zeta|^2)/(2pi). The logarithmic Hessian has determinant (1+|zeta|^2)^(-m-1), so
kappa^m=(m!/pi^m)(1+|zeta|^2)^(-m-1) dLebesgue_(2m).
Its integral is 1: successively integrate each complex coordinate using integral_C (A+|w|^2)^(-p-1) dx dy=(pi/p)A^(-p), obtained by polar integration, for p=m,...,1. The missing projective hyperplane has measure zero for a smooth volume form. This verifies precisely the specified normalization.

The identity beta=i partial r wedge barpartial r/(2pi) shows that beta is semipositive of complex rank 1. Alpha has complex rank m and kernel the complex radial line. Let E be the real Euler field and T=E/2. Since d^c f=-df composed with J/(4pi), one has t(T)=1, s(T)=0 and s(JT)=1/(4pi). Hence beta is positive on the kernel of alpha. They have no common null vector. Consequently C alpha+D beta is smooth and strictly positive whenever C,D>0.

On q^(-1)([v]), choose a unit representative v and write z=w v with w=exp(r/2+i theta). This fiber has r modulo 2 and theta modulo 2pi. On it s=dtheta/(2pi), so integral_fiber beta=2. Let Omega=alpha^m wedge beta. Fiber integration gives integral_Hn Omega=2 integral_Pm kappa^m=2. Omega is strictly positive with the complex orientation; equivalently, (alpha+beta)^n=n Omega.

Because alpha^(m+1)=0 and beta^2=0, the exact volume is omega^n=n C^m D Omega. Also dt=0, ds=alpha, d alpha=0 and d beta=-t wedge alpha. Thus d omega=(C'-D)t wedge alpha, and
lambda=h(r)t, h=(C'-D)/C
is its closed Lee form. Its period on the radial loop is
L=integral_0^2 h dr=-integral_0^2 D/C dr<0,
since the integral of C'/C is zero. In particular lambda is nonexact.

Cohomologous radial Lee forms have equal periods on this loop. Conversely, if their periods agree, a(r)=a0+integral_0^r(h2-h1)(s)ds is a smooth 2-periodic function and lambda2-lambda1=da. Therefore equality of periods is precisely equality of their de Rham classes. The arbitrary a0 also describes the additive constant in the identification.

For the Gauduchon calculation, dd^c=-d^c d and (d^c)^2=0 give d^c t=-alpha, d^c s=0, d^c alpha=0 and d^c beta=-alpha wedge s. For a scalar h(r), dd^c h=h'alpha+h''beta. For a scalar v(r),
dd^c(v beta)=-v'alpha wedge beta-v alpha^2.
Expanding
omega^m=C^m alpha^m+m C^(m-1)D alpha^(m-1) wedge beta
therefore gives
 dd^c omega^m=[(C^m)''-m(C^(m-1)D)']Omega
 =m[C^(m-1)(C'-D)]'Omega.
Since Omega never vanishes, Gauduchon is equivalent to C^(m-1)(D-C')=k for a constant k. Then h=-k C^(-m) and L=-k integral_0^2 C^(-m)dr. The already proved L<0 forces k>0. These formulas apply also to m=1.

Artifacts: the complete proof is retained in notes.json and radial_proof.md in /workspace/research/native-workers/codex-o3nPvJ. Rerun the optional checks with 'python verify_radial.py'. The symbolic Gauduchon residual vanishes for m=1,...,6 in check_output.json. Those are finite algebra checks; the argument above proves the formula for every m>=1. No Vaisman or Monge--Ampere theorem is imported.

Artifacts: /workspace/research/native-workers/codex-o3nPvJ

### n2

Summary: Target B proved for every n>=2, positive smooth 2-periodic F and L0<0 in the entire radial family. For each k>0 the periodic solution is unique; C decreases strictly with k, while its Lee-period magnitude continuously ranges from 0 to infinity. Twisted-class equality is unnecessary.

Detailed summary: Set y=C^(m+1)/(m+1). Its equation y'=F-k((m+1)y)^(1/(m+1)) has a positive invariant interval corresponding to Fmin/k<=C<=Fmax/k. The continuous period map has a fixed point. Ordered distinct periodic solutions would have strictly decreasing difference, which is impossible. A maximum comparison proves C_k2<C_k1 for k2>k1. Continuous dependence is reconstructed on a compact positive interval. H(k)=k integral C_k^(-m) obeys 2k^(m+1)/Fmax^m<=H(k)<=2k^(m+1)/Fmin^m, so exactly one k has H(k)=-L0. Reconstructing D=F/C^m compares every radial candidate.

Support: ["n1"]

This is a complete mathematical proof of B, using n1. Fix m=n-1>=1, a smooth positive 2-periodic F and L0<0. Write p=min F>0 and q=max F.

Every positive radial Gauduchon metric of the prescribed exact volume satisfies, for some k>0,
D=C'+k C^(1-m), C^m D=F,
hence C^m C'=F-kC. Conversely, any positive periodic solution C of this last equation gives the required positive Gauduchon metric upon setting D=F/C^m.

First fix any k>0. Define y=C^(m+1)/(m+1) and c(y)=((m+1)y)^(1/(m+1)). The equation is
 y'=F(r)-k c(y).
Its right side is smooth on y>0 and strictly decreasing in y. Put ell=(p/k)^(m+1)/(m+1) and u=(q/k)^(m+1)/(m+1). The compact positive interval I=[ell,u] is forward invariant. At ell the vector field is F-p>=0, and below ell it is strictly positive. A solution cannot cross below ell, because on an interval below ell it would be increasing, contradicting entry from ell. At u and above it the reversed argument applies. Elementary ODE existence and uniqueness therefore extend every solution starting in I through time 2.

The continuous period map P_k(y0)=y(2;y0,k) maps I to itself. Hence P_k(ell)-ell>=0 and P_k(u)-u<=0. The intermediate value theorem supplies a fixed point. If ell=u, that single value is already a constant solution. Periodicity of F and ODE uniqueness identify the solution shifted by 2 with itself. It is smooth and strictly positive.

This solution is unique among all positive periodic solutions. Indeed, any positive periodic C has extrema, and at each extremum C'=0 implies C=F/k. Thus p/k<=C<=q/k. Alternatively, two solutions of the y equation either agree everywhere or never cross, by uniqueness. Order two distinct periodic solutions as y1>y2. Their difference satisfies
 (y1-y2)'=-k(c(y1)-c(y2))<0
at every point, contradicting periodicity after integration over a period. Denote the unique solution by C_k; it satisfies p/k<=C_k(r)<=q/k.

Now let k2>k1>0 and take the periodic difference delta=y_k2-y_k1. If its maximum were nonnegative, at a point r0 of maximum one would have C_k2>=C_k1>0, but
 delta'(r0)=-k2 C_k2(r0)+k1 C_k1(r0)<0.
This contradicts delta'(r0)=0. Therefore C_k2(r)<C_k1(r) for every r.

Here are details justifying the needed continuous dependence. Fix k*>0 and restrict nearby k to [k*/2,2k*]. The bounds place all C_k in the common compact positive interval [p/(2k*),2q/k*], and the y values likewise remain away from zero. On a slightly larger compact positive interval the right side has a common Lipschitz bound K in y and a bound M for c(y). For k_j tending to k*, take a convergent subsequence of the bounded initial values y_kj(0), with limit y0. Compare with the solution at k* starting at y0. Integrating the Lipschitz inequality gives, on 0<=r<=2,
 |y_j(r)-y_*(r)| <= (|y_j(0)-y0|+2M|k_j-k*|) exp(2K).
The estimate follows by the elementary integrating-factor argument for the corresponding integral inequality. Local comparison and continuation keep the limit in the compact positive interval and extend it through the full period. Uniform convergence passes periodic endpoint equality to the limit. Uniqueness at k* identifies the limit with y_k*. Every convergent subsequence has this same limit, proving uniform continuity of k -> C_k on a period. The same estimate establishes continuity of the period map used above.

Define H(k)=k integral_0^2 C_k(r)^(-m)dr. It is continuous. It is strictly increasing, since k2>k1 and C_k2<C_k1 give k2 C_k2^(-m)>k1 C_k1^(-m) pointwise. The bounds on C_k yield
 2 k^(m+1)/q^m <= H(k) <= 2 k^(m+1)/p^m.
Thus H tends to zero as k tends to zero from above and tends to infinity as k tends to infinity. The intermediate value theorem and strict monotonicity give exactly one k>0 with H(k)=-L0.

For this k, set C=C_k and D=F/C_k^m=C_k'+k C_k^(1-m). These functions are smooth, positive and periodic. Note n1 proves the exact volume nF Omega, the Gauduchon equation, and the Lee period -H(k)=L0. Any other radial candidate with these data has some k'>0, must have C=C_k' by fixed-parameter uniqueness, and must satisfy H(k')=-L0. Therefore k'=k and both C and D coincide. This compares the entire family A without assuming equality of twisted classes.

Optional evidence: 'python verify_radial.py' uses F=1+0.2 cos(pi r)+0.1 sin(2pi r), conservative bounds 0.7<=F<=1.3, m=1,2,4 and k=0.5,1,2. For m=1 the computed Lee periods were approximately -0.5000661642, -2.0037958512 and -8.1095093168, with periodic y residuals at most 2.7e-15. For m=4 the periods were approximately -0.0625013085, -2.0358692028 and -82.9222743222. All sampled successive differences of C were negative. Programs, inputs and outputs are verify_radial.py, check_input.json and check_output.json; versions are in environment.json. These are finite floating-point observations, not an exhaustive or certified numerical result. They do not replace the all-parameter proof.

Artifacts: /workspace/research/native-workers/codex-o3nPvJ

### n3

Summary: Target C proved with an explicit global strictly positive twisted potential in the original normalization. The gauge identity holds for every fixed additive constant, and u=e^(-a)U2-U1 witnesses the actual identified class difference. Constants in twisted potentials are not normalized away.

Detailed summary: For a B metric let b=k C^(-m)>0 and B=integral_0^2 b=-L0. The positive periodic function U=(1-e^(-B))^(-1) integral_(r-2)^r exp(-integral_s^r b)C(s)ds satisfies U'+bU=C. The exact radial twisted coefficients give D_lambda U=C alpha+(C'+bC)beta=omega. Multiplication by e^(-a) intertwines both twisted first-order operators for lambda2=lambda1+da and hence their composition. Consequently e^(-a)omega2-omega1=D_lambda1(e^(-a)U2-U1) for any prescribed gauge constant.

Support: ["n1", "n2"]

This proves C using the actual metrics constructed in n1-n2.

For a B metric put lambda=-b(r)dr, where b=k C^(-m)>0, and B=integral_0^2 b=-L0>0. Define
 U(r)=(1-exp(-B))^(-1) integral_(r-2)^r exp(-integral_s^r b(t)dt) C(s)ds.
The denominator and integrand are strictly positive. The function is smooth and 2-periodic, since b and C are periodic. It therefore defines an actual global smooth strictly positive function on H_n.

If V is the numerator, differentiation of its endpoints and kernel gives
 V'=C(r)-exp(-B)C(r-2)-b(r)V
    =(1-exp(-B))C-bV.
Thus U'+bU=C.

To verify the original twisted normalization, for lambda=h(r)dr choose a local primitive f with f'=h. For a radial function W, the local exponential formula and n1 give
 D_lambda W=(W'-hW)alpha+[W''-2hW'+(h^2-h')W]beta
           =(W'-hW)alpha+[(W'-hW)'-h(W'-hW)]beta.
With h=-b and W=U, the alpha coefficient is C and the beta coefficient is C'+bC=C'+k C^(1-m)=D. Therefore D_lambda U=omega in precisely the specified convention. Closedness of lambda gives d_lambda^2=0, also directly by local exponential conjugation, so these are legitimate d_lambda-closed images. The actual twisted Bott--Chern class is zero.

Now let lambda2=lambda1+da and G(v)=exp(-a)v. The product rule and (da)^c=d^c a give, on every smooth form v,
 d_lambda1(Gv)=G d_lambda2 v,
 d_lambda1^c(Gv)=G d_lambda2^c v.
Composing these identities proves
 D_lambda1(Gv)=G D_lambda2 v.
This is a full operator identity; no radial assumption on a or v is needed. Replacing a by a+c multiplies G by exp(-c) and preserves every equality with that same fixed c.

For two B metrics with cohomologous Lee forms, choose a with its prescribed additive constant. Their positive potentials give the actual smooth real function
 u=exp(-a)U2-U1.
Then
 exp(-a)omega2-omega1=D_lambda1 u,
 A=omega1+D_lambda1 u=exp(-a)omega2>0,
 omega2=exp(a)A.
This verifies the actual identified class difference for every allowed gauge constant.

No constant has been removed from a twisted potential. Indeed the coefficient formula gives D_lambda 1=b alpha+(b'+b^2)beta, whose alpha coefficient is strictly positive here. Thus D_lambda 1 is not zero. The claim is existence of a positive potential and the actual identification; it does not assert uniqueness of arbitrary scalar potentials or triviality of the kernel.

Artifacts: rerun 'python verify_radial.py'. In check_output.json the symbolic local exponential coefficient check and both radial gauge coefficients have zero residual. The full product-rule proof above establishes the identity for arbitrary smooth a; finite symbolic checks merely corroborate it. Full proof and commands are retained in radial_proof.md and RUN.md.

Artifacts: /workspace/research/native-workers/codex-o3nPvJ

### n4

Summary: Target D proved for every nonconstant F: |lambda|^2=4pi k^2/(F C^m). Parallelism forces constant norm, which forces C and F constant by evaluating the Gauduchon volume equation at extrema. Public primary sources confirm the definition using the actual parallel Lee form.

Detailed summary: For T=one-half the real Euler field, dr(T)=1, d^c r(JT)=1/(4pi), and alpha annihilates T and JT. With g(V,W)=omega(V,JW), g(T,T)=D/(4pi) and |dr|^2=4pi/D. Therefore the actual Lee norm has the stated formula. Constant norm gives F C^m=K>0 and K=C^(2m)C'+k C^(m+1); maxima and minima force C constant. Constant coefficients conversely give a product metric with parallel dr, verifying the standard alpha+beta metric used in E without a rigidity theorem.

Support: ["n1", "n2"]

This proves D from the metric-specific definition: the actual Lee form must be parallel for the Levi--Civita connection of the actual metric.

The definition is confirmed in the public primary sources Ornea--Verbitsky, A Calabi-Yau theorem for Vaisman manifolds, arXiv:2206.08808v2, Definition 2.3, https://arxiv.org/html/2206.08808v2, and Parton, Hopf surfaces: a family of locally conformal Kahler metrics and elliptic fibrations, Definition 2.1, https://arxiv.org/html/math/9907105v1. No other theorem or d^c convention from these sources is used.

Let T=E/2. By n1,
 dr(T)=1, dr(JT)=0, s(T)=0, s(JT)=1/(4pi).
Alpha annihilates T and JT. The space H=ker dr intersect ker s is J-invariant because dr composed with J=-4pi s and s composed with J=dr/(4pi). It complements span(T,JT).

For g(V,W)=omega(V,JW), T is orthogonal to H and to JT, and
 g(T,T)=omega(T,JT)=D/(4pi).
Thus the dual of dr is (4pi/D)T and |dr|^2=4pi/D. Since lambda=-k C^(-m)dr and F=C^m D,
 |lambda|^2=4pi k^2 C^(-2m)/D=4pi k^2/(F C^m).
All normalization factors have therefore been retained.

If lambda is parallel, metric compatibility gives V(|lambda|^2)=2<nabla_V lambda,lambda>=0 for every vector V. Its positive norm is constant on the connected manifold, so F C^m=K>0. Combining this with F=C^m C'+kC gives
 K=C^(2m)C'+k C^(m+1).
At the maximum and minimum of periodic C, its derivative vanishes. Hence K=k(max C)^(m+1)=k(min C)^(m+1). Since k>0, C is constant and then F=kC is constant. The contrapositive proves D for every nonconstant F.

The standard metric in E can also be checked directly. Constant F gives constant C=F/k by n2, and constant D=k C^(1-m). In the product coordinates of n1, s and alpha are independent of r. The metric is g=(D/(4pi))dr tensor dr+g_S, with no radial mixed terms and g_S independent of r. The Christoffel symbols with upper radial index vanish: its coefficient is constant, its mixed coefficients vanish, and sphere coefficients have zero r derivative. Therefore dr, and the constant multiple lambda, are parallel. In particular omega0=alpha+beta is an actual Vaisman metric with lambda0=-dr.

Evidence: verify_radial.py independently constructs the real-coordinate forms at z=(1,0) in C^2. SymPy obtains g=diag(D/pi,D/pi,C/pi,C/pi) and |dr|^2=4pi/D exactly in check_output.json. Rerun 'python verify_radial.py'. The general frame argument proves the formula for all n>=2; the coordinate calculation is additional finite evidence. No indispensable uncertain imported geometric premise occurs.

Artifacts: /workspace/research/native-workers/codex-o3nPvJ

### n5

Summary: Target E proved for every permitted epsilon and n>=2: positive non-Vaisman Gauduchon LCK cosine metrics, nonexact Lee form, positive actual twisted potential, zero twisted class, positive nonconstant F of average 1, and omega^n=2nF dV. The density fails invariance under the standard Vaisman Lee field, although the new metric's own radial volume flux is constant.

Detailed summary: With c0=(3/2)^(1-m), the bounds give 1/2<C<3/2, C^(1-m)>=c0 and |C'|<c0/4, hence D>3c0/4. The Gauduchon first integral is k=1. F=C^m C'+C is positive, takes values 1+epsilon and 1-epsilon at r=0 and 1, and has integral 2. The standard Lee field is X0=-4pi T, so Lie_X0(F dV)=-4pi F' dV is nonzero. The new Lee field is X=-4pi/F T; its radial flux F times the coefficient is constant, giving Lie_X omega^n=0.

Support: ["n1", "n2", "n3", "n4"]

Let m=n-1>=1 and 0<epsilon<min(1/2,(3/2)^(1-m)/(4pi)). Define
 C=1+epsilon cos(pi r),
 D=C'+C^(1-m),
 F=C^m C'+C.
These are actual smooth 2-periodic functions. Put c0=(3/2)^(1-m)>0. The epsilon bounds give 1/2<C<3/2, C^(1-m)>=c0 and |C'|<=pi epsilon<c0/4. Therefore D>3c0/4>0. By n1, omega=C alpha+D beta is a strictly positive smooth LCK metric. Also F=C^m D>0, so its density never degenerates.

Since C^(m-1)(D-C')=1, n1 proves Gauduchon. Its actual closed Lee form is lambda=-C^(-m)dr, with negative period L=-integral_0^2 C^(-m)dr, so it is nonexact. Its exact volume is nF Omega. It is consequently the B metric for this F,L, with k=1.

The integral of C^m C' over a period is zero, being the integral of the derivative of C^(m+1)/(m+1). The integral of C is 2. Thus F has period average 1. Since C' vanishes at 0 and 1, F(0)=1+epsilon and F(1)=1-epsilon. Therefore F is nonconstant for every allowed epsilon. Note n4 proves that the actual Lee form is not parallel and omega is not Vaisman.

Use the positive potential formula in n3 with b=C^(-m) and B=integral_0^2 C^(-m). It provides a global smooth U>0 with D_lambda U=omega in the original normalized convention. The actual twisted Bott--Chern class is zero.

By n1, dV=Omega/2 is a smooth strictly positive probability volume. The exact formula is therefore omega^n=2nF dV, with density exactly 2nF relative to the specified dV.

It remains to check the specified invariance statement. For the standard metric omega0=alpha+beta, n4 proves Vaisman and gives lambda0=-dr and its metric dual X0=-4pi T. The flows of T are positive scalar dilations and those of JT are scalar rotations. They are holomorphic and change r by a constant or leave it fixed. Therefore alpha, beta, Omega and dV are invariant under both T and JT. Hence
 Lie_X0(F dV)=-4pi F' dV,
 Lie_X0(omega^n)=-8pi n F' dV.
Because F is nonconstant, these derivatives do not vanish identically. The density is not invariant under the Lee translations of the standard Vaisman metric. Its standard anti-Lee field JX0=-4pi JT does preserve the volume, since F depends only on r. Thus simultaneous invariance fails.

For comparison, the new metric's actual Lee field is
 X=-4pi C^(-m)/D T=-4pi/F T.
Set eta=i_T Omega=alpha^m wedge s. Then Omega=dr wedge eta, eta is independent of r and d eta=alpha^(m+1)=0. Cartan's formula gives, for a radial coefficient v(r),
 Lie_(vT)(nF Omega)=n(vF)'Omega.
For X the product vF=-4pi is constant, so Lie_X omega^n=0. This explains exactly why substituting the new Lee field would not check E's assertion.

Optional evidence: 'python verify_radial.py' with m=1 and epsilon=1/(8pi) reports sampled min D=0.875, sampled min F about 0.8701921308, numerical average F=0.9999999999999999, Lee period about -2.0015850257, sampled min U about 0.9752335412, and periodic U residual about 6.7e-16. The sampled squared Lee norm ranges approximately from 10.89608507 to 14.66974584. Additional m=2,4 observations are in check_output.json. These are finite floating-point observations, not certified minima. The inequalities, integrals, field calculations and previous proofs establish E for every allowed parameter.

Artifacts: /workspace/research/native-workers/codex-o3nPvJ

### n6

Summary: Public-source assessment confirms the actual parallel-Lee definition and identifies related older Hopf families and cohomogeneity-one Gauduchon first integrals. No exact match to B was identified in the examined material; priority remains unestablished. No uncertain imported geometric theorem is indispensable to A--F.

Detailed summary: Checked Ornea--Verbitsky arXiv:2206.08808v2 Definition 2.3 and Theorem 4.1, Parton math/9907105v1 Definition 2.1 and Section 3.2, the Gauduchon--Ornea 1998 article's public bibliographic abstract, and Angella--Pediconi's cohomogeneity-one paper including Proposition 4.6. None supplies a premise for the reconstructed radial proofs. The Vaisman volume theorem has restricted metric and invariance hypotheses. Related prior results prevent a blanket novelty claim. A finite search cannot establish absence of a prior exact B theorem. The supplied book question and pagination were not independently verified.

Support: ["n1", "n2", "n3", "n4", "n5"]

This is an observational bibliographic assessment, not a proof of priority.

Ornea--Verbitsky, A Calabi-Yau theorem for Vaisman manifolds, arXiv:2206.08808v2, Definition 2.3, and Parton, Hopf surfaces: a family of locally conformal Kahler metrics and elliptic fibrations, arXiv:math/9907105v1, Definition 2.1, both use parallelism of the actual Lee form for the metric's Levi--Civita connection. The primary URLs are https://arxiv.org/html/2206.08808v2 and https://arxiv.org/html/math/9907105v1. This confirms the supplied definition. No classification or flow-rigidity theorem is inferred from that definition; n4 uses explicit metric calculations.

Theorem 4.1 in the first source assumes a compact Vaisman background, a volume invariant under its Lee and anti-Lee fields, and a total-volume condition. Its conclusion concerns Vaisman metrics. It is not used in n1-n5 and is not independently reproved because none of its conclusions is imported. Its scope does not directly cover E's nonconstant radial densities. Differences in how scaling is presented in the source abstract and theorem are likewise not used.

Related work already exists. Parton's Section 3.2 constructs circle-function deformations on scalar Hopf surfaces, with constant transverse coefficient and variable radial coefficient, and discusses parallelism of their Lee forms. These are related prior families, not an imported proof of B. They are conformally related to the surface radial setting and should be considered in any thorough priority analysis. The public bibliographic/abstract page for Gauduchon--Ornea, Locally conformally Kahler metrics on Hopf surfaces (1998), was also inspected: https://aif.centre-mersenne.org/articles/10.5802/aif.1651/.

Angella--Pediconi, On cohomogeneity one Hermitian non-Kahler metrics, studies related invariant LCK, Vaisman and Gauduchon conditions. Proposition 4.6 gives a Gauduchon first integral in its coordinates. The primary article is https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/on-cohomogeneity-one-hermitian-nonkahler-metrics/22A9EFC5FB5B5213B7123018F40E354E. No coordinate identification or theorem from it is assumed here.

Searches combined Hopf, radial, Gauduchon, prescribed volume, Lee and cohomogeneity one. In the inspected material I did not identify a prior statement matching B for every dimension n>=2, every smooth strictly positive periodic F and every negative Lee period, with existence and uniqueness in the entire specified family. This is a limited search observation. It does not establish novelty; the exact prior status of B remains unestablished. Related families and first-integral methods are already known, so no broad priority claim is justified.

Premise audit: n1-n5 reconstruct the form normalizations, exterior identities, periodic ODE applications, positive twisted potential, gauge operators and metric norm using the elementary foundations permitted in the input. No uncertain imported geometric theorem is indispensable. In particular no general Gauduchon conformal existence theorem, Hermitian Monge--Ampere uniqueness theorem, positive-potential theorem, Vaisman classification or prescribed-volume theorem is used. The book question, version and pagination are supplied problem data; they were not independently verified by reading the book.

Reproducibility: source_audit.json records the primary URLs, checked sections and search queries. web_evidence.json and web_evidence_additional.json preserve retrieval excerpts. Repeat these public requests in a browser to rerun the limited assessment. 'python verify_radial.py' regenerates check_output.json and environment.json from check_input.json. The environment is Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and SymPy 1.14.0 on Linux x86_64. All computations were small serial local checks; no resource-heavy computation or supervised service was required. No author article or original proof of the proposed new radial theorem, private notes, other campaign files or credentials were read.

Failures and limitations: no mathematical failure or false target was found within A--F. A patch-tool attempt to replace a web artifact with a simultaneous delete/add was rejected; it was resolved by storing the additional retrieval separately. This affected no proof. Numerical observations are finite and noncertified, and symbolic checks cover only specified identities. Bibliographic priority and unrestricted P04 remain unresolved.

Artifacts: /workspace/research/native-workers/codex-o3nPvJ

### n7

Summary: Target F and the complete restricted A--F assignment are proved as unverified drafts: two radial candidates satisfying the original coupled equations have equal metrics by B, and C verifies the actual fixed twisted identification. candidate=true applies only to the restricted theorem; unrestricted original P04 closure=false.

Detailed summary: For radial candidates, omega2=e^a A and A^n=e^(-na)omega1^n give the same strictly positive volume nF Omega. The second coupled equation is exactly Gauduchon for omega2. Closed lambda and d_lambda A=0 give its actual Lee form lambda+da; equal Lee classes give equal negative radial periods. Thus n2 forces equality of C and D and hence of metrics. Note n3 provides the actual potential e^(-a)U2-U1 for every fixed gauge constant. Scalar representatives can differ through conformal compensation and the twisted kernel. All restricted targets are covered; no unrestricted uniqueness proof or unequal compact pair is supplied, and priority remains unestablished.

Support: ["n1", "n2", "n3", "n4", "n5", "n6"]

This note proves F and claims completion of the EXACT RESTRICTED A--F assignment. These are ordinary unverified proof drafts. Explicitly, unrestricted original P04 closure=false.

Suppose both omega1 and omega2 are actual radial metrics on the specified H_n and satisfy all original hypotheses, including
 A=omega1+D_lambda u>0,
 omega2=exp(a)A,
 A^n=exp(-na)omega1^n,
 dd^c(exp((n-1)a)A^(n-1))=0.
Omega1 is Gauduchon, lambda is its actual closed Lee form, and the additive constant in a is fixed by the original identification.

First verify the properties used in B. For closed lambda, the local exponential formula gives d_lambda D_lambda u=0, since locally it is exp(f)d dd^c(exp(-f)u)=0. Also d_lambda omega1=0. Hence dA=lambda wedge A and d omega2=(lambda+da) wedge omega2.

The Lee form is unique for a positive (1,1) form when n>=2. Indeed, tau wedge omega=0 implies tau wedge omega^(n-1)=0. In a symplectic coframe omega=sum_j e_j wedge f_j, the coefficients of tau produce independent complementary (2n-1)-forms in this latter product. Thus this map is injective and tau=0. Consequently the radial Lee forms computed in n1 are the actual forms in the coupled system.

The first volume equation yields exactly omega2^n=exp(na)A^n=omega1^n. Write omega1=C1 alpha+D1 beta and F=C1^m D1>0. The common volume is nF Omega, with F smooth and 2-periodic. Radiality of omega2 gives C2^m D2=F. The second coupled equation is precisely dd^c omega2^m=0, so both metrics are Gauduchon. Their equal Lee classes give equal negative periods L0 by n1. The complete-family theorem B, proved in n2, now forces C1=C2 and D1=D2. Therefore
 omega2=omega1,
 equivalently exp(a)(omega1+D_lambda u)=omega1.
No radial assumption on u was required.

The actual twisted identification has also been verified, rather than changed. Note n3 supplies, for any fixed additive constant in a,
 u_can=exp(-a)U2-U1,
 D_lambda u_can=exp(-a)omega2-omega1.
The originally supplied u can differ from this witness by a member of ker D_lambda. Metric uniqueness does not require scalar uniqueness.

For example, even after metric equality, any fixed constant c can be represented by a=c, u=(exp(-c)-1)U1 and A=exp(-c)omega1. Both coupled equations hold and omega2=omega1. This is exact conformal compensation, not an unequal-metric counterexample. Nor can one freely add constants to u, because D_lambda 1 is generally nonzero, as n3 explicitly computes.

Coverage is complete for the restricted assignment: n1 proves A and derives the Gauduchon equation with all normalization factors; n2 proves B for every allowed F, L0 and n, comparing all periodic solutions; n3 proves C with a strictly positive actual twisted potential and every fixed gauge constant; n4 proves D for every nonconstant F using the actual metric norm; n5 proves E, including the standard-field invariance distinction; this note proves F's equality assertion. Note n6 independently checks the source definition and assesses the public literature. Related prior results are identified, while the exact priority of B remains unestablished. No priority is asserted.

The scope limitation is essential. Nothing here proves that arbitrary Gauduchon LCK metrics are radial or reduces the unrestricted coupled problem to this ODE. Example E is a non-Vaisman metric with a noninvariant positive volume, not an unequal pair with all original class data. No Vaisman prescribed-volume theorem is a premise. These notes provide neither an unrestricted uniqueness theorem nor an unrestricted counterexample. Therefore unrestricted original P04 closure=false.

Artifacts are in /workspace/research/native-workers/codex-o3nPvJ: notes.json and radial_proof.md contain the full drafts; verify_radial.py and check_input.json retain the optional calculations, with check_output.json and environment.json; source_audit.json and the web evidence files retain the public-source audit. Rerun 'python verify_radial.py' and 'python validate_notes.py'. Packaging validation completed for all seven notes, confirmed that all local support references precede their uses, and recorded restricted candidate scope and unrestricted closure=false in validation_output.json. RUN.md gives the commands, and manifest.json records artifact hashes. Execution and schema-validation success establish reproducibility only, not mathematical correctness. The candidate flag is true solely for the complete restricted A--F theorem claimed here.

Artifacts: /workspace/research/native-workers/codex-o3nPvJ


## Entire current scope-qualified article

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\PP}{\mathbb P}
\newcommand{\D}{D_\lambda}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Prescribed radial volumes for Gauduchon LCK metrics\newline
on scalar Hopf manifolds}
\author{}
\date{}
\begin{document}
\maketitle
\noindent\textbf{Working draft.} Independent mathematical review,
reconstruction and final comparison are pending. The unrestricted
Gauduchon LCK uniqueness problem is not resolved by this article.
\begin{abstract}
On each scalar Hopf manifold $H_n$ defined below, $n\geq2$,
a strictly positive smooth radial volume and a negative Lee period
determine exactly one radial Gauduchon locally conformally K\"ahler
metric. A periodic scalar equation gives existence, while a strict
ordering of its solutions gives uniqueness. Every resulting metric has
an explicit positive twisted potential and zero twisted Bott--Chern
class in the actual Lee gauge. A nonconstant radial volume always
produces a non-Vaisman metric. The conclusion concerns the stated
radial family and does not assert uniqueness among all LCK metrics.
\end{abstract}

\section{Forms, class data and statement}
Use $d^c=\frac{i}{4\pi}(\bar\partial-\partial)$ and
$\ddc=\frac{i}{2\pi}\partial\bar\partial$. Put $m=n-1$, where
$n\ge2$, and set
\[
 H_n=(\mathbb C^n\setminus\{0\})/\langle z\mapsto ez\rangle,
 \qquad q:H_n\longrightarrow\PP^m.
\]
Let $\kappa$ be the Fubini--Study form with $\int_{\PP^m}\kappa^m=1$.
The circle-valued function $r=\log\|z\|^2\pmod2$ has a global
differential, and
\[
 \alpha=q^*\kappa=\ddc r,
 \qquad \beta=dr\wedge d^cr.
\]
Here $\alpha$ is closed, semipositive and of rank $m$; $\beta$ is
semipositive of rank one and positive in the complex radial direction.
Their kernels are complementary. Direct differentiation gives
\begin{equation}\label{eq:forms}
 \alpha^n=\beta^2=0,\qquad
 d\beta=-dr\wedge\alpha,\qquad
 d^c\beta=-\alpha\wedge d^cr,\qquad
 \ddc\beta=-\alpha^2.
\end{equation}
On a fiber, $d^cr=d\arg z/(2\pi)$ and $r$ has period two;
therefore $\int_{q^{-1}(x)}\beta=2$ and
$\int_{H_n}\alpha^m\wedge\beta=2$.

Consider precisely the metrics
\begin{equation}\label{eq:radial}
 \omega=C(r)\alpha+D(r)\beta,
 \qquad C,D\in C^\infty(\mathbb R/2\mathbb Z),\quad C,D>0.
\end{equation}
Every such form is LCK, with actual closed Lee form
\begin{equation}\label{eq:lee}
 \lambda=l(r)\,dr,\qquad l=\frac{C'-D}{C},
 \qquad d\omega=\lambda\wedge\omega.
\end{equation}
The Lee form is unique since wedging one-forms with a positive
$(1,1)$ form is injective in complex dimension at least two.
Its period is
\begin{equation}\label{eq:period}
 L=\int_0^2l(r)\,dr=-\int_0^2\frac{D(r)}{C(r)}\,dr<0.
\end{equation}
Thus the Lee form is nonexact. Two radial Lee forms have the same
de Rham class exactly when their periods agree: their difference is
the differential of a smooth periodic function in that case, and the
radial circle detects the period in the converse direction.

For a closed real one-form $\lambda$, use
$d_\lambda=d-\lambda\wedge$,
$d_\lambda^c=d^c-\lambda^c\wedge$ and
$D_\lambda=d_\lambda d_\lambda^c$, where
$\lambda^c=\frac{i}{4\pi}(\lambda^{0,1}-\lambda^{1,0})$.
Locally, $\lambda=df$ gives
$D_\lambda u=e^f\ddc(e^{-f}u)$.
The real twisted Bott--Chern group is the space of smooth real
$d_\lambda$-closed $(1,1)$ forms modulo the image of $D_\lambda$
on smooth real functions. This is the normalized convention for the
weighted group of \cite[Definition 18.34]{OVbook}.

\begin{theorem}\label{thm:main}
For every positive smooth two-periodic function $F$ and every
$L_0<0$, there is exactly one metric of the form \eqref{eq:radial}
which is Gauduchon, has volume
\[
 \omega^n=nF(r)\alpha^m\wedge\beta,
\]
and has Lee period $L_0$. Its actual Lee form admits a positive
smooth global function $U$ such that $\omega=D_\lambda U$.
In particular its twisted Bott--Chern class is zero. If $F$ is
nonconstant, the resulting metric is not Vaisman.
\end{theorem}

Theorem~\ref{thm:main} proves uniqueness within the entire stated
radial family without assuming equality of twisted classes.
It consequently applies to radial candidates satisfying the fixed
class identification of \cite[Question 47.56(3)]{OVbook}.
That question has no radial assumption and remains unanswered here.
The known Vaisman prescribed-volume theorem assumes invariance
under the Lee and anti-Lee fields \cite[Theorem 4.1]{OV24}; the
present scalar argument does not invoke that theorem.

\section{The exact periodic equation}
For any smooth two-periodic scalar $G$, the chain rule and
\eqref{eq:forms} give
\begin{equation}\label{eq:scalar}
 \ddc G=G'\alpha+G''\beta,
 \qquad
 \ddc(G\beta)=-G'\alpha\wedge\beta-G\alpha^2.
\end{equation}
Indeed $d^c(G\beta)=-G\alpha\wedge d^cr$, since
$d^cG\wedge\beta=0$. Taking $d$ proves the second formula with
both displayed signs. Expanding the penultimate and top powers gives
\begin{align*}
 \omega^m&=C^m\alpha^m+mC^{m-1}D\alpha^{m-1}\wedge\beta,\\
 \omega^n&=nC^mD\alpha^m\wedge\beta.
\end{align*}
Consequently
\[
 \ddc(\omega^m)=
 \bigl[(C^m)''-m(C^{m-1}D)'\bigr]\alpha^m\wedge\beta.
\]
The Gauduchon condition is equivalent to
\begin{equation}\label{eq:k}
 C^{m-1}(C'-D)=k
\end{equation}
for a real constant $k$. With $F=C^mD$ fixed, this is the equation
\begin{equation}\label{eq:ode}
 C^mC'=kC+F(r),\qquad D=\frac{F}{C^m}.
\end{equation}
Integration over a period yields
\begin{equation}\label{eq:integral}
 k\int_0^2C\,dr+\int_0^2F\,dr=0,
\end{equation}
so $k<0$. Equations \eqref{eq:lee} and \eqref{eq:k} also give
\begin{equation}\label{eq:L}
 l=kC^{-m},\qquad
 L(C)=-\int_0^2\frac{F(r)}{C(r)^n}\,dr.
\end{equation}

\begin{lemma}\label{lem:order}
For fixed $F$, positive periodic solutions of \eqref{eq:ode}
are unique for a fixed $k<0$. If $k_2>k_1$, their solutions satisfy
$C_2>C_1$ everywhere and $L(C_2)>L(C_1)$.
\end{lemma}
\begin{proof}
At any zero of $R=C_2-C_1$, the equation gives
$R'=(k_2-k_1)C_1^{1-m}>0$. Every zero would thus be a strict
upward crossing. A differentiable periodic function cannot have
only such crossings: their nonzero derivatives make the zeros
isolated, compactness makes their number finite, and a return around
the circle requires a downward crossing. Hence $R$ has constant
strict sign. Equation~\eqref{eq:integral} gives
$\int C_i=-\int F/k_i$ and fixes that sign as positive.
Equation~\eqref{eq:L} now gives the strict inequality of periods.

For equal $k$, initial-value uniqueness for the smooth equation
$C'=kC^{1-m}+FC^{-m}$ on $C>0$ identifies solutions which meet.
Solutions which never meet are strictly ordered, contradicting their
equal integrals in \eqref{eq:integral}. This proves uniqueness.
\end{proof}

\section{Existence and prescribed Lee period}
Fix $k<0$, put $c=-k$, and set $f_0=\min F>0$, $f_1=\max F$.
The equation $C'=C^{-m}(F-cC)$ points inward or tangentially at
both ends of the positive interval
\[
 I_k=[f_0/c,f_1/c].
\]
Its forward flow exists on this compact interval throughout one
period. The time-two map is a continuous self-map of $I_k$;
the intermediate value theorem applied to its difference from the
identity gives a fixed point. This includes the degenerate interval
when $f_0=f_1$. The associated positive solution is two-periodic,
and all derivatives agree at the endpoints by the smooth periodic
equation. Lemma~\ref{lem:order} makes this solution $C_k$ unique.

In particular,
\begin{equation}\label{eq:barriers}
 \frac{f_0}{-k}\le C_k(r)\le\frac{f_1}{-k}.
\end{equation}
The function $L(k)=-\int F/C_k^n$ is strictly increasing by
Lemma~\ref{lem:order}. It is continuous: on a compact neighborhood
of any $k_0<0$, the barriers are uniformly positive and finite;
the equation then bounds all derivatives uniformly. Compactness
gives subsequential limits as $k\to k_0$, and the equation and
uniqueness identify every limit as $C_{k_0}$. Thus $C_k\to C_{k_0}$
uniformly and the integral is continuous. The same barriers imply
\[
 \lim_{k\uparrow0}L(k)=0,
 \qquad \lim_{k\to-\infty}L(k)=-\infty.
\]
Every $L_0<0$ therefore selects exactly one $k$. With
$D=F/C_k^m$, equations \eqref{eq:ode}--\eqref{eq:L} verify every
volume, Lee and Gauduchon requirement in
Theorem~\ref{thm:main}. This is uniqueness among all positive
periodic solutions of the radial equation.

\section{Actual twisted potentials and gauge identification}
For this metric let $l=kC^{-m}<0$ and
$f(r)=\int_0^rl(s)\,ds$ on the real radial cover. Thus
$f(r+2)=f(r)+L_0$. The solution of
\begin{equation}\label{eq:U}
 U'-lU=C
\end{equation}
with
\[
 U(0)=\frac{e^{L_0}}{1-e^{L_0}}
       \int_0^2e^{-f(s)}C(s)\,ds,
 \qquad
 U(r)=e^{f(r)}\left[U(0)+\int_0^re^{-f(s)}C(s)\,ds\right]
\]
is strictly positive on $[0,2]$ and satisfies $U(2)=U(0)$.
Periodicity of the equation makes all derivatives match, so $U$
is a global smooth positive function on $H_n$. Directly, in the
task's exact twisted convention,
\begin{align*}
 D_\lambda U
 &= (U'-lU)\alpha+
    \bigl[U''-2lU'+(l^2-l')U\bigr]\beta\\
 &=C\alpha+(C'-lC)\beta=\omega.
\end{align*}
This verifies the actual zero twisted class without any assertion
about ordinary Bott--Chern exactness.

If $\lambda_2=\lambda_1+da$ has the same radial period,
$a$ is a smooth periodic function, with its additive constant fixed
by the chosen class identification. The exact covariance formula is
\[
 e^{-a}D_{\lambda_2}U_2=D_{\lambda_1}(e^{-a}U_2).
\]
Thus the two identified classes are indeed zero and the class
difference has the genuine potential $e^{-a}U_2-U_1$.
No addition of a constant to a twisted potential is used as a
normalization. For two radial metrics with the same volume and Lee
class, the preceding uniqueness proof already gives equal metrics.

\section{Non-Vaisman volumes and an explicit family}
The squared dual norm of $dr$ for \eqref{eq:radial} is $K/D$,
where $K>0$ is a fixed constant determined by our differential
normalization. Indeed the radial complex line is orthogonal to
$\ker dr\cap\ker d^cr$, and its metric is $D\beta$.
Equation~\eqref{eq:L} therefore gives
\[
 |\lambda|_\omega^2=Kk^2\frac{C^{-2m}}{D}.
\]
A Vaisman Lee form is parallel \cite[Definition 2.3]{OV24},
so its norm is constant. Since $k\ne0$, this would imply
$D=Q C^{-2m}$ for a constant $Q>0$. At both a maximum and a
minimum of $C$, equation~\eqref{eq:k} would then give
\[
 kC^{m+1}+Q=0.
\]
This has only one positive root. The maximum and minimum of $C$
would coincide, forcing $C,D,F$ constant. Every nonconstant $F$
thus gives a non-Vaisman metric, completing the theorem.

For an explicit family take
\[
 C=1+\varepsilon\cos(\pi r),\qquad
 D=C'+C^{1-m},\qquad k=-1,
\]
where
\[
 0<\varepsilon<\min\left\{\tfrac12,
                 \frac{(3/2)^{1-m}}{4\pi}\right\}.
\]
Then $D\ge(3/2)^{1-m}-\pi\varepsilon>
\tfrac34(3/2)^{1-m}>0$. Its exact Lee form and volume density are
\[
 \lambda=-C^{-m}dr,
 \qquad F=C^mC'+C>0.
\]
The Gauduchon identity holds with $k=-1$. Moreover
$F(0)=1+\varepsilon$, $F(1)=1-\varepsilon$ and
$\frac12\int_0^2F\,dr=1$. With
$dV=\frac12\alpha^m\wedge\beta$, a positive probability measure,
the exact volume is $\omega^n=2nF\,dV$.

Its volume is not invariant under the radial Lee translation of
the standard Vaisman metric $\alpha+\beta$, since $F$ is
nonconstant. This distinguishes the prescribed data from the
invariance hypotheses in \cite[Theorem 4.1]{OV24}. It does not
assert noninvariance under the new metric's own Lee field:
its radial volume flux is $lF/D=-1$, consistently with its
Gauduchon condition. The example is an admissible non-Vaisman
member of the radial uniqueness theorem, not an unequal pair
answering the unrestricted question negatively.

\begin{thebibliography}{9}
\bibitem{OV24} L. Ornea and M. Verbitsky,
\emph{A Calabi--Yau theorem for Vaisman manifolds},
Communications in Analysis and Geometry \textbf{32} (2024),
no. 10, 2889--2900. Primary version:
\href{https://arxiv.org/abs/2206.08808v2}{arXiv:2206.08808v2},
Definition 2.3 and Theorem 4.1 with its proof and footnote 5.
\bibitem{OVbook} L. Ornea and M. Verbitsky,
\emph{Principles of Locally Conformally K\"ahler Geometry},
\href{https://arxiv.org/abs/2208.07188v6}{arXiv:2208.07188v6},
Definition 18.34 and Question 47.56(3), pp. 263 and 683--684.
\end{thebibliography}
\end{document}


## Required complete comparison

Compare all A--F claims and every generated dependency. The independent ODE parameter k>0 equals the negative of the root k<0. Compare both complete periodic existence/uniqueness arguments, continuity, endpoint ranges and all dimensions n>=2. Check exact d^c, Lee, fiber, Fubini--Study and probability-volume constants. Check both positive U formulas, actual twisted class, all fixed additive constants in a, the possible scalar kernel and conformal compensation. Check norm4pi/D, non-Vaisman conclusion for every nonconstant F, standard-Lee invariance distinction and the actual complete coupled equations for radial candidates. The current article only qualifies the deck multiplier to the defined H_n and avoids a global literature-status assertion; mathematical proof text is unchanged. The n6 bibliographic survey is observational, never a premise proving the new theorem or its priority. The author Vaisman volume theorem is background only and is not imported. Obtain fresh precise primary evidence for every indispensable external premise with valid nonnegative binding indices. No omitted or uncertain indispensable premise may be certified from an earlier verdict. State honest limitations and whether the entire scoped theorem is mathematically established. Original P04 remains unresolved.


## Final standalone source

```tex
\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\PP}{\mathbb P}
\newcommand{\D}{D_\lambda}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Prescribed radial volumes for Gauduchon LCK metrics\newline
on scalar Hopf manifolds}
\author{}
\date{}
\begin{document}
\maketitle
\noindent The unrestricted Gauduchon LCK uniqueness problem is not
resolved by this article.
\begin{abstract}
On each scalar Hopf manifold $H_n$ defined below, $n\geq2$,
a strictly positive smooth radial volume and a negative Lee period
determine exactly one radial Gauduchon locally conformally K\"ahler
metric. A periodic scalar equation gives existence, while a strict
ordering of its solutions gives uniqueness. Every resulting metric has
an explicit positive twisted potential and zero twisted Bott--Chern
class in the actual Lee gauge. A nonconstant radial volume always
produces a non-Vaisman metric. The conclusion concerns the stated
radial family and does not assert uniqueness among all LCK metrics.
\end{abstract}

\section{Forms, class data and statement}
Use $d^c=\frac{i}{4\pi}(\bar\partial-\partial)$ and
$\ddc=\frac{i}{2\pi}\partial\bar\partial$. Put $m=n-1$, where
$n\ge2$, and set
\[
 H_n=(\mathbb C^n\setminus\{0\})/\langle z\mapsto ez\rangle,
 \qquad q:H_n\longrightarrow\PP^m.
\]
Let $\kappa$ be the Fubini--Study form with $\int_{\PP^m}\kappa^m=1$.
The circle-valued function $r=\log\|z\|^2\pmod2$ has a global
differential, and
\[
 \alpha=q^*\kappa=\ddc r,
 \qquad \beta=dr\wedge d^cr.
\]
Here $\alpha$ is closed, semipositive and of rank $m$; $\beta$ is
semipositive of rank one and positive in the complex radial direction.
Their kernels are complementary. Direct differentiation gives
\begin{equation}\label{eq:forms}
 \alpha^n=\beta^2=0,\qquad
 d\beta=-dr\wedge\alpha,\qquad
 d^c\beta=-\alpha\wedge d^cr,\qquad
 \ddc\beta=-\alpha^2.
\end{equation}
On a fiber, $d^cr=d\arg z/(2\pi)$ and $r$ has period two;
therefore $\int_{q^{-1}(x)}\beta=2$ and
$\int_{H_n}\alpha^m\wedge\beta=2$.

Consider precisely the metrics
\begin{equation}\label{eq:radial}
 \omega=C(r)\alpha+D(r)\beta,
 \qquad C,D\in C^\infty(\mathbb R/2\mathbb Z),\quad C,D>0.
\end{equation}
Every such form is LCK, with actual closed Lee form
\begin{equation}\label{eq:lee}
 \lambda=l(r)\,dr,\qquad l=\frac{C'-D}{C},
 \qquad d\omega=\lambda\wedge\omega.
\end{equation}
The Lee form is unique since wedging one-forms with a positive
$(1,1)$ form is injective in complex dimension at least two.
Its period is
\begin{equation}\label{eq:period}
 L=\int_0^2l(r)\,dr=-\int_0^2\frac{D(r)}{C(r)}\,dr<0.
\end{equation}
Thus the Lee form is nonexact. Two radial Lee forms have the same
de Rham class exactly when their periods agree: their difference is
the differential of a smooth periodic function in that case, and the
radial circle detects the period in the converse direction.

For a closed real one-form $\lambda$, use
$d_\lambda=d-\lambda\wedge$,
$d_\lambda^c=d^c-\lambda^c\wedge$ and
$D_\lambda=d_\lambda d_\lambda^c$, where
$\lambda^c=\frac{i}{4\pi}(\lambda^{0,1}-\lambda^{1,0})$.
Locally, $\lambda=df$ gives
$D_\lambda u=e^f\ddc(e^{-f}u)$.
The real twisted Bott--Chern group is the space of smooth real
$d_\lambda$-closed $(1,1)$ forms modulo the image of $D_\lambda$
on smooth real functions. This is the normalized convention for the
weighted group of \cite[Definition 18.34]{OVbook}.

\begin{theorem}\label{thm:main}
For every positive smooth two-periodic function $F$ and every
$L_0<0$, there is exactly one metric of the form \eqref{eq:radial}
which is Gauduchon, has volume
\[
 \omega^n=nF(r)\alpha^m\wedge\beta,
\]
and has Lee period $L_0$. Its actual Lee form admits a positive
smooth global function $U$ such that $\omega=D_\lambda U$.
In particular its twisted Bott--Chern class is zero. If $F$ is
nonconstant, the resulting metric is not Vaisman.
\end{theorem}

Theorem~\ref{thm:main} proves uniqueness within the entire stated
radial family without assuming equality of twisted classes.
It consequently applies to radial candidates satisfying the fixed
class identification of \cite[Question 47.56(3)]{OVbook}.
That question has no radial assumption and remains unanswered here.
The known Vaisman prescribed-volume theorem assumes invariance
under the Lee and anti-Lee fields \cite[Theorem 4.1]{OV24}; the
present scalar argument does not invoke that theorem.

\section{The exact periodic equation}
For any smooth two-periodic scalar $G$, the chain rule and
\eqref{eq:forms} give
\begin{equation}\label{eq:scalar}
 \ddc G=G'\alpha+G''\beta,
 \qquad
 \ddc(G\beta)=-G'\alpha\wedge\beta-G\alpha^2.
\end{equation}
Indeed $d^c(G\beta)=-G\alpha\wedge d^cr$, since
$d^cG\wedge\beta=0$. Taking $d$ proves the second formula with
both displayed signs. Expanding the penultimate and top powers gives
\begin{align*}
 \omega^m&=C^m\alpha^m+mC^{m-1}D\alpha^{m-1}\wedge\beta,\\
 \omega^n&=nC^mD\alpha^m\wedge\beta.
\end{align*}
Consequently
\[
 \ddc(\omega^m)=
 \bigl[(C^m)''-m(C^{m-1}D)'\bigr]\alpha^m\wedge\beta.
\]
The Gauduchon condition is equivalent to
\begin{equation}\label{eq:k}
 C^{m-1}(C'-D)=k
\end{equation}
for a real constant $k$. With $F=C^mD$ fixed, this is the equation
\begin{equation}\label{eq:ode}
 C^mC'=kC+F(r),\qquad D=\frac{F}{C^m}.
\end{equation}
Integration over a period yields
\begin{equation}\label{eq:integral}
 k\int_0^2C\,dr+\int_0^2F\,dr=0,
\end{equation}
so $k<0$. Equations \eqref{eq:lee} and \eqref{eq:k} also give
\begin{equation}\label{eq:L}
 l=kC^{-m},\qquad
 L(C)=-\int_0^2\frac{F(r)}{C(r)^n}\,dr.
\end{equation}

\begin{lemma}\label{lem:order}
For fixed $F$, positive periodic solutions of \eqref{eq:ode}
are unique for a fixed $k<0$. If $k_2>k_1$, their solutions satisfy
$C_2>C_1$ everywhere and $L(C_2)>L(C_1)$.
\end{lemma}
\begin{proof}
At any zero of $R=C_2-C_1$, the equation gives
$R'=(k_2-k_1)C_1^{1-m}>0$. Every zero would thus be a strict
upward crossing. A differentiable periodic function cannot have
only such crossings: their nonzero derivatives make the zeros
isolated, compactness makes their number finite, and a return around
the circle requires a downward crossing. Hence $R$ has constant
strict sign. Equation~\eqref{eq:integral} gives
$\int C_i=-\int F/k_i$ and fixes that sign as positive.
Equation~\eqref{eq:L} now gives the strict inequality of periods.

For equal $k$, initial-value uniqueness for the smooth equation
$C'=kC^{1-m}+FC^{-m}$ on $C>0$ identifies solutions which meet.
Solutions which never meet are strictly ordered, contradicting their
equal integrals in \eqref{eq:integral}. This proves uniqueness.
\end{proof}

\section{Existence and prescribed Lee period}
Fix $k<0$, put $c=-k$, and set $f_0=\min F>0$, $f_1=\max F$.
The equation $C'=C^{-m}(F-cC)$ points inward or tangentially at
both ends of the positive interval
\[
 I_k=[f_0/c,f_1/c].
\]
Its forward flow exists on this compact interval throughout one
period. The time-two map is a continuous self-map of $I_k$;
the intermediate value theorem applied to its difference from the
identity gives a fixed point. This includes the degenerate interval
when $f_0=f_1$. The associated positive solution is two-periodic,
and all derivatives agree at the endpoints by the smooth periodic
equation. Lemma~\ref{lem:order} makes this solution $C_k$ unique.

In particular,
\begin{equation}\label{eq:barriers}
 \frac{f_0}{-k}\le C_k(r)\le\frac{f_1}{-k}.
\end{equation}
The function $L(k)=-\int F/C_k^n$ is strictly increasing by
Lemma~\ref{lem:order}. It is continuous: on a compact neighborhood
of any $k_0<0$, the barriers are uniformly positive and finite;
the equation then bounds all derivatives uniformly. Compactness
gives subsequential limits as $k\to k_0$, and the equation and
uniqueness identify every limit as $C_{k_0}$. Thus $C_k\to C_{k_0}$
uniformly and the integral is continuous. The same barriers imply
\[
 \lim_{k\uparrow0}L(k)=0,
 \qquad \lim_{k\to-\infty}L(k)=-\infty.
\]
Every $L_0<0$ therefore selects exactly one $k$. With
$D=F/C_k^m$, equations \eqref{eq:ode}--\eqref{eq:L} verify every
volume, Lee and Gauduchon requirement in
Theorem~\ref{thm:main}. This is uniqueness among all positive
periodic solutions of the radial equation.

\section{Actual twisted potentials and gauge identification}
For this metric let $l=kC^{-m}<0$ and
$f(r)=\int_0^rl(s)\,ds$ on the real radial cover. Thus
$f(r+2)=f(r)+L_0$. The solution of
\begin{equation}\label{eq:U}
 U'-lU=C
\end{equation}
with
\[
 U(0)=\frac{e^{L_0}}{1-e^{L_0}}
       \int_0^2e^{-f(s)}C(s)\,ds,
 \qquad
 U(r)=e^{f(r)}\left[U(0)+\int_0^re^{-f(s)}C(s)\,ds\right]
\]
is strictly positive on $[0,2]$ and satisfies $U(2)=U(0)$.
Periodicity of the equation makes all derivatives match, so $U$
is a global smooth positive function on $H_n$. Directly, in the
task's exact twisted convention,
\begin{align*}
 D_\lambda U
 &= (U'-lU)\alpha+
    \bigl[U''-2lU'+(l^2-l')U\bigr]\beta\\
 &=C\alpha+(C'-lC)\beta=\omega.
\end{align*}
This verifies the actual zero twisted class without any assertion
about ordinary Bott--Chern exactness.

If $\lambda_2=\lambda_1+da$ has the same radial period,
$a$ is a smooth periodic function, with its additive constant fixed
by the chosen class identification. The exact covariance formula is
\[
 e^{-a}D_{\lambda_2}U_2=D_{\lambda_1}(e^{-a}U_2).
\]
Thus the two identified classes are indeed zero and the class
difference has the genuine potential $e^{-a}U_2-U_1$.
No addition of a constant to a twisted potential is used as a
normalization. For two radial metrics with the same volume and Lee
class, the preceding uniqueness proof already gives equal metrics.

\section{Non-Vaisman volumes and an explicit family}
The squared dual norm of $dr$ for \eqref{eq:radial} is $K/D$,
where $K>0$ is a fixed constant determined by our differential
normalization. Indeed the radial complex line is orthogonal to
$\ker dr\cap\ker d^cr$, and its metric is $D\beta$.
Equation~\eqref{eq:L} therefore gives
\[
 |\lambda|_\omega^2=Kk^2\frac{C^{-2m}}{D}.
\]
A Vaisman Lee form is parallel \cite[Definition 2.3]{OV24},
so its norm is constant. Since $k\ne0$, this would imply
$D=Q C^{-2m}$ for a constant $Q>0$. At both a maximum and a
minimum of $C$, equation~\eqref{eq:k} would then give
\[
 kC^{m+1}+Q=0.
\]
This has only one positive root. The maximum and minimum of $C$
would coincide, forcing $C,D,F$ constant. Every nonconstant $F$
thus gives a non-Vaisman metric, completing the theorem.

For an explicit family take
\[
 C=1+\varepsilon\cos(\pi r),\qquad
 D=C'+C^{1-m},\qquad k=-1,
\]
where
\[
 0<\varepsilon<\min\left\{\tfrac12,
                 \frac{(3/2)^{1-m}}{4\pi}\right\}.
\]
Then $D\ge(3/2)^{1-m}-\pi\varepsilon>
\tfrac34(3/2)^{1-m}>0$. Its exact Lee form and volume density are
\[
 \lambda=-C^{-m}dr,
 \qquad F=C^mC'+C>0.
\]
The Gauduchon identity holds with $k=-1$. Moreover
$F(0)=1+\varepsilon$, $F(1)=1-\varepsilon$ and
$\frac12\int_0^2F\,dr=1$. With
$dV=\frac12\alpha^m\wedge\beta$, a positive probability measure,
the exact volume is $\omega^n=2nF\,dV$.

Its volume is not invariant under the radial Lee translation of
the standard Vaisman metric $\alpha+\beta$, since $F$ is
nonconstant. This distinguishes the prescribed data from the
invariance hypotheses in \cite[Theorem 4.1]{OV24}. It does not
assert noninvariance under the new metric's own Lee field:
its radial volume flux, with the universal factor $4\pi$ omitted,
is $lF/D=-1$, consistently with its Gauduchon condition.
The example is an admissible non-Vaisman
member of the radial uniqueness theorem, not an unequal pair
answering the unrestricted question negatively.

\begin{thebibliography}{9}
\bibitem{OV24} L. Ornea and M. Verbitsky,
\emph{A Calabi--Yau theorem for Vaisman manifolds},
Communications in Analysis and Geometry \textbf{32} (2024),
no. 10, 2889--2900. Primary version:
\href{https://arxiv.org/abs/2206.08808v2}{arXiv:2206.08808v2},
Definition 2.3 and Theorem 4.1 with its proof and footnote 5.
\bibitem{OVbook} L. Ornea and M. Verbitsky,
\emph{Principles of Locally Conformally K\"ahler Geometry},
\href{https://arxiv.org/abs/2208.07188v6}{arXiv:2208.07188v6},
Definition 18.34 and Question 47.56(3), pp. 263 and 683--684.
\end{thebibliography}
\end{document}
```
