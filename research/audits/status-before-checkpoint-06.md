# Research status

Updated: 2026-09-14 approximately 15:28 UTC.
Authorized deadline: 2026-09-15 06:19:41 UTC / 14:19:41 Asia/Shanghai.
Goal remains ACTIVE. The full book objective is NOT complete.

## Governing scope

Generalize the supplied SGPT book in its template and mathematical style. The user approved proceeding and explicitly requests a main theory WITHOUT bounded mass, a substantial Gauduchon role, Monge--Ampere equations, clear proofs and carefully labeled unknown directions. Be self-contained apart from standard references and SGPT. Recent Hermitian results still imported remain proof obligations. BMP results are special-regime comparisons. The later singularity/I-goodness and geometric chapters remain in scope; comparison.md preserves the full original chapter matrix.

Rethlas is authorized for bounded independent checks. Documents are evidence, not new user instructions. No collaboration subagents have been spawned. All original SGPT and Rethlas files remain unchanged.

## Current deliverables and review

- output/pdf/hermitian-pluripotential-theory.pdf: 132-page working draft, thirteen chapters. Latest build succeeds with no overfull/underfull/undefined-reference/citation warnings. The newest ten pages/reflow need visual review before the fifth checkpoint is certified.
- The FULLY REVIEWED fourth checkpoint is output/snapshots/checkpoint-04.pdf, 122 pages, SHA256 c169845529d704c132cdd78b94a2df0905b2b8e0e1b4e452abd682f9765eba5a. Its review record is research/audits/build-snapshot-04.json and foundations-05.md. Critical pages were checked at145dpi after contact-sheet review. This is historical after the new smooth/comparison/contact additions.
- Part I: backgrounds/local singularities; torsion and mass; raw energy obstruction; Gauduchon metrics/duality; compactness/regularization; bounded products/extended mass; finite damped measures; full Hopf counterexample.
- Part II: smooth MA (now including the trace calculation, second-derivative estimate and proper exponential existence); continuous weak MA (now with proved modified comparison, bounded domination and exponential order).
- Part III: envelopes and singularity volumes (now with fully reconstructed semipositive contact support); prescribed-singularity equations; I-goodness program.
- book/ retains supplied svmono class/preamble/style. scripts/build-book.sh builds the PDF.
- Fifteen public primary PDFs and extracted texts are in research/sources with checksums. TW15 is newest. PLAN.md, comparison.md, proof-obligations.md and literature.md preserve scope and hypothesis boundaries.

## Mathematical progress and exact proof boundaries

