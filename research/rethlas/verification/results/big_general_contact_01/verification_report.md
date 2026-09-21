# Verification report: big_general_contact_01

## Verdict

**Correct relative to the explicitly accepted inputs.** The audit found **0 critical errors and 0 gaps** across **82 deduction checks** and **9 reference checks**.

The conclusion established by the supplied proof is
\[
p=P_\theta(f)\leq f\quad\text{quasi-everywhere},\qquad
\mathbf 1_{\{p<f\}}\mathrm{MA}_\theta(p)=0.
\]
Here \(\theta\) may be nonclosed and non-semipositive, and the positive extended measure may have infinite total mass.

This is the requested bounded mathematical audit, not formal correctness or novelty certification. The supplied proof was read and checked in textual order. Two independent supporting reviews checked the bounded approximation chain and the signed truncation argument. The manuscript was not edited.

## Scope and assumptions

The manuscript's [standing conventions](/Users/mingchen/Non-Kahler/book/author/conventions.tex:3) make \(X\) a connected compact complex manifold without boundary. The source's normalized \(L^1\) theorem covers arbitrary smooth real backgrounds; thus the use of global supremum normalization is valid.

The following are inputs to this audit, as explicitly authorized:

- The previously verified [continuous-obstacle theorem](/Users/mingchen/Non-Kahler/book/author/section_big_continuous_contact.tex:15), including the existence of a strict analytic barrier from the accepted regularization input.
- Ordinary envelope and maximum properties, genuine envelopes' quasi-everywhere obstacle bounds, canonical representatives, and normalized \(L^1\) compactness.
- Local Bedford–Taylor mixed products, plurifine locality, bounded monotone convergence including regularized increasing limits, and the stated capacity/quasi-continuity facts.
- [Signed bounded products and the arbitrary extended measure construction](/Users/mingchen/Non-Kahler/book/author/chapter_products.tex:94), including restricted positivity/locality and no pluripolar mass.
- The accepted [bounded quasi-continuous to lower-semicontinuous approximation lemma](/Users/mingchen/Non-Kahler/book/author/section_bounded_contacts.tex:72).

The only global pluripolar existence input is SGPT Theorem 1.1.5. Its citation and context were checked. The proof does not import a general-big-contact theorem, mass domination, BMP, or PVP. Reading a source's definitions does not import other results in that source.

## Findings

- **Critical errors:** none.
- **Gaps:** none.
- **Repair hints:** none required.

The expansions below verify the deductions already present in the proof. They do not introduce a missing theorem or a new argument needed to change the verdict.

## Six priority checks

### 1. Exceptional-set repair and the increasing envelope

SGPT supplies a genuine auxiliary function \(\chi_0\) whose poles contain \(E=\{u>f\}\). Compactness supplies a finite \(B\geq1\) such that
\[
\mathrm{dd}^{c}\chi_0\geq-B\omega.
\]
Thus \(\chi=(\chi_0-\sup_X\chi_0)/B\) is nonpositive, retains those poles, and satisfies \(\mathrm{dd}^{c}\chi\geq-\omega\). After shifting \(\rho\) below \(\inf f\), the exact identity is
\[
(1+s)(\theta+\mathrm{dd}^{c} u_t)
=(\theta+\mathrm{dd}^{c} u)+t\mathrm{dd}^{c}\chi+s(\theta+\mathrm{dd}^{c}\rho),
\qquad s=t/\kappa.
\]
The curvature loss and gain cancel because \(-t+s\kappa=0\). Genuineness and convergence follow on the full-measure common finite locus; the pointwise obstacle inequality also holds at the exceptional points because \(t\chi=-\infty\).

For fixed \(t,\eta>0\), upper semicontinuity of \(u_t\) and continuity of \(f_j\) make \(\{u_t<f_j+\eta\}\) open. They increase and cover every point, including poles. A finite subcover yields one common index. Passing first \(\eta\downarrow0\), then \(t\downarrow0\), gives almost-everywhere domination. Canonical quasi-psh representatives, recovered by local averages after a common correction, give pointwise domination. Upper regularization then preserves domination of the full envelope. There is no domination-theorem step.

### 2. Local bounded monotone Bedford–Taylor limits

For bounded obstacle approximations, a common shifted barrier and a common upper bound give uniform finite bounds on every relatively compact subset of \(X\setminus Z\). A fixed quadratic correction makes all potentials psh there. Mixed bounded increasing or decreasing BT convergence applies, and the finite expansion in \(\theta-\mathrm{dd}^{c} q\) handles the nonclosed background.

The increasing limit is the regularized limit, which differs from the pointwise limit only pluripolarly. SGPT's local theorem explicitly permits the corresponding almost-everywhere increasing convergence. Portmanteau is applied only to positive locally finite measures off \(Z\). It does not require finite global mass.

### 3. Fixed quasi-continuous coefficients for signed measures

Let \(w_j=v_j+q\) and choose a fixed quadratic \(h\) with \(\mathrm{dd}^{c} h=\kappa_0\). Positivity of the expansion gives
\[
\binom n\ell(\mathrm{dd}^{c} w_j)^\ell\wedge\kappa_0^{n-\ell}
\leq(\mathrm{dd}^{c}(w_j+h))^n.
\]
A fixed affine rescaling puts the uniformly bounded \(w_j+h\) in the local capacity test range \([0,1]\). Every smooth-form summand of the signed product is therefore dominated in total variation by a constant times capacity. This includes \(\ell=0\), and the same bound holds for the limit.

