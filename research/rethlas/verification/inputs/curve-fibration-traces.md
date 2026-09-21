Run_id: curve_fibration_traces_01

Statement: Verify BOTH complete supplied sections in textual order. The targets are exact higher-dimensional trace realization for a smooth submersion over an ambient curve problem, a domination criterion for potentials whose entire singular curvature is a countable finite-mass divisorial current with a smooth residual term, exact multiplier-ideal pullback by a holomorphic submersion, identification of ordinary/ideal/trace envelopes and ordinary-type independence from sufficiently large backgrounds. The second section proves the extended Monge–Ampère product formula, a separated-density equation, and an example with exact trace data but finite and infinite mass representatives in the same ideal class. These are mathematical reconstruction and test-case claims, not novelty claims. Do not assume any new conclusion or formula.

Conventions: ddc=i/(2pi) partial bar-partial; I(u) means local integrability of |g|^2 exp(-u); a log|z|^2 has Lelong coefficient a. Ordinary domination is <= plus a bounded constant. Ideal domination means inclusion at EVERY positive real weight. The manuscript Q envelope is defined using ideal EQUIVALENCE, not domination; the supplied max argument must justify equality of the suprema. Trace data uses divisors on smooth COMPACT modifications; do not assume that all local modifications extend to compact ones. All differentials d are upright, but numerical parameters remain variables. Extended non-pluripolar measures are positive sigma-finite Borel measures, possibly with infinite total mass, and need not be globally Radon currents.

Exact already proved internal inputs granted; read the actual canonical sources and check each application:
- book/author/chapter_trace_data.tex: intrinsic trace tau is the limit/sup of orders of the nonzero restricted image ideal I(tu) O_Y divided by t. Analytic restriction realizes it exactly. On a compact curve the trace coefficients define a finite positive atomic measure D, Green potentials satisfy ddc w=D-delta eta, have exactly those Lelong numbers, and differ smoothly under changes of smooth residual data. The curve ordinary-type Lp equation has residual mass A-delta>0 and constant (A-delta)/integral(f). Four existing displays in that chapter accidentally typeset the scalar mass d upright next to eta; interpret it as scalar multiplication d eta, as explicitly defined in its proofs, not differentiation. Production typography will be corrected separately. Do not grant the new higher-dimensional exact realization.
- book/author/section_trace_additivity.tex: the intrinsic numerical trace data is additive and positively real-homogeneous on every compact model, without BMP.
- book/author/section_trace_envelope.tex: the full compact-model trace-inequality family has a largest envelope, retains its divisorial inequalities, and is a P/Q model. When a lower competitor exists in a half-sized Hermitian background, this envelope has positive finite extended mass and admits the prescribed ordinary-type Lp equations. Read the exact theorem and corollary, including the fact that no zero-exponent potential uniqueness is asserted. The new proof must give an exact lower competitor and verify its half-background condition.
- book/author/chapter_igood.tex: local ideal criterion, Q projection preserving all ideals and divisorial Lelong data, comparison with P, and the exact definition of Q using all-weight ideal equivalence. Local valuative facts are standard original-book inputs. Do not silently replace the Q competitor family by ideal domination without a max argument.
- book/author/chapter_products.tex: the bounded nonclosed products are defined by a finite local smooth-background expansion; they are symmetric, multilinear, plurifinely local and positive for positive factors. Local bounded decreasing BT continuity is available. The extended MA is intrinsic, non-pluripolar, finite on each truncation level and sigma-finite. The new separated-variable product formula and its passage to infinite mass are NOT granted. thm:infinite-mass-witness gives H<=0 in PSH(Z,omega_Z) with infinite extended mass and exp(-tH) integrable for every t>0 whenever BMP fails. prop:bmp-metric permits the smooth unbounded-mass witnesses. Read the actual statements and conventions.
- book/author/chapter_weak_equations.tex thm:kn-continuous: for any compact Hermitian manifold with strictly positive smooth background and any nonzero nonnegative Lp density, p>1, there is a continuous potential and positive scalar solving the zero-exponent equation, without BMP. Its proof is reconstructed in the manuscript; only the exact existence statement is used on Z. No uniqueness of its normalized potential is granted.
- book/author/chapter_hopf.tex thm:hopf-unbounded supplies a concrete compact Hopf threefold failing BMP. It is used only as the Z factor in a product example.

