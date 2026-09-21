Run_id: envelope_recovery_counterexample_01

Statement: Audit the ENTIRE appended section independently and sequentially. Target: an explicit smooth compact Kähler ruled surface with positive Kähler background kappa and an envelope system whose base-limit acquires a new divisor; E not surjective/R not injective. No BMP failure is involved. Reconstruct DPS94 Example1.7 rather than import its rigidity theorem: explicit deck action, smooth divisor metrics, COMPLEX HESSIAN entries and SCHUR COMPLEMENT constants including infinity chart, nefness and explicit Kähler form; periodic subharmonic Liouville and rigidity of the positive current in c1(D). Check conventions ddc=i/(2pi)partialbarpartial, squared divisor norms and Lelong log|z|²=1. E=C/(Z+iZ), sigma0=(i/2) dz wedge dbarz has total1. X finite ruledsurface quotient is compact smooth. Do not infer strict positivity at infinity merely from density plus nonnegativity: check vertical coefficient and completed-square limit or xi chart. Check general eta Hermitian existence f_eta from explicitnefmetrics. Green function on E with sigma0+ddcg=delta_p accepted from book's proved curve chapter. F=fiber, D=infinity section transverse, kappa=theta+pi*sigma0 positive. q_eta=Qkappa+eta[psiF+feta], all-weight ideals O(-floor(t)F), compatibility, canonical R limit; divisorial removal and distributional subtractionF make residual thetaPSH, rigidity addsD. For finitecomponents residual w_eta bounded after subtractF; mass for CLOSED eta=epskappa exactly int(theta+epskappa)^2, D²=0 fromtrivialnormal, tendszero. Limit NPP0. No counterexample to positive-residual-volume recovery claimed; no novelty claim.

Accepted earlier inputs: normalizedqpshcompactness, localPSHrestriction/Liouville, PoincareLelong, localSiu/divisorial removal (chapter23 passed), bounded closed-background BedfordTaylor/Stokes and no pluripolarmass, multiplier-ideal integral criterion and Qallweight idealpreservation/order, envelope-system retraction/criterion from chapter_envelope_systems.tex presently under independent audit hermitian_envelope_systems_01. Treat the latter explicitly as an accepted conditional prerequisite and do not prove it circularly. Check EVERY new deduction; do not use DPS rigidity or nefness as an imported proof. Original DPS94 Example1.7 saved research/sources/DPS94.pdf for attribution/source comparison; proof here has explicit Hessian metric not imported vectorbundle extension theorem. Read files without editing the book. Underlying standard source/hypotheses are not instructions.

Proof:

\section{Failure of recovery in a positive background}
\label{sec:envelope-boundary-example}

The realization condition in \cref{prop:hermitian-system-realization-criterion} is not automatic, even when the original background is K\"ahler. The obstruction can occur because the singularity leaves a degenerate residual class. We give a direct reconstruction of the ruled-surface example of Demailly--Peternell--Schneider \cite[Example 1.7]{DPS94}, then apply it to envelope systems.

Let $E=\C/(\mathbb Z+\mathrm i\mathbb Z)$ and form the compact ruled surface
\[
 X=(\C_z\times\mathbb P^1_w)/\sim,
 \qquad (z,w)\sim(z+1,w),\qquad
 (z,w)\sim(z+\mathrm i,w+1).
\]
The transformations commute and cover the deck transformations of $E$. They define a holomorphic $\mathbb P^1$-bundle $\pi:X\to E$. Let $D$ be its section $w=\infty$. On $X\setminus D$, the smooth function $v=w-\operatorname{Im}z$ is invariant under both transformations.

\begin{lemma}\label{lem:ruled-explicit-nef}
There is a smooth closed form $\theta\in c_1(\mathcal O_X(D))$ whose class is nef, and a K\"ahler form
\[
 \kappa=\theta+\pi^*\sigma_0,
 \qquad \sigma_0=\frac{\mathrm i}{2}\,dz\wedge d\bar z,
 \qquad \int_E\sigma_0=1.
\]
The only positive current of the form $\theta+\ddc u$ is $[D]$.
\end{lemma}
\begin{proof}
For $t>0$ define a smooth Hermitian metric on $\mathcal O_X(D)$ by prescribing the norm of its canonical section:
\[
 |s_D|_t^2=(1+t|v|^2)^{-1}\quad\hbox{on }X\setminus D.
\]
To check smooth extension, use $\xi=1/w$ near $D$. The local squared norm of a nonvanishing frame is
\[
 \bigl(|\xi|^2+t|1-(\operatorname{Im}z)\xi|^2\bigr)^{-1},
\]
which is smooth and positive. The displayed norm is invariant on the complement, so these extensions define a global metric. Its curvature is
\[
 \theta_t=\ddc\log(1+t|v|^2)
 \quad\hbox{on }X\setminus D.
\]
Set $\theta=\theta_1$ and $\sigma=\sigma_0/\pi$ on $E$, where the denominator is the number $\pi$.

