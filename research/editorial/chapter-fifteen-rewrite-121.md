# Chapter 15 rewrite — checkpoint121

Baseline: `902dc385df3b3851884af5ea45837f1aded5f045`. The complete chapter and all three recursively nested inputs receive two direct mathematical/editorial reads. The second statement-to-proof pass follows the first rendered chapter inspection. All four inputs are edited. No independent agent or verifier is run.

## Architecture and notation

The chapter is now titled *Multiplier-ideal envelopes and I-goodness*. Its seven sections and two subsections separate the Kähler characterization, ideal projection and calculus, dependence of envelope mass on the background, infinite-mass envelope equality, the ideal L1 metric and its completion, dyadic envelope limits, and the remaining topology problem. The analytic-envelope proposition precedes its curve and scalar applications. The scalar-normalization examples are grouped beside the metric comparison rather than interrupting the approximation proof.

Repeated definitions of the ordinary order, ideal order, multiplier ideals, minimal envelope and normalized compact family are removed. General psh facts stay in Chapter 1; almost-everywhere order and local ideal calculus are used through internal references. This checkpoint does not add general psh results outside Chapter 1 or move specialized ideal-envelope theory into the foundations. The general setting and smooth probability volume are fixed once, with explicit changes to curves, semipositive big backgrounds and Kähler backgrounds where required. Ordinary equivalence uses the existing first-chapter symbol. The existence of a chosen potential supplies each envelope's nonempty competitor family; no blanket nonemptiness assumption is imposed on arbitrary backgrounds. Paper citations remain in Chapter 33.

## Mathematical review

The ideal projection proof fixes a point and a weight before applying increasing-limit strong openness, with one common smooth local correction. Maxima stay within the ideal class. Once the regularized supremum is in that class, it is an actual competitor, proving the pointwise supremum assertion and idempotence. Ordinary-envelope comparison, scaling, addition and smooth-gauge bounds retain their exact hypotheses. The finite envelope mass remains restricted to semipositive big backgrounds; its infinite-mass representative counterexample remains distinct.

For analytic singularities, local ideal dominance supplies ordinary domination, proving equality of the two envelopes and preservation of analytic type with bounded remainder. The Green-potential proof now explicitly requires the comparison potential to be theta-psh. Its prescribed atoms exhaust the curvature mass, so harmonic uniqueness identifies the envelope. Rational finite atomic approximation and normalized compactness identify the entire completion. The positive-mass example has mass tau and converges in the ideal metric to zero, whose mass is one; its mass does not converge. The introduction no longer describes this upward jump as loss of mass. Removing the atomic part gives the asserted weak limit tau times theta. The ordered source distance remains the strictly positive constant (1-tau)/2.

One scope correction is substantive: the scalar-distance example previously declared theta to be an arbitrary smooth closed big form, but the cited Chapter 14 functional/formula is established for semipositive big backgrounds and its displayed closed formula assumes theta Kähler. The example now assumes theta Kähler. The argument does not establish the former arbitrary-big assertion. Its projective Fubini–Study examples and sharp comparison constant retain their full conclusions. No theorem extending the scalar construction to arbitrary prescribed singularities in a nonsemipositive big background is inferred from the minimal-type selection theorem.

The dyadic argument retains a fixed auxiliary Hermitian metric, decreasing errors, multiplier-ideal analytic types and the original lower bound. Subadditivity orders the types; decreasing backgrounds order the envelopes. Divisorial error estimates recover every local ideal of the limit. The chosen regularization's L1 convergence is now stated before the fixed-background rescaling argument uses it. The dyadic-envelope limit itself still holds for all the displayed admissible types; it does not need an unstated mass convergence hypothesis. Rational curvature errors make the rescaled analytic coefficients rational. The final problem remains open and is not claimed solved by universal density in the ideal metric.

## Sources and direct-review scope

The supplied SGPT source tree is now at `/Users/mingchen/Downloads/Singularities_in_global_pluripotential_theory_Final/`; the older manifest spells that directory with spaces. Its `chapter_Igood.tex`, `chapter_comp.tex` and `chapter_envelopes.tex` each match the historical manifest SHA-256 exactly. The manifest is preserved as historical evidence. Relevant statements/proofs were checked in those files and the matching local `/Users/mingchen/Downloads/SGPT_final.pdf`:

- Proposition 3.2.10, analytic-envelope type; PDF physical page 143.
- Lemma 6.2.2, ordered singularity-distance formula; PDF physical pages 224–225. This replaces the vague chapter-level locator in Chapter 15.
- Theorem 7.1.1 and its implication (3) to (1), Step 1; PDF physical pages 250–252.

These are targeted local book-source checks, not a fresh publication-status or whole-source audit. Chapter 1 local ideals, analytic regularization, divisorial estimates, normalized compactness, almost-everywhere order and envelope inputs were checked as dependencies. Chapter 14's scalar setting/closed formula and the later curve distance formula were checked at their uses. No whole-chapter certification is claimed for those dependencies in this checkpoint.

## Release checks

All 19 formal statements, including the final problem, retain their labels; 12 are byte-identical to the baseline. There are 15 proof environments, of which 8 are byte-identical. The scalar-example scope correction and the explicit admissibility condition in the curve proof are recorded above; the remaining differences concern notation, dependencies and exposition.

The house audit retains zero errors and two inherited label-prefix warnings. Non-book citation placement passes. The final book has 794 pages, with no build errors, unresolved references/citations, duplicate labels or overfull boxes. One inherited bibliography underfull paragraph remains. All 38 selected final pages passed visual inspection: front matter and contents, conventions, complete Chapter 15 and its transition pages, and the complete bibliography. The statement/proof and section-opening page breaks were adjusted and reinspected. The seventeen-page companion is byte-identical to checkpoint120. Both PDFs rebuild from a fresh empty source-package extraction, with every page text matching production. The active book has 33 chapters and 211 author inputs. Exact hashes and checks are in build-snapshot-121.json and source-package-portability-121.json. All 190 historical verifier reports and three hidden sources remain unchanged.

Both whole-chapter queues proceed to Chapter 16 and all its nested inputs. The broader writing and research goal remains active and incomplete.
