# Relative envelopes and prescribed equations audit

14 September 2026, continuing the authorized research window. This records a mathematical review, not a formal certificate.

## Authored chapters

- Envelopes and volumes of singularities: definitions, contact inputs, rooftop inequality, finite mass of fixed points without BMP, upper/lower volumes and gauge/scaling invariance, volume monotonicity, adding positive currents, relative full mass and model distinctions.
- Equations with prescribed singularities: bounded subsolution theorem; same-type Lp equations without BMP; general non-pluripolar measures under the exact ALS and Li hypotheses; strict domination, scalar/potential uniqueness distinctions, singular zero-exponent topology and quantitative normalized Lp estimate.

## Important checked points

1. BGL25 published Theorem2.9 and Proposition2.11 are stated here in their big-background BMP regime. ALS26 Theorems2.1-2.2 provide semipositive-big versions using possibly infinite extended measures without BMP. The manuscript does not silently use a global Radon measure outside these regimes.
2. For an envelope fixed point phi, P_theta(phi+j,0)=phi. The rooftop inequality is first restricted to {phi>-t}, then j>t kills the potentially infinite pole-tail term. No subtraction of infinite measures occurs.
3. Upper volume monotonicity is proved with max(v1,u2-t) and plurifine restrictions; v1 need not be bounded. BGL Proposition3.7 contains a phrase saying v1 is bounded despite equivalent arbitrary singularities; this proof avoids relying on that phrase.
4. Adding a positive current: upper volume uses competitor addition; lower volume uses P_theta(w-v), its same-type bounds, contact support and mixed positivity. This is Li Proposition2.5, not an unsupported extrapolation of BGL's older solvable-singularity result.
5. E_env uses convex competitor inequalities to avoid infinity-minus-infinity at common poles. Uniform upper bounds for the competitors are proved using the normalized L1 bound on a positive-volume set where phi is bounded below.
6. E_env implies equality of both volumes by scaling/addition/monotonicity. E_vol implies E_env by the collapsing-rooftop contradiction, lower volume positivity, and taking the supremum of masses over equivalent representatives. The last supremum is essential. The proof uses no separate global PVP, although the source paper imposes it in the standing setup.
7. Rethlas relative_equivalence_01 returned correct, conditional on Inputs A,C,K,V. It found no errors or gaps in the forward and collapsing-rooftop implications; this does not independently prove the stipulated inputs.
8. Model phi in ALS: envelope fixed point plus P_epsilon theta(phi) genuine for some 0<epsilon<1. Model phi in Li: envelope fixed point plus positive LOWER singularity volume. Li E definition uses UPPER volume equality. Bars were checked visually on PDF pp9-10, not inferred from extracted text.
9. ALS Theorem5.1 allows a nonzero bounded density relative to MA of a bounded theta-psh potential. Theorem5.4/5.7 same-type Lp solutions use no global BMP/PVP. Theorem5.8/Cor5.9 general-measure solutions require v_minus(theta)>0, still no BMP. All share semipositive big theta and the specified ALS model.
10. Li Theorems6.1/6.2 and Cor6.1 require both metric BMP and PVP, big theta and positive lower volume of the model. Constant c uniqueness is distinguished from potential uniqueness at lambda=0.
11. Strict domination inputs: ALS3.11 (smaller-background u, v preceq u), ALS3.14 (v_minus(theta)>0, relative u, v preceq phi, one finite mass), Li3.2 (BMP/PVP setup). Exponential uniqueness and scalar uniqueness are proved separately from those inputs.
12. Unbounded prescribed type prevents uniform lambda u_lambda convergence to a finite constant, including essential L-infinity convergence. The quantitative Lp lemma instead uses 1-exp(lambda v)<=lambda|v| and uniform Lq moments of normalized theta-psh functions.
13. ALS dominated continuity is cited as the combination of Lemma4.2 and Theorem4.1 condition(2), with v_minus(theta)>0. The lemma supplies the common rooftop in E required by Theorem4.1. Mere L1 convergence is not asserted sufficient.

## Primary source versions

arXiv2511.02339 and arXiv2601.13446 landing pages checked again: both still show only v1 (4Nov2025 and19Jan2026, respectively). All theorem locations refer to those saved versions. BGL refers to the published43-pagePDF. New statements are attributed, with no novelty claims.

## Remaining review

The relative-equivalence Rethlas result is complete. Inspect all added PDF pages and perform a second direct reading of the additional proofs; see STATUS.md and the fourth audit for later additions. Deeper PDE estimates and the original SGPT I-goodness equivalences remain research obligations. The full book is not complete.
