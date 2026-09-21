# Proof boundary and remaining obligations

This is a working ledger, not an assertion that the book is complete. User priority: self-contained apart from standard references and SGPT, with no BMP in the main theory.

## Accepted standard foundations

The manuscript states the local facts it uses: canonical psh distributions, local smooth correction, bounded Bedford--Taylor products, capacity/quasi-continuity, local Skoda integrability, local valuative multiplier-ideal criterion, strong openness, Choquet's lemma, and basic current calculus. The functional-analysis boundary is Hahn--Banach, scalar elliptic Fredholm theory/regularity/maximum principle and the implicit function theorem. SGPT supplies the local singularity conventions and standard results. These inputs must retain precise formulations; calling a fact standard does not justify an incorrect extension to a non-closed background.

## Hermitian arguments now written out

| Argument | Current proof boundary |
|---|---|
| Smooth torsion and mass formulas; raw energy obstruction | Algebra, Stokes and local test functions; independently audited |
| Gauduchon conformal theorem | Standard elliptic theory; proof supplied and independently audited |
| Generalized Lamari criterion and positivity threshold | Hahn--Banach and explicit scalar elliptic inverse; proof supplied and independently audited |
| Bounded non-closed products and restricted positivity | Local BT and constant-form freezing; arbitrary-background extension independently audited in general_background_01 |
| Extended positive measures for arbitrary smooth backgrounds | Compatible restricted products; infinite mass is allowed; general_background_01 passed |
| Finite damping and continuity | Local BT plus cutoff estimates; coarse version independently audited |
| Sharper range growth from Gauduchon trace | Exact top-wedge cancellation; gauduchon_growth_01 passed |
| Raw-tail/integrability criterion and exponential PDE closedness | Standard bounded capacity continuity and finite-measure calculus; general_background_01 passed |
| I-envelope projection and its model consequence | Precisely stated local valuative/strong-openness inputs from SGPT; proof supplied |
| Relative envelope/full-volume equivalence | Conditional on contact and volume facts in their stated BMP regime; reconstructed proof independently audited |
| Smooth normalization derivatives and weak zero-exponent barriers | Explicit calculations supplied; scope of separate inputs is stated |

## Important remaining Hermitian proof obligations

1. Global normalized L1 compactness: DISCHARGED from local psh compactness, connected-cover propagation and a moving-center submean argument. The full chapter passed compactness_regularization_01.
2. Bounded exact-background smooth regularization: DISCHARGED from bounded local convolution comparisons, compatible smooth maxima, a decreasing diagonal and a signed rescaling argument. BK07 provides attribution, not an imported global theorem. The full chapter passed compactness_regularization_01.
3. Semipositive contact support: DISCHARGED. local_contacts_01 passed arbitrary-background ordered contact, continuous Hermitian envelopes and unbounded reduction; penalized_contacts_01 passed proper existence/penalization, continuous/lsc/quasi-continuous obstacles and semipositive limits. Genuine envelopes may have infinite mass. The separate non-semipositive big/BMP theorem remains imported.
4. Bounded and smaller-background singular domination: DISCHARGED. bounded_comparison_01 passed Hermitian modified comparison and bounded domination. singular_domination_01 passed ANY big-background individual noncollapse, semipositive bounded domination, zero-set lemma and singular strict domination with smaller-background envelope. Infinite-measure cancellation is localized. General E_env domination/class closure under PVP remains to reconstruct.
5. Smooth Hermitian MA: DISCHARGED relative to standard elliptic regularity. smooth_czero_01, smooth_second_estimate_01 and penalized_contacts_01 passed the C0, trace/completed-square estimate, real concave Evans–Krylov reduction, continuity and proper exponential solvability. STW is separate below.
6. Continuous weak existence (KN/Nguyen): DISCHARGED. weak_lp_existence_01 passed the local-to-global capacity proof, backwards iteration, lower density Lp norm, C0, L1-to-uniform compactness, Gauduchon normalization and both existence arguments. Only two explicitly stated standard LOCAL BT estimates remain inputs. No BMP/PVP.
7. Prescribed singularities (ALS/Li): bounded semipositive big Lp existence, relativeuniformestimate andsupersolution passed big_lp_equations_01/relative_lp_barriers_01. Common-barrier compactness main proof passed with one standalone monotone overstatement; corrected and fully resolved by common_barrier_repair_01. bounded_subsolution_01 andweighted_measure_addition_01 passed andtheircommonbarrierprerequisites are now available. Fullprescribedtypeexistence written; prescribed_lp_existence_01 passed. GeneralNPP/PVP classclosure/existence andLi broaderbig regime remain imported.
8. Prescribed Gauduchon volume (STW): explain the scalar ansatz, first-derivative torsion term and Aeppli constraint, with the nonlinear estimate identified separately.
9. XZ26 Hopf-threefold/heat-kernel counterexample: full reconstruction WRITTEN, including normalization, vertical-energy mass identity, positivity matrix, Fourier estimates, scale variation, integrated defect and smooth correction. hopf_counterexample_01 PASSED, including every heat estimate and correction step; the bounded lower-mass corollary accepts regularization/BT, with regularization separately proved. The chosen metric is Gauduchon with v_minus=6 and v_plus=infinity in our normalization.
10. Later SGPT transfer chapters: analytic approximation, singularity topology, traces, rays/test curves, toric/non-Archimedean data, b-divisors, Okounkov bodies and partial Bergman kernels. Maintain the complete comparison matrix and clearly separate constructions requiring closed or integral backgrounds.

