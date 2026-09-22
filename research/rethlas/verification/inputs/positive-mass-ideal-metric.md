Run_id: positive_mass_ideal_metric_01

Run scope: Bounded verification through the normal Rethlas workflow. The parent owns manuscript edits, build and release. Restrict writes to normal verifier tools, memory and results. Do not alter book/editorial/blueprint/status/changelog files, frozen inputs, original references or historical reports. Do not commit or push.

Statement: Check the following elementary consequence for the ideal-envelope L1 metric on a compact Riemann surface. The full current converges to the smooth background, but the non-pluripolar measures converge to a fixed smaller multiple of it, although every approximant is an analytic ideal-model potential with the same strictly positive mass. No assertion about capacity convergence, d_S convergence, incompleteness of the positive-mass locus, or novelty is made. No result of Popovici is used.

Conventions and accepted inputs: d^c=i/(4*pi)(bar-partial minus partial); dd^c log|z|^2=delta_0. Y is a compact connected Riemann surface and theta is a smooth strictly positive (1,1)-form with total mass one. PSH(Y,theta) has its canonical upper semicontinuous representatives. The normalized family K_theta={u in PSH(Y,theta):sup_Y u=0} is L1 compact and L1 limits preserve the supremum normalization. Every positive probability measure nu admits a theta-psh Green potential q_nu, unique up to a constant, with theta+dd^c q_nu=nu. For a finitely supported measure, its normalized potential has precisely those logarithmic poles and smooth local remainders. A distribution with dd^c zero on Y is a constant.

For theta-psh u, the ideal envelope P_theta[u]_I is the upper semicontinuous regularized supremum of theta-psh v<=0 with I(lambda v)=I(lambda u) for every lambda>0. The previously proved projection theorem gives P_theta[u]_I ideal-equivalent to u, sup zero, and idempotence. The analytic-envelope theorem gives P_theta[a]_I ordinarily equivalent to a when a has analytic singularities: their difference is locally bounded, including near each logarithmic pole. In particular that envelope retains the same finite pole set, coefficients and analytic type up to a bounded remainder; it is locally bounded away from the pole set. These are accepted earlier book results; check their applicability here, not their full proof. On a curve the Lelong number of u at p equals the atom of theta+dd^c u. The non-pluripolar measure of a potential with only finitely many logarithmic poles is its curvature measure with those atoms removed. A locally bounded potential's curvature has no mass on locally polar sets. Rational logarithmic coefficients give analytic singularities in the source book convention.

The metric is d_I([u],[v])=integral_Y |P_theta[u]_I-P_theta[v]_I| dV, where dV is any fixed smooth positive probability volume. It is finite and well defined by ideal projection. Smooth positive theta implies P_theta[0]_I=0.

Proposition. For every rational tau in (0,1), there is a sequence r_j in K_theta of analytic ideal-model potentials such that

P_theta[r_j]_I=r_j,
r_j -> 0 in L1,
MA_theta(r_j)(Y)=tau for every j,
MA_theta(r_j) -> tau theta weakly.

Consequently d_I([r_j],[0])->0, whereas MA_theta(0)=theta and its mass is one. Thus non-pluripolar mass is not continuous for this metric even on a family with masses bounded below by a fixed positive constant.

Proof. Choose finitely supported probability measures nu_j with positive rational weights converging weakly to theta. For example use finite partitions of arbitrarily small mesh, then approximate their weights by rational probabilities with total variation error tending to zero. Combine repeated support points. Let q_j be the Green potential normalized by sup_Y q_j=0, so theta+dd^c q_j=nu_j. Normalized compactness and the curvature equation show q_j->0 in L1: any subsequential L1 limit q satisfies theta+dd^c q=theta and has supremum zero, hence q=0; compactness upgrades this to whole-sequence convergence.

Put a=1-tau in (0,1) and r_j=P_theta[a q_j]_I. Scaling is admissible in the same background, since

theta+dd^c(a q_j)=(1-a)theta+a nu_j>=0.

The functions a q_j are normalized, have finitely many logarithmic poles with positive rational coefficients, and are below zero. Ideal projection and the analytic-envelope theorem give P_theta[r_j]_I=r_j, sup r_j=0, and r_j ordinarily equivalent to a q_j. Because a q_j is a competitor, a q_j<=r_j<=0. Hence integral |r_j| dV<=a integral |q_j| dV->0.

If nu_j=sum_k b_jk delta_pjk, the exact pole coefficient of r_j at p_jk is a b_jk. The curvature measure theta+dd^c r_j has exactly these atoms at its finite pole set. Elsewhere r_j is locally bounded, so its non-pluripolar measure agrees with its full curvature measure there and has no further removed mass. Therefore as finite Borel measures,

MA_theta(r_j)=theta+dd^c r_j-a nu_j.

Distributional Stokes gives the total mass 1-a=tau. Since r_j->0 in L1, the full curvature currents converge distributionally to theta, and since they are positive measures of fixed mass one, they converge weakly as measures (approximate continuous test functions uniformly by smooth ones). Also nu_j->theta weakly. Subtracting the two limits gives MA_theta(r_j)->(1-a)theta=tau theta. Finally P_theta[0]_I=0 and P_theta[r_j]_I=r_j, so the distance to [0] is the L1 norm of r_j and tends to zero. This proves all assertions.

Checks: Check the normalization, admissibility of a q_j without changing theta, exact atom coefficients after taking the ideal envelope, absence of further lost polar mass, positivity and fixed mass when turning distributional into weak convergence, and the interpretation of the metric on ideal classes. The proof uses analytic-type preservation up to a bounded remainder, not a smooth-remainder theorem. The conclusion is discontinuity, not failure of well-definedness of mass on ideal classes. Do not claim it contradicts the positive-mass d_S theory or proves incompleteness of the uniformly positive-mass locus.
