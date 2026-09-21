Run_id: big_model_measures_01

Statement: Verify the two full proofs below of general finite-NPP-measure equations in an arbitrary positive-lower-volume model class of ANY smooth big real theta. BMP is explicit; no independent global PVP or semipositivity/closedness is assumed. The positive-exponent solution is unique in E_phi; the zero-exponent positive scalar is unique, not necessarily the normalized potential. Conditional only on the exact supersolution corollary in the separately audited projection source described in item5. Check every order direction, anti-collapse, attainment of weighted-mass maximum, fixed-measure limits, and retention of subsequence reciprocal exponents.

Exact legitimate internal premises in /Users/mingchen/Non-Kahler/book/author, already reconstructed and independently audited:
1. chapter_envelopes.tex and section_big_relative_foundations.tex: E_phi is defined by u preceq phi and every convex stretching; under BMP and ell=lowerVol(phi)>0 it equals the upper-ordinary-type-volume class. All members have raw MA mass in [ell,M] with ell>0 and M<infinity. They have P_theta[u]=phi and u-sup u<=phi. Constant changes and positive simultaneous scaling of theta,phi,u preserve the appropriate class (volumes and MA scale by lambda^n). SAME-CLASS finite roofs and stretching are available. Strict domination: u in E_phi, v preceq phi, 1_{u<v}MAu<=c1_{u<v}MAv with c<1 implies u>=v. In particular weighted measure order e^-lambda u MAu<=e^-lambda v MAv implies u>=v; constant-scalar equations have unique positive scalar, not necessarily potential.
2. section_big_relative_foundations.tex thm:big-relative-fixed-continuity: u_j in E_phi with a GENUINE smooth L1 limit and MAu_j<=one fixed finite NPP measure implies u in E_phi, capacity convergence and raw weak MA convergence. A fixed dominator alone does NOT prevent collapse. Normalized qpsh compactness, Hartogs lemma, canonical representatives and monotone limits are standard inputs.
3. section_relative_compactness.tex lem:fixed-npp-integrals: uniformly bounded qpsh functions with one lower curvature bound and smooth L1 convergence converge in L1 of a FIXED finite NPP measure. Positive exponentials of upper-bounded theta-psh sequences meet those hypotheses. Do not substitute direct L1(nu) convergence of unbounded potentials. Bounded-carrier decomposition lem:bounded-measure-carrier: any finite NPP mu=f MA_omega(psi), psi bounded omega-psh for a Hermitian omega, f>=0 in L1 of that carrier.
4. section_big_weighted_addition.tex thm:big-weighted-addition, independently passed big_weighted_addition_01 with its conditional weighted-limit dependency discharged by big_weighted_limits_01: u,v in E_phi and MAv<=A MA_omega(psi) for bounded psi imply unique a in E_phi with MAa=e^{a-u}MAu+e^{a-v}MAv. The undamped weighted sum may be infinite; a<=min(u,v) and MAa finite. Its statement also covers one ordinary-type input, not needed here.
5. CONDITIONAL premise, audited separately and not to be re-proved in this run: cor:big-relative-supersolution in /Users/mingchen/Non-Kahler/research/editorial/section_big_relative_projection.tex. For every NONZERO finite NPP measure nu there is Q in E_phi with 0 != e^-Q MAQ <= nu, under exactly the same BMP/big/positive-lower-model-volume hypotheses. This is proved there from minimal-reference existence and an explicitly constructed cross-class rooftop. The present audit may accept exactly this corollary conditionally. All other steps must be checked.

Source attribution: XL26 Theorems6.1--6.2, official https://arxiv.org/html/2601.13446v1, archived /Users/mingchen/Non-Kahler/research/sources/P26.txt. Those conclusions are not allowed premises. The source's extra moving-measure lemma is replaced by continuous approximation in L1 of the fixed dominator; check this directly. Follow normal sequential Rethlas workflow; do not edit manuscript or submitted sources. Persist full findings and final JSON, then stop.

Proof:

\section{General measures with a model reference}
\label{sec:big-model-general-measures}

We retain bounded mass, an arbitrary smooth big real background $\theta$, and a model reference $\varphi$ with positive lower relative volume. As before, every member of $\mathcal E_\varphi$ has mass in $[\ell,M]$. The preceding projection and addition results now give both general-measure equations. The construction follows \cite[Theorems 6.1--6.2]{XL26}; the compactness of the weighted measures is justified directly with a fixed dominating measure.

