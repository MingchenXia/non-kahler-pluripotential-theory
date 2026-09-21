# Proof verification: big_model_measures_01

## Verdict

**Correct, conditional only on the exact supersolution corollary in item 5.**

Both proofs are correct under the explicitly accepted internal premises, conditional only on item 5: cor:big-relative-supersolution for every nonzero finite NPP measure under the same BMP, arbitrary smooth big real background, and positive-lower-model-volume hypotheses. The sequential audit verifies every exponential-order direction and establishes genuine L1 limits before invoking fixed-dominator continuity. The weighted-mass supremum is attained: bounded-exponential convergence in L1 of the fixed measure and continuous L1 approximation identify MA(w)=exp(w)nu; non-pluripolarity justifies removing the weight across pole sets. The residual supersolution meets the addition theorem's bounded-carrier hypothesis and forces saturation. Nonzero carrier truncations, their decreasing solutions, dominated convergence, simultaneous scaling, and positive-exponent uniqueness all pass. For zero exponent, the coefficients stay uniformly positive, normalization yields a genuine limit in E_phi, and exp(v_j/j) has a common lower curvature bound and converges to one in L1(mu). The retained exponents are exactly 1/j_k, giving total-variation convergence to c mu. Integration gives ell/mu(X)<=c<=M/mu(X); strict domination proves uniqueness of c without asserting normalized-potential uniqueness. The attribution to [XL26, Theorems 6.1–6.2](https://arxiv.org/html/2601.13446v1) is verified. Its conclusions and standing global positive-volume assumption are not imported. No semipositivity or closedness of theta, no independent global PVP, and no ordinary-type conclusion u approximately phi are used. No critical errors or gaps were found.

## Sequential deduction checks

### 1. Section opening / hypotheses

1. Read the proof in its displayed order. The retained hypotheses are BMP, arbitrary smooth big real theta, a model phi of positive lower relative volume ell, finite upper bound M, and a nonzero finite NPP datum mu.
2. E_phi means the authorized every-convex-stretching envelope class, equivalently the upper ordinary-type-volume class under these hypotheses. It is not replaced by the ordinary singularity type u approximately phi, nor by equality of individual raw masses.
3. BMP/bigness/model positivity enter the authorized class, domination, continuity, addition and conditional supersolution results. The numerical lower bound ell supplies anti-collapse and positive scalars; M supplies the final upper scalar bound. No closedness, semipositivity or independent global positive-volume property is introduced.
4. The XL26 citation is attribution of the construction only; both external conclusions remain excluded as premises.

Critical errors: none. Gaps: none.

### 2. thm:big-model-exponential / bounded-carrier case: supersolution and T

1. Under mu<=A sigma with bounded Hermitian carrier, mu is still a nonzero finite NPP measure, so item 5 conditionally supplies an actual Q in E_phi and 0!=nu0=exp(-Q) MA(Q)<=mu. Finiteness follows from domination by mu.
2. The weighted measures vanish on poles. Multiplication back by exp(w), with zero at a pole, recovers MA(w), since MA(w) is NPP.
3. Q belongs to T by equality at the lower end and the supersolution inequality at the upper end; thus T is nonempty.
4. For w in T, exp(-Q)MA(Q)<=exp(-w)MA(w). Weighted order applied with first input Q yields Q>=w, the stated direction.
5. Since MA(w)=exp(w)nu_w and nu_w<=mu, ell<=MA(w)(X)<=exp(sup w)mu(X), so sup w>=log(ell/mu(X)). Also sup w<=sup Q<infinity.
6. A common upper bound for theta-psh potentials together with the displayed uniform lower bound on their suprema excludes the identically minus-infinity compactness alternative. Thus any sequence in T has a subsequence converging in smooth-volume L1 to a genuine theta-psh function, before any fixed-dominator theorem is used.

Critical errors: none. Gaps: none.

### 3. thm:big-model-exponential / maximizing sequence and weak measure limit

