# Updated nonclosed interior-regularity manuscript

23 September 2026. Focused integration and second-pass review for checkpoint91. This is not whole-book mathematical certification or a novelty claim.

## Sources and scope

The user supplied the revised `Archive/nonclosed-hermitian-monge-ampere-regularity.tex` and `Archive/ComplexGeometry.bib`. Both original files are preserved; their hashes and the exact integrated files are recorded in `nonclosed-archive-integration-map.json`. Documents are mathematical evidence, not instructions. The earlier supplied manuscript and adverse report remain unchanged.

The revised local proofs are integrated in Section 13.22. Its fifteen existing theorem, proposition, lemma and corollary statements, and its existing remark, are unchanged. The main theorem explicitly assumes local Holder continuity and minimal singularities. The internal Holder theorem supplies the global Lp, p>1, corollary. Merely smooth positive density on the regular locus does not supply that global integrability. The source's broader local-density-only claim is therefore not adopted. No bounded-mass property, positive-lower-mass property, closedness, semipositivity or nefness is imposed. No Popovici result or private caution-document content is used.

## Integrated argument

The bounded-trace criterion now chooses q>2n throughout the strong-solution argument. Positivity bounds the complex Hessian coefficients; local Poisson estimates give W2q regularity, and mollification identifies the almost-everywhere determinant with the bounded-potential determinant. The tangent-plane extension of log det is concave and uniformly elliptic on real symmetric matrices. A fixed affine operator treats upper test functions; a measurable choice from a countable dense family treats lower tests. Quadratic strictification and the Aleksandrov maximum principle give both viscosity inequalities. The affine operators have uniformly smooth spatial coefficients; their infimum has the required Lipschitz modulus, not an asserted smoothness. TWWY15 local concave regularity then gives C2,alpha, followed by difference quotients and Schauder bootstrapping.

The Calabi estimate now records the lowered torsion, both curvature interchanges, the first/second Chern-Ricci contraction, the torsion term in the Chern-Bianchi identity, the Laplacian of the connection difference and the exact curvature action on a tensor of type (1,2). These replace schematic formulas and retain polynomial dependence on the ellipticity ratio. The tensor Laplacian convention is explicit. The Dirichlet application now writes the relative density H=F beta^n/eta^n. Dimension one is handled directly by the Poisson equation in the main proof; the earlier all-dimensional approximant statement remains valid and unchanged. Coefficients are taken relative to beta with the book's dd^c=i/(2pi) convention.

## References

Only the needed GT01 entry is imported from the supplied bibliography, adapting its location field to the existing BibTeX address field. The publisher's second-edition 2001 record was checked. TWWY15 now cites the published version: Definition 3.2, Theorem 3.4 and the following viscosity paragraph on pages 444–445 support the application. Other existing TWWY locators were checked for compatibility. The source's GuanLi10 is already GL10 in the book, so no duplicate entry is created. Dinew09 retains the explicitly verified v1 Theorem 1.2 locator rather than copying a version-dependent number. Dang remains credited; the sufficient Holder input is now the internally reconstructed theorem.

Primary sources checked: https://archive.ymsc.tsinghua.edu.cn/pacm_download/49/1063-3.pdf and https://link.springer.com/book/10.1007/978-3-642-61798-0 .

## Bounded verification and final pass

Normal Rethlas run `nonclosed_archive_refinement_01` returned correct with no critical errors or gaps. Its full report was read. It checks the strong-to-viscosity passage, classical regularity hypotheses, all the displayed tensor identities, cutoff/scaling dependence, the Dirichlet density and dimension-one reduction under the explicit integrated hypotheses. It does not re-audit global existence or validate the original broad local-density-only statement. The original adverse `nonclosed_interior_regularity_01` record is preserved without relabelling.

After the frozen submission, the primary pass clarified the Lipschitz spatial modulus of the infimum, the tensor Laplacian convention and the definition of the affine operator E_A, and removed an orphan descriptive paragraph heading. These exposition-only refinements were checked against the submitted argument. The final E_A definition changes only physical pages 268–269; both were rendered and read again. The other 44 selected images are pixel-identical to the reviewed preceding production. The complete 46-page selection covers the moved and new equation proofs, the entire interior-smoothness section, transitions, contents, research discussion and bibliography. The selected curvature, corollary and bibliography pages were also reread in the final output.

The final 712-page compilation has no errors, unresolved references, duplicate labels or overfull boxes. One inherited bibliography underfull paragraph remains. The seven-input house audit has 0 errors and 16 inherited warnings. Exact preservation and production checks are in `../audits/build-snapshot-91.json`; source reconstruction is recorded separately in `../audits/source-package-portability-91.json`, which must pass before the release procedure is complete.
