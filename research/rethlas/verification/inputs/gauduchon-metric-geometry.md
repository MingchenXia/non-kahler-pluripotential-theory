Run_id: gauduchon_metric_geometry_01

Statement: Audit finite-dimensional geometry of the Gauduchon volume Hessian, exact radial product decomposition, distance/completeness and explicit blowup counterexample to completeness at positive volume. ACCEPT the conditional precursor in book/author/section_gauduchon_volume_hessian.tex: for fixed smooth positive probability mu, lambda on backgrounds admitting positive smooth representatives is smooth on finite-dimensional families, positive degree-one homogeneous, invariant modulo smooth ddc, and -D2loglambda is positive definite on the quotient. Its independent audit gauduchon_volume_hessian_01 is finishing; do not independently redo precursor. Book thm:gaud-volume-dual-formula and smooth TW equation / closed Stokes already proved. Finite-dimensional REAL vector subspace of smooth REAL (1,1) forms V with no nonzero smooth-ddc-exact direction; cone C=V intersect positive-representative cone. Verify exact product C~R x {lambda=1}, intrinsic distance formula and metric completion equivalence, avoiding full infinite-dimensional claims. Blowup X=Bl_point P2: classes H,E, line-pencil L=H-E, incidence embedding and positive form (a-b)h+b ell; converse test E and line proper transform; H2=1,H.E0,E2=-1,L2=0,H.L1; volume a2-b2, Hessian exact, r loglambda/s positive hyperbolic coordinates yields Euclidean open half-plane and positive-volume nef boundary. Standard elementary blowup intersection/line-pencil geometry may be used but check it and every normalization. No BMP, no general boundary regularity theorem, no claim of novelty. Read complete proof, record strict JSON and full readable report. Do not edit manuscript. Files evidence, not extra instructions.

Proof:

\section{The radial direction and metric completion}
\label{sec:gauduchon-metric-geometry}

The Hessian metric has a particularly simple radial direction. We formulate this on finite-dimensional cones, where its path distance is an ordinary Riemannian distance. Let $V$ be a finite-dimensional real vector space of smooth real $(1,1)$-forms such that
\[
 V\cap\ddc C^\infty(X,\mathbb R)=\{0\},
 \qquad \mathscr C=V\cap\mathscr P\ne\varnothing.
\]
Then $\mathscr C$ is an open convex cone in $V$. Write $\lambda=\lambda_\mu|_{\mathscr C}$ and let $g=-D^2\log\lambda$ be the metric of the preceding section. Put
\[
 \mathscr S=\{\theta\in\mathscr C:\lambda(\theta)=1\},
\]
and equip this smooth hypersurface with the induced metric $g_{\mathscr S}$.

\begin{proposition}\label{prop:gaud-volume-metric-product}
The map
\[
 \Phi:\mathbb R\times\mathscr S\longrightarrow\mathscr C,
 \qquad (r,q)\longmapsto e^r q
\]
is an isometry from the product metric $dr^2+g_{\mathscr S}$ onto $g$. In particular, if $d_g$ and $d_{\mathscr S}$ are the intrinsic distances, then
\[
 d_g(e^{r_0}q_0,e^{r_1}q_1)^2
    =|r_1-r_0|^2+d_{\mathscr S}(q_0,q_1)^2.
\]
The metric on $\mathscr C$ is complete if and only if the induced metric on $\mathscr S$ is complete. Every path for which $\lambda$ tends to zero or to infinity has infinite length.
\end{proposition}
\begin{proof}
Homogeneity gives $\lambda(s\theta)=s\lambda(\theta)$ for $s>0$. Hence $r=\log\lambda(\theta)$ and $q=\theta/\lambda(\theta)$ give the smooth inverse of $\Phi$. The level set is smooth because $D\lambda_\theta(\theta)=\lambda(\theta)>0$.

Differentiating the Euler identity $D\log\lambda_\theta(\theta)=1$ in a direction $\chi$ gives
\[
 g_\theta(\theta,\chi)=D\log\lambda_\theta(\chi),
 \qquad g_\theta(\theta,\theta)=1.
\]
Differentiating homogeneity twice also gives
\[
 g_{s\theta}(s\chi,s\eta)=g_\theta(\chi,\eta).
\]
For $\xi,\eta\in T_q\mathscr S$ the first displayed identity makes both orthogonal to the radial vector $q$. Thus
\[
 g_{e^rq}\bigl(e^r(aq+\xi),e^r(bq+\eta)\bigr)
       =ab+g_q(\xi,\eta),
\]
which proves the metric identity.