1. Every weighted mass in T is at most mu(X), and at least nu0(X)>0. Hence alpha is a finite positive supremum and a maximizing sequence exists by the definition of supremum; no compactness or attainment is presupposed.
2. Apply the preceding anti-collapse argument to select w_j with a genuine L1 limit w.
3. MA(w_j)=exp(w_j)nu_j<=exp(sup Q)mu is one fixed finite NPP raw-measure bound. The authorized fixed-continuity theorem now gives w in E_phi, capacity convergence and raw weak convergence to MA(w).
4. On compact X, the finite measures nu_j<=mu have weakly convergent subsequences. Extract within the potential-convergent maximizing subsequence, so all preceding convergences remain valid.
5. Measure inequalities nu0<=nu_j<=mu pass to the weak limit by testing nonnegative continuous functions and regularity of finite Borel measures; hence nu0<=nu<=mu and nu is NPP.
6. Testing by the constant function 1 gives nu(X)=lim nu_j(X)=alpha.

Critical errors: none. Gaps: none.

### 4. thm:big-model-exponential / fixed-dominator proof of weighted-mass attainment

1. The potentials w_j,w share the finite upper bound sup Q. With theta<=C_omega omega, the convex chain rule gives dd^c exp(w_j)>=-C_omega exp(sup Q)omega. The exponentials are uniformly bounded qpsh functions (zero at poles), and their smooth L1 convergence follows from the exponential's Lipschitz bound on this half-line.
2. The fixed-NPP integration premise applied to mu gives integral |exp(w_j)-exp(w)| dmu -> 0. It is applied to bounded exponentials, never to unbounded potentials in L1(mu).
3. For every continuous test f, replacing exp(w_j) by exp(w) against nu_j costs at most ||f||_infinity integral |exp(w_j)-exp(w)| dmu, which tends to zero.
4. The fixed function h=f exp(w) is bounded Borel. Since X is compact metric and mu is a finite Borel measure, choose continuous h_m with ||h_m-h||_{L1(mu)}->0. Both nu_j and nu are dominated by mu, so each of the two approximation errors is at most this same L1(mu) norm.
5. For a fixed m, integrals of h_m against nu_j converge weakly. Let j tend to infinity and then m tend to infinity. This proves integral f exp(w) dnu_j -> integral f exp(w) dnu without invoking a moving-measure integration lemma.
6. Combine that conclusion with raw weak convergence to obtain MA(w)=exp(w)nu as measures.
7. Because nu<=mu is NPP, nu gives zero mass to the pluripolar set {w=-infinity}; multiplication by exp(-w) is legitimate off that set and gives exp(-w)MA(w)=nu on all X under the pole convention.
8. The inequalities nu0<=nu<=mu place w in T and nu(X)=alpha proves actual attainment of the maximum.

Critical errors: none. Gaps: none.

### 5. thm:big-model-exponential / addition contradiction

1. If mu-nu is nonzero, it is a positive finite NPP measure, since 0<=mu-nu<=mu. The exact conditional supersolution premise therefore supplies v in the same E_phi with nonzero finite nu_v=exp(-v)MA(v)<=mu-nu.
2. MA(v)=exp(v)nu_v<=exp(sup v)mu<=A exp(sup v)sigma. The finite supremum of the genuine qpsh function v ensures a finite carrier constant.
3. Both inputs w,v are in E_phi and the v input has the required bounded-carrier domination. The authorized addition theorem, at exponent one, applies.
4. The addition equation implies exp(-a)MA(a)=nu+nu_v off the union of the three potential pole sets; all measures involved are NPP, so this equality holds globally with the declared convention.
5. nu+nu_v is between nu0 and mu; thus a belongs to T. Its weighted mass is alpha+nu_v(X)>alpha because nu_v is a nonzero positive finite measure, contradicting the supremum.
6. Consequently mu=nu and the attained potential w solves MA(w)=exp(w)mu. This does not assume existence of a maximizer without proving it or assume finiteness of an arbitrary undamped weighted sum.

Critical errors: none. Gaps: none.

### 6. thm:big-model-exponential / arbitrary finite NPP datum

