Run_id: gauduchon_surface_uniqueness_01

Statement: Verify the supplied smooth mixed-form integration identity and its uniqueness consequence; then verify the compact Gauduchon surface corollary for smooth nonnegative density with zero set of empty interior. This is a bounded independent proof audit, not a novelty claim.

Accepted standard inputs: elementary smooth differential-form calculus and Stokes on compact manifolds without boundary; Hermitian matrix positivity and diagonalization; connectedness; definition ddc=i/(2pi)partial barpartial and dc=i/(4pi)(barpartial-partial). A Gauduchon metric satisfies ddc omega^(n-1)=0. You may inspect the original source construction only if needed to check the final scope comparison, but do not assume any new uniqueness result. Every assertion in the proof itself must be verified. Do not read or write book files except read-only input inspection. Write only this run's MCP memory and results using the prescribed tools; persist a full readable report alongside the final strict verification.json. Ordinary approval workflow only, never unsafe mode. No new external theorem is invoked. Check all normalization/sign conventions, real positivity of dw wedge dcw, bidegrees, Stokes sign, exact role of dense positivity, smoothness and dimension. Explicitly assess whether higher-dimensional Gauduchon alone justifies ddcT=0 (it does not appear to, and the draft does not claim it).

Proof:

\section{A Gauduchon uniqueness criterion on surfaces}
\label{sec:gauduchon-surface-uniqueness}

The preceding counterexample lives in dimension three. On a surface, the Gauduchon condition cancels precisely the integration-by-parts error in the smooth uniqueness argument, provided the density is positive on a dense set. The following identity makes that role explicit.

\begin{proposition}\label{prop:mixed-ddc-uniqueness}
Let $X$ be a connected compact complex manifold of dimension $n\geq2$, let $\omega$ be Hermitian, and let $u,v$ be smooth $\omega$-plurisubharmonic functions with
\[
 A^n=B^n=f\,dV,\qquad
 A=\omega+\ddc u,\quad B=\omega+\ddc v,
\]
where $dV$ is smooth and strictly positive. Put
\[
 w=u-v,\qquad
 T=\sum_{j=0}^{n-1}A^j\wedge B^{n-1-j}.
\]
Then
\begin{equation}\label{eq:mixed-uniqueness-defect}
 \int_X dw\wedge\dc w\wedge T
       =\frac12\int_X w^2\ddc T.
\end{equation}
If $\ddc T=0$ and $\{f>0\}$ is dense in $X$, then $u-v$ is constant.
\end{proposition}
\begin{proof}
The difference of powers factors as
\[
 0=A^n-B^n=\ddc w\wedge T.
\]
The product rule gives
\[
 \ddc(w^2)=2w\ddc w+2dw\wedge\dc w.
\]
Integrating against the smooth form $T$ and applying Stokes twice yields
\[
 \int_X\ddc(w^2)\wedge T=\int_Xw^2\ddc T.
\]
Substitution proves \eqref{eq:mixed-uniqueness-defect}.

Every mixed term in $T$ is semipositive, as is $dw\wedge\dc w$. When $\ddc T=0$, the nonnegative smooth integrand on the left has zero integral and therefore vanishes everywhere. At any point with $f>0$, both $A$ and $B$ are positive definite. In particular, the term $B^{n-1}$ shows that $dw\wedge\dc w\wedge T=0$ forces $dw=0$ at that point. Density of $\{f>0\}$ and continuity of $dw$ give $dw=0$ on all of $X$. Connectedness proves the assertion.
\end{proof}

\begin{corollary}\label{cor:gauduchon-surface-uniqueness}
Let $X$ be a connected compact complex surface and let $\omega$ be a Gauduchon metric. If $f\geq0$ is smooth and its zero set has empty interior, then two smooth normalized $\omega$-plurisubharmonic solutions of
\[
 (\omega+\ddc u)^2=cf\,dV
\]
with the same $c>0$ coincide.
\end{corollary}
\begin{proof}
In dimension two, $T=A+B$ and
\[
 \ddc T=2\ddc\omega=0,
\]
which is exactly the Gauduchon condition on a surface. Smooth nonnegative $f$ with zero set of empty interior is positive on a dense set. The proposition gives equality up to a constant; normalization removes that constant.
\end{proof}

This argument concerns smooth solutions and a Gauduchon background. It does not assert the result for every Hermitian metric on a surface or for all bounded solutions. Passing to a conformally Gauduchon metric changes the equation, so the conformal theorem does not remove the hypothesis. In higher dimension, $\ddc\omega^{n-1}=0$ alone does not make the mixed form $T$ above $\ddc$-closed; its error is the right side of \eqref{eq:mixed-uniqueness-defect}.
