# Verification report: generic_adjoints_01

## Verdict

**Correct.** Every deduction in the supplied new manuscript passes in the accepted book normalization setting. There are **0 critical errors** and **0 gaps**.

## Scope and accepted inputs

The audit follows the supplied text in order. The earlier chapter 14 proofs are accepted and are not re-audited. No book file is edited and no claim in the submitted manuscript is repaired or replaced.

The setting is a fixed normalization regime, with compact metrizable X, the finite concave 1-Lipschitz functional B_phi on C(X,R), nonempty weakly compact convex supporting-probability sets A_phi(F), the stated closed graph property, and the exact one-sided derivative formulas. The standard compactness, Riesz, separability, Baire, and elementary concavity facts expressly permitted in the prompt are used with their hypotheses checked below.

The Hermitian closing sentence is interpreted in its existing book context: thm:normalization-gauduchon-recovery identifies the classical smooth adjoint probability with the member of A_0 at the same smooth logarithmic density. Its statement and normalization were inspected as evidence of applicability; no new PDE existence input was introduced.

## Main checks

The proof's derivative orientation is correct. For a concave restriction b and s<t,

\[
b'_-(t)\ge b'_+(t),\qquad
b'_+(s)\ge\frac{b(t)-b(s)}{t-s}\ge b'_-(t).
\]

Consequently the nonempty intervals (b'_+(t),b'_-(t)) at nondifferentiability points are pairwise disjoint. Choosing the first rational in each interval from a fixed enumeration gives an injection into the rationals. At a differentiability point, the accepted derivative formulas give

\[
w_h(F+th)=b'_-(t)-b'_+(t)=0.
\]

The countable Baire intersection is exactly the singleton locus. The identification uses the unit-mass estimate

\[
\left|\int h\,d\nu-\int h\,d\eta\right|
\le 2\|h-h_{j_\ell}\|_\infty\longrightarrow0
\]

when the h_j integrals agree. Nonemptiness is used when passing from at most one supporting probability to a singleton.

## Sequential deduction audit

The following 13 records contain 43 individual deduction checks. Their sequence follows the manuscript.

### 1. sec:generic-adjoints — introductory scope and uniform topology

**Status: passed.**

1. **Fix the background/reference regime and work on all of C(X,R) with its uniform norm.** This is exactly the supplied domain and accepted finite concave 1-Lipschitz functional. No restriction to smooth densities, positivity cone in F, or changing regime is introduced.

2. **Generic uniqueness is weaker than uniqueness at every continuous density.** This is a scope statement to be established by the ensuing proof. Concavity does not generally imply uniqueness everywhere. For example, on any compact X containing distinct x,y, B(F)=-max(F(x),F(y)) is finite concave and 1-Lipschitz, with multiple supporting probabilities at a tie. This diagnostic is not an assertion about a particular normalization regime.

### 2. thm:generic-adjoint-uniqueness — width definition and attained extrema

**Status: passed.**

1. **nu -> integral_X h dnu is weakly continuous.** This is the definition of weak convergence of probabilities on compact X for continuous real h.

2. **The maximum and minimum in w_h(F) exist.** A_phi(F) is nonempty weakly compact by accepted input, so both continuous extrema are attained.

3. **w_h(F)>=0 and is finite.** Each integral lies in [-||h||_infinity,||h||_infinity] because nu has mass one. Thus 0<=w_h(F)<=2||h||_infinity.

### 3. thm:generic-adjoint-uniqueness — upper semicontinuity of width

**Status: passed.**

1. **Choose maximizing and minimizing probabilities along F_n -> F.** Both extrema exist; countable choices need no measurable-selection theorem.

2. **Extract a subsequence realizing limsup w_h(F_n), then simultaneous weak limits.** Widths lie in [0,2||h||_infinity]. P(X)xP(X) is compact metrizable, so a common further subsequence gives limits nu^+,nu^- and retains the same width limit.

3. **The weak limits belong to A_phi(F).** Apply the accepted closed graph property to each sequence of probabilities.

4. **limsup w_h(F_n)<=w_h(F).** Weak convergence of the two integrals identifies the limsup with integral h dnu^+ minus integral h dnu^-, bounded by the maximum minus minimum over A_phi(F). The sequential criterion suffices because the uniform topology on C(X,R) is metrizable.

### 4. thm:generic-adjoint-uniqueness — open width sets and line reduction

**Status: passed.**

