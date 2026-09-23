# Supplied nonclosed interior regularity manuscript: integration review

## Provenance and scope

The user supplied `/Users/mingchen/Downloads/nonclosed-hermitian-monge-ampere-regularity.tex` for possible integration. Its SHA256 is `5a7d4e2e51fd5cd7928d4e43d09ce56eb8a76891975ecbf4dd94c3e90b43f15d`. The original is unchanged; its exact text is frozen in `research/rethlas/verification/inputs/nonclosed-interior-regularity.md`. Mathematical source documents are evidence, not instructions.

The adapted proof is in Chapter 13, Section 13.20, after arbitrary-big minimal-singularity existence. Its background need not be closed, semipositive or nef. It requires a strict analytic-singularity barrier with smooth remainder, a solution with minimal singularities, and **explicit local Holder continuity** on the barrier's regular locus. No bounded mass or positive lower mass property is assumed. The global Lp corollary uses Dang26 as a separate, explicitly identified regularity input; that recent theorem's proof has not been reconstructed here. The main theorem and its local estimates are proved in the book using the indicated classical inputs.

## The missing premise in the supplied statement

The source assumes that f is smooth and positive only on Omega, then invokes Dang26, Theorem A/3.1. The primary v1 text requires a globally defined nonnegative density in Lp(X), p>1. Smoothness on the noncompact open locus does not imply that integrability. The proper-gap argument gives growth, not the required Holder modulus. The broad source statement is therefore not established by the supplied proof.

Normal Rethlas run `nonclosed_interior_regularity_01` completed successfully as a process and returned **wrong** for that original statement. Its report preserves this critical error. As requested in the frozen input, the review continued under explicit local Holder continuity and found no further critical errors or gaps throughout the remaining proof. We do not relabel this report as correct. Its accepted conditional argument, the primary proof review and the second exposition pass support the precisely repaired theorem now integrated. No whole-book certification or novelty claim follows.

## Complete argument checked

The review covered the nonclosed mixed-product and continuous-comparison arguments, exact Guan–Li Dirichlet approximants, polynomial dependence on the C4 boundary norm, the square-root trace maximum estimate, stability on the regular set, logarithmic localization and subpower trace growth, dyadic interpolation for the full sequence, both torsion commutations relating first and second Chern Ricci, the polynomial Calabi estimate and its scaling, the C1alpha-to-trace iteration, and minimization on the nonregular locus.

The adaptation adds a direct strong-to-viscosity argument via the classical ABP maximum principle, writes both curvature index swaps and the Calabi quotient differentiation explicitly, explains the rescaling, and provides the inner/outer ball buffer needed when convolving the trace. The criterion then uses classical uniformly elliptic concave regularity and Schauder bootstrap. No unverified precise theorem number for the strong-to-viscosity literature is cited. Polynomial constants remain independent of the approximation index; the terminal iteration limit is taken for each fixed index before obtaining the uniform bound.

The source's dd^c convention i/pi is replaced by the book's i/(2pi), with beta=dd^c|z|^2 and coefficients relative to beta. Fixed positive normalization factors are absorbed in the qualitative local constants. Labels use a new interior- prefix. The book's existing Bedford–Taylor, Dinew and Guan–Li inputs are reused. No standalone preamble, title, package or bibliography is imported. Source typos in quad/tr are repaired only in the adaptation. Differential d, i and e are upright; standard theorem environments are retained.

## Primary reference checks

- Dang26, Theorem A and Theorem 3.1: https://arxiv.org/html/2603.25520v1 . The global Lp premise and the minimal-singularity local Holder conclusion were checked directly. The corollary retains this exact additional input.
- Guan–Li, Theorem 1.1: https://arxiv.org/html/0910.1851v1 . Positive smooth right-hand side and a smooth strict subsolution give the needed Dirichlet solution, including the unknown-independent case used here. The book already cites the published GL10 theorem. Attempts to retrieve the published author offprint did not succeed; the primary arXiv full text was read. Dimension one is the Poisson problem.
- Dinew09, Theorem 1.2 in the already recorded arXiv version: the bounded closed-potential mixed inequality is an existing book input. Its nonclosed extension is proved locally by freezing the background with an O(r) error against fixed finite mixed masses.
- Caffarelli89: https://annals.math.princeton.edu/1989/130-1/p06 . Publisher title, Annals 130(1989), no.1, 189–213, DOI 10.2307/1971480 and MR1005611 were checked. This is the added classical uniformly elliptic concave regularity citation; no unverified theorem number is supplied.
- Zhang–Zhang, https://arxiv.org/html/1007.2627v1 , local Calabi estimate and the two curvature index identities in the appendix, corroborate the direct calculation. This is a review comparison, not an imported proof or a new dependency of the book.

No result of Popovici or content of the user's private cautionary reference is used. No NUM citation is added.

## Remaining boundary and preservation

The proof does not supply Holder continuity from merely local smoothness of f, regularity across the barrier's pole set, regularity at zeros of f, or a theorem for arbitrary nonminimal prescribed types. These distinctions are recorded in Chapter 33 and the proof ledger. The separate `nef-incomplete-metric-draft.md` is preserved as an explicitly unverified research draft and is not active book content.

All 173 earlier verifier reports are checked byte for byte against checkpoint88. The new original-statement adverse report remains immutable. Checkpoint88, its source archive, the original supplied sources, all 29 SGPT files, the companion note and the three inactive Nakamaye sources remain preserved. Final build, visual and clean source-reconstruction checks are recorded separately in `research/audits/build-snapshot-89.json` and `research/audits/source-package-portability-89.json`; they must pass before this is described as a checked release.