For a fixed bounded quasi-continuous coefficient \(H\), choose an open \(O\) of capacity at most \(\varepsilon\) and a continuous extension \(H_\varepsilon\) agreeing with \(H\) outside \(O\), with the same supremum bound. Then
\[
\left|\int(H-H_\varepsilon)\,d\nu_j\right|
\leq 2\|H\|_\infty |\nu_j|(O)
\leq 2\|H\|_\infty K\varepsilon,
\]
and the same estimate holds for the limit. Weak convergence for \(H_\varepsilon\), followed by \(\varepsilon\to0\), proves the assertion without assigning positivity to \(\nu_j\).

### 4. Strict upper cutoff

The positive-volume sublevel set and normalized \(L^1\) bound give one finite upper bound for all competitors and their envelopes. Choosing \(M\) strictly above it ensures \(p_j<M\) everywhere. Consequently
\[
\{p_j<\min(f_j,M)\}=\{p_j<f_j\}.
\]
Equality of the capped and uncapped envelopes follows from their actual quasi-everywhere competitor definition. The artificial upper cutoff creates no possible contact point.

### 5. Locality and positivity of constant truncations

The truncations \(\max(p_j,-C)\) are bounded \(\Omega\)-psh for a Hermitian \(\Omega\geq\theta\). The proof uses their globally signed \(\theta\)-products.

The set \(\{H_{k,C}>0\}\) need not itself be plurifinely open. Locality is first applied on the larger plurifinely open set
\[
\{p_j>-C\}\cap(X\setminus Z),
\]
where the truncation equals the locally bounded \(p_j\). Equality of those measures can then be restricted to the Borel subset \(\{H_{k,C}>0\}\). For the unbounded limiting \(p\), the accepted extended construction directly supplies
\[
\mathbf1_{\{p>-C\}}(\theta+\mathrm{dd}^{c}\max(p,-C))^n
=\mathbf1_{\{p>-C\}}\mathrm{MA}_\theta(p)\geq0.
\]
No globally positive \(\theta\)-truncation product or global finite untruncated MA measure is presumed.

### 6. Exhaustion when total mass is infinite

For fixed \(k,C\), the signed convergence lemma gives zero integral for the limiting coefficient. Since its support is inside \(\{p>-C\}\), the weighted limiting measure is positive. Therefore
\[
\mathrm{MA}_\theta(p)(\{H_{k,C}\geq 1/r\})=0
\quad(r\in\mathbb N),
\]
and hence \(\mathrm{MA}_\theta(p)(\{H_{k,C}>0\})=0\).

The countable union over \(k,C\) covers every point with finite \(p<f\) outside \(Z\). The remaining pole sets are pluripolar and uncharged. Countable subadditivity completes the conclusion. Constants may depend on \(C\): the argument never sums them, sends \(C\) to infinity inside an integral, or invokes continuity of globally unbounded products.

## Reference and definition checks

The exact local [SGPT text](/Users/mingchen/Non-Kahler/research/sources/SGPT.txt:780) and [SGPT PDF](/Users/mingchen/Non-Kahler/research/sources/SGPT.pdf) were checked; Theorem 1.1.5 appears on PDF page 24, printed page 8. The PDF page was also visually inspected.

The required theorem-search tool was queried first. After one transient approval-review timeout, its retry succeeded but returned no matching statement. The required web fallback located the author's [SGPT source](https://mingchenxia.github.io/Lectures/SGPT.pdf) and its cited primary result, [Vu, Theorem 1.1](https://arxiv.org/pdf/1812.00465). These confirm the compact-complex global pole-containment statement.

One definition distinction was checked explicitly. SGPT Definition 1.5.1 describes its quasi-psh class using some smooth **closed auxiliary** background. The present proof's \(\theta\) is arbitrary smooth. The proof needs only a smooth lower bound for the supplied \(\chi_0\); domination of that auxiliary form by \(B\omega\) gives this bound. The two background classes are never identified. Vu's source defines quasi-psh locally as psh plus smooth and confirms this same required consequence. Any difference in the positive scalar normalization of \(\mathrm{dd}^{c}\) is absorbed into \(B\) before the displayed normalization of \(\chi\).

### R01. Section setup; Proposition big-bounded-lsc-contact

**Result: pass.** [Continuous-obstacle theorem](/Users/mingchen/Non-Kahler/book/author/section_big_continuous_contact.tex:15); [accepted previous verification](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/big_continuous_contact_01/verification.json).

**Input checked.** Theorem big-continuous-envelope-contact: for a continuous obstacle in the stated strict analytic big background, the genuine envelope is continuous off Z and its extended MA vanishes on the strict-gap set, with infinite total mass allowed.

**Context.** The source states the smooth possibly nonclosed background, strict rho, continuity off Z, and extended measure convention. The earlier verification's conditional prerequisites remain accepted exactly as the user specified.

**Application.** Each f_j used here is continuous and bounded on compact X, and the same strict rho is available after shifts. The present proof uses only that theorem's contact and local regularity consequences. Analytic regularization of the barrier is explicitly accepted, not re-certified here.

### R02. Lemma big-pointwise-competitor

