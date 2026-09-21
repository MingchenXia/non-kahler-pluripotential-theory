Run_id: hopf_sections_01

Statement: Audit the complete explicit Hopf section/Bergman computation below. X_n=C^n minus0/exp(-1),n>=2, forms alpha=ddclog|z|²,zeta=ds dc s,omega=alpha+zeta; Gauduchon, integrals2 and2n. L_k characterexp(-k),metric|t|²|z|^-2k curvaturekalpha. Sections L_k^m exactlyhomogeneouspolysdegreekm byHartogs/Taylor. U(n)invariantnormandradialcancellation makeK=B constantN withdVprob. Degree2k(n-1)>0 butN_m~m^(n-1),normalizedtopvolume0 andcurvaturetop0,whileomega^n mass2n. Checkbundleequivariance signs, curvnormalization,fiberfactor2,action/metricinvariance,degree,count,k0,n2edges. No claim about allholomorphiclinebundles oralgebraicdimension.

Accepted standardinputs: Hartogs puncture removabilityn>=2, finiteHilbertspace orthonormalidentity integralK=dimension forweight0, basicclosedpositivecurvcalc. Existing audited hopf_counterexample_01 and bookchapter_hopf.tex provide the geometric calculation in dimension3, includingddczeta=-alpha² andellipticfiberintegral2 withnormalizedFSbasevolume1; verify extension toallnexplicitly. NoBMP,PVP,Kahlerassumptions. Bookread-only; proofbelow authoritative. Usualboundedverificationworkflow.

Proof:

\section{An explicit Bergman calculation on a Hopf manifold}

The following example puts a closed line-bundle curvature and a non-closed Hermitian background on the same manifold. It also shows that positive Gauduchon degree need not give growth of order $m^n$.

Let $n\geq2$ and
\[
 X_n=(\C^n\setminus\{0\})/\langle z\mapsto e^{-1}z\rangle.
\]
Use the forms
\[
 s=\log|z|^2,\qquad \alpha=\ddc s,\qquad
 \zeta=ds\wedge\dc s,\qquad \omega=\alpha+\zeta.
\]
These are the forms of \cref{chap:hopf}, with $\zeta$ replacing that chapter's symbol $\beta$. The same calculation gives
\[
 \alpha^n=0,\qquad \zeta^2=0,\qquad
 \ddc\zeta=-\alpha^2,
 \qquad \ddc(\omega^{n-1})=0.
\]
Thus $\omega$ is Gauduchon. Under projectivization $\pi:X_n\to\mathbb P^{n-1}$, the form $\alpha$ is the pullback of the normalized Fubini--Study form. The elliptic fiber calculation in \cref{chap:hopf} gives
\[
 \int_{X_n}\alpha^{n-1}\wedge\zeta=2,
 \qquad \int_{X_n}\omega^n=2n.
\]
Set $dV=\omega^n/(2n)$, a probability measure.

For an integer $k\geq0$ let $L_k$ be the line bundle defined by
\[
 (z,t)\sim(e^{-1}z,e^{-k}t)
\]
on $(\C^n\setminus\{0\})\times\C$. Give it the metric
$|t|_{h_k}^2=|t|^2|z|^{-2k}$. Both factors transform inversely, so this metric descends. Its curvature is $k\alpha$.

\begin{proposition}\label{prop:hopf-bergman-exact}
For $m\geq1$, with weight $u=0$, we have
\[
 N_m:=h^0(X_n,L_k^m)=\binom{km+n-1}{n-1},
 \qquad B_{m,0}=N_m.
\]
The Bergman potential is the constant $m^{-1}\log N_m$, and its curvature current is $k\alpha$. Moreover,
\[
 \deg_\omega L_k=2k(n-1),\qquad
 \lim_{m\to\infty}m^{-n}N_m=0,
 \qquad (k\alpha)^n=0.
\]
In contrast, $\int_{X_n}\omega^n=2n>0$.
\end{proposition}
\begin{proof}
A section lifts to a holomorphic function $f$ on $\C^n\setminus\{0\}$ satisfying
\[
 f(e^{-1}z)=e^{-km}f(z).
\]
Since $n\geq2$, Hartogs' removable-singularity theorem extends $f$ to all of $\C^n$. In its Taylor series, a monomial of total degree $j$ transforms by $e^{-j}$. Comparing coefficients shows that only degree $km$ occurs. Conversely every homogeneous polynomial of that degree has the required equivariance. Counting monomials gives the binomial coefficient, including the constant polynomial when $k=0$.

The inner product defined by $h_k^m$ and $dV$ is invariant under $U(n)$, so the basis-independent function $K_{m,0}$ is $U(n)$-invariant. It is also unchanged under any positive radial dilation: every section is homogeneous of degree $km$, and the factor $|z|^{-2km}$ in its squared norm cancels that dilation. Unitary transformations and positive radial dilations act transitively on $\C^n\setminus\{0\}$. Consequently $K_{m,0}$ is constant. Its integral is $N_m$ by the orthonormal-basis identity, and $dV$ has mass one. Thus $K_{m,0}=B_{m,0}=N_m$.

The potential and curvature statements follow immediately. Finally,
\[
 \int_{X_n}k\alpha\wedge\omega^{n-1}
 =k(n-1)\int_{X_n}\alpha^{n-1}\wedge\zeta
 =2k(n-1).
\]
The binomial coefficient grows at most as $m^{n-1}$, proving the normalized limit, and $\alpha^n=0$ proves the vanishing curvature mass.
\end{proof}

For $n=3$ this is the same manifold and Gauduchon form used in the unbounded-mass construction. Its line bundles $L_k$ have positive Gauduchon degree when $k>0$, explicit section spaces and zero top-degree closed-curvature mass. The Hermitian operator associated with $\omega$ has a different behavior, including the unbounded masses of \cref{thm:hopf-unbounded}. The example exhibits both theories in one geometry and keeps their respective curvatures visible.
