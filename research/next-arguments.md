# Next arguments: relative compactness without BMP

Research notes,14 September2026 ~16:00UTC. These are a proof plan, NOT yet book theorems. The146-page checkpoint does not contain this material. Read pending Rethlas reports before using new big-Lp and relative-barrier results as audited inputs.

## A. A weighted lower-semicontinuity lemma

For semipositive theta (or any smooth theta using local corrections), u_j->u in capacity, uniformly bounded above, and nonnegative uniformly bounded quasi-continuous a_j->a in capacity, aim to prove for nonnegative continuous eta:
 integral eta a MA_ext(u) <= liminf integral eta a_j MA_ext(u_j).
No uniform raw-mass hypothesis is needed. Take continuous cutoffs g_T(s) in[0,1] vanishing for s<=-2T, equal1 for s>=-T, and increasing to1 asT->infinity. Rewrite a_j g_T(u_j) MA_ext(u_j) as a_j g_T(max(u_j,-2T)) MA(max(u_j,-2T)). Bounded capacity continuity gives its limit. It is <=a_j MA_ext(u_j). ExhaustT and use absence of pluripolar mass. This also supplies lower semicontinuity of integrals |exp(u_j)-exp(v)| against moving MA when capacity convergence holds, via quasi-continuous weights and common upper bounds.

For monotone genuine qpsh sequences, capacity convergence follows by bounded truncation continuity plus the capacity tail of a common genuine lower bound. For a selected a.e.-convergent L1 subsequence, upper tails U_j=(sup_{ell>=j}u_ell)^* decrease to canonicalu; local Hartogs lemma identifies the limit. This is useful for capacity sandwiches.

## B. Fixed-measure integral convergence as a STANDARD local input

GZ17 Lemma11.5 / classical Cegrell lemma: a uniformly bounded qpsh sequence in a fixed lower-curvature class, converging in L1(dV), converges in L1(mu) for each fixed finite NPP measure mu. State the exact input and its local-to-global use; user permits standard references. KN22 Lem2.1/Cor2.2 give the subsequence version from a.e. convergence; full convergence follows by the every-subsequence-has-a-further-subsequence criterion. Do not cite a recent Hermitian global lemma as a substitute without explaining this classical boundary.

For unbounded u_j with a common upper bound C, exp(u_j) is a uniformly bounded A omega-psh family (A dependingC and theta), and exp(u_j)->exp(u) in L1(dV). Thus the fixed-measure input applies to exponential weights. This is what ALSLemma2.6 usages with unbounded normalized u_j really need.

## C. Moving bounded BT measures: reconstruct, do not copy KN22

New primary research/sources/KN22.pdf/.txt = arxiv2212.11550v1Dec2022, fulltext first5pages read. Lem2.3 proof has apparent omissions: T sum starts at1 instead0, and h ddcT vanishes from the next displayed line without justification. Restore these terms. Source proceedings were published2025 (conference2022),vol481,113-123,DOI10.1007/978-981-96-0447-0_10; institutional records verified.

Target: bounded omega-psh u_j->u L1 and bounded omega-psh w_j->w in capacity imply integral|u_j-u| omega_wj^k omega^(n-k)->0 for allk. Their uniform range alone bounds each mass by localCLN; noBMP.

1. phi_j=max(u_j,u)->u in capacity (Hartogs/quasi-continuity, or upper-tail sandwich after a.e. subsequence). Thus integral(phi_j-u)omega_wj^k omega^(n-k)->0 by a UNIFORM capacity bound for fixed-range mixed products.
2. h_j=phi_j-u_j>=0. Let z=w_j-w_l. Difference of products is ddc z wedge T, where T=sum_{s=0}^{k-1}omega_wj^s omega_wl^(k-1-s) omega^(n-k), degree(n-1,n-1).
3. Compact Stokes: integral h_j ddc z T = integral z ddc(h_j T). Keep ALL terms:
 ddc(hT)=ddch T + dh dcT - dch dT + h ddcT.
 dT=domega R,dcT=dcomega R with positive mixed polynomialR ofdegree n-2. ddcT is a finite sum of ddcω times positive mixeddegree n-2 and domega dcω times positive mixeddegree n-3; exact coefficients can be written but uniform constants suffice. Bound absolute terms by fixed smooth ω powers and positive mixed products.
