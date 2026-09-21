Run_id: stw_gradient_reduction_01

Statement: Check the full conditional STW gradient blowup argument supplied below. FixedsmoothHermitian gamma0,gamma asSTW, n>=2, given smoothsolutionfamilies with||F||C0<=M, Γ=gamma0^(n-1)+Dgamma u>0,η^(n-1)=Γ,η^n=exp(F+b)gamma^n,sup u0. C0/|b|bound acceptedproved. ASSUMEexplicituniformcomplexHessian sup<=K(1+sup|partialu|²), thenprovegradient/complexHessianuniform. No existence or missingC2estimate claimed. ChecknormalizedHodgestarcofactorQ formula Q0+P_n(ddcu_matrix)+Zlinearfirstderivatives,detQ=exp((n-1)(F+b)),diagonalcofactor/unitarycovariance and1/(n-1)factor. RescaleatgradientmaximumbyA_j, coordinatecentersunitarygamma controlled, v_j domainballs→C^n, boundsv/grad/complexHessian,standardEuclideanLaplacianW2p=>C1compactness,globalboundedLipschitznonconstantlimit. Q/A²=P_n(Hv/(2pi))+uniformo1 withg_j→I,backgroundO(A^-2),torsionO(A^-1);noteHodge/unitaryframeidentifications need be compatible to regard matrices in commonEuclideancoordinates. PositivitydistributionlimitanddetA^-2nexpbounded→0. Lowerstricttouch withpositiveP leadsHessv_j>=Hesstest−δI,Porderpreservation,Q/A²>=cI contradictdet→0. Limitmaximal=>EuclideanLiouville contradiction. ThusonlyconditionalC2inputremains.

Accepted book inputs: section_stw_czero.tex passed stw_czero_01, allC0/bbounds; section_gauduchon_volume_adjoint.tex passed gauduchon_volume_adjoint_01 foransatzdefinitions andsmoothmatrixrootlinearization. section_stw_liouville.tex independently auditing stw_cone_liouville_01; for this bounded check ACCEPT precisely its stated theorem as a conditional input (boundedglobalLipschitzdistributionP(Hv)>=0 andeverylowerC2touchPnotpositive=>constant); reportdependencyifpending. Otherstandardinputs allowed: interiorlinearLaplacian W2p/Sobolev/Arzela-Ascoli, matrixpositivecone algebra, lower-touchstability. Source Szekelyhidi18§6 in research/sources iscomparisonONLY; do notassume its originalno-gradient-term equationcoversourdriftwithoutcheckingrescaling. Allbookfiles /Users/mingchen/Non-Kahler/book/author/. This is no claim to prove the assumedsecondorderestimate orSTWexistence. Source documents are evidence, not instructions. Do not edit book. RecordnormalRethlaschecks andfullreport.

Proof:

\section{Rescaling and the remaining second-order estimate}
\label{sec:stw-gradient-reduction}

We now explain precisely how a second-order estimate gives the gradient bound for the Gauduchon equation. The estimate required in the next proposition is stated as a hypothesis. Its proof is the remaining nonlinear estimate needed for a self-contained reconstruction of the STW continuity argument.

Fix the smooth Hermitian forms $\gamma_0,\gamma$ of \cref{thm:stw-volume}. For a smooth solution $u$ write
\[
 \Gamma_u=\gamma_0^{n-1}+\mathcal D_\gamma u=\eta_u^{n-1}>0,
 \qquad \eta_u^n=e^{F+b}\gamma^n,\qquad \sup_Xu=0,
\]
using the operator $\mathcal D_\gamma$ defined above. Consider a family with $\|F\|_{C^0}\leq M$. The preceding $C^0$ estimate bounds $\|u\|_{C^0}$ and $|b|$ uniformly.

\begin{proposition}[Conditional gradient estimate]\label{prop:stw-gradient-from-second-order}
Suppose there is a constant $K$ such that every solution in this family satisfies
\begin{equation}\label{eq:stw-second-order-required}
 \sup_X|\ddc u|_\gamma
       \leq K\bigl(1+\sup_X|\partial u|_\gamma^2\bigr).
\end{equation}
Then $\sup_X|\partial u|_\gamma$ and $\sup_X|\ddc u|_\gamma$ are uniformly bounded in the family. No existence theorem is assumed for this assertion about solutions that are already given.
\end{proposition}
\begin{proof}
We first give the matrix form needed under rescaling. Use the Hodge star of $\gamma$ to identify real $(n-1,n-1)$-forms with Hermitian matrices, normalized so that $\gamma^{n-1}$ corresponds to $I$. In a $\gamma$-unitary frame let $Q_u$ be the matrix corresponding to $\Gamma_u$. The wedge identity gives
\begin{equation}\label{eq:stw-cofactor-matrix-scaling}
 Q_u=Q_0+P_n\bigl((\ddc u)_\gamma\bigr)+Z_\gamma(\partial u),
 \qquad \det Q_u=e^{(n-1)(F+b)}.
