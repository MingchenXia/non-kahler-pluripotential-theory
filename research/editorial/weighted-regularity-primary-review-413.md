# Weighted regularity and projective envelopes — review 413

The complete 22-page version-one PDF of Nurbek Kh. Narzillaev, *Weighted regularity and plurithinness in C^n*, arXiv:2609.23530v1, has now been actually read. Fifteen original page images are inspected: 6, 8–14, 16–22. The source PDF has SHA256 `88fd47ac7cd605b2d796facfc1b316222965ca924e01ba8b8a54db00cfd7fba5`. Latest/version-one abstract metadata was independently read at 411; the exact source fixes the growth class by delta log^+ norm, and its dd operator is pi times the book operator. Reading the original proofs does not constitute a recursive review of every cited historical foundation. No paper theorem is yet adopted into the book.

The proof assessment distinguishes raw contact from equality of the regularized envelope. Lemma 3.1 proves concavity in the growth parameter and both slope bounds; Theorem 1.1 then restricts a point's regular parameter set to empty, the positive contact endpoint, or the whole contact ray. Proposition 3.2 bounds and characterizes the finite initial slope, while Theorems 3.3–3.4 represent it by active probability/constant pairs. Their quasi-everywhere condition is essential: removing it admits the point mass and destroys the regularization defect. The Hahn–Banach argument, compactness of bounded pairs, and both derivative inequalities are checked directly; the logarithmic-growth pluripolar-barrier premise is still separately pending at primary scope.

Theorem 4.2 uses strict positivity only near the point, together with a global extension in the required growth class. Its pasted competitor is unchanged outside a ball and equals the weight on the compact set. Theorem 1.4 and Proposition 5.2 distinguish local regularity, thinness and negligible sets. The countable rational-ball representation proves negligibility of the maximal relative plurifine open exceptional set; the argument does not assume that an arbitrary union of pluripolar sets is pluripolar.

The product example in Section 6 uses explicit tiny disks at 2, a logarithmic barrier with the bound (4/9)log 2, and a smooth radial weight whose Hessian has rank n−1 outside the unit ball. The non-thin exceptional polydisc is pluripolar and not locally regular. The line-restriction upper bound, the two separate cases in the Green-function convergence at the irregular point, the strict comparison, and the conjugated linear functional in Theorem 6.5 are checked. In particular the derivative depends on a truncated planar compact and equals log 2 on the polydisc boundary. The proof cannot replace pointwise convergence at 2 by convergence away from the compact.

The chair example in Section 7 is globally pluriregular in the explicit sense V_K^*|K=0, yet it is not locally pluriregular at the selected point. The fiber-separation polynomial, separation of the two coordinate projections, local size/non-thinness arguments, and removal of the single bounded boundary exception are checked. Proposition 7.3 proves its exact positive initial slope on an explicit interval h≤tau log(26/25)/(2log 5), using a quasi-everywhere competitor and a sliced upper estimate. The higher-dimensional proof asserts the indicated lower slope bound; it does not claim the two-dimensional exact formula in every dimension. These examples do not contradict regularity for locally pluriregular compacts.

Attempts to obtain the exact cited 2017 Levenberg notes and the Alan 2019 PDF returned 404. An arXiv title search for the latter returned no result; this is not a literature-absence conclusion. A separately identified Levenberg arXiv:1010.4035v1 PDF was actually obtained: 82 pages, SHA256 `5894e1391cac33a029960f9e3c38513c1022e437f540159d707b6f13e6160060`, cover date October 23, 2018. Its cover and complete pages 3–5 were read. This is a different source from the cited 168-page 2017 course notes. Those pages state weighted extremal facts and local-regularity dependence but do not supply the requested complete product/barrier proofs. No exact-2017-source or full-82-page-proof review is claimed. Primary verification of product formulas, logarithmic pluripolar barriers, the thinness barrier and the cited historical open problem remains pending before adoption of the dependent claims.

## A direct bridge from the existing book foundations

The following argument is independently reconstructed from the book's finite-maximum/upper-envelope facts, normalized compactness and removable-singularity lemma. It needs none of the still pending external thinness, product or historical premises. The formulas use the book's operator throughout; no novelty is claimed.

Let chi(z)=log(1+norm(z)^2) on C^n, and let omega_FS have this local potential on P^n, with integral omega_FS^n=1. For delta>0 put theta_delta=(delta/2)omega_FS. Write L_delta for genuine plurisubharmonic u satisfying u≤delta log^+norm+C_u. Then

\[
 u\longleftrightarrow p=u-\frac\delta2\chi
 \quad\text{identifies }L_\delta\text{ with }\operatorname{PSH}(\mathbb P^n,\theta_\delta).
\]

For the forward direction, on the chart Z_i≠0 meeting the hyperplane H={Z_0=0}, the relevant local plurisubharmonic representative is

\[
 p+\frac\delta2\log\frac{\sum|Z_j|^2}{|Z_i|^2}
 =u+\delta\log|Z_0/Z_i|.
\]

It is locally bounded above near H: the norm of the affine coordinates is at most a chart-dependent constant divided by |Z_0/Z_i|. The book's removable-singularity lemma gives its canonical extension, and the smooth potential transitions make the extensions agree. Conversely a compact theta_delta-plurisubharmonic p is bounded above, so u=p+delta chi/2 is plurisubharmonic in the affine chart and has the required upper growth. Agreement on the dense chart and canonical extension give uniqueness in both directions. This establishes the factor one half rather than delta omega_FS.

