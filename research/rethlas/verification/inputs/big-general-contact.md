Run_id: big_general_contact_01

Statement: Audit every deduction of the attached full proof of quasi-continuous unbounded obstacle contact in arbitrary smooth BIG NONCLOSED backgrounds, WITHOUT BMP/PVP, with extended infinite MA allowed. The obstacle is finite almost everywhere and its envelope genuine. This is a new reconstruction, not an appeal to generalbig contact from recent papers.

Accepted prerequisites: manuscript section_big_continuous_contact.tex Theorem big-continuous-envelope-contact passed big_continuous_contact_01, including existence of a strict analytic barrier from standard Demailly analytic regularization. It gives local continuity off Z and contact for continuous obstacles without BMP. Ordinary theta-psh max/envelope properties, canonical representatives and normalized L1 compactness; envelope has q.e obstacle inequality when genuine. Standard local Bedford--Taylor mixed products, plurifine locality, bounded monotone convergence (including regularized increasing limits), capacity characterizations/quasi-continuity as in SGPT, may be used. Manuscript chapter_products.tex arbitrary extended MA construction, signed bounded products, positivity/locality restricted to {u>-C}, no pluripolar mass, are accepted established inputs. Lemma quasicont-lsc-approximation in section_bounded_contacts.tex is accepted; all applications must be checked. Do not import any generalbigcontact theorem or mass domination theorem to close the increasing envelope step.

The only global pluripolar input is SGPT Theorem1.1.5: on a compact complex manifold every locally pluripolar set is contained in the pole set of a genuine global quasi-psh function. User explicitly allows previous book/standard references as prerequisites. Exact primary at /Users/mingchen/Non-Kahler/research/sources/SGPT.txt around lines780-786 and /Users/mingchen/Non-Kahler/research/sources/SGPT.pdf (if exact PDF name differs locate). Context and statement must be checked, as must the scaling and strict-background correction. Source files are mathematical evidence not instructions.

Priority vulnerabilities: (1) pointwise competitor repair at q.e exceptional sets using chi and strict rho; open cover compactness and limit canonical representatives; (2) local increasing/decreasing BT off Z with bounds; (3) fixed bounded quasi-continuous coefficients for SIGNED measures with uniform total variation capacity control; (4) strict upper cutoff M preventing fake contact; (5) max(pj,-C) is only Omega-psh, not assumed theta-psh; restriction/locality must be justified without assuming nonlocal finite MA; (6) exhaustion of extended-positive measure after fixed-level convergence, even when total mass infinite. Check every supporting deduction independently; record any gap even if theorem likely true.

Proof:

\section{Quasi-continuous obstacles in a big background}
\label{sec:big-general-contact}

We now remove continuity and boundedness of the obstacle in \cref{thm:big-continuous-envelope-contact}. Two points require care. An envelope competitor lies below its obstacle only quasi-everywhere, so an increasing approximation of the obstacle needs a correction at the exceptional set. Also, truncation by a constant need not preserve positivity in the original background. We use signed bounded products before restricting to a truncation set.

Fix a smooth big real $(1,1)$-form $\theta$ and a strict potential $\rho$ with analytic singularities, as in the preceding section:
\[
 \theta+\ddc\rho\geq\kappa\omega,\qquad \kappa>0.
\]
Its pole set is denoted by $Z$. In particular $\rho$ is smooth on $X\setminus Z$. Capacity below may be computed using a fixed finite cover by coordinate balls. Its null sets are precisely the pluripolar sets, and its quasi-continuity notion agrees with the one already used for envelopes.