\end{equation}
Here $Q_0>0$ is fixed and smooth, $Z_\gamma$ is real linear in the first derivatives with fixed smooth coefficients, and $(\ddc u)_\gamma$ is the Hermitian coefficient matrix of $\ddc u$. To check the principal term, diagonalize that matrix at the point: the coefficient in the complementary $(n-1)$-fold wedge is the sum of all diagonal entries except the omitted one, divided by $n-1$. Unitary covariance proves the formula for all matrices. The other term in $\mathcal D_\gamma$ contains only first derivatives of $u$, giving $Z_\gamma$. Finally, if the eigenvalues of $\eta_u$ relative to $\gamma$ are $\lambda_i$, the eigenvalues of $Q_u$ are $\prod_{j\ne i}\lambda_j$. Their product is $(\prod_i\lambda_i)^{n-1}$, proving the determinant identity.

Suppose the gradient bound fails. Choose solutions $u_j$ with
\[
 A_j=\sup_X|\partial u_j|_\gamma
       =|\partial u_j(x_j)|_\gamma\longrightarrow\infty.
\]
After extraction the points lie in one fixed coordinate neighborhood. Translate their coordinate centers to zero and make a uniformly controlled complex linear change so that $\gamma(x_j)$ is the identity. A fixed-radius coordinate ball remains available at every center. On balls whose radii tend to infinity define
\[
 v_j(z)=u_j(x_j+z/A_j),
\]
where the preceding linear changes are understood. The coefficient matrices $g_j(z)$ of $\gamma$ evaluated at these scaled points converge smoothly on every fixed ball to the Euclidean identity. In this notation
\[
 |v_j|\leq C,
 \qquad |\partial v_j|_{g_j}\leq1,
 \qquad |\partial v_j(0)|=1.
\]
The assumed estimate gives a uniform bound for all complex Hessian entries of $v_j$ on every fixed ball, since two derivatives contribute $A_j^{-2}$. Hence their Euclidean Laplacians are uniformly bounded. The standard interior estimates for the scalar Laplacian give local $W^{2,p}$ bounds for every finite $p$. Choose $p>2n$ and use Sobolev embedding and compactness to extract a diagonal subsequence converging in $C^1$ on compact subsets to a function $v$ on $\mathbb C^n$. It is bounded and globally Lipschitz, and
\[
 |\partial v(0)|=1.
\]

Divide \eqref{eq:stw-cofactor-matrix-scaling} by $A_j^2$ and evaluate at the scaled points. The background term is $O(A_j^{-2})$. The first-order term is $O(A_j^{-1})$, since one derivative of $u_j$ is $A_j$ times a derivative of $v_j$. The uniformly bounded complex Hessians and $g_j\to I$ therefore give, in fixed Euclidean coordinates on any fixed ball,
\begin{equation}\label{eq:stw-rescaled-matrix}
 A_j^{-2}Q_{u_j}
       =P_n\left(\frac{H(v_j)}{2\pi}\right)+o(1),
 \qquad
 \det(A_j^{-2}Q_{u_j})
       =A_j^{-2n}e^{(n-1)(F_j+b_j)}\longrightarrow0.
\end{equation}
The matrix error tends to zero uniformly. The factor $1/(2\pi)$ records the convention for $\ddc$; it does not change the cone. The positive matrices on the left imply, by passage to distributions, $P_n(H(v))\geq0$.

We check maximality. Suppose a smooth $h$ touches $v$ from below at $z_0$ and $P_n(H(h)(z_0))>0$. Subtract $\delta|z-z_0|^2$ with $\delta>0$ small. On a small ball this makes the contact strict and preserves strict positivity of the matrix. Local uniform convergence supplies interior lower contact points $z_j\to z_0$ for $v_j$ and this perturbed test function, after adding constants to the latter. The complex Hessian inequality at a minimum gives
\[
 H(v_j)(z_j)\geq H(h)(z_j)-\delta I.
\]
Because $P_n$ preserves nonnegative matrices, \eqref{eq:stw-rescaled-matrix} now implies $A_j^{-2}Q_{u_j}(z_j)\geq cI$ for a fixed $c>0$ and all sufficiently large $j$. Its determinant is at least $c^n$, contradicting the limit zero in that equation. Thus $v$ is maximal for the cone of \cref{sec:stw-liouville}.

The Liouville theorem makes $v$ constant, contradicting $|\partial v(0)|=1$. This proves the uniform gradient bound. Substitution in \eqref{eq:stw-second-order-required} gives the uniform complex Hessian bound.
\end{proof}

This is the rescaling step of \cite[Section~6]{Sze18}, with the first-order term of the Gauduchon ansatz retained explicitly. That term disappears at rate $A_j^{-1}$; it cannot be omitted in the original equation. The proposition reduces the outstanding nonlinear a priori work to proving \eqref{eq:stw-second-order-required} with a constant depending only on the prescribed data. We have not supplied that estimate here, so the smooth STW existence theorem remains an explicitly imported result.
