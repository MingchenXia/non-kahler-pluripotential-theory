# a5d audit report (r5g08, r5g09; base 1fece9c)

## Verdicts
- **r5g08: EDITS CORRECT.**
- **r5g09: CORRECT AFTER FIXES.** The new proof of `thm:smooth-boundary-trace-regularity` was right, but it leaned on a remark about the proof of `lem:big-local-comparison` instead of on its statement. The extra-task edit below makes the citation apply as written.

## Counts checked
- r5g08: 4 hypothesis removals, 8 duplicate removals or citation replacements, 3 simplified proofs (plus the shortened proofs behind the duplicates).
- r5g09: 14 hypothesis removals, 5 duplicate removals, 6 simplified proofs.
- I read the math diff of every changed file. Every removed or added display matches a listed change.

## Extra task: `lem:big-local-comparison` (done)
I checked the lemma's proof step by step. It uses only:
- locality and ordered contact (`lem:bounded-ordered-contact`, which allows any smooth θ);
- the local envelope theorem `eq:local-envelope-contact` on a Euclidean ball;
- positivity of mixed products of local bounded products;
- Bedford–Taylor comparison for the plurisubharmonic q.

It never uses B⋐Ω, the barrier ρ, bigness or closedness of θ. Both callers apply it on relatively compact coordinate balls: `thm:big-barrier-domination` and `thm:smooth-boundary-trace-regularity`.

Edits made:
- `section_big_minimal_comparison.tex` l.9:
  - old: "Let $u$ and $v$ be bounded $\theta$-plurisubharmonic functions on a coordinate ball $B$, and assume"
  - new: "In this lemma, $\theta$ may be any smooth real $(1,1)$-form on $X$. Let $u$ and $v$ be bounded $\theta$-plurisubharmonic functions on a coordinate ball $B\subset X$, and assume"
- `section_local_density_boundary.tex` l.28:
  - old: "The local comparison principle of \cref{lem:big-local-comparison}, whose proof uses neither a barrier nor closedness of $\theta$ and therefore applies on every coordinate ball, gives $u\geq V$ and $V\geq u$."
  - new: "The local comparison principle of \cref{lem:big-local-comparison} gives $u\geq V$ and $V\geq u$."

With this, the new proof of the trace theorem is complete for any smooth θ and any u that is locally bounded on Ω. `lem:ball-smooth-dirichlet` allows any smooth background θ near the closed ball and density f dV = Fβ^n with F smooth and positive. u and V are bounded θ-psh on B and have the same measure, and u−V→0 at ∂B. The remark recovering the minimal-singularity case is correct. The example no longer needs ρ=0.

## Priority items (all correct)
- **`prop:lower-barrier-criterion` merged into `thm:common-barrier-criterion`.** I rechecked the proof under φ−C ≤ u_j ≤ C and u⪯φ:
  - φ−C is a competitor, so all rooftops lie between φ−C and C, and the weights stay bounded;
  - p ∼ u ∼ φ;
  - singular domination applies to (p,u);
  - Hartogs holds because u_j ≤ C.

  `cor:common-barrier-continuity` without the upper bound: `lem:fixed-npp-integrals` and `lem:moving-bounded-integrals` need only u_j ≤ C, and the tails need only u_j ≥ φ−C. Every caller still holds:
  - chapter_normalization l.90, prescribed_existence l.43/108 and bounded_subsolution l.41/81 all have u_j within bounded distance of φ, so u⪯φ holds and u∼φ follows;
  - addition_equation uses reference w ∼ φ;
  - semipositive_capacity_limit and gauduchon_moment use the old label, which now resolves to the theorem.
- **Proofs now citing earlier results:**
  - `prop:compact-obstacle-polar-invariance` on ℙⁿ with the Kähler form θ_δ (no circularity; `lem:big-pointwise-competitor` uses only Josefson);
  - `lem:smaller-background-mass-lower`;
  - `cor:singular-exponential-order`, with λ=1 and direction checked;
  - `thm:bounded-one-sided-stability`; I verified h−v ≤ C₀, v−h ≤ 1, and that w and v−δ satisfy the hypotheses of `thm:big-barrier-domination`;
  - `cor:big-exponential-symmetries`, applied to θ=ω and ρ=0;
  - `lem:continuous-density-coefficients`.

  The forward citation `cor:affine-two-sided-growth-slopes` is not circular: its chain uses only `thm:affine-supporting-probabilities`, and compactness is now proved in `lem:affine-active-support-stability`.
