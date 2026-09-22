Run_id: entropy_mass_extrema_01

Statement: Check the proposed exact entropy-difference extrema and the invariance conclusions below through the normal Rethlas workflow. This is a separate candidate beyond checkpoint66, with no novelty claim. The range consists only of probabilities with finite entropy. The intended equalities allow log v_-=-infinity and log v_+=+infinity; the difference itself is finite for each probability in the domain.

Accepted internal inputs: for every continuous real G, the Hermitian zero-reference scalar B_0(G) has a bounded solution with measure exp(B_0(G)+G)dV; every smooth G has a smooth strictly positive solution, and the scalar is unique (chapter_normalization.tex and chapter_smooth_equations.tex). H_0(nu)=sup_{G continuous}(B_0(G)+integral G dnu); supporting probabilities A_0(G) are nonempty and satisfy H_0(sigma)=B_0(G)+integral G dsigma (section_normalization_dual.tex). The entropy variational formula sup_F[integral F dnu-log integral exp(F)dV]=Entropy(nu), including infinite entropy, is proved there. The new checkpoint66 proposition prop:hermitian-dual-entropy-bounds says H_0 finite iff entropy finite on a Hermitian background with reference zero and smooth probability volume; it passed hermitian_dual_entropy_01. The mass extrema v_-(omega),v_+(omega) are the infimum and supremum over bounded omega-psh potentials. They agree with the extrema over smooth strictly positive potentials, by bounded monotone regularization (thm:gaud-volume-mass-extrema in section_gauduchon_volume_extrema.tex, whose proof does not use the candidate; the proof below instead cites the earlier regularization theorem directly). This also identifies them with extrema over the smooth normalized equation masses. Every bounded potential has finite positive mass, but no uniform bound or positive lower infimum is assumed. Under changing dV to exp(a)dV, the established dual transformation is H'_0(nu)=H_0(nu)-integral a dnu; entropy has the same transformation. Smooth background transport by u->u-h preserves bounded solution types whenever both omega and omega+dd^c h are Hermitian.

For smooth G the supporting probability is uniquely the smooth strictly positive Gauduchon adjoint, by thm:normalization-gauduchon-recovery; hence both extremizing families below are smooth strictly positive probabilities. Check also this stronger restricted-domain statement.

Check each direction of the entropy comparison and the sharpness arguments: Gibbs probabilities must give the upper extreme, while supporting probabilities give the lower extreme. Check the finite entropy of both chosen measures, the zero/infinite endpoints, scalar normalization, lack of circular dependence on the later mass-extrema statement, both invariances, and the constant-difference criterion. No extremum-attaining probability is claimed, nor any regularity, mass property, or exact equation for arbitrary unbounded densities. Preserve existing verifier memory, inputs, results and references; use only normal output tools for the new report.

Proof:


Proof:

\subsection{The mass bounds as entropy differences}

Let $\mathcal P_{\mathrm{ent}}(X)$ denote the probabilities of finite entropy relative to the fixed smooth probability volume $\mathrm{d}V$. By \cref{prop:hermitian-dual-entropy-bounds}, the difference $H_0(\nu)-\operatorname{Ent}_{\mathrm{d}V}(\nu)$ is a finite real number for every $\nu$ in this set.

\begin{proposition}\label{prop:entropy-mass-extrema}
For every compact Hermitian background $\omega$,
\[
 \begin{split}
 \inf_{\nu\in\mathcal P_{\mathrm{ent}}(X)}
      \bigl(H_0(\nu)-\operatorname{Ent}_{\mathrm{d}V}(\nu)\bigr)
       &=\log v_-(\omega),\\
 \sup_{\nu\in\mathcal P_{\mathrm{ent}}(X)}
      \bigl(H_0(\nu)-\operatorname{Ent}_{\mathrm{d}V}(\nu)\bigr)
       &=\log v_+(\omega).
 \end{split}
\]
The same extrema are obtained by restricting to smooth strictly positive probability measures. Here $\log0=-\infty$ and $\log(+\infty)=+\infty$. Thus boundedness of this difference above is equivalent to bounded mass, and boundedness below is equivalent to positive lower mass.
\end{proposition}
\begin{proof}
Write $Z_G=\int_X\mathrm{e}^G\,\mathrm{d}V$. The bounded solution for $G\in C(X)$ has mass $\mathrm{e}^{B_0(G)}Z_G$. If $v_-(\omega)>0$, its lower mass bound gives
\[
 B_0(G)\geq\log v_-(\omega)-\log Z_G.
\]
Taking the defining supremum for $H_0$ and using the entropy variational formula gives $H_0-\operatorname{Ent}_{\mathrm{d}V}\geq\log v_-(\omega)$ on $\mathcal P_{\mathrm{ent}}(X)$. If $v_+(\omega)<\infty$, the upper mass bound gives the reverse estimate $H_0-\operatorname{Ent}_{\mathrm{d}V}\leq\log v_+(\omega)$ in the same way. The corresponding bounds are automatic when their endpoints are infinite.

To prove sharpness, first take smooth real $G$ and its Gibbs probability $\nu_G=Z_G^{-1}\mathrm{e}^G\,\mathrm{d}V$. This has finite entropy. Testing the supremum defining $H_0$ with $G$ gives
\[
 H_0(\nu_G)-\operatorname{Ent}_{\mathrm{d}V}(\nu_G)
       \geq B_0(G)+\log Z_G.
\]
For the other direction, let $\sigma_G$ be the smooth strictly positive Gauduchon adjoint probability of \cref{thm:normalization-gauduchon-recovery}. It lies in $\mathcal A_0(G)$, so its dual value is $B_0(G)+\int_XG\,\mathrm{d}\sigma_G$. The entropy variational inequality yields
\[
 H_0(\sigma_G)-\operatorname{Ent}_{\mathrm{d}V}(\sigma_G)
       \leq B_0(G)+\log Z_G.
\]
As smooth $G$ varies, the infimum and supremum of the solution masses $\mathrm{e}^{B_0(G)}Z_G$ are $v_-(\omega)$ and $v_+(\omega)$ because these are all smooth strictly positive potential masses. By \cref{thm:bounded-exact-regularization}, every bounded potential mass is a limit of such masses. Both chosen probabilities are smooth and strictly positive. The last two inequalities prove sharpness on this smaller domain, including zero lower mass and infinite upper mass. The two equivalences follow.
\end{proof}

The lower and upper properties therefore control different sides of a scalar difference. This does not give equality of the two mass bounds or conservation of mass in a nonclosed background.

The difference is independent of the smooth positive reference volume used to define it. Under $\mathrm{d}V'=\mathrm{e}^a\mathrm{d}V$, both $H_0$ and $\operatorname{Ent}$ change by $-\int_Xa\,\mathrm{d}\nu$; see the transformation formula preceding \cref{prop:hermitian-dual-entropy-bounds}. Finite entropy is unchanged because $a$ is bounded. If $\omega'=\omega+\ddc h$ is also Hermitian, transporting bounded solutions by $u\mapsto u-h$ preserves $B_0$ and hence this difference. Finally it is constant on the finite-entropy domain exactly when $v_-(\omega)=v_+(\omega)$, that is, when the masses of all bounded potentials agree.
