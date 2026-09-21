# Lee–Gauduchon geometry: reconstruction review

Checkpoint25 addresses a remaining geometric proof obligation rather than another bounded-mass equation subcase. The production baseline is checkpoint24. Both new proof sources have passed their independent audits and are integrated in the manuscript. Final production and source-package checks are recorded below.

## Sources and the proof route

The primary arXiv record of Ornea–Verbitsky2411.05595 was checked: the current version is v2,14November2024, published as a2025 book chapter. Sections2–4 were read completely in the archived text, followed by Section5.1 and the relevant LCK examples. The target statements are Theorems3.11 and4.5, together with the limitation in Remarks5.6–5.8/Example5.7. Their citations provide attribution; their proofs are not used as unverified premises.

The reconstruction begins with the already proved generalized Lamari criterion and the full Gauduchon trace identity. If both kappa and -kappa are pseudoeffective, their positive representatives sum to a ddc-exact positive current of zero Gauduchon mass. They vanish. Elliptic regularity upgrades the resulting distributional potential to a smooth one, proving that the lineality of the degree-one pseudoeffective cone is precisely ker(j_X).

The image of all smooth ddc-closed complementary forms is identified with the annihilator of this kernel by the same criterion and finite-dimensional Poincare duality. A finite basis of smooth preimages then proves openness of the image of the positive cone. This avoids relying on an unproved infinite-dimensional closed-range or open-image assertion. Finite-dimensional separation gives the strict dual formula, with tests only in C_X minus ker(j_X). Strict positivity is never demanded against zero or any other kernel element. Openness is in W_X, which can be zero or smaller than the whole de Rham group.

For a modification, closed positive (1,1)-currents are pulled back through local psh potentials. Genuine pullback potentials, including over the exceptional locus, are justified before invoking their Hessians. Descent uses positive pushforward and first treats the pushed potential as a distribution. Scalar elliptic regularity proves Bott–Chern pullback injectivity. No pullback for arbitrary currents is asserted.

The H1 isomorphism for a smooth blowup is derived from the Thom isomorphism and the long exact sequences of the center and exceptional-divisor complements. The dual map has direction pi_*:H^(2n-1)(Y)->H^(2n-1)(X). General position makes the identification canonical for the specified bimeromorphic map.

The only new classical external theorem is analytic weak factorization. AKMW, arXiv:math/9904135v4, Theorem0.3.1 explicitly covers compact complex manifolds in case(2), preserving a common isomorphism open set and factoring through smooth-center blowups/blowdowns in that category. The algebraic Theorem0.1.1 would not suffice. The primary PDF was checked online, downloaded through normal authorized access, and its exact Section0.3 statement checked in the extracted text. The source is archived as `research/sources/AKMW02-factorization.pdf`; its checksum and version are in the source manifest. The bibliography specifies the arXiv theorem numbering. Weak factorization is retained as a standard reference, not purportedly proved in the book.

## Consequences and the limitation

The cone criterion shows that containing zero is equivalent to filling W_X and to C_X=ker(j_X). Balanced metrics imply these conditions; Fujiki-class manifolds have W_X=0. A nonzero pseudoeffective class in the image of j_X therefore obstructs balanced metrics throughout the bimeromorphic class. For the known Hopf threefold the cone is an explicit positive half-line. This has no implication that ordinary perturbations remain Vaisman or that their nonlinear masses are bounded.

A second subsection supplies a concrete limitation. The free proper holomorphic C-action

    t.(z,w) = (exp(t)z, exp(i t)w)

on (C2 minus0)^2 has a compact complex quotient. Each orbit has a unique representative on S3 times S3, yielding an explicit smooth product identification. The quotient projects holomorphically and submersively to P1 times P1. Pulling back its product Fubini–Study form gives a nonzero semipositive closed form which is de Rham exact since H2=0, but is not Bott–Chern exact by its positive Gauduchon pairing. H1=H5=0 makes both the image of j_X and the Lee–Gauduchon cone trivial.

The positive exact form obstructs a strongly Gauduchon metric directly: a closed real complementary form with positive pure-type component would pair to zero by Stokes and strictly positively by positivity. The subsection also computes the exact primitive of dc(gamma^(n-1)) for a strongly Gauduchon metric, retaining the factor i/(4pi). Only this obstruction direction is used; the full general characterization of strongly Gauduchon manifolds by exact currents is not imported. Thus vanishing of the Lee–Gauduchon cone is explicitly not a balanced or strongly Gauduchon existence criterion, and image(j_X) need not be every de Rham-exact Bott–Chern class.

## Independent verification and editing

`section_lee_gauduchon_cone.tex` is submitted to `lee_gauduchon_cone_01`; `section_lee_gauduchon_strong.tex` is submitted to `lee_gauduchon_strong_01`. Both original submissions are immutable. The audits are independent: the second example uses only the definitions and direct vanishing of H1 and H5, not the first audit's duality or invariance conclusions. Both normal runners exited0 with verdict correct and no errors or gaps. All15 sequential and4 reference records of the cone audit, all11 sequential and2 reference records of the strongly Gauduchon audit, both failed-check channels and both complete final reports were read. The latter failed-check channel contains one empty issue-audit record, not an adverse finding. Sampling and search/approval timeouts recovered normally without restarting a live run or bypassing review. These are bounded independent checks under the stated premises, not formal verification or novelty certification. The root agent has not edited verifier memory/results or the original Rethlas installation.

The integrated manuscript replaces the old short cone paragraph at the end of Chapter31 by the two proof sources. Chapter31's introduction now signals the invariant and its limitation; Chapter32 connects the result and counterexample to the geometric questions. One new classical bibliography entry is added. The full preview has595 pages and no errors, undefined references or overfull boxes, with one pre-existing underfull bibliography line. All48 initial affected/interface pages have been rendered and viewed. Seven pagination guards keep introductions with formulas and statements with their proofs. Four guards lie in the two submitted sources; removing two from each exactly recovers the immutable submissions. The other three affect the existing Chapter31 opening and Chapter32 formula/problem groupings. All30 final pages covering changed regions and their interfaces were also rendered and viewed. No new mathematical text was changed during pagination.

The remaining self-contained geometric writing obligation is transverse Vaisman existence; the singular Gauduchon theorem on general compact spaces also remains a specifically cited contextual input. These are separate from the reconstructed Chern–Ricci rigidity and the present cone arguments. General no-BMP model equations, I-goodness, high-dimensional traces, positive-volume recovery and other open questions remain part of the full project.


## Integration and release

Seven source files are integrated: two new proof sources, the Chapter31 source and volume-section inclusion, the Chapter32 source and geometric-connections section, and the bibliography. The last geometric-connections section changes only by a pagination guard; earlier Chapter31 volume and rigidity proofs are unchanged. The integration map records all before/after and submitted hashes. Only the five expected pre-existing book files differ from the checkpoint24 source archive; the two new proof files are added. The research guide, proof-obligation ledger, comparison map and literature record now agree that cone duality and invariance have been reconstructed.

The reviewed final preview contains595 pages,32 chapters and an appendix. Production page-text equivalence, compilation checks, original-source preservation and immutable snapshot are recorded in `research/audits/build-snapshot-25.json`. Independent source-archive rebuilds of both the book and unchanged17-page note are checked separately in `research/audits/source-package-portability-25.json`.
