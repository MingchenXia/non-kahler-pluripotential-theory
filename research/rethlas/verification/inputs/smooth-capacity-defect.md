Run_id: smooth_capacity_defect_01

Statement: Verify the following corollary and complete proof, including the common-subsequence assertion for all real T>0 and the whole-total-variation limit. This is a bounded follow-up; no novelty or whole-book certification is claimed.

Ambient setting: X is a connected compact complex manifold of dimension n>=1; omega is a Hermitian form. PSH(X,omega) consists of quasi-plurisubharmonic u with omega+dd^c u>=0. All smooth measures use the same normalization as the book. The capacity is Cap_omega(E)=sup_{v omega-psh, 0<=v<=1} integral_E (omega+dd^c v)^n. Whole total variation is the total mass of the variation measure. v_+(omega) is the supremum of total masses over bounded omega-psh potentials; it is permitted to be infinite.

Accepted internal inputs (verify every use, but do not reopen their proofs):
1. Corollary smooth-prescribed-masses: if v_+(omega)=infinity, any epsilon_j in (0,1) tending to zero and any finite b_j>V_omega=int omega^n can be realized by smooth w_j=s_j u_j, where u_j is omega-psh with sup u_j=0 and 0<s_j<epsilon_j. Their exact masses are b_j and omega+dd^c w_j>=(1-epsilon_j)omega. They tend to zero in L1 for a fixed smooth positive volume (therefore for any such volume); their currents converge in coefficient L1 and full Gauduchon traces in total variation. For every fixed p>0, exp(-p w_j) tends to 1 in L1. This construction was independently checked in smooth_prescribed_masses_01.
2. Normalized sublevel-capacity estimate (eq:global-capacity-tail): Cap_omega({u<-t})<=C/t for all normalized sup-zero omega-psh u and t>1. Constant depends only on the background. Its proof uses local weighted CLN, normalized L1 compactness, and fixed bounded capacity tests; it does not use equation existence, BMP, or the new result. It was included in weak_lp_existence_01.
3. Damped continuity (thm:damped-continuity): for nonpositive omega-psh h_j,h converging in capacity and each fixed p>0, exp(p h_j) MAext_omega(h_j) converges weakly to exp(p h) MAext_omega(h). For smooth potentials these are ordinary smooth top powers; h=0 has measure omega^n. No upper-mass hypothesis is part of this input.

Other classical inputs are positivity of wedges of smooth positive forms, equivalence of smooth positive volume norms on compact X, Chebyshev's inequality, weak sequential compactness of positive measures with fixed mass on a compact metrizable space, and elementary whole-total-variation properties. No external-paper citation is made.

The LaTeX references correspond exactly to the accepted inputs above. The displayed proof follows; inspect all quantifiers and limits in order. Do not modify the manuscript or earlier verifier records. Use the standard verifier tools and write only the new run output through its usual workflow.

Proof:

The preceding example has a singular limit. When bounded mass fails, the smooth sequence of \cref{cor:smooth-prescribed-masses} has a smooth limit and still loses continuity of its total mass. The loss occurs entirely at deep sublevels. Recall that $v_+(\omega)$ is the supremum of $\int_X(\omega+\ddc v)^n$ over bounded $v\in\PSH(X,\omega)$.

