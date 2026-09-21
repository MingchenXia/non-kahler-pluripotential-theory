# Verification report: relative_measure_carrier_01

## Verdict and scope

**Verdict: correct under the explicit prerequisites.** No critical errors or gaps were found.

The audit contains **24 sequential records, 77 small deduction checks, and 9 reference checks**. The supplied proof was read in textual order and checked against the book's exact conventions. Independent reviews of both product comparisons, the convex-sum/Radon–Nikodym passage, and the conditional local reference agreed with the sequential audit.

The sole conditional input is:

> On a bounded coordinate ball, every compactly supported finite non-pluripolar measure is absolutely continuous with respect to the Monge–Ampère measure of some bounded local plurisubharmonic function.

Only that local assertion from the proof of lemma bounded-measure-carrier is imported. Its source and dimension-one argument were inspected. Neither that lemma's global carrier conclusion nor any global equation-existence theorem is assumed. This run does not complete or change general_measure_minimal_01; inclusion remains subject to both audits.

## Audited conclusion and conventions

For smooth semipositive big \(\theta\), genuine \(\varphi\in\operatorname{PSH}(X,\theta)\), and genuine \(P_{\epsilon\theta}(\varphi)\) with \(0<\epsilon<1\), every finite non-pluripolar measure \(\mu\) can be written
\[
\mu=f\,\operatorname{MA}^{\mathrm{ext}}_\theta(\psi),
\qquad
\psi\simeq\varphi,\qquad
0\le f\in L^1\!\left(\operatorname{MA}^{\mathrm{ext}}_\theta(\psi)\right).
\]
The reference measure may have infinite total mass. Ordinary type means two-sided additive bounds, with inequalities used at common poles; it does not mean multiplier-ideal equivalence or a model-envelope fixed point.

The accepted inputs are local positive mixed products, plurifine locality and positivity on finite truncation levels, quasi-psh maxima and pasting, canonical representatives, a strict big potential, and the sigma-finite Radon–Nikodym theorem. No bounded mass property (BMP) or positive lower-volume property (PVP) is used.

## Key calculations

### Strictness and gluing without boundedness

The exact current identity is
\[
\theta+dd^c s
=(\epsilon\theta+dd^cq)+(1-\epsilon)(\theta+dd^c\rho)
\ge(1-\epsilon)a\omega.
\]
Genuineness follows because \(q,\rho\) are locally integrable and finite off pluripolar sets. The order \(s\le\varphi\) allows additional poles of \(s\). A cutoff with \(dd^c\chi_i\ge-L_i\omega\) permits \(\delta_iL_i\le(1-\epsilon)a/2\). On the boundary collar, \(v_i+\chi_i\le-1\); hence the maximum equals \(s\) and pastes globally. The next maximum gives
\[
\varphi-m-2\delta_i\le q_{i,m}\le\varphi.
\]

### Local domination at finite levels

Set \(s_j=\max(s,-j)\) and \(r_j=s_j+\delta_i v_i-2\delta_i\) near \(K_i\). Semipositivity makes \(s_j\) bounded and \(\theta\)-psh, and bounded mixed positivity gives
\[
(\theta+dd^cr_j)^n
=\bigl((\theta+dd^cs_j)+\delta_i dd^cv_i\bigr)^n
\ge\delta_i^n(dd^cv_i)^n.
\]
On \(F_j=D_{i,m}\cap\{s>-j\}\), one has \(q_{i,m}=r_j>-j-\delta_i\). If \(L>j+\delta_i\), its bounded truncation at \(-L\) equals \(r_j\) there. Plurifine locality and increasing exhaustion prove the extended-measure inequality. The bounded local reference measure ignores any extra poles of \(s\).

Almost every point of \(K_i\) lies in \(D_{i,m}\) for an integer \(m>\varphi-s-\delta_i v_i\). The countable union therefore proves the common-null-set assertion without a uniform bound on \(\varphi-s\).

### Relative convex sums and fixed-summand remainders

For example \(t_k=2^{-k-1}/(1+C_k)\) gives positive weights with sum less than one and finite \(B=\sum t_kC_k\). The decreasing sums satisfy
\[
\varphi-B\le\psi_N\le\varphi.
\]
Only the relative deviations are bounded. The lower bound gives uniform \(L^1\) control and prevents collapse.

For \(N\ge k\), use
\[
w_{k,N}=
\frac{\sum_{\ell\le N,\ell\ne k}t_\ell q_\ell+
(1-\sum_{\ell\le N}t_\ell)\varphi}{1-t_k}.
\]
These are decreasing convex combinations with
\[
\varphi-\frac{B-t_kC_k}{1-t_k}\le w_{k,N}\le\varphi.
\]
Their genuine limit gives \(\psi=t_kq_k+(1-t_k)w_k\), \(w_k\simeq\varphi\), without subtracting infinite values at poles.

### Extended positivity and sigma-finite Radon–Nikodym

