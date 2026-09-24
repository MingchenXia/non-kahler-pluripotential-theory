# Bounded verification request: Hopf normalization and its quadratic variation

Run the verification_agent on the mathematical statement and proof below, with fresh run_id `hopf_normalization_defect_01`. Inspect the complete report and return its verdict and any actual gaps. This is one bounded check, not a request to restart other work. Do not modify historical verifier records or memory. The inputs below are explicitly accepted established results in this book; verify the deductions, constants, equality cases and all descent steps rather than re-proving the inputs. Do not claim novelty.

## Accepted internal inputs

1. Smooth Hermitian Monge--Ampere existence/uniqueness and smooth dependence: for every smooth real F on a connected compact Hermitian manifold (X,omega), there is a unique b(F) and unique mean-zero smooth u_F with omega+ddc u_F>0 and (omega+ddc u_F)^n=exp(F+b(F)) omega^n. The mean uses the fixed omega^n. Solutions depend smoothly in Holder spaces on smooth finite-dimensional families of F. The linearized operator is L_u v=n dd c v wedge omega_u^(n-1)/omega_u^n. Its kernel consists of constants; its adjoint probability mu_u is positive and satisfies integral L_u v dmu_u=0. For a Gauduchon omega at u=0, mu_0=omega^n/integral omega^n. The same existence theorem applies on the Kahler base P^2.
2. Hopf geometry and smooth mass identity: dd c=i partial barpartial/(2pi). X=(C^3\{0})/<z->e^-1 z>, pi:X->P^2. On the cover s=log|z|^2, alpha=ddc s=pi^*omega_FS, beta=ds wedge d^c s=(i/(2pi))partial s wedge barpartial s, omega=alpha+beta>0. beta^2=0, alpha^3=0, omega is Gauduchon, integral omega^3=6, integral_P2 omega_FS^2=1. A fiber is E=C/(Z+2pi i Z), with local coordinate w=log z_0, normalized Haar area dA_E=(i/(4pi))dw wedge dbar w. Coordinate changes translate w by a holomorphic function of the base. The probability nu=omega^3/6 disintegrates as dA_E omega_FS^2. For every smooth real u, integral_X omega_u^3=6+6 integral_X |u_w|^2 dnu. The vertical derivative u_w is globally defined. For smooth v on P^2, pi^*(omega_FS+ddc v)+beta>0 iff omega_FS+ddc v>0; its cube is 3pi^*(omega_FS+ddc v)^2 wedge beta.
3. Let A u be normalized Haar average on each elliptic fiber (equivalently average under [z]->[e^a z], a in E). For bounded omega-psh u, A u is a pullback of a bounded omega_FS-psh function, and ||u-Au||_L2(nu)^2 <= (2/3)(integral omega_u^3-6). Equality of mass to 6 holds iff u is a base pullback. For smooth u all averages and descended functions are smooth.

## Proposed proposition

For a smooth real F on this Hopf threefold, let (u_F,b(F)) solve input 1 with integral u_F dnu=0, and define

    D(F)=b(F)+log integral_X exp(F) dnu.

Then

    exp(D(F))=1+integral_X |(u_F)_w|^2 dnu,
    D(F)>=0,
    ||u_F-Au_F||_L2(nu)^2<=4(exp(D(F))-1).

Moreover D(F)=0 iff F=pi^*H for a smooth real H on P^2. In particular, for smooth positive f with integral f dnu=1 the scalar b(log f) is nonnegative, with equality exactly for such base-pullback densities.

For any smooth real G on X, let v be the unique smooth mean-zero solution of

    L_0 v=G-integral G dnu,
    L_0 v=3ddc v wedge omega^2/omega^3.

Then

    (d/dt)D(tG)|_(t=0)=0,
    (d^2/dt^2)D(tG)|_(t=0)=2 integral |v_w|^2 dnu.

The last number vanishes iff G is a smooth base pullback. No global convexity, uniform coercivity, extension to nonsmooth data or general Hermitian mass bound is claimed.

## Complete proposed proof

Integration of omega_u^3=e^(F+b)omega^3 and the smooth mass identity gives exp(D)=M(u)/6=1+integral |u_w|^2 dnu. Nonnegativity follows. Substitute M(u)=6exp(D) into the accepted average inequality for the coefficient 4.

If D(F)=0, the energy vanishes; by smoothness u_w vanishes everywhere. Since u is real it is constant on each connected elliptic fiber, so u=pi^*q for a smooth real q. Strict positivity implies omega_FS+ddc q>0. The cube formula shows
exp(F+b(F))=pi^*((omega_FS+ddc q)^2/omega_FS^2).
The ratio on the right is positive smooth, hence taking its logarithm proves F is a base pullback.

Conversely suppose F=pi^*H. Apply smooth existence on (P^2,omega_FS) to obtain omega_FS+ddc q>0 with (omega_FS+ddc q)^2=exp(H+c)omega_FS^2. Since the base form is closed, Stokes' theorem gives exp(c) integral_P2 exp(H)omega_FS^2=1. Pulling back and wedging with 3beta gives omega_(pi^*q)^3=exp(F+c)omega^3. Subtracting its nu-mean fixes the potential normalization. Uniqueness implies b(F)=c. Disintegration gives integral_X exp(F)dnu=integral_P2 exp(H)omega_FS^2, so D(F)=0. This proves the equality case and the assertion for f.

For the derivative statement, write u_t=u_(tG), b_t=b(tG). Smooth dependence applies with the fixed mean. At t=0, uniqueness gives u_0=0 and b_0=0. Differentiating the logarithmic equation gives L_0 dot u_0=G+dot b_0. Because omega is Gauduchon, nu is its adjoint probability. Integration gives dot b_0=-integral G dnu, hence dot u_0=v. In C^1, (u_t)_w=t v_w+O(t^2), so
exp(D(tG))=1+t^2 integral |v_w|^2 dnu+O(t^3).
Taking logarithms proves both derivative formulas.

If the second derivative vanishes, v_w=0 everywhere and v=pi^*q for smooth q. Direct wedge expansion, using alpha^3=beta^2=0, gives
L_0(pi^*q)=pi^*(2ddc q wedge omega_FS/omega_FS^2).
Thus G=L_0v+integral G dnu is a base pullback. Conversely, if G is a base pullback, so is tG for every real t, and the equality case already proves D(tG)=0. Its second derivative is zero, as required.
