# Independent verification of the thin-zero-set construction

Run ID: `numa_thin_zero_set_independent_01`

## Verdict

**Correct under the stipulated accepted original construction and standard inputs.** The complete sequential audit contains 52 small-deduction checks and 4 reference checks, with no critical errors and no gaps. Repair hints: none.

## Independence and accepted inputs

Only the submitted proof and [the accepted original construction](/Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex) supplied mathematical input. No previous thin-zero-set audit, its results or memory, another new NUMA draft, or a new PDE theorem was used. Fresh parallel subtasks within this run checked the endpoint algebra, barriers, and geometry; the primary verifier independently recomputed every deduction below. No numerical evidence was used. The original source was read directly, including its normalization, coefficient cutoffs, positive nonclosed background, and bounded-mass argument. This report certifies the submitted mathematical argument under those premises, not novelty or current literature status.

## Six crucial claims

| Claim | Finding |
|---|---|
| Fixed trial density | Pass: all three coefficients are positive away from the two rank-one hypersurfaces; the density equals 1 near the omitted lines. |
| Small negative slope perturbations | Pass: compact continuous dependence and scalar uniqueness give one nonempty parameter interval and the strict upper comparison. |
| Both endpoint barriers | Pass: the left residual is negative and is a backward lower barrier; the right residual is positive and is a forward lower barrier. The factor on the right is p(-q)>0. |
| Global interval existence | Pass: hypothetical interior endpoints retain positive horizontal margins on compact intervals, so continuation applies. |
| Smooth flat endpoint extension | Pass at every derivative order: b^(j)=O(delta^(-2j)) and h^(j)=O(p delta^(-2j)); the actual zero extension is smooth. |
| Global assembly, normalization, and BMP | Pass: solution forms are semipositive globally, cubes have the correct common normalization, parameters stay distinct, and the accepted fixed background retains BMP. |

## Sequential deduction ledger

The following entries follow the submitted proof's textual order. Each item records the assertion, its direct check, and the result.

### Statement and proof input

**0.1. Input is usable mathematical proof text. — PASS**

The text gives fixed data, a scalar trapping lemma, a flat-extension lemma, and final global assembly in normal logical order.

**0.2. Target and precise solution class. — PASS**

Need one fixed smooth strictly positive nonclosed background omega on P3 and one fixed smooth g>=0; uncountably many distinct smooth omega-psh potentials (solution forms semipositive, not necessarily strictly positive where g=0) with equal cube g omega_X^3 and sup=0; zero set exactly M_- union M_+; bounded mass for the fixed background.

**0.3. Allowed prerequisites. — PASS**

The full exact original construction is accepted; no new density/ODE claim is accepted from it. Smooth scalar ODE theory and elementary differential calculus/barriers are explicitly accepted. BMP already belongs to the accepted original background. No new PDE theorem is needed.

**0.4. Independence and scope. — PASS**

The old run is named only as the user's acceptance premise; none of its records was opened. Novelty, publication history, and book editing are outside this audit.

### Fixed bump, retained construction, and thin-density definition

**1.1. The new p is permitted by the original construction. — PASS**

C=(integral_{-1}^1 exp(-1/(1-r^2)) dr)^(-1)>0 gives integral p=1, hence beta=2p has integral 2. p is even, positive in the band, smooth and flat at endpoints. q=p'=-2r p/(1-r^2)^2 has the required signs.

**1.2. All original coefficient identities apply to this p. — PASS**

The source sets x=p+a,y=p+b,z=z0=(q^2+chi^2)^(1/2) on the band, with z0>=|q| and z0>0 in the interior. On r<-2/3 inside the band, (x,y,z)=(1+p,p,q); on r>2/3, (x,y,z)=(p,1+p,-q). At r=-1,+1 the values are (1,0,0),(0,1,0).

**1.3. Slope sp is a global smooth trial potential. — PASS**

The accepted F has F'=2p, so G_s=sF/2 is a smooth primitive of sp, constant on each end. ddc G_s=sp(P-Q)+s q R=sH. Thus omega+ddc(G_s-rho)=omega0+sH.

**1.4. Strict positivity in the band for 0<s<1. — PASS**

x+sp=a+(1+s)p>0 and y-sp=b+(1-s)p>0. z+s q=z0+s q>=z0-s|q|>=(1-s)z0>0. Positivity follows in the independent rank-one frame.

