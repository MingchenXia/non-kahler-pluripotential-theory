# Primitive line bundles and lower Monge--Ampère mass

Working direction, 22 September 2026. This is an unintegrated primary-agent calculation and a proposed next test family. It has not received a bounded verifier run or a complete literature audit. No novelty or globally open status is claimed. It uses no additional result of Popovici.

## Geometric setup

Let (B,eta) be a connected compact Kähler surface. Let L be a holomorphic line bundle such that

\[
 \int_B c_1(L)\wedge\eta=0.
\]

Choose a smooth Hermitian metric on L whose curvature is eta-primitive. This is obtained from any metric by the scalar Poisson equation: its curvature trace has mean zero, so a smooth metric change cancels that trace. Fix a real q>1 and form

\[
 X=L^\times/\langle v\mapsto qv\rangle,\qquad \pi:X\to B.
\]

The action is free and properly discontinuous. In a local line-bundle trivialization the quotient is the product with the elliptic curve C^*/q^Z; compactness of the base and fiber makes X compact. The transition maps are holomorphic fiber multiplications. Let t=log|v|^2 for the chosen bundle metric. Although t changes by 2 log q under the deck action, its differentials a=dt and b=d^c t descend. Use the book normalization d^c=i/(4 pi)(bar-partial minus partial), and write

\[
 db=dd^c t=\pi^*c,\qquad \eta\wedge c=0,
 \qquad D=a\wedge b,\qquad \omega=\pi^*\eta+D.
\]

Here c is the negative of the chosen Chern curvature; its sign will not affect the square below. The real form D is semipositive of rank one, positive on the vertical complex line. Thus omega is Hermitian. All formulas use forms on X after descent, even where t itself is only locally defined.

## Calculations to verify in a focused run

Since da=0, d^c a=-pi^*c and d^c b=0, the exterior algebra gives

\[
 D^2=0,\qquad dD=-a\wedge\pi^*c,
 \qquad dd^cD=-\pi^*(c^2).
\]

The primitivity condition therefore yields

\[
 d(\omega^2)=0,\qquad dd^c\omega=-\pi^*(c^2)\geq0.
\]

For the sign, diagonalize the real primitive (1,1)-form c against eta at a point of the surface. Its two eigenvalues are lambda and -lambda, so c^2=-lambda^2 eta^2. This is a pointwise calculation; no cohomological positivity inference is substituted for it.

In a logarithmic fiber coordinate z=x+iy, one has t=2x+constant, D=(1/pi) dx wedge dy, and the real periods are log q and 2 pi. Consequently

\[
 \int_E D=2\log q,\qquad
 V:=\int_X\omega^3=6\log q\int_B\eta^2.
\]

The book's smooth threefold mass identity would then give, for every smooth real u,

\[
 \int_X(\omega+dd^c u)^3
 =V-3\int_Xdu\wedge d^cu\wedge\bigl(-\pi^*c^2\bigr).
\]

The last integral is nonnegative. Thus v_+(omega)=V, first over smooth admissible potentials and then over bounded ones by the existing exact-background regularization. This is a direct special calculation, not a new general bounded-mass criterion.

If c is nonzero, S=-pi^*(c^2) is a nonzero smooth semipositive dd^c-exact (2,2)-form. Pairing S against a hypothetical pluriclosed metric gives a contradiction by Stokes. Pairing it against a closed positive current dominating a Hermitian form similarly excludes a closed Kähler current. These are the same full-current and smooth-form pairings already used for the supplied elliptic example; they do not involve a singular nonlinear product. If c=0, omega is closed and the construction is instead Kähler.

## Question and cautions

For a nonzero primitive Chern class, determine whether v_-(omega) vanishes. The supplied P^1 x P^1 example with opposite line-bundle degrees is one affirmative instance. The calculations above prove only an upper mass bound; they do not give a sequence attaining the maximal allowed Dirichlet energy. Equivalently, zero lower mass would require smooth admissible u_j with

\[
 \int_Xdu_j\wedge d^cu_j\wedge S\longrightarrow V/3.
\]

The fixed-density Gauduchon dual gives a second route: construct normalized positive ddc-closed (2,2)-forms whose determinant measures violate the critical L^(3/2) bound. The known rational-curve/deck-translate argument cannot simply be transferred to an arbitrary base. First test a Kähler surface with a nonzero primitive line-bundle class but without the two rulings used by the supplied example.

When c has no zeros, the same positivity and Stokes calculation forces every closed positive (1,1)-current to have zero vertical coefficients, so the earlier local product descent proof should apply. If c vanishes somewhere, this calculation only controls the complement of its zero set; one must not silently discard possible current mass there. This is a separate issue from the lower-mass problem.

The strongly Gauduchon current-mass estimate gives linear compactness on this balanced family. It does not bound the determinant roots of the positive ddc-closed (2,2)-tests just described. Keeping these bidegrees and equations separate is essential.

## Literature boundary

The primary author-hosted published version of Angella--Guedj--Lu, [Plurisigned Hermitian metrics](https://www.math.univ-toulouse.fr/~guedj/fichierspdf/TAMS22.pdf), was consulted. Theorem2.2 gives upper mass bounds from dd^c omega>=0 in dimension three. Section4.2 records balanced pluripositive invariant metrics on the Iwasawa manifold. These statements do not settle the proposed lower-mass question. The 2023 paper's universal mass questions predate the counterexamples already reconstructed in this book.

The next literature check should identify the precise relation of this line-bundle quotient with existing balanced elliptic-bundle constructions. Do not identify every principal elliptic bundle, every Fu--Yau construction, or every nilmanifold with this one-curvature model. The proof, normalizations and scope of the proposed family need a focused check before manuscript integration.
