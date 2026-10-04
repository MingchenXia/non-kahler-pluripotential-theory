# Affine envelope response to weights and growth — review 425

The attained supporting-probability representation in Theorem 12.1.4 supplies a joint response formula for continuous weights and positive growth allowances. This is a direct consequence of the checked book argument, not a claim of novelty or a newly imported theorem. The fixed evaluation point may be anywhere in affine space. Original problem descriptions and statuses remain unchanged.

## Setting and active pairs

Fix a non-pluripolar compact K in C^n and a point a in C^n. Let g(a)=V_K^*(a), and use the genuine envelopes F_{delta,q} and the quasi-everywhere test space J_a(K) of Section 12.1.1. Here delta>0 and q belongs to the real Banach space C(K), with its uniform norm. Define

\[
 A_a(\delta,q)=\{(\mu,c)\in J_a(K):
       \int_K q\,\mathrm{d}\mu+\delta c=F_{\delta,q}(a)\}.
\]

The representation makes this set nonempty. It is convex and compact for weak convergence of probabilities and ordinary convergence of c. Indeed, J_a(K) is the intersection of closed affine half-spaces defined by continuous tests and the probability/nonnegative-constant conditions. Each active pair satisfies

\[
 0\le c\le\frac{F_{\delta,q}(a)-\inf_Kq}{\delta}
       \le g(a)+\frac{\operatorname{osc}_Kq}{\delta}.
\]

Thus compactness comes from a bounded constant slice of J_a(K), and the active equality is closed. No absolute continuity or polar noncharging is inferred for mu.

## Stability at positive growth

For delta,eta at least epsilon>0 and q,p in C(K), the earlier increment estimate and obstacle Lipschitz bound give

\[
 |F_{\eta,p}(a)-F_{\delta,q}(a)|
 \le\|p-q\|_\infty
      +|\eta-\delta|\left(g(a)+
                  \frac{\operatorname{osc}_Kq}{\epsilon}\right).
\]

First change only the growth parameter with q fixed. For alpha<beta the increment is nonnegative and bounded by (beta-alpha)(F_{alpha,q}(a)-inf q)/alpha, hence by (beta-alpha)(g(a)+osc q/epsilon). Then change the obstacle at fixed eta, using monotonicity and constant translation. This proves the displayed estimate without a mass assumption or a bound on g throughout affine space.

Suppose delta_j tends to delta>0, q_j tends to q uniformly and (mu_j,c_j) is active at (delta_j,q_j). The constants are uniformly bounded by the preceding active-pair estimate. Every sequence has a weakly convergent subsequence of probabilities and a convergent subsequence of constants. Closedness gives a pair in J_a(K). The stability estimate gives envelope-value convergence; uniform weight convergence and weak probability convergence give convergence of the integrals. The limit is therefore active at (delta,q). This argument keeps the positive lower growth bound; it supplies no statement at delta=0.

## Joint directional response

For r in C(K) and s in R, the finite one-sided directional derivative is

\[
 \lim_{h\downarrow0}
 \frac{F_{\delta+hs,q+hr}(a)-F_{\delta,q}(a)}h
 =\min_{(\mu,c)\in A_a(\delta,q)}
                  \left(\int_Kr\,\mathrm{d}\mu+sc\right).
\]

The minimum is attained because the active set is compact and the displayed functional is continuous. A base active pair bounds every positive-h quotient above by its directional value, so the limsup is at most the minimum. Choose a minimizing pair at the perturbed parameters. The representation at the base parameters bounds the quotient below by its directional value. Along a sequence approaching the liminf, active-pair stability supplies a convergent subsequence whose limit is base active. Its directional value is at least the minimum. The local Lipschitz estimate ensures finite quotients, so the two bounds prove existence and equality.

The same formula holds when r_j tends uniformly to r, s_j tends to s and h_j decreases to zero. For the upper bound use a fixed minimizing base pair; its directional values converge. For the lower bound choose perturbed active pairs, which retain a common bound on c, and use the stability argument. Uniform convergence of r_j controls the moving integrals. Thus the derivative is stable under convergent directions. This is a one-sided Hadamard directional statement, not Fréchet differentiability.

