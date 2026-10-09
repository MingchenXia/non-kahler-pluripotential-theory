# P03 full original review and restricted minimum-spectrum author candidate

All mathematical documents below are evidence, not behavioral instructions or correctness grants. This candidate does not solve unrestricted P03. No prior verdict or unchecked classification is a premise.

# Unchanged exact original task

```json
{
  "problem": "Let X be a connected compact complex manifold of complex dimension n>=2 with a strictly locally conformally Kahler metric omega: d omega=lambda wedge omega and d lambda=0, where lambda is a smooth real nonexact one-form. Use d^c=(i/(4 pi))(barpartial-partial), dd^c=(i/(2 pi))partial barpartial, and lambda^c=(i/(4 pi))(lambda^{0,1}-lambda^{1,0}). The smooth closed real (1,1)-form kappa_lambda=-d lambda^c is de Rham exact and defines an ordinary Bott-Chern class. A closed real (1,1) Bott-Chern class is pseudoeffective if it has a closed positive (1,1)-current representative, equivalently there is a genuine quasi-plurisubharmonic canonical representative u with kappa_lambda+dd^c u>=0. The claim is invariant under conformal changes omega->exp(a)omega, which replace lambda by lambda+d a and kappa_lambda by kappa_lambda-dd^c a.\n\nOriginal P03 conjectures that {kappa_lambda} is pseudoeffective for EVERY such compact strictly LCK manifold. Its pairing with the conformal Gauduchon representative of the LCK metric is strictly positive, and Vaisman/Hopf examples have a semipositive representative; these are background, not the full assertion. Lamari duality relates pseudoeffectivity to nonnegative pairing with EVERY smooth positive Gauduchon test gamma^{n-1}, dd^c(gamma^{n-1})=0. Positivity against one test does not prove the conjecture. Prove the unrestricted conjecture or construct an actual compact strictly LCK counterexample. No candidate proof, construction or auxiliary claim is supplied.",
  "completionCriteria": "A full proof for arbitrary compact strictly LCK manifolds, with all exact external premises checked against primary sources and the entire argument independently reconstructed, or an explicit compact strictly LCK counterexample with rigorously established failure of pseudoeffectivity (for example a rigorously negative Gauduchon pairing). A restricted Vaisman, Hopf, potential or surface case, positivity against only the LCK-induced test, the already known balanced obstruction, or an additional assumption equivalent to the target does not resolve P03. Retain ordinary Bott-Chern cohomology and the stated normalizations; de Rham exactness does not imply Bott-Chern triviality."
}
```

# Proposed statement-only restricted A--F

# P03 limited minimum-spectrum targets, independent statements

These are restricted statements, not a solution of the original P03
conjecture. Let X be connected compact complex, n>=2, with a smooth
positive strictly LCK omega, d omega=lambda wedge omega, d lambda=0,
[lambda]!=0. Use exactly d^c=i(barpartial-partial)/(4pi),
lambda^c=i(lambda01-lambda10)/(4pi), kappa=-d lambda^c,
and ordinary wedge powers. All fields and corrections are smooth.

A. Kappa is real closed (1,1), de Rham exact, and nonzero as an
ordinary Bott-Chern class. Under omega->exp(a)omega its Lee curvature
changes to kappa-ddc a, preserving the class and nonexact Lee class.

B. Put Q=lambda wedge lambda^c. For each 1<=k<=n,
int kappa^k omega^(n-k)=(n-k)int Q kappa^(k-1) omega^(n-k).
In particular int kappa omega^(n-1)>0 and int kappa^n=0.
Where eta_t=omega+t kappa is positive, its actual volume polynomial
has degree at most n-1 and derivative
n(n-1)int Q omega eta_t^(n-2)>0. No Gauduchon hypothesis on omega
or eta_t is added.

C. If ONLY the LEAST eigenvalue of kappa relative to omega is
constant on X, then kappa itself is semipositive, the least eigenvalue
equals zero everywhere, and its ordinary Bott-Chern class is nonzero
and pseudoeffective. Constancy of the other eigenvalues and of rank
is not assumed. Pairing against EVERY positive Gauduchon test is
nonnegative. If the whole relative spectrum is constant, rank is
constant between1 and n-1. In particular the conclusion applies to
EVERY ACTUAL compact quotient Gamma backslash G with invariant
complex structure and invariant strictly LCK tensors. No lattice
existence or abstract-Lie-algebra classification is asserted. Every
invariant Hermitian metric on such an actual quotient is Gauduchon.

D. For every n>=2 and 0<epsilon<1, the Hopf quotient of C^n minus0
by z->z/2 is compact connected and supports
rho=sum|zj|^2, Phi=rho+epsilon Re(z1^2), Omega=ddc Phi=ddc rho,
omega=Omega/Phi, lambda=-d log Phi. The tensors descend, omega is
positive strictly LCK and the Lee period is2log2. Its kappa=ddc log
Phi has relative eigenvalues -epsilon,1,...,1 at(1,0,...,0).
The smooth bounded deck-invariant u=log rho-log Phi gives the
actual semipositive closed representative kappa+ddc u=ddc log rho.
Thus this is not a counterexample to the original conjecture.

E. In this example write z1=x+iy, R=sum_(j>1)|zj|^2.
The relative spectrum consists of n-1 ones and
h=epsilon((1-epsilon)y^2-(1+epsilon)x^2)/Phi, in[-epsilon,epsilon].
The first positive volume-ray boundary is t0=1/epsilon. There
1+h/epsilon=(2(1-epsilon)y^2+R)/Phi; degeneracy occurs only on the
real z1 rays with other coordinates0, and the actual total volume
remains positive. The constant-spectrum degeneration argument
therefore does not establish unrestricted pseudoeffectivity.

F. On the SAME scalar Hopf quotient in EVERY n>=2, set s=sum|zj|^2,
q=|z1|^2, Psi=s+epsilon*q^2/s, Omega_epsilon=ddc Psi,
omega_epsilon=Omega_epsilon/s and lambda=-d log s, for EVERY
0<epsilon<1. These are actual smooth strictly LCK tensors descending
to the compact quotient, with Omega_epsilon>=(1-epsilon)ddc s>0
and nonexact Lee form of period2log2. Their curvature is ddc log s,
semipositive of rank n-1, with least relative eigenvalue identically
zero. At(1,0,...,0) the remaining spectrum consists of n-1 copies
of1/(1-epsilon); at(0,1,0,...,0) it consists of n-1 ones. Hence the
remaining spectrum is genuinely nonconstant for EVERY epsilon>0.
This demonstrates that C's hypothesis is strictly weaker than
constant entire spectrum. It is not a counterexample to P03.

Use only these statements and public mathematical sources for blind
reconstruction. No author article, proof, earlier report or private
campaign material is supplied. All A--F require complete ordinary
proofs. Numerical checks, prior candidate flags, one Gauduchon test,
known classification, invariant-only calculations or a noncompact
negative Lie algebra do not substitute for these conclusions.

# Entire current four-page standalone proof

