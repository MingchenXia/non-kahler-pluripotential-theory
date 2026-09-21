# Verification report: numa_thin_zero_set_01

## Verdict

**Correct under the exact accepted prerequisites.** The sequential audit found no critical error and no gap. All six crucial claims pass. The construction gives uncountably many distinct normalized smooth solutions for one fixed smooth nonclosed Hermitian background with bounded mass, and one fixed smooth density whose zero set is exactly two disjoint smooth real hypersurfaces.

## Findings at a glance

| Claim | Result | Decisive check |
| --- | --- | --- |
| 1. Fixed trial density | Pass | All three trial coefficients are positive off the two rank-one interfaces; the density equals 1 near the omitted projective lines. |
| 2. Initial perturbations | Pass | Compact-core continuous dependence gives one perturbation interval; scalar uniqueness keeps each slope strictly below sp. |
| 3. Endpoint barriers | Pass | Left pq is positive and the differential defect is negative; right p(-q) is positive and the differential defect is positive. The backward and forward crossing directions are correct. |
| 4. Global interval existence | Pass | Traps prevent the graph from leaving the smooth ODE domain at a finite interior stopping point. No uniform denominator bound at the endpoints is assumed. |
| 5. Smooth flat extension | Pass | Every derivative of h/p has at most polynomial endpoint growth, and every derivative of h retains the exponential factor p. Endpoint difference quotients vanish at every order. |
| 6. Globalization and bounded mass | Pass | The source chain rule and common cube factor 6 agree. End constants extend smoothly; normalization preserves injectivity; the same background retains the accepted mass bound. |

The archived manuscript supplies the original construction and explicitly leaves the empty-interior question open. The new density and perturbed solutions are verified here from the displayed formulas. No numerical evidence, new PDE theorem, other NUMA draft, or novelty certification is used.

## Scope and evidence

The exact accepted construction was read in full: [section_degenerate_nonuniqueness.tex](/Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex). Its SHA-256 is c55d376ccdd0f320c963f620c01987d97cf6b62cc1cc0d52751f64abb33c4e84.

The [archived NUMA text](/Users/mingchen/Non-Kahler/research/sources/NUMA-Xia.txt) was also read in full. Its SHA-256 is e696e6dd9a3f30889a92982c00ecc14ccd8e40b3d5b6eb6b62165102e6cd0638. The [archived PDF](/Users/mingchen/Non-Kahler/research/sources/NUMA-Xia.pdf) has SHA-256 7482f76f0c53776c313c34cb287e7cb2f71e6a066e4955cba364e70b6d0b72a5. The previous passed verdict was read as provenance, and supplies no proof of the new claims.

The required skill order was sequential verification, reference verification, then synthesis. The ledger below reproduces all 75 deduction checks in textual order and all five reference checks from the MCP memory records. Three independent bounded audits checked the trapping lemma, all-order flatness, and geometric globalization; each found no error or gap.

## Critical errors

None.

## Gaps

None.

## Repair hints

None required.

## Sequential deduction ledger
### Input and theorem announcement

**S00.1 — PASS.** The supplied proof is usable mathematical text. The announced existence theorem is treated as a target, not as a premise.

**S00.2 — PASS.** The target requires one fixed smooth strictly positive nonclosed background omega, one fixed smooth nonnegative g, exactly two real hypersurfaces as its zero set, uncountably many distinct smooth omega-psh solutions after sup normalization, and BMP.

**S00.3 — PASS.** Only the exact accepted source construction, the chosen exponential bump, and the enumerated elementary ODE/calculus inputs are used. A passed earlier verdict is provenance, not evidence for the new density or the new solutions.

### Setup: retained source coefficients and specific bump

**S01.1 — PASS.** The accepted source defines r=log(|A|^2/|B|^2), ddc r=P-Q, R=dr wedge d^c r, independent semipositive rank-one P,Q,R, and P^2=Q^2=R^2=0. Hence ddc G=G'(P-Q)+G''R and the cube is 6xyz PQR.

