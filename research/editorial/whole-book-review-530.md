# Checkpoint 530 — Integration of new results and third whole-book review (in progress)

Request (7 October 2026): “再来检查一轮，顺便看看repo里新解决的问题有没有可以整合进来的。” Later: the standalone results without authors are original to the book and are never cited (“Do not cite these files without authors. They are supposed to be original to the book.”).

## 1. Merge
`origin/main` (24 commits: standalone papers P05, S05, S07-singular and original-condition audits) was merged into `claude/friendly-fermi-jzw1o1` (merge commit 0468794). Book sources were unchanged by the merge.

## 2. Integrated results (commit a37d66c; audits applied in 50aa565 and 320fce8)
Each paper was reconstructed independently against the book's definitions, its literature inputs were replaced by the book's own results, and the draft was then audited by a second, independent reviewer. No standalone paper, file or workflow is cited or mentioned in the book.
- **S04** — Kähler-factor densities on zero-lower-mass products: `lem:closed-factor-bounded-normalization`, `thm:closed-factor-product-equation` (threshold ∫H^N/∫f dV, exact finite-mass equations in the envelope class), `prop:closed-factor-root-subspace` (closed copy of L^N in the root space), `ex:closed-factor-logarithmic-tails`. S04 itself stays open.
- **S05** — zero-exponent limits for separated non-L^p densities (`sec:nonlp-selection`): whole-family convergence, exact scalar error iff (k+1)α<k, divergence otherwise, joint stability.
- **P05** — `thm:lck-chern-ricci-divergence` (∫|(∇λ)^-|² = ½∫(d^*λ)²), strengthened `thm:lck-chern-ricci-rigidity`, `cor:lck-calabi-yau-vaisman-reduction` (the conjecture is equivalent to one strictly LCK metric both Chern–Ricci flat and Gauduchon), `prop:lck-kodaira-flat-gauge`. The conjecture stays open.
- **S07** — weak adjoints for a divisorial reference in a non-Gauduchon background on P¹×P¹ (`sec:nongauduchon-weak-adjoints`); the type reduces to bounded β-psh potentials, giving uniqueness and a special case of `conj:continuous-gaud-adjoint`.
All four audits: correct after small scope/notation fixes (listed in the commit messages of 50aa565 and 320fce8).

## 3. Third whole-book review (in progress)
29 parts (`review-530-reports/`, guide as in checkpoint 529 with added checks for direction words, BMP/Kähler scope and book citations). Status at this snapshot: 18 parts complete (r3g01–03, 05–09, 11, 14–21, 23), 11 running (r3g04, 10, 12, 13, 22, 24–29). Main corrections so far (all local; details in the part reports):
- a wrong-way inequality in `prop:singular-no-uniform-limit` (introduced by the presentation pass);
- a sign error (semipositive vs seminegative) in the Calabi–Eckmann endpoint section;
- sublevel/superlevel direction words (two places); scope of the domination principle in the envelope chapter; the flag-body triangle claim restricted to homogeneous bundles;
- missing hypothesis checks (bigness before the nef-and-big theorem; positivity of bounded masses), a false remark on connectedness of Zariski open sets, a wrong gluing in a Pogorelov example, criticality of torus completions only at s=1/√2;
- coordinator fixes: SGPT section-name locators replaced by numbers (Sections 11.1, 11.1.2, 13.1, Theorem 1.6.1, Appendix A), a W^{1,2} convergence justification, terminology (“determinant measure”), the notation-table row for the Gauduchon trace metric.
Open coordination items are in `review-530-reports/coordination.md`. Deferred: an expert check of `thm:flat-anticanonical-neighborhood` (again flagged).

Remaining steps: finish the 11 running parts, apply coordination items, independent audit of all third-review changes, full build, publication, CHANGELOG/STATUS.
