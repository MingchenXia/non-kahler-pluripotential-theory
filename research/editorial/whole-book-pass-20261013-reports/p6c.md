# p6c report: placement moves and coordination edits

## 1. Moves made

Before the moves I checked the plan's claims with lg.py and q.py, using copies in `scratchpad/p6c/` so the shared graph.pkl was not overwritten. The claims held. The moved igood block had no dependency later than the new chapter, and its earlier users were prose only.

- **igood §Complete model topologies (old 227–273) → `chapter_polar_model_topologies.tex`.**
  - Paragraphs 230–261 became the chapter opening: earlier complete topologies, then this chapter's content. The curve-quotient paragraph is reflowed. A last sentence points to the final section.
  - Added a standing-assumptions paragraph. Compact manifolds are connected. **The bounded mass property is not assumed**, so the Hopf examples are allowed; mass bounds via $v_\pm$ are used only where stated. Notation is that of chap:hermitian-igood and chap:mass-bound-volumes, and the inputs are named: curve models, local polar parts, $d_\theta$ and $\mathcal M_\delta$.
  - Paragraph 263 opens the new `\section{Polar currents on modifications}` (label `sec:polar-currents-modifications`). "The rest of this subsection" became "This section".
  - Paragraph 269 closes that section, with a pointer to qu:singularity-topology-program.
  - igood keeps §1–5, §ordinary topology (incl. all-obstacle and countable poles) and §small curvature. The chapter opening (l.8) gets a one-sentence pointer to the new chapter.
- **Sections of the new chapter.** The `\input`s now sit in the chapter file:
  - fibration (`\section{Relative divisors and fiber obstacles}`);
  - zero_volume (`\section`);
  - separated_curve_product_models (`\section{Several curve factors}`), with weighted / arbitrary / separated_all / general_auxiliary / unbounded as subsections;
  - curve_fibration, promoted to `\section{Models over a curve}`, with Finite curve factors and Hopf fibers as subsections;
  - polar section: polar_current, gauduchon and diffuse promoted from `\subsubsection` to `\subsection`. "next part" became "next subsection".
- **P24: prop:finite-cover-envelope-transport** (all_obstacle 88–121) moved to just before cor:fibration-component-cover (fibration:336).
  - New one-line lead-in.
  - The "Recall … stretching competitor" sentence now sits before prop:fibration-relative-envelope-class, its first user.
  - The sentence about continuous obstacles was dropped: fibration l.17 already says it.
- **ex:zero-volume-comparison-collapse** (mass_bound 735–753) moved to after ex:nonclosed-zero-volume-distinct-models (zero_volume:141).
  - Added a lead-in, and "$U=\overline{\operatorname{vol}}_\theta$ as in def:model-volume-comparison" in the proof.
  - mass_bound:733 is now a prose pointer.
- **P23.** `section_finite_curve_pullback_models` (subsection heading plus envelope-pullback, model-retraction, averaging-not-nearest) is `\input` at the end of sec:curve-model-backgrounds (mass_bound, before joint_curve). Added "results of this section apply on $C$, $C'$ in place of $Y$".
  - finite-curve:original-base-subspace was cut and placed in subsec:finite-curve-factors, where the old `\input` was. It gets a one-sentence recall of $J,R$. "The preceding proposition" became \cref{finite-curve:model-retraction}.
- **§3 Hopf.** `\input{section_hopf_transverse_recovery}` moved from envelope_systems (end) to before `\section{Model comparison under background changes}`.
  - Added a sentence: $X$ lacks the bounded mass property, and the standing hypotheses (bounded mass, bigness) are used only on $B=\mathbb P^2$ with $\kappa$. **This is accurate:** only thm:positive-volume-system-recovery and countable-divisorial:positive-mass need them, both on $B$; everything else cited is from earlier chapters with no mass bound.
  - The mass_bound standing-assumption paragraph now notes the exception.
- **Openings updated:**
  - mass_bound l.11 and l.13: pointer to the new chapter; Hopf recovery and finite curve maps added;
  - envelope_systems l.8: "both recovery theorems are proved in \cref{chap:mass-bound-volumes}";
  - ordinary_type l.6;
  - all_obstacle l.86 (now points to the next subsection and to chap:polar-model-topologies).

