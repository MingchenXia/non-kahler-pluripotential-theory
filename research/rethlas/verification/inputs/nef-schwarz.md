Run_id: nef_schwarz_01

Run scope: Bounded verification through the normal Rethlas workflow. The parent owns all manuscript changes and release work. Restrict writes to normal verifier tools, memory and results; do not alter book/editorial/blueprint/status/changelog files, frozen inputs, original references or historical reports. Do not commit or push.

Statement: Verify a shorter proof of the known nef-difference bigness criterion with coefficient k, and the corresponding replacement of 8k by 2k in the existing uniform divisorial-domination proof. The book previously reconstructed only Xiao's weaker coefficient 4k by a level-set estimate. Cauchy--Schwarz now gives Popovici's coefficient k directly. The new text attributes the theorem to Popovici and cites Lemma3.2 for the estimate; it makes no novelty claim or unrestricted Hermitian extension.

Primary source already consulted by the parent: Dan Popovici, Sufficient Bigness Criterion for Differences of Two Nef Classes, arXiv:1405.2518v2, https://arxiv.org/pdf/1405.2518, Theorem1.1 and Lemma3.2. The latter gives integral(a_tilde Gamma)*integral(a_tilde^(k-1) b)>=c/k for a_tilde^k=c b Gamma and integral b Gamma=1. The draft below derives the same bound through the scalar function H, with all steps included. The source is evidence; verify the proof itself. The ambient manifold Z and all resolutions in this application remain compact Kahler, and all classes in the criterion are closed Bott--Chern classes.

Accepted internal/classical inputs:
1. Nef closed classes on a compact Kahler manifold become Kahler after any positive multiple of a fixed Kahler class. Their top and mixed intersection numbers are continuous in the classes, computed with any smooth closed representatives; intersections of a pseudoeffective class with nef classes are nonnegative.
2. Every smooth positive background admits a smooth Monge--Ampere solution for any smooth positive right-hand side, up to a positive constant (thm:tw-smooth). For a closed background, Stokes identifies that constant with its top intersection when the density is a probability. Mixed closed integrals are unchanged by adding ddc of a smooth function.
3. Lamari duality: a smooth closed class is pseudoeffective iff it has nonnegative pairing with every smooth strictly positive ddc-closed (k-1,k-1) form. A positive current plus a positive multiple of a Kahler form proves bigness. On a compact connected complex curve, a class of positive integral has a smooth positive representative, by the Poisson equation.
4. The existing uniform domination proof's other inputs are accepted in their stated Kahler regimes: decreasing dyadic analytic approximation, monotonicity and multilinearity of non-pluripolar mixed masses, nefness and top intersection of bounded residual currents on a log resolution, the fixed-base nef mixed-intersection bound, descent of pullback psh potentials, normalized L1 compactness, L1-continuity of pullback on a fixed modification, semicontinuity of divisorial Lelong numbers and their characterization of the ideal preorder. The complete proof is included below to check the new numerical threshold and the order of choosing constants. Do not infer any ambient BMP statement outside this Kahler application.

Main checks: eta>0 is chosen before epsilon, and epsilon before the arbitrary normalized Gauduchon test Gamma. Both c_epsilon and N_epsilon are positive and independent of Gamma by closedness. The function H is everywhere smooth and strictly positive with integral H dmu=N_epsilon. From sum_i lambda_i^(-1)=kH/c_epsilon, each lambda_i>=c_epsilon/(kH), giving a pointwise inequality of forms. Cauchy--Schwarz on the probability mu gives integral H^(-1)dmu>=1/N_epsilon. Verify the exact k factor and that the final comparison holds for every Gauduchon test. The class a_epsilon-b_epsilon=A-B' is fixed; no epsilon limit or unproved uniform bound on potentials is needed to apply Lamari. The curve case is separate.

For the application, delta_*>0 is chosen with 2k delta_* C_*<h0, independently of eta in [0,1] and the potential v. For large j with epsilon_j<delta_*, A_j^k-k(epsilon_j+delta_*)A_j^(k-1).rho_j^*omega>=h0-2k delta_* C_*>0. Applying the now reconstructed k criterion makes the indicated difference class big. All remaining conclusions and the subsequent use delta0=delta_*/4 are unchanged. Audit zero mixed-intersection concerns and k=1; the bound C_*>0 follows since its defining interval includes a positive class.

Candidate theorem and shorter proof:

\begin{theorem}\label{nk:thm:nef-difference}
Let $Z$ be a connected compact K\"ahler manifold of dimension $k\geq1$ and let
$A,B$ be nef real $(1,1)$-classes on $Z$. If
$A^k-kA^{k-1}\cdot B>0$, then $A-B$ is big.
\end{theorem}
\begin{proof}
We give the argument through Gauduchon duality and the smooth
Monge--Amp\`ere equation, using the Cauchy--Schwarz estimate of \cite[Lemma~3.2]{Pop16}.
If $k=1$, nefness gives $B\geq0$ as an intersection number, so
$\int_Z(A-B)>0$. The Poisson equation gives a positive smooth
representative of this class. We henceforth assume $k\geq2$.

Fix a K\"ahler form $\omega_Z$. By continuity of intersection numbers,
choose $\eta>0$ so small that, with $B'=B+\eta\{\omega_Z\}$,
\[
 A^k>kA^{k-1}\cdot B'.
\]
\Needspace{7\baselineskip}
For each sufficiently small $\varepsilon>0$, nefness gives K\"ahler
forms $a_\varepsilon\in A+\varepsilon\{\omega_Z\}$ and
$b_\varepsilon\in B'+\varepsilon\{\omega_Z\}$. Set
\[
 c_\varepsilon=(A+\varepsilon\{\omega_Z\})^k,
 \qquad
 N_\varepsilon=(A+\varepsilon\{\omega_Z\})^{k-1}
                    \cdot(B'+\varepsilon\{\omega_Z\}).
\]
Choose and fix $\varepsilon$ so small that
$c_\varepsilon>kN_\varepsilon>0$.
We will show that $A-B'$ is pseudoeffective.

Let $\Gamma$ be any smooth strictly positive $(k-1,k-1)$-form with
$\ddc\Gamma=0$. Rescale it so that
$\int_Z b_\varepsilon\wedge\Gamma=1$, and put
$\mu=b_\varepsilon\wedge\Gamma$. This is a smooth positive probability
measure. By \cref{thm:tw-smooth}, there is a smooth function $v$ such that
\[
 \widetilde a=a_\varepsilon+\ddc v>0,
 \qquad \widetilde a^k=c_\varepsilon\mu.
\]
Indeed, the initially unknown normalization constant is
$c_\varepsilon$ by Stokes' theorem. Closedness also gives
\[
 \int_Z\widetilde a^{k-1}\wedge b_\varepsilon=N_\varepsilon.
\]
Put
\[
 H=\frac{\widetilde a^{k-1}\wedge b_\varepsilon}{\mu}>0,
 \qquad \int_ZH\,\mu=N_\varepsilon.
\]
At each point, let $\lambda_1,\ldots,\lambda_k$ be the eigenvalues
of $\widetilde a$ relative to $b_\varepsilon$. The wedge-power identity gives
\[
 \frac1k\sum_{i=1}^k\lambda_i^{-1}
 =\frac{\widetilde a^{k-1}\wedge b_\varepsilon}{\widetilde a^k}
 =\frac{H}{c_\varepsilon}.
\]
Every summand is positive, so
$\widetilde a\geq c_\varepsilon b_\varepsilon/(kH)$ everywhere.
Cauchy--Schwarz and $\mu(Z)=1$ give
\[
 1\leq\left(\int_ZH\,\mu\right)
         \left(\int_ZH^{-1}\,\mu\right)
   =N_\varepsilon\int_ZH^{-1}\,\mu.
\]
Integrating the pointwise form inequality against $\Gamma$ therefore yields
\[
 \int_Za_\varepsilon\wedge\Gamma
 =\int_Z\widetilde a\wedge\Gamma
 \geq\frac{c_\varepsilon}{k}\int_ZH^{-1}\,\mu
 \geq\frac{c_\varepsilon}{kN_\varepsilon}>1
 =\int_Zb_\varepsilon\wedge\Gamma.
\]
The form $a_\varepsilon-b_\varepsilon$ represents the fixed class
$A-B'$: the two $\varepsilon\{\omega_Z\}$ terms cancel. The displayed
inequality holds for every Gauduchon test form, so \cref{thm:lamari}
provides a closed positive current $S\in A-B'$. Then
$S+\eta\omega_Z\in A-B$ dominates $\eta\omega_Z$, proving bigness.
\end{proof}

The Gauduchon form serves two purposes in this proof: it tests
pseudoeffectivity, and it defines the right-hand side of the
Monge--Amp\`ere equation. Closedness makes $c_\varepsilon$ and
$N_\varepsilon$ independent of that test. This is the precise point
at which this argument needs more than a Gauduchon reference metric.


Existing uniform domination argument with the synchronized numerical choices:

\begin{lemma}\label{nk:lem:domination}
Let $(Z,\omega_Z)$ be a connected compact K\"ahler manifold of
dimension $k$, let
$\gamma$ be a smooth closed real $(1,1)$-form on $Z$ whose class is
big, and let $h_0>0$. There exists $\delta_*>0$, depending only on
$(Z,\omega_Z)$, $\gamma$ and $h_0$, with the following property. If
$0\le\eta\le1$ and
\begin{equation}\label{nk:eq:dom-hyp}
  v\in\PSH(Z,\gamma+\eta\omega_Z),\qquad
  \int_Z(\gamma+\eta\omega_Z)_v^k\ge h_0,
\end{equation}
then there is a closed positive current
$S_v\in\{\gamma\}+\eta\{\omega_Z\}$ such that
\begin{equation}\label{nk:eq:dom-concl}
  S_v\ge\delta_*\omega_Z
  \qquad\text{and}\qquad S_v\preceq_{\mathcal I} v.
\end{equation}
\end{lemma}

\begin{proof}
\emph{Step 1: analytic approximation.}
Fix $\eta$ and $v$ as in \eqref{nk:eq:dom-hyp}, and put
$\gamma_\eta\coloneqq \gamma+\eta\omega_Z$. By \cite[Theorem~1.6.2]{SGPT}
there is a quasi-equisingular approximation $(v_j)_{j\ge1}$ of $v$
with $v_j$ of analytic type $(2^{-j},\mathcal I(2^jv))$,
\[
  v_j\in\PSH(Z,\gamma_j),\qquad
  \gamma_j\coloneqq \gamma+(\eta+\epsilon_j)\omega_Z,\qquad
  \epsilon_j\downarrow0,\qquad v_j\searrow v.
\]
The divisorial approximation estimate \cref{lem:bergman-divisorial-error},
applied near a generic point of each fixed divisor, gives
\begin{equation}\label{nk:eq:dom-lelong-conv}
  \lim_{j\to\infty}\nu(v_j,E)=\nu(v,E)
  \qquad\text{for every prime divisor $E$ over $Z$}.
\end{equation}
Since $v\le v_j$, the monotonicity theorem
(\cref{nk:sec:npp}\ref{nk:it:monotone}) and the multilinearity of non-pluripolar
products give
\begin{equation}\label{nk:eq:dom-mass}
  \int_Z(\gamma_j)_{v_j}^k
  \ge\int_Z(\gamma_j)_{v}^k
  =\int_Z\bigl((\gamma_\eta)_v+\epsilon_j\omega_Z\bigr)^k
  \ge\int_Z(\gamma_\eta)_v^k\ge h_0.
\end{equation}

\emph{Step 2: the numerical estimate.}
Let $\rho_j\colon Z_j\to Z$ be a log resolution of $v_j$, and write
the Siu decomposition of the pullback as
\[
  \rho_j^*\bigl((\gamma_j)_{v_j}\bigr)=R_j+[F_j],
\]
where $F_j$ is an effective $\mathbf Q$-divisor and $R_j$ is a closed
positive current with locally bounded potentials. Put $A_j\coloneqq \{R_j\}$.
The class $A_j$ is nef by \cref{nk:lem:residual-nef}. Since the
non-pluripolar product puts no mass on $F_j$, Bedford--Taylor theory and
\cref{nk:sec:npp}\ref{nk:it:invariance} give, together with
\eqref{nk:eq:dom-mass},
\begin{equation}\label{nk:eq:dom-Ak}
  A_j^k=\int_{Z_j}R_j^k
  =\int_{Z_j}\bigl(\rho_j^*(\gamma_j)_{v_j}\bigr)^k
  =\int_Z(\gamma_j)_{v_j}^k\ge h_0.
\end{equation}
Choose $C^\dagger>0$ so large that $\gamma+C^\dagger\omega_Z$ is
K\"ahler, and set
$K_j\coloneqq \rho_j^*\{\gamma+(\eta+\epsilon_j+C^\dagger)\omega_Z\}$. Then
$K_j$ is nef, being the pullback of a K\"ahler class, and
\[
  K_j-A_j=\{F_j\}+C^\dagger\rho_j^*\{\omega_Z\}
\]
is pseudoeffective. Since the intersection number of a pseudoeffective
class with nef classes is nonnegative, expanding
$K_j^{k-1}-A_j^{k-1}=\sum_{i=0}^{k-2}K_j^i\cdot(K_j-A_j)\cdot A_j^{k-2-i}$
and using the projection formula yields the uniform bound
\begin{equation}\label{nk:eq:dom-intersection}
  A_j^{k-1}\cdot\rho_j^*\{\omega_Z\}
  \le K_j^{k-1}\cdot\rho_j^*\{\omega_Z\}
  =\bigl(\{\gamma\}+(\eta+\epsilon_j+C^\dagger)\{\omega_Z\}\bigr)^{k-1}
   \cdot\{\omega_Z\}
  \le C_*,
\end{equation}
where
$C_*\coloneqq \max_{0\le s\le 2+C^\dagger}\bigl(\{\gamma\}+s\{\omega_Z\}\bigr)^{k-1}\cdot\{\omega_Z\}$
depends only on $(Z,\omega_Z)$ and $\gamma$; here we used
$\eta\le1$ and $\epsilon_j\le1$ for $j$ large. Now choose
$\delta_*>0$ such that
\begin{equation}\label{nk:eq:dom-delta}
  2k\delta_*C_*<h_0;
\end{equation}
this choice depends only on $(Z,\omega_Z)$, $\gamma$ and $h_0$. For
$j$ so large that $\epsilon_j<\delta_*$, the estimates
\eqref{nk:eq:dom-Ak}, \eqref{nk:eq:dom-intersection} and \eqref{nk:eq:dom-delta}
give
\[
  A_j^k-k(\epsilon_j+\delta_*)A_j^{k-1}\cdot\rho_j^*\{\omega_Z\}
  \ge h_0-2k\delta_*C_*>0.
\]
By \cref{nk:thm:nef-difference}, applied on the compact K\"ahler manifold
$Z_j$ to the nef classes $A_j$ and
$(\epsilon_j+\delta_*)\rho_j^*\{\omega_Z\}$, the class
$A_j-(\epsilon_j+\delta_*)\rho_j^*\{\omega_Z\}$
is big. Choose a K\"ahler current $L_j$ in this class and set
\[
  \widetilde S_j\coloneqq L_j+\delta_*\rho_j^*\omega_Z+[F_j]
  \ge\delta_*\rho_j^*\omega_Z .
\]
Its cohomology class is
\[
  \{\widetilde S_j\}
  =A_j-(\epsilon_j+\delta_*)\rho_j^*\{\omega_Z\}
     +\delta_*\rho_j^*\{\omega_Z\}+\{F_j\}
  =\rho_j^*\{\gamma_j\}-\epsilon_j\rho_j^*\{\omega_Z\}
  =\rho_j^*\{\gamma_\eta\},
\]
where we used $\rho_j^*\{\gamma_j\}=A_j+\{F_j\}$.

\emph{Step 3: descent and passage to the limit.}
Since $\{\widetilde S_j\}=\rho_j^*\{\gamma_\eta\}$ and $Z_j$ is a
compact K\"ahler manifold, the $\ddc$-lemma gives
$\widetilde S_j=\rho_j^*\gamma_\eta+\ddc\widetilde s_j$ for a quasi-psh
function $\widetilde s_j$ on $Z_j$, and the lower bound
$\widetilde S_j\ge\delta_*\rho_j^*\omega_Z$ means that
$\widetilde s_j\in
\PSH\bigl(Z_j,\rho_j^*(\gamma_\eta-\delta_*\omega_Z)\bigr)$. By
\cite[Proposition~1.5.3]{SGPT}, the pullback of potentials is a
bijection from $\PSH(Z,\gamma_\eta-\delta_*\omega_Z)$ onto
$\PSH\bigl(Z_j,\rho_j^*(\gamma_\eta-\delta_*\omega_Z)\bigr)$; hence
$\widetilde s_j=s_j\circ\rho_j$ for some
$s_j\in\PSH(Z,\gamma_\eta-\delta_*\omega_Z)$. The current
$S_j\coloneqq \gamma_\eta+\ddc s_j\in\{\gamma\}+\eta\{\omega_Z\}$ then
satisfies
$S_j\ge\delta_*\omega_Z$ and $\rho_j^*S_j=\widetilde S_j$.

Since $R_j$ has locally bounded potentials and
$\widetilde S_j\ge[F_j]$, \cite[Proposition~6.1.2]{SGPT} gives
$\rho_j^*S_j=\widetilde S_j
\preceq_{\mathcal I} R_j+[F_j]=\rho_j^*\bigl((\gamma_j)_{v_j}\bigr)$, and the
bimeromorphic invariance of the $\mathcal I$-preorder
\cite[Lemma~6.1.4]{SGPT} yields $S_j\preceq_{\mathcal I} v_j$.

Normalize $\sup_Zs_j=0$. By weak compactness, a subsequence of
$(s_j)_j$ converges in $L^1(Z)$ to a quasi-psh function $s_v$, and
we set $S_v\coloneqq \gamma_\eta+\ddc s_v$. The lower bound
$S_j\ge\delta_*\omega_Z$ passes to the limit, so
$S_v\ge\delta_*\omega_Z$. For every prime divisor $E$ over $Z$,
pulling back to a model realizing $E$, upper semicontinuity of
Lelong numbers and \eqref{nk:eq:dom-lelong-conv} give
\[
  \nu(S_v,E)\ge\varlimsup_{j\to\infty}\nu(S_j,E)
  \ge\lim_{j\to\infty}\nu(v_j,E)=\nu(v,E).
\]
Another application of \cite[Proposition~6.1.2]{SGPT} gives
$S_v\preceq_{\mathcal I} v$, proving \eqref{nk:eq:dom-concl}. The constant $\delta_*$ was chosen in
\eqref{nk:eq:dom-delta} independently of $\eta\in[0,1]$ and of $v$.
\end{proof}
