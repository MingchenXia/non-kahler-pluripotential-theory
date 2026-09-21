Run_id: big_model_lp_01

Statement: Verify the entire staged relative boundedness section below: (1) concave-envelope contact for u in E_phi WITHOUT already assuming ordinary type phi, for a globally bounded-slope concave chi; (2) a uniform relative depth bound from one uniform m-th datum moment with m>2n+1; (3) the ordinary-type Lp refinement of both general-measure equations. ANY smooth big theta, BMP and positive lower volume of model phi. Check the unbounded two-potential convex chain and local exact theta-psh truncations, all energy/normalization inequalities, Tonelli, the absolutely-continuous ODE, all parameter uniformities, and the absence of circular ordinary-type assumptions.

Exact legitimate internal premises in /Users/mingchen/Non-Kahler/book/author, already reconstructed and independently audited:
1. chapter_envelopes.tex and section_big_relative_foundations.tex: E_phi under BMP and ell=lowerVol(phi)>0 is the envelope class defined by all convex stretching competitors and ordinary upper singularity bound preceq phi. It equals the upper-ordinary-type-volume class. Every member has MA mass in [ell,M], 0<ell<=M<infinity. E_phi is upward stable when h<=target preceq phi. Model phi=P_theta[phi]<=V_theta<=0. For each p in E_phi, P_theta[p]=phi and p-sup p<=phi. SAME-CLASS Q_b(u,phi) belongs to E_phi for u<=phi in E_phi and all b>=1. Strict/zero domination applies when first potential is in E_phi and second is preceq phi.
2. section_big_general_contact.tex: a genuine envelope of a finite-a.e. quasi-continuous obstacle in ANY smooth BIG background has NPP MA carried by contact. Ordered contact for two ordered theta-psh potentials holds; all NPP measures ignore every pluripolar set. Locality on strict comparison sets and bounded products/continuity apply in nonclosed backgrounds. Do not assume a general model has any open locally bounded locus.
3. section_big_minimal_moments.tex lem:big-concave-envelope proof provides the following bounded LOCAL chain calculation, checked independently in big_minimal_moments_01: for locally bounded theta-psh p<=r and C1,1loc convex tau with 0<tau'<=1, w=r+tau(p-r) is theta-psh, theta_w>=tau'(p-r)theta_p+(1-tau'(p-r))theta_r, and MAw>=tau'(p-r)^n MAp. This follows from local convolution after a common correction, with vanishing smooth curvature errors and bounded capacity continuity of derivative factors. It does NOT require theta semipositive or closed. The original lemma's ordinary-minimal-type global conclusion is NOT assumed for arbitrary models; the present proof must build the unbounded extension.
4. Standard local Skoda integrability and normalized qpsh compactness imply uniform exponential and every finite smooth-volume moment on sup-normalized theta-psh potentials for fixed smooth theta. Standard Holder, Tonelli, regularity and integration of absolutely-continuous scalar functions are available. Ordinary type means bounded difference off common poles, not equality of raw masses.
5. CONDITIONAL premise only for existence in the final corollary: the exact thm:big-model-exponential and thm:big-model-normalized in /Users/mingchen/Non-Kahler/research/editorial/section_big_model_measures.tex, being audited in big_model_measures_01. Under these same big/BMP/model-positive-lower-volume hypotheses, every nonzero finite NPP datum has a unique positive-exponent solution in E_phi and a normalized zero-exponent solution in E_phi with unique positive scalar. No ordinary-type conclusion may be assumed. The first lemma and moment proposition have no conditional dependence on those existence theorems.

Source attribution XL26 Corollary6.1 and the relative-estimate method in Theorem5.1, https://arxiv.org/html/2601.13446v1, archived /Users/mingchen/Non-Kahler/research/sources/P26.txt. Do NOT import the Lp ordinary-type conclusion or any relative L-infinity theorem: the supplied proof must establish it. In particular do not assume MA max(u,phi-j)<=datum; that false truncation inference is expressly avoided. Follow normal sequential Rethlas workflow; do not edit manuscript or submitted TeX. Persist every finding and final JSON, then stop.

Proof:

\section{Relative boundedness for \texorpdfstring{$L^p$}{Lp} data}
\label{sec:big-model-lp}

The general-measure theorem gives a solution in $\mathcal E_\varphi$. We now show that $L^p$ data, with $p>1$, force ordinary singularity type $\varphi$. We keep the same bounded-mass and positive lower reference-volume assumptions. The estimate will be applied directly to a relative-class potential: truncating it by $\max(u,\varphi-j)$ would introduce a contact measure not controlled by the original density.

\begin{lemma}\label{lem:big-model-concave-envelope}
Let $u\in\mathcal E_\varphi$, $u\leq\varphi$, and let
$\chi:\mathbb R_{\leq0}\to\mathbb R_{\leq0}$ be increasing and concave, with $\chi(0)=0$. Suppose it is $C^{1,1}$ on compact intervals and
\[
 1\leq\chi'\leq L<\infty.
\]
Then the envelope
\[
 p=P_\theta(\varphi+\chi(u-\varphi))
\]
belongs to $\mathcal E_\varphi$, and
\[
 \mu_p\leq\mathbf1_{\{p=\varphi+\chi(u-\varphi)\}}
                 \chi'(u-\varphi)^n\mu_u.
\]
The obstacle and the contact set are defined off the polar indeterminacy sets, which all these measures ignore.
\end{lemma}
\begin{proof}
For $t\leq0$ the derivative bounds give $Lt\leq\chi(t)\leq t$. Thus
\[
 Q_L(u,\varphi)\leq p\leq u\leq\varphi.
\]
The lower competitor belongs to $\mathcal E_\varphi$ by stretching, so $p$ is genuine and belongs to that class by upward stability. The obstacle is finite and quasi-continuous off poles, and the contact theorem applies.

Let $\tau=\chi^{-1}$. It is convex, with $L^{-1}\leq\tau'\leq1$. We justify the transformation
\[
 w=\varphi+\tau(p-\varphi)
\]
without assuming any open set on which $\varphi$ is locally bounded. On a coordinate ball choose a smooth $q$ with $\theta+\ddc q\geq0$. The functions
\[
 p_m=\max(p,q-m),\qquad
 \varphi_m=\max(\varphi,q-m)
\]
are locally bounded $\theta$-plurisubharmonic functions, and $p_m\leq\varphi_m$. The bounded convex chain calculation in the proof of \cref{lem:big-concave-envelope} applies to
$w_m=\varphi_m+\tau(p_m-\varphi_m)$ and gives
\[
 \theta_{w_m}\geq\tau'(p_m-\varphi_m)\theta_{p_m}
       +(1-\tau'(p_m-\varphi_m))\theta_{\varphi_m}\geq0,
 \qquad
 \mu_{w_m}\geq\tau'(p_m-\varphi_m)^n\mu_{p_m}.
\]
In that calculation the two current coefficients add to one; no positivity of $\theta$ itself is used. Its smoothing argument applies on each smaller ball to these locally bounded potentials and the continuous derivative factors.

The scalar function $(s,t)\mapsto t+\tau(s-t)$ on $s\leq t$ is nondecreasing in each variable. Consequently $w_m$ decreases as $m$ increases. Since $p\leq p_m\leq w_m\leq\varphi_m$, it has a genuine local limit. Off the poles this limit is exactly $w$ as displayed above. The local limits therefore agree canonically on overlaps and define a global $\theta$-plurisubharmonic function.

On $D_m=\{p>q-m\}$ neither $p$ nor $\varphi$ is truncated. Thus $w_m=w$, and plurifine locality transfers the product inequality to $D_m$. These sets exhaust the complement of the poles of $p$, locally on the ball. All products ignore the discarded polar set, so
\[
 \mu_w\geq\tau'(p-\varphi)^n\mu_p.
\]
The obstacle bound gives $w\leq u$, with equality on the contact set of $p$. Ordered contact, the identity
$\tau'(p-\varphi)=1/\chi'(u-\varphi)$ there, and contact support of $\mu_p$ prove the assertion.
\end{proof}

\begin{proposition}\label{prop:big-model-moment-bound}
Let $\mu$ be a finite non-pluripolar measure. Suppose, for some real $m>2n+1$,
\[
 A_m:=\sup_{\substack{v\in\PSH(X,\theta)\\\sup_Xv=0}}
             \int_X(-v)^m\,\mathrm{d}\mu<\infty.
\]
There is a finite constant $C$, depending only on
$n,\ell,M,m,\mu(X)$ and $A_m$, such that every $u\in\mathcal E_\varphi$ with $\sup_Xu=0$ and $\mu_u\leq\mu$ satisfies
\[
 \varphi-C\leq u\leq\varphi.
\]
\end{proposition}
\begin{proof}
The envelope identity gives $u\leq\varphi\leq0$. Put $x=\varphi-u$, defined off poles, and $N=2n+1$. H\"older's inequality gives the uniform first-moment bound
\[
 B:=\int_Xx\,\mu_u
 \leq\int_X(-u)\,\mathrm{d}\mu
 \leq\mu(X)^{1-1/m}A_m^{1/m}=:A_1.
\]
Let $H(t)=\mu_u(\{x>t\})$ and
$T=\sup\{t\geq0:H(t)>0\}$, with $T=0$ if the set is empty. At this point $T$ may be infinite. If $T<\infty$, zero domination applied to $\varphi-t$ for $t>T$ gives $u\geq\varphi-T$. It is therefore enough to bound $T$. We may assume $T>1$ and choose any $S$ with $1<S<T$.

Define, for $t\geq0$,
\[
 g(t)=
 \begin{cases}
  ((1+t)^{3/2}H(t))^{-1},&0\leq t\leq S,\\
  (1+t)^{-3/2},&t>S,
 \end{cases}
 \qquad F(t)=1+\int_0^t g(s)\,\mathrm{d}s,
\]
and set $W(t)=\int_0^t F(s)^{1/N}\,\mathrm{d}s$ and $\chi(-t)=-W(t)$. Since $H(S)>0$, $F$ is bounded on the entire half-line, although its bound may depend on $S$ and $u$. It is locally Lipschitz and nondecreasing. Thus $\chi$ has bounded derivative, is increasing and concave, and meets the preceding lemma's hypotheses. Also $W(t)\geq t$ and $W(t)\leq tF(t)^{1/N}$.

Tonelli's theorem and $H(t)\leq M$ give a bound independent of $S$ and $u$:
\[
 \int_X F(x)\,\mu_u
 =\mu_u(X)+\int_0^\infty g(t)H(t)\,\mathrm{d}t
 \leq3\max(1,M)=:K.
\]
Let $p=P_\theta(\varphi-W(x))\in\mathcal E_\varphi$. On its contact set the preceding lemma bounds its measure by $F(x)^{n/N}\mu_u$. Hence, using $N=2n+1$,
\[
 \begin{split}
 \int_X(\varphi-p)^{1/2}\,\mu_p
 &\leq\int_X x^{1/2}F(x)^{(n+1/2)/N}\,\mu_u\\
 &\leq\left(\int_Xx\,\mu_u\right)^{1/2}
          \left(\int_XF(x)\,\mu_u\right)^{1/2}
 \leq\sqrt{KB}.
 \end{split}
\]
The identity $P_\theta[p]=\varphi$ implies $p-\sup_Xp\leq\varphi$. Since $p\leq\varphi\leq0$, the last integral is at least $\ell\sqrt{-\sup_Xp}$. Consequently
\[
 0\leq-\sup_Xp\leq KA_1/\ell^2=:D.
\]
Using $W(x)\leq\varphi-p\leq-p$, and applying the assumed moment bound to $p-\sup_Xp$, we obtain
\begin{equation}\label{eq:big-model-weight-moment}
 \int_XW(x)^m\,\mathrm{d}\mu
 \leq2^{m-1}\bigl(A_m+D^m\mu(X)\bigr)<C_0,
\end{equation}
where we choose $C_0=1+2^{m-1}(A_m+D^m\mu(X))$. This constant is independent of $S$ and $u$.

For $0<t\leq S$, Chebyshev's inequality and $\mu_u\leq\mu$ give
\[
 H(t)\leq C_0W(t)^{-m},
 \qquad
 F'(t)\geq\frac{W(t)^m}{C_0(1+t)^{3/2}}
 \quad\text{for almost every }t.
\]
Since $W'=F^{1/N}$, the derivative of $(W')^{N+1}$ is at least
\[
 \frac{N+1}{NC_0}\,
 \frac{W^mW'}{(1+t)^{3/2}}.
\]
All functions being differentiated are absolutely continuous on compact intervals. Integrating from zero to $t$, using $W(0)=0$, gives
\[
 (W'(t))^{N+1}
 \geq\frac{N+1}{NC_0(m+1)}
        \frac{W(t)^{m+1}}{(1+t)^{3/2}}.
\]
In particular
\[
 W'(t)\geq c_0(1+t)^{-\gamma}W(t)^\kappa,
 \quad
 \gamma=\frac{3}{2(N+1)}<1,\quad
 \kappa=\frac{m+1}{N+1}>1,
\]
with $c_0>0$ independent of $S,u$. Integrating the derivative of $W^{1-\kappa}$ on $[1,S]$ yields
\[
 (\kappa-1)c_0\int_1^S(1+t)^{-\gamma}\,\mathrm{d}t
 \leq W(1)^{1-\kappa}-W(S)^{1-\kappa}\leq1,
\]
because $W(1)\geq1$. The integral diverges as $S\to\infty$. It follows that every $S<T$ has a common finite upper bound, and hence so does $T$. The zero-domination argument at the start now gives $u\geq\varphi-C$. The cases $T\leq1$, including $B=0$, were already covered.
\end{proof}

\begin{corollary}\label{cor:big-model-lp-type}
Let $\mathrm{d}V$ be a smooth positive volume form and let $0\leq f\in L^p(X,\mathrm{d}V)$, with $p>1$ and $\int_Xf\,\mathrm{d}V>0$.
For $\lambda>0$, the solution in \cref{thm:big-model-exponential} to
\[
 \mathrm{MA}_\theta(u)=e^{\lambda u}f\,\mathrm{d}V
\]
satisfies $u\simeq\varphi$. Every normalized solution in $\mathcal E_\varphi$ of
\[
 \mathrm{MA}_\theta(u)=cf\,\mathrm{d}V,\qquad c>0,
\]
also satisfies $u\simeq\varphi$. In particular both existence statements can be made in the ordinary singularity type of $\varphi$.
\end{corollary}
\begin{proof}
Uniform Skoda integrability for normalized $\theta$-plurisubharmonic functions gives uniform moments of every finite order against $\mathrm{d}V$. H\"older's inequality therefore implies, for every finite $m$,
\[
 \sup_{\substack{v\in\PSH(X,\theta)\\\sup_Xv=0}}
       \int_X(-v)^m f\,\mathrm{d}V<\infty.
\]
Choose $m>2n+1$. For the positive-exponent solution, set $S=\sup_Xu$ and $v=u-S$. Then $v\in\mathcal E_\varphi$, $\sup_Xv=0$, and
\[
 \mu_v=e^{\lambda u}f\,\mathrm{d}V
 \leq e^{\lambda S}f\,\mathrm{d}V.
\]
The proposition applied to this fixed dominating measure shows that $v$, and hence $u$, has ordinary type $\varphi$. For the normalized equation apply it to the measure $cf\,\mathrm{d}V$. This proves the ordinary-type conclusion of \cite[Corollary 6.1]{XL26} directly from the general-measure solutions and the relative estimate above.
\end{proof}

The derivative bound on the concave weight was allowed to depend on the chosen depth $S$. The moment estimate, the normalization of its envelope, and the final depth bound were independent of that derivative bound. This is what permits the argument to start with $u\in\mathcal E_\varphi$ without first assuming $u\simeq\varphi$.
