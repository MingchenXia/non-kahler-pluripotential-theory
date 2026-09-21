Run_id: lower_mass_metric_geometry_01

Statement: Verify the entire attached differential-geometric supplement. The specific compact complex threefold X=(P3 minus two disjoint lines)/<[z:w]->[z:e^(2pi)w]> and its form omega=alpha+beta+dt wedge dc t are described in research/editorial/section_vanishing_lower_mass.tex. Independently check the metric calculations and the numerical upper mass 24pi, the vertical-energy equality characterization, the no-pluriclosed and no-closed-Kahler-current obstruction, and the claimed independence of upper and lower mass properties, conditional only where stated.

Conventions: ddc=i/(2pi) partial bar-partial, dc=i/(4pi)(bar-partial minus partial). The smooth closed semipositive forms alpha and beta are pullbacks from P1 x P1, with Fubini-Study integral ONE on each factor. t=log(||w||^2/||z||^2) is defined on the cover, t shifts 4pi, dt and dc t descend. Fiber coordinate zeta=a+ib has lattice 2pi Z+2pi i Z. The fibration is a holomorphic submersion with connected elliptic fibers. Verify ddc t=beta-alpha, signs in ddc(dt wedge dc t), balanced identity d omega^2=0 and fiber volume, not only positivity.

Canonical prior inputs (root /Users/mingchen/Non-Kahler):
- book/author/section_mass_geometry.tex, eq:threefold-mass-dirichlet and thm:threefold-mass-minimizer: on a Gauduchon threefold the raw mass difference is -3 integral du wedge dc u wedge ddc omega for all smooth real u. The maximum formulation assumes ddc omega>=0. Read the prior proof and check its exact application.
- book/author/section_gauduchon_volume_extrema.tex, thm:gaud-volume-mass-extrema: bounded exact-background regularization makes the smooth strict and bounded mass suprema equal.
- book/author/chapter_products.tex, prop:bmp-metric: metric independence of bounded upper mass.
- book/author/chapter_hopf.tex: the specified Hopf threefold has v_-=6 and v_+=infinity.
- book/author/section_non_kahler_geometry.tex: Fujiki-class-C characterization by a closed Kahler current, attributed there to Demailly-Paun Theorem0.6; this standard preexisting characterization may be used. The geometric obstruction proof itself must only use current Stokes with smooth factors, and positivity, not a singular wedge or class-C assumption.
- research/editorial/section_lower_mass_solvability.tex: under separate review lower_mass_solvability_01, establishes v_->0 iff universal positive-scaled solvability. ONLY the final equation consequence is conditional on this prior proposed result.

Dependency boundary: the preceding new construction's conclusion v_-(h)=0 is under independent audit vanishing_lower_mass_01. Treat this conclusion as a conditional input for the independence statements and the limiting vertical energy of its witness sequence. The identities ddc omega, d omega^2, volume, v_+ upper bound, fiberwise equality case, and metric obstructions are independent of that deep lower-mass theorem, given the explicit quotient and metric setup. Do not assume those new identities themselves. Report the conditional dependencies explicitly. No novelty claim is made.

The supplement has no external-paper citation of its own; verify the exact local canonical theorem uses. Follow the normal sequential, reference and synthesis workflow, with ordinary approvals and no TLS bypass. Write only this audit's memory, results and final output. Do not edit source files, other verifier records, Git state or run synchronization. The primary agent handles manuscript integration and repository history.

Proof:

\subsection{A balanced metric and a finite upper mass}
\label{sec:lower-mass-metric-geometry}

