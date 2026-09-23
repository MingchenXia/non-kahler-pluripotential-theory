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