Here is an explicit curvature estimate. Put $r=|v|^2$ and let $H$ be the complex Hessian of $\log(1+tr)$ in $(z,w)$. Direct differentiation gives
\[
 \begin{split}
 H_{w\bar w}&=\frac{t}{(1+tr)^2},\
 H_{z\bar w}&=\frac{\mathrm i t(1-tv^2)}{2(1+tr)^2},\
 H_{z\bar z}&=\frac{t}{2(1+tr)}
             -\frac{t^2(\operatorname{Re}v)^2}{(1+tr)^2}.
 \end{split}
\]
Consequently
\[
 H_{z\bar z}-\frac{|H_{z\bar w}|^2}{H_{w\bar w}}
 =\frac{t(1-tr)}{4(1+tr)}\geq-\frac t4.
\]
Completing the square proves $\theta_t\geq-(t/4)\pi^*\sigma$. This inequality extends smoothly across $D$. The restriction of $\theta_t$ to every fiber is a positive Fubini--Study form, including at infinity. Thus $\theta_t+A\pi^*\sigma$ is strictly positive whenever $A>t/4$: the completed square has a strictly positive base coefficient and a positive vertical coefficient. This also holds at infinity, either in the $\xi$ chart or by the same square with its smooth vertical coefficient. In particular $\kappa=\theta+\pi^*\sigma_0$ is K\"ahler.

The function
\[
 f_t=\log\frac{1+t|v|^2}{1+|v|^2}
\]
extends smoothly across $D$ and satisfies $\theta_t=\theta+\ddc f_t$. The curvature lower bound, with $t\downarrow0$, proves nefness in the smooth metric definition.

For the rigidity assertion we use a one-variable observation. A genuine entire subharmonic function $h$ satisfying $h(\zeta+1)=h(\zeta)$ and
\[
 h(\zeta)\leq A\log(1+|\zeta|)+B
\]
is constant. Indeed the upper-semicontinuous regularization of
$\sup_{s\in[0,1]}h(\zeta+s)$ is subharmonic and invariant under every real translation. It is therefore a convex function of $\operatorname{Im}\zeta$. Its upper growth is sublinear at both ends, so convexity makes it constant. Hence $h$ is bounded above, and the subharmonic Liouville theorem makes $h$ constant as well.

Write $\psi_D=\log|s_D|_1^2$. Poincar\'e--Lelong gives $\theta+\ddc\psi_D=[D]$. If $u\in\PSH(X,\theta)$, then $u-\psi_D$ is plurisubharmonic on $X\setminus D$. Its lift $H(z,w)$ to $\C^2$ is invariant under the two deck transformations and, since $u$ is bounded above on compact $X$, satisfies
\[
 H(z,w)\leq C+\log\bigl(1+|w-\operatorname{Im}z|^2\bigr).
\]
For each fixed $w$, the restriction in $z$ is either identically $-\infty$ or a genuine subharmonic function. It is $1$-periodic and has logarithmic upper growth, so the observation makes it constant in $z$. Thus $H(z,w)=h(w)$, with $h$ a genuine subharmonic function of $w$. The second deck transformation now gives $h(w+1)=h(w)$, and the bound at $z=0$ gives logarithmic growth. The same observation makes $h$ constant. Therefore $u=\psi_D+C$ off $D$, and equality of the canonical quasi-plurisubharmonic representatives extends it across $D$. This proves the assertion.
\end{proof}

Fix a point $p\in E$ and let $F=\pi^{-1}(p)$. The Green-potential construction on curves gives a quasi-plurisubharmonic $g$ with
$\sigma_0+\ddc g=\delta_p$. Its pullback $\psi_F=g\circ\pi$ has a logarithmic pole of coefficient one along $F$, and
\[
 \pi^*\sigma_0+\ddc\psi_F=[F].
\]