1. The authorized bounded-carrier decomposition gives mu=f sigma with f>=0 integrable and sigma=MA_omega(psi), psi bounded omega-psh. The auxiliary Hermitian metric supplies the semipositive big background required for this lemma, without restricting the target theta or adding a volume hypothesis.
2. For every positive integer k, f_k=min(f,k) is nonnegative bounded, mu_k=f_k sigma<=k sigma, and mu_k is nonzero since integral f dsigma>0 implies {f>0} has positive sigma measure and min(f,k)>0 there.
3. Each mu_k is finite NPP, so the completed bounded-carrier case gives u_k in E_phi with exp(-u_k)MA(u_k)=mu_k.
4. mu_k<=mu_{k+1} and weighted order imply u_k>=u_{k+1}; hence the sequence decreases and has a common finite upper bound sup u_1.
5. The raw lower mass bound and mu_k<=mu give ell<=exp(sup u_k)mu(X), uniformly bounding sup u_k from below. The decreasing theta-psh limit is genuine and convergence holds in smooth L1 by standard monotone compactness.
6. MA(u_k)=exp(u_k)mu_k<=exp(sup u_1)mu provides one fixed finite NPP dominator. Fixed continuity now gives u in E_phi and raw weak convergence.
7. The decreasing canonical potentials converge pointwise to the genuine canonical limit, possibly minus infinity on its polar set. Since f is finite sigma-almost everywhere and f_k increases to f, exp(u_k)f_k converges to exp(u)f sigma-almost everywhere.
8. 0<=exp(u_k)f_k<=exp(sup u_1)f with a fixed L1(sigma) bound. Dominated convergence yields L1(sigma), hence total-variation, convergence of the right-hand measures; monotonicity of their products is not needed.
9. Comparing with raw weak convergence proves MA(u)=exp(u)mu.

Critical errors: none. Gaps: none.

### 7. thm:big-model-exponential / positive scaling and uniqueness

1. For lambda>0, lambda theta is again smooth big real. The simultaneous scaling premise identifies E_{lambda phi} in background lambda theta with lambda E_phi, keeps BMP applicable, and rescales ell,M by lambda^n.
2. lambda^n mu is a nonzero finite NPP measure. The exponent-one theorem in the scaled background supplies U with MA_{lambda theta}(U)=exp(U)lambda^n mu.
3. Set u=U/lambda. Class scaling gives u in E_phi; MA_{lambda theta}(lambda u)=lambda^n MA_theta(u) then yields MA_theta(u)=exp(lambda u)mu.
4. For two solutions, the measure identity MA(u)=exp(lambda(u-v))MA(v) is interpreted off their polar sets, which all data ignore. Equivalently both weighted measures equal mu.
5. Applying weighted order in both directions yields u>=v and v>=u. Explicitly, on {u<v-delta}, MA(u)<=exp(-lambda delta)MA(v-delta), so strict domination gives u>=v-delta; let delta decrease to zero and reverse u,v. Constant shifts remain in the class and their MA measures are unchanged.
6. Thus positive-exponent potential uniqueness is proved in E_phi, with no assertion of ordinary-type bounded difference from phi.

Critical errors: none. Gaps: none.

### 8. thm:big-model-normalized / comparison construction and coefficient bounds

1. The completed exponential theorem applies for every integer j>=1 at lambda=1/j, so each u_j in E_phi actually exists.
2. S=sup u_1 is finite. Constant invariance puts w_j=u_1+(j-1)S in E_phi and MA(w_j)=MA(u_1)=exp(u_1)mu.
3. w_j/j-u_1=((j-1)/j)(S-u_1)>=0 off poles, with both potentials minus infinity at poles. Therefore MA(w_j)<=exp(w_j/j)mu.
4. After weighting, exp(-w_j/j)MA(w_j)<=mu=exp(-u_j/j)MA(u_j). Exponential order yields w_j>=u_j, as stated.
5. sup w_j=j S, hence sup u_j<=j S and c_j=exp(sup u_j/j)<=exp(S), regardless of the sign of S.
6. v_j=u_j-sup u_j belongs to E_phi, has supremum zero, and its MA measure is unchanged. The exact equation becomes MA(v_j)=c_j exp(v_j/j)mu.
7. Since v_j<=0, ell<=MA(v_j)(X)<=c_j mu(X); this proves c_j>=ell/mu(X)>0 and also the fixed domination MA(v_j)<=exp(S)mu.
8. The authorized envelope identity gives v_j<=phi; this uses envelope-class normalization, not ordinary-type bounded difference or boundedness of v_j.

