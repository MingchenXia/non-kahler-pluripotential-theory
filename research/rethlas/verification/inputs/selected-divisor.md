Run_id: selected_divisor_01

Run scope: Check the three proposed statement extensions through the normal Rethlas workflow. The parent owns the manuscript release and Git publication. Restrict writes to the normal verifier tools/runtime/memory/results. Leave all book, editorial, blueprint, status and changelog files, frozen inputs and historical results unchanged. Do not commit or push.

Statement: In the divisorial-threshold proposition and its semipositive and nef divisor corollaries, uniform integrability along one smooth maximizing Gauduchon sequence suffices. The old global root-tail hypothesis remains a sufficient special case. The geometric proofs are retained. Check the weakening of hypotheses, every zero/finite-domain issue, existence of a current cluster, and each resulting contradiction. No novelty claim. No regularity or exact equation is claimed from the selected-sequence condition.

Standing setting: X is a connected compact complex n-manifold, n>=2, omega is a smooth Hermitian form, dV is a smooth strictly positive probability volume, f is nonnegative nonzero in L1(dV), p=f^(1/n), b=b_omega(f). G_omega is the compact family of positive ddc-closed (n-1,n-1) currents normalized by integral omega wedge T=1. Smooth maximizing sequences consist of smooth strictly positive T_j in this family. Gamma_0(T)=k_T dV is its determinant-weighted measure, defined using the full matrix coefficient measure; D_p(T)=integral p k_T dV. Pairings with a fixed smooth (1,1) form are current-continuous. Never define [E] wedge T for singular T.

Accepted internal inputs, with scopes:
1. The subsolution threshold is finite for nonzero f. b>0 iff the root p is in the finite root space D_omega, and rho_omega(p)=b^(-1/n)>0. The supremum of D_p over smooth strictly positive tests and over G_omega equals rho, even when the root norm is infinite. A subsolution MA_ext(u)>=c f dV with c>0 gives b>=c.
2. For p in D_omega^0 (the closure of bounded roots), all densities p k_T, T in G_omega, are uniformly integrable. For arbitrary nonzero p in D_omega, if T_j is a maximizing sequence, T_j->T weakly and p k_Tj is uniformly integrable, then D_p(T)=rho and p k_Tj dV converges weakly to p k_T dV (prop:selected-gauduchon-attainment; selected_gauduchon_limits_01 returned correct). This is an accepted criterion, not unrestricted upper semicontinuity of D_p. The parent reread its full proof.
3. For any smooth strictly positive normalized Gauduchon form T and subsolution MA_ext(u)>=c f dV, the measure R=(omega+ddc u) wedge T-c^(1/n) p k_T dV is positive and has mass 1-c^(1/n)D_p(T). If omega+ddc u>=[E], its restriction to Supp(E) dominates [E] wedge T. Poincare--Lelong and distributional Stokes identify this last mass with integral beta_E wedge T for a smooth closed representative beta_E. The smooth infimum of this pairing is kappa_omega(beta_E); kappa>0 is equivalent to bigness in the smooth-test criterion.
4. For a smooth semipositive beta_E with matrix B, a normalized current T with zero beta_E pairing has tr(B P_T)=0 almost everywhere for its full coefficient measure sigma_T. Wherever B is nonzero, this forces P_T singular and hence Gamma_0(T)=0 there. Gamma_0 has density k_T with respect to dV. Zero determinant does not imply zero trace current.
5. If beta is nef and its fixed-density variational volume lambda_mu(beta)>0 for a smooth positive probability mu, every T in G_omega annihilating beta has Gamma_0(T)=0 (prop:nef-annihilator-determinant). Nefness gives lambda_mu(beta)>=0 for every such mu. This is a fixed-density conclusion; do not identify it with bigness or claim a uniform positive lower mass.
6. The exceptional-curve smoothing-obstruction example and the Hopf illustration are unchanged. On the Hopf threefold used in the book, D_omega^0=L3, and the hyperplane class has a nowhere zero smooth semipositive representative of rank two. The previously proved divisorial removal gives omega+ddc u>=a[H] when u has a positive generic coefficient a along H.

Requested audit: The first proposition still needs no uniform integrability for coefficient loss, annihilation by every smooth maximizing cluster, nonbigness, or the proper exposed-face conclusion. UI is used only to make a chosen cluster maximize D_p. The two following corollaries assume b>0 explicitly, so their finite root space and positive maximum are justified before applying the selected criterion. Compactness supplies at least one cluster from the chosen sequence. The older p in D_omega^0 conclusions and Hopf illustration follow immediately. This does not assert that selected UI is equivalent to the global root-tail condition, that every Gauduchon current is smooth-approximable, or that this hypothesis gives an exact equation.

Candidate texts (the named labels and all geometric proof steps are already present; only the indicated conditional clauses and three-sentence transition are modified):

\subsection{Divisorial components of threshold subsolutions}

