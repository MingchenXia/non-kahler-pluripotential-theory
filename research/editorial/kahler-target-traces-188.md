# Exact traces on Kahler submanifolds — checkpoint188

Baseline: `a453dd438cca5ffebc429ff06e42150dae6449cc`. Checkpoint187 was completed and privately synchronized; the preceding goal turn was progress. The checkout was clean when this unit began.

## Mathematical change

Theorem 18.6.3 realizes all trace numbers on every smooth compact modification when the submanifold Y is Kahler. The ambient compact complex manifold and its smooth background may be non-Kahler and nonclosed. Choose a Hermitian form Omega0 above the restricted ambient background, then a Kahler form kappa at least twice Omega0. Every Hermitian background Omega at least kappa has the asserted exact trace numbers.

The restricted analytic approximants eventually belong to PSH(Y,kappa). Their dyadic ordinary model envelopes decrease to the trace envelope by the preceding restricted-envelope theorem. The normalized majorant lies below that envelope in the half-sized background. The smaller-background mass lemma and Stokes give positive closed mass. The retained classical closed model-continuity theorem then gives convergence of each divisorial Lelong number to the prescribed asymptotic restricted ideal order. For Omega above kappa, the exact kappa-envelope is a competitor, supplying the upper Lelong bound; the defining trace constraints supply the reverse bound.

This does not give exactness in an arbitrary original restricted background, ordinary-type independence under arbitrary background changes, or general non-Kahler realization. Chapter 32 narrows the remaining exact-realization problem accordingly. The second revised pass shortens the closing hypothesis sentence and removes the repeated envelope-order proof at the opening of the curve-fibration section.

## Review and source scope

All seven Chapter 18 inputs received an original read and two complete direct revised mathematical/editorial reads. The second revised read followed the first build and visual inspection. Chapter 32's trace-realization section and adjacent transition, Chapter 33 Section 33.11 and its transition, and the existing DDNL21 bibliography entry received bounded reads. These are direct scoped reviews, not a new independent verifier run or a whole-book proof audit.

All eighteen prior Chapter 18 formal blocks and proofs remain, and one theorem/proof is added. All 38 prior labels remain, and the new theorem adds one. Four Chapter 18 nested inputs are unchanged. Only five author inputs change. Problem 32.8.1 is narrowed to a non-Kahler target; every other Chapter 32 formal statement is unchanged. The bibliography adds the house label to its existing DDNL21 entry, with no new entry. Paper attribution remains in Chapter 33; the body cites the book SGPT.

The new retained classical input is SGPT Proposition 3.1.12. Its complete statement and proof on printed pages 96--97 were read from the local PDF identified in the audit. The complete statement and proof of [Darvas--Xia Proposition 2.1, version 2](https://arxiv.org/html/2403.08259v2) were also checked; Lemmas 3.2, 3.3 and 3.9 were read in bounded source comparison. [DDNL Lemmas 4.3 and 4.4, preprint version 1](https://arxiv.org/pdf/1909.00839), pages 14--16, were read with their proofs. Their closed hypotheses remain in force. Earlier classical dependencies retain their accepted scope; this is not a full fresh audit of the dependency chain or of any entire source. No novelty claim or Popovici reliance is introduced. All supplied-paper integrations, including Q8.2 in Sections 14.8--14.10, retain their existing records. No new author correction requires a skill change.

## Release checks

Both production outputs build. The book has 817 pages and the companion seventeen; the companion is byte-identical to checkpoint187. Final engine logs have no errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph remains. The house audit has zero errors and 26 warnings: 25 are reproduced by the baseline audit, and one concerns the newly cited DX24 preprint. Its exact v2 was checked and is retained without a claim about a published successor.

The first visual selection contains 64 pages: 32 changed images directly inspected through eight contact sheets and 32 identical to the inspected checkpoint187 render. The final selection contains 64 pages: eight changed images directly inspected through two contact sheets and 56 identical to the first inspected render. It covers the complete Chapter 18 and transitions, bounded Chapter 32/33 interfaces, contents and all other changed body pages. The graph remains 33 chapters and 221 author inputs.

Both outputs rebuild from a fresh empty source-package extraction, and every page text agrees with production. The final package manuscript and build scripts match that rebuilt payload. All 221 active author inputs are included. The 190 historical verifier reports and three hidden Nakamaye sources remain unchanged; the hidden sources remain excluded. See build-snapshot-188.json and source-package-portability-188.json.

## Continuation

Investigate a quantitative upper-volume-deficit bound for divisorial Lelong numbers in Chapter 29 and its conditional application to non-Kahler trace realization; keep upper-volume continuity as a separate unproved obligation. A possible route is the existing contact-envelope collapse argument with a representative whose mass is near its upper volume. This is a candidate for the next unit, not a new manuscript theorem. Positive actual model mass alone must not be substituted for positive lower volume, and contact-measure convergence does not by itself prove upper-volume continuity in a nonclosed background. The broader goal remains active and incomplete.
