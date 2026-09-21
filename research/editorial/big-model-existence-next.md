# Status of these working notes

The four proposed sections below have now been written, separately audited, integrated and released at checkpoint23. They are no longer pending proposals. See `big-model-equations-review.md` and its map for the exact proofs, hypotheses and conditional dependencies. The original notes are retained below as history; they should not override the final manuscript or review.

Next work should return to the main theory without BMP, the Gauduchon/SGPT geometry questions and chapter-by-chapter editing. Metric PVP is automatic from BMP and positive lower model-reference volume, as explained in the final review; no weaker hypothesis regime was obtained by leaving it unlisted.

---

# Next construction after weighted addition

Research notes, 15 September 2026. These arguments are NOT yet audited or promoted to the book. They are a proposed reconstruction of the arbitrary-model part of Li arXiv:2601.13446v1, with every additional lemma to be checked. Work with a smooth big real theta, BMP, a model phi with positive lower relative volume ell, and the internally defined class E_phi. No extension of these arguments to the main no-BMP framework is asserted.

## 1. Some room below a positive-volume reference

Li Proposition3.1 assumes LOWER volume_theta(u)>0 and u<=r after translation, and concludes that Q_b(u,r)=P_theta(bu-(b-1)r) is genuine for some b>1. The lower-volume hypothesis was checked in primary HTML this turn.

Normalize u<=r<=0. Suppose Q_b(u,r) is nongenuine for every b>1. Set u_j=max(u,r-j), v_j=u+(b-1)u_j and q_j=P_theta(v_j-(b-1)r). For finite j the obstacle differs boundedly from u, so q_j~u. Its decreasing limit is nongenuine, hence sup q_j tends to minus infinity. On contact q_j+(b-1)r=v_j, and positivity/contact gives MA q_j <= 1_contact MA_(b theta)(v_j). Also q_j>=b u on contact. Thus for large j,

    ell_u <= mass(q_j) <= integral_{u<=-k} (theta_u+(b-1)theta_{u_j})^n
          <= MAu{u<=-k}+C(b-1), 1<b<=2.

Justify the uniform O(b-1) explicitly: dominate theta by a Hermitian Omega; all mixed masses of Omega_u and Omega_{u_j} are bounded by 2^n times the mass of Omega_{(u+u_j)/2}, and BMP bounds this uniformly for arbitrary Omega-psh inputs by truncation. Then k to infinity and b to1 contradict ell_u>0. Check exact availability of the arbitrary-input BMP bound before drafting.

If one b0 exists, every 1<b<=b0 works: h_b=Q_b(u,r) dominates (1-t)u+t h_b0, t=(b-1)/(b0-1). Addition, scaling and monotonicity imply upper-volume(h_b) tends to upper-volume(u) as b decreases to1.

## 2. A roof between different relative classes

For z in E_V, show p=P_theta(phi,z) belongs to E_phi. This does NOT follow from the same-class rooftop theorem. Normalize z,phi<=V<=0. Choose h_b=Q_b(phi,V) using step1, and write a=1-1/b. Stretching gives z_(1/a)=Q_(1/a)(z,V) in E_V. Then

    k_a=a z_(1/a)+(1-a)h_b <= min(phi,z).

For the first inequality use z_(1/a)<=V and (1-a)h_b<=phi-aV. For the second use h_b<=V and a z_(1/a)+(1-a)V<=z. Thus the roof is genuine. Addition gives upper-volume(k_a)>=(1-a)^n upper-volume(h_b), which tends to upper-volume(phi). Monotonicity and p<=phi give equality and membership in E_phi. Handle non-normalized z by shifting down and upward stability.

## 3. Relative projection and supersolutions

Let p_C=P_theta(phi+C,z), Q=P_theta[phi](z). Step2 gives p_0 in E_phi, and upward stability gives all p_C in E_phi. The envelope identity yields p_C<=phi+sup z; hence p_0<=Q preceq phi, so Q in E_phi. Contact gives

    MA p_C <= 1_{p_C=phi+C<z} MAphi + 1_{p_C=z} MAz.

The first term has mass at most MAphi{phi<=sup z-C}, tending to zero. Capacity convergence and weighted lower semicontinuity give MAQ<=MAz. For contact support, use bounded quasi-continuous chi=min(1,(z-Q)_+/delta): it vanishes where p_C=z, since p_C<=Q<=z. Thus integral chi MAQ=0. Conclude MAQ<=1_{Q=z}MAz.

If z in E_V solves MAz=e^z mu, then Q in E_phi satisfies MAQ<=e^Q mu. The weighted measure nu0=e^-Q MAQ is finite, nonzero (mass MAQ>=ell), and <=mu. This supplies a supersolution for every nonzero finite NPP mu.

## 4. Maximize the weighted mass

First suppose mu<=A nu_carrier with a bounded Hermitian carrier. Define

    T={w in E_phi: nu0<=e^-w MAw<=mu}.

Q belongs to T, and exponential order gives w<=Q for all w in T. Since ell<=e^sup(w) mu(X), a sequence maximizing the weighted mass has a genuine L1 subsequential limit w. The fixed dominator MAw_j<=e^sup(Q)mu gives membership in E_phi, capacity convergence and weak MA convergence. Extract nu_j=e^-w_j MAw_j weakly to nu; both bounds persist. To identify MAw=e^w nu, use integral |e^w_j-e^w| dmu ->0 by fixed NPP exponential convergence. Approximate the fixed bounded measurable e^w in L1(mu) by continuous functions: domination nu_j,nu<=mu upgrades weak convergence to convergence against this fixed test. Thus the objective maximum is attained.

