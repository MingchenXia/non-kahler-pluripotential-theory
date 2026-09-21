Run_id: relative_lp_barriers_01

Statement: Audit the supplied proof of uniform relative L-infinity estimate and prescribed-type Lp supersolution. theta>=0 big, model phi=P_theta[phi] with P_epsilon theta(phi) genuine for some epsilon<1; normalized u equivalent to phi and MAu<=f dV,f>=0,Lp,p>1. Conclude phi-C<=u<=phi with C depending fixed data and UPPER norm of f only, no lower integral assumption, noBMP/PVP. Second target given nonzero f Lp and lambda>0, construct w equivalent phi with MAw<=exp(lambda w)f. Accepted inputs: classical local BT/calculus/quasi-continuity/canonical reps/monotone continuity; product positivity; ordered contact and rooftop inequality; fixed-point MAphi<=1_phi=0 theta^n; normalized qpsh uniform small exponential integrability and fixed qpsh small exponential integrability; semipositive big bounded normalized and proper exponential existence with uniform bounds given norm upper and root-integral lower, proved in section_big_lp_equations.tex and independently audited in big_lp_equations_01 (check report status, conditional input if pending); singular strict domination for u with smaller-background envelope, v preceq u, MAu<=cMAv strictset,c<1, reconstructed in section_singular_domination.tex and independently audited. Check uniform constants including +1 added to auxiliary density, choice exponents, convex 2-variable composition and truncations without assuming difference of unbounded qpsh is qpsh, common finite-level product inequalities, exponential-vs-polynomial bound, no subtraction infinite measures, final threshold, and supersolution rooftop contact split. Source ALS26 arxiv2511.02339v1 Lemma5.5/5.6. Note source's printed final -3/-2 inference and constant a omissions should NOT be inherited. Our proof supplies explicit K. Read-only book; write usual report and records. No existence beyond supersolution claimed in this run.

Proof:

\begin{theorem}[Relative uniform estimate]\label{thm:relative-linfty}
Under the hypotheses on $(X,\theta,\varphi)$ above, suppose $u\simeq\varphi$, $\sup_Xu=0$, and
\[
 \mathrm{MA}_\theta(u)\leq f\,dV,
 \qquad0\leq f\in L^p(dV),\quad p>1.
\]
There is a constant $C$, depending on the fixed geometry, $\varphi$, $p$, and an upper bound for $\|f\|_{L^p}$, such that
\[
 \varphi-C\leq u\leq\varphi.
\]
\end{theorem}

\begin{proof}
We reconstruct \cite[Lemma 5.5]{ALS26}. The upper bound follows directly from the fixed-point property: $u\leq0$ and $u\preceq\varphi$, so $u$ is a competitor for $P_\theta[\varphi]$.

Fix $0<\varepsilon<1$ for which $\varphi_\varepsilon=P_{\varepsilon\theta}(\varphi)$ is genuine. Since $\varphi_\varepsilon\leq\varphi\leq0$, uniform exponential integrability for normalized $u$ and exponential integrability for this fixed $\varphi_\varepsilon$ allow a choice of $\gamma>0$ and $1<q<p$ such that
\[
 g=e^{-\gamma(\varphi_\varepsilon+u)}f
\]
has a uniform $L^q$ bound. More explicitly, choose $q<p$ first, apply H\"older with exponents $p/q$ and $p/(p-q)$, and then choose $\gamma$ small enough to control the exponential factor by Cauchy--Schwarz and the two exponential integrability estimates.

Apply \cref{thm:big-bounded-normalized} in background $(1-\varepsilon)\theta$ to the density $1+g$. We obtain a bounded $v$, with $\sup_Xv=0$, and $c>0$ such that
\[
 ((1-\varepsilon)\theta+\ddc v)^n=c(1+g)\,dV.
\]
Both $\|v\|_\infty$ and $c^{-1}$ are uniformly bounded. The added constant one ensures a uniform positive root integral, even if no lower bound for the integral of $f$ was specified.

