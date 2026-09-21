Run_id: dominated_relative_compactness_01

Statement: Audit the new fixed-measure compactness supplement below. Connected compact complex X; semipositive big theta; model phi=Pphi with genuine smaller-background envelope; separate v_minus(theta)>0, NO upper mass bound/BMP. E_phi means convex-envelope class, may include infinite mass. Sequence u_j inE_phi converges L1 to genuine u and MA(u_j)<=fixed finiteNPPnu. We claim after one extraction there is a common lower envelope inE_phi, then full-sequence capacity and raw weak convergence. We do NOT claim entireoriginalsequence rooftop exists. Crucial argument: disjoint contact partition gives MA finite-roof<=nu with no number-of-obstacles factor; summable self-errors; forfixedB stretchedtails haveMA<=B^nnu andmass>=kappa, so testinge^u preventscollapse forlarge startingindexj uniformly inendpointN. Restorefiniteprefix byB=2b, averagingtail/prefixstretchedcompetitors. Check quantifiers carefully.

Accepted prerequisites: elementary E_phi properties and P[u]=phi forE_phi; normalizedL1compactness/Hartogs; fixedfiniteNPPmeasure exponential L1integration lemma; semipositive contact, orderedcontact; monotonecapacity withgenuinelowerbarrier; weightedextended lowersemicont andrawtailcontinuity. Allreconstructed earlier (chapter_envelopes.tex, section_relative_compactness.tex, chapter_damped_measures.tex). CONDITIONALLY accept newly drafted relative_class_domination_01 until reportavailable: finite rooftopclosure, Q_borderedstretchclosure, uniformmasslower kappa, strictdomination withfinite MA ofsmallerpotential. Readreportifavailable. Sources are attribution; do not import ALS Lem4.2 wholesale, itscompressedindexmanipulations arepreciselywhat thisproof avoids. Bookread-only. Usualworkflow/report; no noveltyclaim.

Proof:

\section{A common envelope after extraction}