Put \(E_j=\{q_k>-j\}\cap\{w_k>-j\}\). For bounded truncations \(Q_j,W_j\), their convex combination \(V_j=t_kQ_j+(1-t_k)W_j\) satisfies
\[
(\theta+dd^cV_j)^n\ge t_k^n(\theta+dd^cQ_j)^n.
\]
Locality on \(E_j\), followed by exhaustion off the common pole set, proves the global inequality of positive extended measures. Thus any null set for the single carrier is null for every \(q_k\) carrier, hence for \(\mu\).

Each restriction to \(\{\psi>-j\}\) is part of one fixed bounded product of finite mass on compact \(X\). The countable level sets and null pole set prove sigma-finiteness; no uniform mass bound is needed. Radon–Nikodym then gives
\[
\int_X f\,d\operatorname{MA}^{\mathrm{ext}}_\theta(\psi)=\mu(X)<\infty.
\]

## Full sequential verification

The records below preserve textual order. Every listed step passed; all corresponding critical-error and gap arrays are empty.

### S01. Proposition: assumptions and intended conclusion

Source: [book/author/section_relative_measure_carrier.tex, lines 1-17](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:1).

1. **Valid.** The input is usable mathematical proof text. Standing conventions give connected compact complex X of dimension n>=1, canonical quasi-psh representatives, and smooth Hermitian omega. Theta is smooth, semipositive and big, but need not be closed.

2. **Valid.** Phi is genuine theta-psh and P_(epsilon theta)(phi) is explicitly assumed genuine for some 0<epsilon<1. Mu is a finite positive Borel measure that vanishes on pluripolar sets.

3. **Valid.** Ordinary equivalence means two-sided additive-constant inequalities. It is neither equality of multiplier ideals nor a model-envelope fixed point.

4. **Valid.** The target is a carrier representation with f>=0 integrable relative to a possibly infinite extended measure; no equation with prescribed density or mass is being solved. The ONLY conditional import is the bounded local carrier assertion.

### S02. Proof paragraph 1: normalization and smaller-background envelope

Source: [book/author/section_relative_measure_carrier.tex, lines 19](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:19).

1. **Valid.** A constant translation makes phi<=0 without changing its current or ordinary type. Envelope translation invariance follows directly by translating its competitors, so genuineness persists.

2. **Valid.** By the envelope definition and genuine-envelope assumption, q=P_(epsilon theta)(phi) belongs to PSH(X,epsilon theta). It satisfies q<=phi: the q.e. obstacle inequality is pointwise for canonical representatives and the upper semicontinuous obstacle phi.

3. **Valid.** Bigness gives a genuine rho in PSH(X,theta) with theta+ddc rho>=a omega, a>0. An additive normalization gives rho<=0. No boundedness or analytic singularities of rho is needed.

### S03. Proof paragraph 1: strict stronger-singularity potential s

Source: [book/author/section_relative_measure_carrier.tex, lines 21-24](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:21).

1. **Valid.** The exact identity theta+ddc s=(epsilon theta+ddc q)+(1-epsilon)(theta+ddc rho) implies theta+ddc s>=(1-epsilon)a omega. The positive leftover coefficient uses epsilon<1.

2. **Valid.** Since rho<=0 and q<=phi, s=q+(1-epsilon)rho<=phi. Only the stronger singularity order is asserted; s need not have phi's ordinary type and may have additional poles.

3. **Valid.** The sum is genuine: q and rho are locally integrable and finite outside a pluripolar union, so their sum is locally integrable and not identically -infinity. The strict current inequality alone is not being used to infer genuineness.

4. **Valid.** The pole sets of s and phi are pluripolar and Borel, hence mu-null. S<=phi also implies that a finite point of s is a finite point of phi.

### S04. Proof paragraph 2: finite coordinate cover and conditional local carriers

Source: [book/author/section_relative_measure_carrier.tex, lines 26-29](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:26).

1. **Valid.** Compactness supplies finitely many compact inner coordinate balls K_i whose interiors cover X, each contained in a larger coordinate ball B_i. Thus mu_i=1_(K_i)mu is finite, positive, NPP and compactly supported inside B_i.

2. **Valid.** The stipulated local assertion supplies a bounded local psh v_i with mu_i << (ddc v_i)^n. This uses no global carrier conclusion of lemma bounded-measure-carrier and no equation theorem.

3. **Valid.** A positive affine change puts the bounded potential in [1,2], multiplying its MA product by a strictly positive constant and preserving null sets. Zero pieces may be omitted or assigned any bounded psh carrier.

4. **Valid.** The measure nu_i=(ddc v_i)^n is locally finite and non-pluripolar by the accepted bounded local product theory. No total-mass estimate near the boundary of B_i is required.

### S05. Proof paragraph 2: cutoff and curvature reserve

Source: [book/author/section_relative_measure_carrier.tex, lines 30-34](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:30).

