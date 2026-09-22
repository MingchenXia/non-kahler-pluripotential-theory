# Density norms and entropy with prescribed singularities — 22 September 2026

This review follows the Chapter13 prescribed-type existence proof and the Chapter15 normalization dual. It develops one reusable estimate rather than repeating the same strict-domination argument inside several limit proofs. The background remains smooth, semipositive and big. The model reference must admit a genuine envelope in epsilon times the background, with epsilon strictly between zero and one. No metric mass property is assumed.

## Relative lower-density estimate

A potential of the prescribed ordinary type whose extended Monge–Ampère measure is F dV has Lq density norm bounded below for every fixed q>1. The bound is uniform over references sharing the same theta and epsilon.

Zero density is excluded by strict domination applied to u and u+1. For N=norm(F)_q>0, the earlier bounded subsolution lemma in (1-epsilon)theta supplies s with measure at least (b_q/N)F dV. Adding P_{epsilon theta}(phi) gives a genuine theta-psh h more singular than u. Positivity is used on finite truncation levels and then exhausted off a pole set of zero smooth volume. If N<b_q, strict domination would force u>=h+t for every real t. This is impossible at a common finite point. The constant comes entirely from the residual background, not from the reference potential.

The lemma uses neither prescribed-equation existence proof. Applying it to the normalized exponential approximants yields b_p<=c_j norm(f)_p, so their scalar limits are positive before passing to the limiting equation. This replaces the later separate zero-measure contradiction. The existence theorem, relative estimate, capacity argument and scalar uniqueness statement are otherwise unchanged.

## Entropy and varying references

The new lemma gives the scalar lower bound needed for a_q+Entropy/q<=H_phi. For the upper bound, enlarge theta to a fixed Hermitian Omega. Positivity gives MA_Omega(u)>=MA_theta(u). If the prescribed-type scalar exceeded the bounded Omega scalar, strict domination with the bounded Omega solution and arbitrary translates of u would be impossible. Thus B_phi<=B_{Omega,0}, and the already checked Hermitian entropy upper bound applies. The entropy variational formula gives the lower bound, including infinite entropy. Non-absolutely-continuous probabilities have both values infinite by the earlier compact-dual theorem.

For fixed theta and epsilon both constants are uniform over the admitted model references. In particular, uniformly bounded logarithmic densities and arbitrary supporting probabilities for these references give uniformly bounded entropies. The Hermitian upper estimate then places them in a single compact H_{Omega,0} sublevel. Their densities are uniformly integrable; weak limits have finite entropy. This does not identify a limiting supporting set for an arbitrary changing reference.

## Readability and audit scope

The original Chapter13 semipositive bounded-subsolution construction, singular strict domination, relative uniform estimate and both prescribed ordinary-type existence proofs were reread at the actual dependencies. The Chapter15 normalization, dual and entropy arguments were rechecked at the interfaces. The earlier Chapter10 lower-density estimate was also compared. Existing formal theorem statements and labels are preserved. The new density lemma precedes its use; the entropy section now has a shorter title covering both the Hermitian and prescribed-reference subsections.

Rethlas run prescribed_dual_entropy_01 independently checks the lower-density lemma, the entropy corollary, reference uniformity, the revised positive-scalar argument and the varying-reference consequence. Its actual report and scope are recorded in the build audit. The final exposition explicitly names the solution u in the entropy proof, where the submission had referred to it without naming it. A new paragraph and a spacing instruction keep the comparison-barrier definition together at a page break. Neither edit changes a mathematical step. Frozen inputs and original verifier outputs are preserved.

The focused writing audit has zero errors and two inherited chapter-label warnings. Seventeen selected pages cover the new results, both revised interfaces and the affected surrounding proofs. The complete production-versus-preview and clean reconstruction checks are recorded separately.

## Literature boundary

The introduction of [Li, arXiv:2601.13446v1](https://arxiv.org/html/2601.13446v1), dated 19 January 2026, explicitly assumes both bounded mass and positive volume after its introductory survey and discusses stability under changing singularity types. Its result concerns a different ambient regime and stronger solution-level questions. The present deductions concern scalar duals and supporting probabilities under the stated semipositive smaller-background condition. No novelty conclusion follows from the search, and no extra external result is used in these proofs.

## Further work

An independent draft at /private/tmp/section_reference_comparison.tex proposes the more precise comparison B_0+n log(1-epsilon)<=B_phi<=B_0 and its dual version, plus supporting-probability stability when epsilon tends to zero. It is not part of checkpoint68. A proposed example based on arbitrary ordinary envelopes was deliberately not asserted: automatic idempotence of those envelopes must not be assumed outside its established regimes. Analytic singularities have a separately proved envelope theorem that can be used for concrete examples after checking all hypotheses.

Entropy-difference extrema for a general singular reference, arbitrary-reference stability, weak-current regularity and the unrestricted individual zero-lower-mass equation remain separate questions.
