# Normalized exponential limits and a shorter existence proof

23 September 2026. Focused review for checkpoint91, not whole-book certification or a novelty claim.

## Argument and dependency order

Section 13.19 now contains the existing reference stability and compactness theorem. Section 13.20 retains positive-exponent existence and gives a shorter zero-exponent proof. Section 13.21 retains local Holder continuity and adds subsection 13.21.1 on normalized exponential limits. Interior smoothness remains Section 13.22. V_theta was already defined in Chapter12. Stability uses the earlier subsolution and strict-barrier comparison results, so this order has no circular dependence on zero-exponent existence. The positive-exponent construction varies analytic types and retains its envelope passage unchanged.

The uniform estimates for all real parameters 0<lambda<=1 are proved once as a lemma. A Gauduchon trace and normalized quasi-psh compactness bound c_lambda above. Skoda integrability and the reference-preserving subsolution with reference V_theta-1 and barrier rho-1 give its positive lower bound. Exponential order gives V_theta-B<=v_lambda<=V_theta. The scalar and exponential comparison orientations were checked directly. These estimates use neither metric mass property.

For lambda=1/j, fixed-reference compactness upgrades L1 convergence to uniform convergence of differences on Omega and identifies the limiting density. Dominated convergence against f^p gives strong Lp convergence to cf. Thus the existing normalized existence statement needs no second pair of tail envelopes. This is a simplification of the proof, not a stronger existence theorem.

For the full family, the fixed lower bound gives 0<=1-exp(lambda v_lambda)<=1-exp(lambda(V_theta-B)) away from the pole set. Dominated convergence proves whole-family density convergence. Every potential cluster solves the zero-exponent equation, and scalar uniqueness gives whole-family scalar convergence. Uniform local Holder estimates and interpolation upgrade the same subsequence to every compact and every strict sub-endpoint Holder exponent. These are consequences of the internally proved inputs, without a novelty claim.

If biholomorphisms preserve theta and f dV, the envelope definition gives invariance of V_theta. Positive-exponent uniqueness gives invariance of the exponential solutions. L1 continuity of pullback gives invariance of cluster limits; the chosen barrier and Omega need not be preserved. Whole-family potential convergence is asserted only if the normalized minimal equation has a unique invariant solution. General potential uniqueness and unconditional selection are not asserted.

## Independent review and second pass

Normal Rethlas run `big_exponential_compactness_01` returned correct, with no critical errors or gaps, under its explicitly listed established internal and classical inputs. Its immutable submission contains the old uniform estimates plus the shortened ending, and a proposition with the all-real-parameter uniform estimates in its proof. The final text factors that latter checked subproof into the preceding uniform-type lemma and cites it twice. This editorial factoring, shifted-reference clarification, statement preservation and dependency order were checked separately by the primary agent; the report is not described as a verbatim review of the final layout. The earlier correct stability and Holder reports remain the inputs of this bounded review, not results re-audited here.

The final pass preserves every prior formal statement in the affected inputs, the entire positive-exponent construction, and the moved stability/Holder proofs. Three formal blocks are added: uniform bounds, exponential cluster limits, and the conditional symmetry corollary. The supplied original TeX files and all 176 previous reports are unchanged. The original adverse interior-regularity report is not relabelled. The separate nef incomplete-metric draft remains unverified and inactive.

The published BGL25 proof of Theorem 4.7 was reread against the shorter argument; attribution to Theorems 4.6–4.7 remains. The Springer published record and Dang's author research page were checked on 23 September 2026; the latter lists the regularity paper with an arXiv link and no journal entry. No new external theorem or Popovici result is used.

Primary pages: https://link.springer.com/article/10.1007/s42543-025-00105-2 and https://quangtuandang.github.io/Webpage/research.html .

The combined final production has 712 pages. All 46 selected pages covering the moved and new results, the complete revised interior-smoothness section, chapter introduction, transitions, contents, research discussion and bibliography were rendered and read. After the final affine-operator definition was added, physical pages 268–269 were reread and the other 44 selected images were pixel-identical. The seven-input house audit has 0 errors and 16 inherited warnings: existing labels/topology prompts, the recognized Demailly theorem title and existing preprint metadata. Exact preservation and production checks are recorded in `../audits/build-snapshot-91.json`; clean reconstruction is recorded in `../audits/source-package-portability-91.json`, which must pass before the release procedure is complete. The Archive integration has its own focused review and does not strengthen the original source's unsupported local-density-only claim.

The final synchronization check removed one trailing blank line at EOF from the split stability input. A fresh build preserves every one of the 712 page texts and all 46 selected rendered images exactly. The source map records the final source checksum.