1. **Valid.** Choose a smooth function chi_i in [-3,0], zero on a neighborhood of K_i and -3 near the boundary of B_i. Its Hessian is bounded below by -L_i omega, since its transition region is relatively compact.

2. **Valid.** Writing c=(1-epsilon)a>0, choose delta_i>0 with delta_i L_i<=c/2 (arbitrary sufficiently small positive delta_i if L_i=0). Then theta+ddc(s+delta_i(v_i+chi_i)) >= (c/2)omega+delta_i ddc v_i.

3. **Valid.** This calculation uses the strict lower current bound for s and smoothness of chi_i. It does not use boundedness of s or a local potential for the nonclosed theta.

### S06. Proof paragraph 2: pasting S_i with s

Source: [book/author/section_relative_measure_carrier.tex, lines 35-38](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:35).

1. **Valid.** Both branches s and s+delta_i(v_i+chi_i) are theta-psh on B_i, so their maximum is theta-psh by the accepted maxima rule.

2. **Valid.** On the boundary collar v_i+chi_i<=2-3=-1. Thus the maximum equals s on a whole collar, including at poles; extending it by s outside B_i is a legitimate global pasting.

3. **Valid.** Because chi_i<=0 and v_i<=2, the pointwise bounds s<=S_i<=s+2delta_i<=phi+2delta_i hold, interpreted as extended-real inequalities at poles.

4. **Valid.** S_i is genuine and may be unbounded. The pasting reference is s itself, for which collar equality is available; it is not phi-m.

### S07. Proof paragraph 2: q_(i,m) and ordinary-type bounds

Source: [book/author/section_relative_measure_carrier.tex, lines 39-46](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:39).

1. **Valid.** For every integer m>=1, both phi-m and S_i are global theta-psh. Their maximum followed by subtraction of 2delta_i gives a genuine theta-psh q_(i,m).

2. **Valid.** The first branch gives q_(i,m)>=phi-m-2delta_i. Since phi-m<=phi and S_i<=phi+2delta_i, the maximum is <=phi+2delta_i, giving q_(i,m)<=phi.

3. **Valid.** Therefore phi-C_(i,m)<=q_(i,m)<=phi with C_(i,m)=m+2delta_i<infinity. This proves precisely ordinary type equivalence and equality of the pole sets with that of phi, without an absolute boundedness assertion.

### S08. Proof paragraph 3: winning set D_(i,m)

Source: [book/author/section_relative_measure_carrier.tex, lines 48-52](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:48).

1. **Valid.** Where chi_i=0 near K_i, v_i>=1 implies s+delta_i v_i>s at finite points of s. Hence S_i=s+delta_i v_i there; at poles both expressions equal -infinity.

2. **Valid.** D_(i,m) is restricted to finite values and to that neighborhood. It is Borel and plurifinely open: quasi-psh functions are plurifinely continuous at finite points, and the strict comparison of the two finite branches is open in that topology.

3. **Valid.** On D_(i,m), the chosen branch yields q_(i,m)=s+delta_i v_i-2delta_i. This is equality on a plurifinely open Borel set, exactly the locality hypothesis.

### S09. Local domination: bounded-level positive product inequality

Source: [book/author/section_relative_measure_carrier.tex, lines 53-57](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:53).

1. **Valid.** An explicit implementation of the submitted finite-level argument is s_j=max(s,-j). Since theta>=0 and s<=0, s_j is a globally bounded theta-psh potential.

2. **Valid.** On the neighborhood of K_i put r_j=s_j+delta_i v_i-2delta_i, a bounded local quasi-psh potential. The exact current decomposition is theta+ddc r_j=(theta+ddc s_j)+delta_i ddc v_i.

3. **Valid.** Both summands are positive with bounded local potentials. Bounded mixed multilinearity and positivity therefore yield (theta+ddc r_j)^n >= delta_i^n nu_i. The signed terms in a nonclosed-background smooth expansion are not separately declared positive.

4. **Valid.** Thus the claimed comparison can be justified entirely with the accepted finite-level products. No boundedness of the original s, closedness of theta, BMP or PVP enters.

### S10. Local domination: locality and exhaustion for extended measures

Source: [book/author/section_relative_measure_carrier.tex, lines 53-57](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:53).

1. **Valid.** Let F_j=D_(i,m) intersect {s>-j}. It is Borel and plurifinely open. On F_j, r_j=q_(i,m), and the lower bound v_i>=1 gives q_(i,m)>-j-delta_i.

2. **Valid.** For L>j+delta_i, max(q_(i,m),-L)=q_(i,m)=r_j on F_j. Bounded locality identifies the r_j product with the restriction of the bounded q_(i,m) truncation product, and hence with MA_theta^ext(q_(i,m)) there.

3. **Valid.** It follows that 1_(F_j)MA_theta^ext(q_(i,m))>=delta_i^n 1_(F_j)nu_i. As j increases, F_j exhausts D_(i,m), since s is finite there. Continuity from below of positive measures proves exactly the displayed local domination.

