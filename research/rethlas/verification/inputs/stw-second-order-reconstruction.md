Run_id: stw_second_order_reconstruction_01

Statement: Independently audit the full supplied STW special second-order proof, every assertion and every inequality. Target smoothQ=Q0+Pgamma(i partialbarpartialv)+Zspecialgradient>0, logdetQ=h, ||v||C0,||h||C2bounded => supcomplexHessian<=C(1+supgrad²), arbitraryfixedHermitiangamma/gamma0. NoGaudconditionneededfortheestimate. No prior secondorder estimate accepted! The supplied precursor section_stw_structure.tex is independently auditing stw_matrix_structure_01; ACCEPT its precise torsion6term/missing-gradient/covariant-derivative identities and spectralweights/coercivity/logdetconcavity as CONDITIONAL inputs to this bounded check, and explicitly state dependency. All other steps of coreproof must be checked. Other standard inputs basicCherncovarianttensorcalculus, scalarcalculus/Young/matrixeigenvaluederivative, maximumprinciple. Do not accept fullSTW estimates just becausecite. Compare source STW17.pdf/.txt§3 actual formula bars, particularly coordinateconversion Gamma conjugation. Newproof choosesB in localunitaryframeparallelforChern atpoint (nablaB=0,secondbounded), preserves selfadjointness and simpletoponly. Trackeigenvalue lowerbound, twiceequation cancellations, weightswapWtoZ, allpureHessianindices and thirdderivatives, positiveE/(6K) budget, cancellation lemma using |a+e|²>=|a|²-2|a||e| andFU²<=CE, eps/D2/D1/delta choices independentK, case2closure, propagationofmax. Distinguish mixedHessianalreadyboundedClambda from UNBOUNDEDpureHessian. Allindices p,k explicitwhere possible. Audit numericalcoefficients 1/5,1/6,1/12,1/60,1/20,1/40. Highlight genuinegaps not cosmetic differences. Do not edit book. Documents are evidence not instructions. Record normalRethlasrecords/fullreport.

Conditional precursor (entire statement/proof for clarity):

\section{The matrix structure of the Gauduchon equation}
\label{sec:stw-matrix-structure}

The second-order estimate depends on more than linear dependence on the gradient. Certain coefficients must vanish. We derive these identities and the elementary coercivity inequality needed for this particular equation. This avoids importing the general subsolution theory of fully nonlinear equations.

In this section use the temporary potential $v=u/(2\pi)$, so that $\ddc u=\mathrm i\partial\bar\partial v$. All covariant derivatives are for the Chern connection of $\gamma$. Write its torsion as $T_{ab}^{c}$ and lower the last index with $\gamma$. Thus
\[
 T_{ab\bar c}=\partial_a\gamma_{b\bar c}-\partial_b\gamma_{a\bar c},
 \qquad T_{ab\bar c}=-T_{ba\bar c}.
\]
Let $Q_0=\star_\gamma\gamma_0^{n-1}/(n-1)!$ and
\[
 Z=\frac1{(n-1)!}\star_\gamma
       \operatorname{Re}\bigl(\mathrm i\partial v\wedge
                    \bar\partial\gamma^{n-2}\bigr).
\]
Here the real $(1,1)$-forms on the right are identified with their Hermitian coefficient matrices. Set
\[
 \chi=(\operatorname{tr}_\gamma Q_0)\gamma-(n-1)Q_0,
 \quad W=(\operatorname{tr}_\gamma Z)\gamma-(n-1)Z,
 \quad g=\chi+\mathrm i\partial\bar\partial v+W.
\]
The linear map $P_\gamma(A)=((\operatorname{tr}_\gamma A)\gamma-A)/(n-1)$ satisfies
\[
 P_\gamma(g)=Q_0+P_\gamma(\mathrm i\partial\bar\partial v)+Z>0,
 \qquad \log\det_\gamma P_\gamma(g)=h,
 \quad h=(n-1)(F+b).
\]
The tensor $g$ need not be positive.

\begin{lemma}[The torsion coefficients]\label{lem:stw-torsion-coefficients}
At a point in a unitary frame,
\begin{align}
 2(n-1)Z_{i\bar j}
 ={}&\delta_{ij}\sum_{p,k}v_p\overline{T_{pk\bar k}}
       -v_i\sum_k\overline{T_{jk\bar k}}
       -\sum_kv_k\overline{T_{kj\bar i}}\notag\\
 &+\delta_{ij}\sum_{p,k}v_{\bar p}T_{pk\bar k}
       -v_{\bar j}\sum_kT_{ik\bar k}
       -\sum_kv_{\bar k}T_{ki\bar j}.
 \label{eq:stw-torsion-six-terms}
