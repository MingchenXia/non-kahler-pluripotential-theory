# Bounded audit: Gauduchon persistence and bounded adjoint measures

run_id: gauduchon_persistence_adjoint_01

Use the normal verification workflow and persist the complete report. Audit the mathematical text below in order. This is a bounded check, not whole-book certification. Accepted internal/classical inputs are stated explicitly; check their application rather than reproving them. No assertion of novelty.

## Conventions and accepted inputs

X is connected compact complex, n>=2; dd^c=i/(2 pi) partial bar-partial. A Hermitian form is smooth strictly positive. H_omega consists of smooth real u with omega+dd^c u>0. PSH potentials are genuine quasi-psh functions with omega+dd^c u>=0.

1. Gauduchon theorem: for each Hermitian eta there is a unique positive smooth rho, normalized by integral rho eta^n=1, with dd^c(rho eta^(n-1))=0. The adjoint probability is rho eta^n. The smooth operator L_u v=n dd^c v wedge eta^(n-1)/eta^n annihilates this probability in integral.
2. First mass variation: D M(u)[v]=n integral v dd^c((omega+dd^c u)^(n-1)). H_omega is convex and open in C^infty.
3. The book's Chiose characterization (forward cross-reference only) states that mass invariance for every smooth strictly positive potential is equivalent to dd^c omega^j=0 for every 1<=j<=n-1.
4. The raw one-form alpha_u(v)=integral v(omega+dd^c u)^n has a differentiable primitive on H_omega iff d omega=0. In particular a non-Kahler surface with any Hermitian form cannot have such a primitive.
5. Bounded exact regularization on a compact Hermitian manifold: each bounded omega-psh u is the decreasing limit of uniformly bounded smooth potentials u_j with omega+dd^c u_j>0. This is an internal theorem; no closed-background assumption.
6. Bounded Bedford--Taylor products in a smooth nonclosed background are positive, with decreasing continuity, and on a coordinate ball are defined by the finite expansion
(omega+dd^c u)^n = sum_{k=0}^n binom(n,k) (dd^c(u+q))^k wedge (omega-dd^c q)^(n-k),
where q is a fixed smooth strongly psh quadratic making u+q psh. The local classical capacity theorem gives weak convergence of all bounded mixed products for uniformly locally bounded psh sequences converging in local BT capacity. The book's Hermitian capacity is locally equivalent to this capacity on inner coordinate balls. Use a finite cover and partition of unity.

## Text to verify

The measure $\mu_u$ depends on the solution metric $\eta$. Its multiplier is constant precisely when $\eta$ is Gauduchon: a constant multiplier satisfies the defining equation exactly in that case, and uniqueness then applies. Thus
\[
 \mu_u=\frac{\eta^n}{\int_X\eta^n}
 \quad\text{if }\ddc(\eta^{n-1})=0.
\]
On a surface, $\ddc\omega_u=\ddc\omega$, so every positive potential perturbation of a Gauduchon form is still Gauduchon. In higher dimension this persistence requires more than the Gauduchon condition at $u=0$.

\begin{proposition}\label{prop:gauduchon-potential-persistence}
Every form $\omega_u$, for $u\in\HH_\omega$, is Gauduchon if and only if
\[
 \int_X\omega_u^n=\int_X\omega^n
 \quad\text{for every }u\in\HH_\omega.
\]
In that case, with $M=\int_X\omega^n$, the normalized multiplier is $\rho_u=M^{-1}$ and $\mu_u=M^{-1}\omega_u^n$ for every $u\in\HH_\omega$.
\end{proposition}
\begin{proof}
The first variation in \cref{prop:mass-variation} is
\[
 \left.\frac{\mathrm d}{\mathrm dt}\right|_{t=0}
       \int_X\omega_{u+tv}^n
 =n\int_Xv\ddc(\omega_u^{n-1}).
\]
If all $\omega_u$ are Gauduchon, this derivative vanishes in every direction; integrating along the segment from $0$ to $u$ gives the asserted mass identity. Conversely, the identity makes the displayed integral zero for every smooth real test function $v$, so $\ddc(\omega_u^{n-1})=0$. The normalized multiplier is then the constant $M^{-1}$ by \cref{thm:gauduchon}.
\end{proof}

The differential characterization is given by \cref{thm:mass-invariance-characterization}: persistence is equivalent to $\ddc(\omega^j)=0$ for all integers $1\leq j\leq n-1$. The following example distinguishes it from the single Gauduchon identity in dimension three.

\begin{example}\label{ex:gauduchon-persistence-torus}
Let $E=\mathbb C/(\mathbb Z+\mathrm i\mathbb Z)$ and $X=E^3$. Write $z_j=x_j+\mathrm i y_j$ for the coordinates on the covering space, for $1\leq j\leq3$, and let $\eta_j=(\mathrm i/2)\mathrm dz_j\wedge\mathrm d\bar z_j$ be the descended forms. The periodic functions
\[
 b=\exp(\cos(2\pi x_1)),\qquad c=b^{-1}
\]
define a Hermitian form
\[
 \omega=\eta_1+b\eta_2+c\eta_3.
\]
Since $bc=1$,
\[
 \omega^2=2b\eta_1\wedge\eta_2
          +2c\eta_1\wedge\eta_3+2\eta_2\wedge\eta_3.
\]
The derivatives of $b,c$ involve only $x_1$, so $\ddc(\omega^2)=0$.

