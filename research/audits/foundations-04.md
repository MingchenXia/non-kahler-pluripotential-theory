# General theory without bounded mass: fourth audit

14 September 2026, ~13:04 UTC. The full twenty-hour book goal remains active and incomplete. This file records mathematical scope and verification limits, not a formal certificate.

## Self-contained foundations added

- The Gauduchon conformal theorem now has a Fredholm/maximum-principle proof. Normalize the adjoint kernel by its nonzero integral, exclude a negative region by solving an impossible strictly positive equation, and handle its arbitrary zeroth-order coefficient by subtracting the positive part before the strong minimum principle.
- The generalized Lamari criterion for arbitrary smooth theta now has a Hahn--Banach proof. The Gauduchon test form is an order unit. The induced sublinear majorant is finite, the positive extension is continuous in the uniform norm, and an explicit scalar elliptic right inverse proves the distributional ddc factorization. No global ddbar lemma is used. Its quantitative positivity threshold is attained by a current, not necessarily by a minimizing smooth test metric.
- Rethlas `gauduchon_duality_01`: correct under the listed standard inputs; 17 sequential records and four source checks, no errors or gaps. It completed with exit0. Historical citations were not used as premises.
- The I-envelope projection, idempotence, ordinary model identity, order/scaling/addition are proved using the local valuative criterion and increasing-limit strong openness already allowed from SGPT. Local modifications are not silently globalized. Finite maxima preserve ideal equivalence by the elementary Lelong identities; Choquet plus one common smooth correction gives the increasing sequence to which strong openness applies. The ordinary P-envelope preserves ideals by the sandwich between u and Q[u]. No BMP or closedness is used.

## Damping and the Gauduchon improvement

- Rethlas `damped_measures_01`: correct conditional on standard local BT inputs1-4, 94 deductions. This checks only the ORIGINAL coarse range exponent n, q>n, capacity exponent1-n/q, and the original damped-continuity proof. Input and report are preserved unchanged.
- Subsequent direct deduction: the local cutoff induction can start at degree1 because the Gauduchon trace bounds the first corrected-Hessian integral uniformly. Thus mixed integrals of j positive factors grow at most as (1+A)^(j-1). The exact top wedge has integral zero, eliminating degree n and giving the total range bound C(1+A)^r for r=max(n-2,0).
- Current manuscript consequences: exponential bound C(1+p^-1)^r; shallow mass C(1+t)^r; polynomial damping q>r; deep-tail bound Cq/(q-r)(1+T)^(r-q); capacity exponent(q-r)/(q+n-r), equal to1-n/(q+2) for n>=2. At capacity delta<=1 use T=delta^(-1/(q+n-r)); T^n delta=T^(r-q). No optimality/novelty assertion.
- Supplemental Rethlas `gauduchon_growth_01` returned correct under its stated standard BT, Gauduchon-trace and earlier damping inputs. It separately checked the exact signed-product cancellation and all substituted exponents, finding no errors or gaps. The earlier damping report still certifies only its own coarse version.

## Arbitrary smooth backgrounds

- Constant truncations are taken in a dominating Hermitian background Omega. The bounded product with the original theta is initially signed.
- On D_t={u>-t}, freeze theta near a point, take r with ddc r=theta'+epsilon kappa, and use h_k=max(u+r,-k)-r for k>t+sup|r|. It agrees with u_t on D_t and theta+ddc h_k+2epsilon kappa is globally positive on that small chart.
- Locality transfers positivity to the restricted product with u_t. For fixed u_t its polynomial expansion in epsilon converges in total variation locally, so restriction to D_t does not create a weak-restriction gap. Mixed positivity and a telescoping difference give domination by the Omega product.
- Increasing compatible restrictions define a positive sigma-finite extended measure for every smooth theta and every theta-psh u. No bigness or BMP. Smooth gauge invariance follows by comparing sufficiently deep bounded representatives on a common exhaustion away from the pole set.
- Damping bounds follow by domination; capacity-continuity uses bounded signed-product expansions at a fixed cutoff, then uniform tails. The cutoff vanishes at the truncation level. These arguments have primary-agent review only so far.

## Undamped measures and equations

- Capacity convergence plus a sequence mass bound and uniformly small deep-sublevel masses implies finite undamped weak convergence. Finiteness of the limit is first proved with monotone cutoffs; its own tail then tends to zero by finite measure continuity.
- Increasing unbounded weight integrability implies those conditions. Conversely construct a locally finite sum of ramps at levels with geometric tail bounds. The condition is an integrability functional, not an asserted energy primitive or a convex finite-energy class.
- A finite NPP measure is uniformly absolutely continuous with respect to capacity: otherwise take sets of summable capacities and uniformly positive measure; their limsup has capacity zero but positive measure. Capacity-zero iff pluripolar is explicitly a standard local-capacity input.
- Exponential equations with positive exponents converging to a positive limit, L1-convergent densities, and capacity-convergent nonpositive potentials have uniform raw tails and pass to the limit. Density convergence is in total variation; uniform control of s exp(-lambda s/2) handles the changing exponent. The theorem now allows arbitrary smooth theta.
- None of this proves that L1 compactness implies capacity compactness, preserves a relative envelope class, proves existence, or supplies uniform tails as lambda approaches zero. Deeper recent-paper PDE inputs are still marked as unfinished self-contained proof obligations.

## Remaining obligations

Finish the supplemental audit and visual PDF review, then independently review the arbitrary-background and raw-tail/PDE extensions. Reconstruct the XZ heat-kernel counterexample and recent-paper contact/domination/existence proofs. Most later SGPT comparison chapters remain unwritten. Preserve these limits in every progress report.

At ~13:18 UTC: general_background_01 launched in the normal Rethlas sandbox, exec60798. The97-page PDF passed final build and visual review; checksum and detailed scope are in build-snapshot-03.json. No goal-completion claim is made.