```latex
\documentclass[11pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\dc}{d^c}
\newcommand{\kap}{\kappa_\lambda}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Lee curvature with constant minimum spectrum\newline
on compact locally conformally K\"ahler manifolds}
\author{}\date{}
\begin{document}\maketitle
\noindent\textbf{Working draft.} Complete independent review and
reconstruction are pending. The unrestricted P03 conjecture is not
resolved here.
\begin{abstract}
We prove that a compact strictly locally conformally K\"ahler metric
whose Lee curvature has constant least relative eigenvalue has
semipositive Lee curvature. The least eigenvalue is necessarily zero. The proof uses a strictly increasing volume polynomial
and compact Stokes, and applies in particular to compact quotients
with invariant LCK tensors. An explicit compact family has constant
least eigenvalue and nonconstant remaining spectrum, so the condition
is strictly weaker than constant spectrum. No classification is used. We give an explicit compact Hopf metric with indefinite
Lee curvature and a smooth correction to a semipositive representative.
In that example the first degeneracy of the volume ray leaves positive
total volume, explaining the limitation of the constant-spectrum
argument. All statements retain ordinary Bott--Chern cohomology.
\end{abstract}

\section{Conventions and the restricted statement}
Let $X$ be connected compact complex of dimension $n\geq2$. A smooth
positive real $(1,1)$ form $\omega$ is strictly LCK when
\[
 d\omega=\lambda\wedge\omega,\qquad d\lambda=0,
 \qquad [\lambda]\ne0\text{ in }H^1_{\rm dR}(X,\mathbb R).
\]
Use ordinary wedge powers and
\[
 \dc=\frac{i}{4\pi}(\bar\partial-\partial),\qquad
 \ddc=\frac{i}{2\pi}\partial\bar\partial,\qquad
 \lambda^c=\frac{i}{4\pi}(\lambda^{0,1}-\lambda^{1,0}),
 \qquad\kap=-d\lambda^c.
\]
Locally $\lambda=df$, so $\kap=-\ddc f$. Thus $\kap$ is smooth,
real, closed and of type $(1,1)$, and is de Rham exact. Its ordinary
Bott--Chern class need not vanish. Pseudoeffectivity means existence
of a closed positive current in that class.

\begin{theorem}\label{th:constant}
Suppose the LEAST eigenvalue of $\kap$ relative to $\omega$ is
constant on $X$. Then $\kap$ is semipositive, its least eigenvalue
equals zero, and its ordinary Bott--Chern class is nonzero and
pseudoeffective. No constancy of the other eigenvalues or of the
rank is assumed.

If the entire spectrum is constant, the rank is constant in
$\{1,\ldots,n-1\}$. In particular the conclusion applies to any
actual compact quotient $\Gamma\backslash G$ with left-invariant
complex structure and left-invariant strictly LCK tensors
$\omega,\lambda$.
\end{theorem}

The minimum-spectrum hypothesis is a condition on this metric and
its Lee form, rather than merely on the complex manifold. The
unrestricted assertion for every compact strictly LCK manifold is
the conjecture recorded in \cite[Conjecture 5.13]{OV}. Neither a
single positive Gauduchon pairing nor the restricted theorem proves
that assertion. No literature priority is claimed.

\section{Compact Stokes and the volume ray}
The two-form
\[
 Q=\lambda\wedge\lambda^c
   =\frac{i}{2\pi}\lambda^{1,0}\wedge\lambda^{0,1}
\]
is semipositive and is nonzero on an open set. The latter follows
because the nonexact smooth form $\lambda$ is not identically zero.

\begin{lemma}\label{lem:stokes}
For $1\leq k\leq n$ one has
\[
 \int_X\kap^k\wedge\omega^{n-k}
  =(n-k)\int_X Q\wedge\kap^{k-1}\wedge\omega^{n-k}.
\]
Consequently
\[
 \int_X\kap\wedge\omega^{n-1}>0,\qquad
 \int_X\kap^n=0.
\]
The ordinary Bott--Chern class of $\kap$ is nonzero.
\end{lemma}
\begin{proof}
Use $d\kap=0$, $d\lambda^c=-\kap$ and
$d\omega^j=j\lambda\wedge\omega^j$. Differentiation gives
\[
 d(\lambda^c\wedge\kap^{k-1}\wedge\omega^{n-k})
 =-\kap^k\wedge\omega^{n-k}
   +(n-k)Q\wedge\kap^{k-1}\wedge\omega^{n-k}.
\]
Integration and smooth Stokes prove the identity. For $k=1$, the
right side is strictly positive since $n\geq2$, $\omega$ is positive
and $Q$ is nonzero on an open set. For $k=n$ it is zero.

If $\kap=\ddc a$ for a smooth real global $a$, the conformal LCK
metric $e^a\omega$ has Lee form $\lambda+da$ and zero Lee curvature.
Its Lee form remains nonexact. Applying the positive $k=1$ identity
to this metric is a contradiction. This concerns ordinary
Bott--Chern exactness, rather than de Rham exactness.
\end{proof}

\begin{proposition}\label{prop:ray}
On the interval where $\eta_t=\omega+t\kap$ is positive, the
polynomial $V(t)=\int_X\eta_t^n$ has degree at most $n-1$ and
\[
 V'(t)=n(n-1)\int_X Q\wedge\omega\wedge\eta_t^{n-2}>0.
\]
No Gauduchon condition on $\omega$ or $\eta_t$ is assumed.
\end{proposition}
\begin{proof}
Since $d\eta_t=d\omega=\lambda\wedge\omega$, smooth Stokes gives
\[
 0=\int_X d(\lambda^c\wedge\eta_t^{n-1})
  =-\int_X\kap\wedge\eta_t^{n-1}
    +(n-1)\int_X Q\wedge\omega\wedge\eta_t^{n-2}.
\]
Differentiating the finite wedge polynomial proves the formula.
All factors in the final integral are positive or semipositive,
and it is strictly positive on the open set where $\lambda\ne0$.
Lemma~\ref{lem:stokes} makes its top coefficient
$\int_X\kap^n$ vanish.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{th:constant}]
Let $r$ be the constant least relative eigenvalue. If $r<0$, put
$t_0=-1/r>0$. For $0\leq t<t_0$ the form
$\eta_t=\omega+t\kap$ is positive. At $t_0$ it is semipositive
and has a kernel at EVERY point, independently of the other
eigenvalues. Thus $V(t_0)=0$. Proposition~\ref{prop:ray} and
polynomial continuity instead give $V(t_0)\geq V(0)>0$.
This contradiction gives $r\geq0$ and pointwise semipositivity.

The continuous top power $\kap^n$ is now nonnegative and has zero
integral by Lemma~\ref{lem:stokes}. It vanishes identically. Thus
the least eigenvalue is zero at every point. The same lemma proves
that the ordinary Bott--Chern class is nonzero, while $\kap$ itself
is its closed positive representative.

If all eigenvalues are constant, the rank is constant. It cannot
be zero, and cannot be $n$, hence lies between one and $n-1$.
For invariant tensors on an actual compact quotient, the relative
matrix is constant in a left-invariant frame. No lattice existence
for an abstract Lie algebra is inferred from this calculation.
\end{proof}

\begin{remark}
Every invariant Hermitian metric $\gamma$ on such a compact quotient
is Gauduchon: $\ddc\gamma^{n-1}$ is an invariant top form, hence a
constant multiple of the invariant volume. Smooth Stokes makes
that constant zero. The theorem uses pointwise semipositivity of
$\kap$, so it controls pairings against all positive Gauduchon
tests, including those which are not invariant.
\end{remark}

\section{An indefinite Hopf representative and its correction}
Fix $0<\varepsilon<1$, and on $\mathbb C^n\setminus\{0\}$ put
\[
 \rho=\sum_{j=1}^n|z_j|^2,\qquad
 \Phi=\rho+\varepsilon\operatorname{Re}(z_1^2),\qquad
 \Omega=\ddc\Phi=\ddc\rho>0.
\]
The bounds $(1-\varepsilon)\rho\leq\Phi\leq(1+\varepsilon)\rho$
make $\Phi$ positive. The action $g(z)=z/2$ is free and properly
discontinuous. Polar coordinates show that its quotient $X$ is
connected compact, with a fundamental interval of logarithmic radii.
Both $\Phi$ and $\Omega$ scale by $1/4$ under $g$. Therefore
\[
 \omega=\Omega/\Phi,\qquad \lambda=-d\log\Phi
\]
descend and satisfy $d\omega=\lambda\wedge\omega$. The Lee period
along the quotient loop lifted from $z$ to $z/2$ is $2\log2$, so this
is a strictly LCK metric. Its Lee curvature is $\kap=\ddc\log\Phi$.

Writing $F_i=\bar z_i+\varepsilon z_1\delta_{i1}$, its complex
Hessian is
\[
 H_{i\bar j}=\frac{\delta_{ij}}\Phi-
                   \frac{F_i\overline{F_j}}{\Phi^2}.
\]
At $(1,0,\ldots,0)$ the diagonal entries are
$-\varepsilon/(1+\varepsilon)$ and $1/(1+\varepsilon)$ in the
remaining directions. Relative to $\omega$, its eigenvalues there
are $-\varepsilon,1,\ldots,1$. Thus this metric has indefinite Lee
curvature; a positive strictly psh automorphic potential can have
a logarithm which is not psh.

Nevertheless the smooth bounded deck-invariant function
\[
 u=\log\rho-\log\Phi
\]
descends and gives
\[
 \kap+\ddc u=\ddc\log\rho\geq0.
\]
Indeed the Hessian of $\log\rho$ is
$\delta_{ij}/\rho-\bar z_i z_j/\rho^2$, semipositive by
Cauchy--Schwarz. This is an actual smooth semipositive representative
of the ordinary Bott--Chern class. The example is not a
counterexample to pseudoeffectivity.

To examine its first volume-ray boundary, write $z_1=x+iy$ and
$R=\sum_{j>1}|z_j|^2$. The remaining relative curvature eigenvalue is
\[
 h=\frac{\varepsilon((1-\varepsilon)y^2-(1+\varepsilon)x^2)}
            {(1+\varepsilon)x^2+(1-\varepsilon)y^2+R},
 \qquad -\varepsilon\leq h\leq\varepsilon.
\]
The other $n-1$ eigenvalues are one. Hence the first positive-ray
boundary is $t_0=1/\varepsilon$. At this boundary
\[
 1+h/\varepsilon=
 \frac{2(1-\varepsilon)y^2+R}{\Phi}.
\]
It vanishes only on the real $z_1$ rays with $z_j=0$ for $j>1$.
The top power of $\eta_{t_0}$ is positive on a nonempty open set,
so its total volume is positive. First degeneracy on a general
compact LCK manifold therefore need not collapse the total volume.

\begin{remark}
The proof of the restricted theorem uses a globally constant least
eigenvalue to force degeneration everywhere at one parameter. The Hopf
calculation explains why that step does not prove the unrestricted
conjecture. No classification, all-cover construction, unbounded
potential assertion or literature priority is established here.
\end{remark}

\section{Constant minimum with genuinely variable remaining spectrum}
The weaker hypothesis is nonvacuous beyond constant spectrum.
On the SAME scalar Hopf quotient, put $s=\rho$, $q=|z_1|^2$,
and, for any $0<\varepsilon<1$, define
\[
 \Psi=s+\varepsilon\frac{q^2}{s},\qquad
 \Omega_\varepsilon=\ddc\Psi,\qquad
 \omega_\varepsilon=\Omega_\varepsilon/s,\qquad
 \lambda=-d\log s.
\]
Here $\Psi$ is smooth on the punctured space and scales by $1/4$
under $z\mapsto z/2$. Let $a=q/s\in[0,1]$, and use subscripts
for complex derivatives. Direct differentiation gives
\[
 \left(\frac{q^2}{s}\right)_{i\bar j}
 =\frac{2}{s}(q_i-a s_i)(q_{\bar j}-a s_{\bar j})
       +2a\,\delta_{i1}\delta_{j1}-a^2\delta_{ij}.
\]
The first two matrix terms are positive semidefinite, so the
complex Hessian is at least $-I$. Consequently
$\Omega_\varepsilon\geq(1-\varepsilon)\ddc s>0$.
This is an actual positive closed automorphic form, not merely
an algebraic assignment of eigenvalues. The form
$\omega_\varepsilon$ descends to the compact quotient, with
$d\omega_\varepsilon=\lambda\wedge\omega_\varepsilon$.
The Lee period remains $2\log2$, proving strict LCK.

Its Lee curvature is $\kap=\ddc\log s$. This is semipositive
of rank $n-1$, so the least relative eigenvalue is identically
zero for every member of this family. At $z=(1,0,\ldots,0)$
the complex Hessian of $q^2/s$ is
$\operatorname{diag}(1,-1,\ldots,-1)$, and the relative
curvature spectrum is
\[
 0,\ (1-\varepsilon)^{-1},\ldots,(1-\varepsilon)^{-1}.
\]
At $z=(0,1,0,\ldots,0)$, $q^2/s$ vanishes to fourth order,
so its complex Hessian is zero. The relative spectrum there
is $0,1,\ldots,1$. Thus the remaining spectrum is genuinely
nonconstant for every $\varepsilon>0$, in every $n\geq2$.
The constant-minimum condition is strictly weaker than requiring
all eigenvalues constant. This is a sufficiency example, not a
counterexample to the unrestricted conjecture.

\paragraph{Verification boundary.}
The original compact strictly LCK hypotheses and ordinary
Bott--Chern class are retained. The minimum-spectrum theorem
and both compact families above are new unverified author
statements requiring independent reconstruction. The earlier
constant-spectrum working draft and its frozen review inputs
are preserved; they are not correctness grants. No unrestricted
P03 closure or literature priority is asserted.

\begin{thebibliography}{9}
\bibitem{OV} L. Ornea and M. Verbitsky,
\emph{The Lee--Gauduchon cone on complex manifolds},
\href{https://arxiv.org/abs/2411.05595v2}{arXiv:2411.05595v2},
Conjecture 5.13 (problem context).
\end{thebibliography}
\end{document}
```

