Run_id: semipositive_dual_attainment_01

Statement: Verify the proposed local regularity and exact threshold equation when a smooth semipositive maximizing Gauduchon form is strictly positive outside a proper analytic subset, and the classification of differences by divisorial Bott--Chern relations. Check uniqueness within multiplier-ideal equivalence classes (hence ordinary types), and under independence of the divisor classes, especially codimension at least two. No novelty claim. This draft is OUTSIDE the checked checkpoint47 book.

Source: /Users/mingchen/Non-Kahler/research/editorial/section_semipositive_dual_attainment.tex. Accepted internal inputs are the attained subsolution theorem in section_individual_density_subsolutions.tex; all-Hermitian trace inequality and saturation in section_threshold_trace_saturation.tex; the local regularity and matrix-equality arguments in section_smooth_dual_regularity.tex; the determinant density definition in section_weak_gauduchon_duality.tex and the all-Ln supremum formula in section_integrable_gauduchon_currents.tex. The latter supremum formula holds without root tails; root tails are needed for general compact attainment, not for the supremum formula. Here smooth semipositive attainment is an explicit hypothesis. The local multiplier-ideal criterion is thm:local-i-inputs in chapter_igood.tex, imported there from SGPT and stated precisely. Read these exact dependencies.

Classical external input: Demailly, Complex Analytic and Differential Geometry, version21June2012, ChapterIII Corollary2.11 (printedp141), Corollary2.14 (printedp143): a normal (p,p)-bidimensional current supported on an analytic set of dimension below p vanishes, and a closed order-zero current supported on a pure p-dimensional analytic set is a linear combination of its components. Exact official PDF https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf. Root read these statements, their normal/order-zero hypotheses and the short deduction on the regular locus. For a possibly nonpure Z, apply the support theorem to the divisorial regular locus and discard the remaining codimension>=2 support. Do not require positivity of the difference current.

Check sequentially: normalized positive regularization T_epsilon=(T+epsilon T0)/(1+epsilon); uniform continuity of the determinant-root density for smooth semipositive forms; fixed p integrability for the trace limit; exact equality by total mass1; applicability of all Hermitian tests locally off Z; local regularity before identifying nonlinear products; equality on Z because both extended MA and f dV vanish there; order-zero and closedness of ddc(u-v); divisor coefficient reality and the class relation in smooth Bott--Chern cohomology; recovery of each coefficient as a generic Lelong difference with this book's ddc=i/(2pi) partial barpartial normalization; I-equivalence and uniqueness. Existence of a form T with these properties is ASSUMED, not promised for every density. No general singular-current wedge, global smoothness, exponential convergence, BMP, positive lower mass or root-tail hypothesis is claimed. Preserve all previous results and memory.

Proof:

\subsection{A smooth maximizing form with an analytic degeneracy set}

Strict positivity of a smooth maximizing form can be weakened if its degeneracy is confined to a proper analytic subset. The proof is local away from that subset. The possible ambiguity of the potential is then divisorial.

\begin{theorem}\label{thm:semipositive-dual-exact-equation}
Let $\omega$ be Hermitian on a connected compact complex manifold of dimension $n\geq2$, let $0\leq f\in L^1(\mathrm{d}V)$ be nonzero, and assume $b=b_\omega(f)>0$. Suppose $D_{f^{1/n}}$ has a smooth semipositive maximizer $T\in\mathscr G_\omega$ which is strictly positive on $X\setminus Z$, where $Z$ is a proper analytic subset. Then every threshold subsolution is smooth on $X\setminus Z$ and satisfies
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(u)=bf\,\mathrm{d}V
\]
on $X$. Such a solution exists and has finite mass. The function $f^{1/n}$ has a smooth nonnegative representative on $X\setminus Z$.

If $u,v$ are threshold subsolutions and $Z_1,\ldots,Z_m$ are the prime divisorial components of $Z$, there are real numbers $c_j$ such that
\begin{equation}\label{eq:semipositive-dual-divisorial-difference}
 \ddc(u-v)=\sum_{j=1}^m c_j[Z_j],\qquad
 \sum_{j=1}^m c_j\{Z_j\}=0
       \quad\text{in }H^{1,1}_{\mathrm{BC}}(X,\mathbb R).
