# Verification report: geometry_problem_connections_repair_01

## Verdict and scope

**Correct relative to the stated accepted inputs: zero critical errors and zero gaps.**

The final **Proof** block is the audited manuscript. The earlier unrepaired copy in the input is background for this targeted repair. The six research problems are proposed targets, not assertions to prove. This report checks literature attribution, exact definitions, applications, and claimed deductions; it does not certify novelty or independently re-prove the cited research papers.

The prior audit’s only recorded error has been repaired. The manuscript now uses Dang’s **almost analytic singularities**, gives the intersection definition of the non-Hermitian locus, invokes the attainment theorem, and retains both conditions from Definition 2.8. The former NUMA condition is discharged by the passed `degenerate_nonuniqueness_01` audit.

The verification read all prior statement and reference records and both prior output files. A manual comparison of the two supplied manuscript versions found the changed opening Dang paragraph; the remaining manuscript is unchanged. Positive prior checks were retained only under the user’s explicit authorization and were supplemented by independent primary-source checks. The present audit records the material in manuscript order, with **64 individual checks** in seven ordered records (scope plus six subsections).

## Accepted inputs and boundaries

The accepted inputs are the Gauduchon root volume and its nth power, smooth Monge–Ampère duality and first variation, nef continuity, density comparison, bigness implying positive variational volume, the Gauduchon bigness threshold and collapse criterion, determinant subcritical estimates and the exact endpoint theorem, and the normalized Hopf calculation.

The persisted JSON verdicts for `smooth_cone_flow_01`, `big_continuous_contact_01`, `local_homogeneous_dirichlet_01`, and `degenerate_nonuniqueness_01` were read and are **correct**. The continuous-obstacle and local homogeneous inputs supply their stated elliptic conclusions. They do not import general unbounded contact, unrestricted moving non-pluripolar-product proofs, a general nef-positive-volume-to-bigness theorem, or general parabolic estimates.

## The repaired definition: direct comparison

The archived primary text is **Dang, Hermitian null loci, arXiv:2404.01126v2**, with arXiv margin date **17 June 2026** and internal manuscript date **18 June 2026**. These are different date fields of the same archived version.

Definition 2.8 on printed page 6 requires a coherent ideal sheaf \(\mathcal I\), a constant \(c>0\), and both of the following:

\[
\varphi=c\log\!\left(\sum_j|f_j|^2\right)+g,
\qquad g\text{ bounded locally},
\]
and, on a suitable global modification obtained by finitely many blowups with smooth centers and with a normal-crossing effective divisor,
\[
\varphi\circ\pi
=c\sum_\ell a_\ell\log|g_\ell|^2+h,
\qquad h\text{ smooth}.
\]

The repaired paragraph preserves the distinction between the **bounded remainder downstairs** and the **smooth remainder on the resolution**. Describing the logarithm of the ideal norm rather than its square changes only the unspecified positive coefficient.

