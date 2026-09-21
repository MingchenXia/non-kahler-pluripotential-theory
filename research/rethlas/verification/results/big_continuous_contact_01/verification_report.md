# Verification report: big_continuous_contact_01

**Verdict: correct under the stated accepted inputs and the explicit conditional homogeneous replacement prerequisite.**

The complete submitted proof was checked in textual order: **18 proof items, 108 individual deductions, and six reference/application checks**. There are **zero critical errors and zero gaps**. This is a bounded mathematical audit, not formal verification or novelty certification. No book file was edited.

The verdict is conditional on the exact statement of [thm:ball-homogeneous-replacement](/Users/mingchen/Non-Kahler/book/author/section_local_homogeneous_dirichlet.tex:23). Its proof and the outcome of the separate audit \`local_homogeneous_dirichlet_01\` are outside this run. Inclusion in the book still requires both audits to pass.

The accepted inputs are the elementary genuine envelope construction and canonical representatives, max closure for the same smooth background, and the extended nonpluripolar measure's local bounded agreement and noncharging of pluripolar sets. The earlier [local_big_continuity_01 report](../local_big_continuity_01/verification_report.md) supplies only the Kiselman proof method. This run independently checks its use for globally unbounded \(p\).

The standing [manuscript conventions](/Users/mingchen/Non-Kahler/book/author/conventions.tex:3) specify a connected compact complex manifold without boundary, with dimension at least one. The manuscript's definition of big is existence of a strict potential; no numerical-volume characterization is substituted.

## Central source comparison

The supplied [Demailly94 primary PDF](/Users/mingchen/Non-Kahler/research/sources/Demailly94-flow.pdf), its extracted text, and images of printed pages 12 and 16 were checked against the [author-hosted source](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization_flow.pdf). The required result is Theorem 4.1 with the full base-fiber Hessian estimate, together with Section 3 and Remarks 4.6–4.7.

| Source hypothesis or notation | Exact use in this proof |
| --- | --- |
| Closed current \(T_D=\alpha_D+(i/\pi)\partial\bar\partial\psi_D\) | \(T_D=dd^c p,\ \alpha_D=0,\ \psi_D=p/2\), since the manuscript uses \(dd^c=(i/2\pi)\partial\bar\partial\). |
| Continuous real lower form \(\gamma\) | \(-\theta\); the source does not require this form to be closed. |
| Arbitrary quasi-psh potential | The genuine envelope is globally \(L^1\), though possibly unbounded below. |
| Smooth semipositive curvature comparison form | A sufficiently large fixed \(A_D\omega\); no semipositivity of \(\theta\) is needed. |
| \(\Psi_D(z,w)\) | \(R_{|w|}p(z)/2\), for the same positive normalized formal-exph averaging operator. |
| \(\lambda_D=t\partial_t(\Psi_D+K_{0,D}t^2)\) | Put \(K_0=2K_{0,D}\), so \(\lambda_{\mathrm{here}}=t\partial_t(R_tp+K_0t^2)=2\lambda_D\). Rename \(A=A_D/2\). |
| Source error tending to zero | An increasing majorant \(\epsilon(t)\to0\), with no claimed power rate. |

The normalization conversion leaves the coefficient of \(\theta\) unchanged. It rescales only the fixed constants used in the proof.

The source does not hide a bounded-potential assumption. Section 3 controls remainders through local integrals of a quasi-psh function and its positive corrected Hessian, including logarithmic averaged growth and the scaled Lelong estimate in (3.11). Such bounds are finite for the fixed \(p\). The constants can depend on that function, the lower form, and the fixed geometry; they need only be independent of the small parameters \(c,\delta\), not independent of every possible envelope.

Positive-radius smoothness is a separate elementary consequence of (3.1)–(3.2): after a change of variables, the operator has a smooth integral kernel acting on an \(L^1\) function. No global gradient estimate is needed.

## Why the unbounded-p argument passes

Writing
\[
F(z,t)=R_tp+Kt^2+Kt,\qquad
\widetilde\lambda=\lambda+2(K-K_0)t^2+Kt,
\]
gives a strictly positive second logarithmic derivative. The \(Kt\) term supplies a positive vertical Hessian of size \(K/t\), which absorbs the fixed mixed and vertical source errors by Young's inequality. The remaining horizontal error has the form \(A\widetilde\lambda+\epsilon(t)\).

On any fixed compact neighborhood outside \(Z\), \(p\) has a finite uniform lower bound. Thus
\[
R_tp+Kt^2\ge p
\]
and the logarithmic penalty exclude \(t=0\) uniformly on that neighborhood for fixed \(c,\delta\). The cap value is bounded by \(R_\delta h\). The minimizer is unique and continuous, and local radius intervals allow the same minimum principle as in the prior audit. The cap case is legitimate: infimum over the open interval ending at the cap equals the capped minimum by continuity. The full [Kiselman tube theorem](https://arxiv.org/pdf/1810.12733), Theorem 1.1, imposes no interior-attainment requirement.

For the precise extension across \(Z\), set \(B=\theta+(Ac+\epsilon(\delta))\omega\). For each \(\eta>0\), freeze \(B\) at a center \(z_0\), choose a quadratic \(q\) satisfying
\[
dd^c q=B(z_0)+\eta\beta,
\]
and shrink so the variation of \(B\) is at most \(\eta\beta\). The allowed psh removal theorem extends \(\Phi+q\). Subtracting \(q\) gives the same canonical extension regardless of the chosen correction, and on that ball
\[
dd^c\Phi\ge -B-2\eta\beta.
\]
For fixed \(\eta\), these balls cover the coordinate region. Current positivity is local, so the estimate holds throughout that region before \(\eta\downarrow0\). The limit yields the exact asserted lower form. This uses potentials only for constant forms.

The barrier correction then makes \(v_\delta-m(\delta)\) a genuine global envelope competitor. The exact affine identity and the choice \(c\ge\delta\) give, on each fixed \(L\Subset X\setminus Z\),
\[
\Phi_{c,\delta}-p\le C_Lc,\qquad
t_{\min}\ge a_L\delta,\qquad
\sup_L|R_{a_L\delta}p-p|\le C'_Lc\longrightarrow0.
\]
Smooth positive-radius averages consequently prove continuity, with no contact assertion used along the way.

## Contextual existence of the analytic barrier

The source for this separate claim is [Demailly, Analytic Methods in Algebraic Geometry, July 2011, Theorem 14.12](/Users/mingchen/Non-Kahler/research/sources/Demailly-analytic-methods.txt:8405), particularly (c), with the preceding Section 14.B construction; the [author-hosted book](https://www-fourier.ujf-grenoble.fr/~demailly/manuscripts/analmeth_book.pdf) was also located.

Given a strict potential \(q\) with \(\theta+dd^cq\ge\kappa_0\omega\), apply the theorem to \(\phi_D=q/2\) and \(\gamma=\kappa_0\omega-\theta\). Set \(\rho=2\phi_m\) for an approximant with \(\epsilon_m<\kappa_0/2\). This gives
\[
\theta+dd^c\rho\ge(\kappa_0-\epsilon_m)\omega
\ge\tfrac12\kappa_0\omega.
\]
Theorem 14.12 allows the arbitrary continuous lower form used here. Its construction provides analytic singularities and smoothness off the pole set: the glued expression is the logarithm of a positive smooth weighted sum of Bergman squared norms away from its coherent ideal's zero set. Smoothness is not inferred from the bounded-remainder convention for analytic singularities alone.

This checks the contextual sentence from the classical construction, without a general big contact theorem.

## Conditional contact argument

The boundary data and competitor in the homogeneous replacement theorem are continuous because continuity has already been proved on a neighborhood of the closed ball. Thus its domination property really applies to \(p\).

Trace positivity gives \(\Delta H\ge-C\) in a fixed chart, with \(C\) independent of the shrinking radius and replacement. If
\[
q_r=\sup_{\partial B_r}p+C'(r^2-|z-x|^2),
\]
then choosing \(C'\) sufficiently large makes \(H-q_r\) subharmonic and nonpositive at the boundary. The scalar maximum principle gives
\[
H\le \sup_{\partial B_r}p+C'r^2.
\]
That upper bound tends to \(p(x)\), while \(\inf_{B_r}h\to h(x)>p(x)\), furnishing actual obstacle slack.

For pasting, let \(q_a=\max(p,H-a)\) inside and \(p\) outside. Boundary continuity gives a collar on which \(q_a=p\), so accepted max closure applies in the original nonclosed background. If \(q\) is the desired pasted function, then \(0\le q-q_a\le a\) on the ball, while the functions agree outside; hence the current inequality passes to \(q\). Since \(q\le h\) and \(q\ge p\), the envelope property forces \(q=p\).

The extended measure agrees locally with the homogeneous bounded product. A countable subcover of the resulting zero-measure balls covers \(\{p<h\}\setminus Z\); \(Z\) has zero measure by the accepted nonpluripolar property. No finiteness of total mass is needed.

## Complete sequential deduction record

The following items preserve the proof's written order. They expand its existing arguments and the exact applicability of its references.


### 1. Opening setup and contextual analytic-barrier claim

1. The standing manuscript conventions specify connected compact complex X of positive dimension without boundary. This supplies finite suprema and uniform constants; no noncompact extension is claimed.
2. The displayed strict analytic barrier is an explicit hypothesis. Analytic poles form a proper analytic set because rho is genuine; smoothness off that set is separately supplied.
3. In the manuscript, big means there is a genuine q with theta+ddc q>=kappa0 omega for some kappa0>0. It does not mean positive numerical volume or a nef-volume criterion.
4. With manuscript ddc=i/(2pi)partial barpartial, apply Demailly's Theorem 14.12 to phi=q/2 and gamma=kappa0 omega-theta. Its approximants phi_m give q_m=2phi_m, so ddc q_m>=gamma-epsilon_m omega and q_m has logarithmic analytic singularities. The current being regularized is the closed ddc q, not theta+ddc q.
5. The source's glued Bergman construction is smooth wherever its positive weighted sum is nonzero. Its local coherent ideals agree across charts, so the zero set is analytic. Thus the chosen approximant is smooth off its analytic pole set; this is not inferred from a bounded-remainder definition alone.
6. Choose m with epsilon_m<kappa0/2 and set rho=q_m. It is genuine, has the needed poles/smoothness, and theta+ddc rho>=kappa0 omega/2. Closedness of gamma, theta, or omega is not needed. Exact external evidence is recorded separately.

**Finding:** checked; no critical error or gap.

### 2. thm:big-continuous-envelope-contact — normalization and envelope

1. A genuine quasi-psh rho has finite upper bound on compact X; h has finite minimum. Subtraction of a finite constant makes rho+2<=h without changing ddc rho.
2. rho+2 is a genuine theta-psh competitor, so the accepted elementary envelope construction gives genuine canonical p and rho+2<=p<=h everywhere.
3. On every compact neighborhood off Z, rho is smooth and bounded below, whereas h is bounded above. Thus p is finite and uniformly bounded on that neighborhood before continuity is known.
4. p is quasi-psh since ddc p>=-theta and theta is smooth. As a genuine quasi-psh function on compact X, p is in L1; global boundedness below is not asserted.

**Finding:** checked; no critical error or gap.

### 3. Regularization paragraph — exact Demailly input and constants

1. The manuscript convention is ddc=i/(2pi)partial barpartial, while Demailly uses i/pi. The literal substitution is T_D=ddc p, alpha_D=0, psi_D=p/2 and gamma=-theta. T_D and alpha_D are closed; gamma is merely a continuous real lower form in Theorem 4.1.
2. Choose a smooth curvature comparison form A omega with A>0 sufficiently large. Compactness bounds the negative Chern bisectional curvature, in particular on the source's required orthogonal pairs. This auxiliary form is unrelated to semipositivity of theta.
3. The source's equations (3.1)-(3.2) are positive normalized radial formal-exph averages. Changing variables produces a smooth kernel for positive radius, so averaging an L1 potential is finite and smooth, even when its values are minus infinity on a pluripolar set.
4. Theorem 4.1 is stated for general quasi-psh psi, not bounded psi. Its full base-fiber lower bound has a fixed mixed error C|zeta||eta| and vertical error C|eta|^2, not just a horizontal Hessian estimate.
5. The proof of Proposition 3.8 estimates remainders by local integrals of the potential and its positive corrected Hessian. The mean-value/Lelong estimates on pp.10-12 allow logarithmic averaged growth and O(t^-2) scaled Hessian integrals. They do not require a finite global infimum or L-infinity norm.
6. The constants may depend on this fixed p, its finite local L1 bounds, its smooth lower bound and the fixed geometry. They are uniform in x and small t, independent of c and delta; no uniform estimate over a family of envelopes is needed.
7. With K0 from the source, lambda=t*d/dt(R_t p+K0 t^2) is nonnegative and increasing. The corrected averages are logarithmically convex, increase with t, and converge to the canonical p; hence R_t p+K0 t^2>=p.
8. Pointwise convergence follows also from Remark 4.6 comparing with ordinary radial convolution up to O(t^2). Upper semicontinuity and the psh local correction identify the limit with the canonical representative, including unbounded potentials.
9. Linearity gives Psi_D=R_t p/2 and ddc_D Psi_D=ddc_here R_t p. Taking K0=2K0,D yields lambda_here=2lambda_D, so the curvature coefficient is rescaled to A_D/2 and other fixed constants are renamed. This exactly preserves the displayed form of the proof's estimates; no theta coefficient is altered.

**Finding:** checked; no critical error or gap.

### 4. Regularization paragraph — correction and mixed-error absorption

1. Take K>=K0 with K>0 and write F(z,t)=R_t p+Kt^2+Kt. Its logarithmic derivative is lambda_tilde=lambda+2(K-K0)t^2+Kt>=lambda.
2. The second logarithmic derivative of F is d(lambda)/d(log t)+4(K-K0)t^2+Kt>0, so subtracting c log t preserves strict convexity in log t.
3. The Hessian of K|w| contributes a positive vertical term proportional to K|eta|^2/(4t). Young's inequality bounds C|zeta||eta| by C' t|zeta|^2 plus part of that vertical contribution.
4. For sufficiently small t the remaining positive vertical term absorbs C|eta|^2. K|w|^2 only adds a nonnegative vertical term.
5. The resulting full lower bound is -theta-(A lambda+epsilon0(t)+C't)omega on base directions. Replacing lambda by the larger lambda_tilde weakens the estimate in the valid direction.
6. Take an increasing nonnegative majorant epsilon(t) of epsilon0(t)+C't, tending to zero. The procedure uses the source's fixed constants and neither semipositivity of theta nor boundedness below of p.
7. The source's Remark 4.7 uses a different correction Psi+|w| with derivative lambda+t-2K0t^2. It is not identified with F; the larger correction used here has been checked directly.

**Finding:** checked; no critical error or gap.

### 5. Regularization paragraph — minimizing radii and local minimum principle

1. For fixed c>0 and small delta, the objective is at least p-K(delta^2+delta)-c log(t/delta). On a fixed compact neighborhood off Z, the first term has a uniform lower bound.
2. At t=delta the objective is R_delta p<=R_delta h, uniformly bounded above. Hence all local minimizers lie in one compact interval [b,delta] with b>0, for these fixed parameters. No information about p on kernel supports beyond the global smoothing inequality is required.
3. Smoothness for positive radius, compactness of that interval, and strict logarithmic convexity give a unique minimizing radius, continuous in the base point. The minimum value is finite and continuous locally off Z.
4. At an interior minimizing radius lambda_tilde=c; at the upper cap lambda_tilde<=c, since the left derivative of the objective there is nonpositive.
5. For any small eta>0, continuity of the minimizer and of lambda_tilde allows a fixed radial interval around nearby minimizers whose upper endpoint has lambda_tilde<c+eta. Monotonicity bounds it on the entire interval.
6. If the minimizer is the cap, the infimum over the open interval ending at delta equals its closed-cap minimum by continuity. The general Kiselman principle does not require interior attainment.
7. Write w=exp(tau) on a product of a coordinate ball and a strip. This product is pseudoconvex, has connected tube fibers, and the objective is independent of Im(tau); the logarithmic penalty is pluriharmonic.
8. Freeze B(z)=theta(z)+(A(c+eta)+epsilon(delta))omega(z). For any e>0 a quadratic q with ddc q=B(z0)+e beta makes the full objective plus q psh on a sufficiently small base ball.
9. Kiselman's minimum principle applies to this finite fiber infimum. Comparing B(z0) with B(z), covering the base neighborhoods, and letting e and then eta tend to zero gives theta+ddc Phi>=-(Ac+epsilon(delta))omega locally throughout X minus Z.
10. This repeats the audited lemma's method on compact neighborhoods where p is bounded; no assertion of its globally bounded conclusion for this p has been assumed.

**Finding:** checked; no critical error or gap.

### 6. Regularization paragraph — cap bound

1. Evaluating at t=delta makes both polynomial corrections and the logarithmic penalty zero, giving Phi<=R_delta p.
2. Positivity of the same averaging kernel and p<=h imply R_delta p<=R_delta h.
3. R_delta h is smooth and bounded for fixed delta, so Phi has a uniform upper bound near the entire analytic set Z. The bound applies on the domain X minus Z, as needed for removal.

**Finding:** checked; no critical error or gap.

### 7. Extension paragraph — removable singularities with the precise lower form

1. Put e0=Ac+epsilon(delta) and B=theta+e0 omega. On X minus Z, ddc Phi>=-B.
2. On a fixed coordinate region let beta be a constant positive Euclidean form. For any eta>0, around any center z0 choose a ball on which -eta beta<=B(z)-B(z0)<=eta beta.
3. Choose a real quadratic q with ddc q=B(z0)+eta beta. Then Phi+q is psh off Z and locally bounded above. The allowed analytic-set removable singularity theorem extends it by limsup from the complement.
4. Subtract q. The extension equals limsup of Phi from the complement because q is continuous, so extensions using different centers, corrections, or eta agree. It is a genuine global quasi-psh function since Phi is finite off the proper set Z.
5. The corrected extension satisfies ddc Phi>=-B(z0)-eta beta>=-B(z)-2eta beta on that ball. For each eta these balls cover the fixed coordinate region, and current positivity is local.
6. Thus ddc Phi+B+2eta beta>=0 throughout the region. Let eta decrease to zero in pairings with positive test forms. This gives ddc Phi+B>=0 exactly, including on Z.
7. This argument uses potentials only for constant coefficient forms, and never assumes a local potential for nonclosed theta. The shrinking balls cause no gap because the inequality is patched for each fixed eta before taking the limit.
8. The upper bound Phi<=R_delta h survives the limsup extension since R_delta h is continuous.

**Finding:** checked; no critical error or gap.

### 8. Extension paragraph — lower comparison with the barrier

1. For every t<=delta, R_t p+Kt^2>=p, Kt>=0, and -c log(t/delta)>=0. Taking the infimum gives Phi>=p-K(delta^2+delta) off Z.
2. Take delta small enough that K(delta^2+delta)<=1. The initial envelope inequality then gives Phi>=rho+1 off Z.
3. On Z the barrier equals minus infinity, so rho<=Phi there as an extended-real inequality regardless of whether Phi is finite. Thus rho<=Phi everywhere.

**Finding:** checked; no critical error or gap.

### 9. Parameter paragraph — m, c, and s

1. Kernel support lies within distance C t of the base point for all small t, and the kernel is positive with integral one. Hence |R_t h-h| is bounded by the uniform continuity modulus of h at Ct.
2. Taking the supremum over 0<t<=delta gives finite nonnegative m(delta) tending to zero. This does not assume h is differentiable.
3. c=m(delta)+epsilon(delta)+delta is positive, tends to zero, and dominates m(delta), epsilon(delta), and delta.
4. With A>=0 and kappa>0, s=(Ac+epsilon(delta))/kappa is nonnegative, tends to zero, and satisfies s<=((A+1)/kappa)c and s kappa=Ac+epsilon(delta). We may keep A>0 to avoid any zero-times-minus-infinity notation.

**Finding:** checked; no critical error or gap.

### 10. Barrier correction paragraph — theta-psh competitor

1. The affine-current identity is theta+ddc v=[theta+ddc Phi+s(theta+ddc rho)]/(1+s). It holds for nonclosed theta.
2. Its numerator is at least (-(Ac+epsilon(delta))+s kappa)omega=0, so v is theta-psh.
3. Both summands are genuine quasi-psh, bounded above, and finite off Z. Their positive affine combination is genuine, L1, and has the canonical quasi-psh representative.
4. Since rho<=Phi and s>=0, v<=Phi<=R_delta h<=h+m(delta), with the same valid extended-real inequality at poles.
5. Subtracting m(delta) leaves the theta-psh condition unchanged and produces a genuine envelope competitor. Hence v-m(delta)<=p, or v<=p+m(delta), everywhere.
6. Only the envelope definition is used for this comparison; there is no stability theorem, contact theorem, or Monge-Ampere mass estimate.

**Finding:** checked; no critical error or gap.

### 11. Compact-set paragraph — control of Phi minus p

1. On L compactly contained in X minus Z, p and rho are finite and p-rho<=sup_L h-inf_L rho<infinity.
2. Multiplying the definition of v by 1+s gives exactly Phi-p=(1+s)(v-p)+s(p-rho). The last term has a plus sign.
3. Use v-p<=m(delta), bounded 1+s, and s=O(c) to get Phi-p<=C_L c. Constants depend on L and the fixed data, not delta or the base point in L.
4. The lower bound Phi-p>=-K(delta^2+delta) remains available; neither bound presupposes continuity of p.

**Finding:** checked; no critical error or gap.

### 12. Compact-set paragraph — radius lower bound

1. At the previously established minimizer t, rearrange its defining equality: -c log(t/delta)=Phi-(R_t p+Kt^2)-Kt+K(delta^2+delta).
2. Use R_t p+Kt^2>=p and -Kt<=0 to obtain -c log(t/delta)<=Phi-p+K(delta^2+delta).
3. For delta<1, delta^2+delta<=2delta<=2c. The preceding compact-set estimate bounds the right hand side by another C_L c.
4. Divide by c>0 to obtain log(delta/t)<=C_L. Thus t>=a_L delta with a_L=exp(-C_L)>0, decreased to at most one if necessary. It is fixed for L and independent of delta.
5. No uniform global lower bound for minimizing radii near Z is claimed or needed.

**Finding:** checked; no critical error or gap.

### 13. Compact-set paragraph — uniform smoothing convergence and continuity

1. Monotonicity and a_L delta<=t give R_(a_L delta)p+K(a_L delta)^2<=R_t p+Kt^2.
2. The minimum identity gives R_t p+Kt^2=Phi+Kdelta^2+Kdelta-Kt+c log(t/delta)<=Phi+Kdelta^2+Kdelta.
3. Dropping the nonnegative term K(a_L delta)^2 proves the asserted upper bound; the source's monotone lower bound gives R_(a_L delta)p>=p-K(a_L delta)^2.
4. Combine with Phi-p<=C_L c to obtain sup_L |R_(a_L delta)p-p|<=C'_L c, which tends to zero.
5. Each R_(a_L delta)p is smooth for positive radius by its L1 kernel representation. A sequence delta decreasing to zero yields a uniform limit of continuous functions on L.
6. Take compact neighborhoods inside X minus Z to obtain continuity at every point there. This proves the first assertion without contact support and without a global smoothing gradient bound.

**Finding:** checked; no critical error or gap.

### 14. Contact paragraph — open ball and conditional replacement

1. For x in {p<h} minus Z, continuity of p and h off Z gives a neighborhood with positive obstacle slack; choose a coordinate ball whose closure lies there.
2. p is continuous on that closed ball and theta-psh inside, so p restricted to the boundary is continuous admissible boundary data.
3. The exact conditional theorem gives a continuous theta-psh H on the closed ball with the same boundary, homogeneous bounded local MA in the interior, and domination of every continuous theta-psh competitor with boundary below the data.
4. Taking p itself as competitor gives H>=p. No comparison for unbounded competitors or different backgrounds is used. The contraction and smooth-boundary Lipschitz assertions of the prerequisite are not needed.
5. The prerequisite's proof and the outcome of its separate audit local_homogeneous_dirichlet_01 are not certified or assumed to have passed by this audit.

**Finding:** checked; no critical error or gap.

### 15. Obstacle-slack paragraph — uniform scalar upper bound

1. Fix one chart around x before varying r. Tracing theta+ddc H>=0 against the Euclidean metric gives the distributional inequality Delta H>=-C, with C depending only on a fixed upper bound for the trace of smooth theta on the chart.
2. Set S_r=sup_boundary(B_r) p and q_r=S_r+C'(r^2-|z-x|^2). In the real Euclidean convention Delta |z-x|^2=4n; choose C'>=C/(4n), adjusted for the fixed ddc normalization if needed.
3. Delta(H-q_r)>=0, while H-q_r<=0 on the boundary. The scalar subharmonic maximum principle applies to the continuous H, giving H<=q_r<=S_r+C'r^2.
4. C' is independent of r and H. Continuity of p at x gives S_r+C'r^2 tending to p(x); continuity of h gives inf_Br h tending to h(x).
5. If d=h(x)-p(x)>0, shrink so S_r+C'r^2<p(x)+d/3 and inf_Br h>h(x)-d/3. Then H<h on the ball, and in particular H<=h, while the closure remains away from Z.
6. This uses only a scalar trace and scalar maximum principle; it does not invoke a theta potential or a nonclosed Monge-Ampere comparison theorem.

**Finding:** checked; no critical error or gap.

### 16. Pasting paragraph — legitimate nonclosed pasting

1. For a>0, continuity of H-p on the closed ball and its zero boundary values give H-a<p on an inner collar of the compact boundary.
2. Define q_a=max(p,H-a) inside and p outside. It is p on a neighborhood of the boundary and theta-psh elsewhere by the accepted max closure for this same theta.
3. Let q equal H inside and p outside. It is well defined and continuous near the boundary because boundary values agree; it equals the canonical p away from the ball.
4. Since H>=p inside, H-a<=q_a<=H there. Thus 0<=q-q_a<=a inside and q_a=q=p outside; the differences are supported off Z.
5. As a decreases to zero the convergence is uniformly controlled near and inside the closed ball, and is unchanged elsewhere. In particular it is local L1 convergence, so theta+ddc q>=0 follows by passing to currents.
6. The resulting pasted representative is quasi-psh and canonical: it is the continuous representative around the closed ball and equals p on the exterior. Alternatively the same local uniform limit after quadratic correction is psh.
7. Both H and p are at most h in their respective regions, so q<=h globally; q is genuine since it is finite off Z. It is therefore a valid envelope competitor.
8. q>=p by H>=p, while the definition of p gives q<=p. Consequently q=p everywhere and p=H on B_r.
9. None of these operations requires closedness of theta. A bare piecewise gluing without the max/collar argument would not suffice, but the submitted proof supplies that argument.

**Finding:** checked; no critical error or gap.

### 17. Final contact paragraph — locality and extended measure

1. p=H on B_r and both functions are locally bounded there. The conditional homogeneous equation and locality of the accepted local bounded product give MA_theta(p)(B_r)=0.
2. Such balls cover U={p<h} minus Z. Since the manifold is second countable, choose a countable subcover; countable subadditivity gives MA_theta(p)(U)=0 even when the total measure is infinite.
3. The accepted extended measure agrees with the bounded local measure off Z and charges no pluripolar set. Z is analytic and is also contained in the pole set of the global quasi-psh rho, hence pluripolar.
4. The set {p<h} is Borel (indeed p-h is upper semicontinuous). Its intersection with Z has zero extended measure. Together with U this yields the displayed restricted measure equal to zero on all X.
5. No finite-total-mass subtraction, dominated convergence of masses, BMP, or PVP is used.

**Finding:** checked; no critical error or gap.

### 18. Closing scope and full hypothesis-use audit

1. The argument treats continuous finite obstacles only. No transition to quasi-continuous unbounded obstacles is asserted.
2. Compactness enters normalization, L1 integrability, uniform geometry/kernel constants, and uniform continuity of h. The standing manuscript supplies it explicitly.
3. Theta smoothness supplies the lower-form regularity, local freezing and uniform scalar trace bound; its closedness and semipositivity are never used.
4. Strictness kappa>0 absorbs Ac+epsilon(delta) by the affine barrier correction. Local boundedness of rho off Z controls p and p-rho on compact sets; analyticity of Z permits removal and pluripolar noncharging.
5. The independently asserted smoothness of rho off Z is stronger than the local boundedness needed for these estimates and is harmless; it is available from the classical construction.
6. Bigness need not be used again after the explicit strict barrier has been supplied. Its contextual implication has been separately checked with gamma=kappa0 omega-theta.
7. The only local homogeneous replacement properties used are continuous solvability, the same boundary, homogeneous MA, and domination of continuous competitors, all expressly accepted conditionally.
8. The conclusion is conditional on that prerequisite and the stated accepted manuscript inputs. It is not a formal verification, novelty certification, or certification of the replacement proof.

**Finding:** checked; no critical error or gap.

## Reference and retrieval record

### analytic_barrier

**Location:** Opening contextual claim: bigness supplies a strict analytic barrier

**Status:** matched_and_applicable.

The returned Kähler-Einstein and closed-Kähler envelope statements do not match. The equisingular approximation statement in arXiv:2202.04791, Theorem 2.5, asserts smoothness off an analytic set but not the required analytic singularity type; it is not used as a substitute.

The theorem concerns an almost psh scalar potential on any compact complex manifold with an arbitrary continuous real lower form gamma; gamma need not be closed. The constructed logarithmic analytic singularities are comparable to finite holomorphic generator norms. Smoothness off their poles is checked from the positive smooth weighted Bergman sum, not inferred merely from the bounded remainder terminology.

For theta+ddc q>=kappa0 omega in the manuscript normalization, put phi_D=q/2 and gamma=kappa0 omega-theta. The source gives phi_m and ddc_D phi_m>=gamma-epsilon_m omega. Set rho=2phi_m and take epsilon_m<kappa0/2. Then theta+ddc rho>=kappa0 omega/2, with a proper analytic pole set and smoothness on its complement.

The arxiv-first query and full-statement web fallback were run. Targeted primary-author searches identified the exact book, but direct web PDF retrieval timed out and indexed search did not display Theorem 14.12. The supplied workspace primary PDF/text contains the full theorem and construction and was read directly. This is a resolved retrieval limitation, not an absent reference.

Primary web source: [Demailly, Analytic Methods in Algebraic Geometry, July 2011, Section 14.B, equations (14.6)-(14.8), the gluing on p.142, and Theorem 14.12(c), pp.142-143.](https://www-fourier.ujf-grenoble.fr/~demailly/manuscripts/analmeth_book.pdf).

Local source: [/Users/mingchen/Non-Kahler/research/sources/Demailly-analytic-methods.pdf](/Users/mingchen/Non-Kahler/research/sources/Demailly-analytic-methods.pdf).


### demailly94_full_hessian

**Location:** Regularization paragraph and unbounded-p extension of lemma77

**Status:** matched_and_applicable.

arXiv:2011.09637 Theorem 2.6 and arXiv:1909.08820 Theorem 2.2 state singularity attenuation results rather than the requested full base-fiber Hessian formula. arXiv:math/0402029 Theorem 5.2 imposes a curvature positivity setting and is not the needed general statement. None is accepted as the exact match.

Closedness belongs to T and alpha_D, while gamma is only a continuous real (1,1)-form. The potential is arbitrary quasi-psh. The auxiliary curvature form is smooth and semipositive; a large A_D omega works regardless of theta. The full estimate includes mixed and vertical tangent directions. The source's lambda is the logarithmic derivative of Psi+K0,D t^2.

With ddc_here=i/(2pi)partial barpartial, take T_D=ddc_here p, alpha_D=0, psi_D=p/2 and gamma=-theta. Then ddc_D Psi_D=ddc_here R_t p. Rename K0=2K0,D and A=A_D/2 so lambda_here=2lambda_D. The formula becomes precisely the type used in the proof, with unchanged coefficient of theta and rescaled fixed numerical constants.

p is genuine quasi-psh and globally L1. Section 3's error estimates use local integrals, logarithmic averaged growth and Lelong-type bounds for positive corrected Hessians; a finite L-infinity norm or global lower bound is absent. Compactness and the fixed p yield constants uniform in x and small t. Positive-radius smoothing follows from the smooth-kernel change of variables. The monotone limit is the canonical p. Only local lower bounds away from Z are used in minimizing-radius exclusion.

The submitted correction R_t p+Kt^2+Kt has derivative lambda_here+2(K-K0)t^2+Kt. It is not the source's Remark 4.7 correction Psi_D+t, whose derivative is lambda_D+t-2K0,D t^2. Direct vertical Hessian and Young estimates validate the submitted variant.

The author PDF was indexed with the exact Theorem 4.1 formula. Direct PDF web open failed, but the local primary PDF/text was fully available; existing page images for printed pages 12 and 16 were visually inspected.

Primary web source: [Demailly94, equations (3.1)-(3.2), Proposition 3.8 and its proof pp.8-12, Theorem 4.1 p.12 and proof pp.13-16, Remarks 4.6 and 4.7 p.16.](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization_flow.pdf).

Local source: [/Users/mingchen/Non-Kahler/research/sources/Demailly94-flow.pdf](/Users/mingchen/Non-Kahler/research/sources/Demailly94-flow.pdf).


### lemma77_prior_method

**Location:** Reference to lem:general-kiselman-modulus

**Status:** accepted_prior_method_with_extension_checked.

The previous audit concerns a globally bounded u and records the full-Hessian absorption, strict logarithmic convexity, cap localization, and constant-form freezing. Its stability and smoothing gradient inputs are not accepted for unbounded p by this proof.

The current audit reconstructs every relevant step: Demailly applies directly to L1 p, all constants remain fixed, the objective is localized on a compact radius interval only over compact neighborhoods off Z, and the resulting lower current bound is proved there and then extended. The previous theorem's global boundedness, one-sided stability, Lp equation, and gradient estimate are not imported.

Local source: [/Users/mingchen/Non-Kahler/research/rethlas/verification/results/local_big_continuity_01/verification_report.md](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/local_big_continuity_01/verification_report.md).


### kiselman_minimum

**Location:** Localized capped radial minimum

**Status:** matched_and_applicable.

The unrelated dynamical and group-orbit lemmas do not match. Proposition 8.5 of arXiv:1806.06033 requires a C2 function attaining its fiber minimum strictly in the interior, so that returned special version cannot justify the cap case and was not used.

The full principle requires a pseudoconvex total domain, connected tube fibers, and invariance under imaginary translations in the fiber. It does not require that the infimum be attained inside the open fiber.

After local radial localization and a quadratic correction for the frozen lower form, the total domain is a coordinate ball times a strip. The corrected function is psh and invariant; the finite fiber infimum equals the capped infimum even if the cap minimizes. All hypotheses fit.

Primary web source: [Deng–Wang–Zhang–Zhou, A new proof of Kiselman's minimum principle for plurisubharmonic functions, Theorem 1.1 (tube version) and Theorem 1.2 (Reinhardt version), p.1.](https://arxiv.org/pdf/1810.12733).


### removable_singularities

**Location:** Extension across Z

**Status:** accepted_theorem_exact_lower_form_extension_checked.

This precise standard theorem is expressly permitted by the user. It applies to Phi plus a constant-form quadratic correction, not directly to a potential for a nonclosed lower form.

For B=theta+(Ac+epsilon(delta))omega, freeze B at z0 up to eta beta; extend Phi+q with ddc q=B(z0)+eta beta; obtain ddc Phi>=-B-2eta beta on each small ball. Patch the local positivity for fixed eta and then let eta decrease to zero. Continuity of q identifies all extensions, and continuity of R_delta h preserves the obstacle bound.


### conditional_homogeneous_replacement

**Location:** Contact proof on B_r

**Status:** conditionally_accepted_application_checked.

The exact source theorem thm:ball-homogeneous-replacement was read. This statement is expressly accepted as a conditional prerequisite. Its independent audit local_homogeneous_dirichlet_01 must also pass for the book's inclusion decision; the present audit certifies neither its proof nor that audit's outcome.

Continuity is proved first, so boundary p and the competitor p on the closed ball meet the prerequisite. Only its continuous solvability, domination and homogeneous equation are used. The fixed scalar trace bound proves sufficient obstacle slack, and collar/max approximants prove theta-psh pasting in the original background.

Local source: [/Users/mingchen/Non-Kahler/book/author/section_local_homogeneous_dirichlet.tex:23](/Users/mingchen/Non-Kahler/book/author/section_local_homogeneous_dirichlet.tex:23).


## Findings, limits, and persistence

Critical errors: none.

Gaps: none.

Repair hints: empty, as required by the strict verdict rule.

The author-site fetch failures are documented retrieval limitations resolved by reading the available primary sources; they are not unresolved mathematical-reference gaps. No prohibited contact theorem was used. The conditional prerequisite's proof was not audited here.

The final normalized records are in [audit_details.json](audit_details.json). The memory channels retain the ordered statement checks, source comparisons, zero-issue finding, report, and run events. Items 1 and 3 have later revisions spelling out the operator normalization; those revisions supersede the earlier shorthand records and are the versions reproduced here.

Final output: [verification.json](verification.json).

