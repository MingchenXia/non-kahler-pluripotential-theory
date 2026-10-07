# Checkpoint 528 — Oeljeklaus–Toma manifolds: a new direction

Date: 6 October 2026. Branch: `claude/friendly-fermi-jzw1o1`.

## Request

After the presentation revision (checkpoint 527), the author asked for free exploration of research directions that fit the book's theme and are not yet in the literature: “修改完成后，你也可以尝试探索与本书主题相关的其他方向，看看有什么可以加入本书的内容，你可以自由发挥。注意要探索目前里文献没有，但和本书主题契合的新研究问题。”

## Choice of direction

The book tests its theory on Hopf manifolds, Calabi–Eckmann manifolds, elliptic threefolds, tori, Kummer surfaces and blowup families. It does not cover Inoue surfaces or their higher-dimensional analogues, the Oeljeklaus–Toma (OT) manifolds. These are compact non-Kähler manifolds with few or no subvarieties; they carry a closed semipositive form whose kernel is a foliation by complex affine spaces.

Literature check (abstract or text level, as indicated):
- Fang–Tosatti–Weinkove–Zheng (J. Funct. Anal. 2016), Section 2 read: T³-fibration, dense leaves, Liouville argument for bounded harmonic functions on leaves, Tricerri metric, `Ric(ω_T) = −α`. No classification of α-psh functions.
- Angella–Guedj–Lu (TAMS 2023), introduction and Theorems A–D read: plurisigned criteria for `v_+ < ∞` and `v_- > 0` in dimension three, Problem 1.8; no OT manifolds.
- Angella–Dubickas–Otiman–Stelzig (Publ. Mat. 2024), Corollary 3 read: pluriclosed metrics exist only if `s = t`.
- Ornea–Verbitsky (MRL 2011), abstract and statement: OT manifolds with `t = 1` have no positive-dimensional subvarieties.
- Oeljeklaus–Toma (AIF 2005), abstract and metadata.
- Xuan Li, arXiv:2601.13446: abstract only; no OT examples.

No source found treats the pluripotential questions below.

## Added to the book (Section 27.19, Problems 32.3.6–32.3.7)

Results with complete proofs in the book:

1. `lem:ot-real-density`: the real embeddings of `O_K` (or of any full lattice `L ⊂ K`) are dense in `R^s` when `t ≥ 1` (trace form and Dedekind independence).
2. `thm:ot-transverse-potentials`: `PSH(X,θ)` consists exactly of the functions `f(y) + Σ log y_j` with `f` convex and satisfying the unit automorphy; in particular every θ-psh function is continuous.
3. `cor:ot-no-singular-potentials`: one ordinary singularity type, zero Lelong numbers, trivial multiplier ideals, vanishing Monge–Ampère measures; θ is nef and not big.
4. Inoue example: a closed positive current in `c_1^{BC}(K)` with continuous potential, supported on a single Levi-flat 3-torus.
5. `cor:ot-finite-lelong`: for `t = 1` and any smooth background, Lelong upper level sets are finite and multiplier ideals have finite colength (Ornea–Verbitsky + Siu + Skoda).
6. `prop:ot-threefold-mass` (type (2,1)), for the natural Gauduchon metric `ω = θ + y₁y₂ dd^c|z|²`:
   - the exact quadratic mass identity `M(u) = ∫ω³ + (3/16π³)∫Re(∂_{w1}u ∂̄_{w2}u) dV₀`;
   - on fiber-invariant potentials, `M(u) = (∫ω³/|T|)∫PQ`, with explicit positive upper and lower bounds;
   - smooth potentials with masses on both sides of `∫ω³`, so `v_- < ∫ω³ < v_+`;
   - the fiber-average decomposition `M(u) = M(Au) + F(u − Au)`.
7. `prop:ot-no-plurisigned`: OT manifolds of type `(s,1)`, `s ≥ 2`, carry no Hermitian metric whose `dd^c` is semipositive or seminegative on 2-planes. The plurisigned criteria of Angella–Guedj–Lu therefore do not apply.

New problems:

- `qu:ot-bounded-mass`: bounded mass and positive lower mass on OT threefolds of type (2,1), reduced to the fluctuation term.
- `qu:foliated-rigidity`: continuity of θ-psh functions for closed semipositive forms with Liouville null leaves whose closures have real codimension equal to the rank.

## Checks

- Constants checked by an independent exterior-algebra computation, and by a numerical test of the mass identity for an x-, y- and z-dependent function (agreement to 2·10⁻⁶ relative).
- A first independent referee read found four errors and three gaps in the framing. All were corrected: the problem equivalences, the rigidity hypothesis, the description of the plurisigned criteria, the scope of the Inoue surfaces, and the missing justifications.
- A second independent referee read of the revised text found no errors. It found one gap: properness of the Lelong level sets in `cor:ot-finite-lelong`, now fixed by the pluripolarity of `{u = −∞}`. It also raised minor points (Skoda source, freeness and cocompactness for general lattices, validity of the corollary for all Inoue surfaces); all are addressed.
- The final full build is clean: 1514 physical / 1486 printed pages, no errors, no overfull boxes and no undefined references. The citation-placement check passes.
- Published to the homepage in website commit c7aba05, with the remote blobs verified.

The novelty statements are limited to the literature search recorded above; no claim of priority is made in the book.
