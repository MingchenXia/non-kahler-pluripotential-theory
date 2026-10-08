# P14: general warped root proof, full review pending

Assess the complete explicit sufficient-condition theorem for this selected task. Scope: General warped nonclosed endpoint paths, actual minimizing metrics and cost independent of every minimizer selection, geometric quantitative integrable endpoint profiles and exact endpoint volume/nonbigness, beyond closed positive-volume core cases. The broader original programme remains open. No accepted companion theorem, proof verdict, article or trusted note is a premise. Other parts of the complete shared root note are preserved and must not be promoted to a full original closure.

# P02/P14: a general warped-product formula and geometric power orders

ROOT-DEVELOPED, UNVERIFIED mathematical exploration. No native mathematical
review, blind reconstruction, final comparison, acceptance or publication has
occurred. This is not an additional checked paper or a completed original
problem. Existing frozen radial arguments and their historical evidence remain
unchanged. The proposed theorem imports the ordinary smooth positive-density
Monge--Ampere existence theorem, with the exact source application stated below.

Use dd^c=(i/(2 pi))partial barpartial. Let B be a connected compact Kahler
m-fold, m>=2, with Kahler form kappa. Let C be any connected compact complex
curve with smooth positive probability form w. On X=B times C put n=m+1,
h0=kappa+w, and mu=sigma wedge w, where sigma is any smooth positive probability
volume on B. All pullbacks are implicit. Let chi be a smooth closed real nef
(1,1)-form on B, and let a>=0 be smooth on B. Put theta=chi+a w. For eps>0 set

 chi_eps=chi+eps kappa,
 L_eps=a+eps,
 W_eps=integral_B chi_eps^m,
 H_eps=integral_B sigma/L_eps.

Nefness of chi means chi_eps has a smooth strictly positive dd^c representative
for each eps; adding L_eps w gives strict admissibility of theta+eps h0.

## 1. Proposed exact full-test formula

The proposed formula is

 V_mu(theta+eps h0)=n W_eps/H_eps.                         (1)

Choose a smooth Kahler representative K_eps of chi_eps. The smooth positive
density (W_eps/H_eps) sigma/L_eps has integral W_eps. Applying the smooth
Monge--Ampere existence theorem on the CLOSED background K_eps gives a smooth
strict closed form A_eps=chi_eps+dd^c phi_eps satisfying

 A_eps^m=(W_eps/H_eps) sigma/L_eps.

Precisely, write F=log(((W_eps/H_eps) sigma/L_eps)/K_eps^m).
Tosatti--Weinkove, arXiv:0910.1390v2, Corollary 1, printed page1, gives
(K_eps+i partial barpartial psi)^m=exp(F+b) K_eps^m. Closedness and integration
give b=0 since both desired and background top masses are W_eps. In the
normalization here phi_eps includes the previously chosen representative
potential plus 2 pi psi. Source page2 explicitly states the closed-background
normalization. The source's Main Theorem proof, printed pages3--8, has also been
read; its closing paragraph refers the existence-continuity argument to
Cherrier/Demailly or its earlier TW paper. Do not claim that this source supplies
a self-contained reconstruction of those additional external proofs. This
exploration uses the same smooth positive-data existence foundation already
present in the original catalogue, applied on B, not a new singular existence
theorem. No uniform estimates as eps approaches0 are assumed or used.

Put Omega_eps=A_eps+L_eps w and c_eps=n W_eps/H_eps. Then
Omega_eps^n=c_eps mu. For every smooth strict Gauduchon test gamma on X, matrix
AM--GM and dd^c gamma^m=0 give

 integral theta_eps gamma^m
 =integral Omega_eps gamma^m
 >=c_eps^(1/n) integral(mu/gamma^n)^(1/n)gamma^n.

