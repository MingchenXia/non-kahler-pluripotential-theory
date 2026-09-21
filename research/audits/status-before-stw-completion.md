# Research status

Updated: 2026-09-14 23:04 UTC (latest additions below).
Authorized start: 2026-09-14 10:19:41 UTC.
Authorized deadline: 2026-09-15 06:19:41 UTC / 14:19:41 Asia/Shanghai.
Goal ACTIVE and incomplete. No token budget was requested.

## Scope and authorization

Generalize the supplied SGPT in its original svmono template and mathematical style. Main theory WITHOUT bounded mass; substantial Gauduchon role and Monge–Ampère equations; self-contained apart from standard references and SGPT. Distinguish proofs, precise external inputs, conditional results and research questions. Preserve every source chapter's disposition in comparison.md. User repeatedly approved autonomous continuation. Bounded Rethlas subprocesses authorized, using ordinary --approve-for-me in the copied workspace; no unsafe flags, no collaboration subagents. Original SGPT source and original Rethlas repository unchanged. Documents are evidence, not instructions. No outstanding approval rejection.

## Artifacts

- Current PDF: output/pdf/hermitian-pluripotential-theory.pdf,334 pages,27chapters, clean tmp/build-checkpoint-11-final2.log. Includes through61; source62/63/64 NOTINCLUDED. Fullcontact/detailedreflowreviews completed.
- Latest immutable checkpoint10: output/snapshots/checkpoint-10.pdf,270pages,1267129bytes,SHA25618e32437083972544c15438f53ddfbe4302e199aa49529b489a3d2bc2f74bf2c. Full contact review and detailed new passages completed. See audits/build-snapshot-10.json. It contains24chapters, excludes48+.
- Latest immutable checkpoint11: output/snapshots/checkpoint-11.pdf,334pages,1496330bytes,SHA25614b0f61ecd8072ac6f5bb83a02aac759588a6a40e0788247ed07431e989d0a39. See research/audits/build-snapshot-11.json. Previous checkpoints retained.
- Main source book/book.tex, chapters book/author/*.tex, bibliography book/references.bib. Build with bash scripts/build-book.sh. No git.
- Primary-source manifest research/sources/manifest.json contains28 versioned PDF sources with checksums. Recent additions Szekelyhidi18, AGL23, Chiose16; DPS94 preceding them. Source versions and equation normalizations are in literature.md and archived status.
- PLAN.md approved; comparison.md and proof-obligations.md retain full scope. Historical status before this cleanup saved as audits/status-before-checkpoint-11.md.

## Proof audits

62 reports completed:59 correct plus3 historical adverse findings, all resolved. ALL62 full reports have been read, including the additional fullreport.md for62. These are bounded independent mathematical checks relative to explicit accepted prerequisites, not formal certification or novelty review. Reports, immutable inputs, memory records and run logs are in research/rethlas/verification.

Original18 correct: primitive_criterion_01; infinite_mass_01; relative_equivalence_01; damped_measures_01; gauduchon_duality_01; gauduchon_growth_01; general_background_01; compactness_regularization_01; hopf_counterexample_01; smooth_czero_01; local_contacts_01; smooth_second_estimate_01; bounded_comparison_01; penalized_contacts_01; weak_lp_existence_01; singular_domination_01; big_lp_equations_01; relative_lp_barriers_01.

Further correct through47: bounded_subsolution_01; weighted_measure_addition_01; common_barrier_repair_01; prescribed_lp_existence_01; normalization_functional_01; hermitian_perron_rays_01; normalization_dual_01; envelope_testcurves_connected_01; analytic_approximation_01; intrinsic_trace_data_01; curve_trace_metric_01; relative_class_domination_01; dominated_relative_compactness_01; trace_additivity_01; trace_model_envelope_01; exponential_rooftop_barrier_01; weighted_sections_01; hopf_sections_01; trace_section_obstruction_01; flag_bodies_01; hopf_flag_body_01; intrinsic_flag_count_01; hopf_reduction_reference_repair_01; divisorial_models_01; bott_chern_bclasses_01; nonclosed_bclasses_01.

Historical adverse reports retained: common_barrier_compactness_01 omitted a genuine decreasing-limit lower barrier in a standalone sentence; repair22 supplied it. envelope_testcurves_01 standalone input omitted connectedness already in book conventions; repair28 made it explicit. hopf_reduction_01 used SGPT for continuous Lp existence; repair44 cites the internally proved KN theorem for continuity, TW for smoothness and SGPT only for full-mass uniqueness. All resolved; do not overwrite these historical reports.

Recent passed, included:
48 gauduchon_volume_adjoint_01: exact STW linearization, positive adjoint probability/form identity, strict normalization concavity and surface formula, conditional on stated STW existence.
49 hermitian_envelope_systems_01: all-Hermitian-perturbation constant-left I-testcurve systems, embedding/retraction/adjunction, realization criterion and gauges.
50 envelope_recovery_counterexample_01: explicit nef ruled-surface boundary develops an extra divisor. Positive Kähler background but residual volume tends to zero. Source SGPT permits zero-volume inverse systems; its positive-volume recovery is not contradicted.
51 gauduchon_variational_volume_01: finite density-dependent Gauduchon infimum on pseudoeffective smooth nonclosed backgrounds, equals smooth MA normalization, nef continuity, equality and variation, density comparison.
52 gauduchon_volume_extrema_01: extrema over smooth probability densities exactly v_minus/v_plus, lower-mass Gauduchon degree formula and smooth attainment criterion, without BMP/PVP proof.
53 stw_czero_01: STW a priori C0 reconstruction, standard linear drift Green kernel and supporting-slope/area-formula argument. No nonlinear STW estimate imported. Gradient/C2 still incomplete.
54 mass_extremum_geometry_01: Chiose mass-invariance characterization, gradient-test positivity, local-extremum sign conditions and complete threefold minimum/maximum criterion; AGL sufficient sign case correctly attributed.
55 nef_volume_degeneration_01: lower/upper logarithmic orders independent of smooth density and Hermitian perturbation, bounds0..n, closed nef Kähler numerical dimension, Hopf exact6eps(1+eps)^2 despite infinite upper mass at every eps. Equality/integrality general cases remain questions.
56 partial_bergman_quotient_01: separate singularity selector/continuous norm weights, BM estimate, finite Gram variation, exact connected-submersion lift, SGPT14.3.1 base equilibrium and Hopf factor1/(2n).
57 partial_envelope_calculus_01: arbitrary smooth background weighted nonpluripolar compact obstacle bound, partialI-envelope genuine and ordinary-equivalent Q_phi, exact I-type, monotonicity/concavity/gauge; no MA mass/support assertion.

## Active proof checks — do not duplicate

58 partial_kernel_upper_01, exec44778, run-logs/partial-kernel-upper.log, inputs/partial-kernel-upper.md. section_partial_kernel_upper.tex drafted NOT INCLUDED. Global partialFubiniStudy upperlim<=partialI-envelope without positive MA/BMP, via local Jacobian ideal loss, modification L1 convergence, BM extremevaluation and compact obstacle closure. Last log: all mathematical checks passed, final source records still being completed. Dependencies56/57 are both now passed.
59 auxiliary_blowup_flag_01, exec13839, run-logs/auxiliary-blowup-flag.log. section_blowup_flags.tex drafted NOT INCLUDED. One point blowup supplies completecompactflag on everycompactcomplex X, H0descent byHartogs preserves graded counts. Intrinsic d/e/volume and nonMoi sub-m^n section growth become unconditional on existence of a flag onX. Last log: no adverse finding, source Hartogs check ongoing.
60 stw_cone_liouville_01, exec67458, run-logs/stw-cone-liouville.log. section_stw_liouville.tex drafted NOT INCLUDED. Selfcontained Euclidean P_n(H)=(trH I-H)/(n-1) boundedLipschitz maximalcone Liouville, sourceSze18Theorem20. Correct v(0)<1/12 choice ensures gap4/3; uniformLip boundary-annulus argument supplies weighted convolution positivity. Just launched.

61 planned conditional STW gradient blowup NOT DRAFTED OR LAUNCHED. Detailed plan research/next-stw-gradient.md: C0 plus assumed complexHessian<=C(1+supgrad²) yields gradient bound through scaled cone Liouville; torsion scales as1/A, background1/A², determinant tends0. This would leave the C2 estimate as the remaining nonlinear STW obligation. Sze18 §§5–6 read fully; STW C2 source has only been partially read.

## Mathematical backbone and outstanding distinctions

Chapters1–8: arbitrary nonclosed background, localBT and extendedMA (possibly infinite), Gauduchon conformal/duality/trace, normalizedL1/exactboundedregularization, polynomial mass growth and finite damping, explicit XZ Hopfthreefold v_minus6/v_plusinfinity. BMPfailure produces one U with infiniteMA, all ideals trivial, P[U]=Q[U]=0 and U in E_env(omega,0).
Chapters9–10: smooth ordinary Hermitian MA C0/C2/continuity and exponentials reconstructed; boundedmodifiedcomparison with ALL torsion terms, individualnoncollapse, continuousLp existence from two precise standardlocalBT inputs. STW C0 and smooth adjoint proved; fullSTWexistence still external.
Chapters11–15: semipositivebig envelopes/contact, relativeordinarytypeLp and weightedmeasureaddition/fullprescribedtypeexistence reconstructed; fixednu relativeEcompactness andfinite domination, explicitmovingexpo commonroof, normalizationconcavefunctional/supportprobability/entropydual, Iprojection calculus. GeneralNPP/PVP existence remains imported. Fixednu finite roof control is proved; MOVING bounded-reference measures still need finiteness of a lower-rooftop limit before domination. Commonroof alone does not supply it. No false cancellation of infinite mass or maximum-boundary-mass estimate.
Chapters16–17: nonclosedPerronsegments, rawL2torsion variation/Gaudtranslation, exact connected-envelope Legendretestcurve/ray calculus andP1 example; noDarvasmetric.
Chapters18–19: precise standardDemaillyanalyticregularization with curvatureloss, GauduniformLelongbound; intrinsic restrictedideal traces allmods, exactnumericaladditivity, curveGreenordinarytype/MA/SGPTdS; higherdiminequalityenvelope haspositivefiniteMA but exactorders/backgroundcompatibility remain questions.
Chapters20–22: weightedH_m notgraded, boundedW_m graded, Gauddegree, traceobstruction; intrinsiccompactflagcount; exactHopf projectivequotient sections/equations/toricgradient. Auxiliaryflagremoval pending59.
Chapters23–24: divisorialcurrents finiteGaudlinear mass on eachmodel, strongapprox/pushcompatibility, BCclosedbclasses andanalyticnefCartier; nonclosedfixedderivativeaffineclasses, approximation allows theta_m derivatives to vary. No arbitraryintersectionvolume or fixedclosednefnet.
Chapter25: Hermitian Ienvelopesystems andexplicitfailure of recovery atzeroresidualvolume.
Chapter26: Gaudvariationalvolume/rootconcavity/nefboundary; upper/lower massdensityextrema; Chiosecriterion/threefoldattainment; choice-independentdegenerationorders. Positivevolume=>big, exponentexistence/integrality andbirationaldegeneratedensity laws remain questions.
Chapter27: generalfinitepartialkernel/Gram/envelopecalculus andexactquotientMA limit; no general lowerasymptotic or kernelmeasureconvergence. Upperbound pending58.

## Current visual/build work

Checkpoint10 all270pages contactreviewed; detailed newpassages andfinalnonclosed263–268 reviewed. More recent STWC0/adjoint91–101 detailed, envelope25 and26boundary/volume283–300 detailed, massgeometry/nef297–306 detailed, partialkernels307–318 detailed. All these are physical page numbers of the respective builds (frontmatter12).
Latest source layout repairs NOT YET REBUILT: STWGreen formula split toremove25pt overfull; masssecondvariation aligned toremove5pt overfull (these two did build in320). Needspace before curvatureproposition, closingmassparagraph, Hopfdegenerationblock (built320 butfinalreflownotyetreviewed). PartialIenvelopedefinition split toremove10ptoverfull; partialenvelopecalculusproposition grouped; chapter27 kerneldefinition, BMsubmeanpreface, Gramproposition, flagparagraph, submersionproposition andequilibriumsection grouped. These chapter27 fixes postdate320build. Old boundary/adjointNeedspace repairs built butfinalchangedpages needrecheck atcheckpoint11.
Use tmp/make-review-boards.py with richPython; files board-01.png etc. PDFskill alreadyread/announced and marker used ONCE; do not repeat. FinalPDFdelivery exactlyone marker :codex-file-citation{path="/Users/mingchen/Non-Kahler/output/pdf/hermitian-pluripotential-theory.pdf" purpose="output"}; no duplicatePDFmarkdown.

## Next actions

1. Read complete58/59 reports when written; ifcorrect include58afterpartialenvelopes,59afterintrinsicflagcount. Updatechapter21opening/ending toflagavailableonauxmod andchapter27replaceconditionalcompactflagparagraph bygeneralnonMoi corollary. These strengthenings dependon59.
2. Rebuild, resolve every warning, detailednew/reflowvisualreview, fullcontactreview andfreezecheckpoint11 (mayexclude60/61untilpassed).
3. Finish conditionalgradientdraft61 while60 audits, then reconstructSTWspecialC2estimate iffeasible. Do not markSTWexistence selfcontained until allstepsproved.
4. Revisit generalNPP/PVP movingfiniteness, exacttrace/singularitytopology, lowerBergmanasymptotics, andclearfinalresearchprogram. AllSGPTrows remaininscope.
5. Keep source/version/proof ledgerscurrent; no noveltyclaim. Continue autonomously untildeadline, then reporthonestachievements/gaps; do not markgoalcompletebecausebuildpassed or timeexpired.

## Runtime and conventions

ddc=i/(2pi)partialbarpartial; multiplierweight exp(-u),nu(log|z|²)=1;u preceqv meansMOREsingular. TW/STW u_ours=2pi phi_ref;KN/Nguyenours=2ref;BGLpublisherours=4piref;XZformsdivided2pi,potentialsunchanged. Recentexactprimaryversions are archived inmanifest/literature.
Existing hourlyheartbeat hermitian-pluripotential-book onthread01a09f6c-4163-7531-acef-65c72b0cce54 ACTIVE untildeadline, quietexceptmeaningfulchange. Do notduplicate. Atdeadlinepause/report; goalstatusonlycompleteifactualobjectiveachieved.
Rethlas runtime /Users/mingchen/math-agents/Rethlas/agents/verification/.venv/bin/python; copiedworkspace research/rethlas/verification; originalAGENTS readfull. Modelanalytics/sourcewebtimeouts occur; ordinarytoolmemoryapprovaltimeouts earlierrecovered. No outstandingunsafeaction or approvalrejection.
RichPython /Users/mingchen/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3; TeX2021+Poppler installed. Workspacewritable; originalsourcesreadonly.

22:27UTC: section_stw_gradient.tex nowdrafted NOT INCLUDED; audit61 NOT YET PREPARED/LAUNCHED. ConditionalcomplexHessianbound=>gradient viarescale; exactcofactorP_n+linearZ,1/(2pi) convention, determinantA^-2n; standardLaplaceW2p=>C1compactness and coneLiouville60. Needcheckfullmatrixidentification andframechangeerror, conditionalhypothesisexplicit. Buildpostformatting running exec54228.

22:26UTC: partial_kernel_upper_01 PASSED and fullreportread, dependency57resolved. Includedin27 afterpartialenvelopes. Buildpostformat320pages tmp/build-partial-kernels-02.log nowclean (noover/under/undefinedwarnings). New58requiresbuildandreflow. Conditionalgradient61 inputrunnerpreparednow.

22:27UTC: stw_gradient_reduction_01 launched exec2859, draft61NOTINCLUDED. InputacceptsconeLiouville60conditionally pendingitsfullaudit. Originalfuture22:27drafttimestampapproximate; actuallaunch22:27. No otheractivejobsbesidesRethlas59/60/61.

22:32UTC: auxiliary_blowup_flag_01 PASSED, fullreportread; includedin21afterintrinsiccountbeforeHopf, chapter21opening/endingupdated and27nonMoi examplegeneralizedwithprecisecorollaryref. No originalXflaghypothesisnow. 58alsoincluded, buildingnewPDF now. STW60/61stillNOTINCLUDED. C2reconstructionplan savednext-stw-second-order.md, fullSTW§3textread andpp26–27torsionformulasvisuallychecked. NoC2theoremwritten.

## 23:04 UTC — current state supersedes old pending notes

Current PDF334pages,27chapters includes58/59/60/61. Clean finalpass tmp/build-checkpoint-11-final.log; one last ONLYtypographic edit nowbuilding tmp/build-checkpoint-11-final2.log: Hopfequilibriumapplication gets ownsection toavoid3lineclosingpage. STWmainstatement andnormalizationderivativetheorem groupedusingNeedspace; resultingchapter9still29pages. Full334contactreviewcompletedin tmp/pdfs/checkpoint-11-final/all boards01–28. Detailednew58physical315–319old326build andnew59physical250–252old326build; updated59physical258–260new334buildreviewed. Detailed60/61physical99–106reviewed, thenallfinalreflow93–107reviewed in tmp/pdfs/checkpoint-11-reflow. Ch27last329–332reviewed; finalHopfsectionreflowstillneedsnewview beforefreeze11. Allotherreflow/new48–57 detailedreviewinpreviousstatus retained. Checkpoint11 NOTYETWRITTEN, dofreezeafterlastPDFcheckwithoutmoremathchanges. Source62/63/64notincluded.

60 stw_cone_liouville_01 PASSED/fullreportread. Included afteradjoint. SelfcontainedboundedLipschitzP_nmaximalLiouville withsmoothcomparison/translatedenergy/dimensioninduction/weightedannulusconvolution.
61 stw_gradient_reduction_01 PASSED/fullreportread;60dependencyresolved. Included after60; conditionalC2boundexplicit. Addedcompatibleg_j^-1/2unitaryframeexplanationfromfullreportforpreciseexactdetidentity. STWexistencestillexternal.
62 stw_matrix_structure_01 PASSED/fullJSONandfullreport.mdread. NOTINCLUDED. Newsection_stw_structure.tex: exactdelta^{paj}_{bci}alternatingcontractor/[2(n-1)]derivestorsion6terms,Hodgeindextransposechecked;missinggradientcoefficientsandcovariantderivativeexclusions; P^-1chi/W;logdetweights/coercivity andcomplexconcavitysquare. Indepverifierrealbasisexteriorchecks n2..6 allpassed, generaldimproofalsoverified. exec40748maystillrunnerfinishing; reportcomplete.
63 stw_second_order_reconstruction_01 ACTIVE exec74991, section_stw_second_order.tex NOTINCLUDED; inputrunlogs stw-second-order-reconstruction. FullspecialSTW C2draft ~280lines. Accepts62asconditionalprecursor;62nowpassed. CoreeigenvalueBchosenlocalunitaryframeChernparallelatpoint so∇B0,topgapfixed; weightedthirdderivativeZcancel; exactconjugatedGamma; simplifiedYoungcancellation usingFU²<=CE;eps,D2,D1,deltaordering;2casesandglobalpropagation. Lastlogalltorsioncancellationandnumericalbudgetpassed, noreportyet. Networktimeoutat22:50recoveredautomatically. Correctedliteralmissingbackslash 'Ccal+sum_kf_k' to 'Ccal+\sum_k f_k' afterauditoridentifiedcosmetic; plusspacingall\sum_k f_k. Immutableinputunchanged; documentthisformatonlydifference.
64 stw_continuity_reconstruction_01 ACTIVE exec15739, section_stw_continuity.tex NOTINCLUDED. BoundedQ=>fixedLaplaceW2p=>C1alpha freezeZ(Dv), globalrealconcaveuniformellipticextensioninfBoxtangentslogdet withP_n∘complexHess, standardEvansKrylov/Schauder; meanzerocontinuitypathF0loggamma0n/gamman, driftFredholm+scalarb,closedness,uniqueness. Conditional63input; maynotmarkfullSTWselfcontaineduntil63/64bothpassed. Addedlabelsec:gauduchon-volume-adjointtoexistingsection.

Next: freezecheckpoint11 containingthrough61, excluding62+. Readfull63/64reports,fixanyadversefinding, theninclude62+63+64 onlyifcorrect. ReorderSTWsectionslogically(C0,adjoint,structure,secondorder,Liouville,gradient,continuity), removeall'externallyimportedSTW'languageconsistentlyafteractualdependenciesdischarged. Gradientpropositioncanremainconditionallyformulatedgenerallemma, butitsclosingparagraphshouldexplainC2hypothesissuppliedby63forboundedC2F. DoNOTremoveexplicitlyexternalgeneralNPP/PVPinputs. Needcontinuetaskbeforedeadline06:19:41UTC,~7h15remaining.

23:07UTC: CHECKPOINT11 FROZEN,334pages. Fullmetadata in audits/build-snapshot-11.json. All finalreflow93–107 andHopf330–331reviewed; no pendinglayoutrepairs inthissnapshot. Source62passedbutexcluded;63/64active. Do not repeat freeze.
