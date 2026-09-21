Run_id: relative_equivalence_01

Statement: Conditional on Inputs A, C, K, and V below, on a compact connected complex n-manifold with the bounded mass property and a smooth real big (1,1)-form theta, if phi is theta-psh and has strictly positive lower singularity volume, the envelope and upper-volume definitions of relative full mass coincide. Both lower and upper volumes agree with those of phi for every member. In particular, no additional global positive volume property is needed for this equivalence of definitions. Verify the proof, not a novelty claim or the existence theorems in the literature.

Use ddc=i/(2pi) partial bar-partial and canonical quasi-psh representatives. u preceq v means u<=v+C. u simeq v means both orders. theta is big if it contains a strictly positive current. Under bounded mass, all positive mixed non-pluripolar products of quasi-closed currents used here are finite, positive, multilinear, and ignore pluripolar sets.

Input A: Non-pluripolar products have plurifine locality and positivity as just stated. Maxima of theta-psh potentials are theta-psh. Every such potential is bounded above, integrable with respect to smooth volume and finite outside a pluripolar set. A quasi-psh inequality holding almost everywhere holds everywhere for canonical representatives.

Input C: If f is quasi-continuous (in particular a difference of quasi-psh functions away from poles) and P_theta(f) is a genuine theta-psh envelope, its measure is supported on its contact set with f, and it is below f outside a pluripolar set. If p<=q are theta-psh, then 1_{p=q}MA_theta(p)<=1_{p=q}MA_theta(q). For b>1 define Q_b(u,phi) as the usc envelope of h in PSH(theta) with b^{-1}h+(1-b^{-1})phi<=u. The inequality uses sums rather than undefined differences at common poles. If the family is nonempty, it is bounded above, gives a genuine theta-psh envelope, and the defining convex inequality holds everywhere. If empty, Q_b=-infinity. All these statements also hold for every other big background below.

Input K: For a fixed smooth background the normalized theta-psh family sup_X h=0 has uniformly bounded L1 norms and is L1 precompact. A decreasing sequence of theta-psh functions either has a genuine theta-psh limit or tends identically to minus infinity; in the latter case its suprema on compact X tend to minus infinity (Hartogs lemma). The limit of decreasing Q_b targets as u_j decreases to u is Q_b(u,phi), by passing the convex inequality to the limit whenever the limit is genuine.

Definitions: lower_vol_theta(u)=inf int_X MA_theta(w) and upper_vol_theta(u)=sup int_X MA_theta(w), over all theta-psh w simeq u. Under bounded mass they are finite and nonnegative. Their values are constant on ordinary singularity types. E_env={u theta-psh:u preceq phi and Q_b(u,phi) genuine for every b>=1}; Q_1(u,phi)=u. E_vol={u theta-psh:u preceq phi and upper_vol_theta(u)=upper_vol_theta(phi)}.

Input V: Both singularity volumes are monotone in the singularity order in a fixed big background: u preceq v implies vol_theta(u)<=vol_theta(v). They scale by vol_{t theta}(tu)=t^n vol_theta(u). They increase on adding a positive quasi-closed current to a current in a big class: vol_theta(u)<=vol_{theta+eta}(u+v) whenever theta is big, u theta-psh and v eta-psh. This is an explicit hypothesis of this conditional verification, not a citation requiring proof here.

Proof (the text is LaTeX, with the preceding input statements supplying the named references):