## Explanatory example now supplied

The P1 pole/truncation example is written as ex:p1-raw-tail in the damping chapter. Bounded truncations have mass1 supported where u_j=-j, approach a pole in the weak limit, and violate uniform raw tails despite capacity convergence. Their damped measures tend to zero. This distinguishes BMP from the sequence tail condition even in the Kähler case.

## Newly located literature still to audit

- ALS26 is now listed by the authors/publisher as JFA291(9), article111608 (issue date November2026), DOI10.1016/j.jfa.2026.111608. Current numbered statements deliberately follow the saved arXiv2511.02339v1. Compare the published text before changing theorem numbers.
- The January2024 arXiv2401.03440v2 is a single-author Salouf preprint; the later published ALS24 paper is by Alehyane--Lu--Salouf, JGA34,320, DOI10.1007/s12220-024-01772-w. Do not silently identify their authors/version-specific numbering. Its unbounded contact proof reduces to the bounded GL22 theorem.
- Sun--Wang arXiv2506.07336 and Li--Lin--Zhou arXiv2311.14958 should be audited for bounded-potential/non-closed versus closed background regimes before enlarging the PDE survey. Search abstracts are not sufficient evidence of exact hypotheses.

## New chapters,16:59UTC

Normalization functional: fullproofs oforder/concavity/boundedL1continuity,supportingprobabilitiesandabsolutecontinuity,stability/derivatives/smoothGaudidentificationwritten. normalization_functional_01 passed. No weak uniqueness/currentadjoint claimed.

Perron interpolation: localnonclosedKiselmanfreezing,product/endpoint/gluingproofs,ordinarytypeendpointsegmentsandLipschitz,SchurHCMAformula,rawL2actiontorsionandGaudtranslationcharacterizationwritten. hermitian_perron_rays_01 passed. Pure envelopeLegendretestcurve/raydualitynext; noDarvasmetricorunrestrictedEenvidentificationclaimed.

## Further development,17:26UTC

Pure envelope Legendre correspondence written with explicit connectedness, P-fixed initial potential and exact ray definitions. Historical standalone audit omitted the book's standing connectedness; all other deductions passed under that hypothesis. Explicit chapter repetition under focused check envelope_testcurves_connected_01.

Dual normalization supplement is written, normalization_dual_01 active. It defines a probability-measure variational problem, uniformly integrable dual sublevels, and extends supporting probabilities to bounded measurable logarithmic densities. No raw MA energy primitive, weak-adjoint uniqueness or strong density convergence is claimed.

Next: standard Demailly regularization must be read in its exact almost-positive closed-current form with arbitrary continuous lower bound; apply to ddcu, rather than pretending theta+ddcu is closed. Analytic approximation and a possible intrinsic trace through restricted multiplier ideals are under development, not yet book theorems.

## 18:20 UTC: approximation and trace boundary updated

