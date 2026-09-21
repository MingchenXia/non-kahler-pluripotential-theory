# Source-to-Hermitian comparison

Working audit, 14 September 2026. A row marked pending is a research obligation, not an asserted impossibility. Original source labels are retained below to make the comparison traceable.

| Original chapter | Hermitian counterpart and transfer issue | Required verification / disposition |
|---|---|---|
| Plurisubharmonic functions | Local psh, Lelong numbers and multiplier ideals do not require a global Kähler metric. Arbitrary qpsh functions are bounded below in curvature by a multiple of a Hermitian metric. Non-closed forms have no local dd^c potentials. | Develop local tools and precise normalization. Do not import global positivity-preserving approximation in a fixed background without curvature-loss estimates. |
| Non-pluripolar products | Bounded local products survive with a smooth non-closed background by local expansion. For unbounded potentials, local finiteness and uniform total mass require separate checks. A non-closed positive current is not a closed positive current. | Audit BGL25 construction and bounded-mass hypothesis. Separate closed-current products and Hermitian background products. |
| Envelope operators | Obstacle envelopes can be formed using theta-psh functions. Existence, contact-set support, modelization, mass invariance and equality characterizations are different statements. | Define with explicit nonempty competitor assumption. Audit ALS26/P26, including background hypotheses and singularity order. |
| Geodesic rays in the space of potentials | Subgeodesic positivity on a product can be written down, but raw Monge-Ampere energy need not possess a primitive. Darvas geometry and energy identities require new arguments. | Prove a smooth obstruction first. Study which envelope/Legendre constructions survive independently of metric geometry. |
| Toric theory on ample line bundles | Curvature of a holomorphic line bundle is closed. Smooth projective toric varieties already admit Kähler forms. A torus-invariant non-closed Hermitian metric is a different analytic structure. | Retain toric theory as a comparison/test case; identify exactly which new Hermitian parameter is being varied. |
| Comparison of singularities | The order u <= v+C and multiplier ideals are intrinsic. SGPT's background-independent P-preorder uses a mass-preserving envelope and polynomial mass identities. Its d_S uses geodesic distance. | Do not silently substitute a fixed-background relation for the original global relation. Audit background independence and the distinction between a metric and a distance-like function. |
| I-good singularities | SGPT `thm:charIgoodasclosure` equates analytic-approximation closure, a mass-volume identity, and equality of P/I envelopes. Raw mass is not even invariant under bounded perturbation in general. | Central research task: identify a viable Hermitian replacement using singularity envelopes and upper/lower volumes; prove implications separately and test converse statements. |
| Trace operator | Generic Lelong numbers and resolution data remain local/bimeromorphic objects; restriction of arbitrary qpsh functions may be identically minus infinity. Trace via I-models depends on the preceding equivalences. | Audit original construction; distinguish ordinary restriction, valuative restriction and an envelope-defined trace. |
| Test curves | Concavity and Legendre duality may be formal; maximality, mass and energy require global input. | Develop a hypothesis ledger for each duality result. |
| Okounkov bodies | Graded linear series of holomorphic line bundles can be considered on compact complex manifolds, but non-closed backgrounds are not Chern classes. Positive algebraic volume may force special geometry. | State geometric domain precisely and audit links to Hermitian analytic masses. |
| b-divisors | Analytic modifications and divisorial valuations exist beyond the projective case; intersection volumes and nef approximation require additional structures. | Separate local divisor data from algebraic positivity and intersection identities. |
| Toric theory on big line bundles | Remains a projective/closed-curvature comparison theory, not automatically an extension to arbitrary Hermitian backgrounds. | Explain the obstruction explicitly and preserve useful convex examples. |
| Non-Archimedean theory | The source already defines analytic I-model test-curve inverse systems on compact Kähler manifolds; only its final Berkovich comparison is projective. Closed positive perturbations, mass continuity and positive-volume recovery enter its analytic construction. | Transfer the envelope-system formalism with exact transition maps; separate volume, recovery from the limiting background, and algebraic analytification. A bounded-left prototype is under development without BMP. |
| Partial Bergman kernels | Holomorphic sections and weighted Hilbert norms remain meaningful. Leading asymptotics, volume and curvature positivity have distinct hypotheses; Chern curvature is closed. | Audit estimates and positivity assumptions, then compare with I-goodness in the closed regime. |
| Historical/bibliographical notes | Rapid changes in 2025-26 affect the status of conjectures. | Version all primary sources; flag old open questions resolved by XZ26. |
| Convex appendix | Local real-variable statements are independent of Kähler geometry. | Reuse only necessary tools with verified normalizations. |
| Unibranch spaces appendix | Extension to singular spaces needs a separate theory of Hermitian forms, local embeddings and modifications. | Keep in scope as a clearly delimited extension after the smooth compact case; do not claim automatic transfer. |
| Almost semigroups appendix | Combinatorial tools survive; applicability to geometric volumes requires a relevant graded series. | Retain only when needed and explicitly identify the series. |

