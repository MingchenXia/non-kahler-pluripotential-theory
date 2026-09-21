# Local continuity with a strict singular barrier

Candidate next bounded argument, NOT yet in the book or audited.

Let theta be smooth semipositive big, rho theta-psh with theta+ddc rho>=kappa omega, normalized rho<=-C0-1, and bounded u in[-C0,0] solve MA_theta(u)=f dV, f nonnegativeLp. Existing one-sided stability71 permits an UNBOUNDED v<=0.

Use Demailly94 Theorem4.1 and Remark4.7 with closed current ddcu and nonclosed lower bound -theta. The faithful general curvature error is an increasing epsilon(delta)->0, not an unverified linear rate. Reconstruct the same capped Kiselman transform Phi from R_tu+K(t²-delta²)+K(t-delta)-c log(t/delta), with theta+ddcPhi>=-(Ac+epsilon(delta))omega. The source mixed estimate and Kt absorption should justify this; do not cite KN19omega lemma as literally the general theta statement. No genuine fiber-holomorphic exph assumption.

Given eta<stability endpoint, alpha=2eta<1, choose c=delta^alpha+epsilon(delta), e=Ac+epsilon(delta), s=e/kappa, and v=(Phi+s rho)/(1+s). Then theta+ddcv>=0, v<=Phi<=R_delta u<=0, since Phi>=u-K(delta²+delta)>=-C0-1>=rho for small delta. Integral positivepart(v-u)<=O(delta²) from73 averaging proof. Stability gives v-u<=Cdelta^alpha globally.

On {rho>=-M}, Phi-u=(1+s)(v-u)+s(u-rho)<=C_M c. At an attained minimizing radius, -c log(t/delta)<=Phi-u+K(delta²+delta)<=C_M c, so t>=a_M delta. Monotonic smoothing then gives |R_{a_M delta}u-u|<=C_M c on this set. Thus on each compact subset of the ordinary locally-bounded locus of rho, smooth approximants converge uniformly, proving continuity. The global derivative bound C/t gives an explicit modulus by choosing t=sqrt(distance); one gets a bound involving epsilon(C sqrt(distance)) and distance^(alpha/2). No Holder exponent follows without a proved power bound on epsilon.

If a sharp O(delta) general-theta curvature error is independently established, the same proof yields73's Holder exponent locally. Demailly94 printed theorem only gives an unspecified modulus. Its proof freezes gamma on shrinking charts; one must quantify the resulting constants, not simply assert the linear rate from smoothness. The plain continuity result avoids this issue.

This would improve the current bounded semipositive-big equation section while keeping classical regularization as the permitted standard input. It does not prove global continuity on all singular resolutions or general NPP moving-reference finiteness.