**1.5. Positivity off the band and exact rank at its boundaries. — PASS**

H=0 for |r|>=1. omega0 is strictly positive for |r|>1, including its Fubini-Study extensions over the omitted projective lines. At M_- it is P and at M_+ it is Q, each rank one. Hence only those hypersurfaces have zero cube.

**1.6. Fixed smooth density and determinant normalization. — PASS**

The smooth global form omega0+sH has smooth cube. Divide by the positive global smooth volume omega_X^3 to obtain smooth g>=0. On U the cube is 6 k_s P wedge Q wedge R, while omega_X^3=6 sigma(r)sigma(-r)sigma'(r) P wedge Q wedge R, so g=k_s/[sigma(r)sigma(-r)sigma'(r)]. The common factor 6 cancels and g is chosen before eta.

**1.7. The zero set consists of smooth real hypersurfaces of measure zero and empty interior. — PASS**

In accepted local coordinates partial r contains -d tau/tau with tau nonzero. Thus dr never vanishes on U, and the two distinct finite level sets r=-1,+1 are disjoint smooth real codimension-one submanifolds of real six-dimensional P3. Their local graphs have zero smooth-volume measure and empty interior; no extra zeros occur at X minus U.

### Lemma: Trapping the scalar solutions — equation and left endpoint

**2.1. Smooth scalar ODE domain. — PASS**

D={(r,h):-1<r<1,-x(r)<h<y(r)} is open. Both denominator factors are strictly positive there and all coefficients are smooth, so F_s=k_s/[(x+h)(y-h)]-z is smooth on D. This assertion does not extend D to the singular endpoints.

**2.2. The exact solution sp lies in D. — PASS**

Substitute h=sp: F_s(r,sp)=z+s q-z=s q=(sp)'. The horizontal factors are the positive quantities established in step 1.4. Thus uniqueness comparisons use an actual exact solution on all of (-1,1).

**2.3. Left trial determinant coefficient. — PASS**

For x=1+p,y=p,z=q and h=cp, the three factors are 1+(1+c)p, (1-c)p, and (1+c)q. Their product is (1-c^2)(1+(1+c)p)pq, exactly the submitted formula. Here p>0 and q>0.

**2.4. Left comparison is strictly positive on a full endpoint neighborhood. — PASS**

For 0<c_L<s, the coefficient difference A(c_L,p)-A(s,p), where A(c,p)=(1-c^2)(1+(1+c)p), has value s^2-c_L^2>0 at p=0. Continuity and p(r)->0 give a fixed open endpoint neighborhood with positive difference. Multiplication by p q>0 preserves the strict sign without requiring either factor bounded away from zero.

**2.5. Left differential residual and barrier type. — PASS**

For L=c_Lp, F_s(r,L)-L'=(k_s-k_cL)/[(x+c_Lp)(y-c_Lp)]<0; denominator=[1+(1+c_L)p](1-c_L)p>0. Thus L'>F_s(r,L): a strict forward supersolution, which is the lower barrier for backward evolution.

### Lemma: Trapping the scalar solutions — right endpoint

**2.6. Right trial determinant coefficient, including q sign. — PASS**

For x=p,y=1+p,z=-q and h=cp, the three factors are (1+c)p, 1+(1-c)p, and (c-1)q=(1-c)(-q). The product is (1-c^2)(1+(1-c)p)p(-q). On this neighborhood q<0, so p(-q)>0.

**2.7. Right comparison for the negative lower barrier. — PASS**

For s<t<1, A_R(s,0)-A_R(-t,0)=(1-s^2)-(1-t^2)=t^2-s^2>0, where A_R(c,p)=(1-c^2)(1+(1-c)p). Hence k_s>k_-t throughout a sufficiently small fixed right endpoint neighborhood. The factor p(-q)>0 is essential and has the correct sign.

**2.8. Right differential residual and barrier type. — PASS**

For B=-tp, B'=-tq. Subtracting it gives F_s(r,B)-B'=(k_s-k_-t)/[(x-tp)(y+tp)]>0. Denominator=(1-t)p[1+(1+t)p]>0. Thus B'<F_s(r,B): a strict forward subsolution and lower barrier for forward evolution.

### Lemma: Trapping the scalar solutions — compact initial interval and crossing arguments

