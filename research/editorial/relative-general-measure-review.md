# Relative general-measure reconstruction — verified integration

15 September 2026. Both proof audits passed and were read in full before integration. The three sections are now included in Chapter14; checkpoint18 is frozen at536 pages. Checkpoint17 is preserved unchanged.

## Proposed dependency order

1. Existing finite-measure relative domination, proved independently by a decreasing family of stretched envelopes and a fixed finite dominator.
2. New zero-domination without finite mass of either original measure. The auxiliary envelope `k=P_(beta theta)(u-q)` lies in the minimal envelope class; its measure is supported on `{k>=0}`, hence is finite by locality with the single bounded potential `max(k,-1)`. Only now is finite-measure domination used, in background beta theta and with reference zero.
3. Strict domination follows from one stretched envelope, contact support and subtraction on common finite truncation levels, followed by zero-domination. No subtraction of infinite total masses occurs.
4. A common lower member of the relative envelope class and vanishing exponential self-error yield capacity convergence. Weighted lower semicontinuity is used only after monotone capacity convergence. The limiting lower roof need not have finite mass.
5. Moving bounded reference measures give the self-error estimate and uniform raw tails. The tails then give finiteness and weak convergence of the limiting Monge–Ampère measure.
6. Positive continuous density: smooth the bounded reference in a dominating Hermitian background, solve the already reconstructed ordinary-type Lp equations, obtain a common upper bound by singular exponential order in that metric, and use the moving-measure result. The uniform positive lower mass controls the suprema from below.
7. Bounded measurable density: a common nonzero submeasure of the positive continuous approximations supplies a comparison potential through the already reconstructed minimal-reference theorem. Compare with reference zero. Fixed-measure continuity then suffices.
8. Integrable density: increasing density truncations give decreasing solutions, fixed finite domination and dominated convergence.
9. Zero exponent: compare with a minimal-reference solution to control the normalization; the fixed non-pluripolar integration lemma handles the vanishing exponent. The positive scalar is unique; the normalized potential is not asserted unique.

## Scope checks made by the main agent

- Semipositivity, bigness, the smaller-background model condition and positive lower volume remain explicit. Bounded mass is never assumed. The non-semipositive Li theorem is not covered.
- Scaling gives `v_-(beta theta)=beta^n v_-(theta)` by a bijection of bounded potentials. The scaled envelope is in the scaled minimal class by scaling every defining competitor, not by a mass interpretation of that class.
- The difference obstacle is quasi-continuous and finite off pluripolar pole sets. General contact is applied in a big background, without assigning values to differences of two negative infinities.
- The bounded auxiliary truncation proves finiteness of one measure, not a uniform bound over all bounded potentials.
- The smooth reference regularization occurs in omega, a Hermitian metric dominating theta. It does not purport to preserve an arbitrary semipositive big theta while smoothing.
- The existing bounded-subsolution theorem has a same-theta carrier. An initial drafting approach tried to apply it to an omega-carrier; this mismatch was corrected before the downstream audit submission. The submitted proof instead invokes the independently reconstructed general minimal-reference theorem in theta. Its comparison uses reference zero, not the unjustified order `u_j preceq s`.
- The step-one comparison does use ordinary singular exponential order in omega, with a bounded first potential. That theorem needs no positive lower volume for omega.
- No unrestricted L1 lower semicontinuity of non-pluripolar mass, inequality bounding the measure of a maximum by the sum, or implication from capacity to total variation is used. Total variation is asserted only when a fixed finite dominating measure and L1 density convergence supply it.

## Independent checks and preview

- `relative_extended_domination_01`: correct. The final JSON, all15 sequential records and all7 reference records were read in full. Input contains exact envelope definitions and the independently proved finite-domination argument before the new proof.
- `relative_moving_general_existence_01`: correct, explicitly conditional on the zero-domination lemma alone from the first submission. The prerequisite passed independently. The final JSON, all19 sequential records and all7 reference records were read in full. The general existence theorem being reconstructed was not an allowed premise. Both runners exited0.
- Rethlas runs use the ordinary authorized approval mode. Initial sandbox initialization failed; the authorized escalated runs started. Intermittent service transport errors are being retried by the tool; no verdict is inferred from these errors.
- Private preview: `tmp/checkpoint-18-preview`, 536 pages. It contains the staged sections and the old surrounding proof-boundary prose, so it is not a release. All 22 pages from physical 253 through 274 were visually inspected. The exponential common-envelope proposition and the moving continuity theorem need better paragraph grouping; the new general-existence closing paragraph should be kept with its proof. The one low-level underfull bibliography line can be checked when the final surrounding prose is updated.

The exact internal existence target is reconstructed. The stronger relative-volume lower bound additionally displayed in ALS26 Theorem5.8/Corollary5.9 was not part of that target and is not inferred from this audit. The proved uniform bound is `(1-epsilon)^n v_-(theta)`.

Integration changes only cross-references, surrounding explanation and pagination. The new zero/strict-domination section is byte-identical to its submitted source. Removing two Needspace guards recovers the exact submitted moving-measure section. In the general-measure section, removing one Needspace guard and restoring its final expository recap recovers the exact submitted source. That deleted recap contains no additional assertion. The older finite-domination proof is unchanged; it remains independent of the new zero lemma. Two surrounding section conclusions, the Chapter13 preview/attribution and the Chapter32 proof boundary were rewritten to reflect the completed proof. The non-semipositive theorem remains imported with both metric volume properties.

All22 initial preview pages,15 first grouping pages,9 interface pages,9 final grouping pages and2 final contents pages were viewed. All production page text equals the final reviewed preview. The original template is retained. An underfull bibliography line was visually inspected and has no overflow or missing text; it is not a mathematical or compilation failure. Historical reports, original source files and Rethlas memory/results are preserved. These audits are evidence at their stated scope, not formal verification or a novelty certification.