The equality in the first line is ordinary distributional/smooth Stokes, not a
formal assertion about a convenient determinant. An ACTUAL minimizing metric is

 gamma_eps=L_eps^(-1/m) Omega_eps,
 T_eps=gamma_eps^m=L_eps^(-1) A_eps^m+m A_eps^(m-1) w.

T_eps is d-closed: the derivative of its first term is a form of base degree
2m+1 and vanishes, while its second term consists of closed factors. Therefore
gamma_eps is an admissible strict Gauduchon metric. Its numerator is n W_eps,
and its denominator is c_eps^(m/n) H_eps. The quotient equals c_eps^(1/n),
proving (1) from the ENTIRE test infimum and providing an actual minimizer.

No symmetry, radial potential, regularized maximum or endpoint weak
Monge--Ampere solution is used in this argument.

For any smooth nef theta, its Gauduchon root infimum is continuous under a
positive perturbation from above: monotonicity gives lambda(theta+eps h0)>=
lambda(theta), while each fixed test gives limsup lambda(theta+eps h0) at most
its theta-quotient. Taking the infimum of those fixed quotients gives the
reverse limit inequality. Thus the endpoint value in (1) is its actual
decreasing-limit value. It is n W0/H0, with value0 if W0=0 or H0=infinity.
If H0=infinity and W0=0 this same value0 follows from W_eps bounded and H_eps
increasing; no undefined quotient or singular-product passage is needed.

## 2. Numerical and geometric degeneration orders

Define nu=max{j in {0,...,m}:integral_B chi^j kappa^(m-j)>0} and q=m-nu.
The coefficients of W_eps are nonnegative: approximate the nef class by strict
closed representatives and use closed Stokes for their intersection numbers.
The coefficient for j=0 is positive. Therefore

 W_eps is bounded above and below by positive constants times eps^q.

Suppose the zero set of a is a nonempty finite DISJOINT union of smooth compact
real submanifolds Z_i of real codimension d_i>0. Assume explicit two-sided
geometric estimates c_i dist(x,Z_i)^(k_i)<=a(x)<=C_i dist(x,Z_i)^(k_i) in fixed
tubular neighborhoods, with k_i>0. Outside these neighborhoods a is bounded
below. This is an actual geometric vanishing hypothesis, not an assumption
about H_eps or the desired order. Smooth positive sigma is comparable to the
tubular Euclidean volume. Put r=min_i d_i/k_i and z=max(0,1-r).

Tubular integration compares H_eps to sums of
integral_0^R t^(d_i-1)/(t^(k_i)+eps)dt. Rescaling t=eps^(1/k_i)y and splitting
the rescaled integral at1 shows:

 r<1: H_eps is comparable to eps^(r-1);
 r=1: H_eps is comparable to log(1/eps);
 r>1: H_eps tends to a finite positive H0.

Hence a_minus(theta)=a_plus(theta)=q+z. The common order is integral if and
only if r>=1, since q is an integer and 0<z<1 when r<1. For r=1 the order q
has the additional inverse-logarithmic decay; q=0 in that case does not imply
positive endpoint volume. If the zero set is empty take z=0, H0 finite.
Positive endpoint volume is equivalent to nu=m and H0 finite, which in this
geometric class is equivalent to nu=m and either no zero or r>1.

Arbitrary smooth positive probability volumes on X are comparable to mu; their
Gauduchon denominators, hence volumes, differ by fixed positive factors.
Arbitrary Hermitian perturbing metrics are bounded between c h0 and C h0;
monotonicity sandwiches their perturbed volumes between the h0 volumes at
c eps and C eps. Thus the common power order and its integrality conclusion
hold for every smooth positive reference volume and every Hermitian h.
Exact numerical formula (1) is claimed for the displayed product probability
and product perturbation; no density-independent exact value is asserted.

## 3. Complete comparison criterion INSIDE this geometric family

