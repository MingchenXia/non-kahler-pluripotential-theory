# STW special second-order reconstruction — research plan only

Sources STW17.pdf/.txt §2–4 fully inspected in text; exact bars in §4 formula4.3 and following specializations visually inspected pp26–27 at135dpi in tmp/pdfs/stw-source-torsion. Source uses v=u_ours/(2pi), so work temporarily with v and i partialbarpartial v, then restore constants.

Set Q0=*(gamma0^(n-1))/(n-1)! positive; Z=*(Re(i partialv wedgebarpartial gamma^(n-2)))/(n-1)!. Let chi=tr(Q0)gamma-(n-1)Q0, W=tr(Z)gamma-(n-1)Z, g=chi+v_i barj+W, P(g)=Q0+P(Hv)+Z. F(g)=logdetP(g)=h=(n-1)(Fdata+b).

Atunitarypoint, T_{ij barℓ}=T^k_ij gamma_kbarℓ skewi,j, exact
2(n-1) Z_i barj = δij Σ_p,k v_p conjugate(T_p k bark) - v_i Σ_k conjugate(T_j k bark) - Σ_k v_k conjugate(T_k j bari)
+ δij Σ_p,k v_barp T_p k bark - v_barj Σ_k T_i k bark - Σ_k v_bark T_k i barj.
Diagonal reducesΣ_p≠i,k≠i (v_p barT_p k bark+v_barp T_p k bark)/(2(n-1)); offdiagonal sums k≠j andk≠i. ThusZ_i barj independentv_bari andv_j; Zii independentbothv_i/v_bari, andcovariant∇iZii lacksv_bari viaunitarytensoridentity. Needfullyderivewedgeformulaandcovariantconsequences, notmerelyassertlongcalculation.

Eigenvaluesλ1>=...>=λn ofg, µ_i=(Σj≠iλj)/(n-1)>0 orderedascending. tildef_i=1/µ_i, f_i=Σj≠i tildef_j/(n-1), Σf=Σ1/µ. f1small, allfk k>1 comparableΣf, tildef_i i>1<=(n-1)f1. Pχ=Q0>=τI givesΣfiχii>=τΣf,Σfiλi=n. WithdetQboundedabove, largeλ1forcesµmaxlarge andµminsmall, henceΣfi(χii−λi)>τ/2Σf. Onlysourcealternative(a)neededforlogdetP, generalCsubsolutiontheorycanbeavoided.

Test H=logλmax(g)+φ(|partialv|²)+ψ(v), K=1+sup|partialv|², φ(s)=−1/2log(1-s/(2K)), 1/(4K)<=φ'<=1/(2K),φ''=2φ'^2. ψ(v)=D1exp(-D2v) positive,ψ'<0,ψ''>0, ratioψ''/|ψ'|=D2. Atglobalmaxlargeλ1, needfirstandsecondderivativeinequalityequivalentSTW3.28 withallthirdgradienttermcancellations.

A rigorous eigenvalue perturbation: choose a smooth LOCAL gamma-unitary frame e_i, matchedtoeigenvectorsatmaximum, and B=δ(I-e1 tensor e1*gamma), δfixedsmall>0. ThenA-B remainsgamma-selfadjoint nearpoint,largesttildeλ smoothisolated, <=λmax(A), equalsλ1atpoint. ConstantdiagonalB inarbitraryholcoordinateframewouldnotnecessarilyremainselfadjointawaypoint. Thischoicehasboundedfirst/secondderivatives, B11,k=0atpoint inholframe becauseB=S B0 S^-1 diagonalcommutator, so λtilde1,k=g11,k+O(λ1); secondderivativeextraBtermsO(1) absorbed. Other eigenvalues neednotbesimple; onlytopisolated. Positivequadratic eigenvalue termsdenominators λ1-λp+δ <=C_nλ1 usingtraceg>0, yielding >=c/λ1 squaresoffdiagderivatives. Mustderiveestimatewiththeseextraboundedterms explicitly.

Sourcecore3.28:
0 >= -F^{pq,rs} ∇1 g_qbarp ∇bar1 g_sbar r /λ1 -Σ f_k |λtilde1,k|²/λ1² + (1/(6K))Σ_k,p f_k(|v_pk|²+|v_pbar k|²)+φ''Σf_k|V_k|²+ψ''Σf_k|v_k|²+ψ'Σf_k v_kbar k-C(Σf_k|g11,k|/λ1+Σf).
Indicesbars MUSTcheckedvisuallynotcopiedfrompdftotext.

CaseA δλ1>=-λn, I={k:fk>f1/δ}. ForoutsideI useH_k0 andφ''=2φ'^2 toabsorbnegativegradientterm, cost2ψ'^2 δ^-1f1K. InsideI concavityspectralterm cancels(1-2δ)negativeeigen-gradientaftercomparing∇1g_kbar1 withλtilde1,k; skewZ ensuresWderivativesavoidpurev11 whenk>1, allremainingpureHessianscarrycomparablegoodfk. Source3.36keylemma includes -1/(12K)goodHessianenergy +C_epsψ'Σfk|vk|²+epsCψ'Σf-CΣf. DetailedYoungabsorption3.38–3.50needed.
Afterdealingwithg11,kand W viaequation obtains3.55:
0 >= f1(λ1²/(40K)-2ψ'^2δ^-1K)+(ψ''/2+C_epsψ')Σfk|vk|²-C0Σf+eps C0ψ'Σf-ψ'Σfk(χkk-gkk).
Usecoercivity(a), chooseepssmallrelτ thenD2largeCeps thenD1largeC0 thenδsmall4δψ'^2<ψ''/2; forcesλ1/Kbounded.

CaseB δλ1<-λn: f_n>=Σf/n andmixedHess v_nbar n≈λn+O(sqrtK) givesgoodenergy>=δ²Σf λ1²/(10nK)-CΣf. Discardconcavity, absorbg11,kbyhalfnegativegrad andH_k0 withφ''=2φ'^2, ψfixed; get0>=δ²Σfλ1²/(10nK)-Cλ1Σf, soλ1/Kbounded. FrommaxH andboundedφ/ψ, globalλ1boundC K andtraceg>0 givesallcomplexHessianboundedCK. Thenconditionalgradient61finishesgradient.

NOTYETDRAFTED, NOTCLAIMED. Needwriteandindependentaudit alllemmas,skewformulaandgeometry beforemarkingC2reconstructed. Atdeadlineifunfinishedremainexplicitexternal.
