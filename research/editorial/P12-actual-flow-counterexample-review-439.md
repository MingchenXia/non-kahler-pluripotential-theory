# Actual radial Chern--Ricci endpoint — research439

The author’s413-line P12 article gives an actual finite-time flow counterexample, rather than only a nef background. Its main numerical implication is negatively resolved in every n>=3. The paper uses Ric=-ddc log(volume); the book uses Ric=-2pi ddc log(volume). The same initial metric therefore has maximal book time tau=1/(2pi), with the same limiting background and volume. Catalogues still have39 open directions until manuscript integration; the checked negative P12 resolution would leave38 original directions open. Conditional convergence results assuming bigness remain intact.

Use the exact data of Section25.12: m=n-1>=2, t=(m-1)/m, a=x/t, theta=omega+a w, mu=omega^m wedge w, Z={p} times the projective line. Put omega0=(n+1)omega+(a+2)w. It is a smooth strictly positive Hermitian form, with volume n(n+1)^m(a+2)mu. It is nonclosed because da wedge w is not identically zero.

In the book convention the Fubini--Study Ricci forms are2pi n omega and4pi w. Hence

\[
 \chi=\operatorname{Ric}(\omega_0)
 =2\pi\bigl(n\omega+2w-\ddc\log(a+2)\bigr).
\]

For actual book time s>=0, write r=2pi s. The affine background is

\[
 \alpha_s=(n+1-nr)\omega+(a+2-2r)w
                     +r\ddc\log(a+2).
\]

When 0<=r<1 the smooth potential -r log(a+2) gives a strict representative: its horizontal coefficient is at least one and its vertical coefficient is at least2(1-r)>0. At r=1 the background is theta+ddc log(a+2). It is nef, not big, and has exact V_mu=n, by the already independently reconstructed radial theorem and smooth gauge invariance. The gauge-potential bijections preserve all quasi-psh potentials and nef approximation, and Gauduchon Stokes preserves every test numerator and the same Hermitian regularization. The logarithm is globally smooth because a+2 is bounded below by two.

For r>1 choose nonzero smooth f>=0 on the base supported where a+2-2r<0. The closed semipositive base-top-degree test S=f omega^m gives

\[
 \int_X(\alpha_s+\ddc v)\wedge S
       =\int_B f(a+2-2r)\omega^m<0.
\]

This excludes every positive current representative, including singular quasi-psh potentials, without restricting a singular current to the fiber or using averaging. At r=1 any smooth strict representative would contradict the radial nonbigness theorem. The exact maximal-time theorem already proved in the book therefore gives a unique actual smooth Chern--Ricci flow until tau=1/(2pi). The displayed strict representatives are reference forms, not asserted to solve the flow equation themselves. In the paper’s normalized time u, u=2pi s and its maximal time is one. The source and book conventions are consistent.

The smooth endpoint restriction to Z is zero: theta restricts to zero there, and the smooth base gauge term has zero pullback. Only smooth forms are restricted. The positive closed current T=[Z]/2 has omega0-trace one, since omega0 restricted to Z is2w. It annihilates alpha_tau and has rank-one normalized matrix n Pi_vert, hence zero determinant-weighted measure for every smooth positive reference density.

For any normalized positive dd^c-closed annihilator R of this endpoint, smooth gauge Stokes gives integral theta wedge R=0. This is a nonnegative measure of total mass zero, hence it vanishes. On every compact K outside Z, theta>=c_K omega0 with c_K>0. Thus sigma_R=omega0 wedge R has no mass on K; a countable compact exhaustion shows its support is in Z. This conclusion uses the explicit semipositive representative, not only determinant vanishing.

The coefficient-matrix convention already used in the book is

\[
 \beta\wedge R=\frac1n\operatorname{tr}(B_\beta P_R)\sigma_R,
 \qquad P_R\geq0,\quad\operatorname{tr}P_R=n.
\]

At Z, theta is positive on the horizontal m-plane and zero on the vertical line. Its zero pairing implies that all horizontal diagonal entries of P_R vanish. Positivity gives |(P_R)ij|^2<=(P_R)ii(P_R)jj, so their rows and columns vanish too. The remaining vertical entry is n. Therefore every such annihilator has matrix n Pi_vert, rank one and determinant measure zero. No uniqueness of the scalar trace probability or of all annihilators is claimed here.

The source’s averaged identity is already a direct specialization of the last displayed flow identity in the complete191-line smooth-cone input. For any finite actual maximal time tau and any normalized endpoint annihilator R, the endpoint equation gives integral chi wedge R=1/tau, so

\[
 \int_X\omega(s)\wedge R=1-s/\tau.
\]

The global smooth potential in the book has coefficient2pi in its time integral; Gauduchon-current Stokes removes it. This works for every positive dd^c-closed R and does not require d-closedness or smoothness. In the explicit model the value is1-2pi s. It is an averaged identity, not a pointwise metric-collapse assertion. It does not give analytic support at an arbitrary endpoint, a limiting metric, local convergence or completeness.

The complete413-line author article has fresh first and automatic second reads, including its complete bounded canonical radial proof, actual all-test minimizers, original nef regularization and all-potential obstruction. The shorter closed base test above independently replaces its fiber averaging. The book’s138-line radial input is unchanged at438; its complete proof reads and the40-obligation435 reconstruction are reused at exact scope. The smooth-root and trace-current formulas are already established in the book. The complete191-line smooth-cone input is read at combined scope:1--63 reused from437,64--191 freshly read; the current-matrix section1--114 is freshly read. No fresh parabolic-primary or Demailly-primary inspection is claimed; those standalone source citations are not additional manuscript premises. The maximal-time and matrix statements used here are the exact existing book statements, with their earlier accepted dependency scope.

Placement: put a short explicit flow example and all-annihilator proposition after the current lifetime theorem in Section25.19. Do not duplicate the136-line radial construction or the already existing general averaged identity. Replace the obsolete unrestricted P12 question by a precise account of the negative implication; preserve its complete original statement in the historical catalogue and separate the known conditional convergence theorem. Update the Introduction and history as needed for coherence, but retain the closed-nef, surface, Guan--Li and completeness questions in their proper scopes.

No novelty, autonomous solver, report-verdict premise, new external theorem, surface counterexample, weak continuation or unconditional local convergence is asserted. The original P12 source and reports remain immutable evidence. The broad listing comparison remains431; a separately retrieved first-jet preprint is only partially read and not adopted. Book publication remains the checked438 release pending manuscript integration of this result.

Package validation passes: 2195 archive entries, 2194 checksum payloads and 333 exact book sources matching the actual empty reconstruction at438. The current book remains the 1217-printed-page live438 release. No new author build or publication.
