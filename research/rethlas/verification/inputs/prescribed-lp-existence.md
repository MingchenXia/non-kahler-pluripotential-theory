Run_id: prescribed_lp_existence_01

Statement: Audit the complete proofs below of ALS prescribed ordinarytype Lp existence, positive exponent andnormalizedzeroexponent. theta>=0big,phi=Ptheta[phi] withP_epsilon theta(phi)genuine, f>=0Lp(dV),p>1,integralf>0. Claim uniqueu~phi forMAextu=exp(lambda u)f dV,lambda>0; andv~phi,c>0 forMAextv=c f dV,scalarunique NOTpotentialuniqueness. NoBMP/PVP. Every part of Perron weightedmassmaximization, commonbarriers, weakweightedlimit and residualaddition must be checked. SourcesALS26arxiv2511.02339v1Theorems5.4/5.7 forcomparisononly.

Accepted independentlyaudited inputs: bigboundedsemipositiveLp normalized/properexistence(big_lp_equations_01); modeluniformrelativeestimate andLp supersolution(relative_lp_barriers_01); singularstrictdom andexporder withv preceq u smallerbg(singular_domination_01); qpshnormalizedcompactness,expintegrab and elementarylem:normalized-exponential-lp (proofinbook); standardmeasurecompactness, RN,continuousdensityinL1finiteRadon. Newprerequisites commonbarriercompactness/continuity andfixedNPPexpconvergence are being audited common_barrier_compactness_01; weightedmeasureaddition being audited weighted_measure_addition_01 anditsboundedsubsolprereqbounded_subsolution_01. Readtheirreportstatuses,acceptconditionallyifpending, notneedreprovewholeprereqs. Checkscope exactly.

Part1 choosebaselinew,nu0, maximizingnu_uj≤mu; expcomparisonuj≤w; lowerh=psi+phi_epsilon MAYMOREsingular, verifyordercorrect; uniformsupbounds thenrelativeestimatecorrectnormalization;commonstrip/finitefixeddom giveL1/cap/rawweak;nu_jweakdominatedmu, boundedexpweightsL1mu implyweightedweakviafixedcontinuousL1muapprox (no illicitweaktest);nu0≤nu≤mu,weightcancellationoffpoles, massmax; residualr=f-g Lpnonzero, supersolutionv positiveweightedmass byzerodom, additionstrictlyenlargesmax. Part2 boundedh normalizedαf suppliesboundedHj uppercomparison forsingularuj (correctorientation/more-singular comparisoncondition);c_jupper;normalizedrelativeestimate,commonbarrierlimit; exp(vj/j)fTV->fviauniformLq;rawweakgivesMA=c f;c>0viazerodom;scalaruniquetranslationstrictdom. Readonlybookusualreport.

Proof:

\subsection{Existence for a positive exponent}

We have all the ingredients to prove the first assertion of \cref{thm:als-prescribed-lp}. The construction maximizes the mass of a weighted measure lying below the prescribed data. Domination controls the potentials; addition rules out a remaining deficit.

\begin{proof}[of \cref{thm:als-prescribed-lp}, part (1)]
Fix $\lambda>0$. By \cref{lem:relative-lp-supersolution}, choose $w\simeq\varphi$ such that
\[
 \nu_0:=e^{-\lambda w}\mathrm{MA}^{\mathrm{ext}}_\theta(w)
 \leq\mu=f\,dV.
\]
Consider all potentials $z\simeq\varphi$ for which
\[
 \nu_0\leq\nu_z:=e^{-\lambda z}
                   \mathrm{MA}^{\mathrm{ext}}_\theta(z)\leq\mu,
\]
and let $B$ be the supremum of their weighted masses $\nu_z(X)$. This is a nonempty family, since it contains $w$, and $B\leq\mu(X)<+\infty$. Choose $u_j$ in the family with $\nu_{u_j}(X)\to B$. Singular exponential order gives $u_j\leq w$.

We need a lower bound for their suprema. Put
$\varphi_\varepsilon=P_{\varepsilon\theta}(\varphi)\leq0$ and solve the bounded equation
\[
 ((1-\varepsilon)\theta+\ddc\psi)^n=e^{\lambda\psi}f\,dV
\]
using \cref{thm:big-bounded-exponential}. For $h=\psi+\varphi_\varepsilon$, positivity of the current splitting gives
\[
 e^{-\lambda h}\mathrm{MA}^{\mathrm{ext}}_\theta(h)
 \geq e^{-\lambda\varphi_\varepsilon}f\,dV
 \geq\mu\geq\nu_{u_j}.
\]
Here $h\preceq u_j$ because $h\preceq\varphi$ and $u_j\simeq\varphi$. Each $u_j$ admits a smaller-background envelope by bounded equivalence with $\varphi$. Singular exponential order therefore gives $u_j\geq h$. Consequently
\[
 \sup_Xh\leq M_j:=\sup_Xu_j\leq\sup_Xw.
\]
The lower bound is finite because $h$ is genuine.

Apply the relative uniform estimate to $v_j=u_j-M_j$. Their measures satisfy
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(v_j)
 =\mathrm{MA}^{\mathrm{ext}}_\theta(u_j)
 \leq e^{\lambda\sup_Xw}f\,dV.
\]
Thus $\varphi-C\leq v_j\leq\varphi$. The bounds for $M_j$ give a fixed bounded distance between all $u_j$ and $\varphi$. Extract an $L^1$ limit $u$. The common-barrier dominated continuity theorem gives convergence in capacity and
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u_j)
 \rightharpoonup\mathrm{MA}^{\mathrm{ext}}_\theta(u),
 \qquad u\simeq\varphi.
