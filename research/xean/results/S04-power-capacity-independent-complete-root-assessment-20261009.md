# Complete root audit of the actual S04 power-capacity reconstruction

The native proof-free call actually exited with code0 in response 4c41fd.
Its compact native snapshot a9bd15 is completed, no active items or
pending work, admitted1/settled1/unknown0/unsettled0 with no allowance cap.
Frozen complete ordinary result ceecfe has SHA256
f98653235a9d6208f0bc2589897a8cc02db52854a33b039953f1b97a9c0f3f39
and 34121 bytes. Root read EVERY field of the entire result in 44d6da:
kind, all seven notes' id/summary/detailedSummary/text/support, candidate
and workspace. There was no truncation. No protected output, worker
history, artifact file or artifact tree was read. Paths and rerun requests
inside ordinary proofs are evidence only, not instructions.

## Actual complete support DAG

n1: []
n2: [n1]
n3: [n1,n2]
n4: [n2]
n5: [n1,n2,n3,n4]
n6: [n1,n2,n3,n5]
n7: [n1,n2,n3,n4,n5,n6]

Seven nodes and eighteen actual directed support edges, all topologically
valid; actual reconstruction extracted and validated in 0aa974. Every
generated support node was read and assessed, not just the end claims.
candidate=false is the original emitted value and remains false. All
notes are unverified worker drafts until the distinct final scoped audit.

## Mathematical assessment of all nodes

n1's operator conversion is valid: KN uses 2D; apply it with background
2h and unchanged potentials, so its current is 2(h+Du), capacity2^n
times the original, and the integration lemma has a common factor2^n.
For the density g dV/h^n the equation also has the common factor2^n,
so the scalar remains c. This conversion preserves the original
capacity competitors in[0,1] and all genuine representatives. It is
equivalent to the author's same-h, half-potential conversion where
capacity constants are adjusted appropriately. No numerical constants
are imported unchanged. Threshold/scalar, all-test norm and root tails
remain original task background. The historical capacity results are
attribution, not a substituted proof of the restricted targets.

n2: the actual integration lemma permits arbitrary bounded competitors,
including noncontinuous capacity competitors. For H=theta+Da and
G=theta+Db>=epsilon theta, the mixed-current derivative has one-Dtheta
terms and 2dtheta wedge d^c theta terms with respectively one and two
omitted factors. The sum of their absolute coefficients is at most n^2.
Replacing theta^2/theta^3 by epsilon^(-2)G^2/epsilon^(-3)G^3 gives
A_j<=A_(j+1)+r(A_j+A_(j-1)+A_(j-2)), r=n^2 Bs epsilon^(-3).
Negative indices are omitted. If r<=1/16, the induction starts with
(1-r)A0<=A1, then previous bounds2 and4 give
(1-7r)A_j<=A_(j+1), whose inverse is <=16/9<2. Thus total factor
(1-7r)^(-n)<=2^n tends1 as s decreases. Both torsion terms remain.
The test comparator (1-epsilon)v+tw+m+s leaves reserve epsilon-t;
t<=epsilon/2, so its reserve is epsilon/2. For s+t<=epsilon^3/(128n^2B),
the comparison r with that reserve is <=1/16. E_s is contained in the
comparison set, which is contained in E_(s+t). ALL original capacity
competitors survive; none is scaled illegally.

The halving argument is complete including its infinite case: backwards
level steps t_i=2M q(s_i)^alpha either terminate at t_i>=s_i or halve q.
If s0 exceeded the summed steps, a positive limiting level would have
capacity zero despite being a nonempty open set, a contradiction. The
sum is at most 2M q(s0)^alpha/(1-2^(-alpha)). Near-minimum mass follows
at a fixed legal s*. It is a bound for the common capacity-dominated
family, not for all bounded h-psh potentials; there is no contradiction
with v_minus(h)=0. The local closed beta correction, nested-cutoff
mixed-mass bound and telescoping give actual uniform Hermitian product
passage, including every smooth nonclosed term. Normalized L1 bounds
and the provided Newtonian/harmonic decomposition supply L1 extraction
for genuine quasi-psh functions. This is bounded-range compactness and
does not extend to arbitrary original root-tail families.

