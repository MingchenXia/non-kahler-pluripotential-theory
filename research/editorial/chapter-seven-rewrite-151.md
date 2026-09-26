# Chapter 7 rewrite — checkpoint151

Baseline: `91e33be03a4a01bb833768e9e72e803daf9dbea4` (checked checkpoint150).

## Scope and reads

The complete chapter consists of `chapter_damped_measures.tex` and its sole nested input `section_general_damping_weights.tex`. The original read recorded during checkpoint150 was revalidated against both source hashes, and both original files were read again before editing. Both complete revised files received a first mathematical/editorial read, a build and visual inspection, and a second direct mathematical/editorial read. Subsequent bounded wording and layout changes were reread at their changed interfaces. No other author file is edited or claimed as newly reviewed in full.

The consulted foundations are the local cutoff and weighted capacity-continuity statements in Chapter 1, exact bounded regularization, the smooth top-wedge cancellation in Chapter 2, the Gauduchon trace bound in Chapter 4 and the infinite/prescribed-mass constructions in Chapter 6. These are dependency checks within this chapter's revision, not a new recursive audit of those chapters. The two installed writing skills continue to apply; the existing rules cover this consolidation, and no new author intervention requires a skill change.

## Mathematical and editorial changes

Six sections replace the previous seven. The stronger range estimate absorbs the unused weaker estimate and its repeated local setup. A single restricted-mass lemma gives both the polynomial bound and the finite-depth capacity bound. The exponential transform retains its own explicit capacity constant; its mass and capacity conclusions share one theorem.

The general decreasing-weight criterion precedes its polynomial and logarithmic applications and incorporates capacity continuity. The old general-weight and damped-continuity labels name this same theorem. There is one layer-cake proof and one finite-level weighted identity. The bounded weighted continuity is used directly from Chapter 1, instead of repeating the general exceptional-set argument. The same cutoff then proves finite limiting mass and undamped weak convergence under uniform tails. The integrability argument distinguishes a continuous function of the depth from its quasi-continuous composition with a potential. The total-variation convention is not declared again.

All sixteen original labels are retained. The weaker range label and separate exponential-capacity label remain aliases of the stronger results. No downstream caller needs a stronger hypothesis, and non-book source attribution remains in Chapter 33. This revision introduces no new external result, bibliographic locator, Popovici dependency or independent verifier run.

## Mathematical checks

The local first Hessian mass is uniformly controlled by the global trace; each subsequent cutoff costs one range factor. Smooth cancellation followed by exact bounded regularization gives the zero top exact wedge for bounded potentials. Positivity of the mixed masses gives exponent `max(n-2,0)`, including dimensions one and two. The finite-depth restriction uses truncation at `-t-1`, strictly below the set on which locality is applied; rescaling by `1+t` gives the exact capacity factor.

The weight condition is explicitly an assumption on `B_w(0)`. Tonelli is valid for the sigma-finite extended measure, the level zero is included, and the pole set has zero measure. The cutoff vanishes exactly at the truncation value. Its bounded quasi-continuous coefficients converge in capacity, so Chapter 1 applies. Uniform tails permit the second limit. The polynomial threshold `q>r_n`, capacity exponent `(q-r_n)/(q+n-r_n)`, exponential tail bound and critical logarithmic threshold `a>1` are retained. In dimensions at most two the criterion is `B_w(T)=w(T)`.

For undamped convergence, uniform tails first bound total mass; increasing compact cutoffs prove finiteness of the limiting measure before they are removed. Increasing integrability weights give tails by Markov's inequality, and locally finite ramps prove the converse for an arbitrary family. The projective-line example has zero extended limiting measure but unit full current mass. In the smooth mass-defect example the positive volume lower bound and exponential damping give total-variation convergence at every fixed depth; a common weak subsequence leaves the prescribed excess mass in every tail. No support or polar-character conclusion for that defect is inferred.

For a general smooth background, a Hermitian majorant supplies mass and capacity bounds. At a fixed level the signed product expansion is treated term by term by Chapter 1 capacity continuity, and the vanishing cutoff gives the restricted positive measure. The proof does not assume that constant truncation preserves positivity in the original background.

## Release checks

The two changed author inputs have zero house-audit errors and one inherited label warning. Non-book citations remain in Chapter 33. The 804-page book and seventeen-page companion compile without unresolved references/citations, duplicate labels or overfull boxes; the inherited bibliography underfull paragraph remains. All 45 selected final pages pass visual review, with 8 changed images directly inspected and 37 byte-identical to inspected first-output images. Both outputs rebuild from a fresh empty source-package extraction, with every page text matching production. There are 33 active chapters and 216 author inputs; all 190 historical verifier reports and three hidden sources remain unchanged. Exact scopes are recorded in chapter-seven-rewrite-151.md, build-snapshot-151.json and source-package-portability-151.json.

The first selection had 45 pages: 34 were directly inspected on 9 sheets and 11 were byte-identical to the checked checkpoint150 output. Layout adjustments keep the exponential definition together, reduce the excessive reservation before the logarithmic application, keep the finite-level limit with its lead-in, and keep section openings with their first content. The logarithmic measure is written inline where its separate display split the sentence. A redundant introduction before the smooth defect corollary is removed. The final visual scope covers the complete Chapter 7 and its transitions, front matter and contents, and every other changed body page matched within its chapter while ignoring shifted running page numbers. The last layout refresh changed seven previously inspected images; all seven were reinspected directly. All sixteen original labels remain, with three pairs absorbed into shared statements. The companion is byte-identical to checkpoint144. The final package manuscript and build payloads match those rebuilt; later changes affect only research documentation. Routine private synchronization follows the checks.

## Continuation

Continue with the complete present Chapter 8, then Chapter 9 and its nested inputs. The broader writing and research goal remains active and incomplete.