1. **{F:w_h(F)<epsilon} is open for epsilon>0.** Strict upper sublevel sets of an upper semicontinuous real function are open, with the sign of semicontinuity and strict inequality correctly matched.

2. **If h=0 the width set is dense.** w_0 vanishes identically, so the set is the entire Banach space.

3. **For h!=0, fix F and a radius r>0 and consider b(t)=B_phi(F+th) for all real t.** All F+th remain in the accepted domain C(X,R). Since B_phi is finite and concave, its restriction to this affine line is finite and concave.

4. **The one-sided derivatives of b are finite.** The 1-Lipschitz bound on B_phi gives |b(t)-b(s)|<=||h||_infinity |t-s|. Elementary concavity yields both one-sided derivative limits, and this bound makes each finite with absolute value at most ||h||_infinity.

### 5. thm:generic-adjoint-uniqueness — countable nondifferentiability

**Status: passed.**

1. **Order the one-sided derivatives correctly.** For a finite concave b, b'_-(t)>=b'_+(t). For s<t, concavity of secant slopes gives b'_+(s)>=(b(t)-b(s))/(t-s)>=b'_-(t). These inequalities also show each one-sided derivative is nonincreasing.

2. **Nondifferentiability corresponds exactly to a nonempty interval I_t=(b'_+(t),b'_-(t)).** Both derivatives are finite; equality is precisely existence of the ordinary two-sided derivative.

3. **The intervals I_t at distinct nondifferentiability points are disjoint.** For s<t, every element of I_s is greater than b'_+(s)>=b'_-(t), while every element of I_t is less than b'_-(t). Touching endpoints cannot create overlap of these open intervals.

4. **There are at most countably many nondifferentiability points.** Fix an enumeration of Q and assign to t the first rational in nonempty I_t. Disjointness makes this assignment injective into Q. This verifies the provided proof directly; it does not import a generic-differentiability theorem.

### 6. thm:generic-adjoint-uniqueness — density of the width sublevel set

**Status: passed.**

1. **Choose a differentiability point t arbitrarily close to zero.** The exceptional set is countable, while every nonempty real open interval is uncountable. For a prescribed ball B(F,r), choose such t with |t|<r/||h||_infinity.

2. **F+th lies in the prescribed ball.** ||F+th-F||_infinity=|t| ||h||_infinity<r.

3. **Differentiability of b at t gives w_h(F+th)=0.** The difference quotients for b(t+s)-b(t) are exactly those for B_phi at F+th in direction h. Hence w_h(F+th)=b'_-(t)-b'_+(t)=(-min integral h)-(-max integral h)=0. The signs and direction agree with the accepted formulas.

4. **The set {w_h<epsilon} is dense.** For epsilon>0 its zero-width point belongs to every prescribed ball. Constant nonzero h also causes no exception: the same line argument applies.

### 7. thm:generic-adjoint-uniqueness — countable Baire intersection

**Status: passed.**

1. **Choose a countable uniformly dense family (h_j) in C(X,R).** Compact metrizability of X implies separability of real continuous functions in the uniform norm, an expressly allowed standard fact.

2. **Each O_jk={F:w_hj(F)<1/k} is open and dense.** Apply the two preceding width arguments for h=h_j and positive epsilon=1/k.

3. **The intersection over j,k>=1 is a dense G_delta.** The index set N x N is countable and C(X,R) is complete in the uniform norm. Baire therefore gives density; a countable intersection of open sets is by definition G_delta. Completeness supplies the required hypothesis.

### 8. thm:generic-adjoint-uniqueness — exact identification of the intersection

**Status: passed.**

1. **At a point in the intersection, w_hj(F)=0 for every j.** Each nonnegative width is less than 1/k for every positive integer k, hence is zero.

2. **Every pair nu,eta in A_phi(F) has equal h_j integrals.** Both integrals lie between the same maximum and minimum, which coincide because the width vanishes.

3. **Equality extends to every continuous h.** Choose h_{j_l}->h uniformly. Then |integral h dnu-integral h deta|<=2||h-h_{j_l}||_infinity+|integral h_{j_l}dnu-integral h_{j_l}deta|=2||h-h_{j_l}||_infinity->0. The two unit masses justify this bound.

4. **A_phi(F) is a singleton.** Uniqueness in Riesz representation identifies nu=eta. Its accepted nonemptiness upgrades at most one element to exactly one.