Let pi:Y->B be a proper modification with connected smooth compact Kahler Y.
Assume a and pi*a both meet the displayed geometric zero-set hypotheses, with
deficits z_B and z_Y (not necessarily identical codimensions). Choose a smooth
curvature eta_D of an effective real divisor D on Y and assume the CLOSED
residual chi_D=pi*chi-eta_D is nef. Work on Y times C, with the product
modification Pi=pi times id_C and beta=chi_D+(pi*a)w. The positive current

 Pi*theta-beta+dd^c log|s_D|^2=[D]

is understood with local metric weights and real divisor coefficients, so the
effective comparison concerns actual divisorial mass. Every background and
residual in this assertion is smooth nef. Perturbative minimal multiplicities
are not being substituted for this current.

The proposed common orders are

 source: m-nu_B(chi)+z_B;
 pure pullback: m-nu_Y(pi*chi)+z_Y;
 residual: m-nu_Y(chi_D)+z_Y.

Here nu is the same explicit intersection maximum with a Kahler metric on its
own base. One can prove the needed intersection facts directly:

(a) nu_Y(pi*chi)=nu_B(chi). For a nonzero source intersection, pi*kappa_B<=
C kappa_Y, and positive nef approximants give a nonzero target intersection.
For a zero source intersection of degree j, let K_delta=chi+delta kappa_B+
dd^c u_delta>0. The positive closed currents K_delta^j have masses tending0
against kappa_B^(m-j), so they tend weakly to0. Their cohomology classes tend
to [chi]^j, which must consequently vanish (pair against a basis of smooth
closed complementary forms). Pullback then forces every target intersection
of that degree to be0. This argument does not assume a smooth semipositive
representative of chi or a numerical-dimension theorem beyond that definition.

(b) nu_Y(chi_D)<=nu_Y(pi*chi). Indeed for two nef classes alpha,beta with
alpha-beta=[D] effective,
alpha^j-beta^j=[D] sum_(l=0)^(j-1) alpha^l beta^(j-1-l).
Pair against kappa_Y^(m-j). Each summand is nonnegative by taking smooth
positive nef approximants of alpha and beta, pairing them with the positive
divisor current and passing to the finite intersection-number limit. Thus a
vanishing alpha intersection forces the beta intersection to vanish.

(c) z_Y>=z_B. Any smooth positive probability sigma_Y dominates a positive
constant times the smooth semipositive top form pi*sigma_B. Therefore H_Y(eps)
>=c H_B(eps), using degree1 integration on the modification. The established
power/log asymptotics force the displayed deficit inequality.

Both contributions to the residual order difference are nonnegative. Pure
modification equality holds EXACTLY when z_Y=z_B. Equality in the composite
effective-divisorial comparison holds EXACTLY when

 nu_Y(chi_D)=nu_B(chi) AND z_Y=z_B.

For a divisor removed on the same base, this reduces to the precise geometric
criterion nu(chi_D)=nu(chi). These criteria compare actual intersection maxima
and actual zero-set codimensions/vanishing orders, not the desired exponents
restated as an assumption. They apply only to this stated product class and
the modifications for which both zero-set estimates hold. Arbitrary
modifications, intersecting zero strata and arbitrary nonclosed backgrounds
are not classified by this exploration.

The radial point-blowup draft is a concrete instance: chi=b H with b>0, a=Cx^k,
d_B=2m, k_B=2k; after blowing up p, d_Y=2, k_Y=2k. The deficits are
max(0,1-m/k) and max(0,1-1/k), with equality exactly k=1. Its named residual
intersections give the previously proposed terminal integer jumps. Existing
radial arguments are self-contained and do not rely on this new note.

## 4. Endpoint cost without a radial hypothesis

For this part assume chi=alpha is Kahler, W=integral_B alpha^m>0. Fix t>0 and
consider theta_s=alpha+(a+t-s)w, 0<=s<t, with eta=w and nef endpoint
theta_t=alpha+a w. Write eps=t-s, H(eps)=integral sigma/(a+eps),
J(eps)=integral sigma/(a+eps)^2. The actual minimizing metrics of section1 give

 integral_X eta T_s=W J/H,
 D_mu(gamma_s)=(n W/H)^(m/n) H,
 cost(s)=n^(-m/n) W^(1/n) H^(-(n+1)/n) J.

