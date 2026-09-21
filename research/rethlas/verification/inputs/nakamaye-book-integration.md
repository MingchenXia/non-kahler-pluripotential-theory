Run_id: nakamaye_book_integration_01

Statement: Verify the bounded mathematical adaptation of the supplied Vu–Xia Nakamaye proof into the book, and verify the new self-contained proof of Xiao's weak nef-difference criterion in full. This is not a repeat of the original source audit: transcendental_nakamaye_01 is complete and correct, its entire source proof may be accepted in its compact connected Kähler setting, and its files must remain unchanged. The theorem being incorporated asserts zero numerical restricted volume on every positive-dimensional irreducible component of the non-Kähler locus and equality with the numerical null locus. It does not assert zero restricted volume on every subvariety contained in that locus.

Accepted source: /Users/mingchen/Non-Kahler/research/sources/VX-null-locus.tex, SHA256 a303e40d45e5f073e3e73887e79711d82d22a491ec92be852c5aef9d77d21b7a. Accepted previous report: results/transcendental_nakamaye_01/verification.json. The source has already undergone a complete sequential audit. The goal here is to check that manuscript changes preserve this proof, its hypotheses and its interfaces, plus the new numerical proof below. Do not rerun the unchanged source proof merely to duplicate that audit.

Manuscript files to compare read-only:
- /Users/mingchen/Non-Kahler/book/author/chapter_transcendental_nakamaye.tex
- /Users/mingchen/Non-Kahler/book/author/section_nakamaye_nef_difference.tex
- /Users/mingchen/Non-Kahler/book/author/section_nakamaye_regularization.tex
- /Users/mingchen/Non-Kahler/book/author/chapter_bott_chern_loci.tex
- /Users/mingchen/Non-Kahler/research/editorial/nakamaye-adaptation-map.json

Changes to check: all source labels have prefix nk:, notation expanded into standard book operators, existing bibliography keys mapped exactly. Article front matter and author addresses removed. Main theorem restated exactly with positive dimension explicit. Repeated no-isolated-point proof replaced by already proved prop:bc-no-isolated-locus. Custom Setup environment replaced by explicit standing-assumptions paragraph. Connected ambient Y is added to relative principalization; all actual applications have it. A dependency-order table and the final Kähler/Hermitian proof-boundary discussion are new; check every assertion and quantifier in these additions. The source main proof is otherwise retained. Verify no accidental macro replacement has changed a formula or removed a hypothesis, and that source definitions agree with the previous closed-loci chapter in the shared Kähler regime. The requested source-map comparison is substantive; do not treat successful compilation as proof.

Independent boundary: the new Hermitian versions of quantitative regularization and the global ideal potential lemma are undergoing hermitian_quantitative_regularization_01. For this integration audit use ONLY their already verified original Kähler specializations as premises. The main theorem applies them only in that Kähler setting. Check that no stronger version is needed there. The final Hermitian discussion is conditional on the separate audit and cannot itself establish the generalization. Both audits must pass before inclusion.

The one new full mathematical proof in this submission reconstructs the numerical criterion; verify it without assuming the target criterion. Existing book inputs are thm:tw-smooth in chapter_smooth_equations.tex and thm:lamari in chapter_gauduchon.tex. Read their actual hypotheses. The source claim is Xiao15 Theorem1.4, https://www.numdam.org/item/10.5802/aif.2959.pdf ; the source is attribution, not a premise replacing the proof below. No bounded mass property is assumed anywhere in the general Hermitian framework. Closedness is used explicitly inside this Kähler theorem.

Proof:

The numerical statement is: Let Z be a connected compact Kähler manifold of dimension k>=1, and A,B nef real (1,1) Bott–Chern classes. If A^k-4k A^{k-1} B>0, then A-B is big.