5. **Conversely a singleton lies in the entire intersection.** All widths of a singleton vanish, so every strict inequality 0<1/k holds. Thus the displayed intersection equals U_phi, rather than merely being a residual subset of it.

### 9. thm:generic-adjoint-uniqueness — Gateaux derivative

**Status: passed.**

1. **At F in U_phi, B_phi is Gateaux differentiable.** For every fixed h both accepted directional derivatives equal -integral h dnu_F, giving the two-sided directional limit.

2. **The derivative is a bounded linear functional of h.** Linearity follows from integration, and |integral h dnu_F|<=||h||_infinity. This is the stated Gateaux conclusion; no estimate uniform in varying directions, hence no Frechet conclusion, is asserted.

### 10. cor:generic-adjoint-approximation — arbitrary choices and weak convergence

**Status: passed.**

1. **Arbitrary nu_j in A_phi(F_j) are available.** The accepted nonemptiness holds at each continuous F_j; no consistency or uniqueness at F_j is required.

2. **Every subsequence has a weakly convergent further subsequence.** All terms are in the single compact metrizable probability space P(X), which is sequentially compact.

3. **Each such limit is the unique nu_F in A_phi(F).** Every selected density subsequence still converges uniformly to F. Closed graph stability gives membership, and F in U_phi gives equality with nu_F.

4. **The full sequence converges weakly to nu_F.** If it failed to converge, some weak neighborhood of nu_F would be avoided infinitely often. That subsequence has a further subsequence converging to nu_F, contradicting eventual membership in the neighborhood. This verifies the compactness-and-unique-cluster-point inference.

### 11. Closing paragraph — Hermitian background and zero reference

**Status: passed.**

1. **Interpret the classical Gauduchon adjoint probabilities as supporting probabilities for the same B_0.** The preceding chapter's thm:normalization-gauduchon-recovery explicitly states A_0(H)={mu_u} for smooth H, theta=omega Hermitian, phi=0, with dmu_u=rho_u omega_u^n, dd^c(rho_u omega_u^(n-1))=0 and mu_u(X)=1; for n=1 it gives mu_u=omega_u/integral omega_u. This fixes the exact measure and normalization meant by the closing sentence. Source: inputs/normalization-functional.md:214-221. This uses the existing smooth identification in the book normalization setting; its earlier proof is not reopened.

2. **Apply the corollary to smooth F_j -> F uniformly.** Smooth approximation of continuous real functions on a compact smooth manifold is standard. The existing smooth normalization theory provides the classical probabilities, and its identification places each in A_0(F_j). For F in U_0, the proved corollary forces all of them to converge weakly to the unique member of A_0(F). No convergence of potentials or new PDE existence theorem is inferred.

3. **The limit is uniquely determined across choices of smooth approximations.** Every such sequence has the same limit nu_F; it depends only on the fixed regime and F.

### 12. Closing paragraph — exact scope of the conclusion

**Status: passed.**

1. **A dense G_delta need not contain every continuous function.** Residuality and equality with the whole space are different assertions. The proof establishes precisely the former, with no implication that every density belongs to U_phi.

2. **The argument does not establish Frechet differentiability or a weak linearized operator at a solution.** The derivative proof supplies limits for each fixed direction and a bounded linear integration functional. It contains neither a uniform-in-direction remainder estimate required for Frechet differentiability nor any construction or verification of a linearized PDE operator. The stated limitations are accurate.

### 13. Full manuscript — use of assumptions and bounded audit scope

**Status: passed.**

1. **All hypotheses needed for the new functional-analytic deductions are accounted for.** Compact metrizability yields sequential compactness of probabilities and separability of C(X). Nonemptiness and weak compactness give extrema and selections. Unit mass gives bounded widths and uniform-approximation estimates. Closed graph stability is used for upper semicontinuity and the corollary. Concavity and the Lipschitz bound justify finite one-variable derivatives. The directional formulas relate zero width to line differentiability and identify the final derivative. The Banach property gives Baire.

2. **Unused geometric structure and convexity introduce no hidden gap.** Connectedness, complex structure, the detailed reference hypotheses, and convexity of each A_phi(F) are not independently needed for the abstract deductions after the accepted properties of B_phi and A_phi are granted. Their role is upstream in the fixed normalization regime. Smooth manifold structure and the earlier smooth identification enter only the Hermitian specialization.

