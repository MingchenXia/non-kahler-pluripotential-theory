Run_id: curve_atomic_source_topology_01

Run scope: Bounded verification through the normal Rethlas workflow. The parent owns manuscript edits, build and release. Restrict writes to normal verifier tools, memory and results. Do not alter book/editorial/blueprint/status/changelog files, frozen inputs, original references or historical reports. Do not commit or push.

Statement: Check the lemma, theorem and corollary below, including the non-total-boundedness observation. They identify the source singularity metric topology on positive-mass ideal envelopes on a compact curve with total variation of the purely atomic Lelong data. This is a deduction from the original book's metric inequalities and earlier local ideal/envelope inputs, not a new construction of d_S on a general Hermitian manifold and not a novelty claim. No Popovici result is used.

Accepted inputs: The compact-curve Green kernel, distributional Stokes, positivity and atom/Lelong identity, local bounded quasi-subharmonic functions have nonpolar curvature, and normalized potential compactness. The Green kernel G(x,p) for eta=theta/A, where A=integral theta, may be chosen nonpositive, satisfies dd^c_x G=delta_p-eta, and has uniformly bounded L1 norm in p. For every finite positive purely atomic measure D, w_D=integral G(x,p) dD(p) is a genuine quasi-psh function with dd^c w_D=D-D(Y)eta. The local ideal criterion says that on a smooth curve equality of multiplier ideals at all positive weights is equivalent to equality of point Lelong numbers. The ideal envelope P_theta[u]_I retains those ideals, is normalized with supremum zero, is idempotent, and dominates u-sup u. A global L1 distribution whose dd^c is bounded below by a smooth form has a quasi-psh representative. Almost-everywhere inequalities between canonical quasi-psh functions hold everywhere. These are established earlier book results.

Source metric inputs: The source SGPT pseudometric d_{S,theta} on potentials in a fixed closed positive background has the triangle inequality, vanishes on ordinary-equivalent potentials, and satisfies the following two formulas. Write u vee v=max(u,v). For u<=v on a curve,

d_S(u,v)= ( MA_theta(v)(Y)-MA_theta(u)(Y) )/2.

For u,v and z=max(u,v),

d_S(u,v) <= d_S(u,z)+d_S(v,z) <= 48 d_S(u,v).

The first is the n=1 case of lma:varphileqpsi_metric in the original supplied SGPT source author/chapter_comp.tex:764–783. The second is lma:dSalmostriang there, lines695–737, with C_n=3(n+1)2^(n+2), hence C_1=48. Both statements and adjacent proofs have been read directly by the parent. Use these as source-book inputs, not a result to reconstruct from ray geometry. All potentials to which these are applied below have strictly positive non-pluripolar mass. Invariance under addition of constants is included in ordinary equivalence.

Conventions: Y is a compact connected Riemann surface; theta is smooth strictly positive, A=integral_Y theta>0, eta=theta/A. d^c=i/(4*pi)(bar-partial minus partial). A positive purely atomic measure D means a countable sum of nonnegative Dirac masses with finite total mass. Total variation norm means |D-E|(Y), not half of that quantity.

Lemma. For every positive purely atomic D with D(Y)<A, let w_D=integral G dD and q_D=P_theta[w_D]_I. Then w_D is theta-psh, q_D is ordinarily equivalent to w_D, and

MA_theta(w_D)(Y)=MA_theta(q_D)(Y)=A-D(Y).

Moreover D->q_D is a bijection from {positive purely atomic D: D(Y)<A} to the normalized ideal envelopes having positive non-pluripolar mass. Under this map D is exactly the atomic part of theta+dd^c q_D.

Proof. The curvature identity gives theta+dd^c w_D=D+(A-D(Y))eta>=0. Every atom of D is a pole of w_D. The smooth measure eta charges no polar set, so deleting the polar part of this curvature gives MA_theta(w_D)=(A-D(Y))eta.

Put q=q_D. Ideal projection makes each Lelong number of q equal to the corresponding atom of D. Thus theta+dd^c q-D is a positive measure: deleting all atoms of a positive measure leaves a positive measure, even with countably many atoms. Consequently as distributions

dd^c(q-w_D)=(theta+dd^c q-D)-(A-D(Y))eta >= -(A-D(Y))eta.

So q-w_D has a global quasi-psh representative, which is bounded above on compact Y. The envelope inequality q>=w_D-sup w_D bounds the same difference below almost everywhere. The representative is therefore bounded above and below. This proves ordinary equivalence, interpreting the difference first as an L1 distribution and then extending the comparison by canonical representatives.

Let b=q-w_D be this bounded quasi-psh representative. The measure (A-D(Y))eta+dd^c b is positive, by the displayed inequality, and puts no mass on polar sets by local boundedness after a smooth correction. Hence theta+dd^c q=D+((A-D(Y))eta+dd^c b) has polar part exactly D, proving the mass formula and the atomic assertion without needing a nonlinear bounded-change theorem.

