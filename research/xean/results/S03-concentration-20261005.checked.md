# S03: checked zero-threshold concentration theorem

An explicit radial density criterion gives actual finite-mass exponential subsolutions on compact Hermitian products. For every prescribed smooth collapsing base sequence, tailored smooth positive projective factors yield a single strictly positive L1 probability density in the original concentration family with b_H(f)=0, solvable for every lambda>0. The task-granted principle gives greatest genuine finite-mass exact solutions, necessarily unbounded. The retained elliptic threefold gives concrete zero-lower-mass fourfold and fivefold examples. Subsolution masses are 96pi and 240pi; exact-solution masses are not identified with them. General classification and arbitrary previously chosen full-product families remain unresolved.

The substantive construction originated in an autonomous Xean original-task call with one explicitly supplied checked P07 background note. Its historical candidate=false is preserved. Complete original-task review, new statement-only reconstruction with notes=[], and separate scoped full comparison use gpt-6.1-sol xhigh, concurrency one, without arbitrary call caps. All ordinary proofs, full reports and current source were actually read and mathematically assessed. The unchanged prior factor proof and its five earlier complete independent reconstructions are retained and the new application is separately assessed. No verdict or candidate flag supplies mathematical authority; no accepted-note full-solver graph is claimed.

Exact primary applications of TW0910.1390v2 Cor1, Lamari1999 Lemma3.3, Demailly canonical compactness, Siu and bounded-product calculus, Bedford--Taylor1982 Thm2.1/Cor2.2, KN1312.5491v2 Thm0.1/Section1/Prop1.2 and Nguyen1501.00891v1 Cor0.2 were assessed with their actual hypotheses and dd^c conversions. The latter bounded/Lp theorems are never applied to the final unbounded zero-threshold L1 density. The supplied greatest-solution principle remains explicit background. Synthetic numerical execution, necessity, literature priority and recursive certification of all cited foundations are unclaimed. Model-assisted checking is not journal peer review.

## Complete frozen comparison assembly

# S03 complete scoped proof comparison

The new acceptance object is all scoped targets A--D. The exact original context and complete autonomous exploration proof assembly are retained unchanged. The exploration historical candidate=false is preserved. No report, verdict or candidate flag supplies mathematical authority. Historical pending labels do not assert completion. General original classification and arbitrary already-chosen concentration families remain unresolved.

## Entire unchanged exploration assembly and supplied prior factor proof

# S03 complete zero-threshold concentration argument

Independently assess the exact original task and every complete ordinary proof below. Neither the exploration candidate=false nor any prior review supplies mathematical authority. Preserve that historical flag. The proposed result is a substantive sufficient criterion and a rigorously constructed choice of the given concentration family on an actual compact Hermitian manifold with b_H(f)=0 and v_minus(H)=0. The general classification and arbitrary family choices remain unanswered; original_S03_completed=false.

## Exact original task

{
  "problem": "Let (X,h) be a connected compact Hermitian manifold with bounded-potential lower Monge-Ampere mass v_-(h)=0. Use dd^c=(i/(2 pi))partial barpartial and genuine h-psh potentials, locally a genuine psh function plus a smooth function with the canonical upper representative; arbitrary null-set modifications are excluded. Fix a smooth positive probability volume dV, a nonzero nonnegative f in L1(dV), and lambda>0. The individual threshold b_h(f)=lim_k c_h(min(f,k)) is the maximal a>=0 for which a genuine h-psh u satisfies MA_ext_h(u)>=a f dV. Assume b_h(f)=0. Original S03 asks to characterize when a genuine, possibly unbounded exponential subsolution s exists with MA_ext_h(s)>=exp(lambda s) f dV, and hence when there is a greatest finite-mass exact solution of MA_ext_h(u)=exp(lambda u) f dV. The exponential right-hand side is zero on poles, and extended non-pluripolar products do not charge poles.\n\nThe supplied existing result is that any such exponential subsolution gives a greatest exact finite-mass solution by decreasing bounded-density approximation. A positive individual threshold provides exponential subsolutions for every exponent; that case is excluded here. Conversely the greatest solution is a subsolution. For f in Lp, p>1, a bounded continuous equation exists, but such f have positive threshold and do not address the question at b_h(f)=0. A genuine unbounded solution must not be replaced by a bounded one.\n\nThe lower-mass concentration construction has the following explicitly defined family. Choose smooth strictly positive probability densities f_j with c_h(f_j)<=2^(-2j), and set f=sum_(j>=1)2^(-j)f_j. Then f is L1, integral f dV=1 and f>= (1/2) min f_1>0. It has b_h(f)=0: any positive scaled subsolution would give a*2^(-j)<=c_h(f_j) for all j. This proves no bounded exponential subsolution because a bounded s makes exp(lambda s) bounded below, but it does not exclude an unbounded exponential subsolution. The choices of f_j are not unique; when testing this concentration family distinguish conclusions for every such choice, for a rigorously constructed choice, or under additional explicitly proved hypotheses on the choice.\n\nNo candidate measure hypothesis, potential construction, obstruction, family choice or proof is supplied.",
  "completionCriteria": "Prove substantive intrinsic geometric or density criteria for exponential solvability at zero individual threshold, with a nonvacuous b_h(f)=0 example or counterexample. Address the stated concentration family to the extent that can actually be proved, declaring the quantifier over its choices. Preserve genuine canonical admissibility, unbounded-potential non-pluripolar products, the exact exponential coefficient and finite mass of the resulting greatest solution. A reformulation as existence of a subsolution or as noncollapse of the already-defined approximating solutions, a result for positive threshold or Lp p>1, or the existing bounded obstruction alone is not new progress on S03. Check indispensable external theorem hypotheses against primary sources and independently reconstruct the full proof. Keep any sufficient-condition result or named example scoped and identify any unresolved classification."
}


## Complete ordinary notes and support

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "Explicit sufficient density-growth criterion on a split Hermitian product X0×P^k. A canonical radial potential has finite non-pluripolar mass and supplies exponential attenuation with the exact requested coefficient. This is a restricted sufficient condition; n2 establishes zero-threshold nonvacuity.",
      "detailedSummary": "For H=h0+κ, C=binomial(m+k,m), V0=∫h0^m and μ=(h0^m/V0)∧κ^k, define L=1−log(Σi≥1|zi|²/Σi≥0|zi|²) and u=1−L^α, 0<α<1. The note reconstructs genuine canonical admissibility, the explicit projective density qα, projective non-pluripolar mass one, and product mass CV0. If f/(μ/dV)≤Aqα exp(λ(L^α−1)), an explicit constant shift of u is an exponential subsolution with coefficient λ and mass CV0. An equivalent critical radial growth condition and a condition sufficient for every exponent are given. The greatest exact solution follows from the implication supplied in the task. Necessity and general Hermitian geometry remain unresolved.",
      "text": "This is a mathematical proof draft of a sufficient geometric/density criterion, not a classification of S03. Its nonvacuity at zero threshold is proved in n2. Use dd^c=i∂bar∂/(2π), with ordinary wedge powers.\n\nLet (X0,h0) be connected compact Hermitian of dimension m. Let Y=P^k, k≥1, carry normalized Fubini–Study κ with ∫Yκ^k=1. On X=X0×Y put H=h0+κ, N=m+k, C=binomial(N,m), V0=∫X0h0^m, and μ=(h0^m/V0)∧κ^k. Pullbacks are understood. For any smooth positive probability dV, put R=μ/dV. Thus R is smooth and bounded above and below by positive constants. Write F=f/R, so f dV=Fμ.\n\nFix 0<α<1 and o=[1:0:…:0]. Define, off o,\nψ=log(Σi≥1|zi|²/Σi≥0|zi|²), L=1−ψ, and u=1−L^α.\nSet u(o)=−∞, its canonical value. In the chart z0=1 put r=Σi≥1|zi|²; then L=1−log(r/(1+r)). Define\n t=exp(1−L), a=αL^(α−1),\n Q=t+(1−t)a,\n D=t(1−a)+(1−t)α(1−α)L^(α−2),\n qα=Q^(k−1)D exp(k(L−1)).\nThis gives a smooth positive density on Y\\{o}, including by smooth extension the hyperplane z0=0, where its value is 1−α. Below we prove MAκ^ext(u)=qακ^k, ∫qακ^k=1, and qα≥(1−α)^k.\n\nFor a fixed λ>0, the sufficient density condition is\n F(x,y)≤Aqα(y)exp(λ(L(y)^α−1))                                      (1)\nalmost everywhere off X0×{o}, for some finite A>0. Under (1), the genuine H-psh function\n sλ=u+(1/λ)log(CV0/A)                                               (2)\nsatisfies MAH^ext(sλ)≥exp(λsλ)f dV and has total mass exactly CV0. The supplied subsolution-to-greatest-solution implication therefore gives a greatest exact finite-mass solution. No positive individual threshold is required.\n\nThe hypothesis is an explicit density test, with no unknown potential. One useful growth formulation is the following. Put p=1+k(1−α). Suppose F is essentially bounded on every compact subset of X\\(X0×{o}). If, for all sufficiently large L, uniformly essentially over x and the projective spheres,\n F(x,y)≤A′exp(k(L−1)+λL^α)L^(−p),                                 (3)\nthen (1) holds with another finite constant. In r coordinates, this is critical growth r^(−k), a logarithmic decay of power p, and an exp(λ|log r|^α) allowance.\n\nFor one density to pass for every λ>0, it suffices that F be locally essentially bounded off the displayed fiber and\n ess limsup(y→o) ess sup_x [log⁺(F(x,y)/qα(y))/L(y)^α]=0.             (4)\nFor a fixed λ, (4) bounds F/qα by exp((λ/2)L^α) near o. The remaining compact region has bounded ratio. Increasing a finite constant gives (1).\n\nGenuine admissibility is established directly. For 0<ε≤1, define\n ψε=log((Σi≥1|zi|²+ε|z0|²)/Σi≥0|zi|²).\nThis is smooth, ≤0, and κ-psh: locally κ+dd^cψε is dd^c of the logarithm of a positive sum of squared holomorphic coordinates. The function χ(t)=1−(1−t)^α, t≤0, has 0<χ′≤α and χ″>0. Hence\n κ+dd^cχ(ψε)=(1−χ′)κ+χ′(κ+dd^cψε)+χ″dψε∧d^cψε≥(1−α)κ.\nAs ε decreases to zero, these smooth functions decrease to u. Near o, |u|=O(1+|log r|^α), which is locally integrable against smooth volume. The decreasing local psh-plus-smooth limit is therefore nontrivial, and the submean inequalities pass to it. It is the genuine canonical κ-psh function, with value −∞ at o. Its pullback is genuine H-psh. Adding the constant in (2) changes neither admissibility nor mass. No potential is modified on a null set.\n\nThe non-pluripolar measure and its mass can also be computed directly. On the affine chart, a local primitive of κ+dd^c u is\n Φ(r)=log(1+r)+1−[1−log(r/(1+r))]^α.\nDifferentiation gives rΦ′(r)=(r+αL^(α−1))/(1+r)=Q. The complex Hessian has tangential eigenvalue Φ′, repeated k−1 times, and radial eigenvalue Φ′+rΦ″=dQ/dr. Both are positive. Polar integration yields\n ∫{a<r<b}(dd^cΦ)^k=Q(b)^k−Q(a)^k.                                (5)\nIndeed, the determinant is (Q/r)^(k−1)Q′ and radial smooth volume is a fixed constant times r^(k−1)dr. Its primitive is therefore a fixed constant times Q^k. The constant is one by comparison with the normalized Fubini–Study primitive log(1+r), whose flux is (r/(1+r))^k and whose total mass is one.\n\nIn the L coordinate, dQ/dL=−D. The radial Fubini–Study probability is k exp(−k(L−1))dL, oriented toward the pole. Thus (5) gives exactly qα above. Q tends to zero at r=0 and to one at infinity. The omitted hyperplane has zero smooth volume, and u is smooth there. On {u>−J}, max(u,−J) agrees with smooth u. These sets exhaust Y\\{o}; the defining non-pluripolar exhaustion discards the pole and cutoff-level masses. Consequently\n MAκ^ext(u)=qακ^k,  ∫Yqακ^k=1.\nThis is a flux computation, not an inference of full mass from zero Lelong number. The strict positivity bound proves qα≥(1−α)^k off the pole.\n\nOn X\\(X0×{o}), sλ is smooth. Factor dimensions give\n (H+dd^csλ)^N=C h0^m∧(κ+dd^cu)^k.\nUsing the same non-pluripolar exhaustion gives\n MAH^ext(sλ)=CV0qαμ, with mass CV0.                               (6)\nNo singular current is restricted to a fiber. Equations (1), (2), and (6) imply\n exp(λsλ)f dV≤(CV0/A)exp(λu)Aqαexp(−λu)μ=MAH^ext(sλ).\nBoth measures give zero mass to the polar fiber. This verifies the exact exponential coefficient.\n\nAs L→∞,\n Q~αL^(α−1), D~α(1−α)L^(α−2),\n qα~α^k(1−α)exp(k(L−1))L^(−1−k(1−α)).                            (7)\nThe radial density of qακ^k is\n W(L)=kQ^(k−1)D~kα^k(1−α)L^(−1−k(1−α)).\nFor every τ>0,\n exp(τ(L^α−1))W(L)→∞.                                           (8)\nThe logarithm is τL^α minus a fixed multiple of log L, which tends to infinity. Every punctured neighborhood of o therefore has infinite mass for qαexp(−τu)κ^k, although qακ^k has mass one. Relation (7) proves the comparison needed for (3).\n\nIf v−(h0)=0, then v−(H)=0. For any bounded genuine h0-psh v, the bounded product calculus gives\n MAH(v)=C MAh0(v)∧κ^k.\nTo verify the algebra, locally write h0+dd^cv=dd^c(v+ρ)+(h0−dd^cρ), with v+ρ bounded psh and ρ smooth. Expand the defining multilinear bounded products and smooth-background corrections. Pullback respects these expressions; degrees exceeding m on the base or k on the projective factor vanish. The only surviving total-degree N term has coefficient C. Pulling back bounded potentials with masses tending to zero proves the claim.\n\nDependencies and scope: the greatest-exact-solution implication is used exactly as supplied in the task. No result from background-P07 is needed in this note. The radial admissibility, density, mass, and product calculation have been reconstructed. This is a sufficient condition on a split product; necessity, arbitrary metrics, and all choices in the concentration family are not established.\n\nArtifacts and evidence: the full proof is retained in n1.txt. Rerun the small check with `python radial_check.py artifacts/radial_input.json > artifacts/radial_output.json`. It symbolically checks rΦ′=Q and −dQ/dL=D. At α=1/2, k=1, both checks returned true; the finite radial mass from L=1 to 100 was 0.95, remaining flux was 0.05, and their sum was 1.0 to the reported precision. Numerical integration is not interval certified and does not prove the analytic limits or compact-manifold claims. Environment, commands, and source-access records are in artifacts/environment.txt, artifacts/commands.txt, and sources/source_checks.txt. No resource-heavy computation was used.\n\nArtifacts: /workspace/research/native-workers/codex-4t3gPZ",
      "support": []
    },
    {
      "id": "n2",
      "summary": "A rigorously constructed choice of the specified concentration family has bH(f)=0 but admits genuine unbounded exponential subsolutions, hence greatest finite-mass exact solutions, for every λ>0. Background-P07 supplies a concrete compact fourfold. Arbitrary family choices and the full S03 classification remain unresolved.",
      "detailedSummary": "Given smooth positive base probabilities Fj with ch0(Fj)≤2^(−2j)/C, construct smooth positive projective probabilities gj with disjoint annular bumps and tiny smooth baselines. For fj=(μ/dV)Fjgj, a directly proved radial ODE and factor equation give cH(fj)=Cch0(Fj)≤2^(−2j). Thus f=Σ2^(−j)fj is a positive probability, finite everywhere and smooth off the polar fiber, with bH(f)=0. The jth bump is bounded by qαexp((L^α−1)/j), so this single f passes n1 for every positive exponent. Explicit subsolutions have mass CV0; the greatest exact solutions follow from the task’s supplied implication and are necessarily unbounded. Their numerical mass and a formula for them are not asserted. The supplied elliptic quotient provides actual smooth collapsing base potentials, giving a fourfold with subsolution mass 96π or a fivefold with mass 240π. The result concerns tailored choices, not every permitted concentration family. Numerical checks use synthetic inputs and are illustrative. Necessity and a nonsolvable zero-threshold example remain open.",
      "text": "This is restricted mathematical progress, conditional on the supplied normalization and greatest-solution premises and on the supplied background-P07 geometry. It proves solvability for a rigorously constructed choice in the concentration family, not for every allowed choice, and does not classify unrestricted S03.\n\nUse the product notation of n1. Suppose the base has smooth strictly positive probability densities Fj relative to dV0=h0^m/V0 satisfying\n ch0(Fj)≤2^(−2j)/C.                                                (9)\nWe construct smooth strictly positive probabilities gj relative to κ^k such that\n fj(x,y)=R(x,y)Fj(x)gj(y),  f=Σj≥1 2^(−j)fj                        (10)\nhas integral one, is finite everywhere, is smooth off X0×{o}, and is bounded below by (1/2)minXf1>0. Its component scalars satisfy cH(fj)=Cch0(Fj)≤2^(−2j), so bH(f)=0. This one density has exponential subsolutions and greatest exact finite-mass solutions for every λ>0. All its exact exponential solutions are unbounded. If v−(h0)=0, n1 also gives v−(H)=0.\n\nThe construction works for every base sequence satisfying (9), by tailoring the projective densities to that sequence. It is not a theorem about arbitrary components already chosen on the full product.\n\nThere is an actual compact example. Take the supplied elliptic quotient X0=Ω/〈g〉, where Ω={[z:w]∈P^3:z,w∈C^2 are nonzero} and g[z:w]=[z:exp(2π)w]. Its supplied metric is\n h0=ω=α0+β0+dt∧d^ct,  t=log(‖w‖²/‖z‖²).\nBackground-P07 proves compactness, connectedness, positivity, V0=24π, and actual smooth potentials vl with h0+dd^cvl>0 and δl=∫(h0+dd^cvl)^3→0. Only those geometric and collapsing-potential conclusions are imported; its positive-threshold product densities are not used.\n\nChoose a subsequence with δl≤2^(−2j)/C and define\n Fj=((h0+dd^cvl)^3/dV0)/δl.\nThese are smooth positive probabilities. The displayed equation and supplied uniqueness of the normalization scalar give ch0(Fj)=δl, proving (9). Thus the sequence needed here is available, rather than an unresolved premise. Taking k=1 gives a compact complex fourfold with C=4 and explicit subsolution mass CV0=96π. Taking k=2 gives subsolution mass 240π. These are not asserted masses of the greatest exact solutions.\n\nFix 0<α<1 once and for all and use u,L,qα from n1. Put\n wj=2^(−j), Mj=maxX0Fj, b0=(1−α)^k,\n Bτ(y)=qα(y)exp(τ(L(y)^α−1)).\nThen Bτ≥b0, and its radial measure is exp(τ(L^α−1))W(L)dL, with W from n1.\n\nChoose 0<εj≤1/2 such that\n wjεjMj≤b0 2^(−j−2).                                             (11)\nAlso impose wjεj‖Fj‖Cj≤2^(−j), using fixed smooth coordinate seminorms. Both conditions are possible for each smooth Fj. The baseline\n E(x)=Σj wjεjFj(x)\nthen converges smoothly: for each fixed derivative order, all sufficiently large j are controlled by the second condition. It satisfies 0<E≤b0/4.\n\nChoose one smooth cutoff ρ supported in [0,1], positive inside, flat at the endpoints, with 0≤ρ≤1; for example ρ(t)=exp(4−1/(t(1−t))) on (0,1), zero outside. Inductively choose Aj≥2 and Aj>Aj−1+2 such that\n Zj=∫Aj^(Aj+1) ρ(L−Aj)exp((L^α−1)/j)W(L)dL≥2wjMj.                 (12)\nThis choice is rigorously possible. For each fixed j, equation (8) of n1 shows that exp((L^α−1)/j)W(L) tends uniformly to infinity on [A,A+1] as A→∞. Since ∫ρ>0, the integral tends to infinity. Successive doubling gives a constructive search that terminates analytically. The annuli are disjoint and tend to the pole.\n\nOn the jth annulus define\n bj(y)=ρ(L(y)−Aj)B1/j(y)/Zj,                                      (13)\nand set it to zero outside. The annulus is compactly contained in Y\\{o} and misses z0=0. Flatness of ρ makes extension by zero smooth. Each individual bump also vanishes on a neighborhood of o. It is radial, smooth globally, and has integral one by (12). Set\n gj=εj+(1−εj)bj.                                                  (14)\nThis is a smooth strictly positive probability. Moreover,\n wjMj(1−εj)bj≤B1/j/2                                              (15)\non its annulus. Different bump supports are disjoint.\n\nWe directly solve the smooth projective component equation, avoiding a new external existence theorem. For g=gj, set\n G(r)=∫{|z|²<r}gκ^k,  Qg(r)=G(r)^(1/k).\nDefine a radial φ, up to an additive constant, by\n φ′(r)=[Qg(r)−r/(1+r)]/r.                                        (16)\nThe local primitive Φg=log(1+r)+φ has tangential eigenvalue Qg/r>0 and radial eigenvalue Qg′>0, because g is positive. The flux formula from n1 gives\n (κ+dd^cφ)^k=gκ^k.                                                (17)\n\nGlobal smoothness and positivity require checking both ends. For small r, the bump is zero, so G(r)=εj(r/(1+r))^k and φ=(εj^(1/k)−1)log(1+r)+constant, smooth at the origin. For large r, the entire bump has been integrated, so\n G(r)=1−εj+εj(r/(1+r))^k.\nWith v=1/r, Qg=(1−εj+εj(1+v)^(−k))^(1/k) is analytic near zero and equals one there. Equation (16) becomes dφ/dv=−(Qg−1/(1+v))/v, analytic at zero. Since v=|z0|²/Σi≥1|zi|² is smooth near z0=0, φ extends smoothly over that hyperplane. The tangential metric there is κ and the transverse coefficient is εj>0. At the origin the metric is εj^(1/k)κ. This proves smooth strict positivity and (17), including k=1.\n\nNow compute the exact component scalar. Let vj be the supplied bounded continuous normalized solution\n MAh0(vj)=ch0(Fj)Fj dV0.\nIn the concrete example, it can be chosen smooth from the collapsing sequence. Let φj solve (17) and put Uj(x,y)=vj(x)+φj(y). This is a genuine bounded H-psh function. Factor dimensions and the bounded product algebra reconstructed in n1 give\n MAH(Uj)=C MAh0(vj)∧(κ+dd^cφj)^k\n         =Cch0(Fj)Fjgjμ\n         =Cch0(Fj)fj dV.\nSubtracting the supremum normalizes Uj without changing the equation. Since fj is smooth and strictly positive, supplied scalar uniqueness gives\n cH(fj)=Cch0(Fj).                                                 (18)\nThe factor R is retained for arbitrary dV.\n\nPositivity and Tonelli yield ∫f dV=Σwj=1. Away from the polar fiber, only finitely many annuli meet any compact neighborhood, and\n F=f/R=E(x)+Σj wj(1−εj)Fj(x)bj(y)\nis smooth. On the polar fiber every individual bj vanishes, and the same pointwise sum is the finite E(x). Thus f is finite everywhere. Also f≥w1f1, giving the required uniform positive lower bound.\n\nTo prove zero threshold, suppose a>0 and a genuine H-psh v satisfied MAH^ext(v)≥af dV. For every j it would satisfy MAH^ext(v)≥awjfj dV. The supplied maximal-threshold property and (18) imply\n awj≤bH(fj)=cH(fj)≤2^(−2j),\nhence a≤2^(−j) for every j, impossible. Therefore bH(f)=0. This checks the stated concentration-family constraints on the full product densities fj, not merely on base densities.\n\nFix any λ>0. Choose J with 1/j≤λ for j≥J. Since u≤0, B1/j≤Bλ for those indices. Disjoint supports and (15) imply that the entire tail of annular contributions is at most Bλ/2 at each point. The baseline is at most b0/4≤Bλ/4. The remaining finitely many contributions have bounded coefficient\n Kλ=maxY Σj<J wj(1−εj)Mj bj<∞.\nSince Bλ≥b0, they are at most (Kλ/b0)Bλ. Consequently\n F≤DλBλ,  Dλ=3/4+Kλ/b0>0.                                       (19)\nBy n1, the explicit genuine subsolution\n sλ=u+(1/λ)log(CV0/Dλ)\nsatisfies\n MAH^ext(sλ)=CV0qαμ≥exp(λsλ)f dV,\nwith total mass CV0. Its pole is canonically X0×{o}; both sides assign that fiber zero mass. The density has not been used to change any value of the potential. The density f is fixed independently of λ.\n\nThe same construction verifies n1’s criterion (4). On the jth annulus,\n F/qα≤1/4+(1/2)exp((L^α−1)/j);\noutside all annuli it is at most 1/4. As y→o through annuli, j→∞ and L→∞. Taking positive logarithms and dividing by L^α gives the required limit uniformly in x.\n\nThe task’s supplied subsolution-to-greatest-solution theorem now applies for each λ to this same f. It gives a greatest genuine exact solution uλ with\n MAH^ext(uλ)=exp(λuλ)f dV.\nIts mass is finite: a nontrivial genuine quasi-psh function on compact X has a finite upper bound and f is L1. Its mass is positive because f>0 and uλ is finite almost everywhere. No numerical value CV0 is asserted for this solution’s mass, and it is not identified with sλ. A bounded exponential subsolution would have exp(λs) bounded below by a positive constant, contradicting bH(f)=0. Hence the exact solutions obtained here are genuinely unbounded. This bounded obstruction is used only to distinguish the new unbounded solutions, not offered as new progress itself.\n\nDependencies and source check: this note uses n1 and background-P07’s quotient geometry, V0, and smooth collapsing potentials. Threshold maximality, bounded scalar uniqueness, and the greatest-solution implication are supplied by the task. No new global existence theorem is assumed. As a consistency check, Tosatti–Weinkove, https://arxiv.org/pdf/0910.1390v2, Corollary 1 on PDF page 1 and closed normalization on page 2, was inspected at the primary source. Its smooth normalization theorem covers compact Hermitian manifolds of dimension at least two and smooth positive densities. Its operator is i∂bar∂; multiplying its potential by 2π gives this task’s convention. It is not applied to the unbounded density f. The projective equation is independently proved by (16)–(17).\n\nProof and implementation artifacts: n1.txt, n2.txt, radial_check.py, artifacts/radial_input.json, artifacts/radial_output.json, artifacts/environment.txt, artifacts/commands.txt, sources/source_checks.txt, and deliverable.json. Rerun with `python radial_check.py artifacts/radial_input.json > artifacts/radial_output.json`.\n\nThe numerical input uses α=1/2, k=1 and six synthetic base suprema 10^j. It does not compute elliptic-quotient densities or thresholds. Both symbolic derivative checks returned true. Finite radial mass 0.95 plus remaining flux 0.05 returned 1.0 to the reported precision. The six logarithmic intervals were [192,193], [1552,1553], [6216,6217], [12436,12437], [24876,24877], and [49756,49757]. Their Zj values were approximately 14.0190, 342.2607, 36385.8367, 69098.9377, 1002663.2577, and 102364185.2667, against required bounds 10, 50, 250, 1250, 6250, and 31250. The largest computed coefficient wjMj(1−εj)/Zj was 0.3521994623<1/2. The six-term baseline bound was 0.123046875<0.125=b0/4. These are finite implementation observations, not interval-certified proofs or exhaustive mathematical results. Infinite termination follows analytically from (8) and (12). Python compilation and deliverable-format checks passed. No resource-heavy computation was launched.\n\nThe direct curl attempt to cache the primary PDF failed because the inherited proxy was unreachable; public web inspection succeeded. No proxy bypass or credential inspection was attempted. The access record is retained in sources/source_checks.txt.\n\nUnresolved scope: this establishes a substantive sufficient density criterion and actual zero-threshold examples. It disproves any blanket inference that zero threshold or the concentration-family format prevents exponential solvability. It does not show that every allowed family choice is solvable, does not supply a nonsolvable zero-threshold example, and does not establish necessity or a classification on arbitrary Hermitian manifolds. The full original S03 question remains unresolved.\n\nArtifacts: /workspace/research/native-workers/codex-4t3gPZ",
      "support": [
        "n1",
        "background-P07"
      ]
    }
  ],
  "candidate": false,
  "workspace": "/workspace/research/native-workers/codex-4t3gPZ"
}