**2.9. Uniform compact-interval continuous dependence. — PASS**

Choose r_L,r_R in the fixed respective endpoint neighborhoods. The graph of sp over [r_L,r_R] is compact in D, so its distance to each horizontal boundary is positive. At its endpoints, sp-c_Lp=(s-c_L)p(r_L)>0 and sp-(-tp)=(s+t)p(r_R)>0. Smooth ODE continuous dependence forward and backward from 0 preserves domain membership and both strict endpoint inequalities for a single eta0>0 and every 0<eta<eta0.

**2.10. No crossing of the upper exact solution. — PASS**

If h first meets sp at an interior point of its connected interval of existence, local uniqueness makes the two solutions identical near that point and throughout their common connected interval, contradicting h(0)=sp(0)-eta. Therefore h<sp everywhere it exists, in either time direction.

**2.11. Left lower barrier cannot be crossed backward. — PASS**

At a proposed first contact r_* on moving left, w=h-c_Lp has w(r_*)=0 and w>0 immediately to its right. Differentiability gives w'(r_*)>=0. Step 2.5 instead gives w'(r_*)<0. This contradiction proves strict c_Lp<h throughout the left interval of existence.

**2.12. Right lower barrier cannot be crossed forward. — PASS**

At a proposed first contact moving right, w=h+tp has w(r_*)=0 and w>0 immediately to its left; thus w'(r_*)<=0. Step 2.8 gives w'(r_*)>0. Hence -tp<h throughout the right interval of existence.

### Lemma: Trapping the scalar solutions — continuation and quotient bounds

**2.13. No left finite continuation breakdown inside (-1,1). — PASS**

On the left trap, x+h>=1+(1+c_L)p>0 and y-h>=(1-s)p>0. If a maximal left endpoint r_*>-1 existed, p would have a positive minimum on a small compact interval containing r_* and lying in the left neighborhood. The closed trapped strip there is bounded and is a compact subset of D, so accepted continuation extends h. The argument does not claim a uniform positive lower bound as r approaches -1.

**2.14. No right finite continuation breakdown inside (-1,1). — PASS**

On the right trap, x+h>=(1-t)p>0 and y-h>=1+(1-s)p>0. At a proposed maximal endpoint r_*<1, p has a positive minimum on a compact neighborhood. The graph stays in a compact subset of D and extends by continuation. No coefficient lower bound at r=1 is assumed.

**2.15. Global interval existence and compact quotient ranges. — PASS**

The solution already exists on [r_L,r_R]; steps 2.13 and 2.14 extend it to all (-1,1). All neighborhoods and c_L,t,eta0 were chosen independently of eta. Division by p>0 gives b=h/p in (c_L,s) on the left and (-t,s) on the right, with closures compactly contained in (-1,1).

### Lemma: Flat extension at the endpoints — scaled identities and smooth rational functions

**3.1. The quotient b=h/p is legitimate and bounded. — PASS**

p>0 on the open band, so b is smooth there. Trapping gives closures [c_L,s] and [-t,s], each a compact subset of (-1,1), independently of eta. These are endpoint bounds only; no limiting value or endpoint differentiability of b is assumed.

**3.2. Recomputed left ODE identity. — PASS**

At h=bp the horizontal product is [1+(1+b)p](1-b)p. Dividing k_s=(1-s^2)[1+(1+s)p]pq by this product and subtracting z=q yields h'=q{(1-s^2)[1+(1+s)p]/([1+(1+b)p](1-b))-1}. This equals q R_L(p,b).

**3.3. Recomputed right ODE identity. — PASS**

At h=bp the horizontal product is (1+b)p[1+(1-b)p]. Dividing k_s=(1-s^2)[1+(1-s)p]p(-q) by it and subtracting z=-q gives h'=q{1-(1-s^2)[1+(1-s)p]/((1+b)[1+(1-b)p])}. This equals q R_R(p,b), with the right sign.

**3.4. Every rational-function partial derivative is bounded on a fixed relevant neighborhood. — PASS**

Restrict p to [0,Pmax] on fixed small endpoint neighborhoods. For the left compact b interval, [1+(1+b)p](1-b)>=1-s>0; for the right, (1+b)[1+(1-b)p]>=1-t>0. Compactness permits a slightly larger open neighborhood whose closure avoids denominator zeros, so all partial derivatives of each rational R are bounded there, order by order.

