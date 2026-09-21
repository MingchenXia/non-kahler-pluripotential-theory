# Verification report: Uniqueness Criteria for Hermitian Monge–Ampère Equations

Run: `uniqueness_criteria_01`

**Strict verdict: correct within the requested scope.** No critical error or substantive gap was found. This is a mathematical correctness audit, not novelty certification.

The audit covers all positive criteria and complete proofs in Sections 1–6: Theorems 1.1–1.5, Lemmas 2.1–2.2, the dense-positive low-dimensional corollary, and the comparison/mass-invariance equivalence. Theorem 1.4 is accepted only for its positive sublevel-volume and inverse-square-root-integrability assertions. Its sharpness claim, the Section 7 construction, and Sections 8–9 are excluded. Introductory statements about those excluded results receive no verdict.

The supplied source was read in its mathematical order. The local input is `inputs/uniqueness-criteria.md`. Neither the manuscript nor the book was edited. Each proof was decomposed into the small deductions below. Independent second readings checked Section 3, Sections 4–5 and the hypersurface topology, and Section 6 with its primary sources. All agree with the master audit.

| Result | Essential inputs checked | Disposition |
|---|---|---|
| Extremal anchors and component criteria | Continuous density; C^{1,1} potentials; semipositivity almost everywhere | Pass |
| Measurable ellipticity and maximum principle | Local essential upper and positive lower coefficient bounds; C^{1,1} strong solution | Pass |
| Weighted cofactor energy | C^2 potentials; continuous positive h with dd^c(hT)=0 | Pass |
| Range-field and bracket propagation | Continuous nonnegative symbol; locally Lipschitz range fields; smooth fields for brackets | Pass |
| Sobolev rigidity | W^{2,n}, n=2 or 3; positive density almost everywhere; threefold covector sign when n=3 | Pass |
| Dense-positive classical corollary | C^2 potentials; continuous density positive densely; same threefold sign | Pass |
| Square-root sublevels | C^{1,1} density; C^2 potentials; stated liminf condition | Pass, positive assertion only |
| Bounded Guan–Li theory | Conditions on the equation form; bounded potentials; nonnegative L^p density, p>1, with positive integral | Pass |

## Sequential statement and proof checks

All items below have `critical_errors=[]` and `gaps=[]`. Ordinary short deductions are expanded where useful; their expansion does not indicate a substantive omission in the manuscript.

### 1. Section 1: standing assumptions, normalization and Theorems 1.1–1.5

1. X compact, connected, without boundary; smooth positive real (1,1) equation form need not be closed; complex n>=1. dd^c=i/(2pi) partial barpartial follows from d^c=i/(4pi)(barpartial-partial).

2. For imported D0=k dd^c, the potential u/k gives the same solution form. Positive common rescaling preserves strict sublevel sets, boundedness and normalization.

3. Even-degree forms commute, so dd^c(u-v) wedge sum A^j B^(n-1-j)=A^n-B^n without closedness.

4. Theorem 1.1 uses C^{1,1} potentials plus continuous density; Theorem 1.2 uses C^2 potentials and an explicitly assumed positive continuous weight only in part (1); Theorem 1.3 uses W^{2,n}, a.e. positive coefficient density, and the threefold sign only when n=3.

5. Theorem 1.4 positive conclusion uses C^2 potentials and C^{1,1} density, distinct regularity assumptions. Sharpness expressly excluded. Theorem 1.5 assumes Guan–Li on the equation form, L^p p>1 and positive density integral.

### 2. Lemma 2.1 (Good contact)

1. The C^{1,1} gradient of g_delta is Lipschitz on the compact ball and maps the full-measure exceptional complement N to a null set, including the null boundary.

2. Choose slope |s|<delta rho outside F(N). The displayed radial quadratic estimate is strictly negative for |x-p|>=rho, so the tilted maximum is interior to B(p,rho).

3. Stationarity F(x)=s excludes N. The second-order upper contact gives D^2 g_delta<=0 and hence D^2g<=2delta I.

4. Rademacher applied to Lipschitz first derivatives supplies a full-measure set of second-order Taylor points.

### 3. Lemma 2.2 (Measurable strong maximum principle)

1. W^{2,infinity}_loc supplies a C^{1,1}_loc representative. Strict weak comparison reduces a hypothetical interior maximum to Good contact and Lb<=2delta tr a<=2delta m Lambda<kappa.