Direct differentiation of lambda(s)=(n W/H(t-s))^(1/n) gives exactly
-lambda'(s)=cost(s), not merely an estimate for selected convenient tests.
For each fixed s<t all densities and minimizers are smooth; no smooth selection
of potentials as s varies is needed because their displayed cost is independent
of the choice. In fact every other actual minimizing Gauduchon test has the
same scalar cost: hold that test fixed at s and test theta_(s+delta). The full
infimum gives lambda(s+delta)<=lambda(s)-delta cost_test. Divide by positive
and negative delta in the strict path interval and use the differentiability
of the explicit lambda to obtain cost_test=-lambda'(s). Thus the identity
does not depend on which actual minimizer is selected, and no differentiability
of a selected family of metrics is assumed. The actual endpoint limit from section1 and the fundamental
theorem on each compact path segment prove the improper identity

 integral_0^t cost(s)ds=lambda(0)-lambda(t)<infinity.

No desired cost integrability is assumed. It follows from the geometric
construction and the exact quotient for all tests. General product sigma and
the actual torsion d theta_s=da wedge w remain explicit. Closed base
intersection invariance is used only for W; no nonclosed intersection-number
invariance is presumed.

For a SINGLE zero submanifold of codimension d and order k with the two-sided
distance estimates above, tubular integration gives further quantitative cost:

 d<k: cost(t-eps) comparable to eps^((1-d/k)/n-1);
 d=k: comparable to eps^(-1) [log(1/eps)]^(-(n+1)/n);
 k<d<2k: comparable to eps^(d/k-2);
 d=2k: comparable to log(1/eps);
 d>2k: cost tends to a finite positive limit.

In the last three lines H0 is finite. These follow by comparing J to
integral_0^R u^(d-1)/(u^k+eps)^2 du; for d>2k use dominated convergence.
All five displayed endpoint profiles are integrable. Positive endpoint volume
occurs exactly when d>k, or there is no zero.

Nevertheless theta_t is NOT BIG whenever a has a zero. This can be seen
without restricting any singular potential to a fiber and without a group
average: if theta_t+dd^c v>=delta(kappa+w), test against rho kappa^m for any
nonnegative smooth rho on B. The test form is dd^c-closed because its base
degree is already top degree. Distributional Stokes annihilates dd^c v, and
the horizontal forms disappear. The inequality reads

 integral_B rho(a-delta)kappa^m>=0.

Thus a>=delta everywhere, contradicting any zero. This applies to EVERY
genuine quasi-psh v, including unbounded ones, since v is locally integrable
and the test is smooth. If a is strictly positive and alpha is Kahler, theta_t
itself is positive, hence big. The resulting exact positive-volume/nonbigness
criterion in this warped family is a genuine nonclosed endpoint phenomenon.

## Audit boundary and next steps

TW source Corollary1 and closed normalization have been fully read at primary
pages1--2; the complete printed Main Theorem proof pages3--8 has been read in
text. Four actual primary page views (1,2,7,8) are recorded separately; do not
call those eight actual views or a recursive reconstruction of every cited
estimate/continuity theorem. The matrix calculation, product Stokes, tubular
integrals and intersection-comparison arguments above are new root proofs.
Poincare--Lelong for the divisor uses the exact Demailly foundation assessed
for the existing radial P02 draft, with a fresh application still needed in
any eventual native review.

No native model has received this new theorem, and none of the untouched cold
original-only inputs has been seeded with it. Native review and blind
reconstruction would still have to assess ALL arguments, the smooth existence
application and the comparison statements. The original P02 and P14 broader
programmes remain open. No article or acceptance count is changed by this note.


## Exact source applications and scope

