Run_id: prescribed_dual_entropy_01

Statement: Verify the following proposed extension of the chapter15 entropy bounds to all the model references already covered by that chapter. This is a candidate, not a claimed result yet and not a novelty claim. Check the exact uses of strict domination, order of singularities, positivity of nonclosed extended products, uniformity in the reference when the same epsilon works, all infinite-value cases and the absence of any BMP/PVP assumption.

Accepted internal inputs, with actual proofs available under book/author:
- chapter_normalization.tex: theta is smooth semipositive and big, phi=P_theta[phi], and P_{epsilon theta}(phi) is genuine for a fixed 0<epsilon<1. For every continuous G there is u of ordinary type phi with MA_theta^ext(u)=exp(B_phi(G)+G)dV; scalar uniqueness holds. The dual is H_phi(nu)=sup_G[B_phi(G)+integral G dnu].
- section_singular_domination.tex, thm:singular-strict-domination: if a is theta-psh with genuine P_{delta theta}(a), b preceq a, and MA(a)<=r MA(b) on {a<b} for 0<=r<1, then a>=b. The background is smooth semipositive and big; the extended measures may have infinite total mass. Bounded equivalence transfers genuineness of the smaller-background envelope.
- section_big_lp_equations.tex, lem:big-lp-subsolution: for any fixed smooth semipositive big background eta and fixed q>1,L>0 there is b>0 so that every nonnegative f of Lq norm at most L admits a bounded eta-psh s, -1<=s<=0, with MA_eta(s)>=bf dV. Its proof uses a fixed strict singular barrier for eta, the Hermitian equations and a convex reparametrization. It does not need a positive lower root integral. All positive multiples of theta are big.
- Positivity on common finite levels gives MA_theta(phi_epsilon+s)>=MA_{(1-epsilon)theta}(s) off the pole set of phi_epsilon when phi_epsilon is epsilon theta-psh. That pole set has zero smooth volume, so the density lower bound extends globally. This same splitting occurs in section_prescribed_existence.tex. Smooth positive background enlargement gives MA_Omega^ext(u)>=MA_theta^ext(u) if Omega>=theta; no signed unrestricted product is used.
- section_hermitian_dual_entropy.tex, prop:hermitian-dual-entropy-bounds: H_{Omega,0}<=A+n Entropy for every smooth Hermitian Omega; hermitian_dual_entropy_01 passed. The lower Hermitian bound and the entropy variational formula also hold. This input is independent of the candidate.
- section_normalization_dual.tex: non-absolutely-continuous probabilities have H_phi=infinity; H_phi never equals minus infinity. The usual variational entropy formula for absolutely continuous probabilities includes infinite entropy.

The candidate now first proves a reusable relative lower-density-norm lemma. For a density F, N=norm(F)_q is positive by strict domination if MA(u)=0; otherwise the comparison uses h=P_{epsilon theta}(phi)+s and u of ordinary type phi. If N<b_q, then MA(u)<=(N/b_q)MA(h+t), forcing u>=h+t for every t. The entropy corollary reuses this lemma. The second comparison uses a bounded Omega solution v and the possibly singular theta solution u: c>c_Omega would force v>=u+t for every t. In both cases choose one point where the genuine potentials are finite for the contradiction. No new equality or attainment formula for singular-reference masses is claimed.

Proposed application in the earlier normalized-equation proof: for MA(v_j)=c_j exp(v_j/j) f dV, v_j of ordinary type phi and sup v_j=0, this lemma with q=p gives b_p<=norm(c_j exp(v_j/j)f)_p<=c_j norm(f)_p. Hence c_j>=b_p/norm(f)_p. This lets that proof choose a subsequential scalar limit c>0 directly and remove its later separate zero-mass contradiction. Check that this is noncircular: the new lemma uses only the earlier bounded subsolution construction, positivity and singular strict domination, not either prescribed equation existence proof.

Check also the final varying-reference consequence: common theta and epsilon, uniformly bounded logarithmic densities G_j, arbitrary supporting probabilities. The scalar comparison gives a uniform upper bound on H_phi_j at these probabilities, the reference-uniform lower entropy estimate gives bounded entropy, and the Hermitian upper entropy estimate places all of them in a single H_{Omega,0} sublevel. Its compactness theorem yields uniform integrability and weak-L1 compactness; limits have finite entropy. This does not identify a limit with the supporting set of a limiting reference.

Proofs:
\begin{lemma}\label{lem:relative-density-lower-bound}
Fix $q>1$ under the preceding hypotheses on $\theta,\varphi$. There is $b_q>0$ such that every $u\in\PSH(X,\theta)$ of ordinary type $\varphi$ with
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)=F\,\mathrm{d}V,
 \qquad 0\leq F\in L^q(\mathrm{d}V),
\]
satisfies $\|F\|_q\geq b_q$. For fixed $\theta$ and smaller-background parameter $\varepsilon$, this constant is independent of $\varphi$.
\end{lemma}
\begin{proof}
Bounded equivalence with $\varphi$ gives a genuine smaller-background envelope for $u$. If $F=0$, strict domination applied to $u,u+1$ is impossible, so $N=\|F\|_q>0$.