4. **Valid.** The broader exhaustion off s's pole set in the proof is also sound: nu_i charges no pluripolar set, so it loses no mass at possible additional poles of s. No unrestricted weak convergence of unbounded MA products is used.

### S11. Proof paragraph 4: union over m at finite points

Source: [book/author/section_relative_measure_carrier.tex, lines 59](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:59).

1. **Valid.** For mu_i-almost every x in K_i, both s(x) and phi(x) are finite. Choose an integer m>max(0,phi(x)-s(x)-delta_i v_i(x)); then x belongs to D_(i,m).

2. **Valid.** Thus the countable union over positive integers m covers K_i outside a single mu_i-null pluripolar set. No uniform bound on phi-s is needed and no boundedness of s is inferred.

### S12. Proof paragraph 4: common null sets of the carrier family

Source: [book/author/section_relative_measure_carrier.tex, lines 59](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:59).

1. **Valid.** Let A be a Borel set null for every MA_theta^ext(q_(i,m)). For each i,m, local domination and delta_i>0 give nu_i(A intersect D_(i,m))=0.

2. **Valid.** Since mu_i<<nu_i, also mu_i(A intersect D_(i,m))=0. Countable subadditivity in m and the preceding finite-point cover give mu_i(A)=0.

3. **Valid.** The K_i cover X, so mu(A)<=sum_i mu_i(A)=0. Overlaps cause no difficulty. This is a common-null-set conclusion for the whole countable family, not a claim that one fixed q_(i,m) dominates all of mu.

### S13. Proof paragraph 5: enumeration and summable weights

Source: [book/author/section_relative_measure_carrier.tex, lines 61-65](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:61).

1. **Valid.** Finitely many i and countably many m form a countable family, indexed by k. Its constants C_k=m+2delta_i are finite and positive.

2. **Valid.** For example t_k=2^(-k-1)/(1+C_k), k>=1, gives positive weights with sum t_k<=1/2<1 and sum t_k C_k<=1/2<infinity.

3. **Valid.** Write B=sum t_k C_k. The controlled quantities are the bounded relative deviations from phi, not the absolute norms of the unbounded q_k.

### S14. Proof paragraph 5: finite convex combinations and monotonicity

Source: [book/author/section_relative_measure_carrier.tex, lines 66-71](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:66).

1. **Valid.** Each psi_N is a convex combination of theta-psh q_1,...,q_N and phi: all coefficients are nonnegative, sum to one, and the remaining phi coefficient is positive. Thus psi_N is genuine theta-psh.

2. **Valid.** At finite points of phi, psi_N=phi+sum_(k<=N)t_k(q_k-phi). This yields phi-B<=psi_N<=phi and psi_(N+1)-psi_N=t_(N+1)(q_(N+1)-phi)<=0.

3. **Valid.** At poles of phi every q_k and every psi_N equals -infinity; the inequalities and decreasing order hold there directly as extended-real statements. No subtraction of infinite values is required.

### S15. Proof paragraph 5: genuine limit and ordinary type

Source: [book/author/section_relative_measure_carrier.tex, lines 71](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:71).

1. **Valid.** The bound phi-B<=psi_N<=phi<=0 gives uniform smooth-volume L1 control, since phi is locally integrable on compact X. It excludes collapse to the identically -infinite function.

2. **Valid.** The decreasing limit theorem for quasi-psh functions with a fixed lower curvature bound yields a genuine theta-psh limit psi and L1 convergence. The decreasing limit is its canonical upper semicontinuous representative.

3. **Valid.** Passing the bounds to the pointwise limit gives phi-B<=psi<=phi, proving exactly psi~phi. It also proves that psi and phi have precisely the same pole set.

### S16. Fixed-summand decomposition: construction of w_k

Source: [book/author/section_relative_measure_carrier.tex, lines 71-76](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:71).

1. **Valid.** For fixed k and N>=k define w_(k,N)=[sum_(l<=N,l!=k)t_l q_l+(1-sum_(l<=N)t_l)phi]/(1-t_k). Since 0<t_k<1, its coefficients are nonnegative and sum to one.

2. **Valid.** These remainders decrease and satisfy phi-(B-t_k C_k)/(1-t_k)<=w_(k,N)<=phi. Thus the same lower-bound and decreasing-limit argument gives a genuine w_k in PSH(X,theta), with w_k~phi.

3. **Valid.** The finite identities psi_N=t_k q_k+(1-t_k)w_(k,N) pass to the limit at finite points and hold as sums of negative infinities at common poles. This proves the decomposition without defining w_k by an undefined infinity-minus-infinity subtraction.

### S17. Fixed-summand comparison: common pole set

Source: [book/author/section_relative_measure_carrier.tex, lines 76-81](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:76).

1. **Valid.** The two-sided ordinary bounds for q_k, w_k and psi show that each is finite exactly where phi is finite. Hence their common pole set is exactly P={phi=-infinity}.

