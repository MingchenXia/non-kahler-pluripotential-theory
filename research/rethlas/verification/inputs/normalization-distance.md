Run_id: normalization_distance_01

Run scope: Bounded verification through the normal Rethlas workflow. The parent process is actively editing and preparing the manuscript release. Restrict writes to normal verifier runtime, memory and output tools. Leave book files, BLUEPRINT.md, research/STATUS.md, CHANGELOG.md, other editorial files and Git publication to the parent. Never rewrite any existing report, frozen input or source reference.

Statement: Check the candidate entropy variational lemma, finite pseudometric on admitted model references, exact dual formula on the common finite-entropy domain, measurable-data stability under Delta convergence, and the projective examples below. No novelty claim. The old scalar comparison and zero-reference corollary are accepted only with their actual hypotheses.

Important convention audit: chapter_analytic_approximation.tex defines analytic singularities with POSITIVE RATIONAL coefficient c. The checkpoint69 analytic family P_theta[ta], as written for arbitrary real 0<t<1, invokes the analytic-envelope theorem without explicitly keeping that convention. The parent found this mismatch after the bounded report reference_comparison_01, which had not audited this convention. Do NOT overwrite that report. For the present revision, restrict t to rational numbers in (0,1) in ex:analytic-reference-normalization. The existing analytic-envelope equivalence and resulting model property then apply literally. All occurrences of the new analytic projective family use rational t as well. General scalar/dual comparisons and the small-epsilon_j corollary still allow real epsilon_j, since these do not assert analytic singularities. Verify that this restriction repairs the example without assuming ordinary-envelope idempotence for arbitrary singularities.

Accepted internal inputs:
1. Chapter15 works with fixed smooth semipositive big theta and smooth positive dV. Each admitted reference is a model P_theta[phi]=phi with P_{epsilon theta}(phi) genuine for some 0<epsilon<1. Scalar B_phi(G) is finite for bounded measurable G, is one-Lipschitz in sup norm, and is continuous under L1(dV) convergence of uniformly bounded measurable G for EACH FIXED reference (thm:normalization-bounded-lone). Ordinary-type solutions and scalar uniqueness exist in this regime. Neither BMP nor a separate positive-lower-mass hypothesis is imposed.
2. H_phi(nu)=sup_{G continuous}[B_phi(G)+integral G dnu]. Its finite sublevels are weakly compact, have uniformly integrable densities, and on them weak measure convergence implies weak L1 convergence (thm:normalization-dual-compactness). The dual minimum and nonempty supporting sets hold for all bounded measurable G, with integrals understood for finite H, whose measures are absolutely continuous (thm:normalization-measurable-adjoint). At a support nu in A_phi(G), H_phi(nu)=B_phi(G)+integral G dnu. H_phi is weakly lower semicontinuous.
3. cor:prescribed-dual-entropy identifies finite H_phi exactly with finite entropy for all admitted references. Its statement uses dV(X)=1; smooth-volume change gives the same finite-domain assertion for a non-normalized smooth positive volume. H'_phi(nu)=H_phi(nu)-integral a dnu when dV'=exp(a)dV, and B'_phi(G)=B_phi(G+a). This transformation is already proved directly before the entropy bounds, without the new variational lemma.
4. prop:reference-normalization-comparison gives B_0+n log(1-epsilon)<=B_phi<=B_0 on all C(X); both extended dual inequalities hold. Each admitted reference has its own epsilon, so this makes the proposed uniform difference finite. No common epsilon across a Delta-convergent family is newly assumed.
5. Closed Kahler backgrounds: ordinary bounded equivalence preserves non-pluripolar mass. The standing references have positive mass m_phi, and B_phi(G)=log m_phi-log integral exp(G)dV (eq:normalization-closed-formula). The analytic-envelope theorem prop:analytic-envelope-type gives P_theta[a] ordinarily equivalent to a and equal to Q_theta[a] for analytic a in any smooth background. Bounded-change invariance of P_theta implies its model identity in this analytic case.
6. dd^c=i/(2pi)partial barpartial, so dd^c log|z|^2=delta_0. The book uses multiplier weight exp(-u): I(lambda log|z|^2)=(z^floor(lambda)). For normalized Fubini--Study theta on P^n and a hyperplane section s_D, dd^c log|s_D|^2=[D]-theta. The non-pluripolar measure of ta_D vanishes on D and equals (1-t)^n theta^n off D. The projective example is placed in Chapter16 after the already proved analytic-envelope example.