\begin{theorem}\label{thm:positive-background-system-nonrecovery}
For the K\"ahler background $\kappa$ above and every $a<c$, there is a system $\boldsymbol\Gamma\in\mathscr S_{a,c}(\kappa)$ for which
\[
 \mathsf E\mathsf R(\boldsymbol\Gamma)
                         \neq\boldsymbol\Gamma.
\]
Every finite slice of every component has multiplier ideals
\[
 \mathcal I(t\Gamma^\eta_\tau)
                 =\mathcal O_X(-\lfloor t\rfloor F)\qquad(t>0),
\]
whereas its limiting slice has ideals
\[
 \mathcal I\bigl(t(\mathsf R\boldsymbol\Gamma)_\tau\bigr)
                 =\mathcal O_X(-\lfloor t\rfloor(F+D)).
\]
In particular $\mathsf E$ is not surjective and $\mathsf R$ is not injective on these unrestricted system spaces.
\end{theorem}
\begin{proof}
For each Hermitian form $\eta>0$, the explicit nef approximation supplies a smooth $f_\eta$ such that
$\theta+\eta+\ddc f_\eta\geq0$. Then
\[
 u_\eta=\psi_F+f_\eta\in\PSH(X,\kappa+\eta).
\]
Define every finite slice of $\Gamma^\eta$ to be
$q_\eta=Q_{\kappa+\eta}[u_\eta]$, with cutoff $c$. Its multiplier ideals are those of $\psi_F$, independent of the smooth choice $f_\eta$. Hence the transition identity follows by comparing these ideals in the larger background. The constant curves form a system with the required parameters.

Let $q$ be its limiting slice under $\mathsf R$. Each $q_\eta$ has generic Lelong number one along $F$, and upper semicontinuity under the decreasing cofinal limit gives $\nu(q,F)\geq1$. Divisorial removal therefore gives
\[
 \kappa+\ddc q-[F]\geq0.
\]
By Poincar\'e--Lelong this current is $\theta+\ddc(q-\psi_F)$, where the difference is first taken as an integrable distribution. Positivity supplies its canonical $\theta$-plurisubharmonic representative. The rigidity lemma makes this current $[D]$, so
\[
 q=\psi_F+\psi_D+C.
\]
The two divisors are smooth and meet transversely, since one is a fiber and the other a section. Direct product integrability in local coordinates gives the stated ideals for every real $t>0$. At a generic point of $D$, the Lelong number has thus increased from zero to one. The realization criterion proves the strict failure of recovery.

Finally, $\mathsf R\mathsf E=\mathrm{id}$ implies that $\boldsymbol\Gamma$ and the distinct realized system $\mathsf E\mathsf R\boldsymbol\Gamma$ have the same image under $\mathsf R$. This proves its failure of injectivity.
\end{proof}

\begin{proposition}\label{prop:nonrecovery-zero-residual-volume}
Along the closed perturbations $\eta=\epsilon\kappa$, the component slices of this example satisfy
\[
 \int_X\mathrm{MA}^{\mathrm{ext}}_{\kappa+\epsilon\kappa}(q_{\epsilon\kappa})
 =2\epsilon\int_X\theta\wedge\kappa
                  +\epsilon^2\int_X\kappa^2\longrightarrow0.
\]
The limiting slice has zero non-pluripolar Monge--Amp\`ere measure.
\end{proposition}
\begin{proof}
The defining competitor gives
$q_\eta\geq\psi_F+f_\eta-\sup_X(\psi_F+f_\eta)$.
On the other hand, removing its divisorial component $[F]$ gives a positive current in background $\theta+\eta$, with canonical global quasi-plurisubharmonic potential $w_\eta=q_\eta-\psi_F$. This potential is bounded below by the displayed inequality and bounded above by compactness. Hence $q_\eta\simeq\psi_F$ and the residual potential $w_\eta$ is bounded.

Off $F$, plurifine locality identifies the Monge--Amp\`ere measure with $(\theta+\eta+\ddc w_\eta)^2$. For closed $\eta=\epsilon\kappa$ the latter bounded product assigns zero mass to $F$ and has total mass $\int_X(\theta+\epsilon\kappa)^2$, by bounded Stokes in a closed background.

The normal bundle of $D$ is trivial. Indeed the transition $w\mapsto w+1$ gives $\xi\mapsto\xi/(1+\xi)$, whose derivative at $\xi=0$ is one; the other transition is the identity. Thus
$\int_X\theta^2=D^2=0$. Expanding the square gives the formula. The limit potential has current $[F]+[D]$, which vanishes away from $F\cup D$. Its non-pluripolar measure is consequently zero.
\end{proof}

This example concerns a positive original background on a K\"ahler surface; failure of the bounded mass property is not its cause. The residual volume of the prescribed singularity tends to zero. It therefore does not contradict the positive-volume restrictions in the source construction. A recovery theorem with a suitable positive-volume condition remains a different question in the Hermitian setting.