4. S0 bounded by integral|z|(omega_phi_j+omega_uj)T ->0 uniformlyj,l large, since z->0 in capacity and all mixed potentials have fixed bounded range.
5. h ddcT bounded by C integral|z| times fixed-range positive mixed products ->0. This term MUST be retained.
6. Gradient term Cauchy–Schwarz <= C[ integral|z| dh dch ωR ]^(1/2)[ integral|z|ω²R ]^(1/2). First factor uniformlybounded because|z|<=2A and integral dhdch ωR<=C(A). Prove this last uniform energy by dhdch<=2(dphi dcphi+du dcu), identity ddcp²=2pddcp+2dpdcp and integration by parts. ∫dpdcp S =1/2∫p² ddcS -∫pddcp S; bounded p, positive omega_p and full torsion expansion ofddcS plus localCLN bound it. AllmixedSforms have fixedrange; smoothapprox thenBT justifies calculation. Secondfactor ->0 bycapacity. The othergradientterm similar.
7. Fix l large, use fixed-measure Cegrell for integral h_j MA(w_l)->0, then letl->infinity. This avoids using movingmeasurelemma to prove itself. Worksn1 triviallyT=1,dT0.

## D. Capacity criterion with a common same-type lower barrier

Hypotheses theta>=0big, ALSmodelphi with smaller-background envelope, u_j andu in same ordinarytype phi, common w<=u_j with w~phi, uniform upper bound, and supMAmassesfinite. If I_j=∫|exp(u_j)-exp(u)| MA(u_j)->0, then capacity convergence.

Proof after selecting subsequence I_j<=2^-j and a.e. convergence:
 p_j,N=Ptheta(min_{j<=ell<=N}u_ell), p_j=Ptheta(inf_{ell>=j}u_ell). All >=w and <=phi+C, hence genuine same type. Rooftop contact partition gives ∫|exp(p_j,N)-exp(u)|MA(p_j,N)<=Σ_{ell=j}^N I_ell<=2^(1-j). A above +decreasing capacity convergence passesN; increasingp_j->p andA give ∫|exp(p)-exp(u)|MA(p)=0. Have w<=p<=u so bothp,u~phi. ThereforeMA(p){p<u}=0. Singular strict domination c=0 applies to(p,u) becauseP_delta theta(p) genuine, yieldingp>=u. Thusp=u. Sandwichp_j<=u_j<=U_j (upper tails) withbothmonotonecapacitylimitsu proves result. Every-subsequence argument givesfullsequence.

Then if MA(u_j)<=nu fixedfiniteNPP, B onexp(u_j) givesI_j->0. Also tails{u_j<-T}subset{w<-T}, so nu tails ->0. Our raw-tail continuity proves weak MA convergence. This is the same-type/commonbarrier regime of ALS4.1, requiresNO PVP. Do NOT confuse with ALS4.2 which constructs a relative rooftop fromdominationusingPVP.

For domination by C MA(psi_j), boundedpsi_j->psi cap, C givesI_j->0; capacities dominate measuresuniformly and commonw tailcapacity->0, so rawcontinuityagain. This suppliesALS4.1condition1inthecommonbarrier regime.

## E. Bounded subsolution theorem ALS5.1

1 smoothstrictf relative to MAθ(psi),psiboundedθpsh. ChooseHermitianΩ>=θ and smoothΩpsh psi_j↓psi (boundedexactreg), q_j=Pθ(psi_j) bounded↓psi. Contact and orderedcomparisoninΩ implyMAθ(q_j)<=Ω_psij^n, henceboundedLebesguedensity foreachj. BigLp theorem solvesMAθ(u_j)=exp(lambda u_j) f MAθ(q_j). Uniformbarriersq_j±C boundu_j. ApplyD+C (dominationbyΩ_psij andcommonconstantbarrier) forcapacity; boundedweightedBT passesrightside.
2 boundedf>=0nonzero, smoothpositivef_j uniformlybounded convergingL1(MApsi) anda.e. Solveusingstep1. Lowerbarrierpsi-C uniform. UpperneedsmixedMA inequality andfixed boundedpsi trace, since supf_j^-1 notuniform.
 At eachsolutionconstructedbyq_k approximate, mixedinequality MAroot yields theta_uj wedge theta_psi^(n-1)>=exp(lambda uj/n) f_j^(1/n) MAθpsi; caninvokeSTANDARDLOCALmixedmeasureinequalitybutformulateandverify itsnonclosedpassage byboundedlocalcalculus. SourceNguyen16Lemma1.9.
 Normalizev_j=u_j-sup, c_j=exp(lambda sup). exp(lambda v_j/n) uniformlyboundedqpsh, B gives subseqconvergenceµpsi-a.e. Nonzerof ensuresweightedrootintegral positive limit. Then integrate mixedinequality. Needbound∫theta_vj theta_psi^(n-1) uniformly; replacepositiveformsbyHermitianΩpsi andStokes:
 ∫theta_vj Ωpsi^(n-1)=∫theta Ωpsi^(n-1)+∫v_j ddcΩpsi^(n-1).
 Normalizev_j<=0; torsionexpansion bounds using weightedCLN withnegativeqpshv_j andboundedpsi, normalizedL1. Thisgivesc_j upper. Commonlowerandupper now D+B givescapacity andequation. f_j->f L1fixedµ plusweights yieldsrightconvergence. NoPVP/BMP.

