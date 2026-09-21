Run_id: relative_extended_domination_01

Statement: Verify the new staged proof of zero and strict domination in the relative envelope class with NO finiteness hypothesis on either Monge--Ampere measure. X is compact connected Hermitian, theta is smooth semipositive and big (not necessarily closed), phi is a normalized model reference P_theta[phi]=phi, sup phi=0, with P_(epsilon theta)(phi) genuine for some 0<epsilon<1, and v_-(theta)>0. No bounded mass hypothesis is allowed. The exact envelope class is defined by all convex competitors, not by a finite-volume equality. The proposed proof uses the independently established finite-measure theorem only for an auxiliary envelope k, AFTER proving its mass finite. Check scaling, class membership, admissibility/contact for the difference obstacle, finite-level subtraction, canonical representatives, and noncircularity. This is a new claim being audited, not a known theorem premise.

The preliminary internal results below have previously reconstructed proofs and are legitimate premises at their exact stated scope. Do not use the general prescribed-reference existence theorem or the proposed conclusion to justify any of them. The earlier finite-domination proof is included to check dependency. Standard local Bedford--Taylor positivity, plurifine locality, canonical quasi-psh representatives and finite mass of one bounded potential are allowed. Extended products have the same positive mixed-product inequalities after restriction to common finite truncation levels and do not charge pluripolar sets. General contact for a genuine envelope of an almost-everywhere finite quasi-continuous obstacle in a smooth big background is an already established premise, including without finite total mass. Read the source proof at book/author/section_big_general_contact.tex if needed. The pole sets of the difference obstacle are ignored, not assigned arithmetic differences of infinities.

Proof:

## Definitions and independently proved premises

\section{Relative full mass through convex combinations}

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
For big $\theta$, the family is uniformly bounded above. Indeed, choose $m$ such that $D=\{\varphi>-m\}$ has positive smooth volume $d$. On $D$, every competitor satisfies $h\leq L:=b\sup_Xu+(b-1)m$. Choose $C>0$ with $\theta\leq C\omega$. The normalized $L^1$ estimate \eqref{eq:normalized-lone}, applied after scaling, gives $\int_X|h-\sup_Xh|\,\mathrm{d}V\leq K$. Thus $\sup_Xh\leq L+K/d$ whenever $\sup_Xh>L$, and the bound is immediate otherwise. The local envelope theorem then shows that $Q_b$ is a genuine potential. The defining convex inequality holds everywhere by the canonical quasi-plurisubharmonic representatives. These facts are also recorded in \cite[Propositions 2.4 and Lemma 2.5]{ALS26} and \cite[Section 2.1]{XL26}.

\begin{definition}\label{def:relative-envelope-class}
Define
\[
 \mathcal E_{\mathrm{env}}(X,\theta,\varphi)
 =\{u\in\PSH(X,\theta):u\preceq\varphi,
       \ \mathcal A_b(u,\varphi)\ne\varnothing
       \text{ for every }b\geq1\}.
\]
Under bounded mass we also define
\[
 \mathcal E_{\mathrm{vol}}(X,\theta,\varphi)
 =\{u\in\PSH(X,\theta):u\preceq\varphi,
 \ \overline{\operatorname{vol}}_\theta(u)
   =\overline{\operatorname{vol}}_\theta(\varphi)\}.
\]
\end{definition}

The first is the definition used in \cite[Definition 3.2]{ALS26} for semipositive big $\theta$; the second is \cite[Definition 3.2]{XL26}. Our temporary subscripts keep their definitions visible before proving their equivalence in a common regime.

