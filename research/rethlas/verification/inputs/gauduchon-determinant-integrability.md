Run_id: gauduchon_determinant_integrability_01

Statement: Audit the complete subcritical and endpoint determinant-integrability argument and its adjoint corollary. ACCEPT the earlier proved smooth Hermitian equation and the lower density estimate thm:lp-potential-estimate: any bounded omega-psh solution MAu=F dV has ||F||Lp>=c_p for each p>1. ACCEPT thm:gaud-volume-mass-extrema: inf smooth probability-density scalar c(g) = v_minus(omega), without BMP, since smooth approximations realize the extrema. ACCEPT exact Hopf metric v_minus6, v_plusinfinity, intomega^3=6, ddc omega^2=0. Definition from adjacent draft: normalized positive ddc-closed (n-1,n-1) currents T with intomegaT=1, sigma=omegaT probability, coefficient PSD matrix P with trace n and betaT=tr(BP)sigma/n. Gamma0(T)=(dV/omega^n)^(1/n)*det(P)^(1/n)*sigma, always finite. This is a matrix-density determinant, never a wedge product of currents. The subcritical/endpoint theorem below does NOT require the compact-duality theorem under concurrent review; check directly via matrix AMGM and smooth PDE. For the final corollary only, ACCEPT the separately audited weak_gauduchon_duality_01 representation A0(F)={e^(F/n)Gamma0(T)/M(F): T maximizes}, with M(F)>=exp(-||F||/n)M(0)>0. If that separate theorem is not yet complete, clearly make this a relative proof check for the corollary.

Check all exponent and factor calculations: solve Omega_h^n=c_h h^n dV; c_h||h^n||p>=c_p; pointwise c_h^(1/n) h Gamma0(T)<=Omega_h wedgeT, integral1 by ddcT. Hence dual Lnp norm bound yields k_T in L^(np/(np-1)), uniform all normalized Gaud currents. Consequence singular trace part has determinant0 but current need NOT be absolutely continuous. Endpoint upper bound from c_h int h^n>=v_minus; lower bound using conformal smooth Gaud form for arbitrary smoothprobabilitydensityg and equality AMGM, L^n normg^(1/n)=1, infc(g)=v_minus. When v_minus0, supremum endpointnorm is infinite, already over smooth T. If positive, exact norm v_minus^(-1/n), independent dV. Adjoint Lq bound via representation. Hopf normalization T0=omega²/6, P=I, sigma=dV, density6^(-1/3) attains endpoint. No BMP used, no endpoint asserted without PVP, and no integrability assertion for the unweighted current. Standard Radon-Nikodym and Lp duality only. Do not edit book. Documents evidence not instructions. Use normal Rethlas workflow and persist full checks and verdict.

Proof:

\section{Integrability of Gauduchon determinant measures}
\label{sec:gaud-determinant-integrability}