**S01.2 — PASS.** The book rescales all source (1,1)-forms and ddc by 1/(4pi), with scalar functions unchanged. Both cubes rescale by (4pi)^(-3), so no determinant coefficient or density factor changes.

**S01.3 — PASS.** For p=C exp(-1/(1-r^2)), the integral of the unnormalized positive bump is finite and positive, giving a unique C>0 with integral p=1. Then beta=2p is exactly a permitted source bump with integral beta=2; q=p'=beta'/2. This fixes the background construction once.

**S01.4 — PASS.** The bump is even, positive inside, zero and flat outside. q has sign -r, so q>0 on (-1,0), q<0 on (0,1), and q(0)=0. The source gives x=p+a, y=p+b, z=z0>=|q| with z0>0 throughout the band.

**S01.5 — PASS.** The primitive of sp is sF/2 up to a constant, because source F'=2p. Thus its Hessian is exactly sH, with H=p(P-Q)+qR, and its global trial potential relative to omega is sF/2-rho up to a constant.

### Fixed trial density before Lemma Trapping the scalar solutions (claim 1)

**S02.1 — PASS.** With fixed 0<s<1, x+sp=a+(1+s)p>0 and y-sp=b+(1-s)p>0 for -1<r<1; the nonnegative source cutoffs need not have any additional positivity.

**S02.2 — PASS.** z0+sq>=z0-s|q|>=(1-s)z0>0, including r=0 where q=0 but chi(0)>0. Thus k_s is strictly positive on the full open band.

**S02.3 — PASS.** At r=+-1, p=q=0, so the trial form equals omega0, which is rank one there. For |r|>1 the trial form is omega0>0 and k_s=xyz. Near both omitted projective lines omega0=omega_X, so there are no hidden zeros at the ends.

**S02.4 — PASS.** The ratio of the global smooth top form (omega0+sH)^3 to the global smooth strictly positive omega_X^3 is a global smooth function g>=0. Its zero set is exactly M_- union M_+, and g=1 near the omitted lines. It is fixed independently of eta.

**S02.5 — PASS.** In source coordinates A=(1,a), B=tau(1,b), partial r has coefficient -1/tau in d tau. Hence dr is nowhere zero on U; r=+-1 are smooth real codimension-one level sets. They are disjoint, closed in X, and have empty interior and zero measure for any smooth volume form.

### Lemma Trapping the scalar solutions: ODE domain and upper exact solution (claim 2)

**S03.1 — PASS.** D={(r,h):-1<r<1,-x(r)<h<y(r)} is open. The denominator (x+h)(y-h) is positive on D, and all coefficients and k_s are smooth, so F_s is smooth on D.

**S03.2 — PASS.** Substitution of h_s=sp gives F_s(r,sp)=z+sq-z=sq=(sp)'. Both horizontal factors were checked positive, so h_s is a solution in D on the entire open band.

**S03.3 — PASS.** An initial value sp(0)-eta lies in D for all sufficiently small eta>0. Local smooth scalar existence and uniqueness therefore apply. The admissible maximal interval contains zero.

### Lemma Trapping the scalar solutions: left endpoint calculation (claim 3, left)

**S04.1 — PASS.** The source cutoffs give exactly a=1,b=0,chi=0 near -1. Consequently x=1+p, y=p, z=q and q>0 there.

**S04.2 — PASS.** For -1<c<1 the trial coefficient is [1+(1+c)p](1-c)p(1+c)q=(1-c^2)[1+(1+c)p]pq. In particular pq>0; it is not discarded as sign-indefinite.

**S04.3 — PASS.** For any fixed c_L in (0,s), the difference of the bracketed coefficients at p=0 is s^2-c_L^2>0. Continuity in p and p(r)->0 give a fixed open left endpoint interval with k_cL>k_s. No uniform strictly positive value at the endpoint is claimed.

**S04.4 — PASS.** The trial denominator [1+(1+c_L)p](1-c_L)p is positive at every interior point. Since k_cL=denominator*(z+c_Lq), F_s(r,c_Lp)-c_Lq=(k_s-k_cL)/denominator<0.