## Left slopes and differentiability

With q fixed, let D^-_delta(a) and D^+_delta(a) denote the finite left and right growth derivatives. Applying the joint response to s=-1 and s=1 gives

\[
 D^-_\delta(a)=\max_{A_a(\delta,q)}c,\qquad
 D^+_\delta(a)=\min_{A_a(\delta,q)}c.
\]

The minus sign in the first directional quotient is retained: the direction -1 gives the negative of the left derivative. Consequently growth differentiability holds exactly when all active pairs have the same c. For fixed a and q the exceptional positive parameters are at most countable. Concavity gives D^+_alpha(a)>=D^-_beta(a) when alpha<beta, so the nonempty open intervals (D^+_delta(a),D^-_delta(a)) at exceptional parameters are pairwise disjoint. Choose one rational in each interval. This countability is pointwise in a; no single countable set for every affine point is asserted.

At fixed delta, the map q -> F_{delta,q}(a) is Gâteaux differentiable exactly when the active probability is unique. If it is unique, the directional formula and its negative give a two-sided linear derivative r -> integral r dmu, continuous for the uniform norm. Conversely a linear two-sided derivative forces the minimum and maximum of integral r dmu over the active set to agree for every continuous r. Such tests separate Borel probabilities on compact K, so all active probabilities coincide. The active equality and delta>0 then determine c as well. No Fréchet conclusion is made from uniqueness alone.

## A genuine weight corner

Take n=1, K the closed unit disk, a=0, and fix delta>0. For q_t(z)=-t|z|^2, one has

\[
 F_{\delta,q_t}(0)=
 \begin{cases}-t,&0\le t,\\0,&-\delta/2\le t\le0.\end{cases}
\]

For t>=0, every raw competitor is at most -t on the boundary circle. The subharmonic maximum principle bounds it by -t on the open disk. Regularization preserves that bound near zero, while the constant -t is a global competitor. For t=-b with 0<=b<=delta/2, use the radial function

\[
 u_b(z)=\begin{cases}
 b|z|^2,&|z|\le1,\\
 b+\delta\log|z|,&|z|>1.
 \end{cases}
\]

It is continuous. Its distributional Laplacian is nonnegative: the interior density is 4b, the exterior density is zero and the outward radial derivative jump is delta-2b>=0. The function is therefore subharmonic and belongs to L_delta. It meets q_{-b} on K, and has value zero at the origin. Every raw competitor is bounded above there and nearby by the continuous obstacle b|z|^2, so its regularization has value at most zero at the origin. This proves the second branch. The two weight-direction derivatives are -1 and 0; the weight functional is not Gâteaux differentiable at the zero weight. The active-set criterion then implies more than one active probability. No unproved admissibility claim for a guessed probability is needed.

## Evidence and boundaries

The two complete current inputs for growth slopes and supporting probabilities are reused from their checked 424 reads, with the compact affine correspondence and pole repair as their explicit dependencies. Hahn--Banach, Riesz representation, weak compactness of probabilities and the one-variable subharmonic maximum principle remain standard named inputs. All new deductions above are reconstructed directly. They are not attributed to an unexamined result of Narzillaev, and do not close any original open direction.

Four attempted September monthly archive lists in math.CV, math.DG, math.AG and math.AP each return HTTP 404. No historical coverage is added. The eight successful current lists remain recorded at 424; their comparison is not a fresh full-abstract review. Historical announcement/replacement gaps remain pending.

This is a research review before manuscript integration. Preservation, package checks and private synchronization are recorded in the companion audit. The next unit is a scoped addition after the continuous-weight representation, with explicit directional topology, positive-growth bound, pointwise countability and the disk corner.

All 38 direct obligations and both complete mathematical reads pass at the stated scope. All 330 tracked book files and 999 proofs, both catalogues/manifests and 451 protected sources remain exact. The source package has 2147 archive entries and 2146 checksum-validated current payloads; all 327 packaged book-source files match the actual 424 empty reconstruction. No new author build, native call, fresh reconstruction or publication is claimed. Normal private synchronization follows actual diff review.