## F. ALS5.2 addition theorem and same-type existence

SourceALS26.txtlines1130-1445 fully read. Addition theorem forµ=exp(-lambda u)MAu+exp(-lambda v)MAv finite,u~v~phi:truncateu_j,v_j,solveboundedexpwithµ_jviaE, andbarriers(uj+vj)/2-C/2-nlog2/lambda <=solution<=minuj,vj. Commonphi-Cbarrier. Weightedselferror splitsfinitelevelwhereµ_j=µ anddeepregion with |exp(solution_j)-exp(limit)|<=Cexp(-j), massboundedpolynomialO(j^r) (oursharperr works withconstantsC; sourcesusen). D givescapacity; rawtailclosedness/commonbarrierlocalizedweights thenequation. Needexplicituniformrawtails maybeusingexpdampeddata onfinitelevels+truncdeepmass timesexp factors; sourcehandleslocalizedmasscomparison, inspectcarefully.

ALS5.4Perron/maximalweightedmass argument uses existing supersolutionw~phi, µ0=exp(-lambda w)MAw<=f; familyweightedmeasures betweenµ0andf. Candidatesu_j<=w bysingularexpcomparison. Uniformlower boundonsup frombounded auxiliarypsi+P_epsilon theta(phi) (its type mayMOREsingularbutorderconditionvalid becausecandidate has smallerbackground). Relativeestimate thencommonphi-Cbarrier; D givescapacity and MAcontinuity. Weightedmeasureweaklimit<=f andfinitelevelweightedidentification givesweightedMA=family supremum. Ifresidualf-g nonzero, supersolutionv forresidual haspositiveMA bysingularDom; Fadditiongivescontrad largerweightedmass. No uniformmass/PVP.
ALS5.7 smalllambda followsboundedauxcomparisonupperc_j, normalizedrelativeestimatecommonbarrier,D thenequationandpositivity fromsingularDom. Carefulcandidatev_jexpweights smalllambdaL1 estimatealreadyproved. FullNPPversionstillneedsPVPandadditionalclassclosureproof.

## Update16:36UTC

A–F are now written in section_relative_compactness.tex, section_bounded_subsolution.tex, section_addition_equation.tex and section_prescribed_existence.tex. Full same-type Lp existence is in the160-page current draft, independently auditing prerequisites. The commonbarrier audit found a standalone monotone-sequence sentence lacking genuineness of the decreasing limit. It is corrected explicitly; every actual application had phi-C as a genuine lower barrier. Retain the failed report and run a bounded repair check. The main criterion needs NO uniform rawmass, and prop:lower-barrier-criterion allows bounded approximants if the limit retains typephi. Addition localizes on g_T(w) withw=(u+v)/2-D; then truncation error region is killed exactly forj>2T. General NPP/PVP and laterSGPTgeometry remain open proof obligations.

## Normalization chapter,16:56UTC

Now written in chapter_normalization.tex (current168-pagePDF14chapters), normalization_functional_01 running(exec16260). B_phi(F)=logunique scalar forMAu=c expF dV inordinarytypephi. Provedorder/translation/Lip, concavity viaunboundedconvexdensity finite-levelreduction, boundedL1continuityviarelativeestimate/commonbarriers. HB directional sublinearfunctional ->nonemptyconvexweakcompactsupportingprobabilities A_phi(F); boundedL1continuityandsmallvolumecutoffs proveeachprobac dV. StabilityunderuniformF andone-sidedderivative formulas giveGateauxdiffiffsingleton. SmoothHermitianF recoversGaudadjoint; closedKahler formulaB=logmassphi-log integralexpF. NoassertionofuniqueAinweakcaseorweakadjointcurrentidentity. No noveltyclaim. All168pagesvisuallyreviewed; physical151–158at110dpi; firstpropositionopeningneedspaceadded,rebuild/reflowreviewpending. Priorphysical128–149repairpagesrechecked95dpi.

