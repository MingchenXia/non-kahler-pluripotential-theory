Run_id: hermitian_quantitative_regularization_01

Statement: Verify a bounded extension of the supplied quantitative Bergman regularization lemma to an arbitrary compact connected Hermitian manifold, with a CLOSED smooth background zeta. This is not a claim for a nonclosed background. The conclusion is only the displayed lower positivity bound uniform in zeta,phi,m and the one-sided multiplier-ideal singularity lower bound; it does not assert full analytic type or convergence. Also verify the final global coherent-ideal potential lemma in the same Hermitian setting. The old source audit transcendental_nakamaye_01 accepted the Kähler version; preserve its results and memory unchanged. This submission is a new proof in full, using Euclidean measures separately on the coordinate balls, classical singular Hörmander on balls, DEL00 Proposition1.2 with Euclidean Kähler volume and standard psh extension. Check each transition, especially the uniform overlap comparison and retention of the original smooth lower bound after extension across the analytic set. No bounded mass property is assumed.

References: SGPT is Mingchen Xia's supplied book at https://mingchenxia.github.io/Lectures/SGPT_final.pdf ; DemCADG is Demailly, Complex Analytic and Differential Geometry, https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf ; DEL00 is Demailly–Ein–Lazarsfeld, A subadditivity property of multiplier ideals, MichiganMathJ48(2000)137–156. Dem92, DPS01 and GR56 are the classical references listed in /Users/mingchen/Downloads/Transcendental Nakamaye theorem (Copy)/ComplexGeometry.bib. Internal forward references to the eventual ambient-current construction are motivation only, not premises.

Proof:

\subsection{Regularization with controlled positivity}

The next lemma is Demailly's regularization theorem \cite{Dem92,DPS01},
proved by the Bergman-kernel method, in a quantitative form: the loss of
positivity is $O(m^{-1})$, with a constant independent of the current
being regularized. The qualitative version, with an unspecified loss
$\epsilon_m\downarrow0$ but with the precise singularity type
$(m^{-1},\mathcal I(m\varphi))$, is \cite[Theorem~1.6.2]{SGPT}, and it
suffices for all the regularizations performed on $V$ below. The
$O(m^{-1})$ rate is needed exactly once, for the ambient current of
\cref{nk:sec:ambient}, whose positivity must be comparable in size to its
singularities; we include a complete proof. The loss of positivity comes only from
the gluing of the local Bergman kernels, and we only record the lower
bound on the singularities of $\varphi_m$, which is all that will be
used.

For $\delta>0$ and $N\ge1$, the \emph{regularized maximum}
$M_\delta\colon[-\infty,\infty)^N\to[-\infty,\infty)$ is defined by
\[
  M_\delta(t_1,\dots,t_N)\coloneqq \int_{\mathbf R^N}\max_i(t_i+\tau_i)
  \prod_{i=1}^N\frac1\delta\,\vartheta\Bigl(\frac{\tau_i}\delta\Bigr)
  \,\mathrm{d}\tau_1\cdots \mathrm{d}\tau_N,
\]
where $\vartheta\in C^\infty_c((-1,1))$ is a fixed even nonnegative
function with $\int\vartheta=1$. It has the following well-known
properties \cite[Chapter~I, Lemma~5.18]{DemCADG}: it is smooth, convex and
nondecreasing in each variable on $\mathbf R^N$;
$\max_it_i\le M_\delta(t)\le\max_it_i+N\delta$;
$M_\delta(t+c\mathbf 1)=M_\delta(t)+c$; and $M_\delta(t)$ does not
depend on $t_i$ on the set where
$t_i+\delta<\max_{j\ne i}(t_j-\delta)$, where it coincides with the
regularized maximum of the remaining variables. If $f_1,\dots,f_N$ are
smooth functions with $\zeta+\ddc f_i\ge\Gamma'$ for a smooth real
$(1,1)$-form $\Gamma'$, then
$\zeta+\ddc M_\delta(f_1,\dots,f_N)\ge\Gamma'$: by the chain rule,
$\ddc M_\delta(f_1,\dots,f_N)$ equals
$\sum_i\partial_iM_\delta\,\ddc f_i$ plus a form which is positive
semidefinite because $M_\delta$ is convex, and
$\partial_iM_\delta\ge0$ with $\sum_i\partial_iM_\delta=1$.
\begin{lemma}\label{nk:lem:regularization}
Let $(Z,\omega_Z)$ be a connected compact Hermitian manifold of
dimension $d$,
and let $\zeta$ be a smooth closed real $(1,1)$-form on $Z$. There
is a constant $c>0$, depending only on $(Z,\omega_Z)$ and not on
$\zeta$, with the following property. For every
$\varphi\in\PSH(Z,\zeta)$ and every integer $m\ge1$, there is a
quasi-psh function $\varphi_m$ on $Z$ such that
\begin{enumerate}[label=(\roman*),leftmargin=*,itemsep=.2em,topsep=.3em]
\item\label{nk:it:reg-positivity}
  $\zeta+\ddc\varphi_m\ge-\dfrac{c}{m}\,\omega_Z$;
