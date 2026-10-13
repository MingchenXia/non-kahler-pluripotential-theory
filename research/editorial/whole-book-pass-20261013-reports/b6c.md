# b6c audit report (p6c, p6f, and section_curve_ordinary_topology)

## Verdicts
- **p6c: CORRECT AFTER FIXES.** One real gap: the polar-currents section used $X$ without defining it. Fixed.
- **p6f: MOVES CORRECT.** I made one precision edit.
- **section_curve_ordinary_topology** (the coordinator's citation of lem:polar-cantor-nonatomic-measure): correct.

## What I checked
- **Math diff.** I ran an aggregated math diff (base 099fd4b) over the 27 p6c files (with curve_ordinary_topology and psh_local_capacity) and over the 12 p6f files.
  - Moved segments cancel.
  - What remains is the listed rewrites.
  - No label or `\index` entry was lost. Added: 3 labels and 2 index entries.
- **Label graph** (private copy, rebuilt after my edits). In all 40 files there are no forward references from a proof or statement. The one exception is research_program:356 (problem → appendix), which is unchanged since the base and is harmless. Users of every moved or new label were checked; all earlier users are prose.
- **Moves and standing assumptions.**
  - p6c: 9 move items.
    - The igood "Complete model topologies" block became the chapter opening, the section intro and the closing paragraph.
    - The fibration, zero-volume, several-curve (6 children), models-over-a-curve and polar sections.
    - P24, ex:zero-volume-comparison-collapse, P23 with the split of finite-curve:original-base-subspace, and the Hopf section.
  - p6f: 3 move items.
- **Rewritten or new mathematics, checked as a referee.**
  - p6c (11 items):
    - lem:small-pole-full-measures;
    - the shortened statement of thm:small-pole-envelope-residual;
    - prop:diffuse-representative-mass;
    - the restored route in countable-divisorial:positive-mass;
    - ex:diffuse-polar-zero-model;
    - the 3 Cantor citations;
    - the merged problem;
    - 5c;
    - 5d.
  - p6f: lem:big-weighted-common-bound, thm:big-relative-self-measure-convergence, cor:metric-pvp-minimal-volume with the converse paragraph, and cor:positive-lower-mass-solvability.

## Findings

### 1. New chapter: $X$ undefined (fixed)
- In igood, the chapter fixed $X$. In chapter_polar_model_topologies nothing does.
- The polar subsections nevertheless begin "Here $X$ has dimension $n\geq2$", "Here $n\geq1$ is arbitrary, and $\omega$ is a Hermitian form on $X$", and "From here on, $n\geq2$ and $\omega$ is a Hermitian form on $X$".
- No other moved section uses igood's fixed $X$, $\theta$ or $\mathrm dV$. Every other section fixes its own data.
- **Fix** (chapter_polar_model_topologies.tex, intro of sec:polar-currents-modifications): "…although they lower the volume." → "…although they lower the volume. Throughout the section, $X$ is a compact complex manifold of dimension $n$."

### 2. section_finite_curve_pullback_models.tex l.8 (fixed)
- "The definitions and results of this section apply on $C$ and on $C'$ in place of $Y$" → "The curve results of \cref{sec:curve-zero-volume-models} and of this section apply on $C$ and on $C'$ in place of $Y$".
- Reason: the file is a subsection, and the notation it uses ($U$, $\mu$, $p_\beta$, $\mathcal M$, $d_\sigma$) comes from both curve sections.

### 3. section_hopf_transverse_recovery.tex intro (fixed, clarity)
- At its old place the section relied on "fix real numbers $a<c$" in the envelope-systems chapter opening.
- **Added:** "The envelope systems $\mathscr S_{a,c}$, for the real numbers $a<c$ fixed there, and the maps $\mathsf E$ and $\mathsf R$ are those of \cref{subsec:positive-system-recovery}."
- **The added bounded-mass sentence is accurate.** The only mass_bound results cited are thm:positive-volume-system-recovery and countable-divisorial:positive-mass, both used on $B=\mathbb P^2$ with $\kappa$. Everything else cited comes from earlier chapters.

### 4. chapter_relative_finite_measures.tex, proof of cor:positive-lower-mass-solvability (fixed, precision)
- The corollary now uses this chapter's $\mathrm dV$, while thm:lower-mass-obstructing-measure uses the probability $\mathrm dV$ of chapter_prescribed_equations.
- "the density of \cref{thm:lower-mass-obstructing-measure} violates (3)" → "the probability measure of \cref{thm:lower-mass-obstructing-measure} has a density with respect to $\mathrm{d}V$ that is bounded below by a positive constant, and it violates (3)".
- **Otherwise correct.**
  - (1)⇒(2) needs eq:relative-positive-lower-volume only for $\theta=h$, which is hypothesis (1).
  - Hermitian $h$ is semipositive and big, and $0$ satisfies eq:als-model-condition, so thm:als-general-measure applies.
  - (3)⇒(1) uses no lower-mass assumption.

### 5. Results of the referee checks (no problems found)
- **lem:small-pole-full-measures.** The proof is complete without bounded mass. It covers the limits, Stokes, eq:small-pole-full-total, $v_-\le J\le v_+$, the off-$S$ identity, and $q$-independence via $q+C|z|^2$ and multilinearity of thm:small-pole-local-products.
- **thm:small-pole-envelope-residual.** The shortened statement keeps all of its content: the full measures and their restriction formula now come from the lemma. Steps 3–4 still use $v_+<\infty$ (standing in mass_bound).
- **prop:diffuse-representative-mass.** It uses only the lemma and lem:small-pole-residual-invariance, and needs no bounded mass. Its later users either assume $0<v_-\le v_+<\infty$ (cor:diffuse-hermitian-model-interval, prop:disjoint-diffuse…) or derive bounded mass first (prop:equal-residual-anisotropic-models) before they cite the theorem.
- **countable-divisorial:positive-mass.** The restored route matches 1fece9c step by step:
  - item 1 of thm:local-i-inputs;
  - local factorization into point blowups that extend to $X$;
  - one more blowup, which gives a generic Lelong number;
  - lem:birational-ideal-order for the converse.
- **ex:diffuse-polar-zero-model.** $T_p\ge\mu_p$ with both of mass $A$ gives $T_p=A\sigma$. Nonatomic $\sigma$ gives zero Lelong numbers and trivial ideals, $P[p]_{\mathcal I}=0$, and $\tau=A$. The users (zero-volume examples) need only $P[w]=w$, $P[w]_{\mathcal I}=0$ and unboundedness.
- **lem:polar-cantor-nonatomic-measure.** Correct ($2r_{k+1}<r_k$, $u(x)\le2^{1-k}\log r_k=-2^{k+3}$). The diffuse-lemma, ordinary-type and curve-ordinary citations get what they use.
- **lem:big-weighted-common-bound.** Correct line by line. The finite rooftops are not assumed to lie in $\mathcal E_\varphi$, and the text says so correctly. On $\{a=-\infty\}$ the integrands are irrelevant because all the measures are non-pluripolar.
- **thm:big-relative-self-measure-convergence.** The lemma applies with $h=p_1$ and $\lambda=1$.
- **No circularity.** The lemma cites only framework/products results and zero domination (mass_bound).
- **cor:metric-pvp-minimal-volume.** It uses only bounded mass, a strict barrier, prop:volume-addition and thm:volume-monotonicity, so "Assume only…" is right. The converse paragraph is a correct application of thm:volume-monotonicity ($\theta\le C\omega$, $\varphi\preceq0$).
- finite-curve:original-base-subspace and ex:zero-volume-comparison-collapse are correct at their new places.
- **Openings and the merged problem.** The openings (new chapter, igood l.8, mass_bound l.11/13/15, envelope_systems l.8, ordinary_type l.6, all_obstacle l.86) are accurate. qu:singularity-topology-program covers all of the old qu:i-good-no-bmp.

## Remaining (files I may not edit)
- **chapter_research_program.tex l.232.** The second label qu:i-good-no-bmp now has no users and can be dropped. Otherwise there is no problem in the research programme.
- **chapter_history.tex l.439** is now false. It says the order test "uses the projective valuative characterization of Darvas and Xia", but the proof now uses thm:local-i-inputs. p6c's replacement text should be applied.
- **chapter_history.tex l.467.** "The Cantor construction of \cref{ex:diffuse-polar-zero-model}" → "…of \cref{lem:polar-cantor-nonatomic-measure}".
- **chapter_history.tex l.600.** "described above" is still location-dependent (see p6c §4).

## Compile check
chapcheck b6c (9 chapters), run 3 times after the edits:
- No errors and no overfull boxes. The only box warning is the known Underfull (badness 1783).
- **Multiply defined:** lem:bc-one-one-current-description, lem:nef-blowup-metric, eq:nef-blowup-positive-metric. Each is defined once in the source (baseline aux artefact).
- **Undefined** (log scanned with wrapped lines joined): only labels of chapters outside this build, all present in the source (prop:primitive-elliptic-*, thm:parallel-torsion-kahler, prop:gaud-positive-volume-collapse, …), cited from section_non_kahler_geometry and other agents' files.