Smooth positive-data MA existence is used ONLY on the strict CLOSED Kahler base representative K_epsilon, with positive normalized total target mass W_epsilon. Tosatti-Weinkove arXiv0910.1390v2 Corollary1 and printed2 closed normalization, https://arxiv.org/pdf/0910.1390v2. Entire printed relevant proof3-8 read previously; cited final existence-continuity dependencies not recursively certified. Source potentials rescale2pi. The cofactor minimizer, full variational equality, power orders and endpoint limits are new proofs.

For the effective real divisor D=sum d_j D_j, write its global potential as sum d_j log||s_j||^2, not a section of an unconstructed real line bundle. Demailly June21,2012 III2.15 entire proof143-144 and V13.1-13.3 calculation271, https://people.math.harvard.edu/~demarco/Math274/Demailly.pdf, give our dd^c phi_D=[D]-eta_D with eta_D=sum d_j iTheta/(2pi). All three pages were freshly read and viewed for this application. Current positivity with smooth wedges, elementary deRham duality and Stokes are separately assessed; no numerical-dimension invariance, nonclosed top-product law, endpoint MA existence or desired cost bound is an assumed premise.

Each external or task source passage must have a valid declared nonnegative premise index; never use negative indices. Retrieve primary evidence and identify every false statement, missing argument or unresolved indispensable premise honestly.


# Entire current standalone article, including its concrete examples

Assess the whole article and all new explicit calculations against the exact unchanged task. No native review has occurred for this article-inclusive preparation. The draft labels do not grant a result.

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Endpoint cost for all minimizing Gauduchon metrics\newline on nonclosed warped paths}
\author{}\date{}
\begin{document}\maketitle
\noindent\textbf{Working draft.} This new root-developed candidate has not
passed complete native review, independent reconstruction or final comparison.
\begin{abstract}
We propose an exact endpoint-cost theorem on a compact K\"ahler manifold
times a curve. A smooth nonnegative vertical coefficient determines
nonclosed paths with actual balanced minimizers. The cost is independent
of every choice of attaining Gauduchon metric, and its improper integral
equals the drop in root volume. Tubular codimension and vanishing order
give five quantitative integrable profiles. Positive endpoint volume is
compatible with failure of bigness, which is excluded for every genuine
quasi-psh strict representative by a smooth closed test.
\end{abstract}

Use $\ddc=\frac{i}{2\pi}\partial\bar\partial$ and ordinary wedge powers.
Let $(B,\alpha)$ be a connected compact K\"ahler $m$-fold, $m\geq2$,
$W=\int_B\alpha^m>0$. Let $C$ be a connected compact complex curve
with a smooth positive probability form $w$, and $\sigma$ a smooth
positive probability on $B$. Put $X=B\times C$, $n=m+1$,
$\mu=\sigma\wedge w$; suppress pullbacks. Fix $a\geq0$ smooth and $t>0$.
Consider the strict path and nef endpoint
\[
 \theta_s=\alpha+(a+t-s)w,\quad 0\leq s<t,
 \qquad\theta_t=\alpha+aw,\qquad\eta=w.
\]
For nonconstant $a$, the torsion is $d\theta_s=da\wedge w\ne0$.
Dependence on the specified $\sigma$ remains in the formulas below.

For every smooth positive Gauduchon metric define
\[
 D_\mu(\gamma)=\int_X(\mu/\gamma^n)^{1/n}\gamma^n,
 \quad\lambda_\mu(\theta)=
 \inf_{\ddc\gamma^m=0}\frac{\int_X\theta\wedge\gamma^m}{D_\mu(\gamma)},
 \quad V_\mu=\lambda_\mu^n.
\]
The endpoint is defined by decreasing Hermitian regularization, agreeing
with the nonnegative full infimum as proved below. A background is big
if it has a genuine global quasi-psh potential making it dominate a
positive multiple of a Hermitian metric.