\item\label{nk:it:reg-lower} locally on $Z$,
  $\varphi_m\ge m^{-1}\psi_{\mathcal I(m\varphi)}+O(1)$.
\end{enumerate}
\end{lemma}

The conclusion is deliberately one-sided: it does not assert analytic singularities of a prescribed type or convergence of this family. The constant in the positivity bound is uniform in the closed background; the locally bounded term in the singularity bound need not be uniform in $m$ or $\varphi$.
 
\begin{proof}
Put $\gamma_0\coloneqq -\zeta$, so that $\ddc\varphi\ge\gamma_0$.
On each coordinate ball $B_j$, write $\mathrm{d}\lambda_j$ for Euclidean
volume in its chosen coordinates. The local Hilbert spaces use these
Euclidean measures. Their comparison on fixed compact overlaps involves
only the coordinate charts, independently of $\zeta$, $\varphi$ and $m$.
 
\emph{Step 1: local Bergman weights.}
Fix once and for all, depending only on $Z$, a finite cover of $Z$ by
coordinate balls $\Omega_i$, a refinement of it by coordinate balls
$B_j^+$, $j=1,\dots,J$, and concentric balls
\[
  U_j\Subset V_j\Subset B_j\Subset B_j^+
\]
such that the $U_j$ cover $Z$. Whenever
$\overline V_j\cap\overline V_l\ne\varnothing$, the union
$B_j^+\cup B_l^+$
is contained in one of the balls, say $\Omega_{jl}$. We may write
$\gamma_0=\ddc H_{jl}$ on $\Omega_{jl}$ for a smooth function $H_{jl}$.
All coordinate metrics and coordinate volume measures are uniformly comparable on the finitely many compact overlaps. These comparison constants depend only on the fixed cover and $\omega_Z$.
 
Choose $h_j\in C^\infty(B_j^+)$ with $\ddc h_j=\gamma_0$, and set
$\psi_j\coloneqq \varphi-h_j$, which is psh on $B_j^+$. For an integer
$m\ge1$, let
\[
  \mathcal H_{j,m}\coloneqq \Bigl\{f\in\mathcal O(B_j):
     \|f\|_{j,m}^2\coloneqq \int_{B_j}|f|^2\mathrm{e}^{-m\psi_j}\,\mathrm{d}\lambda_j<\infty\Bigr\},
\]
let $(\sigma_{j,m,\ell})_\ell$ be an orthonormal basis, and define
\[
  K_{j,m}\coloneqq \sum_\ell|\sigma_{j,m,\ell}|^2,\qquad
  \psi_{j,m}\coloneqq \frac1m\log K_{j,m},\qquad
  \varphi_{j,m}\coloneqq \psi_{j,m}+h_j.
\]
The function $\psi_{j,m}$ is
psh, it is smooth outside the zero set of $K_{j,m}$, where it equals
$-\infty$, and
\begin{equation}\label{nk:eq:reg-local-positivity}
  \zeta+\ddc\varphi_{j,m}\ge0\qquad\text{on }B_j.
\end{equation}
 
