# Current research status

Updated 2026-09-15 02:05 UTC. The goal remains active and incomplete. Authorized deadline: 2026-09-15 06:19:41 UTC (14:19:41 Shanghai). No new approval is required to continue within the authorized scope.

## Book and verification

The current built PDF has 399 pages, 28 chapters and an appendix. Its clean build is `tmp/build-checkpoint-12-review.log` (1743212 bytes). It includes completed audits through76. Snapshot11 remains immutable at334pages, SHA25614b0f61ecd8072ac6f5bb83a02aac759588a6a40e0788247ed07431e989d0a39. Snapshot12 is not yet frozen.

77 completed bounded Rethlas reports:74correct and3historical adverse reports, all resolved by subsequent repairs. Full reports through77 have been read, including77verification.json. These are reviews relative to stated prerequisites, not formal verification or novelty certification.

75 (determinant integrability) and76 (generic adjoints) passed and are included in399pages. Every normalized positive ddc-closed Gauduchon current has a determinant-weighted Lq density for1<q<n/(n-1), without BMP/PVP. Endpoint supremum is v_minus^(-1/n), including infinity. All supporting adjoint probabilities inherit subcritical bounds, and endpoint bounds under PVP. Generic supporting-probability uniqueness holds on an exact dense G-delta set; uniqueness for every continuous density remains a working conjecture.

77 local_big_continuity_01 passed. General Demailly94 curvature modulus and capped Kiselman localization were checked. It proves bounded Lp solutions in semipositive big backgrounds continuous on every open set where a given strict singular barrier is locally bounded. No BMP/PVP, prior continuity, or unproved power rate. Source `section_local_big_continuity.tex` is now INCLUDED after73 but NOT YET BUILT. The73closing paragraph and researchprogram references have been updated. Full report and JSON read; verifier may still be finishing its process.

## Active bounded audits

78 local_homogeneous_dirichlet_01, exec28654, log `research/rethlas/verification/run-logs/local-homogeneous-dirichlet.log`. Source `section_local_homogeneous_dirichlet.tex` NOT INCLUDED. Arbitrary smooth nonclosed background on a Euclidean ball; Guan–Li10 classical positive smooth Dirichlet input, explicit boundary barriers and translation comparison yield uniform Lipschitz bounds as epsilon tends to0 for smooth boundary data. C0 contraction extends to continuous boundary. Upper-test positivity gives domination of any continuous admissible competitor. Does NOT claim uniqueness among all arbitrary weak homogeneous solutions. The needed constructed maximal solution suffices.

79 big_continuous_contact_01, exec65513, log `research/rethlas/verification/run-logs/big-continuous-contact.log`. Source `section_big_continuous_contact.tex` NOT INCLUDED. Conditional on exact78statement, independently checks Demailly regularization of unbounded global envelope, local radius coercivity off analytic Z, removable extension, strict-barrier competitor and uniform smoothing => continuity offZ. Then78homogeneous replacement and scalar barrier/ordinary max pasting prove contact support for continuous obstacles, arbitrary bigtheta, noBMP. Include only if BOTH78 and79pass. General unbounded/quasicontinuous obstacle extension is NOT claimed.

## PDF review

All399pages were rendered at `tmp/pdfs/checkpoint-12-review/all`;23 contact boards. Boards01–12 (physical1–216) have now been viewed. No clipping. Minor theorem statement split at physical48→49: Needspace11 added before bounded-exact-regularization in chapter5, notyetbuilt. Physical65→66 polynomial damping theorem grouping can be improved. Detailed new75/76 and73/appendix reflow renders RUNNING exec69496 in `tmp/pdfs/checkpoint-12-review/new`, selected17pages. Need inspect these and remainingcontactboards13–23. Earlier full reviews and detailed73/74/program/appendix reviews are recorded in archived status. Latest399build fixed the75Lq overfull display and retains appendix/Holder Needspace repairs.

## Remaining reconstruction and research questions

General non-pluripolar measure existence under PVP is a published theorem, explicitly external in the manuscript, not a new conjecture. The fixed-measure dominated case is proved. For moving bounded references, the common envelope barrier gives genuine potentials in E but does not yet give finite mass of all lower roofs. Avoid unrestricted L1 mass semicontinuity, max-measure <=sum, commonE=>finiteMA, or capacity=>TV shortcuts. See `research/next-arguments.md` and the researchprogram chapter.

The continuous-obstacle contact route may remove part of the other recent external input; it does not yet reconstruct contact for every unbounded quasi-continuous obstacle. Higher-dimensional exact trace realization, unrestricted singularity topology/I-goodness, lower Bergman asymptotics and general birational/NA recovery remain clearly stated research directions, not proved claims.

## Sources and workflow