2. A point outside the proper closed maximum set can be chosen sufficiently near its relative boundary to have a positive-distance tangent ball compactly inside the domain.

3. On the annulus, a radial exponential has Lb>=kappa>0 for sufficiently large alpha, by uniform lambda and Lambda bounds.

4. The inner sphere is compact and avoids the maximum set; a small positive perturbation fits both boundary spheres. Strict comparison extends the bound to the annulus.

5. At the tangent maximum the gradient of z vanishes; the exponential has a strictly positive inward first derivative, contradicting the comparison bound. Connectedness concludes.

### 4. Section 2: cofactor comparison and locally uniform ellipticity

1. All mixed terms are nonnegative in covector-testing order. Binomial coefficients lie between 1 and 2^(n-1), giving 2^(-(n-1))H^(n-1)<=T<=H^(n-1).

2. In an H-eigenframe the cofactor eigenvalues are fixed positive multiples of products omitting one eigenvalue.

3. An essential lower bound H>=c beta gives cofactor ellipticity. Conversely, for n>=2 use H<=M beta and a product omitting an index other than a smallest eigenvalue to obtain lambda_min>=c'/M^(n-2).

4. Local coefficient upper bounds follow from C^{1,1} potentials. n=1 is explicitly separated: T=1 is elliptic everywhere, even where H degenerates.

### 5. Theorem 1.1 proof in Section 2: extremal localization and propagation

1. At the smooth perturbed maximum, expansion gives (1+s)B>=A+sC. Since C>0, B>0; common determinant then gives A>0.

2. In the B frame, det J=1 implies tr J>=n. Hence tr K<=n, K<=n I and det K<=1. This proves B>=C/n and B^n>=C^n.

3. For C^{1,1}, Good contact at points x_j->p with D^2g<=2delta_j I gives dd^c g<=delta_j beta0. Thus C_j=C-(delta_j/s)beta0 is exactly the required error and is positive for fixed s and large j.

4. The determinant comparison at x_j passes to p using only continuity of f,dV,C. Uniform convergence of the perturbed functions as s->0 locates an actual maximum in P_chi; swap u,v for the minimum.

5. P_chi is nonempty compact and lies in U because C^n>0. On relatively compact subsets of U, positive determinant and essential coefficient bounds force every A and B eigenvalue uniformly positive, so U subset E_unif.

6. The linearization is a measurable nondivergence equation with positive cofactor symbol on E_unif. Local SMP propagates the global maximum and minimum through their respective components; continuity gives the closure statements.

7. The same proof applies to components of U itself, not merely to E_unif. Unequal extreme values force disjoint closures.

### 6. Theorem 1.1 proof in Section 2: component criteria and connected embedded hypersurface

1. Pairwise closure intersection among anchored components contradicts distinct extreme values. A connected elliptic open locus places both anchors in one component.

2. For an open dense set with two components, closure of the finite union is X. Two disjoint nonempty closures would disconnect X. The one-component case is immediate.

3. Since Z=f^{-1}(0) is closed, an embedded C^1 hypersurface admits flattening neighborhoods with exactly two connected local sides. The unordered pair of ambient complement-component labels is locally constant along Z.

4. Connectedness of Z makes this unordered pair fixed, allowing both labels to coincide and allowing their interchange around a loop. No orientation/coorientation is required.

5. Every component of X minus Z has nonempty boundary in Z: otherwise it is both open and closed in connected X. Near a boundary point it contains a local side. Thus there are at most two complement components.

6. A hypersurface has empty interior, so U is dense. The dense at-most-two criterion applies.

### 7. Section 3.1: weighted cofactor energy and reachable sets

1. The hypothesis is dd^c(hT)=0 in distributions, not d(hT)=0; no existence of h is inferred.

2. C^2 approximation permits the test w^2. With d^c=i/(4pi)(barpartial-partial), dw wedge d^cw=(i/(2pi))partial w wedge barpartial w and dd^c(w^2)=2w dd^cw+(i/pi)partial w wedge barpartial w.

3. dd^cw wedge T=0 cancels the first term. The continuous nonnegative integrand with continuous h>0 has integral zero, hence vanishes everywhere.

4. For positive semidefinite Q, Q(dw)=0 implies the bilinear cross terms Q(dw,eta)=0. This is precisely annihilation by dw of im Q^sharp.