\emph{Step 2: a uniform comparison on overlaps.}
Fix a pair $(j,l)$ with $\overline V_j\cap\overline V_l\ne\varnothing$.
On $B_j$ and $B_l$ we may write
\[
  h_j-H_{jl}=\Re a_j,\qquad h_l-H_{jl}=\Re a_l,
\]
with $a_j\in\mathcal O(B_j)$ and $a_l\in\mathcal O(B_l)$, since the two differences
are pluriharmonic on simply connected balls. Put $\Psi\coloneqq \varphi-H_{jl}$,
a psh function on $\Omega_{jl}$. Multiplication by $\mathrm{e}^{ma_j/2}$ is an
isometry from $\mathcal H_{j,m}$ onto the Hilbert space of holomorphic
functions on $B_j$ which are square integrable against
$\mathrm{e}^{-m\Psi}\mathrm{d}\lambda_j$, and similarly on $B_l$. Denoting by $\Psi_{j,m}$ and
$\Psi_{l,m}$ the corresponding Bergman weights, computed on $B_j$ and
on $B_l$ respectively with the common weight $\Psi$, the transformation
rule for Bergman kernels gives
\[
  \varphi_{j,m}=\Psi_{j,m}+H_{jl},\qquad
  \varphi_{l,m}=\Psi_{l,m}+H_{jl}.
\]
 
We now compare the two kernels. Choose a cut-off function
$\theta_{jl}\in C^\infty_c(B_j\cap B_l)$ with
$0\le\theta_{jl}\le1$, equal to $1$ on a
neighborhood of the compact set $\overline V_j\cap\overline V_l$, let
$r>0$ be the distance from $\overline V_j\cap\overline V_l$ to the
support of $\bar\partial\theta_{jl}$, and let $R$ be the diameter of
$B_l$, both computed in the coordinates of $B_l$. Fix
$x\in\overline V_j\cap\overline V_l$.
 
Let $f$ be in the unit ball of the $\Psi$-weighted Hilbert space on
$B_j$. Extend $\theta_{jl}f$ by zero to $B_l$ and solve
\begin{equation}\label{nk:eq:reg-dbar}
  \bar\partial g=\bar\partial(\theta_{jl}f)\qquad\text{on }B_l
\end{equation}
with respect to the weight
\[
  \Phi_{m,x}\coloneqq m\Psi+2d\log|z-x|+|z|^2 .
\]
The right-hand side of
\eqref{nk:eq:reg-dbar} is $\bar\partial$-closed, and it is supported where
$|z-x|\ge r$. Since $\Phi_{m,x}$ is psh with
$\ddc\Phi_{m,x}\ge\ddc|z|^2$, H\"ormander's $L^2$-estimate \cite[Chapter~VIII, \S6]{DemCADG}, gives a solution $g$ with
\begin{equation}\label{nk:eq:reg-hormander}
  \int_{B_l}|g|^2\mathrm{e}^{-\Phi_{m,x}}\,\mathrm{d}\lambda
  \le C_H\int_{B_l}|\bar\partial\theta_{jl}|^2|f|^2\mathrm{e}^{-\Phi_{m,x}}\,\mathrm{d}\lambda,
\end{equation}
where $\mathrm{d}\lambda$ is the Lebesgue measure and $C_H$ depends only on
$d$. Here and below, the uniform comparison between $\mathrm{d}\lambda$
and the relevant coordinate measures is absorbed into the constants. On the support of
$\bar\partial\theta_{jl}$ the factor $|z-x|^{-2d}$ is bounded by
$r^{-2d}$, so the right-hand side of \eqref{nk:eq:reg-hormander} is at most
a constant $C_1$ independent of $m$, $\Psi$ and $x$. Since
$|z-x|\le R$ on $B_l$, the left-hand side dominates the ordinary
weighted norm, and we get
\[
  \int_{B_l}|g|^2\mathrm{e}^{-m\Psi}\,\mathrm{d}\lambda_l\le C_2 .
\]
Near $x$ the function $g$ is holomorphic, and $\Psi$ is bounded
above there; the integrability of $|g|^2|z-x|^{-2d}$ near $x$ therefore
forces $g(x)=0$. Hence
$F\coloneqq \theta_{jl}f-g$ is holomorphic on $B_l$, satisfies $F(x)=f(x)$, and
has $\Psi$-weighted norm at most a uniform constant. The extremal
characterization of the Bergman kernel, applied to $F$, and the same
argument with $j$ and $l$ interchanged, yield
\begin{equation}\label{nk:eq:reg-overlap}
  \varphi_{j,m}\le\varphi_{l,m}+\frac{C_B}{m},\qquad
  \varphi_{l,m}\le\varphi_{j,m}+\frac{C_B}{m}
  \qquad\text{on }\overline V_j\cap\overline V_l,