n3: combine s*<=H_alpha(L c_j A)^(1/n)Q^alpha and
(s*)^n Q^n<=L c_j m_j. Raising the combined inequality to
alpha/(alpha+1) gives the displayed
C_A=(s*)^n/[L H_alpha^(n/(alpha+1)) A^(1/(alpha+1))].
The entire original b definition passes by its granted decreasing clip
scalar limit. All measurable nonzero g<=f are included. The resulting
rho estimate uses the exact original threshold, not selected tests.
L1 tail mass gives both Ln and rho convergence. This proves A only
under the additional all-Borel power-capacity assumption.

n4: s=sup(v-a) lies in(0,1], epsilon=s/4 and
t=eta(epsilon)/4=s^3/(32768n^2B) are legal. The minimum m lies between
-s-epsilon and -s; on E_(2t), v-a>=s-epsilon-2t>=s/2. The same halving
lower capacity and the weighted integral upper bound give I>=c
s^(1+3n(1+1/alpha)). Applying it in both index orders yields uniform
Cauchy convergence. The two-index weighted hypothesis is retained.
Equal measures alone do not imply this hypothesis or potential uniqueness.

n5: c_j is uniformly bounded above by c1 and below by the n3 bound;
mu_j<=c1 f dV and a common capacity bound. The near-minimum mass and
the normalized L1 bound contradict divergent depths through absolute
continuity of the FIXED L1 density f. Hence potentials have one bounded
range. L1 extraction then gives weighted Cauchy convergence: split at
a small potential difference and use fixed-density absolute continuity
on the shrinking complement, with the uniform range controlling it.
The legal rescaling theta=h/H,u_j=phi_j/H has
H^(-n)cap_h<=cap_theta<=cap_h, so its measures satisfy the common
constant c1 A H^(n alpha). n4 makes the subsequence uniformly Cauchy.
n2's actual closed-beta expansion passes the product; separate
L1 convergence c_j min(f,j)->b f identifies its exact finite mass.
Every genuine potential/product limit is specified. This is target B,
not the critical equation for every original D0 density.