3. **No unsupported strengthening or external-paper result is used.** The proof concerns all continuous logarithmic densities in one fixed regime at a time and arbitrary supporting-probability sequences there. It asserts no common residual set over uncountably many regimes, no global BMP, no new PDE solvability, no novelty, and no linearized-operator result.

## Reference audit

All internal references were compared with the accepted inputs and the earlier chapter's statement text. The new manuscript cites no external-paper theorem, lemma, or definition, so the required arXiv-first/web-fallback procedure has no applicable target.

### 1. Section setup — eq:normalization-reference

**Referenced statement:** Retain the fixed background and reference hypotheses eq:normalization-reference.

**Evidence:** inputs/normalization-functional.md:14-19

**Context and definitions:** The book fixes the geometric background and model reference, including P_theta[phi]=phi and P_{epsilon theta}(phi) not identically -infinity for some 0<epsilon<1. The accepted functional properties apply on C(X,R) in the chosen regime.

**Application check:** No background or regime changes during the proof.

### 2. Width semicontinuity and corollary — prop:weak-adjoint-stability

**Referenced statement:** If F_j -> F uniformly and nu_j is in A_phi(F_j), every weak cluster point of nu_j belongs to A_phi(F). If A_phi(F) is a singleton, nu_j converges to it.

**Evidence:** User accepted inputs; inputs/normalization-functional.md:178-182

**Context and definitions:** A_phi is defined by B_phi(G)<=B_phi(F)-integral(G-F)dnu for all continuous G. Weak convergence tests continuous functions.

**Application check:** All extracted densities still converge uniformly. Compact metrizability gives the needed weak subsequences. Both applications exactly match this accepted statement.

### 3. Density and derivative — prop:normalization-directional

**Referenced statement:** For continuous F,h, B'_+(F;h)=-max_A integral h and B'_-(F;h)=-min_A integral h. A singleton A_phi(F) gives the bounded linear Gateaux derivative h -> -integral h dnu.

**Evidence:** User accepted inputs; inputs/normalization-functional.md:192-201

**Context and definitions:** The derivatives use positive and negative increments in the same direction h, respectively.

**Application check:** For b(t)=B_phi(F+th), the width at F+th equals b'_-(t)-b'_+(t). Signs, directions, and continuous-function domain coincide with the accepted input.

### 4. Closing Hermitian sentence — thm:normalization-gauduchon-recovery

**Referenced statement:** For theta=omega Hermitian, phi=0, smooth H and its smooth normalized solution u, A_0(H)={mu_u}, dmu_u=rho_u omega_u^n, dd^c(rho_u omega_u^(n-1))=0, mu_u(X)=1. For n=1, mu_u=omega_u/integral omega_u.

**Evidence:** inputs/normalization-functional.md:214-221; smooth approximation consequence at line 233

**Context and definitions:** This earlier book statement identifies the classical Gauduchon adjoint probability with the supporting probability for the same B_0 and A_0.

**Application check:** The closing sentence has exactly Hermitian background, zero reference, and smooth approximating densities. The existing smooth identification puts these probabilities into A_0(F_j), so the new corollary applies. The earlier theorem's proof and PDE existence are not re-audited.

### 5. Complete new manuscript — standard facts and external-paper inventory

**Referenced statement:** Standard compactness, Riesz, separability, Baire, and elementary one-variable concavity are expressly allowed.

**Evidence:** User accepted inputs

**Context and definitions:** For compact metric X, P(X) is weakly compact metrizable and C(X,R) is a separable Banach space. Continuous integrals determine probabilities. Baire applies to countably many open dense sets.

**Application check:** All standard hypotheses were verified sequentially. The nondifferentiability-countability argument was checked directly.

**Search disposition:** There are no external-paper citations in the new proof. The required arXiv-first/web-fallback procedure is not triggered. All named references are accepted internal chapter results or expressly permitted standard facts.

## Findings and repair hints

- Critical errors: none.
- Gaps: none.
- Repair hints: none required.

## Artifacts

- Final machine-readable verdict: [verification.json](verification.json).
- Input snapshot: [generic-adjoints.md](../../inputs/generic-adjoints.md).
- Per-deduction and reference records: `memory/generic_adjoints_01/statement_checks.jsonl` and `memory/generic_adjoints_01/reference_checks.jsonl`.
- Run metadata, events, failed-check inventory, and report records are persisted in the corresponding memory channels.

The strict rule is satisfied: both finding lists are empty, so the verdict is `correct`.