Demailly's analytic approximation is a precisely stated STANDARD reference input, verified against the actual2011 construction including exact ideal type. Local estimates and normalization are proved. Gauduchon uniform Lelong/divisorial bounds are proved. analytic_approximation_01 passed. Intrinsic restricted-ideal trace data, curve Green realization, its MA equation and source metric comparison are proved and passed intrinsic_trace_data_01/curve_trace_metric_01; their conditional upstream dependency is now discharged. Higher-dimensional exact realization remains open in this manuscript.

The normalization dual supplement passed normalization_dual_01. The testcurve connectedness recheck passed envelope_testcurves_connected_01. Those earlier pending notes are superseded.

A new relative finite-measure chapter is drafted separately (not yet included in current208-page PDF). relative_class_domination_01 checks finite roofs, class lower bounds and strict domination when MA(u) is finite. dominated_relative_compactness_01 checks a common relative lower envelope AFTER EXTRACTION and fixed-measure dominated capacity/weak continuity. Both active. The proof keeps disjoint contact pieces, avoids a spurious number-of-obstacles factor for a fixed dominating measure, and restores a finite prefix by a2b averaging argument. The moving bounded-reference measure case and full arbitrary NPP existence are not yet reconstructed.

## 18:59 UTC update

Checkpoint09 (222pages) contains passed relative finite domination and fixed-nucompactness, exact numerical trace addition reconstructed from Cao, and the higherdimtrace-inequality model envelope with positivefinite mass and prescribedordinarytypeLp equations. Exacthigherdimorders/backgroundcompatibility remainunknown. New explicitmovingexpo commonroof barrier and weightedsections/Gauddegree chapter are separately drafted and independently auditing; not yet included. Generalmovingcapacityproof stillneedsfinite mass of the lower-rooftop limit; no Kähler finiteness assertion is silently transferred.


## 19:38 UTC update (supersedes previous pending notes)

Explicit exponential common roof, weighted-section/Bergman/Gauduchon degree chapter, restricted-section trace obstruction and exact Hopf kernel all passed and are included. General compact-flag valuation bounds, full-lattice count, Moishezon/BMP implication and explicit Hopf simplex also passed and are being built as chapter21. Intrinsic-lattice/period count and field interpretation are separately auditing, as is the Hopf projective-base reduction with reduced Hermitian equations and smooth toric gradient. None assumes BMP. The general moving-reference capacity/finiteness gap, unrestricted singularity metric, exact higher-dimensional trace realization and STW estimates remain.


## 20:17 UTC update

Intrinsic flag count (exact lattice, degree period, section-ratio transcendence degree) passed and is included. Hopf reduction passed after correcting the continuity citation to the book's proved KN theorem; SGPT is used only for full-mass uniqueness. Divisorial-current summability, strong divisorial convergence on fixed models, compatible pushforwards and one original-background trace majorant passed. Bott–Chern bclasses of positive closed currents and analytic-singularity nef Cartier realizations passed; no global ddbar lemma is imposed. These are chapter23. A separate chapter on fixed-derivative affine classes for nonclosed backgrounds is drafted and auditing; its approximation explicitly allows the smooth derivative to vary, and no nonlinear volume identification is claimed. The general moving-reference capacity/finiteness gap and STW estimates remain obligations.


##20:44 UTC update

Checkpoint10 contains24 chapters including the passed nonclosed fixed-derivative bclass chapter. Gauduchon-volume adjoint supplement passed and is now included in a new build: exact drift adjoint, positive probability and strict normalization concavity conditional on explicit STW existence. The STW estimates remain external. Constant-left Hermitian I-envelope systems are drafted and under audit; retraction and realization criterion only, no surjectivity or volume theorem.

21:20UTC: Envelope-boundary counterexample50 and Gauduchon variational volume51 both passed bounded independent checks; full reports read. Included chapter25 example proves failure of recovery at zero residual volume even in a positive closed Kähler background. Chapter26 gives exact finite density-dependent Gauduchon infimum = smooth MA normalization root, with nef extension, equality and first variation. All dependencies resolved. Extrema supplement52 and STW C0 reconstruction53 pending. Neither general NPP/PVP reconstruction nor full STW estimates are claimed solved.