Proposed editorial use after verification:
- Put the elementary entropy lemma after the entropy definition and before the closed-case computation. The existing closed-case proposition keeps its statement and has a one-line proof by substituting the closed scalar formula into the lemma. The later Hermitian entropy proof uses the lemma directly for every probability, with changes of variable F=qG and F=G/n; this also covers non-absolute-continuity without repeating the dual compactness argument. The prescribed entropy proof uses the lemma with F=qG for its lower bound and keeps its existing upper comparison. No proof depends on a later entropy result.
- Put the new pseudometric subsection after the scalar reference-comparison proposition and before the existing zero-reference corollary. Replace only that corollary's proof by: delta_j=-n log(1-epsilon_j)->0; scalar comparison bounds the uniform scalar difference by delta_j, giving uniform convergence on C(X); the new general stability proposition with fixed limiting reference zero proves all supporting-probability assertions. This is a forward-free reuse, since the general proposition is placed first and does not use the corollary.
- Restrict the previous analytic example's scaling parameter to rational t in (0,1) as above. No mathematical claim for arbitrary real scaling is retained through that analytic theorem. A limit along rational t suffices for the example and sharpness.

Check every finite/infinite domain issue: dual differences are taken only where both H are finite. Check the factor 2 in the stability gap, the measurable approximation of scalar tests for a fixed pair, and passage against varying bounded measurable G_j using uniform integrability and weak L1. No strong L1, total variation, potential convergence, completeness or separation of singularity types is claimed.

Proofs:


\begin{lemma}\label{lem:entropy-variational}
For every Borel probability measure $\nu$,
\[
 \operatorname{Ent}_{\mathrm{d}V}(\nu)
 =\sup_{F\in C(X)}\left(\int_XF\,\mathrm{d}\nu
                     -\log\int_X\mathrm{e}^F\,\mathrm{d}V\right).
\]
The identity includes infinite values and requires no geometric hypothesis on the background.
\end{lemma}
\begin{proof}
If $\nu$ is not absolutely continuous, choose a compact set $K$ with $\mathrm{d}V(K)=0$ and $\nu(K)>0$. For $t>0$, regularity and a continuous cutoff give $0\leq\chi_t\leq1$, equal to one on $K$, with support of volume at most $\mathrm{e}^{-2t}$. With $F=t\chi_t$, the expression in the supremum is at least
\[
 t\nu(K)-\log\bigl(\mathrm{d}V(X)+\mathrm{e}^{-t}\bigr),
\]
which tends to infinity.

Suppose $\nu=h\,\mathrm{d}V$. When its entropy is finite, Jensen's inequality for the logarithm gives
\[
 \int_XF\,\mathrm{d}\nu-\operatorname{Ent}_{\mathrm{d}V}(\nu)
 \leq\log\int_{\{h>0\}}\mathrm{e}^F\,\mathrm{d}V
 \leq\log\int_X\mathrm{e}^F\,\mathrm{d}V.
\]
For infinite entropy the resulting upper bound is automatic. For the opposite inequality set
\[
 F_k=\log\bigl(\max\{k^{-1},\min\{h,k\}\}\bigr),\qquad k\geq1.
\]
Then $\int_X\mathrm{e}^{F_k}\,\mathrm{d}V\to1$, and $\int_XF_k\,\mathrm{d}\nu\to\operatorname{Ent}_{\mathrm{d}V}(\nu)$, with infinity allowed. The positive parts converge increasingly, and the negative parts are dominated by the integrable negative part of $h\log h$. For each fixed $k$, approximate $F_k$ in $L^1(\mathrm{d}V+\nu)$ by continuous functions with the same bounds. Their two integrals converge to those of $F_k$, including the exponential integral. The continuous supremum is therefore at least its value at $F_k$. Let $k\to\infty$.
\end{proof}


\subsection{Uniform comparison of the scalar functionals}

The preceding limit has a functional formulation that also applies away from reference zero. Fix $\theta$ as above and, for two references satisfying \eqref{eq:normalization-reference}, put
\begin{equation}\label{eq:normalization-distance}
 \Delta(\varphi,\psi)
   =\sup_{G\in C(X)}|B_\varphi(G)-B_\psi(G)|.
\end{equation}
The comparison with $B_0$ makes this number finite for every such pair. It is a pseudometric: symmetry, vanishing on the diagonal and the triangle inequality follow from the uniform norm. Distinct singularity types can have distance zero, as \cref{ex:normalization-distance-projective} shows.

\begin{proposition}\label{prop:normalization-distance-dual}
For admitted model references,
\[
 \Delta(\varphi,\psi)
 =\sup_{\operatorname{Ent}_{\mathrm{d}V}(\nu)<\infty}
                       |H_\varphi(\nu)-H_\psi(\nu)|,
\]
where the supremum is over probability measures. The same value is obtained in \eqref{eq:normalization-distance} using all bounded measurable $G$. It is independent of the smooth positive reference volume.
\end{proposition}
\begin{proof}
By \cref{cor:prescribed-dual-entropy}, finite entropy is the common finite domain of the two duals; rescaling the reference volume to have mass one does not change finiteness. A uniform bound for $|B_\varphi-B_\psi|$ passes to their defining suprema, so the displayed supremum is at most $\Delta(\varphi,\psi)$. Conversely, denote that supremum by $D$. If $\nu\in\mathcal A_\psi(G)$, it has finite entropy and the dual minimum formula gives
\[
 B_\varphi(G)
 \leq H_\varphi(\nu)-\int_XG\,\mathrm{d}\nu
 \leq B_\psi(G)+D.
\]
Interchanging the references proves the opposite inequality. Thus $\Delta\leq D$.