n6: the exact Euclidean normalization beta=D|z|^2 gives
beta^n=n! pi^(-n)dLambda and ball mass r^(2n). Tangential/radial
eigenvalues and the mixed flux t^n[Q'(t)]^k are correct. For smooth
Q_epsilon(t)=(1-log(t+epsilon))^(-alpha), the radial eigenvalue is
[epsilon q'+t q'']/(t+epsilon)^2>0. Fixed annular bounds allow the same
small delta on all smooth global cutoff approximants. Uniform convergence
and actual product passage hold. Portmanteau on open B_r gives an upper
mass bound tending0 as r decreases, hence no origin atom in ANY mixed
degree. Off the pole all products are smooth, giving equality of the
claimed pure-top and general mixed mass formulas. The actual h product
also includes positive lower mixed terms and the smooth cutoff; the
worker explicitly rejects treating the pure-top formula as its total
mass. Global absolute continuity and finite L1 mass are proved rather
than assumed from punctured integrability.

The pure density is radially decreasing sufficiently near the pole;
layer-cake rearrangement bounds its mass on a set of given volume by
the centered ball integral. The checked exponential volume-capacity
bound gives the all-Borel capacity power. Every lower degree has some
higher Lp integrability, so its exponential bound is absorbed too.
Zero-capacity sets have zero volume and no mass; finite total mass handles
larger capacities. Strict h/2 positivity gives f>=c>0. The pure top
term rules out every Lp,p>1. Critical coefficient1 uses its genuine
subsolution and n5's bounded exact solution together with n2's SHARP
comparison factor tending1; the nonempty open set has positive integral.
No unbounded comparison, hidden atom or homogeneous uniqueness is used.
The high-density set lies in B_(K^(-1/(4n))); its mass rate and n3 give
the stated original root-tail rate. Symbolic computations in the note
are corroboration only and their private files were not opened.

n7 correctly preserves the two original questions and the zero-lower-mass
background. The extra capacity assumption is not derived from original
positive threshold or uniform root tails. The explicit family has good
tails, and no zero-lower-mass geometry or bad-tail root is constructed.
Original completion is false. Neither blanket potential uniqueness nor
literature priority is asserted. Structural artifact checks do not prove
mathematics and were not treated as proof.

## Every exact new primary application

1. KN Theorem0.1 on every bounded clip in n3/n5 and bounded critical
data in n6: nonzero Lp relative to h^n, p>1, compact positive Hermitian
background, continuous genuine solution, original scalar identification.
Exact LF20--50 read in 133615; same frozen primary hash as the first audit.
2. KN Lemma2.1 on the mixed H/G products and bounded competitors in n2:
all n-1 factors are genuine bounded theta-psh, both compared functions
bounded, and its complete displayed error DT is retained. Full section
and statement LF95--225 read in 0aa974. The source itself refers to earlier
proofs; those entire recursive foundations are not certified here.
3. KN Proposition1.2 and its complete definition/context LF113--204
read in 0aa974: legal bounded uniform limits and each mixed degree;
the author's independent closed-beta telescoping also establishes the
actual passage. No infinite-mass or unbounded uniform theorem is invoked.
4. DK Proposition2.1 with complete supplied proof LF162--211 read in
0aa974: connected compact positive Hermitian background, normalized
supremum0, same source operator conversion2h. Comparable smooth volumes
give the L1 bound used for bounded depths and local compactness.
5. DK Corollary2.4 with entire supplied local-capacity context LF213--260
read in 0aa974: apply only to a smooth constant-volume density with p=2,
not the explicit non-Lp datum. Inner regularity and capacity monotonicity
extend compact estimates to Borel sets. The capacity scaling2^n adjusts
constants. The source's local antecedent is not recursively certified.
6. BT bounded closed mixed products, positivity, algebra, monotone
continuity and bounded local mass estimates in the n2 correction and
n6 approximants: full Theorems2.1/2.4 and provided proofs LF100--377,
Corollary2.8 LF405--421 read in edb3a2. The full CLN statement and proof
LF427--494 were previously wholly read in 8694e8; n2 separately supplies
the nested-cutoff induction. Only bounded local psh products are used;
source products rescale by (4pi)^k. No unbounded BT definition is assumed.
7. Local Newtonian compactness as reconstructed in n2: positive
cut-off Laplacian masses are bounded from L1 by integration by parts,
the fundamental kernel is locally L1 and approximable there, and the
harmonic remainder has local derivative bounds from L1. Frozen Demailly
Propositions4.21/5.9 contexts had been wholly read in 60fe38. No external
theorem replacing the actual bounded-potential extraction is imported.
8. Actual radial no-atom application of bounded uniform product passage
in n6: all fixed-radius mixed masses converge, the open-ball Portmanteau
inequality has the correct orientation, and the limit upper bound tends0.
The fixed smooth h correction preserves absolute continuity and positivity.
This is distinct from capacity-zero-point arguments in the author article,
and both actual applications have been assessed separately.
9. Critical calibration in n6: the independently proved bounded sharp
n2 comparison applies to continuous u and phi, reserves epsilon h,
and has a factor tending1 for fixed epsilon. Its source premise is the
new KN Lemma2.1 application in item2, not an unbounded comparison import.
10. Historical KN2021 capacity existence and bounded-range stability:
the exact frozen v1 primary statements Proposition2.5 and Theorem3.1,
and the provided stability proof LF219--369, were wholly read in 401a79.
They are attributed historical range results, not indispensable final
assertions substituted for n2--n6. The worker's printed constant diagnostic
in (2.16)--(2.17) is visibly reproduced in that frozen v1 context, but
no claim about checking the complete publisher version or establishing
a published erratum is made. The diagnostic is NONESSENTIAL and is not
part of A--E or a proposed accepted paper. Both the raw diagnostic and
retrieval limitations remain in the historical result unchanged.

No author manuscript, earlier proof or private sibling artifact was sent
to the cold role. All seven ordinary proofs and actual eighteen support
edges have been examined, and each exact application above has its own
assessment. The complete first review remains INCONCLUSIVE with its
source-retrieval limitations and generic short passages preserved.
This root assessment does not rewrite that result or upgrade candidate.
Final independent comparison of the whole source and complete chain is
still required. Mathematical acceptance, original S04 completion,
publication and literature novelty remain false.