Apply \cref{lem:big-lp-subsolution} in background $(1-\varepsilon)\theta$ to $F/N$, whose $L^q$ norm is one. It gives a bounded $s$, with $-1\leq s\leq0$, and a constant $b_q>0$ depending only on this fixed background and $q$, such that
\[
 \mathrm{MA}_{(1-\varepsilon)\theta}(s)\geq(b_q/N)F\,\mathrm{d}V.
\]
Put $h=P_{\varepsilon\theta}(\varphi)+s$. This is a genuine $\theta$-plurisubharmonic potential with $h\preceq u$. The current splitting is positive, so the same density bound holds for $\mathrm{MA}^{\mathrm{ext}}_\theta(h)$. To justify it, first truncate $P_{\varepsilon\theta}(\varphi)$ on finite levels, use positivity of bounded mixed products, and then exhaust its finite locus. Its pole set has zero smooth volume.

If $N<b_q$, we would have
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)
       \leq(N/b_q)\mathrm{MA}^{\mathrm{ext}}_\theta(h+t)
 \quad\text{for every }t\in\mathbb R.
\]
Since $N/b_q<1$, \cref{thm:singular-strict-domination} would imply $u\geq h+t$ for every $t$. At a point where both potentials are finite this is impossible. Thus $N\geq b_q$. The construction of $s$ used no property of $\varphi$, proving the uniform assertion.
\end{proof}

This is a lower bound for the density norm in a prescribed ordinary type. It does not impose a positive lower bound on its total mass.

\subsection{Entropy for a prescribed ordinary type}

The smaller-background condition lets the preceding entropy bounds survive prescribed singularities. The comparison uses a bounded subsolution in the part of the background left over by that condition.

\begin{corollary}\label{cor:prescribed-dual-entropy}
Under the standing hypotheses \eqref{eq:normalization-reference}, normalize $\mathrm{d}V(X)=1$. For every $q>1$ there is a finite real $a_q$, and there is a finite real $A$, such that
\[
 a_q+\frac1q\operatorname{Ent}_{\mathrm{d}V}(\nu)
 \leq H_\varphi(\nu)
 \leq A+n\operatorname{Ent}_{\mathrm{d}V}(\nu)
\]
for every Borel probability $\nu$, including infinite values. Thus finite dual value and finite entropy have the same domain, and uniformly bounded dual values are equivalent to uniformly bounded entropies. For fixed $\theta$ and $\varepsilon$ in \eqref{eq:normalization-reference}, the constants can be chosen independently of the model reference $\varphi$.
\end{corollary}
\begin{proof}
For $G\in C(X)$, apply \cref{lem:relative-density-lower-bound} to a solution of ordinary type $\varphi$ with density $c\mathrm{e}^G$, where $c=\mathrm{e}^{B_\varphi(G)}$. It gives $c\|\mathrm{e}^G\|_q\geq b_q$, hence
\[
 B_\varphi(G)\geq\log b_q-\frac1q
                         \log\int_X\mathrm{e}^{qG}\,\mathrm{d}V.
\]

For the upper bound choose a Hermitian form $\Omega\geq\theta$, and let $B_{\Omega,0}$ denote its bounded-type normalization. A bounded solution $v$ for $G$ in this background has a genuine smaller-background envelope. Moreover $u\in\PSH(X,\Omega)$, $u\preceq v$, and positivity gives
\[
 \mathrm{MA}^{\mathrm{ext}}_\Omega(u)
       \geq\mathrm{MA}^{\mathrm{ext}}_\theta(u)
       =c\mathrm{e}^G\,\mathrm{d}V.
\]
If $c>\mathrm{e}^{B_{\Omega,0}(G)}$, the same strict domination argument, now applied to $v$ and $u+t$ in background $\Omega$, is impossible. Hence $B_\varphi\leq B_{\Omega,0}$ and $H_\varphi\leq H_{\Omega,0}$. \Cref{prop:hermitian-dual-entropy-bounds} gives the required upper bound.

For an absolutely continuous probability, take the defining supremum in the lower scalar estimate and use the entropy variational formula with $F=qG$. This proves the lower bound with $a_q=\log b_q$, including infinite entropy. Every non-absolutely-continuous probability has both values infinite by \cref{thm:normalization-dual-compactness}. The finite-domain and bounded-family assertions follow by taking $q=2$. The lower-density lemma is uniform in the reference for fixed $\varepsilon$, and the upper bound uses only $\Omega$. This proves the final assertion.
\end{proof}

For example, let the model references $\varphi_j$ satisfy the same smaller-background condition with fixed $\varepsilon$, let $\|G_j\|_\infty\leq M$, and choose $\nu_j\in\mathcal A_{\varphi_j}(G_j)$. Then
\[
 H_{\varphi_j}(\nu_j)
 =B_{\varphi_j}(G_j)+\int_XG_j\,\mathrm{d}\nu_j
 \leq B_{\Omega,0}(0)+2M.
\]
The uniform lower entropy estimate bounds their entropies. The Hermitian upper estimate places all $\nu_j$ in a single finite sublevel of $H_{\Omega,0}$. Hence \cref{thm:normalization-dual-compactness} gives weak compactness and uniform integrability of their densities. Every weak limit has finite entropy. This gives compactness as the reference varies; identifying the limit as a supporting probability for a limiting reference requires further information.

The corollary retains the model and smaller-background assumptions. It gives no comparison for an arbitrary singular reference outside this solvability regime, and no formula for the extrema of $H_\varphi-\operatorname{Ent}_{\mathrm{d}V}$ when the reference is singular.
