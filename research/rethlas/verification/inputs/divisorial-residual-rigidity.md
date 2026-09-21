Run_id: divisorial_residual_rigidity_01

Statement: Verify the strengthened finite-divisor residual equation theorem in research/editorial/section_divisorial_residual_rigidity.tex. This is a candidate replacement for thm:divisorial-residual-equation in book/author/section_divisorial_gauduchon_volume.tex. It is outside checked checkpoint53. Do not edit any frozen submission, prior result or memory manually; use the normal verification workflow. No novelty claim or new external paper theorem is involved.

Context: X is a connected compact complex manifold, n>=1. mu is a smooth strictly positive probability volume. theta is any smooth real (1,1)-form; D=sum a_j D_j is a finite effective real divisor, a_j>0. Choose smooth line-bundle metrics, sigma_D=sum a_j log|s_j|^2, eta_D=sum a_j curvature_j, beta_D=theta-eta_D. Then ddc sigma_D=[D]-eta_D, ddc=i/(2pi) partial barpartial. Assume beta_D has a smooth strictly positive representative. c=V_mu(beta_D)>0 is its smooth equation constant. The draft claims more than ordinary-type uniqueness: any genuine theta-psh u with all generic divisorial coefficients at least a_j and extended MA measure >=c mu must equal the constructed sigma_D+v plus a constant. Its remainder is therefore smooth without assuming boundedness. Any equation solution in the ordinary type sigma_D, even with an initially unspecified nonnegative scalar, has that scalar c and is unique modulo constants.

Accepted internal inputs: Read the precise relevant book statements and accept their proved scopes. These are prop:divisorial-gaud-feasibility and its finite nonclosed divisorial-removal argument in section_divisorial_gauduchon_volume.tex / lem:nonclosed-divisorial-removal in chapter_divisorial_models.tex; the smooth equation and thm:gaud-volume-dual-formula; prop:individual-normalizer-lp in section_individual_density_subsolutions.tex; cor:smooth-dual-exact-equation (all genuine threshold subsolutions unique constants under smooth strictly positive dual attainment, n>=2) in section_smooth_dual_regularity.tex; and thm:bounded-strict-domination in section_modified_comparison.tex. Chapter_products.tex provides positivity, intrinsic local products under smooth changes of potential decomposition, and vanishing of extended measures on pluripolar sets. For n=1 the extended measure is the full positive current with its polar mass removed, so it is dominated by that current. Classical elliptic regularity and constancy of a pluriharmonic distribution on connected compact X are standard inputs.

Check every step of the reduction for an UNBOUNDED remainder. Divisorial removal gives w=u-sigma_D-v as an L1 distribution with its genuine Omega-psh representative, where Omega=beta_D+ddc v>0. Off D, theta+ddc u=Omega+ddc w and the local smooth gauge change identifies extended measures; both global measures vanish on D. With dV=mu, zero solves MA_Omega(0)=c mu, so b_Omega(1)=c and its smooth solution supplies a normalized strictly positive Gauduchon dual maximizer. The accepted rigidity theorem applies in n>=2. In n=1 use the full current Omega+ddc w>=MAext_Omega(w)>=c mu=Omega, and its total mass c from Stokes. For the last assertion an ordinary-type remainder is bounded; compare its measure c' mu with c mu using bounded strict domination and every constant translate. Check both possible inequalities and the case c'=0. Then the preceding stronger rigidity applies.

Proof:

\begin{theorem}\label{thm:divisorial-residual-equation}
Suppose $\beta_D$ admits a smooth positive representative, and put $c=\mathcal V_\mu(\theta;D)$. There is a $\theta$-plurisubharmonic potential $u_0=\sigma_D+v$, with $v$ smooth, satisfying
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u_0)=c\mu.
\]
Every $u\in\PSH(X,\theta)$ such that
\[
 \nu(u,D_j)\geq a_j\quad(1\leq j\leq N),\qquad
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)\geq c\mu
\]
is a constant translate of $u_0$. In particular, a solution in the ordinary singularity type of $\sigma_D$ has scalar $c$, has a smooth remainder, and is unique up to constants.
\end{theorem}
\begin{proof}
The smooth equation and \cref{thm:gaud-volume-dual-formula} give
\[
 \Omega=\beta_D+\ddc v>0,\qquad \Omega^n=c\mu.
\]
Then $\theta+\ddc(\sigma_D+v)=[D]+\Omega\geq0$. Off $D$ its extended measure is $\Omega^n$, and both measures give $D$ zero mass. This proves existence.

For a potential $u$ satisfying the displayed inequalities, divisorial removal as in \cref{prop:divisorial-gaud-feasibility} makes
\[
 w=u-\sigma_D-v\in\PSH(X,\Omega),\qquad
 \Omega+\ddc w=\theta+\ddc u-[D]\geq0.
\]
The difference is first taken in $L^1$ and then with its canonical representative. On $X\setminus D$ the two currents have smooth changes of local potential decomposition, so their extended measures agree there. Both measures vanish on $D$. Hence
\[
 \mathrm{MA}^{\mathrm{ext}}_\Omega(w)
       =\mathrm{MA}^{\mathrm{ext}}_\theta(u)\geq c\mu.
\]
Use $\mathrm{d}V=\mu$. The zero potential solves the smooth equation in background $\Omega$, so $b_\Omega(1)=c$ by \cref{prop:individual-normalizer-lp}. For $n\geq2$, its Gauduchon representative gives a smooth strictly positive dual maximizer. By \cref{cor:smooth-dual-exact-equation}, all threshold subsolutions differ by constants; comparing $w$ with zero shows that $w$ is constant. For $n=1$, the positive current $\Omega+\ddc w$ dominates its extended measure, hence dominates $c\mu=\Omega$. Its total mass is $\int_X\Omega=c$ by Stokes. Thus $\ddc w=0$, and $w$ is again constant.

Finally, if $u$ lies in the ordinary type of $\sigma_D$ and solves an equation with scalar $c'\geq0$, the same reduction gives a bounded $w$ with $\mathrm{MA}_\Omega(w)=c'\mu$. If $c'\ne c$, the smaller of these two measures is at most a constant strictly less than one times the larger. Applying \cref{thm:bounded-strict-domination} after every constant translation of the larger-measure potential is impossible. Therefore $c'=c$, and the rigidity just proved gives $u=u_0+\mathrm{constant}$.
\end{proof}