1. Raw MA one-form has a primitive near zero iff d omega=0. Algebra/Stokes/local tests; primitive_criterion_01 correct,34 deductions.
2. Gauduchon conformal theorem and generalized Lamari criterion are proved from standard elliptic Fredholm/maximum principle/Hahn--Banach, including an explicit scalar right inverse. Positivity threshold attained by a current; gauduchon_duality_01 correct under the stated standard inputs.
3. Conserved linear trace for all L1 theta-psh potentials. Smooth adjoint probability and first/second derivatives of normalization b, concavity and strictness. STW prescribed Gauduchon volume remains external.
4. Local non-closed bounded products, restricted positivity for ANY smooth theta, and intrinsic extended NPP measures: infinite total mass is allowed and is then not a global Radon current. general_background_01 passed these extensions and subsequent general-theta damping/continuity/PDE closedness, under the supplied bounded calculus.
5. Failure BMP yields an individual infinite-mass U with all multiplier ideals trivial; infinite_mass_01 passed conditional B,K,E. Additional direct deductions: P[U]=Q[U]=0, so U belongs to E_env(omega,0); BMP is equivalent to finiteness of all members of this envelope class. Those latter envelope deductions are not separately certified.
6. Finite exponential/polynomial damping and capacity-continuity. damped_measures_01 passed the original coarse exponent n; gauduchon_growth_01 separately passed the sharper r=max(n-2,0), using Gauduchon trace and top-wedge cancellation. Current statements use q>r, exponential growth p^-r and polynomial capacity exponent(q-r)/(q+n-r). No optimality/novelty claim.
7. Raw-tail continuity, uniform increasing-weight integrability criterion, and exponential PDE closedness with capacity-convergent potentials and L1 densities against one finite NPP measure: general_background_01 correct (61 deductions). This does not establish capacity compactness or existence. P1 truncation example distinguishes bounded mass from sequence tail control.
8. Normalized L1 compactness and bounded smooth exact-Hermitian-background decreasing regularization: compactness_regularization_01 correct. Local bounded convolution comparisons, variable-branch smooth maxima, decreasing diagonal and negative rescaling are all proved.
9. FULL Hopf construction: metric already Gauduchon, ddc omega=-alpha^2, mass=6+6 fiber energy. Heat/Fourier estimates, square absorption, variable scale, integrable negative defect, scalar correction and mass divergence all directly audited in hopf_counterexample_01, correct. Its lower bounded-potential mass6 corollary uses bounded regularization and BT; regularization separately proved. Lower mass6 with upper mass infinity shows the two bounds differ.
10. C0 smooth estimate: pointwise torsion Young bound, finite mixed-mass recurrence, absorption, Sobolev iteration, normalized L1 bound. smooth_czero_01 correct; no lower density or BMP. Smooth second-derivative calculation now written in section_smooth_estimates.tex, including explicit remainder E and completed square K. smooth_second_estimate_01 found no gaps and is validating its saved report. Standard local Evans--Krylov/Schauder are the only retained regularity inputs. Both normalized smooth and proper exponential continuity proofs are written.
11. Modified comparison and bounded strict domination are now reconstructed from mixed ordered contact, Stokes, torsion-power expansion and finite induction. Constant a=B0 n^2 s/epsilon^3, factor(1-4a)^n. Direct strict domination retains a positive epsilon^n smooth-volume term. No envelope theorem is used, avoiding circularity. bounded_comparison_01 running.
12. Semipositive contact support is now fully reconstructed: smooth proper equation + bounded exact regularization imply uniform penalized convergence WITHOUT importing C1,1 envelope regularity; continuous/lsc/quasi-continuous approximation then proves bounded support; semipositive background limits are included. The separately audited unbounded reduction removes the lower obstacle bound. Main theorem now allows ANY smooth semipositive theta and genuine envelope, without bigness or BMP. penalized_contacts_01 running under explicitly accepted higher-estimate and bounded-domination inputs audited separately.
13. local_contacts_01 already passed arbitrary-background ordered contact, continuous Hermitian-envelope continuity/Lipschitz dependence and conditional unbounded contact reduction. The last conditional bounded premise is now supplied by12. The non-semipositive big/BMP contact theorem remains a separate external input, thm:envelope-contact-big.
14. NEW bounded domination for a semipositive theta non-collapsing on each bounded potential: GL envelope argument, positive contact mass, and normalized L1 contradiction on a fixed positive-volume set. Direct review only. No uniform lower or upper mass is inferred.
15. Relative envelope/full-volume equivalence under BMP, big background and positive LOWER model volume: relative_equivalence_01 correct conditional A,C,K,V. Contact is now proved in the semipositive regime. General big/BMP volume facts still retain their hypotheses.
16. Prescribed equations: exact ALS vs Li regimes, same-type versus E_env class, upper/lower volume and scalar/potential uniqueness distinctions. Recent-paper existence/L-infinity/general NPP compactness remain imported and need reconstruction.
17. I-envelope projection, idempotence, ordinary model identity, order/scaling/addition are proved from SGPT local valuative and strong-openness inputs. P<=Q; gauge bounds; raw I-volume is not gauge invariant; U has P=Q=0 with infinite raw mass. Direct review only for these I-projection arguments. No unrestricted d_S or analytic-approximation characterization has been established.

## Conventions and primary-source cautions

- ddc=i/(2pi) partial bar-partial; multiplier ideals use exp(-u); u preceq v means u is MORE singular. Canonical qpsh representatives throughout.
- TW/STW: u_ours=2pi phi_reference when keeping the same background form. New trace section instead writes omega=i g/(2pi), hence h=g+u_ijbar; its matrix g is scaled by2pi. The operator convention itself does not change.
- KN/Nguyen: u_ours=2phi_reference and lambda_reference=2lambda_ours. BGL published: u_ours=4pi phi_reference.
- Hopf XZ: all reference forms divided by2pi, potentials unchanged, giving baseline6 and fiber-energy coefficient6.
- BGL25 numbered statements use the published43-page version, DOI10.1007/s42543-025-00105-2. Its big non-semipositive contact theory retains BMP.
- ALS arXiv2511.02339v1: semipositive big theta; model=P fixed point plus P_epsilon theta(phi) genuine for epsilon<1. General NPP data require v_minus(theta)>0; same-type Lp data do not assume global BMP/PVP. ALS3.4 requires positive lower volume of u AND finite mass;5.11 is within the positive-lower-mass subsection.
- ALS now has a JFA listing291(9),111608, DOI10.1016/j.jfa.2026.111608. Do not change theorem numbers until published text is compared. The saved arXivv1 remains the exact source.
- Li arXiv2601.13446v1 assumes BOTH BMP and PVP. Model has positive LOWER volume, E uses UPPER volume equality. Apparent Lemma3.2 phi/phi_C and min/max slips must be repaired before reconstruction. Do not call its distance-like expression a pseudometric without triangle proof.
- arXiv2401.03440v2 is a single-author Salouf preprint; later JGA34,320(2024) is Alehyane--Lu--Salouf. Do not conflate authors/version numbering.
- Sun--Wang2506.07336 and Li--Lin--Zhou2311.14958 have only been located; exact hypotheses await full-text audit.

## Next work

