Run_id: gauduchon_moment_threshold_01

Statement: Check the lemma, proposition and conditional theorem below through the normal Rethlas workflow. These are candidate additions beyond checkpoint63. The objective is an exact equation at a positive individual threshold, without either global mass property, assuming bounded first moments along one smooth maximizing Gauduchon sequence and a genuine smaller-background envelope of the greatest normalized threshold subsolution. Do not assume any regularity or convergence of singular maximizing currents. No novelty claim is made.

Accepted earlier inputs (read exact sources as needed): ordered contact for finite maxima of arbitrary genuine potentials (book/author/chapter_products.tex); monotone capacity convergence with a genuine common lower bound and common upper bound (book/author/section_relative_compactness.tex); damped continuity of exp(u) MA_ext(u) for nonpositive potentials converging in capacity (book/author/chapter_damped_measures.tex); normalized quasi-psh compactness, Choquet envelope lemma and Hartogs upper-tail identification. Earlier attained density threshold and greatest exponential solution with c_lambda>=b, c_lambda->b, c_lambda exp(lambda v_lambda)f->bf in L1, and comparison v_lambda>=s-lambda^-1 log(c_lambda/b) for every normalized threshold subsolution s (book/author/section_individual_density_subsolutions.tex and section_individual_exponential_equations.tex). The smooth-test Gauduchon formula rho_omega(p)=sup_T D_p(T)=b^-1/n, and the unbounded trace inequality against any smooth positive (n-1,n-1) form (book/author/section_threshold_trace_saturation.tex). The lower-barrier capacity criterion (prop:lower-barrier-criterion in section_relative_compactness.tex) requires phi-C<=u_j<=C, genuine P_delta theta(phi), L1 limit u preceq phi, and vanishing integral |exp(u_j)-exp(u)| MA_ext(u_j); it implies capacity convergence without a mass property. These named prior statements are accepted inputs with their actual scopes, not claims to recertify the entire book.

Check every step of the new closure argument, including tail-inf densities, possibly infinite undamped masses, finite maxima of unbounded functions, canonical increasing limits and the two damped passages. Check normalization of Phi_f, compactness, no accidental equation claim for it. For the theorem check the directions of the inequalities, Jensen, all normalizations, genuine envelopes, limit ordinary type, and use of damped continuity to establish exact equality and finiteness only after capacity convergence. Check the sufficiency of the two simple conditions in the final paragraph. No assertion that either new hypothesis is automatic at zero lower mass is intended. Preserve all frozen sources, previous results and verifier memory; only normal verifier output tools should write the new result.

Proof:

\subsection{The greatest normalized threshold subsolution}