Critical errors: none. Gaps: none.

### 9. thm:big-model-normalized / normalized compactness and fixed continuity

1. The normalized theta-psh family has a fixed lower curvature bound and sup v_j=0. Standard normalized compactness supplies a genuine smooth-volume L1 subsequential limit u with sup u=0; canonical representatives and Hartogs' lemma preserve this normalization.
2. The coefficient interval [ell/mu(X),exp(S)] is compact and bounded away from zero. Take a further subsequence within the potential-convergent one so that c_{j_k}->c>0.
3. Retain the increasing original indices j_k; thus j_k tends to infinity and every earlier expression still has denominator j_k.
4. The hypotheses of fixed-dominator continuity are now met: v_{j_k} in E_phi, genuine theta-psh L1 limit u, and MA(v_{j_k})<=exp(S)mu, one fixed finite NPP measure.
5. The theorem yields u in E_phi, capacity convergence and raw weak convergence MA(v_{j_k})->MA(u). It is not asked to establish noncollapse from a dominator alone.

Critical errors: none. Gaps: none.

### 10. thm:big-model-normalized / bounded exponentials and fixed-measure limit

1. Choose a Hermitian omega0 and C>0 with theta<=C omega0. Then dd^c v_j>=-C omega0, and for h_j=exp(v_j/j), the convex chain rule gives dd^c h_j >=-(C/j)exp(v_j/j)omega0 >=-C omega0. The bound extends to singular v_j using the standard qpsh truncation/composition argument. No truncation is assumed theta-psh when theta is arbitrary.
2. 0<=h_j<=1, including h_j=0 at poles, so these are uniformly bounded qpsh functions with one smooth lower curvature bound. The limit function 1 has the same required lower bound.
3. For real t<=0, 0<=1-exp(t)<=-t. Applying t=v_j/j gives the displayed inequality off poles, and in the extended sense also at poles.
4. Normalized compactness gives a uniform smooth-volume integral bound integral(-v_j)dV<=B; poles are smooth-volume null. Therefore ||1-h_j||_{L1(dV)}<=B/j->0 along the full original sequence.
5. Apply the authorized fixed-NPP lemma directly to h_j and 1, giving ||1-h_j||_{L1(mu)}->0. No assertion that the unbounded v_j converge in L1(mu) is made.
6. Along the retained subsequence, h_{j_k}=exp(v_{j_k}/j_k); the denominator is not replaced by k. The estimate ||c_{j_k}h_{j_k}mu-c mu||_TV <=exp(S)||h_{j_k}-1||_{L1(mu)}+|c_{j_k}-c|mu(X) tends to zero.
7. The total-variation limit of the right-hand measures and the raw weak limit from fixed continuity coincide, yielding MA(u)=c mu.

Critical errors: none. Gaps: none.

### 11. thm:big-model-normalized / scalar bounds and scalar uniqueness

1. u in E_phi and MA(u)=c mu imply ell<=c mu(X)<=M. Since mu(X)>0, division yields ell/mu(X)<=c<=M/mu(X).
2. For completeness, suppose two solutions U,V in E_phi have positive scalars c1<c2. For every real t, V+t preceq phi and MA(U)=(c1/c2)MA(V+t). Strict domination with constant c1/c2<1 implies U>=V+t.
3. Choose a point outside the union of the pole sets of U,V, where both are finite, and let t increase without bound. This is impossible. Interchanging the scalars treats the other strict inequality, so the positive scalar is unique.
4. This arbitrary-translation argument requires neither equality nor uniqueness of normalized potentials. The proof correctly makes no such assertion.

Critical errors: none. Gaps: none.

### 12. Section closing / claimed scope

