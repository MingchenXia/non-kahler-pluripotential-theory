# Affine envelope slopes and supporting probabilities — review 423

This unit reconstructs the growth-slope estimates, continuous-weight probability representation and attained derivative formula in Nurbek Kh. Narzillaev, *Weighted regularity and plurithinness in C^n*, arXiv:2609.23530v1, Lemma 3.1, Proposition 3.2 and Theorems 3.3–3.4, pp.6–9. It also checks their direct extension from regular points to every fixed affine point and every positive growth parameter. No novelty claim or original open-problem closure is made.

The exact cached 22-page PDF has SHA256 `88fd47ac7cd605b2d796facfc1b316222965ca924e01ba8b8a54db00cfd7fba5`. Complete text pages 6–9 and all four original page images are freshly read. The primary abstract is freshly retrieved and still lists only v1, submitted 20 September 2026; its SHA256 is `c6b6f699e80dff0cb17ee78046d0e483308264fe216ed9288f826218799c6786`. The complete 22-page reading at 413 and selected foundations at 421/422 are inherited only at their recorded scopes. No new broad announcement scan or repair of historical list gaps is claimed.

The current 96-line affine/projective parent and 37-line pole-obstacle input were read completely in the preceding checked unit and are reused here. The first gives genuine finite envelopes, raw/almost-everywhere regularization and growth-parameter concavity; the second gives quasi-everywhere competitor repair within the same growth allowance. The local upper-envelope theorem's pluripolar exceptional set remains an accepted Chapter 1 input. The 421 exact global Josefson dependency review is not enlarged into an independent certification of all cited premises. The supporting-functional argument in Chapter 14, lines 100–144, is additionally read as comparison context; its absolute-continuity conclusion is not imported into the affine problem.

## Fixed compact and slope estimates

Let K be a non-pluripolar compact subset of C^n, psi a bounded real function on K, m=inf_K psi and M=sup_K psi. Use the current book classes L_delta, everywhere-obstacle raw envelopes V_delta and their finite regularizations F_delta. Let g be the regularized unweighted growth-one envelope. Thus g>=0 everywhere, and scaling and obstacle order give

    delta*g+m <= F_delta <= delta*g+M.

Adding an alpha-competitor and (beta-alpha) times an unweighted growth-one competitor gives a beta-competitor. At the raw level, V_beta>=V_alpha+(beta-alpha)*V_1,0. All three raw envelopes agree almost everywhere with their genuine regularizations, so canonical order gives the inequality everywhere. Scaling about m gives the upper inequality. Therefore, for 0<alpha<beta,

    (beta-alpha)*g <= F_beta-F_alpha
                         <= ((beta-alpha)/alpha)*(F_alpha-m).

This proves more than monotonicity and keeps the same factor alpha in the upper bound. Convex combinations give concavity at every affine point, as already checked in the book.

Fix any a in C^n and any tau>0; no regularity assumption is needed for this paragraph. Concavity makes

    q_h(a)=(F_(tau+h)(a)-F_tau(a))/h

nonincreasing in h>0. The two-sided estimate gives g(a)<=q_h(a)<=(F_tau(a)-m)/tau. Consequently the finite right derivative D_tau(a)=lim_(h down to 0)q_h(a) exists, with the same bounds. All later secants lie below D_tau(a).

The obstacle sandwich also gives

    0 <= q_h(a)-g(a) <= (M-m)/h,

for every a in C^n and every h>0, because F_(tau+h)<= (tau+h)*g+M and F_tau>=tau*g+m. Thus the later secants approach the unweighted envelope with a uniform error on the entire affine space. This statement concerns the difference after subtracting g; it does not assert that the separate unbounded functions have finite sup norms or that the initial derivatives converge uniformly in tau.

The initial slope equals g(a) exactly when every later secant equals g(a), equivalently

    F_delta(a)=F_tau(a)+(delta-tau)*g(a) for all delta>=tau.

At a regular contact parameter tau in Lambda_reg(a), with a in K, F_tau(a)=psi(a). Then D_tau(a)=0 is equivalent to persistence of regularity at every later parameter. If D_tau(a)>0, small positive increments have positive defect; monotonicity propagates it to every positive increment. The existing contact-ray theorem implies that tau is the smallest contact parameter in this case. This last threshold assertion retains its global raw-contact hypothesis, even though the derivative and secant estimates themselves hold at arbitrary points and parameters.

## Quasi-everywhere pointwise representation

For continuous f on K, the genuine F_(delta,f) itself satisfies F_(delta,f)<=f quasi-everywhere on K, since regularization changes the raw envelope only on a pluripolar set. Conversely the already proved repair shows that every quasi-everywhere competitor lies below F_(delta,f) everywhere. Hence

    F_(delta,f)(z)=sup{u(z):u in L_delta, u<=f q.e. on K}