## Complete unchanged supplied prior factor proof

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\dc}{d^c}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\PSH}{\operatorname{PSH}}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Exact equations for $L^1$ densities on products with zero lower mass}
\author{}\date{}
\begin{document}\maketitle
\begin{abstract}
Let a compact Hermitian manifold of zero lower Monge--Amp\`ere mass be
multiplied by a normalized projective space. We construct explicit
probability densities in $L^1$ and in no $L^p$, $p>1$, whose individual
thresholds are positive and computed exactly. A genuine unbounded
potential solves the exact finite-mass equation and belongs to the
stretching envelope class; every smaller-background obstacle envelope
has an actual competitor. The threshold calculation retains the
truncations for an arbitrary smooth reference probability. We give a
complete proof of the supplied elliptic-quotient factor construction,
with a direct smooth normalization estimate, and obtain a concrete
fivefold with threshold $240\pi$. The unrestricted zero-lower-mass
$L^1$ equation and potential selection remain open.
\end{abstract}

Use $\ddc=i\partial\bar\partial/(2\pi)$, $\dc=i(\bar\partial-\partial)/(4\pi)$
and ordinary wedge powers. All quasi-psh functions have their genuine
canonical values. The extended measure is the non-pluripolar product
with smooth-background corrections. For a Hermitian form $h$ write
\[
 v_-(h)=\inf_{u\in\PSH(X,h)\cap L^\infty}\int_X(h+\ddc u)^n,
 \qquad b_h(f)=\lim_{j\to\infty}c_h(\min(f,j)).
\]
We use the supplied normalization theorem: $c_h(g)>0$ is the unique
scalar of the normalized continuous bounded-density equation, and
$b_h(f)$ is the maximal scalar of a genuine extended subsolution.
Consequently $b_h$ is decreasing in its density and satisfies
$b_h(tf)=b_h(f)/t$, $t>0$. For bounded densities its truncations are
eventually constant, so $b_h=c_h$. These facts do not identify an
unbounded exact solution.

The stretching class $\mathcal E_{\rm env}(X,h,0)$ consists of genuine
$h$-psh $u\preceq0$ for which every $t\geq1$ admits an $h$-psh $a_t$
with $t^{-1}a_t\leq u$, canonically also at common poles.

\section{The product theorem}
Let $(X_0,h_0)$ be connected and compact of complex dimension $m$,
with $v_-(h_0)=0$, and put $V_0=\int_{X_0}h_0^m>0$.
Let $Y=\mathbb P^k$, $k\geq2$, with normalized Fubini--Study form
$\kappa$, $\int_Y\kappa^k=1$. On $X=X_0\times Y$, of dimension
$N=m+k$, put
\[
 H=h_0+\kappa,\quad C=\binom Nm,\quad
 \mu=\frac{h_0^m}{V_0}\wedge\kappa^k,\quad R=\frac\mu{dV},
\]
where $dV$ is any smooth strictly positive probability on $X$.
All factor forms and functions are pulled back when necessary.
For $0<\alpha<1$ define
\[
 \psi([z])=\log\frac{\sum_{i=1}^k|z_i|^2}{\sum_{i=0}^k|z_i|^2},
 \qquad u_\alpha=1-(1-\psi)^\alpha.
\]
Its unique pole is $o=[1:0:\cdots:0]$. Write
$\MA_\kappa^{\rm ext}(u_\alpha)=q_\alpha\kappa^k$, with density
value $q_\alpha(o)=+\infty$, a harmless measure-zero convention.

\begin{theorem}\label{th:product}
The density $f=R q_\alpha$ is a probability in $L^1(dV)$ and in no
$L^p(dV)$, $p>1$. The genuinely nonclosed product metric satisfies
$v_-(H)=0$, while
\[
 b_H(f)=C V_0>0,\qquad
 \MA_H^{\rm ext}(u_\alpha)=b_H(f)f\,dV.
\]
The displayed solution has supremum zero and finite total mass $CV_0$.
Moreover,
\[
 u_\alpha\in\mathcal E_{\rm env}(X,H,0).
\]
For every $0<\delta<1$
the obstacle envelope $P_{\delta H}(u_\alpha)$ is genuine.
\end{theorem}

\section{The singular density on the closed factor}
The logarithmic norm $\psi$ is a genuine $\kappa$-psh function, because locally
\[
 \kappa+\ddc\psi=\ddc\log\sum_{i\geq1}|z_i|^2\geq0.
\]
The increasing convex function $\chi(t)=1-(1-t)^\alpha$ has
$0<\chi'\leq\alpha$. The composition is $\kappa$-psh, by the smooth
chain rule off its pole and bounded truncation/local regularization
at the pole. Off $o$ it satisfies
$\kappa+\ddc u_\alpha\geq(1-\alpha)\kappa$. It is smooth along
the hyperplane $z_0=0$ and has supremum zero there.

In the affine chart $z_0=1$, put $r=\sum_{i\geq1}|z_i|^2$ and
\[
 F(r)=\log(1+r)+1-\left[1-\log\frac r{1+r}\right]^\alpha,
 \quad Q(r)=rF'(r)
 =\frac{r+\alpha[1-\log(r/(1+r))]^{\alpha-1}}{1+r}.
\]
Radial Stokes with our normalization gives
\[
 \int_{a<|z|^2<b}(\ddc F)^k=Q(b)^k-Q(a)^k.
\]
Indeed the tangential eigenvalue is $F'$ with multiplicity $k-1$ and
the radial eigenvalue is $F'+rF''$; polar integration is the derivative
of $(rF')^k$, with its constant fixed by normalized Fubini--Study mass.
Here $Q(0)=0$ and $Q(\infty)=1$. The omitted hyperplane is smooth and
has zero measure, so the non-pluripolar mass is one. This is a direct
flux calculation, rather than a deduction from zero Lelong number.

Near the pole put $L=1-\log r$. The tangential and radial eigenvalues
are respectively comparable to $r^{-1}L^{\alpha-1}$ and
$r^{-1}L^{\alpha-2}$. Thus
\begin{equation}\label{eq:density}
 q_\alpha(r)\asymp r^{-k}L^{-1-k(1-\alpha)}.
\end{equation}
The radial smooth volume is comparable to $r^{k-1}dr$, proving $L^1$
integrability. For every $p>1$ the substitution $r=e^{1-L}$ leaves
the exponentially increasing factor $e^{k(p-1)L}$, proving divergence.
In particular $q_\alpha\to+\infty$ uniformly as $r\downarrow0$.
Every $q_j=\min(q_\alpha,j)$ is therefore strictly positive and
continuous on all of $Y$, including $o$. Its integral $M_j$ increases
to one. This density convention never alters the canonical pole of $u_\alpha$.

\section{The exact threshold and product measure}
First take smooth $g>0$ on $Y$, with $M_g=\int_Yg\kappa^k$.
Smooth existence in the closed class \cite[Corollary 1]{TW} gives
\[
 A_g=\kappa+\ddc\phi_g>0,\qquad A_g^k=(g/M_g)\kappa^k.
\]
Closed integration forces the source scalar to zero; our potential
is $2\pi$ times the source potential. The pulled-back smooth function
solves the actual full-product equation
\[
 (H+\ddc\phi_g)^N=C h_0^m\wedge A_g^k
                  =(CV_0/M_g)R g\,dV.
\]
Uniqueness of the bounded equation scalar gives $c_H(Rg)=CV_0/M_g$.
For strictly positive continuous $g$, smooth uniform approximation,
its positive lower bound, density monotonicity and reciprocal homogeneity
give the same identity by a multiplicative squeeze. No rough product
limit is needed. Hence $c_H(Rq_j)=CV_0/M_j$.

Put $a=\min_XR>0$ and $A=\max_XR$. The exact original truncation obeys
\[
 R\min(q_\alpha,j/A)\leq\min(Rq_\alpha,j)
                      \leq R\min(q_\alpha,j/a).
\]
Using the continuous-factor identity at both real truncation levels gives
\[
 \frac{CV_0}{M_{j/a}}\leq c_H(\min(f,j))
                       \leq\frac{CV_0}{M_{j/A}}.
\]
Both bounds tend to $CV_0$, proving the exact threshold for arbitrary $dV$.

Now compute the actual unbounded equation separately. Bounded local
products and factor dimensions give
\[
 \MA_H(\max(u_\alpha,-j))
   =C h_0^m\wedge\MA_\kappa(\max(u_\alpha,-j)).
\]
Multiplying by $\mathbf1_{\{u_\alpha>-j\}}$ and taking the defining
non-pluripolar limit yields
\[
 \MA_H^{\rm ext}(u_\alpha)
   =C h_0^m\wedge q_\alpha\kappa^k=CV_0 f\,dV.
\]
This is finite of mass $CV_0$; it is not inferred from scalar convergence.
Smooth bounds on $R$ preserve all the integrability conclusions.

For bounded $h_0$-psh functions $v_j$ with masses tending to zero,
the same local factor expansion gives
\[
 \int_X\MA_H(v_j)=C\int_{X_0}\MA_{h_0}(v_j)\longrightarrow0.
\]
This expansion follows by binomial algebra of local bounded psh products
and smooth-background corrections; no singular current is restricted
to a fiber. Thus $v_-(H)=0$. If $h_0$ were closed positive, bounded
Stokes would fix all its bounded masses to $V_0>0$. Therefore $h_0$
and $H$ are nonclosed.

\section{Actual envelope competitors}
Fix $t\geq1$, choose $\alpha<\beta<1$ and $\varepsilon\beta\leq1$.
The finite constant
\[
 K_t=\sup_{s\geq1}\{ts^\alpha-\varepsilon s^\beta\}-t
\]
makes $a_t=-\varepsilon(1-\psi)^\beta-K_t\leq t u_\alpha$.
Its increasing convex composition has derivative at most
$\varepsilon\beta$, so $\ddc a_t\geq-\kappa$. Its pullback is genuine
$H$-psh, canonically minus infinity at the common pole. Together with
$u_\alpha\leq0$ this proves the precise stretching-class membership.
For $P_{\delta H}$ use $t=1$ and $\varepsilon\beta\leq\delta$.
This supplies an actual $\delta H$-psh competitor below the obstacle.
The upper-regularized envelope remains below the usc obstacle and above
this competitor, hence is genuine and not identically minus infinity.

\appendix
\section{A supplied zero-lower-mass factor, with a complete application proof}
We reproduce the named factor construction supplied in the author's
manuscript; it is not claimed as a new result. Its last normalization
step is proved here directly, without importing a duality formula.

Set $q=e^{2\pi}$, $\Omega=\{[z:w]\in\mathbb P^3:z,w\ne0\}$,
$z,w\in\mathbb C^2$, and $g[z:w]=[z:qw]$.
The free cyclic action has $t=\log(\|w\|^2/\|z\|^2)$ shifted by $4\pi$;
bounded $t$ ranges give proper discontinuity. Its strip $0\leq t\leq4\pi$
is compact: in total-norm-one coordinates both blocks stay away from zero.
It meets every orbit. Thus $X_0=\Omega/\langle g\rangle$ is a connected
compact complex threefold. It maps to $\mathbb P^1\times\mathbb P^1$
with elliptic fiber $\mathbb C/(2\pi\mathbb Z+2\pi i\mathbb Z)$.
Let $\alpha_0,\beta_0$ be the normalized base forms. Then
\[
 \omega=\alpha_0+\beta_0+dt\wedge\dc t>0
\]
descends. The base and vertical kernels have zero intersection.

In the product chart use $x=z_1/z_0$, $y=w_1/w_0$,
$\zeta=\log(w_0/z_0)$, and $\sigma_v=i\,dv\wedge d\bar v/(2\pi)$.
Let $p$ be a smooth probability relative to $\sigma_v$, positive on
$|v|<1$ and zero on $|v|\geq1$. Take a smooth $0\leq\chi_0\leq1$,
supported there and equal to one on $|v|\leq1/2$; put
$\chi=\chi_0(x)\chi_0(y)$ and
\[
 B_\delta=\chi\delta^{-2}p(\zeta/\delta)\sigma_\zeta,
 \quad C_\delta=\sup_{\Theta>0,\ \ddc\Theta=0,\ \int\omega\Theta=1}
                  \int B_\delta\Theta.
\]
Smooth extension by zero makes $B_\delta$ global, and $B_\delta\leq M_\delta\omega$
makes $C_\delta$ finite. The test family is nonempty: direct differentiation
gives $d(\omega^2)=0$, and $\omega^2/(24\pi)$ is a normalized strictly
positive test. In fact $C_\delta\to\infty$. Otherwise Lamari's
lemma \cite[Lemma 3.3]{Lamari}, applied to the smooth possibly nonclosed
$C\omega-B_{\delta_l}$, gives genuine $v_l$ with supremum zero and
$C\omega+\ddc v_l\geq B_{\delta_l}$.

For clarity normalized compactness here follows from local submean and
\cite[I.4.21, I.5.8--5.9]{Dem}. Cover by inner coordinate balls of
radius $r_i$ with outer radius $4r_i$, and choose bounded nonnegative
smooth $\rho_i$ making $v_l+\rho_i$ psh. At a maximum point of $v_l$,
submean on a ball of radius $2r_i$ bounds $\int_{B_i}(-v_l)$.
On every positive-volume overlap this bound supplies a point with
$v_l\geq-A$; submean in the next outer chart bounds its inner ball.
The finite connected overlap graph propagates a global uniform $L^1$
bound. Primary local compactness and finite extraction give a nontrivial
canonical $L^1$ limit $v$. Positivity passes to the limit and
$B_{\delta_l}\rightharpoonup\chi[\zeta=0]$.

On $\chi=1$ the positive closed local current $\ddc(v+\rho)$ dominates
the smooth divisor current and has geometric Lelong number at least one.
Smooth changes of $\rho$ do not change this number. Siu's theorem
\cite[III.8.5]{Dem} gives a proper analytic level set of dimension at most
two containing the divisor segment. This invokes only positive closed
local currents; Demailly's operator is twice ours, with the equivalent
potential-current level equal to two. Its lift contains an open part
of $H_0=\{w_0=z_0\}$. Since $H_0\cap\Omega$ is a projective plane
minus two points, the identity principle gives all of it. Deck invariance
gives $H_k=\{w_0=q^kz_0\}$. Near $[0:1:1:0]$, in the chart $z_1=1$,
these graphs are $z_0=q^{-k}w_0$. Every local defining holomorphic
function vanishes on all of them; for fixed $(w_0,w_1)$ near $(1,0)$,
their distinct values accumulate at zero. The one-variable identity
theorem makes the function vanish on the polydisk, contradicting properness.

Choose $\delta_j\downarrow0$ and smooth positive $\ddc$-closed $\Theta_j$
with $\int\omega\Theta_j=1$ and $J_j=\int B_{\delta_j}\Theta_j>j^4$.
The automorphisms
\[
 T_{a,b,\tau}[z_0:z_1:w_0:w_1]
 =[z_0:z_1+az_0:e^\tau w_0:e^\tau(w_1+bw_0)]
\]
commute with the deck group and translate $(x,y,\zeta)$ by $(a,b,\tau)$.
Average $T^*\Theta_j$ against
$3^{-4}p(a/3)p(b/3)(3\delta_j)^{-2}p(\tau/(3\delta_j))$
relative to $\sigma_a\sigma_b\sigma_\tau$, obtaining $\widehat\Theta_j$.
The parameter set is fixed compact, so $\int\omega\widehat\Theta_j\leq C_1$.
On $V_j=\{|x|,|y|<1/4,|\zeta|<\delta_j/4\}$, every translation to
the support of $B_{\delta_j}$ has $|a|,|b|\leq5/4$,
$|\tau|\leq5\delta_j/4$. The weights are bounded below by a fixed
constant times $\delta_j^{-2}$. The horizontal coefficient
$\widehat F_j$ of $\widehat\Theta_j$ therefore satisfies
$\widehat F_j\geq cJ_j$ on $V_j$.

Put $f_0(a,b)=p(4(a-1))p(b/2)$ and
$w_j(\tau)=4\delta_j^{-2}p(2\tau/\delta_j)$. Average the curves
\[
 [z_0:z_1]\longmapsto
 [z_0:z_1:e^\tau(z_0+uz_1):e^\tau(az_1+bz_0)]
\]
against $w_j(\tau)f_0(a,b)\varepsilon^{-2}p(u/\varepsilon)$,
relative to all four parameter $\sigma$ forms, $0<\varepsilon\leq1/16$.
On these supports $|a-bu|\geq5/8$, so the lines lie in $\Omega$,
and their deck translates are disjoint. Evaluation is a submersion:
variations in $u,a$ span the $w$ directions at $z_1\ne0$, and
variations in $\tau,b$ do so at $z_1=0$. The curve coordinate spans
the remaining direction. Fiber integration of the smooth supported
weights makes the average $T_{j,\varepsilon}$ globally smooth,
semipositive and closed. Compact parameter support bounds its
$\omega$ degree uniformly in $j,\varepsilon$.

At $u=0$, the local equations are $\zeta=\tau$, $y=ax+b$, giving
\[
 T_{j,0}=w_j(\zeta)\sigma_\zeta\wedge K_{f_0},\quad
 K_{f_0}=\int f_0(a,y-ax)\frac{i}{2\pi}
 (dy-a\,dx)\wedge(d\bar y-\bar a\,d\bar x)\,\sigma_a.
\]
On $|x|,|y|\leq1/4$ the weight is bounded below for $a$ in a fixed
disk about one. These covectors have no common nonzero annihilator,
so $K_{f_0}$ has a uniform positive lower bound. For general $u$,
solve $\tau=\zeta-\log(1+ux)$, $b=(1+ux)y-ax$. For each fixed $j$
the resulting coefficients and all their derivatives depend smoothly
on small $u$. Approximate-identity averaging proves local $C^\infty$
convergence to $T_{j,0}$ as $\varepsilon\downarrow0$. No uniform-in-$j$
convergence is asserted.

In the coframe $(x,y,\zeta)$ a positive $(2,2)$ form has cofactor
matrix $Q$, defined by $\xi\wedge\Theta=\operatorname{tr}(H_\xi Q)dV_0$,
$dV_0=\sigma_x\sigma_y\sigma_\zeta$. Its positive root obeys
\[
 Q=2\det(H)H^{-1},\quad H=\sqrt{\det(Q)/2}\,Q^{-1},\quad
 \Theta^{3/2}=\frac3{\sqrt2}\sqrt{\det Q}\,dV_0.
\]
Write $Q_{\widehat\Theta_j}=\left(\begin{smallmatrix}A_j&p_j\\p_j^*&\widehat F_j\end{smallmatrix}\right)$.
On $V_j$, $Q_{T_{j,0}}=\operatorname{diag}(B_j,0)$ with
$B_j\geq c\delta_j^{-2}I_2$. Positivity and the Schur complement give
\[
 \det(Q_{\widehat\Theta_j}+\operatorname{diag}(B_j,0))
 =\widehat F_j\det(B_j+A_j-p_jp_j^*/\widehat F_j)
 \geq\widehat F_j\det B_j.
\]
The root volume on $V_j$ is at least
$c\delta_j^{-2}\sqrt{J_j}\,dV_0$. The smaller region
$|x|,|y|<1/8$, $|\zeta|<\delta_j/8$ has volume comparable to
$\delta_j^2$. For this fixed $j$, choose $\varepsilon_j>0$ so that
local smooth convergence preserves half this root integral. Then
$\Gamma_j=\widehat\Theta_j+T_{j,\varepsilon_j}$ is smooth, positive,
$\ddc$-closed, has bounded $\omega$ degree and root volume
$R_j\geq c\sqrt{J_j}/2\to\infty$.

For any Hermitian $h_0\leq A\omega$, take $\eta_j^2=\Gamma_j$,
$P_j=\int h_0\eta_j^2\leq C$, and $\mu_j=\eta_j^3/R_j$.
General Hermitian smooth existence \cite[Corollary 1]{TW} gives
$h_j=h_0+\ddc v_j>0$, $h_j^3=c_j\mu_j$, $\sup v_j=0$.
The source scalar is not set to zero here. Smooth Stokes and matrix
AM--GM give
\[
 P_j=\int h_j\eta_j^2\geq c_j^{1/3}R_j^{2/3},\qquad
 0<\int h_j^3=c_j\leq P_j^3/R_j^2\longrightarrow0.
\]
These actual smooth potentials prove $v_-(h_0)=0$ for every $h_0$.

On a fiber $\zeta=s+i\tau$ has both periods $2\pi$ and $t=2s$ up to
a constant. Thus $dt\wedge\dc t=ds\wedge d\tau/\pi$ has fiber
area $4\pi$. Its square is zero and $(\alpha_0+\beta_0)^3=0$, whence
\[
 \int_{X_0}\omega^3
 =3\int(\alpha_0+\beta_0)^2\,\cdot4\pi=24\pi.
\]
Furthermore $\ddc t=\beta_0-\alpha_0$, so
$d\omega=-dt\wedge(\beta_0-\alpha_0)\ne0$.
Taking $h_0=\omega$, $Y=\mathbb P^2$ in Theorem~\ref{th:product}
gives the concrete fivefold and $b_H(f)=\binom53\,24\pi=240\pi$.

\begin{remark}
The sufficient geometric condition is the split background and displayed
density family. No positive lower mass, $L^p$ hypothesis, dual maximizer
or moment bound is assumed. We prove exactness by factor calculation,
rather than selecting a limit of exponential solutions. This does not
resolve arbitrary $L^1$ data at zero lower mass, uniqueness of the
unbounded solution, a greatest-member identity or literature priority.
The named factor is supplied prior work; only the product equation and
its exact constants are the candidate contribution.
\end{remark}
\begin{thebibliography}{9}
\bibitem{TW} V. Tosatti and B. Weinkove, \emph{The complex Monge--Amp\`ere
equation on compact Hermitian manifolds}, arXiv:0910.1390v2 (2009),
Corollary 1 and closed normalization, pp.~1--2;
\url{https://arxiv.org/pdf/0910.1390v2}.
\bibitem{Lamari} A. Lamari, \emph{Courants k\"ahl\'eriens et surfaces
compactes}, Ann. Inst. Fourier \textbf{49} (1999), 263--285,
Lemma 3.3 and proof, pp.~275--276;
\url{https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf}.
\bibitem{Dem} J.-P. Demailly, \emph{Complex Analytic and Differential
Geometry}, 21 June 2012, I.4.21 and I.5.8--5.9, pp.~36--40;
III.5.7--5.9, p.~159; III.8.5 and complete relevant proof, pp.~174--180;
\url{https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf}.
\end{thebibliography}
\end{document}


## Exact application and scope questions

Check both full notes independently, including canonical radial regularization, the exact q_alpha formula and full projective flux, finite actual product mass, explicit shift for the exact lambda, nonintegrability of the attenuation allowance, and the annular construction for every given smooth collapsing base sequence. Verify existence of each A_j and Z_j with the infinite quantifiers; all baseline derivative bounds, actual smooth projective g_j with positive endpoints and all infinity charts; exact full-product c_H(f_j)=C c_h0(F_j), smooth positivity and probability of each component; all original concentration inequalities and b_H(f)=0. Verify f is fixed independently of lambda, finite pointwise and positive, with its canonical subsolutions for every lambda>0. Use the greatest-solution implication only as explicitly supplied in the original task, retaining its exact finite mass. The explicit subsolutions have mass CV0, whereas the greatest solution masses are not identified with CV0. Necessarily unbounded solutions are new examples rather than the already known bounded obstruction.

The named X0 quotient and its actual smooth positive bounded-potential mass collapse are supplied prior work, reproduced completely above. The new application obtains smooth F_j from those actual potentials, not from an unsupported v_minus assertion. It uses none of the positive-threshold P07 product densities to answer zero-threshold S03. Reassess the imported exact compactness, positivity, volume24pi and mass-collapse dependency against its complete proof and fresh primary hypotheses (TW0910.1390v2 Corollary1, Lamari3.3, Demailly local compactness and SiuIII.8.5). No new arbitrary-L1 existence black box is permitted. Primary-source comparisons and every indispensable uncertainty require fresh exact evidence with valid nonnegative premise indices. No recursive certification of all cited foundations, priority or numerical correctness is requested. Synthetic finite numerical observations are auxiliary only; do not certify their execution or use them as proofs.


## Entire unchanged new statement-only reconstruction result

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "Dependency audit: retain the supplied threshold, greatest-solution principle, and P07 factor theorem; check smooth Hermitian existence at its primary source with the exact dd^c conversion. Prior factor-proof texts were not supplied.",
      "detailedSummary": "States the canonical and actual-product conventions, distinguishes supplied dependencies from new proofs, checks Tosatti–Weinkove Corollary 1 without a positive lower-mass hypothesis, and independently proves multiplicative-normalizer uniqueness. Records failed direct downloading and successful primary-source inspection. The named-factor theorem is retained as supplied; its unavailable earlier proofs were not fetched or compared.",
      "text": "This assignment is the restricted A–D reconstruction. Throughout, original_S03_completed=false. No necessity criterion, classification of all zero-threshold densities, or assertion for every previously chosen full-product concentration family is proved.\n\nWe use d^c=i(∂̄−∂)/(4π), hence dd^c=i∂∂̄/(2π). A genuine h-psh potential has its canonical upper representative, is locally psh plus smooth, satisfies h+dd^c u≥0, and is not identically −∞. Extended Monge–Ampère means the actual non-pluripolar measure obtained by restricting bounded truncations to {u>−T} and increasing T; poles receive no mass. Bounded products mean actual Bedford–Taylor products.\n\nThree assertions explicitly supplied by the task are dependencies, not newly proved:\n\n1. The smooth normalizer c_h(g) and individual threshold b_h(f) have the stated maximal scaled-subsolution interpretation. In particular, for smooth strictly positive g, any genuine w with MA_h^ext(w)≥a g dV has a≤c_h(g).\n2. A genuine exponential subsolution at the specified positive exponent gives a greatest genuine finite-mass exact solution by the supplied decreasing bounded-density approximation principle.\n3. The separately assessed prior P07 factor theorem gives the specified connected compact Hermitian threefold, V0=24π, and actual smooth v_l with h0+dd^c v_l>0 and δ_l=∫(h0+dd^c v_l)^3→0. Its geometry and normalization are retained exactly as supplied, not rediscovered.\n\nThe additional global existence theorem used is Tosatti–Weinkove, Corollary 1, page 1 of the [primary preprint](https://arxiv.org/pdf/0910.1390), with [journal publication](https://doi.org/10.1090/S0894-0347-2010-00673-X). Its compact Hermitian, dimension at least two, smooth real exponent hypotheses were checked in the primary PDF. For a smooth positive probability F relative to dV0=h0^m/V0, take the source exponent log(F/V0) and source potential a/(2π). Its equation becomes\n\n(h0+dd^c a)^m=c F dV0, with h0+dd^c a>0 and c>0.\n\nNo Kähler, balanced, or v_minus>0 hypothesis is required. We invoke this established existence conclusion; no new proof of its PDE estimates is claimed. In dimension one, integration gives c=V0 and the equation reduces to the zero-mean Poisson equation. An infinite sequence of these normalizers tending to zero therefore cannot occur in dimension one. The named application has m=3.\n\nMultiplicative-normalizer uniqueness is independently elementary. If two smooth positive equations with the same density have potentials a,b and coefficients c_a,c_b, at a maximum of a−b the complex Hessian inequality gives h+dd^c a≤h+dd^c b, hence c_a≤c_b. At a minimum it gives c_a≥c_b. Thus c_a=c_b. This identifies any explicitly constructed smooth positive equation with c_h(g). Potentials may be shifted to have supremum zero.\n\nThe previous P07 root proof and five factor-proof notes were not supplied in this fresh workspace. Their contents were not inspected, modified, or claimed to have been compared. The supplied theorem statement alone is the dependency used in D.\n\nArtifacts: input.json retains the task input; proofs/n1_dependencies.md records this dependency audit; sources/primary_source_audit.md records the primary theorem check. An initial web request used an unsupported argument and failed; the corrected search and primary PDF inspection succeeded. The command `curl -L --fail --max-time 30 https://arxiv.org/pdf/0910.1390 -o sources/tosatti_weinkove_0910.1390.pdf` failed with exit code 7 because the configured proxy on port 8080 was unreachable. No downloaded PDF is asserted. No prior article, discovery proof, campaign report, credentials, or resource-heavy computation was used.\n\nArtifacts: /workspace/research/native-workers/codex-JvDwPC",
      "support": []
    },
    {
      "id": "n2",
      "summary": "A: the canonical projective potential is genuinely admissible, has actual mass one and the stated radial tail, and satisfies q_α≥(1−α)^k. Its product mass is CV0; actual bounded lower-mass zero propagates to the product.",
      "detailedSummary": "Derives exact radial formulas for the slope, density, and mass. Proves canonical psh extension, positivity, smooth density extension across infinity, and the actual non-pluripolar product through truncation locality. Establishes the attenuation allowance's nonintegrability and propagates v_minus=0 using actual bounded Bedford–Taylor products.",
      "text": "Fix 0<α<1 and k≥1. On Z0≠0 put z_i=Z_i/Z0, r²=∑|z_i|², s=log r². With the prescribed convention, normalized Fubini–Study is κ=dd^c log(1+r²). Write\n\nv=r²/(1+r²)=exp(1−L), ψ=log v, L=1−ψ,\nu=1−L^α, a=αL^(α−1), b=α(1−α)L^(α−2).\n\nThe variable v is also the globally smooth function ∑_{i≥1}|Z_i|²/∑_{i≥0}|Z_i|². It is zero precisely at o and equals one on the infinity hyperplane. Set u(o)=−∞, its canonical pole value.\n\nAdmissibility and positivity. For χ(t)=1−(1−t)^α, χ'=a and χ''=b. Off o,\n\nκ+dd^c u=(1−a)κ+a(κ+dd^c ψ)+b dψ∧d^cψ.\n\nThe middle form is dd^c log r² on the affine chart, hence semipositive with tangential rank k−1. On any homogeneous-coordinate chart away from o it likewise has a local log-squared-norm potential and is semipositive. The last form is semipositive. Since a≤α<1, the whole form is ≥(1−α)κ and is smooth strictly positive off o.\n\nAt o, the local function P(s)=log(1+exp s)+u is genuinely psh. Its radial slopes are\n\np=P'(s)=v+a(1−v)>0,\nP''(s)=(1−a)v(1−v)+b(1−v)^2>0.\n\nThese give tangential and radial Hessian positivity. P tends to −∞ at the origin and is locally integrable, with negative growth of order (log(1/r))^α. On each complex line through the origin its convex increasing radial expression extends subharmonically with value −∞; the boundary flux is nonnegative and tends to zero since p→0. On other lines it is smooth subharmonic. The line criterion proves the canonical extension is psh. Thus u=P−log(1+r²) is genuinely κ-psh, without exceptional-set alterations. Its pullback is genuinely H=h0+κ-psh: locally, add a sufficiently large smooth quadratic function in the base variables to P to obtain a genuine psh representative; the remaining term is smooth and the block current is positive.\n\nExact density and normalization. For a radial P(log r²) on C^k\\{0}, the complex Hessian eigenvalues are p/r² in k−1 tangential directions and P''/r² radially. With normalized spherical measure dσ, its top Monge–Ampère measure is\n\nk p^(k−1)P''(s) ds dσ.\n\nThe constant follows from the exact dd^c: the Euclidean density is k!/π^k times the Hessian determinant, the sphere area is 2π^k/(k−1)!, and ds=2 dr/r. Applying this to log(1+r²), whose slope is v, gives ∫κ^k=[v^k]_0^1=1.\n\nSince dL/ds=−(1−v), define\n\nD=−dp/dL=(1−a)v+b(1−v)>0.\n\nThe positive radial density of κ^k with respect to dL dσ is k v^k. The Monge–Ampère radial density and its density relative to κ^k are therefore exactly\n\nW(L)=k p^(k−1)D,\nq_α=W/(k v^k)=(p/v)^(k−1)[(1−a)+b(1−v)/v].\n\nThese are smooth positive off o. At the infinity hyperplane v=1, L=1−log v is smooth and the expression extends smoothly, with q_α(1)=1−α. The form inequality already proved gives q_α≥(1−α)^k off o, hence almost everywhere. The density's value at the single pole is measure-irrelevant; +∞ may be assigned there.\n\nActual non-pluripolar mass. For u_T=max(u,−T), locality on {u>−T} gives\n\n(κ+dd^c u_T)^k=q_ακ^k.\n\nThe restricted measures in the non-pluripolar definition exhaust P^k\\{o} and put no mass at o. Consequently MA_κ^ext(u)=q_ακ^k and\n\n∫q_ακ^k=∫_1^∞W(L)dL=p(1)^k−p(∞)^k=1.\n\nThis uses actual truncation locality rather than Stokes for an unbounded potential. On the product the same truncation argument and the smooth block expansion off the polar fiber give\n\nMA_H^ext(u)=C h0^m∧q_ακ^k=CV0 q_α μ,\n∫MA_H^ext(u)=CV0.\n\nThere is zero mass on X0×{o}.\n\nTail and allowance. As L→∞, v=e^(1−L) is exponentially small, p/a→1, and D/b→1. For β=k(1−α)>0,\n\nW(L)~k α^k(1−α)L^(−1−β),\nq_α(L)~α^k(1−α)e^(k(L−1))L^(−1−β).\n\nFor every τ>0,\n\nlog(e^(τ(L^α−1))W(L))=τL^α−(1+β)log L+O(1)→+∞.\n\nThus e^(τ(L^α−1))W(L)→∞, and the allowance is not locally integrable near o:\n\n∫_{L>T}q_α e^(τ(L^α−1))κ^k=∫_T^∞e^(τ(L^α−1))W(L)dL=∞.\n\nActual bounded lower mass. If v_minus(h0)=0, choose bounded genuine h0-psh w_l with ∫(h0+dd^c w_l)^m→0. Their pullbacks are bounded genuine H-psh. For these actual bounded products,\n\n(H+dd^c w_l)^(m+k)=C(h0+dd^c w_l)^m∧κ^k.\n\nIndeed, locally write w_l as bounded psh plus smooth and approximate the psh part monotonically by smooth psh functions on smaller charts. The smooth block identity passes to Bedford–Taylor products; terms exceeding either factor's dimension vanish. Integrals are C times the base integrals and tend to zero. Positivity then proves v_minus(H)=0 in the actual bounded sense.\n\nThis proves A. Artifact: proofs/n2_projective_A.md. The additional exact algebra check is rerunnable with `python checks/verify.py`; its output is checks/output.json. Execution is not the proof of the analytic statements.\n\nArtifacts: /workspace/research/native-workers/codex-JvDwPC",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "B: explicit density domination gives a genuine subsolution at exactly λ with mass CV0. The stated local boundedness and logarithmic growth test works for every exponent. At zero threshold exact solutions have finite positive mass and are genuinely unbounded below.",
      "detailedSummary": "Proves the explicit shifted-potential inequality, the all-exponent essential-limsup criterion, and the fixed-exponent alternative. Uses the supplied principle only for passage to the greatest exact solution. Its mass is positive and finite, without identifying it with the subsolution mass. These are sufficient tests, not necessity assertions.",
      "text": "Retain n2's notation and actual projective measure. For any smooth positive probability dV on the product, R=μ/dV is smooth positive and bounded above and below. Put F=f/R. Then f dV=F μ exactly. Assume f is nonzero, nonnegative, and L1(dV).\n\nFixed-exponent test. If, for λ>0 and finite A>0,\n\nF≤A q_α exp(λ(L^α−1))\n\nalmost everywhere off the polar fiber, define\n\ns_λ=u+λ^(−1)log(CV0/A).\n\nThis constant shift is a genuine unbounded H-psh potential and has the same actual non-pluripolar measure as u. At exactly the specified exponent,\n\nexp(λs_λ)F=(CV0/A)exp(λu)F≤CV0 q_α.\n\nMultiplication by μ proves MA_H^ext(s_λ)≥exp(λs_λ)f dV globally. On the polar fiber the left measure has no mass and the exponential is zero. The subsolution mass is exactly CV0.\n\nThe supplied subsolution-to-greatest-solution principle yields a greatest genuine finite-mass exact solution U_λ at the same exponent. Its mass is also directly positive and finite: a nontrivial genuine quasi-psh function on a connected compact manifold has finite supremum and a Lebesgue-null pole set. Therefore\n\n0<∫MA_H^ext(U_λ)=∫exp(λU_λ)f dV≤exp(λ sup U_λ)∫f dV<∞.\n\nNo equality with CV0 is asserted.\n\nAll-exponent test. Interpret the essential limsup uniformly in the base and projective directions: for every ε>0, some T satisfies\n\nlog^+(F(x,y)/q_α(y))≤ε L(y)^α\n\nfor almost all (x,y) with L(y)>T. This is the stated essential-limsup condition, equivalently expressed using essential suprema over x and projective spheres. Assume this and local essential boundedness off the polar fiber. Fix λ>0 and take ε=λ/2. Near the pole, F/q_α≤exp((λ/2)L^α); its ratio to exp(λ(L^α−1)) is bounded, for example by exp(λ). On the remaining compact region L≤T, a finite subcover converts local essential boundedness into a single finite bound. Since q_α≥(1−α)^k and exp(λ(L^α−1))≥1, that region also has a finite domination constant. Combining the regions gives A_λ<∞ in the explicit fixed-exponent test.\n\nThus one fixed f satisfying this test admits the explicit subsolutions and greatest finite positive mass exact solutions for every λ>0. Only the shift and resulting solution depend on λ.\n\nFixed-exponent alternative. The q_α asymptotic in n2 supplies c_*>0 and T with\n\nq_α(L)≥c_* exp(k(L−1))L^(−1−k(1−α))\n\nfor L≥T. Hence the stated uniform essential bound\n\nF≤A' exp(k(L−1)+λL^α)L^(−1−k(1−α))\n\nimplies F≤(A'/c_*)exp(λ)q_α exp(λ(L^α−1)) there. Local essential boundedness elsewhere completes the global bound as above. The resulting equation retains exactly λ.\n\nZero-threshold unboundedness. If an exponential subsolution or exact solution had a finite lower bound B, then exp(λw)≥a=exp(λB)>0, producing MA_H^ext(w)≥a f dV. This contradicts b_H(f)=0 by the supplied threshold characterization. Compact quasi-psh functions are bounded above, so the forced unboundedness is below. An almost-everywhere lower bound also passes everywhere for the canonical upper representative by upper semicontinuity and density of the full-measure set. Thus null-set modifications cannot account for the unboundedness.\n\nThese are explicit sufficient density tests. No necessity or unrestricted classification is claimed. Artifact: proofs/n3_density_B.md. The full deliverable is regenerated by `python build_deliverable.py`. Dependencies are n1's supplied principles and n2's proved actual measure and asymptotics.\n\nArtifacts: /workspace/research/native-workers/codex-JvDwPC",
      "support": [
        "n1",
        "n2"
      ]
    },
    {
      "id": "n4",
      "summary": "C: for every admissible base sequence there exist smooth projective factors yielding a finite-everywhere zero-threshold concentration density that works for every λ. Actual component equations give c_H(f_j)=C c_h0(F_j). This does not cover every prechosen full-product family.",
      "detailedSummary": "Constructs disjoint q_α-weighted annular bumps with positive constant backgrounds and proved normalizers. An explicit radial cumulative equation produces actual global smooth projective solutions. Product equations identify normalizers; the series is a positive L1 probability, finite everywhere and smooth off the polar fiber. Its uniform logarithmic growth meets B for every exponent, while the supplied threshold property proves b_H(f)=0.",
      "text": "Quantifier: for every sequence of smooth strictly positive probabilities F_j relative to dV0=h0^m/V0 with c_h0(F_j)≤2^(−2j)/C, suitable projective probabilities g_j exist. No assertion concerns every already chosen full-product family. Fix one α∈(0,1), independently of λ, and put β=k(1−α)>0.\n\nThe primary-checked smooth theorem in n1 gives actual base equations\n\n(h0+dd^c a_j)^m=c_j F_j dV0,\nh0+dd^c a_j>0,\nc_j=c_h0(F_j)≤2^(−2j)/C.\n\nChoose C^r norms from a smooth background connection and set\n\nD_j=max(1,max_{0≤r≤j}||F_j||_{C^r}),\nε_j=1/[2(1+D_j)],\nB0(x)=∑_{j≥1}2^(−j)ε_j F_j(x).\n\nFor each fixed r, terms with j≥r have C^r norm at most 2^(−j)/2. Thus B0 converges in every C^r norm, is smooth positive, and is ≤1/2.\n\nChoose the explicit smooth cutoff χ(t)=exp(−1/[(t−1)(2−t)]) for 1<t<2 and zero elsewhere. It is nonnegative and ≤1. For L≥2, n2's exact formula gives p≥a and 1−v≥1/2, hence\n\nW(L)≥(k/2)α^k(1−α)L^(−1−β).\n\nDefine\n\nd=(k/2)α^k(1−α)∫_1^2χ(t)t^(−1−β)dt>0,\nZ(T)=∫_1^∞χ(L/T)W(L)dL.\n\nFor T≥2, Z(T)≥d T^(−β)>0, and Z(T) is finite because W has integral one.\n\nSet M_j=max(1,||F_j||_∞). Inductively choose T_j as a power of two with T_1≥4, T_j≥4T_(j−1), and\n\nlog(1+2^(−j)M_j T_j^β/d)≤T_j^α/j.       (*)\n\nThe least admissible power of two may be used. It exists because the left side grows as O(log T) for each fixed j, while T^α/j grows faster.\n\nLet Z_j=Z(T_j), and define\n\nρ_j(y)=χ(L(y)/T_j)q_α(y)/Z_j,\ng_j(y)=ε_j+(1−ε_j)ρ_j(y).\n\nExtend ρ_j by zero outside T_j<L<2T_j. Its support is separated from both o and the infinity hyperplane; flatness of χ makes it globally smooth. Its integral against κ^k is exactly one. Consequently g_j is a smooth strictly positive probability and is constant ε_j near both endpoints. The annular supports are disjoint and escape to o.\n\nActual global projective equations. Each g_j is a smooth radial function of v∈[0,1]. Define\n\nI_j(v)=k∫_0^v g_j(t)t^(k−1)dt,\np_j(v)=I_j(v)^(1/k),\nφ_j(v)=∫_0^v [p_j(t)−t]/[t(1−t)]dt.\n\nNear v=0, g_j=ε_j gives I_j=ε_j v^k and p_j=ε_j^(1/k)v. The integrand is then (ε_j^(1/k)−1)/(1−t), smooth at zero. Near v=1, exact probability normalization gives\n\nI_j(v)=1−ε_j(1−v^k).\n\nIts positive kth root is smooth, p_j(1)=1, and p_j(v)−v is smoothly divisible by 1−v. Thus φ_j is smooth up to both endpoints. Composition with the global smooth variable v gives a globally smooth projective potential.\n\nThe s-slope of log(1+r²)+φ_j(v(s)) is p_j. Differentiating p_j^k=I_j gives\n\ndp_j/dv=g_j(v)(v/p_j)^(k−1)>0,\ndp_j/ds=g_j(v)(v/p_j)^(k−1)v(1−v)>0.\n\nThe exact radial determinant formula therefore proves\n\n(κ+dd^c φ_j)^k=g_j κ^k.\n\nStrict positivity also holds at the endpoints: at o all eigenvalue ratios relative to κ tend to ε_j^(1/k); at infinity the tangential ratios p_j/v tend to one and the normal ratio (dp_j/ds)/(dv/ds) tends to ε_j. The equation is thus an actual global smooth positive equation, with normalizer c_κ(g_j)=1.\n\nActual product equations. For any smooth positive probability dV, put R=μ/dV, f_j=R F_j g_j, and U_j=a_j(x)+φ_j(y). Each f_j is a smooth strictly positive probability. Block expansion gives the actual global equation\n\n(H+dd^c U_j)^N\n=C(h0+dd^c a_j)^m∧(κ+dd^c φ_j)^k\n=C c_j F_j g_j μ\n=C c_j f_j dV.\n\nNormalizer uniqueness from n1 identifies\n\nc_H(f_j)=C c_h0(F_j)≤2^(−2j).\n\nThis uses actual equations rather than probability normalization alone. The smooth bounded U_j have masses C c_j→0, so v_minus(H)=0. The base equations likewise imply v_minus(h0)=0 whenever an infinite sequence in C's hypotheses exists.\n\nNow define the actual pointwise series f=∑2^(−j)f_j and F=f/R. Its exact representation is\n\nF(x,y)=B0(x)+∑2^(−j)(1−ε_j)F_j(x)ρ_j(y).\n\nAt y=o all annular terms vanish, giving F(x,o)=B0(x)<∞. Away from o at most one annular term is nonzero. On compact subsets off the polar fiber only finitely many supports occur. Thus f is finite everywhere and smooth off X0×{o}. Tonelli and the exact component probabilities give ∫f dV=∑2^(−j)=1. Pointwise,\n\nf≥(1/2)f_1≥(1/2)min_X f_1>0.\n\nZero threshold. If a>0 and a genuine w satisfied MA_H^ext(w)≥a f dV, then for every j it would satisfy MA_H^ext(w)≥a2^(−j)f_j dV. The supplied smooth threshold interpretation and proved product normalizers give\n\na2^(−j)≤c_H(f_j)≤2^(−2j).\n\nThus a≤2^(−j) for all j, a contradiction. The supplied characterization yields b_H(f)=0. This rules out positive scaled subsolutions among genuine unbounded potentials as well.\n\nAll-exponent density criterion. Set K=(1/2)/(1−α)^k. Outside all annuli, F/q_α≤K. On the jth annulus, χ≤1 and Z_j≥d T_j^(−β) give\n\nF/q_α≤K+2^(−j)M_j T_j^β/d.\n\nFor T_j≤L≤2T_j, using (*) and K+B≤(K+1)(1+B),\n\nlog^+(F/q_α)/L^α≤log(K+1)/T_j^α+1/j→0.\n\nOn gaps the bound log^+K/L^α tends to zero. These bounds are uniform in x and projective spheres. Local essential boundedness off the fiber follows from smoothness. Therefore exactly B's all-exponent criterion holds.\n\nThis single f was chosen independently of λ. For every λ>0 it admits the genuine pole-bearing subsolution u+λ^(−1)log(CV0/A_λ), of actual mass CV0, and the supplied principle gives a greatest genuine finite positive mass exact solution. All exact solutions are necessarily unbounded below because b_H(f)=0.\n\nThis proves C with its stated quantifier. Artifact: proofs/n4_concentration_C.md contains the exact cutoff normalizers and global component-potential formulas. The ODE algebra is rerunnable with `python checks/verify.py`. No artificial base sequence or finite numerical simulation is used to establish the infinite construction.\n\nArtifacts: /workspace/research/native-workers/codex-JvDwPC",
      "support": [
        "n1",
        "n2",
        "n3"
      ]
    },
    {
      "id": "n5",
      "summary": "D: normalize the retained P07 theorem's actual collapsing smooth volume forms into a base sequence. This gives fourfold and fivefold zero-threshold all-exponent examples. The explicit subsolution masses are 96π and 240π; exact solution masses are only proved finite and positive.",
      "detailedSummary": "Selects δ_(l_j)≤2^(−2j)/10 and defines actual smooth base probabilities whose normalizers equal δ_(l_j). The same base sequence meets C for k=1 and k=2. Derives the compact product examples and all-exponent subsolutions, then finite positive mass and genuine unboundedness of exact solutions using the supplied principle. The prior factor theorem is a retained dependency, not a new proof.",
      "text": "The retained supplied P07 theorem gives\n\nX0={ [z:w]∈P^3 : z,w∈C^2 nonzero }/<[z:w]↦[z:exp(2π)w]>,\n\nwith the stated h0=α0+β0+dt∧d^c t, t=log(||w||²/||z||²), V0=24π, and actual smooth v_l with h0+dd^c v_l>0 and δ_l=∫(h0+dd^c v_l)^3→0. Its compactness, connectedness, positivity, normalization, and collapsing sequence are used solely as the supplied factor theorem. They are not newly reconstructed.\n\nActual base sequence. Choose increasing indices l_j with δ_(l_j)≤2^(−2j)/10, possible since δ_l→0. Define\n\nF_j=(24π/δ_(l_j))[(h0+dd^c v_(l_j))^3/h0^3].\n\nThis is a smooth strictly positive function. For dV0=h0^3/(24π),\n\nF_j dV0=(h0+dd^c v_(l_j))^3/δ_(l_j),\n\nso it is a probability and satisfies the actual equation\n\n(h0+dd^c v_(l_j))^3=δ_(l_j)F_j dV0.\n\nNormalizer uniqueness proves c_h0(F_j)=δ_(l_j). No additional existence theorem is needed for these base equations. The same sequence meets C for k=1 and k=2, whose binomial constants are respectively 4 and 10. The supplied smooth potentials are individually bounded and have masses tending to zero, proving actual v_minus(h0)=0.\n\nFourfold. For k=1, N=4 and C=4. The product X0×P^1 is connected compact and H=h0+κ is smooth Hermitian. It has actual bounded v_minus(H)=0 by A. Apply C to construct projective g_j^(1). For any smooth positive probability dV^(1), let R^(1)=μ^(1)/dV^(1), f_j^(1)=R^(1)F_j g_j^(1), and f^(1)=∑2^(−j)f_j^(1). All original concentration requirements hold, including finite pointwise values, smoothness off the polar fiber, a positive global lower bound, and b_H(f^(1))=0. For every λ>0, B gives\n\ns_λ^(1)=1−L^α+λ^(−1)log(96π/A_λ^(1)),\n\nwith actual non-pluripolar mass 4·24π=96π.\n\nFivefold. For k=2, N=5 and C=10. The same construction yields projective g_j^(2) and a concentration density f^(2) on the connected compact X0×P^2, relative to any smooth positive probability reference volume. It has v_minus(H)=0, b_H(f^(2))=0, and all the concentration and all-exponent density properties. Its explicit subsolutions are\n\ns_λ^(2)=1−L^α+λ^(−1)log(240π/A_λ^(2)),\n\nwith actual mass 10·24π=240π. One fixed α∈(0,1) suffices. The projective factors and densities depend on k, while neither density depends on λ.\n\nExact solutions. For each k∈{1,2} and λ>0, the supplied principle gives a greatest genuine finite-mass exact solution U_λ^(k). Its nontrivial genuine quasi-psh representative has volume-null poles and finite supremum, while f^(k) is a nonzero L1 probability. Therefore\n\n0<∫MA_H^ext(U_λ^(k))\n=∫exp(λU_λ^(k))f^(k)dV^(k)\n≤exp(λ sup U_λ^(k))<∞.\n\nAny exact solution bounded below would give a positive scaled subsolution, contradicting b_H(f^(k))=0. Thus every exact solution is genuinely unbounded below. The numbers 96π and 240π are only the explicit subsolution masses. Neither is identified as a greatest-exact-solution mass, and no Hermitian mass comparison is inferred from potential ordering.\n\nThis proves the new application in D using the retained factor statement and n2–n4. It does not replace the separately assessed factor proof or compare the five unavailable earlier factor-proof texts. Artifact: proofs/n5_named_application_D.md. Exact binomial arithmetic is rerunnable with `python checks/verify.py`.\n\nArtifacts: /workspace/research/native-workers/codex-JvDwPC",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4"
      ]
    },
    {
      "id": "n6",
      "summary": "Complete scoped A–D reconstruction with explicit dependencies and exact symbolic evidence; original_S03_completed=false. Retrieval failures and unavailable prior-proof comparisons are recorded. candidate=true concerns the restricted assignment only.",
      "detailedSummary": "Confirms all four limited targets with the explicitly retained supplied statements and primary-checked standard smooth existence theorem. Records executed symbolic checks, environment details, artifacts, and rerun commands. Does not assert necessity, unrestricted classification, arbitrary-family solvability, exact-solution mass constants, or comparison of unavailable earlier factor proofs. These remain unverified mathematical drafts.",
      "text": "The independently reconstructed new arguments n2–n5 prove all four restricted targets A–D under the exact conventions and explicitly declared dependencies in n1. A proves canonical projective admissibility, actual non-pluripolar mass and tail, and actual bounded lower-mass propagation. B proves the explicit sufficient density tests at the exact exponent, including the all-exponent test for a single density. C constructs suitable projective factors for every admissible base sequence and proves actual global component equations and normalizers. D normalizes the retained P07 theorem's actual collapsing forms and derives the fourfold and fivefold applications, including finite positive mass and genuine unboundedness of exact solutions.\n\nThe completed task is the scoped A–D implementation assignment. original_S03_completed=false. Necessity, unrestricted S03 classification, arbitrary previously chosen full-product-family solvability, exact greatest-solution mass values, and comparison of unprovided prior factor-proof texts are unasserted. The retained factor theorem, threshold characterization, and greatest-solution principle are dependencies rather than newly claimed results.\n\nExecuted evidence: `python checks/verify.py` passed with Python 3.12.14 and SymPy 1.14.0 on Linux x86_64, platform string Linux-6.18.44-x86_64-with-glibc2.41. It checked exact symbolic identities for −dp/dL, the radial component-equation density, and the tail exponent, and recorded 96*pi and 240*pi as the explicit subsolution masses. These are algebra checks only, not numerical examples, PDE solutions, exhaustive finite results, or analytic certification of the infinite construction. The admissibility, locality, integrability, endpoint smoothness, and series convergence arguments are supplied in the ordinary notes themselves. These are unverified mathematical drafts; execution success does not establish mathematical correctness.\n\nFailures and limitations: an unsupported initial web argument returned an error; correcting it allowed primary-source search and PDF inspection. A direct curl download failed with exit code 7 because the configured proxy was unreachable. The primary-source and convention audit is retained. The prior root proof and five earlier factor-proof notes were absent from the fresh supplied workspace and were not fetched from other reports or campaigns. No resource-heavy computation was required or launched.\n\nArtifacts in /workspace/research/native-workers/codex-JvDwPC: input.json; proofs/n1_dependencies.md through proofs/n6_completion_and_evidence.md; sources/primary_source_audit.md; checks/verify.py; checks/output.json; checks/commands.md; build_deliverable.py; deliverable.json; status.json; and README.md. From that directory rerun `python checks/verify.py` followed by `python build_deliverable.py`. The latter rebuilds all full notes with summaries and support declarations. The manifest and scope check confirmed six nonempty full notes and original_S03_completed=false. status.json records restricted_A_D_completed=true.\n\nThe last-note claim is complete resolution of the exact restricted A–D assignment, using the explicitly authorized supplied statements and the primary-checked standard smooth Hermitian existence theorem. candidate=true applies to this restricted assignment and does not claim completion of original S03.\n\nArtifacts: /workspace/research/native-workers/codex-JvDwPC",
      "support": [
        "n1",
        "n2",
        "n3",
        "n4",
        "n5"
      ]
    }
  ],
  "candidate": true,
  "workspace": "/workspace/research/native-workers/codex-JvDwPC"
}