**Rerun of the dependency check after the moves (lg.py rebuilt):**
- No reference anywhere in the new chapter points after the end of chapter_mass_bound_volumes, except prose pointers to qu:singularity-topology-program.
- Everything earlier that cites the new chapter is prose.
- The Hopf and P23 blocks have no forward dependencies.
- No forward references from a proof or statement remain in any of my files. Book-wide fwd.py now lists 20; none touch this material.

**Forward references that remain (all prose):**
- chap:polar-model-topologies from igood:8, ordinary_type:6 and all_obstacle:86 (×2);
- curve models of mass_bound from igood:196 (prop:model-comparison-gauge), ordinary_type:6/173 and all_obstacle:86;
- envelope_systems:8/181 → thm:positive-volume-system-recovery and the chapter;
- mass_bound:11 → chapter;
- mass_bound:733 → ex:zero-volume-comparison-collapse;
- mass_bound:1179 → ex:nonclosed-zero-volume-distinct-models;
- new chapter l.32 and arbitrary:82 → qu:singularity-topology-program.

## 2. Moves not made
None.

## 3. Coordination edits
- **P15 reduced (applied).** qu:i-good-no-bmp was deleted. Its label is on qu:singularity-topology-program (research_program:232), which already covers its content: positive lower volume, bounded mass, curve topology, gauge/two-sided compatibility, loss of bigness. arbitrary_curve:82 now cites qu:singularity-topology-program.
- **Item 3 (applied).**
  - ordinary_type:159 now reads "…carried by a compact polar set in a small coordinate disk…; such measures exist in every disk by \cref{lem:polar-cantor-nonatomic-measure}".
  - The proof of ex:diffuse-polar-zero-model is shortened to: lemma → $p=p_{A\sigma}$ (lem:curve-polar-model) → $T_p=A\sigma$ → Lelong numbers vanish → $\tau(p)=A$. The explicit Cantor/Green computation is gone.
  - diffuse:21 now takes $K,\sigma$ "constructed in the proof of" the lemma: same $r_k=\exp(-4^{k+1})$, level-zero interval in $\Delta$.
  - p6d's label has landed. It resolves when chapter_framework is compiled.
- **5a (verified duplicate; applied).** Step 2 of thm:small-pole-envelope-residual and the first two paragraphs of the proof of prop:diffuse-representative-mass repeat the same argument: truncation limits via thm:small-pole-local-products with a smooth correction, patching, $\mathbf1_S\Phi_v$ via cor:closed-current-hausdorff-null, $\Phi_v=\mathrm{MA}$ off $S$, Stokes plus the binomial expansion, and the $v_\pm$ bounds.
  - New **lem:small-pole-full-measures** (section_small_pole:6, no bounded mass needed) gives: the definition of $\Phi_v$, the limits $W_j$, eq:small-pole-full-total, $v_-\le J\le v_+$, the off-$S$ identity, and the restriction for every $q$. The general-$q$ case now has a one-line multilinearity argument.
  - Theorem: statement shortened and Step 2 cites the lemma. Diffuse: statement and proof cite the lemma, with $c_j(v)=\int W_j\wedge\omega^{n-j}$. prop:disjoint-diffuse… now refers to the lemma for $\Phi$.
- **5b (applied).** The internal route is correct and short:
  - item 1 of thm:local-i-inputs reduces $\sim_{\mathcal I}$ to equal Lelong numbers on all local modifications;
  - a local modification of a surface is a finite composition of point blowups, which extend to $X$;
  - one more blowup turns a point Lelong number into a generic one. The same fact is used in section_psh_descent:210.
  - I restored this route as the proof. The external DX22 route is no longer mentioned in the text.
- **5c (applied).** In the proof of prop:model-comparison-gauge: "The bijection $u\mapsto u-f$ of \cref{prop:gauge} preserves curvature currents and maps ordinary types onto ordinary types; hence it preserves both singularity volumes."
- **5d (both applied).** ordinary_type:44, with the suggested wording. countable_pole:86 now ends "…and $P_{\omega,F}[u]_{\mathcal I}=P_{\omega,F}[0]_{\mathcal I}$. The latter equals $P_\omega(F)$ because $P_{\omega,F}[0]\le P_{\omega,F}[0]_{\mathcal I}\le P_\omega(F)$."

