Run_id: general_relative_envelopes_01

Run scope: Bounded independent verification through the normal Rethlas workflow. The parent owns manuscript edits, build and release. Restrict writes to normal verifier tools, memory and this new run's results. Do not alter book/editorial/blueprint/status/changelog files, frozen inputs, original references or historical reports. Do not commit or push. No Popovici result is used.

Statement: Verify the relative-envelope elementary properties, stretching closure, finite rooftop closure and ordinary-envelope equality below for an arbitrary smooth real (1,1)-form theta on a compact connected complex manifold X and any genuine phi in PSH(X,theta). No closedness, semipositivity, bigness, model-reference assumption, upper mass property or positive lower mass property is allowed. This strengthens the scope of the book's prior elementary envelope statements, with a shorter direct convex proof of finite rooftops. Check all defining inequalities at common poles, b=1, N=1, constant translations and upper regularization. This is not a novelty or whole-book certification task. Do not accept a mass-based or semipositive proof as justification for the new scope.

Accepted elementary analytic inputs (already established earlier in this book):
1. Every genuine theta-psh potential is quasi-psh, bounded above on compact X, finite almost everywhere and has pluripolar pole set. Its distributional lower bound is preserved under convex combinations, constants, maxima and L1 limits with a genuine limit. Almost-everywhere inequalities between canonical quasi-psh potentials hold everywhere.
2. The family {h in PSH(X,theta):sup_X h=0} has a uniform L1 norm bound for a fixed smooth positive volume form. No bigness or positivity of theta is assumed here; it suffices that the family is nonempty. This follows by comparison theta<=C omega from the book's normalized compactness theorem.
3. A nonempty family of theta-psh functions uniformly bounded above has a theta-psh upper-regularized supremum, equal to the unregularized supremum off a pluripolar set (Choquet extraction). A fixed genuine lower competitor rules out the identically minus infinity case.

Conventions and construction to check: u preceq phi means u<=phi+C for a real constant C. Ordinary equivalence means both orders. P_theta(f) is the upper-regularized supremum of theta-psh h<=f quasi-everywhere, where quasi-everywhere means outside a pluripolar set. For finite rooftops the obstacle is min_i u_i. P_theta[u] is the regularized supremum of h<=0 with h preceq u; its competitor set contains u-sup_Xu. In particular P_theta[u] is genuine, has supremum zero, and is monotone in the ordinary singularity order. Do not assume idempotence or bounded difference from u.

For a finite-almost-everywhere obstacle f, the family of competitors is uniformly bounded above when nonempty. To check this, choose a finite A and a positive-volume measurable set E on which f<=A. If S=sup_Xh>A, then (S-A)Vol(E)<=integral_E |h-S|<=C_theta by accepted input2. This gives a uniform upper bound. For the convex family A_b below, the obstacle bu-(b-1)phi is interpreted off its common pole set; the convex inequality is equivalent there and extends canonically as an inequality between quasi-psh functions. This argument makes each nonempty Q_b genuine and makes Q_b itself a member of A_b. The b=1 sum is interpreted as h, without a zero-times-minus-infinity ambiguity.

The ALS26 citations below are contextual attribution for the pre-existing semipositive big setting, not mathematical inputs for the arbitrary-background proof. The reference to the later volume chapter is navigation only. Verify the new deductions directly from the displayed definitions and the three accepted analytic inputs.

Proof submitted (exact proposed TeX, to be read as mathematical source):

\section{Relative envelope classes}

In this section $\theta$ is an arbitrary smooth real $(1,1)$-form and $\varphi\in\PSH(X,\theta)$. No semipositivity, bigness or mass hypothesis is imposed.

For $u,\varphi\in\PSH(X,\theta)$ and $b\geq1$, define the competitor family
\[
 \mathcal A_b(u,\varphi)=
 \left\{h\in\PSH(X,\theta):
 b^{-1}h+(1-b^{-1})\varphi\leq u\right\}.
\]
For $b=1$ the inequality means $h\leq u$. For $b>1$ the displayed sum of quasi-plurisubharmonic functions is defined also at poles. This notation avoids assigning a value to $bu-(b-1)\varphi$ at a common pole. When the family is nonempty, its upper envelope is denoted
\[
 Q_b(u,\varphi)=P_\theta(bu-(b-1)\varphi).
\]
When the family is nonempty, its envelope is a genuine potential. Indeed, the obstacle $bu-(b-1)\varphi$ is finite almost everywhere, so the finite-sublevel argument at the start of the chapter gives a common upper bound for the competitors. The local envelope theorem applies, and the defining convex inequality holds everywhere by the canonical quasi-plurisubharmonic representatives. This argument needs no bigness or mass hypothesis. The construction in a semipositive big background is also recorded in \cite[Propositions 2.4 and Lemma 2.5]{ALS26}, and in an arbitrary big background in \cite[Section 2.1]{XL26}.

\begin{definition}\label{def:relative-envelope-class}
Define
\[
 \mathcal E_{\mathrm{env}}(X,\theta,\varphi)
 =\{u\in\PSH(X,\theta):u\preceq\varphi,
       \ \mathcal A_b(u,\varphi)\ne\varnothing
       \text{ for every }b\geq1\}.
\]
\end{definition}

This is the definition used in \cite[Definition 3.2]{ALS26} for semipositive big $\theta$. It is meaningful without a mass bound. Its comparison with the volume-defined class is developed in \cref{chap:mass-bound-volumes}. For the fixed reference, write $\mathcal E_\varphi=\mathcal E_{\mathrm{env}}(X,\theta,\varphi)$.

