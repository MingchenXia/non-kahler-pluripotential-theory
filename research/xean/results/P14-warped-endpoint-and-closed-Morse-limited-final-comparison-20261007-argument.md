# P14 restricted A-E final comparison base, not yet submitted

This is a whole-proof comparison of the complete current warped article and the independently reconstructed A-E chain once supplied. It is not another original completion claim. The old wider numerical-order and divisor-modification proposal is preserved in its original assembly, but is excluded from the current article scope and is not an accepted mathematical premise. The earlier unchanged-original full report remains INCONCLUSIVE. Its review of unrelated private comparisons does not make those assertions part of the restricted theorem. Known product calculations and examples retain their credit. The current universal-improper-identity background observation and possible surface generalization are also excluded; no proof or result about those observations is proposed by this article. All primary statements must be independently assessed.


# Complete current working article A-E

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Endpoint cost for all minimizing Gauduchon metrics\newline on nonclosed warped paths}
\author{}\date{}
\begin{document}\maketitle
\noindent\textbf{Working draft.} This new root-developed candidate has not
passed complete native review, independent reconstruction or final comparison.
\begin{abstract}
We propose an exact endpoint-cost theorem on a compact K\"ahler manifold
times a curve. A smooth nonnegative vertical coefficient determines
nonclosed paths with actual balanced minimizers. The cost is independent
of every choice of attaining Gauduchon metric, and its improper integral
equals the drop in root volume. Tubular codimension and vanishing order
give five quantitative integrable profiles. Positive endpoint volume is
compatible with failure of bigness, which is excluded for every genuine
quasi-psh strict representative by a smooth closed test.
\end{abstract}

Use $\ddc=\frac{i}{2\pi}\partial\bar\partial$ and ordinary wedge powers.
Let $(B,\alpha)$ be a connected compact K\"ahler $m$-fold, $m\geq2$,
$W=\int_B\alpha^m>0$. Let $C$ be a connected compact complex curve
with a smooth positive probability form $w$, and $\sigma$ a smooth
positive probability on $B$. Put $X=B\times C$, $n=m+1$,
$\mu=\sigma\wedge w$; suppress pullbacks. Fix $a\geq0$ smooth and $t>0$.
Consider the strict path and nef endpoint
\[
 \theta_s=\alpha+(a+t-s)w,\quad 0\leq s<t,
 \qquad\theta_t=\alpha+aw,\qquad\eta=w.
\]
For nonconstant $a$, the torsion is $d\theta_s=da\wedge w\ne0$.
Dependence on the specified $\sigma$ remains in the formulas below.

For every smooth positive Gauduchon metric define
\[
 D_\mu(\gamma)=\int_X(\mu/\gamma^n)^{1/n}\gamma^n,
 \quad\lambda_\mu(\theta)=
 \inf_{\ddc\gamma^m=0}\frac{\int_X\theta\wedge\gamma^m}{D_\mu(\gamma)},
 \quad V_\mu=\lambda_\mu^n.
\]
The endpoint is defined by decreasing Hermitian regularization, agreeing
with the nonnegative full infimum as proved below. A background is big
if it has a genuine global quasi-psh potential making it dominate a
positive multiple of a Hermitian metric.

