# Bounded regularization in the nefness proofs

Focused primary-agent review for checkpoint74. This revision reuses a previously proved bounded regularization proposition and changes no result statement. No new Rethlas run is claimed.

## Dependency and hypotheses

Chapter5's bounded almost-regularization proposition applies to any smooth real background beta and any bounded beta-plurisubharmonic potential v. For any chosen Hermitian metric gamma it gives smooth v_j and positive epsilon_j tending to zero with beta+ddc(v_j)>=-epsilon_j gamma. Closedness, positive top-degree mass and BMP are absent from that proposition.

For the closed-current lemma in Chapter24, R=beta+ddc(v) is closed, so beta is closed as well. Every approximating smooth form therefore represents the same Bott--Chern class. Given epsilon>0, one index with epsilon_j<=epsilon gives the defining nef estimate. This directly proves the existing conclusion and replaces the longer appeal to the construction of analytic regularization with unit multiplier ideals. No smoothness of an unspecified bounded analytic remainder is needed.

For the analytic residual class in Chapter25, the potential on a log resolution is bounded after subtracting the logarithmic divisor potential with chosen smooth divisor metrics. The same Chapter5 proposition applies to its generally nonclosed smooth background beta. Every approximating representative has exactly the same exterior derivative pi* d(theta), since d ddc(v_j)=0. It therefore remains in the required affine class. This replaces the old instruction to repeat the unit-ideal proof from Chapter24, which would otherwise become an obsolete reference after the first edit.

These are two applications of one existing estimate. In the first case closedness supplies a Bott--Chern class; in the second case the prescribed derivative supplies the affine class. Boundedness of the residual potential remains essential to both applications. The general singular-potential approximation later in Chapter25 still changes the background by a small smooth error. The revision does not solve fixed-derivative nef approximation for arbitrary singularities.

## Reread and boundaries

The current pass reads Chapter24 and its four nested inputs (including the nested divisorial-type corollary), Chapter25 and its affine-difference input, and Chapter26 and its boundary example. It rereads the full Chapter5 proof needed for this simplification and checks the later residual-nef use in Chapter30. The Chapter30 statement retains its Kähler assumptions; its extra positive-class conclusion is not extended to a nonclosed background.

The modelwise linear mass estimate, scalar Gauduchon representatives, continuity of closed-current pullback and countable divisorial summation keep their fixed-model and fixed-metric hypotheses. Exceptional differences remain finite effective divisors and their total-variation limit does not require monotonicity. Their vanishing characterizes pullback of the canonical divisorial ordinary types, not existence of every exact trace potential. The nonclosed classes retain their specified derivative. The envelope-system retraction retains its left-constant curves and its ideal-preservation criterion; the ruled-surface example continues to distinguish positive background from positive residual volume. No nonlinear volume statement is inferred from these linear constructions.

This bounded review does not reconstruct all classical local current theory, log resolution or the original book. Their previously recorded inputs retain their stated scopes. All original mathematical source files and verifier records are preserved.

## Checks

All existing formal result statements and labels in the edited files are unchanged. The reversible source map records both proof replacements. The house audit, build, page inspection, output hashes and clean source reconstruction are recorded in build-snapshot-74.json and source-package-portability-74.json. Original sources, checkpoint73 book and archive, and the companion note are preserved. This remains a research manuscript; continue improvement and research after publication.