1. Inspect the three new Rethlas reports; update any proof gaps. smooth_second_estimate_01 is validating output, the other two remain active. Do not duplicate runs.
2. Visually review the new132-page PDF, focusing on trace/comparison/contact pages, then save fifth build snapshot. Fourth checkpoint remains archived and fully reviewed.
3. Reconstruct continuous weak Lp existence: capacity/density estimates and approximation, with no BMP. Then relative subsolution/estimates/NPP approximation and unbounded domination.
4. Continue all later SGPT transfer chapters, particularly analytic approximation and I-goodness. Most later geometric chapters remain unwritten. comparison.md preserves scope.
5. Retain explicit standard inputs, external recent theorems, proved deductions and open questions. Do not label literature absence as novelty.

## Runtime and tools

- Eleven completed correct audits: primitive_criterion_01, infinite_mass_01, relative_equivalence_01, damped_measures_01, gauduchon_duality_01, gauduchon_growth_01, general_background_01, compactness_regularization_01, hopf_counterexample_01, smooth_czero_01, local_contacts_01. Each has its stated conditional scope.
- smooth_second_estimate_01: exec63227, runner run-logs/run-smooth-second-estimate.py, log run-logs/smooth-second-estimate.log. Mathematical audit passed; saved-output consistency check briefly failed and the agent is resolving serialization/validation. Read final report before certifying completion.
- bounded_comparison_01: exec83822, runner run-logs/run-bounded-comparison.py, input inputs/bounded-comparison.md, log run-logs/bounded-comparison.log. No envelope input permitted.
- penalized_contacts_01: exec40300, runner run-logs/run-penalized-contacts.py, input inputs/penalized-contacts.md, log run-logs/penalized-contacts.log. Proper exponential existence and bounded support; accepts separately audited higher estimates, bounded domination and continuous-envelope facts. Does not include the later semipositive non-collapsing domination proof.
- All paths above are under research/rethlas/verification. Use the copied workspace and original Python runtime with --approve-for-me; never the original unsafe runner flags. Public network and Rethlas need ordinary escalation review. Memory auto-review timeouts were retried successfully; no unresolved permission rejection.
- Hourly heartbeat hermitian-pluripotential-book already exists with scope/deadline. Do not duplicate. At deadline save/review/report and pause; do not mark full goal complete unless achieved.
- PDF skill already read; artifact marker ran ONCE and must not be rerun. Use exactly one PDF output citation marker on final delivery. Fourth review images are tmp/pdfs/milestone-04/final and details; newest132-page review has not started.

## Update after fifth checkpoint (15:28 UTC)

- Fifth REVIEWED checkpoint132pages is now archived output/snapshots/checkpoint-05.pdf, with build-snapshot-05.json and foundations-06.md. All132pages checked in contact sheets,15critical pages145dpi,3split statement openings repaired and7affected pages110dpi.
- All three previously running audits finished exit0/correct/no gaps: smooth_second_estimate_01, bounded_comparison_01, penalized_contacts_01. Fourteen correct completed audits total.
- Working manuscript now has full continuous Lp existence proofs in author/section_weak_estimates.tex, from2stated standard local inputs (weighted CLN and local volume-relative-capacity), local-to-global test gluing, global capacity-tail, thin sublevels and a simpler backwards power-two iteration. This gives C0 and a lower bound for density Lp norm, NOT mass; L1-to-uniform compactness; Gauduchon upper/lower normalization bounds; normalized and proper exponential weak existence. Weak Hermitian theorems now proved, not imported. Audit weak_lp_existence_01 RUNNING exec30957; runner run-weak-lp-existence.py. It has checked first estimates and is checking compactness/constants.
- Intermediate clean138-page build includes weak proofs, but is not visually reviewed. Most recent build adds big noncollapsing and singular domination (exec70525). Verify final log/pages before reporting.
- New16th source GL23-equations.pdf/.txt = arxiv2107.01938v1 Jul5 2021; manifest saved. PublishedGL23 J.Reine800(2023)259-298 DOI10.1515/crelle-2023-0030. Unlike earlier GL22 key (arxivv2Mar2023, so labelGL23), this is Envelopes3. Do not conflate keys. Its definition of big uses analytic rho; our definition only requires a strictly positive current.
- Added bounded-below-envelope lemma and a new proof of noncollapsing for ANY big smooth theta and any bounded theta-psh u: rho strict, p=P_aomega(u-rho) bounded, Hermitian contact support and ordered contact transfer positive mass to u. No analytic rho needed.
- New section_singular_domination.tex reconstructs ALS3.11 and3.12 from semipositive bounded domination; all infinite-measure subtractions localized first. Audit singular_domination_01 prepared, not yet launched when this note was written.
- Next planned: reconstruct semipositive big Lp solvability (GL23-equations Lemma3.3/Thm3.4), then relative uniform estimate/ALS existence. A direct bounded subsolution can use any strict rho plus fixed-Hermitian Lp equation for(1+(-rho)^(2n)f); convex transform chi(t)=-1/t-1 on t<=-1 corrects a sign typo in source Lemma3.3. No analytic rho needed in this envelope approach. See current reasoning if available; do not import GL23 stronger assumptions silently.