**S04.5 — PASS.** Thus c_Lp is a strict supersolution in forward time and has the correct orientation for a lower barrier in backward time.

### Lemma Trapping the scalar solutions: right endpoint calculation (claim 3, right)

**S05.1 — PASS.** The source cutoffs give exactly a=0,b=1,chi=0 near +1. Hence x=p, y=1+p, z=-q and q<0.

**S05.2 — PASS.** The trial product is (1+c)p[1+(1-c)p](c-1)q=(1-c^2)[1+(1-c)p]p(-q). Here p(-q)>0, which is essential for the comparison.

**S05.3 — PASS.** For fixed s<t<1, the coefficient difference for c=s minus c=-t at p=0 is t^2-s^2>0. Continuity gives a fixed right endpoint interval where k_s>k_-t.

**S05.4 — PASS.** At h=-tp the denominator is (1-t)p[1+(1+t)p]>0. Therefore F_s(r,-tp)-(-tp)'=(k_s-k_-t)/denominator>0, exactly as displayed.

**S05.5 — PASS.** Thus -tp is a strict subsolution in forward time and has the correct orientation for a forward lower barrier.

### Lemma Trapping the scalar solutions: common compact core and upper ordering (claims 2 and 4)

**S06.1 — PASS.** Choose fixed r_L<0<r_R inside the respective endpoint intervals. The graph (r,sp(r)) over [r_L,r_R] is compactly contained in D, since the horizontal factors are continuous and positive there.

**S06.2 — PASS.** The reference endpoint gaps are (s-c_L)p(r_L)>0 and (s+t)p(r_R)>0. Smooth ODE continuous dependence over this compact reference segment gives one eta0>0 for existence, admissibility and both strict endpoint inequalities for every 0<eta<eta0.

**S06.3 — PASS.** The same fixed c_L,t,r_L,r_R,eta0 work for the full perturbation interval. There is no assumption of continuous dependence all the way to the singular endpoints.

**S06.4 — PASS.** If h and sp met at any point in their common connected interval, local uniqueness and continuation of equality would give h(0)=sp(0), contradicting eta>0. Thus h<sp throughout its maximal admissible interval.

### Lemma Trapping the scalar solutions: crossing and continuation (claims 3 and 4)

**S07.1 — PASS.** For a first backward contact with c_Lp, w=h-c_Lp is zero at the contact and positive immediately to its right; differentiability requires w'>=0 there. The strict left differential inequality gives w'<0. Thus no such contact occurs.

**S07.2 — PASS.** For a first forward downward contact with -tp, w=h+tp is zero at the contact and positive immediately to its left; differentiability requires w'<=0 there. The strict right differential inequality gives w'>0. Thus no such contact occurs.

**S07.3 — PASS.** Near the left, c_Lp<h<sp implies x+h>1+(1+c_L)p>=1 and y-h>(1-s)p. Near the right, -tp<h<sp implies x+h>(1-t)p and y-h>1+(1-s)p>=1. The slope is bounded by fixed multiples of p.

**S07.4 — PASS.** At a hypothetical maximal left endpoint alpha>-1 or right endpoint beta<1, choose a compact interval around that finite interior point. p has a strictly positive minimum there, so the above inequalities keep the graph in a compact subset of D. F_s is bounded there and smooth on a compact neighborhood; accepted ODE continuation extends the solution, a contradiction.

**S07.5 — PASS.** The core is already covered by compact continuous dependence. Thus the maximal admissible interval is all (-1,1); there is no additional middle continuation case.

**S07.6 — PASS.** Dividing endpoint traps by p>0 places h/p in the closed intervals [c_L,s] and [-t,s], respectively. Both compact intervals lie strictly inside (-1,1), uniformly in eta. No uniform positive lower bound for p at +-1 was needed.

### Lemma Flat extension at the endpoints: exact scaled equations (claim 5)

**S08.1 — PASS.** On each endpoint interval b=h/p is smooth because p>0 and h is smooth. Here b denotes the scaled slope and temporarily shadows the source cutoff b; the formulas explicitly use x=1+p,y=p or x=p,y=1+p, so there is no identification of the two functions.

