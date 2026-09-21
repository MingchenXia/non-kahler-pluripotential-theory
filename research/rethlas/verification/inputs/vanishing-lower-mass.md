Run_id: vanishing_lower_mass_01

Statement: Verify every assertion in the supplied complete book section, including the construction, all limit passages, the threefold theorem, both dimension/product corollaries and the closing density/endpoint consequences. The section reconstructs the user's eight-page manuscript A counterexample to positive lower Hermitian Monge–Ampère mass. It proves existence of a smooth compact complex threefold on which EVERY Hermitian metric has zero lower Monge–Ampère mass; all dimensions >=3 follow, and products with a Hopf threefold give simultaneous failure of both mass properties in every dimension >=6. Do not assume the supplied paper's conclusion, and do not treat a favorable earlier discussion as proof. The whole reconstructed argument must pass.

Conventions: The book uses ddc=i/(2pi) partial bar-partial and dc=i/(4pi)(bar-partial minus partial), so ddc log|z|^2 is the unit divisor current. The supplied PDF uses twice this normalization. The proof is reconstructed directly in the book convention, including sigma_v=i/(2pi) dv wedge dbar-v and integral-one Fubini–Study forms. Smooth strictly positive (2,2)-forms on a threefold correspond to positive Hermitian cofactor matrices. The specific matrix definition and wedge factorials must be checked, not inferred from similar terminology. v_-(h) and v_+(h) are respectively the infimum and supremum over bounded h-psh potentials of the total bounded Monge–Ampère mass. All manifolds are smooth compact connected, and h can be nonclosed.

Canonical prior inputs (read the stated sources and check the exact hypotheses):
- book/author/chapter_gauduchon.tex, thm:gauduchon, prop:gauduchon-trace, thm:lamari: scalar Gauduchon existence and uniqueness; current Stokes; generalized Lamari criterion for arbitrary nonclosed smooth real (1,1)-backgrounds. The equivalence between smooth positive ddc-closed (n-1,n-1)-forms and Gauduchon powers is proved there. Do not import a closed-background-only Lamari statement.
- book/author/chapter_compactness.tex, thm:normalized-compactness: supremum-normalized qpsh L1 compactness in one fixed smooth lower curvature background, without BMP.
- book/author/chapter_smooth_equations.tex, thm:tw-smooth: the smooth Hermitian Calabi–Yau equation for any smooth positive right-hand side, with its scalar and normalized potential. Its reconstruction is already in the book; it needs neither BMP nor PVP.
- book/author/section_gauduchon_volume_extrema.tex, thm:gaud-volume-mass-extrema and eq:gaud-lower-mass-formula: exact smooth-density extrema and lower-mass formula, including bounded-to-smooth regularization. Check that comparing the same Gauduchon quotients gives monotonicity under pointwise background order, and hence metric independence of lower-mass vanishing.
- book/author/chapter_mass.tex: mass invariance for a Gauduchon surface; book/author/chapter_products.tex, prop:bmp-metric: metric independence of bounded upper mass and existence of smooth witnesses for unbounded mass; book/author/chapter_hopf.tex, thm:hopf-unbounded: concrete compact Hopf threefold with smooth unbounded-mass witnesses.
- book/author/chapter_gauduchon_variational_volume.tex, thm:gaud-volume-dual-formula and prop:gaud-volume-density-comparison: positivity of each fixed smooth-density normalization and the displayed comparison of denominators. The final use of only a one-sided bound mu_j<=M mu must be checked from the formula, not by presuming a uniform reverse bound.
- book/author/section_gauduchon_determinant_integrability.tex, thm:gaud-determinant-subcritical and thm:gaud-determinant-endpoint: the precise determinant-density norm statements for ALL normalized Gauduchon currents. Do not identify the whole class with the smaller set of maximizing currents for a fixed equation.

Classical inputs: positive closed integration currents of complex submanifolds; Poincare–Lelong and monotonicity of Lelong numbers under positive current domination; Siu analyticity of positive Lelong superlevel sets, applied locally after smooth correction to qpsh functions; holomorphic identity principle; proper free discrete group quotients and local charts; smooth fiber integration for a submersion with proper support; positivity and closedness under averaging; smooth matrix Schur complements and determinant monotonicity. The Siu74 citation must be verified as a primary reference in the normal reference workflow. The supplied paper is provenance, not a theorem input, and its full proof is reconstructed here. Do not assume its geometric concentration conclusion.