\begin{theorem}\label{thm:big-model-exponential}
Let $\mu$ be a nonzero finite non-pluripolar measure and let $\lambda>0$. There is a unique $u\in\mathcal E_\varphi$ such that
\[
 \mathrm{MA}_\theta(u)=e^{\lambda u}\mu.
\]
\end{theorem}
\begin{proof}
We first take $\lambda=1$. Suppose initially that
\[
 \mu\leq A\sigma,\qquad
 \sigma=\mathrm{MA}_\omega(\psi),\quad
 \psi\in\PSH(X,\omega)\cap L^\infty(X),
\]
where $\omega$ is Hermitian and $A$ is finite. The supersolution corollary gives $Q\in\mathcal E_\varphi$ with a finite nonzero measure
\[
 \nu_0=e^{-Q}\mu_Q\leq\mu.
\]
Consider
\[
 \mathcal T=\{w\in\mathcal E_\varphi:
              \nu_0\leq e^{-w}\mu_w\leq\mu\}.
\]
All weighted measures here are defined to vanish on the polar sets of their potentials. The family contains $Q$. Exponential order gives $w\leq Q$ for every $w\in\mathcal T$. Also
\[
 \ell\leq\mu_w(X)\leq e^{\sup_Xw}\mu(X),
 \qquad
 \sup_Xw\geq\log\frac{\ell}{\mu(X)}.
\]
These bounds prevent collapse of any sequence in $\mathcal T$.

Let
\[
 \alpha=\sup_{w\in\mathcal T}\int_Xe^{-w}\,\mu_w\leq\mu(X),
\]
and choose $w_j\in\mathcal T$ whose weighted masses tend to $\alpha$. Extract a genuine $L^1$ limit $w$. Since
\[
 \mu_{w_j}\leq e^{\sup_XQ}\mu,
\]
the fixed-dominator theorem gives $w\in\mathcal E_\varphi$, convergence in capacity, and $\mu_{w_j}\rightharpoonup\mu_w$. Put $\nu_j=e^{-w_j}\mu_{w_j}$. After another extraction, these finite measures converge weakly to a measure $\nu$, and
\[
 \nu_0\leq\nu\leq\mu,\qquad \nu(X)=\alpha.
\]

We claim $\mu_w=e^w\nu$. The fixed non-pluripolar integration lemma gives
\[
 \int_X|e^{w_j}-e^w|\,\mathrm{d}\mu\longrightarrow0.
\]
If $f$ is continuous, replacing $e^{w_j}$ by $e^w$ in $\int_Xf e^{w_j}\,\mathrm{d}\nu_j$ therefore has error tending to zero. For the remaining integral, approximate the fixed bounded measurable function $f e^w$ in $L^1(\mu)$ by continuous functions. Since $\nu_j,\nu\leq\mu$, the approximation error is uniform in $j$, while the integrals of each continuous approximation converge by weak convergence. Thus
\[
 \int_Xf\,\mu_{w_j}
 =\int_Xf e^{w_j}\,\mathrm{d}\nu_j
 \longrightarrow\int_Xf e^w\,\mathrm{d}\nu.
\]
This proves the claim. The measure $\nu$ ignores the poles of $w$, so $e^{-w}\mu_w=\nu$. Hence $w\in\mathcal T$ attains the maximum $\alpha$.

If $\mu-\nu$ were nonzero, the supersolution corollary would supply $v\in\mathcal E_\varphi$ with
\[
 0\ne\nu_v=e^{-v}\mu_v\leq\mu-\nu.
\]
In particular $\mu_v\leq e^{\sup_Xv}\mu\leq A e^{\sup_Xv}\sigma$, so the bounded-carrier hypothesis of the addition theorem is satisfied. That theorem gives $a\in\mathcal E_\varphi$ with
\[
 e^{-a}\mu_a=e^{-w}\mu_w+e^{-v}\mu_v=\nu+\nu_v.
\]
The right side is between $\nu_0$ and $\mu$, but its mass exceeds $\alpha$. This contradicts maximality. Therefore $\nu=\mu$, and $w$ solves the equation.