For a non-pluripolar compact K in the affine chart and a bounded real weight psi on K, define raw affine and compact-set envelopes with the everywhere obstacle condition. The class correspondence gives, before any regularization,

\[
 V_{\delta,K,\psi}=\frac\delta2\chi+
 \sup\{p\in\operatorname{PSH}(\mathbb P^n,\theta_\delta):
       p|_K\leq\psi-\delta\chi/2\}.
\]

A constant smaller than the obstacle supplies a competitor. There is a uniform upper bound on this whole compact family. Otherwise choose p_j with sup p_j=M_j and M_j−sup_K(psi−delta chi/2)≥j2^j. Their normalized v_j=p_j−M_j satisfy v_j≤0 and have uniformly bounded L1 norms by the existing normalized compactness theorem. The partial sums sum_{j≤N}2^(−j)v_j are decreasing theta_delta-plurisubharmonic functions with uniformly bounded L1 norms. The existing decreasing-limit corollary gives a genuine global limit v, while the displayed inequality forces v=−infinity on K. On the affine chart v+delta chi/2 is a genuine global plurisubharmonic function with value minus infinity on K, so K would be pluripolar, a contradiction. Thus the regularized compact envelope is bounded above and below and is theta_delta-plurisubharmonic. The affine regularization consequently belongs to L_delta^+.

For completeness, the raw envelope equals its canonical regularization almost everywhere without importing a quasi-everywhere theorem. The uniformly bounded competitor family is closed under finite maxima. Choose a sequence whose integrals approach the supremum of all competitor integrals, and replace it by its running maxima with the constant lower competitor. Its increasing limit has a canonical plurisubharmonic regularization P. Dominated convergence gives integral P equal to that supremum. For any competitor q, the integrals of max(q,p_j) have the same bound, so integral(max(q,P)−P)=0. Canonical order then gives q≤P everywhere. Thus the raw supremum is bounded above by P, equals P almost everywhere, and its regularization is P. Adding back the smooth chart potential gives the same fact on the affine chart.

This proves the regularized version of the exact displayed correspondence. The background and the obstacle both change with delta. The construction is not a fixed-obstacle projection path, and it does not assert invariance of an ordinary singularity model under that change.

One can now reconstruct the contact-ray assertion without a logarithmic pluripolar barrier. Let m=inf_K psi. For 0<alpha<beta, scaling a beta-competitor and shifting by m yields the raw inequalities

\[
 0\leq V_\beta-V_\alpha
 \leq\frac{\beta-\alpha}{\alpha}(V_\alpha-m).
\]

The raw values are finite, so they depend continuously on each positive growth parameter. The set Lambda where V_delta=psi everywhere on K is upward closed and relatively closed in (0,infinity). It is empty, all of (0,infinity), or a closed ray [lambda,infinity) with lambda>0. Convex combinations of affine competitors and the just-proved almost-everywhere envelope identity give concavity of F_delta=V_delta^*: the raw inequality first holds almost everywhere, then extends to all points by canonical plurisubharmonic order. Monotonicity is immediate from inclusion of growth classes.

At a∈K and delta∈Lambda, d_delta=F_delta(a)−psi(a) is nonnegative, nondecreasing and concave. If d_alpha=0 at a parameter larger than the contact endpoint, choose eta<alpha in Lambda and beta>alpha. Concavity at alpha forces both nonnegative endpoint defects to vanish. Monotonicity handles all smaller parameters. Hence the regular set at a is empty, the single positive contact endpoint, or the whole contact ray; intersecting these possibilities over K gives the same global alternatives. This direct argument verifies the corresponding parameter assertion independently of the preprint's unreviewed external barrier/product foundations.

Sixteen explicit obligations pass for this bridge: normalized Fubini–Study potential; local affine positivity; upper bound near H; removable canonical extension; inverse growth; uniqueness; exact obstacle transport; nonempty family; non-pluripolar uniform upper bound; canonical upper envelope; almost-everywhere integral-max construction; L_delta^+ bounds; raw parameter continuity; contact-ray closure; canonical concavity; pointwise/global regular-set alternatives. The indispensable book statements and complete proofs are actually read at this checkpoint. Integration of this bounded, verified unit is next; the source-dependent examples retain their pending primary checks.

## Concurrent author intake and scope

Author commit `60161d2cafc922126380f698f6a261dc93866f0f` supplies the anonymous S08 source `research/papers/S08-convex-body-reference-stability.tex` (567 lines; SHA256 `a1773432626757ea400511856b5a78408b6410210bd7320b0410cd4d9d92ad4c`). It is preserved through ordinary merge `cc58cc0ffb3758404f1a37847ae91fc3eb4a0fbb`, with both concurrent changelog entries retained. The six incoming research files are exact author blobs. The attached generated reports are retained as provenance and are not premises; no abandoned runtime is used. Full independent S08 source/proof review remains queued after the verified compact-envelope bridge integration.

This is a research-only checkpoint. All 318 tracked book files and 973 proof bodies, both original manifests and both catalogue sources are exact relative to the merged baseline. The 451 protected files remain exact. Manuscript 412, its 1170-page live release and the saved catalogue editor remain unchanged; no new author build, native compile call or publication is made. Forty original directions remain open. The source package has 2097 archive entries and 2096 checksum-validated current payload entries; all 315 packaged book sources match the actual 412 reconstruction. No new fresh rebuild is claimed. Normal private synchronization follows.