# Exact primary conjecture context, not a theorem import

Source https://arxiv.org/pdf/2411.05595v2; actual LF505--570. Conjecture5.13 is the historical problem context. Theorem5.11, classifications, deformations, all-cover constructions and broader source arguments are NOT proof premises. The source differently scaled d-c changes the Lee curvature by a positive factor, preserving pseudoeffectivity. The entire source and a worldwide current-open-status claim are not certified.

```text
class [ω] ∈ HBC   (M ) of this form is pseudoeffective, and it is exact, because
   2
H (M ) = 0. Moreover, [ω] 6= 0, because a plurisubharmonic function on
a compact manifold is constant. Therefore, M is not strongly Gauduchon;
however, the Lee-Gauduchon cone of M is trivial, because H 5 (M, R) = 0.

Remark 5.8: We obtained that for a Calabi-Eckmann manifold, the cone
of positive exact (1,1)-currents and the cone of positive (1,1)-currents with
Bott–Chern cohomology classes in dc (H 1 (M )) are distinct.

5.2   LCK manifolds
Definition 5.9: A Hermitian manifold of complex dimension > 1 (M, I, g, ω)
is called locally conformally Kähler (LCK) if there exists a closed 1-form
θ such that dω = θ ∧ ω. The 1-form θ is called the Lee form.

Remark 5.10: We recall that all known compact LCK manifolds belong to
one of three classes: blow-ups of LCK with potential, blow-ups of Oeljeklaus–
Toma and Kato manifolds. We refer to [OV1] for LCK geometry.

   Recently, we proved the following result:

Theorem 5.11: ([OV3]) Let (M, ω, θ) be a compact LCK manifold in any
of these classes. Then dc θ is exact pseudoeffective.

Corollary 5.12: For a compact LCK manifold in any of the above classes,
LG(M ) 6∋ 0 and M does not admit a strongly Gauduchon metric.



                                    – 11 –                    version 2.0, Nov. 14, 2024
L. Ornea, M. Verbitsky                              The Lee–Gauduchon cone



   This leads to the following conjecture which was the starting point for
writing this note:

Conjecture 5.13: The two-form dc θ is pseudoeffective on all compact LCK
manifolds.

   The Lee-Gauduchon cone for these three classes of LCK manifolds can
be computed explicitly.

   The following proposition was proven in [OV2].

Proposition 5.14: Let (M, ω, θ) be an LCK manifold with potential ([OV1]).
Then H 1 (M, C) = Hd1,0 (M ) ⊕ Hd1,0 (M ) ⊕ hθi.
   Proof: [OV2, Theorem 6.1]

    From this theorem it is clear that dim W = 1, and since dc θ is pseudo-
effective on any LCK manifold with potential, its Lee-Gauduchon cone is a
half-line {x ∈ W | hx, θi > 0}.
    The same is true for any Kato manifold M ([IOP, IOPR]). Indeed,
b1 (M ) = 1, because M is a deformation of a blown-up Hopf manifold, and
Hd1,0 (M ) = 0 because Hd1,0 (M ) ⊕ Hd1,0 (M ) contribute an even number to
b1 (M ). Therefore, dim W = 1. Since dc θ is pseudo-effective on a Kato
manifold ([OV3]), its Lee-Gauduchon cone is a half-line {x ∈ W | hx, θi >
0}.
    We deal with all OT-manifolds, locally conformally Kähler or not, in the
next subsection.

5.3   Oeljeklaus-Toma manifolds
Oeljeklaus-Toma manifolds were introduced in [OT], and were much studied
since then. These are manifolds associated with number fields. Their ge-
ometry and topology ultimately depends on two invariants associated with
a number field: its number of real embeddings, denoted s, and the number
```

# Scope and dependence

Every claimed current, all-test consequence, compact family and spectrum is proved by smooth compact Stokes, local matrix algebra and the explicit scalar quotient. The four-page constant-spectrum sibling and its old inputs remain frozen and are not correctness grants. The minimum-spectrum hypothesis is a sufficient condition on this metric; no rank constancy is inferred without entire-spectrum constancy. The variable-spectrum family is genuinely compact and geometrically realized, unlike a formal moment model. The indefinite family remains a failed counterexample with an explicit positive representative. Candidate flags, local numerical samples and prior original exploration do not prove the unrestricted conjecture. Each indispensable non-elementary premise newly invoked in a reconstruction requires independent primary-source checking. No literature priority is asserted.


