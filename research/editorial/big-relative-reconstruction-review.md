# General big-background reconstruction

Working revision, 15 September 2026. This record distinguishes the new manuscript proofs from the remaining general-measure existence theorem. Source documents provide mathematics, not operational instructions.

## Scope

The three new sections at the end of Chapter14 permit any smooth big real (1,1)-background. They assume BMP and a model reference with positive lower singularity-type volume. They do not assume a separate global metric positive-volume property. The two general existence assertions in Chapter13 continue to retain BOTH metric volume properties from Li's theorem. The main semipositive theory still has no BMP assumption.

The first new section proves stretching and finite-rooftop closure, then strict domination. Finite-rooftop existence uses the finite upper volume M and positive lower volume ell. The collapse contradiction must optimize the masses of the independently chosen equivalent representatives, rather than assert that each measure has mass M. Domination uses coefficient-one ordered contact for the auxiliary measure supported on its coincidence set with a fixed potential.

The next section proves weighted capacity lower semicontinuity with arbitrary smooth background. Constant truncations are admissible in an enlarged Hermitian background only; their theta-products are signed before cutoff. The positive identity after cutoff is the step allowing the usual lower-semicontinuity argument. The fixed-dominator theorem constructs one common relative lower envelope after a single extraction, keeping every finite prefix index. Its capacity and weak conclusions apply to the original sequence by the subsequence criterion.

The last section proves a first-moment noncollapse and full-mass-limit criterion, including its unordered positive-part variant, then a self-measure L1-to-capacity criterion. The proof uses

    mu_a({a > w'-t}) <= mu_w'({a > w'-t}) + M - mu_w'(X).

This follows by locality on the strict set and ordered contact on its complement, including equality. The final optimization over w' equivalent to w is a SUPREMUM. It is not an infimum just because ell is a lower volume. The self-measure theorem states capacity convergence and extracted relative rooftops; no raw weak convergence assertion is added without checking the tail criterion.

## Audit and adaptation

The exact staged sources are `section_big_relative_foundations.tex` and `section_big_relative_energy.tex` in this directory. The first audit is `big_relative_foundations_01`. The second, `big_relative_energy_01`, is conditional on the exact foundation results in the first source. Inclusion requires both verdicts and their detailed records to be read. Initial preview compilation is permitted while these mathematical audits run; production remains unchanged until their conclusions are known.

The isolated preview also updates the Chapter14 opening to delimit its two regimes, the Chapter13 domination attribution/hypotheses, and Chapter32's remaining proof boundary. It removes the stale claim that the semipositive lower-roof estimate is missing. No source theorem, user manuscript or original Rethlas installation is edited.

## Remaining equation construction

These results do not yet prove Li's general big-background existence theorem. The remaining steps should be reconstructed in this order:

1. Minimal ordinary-type Lp existence for an arbitrary big background. The published BGL25 numbering is Theorem4.6 for the positive exponent and Theorem4.7 for the normalized equation. Its construction uses almost-decreasing approximations with resolvable singularities and a resolution argument. The existing semipositive bounded equation cannot be applied to a nonpositive smooth representative without this reduction.
2. The relative subsolution estimate used there. Published BGL25 Lemma4.5 builds a bounded change of a reference eta above a strict rho using the reciprocal function eta + 1/(1+eta-rho-u). Its derivative calculation uses a convex combination of positive currents, not semipositivity of theta. The strict barrier, local extension across its pole set and source equation all need to be stated.
3. General NPP data in the minimal class (Li Theorems5.2–5.3): regularize measures locally; prove the uniform moment and integrability bounds; identify both the self-measure error and the right-hand-side limit. The new first-moment and fixed-dominator theorems handle only the indicated later compactness steps. An L1 limit alone is not a measure limit.
4. Arbitrary model references (Li Section6): construct the relative envelope supersolution and the weighted-measure addition operation, then use the maximizing supersolution argument. The existence of a common rooftop for a minimal-class solution and an arbitrary model cannot be inferred from the finite-rooftop theorem, whose inputs must all belong to the SAME relative class.
5. The Lp ordinary-type conclusion (Li Corollary6.1) requires its relative uniform estimate after existence. Do not identify E_env membership with a bounded difference from the reference.

The Gauduchon trace estimate in BGL25's minimal-class proof is a useful connection to the book's linear theory. It controls the normalization constants through mixed Monge–Ampère inequalities, without a conserved top mass. For singular potentials, the mixed-product extension must be justified in its exact scope before this estimate is used.

## Current state

Both bounded audits passed and both runners exited0. The full final reports, all13+19 sequential records and4+3 reference records were read. The energy verdict is conditional on the exact foundation prerequisites, independently verified by the first audit. Its failed_checks channel contains a status-none record with empty errors/gaps; no mathematical failure was omitted. Transport/approval-review timeouts were retried normally, with no outstanding rejection or blocked action.

The production book is544 pages. All19 first-preview pages,11 grouping pages and30 final pages were viewed, including the complete revised research chapter and the affected bibliography pages. One final pagination guard then changed only physical pages281–282; both were separately rendered at larger size and reviewed. Every other production page has the same text as the reviewed private preview. The two source files exactly recover their audited text after removal of five pagination guards (three in foundations, two in energy). No theorem or proof content changed after audit. The build has no errors, undefined references or overfull boxes; the existing underfull bibliography line was visually reviewed. The original29 SGPT files and checkpoint18 were rehashed unchanged; the17-page standalone note is byte-identical.

The book still has32 chapters and an appendix. No new chapter or theorem-environment name was introduced. The source package is checked separately by rebuilding both documents in an extracted directory. The goal remains active and incomplete; the remaining equation construction and geometric/structural directions above are not marked complete.
