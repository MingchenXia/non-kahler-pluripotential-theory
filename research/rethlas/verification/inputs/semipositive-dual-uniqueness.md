Run_id: semipositive_dual_uniqueness_01

Statement: Verify the stronger and shorter v2 of the smooth semipositive dual-attainment theorem. Under the identical hypotheses (connected compact complex n>=2, Hermitian omega, nonzero f>=0 in L1, b_omega(f)>0, smooth semipositive maximizing T strictly positive outside a proper analytic set Z), ALL genuine threshold subsolutions should be unique modulo constants, without prescribing multiplier ideals or assuming independence of divisor classes. This replaces the earlier sufficient conditions by a maximum argument. No novelty claim. V2 is OUTSIDE the checked checkpoint48 book until independently checked.

Source: /Users/mingchen/Non-Kahler/research/editorial/section_semipositive_dual_attainment_v2.tex. The previous complete source section_semipositive_dual_attainment.tex and its normal correct report semipositive_dual_attainment_01 are accepted for existence, exactness, local regularity, common full current on X minus Z and the support theorem. The trace/exactness portion in v2 is unchanged. Read the exact new dependency prop:ordered-contact-general in book/author/chapter_products.tex; it applies to arbitrary genuine potentials, arbitrary smooth backgrounds and infinite extended mass. Non-pluripolar measures ignore pole sets. The maximum remains omega-psh. Generic Lelong monotonicity and maximum calculus are standard local inputs already recalled in chapter_igood.tex and chapter_divisorial_models.tex.

Check the new uniqueness proof without assuming its conclusion: w=max(u,v) is a threshold subsolution by ordered contact on the two disjoint pieces {u>=v},{u<v}, including treatment of poles. The already established local formula therefore holds for all three potentials. For q=u and q=v, S=ddc(w-q) is real closed order-zero, hence normal, supported on Z. Demailly CADG ChapterIII Corollaries2.11 and2.14 apply to nonpure Z after discarding its lower-codimension remainder. Local Poincare--Lelong identifies c_j as nu(w,Z_j)-nu(q,Z_j), which is <=0 by w>=q. Pair with ANY smooth strict Gauduchon eta: distributional Stokes gives sum c_j integral_Zj eta^(n-1)=0; every divisor degree is >0, so c_j=0. The resulting globally pluriharmonic distributions w-u and w-v are constants; hence u-v is constant. Verify no boundedness, ideal equivalence, BC independence, BMP, lower mass, or root tails have slipped in. Exact support input and normalization were checked in semipositive_dual_attainment_01; preserve that history. The intended simplification makes an exploratory polytope parameterization unnecessary: do not verify or integrate the separate polytope draft.

Proof:

\subsection{A smooth maximizing form with an analytic degeneracy set}

Strict positivity of a smooth maximizing form can be weakened if its degeneracy is confined to a proper analytic subset. The proof is local away from that subset. A maximum argument and a Gauduchon integral then give uniqueness without prescribing a singularity type.

\begin{theorem}\label{thm:semipositive-dual-exact-equation}
Let $\omega$ be Hermitian on a connected compact complex manifold of dimension $n\geq2$, let $0\leq f\in L^1(\mathrm{d}V)$ be nonzero, and assume $b=b_\omega(f)>0$. Suppose $D_{f^{1/n}}$ has a smooth semipositive maximizer $T\in\mathscr G_\omega$ which is strictly positive on $X\setminus Z$, where $Z$ is a proper analytic subset. Then every threshold subsolution is smooth on $X\setminus Z$ and satisfies
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(u)=bf\,\mathrm{d}V
\]
on $X$. Such a solution exists and has finite mass. The function $f^{1/n}$ has a smooth nonnegative representative on $X\setminus Z$.

All threshold subsolutions differ by constants.
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

It remains to prove uniqueness. Let $v$ be another threshold subsolution and put $w=\max(u,v)$. By \cref{prop:ordered-contact-general},
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(w)\geq
 \mathbf1_{\{u\geq v\}}\mathrm{MA}^{\mathrm{ext}}_\omega(u)
 +\mathbf1_{\{u<v\}}\mathrm{MA}^{\mathrm{ext}}_\omega(v)
 \geq bf\,\mathrm{d}V.
\]
The common pole set has zero mass for all the measures involved. Thus $w$ is also a threshold subsolution, and the preceding argument gives the same smooth current $a\gamma$ for $u,v,w$ on $U$.

For $q=u$ or $q=v$, the current $S=\ddc(w-q)$ is real, closed, of order zero and supported on $Z$. The classical support theorem, \cite[Chapter III, Corollaries 2.11 and 2.14]{DemCADG}, gives
\begin{equation}\label{eq:semipositive-dual-divisorial-difference}
 S=\sum_{j=1}^m c_j[Z_j],\qquad
 c_j=\nu(w,Z_j)-\nu(q,Z_j)\leq0,
\end{equation}
where $Z_j$ are the prime divisorial components of $Z$. Indeed, near a generic smooth point of $Z_j$, the difference $w-q-c_j\log|z_1|^2$ is pluriharmonic, since $\ddc\log|z_1|^2=[Z_j]$ in our normalization. This identifies the coefficient; its sign follows from $w\geq q$. Higher-codimension components carry no closed order-zero $(1,1)$-current.

Choose any smooth strictly positive Gauduchon metric $\eta$. Distributional Stokes gives
\[
 0=\int_X\ddc(w-q)\wedge\eta^{n-1}
   =\sum_jc_j\int_{Z_j}\eta^{n-1}.
\]
Each divisor integral is positive and each $c_j$ is nonpositive, so every coefficient vanishes. Therefore $w-q$ is a global pluriharmonic distribution and is constant on connected compact $X$. Applying this to both $q=u$ and $q=v$ shows that $u-v$ is constant.
\end{proof}

The theorem assumes a smooth form. It neither defines a wedge product with an arbitrary singular maximizing current nor proves that such a current has an analytic degeneracy set. No bounded mass, positive lower mass, root-tail condition, or convergence of an exponential approximation is used.