## First direct obstruction chain

1. For smooth potentials, total mass has torsion-dependent first and higher variations.
2. Smooth bounded potentials all have the same ordinary singularity type and trivial multiplier ideals.
3. Therefore raw total mass does not define an invariant of ordinary singularity type for a general Hermitian background.
4. An unmodified global comparison principle for every pair of smooth potentials would force total mass to be constant (shift one potential by a large constant and then exchange the pair).
5. The Kähler primitive of the raw Monge-Ampere operator requires symmetry of its linearization. Nonconstant total mass already obstructs this symmetry in the constant direction.

The manuscript will prove these claims without relying on the deep Hermitian literature.

## Progress through18:20UTC

Perron interpolation, exact envelope Legendre correspondence and a computedP1 example are now supplied and audited, independently of a Hermitian metric on singularity types. Analytic approximation is available through the exact classical Demailly input, with its curvature loss and ideal type; Gauduchon linear trace bounds all restricted divisorial orders. Intrinsic trace data is constructed from restricted ideals in every dimension, and the curve case now has a canonical ordinary-type realization, a complete equation theorem and quantitative convergence in SGPT's curve metric. These chapters passed their bounded audits. Higher-dimensional realization, a general Hermitian singularity topology and the remaining geometric rows are still research obligations.

## 18:59 UTC update

Checkpoint09 (222pages) contains passed relative finite domination and fixed-nucompactness, exact numerical trace addition reconstructed from Cao, and the higherdimtrace-inequality model envelope with positivefinite mass and prescribedordinarytypeLp equations. Exacthigherdimorders/backgroundcompatibility remainunknown. New explicitmovingexpo commonroof barrier and weightedsections/Gauddegree chapter are separately drafted and independently auditing; not yet included. Generalmovingcapacityproof stillneedsfinite mass of the lower-rooftop limit; no Kähler finiteness assertion is silently transferred.


## 19:38 UTC update (supersedes previous pending notes)

Explicit exponential common roof, weighted-section/Bergman/Gauduchon degree chapter, restricted-section trace obstruction and exact Hopf kernel all passed and are included. General compact-flag valuation bounds, full-lattice count, Moishezon/BMP implication and explicit Hopf simplex also passed and are being built as chapter21. Intrinsic-lattice/period count and field interpretation are separately auditing, as is the Hopf projective-base reduction with reduced Hermitian equations and smooth toric gradient. None assumes BMP. The general moving-reference capacity/finiteness gap, unrestricted singularity metric, exact higher-dimensional trace realization and STW estimates remain.


## 20:17 UTC update

Intrinsic flag count (exact lattice, degree period, section-ratio transcendence degree) passed and is included. Hopf reduction passed after correcting the continuity citation to the book's proved KN theorem; SGPT is used only for full-mass uniqueness. Divisorial-current summability, strong divisorial convergence on fixed models, compatible pushforwards and one original-background trace majorant passed. Bott–Chern bclasses of positive closed currents and analytic-singularity nef Cartier realizations passed; no global ddbar lemma is imposed. These are chapter23. A separate chapter on fixed-derivative affine classes for nonclosed backgrounds is drafted and auditing; its approximation explicitly allows the smooth derivative to vary, and no nonlinear volume identification is claimed. The general moving-reference capacity/finiteness gap and STW estimates remain obligations.