\begin{theorem}[Equivalence of the two full mass definitions]\label{thm:relative-equivalence}
Suppose $X$ has bounded mass, $\theta$ is big, and
$\underline{\operatorname{vol}}_\theta(\varphi)>0$. Then
\[
 \mathcal E_{\mathrm{env}}(X,\theta,\varphi)
 =\mathcal E_{\mathrm{vol}}(X,\theta,\varphi).
\]
Every member also satisfies
$\underline{\operatorname{vol}}_\theta(u)
=\underline{\operatorname{vol}}_\theta(\varphi)$.
\end{theorem}
\begin{proof}
First assume the envelope condition. For each $a\in(0,1)$ there is $h\in\PSH(X,\theta)$ such that $a\varphi+(1-a)h\leq u$. By \cref{thm:volume-monotonicity,prop:volume-addition} and homogeneity, for either volume,
\[
 a^n\operatorname{vol}_\theta(\varphi)
 \leq\operatorname{vol}_\theta(a\varphi+(1-a)h)
 \leq\operatorname{vol}_\theta(u)
 \leq\operatorname{vol}_\theta(\varphi).
\]
Let $a\to1$. This proves equality of both volumes in this direction, even without positive lower volume.

Conversely, suppose equality of the upper volumes, and fix $b>1$. Shift the potentials so that $u\leq\varphi\leq0$, and put
\[
 u_j=\max(u,\varphi-j),\qquad q_j=Q_b(u_j,\varphi).
\]
Each $q_j$ is genuine and equivalent to $\varphi$: the lower competitor $\varphi-bj$ and the defining inequality give
$\varphi-bj\leq q_j\leq\varphi$.
The sequence decreases. If its limit were $-\infty$, the compactness and Hartogs lemma for normalized quasi-plurisubharmonic functions would give $\sup_Xq_j\to-\infty$.

Set $C_j=\{b^{-1}q_j+(1-b^{-1})\varphi=u_j\}$. The contact theorem and positivity of mixed products give
\[
 \mathrm{MA}_\theta(q_j)
 \leq b^n\mathbf1_{C_j}\mathrm{MA}_\theta(u_j).
\]
On $C_j\cap\{q_j\leq-bk\}$, the inequality $\varphi\leq0$ implies $u_j\leq-k$, hence $u\leq-k$. For $j>k$, locality on $\{u>-k\}\subset\{u>\varphi-j\}$ therefore yields
\[
 \begin{split}
 \int_{\{q_j\leq-bk\}}\mathrm{MA}_\theta(q_j)
 &\leq b^n\int_{\{u\leq-k\}}\mathrm{MA}_\theta(u_j)\\
 &\leq b^n\left(
 \overline{\operatorname{vol}}_\theta(\varphi)
 -\int_{\{u>-k\}}\mathrm{MA}_\theta(u)\right).
 \end{split}
\]
If $\sup_Xq_j\to-\infty$, the domain on the left is all of $X$ for large $j$. It follows, on letting $k\to+\infty$, that
\[
 \underline{\operatorname{vol}}_\theta(\varphi)
 \leq b^n\left(
 \overline{\operatorname{vol}}_\theta(\varphi)
 -\int_X\mathrm{MA}_\theta(u)\right).
\]
The same collapse would hold with any $u'\simeq u$ in place of $u$: a competitor for either target gives one for the other by a constant translation. Repeating the argument and taking the supremum of $\int_X\mathrm{MA}_\theta(u')$ gives
\[
 \underline{\operatorname{vol}}_\theta(\varphi)
 \leq b^n\left(
 \overline{\operatorname{vol}}_\theta(\varphi)
 -\overline{\operatorname{vol}}_\theta(u)\right)=0,
\]
a contradiction. Thus $Q_b(u,\varphi)$ is genuine for every $b$. The argument is the full-volume case of \cite[Lemma 3.1]{XL26}; the proof uses bounded mass and the displayed positive lower volume, without a separate global positive volume hypothesis.
\end{proof}


Instructions: Use the Rethlas verification AGENTS.md and three required verification skills, verifying every deduction sequentially. Inputs A,C,K,V are hypotheses of this conditional theorem; do not claim to verify them independently. The source attribution at the end is contextual and is not a replacement for any proof step. Check especially the family nonemptiness, whether q_j is equivalent to phi, contact-set inequalities, use of j>k, the order of limits, changing u by a bounded amount, and the supremum versus infimum over equivalent potentials. Produce results/relative_equivalence_01/verification.json. Do not edit the manuscript or files outside this copied verification workspace.