Potential next deduction NOTYETWRITTEN: H_phi(nu)=sup_FinC(X)(B_phi(F)+integralFnu) isconvexweaklsc onProb, >=B_phi(0). Supportinginequality yields B_phi(F)=min_nu[H_phi(nu)-integralFnu], minimizers exactlyA_phi(F). FiniteHforcesac: compactnullKwithnuK>0, F=tchi_j, boundedL1B(tchi_j)->B0 forfixedt, H>=B0+t nuK all t. ClosedKahler H=logmassphi+relativeentropy(nu|dV) (dVnotnecessarilyprob): Gibbsinequality givesupper; clippedlogdensityandcontinuousL1(dV+nu)approxgivelower,nonacHinf. This is a density-sidevariationalformula, notrawMAenergy. Couldaddwithshortseparateaudit.

## Rays and test curves nowwritten17:10UTC

Seechapter_rays.tex/chapter_testcurves.tex andSTATUS. Bothauditing. PureenvelopedualityusesPfixedphiandP[u_t]=phi,supct explicitly; neverusegeneralPidempotenceoridentifyEenv. Normalizationchapterpassed. Nextgeometrytrace/analyticregularizationneedsreader-friendlysourceaudit. Entropydualityideaabovestillnotwritten.

## Update17:26UTC: duality and restriction

The normalization dual idea is now written in section_normalization_dual.tex, with additional uniform-integrability and measurable-data stability arguments. Audit normalization_dual_01 active (exec46522). Testcurve connectedness recheck active (exec94518); original book convention already connected, historical extract was missing it.

Candidate trace datum, NOT YET PROVED/WRITTEN: for smooth connected compact Y in X and generic nu(u,Y)=0, a_t=I(tu) O_Y nonzero. For every divisorial valuation E overY, tau_Y,u(E)=lim_t ord_E(a_t)/t. Subadditivity of multiplier ideals gives superadditivity of ord and Fekete gives existence (possiblyinfinity). Global Demailly approximants of ordinarytype (1/m,I(mu)), uniform lower curvature, restriction and normalized compactness on a resolution should make every tau finite. Depends only on ambient I-class; homogeneous; order; superadditive for sums from ideal subadditivity. Analytic u should give tau=nu_E(u|Y) by Skoda I-versus-Iinfty bounds. For genuine naive restriction, OT ideal inclusion gives tau<=nu_E(u|Y). No general qpsh realization or canonical P-class follows automatically. On a compact curve, total sum tau(p)<=integral theta|Y from approximant mass and Stokes; construct a realizing qpsh potential by scalar Poisson with current sum tau(p)delta_p plus smooth residual. This would give a unique I-class, not automatically a P-class. Need exact global approximation input and a full audit.

## Trace nowwritten17:48UTC

chapter_analytic_approximation.tex andchapter_trace_data.tex written, auditsinprogress analytic_approximation_01(exec2404) andintrinsic_trace_data_01(exec79973). The standardglobal theorem is DemaillyJuly2011Theorem14.12, notmerely1992mainattenuationtheorem. Maintraceatallglobaldivisors finiteviaGauddegree1oncompactmodifications. CurveprofileD hasmassd<=M=integralthetaY; Greenpotentialw hasddcw=D-deta, definescanonicalORDINARYtype (differentvolumechoices differencesmooth). Curverepv solvesfullcurrentD+(M-d)eta; extendedMAexact(M-d)eta. Dm<=D, TVconv,dyadicDm↑D andGreenwm↓w; analapproxrestrictionordinaryeqwm. Naiverestrictiongenuinepreceqw sinceitsatomiccurvaturedominatesD; analyticordinaryequality. CurveLp equationinthisordinarytype hasc=(M-d)/integralf, positiveiffM>d, normalizedpotentialunique. Necessity: boundedqpshdifferencea-w impliesnonatomicresidualcurvaturedoesnotchargepolarsets. Allpendingindependentaudit.