20:27 source correction: chapter_NApotential.tex explicitly begins with compact Kähler analytic test-curve systems, not just algebraic varieties. The matrix now records this exact scope. research/next-envelope-systems.md plans a mass-free Hermitian prototype with a fixed finite cutoff interval, compatible Q projections under all positive Hermitian perturbations, a canonical base-limit retraction, and an explicit criterion for recovering the whole system. No surjectivity or NA volume theorem is assumed.


##20:44 UTC update

Checkpoint10 contains24 chapters including the passed nonclosed fixed-derivative bclass chapter. Gauduchon-volume adjoint supplement passed and is now included in a new build: exact drift adjoint, positive probability and strict normalization concavity conditional on explicit STW existence. The STW estimates remain external. Constant-left Hermitian I-envelope systems are drafted and under audit; retraction and realization criterion only, no surjectivity or volume theorem.

21:20UTC: Analytic NA prototype now has a proved boundary obstruction: a nef ruled-surface divisor creates extra divisorial singularities in the perturbation limit. SGPT full inverse systems also allow zero volume; its positive-volume recovery theorem is not contradicted. Finite Gauduchon variational volume is proved on arbitrary smooth pseudoeffective dd^c backgrounds, agrees with smooth equation normalization on the positive cone and with closed nef Kähler intersection volume, and explicitly retains a smooth probability measure. Birational degenerate-density compatibility and b-class volumes remain questions.

22:07UTC: Curvature classification54 and nefdegeneration55 passed and included in chapter26. General partial-kernel finiteGramcalculus, exactquotientlift and SGPTbaseequilibrium56 passed, as did arbitrary-background partialIweightedcompactenvelope57. Chapter27 included and building. General partialFubiniStudy upperbound58 is drafted/auditing, notincluded; lowerasymptotic/generalmeasurelimit remain separate. All claims retain closed linebundle curvature versus nonclosed Hermitian MA distinction. STW C0 now reconstructed; gradient/C2 and generalNPP/PVPmovingfiniteness remain uncompleted obligations.

23:07UTC: Checkpoint11 includes general partialFubiniStudy upperbound58 and auxiliaryblowupflag59; no flaghypothesis on originalX is needed for sectioncount/nonMoishezonvanishing. Includes reconstructed coneLiouville60 and conditionalSTWgradient61. Exacttorsion/coercivity62 passed but is excluded pending fullsecondorder63/continuity64 checks. FullSTW still explicitexternal incheckpoint11. No generalNPP/PVPmovingfiniteness, exacthigherdimtrace, arbitrarylowerBergmanasymptotic or singularitymetric claim has been added.

23:20UTC: Full smooth STW Gauduchon-volume proof reconstructed and included: exactmatrixstructure62, specialC2estimate63, andregularity/continuity64 allpassed, withallconditionaldependenciesresolved. C0/adjoint48,53 andconeLiouville/gradient60,61 precededthem. Standardlinear/concaveellipticregularity is the only PDE referenceinput. GeneralNPP/PVPmovingfiniteness remains anuncompletedreconstruction, not a claim that the publishedtheorem is open. NewfixedbackgroundidealL1metric/curvecompletion65 drafted andauditing.


## 2026-09-15 00:55UTC: current manuscript through72

All65–72 passed and included;72completed reports total,69correct and3historicaladverse reportsallresolved; all fullreportsread. Fixed-background idealL1metric and complete curve counterexample65; exactfinite-divisorGaudvolume andthreshold66; negative-square Hessian/classderivative recovery67; compactunibranch resolution foundations68; finite-cone radialmetric product andpositivevolumeblowupboundary69; finiteGaudtracehomeomorphism/completepotentialmetric70; quantitativeonesidedboundedstability71; exactGauddenominatorcollapsecriterion72. New final researchprogram separates publishedbutunreconstructed NPP/PVP existence from two workingconjectures and higherdimtrace, topology, residualsystem, kernel andsingularspacequestions.

