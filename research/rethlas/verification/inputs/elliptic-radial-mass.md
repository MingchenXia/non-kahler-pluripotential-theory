Run_id: elliptic_radial_mass_01

Run scope: Bounded verification through the normal Rethlas workflow. The parent owns manuscript edits, build and release. Restrict writes to normal verifier tools, memory and results. Do not alter book/editorial/blueprint/status/changelog files, frozen inputs, original references or historical reports. Do not commit or push.

Statement: Verify the complete proposition and proof below, including the sharp infimum 8 and its nonattainment within the stated smooth strictly positive class. The class consists of separated potentials f(t)+pi^*v on the book's elliptic threefold, where f is 4*pi-periodic and v is any smooth real function on P^1 x P^1. This is a restricted-class calculation, not an assertion about all potentials; the unrestricted lower mass is zero. No novelty is claimed and no result of Popovici is used.

Exact geometric setup: Let Omega={[z:w] in P^3: z,w in C^2 are both nonzero}, q=e^(2*pi), g[z:w]=[z:qw], X=Omega/<g>. This is a connected compact complex threefold, with holomorphic submersion pi:X->B=P^1 x P^1 given by [z:w]->([z],[w]). Each fiber is C/(2*pi*Z+2*pi*i*Z). On Omega, t=log(||w||^2/||z||^2), so t o g=t+4*pi. The smooth forms dt and d^c t descend to X. On X put D=dt wedge d^c t, alpha=pi^*alpha_B, beta=pi^*beta_B, where each Fubini--Study form has integral one on its P^1. The metric is omega=alpha+beta+D, and dd^c t=beta-alpha. D is semipositive of rank one, positive on the vertical complex line. Its kernel is ker partial t. This horizontal complex two-plane projects isomorphically onto the tangent space of B. The normalization is d^c=i/(4*pi)(bar-partial minus partial), dd^c=i/(2*pi) partial bar-partial. In logarithmic fiber coordinate x+i*y, both x and y have period 2*pi, t=2*x+constant and D=(1/pi)dx wedge dy.

Accepted inputs: The geometric facts just stated and the previously proved smooth mass identity integral_X(omega+dd^c u)^3=24*pi-6 integral_X du wedge d^c u wedge alpha wedge beta for every smooth real u. Its full proof is in section_lower_mass_metric_geometry.tex and was checked in lower_mass_metric_geometry_01. Standard Stokes on P^1, elementary differential calculus and periodic convolution with smooth nonnegative approximate identities may be used. Verify all remaining inequalities and constants rather than importing a radial optimization theorem.

Checks: For a fixed t modulo 4*pi, there is a point of that value above every base point. Explain why positivity on ker partial t forces the base (1,1)-form (1-p)alpha_B+(1+p)beta_B+dd^c v to be positive for each value p=f'(t), and why integration over the two rulings forces |p|<1. Base-dependent v is arbitrary, not assumed plurisubharmonic. The vertical condition p'>-1 is independent of v. Check that these conditions suffice when v=0; the sharpness sequence sets v=0. Verify exact fiber normalization, disappearance of horizontal derivatives in the mass identity and the one-dimensional optimization for L=4*pi. In the interval argument, p need not be monotone: only endpoint values and p'>=-1 are used. In the approximation, a positive jump at the period join must be retained distributionally; convolution must preserve mean zero and the derivative lower bound, and the additional factor 1-epsilon must make positivity strict. The primitive is periodic because p_epsilon has mean zero. Do not infer a positive lower mass for the unrestricted class or for arbitrary elliptic bundles.

Proof:

The mass identity also explains a limitation of a simple choice of potentials.
Allowing a function of $t$ and an independent function on the base still does
not produce masses tending to zero.