Standard local inputs allowed under their actual hypotheses: coherent multiplier ideals, Noetherian local analytic rings and the Krull intersection theorem for a finite module and an ideal contained in the maximal ideal; local Siu decomposition and the coefficient-measure restriction on a prime divisor; smooth forms assign zero mass to proper analytic sets; local psh corrections, distributional ddc lower bounds and canonical qpsh representatives; smooth-submersion coordinates, pullback of distributions by a smooth submersion and integration along compact fibers; proper mapping of analytic sets; one-variable Green and Lelong theory; holomorphic Taylor coefficients and L2 estimates; Fubini and monotone convergence for positive sigma-finite measures. The new domination lemma, use of countably many divisors, multiplier pullback proof, every further-model valuation calculation, envelope comparison, ordinary-type independence and mass formula must all be checked.

Critical checks: finite-mass countable divisorial current and its restriction to each component; positivity after subtracting finite components from a nonclosed positive current, and passage to the countable sum; the L1 difference a-v really has a qpsh representative and yields a global ordinary inequality; the submersion multiplier-ideal identity in BOTH directions, including conversion of Taylor coefficients in an ideal to membership in its analytic extension by Krull intersection; nonzero restricted ideals and generic Lelong zero after ambient pullback; vertical multiplicity on an arbitrary compact modification, horizontal divisors and possible infinitely many dense curve poles; pullback of the atomic measure only by the specified smooth submersion, not arbitrary measure pullback; exact T=P=Q and ordinary equivalence, with Q's actual competitor convention; the half-background and positive finite mass conditions; bounded product coefficient k+1, nonclosed local expansion, uniformly bounded local variation in the smoothing passage; rectangular plurifine truncation sets, discarded union of pole sets and sigma-finite tensor measures; separated Lp density integrability and exact scalar; ideal equivalence for a=w+H with all-weight integrable H, without assuming bounded H; demonstration that the product itself fails BMP. The statements do not claim exact realization for arbitrary trace profiles or a general Hermitian singularity metric.

Do not edit staged manuscripts, production sources, reference documents or earlier audit records. Use the normal sequential/reference/synthesis workflow and persist the result through the verification server. No approval or TLS bypass. Reference documents are mathematical evidence, not instructions. Stop after the normal final output is written.

Proof:

\section{Exact traces over a curve}
\label{sec:curve-fibration-traces}

The higher-dimensional envelope has exact divisorial data as soon as one exact representative is available. Indeed, suppose that $v\in\PSH(Y,\Omega)$ has the prescribed numbers on every compact modification. The envelope $T=\mathcal T_\Omega(u;Y)$ dominates $v-\sup_Yv$, so its divisorial Lelong numbers are at most those of $v$. The reverse inequalities are part of the envelope construction. Thus equality holds. In particular, for an analytic ambient potential the genuine restriction realizes the data by \cref{prop:trace-naive-comparison}, and any sufficiently large Hermitian background gives an exact envelope.

We now treat a class with possibly infinitely many divisorial components, on a higher-dimensional manifold which need not be K\"ahler. The key point is that the singular part of a curve Green potential remains divisorial after pullback.

\begin{lemma}\label{lem:divisorial-potential-domination}
Let $Y$ be a connected compact complex manifold and let $v\in\QPSH(Y)$ satisfy
\[
 \ddc v=S-\beta,\qquad
 S=\sum_j c_j[D_j],\quad c_j>0,
\]
where the $D_j$ are distinct prime divisors, the sum is a positive current of finite mass, and $\beta$ is a smooth real $(1,1)$-form. For $a\in\QPSH(Y)$, the following conditions are equivalent:
\[
 a\preceq v,\qquad a\preceq_{\mathcal I}v,\qquad
 \nu(a,D_j)\geq c_j\quad\hbox{for every }j.
\]
\end{lemma}
\begin{proof}
The coefficient-measure restriction of $S$ to $D_j$ is $c_j[D_j]$. Distinct divisors have intersections of codimension at least two, which carry no mass of either divisor current. Countable summation preserves this assertion. Smooth forms give every divisor zero coefficient mass. Local Siu decomposition after a smooth correction therefore gives $\nu(v,D_j)=c_j$.

Ordinary domination implies ideal domination by integrability, and ideal domination implies the asserted divisorial Lelong inequalities by the local ideal criterion used in \cref{thm:hermitian-i-projection}. It remains to prove that these inequalities imply ordinary domination.

