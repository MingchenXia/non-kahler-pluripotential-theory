Run_id: bounded_subsolution_01

Statement: Audit every statement and full proof in section_bounded_subsolution.tex, supplied below. Main theorem theta>=0 big, psi boundedthetaPSH,nu=MApsi,f>=0 boundednu-measurable, integral f dnu>0,lambda>0 =>unique bounded u MAu=exp(lambda u)fnu. NoBMP/PVP, no continuous density with respect to smooth volume assumed. Also audit arbitrary-background mixed inequality for smooth-volume densities via constant-form freezing from the classical local closed inequality, and uniform mixed reference trace for normalized boundedv with varying oscillation but fixed boundedpsi, including exact torsion coefficient(n-1)(n-2), dimensions1/2, weightedCLN and all rough limits.

Accepted inputs: classical LOCAL mixedMA inequality for boundedpsh with Lebesgue densities(Dinew arxiv0705.0974v1Theorem1.2); local boundedBT/current/gradient/Stokes/chain/quasi-continuity/capacity weightedcontinuity; local weightedCLN,normalizedqpsh L1compactness; boundedexactHermitian smoothdecreasingregularization(compactness_regularization_01); semipositivegenuineenvelopecontactandanybackgroundorderedcontact(local_contacts_01+penalized_contacts_01); individualboundednoncollapseandboundedexponentialorder(singular_domination_01); bigboundedLp exponentialexistence(big_lp_equations_01). Commonbarrierdominatedcontinuitycor:common-barrier-continuity andfixedNPPexponentialintegrals in section_relative_compactness.tex are being independentlychecked common_barrier_compactness_01: inspect report; accept conditionally ifpending, do not reprove entire prerequisite. Proof targets are NOT accepted as imported fromALS5.1 orNguyen1.9. Audit smoothpositivef approximation, boundeddensityofrooftop, uniformbarriers, capacitypassage, approximationfj forRadonnu, mixedinequalitypassfromsmooth-volume approximants, normalizationcontradictionM_j->infty, lowerbarrierandtotalvariationpass. Definitionsbigonlygenuinepositivecurrentrho,notanalytic. Checkbookcitationaccuracy andnormconvention i/(2pi). Readonlybook. Produce usual verificationreport.

Proof:

\section{A bounded subsolution theorem}