**3.5. Scaled differential equation has no missing term or factor. — PASS**

Differentiating h=pb gives h'=q b+p b'. Combining with h'=q R yields b'=(q/p)(R-b). For the chosen bump q/p=-2r/(1-r^2)^2 exactly.

### Lemma: Flat extension at the endpoints — bump growth and all-order induction

**3.6. Controlled logarithmic derivatives. — PASS**

For endpoint distance delta and A=q/p=-2r/(1-r^2)^2, A^(m)=O(delta^(-m-2)) for every m, since its endpoint poles have order at most 2.

**3.7. Every derivative of p retains exponential decay. — PASS**

T_0=1 and T_(j+1)=T_j'+A T_j give p^(j)=p T_j. The rational T_j has pole order at most 2j. Hence |p^(j)|<=C_j p delta^(-2j).

**3.8. Noncircular induction at every order. — PASS**

One can sharpen the draft to b^(j)=O(delta^(-2j)). The base case is trapping. Put S=R-b. In j derivatives of A S(p,b), derivatives of S of order ell involve p and b derivatives whose total order is ell and individual orders are at most ell. Bounded partials and the induction hypothesis give O(delta^(-2ell)). A product A^(m) (S(p,b))^(j-m) is O(delta^(-(m+2)-2(j-m))) and thus O(delta^(-2j-2)). Only b derivatives of orders <=j are used to bound b^(j+1).

### Lemma: Flat extension at the endpoints — vanishing jets and zero extension

**3.9. Every h derivative tends to zero. — PASS**

Leibniz gives h^(j)=sum_i binom(j,i) p^(i)b^(j-i)=O(p delta^(-2j)). Since p=C exp[-1/(delta(2-delta))], this tends to zero for every j at both endpoints.

**3.10. Actual smooth extension, not merely vanishing function values. — PASS**

Extend every h^(j) by zero at and beyond an endpoint. It is continuous by step 3.9. By the mean value theorem the interior difference quotient at the endpoint for extended h^(j) equals h^(j+1) at an intervening point, which tends to zero. The exterior difference quotient is zero. Induction proves these are all successive derivatives of extended h. It is C-infinity and flat.

**3.11. No extra endpoint assumptions. — PASS**

The argument never evaluates the singular ODE at +/-1, assumes no limiting value or smoothness for b=h/p, and uses no uniform endpoint ellipticity. All growth estimates are derived from the equation.

### Main theorem proof — global primitive and solution form

**4.1. Global smooth primitive on the real line. — PASS**

The proved zero extension is C-infinity and supported in [-1,1]. Thus G_eta(r)=integral_0^r h_eta(t)dt is smooth and constant separately on r<=-1 and r>=1. Its constants need not coincide.

**4.2. Smooth projective extension. — PASS**

The open sets |A|^2<e^(-1)|B|^2 and |A|^2>e|B|^2 contain the omitted lines A=0 and B=0. G_eta is already constant on their portions in U, so assigning the respective constant gives smooth extensions. Near r=+/-1, its smoothness follows from the flat-extension lemma and the smooth finite coordinate r.

**4.3. Exact form and normalization factors. — PASS**