2. **Valid.** Set E_j={q_k>-j} intersect {w_k>-j}. These Borel plurifinely open sets increase to X minus P. All of the relevant extended measures assign P zero mass.

### S18. Fixed-summand comparison: bounded positive products

Source: [book/author/section_relative_measure_carrier.tex, lines 76-81](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:76).

1. **Valid.** Put Q_j=max(q_k,-j), W_j=max(w_k,-j) and V_j=t_k Q_j+(1-t_k)W_j. Semipositivity of theta makes Q_j and W_j bounded theta-psh; the same holds for V_j.

2. **Valid.** The exact bounded decomposition theta+ddc V_j=t_k(theta+ddc Q_j)+(1-t_k)(theta+ddc W_j), followed by mixed positivity, gives MA_theta(V_j)>=t_k^n MA_theta(Q_j).

3. **Valid.** On E_j, V_j=psi>-j, so V_j=max(psi,-j) there. Locality identifies both sides with the restrictions of MA_theta^ext(psi) and MA_theta^ext(q_k), respectively.

4. **Valid.** Taking increasing restrictions along E_j proves MA_theta^ext(psi)>=t_k^n MA_theta^ext(q_k) globally. This is an inequality of positive extended measures even if their masses are infinite; it never subtracts infinite measures or treats them as globally finite currents.

### S19. Absolute continuity with respect to the single carrier

Source: [book/author/section_relative_measure_carrier.tex, lines 81-82](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:81).

1. **Valid.** If MA_theta^ext(psi)(A)=0 for a Borel set A, the preceding inequality with t_k>0 forces MA_theta^ext(q_k)(A)=0 for every k.

2. **Valid.** The previously proved common-null-set statement now gives mu(A)=0. Hence mu<<MA_theta^ext(psi). Countability and positive individual weights suffice; no uniform domination constant over k is needed.

### S20. Final proof paragraph: sigma-finiteness

Source: [book/author/section_relative_measure_carrier.tex, lines 84](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:84).

1. **Valid.** The sets H_j={psi>-j}, j>=1, are Borel and exhaust the complement of the pole set, since psi<=0.

2. **Valid.** By compatible finite-level locality in the exact extended-measure definition, 1_(H_j)MA_theta^ext(psi)=1_(H_j)(theta+ddc max(psi,-j))^n.

3. **Valid.** Each fixed bounded product has finite total mass on compact X by local bounded-product theory and a finite coordinate cover. No upper bound uniform in j is asserted or required.

4. **Valid.** The countable collection H_j together with the pole set, of mass zero, covers X by finite-measure sets. This proves sigma-finiteness, not finiteness.

### S21. Final proof paragraph: Radon--Nikodym and integrability

Source: [book/author/section_relative_measure_carrier.tex, lines 84-88](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:84).

1. **Valid.** Both measures are defined on the Borel sigma-algebra; the reference is sigma-finite and mu is finite, hence sigma-finite. The absolute continuity hypothesis was established in S19.

2. **Valid.** The accepted sigma-finite Radon--Nikodym theorem supplies a measurable density f>=0 with mu=f MA_theta^ext(psi).

3. **Valid.** Integrating over X gives integral f dMA_theta^ext(psi)=mu(X)<infinity. Thus f belongs to the claimed L1 space and is finite almost everywhere for the reference measure, even if its total mass is infinite.

### S22. Final proof paragraph: zero measure

Source: [book/author/section_relative_measure_carrier.tex, lines 88](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:88).

1. **Valid.** For mu=0, choosing psi=phi and f=0 gives the required theta-psh potential, identical ordinary type and zero weighted measure.

2. **Valid.** The zero function has L1 integral zero for a possibly infinite measure, by the definition of the nonnegative Lebesgue integral. No expression 0 times an infinite total mass is used.

### S23. Final paragraph: exact scope and no equation overclaim

Source: [book/author/section_relative_measure_carrier.tex, lines 91](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:91).

1. **Valid.** Bounded relative difference psi-phi, interpreted via ordinary-type inequalities at poles, does not imply absolute boundedness of psi when phi is unbounded.

2. **Valid.** The bounded subsolution theorem as stated in section_bounded_subsolution.tex:61-72 requires both a bounded reference potential and a bounded density. The constructed psi need not meet the first requirement, and f need not meet the second.

3. **Valid.** Truncating f gives bounded densities and finite measures, because min(f,j)<=f is integrable. It supplies neither a bounded reference nor an existence result in psi's prescribed ordinary type. The final paragraph accurately leaves that existence or compactness step separate.

### S24. Global hypothesis and dependency audit

Source: [book/author/section_relative_measure_carrier.tex, lines 1-91](/Users/mingchen/Non-Kahler/book/author/section_relative_measure_carrier.tex:1).