Definition 2.9 identifies a Hermitian current with a current dominating a Hermitian metric, matching “strict current.” Definition 2.12 on printed pages 7–8 takes the intersection over **all such currents with almost analytic singularities**. Theorem 2.14 on page 8 attains the intersection by one current of that same type, and consequently makes the locus analytic. The manuscript now states this correctly. Analyticity of the locus does not change the singularity condition on the potential. [Primary source](https://arxiv.org/pdf/2404.01126v2).

The intrinsic definition of bigness on analytic subvarieties is preserved as well: §2.3 uses forms and currents on complex spaces via local embeddings; Definition 3.1 uses intrinsic bigness of the restricted background. The manuscript does not replace this by an unproved resolution-based definition.

## Sequential verification

### Scope and introductory paragraph

1. The final Proof block is the operative repaired manuscript; the earlier unrepaired copy is context, not a second assertion to certify.

2. Read the previous complete statement_checks, reference_checks, verification report and JSON. They contain one Dang singularity-definition defect, no other reported issues.

3. Compared the prior and final manuscript in textual order: only the opening Dang definition paragraph changes. Retention of positive prior checks is explicitly authorized.

4. Accepted the listed book results without re-proving them; verified correct JSON verdicts for smooth_cone_flow_01, big_continuous_contact_01, local_homogeneous_dirichlet_01 and degenerate_nonuniqueness_01.

5. Questions and conjectures are proposed targets. No general unbounded contact, moving non-pluripolar product, nef-positive-V-to-big implication, or unrestricted parabolic estimates are assumed.

**Finding:** no critical error or gap.

### 1. Nef classes, bigness and the Fujiki class

1. The definition of Fujiki class is bimeromorphic equivalence with a compact Kähler manifold. DP04's current is CLOSED and strictly positive, not an arbitrary nonclosed big background.

2. DP04 arXiv Theorem 0.6 and Conjecture 0.7 have the cited numbering. The conjectural input is a closed real nef (1,1) class with positive top intersection.

3. Bigness of alpha implies class C by the closed Kähler-current characterization. Conversely class C plus closed nef alpha and positive top intersection gives bigness by the standard class-C nef criterion (pull to a Kähler modification, apply the nef-and-big criterion and push the strict current down).

4. GL22 Theorem 4.9 equates bigness and BMP under exactly the closed-nef positive-intersection assumptions. This does not assert BMP universally. Finiteness of \(v_+\)(h) is independent of the chosen Hermitian metric.

5. BGL25 Theorem C uses positive upper volume of a closed Bott-Chern class together with BMP. This volume is not \(\mathcal V_\mu\)=\(\lambda_\mu\)^n.

6. The Hopf upper-mass failure alone lacks the closed nef positive-top-intersection hypothesis needed to refute DP04. Conversely GL22 shows why BMP must follow if that geometry forces bigness.

7. Both displayed bridges remain questions in the unrestricted setting. In the Kähler closed-nef setting the volume formula and nef-big criterion apply. Every strictly Hermitian h has positive \(\mathcal V_\mu\) by the accepted smooth theory (also h is big), so nonclosed positivity cannot characterize class C.

8. The numbered problem requests two missing steps; it does not assert either. For positive lambda, duality gives numerator(alpha,gamma)>=lambda \(D_\mu\)(gamma). After trace normalization, along a threshold-minimizing sequence with \(D_\mu\)>=delta>0 this yields kappa_h(alpha)>=lambda delta>0, hence bigness by the accepted threshold criterion.

9. Rescaling a Gauduchon metric achieves integral h wedge gamma^(n-1)=1 in dimensions at least two; the complex-curve case is already Kähler and elementary. No determinant bound is obtained merely by this normalization.

10. Aeppli-preserving changes of gamma^(n-1) preserve pairing with a closed (1,1) alpha by integration by parts; they need not preserve pairing with nonclosed h. Thus changing density does not furnish the missing normalized determinant estimate.

**Finding:** no critical error or gap.

### 2. Positive lower volume as an endpoint estimate

1. Universal positive lower volume and bounded upper mass are distinct properties. The accepted Hopf normalization gives \(v_-\)=6 while \(v_+\)=infinity.

2. GL22, BGL25 and XZ26 are cited only for the scoped claim that those sources do not settle unrestricted PVP, not for an exhaustive novelty or latest-literature certification.

3. For n>=2 and the stipulated smooth probability dV, the exact accepted endpoint theorem applies to Gamma_0(T)=k_T dV for trace-normalized positive \(dd^c\)-closed Gauduchon currents.

4. The exact supremum is \(v_-\)(h)^(-1/n), with infinity when \(v_-\)=0. Therefore positivity is equivalent to finiteness of the endpoint supremum. The accepted subcritical estimates require neither PVP nor BMP.

5. The proposed endpoint problem retains positivity, \(dd^c\) T=0 and trace normalization. It is not a theorem being asserted.

6. Trace bounds on arbitrary positive matrices do not imply determinant-density endpoint control; scalar matrix concentrations show why a differential restriction matters. Uniform bounds or compactness at smaller exponents alone do not force a critical-exponent bound.

7. An unbounded endpoint sequence in the same normalized Gauduchon class makes the exact supremum infinite and hence \(v_-\)=0. Unbounded upper MA masses do not do so: the Hopf example already has them with finite endpoint norm.

8. Universal PVP, if proved, removes only that metric hypothesis from theorems using it. It does not remove independent BMP, geometry, singularity or measure assumptions.

**Finding:** no critical error or gap.

### 3. Null loci and the singularities of the Chern--Ricci flow

1. Repaired Definition 2.12: \(E_{\mathrm{nH}}\)(theta) is the intersection of Sing(T) over ALL strict currents T=theta+\(dd^c\) phi with almost analytic singularities. Source Definition 2.9's Hermitian current means T dominates a Hermitian metric, exactly strict positivity here.

2. Definition 2.8(i): phi=c log(sum |f_j|^2)+g locally for a coherent ideal, c>0 and bounded g. 'Positive multiple of the logarithm of an ideal norm' is equivalent up to the harmless factor of two for the norm versus its square.

3. Definition 2.8(ii): on a global proper modification by finitely many smooth-center blowups with normal-crossing divisor, phi o pi=c sum a_l log|g_l|^2+h with h smooth. The repaired sentence retains this condition and does not claim the downstairs bounded remainder is smooth.

4. Theorem 2.14 applies with bigness alone and attains the intersection by a strict current with the SAME almost analytic singularities. Analyticity is a conclusion about the singular set, not a replacement of the potential's singularity definition.

5. Section 2.3 defines positivity and bigness on analytic spaces intrinsically via local embeddings, forms and currents. Definition 3.1 unions all positive-dimensional irreducible analytic V with theta|V not big; no arbitrary-resolution substitute is used.

6. Theorem 1.1 requires theta nef AND big on compact complex X, permits nonclosed theta and imposes no BMP. The stated qualitative identification and later conditional use have those hypotheses.

7. The description of Theorem A records its extra HX volume hypotheses. It is not a complete stand-alone theorem statement or an assertion that HX alone implies bigness: the source also requires nef theta and positive \(\widehat v_-\)(X,theta), and no use in this manuscript omits these.

8. Theorem C's positive limiting lower volume is \(\widehat v_-\)(X,theta_tau), not \(\mathcal V_\mu\). Its finite-time requirement and the alternatives n=2 arbitrary omega_0 or n>=3 with \(dd^c\) omega_0=0 and d omega_0 wedge dc omega_0=0 are preserved.

9. The accepted finite-current-lifetime theorem gives nefness of theta_tau and existence of normalized annihilating currents at finite maximal time. For every such current the stated pairing is zero.

10. The accepted nef-annihilator determinant theorem gives vanishing determinant-weighted measure when \(\mathcal V_\mu\)(theta_tau)>0. This does not imply vanishing trace or analytic concentration: a smooth rank-deficient semipositive matrix may have positive trace on an open set.

11. The flow problem asks for volume-to-bigness and convergence; it proves neither. If bigness is obtained then nefness plus Theorem 1.1 identifies the exceptional analytic locus.

12. Continuous-obstacle contact and homogeneous replacement yield the accepted elliptic continuity away from analytic barrier poles; they do not by themselves give parabolic estimates.

13. Context only: Dang Theorem 4.3 already proves smooth local convergence under bigness of the limiting form using parabolic estimates. The manuscript's boundary statement about what its elliptic inputs establish does not claim this conditional literature result is unknown; no novelty is certified.

**Finding:** no critical error or gap.

### 4. Degenerate densities and uniqueness

1. Read the passed degenerate_nonuniqueness_01 JSON. The former conditional prerequisite is fulfilled, including smooth P3 construction, strict Hermitian background, normalized distinct solutions, smooth nonzero density with an open zero band, and bounded mass.

2. A Hermitian background is itself a smooth strict current with empty singular set (the unit ideal gives allowed almost analytic singularities), so \(E_{\mathrm{nH}}\) is empty. Its restrictions are intrinsically Hermitian on analytic subvarieties, so the background null locus cannot detect the example's density degeneration.

3. On compact Kähler P3, any smooth Hermitian h is bounded above by C omega_FS; for bounded h-psh u, C omega_FS+\(dd^c\) u >= h+\(dd^c\) u >=0, so determinant monotonicity and closed-class mass give a uniform upper bound. This verifies the bounded-mass consequence independently of nonclosedness of h.

4. Two smooth normalized solutions are both in the ordinary minimal singularity type for a Hermitian background. Hence that type plus existence does not select a canonical potential.

5. A canonical assignment needs a specified, well-defined selection rule. Nonuniqueness of some potentials does not erase the accepted smooth positive-data scalar or volume invariant.

6. The empty-interior-zero-set question is not answered by an example with a nonempty open zero band; specifying bounded solutions is a legitimate sharpening of the source question.

7. The vanishing-parameter limit question is separate from fixed-positive-parameter uniqueness: uniqueness of each member does not imply convergence as the parameter tends to zero or identify a unique limit.

8. A finite continuous F on compact X has strictly positive e^F (indeed a positive minimum). The example's f=0 on an open set gives log f=-infinity there, so it cannot refute the finite-continuous-log-density adjoint conjecture.

**Finding:** no critical error or gap.

### 5. Balanced and pluriclosed metrics

1. Balanced is d beta^(n-1)=0; pluriclosed is \(dd^c\) omega=0. FV26 Conjecture 1.1 allows different metrics and is used only as a conjecture.

2. For the same metric, balanced plus pluriclosed forces Kähler: in n=2 balanced already means closed; in n>=3 the primitive torsion identity together with \(dd^c\) omega=0 and d omega^(n-1)=0 forces the torsion norm to vanish. This says nothing about two distinct metrics.

3. Chiose Theorem 0.2 requires both class C and a pluriclosed positive metric. Producing a CLOSED strict positive current gives class C by DP04, and the already assumed pluriclosed metric then gives Kählerness. A nonclosed big background would not suffice.

4. Distributional differential operators obey d \(dd^c\) u=0, so d(omega+\(dd^c\) u)=d omega. Fixed-background scalar potentials cannot remove nonzero torsion. Smooth solvability does not alter this identity.

5. The weaker Gauduchon condition \(dd^c\) gamma^(n-1)=0 does not imply balancedness d gamma^(n-1)=0. Positivity or a scalar normalization cannot supply the missing differential constraint.

6. For any exact real two-form d a, Stokes and balancedness give integral d a wedge beta^(n-1)=0. Thus exact flow components vanish in this pairing.

7. FV26 Conjecture 1.2 assumes balanced existence, c1(X)=0 and an initial pluriclosed metric; it proposes long-time flow and a smooth Kähler limit rather than proving it generally.

8. The invariant conserved balanced-trace illustration is a source-supported special setting. A finite integrated trace alone allows concentration and small eigenvalues, so it is not a pointwise ellipticity estimate.

9. The proposed geometry/flow/determinant questions remain targets. The section asserts no general passage from integral trace and scalar positivity to local metric bounds.

**Finding:** no critical error or gap.

### 6. Morse inequalities and the choice of volume

1. Tosatti26 is explicitly a recent preprint, not a reconstructed book theorem. Its displayed inequality concerns Vol(alpha-beta) for closed nef classes alpha,beta on compact Kähler X.

2. Corollary 1.2's differentiability and cone-duality consequences stay in the same closed Kähler setting. The section does not claim an unrestricted Hermitian extension.

3. GL22 Theorem 4.12 is a qualitative bigness criterion under BMP and the strict inequality alpha^n>n alpha^(n-1).beta for closed nef classes; it is not substituted for the quantitative Tosatti bound.

4. For nonclosed representatives, integration by parts leaves \(dd^c\) of background wedge powers; total intersection expressions need not be invariant under \(dd^c\) potential changes.

5. Upper class volume and finite \(\mathcal V_\mu\) have distinct definitions and possible finiteness behavior. Neither is identified with the other or with a moving intersection product.

6. A positive representative at every point of the segment places the entire path in the accepted smooth cone. Smooth MA duality provides a Gauduchon minimizer, and the accepted first-variation formula gives derivative - integral eta wedge gamma_s^(n-1) / \(D_\mu\)(gamma_s).

7. Integrating that derivative by the fundamental theorem of calculus gives exactly the displayed subtraction identity, with the negative sign and no extra n factor because this is \(\lambda_\mu\), not \(\mathcal V_\mu\).

8. Under gamma_s -> a gamma_s both numerator and \(D_\mu\) scale by a^(n-1), so the quotient is independent of scale. The smooth-cone argument invokes no upper MA mass bound.

9. If the integrand is bounded above by M, the identity gives \(\lambda_\mu\)(theta-t eta)>=\(\lambda_\mu\)(theta)-Mt. Passing to a degenerate nef endpoint needs the proposed further cost control and accepted nef continuity.

10. Concavity provides the tangent UPPER bound, not the lower bound needed to retain positive root volume. Positive endpoint root volume implying bigness remains a question.

11. The final divisorial discussion records only the accepted finite residual-volume viewpoint and explicit tests; it does not claim a general moving product or birational volume formula.

**Finding:** no critical error or gap.

## Reference verification and provenance

The required arXiv-first workflow was preserved. For unchanged references, the prior run’s persisted records document the dedicated theorem search followed by primary-web checking; those records were read and retained, with fresh inspection of the archived primary statements. Fresh dedicated searches were run for the repaired Dang definitions/attainment statement, the scoped lower-volume claim, and the conditional flow theorem used as contextual cross-check.

The fresh dedicated searches returned no exact matches. In particular, the result about **gentle analytic singularities** had additional rationality, smooth-exponential, and Kähler-modification hypotheses, so it was rejected as a substitute for Dang’s definition. A lower-volume result with a fixed oscillation bound was also rejected as a resolution of the unrestricted infimum. A flow result with bounded mass and uniform noncollapse was rejected as an exact match for Dang’s conditional bigness theorem.

Built-in primary-web searches followed those searches. The Dang primary PDF text was accessible; its versioned abstract page and attempted screenshots returned cache misses. The permitted archived primary text supplied the exact definitions and formulas. The Xia–Zhang primary arXiv result confirms that XZ26 is an **upper-mass** counterexample. The full local sources, rather than an absence of search hits, determine applicability.

| Source | Exact version and passage | Application checked |
|---|---|---|
| DP04 | arXiv math/0105176v2, 24 September 2001; Theorem 0.6 and Conjecture 0.7; text lines 156–168 | Closed Kähler current/class-C characterization; closed-nef positive-top-intersection conjecture. The corresponding published numbering differs. |
| GL22 | arXiv 2106.04272v2, 2 March 2023; Theorems 4.9 and 4.12; text lines 1254–1258 and 1281–1288 | Exact closed-nef intersection hypotheses and BMP equivalences. The bibliography key is not a claim that v2 was dated 2022. |
| BGL25 | Published source, DOI 10.1007/s42543-025-00105-2; Theorem C; text lines 136–158 and 206–211 | Closed Bott–Chern class volume and BMP. Upper/lower class volumes coincide in this closed setting under BMP; neither is identified with the book’s variational invariant. |
| DangNull26 | arXiv 2404.01126v2, 17 June 2026; Definitions 2.8, 2.9, 2.12, 3.1; Theorems 2.14, 1.1, A, C | Exact repaired singularities, intrinsic restricted bigness, nef-and-big hypothesis, and separate lower-volume/BMP/flow conditions. |
| NUMA | User-supplied full six-page PDF; Theorem A, p.1; no printed author/date asserted | Smooth projective-space counterexample and its open density-zero band. Passed prerequisite supplies the audited construction and bounded mass. |
| Chiose14 | Specified author manuscript, Theorem 0.2, text lines 34–36; published Proc. AMS 142 (2014), 3561–3568 | Class C plus a pluriclosed metric implies Kähler. |
| FV26 | arXiv 2606.03176v1, 2 June 2026; Conjectures 1.1–1.2 and invariant trace discussion, text lines 27–37, 55–58, 102–123 | Different balanced/pluriclosed metrics allowed; flow conjecture retains balanced existence, c1=0 and pluriclosed initial data. |
| Tosatti26 | arXiv 2608.30153v1, 31 August 2026; Theorem 1.1 and Corollary 1.2, text lines 48–52 and 72–88 | Recent preprint’s closed-nef compact-Kähler inequality and consequences. |
| XZ26 | arXiv 2608.21053v1, 21 August 2026; text lines 60–70 | Failure of bounded upper mass, not resolution of universal positive lower volume. |

All **nine PDF SHA-256 hashes** match the supplied source manifest. The verified entries are saved in `source_manifest.json` beside this report.

### Context about the conditional flow step

Dang’s Theorem 4.3 on printed page 19 already supplies smooth convergence off the non-Hermitian locus **when the limiting background is big**, using parabolic estimates. This is compatible with the manuscript’s statement that the book’s elliptic contact arguments alone do not provide those estimates. The unresolved volume-to-bigness implication is not silently assumed. The present verdict makes no novelty claim about a conditional step already present in the literature. [Primary source](https://arxiv.org/pdf/2404.01126v2).

## Issue ledger and conclusion

- Prior critical error: replacing almost analytic singularities by analytic singularities in Dang’s locus definition.
- Disposition in this run: **resolved** by the corrected definition and verified attainment theorem.
- New critical errors: **none**.
- New gaps: **none**.
- Conditional NUMA prerequisite: **fulfilled**.
- Repair hints: empty, as required for a correct verdict.

The manuscript preserves the closed/nonclosed distinction, separates all relevant volume notions, uses the passed book inputs within their scope, and labels proposed mathematical targets as questions. No book file or prior audit output was edited.