1. The two constructions prove the stated general-measure equations in E_phi, conditional only on the exact supersolution corollary specified by the user and using the already authorized internal premises.
2. The equations have finite right-hand sides: for positive exponent a fixed genuine potential has finite supremum and mu is finite; for zero exponent c is finite and positive.
3. No step claims u approximately phi. The text correctly separates that stronger relative boundedness assertion for Lp data from the present result and does not rely on it.
4. Full primary sequential audit has found zero critical errors and zero gaps. External attribution remains to be verified in the next required skill.

Critical errors: none. Gaps: none.

## Reference and premise checks

### Section opening / XL26 Theorems 6.1–6.2; thm:big-model-exponential

Reference: XL26 Theorem 6.1

Official source: https://arxiv.org/html/2601.13446v1

Locator: Theorem 6.1, HTML lines 1065–1089; archived P26.txt lines 1911–1963

Theorem search: All five retrieved results concern Lp densities and bounded potentials, not general finite NPP data in a prescribed model-relative class. They do not match the requested theorem.

The official arXiv HTML and local archive verify the attribution after the theorem-search results failed to match.

- The source permits a possibly nonclosed smooth big real (1,1)-form. Bigness is stated using an analytic-singularity potential with theta+dd^c rho>=delta omega_X.
- Source Definition 3.1 requires P_theta[phi]=phi and positive LOWER relative volume; Definition 3.2 requires u preceq phi and equality of UPPER ordinary-type volumes. Here u preceq phi means u<=phi+C, as explicitly defined in Section 2.1; it is not the reverse inequality and it does not mean u approximately phi.
- Upper/lower volumes are respectively sup/inf of raw non-pluripolar MA masses over potentials of the same ordinary singularity type. They are not individual raw masses.
- The official HTML resolves overbars/underbars lost in the archive's plain-text extraction. These definitions match the authorized internal class equivalence, rather than requiring identification by similar terminology.
- The source's introduction globally assumes both BMP and positive volume property. The user authorizes BMP plus positive lower MODEL volume and independent internal reconstructions, with precisely item 5 conditional. The citation is checked as method attribution; these external conclusions are neither imported nor used to bypass that difference.
- A positive Radon measure is finite on compact X; the submitted proof explicitly imposes nonzero finite NPP data, resolving the convention on positivity.


The bounded-carrier supersolution family, weighted-mass maximum, residual addition and carrier truncation do correspond to the cited construction. The source's DDNL25 Lemma 2.5 invocation is not used here: the submitted proof independently proves the needed moving weighted-measure limit by fixed-NPP exponential convergence and density of continuous functions in L1(mu), with the two approximation errors uniformly controlled by nu_j,nu<=mu.


Critical errors: none. Gaps: none.

### Section opening / XL26 Theorems 6.1–6.2; thm:big-model-normalized

Reference: XL26 Theorem 6.2

Official source: https://arxiv.org/html/2601.13446v1

Locator: Theorem 6.2, HTML lines 1091–1101; archived P26.txt lines 1968–1984

Theorem search: The five results concern bounded Lp solutions, weighted energy characterizations, unrelated curvature, or closed Kahler settings. None is XL26 Theorem 6.2.

The official arXiv HTML and local archive verify the attribution after the theorem-search results failed to match.

- The source permits a possibly nonclosed smooth big real (1,1)-form. Bigness is stated using an analytic-singularity potential with theta+dd^c rho>=delta omega_X.
- Source Definition 3.1 requires P_theta[phi]=phi and positive LOWER relative volume; Definition 3.2 requires u preceq phi and equality of UPPER ordinary-type volumes. Here u preceq phi means u<=phi+C, as explicitly defined in Section 2.1; it is not the reverse inequality and it does not mean u approximately phi.
- Upper/lower volumes are respectively sup/inf of raw non-pluripolar MA masses over potentials of the same ordinary singularity type. They are not individual raw masses.
- The official HTML resolves overbars/underbars lost in the archive's plain-text extraction. These definitions match the authorized internal class equivalence, rather than requiring identification by similar terminology.
- The source's introduction globally assumes both BMP and positive volume property. The user authorizes BMP plus positive lower MODEL volume and independent internal reconstructions, with precisely item 5 conditional. The citation is checked as method attribution; these external conclusions are neither imported nor used to bypass that difference.
- A positive Radon measure is finite on compact X; the submitted proof explicitly imposes nonzero finite NPP data, resolving the convention on positivity.