Remaining recent theorem inputs: BGLbig-backgroundcontact support underitsstatedregime; ALSgeneralNPP/PVP existence(noBMP); XLarbitrarybiggeneralNPP existence(BMPandPVP). Fixed-nudominatedcontinuity nowfullyproved anditsoutdatedexternal labelremoved. No general moving-reference lowerroofmassfiniteness claim. StandardlocalBT/envelopes/regularization and SGPTcharacterizations remainallowed standardinputs.

New73Holderregularity and74compactGaudcurrentdual problem are draftedandunderboundedRethlasreview, NOTINCLUDED. Current386pagebuild includes28chapters+unibranchappendix; needscleverefproblemformatfix(repairedsource), reflowcheckandcheckpoint12freeze.

## 2026-09-15 01:38 UTC: further differences and verified constructions

The bounded equation theory now includes quantitative one-sided stability and an explicit nonoptimalHolder theorem in strictlypositiveHermitian backgrounds, withoutBMP orpositive lowerdensity. GeneraldegenerateHolderregularity has not been obtained by relabeling the background.

The Gauduchon theory extends from smoothmetrics to compactnormalizedpositive ddc-closedcurrents. Determinants are applied to Radon–Nikodym matrixdensities, not by wedgingcurrents. The optimization representsallscalar-normalization supportingprobabilities forcontinuouslogdensities. It providesuniformsubcriticalLqintegrability, withcriticalexponentn/(n-1) exactlyequivalenttoPVP. Uppermassmayremaininfinite, as the explicitHopfexample shows. GenericuniquenessisprovedbyBaire; uniquenessateverycontinuousdensityremainsaseparateconjecture.

Pan25singularGaudmetricexistenceisnowrecordedasknownliterature, withreducedirreducibleambienthypotheses and conformal/quasiisometricuniquenessclass. It is context, not an unproved premise of the unibranchappendix. LuHDR22's scalarfactorforweakMApowerquestionisdistinguishedfromourmatrix-currentoptimization.


2026-09-15 02:05UTC: audit77 passed and full report read. Bounded semipositive-big Lp solutions are locally continuous wherever a fixed strict barrier is locally bounded, noBMP/PVP; general Demailly curvature modulus retained. Included after73, awaiting build. Audits78(local homogeneous Dirichlet) and79(continuous-obstacle general-big contact) are pending and not included. Full general unbounded-obstacle contact and moving-reference generalNPP reconstruction remain incomplete.


2026-09-15 03:24UTC: audits80smooth-current-flow,81NUMAconstruction,83symmetryselection allpassed and full persisted records/reports read. 82geometryinitial wrong only for almostanalytic vsanalytic definition; geometry_problem_connections_repair_01 passed, fullreportread, exactdefinitionfixed and section INCLUDED. DangTheorem4.3 conditional smoothflowconvergence underbigness nowexplicitlyknown/cited afterrootfullstatementread, notleftasopenconditionalstep. 84big_general_contact_01 PASSED all82deductions/ninereferences; FULL562linereportandfinalJSONread. Generalbigcontact forfiniteaeqcunboundedobstacles reconstructedwithoutBMP/PVP usingglobalpolecompetitorrepair plusfixed-levelSIGNEDcapacitylimits. INCLUDED and chapter11external label/BMPassumptionremoved; researchprogram distinguishesstillunresolvedmovingroofmassgap. 85radialC1,1NUMAfamily and86canonicalselectedlimit areACTIVE, NOTINCLUDED.

2026-09-15 04:20 UTC: Minimal-reference general NPP measure equations now reconstructed under PVP, no BMP (general_measure_minimal_01 passed). Local Ceg98 decomposition -> global bounded theta-carrier -> bounded-density truncations -> fixed-measure continuity. Earlier general-measure gap notes now apply to arbitrary prescribed reference, not phi=0.