**S08.2 — PASS.** On the left the denominator is [1+(1+b)p](1-b)p and k_s=(1-s^2)[1+(1+s)p]pq. Cancelling p gives h'=q*((1-s^2)[1+(1+s)p]/([1+(1+b)p](1-b))-1)=q R_L.

**S08.3 — PASS.** On the right the denominator is (1+b)[1+(1-b)p]p and k_s=(1-s^2)[1+(1-s)p]p(-q). Subtracting z=-q gives h'=q*(1-(1-s^2)[1+(1-s)p]/((1+b)[1+(1-b)p]))=q R_R. The sign agrees with q<0.

**S08.4 — PASS.** Differentiating h=pb gives h'=qb+pb'; division by p, not by q, yields b'=(p'/p)(R_L/R-b). These R_L/R are rational scalar functions and do not denote the source rank-one form R.

**S08.5 — PASS.** On a fixed rectangle 0<=p<=p_max and b in [c_L,s] or [-t,s], 1-b>=1-s>0, 1+b>=1-t>0 and 1+(1+-b)p>=1. The rational denominators stay nonzero even at p=0. There is an open neighborhood with compact closure where every partial derivative is bounded, order by order.

### Lemma Flat extension at the endpoints: polynomial derivative induction (claim 5)

**S09.1 — PASS.** Direct differentiation of log p gives L=p'/p=-2r/(1-r^2)^2. Each derivative of L is rational with poles only at +-1; it is therefore bounded by a finite power of d^(-1), where d=1-|r|.

**S09.2 — PASS.** Write p^(m)=p A_m, A_0=1 and A_(m+1)=A_m'+L A_m. Induction makes every A_m rational with poles only at +-1. Thus every p derivative is p times a polynomially bounded rational function, and is itself polynomially bounded since p is bounded.

**S09.3 — PASS.** Set S(p,b)=R_L/R(p,b)-b. All its partial derivatives are bounded on the same compact rectangle; this explicitly includes the linear -b term in the displayed scaled ODE.

**S09.4 — PASS.** The trapping estimate supplies the induction base b bounded. Since b'=L S(p,b), the first derivative is polynomially bounded.

**S09.5 — PASS.** Assume derivatives b^(m), m<=j, are polynomially bounded. Differentiating b'=L S(p,b) j times gives a finite sum of L derivatives times composite derivatives of S. Repeated chain and product rules use only bounded partial derivatives of S and derivatives of p,b of order at most j. Products of finitely many polynomial bounds remain polynomial bounds. No b^(j+1) occurs on that right side.

**S09.6 — PASS.** Thus b^(j+1) is polynomially bounded. Induction covers every finite derivative order; it does not assume b has a limit or a smooth extension.

### Lemma Flat extension at the endpoints: flatness and one-sided extension (claim 5)

**S10.1 — PASS.** Leibniz gives h^(j)=sum_(ell=0)^j binom(j,ell) p^(ell)b^(j-ell). Each p derivative contains the factor p, and each remaining factor has polynomial endpoint growth, so |h^(j)|<=C_j p d^(-N_j) for every j.

**S10.2 — PASS.** Since 1-r^2=d(1+|r|)<=2d, p<=C exp(-1/(2d)). Hence p d^(-N)->0 for every finite N, proving h^(j)->0 from inside at both endpoints for every j.

**S10.3 — PASS.** For each j define f_j=h^(j) inside and zero at and outside the endpoints. Each f_j is continuous. Its endpoint difference quotient is bounded by C_j p d^(-N_j-1)->0. Therefore f_j is differentiable at each endpoint with derivative zero, equal to f_(j+1). Inside and outside this derivative identity already holds.

**S10.4 — PASS.** Induction in j proves the zero extension is C-infinity on R with all derivatives zero at +-1. This verifies actual one-sided smooth gluing, not merely h tending to zero.

### Main theorem proof: global primitives and fixed background (claim 6)