38 archived primary PDFs, checksums in `research/sources/manifest.json`. New38GL10: published AdvMath225(2010)1185–1223,39pages; full intro and Theorem1.1 read. Arbitrary smoothchi allowed; local positive-density Dirichlet under strictsubsolution, no closedness. Primary https://people.math.osu.edu/guan.19/Papers/Guan-Li.aim.pdf; arxiv0910.1851. Ours potential=pi times source. Other recent37sources and exact conventions are in literature.md and the archived status.

Use the copied Rethlas workspace, ordinary --approve-for-me only. Original sourcebook/Rethlas unchanged. Root never writes verifier memory or result JSON. No collaboration agents. Transient approval-review timeouts in77were recovered by permitted retries; no outstanding rejection/block.

Build: `bash scripts/build-book.sh > tmp/build-NAME.log 2>&1`. Rich Python: `/Users/mingchen/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`. Maintain concise progress commentary. Continue useful work until the authorized deadline; do not mark the goal complete merely because a build succeeds.


02:11UTC: ALL399physicalpages contactreviewed (boards01–23). All17 selected detailed pages reviewed (newboards01–06):73/71reflow164–167,76at212–213,75at343–346,appendix389–395. No clipping, previousappendix/Holderstatement grouping repairs verified. Needspace repairs now added before75endpointtheorem (344→345split), nef-degeneration-kahler proposition(354→355split), holderproofparameterdisplay(166→167phrase), andchapter5boundedregularization(previouslynoted). Awaitbuild andaffectedpage review. Polynomialdamping already hasNeedspace15 and its long statement startsfreshon66; no additional repair needed.

New user direction: explicitly explore interaction with open problems in non-Kahler geometry. Acknowledged and researching primary sources: Demailly–Paun nef/big/FujikiclassC, positive lower volume/endpoint Gaud determinant, Hermitian null loci, and balanced/pluriclosed or Hermitian-symplectic geometry. Integrate a substantial precise section, not merely a promise. Preserve currentstatus/solvepublishedvsopen distinction.


02:37UTC update: 78local_homogeneous_dirichlet_01 and79big_continuous_contact_01 BOTH passed; FULL reports and finalJSON read. Now79completed audits=76correct+3historical resolved adverse. 78and79 INCLUDED after77 in chapter12, notyetbuilt. Chapter11 andprogram acknowledge continuous-obstacle generalbigcontact now reconstructed withoutBMP, full unbounded/quasicont extension still external. 403page77build clean and localized review completed, with further section/lemma grouping repairs pendingbuild. All399priorpages alreadycontactreviewed. Checkpoint12NOTfrozen.

80 smooth_cone_flow_01 ACTIVE exec4223, input/runlog smooth-cone-flow. New section_smooth_cone_duality.tex NOTINCLUDED. NEW draft section_non_kahler_geometry.tex NOTINCLUDED/NOTAUDITED. CoversDP closednef/big, universalPVPendpoint, Dangnull/ChernRicci, balancedpluriclosed, andMorse. Needboundedreference/derivationaudit, properprimarycitations. NewprimarysourcesDP04(arxivv2numeration0.6/0.7),DangNull26v2,FV26,Chiose14authorPDF,Tosatti26preprintarchivedandmainstatementsread. Bibliographyadded.

NEW user supplied https://mingchenxia.github.io/Papers/NUMA_vibe.pdf. FULL6pages read, fractions/cutoffs visually checked pp3–4. Source44NUMA-Xia.pdf/.txt SHA7482f76f0c53776c313c34cb287e7cb2f71e6a066e4955cba364e70b6d0b72a5. No author/date printed; bibNUMA says suppliedbyMingchenXia, undatedretrieved15Sep, no inventedauthorship. Main result smoothnonunique normalizedzeroexponent solutions for smoothnonnegative densityzeroonopenband, nonclosedHermitianbackgroundonP3; BMPstillholds. Scalaruniqueness/exponentialuniqueness unaffected. ContinuouslogdensityF adjointconjecture NOTrefuted (logf=-infinity onband). Sourceempty-interior-zero-set uniquenessquestion remains. UseracknowledgedinChineseandexplainedimpact.

81 degenerate_nonuniqueness_01 ACTIVE exec42940, runlog degenerate-nonuniqueness. Full proof adaptation section_degenerate_nonuniqueness.tex NOTINCLUDED untilauditpasses. Sourceoperator2ipartialbarpartial=4pi ours; allformsdivided4pi scalarfunctionsunchanged. Added explicitBMPproofviaomega<=CFubiniStudy, mixedpositivity/closedboundedStokes. Wholebookuniquenesssearch foundexistingstatementsalreadycareful: smoothstrictpositive, exponentiallambda>0, orscalar-only. Need addcrossrefs/sourcecounterexample toweak/prescribed/normalization/program, and preciselyformulatenewopenquestion. Source81inputincludesimpactcheck. Noaudit82yet.