The reciprocal-exponent normalization method and uniqueness of c correspond to the cited construction. The submitted proof proves a positive uniform lower bound for c_j, obtains a genuine normalized L1 limit before fixed continuity, applies the fixed-NPP lemma to bounded qpsh exp(v_j/j), and retains 1/j_k explicitly. It makes no claim of normalized-potential uniqueness.


Critical errors: none. Gaps: none.

### All internal references / premise scope


- /Users/mingchen/Non-Kahler/book/author/chapter_envelopes.tex (def:relative-envelope-class, thm:relative-equivalence): Exact definitions use u preceq phi and nonempty A_b for EVERY b>=1, with A_b={h theta-psh: b^{-1}h+(1-b^{-1})phi<=u}; under BMP, big theta and positive lower phi volume this equals the upper ordinary-type-volume class. These exact premises, not a visually similar class, are used.
- /Users/mingchen/Non-Kahler/book/author/section_big_relative_foundations.tex (eq:big-relative-mass-interval, thm:big-relative-domination, thm:big-relative-fixed-continuity): Statements explicitly allow any smooth big real form under BMP and positive lower model volume, require a genuine L1 potential limit for fixed continuity, and give strict domination in the stated direction. The paragraph following domination gives exponential order and scalar uniqueness, not zero-exponent potential uniqueness. Their uses all match.
- /Users/mingchen/Non-Kahler/book/author/section_relative_compactness.tex (lem:fixed-npp-integrals): The fixed measure must be finite NPP, tested functions uniformly bounded qpsh with a common lower curvature bound and smooth L1 convergence. The upper-bounded-potential exponential corollary is explicit. All three limit uses satisfy these exact hypotheses. Direct L1(mu) convergence of unbounded potentials is never substituted.
- /Users/mingchen/Non-Kahler/book/author/section_general_measure_minimal.tex (lem:bounded-measure-carrier): The lemma is the bounded Hermitian carrier decomposition authorized in item 3. It is distinct from the later relative carrier result with semipositive-background assumptions; those assumptions are not imported.
- /Users/mingchen/Non-Kahler/book/author/section_big_weighted_addition.tex (thm:big-weighted-addition): Same-class u,v and domination of MA(v) by A MA_omega(psi) for a bounded Hermitian potential suffice. The residual supersolution v has precisely this domination. The input weighted sum in this application is finite since it is at most mu; no arbitrary undamped sum is assumed finite. Item 4 and its discharged weighted-limit dependency are accepted exactly as authorized.
- /Users/mingchen/Non-Kahler/research/editorial/section_big_relative_projection.tex (cor:big-relative-supersolution): Read and matched the corollary: for every nonzero finite NPP nu, Q in E_phi exists with 0!=exp(-Q)MA(Q)<=nu. Accepted conditionally only, as requested; its proof and its cross-class rooftop construction are outside this run. Both invocations (initial mu and nonzero residual mu-nu) meet its exact input requirements.

Critical errors: none. Gaps: none.

### lem:bounded-measure-carrier / exact Hermitian specialization

The author lemma is formulated for a smooth semipositive big form. Apply it with that form equal to an auxiliary Hermitian metric omega, which is positive and big (the zero potential is a strict smooth potential). Its result is exactly mu=f MA_omega(psi) with psi bounded omega-psh and f integrable. Semipositivity here is a property of the auxiliary metric, and imposes no semipositivity on the arbitrary target theta. The lemma explicitly needs no upper or lower volume property.


Critical errors: none. Gaps: none.

## Audit boundary

Internal premises 1–4 are accepted exactly as supplied. Item 5 is conditional and was not re-proved. XL26 Theorems 6.1–6.2 are attribution only. The manuscript and submitted source files were read without edits.

## Artifact completeness

12 logical statement records and 4 reference records were checked. Statement record 6 was re-persisted after final storage inspection found its first append absent; the report follows its original logical order. The output JSON schema validation passed.
