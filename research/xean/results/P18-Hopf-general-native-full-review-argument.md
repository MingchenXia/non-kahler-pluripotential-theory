# Complete new P18 general-dimensional root candidate

PRIVATE, UNVERIFIED. No native mathematical acceptance or publication. The frozen surface inputs remain unchanged.

## Exact original task

{
  "problem": "All manifolds are connected and compact. Write dd^c=(i/(2 pi))partial barpartial. Use genuine canonical quasi-psh representatives. For a smooth real (1,1) form theta, PSH(X,theta) means theta+dd^c u>=0. Ordinary order u preceq v means u<=v+C and equivalence means mutual order, including the canonical values at common poles. Extended products mean non-pluripolar Monge-Ampere products with smooth-background corrections. A big background admits a genuine strict current theta+dd^c u>=epsilon h for some Hermitian h and epsilon>0. BMP means v_+(h)<infinity, where v_+(h) and v_-(h) are the supremum and infimum of integral(h+dd^c u)^n over all bounded h-psh u. Positive lower mass means v_-(h)>0; it is distinct from BMP. Define I(tu) by local integrability of |g|^2 exp(-tu), with no extra factor 2. Ideal equivalence means equality at every real t>0. P_theta[u]_I is the usc supremum of theta-psh v<=0 ideal-equivalent to u. P_theta[u] is the ordinary singularity envelope, the usc supremum of theta-psh v<=0 with v preceq u. The lower and upper singularity volumes are the infimum and supremum of the extended mass over all v ordinarily equivalent to u in the specified background, not the raw mass of one representative. Let Y be a connected positive-dimensional compact complex submanifold of X, and u quasi-psh on X with generic Lelong number nu(u,Y)=0. The restricted ideal a_t=I(tu)O_Y is the image ideal, which is coherent and nonzero. A divisor over Y is a prime divisor E on any connected smooth compact modification pi:Z->Y. Define tau_(Y,u)(E)=lim_(t->infinity)ord_E(a_t)/t; the finite limit equals the supremum over t>0 and the integer limit. These intrinsic data depend only on the ambient ideal class and are additive and positively homogeneous. A naive restriction u|Y can be identically minus infinity; it is not the definition of these data. For a sufficiently large Hermitian Omega on Y, define T_Omega(u;Y) as the usc supremum of Omega-psh v<=0 with nu(v composed pi,E)>=tau_(Y,u)(E) on every such modification. Original P18: when Y fails at least one of BMP and positive lower mass, can Omega be chosen so that equality holds simultaneously for every prime divisor on every modification? After exactness, determine a background-compatible ordinary or ideal type, with addition and analytic approximation properties. Known background: a common competitor, the trace envelope, ideal/ordinary fixedness, convergence of restricted analytic envelopes, and pulled-background modification compatibility already hold without either mass property. Their Lelong conclusions are only lower inequalities. Doubling an admissible background gives positive finite individual envelope mass and prescribed-type Lp equations, but does not already prove exact trace numbers. Exact realization on curves, on Kahler targets in a sufficiently large closed background, under both mass properties, and for specified curve-fibration trace data is already known. A single model divisor current cannot encode all exceptional orders, and exact divisorial data alone does not determine top mass. No new realization, geometry, criterion or proof is supplied.",
  "completionCriteria": "Resolve simultaneous exactness in the stated generality by proof or an actual counterexample, then state and prove the compatible type, addition and approximation conclusions actually available. Alternatively give new substantive sufficient conditions on a genuinely non-Kahler target failing a mass property, beyond the listed curve and fibration cases. Do not mistake curvature room, individual envelope mass, a lower Lelong inequality or exactness on a single model for simultaneous exactness. A restricted theorem remains explicitly scoped. Verify exact indispensable external claims at primary sources and independently reconstruct the full argument."
}


## Full private mathematical note: notes/Hopf-all-dimensions-unbounded-mass.private-unverified.md

# Candidate: unbounded Monge--Ampere mass on every diagonal Hopf manifold of dimension at least three

PRIVATE, UNVERIFIED ROOT CANDIDATE. No mathematical acceptance, native review, independent reconstruction, publication or full catalogue closure is claimed. The frozen P18 six-page article and review/reconstruction inputs are unchanged. This is a separate extension proposal using the ORIGINAL Xia--Zhang smooth construction, not the unaccepted S02 heat-scale modification.

## Proposed theorem

For every integer n>=3, H_n=(C^n\{0})/<z->ez> fails BMP. Use our dd^c=i/(2 pi) partial barpartial, k=n-1, projectivization q_n:H_n->P^k, alpha_n=q_n^*omega_FS with integral_Pk omega_FS^k=1, r=log||z||^2 modulo two, beta_n=dr wedge d^c r, h_n=alpha_n+beta_n. The smooth potentials from the actual Xia--Zhang original transport construction on H_3 can be put on H_n using exactly the same radial/fiber function. Their positivity inequalities are dimension independent, and their positive-side annular masses compare from below by a fixed multiple of the threefold annular mass.

## Actual local matrices and angular integration

In the chart z0!=0 write xi=(z1/z0,...,zk/z0), x=log|xi|^2, and w=log z0 modulo Z+2 pi i Z. Put L=log(1+exp x), mu=exp x/(1+exp x). Then r=w+bar w+L and alpha=dd^c L.

For any real smooth V(x,w) with the original source's endpoint extensions, the matrix of h_n+dd^c V in the source's angular/radial/fiber frame (scaled for our normalization) has:

- k-1=n-2 identical angular eigenvalues A=(mu+V_x)/mu;
- the same radial/fiber two-by-two block as the threefold source (its dimension does not change).

Source normalization: dd^c_source=i partial barpartial=2 pi times ours. Both source alpha and beta divide by 2 pi to give ours, and the same numerical V gives h_n+dd^c_ours V=(h_n_source+dd^c_source V)/(2 pi). Thus the positivity ratios below use the exact numerical derivatives of the source V, with no potential rescaling.

Let

    Q[V]=V_xx+mu-|mu+V_(x bar w)|^2/(1+V_(w bar w)).

The positivity conditions, for every n>=3, are exactly

    1+V_(w bar w)>0, mu+V_x>0, Q[V]>0.

More explicitly the common radial/fiber block is

    [ (mu+V_xx)/(mu(1-mu)),
      (mu+V_(x bar w))/sqrt(mu(1-mu));
      (mu+V_(w x))/sqrt(mu(1-mu)), 1+V_(w bar w) ].

Its determinant equals (1+V_(w bar w))Q[V]/(mu(1-mu)). The background radial/fiber block has determinant one, so these determinants also give the relative volume factor. These are actual smooth matrices, not formal unbounded currents. The apparent -(1-mu)V_x term in the source's differential-form expansion cancels the radial contribution of its angular prefactor; it is absent from the evaluated radial matrix entry.

Normalize the angular contact measure on S^(2k-1) by mass one. The base Fubini--Study volume has radial density

    k mu^(k-1) mu' dx = k mu^k(1-mu) dx.

The vertical part of beta has fiber mass two. Consequently the angularly integrated smooth h_n^n volume has radial/fiber density 2n k mu^k(1-mu) dx dA_E, where dA_E is normalized Haar probability measure. The mixed base components of beta vanish after wedging with the top base form. Multiplication by the actual determinant above gives the smooth MA density.

