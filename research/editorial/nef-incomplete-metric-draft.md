# Nef incomplete metric: unverified construction

23 September 2026. Research draft only. Not part of the book, not a proved answer to the nef question, and not a novelty claim. Work was interrupted by the user's new regularity manuscript. The calculations below are preserved for later independent review. Checkpoint88 remains the checked result.

## Surface model

Let Y be the blowup of P² at a point, with beta the pullback of Fubini--Study and gamma the pencil class, using the notation and normalization dd^c=i partial barpartial/(2pi) of Section28.8. The form theta0=A beta is nef, semipositive and big. For the exceptional norm s_E,

    A beta + dd^c(epsilon log s_E)
      = (A-epsilon) beta + epsilon gamma + epsilon [E].

For 0<epsilon<A this is strictly positive. The expected ample locus is Y\E; check the restriction-to-E argument for every strict current smooth at any point of E.

On the affine chart about the blown-up point write r=|z|, R=r², and

    f(r)=-3 log(1-r),  0<=r<r0<1.

As a function of R,

    f_R=3/(2r(1-r)),
    f_R+R f_RR=3/(4r(1-r)²),
    det(f_i barj)=9/(8r²(1-r)³).

Thus (dd^c f)²=9/(4pi²) r^-2 (1-r)^-3 d lambda_z. Choose B>0 and A sufficiently large. A smooth regularized maximum of f(r)+B and A log(1+r²) should equal the first near zero and the second near an outer collar. It gives a global bounded continuous A omega_FS-psh potential chi, smooth off the point. Put rho0=pi*chi and T0=A beta+dd^c rho0. Near E,

    rho0=f(r)+B-A log(1+r²),  T0=dd^c f(r).

In blowup coordinates z=(t,tw), r=|t|sqrt(1+|w|²), define dV0=e^-rho0 T0² off E. The formal expression is

    dV0=9e^-B/(4pi²) (1+r²)^A/(1+|w|²) d lambda_(t,w),

which is smooth and positive across E. Check gluing between charts and in the regularized-maximum region. This would give MA_theta0(rho0)=e^rho0 dV0, with bounded minimal potential, full mass A² and finite energy. The radial length is comparable to integral_0^epsilon r^-1/2/(1-r) dr<infinity. A first-exit argument as in Section28.8 would show incompleteness on every nonempty connected open subset of Y\E.

## Nonempty divisor by a product

On C=P¹, at a=0 put R=|z|², L=-log R and F_c=-2log L near zero. Then

    dd^c F_c=2/(pi R L²) d lambda_z.

This measure is finite, has no atom and has zero Lelong number. Join it by a cutoff to a smooth positive measure away from a; call the result eta and its total mass A_c. A Green potential u solves eta=A_c omega_FS+dd^c u and locally

    u=F_c-A_c log(1+R)+h_c

with h_c smooth harmonic. For s_a=R/(1+R),

    dV_c=e^-u s_a eta=(2/pi)e^-h_c(1+R)^(A_c-1)d lambda_z

extends smoothly and positively. The energy integral near a reduces to integral^infinity log L/L² dL, which is finite.

Set X=Y x C, Theta=pr_Y theta0+pr_C(A_c omega_FS), D=Y x {a}, phi=pr_Y rho0+pr_C u, and dV_X=3dV0 x dV_c. The formal product calculation gives

    MA_Theta(phi)=3 T0² x eta=e^phi |sigma_D|^-2 dV_X.

The anticipated class is nef and big; phi has zero Lelong numbers and lies in E¹, although it is not minimal along D. On (Y\E) x (C\{a}) the metric is smooth positive, and a path in the Y-factor at fixed c!=a has finite length approaching E. Check all mixed energy integrals, non-pluripolar product identities, uniqueness, and the precise scope of DNGL26 Question3.5. No assertion about flow-compatible divisor/class data is intended.

## Pending checks

1. Verify the regularized maximum, its strict positivity away from E and the exact volume constants.
2. Verify full mass and E¹ on the product without silently replacing ordinary minimality by zero Lelong numbers.
3. Check that the stated regular locus is maximal, and justify the every-open-subset completeness conclusion.
4. Compare the result with primary literature before any novelty or problem-resolution statement.
5. Submit the complete proof to independent review before placing a theorem in the book.
