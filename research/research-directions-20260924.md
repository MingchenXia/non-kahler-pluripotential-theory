# Research directions from the present proof boundary

Status: working program, 24 September 2026. These are questions to investigate, not claims of novelty or established general theorems. The new arXiv candidates are recorded in `arxiv-watch.json`; no result from those papers has yet been adopted as a premise in the book.

## Individual equations and Gauduchon tests

Fix a compact Hermitian manifold $(X,h)$ of complex dimension $n\geq2$ and a nonzero nonnegative density $f\in L^1(X,\mathrm{d}V)$ for a smooth positive probability volume $\mathrm{d}V$. Use the attained subsolution threshold $b_h(f)$ and normalized Gauduchon-current dual of Chapters 10 and 26. The unresolved implication is from $b_h(f)>0$ to an exact solution of $(h+\mathrm{d}\mathrm{d}^{\mathrm c}u)^n=b_h(f)f\,\mathrm{d}V$ when the metric lower mass vanishes, with the same measure convention as the threshold theorem.

A bounded next task is quantitative: determine whether a vanishing-tail condition on $f^{1/n}$ together with an explicit nonconcentration condition on maximizing Gauduchon currents produces common lower barriers for normalized exponential solutions. The existing scalar convergence does not control the potential error divided by the exponent. First test a proposed estimate on the book's smooth semipositive dual examples and on the balanced elliptic examples; write down exactly where an $O(\lambda)$ estimate, rather than an $o(1)$ estimate, is required. The root-tail hypothesis alone is not asserted sufficient.

Success would be a lemma giving a common barrier or capacity compactness under a condition on this one density. A proof that assumes a uniform bound over every potential would instead belong to the separate mass-bound theory. An explicit example with a positive threshold and failure of the proposed barrier would also advance the problem.

## Degenerate curvature and ideal-selected kernels

Fix a holomorphic line bundle with a smooth semipositive metric near a point. The local curvature can vanish to finite order, while a separate quasi-plurisubharmonic weight imposes multiplier-ideal conditions on the sections. These two sources of degeneracy should be tracked separately. Chiang's arXiv:2609.24869v1, Definition I.1 and Theorems I.2, I.8 and I.10, motivate this question. Theorem I.2 is in a complete Kähler adjoint setting; the more general Hermitian statements impose localized and model spectral gaps. Their proofs have not been fully audited here.

The working note `editorial/degenerate-selected-kernels.md` gives direct proofs of an exact one-dimensional weighted entire-function model and a conditional finite-jet projection lemma. It distinguishes fixed vanishing order from vanishing orders tending to infinity. The latter is necessary for multiplier ideals of $m\lambda\log|z|^2$, whose order is $\lfloor m\lambda\rfloor$.

Checkpoint96 resolves the exact entire-function model with its uniform Poisson comparison. Checkpoint97 transfers the Gaussian transition to compact curves for $q_m=o(m^{1/(2r+1)})$, with a smooth semipositive metric strictly positive away from the chosen point and local weight $|z|^{2r}+O(|z|^{2r+1})$. The local upper bound needs only the local data. The lower proof uses finite model polynomials and a smooth L2 correction whose logarithmic weights retain the growing vanishing order. The full argument passed `compact_growing_jets_01` and is Theorem 27.13.1. See `editorial/compact-growing-jets-energy-review-97.md` for its dependencies and review scope.

The two upper/lower drafts remain derivation history. The earlier conditional fixed-jet projection lemma remains independently unaudited. Problem 33.12.3 now asks which larger ranges within $q_m=o(m)$ retain the Gaussian law, and how further weight terms change its center and scale. A bounded next calculation is a radial perturbed model, followed by genuinely angular terms; no larger-range estimate is established here. Transfer through the book's fibration identities additionally requires control of the selected section spaces and pushed-forward norm. Neither higher-dimensional localization nor a general non-Kähler theorem follows from the curve result.

## Equation-dependent singular loci

Fix a closed big class on a compact Kähler manifold when discussing its ample/non-Kähler locus, as in Chapter 28. Fang--Ma's arXiv:2609.26340v1 proposes a numerical singular locus for the semistable J-equation. Only its abstract has been read in this increment. It suggests comparing the locus where a chosen equation has a smooth solution with the locus where the class admits a smooth strictly positive representative. These are different constructions and their equality is not presumed.

For a nonclosed smooth big background, a precise first question is whether local smoothness of the book's normalized Monge--Ampère solution can be characterized using strict barriers together with a nonconcentration condition on the corresponding Gauduchon adjoint measures. Define the test family and topology before proposing a locus; dependence on the density and background representative must be retained. Start with the explicit semipositive examples and the existing blow-up model. Do not revive the hidden Nakamaye chapter or claim a Hermitian null-locus theorem from a Kähler J-equation result.

## Modifications and singular-space descent

