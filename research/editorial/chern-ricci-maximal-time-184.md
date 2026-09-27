# Chern–Ricci maximal time — checkpoint184

Baseline: `02b98b837d5e7a9444f21341c19a53b346b72d91`. The preceding goal turn completed and privately synchronized checkpoint183, so it was progress. The checkout was clean before this unit.

## Proof and normalization

Theorem 25.17.2 now proves the Chern–Ricci maximal-time formula for every initial Hermitian metric. A positive representative at a later time supplies an affine positive reference path. Time-weighted potential identities bound the potential derivative, and the existing elliptic torsion calculation gives a parabolic trace estimate after the reference-metric derivative is retained. Uniform ellipticity, classical parabolic regularity and short-time existence give continuation. The current lifetime corollary now uses this internal theorem; its statement and the two earlier formal statements are unchanged. Four labels and one theorem/proof are added.

For an admissible time T and a positive representative theta_T + ddc a, the background gamma_t is its convex interpolation with the initial metric. With Omega = exp(a/(2 pi T)) omega_0^n, the scalar equation is u_t = 2 pi log((gamma_t + ddc u)^n/Omega). Thus the potential is scaled relative to the source, while physical time and the source Ricci form are unchanged.

The quantities t u_t - u - 2 pi n t and (T-t)u_t + u + 2 pi n t have opposite maximum-principle signs. Under the contradiction T_* < T, the second has denominator bounded below by T-T_*. The first controls the upper derivative away from zero; the existing initial smooth interval covers zero. No endpoint estimate at the numerical boundary is asserted.

For S = tr_g h with the moving reference g(t), differentiating adds tr_g(g_t)/S and -tr(g^(-1)g_t g^(-1)h)/S. These are bounded by C B + C. The Delta_g(u_t)/S term cancels the differentiated density term in the elliptic trace inequality. The reciprocal-potential correction absorbs the first-order torsion term. Both n=1 and n>=2 are included. No total Monge–Ampère mass conservation is used.

The classical parabolic regularity step uses the infimum of supporting affine functions on a compact set of positive Hermitian matrices. After projection of the real Hessian to its complex part, this is a concave uniformly elliptic extension. The reference and density have smooth coefficients. Evans–Krylov and differentiated Schauder estimates therefore give all derivatives away from time zero; the original smooth interval supplies the initial bounds. Time-derivative bounds make the limiting potential Cauchy in every spatial C^k norm and allow restart with a positive metric.

## Source and review scope

The complete current-duality author input receives an original read and two revised direct mathematical/editorial reads, with the second after the first build and page inspection. The history paragraph and adjoining transitions receive bounded reviews. The earlier elliptic trace proof is reread for this application. Source review covers arXiv:1201.0312v3, Theorem 1.2, Proposition 3.1 with its proof, the Section 4 proof of Theorem 1.2 and the associated Section 9 trace calculation. Classical local parabolic short-time, Evans–Krylov and Schauder theorems remain accepted inputs. No whole-Chapter-25 reread, new independent verification, bibliography change or new Popovici reliance is claimed.

The source PDF SHA-256 is `b741dd6dd119a80c5be6036a8adb055177311c5516438672dfcae4a4b6adcbff`, matching the historical source inventory. The publisher endpoint was attempted but did not expose the paper; the history retains explicitly checked arXiv locators and the existing published bibliography entry. This is a reconstruction of the maximal-time proof, not a fresh review of the source's surface classification, long-time convergence or every external dependency. Gill's specialized higher-order result is replaced here by the stated classical local parabolic regularity argument.

The first page inspection covers 38 selected pages: 21 images were directly inspected and 17 are byte-identical to the checked checkpoint183 render. The second revision improves the subsection opening, keeps the dimension-one and higher-dimensional eigenvalue cases together, and shortens the historical paragraph to avoid an almost empty final page. The current formula does not identify a singularity locus or prove local convergence at the boundary; the separate Chapter 32 parabolic literature comparisons retain their previous scope.

The 811-page book and seventeen-page companion compile without unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph remains. The house audit has zero errors and fourteen inherited warnings. All 38 selected final pages pass visual review: six changed images were directly inspected and 32 match the inspected first render. The first render included 21 directly inspected images. Both outputs rebuild from a fresh empty source extraction with identical page text; the companion remains byte-identical to checkpoint183. The 221-input graph, 190 historical verifier reports and three hidden sources are unchanged. See build-snapshot-184.json and source-package-portability-184.json. Original supplied sources, three hidden Nakamaye inputs and 190 historical verifier reports are preserved. No new author intervention requires a skill change.

## Continuation

Return to Chapter 15: examine which convergence hypotheses on analytic approximants force equality of ordinary and multiplier-ideal envelopes, keeping the unrestricted singularity-topology and trace questions distinct. The broader goal remains active and incomplete.
