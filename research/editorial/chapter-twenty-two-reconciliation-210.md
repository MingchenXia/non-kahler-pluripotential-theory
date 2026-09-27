# Divisorial currents and intrinsic trace envelopes — checkpoint210

Baseline: `bcfeee326e8879e7c22cf693fb9e7eeb390bde6e`. This continues the live chapter revision queue after the whole-book Introduction and index update.

## Complete chapter revision

Chapter 22 now uses the intrinsic trace envelope as the canonical common majorant on every modification. The opening distinguishes divisorial currents visible on one model from the full trace inequalities on all models. The common-majorant proof uses Chapter 18 instead of repeating its compactness argument. The constant-trace representative proof uses the normalized Green inverse from Chapter 5, with its top-degree datum and normalization explicit. The exceptional-divisor discussion gives the residual-current identity in the closed-background case and explains why its correction is compatible with exact pullback of the full trace envelope.

All four recursive Chapter 22 inputs, including every proof, receive a complete original read and two complete revised mathematical/editorial reads; the second follows the first build and visual inspection. Of sixteen statement/example/definition environments, fifteen are unchanged after removing index commands and spacing. The ordinary-type corollary now explicitly chooses current decompositions with smooth closed residual forms: its smooth-difference conclusion concerns those potentials, while its ordinary-type comparison is independent of that choice. Eleven of fourteen proofs are unchanged after the same normalization; three have simplified or clarified dependencies. All 28 previous labels remain and one section label is added. The eight-section structure remains, with Section 22.3 retitled. Chapter 27 changes only two nonprinting index commands; its mathematics and all other author inputs, bibliography and active input graph remain unchanged.

The index now has 255 entries in 115 author inputs: 251 clickable page locators and four alternate-term cross-references. Nine locators are added for Chapter 22 constructions, and the nef and pseudoeffective definition locators move from the later Chapter 27 reminder to their first definitions in Chapter 22. All page links and labeled locators pass checks; the new statement locators also match the actual printed statement openings. The historical checkpoint209 index map is preserved, with the current map recorded separately.

## Mathematical review scope

The four files are chapter_divisorial_models.tex, section_bott_chern_bclasses.tex, section_continuous_bc_representatives.tex and section_trace_exceptional_divisors.tex. The review checks the finite-subsum Gauduchon bound, countable current construction, coefficientwise and trace-mass limits, pushforward compatibility, common trace-envelope majorant, Bott–Chern current quotient and pairings, self-trace identification, nef Cartier realization, constant-trace representatives, continuity of closed positive pullback, countable divisorial pullback, exceptional cocycle, ordinary-type comparison and both final examples.

The majorant is the envelope in the original restricted background, with all-model inequalities. Its pullback identity does not imply exact prescribed Lelong numbers in general. The positive residual-current formula R_Z'=g*R_Z-[E_g] is stated only for closed theta, where the positive closed pullback construction applies. A nonzero exceptional correction remains compatible with exact trace realization, as shown by the existing isolated logarithmic pole and its non-BMP product example.

The second read makes the Green operator input explicit as the top-degree distribution (sigma_gamma(T)-c_T) gamma^n, normalized by gamma^n/V_gamma. It retains the elliptic-symbol argument, finite-dimensional smooth representatives, L1 continuity and linear mass bound. No new general psh theorem is introduced or relocated.

Internal dependency reads include the complete Chapter 18 trace-envelope input; the complete Chapter 1 divisorial-potential domination and ordinary-type inputs; the complete Chapter 23 exceptional affine-difference input; and the Chapter 5 trace homeomorphism and Green construction. Bounded reads cover the Chapter 18 setup, Chapter 1 modification descent and L1 pullback statements/proofs, Chapter 21 closing toric argument, Chapter 23 opening and affine setup, Chapter 27 positivity reminder, and the Chapter 32 trace-realization question. These are the actual interface scopes, not fresh whole-chapter reviews of those chapters. Existing book citations are retained; no external source is newly verified and no independent verifier run is claimed.

## Checks and continuation

The 878-page book and seventeen-page companion compile without errors, unresolved references/citations, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph and template warning remain. The complete-chapter house audit has zero errors and one inherited label warning. MakeIndex accepts all 255 entries without rejection or warning. The final 53 selected pages pass visual review: 8 changed or newly selected images directly inspected and 45 byte-identical to the inspected preceding stage. The first review inspects 23 images and the intermediate review 14. The companion is byte-identical to checkpoint209. The book retains 33 active chapters and 225 active author inputs.

The first visual pass identifies the stranded Section 22.4 opening and final example, the split theorem lead-in, and an index anchor before its printed corollary. The second identifies two display splits caused by repagination. Local spacing fixes resolve these; the final index is inspected in full through direct or byte-identical carried images. Definition locators are at the actual defining paragraphs.

Both outputs rebuild from a fresh empty source extraction with identical page text. The 190 historical verifier reports and three hidden sources are unchanged; hidden sources and original supplied papers are excluded from the archive.

Review and rewrite the complete two-input Chapter 23, checking affine classes with prescribed exterior derivative, residual trace classes and exceptional translations against the intrinsic trace-envelope construction, while preserving the distinction between numerical compatibility and realization of an ordinary singularity type.

The broader writing and research goal remains active and incomplete. The existing book-writing skill already covers these changes and receives no timestamp-only update.