21:33UTC: STW C0 a priori reconstruction passed stw_czero_01 and is included. It uses standard linear nonsymmetric drift Green kernel estimates and an explicit supporting-slope area formula; no nonlinear ABP or STW existence theorem imported. Gradient and second-order estimates remain the outstanding STW nonlinear inputs. Gauduchon mass-extrema formula passed52. Curvature classification54 and nefdegenerationorders55 are drafted and being checked, not included.

22:07UTC: Curvature classification54 and nefdegeneration55 passed and included in chapter26. General partial-kernel finiteGramcalculus, exactquotientlift and SGPTbaseequilibrium56 passed, as did arbitrary-background partialIweightedcompactenvelope57. Chapter27 included and building. General partialFubiniStudy upperbound58 is drafted/auditing, notincluded; lowerasymptotic/generalmeasurelimit remain separate. All claims retain closed linebundle curvature versus nonclosed Hermitian MA distinction. STW C0 now reconstructed; gradient/C2 and generalNPP/PVPmovingfiniteness remain uncompleted obligations.

23:07UTC: Checkpoint11 includes general partialFubiniStudy upperbound58 and auxiliaryblowupflag59; no flaghypothesis on originalX is needed for sectioncount/nonMoishezonvanishing. Includes reconstructed coneLiouville60 and conditionalSTWgradient61. Exacttorsion/coercivity62 passed but is excluded pending fullsecondorder63/continuity64 checks. FullSTW still explicitexternal incheckpoint11. No generalNPP/PVPmovingfiniteness, exacthigherdimtrace, arbitrarylowerBergmanasymptotic or singularitymetric claim has been added.

23:20UTC: Full smooth STW Gauduchon-volume proof reconstructed and included: exactmatrixstructure62, specialC2estimate63, andregularity/continuity64 allpassed, withallconditionaldependenciesresolved. C0/adjoint48,53 andconeLiouville/gradient60,61 precededthem. Standardlinear/concaveellipticregularity is the only PDE referenceinput. GeneralNPP/PVPmovingfiniteness remains anuncompletedreconstruction, not a claim that the publishedtheorem is open. NewfixedbackgroundidealL1metric/curvecompletion65 drafted andauditing.


## 2026-09-15 00:55UTC: current manuscript through72

All65–72 passed and included;72completed reports total,69correct and3historicaladverse reportsallresolved; all fullreportsread. Fixed-background idealL1metric and complete curve counterexample65; exactfinite-divisorGaudvolume andthreshold66; negative-square Hessian/classderivative recovery67; compactunibranch resolution foundations68; finite-cone radialmetric product andpositivevolumeblowupboundary69; finiteGaudtracehomeomorphism/completepotentialmetric70; quantitativeonesidedboundedstability71; exactGauddenominatorcollapsecriterion72. New final researchprogram separates publishedbutunreconstructed NPP/PVP existence from two workingconjectures and higherdimtrace, topology, residualsystem, kernel andsingularspacequestions.

Remaining recent theorem inputs: BGLbig-backgroundcontact support underitsstatedregime; ALSgeneralNPP/PVP existence(noBMP); XLarbitrarybiggeneralNPP existence(BMPandPVP). Fixed-nudominatedcontinuity nowfullyproved anditsoutdatedexternal labelremoved. No general moving-reference lowerroofmassfiniteness claim. StandardlocalBT/envelopes/regularization and SGPTcharacterizations remainallowed standardinputs.

New73Holderregularity and74compactGaudcurrentdual problem are draftedandunderboundedRethlasreview, NOTINCLUDED. Current386pagebuild includes28chapters+unibranchappendix; needscleverefproblemformatfix(repairedsource), reflowcheckandcheckpoint12freeze.

## 2026-09-15 01:38 UTC: incorporated audits73–76

All four full reports read; each verdict correct relative to its explicit accepted prerequisites. Total76 completed reports:73correct and3historicaladverse, all earlier adverse findings resolved in retained repair reports. The new claims remain mathematical claims for review, not formal verification or novelty certification.

73 holder_regularization_01: bounded strictly Hermitian solution, nonnegativeLp density,p>1, has every Holder exponent beta<2(p-1)/(np+3(p-1)). Inputs only71stability and classicalDemailly94/KN19regularization. The adjoint averaging cancellation,L1O(t²),kernelgradientO(1/t),scalarpositivityrepair,minimizing-radiusbound and elementary modulus are proved. Formal-exph interpretation explicit; capped transform onlyqpsh. No density lowerbound/BMP/priorcontinuity.