For bounded measurable $G$, take continuous approximations with the same uniform bound converging in $L^1(\mathrm{d}V)$. The continuity theorem \cref{thm:normalization-bounded-lone}, applied separately to the two fixed references, extends the scalar bound to $G$. Finally a volume change $\mathrm{d}V'=\mathrm{e}^a\mathrm{d}V$ replaces each $B(G)$ by $B(G+a)$. Translation by $a\in C(X)$ is a bijection of the test space, so the supremum is unchanged.
\end{proof}

\begin{proposition}\label{prop:normalization-distance-stability}
Suppose $\Delta(\varphi_j,\varphi)\to0$. Let $G_j,G$ be uniformly bounded measurable functions with $G_j\to G$ in $L^1(\mathrm{d}V)$, and choose $\nu_j\in\mathcal A_{\varphi_j}(G_j)$. Their densities are uniformly integrable. Every weak cluster point belongs to $\mathcal A_\varphi(G)$, and convergence of a subsequence also holds weakly in $L^1$. If $\mathcal A_\varphi(G)$ is a singleton, the full sequence converges to it in these two senses.
\end{proposition}
\begin{proof}
Write $\delta_j=\Delta(\varphi_j,\varphi)$. The scalar and dual bounds, together with the supporting identity, give
\[
 0\leq H_\varphi(\nu_j)-\int_XG_j\,\mathrm{d}\nu_j-B_\varphi(G_j)
       \leq2\delta_j.
\]
If $\|G_j\|_\infty\leq M$, then $H_\varphi(\nu_j)\leq B_\varphi(0)+2M+2\delta_j$. Thus all measures lie in one finite dual sublevel. By \cref{thm:normalization-dual-compactness}, their densities are uniformly integrable, and a weakly convergent subsequence also converges weakly in $L^1$.

Let its limit be $\nu$. Uniform integrability, the common bound and convergence in measure give $\int_X|G_j-G|\,\mathrm{d}\nu_j\to0$. Weak $L^1$ convergence applies to the bounded function $G$, and \cref{thm:normalization-bounded-lone} gives $B_\varphi(G_j)\to B_\varphi(G)$. Lower semicontinuity in the displayed inequality yields
\[
 H_\varphi(\nu)-\int_XG\,\mathrm{d}\nu-B_\varphi(G)\leq0.
\]
The measurable dual minimum formula gives the reverse inequality and identifies equality with $\nu\in\mathcal A_\varphi(G)$. Compactness proves whole-sequence convergence when this set is a singleton.
\end{proof}

This criterion concerns the scalar functionals and their supporting probabilities. It does not assert convergence of the solution potentials. To use it for a family of singularities, one still needs a way to prove $\Delta\to0$ from information about those singularities. The preceding smaller-background comparison gives one such condition.


\begin{example}\label{ex:normalization-distance-projective}
The pseudometric retains only the mass in a closed K\"ahler background. Indeed \eqref{eq:normalization-closed-formula} gives
\[
 \Delta(\varphi,\psi)=|\log m_\varphi-\log m_\psi|.
\]
For an explicit calculation, let $\theta$ be the Fubini--Study form on $\mathbb P^n$, normalized by $\int_X\theta^n=1$, and let $D$ be a hyperplane. A defining section with its Fubini--Study metric gives $a_D=\log|s_D|^2\leq0$ after rescaling, with
\[
 \ddc a_D=[D]-\theta,\qquad
 \theta+\ddc(ta_D)=(1-t)\theta+t[D].
\]
Take a rational $0<t<1$ and put $\varphi_{t,D}=P_\theta[ta_D]$. As in \cref{ex:analytic-reference-normalization}, this is an admitted model reference of ordinary type $ta_D$. Off $D$ its original representative has Monge--Amp\`ere measure $(1-t)^n\theta^n$, and its non-pluripolar measure puts no mass on $D$. Invariance of mass under bounded changes in the closed background therefore gives
\[
 m_{\varphi_{t,D}}=(1-t)^n,\qquad
 B_{\varphi_{t,D}}(G)-B_0(G)=n\log(1-t).
\]
Thus the constant in \cref{prop:reference-normalization-comparison} is sharp.

On $\mathbb P^1$, choose two distinct points $p,q$ for $D$. The corresponding references have distance zero, although one is unbounded at $p$ and bounded at $q$, while the other has the reverse behavior. They are not ordinarily equivalent. For every positive integer $m$,
\[
 \mathcal I(m\varphi_{t,p})=\mathcal O(-\lfloor mt\rfloor p),\qquad
 \mathcal I(m\varphi_{t,q})=\mathcal O(-\lfloor mt\rfloor q).
\]
The one-variable integrability criterion proves these identities. For $mt\geq1$ the ideals differ. Thus $\Delta$ does not separate ideal types either, and cannot replace the singularity topology sought in this chapter.
\end{example}
