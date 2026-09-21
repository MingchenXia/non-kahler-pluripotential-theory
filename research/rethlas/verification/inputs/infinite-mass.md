Run_id: infinite_mass_01

Statement: Let X be a connected compact complex manifold with a smooth Hermitian form omega. Use ddc=i/(2pi) partial bar-partial. Suppose that the supremum of integral_X (omega+ddc v)^n over smooth omega-psh functions v is infinite. Assuming the explicitly stated classical inputs B, K, and E below, there is U in PSH(X,omega), U<=0, whose extended non-pluripolar Monge-Ampere measure has infinite total mass, although integral_X exp(-p U)dV is finite for every p>0. In particular every multiplier ideal I(pU), with weight exp(-pU), equals O_X. Arbitrarily small positive scalar multiples of U have the same two properties and converge to zero in L1. No novelty claim is requested.

The following are mathematical assumptions of this verification task. The goal is to verify the deduction from them, not to verify a research-paper citation.

Input B: For bounded omega-psh functions, and also for bounded potentials of arbitrary smooth semipositive backgrounds, Bedford--Taylor mixed products are well defined, positive, multilinear, and local in the plurifine topology. These finite measures do not charge pluripolar sets. Products of smooth inputs agree with usual wedges. In particular, if bounded omega-psh functions coincide on a plurifine open Borel set, their Monge-Ampere measures have equal restrictions there.

Input K: For a fixed smooth positive volume form dV, the family of omega-psh functions v with sup_X v=0 has uniformly bounded L1 norms. A decreasing sequence of omega-psh functions with uniformly bounded L1 norms has its pointwise limit in PSH(X,omega), with the canonical upper semicontinuous representative; it is not identically minus infinity.

Input E: There exist alpha>0 and C<infinity depending on (X,omega,dV) such that integral_X exp(-alpha v)dV<=C for every omega-psh v normalized by sup_X v=0.

Definition: For u in PSH(X,omega) with u<=0, put u_t=max(u,-t), D_t={u>-t}, and nu_t=1_{D_t}(omega+ddc u_t)^n. These positive measures increase with t by Input B: for s>t, u_s=u_t on D_t, so nu_s restricted to D_t equals nu_t. The set D_t is plurifine open and Borel. Define the extended measure mu_omega(u)=lim_{t to infinity} nu_t. This is allowed to have infinite mass; no assertion that it is a Radon measure is made without a separate finiteness bound.

Proof:

Choose a_j=2^{-j}, j>=1, so sum a_j=1. By unbounded smooth mass, choose smooth omega-psh u_j with sup_X u_j=0 and M_j=integral_X(omega+ddc u_j)^n>=2^{j(n+1)}.

Set U_N=sum_{j=1}^N a_j u_j. Since u_j<=0, the functions U_N decrease, and they are omega-psh because
omega+ddc U_N=sum_{j=1}^N a_j(omega+ddc u_j)+(1-sum_{j=1}^N a_j)omega>=0.
Input K bounds their L1 norms by a constant independent of N. Therefore U=lim_N U_N is omega-psh and U<=0.

Fix j. The function v_j=U-a_j u_j equals the decreasing series sum_{k not equal j} a_k u_k. It is a quasi-psh function with
(1-a_j)omega+ddc v_j>=0,
by the same partial-sum positivity and convergence of currents; subtracting the smooth function a_j u_j also identifies its canonical representative. In particular v_j<=0.

For t>0, let v_{j,t}=max(v_j,-t). Since the background (1-a_j)omega is semipositive, this is a bounded potential with (1-a_j)omega+ddc v_{j,t}>=0. Put W_{j,t}=a_j u_j+v_{j,t}. This is bounded and omega-psh.

On D_t={U>-t}, one has v_j=U-a_j u_j>=U>-t, hence v_{j,t}=v_j and W_{j,t}=U=U_t. By Input B,
nu_t=1_{D_t}(omega+ddc W_{j,t})^n.
The decomposition
omega+ddc W_{j,t}=a_j(omega+ddc u_j)+((1-a_j)omega+ddc v_{j,t})
has two positive terms. Positivity and multilinearity of bounded products give
nu_t >= a_j^n 1_{D_t}(omega+ddc u_j)^n.

As t tends to infinity, D_t increases to X minus {U=-infinity}. The pole set is pluripolar and has zero smooth volume. Since u_j is smooth, its Monge-Ampere measure also gives that set zero mass. Thus
mu_omega(U)(X)>=a_j^n M_j>=2^j.
This holds for every j, proving infinite mass.

For the exponential assertion, fix p>0. Choose N such that delta=sum_{j>N}a_j=2^{-N} satisfies p delta<=alpha. Write U=A_N+V_N, where A_N=sum_{j<=N} a_j u_j is smooth and V_N=sum_{j>N}a_j u_j.

We claim integral_X exp(-p V_N)dV<=C', where C'=max(C,integral_X dV). For a finite truncation m>N, use Jensen's inequality with weights a_j/delta for N<j<=m, plus the remaining weight 1-sum_{N<j<=m}a_j/delta on the zero function. This yields
exp(-p sum_{N<j<=m} a_j u_j)
 <= sum_{N<j<=m} (a_j/delta) exp(-p delta u_j)
    +(1-sum_{N<j<=m}a_j/delta).
Since u_j<=0 and p delta<=alpha, Input E bounds the integrals of each exponential on the right by C. Integrating and then using monotone convergence as m tends to infinity proves the claim. Since A_N is smooth on compact X, exp(-p A_N) is bounded, and therefore integral_X exp(-p U)dV<infinity.

The constant germ 1 is locally integrable against exp(-pU), so I(pU)=O_X for every p>0 (with the multiplier-ideal convention stated in the claim).

Finally fix 0<epsilon<=1. The function epsilon U is omega-psh, nonpositive, and has all the exponential integrability properties just proved (replace p by p epsilon). To see that its mass is infinite, use the bounded potentials epsilon U_t on D_t={U>-t}. The canonical truncation max(epsilon U,-epsilon t) equals epsilon U_t everywhere. Thus its truncation measure on D_t is
1_{D_t}(omega+ddc(epsilon U_t))^n
 >= epsilon^n 1_{D_t}(omega+ddc U_t)^n,
because omega+ddc(epsilon U_t)=epsilon(omega+ddc U_t)+(1-epsilon)omega. Let t tend to infinity. This proves mu_omega(epsilon U)(X)=infinity. Since U is L1, epsilon U tends to zero in L1 as epsilon tends to zero.

Instructions: Use the Rethlas verification AGENTS.md and three required verification skills. Initialize memory for this run and verify every deduction, including the extended-measure definition, the common plurifine sets, background coefficients, infinite series, Jensen step, and scaling. Inputs B,K,E are hypotheses of the present conditional theorem and are not claimed to be proved here. Do not replace the theorem by a stronger one assuming a finite global product. Produce results/infinite_mass_01/verification.json and a concise final report. Do not edit the book or files outside this copied verification workspace.
