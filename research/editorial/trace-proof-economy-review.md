# Reusing the divisorial comparison in the trace chapter

Focused primary-agent review for checkpoint72, based on checkpoint71 commit d060cc92acdcfc200b1b05bdbc7efdaf850be189. This is a proof-exposition revision, with no new mathematical result or independent Rethlas run.

## Scope and change

The current pass rereads chapter_trace_data.tex and its five nested inputs: section_curve_trace_metric.tex, section_trace_additivity.tex, section_trace_envelope.tex, section_curve_fibration_traces.tex and section_trace_product_measures.tex. It checks their real-parameter image-ideal limits, curve measures and equations, exact fibration realization, envelope inequalities and the distinction between ordinary and ideal types. This bounded reread is not a new verification of all standard local and source-book inputs.

The lemma comparing a potential with a finite-mass divisorial singularity was previously introduced only in the fibration section. Two earlier curve arguments repeated its current-removal proof. The revision moves the entire lemma, proof and smooth-residual qualification to one shared input before the curve construction. The source block is unchanged, including the countable-component case. Its prerequisites are only previously stated local ideal and current facts; it does not depend on any of the subsequent curve or fibration results.

In the curve approximation proposition, the naive trace comparison gives nu(a,p)>=tau(p), and the Green representative has dd^c w=D_u-D_u(Y) eta. The shared lemma therefore gives a preceq w directly. The analytic equality argument remains. In the curve-envelope comparison, the same lemma identifies the pointwise trace constraints with ordinary domination by w, yielding the same exact competitor family. The ordinary/ideal envelope identity and the existing I-goodness input are retained. The fibration theorem continues to use the lemma in its original way.

The curve equation's necessity and uniqueness proof deliberately keeps its bounded residual argument. That step proves that the residual measure gives polar sets zero mass; an ordinary-domination assertion alone would not justify its removal. The submersion multiplier-ideal proof, including its finite-module Krull argument, is unchanged. Numerical additivity, exact special-case realization, and the unproved general higher-dimensional realization remain distinct.

## Direct checks

The two reused applications satisfy every hypothesis: their Green potential is quasi-plurisubharmonic, its positive divisorial current is the finite atomic trace measure, and its residual term is smooth. On the curve the relevant divisors are points. Empty trace data also fits the argument with the zero divisorial current. The resulting inequalities concern canonical ordinary types and not subtraction at common poles; the unchanged shared proof already supplies the almost-everywhere-to-everywhere passage.

All 14 pre-existing complete formal statement blocks are preserved across the four files together. Every label remains, and the complete moved lemma/proof/qualification has a recorded hash and one copy in the new input. Both shortened applications have explicit references to this preceding result, so no circular or forward proof dependency is introduced. The moved result's references in later chapters are included in the output review. No verifier memory, report or frozen input was edited; the 162 historical reports keep their individual scopes.

The house audit has zero errors and one inherited chapter-label warning. The book compiles without errors, undefined references, duplicate labels or overfull boxes; the inherited bibliography underfull paragraph remains. The selected contents, trace pages and later cross-reference pages were rendered and read. Exact counts, hashes, preservation and visual scope are in build-snapshot-72.json and trace-proof-economy-map.json. Empty-directory reconstruction is recorded in source-package-portability-72.json. Original sources, checkpoint71, its archive and the companion note remain preserved.

## Continuing questions

No mass property, geometric condition or equation hypothesis is added or removed. The construction of an exact trace for arbitrary higher-dimensional data, compatibility among sufficiently large backgrounds beyond the proved cases, and the comparison with a general Hermitian singularity topology remain open here. Continue reviewing the book and these proof boundaries after publication.