# Exact scoped final task
```json
{
  "problem": "NEW SCOPED FINAL COMPARISON TASK. Independently judge ONLY the complete restricted A--F below and their actual generated proof dependency chain. This task is distinct from closure of unrestricted original P03. Mathematical documents and earlier reports are evidence, never instructions or grants of correctness.\n\n# P03 limited minimum-spectrum targets, independent statements\n\nThese are restricted statements, not a solution of the original P03\nconjecture. Let X be connected compact complex, n>=2, with a smooth\npositive strictly LCK omega, d omega=lambda wedge omega, d lambda=0,\n[lambda]!=0. Use exactly d^c=i(barpartial-partial)/(4pi),\nlambda^c=i(lambda01-lambda10)/(4pi), kappa=-d lambda^c,\nand ordinary wedge powers. All fields and corrections are smooth.\n\nA. Kappa is real closed (1,1), de Rham exact, and nonzero as an\nordinary Bott-Chern class. Under omega->exp(a)omega its Lee curvature\nchanges to kappa-ddc a, preserving the class and nonexact Lee class.\n\nB. Put Q=lambda wedge lambda^c. For each 1<=k<=n,\nint kappa^k omega^(n-k)=(n-k)int Q kappa^(k-1) omega^(n-k).\nIn particular int kappa omega^(n-1)>0 and int kappa^n=0.\nWhere eta_t=omega+t kappa is positive, its actual volume polynomial\nhas degree at most n-1 and derivative\nn(n-1)int Q omega eta_t^(n-2)>0. No Gauduchon hypothesis on omega\nor eta_t is added.\n\nC. If ONLY the LEAST eigenvalue of kappa relative to omega is\nconstant on X, then kappa itself is semipositive, the least eigenvalue\nequals zero everywhere, and its ordinary Bott-Chern class is nonzero\nand pseudoeffective. Constancy of the other eigenvalues and of rank\nis not assumed. Pairing against EVERY positive Gauduchon test is\nnonnegative. If the whole relative spectrum is constant, rank is\nconstant between1 and n-1. In particular the conclusion applies to\nEVERY ACTUAL compact quotient Gamma backslash G with invariant\ncomplex structure and invariant strictly LCK tensors. No lattice\nexistence or abstract-Lie-algebra classification is asserted. Every\ninvariant Hermitian metric on such an actual quotient is Gauduchon.\n\nD. For every n>=2 and 0<epsilon<1, the Hopf quotient of C^n minus0\nby z->z/2 is compact connected and supports\nrho=sum|zj|^2, Phi=rho+epsilon Re(z1^2), Omega=ddc Phi=ddc rho,\nomega=Omega/Phi, lambda=-d log Phi. The tensors descend, omega is\npositive strictly LCK and the Lee period is2log2. Its kappa=ddc log\nPhi has relative eigenvalues -epsilon,1,...,1 at(1,0,...,0).\nThe smooth bounded deck-invariant u=log rho-log Phi gives the\nactual semipositive closed representative kappa+ddc u=ddc log rho.\nThus this is not a counterexample to the original conjecture.\n\nE. In this example write z1=x+iy, R=sum_(j>1)|zj|^2.\nThe relative spectrum consists of n-1 ones and\nh=epsilon((1-epsilon)y^2-(1+epsilon)x^2)/Phi, in[-epsilon,epsilon].\nThe first positive volume-ray boundary is t0=1/epsilon. There\n1+h/epsilon=(2(1-epsilon)y^2+R)/Phi; degeneracy occurs only on the\nreal z1 rays with other coordinates0, and the actual total volume\nremains positive. The constant-spectrum degeneration argument\ntherefore does not establish unrestricted pseudoeffectivity.\n\nF. On the SAME scalar Hopf quotient in EVERY n>=2, set s=sum|zj|^2,\nq=|z1|^2, Psi=s+epsilon*q^2/s, Omega_epsilon=ddc Psi,\nomega_epsilon=Omega_epsilon/s and lambda=-d log s, for EVERY\n0<epsilon<1. These are actual smooth strictly LCK tensors descending\nto the compact quotient, with Omega_epsilon>=(1-epsilon)ddc s>0\nand nonexact Lee form of period2log2. Their curvature is ddc log s,\nsemipositive of rank n-1, with least relative eigenvalue identically\nzero. At(1,0,...,0) the remaining spectrum consists of n-1 copies\nof1/(1-epsilon); at(0,1,0,...,0) it consists of n-1 ones. Hence the\nremaining spectrum is genuinely nonconstant for EVERY epsilon>0.\nThis demonstrates that C's hypothesis is strictly weaker than\nconstant entire spectrum. It is not a counterexample to P03.\n\n\nEXACT UNRESTRICTED ORIGINAL CONTEXT, PRESERVED WITHOUT CHANGES:\nLet X be a connected compact complex manifold of complex dimension n>=2 with a strictly locally conformally Kahler metric omega: d omega=lambda wedge omega and d lambda=0, where lambda is a smooth real nonexact one-form. Use d^c=(i/(4 pi))(barpartial-partial), dd^c=(i/(2 pi))partial barpartial, and lambda^c=(i/(4 pi))(lambda^{0,1}-lambda^{1,0}). The smooth closed real (1,1)-form kappa_lambda=-d lambda^c is de Rham exact and defines an ordinary Bott-Chern class. A closed real (1,1) Bott-Chern class is pseudoeffective if it has a closed positive (1,1)-current representative, equivalently there is a genuine quasi-plurisubharmonic canonical representative u with kappa_lambda+dd^c u>=0. The claim is invariant under conformal changes omega->exp(a)omega, which replace lambda by lambda+d a and kappa_lambda by kappa_lambda-dd^c a.\n\nOriginal P03 conjectures that {kappa_lambda} is pseudoeffective for EVERY such compact strictly LCK manifold. Its pairing with the conformal Gauduchon representative of the LCK metric is strictly positive, and Vaisman/Hopf examples have a semipositive representative; these are background, not the full assertion. Lamari duality relates pseudoeffectivity to nonnegative pairing with EVERY smooth positive Gauduchon test gamma^{n-1}, dd^c(gamma^{n-1})=0. Positivity against one test does not prove the conjecture. Prove the unrestricted conjecture or construct an actual compact strictly LCK counterexample. No candidate proof, construction or auxiliary claim is supplied.\n\nEXACT ORIGINAL COMPLETION CRITERIA, RETAINED AS SCOPE CONTEXT:\nA full proof for arbitrary compact strictly LCK manifolds, with all exact external premises checked against primary sources and the entire argument independently reconstructed, or an explicit compact strictly LCK counterexample with rigorously established failure of pseudoeffectivity (for example a rigorously negative Gauduchon pairing). A restricted Vaisman, Hopf, potential or surface case, positivity against only the LCK-induced test, the already known balanced obstruction, or an additional assumption equivalent to the target does not resolve P03. Retain ordinary Bott-Chern cohomology and the stated normalizations; de Rham exactness does not imply Bott-Chern triviality.",
  "completionCriteria": "PASS requires every restricted A--F in the current whole article to have a complete correct proof, with the full original review and all eight fresh statement-only ordinary notes compared. Independently reconstruct throughout the actual support DAG, not merely its leaves. Preserve the stipulated ddc/dc/Lee-form normalizations, all dimensions n>=2 and all epsilon in(0,1), actual compact quotients and tensor descent, ordinary Bott-Chern nontriviality, EVERY positive Gauduchon test, least-only constancy with variable remaining spectrum, and actual everywhere-versus-partial degeneration of the volume ray. No lattice-existence or classification premise, one-test Lamari sufficiency, or symbolic checks substitute for a proof. No indispensable nonroutine external theorem is asserted: verify this assertion and supply exact primary bindings for any genuinely needed import. Ornea-Verbitsky and Lamari are cited historical context, not proof imports. Inspect all supplied components fully; do not infer acceptance from the prior report or candidate flags. The historical full-original INCONCLUSIVE correctly records failure to close unrestricted P03. A scoped PASS must explicitly leave that original unresolved. Note6 contains an additional exact ray-volume formula; do not silently extend the article release beyond its stated A--F. Do not read private worker histories, raw outputs, artifact trees or paths referenced in ordinary notes. Return the complete structured scoped verdict and precise remaining gaps. A proof defect or indispensable unresolved application must not receive PASS."
}
```