Liu--Rao's arXiv:2609.23469v1 announces counterexamples concerning inheritance and bimeromorphic behavior of the $\partial\bar\partial$ property. Its abstract, not its complete proof, has been checked. Audit whether any future descent argument tries to infer this property for a submanifold or a modification without a theorem. The present unibranch appendix should continue to use its explicit resolution and descent hypotheses.

A further bounded problem is to compare finite Gauduchon traces of a single potential on two resolutions of a fixed unibranch Hermitian space, with uniform control near the exceptional loci. Pan's existing singular Gauduchon theorem is already recorded in the book's literature map and is not a new discovery. The obstacle is compatibility of the singular trace and boundary terms under refinement, not existence of a smooth elliptic operator across the singular set. Do not use Popovici in this argument until the user's full-proof check is satisfied.

## Order of work

Proceed first with the growing-jet model and the individual-density barrier question, while rotating the chapter revision queue. Full audits of the new Bergman and J-equation papers are reading tasks, not substitutes for checking the book's existing proofs. Preserve failed estimates with explicit hypotheses so that daily continuation can build on them.

## Gauduchon persistence: bounded result and next test

Checkpoint98 proves that persistence of the Gauduchon condition along all smooth positive potential perturbations is exactly smooth mass invariance. The explicit three-torus example separates persistence from the Gauduchon condition at a single metric. In the persistence regime, Proposition 4.6.1 gives a canonical bounded adjoint probability and weak continuity for uniformly bounded capacity-convergent sequences. The full new argument passed the bounded audit `gauduchon_persistence_adjoint_01`; its six accepted inputs are explicit.

A next bounded question is to compute or bound the varying normalized Gauduchon multiplier on the non-persistent torus example as the positive metric approaches degeneracy. No such estimate is proved here. Any extension to unbounded potentials must control those weights in addition to Monge–Ampère products; linear trace compactness alone does not provide this. General weak-adjoint uniqueness and a singular weak linearization remain open.

## Quantitative trace coordinates and auxiliary metrics

Checkpoint99 proves C^-1 ||u-v||_1 <= d_gamma,d(u,v) <= C ||u-v||_1^(1/2) on the whole mean-normalized theta-psh space, with sharp exponents. The bounded audit passes under stated classical elliptic inputs. This refines the finite-coordinate theorem without bounding nonlinear mass or identifying different singularity classes.

Fix X, theta, dV and d, and choose two smooth Gauduchon metrics gamma_1,gamma_2. Composing the proved inequalities gives d_gamma_2,d <= C d_gamma_1,d^(1/2), and conversely: an elementary corollary, not a separate verifier claim. A bounded next question asks for stronger mutual moduli, starting with distinct constant metrics on a complex two-torus. Neither Lipschitz equivalence nor its failure is asserted. The one-metric sharpness example does not settle this two-metric question. Degenerating multipliers, capacity convergence and singularity-quotient metrics remain separate unresolved directions.

## Smooth mass defects under strong linear convergence

Checkpoint100, Corollary 6.8.2, is proved and passes a bounded Rethlas check under the three stated internal inputs. On a compact Hermitian manifold with v_+(omega)=infinity, any error sequence epsilon_j in (0,1) tending to zero and any finite real sequence b_j>V_omega:=int_X omega^n can be realized by smooth normalized w_j with omega+dd^c w_j >= (1-epsilon_j)omega and exact masses b_j. The currents converge in coefficient L1 to omega, their full Gauduchon traces converge in total variation, w_j tends to zero in L1, and exp(-p w_j) tends to 1 in L1 for each fixed p>0. There is no uniform-in-p assertion. The exact-mass step uses continuity and the intermediate value theorem, not monotonicity of the mass polynomial. No novelty is asserted.

A direct additional deduction, not separately checked by Rethlas: fix b>V_omega. Compactness of positive measures of mass b on compact X gives a weakly convergent subsequence of (omega+dd^c w_j)^n. Its limit nu has mass b. The pointwise lower bound gives (omega+dd^c w_j)^n >= (1-epsilon_j)^n omega^n. Testing against nonnegative continuous functions and passing to the limit gives nu>=omega^n. Thus sigma:=nu-omega^n is a positive finite measure with mass b-V_omega. This demonstrates a nonzero determinant defect under the stated strong linear and exponential convergence, while every approximant has the same finite mass.

Open in this manuscript: for a fixed X,omega where BMP fails and a fixed b>V_omega, which positive measures sigma of mass b-V_omega arise in this way? A bounded initial question is whether one can force a nonzero defect to be supported in a prescribed coordinate ball; the present construction gives neither arbitrary localization nor arbitrary realization. This is a question, not an adopted conjecture. Additional nonlinear uniform integrability or capacity hypotheses would have to exclude these examples. Coefficient L1 control, total-variation trace control, all fixed exponential weights and a bound on the masses alone do not do so.

## Capacity convergence and the location of mass defects

