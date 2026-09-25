# Chapter 8 rewrite — checkpoint114

Baseline: `009f5246dc7384333d2b382b1aac575c21a31e18`. Chapter 8, *Unbounded mass on a Gauduchon threefold*, is treated as one complete unit under the user's chapter-by-chapter instruction. Its single author input contains all seven sections and has no nested inputs.

## Argument and exposition

The chapter opening now follows the construction: the mass identity reduces unbounded mass to vertical energy; the heat kernel produces concentration; a varying heat time controls mixed derivatives; a base correction restores positivity without changing vertical energy. The final section uses the same identity to identify minimum mass and quantify the difference from a fiber average.

All seven section openings and their headings have been rewritten around these steps. Repeated declarations of the Hopf manifold, elliptic curve, lattice, affine coordinates, background forms, heat kernel, heat potential, radial parameters and positivity expression are removed. Notation is carried from its first definition. The extension conditions remain explicit, and the nonconstant base region may depend on the potential. The second cutoff is explicitly valued in [0,1]. Repeated coordinate declarations in the sharpness example and the repeated definition of the logarithmic radial function in the averaging proof are removed.

The general quasi-psh fact upgrading almost-everywhere equality is now invoked through the first-chapter strict-set lemma. Bounded exact regularization and bounded-product continuity remain first-chapter dependencies. The chapter contains the specialized Hopf calculations; no further general psh result needs relocation. Paper citations remain in the historical chapter, with no source metadata or verification status changed.

## Direct mathematical checks

Both complete direct mathematical and writing reads are finished. The review checks the quotient and fiber-area normalization, background mass six, torsion identities, integration by parts and coefficient six in the vertical energy formula. The radial–vertical matrix gives the stated Schur complement, including smooth extension at the zero base coordinate.

The heat checks include the Gaussian and Fourier normalizations, lowest nonzero eigenvalue one quarter, logarithmic Hessian estimate, logarithmic energy growth and large-time exponential decay. The logarithmic-gradient estimate and its square consequence retain the same parameter range. The varying-scale proof is checked in the initial transition, small-time, large-time and final cutoff regions, with the negative-defect integral tending to zero. The constants controlling the square estimate and the positive margin on [-2,-1] are retained.

For the base correction, the integral of the prescribed second derivative is zero, its first derivative is small and nonpositive, and all three positivity conditions hold. The fixed base ball contributes divergent vertical energy even though the support region of the individual constructed potentials may expand. The bounded lower-mass argument uses uniformly bounded decreasing regularization. Fiber averaging preserves positivity and descends to the base; the fiber Poincare inequality yields the coefficient two thirds, and the cosine example attains the ratio for small nonzero amplitude. The equality characterization uses the bounded quasi-psh hypotheses of the first-chapter lemma. The final normalized-equation consequence is checked against the precise later solvability corollary.

All nine formal statements are byte-identical to the baseline. Eight of nine proof environments are byte-identical; the fiber-averaging proof removes repeated notation and makes its general equality input explicit. The cutoff range is clarified in the construction outside those proof environments. These are direct preservation and proof checks, not independent verification.

## Release checks and remaining work

The baseline and final house audits both have zero errors and two inherited warnings, concerning the legacy chapter label and the recognized Xia–Zhang attribution. The final book has 810 pages. Compilation has no errors, unresolved references/citations, duplicate labels or overfull boxes; one inherited bibliography underfull paragraph remains. All 33 selected book pages passed visual inspection, including the whole chapter, adjacent openings and the front contents. The 17-page companion is byte-identical to checkpoint113. Both outputs rebuilt in a fresh empty extraction, with every reconstructed page text matching production. Exact hashes and checks are recorded in build-snapshot-114.json and source-package-portability-114.json.

The chapter-rewrite queue advances to Chapter 9. The separate proof queue remains at Section 12.2; Q2.8 and the broader writing/research goal remain incomplete. No new independent verifier run, source validation, announcement coverage or novelty judgment is claimed. All 190 historical verifier reports and the three hidden Nakamaye sources are unchanged.
