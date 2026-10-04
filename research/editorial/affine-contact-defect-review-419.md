# Affine contact defects on a non-thin compact — review 419

This review reconstructs a restricted part of the product example in Nurbek Kh. Narzillaev, *Weighted regularity and plurithinness in C^n*, arXiv:2609.23530v1, Lemmas 6.1–6.2, pp.12–14. The latest primary abstract still lists only v1, submitted 20 September 2026. The cached exact 22-page PDF has SHA256 `88fd47ac7cd605b2d796facfc1b316222965ca924e01ba8b8a54db00cfd7fba5`. Complete pages 12–13 and the relevant first 40 text lines of page 14 are freshly read; all three original page images are actually inspected. The complete 22-page reading at 413 is inherited at its recorded scope, not repeated here.

The proof below uses the book's compactness, canonical order and affine/projective correspondence. It checks a quantitative contact defect at a point with a transverse complex disk. It does not adopt the general product formula, all-boundary-point regularity classification, smooth-weight counterexample, parameter derivative, plurifine decomposition or chair example. Exact cited 2017 Levenberg notes and Alan 2019 historical premises remain pending: fresh attempted academic and publisher URLs return 404. The different 82-page Levenberg source is not a replacement for those notes. Only its pages 15 and 17 are freshly read here; they concern Gram matrices and do not supply the missing product proof.

## Direct construction

Let $D$ be the open unit disk, $p_j=2+2^{-j}$ and $r_j=\exp(-16\, 2^j)$. Put

\[
 E=\overline D\cup\{2\}\cup\bigcup_{j\geq1}\overline D(p_j,r_j),
 \qquad K=E\times\overline D^{\,n-1}\quad(n\geq2).
\]

The estimate $r_j<2^{-j-3}$ gives disjoint small disks, all outside the unit disk, with their only accumulating center 2. Thus $E$ and $K$ are compact. Every neighborhood of every point of $K$ contains an open product of disk pieces, using sufficiently small disks when the first coordinate is 2. In particular all local pieces are non-pluripolar.

Define the logarithmic series

\[
 h(\zeta)=\sum_{j\geq1}2^{-j}\log|\zeta-p_j|+2\log2.
\]

The canonical convergence can be verified on the projective line. Write $\chi=\log(1+|\zeta|^2)$ and $\theta=\omega_{\rm FS}/2$. The affine/projective growth lemma extends

\[
 q_j=\log|\zeta-p_j|-\chi/2
\]

to a genuine $\theta$-plurisubharmonic function. Cauchy–Schwarz gives $q_j\leq\log4$, and its value at infinity is0, so $0\leq\sup q_j\leq\log4$. Normalized compactness gives a uniform bound for $\|q_j-\log4\|_{L^1}$. The partial sums

\[
 w_N=\sum_{j=1}^N2^{-j}(q_j-\log4)
\]

are nonpositive, decrease, remain $\theta$-plurisubharmonic and have uniformly bounded $L^1$ norms. The decreasing-limit corollary supplies their genuine canonical limit $w$. Since the partial weights tend to1, its affine representative gives exactly

\[
 h=w+\chi/2+\log4+2\log2.
\]

Thus $h$ is subharmonic and has logarithmic growth at most 1. The geometric sum $\sum j2^{-j}=2$ gives $h(2)=0$. For $\zeta\in\overline D(p_j,r_j)$ all other distances to the centers are less than1, hence

\[
 h(\zeta)\leq2^{-j}\log r_j+2\log2=-16+2\log2.
\]

This also gives a genuine planar thinness barrier at 2. On $\overline D$ one has $h\leq4\log2$. Consequently

\[
 v(\zeta)=\frac{8\log^+|\zeta|+h(\zeta)-4\log2}{9}
\]

is subharmonic with logarithmic growth at most 1, satisfies $v\leq0$ on $E\setminus\{2\}$, and has $v(2)=4\log2/9$. Indeed on every small disk the numerator is at most $14\log2-16<0$.

