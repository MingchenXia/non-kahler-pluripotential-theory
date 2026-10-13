# a5k audit of r5g01 (preface, conventions, chapter_framework through sec:analytic-types; base cae12da)

## Verdict
r5g01: **CORRECT AFTER FIXES**. The only fix makes the uniformity of the constant in `lem:bounded-reference-trace` part of its statement, as the assignment asked. I found no mathematical error introduced by the pass.

## What I checked
- **11 hypothesis removals:** prop:convexity; lem:strict-set-positive-volume; lem:bounded-reference-trace; eq:global-capacity-tail; b locally bounded in the prop, thm and thm; thm:small-pole-local-products and lem:small-pole-residual-invariance; lem:common-bound-zero-measure. I also checked the 6 standing-assumption restatements that were deleted.
- **2 rigor fixes:** "connected" and "nowhere dense".
- **4 duplicate removals:** the zero-cluster theorem merged into the bounded-background one; the Dirac proposition; the proof of lem:local-vague-metric; the bounded-background construction.
- **5 simplified proofs:** 2 GZ17 citations and 3 shortened by citation.
- I also ran the math diff over all 22 files. Every removed or added display is one of the listed changes.

## Priority items
- **Cluster-set merge.** The b=0 case of thm:bounded-background-cluster-sets gives everything the deleted theorem stated:
  - closed F gives smooth bounded u_j≤0 tending to 0 in every L^p and in local capacity, because u_j−b is bounded and smooth when b is smooth;
  - conversely, such u_j are locally bounded, so condition (2) gives that F is closed.
  - The label and the "full cluster sets" `\index` entry moved. The only `\cref` of the old label is in chapter_history l.43. Neither subsection label has any reference.
  - The merged proof is complete: closedness of tails in the metric of lem:local-vague-metric; concatenation of a dense sequence; the empty case; the j-th step of thm:local-prescribed-excess applied to the positive excess ν_j−(dd^c b)^n, with errors 2/j and capacity bounds C/j that do not depend on the measure; the d_v comparison.
  - lem:local-vague-metric now cites the earlier proof of thm:local-prescribed-excess (the choice of f_i and the atomic approximation). Neither of those uses boundedness of Ω. Not circular.
- **prop:smooth-dirac-concentration.** The case b=0, ν=cδ_a gives u_j≤0 with u_j bounded and smooth, and (dd^c u_j)^n→cδ_a, plus L^p and capacity convergence; the parameters match. The proof of the theorem uses prop:local-one-atom-addition, lem:smooth-logarithmic-ridge, lem:ridge-lower-degree-limit, lem:local-mixed-cln-trace and thm:bt-input, none of which uses the proposition. So the forward citation is not circular. I rechecked the H_δ computation that moved into the one-atom proof: the density m!/π^m·δ²/(s+δ²)^{m+1}, the ball mass (ρ²/(ρ²+δ²))^m, and the exponents ε^{(n−r)/(n−1)}c^{(r−1)/(n−1)}.
- **GZ17 citations.**
  - Theorem 3.18 (printed p. 87) needs: T closed positive of bidegree (p,p); decreasing sequences of psh functions with limits in PSH∩L^∞_loc; p+q≤n. With T=1 (p=0) and q=r≤n, this is exactly the psh case, including top degree. GZ17's dd^c=(i/π)∂∂̄ gives the factor 2^r on both sides.
  - The quasi-psh extension is correct. After expanding, the A_j-terms converge by GZ17 wedged with fixed smooth forms. The terms with the correction f converge by the decreasing continuity in thm:bt-input. C^∞-convergent factors are handled by the CLN mass bounds (C^0 convergence would already suffice).
  - Lemma 2.28 (p. 54) ends: "if a psh function is bounded from above in C^n, then it is constant".
  - The errata file has no entry on either result. C2-M02 concerns the κ_{2n} constant in §2.3.1 and does not affect the Liouville conclusion.