Source comparison: research/sources/LowerMass26.pdf and LowerMass26.txt contain the original supplied paper, downloaded from https://mingchenxia.github.io/Papers/volinf0_vibe.pdf on 21 September 2026. No author appears in the PDF. The new draft omits its optional dense enumeration of metrics: ordinary existential choices of delta_j and Theta_j suffice for the stated existence theorem. Check all other adaptations and normalization factors independently. Its citation key LowerMass26 denotes this supplied manuscript, not a claim of publication or authorship.

Critical review points: compactness and connectedness of the quotient; correct coordinates on the elliptic fiber; the local cutoffs and positivity; Siu set properness and deck-translate analytic accumulation; uniform degree under automorphism averaging; uniform lower bound for the translated trace on the shrinking product region; globally embedded rational curves and the evaluation-submersion argument at every projective point; smoothness only for epsilon>0; local C-infinity convergence as epsilon->0 for fixed j; positive horizontal K_f; root and cofactor constants; dependence of epsilon_j on j; finite-degree/unbounded-root-volume implication through the smooth equation; product coefficients and metric comparisons; exact separation between fixed and varying densities and between arbitrary and maximizing Gauduchon currents.

Follow the normal sequential/reference/synthesis workflow with ordinary approvals and no TLS bypass. Preserve all submitted sources and other verifier records. Write only this audit's memory, result and final output; do not edit production book files or run Git synchronization. The primary agent handles integration and repository history after reading the report.

Proof:

\section{Vanishing lower mass}
\label{sec:vanishing-lower-mass}

The infimum in \eqref{eq:gaud-lower-mass-formula} need not be positive. We reconstruct the example of the supplied manuscript \cite{LowerMass26}, using the normalization of this book throughout. The construction separates two operations: concentration of a Gauduchon trace and averaging of compact curves. Their combination makes the volume of the positive root large while its degree stays bounded.

\begin{theorem}\label{thm:vanishing-lower-mass}
There is a connected compact complex threefold $X$ such that, for every Hermitian form $h$ on $X$, there are smooth real functions $u_j$ satisfying
\[
 h+\ddc u_j>0,\qquad \sup_Xu_j=0,\qquad
 \int_X(h+\ddc u_j)^3\longrightarrow0.
\]
In particular, $v_-(h)=0$ for every Hermitian form on this manifold.
\end{theorem}