1. **Valid.** Smoothness controls local corrections and cutoff Hessians. Semipositivity justifies all constant truncations. Compactness supplies the finite cover and finiteness of each fixed bounded product.

2. **Valid.** Bigness gives rho with a strict lower curvature bound, while genuineness of the smaller-background envelope gives q and epsilon<1 supplies the strictly positive curvature reserve for local perturbations.

3. **Valid.** Non-pluripolarity removes the poles and the singular part in the conditional local input; finiteness of mu supplies that input and the final density's integrability.

4. **Valid.** No model fixed-point property of phi, bounded mass property, positive lower-volume property, equality of masses under equivalent singularities, global carrier lemma, or equation-existence result is invoked. All assumptions have accounted-for roles; no suspicious unused hypothesis remains.

## Full reference verification

Internal references and accepted inputs were checked against their exact scope. The only external-paper theorem within the conditional local input was searched through search_arxiv_theorems first, then built-in web search when no match was returned.

### R01. Proof paragraph 1 and ordinary-type conclusions

**Status:** checked. **Kind:** local conventions / accepted input.

**Sources:**

- [conventions.tex](/Users/mingchen/Non-Kahler/book/author/conventions.tex:3): lines 3-14
- [chapter_envelopes.tex](/Users/mingchen/Non-Kahler/book/author/chapter_envelopes.tex:8): lines 8-22,66-82

**Referenced assertion:** Big means existence of genuine rho with theta+ddc rho>=a omega; P_theta(f) is the usc regularized supremum of theta-psh competitors below f q.e.; ordinary equivalence means two-sided additive-constant bounds.

**Context and definitions:** Compact connected X and canonical quasi-psh representatives are standing conventions. Theta need not be closed. Ordinary type and multiplier-ideal type are different notions. A genuine smaller-background envelope is assumed directly, not obtained from a model fixed point.

**Application:** The proof uses exactly these definitions: q<=phi, strict s=q+(1-epsilon)rho, and phi-C<=q_(i,m)<=phi. No envelope fixed-point consequence is imported.

**Critical errors:** none. **Gaps:** none.

### R02. Finite-level local and fixed-summand product inequalities; sigma-finiteness

**Status:** checked. **Kind:** local conventions / accepted input.

**Sources:**

- [chapter_products.tex](/Users/mingchen/Non-Kahler/book/author/chapter_products.tex:25): lines 25-46,50-87,98-140

**Referenced assertion:** Bounded products are multilinear, plurifinely local and positive when their factors are positive. Constant truncations preserve theta-psh when theta>=0. The extended MA is the increasing limit of restrictions 1_{u>-t}(theta+ddc max(u,-t))^n, with zero mass on pluripolar sets and possibly infinite total mass.

**Context and definitions:** The smooth nonclosed background is expanded separately; its signed expansion terms are not individually positive. Finite-level positivity applies on common truncation sets. Every fixed bounded product has finite mass on compact X, with no uniform BMP bound required. The extended measure can fail to be a globally locally finite current.

**Application:** S09-S10 and S17-S18 explicitly realize both inequalities with positive bounded factors on common finite-level sets. S20 uses finiteness of each individual bounded product only, which proves sigma-finiteness exactly as chapter_products.tex:128-140 states.

**Critical errors:** none. **Gaps:** none.

### R03. Proof paragraph 2: reference to lemma bounded-measure-carrier

**Status:** accepted_conditional_input_and_inspected. **Kind:** exact conditional local prerequisite.

**Sources:**

- [section_general_measure_minimal.tex](/Users/mingchen/Non-Kahler/book/author/section_general_measure_minimal.tex:15): lines 15-28

**Referenced assertion:** On a bounded coordinate ball, every compactly supported finite non-pluripolar measure tau is absolutely continuous with respect to (ddc v)^n for some bounded local psh function v.

**Context and definitions:** This is ONLY the local assertion inside the proof. The local Cegrell class E_0 is not the book's global envelope class E_0. No global bounded carrier, global equation or measure-continuity theorem is accepted through this cross-reference.

**Application:** Each mu_i is finite, NPP and compactly supported in B_i. A positive affine change normalizes v_i to [1,2] and preserves the product's null sets. Both dimension regimes are covered by R04 and R05. The root verdict remains explicitly conditional on this exact local assertion, as requested; it does not complete or change general_measure_minimal_01.

**Critical errors:** none. **Gaps:** none.

### R04. Conditional local assertion: Cegrell 1998, Theorem 6.3 and local E_0 definition

**Status:** matched_and_applicable_within_conditional_scope. **Kind:** external paper inside the exact conditional prerequisite.

**Sources:**

- [Ceg98.pdf](/Users/mingchen/Non-Kahler/research/sources/Ceg98.pdf): physical 23 / printed 209: Theorem 6.3; physical 2 / printed 188: standing domain and E_0 definition
- [Urban Cegrell, Pluricomplex energy, Acta Mathematica 180 (1998), 187-217](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6561-11511_2006_Article_BF02392899.pdf)