**Result: pass.** [SGPT Theorem 1.1.5](/Users/mingchen/Non-Kahler/research/sources/SGPT.txt:780); [SGPT Definition 1.5.1](/Users/mingchen/Non-Kahler/research/sources/SGPT.txt:1813); [cited primary paper](https://arxiv.org/pdf/1812.00465).

**Input checked.** If X is a compact complex manifold and E is locally pluripolar, there is a genuine global quasi-plurisubharmonic function chi on X whose pole set contains E.

**Context.** The exact local SGPT primary was read in text and visually checked in its PDF. SGPT Definition 1.1.4 uses local containment in genuine psh poles, so E is precisely of that kind. Theorem 1.1.5 has compact complex, not compact Kahler, hypotheses. SGPT Definition 1.5.1 phrases QPSH through some smooth closed auxiliary form theta0, whereas this proof uses arbitrary smooth theta. These background classes are not identified: the only consequence needed from the supplied chi is a smooth lower bound for ddc chi. If chi is in the source's theta0 class, theta0<=B omega implies ddc chi>=-B omega. The cited original paper, Vu Theorem 1.1 (arXiv:1812.00465), uses local psh-plus-smooth quasi-psh functions and global pole containment and confirms exactly this weaker existence consequence in the general Hermitian setting. No additional contact or domination theorem from it is imported.

**Application.** For E={u>f}, q.e. order gives local pluripolarity. The supplied function is genuine and thus finite a.e. and has finite supremum. Divide chi0-sup chi0 by max{B,1} to obtain chi<=0 and ddc chi>=-omega, preserving poles. Shift rho below inf f. With s=t/kappa, -t omega+s kappa omega=0 exactly, so the corrected u_t is theta-psh in the original nonclosed background. The reference does not claim E is the exact pole set, chi is theta-psh, or that theta can be scaled harmlessly.

### R03. Proposition big-bounded-lsc-contact, initial approximation

**Result: pass.** [Infimum construction](/Users/mingchen/Non-Kahler/book/author/section_bounded_contacts.tex:57).

**Input checked.** For bounded lsc f on a compact metrizable X, f_j(x)=inf_y(f(y)+j d(x,y)) are continuous, have common bounds and increase pointwise to f.

**Context.** The quoted proposition has a Hermitian-background contact conclusion proved later using domination, but the displayed infimum construction depends only on the compact metric space and bounded lsc obstacle.

**Application.** The proof imports only that construction; its Lipschitz bounds and lsc limit were checked directly in S13. The subsequent domination-based source argument is not used.

### R04. Both bounded propositions; explanatory increasing-continuity paragraph; signed-truncation-quasicont

**Result: pass.** [SGPT local monotone convergence](/Users/mingchen/Non-Kahler/research/sources/SGPT.txt:2694); [local products](/Users/mingchen/Non-Kahler/book/author/chapter_products.tex:8).

**Input checked.** Bounded local mixed Bedford-Taylor products converge under decreasing approximation, and under increasing approximation converging almost everywhere to the regularized locally bounded psh limit; they are plurifinely local.

**Context.** SGPT Theorem 2.1.1 is a local psh theorem and explicitly includes the increasing/a.e. variant. It is not a theorem about arbitrary unbounded nonclosed theta-products. The accepted bounded-product machinery provides the finite smooth-form expansion after a quadratic correction.

**Application.** S26, S36 and S41-S50 exhibit the necessary common local/global bounds and fixed quadratic corrections. Upper regularization is handled by the a.e. increasing version. Smooth nonclosed factors occur only outside the BT currents in a finite expansion.

### R05. Proposition big-bounded-quasicont-contact

**Result: pass.** [Accepted approximation lemma](/Users/mingchen/Non-Kahler/book/author/section_bounded_contacts.tex:72).

**Input checked.** Every bounded quasi-continuous f admits bounded lsc f_j with common bounds, decreasing to f quasi-everywhere and converging in capacity.

**Context.** Its construction uses nested open exceptional sets G_j and a fixed upper bound M, defining f_j=M on G_j and f elsewhere. It gives global monotonicity and f_j>=f, not merely unrelated q.e. approximants.

**Application.** The bounded QC proposition meets both boundedness and quasi-continuity hypotheses. A common shifted strict barrier and a common upper obstacle bound make all envelope limits genuine and locally bounded off Z. The unbounded theorem applies this proposition only to the bounded g_j=min(max(f,-j),M).

### R06. Quasi-continuous coefficient arguments and capacity setup

**Result: pass.** [SGPT quasi-continuity and capacity](/Users/mingchen/Non-Kahler/research/sources/SGPT.txt:3053).

**Input checked.** Quasi-continuity means Borel measurability and finite continuity outside open sets of arbitrarily small capacity; pluripolar sets are capacity-null, and qpsh functions are quasi-continuous. The local BT capacity is defined using psh test functions with values in [0,1].

**Context.** The source's global theta-capacity is presented in its global setting; this proof explicitly uses the accepted equivalent local coordinate-cover notion. It does not assume that a nonclosed big theta admits the same bounded global capacity test family. The source's QC definition requires finite real values on the complement, so all subtractions there are well-defined.

**Application.** At each coefficient passage only a fixed bounded QC function is used. The proof establishes its own local capacity estimates from bounded psh test functions, including total variation in the signed case. At poles and on Z the coefficients have explicit harmless values and these sets can be removed within the capacity budget.

### R07. Envelope comparisons, canonical limits, and the unbounded theorem's common upper bound

**Result: pass.** [Envelope convention and upper-bound argument](/Users/mingchen/Non-Kahler/book/author/chapter_envelopes.tex:14).

**Input checked.** P_theta(f) is the usc-regularized supremum of genuine theta-psh functions below f q.e.; a genuine envelope has the q.e. obstacle bound; canonical qpsh representatives preserve a.e. inequalities; normalized theta-psh functions have a uniform L1 bound.

**Context.** The manuscript uses q.e. competitors. It defines big theta by a strict lower current bound, without requiring closedness. The normalized L1 estimate concerns potentials and smooth volume, not Monge-Ampere mass.

**Application.** All limits offered as competitors are genuine and obey the obstacle outside a countable pluripolar union. The uniform upper bound follows from the positive-volume finite sublevel and the accepted L1 bound exactly as in S53-S55. Canonical order is checked via local psh averages, not by an invalid inference from usc alone.

### R08. Signed-truncation-quasicont and final theorem, restriction to {p_j>-C} and {p>-C}

**Result: pass.** [Signed bounded products](/Users/mingchen/Non-Kahler/book/author/chapter_products.tex:18); [restricted extended products](/Users/mingchen/Non-Kahler/book/author/chapter_products.tex:94).

**Input checked.** Signed bounded products for arbitrary smooth theta are multilinear and plurifinely local. For u theta-psh, their restrictions 1_{u>-C}(theta+ddc max(u,-C))^n are positive, compatible with deeper levels, and equal the restriction of the positive non-pluripolar extended measure MA_theta(u), even when its total mass is infinite.

**Context.** The exact construction enlarges to Hermitian Omega>=theta and forms signed products of bounded Omega-psh truncations. It asserts positivity only on the truncation superlevel set. The extended object is a positive Borel measure, finite on each such set and allowed infinite mass globally.

**Application.** The proof follows precisely this order. For p_j, local boundedness off Z plus locality on the larger plurifine-open set {p_j>-C} justifies arbitrary Borel restriction to {H>0}. For unbounded p, the established truncation restriction identity is used directly. Subsequent exhaustion uses only countable unions of null sets, not finite total mass.

### R09. Ambient conventions; Theorem big-general-envelope-contact common upper bound; SGPT contextual normalization

**Result: pass.** [Ambient conventions](/Users/mingchen/Non-Kahler/book/author/conventions.tex:3); [normalized compactness](/Users/mingchen/Non-Kahler/book/author/chapter_compactness.tex:10).

**Input checked.** The manuscript works on connected compact complex X, permits arbitrary smooth real theta, and gives a uniform normalized L1 bound for this class; dd^c is normalized as i/(2 pi) partial bar-partial.

**Context.** The connectedness convention is explicit, so global sup normalization is sufficient. The source compactness theorem is for arbitrary smooth real theta, not only closed or semipositive backgrounds. The primary Vu paper uses a different positive scalar normalization of dd^c; its global pole-containment conclusion is unchanged by this normalization.

**Application.** The L1 constant in S54 is exactly the accepted one for the manuscript convention. A factor change in dd^c only changes the preliminary finite constant B in ddc chi0>=-B omega; rescaling then produces the claimed ddc chi>=-omega in the manuscript convention. All subsequent t/kappa cancellation uses that one convention consistently.

## Complete deduction ledger, in proof order

Each numbered deduction below passed relative to the inputs listed above. Critical errors and gaps are empty for every proof item.

### Section setup

**S01. A strict analytic barrier rho exists for big theta.**

Accepted explicitly through big_continuous_contact_01 and the stated analytic-regularization prerequisite; no new global contact theorem is used.

**S02. rho is smooth off its analytic pole set Z and Z is pluripolar.**

Part of the accepted barrier setup. In particular rho has a finite lower bound on each compact subset of X\Z.

**S03. Local capacity on a finite coordinate cover has pluripolar null sets and the required quasi-continuity.**

This is the explicitly accepted local BT/SGPT capacity notion. Charts may be shrunk inside slightly larger coordinate balls; compactness supplies a finite cover.

### Lemma big-pointwise-competitor

**S04. E={u>f} is pluripolar.**

Exactly the hypothesis u<=f quasi-everywhere. The global pluripolar theorem applies to arbitrary subsets; no regularity of f beyond its finite bounds is needed here.

**S05. There is genuine global quasi-psh chi with chi=-infinity on E.**

Matches SGPT Theorem 1.1.5 as read at SGPT.txt lines 780-786; formal reference search and contextual check follow in reference phase.

**S06. chi may be normalized to chi<=0 and ddc chi>=-omega.**

Compactness gives ddc chi0>=-B omega and finite sup chi0 for a genuine quasi-psh function. Taking chi=(chi0-sup chi0)/max{B,1} retains the pole set and gives both bounds; no scaling of theta-psh functions is asserted.

**S07. rho can be shifted below inf f.**

rho has finite global supremum; inf f is a real number because f is bounded. Subtracting a constant preserves theta+ddc rho>=kappa omega.

**S08. u_t=(u+t chi+s rho)/(1+s), s=t/kappa, is genuine quasi-psh.**

All coefficients are positive and all three functions are locally integrable and finite almost everywhere. Their sum is canonical quasi-psh, has no +infinity values, and is finite on a full-measure intersection.

**S09. theta+ddc u_t is positive.**

Exact identity (1+s)(theta+ddc u_t)=(theta+ddc u)+t ddc chi+s(theta+ddc rho). The last two lower bounds sum to (-t+s kappa)omega=0. This uses no closedness or semipositivity of theta.

**S10. u_t<=f outside E.**

u<=f, rho<=inf f<=f and t chi<=0 give numerator <=(1+s)f; f is finite so extended-value arithmetic is unambiguous.

**S11. u_t<=f on E.**

chi=-infinity and t>0 force u_t=-infinity there. Neither u nor rho takes +infinity, so there is no indeterminate sum.

**S12. u_t tends to u almost everywhere as t decreases to zero.**

At every point where u, chi and rho are finite, the displayed algebraic expression tends to u. The complement is a finite union of zero-volume pole sets.

### Proposition big-bounded-lsc-contact

**S13. Continuous f_j increase to bounded lsc f with common bounds.**

The cited inf-convolution f_j(x)=inf_y(f(y)+j d(x,y)) is j-Lipschitz, bounded below by m and above by f<=M, and increases. Approximate minimizers approach x since f is bounded; lsc gives the limit f(x). Only this elementary construction is imported from prop:lsc-obstacle-support, not its domination-based contact proof.

**S14. rho<=p_j<=M and the envelopes increase.**

Shift rho below m; it is a pointwise competitor for every f_j. Monotonicity follows from f_j<=f_{j+1}. The upper envelope bound follows from f_j<=M and canonical upper regularization.

**S15. q=(lim p_j)^* is genuine theta-psh.**

The family has a common upper bound and a genuine lower barrier. Accepted envelope/regularized increasing-limit properties give theta-psh q with rho<=q<=M.

**S16. q<=f quasi-everywhere and q<=p.**

The increasing regularization changes lim p_j only on a pluripolar set. Since p_j<=f_j everywhere for continuous obstacles, lim p_j<=f. Accepted q.e.-obstacle envelope properties, equivalently the preceding repair lemma, then give q<=P_theta(f).

**S17. Every competitor u admits u_t<=f everywhere.**

The repair lemma applies because f is bounded and u is genuine theta-psh with the required obstacle inequality.

**S18. {u_t<f_j+eta} are open, increasing, and cover X.**

u_t is upper semicontinuous and f_j is continuous, so the strict inequality defines an open set, including points with u_t=-infinity. Monotonicity follows from that of f_j. Since f_j(x) tends to finite f(x)>=u_t(x), positive eta guarantees eventual membership at each point.

**S19. A single index gives u_t<=f_j+eta on all X.**

Compactness gives a finite subcover. Since the sets increase, its largest index alone covers X; all later indices do also.

**S20. q>=u_t-eta, then q>=u almost everywhere.**

For all large j, u_t-eta is a theta-psh pointwise competitor for f_j, so p_j>=u_t-eta. Let eta tend to zero and then t tend to zero at finite points of all three potentials.

**S21. Almost-everywhere q>=u implies everywhere q>=u.**

Locally add a common quadratic correction to make both functions psh. The canonical representative of each is recovered by limits of local averages; the almost-everywhere inequality passes to those averages and hence to the canonical values. This is stronger than mere upper semicontinuity.

**S22. q>=p and consequently q=p.**

q dominates every competitor pointwise. The raw supremum is <=q, and upper regularization stays <=q since q is usc. Combine with S16.

**S23. p is locally bounded off Z.**

rho<=p<=M and rho smooth off Z give both finite bounds on each relatively compact chart there.

**S24. U_k={p<f_k} is open and p_j<f_j on U_k for j>=k.**

p is usc and f_k continuous; the inequalities p_j<=p<f_k<=f_j are pointwise.

**S25. MA_theta(p_j) vanishes on U_k.**

The accepted continuous-obstacle contact theorem applies to each f_j, and restriction to the smaller strict-gap set is legitimate for its positive extended measure.

**S26. Local increasing BT convergence gives MA_theta(p_j) tending weakly to MA_theta(p) off Z.**

On a compactly contained coordinate ball all p_j have common finite bounds. Choose one smooth quadratic q0 with ddc q0>=theta, so p_j+q0 are bounded psh. Apply the accepted regularized increasing mixed BT convergence and expand against the fixed smooth forms theta-ddc q0. The resulting bounded theta-products agree there with the extended measures.

**S27. MA_theta(p)(U_k\Z)=0.**

These are positive locally finite measures off Z. On every compactly supported local test domain the Portmanteau inequality for open subsets bounds the limit's mass by the zero liminf. A countable coordinate exhaustion proves the assertion for all of U_k\Z.

**S28. The union over k equals {p<f}\Z and adding Z causes no mass.**

If p(x)<f(x), increasing real f_k(x) eventually exceeds p(x), including p=-infinity. Conversely f_k<=f. The accepted extended measure vanishes on the pluripolar set Z.

**S29. The following paragraph invokes only bounded increasing convergence.**

All bounds and convergence used above are local off Z; no assertion about global mass or an unbounded increasing sequence is needed.

### Proposition big-bounded-quasicont-contact

**S30. The accepted lsc-approximation lemma applies to bounded quasi-continuous f.**

Its exact hypotheses match. The construction in section_bounded_contacts.tex gives lsc f_j with common bounds, globally decreasing, f_j>=f and q.e. limit f. Only the approximation lemma is imported.

**S31. p_j=P_theta(f_j) decrease and dominate p=P_theta(f).**

Envelope monotonicity applies; q.e. order suffices for the accepted envelope convention. A common shift of rho below the common lower bound supplies a genuine competitor for every obstacle, including f.

**S32. The decreasing limit equals p.**

The limit r is theta-psh and genuine since it dominates the common rho barrier. Outside the countable union of envelope exceptional sets and the approximation exceptional set, r<=lim f_j=f. Thus r is a q.e. competitor and r<=p. Monotonicity supplies r>=p. A decreasing genuine qpsh limit already is the canonical representative, so this is pointwise equality.

**S33. p_j and p have common local finite bounds off Z.**

The common upper obstacle bound and the common shifted rho supply these on every relatively compact subset of X\Z.

**S34. H_k=min{1,(f-p_k)_+} is bounded quasi-continuous off Z.**

p_k is finite and locally bounded there and is quasi-continuous as a qpsh function. Outside a union of small-capacity open sets, subtraction and the bounded continuous truncation preserve continuity.

**S35. H_k MA_theta(p_j)=0 off Z for j>=k.**

On its positive set p_j<=p_k<f<=f_j outside a pluripolar set. The preceding lsc contact proposition gives zero there. Its positive extended measure ignores the exceptional set; the bounded coefficient vanishes on the complement.

**S36. The bounded local products converge decreasingly.**

Common local bounds and a common quadratic correction reduce to the accepted mixed decreasing BT theorem, followed by a finite smooth-form expansion in the nonclosed background.

**S37. The convergence holds against fixed gH_k for compactly supported continuous g off Z.**

Work in finitely many nested coordinate balls covering supp g. Their uniformly bounded corrected potentials give a common capacity bound for all mixed products and for the limit. On the compact complement of an open set of capacity <epsilon, gH_k is continuous and has a continuous extension with the same supremum bound; use a cutoff supported in the chosen balls. The integral error is at most 2||gH_k||_infinity times a constant times epsilon. Weak convergence for the extension and then epsilon->0 prove the claimed convergence.

**S38. H_k MA_theta(p)=0 off Z.**

The integral of gH_k is zero for every compactly supported continuous g after S35-S37. The weighted positive locally finite measure is therefore zero on X\Z.

**S39. The positive sets of H_k exhaust {p<f} off Z.**

Here p_k decreases pointwise to finite p, so at a strict gap some p_k is already <f. Conversely p<=p_k implies every positive set is inside {p<f}. Countable union of zero-measure sets remains null.

**S40. Non-pluripolarity removes Z.**

Z is pluripolar and the accepted extended measure assigns it zero mass. Thus the bounded QC proposition has both asserted conclusions.

### Lemma signed-truncation-quasicont

**S41. A common quadratic q makes v_j+q psh on a coordinate ball.**

Since Omega+ddc v_j>=0, choose a smooth quadratic with ddc q>=Omega on a slightly larger coordinate ball. This only uses smoothness and a compact chart closure, not closedness of Omega.

**S42. The corrected psh potentials have uniform finite bounds, including the limit.**

The given common global bounds and the fixed bounded quadratic give uniform local bounds. A decreasing limit of these bounded functions is bounded Omega-psh.

**S43. The displayed finite signed-product expansion is valid.**

theta+ddc v_j=ddc(v_j+q)+(theta-ddc q); the accepted bounded products are multilinear and allow arbitrary smooth factors. The same definition applies to the limit. No sign is assigned to theta-ddc q.

**S44. Each signed summand's variation is dominated by a constant times (ddc(v_j+q))^ell wedge kappa_0^(n-ell).**

On a compactly contained chart the coefficients of the fixed smooth form (theta-ddc q)^(n-ell) have bounded size. The positivity of the BT current bounds its contraction with that form in absolute value by a fixed Euclidean positive test form.

**S45. The mixed positive measures have a uniform capacity bound.**

Put w_j=v_j+q and choose fixed h with ddc h=kappa_0. Every term in (ddc(w_j+h))^n is positive, hence binomial(n,ell)(ddc w_j)^ell wedge kappa_0^(n-ell) is bounded by that top power. Choose fixed a and L>0 with 0<=(w_j+h-a)/L<=1 on the larger ball for all j. By the local capacity definition its top MA on every Borel set E is <=Cap(E); rescaling gives the required constant times Cap(E).

**S46. The capacity bound also includes ell=0 and the limiting measure.**

ell=0 is the h-only term in the same positive expansion. The limit w+h satisfies the identical finite range bound, so the same estimate applies. In particular the signed sequence and signed limit charge no capacity-zero set.

**S47. The total variations are uniformly controlled on a finite cover.**

Sum the finitely many expansion estimates and use a partition of unity on inner balls covering compact X. The cover and constants are fixed for the given common bounds; no estimate uniform over unbounded truncation levels is asserted.

**S48. Weak convergence holds term by term.**

Ordinary decreasing mixed BT current convergence applies to the uniformly bounded psh potentials. Multiplication by the fixed smooth forms preserves distributional convergence; the uniform local variation bounds extend this to weak convergence of measures against continuous tests.

**S49. Weak convergence upgrades to every fixed bounded quasi-continuous coefficient.**

For coefficient h and an open exceptional set O of capacity <epsilon, Tietze extension from compact X\O gives continuous h_epsilon with ||h_epsilon||<=||h|| and h_epsilon=h outside O. The error in each integral, for sequence and limit, is <=2||h|| K epsilon by total variation, regardless of sign. First take j->infinity for h_epsilon, then epsilon->0.

**S50. This proves exactly the stated signed convergence lemma.**

The coefficient is fixed as j varies, all potentials have common finite bounds, and compactness permits the finite-cover estimate. Positivity of the signed measures is neither stated nor used.

### Theorem big-general-envelope-contact

**S51. The conclusion p<=f quasi-everywhere holds.**

This is the explicitly accepted envelope obstacle property under the theorem's genuineness hypothesis.

**S52. f_j=max(f,-j) are quasi-continuous, finite almost everywhere, decrease to f, and admit p as a competitor.**

The bounded-below truncation preserves quasi-continuity outside the same exceptional open sets. Pointwise max(f,-j) decreases to f, also at infinite values. The accepted p<=f q.e. gives p<=f_j q.e.

**S53. A finite sublevel A={f_1<=N} has positive smooth volume.**

The increasing union over integer N of these Borel sublevels contains the full-measure finite locus of f_1; X has positive finite smooth volume. Therefore some sublevel has positive volume.

**S54. Every competitor a for f_1 has a common finite supremum bound.**

a is genuine qpsh so sup_X a is finite and sup_X a-a>=0. On A outside a pluripolar hence zero-volume set, a<=N, whence Vol(A)(sup_X a-N)<=integral_A(sup_X a-a)<=C by the accepted normalized L1 bound. Thus sup_X a<=N+C/Vol(A). No Monge-Ampere mass enters this estimate.

**S55. The same upper bound applies to all envelopes p_j, which are genuine.**

Every competitor for f_j is one for f_1. Their raw supremum and its usc regularization stay below the constant bound. They dominate the genuine p, excluding the identically -infinity alternative; together the bounds justify genuineness.

**S56. One may choose M strictly greater than the common envelope bound.**

S54 gives a fixed real bound, so add any positive constant. The inequality p_j<M holds everywhere after upper regularization, not just q.e.

**S57. g_j=min(f_j,M) is bounded and quasi-continuous.**

Its values lie between min{-j,M} and M. Min with a finite constant preserves continuity on the complement of every quasi-continuity exceptional set, also if f has infinite values.

**S58. P_theta(g_j)=p_j.**

p_j is theta-psh, genuine, <=f_j q.e. and <M everywhere, so it is a q.e. competitor for g_j. Hence p_j<=P_theta(g_j); g_j<=f_j gives the reverse inequality by monotonicity.

**S59. Bounded contact at g_j implies contact at f_j.**

The bounded QC proposition applies separately to each bounded g_j. Because p_j<M everywhere, p_j<min(f_j,M) is equivalent to p_j<f_j. Thus the artificial upper cutoff contributes no false contact locus.

**S60. p_j is locally bounded off Z with barrier rho-C_j.**

Choose C_j so rho-C_j<=inf g_j. This is a genuine theta-psh competitor for g_j, so rho-C_j<=p_j<=M. Constants may depend on j; this local boundedness is used only for each fixed p_j, not as an unbounded-sequence uniform lower bound.

**S61. p_j decreases pointwise to p.**

Monotonicity follows from f_j decreasing. The limit r is genuine theta-psh because p<=r and there is a common finite upper bound. Outside a countable union of pluripolar exceptional sets, r<=lim f_j=f. Thus r<=P_theta(f)=p, while r>=p. A genuine decreasing qpsh limit is canonical without further upper regularization.

**S62. There is a Hermitian Omega>=theta.**

Compactness and smoothness allow Omega=L omega for a sufficiently large positive L.

**S63. v_{j,C}=max(p_j,-C) and v_C=max(p,-C) are bounded Omega-psh.**

p_j and p are Omega-psh because Omega-theta>=0. The constant -C is Omega-psh because Omega is positive. Accepted maximum stability applies in this common background. There is no claim that these truncations are theta-psh.

**S64. For each fixed C, the truncations have common finite global bounds and decrease to v_C.**

Their lower bound is -C and their upper bound is max{M,-C}. Max with a fixed constant commutes pointwise with a decreasing limit, so the convergence is exactly as required by the signed lemma.

**S65. H_{k,C} is well-defined on X\Z.**

p_k is finite there by S60, so f-p_k is unambiguous even at f=+/-infinity. The second factor min{1,(p+C)_+} is defined with value zero at p=-infinity. Both factors take values in [0,1], so no undefined infinity-times-zero product occurs.

**S66. H_{k,C} is quasi-continuous off Z.**

p_k, p and f are quasi-continuous for the accepted local capacity. Outside a union of open sets of arbitrarily small capacity they are finite and continuous, and the displayed subtraction, addition, bounded truncations and multiplication are continuous there.

**S67. Extending H_{k,C} by zero on Z preserves bounded quasi-continuity and measurability.**

Z is a closed pluripolar analytic set and has open neighborhoods of arbitrarily small capacity. Remove one such neighborhood. Its complement is compact inside X\Z and covered by finitely many charts where S66 applies; summing their capacity budgets gives global quasi-continuity. The zero extension across the Borel set Z is Borel.

**S68. For j>=k, H_{k,C}>0 implies p_j>=p>-C and p_j<=p_k<f<=f_j.**

The second positive factor is equivalent to p>-C; monotonicity gives p_j>=p and p_j<=p_k. The first factor is positive exactly when f>p_k. Finally f_j=max(f,-j)>=f. Envelope exceptional sets, if retained, are pluripolar and are null for both relevant products.

**S69. The signed bounded product nu_{j,C} equals MA_theta(p_j) on the positive set of H_{k,C}.**

First apply plurifine locality on the larger plurifine-open Borel set {p_j>-C} intersected with X\Z: v_{j,C}=p_j there and p_j is locally bounded off Z. The accepted bounded expansion is plurifinely local even though it is signed globally. Its bounded product equals the extended MA of p_j off Z. Now restrict this equality of measures to the Borel subset {H_{k,C}>0}; that subset itself need not be plurifinely open. Alternatively the accepted truncation-restriction identity gives the same equality directly.

**S70. H_{k,C} nu_{j,C}=0.**

On its positive set the identified positive measure MA_theta(p_j) vanishes by S59 and S68. Outside that set the coefficient is zero, so multiplication yields the zero signed measure globally. Uniform capacity control also makes any omitted pluripolar sets irrelevant.

**S71. The signed convergence lemma yields integral H_{k,C}(theta+ddc v_C)^n=0.**

For fixed k,C the coefficient is fixed and bounded QC, while the potentials have common bounds at this C and decrease by S64. Each input weighted integral is zero by S70. The limit signed product has finite total variation at this fixed truncation level.

**S72. H_{k,C}(theta+ddc v_C)^n=H_{k,C}MA_theta(p) is positive.**

H is supported in D_C={p>-C}. The accepted arbitrary-extended-MA construction identifies 1_{D_C}(theta+ddc max(p,-C))^n with 1_{D_C}MA_theta(p) and makes this restricted product positive. Since H=0 on the complement, multiplication gives the equality globally. No positivity of the un-restricted signed product or finite total mass of MA_theta(p) is assumed.

**S73. MA_theta(p)({H_{k,C}>0})=0.**

The weighted measure is positive and has zero total integral by S71-S72, hence is zero. More explicitly MA({H>=1/r})<=r integral H dMA=0 for every positive integer r; these sets exhaust {H>0}. Its finiteness also follows from fixed-level signed variation control, without a global MA bound.

**S74. Every x outside Z with finite p(x)<f(x) belongs to some {H_{k,C}>0}.**

By pointwise p_k(x) decreasing to p(x), the strict gap forces p_k(x)<f(x) for some k. This remains true if f(x)=+infinity since p_k(x) is finite off Z. Choose an integer C>-p(x). Both factors are then strictly positive.

**S75. The positive sets are contained in the strict-gap set outside the excluded poles.**

H>0 gives p<=p_k<f and p>-C, and the extension makes H=0 on Z. Thus the countable union in S74 is exactly the desired strict-gap set with Z and the poles of p removed.

**S76. The excluded sets Z and {p=-infinity} are pluripolar and carry no MA mass.**

Z is the barrier's analytic pole set; a genuine qpsh p has a pluripolar pole set. The accepted extended construction is non-pluripolar even with infinite total mass.

**S77. Countable exhaustion proves the asserted contact identity for an extended measure.**

The index set N x N is countable. Countable subadditivity of a positive measure makes the union of the zero-measure positive sets null. Add the two null pole sets using S76. This uses no continuity theorem for an unbounded product and no integration of an unbounded coefficient.

### Closing paragraph and hypothesis-use audit

**S78. Capacity bounds may depend on C without affecting the conclusion.**

Every limit j->infinity is taken with fixed k,C. Afterward only countable unions of zero-measure sets are taken; there is no sum or uniform supremum of the level-dependent capacity constants.

**S79. The big and strict-barrier hypotheses are used.**

They supply nonempty bounded-obstacle competitor families, local finite lower bounds off Z, and the t/kappa exceptional-set curvature correction. They are not unused assumptions.

**S80. Quasi-continuity and almost-everywhere finiteness have the stated roles.**

Quasi-continuity is used for bounded lsc approximation and every coefficient-limit argument; almost-everywhere finiteness supplies a positive-volume finite sublevel for the uniform envelope upper bound. SGPT's quasi-continuity convention itself is finite and continuous outside small-capacity sets, so some finiteness can also follow from that convention; the explicit hypothesis is harmless.

**S81. Genuineness of the original envelope is used.**

It supplies a genuine lower competitor for all lower-truncated obstacles and prevents the decreasing unbounded limit from degenerating to identically -infinity. The theorem does not establish nonemptiness from obstacle measurability alone.

**S82. Nonclosed backgrounds and infinite mass are consistently allowed.**

All uses of BT occur after a common local quadratic correction, with finite expansion in smooth possibly nonclosed factors. All positivity claims about truncations are restricted. No BMP, PVP, general-big-contact result, mass domination theorem, or global finite-mass convergence is invoked.

## Persisted artifacts

All 82 step checks are recorded in the ordered records of [statement_checks.jsonl](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/big_general_contact_01/statement_checks.jsonl). All nine reference checks are recorded in [reference_checks.jsonl](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/big_general_contact_01/reference_checks.jsonl). Independent reviews and run events are in [events.jsonl](/Users/mingchen/Non-Kahler/research/rethlas/verification/memory/big_general_contact_01/events.jsonl). The failed-check channel is empty because no mathematical error or gap was found.

The final structured result is [verification.json](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/big_general_contact_01/verification.json). Its verdict is correct exactly because both finding lists are empty.