Checkpoint101, Corollary 7.6.2, is proved and passes its bounded Rethlas check under the smooth prescribed-mass construction, normalized capacity tail estimate and damped continuity. With the same fixed b>V_omega, the sequence from checkpoint100 converges to zero in capacity. For every fixed T>0 the shallow restriction 1_{w_j>=-T} MA(w_j) converges in whole total variation to omega^n. Its complement has mass tending to b-V_omega. Any chosen weakly convergent subsequence of the full measures therefore yields a single positive defect sigma which is also the weak limit of every fixed deep restriction. No T-dependent extraction is needed. This replaces the earlier suggestion that capacity convergence alone might exclude that example: it does not. The relevant extra estimate is uniform control of undamped tails.

The proof uses the lower form bound to control the shallow part from below and exponential damping to control it from above. Small capacity of the moving deep sets does not by itself locate their weak limiting mass. Open in this manuscript: can a prescribed coordinate ball carry such a defect, and must these limits charge pluripolar sets? Neither conclusion is asserted. A bounded next test is to compare a concrete Hopf model with its radial pushforward measure; if no BMP-failing model is available in that chapter, record that obstruction rather than assume arbitrary localization. Varying adjoints and auxiliary trace metrics remain separate questions.

## Hopf fiber averages and the localization obstruction

Checkpoint102 proves Proposition 8.7.1, with a complete bounded audit under the smooth Hopf mass identity, bounded regularization and bounded product continuity. For the displayed metric, ||u-Au||_L2(nu)^2 <= (2/3)(M(u)-6), with sharp constant, and M(u)=6 exactly for bounded base pullbacks. This is a proved model deduction, not a new premise of the general theory or a novelty claim.

The earlier localization test has not been solved. In the explicit heat construction, L=log(1/eta), q_0=sqrt(L+L/eta^2), a=sqrt(kappa/(2eta)) and x_*=(q_0+1/2)/a, so x_* grows on the order of sqrt(L/eta). The region in which the potential varies is not confined to a common relatively compact part of the affine base chart. Large fiber energy over a fixed ball therefore does not establish a defect supported in that ball. Prescribed support and pluripolar charging remain open here; this is a limitation of the construction, not a nonexistence theorem.

Next bounded test alongside Chapter 9: use the explicit Hopf mass-minimizer characterization to constrain the scalar in a smooth normalized Monge–Ampère equation whose density has the background total mass. Determine the equality case directly, and distinguish total-volume information from the full fiber profile of the prescribed density. No general zero-exponent uniqueness or singular weak conclusion should be inferred from a smooth equality calculation.

## Hopf normalization: proved deduction and next boundary

Checkpoint103 proves Proposition 9.9.1 and Corollary 9.9.1. For the fixed Hopf metric, nu=omega^3/6, smooth mean-zero solution u_F and scalar b(F), put D(F)=b(F)+log integral exp(F)dnu. Then exp D=1+integral |(u_F)_w|^2dnu, and ||u_F-Au_F||^2<=4(exp D-1). In particular D>=0, with equality exactly for smooth base-pullback logarithmic densities. For normalized positive f this says b(log f)>=0, with equality exactly for base-pullback f. This completes the bounded test proposed at checkpoint102.

For smooth G, let v have zero nu-mean and L_0v=G-integral Gdnu. The second variation at the background is D''(0)[G,G]=2 integral |v_w|^2dnu. Its kernel consists exactly of base-pullback G. The direct proof differentiates the energy identity after using the Gauduchon adjoint to identify v. The bounded run `hopf_normalization_defect_01` passes, with complete report read; this is an internal model deduction and carries no novelty claim.

Open here: whether D is convex away from the background; no conclusion follows from adding concave b to a convex log-integral. No uniform norm coercivity for logarithmic densities or nonsmooth equality case has been proved. A next bounded test, after the remaining Chapter 9 second pass, is to compare the scalar's known uniform extension with the exact continuous-density solvability and convergence hypotheses in Chapter 10. Determine whether the Hopf equality case extends to continuous densities, checking convergence of potentials and fiber disintegration rather than assuming nonlinear continuity from L1 convergence. Fixed-region mass-defect localization, support and pluripolar charging remain separate open questions.

## Hopf normalization for Lp densities: resolved boundary and next test

Checkpoint105, Proposition 10.10.1, proves c_f I_f>=1 and ||u-Au||_L2(nu)^2<=4(c_f I_f-1) for continuous solutions and nonnegative nonzero f in Lp, p>1. Equality holds exactly when f is almost everywhere a base pullback; then every continuous solution descends. The bounded run `hopf_lp_normalization_01` passes under four explicit internal inputs. Measurable descent and the bounded cube identity are proved directly. This resolves the preceding continuous-density question in a stronger range; it does not give a weak vertical-energy identity or a theorem for unbounded potentials.

A next bounded question: fix p>1 and an Lp upper bound, normalize I_f=1, and let c_f decrease to 1. Determine which weak limits of the density measures must be base pullbacks, using the actual uniform compactness of continuous solution potentials and the fiber-average estimate. Separate this qualitative claim from a uniform density-norm modulus; no such modulus is established here. Global convexity, L1 endpoints, unbounded solutions and the mass-defect support questions remain open.