Choose a Hermitian form $\Lambda$ with $a\in\PSH(Y,\Lambda)$. The divisorial inequalities allow removal of each finite partial sum of $S$ from $\Lambda+\ddc a$ while retaining positivity. To see this locally, add a smooth correction to $a$ to obtain a psh function. Siu decomposition identifies the coefficient mass of its closed positive curvature current on each divisor. The smooth correction has no such mass, so removal of those same coefficients from the original positive current is still positive. Passing to the increasing finite sums gives
\[
 \Lambda+\ddc a-S\geq0.
\]
Consequently $\ddc(a-v)\geq\beta-\Lambda$. The $L^1$ difference has a quasi-plurisubharmonic representative and is bounded above on compact $Y$. This yields $a\leq v+C$ almost everywhere. Canonical local averages of quasi-plurisubharmonic functions give the same inequality everywhere. This proves ordinary domination.
\end{proof}

Here a finite-mass divisorial current may have infinitely many components. The lemma imposes a smooth residual term in the equation for $v$; it is not an assertion about every potential with the same divisorial Lelong numbers.

We also record the local ideal identity needed for the ambient pullback. In the proof, extension of an ideal means the ideal generated by its pullbacks.

\begin{lemma}\label{lem:submersion-multiplier-pullback}
If $p:X\to M$ is a holomorphic submersion and $U\in\QPSH(M)$, then for every $t>0$,
\[
 \mathcal I(tU\circ p)
       =\mathcal I(tU)\mathcal O_X.
\]
\end{lemma}
\begin{proof}
Work in product coordinates $(z,\zeta)$ with $p(z,\zeta)=z$. A germ in the ideal on the right is a finite sum of bounded holomorphic multiples of pullbacks of germs integrable against $e^{-tU(z)}$. Fubini proves its weighted integrability on a sufficiently small product neighborhood.

Conversely, let $F(z,\zeta)$ be a weighted-integrable holomorphic germ and expand it in the fiber variables,
\[
 F(z,\zeta)=\sum_\alpha f_\alpha(z)\zeta^\alpha.
\]
The coefficient estimate for a holomorphic function on a polydisc gives, on smaller product neighborhoods,
\[
 |f_\alpha(z)|^2\leq C_\alpha
       \int |F(z,\zeta)|^2\,\mathrm{d}V_\zeta.
\]
Multiply by $e^{-tU(z)}$ and integrate. Each coefficient germ belongs to $\mathcal I(tU)$. Let $J$ be the extension of this ideal to the local analytic ring $R$ of the product. Every finite Taylor sum belongs to $J$, and the remainder of total fiber degree at least $N$ belongs to $(\zeta)^N$. Thus the class of $F$ in $R/J$ lies in $(\zeta)^N(R/J)$ for every $N$. The Krull intersection theorem for the finite module $R/J$ over the Noetherian local analytic ring gives intersection zero. Hence $F\in J$. This is the usual local algebra form of convergence for coherent ideals. Smooth corrections and smooth positive volume densities do not change the integrability ideals.
\end{proof}

Let $p:X\to M$ be a surjective holomorphic submersion of connected compact complex manifolds with connected fibers. Let $C\subset M$ be a connected compact smooth curve, put $Y=p^{-1}(C)$, and write $q=p|_Y:Y\to C$. Then $Y$ is a connected smooth compact submanifold. Take $U\in\QPSH(M)$ with $\nu(U,C)=0$, and set $u=U\circ p$. The generic Lelong number of $u$ along $Y$ is zero, since in product coordinates it equals that of $U$ along $C$.

Let
\[
 D=\sum_{b\in C}\tau_{C,U}(b)\,\delta_b,
 \qquad \delta=D(C)<+\infty.
\]
Choose a smooth positive probability form $\eta$ on $C$ and its nonpositive Green kernel. The curve construction gives a genuine $w\in\QPSH(C)$ with
\[
 \ddc w=D-\delta\eta.
\]
Put $v=w\circ q$. Pullback of distributions by a smooth submersion is defined by integration along the fibers. It commutes with differentiation and with positive sums here, so
\begin{equation}\label{eq:curve-fiber-divisorial-current}
 \ddc v=\sum_{b\in C}\tau_{C,U}(b)[Y_b]-\delta q^*\eta,
 \qquad Y_b=q^{-1}(b).
\end{equation}
Each fiber is a smooth connected prime divisor. The sum is a positive closed current of finite mass, as also follows locally from the positive current $\ddc(w\circ q)+\delta q^*\eta$.