Potential NEXTshortsupplementnotyetwritten: chooseAeta oncurve dominatingallrestrictedapproxbackgrounds andA>d. SGPT exactordered dS formula (sourcechapter_comp.tex lemma lma:varphileqpsi_metric, lines764ff) gives dS(w,wm)=1/2[d-Dm(Y)] because j=0termcancels,n=1. Ordinaryequivwm~u_mY gives same distance forrestrictedapproximant. Thus fullsequence dSconverges w oncurve, usingaKahlermetricONCURVE only, noambientKahler/BMP. WhenambientXisKahler, SGPTquasiequiDemaillytype(2^-j,I(2^ju)) givesdefinitionofsource trace, soatomictrace representsSGPTtrace Pclass. This fillscomparison forcurve only; do not infer higherdimmetric.

## 2026-09-14 18:25 UTC — next proofs, not yet established

### Cao comparison and exact trace additivity
Primary Cao2015 published3-page PDF now research/sources/Cao15.pdf/.txt, manifest entry. DOI10.1016/j.crma.2014.11.004. Read entire primary webPDF. Source order is opposite ours. Its printed approximant1/k log sum|g|² with weight e^-2kphi has a normalization inconsistency; use our exact1/m log sum andexp(-mu) throughout, reconstruct locally.

Proposed proof: fixed analytic approximation S_k to u+v satisfies u+v<=S_k+O(1). Resolve its ideal: S_k∘π=sum c_i log|s_i|²+O(1),c_i>0. Siu decomposition of locally smooth-corrected closed positive ddc(u∘π),ddc(v∘π) gives generic orders alpha_i,beta_i with alpha_i+beta_i>=c_i. Choose0<=a_i<=alpha_i,0<=b_i<=beta_i,a_i+b_i=c_i. Residual qpsh bounded above gives uπ<=sum a_i logs+C and vπ<=sum b_i logs+C. For f∈I(mu),g∈I(mv), pullback integrability with Jacobian orderA_i=ordEJ+1 gives ordEf+A_i>ma_i,ordEg+A_i>mb_i. Hence ordE(fg)>mc_i-2A_i. For eps_m=max_i2A_i/(mc_i), mlarge, every product generator has order>=m(1-eps_m)c_i along all selected components. Divide holomorphic generators by these monomials; their norms give U_m+V_m <=(1-eps_m)S_k+O(1) upstairs then downstairs. Bounded S_k is trivial. Finite cover handlesglobalcompactordinarycomparison; prooflocaldoesnotneedclosedglobalbackground. RestrictY thenpullbackdivisorE: b_m(u)/m+b_m(v)/m >=(1-eps_m) b_k(u+v)/k. Letm∞ thenksup ⇒tau_u+tau_v>=tau_sum. Existing subadditivity givesopposite ⇒EXACTADDITIVITY. This is a proposed reconstruction to write/check, NOT yet a theorem inbook. Rational coefficient convention applies tointegerapproximants; coefficientsa_i,b_i realonlyintermediate.

### Higher-dimensional trace majorants
Possible easy construction, NOT exact realization yet: restricted approximants U_m inonefixedHermitianbackground onY; normalize sup0 thenL1subsequence limitv. Pullback underanyfixedcompactmodification should preserveL1convergence (prove usinglocalqpshcompactness andidentityoffexceptional), and uppersemicontLelong givesnu(v,E)>=tau(E). Thus profile has a global qpsh majorant. Alternatively dyadic I-envelopes Q_Comega(U_2j) decrease sincea2m⊂a_m², have sup0 andyieldgenuineIfixedlimit. Exactnu=tau stillnotautomatic; possible extraordersinlimit. Define envelope ofallComega-psh potentials<=0 withnu>=tau, showgenuine andIfixed usinglocalvaluativecriteria/Choquet/Lelonguppersemicont, separateambientbackground dependence. Oncurves thisenvelopeisQ(w) andrecoversexacttrace. Do notclaimhigherdimexactrealizationwithoutproof.

### General nonpluripolar equations
New relative_class_domination chapter and fixed-nucompactness supplement nowdrafted; separateaudits32/33 activeorfinishing. Fixednu proof usesdisjointcontactpieces=>MA finite-roof<=nu (noNfactor); stretchedrooftopmass>=kappa and<=B^nnu; testexp(u) preventscollapse forlarge tailstartj uniformlyendpointN; B=2b averagingrestoresfiniteprefix. Afterextraction commonhE; lowerrooflimitp hasMAp<=nu BEFOREstrictdomination. Originalwhole-sequence roofisnotasserted.

Moving uniformly boundedreference MA measures remainhard. ALS4.2 sourceproof says passsubsequencephi_j<=-j butjcountsnumberobstacles; arbitraryroofsubsequence cannotrenamethatcount. Also fixednu sourceproof usesv_j=P(u1..uj) butquotes2^-j tailerror; our newproofusesactualtailj..N. Need repairmovingcase, notcopy.

