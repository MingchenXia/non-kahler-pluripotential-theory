# General theory and separate mass assumptions

Checkpoint85 implements the user's request to hide the former Chapter 30 and to separate the substantial theory requiring uniform mass properties. This is a structural and exposition revision, not a new mathematical result. The reversible source map preserves the full before/after text and hashes against checkpoint84.

## Retained general theory

Chapter 12 keeps extended upper/lower volumes and the relative envelope class. The stretching, difference-envelope, finite-rooftop and smaller-background arguments have section-local assumptions: semipositive big background and an ordinary model reference admitting a smaller-background envelope. They do not assume a positive uniform lower mass. The lower estimate can be zero, while its individual positivity assertion is proved separately. Infinite-mass examples in the envelope class remain alongside these general constructions.

Chapter 13 keeps ordinary-type Lp equations, individual-density subsolutions, exponential approximation and the characterization/failure of universal normalized solvability. Both measure representations were moved here: the bounded potential carrier and the prescribed ordinary-type carrier. Their statements require no uniform mass property. The second may have an infinite reference measure. Neither representation asserts a bounded density or solves an arbitrary-measure equation. The Cegrell local class notation is distinguished from the global envelope class, and the relocated proof is cited by its stable label.

## The separated part

Chapter 30 contains finite singularity volumes, their monotonicity/addition, the volume-defined relative class and its comparison with the envelope class. The definition formerly containing both classes is split; its two displayed defining formulas are unchanged. Positive lower reference volume remains explicit in the reverse implication. The bounded-mass model-reference condition and conditional volume characterization of ideal-envelope equality follow. The latter retains its relative-class and positive-volume assumptions. Its problem and the warning about an unproved triangle inequality remain.

Chapter 31 assumes semipositive big theta, the smaller-background model condition and positive lower mass; it permits infinite upper mass. Its domination and compactness arguments distinguish finite auxiliary measures from potentially infinite measures of the original potentials. The general-measure theorem and its later proofs are now in the same chapter. The analytic nonuniqueness example still distinguishes scalar uniqueness from potential uniqueness.

Chapter 32 assumes bounded mass, a smooth big background and positive lower model-reference volume. These imply metric positive lower mass by the retained volume comparison, rather than enlarge Li's theorem by silently dropping a condition. The existing relative projection, weighted addition, general-measure existence and Lp ordinary-type proofs remain. The three-regime comparison at the end explicitly uses each regime's own assumptions; its first regime requires neither uniform mass property. That first theorem is already proved in the main sequence.

## Hidden chapter and preserved history

The former Nakamaye chapter and its two input files are excluded from the active inclusion graph and are byte-for-byte unchanged. Active cross-references promising those proofs are removed from the preface, Bott–Chern loci chapter and research chapter. The ordinary loci definitions and classical nef result remain, as does the separately checked strongly Gauduchon criterion in the LCK chapter. The private Popovici working reference is not integrated. Historical review files and old chapter numbers are preserved in Git and audit records.

## Review scope

The source comparison checks 147 unchanged formal blocks, including all retained proofs in the 17 changed files after two explicitly recorded notation/navigation normalizations. One old definition becomes two with identical formulas. All remaining changes are driver structure, headings, assumptions restated in new locations, cross-references, explanatory prose and page-break control. No verifier run was started for this reorganization; the existing 171 reports retain their previous scopes. This review does not independently recertify their mathematics.

The primary review checked the scope of every moved section, the main/conditional distinction, stable-label references, definition order and the chapter-level hypotheses. The second exposition pass shortened the preface, merged two adjacent volume subsections and corrected orphan headings and split statements. The house audit retains three pre-existing driver-macro errors under the user-requested original-template exception. Its 31 warnings comprise the previous 28 and three new chapter/part-prefix warnings; the script's paper-oriented prefix list does not include the book's established chapter/part labels. No new mathematical environment or notation is introduced.

Final build, visual coverage, source preservation, exact production/preview equality and portable reconstruction are recorded in `research/audits/build-snapshot-85.json` and `research/audits/source-package-portability-85.json`. The research remains incomplete.
