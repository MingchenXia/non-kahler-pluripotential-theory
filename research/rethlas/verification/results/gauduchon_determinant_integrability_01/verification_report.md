# Gauduchon determinant integrability: verification report

Run: `gauduchon_determinant_integrability_01`

**Verdict: correct under the expressly accepted inputs.**

All 14 sequential audit items and four reference checks pass. No critical errors or gaps were found. The determinant theorems are independent of compact duality. The adjoint corollary uses the accepted representation; its separate audit completed with verdict correct during this run. The book was not edited.

## Scope and accepted inputs

The setting is the inherited compact complex Hermitian manifold, n >= 2, with smooth positive probability volume dV. The smooth Hermitian equation, lower Lp density estimates, smooth-density mass-extrema equality, exact Hopf metric data, and the representation for the corollary are the user-accepted inputs. Gamma_0 is the prescribed matrix-density determinant measure. The unweighted current is allowed to have a singular part.

## Sequential deduction checks

### 1. Opening setup and definition of Gamma_0

**Status: passed.**

1. Read the submitted proof in its written order. The ambient compact complex Hermitian setting and smooth positive probability measure are inherited from the preceding section; n>=2 is explicit.

2. sigma_T=omega wedge T is a positive probability measure. The supplied coefficient convention is beta wedge T=tr(BP_T)sigma_T/n, tr P_T=n, P_T positive semidefinite sigma_T-almost everywhere.

3. Put f_0=(dV/omega^n)^(1/n)>0. By scalar AMGM for the eigenvalues of P_T, 0<=(det P_T)^(1/n)<=tr P_T/n=1. Thus Gamma_0(T)=f_0(det P_T)^(1/n)sigma_T is a finite positive measure, even before proving absolute continuity.

4. Only a smooth form is wedged with T. det P_T is a measurable matrix determinant; no nonlinear wedge product of currents or total nonlinear Monge-Ampere mass bound enters.

### 2. thm:gaud-determinant-subcritical — smooth equation and lower density bound

**Status: passed.**

1. For fixed p>1 and h smooth strictly positive, h^n is smooth strictly positive and the accepted smooth equation yields smooth real u_h, Omega_h=omega+ddc u_h>0 and c_h>0 with Omega_h^n=c_h h^n dV.

2. u_h is bounded on compact X and omega-psh. Hence the accepted lower density estimate applies to F_h=c_h h^n and gives ||F_h||_p=c_h||h^n||_p>=c_p, with c_p independent of h and T.

3. Rearrangement gives c_h^(-1/n)<=c_p^(-1/n)||h^n||_p^(1/n). Since ||h^n||_p^(1/n)=(integral h^(np)dV)^(1/(np))=||h||_(np), the exponent and constant in the displayed estimate are exact.

4. If the accepted smooth solvability is formulated only for probability densities, apply it to h^n/A, A=integral h^n dV, and take c_h=c(h^n/A)/A. Thus the unrestricted positive h introduces no extra existence assumption.

### 3. thm:gaud-determinant-subcritical — pointwise matrix inequality

**Status: passed.**

1. In an omega-unitary frame let B_h>0 represent Omega_h. Then det B_h=Omega_h^n/omega^n=c_h h^n(dV/omega^n).

2. For sigma_T-almost every point, Q=B_h^(1/2)P_T B_h^(1/2) is positive semidefinite. AMGM gives tr(B_h P_T)/n=tr Q/n>=det Q^(1/n)=(det B_h det P_T)^(1/n). No simultaneous diagonalization of B_h and P_T is assumed.

3. Multiplying by sigma_T yields Omega_h wedge T >= c_h^(1/n)h f_0(det P_T)^(1/n)sigma_T=c_h^(1/n)h Gamma_0(T). This is a comparison of measures with respect to sigma_T and is valid on its singular part as well.

4. The factor n in tr P_T=n cancels the factor 1/n in beta wedge T exactly. The inequality has no additional n or factorial.

### 4. thm:gaud-determinant-subcritical — Stokes and positive test functions

**Status: passed.**

1. Distributional integration by parts with smooth global u_h gives integral ddc u_h wedge T=<ddc T,u_h>=0 because X is compact without boundary and ddc T=0. Neither dT=0 nor closedness of omega is needed.

2. Consequently integral Omega_h wedge T=integral omega wedge T=1. Integrating the matrix inequality gives integral h dGamma_0(T)<=c_h^(-1/n)<=c_p^(-1/n)||h||_(np).