Put $v=\cos(2\pi x_2)$ and $h=-\pi\cos(2\pi x_2)$. With the book's normalization, $\ddc v=h\eta_2$. For a real $s$ with $0<|s|<1/(\pi\mathrm e)$, the form
\[
 \omega_{sv}=\eta_1+(b+sh)\eta_2+c\eta_3
\]
is positive, since $b\geq\mathrm e^{-1}$ and $|h|\leq\pi$. However,
\[
 \ddc(\omega_{sv}^2)
 =2s\ddc\omega\wedge\ddc v
 =2sh\ddc c\wedge\eta_2\wedge\eta_3\ne0.
\]
Indeed, $\ddc c=(c''/(4\pi))\eta_1$, where the prime differentiates in $x_1$, and $c''(0)=4\pi^2\mathrm e^{-1}$ while $h=-\pi$ at $x_2=0$. Thus a Gauduchon form can have arbitrarily small positive potential perturbations which are not Gauduchon.
\end{example}

Even when persistence holds, the one-form $v\mapsto\int_Xv\,\mathrm d\mu_u$ need not have a primitive on $\HH_\omega$. On a compact non-K\"ahler surface equipped with a Gauduchon form, the proposition identifies it with the raw Monge--Amp\`ere one-form divided by the constant $M$. By \cref{thm:raw-primitive}, it has no primitive. The adjoint measure provides the compatibility condition for a linear equation; this is distinct from a variational primitive.

\section{Limits of adjoint measures}
\label{sec:adjoint-measure-limits}

Let $X$ be a connected compact complex manifold of dimension $n\geq2$, and let $\omega$ be a Hermitian form on $X$. Put $\HH_\omega=\{v\in C^\infty(X,\mathbb R):\omega_v:=\omega+\ddc v>0\}$. For $v\in\HH_\omega$, let $\mu_v=\rho_v\omega_v^n$ be the probability measure defined by the normalized Gauduchon multiplier in \cref{prop:adjoint-gauduchon}. For bounded potentials, use the products of \cref{prop:bounded-products} and convergence in the capacity defined in \cref{sec:hermitian-capacity}. Weak convergence of measures means convergence against continuous functions on $X$.

\begin{proposition}\label{prop:bounded-adjoint-persistence}
Assume that $\omega_v$ is Gauduchon for every $v\in\HH_\omega$, and set $M=\int_X\omega^n$. For every $u\in\PSH(X,\omega)\cap L^\infty(X)$, the measure
\[
 \mu_u:=M^{-1}(\omega+\ddc u)^n
\]
is a probability measure and agrees with the preceding definition when $u\in\HH_\omega$. If $u_j,u\in\PSH(X,\omega)\cap L^\infty(X)$, for integers $j\geq1$, are uniformly bounded and $u_j\to u$ in capacity, then $\mu_{u_j}\rightharpoonup\mu_u$.
\end{proposition}
\begin{proof}
For smooth strictly positive potentials, both assertions about the definition follow from \cref{prop:gauduchon-potential-persistence}. For bounded $u$, choose uniformly bounded smooth strictly positive approximants decreasing to $u$ by \cref{thm:bounded-exact-regularization}. Continuity of bounded products passes their common mass $M$ to the limit. Positivity is \cref{prop:bounded-products}.

To prove convergence, work on an inner coordinate ball and add one fixed smooth quadratic $q$ so that all $u_j+q$ and $u+q$ are plurisubharmonic. They are uniformly bounded and converge in local Bedford--Taylor capacity, by the capacity comparison recalled in \cref{sec:hermitian-capacity}. The classical bounded capacity-continuity theorem therefore gives convergence of their mixed products. Multiply by the fixed smooth coefficients in \eqref{eq:bounded-expansion}, then use a finite cover and a partition of unity. This gives $(\omega+\ddc u_j)^n\rightharpoonup(\omega+\ddc u)^n$ on $X$, and division by $M$ proves the assertion.
\end{proof}

The proposition applies to every Gauduchon surface. It gives an approximation-independent extension in the bounded range under its explicit geometric hypothesis. It does not construct a weak linearized operator.

For a general Hermitian form, the conformal theorem does not define $\rho_u$ when $\omega+\ddc u$ is only a current. Suppose smooth potentials $u_j\in\HH_\omega$ converge to a genuine $u\in\PSH(X,\omega)$ in capacity. Which energy or nondegeneracy hypotheses ensure that $\mu_{u_j}$ has a unique weak limit, independent of the approximation? Does this limit satisfy an adjoint identity for a weak linearization? In \cref{chap:normalization}, supporting probabilities for the normalization functional recover $\mu_u$ in the smooth case and yield a conditional approximation theorem. Outside the preceding bounded regime and those stated hypotheses, uniqueness and a distributional adjoint identity remain open here.