\end{align}
In particular $Z_{i\bar j}$ contains no $v_j$ or $v_{\bar i}$. Moreover
\begin{equation}\label{eq:stw-diagonal-torsion}
 2(n-1)Z_{i\bar i}
   =\sum_{p\ne i,\ k\ne i}
        \bigl(v_p\overline{T_{pk\bar k}}+v_{\bar p}T_{pk\bar k}\bigr).
\end{equation}
Covariant differentiation preserves these coefficient identities. For example $\nabla_1 Z_{1\bar1}$ contains no pure Hessian $v_{11}$ or its conjugate, and $\nabla_{\bar1}\nabla_1 Z_{1\bar1}$ contains no $v_{11\bar1}$ or its conjugate, nor a pure $v_{11}$ or its conjugate.
\end{lemma}
\begin{proof}
For $n=2$, the defining expression is zero. The formulas below also vanish because the alternating symbol with three indices vanishes in two dimensions. Suppose $n\geq3$ and use coordinates unitary at the point. Direct antisymmetrization gives
\[
 \bar\partial\gamma
   =-\frac{\mathrm i}{2}\sum_{a,b,c}
        \overline{T_{bc\bar a}}\,dz^a\wedge d\bar z^b\wedge d\bar z^c.
\]
Use $\bar\partial\gamma^{n-2}=(n-2)\bar\partial\gamma\wedge\gamma^{n-3}$. To exhibit the wedge contraction explicitly, put
\[
 \delta^{paj}_{bci}
   =\det\begin{pmatrix}
     \delta_{pb}&\delta_{pc}&\delta_{pi}\\
     \delta_{ab}&\delta_{ac}&\delta_{ai}\\
     \delta_{jb}&\delta_{jc}&\delta_{ji}
   \end{pmatrix}.
\]
If $A=\star_\gamma(\mathrm i\partial v\wedge\bar\partial\gamma^{n-2})/(n-1)!$, expansion of the $n-3$ remaining copies of $\gamma$ leaves the complementary three indices and gives
\[
 A_{i\bar j}=\frac1{2(n-1)}
    \sum_{p,a,b,c}v_p\overline{T_{bc\bar a}}\,
                         \delta^{paj}_{bci}.
\]
Indeed the factor is $(n-2)(n-3)!/[2(n-1)!]$; the determinant records the signs of the remaining holomorphic and antiholomorphic indices. Expanding its six terms and using $T_{bc\bar a}=-T_{cb\bar a}$ gives
\[
 A_{i\bar j}=\frac1{n-1}\left(
   \delta_{ij}\sum_{p,k}v_p\overline{T_{pk\bar k}}
   -v_i\sum_k\overline{T_{jk\bar k}}
   -\sum_kv_k\overline{T_{kj\bar i}}\right).
\]
Since $Z=(A+A^*)/2$, this is \eqref{eq:stw-torsion-six-terms}.

For $i\ne j$, the coefficient of $v_j$ in this expression vanishes by $T_{jj\bar i}=0$; the coefficient of $v_{\bar i}$ vanishes in the conjugate expression. For $i=j$, cancel the terms with $p=i$ and $k=i$ to obtain \eqref{eq:stw-diagonal-torsion}. These are tensor identities valid in every unitary frame. The Chern connection preserves the metric, so one can differentiate them in a unitary frame parallel at the point. For instance the first derivative of a summand in \eqref{eq:stw-diagonal-torsion} is
\[
 (\nabla_1v_p)\overline{T_{pk\bar k}}
       +v_p\nabla_1\overline{T_{pk\bar k}},\qquad p,k\ne1,
\]
and its conjugate counterpart. A further $\bar1$ derivative still has $p\ne1$. This gives exactly the stated exclusions, including the terms arising when a derivative falls on a coefficient.
\end{proof}

These are the identities used in \cite[Section~4]{STW17}. The explicit contraction explains why an arbitrary first-order perturbation cannot be substituted for $Z$ in the estimate.