The linear Gauduchon threshold of \cref{cor:gauduchon-threshold} controls how much a divisorial component lowers the coefficient in a Monge--Amp\`ere inequality. For this subsection, fix a Hermitian form $\omega$ on a connected compact complex manifold of dimension $n\geq2$, a smooth probability volume $\mathrm{d}V$, and a nonzero $0\leq f\in L^1(\mathrm{d}V)$. Write $p=f^{1/n}$ and $b=b_\omega(f)$.

\begin{proposition}\label{prop:threshold-divisorial-constraint}
Suppose $u\in\PSH(X,\omega)$ satisfies
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(u)\geq c f\,\mathrm{d}V,
 \qquad \omega+\ddc u\geq[E],
\]
where $c>0$ and $E$ is an effective real divisor. Let $\beta_E$ be a smooth closed representative of its Bott--Chern class, and put $\kappa=\kappa_\omega(\beta_E)$. Then $b>0$, $0\leq\kappa<1$ and
\begin{equation}\label{eq:divisorial-coefficient-loss}
 c\leq b(1-\kappa)^n.
\end{equation}
If $c=b$, every smooth maximizing sequence $(T_j)$ for $D_p$ satisfies
\[
 \int_X\beta_E\wedge T_j=\int_X[E]\wedge T_j\longrightarrow0.
\]
Every weak cluster current $T$ therefore satisfies $\int_X\beta_E\wedge T=0$, and the class of $E$ is not big. If the densities $p k_{T_j}$ of the chosen sequence are uniformly integrable, every such cluster current maximizes $D_p$. In particular, this holds for every smooth maximizing sequence when $p\in\mathcal D_\omega^0$.
\end{proposition}
\begin{proof}
The subsolution characterization gives $b\geq c>0$. For a smooth strictly positive normalized Gauduchon form $T$, \cref{lem:unbounded-gauduchon-trace-density} shows that
\[
 R=(\omega+\ddc u)\wedge T-c^{1/n}p k_T\,\mathrm{d}V
\]
is positive, with mass $1-c^{1/n}D_p(T)$. The density term gives no mass to the support of $E$, whereas $[E]\wedge T$ is supported there. Restricting the positive measure $R$ to that support and using $\omega+\ddc u\geq[E]$ gives
\[
 \int_X[E]\wedge T\leq R(X)=1-c^{1/n}D_p(T).
\]
Write $[E]=\beta_E+\ddc\ell_E$ by the Poincar\'e--Lelong formula. Since $\ell_E$ is locally integrable and $T$ is smooth and $\ddc$-closed, distributional Stokes identifies the left side with $\int_X\beta_E\wedge T$. It is nonnegative for every such test, so $\kappa\geq0$. Also $D_p(T)>0$, which gives $\kappa<1$. Taking the supremum of $D_p(T)$ and using $\rho_\omega(p)=b^{-1/n}$ proves \eqref{eq:divisorial-coefficient-loss}.

If $c=b$ and $(T_j)$ is maximizing, the right side of the preceding measure bound tends to zero. Pairing with the fixed smooth form $\beta_E$ is continuous under current convergence, proving the cluster assertion. Equation~\eqref{eq:divisorial-coefficient-loss} forces $\kappa=0$, so \cref{cor:gauduchon-threshold} excludes bigness. Uniform integrability along the chosen sequence gives the maximizing assertion by \cref{prop:selected-gauduchon-attainment}. When $p\in\mathcal D_\omega^0$, \cref{thm:integrable-current-attainment} supplies this condition for every sequence.
\end{proof}

At the threshold $c=b$, if $E\ne0$, the vanishing pairing defines a nonempty proper exposed face of the weak closure of smooth strictly positive normalized Gauduchon forms. Indeed, this closure is compact and convex; the pairing with $\beta_E$ is continuous and nonnegative there, and it is strictly positive on every smooth strictly positive member. The proposition places every cluster of a smooth maximizing sequence on this face. This assertion concerns that closure; it does not assert that every normalized Gauduchon current is a limit of smooth ones. Nor does the smooth pairing $\int_X\beta_E\wedge T$ define $[E]\wedge T$ for a singular $T$.

\input{author/section_threshold_divisorial_geometry}

\input{author/section_nef_divisor_threshold}

These are necessary conditions on divisorial singularities at the maximal global coefficient. They do not apply unchanged to a smaller coefficient or to a threshold defined within a prescribed singularity type. Determining which annihilating currents occur, and whether these conditions can be supplemented to characterize the possible divisorial components, remains a geometric realization problem. No identification with a null locus or a non-K\"ahler locus is asserted.


\begin{example}\label{ex:gauduchon-current-smoothing-obstruction}
The weak closure of smooth strictly positive normalized Gauduchon forms can be smaller than $\mathscr G_\omega$, even on a K\"ahler surface. Let $X$ be the blowup of $\mathbb P^2$ at one point and $C$ its exceptional curve. Fix a K\"ahler form $\omega$ and a smooth closed representative $\beta_C$ of $\{C\}$. Then
\[
 T_C=\frac{[C]}{\int_C\omega}\in\mathscr G_\omega,
 \qquad
 \int_X\beta_C\wedge T_C=\frac{-1}{\int_C\omega}<0.
\]
Every smooth strictly positive $T\in\mathscr G_\omega$ instead satisfies
$\int_X\beta_C\wedge T=\int_C T>0$.
\end{example}
\begin{proof}
The integration current $[C]$ is positive and closed, so its normalization belongs to $\mathscr G_\omega$. Its pairing with the smooth form $\beta_C$ is the self-intersection $C^2=-1$, computed in \cref{ex:gaud-metric-blowup}. For smooth $T$, the Poincar\'e--Lelong formula and $\ddc T=0$ give the second identity. The pairing with the fixed smooth $\beta_C$ is continuous under current convergence. It is therefore nonnegative on the weak closure of these smooth tests, which excludes $T_C$.
\end{proof}

The example reflects the two positivity criteria: smooth Gauduchon tests detect pseudoeffectivity by \cref{thm:lamari}, whereas all currents in $\mathscr G_\omega$ test nefness by \cref{thm:smooth-cone-current-duality}.

The next two corollaries use uniform integrability along one smooth maximizing sequence. The root-tail condition $p\in\mathcal D_\omega^0$ is sufficient, since it gives $b>0$ and uniform integrability for the entire test family.

\Needspace{12\baselineskip}
\begin{corollary}\label{cor:semipositive-divisor-exclusion}
Assume $b>0$ and that $D_p$ has a smooth maximizing sequence $(T_j)$ with uniformly integrable densities $p k_{T_j}$. Let $E$ be an effective real divisor whose class has a smooth semipositive representative $\beta_E$. If
\[
 \int_{\{\beta_E=0\}}f\,\mathrm{d}V=0,
\]
no subsolution at the threshold $b_\omega(f)$ satisfies $\omega+\ddc u\geq[E]$.
\end{corollary}
\begin{proof}
If such a subsolution existed, \cref{prop:threshold-divisorial-constraint} would supply a maximizing current $T\in\mathscr G_\omega$ with $\int_X\beta_E\wedge T=0$. In the matrix-density notation of \cref{sec:weak-gauduchon-duality}, write $B$ for the matrix of $\beta_E$. Positivity makes $\operatorname{tr}(BP_T)=0$ for $\sigma_T$-almost every point. Wherever $B\ne0$, this forces $P_T$ to be singular: a positive definite $P_T$ would have strictly positive trace against the nonzero positive semidefinite $B$. Thus $\Gamma_0(T)$ is supported on $\{\beta_E=0\}$. It equals $k_T\,\mathrm{d}V$ by \cref{thm:gaud-determinant-subcritical}. The hypothesis gives $p k_T=0$ almost everywhere, contradicting $D_p(T)=\rho_\omega(p)>0$.
\end{proof}

For example, the hyperplane divisor $H$ on the Hopf threefold has a smooth semipositive representative of rank two everywhere. By \cref{cor:hopf-lower-mass,prop:root-uniform-tails}, one has $\mathcal D_\omega^0=L^3$ on this example. Hence, for every nonzero nonnegative $L^1$ density, a threshold subsolution has zero generic divisorial coefficient along $H$. Otherwise divisorial removal, as in \cref{prop:divisorial-gaud-feasibility}, would give $\omega+\ddc u\geq a[H]$ for some $a>0$, contradicting the corollary applied to $aH$. This exclusion uses no bounded mass property. It is stronger here than nonbigness alone: the residual formulas of \cref{prop:hopf-divisorial-threshold} allow a positive coefficient along $H$ at smaller equation constants.


\begin{corollary}\label{cor:nef-divisor-threshold-volume}
Assume $b>0$ and that $D_p$ has a smooth maximizing sequence $(T_j)$ with uniformly integrable densities $p k_{T_j}$. Suppose a subsolution at $b$ satisfies $\omega+\ddc u\geq[E]$ for an effective real divisor $E$ whose Bott--Chern class is nef. Then
\[
 \lambda_\mu(\beta_E)=0
\]
for every smooth positive probability measure $\mu$, where $\beta_E$ is any smooth closed representative of that class.
\end{corollary}
\begin{proof}
By \cref{prop:threshold-divisorial-constraint}, there is a maximizing current $T\in\mathscr G_\omega$ with $\int_X\beta_E\wedge T=0$. If $\lambda_\mu(\beta_E)>0$, \cref{prop:nef-annihilator-determinant} gives $\Gamma_0(T)=0$. It follows that $D_{f^{1/n}}(T)=0$, contradicting its positive maximal value. Since nefness gives $\lambda_\mu(\beta_E)\geq0$, the conclusion follows for each $\mu$.
\end{proof}

This criterion uses nefness and the variational volume, without requiring a smooth semipositive representative. It complements \cref{cor:semipositive-divisor-exclusion}: the Hopf hyperplane class has zero variational volume, yet its nowhere vanishing semipositive representative excludes a component at the threshold. Neither argument identifies positive nef volume with bigness or classifies all possible divisorial components.