## Everywhere-obstacle competitors

No quasi-everywhere obstacle substitution is needed. Let

\[
 b(\zeta)=\log|\zeta-2|-\log3,\qquad
 u_\varepsilon(z)=\frac{v(z_1)+\varepsilon b(z_1)}{1+\varepsilon}
 \quad(\varepsilon>0).
\]

The bound $|\zeta-2|\leq3$ on $E$ gives $b\leq0$ there, with value $-\infty$ at 2. Each $u_\varepsilon$ is a genuine plurisubharmonic function of logarithmic growth at most 1 on $\mathbb C^n$ and satisfies the zero obstacle at **every** point of $K$. Thus $u_\varepsilon\leq V_{1,K, 0}\leq F_{1,K, 0}$. Off the hyperplane $z_1=2$, passage to $\varepsilon\downarrow0$ gives $F_{1,K, 0}\geq v(z_1)$. Canonical almost-everywhere order extends this inequality across the hyperplane. For every $a=(2,w)$ with $w\in\overline D^{\,n-1}$,

\[
 V_{1,K, 0}(a)=0,\qquad
 F_{1,K, 0}(a)\geq\frac49\log2>0.
\]

Scaling is an exact bijection of the zero-obstacle competitor classes, so for every $\delta>0$,

\[
 V_{\delta,K, 0}=\delta V_{1,K, 0},\qquad
 F_{\delta,K, 0}=\delta F_{1,K, 0},\qquad
 F_{\delta,K, 0}(a)\geq\frac{4\delta}{9}\log2.
\]

Raw contact holds for all positive growth parameters, whereas regularized contact at these points never holds. For each positive radius, the compact piece $K\cap\overline B(a,r)$ is non-pluripolar, and monotonicity makes its regularization defect at least the displayed defect. This establishes failure of local envelope regularity there without computing an exact product extremal function.

At $a_0=(2, 0,\ldots, 0)$, every local plurisubharmonic function $f$ satisfies

\[
 f(a_0)\leq\limsup_{K\setminus\{a_0\}\ni z\to a_0}f(z).
\]

If $f(a_0)=-\infty$ this is automatic. Otherwise restrict to the complex line that varies the second coordinate, keeping the others fixed. A small disk in this line lies in $K$ and its center is $a_0$. The restriction is a genuine subharmonic function. A strict jump at the center contradicts its circular submean inequality. This proves non-plurithinness at the stated interior-fiber point. It does not assert the all-boundary-point statement, whose additional planar disk argument is outside this restricted reconstruction.

## Scope and continuation

Twenty-eight direct mathematical obligations are checked in the audit: disk geometry; local non-pluripolarity; projective logarithmic potentials; normalized bounds; decreasing curvature and $L^1$ bounds; canonical series; every sign and numerical constant; everywhere-obstacle repair; growth and order across the polar hyperplane; all positive parameters; local-piece monotonicity; and the transverse submean argument. The complete 96-line affine/projective input is read, with its short truncated passage recovered separately. The compactness input through its theorem and final corollary is read completely; the relevant first 49 lines of the maxima input and the first 56 lines of the Chapter 12 root are read. These are dependency/seam reads, not a new recursive whole-Chapter 1/12 review.

The two mathematical units are ready for scoped book integration after the affine/projective envelope argument. Exact published-paper attribution belongs in Chapter 33; no earlier Alan priority claim is made without the original historical source. No general open problem is closed. The book's 1191-page manuscript 418, publication, both catalogues, original manifests, 989 proof bodies and 451 protected sources remain unchanged in this research-only checkpoint. No author rebuild, native call or new public publication is made.

The current source package has2124 archive entries and2123 checksum-validated current payloads. Its322 book sources match the actual418 empty-source reconstruction byte for byte. No new fresh reconstruction is claimed for this research-only snapshot. Regular normal private synchronization follows.