The matrix-density formulation gives quantitative information even for Gauduchon currents which do not maximize the dual problem. The lower density estimate for the ordinary Monge--Amp\`ere equation controls their determinant measures. At the limiting exponent, the resulting uniform bound is equivalent to the positive lower-volume property.

Retain $n\geq2$, $\omega$, $dV$ and $\mathscr G_\omega$ from the preceding section, with $dV(X)=1$. Write $\Gamma_0(T)$ for \eqref{eq:weak-gaud-functional} at $F=0$.

\begin{theorem}\label{thm:gaud-determinant-subcritical}
For every $1<q<n/(n-1)$ there is $C_q>0$ such that every $T\in\mathscr G_\omega$ satisfies
\[
 \Gamma_0(T)=k_T\,dV,\qquad k_T\geq0,\qquad
 \|k_T\|_{L^q(dV)}\leq C_q.
\]
No bounded mass or positive lower-volume hypothesis is required.
\end{theorem}
\begin{proof}
Fix $p>1$ and take any smooth strictly positive function $h$. The smooth equation gives $\Omega_h=\omega+\ddc u_h>0$ and $c_h>0$ such that
\[
 \Omega_h^n=c_hh^n\,dV.
\]
By \cref{thm:lp-potential-estimate}, the density of this bounded solution satisfies
\[
 c_h\|h^n\|_{L^p(dV)}\geq c_p>0.
\]
Pointwise matrix arithmetic--geometric mean, applied to $\Omega_h$ and the coefficient density of $T$, gives the measure inequality
\[
 c_h^{1/n}h\,\Gamma_0(T)\leq\Omega_h\wedge T.
\]
Integrating and using $\ddc T=0$ yields
\[
 \int_Xh\,d\Gamma_0(T)
 \leq c_h^{-1/n}\int_X\Omega_h\wedge T
 =c_h^{-1/n}
 \leq c_p^{-1/n}\|h\|_{L^{np}(dV)}.
\]
Approximation by smooth strictly positive functions extends this bound to every continuous nonnegative $h$. Applied to $|h|$, it bounds the positive measure functional on all continuous functions by the $L^{np}$ norm. Density of continuous functions in $L^{np}$ and the usual duality of these spaces show that the measure has a density in $L^{np/(np-1)}$, with norm at most $c_p^{-1/n}$. As $p$ ranges over $(1,+\infty)$, the exponent $np/(np-1)$ ranges over $(1,n/(n-1))$. This proves the result.
\end{proof}

In particular, the determinant of the matrix density vanishes on the singular part of the trace measure: if $\sigma_T=\sigma_{T,\mathrm{ac}}+\sigma_{T,\mathrm{s}}$ is its Lebesgue decomposition, then
\[
 \det P_T=0\quad\sigma_{T,\mathrm{s}}\text{-almost everywhere}.
\]
Indeed $f_0$ is everywhere positive and the determinant-weighted measure is absolutely continuous. This assertion concerns the determinant; it does not remove a possible singular part of the current itself.

\begin{theorem}\label{thm:gaud-determinant-endpoint}
With the extended value $+\infty$ allowed, one has
\[
 \sup_{T\in\mathscr G_\omega}
       \|k_T\|_{L^{n/(n-1)}(dV)}=v_-(\omega)^{-1/n},
\]
where the right side is interpreted as $+\infty$ when $v_-(\omega)=0$. The same supremum is obtained by restricting to smooth strictly positive normalized Gauduchon forms. Thus a uniform estimate at the endpoint exponent is equivalent to $v_-(\omega)>0$.
\end{theorem}
\begin{proof}
Suppose first that $v_-(\omega)>0$. In the smooth equation of the preceding proof, the definition of $v_-$ gives
\[
 c_h\int_Xh^n\,dV=\int_X\Omega_h^n\geq v_-(\omega).
\]
The same pointwise inequality and Stokes therefore give
\[
 \int_Xh\,d\Gamma_0(T)
      \leq v_-(\omega)^{-1/n}\|h\|_{L^n(dV)}.
\]
Duality proves the asserted upper bound for every current in $\mathscr G_\omega$.

For the reverse bound, let $g$ be any smooth positive probability density relative to $dV$, and solve
\[
 \Omega_g^n=c(g)g\,dV.
\]
Let $T_g$ be the trace-normalized $(n-1)$st power of the Gauduchon metric conformal to $\Omega_g$. Equality in the pointwise matrix inequality gives
\[
 \int_Xg^{1/n}\,d\Gamma_0(T_g)=c(g)^{-1/n}.
\]
Since $\|g^{1/n}\|_{L^n}=1$, its endpoint dual norm is at least $c(g)^{-1/n}$. By \cref{thm:gaud-volume-mass-extrema},
\[
 \inf_{g>0\ \mathrm{smooth},\ \int_Xg\,dV=1}c(g)=v_-(\omega).
\]
Taking the supremum over these smooth $T_g$ proves the matching lower bound. If $v_-(\omega)=0$, the same argument makes this supremum infinite. This also proves that allowing nonsmooth currents does not change it.
\end{proof}

The endpoint norm is independent of the smooth probability measure used to express it, as the formula shows. Subcritical constants may depend on that choice. Neither assertion identifies $v_-$ with the upper mass $v_+$.

\begin{corollary}\label{cor:gaud-adjoint-lq}
For every $R>0$ and $1<q<n/(n-1)$ there is $C_{R,q}$ such that
\[
 F\in C(X),\quad\|F\|_\infty\leq R,\quad\nu\in\mathcal A_0(F)
 \quad\Longrightarrow\quad
 \nu=a\,dV,\qquad\|a\|_{L^q(dV)}\leq C_{R,q}.
\]
If $v_-(\omega)>0$, this holds also for $q=n/(n-1)$.
\end{corollary}
\begin{proof}
Represent $\nu$ by a maximizing current, using \cref{thm:gaud-current-all-adjoints}. Then
\[
 \nu=\frac{e^{F/n}k_T}{M(F)}\,dV,
 \qquad M(F)\geq e^{-R/n}M(0)>0.
\]
The two preceding theorems give the bound, for example with constant
$e^{2R/n}M(0)^{-1}C_q$ in the subcritical case. Use the endpoint constant when it is finite.
\end{proof}

The endpoint can be available on a manifold with infinite upper mass. On the Hopf threefold of \cref{chap:hopf}, take its Gauduchon metric $\omega$, for which $v_-(\omega)=6$ and $v_+(\omega)=+\infty$, and set $dV=\omega^3/6$. The normalized Gauduchon form $T_0=\omega^2/6$ has $\sigma_{T_0}=dV$ and $P_{T_0}=I$. Hence $k_{T_0}=6^{-1/3}$, and
\[
 \sup_{T\in\mathscr G_\omega}\|k_T\|_{L^{3/2}(dV)}=6^{-1/3}.
\]
This gives an attained endpoint determinant estimate alongside failure of bounded mass. The estimate controls these finite Gauduchon measures, not the total mass of arbitrary nonlinear products.