For u_tilde=G_eta-rho, omega+ddc u_tilde=omega0+ddc G_eta. The accepted chain rule gives (x+h)P+(y-h)Q+(z+h')R with no additional 2 or 4pi factor: F'=2p and H=(1/2)ddc F, and all retained forms use the source's same scaled normalization.

### Main theorem proof — positivity and equality of measures

**4.4. Strict positivity throughout the open band. — PASS**

Continuation and trapping give x+h>0 and y-h>0. The ODE gives z+h'=k_s/[(x+h)(y-h)]>0, since k_s>0 at every interior point, including r=0 where z0=chi(0)>0. Positivity follows from the independent rank-one frame.

**4.5. Global semipositivity, including degeneracy hypersurfaces. — PASS**

On |r|>1, h=h'=0 gives omega0, strictly positive there and equal to omega_X near omitted lines. At r=+/-1, flatness gives h=h'=0, so the form equals P on M_- and Q on M_+, each semipositive of rank one. These are admissible smooth omega-psh solutions.

**4.6. The cube equals the same fixed density everywhere. — PASS**

In the band, (x+h)(y-h)(z+h')=k_s; both cubes therefore equal 6 k_s P wedge Q wedge R. Outside, both forms reduce to omega0. On M_+/- their rank-one cubes are zero. Smooth gluing introduces no singular boundary derivatives. Dividing by omega_X^3 gives precisely the earlier g, independent of eta.

### Main theorem proof — normalization, distinctness, background and bounded mass

**4.7. Supremum normalization is defined and preserves the equation. — PASS**

Each u_tilde is globally smooth on compact P3, hence has a finite attained supremum. Subtracting it leaves ddc u unchanged, so positivity and the fixed measure are preserved.

**4.8. Injection survives normalization. — PASS**

Different eta give different h_eta(0). If two normalized potentials were equal, their unnormalized potentials would differ by a constant, so d(G_eta-G_nu)=(h_eta-h_nu)dr would vanish. At r=0, dr is nonzero and the slope difference is nonzero, a contradiction. The parameter interval (0,eta0) is uncountable.

**4.9. The same strict smooth nonclosed background is retained. — PASS**

omega=omega0+ddc rho is the accepted source background for the permitted explicit p, and neither h nor eta changes it. The source's small-epsilon argument proves strict positivity. Direct differentiation gives dR=-dr wedge(P-Q), hence d omega=dr wedge[(x'-z)P+(y'+z)Q]. At r=0, x'=y'=0 and z=chi(0)>0, so this is z dr wedge(Q-P), nonzero in the independent source frame.

**4.10. Bounded mass is inherited with its exact meaning. — PASS**

The accepted source already proves for every bounded omega-psh v that integral(omega+ddc v)^3<=C^3 integral omega_X^3, using omega<=C omega_X, the positive mixed expansion, and closed bounded Stokes. The new construction changes only the density and potentials. omega is unchanged, so the same bound for all bounded omega-psh functions remains valid; it is not merely a bound on the constructed family.

### Concluding explanatory paragraph and assumption audit

**5.1. Infinite-order density degeneracy. — PASS**

At each hypersurface, the two vanishing coefficients of the trial form are flat in r: on the interior they contain p or q, and on the exterior they are the source's flat cutoff coefficients. The third coefficient is smooth. Their product, divided by a smooth nonzero volume factor, is flat. Thus g degenerates to infinite order along M_+/-.

**5.2. Exactly three components in the positive-density set. — PASS**

Normalize homogeneous lifts by |A|^2+|B|^2=1. For each finite r the level is the connected quotient of two 3-spheres at fixed positive radii by diagonal S^1. Varying the radii connects each r-interval, and each omitted projective line belongs to the appropriate connected exterior region. Thus r<-1, -1<r<1, and r>1, with the projective ends included, are exactly the three components.

**5.3. Different exterior translation constants are possible and actually occur. — PASS**

For eta!=nu, scalar uniqueness makes h_eta-h_nu have one strict sign on the band. For D=G_eta-G_nu, its constant exterior values satisfy D_right-D_left=integral_{-1}^1(h_eta-h_nu)dr!=0. Normalization changes both constants by the same amount, so their difference persists. The fixed rho cancels in potential differences.

**5.4. No invalid global ellipticity inference. — PASS**

All solution forms are positive on the three open components but rank one on both intervening hypersurfaces. Their squared forms and pairwise mixed products vanish at those hypersurfaces. Thus the usual linearized mixed tensor cannot be globally elliptic there. The paragraph is a description consistent with the explicit construction, and no maximum-principle or PDE uniqueness theorem is imported.

**5.5. All material prerequisites are used correctly. — PASS**

0<s<1 ensures positive trial coefficients and allows c_L<s<t<1; the negative initial displacement is necessary for the upper comparison; the exact endpoint cutoffs determine both barriers; z0>=|q| with z0>0 supplies interior positivity; the special exponential p supplies polynomial logarithmic derivatives and flatness; the rank-one frame and global source background supply geometry and BMP. No required hypothesis is silently dropped.

## Reference ledger

The submitted proof cites the accepted internal construction and its own new lemmas, and invokes explicitly accepted scalar ODE inputs. It cites no new external-paper theorem. Consequently the required arXiv-first/web-fallback procedure was not triggered; the original construction's own accepted proof was not reopened through external sources.

### Reference 1: Thin-density setup: reference to sec:degenerate-hermitian-nonuniqueness

**Statement.** Retain p,q,x,y,z,P,Q,R,omega0,rho from the original construction, using its permitted exponential bump; P^2=Q^2=R^2=0, P wedge Q wedge R>0, ddc G(r)=G'(P-Q)+G''R, and omega=omega0+ddc rho is smooth, strictly positive and nonclosed.

**Definitions and hypotheses.** The source's beta has integral 2, p=beta/2 has integral 1, q=p', and F'=2p. H=(1/2)ddc F. All source forms are scaled by 1/(4pi) relative to its NUMA convention while functions remain unchanged. The new proof uses these same forms and hence the same coefficient identities.

**Comparison and application.** Exact definitions and factors match. On the band x=p+a,y=p+b,z=z0. z0>=|q| is positive inside. The source gives precisely (1+p,p,q) on the left and (p,1+p,-q) on the right, with rank-one omega0 only at M_+/- and omega_X near omitted lines. The new ODE and density conclusions were checked separately, not inferred from this citation.

**Search disposition.** No external-paper theorem is newly cited here. This is an explicitly accepted internal construction, inspected directly as required. Searching another source would not replace the stipulated input.

**Result:** matched_and_applicable; no error or gap.

### Reference 2: Trapping lemma and flat-extension lemma: accepted standard inputs and internal cross-references

**Statement.** Smooth scalar ODE existence, uniqueness, continuous dependence, and continuation on compact subsets of the smooth domain; elementary scalar barrier crossing; differentiation and flatness. The theorem invokes the two newly proved lemmas.

**Definitions and hypotheses.** The ODE is used only on D={-1<r<1,-x(r)<h<y(r)}. Compact-interval continuous dependence is invoked before either endpoint. Continuation is invoked only at hypothetical endpoints strictly inside (-1,1). Endpoint smoothness is proved directly rather than obtained from continuation at a singular endpoint.

**Comparison and application.** All prerequisites were checked in steps 2.1-2.15 and 3.1-3.11. The internal lemma conclusions used in global assembly match what was proved. No external existence, PDE regularity, or uniqueness theorem is invoked.

**Search disposition.** User explicitly accepts these standard inputs; no external paper cited.

**Result:** matched_and_applicable; no error or gap.

### Reference 3: Opening and closing discussion: the source's unresolved empty-interior question

**Statement.** The original source leaves uniqueness for a density whose zero set has empty interior as a further question.

**Definitions and hypotheses.** The exact final paragraph states that this further question is explicitly left open in NUMA and that regularity and solution class matter. Here the claimed answer concerns smooth normalized omega-psh potentials on a nonclosed Hermitian background.

**Comparison and application.** The proposed construction does address the smooth class stated in this submission. This audit does not certify novelty or independently establish the current literature status. No theorem from the manuscript is used to infer the new conclusion.

**Search disposition.** Historical context is an explicitly accepted premise, not an external theorem used as a proof step. No external-paper theorem is present in the submitted proof requiring arXiv-first search.

**Result:** matched_as_accepted_context; no error or gap.

### Reference 4: Main theorem proof: inherited bounded mass

**Statement.** The fixed original omega has a uniform Monge-Ampere mass bound for all bounded omega-psh functions.

**Definitions and hypotheses.** The source proves this using omega<=C omega_X, a positive mixed expansion, and closed bounded Stokes, giving mass at most C^3 integral omega_X^3.

**Comparison and application.** The submitted proof keeps exactly the same omega and changes only the density and potentials. The previously accepted estimate therefore applies to all bounded omega-psh functions. No new theorem is needed.

**Search disposition.** Explicitly accepted internal source; not a newly cited external-paper theorem.

**Result:** matched_and_applicable; no error or gap.

## Adversarial failure checks

The sign of the backward barrier, the negative q on the right, loss of denominator margins, uncontrolled high endpoint derivatives, missing one-sided extension, failure of global positivity, determinant factors, and collapse after normalization were all tested directly in the ledger. None produced a failure. In particular, no lower bound away from zero at r=+/-1 was assumed, and no convergence or smooth extension of b=h/p itself was required.

## Artifact and verdict checks

All deduction and reference records were persisted with MCP memory tools in this run. Operational memory-write approval timeouts were retried successfully and caused no lost finding. Mathematical failure arrays are empty. The final JSON is validated and written with the required MCP verification-output tools. No book file or previous result was edited.
