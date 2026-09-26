# Chapter 30 rewrite — checkpoint136

Baseline: `d0b2c09d73af8581cab4f21be446d6ce267c66ed` (checkpoint135).

## Complete chapter scope

The chapter and all eight nested inputs were read in full before editing and twice after revision. The second revised read followed the first full build and inspection of all forty selected pages. The nine inputs are:

- `chapter_relative_finite_measures.tex`
- `section_relative_extended_domination.tex`
- `section_dominated_relative_compactness.tex`
- `section_exponential_rooftop_barrier.tex`
- `section_relative_moving_measures.tex`
- `section_general_measure_minimal.tex`
- `section_positive_lower_mass_threshold.tex`
- `section_general_measure_relative.tex`
- `section_analytic_example_fullmass.tex`

The chapter has ten sections and one subsection, with no figure inputs. All nine files are edited. Its introductions now explain the progression from domination through relative compactness to general-measure existence. The chapter setting, relative class notation, smooth volume, capacity metric and uniform lower mass bound are declared once. Repeated definitions of the class, stretching envelopes, singularity order and lower mass are replaced by internal references. The extended-measure section has a mathematical title. General psh compactness, almost-everywhere order, monotone capacity convergence and fixed/moving integration inputs are referenced from Chapter 1.

The finite-measure exponential corollary is merged into the existing extended-measure corollary; its label remains as an alias. All labels are preserved. The finite-measure domination theorem remains before the zero-domination lemma, which applies it only after proving the auxiliary envelope has finite mass. There is no circular use of extended domination in that proof. The chapter has fourteen formal blocks and fourteen proof environments after the merge, down from fifteen each; four formal blocks and one proof environment are byte-identical. The remaining changes concern setup, notation, internal dependencies and exposition, not additional theorem strength.

## Mathematical read

Both direct reads checked all fourteen retained proofs, including the following points:

- Subtraction of extended measures is first performed on common finite truncation levels. The finite-measure comparison argument obtains coefficient-one contact domination before using small tails.
- The zero-domination argument constructs a finite auxiliary measure in the scaled background and verifies its positive lower mass before applying finite domination. Its final limit uses a convex competitor as the background coefficient tends to one.
- The common-envelope extraction is made once. Its finite-prefix and infinite-tail construction supplies every stretching condition for the same extracted sequence; the prefix is not silently discarded separately for each parameter.
- Weighted lower semicontinuity and zero domination identify the increasing rooftop limit. Fixed domination then supplies uniform raw tails. The moving-measure proof combines a uniform bounded-reference capacity estimate with the fixed non-pluripolar measure's tails.
- The exponential barrier proposition retains both alternatives: positive lower mass, or ordinary reference type of every approximant. The latter uses the earlier smaller-background comparison theorem and does not require uniform ordinary-type constants or convergence of the bounded carrier potentials.
- Minimal-class solutions compare from above with the prescribed-reference approximants by using reference zero. The proof does not assume those approximants are more singular than the comparison solution. In the zero-exponent step only an upper bound on that solution is used; the normalization scalars retain an explicit positive lower bound.
- Positive exponents determine a unique potential. At exponent zero the comparison proof determines the scalar only. The projective examples have two smooth normalized solutions, and their boundedness puts them in the minimal envelope class.

The first revised read corrected the missing name for the fixed smooth volume and a local variable after removing repeated setup. The second read corrected two display-ending punctuation marks; the corrected paragraphs were reread. No new theorem, independent verifier run, supplied-paper integration or Popovici result is claimed.

## Source and dependency scope

The primary source is the exact ALS26 version `https://arxiv.org/pdf/2511.02339v1`, 549323 bytes, SHA-256 `c7e1eb6d0665af711dc1469609f0f8b0ff1fdf3121576c32a844270f4b54496b`. The copy downloaded and verified in checkpoint135 was reused and rehashed; it still matches the archived source manifest. This checkpoint does not claim a new publication-status search or a new source-PDF visual inspection.

Direct source-text reads cover Theorems 3.11 and 3.14, Lemma 3.12, Corollaries 3.13 and 3.15, Theorem 4.1 and Lemmas 4.2–4.3, and Theorem 5.8 and Corollary 5.9, with their complete proofs. The source's finite-mass statements are distinguished from the book's existing extended-measure proofs. The book retains its explicit prefix/tail repair in the extraction argument. Existing provenance paragraphs in the historical chapter were checked at the relevant bounded locations; no historical source citation changes were needed.

Internal dependency reads include the complete fixed-measure integration, bounded-carrier, bounded-subsolution, relative compactness and psh compactness inputs. Targeted complete statements/proofs were read for monotone capacity convergence, bounded-reference trace convergence, raw-tail continuity and its smooth-background extension, the relative difference envelope and relative uniform mass lower bound. The prescribed ordinary-type existence theorem and the analytic-density nonuniqueness theorem were checked at statement level; their complete longer proof chains are retained from previous chapter reviews, not represented as freshly reread here. The positive-threshold corollary uses the existing individual-density theory and its explicit internal references.

All non-book citations remain in final Chapter 33. The body uses the earlier general results through internal references. Historical reports, inactive Nakamaye sources and automation settings are preserved.

## Release checks

The house audit has zero errors and one inherited label warning, down from two warnings. Non-book citation placement passes. The final book has 786 pages, with no build errors, unresolved references/citations, duplicate labels or overfull boxes. One inherited bibliography underfull paragraph remains. All 40 selected final pages passed visual inspection: front matter, contents and conventions, complete Chapter 30 with neighboring transitions, and the complete bibliography. The seventeen-page companion is byte-identical to checkpoint135. Both PDFs rebuild from a fresh empty source-package extraction, with every page text matching production. The active book has 33 chapters and 211 author inputs; all 190 historical verifier reports and three hidden sources remain unchanged. Exact hashes and checks are in build-snapshot-136.json; the portability audit is source-package-portability-136.json.

Thirty-eight final rendered images are byte-identical to the inspected first pass; the two punctuation-changed pages were reinspected. Both queues continue at Chapter 31. The whole-book goal remains active and incomplete.