Now let $\mu$ be any nonzero finite non-pluripolar measure. The bounded-carrier decomposition writes
\[
 \mu=f\sigma,\qquad
 \sigma=\mathrm{MA}_\omega(\psi),\quad
 \psi\in\PSH(X,\omega)\cap L^\infty(X),\quad
 0\leq f\in L^1(\sigma).
\]
Set $f_k=\min(f,k)$ and $\mu_k=f_k\sigma$. These measures are nonzero, and the first part gives $u_k\in\mathcal E_\varphi$ with $\mu_{u_k}=e^{u_k}\mu_k$. Exponential order shows that $u_k$ decreases. The uniform bound
\[
 \sup_Xu_k\geq\log\frac{\ell}{\mu(X)}
\]
gives a genuine limit $u$. Moreover $\mu_{u_k}\leq e^{\sup_Xu_1}\mu$. Fixed-dominator continuity gives $u\in\mathcal E_\varphi$ and weak convergence of these measures. On the right,
$e^{u_k}f_k\to e^u f$ in $L^1(\sigma)$ by dominated convergence, with dominator $e^{\sup_Xu_1}f$. Thus $\mu_u=e^u\mu$.

For general $\lambda>0$, apply the exponent-one result in background $\lambda\theta$, with model $\lambda\varphi$ and datum $\lambda^n\mu$, and divide its potential by $\lambda$. Scaling of the class and the Monge--Amp\`ere measure gives the displayed equation. Finally, if $u,v\in\mathcal E_\varphi$ solve it, then $\mu_u=e^{\lambda(u-v)}\mu_v$. The strict domination theorem with constant shifts gives $u=v$.
\end{proof}

\begin{theorem}\label{thm:big-model-normalized}
For every nonzero finite non-pluripolar measure $\mu$, there are $u\in\mathcal E_\varphi$ and $c>0$ such that
\[
 \sup_Xu=0,\qquad \mathrm{MA}_\theta(u)=c\mu.
\]
The scalar $c$ is unique and satisfies
\[
 \frac{\ell}{\mu(X)}\leq c\leq\frac{M}{\mu(X)}.
\]
Uniqueness of the normalized potential is not asserted.
\end{theorem}
\begin{proof}
For each integer $j\geq1$, solve
\[
 \mu_{u_j}=e^{u_j/j}\mu,\qquad u_j\in\mathcal E_\varphi,
\]
using the preceding theorem. Put $S=\sup_Xu_1$ and $w_j=u_1+(j-1)S$. Then $w_j/j\geq u_1$, and hence
\[
 \mu_{w_j}=e^{u_1}\mu\leq e^{w_j/j}\mu.
\]
Exponential order at exponent $1/j$ gives $u_j\leq w_j$. Define
\[
 v_j=u_j-\sup_Xu_j,\qquad
 c_j=e^{(\sup_Xu_j)/j}.
\]
The upper bound just proved and the positive lower mass imply
\[
 \frac{\ell}{\mu(X)}\leq c_j\leq e^S,
 \qquad \mu_{v_j}=c_j e^{v_j/j}\mu\leq e^S\mu.
\]
The envelope identity gives $v_j\leq\varphi$. Normalized compactness supplies a subsequence $j_k$ for which $v_{j_k}\to u$ in $L^1$, with $u$ genuine and $\sup_Xu=0$, and $c_{j_k}\to c>0$. Fixed-dominator continuity gives $u\in\mathcal E_\varphi$ and $\mu_{v_{j_k}}\rightharpoonup\mu_u$.

The bounded quasi-plurisubharmonic functions $e^{v_j/j}$ have a common lower curvature bound. Since $v_j\leq0$,
\[
 0\leq1-e^{v_j/j}\leq-j^{-1}v_j.
\]
The uniform normalized $L^1$ estimate shows convergence to one in smooth-volume $L^1$. The fixed non-pluripolar integration lemma then gives convergence to one in $L^1(\mu)$. Consequently $c_{j_k}e^{v_{j_k}/j_k}\mu\to c\mu$ in total variation. The retained reciprocal exponents are $1/j_k$, so the limit equation is $\mu_u=c\mu$. Integrating it gives the stated interval for $c$. Uniqueness of the positive scalar follows from \cref{thm:big-relative-domination}, as explained after that theorem.
\end{proof}

These theorems complete the general-measure existence assertions for an arbitrary model reference in the stated bounded-mass regime. The equations themselves give finite measures. The solution belongs to the envelope class $\mathcal E_\varphi$; the stronger conclusion $u\simeq\varphi$ for $L^p$ data requires a relative boundedness estimate. That estimate is a separate step.