We first give the manifold and the concentration argument. The last step of the proof will use the smooth Monge--Amp\`ere equation.

\subsection{The elliptic quotient}

Write points of $\mathbf P^3$ as $[z:w]$, with $z,w\in\C^2$, and set
\[
 \Omega=\{[z:w]:z\ne0,\ w\ne0\},\qquad
 q=\mathrm{e}^{2\pi},\qquad g[z:w]=[z:qw].
\]
The action of $\langle g\rangle$ is free. Indeed, equality of two projective points in one orbit would require the same scalar to be $1$ on the nonzero $z$ block and $q^k$ on the nonzero $w$ block. Thus $g^k$ has a fixed point only for $k=0$. The function
\[
 t=\log\frac{\|w\|^2}{\|z\|^2}
\]
is well defined on $\Omega$ and satisfies $t\circ g=t+4\pi$. It follows that the action is properly discontinuous: two compact subsets have bounded $t$ ranges, so only finitely many translates can meet. Moreover, the strip $0\leq t\leq4\pi$ is compact. In homogeneous coordinates of total norm one its defining inequalities bound both blocks away from zero, making it a closed subset of $\mathbf P^3$ contained in $\Omega$. The strip meets every orbit. Consequently
\[
 X=\Omega/\langle g\rangle
\]
is a connected compact complex threefold.

The map $[z:w]\mapsto([z],[w])$ induces a holomorphic submersion
$X\to\mathbf P^1\times\mathbf P^1$. Its fibers are
$E=\C/(2\pi\mathbb Z+2\pi\mathrm{i}\mathbb Z)$, using a logarithm of the relative scalar. Let $\alpha,\beta$ be the pullbacks of the Fubini--Study forms on the two factors, each of integral one in our normalization. Although $t$ does not descend, its differentials do. The form
\begin{equation}\label{eq:lower-mass-quotient-metric}
 \omega=\alpha+\beta+\mathrm{d}t\wedge\dc t
\end{equation}
is Hermitian. Its first two terms are positive in the two base directions, and the last is semipositive and strictly positive on the vertical complex line. Their kernels have zero intersection.

On the open set $z_0w_0\ne0$, use coordinates
\[
 x=\frac{z_1}{z_0},\qquad y=\frac{w_1}{w_0},\qquad
 \zeta=\log\frac{w_0}{z_0}\in E.
\]
Near $0\in E$, the last coordinate is represented by an ordinary complex number. For any one of these coordinates put
$\sigma_v=\frac{\mathrm{i}}{2\pi}\mathrm{d}v\wedge\mathrm{d}\bar v$.
Choose a smooth probability density $p$ relative to $\sigma_v$, positive on $|v|<1$ and zero on $|v|\geq1$. Choose a smooth function $\chi_0$ supported in $|v|<1$, equal to one on $|v|\leq1/2$, and with values in $[0,1]$. Write $\chi(x,y)=\chi_0(x)\chi_0(y)$. For $0<\delta<1/100$ define, with extension by zero,
\[
 B_\delta=\chi(x,y)\delta^{-2}p(\zeta/\delta)\sigma_\zeta.
\]
All extensions are smooth because the chosen functions are smooth with compact support in their coordinate domains.

\begin{lemma}\label{lem:lower-mass-trace-concentration}
The finite numbers
\[
 C_\delta=\sup\left\{\int_XB_\delta\wedge\Theta:
 \Theta>0,\ \ddc\Theta=0,\ \int_X\omega\wedge\Theta=1\right\},
\]
where $\Theta$ is a smooth real $(2,2)$-form, tend to infinity as $\delta\downarrow0$.
\end{lemma}
\begin{proof}
For fixed $\delta$, the inequality $B_\delta\leq M_\delta\omega$ proves finiteness. Suppose instead that $C_{\delta_l}\leq C$ along a sequence tending to zero. Scaling the test forms and applying \cref{thm:lamari} to $C\omega-B_{\delta_l}$ gives normalized quasi-plurisubharmonic functions $v_l$ such that
\[
 C\omega+\ddc v_l\geq B_{\delta_l},\qquad \sup_Xv_l=0.
\]
By \cref{thm:normalized-compactness}, a subsequence converges in $L^1$ to a nontrivial $C\omega$-plurisubharmonic function $v$. The approximate identity in the $\zeta$ variable gives
\[
 B_{\delta_l}\rightharpoonup\chi[\zeta=0],\qquad
 C\omega+\ddc v\geq\chi[\zeta=0].
\]
On a coordinate ball where $\chi=1$, add a smooth strictly plurisubharmonic function whose Hessian dominates $C\omega$. The resulting positive closed current dominates $[\zeta=0]$. Hence $v$ has Lelong number at least one on an open subset of this hypersurface. Smooth correction does not change Lelong numbers. Siu's analyticity theorem \cite[Theorem~I]{Siu74} implies that
$Z=\{\nu(v,\cdot)\geq1\}$ is an analytic subset of $X$. It is proper because $v$ is not identically $-\infty$.

Its inverse image $\widetilde Z$ in $\Omega$ contains an open subset of
$H_0\cap\Omega$, where $H_0=\{w_0=z_0\}$. This surface is a projective plane with two points removed, so it is connected and irreducible. The identity principle gives $H_0\cap\Omega\subset\widetilde Z$. Deck invariance then gives
\[
 H_k\cap\Omega\subset\widetilde Z,\qquad H_k=\{w_0=q^kz_0\},
 \qquad k\in\mathbb Z.
\]
Use the chart $z_1=1$ near $[0:1:1:0]$. There $H_k$ is the graph $z_0=q^{-k}w_0$. For each fixed $(w_0,w_1)$ in a small neighborhood of $(1,0)$, every local defining holomorphic function of $\widetilde Z$ vanishes at these distinct values of $z_0$, which tend to zero. The one-variable identity theorem makes each defining function identically zero on the polydisk. Thus $\widetilde Z$ contains an open subset of the connected manifold $\Omega$, contradicting properness. This excludes every bounded subsequence of $C_\delta$ as $\delta\downarrow0$.
\end{proof}

Choose $\delta_j\downarrow0$ and smooth positive $\ddc$-closed forms $\Theta_j$ with
\begin{equation}\label{eq:lower-mass-large-trace}
 \int_X\omega\wedge\Theta_j=1,\qquad
 J_j=\int_XB_{\delta_j}\wedge\Theta_j>j^4.
\end{equation}
The lemma permits each $\delta_j$ to be smaller than half its predecessor, and the definition of the supremum supplies $\Theta_j$. No compactness of this family is assumed.

\subsection{Averaging the trace and compact curves}

Fix $j$ and write $\delta=\delta_j$. The automorphisms
\[
 T_{a,b,\tau}[z_0:z_1:w_0:w_1]
 =[z_0:z_1+az_0:\mathrm{e}^{\tau}w_0:
                  \mathrm{e}^{\tau}(w_1+bw_0)]
\]
commute with $g$ and act in the product chart by
$(x,y,\zeta)\mapsto(x+a,y+b,\zeta+\tau)$.
Average $T_{a,b,\tau}^*\Theta_j$ against the probability density
\[
 3^{-4}p(a/3)p(b/3)(3\delta)^{-2}p(\tau/(3\delta))
       \sigma_a\wedge\sigma_b\wedge\sigma_\tau
\]
and denote the result by $\widehat\Theta_j$. It is smooth, positive and $\ddc$-closed. The parameters range in a fixed compact set of automorphisms. Thus $(T_{a,b,\tau}^{-1})^*\omega\leq C\omega$ with one constant, and change of variables gives
\begin{equation}\label{eq:lower-mass-averaged-degree}
 \int_X\omega\wedge\widehat\Theta_j\leq C.
\end{equation}

Let $F_j$ be the coefficient of $\sigma_x\wedge\sigma_y$ in the restriction of $\Theta_j$ to a $\zeta$ slice, and let $\widehat F_j$ be the corresponding coefficient for $\widehat\Theta_j$. Positivity gives $F_j\geq0$. The translations express $\widehat F_j$ as an average of $F_j$. At a point of
\[
 V_j=\{|x|,|y|<1/4,\ |\zeta|<\delta/4\},
\]
every translation to $\operatorname{supp}B_\delta$ has
$|a|,|b|\leq5/4$ and $|\tau|\leq5\delta/4$. The first two averaging factors are bounded below by a positive constant on this range, and the third is bounded below by a positive constant times $\delta^{-2}$. Since $\chi\leq1$ and $p$ is bounded, comparison of these integrands in \eqref{eq:lower-mass-large-trace} gives
\begin{equation}\label{eq:lower-mass-spread-trace}
 \widehat F_j\geq cJ_j\quad\hbox{on }V_j,
\end{equation}
with $c>0$ independent of $j$.

The second average will occupy the other two cofactor directions. Put
\[
 f(a,b)=p(4(a-1))p(b/2),\qquad
 w_j(\tau)=4\delta^{-2}p(2\tau/\delta).
\]
For parameters in these supports and $|u|\leq1/16$, consider the maps
\begin{equation}\label{eq:lower-mass-rational-curves}
 \iota_{\tau,u,a,b}[z_0:z_1]
 =[z_0:z_1:\mathrm{e}^{\tau}(z_0+uz_1):
                \mathrm{e}^{\tau}(az_1+bz_0)]\in X.
\end{equation}
For $\varepsilon>0$, average their integration currents against
\[
 w_j(\tau)f(a,b)\varepsilon^{-2}p(u/\varepsilon)
       \sigma_\tau\wedge\sigma_a\wedge\sigma_b\wedge\sigma_u,
 \qquad 0<\varepsilon\leq1/16,
\]
and call the result $T_{j,\varepsilon}$. Define $T_{j,0}$ by setting $u=0$ and omitting the last probability integral.

\begin{lemma}\label{lem:lower-mass-curve-average}
For $\varepsilon>0$, the form $T_{j,\varepsilon}$ is globally smooth, semipositive and closed, and
\[
 \int_X\omega\wedge T_{j,\varepsilon}\leq C'
\]
with $C'$ independent of $j,\varepsilon$. For each fixed $j$, it converges smoothly to $T_{j,0}$ on compact subsets of the product chart as $\varepsilon\downarrow0$. There
\begin{equation}\label{eq:lower-mass-curve-local}
 T_{j,0}=w_j(\zeta)\sigma_\zeta\wedge K_f,\qquad
 K_f=\int_\C f(a,y-ax)\frac{\mathrm{i}}{2\pi}
       (\mathrm{d}y-a\,\mathrm{d}x)\wedge
       (\mathrm{d}\bar y-\bar a\,\mathrm{d}\bar x)\,\sigma_a.
\end{equation}
The form $K_f$ has a uniform positive lower bound on $|x|,|y|\leq1/4$.
\end{lemma}
\begin{proof}
On the parameter supports, $|a-bu|\geq3/4-2/16=5/8$. Hence the matrix
$\left(\begin{smallmatrix}1&u\\ b&a\end{smallmatrix}\right)$ is uniformly invertible. The projective line in \eqref{eq:lower-mass-rational-curves} lies in $\Omega$. Distinct deck translates of this line are disjoint: equality at a point fixes $[z_0:z_1]$, and invertibility of the matrix then forces the deck scalar to be one. Thus the map is an embedded compact rational curve in $X$.

The evaluation map from $\mathbf P^1$ times the open parameter domain to $X$ is a holomorphic submersion. At $z_1\ne0$, variations of $u$ and $a$ span the two $w$ coordinates after fixing a projective gauge; at $z_1=0$, variations of $\tau$ and $b$ span them. The $\mathbf P^1$ coordinate supplies the remaining direction. For $\varepsilon>0$, integration along the fibers of this submersion, with the smooth compactly supported parameter density, proves global smoothness. Averaging closed positive integration currents proves closedness and semipositivity.

All curve parameters belong to one compact subset of the invertible-matrix domain. Their $\omega$ areas consequently have a common bound by smooth dependence of the maps. The $\tau$ and $u$ weights have mass one, and the $a,b$ weight has fixed finite mass. This proves the degree bound.

When $u=0$, the local equations are $\zeta=\tau$ and $y=ax+b$. Integrating in $b$ and $\tau$ yields \eqref{eq:lower-mass-curve-local}; the displayed $(1,1)$-factor is the integration-current formula for the graph of $y=ax+b$. On $|x|,|y|\leq1/4$, the density $f(a,y-ax)$ is bounded below by a positive constant for $a$ in a fixed sufficiently small disk about $1$. The covectors $\mathrm{d}y-a\,\mathrm{d}x$, as $a$ ranges in that disk, have no common nonzero annihilator. Integrating their squared values and using compactness of the horizontal unit sphere gives the asserted lower bound.

For general $u$, the local equations are
\[
 \zeta=\tau+\log(1+ux),\qquad y=\frac{ax+b}{1+ux}.
\]
On any fixed compact subset, $1+ux$ stays nonzero for all sufficiently small $u$. Solving for $\tau$ and $b$ gives
$\tau=\zeta-\log(1+ux)$ and $b=(1+ux)y-ax$. Regard $w_j$ as a smooth function on $E$, so this change of variables also applies near the boundary of its support. The Jacobians, density coefficients and every fixed number of their derivatives depend smoothly on $u$. Averaging against the approximate identity in $u$ proves local $C^\infty$ convergence. This convergence is needed for fixed $j$ only; it is not asserted uniformly in $j$.
\end{proof}

\subsection{The volume of the positive root}

We make the cofactor convention explicit. In the coframe $(x,y,\zeta)$ put
$\mathrm{d}V_0=\sigma_x\wedge\sigma_y\wedge\sigma_\zeta$. A real $(2,2)$-form $\Theta$ corresponds to a Hermitian matrix $Q_\Theta$ by
\[
 \xi\wedge\Theta=\operatorname{tr}(H_\xi Q_\Theta)\,\mathrm{d}V_0,
\]
where $H_\xi$ is the coefficient matrix of a real $(1,1)$-form in the same normalization. Strict positivity is equivalent to $Q_\Theta>0$. If $\eta^2=\Theta$ and $H=H_\eta$, the wedge expansion gives
\[
 Q_\Theta=2(\det H)H^{-1},\qquad
 \eta^3=\frac{3}{\sqrt2}(\det Q_\Theta)^{1/2}\,\mathrm{d}V_0.
\]
Conversely, these formulas uniquely recover a smooth positive $H$ from $Q_\Theta>0$. This is the dimension-three root construction already used in \cref{thm:lamari}. Write $\Theta^{3/2}=\eta^3$.

\begin{lemma}\label{lem:lower-mass-unbounded-root}
There are smooth strictly positive $\ddc$-closed $(2,2)$-forms $\Gamma_j$ such that
\[
 \int_X\omega\wedge\Gamma_j\leq C_2,\qquad
 R_j=\int_X\Gamma_j^{3/2}\longrightarrow+\infty.
\]
\end{lemma}
\begin{proof}
Write the cofactor matrix of $\widehat\Theta_j$ in block form as
\[
 Q_j=\begin{pmatrix}A_j&p_j\\p_j^*&\widehat F_j\end{pmatrix}.
\]
The cofactor matrix of $T_{j,0}$ is $\operatorname{diag}(B_j,0)$. By the lower bound for $K_f$ and the definition of $w_j$, one has $B_j\geq c_0\delta_j^{-2}I_2$ on $V_j$. The Schur complement gives
\[
 \det\bigl(Q_j+\operatorname{diag}(B_j,0)\bigr)
 =\widehat F_j\det\left(B_j+A_j-
             \frac{p_jp_j^*}{\widehat F_j}\right)
 \geq\widehat F_j\det B_j.
\]
Here $A_j-p_jp_j^*/\widehat F_j$ is positive definite because $Q_j>0$; monotonicity of determinant on positive Hermitian matrices proves the inequality. Combining the root formula with \eqref{eq:lower-mass-spread-trace} shows that
\[
 (\widehat\Theta_j+T_{j,0})^{3/2}
       \geq c\delta_j^{-2}\sqrt{J_j}\,\mathrm{d}V_0
       \quad\hbox{on }V_j.
\]
The smaller region $W_j=\{|x|,|y|<1/8,\ |\zeta|<\delta_j/8\}$ has $\mathrm{d}V_0$ volume equal to a fixed positive constant times $\delta_j^2$. Consequently
\[
 I_j=\int_{W_j}(\widehat\Theta_j+T_{j,0})^{3/2}
       \geq c_1\sqrt{J_j}>c_1j^2.
\]
For this fixed $j$, the preceding lemma gives smooth convergence on the closure of $W_j$. The matrix of $\widehat\Theta_j+T_{j,0}$ is strictly positive there, so the positive-root volume depends continuously on these smooth coefficients. Choose $0<\varepsilon_j\leq1/16$ sufficiently small that
\[
 \int_{W_j}(\widehat\Theta_j+T_{j,\varepsilon_j})^{3/2}
       \geq I_j/2.
\]
Set $\Gamma_j=\widehat\Theta_j+T_{j,\varepsilon_j}$. It is smooth, strictly positive and $\ddc$-closed. Its degree is bounded by \eqref{eq:lower-mass-averaged-degree} and \cref{lem:lower-mass-curve-average}, whereas its root volume is at least $c_1j^2/2$. No uniform choice of $\varepsilon_j$ was used.
\end{proof}

\begin{proof}[of \cref{thm:vanishing-lower-mass}]
Fix any Hermitian form $h$ on $X$, and choose $A>0$ with $h\leq A\omega$. Let $\eta_j^2=\Gamma_j$. These metrics are Gauduchon, and
\[
 P_j=\int_Xh\wedge\eta_j^2\leq AC_2,\qquad
 R_j=\int_X\eta_j^3\longrightarrow+\infty.
\]
Solve the smooth equation from \cref{thm:tw-smooth} in background $h$ with right-hand side proportional to $\eta_j^3$:
\[
 h_j=h+\ddc u_j>0,\qquad h_j^3=\mathrm{e}^{b_j}\eta_j^3,
 \qquad \sup_Xu_j=0.
\]
The arithmetic--geometric mean inequality gives
$h_j\wedge\eta_j^2\geq\mathrm{e}^{b_j/3}\eta_j^3$.
Gauduchon Stokes therefore yields
\[
 P_j=\int_Xh_j\wedge\eta_j^2\geq\mathrm{e}^{b_j/3}R_j,
 \qquad
 0<\int_Xh_j^3=\mathrm{e}^{b_j}R_j
       \leq\frac{P_j^3}{R_j^2}\longrightarrow0.
\]
The functions are smooth and hence bounded on compact $X$, proving $v_-(h)=0$. Equivalently, the same bounds make the test quotients in \eqref{eq:gaud-lower-mass-formula} tend to zero.
\end{proof}

\subsection{Consequences for dimension and equations}

\begin{corollary}\label{cor:lower-mass-dimension}
Every Hermitian form on a compact complex manifold of dimension at most two has positive lower mass. In every dimension $n\geq3$ there is a connected compact complex manifold on which every Hermitian form has zero lower mass.
\end{corollary}
\begin{proof}
The formula \eqref{eq:gaud-lower-mass-formula} shows that $h_1\leq h_2$ implies $v_-(h_1)\leq v_-(h_2)$, and also gives degree-$n$ homogeneity. In dimension one the mass is $\int_Xh>0$. On a surface choose a Gauduchon metric $\gamma$ and $a>0$ with $h\geq a\gamma$. Mass invariance on the Gauduchon surface gives
$v_-(h)\geq a^2\int_X\gamma^2>0$.

For $n>3$, take the product of the preceding threefold with $\mathbf P^{n-3}$ and a split metric $h_0=\omega+\kappa$, with pullbacks understood. For the potentials supplied by the theorem,
\[
 \int_{X\times\mathbf P^{n-3}}(h_0+\ddc u_j)^n
 =\binom n3\left(\int_X(\omega+\ddc u_j)^3\right)
                   \left(\int_{\mathbf P^{n-3}}\kappa^{n-3}\right)
 \longrightarrow0.
\]
For another Hermitian $h$, choose $A$ with $h\leq Ah_0$. Monotonicity and homogeneity give $v_-(h)\leq A^n v_-(h_0)=0$.
\end{proof}

\begin{corollary}\label{cor:both-mass-properties-fail}
In every dimension $n\geq6$ there is a connected compact complex manifold with
\[
 v_-(h)=0,\qquad v_+(h)=+\infty
\]
for every Hermitian form $h$.
\end{corollary}
\begin{proof}
Take the product of the threefold above with the Hopf threefold of \cref{chap:hopf}. For a split metric, potentials pulled back from the first factor make the masses tend to zero, while smooth potentials pulled back from the second make them tend to infinity. In each case the product integral is $\binom63$ times the product of the two factor masses. The preceding metric comparison handles the lower mass, and metric independence in \cref{prop:bmp-metric} handles the upper mass. Products with projective spaces give every higher dimension by the same wedge expansion.
\end{proof}

Finally fix a smooth positive probability measure $\mu$ on the threefold. The smooth equation still gives $\mathcal V_\mu(h)>0$ for each Hermitian $h$. The mass-extrema theorem now says
\[
 \inf_{\nu\in\mathscr M}\mathcal V_\nu(h)=0,
 \qquad \lambda_*(h)=0.
\]
Thus even a smooth strictly positive background can have vanishing density infimum. This does not contradict positivity for a fixed density or the bigness question for $\lambda_\mu$. For the sequence in the proof, put $\mu_j=\eta_j^3/R_j$. Its equation constants satisfy
$\mathcal V_{\mu_j}(h)\leq P_j^3/R_j^2\to0$.
The densities $\mu_j/\mu$ cannot have a uniform upper bound: such a bound $\mu_j\leq M\mu$ would give $\mathcal V_{\mu_j}(h)\geq M^{-1}\mathcal V_\mu(h)>0$ by the denominator comparison in \cref{prop:gaud-volume-density-comparison}. The degeneration concerns the varying right-hand sides, not the existence of a solution for any one smooth positive right-hand side.

The example also makes the endpoint in \cref{thm:gaud-determinant-endpoint} fail for the full family of normalized Gauduchon currents: its supremum of $L^{3/2}$ determinant-density norms is infinite, although every subcritical $L^q$ norm, $1<q<3/2$, remains uniformly bounded by \cref{thm:gaud-determinant-subcritical}. An endpoint estimate restricted to the maximizing currents that represent adjoint measures remains a separate question.