\end{equation}
Consequently threshold solutions are unique modulo constants within each multiplier-ideal equivalence class, hence within each ordinary singularity type. They are unique modulo constants without a prescribed type if the classes $\{Z_j\}$ are linearly independent. In particular this holds when $Z$ has codimension at least two.
\end{theorem}
\begin{proof}
Put $p=f^{1/n}$ and $A=\omega+\ddc u$, where $u$ is any threshold subsolution. Existence of at least one such $u$ is \cref{thm:individual-density-subsolution}. Fix a smooth strictly positive $T_0\in\mathscr G_\omega$ and set $T_\varepsilon=(T+\varepsilon T_0)/(1+\varepsilon)$. Each $T_\varepsilon$ belongs to $\mathscr G_\omega$ and has a smooth Hermitian root, so \cref{prop:threshold-trace-saturation} gives
\[
 A\wedge T_\varepsilon\geq b^{1/n}p k_{T_\varepsilon}\,\mathrm{d}V.
\]
For smooth semipositive forms, $k_T$ is the determinant root of the coefficient matrix, in the normalization of \cref{sec:weak-gauduchon-duality}. This is a continuous function of that matrix. Thus $k_{T_\varepsilon}\to k_T$ uniformly on compact $X$. Since $p\in L^1$, passage to the limit gives
\[
 A\wedge T\geq b^{1/n}p k_T\,\mathrm{d}V.
\]
The left side has mass one by Stokes and $\ddc T=0$. The right side has mass $b^{1/n}D_p(T)=1$, because $T$ maximizes. Their difference is positive and has zero mass, hence
\begin{equation}\label{eq:semipositive-dual-trace-equality}
 A\wedge T=b^{1/n}p k_T\,\mathrm{d}V.
\end{equation}

On $U=X\setminus Z$ write $T=\gamma^{n-1}$, where $\gamma$ is smooth and strictly positive, and set $a=(bf\,\mathrm{d}V/\gamma^n)^{1/n}$. The trace equality becomes $A\wedge\gamma^{n-1}=a\gamma^n$. On relatively compact subsets of $U$ this controls every coefficient measure of $A$ by an $L^n$ density. The all-Hermitian trace inequalities and matrix arithmetic--geometric mean, exactly as in the proof of \cref{cor:smooth-dual-exact-equation}, force $A=a\gamma$ there. This step uses only the local positivity of $\gamma$; the other Hermitian tests extend smoothly from smaller coordinate charts to $X$.

The local regularity lemma \cref{lem:smooth-conformal-current} makes $u,a$ smooth on $U$. Taking the smooth top power proves the equation there, and $f^{1/n}=b^{-1/n}a(\gamma^n/\mathrm{d}V)^{1/n}$ is smooth and nonnegative there. Both $\mathrm{MA}^{\mathrm{ext}}_\omega(u)$ and $f\,\mathrm{d}V$ vanish on the pluripolar set $Z$. Hence the equality holds on $X$, and its total mass is $b\int_Xf\,\mathrm{d}V<+\infty$.

For two threshold subsolutions the formula $\omega+\ddc u=a\gamma$ has the same right side on $U$. Thus $S=\ddc(u-v)$ is a real closed current supported on $Z$. It has order zero, being the difference of the positive currents $\omega+\ddc u$ and $\omega+\ddc v$. The classical support theorem gives $S=\sum_jc_j[Z_j]$; components of higher codimension carry no such current. This is \cite[Chapter III, Corollaries 2.11 and 2.14]{DemCADG}. To check the class relation with smooth representatives, write $[Z_j]=\beta_j+\ddc\ell_j$, using a smooth Hermitian metric on the divisor line bundle. Then
\[
 \sum_jc_j\beta_j
   =\ddc\bigl(u-v-\sum_jc_j\ell_j\bigr).
\]
The left side is smooth. Taking its local trace and applying elliptic regularity makes the global $L^1$ potential on the right smooth. Hence the displayed form is $\ddc$-exact in smooth Bott--Chern cohomology, proving \eqref{eq:semipositive-dual-divisorial-difference}.

Near a regular point of $Z_j$ lying on no other component, choose a local defining function $z_1$. In our normalization $\ddc\log|z_1|^2=[Z_j]$, so
\[
 \ddc\bigl(u-v-c_j\log|z_1|^2\bigr)=0.
\]
The expression in parentheses is a smooth pluriharmonic function by distributional elliptic regularity. Taking generic Lelong numbers therefore gives $c_j=\nu_{Z_j}(u)-\nu_{Z_j}(v)$. If $u\sim_{\mathcal I}v$, these numbers agree by \cref{thm:local-i-inputs}, so all coefficients vanish. Ordinary equivalence implies multiplier-ideal equivalence. Alternatively, independence of the divisor classes forces them all to vanish directly from \eqref{eq:semipositive-dual-divisorial-difference}. In either case $\ddc(u-v)=0$ globally, and a real pluriharmonic distribution on connected compact $X$ is constant. When $Z$ has codimension at least two, the sum is empty.
\end{proof}

The theorem assumes a smooth form. It neither defines a wedge product with an arbitrary singular maximizing current nor proves that such a current has an analytic degeneracy set. The divisor relation is necessary for two threshold solutions to differ; it does not assert that every relation is realized. No bounded mass, positive lower mass, root-tail condition, or convergence of an exponential approximation is used.