74 weak_gauduchon_duality_01: compact trace-normalized positive ddc-closed current set; intrinsic determinant-density measure and continuous-test dualinf; maxD_F=e^(-B0(F)/n); smoothFuniqueoptimizeramongALLcurrents; continuousFmaxformula; nearmaximizer weighted-measure continuity/affineness; exact representation of every A0(F) member. No wedge of currents, generalcurrentssmoothing, unweightedcurrentabsolutecontinuity, allcontinuousuniqueness orweaklinearization.

75 gauduchon_determinant_integrability_01: every normalizedGaudcurrent has determinant measure k_TdV with uniformLq,1<q<n/(n-1), noBMP/PVP. Endpoint supremum (alreadyoversmoothforms)=v_minus(omega)^(-1/n),∞ifvminus0. Proof uses ordinary smoothMA, earlierLp-densitylowerestimate, and mass-extremaformula52. AdjointdensitieshaveuniformsubcriticalLqonboundedFsets; endpointunderPVP. Hopf3attains6^(-1/3)whilevplus∞. This is not a boundonunweightedcoefficients or arbitraryMAmass.

76 generic_adjoints_01: everyfixedchapter14regime has exactdenseGdelta singleton locus ofA_phi(F) inuniformC(X). Widthuscfromclosedgraph, directionalzero-widthdensityfromcountablenondifferentiabilityonlines, thenBaire. Allapproximatingsupportprobabilitiesconvergeatthesepoints. Gateaux,notFrechet; nouniquenessclaimedateveryF.

GeneralNPP/PVPmoving-reference lowerroofmassfiniteness remains unresolved in this manuscript; publishedexistenceisnot labeleda conjecture. Local-big-continuity77nowauditingusesgeneralDemaillyerrorMODULUSratherthanunprovedlinearrate. It is NOT included and supplies no input to the current book until reviewed.


2026-09-15 02:05UTC: audit77 passed and full report read. Bounded semipositive-big Lp solutions are locally continuous wherever a fixed strict barrier is locally bounded, noBMP/PVP; general Demailly curvature modulus retained. Included after73, awaiting build. Audits78(local homogeneous Dirichlet) and79(continuous-obstacle general-big contact) are pending and not included. Full general unbounded-obstacle contact and moving-reference generalNPP reconstruction remain incomplete.


Audits78–79 bothpassed andfullreportsread: arbitrarynonclosedlocal homogeneous replacement forcontinuousdata viaGL10, thencontinuousobstacleenvelope continuity/contact in arbitrarybigbackground noBMP. Globalunbounded/quasicontinuouscontact NOTsettled. Audit81newuserNUMA counterexample active; do not conflate zerodensitypotentialuniqueness with scalar/exponentialuniqueness or continuousfiniteFadjoints.


2026-09-15 03:24UTC: audits80smooth-current-flow,81NUMAconstruction,83symmetryselection allpassed and full persisted records/reports read. 82geometryinitial wrong only for almostanalytic vsanalytic definition; geometry_problem_connections_repair_01 passed, fullreportread, exactdefinitionfixed and section INCLUDED. DangTheorem4.3 conditional smoothflowconvergence underbigness nowexplicitlyknown/cited afterrootfullstatementread, notleftasopenconditionalstep. 84big_general_contact_01 PASSED all82deductions/ninereferences; FULL562linereportandfinalJSONread. Generalbigcontact forfiniteaeqcunboundedobstacles reconstructedwithoutBMP/PVP usingglobalpolecompetitorrepair plusfixed-levelSIGNEDcapacitylimits. INCLUDED and chapter11external label/BMPassumptionremoved; researchprogram distinguishesstillunresolvedmovingroofmassgap. 85radialC1,1NUMAfamily and86canonicalselectedlimit areACTIVE, NOTINCLUDED.

2026-09-15 04:20 UTC: Minimal-reference general NPP measure equations now reconstructed under PVP, no BMP (general_measure_minimal_01 passed). Local Ceg98 decomposition -> global bounded theta-carrier -> bounded-density truncations -> fixed-measure continuity. Earlier general-measure gap notes now apply to arbitrary prescribed reference, not phi=0.