# Complete full-original PUBLIC report; a historical judgment, not proof authority
```json
{
  "verdict": "INCONCLUSIVE",
  "report": "The unrestricted P03 completion criteria are not met. Independent reconstruction establishes the restricted statements A–F and their supplied proofs; I found no concrete mathematical defect in them. The constant-minimum hypothesis is an explicit antecedent, and no argument establishes it, or supplies another positive-current construction, for arbitrary compact strictly LCK manifolds. Both explicit families have pseudoeffective Lee-curvature classes, so neither is a counterexample.\n\nFor A–B, local exactness λ=df gives λᶜ=dᶜf and κ=−ddᶜf, establishing reality, type (1,1), closedness and de Rham exactness with precisely the stipulated normalization. Conformal change gives λ′=λ+da and κ′=κ−ddᶜa. Writing Q=λ∧λᶜ=(i/(2π))λ¹⁰∧λ⁰¹ shows that Q is semipositive and nonzero wherever λ is nonzero. Nonexactness ensures a nonempty open set of such points. Direct differentiation, including the degree-one sign, gives\n d(λᶜ∧κ^(k−1)∧ω^(n−k))=−κ^k∧ω^(n−k)+(n−k)Q∧κ^(k−1)∧ω^(n−k).\nCompact Stokes therefore proves every asserted identity for 1≤k≤n. The cases k=1 and k=n give the strictly positive first integral and zero top integral. Here n≥2 is essential to the first conclusion.\n\nThe nonzero ordinary Bott–Chern conclusion is also established, rather than inferred from de Rham exactness. If κ=ddᶜa globally, e^aω has zero Lee curvature and still has nonexact Lee form λ+da. Applying the same k=1 identity to that metric contradicts its zero left side and strictly positive right side.\n\nFor the volume ray, dη_t=λ∧ω, and Stokes gives ∫κ∧η_t^(n−1)=(n−1)∫Q∧ω∧η_t^(n−2). Consequently V′(t)=n(n−1)∫Q∧ω∧η_t^(n−2), strictly positive whenever η_t is positive. The coefficient of t^n is ∫κ^n=0. These calculations require no Gauduchon condition and use ordinary wedge powers throughout.\n\nFor C, let the constant least relative eigenvalue be r. If r<0, then η_t is positive for 0≤t<−1/r, while η_(−1/r) is semipositive with a kernel at every point. Its top power therefore vanishes everywhere. This contradicts monotonicity and continuity of V, which give V(−1/r)≥V(0)>0. Thus κ is semipositive. Its nonnegative continuous top power has zero integral, hence vanishes identically; the least eigenvalue is consequently zero everywhere. The previously proved nonzero Bott–Chern class has κ itself as a closed positive-current representative. Wedge positivity gives nonnegative pairing against every positive Gauduchon test. No rank constancy was used. Under constant entire spectrum, the rank is constant, nonzero and at most n−1. On an actual compact quotient with invariant tensors, κ and ω have constant matrices in an invariant frame. Likewise, ddᶜγ^(n−1) is an invariant top form, hence a constant multiple of γ^n; Stokes forces that constant to vanish. This proves the invariant Gauduchon assertion without any lattice-existence or classification premise.\n\nFor D–E, scalar contraction acts freely and properly discontinuously: compact subsets of the punctured space have radii bounded above and away from zero, allowing only finitely many intersecting translates. A closed radial annulus supplies a compact fundamental set, and local quotient charts give the connected compact complex manifold. The bounds (1−ε)ρ≤Φ≤(1+ε)ρ ensure positivity. Both Φ and Ω scale by 1/4, so Ω/Φ and −d log Φ descend. Closedness of Ω gives the LCK equation, and a loop lifted from z to z/2 has Lee period 2 log 2, proving nonexactness.\n\nThe Hessian calculation is correct: relative curvature has matrix I−FF*/Φ, where F_i=bar(z_i)+εz_1δ_i1. Its spectrum is n−1 copies of 1 and h=1−|F|²/Φ. Substitution of z_1=x+iy gives exactly the stated formula for h, with range [−ε,ε]; at (1,0,…,0) the spectrum is −ε,1,…,1. The bounded smooth invariant correction u=log ρ−log Φ gives κ+ddᶜu=ddᶜ log ρ, whose Hessian is semipositive by Cauchy–Schwarz. Thus the negative eigenvalue does not disprove class pseudoeffectivity. At the first positive-ray boundary t=1/ε, the volume density relative to ω^n is (1+1/ε)^(n−1)(2(1−ε)y²+R)/Φ. It vanishes precisely on the stated real rays and is positive on an open set, so total volume remains positive. This explicitly verifies why pointwise first degeneration cannot replace the everywhere-degeneration step in C.\n\nFor F, differentiating f=q²/s with a=q/s gives f_(i bar j)=(2/s)(q_i−a s_i)(q_(bar j)−a s_(bar j))+2aδ_i1δ_j1−a²δ_ij. The first two terms are semipositive and 0≤a≤1, proving Ω_ε≥(1−ε)ddᶜs>0 for every stipulated ε. Homogeneity ensures descent, and division by s gives the asserted LCK equation and nonzero Lee period. Curvature is ddᶜ log s, semipositive of rank n−1, so its least relative eigenvalue is identically zero. At the first stated point, the Hessian of f is diag(1,−1,…,−1), giving spectrum 0,(1−ε)^(−1),…,(1−ε)^(−1). At the second point its Hessian vanishes, giving spectrum 0,1,…,1. This establishes genuine variation of the remaining spectrum in every n≥2.\n\nThese mathematical arguments are self-contained and invoke no nonroutine external theorem. The cited [primary paper](https://arxiv.org/pdf/2411.05595v2) was opened and confirms the historical Conjecture 5.13 context; its classification statements and Theorem 5.11 are not proof premises here. No Lamari-duality import is needed for the explicitly constructed smooth positive representatives. The only harmless terminology clarification is that ∫η_t^n equals n! times the usual metric volume; the draft’s stipulated convention leaves every identity and sign unchanged. Unrestricted P03 remains unresolved by this submission.",
  "passages": [],
  "premises": [],
  "kind": "codex-report",
  "operationId": "0ef735aa-efdd-4769-a910-93d0737d0806",
  "reportedAt": "2026-10-09T07:07:20.551Z"
}
```