\begin{proposition}\label{prop:elliptic-radial-mass}
Let $\pi:X\to B=\mathbf P^1\times\mathbf P^1$ be the elliptic fibration above,
and put $L=4\pi$. Among smooth real potentials of the form
\[
 u=f(t)+\pi^*v,\qquad f(s+L)=f(s),\qquad v\in C^\infty(B,\R),
 \qquad \omega+\ddc u>0,
\]
the infimum of $\int_X(\omega+\ddc u)^3$ is $8$. Every such mass is
strictly greater than $8$, and this infimum is approached already with $v=0$.
\end{proposition}
\begin{proof}
Write $p=f'$. It is $L$-periodic and has mean zero. The chain rule gives
\[
 \omega+\ddc u
 =(1-p)\alpha+(1+p)\beta+\pi^*\ddc v+(1+p')D.
\]
Positivity on the vertical line implies $p'>-1$. On the complex plane
$\ker\partial t$, the projection to the base is an isomorphism and $D$
vanishes. For each fixed value of $t$ modulo $L$, every base point has a
point above it with that value. Thus, writing $\alpha_B,\beta_B$ for the
two Fubini--Study forms on $B$, the form
$(1-p)\alpha_B+(1+p)\beta_B+\ddc v$ is positive on $B$ for each value of
$p$. Integration over the two rulings gives $1-p>0$ and $1+p>0$.
Consequently
\[
 |p|<1,\qquad p'>-1,\qquad \int_0^L p(s)\,\mathrm{d}s=0.
\]
When $v=0$, these inequalities also suffice for strict positivity.

In a logarithmic fiber coordinate $x+\mathrm{i}y$, both real periods are
$2\pi$, while $t=2x+$ a constant and
$D|_E=\pi^{-1}\mathrm{d}x\wedge\mathrm{d}y$. Hence, for any $L$-periodic
function $F$,
\[
 \int_E F(t)D=\int_0^L F(s)\,\mathrm{d}s.
\]
Only the vertical derivative of $u$ contributes to
\eqref{eq:lower-mass-vertical-energy}. Fiber integration therefore gives
\begin{equation}\label{eq:elliptic-radial-mass}
 \int_X(\omega+\ddc u)^3
 =6\left(L-\int_0^L p(s)^2\,\mathrm{d}s\right).
\end{equation}

Suppose first that $p\not\equiv0$, and put
$A=\max p>0$, $-B_0=\min p<0$ and $r=A+B_0<2$.
The function $G(s)=(A-s)(s+B_0)$ is nonnegative on $[-B_0,A]$.
Choose a forward interval $I$ of length at most $L$ from a maximum of
$p$ to a subsequent minimum. Since $p'\geq-1$, we have
$G(p)\geq-G(p)p'$. Using the zero mean of $p$, we obtain
\[
 \begin{split}
 AB_0L-\int_0^L p^2\,\mathrm{d}s
 &=\int_0^L G(p)\,\mathrm{d}s
 \geq-\int_I G(p)p'\,\mathrm{d}s\\
 &=\int_{-B_0}^{A}G(s)\,\mathrm{d}s=\frac{r^3}{6}.
 \end{split}
\]
As $AB_0\leq r^2/4$, it follows that
\[
 \int_0^L p^2\,\mathrm{d}s
 \leq\frac{Lr^2}{4}-\frac{r^3}{6}<L-\frac43.
\]
The strict inequality follows because the middle expression is strictly
increasing for $0<r\leq2$, as $L>2$. It also holds when $p=0$.
Equation~\eqref{eq:elliptic-radial-mass} now gives the strict lower bound $8$.

To prove sharpness, put $a=(L-2)/2$ and define an $L$-periodic function
$p_0$ by
\[
 p_0(s)=
 \begin{cases}
  1,&0\leq s<a,\\
  1-(s-a),&a\leq s<a+2,\\
  -1,&a+2\leq s<L.
 \end{cases}
\]
It has mean zero, $|p_0|\leq1$ and
$\int_0^L p_0^2\,\mathrm{d}s=L-4/3$.
Its distributional derivative is $-1$ on the descending interval, zero
on the two constant intervals, and has a positive atom at the period
join. Thus $p_0'\geq-1$ as distributions on the circle.
Let $\rho_\varepsilon$ be a nonnegative smooth periodic approximate
identity of integral one, and set
$p_\varepsilon=(1-\varepsilon)(p_0*\rho_\varepsilon)$ for
$0<\varepsilon<1$. Then $p_\varepsilon$ is smooth, has mean zero, and
\[
 |p_\varepsilon|\leq1-\varepsilon,
 \qquad p_\varepsilon'\geq-1+\varepsilon,
 \qquad p_\varepsilon\longrightarrow p_0\quad\hbox{in }L^2.
\]
Its primitive $f_\varepsilon$ is smooth and periodic, so
$u_\varepsilon=f_\varepsilon(t)$ is admissible. Substitution in
\eqref{eq:elliptic-radial-mass} proves that its mass tends to $8$.
\end{proof}

Thus the sequence in \cref{thm:vanishing-lower-mass} cannot be chosen in
this separated form. In the fixed normalization above, even this enlarged
radial class has a positive gap from zero.
