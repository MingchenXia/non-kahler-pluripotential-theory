Run_id: weighted_measure_addition_01

Statement: Audit the new lower-barrier capacity criterion variant and the full addition theorem below. theta>=0big, phi ANYthetaPSH admitting genuine P_delta theta(phi); u~v~phi;lambda>0; mu=exp(-lambda u)MAextu+exp(-lambda v)MAextv FINITE. Claim unique a~phi withMAexta=exp(lambda a)mu. NoBMP/PVP/uniform approximating rawmass. Finiteu_j/v_j/a_j are bounded, not ordinarytypephi. The variant requires lowerphi-C<=a_j andcommonupperbound,limit a preceqphi,vanishing integral|exp a_j-exp a|MAa_j. Check carefully its rooflimits and strictdom applicability despite finite rooftops notsamephi. Then check barriers, factor2^n, translation, truncationfinitelevelerrors, polynomialj^r withr=max(n-2,0), and particularly NEW direct localizedpassage: fixedlowerw=(u+v)/2-D<=a_j, g_T(w) cutoffvanishesondeep truncationregion forj>2T, hence exactweightedidentitypassesbyboundedBT/fixedmeasure. No globalrawweakconvergence assumed. Auditpositiveextendedmeasure limits,absencepluripolarmass, andlimitfinitefollowsfromequation.

Accepted inputs: standardboundedBT/quasicont/capacityweightedcontinuityandmonotoneconvergence; classicalfixedNPPexponentialintegralconvergence; normalizedL1compactness; semipositivecontact/anybackgroundorderedcontact/finite-roofpartition; smallerbackgroundsingularstrictdom/exponentialorder(singular_domination_01); Gauduchon bounded-range massestimateC(1+j)^r,including1/2dimensions(gauduchon_growth_01). The common-barrier criterion thm:common-barrier-criterion and weightedextendedlowersemicont are being checked common_barrier_compactness_01, acceptconditionallyifpending (readbook/inputofthatrun for exactproof). Boundedsubsolutiontheorem is being checked bounded_subsolution_01,acceptconditionallyifpending. DoNOTaccept targetadditionfromALS5.2 asaninput;compare source only. Readonlybook,usualreport.

Proof:

\begin{proposition}[Approximants with milder singularities]\label{prop:lower-barrier-criterion}
In \cref{thm:common-barrier-criterion}, one may replace the two bounds on $u_j$ by
\[
 \varphi-C\leq u_j\leq C
\]
provided the $L^1$ limit satisfies $u\preceq\varphi$. In particular the approximants may be bounded while $\varphi$ is unbounded.
\end{proposition}
\begin{proof}
The $L^1$ limit satisfies $u\geq\varphi-C$, so the additional hypothesis implies $u\simeq\varphi$. Repeat the finite rooftop construction in the theorem. Every $p_{j,N}$ remains genuine and lies between $\varphi-C$ and $C$, which is enough for contact support and for the bounded exponential weights. The resulting inequality is still
\[
 \int_X|e^{p_{j,N}}-e^u|\,
             \mathrm{MA}^{\mathrm{ext}}_\theta(p_{j,N})\leq2^{1-j}.
\]
The limits $p_j$ exist by the common lower bound, and $p_j\leq u$ follows from $p_j\leq u_\ell$ for every $\ell\geq j$ and almost-everywhere convergence. Thus
$\varphi-C\leq p_j\leq u$, and all $p_j$ and their increasing limit $p$ have the same ordinary type as $\varphi$. Monotone capacity convergence and weighted lower semicontinuity give
$\mathrm{MA}^{\mathrm{ext}}_\theta(p)(\{p<u\})=0$. Singular domination applies to $(p,u)$ exactly as before, so $p=u$. The upper tail envelopes decrease to $u$, and the same sandwich gives capacity convergence. No singularity-type assertion was needed for the finite rooftops or for the individual approximants.
\end{proof}