# Entire fresh statement-only PUBLIC result, all eight ordinary proofs and supports
```json
{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "Structural A and normalization are proved: Lee curvature is real, closed, exact and of type (1,1), with the stated conformal covariance. Smooth semipositive representatives give positivity against every Gauduchon test.",
      "detailedSummary": "Proves the local primitive identities, positivity of Q, conformal covariance, and integration by parts for the ordinary Bott–Chern pairing. A’s nontriviality is deferred to n3. Neither Gauduchon existence nor Lamari sufficiency is used.",
      "text": "Use d^c=i(barpartial−partial)/(4π), dd^c=i partial barpartial/(2π), and ordinary wedge powers without factorial division. Write α=λ^{1,0}. Since λ is real, λ=α+conjugate(α), and\nQ=λ∧λ^c=i α∧conjugate(α)/(2π).\nThus Q is real semipositive of type (1,1), with rank one wherever λ≠0.\n\nHere is a direct local primitive argument. On a small real coordinate ball centered at 0, write λ=sum a_j(x)dx_j and define f(x)=integral_0^1 sum a_j(tx)x_j dt. Closedness gives partial_k a_j=partial_j a_k. Differentiation therefore gives partial_k f=integral_0^1 [a_k(tx)+t sum x_j partial_j a_k(tx)]dt=a_k(x). Hence λ=df locally, λ^c=d^c f, and κ=−dd^c f locally. The displayed dd^c normalization follows from barpartial partial=−partial barpartial. For real f, dd^c f is real and of type (1,1). Consequently κ is globally real, closed and of type (1,1). It is de Rham exact with global primitive −λ^c. This does not establish Bott–Chern triviality.\n\nFor global smooth real a, differentiation gives d(e^aω)=(λ+da)∧e^aω. The new closed Lee form is λ'=λ+da, with [λ']=[λ]≠0, and κ'=−d(λ^c+d^c a)=κ−dd^c a. Thus the ordinary real Bott–Chern class—closed smooth real (1,1)-forms modulo dd^c of global smooth real functions—is conformally invariant. Its nontriviality is proved in n3.\n\nFor any smooth real u and smooth (n−1,n−1)-form Γ, Stokes twice gives integral_X dd^c u∧Γ=integral_X u dd^cΓ. Indeed, integrating d(d^c u∧Γ) first gives integral dd^c u∧Γ=integral d^c u∧dΓ. Integrating d^c(u dΓ) makes the latter integral equal to −integral u d^c dΓ=integral u dd^cΓ. The integral of a d^c derivative of degree 2n−1 is zero: its relevant partial and barpartial terms are d derivatives after selecting their types, so ordinary Stokes applies.\n\nTherefore, for EVERY positive Hermitian γ satisfying dd^c(γ^{n−1})=0, a smooth representative K=κ+dd^c u satisfies integral κ∧γ^{n−1}=integral K∧γ^{n−1}. If K≥0, this pairing is nonnegative. If K is nonzero, it is strictly positive: pointwise K∧γ^{n−1}=(trace_γ K)γ^n/n, and the trace is positive on a nonempty open set. A smooth closed semipositive K is itself a closed positive current. A global smooth u is genuinely quasi-plurisubharmonic: on every relatively compact coordinate ball its Levi form is bounded below, so adding a sufficiently large multiple of |z|^2 makes it plurisubharmonic.\n\nOnly differentiation, Hermitian linear algebra and Stokes are used. Artifact: proofs/n1.txt, serialized with notes.json by python build_notes.py. This proves structural A and the smooth every-test pairing fact, without asserting unrestricted pseudoeffectivity.\n\nArtifacts: /workspace/research/native-workers/codex-X9UWRL",
      "support": []
    },
    {
      "id": "n2",
      "summary": "B is proved in every dimension by Stokes, including all mixed integrals and the strictly increasing actual volume polynomial. No Gauduchon hypothesis is needed.",
      "detailedSummary": "Proves integral κ^kω^{n−k}=(n−k) integral Qκ^{k−1}ω^{n−k}, the positive first integral, and zero top integral. The actual V(t)=integral(ω+tκ)^n has degree at most n−1 and derivative n(n−1) integral Qω(ω+tκ)^{n−2}>0 wherever the ray is positive. These particular integrals do not provide all Gauduchon tests.",
      "text": "By n1, dκ=0. The LCK equation gives d(ω^m)=mλ∧ω^m for every nonnegative integer m. For 1≤k≤n, the graded Leibniz rule gives\n d(λ^c∧κ^{k−1}∧ω^{n−k})\n =−κ^k∧ω^{n−k}+(n−k)Q∧κ^{k−1}∧ω^{n−k},\nbecause dλ^c=−κ and λ^c∧λ=−Q. This is the derivative of a global form of degree 2n−1. Stokes therefore proves exactly\n integral_X κ^k∧ω^{n−k}=(n−k) integral_X Q∧κ^{k−1}∧ω^{n−k}.\nFor k=n this gives integral κ^n=0. For k=1, Q∧ω^{n−1} is nonnegative and strictly positive wherever λ≠0. Nonexact λ cannot vanish identically, so smoothness gives such a nonempty open set. Since n≥2, integral κ∧ω^{n−1}=(n−1) integral Q∧ω^{n−1}>0.\n\nSet η_t=ω+tκ and V(t)=integral_X η_t^n, using ordinary powers. Its binomial expansion is the actual integral polynomial. The coefficient of t^n is integral κ^n=0, so its degree is at most n−1. Crucially dη_t=dω=λ∧ω. Thus\n V'(t)=n integral_X κ∧η_t^{n−1},\n d(λ^c∧η_t^{n−1})=−κ∧η_t^{n−1}+(n−1)Q∧ω∧η_t^{n−2}.\nStokes yields\n V'(t)=n(n−1) integral_X Q∧ω∧η_t^{n−2}.\nWhenever η_t is positive, this integrand is nonnegative and strictly positive where λ≠0. Pointwise, choose an η_t-unitary coframe placing the rank-one Q in the first direction. The restriction of ω to the remaining n−1 directions has positive trace; wedging with η_t^{n−2} gives a positive multiple of that trace. This also covers n=2, when η_t^0=1. Hence V'(t)>0 wherever η_t>0.\n\nNo dd^c(ω^{n−1}) or dd^c(η_t^{n−1}) condition was imposed. These identities do not establish positivity against EVERY Gauduchon test. Artifact: proofs/n2.txt; rerun python build_notes.py. These are ordinary all-dimensional proofs.\n\nArtifacts: /workspace/research/native-workers/codex-X9UWRL",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "A is completed: the ordinary Bott–Chern Lee-curvature class is nonzero on every compact strictly LCK manifold, despite being de Rham exact.",
      "detailedSummary": "A globally dd^c-exact curvature could be killed by a conformal rescaling. Applying B to the resulting strictly LCK metric contradicts its positive first curvature integral. This avoids any identification of de Rham and Bott–Chern cohomology.",
      "text": "Suppose {κ}=0 in ordinary real Bott–Chern cohomology. By definition, κ=dd^c a for a global smooth real a. If the quotient is initially expressed using complex functions, taking real parts provides such a real a because κ is real.\n\nSet ω'=e^aω. By n1 this is smooth positive LCK, its closed Lee form λ'=λ+da remains nonexact, and κ'=κ−dd^c a=0. Apply n2’s k=1 identity to these actual rescaled tensors:\n integral_X κ'∧(ω')^{n−1}=(n−1) integral_X λ'∧(λ')^c∧(ω')^{n−1}>0.\nThe inequality follows from [λ']≠0 and n≥2, exactly as proved in n2. The left side is zero, a contradiction. Therefore {κ}≠0 in ordinary Bott–Chern cohomology.\n\nTogether with n1, this proves every assertion of A. Pseudoeffectivity is not inferred. Artifact: proofs/n3.txt; rerun python build_notes.py.\n\nArtifacts: /workspace/research/native-workers/codex-X9UWRL",
      "support": [
        "n1",
        "n2"
      ]
    },
    {
      "id": "n4",
      "summary": "C is proved using constancy of the least eigenvalue alone. That value is zero and κ is semipositive. The conclusions hold on actual compact invariant quotients, where every invariant Hermitian metric is Gauduchon.",
      "detailedSummary": "A negative constant minimum forces pointwise zero determinant at a finite positive boundary, contradicting B’s increasing actual volume. A positive minimum contradicts integral κ^n=0. No other eigenvalue or rank is assumed constant. Constant entire spectrum gives rank 1 through n−1. Quotient conclusions use actual compactness and invariant coefficients, without classifications or lattice existence.",
      "text": "Let r_1(x)≤...≤r_n(x) be the real relative eigenvalues of κ with respect to ω, and assume ONLY r_1(x)=c is constant.\n\nIf c<0, put T=−1/c>0. For 0≤t<T, all factors 1+tr_j(x)≥1+tc>0, so η_t=ω+tκ is positive. At T all factors are nonnegative, and the factor arising from r_1 vanishes at EVERY point. Hence η_T is semipositive with η_T^n=0 pointwise, so V(T)=0. But n2 gives V'(t)>0 on [0,T), with V(0)=integral ω^n>0. Continuity of the actual polynomial yields V(T)≥V(0)>0, a contradiction. Thus c≥0 and κ is semipositive.\n\nIf c>0, κ is positive everywhere and integral κ^n>0, contradicting n2. Therefore c=0 everywhere. This used no constancy of the other eigenvalues, their multiplicities, or rank. By n3, {κ} is nonzero. The smooth closed semipositive κ is itself a positive-current representative, with canonical correction u=0. By n1 its ordinary Bott–Chern class has nonnegative pairing against EVERY positive Gauduchon test; indeed the pairings are strictly positive since κ is not identically zero.\n\nIf the entire sorted spectrum is constant, the number of positive eigenvalues is constant and at most n−1. It is at least one, because otherwise κ=0 would contradict n2’s positive first integral. Thus rank is constant between 1 and n−1. Under the least-only hypothesis, no constant rank or everywhere-positive lower rank is asserted.\n\nLet X=Γ\\G be an ACTUAL connected compact quotient carrying invariant complex structure and invariant strictly LCK tensors. On G choose a frame by left translation from the identity. The complex structure, ω and λ have constant coefficients; exterior and type differentiation preserve invariance, so κ also has constant coefficients. The relative endomorphism consequently has constant numerical matrix and entire spectrum. These descended tensors therefore satisfy the preceding conclusion. This uses invariant coefficients on the covering group, without assuming that a right action preserves the quotient tensors.\n\nFor ANY invariant Hermitian metric γ on this quotient, partial and barpartial preserve invariant forms. Thus dd^c(γ^{n−1}) is an invariant real top-degree form and equals bγ^n for a real constant b. This equality descends. Stokes and compactness give 0=integral dd^c(γ^{n−1})=b integral γ^n. Since the last integral is positive, b=0 and γ is Gauduchon, independently of whether it is LCK.\n\nNo lattice existence, abstract Lie-algebra compactness, or classification is asserted or invoked. Artifact: proofs/n4.txt; rerun python build_notes.py. This proves restricted C, without resolving unrestricted P03.\n\nArtifacts: /workspace/research/native-workers/codex-X9UWRL",
      "support": [
        "n1",
        "n2",
        "n3"
      ]
    },
    {
      "id": "n5",
      "summary": "D is proved on the actual compact scalar Hopf quotient in every n≥2. Its displayed curvature has a negative eigenvalue, but a bounded smooth correction gives a semipositive representative.",
      "detailedSummary": "Directly verifies compactness, descent, positivity, the LCK equation, and Lee period 2 log 2. Calculates spectrum (−ε,1,...,1) at e1. The global correction log ρ−log Φ yields the closed semipositive rank n−1 representative dd^c log ρ, so the example has every-test positivity and is no counterexample.",
      "text": "Fix n≥2 and 0<ε<1. On M=C^n\\{0}, let D(z)=z/2. Its integer iterates act freely, since D^kz=z with z≠0 forces k=0. They act properly discontinuously: a compact set has radius in [a,b] with a>0, and only finitely many factors 2^{−k} can make that radial interval meet itself. The quotient H_n=M/<D> is therefore a smooth complex manifold. In polar coordinates z=rv, the action is (v,log r)→(v,log r−log 2). Consequently H_n is diffeomorphic to S^{2n−1}×(R/(log 2)Z), proving actual compactness and connectedness in every dimension.\n\nLet ρ=sum |z_j|^2 and Φ=ρ+ε Re(z_1^2). The estimate (1−ε)ρ≤Φ≤(1+ε)ρ proves Φ>0. The added real part is pluriharmonic, so Ω=dd^cΦ=dd^cρ=(i/(2π))sum dz_j∧d conjugate(z_j)>0. Under D both Φ and Ω scale by 1/4; therefore ω=Ω/Φ descends smoothly and positively. Since log Φ(Dz)=log Φ(z)−2 log 2, λ=−d log Φ is deck invariant and descends closed. Closedness of Ω gives dω=λ∧ω.\n\nThe path z(t)=2^{−t}z_0, 0≤t≤1, projects to a closed loop. Its Lee integral is −[log Φ(z(1))−log Φ(z(0))]=2 log 2. Hence λ is nonexact and the metric is strictly LCK. Directly λ^c=−d^c log Φ, so κ=dd^c log Φ.\n\nFor the Levi quadratic form H_f(v)=sum f_{j bar k}v_j conjugate(v_k), write p(v)=sum Φ_jv_j. Since H_Φ(v)=|v|^2,\n H_log Φ(v)=|v|^2/Φ−|p(v)|^2/Φ^2.\nThe common factor i/(2π) cancels in relative eigenvalues. Relative to ω this is identity minus a rank-one nonnegative form, with n−1 eigenvalues 1 and the remaining eigenvalue 1−sum |Φ_j|^2/Φ. At e_1=(1,0,...,0), Φ=1+ε and the derivative vector is (1+ε,0,...,0), so this eigenvalue is −ε. This proves the asserted spectrum exactly.\n\nSet u=log ρ−log Φ. Scaling constants cancel, so u descends globally, smoothly, and boundedly, with −log(1+ε)≤u≤−log(1−ε). It is genuinely quasi-plurisubharmonic by n1. Its corrected representative is κ+dd^c u=dd^c log ρ. Cauchy–Schwarz gives\n H_log ρ(v)=|v|^2/ρ−|sum conjugate(z_j)v_j|^2/ρ^2≥0,\nwith equality precisely for v∈Cz. Thus the corrected form is descended, smooth, closed, semipositive of rank n−1. It is a positive current in the ordinary Bott–Chern class, nonzero by n3, with nonnegative pairing against EVERY positive Gauduchon test by n1. D is therefore no counterexample to P03.\n\nArtifacts: proofs/n5.txt and checks/verify.py. Rerun python checks/verify.py > checks/output.txt for supplementary exact algebra, and python build_notes.py for serialization. The proof does not depend on numerical execution.\n\nArtifacts: /workspace/research/native-workers/codex-X9UWRL",
      "support": [
        "n1",
        "n3"
      ]
    },
    {
      "id": "n6",
      "summary": "E is proved, with first positive boundary t=1/ε and exact volume V(t)=(1+t)^{n−1}V(0). Degeneracy occurs only on the stated real rays, while boundary total volume remains positive.",
      "detailedSummary": "Calculates h∈[−ε,ε], attaining both endpoints, so the least eigenvalue varies. The boundary factor has numerator 2(1−ε)y^2+R. Exactness gives integral hω^n=0 and the exact integrated determinant polynomial. This identifies the missing everywhere-degeneracy premise in an unrestricted extension of C.",
      "text": "Continue with n5’s actual compact quotient and tensors. Write z_1=x+iy and R=sum_{j>1}|z_j|^2. Then Φ=(1+ε)x^2+(1−ε)y^2+R, Φ_1=(1+ε)x−i(1−ε)y, and Φ_j=conjugate(z_j) for j>1. The exceptional relative eigenvalue is therefore\n h=1−[(1+ε)^2x^2+(1−ε)^2y^2+R]/Φ\n  =ε[(1−ε)y^2−(1+ε)x^2]/Φ.\nThe other n−1 eigenvalues are 1. Rearrangement gives\n (h+ε)Φ=ε[2(1−ε)y^2+R]≥0,\n (ε−h)Φ=ε[2(1+ε)x^2+R]≥0.\nThus −ε≤h≤ε, with endpoints attained at e_1 and i e_1 respectively. Since ε<1, h is the least eigenvalue everywhere and is nonconstant.\n\nFor t≥0, η_t=ω+tκ has relative factors 1+t, repeated n−1 times, and 1+th. All are positive for 0≤t<1/ε. At t_0=1/ε the exceptional factor vanishes somewhere; for t>1/ε it is negative at e_1. Hence t_0 is exactly the first positive boundary. There\n 1+h/ε=[2(1−ε)y^2+R]/Φ.\nBecause Φ>0 and 1−ε>0, degeneracy is precisely y=0 and R=0: z=(x,0,...,0) with x real nonzero. These are the real z_1 rays and their quotient images. Everywhere else η_{t_0} is positive, so its top power already has positive integral.\n\nAn exact volume formula strengthens this observation. Ordinary determinant identities give κ^n=hω^n and η_t^n=(1+t)^{n−1}(1+th)ω^n. By n2, integral κ^n=0, hence integral hω^n=0. Therefore, for all real t as a polynomial identity,\n V(t)=(1+t)^{n−1}V(0), where V(0)=integral ω^n>0.\nIn particular V(t_0)=(1+1/ε)^{n−1}V(0)>0. The full positivity interval is −1<t<1/ε: for −1<t<0, h≤ε gives 1+th≥1+tε>0, while the repeated factor requires t>−1.\n\nC’s contradiction requires zero determinant at EVERY point at its boundary. Here that premise fails, because degeneracy occurs only on the specified rays. Thus attaining a negative least eigenvalue somewhere does not reproduce C’s proof when the minimum varies. This establishes E’s failed-extension diagnosis; it does not rule out another proof of unrestricted P03. The example itself has a positive representative by n5.\n\nArtifacts: proofs/n6.txt, checks/verify.py and checks/output.txt. Rerun python checks/verify.py > checks/output.txt and python build_notes.py. The written proof applies to arbitrary n; selected-dimensional checks are supplementary.\n\nArtifacts: /workspace/research/native-workers/codex-X9UWRL",
      "support": [
        "n2",
        "n5"
      ]
    },
    {
      "id": "n7",
      "summary": "F is proved for every n≥2 and 0<ε<1 on the same actual compact Hopf quotient. Its least eigenvalue is identically zero while the remaining spectrum varies.",
      "detailedSummary": "An all-dimensional Levi square decomposition proves Ω_ε≥(1−ε)dd^c s>0. Descent and Lee period establish strictly LCK tensors. Curvature has rank n−1, with spectra (0,1/(1−ε),...) at e1 and (0,1,...) at e2. This proves that C’s hypothesis is strictly weaker than constant entire spectrum; the example remains pseudoeffective.",
      "text": "On n5’s actual compact connected Hopf quotient, fix n≥2 and 0<ε<1. On the cover put s=sum |z_j|^2>0, q=|z_1|^2, f=q^2/s, Ψ=s+εf, and Ω_ε=dd^cΨ. These are smooth away from zero. The functions s,q,f,Ψ all have homogeneity two under real scaling, so D^*Ψ=Ψ/4 and D^*Ω_ε=Ω_ε/4.\n\nFor an arbitrary complex tangent vector v, put b=sum conjugate(z_j)v_j and c=conjugate(z_1)v_1. These are the first directional derivatives of s and q, whose Levi forms are |v|^2 and |v_1|^2. For F(q,s)=q^2/s,\n F_q=2q/s, F_s=−q^2/s^2,\n F_qq=2/s, F_qs=−2q/s^2, F_ss=2q^2/s^3.\nThe complex chain rule gives the all-dimensional identity\n H_f(v)=(2/s)|c−(q/s)b|^2+(2q/s)|v_1|^2−(q/s)^2|v|^2.\nThe first two terms are nonnegative and 0≤q/s≤1. Thus H_f(v)≥−|v|^2 and H_Ψ(v)≥(1−ε)|v|^2. With the stipulated dd^c factor this proves Ω_ε≥(1−ε)dd^c s>0, at every point and in every dimension.\n\nTherefore ω_ε=Ω_ε/s descends smoothly and positively. The closed deck-invariant λ=−d log s descends, and dω_ε=λ∧ω_ε. Along z(t)=2^{−t}z_0 its period is 2 log 2, proving nonexactness and strict LCK. The denominator is s, so κ=−dλ^c=dd^c log s. The Cauchy–Schwarz calculation in n5, with s=ρ, proves that κ is semipositive, with kernel Cz and rank n−1. Relative to positive ω_ε it consequently has exactly one zero eigenvalue and no negative eigenvalues; its least eigenvalue is identically zero.\n\nAt e_1=(1,0,...,0), s=q=1 and b=c=v_1. The square term vanishes and H_f(v)=|v_1|^2−sum_{j>1}|v_j|^2. Thus H_Ψ is diagonal with entries (1+ε,1−ε,...,1−ε), while H_log s has entries (0,1,...,1). Since s=1, the relative spectrum is (0,1/(1−ε),...,1/(1−ε)). At e_2=(0,1,0,...,0), q=c=0, so H_f=0 and H_Ψ is identity; H_log s has one zero in direction e_2 and n−1 ones. The spectrum is (0,1,...,1). The points lie on distinct coordinate axes and cannot be identified by a scalar deck transformation. These spectra differ for EVERY ε>0.\n\nThis gives, in every allowed dimension, an actual compact example with constant least eigenvalue and genuinely nonconstant remaining spectrum. The curvature itself is a smooth closed semipositive representative, with correction zero. Its ordinary Bott–Chern class is nonzero by n3 and has nonnegative pairing against EVERY positive Gauduchon test by n1. F is therefore no counterexample to P03.\n\nArtifacts: proofs/n7.txt, checks/verify.py and checks/output.txt. Rerun python checks/verify.py > checks/output.txt for exact scalar chain-rule algebra, direct Hessian checks in n=2,3 and endpoint spectra; rerun python build_notes.py for serialization. The square decomposition is the proof for arbitrary n.\n\nArtifacts: /workspace/research/native-workers/codex-X9UWRL",
      "support": [
        "n1",
        "n3",
        "n5"
      ]
    },
    {
      "id": "n8",
      "summary": "All restricted A–F have complete elementary reconstructions and supplementary exact algebra checks. No unrestricted P03 proof or compact counterexample is obtained; candidate=false.",
      "detailedSummary": "Records the support DAG, primary-source boundary, reproducible artifacts, environment and finite scope of execution evidence. No indispensable external theorem is applied. Lamari’s primary Lemma 3.3 was inspected only for context. Restricted conditional results and the positive Hopf examples leave the original criterion unresolved.",
      "text": "A is established by n1+n3, B by n2, C by n4, D by n5, E by n6, and F by n7. All six restricted statements are accepted with complete ordinary proofs. The support DAG is acyclic: n1 has no dependencies; n2 uses n1; n3 uses n1,n2; n4 uses n1,n2,n3; n5 uses n1,n3; n6 uses n2,n5; n7 uses n1,n3,n5; this audit uses n1–n7. No supplied earlier notes exist or were consulted.\n\nIndispensable external applications: NONE. No Lamari sufficiency, conformal Gauduchon existence, root theorem for (n−1,n−1)-forms, LCK classification, lattice existence, or current regularization is used. The generic tools are differentiation, Stokes and finite-dimensional positivity. Local primitives, every-test pairing, actual compact Hopf quotients and Levi bounds were reconstructed explicitly.\n\nFor contextual source identification only, the primary item inspected was Ahcène Lamari, Courants kählériens et surfaces compactes, Annales de l’Institut Fourier 49 (1999), 263–285, DOI 10.5802/aif.1673, Lemma 3.3 on printed pages 275–276: https://aif.centre-mersenne.org/item/10.5802/aif.1673.pdf . Its proof treats zero pairing separately before the positive case. It is not a premise of these proofs: restricted every-test positivity follows from the displayed smooth semipositive representatives and integration by parts. Sources/audit.txt and sources/fetch.log record access limitations; no full PDF was saved. No author LCK manuscript, earlier verdict, sibling proof, private note or full-review packet was inspected.\n\nRerun from /workspace/research/native-workers/codex-X9UWRL:\n python checks/verify.py > checks/output.txt\n python build_notes.py\n python checks/audit_notes.py > checks/audit_output.txt\nThe supplied input is input.json. Deliverables are notes.json and proofs/n1.txt through proofs/n8.txt. The proof texts are authoritative unverified drafts; execution does not establish mathematical correctness.\n\nChecks/output.txt contains 17 PASS checks followed by ALL EXACT ALGEBRA CHECKS PASSED. These verify D/E’s exceptional eigenvalue and bounds; F’s direct Levi Hessian in n=2,3, endpoint spectra, and scalar chain rule; and determinant-polynomial reductions in n=2,3,4,7. They are exact finite symbolic results, without numerical approximation, and do not substitute for arbitrary-dimensional proofs. The initial checker compared −1/(ε−1) and 1/(1−ε) structurally; rational cancellation repaired that implementation issue. Checks/initial_failure.txt preserves the diagnostic.\n\nChecks/audit_output.txt records passing schema, ordered acyclic support, proof-text consistency and output-count checks. RUNBOOK.txt records commands and manifest.json records SHA-256 hashes. This verifies artifact consistency only.\n\nChecks/environment.json records Python 3.12.14, SymPy 1.14.0, Linux x86_64 and glibc 2.41. No packages were added and no resource-heavy computation was launched. No AGENTS.md was found in the workspace or its ancestors. The cloud runtime skill was read, but its environment_status tool was unavailable. The network-policy snapshot indicated vpn_configured=false. A direct source download was denied; the public primary source text was obtained through the web tool. No credential contents were inspected.\n\nThe original criterion remains unresolved here. These arguments neither prove pseudoeffectivity of {κ_λ} on arbitrary compact strictly LCK manifolds nor construct an actual compact strictly LCK counterexample with a rigorously negative Gauduchon pairing or another established failure of pseudoeffectivity. B covers particular mixed tests; C assumes a constant least eigenvalue; D–F are positive examples. E identifies why the everywhere-degeneration argument fails without C’s extra hypothesis. Ordinary Bott–Chern cohomology and the exact normalization were preserved throughout. No complete solution of unrestricted P03 is claimed, so candidate=false.\n\nArtifacts: /workspace/research/native-workers/codex-X9UWRL",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "n6",
        "n7"
      ]
    }
  ],
  "candidate": false,
  "workspace": "/workspace/research/native-workers/codex-X9UWRL"
}
```

# Actual dependency chain and source boundary
```json
{
  "n1": [],
  "n2": [
    "n1"
  ],
  "n3": [
    "n1",
    "n2"
  ],
  "n4": [
    "n1",
    "n2",
    "n3"
  ],
  "n5": [
    "n1",
    "n3"
  ],
  "n6": [
    "n2",
    "n5"
  ],
  "n7": [
    "n1",
    "n3",
    "n5"
  ],
  "n8": [
    "n1",
    "n2",
    "n3",
    "n4",
    "n5",
    "n6",
    "n7"
  ]
}
```
All generated notes have been read in full. n1 establishes structural A without its nontriviality; n3 completes that part using n1,n2, so there is no cycle. n4 proves C; n5 D; n6 E; n7 F; n8 records scope and symbolic checks only. Primary historical context is not an indispensable theorem application. Reconstruction and correctness must be judged directly from complete mathematical proofs. The source remains the same reviewed four-page manuscript. No private files may be opened.