5. The chain rule for C^1 w on absolutely continuous curves proves constancy along every allowed curve. A single dense reachable set suffices; alternatively positive definiteness densely makes dw zero densely and, by continuity, globally.

### 8. Section 3.2: real symbol and exterior-ball normal obstruction

1. The complex Hessian expansion has the stated imaginary cross-term signs. For C_cf=P+iQ, L=Tr(aD^2) with a=(1/(8pi))[[P,Q],[-Q,P]].

2. For a real covector (xi,eta), its (1,0) coefficients are (xi-i eta)/2; thus its cofactor quadratic value equals 2pi times (xi,eta)^T a(xi,eta). Symbol ranges agree exactly.

3. For a nearest point z to y outside K, the ball centered at z+theta(y-z) of radius theta|y-z| has unique contact z. The triangle-inequality equality case verifies this, and sufficiently small theta keeps it in the chart.

4. Assuming positive normal quadratic value, continuity supplies positivity nearby and large gamma gives Lpsi<0 with the displayed sign.

5. On the lens boundary, the tangent-sphere portion has psi=0. The other compact boundary portion avoids K and has uniform negative W-M, so one epsilon fits the whole boundary.

6. A positive interior maximum of W-M-epsilon psi contradicts a>=0 and L(W-M-epsilon psi)>0. Outside the tangent ball psi>=0, so the comparison holds on a full neighborhood of z.

7. Second-order contact yields 0<=LW(z)<=epsilon Lpsi(z)<0. Therefore every exterior normal lies in ker a at the contact.

### 9. Section 3.2: Lipschitz propagation and bracket-generating orbits

1. Since a is symmetric positive semidefinite, ker a is perpendicular to im a. Thus the exterior normal is orthogonal to each range field at a nearest point.

2. Nested compact chart neighborhoods and short flow time keep all nearest points in the chart interior. Fixing such a point to bound the upper Dini derivative gives D^+dist(gamma,K)^2<=2 Lip(Z)dist(gamma,K)^2.

3. Gronwall gives invariance for positive time; -Z gives negative time; continuation gives finite concatenations.

4. Apply to w and -w, both solving L=0. A maximum set is nonempty closed and contains an orbit from every point in it. Every orbit dense therefore implies constancy.

5. The span D_p of all pushed original field values is invariant under original flows. At fixed p, differentiating pushed values keeps the derivative in the finite-dimensional closed space D_p. Induction using invariance and Jacobi includes every iterated Lie bracket.

6. Full bracket rank gives D_p=T_pX. Select a basis of pushed original fields; their conjugate flows stay in the orbit. The successive-flow map has invertible derivative, making each orbit open. Connectedness gives one orbit.

7. No constant-rank assumption or matrix square root is used. Locally Lipschitz columns suffice for flow propagation; brackets are asserted for smooth data only.

### 10. Section 4: Theorem 1.3 Sobolev rigidity

1. C,D have L^n coefficients and top products are L^1 by Holder. Positive common determinant ensures positive definite A,B almost everywhere, so congruence diagonalization and product lambda_j=1 are justified.

2. For n=2, D^2=2(2-lambda1-lambda2)E<=0. For n=3, 2C D^2=A^3+B^3-A^2B-AB^2 and coefficients are 6,6,2sum lambda,2sum pair products. AM–GM gives nonpositivity and equality exactly A=B.

3. Smooth strong W^{2,n} approximations exist and need not preserve positivity. In n=2, D_k^2=d(d^cw_k wedge D_k), so integral zero passes by strong L^2 product convergence. The strict equality case gives D=0 a.e.

4. In n=3 the exact dd^cs_k wedge D_k^2 integrates to zero. With J_k=dw_k wedge d^cw_k, d^cJ_k=-D_k wedge d^cw_k and dd^cJ_k=-D_k^2.

5. The two displayed Stokes identities yield integral C_k D_k^2=-integral J_k dd^comega, with no missing first-order torsion term.

6. Strong L^3 convergence of C_k,D_k gives strong L^1 triple-product convergence; gradient convergence gives J_k->J in L^{3/2}, sufficient against smooth dd^comega.

7. The imposed covector sign and J=(i/(2pi))partial w wedge barpartial w make the last integral nonnegative. Its left integrand is nonpositive, hence zero a.e.; strict equality gives D=0 a.e.

