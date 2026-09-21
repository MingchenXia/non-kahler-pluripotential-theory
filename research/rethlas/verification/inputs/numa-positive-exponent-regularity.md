Run_id: numa_positive_exponent_regularity_01

Statement: Critically audit a local sharp regularity consequence of the symmetric NUMA example. For EVERY lambda>0, its unique bounded exponential solution equals the explicitly selected u_star plus a constant on the open zero-density band, so both are C1,1 there but NOT C2 at r=+-t_star. No global C1,1 claim for u_lambda and no assertion for strictly positive density.

Accepted inputs now PASSED with full reports read: book/author/section_degenerate_nonuniqueness.tex (degenerate_nonuniqueness_01), section_numa_radial_family.tex (numa_radial_family_01), section_symmetric_equation_selection.tex (symmetric_equation_selection_01), section_numa_canonical_limit.tex (numa_selected_limit_01). The last audit's conditional radial existence is satisfied by the passed preceding audit. Read actual coefficient conventions and flux proof. Unique bounded exponential solution exists by chapter10 weak equation theory and preserves data symmetry. Standard BV and bounded local BT continuity are accepted.

New work to scrutinize: extending the weak radial flux from prescribed k(r) to k_lambda(r)=exp(lambda(G_lambda-rho))k(r). Do not silently assume regularity of solution; first bounded data coefficient, positivity -> GlocLip/BV, then no atoms/jumps -> continuous derivative, then continuous RHS/inversion. On band k_lambda=0 and symmetry initial h0=0, all first-contact and no-departure sign hypotheses must be checked. Identical derivative -> one constant; one-sided slope derivatives have opposite signs because z0(t*)>0,p'(t*)<0; scalar-to-manifold nonC2 at every point via r submersion and smooth rho. No new external references or novelty claim.

Proof:

\section{Loss of second derivatives at positive exponent}
\label{sec:numa-positive-exponent-regularity}

The selected solution is not $C^2$. In fact the same local loss of regularity occurs at every positive exponent, despite smoothness of the background and the nonnegative density. Thus the exponential term restores uniqueness without removing this degeneracy.

\begin{proposition}\label{prop:numa-positive-exponent-nonc2}
For the symmetric projective data of \cref{thm:numa-selected-limit}, let $u_\lambda$ solve
\[
 \mathrm{MA}_\omega(u_\lambda)
       =e^{\lambda u_\lambda}f\omega_X^3,
 \qquad\lambda>0.
\]
On the open band $\{-1<r<1\}$, $u_\lambda-u_*$ is constant. Both potentials are $C^{1,1}$ there and fail to be $C^2$ at every point of the two hypersurfaces $r=\pm t_*$. In particular, none of these positive-exponent solutions is a globally $C^2$ potential.
\end{proposition}
\begin{proof}
Uniqueness and invariance of the data imply that $u_\lambda$ is $K$-invariant. Write $u_\lambda+\rho=G_\lambda(r)$ on $U$. The positivity argument in \cref{lem:numa-radial-flux} uses only boundedness and invariance, so $G_\lambda$ is locally Lipschitz and $h_\lambda=G_\lambda'$ is locally of bounded variation, with
\[
 -x\leq h_\lambda(r\pm)\leq y,
 \qquad dh_\lambda+z\,dr\geq0.
\]
Its weak flux equation is the same one, with the prescribed coefficient replaced by
\[
 k_\lambda(r)=e^{\lambda(G_\lambda(r)-\rho(r))}k(r).
\]
Indeed, the scalar convolution and signed-product argument of that lemma is unchanged, and this is exactly the radial coefficient of the right-hand measure. At the initial bounded stage $k_\lambda$ is locally bounded. Hence the right side of the flux equation has no atoms. The same strictly positive jump integral eliminates every jump of $h_\lambda$. Thus $h_\lambda$ is continuous and $G_\lambda$ is $C^1$. The coefficient $k_\lambda$ is consequently continuous. Where $A(r,h_\lambda)>0$, inversion of the $C^1$ flux gives
\[
 h_\lambda'=\frac{k_\lambda(r)}{A(r,h_\lambda)}-z.
\]

On $-1<r<1$ the coefficient $k_\lambda$ is identically zero. Exchange invariance gives $h_\lambda(0)=0$ and oddness. On the positive half-band, the first-contact and no-departure arguments in the proof of \cref{thm:numa-selected-limit} apply verbatim: the first branch solves $h'=-z_0$, reaches $-p$ at $t_*$, and cannot leave that lower boundary to its right because $(h+p)'=p'-z_0<0$ on every proposed departure interval. Therefore
\[
 h_\lambda(r)=
 \begin{cases}
  p(r),&-1<r\leq-t_*,\\
  -\displaystyle\int_0^r z_0(s)\,ds,&-t_*\leq r\leq t_*,\\
  -p(r),&t_*\leq r<1.
 \end{cases}
\]
This is the derivative of $u_*+\rho$. Its primitive differs from $G_\lambda$ by one constant on the connected band. The claimed local $C^{1,1}$ regularity follows from the explicit slope.

At $t_*\in(0,1)$ the two one-sided derivatives of this slope are
\[
 h_\lambda'(t_*-)=-z_0(t_*)<0,
 \qquad
 h_\lambda'(t_*+)=-p'(t_*)>0.
\]
They are different. Thus the scalar primitive has no second derivative there. Since $r$ is a smooth submersion on $U$, a smooth local curve with $r$ as its parameter transfers this failure to the potential on $X$. Subtracting the smooth $\rho$ cannot remove the discrepancy. Oddness gives the same failure at $-t_*$. The identical slope proves the assertion for $u_*$ as well.
\end{proof}

The zero set of $f$ contains the whole band. This example therefore does not concern the smooth strictly positive densities in the Hermitian Calabi--Yau theorem. It does show why smoothness of a nonnegative density alone is insufficient for second-order regularity, even when the equation includes a strictly increasing exponential factor.


Follow AGENTS.md, persist all sequential/reference/failure records, full readable report and final results/numa_positive_exponent_regularity_01/verification.json via MCP. Never edit book/prior results. Strict correct iff no gaps/errors.
