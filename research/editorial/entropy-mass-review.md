# Entropy differences and mass extrema — 22 September 2026

This bounded follow-up to checkpoint66 concerns the Hermitian zero-reference dual, the already proved smooth/bounded mass extrema and their curvature interpretation. It is a focused proof and exposition review, not a certification of the entire manuscript or a novelty claim.

## Claim and proof

On probabilities of finite relative entropy, the infimum and supremum of H_0 minus entropy are log v_- and log v_+. These exact extrema are already obtained by restricting the domain to smooth strictly positive probability measures. No probability attaining an extremum is asserted. Zero lower mass and infinite upper mass are included.

For any continuous logarithmic density G, the bounded solution mass is exp(B_0(G)) times Z_G, where Z_G is the integral of exp(G). Its mass bounds imply the two inequalities for B_0. Taking the defining dual supremum and the ordinary entropy variational supremum gives the global bounds on the difference. Only finite-entropy probabilities are subtracted; checkpoint66 makes their dual values finite.

The two sharpness arguments use different probabilities. A smooth Gibbs probability has entropy equal to its G integral minus log Z_G; testing H_0 with G gives the lower bound by log of the solution mass needed for the upper extreme. The smooth Gauduchon adjoint probability attains the dual minimum at G, while entropy is at least that same test expression; this gives the upper bound by log mass needed for the lower extreme. Both probabilities are smooth and strictly positive. Smooth normalization realizes every smooth strictly positive potential mass. The earlier exact bounded regularization theorem then supplies every bounded mass as a limit of these masses. This avoids a forward dependence on the Chapter27 mass-extrema theorem.

Changing the smooth reference volume adds the same bounded linear functional to H_0 and entropy. Smooth changes of Hermitian representative transport bounded solutions and preserve their normalization scalars. The difference is consequently invariant under both changes. Its constancy is equivalent to v_-=v_+, with their common value necessarily finite and positive because the zero potential is admissible. The Chapter27 curvature characterization of mass invariance therefore also characterizes constancy of this difference. Its existing theorem and proof were preserved; only the explanatory paragraph was updated.

## Scope and checks

The Chapter15 scalar normalization, mixed concavity, weak adjoint construction, directional derivatives, smooth recovery, probability dual, measurable extension, entropy computation and generic uniqueness arguments were reread in full. The Chapter2 mass polynomial and comparison obstruction, the Chapter27 mass extrema and curvature characterization, and the bounded regularization dependency were checked at their interfaces. The new proof reuses those established statements instead of rebuilding them. Existing theorem labels and formal statements remain unchanged.

The separate normal Rethlas run entropy_mass_extrema_01 checks the candidate, the smooth positive restriction, both invariant changes and the constant-difference criterion. Its actual report is recorded in the release audit. No verifier input, result or memory is edited. The reviewed TeX is identical to the submitted mathematical text.

The final style audit has zero errors and one inherited warning for the recognized historical theorem name Chiose. Thirteen selected output pages are rendered and read, including the table of contents, the complete new proposition and surrounding proofs, and the curvature interface. The production and reconstruction checks are recorded in the build and package audits.

## Remaining boundary

This result is confined to a Hermitian background and reference zero. It does not provide entropy-difference extrema for a singular reference, a regularity theorem for weak currents, an exact equation for an arbitrary unbounded density, or a mass property on a general manifold.

A separate draft at /private/tmp/section_prescribed_dual_entropy.tex proposes extending the two-sided entropy estimates to the model references already admitted by Chapter15, with a common smaller-background parameter. Its argument uses a bounded subsolution in the residual semipositive big background and comparison with a dominating Hermitian background. It is not part of checkpoint67; its strict-domination hypotheses and uniformity require a separate verification. No new source is silently treated as an instruction.