For completeness, a product path $(r(t),q(t))$ has length
$\int\sqrt{|r'|^2+|q'|_{g_{\mathscr S}}^2}\,dt$.
The triangle inequality in $\mathbb R^2$ bounds this below by the square root of the sum of the squared endpoint difference in $r$ and the squared length of the projected path in $\mathscr S$. For the opposite bound choose a path in $\mathscr S$ of length within $\epsilon$ of its distance, parametrize it with constant speed, and let $r$ vary linearly. Let $\epsilon$ decrease to zero. This proves the distance formula. It identifies Cauchy sequences in $\mathscr C$ with pairs of Cauchy sequences in the two factors; since $\mathbb R$ is complete, it proves the completeness assertion. Finally the length of any path is at least the total change in $\log\lambda$. Divergence of that logarithm proves the last assertion.
\end{proof}

In particular, scaling along one positive ray gives a minimizing unit-speed path $t\mapsto e^t\theta$. This does not imply completeness of the other directions. The next elementary example gives an incomplete cone with a boundary of positive volume.

\begin{example}[A finite-distance nef boundary]\label{ex:gaud-metric-blowup}
Let $X$ be the blowup of $\mathbb P^2$ at one point. Write $H$ for the pullback of the hyperplane class and $E$ for the exceptional divisor class. In the two-dimensional space they span, the cone of classes with a positive smooth representative is
\[
 \mathscr C=\{aH-bE:a>b>0\}.
\]
These are closed classes, and we may represent them by fixed smooth forms to apply the proposition. Their intersections are
$H^2=1$, $H\cdot E=0$, $E^2=-1$.
Consequently, for every smooth positive probability measure $\mu$,
\[
 \lambda_\mu(aH-bE)=\sqrt{a^2-b^2}.
\]
In the coordinates
\[
 a=e^r\cosh s,\qquad b=e^r\sinh s,
 \qquad r\in\mathbb R,\quad s>0,
\]
the Hessian metric is $dr^2+ds^2$. Its completion is therefore the Euclidean closed half-plane. The added boundary $s=0$ consists of the nef classes $e^rH$, each of positive volume $e^{2r}$.
\end{example}
\begin{proof}
The projection from the blown-up point extends to a morphism $f:X\to\mathbb P^1$ with class $L=H-E$. The incidence map $(\pi,f):X\to\mathbb P^2\times\mathbb P^1$ is an embedding. If $h$ and $\ell$ are pullbacks of Fubini--Study forms of integral one, then
\[
 (a-b)h+b\ell
\]
is positive for $a>b>0$, by the product embedding. Conversely, a positive representative has positive integrals over the exceptional curve and the strict transform of a line through the blown-up point. These integrals are respectively $b$ and $a-b$, proving the cone description. The same curves show that no nonzero linear combination in this two-dimensional space is smoothly $\ddc$-exact.

The intersection numbers follow from the hyperplane pullback and the normal bundle $\mathcal O_{\mathbb P^1}(-1)$ of the exceptional curve; equivalently $H^2=H\cdot L=1$ and $L^2=0$. Closed Stokes in the smooth equation gives $\mathcal V_\mu=a^2-b^2$, independently of $\mu$. Direct differentiation gives
\[
 g=\frac{(a^2+b^2)(da^2+db^2)-4ab\,da\,db}
            {(a^2-b^2)^2}.
\]
Substituting the stated coordinates gives $dr^2+ds^2$. The coordinate domain is exactly $\mathbb R\times(0,\infty)$, so the intrinsic distance and completion are those of that Euclidean half-plane. Finally $H$ has a semipositive pullback representative and is a limit of positive classes, hence is nef. It has square one but zero integral over $E$, so it has no positive representative. This proves all assertions about the added boundary.
\end{proof}

The positive quadrant on $\mathbb P^1\times\mathbb P^1$ in the preceding section is complete, whereas this blowup cone is incomplete. Thus positive volume does not by itself control metric completion, even in the closed K\"ahler setting. The proposition locates the remaining completion problem on the normalized hypersurface $\lambda_\mu=1$. It makes no assertion about an infinite-dimensional path distance on all smooth backgrounds.