\begin{proposition}\label{prop:relative-elementary}
The class $\mathcal E_{\mathrm{env}}(X,\theta,\varphi)$ is convex, contains all potentials equivalent to $\varphi$, and is stable under bounded changes of its members. If $u$ belongs to it, $u\leq v$ and $v\preceq\varphi$, then $v$ belongs to it. In particular, it is stable under taking maxima of two members.
\end{proposition}
\begin{proof}
If $u\geq\varphi-C$, use $h=\varphi-bC$ for each $b$. More generally, if $u'\geq u-C$ and $h\in\mathcal A_b(u,\varphi)$, then $h-bC\in\mathcal A_b(u',\varphi)$. The singularity-order condition persists under bounded changes. Convex combinations of two competitors give competitors for the same convex combination of their target functions. Finally a competitor for $u$ is a competitor for any larger $v$; the assumed relation $v\preceq\varphi$ supplies the other defining condition.
\end{proof}


\chapter[Relative envelopes and finite measures]{Finite measures in the relative envelope class}
\label{chap:relative-finite-measures}

The relative envelope class can contain potentials of infinite Monge--Amp\`ere mass. This does not prevent it from providing the right setting for equations with finite measures. The distinction is between a condition on singularities and the additional measure control supplied by an equation. In this chapter we develop the envelope arguments that connect the two. A positive lower volume enters explicitly; no upper volume bound is imposed.

Throughout, $X$ is connected and compact, $\theta\geq0$ is smooth and big, and $\varphi$ satisfies \eqref{eq:als-model-condition}. Fix $0<\varepsilon<1$ with $P_{\varepsilon\theta}(\varphi)$ genuine. Write
\[
 \mathcal E_\varphi=\mathcal E_{\mathrm{env}}(X,\theta,\varphi),
 \qquad \mathcal E_0=\mathcal E_{\mathrm{env}}(X,\theta,0),
 \qquad \mu_u=\mathrm{MA}^{\mathrm{ext}}_\theta(u).
\]
The notation $Q_b$ refers to the convex competitor definition in \cref{def:relative-envelope-class}; differences at common poles are never assigned artificial values. The first envelope lemmas do not require a positive lower volume.

\section{Room below the reference potential}

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

\begin{lemma}\label{lem:relative-difference-envelope}
If $u\in\mathcal E_\varphi$ and $u\leq\varphi$, then
\[
 w=P_\theta(u-\varphi)\in\mathcal E_0,
 \qquad w\leq0,
 \qquad w+\varphi\leq u.
\]
\end{lemma}
\begin{proof}
Since $\varphi\leq0$, the potential $u$ is a competitor for the obstacle $u-\varphi$ away from its pole set. The envelope is genuine, bounded above by zero, and satisfies the asserted sum inequality by canonical representatives. For $b\geq1$, let $h_b=Q_b(u,\varphi)$. Then
\[
 h_b\leq bu-(b-1)\varphi\leq b(u-\varphi).
\]
Semipositivity makes $b^{-1}h_b$ a $\theta$-plurisubharmonic competitor for $w$. Hence $h_b\leq bw$, supplying a competitor for $P_\theta(bw)$ for every $b$. This is exactly $w\in\mathcal E_0$.
\end{proof}

\begin{proposition}\label{prop:relative-finite-rooftops}
The rooftop of any finite collection of members of $\mathcal E_\varphi$ is genuine and belongs to $\mathcal E_\varphi$.
\end{proposition}
\begin{proof}
It suffices first to produce a genuine rooftop for two members $u,v$. Translate them so that $u,v\leq\varphi$, and let $w_u,w_v\in\mathcal E_0$ be the preceding difference envelopes. Their rooftop $z=P_\theta(w_u,w_v)$ is genuine: the potential
\[
 \tfrac12P_\theta(2w_u)+\tfrac12P_\theta(2w_v)
 \leq w_u+w_v\leq\min(w_u,w_v)
\]
is a competitor. For each $b\geq1$, the same argument with $2b$ in place of $2$ gives a $\theta$-plurisubharmonic $h_b\leq b\min(w_u,w_v)$. Therefore $b^{-1}h_b\leq z$ and $P_\theta(bz)$ is genuine. Thus $z\in\mathcal E_0$.

Set $\delta=1-\varepsilon$ and $q=P_{\varepsilon\theta}(\varphi)$. Since $P_\theta(z/\delta)$ is genuine, the potential
\[
 \delta P_\theta(z/\delta)+q
 \leq z+\varphi\leq\min(u,v)
\]
is a genuine $\theta$-plurisubharmonic competitor. This proves nonemptiness of the rooftop for any pair in the class.

To prove class membership, put $u_b=Q_b(u,\varphi)$ and $v_b=Q_b(v,\varphi)$. They belong to $\mathcal E_\varphi$ by \cref{lem:relative-stretch-closure}, so the just-proved nonemptiness gives $r_b=P_\theta(u_b,v_b)$. If $p=P_\theta(u,v)$, then
\[
 b^{-1}r_b+(1-b^{-1})\varphi\leq p.
\]
Indeed, the left side is a $\theta$-plurisubharmonic competitor below both $u$ and $v$. This is a competitor for the defining $b$-condition of $p$. Since $p\leq u\preceq\varphi$, it proves $p\in\mathcal E_\varphi$. Iterate to handle a finite collection. These arguments reconstruct \cite[Propositions 3.5--3.7]{ALS26} in the precise forms needed here.
\end{proof}

\begin{lemma}\label{lem:smaller-background-mass-lower}
If $0<a<1$ and $q=P_{a\theta}(u)$ is genuine for $u\in\PSH(X,\theta)$, then
\[
 \int_X\mu_u\geq(1-a)^n v_-(\theta).
\]
The mass on the left is also strictly positive individually, even if $v_-(\theta)=0$.
\end{lemma}
\begin{proof}
The obstacle $u-q$ is nonnegative away from the poles. The bounded-below envelope lemma makes
$p=P_{(1-a)\theta}(u-q)$ bounded. Its measure is carried by $D=\{p+q=u\}$, and $p+q\leq u$ everywhere. Positivity of mixed products and ordered contact imply
\[
 \mathrm{MA}_{(1-a)\theta}(p)
 \leq\mathbf1_D\mathrm{MA}^{\mathrm{ext}}_\theta(p+q)
 \leq\mathbf1_D\mu_u.
\]
All assertions are first restricted away from the poles. Integrating and writing $p=(1-a)\widetilde p$ proves the lower bound from the definition of $v_-(\theta)$. The bounded potential $p$ has strictly positive mass by \cref{prop:big-noncollapsing}, since $(1-a)\theta$ is big. This proves the individual assertion as well.
\end{proof}

\begin{theorem}\label{thm:relative-uniform-mass-lower}
Every $u\in\mathcal E_\varphi$ admits a genuine $P_{(\varepsilon+\delta)\theta}(u)$ whenever $0<\delta<1-\varepsilon$. Consequently
\[
 \int_X\mu_u\geq(1-\varepsilon)^n v_-(\theta),
 \qquad \int_X\mu_u>0.
\]
The first bound is uniform over the class; the second is an individual assertion. Neither asserts finiteness.
\end{theorem}
\begin{proof}
Translate $u$ below $\varphi$ and use $w\in\mathcal E_0$ from \cref{lem:relative-difference-envelope}. The potential
\[
 P_{\varepsilon\theta}(\varphi)+\delta P_\theta(w/\delta)
 \leq\varphi+w\leq u
\]
has background $(\varepsilon+\delta)\theta$. It supplies the asserted competitor. Apply \cref{lem:smaller-background-mass-lower} and let $\delta\downarrow0$ for the uniform estimate. The individual conclusion follows by taking any one such $\delta$. This is the lower-volume mechanism of \cite[Proposition 3.8]{ALS26}.
\end{proof}

\section{Domination with one finite measure}

We now impose the separate condition
\begin{equation}\label{eq:relative-positive-lower-volume}
 v_-(\theta)>0.
\end{equation}
Set $\kappa=(1-\varepsilon)^n v_-(\theta)>0$. This condition concerns a lower bound. It is compatible with $v_+(\theta)=+\infty$, as the Hopf example shows.

\begin{theorem}\label{thm:relative-finite-domination}
Let $u\in\mathcal E_\varphi$ have finite $\mu_u$, and let $v\in\PSH(X,\theta)$ satisfy $v\preceq\varphi$. If, for some $0\leq c<1$,
\[
 \mu_u\leq c\mu_v\quad\hbox{on }\{u<v\},
\]
then $u\geq v$.
\end{theorem}
\begin{proof}
Replace $v$ by $w=\max(u,v)$. Upward stability gives $w\in\mathcal E_\varphi$ and locality gives $\mu_u\leq c\mu_w$ on $\{u<w\}$. For $b>1$ put $q_b=Q_b(u,w)\in\mathcal E_\varphi$. It satisfies $q_b\leq u$, and its measure is carried by
\[
 D_b=\{b^{-1}q_b+(1-b^{-1})w=u\}.
\]
On $D_b$, positivity and ordered contact give
\[
 b^{-n}\mu_{q_b}+(1-b^{-1})^n\mu_w\leq\mu_u.
\]
Choose $b$ so large that $(1-b^{-1})^n>c$. On $D_b\cap\{u<w\}$ the preceding inequality forces both $\mu_w$ and $\mu_{q_b}$ to vanish. To justify this even when $\mu_w(X)=+\infty$, restrict first to common finite truncation levels of the potentials. On each such set the measures are finite and subtraction is legitimate. Exhausting the complements of the pole sets proves the assertion for the extended measures.

It follows that $\mu_{q_b}$ is carried by $D_b\cap\{u=w\}\subseteq\{q_b=u\}$. Since $q_b\leq u$, another application of ordered contact gives the bound with coefficient one
\begin{equation}\label{eq:relative-contact-fixed-measure}
 \mu_{q_b}\leq\mathbf1_{\{q_b=u\}}\mu_u.
\end{equation}
This coefficient is independent of $b$.

Along integers $b\to\infty$, the potentials $q_b$ decrease. If they collapsed identically to $-\infty$, compactness and Hartogs' lemma would give $M_b:=\sup_Xq_b\to-\infty$. But \eqref{eq:relative-contact-fixed-measure} would then imply
\[
 \kappa\leq\int_X\mu_{q_b}
 \leq\mu_u(\{u\leq M_b\})\longrightarrow0.
\]
Here finiteness of $\mu_u$ and its vanishing on the pole set are exactly what gives the limit. This is impossible. Hence the decreasing limit $q$ is genuine. On $\{u<w-a\}$, for any $a>0$, the defining inequality gives $q_b\leq u-(b-1)a$. Outside the poles its limit is $-\infty$ there. Such a set has smooth volume zero because $q$ is genuine. Thus $u\geq w$ almost everywhere, and then everywhere for canonical representatives. This proves the theorem.
\end{proof}

The theorem reconstructs the finite-$\mu_u$ case of \cite[Theorem 3.14]{ALS26}. Its proof displays the fixed finite measure that prevents collapse. It does not assume that every member of $\mathcal E_\varphi$ has finite mass.

\Needspace{13\baselineskip}
\begin{corollary}\label{cor:relative-finite-exponential-order}
Under the hypotheses on $u,v$ in \cref{thm:relative-finite-domination}, let $\lambda>0$. Then
\[
 e^{-\lambda u}\mu_u\leq e^{-\lambda v}\mu_v
 \quad\Longrightarrow\quad u\geq v.
\]
Also $\mu_u\leq c\mu_v$ on $X$ with a finite constant $c\geq0$ implies $c\geq1$.
\end{corollary}
\begin{proof}
For each $a>0$, the exponential inequality gives $\mu_u\leq e^{-\lambda a}\mu_v$ on $\{u<v-a\}$. Apply the theorem to $v-a$ and then let $a\downarrow0$. The weights are finite and positive off the pole sets, so their cancellation is done there. If the second assertion failed, apply the theorem to $v+A$ for every real constant $A$, since its Monge--Amp\`ere measure is unchanged. The resulting inequalities $u\geq v+A$ contradict finiteness at a common point.
\end{proof}

In particular, two solutions in $\mathcal E_\varphi$ of an exponential equation with a fixed finite non-pluripolar right-hand measure must agree. Their Monge--Amp\`ere measures are finite because their potentials are bounded above. For the equation $\mu_u=c\nu$, the positive scalar is unique whenever two such finite-measure solutions exist. No assertion of uniqueness modulo constants for the zero-exponent potentials follows from this argument.


## New proof to audit completely

\section{Domination without a mass bound}

The finite-measure theorem also controls an auxiliary envelope whose finiteness follows from contact support. This permits us to remove the finiteness hypothesis on the original potentials. The standing assumption $v_-(\theta)>0$ remains in force.

\begin{lemma}\label{lem:relative-zero-domination}
Let $u,v\in\mathcal E_\varphi$ satisfy $u\leq v$. If
\[
 \mu_u(\{u<v\})=0,
\]
then $u=v$. The measures may have infinite total mass.
\end{lemma}
\begin{proof}
Translate both potentials by a common constant so that $u\leq v\leq\varphi\leq0$. Fix $\varepsilon<\delta<1$, put $\beta=1-\delta$, and set
\[
 q=P_{\delta\theta}(v).
\]
This envelope is genuine by \cref{thm:relative-uniform-mass-lower}. By \cref{lem:relative-difference-envelope},
\[
 w=P_\theta(u-\varphi)\in\mathcal E_0,
 \qquad w+\varphi\leq u,\qquad w\leq0.
\]
The stretching lemma with reference zero shows that
$z=P_\theta(w/\beta)$ belongs to $\mathcal E_0$. Scaling the background and each defining competitor gives
\[
 \beta z\in\mathcal E_{\mathrm{env}}(X,\beta\theta,0).
\]
Indeed, if $a\in\PSH(X,\theta)$ lies below $t z$, then $\beta a\in\PSH(X,\beta\theta)$ lies below $t\beta z$, for every $t\geq1$.

Since $q\leq v\leq\varphi$, we have
\[
 \beta z\leq w\leq u-\varphi\leq u-q
\]
off the pole sets. Thus
\[
 k=P_{\beta\theta}(u-q)
\]
is genuine. Here the difference obstacle is taken off the pluripolar pole sets; it is quasi-continuous and finite almost everywhere. The general envelope theorem gives a finite upper bound for $k$ and the canonical inequality $k+q\leq u$. Upward stability therefore gives
$k\in\mathcal E_{\mathrm{env}}(X,\beta\theta,0)$.

Write $\nu_k=\mathrm{MA}^{\mathrm{ext}}_{\beta\theta}(k)$. Contact support carries $\nu_k$ by
\[
 D=\{k+q=u\}
\]
outside the pole sets. Positivity of mixed products and ordered contact give
\[
 \nu_k\leq\mathbf1_D\mu_u.
\]
These inequalities are first restricted to common finite truncation levels and then exhausted. On $D\cap\{k<0\}$ we have $u=k+q<q\leq v$, so $\nu_k(\{k<0\})=0$.

This vanishing proves that $\nu_k$ is finite. In fact, $\widehat k=\max(k,-1)$ is a single bounded $\beta\theta$-plurisubharmonic function, and locality gives
\[
 \nu_k(X)=\nu_k(\{k\geq0\})
 =\int_{\{k\geq0\}}\mathrm{MA}_{\beta\theta}(\widehat k)
 \leq\int_X\mathrm{MA}_{\beta\theta}(\widehat k)<\infty.
\]
The last bound concerns one bounded potential; it is not a bounded mass assumption.

Apply \cref{thm:relative-finite-domination} in the background $\beta\theta$, with reference zero and potentials $k,0$, using coefficient zero. Its hypotheses hold: $\beta\theta$ is semipositive and big, zero satisfies the model condition, and
\[
 v_-(\beta\theta)=\beta^n v_-(\theta)>0.
\]
The scaling identity follows by the bijection $a\mapsto\beta a$ between bounded potentials in the two backgrounds. We have just proved finiteness of $\nu_k$. The theorem yields $k\geq0$, hence $u\geq q$.

To pass to $\delta\uparrow1$, fix $\delta_0\in(\varepsilon,1)$ and $r=P_{\delta_0\theta}(v)$. For $\delta_0<\delta<1$, set $t=(\delta-\delta_0)/(1-\delta_0)$. The potential $t v+(1-t)r$ has background $\delta\theta$ and lies below $v$. Therefore
\[
 u\geq P_{\delta\theta}(v)\geq t v+(1-t)r.
\]
Let $t\uparrow1$ at points where $v,r$ are finite. This gives $u\geq v$ almost everywhere, and then everywhere by the canonical representatives. Together with $u\leq v$, it proves equality.
\end{proof}

\begin{theorem}\label{thm:relative-extended-domination}
Let $u\in\mathcal E_\varphi$ and $v\in\PSH(X,\theta)$ with $v\preceq\varphi$. If $0\leq c<1$ and
\[
 \mu_u\leq c\mu_v\quad\hbox{on }\{u<v\},
\]
then $u\geq v$. Neither measure is required to have finite mass.
\end{theorem}
\begin{proof}
Put $w=\max(u,v)\in\mathcal E_\varphi$ and choose $b>1$ with $(1-b^{-1})^n>c$. The stretching lemma gives $p=Q_b(u,w)\in\mathcal E_\varphi$ and $p\leq u$. Its measure is carried by
\[
 D=\{b^{-1}p+(1-b^{-1})w=u\}.
\]
On $D$, positivity and ordered contact imply
\[
 b^{-n}\mu_p+(1-b^{-1})^n\mu_w\leq\mu_u.
\]
On $\{u<w\}$, locality gives $\mu_u\leq c\mu_w$. Restricting both inequalities to $D\cap\{u<w\}$ and to common finite truncation levels makes subtraction legitimate. Since $(1-b^{-1})^n>c$, it follows that $\mu_p$ vanishes there. Exhausting the finite levels proves that $\mu_p$ is carried by $D\cap\{u=w\}\subseteq\{p=u\}$. Thus $\mu_p(\{p<u\})=0$.

Apply \cref{lem:relative-zero-domination} to $p\leq u$, both in $\mathcal E_\varphi$. It yields $p=u$. Substitution into the defining convex inequality for $p$ gives $w\leq u$ off the poles, hence everywhere by canonical representatives. Since $v\leq w$, the result follows.
\end{proof}

\begin{corollary}\label{cor:relative-extended-exponential-order}
Under the hypotheses on $u,v$ in \cref{thm:relative-extended-domination}, for every $\lambda>0$,
\[
 e^{-\lambda u}\mu_u\leq e^{-\lambda v}\mu_v
 \quad\Longrightarrow\quad u\geq v.
\]
Also $\mu_u\leq c\mu_v$ on $X$ for a finite constant $c\geq0$ implies $c\geq1$.
\end{corollary}
\begin{proof}
On $\{u<v-a\}$ the exponential inequality gives $\mu_u\leq e^{-\lambda a}\mu_v$. Apply the theorem to $v-a$ and let $a\downarrow0$. All weights are taken off the pluripolar pole sets. For the second assertion, if $c<1$, applying the theorem to $v+A$ for every real $A$ contradicts finiteness of both potentials at a common point.
\end{proof}

The proof is ordered to avoid circularity: finite-measure domination is established first, then used only for the auxiliary potential $k$, whose measure has already been proved finite. The original potentials and the stretched envelope $p$ need no upper mass estimate.