**Referenced assertion:** A positive compactly supported measure tau on a bounded hyperconvex domain in C^n, n>=2, has a decomposition tau=g(ddc v)^n+tau_s with v in local E_0, 0<=g in L1((ddc v)^n), and tau_s a positive measure carried by a pluripolar set.

**Context and definitions:** The paper's domain is bounded, connected and hyperconvex in C^n, n>=2. Its local E_0 consists of bounded negative psh functions with limit zero at every boundary point and finite total MA mass. This is not the global envelope class denoted E_0 elsewhere in the book.

**Application steps:**

1. A coordinate ball is bounded, connected and hyperconvex, and mu_i is finite and compactly supported in that ball.

2. The singular measure tau_s is positive, satisfies tau_s<=tau and is carried by a pluripolar set P. If tau is NPP, tau(P)=0, hence tau_s=0.

3. The remaining decomposition gives tau<< (ddc v)^n, exactly the conditional input.

4. A positive affine change of v and a positive normalization change of ddc preserve the MA measure's null sets.

5. No subsequent increasing-measure or equation-existence consequence of Theorem 6.3 is imported. The dimension-one case is handled separately.

**First search:** search_arxiv_theorems, 5 results, endpoint https://leansearch.net/thm/search.

Exact query:

> Cegrell 1998 Theorem 6.3. Let mu be a nonnegative measure of compact support in a bounded hyperconvex domain Omega in C^n, n>=2. Then there is a plurisubharmonic function phi in E_0(Omega) and 0<=f in L^1((ddc phi)^n) such that mu=f(ddc phi)^n+mu_s, where mu_s is carried by a pluripolar set. E_0 consists of bounded negative plurisubharmonic functions with zero boundary values and finite total Monge-Ampere mass.

Returned candidates and direct comparisons:

