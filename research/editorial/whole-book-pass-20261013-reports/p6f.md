# p6f report

## 1. Moves made

**(a) The paragraph "The standing assumptions also give $v_-(\omega)>0$"** moved from chapter_bounded_mass_equations (old l.57–62) to section_big_minimal_measures, right after the proof of `cor:metric-pvp-minimal-volume`.
- It now opens with "Conversely, the standing assumptions imply $v_-(\omega)>0$." The argument and display are unchanged.
- One closing sentence is added: under bounded mass, some smooth big background admits a reference satisfying eq:li-model-condition exactly when $v_-(\omega)>0$, and then $V_\theta$ satisfies it in every smooth big background.
- The corollary statement now begins "Assume only that $X$ has the bounded mass property and that $v_-(\omega)>0$." (a5n item 2). Its proof is unchanged. The proof uses only bounded mass (for $M_V<\infty$), a strict barrier, prop:volume-addition and thm:volume-monotonicity, so the weaker hypothesis is enough.
- Dependencies: thm:volume-monotonicity, prop:volume-addition and eq:li-model-condition are all in chapter_mass_bound_volumes, which comes earlier. Nothing cites the paragraph, and the corollary has no users.

**(b) `lem:big-weighted-common-bound`** moved from section_big_weighted_limits to section_big_relative_energy, just before `thm:big-relative-self-measure-convergence`.
- The lemma's proof is now written out in full. It used to say "follow the proof of the theorem". It now has its own subsequence extraction, the weighted rooftop partition, $h\le p_j\le a$ with upward stability, lem:monotone-psh-capacity with lower bound $h$, lem:weighted-extended-lsc with weights $\min(1,|\cdot-a|)e^{\lambda a}$, positivity of the exponential off the pluripolar pole set, zero domination, and the Hartogs squeeze.
- The theorem's proof is shorter. It extracts a subsequence, gets the unweighted rooftop bound (eq:big-self-measure-roofs, partition "as in the proof of the preceding lemma"), and applies prop:big-relative-first-moment (one-sided form) to get $p_j\in\mathcal E_\varphi$, which proves the second assertion. It then applies the lemma to the extracted sequence with $h=p_1$ and $\lambda=1$.
- The lemma's hypotheses hold there: $p_1\le u_k$ for all $k$; $u_j,u\le\varphi+C$ (envelope identity and Hartogs); $u\preceq\varphi$; and $\int|u_j-u|e^{u}\mu_{u_j}\le e^{\sup u}\int|u_j-u|\mu_{u_j}\to0$.
- New linking sentences: one before the lemma, and "Without a given lower bound, the first-moment criterion produces one…" before the theorem.
- In the weighted-limits opening, "This bound gives convergence in capacity" became "By \cref{lem:big-weighted-common-bound}, this bound gives…".
- Label graph (private copy of lg.py/q.py):
  - The lemma's proof cites lem:qpsh-almost-everywhere-order, lem:monotone-psh-capacity and lem:weighted-extended-lsc. All are earlier (framework and products chapters). "Zero domination" points through the chapter opening to thm:big-relative-domination in mass_bound_volumes.
  - The theorem's proof cites prop:big-relative-first-moment, which is in the same section and earlier, and the lemma, which now comes before it.
  - Users of the lemma are the weighted-limits prose and the proof of lem:big-truncated-addition-limit, both later.
  - `reach()` finds no path from the lemma to the theorem, and no transitive dependency on later labels. Nothing is circular.

**(c) `cor:positive-lower-mass-solvability`** moved from section_lower_mass_solvability (chapter_prescribed_equations) to chapter_relative_finite_measures, in sec:relative-general-setting, right after thm:als-general-measure and its following paragraph. The definition sentence on $\mathcal E_{\mathrm{env}}(X,h,0)$ moved with it.
- Assumptions stated at the new place:
  - the statement begins "Let $h$ be a Hermitian form on $X$";
  - the preceding prose says that the next corollary does not assume eq:relative-positive-lower-volume, which that chapter otherwise assumes.
  - $X$ connected is the book's global convention.
- Chapter opening: one sentence added after the standing assumption. For a Hermitian background and reference 0, positive lower mass is also necessary for solvability with all measures.
- Old place: the section intro "if and only if" sentence now reads "…when $h$ has zero lower mass, some probability density admits no positive scaled subsolution. Conversely, if $v_-(h)>0$, every … measure admits such a solution (\cref{cor:positive-lower-mass-solvability} in \cref{chap:relative-finite-measures})." This is a prose forward pointer.
- Dependencies of the corollary's proof: eq:als-model-condition (chapter_envelopes), thm:als-general-measure (statement just before; its proof in section_general_measure_relative does not cite the corollary), and thm:lower-mass-obstructing-measure (chapter_prescribed_equations, earlier). All are earlier. Users are prose only: lower_mass_solvability:10, extrema:38, the relative-chapter opening (l.15) and research_program:25.
- No `\index` entries were involved in (a)–(c), and no labels were renamed or deleted. No new labels.