- **b locally bounded.** The data of b enter only through ‖b‖_{L^∞(L)}, via lem:local-mixed-cln-trace (the choice of γ). The perturbation h does not depend on b, and the intermediate potentials are b plus a bounded function. "u_j−b bounded and ≤0" follows from Σh_{j,s}. The lemma lem:capacity-limit-measure-floor already allowed locally bounded b. Callers: the Dirac proposition (b=0) and history only.
- **Small poles.** DemCADG III Thm 4.5 and Prop 4.9 (checked in the text) need H^{2p−2m+1}(L(u_{j1})∩…∩L(u_{jm})∩Supp T)=0. With T=1 and p=n, m≤q≤n, the needed dimension is ≥1, so H^1(S)=0 suffices; the case n=1 is fine too. The residual-invariance proof uses only the theorem, locality and {a=−∞}=S, never pluripolarity of S or dimension zero. cor:closed-current-hausdorff-null needs H^{2(n−j)}≥H^2 and is unaffected. The downstream users (small_pole_envelope_residual, diffuse_product_polar_obstruction) assume Hausdorff dimension zero, which is stronger, so they still apply.
- **lem:bounded-reference-trace without θ≥0.** For a general smooth θ: a Hermitian Ω≥θ exists; θ_v and θ_ψ are positive because v and ψ are θ-psh; Ω_ψ≥θ_ψ; Stokes holds for bounded v; thm:normalized-compactness holds for every smooth θ; the case n=1 gives C=∫θ.
- **Remaining items, all correct:**
  - eq:global-capacity-tail: Chebyshev works for every t>0.
  - prop:convexity: the proof already omits zero terms, so a=b=0 gives 0∈PSH(X,0).
  - lem:strict-set-positive-volume: a real c with a(x)<c<b(x) exists, since b(x)<∞.
  - lem:common-bound-zero-measure: the uniform local bound implies L^∞_loc.
  - "connected": lem:uniform-exponential needs X connected, and the only use is on P^n.
  - "nowhere dense": every caller applies the lemma to divisors, hypersurfaces or points. The proof's "not all identically zero" works on connected local neighborhoods.
  - The deleted remarks (preface mass sentence, singularity-types intro, positivity remarks, the "In particular" in cor:nonclosed-analytic-approximation) are not cited anywhere and do not change scope.

## Fix made (section_psh_global_capacity.tex, lem:bounded-reference-trace)
- Statement: "There is a constant $C_\psi$ such that" → "There is a constant $C_\psi$, depending only on an upper bound for $\|\psi\|_\infty$, such that".
- Proof: "The first term on the right is bounded independently of $v$." → "The first term on the right does not depend on $v$; since $\theta\leq\Omega$, it is at most the mass of $\Omega\wedge\Omega_\psi^{n-1}$."
- Proof, added before the last sentence: "The same expansion and the range estimate \eqref{eq:local-cln-range} bound the mass of $\Omega\wedge\Omega_\psi^{n-1}$ by $C(1+\|\psi\|_\infty)^{n-1}$."
- Reason: the second-term bound C(1+‖ψ‖_∞)^n(1+‖v‖_{L^1}) was already in the proof; only the first term lacked an explicit dependence.

## Proposals for files outside the part
- **section_holder_reference_equation.tex l.38.** Replace "The trace bound in \cref{lem:bounded-reference-trace} is uniform for references with a fixed supremum norm, as its proof shows." with "By \cref{lem:bounded-reference-trace}, the trace bound is uniform for references with a common bound on their supremum norms." The \hat v_l converge uniformly to u, so their sup norms are bounded in common.
- **chapter_history.tex.** I endorse r5g01's replacements for l.823 (GZ17 Theorem 3.18), l.43 (the case b=0 of thm:bounded-background-cluster-sets) and l.29 (zero one-dimensional Hausdorff measure). The l.41 proposal needs a check against Qin's Theorem B, which I could not do.

## Compile
- `chapcheck.sh a5k preface conventions chapter_framework`: no errors, overfull boxes or undefined references.
- The only message is the allowed Underfull (badness 1783) in section_psh_polar_invariance, which is not in this part.