Let J_3(V;x,w) denote the corresponding angularly integrated threefold MA density, including its h_3^3 radial/fiber volume density 12 mu^2(1-mu). The exact identity is

    J_n(V;x,w)=[n(n-1)/6] (mu+V_x)^(n-3) J_3(V;x,w).

Indeed the higher-dimensional determinant contributes A^(n-3), while the normalized radial/fiber background volume contributes [n(n-1)/6] mu^(n-3). This identity is independent of a changed angular sphere dimension because each contact sphere has been integrated with its own normalized probability measure. It gives an identity of integrated densities, not a pointwise identification of different manifolds.

## Apply the unchanged source family

The original source constructs V_eta=W_eta+g_eta, with W_eta=theta(q(x))F_eta(t(x),w), epsilon_eta=eta^(1/eta^2), all three strict positivity conditions, W_eta=F_eta(epsilon_eta,w) on x<=0 and constant at the positive end after adding g. It proves

    sup_(x,w) [W_(eta,x)]_- = o(1),
    -m_eta<=g_eta'<=0, m_eta=o(1),
    g_eta''=r_eta-m_eta psi,
    integral r_eta=m_eta, integral psi=1,

with psi supported in (-2,-1), r_eta supported in (-1/2,b_eta+1/2), and g_eta=0 on x<=-2. Thus for x>=0 and all sufficiently small eta,

    mu+V_(eta,x) >= 1/2-o(1) >=1/4.

The same V_eta is a smooth global potential on H_n: on the negative end it is independent of the singular radial coordinate and is smooth in the actual holomorphic fiber coordinate over xi=0; on the positive end it is one constant, independent of w and the base. The source's compact-chart extension proof applies with xi in C^k. Each angular eigenvalue is positive and the common two-by-two block is positive, so h_n+dd^c V_eta>0.

## Threefold mass cannot escape entirely to the negative side

The source gives integral_H3 MA_h3(V_eta)->infinity. It remains to show that the part x<0 is uniformly bounded; then the exact density comparison forces higher-dimensional divergence.

For x<0 the heat term W_eta=F_eta(epsilon_eta,w) has no x derivative. The only x derivatives are g',g''. Hence V_(x bar w)=0, and the fiber integral of F_(w bar w) is zero. The exact angular/fiber-averaged threefold MA density on x<0 therefore is

    12 (mu+g') [g''+mu(1-mu)].

Here -m_eta<=g'<=0 and mu+g'>0. On x<=-2 it equals the background density 12 mu^2(1-mu), which is integrable from minus infinity. On [-2,0], mu is bounded away from zero, |g'|<=m_eta, and

    integral_R |g''| <= integral r_eta + m_eta integral psi =2m_eta.

Since 0<mu+g'<=mu<=1, the integral of the displayed density over x<0 is at most the background contribution on x<0 plus 24m_eta, hence uniformly bounded. The possibly very high amplitude of F_(w bar w) causes no hidden bound problem: it has been integrated exactly and has zero fiber integral, while all remaining factors on x<0 are independent of w.

It follows that integral_(x>=0) J_3(V_eta;x,w) dx dA_E ->infinity. On that region the exact density formula yields

    integral_Hn MA_hn(V_eta)
      >= [n(n-1)/6] 4^(-(n-3)) integral_(x>=0) J_3(V_eta)
      ->infinity.

All potentials are smooth and globally strictly positive. Any other Hermitian metric H on H_n dominates c h_n for some c>0. Then H+dd^c(c V_eta)>=c(h_n+dd^c V_eta)>0 and its smooth mass is at least c^n times the displayed divergent mass. Therefore BMP fails for every Hermitian metric on H_n.

## Remaining checks and scope

The source identity integral_H3 MA->infinity, exact original endpoint descriptions, negative-slope estimate and correction integral are taken from Xia--Zhang arXiv:2608.21053v1, Theorem 1.1, Lemmas 2.1--2.3 and Proposition 4.1. Root has read its complete 902-line extraction and relevant actual pages for other exact applications; this new all-dimensions application must itself be assessed with the primary. The angular multiplicity, normalized radial measures, exact density ratio and negative-side estimate are new root calculations and still require independent reconstruction.

This candidate would allow a P18 projective-base extension to arbitrary higher-dimensional Hopf targets if a separately checked general-dimensional extraction lemma is supplied. It does not alter the current surface-base P18 candidate, prove sharp damping in original S02, prove positive lower mass in any dimension, determine all ordinary singularity volumes, or solve the unrestricted original catalogue.


## Full private mathematical note: notes/P18-general-divisorial-extraction.private-unverified.md

# Candidate: divisorial extraction for proper dominant maps in arbitrary dimension

PRIVATE, UNVERIFIED ROOT CANDIDATE. This note makes a new mathematical application of analytic resolution. No independent mathematical acceptance, native review, reconstruction, publication or original P18 closure is claimed. The frozen six-page surface-base P18 manuscript and its full-review and statement-only inputs remain unchanged.

## Exact proposed lemma

Let f:Z->B be a proper dominant holomorphic map of connected smooth compact complex manifolds, dim B=d>=1, and let E be a prime divisor on Z. If f(E)=B, every nonzero coherent ideal b on B satisfies ord_E(f^*b)=0, and every genuine quasi-psh w on B satisfies nu(w composed f,E)=0.

If f(E) is proper, there exist a smooth compact modification sigma:B'->B, a prime divisor F on B', a compact irreducible analytic graph G proper and bimeromorphic over Z, and a holomorphic map f':G->B', with the following properties. The projection G->Z is an isomorphism near the generic point of E. Its strict transform E' is a prime divisor there, f'(E')=F, and, for one integer e>=1,

    ord_E(f^*b)=e ord_F(sigma^*b)
    nu(w composed f,E)=e nu(w composed sigma,F).

The identities hold for every nonzero coherent ideal b and every genuine quasi-psh w. The graph need not be smooth away from the generic divisor. Its singularities away from that divisor are irrelevant to both identities. Every target B' is globally smooth and compact. No finite family of models replaces the quantifier over all original E.

## Finite construction using the order of a pulled-back top form

Start with G=Z and B'=B. At every stage retain the actual original smooth coordinate neighborhoods near a dense open subset of E; the projection to Z is an isomorphism there. The resulting G is a compact irreducible analytic space proper over Z, with a dominant holomorphic map f' to a smooth compact B'. The closure of the generic divisor is compact and irreducible, and its image S in B' is a compact irreducible analytic subset by the proper mapping theorem.

Near a smooth point of S where E maps generically, let y1,...,yd be coordinates of B'. Define J_E(f') as the minimum order along E of the coefficients of the nonzero d-form

    f'^*(dy1 wedge ... wedge dyd)

in a smooth local d-form frame on the retained neighborhood of E. Dominance makes this form nonzero. Thus J is a finite nonnegative integer. Changing smooth local coordinates multiplies the target volume form by a holomorphic unit and changes the source coefficient frame by an invertible holomorphic matrix; J does not change. There is no global volume-form requirement.

If S is already a divisor, stop. Otherwise c=codim S>=2. Blow up the coherent ideal of the reduced analytic subset S in B'. This blow-up is a proper compact analytic space T and is bimeromorphic over B'. It can be singular globally. Over the smooth part of S it is exactly the blow-up of a smooth center and is smooth.

At a generic point of E mapping to the smooth part of S, choose coordinates with S={y1=...=yc=0}. Let

    m=min_{1<=i<=c} ord_E(f'^*yi)>=1.

After choosing the least-order coordinate, say y1, and shrinking about a generic point of E, write f'^*y1=z1^m u, where u is a holomorphic unit. Every quotient f'^*yi/f'^*y1 is holomorphic there. The map therefore lifts holomorphically to the y1-chart of T on this neighborhood. This chart has coordinates

    s=y1, t2=y2/y1,...,tc=yc/y1,y_(c+1),...,yd.

It is smooth, including its exceptional divisor. Its map to B' satisfies the exact identity

    dy1 wedge ... wedge dyd
      =s^(c-1) ds wedge dt2 wedge ... wedge dtc
         wedge dy_(c+1) wedge ... wedge dyd.

Take the main component of the graph of this meromorphic lift; it is proper over the compact G and is an isomorphism on the displayed neighborhood of the generic E. Now resolve T by a proper bimeromorphic map rho:T_tilde->T which is an isomorphism over the entire smooth part of T. The new target T_tilde is smooth and compact. Near the generic image of E, rho is an isomorphism, so the same local lift persists. Take the main graph of the resulting meromorphic lift to T_tilde. Its projection again preserves the generic neighborhood of E. Composition with the old target modification gives a smooth compact modification of B.

The resolution introduces no change at the generic E image, because that image lies in the smooth blow-up chart. Pulling back the displayed Jacobian identity yields

    J_new=J_old-(c-1)m.

The new map is holomorphic on the retained smooth neighborhood, so J_new>=0. Each step with codim S>=2 strictly decreases the nonnegative integer J. Therefore the procedure terminates after at most the initial J such steps. The terminal image cannot be the whole target if the original image was proper: composition to B would otherwise make f(E)=B. Thus the terminal image is a prime divisor F.

This argument imports proper analytic blow-up, the proper mapping theorem, and resolution preserving the smooth locus. It proves its own termination and generic-lift assertions. It does not appeal to an unproved global lifting of Z or to resolution of a graph that might alter the generic E.

## Ideal orders and the ramification normal form

At a very general smooth point of E mapping to a smooth point of F, the map E->F has tangential rank d-1. This follows from dominance in characteristic zero; its critical values lie in a proper analytic subset. Write y1=0 for F. Then f'^*y1=z1^e u with e>=1 and u a holomorphic unit. Absorb a local e-th root of u into z1. Taking f'^*y2,...,f'^*yd as d-1 source coordinates gives the exact local normal form

    f'(z1,z2,...,zd,z')=(z1^e,z2,...,zd).

The extra coordinates z' may be absent. For an ideal sigma^*b of generic order a along F, one local generator has form y1^a times a unit at a generic point of F and all generators are divisible by y1^a. Pullback then has order ea along E. This proves the ideal identity. No finite generation or uniform very-general point across infinitely many ideals is required: the identity is assessed for each ideal separately.

## Lelong identity, including a residual potential infinite on F

Add a smooth local function to w composed sigma so that it is psh. Let a be its generic Lelong number along F. By divisorial Siu decomposition, locally

    w composed sigma = a log|y1|^2 + R + smooth,

where R is psh and its generic Lelong number along F is zero. Our convention is dd^c=i/(2 pi) partial barpartial, and log|y1|^2 has divisor coefficient one. The generic value zero means that the full point Lelong number of R is zero at very general points of F, after discarding the countable union of its positive Lelong level sets intersected with F. This does not require R restricted to F to be finite.

Fix such a point of F and any t>0. Skoda local integrability makes exp(-t R) locally integrable for every fixed t. In the above ramification normal form, the pushforward of smooth volume under z1->z1^e has a constant multiple of the normal weight

    |y1|^(2/e-2).

For e>1 this weight lies locally in L^p for every 1<p<e/(e-1); for e=1 it is bounded. Choose one such p. Holder's inequality and Skoda applied to tp' R imply that exp(-t R composed f') is locally integrable for every t>0. Integration in the free coordinates only contributes a bounded smooth factor on a product neighborhood.

If R composed f' had positive generic divisor coefficient a'>0 along E, its Siu decomposition would bound it above by a' log|z1|^2 plus a locally bounded-above residual psh function. The exponential exp(-t R composed f') would then be nonintegrable in the normal variable whenever t a'>=1. This contradiction proves nu(R composed f',E)=0. Hence the full pulled-back generic Lelong number is ea. The possible condition R|F identically minus infinity is handled by integrability and is not silently excluded.