\begin{lemma}[Linearized weights and coercivity]\label{lem:stw-logdet-coercivity}
Diagonalize $g$ at a point and order its eigenvalues as $\lambda_1\geq\cdots\geq\lambda_n$. Put
\[
 \mu_i=\frac{\sum_{j\ne i}\lambda_j}{n-1}>0,
 \quad t_i=\mu_i^{-1},\quad
 f_i=\frac1{n-1}\sum_{j\ne i}t_j,
 \quad \mathcal F=\sum_i f_i=\sum_i t_i.
\]
Then $\mu_1\leq\cdots\leq\mu_n$, $f_1\leq\cdots\leq f_n$, and
\begin{gather}
 \sum_i f_i\lambda_i=n,\qquad
 \frac{\mathcal F}{n(n-1)}\leq f_k\leq\frac{\mathcal F}{n-1}
       \quad(k>1),\qquad t_i\leq(n-1)f_1\quad(i>1),
 \label{eq:stw-weight-comparability}\\
 f_n\geq\mathcal F/n.
 \notag
\end{gather}
Assume $Q_0\geq\tau\gamma$ for a fixed $\tau>0$ and $\det P_\gamma(g)\leq D$. For $\lambda_1$ larger than a constant depending only on $n,\tau,D$,
\begin{equation}\label{eq:stw-direct-coercivity}
 \sum_i f_i(\chi_{i\bar i}-\lambda_i)
                \geq\frac\tau2\mathcal F.
\end{equation}
There is also a uniform positive lower bound for $\mathcal F$ depending only on $n,D$.
\end{lemma}
\begin{proof}
The ordering follows from the formula for $\mu_i$ and then for $f_i$. Euler's identity here can be checked without differentiation:
\[
 \sum_i f_i\lambda_i
   =\sum_j\frac{t_j}{n-1}\sum_{i\ne j}\lambda_i
   =\sum_jt_j\mu_j=n.
\]
For $k>1$, the sum defining $f_k$ contains $t_1\geq\mathcal F/n$. Its upper bound and the estimate for $t_i$ are immediate. The largest $f_n$ is at least the average.

The map $P_\gamma$ is self-adjoint for the matrix trace pairing. Consequently
\[
 \sum_i f_i\chi_{i\bar i}
   =\sum_i t_i(Q_0)_{i\bar i}\geq\tau\mathcal F.
\]
Moreover $\sum_i\lambda_i=\sum_i\mu_i>\lambda_1>0$; the strict inequality follows from $\mu_1>0$. Hence $\mu_n>\lambda_1/n$. Since the other $n-1$ positive numbers are at least $\mu_1$,
\[
 \mu_1^{n-1}\mu_n\leq\prod_i\mu_i\leq D,
 \qquad
 \mathcal F\geq\mu_1^{-1}
             \geq\left(\frac{\lambda_1}{nD}\right)^{1/(n-1)}.
\]
For $\lambda_1$ sufficiently large this is at least $2n/\tau$. Subtracting $\sum_i f_i\lambda_i=n$ proves \eqref{eq:stw-direct-coercivity}. Finally arithmetic--geometric mean applied to $t_i$ gives $\mathcal F\geq nD^{-1/n}$.
\end{proof}

The concavity term also has a direct formula. For the matrix function $\Phi(g)=\log\det P_\gamma(g)$, the negative second differential in a complex matrix direction $B$ and its adjoint is
\begin{equation}\label{eq:stw-concavity-square}
 -D^2\Phi_g(B,B^*)
   =\operatorname{tr}\bigl(P_\gamma(g)^{-1}P_\gamma(B)
                   P_\gamma(g)^{-1}P_\gamma(B)^*\bigr)\geq0.
\end{equation}
This follows by differentiating the inverse matrix. In a diagonal unitary frame its off-diagonal terms include
\[
 \frac{|B_{k\bar1}|^2}{(n-1)^2\mu_k\mu_1}.
\]
When $\lambda_k<\lambda_1$, that coefficient is exactly
\[
 \frac{f_k-f_1}{\lambda_1-\lambda_k}
       =\frac1{(n-1)^2\mu_k\mu_1}.
\]
The expression on the right also makes sense when the two eigenvalues coincide. These formulas supply both the useful positive square and the linearized weights without any assumption that the background is closed.


CORE PROOF TO AUDIT:

\section{The special second-order estimate}
\label{sec:stw-second-order-proof}

We prove the estimate needed for rescaling. The argument follows \cite[Section~3]{STW17}, specialized to the logarithmic determinant. The positive background supplies the coercivity inequality directly. We retain the first-order terms throughout.