\begin{proof}
We give the argument through Gauduchon duality and the smooth
Monge--Amp\`ere equation, following the estimate of \cite{Xiao15}.
If $k=1$, nefness gives $B\geq0$ as an intersection number, so
$\int_Z(A-B)>0$. The Poisson equation gives a positive smooth
representative of this class. We henceforth assume $k\geq2$.

Fix a K\"ahler form $\omega_Z$. By continuity of intersection numbers,
choose $\eta>0$ so small that, with $B'=B+\eta\{\omega_Z\}$,
\[
 A^k>4kA^{k-1}\cdot B'.
\]
For each sufficiently small $\varepsilon>0$, nefness gives K\"ahler
forms $a_\varepsilon\in A+\varepsilon\{\omega_Z\}$ and
$b_\varepsilon\in B'+\varepsilon\{\omega_Z\}$. Set
\[
 c_\varepsilon=(A+\varepsilon\{\omega_Z\})^k,
 \qquad
 N_\varepsilon=(A+\varepsilon\{\omega_Z\})^{k-1}
                    \cdot(B'+\varepsilon\{\omega_Z\}).
\]
Choose and fix $\varepsilon$ so small that
$c_\varepsilon>4kN_\varepsilon>0$.
We will show that $A-B'$ is pseudoeffective.

Let $\Gamma$ be any smooth strictly positive $(k-1,k-1)$-form with
$\ddc\Gamma=0$. Rescale it so that
$\int_Z b_\varepsilon\wedge\Gamma=1$, and put
$\mu=b_\varepsilon\wedge\Gamma$. This is a smooth positive probability
measure. By \cref{thm:tw-smooth}, there is a smooth function $v$ such that
\[
 \widetilde a=a_\varepsilon+\ddc v>0,
 \qquad \widetilde a^k=c_\varepsilon\mu.
\]
Indeed, the initially unknown normalization constant is
$c_\varepsilon$ by Stokes' theorem. Closedness also gives
\[
 \int_Z\widetilde a^{k-1}\wedge b_\varepsilon=N_\varepsilon.
\]
Thus the smooth positive function
\[
 H=\frac{\widetilde a^{k-1}\wedge b_\varepsilon}{\mu}
\]
has $\mu$-integral $N_\varepsilon$. The set
$E=\{H>2N_\varepsilon\}$ has $\mu(E)\leq\tfrac12$.

At a point of $Z\setminus E$, let $\lambda_1,\ldots,\lambda_k$ be
the eigenvalues of $\widetilde a$ relative to $b_\varepsilon$. The
identity for the ratio of wedge powers gives
\[
 \frac1k\sum_{i=1}^k\lambda_i^{-1}
 =\frac{\widetilde a^{k-1}\wedge b_\varepsilon}{\widetilde a^k}
 =\frac{H}{c_\varepsilon}
 \leq\frac{2N_\varepsilon}{c_\varepsilon}.
\]
Each summand is positive, hence every
$\lambda_i\geq c_\varepsilon/(2kN_\varepsilon)$. Consequently,
\[
 \widetilde a\geq
 \frac{c_\varepsilon}{2kN_\varepsilon}b_\varepsilon
 \quad\text{on }Z\setminus E.
\]
Since $\Gamma>0$ and $\ddc\Gamma=0$, integration yields
\[
 \begin{split}
 \int_Z a_\varepsilon\wedge\Gamma
 &=\int_Z\widetilde a\wedge\Gamma\\
 &\geq\frac{c_\varepsilon}{2kN_\varepsilon}\mu(Z\setminus E)
 \geq\frac{c_\varepsilon}{4kN_\varepsilon}>1
 =\int_Zb_\varepsilon\wedge\Gamma.
 \end{split}
\]
The form $a_\varepsilon-b_\varepsilon$ represents the fixed class
$A-B'$: the two $\varepsilon\{\omega_Z\}$ terms cancel. The displayed
inequality holds for every Gauduchon test form, so \cref{thm:lamari}
provides a closed positive current $S\in A-B'$. Then
$S+\eta\omega_Z\in A-B$ dominates $\eta\omega_Z$, proving bigness.
\end{proof}

The Gauduchon form serves two purposes in this proof: it tests
pseudoeffectivity, and it defines the right-hand side of the
Monge--Amp\`ere equation. Closedness makes $c_\varepsilon$ and
$N_\varepsilon$ independent of that test. This is the precise point
at which this argument needs more than a Gauduchon reference metric.


The remaining proof of the main theorem is the accepted source argument, transformed in the files listed above. Check the complete adaptation map and all changed interfaces before final verdict. Preserve every existing audit.
