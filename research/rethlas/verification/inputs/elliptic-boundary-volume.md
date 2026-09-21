Run_id: elliptic_boundary_volume_01

Statement: Check every assertion in this short companion section. The new calculation concerns the fixed-density variational volume on the explicit elliptic threefold, its boundary orders 1,2,3, and the relation to section growth on the nonnegative integral quadrant. It is not a proposed general numerical-dimension theorem. No novelty claim.

Conventions: ddc=i/(2pi) partial bar-partial. The threefold and forms are those of book/author/section_vanishing_lower_mass.tex and section_lower_mass_metric_geometry.tex: X maps to B=P1xP1 with connected compact elliptic fibers; alpha,beta are the integral-one FS pullbacks; D=dt wedge dc t is globally smooth rank-one semipositive; omega=alpha+beta+D is Hermitian; alpha²=beta²=D²=0, omega³=6 alpha wedge beta wedge D, integral omega³=24pi. These prior proofs and their independent audits are complete and accepted canonical inputs. X has BMP and every Hermitian metric has v_-=0 by those established sections. The new proof may not infer equality of raw masses from equality of the equation scalar.

Canonical inputs, inspect locally under /Users/mingchen/Non-Kahler:
1. book/author/chapter_gauduchon_variational_volume.tex, thm:gaud-volume-dual-formula identifies the smooth normalized-equation scalar with V_mu for each strictly positive Hermitian background; thm:gaud-volume-nef-limit gives continuity along theta+epsilon h; prop:gaud-volume-density-comparison controls changes of smooth positive probability measure.
2. book/author/section_nef_degenerations.tex, prop:nef-degeneration-orders defines the liminf/limsup logarithmic orders and proves independence of h and mu. The Hopf example there is analogous but is not a premise for this new calculation.
3. Standard holomorphic maximum principle on compact connected fibers, local holomorphic sections of the elliptic bundle, and bihomogeneous polynomial dimensions on P1xP1 prove h0(X,pi*O(am,bm))=(am+1)(bm+1) for a,b nonnegative integers. Check this short argument independently; do not assume the pending elliptic_closed_current_descent_01 audit. The phrase 'preceding proposition' describes proposed placement, and may be checked against research/editorial/section_elliptic_closed_current_descent.tex, but the section-count formula itself must be verified here. No ideal or partial-kernel conclusion is used in this companion.

Check coefficients, normalization of mu0, positivity of Omega_epsilon even at the cone boundary, passage from the explicit scalar to V_mu, all corner cases a=0 or b=0, the logarithmic limits, and exact limits of the interpretation of section growth. The proposed closed-current cone calculation in the other draft is not a premise for this formula on the explicitly given family a alpha+b beta. The reference to its faces may be read as the elementary nonnegative quadrant alone.

Use the normal Rethlas sequential, reference and synthesis workflow. Write only this run's memory/results and final response; do not edit any submitted proof, the production book, another audit, verifier installation or Git history. No approval or TLS bypass. Parent handles source history and any repairs.

Proof:

\subsection{The boundary volume and section growth}
\label{sec:elliptic-boundary-volume}

The same forms permit an exact calculation of the fixed-density volume near the nef boundary. It gives all three possible orders associated with the faces of this cone.

\begin{proposition}\label{prop:elliptic-boundary-volume}
On the elliptic threefold, put $\theta=a\alpha+b\beta$ with $a,b\geq0$, and let $\mu_0=\omega^3/(24\pi)$. Then for every $\epsilon>0$,
\begin{equation}\label{eq:elliptic-boundary-volume}
 \mathcal V_{\mu_0}(\theta+\epsilon\omega)
       =24\pi\epsilon(a+\epsilon)(b+\epsilon).
\end{equation}
In particular $\mathcal V_\mu(\theta)=0$ for every smooth positive probability measure $\mu$. If $q$ is the number of positive entries among $a,b$, then the orders of \cref{prop:nef-degeneration-orders} satisfy
\[
 \underline a(\theta)=\overline a(\theta)=3-q.
\]
These orders hold for every smooth positive probability measure and every Hermitian perturbation direction.
\end{proposition}
\begin{proof}
The forms $\alpha,\beta,D$ are semipositive of rank one, their squares vanish, and $\omega=\alpha+\beta+D$ is strictly positive. Thus
\[
 \Omega_\epsilon=\theta+\epsilon\omega
       =(a+\epsilon)\alpha+(b+\epsilon)\beta+\epsilon D>0.
\]
The wedge expansion gives
\[
 \Omega_\epsilon^3
   =6\epsilon(a+\epsilon)(b+\epsilon)\alpha\wedge\beta\wedge D
   =24\pi\epsilon(a+\epsilon)(b+\epsilon)\mu_0.
\]
The zero potential therefore solves its smooth normalized equation. By \cref{thm:gaud-volume-dual-formula}, the equation's scalar is precisely $\mathcal V_{\mu_0}(\Omega_\epsilon)$, proving \eqref{eq:elliptic-boundary-volume}. Nef continuity in \cref{thm:gaud-volume-nef-limit} and smooth-density comparison give $\mathcal V_\mu(\theta)=0$.

If both $a,b$ are positive, the leading term is $24\pi ab\epsilon$. If exactly one is positive, it is $24\pi(a+b)\epsilon^2$. If both are zero, the formula is $24\pi\epsilon^3$. The logarithmic quotients have limits $1,2,3$, respectively. Their independence of the density and perturbing metric is \cref{prop:nef-degeneration-orders}.
\end{proof}

For nonnegative integers $a,b$, the bundle $L=\pi^*\mathcal O_B(a,b)$ has
\[
 h^0(X,L^m)=(am+1)(bm+1).
\]
Indeed the compact-fiber descent and bihomogeneous polynomial argument of the preceding proposition also apply when one or both integers vanish. Its growth degree is exactly $q$, while the boundary order of its smooth curvature representative is $3-q$. Thus the boundary order records the loss of algebraic growth dimension in this explicit family, even though the unperturbed three-dimensional Monge--Amp\`ere measures vanish.

Every positive perturbation $\Omega_\epsilon$ still has zero lower mass, by \cref{thm:vanishing-lower-mass}, and finite upper mass, since $X$ has BMP. Formula \eqref{eq:elliptic-boundary-volume} concerns one fixed smooth density, and does not assert conservation of the raw mass over all potentials. Whether comparable identifications hold beyond such explicit families is part of \cref{qu:nef-degeneration-exponent}.