3. For nonnegative continuous h, choose smooth approximations converging uniformly and add a positive error offset so all approximants are strictly positive. Uniform convergence gives convergence of their integrals against finite Gamma_0(T) and of their L^(np)(dV) norms.

4. For an arbitrary real or complex continuous h, positivity gives |integral h dGamma_0(T)|<=integral |h|dGamma_0(T)<=c_p^(-1/n)||h||_(np); |h| is continuous and its bound has already been obtained.

### 5. thm:gaud-determinant-subcritical — Lp duality and exponent range

**Status: passed.**

1. Set r=np. Because n>=2 and p>1, 1<r<infinity; continuous functions are dense in L^r(dV). The measure functional extends uniquely to a bounded linear functional on L^r of norm at most c_p^(-1/n).

2. Standard L^r duality represents it by k_T in L^(r/(r-1))(dV). Equality of the functionals on all continuous functions identifies the finite Borel measures Gamma_0(T) and k_T dV; positivity implies k_T>=0 almost everywhere.

3. The dual exponent is q=np/(np-1). It decreases from n/(n-1) to 1 as p increases from 1 to infinity, with neither endpoint attained. Conversely p=q/(n(q-1))>1 exactly when 1<q<n/(n-1).

4. For prescribed q take C_q=c_(q/[n(q-1)])^(-1/n). The Radon-Nikodym density is unique, so the assertions for different p concern the same k_T. All constants are uniform over normalized currents.

5. Only the accepted smooth solvability, the lower L^p density estimate, the matrix-density definition, and ddc-closed trace normalization were used. BMP, positive lower volume, and compact duality are unnecessary.

### 6. Paragraph following thm:gaud-determinant-subcritical — singular trace part

**Status: passed.**

1. Choose a dV-null Borel set N supporting sigma_(T,s). Absolute continuity of Gamma_0(T) gives Gamma_0(T)(N)=0.

2. The density of Gamma_0(T) relative to sigma_(T,s) on N is the nonnegative function f_0(det P_T)^(1/n). Since f_0 is strictly positive everywhere, det P_T=0 sigma_(T,s)-almost everywhere.

3. Rank deficiency of P_T does not imply P_T=0; tr P_T=n. This does not remove the singular part of T or assert integrability of its unweighted coefficients.

### 7. thm:gaud-determinant-endpoint — upper bound

**Status: passed.**

1. The lower volume is nonnegative and finite: the zero potential is an admissible test, so v_minus<=integral omega^n<infinity. First assume v_minus>0.

2. Each smooth strictly positive Omega_h=omega+ddc u_h is an admissible test for v_minus, whence c_h integral h^n dV=integral Omega_h^n>=v_minus.

3. Thus c_h^(-1/n)<=v_minus^(-1/n)(integral h^n dV)^(1/n). The already established matrix inequality and Stokes imply integral h dGamma_0(T)<=v_minus^(-1/n)||h||_n.

4. The same uniform approximation, positivity and continuous-function density argument extends this estimate to a bounded functional on L^n(dV). Its representing density is the previously identified k_T, in L^(n/(n-1)) with norm at most v_minus^(-1/n).

5. All normalized ddc-closed positive currents are covered. This endpoint argument uses PVP and does not take an unjustified limit of the lower density constants c_p as p decreases to 1.

### 8. thm:gaud-determinant-endpoint — smooth conformal Gauduchon test

**Status: passed.**

1. Take any smooth strictly positive g with integral g dV=1. The accepted smooth equation gives Omega_g=omega+ddc u_g>0 and c(g)>0 with Omega_g^n=c(g)g dV.

2. The classical smooth Gauduchon conformal theorem applies to the Hermitian metric Omega_g on compact X of dimension n>=2: choose eta_g=e^phi Omega_g with ddc eta_g^(n-1)=0. Its existence, the only additional geometric standard fact here, is queued for reference verification.

3. Set Z_g=integral omega wedge eta_g^(n-1)>0 and T_g=eta_g^(n-1)/Z_g=a_g Omega_g^(n-1), where a_g=e^((n-1)phi)/Z_g is smooth and strictly positive. Then T_g is smooth strictly positive, ddc-closed and integral omega wedge T_g=1.

4. Since Omega_g-omega=ddc u_g, distributional Stokes gives integral Omega_g wedge T_g=1. Normalizing by the omega trace rather than by volume therefore supplies exactly the required integral.