\end{equation}
where $C_B\ge0$, the maximum of the corresponding constants over the
finitely many pairs $(j,l)$, depends only on the fixed cover
and the background geometry.
 
\emph{Step 3: global gluing.}
Choose $\chi_j\in C^\infty_c(V_j)$ with $0\le\chi_j\le1$ and
$\chi_j=1$ on $U_j$, and let $C_\chi$ be such that
$\ddc\chi_j\ge-C_\chi\omega_Z$ for all $j$. Put
$\delta\coloneqq 1/(4m)$, and set
\begin{equation}\label{nk:eq:reg-glue}
  \varphi_m(z)\coloneqq M_\delta\Bigl(\varphi_{j,m}(z)+\frac{C_B+1}m\chi_j(z)
   \ :\ z\in V_j\Bigr),
\end{equation}
the regularized maximum of the branches defined at $z$. We check that
this is a well-defined quasi-psh function on $Z$. Let
$q\in\partial V_j$ and choose $l$ with $q\in U_l$. On a small
neighborhood of $q$ we have $\chi_j=0$ and $\chi_l=1$, so that on
its intersection with $V_j\cap V_l$, \eqref{nk:eq:reg-overlap} gives
\[
  \varphi_{j,m}+\frac{C_B+1}m\chi_j+\delta
  \le\varphi_{l,m}+\frac{C_B}{m}+\delta
  <\varphi_{l,m}+\frac{C_B+1}m\chi_l-\delta
\]
off the zero locus $Z_0$ of $\mathcal I(m\varphi)$, where all branches
are finite by Step~4 below. By the independence property of
$M_\delta$, the $j$-th branch therefore does
not contribute to \eqref{nk:eq:reg-glue} near $\partial V_j\setminus Z_0$;
on $Z_0$ every branch equals $-\infty$, so \eqref{nk:eq:reg-glue}
equals $-\infty$ there whichever branches are used. In either case the local
definitions agree when branches are added or removed, and near every point
of $Z$ the function $\varphi_m$ is the regularized maximum of finitely
many branches defined on a neighborhood of that point. Each branch is
smooth where it is finite, and it satisfies
\[
  \zeta+\ddc\Bigl(\varphi_{j,m}+\frac{C_B+1}m\chi_j\Bigr)
  \ge-\frac{(C_B+1)C_\chi}{m}\omega_Z
\]
there, by \eqref{nk:eq:reg-local-positivity}. By Step~4 below, the branches
defined near a given point all equal $-\infty$ exactly on the zero
locus $Z_0$ of $\mathcal I(m\varphi)$, a proper analytic subset. Hence
$\varphi_m$ is smooth on $Z\setminus Z_0$, where it satisfies
$\zeta+\ddc\varphi_m\ge-((C_B+1)C_\chi/m)\omega_Z$ by the property of
$M_\delta$ recalled before the lemma; it is locally bounded above, and
it tends to $-\infty$ along $Z_0$, since
$M_\delta(t)\le\max_it_i+N\delta$. By the Grauert--Remmert extension
theorem for psh functions bounded above near an analytic subset
\cite{GR56} (see \cite[Theorem~1.2.1]{SGPT}), $\varphi_m$ is
quasi-psh on $Z$ and
the inequality $\zeta+\ddc\varphi_m\ge-((C_B+1)C_\chi/m)\omega_Z$ holds on
all of $Z$. Here no local potential for $\omega_Z$ is needed. On a smaller coordinate ball, add a sufficiently large quadratic function to obtain a psh function off $Z_0$, and extend it across $Z_0$. The extended current has the stated smooth lower bound off $Z_0$; any part it charges on $Z_0$ is positive, so the lower bound holds globally. This proves \ref{nk:it:reg-positivity} with
$c\coloneqq (C_B+1)C_\chi$,
which depends only on the fixed cover, the cut-off functions and
$\omega_Z$, and not on $\zeta$, $\varphi$ or $m$.
 