at every z, before any additional regularization of the right-hand side. This stronger pointwise statement, rather than equality of regularizations alone, is what the measure proof needs. The obstacle continuity is retained for the Banach-space and weak-compactness arguments below.

Fix any a in C^n. Define J_a(K) as the pairs (mu,c), where mu is a Borel probability measure on K and c>=0, such that

    u(a) <= integral_K f dmu + c

whenever u is in L_1, f is continuous real-valued on K and u<=f quasi-everywhere there. These inequalities integrate only continuous tests f, so no integral of an unbounded pole function is introduced.

Put T(f)=F_(1,f)(a) on the real Banach space C(K). It is finite, monotone, concave, satisfies T(f+t)=T(f)+t and is 1-Lipschitz in the uniform norm. For any f0, the Hahn–Banach supporting-functional construction gives a continuous linear ell with

    T(f)<=T(f0)+ell(f-f0).

For completeness the usual retained functional-analytic step can be reconstructed: the one-sided directional derivative of the convex 1-Lipschitz function -T is finite and sublinear; Hahn–Banach supplies a dominated continuous linear functional, and the monotonicity of convex secants gives its supporting inequality. Changing sign gives ell above. Testing f0+t h with h>=0 proves positivity of ell; testing both signs of a constant gives ell(1)=1. The Riesz representation theorem gives ell(f)=integral f dmu for a probability mu. With c=T(f0)-integral f0 dmu, the support inequality at f=0 gives c>=T(0)=g(a)>=0. The pointwise quasi-everywhere representation proves (mu,c) belongs to J_a(K) and attains the value T(f0).

Conversely any pair in J_a(K), tested against the genuine quasi-everywhere competitor F_(1,f0), gives T(f0)<=integral f0 dmu+c. Scaling then proves, for every continuous q and delta>0,

    F_(delta,q)(a)=min_(mu,c in J_a(K))(integral_K q dmu+delta*c),
    min_(mu,c in J_a(K)) c = g(a).

The minimum is attained, and J_a(K) is nonempty. The extension to a outside K uses exactly the same finite-envelope and support argument; no new local-regularity premise is substituted. Hahn–Banach, Riesz representation and compactness of probabilities on a compact metric space remain named retained functional-analytic inputs, not freshly audited external papers. No absolute continuity or noncharging conclusion about these supporting probabilities follows from this construction.

## Attained right derivative

Now let psi be continuous, fix a in C^n and tau>0, and call a pair active if integral psi dmu+tau*c=F_tau(a). Every active pair satisfies

    0<=c<=(F_tau(a)-m)/tau.

The set J_a(K) is closed in the weak probability topology times the ordinary topology on c, since every defining test f is continuous. Its intersection with any bounded c interval is compact. Active pairs exist by the preceding representation, so the minimum active c is attained.

An active pair gives F_(tau+h)(a)<=F_tau(a)+h*c. Thus D_tau(a)<= every active c. For a minimizing pair (mu_h,c_h) at tau+h, the representation at tau gives c_h<=q_h(a), which uniformly bounds c_h as h decreases to zero. A sequence h_j down to zero has a convergent subsequence of these pairs. Its limit is in J_a(K), is active at tau, and has c<=D_tau(a). The two inequalities prove

    D_tau(a)=min{c:(mu,c) in J_a(K),
                       integral psi dmu+tau*c=F_tau(a)}.

Since every pair has c>=g(a), equality D_tau(a)=g(a) is equivalent to an active pair (mu,g(a)), or integral psi dmu=F_tau(a)-tau*g(a). At a regular contact point this becomes precisely the source's weight-and-unweighted-test criterion with F_tau(a)=psi(a). The statements for bounded weights above are not silently upgraded to this weak probability formula: continuity of psi is used when taking weak limits of its integrals.

## Boundary and continuation

The audit lists 41 direct obligations, including the stronger pointwise quasi-everywhere identity, both directions of support/minimum equality, weak compactness, derivative attainment, the uniform large-increment estimate and the exact scope of the contact-threshold consequence. General product formulas, all-boundary regularity, local thinness characterizations, smooth-weight and chair constructions remain outside this unit. No catalogue closure, manuscript edit, author rebuild, native catalogue call or public publication occurs. All 328 tracked book files, 994 proof bodies, both catalogues, both original manifests and 451 protected files remain exact to the checked 1195-page release 422.

The current package has 2139 archive entries and 2138 checksum-validated payloads. Its 325 book-source files match the actual checkpoint 422 empty-source reconstruction byte for byte; no new source reconstruction is performed for this research-only snapshot.

Next: integrate the growth slopes after the contact-ray theorem, followed by the continuous-weight supporting-measure representation. Preserve bounded versus continuous obstacle hypotheses and use source-accurate attribution in Chapter 33. Complete scoped manuscript rereads, output checks and reconstruction before continuing the remaining research programme.