\section{Actual minimizers and the full volume}
Write $\epsilon=t-s$, $L=a+\epsilon$, and
\[
 H(\epsilon)=\int_B\frac{\sigma}{a+\epsilon},\qquad
 J(\epsilon)=\int_B\frac{\sigma}{(a+\epsilon)^2}.
\]
Smooth Monge--Amp\`ere existence in the closed positive class
$[\alpha]$, in the formulation of \cite[Corollary 1]{TW}, gives
\[
 A_\epsilon=\alpha+\ddc\phi_\epsilon>0,\qquad
 A_\epsilon^m=\frac{W}{H(\epsilon)}\frac{\sigma}{L}.
\]
The target has total mass $W$, so integration in the closed class fixes
the source scalar. Our potential is $2\pi$ times the source's
$i\partial\bar\partial$ potential. No endpoint equation or uniform
endpoint estimate is imported.

Set $\Omega_\epsilon=A_\epsilon+Lw$,
$c_\epsilon=nW/H(\epsilon)$, and
$\gamma_s=L^{-1/m}\Omega_\epsilon$. Then
\[
 \Omega_\epsilon^n=c_\epsilon\mu,
 \qquad \gamma_s^m=L^{-1}A_\epsilon^m+mA_\epsilon^{m-1}\wedge w.
\]
Its first cofactor summand is a base top-degree form and its second is
closed, so $d\gamma_s^m=0$. For every admissible test $\xi$, smooth
Stokes and matrix AM--GM give
\[
 \int_X\theta_s\wedge\xi^m=\int_X\Omega_\epsilon\wedge\xi^m
 \geq c_\epsilon^{1/n}D_\mu(\xi).
\]
For the named $\gamma_s$ the numerator is $nW$ and denominator
$c_\epsilon^{m/n}H(\epsilon)$; hence it attains equality. In particular
\begin{equation}\label{eq:volume}
 V_\mu(\theta_s)=\frac{nW}{H(t-s)}.
\end{equation}
This is the full infimum over all smooth positive Gauduchon metrics,
not an infimum over product tests.

\section{Cost independent of the minimizing selection}
For an actual attaining metric $\xi$ at $s$ define
\[
 C_\xi(s)=\frac{\int_X w\wedge\xi^m}{D_\mu(\xi)}.
\]
The named balanced metric satisfies
\[
 \int_X w\wedge\gamma_s^m=\frac{WJ}{H},
 \quad D_\mu(\gamma_s)=(nW/H)^{m/n}H,
 \quad C(s)=n^{-m/n}W^{1/n}H^{-(n+1)/n}J.
\]
The last expression is also $-\lambda_\mu'(\theta_s)$ by
differentiating \eqref{eq:volume}.

\begin{lemma}\label{lem:all}
Every actual minimizing Gauduchon metric at $s$ has cost $C(s)$.
No differentiability of a selected family of metrics is required.
\end{lemma}
\begin{proof}
Hold any such $\xi$ fixed. The all-test infimum at a nearby path point
gives, for both signs of sufficiently small $\delta$,
\[
 \lambda_\mu(\theta_{s+\delta})
 \leq\lambda_\mu(\theta_s)-\delta C_\xi(s).
\]
The explicit volume is differentiable on the strict path. Dividing by
positive and negative $\delta$ and taking their limits forces
$C_\xi(s)=-\lambda_\mu'(\theta_s)=C(s)$.
At $s=0$ the same argument uses the short strict extension to negative
$s$, for which $a+t-s$ is still positive.
\end{proof}

\begin{theorem}\label{th:endpoint}
For any smooth $a\geq0$ and any selection of actual attaining metrics,
the improper integral exists and
\[
 \int_0^t C(s)\,ds
 =\lambda_\mu(\theta_0)-\lambda_\mu(\theta_t)<\infty,
 \qquad V_\mu(\theta_t)=\frac{nW}{H(0)}.
\]
Here $H(0)=\int_B\sigma/a$, with endpoint volume zero if it is infinite.
\end{theorem}
\begin{proof}
The full root infimum at the nef endpoint is the limit of its strict
path values. Monotonicity gives one inequality. For any fixed test its
quotient converges to its endpoint quotient; taking the infimum gives
the reverse inequality. The same argument with any positive Hermitian
regularization identifies the original endpoint definition.
Monotone convergence yields $H(\epsilon)\to H(0)$, so
\eqref{eq:volume} gives the asserted actual endpoint value.

On each compact strict path segment the fundamental theorem gives
\[
 \int_0^r C(s)\,ds=\lambda_\mu(\theta_0)-\lambda_\mu(\theta_r).
\]
The integrand is nonnegative and the endpoint limit just proved is
finite. Letting $r\uparrow t$ proves the improper identity.
Neither integrability nor an endpoint Monge--Amp\`ere solution has been
assumed. Lemma~\ref{lem:all} covers every minimizing selection.
\end{proof}

\section{Quantitative geometric profiles}
Suppose $\{a=0\}$ is a smooth compact real submanifold of codimension
$d>0$ and in a fixed tube
$a\asymp\operatorname{dist}(\cdot,\{a=0\})^k$, $k>0$,
with positive two-sided constants. Assume $a$ is bounded below outside
the tube, and put $r=d/k$. These are geometric hypotheses on the
coefficient, not hypotheses on the desired cost.

Tubular integration compares $H$ and $J$ to
\[
 \int_0^R\frac{u^{d-1}}{u^k+\epsilon}\,du,
 \qquad \int_0^R\frac{u^{d-1}}{(u^k+\epsilon)^2}\,du.
\]
Splitting at $\epsilon^{1/k}$ gives the thresholds one and two. Therefore
\begin{equation}\label{eq:profiles}
 C(t-\epsilon)\asymp
 \begin{cases}
 \epsilon^{(1-r)/n-1},&r<1,\\
 \epsilon^{-1}\bigl[\log(1/\epsilon)\bigr]^{-(n+1)/n},&r=1,\\
 \epsilon^{r-2},&1<r<2,\\
 \log(1/\epsilon),&r=2,\\
 1,&r>2.
 \end{cases}
\end{equation}
In the final case the cost tends to the finite positive value
$n^{-m/n}W^{1/n}H(0)^{-(n+1)/n}J(0)$ by dominated convergence.
Each profile is integrable: the first power is greater than $-1$;
the logarithmic power at $r=1$ exceeds one; the power for $1<r<2$
is again greater than $-1$. The endpoint volume is positive exactly
when $d>k$. With finitely many disjoint finite-order components the
same comparisons use their smallest codimension/order ratio.

\section{Bigness and an explicit positive-volume nonbig endpoint}
If $a$ has a zero, $\theta_t$ is not big. Indeed suppose for a genuine
quasi-psh $u$ that
\[
 \theta_t+\ddc u\geq\delta(\alpha+w),\qquad\delta>0.
\]
Test against the pullback of an arbitrary smooth nonnegative base
top-degree form $\zeta$. This test is $\ddc$-closed by dimension, so
distributional Stokes gives
$\int_B(a-\delta)\zeta\geq0$.
A nonzero $\zeta$ supported where $a<\delta$ contradicts this.
The argument uses local integrability of genuine quasi-psh functions
and smooth tests; no singular potential is restricted to a curve fiber.
If $a>0$ everywhere then $\theta_t$ itself is positive and big.
Thus in this family bigness is exactly the absence of zeros.

For a concrete genuinely nonclosed example take $B=\mathbb P^m$,
$\alpha=\kappa$ normalized Fubini--Study, $\sigma=\kappa^m$,
$C=\mathbb P^1$, and
\[
 a([Z])=\frac{\sum_{j=1}^m|Z_j|^2}{\sum_{j=0}^m|Z_j|^2}.
\]
Its single zero is quadratic in a real codimension-$2m$ affine chart,
so $r=m>1$. The law of $a$ has density $m x^{m-1}dx$ on $[0,1]$:
polar integration in the $Z_0$ chart gives radial density
$m q^{m-1}(1+q)^{-m-1}dq$, and $x=q/(1+q)$ gives this law.
Hence $W=1$, $H(0)=m/(m-1)$ and
\[
 V_\mu(\theta_t)=\frac{(m+1)(m-1)}m>0,
\]
although the endpoint is not big. Its cost is logarithmic at $m=2$,
and has a finite positive limit for $m>2$.
These statements retain the nonclosed torsion and the chosen probability.

\section{Closed Morse comparison and the closed-core boundary}
In the closed subcase $a\equiv a_0\geq0$, put
$P=\alpha+(a_0+t)w$ and $Q=tw$ on the compact K\"ahler product.
Both forms are $d$-closed and their real $(1,1)$ classes are nef.
Since $w^2=0$ and $\alpha^{m+1}=0$,
\[
 \int_X P^n=nW(a_0+t),\qquad
 \int_X P^{n-1}\wedge Q=tW.
\]
The cohomological nef Morse inequality
\cite[Theorem 1.1]{Morse} therefore reads
\[
 \operatorname{vol}([P]-[Q])\geq
 \int_XP^n-n\int_XP^{n-1}\wedge Q
 =nWa_0=V_\mu(\theta_t).
\]
For $a_0>0$, the final equality also follows directly from
$H(0)=1/a_0$; for $a_0=0$ both displayed values are zero.
The expression is independent of $\sigma$ because $\int_B\sigma=1$.
Here $\operatorname{vol}$ is the usual volume of a closed cohomology
class, extended by zero outside the pseudoeffective cone.
This comparison uses the established closed-class theorem, without
proposing another proof of its general assertion.

For nonconstant $a$, $d\theta_t=da\wedge w\ne0$ and
$H(0)=\int_B\sigma/a$ retains the specified density.
There is no class $[\theta_t]$ to which that closed-class theorem applies.
In particular the preceding comparison supplies no nonclosed
intersection-number formula.

Moreover every endpoint with a zero lies outside the closed-core
hypothesis. Suppose, even up to a smooth global potential gauge, that
$\theta_t=\chi+\beta+\ddc f$, where $\chi$ is smooth real and
$d$-closed, $[\chi]$ is nef with $\int_X\chi^n>0$, and
$\beta\geq0$ is smooth. By \cite[Theorem 2.12]{DP}, the class
$[\chi]$ contains a K\"ahler current. The K\"ahler
$\partial\bar\partial$ lemma and the rescaling of potentials give a
genuine global quasi-psh $v$ with
$\chi+\ddc v\geq\delta(\alpha+w)$ for some $\delta>0$.
Then
\[
 \theta_t+\ddc(v-f)=\chi+\ddc v+\beta
 \geq\delta(\alpha+w),
\]
contradicting the nonbigness proof for every genuine potential.
This excludes every such closed nef positive-volume core, rather than
only a chosen product core.

The full product volume calculation, tubular inverse-moment estimates
and a scaled version of the projective positive-volume nonbig example
already occur in the companion manuscript and the checked warped-cone
calculation \cite{Companion}. They serve here as context.
The present theorem gives the exact improper endpoint identity for
every attaining selection on an arbitrary compact K\"ahler base,
and the five geometric cost profiles. No literature priority or
classification of arbitrary nonclosed paths is asserted.

\begin{remark}
This theorem supplies a geometric endpoint family beyond conclusions
requiring a closed positive-volume core. It does not classify arbitrary
paths or assert that positive nonclosed root volume implies bigness.
Only the closed base mass $W$ is invariant under smooth potential
changes; no nonclosed intersection-number invariance, metric uniqueness,
endpoint PDE solvability or literature priority is asserted.
\end{remark}
\begin{thebibliography}{9}
\bibitem{TW} V. Tosatti and B. Weinkove, \emph{The complex Monge--Amp\`ere
equation on compact Hermitian manifolds}, arXiv:0910.1390v2
(11 November 2009), Corollary 1 and closed-background normalization,
pp.~1--2; \url{https://arxiv.org/abs/0910.1390}.
\bibitem{DP} J.-P. Demailly and M. P\u{a}un,
\emph{Numerical characterization of the K\"ahler cone of a compact
K\"ahler manifold}, arXiv:math/0105176v2 (24 September 2001),
Theorem 2.12; \url{https://arxiv.org/abs/math/0105176}.
\bibitem{Morse} V. Tosatti, \emph{Transcendental Morse inequality on
K\"ahler manifolds}, arXiv:2608.30153v2 (8 September 2026),
Theorem 1.1; \url{https://arxiv.org/abs/2608.30153}.
\bibitem{Companion} M. Xia, \emph{Non-K\"ahler pluripotential theory},
companion repository: the radial positive-volume nonbig example,
Gauduchon test limits and volume-variation sections, and the
P15 warped-cone calculation;
\url{https://github.com/MingchenXia/non-kahler-pluripotential-theory}.
\end{thebibliography}
\end{document}



# Unchanged complete original full-review report, historical INCONCLUSIVE

{
  "verdict": "INCONCLUSIVE",
  "report": "The displayed restricted warped-path theorem checks out mathematically. I found no concrete defect in its volume formula, minimizing metrics, endpoint passage, cost profiles, nonbigness proof, or stated modification comparisons. Exact task completion remains uncertified: novelty relative to the mentioned companion manuscripts cannot be checked from the supplied overlap notes, and the submitted article omits the requested Morse-bound comparison. The unspecified historical residual-jump claims are also not independently established here. These limitations do not invalidate the restricted endpoint theorem or justify declaring the original programme closed.\n\nThe smooth existence application is valid. On the closed Kähler representative Kε, the target density is smooth, strictly positive, and has mass Wε. [Tosatti–Weinkove, Corollary 1](https://arxiv.org/pdf/0910.1390v2) supplies the solution up to a scalar; closed Stokes forces that scalar to be zero. Multiplying its potential by 2π gives the specified dd^c normalization. No uniform endpoint estimate is needed. Independently expanding Ωε^n gives cε μ. Matrix AM–GM and Gauduchon Stokes provide the lower bound for every test. The displayed cofactor γ ε^m is closed: its first term has top base degree, and its second has closed factors. Its numerator nWε and denominator cε^(m/n)Hε attain equality, proving the full-test formula and actual minimizing-test existence.\n\nThe cost computation and differentiation agree, including every factor of n and H. Holding any attaining test fixed and using both signs of the path increment proves that every minimizer has the same cost. The short negative-s extension handles s=0. Consequently arbitrary minimizing selections produce the same smooth scalar integrand; no measurable or differentiable metric selection is required. Monotonicity and the fixed-test upper bound establish the actual endpoint infimum, also for Hermitian regularization. Monotone convergence identifies H(0), including infinity. The fundamental theorem on compact segments then proves the finite improper integral without assuming its desired bound.\n\nThe tubular estimates reconstruct correctly. Splitting at ε^(1/k) gives H thresholds d/k=1 and J thresholds d/k=2, yielding all five stated integrable profiles. The r>2 limit follows by dominated convergence. Finite disjoint components are controlled by the smallest ratio. The polynomial Wε has nonnegative coefficients and leading order ε^(m−ν), so the volume power order is q+z. Density-comparison and metric-sandwich arguments preserve this order; their constants depend on density bounds and geometry, and give no density-independent exact value.\n\nThe modification arguments also work under their stated hypotheses. Vanishing mass of positive nef approximants forces their weak limit to zero; nondegeneracy of the de Rham pairing then gives [χ]^j=0. Pullback preserves ν. Pairing effective divisor currents with positive nef approximants proves ν(χD)≤ν(π*χ). Degree-one integration and σY≥cπ*σB prove zY≥zB. The real-divisor potential must be the weighted sum of individual logarithmic norms, as the final source application correctly specifies. Its normalization agrees with [Demailly V.13.2](https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf).\n\nThe nonbigness test is valid for every genuine quasi-psh potential: pullback base top-degree tests are smooth, positive and dd^c-closed, and distributional Stokes eliminates dd^c u. It forces a≥δ everywhere. Conversely, a>0 makes the endpoint itself positive. The projective radial density, H(0)=m/(m−1), endpoint volume (m+1)(m−1)/m, and logarithmic versus finite cost limits are correct. Since X is Kähler, [Demailly–Păun’s positive-mass nef criterion](https://arxiv.org/pdf/math/0105176) also confirms that these nonbig endpoints cannot contain a closed nef positive-volume core plus a semipositive summand.\n\nFor the missing comparison, the Morse inequality concerns usual cohomological volume and d-closed nef real (1,1) classes on a compact Kähler manifold; its general quantitative statement appears in [Tosatti, Theorem 1.1, September 2026](https://arxiv.org/pdf/2608.30153v2). In the closed subcase a≡a0, take A=α+(a0+t)w and B=tw: its right-hand side is nWa0, exactly the computed endpoint root-volume power Vμ. For nonconstant a, dθ=da∧w and the inverse moment H retains μ-dependence, so the cohomological comparison cannot be transferred to this nonclosed background.\n\nPresentation corrections: define the otherwise undefined symbols a− and a+; the proved logarithmic volume exponent is q+z. Specify that modification ‘equality’ means equality of power orders. It does not include logarithmic comparability or preservation of positive endpoint volume: the quadratic point-blowup case has order zero on both bases but introduces inverse-logarithmic decay.",
  "passages": [
    {
      "id": "6bea049b-1c8c-4297-97d4-705c2e658a0c/0",
      "statement": "On a connected compact Hermitian manifold (M,ω) of complex dimension d≥2, every smooth real function F admits a unique real number b and a unique smooth real function ψ normalized by sup_M ψ=0 such that ω+i∂bar∂ψ>0 and (ω+i∂bar∂ψ)^d=e^(F+b)ω^d (Tosatti–Weinkove, arXiv:0910.1390v2, Corollary 1).",
      "url": "https://arxiv.org/pdf/0910.1390v2",
      "quote": "there exists a unique real number b and a unique smooth real-valued function ϕ on M solving",
      "premise": 0
    },
    {
      "id": "6bea049b-1c8c-4297-97d4-705c2e658a0c/1",
      "statement": "For a holomorphic line bundle L on a complex manifold, equipped with a smooth Hermitian metric of Chern curvature Θ(L), and a holomorphic section s not identically zero on any connected component, log||s||² is locally integrable and satisfies (i/(2π))∂bar∂log||s||²=[div(s)]−iΘ(L)/(2π); the effective divisor integration current [div(s)] is positive and closed.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "(13.2) id′d′′ log |s|² = 2π ∑mj [Zj] − i Θ(E).",
      "premise": 1
    },
    {
      "id": "6bea049b-1c8c-4297-97d4-705c2e658a0c/2",
      "statement": "For every compact oriented smooth real N-manifold without boundary, the de Rham cohomology groups are finite dimensional and the integration pairing H^p_dR(M,R)×H^(N−p)_dR(M,R)→R is nondegenerate.",
      "url": "https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf",
      "quote": "is a non degenerate duality.",
      "premise": 2
    },
    {
      "id": "6bea049b-1c8c-4297-97d4-705c2e658a0c/3",
      "statement": "If (M,ω) is a compact Kähler n-fold and τ is a smooth d-closed real (1,1)-form whose class is nef and satisfies ∫_M τ^n>0, then there exist δ>0 and a genuine global quasi-psh function u such that τ+(i/(2π))∂bar∂u≥δω (Demailly–Păun, Theorem 2.12).",
      "url": "https://arxiv.org/pdf/math/0105176",
      "quote": "contains a Kähler current T, that is, a closed positive current T such that T ≥ δω for some δ > 0.",
      "premise": 3
    },
    {
      "id": "6bea049b-1c8c-4297-97d4-705c2e658a0c/4",
      "statement": "For a compact Kähler n-fold M and nef real (1,1) cohomology classes A and B, the usual cohomological volume, set to zero outside the pseudoeffective cone, satisfies vol(A−B)≥∫_M A^n−n∫_M A^(n−1)B (Tosatti, arXiv:2608.30153v2, Theorem 1.1).",
      "url": "https://arxiv.org/pdf/2608.30153v2",
      "quote": "Vol([α] − [β]) ⩾ ∫X αⁿ − n ∫X αⁿ⁻¹ ∧ β.",
      "premise": 4
    }
  ],
  "premises": [
    "On a connected compact Hermitian manifold (M,ω) of complex dimension d≥2, every smooth real function F admits a unique real number b and a unique smooth real function ψ normalized by sup_M ψ=0 such that ω+i∂bar∂ψ>0 and (ω+i∂bar∂ψ)^d=e^(F+b)ω^d (Tosatti–Weinkove, arXiv:0910.1390v2, Corollary 1).",
    "For a holomorphic line bundle L on a complex manifold, equipped with a smooth Hermitian metric of Chern curvature Θ(L), and a holomorphic section s not identically zero on any connected component, log||s||² is locally integrable and satisfies (i/(2π))∂bar∂log||s||²=[div(s)]−iΘ(L)/(2π); the effective divisor integration current [div(s)] is positive and closed.",
    "For every compact oriented smooth real N-manifold without boundary, the de Rham cohomology groups are finite dimensional and the integration pairing H^p_dR(M,R)×H^(N−p)_dR(M,R)→R is nondegenerate.",
    "If (M,ω) is a compact Kähler n-fold and τ is a smooth d-closed real (1,1)-form whose class is nef and satisfies ∫_M τ^n>0, then there exist δ>0 and a genuine global quasi-psh function u such that τ+(i/(2π))∂bar∂u≥δω (Demailly–Păun, Theorem 2.12).",
    "For a compact Kähler n-fold M and nef real (1,1) cohomology classes A and B, the usual cohomological volume, set to zero outside the pseudoeffective cone, satisfies vol(A−B)≥∫_M A^n−n∫_M A^(n−1)B (Tosatti, arXiv:2608.30153v2, Theorem 1.1)."
  ],
  "kind": "codex-report",
  "operationId": "6bea049b-1c8c-4297-97d4-705c2e658a0c",
  "reportedAt": "2026-10-07T22:28:12.154Z"
}



# Known companion evidence, not a trusted proof premise: section_radial_positive_volume_nonbig.tex

\Needspace{12\baselineskip}
\section{Positive volume without bigness}
\label{sec:radial-positive-volume-nonbig}

By \cref{cor:gaud-volume-big-positive}, every big background has positive volume. For a closed nef class on a compact K\"ahler manifold the converse also holds: the volume is then $\int_X\theta^n$, and a closed nef class with positive top self-intersection is big. We now show that the converse fails for nonclosed nef backgrounds, even on a projective manifold: such a background can have positive volume without containing a K\"ahler current. In the example, the coefficient of a fiber direction vanishes at one point of the base. A radial potential on the base compensates for this vanishing, and the determinant of the resulting current bounds every Gauduchon quotient from below. Bigness, on the other hand, is excluded by pairing with a closed semipositive form concentrated near the vanishing point.

Throughout this section fix an integer $m\geq2$, and put $n=m+1$, $t=(m-1)/m$ and $B=\mathbb P^m$. Give $B$ and $\mathbb P^1$ their Fubini--Study forms $\omega$ and $w$, normalized by $\int_B\omega^m=\int_{\mathbb P^1}w=1$. On $B$ define
\[
 x([Z_0:\cdots:Z_m])=
 \frac{\sum_{j=1}^m|Z_j|^2}{\sum_{j=0}^m|Z_j|^2},
 \qquad a=x/t,\qquad p=[1:0:\cdots:0].
\]
Thus $x$ is a smooth function on $B$ with values in $[0,1]$; it vanishes only at $p$ and equals one on the hyperplane $\{Z_0=0\}$. On $X=B\times\mathbb P^1$, with pullbacks understood, set
\[
 h=\omega+w,\qquad \mu=\omega^m\wedge w,
 \qquad\theta=\omega+a w.
\]
For $\epsilon>0$ put
\begin{equation}\label{eq:radial-volume-normalization}
 H_\epsilon=m\int_0^1\frac{y^{m-1}}{y/t+\epsilon}\,\mathrm{d}y.
\end{equation}

\begin{lemma}\label{lem:radial-volume-representatives}
There are smooth real functions $\varphi_\epsilon$ on $B$ such that $A_\epsilon=\omega+\ddc\varphi_\epsilon>0$ and
\begin{equation}\label{eq:radial-volume-smooth-density}
 A_\epsilon^m=\frac{\omega^m}{H_\epsilon(a+\epsilon)}.
\end{equation}
As $\epsilon\downarrow0$ they converge uniformly to a bounded continuous function $\varphi\in\PSH(B,\omega)$ that is smooth on $B\setminus\{p\}$. On $B\setminus\{p\}$ the current $A=\omega+\ddc\varphi$ is a smooth strictly positive form satisfying
\begin{equation}\label{eq:radial-volume-endpoint-density}
 A^m=a^{-1}\omega^m.
\end{equation}
Moreover $H_\epsilon\to1$ as $\epsilon\downarrow0$.
\end{lemma}
\begin{proof}
In the affine chart $Z_0=1$, write $s=|z|^2$. Then $x=s/(1+s)$ and $\omega=\ddc\log(1+s)$. Polar integration gives
\begin{equation}\label{eq:radial-volume-integration}
 \int_B b(x)\omega^m=m\int_0^1 b(y)y^{m-1}\,\mathrm{d}y
\end{equation}
for every integrable function $b$ on $[0,1]$, since the normalized radial density of $\omega^m$ in the variable $s$ is $m s^{m-1}(1+s)^{-m-1}\,\mathrm{d}s$. In particular $\int_B a^{-1}\omega^m=mt/(m-1)=1$, and monotone convergence in \eqref{eq:radial-volume-normalization} gives $H_\epsilon\to1$.

Define $q_\epsilon\geq0$ and $\varphi_\epsilon$ on $[0,1]$ by
\[
 q_\epsilon(x)^m=\frac m{H_\epsilon}
       \int_0^x\frac{y^{m-1}}{y/t+\epsilon}\,\mathrm{d}y,
 \qquad
 \varphi_\epsilon(x)=\int_0^x
       \frac{q_\epsilon(y)-y}{y(1-y)}\,\mathrm{d}y.
\]
Near zero,
\[
 q_\epsilon(x)=x\left(\frac m{H_\epsilon}
       \int_0^1\frac{u^{m-1}}{xu/t+\epsilon}\,\mathrm{d}u\right)^{1/m},
\]
so $q_\epsilon$ is $x$ times a smooth positive function; moreover $q_\epsilon(1)=1$. Hence both apparent singularities of $\varphi_\epsilon'$, at $0$ and at $1$, are removable, and $\varphi_\epsilon$ is smooth on $[0,1]$. Composing with the smooth function $x$ gives a smooth function on $B$, again denoted $\varphi_\epsilon$.

To compute $A_\epsilon$, recall that for a local potential of the form $F(s)$, with $q=sF'(s)$, the complex Hessian has the tangential eigenvalue $q/s$, of multiplicity $m-1$, and the radial eigenvalue $\mathrm{d}q/\mathrm{d}s$. For $F_\epsilon=\log(1+s)+\varphi_\epsilon(x)$ one finds $sF_\epsilon'=q_\epsilon(x)$. Differentiating the integral defining $q_\epsilon$ shows that both eigenvalues are positive, also at $s=0$ by the smooth factorization above. Their product relative to the Fubini--Study determinant is
\[
 \frac{A_\epsilon^m}{\omega^m}
 =\frac{q_\epsilon^{m-1}q_\epsilon'}{x^{m-1}}
 =\frac1{H_\epsilon(a+\epsilon)}.
\]
At a point of the hyperplane $\{Z_0=0\}$, the smooth form $A_\epsilon$ is semipositive, as a limit of the positive matrices in the affine chart. Since the determinant just computed extends there with a strictly positive value, every eigenvalue is positive. This proves strict positivity on all of $B$ and \eqref{eq:radial-volume-smooth-density}.

We now pass to the limit. For $x>0$, $q_\epsilon(x)$ tends to $x^t$. To bound $q_\epsilon$ uniformly, note that $q_\epsilon^m$ is the distribution function of the probability density $\frac{m}{H_\epsilon}\frac{y^{m-1}}{y/t+\epsilon}$ on $[0,1]$. Relative to the probability density $my^{m-1}$, this density has a decreasing weight; relative to $(m-1)y^{m-2}$, its weight is proportional to $y/(y+t\epsilon)$ and hence increasing. If one probability density on $[0,1]$ has a decreasing weight relative to another, its average weight on $[0,x]$ is at least one and its distribution function is the larger of the two; an increasing weight reverses the inequality. Consequently
\[
 x^m\leq q_\epsilon(x)^m\leq x^{m-1},
 \qquad\text{that is,}\qquad x\leq q_\epsilon(x)\leq x^t.
\]
The function
\[
 \varphi(x)=\int_0^x\frac{y^t-y}{y(1-y)}\,\mathrm{d}y
\]
is bounded and continuous on $[0,1]$, since $t>0$, and smooth on $(0,1]$; its derivative extends smoothly at one. The integrable function $(y^t-y)/[y(1-y)]$ dominates the derivatives of the functions $\varphi_\epsilon$, so dominated convergence gives uniform convergence $\varphi_\epsilon\to\varphi$ on $B$. Distributional convergence shows that $A$ is a closed positive current. On each coordinate chart, a smooth local potential of $\omega$ plus $\varphi$ is a uniform limit of the corresponding plurisubharmonic functions built with $\varphi_\epsilon$, including at $p$. Hence $\varphi$ is $\omega$-plurisubharmonic. Off $p$, the limit $q=x^t$ gives
\[
 \frac{A^m}{\omega^m}
 =\frac{(x^t)^{m-1}t x^{t-1}}{x^{m-1}}=\frac t x=\frac1a.
\]
Smoothness of $\varphi$ off $p$ and the same determinant argument at the hyperplane $\{Z_0=0\}$ prove \eqref{eq:radial-volume-endpoint-density}.
\end{proof}

\Needspace{14\baselineskip}
\begin{theorem}\label{thm:radial-positive-volume-nonbig}\index{Gauduchon variational volume!positive nonbig background}
The background $\theta$ on $X$ is smooth, semipositive, nef and nonclosed. It is not big, but
\begin{equation}\label{eq:radial-positive-volume-nonbig}
 \lambda_\mu(\theta)=n^{1/n},\qquad\mathcal V_\mu(\theta)=n.
\end{equation}
For $\theta_\epsilon=\omega+(a+\epsilon)w$, one has
\[
 \mathcal V_\mu(\theta_\epsilon)=\frac n{H_\epsilon},
\]
and the smooth positive metrics
\begin{equation}\label{eq:radial-volume-minimizing-metrics}
 \gamma_\epsilon=(a+\epsilon)^{-1/m}
                 \bigl(A_\epsilon+(a+\epsilon)w\bigr)
\end{equation}
are balanced and minimize the defining quotient at $\theta_\epsilon$.
\end{theorem}
\begin{proof}
The coefficient $a$ is nonnegative, and $\theta+\eta h>0$ for every $\eta>0$; this proves semipositivity and nefness. Since $a$ is nonconstant, $\mathrm{d}\theta=\mathrm{d}a\wedge w\ne0$.

Suppose that $\theta+\ddc v\geq\delta h$ for a quasi-plurisubharmonic function $v$ and some $\delta>0$. Choose a nonzero smooth function $f\geq0$ on $B$ supported in $\{a<\delta\}$. Its pullback $S=f\omega^m$ is a smooth semipositive $(m,m)$-form, closed because it has top degree on the base. Positivity and distributional Stokes would give
\[
 0\leq\int_X(\theta+\ddc v-\delta h)\wedge S
   =\int_B f(a-\delta)\omega^m<0.
\]
This contradiction shows that $\theta$ is not big, since every Hermitian form on $X$ dominates a positive multiple of $h$.

For the lower bound on the volume, pull back the bounded potential $\varphi$ of \cref{lem:radial-volume-representatives}. The positive current $\Omega=A+a w=\theta+\ddc\varphi$ is a smooth strictly positive form off $Z=\{p\}\times\mathbb P^1$, where
\[
 \Omega^n=n a A^m\wedge w=n\mu.
\]
Let $\gamma$ be a Gauduchon metric. Since $\varphi$ is bounded, distributional Stokes lets us replace $\theta$ by $\Omega$ in the numerator of its quotient. The set $Z$ has zero smooth volume and $\Omega\wedge\gamma^{n-1}$ is a positive measure, so the pointwise arithmetic--geometric mean inequality off $Z$ gives
\[
 \int_X\theta\wedge\gamma^{n-1}
 \geq n^{1/n}\int_X
            (\mu/\gamma^n)^{1/n}\gamma^n
 =n^{1/n}D_\mu(\gamma).
\]
This lower bound holds for every test in \cref{def:gaud-variational-volume}; no power of the current $\Omega$ along $Z$ is needed.

For the upper bound, put $c_\epsilon=n/H_\epsilon$ and $\Omega_\epsilon=A_\epsilon+(a+\epsilon)w=\theta_\epsilon+\ddc\varphi_\epsilon$. Then $\Omega_\epsilon^n=c_\epsilon\mu$. The metrics in \eqref{eq:radial-volume-minimizing-metrics} satisfy
\[
 T_\epsilon=\gamma_\epsilon^m
 =(a+\epsilon)^{-1}A_\epsilon^m
       +m A_\epsilon^{m-1}\wedge w.
\]
The first term has top degree on the base and the second is a product of closed forms, so $T_\epsilon$ is closed; that is, $\gamma_\epsilon$ is balanced, and in particular Gauduchon. Smooth Stokes and \eqref{eq:radial-volume-integration} give
\[
 \int_X\theta_\epsilon\wedge T_\epsilon
 =c_\epsilon\int_X(a+\epsilon)^{-1}\mu=n,
 \qquad
 D_\mu(\gamma_\epsilon)=c_\epsilon^{m/n}H_\epsilon,
\]
so the quotient of $\gamma_\epsilon$ at $\theta_\epsilon$ equals $c_\epsilon^{1/n}$. The same arithmetic--geometric mean argument, applied to the smooth representative $\Omega_\epsilon$, bounds every Gauduchon quotient at $\theta_\epsilon$ below by $c_\epsilon^{1/n}$. This proves that $\gamma_\epsilon$ minimizes, and gives the formula for $\mathcal V_\mu(\theta_\epsilon)$. Since $\theta\leq\theta_\epsilon$, the metrics $\gamma_\epsilon$, used as tests for $\theta$, also give $\lambda_\mu(\theta)\leq c_\epsilon^{1/n}$. Letting $\epsilon\downarrow0$ proves \eqref{eq:radial-positive-volume-nonbig}. By \cref{thm:gaud-volume-nef-limit}, this value is also the limit of the volumes of the Hermitian perturbations $\theta+\epsilon h$.
\end{proof}

The value $n$ refers to the probability measure $\mu$ fixed above, but positivity holds for every smooth positive probability measure by \cref{prop:gaud-volume-density-comparison}. Thus positive volume does not characterize bigness for nonclosed nef backgrounds, even on a projective manifold. The construction needs $m\geq2$, so that $t>0$ and the endpoint potential is bounded; it says nothing about surfaces, or about closed nef classes on general compact complex manifolds.

\input{author/section_radial_gauduchon_test_limits}



# Known companion evidence, not a trusted proof premise: section_radial_gauduchon_test_limits.tex

\Needspace{12\baselineskip}
\subsection{Volume tests and threshold tests}
\label{sec:radial-gauduchon-test-limits}

Two quotients are formed from the same pairing $\int_X\theta\wedge\gamma^{n-1}$. The volume quotient divides it by the determinant integral $D_\mu(\gamma)$, whereas the linear threshold $\kappa_h(\theta)$ of \cref{cor:gauduchon-threshold} divides it by the trace $\int_Xh\wedge\gamma^{n-1}$. This threshold is positive exactly when $\theta$ is big, and we call it the bigness threshold; for the pseudoeffective but nonbig background $\theta$ of \cref{thm:radial-positive-volume-nonbig} it vanishes. The same metrics can approach both infima, but need not do so. In the radial model, the volume-minimizing metrics approach the bigness threshold only in dimension three, while a second family of smooth balanced metrics approaches it in every dimension by concentrating on the fiber over $p$.

Keep the data of \cref{thm:radial-positive-volume-nonbig}, and put
\[
 T_\epsilon=\gamma_\epsilon^m,\qquad
 I_\epsilon=\int_B(a+\epsilon)^{-2}\omega^m,
 \qquad M_\epsilon=m+I_\epsilon/H_\epsilon,
 \qquad g_\epsilon=M_\epsilon^{-1/m}\gamma_\epsilon.
\]
Write $Z=\{p\}\times\mathbb P^1$. Its integration current $[Z]$ satisfies $\int_Zh=1$ and annihilates $\theta$, since $\theta|_Z=a(p)w=0$.

\Needspace{18\baselineskip}
\begin{proposition}\label{prop:radial-volume-test-limits}\index{Gauduchon variational volume!normalized radial tests}
The metrics $g_\epsilon$ are balanced, satisfy $\int_Xh\wedge g_\epsilon^m=1$, and
\begin{equation}\label{eq:radial-test-pairings}
 \int_X\theta\wedge g_\epsilon^m
   =\frac{n-\epsilon I_\epsilon/H_\epsilon}{M_\epsilon},
 \qquad D_\mu(g_\epsilon)
   =\frac{(n/H_\epsilon)^{m/n}H_\epsilon}{M_\epsilon}.
\end{equation}
Their volume quotients tend to $n^{1/n}$ as $\epsilon\downarrow0$. If $n=3$, then $g_\epsilon^2$ converges weakly to $[Z]$, and
\begin{equation}\label{eq:radial-threefold-test-collapse}
 \int_X\theta\wedge g_\epsilon^2
       \sim\frac6{\log(1/\epsilon)},
 \qquad D_\mu(g_\epsilon)
       \sim\frac{2\,3^{2/3}}{\log(1/\epsilon)}.
\end{equation}
If $n\geq4$, put $M_0=m+(m-1)^2/[m(m-2)]$. Then
\[
 \int_X\theta\wedge g_\epsilon^m\longrightarrow\frac n{M_0}>0,
 \qquad D_\mu(g_\epsilon)\longrightarrow\frac{n^{m/n}}{M_0}>0.
\]
Thus this family approaches the bigness threshold, which is zero, exactly when $n=3$.
\end{proposition}
\begin{proof}
By the power formula in the proof of \cref{thm:radial-positive-volume-nonbig} and \eqref{eq:radial-volume-smooth-density},
\[
 T_\epsilon=\frac{\omega^m}{H_\epsilon(a+\epsilon)^2}
               +mA_\epsilon^{m-1}\wedge w.
\]
Since $A_\epsilon$ is cohomologous to $\omega$, closed Stokes gives
$\int_B\omega\wedge A_\epsilon^{m-1}=1$. Consequently the two terms have $h$-traces $I_\epsilon/H_\epsilon$ and $m$, which proves the trace normalization of $g_\epsilon^m=T_\epsilon/M_\epsilon$. Subtracting $\epsilon w$ from $\theta_\epsilon$ subtracts $\epsilon I_\epsilon/H_\epsilon$ from the pairing $\int_X\theta_\epsilon\wedge T_\epsilon=n$. Rescaling $\gamma_\epsilon$ by $M_\epsilon^{-1/m}$ divides both the linear pairing and $D_\mu$ by $M_\epsilon$, proving \eqref{eq:radial-test-pairings}.

Polar integration gives
\[
 I_\epsilon=m t^2\int_0^1
              \frac{x^{m-1}}{(x+t\epsilon)^2}\,\mathrm{d}x.
\]
When $m=2$, put $q=\epsilon/2$. Direct integration yields
\[
 I_\epsilon=\tfrac12\left(\log\frac{1+q}{q}
                      +\frac q{1+q}-1\right),
 \qquad H_\epsilon=1-q\log\frac{1+q}{q}.
\]
Hence $I_\epsilon\sim\tfrac12\log(1/\epsilon)$ and $\epsilon I_\epsilon\to0$. Since $H_\epsilon\to1$, the asymptotics in \eqref{eq:radial-threefold-test-collapse} follow from \eqref{eq:radial-test-pairings}.

For the weak limit when $n=3$, note that the mixed positive term $2A_\epsilon\wedge w$ has $h$-trace two; divided by $M_\epsilon\to\infty$, it tends weakly to zero. The horizontal probability measure
\[
 I_\epsilon^{-1}(a+\epsilon)^{-2}\omega^2
\]
on $B$ concentrates at $p$: outside any fixed neighborhood of $p$ its unnormalized density stays bounded, while $I_\epsilon\to\infty$. For a smooth $(1,1)$-test form on $X$, integration along the fibers $\{b\}\times\mathbb P^1$ gives a smooth function on $B$. The convergence of these probability measures to the Dirac mass at $p$ therefore shows that the horizontal term of $g_\epsilon^2$ converges to $[Z]$, because its coefficient $I_\epsilon/(H_\epsilon M_\epsilon)$ tends to one.

For $m\geq3$, monotone convergence instead gives
\[
 I_\epsilon\longrightarrow m t^2\int_0^1x^{m-3}\,\mathrm{d}x
                =\frac{(m-1)^2}{m(m-2)}.
\]
In both cases $\epsilon I_\epsilon\to0$. Using $H_\epsilon\to1$ in \eqref{eq:radial-test-pairings} proves the remaining limits, including that of the volume quotients.
\end{proof}

For $n\geq4$ the metrics $g_\epsilon$ still minimize the perturbed volumes, and their quotients converge to $\lambda_\mu(\theta)$, but their normalized pairings with $\theta$ stay bounded away from zero. This does not contradict nonbigness: the bigness threshold is approached by a different family.

\Needspace{16\baselineskip}
\begin{proposition}\label{prop:radial-localized-balanced-tests}\index{Gauduchon variational volume!localized balanced tests}
For every $n\geq3$ there are smooth balanced metrics $b_\rho$, $0<\rho<1$, with
\[
 \int_Xh\wedge b_\rho^m=1,\qquad
 b_\rho^m\rightharpoonup[Z],\qquad
 \int_X\theta\wedge b_\rho^m\longrightarrow0,
 \qquad D_\mu(b_\rho)\longrightarrow0
\]
as $\rho\downarrow0$.
\end{proposition}
\begin{proof}
Choose a nonzero smooth function $f_\rho\geq0$ on $B$, supported in $\{x<\rho\}$ and normalized by $\int_Bf_\rho\omega^m=1$. The form
\begin{equation}\label{eq:radial-localized-test-form}
 \Gamma_\rho=\frac{f_\rho\omega^m+\rho h^m}{1+n\rho}
\end{equation}
is smooth, strictly positive and closed: the first summand has top degree on the base, and $h$ is K\"ahler. The positive-root construction in the proof of \cref{thm:lamari} gives a unique smooth metric $b_\rho$ with $b_\rho^m=\Gamma_\rho$, and $b_\rho$ is balanced because $\Gamma_\rho$ is closed. Since $\int_Xh^{m+1}=n$, its $h$-trace is one.

Put $C_\theta=\int_X\theta\wedge h^m$. Since $a<\rho/t$ on the support of $f_\rho$,
\[
 0\leq\int_X\theta\wedge\Gamma_\rho
 \leq\frac{\rho/t+\rho C_\theta}{1+n\rho}\longrightarrow0.
\]
The lower bound in the proof of \cref{thm:radial-positive-volume-nonbig} gives
$D_\mu(b_\rho)\leq n^{-1/n}\int_X\theta\wedge\Gamma_\rho$, so the determinant integrals also tend to zero. The probability measures $f_\rho\omega^m$ converge to the Dirac mass at $p$ because their supports shrink to that point. Fiber integration, as in the preceding proof, gives the current limit $[Z]$, while the term $\rho h^m$ tends to zero.
\end{proof}

Thus the normalized current $[Z]$ is a weak limit of smooth balanced metrics normalized by their $h$-traces. It annihilates $\theta$, and its determinant-weighted measure vanishes by \cref{prop:nef-annihilator-determinant}. The two families give explicit instances of the separation between the volume and threshold denominators described in \cref{prop:gaud-positive-volume-collapse}, without any general smoothing result for Gauduchon currents.



# Known companion evidence, not a trusted proof premise: section_gauduchon_volume_variation.tex

\Needspace{11\baselineskip}
\section{Normalization for the Gauduchon equation}

By \cref{thm:stw-volume}, every smooth real function $F$ determines a scalar $b_\gamma(F)$, the constant $b$ of that theorem. As for the Monge--Amp\`ere equation, its variation is governed by the adjoint probability measure $\mu_u^\gamma$ of \cref{prop:gaud-volume-linearization} and by the concavity of the logarithmic determinant. To differentiate solutions, we fix a smooth positive volume form $\mathrm{d}V_0$ and use the normalization $\int_Xu\,\mathrm{d}V_0=0$ in place of $\sup_Xu=0$.

\begin{lemma}\label{lem:gaud-volume-smooth-dependence}
The solution $(u,b_\gamma(F))$, normalized by $\int_Xu\,\mathrm{d}V_0=0$, depends smoothly on the parameters of every smooth finite-dimensional family of functions $F$.
\end{lemma}
\begin{proof}
The map $\Gamma\mapsto\eta$ with $\eta^{n-1}=\Gamma$ is smooth on positive forms, since in a frame it is the inverse of the smooth map $\eta\mapsto\eta^{n-1}$, whose differential is invertible. The openness argument in the proof of \cref{thm:stw-volume}, with the $\mathrm{d}V_0$-mean in place of the $\gamma^n$-mean, gives a bounded inverse for the derivative with respect to the potential and the scalar between the relevant H\"older spaces. The implicit function theorem gives local smooth solution maps, and uniqueness shows that they agree on overlaps. Applying this for every order of H\"older regularity gives the assertion for smooth data.
\end{proof}

\Needspace{7\baselineskip}
For a smooth family of prescribed functions $F_t\in C^\infty(X,\mathbb R)$, with $t$ in an open interval of $\mathbb R$, let $u_t$ be the corresponding solutions with $\int_Xu_t\,\mathrm{d}V_0=0$, and set $Q_t=Q_{u_t}$ as in \eqref{eq:stw-cofactor-matrix-scaling}. The expression
\[
 \operatorname{tr}\bigl((Q_t^{-1}\dot Q_t)^2\bigr)
\]
is independent of the chosen frame and nonnegative, because $Q_t^{-1}\dot Q_t$ is similar to the Hermitian matrix $Q_t^{-1/2}\dot Q_t Q_t^{-1/2}$.

\Needspace{18\baselineskip}
\begin{theorem}\label{thm:gaud-volume-normalization-derivatives}
For a smooth family $F_t$ and its solutions,
\begin{align*}
 \dot b_\gamma(F_t)&=-\int_X\dot F_t\,\mathrm{d}\mu_{u_t}^\gamma,\\
 \ddot b_\gamma(F_t)&=-\int_X\ddot F_t\,\mathrm{d}\mu_{u_t}^\gamma
 -\frac1{n-1}\int_X
        \operatorname{tr}\bigl((Q_t^{-1}\dot Q_t)^2\bigr)
                          \,\mathrm{d}\mu_{u_t}^\gamma.
\end{align*}
In particular, $b_\gamma$ is concave, and along $F_t=F_0+tG$ its second derivative is strictly negative unless $G$ is constant. Moreover, for smooth real functions $F,G$ on $X$ and every real constant $a$,
\[
 b_\gamma(F+a)=b_\gamma(F)-a,
 \qquad |b_\gamma(G)-b_\gamma(F)|\leq\|G-F\|_\infty.
\]
\end{theorem}
\begin{proof}
By \eqref{eq:stw-cofactor-matrix-scaling},
\[
 \mathcal G(u)=\frac1{n-1}\log\det_\gamma Q_u.
\]
Differentiating $\mathcal G(u_t)=F_t+b_\gamma(F_t)$ once gives $\mathcal L_{u_t}\dot u_t=\dot F_t+\dot b_\gamma(F_t)$, and integration against the adjoint probability measure gives the first formula.

Because $\Gamma_u$ is affine in $u$, its second derivative along the family is $\mathcal D_\gamma\ddot u_t$. The formula for the second derivative of $\log\det$ used in the proof of \cref{thm:b-derivatives} therefore gives
\[
 \mathcal L_{u_t}\ddot u_t
 -\frac1{n-1}\operatorname{tr}\bigl((Q_t^{-1}\dot Q_t)^2\bigr)
 =\ddot F_t+\ddot b_\gamma(F_t).
\]
Integrating against $\mu_{u_t}^\gamma$ at this fixed parameter gives the second formula; no derivative of the measure is needed.

For affine $F_t$, we have $\ddot F_t=0$, and positivity of the density of $\mu_{u_t}^\gamma$ proves concavity. If the second derivative vanishes, then $\dot Q_t=0$, so $\dot\Gamma_{u_t}=0$ and $\mathcal L_{u_t}\dot u_t=0$. By \cref{prop:gaud-volume-linearization}, $\dot u_t$ is constant, and the first differentiated equation forces $G$ to be constant. Conversely, adding a constant to $F$ changes only $b$, by the opposite constant. Finally, integrate the first derivative along the segment from $F$ to $G$: since $\mu_{u_t}^\gamma$ is a probability measure, the derivative lies between $-\sup_X(G-F)$ and $-\inf_X(G-F)$, which proves the Lipschitz bound.
\end{proof}

\Needspace{6\baselineskip}
The Lipschitz bound extends $b_\gamma$ uniquely to continuous functions $F$. Constructing corresponding weak solutions would require, in addition, a volume measure for the $(n-1)$st roots of singular forms in the Aeppli ansatz, compactness of their potentials, and stability of the adjoint equation.

\Needspace{13\baselineskip}
On a surface with Gauduchon background form $\gamma_0$, conservation of the total mass makes the scalar and the adjoint probability measure explicit.

\Needspace{9\baselineskip}
\begin{example}\label{ex:gaud-volume-surface}
If $n=2$ and $\gamma_0$ is Gauduchon, then $\Gamma_u=\gamma_0+\ddc u=\eta_u$, and $\eta_u$ is also Gauduchon. The mass identity of \cref{thm:mass-invariance-characterization} gives $\int_X\eta_u^2=\int_X\gamma_0^2$. Therefore
\[
 b_\gamma(F)=\log\int_X\gamma_0^2-
                   \log\int_X\mathrm{e}^F\gamma^2,
 \qquad
 \mathrm{d}\mu_u^\gamma=\frac{\mathrm{e}^F\gamma^2}{\int_X\mathrm{e}^F\gamma^2}.
\]
The adjoint equation of \cref{prop:gaud-volume-form-adjoint} gives the same measure, because $\ddc\eta_u=0$ and hence $\rho_u$ is constant. Along $F+tG$, the second derivative of $b_\gamma$ is minus the variance of $G$ with respect to this probability measure.
\end{example}



# Exact separately assessed primary applications

{
  "recorded_at_utc": "2026-10-07T22:41:25.280252+00:00",
  "scope": "P14 restricted warped endpoints A-E",
  "sources": [
    {
      "name": "Tosatti-Weinkove-0910.1390v2",
      "pdf_sha256": "ec91e6da8d65df639ecd8c972a299947001edddfc30a857b927c056f901cdcd5",
      "text_sha256": "f174af579b24afd6afc474735707c2ba3087c1de54b3757aaecb4247a69df2c2",
      "exact_application": "Closed smooth positive-data existence on B only; target mass W makes its scaling constant zero by closed Stokes; potentials rescale2pi. No endpoint PDE or uniform endpoint estimate imported.",
      "actual_root_read_ranges": "Current root re-read1-110; entire printed proof3-8 separately root-read earlier.",
      "source_statement_and_hypotheses_assessed": true,
      "standard_foundations_imported_not_recursively_certified": true
    },
    {
      "name": "Demailly-Paun-nef-positive-0105176-P14-final",
      "pdf_sha256": "258142c71b3bb77dcc5dec480ac2bd2bd679e60b4629bf03c9ea1d2be556ed2d",
      "text_sha256": "d7c7acecb1995055d27fa4297afc68939882142f9dd5ba65ff11ea2129f75c3b",
      "exact_application": "Compact Kahler X=B x C; any smooth real closed chi of nef class with positive top mass contains a closed Kahler current. Global genuine quasi-psh potential follows from the established current ddbar lemma on Kahler X; normalization2pi. Adding arbitrary smooth semipositive beta and undoing a smooth gauge forces bigness, contradicting the full-potential smooth-test exclusion.",
      "actual_root_read_ranges": "Current whole622-685 theorem and printed proof, plus580-621 proof boundary; whole1-130 earlier current context.",
      "source_statement_and_hypotheses_assessed": true,
      "standard_foundations_imported_not_recursively_certified": true
    },
    {
      "name": "Tosatti-nef-Morse-2608.30153v2-P14-final",
      "pdf_sha256": "a40feb12fb2b0219a0857f4f9b81e2f6acea43c08ef7e461d00a9d4020d03fe0",
      "text_sha256": "22333d0abe50acb08e5c7e0d349702cb39e76d8dd768572f26a05e48ae7a4867",
      "exact_application": "Only usual closed cohomological volume and closed nef real classes on compact Kahler X. Constant a0 gives P=alpha+(a0+t)w,Q=tw, binomial RHS=nWa0=the exact fixed-density volume. Nonconstant a is not a closed-class application. No new general Morse theorem or general identification of nonclosed root volume with cohomological volume.",
      "actual_root_read_ranges": "Whole1-200 introduction separately root-read; current entire200-410 nullset-current and Hahn--Banach proofs; whole411-620 main proof.",
      "source_statement_and_hypotheses_assessed": true,
      "standard_foundations_imported_not_recursively_certified": true
    },
    {
      "name": "Demailly-agbook-Harvard",
      "pdf_sha256": "d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1",
      "text_sha256": "894bffdb8514fbe484b38090c3fcb1951cad78c0587c1516a8e09ab2b560d8de",
      "exact_application": "Compact Kahler smooth ddbar lemma VI8.6 and Cor8.7, and its established distributional-current extension, for the global potential of the DP current only. Standard Hodge and elliptic foundations remain imported. Other full-review premises concerning weighted PL and Poincare duality belong to broader historical private comparisons excluded from A-E release scope.",
      "actual_root_read_ranges": "Current whole17220-17470 covers exactlemma8.6/Cor8.7 printedproof and surrounding Hodge passages.",
      "source_statement_and_hypotheses_assessed": true,
      "standard_foundations_imported_not_recursively_certified": true
    }
  ],
  "new_statement_only_input_sha256": "4be93a757df69d7b346ad8e74b080d3f4c1e0a18235ccd32ebb94e2b5910658b",
  "no_original_proofs_or_verdicts_in_cold_input": true,
  "known_companion_mathematics_credited": true,
  "original_P14_completed": false,
  "mathematical_acceptance": false,
  "published": false
}



# Primary evidence, exact application judged separately: Tosatti-Weinkove-0910.1390v2


## Source lines 1-110

                                                               The complex Monge-Ampère equation
                                                                 on compact Hermitian manifolds1


                                                                 Valentino Tosatti and Ben Weinkove
arXiv:0910.1390v2 [math.DG] 11 Nov 2009




                                                                                   Abstract
                                                   We show that, up to scaling, the complex Monge-Ampère equation on compact
                                                Hermitian manifolds always admits a smooth solution.




                                          1   Introduction

                                          Let (M, g) be a compact Hermitian manifold of complex dimension n ≥ 2 and write ω
                                          for the corresponding real (1, 1) form
                                                                               √ X
                                                                          ω = −1   gij dz i ∧ dz j .
                                                                                     i,j

                                          For a smooth real-valued function F on M , consider the complex Monge-Ampère equa-
                                          tion
                                                                          √
                                                                     (ω + −1∂∂ϕ)n = eF ω n , with
                                                                          √                                              (1.1)
                                                                     ω + −1∂∂ϕ > 0, sup ϕ = 0,
                                                                                              M

                                          for a real-valued function ϕ.
                                              Our main result is as follows.

                                          Main Theorem Let ϕ be a smooth solution of the complex Monge-Ampère equation
                                          (1.1). Then there are uniform C ∞ a priori estimates on ϕ depending only on (M, ω)
                                          and F .

                                              A corollary of this is that we can solve (1.1) uniquely after adding a constant to F ,
                                          or equivalently, up to scaling the volume form eF ω n .

                                          Corollary 1. For every smooth real-valued function F on M there exists a unique
                                          real number b and a unique smooth real-valued function ϕ on M solving
                                                                        √
                                                                   (ω + −1∂∂ϕ)n = eF +b ω n , with
                                                                       √                                            (1.2)
                                                                   ω + −1∂∂ϕ > 0, sup ϕ = 0.
                                                                                              M


                                            1
                                              Research supported in part by National Science Foundation grant DMS-08-48193. The second-
                                          named author is also supported in part by a Sloan Foundation fellowship.


                                                                                       1

   In the case of ω Kähler, that is when dω = 0, this result is precisely the celebrated
Calabi Conjecture [Ca] proved by Yau [Ya]. We note here that if ω satisfies

                                ∂∂ω k = 0,    for k = 1, 2,                           (1.3)

(in particular if ω is closed) then the constant b must equal

                                               ωn
                                            R
                                       log R M F n .
                                            Me ω

     We mention now some special cases where the results of the Main Theorem and
Corollary are already known. Cherrier [Ch] gave a proof when the complex dimension
is two or if ω is balanced, that is, d(ω n−1 ) = 0 (an alternative proof was very recently
given in [TW]). In addition, Cherrier [Ch] dealt with the case of conformally Kähler
and considered a technical assumption which is slightly weaker than balanced, see also
the related work of Hanani [Ha]. Guan-Li [GL] gave a proof under the assumption (1.3).
For further background we refer the reader to [TW] and the references therein.
     As the reader will see in the proof below, we note that the key L∞ bound of ϕ in
the Main Theorem follows from combining a lemma of [Ch] with some recent estimates
of the authors [TW].
     Finally, we remark that one can give a geometric interpretation of (1.2) in terms of
the first Chern class c1 (M ) of M . We denote by Ric(ω) the first Chern form of the Chern
connection of ω, which is a closed form cohomologous to c1 (M ). We then consider    √ the
                           1,1
real Bott-Chern space HBC      (X, R) of closed real (1, 1) forms modulo the image of −1∂∂
acting on real functions. It has a natural surjection to the familiar space H 1,1 (M, R),
which is an isomorphism if and only if b1 (M ) = 2h0,1 [G2] (in particular if M is Kähler).
                                                          1,1
The form Ric(ω) determines a class cBC      1 (M ) in HBC (M, R) which maps to the usual
first Chern class c1 (M ) via the above surjection. Then from our main theorem we get
the following Hermitian version of the Calabi conjecture (see also a related question of
Gauduchon [G2, IV.5]):

Corollary 2. Every representative of the first Bott-Chern class cBC1 (M
                                                                      √) can be rep-
resented as the first Chern form of a Hermitian metric of the form ω + −1∂∂ϕ.

   To see why this holds, just notice that (1.2) holds for some constant b if and only if
                                                       √
                               √                         −1
                      Ric(ω + −1∂∂ϕ) = Ric(ω) −              ∂∂F,                  (1.4)
                                                        2π
and
√
     that by definition every form representing cBC 1 (M ) can be written as Ric(ω) −
  −1
 2π ∂∂F for some function F . We note here that in the case n = 2 [TW, Corollary 2]
gives a criterion to decide which representatives of c1 (M ) can be written in this form.



# Primary evidence, exact application judged separately: Demailly-Paun-nef-positive-0105176-P14-final


## Source lines 1-130

arXiv:math/0105176v2 [math.AG] 24 Sep 2001




                                                            Numerical characterization of the
                                                   Kähler cone of a compact Kähler manifold

                                                                  Jean-Pierre Demailly∗ and Mihai Paun∗∗

                                                                        ∗
                                                                            Université Joseph Fourier, Grenoble
                                                                       ∗∗
                                                                            Université Louis Pasteur, Strasbourg




                                             Abstract. The goal of this work is give a precise numerical description of the Kähler cone
                                             of a compact Kähler manifold. Our main result states that the Kähler cone depends only on
                                             the intersection form of the cohomology ring, the Hodge structure and the homology classes
                                             of analytic cycles: if X is a compact Kähler manifold, the Kähler cone K of X is one of the
                                             connected components of the set P of real (1, 1) cohomology classes {α} which are numerically
                                                                              R
                                             positive on analytic cycles, i.e.    αp > 0 for every irreducible analytic set Y in X, p = dim Y .
                                                                                Y
                                             This result is new even in the case of projective manifolds, where it can be seen as a generalization
                                             of the well-known Nakai-Moishezon criterion, and it also extends previous results by Campana-
                                             Peternell and Eyssidieux. The principal technical step is to show that every nef class {α} which
                                                                                             R
                                             has positive highest self-intersection number       αn > 0 contains a Kähler current; this is done by
                                                                                             X
                                             using the Calabi-Yau theorem and a mass concentration technique for Monge-Ampère equations.
                                             The main result admits a number of variants and corollaries, including a description of the cone
                                             of numerically effective (1, 1) classes and their dual cone. Another important consequence is the
                                             fact that for an arbitrary deformation X → S of compact Kähler manifolds, the Kähler cone
                                             of a very general fibre Xt is “independent” of t, i.e. invariant by parallel transport under the
                                             (1, 1)-component of the Gauss-Manin connection.




                                             0. Introduction

                                             The primary goal of this work is to study in great detail the structure of the Kähler
                                             cone of a compact Kähler manifold. Our main result states that the Kähler cone
                                             depends only on the intersection form of the cohomology ring, the Hodge structure
                                             and the homology classes of analytic cycles. More precisely, we have

                                                                                                 1

0.1. Main Theorem. Let X be a compact Kähler manifold. Then the Kähler
cone K of X is one of the connected components of the set P of real (1, 1)R cohomol-
ogy classes {α} which are numerically positive on analytic cycles, i.e. Y αp > 0
for every irreducible analytic set Y in X, p = dim Y .

    This result is new even in the case of projective manifolds. It can be seen
as a generalization of the well-known Nakai-Moishezon criterion, which provides
a necessary and sufficient criterion for a line bundle to be ample:Za line bundle
L → X on a projective algebraic manifold X is ample if and only if              c1 (L)p > 0,
                                                                            Y
for every algebraic Rsubset Y ⊂ X, p = dim Y . When X is projective, we show
that the condition Y αp > 0 characterizes precisely all Kähler classes, even when
{α} is not an integral class – and even when {α} lies outside the real Neron-Severi
group N SR (X) = N S(X) ⊗Z R. In the notation of the Main Theorem, we have
therefore K = P if X is projective.
     This result extends a few special cases which had been proved earlier by
completely different methods: Campana-Peternell [CP90] showed that the Nakai-
Moishezon criterion holds true for classes {α} ∈ N SR (X). Quite recently, using
L2 cohomology techniques for infinite coverings of a projective algebraic mani-
fold, P. Eyssidieux [Eys00] obtained a version of the Nakai-Moishezon for all real
combinations of (1, 1) cohomology classes which become integral after taking the
pull-back to some finite or infinite covering.
     The Main Theorem admits quite a number of useful variants and corollaries.
Two of them are descriptions of the cone of numerically effective (nef) classes –
see section 1 for the precise definition of numerical effectivity on general compact
complex manifolds.

 0.2. Corollary. Let X be a compact Kähler manifold. A (1, 1) cohomology
Rclassk{α}p−k
           on X is nef if and only if there exists a Kähler metric ω on X such that
  Y
    α  ∧ω     ≥ 0 for all irreducible analytic sets Y and all k = 1, 2, . . . , p = dim Y .

0.3. Corollary. Let X be a compact Kähler manifold. A (1, 1) cohomology class
{α} on X is nef if and only for every irreducible
                                             R      analytic set Y in X, p = dim X
and every Kähler metric ω on X we have Y α ∧ ω p−1 ≥ 0. In other words, the
dual of the nef cone is the closed convex cone generated by cohomology classes of
currents of the form [Y ] ∧ ω p−1 in H n−1,n−1 (X, R).

We now briefly discuss the essential ideas involved in our approach. The first basic
result is a sufficient condition for a nef class to contain a Kähler current. The proof
is based on a technique of mass concentration for Monge-Ampère equations, using
the Aubin-Calabi-Yau theorem [Yau78].

0.4. Theorem. Let (X, ω) be a compact n-dimensional Kähler   R      manifold and let
          1,1                                                     n
{α} in H (X, R) be a nef cohomology class such that X α > 0. Then {α}
contains a Kähler current T , that is, a closed positive current T such that T ≥ δω
for some δ > 0. The current T can be chosen smooth in the complement X r Z
of an analytic set, with logarithmic poles along Z.

                                            2

     In a first step, we show that the class {α}p dominates a small multiple of
any p-codimensional analytic set Y in X. As we already mentioned, this is done
by concentrating the mass on Y in the Monge-Ampère equation. We then apply
this fact to the diagonal ∆ ⊂ X e = X × X to produce a closed positive current
Θ ∈ {π1∗ α + π2∗ α}n which dominates [∆] in X × X. The desired Kähler current T
is easily obtained by taking a push-forward π1∗ (Θ ∧ π2∗ ω) of Θ to X.
    The technique produces a priori “very singular” currents, since we use a weak
compactness argument. However, we can apply the general regularization theorem
proved in [Dem92] to get a current which is smooth outside an analytic set Z
and only has logarithmic poles along Z. The idea of using a Monge-Ampère
equation to force the occurrence of positive Lelong numbers in the limit current
was first exploited in [Dem93], in the case when Y is a finite set of points, to
get effective results for adjoints of ample line bundles (e.g. in the direction of the
Fujita conjecture).
     The use of higher dimensional subsets Y in the mass concentration process
will be crucial here. However, the technical details are quite different from the
0-dimensional case used in [Dem93]; in fact, we cannot rely any longer on the
maximum principle, as in the case of Monge-Ampère equations with isolated Dirac
masses in the right hand side. The new technique employed here is essentially taken
from [Pau00]; it was already proved there – for projective manifolds – that any big
semi-positive (1, 1)-class contains a Kähler current. The Main Theorem is deduced
from 0.4 by induction on dimension, thanks to the following useful result which
was already observed in the second author’s Thesis ([Pau98a, Pau98b]).

0.5. Proposition. Let X be a compact complex manifold (or complex space).


## Source lines 580-685

                                           1
(2.9′′ )                     αn−p
                              ε   ∧ ωεp ≥ λp+1 . . . λn ωεn ,
                                          n!
The last inequality (2.9′′ ) implies
      Z                         Z               Z
                         n
          λp+1 . . . λn ωε ≤ n!     αε ∧ ωε = n! (α + εω)n−p ∧ ω p ≤ M
                                     n−p  p
           X                      X                      X

for some constant M > 0 (we assume ε ≤ 1, say). In particular, for everyR δ > 0, the
subset Eδ ⊂ X of points z such that λp+1 (z) . . . λn (z) > M/δ satisfies Eδ ωεn ≤ δ,
hence
                    Z                      Z
                          p     n−p    n−p
(2.10)                   ωε ∧ ω     ≤2             ωεn ≤ 2n−p δ.
                        Eδ                         Eδ

The combination of (2.8) and (2.10) yields
                    Z
                               ωεp ∧ ω n−p ≥ δp (U ) − 2n−p δ.
                       (U∩Vε )rEδ


                                            11

On the other hand (2.7′ ) and (2.9′ ) imply
                          Cε               Cε p
               αpε ≥                 ωεp ≥    ω         on (U ∩ Vε ) r Eδ .
                       λp+1 . . . λn       M/δ ε
From this we infer
       Z                      Z
               p    n−p   Cε                           Cε
(2.11)        αε ∧ω     ≥                 ωεp ∧ω n−p ≥     (δp (U )−2n−p δ) > 0
         U∩Vε             M/δ  (U∩Vε )rEδ              M/δ

provided that δ is taken small enough, e.g. δ = 2−(n−p+1) δp (U ). The family of
(p, p)-forms αpε is uniformly bounded in mass since
                    Z               Z
                         p    n−p
                       αε ∧ ω     =   (α + εω)p ∧ ω n−p ≤ Const.
                   X                  X

Inequality (2.11) implies that any weak limit Θ of (αpε ) carries a positive mass
on U ∩ Y . By Skoda’s extension theorem
                                  P          [Sk81], 1Y Θ is a closed positive current
with support in Y , hence 1Y Θ =     λj [Yj ] is a combination of the various compo-
nents Yj of Y with coefficients λj > 0. Our construction shows that Θ belongs to
the cohomology class {α}p . Proposition 2.6 is proved.


We can now prove the main result of this section.
2.12. Theorem. Let (X, ω) be a compact n-dimensionalRKähler manifold and
let {α} in H 1,1 (X, R) be a nef cohomology class such that X αn > 0. Then {α}
contains a Kähler current T , that is, a closed positive current T such that T ≥ δω
for some δ > 0.
Proof. The trick is to apply Proposition 2.6 to the diagonal Ye = ∆ in the product
         e = X ×X. Let us denote by π1 and π2 the two projections of X
manifold X                                                              e = X ×X
                         e admits
onto X. It is clear that X

                                    e = π1∗ ω + π2∗ ω
                                    ω

as a Kähler metric, and that the class of

                                    e = π1∗ α + π2∗ α
                                    α
                  e [it is a limit of the Kähler classes π ∗ (α + εω) + π ∗ (α + εω)].
is a nef class on X                                        1              2
Moreover, by Newton’s binomial formula
                         Z               Z        2
                                  2n     2n
                                α
                                e =               αn > 0.
                           X×X            n     X

The diagonal is of codimension n in X,  e hence by Proposition 2.6 there exists a
                                       n
closed positive (n, n)-current Θ ∈ {eα } such that Θ ≥ ε[∆] for some ε > 0. We
define the (1, 1)-current T to be the push-forward

                                  T = c π1∗ (Θ ∧ π2∗ ω)

                                           12

for a suitable constant c > 0 which will be determined later. By the lower estimate
on Θ, we have
                           T ≥ cε π1∗ ([∆] ∧ π2∗ ω) = cε ω,
                                                        αn }, the current T belongs
thus T is a Kähler current. On the other hand, as Θ ∈ {e
to the cohomology class of the (1, 1)-form
                                        Z
                         n   ∗
                                                          n
                c π1∗ (e
                       α ∧ π2 ω)(x) = c      α(x) + α(y) ∧ ω(y),
                                          y∈Y

obtained by a partial integration in y with respect to (x, y) ∈ X ×X. By Newton’s
binomial formula again, we see that
                                        Z                     
                        n    ∗                     n−1
               c π1∗ (e


# Primary evidence, exact application judged separately: Tosatti-nef-Morse-2608.30153v2-P14-final


## Source lines 1-620

                                           TRANSCENDENTAL MORSE INEQUALITY ON KÄHLER
                                                          MANIFOLDS

                                                                          VALENTINO TOSATTI


                                                  Abstract. We prove the transcendental Morse inequality conjecture
                                                  of Boucksom-Demailly-Păun-Peternell. Among the corollaries of this
arXiv:2608.30153v2 [math.CV] 8 Sep 2026




                                                  result, this proves orthogonality of divisorial Zariski decompositions,
                                                  shows that the pseudoeffective and movable cones are dual, and estab-
                                                  lishes the differentiability of the volume function on the big cone, on all
                                                  compact Kähler manifolds.




                                                                           1. Introduction
                                          1.1. The volume function. The volume Vol([α]) ∈ R⩾0 of a (1, 1) co-
                                          homology class [α] ∈ H 1,1 (X, R) on a compact Kähler manifold X n is a
                                          fundamental quantity, introduced by Boucksom [6], which specializes to the
                                          volume of a holomorphic line bundle L in the case when [α] = c1 (L):
                                                                                            h0 (X, kL)
                                          (1.1)                      Vol(L) = lim sup                  .
                                                                                   k→∞        k n /n!
                                          For a general (1, 1)-class [α], its volume is set to be zero if the class is not
                                          pseudoeffective (i.e. it does not contain any closed positive (1, 1)-current),
                                          and otherwise it is defined by
                                                                                         Z
                                                                                              n
                                          (1.2)                     Vol([α]) = sup          Tac ,
                                                                                    T ∈[α],T ⩾0 X

                                          where the supremum ranges over all closed positive (1, 1)-currents in the
                                          class [α], and Tac denotes the absolutely continuous part in the Lebesgue
                                          decomposition of T . Boucksom [6] shows that the resulting function Vol :
                                          H 1,1 (X, R) → R⩾0 is continuous, and that classes with strictly positive
                                          volume (“big”) are characterized by the fact that they contain a Kähler
                                          current (a closed positive current which dominates some Kähler form).
                                          1.2. Transcendental Morse inequality. The main result of this paper is
                                          a resolution of the following “transcendental Morse inequality” conjecture
                                          about the volume function, which was formulated by Boucksom-Demailly-
                                          Păun-Peternell [8] in 2004, see also [16]:
                                          Theorem 1.1. Let X n be a compact Kähler manifold, and let [α], [β] ∈
                                          H 1,1 (X, R) be two nef classes. Then we have
                                                                              Z        Z
                                          (1.3)              Vol([α] − [β]) ⩾   αn − n   αn−1 ∧ β.
                                                                                    X            X
                                                                                        1

2                               VALENTINO TOSATTI


   The case when X is projective and [α], [β] are first Chern classes of line
bundles is a classical result due to Siu, Catanese, Ein-Lazarsfeld (see [22,
Thm. 2.2.15]), and independently Trapani [32], and this easily extends to
R-divisors [8, Lemma 4.2]. Further analytic and algebraic refinements were
found by Demailly [15, §12], Trapani [33] and Angelini [1]. The case of arbi-
trary nef (1, 1)-classes on a projective manifold was proved by Witt Nyström
[35] in 2016. For general Kähler manifolds, Popovici [26] (sharpening ideas
of Chiose [11] and Xiao [37]) proved that if the RHS of (1.3) is strictly posi-
tive, then so is the LHS. His method also proves a weaker bound than (1.3),
with the constant n on the RHS replaced by n2 [30, 27].
1.3. Applications. The seemingly innocuous statement of Theorem 1.1,
which is the transcendental version of a relatively easy statement in algebraic
geometry, turns out to have far-reaching consequences which were discovered
in the pioneering and deep works of Boucksom, Demailly, Favre, Jonsson,
Păun and Peternell in [8, 9]. Indeed, as explained for example in the clear
exposition by Boucksom in the appendix of [35], the following results are
corollaries of Theorem 1.1:
Corollary 1.2. Let X n be a compact Kähler manifold. Then we have:
    • (Orthogonality of divisorial Zariski decompositions) For every pseu-
      doeffective class [α] ∈ H 1,1 (X, R),
(1.4)                         Vol([α]) = ⟨[α]n−1 ⟩ · [α].
        • (Differentiability of Vol) Vol is locally C 1,1 in the cone of big (1, 1)-
          classes, and its gradient can be described as follows. Given [α], [β] ∈
          H 1,1 (X, R) with [α] big, we have
                      d
(1.5)                        Vol([α] + t[β]) = n⟨[α]n−1 ⟩ · [β].
                      dt t=0
        • (Dual of the pseudoeffective cone) The pseudoeffective cone E ⊂
          H 1,1 (X, R) and the movable cone M ⊂ H n−1,n−1 (X, R) are dual
          under the Poincaré pairing.
   Here ⟨·⟩ denotes the movable intersection products of Boucksom [5, 8], and
the movable cone M is the closed cone generated by classes of (n − 1, n − 1)-
currents of the form π∗ (ω˜1 ∧· · ·∧ ω̃n−1 ) where π : X̃ → X is any modification
and ω̃j are Kähler forms on X̃.
   A few remarks about these results. Divisorial Zariski decompositions were
defined by Boucksom [7], and the orthogonality statement in (1.4) can be
interpreted as the appropriate generalization of the fact that on surfaces the
positive and negative parts of the Zariski decomposition of a line bundle are
orthogonal, see the discussion in [8]. Boucksom-Demailly-Păun-Peternell [8]
had proved orthogonality and the duality statement for projective manifolds
and classes in the real Néron-Severi group, and this last restriction was
removed by Witt Nyström. In the general setting, the author [31] proved
orthogonality (1.4) when Vol([α]) = 0.

        TRANSCENDENTAL MORSE INEQUALITY ON KÄHLER MANIFOLDS                   3


   The C 1 differentiability of Vol on the Néron-Severi part of the big cone of
a projective manifold was proved independently by Boucksom-Favre-Jonsson
[9] and Lazarsfeld-Mustaţă [23]. Boucksom-Favre-Jonsson also proved (1.5),
and showed that their proof would go through in the general case provided
Theorem 1.1 holds, see again the appendix of [35]. Cao and the author [10]
recently observed that the transcendental Morse inequality (1.3), together
with the C 1 differentiability and (1.5), implies that the volume function is
locally C 1,1 inside the big cone of a compact Kähler manifold, and this is
sharp in general. This result is now therefore proved unconditionally. At
the boundary of the big cone, Vol is only locally Lipschitz and no better, in
general, see [10, 19] for examples, even when restricting Vol to segments.
   Furthermore, if we take [β] = c1 (D) where D ⊂ X is a prime divisor, then
Witt Nyström [36] and Vu [34] proved unconditionally that the derivative
in (1.5) exists, and equals n⟨[α]n−1 ⟩|X|D , which is n times the numerical
restricted volume of [α] along D, as defined by Boucksom [5] and studied
further by Collins and the author [12]. As a corollary of this (or following
directly the arguments in [9]), we obtain the transcendental generalization
of [9, Thm B]:
Corollary 1.3. If D ⊂ X is a prime divisor on a compact Kähler manifold
and [α] ∈ H 1,1 (X, R) is a big class, then we have
(1.6)                    ⟨[α]n−1 ⟩|X|D = ⟨[α]n−1 ⟩ · D.
Furthermore, this quantity equals zero if and only if D is contained in the
non-Kähler locus EnK ([α]).
   The last statement, which is the divisorial part of a conjecture of Collins
and the author [12], was already proved in [34, 36], but (1.6) was not known
in general.
   The last corollary that we will mention follows immediately from the work
of Toma [29], as observed by Fu-Xiao [20, Appendix], and the arguments in
[8, Remark 5.2], together with Theorem 1.1:
Corollary 1.4. Let X be a compact Kähler manifold. Then the movable
cone M ⊂ H n−1,n−1 (X, R) equals the closure of the balanced cone, which
consists of cohomology classes of the form [γ n−1 ] where γ is a Hermitian
metric with d(γ n−1 ) = 0 (“balanced”). Furthermore, M also equals the
closed cone generated by classes of (n−1, n−1)-currents of the form π∗ (ω̃ n−1 )
where π : X̃ → X is any modification and ω̃ is a Kähler form on X̃.
1.4. Ideas of proof. The basic method that we employ to prove Theorem
1.1, which was also underpinning many of the above-mentioned previous
works, is the mass concentration technique, which first appeared in De-
mailly’s visionary paper [14], and was later greatly extended by Demailly-
Păun [18], and further refined in [11, 37, 26]. By definition, to obtain a
lower bound for the volume of [α] − [β], it suffices to construct a closed pos-
itive current T in this class with an explicit lower bound for its absolutely-
continuous Monge-Ampère operator Tac   n , which after integration provides a

4                             VALENTINO TOSATTI


lower bound for the volume. For this, Demailly’s idea is to solve a family
of complex Monge-Ampère equations, whose solutions are provided by the
Calabi-Yau Theorem [38], and with RHS of the equation that degenerates
in the limit, to a singular measure that concentrates along a closed analytic
subvariety. One then shows that any weak limit T of these solutions will
have a nontrivial mass along the subvariety, and one can try to leverage this
to bound Tac n . In the case of (1.3), this strategy was first implemented in

[8, Appendix] in the projective case, and resulted in a suboptimal constant.
The works [11, 37, 26] observed that the mass concentration technique can
be coupled with a duality result of Lamari [21], involving Gauduchon metrics
(Hermitian metrics χ with ∂∂(χn−1 ) = 0), to produce the desired current T
via the Hahn-Banach theorem (a versatile technique discovered by Sullivan
[28]). Subsequently, Witt Nyström exploited the fact that in the projective
case one may assume [β] = c1 (A) where A is very ample, and use the current
of integration [H] along a divisor H ∈ |A| to “subtract off” [β] from [α] and
relate directly the space of α-psh functions and of (α − β)-psh functions. He
also remarked, see also McCleerey [24], that in the general Kähler case, the
role of [H] could be played by a closed positive current in a Kähler class [β]
which is supported on a pluripolar set. Unfortunately, it seems very hard
to construct such plurisupported currents in general.
   Our first observation is that it is easy to construct closed positive currents
in any Kähler class which are supported on a Lebesgue nullset (Proposition
2.1). These will typically be supported on a union of real-analytic hypersur-
faces. We then modify the mass concentration procedure of [8] using one of
these currents (or rather its regularizations) in the class [β] (which may be
assumed to be Kähler), and are able to show that any weak limit γ∞ of the
solutions of the family of complex Monge-Ampère equations (2.26), which
belong to [α], will have a sharp lower bound for (γ∞ )nac . Here we use cru-
cially that our auxiliary current is supported on a nullset, which forces the
singular part (γ∞ )sing of the limit to have at least the same mass as what a
current in the class [β] would have. This can be viewed as a transcendental
analog of the above-mentioned subtraction of [β] in [35]. In this argument,
there is also an auxiliary Gauduchon metric χ, and the output of the mass
concentration is then fed into a modification of the Lamari’s Hahn-Banach
argument (Proposition 2.3), which instead of producing a current R (in the
class [α] − [β]) with an explicit positive lower bound (which is what the
arguments in [21, 11, 37, 26, 30] do), gives an explicit positive lower bound
      n , which is exactly what suffices to estimate Vol([α] − [β]).
for Rac

Acknowledgments. The author is grateful to David Witt Nyström and
Nick McCleerey for discussions around 2018 about the method of [35] and
plurisupported currents. The idea that the role of plurisupported currents
in a Kähler class (whose existence remains unclear) could be played by
currents supported on a Lebesgue nullset (which can be easily constructed)
was discovered during discussions with ChatGPT. The author also thanks

        TRANSCENDENTAL MORSE INEQUALITY ON KÄHLER MANIFOLDS                    5


Mihai Păun for comments on a previous version. The author was partially
supported by NSF grant DMS-2404599.

                     2. Proof of the main theorem
  Throughout the paper we assume n ⩾ 2, since when n = 1 the main
theorem is well-known, simple, and left as an exercise.
2.1. Currents supported on a nullset.
Proposition 2.1. Let (X n , ω) be a compact Kähler manifold. Then there
is a closed positive current T ∈ [ω] with
(2.1)                            Supp(T ) ⊂ Σ,
where Σ ⊂ X is closed with Lebesgue measure zero.
Proof. Given any x ∈ X, we can find an open set x ∈ U contained in a
coordinate chart, and a smooth strictly plurisubharmonic function φ on U
such that ω = i∂∂φ on U . As in [3, Proof of Thm. 4], up to adding to φ the
real part of a holomorphic quadratic polynomial, we may assume without
loss that φ attains a strict local minimum at x. Up to shrinking U , there is
a > 0 such that min∂U φ ⩾ φ(x) + a. Thus, for any c ∈ (φ(x), φ(x) + a/2),
the open set {φ < c} is compactly contained in U and contains x. Thus,
                           
                              max{c − φ, 0} on U,
                     Φ=
                              0              on X\U,
defines a continuous nonnegative ω-psh function on X, with ω + i∂∂Φ iden-
tically zero on the open neighborhood {φ < c} of x (where it is of course
smooth). We will use the freedom to pick the constant c in an open interval.
   Repeating this construction atSevery point x ∈ X, and using compactness,
we obtain an open cover X = N           i=1 Ui by open sets as above, with points
xi ∈ Ui , smooth functions φi on Ui , constants ai > 0, such that if we pick
ci ∈ (φi (xi ), φi (xi ) + ai /2), then the continuous function
                               
                                  max{ci − φi , 0} on Ui ,
                         Φi =
                                  0                 on X\Ui ,
is ω-psh, nonnegative, supported on Ui , smooth on {Φi > 0} ∋ xi and
with ω + i∂∂Φi ≡ 0 there. Up to replacing (φi (xi ), φi (xi ) + ai /2) with a
smaller subinterval, we may assume that the open sets {Φi > 0} still cover
X, whenever the constants ci are chosen in these subintervals.
    We now make the choice of the constants ci as follows. For each 1 ⩽
i < j ⩽ N, and for each connected component V of Ui ∩ Uj (of which there
are at most countably many), we have that φi − φj is pluriharmonic on V ,
hence real analytic. If it happens that (φi − φj )|V is a constant, say A,
then we will choose our constants so that ci − cj ̸= A. Varying the indices
i, j and the connected component V , we have an at most countable number
of such conditions to satisfy. Since each constant ci can be chosen in some
open subinterval of (φi (xi ), φi (xi ) + ai /2), while the obstructions we just

6                            VALENTINO TOSATTI


described have Lebesgue measure zero in the product of these intervals, it
follows that we can make a choice for the constants {ci }N i=1 which satisfies
all these constraints.
   With this choice fixed, we obtain the functions Φi as above (with the sets
{Φi > 0} covering X), and we set Φ := max1⩽i⩽N Φi . This is a continuous
function on X, which is ω-psh, and we claim that the closed positive real
(1, 1)-current T := ω + i∂∂Φ satisfies the requirement (2.1). It is clear that
Φ > 0 on X. For each 1 ⩽ i < j ⩽ N, define closed sets
(2.2)                 Σij := {Φi = Φj = Φ} ⊂ Ui ∩ Uj ,
and
                                          [
(2.3)                         Σ :=             Σij .
                                     1⩽i<j⩽N

We claim that Σ has Lebesgue measure zero. Indeed, given 1 ⩽ i < j ⩽ N
and a connected component V of Ui ∩ Uj , if x ∈ Σij ∩ V then we must have
(2.4)                     φi (x) < ci ,   φj (x) < cj ,
and so
(2.5)            Φi (x) = ci − φi (x),    Φj (x) = cj − φj (x),
which shows that
(2.6)                Σij ∩ V ⊂ {φi − φj = ci − cj } ∩ V.
If φi − φj is constant on V , then this constant cannot be ci − cj thanks to
our choice, so in this case {φi − φj = ci − cj } ∩ V is empty. If, on the other
hand, φi − φj is nonconstant on V , then the level set {φi − φj = ci − cj } ∩ V
has Lebesgue measure zero since φi − φj is real analytic. This proves that
Σ is a Lebesgue nullset.
   Finally, we show that Supp(T ) ⊂ Σ. Given x ∈ X\Σ, by definition there
is a unique index 1 ⩽ j ⩽ N such that Φ(x) = Φj (x). Since the functions Φi
are continuous, and Φi (x) ̸= Φ(x) for all i ̸= j, it follows that the equality
Φ = Φj holds on an open neighborhood U of x. Since Φj (x) = Φ(x) > 0, up
to shrinking U we may assume that Φj > 0 on U , hence on U we have
(2.7)                 T = ω + i∂∂Φ = ω + i∂∂Φj ≡ 0,
as desired.                                                                  □
Remark 2.2. The support of the currents T produced by Proposition 2.1
will typically be a union of real analytic hypersurfaces, and will not be
pluripolar in general.
2.2. The Hahn-Banach argument. Given a closed positive real (1, 1)-
current T , there is a Lebesgue decomposition T = Tac + Tsing , see [6], into a
positive current whose coefficient measures are absolutely continuous with
respect to Lebesgue, and a positive current whose coefficients are singular.
This decomposition is linear in T .

         TRANSCENDENTAL MORSE INEQUALITY ON KÄHLER MANIFOLDS                   7


Proposition 2.3. Let (X n , ω) be a compact Kähler manifold, ψ be a closed
real (1, 1)-form, and f > 0 a smooth strictly positive function. Suppose that
given any Gauduchon metric χ on X, there is a positive (1, 1)-current ξ on
X (that may depend on χ) such that
                        Z              Z
(2.8)                      ψ ∧ χn−1 ⩾     ξac ∧ χn−1 ,
                         X                  X

and
(2.9)                             (ξac )n ⩾ f ω n ,
Lebesgue a.e. Then there is a closed positive current R ∈ [ψ] with
(2.10)                           (Rac )n ⩾ f ω n ,
Lebesgue a.e.
Proof. Let C be the set of real positive (1, 1)-currents T ⩾ 0 which satisfy
(Tac )n ⩾ f ω n Lebesgue a.e., which is nonempty (it contains Aω for A ≫ 1).
The set C is convex, thanks to the linearity of the Lebesgue decomposition
of real positive (1, 1)-currents, and the concavity of the map
                                                   1
                                       (Tac )n
                                     
                                                    n
(2.11)                      T (x) 7→           (x)    ,
                                         ωn
for Lebesgue a.e. x, which is proved in [6, Proof of Prop. 4.5].
   We claim that C is closed in the weak topology. Since all currents in C
are positive, and the weak topology is metrizable when restricted to real
positive (1, 1)-currents (see e.g. [17, p.174]), it suffices to check that C is
weakly sequentially closed. This in turn follows immediately from [6, Prop.
2.1], where it is proved that if positive real (1, 1)-currents Ti converge weakly
to T , then for Lebesgue a.e. x ∈ X we have
                            n
(2.12)                     Tac (x) ⩾ lim inf (Ti )nac (x).
                                       i→∞

Note also that if T ∈ C then Tac ∈ C too.
   If we let F be the set of closed real (1, 1)-currents of the form ψ + i∂∂u,
where u is a distribution, then the conclusion of the Proposition is precisely
the statement that C ∩ F is nonempty. The affine subspace F is also closed
in the weak topology, since by the ∂∂-Lemma it is identified with the space
of closed real (1, 1)-currents in the class [ψ] (see also [2, p.149] for another
proof).
   Suppose for a contradiction that C ∩ F = ∅, and consider the difference
set D := C − F = {T − S | T ∈ C, S ∈ F}. It is convex, and by assumption
it does not contain 0 (the zero current). It is also weakly closed, by the
following argument. Pick an arbitrary
                                    R current     W ∈R C − F, and let U be the
set of real (1, 1)-currents U with X U ∧ ω    n−1  < X W ∧ ω n−1 + 1, which
is an open neighborhood of W in the weak topology. Given any current

8                                   VALENTINO TOSATTI


U ∈ U ∩ (C − F ), write U = T − S with T ∈ C, S ∈ F, and observe that the
ω-mass of T satisfies
(2.13)
Z             Z            Z             Z             Z
        T ∧ω n−1 =       U ∧ω n−1 +       S∧ω n−1 ⩽          W ∧ω n−1 +       ψ∧ω n−1 +1 =: M,
    X                X                X                  X                X
where M is independent of U . Thus, T belongs to the weakly compact set
K of currents in C (which is weakly closed) with mass bounded above by M ,
and so U belongs to the difference set K − F, which is weakly closed since it
is the difference of a weakly compact and a weakly closed set (and the weak
topology is Hausdorff). This discussion shows that U ∩ (C − F) ⊂ K − F .
Returning to our current W , it thus belongs to
(2.14)          U ∩ (C − F) ⊂ U ∩ (C − F ) ⊂ K − F = K − F ⊂ C − F,
where the first inclusion uses that U is open, and we are done.
   We can then apply the Hahn-Banach strict separation theorem to separate
D and {0}, and we obtain a smooth real (n − 1, n − 1)-form σ and a constant
c > 0 such that
                             Z
(2.15)                          (T − S) ∧ σ ⩾ c,
                                      X

for all T ∈ C and S ∈ F. This implies that σ is ∂∂-closed and positive (in
the usual sense of positivity as currents, which for smooth (n − 1, n − 1)-
forms is equivalent to being semipositive definite). For the first property,
take any T ∈ C and any distribution u. Then for any t ∈ R we have that
ψ + ti∂∂u ∈ F, and so
                    Z                  Z
(2.16)                 (T − ψ) ∧ σ − t     i∂∂u ∧ σ ⩾ c,
                            X                    X
                                               R
and since this holds for all t ∈ R this forces X i∂∂u ∧ σ = 0. Since this
holds for u arbitrary, this
                         R means that ∂∂σ = 0. To prove that σ is positive,
we need to show that X V ∧ σ ⩾ 0 for any positive real (1, 1)-current V .
Pick any T ∈ C and t ∈ R⩾0 . Then T + tV is a positive real (1, 1)-current
with (Tac + tVac )n ⩾ (Tac )n Lebesgue a.e., and so T + tV ∈ C. Applying
(2.15) with S = ψ gives
                       Z                  Z
(2.17)                    (T − ψ) ∧ σ + t   V ∧ σ ⩾ c,
                                X                    X
                                                  R
and since this holds for all t ⩾ 0, we must have X V ∧ σ ⩾ 0 as desired.
   For any ε > 0, σ + εω n−1 is therefore a ∂∂-closed and strictly positive
definite real (n − 1, n − 1)-form, which for any T ∈ C satisfies
          Z                                  Z                Z
             (T − ψ) ∧ (σ + εω n−1 ) ⩾ c + ε    T ∧ ω n−1 − ε    ψ ∧ ω n−1
           X
(2.18)                                       ZX                X
                                                     n−1     c
                                     ⩾c−ε       ψ∧ω       ⩾ > 0,
                                              X             2

       TRANSCENDENTAL MORSE INEQUALITY ON KÄHLER MANIFOLDS                  9


provided we choose ε sufficiently small (independently of T ). Fix this value
of ε. Then, as observed in [25], there is a Gauduchon metric χ with χn−1 =
σ+εω n−1 . By our assumptions (2.8) and (2.9), there is a current ξ ∈ C which
also satisfies (2.8), hence contrasting this with (2.18) (with T = ξac ∈ C) we
get
               Z               Z                Z
                        n−1               n−1                   c
(2.19)             ψ∧χ       ⩾    ξac ∧ χ     ⩾     ψ ∧ χn−1 + ,
                X               X                X              2
which is a contradiction.                                                    □
Remark 2.4. Proposition 2.3, formulated using Bott-Chern cohomology,
remains true also when X is a general compact complex manifold, with very
minor changes to the proof (using a Gauduchon metric instead of a Kähler
one). Since we will not need this, we leave this to the interested reader.
2.3. The main proof.
Proof of Theorem 1.1. Up to adding a small multiple of [ω] to [α] and [β],
and using that the RHS of (1.3) is continuous as we vary the cohomology
classes, we may assume without loss that [α], [β] are Kähler classes, and we
fix Kähler forms γ ∈ [α], η ∈ [β]. Let
                                 n X γ n−1 ∧ η
                                   R
(2.20)                      δ :=     R
                                         n
                                               > 0.
                                      Xγ
We may assume without loss that δ < 1, otherwise (1.3) is trivially true.
Applying Proposition 2.1 to (X, η), we obtain a closed positive current T ∈
[β] with Supp(T ) ⊂ Σ, where Σ is a closed Lebesgue nullset.
   Write T = η + i∂∂φ for some quasi-psh function φ. Since [β] is Kähler,
applying Demailly’s regularization [13], specifically the version in [4, Thm
1], produces a sequence η + i∂∂φk of smooth closed semipositive real (1, 1)-
forms cohomologous to [β], with φk ↓ φ. Then
                                         !
                                    φk           1
(2.21)             Tk := η + i∂∂       1   ⩾        η > 0,
                                  1+ k        k+1
is a sequence of Kähler metrics in the class [β] which converge weakly to T .
    Choose open subsets {Uj }∞j=1 of X with Uj+1 ⊂ Uj for all j ⩾ 1, and Σ =
T∞
   j=1 Uj , and pick smooth cutoff functions 0 ⩽ ρj ⩽ 1 with Supp(ρj ) ⊂ Uj
and ρj |Uj+1 ≡ 1.
    Let χ be an arbitrary Gauduchon metric on X. Since the Radon measure
T ∧ χn−1 is supported on Σ, for every j ⩾ 1 we have
               Z                Z               Z
(2.22)            ρj T ∧ χn−1 =    T ∧ χn−1 =      η ∧ χn−1 > 0.
              X                 X               X
By weak convergence of Tk ∧ χn−1 to T ∧ χn−1 , for each j ⩾ 1 we can find
k(j) such that
                 Z                    Z
                                                     1
(2.23)              ρj Tk(j) ∧ χn−1 ⩾    η ∧ χn−1 − .
                  X                    X             j

10                           VALENTINO TOSATTI


To simplify notation, we will write simply Tj := Tk(j) . Then (2.23) implies
in particular that
                    Z                 Z
                                n−1                 1
(2.24)                   Tj ∧ χ     ⩾    η ∧ χn−1 − .
                      Uj               X            j
For j sufficiently large, the RHS of (2.24) is positive, hence
                    Z              !2 Z             2
                               n−1               n−1       C
(2.25)                  Tj ∧ χ       ⩾      η∧χ          − ,
                     Uj                  X                  j
for some constant C independent of j, which may change from line to line
in the following.
   For each j ⩾ 1, by the Calabi-Yau Theorem we can find a Kähler metric
γj ∈ [α] that satisfies
                                         R n
                                            γ
(2.26)            γjn = (1 − δ)γ n + δ R X n−1 Tj ∧ χn−1 .
                                        Xη∧χ
Indeed, the RHS of (2.26) integrates to X γ n .
                                          R


Key claim. For j sufficiently large we have
                  Z                 Z
                                                 C
(2.27)                 γj ∧ χn−1 ⩾     η ∧ χn−1 − ,
                   Uj                X           j
for some constant C independent of j.

The proof of the key claim follows the method of [8, Appendix], but crucially
on the LHS of (2.27) we are only integrating on the small open set Uj , while
on the RHS we integrate on all of X. This is a reflection of the key property
that T is supported on the nullset Σ.
   To prove the key claim, at each point x ∈ X, let 0 < λ1 (x) ⩽ · · · ⩽ λn (x)
be the eigenvalues of γj (x) with respect to Tj (x), which are continuous
functions of x. Then, dropping the point x from the notation, we have the
pointwise inequality γj ⩾ λ1 Tj , while (2.26) implies that
                       n            R n
                      Y                 γ     Tj ∧ χn−1
(2.28)                   λp ⩾ δ R X n−1                 ,
                                  Xη∧χ           Tjn
                      p=1
so we can estimate
(2.29)
                                     R n                                     !2
                                        γ                        Tj ∧ χn−1
Z               Z                             Z
          n−1               n−1                        1
    γj ∧χ     ⩾     λ1 Tj ∧χ    ⩾ δR  X
                                                                                  Tjn .
 Uj              Uj                 Xη∧χ
                                          n−1
                                               Uj λ2 · · · λn       Tjn
To estimate the RHS of (2.29) we use Hölder
(2.30)
                !2 Z                            !2  Z                    !
  Z
                                      T  ∧ χ n−1
                               1       j
      Tj ∧ χn−1   ⩽                               Tjn     λ2 · · · λn Tjn ,
   Uj                  Uj λ2 · · · λn    Tjn             Uj

         TRANSCENDENTAL MORSE INEQUALITY ON KÄHLER MANIFOLDS                  11


and the elementary inequality
                    nγjn−1 ∧ Tj        n Y
                                       X
(2.31)                             =              λp ⩾ λ2 · · · λn ,
                        Tjn
                                       i=1 p̸=i

which after integration gives
       Z                      Z              Z              Z
                        n        n−1            n−1
(2.32)     λ2 · · · λn Tj ⩽ n   γj ∧ T j ⩽ n   γj ∧ T j = n   γ n−1 ∧ η.
         Uj                   Uj                       X                   X

This, combined with (2.29) and (2.30), and using also (2.20) and (2.25),
gives
                             R n                      !2
                                γ
        Z                              Z
                                                              1
            γj ∧ χn−1 ⩾ δ R X n−1           Tj ∧ χn−1     R
         Uj                Xη∧χ          Uj              n X γ n−1 ∧ η
                                      Z              !2
(2.33)                        1                  n−1
                      =R         n−1
                                          Tj ∧ χ
                          Xη∧χ         Uj
                        Z
                                      C
                      ⩾     η ∧ χn−1 − ,
                          X            j
for all j large, where C is independent of j. This proves the key claim.

Next, by precompactness of currents in a fixed class, up to passing to a
subsequence (that we will suppress from the notation) we have γj ⇀ γ∞ ,
where γ∞ is a closed positive current in [α]. Write γ∞ = (γ∞ )ac + (γ∞ )sing
for its Lebesgue decomposition. For any given j > k ⩾ 1, thanks to the key
claim (2.27) we have
               Z                 Z               Z
                                                                C
(2.34)            ρk γj ∧ χn−1 ⩾     γj ∧ χn−1 ⩾     η ∧ χn−1 − ,
                X                 Uj              X             j
so letting j → ∞ we get
                     Z                  Z
                                  n−1
(2.35)                  ρk γ∞ ∧ χ     ⩾   η ∧ χn−1 .
                       X                           X

Since ρk converges pointwise to the characteristic function of Σ, we can
let k → ∞ and dominated convergence (with respect to the finite measure
γ∞ ∧ χn−1 ) gives
                     Z               Z
                               n−1
(2.36)                  γ∞ ∧ χ     ⩾     η ∧ χn−1 .
                        Σ                         X

But since the positive measure (γ∞ )ac ∧ χn−1 is absolutely continuous with
respect to Lebesgue, and Σ is a nullset, this gives
             Z                    Z                     Z
(2.37)         (γ∞ )sing ∧ χn−1 ⩾ (γ∞ )sing ∧ χn−1 ⩾       η ∧ χn−1 ,
              X                         Σ                              X

12                                         VALENTINO TOSATTI


and so
(2.38)
 Z                               Z                          Z
                       n−1                        n−1
         (γ − η) ∧ χ         =           γ∞ ∧ χ      η ∧ χn−1
                                                        −
     X
                               ZX                  X
                                                     Z                      Z
                                              n−1                     n−1
                             =    (γ∞ )ac ∧ χ     +     (γ∞ )sing ∧ χ     −    η ∧ χn−1
                                X                     X                      X
                               Z
                             ⩾    (γ∞ )ac ∧ χn−1 .
                                 X
This is where the crucial “subtraction of [β]” happened. On the other hand,
(2.26) implies that
(2.39)                                       γjn ⩾ (1 − δ)γ n ,
and [6, Prop. 2.1] gives that
(2.40)                                     (γ∞ )nac ⩾ (1 − δ)γ n ,
Lebesgue a.e. We can then feed (2.38) and (2.40) into Proposition 2.3 (taking
                          n
ψ = γ − η, f = (1 − δ) ωγ n , and for each given Gauduchon metric χ we take
ξ = γ∞ ) to get a closed positive current R ∈ [α] − [β] with
(2.41)                                     (Rac )n ⩾ (1 − δ)γ n .
Thus,
                                     Z                          Z         Z          Z
                                               n                    n         n
(2.42) Vol([α] − [β]) ⩾                   (Rac ) ⩾ (1 − δ)          γ =       α −n       αn−1 ∧ β,
                                     X                          X         X          X
and we are done.                                                                                 □


# Primary evidence, exact application judged separately: Demailly-agbook-Harvard


## Source lines 17220-17428

                            § 6. Commutation Relations                                                    305

(6.3) Lemma. In Cn , we have [d′′⋆ , L] = id′ .
Proof. Formula (6.2′′ ) can be written more briefly
                                                       X ∂             ∂u 
                                         d′′⋆ u = −                         .
                                                        ∂z k           ∂zk
                                                          k

Then we get
                                    X ∂              ∂                X ∂                   ∂u 
                 [d′′⋆ , L]u = −                          (ω ∧ u) + ω ∧                               .
                                     ∂z k             ∂zk                ∂z k                 ∂zk
                                    k                                            k

                                                           ∂                ∂u
Since ω has constant coefficients, we have                    (ω ∧ u) = ω ∧     and therefore
                                                          ∂zk               ∂zk
                                        X ∂                 ∂u         ∂      ∂u 
                                                                                      
                     ′′⋆
                   [d , L] u = −                         ω∧         −ω∧
                                               ∂z k           ∂zk          ∂z k  ∂zk
                                         k
                                        X ∂              ∂u
                                   =−                   ω ∧       .
                                              ∂z k           ∂zk
                                         k

           ∂
Clearly             ω = −idzk , so
          ∂z k
                                                       X              ∂u
                                    [d′′⋆ , L] u = i          dzk ∧       = id′ u.                         
                                                                      ∂zk
                                                          k



   We are now ready to derive the basic commutation relations in the case of an arbitrary
Kähler manifold (X, ω).

(6.4) Theorem. If (X, ω) is Kähler, then

                                    [d′′⋆ , L]= id′ ,            [d′⋆ , L]= −id′′ ,
                                    [Λ, d′′ ] = −id′⋆ ,          [Λ, d′ ] = id′′⋆ .


Proof. It is sufficient to verify the first relation, because the second one is the conjugate
of the first, and the relations of the second line are the adjoint of those of the first line.
If (zj ) is a geodesic coordinate system at a point x0 ∈ X, then for any (p, q)-forms u, v
with compact support in a neighborhood of x0 , (4.9) implies
                                    Z    X                      X                       
                      hhu, vii =                   uIJ v IJ +             aIJKL uIJ v KL dV,
                                     M       I,J                I,J,K,L


with aIJKL (z) = O(|z|2 ) at x0 . An integration by parts as in (3.12) and (6.2′′ ) yields
                           X ∂uI,J ∂                                      X
           d′′⋆ u = −                               (dzI ∧ dz J ) +             bIJKL uIJ dzK ∧ dz L ,
                              ∂zk ∂z k
                           I,J,k                                      I,J,K,L

306                                                  Chapter VI. Hodge Theory

where the coefficients bIJKL are obtained by derivation of the aIJKL ’s. Therefore
bIJKL = O(|z|). Since ∂ω/∂zk = O(|z|), the proof of Lemma 6.3 implies here [d′′⋆ , L]u =
id′ u + O(|z|), in particular both terms coincide at every given point x0 ∈ X.         

(6.5) Corollary. If (X, ω) is Kähler, the complex Laplace-Beltrami operators satisfy

                                                          1
                                           ∆′ = ∆′′ =       ∆.
                                                          2

Proof. It will be first shown that ∆′′ = ∆′ . We have
                                                                       
                                 ∆′′ = [d′′ , d′′⋆ ] = −i d′′ , [Λ, d′ ] .

Since [d′ , d′′ ] = 0, Jacobi’s identity (5.7) implies
                                                               
                                 − d′′ , [Λ, d′ ] + d′ , [d′′ , Λ] = 0,
                           
hence ∆′′ = d′ , −i[d′′ , Λ] = [d′ , d′⋆ ] = ∆′ . On the other hand

                  ∆ = [d′ + d′′ , d′⋆ + d′′⋆ ] = ∆′ + ∆′′ + [d′ , d′′⋆ ] + [d′′ , d′⋆ ].

Thus, it is enough to prove:

(6.6) Lemma. [d′ , d′′⋆ ] = 0, [d′′ , d′⋆ ] = 0.
                                             
Proof. We have [d′ , d′′⋆ ] = −i d′ , [Λ, d′ ] and (5.7) implies
                                                                   
                         − d′ , [Λ, d′ ] + Λ, [d′ , d′ ] + d′ , [d′ , Λ] = 0,
                     
hence −2 d′ , [Λ, d′ ] = 0 and [d′ , d′′⋆ ] = 0. The second relation [d′′ , d′⋆ ] = 0 is the adjoint
of the first.                                                                                     

(6.7) Theorem. ∆ commutes with all operators ⋆, d′ , d′′ , d′⋆ , d′′⋆ , L, Λ.

Proof. The identities [d′ , ∆′ ] = [d′⋆ , ∆′ ] = 0, [d′′ , ∆′′ ] = [d′′⋆ , ∆′′ ] = 0 and [∆, ⋆] = 0 are
immediate. Furthermore, the equality [d′ , L] = d′ ω = 0 together with the Jacobi identity
implies                                                       
                 [L, ∆′ ] = L, [d′ , d′⋆ ] = − d′ , [d′⋆ , L] = i[d′ , d′′ ] = 0.
By adjunction, we also get [∆′ , Λ] = 0.                                                            

§ 6.2. Commutation Relations on Hermitian Manifolds
   We are going to extend the commutation relations of § 6.1 to an arbitrary hermitian
manifold (X, ω). In that case ω is no longer tangent to a constant metric, and the
commutation relations involve extra terms arising from the torsion of ω. Theorem 6.8
below is taken from [Demailly 1984], but the idea was already contained in [Griffiths 1966].

(6.8) Theorem. Let τ be the operator of type (1, 0) and order 0 defined by τ = [Λ, d′ ω].
Then

                       § 6. Commutation Relations                                                   307

a)     [d′′⋆ , L]= i(d′ + τ ),
b)     [d′⋆ , L] = −i(d′′ + τ ),
c)     [Λ, d′′ ] = −i(d′⋆ + τ ⋆ ),
d)     [Λ, d′ ] = i(d′′⋆ + τ ⋆ ) ;
d′ ω will be called the torsion form of ω, and τ the torsion operator.
Proof. b) follows from a) by conjugation, whereas c), d) follow from a), b) by adjunction.
It is therefore enough to prove relation a).
   Let (zj )1⩽j⩽n be complex coordinates centered at a point x0 ∈ X, such that the n-
tuple (∂/∂z1 , . . . , ∂/∂zn ) is an orthonormal basis of Tx0 X for the metric ω(x0 ). Consider
the metric with constant coefficients
                                              X
                                       ω0 = i      dzj ∧ dz j .
                                                1⩽j⩽n

The metric ω can then be written
                                  ω = ω0 + γ with γ = O(|z|).
Denote by h , i0 , L0 , Λ0 , d′⋆   ′′⋆
                              0 , d0 the inner product and the operators associated to
the constant metric ω0 , and let dV0 = ω0n /2n n!. The proof of relation a) is based on a
Taylor expansion of L, Λ, d′⋆ , d′′⋆ in terms of the operators with constant coefficients
L0 , Λ0 , d′⋆   ′′⋆
           0 , d0 .

(6.9) Lemma. Let u, v ∈ C∞ (X, Λp,q TX
                                     ⋆
                                       ). Then in a neighborhood of x0
                          hu, vi dV = hu − [γ, Λ0 ]u, vi0 dV0 + O(|z|2 ).

Proof. In a neighborhood of x0 , let
                           X                 ⋆
                     γ=i          γj ζj⋆ ∧ ζ j ,            γ1 ⩽ γ2 ⩽ · · · ⩽ γn ,
                                1⩽j⩽n

be a diagonalization of the (1,1)-form γ(z) with respect to an orthonormal basis (ζj )1⩽j⩽n
of Tz X for ω0 (z). We thus have
                                               X              ⋆
                                ω = ω0 + γ = i     λj ζj⋆ ∧ ζ j

with λj = 1 + γj and γj = O(|z|). Set now

              J = {j1 , . . . , jp },     ζJ⋆ = ζj⋆1 ∧ · · · ∧ ζj⋆p ,     λJ = λj1 · · · λjp ,
                              X                  ⋆              X                  ⋆
                     u=             uJ,K ζJ⋆ ∧ ζ K ,      v=          vJ,K ζJ⋆ ∧ ζ K
where summations are extended to increasing multi-indices J, K such that |J| = p,
|K| = q. With respect to ω we have hζj⋆ , ζj⋆ i = λ−1
                                                   j , hence
                    X
        hu, vi dV =   λ−1  −1
                        J λK uJ,K v J,K λ1 · · · λn dV0
                       J,K
                       X         X            X             X        
                   =         1−         γj −         γj +           γj uJ,K v J,K dV0 + O(|z|2 ).
                       J,K        j∈J          j∈K          1⩽j⩽n

308                                                Chapter VI. Hodge Theory

Lemma 6.9 follows if we take Prop. 5.8 into account.                                    
                                         
(6.10) Lemma. d′′⋆ = d′′⋆           ′′⋆
                         0 + Λ0 , [d0 , γ] at point x0 , i.e. at this point both operators
have the same formal expansion.
Proof. Since d′′⋆ is an operator of order 1, Lemma 6.9 shows that d′′⋆ coincides at point
x0 with the formal adjoint of d′′ for the metric
                                        Z
                            hhu, vii1 =   hu − [γ, Λ0 ]u, vi0 dV0 .
                                            X

For any compactly supported u ∈ C∞ (X, Λp,q TX       ⋆
                                                       ), v ∈ C∞ (X, Λp,q−1 TX   ⋆
                                                                                   ) we get by
definition
                       Z                             Z
               ′′                         ′′
         hhu, d vii1 =   hu − [γ, Λ0 ]u, d vi0 dV0 =     hd′′⋆    ′′⋆
                                                           0 u − d0 [γ, Λ0 ]u, vi0 dV0 .
                         X                                 X

Since ω and ω0 coincide at point x0 and since γ(x0 ) = 0 we obtain at this point
                                                                 ′′⋆            
                 d′′⋆ u = d′′⋆
                           0   u − d ′′⋆
                                     0   [γ, Λ0 ]u  = d ′′⋆
                                                        0   u −  d 0  , [γ, Λ0 ]  u;
                    ′′⋆    ′′⋆
                                   ′′⋆           
                   d = d0 − d0 , [γ, Λ0 ] .

We have [Λ0 , d′′⋆     ′′     ⋆              ′′
               0 ] = [d , L0 ] = 0 since d ω0 = 0. The Jacobi identity (5.7) implies
                               ′′⋆                       
                                d0 , [γ, Λ0] + Λ0 , [d′′⋆
                                                      0 , γ] = 0,


# COMPLETE independent A-E reconstruction and dependency chain

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "A–B: actual balanced full-test minimizers give V=nW/H and the same cost for every attaining selection. Fixed-test limits identify the nef endpoint and prove the finite improper identity for every smooth a, without an endpoint PDE or regularity of metric selections.",
      "detailedSummary": "The permitted closed base Monge–Ampère theorem supplies A_epsilon^m=(W/H)sigma/(a+epsilon). The metric gamma=(a+epsilon)^(-1/m)(A_epsilon+(a+epsilon)w) is balanced. Matrix AM–GM proves the lower bound for every Gauduchon test, and gamma attains equality. Differentiability of the explicit value and a supporting-line argument determine every minimizer's cost, including s=0 by strict extension. Fixed-test comparison identifies the raw endpoint infimum with both the path limit and decreasing Hermitian regularization. Monotone convergence gives V_endpoint=nW/H(0), interpreted as zero for an infinite inverse moment. Ordinary calculus then proves the finite improper integral for every minimizing selection. Only the expressly permitted smooth positive closed-class existence theorem is imported.",
      "text": "This note proves restricted targets A and B for the exact product probability in the assignment. Write n=m+1, a in C-infinity(B), L=a+epsilon with epsilon=t-s>0, H(epsilon)=integral_B L^(-1) sigma, J(epsilon)=integral_B L^(-2) sigma, and W=integral_B alpha^m. Pullbacks to X=B x C are implicit. A smooth area form w on the curve is d-closed for dimensional reasons. Hence Omega=alpha+w is a Kähler metric on X and is itself a Gauduchon test; the test set is nonempty. Theta_s=alpha+Lw is positive. Theta_t=alpha+aw is semipositive, so theta_t+delta h>0 for every delta>0 with zero potential. Thus the endpoint is nef in the specified Hermitian definition.\n\nThe only imported PDE is the expressly permitted smooth positive-data theorem in a strict closed Kähler class. Its indispensable statement was checked against Tosatti–Weinkove, https://arxiv.org/pdf/0910.1390v2, Corollary 1 on printed page 1 and the closed normalization on printed page 2. Their potential convention is i partial barpartial; multiplying the source potential by 2 pi gives the present dd^c. The density constant is zero for a closed background when the total masses coincide, by smooth Stokes. Here rho_epsilon=(W/H) sigma/L is smooth positive and has total mass W. The theorem therefore supplies a genuine global smooth phi_epsilon with\n  A_epsilon=alpha+dd^c phi_epsilon>0, d A_epsilon=0,\n  A_epsilon^m=(W/H) sigma/L.\nClosedness also gives integral_B A_epsilon^m=W directly: expand the power and integrate each term containing dd^c phi_epsilon by Stokes against its remaining closed factors. Existence is used independently at each epsilon; continuity or differentiability of epsilon -> phi_epsilon is not presumed.\n\nPut Psi=A_epsilon+Lw and v=nW/H. Since w^2=0 and horizontal forms above degree 2m vanish,\n  Psi^n=n L A_epsilon^m wedge w=v mu,\n  gamma=L^(-1/m) Psi,\n  gamma^m=A_epsilon^m/L+m A_epsilon^(m-1) wedge w.\nGamma is a smooth positive Hermitian metric. The first term of gamma^m is a horizontal top-degree form, so its exterior derivative vanishes even for nonconstant L. The second is closed because A_epsilon and w are closed. Thus d gamma^m=0 and dd^c gamma^m=0: gamma is an actual balanced Gauduchon test.\n\nFor ANY smooth positive Gauduchon metric xi on X, Stokes and dd^c xi^m=0 imply\n  integral_X theta_s wedge xi^m=integral_X Psi wedge xi^m.\nNo product structure or closedness of xi is assumed. Diagonalize Psi relative to xi at a point, with positive eigenvalues r_1,...,r_n. The wedge identities and matrix AM–GM give\n  (Psi wedge xi^m)/xi^n=(r_1+...+r_n)/n\n    >=(r_1...r_n)^(1/n)=(Psi^n/xi^n)^(1/n).\nUsing Psi^n=v mu and integrating yields\n  integral_X theta_s wedge xi^m>=v^(1/n) D_mu(xi).\nThe denominator is positive and finite on the compact manifold. This lower bound holds for every participating test, including arbitrary nonproduct Gauduchon metrics.\n\nFor the constructed metric,\n  gamma^n=v L^(-n/m) mu,\n  D_mu(gamma)=v^(m/n) integral_X L^(-1) mu=v^(m/n) H,\n  integral_X theta_s wedge gamma^m=integral_X Psi wedge gamma^m=v H.\nThe probability normalization integral_C w=1 is used exactly. Gamma therefore attains the full infimum, and\n  lambda_mu(theta_s)=(nW/H)^(1/n),\n  V_mu(theta_s)=nW/H.\nThis is full-test equality and actual minimizing-test existence. The answer retains the specified probability sigma wedge w: the shape of w cancels through its mass-one normalization, whereas the inverse moment H retains sigma.\n\nFor gamma the cost numerator is\n  integral_X w wedge gamma^m=integral_B A_epsilon^m/L=(W/H)J.\nAfter division by D_mu(gamma), its cost is\n  C(s)=n^(-m/n) W^(1/n) H^(-(n+1)/n) J.\nTo prove the same cost for every attaining metric, define\n  Q_r(xi)=integral_X theta_r wedge xi^m/D_mu(xi),\n  c_xi=integral_X w wedge xi^m/D_mu(xi).\nIf xi attains at s, then at each neighboring strict point r,\n  lambda_mu(theta_r)<=Q_r(xi)\n    =lambda_mu(theta_s)-(r-s)c_xi.\nOn compact strict intervals L has a uniform positive lower bound, so dominated differentiation gives dH/ds=J. Differentiating the explicit value gives\n  d/ds lambda_mu(theta_s)\n    =-n^(-m/n) W^(1/n) H^(-(n+1)/n)J.\nDivide the supporting-line inequality by r-s first for r>s and then for r<s. Taking limits forces -c_xi to equal this derivative. Thus every attaining xi has cost C(s). The argument includes s=0 because the same strictly positive path and formulas extend to all real s<t, including negative s. No metric uniqueness or differentiable metric family is used.\n\nDefine the raw endpoint infimum over the same full test set by\n  E=inf_xi integral_X theta_t wedge xi^m/D_mu(xi).\nIt is nonnegative by semipositivity and finite by testing Omega. For each fixed xi,\n  Q_(t-epsilon)(xi)=Q_t(xi)+epsilon c_xi,\nwith c_xi finite and nonnegative. Consequently lambda_mu(theta_(t-epsilon))>=E, and these values decrease as epsilon decreases. Let their limit be ell. For each fixed xi, taking the limit in lambda_mu(theta_(t-epsilon))<=Q_t(xi)+epsilon c_xi gives ell<=Q_t(xi). Taking the infimum yields ell<=E. Thus ell=E, without interchanging an infimum and an uncontrolled limit.\n\nThe identical argument applies to theta_t+delta h. Its raw infimum lambda_delta is at least E, decreases as delta decreases, and for every fixed xi satisfies\n  lambda_delta<=Q_t(xi)+delta integral_X h wedge xi^m/D_mu(xi).\nThe final term tends to zero. Therefore lim_(delta down to 0) lambda_delta=E for the specified arbitrary Hermitian h. The raw endpoint infimum agrees with decreasing Hermitian regularization.\n\nMonotone convergence gives H(epsilon)->H(0)=integral_B sigma/a, with reciprocal +infinity on a=0. Hence\n  lambda_mu(theta_t)=(nW/H(0))^(1/n),\n  V_mu(theta_t)=nW/H(0),\nwhere 1/(+infinity)=0. This covers a identically zero, positive-measure zero sets and arbitrarily flat zeros. No endpoint Monge–Ampère solution is assumed.\n\nFor any selection of attaining metrics xi_s, without any assumed measurability or regularity of the metric-valued selection, the scalar cost equals the same smooth nonnegative C(s) at every strict s. The scalar cost is therefore continuous and measurable. For b<t, ordinary calculus gives\n  integral_0^b C(s) ds=lambda_mu(theta_0)-lambda_mu(theta_b).\nThese integrals increase with b and are bounded by lambda_mu(theta_0). Taking the actual endpoint limit proves\n  integral_0^t C(s) ds=lambda_mu(theta_0)-lambda_mu(theta_t)<infinity.\nThus the improper integral is established for every selection, rather than assumed.\n\nEvidence and reproducibility: sources/primary_checks.json records the precise permitted primary statements and conventions checked. Run \"python3 fetch_sources.py\" to repeat the public PDF download commands. Their initial local executions failed with curl exit 7 because the configured proxy at port 8080 was unreachable; artifacts/source_fetch_log.json retains the failures. The public primary PDF statements were successfully read through the available web tool; sources/web_commands.json records reproducible requests. The PDE foundation is expressly imported, not recursively reproved. All remaining steps use the specified elementary tools. No additional uncertain indispensable premise remains in A–B. This is an unverified mathematical draft.\n\nArtifacts: /workspace/research/native-workers/codex-Mtj7p2",
      "support": []
    },
    {
      "id": "n2",
      "summary": "C: two-sided distance^k vanishing along a nonempty codimension-d zero submanifold gives all five proposed integrable cost profiles. Positive endpoint volume is equivalent to d>k; finitely many disjoint finite-order components use the smallest ratio.",
      "detailedSummary": "Positive smooth density and bounded tubular Jacobians reduce inverse moments to integral rho^(d-1)/(rho^k+epsilon)^p d rho. With r=d/k, substitution gives power divergence for r<p, logarithmic divergence for r=p, and an actual finite moment limit for r>p. Applying p=1,2 to n1's scalar cost proves every proposed profile and its integrability. The endpoint inverse moment is finite exactly for r>1. For finitely many disjoint components, the smallest ratio controls the divergent terms and positivity prevents cancellation. These are geometric hypotheses, not assumed integral bounds; they do not classify arbitrary paths.",
      "text": "This note proves target C using the full volume and cost formula of n1. Fix a smooth Riemannian metric on B. The tubular hypothesis describes a nonempty zero set Z={a=0}, a smooth compact embedded real submanifold of positive codimension d, with\n  c dist(b,Z)^k<=a(b)<=C dist(b,Z)^k\nin a fixed sufficiently small normal tube, for c,C>0 and k>0. Outside the tube, a is bounded below by a positive constant. If the zero set is empty, a instead has a positive minimum, H(0),J(0) are finite, and the cost has a finite positive limit; no codimension/order ratio is required.\n\nSet r=d/k. The smooth positive sigma has density bounded above and below relative to the fixed Riemannian volume. In a smaller fixed tube, normal tubular coordinates have smooth positive Jacobian bounded above and below. Radial integration in the d-dimensional normal directions contributes rho^(d-1) d rho, with positive finite factors from integration over Z and the unit normal spheres. These hypotheses justify the following comparisons without assuming any inverse-moment behavior.\n\nFor p=1,2 put M_p(epsilon)=integral_B (a+epsilon)^(-p) sigma. For a fixed tube radius R,\n  M_p(epsilon) comparable to\n    1+integral_0^R rho^(d-1)/(rho^k+epsilon)^p d rho\nas epsilon decreases to zero. The complement contributes a bounded term. The denominators c rho^k+epsilon and C rho^k+epsilon are uniformly comparable to rho^k+epsilon, using min(c,1) and max(C,1).\n\nSubstituting q=rho^k and then q=epsilon y gives exactly\n  (1/k) integral_0^(R^k) q^(r-1)/(q+epsilon)^p dq\n    =(epsilon^(r-p)/k)\n       integral_0^(R^k/epsilon) y^(r-1)/(1+y)^p dy.\nAt zero the integrand is integrable because r>0. If r<p, its tail is comparable to y^(r-p-1), an integrable power at infinity, and the scaled integral tends to a finite strictly positive constant. If r=p, the tail is comparable to 1/y, giving logarithmic growth. If r>p, the unregularized radial exponent r-p-1 is integrable at zero, and the tube and complement estimates prove M_p(0)<infinity. Monotone convergence then gives the actual finite limit. Conversely the lower tubular estimate makes M_p(0) infinite for r<=p. Therefore\n  r<p: M_p(epsilon) comparable to epsilon^(r-p);\n  r=p: comparable to log(1/epsilon);\n  r>p: M_p(epsilon)->M_p(0), finite and positive.\nThe finite moments are strictly positive since a is positive away from its proper zero submanifold.\n\nApply p=1,2 to H=M_1 and J=M_2. By n1,\n  C(t-epsilon)=K H(epsilon)^(-(n+1)/n)J(epsilon),\n  K=n^(-m/n)W^(1/n)>0.\nFor r<1 the resulting exponent is\n  -(r-1)(n+1)/n+r-2=(1-r)/n-1.\nFor r=1, H is logarithmic and J is comparable to epsilon^(-1). For 1<r<2, H tends to H(0)>0 and J has exponent r-2. For r=2, H has a finite positive limit and J is logarithmic. For r>2, both moments have finite positive limits. Thus every proposed profile holds:\n  r<1: C(t-epsilon) comparable to epsilon^((1-r)/n-1);\n  r=1: comparable to epsilon^(-1)log(1/epsilon)^(-(n+1)/n);\n  1<r<2: comparable to epsilon^(r-2);\n  r=2: comparable to log(1/epsilon);\n  r>2: tends to K H(0)^(-(n+1)/n)J(0)>0.\nComparability means two bounds with fixed positive constants independent of sufficiently small epsilon. The hypotheses do not prescribe an exact leading coefficient in the first four regimes.\n\nEach profile is integrable at epsilon=0. For r<1 its exponent exceeds -1. For r=1, substitution u=log(1/epsilon) gives a convergent tail integral of u^(-(n+1)/n), since (n+1)/n>1. For 1<r<2 the exponent r-2 exceeds -1. The logarithm at r=2 is integrable, and the final profile is bounded. These are quantitative geometric sufficient conditions, not assumptions of the desired improper-integral bound. Its exact total value was proved independently in n1.\n\nBy n1 the endpoint volume is positive exactly when H(0) is finite. The p=1 radial criterion makes this equivalent to r>1, or d>k. Thus positive volume can occur with a nonempty zero set; n3 establishes the bigness obstruction in that case.\n\nFor finitely many disjoint nonempty zero components Z_j, with codimensions d_j and finite orders k_j satisfying the respective two-sided bounds, choose disjoint small fixed tubes. Their complement has a positive lower bound for a. Each moment is a finite sum of tube contributions and a bounded complement contribution. Let r_*=min_j d_j/k_j. If r_*<p, a minimum-ratio component has the strongest divergent power epsilon^(r_*-p); larger-ratio contributions have lower growth or stay bounded. If r_*=p, at least one contribution is logarithmic and all others are bounded. If r_*>p, every unregularized moment is finite and monotone convergence gives the finite total limit. All contributions are positive, so cancellation cannot occur. The five profiles therefore hold with r replaced by r_*, and positive endpoint volume is equivalent to r_*>1. When r_*>2 the exact limit uses the actual total H(0),J(0).\n\nEvidence: the exponent identity is algebraic for every admissible real r. The small program checks.py also verifies it at 18 rational (n,r) pairs; those finite checks are not the proof of the continuous statement. Run \"python3 checks.py\"; artifacts/check_inputs.json and artifacts/check_output.json retain its inputs and outputs. No additional PDE or uncertain indispensable premise is needed beyond n1 and the stated geometric hypotheses. This restricted result does not classify arbitrary paths.\n\nArtifacts: /workspace/research/native-workers/codex-Mtj7p2",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "D: theta_t is big exactly when a has no zero, proved against every genuine quasi-psh potential using distributional smooth tests. Normalized projective examples are nonclosed and nonbig but have V=(m+1)(m-1)/m>0, logarithmic cost for m=2 and a positive finite cost limit for m>2.",
      "detailedSummary": "Pairing a purported strict current with f alpha^m for arbitrary smooth nonnegative base f removes the potential by distributional Stokes and forces a to be uniformly positive. No singular current is restricted to a fiber. Conversely a positive minimum gives a smooth strict metric. The affine Fubini–Study density and radial substitution prove mass one and the exact probability law m x^(m-1)dx for the specified global a. Its sole zero is quadratic with codimension 2m. Exact moments give the full endpoint volume and the claimed costs through n1. Rational and Decimal checks corroborate implemented arithmetic only; they do not certify the PDE or exhaust Gauduchon tests.",
      "text": "This note proves target D, using n1 for full-test values and n2 for geometric profiles. Consider any genuine global quasi-psh u with\n  T=theta_t+dd^c u>=delta h,\nwhere delta>0. Genuine quasi-psh local integrability makes u a global distribution. It need not be finite on any particular fiber. Compactness and positivity give c>0 such that h>=c Omega, where Omega=alpha+w.\n\nFor every smooth nonnegative f on B, F=f alpha^m is a smooth strongly semipositive (m,m) test form on X. It satisfies dd^c F=0: its coefficients and factors are pulled back from B, and dd^c F would have horizontal bidegree (m+1,m+1) on an m-fold. Distributional Stokes gives\n  integral_X dd^c u wedge F=integral_X u dd^c F=0.\nPair positivity of T-delta c Omega with F. Using alpha^(m+1)=0 and integral_C w=1 gives\n  0<=integral_X (T-delta c Omega) wedge f alpha^m\n    =integral_B f(a-delta c)alpha^m.\nThese are smooth test pairings; no restriction or trace of T on a fiber occurs. Since this holds for every such f, continuity forces a>=delta c everywhere: a smooth nonnegative bump supported where a-delta c<0 would contradict it. Thus a zero excludes EVERY genuine strict quasi-psh representative, including a potential singular on the whole zero fiber.\n\nConversely, if a has no zero, its compact minimum is positive. Theta_t=alpha+aw is then smooth strictly positive and dominates a positive multiple of h. The genuine potential u=0 proves bigness. Consequently theta_t is big if and only if a has no zero. Combining this with n2 gives positive-volume nonbig endpoints whenever the zero set satisfies the tubular criterion with minimum ratio greater than one. This is a criterion for these product backgrounds, not a general positive-volume bigness theorem.\n\nFor the explicit example, on projective m-space, m>=2, use the chart Z_0!=0 with z_j=Z_j/Z_0 and rho^2=sum_j |z_j|^2. Define\n  kappa=dd^c log(1+rho^2).\nOn other charts the potentials are log(sum |Z_j|^2/|Z_i|^2). Their differences are logarithms of squared moduli of nonvanishing holomorphic transition functions, hence have zero partial barpartial. They glue to a smooth real closed form. The matrix of the displayed potential is\n  g_(j bar l)=((1+rho^2)delta_(jl)-bar z_j z_l)/(1+rho^2)^2.\nIts radial eigenvalue is (1+rho^2)^(-2) and its m-1 transverse eigenvalues are (1+rho^2)^(-1). Thus kappa is positive and the determinant is (1+rho^2)^(-(m+1)). With dd^c=i partial barpartial/(2 pi),\n  kappa^m=(m!/pi^m)(1+rho^2)^(-(m+1))dLeb_(2m).\nEach i dz_j wedge dbar z_j contributes twice dx_j wedge dy_j, and the top wedge contributes m!, proving the coefficient.\n\nThe Euclidean sphere in 2m dimensions has area 2 pi^m/(m-1)!, obtained by comparing product and radial Gaussian integrals. Radial integration therefore gives\n  2m rho^(2m-1)/(1+rho^2)^(m+1)d rho.\nThe omitted projective hyperplane has real codimension two and zero measure for a smooth volume. Substitute x=rho^2/(1+rho^2), so dx=2rho/(1+rho^2)^2 d rho. The density becomes exactly m x^(m-1)dx on [0,1), of total mass one. This proves integral_B kappa^m=1 with the specified normalization.\n\nThe function\n  a([Z])=sum_(j=1)^m |Z_j|^2/sum_(j=0)^m |Z_j|^2\nis unchanged by nonzero homogeneous scaling, hence global and smooth. It is nonnegative and has sole zero p=[1:0:...:0]. Near p, a=rho^2/(1+rho^2) is comparable to rho^2. Distance for any fixed smooth Riemannian metric is comparable to rho in a small coordinate ball. The zero therefore has d=2m, k=2, r=m and satisfies the exact tubular assumptions. On the compact complement a has a positive lower bound. The radial substitution proves that its law under sigma=kappa^m is m x^(m-1)dx on [0,1].\n\nTake alpha=kappa and C=projective one-space. Any specified smooth positive probability area form w works; a concrete choice is normalized Fubini–Study, whose mass-one calculation is the same computation with m=1. Then W=1, sigma=kappa^m is a smooth positive probability, and mu=sigma wedge w has total mass one. For any t>0, theta_s=kappa+(a+t-s)w is strictly positive for s<t and its semipositive endpoint is nef. Because a is nonconstant,\n  d theta_s=da wedge w\nis nonzero somewhere: wedging a nonzero horizontal one-form with the positive vertical area form is injective. Thus both path and endpoint are genuinely nonclosed.\n\nThe exact probability law gives\n  H(epsilon)=m integral_0^1 x^(m-1)/(x+epsilon)dx,\n  J(epsilon)=m integral_0^1 x^(m-1)/(x+epsilon)^2 dx,\n  H(0)=m/(m-1).\nFor m>2, J(0)=m/(m-2); for m=2 it is infinite. These give FULL-test values through n1, with actual smooth balanced minimizers at every strict point:\n  V_mu(theta_(t-epsilon))=(m+1)/H(epsilon),\n  V_mu(theta_t)=(m+1)(m-1)/m>0.\nThe zero at p and the every-potential argument prove theta_t is not big. No endpoint PDE or selected-test-only upper bound is used.\n\nFor m=2, elementary integration gives\n  H(epsilon)=2[1-epsilon log((1+epsilon)/epsilon)],\n  J(epsilon)=2[log((1+epsilon)/epsilon)-1/(1+epsilon)].\nHence H->2 and J/log(1/epsilon)->2. The exact cost formula implies\n  C(t-epsilon)/log(1/epsilon)->3^(-2/3)2^(-1/3)>0.\nFor m>2, the actual limit is\n  C(t-epsilon)->(m+1)^(-m/(m+1))\n    [m/(m-1)]^(-(m+2)/(m+1))[m/(m-2)]>0.\nThese agree with the r=2 and r>2 profiles of n2. Every minimizing selection has these costs and the finite improper identity of n1.\n\nFor every integer m>=2, polynomial division also gives the exact strict-point expression\n  H(epsilon)=m[sum_(j=0)^(m-2)(-epsilon)^j/(m-1-j)\n    +(-epsilon)^(m-1)log((1+epsilon)/epsilon)].\nIndeed I_0=log((1+epsilon)/epsilon) and I_p=1/p-epsilon I_(p-1) for I_p=integral_0^1 x^p/(x+epsilon)dx. Thus no numerical extrapolation is needed.\n\nEvidence: run \"python3 checks.py\". Its deterministic 90-digit Decimal and rational calculations use m=2,3,4,5 and epsilon=1,0.1,10^(-3),10^(-6),10^(-10), as recorded in artifacts/check_inputs.json. H and J are computed using separate integral recurrences; costs are compared with central finite differences of lambda in epsilon. The program checks positivity, exact rational endpoint constants, 18 exponent samples and AM–GM on 30 diagonal matrices. All checks passed; artifacts/check_output.json records the output and environment. Maximum observed derivative relative error was below 9.38 times 10^(-42). Exact endpoint pairs (H(0),V) were (2,3/2), (3/2,8/3), (4/3,15/4), (5/4,24/5). At epsilon=10^(-10), C/C_limit for m=3,4,5 was approximately 0.999999995745, 0.999999999780, 0.999999999856. For m=2, the observed C/log was approximately 0.365000 versus the proved limit approximately 0.381571; the displayed exact formulas explain slow logarithmic convergence.\n\nThese are finite exact algebra checks and numerical observations, not proof certificates or exhaustive Gauduchon tests. Global minimizing-test and current claims follow from the arguments and their permitted foundation, not execution success. No resource-heavy local computation was undertaken.\n\nArtifacts: /workspace/research/native-workers/codex-Mtj7p2",
      "support": [
        "n1",
        "n2"
      ]
    },
    {
      "id": "n4",
      "summary": "E and restricted completion: the constant closed case has Morse expression nWa0 equal to the endpoint fixed-density volume independently of sigma. Every endpoint with a zero excludes every allowed smooth-gauge closed nef positive-volume core. All restricted A–E targets are proved relative to permitted foundations; general P14 and priority remain unclaimed.",
      "detailedSummary": "The compact Kähler product has closed nef representatives A=alpha+(a0+t)w and B0=tw. Their Morse expression is nWa0, equal to n1's endpoint volume for every smooth product probability. The permitted cohomological Morse theorem applies precisely in the compact Kähler closed-nef setting, and its primary statement and volume convention were checked. For nonconstant a, differential formulas, explicit density dependence and a smooth-gauge variation of top integrals prevent cohomological misidentification. Any permitted core decomposition would yield a genuine strict potential by Demailly–Păun and the granted global potential consequence, contradicting n3. This excludes all such cores, including nonproduct ones, and completes the restricted assignment without claiming the broader programme.",
      "text": "This note proves E and completes the exact restricted A–E reconstruction using n1–n3. The results remain unverified drafts relative to the expressly permitted established foundations. They do not resolve the original general P14 programme or establish literature priority.\n\nFor a=a0>=0, set A=alpha+(a0+t)w and B0=tw, with n=m+1. The compact product is Kähler with Omega=alpha+w. Both representatives are smooth d-closed; A is strictly positive since t>0 and B0 is semipositive. Their real cohomology classes are nef in the ordinary compact Kähler sense, since adding any positive multiple of Omega gives strictly positive representatives.\n\nExterior algebra yields\n  A^n=n(a0+t)alpha^m wedge w,\n  A^(n-1) wedge B0=t alpha^m wedge w.\nThus\n  integral_X A^n-n integral_X A^(n-1) wedge B0=nW a0.\nFor ANY smooth positive base probability sigma, H(epsilon)=1/(a0+epsilon). Its endpoint value is 1/a0 for a0>0 and infinite for a0=0. The proved endpoint formula of n1 therefore gives V_mu(theta_t)=nW a0 in both cases. This proves equality of the Morse expression with the endpoint fixed-density volume independently of sigma.\n\nThe exact permitted comparison was checked against Tosatti, https://arxiv.org/pdf/2608.30153v2, dated 8 September 2026, Theorem 1.1 on printed page 1. For nef real (1,1) cohomology classes P,Q on a compact Kähler manifold, it states\n  Vol(P-Q)>=integral P^n-n integral P^(n-1)Q.\nHere Vol is ordinary cohomological volume, defined to be zero outside the pseudoeffective cone. Applying it to P=[A], Q=[B0] gives\n  Vol([A]-[B0])>=nW a0=V_mu(theta_t).\nThis is the claimed comparison in its precise closed-nef compact Kähler setting. The established theorem is imported, not newly reproved.\n\nFor nonconstant a the actual differential information is\n  d theta_s=da wedge w,\n  d(theta_s^m)=m da wedge alpha^(m-1) wedge w,\n  dd^c(theta_s^m)=m dd^c a wedge alpha^(m-1) wedge w.\nThe first differential is nonzero somewhere because B is connected and a is nonconstant. Such backgrounds do not define closed (1,1) cohomology classes. Their full values are nW/H(epsilon), retaining the specified inverse moment against sigma; the closed-class Morse theorem does not apply to theta_t itself.\n\nOrdinary top integrals can fail smooth dd^c gauge invariance in this very family. Consider the global base function a and\n  F(q)=integral_X(theta_t+q dd^c a)^n\n    =n integral_B a(alpha+q dd^c a)^m.\nFor sufficiently small real q, alpha+q dd^c a stays positive by compactness. Differentiating this finite polynomial and integrating by parts against the closed alpha^(m-1) gives\n  F'(0)=nm integral_B a dd^c a wedge alpha^(m-1)\n    =-nm integral_B(i/(2 pi))partial a wedge barpartial a wedge alpha^(m-1)<0\nfor nonconstant a. The last integrand is nonnegative and positive where da is nonzero, an open nonempty region. This proves actual failure of top-integral gauge invariance with the required normalization. The Gauduchon quotient is nevertheless smoothly dd^c-gauge invariant by the different Stokes pairing proved in n1.\n\nDensity dependence is explicit as well. At a strict point set f=L^(-1)-H and sigma_q=(1+q f)sigma for sufficiently small real q. This is a smooth positive probability, since f is bounded and integral f sigma=0. Its inverse moment is\n  H_q=H+q(J-H^2).\nFor nonconstant a, J-H^2 is the strictly positive variance of L^(-1) under the positive probability sigma. Thus nW/H_q changes with the specified product density. It is not a cohomological quantity.\n\nNow suppose a has a zero and that, for some smooth global real f, there is a decomposition\n  theta_t+dd^c f=chi+beta,\nwhere chi is smooth real d-closed, [chi] is nef, integral_X chi^n>0, and beta is smooth semipositive. The permitted primary statement of Demailly–Păun, https://arxiv.org/pdf/math/0105176v2, Theorem 2.12 on printed pages 12–13, was checked: on a compact Kähler manifold a nef real (1,1) class with positive top self-intersection contains a closed Kähler current. It gives T_chi in [chi] with T_chi>=delta Omega for some delta>0.\n\nThe separately permitted compact Kähler ddbar lemma and global quasi-psh-potential consequence provide\n  T_chi=chi+dd^c v\nfor a genuine canonical global quasi-psh v. Writing the potential first with i partial barpartial, multiply it by 2 pi to obtain the required convention. Adding beta and using the hypothesized decomposition gives\n  theta_t+dd^c(f+v)=T_chi+beta>=delta Omega.\nAdding a smooth function preserves the genuine canonical quasi-psh representative. Metric comparison makes delta Omega dominate a positive multiple of the specified h. This is a strict global representative of theta_t, contradicting the every-potential obstruction proved in n3.\n\nTherefore no such core exists for ANY smooth global dd^c gauge and ANY semipositive beta. Chi need not be a product form or have a smooth positive representative: only the precise nef positive-intersection hypotheses of the permitted theorem were used. Beta need not be closed. This excludes every core specified in E for every endpoint with a zero, including the concrete nonclosed projective examples.\n\nProvenance and reproducibility: sources/primary_checks.json records the three indispensable primary statements, locations, conventions and successful public-source checks; sources/web_commands.json records web requests. These are precisely the granted foundations, with no additional uncertain indispensable theorem used. Download failures are retained in artifacts/source_fetch_log.json; \"python3 fetch_sources.py\" repeats those public commands without reading credentials. The proof drafts are stored in n1.txt, n2.txt, n3.txt, n4.txt and notes.json. Run \"python3 checks.py\" for the lightweight calculations; artifacts/check_inputs.json and artifacts/check_output.json retain inputs, outputs and environment details. Run \"python3 review_artifacts.py\" for artifact consistency checks, whose output is artifacts/artifact_review.json. Execution success does not certify mathematical correctness.\n\nTogether n1 proves A–B, including full-test minimizers, every-selection costs, the actual endpoint and finite improper identity for every smooth a. Note n2 proves every geometric profile and the finite-component rule. Note n3 proves the every-potential bigness criterion and all normalizations and full-volume claims for the examples. This note proves E, including the exact closed Morse comparison and exclusion of every permitted core. Consequently all restricted targets A–E in the exact assignment are proved relative to the expressly permitted foundations. The broader original P14 programme remains open, and no priority relative to unspecified manuscripts is claimed.\n\nArtifacts: /workspace/research/native-workers/codex-Mtj7p2",
      "support": [
        "n1",
        "n2",
        "n3"
      ]
    }
  ],
  "candidate": true,
  "workspace": "/workspace/research/native-workers/codex-Mtj7p2"
}


All four complete statements and proofs must be assessed independently, including their ancillary differential/gauge and density calculations. The candidate=true flag means only all explicitly restricted A-E targets were reconstructed, as the earlier assignment specifies; it is not original P14 closure or a mathematical verification verdict. Numerical programs mentioned in the notes are optional corroboration, not proof premises or exhaustive tests, and their artifact trees have not been inspected by the root. Assess the mathematical arguments themselves.