Put $h=\varphi_\varepsilon+v\leq\varphi$ and define
\[
 \chi(t)=\frac1{1-t}\quad(t\leq0),\qquad
 \psi=\varphi+\chi(h-\varphi).
\]
Then $0\leq\chi\leq1$, $0<\chi'\leq1$, and $\chi''>0$. The formula is interpreted off the pole sets and then by the canonical representative. We justify it as follows. The function
$G(x,y)=x+\chi(y-x)$ on $y\leq x$ is convex and nondecreasing in each variable: its first derivatives are $1-\chi'$ and $\chi'$, and its Hessian is
\[
 \chi''\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\geq0.
\]
For bounded ordered potentials the local chain rule therefore gives
\[
 \theta+\ddc G(\varphi,h)
 \geq(1-\chi'(h-\varphi))\theta_\varphi
       +\chi'(h-\varphi)\theta_h\geq0.
\]
This bounded chain rule follows by local convolution after a common smooth correction; $G(x+r,y+r)=r+G(x,y)$ preserves that correction, and positivity follows by the same constant-form freezing used for bounded products. For unbounded potentials apply the bounded assertion to
$\varphi_k=\max(\varphi,-k)$ and $h_k=\max(h,-k)\leq\varphi_k$. Monotonicity of $G$ makes $G(\varphi_k,h_k)$ decrease. Its limit is $\theta$-plurisubharmonic and lies between $\varphi$ and $\varphi+1$, so it is genuine and equals $\psi$ as defined above. Locality on common finite levels and bounded product positivity give
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(\psi)
 \geq(\varphi-h+1)^{-2n}\mathrm{MA}^{\mathrm{ext}}_\theta(h)
 \geq c(\varphi-h+1)^{-2n}e^{-\gamma\varphi_\varepsilon}
             e^{-\gamma u}f\,dV.
\]
Pole sets have zero smooth volume, so the last inequality extends by exhaustion to all Borel sets.

Write $T=-\varphi_\varepsilon\geq0$. If $C\geq1+\|v\|_\infty$, then
$\varphi-h+1\leq T+C$. Since
\[
 A:=\inf_{T\geq0}\frac{e^{\gamma T}}{(T+C)^{2n}}>0,
\]
we obtain, with a uniform $d>0$,
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(\psi)
 \geq d e^{-\gamma u}\mathrm{MA}^{\mathrm{ext}}_\theta(u).
\]
Choose $K=2+\gamma^{-1}|\log d|$. On $\{u<\psi-K\}$ we have $u<1-K$, hence
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(u)
 \leq d^{-1}e^{\gamma(1-K)}
            \mathrm{MA}^{\mathrm{ext}}_\theta(\psi-K)
 \leq e^{-\gamma}\mathrm{MA}^{\mathrm{ext}}_\theta(\psi-K).
\]
The two potentials have the same ordinary singularity type. Moreover $P_{\varepsilon\theta}(u)$ is genuine, since $u\geq\varphi-C_u$ for some constant $C_u$. Singular strict domination yields $u\geq\psi-K\geq\varphi-K$. All constants used to choose $K$ are uniform in the asserted family. The possibly nonuniform $C_u$ is used only to provide a genuine envelope, not in any estimate.
\end{proof}

The estimate controls $u-\varphi$, rather than $u$ itself. The smaller-background condition supplies $\varphi_\varepsilon$ and enables the final domination argument; the bounded auxiliary equation is now supplied by the preceding sections.

\begin{lemma}[A supersolution of the prescribed type]\label{lem:relative-lp-supersolution}
For nonzero $0\leq f\in L^p(dV)$ and $\lambda>0$, there exists $w\simeq\varphi$ such that
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(w)\leq e^{\lambda w}f\,dV.
\]
\end{lemma}
\begin{proof}
Let $v$ be the bounded solution of \cref{thm:big-bounded-exponential}, and write $M=\sup_Xv$, $a=v-M\leq0$. The rooftop $p=P_\theta(a,\varphi)$ satisfies
$\varphi-\|a\|_\infty\leq p\leq\varphi$, so $p\simeq\varphi$. By the rooftop inequality,
\[
 \mathrm{MA}^{\mathrm{ext}}_\theta(p)
 \leq\mathbf1_{\{p=a\leq\varphi\}}\mathrm{MA}_\theta(a)
   +\mathbf1_{\{p=\varphi<a\}}\mathrm{MA}^{\mathrm{ext}}_\theta(\varphi).
\]
The second term vanishes: \cref{prop:fixed-point-finite} carries the measure of $\varphi$ on $\{\varphi=0\}$, while $\varphi<a\leq0$ excludes that set. On the first contact set, $a=p$ and
$\mathrm{MA}_\theta(a)=e^{\lambda(a+M)}f\,dV$. Thus
$\mathrm{MA}^{\mathrm{ext}}_\theta(p)\leq e^{\lambda(p+M)}f\,dV$. Take $w=p+M$. This is the argument of \cite[Lemma 5.6]{ALS26}.
\end{proof}