\begin{proposition}\label{prop:relative-elementary}
The class $\mathcal E_{\mathrm{env}}(X,\theta,\varphi)$ is convex, contains all potentials equivalent to $\varphi$, and is stable under bounded changes of its members. If $u$ belongs to it, $u\leq v$ and $v\preceq\varphi$, then $v$ belongs to it. In particular, it is stable under taking maxima of two members.
\end{proposition}
\begin{proof}
If $u\geq\varphi-C$, use $h=\varphi-bC$ for each $b$. More generally, if $u'\geq u-C$ and $h\in\mathcal A_b(u,\varphi)$, then $h-bC\in\mathcal A_b(u',\varphi)$. The singularity-order condition persists under bounded changes. Convex combinations of two competitors give competitors for the same convex combination of their target functions. Finally a competitor for $u$ is a competitor for any larger $v$; the assumed relation $v\preceq\varphi$ supplies the other defining condition.
\end{proof}

\begin{lemma}\label{lem:relative-stretch-closure}
If $u\in\mathcal E_\varphi$ and $u\leq\varphi$, then $Q_b(u,\varphi)\in\mathcal E_\varphi$ for every $b\geq1$. More generally, if $u,w\in\mathcal E_\varphi$ and $u\leq w$, then $Q_b(u,w)\in\mathcal E_\varphi$.
\end{lemma}
\begin{proof}
Put $u_t=Q_t(u,\varphi)$. Fix $s\geq1$ and choose $t>bs$. The defining inequality for $u_t$ shows that
\[
 \frac bt u_t+\left(1-\frac bt\right)\varphi
 \leq bu-(b-1)\varphi.
\]
The left side is $\theta$-plurisubharmonic, so it is at most $u_b$. Consequently
\[
 \frac{bs}{t}u_t+\left(1-\frac{bs}{t}\right)\varphi
 \leq s u_b-(s-1)\varphi.
\]
This supplies a competitor for every $s$. Also $u_b\leq u\leq\varphi$, which supplies the singularity-order condition. All inequalities are interpreted off the pole sets and then as inequalities between the corresponding convex combinations of canonical potentials.

For the second assertion choose a constant $C$ such that $u-C\leq\varphi$ and $w-C\leq\varphi$. Translation reduces to $u,w\leq\varphi$. The obstacle for $Q_b(u,w)$ lies above that for $Q_b(u,\varphi)$ and below $u$, because $u\leq w\leq\varphi$. Thus
\[
 Q_b(u,\varphi)\leq Q_b(u,w)\leq u\leq\varphi.
\]
Upward stability of the relative class, proved in \cref{prop:relative-elementary}, gives the conclusion. Restoring the translation does not change class membership.
\end{proof}

\begin{proposition}\label{prop:relative-finite-rooftops}
The rooftop of any finite collection of members of $\mathcal E_\varphi$ is genuine and belongs to $\mathcal E_\varphi$.
\end{proposition}
\begin{proof}
Let $u_1,\ldots,u_N\in\mathcal E_\varphi$. The case $N=1$ follows from the definition. A common constant translation reduces the remaining cases to $u_i\leq\varphi$, since rooftops commute with such translations and class membership is unchanged. For $b\geq1$, put
\[
 h_b=\frac1N\sum_{i=1}^N Q_{Nb}(u_i,\varphi).
\]
Every summand is genuine and at most $u_i\leq\varphi$. For each $i$, the defining inequality for its summand and the bounds on the others give
\[
 b^{-1}h_b+(1-b^{-1})\varphi
 \leq (Nb)^{-1}Q_{Nb}(u_i,\varphi)
              +(1-(Nb)^{-1})\varphi
 \leq u_i.
\]
These are inequalities between convex combinations of canonical potentials, so they remain meaningful at common poles. For $b=1$, $h_1$ is a competitor for $p=P_\theta(u_1,\ldots,u_N)$; hence $p$ is genuine. For every $b\geq1$, the left side is a $\theta$-plurisubharmonic competitor below each $u_i$, so it is at most $p$. Thus $h_b\in\mathcal A_b(p,\varphi)$. Together with $p\leq u_1\preceq\varphi$, this proves $p\in\mathcal E_\varphi$.
\end{proof}

\begin{proposition}\label{prop:relative-envelope-equality}
If $u\in\mathcal E_\varphi$, then
\[
 P_\theta[u]=P_\theta[\varphi].
\]
\end{proposition}
\begin{proof}
The relation $u\preceq\varphi$ gives one inequality. For $a\in(0,1)$ choose $h_a$ with $a\varphi+(1-a)h_a\leq u$. Combining normalized competitors for $P_\theta[\varphi]$ and $P_\theta[h_a]$ gives
\[
 aP_\theta[\varphi]+(1-a)P_\theta[h_a]\leq P_\theta[u].
\]
Indeed, their convex combination is below zero and is more singular than $u$; taking the two upper envelopes preserves the inequality by local regularization. For every potential $h$, $P_\theta[h]$ has supremum zero, because it lies above $h-\sup_Xh$ and below zero. The normalized $L^1$ bound therefore applies uniformly to $P_\theta[h_a]$. Along $a\to1$ the left-hand side tends to $P_\theta[\varphi]$ in $L^1$. The inequality passes to the limit almost everywhere and then everywhere for the canonical representatives. This proves the other inequality.
\end{proof}