| Candidate | Theorem | Comparison |
| --- | --- | --- |
| [The Kobayashi distance in holomorphic dynamics and operator theory](https://arxiv.org/abs/1509.01363) | Corollary 11 | Theta-Carleson measure weighted integrals of nonnegative psh functions; not the decomposition theorem. |
| [Toeplitz operators and Carleson measures in strongly pseudoconvex domains](https://arxiv.org/abs/1202.1180) | Corollary 5.21 | Carleson measures and Toeplitz mappings between weighted Bergman spaces; no match. |
| [Local Hölder continuity of solutions of the complex Monge–Ampère equation](https://arxiv.org/abs/2108.08460) | Theorem 1.1 | Local negative subsolutions imply a Hölder-continuous psh subsolution; not Cegrell's decomposition. |
| [The Kobayashi distance in holomorphic dynamics and operator theory](https://arxiv.org/abs/1509.01363) | Lemma 16 | Weighted Carleson-measure equivalence; no match. |
| [Toeplitz operators and Carleson measures in strongly pseudoconvex domains](https://arxiv.org/abs/1202.1180) | Corollary 5.17 | Boundary asymptotics of Toeplitz operators on normalized kernels; no match. |

**Fallback and primary verification:** The same full query was submitted to built-in web search after the arXiv theorem search. The primary 31-page Acta Mathematica PDF above was located and opened. The delegated reference auditor read extracted text and visually inspected the supplied local PDF's physical pages 23 and 2. The exact theorem, dimension, domain context and E_0 definition matched.

ArXiv theorem match: **no**. Web primary match: **yes**. Local primary match: **yes**. Definitions and application: **valid**.

**Critical errors:** none. **Gaps:** none.

### R05. Conditional local assertion: dimension one

**Status:** checked_within_conditional_input. **Kind:** inspected elementary local derivation.

**Sources:**

- [section_general_measure_minimal.tex](/Users/mingchen/Non-Kahler/book/author/section_general_measure_minimal.tex:23): lines 23-28

**Referenced assertion:** For a finite compactly supported non-polar measure tau on a disk, a nonpositive Green potential a with ddc a=tau yields a bounded subharmonic v=exp(a) with tau << ddc v.

**Context and definitions:** This is the n=1 substitute; Cegrell's n>=2 theorem is not used outside its dimension range. The Green potential a can be unbounded, and its negative-infinite locus is polar.

**Application steps:**

1. The finite compactly supported measure has a genuine locally integrable nonpositive Green potential a.

2. For a_M=max(a,-M), the bounded chain inequality and locality imply ddc exp(a_M)>=1_{a>-M}exp(a)tau.

3. The bounded subharmonic functions exp(a_M) decrease to exp(a), hence their Laplacians converge distributionally; the positive right sides increase to exp(a)tau off the polar set.

4. Tau is non-polar, so exp(a)>0 tau-almost everywhere. Thus ddc exp(a)>=exp(a)tau implies tau<<ddc exp(a).

5. The normalization 1+exp(a) lies in [1,2]. No boundedness of a is assumed.

**Critical errors:** none. **Gaps:** none.

### R06. Comparison with the already accepted exponential rooftop barrier argument

**Status:** checked. **Kind:** accepted prior product mechanism; no new external theorem.

**Sources:**

- [section_exponential_rooftop_barrier.tex](/Users/mingchen/Non-Kahler/book/author/section_exponential_rooftop_barrier.tex:47): lines 47-59
- [verification.json](/Users/mingchen/Non-Kahler/research/rethlas/verification/results/exponential_rooftop_barrier_01/verification.json:read): lines read-only verdict and product reasoning

**Referenced assertion:** For genuine possibly unbounded s_(j,b) with theta+ddc s_(j,b)>=delta omega_(psi_j), the extended measure dominates delta^n omega_(psi_j)^n, because the comparison holds at finite local levels and the bounded reference product ignores poles.

**Context and definitions:** The earlier proposition has model/relative-class/volume hypotheses for its other steps, but those hypotheses are not needed for this positive-product implication. The present proposition builds s from its own explicitly assumed smaller-background envelope.

**Application:** The audited local carrier inequality is the same finite-level positive-product mechanism with bounded ddc v_i as the reference factor. Extra poles of s are removed using non-pluripolarity. No model, PVP, exponential order, envelope noncollapse, or class membership assertion of that earlier proposition is imported.

**Critical errors:** none. **Gaps:** none.

### R07. Decreasing convex sums and their fixed-summand remainders

**Status:** checked. **Kind:** local standard decreasing-limit convention.

**Sources:**

- [chapter_compactness.tex](/Users/mingchen/Non-Kahler/book/author/chapter_compactness.tex:39): lines 39-43

**Referenced assertion:** A decreasing sequence in PSH(X,theta) with uniformly bounded L1 norms has a genuine theta-psh limit and converges to it in L1.

**Context and definitions:** The limit must be prevented from collapsing to -infinity; formal infinite sums alone do not ensure genuineness or canonical representatives.

**Application:** Both psi_N and w_(k,N) have explicit lower bounds by phi minus a finite constant and upper bounds by phi<=0. These give the required uniform L1 control. The fixed-summand identity is passed from finite combinations, avoiding undefined subtraction at common poles.

**Critical errors:** none. **Gaps:** none.

### R08. Radon--Nikodym invocation

**Status:** checked. **Kind:** explicitly accepted measure-theoretic prerequisite.

**Referenced assertion:** If a sigma-finite positive measure mu is absolutely continuous with respect to a sigma-finite positive measure nu on the same measurable space, then mu=f nu for a nonnegative measurable f; if mu is finite then integral f dnu=mu(X)<infinity.

**Context and definitions:** The theorem requires sigma-finiteness of the reference, not finite total mass. Here both measures are on the Borel sigma-algebra of X.

**Application:** The proof establishes mu<<MA_theta^ext(psi), proves sigma-finiteness from a countable finite-level cover plus a null pole set, and uses finite mu to obtain f in L1. All hypotheses hold.

**Critical errors:** none. **Gaps:** none.

### R09. Final paragraph: limitation of bounded subsolution theorem

**Status:** checked. **Kind:** internal theorem statement checked only for scope.

**Sources:**

- [section_bounded_subsolution.tex](/Users/mingchen/Non-Kahler/book/author/section_bounded_subsolution.tex:61): lines 61-72

**Referenced assertion:** The bounded subsolution theorem assumes a bounded theta-psh reference psi and a bounded nonnegative density with respect to its MA measure.

**Context and definitions:** The present ordinary-type carrier can be unbounded; bounding a relative difference does not meet the absolute boundedness hypothesis. Only the stated hypotheses were inspected; this theorem is not applied.

**Application:** The final paragraph correctly rules out an automatic application to the constructed carrier and correctly says that density truncation supplies no prescribed-type equation existence. No external theorem is invoked in support of a positive existence assertion.

**Critical errors:** none. **Gaps:** none.

## Failed checks and unresolved issues

- **Critical errors:** none.
- **Gaps:** none.
- **Unresolved mathematical issues inside the accepted scope:** none.
- **External dependency retained:** the exact local carrier assertion remains the agreed conditional input; completion of its separate global-section audit is not asserted.

The initial memory initialization and one reference append each encountered an automatic-review timeout. Each succeeded on its permitted single retry. These were persistence events, not proof defects.

## Final scope check

The proposition provides a measure representation. Bounded relative difference does not make the carrier absolutely bounded. The bounded subsolution theorem requires an absolutely bounded reference, and truncating the density does not provide an existence theorem in the prescribed ordinary type. The closing paragraph states this limitation correctly.

## Artifacts and preservation

The full statement checks, reference checks, failed-check summary, verification reports and events are persisted through MCP under the current run. This readable report and JSON exports are written through MCP. The final contractual JSON is written with write_verification_output.

Only the current run's new memory and result artifacts are written. The book sources and prior results are read-only.

**Repair hints:** none required.