**Final reference status:** the conformal existence theorem was subsequently matched and checked; see the reference section below.

### 9. thm:gaud-determinant-endpoint — equality and endpoint dual test

**Status: passed.**

1. Let B_g be the positive omega-unitary matrix of Omega_g. For T_g=a_g Omega_g^(n-1), the mixed wedge identity gives beta wedge T_g=(a_g/n)tr(B_g^(-1)B_beta)Omega_g^n.

2. Hence sigma_(T_g)=(a_g/n)tr(B_g^(-1))Omega_g^n and P_(T_g)=n B_g^(-1)/tr(B_g^(-1)). In particular tr P_(T_g)=n, and B_g^(1/2)P_(T_g)B_g^(1/2)=[n/tr(B_g^(-1))]I. This is precisely the equality condition in the earlier matrix AMGM.

3. Consequently c(g)^(1/n)g^(1/n)Gamma_0(T_g)=Omega_g wedge T_g as measures. Equivalently Gamma_0(T_g)=a_g c(g)^((n-1)/n)g^((n-1)/n)dV, which directly confirms the power and normalization.

4. Integration and integral Omega_g wedge T_g=1 give integral g^(1/n)dGamma_0(T_g)=c(g)^(-1/n). No pointwise constancy of a_g is assumed or needed.

5. ||g^(1/n)||_n=(integral g dV)^(1/n)=1. Holder with conjugate exponents n and n/(n-1) gives ||k_(T_g)||_(n/(n-1))>=c(g)^(-1/n). Each such k_(T_g) is smooth and individually has finite endpoint norm.

### 10. thm:gaud-determinant-endpoint — sharpness, zero lower volume and equivalence

**Status: passed.**

1. The explicitly accepted mass-extrema theorem identifies inf c(g) over all smooth strictly positive probability densities with v_minus. It applies to exactly the scalar c(g) in Omega_g^n=c(g)g dV.

2. Let S_sm be the endpoint-norm supremum over smooth strictly positive normalized Gauduchon forms and S_all the supremum over all normalized currents. Then S_all>=S_sm>=sup_g c(g)^(-1/n).

3. If v_minus>0, monotonic continuity of t^(-1/n) gives sup_g c(g)^(-1/n)=v_minus^(-1/n), and the upper bound gives S_all<=v_minus^(-1/n). Thus both suprema equal the claimed value.

4. If v_minus=0, there are smooth positive probability densities with c(g) arbitrarily small, so S_sm=+infinity and hence S_all=+infinity. This conclusion does not assert that any individual smooth current has infinite norm.

5. A finite uniform endpoint estimate is therefore equivalent to v_minus>0. No BMP or upper-volume bound is invoked.

### 11. Paragraph following thm:gaud-determinant-endpoint — change of volume measure

**Status: passed.**

1. For another smooth strictly positive probability volume dV'=rho dV, the trace measure sigma_T and coefficient matrix P_T are unchanged, while f_0'=rho^(1/n)f_0. Therefore Gamma_0'(T)=rho^(1/n)Gamma_0(T) and k_T'=rho^(-(n-1)/n)k_T.

2. At q_*=n/(n-1), integral |k_T'|^q_* dV'=integral |k_T|^q_* rho^[1-q_*(n-1)/n]dV=integral |k_T|^q_*dV. Thus even each individual endpoint norm is invariant, including extended infinite values.

3. For subcritical q the exponent 1-q(n-1)/n is positive rather than zero, so such norm invariance is not claimed and constants may depend on dV.

4. Nothing in the proof identifies v_minus with v_plus. The universal bound on the trace mass is the normalization integral omega wedge T=1, distinct from BMP for nonlinear Monge-Ampere masses.

### 12. cor:gaud-adjoint-lq — representation and uniform bound

**Status: passed.**

1. This corollary alone uses the user-accepted representation A_0(F)={e^(F/n)Gamma_0(T)/M(F): T maximizes}, with M(F)>=exp(-||F||_infinity/n)M(0)>0.

2. For ||F||_infinity<=R the representation and the subcritical theorem give nu=a dV with a=e^(F/n)k_T/M(F)>=0. The maximizing current belongs to the same normalized class to which the determinant estimates apply.

3. Multiplication by e^(F/n) has L^q operator norm at most e^(R/n), while M(F)^(-1)<=e^(R/n)M(0)^(-1). Therefore ||a||_q<=e^(2R/n)M(0)^(-1)C_q.