A prescribed ordinary-type barrier is not needed when the Monge--Amp\`ere measures are all bounded by one finite measure. The lower-volume estimate can construct a barrier in the relative envelope class after extraction. We formulate exactly the extraction statement used in the convergence proof.

\begin{lemma}\label{lem:dominated-relative-rooftop-extraction}
Assume \eqref{eq:relative-positive-lower-volume}. Suppose $u_j\in\mathcal E_\varphi$, $u_j\to u\in\PSH(X,\theta)$ in $L^1(X)$, and $\mu_{u_j}\leq\nu$ for a fixed finite non-pluripolar measure $\nu$. There is a subsequence, denoted again by $u_j$, such that
\[
 h=P_\theta\left(\inf_j u_j\right)\in\mathcal E_\varphi.
\]
In particular $u\in\mathcal E_\varphi$.
\end{lemma}
\begin{proof}
The envelope identity \cref{prop:relative-envelope-equality} gives $P_\theta[u_j]=\varphi$. Since $u_j-\sup_Xu_j\leq P_\theta[u_j]$, Hartogs' lemma supplies a constant $C$ with $u_j\leq\varphi+C$ for all $j$. A common translation reduces to $u_j\leq\varphi\leq0$, and then $u\leq\varphi$. By \cref{lem:fixed-npp-integrals},
\[
 I_j=\int_X|e^{u_j}-e^u|\,d\mu_{u_j}\longrightarrow0.
\]
Extract so that $I_j\leq2^{-j}$ and $u_j\to u$ almost everywhere for smooth volume. This extraction is made once.

For $N\geq j$ put $p_{j,N}=P_\theta(u_j,\ldots,u_N)$. These are in $\mathcal E_\varphi$ by \cref{prop:relative-finite-rooftops}. Partition their contact sets by the first index at which the minimum is attained. Ordered contact on these disjoint pieces gives both
\begin{equation}\label{eq:finite-rooftop-common-domination}
 \mu_{p_{j,N}}\leq\nu,
 \qquad
 \int_X|e^{p_{j,N}}-e^u|\,d\mu_{p_{j,N}}
 \leq\sum_{\ell=j}^N I_\ell\leq2^{1-j}.
\end{equation}
The first bound has no factor $N$: each disjoint piece is bounded by the restriction of the same measure $\nu$ to that piece.

Fix a real number $B\geq1$ and set $r_{j,N}=Q_B(p_{j,N},\varphi)$. It belongs to $\mathcal E_\varphi$, so $\mu_{r_{j,N}}(X)\geq\kappa$. Contact support and positivity give
\[
 \mu_{r_{j,N}}\leq B^n\mathbf1_{D_{j,N}}\mu_{p_{j,N}}
 \leq B^n\nu,
\]
where $D_{j,N}=\{B^{-1}r_{j,N}+(1-B^{-1})\varphi=p_{j,N}\}$. On this set, since $\varphi\leq0$,
$e^{p_{j,N}}\leq e^{r_{j,N}/B}$. Consequently
\begin{equation}\label{eq:relative-rooftop-noncollapse-test}
 \int_Xe^u\,d\mu_{r_{j,N}}
 \leq B^n2^{1-j}
      +B^n\nu(X)\exp\!\left(\frac{\sup_X r_{j,N}}B\right).
\end{equation}
On the other hand choose $K>0$ with $B^n\nu(\{u\leq-K\})<\kappa/2$. This is possible since $u$ is genuine and $\nu$ does not charge its pole set. The preceding measure domination and lower mass bound imply
\[
 \int_Xe^u\,d\mu_{r_{j,N}}\geq e^{-K}\kappa/2.
\]
Choose $j$ so large that $B^n2^{1-j}<e^{-K}\kappa/4$. Formula \eqref{eq:relative-rooftop-noncollapse-test} then bounds $\sup_Xr_{j,N}$ from below independently of $N$. The sequence decreases in $N$ and has the common upper bound $\varphi$. Its limit $R$ is therefore genuine. It satisfies, for every $\ell\geq j$,
\begin{equation}\label{eq:relative-tail-stretched-competitor}
 B^{-1}R+(1-B^{-1})\varphi\leq u_\ell,
 \qquad R\leq\varphi.
\end{equation}
The second inequality follows already from $r_{j,N}\leq p_{j,N}\leq\varphi$.

It remains to include the finitely many earlier terms and to establish every defining envelope condition. Fix $b\geq1$ and apply the preceding construction with $B=2b$. Let $j$ and $R$ be as above. If $j>1$, let $p_0=P_\theta(u_1,\ldots,u_{j-1})$ and $S=Q_{2b}(p_0,\varphi)$. Both are genuine by the finite-rooftop and stretching lemmas, and $S\leq\varphi$. For $j=1$ set $S=\varphi$. The potential $H=(R+S)/2$ is $\theta$-plurisubharmonic. For a tail index use \eqref{eq:relative-tail-stretched-competitor} and $S\leq\varphi$; for a prefix index use its counterpart for $S$ and $R\leq\varphi$. In either case,
\[
 b^{-1}H+(1-b^{-1})\varphi\leq u_\ell
 \quad\hbox{for every }\ell\geq1.
\]
For $b=1$ this first proves that $h=P_\theta(\inf_\ell u_\ell)$ is genuine. For general $b$ the left side is a competitor for $h$, so the same inequality with $h$ in place of every $u_\ell$ supplies the defining $b$-condition. Also $h\leq\varphi$. Thus $h\in\mathcal E_\varphi$.

Finally $h\leq u_j$ for all $j$, hence $h\leq u\leq\varphi$ by the almost-everywhere limit and canonical representatives. Upward stability proves $u\in\mathcal E_\varphi$. Restoring the common translation proves the lemma as stated.
\end{proof}

The prefix and tail step matters: extracting a subsequence of finite rooftops does not allow one to rename the number of their obstacles. The proof above fixes a summable error sequence first, proves a lower bound uniform in the finite endpoint $N$, and then restores every term of that extracted sequence. It makes no assertion about the rooftop of the entire original sequence before extraction.

\section{Dominated continuity}

\begin{theorem}\label{thm:relative-fixed-measure-continuity}
Under \eqref{eq:relative-positive-lower-volume}, suppose $u_j\in\mathcal E_\varphi$, $u_j\to u\in\PSH(X,\theta)$ in $L^1(X)$, and $\mu_{u_j}\leq\nu$ for a fixed finite non-pluripolar measure $\nu$. Then
\[
 u\in\mathcal E_\varphi,
 \qquad u_j\longrightarrow u\text{ in capacity},
 \qquad \mu_{u_j}\rightharpoonup\mu_u\leq\nu.
\]
\end{theorem}
\begin{proof}
Start with any subsequence. Apply \cref{lem:dominated-relative-rooftop-extraction} to obtain a further subsequence with $I_j\leq2^{-j}$, almost-everywhere convergence, and a common lower envelope $h\in\mathcal E_\varphi$. Normalize all potentials below zero as in that proof. Keep the notation $p_{j,N}$, and set
\[
 p_j=P_\theta\left(\inf_{\ell\geq j}u_\ell\right),
 \qquad p=(\lim_jp_j)^*.
\]
The limits $p_{j,N}\downarrow p_j$ and $p_j\uparrow p$ have the genuine lower bound $h$, and all potentials are at most $\varphi$. They converge in capacity by the monotone observation preceding \cref{thm:common-barrier-criterion}. Upward stability gives $p_j,p\in\mathcal E_\varphi$.

Apply weighted lower semicontinuity to \eqref{eq:finite-rooftop-common-domination}, first in $N$ and then in $j$. Nonnegative continuous test functions give $\mu_{p_j},\mu_p\leq\nu$, so these measures are finite. The bounded quasi-continuous exponential weights give
\[
 \int_X|e^p-e^u|\,d\mu_p=0.
\]
The construction and almost-everywhere convergence give $p\leq u$. Thus $\mu_p$ vanishes on $\{p<u\}$. Since $p\in\mathcal E_\varphi$ has finite measure and $u\preceq\varphi$, \cref{thm:relative-finite-domination} with coefficient zero yields $p\geq u$. Hence $p=u$.

The upper tail envelopes $U_j=(\sup_{\ell\geq j}u_\ell)^*$ decrease to $u$, by Hartogs' lemma and the almost-everywhere extraction. Their genuine lower bound is $h$. The inequalities $p_j\leq u_j\leq U_j$ and monotone capacity convergence prove capacity convergence of the extracted sequence.

For its raw measures use the same fixed lower bound:
\[
 \mu_{u_j}(\{u_j\leq-T\})
 \leq\nu(\{h\leq-T\})\longrightarrow0
 \quad\hbox{uniformly in }j.
\]
The raw-tail theorem \cref{thm:undamped-tail-continuity} now yields weak convergence to $\mu_u$. Weak limits preserve domination by the fixed finite $\nu$. Every original subsequence has a further subsequence with these conclusions and the same limit $u$. This proves both convergences for the original sequence. Class membership was already supplied by the extraction lemma.
\end{proof}

This reconstructs the fixed-dominating-measure case of \cite[Lemma 4.2 and Theorem 4.1]{ALS26}, in an extraction form sufficient for convergence. The argument uses $v_-(\theta)>0$ only to prevent the stretched comparison envelopes from collapsing. It never uses $v_+(\theta)<+\infty$.