\begin{corollary}\label{cor:smooth-capacity-mass-defect}
Assume $v_+(\omega)=+\infty$ and put $V_\omega=\int_X\omega^n$. Fix a real number $b>V_\omega$ and a sequence $0<\varepsilon_j<1$ tending to zero. The smooth potentials $w_j$ in \cref{cor:smooth-prescribed-masses}, chosen with mass $b$, converge to zero in capacity. For every $T>0$,
\[
 \left\|\mathbf1_{\{w_j\geq-T\}}(\omega+\ddc w_j)^n-\omega^n
 \right\|_{\mathrm{TV}}\longrightarrow0,
 \qquad
 \int_{\{w_j<-T\}}(\omega+\ddc w_j)^n\longrightarrow b-V_\omega.
\]
Here $\|\cdot\|_{\mathrm{TV}}$ is the whole total variation norm of a signed measure. After passage to a subsequence, there is a positive measure $\sigma$ of mass $b-V_\omega$ such that
\[
 (\omega+\ddc w_j)^n\rightharpoonup\omega^n+\sigma,
 \qquad
 \mathbf1_{\{w_j<-T\}}(\omega+\ddc w_j)^n\rightharpoonup\sigma
 \quad\text{for every }T>0.
\]
\end{corollary}
\begin{proof}
The construction in \cref{cor:smooth-prescribed-masses} gives $w_j=s_j u_j$, where $u_j$ is smooth and $\omega$-plurisubharmonic, $\sup_Xu_j=0$ and $0<s_j<\varepsilon_j$. The normalized sublevel estimate \eqref{eq:global-capacity-tail}, whose proof uses only the local weighted Chern--Levine--Nirenberg inequality and normalized $L^1$ compactness, gives, for every fixed $\delta>0$ and all sufficiently large $j$,
\[
 \operatorname{Cap}_\omega(\{|w_j|>\delta\})
 =\operatorname{Cap}_\omega(\{u_j<-\delta/s_j\})
 \leq Cs_j/\delta\longrightarrow0.
\]
This use of the later estimate does not depend on any equation-existence theorem.

Put $\mu_j=(\omega+\ddc w_j)^n$. Fix $T>0$ and write $E_{j,T}=\{w_j\geq-T\}$. The lower bound in \cref{cor:smooth-prescribed-masses} gives
\[
 \mathbf1_{E_{j,T}}\mu_j\geq
 \lambda_{j,T}:=(1-\varepsilon_j)^n\mathbf1_{E_{j,T}}\omega^n.
\]
Since $w_j\to0$ in $L^1$, the smooth volume of $X\setminus E_{j,T}$ tends to zero. Hence $\lambda_{j,T}\to\omega^n$ in total variation. For every $p>0$, \cref{thm:damped-continuity} gives $\int_X\mathrm{e}^{pw_j}\,\mathrm{d}\mu_j\to V_\omega$, and therefore
\[
 \limsup_j\mu_j(E_{j,T})
 \leq\mathrm{e}^{pT}\lim_j\int_X\mathrm{e}^{pw_j}\,\mathrm{d}\mu_j
 =\mathrm{e}^{pT}V_\omega.
\]
Let $p\downarrow0$. Together with the lower bound this proves $\mu_j(E_{j,T})\to V_\omega$. Positivity now yields
\[
 \begin{split}
 \|\mathbf1_{E_{j,T}}\mu_j-\omega^n\|_{\mathrm{TV}}
 &\leq\mu_j(E_{j,T})-\lambda_{j,T}(X)
       +\|\lambda_{j,T}-\omega^n\|_{\mathrm{TV}}\\
 &\longrightarrow0.
 \end{split}
\]
Subtracting this shallow mass from $\mu_j(X)=b$ proves the tail identity.

The positive measures $\mu_j$ have fixed mass on compact $X$, so a subsequence converges weakly to a measure $\nu$ of mass $b$. The inequality $\mu_j\geq(1-\varepsilon_j)^n\omega^n$ gives $\nu\geq\omega^n$. Set $\sigma=\nu-\omega^n$. For each $T>0$, subtract the already established total-variation limit of the shallow restrictions from $\mu_j\rightharpoonup\nu$. This gives the last assertion along the same subsequence for every $T$.
\end{proof}

Thus capacity convergence and a uniform bound on the masses do not replace the tail hypothesis, even for smooth approximants converging to a smooth potential. The currents in this example also converge in coefficient $L^1$, and their Gauduchon traces converge in total variation. The argument does not prescribe the support or the singularity type of the defect measure $\sigma$.