4. If v_minus>0 the identical calculation holds at q=n/(n-1) with C_q=v_minus^(-1/n). No finite endpoint bound is asserted when v_minus=0.

5. At initial audit-status inspection, results/weak_gauduchon_duality_01/verification.json was absent and its verification_reports channel was empty. The deduction is consequently verified relative to the explicitly accepted representation and positive M(0); it is not an independent certification of the concurrent duality theorem.

**Final dependency status:** the initial pending-audit note above is superseded. [weak_gauduchon_duality_01](../weak_gauduchon_duality_01/verification.json) completed with verdict correct during this run. The corollary still uses exactly the representation accepted by the user.

### 13. Final Hopf threefold example — normalization, density and attainment

**Status: passed.**

1. Use exactly the accepted Hopf data: n=3, integral omega^3=6, ddc omega^2=0, v_minus=6, v_plus=+infinity.

2. dV=omega^3/6 is a smooth strictly positive probability volume. T_0=omega^2/6 is smooth strictly positive, ddc-closed, and integral omega wedge T_0=1. Thus sigma_(T_0)=omega wedge T_0=dV.

3. For any smooth (1,1)-form beta represented by B in an omega-unitary frame, beta wedge omega^2=(tr B/3)omega^3. Hence beta wedge T_0=(tr B/3)sigma_(T_0), so the stipulated convention gives P_(T_0)=I with trace 3 and determinant 1.

4. f_0=(dV/omega^3)^(1/3)=6^(-1/3); consequently Gamma_0(T_0)=6^(-1/3)dV and k_(T_0)=6^(-1/3). Since dV(X)=1, its L^(3/2) norm is exactly 6^(-1/3).

5. The endpoint theorem gives the same supremum v_minus^(-1/3)=6^(-1/3), so T_0 attains it. This is consistent with v_plus=+infinity and directly exhibits an endpoint determinant estimate without BMP.

### 14. Full-proof dependency and scope audit

**Status: passed.**

1. The proof has been verified sequentially through the last paragraph. The subcritical and endpoint determinant theorems and singular-trace consequence use no compact-duality or adjoint theorem.

2. The lower density estimate is used for the subcritical constants; the definition of v_minus for the positive endpoint upper bound; mass-extrema equality for sharpness and the v_minus=0 case; the Gauduchon conformal theorem for smooth equality tests; and the stated representation only for the adjoint corollary.

3. Compactness supports boundedness of smooth potentials, distributional Stokes, positive finite normalizing integrals and continuous-to-Lp approximation. Strict positivity of dV and omega gives the everywhere positive f_0 used on the singular trace part.

4. The accepted Hopf values and ddc omega^2=0 are used only in the example. No unused hypothesis hides a missing BMP step: BMP is expressly unnecessary, and PVP is introduced exactly where a finite endpoint constant is asserted.

5. All absolute continuity and Lq conclusions concern determinant-weighted measures and adjoint measures. No density or nonlinear product is assigned to the unweighted current.

## Reference checks

### R1. Supplied proof — citation inventory and accepted internal inputs

**Status: passed.**

- **eq:weak-gaud-functional at F=0:** Gamma_0(T)=(dV/omega^n)^(1/n)(det P_T)^(1/n)sigma_T; sigma_T=omega wedge T probability, tr P_T=n, beta wedge T=tr(BP_T)sigma_T/n. Application: The exact matrix-density definition is used throughout, including on singular trace parts.

- **Smooth Hermitian equation:** For each smooth strictly positive density there is a smooth positive Omega=omega+ddc u and a positive scalar c solving Omega^n=c times that density. Application: Applied to h^n and to probability density g; the rescaling for nonnormalized h^n is explicit in statement record 2.

- **thm:lp-potential-estimate:** For each p>1 there is c_p>0 such that any bounded omega-psh solution MAu=F dV satisfies ||F||_p>=c_p. Application: Smooth u_h is bounded, F=c_hh^n; no dependence on h or T is introduced into c_p.

- **thm:gaud-volume-mass-extrema:** inf c(g) over smooth strictly positive probability densities equals v_minus(omega), without BMP. Application: Exactly this infimum supplies the sharp endpoint lower bound, including the zero-infimum case.

- **chap:hopf:** n=3; v_minus=6; v_plus=+infinity; integral omega^3=6; ddc omega^2=0. Application: All factors in dV, T_0, P_(T_0), and its density were calculated directly.

