# Book-side assessment of the incoming P09 spectral-gap draft

Source: [the complete incoming draft](../drafts/P09-spectral-gap-collapse-20261011.unverified.tex) at private commit 72a9d9524c1e025af78f78bca7afa758cb6415db, Git blob d157013617e6e39196b70a0fd0a2bb25a2225ac3. The existing pending audit is preserved. This record is a direct manual source and proof assessment for possible book integration, not an independent model/verifier certificate, checked article, manuscript adoption or compiled release.

The full draft was read. The book definition and smooth dual-formula context were read at lines 1–105 of chapter_gauduchon_variational_volume.tex; the complete section_gauduchon_collapse.tex and lines 1–47 of section_non_kahler_geometry.tex were also read. Their Git blobs are respectively 7533a8b8890358b4012f8da7da9ac8425aead6e5, 972b1a8d41eb2354561d988d550c78004e193d93, and 7442e4a4584476e8e0dd862fc07760c641dd1160. These three book sources are unchanged from checkpoint 684. The latest P09 additions to BLUEPRINT and STATUS were read from the actual commit patches; no complete reread of their historical records is claimed.

## The two optimization problems

Write
\[
 A_\theta(\gamma)=\int_X\theta\wedge\gamma^{n-1},\qquad
 D_\mu(\gamma)=\int_X(\mu/\gamma^n)^{1/n}\gamma^n.
\]
The threshold minimizes \(A_\alpha/A_h\), whereas the root volume minimizes \(A_\alpha/D_\mu\). Both quotients are invariant under constant metric rescaling. When \(n\geq2\), a ray can be normalized by \(A_h=1\); the scaling factor for each pairing is the \((n-1)\)st power of the metric scaling factor.

The draft estimates every smooth positive Hermitian test before imposing the Gauduchon condition. It therefore does not replace the full test family by translation-invariant or diagonal metrics.

## Manual reconstruction of the spectral estimate

Let \(H=\int_Xh^n\), \(\nu=h^n/H\), \(r=\mu/\nu\) and \(R=\max r\). For the matrix \(G\) of \(\gamma\) relative to \(h\), its cofactor \(C=(\det G)G^{-1}\) satisfies
\[
 A_h=\frac Hn\int\operatorname{tr}C\,d\nu,\quad
 A_B=\frac Hn\int\operatorname{tr}(BC)\,d\nu,\quad
 D_\mu=H^{(n-1)/n}\int r^{1/n}(\det C)^{1/n}\,d\nu.
\]
These identities retain the wedge factor \(1/n\). No derivative or closedness assumption on the test is used.

Suppose \(B\geq0\) has constant rank \(q\), \(1\leq q<n\), with positive eigenvalues at least \(\delta>0\), and set \(m=n-q\). Let \(P\) be its positive spectral projection. Put \(p=\operatorname{tr}(PC)\) and \(s=\operatorname{tr}((I-P)C)\). The Schur-complement determinant inequality, followed by arithmetic–geometric mean in each block, gives
\[
 \det C\leq(s/m)^m(p/q)^q.
\]
This remains valid for nondiagonal \(C\); commutativity of \(B\) and \(C\) is unnecessary. Under \(A_h=1\), put \(y=(H/n)\int p\,d\nu\). Then \(0<y<1\), \(\int s\,d\nu=(n/H)(1-y)\), and \(y\leq e/\delta\), where \(e=A_B\).

The integral weighted arithmetic–geometric mean inequality now yields
\[
 D_\mu\leq n(R/H)^{1/n}
       \left(\frac{1-y}{m}\right)^{m/n}
       \left(\frac yq\right)^{q/n}.
\]
The logarithmic derivative of the variable part is
\[
 \frac{q-ny}{ny(1-y)}.
\]
Thus replacing \(y\) by \(e/\delta\) is justified only for \(0<e/\delta\leq q/n\). This proves the stated small-excess estimate and \(D_\mu=O(e^{q/n})\).

For \(\alpha=ah+B\), \(a>0\), the assumption \(\kappa_h(\alpha)=a\) must remain explicit: \(\alpha\geq ah\) alone proves only \(\kappa_h(\alpha)\geq a\). Under the equality assumption, every normalized threshold-minimizing sequence has \(e_j=A_\alpha-a\to0\), so the estimate applies to every such sequence.

