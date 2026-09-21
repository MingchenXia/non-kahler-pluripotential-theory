Run_id: geometry_problem_connections_repair_01

Statement: Audit the literature claims, definitions, deductions, and logical boundaries in the new research-program section below. The open questions/conjectures are NOT assertions to prove. Verify that the manuscript correctly identifies what is already known, does not misstate source hypotheses or identify different volumes, and that every claimed consequence follows. This responds to the user's explicit request to connect the book with open problems in non-Kahler geometry. No novelty certification.

Accepted manuscript results: Gauduchon root volume lambda_mu and V=lambda^n, smoothMA duality/firstvariation, nefcontinuity, densitycomparison, bigness=>positiveV, Gaudthreshold kappa_h and collapse criterion, determinant Lq estimates and exact endpoint sup=v_minus^(-1/n), Hopf3v_minus6/v_plusinfinite; all are in book/author with corresponding passedprioraudits. smooth_cone_flow_01 has now passed; its fullpersistedstatementchecks/referencechecks and finalJSON were read. This supplies currentlifetimeformula and nefannihilatordeterminant. big_continuous_contact_01 and local_homogeneous_dirichlet_01 have BOTHpassed and are included; suppliesonlycontinuous-obstaclebigcontact/continuityoffanalyticbarrier. Do not assume generalunboundedcontact, generalmovingNPPproof, nefpositiveV=>big, or generalparabolicestimates.

The NUMA counterexample is CONDITIONALLY accepted here with exactly its TheoremA: separately auditing as degenerate_nonuniqueness_01. That audit mustpassbeforethispartis included. SourceuserprovidedFULL6pagePDF /Users/mingchen/Non-Kahler/research/sources/NUMA-Xia.pdf, noauthordateprinted. Check all implicationsinthissection; cannot refutefinitecontinuouslogdensityadjointconjecturewithfzeroband.

New exact primary references to verify arxivfirst thenprimaryweb, use localprimaryPDF/text as fallback where directwebretrievalfails:
1 DP04 /Users/mingchen/Non-Kahler/research/sources/DP04.pdf/.txt arxivmath/0105176v2 Sept24,2001. Theorem0.6closedKahlercurrent iffclassC,Conjecture0.7closedneftoppositive=>classC (publishednumbers0.7,0.8). Do not substitute arbitrarynonclosedbigbackground. Verify equivalence toalpha bigusingstandardclassCnef criterion.
2 GL22sourcepdf/txt arxiv2106.04272v2; exactTheorems4.9and4.12: underclosednefpositiveintersectionconditions big iffBMP. NOTproofBMP universal.
3 BGL25-published.pdf/.txt TheoremC classC iffBMP+positiveUPPERclassvolclosedBCclass. NotV_mu. Existingbooksourceverifiedbutcheckusedclaimexact.
4 DangNull26.pdf/.txt arxiv2404.01126v2 June17,2026. Theorem1.1 hasarbitraryXthetaNEFANDBIG nonclosed,noBMP. TheoremA addsHX BMPX/PVPallpositivedimclosedsubmanifoldsandhatv_minus(theta)>0. TheoremC finiteflowtimeandpositivehatv_minuslimit,either n2arbitraryomega0 or n>=3GuanLi ddcomega0=0anddomega0dc...=0. Do notreplacehatvminusbyV_mu. IntrinsicbignessonanalyticV versusresolutionneedscheckeddefinition.
5 Chiose14.pdf/.txt primaryauthor https://www.imar.ro/~cjoita/MC-SCV/Chiose-closedobstruction.pdf Theorem0.2classC+pluriclosed=>Kahler. PublishedProcAMS142(2014)3561-3568.
6 FV26.pdf/.txt arxiv2606.03176v1 June2,2026,Conj1.1balancedANDpluriclosed(possiblydifferentmetrics)=>Kahler, Conj1.2balanced+c1=0pluriclosedflow longtimeandsmoothKahlerlimit, invariantsettingtraceillustration. Onlyconjecture/context, noimportunprovedflowclaim.
7 Tosatti26.pdf/.txt arxiv2608.30153v1 Aug31,2026,Theorem1.1closednefKahlerMorseinequality,Cor1.2. RecentPREPRINTresult, notproofhere andnotunrestrictedHermitian.
All archivedprimarysourcefilesin /Users/mingchen/Non-Kahler/research/sources, manifesthashes. Checksourceversionnumbersandexactmathematicaldefinitions; researchpapersareevidenceonly.

Proof and program text:

\section{Connections with non-K\"ahler geometry}
\label{sec:non-kahler-geometric-problems}

The general theory should explain geometric obstructions as well as solve equations. We describe six connections. In each case the distinction between a closed Bott--Chern class and an arbitrary smooth background is essential. The literature statements below are recorded with their hypotheses; the subsequent questions ask what the constructions of this book could add.

\subsection{Nef classes, bigness and the Fujiki class}

A compact complex manifold belongs to the Fujiki class $\mathcal C$ if it is bimeromorphic to a compact K\"ahler manifold. The classical characterization by the existence of a closed K\"ahler current is due to Demailly--P\u aun \cite[Theorem 0.6 in the arXiv version]{DP04}. Their transcendental Grauert--Riemenschneider conjecture asks whether a closed nef real $(1,1)$-class $\alpha$ with
\[
 \int_X\alpha^n>0
\]
is big on an arbitrary compact complex manifold. Equivalently in this situation, the proposed conclusion is $X\in\mathcal C$; compare \cite[Conjecture 0.7 in the arXiv version]{DP04}.

The bounded mass property is closely tied to this problem. Under exactly the preceding nefness and positive top-intersection hypotheses, Guedj--Lu prove
\[
 \alpha\text{ is big}\quad\Longleftrightarrow\quad v_+(h)<\infty
\]
for a Hermitian metric $h$ \cite[Theorem 4.9]{GL22}. Boucksom--Guedj--Lu also characterize $\mathcal C$ by bounded mass together with positivity of their upper class volume for some closed Bott--Chern class \cite[Theorem C]{BGL25}. That upper volume is not the invariant $\mathcal V_\mu$ defined here.

The failure of bounded mass on the Hopf threefold does not refute the Demailly--P\u aun conjecture. A counterexample would also need a closed nef class with positive top self-intersection. Conversely, a proof of the conjecture cannot impose bounded mass as an unexplained general fact. The Hermitian framework must account for why that property follows in the particular geometry forced by such a class.

The volume of this book separates two possible steps:
\begin{equation}\label{eq:dp-two-bridges}
 \int_X\alpha^n>0
 \quad\stackrel{?}{\Longrightarrow}\quad
 \mathcal V_\mu(\alpha)>0
 \quad\stackrel{?}{\Longrightarrow}\quad
 \alpha\text{ is big}.
\end{equation}
Neither arrow is established here in the unrestricted compact complex setting. The second is the closed special case of \cref{conj:nef-gaud-volume-big}. On a compact K\"ahler manifold both follow from the usual nef volume formula and the classical nef-and-big criterion. Without closedness, positivity of $\mathcal V_\mu$ cannot characterize $\mathcal C$: every Hermitian metric $h$ already satisfies $\mathcal V_\mu(h)>0$, on every compact complex manifold.

\begin{problem}\label{qu:closed-nef-gaud-bridge}
Let $\alpha$ be closed and nef with $\int_X\alpha^n>0$. Prove a positive lower bound for $\lambda_\mu(\alpha)$, and rule out the collapse in \cref{prop:gaud-positive-volume-collapse} for a sequence minimizing the bigness threshold of $\alpha$.
\end{problem}

This is a proposed route to the geometric conjecture, not a claimed weaker substitute already known to suffice automatically. The relevant test metrics can be normalized by $\int_Xh\wedge\gamma^{n-1}=1$. A positive lower bound for $D_\mu(\gamma)$ along one threshold-minimizing sequence would finish the second step. The Gauduchon equation can change the volume density while retaining an Aeppli class. Since $\alpha$ is closed, it also retains the numerator paired against $\alpha$. The missing estimate is control of the trace normalization and determinant denominator after that change. Merely prescribing a volume density does not give this estimate.

\subsection{Positive lower volume as an endpoint estimate}

The universal positive-volume question asks whether $v_-(h)>0$ for every Hermitian metric on every compact complex manifold. This is separate from bounded mass. The Hopf threefold has $v_-(h)=6$ and $v_+(h)=\infty$ in the normalization of \cref{chap:hopf}. The sources \cite{GL22,BGL25,XZ26} do not settle the unrestricted positive lower-volume question.

For $n\geq2$, the determinant measures give an exact analytic formulation. Fix a smooth positive probability measure $dV$, and write
\[
 \Gamma_0(T)=k_T\,dV,\qquad T\in\mathscr G_h.
\]
By \cref{thm:gaud-determinant-endpoint},
\begin{equation}\label{eq:pvp-endpoint-geometric}
 v_-(h)>0
 \quad\Longleftrightarrow\quad
 \sup_{T\in\mathscr G_h}
       \|k_T\|_{L^{n/(n-1)}(dV)}<\infty.
\end{equation}
The exact supremum is $v_-(h)^{-1/n}$, including the value $+\infty$. Uniform estimates for every smaller exponent $1<q<n/(n-1)$ have already been proved without either volume property.

\begin{problem}\label{qu:universal-gaud-endpoint}
Does positivity and $\ddc T=0$, together with $\int_Xh\wedge T=1$, force the endpoint estimate in \eqref{eq:pvp-endpoint-geometric} on every compact complex manifold?
\end{problem}

The linear differential constraint is part of the question. Arbitrary positive matrix-valued measures of normalized trace need not obey such an estimate. Subcritical compactness also does not imply the endpoint bound. A useful approach would identify an additional estimate coming from $\ddc T=0$ that excludes concentration of the determinant densities at the critical exponent. Conversely, a sequence of normalized Gauduchon currents with unbounded endpoint norms would disprove universal positive lower volume. It would not be enough to construct potentials with unbounded upper Monge--Amp\`ere mass: those already exist in the Hopf example, where the endpoint bound holds.

An affirmative answer would remove the positive lower-volume hypothesis from equation theorems that require only that metric hypothesis. It would not remove a separate bounded mass assumption or prove every singular-background statement. Each equation would still have to retain its geometric, singularity and measure hypotheses.

\subsection{Null loci and the singularities of the Chern--Ricci flow}

For a big smooth background $\theta$, its non-Hermitian locus $E_{\mathrm{nH}}(\theta)$ is the smallest analytic pole set of strict currents with analytic singularities in that background. For nef and big $\theta$, define
\[
 \operatorname{Null}(\theta)
 =\bigcup_{\substack{V\subset X\text{ irreducible analytic}\\
                     \dim V>0,\ \theta|_V\text{ not big}}}V.
\]
Bigness on a singular subvariety uses its intrinsic analytic definition. Dang proves $E_{\mathrm{nH}}(\theta)=\operatorname{Null}(\theta)$ for arbitrary compact complex $X$ and nef, big, possibly nonclosed $\theta$ \cite[Theorem 1.1]{DangNull26}. This qualitative identification is therefore a known theorem. Detecting bigness and this locus from numerical data is a further issue: the same paper's Theorem A uses bounded mass on $X$ and positive lower volume on its positive-dimensional submanifolds.

Theorem C of \cite{DangNull26} identifies finite-time Chern--Ricci singularities with the null locus under positive limiting lower volume, for arbitrary initial metrics in dimension two, and for Guan--Li initial metrics in higher dimensions. Here Guan--Li means $\ddc\omega_0=0$ and $d\omega_0\wedge d^c\omega_0=0$. These hypotheses must not be silently replaced by positivity of $\mathcal V_\mu$.

The current calculation in \cref{cor:chern-ricci-current-lifetime} applies without those extra hypotheses. At a finite maximal time $\tau$, the background $\theta_\tau=\omega_0-\tau\operatorname{Ric}(\omega_0)$ is nef. Its normalized annihilating currents satisfy
\[
 \int_X\theta_\tau\wedge T=0.
\]
If $\mathcal V_\mu(\theta_\tau)>0$, their determinant-weighted measures vanish by \cref{prop:nef-annihilator-determinant}. This is a precise degeneracy statement, but it does not imply that their traces are concentrated on analytic sets. A smooth positive semidefinite matrix of deficient rank can be defined on an open set.

\begin{problem}\label{qu:chern-ricci-gaud-singularities}
Suppose a Chern--Ricci flow has finite maximal time $\tau$ and $\mathcal V_\mu(\theta_\tau)>0$. Can one prove that $\theta_\tau$ is big and that the flow converges smoothly to a positive metric locally on $X\setminus E_{\mathrm{nH}}(\theta_\tau)$, without a bounded mass hypothesis? How do the annihilating Gauduchon currents describe the resulting degeneracy?
\end{problem}

The first assertion is a case of the volume-to-bigness question. If it were established, the qualitative null-locus theorem would identify the exceptional analytic set. Smooth convergence of the flow would still require uniform local parabolic estimates. The local envelope continuity and homogeneous replacement arguments of \cref{thm:big-continuous-envelope-contact} supply an elliptic foundation away from a strict barrier's poles; they are not those parabolic estimates. This divides the proposed approach into separate tasks that can be tested individually.

\subsection{Degenerate densities and uniqueness}

The counterexample of \cite{NUMA}, reconstructed in \cref{thm:degenerate-hermitian-nonuniqueness}, shows that a smooth nonnegative density can have two distinct smooth normalized solutions even on $\mathbb P^3$. Its background is strictly Hermitian, hence its non-Hermitian locus is empty. The degeneration causing nonuniqueness belongs to the density and the solution forms; it is not detected by the background's null locus. The example also has bounded mass.

This places a necessary restriction on any geometric use of the equation. A construction that assigns a canonical potential to arbitrary nonnegative data must specify a selection procedure and prove that it is well defined. Existence in the ordinary minimal singularity type does not provide such a selection. The unique scalar, and the corresponding variational volume for strictly positive data, remain meaningful without uniqueness of every potential.

\begin{problem}\label{qu:density-zero-set-uniqueness}
Let $\omega$ be Hermitian and $f\geq0$ smooth and nonzero. If $\{f=0\}$ has empty interior, are two bounded normalized solutions of $\mathrm{MA}_\omega(u)=cf\,dV$ necessarily equal? Separately, for densities allowing nonuniqueness, do normalized solutions of $\mathrm{MA}_\omega(u_\lambda)=e^{\lambda u_\lambda}f\,dV$ select a unique limit as $\lambda\downarrow0$?
\end{problem}

The first question sharpens the density condition left open in \cite{NUMA}; the bounded solution class is specified here. The second asks for a canonical limit, and does not follow from uniqueness of the positive-exponent equation at each fixed parameter. A selection could exist even when the limiting equation has several solutions. Also, this counterexample does not refute \cref{conj:continuous-gaud-adjoint}: that conjecture uses a finite continuous logarithmic density $F$, for which $e^F$ is strictly positive. In the counterexample, $\log f=-\infty$ on an open set.

\subsection{Balanced and pluriclosed metrics}

A Hermitian metric $\beta$ is balanced if $d\beta^{n-1}=0$, while a Hermitian metric $\omega$ is pluriclosed if $\ddc\omega=0$. The Fino--Vezzoni conjecture asks whether a compact complex manifold admitting both types of metrics is K\"ahler; the two metrics can be different. See \cite[Conjecture 1.1]{FV26} for the statement and recent context. A single metric satisfying both conditions is already K\"ahler, which does not resolve the question with two metrics.

Chiose proves that a compact manifold in $\mathcal C$ admitting a pluriclosed metric is K\"ahler \cite[Theorem 0.2 in the author manuscript]{Chiose14}. Consequently, in the balanced--pluriclosed setting, it would suffice to construct a closed big $(1,1)$-current and apply the characterization of $\mathcal C$. This route emphasizes a geometric existence problem which is absent when one only works with an arbitrary Hermitian background.

There is an elementary obstruction to using the scalar equation alone. For every distributional potential $u$,
\[
 d(\omega+\ddc u)=d\omega.
\]
Thus if the starting pluriclosed metric is nonclosed, no potential in its fixed background makes it K\"ahler. The finite-volume equation, including its smooth solution, does not change this differential datum. Similarly, a conformal Gauduchon representative need not be balanced. Positivity and a scalar normalization cannot be used to replace either missing closedness condition.

The balanced form $\beta^{n-1}$ nevertheless supplies more than a Gauduchon test: it pairs trivially with every exact real two-form by Stokes. It therefore interacts with flows whose variation has an exact component. Fino--Vezzoni propose long-time existence and convergence to a K\"ahler metric for the pluriclosed flow when a balanced metric exists and $c_1(X)=0$ \cite[Conjecture 1.2]{FV26}. Their invariant examples illustrate the use of a conserved balanced trace. In general that integral is not a pointwise metric bound.

\begin{problem}\label{qu:balanced-pluriclosed-program}
Use the coexistence of a balanced metric and a pluriclosed metric to construct closed positive data, or to control a geometric flow that can change the torsion. Determine what estimate beyond the finite balanced trace prevents metric degeneration. Can determinant estimates for Gauduchon currents contribute to that estimate?
\end{problem}

This asks for an interaction with the scalar theory, not an implication already proved by its equation. One can first study families for which the balanced trace and the determinant density are explicitly controlled. The passage from an integral trace bound to local ellipticity is then a concrete analytic target. No such passage for arbitrary families is asserted here.

\subsection{Morse inequalities and the choice of volume}

The closed K\"ahler theory provides a demanding comparison. Tosatti's recent preprint establishes the transcendental Morse inequality
\[
 \operatorname{Vol}(\alpha-\beta)
 \geq\int_X\alpha^n-n\int_X\alpha^{n-1}\wedge\beta
\]
for closed nef classes on compact K\"ahler manifolds, together with the resulting volume differentiability and cone-duality consequences \cite[Theorem 1.1 and Corollary 1.2]{Tosatti26}. We record it as a recent literature result; its proof is not reconstructed here. The unrestricted non-K\"ahler extension remains a different problem. Guedj--Lu's qualitative criterion under bounded mass is \cite[Theorem 4.12]{GL22}.

For nonclosed backgrounds, the displayed intersection expression is not generally invariant under changing representatives. Also, the upper class volume and $\mathcal V_\mu$ have different definitions and different possible finiteness behavior. A Hermitian analogue must first specify which invariant it estimates.

The first-variation formula gives a finite quantity to investigate. Suppose $\theta_s=\theta-s\eta$ has a smooth positive representative for $0\leq s\leq t$, and let $\gamma_s$ be a minimizing Gauduchon metric for its smooth equation. By \cref{prop:gaud-volume-first-variation} and the fundamental theorem of calculus,
\begin{equation}\label{eq:gaud-volume-subtraction-cost}
 \lambda_\mu(\theta-t\eta)
 =\lambda_\mu(\theta)
   -\int_0^t
       \frac{\int_X\eta\wedge\gamma_s^{n-1}}
            {D_\mu(\gamma_s)}\,ds.
\end{equation}
The quotient is unchanged by rescaling the minimizer. This identity is valid on the stated positive segment and uses no upper Monge--Amp\`ere mass bound. A uniform upper bound on its integrand gives a lower bound for the remaining root volume. Proving a useful bound near a degenerate endpoint is an additional problem; concavity alone provides the tangent upper bound, not the lower bound needed here.

\begin{problem}\label{qu:hermitian-morse-program}
Find geometric hypotheses controlling the cost in \eqref{eq:gaud-volume-subtraction-cost} up to a nef endpoint, and determine whether the resulting positive root volume forces bigness there. For closed backgrounds, compare the resulting estimate with classical Morse inequalities. For nonclosed backgrounds, retain the differential data and state explicitly any dependence on $\mu$.
\end{problem}

The singularity and divisorial constructions in the book become relevant at this stage: they record how much positivity can be spent on imposed poles, while the residual Gauduchon volume stays finite. They do not yet give the moving intersection product or the birational volume formula of the closed theory. Recovering such geometric information is a further objective, with the finite-divisor and Hopf calculations serving as explicit tests.


Follow AGENTS.md strictly. Initialize memory; sequentially check all literature statements and deductions, with every gap/error persisted. Questions are proposed targets, not theorems. Write a full readable verification_report.md and finalJSONviaMCP at results/geometry_problem_connections_repair_01/verification.json. Correct iffzerogaps/errorsrelativetostatedacceptedinputs. Do noteditbook.

This is a targeted repair of geometry_problem_connections_01. Read the previous persisted statement/reference checks and report. Its sole defect was replacing almost analytic singularities by analytic singularities in Dang's non-Hermitian locus. The opening paragraph now gives the exact intersection definition, attainment theorem, and Definition2.8 conditions. Independently check this repair against the archived DangNull26 primary text and all consequences. The rest of the section is unchanged; previous positive checks may be retained after verifying unchanged text. The conditional NUMA prerequisite has now PASSED degenerate_nonuniqueness_01. Do not edit book or prior results. Persist a full readable report and final JSON for this new run.

Proof:

\section{Connections with non-K\"ahler geometry}
\label{sec:non-kahler-geometric-problems}

The general theory should explain geometric obstructions as well as solve equations. We describe six connections. In each case the distinction between a closed Bott--Chern class and an arbitrary smooth background is essential. The literature statements below are recorded with their hypotheses; the subsequent questions ask what the constructions of this book could add.

\subsection{Nef classes, bigness and the Fujiki class}

A compact complex manifold belongs to the Fujiki class $\mathcal C$ if it is bimeromorphic to a compact K\"ahler manifold. The classical characterization by the existence of a closed K\"ahler current is due to Demailly--P\u aun \cite[Theorem 0.6 in the arXiv version]{DP04}. Their transcendental Grauert--Riemenschneider conjecture asks whether a closed nef real $(1,1)$-class $\alpha$ with
\[
 \int_X\alpha^n>0
\]
is big on an arbitrary compact complex manifold. Equivalently in this situation, the proposed conclusion is $X\in\mathcal C$; compare \cite[Conjecture 0.7 in the arXiv version]{DP04}.

The bounded mass property is closely tied to this problem. Under exactly the preceding nefness and positive top-intersection hypotheses, Guedj--Lu prove
\[
 \alpha\text{ is big}\quad\Longleftrightarrow\quad v_+(h)<\infty
\]
for a Hermitian metric $h$ \cite[Theorem 4.9]{GL22}. Boucksom--Guedj--Lu also characterize $\mathcal C$ by bounded mass together with positivity of their upper class volume for some closed Bott--Chern class \cite[Theorem C]{BGL25}. That upper volume is not the invariant $\mathcal V_\mu$ defined here.

The failure of bounded mass on the Hopf threefold does not refute the Demailly--P\u aun conjecture. A counterexample would also need a closed nef class with positive top self-intersection. Conversely, a proof of the conjecture cannot impose bounded mass as an unexplained general fact. The Hermitian framework must account for why that property follows in the particular geometry forced by such a class.

The volume of this book separates two possible steps:
\begin{equation}\label{eq:dp-two-bridges}
 \int_X\alpha^n>0
 \quad\stackrel{?}{\Longrightarrow}\quad
 \mathcal V_\mu(\alpha)>0
 \quad\stackrel{?}{\Longrightarrow}\quad
 \alpha\text{ is big}.
\end{equation}
Neither arrow is established here in the unrestricted compact complex setting. The second is the closed special case of \cref{conj:nef-gaud-volume-big}. On a compact K\"ahler manifold both follow from the usual nef volume formula and the classical nef-and-big criterion. Without closedness, positivity of $\mathcal V_\mu$ cannot characterize $\mathcal C$: every Hermitian metric $h$ already satisfies $\mathcal V_\mu(h)>0$, on every compact complex manifold.

\begin{problem}\label{qu:closed-nef-gaud-bridge}
Let $\alpha$ be closed and nef with $\int_X\alpha^n>0$. Prove a positive lower bound for $\lambda_\mu(\alpha)$, and rule out the collapse in \cref{prop:gaud-positive-volume-collapse} for a sequence minimizing the bigness threshold of $\alpha$.
\end{problem}

This is a proposed route to the geometric conjecture, not a claimed weaker substitute already known to suffice automatically. The relevant test metrics can be normalized by $\int_Xh\wedge\gamma^{n-1}=1$. A positive lower bound for $D_\mu(\gamma)$ along one threshold-minimizing sequence would finish the second step. The Gauduchon equation can change the volume density while retaining an Aeppli class. Since $\alpha$ is closed, it also retains the numerator paired against $\alpha$. The missing estimate is control of the trace normalization and determinant denominator after that change. Merely prescribing a volume density does not give this estimate.

\subsection{Positive lower volume as an endpoint estimate}

The universal positive-volume question asks whether $v_-(h)>0$ for every Hermitian metric on every compact complex manifold. This is separate from bounded mass. The Hopf threefold has $v_-(h)=6$ and $v_+(h)=\infty$ in the normalization of \cref{chap:hopf}. The sources \cite{GL22,BGL25,XZ26} do not settle the unrestricted positive lower-volume question.

For $n\geq2$, the determinant measures give an exact analytic formulation. Fix a smooth positive probability measure $dV$, and write
\[
 \Gamma_0(T)=k_T\,dV,\qquad T\in\mathscr G_h.
\]
By \cref{thm:gaud-determinant-endpoint},
\begin{equation}\label{eq:pvp-endpoint-geometric}
 v_-(h)>0
 \quad\Longleftrightarrow\quad
 \sup_{T\in\mathscr G_h}
       \|k_T\|_{L^{n/(n-1)}(dV)}<\infty.
\end{equation}
The exact supremum is $v_-(h)^{-1/n}$, including the value $+\infty$. Uniform estimates for every smaller exponent $1<q<n/(n-1)$ have already been proved without either volume property.

\begin{problem}\label{qu:universal-gaud-endpoint}
Does positivity and $\ddc T=0$, together with $\int_Xh\wedge T=1$, force the endpoint estimate in \eqref{eq:pvp-endpoint-geometric} on every compact complex manifold?
\end{problem}

The linear differential constraint is part of the question. Arbitrary positive matrix-valued measures of normalized trace need not obey such an estimate. Subcritical compactness also does not imply the endpoint bound. A useful approach would identify an additional estimate coming from $\ddc T=0$ that excludes concentration of the determinant densities at the critical exponent. Conversely, a sequence of normalized Gauduchon currents with unbounded endpoint norms would disprove universal positive lower volume. It would not be enough to construct potentials with unbounded upper Monge--Amp\`ere mass: those already exist in the Hopf example, where the endpoint bound holds.

An affirmative answer would remove the positive lower-volume hypothesis from equation theorems that require only that metric hypothesis. It would not remove a separate bounded mass assumption or prove every singular-background statement. Each equation would still have to retain its geometric, singularity and measure hypotheses.

\subsection{Null loci and the singularities of the Chern--Ricci flow}

For a big smooth background $\theta$, Dang defines its non-Hermitian locus $E_{\mathrm{nH}}(\theta)$ as the intersection of the singular sets of all strict currents in that background with \emph{almost analytic singularities}; this intersection is itself attained by such a current \cite[Definition 2.12 and Theorem 2.14]{DangNull26}. In the source's terminology the potential is locally a positive multiple of the logarithm of an ideal norm, up to a bounded remainder, and on a suitable log resolution its remainder after subtracting the divisorial logarithms is smooth \cite[Definition 2.8]{DangNull26}. We retain this exact singularity condition. For nef and big $\theta$, define
\[
 \operatorname{Null}(\theta)
 =\bigcup_{\substack{V\subset X\text{ irreducible analytic}\\
                     \dim V>0,\ \theta|_V\text{ not big}}}V.
\]
Bigness on a singular subvariety uses its intrinsic analytic definition. Dang proves $E_{\mathrm{nH}}(\theta)=\operatorname{Null}(\theta)$ for arbitrary compact complex $X$ and nef, big, possibly nonclosed $\theta$ \cite[Theorem 1.1]{DangNull26}. This qualitative identification is therefore a known theorem. Detecting bigness and this locus from numerical data is a further issue: the same paper's Theorem A uses bounded mass on $X$ and positive lower volume on its positive-dimensional submanifolds.

Theorem C of \cite{DangNull26} identifies finite-time Chern--Ricci singularities with the null locus under positive limiting lower volume, for arbitrary initial metrics in dimension two, and for Guan--Li initial metrics in higher dimensions. Here Guan--Li means $\ddc\omega_0=0$ and $d\omega_0\wedge d^c\omega_0=0$. These hypotheses must not be silently replaced by positivity of $\mathcal V_\mu$.

The current calculation in \cref{cor:chern-ricci-current-lifetime} applies without those extra hypotheses. At a finite maximal time $\tau$, the background $\theta_\tau=\omega_0-\tau\operatorname{Ric}(\omega_0)$ is nef. Its normalized annihilating currents satisfy
\[
 \int_X\theta_\tau\wedge T=0.
\]
If $\mathcal V_\mu(\theta_\tau)>0$, their determinant-weighted measures vanish by \cref{prop:nef-annihilator-determinant}. This is a precise degeneracy statement, but it does not imply that their traces are concentrated on analytic sets. A smooth positive semidefinite matrix of deficient rank can be defined on an open set.

\begin{problem}\label{qu:chern-ricci-gaud-singularities}
Suppose a Chern--Ricci flow has finite maximal time $\tau$ and $\mathcal V_\mu(\theta_\tau)>0$. Can one prove that $\theta_\tau$ is big and that the flow converges smoothly to a positive metric locally on $X\setminus E_{\mathrm{nH}}(\theta_\tau)$, without a bounded mass hypothesis? How do the annihilating Gauduchon currents describe the resulting degeneracy?
\end{problem}

The first assertion is a case of the volume-to-bigness question. If it were established, the qualitative null-locus theorem would identify the exceptional analytic set. Smooth convergence of the flow would still require uniform local parabolic estimates. The local envelope continuity and homogeneous replacement arguments of \cref{thm:big-continuous-envelope-contact} supply an elliptic foundation away from a strict barrier's poles; they are not those parabolic estimates. This divides the proposed approach into separate tasks that can be tested individually.

\subsection{Degenerate densities and uniqueness}

The counterexample of \cite{NUMA}, reconstructed in \cref{thm:degenerate-hermitian-nonuniqueness}, shows that a smooth nonnegative density can have two distinct smooth normalized solutions even on $\mathbb P^3$. Its background is strictly Hermitian, hence its non-Hermitian locus is empty. The degeneration causing nonuniqueness belongs to the density and the solution forms; it is not detected by the background's null locus. The example also has bounded mass.

This places a necessary restriction on any geometric use of the equation. A construction that assigns a canonical potential to arbitrary nonnegative data must specify a selection procedure and prove that it is well defined. Existence in the ordinary minimal singularity type does not provide such a selection. The unique scalar, and the corresponding variational volume for strictly positive data, remain meaningful without uniqueness of every potential.

\begin{problem}\label{qu:density-zero-set-uniqueness}
Let $\omega$ be Hermitian and $f\geq0$ smooth and nonzero. If $\{f=0\}$ has empty interior, are two bounded normalized solutions of $\mathrm{MA}_\omega(u)=cf\,dV$ necessarily equal? Separately, for densities allowing nonuniqueness, do normalized solutions of $\mathrm{MA}_\omega(u_\lambda)=e^{\lambda u_\lambda}f\,dV$ select a unique limit as $\lambda\downarrow0$?
\end{problem}

The first question sharpens the density condition left open in \cite{NUMA}; the bounded solution class is specified here. The second asks for a canonical limit, and does not follow from uniqueness of the positive-exponent equation at each fixed parameter. A selection could exist even when the limiting equation has several solutions. Also, this counterexample does not refute \cref{conj:continuous-gaud-adjoint}: that conjecture uses a finite continuous logarithmic density $F$, for which $e^F$ is strictly positive. In the counterexample, $\log f=-\infty$ on an open set.

\subsection{Balanced and pluriclosed metrics}

A Hermitian metric $\beta$ is balanced if $d\beta^{n-1}=0$, while a Hermitian metric $\omega$ is pluriclosed if $\ddc\omega=0$. The Fino--Vezzoni conjecture asks whether a compact complex manifold admitting both types of metrics is K\"ahler; the two metrics can be different. See \cite[Conjecture 1.1]{FV26} for the statement and recent context. A single metric satisfying both conditions is already K\"ahler, which does not resolve the question with two metrics.

Chiose proves that a compact manifold in $\mathcal C$ admitting a pluriclosed metric is K\"ahler \cite[Theorem 0.2 in the author manuscript]{Chiose14}. Consequently, in the balanced--pluriclosed setting, it would suffice to construct a closed big $(1,1)$-current and apply the characterization of $\mathcal C$. This route emphasizes a geometric existence problem which is absent when one only works with an arbitrary Hermitian background.

There is an elementary obstruction to using the scalar equation alone. For every distributional potential $u$,
\[
 d(\omega+\ddc u)=d\omega.
\]
Thus if the starting pluriclosed metric is nonclosed, no potential in its fixed background makes it K\"ahler. The finite-volume equation, including its smooth solution, does not change this differential datum. Similarly, a conformal Gauduchon representative need not be balanced. Positivity and a scalar normalization cannot be used to replace either missing closedness condition.

The balanced form $\beta^{n-1}$ nevertheless supplies more than a Gauduchon test: it pairs trivially with every exact real two-form by Stokes. It therefore interacts with flows whose variation has an exact component. Fino--Vezzoni propose long-time existence and convergence to a K\"ahler metric for the pluriclosed flow when a balanced metric exists and $c_1(X)=0$ \cite[Conjecture 1.2]{FV26}. Their invariant examples illustrate the use of a conserved balanced trace. In general that integral is not a pointwise metric bound.

\begin{problem}\label{qu:balanced-pluriclosed-program}
Use the coexistence of a balanced metric and a pluriclosed metric to construct closed positive data, or to control a geometric flow that can change the torsion. Determine what estimate beyond the finite balanced trace prevents metric degeneration. Can determinant estimates for Gauduchon currents contribute to that estimate?
\end{problem}

This asks for an interaction with the scalar theory, not an implication already proved by its equation. One can first study families for which the balanced trace and the determinant density are explicitly controlled. The passage from an integral trace bound to local ellipticity is then a concrete analytic target. No such passage for arbitrary families is asserted here.

\subsection{Morse inequalities and the choice of volume}

The closed K\"ahler theory provides a demanding comparison. Tosatti's recent preprint establishes the transcendental Morse inequality
\[
 \operatorname{Vol}(\alpha-\beta)
 \geq\int_X\alpha^n-n\int_X\alpha^{n-1}\wedge\beta
\]
for closed nef classes on compact K\"ahler manifolds, together with the resulting volume differentiability and cone-duality consequences \cite[Theorem 1.1 and Corollary 1.2]{Tosatti26}. We record it as a recent literature result; its proof is not reconstructed here. The unrestricted non-K\"ahler extension remains a different problem. Guedj--Lu's qualitative criterion under bounded mass is \cite[Theorem 4.12]{GL22}.

For nonclosed backgrounds, the displayed intersection expression is not generally invariant under changing representatives. Also, the upper class volume and $\mathcal V_\mu$ have different definitions and different possible finiteness behavior. A Hermitian analogue must first specify which invariant it estimates.

The first-variation formula gives a finite quantity to investigate. Suppose $\theta_s=\theta-s\eta$ has a smooth positive representative for $0\leq s\leq t$, and let $\gamma_s$ be a minimizing Gauduchon metric for its smooth equation. By \cref{prop:gaud-volume-first-variation} and the fundamental theorem of calculus,
\begin{equation}\label{eq:gaud-volume-subtraction-cost}
 \lambda_\mu(\theta-t\eta)
 =\lambda_\mu(\theta)
   -\int_0^t
       \frac{\int_X\eta\wedge\gamma_s^{n-1}}
            {D_\mu(\gamma_s)}\,ds.
\end{equation}
The quotient is unchanged by rescaling the minimizer. This identity is valid on the stated positive segment and uses no upper Monge--Amp\`ere mass bound. A uniform upper bound on its integrand gives a lower bound for the remaining root volume. Proving a useful bound near a degenerate endpoint is an additional problem; concavity alone provides the tangent upper bound, not the lower bound needed here.

\begin{problem}\label{qu:hermitian-morse-program}
Find geometric hypotheses controlling the cost in \eqref{eq:gaud-volume-subtraction-cost} up to a nef endpoint, and determine whether the resulting positive root volume forces bigness there. For closed backgrounds, compare the resulting estimate with classical Morse inequalities. For nonclosed backgrounds, retain the differential data and state explicitly any dependence on $\mu$.
\end{problem}

The singularity and divisorial constructions in the book become relevant at this stage: they record how much positivity can be spent on imposed poles, while the residual Gauduchon volume stays finite. They do not yet give the moving intersection product or the birational volume formula of the closed theory. Recovering such geometric information is a further objective, with the finite-divisor and Hopf calculations serving as explicit tests.