Onepotentialalternate route: globalize standardLOCALCegrell nonpluripolar decomposition intoµ=f MA_theta(psi) boundedpsi forsemipositivebigtheta. Localboundedpshpieces canbegluedto globalomega-psh bounded functions; strictbigbarrierrho plusδlocalpieces andconstanttruncations produceboundedtheta-potentialsdominatinglocalMAonexhaustion; convexsummableboundedseriesgivesoneboundedthetaMA withµabsolutelycontinuous. Requires carefullocalgluing andexactstandardmeasuredecompositioninput. CouldhelpNPPexistence butprescribedtype stillneedsrelativecompactness for smoothboundedψ_j. Do notassumeboundeddatarelative toboundedMA preservesordinarytypephi; that is strongerthanLp theorem andunproved.

We have >11hoursremaining todeadline06:19UTC; do notshrinkfullscope. GeometricSGPTchaptersstilloutstanding.

## 2026-09-14 18:47 UTC — explicit exponential rooftop barrier

New separately drafted section_exponential_rooftop_barrier.tex, not yet included/audited. For u_j Ephi, u_j<=phi+C, MAuj<=A exp(lambda uj) MAomega(psij), psij uniformly bounded, every r_jb=Q_b(uj,phi) has exp(-lambda r_jb/b)MAr_jb<=b^n A MApsij and hence finite mass. q=P_epsilon theta(phi), strict big rho with theta_rho>=a omega, delta<(1-epsilon)a. s_jb=q+(1-epsilon)rho+delta psij-C_b has theta_s>=delta omega_psij and weightedMAs>=b^nA MApsij for delta^n exp(lambda C_b/b)>=b^nA. Relative finite exp comparison underPVP gives r_jb>=s_jb>=H_b fixed genuine. If eachu_j ordinaryeqphi, r_jb ordinaryeqphi and the earlier smaller-background exp comparison applies WITHOUTPVP. ThusH_b/b+(1-1/b)phi belowALLuj, h=Pinfuj genuineEphi forfullsequence. No movingref convergence needed. This avoids sourceALS4.2 bad obstacle-count extraction entirely. L1limitthenEbyupwardstability. Needs independent audit.

Capacity convergence still unresolved in generalmovingcase. Tempting truncation max(uj,phi-K) argument is INVALID as first conceived: MA of a maximum can carry new boundary mass on the equality set, so it is not bounded above by the two obstacle measures. Do not use that argument. Common-h E alone plus selferror gives limitpE supported{p=u}, but neither MAp nor MAu has yet been provedfinite. SourceALS4.3 cites Kähler DDNL25Thm2.6 for finiteness underL1 while capacity is still being established; that step requires a valid Hermitian proof. Fixed-nu case was repaired by finite-roof measures<=nu givingfinitep BEFOREdomination. For moving boundedMA measures, finite-roofpartition bounds bysumdifferentmeasures do not yielduniformmass. This gap remains separate from now-explicitclassclosure.


## 20:22 UTC: alternative Perron route considered, NOT proved

For finite nonzero mu=f MA_omega(psi), psi bounded and f bounded, a global subsolution family could avoid the unresolved moving-reference mass-finiteness argument. With q=P_epsilon theta(phi), strict barrier rho, and delta small, s=q+(1-epsilon)rho+delta psi has MA_theta(s)>=delta^n MA_omega(psi). For each b>1, w_b=s/b+(1-1/b)phi-C_b has MA>= (delta/b)^n MA_omega(psi), and C_b large makes exp(-lambda w_b)MA>=mu. Supremum of all such subsolutions would have stretched envelopes genuine for EVERY b, so potentially E_phi. An upper bound for normalized subsolutions may follow from the LOCAL mixed inequality theta_v wedge omega_psi^(n-1)>=exp(lambda v/n)f^(1/n)MA_omega(psi), normalized weighted CLN and compactness/Cegrell against the fixed finite measure.

NOT SOLVED: Perron equality, not just inequality, with prescribed possibly very singular phi. Local bounded Dirichlet replacement can destroy the upper singularity constraint v preceq phi. Need a justified local lifting retaining that constraint, or a global obstacle/penalization argument. Do not present this as an existence proof. L1 mass lower semicontinuity alone is NOT a safe replacement: local logarithmic divisor approximations illustrate discontinuity of nonpluripolar products; global relative hypotheses must be used. Earlier moving-finiteness gap unchanged.