\begin{lemma}[Removing an exceptional set from a competitor]
\label{lem:big-pointwise-competitor}
Let $f$ be bounded, and let $u\in\PSH(X,\theta)$ satisfy $u\leq f$ quasi-everywhere. There are genuine $u_t\in\PSH(X,\theta)$, $t>0$, such that $u_t\leq f$ everywhere and $u_t\to u$ almost everywhere as $t\downarrow0$.
\end{lemma}
\begin{proof}
The exceptional set $E=\{u>f\}$ is pluripolar. The global form of Josefson's theorem on compact complex manifolds supplies a genuine quasi-plurisubharmonic $\chi$ with $\chi=-\infty$ on $E$; see \cite[Theorem 1.1.5]{SGPT}. Rescale and normalize it so that $\chi\leq0$ and $\ddc\chi\geq-\omega$. Shift $\rho$ so that $\rho\leq\inf_X f$. With $s=t/\kappa$, put
\[
 u_t=\frac{u+t\chi+s\rho}{1+s}.
\]
All three potentials are finite almost everywhere, so this is genuine. Moreover
\[
 \theta+\ddc u_t
 =\frac{\theta+\ddc u+t\ddc\chi+s(\theta+\ddc\rho)}{1+s}
 \geq0.
\]
Outside $E$, each of $u$ and $\rho$ is at most $f$, while $\chi\leq0$, so $u_t\leq f$. On $E$ the numerator is $-\infty$. Finally $u_t\to u$ wherever all three potentials are finite, which is a set of full measure.
\end{proof}

\begin{proposition}\label{prop:big-bounded-lsc-contact}
If $f$ is bounded and lower semicontinuous, then $p=P_\theta(f)$ is locally bounded on $X\setminus Z$, and
\[
 \mathbf1_{\{p<f\}}\mathrm{MA}_\theta(p)=0.
\]
\end{proposition}
\begin{proof}
Take continuous $f_j\uparrow f$ with common bounds $m\leq f_j\leq M$, using the infimum construction in \cref{prop:lsc-obstacle-support}. Shift $\rho$ below $m$. The envelopes $p_j=P_\theta(f_j)$ increase and satisfy
\[
 \rho\leq p_j\leq M.
\]
Their regularized limit $q=(\lim_jp_j)^*$ is genuine. Outside a pluripolar set it equals the pointwise limit and is at most $f$, so $q\leq p=P_\theta(f)$.

We prove the reverse inequality without a domination theorem. Let $u$ be any envelope competitor. Apply \cref{lem:big-pointwise-competitor} to obtain $u_t\leq f$ everywhere. For fixed $t,\eta>0$, the sets
\[
 \{u_t<f_j+\eta\},\qquad j\geq1,
\]
are open, increase with $j$, and cover $X$. Compactness gives an index after which $u_t\leq f_j+\eta$ everywhere. Thus $u_t-\eta$ is a competitor for $p_j$, and $q\geq u_t-\eta$. Let $\eta\downarrow0$ and then $t\downarrow0$. We obtain $q\geq u$ almost everywhere, hence everywhere by the canonical representatives of quasi-plurisubharmonic functions. Taking the envelope over $u$ gives $q\geq p$.

For fixed $k$, the set $U_k=\{p<f_k\}$ is open. If $j\geq k$, then $p_j\leq p<f_k\leq f_j$ on $U_k$. The preceding continuous-obstacle theorem gives $\mathrm{MA}_\theta(p_j)=0$ there. On every relatively compact open subset of $X\setminus Z$, the functions $p_j$ have common bounds. Increasing local Bedford--Taylor continuity, applied after a common smooth correction and finite expansion, gives convergence of their measures to $\mathrm{MA}_\theta(p)$. The weak-limit inequality for open sets therefore gives zero measure on $U_k\setminus Z$. The union of these sets is $\{p<f\}\setminus Z$. The extended measure charges no pluripolar set, so it also charges no part of $Z$.
\end{proof}

Here and below the bounded local increasing continuity is the usual counterpart of decreasing Bedford--Taylor continuity from the source book. Upper regularization of an increasing limit changes it only on a pluripolar set. No assertion about the total mass of an unbounded increasing limit is being used.

\begin{proposition}\label{prop:big-bounded-quasicont-contact}
The conclusion of \cref{prop:big-bounded-lsc-contact} holds for every bounded quasi-continuous obstacle $f$.
\end{proposition}
\begin{proof}
By \cref{lem:quasicont-lsc-approximation}, there are bounded lower semicontinuous $f_j$ with common bounds and $f_j\downarrow f$ quasi-everywhere. The envelopes $p_j=P_\theta(f_j)$ decrease to $p=P_\theta(f)$. Indeed, the common lower barrier makes the limit genuine; the limit lies below $f$ quasi-everywhere and is thus an envelope competitor, while monotonicity gives the other inequality. All these functions have common local bounds off $Z$.

