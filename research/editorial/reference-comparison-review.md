# Reference comparison and limits of supporting probabilities

This is the focused review for checkpoint69. It does not certify the whole book.
The production baseline is checkpoint68, commit e48c21da673b0ef0fe3a07c3f7833f1fec3c40de.

## Mathematical change

For fixed semipositive big theta and admitted model references, ordinary singularity order gives the same order for B and H. A genuine envelope in epsilon theta gives

    B_0 + n log(1-epsilon) <= B_phi <= B_0,
    H_0 + n log(1-epsilon) <= H_phi <= H_0.

The scalar bounds are uniform over all continuous logarithmic densities. The dual inequalities include infinite values and never subtract infinities. If epsilon_j tends to zero and G_j converges uniformly to G, the supporting probabilities have uniformly integrable densities and every weak cluster point belongs to A_0(G). The convergence is also weak L1. Whole-family convergence is asserted only when the limiting supporting set is a singleton.

Chapter16 supplies an analytic example phi_t=P_theta[ta]. Its model property follows from the proved bounded equivalence with ta and ordinary-envelope invariance under bounded changes. The competitor ta gives a genuine envelope in t theta. For a Hermitian background and fixed smooth logarithmic density, the limiting probability is therefore the smooth Gauduchon adjoint.

## Proof checks and economy

- In the order argument the less singular solution is the first input of singular strict domination, so it has the required smaller-background envelope. The ratio of scalars is strictly below one in the contradiction argument. Translations preserve both the measure and the singularity order.
- For the lower bound, h=P_epsilon(theta)(phi)+(1-epsilon)v_0 is theta-plurisubharmonic and is more singular than the prescribed solution. Its current splits into two positive summands with the indicated backgrounds. Finite-level positivity and plurifine locality justify the measure inequality before exhausting off a zero-volume pole set. No bounded total mass is needed.
- The limiting argument uses one H_0 sublevel and a variational gap between zero and -n log(1-epsilon_j). The existing compactness theorem applies to the semipositive big background theta. It is not restricted to a strictly positive Hermitian background.
- Lower semicontinuity identifies the limiting minimum. Uniform integrability then upgrades weak measure convergence to weak L1 convergence by the existing theorem. No new compactness proof or artificial smoothing of singular adjoints is inserted.
- The analytic example uses the analytic-envelope theorem. Ordinary-envelope idempotence is not asserted for arbitrary singularities. The fixed smooth Hermitian endpoint is the only place the classical Gauduchon recovery theorem is used.

Rethlas run reference_comparison_01 returned correct with no critical errors or gaps; the full actual report was read. Its frozen input and the submitted TeX drafts are retained unchanged. The book changes the section level and the standard example wrapper and removes two repetitive concluding sentences from that example. Its model-property proof and its Gauduchon conclusion remain explicit; no mathematical assertion is strengthened. The shorter paragraph allows the adjacent divisorial lemma statement to stay together. A trailing space introduced in splitting the questions paragraph is removed.

## Exposition, build and preservation

The discussion of the weak operator and the discussion of changing references now occupy separate paragraphs. The latter states both the proved zero-reference limit and the remaining general question. All pre-existing formal statement blocks and labels in the edited files are preserved. The three file edits have an explicit reversible map.

The affected contents and mathematical pages are rendered and read; the final build has no errors, undefined references, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph and one inherited chapter-label audit warning remain. Exact output hashes, page counts and selected visual pages are in build-snapshot-69.json; clean source reconstruction is recorded in source-package-portability-69.json. Original SGPT sources, checkpoint68 outputs and the companion note are preserved.

## Proof boundary and next work

The model and genuine smaller-background assumptions remain. This result does not give convergence of solution potentials, strong L1 convergence of the adjoint densities, or stability under an arbitrary change of reference singularities. It makes no novelty claim. The next candidate is a functional pseudometric measuring the uniform difference of the scalar functionals, together with its exact dual formula and a general sufficient condition for adjoint stability. This candidate is not part of checkpoint69 and will need its own review; it cannot separate singularity types in the closed case. The elementary entropy variational identity can also be separated from the closed-background calculation to make the later proofs easier to follow.