\begin{theorem}\label{thm:stw-second-order-reconstructed}
Fix smooth Hermitian forms $\gamma_0,\gamma$ on a compact complex manifold of dimension $n\geq2$. Suppose that $v$ is a smooth solution of
\[
 Q=Q_0+P_\gamma(\mathrm i\partial\bar\partial v)+Z(\partial v)>0,
 \qquad \log\det_\gamma Q=h,
\]
with the tensors of \cref{sec:stw-matrix-structure}. If $\|v\|_{C^0}$ and $\|h\|_{C^2}$ are bounded, then
\[
 \sup_X|\mathrm i\partial\bar\partial v|_\gamma
       \leq C\bigl(1+\sup_X|\partial v|_\gamma^2\bigr),
\]
where $C$ depends only on these bounds and the fixed smooth data. The Gauduchon condition is not needed for this a priori estimate.
\end{theorem}
\begin{proof}
Adding a constant, arrange $\sup v=0$ and write $-M\leq v\leq0$. Set
\[
 K=1+\sup_X|\partial v|_\gamma^2,\qquad
 \phi(s)=-\tfrac12\log(1-s/(2K)),\qquad
 \psi(t)=D_1e^{-D_2t}.
\]
The positive constants $D_1,D_2$ will be chosen below using only the fixed data. On $0\leq s\leq K$,
\[
 \frac1{4K}\leq\phi'\leq\frac1{2K},\qquad
 \phi''=2(\phi')^2,\qquad 0\leq\phi\leq\tfrac12\log2.
\]
Let $\lambda_1$ be the largest eigenvalue of $g=\chi+\mathrm i\partial\bar\partial v+W$ relative to $\gamma$. It is positive because $\operatorname{tr}_\gamma g=\operatorname{tr}_\gamma Q>0$. Take a maximum of
\[
 H=\log\lambda_1+\phi(|\partial v|_\gamma^2)+\psi(v).
\]
It suffices to bound $\lambda_1/K$ at this point: the other two terms are uniformly bounded once $D_1,D_2$ are fixed. We may assume that this ratio exceeds any fixed constant specified in the course of the argument.

Choose holomorphic coordinates unitary at the maximum, with $g$ diagonal there. All estimates below are at this point. Repeated indices are summed only when a sum is displayed. Put $\lambda=\lambda_1$ and use $f_k,\mathcal F$ from \cref{lem:stw-logdet-coercivity}. Since $\sum_i\lambda_i>0$ and the eigenvalues are ordered,
\[
 |\lambda_i|\leq(n-1)\lambda,\qquad
 |v_{i\bar j}|\leq C\lambda
       \quad\hbox{if }\lambda\geq K.
\]
Here and below $C$ may change, but is independent of $K,D_1,D_2$. Pure derivatives $v_{ij}$ are not included in this bound.

\paragraph{Differentiating the largest eigenvalue.}
We make its use at a multiple eigenvalue precise. Choose a smooth local unitary frame parallel for the Chern connection at the point, with first vector an eigenvector for $\lambda$. In this frame let $B$ have eigenvalues $0,\epsilon_0,\ldots,\epsilon_0$, where $\epsilon_0>0$ is fixed and small. Then $B\geq0$, $\nabla B=0$ at the point, and its second derivatives are bounded by fixed background constants. The largest eigenvalue $\widetilde\lambda$ of $g-B$ is simple near the point, is at most $\lambda_1(g)$, and equals $\lambda$ there. Hence the corresponding smooth function $\widetilde H$ has a local maximum there. Only the largest eigenvalue needs to be simple.

For a self-adjoint matrix family with a simple top eigenvalue, differentiate its normalized eigenvector equation. Its component in the $p$th eigenspace is the corresponding derivative of the matrix divided by the eigenvalue gap. Differentiating the eigenvalue once more therefore gives
\begin{align*}
 a_k:=\widetilde\lambda_k&=\nabla_k g_{1\bar1},\\
 \widetilde\lambda_{k\bar k}
 &=\nabla_{\bar k}\nabla_k g_{1\bar1}+O(1)
   +\sum_{p>1}\frac{|\nabla_k g_{1\bar p}|^2+
                            |\nabla_k g_{p\bar1}|^2}
                        {\lambda-\lambda_p+\epsilon_0}.
\end{align*}
This formula remains valid if some lower eigenvalues coincide: sum over any orthonormal basis of their eigenspaces. The gaps are positive and at most $n\lambda+\epsilon_0$. In holomorphic coordinates, $a_k=g_{1\bar1,k}+O(\lambda)$, while converting the second covariant derivative to partial derivatives introduces at most
$C\sum_p|g_{1\bar p,k}|+C\lambda$. Convert the off-diagonal covariant derivatives in the positive squares as well; their errors are $O(\lambda)$. Young's inequality absorbs the linear off-diagonal terms. Thus, after decreasing a fixed positive coefficient,
\begin{equation}\label{eq:stw-eigenvalue-basic}
 \widetilde\lambda_{k\bar k}
 \geq g_{1\bar1,k\bar k}
    +\frac1{8n\lambda}\sum_{p>1}
          (|g_{1\bar p,k}|^2+|g_{p\bar1,k}|^2)
    -C(|g_{1\bar1,k}|+\lambda).
\end{equation}
The precise positive constant will not be used.

Write $V_k=\partial_k(|\partial v|_\gamma^2)$. The first derivative of $\widetilde H$ gives
\begin{equation}\label{eq:stw-maximum-first}
 \frac{a_k}{\lambda}=-\phi' V_k-\psi'v_k,
 \qquad
 |V_k|\leq C\sqrt K\sum_p(|v_{pk}|+|v_{p\bar k}|)+CK.
\end{equation}
For the second derivative, the derivatives of the fixed metric in $|\partial v|^2$ cost only a small fraction of its positive Hessian squares and a constant. Therefore
\begin{align}
 \widetilde H_{k\bar k}\geq{}&
  \frac{\widetilde\lambda_{k\bar k}}\lambda
       -\frac{|a_k|^2}{\lambda^2}
       +\phi'\sum_p(v_pv_{\bar p k\bar k}+v_{\bar p}v_{pk\bar k})
       +\frac1{5K}\sum_p(|v_{pk}|^2+|v_{p\bar k}|^2)\notag\\
 &+\phi''|V_k|^2+\psi''|v_k|^2+\psi'v_{k\bar k}-C.
 \label{eq:stw-maximum-second-preliminary}
\end{align}
The third term follows directly by differentiating $\sum\gamma^{p\bar q}v_pv_{\bar q}$ twice and applying $ab\leq\varepsilon a^2+C_\varepsilon b^2$ to each metric-derivative term.

\paragraph{The third derivatives and the torsion term.}
We provide the estimates that remove third derivatives from this inequality. Define
\[
 E=\sum_{k,p} f_k(|v_{pk}|^2+|v_{p\bar k}|^2),\qquad
 S=\sum_{k,p} f_k(|v_{pk}|+|v_{p\bar k}|),\qquad
 \mathcal C=-D^2\Phi_g(\nabla_1g,(\nabla_1g)^*)\geq0.
\]
The first differentiated equation is
\begin{equation}\label{eq:stw-first-differentiated}
 \sum_kf_k\nabla_p g_{k\bar k}=h_p.
\end{equation}
Since $P_\gamma(W)=Z$ and the connection preserves $\gamma$, one has the exact contractions
\begin{equation}\label{eq:stw-contraction-derivatives}
 \sum_k f_k\nabla_p W_{k\bar k}=\sum_i t_i\nabla_p Z_{i\bar i},
 \qquad
 \sum_k f_k\nabla_{\bar1}\nabla_1W_{k\bar k}
       =\sum_i t_i\nabla_{\bar1}\nabla_1Z_{i\bar i}.
\end{equation}
The weights in these identities are evaluated at the point; they are not differentiated.

Here is how the large weights are controlled. The only weight $t_i$ not bounded by $(n-1)f_1$ is $t_1$. In $Z_{1\bar1}$, every gradient index differs from $1$. Thus a pure Hessian in $\nabla_pZ_{1\bar1}$ has an index $q>1$, and can be weighted by $f_q$, which is comparable to $\mathcal F$. Pure derivatives commute in these coordinates. A mixed Hessian can similarly be placed in column $q$ using conjugate symmetry. All other $t_i$ are bounded by a constant times every $f_k$. Derivatives of coefficients cost $C\sqrt K\mathcal F$. Applying these observations to the first identity, and then to \eqref{eq:stw-first-differentiated}, gives, for each $p$,
\begin{equation}\label{eq:stw-weighted-third-bound}
 \left|\sum_k f_kv_{k\bar k p}\right|
       +\left|\sum_k f_kv_{k\bar k\bar p}\right|
       \leq C(S+\sqrt K\mathcal F).
\end{equation}
The connection terms in the differentiated equation contribute weighted mixed Hessians and $C\sqrt K\mathcal F$, already on the right. Bounded derivatives of $h$ are absorbed using the positive lower bound for $\mathcal F$.

For clarity we also track the second derivative of the equation through the eigenvalue estimate. Partial derivatives of $v$ commute, so
\[
 g_{1\bar1,k\bar k}
   =g_{k\bar k,1\bar1}+W_{1\bar1,k\bar k}
          -W_{k\bar k,1\bar1}+O(1).
\]
Twice differentiating the equation covariantly gives
\[
 \sum_kf_k\nabla_{\bar1}\nabla_1g_{k\bar k}
       =h_{1\bar1}+\mathcal C.
\]
The conversion to partial derivatives uses
\[
 \nabla_{\bar1}\nabla_1g_{k\bar k}
       =g_{k\bar k,1\bar1}
           -2\operatorname{Re}\sum_q\overline{\Gamma^q_{1k}}g_{k\bar q,1}
           +O(\lambda).
\]
Rewrite the derivative of $g$ in this term using
$g_{k\bar q,1}=g_{1\bar q,k}+W_{k\bar q,1}-W_{1\bar q,k}+O(1)$ and its conjugate. The first part is absorbed by the off-diagonal squares in \eqref{eq:stw-eigenvalue-basic}, with cost $C\lambda\mathcal F+C\sum_kf_k|g_{1\bar1,k}|$. The $W_{1\bar q,k}$ part is bounded by
$C\lambda\mathcal F+C\sum_{k,p}f_k|v_{pk}|$. For the remaining part use
\[
 2\operatorname{Re}\sum_q\overline{\Gamma^q_{1k}}W_{k\bar q,1}
       =W_{k\bar k,1\bar1}
          -\nabla_{\bar1}\nabla_1W_{k\bar k}+O(\sqrt K).
\]
It cancels the partial second derivative $-W_{k\bar k,1\bar1}$ above. We obtain
\begin{align}
 \sum_k f_k\widetilde\lambda_{k\bar k}
 \geq{}&\mathcal C+sum_kf_k
       (W_{1\bar1,k\bar k}-\nabla_{\bar1}\nabla_1W_{k\bar k})\notag\\
 &-C\left(\sum_kf_k|g_{1\bar1,k}|
                +\sum_{k,p}f_k|v_{pk}|+\lambda\mathcal F\right).
 \label{eq:stw-eigenvalue-torsion-remainder}
\end{align}

The second contraction in \eqref{eq:stw-contraction-derivatives} bounds its negative torsion term. In the $t_1$ part the possible third derivatives are $v_{q1\bar1}$ and their conjugates with $q>1$; all other parts have weights bounded by $Cf_1$. Commute partial derivatives and use
\[
 v_{1\bar1,k}=g_{1\bar1,k}-\chi_{1\bar1,k}-W_{1\bar1,k}.
\]
The exclusions in \cref{lem:stw-torsion-coefficients} ensure that any remaining pure $v_{11}$ carries only the small weight $Cf_1$. Derivatives of the connection contribute second derivatives with the same weighted bounds. It follows that
\[
 \left|\sum_k f_k\nabla_{\bar1}\nabla_1W_{k\bar k}\right|
 \leq C\left(\sum_kf_k|g_{1\bar1,k}|
             +\sum_{k,p}f_k|v_{pk}|+\lambda\mathcal F\right).
\]
For the positive torsion term write $W_{1\bar1}=\sum_p(c^pv_p+\overline{c^p}v_{\bar p})$ with fixed smooth coefficients. Two derivatives give $c^p\sum_kf_kv_{pk\bar k}$ and its conjugate, plus terms bounded by $C(S+\sqrt K\mathcal F)$. Equation \eqref{eq:stw-weighted-third-bound} bounds the former. In this estimate the mixed Hessians can be bounded by $C\lambda$, giving
\[
 \left|\sum_kf_k W_{1\bar1,k\bar k}\right|
       \leq C\left(\sum_{k,p}f_k|v_{pk}|+\lambda\mathcal F\right).
\]
Substitute these estimates in \eqref{eq:stw-eigenvalue-torsion-remainder}, then in \eqref{eq:stw-maximum-second-preliminary}. The third derivatives in the latter are bounded by \eqref{eq:stw-weighted-third-bound} and $\phi'|\partial v|\leq C/\sqrt K$. The resulting linear Hessian terms are absorbed by a small part of $E/K$, with cost $C\mathcal F$. Thus
\begin{equation}\label{eq:stw-key-maximum-inequality}
 \begin{split}
 0\geq{}&\frac{\mathcal C}{\lambda}
       -\sum_kf_k\frac{|a_k|^2}{\lambda^2}
       +\frac{E}{6K}+\phi''\sum_kf_k|V_k|^2
       +\psi''\sum_kf_k|v_k|^2+\psi'\sum_kf_kv_{k\bar k}\\
 &-C\left(\sum_kf_k\frac{|g_{1\bar1,k}|}{\lambda}+\mathcal F\right).
 \end{split}
\end{equation}

\paragraph{Cancellation when the smallest eigenvalue is controlled.}
Fix $0<\delta<1/2$, to be chosen after $D_1,D_2$. First suppose $\lambda_n\geq-\delta\lambda$. Put $I=\{k:f_k>\delta^{-1}f_1\}$, so $1\notin I$. Equation \eqref{eq:stw-maximum-first} and $\phi''=2(\phi')^2$ give
\begin{align*}
 -\sum_{k\notin I}f_k|a_k|^2/\lambda^2
 &\geq-\phi''\sum_{k\notin I}f_k|V_k|^2
              -2(\psi')^2\delta^{-1}f_1K,\\
 -2\delta\sum_{k\in I}f_k|a_k|^2/\lambda^2
 &\geq-2\delta\phi''\sum_{k\in I}f_k|V_k|^2
              -4\delta(\psi')^2\sum_{k\in I}f_k|v_k|^2.
\end{align*}
Choose $\delta$ small enough that $4\delta(\psi')^2\leq\psi''/2$ throughout $[-M,0]$. By \eqref{eq:stw-concavity-square},
\[
 \frac{\mathcal C}{\lambda}
 \geq\sum_{k\in I}\frac{f_k-f_1}{\lambda(\lambda-\lambda_k)}
                         |\nabla_1g_{k\bar1}|^2
 \geq(1-2\delta)\sum_{k\in I}
                 \frac{f_k|\nabla_1g_{k\bar1}|^2}{\lambda^2}.
\]
Here $(1-\delta)/(1+\delta)\geq1-2\delta$.

We need the following quantitative comparison of the two derivatives. For every $\varepsilon>0$, provided $\lambda/K$ is sufficiently large depending on the fixed function $\psi$,
\begin{equation}\label{eq:stw-derivative-cancellation}
 \sum_{k\in I}f_k\frac{|\nabla_1g_{k\bar1}|^2-|a_k|^2}{\lambda^2}
 \geq-\frac{E}{12K}-C\mathcal F
       -\varepsilon C|\psi'|\mathcal F
       -C_\varepsilon|\psi'|\sum_kf_k|v_k|^2.
\end{equation}
Here is a proof keeping the weights explicit. Let $U=\sum_{p>1,q}|v_{pq}|$. Commuting partial derivatives in $g$ gives, for $k>1$,
\[
 \nabla_1g_{k\bar1}-a_k
       =W_{k\bar1,1}-W_{1\bar1,k}+O(\lambda),\qquad
 |W_{k\bar1,1}|+|W_{1\bar1,k}|\leq C(\lambda+U).
\]
The second inequality uses the absence of $v_1$ in $Z_{k\bar1}$: differentiating in direction $1$ introduces no pure $v_{11}$. All mixed Hessians are bounded by $C\lambda$, and every other pure Hessian belongs to $U$.

Use $|a+e|^2-|a|^2\geq-2|a||e|$, then \eqref{eq:stw-maximum-first}. For $k>1$, the pure Hessians in $V_k$ all belong to $U$. If $H_k=\sum_p|v_{p\bar k}|$, the resulting negative terms, divided by $\lambda^2$, are bounded by a constant times
\[
 K^{-1/2}H_k+K^{-1/2}U
       +\frac{U^2}{\lambda\sqrt K}+1
       +|\psi'||v_k|+\frac{|\psi'|}{\lambda}|v_k|U.
\]
We used $H_k\leq C\lambda$ and $\lambda\geq K$ to simplify the cross terms. The weight comparison \eqref{eq:stw-weight-comparability}, symmetry of pure derivatives and Cauchy--Schwarz give $\mathcal F U^2\leq C E$. Consequently, after multiplication by $f_k$ and summation, the first two terms are bounded by any fixed small fraction of $E/K$ plus $C\mathcal F$. The third is at most $CE/(\lambda\sqrt K)$ and is absorbed by another such fraction for large $\lambda/K$. For the last two terms use
\[
 |v_k|\leq\varepsilon+C_\varepsilon|v_k|^2,\qquad
 |v_k|U\leq |v_k|^2+U^2.
\]
The $U^2$ contribution is at most $C|\psi'|E/\lambda$, again absorbable for large $\lambda/K$. Allocating the fractions to sum to $1/12$ proves \eqref{eq:stw-derivative-cancellation}.

Insert this cancellation and the preceding inequalities into \eqref{eq:stw-key-maximum-inequality}. The remaining derivative error satisfies, by \eqref{eq:stw-maximum-first},
\[
 C\sum_kf_k|g_{1\bar1,k}|/\lambda
 \leq\frac{E}{60K}+C\mathcal F
      +\varepsilon C|\psi'|\mathcal F
      +C_\varepsilon|\psi'|\sum_kf_k|v_k|^2,
\]
after Young's inequality and adjustment of constants. Also the torsion contraction satisfies
\[
 \left|\sum_kf_kW_{k\bar k}\right|
    =\left|\sum_it_iZ_{i\bar i}\right|
    \leq C\sum_kf_k|v_k|
    \leq\varepsilon C\mathcal F+C_\varepsilon\sum_kf_k|v_k|^2.
\]
The first inequality uses the same missing gradient index in $Z_{1\bar1}$. Since $\psi'<0$ and $v_{k\bar k}=\lambda_k-\chi_{k\bar k}-W_{k\bar k}$, we conclude, decreasing the remaining coefficient of $E$ if necessary, that
\begin{equation}\label{eq:stw-first-case-closure}
 \begin{split}
 0\geq{}& f_1\left(\frac{\lambda^2}{40K}
                      -2(\psi')^2\delta^{-1}K\right)
    +\left(\frac{\psi''}{2}-C_\varepsilon|\psi'|\right)
                           \sum_kf_k|v_k|^2\\
 &-C_0\mathcal F-\varepsilon C_0|\psi'|\mathcal F
       +|\psi'|\sum_kf_k(\chi_{k\bar k}-\lambda_k).
 \end{split}
\end{equation}
In obtaining the first term we used
$|v_{1\bar1}|^2\geq\lambda^2/2-CK$, which follows from $\chi+W=O(\sqrt K)$.

For large $\lambda$, \cref{lem:stw-logdet-coercivity} bounds the last sum below by $\tau\mathcal F/2$. Choose first $\varepsilon$ with $\varepsilon C_0<\tau/4$. Next choose $D_2$ so that $\psi''/2>C_\varepsilon|\psi'|$, and then choose $D_1$ so that $|\psi'|\tau/4>C_0$ on $[-M,0]$. Finally choose $\delta$ as above. All these choices depend only on the fixed data. Equation \eqref{eq:stw-first-case-closure} then forces
\[
 \lambda^2\leq80\,\delta^{-1}\sup_{[-M,0]}|\psi'|^2K^2.
\]
This is the desired bound in the first case.

\paragraph{The remaining eigenvalue configuration.}
Suppose now $\lambda_n<-\delta\lambda$, keeping the same constants. Since $f_n\geq\mathcal F/n$ and $|\chi+W|\leq C\sqrt K$,
\[
 \frac{E}{6K}\geq\frac{f_n}{6K}|v_{n\bar n}|^2
       \geq\frac{\delta^2\lambda^2}{12nK}\mathcal F-C\mathcal F.
\]
In \eqref{eq:stw-key-maximum-inequality} discard $\mathcal C$ and the $\psi''$ term. Since $\psi$ is now fixed, $|\psi'\sum_kf_kv_{k\bar k}|\leq C\lambda\mathcal F$. Use $g_{1\bar1,k}=a_k+O(\lambda)$ and Young's inequality to bound its error by
$\frac12\sum_kf_k|a_k|^2/\lambda^2+C\mathcal F$. This leaves
\[
 0\geq-\tfrac32\sum_kf_k|a_k|^2/\lambda^2
       +\frac{\delta^2\lambda^2}{12nK}\mathcal F
       +\phi''\sum_kf_k|V_k|^2-C\lambda\mathcal F.
\]
By \eqref{eq:stw-maximum-first} and the scalar inequality
$\tfrac32|a+b|^2\leq2|a|^2+6|b|^2$,
\[
 \tfrac32\sum_kf_k|a_k|^2/\lambda^2
       \leq\phi''\sum_kf_k|V_k|^2+CK\mathcal F.
\]
As $\lambda\geq K$, cancellation and division by $\lambda\mathcal F>0$ give $\lambda/K\leq C$. This finishes both cases. The maximum property of $H$ propagates the bound to all points, and $|\lambda_i|\leq(n-1)\lambda_1$ then bounds every mixed Hessian entry, as asserted.
\end{proof}