\emph{Step 4: the singularity ideal and the lower bound.}
Let $\mathfrak J_{j,m}$ be the ideal sheaf on $V_j$ generated by the
elements of $\mathcal H_{j,m}$. By definition of $\mathcal H_{j,m}$,
$\mathfrak J_{j,m}\subset\mathcal I(m\psi_j)=\mathcal I(m\varphi)$ on $V_j$,
the equality holding because $h_j$ is smooth. Conversely, since
$\psi_j$ is psh on $B_j^+$, and $B_j\Subset B_j^+$ is a relatively
compact Stein open subset with a basis of Stein neighborhoods,
\cite[Proposition~1.2]{DEL00}, applied with the weight
$\tfrac m2\psi_j$ and the Euclidean K\"ahler volume form $\mathrm{d}\lambda_j$ (the
multiplier ideal is defined there with the factor
$\mathrm{e}^{-2\varphi}$), shows that $\mathcal I(m\varphi)$ is generated on
$B_j$ by the orthonormal basis $(\sigma_{j,m,\ell})_\ell$ of
$\mathcal H_{j,m}$. Hence
\begin{equation}\label{nk:eq:reg-ideal-equality}
  \mathfrak J_{j,m}=\mathcal I(m\varphi)\qquad\text{on }V_j ,
\end{equation}
and in particular the zero set of $K_{j,m}$ is the zero locus of
$\mathcal I(m\varphi)$ in $V_j$, as used in Step~3.
 
We can now prove \ref{nk:it:reg-lower}. Fix $x\in Z$ and choose $j$ with
$x\in U_j$. By coherence and \eqref{nk:eq:reg-ideal-equality}, finitely
many of the $\sigma_{j,m,\ell}$, say with $\ell\le N$, generate
$\mathcal I(m\varphi)$ on a neighborhood of $x$. Therefore
$K_{j,m}\ge\sum_{\ell\le N}|\sigma_{j,m,\ell}|^2$ gives
$\varphi_{j,m}\ge m^{-1}\psi_{\mathcal I(m\varphi)}+O(1)$
on a neighborhood of $x$, the bounded term absorbing $h_j$. Since
$\chi_j\ge0$ and the regularized maximum dominates each of its
entries, $\varphi_m\ge\varphi_{j,m}$ on $V_j$, and
\ref{nk:it:reg-lower} follows.
\end{proof}

The gluing of Step~3 also produces global quasi-psh functions with a
prescribed singularity ideal.

\begin{lemma}\label{nk:lem:ideal-function}
Let $(Z,\omega_Z)$ be a connected compact Hermitian manifold and let
$\mathfrak a\subset\mathcal O_Z$ be a nonzero coherent ideal. There is a
quasi-psh function
$\Psi_{\mathfrak a}$ on $Z$ with analytic singularities of type
$(1,\mathfrak a)$ which is smooth on the complement of the zero locus of
$\mathfrak a$.
\end{lemma}

\begin{proof}
Fix a finite cover of $Z$ by coordinate balls $B_j$ on which
$\mathfrak a$ is generated by $g_{j1},\dots,g_{jN_j}$, together with
concentric balls $U_j\Subset V_j\Subset B_j$ such that the $U_j$ cover
$Z$, and put $\psi_j\coloneqq \log\sum_i|g_{ji}|^2$, a psh function on $B_j$
which is smooth outside the zero locus of $\mathfrak a$, where it equals
$-\infty$. Since the $g_{ji}$ and the $g_{li}$ generate the same
ideal, $|\psi_j-\psi_l|\le C_B$ on $\overline V_j\cap\overline V_l$ for
some constant $C_B$. Now define $\Psi_{\mathfrak a}$ by
\eqref{nk:eq:reg-glue}, with $m=1$, the branches $\psi_j$ in place of
$\varphi_{j,m}$, and the cut-off functions $\chi_j$ and the constant
$\delta=1/4$ as in Step~3 of the proof of
\cref{nk:lem:regularization}. The argument given there shows that
$\Psi_{\mathfrak a}$ is a well-defined quasi-psh function on $Z$, smooth
outside the zero locus of $\mathfrak a$, with
$\ddc\Psi_{\mathfrak a}\ge-(C_B+1)C_\chi\omega_Z$; and the bounds
$\max_it_i\le M_\delta(t)\le\max_it_i+N\delta$, together with
$0\le\chi_j\le1$ and $\psi_j=\psi_{\mathfrak a}+O(1)$, give
$\Psi_{\mathfrak a}=\psi_{\mathfrak a}+O(1)$ locally.
\end{proof}