**S11.1 — PASS.** For each eta the extended h_eta is a globally smooth real function supported in [-1,1]. Its primitive G_eta is smooth and is constant separately on (-infinity,-1] and [1,infinity). The two constants need not be equal.

**S11.2 — PASS.** The ratio |A|^2/|B|^2 tends to 0 near the omitted line A=0 and to infinity near B=0. Hence G_eta(r) is exactly constant on a neighborhood of each line and extends smoothly there. The two lines are disjoint; different constants pose no compatibility constraint.

**S11.3 — PASS.** At finite levels r is smooth and composition with smooth G_eta is smooth, including r=+-1 by the flat extension. The source rho is smooth and zero near the omitted lines. Thus u_tilde_eta=G_eta(r)-rho is globally smooth.

**S11.4 — PASS.** The accepted source constructs rho=epsilon(r^2-1)kappa and chooses one sufficiently small epsilon>0 making omega=omega0+ddc rho strictly positive everywhere. On the central region rho''=2epsilon and rho'=2epsilon r; positivity at the degenerate levels and on the remaining compact region is verified in that source.

**S11.5 — PASS.** The source computes d omega=d omega0=dr wedge((x'-z)P+(y'+z)Q), with x'=y'=0 and z=chi(0)>0 at zero. Independence of dr wedge P and dr wedge Q gives d omega!=0. Neither eta nor the fixed scalar s alters omega or rho.

### Main theorem proof: global admissibility and equality of measures (claim 6)

