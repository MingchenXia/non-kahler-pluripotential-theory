# Bounded verification request: Hopf normalization for Lp densities

Run the verification_agent for the statement and complete proof below, using fresh run_id `hopf_lp_normalization_01`. This is one bounded check. Inspect every inference, the numerical constants, the almost-everywhere descent and the passage of the cube identity to bounded potentials. The four internal inputs below are accepted established results in the book. Check the deductions from them, rather than re-proving them or replacing the task by literature search. Do not claim novelty. Preserve all historical verifier output and memory.

## Accepted internal inputs

1. For any connected compact Hermitian manifold (Y,h), any smooth positive volume dV and any nonnegative nonzero f in Lp(Y,dV), p>1, there is a continuous h-psh u and a scalar c>0 solving (h+ddc u)^n=c f dV. The scalar c is unique among such continuous solutions; potential uniqueness is not asserted. This applies in particular to (P2,omega_FS).
2. Bounded h-psh potentials on a compact Hermitian manifold have uniformly bounded smooth strictly h-psh decreasing approximations. Bounded Bedford–Taylor products are continuous under those decreasing approximations, and are natural under biholomorphisms. These statements also apply to the Kahler base; Stokes therefore gives integral_P2(omega_FS+ddc q)^2=1 for any bounded omega_FS-psh q when integral omega_FS^2=1.
3. Fixed Hopf geometry: dd c=i partial barpartial/(2pi), X=(C3\{0})/<z->e^-1 z>, pi:X->P2, alpha=pi^*omega_FS, beta=(i/(2pi))partial s wedge barpartial s for s=log|z|^2 on the cover, omega=alpha+beta>0, alpha^3=beta^2=0, integral_X omega^3=6. The compact elliptic group E=C/(Z+2pi i Z) acts by tau_a[z]=[e^a z], preserving omega and acting transitively on each pi-fiber. The probability nu=omega^3/6 disintegrates as normalized Haar area dA_E times omega_FS^2. In a holomorphic trivialization with w=log z0, beta restricts to 2dA_E on the fiber. For any smooth real q on the base, omega+ddc(pi^*q)=pi^*(omega_FS+ddc q)+beta; positivity of the base form implies positivity of the total form, and its cube is 3pi^*(omega_FS+ddc q)^2 wedge beta.
4. For every bounded omega-psh u on X, its Haar average Au(p)=integral_E u(tau_a p)dA_E(a) is the pullback of a bounded omega_FS-psh function, and

       ||u-Au||_L2(nu)^2 <= (2/3)( integral_X omega_u^3 - 6 ).

   Moreover integral_X omega_u^3=6 iff u is the pullback of a bounded omega_FS-psh function. In particular every bounded potential has mass at least6.

## Proposed proposition

Let p>1 and f in Lp(X,nu) be nonnegative and not zero. Let c_f>0 be the unique normalization scalar for continuous solutions of

       omega_u^3 = c_f f omega^3.

Put I_f=integral_X f dnu. Then c_f I_f>=1, and every continuous solution u satisfies

       ||u-Au||_L2(nu)^2 <=4(c_f I_f-1).

Equality c_f I_f=1 holds iff f=pi^*g nu-almost everywhere for some nonnegative g in Lp(P2,omega_FS^2). In this case every continuous solution is the pullback of a continuous omega_FS-psh base potential. There is no assumption that f is strictly positive, continuous or bounded. No uniform upper-mass property on X is assumed. No conclusion for unbounded solutions or for L1 densities is asserted.

## Complete proof

Input1 supplies c_f and a continuous solution, since omega^3=6nu. Integrating the equation gives integral_X omega_u^3=6c_f I_f. Input4 gives c_f I_f>=1 and the displayed inequality, with coefficient (2/3)*6=4. The inequality holds for each continuous solution, independently of any choice of additive normalization.

Suppose c_f I_f=1. Input4 implies u=pi^*q for a bounded omega_FS-psh q. Because pi has local holomorphic sections and u is continuous, q is continuous. Thus tau_a^*u=u for every a in E. Naturality of bounded products and invariance of omega imply tau_a^*(f nu)=f nu for every fixed a. This implication is an equality of measures and does not require choosing one common pointwise representative of f for all a.

For f in Lp(X,nu), its fiber average Af is defined almost everywhere by the Haar integral; choose any measurable representative. Fubini and the disintegration give an almost-everywhere defined measurable function g on P2 with Af=pi^*g. Changes of local trivialization translate the Haar variable, so the definitions agree almost everywhere. Jensen gives integral_P2 |g|^p omega_FS^2 <= integral_X |f|^p dnu. Also g>=0 and integral g omega_FS^2=I_f>0.

For every continuous real test function phi and each a in E, measure invariance gives integral_X phi f dnu = integral_X (phi circ tau_a) f dnu. Averaging this identity in a, using Fubini and changing a to -a, gives integral_X phi f dnu = integral_X phi Af dnu. Hence f=Af=pi^*g almost everywhere. This proves necessity, including the assertion for every continuous solution.

Conversely suppose f=pi^*g almost everywhere with g nonnegative Lp on the base. Then I_f=integral_P2 g omega_FS^2>0. By input1 on the base there is a continuous omega_FS-psh q and k>0 such that

       (omega_FS+ddc q)^2 = k g omega_FS^2.

Input2 and Stokes give k I_f=1. Put u=pi^*q. To check its equation with bounded products, choose smooth strictly omega_FS-psh q_j decreasing to q as in input2. Their pullbacks are uniformly bounded, strictly omega-psh and decrease to u. For each j, input3 gives

       omega_(pi^*q_j)^3 =3 pi^*(omega_FS+ddc q_j)^2 wedge beta.

In a local holomorphic trivialization, the right side is precisely 6dA_E times the base measure (omega_FS+ddc q_j)^2: all horizontal terms of beta vanish when wedged with a base top-degree form, and its vertical restriction is 2dA_E. Bounded product continuity on the base gives weak convergence of these base measures. Testing on a trivialization and using a partition of unity shows that their products with the smooth Haar fiber measure converge to 6dA_E times (omega_FS+ddc q)^2. Bounded product continuity on X identifies the other limit with omega_u^3. Therefore

       omega_u^3=6dA_E (g/I_f)omega_FS^2=(f/I_f)omega^3.

This is a continuous solution with scalar I_f^-1. Scalar uniqueness in input1 gives c_f=I_f^-1, so equality holds. Finally any continuous solution has mass6 and is a base pullback by input4; its base potential is continuous by local sections, as above. All assertions follow.

This is the weak-density counterpart of the book's existing smooth Hopf normalization proposition. It does not assert an identity for weak vertical energy, potential uniqueness, a quantitative estimate on the density's distance from pullbacks, or novelty.
