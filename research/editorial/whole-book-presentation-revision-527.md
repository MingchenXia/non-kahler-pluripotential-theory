# Checkpoint 527 — Whole-book presentation revision

Date: 6 October 2026. Branch: `claude/friendly-fermi-jzw1o1` (cloud session); `main` is not changed by this checkpoint.

## Request

The author asked (6 October 2026): “请你对全书做一轮修改，重点放在presentation上，要确保书的presentation像一个正常教材该有的样子。不要语言僵硬或者有未经声明的非标准记号。确保结果正确无误。每次全书编译后按照repo的要求推送到主页。” A follow-up the same day asks, after the revision, for exploration of new research directions that fit the book and are not in the literature.

## What was revised

Every active unit was read and revised line by line: the Introduction, Conventions, Chapters 1–33, the problems chapter, the historical notes and Appendix A (350 files of `book/author/`). The hidden Nakamaye files, the template, `preamble.tex` and `references.bib` are unchanged. The work was split by disjoint file ranges among twenty revision passes that followed one common guide derived from the standing rules in `PLAN.md` and the book-writing skill.

- **Prose.** Telegraphic chains of short sentences became connected arguments; long proofs received a one-line plan or *Step* markers; statements were made self-contained, with commentary moved outside them; workflow vocabulary (verified, integrated, retained, recorded, actual, supplied, the author, internal research labels) was removed from the reader-facing text.
- **Openings.** Each Part now has an entry in its first chapter's opening (Parts III–IX had none); chapter and section openings state the problem, the construction and the mechanism.
- **Notation and terminology.**
  - The undefined working term “genuine” (about 250 uses, meaning “not identically −∞”) is replaced throughout by standard wording.
  - Terms used book-wide but previously undefined now have one definition each, with cross-references elsewhere:
    - complete pluripolar set, generic Lelong number, ideal order/ideal type, rooftop envelope for obstacles;
    - ordinary model (= envelope fixed point = model potential), extended non-pluripolar measure and the `⟨·⟩` notation;
    - lower/upper mass and the abbreviation BMP;
    - balanced and pluriclosed metrics (`def:balanced-pluriclosed`);
    - threshold subsolution/solution, normalization scalar, root functional, Gauduchon variational volume and root volume;
    - least smooth convexity index;
    - selecting potential, selected space, quotient equilibrium measure.
  - Imported notation is recalled with `\cref` at its first use in each chapter.
  - Local symbol clashes were removed by renaming auxiliary letters inside proofs.
- **Front matter.** The Conventions end with a one-page table of frequently used notation linked to the definitions (`book.tex` now loads the standard `array` package for it).
- **Consistency.** American spelling (disk, fiber, neighborhood, center), “nonclosed”, and `\mathbb P` for projective space. Label, reference and citation keys are unchanged.

## Mathematical corrections

All of these are local; none changes a theorem's scope.

- `ex:divisorial-sobolev-endpoint`: the shrinking condition must be `log|f| < −2` with `A = −1`, as the setup requires `χ ∈ C²((−∞, A])`.
- Tail modulus estimate (`section_exponential_tail_modulus.tex`): the root norm includes its `L^n` part, so the factor is `1 + C_s`.
- Cuspidal products: the operator display was missing its argument (`∂∂̄ w`).
- `cor:metric-pvp-minimal-volume`: the undefined “positive volume property” is replaced by positive lower mass `v_-(ω) > 0`, which is exactly what the proof uses; the conclusion `vol(V_θ) > 0` is stated.
- `lem:ball-smooth-dirichlet` is stated for a smooth positive density `F`; later sections already used this generalization of the cited Guan–Li theorem.
- Rooftops with more than two arguments are written `P_θ(min{…})`.
- “positive of rank q−1” corrected to “semipositive of rank q−1” (Hopf point envelope); an inaccurate “cross terms vanish” replaced by the exact identity (normalized kernel stability).
- Sign in the Hessian of the parallelizable cone metric (`−log λ`, differentiated twice).
- Strict Griffiths positivity quantified over `v ≠ 0`.
- `thm:gaud-trace-homeomorphism`: the single-point case now states `PSH(X,θ) ≠ ∅`, replacing the chapter's standing nonemptiness assumption.
- Lelong numbers of restricted analytic approximants attributed to the analytic-type calculus (`thm:trace-divisorial-current-budget`).
- The vanishing variational volume of the Hopf hyperplane class, previously asserted without argument, now has an explicit Gauduchon test computation (`γ_t = α + tζ`, quotient `O(t^{1/3})`).
- A missing classical input (convergence in capacity of bounded monotone sequences) is recalled in Section 1.6.

## Checks performed

1. Each revision pass ran a single-chapter compile check and a math-diff of its files against `dfb285d` (labels, references, citations, index entries and math segments).
2. Book-wide audit against `dfb285d`:
   - no label, reference target or citation was removed;
   - seven labels and 26 index entries were added;
   - there are no dangling references;
   - `scripts/check-citation-placement.py` passes.
3. Independent verification of every math fragment that changed for a reason other than punctuation (1066 fragments in 249 files), split among four reviewers comparing old and new text in context.
   - **One error introduced by the revision**, now fixed: the reworded formula for the determinant density `k_T` in `section_semipositive_dual_attainment.tex` had the wrong normalization. It now follows `eq:weak-gaud-functional`: `k_T = f_0^{1−n}(det P')^{1/n}`.
   - **One hypothesis dropped in revision**, now restored: positive weights and `β > 0` in `thm:moving-divisorial-potential-stability`.
   - **Other slips fixed:** an ambiguous sentence about an infimum, three new symbol clashes, an omitted inline definition (`β_s`) and display punctuation.
   - All other changes were judged harmless or correct.
4. A full clean build has no errors, no overfull boxes and no undefined references or citations:
   - 1501 physical pages; the last index page prints as **1475**;
   - 111 bibliography entries and 898 index entries.
   - Pages were inspected visually: the notation table, the Chapter 1 opening and Section 13.30.

This is an editorial and comparison check, not a new independent certification of the book's proofs.

## Publication

Homepage commit `265ec713aec27d9c62d7373054e9a21f201692bf` on `MingchenXia/mingchenxia.github.io` replaces `Papers/SHPT_vibe.pdf` and updates only the matching description (“A research monograph. 1475 pages. Updated October 6, 2026.”). The remote files were verified by blob hash. The local `gh` token was invalid, so publication used an equivalent git-based publisher with the same checks: one commit, two files, never force-pushed. The live GitHub Pages check is recorded in `research/STATUS.md`.

## Deferred items (no change made)

- **Placement suggestions:**
  - the vector-bundle positivity material in Chapter 4 could form its own chapter;
  - the zero-volume product models of Section 15.6;
  - the metric-geometry sections 27.10–27.15;
  - the algebraic elliptic-ruled-surface block in the Gauduchon-volume chapter;
  - the self-contained individual-density sections 13.24–13.30;
  - the full theorems in the problems chapter.
- **Separate counters.** Theorem and lemma counters are separate (svmono `envcountsect`), so different environments can share a number. Kept, per the skill's rule to preserve theorem counters.
- **Symbols with several meanings, each declared locally:** `μ_u` (adjoint probability, polar curvature, extended measure) and `𝓜`.
- **Kept as is:**
  - `section_gauduchon_local_adjoint_bounds.tex` assumes `n ≥ 3`; this is the author's original hypothesis and is kept.
  - The LCK radial flux constant is stated “up to a constant factor”; one computation gives `4πn·lF/D`.
