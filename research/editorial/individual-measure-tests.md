# Smooth comparison tests for an individual right-hand side

**Update, 22 September 2026:** the positivity question for smooth tests below has a negative answer in the supplement integrated as Section13.23 of checkpoint39. Its bounded audit `individual_density_subsolutions_01` passed. Bounded truncation constants instead give an exact attained threshold for scaled subsolutions. The original note is retained below as research history; its first remaining question is no longer open. Exact threshold equations and geometric interpretations remain separate.

21 September 2026. Research note, not integrated into the book and not independently audited. The short deductions below use checkpoint30 Lemma13.22.1. The possible converse is a question, not a theorem or a claim of novelty.

Fix a Hermitian form h and a smooth positive probability volume dV. For a smooth strictly positive probability density g, write c_h(g) for the scalar of the normalized smooth equation MA_h(v)=c_h(g)g dV. For a measurable probability density f with f>=m>0 almost everywhere, define

    C_h^sm(f) = inf_g c_h(g) ||g/f||_L∞,

where the infimum runs over those smooth probability densities. Every ratio is finite because f has a positive essential lower bound. The value can be zero, and is at most c_h(1)/m. Since ||g/f||∞>=1 for probability densities, C_h^sm(f)>=v_-(h).

## A necessary condition without any candidate mass bound

If MA_h^ext(u)>=a f dV for a genuine h-psh u and a>0, then a<=C_h^sm(f).

Indeed, put R=||g/f||∞. The measure inequality f dV>=R^-1 g dV gives MA_h^ext(u)>=(a/R)g dV. The audited smooth-normalizer lemma gives a/R<=c_h(g). Take the infimum over g. The proof permits infinite extended mass of u.

For smooth strictly positive f, equality C_h^sm(f)=c_h(f) follows: its smooth solution gives the lower inequality, and the test g=f gives the upper one. For the diagonal density of Theorem13.22.1, f>=2^-j f_j and c_h(f_j)<=2^-2j, so C_h^sm(f)<=2^j c_h(f_j)<=2^-j for every j. Thus the necessary invariant detects that example exactly as zero.

If F is that diagonal probability density, then f_t=(1-t)g+tF satisfies C_h^sm(f_t)<=t^-1 C_h^sm(F)=0 for any probability density g and 0<t<1. These zero values are therefore L1 dense when v_-(h)=0. In particular this functional is not lower semicontinuous for the L1 topology: its values on smooth positive g are positive.

## The test does not recover the scalar for every bounded density

Already on a compact Kähler manifold with Kähler form h, let V=integral h^n and choose a closed nowhere dense measurable set K of smooth volume p with 0<p<1. Such a set is supplied by a positive-measure nowhere dense set in a coordinate chart. Put

    f = (1+1_K)/(1+p).

Then f is a probability density bounded above and below. Its normalized equation has scalar V by the usual closed-background mass identity, and a bounded solution exists by the classical Lp theorem.

But C_h^sm(f)=V(1+p). To prove this, first c_h(g)=V for every smooth probability g. If R=||g/f||∞, then g<=R/(1+p) almost everywhere on the open dense complement of K. Continuity gives that bound at every point of this open set, and then on all of X by density. Integrating g gives R>=1+p. The constant test g=1 attains R=1+p. Therefore the invariant is strictly larger than the actual scalar, although f is bounded and its equation is solvable.

The failure of sharpness comes from asking a smooth function to be pointwise dominated by an irregular density. Consequently the smooth-test formula must not be asserted as an extension of the equation scalar to arbitrary L1 data.

## Precise remaining questions

- If f>=m>0 is a probability density and C_h^sm(f)>0, does a normalized solution exist? Even the existence of some positive scaled subsolution from this test bound alone has not been proved here. The Kähler example above refutes equality with the scalar, but does not refute this positivity criterion.
- For a positive lower semicontinuous L1 density with smooth increasing approximants, what extra compactness hypothesis converts a positive lower bound for their normalization constants into a normalized limiting solution? The lower-mass argument supplies necessity. L1 compactness of potentials alone is insufficient for passage of the nonlinear measures.
- Does the Gauduchon quotient formula have an appropriate extension to such individual measures? One must separately justify mixed inequalities and the relation between coefficient determinants and extended non-pluripolar measures; equality cannot be silently assumed for unbounded potentials.

Do not replace the current book's open individual-measure problem by an unproved sufficiency assertion. This note provides a concrete necessary test and a counterexample to its proposed sharpness, for a later bounded review.
