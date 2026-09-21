# General-background contact support: an unfinished localization route

2026-09-15 00:07 UTC. Research notes only, NOT a proof or book theorem.

BGL25 Theorem2.9 (archived text lines870ff) imports bounded mass. Its printed final truncation says min(f,-j), evidently intended max; do not copy. General ordered-contact is already proved without BMP. Need local contact support for a globally theta-envelope locally bounded off an analytic big-locus complement. A strict analytic theta-psh rho exists by standard Demailly approximation; max(f,rho-j) envelopes are bounded on compact subsets of rho-finite locus. If local bounded-contact support can be proved, our localized capacity continuity passes j without global mass.

Possible reduction to globally Hermitian bounded contact theorem: locally gauge theta to beta=theta+ddcq>0, v=p-q bounded on a ball. Extend v by max(v,h) to global Omega-psh V, where h is low inside/high near boundary and Omega positiveglobal equals beta on the ball. Need global quasi-cont obstacle F=V+chi(v-h)(f-p)_+ supported where v>h+epsilon. Then W=P_Omega F equalsV where chi=0. On the plurifine-open region {v>h}, V=v; W+q is theta-psh there and agrees p on a collar where0<v-h<=epsilon. If a justified bounded plurifine pasting theorem glues W+q to p elsewhere, the original theta-envelope maximality forcesW=V on innerregion. Global Hermitian contact then MA_theta p=0 there.

NOT JUSTIFIED: that pasting theorem in precisely the nonclosed setting, boundary/canonicalrepresentative details when v is only bounded qpsh, and how to ensure F globally quasi-cont with all transition collars. For continuous v ordinarypasting likelysuffices, but localcontinuity of the big-background envelope has not been established. Do not use this as a theorem. A local nonclosed Dirichlet theorem would also supply the result, but importing a recent global theorem would defeat the current self-contained proof task.

The fixed-measure dominated-continuity label in chapter12 was corrected: its full proof is chapter13. Remaining recent external results include BGL big-background contact support, ALS generalNPP semipositive/PVP existence, XL generalbig/BMP/PVP existence. These are published inputs, not open conjectures.

## New route,2026-09-15 around01:40UTC: first prove continuous-obstacle envelopes continuous off a strict analytic pole set

This is a candidate, not included or audited. It may remove the old plurifine-pasting obstacle by making {p<h} an ordinary open set.

For arbitrary smooth BIG theta, take a strict analytic theta-psh barrier rho with theta+ddcrho>=kappa omega, smooth off properanalyticZ; classicalanalyticregularization supplies such a barrier from bigness. For continuous global obstacle h normalize rho+2<=h, so p=Ptheta(h)>=rho+2 andp<=h, hencep locallyboundedoffZ.

Apply general Demailly94 fullcurvature estimate to ddcp withlowerbound-theta. The globalinputworksforunboundedqpshpwithfiniteL1; do NOT usebounded73kernelgradientuniformlyoverX. On eachcompactoffZ, p isbounded andminradiuscoercivityholds. The sameKiselman transform Phi has curvature theta+ddcPhi>=-(Ac+epsilon(delta))omega offZ. It is boundedabovebyRdelta p<=Rdelta h globally. ExtendqpshacrossanalyticZbybounded-aboveremovability. OffZ, Phi>=p-K(delta²+delta)>=rho+1forsmalldelta, hence v=(Phi+s rho)/(1+s)<=Phi, s=(Ac+epsilon)/kappa, theta-psh globally. Also v<=Rdelta h<=h+m_h(delta), where m_h(delta)->0 is the ordinary smoothing modulus of h. Therefore v-m_h(delta) is an envelope competitor and v<=p+m_h(delta).

Choose c=m_h(delta)+epsilon(delta)+delta. On {rho>=-M}, Phi-p=(1+s)(v-p)+s(p-rho)<=C_M c. Minimizingradius estimate gives t>=a_Mdelta. Monotonic regularization gives R_(a_Mdelta)p-p<=C_Mc locally; lowerbound-Kdelta². This proves local uniform smooth approximation, hencep continuous offZ. NoPDEstability orBMPused. Need carefully audit globalextension, sameglobalcurvatureconstants, andlocalattainment forunboundedp.

If this is established, p maximal on ordinaryopen{p<h}\Z by usual boundedpasting. Remaining input: maximality for continuous theta-psh implies MA_theta p=0 locally for NONCLOSED theta. A local Hermitian homogeneous Dirichlet/viscosity equivalence argument may supply this. Do not silently use the closed local-potential reduction. A from-belowC²testwiththeta+ddcq>0 would allowraisingp and contradict envelope, provingviscositysupersolution. Need exact standardlocalviscosity-to-pluripotential theorem orreconstructitbyformfreezing; no source checked yet.

Naiveconstantbackgroundreplacement: solve closedtheta_plus homogeneousDirichletwithboundaryp, repairpositivitywithsmallquadratic, envelopeforcesv-p<=epsilon r². Turning this intozeroMAmeasureuniformlyasr->0 is NOT immediate withoutquantitativerelativevolume bounds; do not claim it.