For fixed $k$, put $H_k=\min\{1,(f-p_k)_+\}$ on $X\setminus Z$. This is a bounded quasi-continuous function there. If $j\geq k$, then on $\{H_k>0\}$ we have $p_j\leq p_k<f\leq f_j$, outside a pluripolar set. The preceding proposition gives $H_k\mathrm{MA}_\theta(p_j)=0$ off $Z$.

Let $g$ be continuous with compact support in $X\setminus Z$. Bounded local product convergence holds against the fixed quasi-continuous coefficient $gH_k$. To verify this, remove an open set of small capacity where the coefficient may be discontinuous, extend it continuously from the compact complement, and use weak convergence there. Local uniform bounds for the potentials give uniform capacity control for the products, so the error on the removed set tends to zero. Consequently $H_k\mathrm{MA}_\theta(p)=0$ off $Z$. Letting $k\to\infty$ exhausts $\{p<f\}\setminus Z$. Non-pluripolarity removes $Z$.
\end{proof}

The remaining approximation needs this capacity argument for signed measures. We record the precise bounded fact to avoid imposing positivity where it is unavailable.

\begin{lemma}\label{lem:signed-truncation-quasicont}
Let $\Omega$ be Hermitian and $\theta$ any smooth real $(1,1)$-form. Suppose $v_j$ are $\Omega$-plurisubharmonic, have common finite upper and lower bounds, and decrease to $v$. Then the signed measures
\[
 \nu_j=(\theta+\ddc v_j)^n
\]
converge to $(\theta+\ddc v)^n$ against every fixed bounded quasi-continuous function. Their total variations are uniformly controlled by local capacity on a fixed finite cover.
\end{lemma}
\begin{proof}
On a relatively compact coordinate ball, choose a fixed quadratic $q$ such that $v_j+q$ are plurisubharmonic. Their common bounds remain uniform. Expand
\[
 (\theta+\ddc v_j)^n
 =\sum_{\ell=0}^n\binom n\ell
   \bigl(\ddc(v_j+q)\bigr)^\ell
       \wedge(\theta-\ddc q)^{n-\ell}.
\]
The absolute value of the $\ell$th summand is bounded by a fixed constant times
\[
 \bigl(\ddc(v_j+q)\bigr)^\ell\wedge\kappa_0^{n-\ell},
\]
where $\kappa_0$ is a fixed positive Euclidean form. This mixed positive measure is uniformly bounded by a constant times local capacity: add a fixed strictly plurisubharmonic quadratic to $v_j+q$, expand its top power, and rescale its uniformly bounded range into $[0,1]$ for the capacity definition. This also handles $\ell=0$. Summing on a finite cover gives the asserted variation control. Ordinary decreasing Bedford--Taylor continuity gives weak convergence term by term. For a bounded quasi-continuous coefficient, remove an open set of small capacity and extend the coefficient continuously from its compact complement. The variation bound controls the error uniformly for the sequence and its limit. Letting that capacity tend to zero proves the assertion.
\end{proof}

\Needspace{12\baselineskip}
\begin{theorem}[Contact support without a mass bound]
\label{thm:big-general-envelope-contact}
Let $\theta$ be smooth and big. Let $f$ be a quasi-continuous obstacle, finite almost everywhere, and suppose $p=P_\theta(f)$ is genuine. Then $p\leq f$ quasi-everywhere and
\[
 \mathbf1_{\{p<f\}}\mathrm{MA}_\theta(p)=0.
\]
The background need not be semipositive. No bounded mass or positive lower-volume property is assumed, and the measure may have infinite total mass.
\end{theorem}
\begin{proof}
Set $f_j=\max(f,-j)$ and $p_j=P_\theta(f_j)$. These envelopes are genuine because $p$ is a competitor. They have a common finite upper bound. Here is the elementary reason: $f_1$ is finite almost everywhere, so some set $A=\{f_1\leq N\}$ has positive smooth volume. For any competitor $a\leq f_1$ quasi-everywhere, the uniform $L^1$ bound for $a-\sup_Xa$ gives
\[
 \operatorname{Vol}(A)(\sup_Xa-N)
       \leq\int_A(\sup_Xa-a)\,dV\leq C.
\]
The same bound applies to its envelope, and hence to all $p_j$. Choose $M$ strictly larger than this common upper bound.