## Entire unchanged prior independent factor reconstruction

These five earlier ordinary notes independently establish the retained prior factor theorem. The new A--D worker was given that prior theorem as a statement, not its proof. Its application must be assessed afresh alongside this complete earlier chain, rather than described as a new reconstruction of the old factor.

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "The actual quotient is a compact connected smooth complex threefold and an elliptic bundle over P1×P1. The descending Hermitian form satisfies dω≠0, d(ω²)=0, and ∫ω³=24π. Primary evidence for the allowed foundations was checked.",
      "detailedSummary": "Constructs the quotient using the free properly discontinuous action and explicit bundle transition functions. Proves compactness, positivity, genuine nonclosedness, and the exact volume. Supplies the normalized strictly positive closed test ω²/(24π). Records the precise permitted foundation applications without claiming recursive certification of their cited dependencies.",
      "text": "This is an ordinary unverified proof draft for the named-factor dependency. The separately allowed foundations are the only imported non-elementary theorems. Original unrestricted P07 remains unresolved.\n\nWrite α=α0 and β=β0. The map π:Ω→P1×P1 sends [z:w] to ([z],[w]). On the base chart z_i w_j≠0, choose representatives with z_i=1 and put c=w_j/z_i∈C*. This gives π^{-1}(U_ij)≅U_ij×C*. On overlaps,\nc_{i'j'}=c_{ij}(w_{j'}/w_j)/(z_{i'}/z_i).\nThese are actual holomorphic transition maps. The action of g is c↦qc, so quotient bundle charts are U_ij×(C*/q^Z). Their logarithmic fibre coordinate belongs to E=C/(2πZ+2πiZ). Logarithms of transition functions give translations in E independent of the chosen logarithm. On U_00 the coordinates are exactly x=z1/z0, y=w1/w0, ζ=log(w0/z0).\n\nThe action is free: [z:q^m w]=[z:w], with z,w≠0, forces the projective scalar to be 1 and then q^m=1. It is properly discontinuous because t(g^m P)=t(P)+4πm: compact subsets of Ω have bounded t and meet only finitely many translates. Small open sets with disjoint translates give quotient manifold charts. Thus X0 is a smooth complex threefold. Ω is connected as the image of (C²∖{0})×(C²∖{0}), hence X0 is connected. Every quotient point has a representative z=Z, w=e^{t/2}W with Z,W∈S³ and 0≤t≤4π. The image of this compact parameter set covers X0, proving compactness.\n\nOn U_00,\nt=ζ+barζ+log(1+|y|²)−log(1+|x|²),\nα=dd^c log(1+|x|²)=σ_x/(1+|x|²)²,\nβ=dd^c log(1+|y|²)=σ_y/(1+|y|²)².\nPolar integration gives ∫P1α=∫P1β=1. Put s=α+β, F=β−α and ρ=dt∧d^c t. Then dd^c t=F and ρ=(i/(2π))∂t∧bar∂t≥0. Although t is not a real-valued function on X0, its derivatives are invariant under g. Therefore ω=s+ρ descends. The horizontal part is positive in the two base directions, and ∂t has nonzero vertical component dζ, making ω strictly positive.\n\nSince dρ=−dt∧F, dω=−dt∧F≠0: evaluate on a vertical real direction with dt≠0 and an α-horizontal complex line. Moreover α²=β²=ρ²=0 and sF=0, so d(ω²)=−2s∧dt∧F=0. Direct differentiation gives dd^cρ=−F²=2αβ.\n\nOn a fibre write ζ=a+ib. Then dt=2da, d^c t=db/(2π), and ρ=da∧db/π=σ_ζ. Both a and b have period 2π, hence ∫Eρ=4π. Since ω³=6αβρ, fibre integration gives ∫X0ω³=24π. Consequently Θ*=ω²/(24π) is a globally smooth strictly positive CLOSED (2,2) form with ∫ωΘ*=1.\n\nThe exact foundation applications were checked at public primary sources. Tosatti–Weinkove, arXiv0910.1390v2, Corollary 1, printed p.1, supplies smooth Hermitian MA existence up to a scalar: https://arxiv.org/pdf/0910.1390v2 . In n5 it applies to connected compact X0 of dimension 3, arbitrary smooth Hermitian h, and smooth positive volume η_j³. Its source potential is multiplied by 2π; no degeneration estimate is imported.\n\nLamari, AIF49(1999), Lemma 3.3, printed pp.275–276, supplies the criterion for a smooth (1,1) form without assuming closedness, using every smooth positive dd^c-closed test: https://www.numdam.org/article/AIF_1999__49_1_263_0.pdf . In n2 it is applied to ω−κBδ. Positive rescaling of the source operator leaves the test kernel and distributional potential range unchanged. Proposition 1.3 is unnecessary because Θ* explicitly proves nonemptiness.\n\nDemailly, Complex Analytic and Differential Geometry, 21 June 2012, I.5.8–5.9, printed p.40, supplies canonical psh representatives and local L1 compactness. III.8.5, printed p.174, supplies analytic geometric Lelong upperlevel sets for positive CLOSED currents of bidimension (p,p): https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf . In n2 global normalized compactness is reconstructed, and Siu is applied only to locally closed positive corrections with p=2, never directly to ω+dd^c u.\n\nArtifacts: input.json preserves the input. Source requests and page checks are in sources/web_requests.json; retrieved outputs are in sources/web_find_output.json, sources/web_passages_output.json and sources/web_extra_output.json. Local PDF downloads failed with “Operation not permitted”; public primary text was retrieved through the web connector. Retry downloads with python sources/retrieve_sources.py. Run python artifacts/check_identities.py in /workspace/research/native-workers/codex-toln5o. artifacts/check_output.json reports exact checks ω³=6αβρ, sF=0, −F²=2αβ, fibre volume 4π and total volume 24π. Environment: Python 3.12.14, SymPy 1.14.0, Linux 6.18.44 x86_64. No resource-heavy computation was run. Successful execution is diagnostic evidence, not mathematical verification.\n\nArtifacts: /workspace/research/native-workers/codex-toln5o",
      "support": []
    },
    {
      "id": "n2",
      "summary": "Proves I against the entire normalized smooth positive dd^c-closed test family: Cδ is finite and tends to infinity for every allowed p and χ0. Includes genuine normalized compactness and the explicit divisor-accumulation contradiction.",
      "detailedSummary": "A bounded subsequence of Cδ would, by Lamari, produce canonical ω-psh potentials whose corrected currents dominate a fixed multiple of Bδ. A submean propagation argument supplies global L1 compactness. Closed positive local corrections allow Siu's theorem, producing an analytic set containing ζ=0 locally. Its lift must contain every hyperplane w0=q^m z0. A power-series argument at [0:1:0:1] forces interior, contradicting dimension at most 2. No pairing estimate is inferred from local compactness alone.",
      "text": "Use the quotient geometry from n1. The prescribed Bδ is globally smooth after extension by zero: the base cutoffs are compactly supported, and the smooth density p vanishes with all derivatives at its support boundary. Its ζ-support lies in an injective logarithmic neighbourhood. It is semipositive. On a fixed compact neighbourhood of these supports, σ_ζ≤Kω, so\n0≤Bδ≤K||p||∞δ^{-2}ω.\nEvery normalized positive test therefore satisfies ∫BδΘ≤K||p||∞δ^{-2}. Thus Cδ is finite. Its test family is nonempty by Θ* from n1.\n\nWe first reconstruct the compactness needed below. On a connected compact complex manifold, genuine quasi-psh functions u_j with dd^c u_j≥−h for fixed smooth Hermitian h and sup u_j=0 have an L1-convergent subsequence. Choose finitely many relatively compact connected coordinate balls, with smaller cores covering the manifold. On each choose a bounded quadratic correction ρ with dd^cρ≥h. Then u_j+ρ is genuine psh. Subtracting a fixed upper bound for ρ gives a nonpositive subharmonic function w_j.\n\nThe maxima of u_j are attained. Pass to a subsequence whose maximum points converge to p. In a chart about p, w_j at those points has a uniform lower bound. Submean on fixed-radius balls centred there bounds ∫(−w_j); a fixed smaller ball about p lies in these balls for all sufficiently large j. This supplies an initial uniform L1 bound.\n\nTo propagate it, in a connected coordinate domain let S be the points having neighbourhoods with uniformly bounded ∫(−w_j). S is open. If x is in its relative closure, choose B(x,4r) inside the domain and a fixed ball A⊂S∩B(x,r/4). The bound on A supplies points a_j∈A with w_j(a_j)≥−M for one fixed finite M. Submean on B(a_j,r) bounds its integral of −w_j. Since B(x,r/2)⊂B(a_j,r), x∈S. Thus S is relatively closed and equals the connected coordinate domain. Finite coverings then bound every compact subset. Across overlapping charts, bounded corrections and bounded coordinate Jacobians on a smaller overlap transfer these bounds. The intersection graph of a connected finite coordinate cover is connected, so they propagate across the cover. The smaller cores give a global L1 bound. The permitted local psh compactness theorem, followed by finite diagonal extraction, gives local and global L1 convergence. Limits patch as distributions, and uniqueness of canonical psh representatives after smooth correction makes the limit genuine. This proves the required global normalized compactness.\n\nSuppose δ_j→0 and C_{δ_j}≤M. Put κ=1/(M+1). For EVERY smooth strictly positive dd^c-closed test Θ, normalization by ∫ωΘ gives\n∫(ω−κB_{δ_j})Θ≥(1−κM)∫ωΘ>0.\nLamari's permitted nonclosed-form criterion yields real distributions u_j with\nω+dd^c u_j≥κB_{δ_j}.\nLocal quadratic corrections and the permitted representative theorem make these genuine quasi-psh functions. Subtract their finite suprema. Since dd^c u_j≥−ω, the compactness proof applies. Pass to u_j→u in L1.\n\nThe ordinary approximate-identity calculation in ζ gives\nB_{δ_j}→χ0(x)χ0(y)[D_U],\nwhere D_U={ζ=0} in the product chart; its normalization is ∫pσ_ζ=1. The base cutoffs permit extension by zero. Distributional limits preserve positivity, hence\nT=ω+dd^c u≥κχ0(x)χ0(y)[D_U].\nNear |x|,|y|<1/2 and ζ=0 this implies T≥κ[D_U].\n\nOn each coordinate ball choose ρ=M|z|² with dd^cρ≥ω. The current R=dd^c(u+ρ) is CLOSED and positive and dominates κ[D_U] near that local divisor. Its geometric Lelong number there is at least κ. In the geometric normalization a regular integration-current point has number 1: for a flat complex two-plane, the integral of (σ1+σ2)² over a radius-r ball is r^4. On overlaps the corrected currents differ by a smooth form, whose ball integral is O(r^6) and whose geometric Lelong contribution after division by r^4 is zero. Thus their numbers define one intrinsic function ν_u. Siu applies locally to these closed positive currents of bidimension (2,2). Consequently A={ν_u≥κ/2} is a global closed analytic subset of dimension at most 2 containing the indicated open part of D_U. No Siu theorem for a nonclosed current has been used.\n\nLift A through the quotient covering to an analytic subset Ã⊂Ω. The hypersurface D0={w0=z0}∩Ω is connected: it is P2 with the two points where z=0 or w=0 removed. Since Ã∩D0 is analytic in that connected surface and contains a nonempty open subset, the identity principle gives D0⊂Ã. Quotient invariance gives Dm={w0=q^m z0}∩Ω⊂Ã for every integer m.\n\nAt P=[0:1:0:1]∈Ω use a=z0/z1, b=w0/z1 and r=w1/z1 near (0,0,1). Each Dm is b=q^m a. A local holomorphic defining function F of Ã has expansion F(a,b,r)=Σf_ij(r)a^i b^j. Vanishing on Dm gives, for every degree k and integer m,\nΣ_{i+j=k}f_ij(r)q^{mj}=0.\nFor each r this is a polynomial in q^m with infinitely many distinct roots. All its coefficients vanish. Every f_ij is therefore identically zero. Every local defining function vanishes identically, so Ã has interior near P, contradicting dimension at most 2.\n\nA bounded subsequence of Cδ as δ→0 is impossible; hence Cδ→∞. This proves all of I for every prescribed p and χ0, including finiteness against all tests and the complete concentration implication. No quantitative lower divergence rate is claimed.\n\nThe draft is retained in artifacts/factor_notes.json and artifacts/factor_proof.txt. Rerun auxiliary normalization checks with python artifacts/check_identities.py. The compactness and analytic arguments above are mathematical proofs in an unverified draft; symbolic execution does not verify them.\n\nArtifacts: /workspace/research/native-workers/codex-toln5o",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "Proves II by averaging actual globally embedded rational curves over explicit compact matrix parameters. Tδ,ε are globally smooth semipositive CLOSED forms with uniform ω degree and the required fixed-δ smooth local rank-two limit.",
      "detailedSummary": "Uses curves [Z0:Z1]↦[Z0:Z1:e^s(Z0+eZ1):e^s(bZ0+aZ1)], with a near ±1 and e tending to zero. Global submersivity proves smooth fibre integration without an imported regularization theorem. An explicit parameter change yields the coefficient matrix and C∞ convergence on compact subsets for fixed δ. Symmetric slopes and positive densities give B≥cδ^{-2}I2 on Vδ.",
      "text": "Use n1. Let k_R(v) be the smooth probability density relative to σ_v proportional to exp(−1/(1−|v|²/R²)) for |v|<R, zero elsewhere. Then k_R(v)=R^{-2}k_1(v/R). Choose\nr(a)=½k_{1/16}(a−1)+½k_{1/16}(a+1),  k(b)=k_1(b).\nThe density r is symmetric under a↦−a and supported where 7/8≤|a|≤9/8. Reuse any allowed p from I and put pδ(s)=δ^{-2}p(s/δ). Set ε0=1/64, rε=ε0ε/(1+ε)>0 and lε(e)=k_{rε}(e).\n\nFor parameters in these supports set M=[[1,e],[b,a]] and define the actual holomorphic curve\nF_{a,b,e,s}([Z0:Z1])=[Z0:Z1:e^s(Z0+eZ1):e^s(bZ0+aZ1)]\nfollowed by quotienting to X0. Its determinant a−eb has modulus at least 7/8−1/64>0. Thus neither z nor w vanishes, and the map lands in Ω. The first base projection is the identity of P1, so the quotient curve is embedded.\n\nDefine T_{δ,ε} by\n∫ξ∧T_{δ,ε}=∫r(a)k(b)pδ(s)lε(e)(∫P1F_{a,b,e,s}^*ξ)σ_aσ_bσ_sσ_e.\nAll parameter densities are probabilities. Integration over curves proves reality and positivity as a current. Stokes on each compact curve proves dT_{δ,ε}=0.\n\nThis current is an ACTUAL globally smooth form. On an open neighbourhood of the compact parameter supports, the incidence map F:P1×parameters→X0 is a holomorphic submersion. At fixed Z, parameter variations span the two complex w-directions: if Z1≠0, variations of e and a do so; if Z1=0, variations of s and b do so. Variation of Z gives the remaining z-base direction. This proves rank 3 everywhere, including infinity and w0=0. The current is the pushforward of the smooth parameter (4,4) form on a complex five-dimensional domain. Submersion coordinates express it as integration of smooth coefficients over the remaining coordinates. A finite partition of unity on the compact support permits differentiation under each integral. It is therefore a globally smooth (2,2) form. Positivity as a smooth current implies pointwise semipositivity. No regularization theorem is assumed.\n\nAll matrices M lie in one compact subset of GL2(C), and |s|≤1/100. The maps from P1 times this compact parameter set to X0 have uniformly bounded pullbacks of ω, hence ∫P1F^*ω≤D. More explicitly, the two base contributions are 1+1, while\nt∘F=2Re(s)+log(||MZ||²/||Z||²)\nhas uniformly bounded differential for this compact matrix family. Probability averaging gives ∫ωT_{δ,ε}≤D uniformly in δ and ε.\n\nFix a compact subset of U_00=C_x×C_y×E_ζ. For sufficiently small ε, 1+ex is uniformly near 1 and has a holomorphic logarithm there. Along a curve,\ny=(b+ax)/(1+ex),  ζ=s+log(1+ex) modulo the lattice.\nThe inverse parameter change is b=(1+ex)y−ax and s=ζ−log(1+ex), with real Jacobian |1+ex|². Let Pδ be the smooth periodic extension of pδ to E. In the specified trace convention,\nQ_{δ,ε}=∫r(a)lε(e)k((1+ex)y−ax)Pδ(ζ−log(1+ex))|1+ex|²vv*σ_aσ_e,\nwhere v=(1,(a−ey)/(1+ex),e/(1+ex))^T. Represent H_ξ so that the tangent pullback is (v*H_ξv)σ_x; this fixes the coefficient transpose convention.\n\nFor fixed δ, lε is an approximate identity at e=0. The remaining integrand and every derivative in x,y,ζ are uniformly smooth on the fixed compact set. Thus Q_{δ,ε} converges in C∞ to\nQ_{δ,0}=Pδ(ζ)∫r(a)k(y−ax)(1,a,0)^T(1,a,0)*σ_a.\nPeriodicity makes the formulas compatible across logarithmic representatives. They define a locally smooth semipositive T_{δ,0} on the whole product chart. No global extension or convergence uniform in δ is claimed.\n\nOn Vδ, |y−ax|≤17/32. Set k*=min_{|b|≤17/32}k(b)>0 and p*=min_{|s|≤1/4}p(s)>0. Symmetry gives\n∫r(a)(1,a)^T(1,a)*σ_a=diag(1,∫|a|²r(a)σ_a)≥(7/8)²I2.\nTherefore Q_{δ,0}=diag(B,0) on Vδ, with B≥p*k*(7/8)²δ^{-2}I2. This is the requested bound with c independent of δ, and proves every assertion of II.\n\nThe construction is retained in artifacts/factor_proof.txt and artifacts/factor_notes.json. Run python artifacts/check_identities.py. Exact auxiliary outputs include det M=a−eb, tangent components (a−ey)/(1+ex) and e/(1+ex), and the parameter Jacobian. These finite checks do not independently verify the global analytic construction.\n\nArtifacts: /workspace/research/native-workers/codex-toln5o",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n4",
      "summary": "Proves III by globally averaging witnesses from I and adding the actual closed forms from II. Proves the unique positive square root and obtains diverging root volumes with uniformly bounded ω degree.",
      "detailedSummary": "Global affine automorphisms spread each witness's vertical coefficient across Vδ while preserving positivity, dd^c closedness, and uniform degree control. The horizontal block from II supplies a determinant lower bound. Fixed-δ smooth convergence selects actual ε>0 forms. The proof uses all-test divergence only to select witnesses and asserts no restricted-family variational identity.",
      "text": "Use n2 and n3. Put μ=σ_xσ_yσ_ζ. First prove the root assertion. If η has positive Hermitian tangent matrix H, diagonalization and exterior multiplication give Q_{η²}=2det(H)H^{-1} and det Q=8(det H)². Conversely every positive definite Q has the unique positive definite root H=sqrt(det Q/2)Q^{-1}. Hence η³=(3/sqrt(2))sqrt(det Q)μ. These formulas are coordinate invariant, and local roots patch by uniqueness. They are smooth whenever Γ is smooth and strictly positive.\n\nDefine a global holomorphic automorphism of X0 by\nA_{a,b,s}[z0:z1:w0:w1]=[z0:z1+az0:e^s w0:e^s(w1+bw0)].\nIt preserves Ω, commutes with g and has a holomorphic inverse. On U_00 it is exactly (x,y,ζ)↦(x+a,y+b,ζ+s). For a normalized strictly positive dd^c-closed Θ define\nSδΘ=∫k_2(a)k_2(b)δ^{-2}k_2(s/δ)A_{a,b,s}^*Θ σ_aσ_bσ_s.\nThis is globally smooth, strictly positive and dd^c-closed. Parameters and inverses lie in one compact automorphism family, so (A^{-1})^*ω≤Kω uniformly. Changing variables gives ∫ωSδΘ≤K∫ωΘ=K.\n\nLet q33 be the ζζ coefficient of Θ, which is nonnegative. Put Kδ={|x|,|y|<1, |ζ|<δ} and Aδ(Θ)=∫BδΘ. Then\nAδ(Θ)≤||p||∞δ^{-2}∫Kδq33μ.\nFor any point of Vδ, its translation differences to every point of Kδ satisfy |a|,|b|<5/4 and |s|<5δ/4. The averaging kernel there is at least k0δ^{-2} for a fixed k0>0. Translation derivatives are the identity, so\nq33(SδΘ)≥k0δ^{-2}∫Kδq33μ≥(k0/||p||∞)Aδ(Θ)\non all of Vδ. This proves an actual trace-concentration estimate.\n\nChoose δ_j=2^{-j}/1000. By n2, C_{δ_j}→∞. Select normalized actual smooth strictly positive dd^c-closed witnesses Θ_j with A_j=∫B_{δ_j}Θ_j≥C_{δ_j}/2 for sufficiently large j. Existence follows from the supremum definition; no maximum is assumed. Let S_j be the matrix of S_{δ_j}Θ_j.\n\nFor fixed j the local limit supplied by n3 has horizontal block B≥cδ_j^{-2}I2. Thus the matrix of the local limit of S_{δ_j}Θ_j+T_{δ_j,ε} dominates S_j+d_j diag(1,1,0), where d_j=cδ_j^{-2}. For positive definite S,\ndet(S+d diag(1,1,0))=det S+d(cof11 S+cof22 S)+d²S33≥d²S33.\nThe principal minors are nonnegative. Determinant is monotone on positive definite matrices, as is seen by conjugating with the inverse square root of the smaller matrix. Consequently the limit root-volume density on V_{δ_j} is at least\n(3/sqrt(2))cδ_j^{-2}sqrt((k0/||p||∞)A_j)μ.\n\nDisk integration gives μ(Vδ)=δ²/4096, so this local limit root volume is at least Lsqrt(A_j) for fixed L>0. Convergence from n3 is smooth on the compact closure of V_{δ_j}, and S_{δ_j}Θ_j is strictly positive there. Choose an actual ε_j>0 small enough that the smooth sum's root-volume integral is at least half that limit. Set Γ_j=S_{δ_j}Θ_j+T_{δ_j,ε_j}. These are globally smooth, strictly positive and dd^c-closed, with ∫ωΓ_j≤K+D and ∫Γ_j^{3/2}≥(L/2)sqrt(A_j)→∞. Their unique smooth positive roots satisfy Γ_j=η_j². This proves III with actual global forms using only fixed-δ convergence.\n\nThe proof is retained in artifacts/factor_proof.txt and artifacts/factor_notes.json. Run python artifacts/check_identities.py for the root formulas, determinant identity and μ(Vδ)=δ²/4096. These are finite algebra checks. No full variational identity over a selected test family is used.\n\nArtifacts: /workspace/research/native-workers/codex-toln5o",
      "support": [
        "n1",
        "n2",
        "n3"
      ]
    },
    {
      "id": "n5",
      "summary": "Completes IV and the named-factor dependency: every smooth Hermitian h on X0 admits genuine sup-normalized smooth strictly positive collapsing potentials, so v_-(h)=0. Original unrestricted P07 closure remains false.",
      "detailedSummary": "Smooth Hermitian MA existence with the roots from III gives (h+dd^c u_j)³=c_jη_j³. Smooth Stokes and matrix AM–GM prove ∫(h+dd^c u_j)³≤(∫hΓ_j)³/(∫η_j³)². The numerator is bounded for every fixed arbitrary h and the denominator diverges. This proves all named targets relative to the expressly permitted foundations, without solving the original positive-threshold L1 equation.",
      "text": "Let h be ANY smooth strictly positive Hermitian form on X0. Use Γ_j=η_j² from n4 and set V_j=∫η_j³→∞ and D_j=∫hΓ_j. Compactness gives h≤L_hω for a finite L_h, so 0<D_j≤L_h(K+D) uniformly. No restriction on the metric class is imposed.\n\nApply the permitted Tosatti–Weinkove smooth existence theorem to X0, h and F_j=log(η_j³/h³). The volume ratio is smooth and strictly positive. The exact hypotheses hold by n1: connected compact smooth X0 has complex dimension 3≥2 and h is Hermitian. The theorem gives smooth source potentials φ_j with sup φ_j=0 and scalars b_j satisfying\n(h+i∂bar∂φ_j)³=e^{b_j}η_j³,  h+i∂bar∂φ_j>0.\nSet u_j=2πφ_j and c_j=e^{b_j}. Then sup u_j=0 and h_j=h+dd^c u_j>0 satisfies h_j³=c_jη_j³. Existence is the only imported conclusion; the degeneration estimate follows next.\n\nSmooth Stokes gives ∫dd^c u_jΓ_j=∫u_jdd^cΓ_j=0. Explicitly, integration of d(d^c u_j∧Γ_j) gives ∫dd^c u_jΓ_j=∫d^c u_jdΓ_j. Integration of d^c(u_jdΓ_j), using d^c d=−dd^c, gives the second equality. Therefore D_j=∫h_jη_j² without assuming h or η_j closed.\n\nAt a point diagonalize h_j relative to η_j, with positive eigenvalues λ1,λ2,λ3. Their product is c_j, and\nh_j∧η_j²=((λ1+λ2+λ3)/3)η_j³≥c_j^{1/3}η_j³\nby AM–GM. Integration yields D_j≥c_j^{1/3}V_j. Thus\n∫X0(h+dd^c u_j)³=c_jV_j≤D_j³/V_j²→0.\nThis proves the needed inequality directly from smooth Stokes and matrix algebra. No global mass-extrema theorem or restricted-family variational equality is used.\n\nEach u_j is smooth on compact X0, hence bounded, canonical and genuinely h-psh. Each corrected form is strictly positive and has a smooth finite positive Monge–Ampère measure. The specified extended product agrees with the ordinary smooth product here. Since masses of positive bounded h-psh potentials are nonnegative, this sequence proves v_-(h)=0. These are actual smooth strictly positive forms, not formal current limits or t-only tests.\n\nTogether n1–n4 prove the quotient geometry and EVERY proposed statement I–III; this note proves IV for EVERY smooth Hermitian h. The complete named-factor theorem is therefore proved in this ordinary unverified draft relative only to the expressly allowed foundations. No false named target or unresolved indispensable premise remains in this reconstruction. Selection of test witnesses and MA solutions is nonconstructive but supplies actual smooth objects. Recursive certification of the allowed foundations' cited dependencies is not claimed.\n\nScope: factor_dependency_complete=true; original_unrestricted_P07_closure=false. No density f, unrestricted exact positive-threshold L1 equation, limiting finite-mass solution, or P07 singularity/envelope classification is claimed. This factor theorem alone supplies neither a P07 counterexample nor unrestricted exactness. No priority or product-article acceptance is asserted.\n\nArtifacts: artifacts/factor_notes.json and artifacts/factor_proof.txt retain the proof; artifacts/scope.json records scope; artifacts/artifact_manifest.json records retained files. Inputs, commands, source outputs and environment details remain in /workspace/research/native-workers/codex-toln5o. Run python artifacts/check_identities.py. All lightweight exact symbolic checks passed under Python 3.12.14 and SymPy 1.14.0. Execution success does not establish mathematical correctness.\n\nArtifacts: /workspace/research/native-workers/codex-toln5o",
      "support": [
        "n1",
        "n4"
      ]
    }
  ],
  "candidate": true,
  "workspace": "/workspace/research/native-workers/codex-toln5o"
}