- **`lem:affine-logarithmic-pole-barrier`.** Its only user, `lem:relative-affine-zero-value`, needs only a bounded E. The ℙⁿ proof is correct. The `\index` entry moved with the lemma.
- **`lem:numa-radial-flux` for λ ≥ 0.** k_λ is continuous because G is, so the atom argument goes through. Smoothness follows from the smooth system (G,h). `prop:numa-positive-exponent-nonc2` gets K-invariance from `prop:symmetric-equation-clusters`. κ is even in `subsec:numa-positive-background`.
- **`prop:fixed-spherical-reference` bound.** ν ≤ M_ρ(ν)ρ ≤ k⁻¹M_ρ(ν)MA_h(u_ρ). Callers are consistent, and n=1 is fine (`lem:spherical-bounded-product`).
- **Semipositive degeneration.** "Z closed, ρ smooth off Z" suffices: usc gives ρ→−∞ at Z, so H→−∞ there, and Z is pluripolar, so it has zero μ- and MA-mass. Also checked: n=1, and α>0 in `prop:radial-tube-diameter`.
- **c absorbed into f.** The n=1 step, `prop:interior-tame-approximants` and `cor:big-lp-interior-smoothness` are correct: Z is not charged, φ is normalized, and the density cf·ωⁿ/dV is in L^p. The reduced `prop:interior-criterion` keeps the only direction used; semipositive_degeneration l.167 cites only its Evans–Krylov argument.

## Other changes checked (no problems)
- r5g08:
  - `lem:planar-contact-barrier`: decreasing limits on disks, growth bound, h(2)=0;
  - `lem:affine-local-weighted-regularity`: monotonicity in η, sandwich on K_r;
  - contact-defect lower bound: K∩{z₁=2} is pluripolar;
  - polar invariance via ℙⁿ;
  - `thm:big-bounded-exponential` uniqueness (θ≥0 makes bounded potentials admit P_{δθ});
  - smooth comparison moved;
  - deleted remarks (not cited);
  - shortened remark after `thm:big-minimal-holder`.
- r5g09:
  - `prop:relative-measure-carrier` without θ≥0 (s=q+(1−ε)ρ still strict; μ=0 is harmless);
  - `lem:density-subsolution-lone-closure` (common upper bound from `lem:qpsh-hartogs` at maximum points);
  - `lem:bounded-normalizer-subsolution` with L^p densities (all callers fine);
  - `prop:individual-normalizer-lp` (f_k→f in L^p, no circularity);
  - `prop:mass-deficit` (C closed, so dd^c(β^k)=0);
  - removal of n≥2 and ψ≤0 in `thm:resolved-type`;
  - μ replaced by dV in `thm:minimal-blowup-data`;
  - `prop:interior-calabi` scaling;
  - `prop:symmetric-equation-clusters` via citations.

## Outstanding items for the coordinator (not in my files; proposed by r5g08/r5g09, not yet applied)
- `chapter_history.tex` l.146: "For bounded weights, the proof uses the logarithmic pole barrier of \cref{lem:affine-logarithmic-pole-barrier}." is now false; the corollary no longer uses the lemma. Use r5g08's replacement, and its l.156 replacement.
- `chapter_history.tex` l.806 ("In \eqref{eq:local-density-determinant} the background is zero …") and l.808 ("uses Bedford and Taylor's uniqueness theorem") describe the old proof of the trace theorem. Use r5g09's replacements.
- `section_gauduchon_moment_equations.tex` l.46 and `section_semipositive_capacity_limit.tex` l.11 still say "additional hypothesis … of \cref{prop:lower-barrier-criterion}". This is correct, since the label resolves to the theorem, but the wording is stale. Use r5g08's replacements, adapted to the current l.46 text: "the hypothesis $v\preceq\Phi_f$ of \cref{thm:common-barrier-criterion} holds since $v\leq\Phi_f$".

## Compile check
`chapcheck.sh a5d chapter_envelopes chapter_prescribed_equations`: no errors, no overfull boxes, no undefined references. The only message is the ignorable Underfull (badness 1783) in section_singular_radial_obstacles. On the first run, `eq:split-product-ma` was briefly undefined in section_radial_integrable_selection; that comes from concurrent work outside my files and was gone on rerun.