We next allow a density with respect to the Monge--Amp\`ere measure of a bounded potential. Such a measure may be singular with respect to smooth volume. Two preparatory facts explain how its density controls the normalization of a solution.

\begin{lemma}[Mixed inequality for smooth-volume densities]\label{lem:nonclosed-mixed-density}
Let $\theta$ be any smooth real background, and let $u,v$ be bounded $\theta$-plurisubharmonic functions. If
\[
 \theta_u^n\geq f\,dV,\qquad\theta_v^n\geq g\,dV,
 \qquad f,g\geq0,
\]
then
\[
 \theta_u^k\wedge\theta_v^{n-k}
 \geq f^{k/n}g^{(n-k)/n}\,dV,\qquad0\leq k\leq n.
\]
\end{lemma}
\begin{proof}
The standard local mixed Monge--Amp\`ere inequality for bounded plurisubharmonic functions is the input here; it concerns ordinary closed local Hessians and measurable smooth-volume densities, as stated in \cite[Theorem 1.2]{Dinew09}. We explain why no closedness of $\theta$ is required in its present use.

Fix a coordinate chart with Euclidean form $\kappa$ and $\eta>0$. On a sufficiently small ball centered at $x$, the constant coefficient form $\beta=\theta(x)$ satisfies
\[
 \beta-\eta\kappa\leq\theta\leq\beta+\eta\kappa.
\]
Choose a quadratic $q$ with $\ddc q=\beta+\eta\kappa$. The functions $u+q,v+q$ are bounded and plurisubharmonic on the ball, and their Hessians dominate $\theta_u,\theta_v$. Their top powers therefore dominate $f\,dV,g\,dV$. The local mixed inequality applies. Since
\[
 \theta+2\eta\kappa\geq\beta+\eta\kappa,
\]
positivity transfers the resulting mixed lower bound to the background $\theta+2\eta\kappa$. In a fixed finite atlas $\kappa\leq C\omega$. The small balls cover $X$, so the bound holds globally with background $\theta+2C\eta\omega$. Let $\eta\downarrow0$ in the bounded polynomial expansion of the products. This proves the assertion. This freezing argument also recovers the smooth-volume inequality used in \cite[Lemma 1.9]{Nguyen16}.
\end{proof}

\begin{lemma}[A bounded reference trace]\label{lem:bounded-reference-trace}
Let $\theta\geq0$ and fix a bounded $\psi\in\PSH(X,\theta)$. There is a constant $C_\psi$ such that
\[
 \int_X\theta_v\wedge\theta_\psi^{n-1}\leq C_\psi
\]
for every bounded $v\in\PSH(X,\theta)$ with $\sup_Xv=0$.
\end{lemma}
\begin{proof}
Choose a fixed Hermitian metric $\Omega\geq\theta$. All currents in the left side are positive, and $\Omega_\psi\geq\theta_\psi$. Bounded Stokes gives
\[
 \int_X\theta_v\wedge\theta_\psi^{n-1}
 \leq\int_X\theta\wedge\Omega_\psi^{n-1}
       +\int_Xv\,\ddc(\Omega_\psi^{n-1}).
\]
The first term has a fixed bound. For $n\geq2$, the exact differentiation formula is
\[
 \ddc(\Omega_\psi^{n-1})
 =(n-1)\ddc\Omega\wedge\Omega_\psi^{n-2}
 +(n-1)(n-2)d\Omega\wedge\dc\Omega\wedge\Omega_\psi^{n-3},
\]
where the second term is absent for $n=2$. Its absolute value is bounded by fixed multiples of the corresponding positive mixed measures with $\Omega^2$ and $\Omega^3$ in place of the smooth torsion factors. The weighted local Chern--Levine--Nirenberg inequality from \cref{chap:weak-equations} bounds the integrals of $|v|$ against these measures. Indeed, on each larger coordinate ball add fixed smooth corrections to $v$ and $\psi$, shift the first to be negative, expand in the corrected positive Hessian of $\psi$, and apply that inequality on a smaller ball. The bound is
\[
 C(1+\|\psi\|_\infty)^n(1+\|v\|_{L^1(X)}).
\]
Normalized $\theta$-plurisubharmonic functions have uniformly bounded $L^1$ norms. Summing the local bounds proves the assertion. For $n=1$, the second integral is zero by Stokes, and the result is immediate.
\end{proof}

The trace here is tested against a fixed bounded reference. It is different from an upper bound for $\int_X\theta_v^n$ when all factors vary. Its proof uses weighted local estimates for the torsion terms, while the smooth-volume normalizations earlier used a Gauduchon metric.

\Needspace{15\baselineskip}
\begin{theorem}[A bounded subsolution theorem]\label{thm:bounded-subsolution}
Let $\theta$ be semipositive and big on a compact complex manifold. Suppose
\[
 \mu=f\,\mathrm{MA}_\theta(\psi),\qquad
 \psi\in\PSH(X,\theta)\cap L^\infty(X),\qquad
 0\leq f\in L^\infty(\mathrm{MA}_\theta(\psi)),
\]
and $\mu(X)>0$. For every $\lambda>0$ there is a unique bounded $u\in\PSH(X,\theta)$ satisfying
\[
 \mathrm{MA}_\theta(u)=e^{\lambda u}\mu.
\]
No bounded mass hypothesis on $X$ is required.
\end{theorem}
\begin{proof}
We reconstruct \cite[Theorem 5.1]{ALS26}. Write $\nu=\mathrm{MA}_\theta(\psi)$, a finite non-pluripolar measure.

\emph{Smooth strictly positive density.} First suppose $f$ is smooth and strictly positive. Choose a Hermitian $\Omega\geq\theta$ and smooth $\Omega$-plurisubharmonic $\psi_j\downarrow\psi$, using the bounded regularization theorem. The rooftops
\[
 q_j=P_\theta(\psi_j)
\]
are uniformly bounded and decrease to $\psi$: they lie between $\psi$ and $\psi_j$. Contact support and ordered contact in background $\Omega$ give
\[
 \mathrm{MA}_\theta(q_j)
 \leq\mathbf1_{\{q_j=\psi_j\}}\Omega_{\psi_j}^n.
\]
Each right side has a bounded density with respect to smooth volume. Moreover $\mathrm{MA}_\theta(q_j)(X)>0$ by individual noncollapse. The bounded big-background theorem therefore supplies $u_j$ with
\[
 \mathrm{MA}_\theta(u_j)=e^{\lambda u_j}f\,
                                     \mathrm{MA}_\theta(q_j).
\]
Since $f$ is bounded above and away from zero, $q_j-C$ and $q_j+C$ are lower and upper barriers for a fixed $C$. More explicitly choose $C$ so that
$e^{\lambda(q_j-C)}f\leq1\leq e^{\lambda(q_j+C)}f$ for all $j$. Exponential order then gives
$q_j-C\leq u_j\leq q_j+C$.

Extract an $L^1$ limit $u$, still uniformly bounded. The moving domination
\[
 \mathrm{MA}_\theta(u_j)\leq C'\Omega_{\psi_j}^n
\]
and \cref{cor:common-barrier-continuity}, with reference zero, give convergence in capacity. Bounded capacity continuity with the quasi-continuous weights $e^{\lambda u_j}f$ gives
\[
 \mathrm{MA}_\theta(u)=e^{\lambda u}f\nu.
\]

\emph{Bounded measurable density.} Choose positive smooth $f_j$ with a common upper bound, converging to $f$ in $L^1(\nu)$. Such an approximation follows from regularity of the finite measure, continuous approximation on large compact sets, and smooth uniform approximation of the continuous functions; truncation to a fixed bounded interval and addition of a positive constant tending to zero preserve the bounds and convergence. The first step gives bounded $u_j$ with
\[
 \mathrm{MA}_\theta(u_j)=e^{\lambda u_j}f_j\nu.
\]
A fixed $\psi-C$ is a lower barrier, since
$e^{\lambda(\psi-C)}f_j\leq1$ for all $j$. Hence $u_j\geq\psi-C$. The upper bound requires a separate argument because $\inf_Xf_j$ can tend to zero.

The construction in the first step also gives the mixed inequality
\begin{equation}\label{eq:bounded-subsolution-mixed}
 \theta_{u_j}\wedge\theta_\psi^{n-1}
 \geq e^{\lambda u_j/n}f_j^{1/n}\nu.
\end{equation}
To see this without assuming a mixed inequality for arbitrary singular measures, use that step's approximants $u_{j,k}$ and $q_k$. Their top measures have smooth-volume densities and
\[
 \mathrm{MA}_\theta(u_{j,k})
     =e^{\lambda u_{j,k}}f_j\mathrm{MA}_\theta(q_k).
\]
Apply \cref{lem:nonclosed-mixed-density} to $(u_{j,k},q_k)$. For this fixed $j$ both sequences are uniformly bounded and converge in capacity to $(u_j,\psi)$. Bounded weighted continuity passes the mixed inequality to the limit and yields \eqref{eq:bounded-subsolution-mixed}.

Put $M_j=\sup_Xu_j$, $v_j=u_j-M_j$ and $c_j=e^{\lambda M_j}$. If the $M_j$ were unbounded above, extract $M_j\to+\infty$ and then $v_j\to v$ in $L^1(X)$, with $v$ a genuine normalized potential. By \cref{lem:fixed-npp-integrals},
$e^{\lambda v_j/n}\to e^{\lambda v/n}$ in $L^1(\nu)$. The inequalities
\[
 |f_j^{1/n}-f^{1/n}|^n\leq|f_j-f|,
 \qquad0\leq f_j\leq L,
\]
then give
\[
 \int_X e^{\lambda v_j/n}f_j^{1/n}\,d\nu
 \longrightarrow\int_Xe^{\lambda v/n}f^{1/n}\,d\nu>0.
\]
The last integral is positive because $\mu(X)>0$ and $\nu$ gives no mass to the pole set of $v$. Integrate \eqref{eq:bounded-subsolution-mixed} and apply \cref{lem:bounded-reference-trace}. For some $a>0$ along the extraction, this gives
\[
 a c_j^{1/n}\leq
 \int_X\theta_{v_j}\wedge\theta_\psi^{n-1}\leq C_\psi,
\]
contradicting $M_j\to+\infty$. Thus $u_j$ is uniformly bounded above as well as below.

Extract an $L^1$ limit. Now $\mathrm{MA}_\theta(u_j)\leq C''\nu$, so \cref{cor:common-barrier-continuity} gives capacity and weak Monge--Amp\`ere convergence. The right sides converge in total variation: use the fixed-measure exponential convergence and
\[
 \int_X|e^{\lambda u_j}f_j-e^{\lambda u}f|\,d\nu
 \leq C\|f_j-f\|_{L^1(\nu)}
       +\|f\|_\infty\int_X|e^{\lambda u_j}-e^{\lambda u}|\,d\nu.
\]
Consequently $\mathrm{MA}_\theta(u)=e^{\lambda u}\mu$. Uniqueness is bounded exponential order. Positivity of $\mu(X)$ was used in the normalization argument and cannot be omitted.
\end{proof}

This theorem permits a singular measure dominated by the Monge--Amp\`ere measure of one bounded potential. An arbitrary finite non-pluripolar measure is not assumed to have such a bounded density representation. The common reference in the theorem is the subsolution data needed for this step of the existence theory.