## 2. Moves not made
**Item 3 (appendix: quotient vs toric) was left unchanged.** I checked the identification, and it is correct:
- $X=\{z_1z_2=z_3^2\}=X_\sigma$, with $M=\{(a,b)\in\mathbb Z^2:a+b \text{ even}\}$, $\chi^{(a,b)}=s^at^b$, $\sigma=\mathbb R^2_{\ge0}$ and $N=\mathbb Z^2+\mathbb Z(\tfrac12,\tfrac12)$.
- The primitive rays are $(1,0),(0,1)$, and $D_{(1,0)}=E$.
- The boundary vectors are $w_D=(\tfrac12,1)$ and $w_0=(1,1)$.
- With basis $(1,1),(1,-1)$ the log form is $-\Omega/z_3$, and $q=4$ gives $B_D=z_1z_2^2\Omega^{\otimes4}/z_3^4=\beta$.
- $g=\max(2\sqrt2x_1,4x_2)$, and the recession test, checked on the rays $(1,0)$, $(0,1)$ and the kink $(1/(2\sqrt2),1/4)$, gives exactly eq:quotient-monomial-tests.
- The lemma is likewise the convex-cone lemma with the stated $C,g,\ell$.

It is still not a simplification:
- The citation needs this identification and the kink computation. That is as long as the present three-line elementary proof of lem:weighted-logarithmic-maximum-integral.
- The proposition still needs the double cover for the whole-germ (Parseval) part.
- Putting the toric subsection first would also mean moving the definition eq:quotient-adapted-ideal and its motivating paragraph into the toric subsection, and rewriting both subsection openings.
- chapter_history l.815, which says the example is proved directly by splitting the quadrant, would also need rewriting.

## 3. Coordination edits
- a5n item 2: applied as (a).
- r5g22 §6, first two items: applied as (a) and (b).
- r5g22 §6, third item: rejected (see §2).

## 4. Replacements needed in files I do not own
- **chapter_prescribed_equations.tex**, opening paragraph "The last part of the chapter…":
  - old: "Solvability of $\mathrm{MA}_h(u)=c\mu$ for every nonzero finite non-pluripolar measure $\mu$ is equivalent to a positive lower bound for the masses of bounded $h$-plurisubharmonic functions. Without such a bound,"
  - new: "If the masses of bounded $h$-plurisubharmonic functions have no positive lower bound, some probability measure $\mu$ with density bounded below by a positive constant admits no solution of $\mathrm{MA}_h(u)=c\mu$; with such a bound, every nonzero finite non-pluripolar measure admits one (\cref{cor:positive-lower-mass-solvability} in \cref{chap:relative-finite-measures}). Without such a bound,"
- **section_gauduchon_volume_extrema.tex l.38**: the citation is now a prose forward pointer, which is acceptable.
  - Suggested old: "By \cref{cor:positive-lower-mass-solvability}, positivity of $v_-(\omega)$ is also equivalent"
  - new: "\Cref{cor:positive-lower-mass-solvability} in \cref{chap:relative-finite-measures} shows that positivity of $v_-(\omega)$ is also equivalent"
- **chapter_history.tex**: nothing is required.
  - Optional, l.526: after "implies that the metric has positive lower mass", add "(see the remark after \cref{cor:metric-pvp-minimal-volume})".
  - l.815 is unchanged, since item 3 was not done.
  - l.817 is handled elsewhere.
  - No history paragraph names the locations of the three moved blocks.
- **chapter_research_program.tex l.25, preface, book.tex**: no change.

## 5. Checks
- `chapcheck.sh p6f chapter_bounded_mass_equations chapter_relative_finite_measures appendix_hermitian_spaces chapter_prescribed_equations` was run three times, the last after the final edit.
  - Result: no errors, no overfull boxes, no undefined or multiply defined references.
  - Only the ignorable Underfull (badness 1783) in section_unibranch_nonclosed_cuspidal_products remains.
  - In the first pass only, an undefined eq:split-product-ma appeared (from other agents' files). It resolved in the second pass.
- `mathdiff3.py --base HEAD` on my 6 changed files:
  - The removed paragraph (bounded_mass_equations) matches the added converse in big_minimal_measures.
  - The lemma removed from big_weighted_limits matches the lemma added in big_relative_energy.
  - The other differences are:
    - the theorem-proof tail that is replaced by the lemma citation;
    - the new math $\lambda=1$, $h=p_1$, $p_1\le u_k$, $e^u\le e^{\sup u}$, and the subsequence/squeeze text written out in the lemma;
    - the corollary block, removed from lower_mass_solvability and added in relative_finite_measures, plus "Let $h$ be a Hermitian form on $X$";
    - the corollary hypothesis "bounded mass property" ($X$);
    - $v_-(h)>0$ in the new pointer.
- Appendix files were not changed.
