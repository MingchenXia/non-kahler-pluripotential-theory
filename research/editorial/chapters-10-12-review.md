# Chapters10–12: correctness and proof-economy review

The root pass read every statement and proof in Chapters10–12, including all three Chapter10 inputs, all eleven Chapter11 inputs, and the bounded-contact input in Chapter12. Nine revised sources are integrated in checkpoint33 after compilation and visual inspection. This is a root review, not a new independent audit or a guarantee for the rest of the book. The133 existing audit reports are unchanged.

## Chapter10

Checked mixed ordered contact, bounded Stokes and the five torsion coefficients; the recurrence and parameter restrictions in all dimensions; positive-volume strict sets, strict domination and exponential order. Checked local capacity-test gluing, CLN tails, exponential volume-to-capacity estimates, the backwards iteration, the density-norm lower bound and L1-to-uniform argument. Checked Gauduchon root-integral control of the scalar, Jensen's mean estimate, both approximation limits, and the zero-exponent barriers. The bounded_comparison_01 and weak_lp_existence_01 final reports were read with their actual accepted inputs.

The mixed-contact argument now uses the same decreasing maximum as Chapter6. The short C2 scalar proposition now defines A and B where it is stated; they were previously defined only in the next chapter. Its maximum proof and hypotheses are unchanged.

## Chapter11

Checked good Taylor contact via the Lipschitz gradient, measurable strong maximum principle, cofactor eigenvalues, perturbed extrema, the connected/dense two-component criteria and hypersurface topology. Checked weighted energy, the real-symbol signs and factor, exterior-ball propagation, the distance differential inequality and bracket-generating argument. Checked the surface defect identity, the explicit Gauduchon threefold counterexample, both low-dimensional determinant signs, Sobolev Stokes limits, quadratic density-sublevel separation and the square-root threshold.

Checked ordinary comparison from mass invariance, mass concentration with an auxiliary truncated density and the absence of division by the density. The repeated domination proof is replaced by Chapter10's already proved c=0 case. The mixed-density lemma is correctly described as a later local proof, not an earlier result; that lemma uses local theory alone, so no existence dependency is circular. The surface uniqueness conclusion now reuses the preceding weighted-cofactor theorem. A sentence makes explicit that the extremum argument also runs on the open positive-density set itself.

All nonuniqueness constructions were read: projective rank-one frame and global extensions; flat cutoffs, equal determinant, strict background repair and nonclosedness; the balanced-switch C1,1 family with no interface mass; thin-zero-set ODE trap directions, continuation and all-order flatness; quadratic-density logarithmic slope decay and derivative induction; the analytic determinant identity, outer patch, product normalization, ranks, zero geometry and inverse-power sharpness. Their necessary positivity and endpoint details are retained. Four stray printed commas in differential products and h=pb in the thin-zero proof are corrected to spacing and h=p xi. The latter two source files are shared with the standalone note, whose two changed pages were checked.

Read the existing final reports uniqueness_criteria_01, gauduchon_surface_uniqueness_01, degenerate_nonuniqueness_01, numa_radial_family_01, numa_thin_zero_set_01, numa_thin_zero_set_independent_01, quadratic_density_nonuniqueness_01 and analytic_density_example_01. Their scopes and accepted premises remain intact; this pass did not rerun or edit them.

## Chapter12

Checked finite-obstacle upper bounds, local envelope regularization, continuous obstacles, smooth penalization, lower-semicontinuous approximation and domination, quasi-continuous exceptional-set approximants, semipositive background limits, and the unbounded fixed-cutoff argument. Checked rooftop contact restrictions, non-collapsing from a strict big barrier, semipositive bounded domination, lower/upper volume comparisons and addition, the full-volume equivalence in its stated regime, normalized-envelope equality and the infinite-mass envelope-class witness. Read local_contacts_01, penalized_contacts_01 and relative_equivalence_01 final reports, retaining the latter's stated conditional inputs, supplied by the relevant earlier/later reconstructed proofs.

Two bigness restrictions were unnecessary. The fixed-point estimate only uses semipositive contact support, valid without bigness, and the constant obstacle zero; restricting to finite levels avoids subtraction of infinite measures. The nonempty relative competitor envelope only needs the finite-sublevel upper bound for a fixed smooth background, already proved at the chapter's start. Its obstacle is finite off pluripolar poles and the convex inequality passes to canonical representatives. Reusing that argument shortens a repeated proof. The definitions of lower/upper volume are stated with extended values for arbitrary smooth backgrounds; finiteness, comparison and the closed-mass identification keep their explicit bounded-mass/big scope. No new volume-monotonicity theorem outside that regime is asserted.

## Integration checks and remaining work

The651-page book and17-page note agree with the reviewed preview on every page. All25 changed book pages, both note pages and the final three pagination/scope pages were viewed. The bounded-comparison theorem is kept intact across the page break. No errors, undefined references or overfull boxes remain; the existing underfull bibliography line is unchanged. The exact reversible map and build snapshot33 identify all sources and hashes. Checkpoint32, its source archive and the prior note are preserved. Fresh-source reconstruction and private GitHub synchronization are recorded separately.

Chapter13 has begun: its main chapter, singular domination, semipositive big Lp existence and bounded stability inputs have been read. Its other proof inputs remain pending. Continue this pass through every remaining chapter and appendix, alongside the active research directions.