\]

Extract also $\nu_{u_j}\rightharpoonup\nu$. Since $\nu_0\leq\nu_{u_j}\leq\mu$, the limit satisfies the same inequalities. We claim that
\[
 e^{\lambda u_j}\nu_{u_j}\rightharpoonup e^{\lambda u}\nu.
\]
Indeed $e^{\lambda u_j}\to e^{\lambda u}$ in $L^1(\mu)$ by \cref{lem:fixed-npp-integrals}, and the measures $\nu_{u_j}$ are all at most $\mu$. This controls the error from changing the weight. For the fixed bounded weight $e^{\lambda u}$, approximate it in $L^1(\mu)$ by continuous functions; the domination of both $\nu_{u_j}$ and $\nu$ makes this approximation uniform in the integrals. Their weak convergence then gives the claim. The same argument works after multiplication by any continuous test function.

It follows that
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)=e^{\lambda u}\nu,
 \qquad e^{-\lambda u}\mathrm{MA}^{\mathrm{ext}}_\theta(u)=\nu,
 \qquad\nu(X)=B.
\]
The second identity is taken off the pole set, which has zero $\mu$-measure. Hence $u$ belongs to the maximizing family. Write $\nu=g\,dV$, with $0\leq g\leq f$.

Suppose $g\neq f$ in $L^1(dV)$. Apply the supersolution lemma to $f-g$ to find $v\simeq\varphi$ with
\[
 \nu_v:=e^{-\lambda v}\mathrm{MA}^{\mathrm{ext}}_\theta(v)
 \leq(f-g)\,dV.
\]
This measure is nonzero. More generally, a potential $v$ with a genuine smaller-background envelope cannot have zero Monge--Amp\`ere measure: applying strict domination with coefficient zero to $v$ and $v+1$ would give $v\geq v+1$. Thus $\nu_v(X)>0$.

The sum $\nu+\nu_v$ is finite, so \cref{thm:weighted-measure-addition} supplies $a\simeq\varphi$ with
\[
 e^{-\lambda a}\mathrm{MA}^{\mathrm{ext}}_\theta(a)=\nu+\nu_v.
\]
This measure still lies between $\nu_0$ and $\mu$, but has mass $B+\nu_v(X)>B$, a contradiction. Therefore $g=f$ and $u$ solves the required equation. Uniqueness is singular exponential order in the prescribed ordinary type.
\end{proof}

\subsection{The normalized equation}

\begin{proof}[of \cref{thm:als-prescribed-lp}, part (2)]
For each $j\geq1$, use part (1) to solve
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u_j)=e^{u_j/j}f\,dV,
 \qquad u_j\simeq\varphi.
\]
Write $M_j=\sup_Xu_j$, $v_j=u_j-M_j$ and $c_j=e^{M_j/j}$. Choose a bounded normalized solution $h$ and $\alpha>0$ of
$\mathrm{MA}_\theta(h)=\alpha f\,dV$, supplied by \cref{thm:big-bounded-normalized}. For
$H_j=h+\|h\|_\infty+j\log\alpha$, we have
\[
 e^{-H_j/j}\mathrm{MA}_\theta(H_j)
 =e^{-(h+\|h\|_\infty)/j}f\,dV
 \leq f\,dV
 =e^{-u_j/j}\mathrm{MA}^{\mathrm{ext}}_\theta(u_j).
\]
The bounded $H_j$ admits a smaller-background envelope, and $u_j\preceq H_j$. Exponential order gives $u_j\leq H_j$. In particular
\[
 0<c_j\leq\alpha\exp(2\|h\|_\infty/j).
\]

Since $\sup_Xv_j=0$ and
$\mathrm{MA}^{\mathrm{ext}}_\theta(v_j)=c_je^{v_j/j}f\,dV\leq C f\,dV$,
the relative uniform estimate gives $\varphi-C'\leq v_j\leq\varphi$. Extract $v_j\to v$ in $L^1(X)$ and $c_j\to c\geq0$. The common-barrier dominated continuity theorem yields capacity convergence, $v\simeq\varphi$, and raw weak convergence. Meanwhile \cref{lem:normalized-exponential-lp} gives
\[
 \int_X|e^{v_j/j}-1|f\,dV\longrightarrow0.
\]
Thus the right sides converge in total variation to $cf\,dV$, and
$\mathrm{MA}^{\mathrm{ext}}_\theta(v)=cf\,dV$.
If $c=0$, strict domination applied to $v,v+1$ would again be impossible; hence $c>0$.

For uniqueness of the scalar, suppose $a,b\simeq\varphi$ solve the normalized equation with constants $c_a<c_b$. For every real $t$,
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(a)
 =\frac{c_a}{c_b}\mathrm{MA}^{\mathrm{ext}}_\theta(b+t).
\]
Strict domination gives $a\geq b+t$. At a point where both are finite this is impossible as $t\to+\infty$. Interchanging the two constants proves uniqueness. This argument does not assert uniqueness of the potential after the constants have been shown equal.
\end{proof}

The two parts establish the prescribed-type $L^p$ theory without bounded mass and without a uniform lower mass hypothesis. The common barriers are produced by the relative estimate. In the normalized limit, finiteness and positivity of the mass follow from the equation and singular domination; they are not assumptions on all potentials on $X$.
