# Gauduchon, products, and equations audit

Date: 14 September 2026. This is a mathematical audit record, not a formal proof certificate.

## Independent Rethlas checks completed

- `research/rethlas/verification/results/primitive_criterion_01/verification.json`: correct; 34 deductions checked, including signs, formal adjoint, complex test jets, exterior polarization, and small cutoff Hessians. Incorporated as the raw primitive criterion in the energy chapter. The main agent also read the proof and checked the argument directly.
- `research/rethlas/verification/results/infinite_mass_01/verification.json`: correct CONDITIONAL ON inputs B (bounded products), K (normalized L1 compactness), E (uniform small exponential integrability). 52 deductions in 16 items checked. This is not independent verification of B/K/E. Incorporated as the infinite extended-mass construction and its scaling corollary.

Both jobs completed with exit status 0. The second encountered permission-review timeouts while recording memory, retried and completed; it did not report a mathematical error or leave an approval block. The original Rethlas installation was unchanged.

## External inputs used in the manuscript

- Gauduchon conformal theorem: TW10 v2, immediately preceding Lemma 2.3. Multiplier rho makes rho eta^(n-1) ddc-closed. Existence is imported; trace and Fredholm consequences are proved.
- Generalized Lamari criterion: BGL25 PUBLISHED PDF, Lemma 1.15, before BMP is imposed. Non-closed theta is permitted. Positive (n-1,n-1) root converts the stated test to Gauduchon metrics.
- Smooth MA existence: TW10 Corollary 1, without BMP. Their i partial bar-partial convention requires u=2pi phi. Uniqueness is proved independently by extrema and a linearized maximum principle.
- Gauduchon prescribed volume: STW17 v2, Theorem 1.4. Background gamma is Gauduchon, gamma0 is Hermitian, and uniqueness is within the scalar ansatz. The first-order term is Re(i/(2pi) partial u wedge bar-partial gamma^(n-2)). Its Aeppli-exact expression has coefficient i/(4pi).
- Bounded local products: SGPT local BT input; KN15 Section 1 and BGL25 Section 2.1 for non-closed expansion. Positivity proved by local freezing with 2 epsilon correction. Difference of alternative potential decompositions is smooth by local elliptic regularity.
- Smooth approximation of bounded omega-psh functions: BGL25 Definition 1.16 and following paragraph. This supplies equality of bounded and smooth upper-mass suprema. It does not supply arbitrary non-semipositive theta truncations.
- Normalized L1 bound: Dinew16 Proposition 6.2. The earlier ledger confused this single-author 2016 survey with Dinew--Kolodziej's 2012 paper; corrected in the updated ledger.
- Qualitative local Skoda integrability: Zeriahi01 Section 1, printed pp. 672-673, read in full text uploaded by the author. Local corrections and a finite cover give a small exponent for each qpsh function on compact X. The manuscript proves uniformity via a separate series argument. This proof has primary-agent review only, not an independent Rethlas verdict yet.
- Continuous MA existence: KN15 v2 Theorem 0.1. No BMP/PVP, f>=0 in Lp p>1 nonzero, continuous u and positive c. No potential-uniqueness assertion added.
- Exponential existence: Nguyen16 (local filename), arXiv1501.00891v1, Theorem 0.1. Reference ddc is twice ours: u=2phi and reference lambda=2lambda. Smoothness is NOT inferred from continuous existence.
- Modified comparison: KN15 Theorem 0.2; constants absorb operator normalization. Thickness s<epsilon^3/B and multiplicative error Cs/epsilon^n retained.
- Exponential density order: Nguyen Lemma 2.3. Direct reference normalization uses metric 2lambda omega and potentials lambda a, lambda b; densities scale by (2lambda)^n relative to dV. The barrier proof gives uniform lambda u_lambda -> log c and uniqueness of c, without proving uniqueness of the lambda=0 potential.

## Primary-agent direct checks

- The Gauduchon trace identity is distributional, so unbounded potentials are permitted without defining their nonlinear products.
- The adjoint probability density is rho_u omega_u^n, NOT the unweighted volume of an arbitrary solution metric. Fredholm index zero and maximum principle yield the range condition.
- Second derivative of log determinant gives b''=-integral F''dmu-integral tr(A^2)dmu; no differentiation of the parameter-dependent measure is needed. Strictness along affine data is modulo constant density changes. Smooth dependence uses a linear mean-zero normalization, not differentiability of sup u.
- Strictly positive mass for each fixed bounded potential follows from modified comparison with v=0 and a nonempty ordinary open strict sublevel set. This is weaker than a uniform positive lower-volume bound.
- Extended NPP measures can have infinite total mass and then are not Radon measures on compact X. The construction never treats them as globally finite currents.
- Infinite-mass witness: on D_t, v_j=U-a_j u_j>=U>-t. This common set is essential for the bounded comparison. The pole set has zero measure for each smooth omega_uj^n.
- Uniform exponent lemma: failure at exponents a_j/j yields a convergent negative qpsh series V with exp(-pV) nonintegrable for every p>0, contradicting qualitative Skoda. The final witness uses a separate Jensen tail argument to give integrability for every exponent.

## Still outstanding

Independent review of the additional uniform-exponent lemma, Gauduchon parameter derivatives, and weak barrier argument; detailed reconstruction of the imported PDE a priori estimates; full source proof audit of XZ26; all relative model/full-mass definitions and original SGPT I-goodness implications. No full-book correctness or completeness claim is made.