In the horizontal case f(E)=B, near a very general point of E the restriction E->B is a submersion. Extend its coordinates to a source chart. The pulled-back potential depends on the base coordinates and has no divisor coefficient along the independent normal coordinate of E. Alternatively the same Skoda/submersion argument gives zero. Every ideal is a unit at a generic base point, giving order zero.

## Apply independently to every divisor in the Hopf trace problem

For n>=3 let q:H_n->P^(n-1) be the scalar Hopf elliptic bundle. Given any smooth compact modification pi:Y'->H_n and prime E on Y', the map f=q composed pi is proper and dominant. Apply the lemma to this individual E. If its image is proper it becomes a multiple e of a divisor F on one smooth compact modification of the projective base, giving both the ideal and Lelong identities above. If its image dominates the base both values are zero.

Consequently a closed-base exact trace w with nu(w composed sigma,F)=tau_B(F) on all base models pulls back to a genuine Hopf potential with simultaneous exact coefficients tau_Hn(E) on all Hopf models, provided the actual multiplier-ideal submersion identity b_t pulled back = a_t has independently been established. Taking limits of ideal orders preserves the factor e because e is fixed for the chosen E. This is a candidate extension of the current surface extraction step, not a grant of the rest of original P18.

The full invariant trace-envelope descent and ideal-type/addition/analytic-model conclusions would follow by revisiting all the surface article's other steps in dimension n-1. The finite-level actual mass formula should become 2n b times the closed-base non-pluripolar mass, and a closed-base smaller-background majorant should give the bounds

    2n b (a/2)^(n-1) <= integral MA_(a alpha+b beta)(q^*w)
                          <= 2n b a^(n-1).

These are proposed higher-dimensional applications, not yet a fully assembled or independently reviewed manuscript. The separate all-dimensional BMP candidate is needed to certify that every proposed H_n target fails bounded mass. No positive-lower-mass claim or original P18 closure is made.

## Exact new primary application

Jaroslaw Wlodarczyk, Resolution of singularities of analytic spaces, Proceedings of the 15th Gokova Geometry-Topology Conference 2008, pp.31-63, published 2009. Primary publisher PDF: https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf . Local PDF SHA256 10072416e96eec62fb3bbca78e4bc9dc9efea364b4335126a22c17416aab222a.

Theorem 2.0.1 on printed p.34 (PDF p.4) supplies exactly a proper bimeromorphic resolution which is an isomorphism on the nonsingular part. Apply it to the reduced main analytic blow-up T, not directly to the source Z. Compactness of the resolved target follows from properness over compact T. The analytic theorem applies even if T is not projective or Kahler; neither property is needed for extraction or base closed-positive-current pullback.

