# Individual threshold equations from Gauduchon moments

This review concerns the additions prepared after checkpoint 63. The conditional equation theorem does not assume bounded mass or positive lower mass. It retains two explicit additional hypotheses: a uniform first-moment bound along one smooth maximizing Gauduchon sequence, and genuineness of a smaller-background envelope of the greatest normalized threshold subsolution. Neither hypothesis is asserted to follow from a positive threshold or root tails alone. No novelty claim is made.

## Closure and a greatest normalized subsolution

The new L1 closure lemma preserves a lower density inequality, even if the Monge–Ampère masses are infinite. After an almost-everywhere extraction, take the infima of the density tails and the canonical suprema of the potential tails. For a fixed tail, successive finite maxima have the common density lower bound by ordered contact. They have a genuine lower barrier and a common upper bound, so their convergence holds in capacity. Exponential damping passes the inequality to the canonical supremum. A second monotone capacity passage gives the inequality for the L1 limit. The density-tail infima are bounded by the limiting L1 density almost everywhere, which supplies domination in both passages. Division is only on finite potential sublevels; the pole set carries neither measure.

This independent lemma now shortens the attained-threshold proof. The bounded-truncation solutions have densities converging in L1 to bf, so normalized compactness and the closure lemma attain b directly. This is proof reuse of the same upper-envelope argument, not a new continuity assertion for the original top-degree measures.

The normalized threshold-subsolution family is compact in L1 and stable under finite maxima. A Choquet sequence therefore constructs its greatest member Phi_f. Normalization is retained because this envelope lies between a normalized member and zero. The same closure lemma makes every normalized exponential cluster limit a threshold subsolution, hence at most Phi_f. The proposition does not assert that Phi_f is an exact solution or has finite mass.

## The new sufficient condition

Normalize each smooth positive Gauduchon test T_j by integral omega wedge T_j = 1. Its determinant-weighted density p k_Tj has mass d_j tending to R=b^(-1/n); dividing by d_j gives a probability nu_j. Assume the integrals of -v against nu_j are bounded by C, uniformly over j and all normalized omega-psh v. Apply the unbounded trace inequality to an exponential solution and use Jensen. Passing j to infinity gives

    b <= c_lambda <= b exp(C lambda).

The comparison with the greatest exponential solution then gives Phi_f-C <= v_lambda <= 0. Any L1 cluster limit v belongs to the threshold family, so Phi_f-C <= v <= Phi_f. In particular its ordinary type is exactly that of Phi_f; this is the hypothesis that a bare lower barrier would not establish.

Assume P_{delta omega}(Phi_f) is genuine for some delta between zero and one. The equation measures are dominated by the single finite measure b exp(C) f dV for lambda <= 1. L1 convergence makes the bounded exponential discrepancy tend to zero in measure and hence in integral against f dV. The previously proved lower-barrier criterion now gives capacity convergence, with every one of its hypotheses checked. Damped continuity and L1 convergence of the right sides identify the exact equation for v. This proves existence and finiteness. It does not identify all normalized solutions or give convergence of the whole exponential family.

Uniform Lq control, q>1, of the probability densities is a simple sufficient moment condition. A following elementary calculation also shows that uniform entropy suffices: use uniform exponential integrability of normalized quasi-psh functions, apply t log t-t+1 >= 0 to a probability density relative to exp(-alpha max(v,-T))/Z_T, and then let T increase. Truncation precedes the entropy calculation, so integrability of the desired potential moment is a conclusion rather than an assumed step. This last paragraph is checked directly in the editorial review; the independent submission below covers the closure, greatest-subsolution and conditional equation theorem with its Lq specialization.

## Dependency and integration checks

The closure lemma uses only ordered contact, normalized compactness and the already proved damped capacity continuity. It does not use the attained-threshold theorem that now follows from it. The greatest normalized subsolution uses that theorem, and its assertion about exponential cluster limits uses the later exponential corollary; this is a forward reference with no circular proof dependency. The Gauduchon moment theorem is placed after the unbounded trace inequality in Chapter 27 and reuses the lower-barrier criterion in Chapter 13. Chapter 32 records the additional hypotheses and leaves the unrestricted question open.

All previous labels and result statements are preserved. The new closure lemma and proposition are proved separately so they can be reused without repeating upper-envelope constructions. The first layout review identified two separated introductory lines and displays; their paragraph breaks were adjusted. The final build and selected-page checks are recorded in the checkpoint audit.

## Related literature checked

[Le–Nguyen–Trinh, arXiv:2603.26406v1](https://arxiv.org/html/2603.26406v1), dated 27 March 2026, was checked against the primary full text. Its Theorem 3.1 concerns uniformly bounded potentials converging in capacity. Theorem 3.3 additionally assumes invariance of bounded total mass. Its Theorem 4.1 assumes domination by the measure of a smooth subsolution; that domination gives a bounded density relative to a smooth positive volume. These statements do not settle the present unbounded individual-threshold question. No result from this paper is used as an input in the new proof. The [journal record](https://articles.math.cas.cz/10.21136/CMJ.2026.0476-25) gives online publication on 22 June 2026. The bibliographic search is a scope check, not an exhaustive priority determination.

## Independent check and remaining boundary

The submitted proof is frozen in research/rethlas/verification/inputs/gauduchon-moment-threshold.md, run gauduchon_moment_threshold_01. The completed report returns correct, with no critical errors or gaps, conditional on the stated accepted inputs. It covers the closure lemma, greatest normalized subsolution, conditional equation theorem and its Lq and bounded-envelope sufficient cases. The entropy paragraph was added afterward and checked directly as described above. The research TeX drafts preserve the submitted arrangement; the final book moves the closure lemma before threshold attainment, reuses it in that proof, and adds the entropy paragraph and layout adjustments. No verifier memory, result or frozen input is edited manually.

The two sufficient hypotheses suggest separate research tasks: control moments of near-optimal Gauduchon tests, and establish smaller-background noncollapse for Phi_f. The construction itself does not show either at zero lower mass. Root-tail approximation, singular-current regularity, divisor realization and positive-volume recovery remain distinct questions.