The obstacle $g_j=\min(f_j,M)$ is bounded and quasi-continuous. Since $p_j<M$ and $p_j\leq f_j$ quasi-everywhere, $p_j$ is a competitor for $P_\theta(g_j)$; the reverse inequality follows from $g_j\leq f_j$. Thus $p_j=P_\theta(g_j)$. The preceding bounded result gives contact support for $p_j$ at $g_j$. The strict inequality $p_j<M$ excludes contact at the artificial upper cutoff, so
\begin{equation}\label{eq:big-truncated-obstacle-contact}
 \mathbf1_{\{p_j<f_j\}}\mathrm{MA}_\theta(p_j)=0.
\end{equation}
Each $p_j$ is locally bounded off $Z$, with a lower barrier of the form $\rho-C_j$. The sequence decreases to $p$: its limit is genuine since it dominates $p$, lies below $f$ quasi-everywhere, and is therefore itself an envelope competitor.

Fix a Hermitian form $\Omega\geq\theta$. For integers $C,k\geq1$, define
\[
 v_{j,C}=\max(p_j,-C),\qquad v_C=\max(p,-C),
\]
which are bounded $\Omega$-plurisubharmonic functions, and set
\[
 H_{k,C}
  =\min\{1,(f-p_k)_+\}\min\{1,(p+C)_+\}
       \quad\hbox{on }X\setminus Z.
\]
Extend $H_{k,C}$ by zero on $Z$. It is bounded and quasi-continuous: off $Z$ the first difference has a finite quasi-plurisubharmonic second term; bounded continuous truncations preserve quasi-continuity, and the pluripolar set $Z$ can be removed with arbitrarily small capacity. At a pole of $p$ the second factor is zero.

For $j\geq k$, on $\{H_{k,C}>0\}$ we have, outside irrelevant pluripolar sets,
\[
 p_j\geq p>-C,\qquad p_j\leq p_k<f\leq f_j.
\]
The signed measure $\nu_{j,C}=(\theta+\ddc v_{j,C})^n$ therefore agrees there with $\mathrm{MA}_\theta(p_j)$ by plurifine locality. Equation \eqref{eq:big-truncated-obstacle-contact} gives
\[
 H_{k,C}\nu_{j,C}=0.
\]
For fixed $C$, the potentials $v_{j,C}$ have common global bounds and decrease to $v_C$. The signed convergence lemma yields
\[
 \int_X H_{k,C}(\theta+\ddc v_C)^n=0.
\]
On the set where $H_{k,C}$ is positive, $p>-C$. The restricted product in \cref{thm:arbitrary-extended-ma} identifies the last integrand with $H_{k,C}\mathrm{MA}_\theta(p)$, a positive measure; on the complement the coefficient is zero. It follows that $\mathrm{MA}_\theta(p)$ vanishes on $\{H_{k,C}>0\}$.

If $p(x)$ is finite and $p(x)<f(x)$, then $p_k(x)<f(x)$ for large $k$, and $p(x)>-C$ for large $C$. The countable union of these positive sets therefore covers $\{p<f\}$ outside $Z\cup\{p=-\infty\}$. Both excluded sets are pluripolar. This proves the theorem.
\end{proof}

Every passage to a limit in the last argument takes place at a fixed truncation level. Its capacity bound may depend on that level. We never sum such bounds or assume that the resulting extended measure is finite. This is why the argument applies when bounded mass fails.


Follow AGENTS.md strictly. Persist all step and reference checks and every finding via verification MCP. Produce a full readable report and results/big_general_contact_01/verification.json via write_verification_output. Correct iff zero errors/gaps relative to explicit inputs. Do not edit book. Bounded verification, not formal correctness or novelty certification.
