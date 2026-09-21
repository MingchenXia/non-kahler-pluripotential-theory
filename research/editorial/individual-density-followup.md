# Continuation after the individual-density threshold

22 September 2026. Working deductions conditional on acceptance of `individual_density_subsolutions_01`. Not integrated and not independently audited. No novelty claim.

## Upper semicontinuity of the threshold

Fix the Hermitian background h and smooth probability volume dV. Let b(f) be the proposed attained subsolution threshold for nonzero nonnegative L1 densities.

Claim: if f_j -> f in L1, with all densities nonnegative and f nonzero, then limsup b(f_j) <= b(f). Consequently the threshold is continuous at every f where b(f)=0. If v_-(h)=0, it is discontinuous at every f where b(f)>0, since the previously constructed obstructing densities are L1 dense.

Proof. Choose bounded nonnegative nonzero q_j <= f_j with ||q_j-f_j||_1 <= 1/j and

    b(f_j) <= c(q_j) <= b(f_j)+1/j.

This is possible by sufficiently deep truncation. The Gauduchon trace inequality bounds c(q_j) above uniformly: its denominator is the integral of the nth root of q_j against a fixed positive smooth weight, which converges to the corresponding strictly positive integral for f. (For n=1 use Stokes.) Extract so that c(q_j) -> a=limsup b(f_j), and q_j -> f almost everywhere. If a=0 the claim is immediate.

Take normalized continuous solutions u_j with MA_h(u_j)=c(q_j)q_j dV. Extract an L1 and almost-everywhere convergent subsequence with genuine limit u. Put

    w_j = (sup_{l>=j} u_l)^*,
    r_j = inf_{l>=j} c(q_l)q_l.

On the common full-measure set of density convergence, r_j increases to a f and 0 <= r_j <= a f; define it to be zero on the exceptional null set. Each w_j is bounded between u_j and zero and decreases to u. Finite maxima, ordered contact and bounded increasing continuity give MA_h(w_j) >= r_j dV. Damped decreasing continuity and dominated convergence give e^u MA_h^ext(u) >= a e^u f dV. Divide on {u>-N} and exhaust to obtain MA_h^ext(u)>=a f dV. The defining maximality of b(f) gives a<=b(f).

This is a one-sided stability of the maximal subsolution coefficient. It does not give capacity convergence of u_j, equality of their limiting measures or exact equation solvability. The construction deliberately replaces u_j by tail upper envelopes.

For any bounded approximation q_j -> f, the same argument gives limsup c(q_j)<=b(f). The canonical truncations attain equality in the limit. Thus b(f) is also the upper L1 relaxation of the bounded-density normalization functional:

    b(f) = lim_{delta downarrow 0} sup { c(q): q bounded, nonnegative,
              nonzero, ||q-f||_1 < delta }.

The displayed suprema are finite for sufficiently small delta by the same Gauduchon estimate. This provides a useful exact formulation, but not a continuous extension at positive b when lower mass vanishes.

## Finite sums and the root-density formulation

If b(f), b(g)>0, the new theorem supplies genuine potentials u,v whose extended measures dominate b(f) f dV and b(g) g dV. The local mixed inequality, applied to bounded truncations and restricted to common finite levels, should give for t in [0,1]

    MA_h^ext((1-t)u+t v)
       >= ((1-t)b(f)^(1/n) f^(1/n)
                     + t b(g)^(1/n) g^(1/n))^n dV.

Detailed obligation: the bounded truncations dominate their original densities only off their respective deep sublevel sets. Apply the mixed inequality with those indicators, then restrict to the common finite-level set before exhausting. The union of the two pole sets has zero smooth volume, so no right-hand-side density is discarded in the limit.

Choosing (1-t)b(f)^(1/n)=t b(g)^(1/n) gives

    b(f+g) >= (b(f)^(-1/n)+b(g)^(-1/n))^(-n)>0,

because (f^(1/n)+g^(1/n))^n >= f+g. Thus the data admitting a positive scaled subsolution form a cone closed under finite addition and downward domination. Infinite sums require new control and can leave this cone, as the diagonal obstruction shows.

With root densities p=f^(1/n), the quantity rho(p)=b(p^n)^(-1/n), allowing +infinity, is homogeneous. The preceding mixed inequality suggests subadditivity rho(p+q)<=rho(p)+rho(q). A precise functional-space formulation would need the endpoint conventions and completeness topology checked; do not infer a Banach-space theorem from this note.

## Smooth testing sees only an essential lower envelope

For f bounded below by a positive constant, let f_*(x) be the supremum over neighborhoods U of x of ess inf_U f. A continuous g satisfies g<=R f almost everywhere exactly when g<=R f_* everywhere. The forward implication follows by continuity and the definition of essential infimum; the reverse uses f_*<=f almost everywhere, which follows at Lebesgue points. Thus the smooth-test quantity in the earlier note depends only on f_*.

The proposed counterexample has f_*=1/M even though its bounded-truncation threshold is zero. The constant comparison therefore makes C_h^sm(f)=M c_h(1). This explains the counterexample without claiming that arbitrary Gauduchon-current functionals also ignore measurable changes of density.
