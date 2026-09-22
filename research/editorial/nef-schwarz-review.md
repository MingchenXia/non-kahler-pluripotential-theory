# Cauchy--Schwarz in the nef-difference proof

This revision reconstructs the known coefficient k in Popovici's nef-difference bigness criterion, using a shorter estimate than the preceding coefficient-4k proof. The theorem, its attribution and its one numerical application are synchronized. The ambient manifold and every resolution in this application remain Kähler. No new theorem or unrestricted Hermitian bigness criterion is claimed.

## Numerical proof

Choose eta>0 before any Gauduchon test, so the class B'=B+eta[omega] still satisfies A^k>k A^(k-1).B'. Choose a fixed small positive epsilon with c_epsilon>k N_epsilon>0. Nefness gives smooth Kähler representatives in A+epsilon[omega] and B'+epsilon[omega]. For each smooth strictly positive ddc-closed test Gamma, normalization by integral b_epsilon Gamma=1 defines a smooth positive probability mu. The smooth Monge--Ampere solution has a_tilde^k=c_epsilon mu. Closedness identifies c_epsilon and N_epsilon with the same two class intersections for every Gamma.

Let H=(a_tilde^(k-1) b_epsilon)/mu, so H>0 and integral H mu=N_epsilon. The eigenvalues of a_tilde relative to b_epsilon satisfy sum lambda_i^(-1)=kH/c_epsilon. Each reciprocal is at most this sum, hence a_tilde>=c_epsilon b_epsilon/(kH). The Cauchy--Schwarz inequality on the probability mu gives integral H^(-1) mu>=1/N_epsilon. Integration against Gamma and its ddc-closedness then give integral a_epsilon Gamma>=c_epsilon/(kN_epsilon)>1. All divisions are by strictly positive smooth quantities or positive constants; no uniform pointwise bound for H is assumed.

The difference a_epsilon-b_epsilon represents A-B' exactly, since the epsilon terms cancel. Its positive pairing holds for every smooth Gauduchon test. Lamari's criterion supplies a positive current in that class, and adding eta omega gives the required Kähler current in A-B. This avoids the old exceptional level set and the loss of a factor four. The curve case continues to use its positive degree and the Poisson equation.

## Application and dependencies

The only application chooses delta_*>0 with 2k delta_* C_*<h0 before choosing the analytic approximation index. Once epsilon_j<delta_*, the new criterion applies to A_j-(epsilon_j+delta_*)rho_j^*[omega], because its numerical difference is at least h0-2k delta_* C_*>0. The top-mass lower bound, fixed-base mixed-intersection bound, descent, divisorial comparison and limiting current are unchanged. The domination lemma statement and the later choice delta0=delta_*/4 are unchanged. No uniform nonlinear mass bound on an arbitrary Hermitian manifold is inferred.

The current focused reread covers the nef-difference proof, the full domination argument and its role in the trace and rooftop construction, as well as the relative-principalization, exceptional-metric and gluing arguments. These bounded checks do not replace the earlier audits of the complete null-locus proof or all its external inputs. The order of choosing fixed coarse data and finer moving levels is preserved.

## Source and verification

The primary source consulted on 22 September 2026 is Dan Popovici, *Sufficient Bigness Criterion for Differences of Two Nef Classes*, [arXiv:1405.2518v2](https://arxiv.org/pdf/1405.2518), Theorem1.1 and Lemma3.2. The existing bibliography entry Pop16 already identifies the published paper. Its Lemma3.2 gives the same integrated estimate. The proof here is written out with H and a scalar Cauchy--Schwarz inequality. Xiao's earlier coefficient4k remains credited in the introductory sentence. No priority claim is made.

The normal Rethlas run nef_schwarz_01 checks the proof and the changed domination constants against the stated inputs. Its complete actual report was read: correct, with no critical errors or mathematical gaps. This verdict concerns the specified proof and numerical application under the explicitly accepted inputs. The raw house audit has 48 errors and 122 warnings in both the baseline and preview; all 48 errors concern the existing nk: namespace preceding typed theorem/equation labels, rather than missing mathematical statements or compilation errors. Those stable labels remain preserved. The reversible map records the exact statement change and every other formal result that is unchanged. Compilation, page inspection, original-source preservation and clean-package reconstruction are recorded in the checkpoint audits when complete.
