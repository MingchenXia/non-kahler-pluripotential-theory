# Fixed-divisor residual adjoints — direct review411

This is a research-only extension of the explicit Chapter14 model, not a new manuscript release. The mathematical argument below is derived directly from the accepted bounded products, current identities and residual correspondence. No new external theorem, generated verdict or anonymous source citation is a premise. It gives a sufficient recovery regime for this fixed divisor; arbitrary singular references and general S07/P16 remain open.

Keep the product, divisor, potentials and forms of Section14.2.4. Let $w_j,w\in\operatorname{PSH}(X,\beta)$ satisfy $|w_j|,|w|\leq M$ for one fixed $M\geq1$, and suppose $w_j\to w$ in capacity. Put
\[
 T_j=\beta+\mathrm d\mathrm d^c w_j,\qquad T=\beta+\mathrm d\mathrm d^c w,
 \qquad Q_j=T_j/4,\quad Q=T/4,\quad \nu_j=T_j^2/4,\quad\nu=T^2/4.
\]
Then $Q_j\rightharpoonup Q$ as currents and $\nu_j\rightharpoonup\nu$ as probabilities. These are the nonpolar residual cofactors and measures of the canonical potentials $\psi+w_j$ and $\psi+w$, all of the same ordinary type. If each $T_j$ is smooth and strictly positive, $Q_j$ and $\nu_j$ are its classical residual adjoints. The potentials $\psi+w_j$ still have the fixed divisor pole; no globally smooth theta-potential is asserted.

There is a quantitative estimate. For real $f\in C^\infty(X)$ choose $C_f\geq0$ with $-C_f\beta\leq\mathrm d\mathrm d^c f\leq C_f\beta$, and write $E_{j,\eta}=\{|w_j-w|>\eta\}$ for $\eta>0$. With the already defined global capacity of Chapter1,
\[
 \left|\int_X f(\mathrm d\nu_j-\mathrm d\nu)\right|
 \leq C_f\bigl(2\eta+2M^2\operatorname{Cap}_\beta(E_{j,\eta})\bigr).
\]
Here $\operatorname{Cap}_\beta\leq4\operatorname{Cap}_\omega$ since $\beta\leq2\omega$, so either fixed metric's capacity gives the same convergence.

To prove the estimate, set $a_j=(w_j+M)/(2M)$ and $S_j=\beta+\mathrm d\mathrm d^c a_j$. They are global capacity tests with $0\leq a_j\leq1$, and
\[
 S_j=\left(1-\frac1{2M}\right)\beta+\frac1{2M}T_j.
\]
Positive bounded mixed products give
\[
 S_j^2\geq\left(\frac1M-\frac1{2M^2}\right)\beta\wedge T_j
 \geq\frac1{2M}\beta\wedge T_j.
\]
Consequently $\int_E\beta\wedge T_j\leq2M\operatorname{Cap}_\beta(E)$ for every Borel $E$; the same estimate holds for $T$. Closedness and Stokes give $\int_X\beta\wedge(T_j+T)=8$. The bounded-product identity
\[
 T_j^2-T^2=\mathrm d\mathrm d^c\bigl((w_j-w)(T_j+T)\bigr)
\]
can be tested against the smooth function $f$. Splitting the resulting integral into $E_{j,\eta}$ and its complement gives
\[
 \left|\int_X f(T_j^2-T^2)\right|
 \leq C_f\left(8\eta+2M\int_{E_{j,\eta}}\beta\wedge(T_j+T)\right)
 \leq C_f\left(8\eta+8M^2\operatorname{Cap}_\beta(E_{j,\eta})\right).
\]
Division by four proves the stated bound. First send $j\to\infty$ with $\eta$ fixed, then $\eta\downarrow0$. Smooth tests determine the weak probability limit because all masses equal one and smooth functions are uniformly dense in $C(X)$. No general capacity-continuity theorem is required as a new premise.

For the current limit, the constant capacity test gives $4\mathrm dV(E)\leq\operatorname{Cap}_\beta(E)$. Hence
\[
 \|w_j-w\|_{L^1(\mathrm dV)}
 \leq\eta+\tfrac M2\operatorname{Cap}_\beta(E_{j,\eta}).
\]
Taking the limits in the same order proves $L^1$ convergence. Continuity of distributional differentiation proves $Q_j\rightharpoonup Q$. The limiting cofactor is well defined even if $T$ is degenerate: $\mathrm d\mathrm d^c Q=0$, $\int_X\beta\wedge Q=1$, and its associated bounded-product probability is $T\wedge Q=\nu$. The signed measure $h\mapsto2\mathrm d\mathrm d^c h\wedge T$, for smooth real $h$, is a defined formal residual linearization and has integral zero against the constant factor $1/4$. Actual potential derivatives are asserted only along variations preserving positivity.

For a smooth strictly positive residual $T_j$, closedness makes the classical factor constant by the maximum principle and mass four normalizes it to $1/4$. If the limiting $\psi+w$ solves the relative equation at continuous logarithmic density $F$, Proposition14.2.3 identifies $\nu$ with the sole support $\mathrm e^F\mathrm dV/\int_X\mathrm e^F\mathrm dV$. Thus every approximation satisfying the stated bounded-residual/capacity hypotheses recovers that same support. This does not claim existence of such smooth residual approximations for every bounded potential, convergence in total variation or uniform integrability of their smooth densities. It also does not extend to arbitrary nonclosed residual backgrounds or control a variable conformal multiplier.

The complete used internal portions are actually read: Chapter4's bounded-adjoint persistence proposition and proof, the Chapter1 capacity definition and metric-comparison argument, and Chapter1's bounded-product proposition/proof at the preceding recorded scope. The quantitative estimate is proved above rather than inferred from a missing general theorem statement. The next book unit should reuse the existing global capacity definition in Section14.2.4 instead of redeclaring it, then insert this precise positive residual statement beside the obstruction.

Eight complete current arXiv lists are freshly retrieved and parsed: math.CV, math.DG, math.AG and math.AP, both recent and new, with counts matching every advertised total. All eight full listing byte strings match399 exactly, covering the Sep28--Oct2 new/cross entries and Oct2 replacements. There are706 distinct IDs and no unseen ID. Historical replacement/new-cross gaps remain explicitly recorded; an unchanged screen is not an exhaustive absence claim. The latest and v1 abstract pages of arXiv2609.23530 are actually read, confirming Nurbek Kh. Narzillaev, v1, submitted20September2026. The22-page v1 PDF is retrieved with SHA25688fd47ac7cd605b2d796facfc1b316222965ca924e01ba8b8a54db00cfd7fba5, and only its first page is actually read so far. Complete weighted-regularity/plurithinness proof review remains pending. No statement from that paper is adopted here.

Manuscript410 and its1170-page live release, all318 tracked book sources and972 old proof bodies, both catalogue sources, both original manifests and451 protected sources remain unchanged. No author build, native compiler call, new publication or fresh empty-source rebuild is claimed. The research package is refreshed and checked against current payloads and the actual410 reconstruction before regular private synchronization. Forty original directions remain open. Integrate the verified fixed-residual argument next, then read the complete22-page weighted-regularity primary and its actual dependencies.