\begin{theorem}\label{thm:curve-fibration-exact-trace}
In this setting, $v$ realizes the entire divisorial trace data of $u$ along $Y$:
\[
 \nu(v\circ\pi,E)=\tau_{Y,u}(E)
\]
for every prime divisor $E$ on every smooth compact modification $\pi:Z\to Y$. More explicitly, write $h=q\circ\pi$. If $h(E)=C$, both sides are zero. If $h(E)=\{b\}$, both sides equal
\[
 \operatorname{ord}_E(t_b\circ h)\,\tau_{C,U}(b),
\]
where $t_b$ is a local coordinate vanishing at $b$.

Choose any Hermitian form $\Omega_0$ with $v\in\PSH(Y,\Omega_0)$, and set $\Omega=2\Omega_0$. Then
\begin{equation}\label{eq:curve-fibration-trace-envelope}
 \mathcal T_\Omega(u;Y)=P_\Omega[v]=Q_\Omega[v]\simeq v.
\end{equation}
The envelope has positive finite extended mass and satisfies the prescribed-type equation conclusions of \cref{cor:trace-envelope-prescribed-equation}. Its ordinary type is independent of the chosen Green normalization, smooth probability form, and sufficiently large background.
\end{theorem}
\begin{proof}
The submersion ideal identity and restriction to $Y$ give
\[
 \mathfrak a_t(u;Y)=\mathfrak a_t(U;C)\mathcal O_Y.
\]
The nonzero coherent ideal on the smooth curve is locally generated at $b$ by $t_b^{k_t(b)}$, where $k_t(b)=\operatorname{ord}_b\mathfrak a_t(U;C)$. For a vertical divisor $E$ the order of its extension is therefore $k_t(b)\operatorname{ord}_E(t_b\circ h)$. For a divisor dominating $C$, the generic order is zero, since this curve ideal has only finitely many zeros. Divide by $t$ and use the defining trace limit. This gives exactly the stated formula for $\tau_{Y,u}(E)$.

For a vertical $E$, at a general point its local equation $z_1=0$ satisfies $t_b\circ h=z_1^k g$ with $g$ holomorphic and nonvanishing. A local holomorphic $k$th root of $g$ changes this coordinate so that $t_b\circ h=z_1^k$. The one-variable Lelong number of $w(z_1^k)$ is $k\nu(w,b)=k\tau_{C,U}(b)$, by the definition through circular means. This is also its generic divisorial Lelong number in the product coordinates. For a horizontal $E$, its regular locus contains a point mapped to a point where $w$ is finite; the nonconstant map from that locus to $C$ has open image. The pullback is finite there, so its generic Lelong number on $E$ is zero. This proves exact realization on every compact model.

By \cref{lem:divisorial-potential-domination} and \eqref{eq:curve-fiber-divisorial-current}, a quasi-plurisubharmonic $a$ is more singular than $v$ if and only if $\nu(a,Y_b)\geq\tau_{C,U}(b)$ for each positive coefficient. These fiber inequalities are among the defining trace constraints, and ordinary domination implies all the constraints on further modifications, by the exact formula just proved. Thus the full trace competitor family equals the ordinary-envelope family, and also the family defined by ideal domination. The envelope $Q_\Omega[v]$ was defined using ideal equivalence rather than domination, but this gives the same supremum: replace any member $a$ of the ordinary family by $\max\{a,v-\sup_Yv\}$. The replacement dominates $a$, remains below zero and is ordinarily, hence ideally, equivalent to $v$. Conversely every ideal-equivalent competitor belongs to the ideal-domination family. These comparisons prove the first two equalities in \eqref{eq:curve-fibration-trace-envelope}. The ideal envelope preserves the multiplier ideals and hence the fiber Lelong numbers; the lemma gives $Q_\Omega[v]\preceq v$. Since it dominates $v-\sup_Yv$, ordinary equivalence follows.

The potential $v-\sup_Yv$ supplies a competitor in the half-sized background. The proof of \cref{thm:trace-profile-model-envelope} consequently gives positive finite mass and the stated equations, with the exact representative $v$ in place of an extracted majorant. None of these steps assumes BMP on $X$ or $Y$.

Two Green constructions on $C$ differ smoothly, by the scalar Poisson argument in \cref{thm:curve-trace-realization}. Their pullbacks therefore have the same ordinary type. Every background in the statement gives an envelope ordinarily equivalent to this pullback. This proves the claimed independence, at the level of ordinary type rather than equality of normalized potentials.
\end{proof}