## Entire current article

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\dc}{d^c}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\PP}{\mathbb P}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Exponential equations at zero individual threshold\newline
for a constructed concentration family}
\author{}\date{}
\begin{document}\maketitle
\noindent\textbf{Working draft.} Complete independent review,
statement-only reconstruction and final comparison are pending.
The general classification in S03 remains unresolved here.
\begin{abstract}
We construct a strictly positive integrable probability density on a
compact Hermitian product whose individual Monge--Amp\`ere threshold
is zero, but whose exponential equation has a genuine unbounded
subsolution for every positive exponent. The density is a rigorously
chosen member of the specified concentration family and is independent
of the exponent. An explicit radial density-growth criterion supplies
the subsolutions, with exactly computed finite mass. The supplied
subsolution principle then gives greatest finite-mass exact solutions,
which are necessarily unbounded. A prior elliptic threefold supplies
the required smooth mass collapse and concrete examples in dimensions
four and five. No assertion is made for every concentration-family
choice or for necessity of the sufficient criterion.
\end{abstract}

\section{Conventions, background and product geometry}
Use $\ddc=i\partial\bar\partial/(2\pi)$ and
$\dc=i(\bar\partial-\partial)/(4\pi)$, with ordinary wedge powers.
All quasi-psh potentials have their genuine canonical representatives.
Extended measures are non-pluripolar products with smooth-background
corrections. For a positive Hermitian form $h$ and reference probability
$dV$, let $c_h(g)$ be the unique scalar of the normalized
bounded-density equation, and set
\[
 b_h(f)=\lim_{j\to\infty}c_h(\min(f,j)),\qquad
 v_-(h)=\inf_{v\in\PSH(X,h)\cap L^\infty}\int_X\MA_h(v).
\]
For nonzero nonnegative bounded data, existence of a continuous
potential and uniqueness of this scalar follow from
\cite[Theorem 0.1]{KN} and \cite[Corollary 0.2]{Ng}.
Their $\ddc$ is twice ours, so their potentials are multiplied by two;
the smooth positive reference-volume ratio is absorbed into the density.
Neither theorem is applied to the final unbounded $L^1$ density.
We use the supplied maximal-subsolution characterization of $b_h$.
In particular, $\MA_h^{\rm ext}(v)\geq af\,dV$ implies $a\leq b_h(f)$,
and bounded data satisfy $b_h=c_h$.

We also use exactly the supplied S03 principle: a genuine exponential
subsolution $s$ with
$\MA_h^{\rm ext}(s)\geq e^{\lambda s}f\,dV$, $\lambda>0$, gives a
greatest genuine exact solution by decreasing bounded-density
approximation. This principle is background; we prove the required
subsolutions and their zero-threshold nonvacuity below.

Let $(X_0,h_0)$ be connected compact Hermitian of dimension $m$,
and put $Y=\PP^k$, $k\geq1$, with normalized Fubini--Study form
$\kappa$, $\int_Y\kappa^k=1$. On $X=X_0\times Y$ write
\[
 N=m+k,\quad C=\binom Nm,\quad V_0=\int_{X_0}h_0^m,
 \quad H=h_0+\kappa,
 \quad\mu=\frac{h_0^m}{V_0}\wedge\kappa^k.
\]
For any smooth positive probability $dV$ on $X$, put $R=\mu/dV$.
It is smooth with positive upper and lower bounds. Factor forms and
functions are pulled back when appropriate. Write $F=f/R$, so that
$f\,dV=F\mu$.

\section{A finite-mass radial barrier}
Fix $0<\alpha<1$ and $o=[1:0:\cdots:0]$. Put
\[
 \psi=\log\frac{\sum_{i=1}^k|Z_i|^2}{\sum_{i=0}^k|Z_i|^2},
 \qquad L=1-\psi,\qquad u=1-L^\alpha,
\]
with the canonical value $u(o)=-\infty$. For $1\leq L<\infty$ set
\begin{align*}
 t&=e^{1-L},& a&=\alpha L^{\alpha-1},\\
 Q&=t+(1-t)a,&
 D&=t(1-a)+(1-t)\alpha(1-\alpha)L^{\alpha-2},\\
 q_\alpha&=Q^{k-1}D e^{k(L-1)},&
 W&=kQ^{k-1}D.
\end{align*}
Here $q_\alpha$ is a density function on $Y\setminus\{o\}$;
its extension over $Z_0=0$ has value $1-\alpha$.

\begin{lemma}\label{lem:barrier}
The potential $u$ is genuine $\kappa$-psh and
\[
 \MA_\kappa^{\rm ext}(u)=q_\alpha\kappa^k,\qquad
 \int_Yq_\alpha\kappa^k=1,\qquad q_\alpha\geq(1-\alpha)^k.
\]
Its product pullback has actual extended mass $CV_0$. Moreover,
as $L\to\infty$,
\[
 W(L)\sim k\alpha^k(1-\alpha)L^{-1-k(1-\alpha)},\qquad
 e^{\tau(L^\alpha-1)}W(L)\longrightarrow\infty\quad(\tau>0).
\]
\end{lemma}
\begin{proof}
For $0<\varepsilon\leq1$ replace $\psi$ by the smooth function
\[
 \psi_\varepsilon=
 \log\frac{\sum_{i=1}^k|Z_i|^2+\varepsilon|Z_0|^2}
               {\sum_{i=0}^k|Z_i|^2}.
\]
It is nonpositive and $\kappa$-psh. For
$\chi(s)=1-(1-s)^\alpha$ one has $0<\chi'\leq\alpha$ and
$\chi''>0$, so
\[
 \kappa+\ddc\chi(\psi_\varepsilon)
 =(1-\chi')\kappa+\chi'(\kappa+\ddc\psi_\varepsilon)
   +\chi''d\psi_\varepsilon\wedge\dc\psi_\varepsilon
 \geq(1-\alpha)\kappa.
\]
These functions decrease to $u$. Its growth
$O(1+|\log r|^\alpha)$, $r=\sum_{i=1}^k|z_i|^2$ near $o$,
is locally integrable. Thus the decreasing psh-plus-smooth limit is
nontrivial and canonical, with its stated pole.

In the affine chart $Z_0=1$, $L=1-\log(r/(1+r))$ and a local
primitive of $\kappa+\ddc u$ is
\[
 \Phi(r)=\log(1+r)+1-[1-\log(r/(1+r))]^\alpha,
 \qquad r\Phi'=Q.
\]
The tangential and radial Hessian eigenvalues are $Q/r$ and $Q'$.
Polar integration, with its constant fixed by normalized
Fubini--Study mass, gives
\[
 \int_{a<r<b}(\ddc\Phi)^k=Q(b)^k-Q(a)^k.
\]
Since $-dQ/dL=D$, the radial mass density is $W(L)dL$.
The Fubini--Study radial probability is $ke^{-k(L-1)}dL$;
division gives exactly the displayed $q_\alpha$.
The flux limits are $Q(0)=0$, $Q(\infty)=1$ in the $r$ coordinate.
The function is smooth along the infinity hyperplane. On every
finite superlevel, its truncation agrees locally with smooth $u$;
the defining non-pluripolar exhaustion omits its pole and cutoff
masses. Hence the actual mass is one. The lower form bound proves
the density bound. Factor dimensions give the same finite-level
identity on the product, followed by the actual non-pluripolar limit:
\[
 \MA_H^{\rm ext}(u)=C h_0^m\wedge q_\alpha\kappa^k=CV_0q_\alpha\mu.
\]
Finally $Q\sim\alpha L^{\alpha-1}$ and
$D\sim\alpha(1-\alpha)L^{\alpha-2}$ give the asymptotic for $W$.
The logarithm of the last expression in the lemma is
$\tau L^\alpha-[1+k(1-\alpha)]\log L+O(1)$, tending to infinity.
\end{proof}

For $\tau>0$ write $B_\tau=q_\alpha e^{\tau(L^\alpha-1)}$.
In particular $B_\tau\geq b_0=(1-\alpha)^k$.
Its mass on every punctured pole neighborhood is infinite, even
though $q_\alpha\kappa^k$ has mass one.

\begin{theorem}\label{th:criterion}
Let $f\geq0$ be nonzero and integrable, and fix $\lambda>0$.
If, for some finite $A>0$,
\[
 F(x,y)\leq A B_\lambda(y)\quad\text{almost everywhere},
\]
then the genuine function
\[
 s_\lambda=u+\lambda^{-1}\log(CV_0/A)
\]
is an exponential subsolution with actual mass $CV_0$ and exact
coefficient $\lambda$. The supplied principle gives a greatest exact
solution. The same holds for every $\lambda>0$ if $F$ is locally
essentially bounded off $X_0\times\{o\}$ and
\[
 \mathop{\rm ess\,limsup}_{y\to o}\mathop{\rm ess\,sup}_{x}
    \frac{\log^+(F(x,y)/q_\alpha(y))}{L(y)^\alpha}=0.
\]
\end{theorem}
\begin{proof}
The exact product measure in Lemma~\ref{lem:barrier} gives
\[
 e^{\lambda s_\lambda}f\,dV
 \leq(CV_0/A)e^{\lambda u}Aq_\alpha e^{-\lambda u}\mu
 =\MA_H^{\rm ext}(s_\lambda).
\]
Both measures give zero mass to the polar fiber, and adding the
constant changes neither admissibility nor mass. For the second
claim, the limit condition bounds $F/q_\alpha$ by
$e^{(\lambda/2)L^\alpha}$ near $o$. The remaining compact region
has bounded ratio, so increasing a finite $A$ gives the first claim.
The greatest solution has finite mass because it is bounded above
on compact $X$ and $f$ is integrable.
\end{proof}

The first criterion can also be checked from the explicit growth bound
\[
 F\leq A'e^{k(L-1)+\lambda L^\alpha}L^{-1-k(1-\alpha)}
\]
for all sufficiently large $L$, uniformly essentially in $x$ and
the projective spheres, with local essential boundedness elsewhere.

\section{A zero-threshold concentration family for every exponent}
Assume that $X_0$ has smooth positive probability densities $F_j$
relative to $dV_0=h_0^m/V_0$ satisfying
\begin{equation}\label{eq:base}
 c_{h_0}(F_j)\leq 2^{-2j}/C.
\end{equation}
\begin{theorem}\label{th:construction}
For every sequence satisfying \eqref{eq:base}, one can choose smooth
strictly positive probability densities $g_j$ on $Y$ such that
\[
 f_j=RF_jg_j,\qquad f=\sum_{j\geq1}2^{-j}f_j
\]
are the specified full-product concentration family:
$c_H(f_j)\leq2^{-2j}$, $\int_Xf\,dV=1$, and $b_H(f)=0$.
The density $f$ is finite everywhere, smooth off the polar fiber and
bounded below by $\tfrac12\min_Xf_1>0$. This single $f$, independent
of $\lambda$, has genuine exponential subsolutions and greatest
finite-mass exact solutions for every $\lambda>0$. Every exact
solution is unbounded.
\end{theorem}
\begin{proof}
Put $w_j=2^{-j}$ and $M_j=\max F_j$. Choose
$0<\varepsilon_j\leq1/2$ so that
\[
 w_j\varepsilon_jM_j\leq b_0 2^{-j-2},\qquad
 w_j\varepsilon_j\|F_j\|_{C^j}\leq2^{-j},
\]
using increasing fixed smooth coordinate seminorms. Then
$E(x)=\sum_jw_j\varepsilon_jF_j(x)$ converges smoothly and
$0<E\leq b_0/4$.

Choose a smooth $0\leq\rho\leq1$ supported in $[0,1]$, positive
inside and flat at the endpoints. Inductively choose
$A_j\geq2$, $A_j>A_{j-1}+2$, with
\[
 Z_j=\int_{A_j}^{A_j+1}\rho(L-A_j)e^{(L^\alpha-1)/j}W(L)\,dL
      \geq2w_jM_j.
\]
For each fixed $j$ the integrand apart from $\rho$ tends to infinity
uniformly on intervals $[A,A+1]$ by Lemma~\ref{lem:barrier}.
Thus the choice is possible with arbitrarily large $A_j$.
Set, on that annulus and zero elsewhere,
\[
 b_j=\rho(L-A_j)B_{1/j}/Z_j,\qquad
 g_j=\varepsilon_j+(1-\varepsilon_j)b_j.
\]
Flatness makes $b_j$ smooth globally, vanishing near both $o$ and
the infinity hyperplane. Its integral is one. The $g_j$ are smooth
strictly positive probabilities and their disjoint annuli satisfy
\begin{equation}\label{eq:bump}
 w_jM_j(1-\varepsilon_j)b_j\leq B_{1/j}/2.
\end{equation}

We check the component scalar directly. For a radial $g=g_j$, put
\[
 G(r)=\int_{|z|^2<r}g\kappa^k,\quad Q_g=G^{1/k},\quad
 \phi'(r)=\frac{Q_g-r/(1+r)}r.
\]
The tangential and radial eigenvalues of the local primitive are
$Q_g/r>0$ and $Q_g'>0$, and the flux identity gives
$(\kappa+\ddc\phi)^k=g\kappa^k$. At small $r$, the bump is absent:
$G=\varepsilon_j(r/(1+r))^k$ and
$\phi=(\varepsilon_j^{1/k}-1)\log(1+r)+\mathrm{constant}$.
At large $r$,
\[
 G=1-\varepsilon_j+\varepsilon_j(r/(1+r))^k.
\]
In $v=1/r$, $Q_g$ is analytic near zero with value one and
$d\phi/dv=-(Q_g-1/(1+v))/v$ is analytic there. Since
$v=|Z_0|^2/\sum_{i\geq1}|Z_i|^2$ is smooth near $Z_0=0$,
$\phi$ extends smoothly. The metric is strictly positive there,
with tangential part $\kappa$ and transverse coefficient
$\varepsilon_j>0$; at $o$ it is $\varepsilon_j^{1/k}\kappa$.
This includes $k=1$.

Let $v_j$ solve the bounded base equation above with scalar
$c_{h_0}(F_j)$. The genuine bounded product potential
$U_j=v_j+\phi_j$ has
\[
 \MA_H(U_j)=C\MA_{h_0}(v_j)\wedge g_j\kappa^k
          =C c_{h_0}(F_j)f_j\,dV.
\]
The local bounded-product expansion, including smooth-background
corrections, has only this term by factor dimensions. Scalar
uniqueness and \eqref{eq:base} therefore give
$c_H(f_j)=C c_{h_0}(F_j)\leq2^{-2j}$.

Tonelli gives $\int f=\sum_jw_j=1$. Off the polar fiber, only finitely
many annuli meet any compact set, so
$F=E+\sum_jw_j(1-\varepsilon_j)F_jb_j$ is smooth. On the fiber
the actual pointwise sum equals the finite $E$.
Also $f\geq w_1f_1$, proving the positive lower bound.
If $a>0$ were an admissible subsolution coefficient for $f$, then
for every $j$ maximality would give
\[
 aw_j\leq b_H(f_j)=c_H(f_j)\leq2^{-2j},
 \qquad a\leq2^{-j},
\]
which is impossible. Thus $b_H(f)=0$.

Fix $\lambda>0$ and choose $J$ with $1/j\leq\lambda$ for $j\geq J$.
Since $u\leq0$, $B_{1/j}\leq B_\lambda$ for these indices.
Disjointness and \eqref{eq:bump} bound their total contribution
pointwise by $B_\lambda/2$. The baseline is at most $B_\lambda/4$.
The finitely many remaining bumps have finite constant
\[
 K_\lambda=\max_Y\sum_{j<J}w_j(1-\varepsilon_j)M_jb_j,
 \qquad D_\lambda=3/4+K_\lambda/b_0.
\]
Hence $F\leq D_\lambda B_\lambda$.
Theorem~\ref{th:criterion} gives the explicit subsolution
$s_\lambda=u+\lambda^{-1}\log(CV_0/D_\lambda)$ and a greatest
exact solution. The subsolution mass is $CV_0$; no such numerical
mass is asserted for the greatest solution. Its exact mass is finite
and positive, since its supremum is finite, $f\in L^1$ is strictly
positive, and a genuine nontrivial quasi-psh function is finite
almost everywhere. A bounded exponential subsolution would give
a positive constant coefficient for $f$, contradicting $b_H(f)=0$.
Every exact solution is therefore unbounded.
\end{proof}

The construction also satisfies the second criterion of
Theorem~\ref{th:criterion}: on the $j$th annulus,
$F/q_\alpha\leq1/4+\tfrac12 e^{(L^\alpha-1)/j}$, and elsewhere the
ratio is at most $1/4$. As the pole is approached through annuli,
$j\to\infty$, giving the stated uniform logarithmic limit.

\section{Concrete zero-lower-mass examples and scope}
The prior supplied factor in \cite[Appendix]{Product} is
\[
 X_0=\{[z:w]\in\PP^3:z,w\in\mathbb C^2\setminus\{0\}\}
       /\langle[z:w]\mapsto[z:e^{2\pi}w]\rangle,
 \quad h_0=\alpha_0+\beta_0+dt\wedge\dc t,
\]
where $t=\log(\|w\|^2/\|z\|^2)$ and the two base forms are
normalized. Its complete prior proof establishes compactness,
positivity, $V_0=24\pi$ and actual smooth $v_\ell$ with
$h_0+\ddc v_\ell>0$ and
$\delta_\ell=\int(h_0+\ddc v_\ell)^3\to0$.
Choose a subsequence with $\delta_{\ell_j}\leq2^{-2j}/C$ and put
\[
 F_j=\frac{(h_0+\ddc v_{\ell_j})^3/dV_0}{\delta_{\ell_j}}.
\]
These are smooth positive probabilities, and their actual equations
give $c_{h_0}(F_j)=\delta_{\ell_j}$ by scalar uniqueness.
Thus Theorem~\ref{th:construction} has a concrete instance.
For bounded base potentials $v$, the same local product expansion gives
$\int_X\MA_H(v)=C\int_{X_0}\MA_{h_0}(v)$, proving $v_-(H)=0$.
With $k=1$ this is a compact fourfold and the explicit subsolutions
have mass $96\pi$; with $k=2$ the mass is $240\pi$.
These are masses of the constructed subsolutions, not of the greatest
exact solutions.

\begin{remark}
The quantifier is every base sequence satisfying \eqref{eq:base},
with projective components chosen by the displayed construction.
It does not cover every previously chosen full-product concentration
family. The fixed $f$ solves the zero-threshold solvability problem
for this choice and every exponent. Necessity, arbitrary Hermitian
geometries and a nonsolvable zero-threshold example remain unproved.
No literature priority or discovery of the prior factor is claimed.
\end{remark}
\begin{thebibliography}{9}
\bibitem{KN} S. Ko\l odziej and N. C. Nguyen,
\emph{Weak solutions to the complex Monge--Amp\`ere equation on
Hermitian manifolds}, \href{https://arxiv.org/abs/1312.5491v2}{arXiv:1312.5491v2}, Theorem 0.1.
\bibitem{Ng} N. C. Nguyen,
\emph{The complex Monge--Amp\`ere type equation on compact Hermitian
manifolds and applications},
\href{https://arxiv.org/abs/1501.00891v1}{arXiv:1501.00891v1}, Corollary 0.2.
\bibitem{Product} \emph{Exact equations for $L^1$ densities on products
with zero lower mass}, checked standalone source (2026), Appendix;
\href{https://github.com/MingchenXia/non-kahler-pluripotential-theory/blob/7a244bc4938c5b918f7d906c7201f9385e4188f4/research/papers/P07-zero-lower-mass-product-equations.tex}{immutable source and complete prior factor proof}.
\end{thebibliography}
\end{document}


## Exact scoped targets

# Independent statements: exponential solvability at zero threshold

Keep the exact original S03 task, its canonical conventions, actual
non-pluripolar products, concentration quantifiers and supplied
subsolution-to-greatest-solution principle. The following are scoped
targets. Neither unrestricted classification nor arbitrary choices of
the concentration family are asserted. No new author proof is supplied.

Let (X0,h0) be connected compact Hermitian, dim m, V0=int h0^m.
Let Y=P^k, k>=1, with normalized Fubini-Study kappa, int kappa^k=1.
Put N=m+k, C=binomial(N,m), H=h0+kappa,
mu=(h0^m/V0) wedge kappa^k, and R=mu/dV for ANY smooth positive
probability dV on the product. Use the original exact dd^c. Pullbacks
are understood, and F=f/R denotes density relative to mu.

A. For every 0<alpha<1 put o=[1:0:...:0],
psi=log(sum_{i>=1}|Zi|^2/sum_{i>=0}|Zi|^2), L=1-psi,
and u=1-L^alpha with its canonical pole value. Write
MA_kappa^ext(u)=q_alpha kappa^k. Establish genuine admissibility,
smooth positivity off o, smooth extension of the density across the
infinity hyperplane, integral q_alpha=1, q_alpha>=(1-alpha)^k,
and exact finite product mass CV0. The radial density W(L) of
q_alpha kappa^k satisfies
W(L)~k alpha^k(1-alpha)L^(-1-k(1-alpha)), hence
exp(tau(L^alpha-1))W(L)->infinity for every tau>0. The attenuation
allowance q_alpha exp(tau(L^alpha-1)) is not integrable near o.
If v_minus(h0)=0, then v_minus(H)=0 in the actual bounded sense.

B. For fixed lambda>0, the explicit density condition
F<=A q_alpha exp(lambda(L^alpha-1)), with finite A>0, implies that
s_lambda=u+lambda^(-1)log(CV0/A) is a genuine exponential subsolution
with exact coefficient lambda and actual mass CV0. By the explicitly
supplied task principle it gives a greatest finite-mass exact solution.
For a single nonzero L1 density f, local essential boundedness off the
polar fiber and
ess limsup_{y->o} ess sup_x log^+(F/q_alpha)/L^alpha=0
are sufficient for EVERY lambda>0. A fixed-exponent alternative is
the growth bound F<=A' exp(k(L-1)+lambda L^alpha)
L^(-1-k(1-alpha)) for all large L, uniformly essentially in x and
the projective spheres, with the same local boundedness elsewhere.
These are explicit density tests, not existence reformulations.

C. For EVERY sequence of smooth strictly positive base probabilities
F_j relative to dV0=h0^m/V0 with c_h0(F_j)<=2^(-2j)/C, there EXIST
smooth strictly positive projective probabilities g_j for which
f_j=R F_j g_j and f=sum_{j>=1}2^(-j) f_j satisfy ALL original
concentration requirements: c_H(f_j)<=2^(-2j), integral f=1,
f finite everywhere, f smooth off X0 times {o},
f>=(1/2)min_X f_1>0, and b_H(f)=0. The same f, independent of
lambda, satisfies B's all-exponent density criterion and therefore
admits unbounded genuine exponential subsolutions and greatest
finite-mass exact solutions for EVERY lambda>0. All exact solutions
are necessarily unbounded. Prove actual global component equations
and normalizers, not only density probabilities or finite simulations.
This is not a statement for every already chosen full-product family.

D. The previously supplied prior P07 named elliptic threefold
X0={ [z:w] in P^3 : z,w in C^2 nonzero }/<[z:w]->[z:exp(2pi)w]>
with h0=alpha0+beta0+dt wedge d^c t, t=log(||w||^2/||z||^2),
has volume24pi and actual smooth positive h0+dd^c v_l with total
masses delta_l->0. Treat this prior complete theorem as a separately
assessed supplied dependency; its unchanged full root proof and five
earlier independent factor-proof notes are retained for review and
comparison. Reconstruct its NEW APPLICATION: derive an actual
sequence F_j satisfying C, and hence compact fourfold (k=1) and
fivefold (k=2) examples with v_minus(H)=0 and b_H(f)=0. The explicit
subsolutions have masses96pi and240pi respectively. Do NOT identify
these numbers as greatest-exact-solution masses. Derive finite positive
mass and genuine unboundedness for the exact solutions using only
the supplied principle and the actual hypotheses.

All new A--D arguments and applications must be completely independently
proved. The prior factor theorem is a retained dependency, not a new
discovery or an assertion reconstructed anew by these limited targets.
Any uncertain exact external application must be checked at its primary
source. No synthetic numerical execution, necessity, arbitrary-family
solvability, priority or complete original S03 classification is claimed.


## Required complete comparison

Compare every autonomous proof, every new independent proof and the entire current article. Assess canonical regularization, all affine and infinity charts, exact radial flux, actual non-pluripolar mass, density asymptotics and nonintegrable allowance. Check the fixed-exponent and uniform essential all-exponent conditions and every additive shift. Check EVERY supplied smooth collapsing base sequence, existence of each annulus normalization, convergence of all baseline derivatives, smooth positive global projective component equations including k=1, and the exact full-product normalizers with arbitrary R=mu/dV. Check all original concentration inequalities, probability, pointwise finiteness, strict lower bound, b_H(f)=0, and the SAME f for all lambda. Compare any different independent construction on its actual quantifier and inequalities; equality of recipes is not required. Derive finite positive mass and necessarily unbounded exact solutions using only the explicitly supplied greatest-solution principle. The explicit subsolution masses CV0, 96pi and 240pi are NOT asserted as the masses of greatest exact solutions.

The named compact elliptic threefold is prior supplied work. Compare its entire root proof and five complete earlier factor reconstructions, including compactness, volume24pi, global positive forms, all-test mass-collapse mechanism, actual smooth potentials and scalar constants. Freshly assess the NEW construction of F_j from actual collapsing potentials, subsequence choice and zero-lower-mass products. Do not derive zero-threshold S03 from positive-threshold P07 densities. Every indispensable exact external premise requires fresh primary hypothesis evidence and valid nonnegative premise-indexed bindings. No arbitrary-L1 existence black box, literature priority, recursive certification of all cited foundations or numerical-execution claim is permitted. List all actual false, missing or unresolved claims. Report scoped validity independently of the still-unresolved general classification; original_S03_completed=false.


## Final standalone source

```tex
\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\dc}{d^c}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\PP}{\mathbb P}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Exponential equations at zero individual threshold\newline
for a constructed concentration family}
\author{}\date{}
\begin{document}\maketitle
The general classification in S03 remains unresolved here.
\begin{abstract}
We construct a strictly positive integrable probability density on a
compact Hermitian product whose individual Monge--Amp\`ere threshold
is zero, but whose exponential equation has a genuine unbounded
subsolution for every positive exponent. The density is a rigorously
chosen member of the specified concentration family and is independent
of the exponent. An explicit radial density-growth criterion supplies
the subsolutions, with exactly computed finite mass. The supplied
subsolution principle then gives greatest finite-mass exact solutions,
which are necessarily unbounded. A prior elliptic threefold supplies
the required smooth mass collapse and concrete examples in dimensions
four and five. No assertion is made for every concentration-family
choice or for necessity of the sufficient criterion.
\end{abstract}

\section{Conventions, background and product geometry}
Use $\ddc=i\partial\bar\partial/(2\pi)$ and
$\dc=i(\bar\partial-\partial)/(4\pi)$, with ordinary wedge powers.
All quasi-psh potentials have their genuine canonical representatives.
Extended measures are non-pluripolar products with smooth-background
corrections. For a positive Hermitian form $h$ and reference probability
$dV$, let $c_h(g)$ be the unique scalar of the normalized
bounded-density equation, and set
\[
 b_h(f)=\lim_{j\to\infty}c_h(\min(f,j)),\qquad
 v_-(h)=\inf_{v\in\PSH(X,h)\cap L^\infty}\int_X\MA_h(v).
\]
For nonzero nonnegative bounded data, existence of a continuous
potential and uniqueness of this scalar follow from
\cite[Theorem 0.1]{KN} and \cite[Corollary 0.2]{Ng}.
Their $\ddc$ is twice ours, so their potentials are multiplied by two;
the smooth positive reference-volume ratio is absorbed into the density.
Neither theorem is applied to the final unbounded $L^1$ density.
We use the supplied maximal-subsolution characterization of $b_h$.
In particular, $\MA_h^{\rm ext}(v)\geq af\,dV$ implies $a\leq b_h(f)$,
and bounded data satisfy $b_h=c_h$.

We also use exactly the supplied S03 principle: a genuine exponential
subsolution $s$ with
$\MA_h^{\rm ext}(s)\geq e^{\lambda s}f\,dV$, $\lambda>0$, gives a
greatest genuine exact solution by decreasing bounded-density
approximation. This principle is background; we prove the required
subsolutions and their zero-threshold nonvacuity below.

Let $(X_0,h_0)$ be connected compact Hermitian of dimension $m$,
and put $Y=\PP^k$, $k\geq1$, with normalized Fubini--Study form
$\kappa$, $\int_Y\kappa^k=1$. On $X=X_0\times Y$ write
\[
 N=m+k,\quad C=\binom Nm,\quad V_0=\int_{X_0}h_0^m,
 \quad H=h_0+\kappa,
 \quad\mu=\frac{h_0^m}{V_0}\wedge\kappa^k.
\]
For any smooth positive probability $dV$ on $X$, put $R=\mu/dV$.
It is smooth with positive upper and lower bounds. Factor forms and
functions are pulled back when appropriate. Write $F=f/R$, so that
$f\,dV=F\mu$.

\section{A finite-mass radial barrier}
Fix $0<\alpha<1$ and $o=[1:0:\cdots:0]$. Put
\[
 \psi=\log\frac{\sum_{i=1}^k|Z_i|^2}{\sum_{i=0}^k|Z_i|^2},
 \qquad L=1-\psi,\qquad u=1-L^\alpha,
\]
with the canonical value $u(o)=-\infty$. For $1\leq L<\infty$ set
\begin{align*}
 t&=e^{1-L},& a&=\alpha L^{\alpha-1},\\
 Q&=t+(1-t)a,&
 D&=t(1-a)+(1-t)\alpha(1-\alpha)L^{\alpha-2},\\
 q_\alpha&=Q^{k-1}D e^{k(L-1)},&
 W&=kQ^{k-1}D.
\end{align*}
Here $q_\alpha$ is a density function on $Y\setminus\{o\}$;
its extension over $Z_0=0$ has value $1-\alpha$.

\begin{lemma}\label{lem:barrier}
The potential $u$ is genuine $\kappa$-psh and
\[
 \MA_\kappa^{\rm ext}(u)=q_\alpha\kappa^k,\qquad
 \int_Yq_\alpha\kappa^k=1,\qquad q_\alpha\geq(1-\alpha)^k.
\]
Its product pullback has actual extended mass $CV_0$. Moreover,
as $L\to\infty$,
\[
 W(L)\sim k\alpha^k(1-\alpha)L^{-1-k(1-\alpha)},\qquad
 e^{\tau(L^\alpha-1)}W(L)\longrightarrow\infty\quad(\tau>0).
\]
\end{lemma}
\begin{proof}
For $0<\varepsilon\leq1$ replace $\psi$ by the smooth function
\[
 \psi_\varepsilon=
 \log\frac{\sum_{i=1}^k|Z_i|^2+\varepsilon|Z_0|^2}
               {\sum_{i=0}^k|Z_i|^2}.
\]
It is nonpositive and $\kappa$-psh. For
$\chi(s)=1-(1-s)^\alpha$ one has $0<\chi'\leq\alpha$ and
$\chi''>0$, so
\[
 \kappa+\ddc\chi(\psi_\varepsilon)
 =(1-\chi')\kappa+\chi'(\kappa+\ddc\psi_\varepsilon)
   +\chi''d\psi_\varepsilon\wedge\dc\psi_\varepsilon
 \geq(1-\alpha)\kappa.
\]
These functions decrease to $u$. Its growth
$O(1+|\log r|^\alpha)$, $r=\sum_{i=1}^k|z_i|^2$ near $o$,
is locally integrable. Thus the decreasing psh-plus-smooth limit is
nontrivial and canonical, with its stated pole.

In the affine chart $Z_0=1$, $L=1-\log(r/(1+r))$ and a local
primitive of $\kappa+\ddc u$ is
\[
 \Phi(r)=\log(1+r)+1-[1-\log(r/(1+r))]^\alpha,
 \qquad r\Phi'=Q.
\]
The tangential and radial Hessian eigenvalues are $Q/r$ and $Q'$.
Polar integration, with its constant fixed by normalized
Fubini--Study mass, gives
\[
 \int_{a<r<b}(\ddc\Phi)^k=Q(b)^k-Q(a)^k.
\]
Since $-dQ/dL=D$, the radial mass density is $W(L)dL$.
The Fubini--Study radial probability is $ke^{-k(L-1)}dL$;
division gives exactly the displayed $q_\alpha$.
The flux limits are $Q(0)=0$, $Q(\infty)=1$ in the $r$ coordinate.
The function is smooth along the infinity hyperplane. On every
finite superlevel, its truncation agrees locally with smooth $u$;
the defining non-pluripolar exhaustion omits its pole and cutoff
masses. Hence the actual mass is one. The lower form bound proves
the density bound. Factor dimensions give the same finite-level
identity on the product, followed by the actual non-pluripolar limit:
\[
 \MA_H^{\rm ext}(u)=C h_0^m\wedge q_\alpha\kappa^k=CV_0q_\alpha\mu.
\]
Finally $Q\sim\alpha L^{\alpha-1}$ and
$D\sim\alpha(1-\alpha)L^{\alpha-2}$ give the asymptotic for $W$.
The logarithm of the last expression in the lemma is
$\tau L^\alpha-[1+k(1-\alpha)]\log L+O(1)$, tending to infinity.
\end{proof}

For $\tau>0$ write $B_\tau=q_\alpha e^{\tau(L^\alpha-1)}$.
In particular $B_\tau\geq b_0=(1-\alpha)^k$.
Its mass on every punctured pole neighborhood is infinite, even
though $q_\alpha\kappa^k$ has mass one.

\begin{theorem}\label{th:criterion}
Let $f\geq0$ be nonzero and integrable, and fix $\lambda>0$.
If, for some finite $A>0$,
\[
 F(x,y)\leq A B_\lambda(y)\quad\text{almost everywhere},
\]
then the genuine function
\[
 s_\lambda=u+\lambda^{-1}\log(CV_0/A)
\]
is an exponential subsolution with actual mass $CV_0$ and exact
coefficient $\lambda$. The supplied principle gives a greatest exact
solution. The same holds for every $\lambda>0$ if $F$ is locally
essentially bounded off $X_0\times\{o\}$ and
\[
 \mathop{\rm ess\,limsup}_{y\to o}\mathop{\rm ess\,sup}_{x}
    \frac{\log^+(F(x,y)/q_\alpha(y))}{L(y)^\alpha}=0.
\]
\end{theorem}
\begin{proof}
The exact product measure in Lemma~\ref{lem:barrier} gives
\[
 e^{\lambda s_\lambda}f\,dV
 \leq(CV_0/A)e^{\lambda u}Aq_\alpha e^{-\lambda u}\mu
 =\MA_H^{\rm ext}(s_\lambda).
\]
Both measures give zero mass to the polar fiber, and adding the
constant changes neither admissibility nor mass. For the second
claim, the limit condition bounds $F/q_\alpha$ by
$e^{(\lambda/2)L^\alpha}$ near $o$. The remaining compact region
has bounded ratio, so increasing a finite $A$ gives the first claim.
The greatest solution has finite mass because it is bounded above
on compact $X$ and $f$ is integrable.
\end{proof}

The first criterion can also be checked from the explicit growth bound
\[
 F\leq A'e^{k(L-1)+\lambda L^\alpha}L^{-1-k(1-\alpha)}
\]
for all sufficiently large $L$, uniformly essentially in $x$ and
the projective spheres, with local essential boundedness elsewhere.

\section{A zero-threshold concentration family for every exponent}
Assume that $X_0$ has smooth positive probability densities $F_j$
relative to $dV_0=h_0^m/V_0$ satisfying
\begin{equation}\label{eq:base}
 c_{h_0}(F_j)\leq 2^{-2j}/C.
\end{equation}
\begin{theorem}\label{th:construction}
For every sequence satisfying \eqref{eq:base}, one can choose smooth
strictly positive probability densities $g_j$ on $Y$ such that
\[
 f_j=RF_jg_j,\qquad f=\sum_{j\geq1}2^{-j}f_j
\]
are the specified full-product concentration family:
$c_H(f_j)\leq2^{-2j}$, $\int_Xf\,dV=1$, and $b_H(f)=0$.
The density $f$ is finite everywhere, smooth off the polar fiber and
bounded below by $\tfrac12\min_Xf_1>0$. This single $f$, independent
of $\lambda$, has genuine exponential subsolutions and greatest
finite-mass exact solutions for every $\lambda>0$. Every exact
solution is unbounded.
\end{theorem}
\begin{proof}
Put $w_j=2^{-j}$ and $M_j=\max F_j$. Choose
$0<\varepsilon_j\leq1/2$ so that
\[
 w_j\varepsilon_jM_j\leq b_0 2^{-j-2},\qquad
 w_j\varepsilon_j\|F_j\|_{C^j}\leq2^{-j},
\]
using increasing fixed smooth coordinate seminorms. Then
$E(x)=\sum_jw_j\varepsilon_jF_j(x)$ converges smoothly and
$0<E\leq b_0/4$.

Choose a smooth $0\leq\rho\leq1$ supported in $[0,1]$, positive
inside and flat at the endpoints. Inductively choose
$A_j\geq2$, $A_j>A_{j-1}+2$, with
\[
 Z_j=\int_{A_j}^{A_j+1}\rho(L-A_j)e^{(L^\alpha-1)/j}W(L)\,dL
      \geq2w_jM_j.
\]
For each fixed $j$ the integrand apart from $\rho$ tends to infinity
uniformly on intervals $[A,A+1]$ by Lemma~\ref{lem:barrier}.
Thus the choice is possible with arbitrarily large $A_j$.
Set, on that annulus and zero elsewhere,
\[
 b_j=\rho(L-A_j)B_{1/j}/Z_j,\qquad
 g_j=\varepsilon_j+(1-\varepsilon_j)b_j.
\]
Flatness makes $b_j$ smooth globally, vanishing near both $o$ and
the infinity hyperplane. Its integral is one. The $g_j$ are smooth
strictly positive probabilities and their disjoint annuli satisfy
\begin{equation}\label{eq:bump}
 w_jM_j(1-\varepsilon_j)b_j\leq B_{1/j}/2.
\end{equation}

We check the component scalar directly. For a radial $g=g_j$, put
\[
 G(r)=\int_{|z|^2<r}g\kappa^k,\quad Q_g=G^{1/k},\quad
 \phi'(r)=\frac{Q_g-r/(1+r)}r.
\]
The tangential and radial eigenvalues of the local primitive are
$Q_g/r>0$ and $Q_g'>0$, and the flux identity gives
$(\kappa+\ddc\phi)^k=g\kappa^k$. At small $r$, the bump is absent:
$G=\varepsilon_j(r/(1+r))^k$ and
$\phi=(\varepsilon_j^{1/k}-1)\log(1+r)+\mathrm{constant}$.
At large $r$,
\[
 G=1-\varepsilon_j+\varepsilon_j(r/(1+r))^k.
\]
In $v=1/r$, $Q_g$ is analytic near zero with value one and
$d\phi/dv=-(Q_g-1/(1+v))/v$ is analytic there. Since
$v=|Z_0|^2/\sum_{i\geq1}|Z_i|^2$ is smooth near $Z_0=0$,
$\phi$ extends smoothly. The metric is strictly positive there,
with tangential part $\kappa$ and transverse coefficient
$\varepsilon_j>0$; at $o$ it is $\varepsilon_j^{1/k}\kappa$.
This includes $k=1$.

Let $v_j$ solve the bounded base equation above with scalar
$c_{h_0}(F_j)$. The genuine bounded product potential
$U_j=v_j+\phi_j$ has
\[
 \MA_H(U_j)=C\MA_{h_0}(v_j)\wedge g_j\kappa^k
          =C c_{h_0}(F_j)f_j\,dV.
\]
The local bounded-product expansion, including smooth-background
corrections, has only this term by factor dimensions. Scalar
uniqueness and \eqref{eq:base} therefore give
$c_H(f_j)=C c_{h_0}(F_j)\leq2^{-2j}$.

Tonelli gives $\int f=\sum_jw_j=1$. Off the polar fiber, only finitely
many annuli meet any compact set, so
$F=E+\sum_jw_j(1-\varepsilon_j)F_jb_j$ is smooth. On the fiber
the actual pointwise sum equals the finite $E$.
Also $f\geq w_1f_1$, proving the positive lower bound.
If $a>0$ were an admissible subsolution coefficient for $f$, then
for every $j$ maximality would give
\[
 aw_j\leq b_H(f_j)=c_H(f_j)\leq2^{-2j},
 \qquad a\leq2^{-j},
\]
which is impossible. Thus $b_H(f)=0$.

Fix $\lambda>0$ and choose $J$ with $1/j\leq\lambda$ for $j\geq J$.
Since $u\leq0$, $B_{1/j}\leq B_\lambda$ for these indices.
Disjointness and \eqref{eq:bump} bound their total contribution
pointwise by $B_\lambda/2$. The baseline is at most $B_\lambda/4$.
The finitely many remaining bumps have finite constant
\[
 K_\lambda=\max_Y\sum_{j<J}w_j(1-\varepsilon_j)M_jb_j,
 \qquad D_\lambda=3/4+K_\lambda/b_0.
\]
Hence $F\leq D_\lambda B_\lambda$.
Theorem~\ref{th:criterion} gives the explicit subsolution
$s_\lambda=u+\lambda^{-1}\log(CV_0/D_\lambda)$ and a greatest
exact solution. The subsolution mass is $CV_0$; no such numerical
mass is asserted for the greatest solution. Its exact mass is finite
and positive, since its supremum is finite, $f\in L^1$ is strictly
positive, and a genuine nontrivial quasi-psh function is finite
almost everywhere. A bounded exponential subsolution would give
a positive constant coefficient for $f$, contradicting $b_H(f)=0$.
Every exact solution is therefore unbounded.
\end{proof}

The construction also satisfies the second criterion of
Theorem~\ref{th:criterion}: on the $j$th annulus,
$F/q_\alpha\leq1/4+\tfrac12 e^{(L^\alpha-1)/j}$, and elsewhere the
ratio is at most $1/4$. As the pole is approached through annuli,
$j\to\infty$, giving the stated uniform logarithmic limit.

\section{Concrete zero-lower-mass examples and scope}
The prior supplied factor in \cite[Appendix]{Product} is
\[
 X_0=\{[z:w]\in\PP^3:z,w\in\mathbb C^2\setminus\{0\}\}
       /\langle[z:w]\mapsto[z:e^{2\pi}w]\rangle,
 \quad h_0=\alpha_0+\beta_0+dt\wedge\dc t,
\]
where $t=\log(\|w\|^2/\|z\|^2)$ and the two base forms are
normalized. Its complete prior proof establishes compactness,
positivity, $V_0=24\pi$ and actual smooth $v_\ell$ with
$h_0+\ddc v_\ell>0$ and
$\delta_\ell=\int(h_0+\ddc v_\ell)^3\to0$.
Choose a subsequence with $\delta_{\ell_j}\leq2^{-2j}/C$ and put
\[
 F_j=\frac{(h_0+\ddc v_{\ell_j})^3/dV_0}{\delta_{\ell_j}}.
\]
These are smooth positive probabilities, and their actual equations
give $c_{h_0}(F_j)=\delta_{\ell_j}$ by scalar uniqueness.
Thus Theorem~\ref{th:construction} has a concrete instance.
For bounded base potentials $v$, the same local product expansion gives
$\int_X\MA_H(v)=C\int_{X_0}\MA_{h_0}(v)$, proving $v_-(H)=0$.
With $k=1$ this is a compact fourfold and the explicit subsolutions
have mass $96\pi$; with $k=2$ the mass is $240\pi$.
These are masses of the constructed subsolutions, not of the greatest
exact solutions.

\begin{remark}
The quantifier is every base sequence satisfying \eqref{eq:base},
with projective components chosen by the displayed construction.
It does not cover every previously chosen full-product concentration
family. The fixed $f$ solves the zero-threshold solvability problem
for this choice and every exponent. Necessity, arbitrary Hermitian
geometries and a nonsolvable zero-threshold example remain unproved.
No literature priority or discovery of the prior factor is claimed.
\end{remark}
\begin{thebibliography}{9}
\bibitem{KN} S. Ko\l odziej and N. C. Nguyen,
\emph{Weak solutions to the complex Monge--Amp\`ere equation on
Hermitian manifolds}, \href{https://arxiv.org/abs/1312.5491v2}{arXiv:1312.5491v2}, Theorem 0.1.
\bibitem{Ng} N. C. Nguyen,
\emph{The complex Monge--Amp\`ere type equation on compact Hermitian
manifolds and applications},
\href{https://arxiv.org/abs/1501.00891v1}{arXiv:1501.00891v1}, Corollary 0.2.
\bibitem{Product} \emph{Exact equations for $L^1$ densities on products
with zero lower mass}, checked standalone source (2026), Appendix;
\href{https://github.com/MingchenXia/non-kahler-pluripotential-theory/blob/7a244bc4938c5b918f7d906c7201f9385e4188f4/research/papers/P07-zero-lower-mass-product-equations.tex}{immutable source and complete prior factor proof}.
\end{thebibliography}
\end{document}
```