\section{Actual minimizers and the full volume}
Write $\epsilon=t-s$, $L=a+\epsilon$, and
\[
 H(\epsilon)=\int_B\frac{\sigma}{a+\epsilon},\qquad
 J(\epsilon)=\int_B\frac{\sigma}{(a+\epsilon)^2}.
\]
Smooth Monge--Amp\`ere existence in the closed positive class
$[\alpha]$, in the formulation of \cite[Corollary 1]{TW}, gives
\[
 A_\epsilon=\alpha+\ddc\phi_\epsilon>0,\qquad
 A_\epsilon^m=\frac{W}{H(\epsilon)}\frac{\sigma}{L}.
\]
The target has total mass $W$, so integration in the closed class fixes
the source scalar. Our potential is $2\pi$ times the source's
$i\partial\bar\partial$ potential. No endpoint equation or uniform
endpoint estimate is imported.

Set $\Omega_\epsilon=A_\epsilon+Lw$,
$c_\epsilon=nW/H(\epsilon)$, and
$\gamma_s=L^{-1/m}\Omega_\epsilon$. Then
\[
 \Omega_\epsilon^n=c_\epsilon\mu,
 \qquad \gamma_s^m=L^{-1}A_\epsilon^m+mA_\epsilon^{m-1}\wedge w.
\]
Its first cofactor summand is a base top-degree form and its second is
closed, so $d\gamma_s^m=0$. For every admissible test $\xi$, smooth
Stokes and matrix AM--GM give
\[
 \int_X\theta_s\wedge\xi^m=\int_X\Omega_\epsilon\wedge\xi^m
 \geq c_\epsilon^{1/n}D_\mu(\xi).
\]
For the named $\gamma_s$ the numerator is $nW$ and denominator
$c_\epsilon^{m/n}H(\epsilon)$; hence it attains equality. In particular
\begin{equation}\label{eq:volume}
 V_\mu(\theta_s)=\frac{nW}{H(t-s)}.
\end{equation}
This is the full infimum over all smooth positive Gauduchon metrics,
not an infimum over product tests.

\section{Cost independent of the minimizing selection}
For an actual attaining metric $\xi$ at $s$ define
\[
 C_\xi(s)=\frac{\int_X w\wedge\xi^m}{D_\mu(\xi)}.
\]
The named balanced metric satisfies
\[
 \int_X w\wedge\gamma_s^m=\frac{WJ}{H},
 \quad D_\mu(\gamma_s)=(nW/H)^{m/n}H,
 \quad C(s)=n^{-m/n}W^{1/n}H^{-(n+1)/n}J.
\]
The last expression is also $-\lambda_\mu'(\theta_s)$ by
differentiating \eqref{eq:volume}.

\begin{lemma}\label{lem:all}
Every actual minimizing Gauduchon metric at $s$ has cost $C(s)$.
No differentiability of a selected family of metrics is required.
\end{lemma}
\begin{proof}
Hold any such $\xi$ fixed. The all-test infimum at a nearby path point
gives, for both signs of sufficiently small $\delta$,
\[
 \lambda_\mu(\theta_{s+\delta})
 \leq\lambda_\mu(\theta_s)-\delta C_\xi(s).
\]
The explicit volume is differentiable on the strict path. Dividing by
positive and negative $\delta$ and taking their limits forces
$C_\xi(s)=-\lambda_\mu'(\theta_s)=C(s)$.
At $s=0$ the same argument uses the short strict extension to negative
$s$, for which $a+t-s$ is still positive.
\end{proof}

\begin{theorem}\label{th:endpoint}
For any smooth $a\geq0$ and any selection of actual attaining metrics,
the improper integral exists and
\[
 \int_0^t C(s)\,ds
 =\lambda_\mu(\theta_0)-\lambda_\mu(\theta_t)<\infty,
 \qquad V_\mu(\theta_t)=\frac{nW}{H(0)}.
\]
Here $H(0)=\int_B\sigma/a$, with endpoint volume zero if it is infinite.
\end{theorem}
\begin{proof}
The full root infimum at the nef endpoint is the limit of its strict
path values. Monotonicity gives one inequality. For any fixed test its
quotient converges to its endpoint quotient; taking the infimum gives
the reverse inequality. The same argument with any positive Hermitian
regularization identifies the original endpoint definition.
Monotone convergence yields $H(\epsilon)\to H(0)$, so
\eqref{eq:volume} gives the asserted actual endpoint value.

On each compact strict path segment the fundamental theorem gives
\[
 \int_0^r C(s)\,ds=\lambda_\mu(\theta_0)-\lambda_\mu(\theta_r).
\]
The integrand is nonnegative and the endpoint limit just proved is
finite. Letting $r\uparrow t$ proves the improper identity.
Neither integrability nor an endpoint Monge--Amp\`ere solution has been
assumed. Lemma~\ref{lem:all} covers every minimizing selection.
\end{proof}

\section{Quantitative geometric profiles}
Suppose $\{a=0\}$ is a smooth compact real submanifold of codimension
$d>0$ and in a fixed tube
$a\asymp\operatorname{dist}(\cdot,\{a=0\})^k$, $k>0$,
with positive two-sided constants. Assume $a$ is bounded below outside
the tube, and put $r=d/k$. These are geometric hypotheses on the
coefficient, not hypotheses on the desired cost.

Tubular integration compares $H$ and $J$ to
\[
 \int_0^R\frac{u^{d-1}}{u^k+\epsilon}\,du,
 \qquad \int_0^R\frac{u^{d-1}}{(u^k+\epsilon)^2}\,du.
\]
Splitting at $\epsilon^{1/k}$ gives the thresholds one and two. Therefore
\begin{equation}\label{eq:profiles}
 C(t-\epsilon)\asymp
 \begin{cases}
 \epsilon^{(1-r)/n-1},&r<1,\\
 \epsilon^{-1}\bigl[\log(1/\epsilon)\bigr]^{-(n+1)/n},&r=1,\\
 \epsilon^{r-2},&1<r<2,\\
 \log(1/\epsilon),&r=2,\\
 1,&r>2.
 \end{cases}
\end{equation}
In the final case the cost tends to the finite positive value
$n^{-m/n}W^{1/n}H(0)^{-(n+1)/n}J(0)$ by dominated convergence.
Each profile is integrable: the first power is greater than $-1$;
the logarithmic power at $r=1$ exceeds one; the power for $1<r<2$
is again greater than $-1$. The endpoint volume is positive exactly
when $d>k$. With finitely many disjoint finite-order components the
same comparisons use their smallest codimension/order ratio.

\section{Bigness and an explicit positive-volume nonbig endpoint}
If $a$ has a zero, $\theta_t$ is not big. Indeed suppose for a genuine
quasi-psh $u$ that
\[
 \theta_t+\ddc u\geq\delta(\alpha+w),\qquad\delta>0.
\]
Test against the pullback of an arbitrary smooth nonnegative base
top-degree form $\zeta$. This test is $\ddc$-closed by dimension, so
distributional Stokes gives
$\int_B(a-\delta)\zeta\geq0$.
A nonzero $\zeta$ supported where $a<\delta$ contradicts this.
The argument uses local integrability of genuine quasi-psh functions
and smooth tests; no singular potential is restricted to a curve fiber.
If $a>0$ everywhere then $\theta_t$ itself is positive and big.
Thus in this family bigness is exactly the absence of zeros.

For a concrete genuinely nonclosed example take $B=\mathbb P^m$,
$\alpha=\kappa$ normalized Fubini--Study, $\sigma=\kappa^m$,
$C=\mathbb P^1$, and
\[
 a([Z])=\frac{\sum_{j=1}^m|Z_j|^2}{\sum_{j=0}^m|Z_j|^2}.
\]
Its single zero is quadratic in a real codimension-$2m$ affine chart,
so $r=m>1$. The law of $a$ has density $m x^{m-1}dx$ on $[0,1]$:
polar integration in the $Z_0$ chart gives radial density
$m q^{m-1}(1+q)^{-m-1}dq$, and $x=q/(1+q)$ gives this law.
Hence $W=1$, $H(0)=m/(m-1)$ and
\[
 V_\mu(\theta_t)=\frac{(m+1)(m-1)}m>0,
\]
although the endpoint is not big. Its cost is logarithmic at $m=2$,
and has a finite positive limit for $m>2$.
These statements retain the nonclosed torsion and the chosen probability.

\begin{remark}
This theorem supplies a geometric endpoint family beyond conclusions
requiring a closed positive-volume core. It does not classify arbitrary
paths or assert that positive nonclosed root volume implies bigness.
Only the closed base mass $W$ is invariant under smooth potential
changes; no nonclosed intersection-number invariance, metric uniqueness,
endpoint PDE solvability or literature priority is asserted.
\end{remark}
\begin{thebibliography}{9}
\bibitem{TW} V. Tosatti and B. Weinkove, \emph{The complex Monge--Amp\`ere
equation on compact Hermitian manifolds}, arXiv:0910.1390v2
(11 November 2009), Corollary 1 and closed-background normalization,
pp.~1--2; \url{https://arxiv.org/abs/0910.1390}.
\end{thebibliography}
\end{document}


# Current literature and companion overlap assessment, unverified

# P14 current overlap and endpoint review boundary

This is private unverified scope assessment, not a theorem or a verification
verdict. It does not alter the original P14 task or either frozen candidate.

The current repository was actually read at commit
00a5044d04fa050adfc3969583c482fc78d092e2. The complete files
book/author/section_radial_positive_volume_nonbig.tex and
book/author/section_radial_gauduchon_test_limits.tex were read, as was the
complete section_gauduchon_volume_variation.tex. These are manuscript evidence,
not a substitute for independent primary-source assessment.

The manuscript already proves the projective example with b=1,
a=x/((m-1)/m): its positive nonbig endpoint, actual balanced strict-path
minimizers, full-test volume n/H_epsilon, and the logarithmic versus finite
normalization limits of the volume-minimizing tests. Those facts must not be
reported as a newly discovered example or as a new general positivity theorem.
The P15 checked warped-cone paper also already uses the smooth product
full-test volume calculation and tubular inverse-moment estimates. That overlap
must not be hidden by assigning the same calculation to another problem ID.

The proposed P14 extension has its own explicit endpoint question: on ANY
compact Kahler base times a curve, for EVERY smooth a>=0 and the fixed smooth
product probability, prove the exact improper cost identity for EVERY actual
minimizing selection, without smooth dependence of that selection or an
endpoint Monge--Ampere solution. The quantitative statement gives five
integrable cost profiles from tubular codimension divided by vanishing order.
This is a restricted endpoint theorem; the full programme remains open.

The current saved general article was again read completely. Its argument
constructs balanced minimizers on the strict segment using smooth closed-base
existence, establishes the full quotient with matrix AM--GM and Stokes, uses
the fixed-test inequality with both signs to identify the cost of all other
attaining metrics, and proves the endpoint limit with a fixed-test upper bound.
Monotone convergence identifies H(0), including infinity. The five profiles
follow by splitting tubular H and J integrals at epsilon^(1/k). No singular
endpoint product is needed. Failure of bigness is tested with smooth base
top-degree forms against ALL genuine global quasi-psh strict representatives.

These remain root candidate calculations. Independent native review must
assess both correctness and adequacy beyond the original task's background.
No claim of literature priority, unrestricted P14 completion, mathematical
acceptance or publication follows from this note. The prior article and
inputs retain their original creation metadata and hashes. A current review
assembly may append this assessment while preserving the earlier assembly.