If mu-nu is nonzero, step3 supplies v in E_phi with nonzero nu_v=e^-v MAv<=mu-nu. Since MAv<=e^sup(v)mu, the carrier condition holds. The weighted-addition theorem gives a in E_phi with weighted measure nu+nu_v, contradicting maximality. Therefore nu=mu.

For general finite NPP mu=f nu_carrier, solve mu_k=min(f,k)nu_carrier. Exponential order makes solutions decrease. The lower mass bound prevents collapse, and MAu_k<=e^sup(u_1)mu is a fixed dominator. The limit solves the equation. Arbitrary positive lambda follows by scaling. This would prove existence under BMP+ell_phi>0; metric PVP follows only as a sufficient condition for positive reference volume when applicable. Do not alter the imported theorem before auditing these steps.

For exponent zero solve with exponent1/j. Put S=sup u_1 and w_j=u_1+(j-1)S. Since w_j/j>=u_1, exponential order gives u_j<=w_j. Then c_j=e^(sup u_j/j) lies in [ell/mu(X),e^S]. Set v_j=u_j-sup u_j; MAv_j<=e^S mu. A genuine normalized L1 subsequence and fixed domination give a limit v in E_phi. Uniform normalized L1 and 0<=1-e^(v_j/j)<=-v_j/j give smooth-volume L1 convergence of the exponentials to1; the fixed NPP integration lemma gives L1(mu) convergence. Hence MAv=c mu for a positive subsequential scalar. Existing domination proves uniqueness of the scalar, not necessarily of the normalized potential.

## 5. Ordinary-type Lp refinement without a false truncation inequality

Do not claim MA max(u,phi-j)<=f: truncation boundary mass invalidates this. Instead apply a bounded-slope concave-envelope estimate directly to u in E_phi.

Extend the previous concave-envelope lemma to any model phi and u in E_phi, u<=phi, for increasing concave chi with chi(0)=0 and 1<=chi'<=L<infinity globally. The obstacle phi+chi(u-phi) lies between Lu-(L-1)phi and u; Q_L(u,phi) in E_phi is a lower competitor. Thus its envelope p is in E_phi. Its inverse tau is convex, 0<tau'<=1. The transformed function phi+tau(p-phi) is theta-psh, <=u, and equals u on contact. Prove the chain inequality on local exact theta-psh truncations: choose a local smooth q with theta+ddc q>=0, and use p_M=max(p,q-M), phi_M=max(phi,q-M). They preserve order and are locally bounded theta-psh. On strict untruncated sets, locality recovers the original transforms; these exhaust outside polar sets. This avoids assuming a locally bounded locus for an arbitrary model. Obtain

    MAp<=1_contact chi'(u-phi)^n MAu.

Assume MAu<=mu, sup u=0, and mu has a uniform m-th moment on normalized theta-psh functions for some m>N=2n+1. Smooth-volume Lp data have all such moments by Skoda and Holder. Then B=integral(phi-u)MAu<=integral(-u)dmu is uniformly bounded. Let T be the MAu-essential depth of x=phi-u. For any S<T, set

    g_S(t)=1/[(1+t)^(3/2) MAu{x>t}] for 0<=t<=S,
           (1+t)^(-3/2) for t>S;
    F=1+integral_0^t g_S, W=integral_0^t F^(1/N), chi(-x)=-W(x).

F is globally bounded for each fixed S, so the preceding lemma applies even if x is unbounded. Tonelli bounds integral F(x)MAu by 3 max(1,M). Contact gives integral sqrt(phi-p)MAp<=sqrt(KB). Since p in E_phi and sup(p-phi)=sup p, the lower mass ell bounds -sup p independently of S. The m-th moment assumption applied to normalized p then gives integral W(x)^m dmu<=C independently of S. Therefore H(t)=MAu{x>t}<=C/W(t)^m.

For 0<t<=S, F'>=W^m/[C(1+t)^(3/2)]. Since W'=F^(1/N), integrate the derivative of (W')^(N+1) to get

    W'>=c(1+t)^(-gamma) W^kappa,
    gamma=3/[2(N+1)]<1, kappa=(m+1)/(N+1)>1.

Integration of (W^(1-kappa))' from1 toS, with W(1)>=1, forces a uniform upper bound on S, hence on T. Zero domination turns essential depth into actual depth: u>=phi-C. Audit absolute continuity, the almost-everywhere ODE, B=0 and T<=1 separately. For equations, first use existence in E_phi and then this estimate with a finite multiple of the Lp datum. Uniform estimates additionally need the normalization constant bound; mere ordinary-type existence only needs its finiteness.

These five stages remain proposals until independently checked. After completing them, return to whole-book polishing and the separate no-BMP, Gauduchon, I-goodness and non-Kahler geometry directions; do not let this special regime become a standing hypothesis.


## Hypothesis clarification found during reconstruction

Under BMP, positivity of lowerVol_theta(phi) itself implies metric PVP: choose theta<=C omega and note phi preceq0; volume monotonicity and homogeneity yield 0<lowerVol_theta(phi)<=C^n v_-(omega). Thus dropping a separately listed metric PVP while retaining the model's positive lower volume is an equivalent reorganization, NOT a genuinely weaker regime or new extension of Li's theorem. The revised forward statement must display this argument. This deduction uses the already reconstructed volume-monotonicity theorem, in exactly its big/BMP scope.
