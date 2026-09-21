Run_id: singular_domination_01

Statement: Audit the supplied proofs of non-collapsing for bounded potentials in ANY big smooth real background, bounded domination for non-collapsing semipositive backgrounds, the zero-set singular lemma, and strict singular domination with a smaller-background envelope, plus exponential order. Main singular theorem: theta>=0 big in the sense theta+ddc rho>=a omega for a genuine qpsh rho (no analytic singularities assumed), u theta-psh with P_delta theta(u) genuine for delta in(0,1), v preceq u, MAu<=c MAv on{u<v},c<1 impliesu>=v. No BMP/PVP or finite total mass assumed. All inequalities of extended measures must be checked without subtracting infinities. Convention ddc=i/(2pi) partial bar-partial. Accepted inputs: bounded BT/local NPP calculus, positivity of mixed products on common bounded truncation levels, arbitrary-smooth-background ordered-contact inequality, no mass at pluripolar sets, normalized L1 compactness, canonical qpsh representatives, envelope properties and ANY semipositive-background contact support (proved in penalized_contacts_01 plus local_contacts_01 unbounded reduction), each bounded Hermitian potential has positive mass (bounded_comparison_01), and the simple bounded-below-envelope lemma (constant lower competitor + a finite-obstacle-sublevel set and normalized L1 give common upper bound). Do NOT import semipositive big noncollapsing, semipositive bounded domination, unbounded domination, or global mass bounds. Inspect noncollapsing proof with auxiliary p=P_aomega(u-rho) where rho may be unbounded and theta nonsemipositive; inspect all extended product/contact transitions; then check bounded domination, auxiliary singular-zero lemma, max reduction and integer b barrier contradiction. Source inspiration: ALS26 Theorem3.11 and Lemma3.12, GL22 Prop2.8, GL23-equations Theorem1.11 (but its noncollapsing proof uses analytic rho, unlike our auxiliary-envelope argument). Reference files at /Users/mingchen/Non-Kahler/research/sources/. Verify actual statements and all logical dependencies. Source book current chapter_envelopes.tex has labels if needed. Read only, write normal verification records/reports.

Proof:

\begin{proposition}\label{prop:big-noncollapsing}
If a smooth real background $\theta$ is big, every bounded $u\in\PSH(X,\theta)$ has strictly positive Monge--Amp\`ere mass.
\end{proposition}
\begin{proof}
Choose $\rho\in\PSH(X,\theta)$ and $a>0$ with $\theta_\rho\geq a\omega$. Normalize $\rho\leq0$ and put
\[
 p=P_{a\omega}(u-\rho).
\]
The obstacle is finite almost everywhere and bounded below, so \cref{lem:bounded-below-envelope} gives bounded $p$. The obstacle is quasi-continuous off a pluripolar set. Contact support, applied in the Hermitian background $a\omega$, gives $\mathrm{MA}_{a\omega}(p)$ carried by
$D=\{p+\rho=u\}$, outside the pole set of $\rho$.

We have $p+\rho\leq u$ everywhere, by the canonical representatives, and
\[
 \theta+\ddc(p+\rho)
 =(a\omega+\ddc p)+(\theta_\rho-a\omega)
 \geq a\omega+\ddc p\geq0.
\]
On common finite truncation levels, positivity of the mixed products and ordered contact give
\[
 \mathbf1_D\mathrm{MA}_{a\omega}(p)
 \leq\mathbf1_D\mathrm{MA}^{\mathrm{ext}}_\theta(p+\rho)
 \leq\mathbf1_D\mathrm{MA}_\theta(u).
\]
Exhausting these levels proves the same inequalities for the extended measures. Since $p$ is bounded, its Hermitian Monge--Amp\`ere mass is positive by \cref{cor:bounded-mass-positive}. Integrating proves the assertion. No estimate uniform in $u$ is claimed.
\end{proof}

For semipositive big backgrounds, this gives the non-collapsing input needed below. The proof itself also applies to a big background which is not semipositive, whenever a bounded potential exists.


\begin{theorem}[Guedj--Lu]\label{thm:semipositive-bounded-domination}
Let $\theta\geq0$ be non-collapsing on bounded potentials. Suppose $u,v\in\PSH(X,\theta)\cap L^\infty(X)$ and $0\leq c<1$. If
\[
 \mathbf1_{\{u<v\}}\mathrm{MA}_\theta(u)
 \leq c\,\mathbf1_{\{u<v\}}\mathrm{MA}_\theta(v),
\]
then $u\geq v$.
\end{theorem}
\begin{proof}
We give the envelope argument of \cite[Proposition 2.8]{GL22}. If the conclusion failed, choose $a>0$ such that $E=\{u<v-a\}$ is nonempty. This set has positive volume by \cref{lem:strict-set-positive-volume}. Fix $C$ with $|u|,|v|\leq C$.

For $b>1$ define the bounded envelope
\[
 w_b=P_\theta\bigl(bu-(b-1)v\bigr),\qquad
 D_b=\{w_b=bu-(b-1)v\}.
\]
Constants bounded below are competitors, since $\theta\geq0$. Bounded contact support gives $\mathrm{MA}_\theta(w_b)$ concentrated on $D_b$. The potential
$b^{-1}w_b+(1-b^{-1})v$ lies below $u$ quasi-everywhere, hence everywhere by the canonical representatives, and equals $u$ on $D_b$ outside a pluripolar set. Ordered contact and positivity of the mixed terms give
\[
 \mathbf1_{D_b}\left[b^{-n}\mathrm{MA}_\theta(w_b)
              +(1-b^{-1})^n\mathrm{MA}_\theta(v)\right]
 \leq\mathbf1_{D_b}\mathrm{MA}_\theta(u).
\]
Choose $b$ sufficiently large that $(1-b^{-1})^n>c$. On $D_b\cap\{u<v\}$ this forces $\mathrm{MA}_\theta(w_b)=0$. Non-collapsing gives positive total mass for $w_b$, so some mass is carried by $D_b\cap\{u\geq v\}$. At a point of that set outside the exceptional pluripolar set,
\[
 w_b=bu-(b-1)v=u+(b-1)(u-v)\geq-C.
\]
Consequently $\sup_Xw_b\geq-C$, uniformly as $b\to\infty$.

On the fixed set $E$, the obstacle bound gives
$w_b\leq C-(b-1)a$ quasi-everywhere. Hence
\[
 \int_X|w_b-\sup_Xw_b|\,dV
 \geq\bigl((b-1)a-2C\bigr)\operatorname{vol}_{dV}(E)
\]
for all sufficiently large $b$. This contradicts the normalized $L^1$ bound of \cref{thm:normalized-compactness}. No uniform estimate for the masses of $w_b$ was used.
\end{proof}

The same argument as in \cref{cor:bounded-exponential-comparison} now gives exponential comparison for bounded potentials in every such semipositive background. Removing boundedness requires further control: an envelope used in the proof may then have infinite mass or fail to lie in the desired singularity class.


\section{Domination with a smaller background}

The first singular domination theorem does not need a mass bound. A potential for a smaller background serves as a common lower barrier for a family of envelopes. We reconstruct \cite[Theorem 3.11]{ALS26}, including the auxiliary bounded-envelope argument.

Throughout this section $\theta\geq0$ is smooth and big. Thus every positive multiple of $\theta$ is non-collapsing on bounded potentials by \cref{prop:big-noncollapsing}. All Monge--Amp\`ere measures below are extended measures; their total masses may be infinite.

\begin{lemma}\label{lem:singular-zero-domination}
Suppose $u,v\in\PSH(X,\theta)$, $v\preceq u$, and
$\mathrm{MA}^{\mathrm{ext}}_\theta(u)(\{u<v\})=0$. If $0<\delta<1$ and $v_\delta=P_{\delta\theta}(v)$ is genuine, then $u\geq v_\delta$.
\end{lemma}
\begin{proof}
Choose $C$ with $v-C\leq u$. Since $v_\delta\leq v$, the obstacle $u-v_\delta$ is bounded below by $-C$ off the pole sets and is finite almost everywhere. Hence
\[
 p=P_{(1-\delta)\theta}(u-v_\delta)
\]
is bounded by \cref{lem:bounded-below-envelope}. Its measure is carried by $D=\{p+v_\delta=u\}$ by contact support. Also $p+v_\delta\leq u$ everywhere and
\[
 \theta+\ddc(p+v_\delta)
 =((1-\delta)\theta+\ddc p)+(\delta\theta+\ddc v_\delta).
\]
Positivity of the two summands and ordered contact imply
\[
 \mathbf1_D\mathrm{MA}_{(1-\delta)\theta}(p)
 \leq\mathbf1_D\mathrm{MA}^{\mathrm{ext}}_\theta(u).
\]
These measure inequalities can first be taken on common finite truncation levels and then exhausted. On $D\cap\{p<0\}$ outside the pole sets, we have
$u=p+v_\delta<v_\delta\leq v$. The hypothesis therefore gives
$\mathrm{MA}_{(1-\delta)\theta}(p)(\{p<0\})=0$. Bounded domination in the non-collapsing semipositive background $(1-\delta)\theta$, applied to $p$ and zero, yields $p\geq0$. Since $u\geq p+v_\delta$, the result follows.
\end{proof}

\begin{theorem}[Singular strict domination]\label{thm:singular-strict-domination}
Let $u\in\PSH(X,\theta)$ satisfy $P_{\delta\theta}(u)\not\equiv-\infty$ for some $0<\delta<1$. Suppose $v\in\PSH(X,\theta)$, $v\preceq u$, and $0\leq c<1$. If
\[
 \mathbf1_{\{u<v\}}\mathrm{MA}^{\mathrm{ext}}_\theta(u)
 \leq c\,\mathbf1_{\{u<v\}}\mathrm{MA}^{\mathrm{ext}}_\theta(v),
\]
then $u\geq v$.
\end{theorem}
\begin{proof}
Replace $v$ by $\max(u,v)$. Plurifine locality preserves the displayed inequality on the strict set, and there is $C\geq0$ with
$u\leq v\leq u+C$. For $b>1$ define
\[
 p_b=P_\theta(bu-(b-1)v),\qquad
 D_b=\{p_b=bu-(b-1)v\}.
\]
The competitor $u-(b-1)C$ gives a genuine envelope, and
$u-(b-1)C\leq p_b\leq u$. Contact support concentrates its measure on $D_b$. The potential
$b^{-1}p_b+(1-b^{-1})v$ lies below $u$ and agrees with it on $D_b$. Ordered contact and positivity give
\[
 \mathbf1_{D_b}\bigl[b^{-n}\mathrm{MA}^{\mathrm{ext}}_\theta(p_b)
 +(1-b^{-1})^n\mathrm{MA}^{\mathrm{ext}}_\theta(v)\bigr]
 \leq\mathbf1_{D_b}\mathrm{MA}^{\mathrm{ext}}_\theta(u).
\]
Choose $b$ large enough that $(1-b^{-1})^n>c$. On $D_b\cap\{u<v\}$ the hypothesis forces $\mathrm{MA}^{\mathrm{ext}}_\theta(p_b)$ to vanish. To justify this when masses are infinite, first restrict to the sets where $u,v,p_b>-k$. Every measure there is finite, being bounded by the mass of its fixed bounded truncation. Subtract the finite terms on each such set and then take the union over $k$. No subtraction of infinite masses occurs.

It follows that the measure of $p_b$ is carried by $D_b\cap\{u=v\}\subset\{p_b=u\}$. Apply \cref{lem:singular-zero-domination} to the pair $(p_b,u)$; their singularities are equivalent and the smaller-background envelope of $u$ is genuine. We obtain
\[
 p_b\geq P_{\delta\theta}(u)
\]
for all sufficiently large $b$. If $\{u<v\}$ were nonempty, there would be $a>0$ such that $E=\{u<v-a\}$ had positive volume, with both functions finite there. Indeed the strict-set lemma applies at a finite strict point; if the initial point is a pole of $u$ with $v$ finite, upper semicontinuity and the local submean inequality for $v$ give such finite points nearby. On $E$, the obstacle inequality gives
\[
 P_{\delta\theta}(u)\leq p_b\leq v-ba
\]
quasi-everywhere. Let $b$ tend to infinity through integers. This forces the genuine quasi-plurisubharmonic function $P_{\delta\theta}(u)$ to be $-\infty$ on a set of positive volume, a contradiction. Thus $u\geq v$ off the pole sets, and the canonical representatives give the inequality everywhere.
\end{proof}

\begin{corollary}\label{cor:singular-exponential-order}
Under the smaller-background and singularity-order assumptions of the theorem, if $\lambda>0$ and
\[
 e^{-\lambda u}\mathrm{MA}^{\mathrm{ext}}_\theta(u)
 \leq e^{-\lambda v}\mathrm{MA}^{\mathrm{ext}}_\theta(v)
\]
off the pole sets, then $u\geq v$. In particular the exponential equation has at most one solution in a fixed ordinary singularity type admitting a smaller-background envelope.
\end{corollary}
\begin{proof}
On $\{u<v-t\}$, the assumed inequality gives
$\mathrm{MA}_\theta^{\mathrm{ext}}(u)\leq e^{-\lambda t}\mathrm{MA}_\theta^{\mathrm{ext}}(v-t)$.
Apply the theorem and let $t\downarrow0$. For two solutions of one equation in the stated type, apply the result in both directions. Weighted measures are interpreted off the common pluripolar exceptional sets; no value of an infinite weight on such a set is needed.
\end{proof}