A lower bound for a Monge--Amp\`ere density survives $L^1$ convergence of potentials. This uses upper envelopes and damped continuity, rather than continuity of the original Monge--Amp\`ere measures.

\begin{lemma}\label{lem:density-subsolution-lone-closure}
Let $s_j,s\in\PSH(X,h)$ have a common upper bound and satisfy $s_j\to s$ in $L^1(X)$. Suppose $g_j,g\geq0$, $g_j\to g$ in $L^1(\mathrm{d}V)$, and
\[
 \mathrm{MA}^{\mathrm{ext}}_h(s_j)\geq g_j\,\mathrm{d}V.
\]
Then $\mathrm{MA}^{\mathrm{ext}}_h(s)\geq g\,\mathrm{d}V$.
\end{lemma}
\begin{proof}
Translate the potentials to be nonpositive and extract a subsequence for which both convergences hold almost everywhere. Set
\[
 a_j=\inf_{\ell\geq j}g_\ell,\qquad
 w_j=\left(\sup_{\ell\geq j}s_\ell\right)^*.
\]
Then $0\leq a_j\uparrow g$ almost everywhere and $w_j\downarrow s$. For fixed $j$, the finite maxima $\max_{j\leq\ell\leq N}s_\ell$ have measures at least $a_j\,\mathrm{d}V$ by ordered contact. They increase to $w_j$ after regularization, with the genuine lower bound $s_j$ and upper bound zero. The convergence holds in capacity: truncate at a fixed negative level, use bounded monotone capacity convergence, and then let the level tend to infinity using the genuine lower bound. Damped continuity therefore gives
\[
 \mathrm{e}^{w_j}\mathrm{MA}^{\mathrm{ext}}_h(w_j)
       \geq \mathrm{e}^{w_j}a_j\,\mathrm{d}V.
\]
Indeed the right sides for the finite maxima converge by dominated convergence, since $a_j\leq g$ almost everywhere. Divide by the positive weight off the pole set to obtain $\mathrm{MA}^{\mathrm{ext}}_h(w_j)\geq a_j\,\mathrm{d}V$.

Now $w_j\downarrow s$ is again convergence in capacity with a genuine lower bound. Apply damped continuity once more. Since $0\leq\mathrm{e}^{w_j}a_j\leq g$, dominated convergence gives
\[
 \mathrm{e}^s\mathrm{MA}^{\mathrm{ext}}_h(s)
       \geq\mathrm{e}^s g\,\mathrm{d}V.
\]
Divide on $\{s>-N\}$ and let $N\to\infty$. Both sides of the desired inequality give zero mass to the pole set. Restore the common translation.
\end{proof}

\begin{proposition}\label{prop:greatest-normalized-threshold}
For $b=b_h(f)>0$, the family
\[
 \mathcal S_f=\{s\in\PSH(X,h):\sup_Xs=0,\
             \mathrm{MA}^{\mathrm{ext}}_h(s)\geq bf\,\mathrm{d}V\}
\]
is nonempty and compact in $L^1(X)$. It has a greatest member
\[
 \Phi_f=\left(\sup_{s\in\mathcal S_f}s\right)^*.
\]
Every normalized $L^1$ cluster limit of the greatest exponential solutions from \cref{cor:individual-positive-threshold-exponential} belongs to $\mathcal S_f$ and hence lies below $\Phi_f$.
\end{proposition}
\begin{proof}
Nonemptiness is \cref{thm:individual-density-subsolution}. Normalized compactness and the preceding lemma show that $\mathcal S_f$ is compact. Ordered contact makes it stable under finite maxima. Choose a countable Choquet family for its supremum and take successive finite maxima, including one fixed member of $\mathcal S_f$. This increasing sequence has a genuine lower bound and upper bound zero. Its canonical limit is $\Phi_f$ and its convergence holds in $L^1$. The lemma gives the required measure inequality. Its supremum is zero because it lies between a normalized member and zero. Thus $\Phi_f\in\mathcal S_f$ and it dominates every member.

For an exponential cluster limit, the densities of the measures converge in $L^1$ to $bf$ by \cref{cor:individual-positive-threshold-exponential}. Apply the lemma to these densities and the normalized potentials.
\end{proof}

This proposition asserts a greatest normalized subsolution, not equality of its measure with $bf\,\mathrm{d}V$. In particular it does not assert that $\Phi_f$ has finite mass.


\subsection{A moment condition on maximizing tests}

Smoothness of a maximizing current is one way to obtain an exact threshold equation. Another sufficient condition uses moments of a smooth maximizing sequence and a smaller-background envelope. It makes no regularity assumption on a limiting current.

\begin{theorem}\label{thm:gauduchon-moment-threshold}
Let $n\geq2$, $0\leq f\in L^1(\mathrm{d}V)$ be nonzero, and $b=b_\omega(f)>0$. Put $p=f^{1/n}$ and $R=\rho_\omega(p)=b^{-1/n}$. Suppose there are smooth strictly positive $T_j\in\mathscr G_\omega$ such that
\[
 d_j=D_p(T_j)\longrightarrow R,\qquad
 \mathrm{d}\nu_j=d_j^{-1}p k_{T_j}\,\mathrm{d}V,
\]
and a constant $C$ satisfying
\begin{equation}\label{eq:maximizing-gauduchon-moments}
 \int_X(-v)\,\mathrm{d}\nu_j\leq C
 \quad\text{for all }j\text{ and all }v\in\PSH(X,\omega)
                  \text{ with }\sup_Xv=0.
\end{equation}
For the greatest exponential solutions and their normalizations, one then has
\[
 b\leq c_\lambda\leq b\mathrm{e}^{C\lambda},\qquad
 \Phi_f-C\leq v_\lambda\leq0.
\]
Suppose in addition that $P_{\delta\omega}(\Phi_f)$ is genuine for some $0<\delta<1$. Whenever $\lambda_k\downarrow0$ and $v_{\lambda_k}\to v$ in $L^1(X)$, the convergence holds in capacity and
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(v)=bf\,\mathrm{d}V,
 \qquad \Phi_f-C\leq v\leq\Phi_f.
\]
In particular an exact threshold solution exists. No bounded-mass or positive lower-mass hypothesis is imposed.
\end{theorem}
\begin{proof}
The trace inequality \cref{lem:unbounded-gauduchon-trace-density} and Stokes give, for each $j$ and $\lambda>0$,
\[
 1\geq c_\lambda^{1/n}d_j
              \int_X\mathrm{e}^{\lambda v_\lambda/n}\,\mathrm{d}\nu_j
   \geq c_\lambda^{1/n}d_j\mathrm{e}^{-C\lambda/n}.
\]
The second inequality is Jensen's inequality and \eqref{eq:maximizing-gauduchon-moments}. Let $j\to\infty$. Since $R=b^{-1/n}$, this proves the upper scalar bound. The lower scalar bound and comparison with every normalized threshold subsolution were proved in \cref{cor:individual-positive-threshold-exponential}. Apply that comparison to $\Phi_f$ to obtain
\[
 v_\lambda\geq\Phi_f-\lambda^{-1}\log(c_\lambda/b)
                \geq\Phi_f-C.
\]

Now let $v_{\lambda_k}\to v$ in $L^1$. By \cref{prop:greatest-normalized-threshold}, its limit lies in $\mathcal S_f$ and hence below $\Phi_f$. The lower bound passes to the limit, so $v\simeq\Phi_f$. For all sufficiently large $k$,
\[
 \mathrm{MA}^{\mathrm{ext}}_\omega(v_{\lambda_k})
   =c_{\lambda_k}\mathrm{e}^{\lambda_k v_{\lambda_k}}f\,\mathrm{d}V
   \leq b\mathrm{e}^{C}f\,\mathrm{d}V.
\]
The functions $|\mathrm{e}^{v_{\lambda_k}}-\mathrm{e}^v|$ are uniformly bounded and tend to zero in smooth-volume measure. Their integrals against the fixed $L^1$ density $f$ therefore tend to zero. This gives the self-measure error required by \cref{prop:lower-barrier-criterion}, with reference $\Phi_f$. The additional limit-type condition has just been checked, and the smaller-background condition is an assumption. That proposition gives capacity convergence.

Damped continuity now identifies the equation without a mass-conservation argument. Write $g_k=c_{\lambda_k}\mathrm{e}^{\lambda_k v_{\lambda_k}}f$. We know $g_k\to bf$ in $L^1$ and $0\leq g_k\leq b\mathrm{e}^Cf$ for large $k$. Hence
\[
 \mathrm{e}^{v_{\lambda_k}}\mathrm{MA}^{\mathrm{ext}}_\omega(v_{\lambda_k})
   =\mathrm{e}^{v_{\lambda_k}}g_k\,\mathrm{d}V
   \longrightarrow\mathrm{e}^v bf\,\mathrm{d}V
\]
in total variation, while damped continuity gives the weak limit
$\mathrm{e}^v\mathrm{MA}^{\mathrm{ext}}_\omega(v)$. Divide off the pole set to obtain the equation and its finite mass. Finally normalized compactness supplies an $L^1$ cluster limit along any sequence $\lambda_k\downarrow0$, proving existence.
\end{proof}

The moment condition is automatic if the densities of $\nu_j$ are uniformly bounded in $L^q(\mathrm{d}V)$ for some $q>1$: apply H\"older to the uniform finite moments of normalized quasi-plurisubharmonic functions. The envelope condition is automatic if $\Phi_f$ is bounded. Both conditions are additional hypotheses. Root tails alone have not been shown to imply them. The theorem proves subsequential capacity convergence and existence; it does not identify all normalized solutions, assert whole-family convergence, or assert that $\Phi_f$ itself solves the exact equation.