For the bijection, the point Lelong numbers of any theta-psh u define an atomic measure D_u with D_u(Y)<=A. If D_u(Y)<A, the curve ideal criterion gives u ideal-equivalent to w_Du, hence P_theta[u]_I=q_Du. If D_u(Y)=A, the full curvature theta+dd^c u already equals D_u because its mass is A; its non-pluripolar mass is zero. This also applies to ideal envelopes, so every positive-mass ideal envelope has D_u(Y)<A and is in the indicated range. Conversely every D in that range yields a normalized ideal envelope of positive mass. Distinct D give distinct point Lelong data, proving injectivity.

Theorem. For positive purely atomic measures D,E with masses less than A,

(1/96) ||D-E||_TV <= d_{S,theta}(q_D,q_E) <= (1/2) ||D-E||_TV.

Thus d_S is a metric on these canonical ideal envelopes and induces exactly total-variation convergence of their atomic profiles.

Proof. First suppose D and E have finite support. Use w_D,w_E and put z=max(w_D,w_E). At each point in the union of their supports, the logarithmic coefficient of z is the minimum of the two coefficients (use zero for an absent atom); its local remainder is bounded. Away from this finite set, z is locally bounded. Thus if D wedge E denotes the atomic measure with coefficients min(D{p},E{p}), the non-pluripolar mass of z is A-(D wedge E)(Y). The ordered-distance formula gives

d_S(w_D,z)+d_S(w_E,z)=[D(Y)+E(Y)-2(D wedge E)(Y)]/2=||D-E||_TV/2.

Both source metric inequalities now give the claimed bounds for w_D,w_E. Ordinary equivalence with q_D,q_E transfers them to those envelopes.

For arbitrary countable supports, choose increasing finitely supported restrictions D_m of D and E_m of E whose masses tend to their full masses. Since G<=0, w_D<=w_Dm and w_E<=w_Em. The ordered-distance and mass formulas give exactly

d_S(w_D,w_Dm)=(D-D_m)(Y)/2 ->0,
d_S(w_E,w_Em)=(E-E_m)(Y)/2 ->0.

The triangle inequality shows that d_S(w_Dm,w_Em) tends to d_S(w_D,w_E). The total-variation norms also converge, since D_m->D and E_m->E in total variation. Passing the finite-support inequalities to the limit and using ordinary equivalence proves the theorem. The lower bound plus injectivity of the atomic parametrization proves that this is an actual metric on canonical ideal envelopes. Both bounds give the claimed equivalence of convergence.

Corollary. For every 0<epsilon<A, the space of normalized ideal envelopes q with MA_theta(q)(Y)>=epsilon is complete for d_{S,theta}. Finite-support rational atomic profiles, hence analytic ideal envelopes, are dense in this space. The space is not totally bounded.

Proof. By the lemma it corresponds exactly to the positive purely atomic measures of total mass at most A-epsilon. This is complete for total variation. Indeed a Cauchy sequence of such measures has a finite-measure total-variation limit, which is positive with the same mass bound. The union of their countable supports is countable, and the limit has zero mass off that union, so remains purely atomic. Equivalently this is the closed positive bounded-mass part of l1 of that countable union. By the two metric inequalities, a d_S Cauchy sequence of envelopes gives a total-variation Cauchy sequence of profiles; its limit profile maps to a d_S limit in the same space. This proves completeness.

Finite truncation followed by approximation of the remaining finitely many coefficients by nonnegative rationals from below preserves the mass upper bound and gives total-variation convergence. The corresponding Green potentials have finitely many rational logarithmic poles, and their ideal envelopes have the same ordinary type, so are analytic in the book's convention. The upper metric bound proves density.

Finally fix 0<a<A-epsilon. The profiles a delta_p, as p ranges over Y, have pairwise total-variation distance 2a. The lower metric bound gives pairwise d_S distance at least a/48. There are infinitely many such profiles, so the space is not totally bounded. No claim is made about arbitrary ordinary singularity types, which need not be represented by their ideal envelopes.

Checks: Verify the countable atomic removal, the bounded global distributional difference, the possible polar set outside the atom support, and the endpoint D(Y)=A used for surjectivity. Check that the bounded remainder of a finite maximum is enough for its mass calculation. Check constants 48 and 96 and the total variation normalization. In the infinite-support step, do not assume that the maximum itself is ordinarily equivalent to the minimum-profile potential; that identification is used only for finite poles, and the general theorem follows by the source-metric triangle inequality and finite tails. Check completeness of atomic measures under total variation, approximation from below at the mass boundary, and that density of all finite rational profiles is not a separability assertion (their support points range over an uncountable curve). No Popovici, capacity-convergence, or general Hermitian metric theorem is involved.