The metric used in the construction has additional differential properties. They distinguish this example from the Hopf threefold and identify a geometric obstruction that is independent of the scalar Monge--Amp\`ere equation. We retain the notation of \cref{eq:lower-mass-quotient-metric} and put $D=\mathrm{d}t\wedge\dc t$.

\begin{proposition}\label{prop:lower-mass-balanced-metric}
On the threefold of \cref{thm:vanishing-lower-mass}, the Hermitian form $\omega=\alpha+\beta+D$ satisfies
\[
 \mathrm{d}(\omega^2)=0,\qquad \ddc\omega=2\alpha\wedge\beta\geq0,
 \qquad \int_X\omega^3=24\pi.
\]
For every smooth real function $u$,
\begin{equation}\label{eq:lower-mass-vertical-energy}
 \int_X(\omega+\ddc u)^3
 =24\pi-6\int_X\mathrm{d}u\wedge\dc u\wedge\alpha\wedge\beta.
\end{equation}
Consequently $v_+(\omega)=24\pi$. In particular $X$ has the bounded mass property, while $v_-(h)=0$ for every Hermitian form $h$ on $X$.
\end{proposition}
\begin{proof}
Although $t$ is defined on the covering space, both $\mathrm{d}t$ and $\dc t$ descend. The Fubini--Study potentials give
\[
 B:=\ddc t=\beta-\alpha.
\]
The forms $\alpha,\beta$ are closed, and $\alpha^2=\beta^2=0$, since each is pulled back from a curve. As $D^2=0$, we obtain
\[
 \mathrm{d}D=-\mathrm{d}t\wedge B,\qquad
 \ddc D=-B^2=2\alpha\wedge\beta,
\]
\[
 \mathrm{d}(\omega^2)
 =-2(\alpha+\beta+D)\wedge\mathrm{d}t\wedge(\beta-\alpha)=0.
\]
In the last identity, the term involving $D$ has a repeated $\mathrm{d}t$, and
$(\alpha+\beta)\wedge(\beta-\alpha)=0$. Thus $\omega$ is balanced, hence Gauduchon, and the formula for $\ddc\omega$ follows.

On a fiber use $\zeta=a+\mathrm{i}b$ with both real periods $2\pi$. There $t=2a+$ a constant, so
\[
 D|_E=\frac1\pi\,\mathrm{d}a\wedge\mathrm{d}b,
 \qquad \int_ED=4\pi.
\]
The equality $\omega^3=6\alpha\wedge\beta\wedge D$, fiber integration and the integral-one normalization of each Fubini--Study form give $\int_X\omega^3=24\pi$.

Apply the Gauduchon threefold identity \eqref{eq:threefold-mass-dirichlet} with $\ddc\omega=2\alpha\wedge\beta$ to obtain \eqref{eq:lower-mass-vertical-energy}. Its last integral is nonnegative. Thus every smooth strictly $\omega$-plurisubharmonic mass is at most $24\pi$, and the constant potential attains this value. Bounded exact-background regularization, as in \cref{thm:gaud-volume-mass-extrema}, identifies the same supremum over bounded potentials. Metric independence in \cref{prop:bmp-metric} proves bounded mass on $X$. The assertion about the lower mass is \cref{thm:vanishing-lower-mass}.
\end{proof}

For an admissible smooth $u$, equality in the upper-mass bound holds precisely when $u$ is constant along every elliptic fiber. Indeed, $\alpha\wedge\beta$ is a positive volume form in the base directions, so the nonnegative integral in \eqref{eq:lower-mass-vertical-energy} vanishes exactly when the fiber derivative of $u$ vanishes. The fibers are connected, and smooth local sections then show that $u$ is the pullback of a smooth function on $\mathbf P^1\times\mathbf P^1$. For the sequence with masses tending to zero, that same integral instead tends to $4\pi$.

\begin{proposition}\label{prop:lower-mass-no-pluriclosed}
The threefold $X$ admits neither a pluriclosed Hermitian metric nor a closed K\"ahler current.
\end{proposition}
\begin{proof}
The nonzero smooth semipositive $(2,2)$-form $\alpha\wedge\beta$ is $\ddc$-exact by the preceding calculation. If a Hermitian metric $\eta$ satisfied $\ddc\eta=0$, Stokes would give
\[
 0<\int_X\eta\wedge\alpha\wedge\beta
   =\frac12\int_X\eta\wedge\ddc\omega
   =\frac12\int_X\omega\wedge\ddc\eta=0,
\]
a contradiction. The strict inequality holds because $\eta$ is positive in the vertical direction at every point.

If a closed positive current $T$ dominated $\varepsilon\omega$ for some $\varepsilon>0$, positivity and current Stokes would likewise give
\[
 0<\varepsilon\int_X\omega\wedge\alpha\wedge\beta
 \leq\int_XT\wedge\alpha\wedge\beta
 =\frac12\int_X\omega\wedge\ddc T=0.
\]
All pairings involve a current and smooth forms, so no singular product is being used. This excludes a closed K\"ahler current.
\end{proof}

The example is therefore outside the Fujiki class, by the characterization recalled in \cref{sec:non-kahler-geometric-problems}. It shows that a balanced metric does not guarantee positive lower mass, even together with bounded upper mass. In contrast, the Hopf threefold has positive lower mass and infinite upper mass. The two properties are logically independent. Their simultaneous failure on the products in \cref{cor:both-mass-properties-fail} is a third regime. In particular, bounded mass alone cannot replace the positive lower-mass hypothesis in a theorem asserting solvability for every non-pluripolar measure.