## Sharp flat example and the distinct minimizing excess

On \(E^n\), take unit-area factor forms \(\omega_i\),
\[
 h=\sum_i\omega_i,\quad
 B=\delta\sum_{i=m+1}^n\omega_i,\quad
 \alpha=ah+B,\quad
 \mu=\omega_1\wedge\cdots\wedge\omega_n.
\]
Here \(H=n!\), \(R=1\), and \(B=\delta P\). Consequently \(y=e/\delta\) exactly. The determinant bound holds for every excess \(0<e<\delta\), without the earlier monotonicity substitution:
\[
 D_{\max}(e)=\frac{n}{(n!)^{1/n}}
       \left(\frac{1-e/\delta}{m}\right)^{m/n}
       \left(\frac{e/\delta}{q}\right)^{q/n}.
\]

Attainment is by actual closed metrics. For \(x=e/\delta\), choose cofactor entries
\[
 c_i=\frac{1-x}{m(n-1)!}\ (i\leq m),\qquad
 c_i=\frac{x}{q(n-1)!}\ (i>m).
\]
The inverse cofactor construction \(G=(\det C)^{1/(n-1)}C^{-1}\) gives a positive constant matrix with the declared cofactor. Directly \(A_h=1\), \(A_B=e\), and its denominator equals the displayed maximum. Taking \(x\downarrow0\) proves \(\kappa_h(\alpha)=a\). The upper bound applies to every smooth test, so every normalized threshold-minimizing Gauduchon sequence has \(D_\mu\to0\), not merely the constructed invariant sequence.

The background is closed and strictly positive. Its top intersection is
\[
 M=n!a^m(a+\delta)^q.
\]
Pointwise matrix arithmetic–geometric mean gives \(A_\alpha\geq M^{1/n}D_\mu\) for all tests. The closed metric \(\gamma=\alpha\) attains equality, so \(\lambda_\mu(\alpha)=M^{1/n}>0\).

The fixed-excess frontier also gives the quotient minimum directly. The logarithmic derivative of
\[
 F(x)=\frac{a+\delta x}{(1-x)^{m/n}x^{q/n}}
\]
vanishes exactly when
\[
 (na+m\delta)x=qa.
\]
Since \(F\) diverges at both ends, its minimum occurs at
\[
 x_\lambda=\frac{qa}{na+m\delta},\qquad
 e_\lambda=\frac{\delta qa}{na+m\delta}>0.
\]
These weights also follow from the normalized cofactor of \(\alpha\). They differ from threshold-minimizing weights, for which \(x\to0\). In fact \(A_\alpha/D_\mu\to+\infty\) along every normalized threshold-minimizing sequence, because its numerator tends to \(a>0\) and its denominator tends to zero.

## Consequence for the book and adoption boundary

The example disproves a universal assertion of a positive lower determinant denominator along threshold-minimizing sequences under closed nef positive top intersection. That condition is a useful sufficient route to bigness, but is not a necessary consequence even of strict positivity on a flat Kähler manifold.

It does not contradict the existing conditional collapse proposition: its first assertion assumes nonbigness, which the flat example does not satisfy, and its second assertion assumes the denominator lower bound, which fails. Denominator-only collapse must remain distinct from the joint degeneration \(A_\alpha\to0\) and \(D_\mu\to0\) used for a positive-volume nonbig background. The example settles neither general closed-nef bridge nor the original P09 task.

A natural future location is beside sec:gauduchon-collapse, after the existing conditional proposition, with the complete proof and sharp example. Its explanatory paragraph and the sufficient-route discussion beside qu:closed-nef-gaud-bridge should then distinguish the two quotient minima and make the extra denominator hypothesis explicit. Preserve the original problem identifier and record the unresolved closed-nef implications. Do not claim a new closure or silently strengthen a lower-bound route into a general theorem.

No error was found in the elementary arguments under their stated hypotheses in this manual pass. Literature priority, the full original P09 task, and independent verification were not assessed. Final book adaptation, a second complete review, source compilation, output inspection, catalogue reconciliation and publication remain pending while local execution is unavailable. Xean is withdrawn for the current book task; this assessment uses no Xean call and changes no historical verdict.