**Reason:** These are internal manuscript inputs explicitly accepted by the user, not unverified external-paper citations. They are not re-proved or replaced with unrelated search results.

### R2. thm:gaud-determinant-endpoint — existence of a conformal smooth Gauduchon metric

**Status: passed.**

**Referenced statement:** On a compact complex manifold of complex dimension n>=2, each smooth Hermitian metric Omega has a smooth positive conformal representative eta=e^phi Omega satisfying ddc(eta^(n-1))=0, unique up to positive scaling.

**Arxiv query:** On a compact complex manifold X of complex dimension n >= 2, every smooth Hermitian metric Omega is conformal to a smooth Gauduchon metric eta = exp(phi) Omega satisfying ddc(eta^(n-1)) = 0; the conformal representative is unique up to a positive constant.

**Arxiv results assessment:** The five theorem hits concerned variational critical points, constant Bismut scalar curvature, LCP metrics, prescribed Chern scalar curvature, and distinguished metrics. None stated the required general conformal existence theorem, so no hit was accepted just for containing the word Gauduchon.

**Context expansion:** Both research papers identify the smooth Gauduchon condition as ddc of the (n-1)st power equal to zero and state conformal existence on compact complex manifolds. Pan writes eta^(n-1)=rho Omega^(n-1), so rho=e^((n-1)phi). A nonzero constant change in the ddc convention does not alter this zero equation. Only the smooth theorem is used here; no singular-space extension, balanced condition, or special scalar curvature is required.

**Downstream application:** Apply the theorem to the smooth positive Omega_g. Dividing eta_g^(n-1) by its strictly positive omega-trace integral preserves ddc-closedness and positivity. The resulting a_g Omega_g^(n-1) satisfies the precise matrix AMGM equality condition, as calculated in statement records 8 and 9.

- [Chung-Ming Pan, Singular Gauduchon metrics, introduction](https://arxiv.org/pdf/2106.06259) — Page 1, introduction; page 4, ddc convention

- [Liviu Ornea and Misha Verbitsky, The Lee-Gauduchon cone on complex manifolds, Definition 2.11 and Remark 2.12](https://arxiv.org/html/2411.05595v2#S2.SS4)

### R3. cor:gaud-adjoint-lq — thm:gaud-current-all-adjoints

**Status: passed.**

**Referenced statement:** A_0(F)={e^(F/n)Gamma_0(T)/M(F): T maximizes}; M(F)>=e^(-||F||_infinity/n)M(0)>0.

**Context expansion:** The representation uses the same trace-normalized positive ddc-closed currents and the same determinant-weighted Gamma_0, with exponential weight e^(F/n). It applies to every adjoint measure for real continuous F. This theorem is accepted by the user for the corollary only.

**Downstream application:** The multiplier and denominator bounds each contribute e^(R/n); together they give e^(2R/n)M(0)^(-1) times the determinant-density bound. No claim about the unweighted current is needed.

**Initial status:** Absent at initial inspection; the local corollary was initially treated as relative.

**Final status:** The separate audit completed during this run. Its persisted final verdict is correct with empty critical_errors and gaps, under its stated accepted inputs and inherited connected compact setting.

**Scope:** The determinant theorems are independent of this separate result. The corollary is verified under the accepted representation; there is no remaining incomplete-audit proviso.

**Local evidence:** `results/weak_gauduchon_duality_01/verification.json`

### R4. Standard linear and measure-theoretic facts

**Status: passed.**

**Reason:** These are standard facts, with no external-paper citation; the user expressly permits Radon-Nikodym and Lp duality.

- AMGM applied to B^(1/2)PB^(1/2) gives exactly the needed trace, determinant, and equality factors.

- Distributional Stokes requires smooth u and ddc T=0 on compact X without boundary.

- For 1<r<infinity, density of continuous functions and Lr duality represent the bounded measure functional by an L^(r/(r-1)) density.

- Lebesgue decomposition and positivity force the determinant multiplier to vanish on the singular trace component.

## Findings and strict verdict

- Critical errors: none.
- Gaps: none.
- Verdict: `correct`.
- Repair hints: empty, as required for a correct verdict.

## Persistence

- Final JSON: `results/gauduchon_determinant_integrability_01/verification.json`.
- Full statement checks: `memory/gauduchon_determinant_integrability_01/statement_checks.jsonl`.
- Full reference checks: `memory/gauduchon_determinant_integrability_01/reference_checks.jsonl`.
- Run events and final report are retained in the corresponding memory channels.