8. Distributional dd^cw=0 gives local distributional Euclidean harmonicity. Convolution and the mean-value property give compatible smooth representatives; compactness and connectedness force a constant.

9. Quasi-psh canonical representatives recover pointwise values from ball averages after adding a sufficiently positive smooth local function. Almost-everywhere constant difference therefore holds pointwise for these representatives.

### 11. Corollary 4.1: continuous density positive on a dense set

1. At degenerate points with common top power zero the remaining expressions are -2AB in n=2 and -A^2B-AB^2 in n=3, still nonpositive.

2. The same exact integrals force the continuous signed forms to vanish everywhere. The strict equality case applies on the positive-density locus only.

3. D=0 extends from the dense positive-density locus by continuity. The threefold sign remains required; dd^comega=0 is sufficient.

### 12. Section 5: positive square-root sublevel assertion of Theorem 1.4

1. The liminf volume/sqrt(t)=0 forces Vol(Z)=0.

2. If a convex coordinate ball minus Z has two components, choose small compact endpoint disks inside them. Their corresponding parallel segments form a compact cylinder in the ball and each must meet Z.

3. Density nonnegativity gives gradient zero at zeros; C^{1,1} density gives f(x)<=K|x-z|^2/2 by integrating the Lipschitz gradient.

4. The compact endpoint disks avoid closed Z, giving a uniform zero-free end margin. For small t every segment has a sublevel interval of length 2sqrt(2t/K).

5. Fubini gives volume>=c sqrt(t) for every sufficiently small t. No measurable selection of a zero is needed because every measurable slice has the indicated length lower bound.

6. Thus each sufficiently small ball has connected nonempty complement. Nonempty open overlaps contain points outside null Z, so component labels agree. Connected X forces one global component of U.

7. C^2 potentials satisfy the C^{1,1} requirement on compact X, so the anchor theorem applies. Integrability of f^{-1/2} forces a null zero set and yields Vol{f<=t}/sqrt(t)<=integral_{f<=t}f^{-1/2}->0 by dominated convergence.

8. The final sharpness reference is outside this audit by explicit user scope.

### 13. Section 6: bounded products and Theorem 6.1 comparison/mass equivalence

1. The bounded omega-psh definition specifies the upper semicontinuous quasi-psh representative and positivity of omega+dd^c a as a current. DK Section 2 supplies local multilinear definition, locality and bounded monotone continuity using a closed dominating form, not a local potential for omega.

2. The even-degree product rule gives dd^c(omega^k)=k omega^(k-1)dd^comega+k(k-1)omega^(k-2)domega d^comega, with the displayed positive torsion sign.

3. For n>=3, powers k=1,2 give equivalence with the first two conditions; higher powers follow from the same formula. For n=2 degree-six expressions vanish and only dd^comega=0 remains. For n=1 all differential conditions are automatic.

4. Chiose Theorem 0.2 is read with its explicit smooth-PSH definition and establishes only the claimed smooth equivalence. DK Propositions 3.1–3.2 and condition (3.1) establish the bounded implications under Guan–Li.

5. Constant shifts making the whole X a strict sublevel set and reversing the pair show ordinary bounded comparison implies equal total masses. Comparing to zero fixes that mass to V. Restriction to smooth tests and Chiose closes the converse.

### 14. Section 6: auxiliary existence, capacity and bounded mixed interfaces

1. DK Theorem 5.2 assumes bounded mass invariance, mass normalization, capacity domination alpha*t/h(t^(-1/n)), and an Orlicz function psi with psi(x)/x increasing to infinity; it concludes a continuous omega-psh solution.

2. For nonnegative G in L^p, p>1, DK Corollary 2.4 gives exponential capacity domination. psi(t)=t^p and h(y)=exp(a0*y) satisfy all requirements including the finite integral of y^(-1)exp(-a0*y/n) from 1 to infinity.

3. The source estimate for compact sets extends to Borel sets by inner regularity of G omega^n, capacity monotonicity, and monotonicity of t exp(-a0*t^(-1/n)).

4. DK and Nguyen use D0=2dd^c; Chiose uses D0=2pi dd^c. Rescaling potentials gives the identical solution forms and preserves strict sublevels and convex mixtures.

5. The unit-test capacities for D and 2D are comparable: cap_D<=cap_2D<=2^n cap_D. For the upper bound, a source competitor phi has D-admissible phi and omega+2Dphi<=2(omega+Dphi). Thus the exponential estimate transfers with changed unspecified constants.