## 4. Replacements needed in files I do not own

**chapter_history.tex**
- **l.439.** Replace its first two sentences with: "The order test in \cref{countable-divisorial:positive-mass} reduces ideal equivalence to Lelong numbers on local modifications by \cref{thm:local-i-inputs} and uses the factorization of a modification of a surface into point blowups; on a projective manifold it is also a case of the valuative characterization of Darvas and Xia \cite[Theorem~2.13 and Proposition~2.30]{DX22}, whose Lelong convention differs from the divisor coefficient used here by a factor of two."
- **l.467.** "The Cantor construction of \cref{ex:diffuse-polar-zero-model}" → "The Cantor construction of \cref{lem:polar-cantor-nonatomic-measure}".
- **467–471 (diffuse paragraphs).** Move them to a new `\subsection{Zero-volume models and polar currents}` of sec:history-volumes, after "Curves and zero-volume limits". The text is otherwise location-neutral.
- **473–483.** Location-neutral. The P23 results are now in sec:curve-model-backgrounds, which this subsection already covers.
- **No separate history section for the new chapter is needed.** Its fibration, product and curve-fibration material has no sources. Optionally, end l.432 with: "; on products and fibrations over curves it gives complete metrics on explicit zero-volume model loci, while in higher dimension it misses diffuse product poles."
- **l.600.**
  - "whose closed mass and valuative inputs are described above" → "whose closed mass and Lelong-number inputs are described in \cref{sec:history-volumes}".
  - Better: move the paragraph after l.439, since thm:hopf-transverse-recovery is now in chap:mass-bound-volumes. Then "uses the same positive-volume theorem on $\mathbb P^2$" → "uses the recovery theorem \cref{thm:positive-volume-system-recovery} on $\mathbb P^2$", and "described above" stays.

**preface.tex**
- **l.83:** "\Cref{part:mass-bounds} gives the volume and equation theory under mass hypotheses, together with the zero-volume models on products and fibrations of \cref{chap:polar-model-topologies}, some of which need no mass bound."
- **l.46, l.50:** no change; they only cite labels.

**Other files**
- **section_curve_ordinary_topology.tex:65:** "…in an affine chart, using the Cantor construction in \cref{ex:diffuse-polar-zero-model}." → "…in an affine chart, by \cref{lem:polar-cantor-nonatomic-measure}."
- **book.tex:** no change; the chapter is already included.

## 5. Compile check and math diff
- **chapcheck** (5 chapters, run 3×): no errors and no overfull boxes. The only underfull box is the 1783 one.
  - Undefined references remain only in research-programme inputs owned by others: section_non_kahler_geometry (primitive-elliptic*, gaud-positive-volume-collapse, balanced-pluriclosed-closed), section_gauduchon_collapse and section_parallel_torsion_positivity. These are concurrent moves.
  - With chapter_framework added, lem:polar-cantor-nonatomic-measure resolves. That compile shows lem:bc-one-one-current-description, lem:nef-blowup-metric and eq:nef-blowup-positive-metric as multiply defined; these are others' moves against the baseline aux.
  - **Tool bug:** chapcheck.sh misses undefined-reference warnings when the label is long enough for "undefined" to wrap onto the next log line. I scanned book.log with wrapped lines joined.
- **mathdiff3, base 099fd4b.** HEAD already holds WIP snapshots of these edits, so I used the commit before them. The diff was aggregated over all 25 files.
  - Moved segments cancel.
  - What remains is only the coordination edits: lemma 5a, the diffuse proof, the shortened Cantor proof, the countable-pole chain, the 5b Lelong condition and the 5c phrase.
  - It also shows the new notation sentences: the chapter opening, $J(v)=v\circ r$, $\mathcal M(\beta)$, $U=\overline{\operatorname{vol}}_\theta$, $\Delta$.
  - Labels: no label lost; added lem:small-pole-full-measures and sec:polar-currents-modifications.
  - Index: one entry added, none lost.