\section{Adding weighted Monge--Amp\`ere measures}

The next construction will allow us to enlarge the right-hand side of a prescribed-type equation. Its approximants are bounded, and their raw masses need not have a uniform bound. The capacity criterion with a lower barrier is suited to this situation.

\Needspace{15\baselineskip}
\begin{theorem}[Addition of two weighted measures]\label{thm:weighted-measure-addition}
Let $\theta\geq0$ be big, and suppose $\varphi\in\PSH(X,\theta)$ admits a genuine smaller-background envelope. Let $u,v\simeq\varphi$ and $\lambda>0$. If
\[
 \mu=e^{-\lambda u}\mathrm{MA}^{\mathrm{ext}}_\theta(u)
       +e^{-\lambda v}\mathrm{MA}^{\mathrm{ext}}_\theta(v)
\]
is a finite measure, then there exists $a\in\PSH(X,\theta)$, with $a\simeq\varphi$, such that
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(a)=e^{\lambda a}\mu.
\]
Weights are interpreted off the pluripolar pole sets. The solution is unique in this ordinary singularity type.
\end{theorem}
\begin{proof}
This is the addition argument of \cite[Theorem 5.2]{ALS26}, with a localized passage to the equation. A common translation reduces to $u,v\leq0$: translating by $-S$ multiplies $\mu$ by $e^{\lambda S}$ and translates the resulting solution back by $S$.

Set $u_j=\max(u,-j)$, $v_j=\max(v,-j)$ and
\[
 \mu_j=e^{-\lambda u_j}\mathrm{MA}_\theta(u_j)
           +e^{-\lambda v_j}\mathrm{MA}_\theta(v_j).
\]
For $s_j=(u_j+v_j)/2$, positivity gives
\[
 \mu_j\leq2^n e^{\lambda j}\mathrm{MA}_\theta(s_j).
\]
Each measure is finite and nonzero by individual bounded noncollapse. The bounded subsolution theorem gives $a_j$ with
$\mathrm{MA}_\theta(a_j)=e^{\lambda a_j}\mu_j$.
Bounded exponential order yields
\[
 a_j\leq\min(u_j,v_j)\leq0.
\]
Choose $C$ with $|u-v|\leq C$ off the common poles; then $|u_j-v_j|\leq C$. Put
\[
 D=C/2+n\lambda^{-1}\log2,\qquad b_j=s_j-D.
\]
The inequality
\[
 e^{-\lambda b_j}\mathrm{MA}_\theta(b_j)
 \geq2^{-n}e^{\lambda D-\lambda s_j}
            \bigl(\mathrm{MA}_\theta(u_j)+\mathrm{MA}_\theta(v_j)\bigr)
 \geq\mu_j
\]
follows from $|u_j-v_j|\leq C$. Hence $a_j\geq b_j\geq w$, where
\[
 w=(u+v)/2-D\simeq\varphi
\]
is a fixed genuine potential. Extract $a_j\to a$ in $L^1(X)$. The upper barriers decrease to $\min(u,v)$, so $w\leq a\leq\min(u,v)$ and $a\simeq\varphi$.

To prove convergence in capacity, write $E_j=\{\min(u,v)>-j\}$. Locality gives $\mu_j=\mu$ there. Thus
\[
 \int_{E_j}|e^{a_j}-e^a|\,\mathrm{MA}_\theta(a_j)
 \leq\int_X|e^{a_j}-e^a|\,d\mu\longrightarrow0
\]
by \cref{lem:fixed-npp-integrals}. On $X\setminus E_j$ we have $a_j\leq-j$ and $a\leq-j$, whence $|e^{a_j}-e^a|\leq e^{-j}$. Also
\[
 \mathrm{MA}_\theta(a_j)
 =e^{\lambda(a_j-u_j)}\mathrm{MA}_\theta(u_j)
    +e^{\lambda(a_j-v_j)}\mathrm{MA}_\theta(v_j)
 \leq\mathrm{MA}_\theta(u_j)+\mathrm{MA}_\theta(v_j).
\]
Choose a Hermitian $\Omega\geq\theta$. The bounded-range estimate gives
\[
 \int_{X\setminus E_j}|e^{a_j}-e^a|\,\mathrm{MA}_\theta(a_j)
 \leq C'e^{-j}(1+j)^{r_n}\longrightarrow0,
 \qquad r_n=\max(n-2,0).
\]
The lower-barrier criterion \cref{prop:lower-barrier-criterion} now gives $a_j\to a$ in capacity. Only polynomial control of the approximating masses was needed.

It remains to identify the equation. This can be done on bounded levels without claiming raw weak convergence prematurely. For $T>0$ choose the continuous cutoff $g_T$ from \cref{lem:weighted-extended-lsc} and put $\zeta_T=g_T(w)$. On its support $w>-2T$, hence every $a_j$ and $a$ is above $-2T$. If $j>2T$ and $x\notin E_j$, the inequalities $w(x)\leq a_j(x)\leq-j$ force $\zeta_T(x)=0$. Consequently, for all $j>2T$,
\[
 \zeta_T\mathrm{MA}_\theta(a_j)
       =\zeta_T e^{\lambda a_j}\mu.
\]
Test this identity against any continuous function. On the left, replace $a_j$ by $\max(a_j,-2T)$ and use bounded capacity continuity with the fixed bounded quasi-continuous weight $\zeta_T$. On the right, fixed-measure exponential convergence gives convergence in total variation. Therefore
\[
 \zeta_T\mathrm{MA}^{\mathrm{ext}}_\theta(a)
       =\zeta_Te^{\lambda a}\mu.
\]
Let $T\to\infty$. The cutoffs increase to one off the pole set of the genuine $w$; all measures ignore that set. This proves the equation and, in particular, finiteness of the limiting raw measure. Uniqueness follows from singular exponential order.
\end{proof}