6. Nguyen Lemma 1.9 explicitly permits bounded omega-psh potentials and nonnegative L^1 densities on a Hermitian background, and states exactly the used convex-mixture bound.

7. The indicator-truncated auxiliary density is covered; no density continuity or positive lower bound is required. Existence and mixed inequalities do not presuppose the uniqueness being proved.

### 15. Section 6: domination from bounded ordinary comparison

1. After a common constant shift b<=0. For t||b||_infinity<epsilon, b_t=b+t|b|-epsilon satisfies b-epsilon<=b_t<b; both strict-sublevel inclusions follow.

2. The solution form of b_t is (1-t)omega_b+t omega, so positivity of bounded mixed products gives MA(b_t)>=t^n omega^n.

3. Comparison and MA(a)({a<b})=0 imply zero smooth volume of {a<b-2epsilon}. A countable epsilon sequence gives a>=b almost everywhere.

4. The canonical bounded quasi-psh representatives equal limits of local ball averages, so the inequality holds at every point. No openness of a difference sublevel set is assumed.

### 16. Section 6: restricted-density uniqueness and normalized existence (Theorem 1.5)

1. For equal-density bounded solutions, mass invariance gives mu(X)=V. A nonconstant bounded difference can be centered to have supremum s and infimum -s, with s>0; these extrema need not be attained.

2. The two strict-sign sets are disjoint, so swapping the pair arranges mu(S)<=V/2. Then b0=(V-2mu(S))/V>=0 and G=2F 1_S+b0 is L^p, nonnegative and has integral V.

3. The checked existence theorem supplies rho. Boundedness permits C0>=sup(rho-u), giving q_delta<=u and E_delta subset S.

4. On S, G>=2F. The checked mixed inequality gives MA(q_delta)>=A_delta mu with A_delta=((1-delta)+delta*2^(1/n))^n>1.

5. Ordinary comparison on E_delta and finiteness of mu force mu(E_delta)=0. The independently proved domination applies to a=v,b=q_delta and gives v>=q_delta everywhere.

6. Let delta decrease to zero to get v>=u, contradicting the positive centered supremum. No division by F is used; open zero sets cause no defect.

7. LPT Theorem 3.7 proof and Remark 3.8 verify the methodological attribution and its Hermitian use under ordinary comparison.

8. For I=integral f omega^n>0, c=V/I normalizes the density. Existence supplies a continuous bounded solution; any competing pair has c'=c by mass invariance, and uniqueness of the normalized potential follows.

9. Every bounded solution for this density is continuous because it equals the continuous representative up to a constant. The Guan–Li form here is precisely the equation background.

## Exact external-reference checks

The required theorem-search service was queried first with the full referenced statements. Its results did not give an exact match for the cited interfaces. Built-in web searches with the same statements were followed by direct reading of the primary papers. An unsuccessful search ranking was not treated as evidence that a theorem does not exist. The exact sources below were found and checked. Section 6 search evidence is retained in [section6_reference_evidence.json](section6_reference_evidence.json); its detailed independent audit is [section6_independent_audit.md](section6_independent_audit.md). The book was not needed because the primary interfaces matched directly.

### Sections 1 and 3: Bardi–Goffi attribution

Claim checked: A maximum of a subsolution propagates along locally Lipschitz generalized subunit fields; bracket generation implies a strong maximum principle.