**S12.1 — PASS.** The source chain rule and cancellation of ddc rho give omega+ddc u_tilde_eta=(x+h_eta)P+(y-h_eta)Q+(z+h_eta')R.

**S12.2 — PASS.** Inside the band the horizontal coefficients are strictly positive by the trapping lemma and admissibility. Since k_s>0, the ODE makes z+h_eta'=k_s/[(x+h_eta)(y-h_eta)]>0. Independence of the three rank-one directions gives a positive definite solution form there.

**S12.3 — PASS.** Its cube on the band is 6(x+h_eta)(y-h_eta)(z+h_eta')PQR=6k_sPQR, exactly the cube of omega0+sH. The common factor 6 and the ddc normalization therefore cancel correctly.

**S12.4 — PASS.** For |r|>1 the extended h_eta and h_eta' vanish, so the solution form is omega0 and its cube equals the trial cube. At r=+-1 flatness makes both derivatives zero, giving precisely the rank-one form omega0 and zero cube.

**S12.5 — PASS.** Near each omitted projective line the primitive is constant and rho=0, while omega=omega_X. Thus the global equality also holds there. Alternatively, equality of the two globally smooth top forms on dense U extends to all X.

**S12.6 — PASS.** The solution form is globally semipositive, with strict positivity away from M_+- and rank one on them. Smooth omega-psh means omega+ddc u>=0, not strict positivity of the solution form. Therefore every u_tilde_eta belongs to the required solution class.

### Main theorem proof: normalization and uncountability (claim 6)

**S13.1 — PASS.** Compactness of X and smoothness of each u_tilde_eta imply a finite attained supremum. Subtracting this constant gives sup u_eta=0 and leaves ddc u_eta and its MA measure unchanged.

**S13.2 — PASS.** If two normalized potentials agreed, their unnormalized versions would differ by a constant; rho cancels, so G_eta(r)-G_nu(r) would be constant on X. The map r takes every real value on U, so their scalar derivatives would agree, in particular at zero.

**S13.3 — PASS.** But h_eta(0)-h_nu(0)=nu-eta is nonzero for distinct eta,nu. Thus the parameter map remains injective after supremum normalization. The nonempty real interval (0,eta0) is uncountable, giving the asserted uncountable family for the same fixed data.

### Main theorem proof: bounded mass

**S14.1 — PASS.** This is exactly the accepted background omega, with no eta-dependent change. Compactness gives a fixed C'>0 such that omega<=C'omega_X.

**S14.2 — PASS.** The accepted source bounded-mass argument applies to every bounded omega-psh a: alpha=omega+ddc a>=0 and B=C'omega_X-omega>=0 imply alpha^3<=(alpha+B)^3 by positivity of mixed terms.

**S14.3 — PASS.** Here alpha+B=C'omega_X+ddc a, with closed reference C'omega_X. The accepted closed bounded-Stokes identity gives integral (alpha+B)^3=C'^3 integral omega_X^3. This controls the mass uniformly over all bounded omega-psh a, exactly BMP, rather than only controlling the displayed family.

**S14.4 — PASS.** This uses the bounded-mass proof already included in the permitted source; no new PDE or external uniqueness result validates any ODE step.

### Final explanatory paragraph and assumption-use audit

**S15.1 — PASS.** All derivatives of the trial cube vanish at M_+-: p,q and source endpoint small coefficients are flat; the local density divides by the smooth positive FS volume. Thus infinite-order density degeneracy is justified from the exact source plus chosen bump.

**S15.2 — PASS.** The sets r<-1 (with A=0 adjoined), -1<r<1, and r>1 (with B=0 adjoined) are the three complement components. For example at fixed r the level is the quotient of S^3 times S^3 by the diagonal circle, so it is connected; the intervals in r preserve connectedness.

**S15.3 — PASS.** On each exterior component all G_eta are constant and all u_tilde_eta share the term -rho, so any two solutions differ by a constant there. Scalar uniqueness orders distinct h_eta,h_nu throughout (-1,1); their integral difference across the band is nonzero. Thus their relative exterior translation constants can indeed differ after normalization.

**S15.4 — PASS.** For any two constructed solution forms alpha,beta, alpha=beta=omega0 of rank one at M_+-. Hence the difference-equation tensor alpha^2+alpha wedge beta+beta^2 equals 3omega0^2=0 there. Strict ellipticity on the positive-density components does not supply a global uniformly elliptic maximum-principle argument through these interfaces.

**S15.5 — PASS.** Every substantive prerequisite is used: the source supplies geometry, signs, cutoffs, background and BMP; 0<s<1 ensures positive factors and barrier margins; the explicit exponential bump ensures all-order endpoint bounds; initial perturbation below sp gives upper ordering; compact-domain ODE theory establishes existence and continuation. Integral p=1 ensures exact compatibility with the fixed accepted source, although the local ODE algebra alone would allow other positive scales.

**S15.6 — PASS.** No numerical computation, other NUMA draft, new PDE theorem, or novelty certification enters the verification. No unresolved critical error or gap was found in the sequential deductions.

## Reference ledger

### R1. Retained construction: cref sec:degenerate-hermitian-nonuniqueness

**Status:** verified

**Referenced statement:** The full coefficient construction in section_degenerate_nonuniqueness.tex: r and independent rank-one P,Q,R, chain rule, normalized p=beta/2 and q=p', band coefficients, exact endpoint coefficients, global smooth omega0, small correction rho giving a strict nonclosed Hermitian omega, and bounded mass.

**Source:** /Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex

**Source sha256:** c55d376ccdd0f320c963f620c01987d97cf6b62cc1cc0d52751f64abb33c4e84

**Context expansion:** Read the full exact source. Book ddc=i/(2pi) partial barpartial is 1/(4pi) of the source manuscript convention. Forms, R and cube coefficients scale consistently. The source has endpoint a=1,b=0,z=q on the left and a=0,b=1,z=-q on the right. Its p is explicitly allowed to be the normalized exponential. The new scaled-slope variable b and rational functions R_L/R_R are local notation, not the retained cutoff b or rank-one form R.

**Application check:** Every imported formula matches; the original open-band vanishing density is not treated as a result about the newly defined k_s or g.

**Reason:** User-designated accepted internal construction, inspected directly.

### R2. NUMA attribution and the empty-interior question

**Status:** verified against supplied primary text

**Referenced statement:** NUMA Theorem A constructs two distinct normalized smooth omega-psh solutions with a fixed smooth nonnegative density vanishing on an open band. Its archived final paragraph leaves the empty-interior zero-set question open.

**Source:** /Users/mingchen/Non-Kahler/research/sources/NUMA-Xia.txt

**Source sha256:** e696e6dd9a3f30889a92982c00ecc14ccd8e40b3d5b6eb6b62165102e6cd0638

**Contextual check:** Archived source read in full. Semipositivity defines omega-psh; source ddc=2i partial barpartial, all forms divided by 4pi in the accepted book. The new density and ODE family are not consequences supplied by NUMA. Public version used only to confirm reference existence; exact construction and open-question sentence checked in the authorized archive.

**Search sequence:** Full original theorem statement queried in search_arxiv_theorems first; five unrelated hits. Built-in web fallback then found the author's original theorem.

**Search outcome:** arXiv theorem match: False; web reference found: True.

The author-hosted [original nonuniqueness manuscript](https://mingchenxia.github.io/Papers/NUMA_vibe.pdf) confirms the original reference exists. Its public version has different construction details and was used only for bibliographic confirmation. The exact formulas and open-question wording were verified against the authorized local archive.

### R3. Lemmas Trapping the scalar solutions and Flat extension at the endpoints: standard inputs

**Status:** verified

**Referenced statement:** Smooth scalar ODE local existence/uniqueness, continuous dependence on a compact reference solution segment, continuation when the solution graph remains in a compact subset of its smooth domain; elementary scalar barrier crossing; differentiation and smooth flat extension.

**Context expansion:** F_s is smooth on D with strictly positive horizontal factors. Compact-core continuous dependence is applied before endpoint trapping. Continuation is used only at putative stopping points strictly inside (-1,1). The flatness proof uses only repeated chain/product rules, rational endpoint growth and exponential decay.

**Application check:** All hypotheses are checked in S03-S10. There is no invocation of a theorem guaranteeing endpoint continuation through a singular ODE domain and no endpoint boundedness assumption on p'/p.

**Reason:** These are the user's explicitly accepted standard inputs and no external paper is cited for them.

### R4. Main theorem: bounded mass

**Status:** verified

**Referenced statement:** The accepted source proves BMP by domination omega<=C omega_X, positive mixed expansion, and closed bounded Stokes.

**Context expansion:** The exact same omega is retained. The bound is uniform over all bounded omega-psh potentials, not only this family; omega_X is closed Fubini-Study. This is a user-accepted internal-source input.

### R5. Unrelated uniqueness search hits

**Status:** not applicable

**Referenced statement:** The proof imports no new PDE or external uniqueness theorem.

**Context expansion:** Returned 1404.1289 Theorem 1.10 requires a closed background; returned 1501.00891 Theorem 0.1 requires lambda>0 in exp(lambda u). These exact hypotheses do not match this nonclosed, fixed-density equation. The other three returned theorems concern different problems. None is used.

## Interpretation of the delicate points

The left barrier is a forward supersolution, which is exactly a lower barrier when evolution is followed backward. At a hypothetical first contact its derivative would have to be nonnegative from the right, contrary to the strict negative defect. On the right, the factor is p(-q), not pq; the positive defect gives the forward lower barrier.

The derivative induction does not assert that h/p has a smooth endpoint extension. It only bounds each of its derivatives by some finite power of the inverse endpoint distance. The fixed exponential factor in p then forces every derivative of h, and every required endpoint difference quotient, to vanish. Writing S(p,b)=R(p,b)-b makes explicit that the linear -b term is included in the induction.

The background omega is strictly positive, but the solution forms omega+ddc u are only semipositive at the interfaces. This is precisely the stated smooth omega-psh solution class. There is no conflict with the cube vanishing there. Different constants on the two projective ends impose no gluing constraint because each primitive is exactly constant near the corresponding omitted line.

## Persistence and completion

All mathematical checks and reference checks were persisted through MCP. The failed_checks channel records zero mathematical failures. This readable file is a rendering of those saved records. Some larger memory writes encountered automatic-review timeouts; smaller records succeeded. These operational timeouts do not alter the mathematical findings.

Only the current run's memory and result artifacts were written. The book and prior results were not edited.
