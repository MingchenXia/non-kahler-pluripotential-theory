# Hermitian dual entropy and the general-measure program

This revision adds two-sided entropy estimates for the Hermitian zero-reference dual H_0 and reorganizes the general-measure discussion in Chapter32. It makes no novelty claim. The proposition is restricted to a Hermitian background, reference zero and a smooth probability volume; it is not asserted for an arbitrary singular reference.

## Proof check

For every q>1, the lower Lq density estimate for a bounded normalized solution gives B_0(G)>=log c_q-(1/q)log integral exp(qG)dV, with c_q independent of the continuous logarithmic density G. Subtracting the supremum of the solution does not change its measure. For the opposite bound, fix one smooth Gauduchon metric and normalize its trace against omega to one. Matrix arithmetic-geometric mean and Stokes give exp(B_0(G)/n) integral exp(G/n) k_gamma dV<=1 for smooth G, with k_gamma=(gamma^n/dV)^((n-1)/n). Its smooth positive minimum gives B_0(G)<=-n log m-n log integral exp(G/n)dV. Uniform approximation of G and Lipschitz continuity of B_0 extend this to continuous G. No global mass bound is used.

Add the linear pairing with a probability and take suprema in both inequalities. The substitutions F=qG and F=G/n give the entropy coefficients 1/q and n. The logarithmic-truncation variational entropy calculation is measure-theoretic; its use does not import the closed-background identity for H_0. The argument includes absolutely continuous probabilities of infinite entropy. If the probability is not absolutely continuous, the earlier dual compactness theorem already gives H_0=infinity. There is no subtraction of two infinities. In dimension one the exact formula H_0=log integral omega+entropy and nonnegative entropy on a probability volume give the conclusion directly.

Fixing q=2 identifies the finite domain and the uniformly bounded families. In particular dual sublevels have uniformly bounded entropy. The proposition neither identifies H_0 with entropy plus a constant on a nonclosed background nor gives a fixed Lp bound on arbitrary dual sublevels.

Rethlas run hermitian_dual_entropy_01 returned correct, with no critical errors or gaps. Its report checks the exponents, normalization, dimension one, infinite values and uniformity. The final proof shortens its last paragraph without changing its mathematical steps, keeping the entropy variational calculation and both infinite-value cases. The submitted proof and result are preserved unchanged.

## Exposition and integration

Chapter15 and both of its original nested sources were reread at statement-to-proof scale, together with the lower-density estimate and the new proposition. The moment criterion in Chapter27 now notes that uniform entropy of its test probabilities is equivalent to a uniform H_0 bound. This identifies an existing sufficient condition; it does not remove the smaller-background envelope hypothesis.

Chapter32 was reread and its general-measure section reorganized: the two global existence regimes and their different compactness mechanisms come first, followed by the individual threshold problem, its known regimes and its remaining obstacles. The distinction between density-maximizing tests and threshold-minimizing tests in the bigness problem remains intact. Every previous result reference in the rewritten section is retained, with one new reference to the entropy proposition. All ten complete problem and conjecture blocks in the edited chapter source are byte-identical, not merely their labels. The carrier and interface-mass caveats remain at the end of the existence discussion. No formal problem is silently settled or weakened.

The reversible map records the exact edits and word counts. The first page check found a split at the final sentence of the new proof; shortening that paragraph improved its ending. The final compile, selected-page inspection, source preservation and clean reconstruction are recorded in the checkpoint audits. The house audit has no new diagnostic. This is a targeted follow-up, not a new whole-book certification.

## Further direction

The entropy comparison suggests studying H_0-entropy on the finite-entropy domain. A separate draft investigates whether its infimum and supremum are log v_- and log v_+. That draft is not part of this release or of the Rethlas report above. General singular-reference entropy comparison, geometric noncollapse, singular-current regularity and the unrestricted positive individual threshold equation remain open here.