Exact primary location: Definition 1.1, Theorem 1.2, Corollary 1.3, Lemma 2.1, Proposition 2.4, Theorem 2.5. [Primary paper](https://arxiv.org/pdf/1812.09589).

Definitions and hypotheses: For F=-Tr(aX), a>=0, generalized subunit means p·Z!=0 implies p^Tap>0, equivalently Z in im a. This is not a claim of a fixed normalized matrix inequality a>=Z tensor Z. Shift the maximum to zero if needed; linear F is independent of u.

Application: The source normal-orthogonality/exterior-ball method matches. The manuscript independently proves the C^2 linear specialization, Lipschitz flow invariance and smooth orbit argument.

Result: matched and applicable; no critical error or gap.

### Section 6 opening: DK bounded Hermitian products

Claim checked: Bounded omega-psh Monge–Ampere products on a Hermitian background are well defined, positive, local and continuous under bounded monotone convergence, using a closed dominating form locally.

Exact primary location: Section 2, definition and expansion (2.2); locality used in Proposition 3.1. [Primary paper](https://arxiv.org/pdf/0910.3937).

Definitions and hypotheses: DK omega-psh functions are upper semicontinuous quasi-psh current subsolutions. The background need not be closed; the dominating local form has a potential, while omega is not asserted to have one.

Application: The same bounded Hermitian products are used. D0=2dd^c is handled by scaling potentials.

Result: matched and applicable; no critical error or gap.

### Section 6, Theorem 6.1: Chiose Theorem 0.2

Claim checked: On a compact Hermitian manifold, dd^c omega=0 and d omega wedge d^c omega=0, vanishing dd^c omega^k for 1<=k<=n-1, total mass invariance for all smooth omega-psh potentials, and ordinary comparison for every smooth pair are equivalent.

Exact primary location: p.1 smooth definition of PSH(X,g); Theorem 0.2 p.2. [Primary paper](https://arxiv.org/pdf/1609.05945).

Definitions and hypotheses: Chiose uses i partial barpartial and defines PSH(X,g) here as C-infinity functions. Scaling by 1/(2pi) matches the manuscript. Only smooth-test equivalence is imported.

Application: Bounded implications are supplied separately by DK; no substitution of bounded tests into Chiose is made.

Result: matched and applicable; no critical error or gap.

### Section 6, Theorem 6.1: DK Propositions 3.1–3.2

Claim checked: Bounded mass invariance condition (3.1) implies ordinary comparison for all bounded omega-psh pairs. Guan–Li zero differential conditions imply mass invariance and bounded comparison.

Exact primary location: Section 3, condition (3.1), Propositions 3.1–3.2 and intervening Guan–Li paragraph. [Primary paper](https://arxiv.org/pdf/0910.3937).

Definitions and hypotheses: Condition (3.1) explicitly quantifies over bounded potentials. Proposition 3.2 uses an ordered torsion sign condition more general than needed; only its zero case is invoked, unaffected by reversing the two degree-three factors.

Application: The zero conditions are on the same equation omega. Source D0=2dd^c rescales potentials and preserves all masses/sublevel sets.

Result: matched and applicable; no critical error or gap.

### Section 6, auxiliary solvability: DK Corollary 2.4 and Theorem 5.2

Claim checked: Under bounded mass invariance, any nonnegative normalized L^p density, p>1, has a continuous omega-psh solution. Corollary 2.4 provides exponential capacity domination; Theorem 5.2 assumes an admissible capacity weight h and an Orlicz function psi with psi(t)/t increasing to infinity.

Exact primary location: Definition 2.2, Corollary 2.4; admissibility integral in Theorem 4.3; Theorem 5.2. [Primary paper](https://arxiv.org/pdf/0910.3937).

Definitions and hypotheses: Theorem 5.2 is an existence result for possibly discontinuous nonnegative data, with normalization integral G omega^n=V. Choose psi=t^p, h(y)=exp(a0 y); the required integral is finite.

Application: Indicator truncation preserves L^p. The source capacity with D0=2dd^c obeys cap_D<=cap_D0<=2^n cap_D, so unspecified exponential constants change harmlessly. Compact-set domination extends to Borel sets by inner regularity.

Result: matched and applicable; no critical error or gap.

### Section 6, bounded mixed inequality: Nguyen Lemma 1.9

Claim checked: If nonnegative F,G are L^1(omega^n) and bounded omega-psh a,b satisfy MA(a)>=F omega^n and MA(b)>=G omega^n, then MA((1-t)a+t b)>=((1-t)F^(1/n)+tG^(1/n))^n omega^n for 0<t<1.

Exact primary location: Introduction normalization; Lemma 1.9 p.12. [Primary paper](https://arxiv.org/pdf/1501.00891).

Definitions and hypotheses: The lemma explicitly assumes bounded potentials, not continuous ones; densities are nonnegative L^1; omega is Hermitian and the local proof notes the nonclosed background. D0=2dd^c.

Application: The forms and convex mixtures are unchanged by scaling potentials. On S the auxiliary density is >=2F, producing the required strict amplification even when F vanishes elsewhere.

Result: matched and applicable; no critical error or gap.

### Sections 1 and 6: Lu–Phung–Tô restricted-density method

Claim checked: Equal-density uniqueness can be proved by an auxiliary density twice the restriction of the common density to a strict sublevel set plus a normalizing constant, mixing, ordinary comparison and domination. The proof extends to Hermitian metrics satisfying ordinary comparison.

Exact primary location: Proof of Theorem 3.7 pp.12–13; Remark 3.8 p.13. [Primary paper](https://arxiv.org/pdf/2003.08417).

Definitions and hypotheses: The Hermitian extension explicitly retains ordinary comparison. The manuscript reconstructs the method with bounded DK existence, Nguyen mixing, and its own domination argument; it does not import arbitrary-background uniqueness.

Application: The restricted density and all transitions are checked directly, including mass normalization and sets of zero common density.

Result: matched and applicable; no critical error or gap.

## Further checks of signs, hypotheses, and definitions

The manuscript's convention is
\[
d^c=\frac{i}{4\pi}(\bar\partial-\partial),\qquad
dd^c=\frac{i}{2\pi}\partial\bar\partial.
\]
It gives
\[
dw\wedge d^cw=\frac{i}{2\pi}\partial w\wedge\bar\partial w,
\qquad
dd^c(w^2)=2w\,dd^cw+\frac{i}{\pi}\partial w\wedge\bar\partial w.
\]
For real covectors, the cofactor quadratic form is exactly \(2\pi\) times the real principal-symbol quadratic form. The factor \(1/(8\pi)\) and the two off-diagonal signs in the symbol are consistent with the linearized equation and the energy identity.

The threefold integral has the sign
\[
\int_X C\wedge D^2
=-\int_Xdw\wedge d^cw\wedge dd^c\omega.
\]
The right side is nonnegative under the covector sign assumption, while the left integrand is nonpositive by the determinant algebra.

The density regularity in the threshold theorem is separate from the potential regularity in the anchor theorem. The \(C^{1,1}\) density assumption gives a quadratic upper bound at every zero. Almost-everywhere positive density gives the strict matrix equality cases in the Sobolev theorem. The classical corollary replaces it with dense positivity using continuity of the coefficients.

The connected-hypersurface conclusion uses the unordered pair of local-side component labels, which is constant along connected \(Z\). Every complement component has a boundary point in \(Z\) and contains a local side. This covers a one-sided hypersurface and permits the two labels to agree; orientation is unnecessary.

The energy criterion assumes its weight. Distributional \(dd^c\)-closedness permits the single test \(w^2\), without imposing \(d\)-closedness. The weighted criterion controls the gradient everywhere and needs one dense absolutely continuous reachable set. The unweighted argument controls the extreme sets through locally Lipschitz flows and uses the stated condition on every orbit.

In the bounded proof, the equation background itself satisfies Guan–Li. The auxiliary density has exactly total mass \(V\) and lies in \(L^p\); existence is verified before the solution is used. Boundedness is sufficient for the mixed inequality. Difference sublevel sets are Borel and need not be open. Centering the supremum and infimum does not require that a bounded difference attain either value.

The unit-test capacity changes when the differential operator is rescaled. If the capacities for \(D\) and \(2D\) use test potentials in \([0,1]\), then
\[
\operatorname{Cap}_D(E)\leq\operatorname{Cap}_{2D}(E)
\leq 2^n\operatorname{Cap}_D(E).
\]
For the first inequality, send a \(D\)-admissible \(a\) to \(a/2\). For the second, a \(2D\)-admissible \(\phi\) is also \(D\)-admissible, and
\[
0\leq\omega+2D\phi\leq2(\omega+D\phi).
\]
Positivity of bounded mixed products gives the corresponding measure bound. Thus the source's exponential estimate transfers with changed positive constants, whose values the manuscript leaves unspecified. The manuscript does not claim equality of the two capacities.

No unused hypothesis hides a missing argument. Compactness supplies extrema, normalization, finite volume, and finite integral identities; connectedness gives the global conclusions. Positivity and regularity are used at their stated strengths. No closedness assumption is silently inserted into the general-background arguments.

## Findings and strict decision

Critical errors: none.

Substantive gaps: none.

No in-scope claim depends on the excluded sharpness proof, counterexample, or full-mass theory. No unverified external interface remains. The positive assertions in Sections 1–6 satisfy the required strict acceptance rule.

Repair hints: empty.

The machine-readable result is [verification.json](verification.json). The detailed statement and reference records are persisted in `memory/uniqueness_criteria_01/`.