The same construction respects sums and positive real scalars at the level of ordinary types. Indeed the curve trace measures add by \cref{thm:trace-data-additivity}; their Green representatives add with one fixed kernel, and pullback preserves the sum. Each envelope in a sufficiently large background represents that same ordinary type. This supplies exact higher-dimensional traces in this fibration setting, without constructing a general metric on Hermitian singularity types.


\section{Product realizations and their measures}
\label{sec:trace-product-measures}

Products with a curve give explicit Monge--Amp\`ere measures for the exact trace types above. They also distinguish the ordinary trace representative from other representatives of the same multiplier-ideal class.

Let $C$ be a compact connected curve with a smooth positive probability form $\eta$, and let $(Z,\omega_Z)$ be a compact connected Hermitian manifold of dimension $k\geq1$. On $Y=C\times Z$, denote the projections by $q$ and $r$, and set
\[
 \Omega=q^*(A\eta)+r^*\omega_Z,\qquad A>0.
\]
For positive Borel measures on the factors, $\mu\otimes\nu$ denotes their usual product measure. The extended measures below are sigma-finite by \cref{thm:arbitrary-extended-ma}, so this notation remains meaningful when a total mass is infinite.

\begin{proposition}\label{prop:curve-product-extended-ma}
For $w\in\PSH(C,A\eta)$ and $h\in\PSH(Z,\omega_Z)$, the potential $a=w\circ q+h\circ r$ is $\Omega$-plurisubharmonic and
\begin{equation}\label{eq:curve-product-extended-ma}
 \mathrm{MA}^{\mathrm{ext}}_\Omega(a)
 =(k+1)\,
       \mathrm{MA}^{\mathrm{ext}}_{A\eta}(w)
                \otimes\mathrm{MA}^{\mathrm{ext}}_{\omega_Z}(h).
\end{equation}
No finiteness of either total mass is assumed.
\end{proposition}
\begin{proof}
The curvature is the sum of the two positive pullback currents, proving positivity. Suppose first that both potentials are bounded. Multilinearity of the bounded products leaves only the term with one curve factor and $k$ factors from $Z$: two curve factors vanish by dimension, as do $k+1$ factors from $Z$. The binomial coefficient is $k+1$. This gives the formula for bounded potentials. To justify the exterior product identity at this regularity, use local psh corrections on each factor and decreasing convolution on smaller product charts. For smooth approximants it is the ordinary exterior product of forms. Local Bedford--Taylor convergence and the finite smooth-background expansion give weak convergence of the factor measures with uniformly bounded variation on compact subcharts. Products then converge weakly: first test against products of continuous functions and then use uniform approximation by finite sums of such products. This proves the identity in the limit. These approximations do not require the background on $Z$ to be closed.

For general potentials subtract constants so that $w,h\leq0$. Set $w_j=\max(w,-j)$ and $h_j=\max(h,-j)$. On
\[
 R_j=\{w>-j\}\times\{h>-j\}
\]
the sum agrees with the bounded potential $w_j\circ q+h_j\circ r$. This is a plurifine open Borel set, and it lies in $\{a>-2j\}$. Locality of the bounded truncation products therefore identifies the extended measure of $a$ restricted to $R_j$ with that of this bounded sum. The bounded formula identifies it with $k+1$ times the product of the two restricted truncation measures. These are exactly the restrictions of the two extended factor measures.

The sets $R_j$ increase to the product of the complements of the two pole sets. Both sides of the proposed identity give the remaining set zero mass. For the left side it is the pole set of the sum; for the right side this follows from the non-pluripolar property of each factor and sigma-finiteness of the product measures. Monotone convergence of positive measures proves the formula, even when the resulting mass is infinite.
\end{proof}

Suppose now that $D$ is the finite atomic trace measure of a curve problem as above, put $\delta=D(C)$, and let $w$ have $\ddc w=D-\delta\eta$. For $A>\delta$, the canonical product representative $v=w\circ q$ satisfies
\begin{equation}\label{eq:product-trace-smooth-measure}
 \mathrm{MA}^{\mathrm{ext}}_\Omega(v)
       =(k+1)(A-\delta)\,\eta\otimes\omega_Z^k.
\end{equation}
Thus its measure is smooth and positive, despite the possibly infinite family of singular fibers. This identity concerns the extended measure: its definition discards the divisorial part of the full curvature current.

The product formula also gives a separated-density equation in this ordinary trace type. Let $0\leq f\in L^p(C,\eta)$ and $0\leq g\in L^p(Z,\mathrm{d}V_Z)$, $p>1$, have positive integrals, where $\mathrm{d}V_Z$ is smooth and positive. The curve equation gives $w_f\simeq w$ with
\[
 \mathrm{MA}^{\mathrm{ext}}_{A\eta}(w_f)=c_C f\eta,
 \qquad c_C=\frac{A-\delta}{\int_Cf\eta}.
\]
The bounded Hermitian equation on $Z$ gives a bounded $h_g$ and $c_Z>0$ with
\[
 \mathrm{MA}_{\omega_Z}(h_g)=c_Zg\,\mathrm{d}V_Z.
\]
Here we use exactly the continuous existence theorem \cref{thm:kn-continuous}; neither BMP nor uniqueness of the normalized zero-exponent potential is needed. The sum $a=w_f\circ q+h_g\circ r$ is ordinarily equivalent to $v$, and
\[
 \mathrm{MA}^{\mathrm{ext}}_\Omega(a)
       =(k+1)c_Cc_Z\,(f\eta)\otimes(g\,\mathrm{d}V_Z).
\]
The tensor density belongs to $L^p$ by Fubini. This gives an explicit separated construction; existence for nonseparated $L^p$ data in a sufficiently large trace background follows from the preceding theorem.

\begin{proposition}\label{prop:exact-trace-infinite-representatives}
Suppose $v_+(\omega_Z)=+\infty$ and $A>\delta$. In the same product background there is $a\in\PSH(Y,\Omega)$ such that
\[
 a\sim_{\mathcal I}v,\qquad
 \int_Y\mathrm{MA}^{\mathrm{ext}}_\Omega(v)<+\infty,
 \qquad
 \int_Y\mathrm{MA}^{\mathrm{ext}}_\Omega(a)=+\infty.
\]
Both potentials have the same divisorial Lelong numbers on every modification. When $D$ comes from the ambient curve problem, these are the exact trace numbers in \cref{thm:curve-fibration-exact-trace}. The product manifold itself fails BMP.
\end{proposition}
\begin{proof}
Choose the nonpositive potential $H$ of \cref{thm:infinite-mass-witness} on $Z$. It has infinite extended mass and $e^{-tH}$ is integrable for every $t>0$. Put $a=w\circ q+H\circ r$. The product formula and $A-\delta>0$ show that its mass is infinite. Formula \eqref{eq:product-trace-smooth-measure} gives the finite positive mass of $v$.

We verify ideal equivalence locally for every $t>0$. Since $H\leq0$, integrability against $e^{-ta}$ implies integrability against $e^{-tv}$, so $\mathcal I(ta)\subseteq\mathcal I(tv)$. Conversely the submersion identity gives $\mathcal I(tv)=\mathcal I(tw)\mathcal O_Y$. Local generators pulled back from $C$ are integrable against $e^{-tw}$; their products with $e^{-tH}$ are integrable by Fubini. Bounded holomorphic multipliers and finite sums preserve local integrability. Thus $\mathcal I(tv)\subseteq\mathcal I(ta)$, proving equality at every positive weight. The local ideal criterion then gives equality of all divisorial Lelong numbers after modification.

Finally, by \cref{prop:bmp-metric}, failure of BMP on $Z$ gives smooth $\omega_Z$-plurisubharmonic $H_j$ with unbounded top masses. The smooth functions $H_j\circ r$ are $\Omega$-plurisubharmonic and have masses
\[
 (k+1)A\int_Z(\omega_Z+\ddc H_j)^k,
\]
by the smooth product formula. These are unbounded, proving failure of BMP on $Y$.
\end{proof}

For a concrete ambient realization, take a compact manifold $M$ containing the curve $C$, a potential $U$ with $\nu(U,C)=0$, and $X=M\times Z$. Then $Y=C\times Z$ and $u=U\circ\operatorname{pr}_M$ satisfy the preceding fibration theorem. The factor $Z$ can be the Hopf threefold of \cref{thm:hopf-unbounded}. Small logarithmic poles of $U$ at finitely many points of $C$ already give nonzero trace data; the curve construction also allows any countable trace data produced by the ambient ideal sequence. The finite and infinite measures above occur with exactly the same prescribed trace profile. Exact realization therefore does not, by itself, control the nonlinear mass of every representative of its ideal class.