Root read the complete exact statements at text lines149-275; the germ statements and full resolution-principle and gluing arguments at465-746; the full displayed marked-ideal algorithm proof at1232-1575; and the full final strengthening argument at1575-1645. Actual PDF pages4,5,11,12,13,14,15,30,31 were rendered and viewed. This does not claim that all preceding lemmas in the 33-page source or all its cited premises have been recursively verified. The source resolution theorem is an explicit supporting assumption subject to native independent source review.

Demailly's proper mapping theorem, smooth-center blow-up charts, Siu divisorial decomposition and Skoda integrability are the exact already-read primary statements recorded for the frozen surface article. Their application here is new, particularly the codimension-c Jacobian decrease and the source with generic smoothness only. They need new application judgments, not automatic reuse of the surface audit's acceptance.


## Entire current seven-page working manuscript

\documentclass[11pt]{article}
\usepackage[a4paper,margin=28mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newcommand{\ddc}{dd^c}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\ord}{\operatorname{ord}}
\newcommand{\PP}{\mathbb P}
\newcommand{\I}{\mathcal I}
\newcommand{\cO}{\mathcal O}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\title{Exact intrinsic traces on scalar Hopf manifolds\newline
and unbounded mass in every dimension at least three}
\author{}
\date{}
\begin{document}
\maketitle
\noindent\textbf{Working draft.} Mathematical review, independent
reconstruction and final comparison are pending. The unrestricted
non-K\"ahler trace problem remains open.
\begin{abstract}
For every scalar Hopf manifold of dimension at least three, we extend
the original smooth Xia--Zhang threefold construction to obtain
unbounded Monge--Amp\`ere mass. An exact comparison of angularly
integrated densities supplies the extension. On these targets, ambient
potentials pulled back from projective space nevertheless have exact
intrinsic traces on every smooth compact modification. The full trace
envelope descends to a closed trace on the projective base. A finite
divisorial extraction argument works in arbitrary base dimension:
blow up each divisor image and resolve the target without changing its
smooth locus, while the order of a pulled-back top form decreases.
We prove ideal-type compatibility, addition and analytic approximation,
and compute positive finite individual masses. These conclusions treat
the specified pullback data; unrestricted non-K\"ahler exactness and
ordinary-type independence are not claimed.
\end{abstract}

We use $d^c=\frac{i}{4\pi}(\bar\partial-\partial)$ and
$\ddc=\frac{i}{2\pi}\partial\bar\partial$.
Potentials have their genuine canonical representatives.
The ideal $\I(tu)$ is defined by local integrability of
$|g|^2e^{-tu}$, with no additional factor two.
An ideal restricted to a submanifold always means its coherent image
ideal. Non-pluripolar products with nonclosed smooth backgrounds use
bounded local products with smooth corrections and truncation
\cite[Section 2.1]{BGL}.

\section{Geometry and statement}
Fix an integer $n\ge3$ and put $d=n-1$. Let
\[
 M=(\mathbb C^{n+1}\setminus\{0\})/\langle z\mapsto ez\rangle,
 \qquad
 Y=H_n=(\mathbb C^n\setminus\{0\})/\langle z\mapsto ez\rangle.
\]
The inclusion of the first $n$ coordinates identifies $Y$ with a
linear submanifold of $M$. Projectivization gives the commuting square
\[
 \begin{matrix}Y&\longrightarrow&M\\
 q\downarrow&&\downarrow p\\
 B=\PP^d&\longrightarrow&\PP^n.
 \end{matrix}
\]
Both vertical maps are holomorphic submersions with connected elliptic
fiber $E=\mathbb C/(\mathbb Z+2\pi i\mathbb Z)$.
Normalize the Fubini--Study form $\kappa$ on $B$ by
$\int_B\kappa^d=1$. On $Y$, put
\[
 r=\log\|z\|^2\pmod 2,
 \quad \alpha=q^*\kappa=\ddc r,
 \quad \beta=dr\wedge d^cr,
 \quad \Omega_{a,b}=a\alpha+b\beta \quad(a,b>0).
\]
The differential of $r$ is global. The form $\beta$ has rank one,
is positive along the fibers, and $\int_E\beta=2$.
Thus $\Omega_{a,b}$ is Hermitian, $\int_Y\Omega_{a,b}^n=2nba^d$,
and $d\Omega_{a,b}=-b\,dr\wedge\alpha\ne0$.
The target is non-K\"ahler, since its first Betti number is one.
Section~\ref{sec:bmp} proves that it fails BMP for every $n\ge3$,
using the original threefold family of \cite{XZ}.

Let $U$ be genuine quasi-psh on $\PP^n$ with $\nu(U,B)=0$,
and let $u=p^*U$. Set
\[
 \mathfrak b_t=\I(tU)\cO_B,
 \qquad \mathfrak a_t=\I(tu)\cO_Y.
\]
These image ideals are nonzero. For a prime divisor $F$ over $B$,
write
\[
 \tau_B(F)=\lim_{t\to\infty}t^{-1}\ord_F\mathfrak b_t;
\]
define $\tau_Y$ from $\mathfrak a_t$ in the same way.
For any sufficiently large background $\Theta$, let
$T_\Theta$ denote the usc supremum of all $\Theta$-psh potentials
$v\le0$ satisfying $\nu(v,F)\ge\tau(F)$ on every smooth compact
modification. The definition includes all competitors.

\begin{theorem}\label{thm:main}
There is $a_0>0$, depending on the ambient curvature bound for $U$,
such that for $a\ge a_0$ and every $b>0$,
\[
 T_{\Omega_{a,b}}(u;Y)=q^*T_{a\kappa}(U;B).
 \tag{1}
\]
For every smooth compact modification $\pi:Z\to Y$ and every prime
divisor $D$ on $Z$, simultaneously,
\[
 \nu(T_{\Omega_{a,b}}(u;Y)\circ\pi,D)=\tau_Y(D).
 \tag{2}
\]
Equality (2) also holds for the trace in any Hermitian background
$\Omega\ge\Omega_{a,b}$. In the backgrounds in (1), the trace has
positive finite individual non-pluripolar mass and
\[
 \int_Y\MA_{\Omega_{a,b}}(T_{\Omega_{a,b}})
   =2nb\int_B\MA_{a\kappa}(T_{a\kappa}),
 \qquad
 2nb(a/2)^d\le\int_Y\MA_{\Omega_{a,b}}(T_{\Omega_{a,b}})
   \le2nba^d.
 \tag{3}
\]
The ideal class of the traces in (1) is independent of $a,b$ within
this range, is additive and positively homogeneous in the ambient
ideal trace data, and admits the dyadic analytic approximation
described below.
\end{theorem}

\section{Unbounded mass in all Hopf dimensions}\label{sec:bmp}
\begin{proposition}\label{prop:bmp}
For every $n\ge3$, $H_n$ fails the bounded mass property.
There are globally smooth $V_\eta$ with
$\alpha+\beta+\ddc V_\eta>0$ and total mass tending to infinity.
\end{proposition}
\begin{proof}
Use the original Xia--Zhang family, with its original heat scale
$\varepsilon_\eta=\eta^{1/\eta^2}$, not a new transport family.
Write $\xi\in\mathbb C^d$, $x=\log|\xi|^2$,
$w=\log z_0\pmod{\mathbb Z+2\pi i\mathbb Z}$ and
$\mu=e^x/(1+e^x)$ on the projective affine chart. Then
$r=w+\bar w+\log(1+e^x)$.
There are $n-2$ angular directions orthogonal to the radial direction.
Differentiating in these directions gives the identical angular
entries $A=(\mu+V_x)/\mu$. The radial/fiber block, in the frame
of \cite[Lemma 2.2]{XZ}, is
\[
 K_V=\begin{pmatrix}
 (\mu+V_{xx})/[\mu(1-\mu)]&
 (\mu+V_{x\bar w})/\sqrt{\mu(1-\mu)}\\
 (\mu+V_{wx})/\sqrt{\mu(1-\mu)}&1+V_{w\bar w}
 \end{pmatrix}.
\]
The background block has determinant one. The differential-form
expansion contains $-(1-\mu)V_x$, but its radial contribution
cancels that of the angular prefactor, giving exactly this block.
Thus the positivity conditions in every dimension are
\[
 1+V_{w\bar w}>0,\qquad \mu+V_x>0,\qquad
 Q[V]=V_{xx}+\mu-\frac{|\mu+V_{x\bar w}|^2}{1+V_{w\bar w}}>0.
\]
The source operator is $i\partial\bar\partial$; dividing both
source background forms by $2\pi$ gives ours with the same
numerical potential and these same ratios.

Normalize angular contact measure by mass one and write $dA_E$
for Haar probability measure on the elliptic fiber. The radial
Fubini--Study density on $\PP^d$ is
$d\mu^{d-1}\mu'\,dx=d\mu^d(1-\mu)\,dx$.
Since the fiber mass is two, the angularly integrated background
volume density is $2nd\mu^d(1-\mu)\,dx\,dA_E$.
Let $J_n(V;x,w)$ denote the angularly integrated smooth
Monge--Amp\`ere density. Multiplying by $A^{n-2}\det K_V$ gives
\[
 J_n(V;x,w)=\frac{n(n-1)}6(\mu+V_x)^{n-3}J_3(V;x,w).
 \tag{7}
\]
This compares integrated densities; the angular spheres in the
different dimensions each have their own probability normalization.

The original family is $V_\eta=W_\eta+g_\eta$.
It has all three strict positivity inequalities, is independent
of $x$ at the negative end, and is one constant at the positive end
\cite[Proposition 4.1]{XZ}. These endpoint properties give the
same global smooth extension with $\xi\in\mathbb C^d$.
Its construction also gives
\[
 \begin{gathered}
 \sup[W_{\eta,x}]_-=o(1),\qquad
 -m_\eta\le g_\eta'\le0,\qquad m_\eta=o(1),\\
 g_\eta''=r_\eta-m_\eta\psi,\qquad
 \int r_\eta=m_\eta,\quad\int\psi=1.
 \end{gathered}
\]
Here $r_\eta,\psi\ge0$ and $g_\eta=0$ on $x\le-2$.
Consequently $\mu+V_{\eta,x}\ge1/4$ for $x\ge0$ and small $\eta$.

The source proves $\int J_3(V_\eta)\to\infty$. To localize this
divergence, on $x<0$ one has
$W_\eta=F_\eta(\varepsilon_\eta,w)$, with no $x$ derivatives.
Since $\int_EF_{w\bar w}\,dA_E=0$, exact fiber integration gives
\[
 \int_E J_3(V_\eta;x,w)\,dA_E
   =12(\mu+g_\eta')[g_\eta''+\mu(1-\mu)].
\]
Use $0<\mu+g_\eta'\le\mu$ and
$\int|g_\eta''|\le2m_\eta$. The total mass on $x<0$ is at most
$12\int_{-\infty}^0\mu^2(1-\mu)\,dx+24m_\eta
=3/2+24m_\eta$.
The high amplitude of $F_{w\bar w}$ has been integrated exactly;
no uniform derivative bound is needed there.
It follows that $\int_{x\ge0}J_3(V_\eta)\to\infty$.
Equation (7) now gives
\[
 \int_{H_n}(\alpha+\beta+\ddc V_\eta)^n
 \ge\frac{n(n-1)}6\,4^{-(n-3)}\int_{x\ge0}J_3(V_\eta)
 \longrightarrow\infty.
\]
Every other Hermitian form $h$ dominates $c(\alpha+\beta)$
for some $c>0$. The potentials $cV_\eta$ have strictly positive
perturbed $h$, and their smooth masses dominate $c^n$ times
the preceding divergent masses. This proves BMP failure.
\end{proof}

\section{Divisorial extraction in arbitrary dimension}
\begin{lemma}\label{lem:extract}
Let $f:Z\to B$ be a dominant holomorphic map of connected smooth
compact complex manifolds, with $\dim B=d$, and let $D$ be a prime
divisor on $Z$. Either $f(D)=B$, or there is a smooth compact
modification $\sigma:B'\to B$ such that $f$ lifts holomorphically
near generic $D$ and $D$ dominates a prime divisor $F$ on $B'$.
For an integer $e\ge1$, every nonzero coherent ideal $\mathfrak b$
and every genuine quasi-psh $w$ on $B$ satisfy
\[
 \ord_D f^*\mathfrak b=e\ord_F\sigma^*\mathfrak b,
 \qquad \nu(w\circ f,D)=e\nu(w\circ\sigma,F).
 \tag{8}
\]
In the horizontal case both orders and generic Lelong numbers are zero.
\end{lemma}
\begin{proof}
Maintain a compact analytic graph proper over $Z$ which is an
isomorphism near generic $D$, with a dominant map to a smooth
compact modified base. The graph may be singular away from this
unchanged neighborhood. The divisor image $S$ is irreducible
analytic by the proper mapping theorem
\cite[Chapter II, Theorem 8.8]{Dem}.
Near generic $D$, define $J_D(f)$ as the minimum order of the
coefficients of $f^*(dy_1\wedge\cdots\wedge dy_d)$ in a smooth
source frame. Dominance gives a finite nonnegative integer,
independent of the local smooth coordinate choices.

If $S$ has codimension $c\ge2$, blow up its reduced coherent ideal.
The blowup can be singular globally, but it is smooth over the
smooth part of $S$. There use $S=\{y_1=\cdots=y_c=0\}$ and let
$m=\min_{i\le c}\ord_D f^*y_i\ge1$.
Choose $y_1$ of least order and shrink at generic $D$ so its
leading coefficient is a unit. All ratios $f^*y_i/f^*y_1$ are
holomorphic there, giving a lift to the smooth blowup chart
\[
 (y_1,\ldots,y_c)=(s,st_2,\ldots,st_c).
\]
Take the main graph of this lift. Resolve the target blowup using
a proper resolution which is an isomorphism on its whole smooth
locus \cite[Theorem 2.0.1]{Wlo}. The new target is smooth and
compact. The lift at generic $D$ is preserved, since its image
lies in that smooth locus. Taking the main graph of the resulting
meromorphic lift again preserves the generic source neighborhood.

The smooth-center Jacobian identity is
\[
 dy_1\wedge\cdots\wedge dy_d
   =s^{c-1}ds\wedge dt_2\wedge\cdots\wedge dt_c
                  \wedge dy_{c+1}\wedge\cdots\wedge dy_d.
\]
The target resolution is locally an isomorphism here. Therefore
\[
 J_D(f_{\rm new})=J_D(f)-(c-1)m\ge0.
\]
Each step strictly decreases $J$. After finitely many steps the
image has codimension one; it cannot dominate the target if its
original image was proper. This proves extraction without a
resolution of the source graphs that might change generic $D$.
Generic ideal generators along $F$ are powers of its equation
times a unit ideal, giving the first equality in (8).

At generic smooth points, tangential dominance $D\to F$ gives
rank $d-1$. Absorb a unit into a local normal coordinate using
an $e$-th root, and use the tangential base coordinates as source
coordinates. The exact local form is
\[
 (z_1,z_2,\ldots,z_d,z')\longmapsto(z_1^e,z_2,\ldots,z_d).
\]
After a smooth local correction, divisorial Siu removal writes
$w\circ\sigma=c\log|y_1|^2+R$, with $R$ psh and generic
Lelong number zero on $F$
\cite[Chapter III, (8.15)--(8.16)]{Dem}.
At a very general point of $F$ its full point Lelong number is zero.
Skoda's lemma gives integrability of $e^{-tR}$ for each $t>0$
\cite[Lemma 5.6(a)]{DemAM}.
For $e>1$ choose $1<p<e/(e-1)$. The ramification density
$|y_1|^{2/e-2}$ lies in $L^p$, so change of variables and
H\"older, using Skoda for $tp'R$, give
\[
 \int e^{-tR(z_1^e,z_2,\ldots,z_d)}dV_z
 =C_e\int e^{-tR(y)}|y_1|^{2/e-2}dV_y<\infty.
\]
Free variables contribute a harmless product factor. For $e=1$
use Fubini. A positive generic divisor coefficient $c'$ of the
residual pullback would force nonintegrability when $tc'\ge1$.
Its coefficient is therefore zero, and the logarithm gives $ec$.
This proves the Lelong equality, including when $R|_F\equiv-\infty$.
In the horizontal case $D\to B$ is a submersion at very general
points. Skoda and Fubini give zero generic coefficient; every
nonzero ideal is generically a unit there.
\end{proof}

\section{Ideal pullback and the full envelope}
\begin{lemma}\label{lem:ideals}
For a holomorphic submersion $q$ and a genuine quasi-psh potential
$v$ on its base, $\I(tq^*v)=q^*\I(tv)$ for every real $t>0$.
In the geometry above, $\mathfrak a_t=q^*\mathfrak b_t$ and
$\nu(u,Y)=0$.
\end{lemma}
\begin{proof}
Use local product coordinates $(x,y)$. The inclusion of the extended
base ideal follows by Fubini. For the reverse inclusion expand an
integrable holomorphic germ as $g(x,y)=\sum_\gamma g_\gamma(x)y^\gamma$.
The fiber coefficient estimate for holomorphic functions bounds
$|g_\gamma(x)|^2$ by a constant times the fiber integral of $|g|^2$.
Each coefficient therefore lies in $\I(tv)$ at the selected base point.
Every finite Taylor truncation belongs to its extended ideal $J$,
so $g\in J+(y)^N$ for all $N$. Krull intersection in the Noetherian
local analytic ring modulo $J$ gives $g\in J$. Smooth corrections
do not affect integrability. Apply the result to $p$ and restrict
the ideal to $Y$. Local submersion coordinates also preserve the
generic Lelong number along the inverse image of $B$.
\end{proof}

For clarity, recall the supplied closed-target trace construction.
Choose $a\kappa$ at least twice an admissible Hermitian background on
$B$ and discard finitely many indices of the ambient analytic
regularization $U_m$. The normalized ordinary analytic models
\[
 w_j=P_{a\kappa}[U_{2^j}|_B]
\]
decrease to $w=T_{a\kappa}(U;B)$.
The trace majorant lies in $\PSH(B,a\kappa/2)$ and is below $w$.
Closed mass monotonicity and the smaller-background expansion give
$\int_B\MA_{a\kappa}(w)\ge(a/2)^d$, while the closed upper bound is
$a^d$. The decreasing positive-mass model theorem
\cite[Proposition 3.1.12]{SGPT} now gives, for every divisor $F$ over $B$,
\[
 \nu(w,F)=\lim_j\nu(w_j,F)
  =\lim_j2^{-j}\ord_F\mathfrak b_{2^j}=\tau_B(F).
 \tag{6}
\]
The model and positive-mass hypotheses are essential; arbitrary
decreasing quasi-psh convergence would not imply this equality.
The closed-target construction and analytic envelope properties are
the known trace background, rather than conclusions imported to $Y$.

\begin{proof}[Proof of Theorem \ref{thm:main}]
Apply Lemma \ref{lem:extract} to $q\circ\pi$ for every target
modification $\pi:Z\to Y$. Equations (8), (6) and Lemma
\ref{lem:ideals} give
$\nu(q^*w\circ\pi,D)=\tau_Y(D)$ for each divisor, so $q^*w$ is
an exact competitor.

The compact elliptic group acts along the fibers, preserving
$\alpha,\beta$ and every $\mathfrak a_t$. It consequently preserves
the full trace competitor family, including its constraints on all
modifications. Its usc envelope is invariant and descends to a
genuine quasi-psh potential on $B$ by local sections. For a basic
potential $q^*v$, the background inequality is equivalent to
$a\kappa+\ddc v\ge0$. Indeed wedge the background inequality
with the smooth semipositive $\beta$ and push forward by $q$.
Since $\beta^2=0$ and its fiber integral is two, the resulting
positive current is $2(a\kappa+\ddc v)$. Conversely add $b\beta\ge0$.

Every base modification $B'\to B$ lifts to the smooth compact
modification $Y\times_B B'\to Y$. The inverse image of a prime divisor
$F$ is prime, since the elliptic fibers are connected; at generic
points its multiplicity is one. Thus the descended trace envelope
satisfies every base constraint, and is at most $w$. The opposite
inequality follows from the exact competitor $q^*w$. This proves
(1) and (2). For $\Omega\ge\Omega_{a,b}$ the same exact competitor
lies below $T_\Omega$, so
$\tau_Y(D)\le\nu(T_\Omega,D)\le\nu(q^*w,D)=\tau_Y(D)$.

For $v_j=\max(v,-j)$ on the base, actual bounded local products give
\[
 (\Omega_{a,b}+\ddc q^*v_j)^n
   =nb\,\beta\wedge q^*(a\kappa+\ddc v_j)^d,
\]
since the horizontal current has rank at most $d$ and $\beta^2=0$.
Multiply by $\mathbf1_{\{v>-j\}}$ and pass to the non-pluripolar
limit. Integrating over the fibers gives the factor $2nb$ in (3).
The closed-base bounds above give its two inequalities.
These are individual masses, not extremal volumes of all ordinary
representatives.

Different sufficiently large base backgrounds produce potentials
with the same numbers (6); the closed K\"ahler ideal criterion
\cite[Proposition 3.2.1]{SGPT} gives the same ideals at every real
weight. Lemma \ref{lem:ideals} transfers this to (1).
Intrinsic trace data are additive and positively homogeneous.
On the base, the sum of two exact realizers has the sum of their
divisorial numbers. The same criterion identifies its ideal class
with the trace for $U_1+U_2$, in a background with sufficient
curvature room. Positive scaling is identical. Pull back to $Y$.
This uses the ideal criterion on the projective base, and does not
assume a global valuative criterion on an arbitrary non-K\"ahler target.
\end{proof}

\section{Approximation and a point trace}
For the dyadic $w_j$ above, put $v_j=q^*w_j$. Compact elliptic
invariance applied to the full ordinary obstacle envelopes shows,
for $h\in\PSH(B,a\kappa)$,
\[
 P_{\Omega_{a,b}}[q^*h]=q^*P_{a\kappa}[h].
\]
At each finite obstacle level the competitor family is invariant;
its full supremum descends, and ordinary order is equivalent on
the base by surjectivity. Thus $v_j$ are the full ordinary analytic
models of the pulled-back restricted approximants. They decrease
to (1) in $L^1(Y)$: decreasing quasi-psh convergence is genuine,
or one can integrate a fixed invariant volume along the fibers.
For every divisor $D$ over $Y$, (6) and (8) yield
\[
 \nu(v_j,D)\longrightarrow\tau_Y(D).
\]
The same potentials pulled back to any target modification converge
in $L^1$ there, by quasi-psh compactness and uniqueness off the
exceptional set. This assertion supplies no convergence theorem
for extremal non-K\"ahler singularity volumes or capacities.

A concrete trace involving exceptional divisors is obtained from
\[
 U([z_0:\cdots:z_n])
  =\log\frac{\sum_{i=0}^{n-2}|z_i|^2}{\sum_{i=0}^{n}|z_i|^2},
 \qquad B=\{z_n=0\}.
\]
Its generic number along $B$ is zero, and its restricted image
ideals are
\[
 \mathfrak b_t=\mathfrak m_P^{\max(\lfloor t-d+1\rfloor,0)},
 \qquad P=[0:\cdots:0:1]\in B.
\]
The formula follows from the normal radial integrability condition
$k>t-d$ in $d$ normal coordinates to the ambient singular line.
Consequently $\tau_Y(D)=\ord_Dq^*\mathfrak m_P$ on every model.
The genuine potential $q^*(U|_B)$ is an explicit exact realizer,
singular along the elliptic fiber over $P$. For $a>1$,
\[
 \int_Y\MA_{\Omega_{a,b}}(q^*(U|_B))=2nb(a^d-1).
\]
On the point blowup the horizontal current, after removing the
exceptional divisor $F$, has class $aH-F$ and smooth semipositive
representative $(a-1)\sigma^*\kappa+\eta$. Here $\eta$ is the
pullback of the Fubini--Study form by the resolved projection to
$\PP^{d-1}$. The mixed intersections of $H$ and $F$ vanish,
$H^d=1$ and $F^d=(-1)^{d-1}$, giving $(aH-F)^d=a^d-1$.
Its smooth product off $F$ is the pullback of the actual
non-pluripolar product, and a smooth measure charges no divisor.
The displayed potential need not equal the normalized trace envelope.

\begin{remark}
The theorem treats arbitrary genuine ambient $U$ with the stated
generic condition, including nonanalytic data and cases where
$U|_B$ is identically $-\infty$; image ideals, not naive restriction,
define the trace. The base has arbitrary dimension $d\ge2$. No finite selection
of exceptional divisors replaces the simultaneous constraint.
Ideal-type compatibility is asserted for the invariant backgrounds
in (1). Exactness in larger arbitrary backgrounds follows by the
sandwich argument, but ordinary-type independence is not claimed.
\end{remark}

\begin{thebibliography}{9}
\bibitem{BGL} S. Boucksom, V. Guedj and C. H. Lu,
\emph{Volumes of Bott--Chern classes}, arXiv:2406.01090.
\bibitem{Dem} J.-P. Demailly, \emph{Complex Analytic and Differential
Geometry}, Harvard-hosted June 2012 manuscript.
\bibitem{DemAM} J.-P. Demailly, \emph{Analytic Methods in Algebraic
Geometry}, Surveys of Modern Mathematics 1, 2012.
\bibitem{SGPT} M. Xia, \emph{Singularities in global pluripotential
theory}, lecture manuscript, July 18, 2026 version,
\url{https://mingchenxia.github.io/Lectures/SGPT_final.pdf}.
\bibitem{Wlo} J. W\l{}odarczyk,
\emph{Resolution of singularities of analytic spaces},
Proceedings of the 15th G\"okova Geometry--Topology Conference
(2008), 31--63, published 2009,
\url{https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf}.
\bibitem{XZ} M. Xia and K. Zhang,
\emph{A counterexample to the bounded mass property},
arXiv:2608.21053v1.
\end{thebibliography}
\end{document}


## Whole root primary application audit, not an independent acceptance

{
  "created_utc": "2026-10-05T08:57:11.208665+00:00",
  "status": "root-primary-applications-assessed-native-gates-pending",
  "article_source": "papers/P18-Hopf-all-dimensions-exact-projective-traces.tex",
  "article_source_sha256": "151c057261d563a73ade3ce0b56b9b434d64d0d9a2ae61861f64aded27c5c422",
  "article_entire_root_read": true,
  "all_seven_actual_pdf_pages_viewed": true,
  "notes_entire_root_read": true,
  "native_mathematics_started": false,
  "independent_mathematical_acceptance": false,
  "original_fully_closed": false,
  "publication_called": false,
  "frozen_surface_input_hashes_unchanged": {
    "papers/P18-Hopf-threefold-exact-surface-traces.tex": "2fea6343489bf45080f8fcf14e9a98492b459ade346cf8e06849e9e75a98a9f3",
    "notes/P18-Hopf-surface-native-full-review-argument.md": "03a75fd10cc8ec0d002b56c0eb1f43a1b404e14a26caf54c1df29ef1f87ed89c",
    "inputs/P18-Hopf-surface-native-blind-reconstruction-input.json": "23971239a9f48cfe96a9165d1cfa25ca312c6735d626bf1864278bc9bfd95b86"
  },
  "new_resolution_application": {
    "source_url": "https://gokovagt.org/proceedings/2008/ggt08-wlodarczyk.pdf",
    "source": "inputs/primary/Wlodarczyk-resolution-analytic-2009.pdf",
    "sha256": "10072416e96eec62fb3bbca78e4bc9dc9efea364b4335126a22c17416aab222a",
    "exact_statement": "Theorem 2.0.1, printed34/PDF4: proper bimeromorphic resolution is an isomorphism on the entire nonsingular part.",
    "whole_text_ranges_read": [
      [
        149,
        275
      ],
      [
        465,
        746
      ],
      [
        1232,
        1575
      ],
      [
        1575,
        1645
      ]
    ],
    "actual_pages_viewed": [
      4,
      5,
      11,
      12,
      13,
      14,
      15,
      30,
      31
    ],
    "application": "Resolve the reduced main blow-up of the target image. It is compact and smooth over generic smooth center. Properness preserves compactness; preservation of the smooth locus preserves the generic divisor lift. Source graph resolution is not assumed.",
    "root_new_jacobian_calculation": "J_new=J_old-(codim S-1)*min ord_D(f^*I_S); nonnegative J proves finite termination.",
    "recursive_verification_of_all_source_dependencies": false
  },
  "new_all_dimensional_mass_application": {
    "source": "inputs/primary/Xia-Zhang-2608.21053v1.pdf",
    "sha256": "0c39d024097dae97940403328cf6f8fb39fe3e21270edd02449948ea17303baa",
    "source_operator": "i partial barpartial = 2pi ours; divide source background by2pi, preserve numerical potentials.",
    "whole_text_ranges_read_this_application": [
      [
        1,
        126
      ],
      [
        215,
        320
      ],
      [
        600,
        875
      ]
    ],
    "source_entire_902_line_text_read_prior_unchanged": true,
    "actual_pages_fresh_viewed": [
      4,
      5,
      10,
      11,
      12
    ],
    "application": "Use unchanged original smooth heat family and original epsilon=eta^(1/eta^2), endpoint charts, strict three scalar inequalities, sup negative Wx=o(1), correction derivative [-m,0] and integral |gpp|<=2m.",
    "root_new_calculations": [
      "n-2 identical angular entries and unchanged 2x2 block",
      "Normalized radial FS density d mu^d(1-mu)",
      "Jn=n(n-1)/6*(mu+Vx)^(n-3)*J3",
      "Exact negative-side fiber average12(mu+gp)[gpp+mu(1-mu)] and total<=3/2+24m",
      "Positive-side lower bound mu+Vx>=1/4 yields divergence every n>=3"
    ],
    "uses_unaccepted_S02_new_heat_scale": false
  },
  "reassessed_other_primary_applications": [
    "Demailly proper mapping applies to each compact analytic graph and its strict divisor; smooth-center charts give exact codimension-c Jacobian factor.",
    "Siu generic/divisorial removal and Skoda zero-point-Lelong integrability apply in any dimension; Holder normal ramification weight is Lp for1<p<e/(e-1), with free variables integrated by Fubini.",
    "Closed-base SGPT3.1.12 decreasing ordinary models have positive actual closed mass from the smaller-background majorant in arbitrary dimension d. Each modified divisor is assessed separately.",
    "Closed Kahler base SGPT3.2.1 gives equality of ideals at every real weight. Actual submersion ideal identity pulls this to the Hopf target; no unrestricted non-Kahler valuative criterion is imported.",
    "BGL Section2.1 bounded locality and smooth-background corrections suffice at each truncation. Horizontal degree d and beta square zero give nb times pullback mass, fiber integral2; no BMP-dependent unbounded theorem used.",
    "Point blowup class aH-F has top intersection a^d-1. Ambient codimension-d integrability gives the exact real-weight image ideal exponents."
  ],
  "primary_bytes_and_old_exact_locators": "checks/P18-Hopf-surface-root-primary-application.pending.json; old source bytes and statements reused only, no automatic new mathematical acceptance.",
  "all_primary_premises_recursively_certified": false
}


## Pure statement-only reconstruction targets

# P18 general-dimensional scoped statement-only targets A--F

Retain every convention and the exact original task. These are requested
conclusions, not granted lemmas, source judgments or author proof steps.
The unrestricted original remains open; independently judge scoped adequacy.

A. For each integer n>=3 the scalar Hopf manifold
H_n=(C^n\{0})/<z->ez> fails BMP: for every Hermitian h there are
globally smooth real potentials with h+dd^c V>0 and total mass tending
to infinity. Verify the actual higher-dimensional positivity and mass,
using indispensable ordinary primary literature independently. The original
threefold theorem may be used only after exact source application checking.
No new heat-scale construction, pending S02 result or mere dimension analogy
is granted.

B. If f:Z->B is a dominant holomorphic map of connected smooth compact
complex manifolds of arbitrary base dimension d>=1 and D is a prime source
divisor, either f(D)=B and all nonzero coherent base ideal pullback orders
and genuine quasi-psh generic pullback Lelong numbers are zero, or there is
a smooth compact modification sigma:B'->B and a prime divisor F on B',
dominated by D under a holomorphic lift near generic D, and an integer e>=1
such that for every nonzero coherent ideal b and every genuine quasi-psh w,
ord_D(f^*b)=e ord_F(sigma^*b) and
nu(w composed f,D)=e nu(w composed sigma,F).
Prove existence, finiteness, all compact analytic auxiliary identifications
and both identities, including residual potentials infinite on F. No
extraction argument, termination invariant or finite-family shortcut is
granted. Any indispensable resolution or proper-mapping theorem requires
exact independent primary application verification.

C. Fix n>=3,d=n-1, M=H_(n+1), Y=H_n linearly embedded as the first
n coordinates. Projectivization gives p:M->P^n and q:Y->B=P^d,
where B is the linear hyperplane z_n=0. For any genuine quasi-psh U on
P^n with nu(U,B)=0, put u=p^*U. Prove nu(u,Y)=0 and
I(tu)O_Y=q^*(I(tU)O_B) for every real t>0, using actual image ideals.
Prove the submersion multiplier-ideal identity at every real weight.

D. Normalize kappa=FS on B by integral kappa^d=1, and set
r=log||z||^2 modulo two, alpha=q^*kappa, beta=dr wedge d^c r,
Omega_(a,b)=a alpha+b beta. Prove that there is a0 depending on ambient
curvature room such that for all a>=a0 and b>0 the FULL intrinsic envelope
T_Omega(u;Y)=q^*T_(a kappa)(U;B), and its generic Lelong numbers equal
every intrinsic tau_(Y,u)(D) on every smooth compact target modification.
Exactness also holds in every Hermitian Omega>=Omega_(a,b). Verify every
competitor and every exceptional divisor, not only selected modifications.
The targets are genuinely non-Kahler and fail BMP by A.

E. In the invariant backgrounds in D, prove positive finite INDIVIDUAL
trace mass, the actual formula integral_Y MA_Omega(T)=
2nb integral_B MA_(a kappa)(T_base), and bounds
2nb(a/2)^d<=integral_Y MA_Omega(T)<=2nb a^d.
Prove independence of the IDEAL class across these large invariant
backgrounds, addition and positive homogeneity with appropriate curvature
room. Prove full ordinary obstacle-envelope pullback for basic potentials,
and full dyadic restricted analytic model approximants decreasing in L1
on Y and every modification, whose generic Lelong numbers converge to
each intrinsic order. Do not infer ordinary-type independence or extremal
ordinary singularity volumes from these individual masses. Do not apply
a BMP-dependent unbounded product theorem on a target failing BMP.

F. For U=log(sum_(i=0)^(n-2)|z_i|^2 / sum_(i=0)^n|z_i|^2) on P^n
and B={z_n=0}, prove the image ideals are
b_t=m_P^max(floor(t-d+1),0), P=[0:...:0:1] in B, and the profile on Y
is ord_D(q^*m_P) for every prime divisor on every target modification.
The genuine potential q^*(U|B) is an exact realizer with actual mass
2nb(a^d-1) for a>1. Equality of this potential with the normalized full
trace envelope is not requested.

Independently verify all indispensable primary claims and each application.
Produce full ordinary proof notes with valid earlier-note support references
and retain all genuine gaps. The requested model is gpt-6.1-sol xhigh.

