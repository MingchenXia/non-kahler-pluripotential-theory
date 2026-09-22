Run_id: strong_gauduchon_criterion_01

Run scope: Bounded verification through the normal Rethlas workflow. The parent owns manuscript edits, build and release. Restrict writes to normal verifier tools, memory and results. Do not alter book/editorial/blueprint/status/changelog files, frozen inputs, original references or historical reports. Do not commit or push.

Statement: Verify the complete reconstructed criterion that a connected compact complex n-manifold, n>=2, admits a strongly Gauduchon metric if and only if it has no nonzero positive de Rham-exact (1,1)-current. Check also the equivalence of definitions, the zero Lee--Gauduchon class computation, and the equivalent formulation in terms of nonzero pseudoeffective Bott--Chern classes having nonzero de Rham image. This is a known criterion, not a novelty claim.

Definitions: d^c=i/(4 pi)(bar-partial minus partial), so d d^c=i/(2 pi) partial bar-partial. A Gauduchon metric gamma satisfies ddc(gamma^(n-1))=0. Its Lee--Gauduchon class is [d^c(gamma^(n-1))] in real degree-(2n-1) de Rham cohomology. A real smooth BC class in bidegree (1,1) is pseudoeffective when represented by a closed positive (1,1)-current. Smooth and current BC cohomology agree, as usual. The image of the class in de Rham cohomology is represented by the same current. Balanced means d(gamma^(n-1))=0.

Accepted classical/internal inputs:
1. Hahn--Banach separation of a nonempty open convex set from a disjoint closed linear subspace in a real locally convex space. The separator is nonzero and continuous; linearity forces vanishing on the subspace, and conicity permits the inequality to have zero separating constant. Check its application to the actual spaces in this proof.
2. On a compact manifold, the continuous dual of the real Frechet space of smooth real k-forms is the space of real degree-(2n-k) currents. Distributional Stokes is valid. The current de Rham theorem and Poincare duality imply that a closed current whose pairings with all smooth closed complementary forms vanish is exact. A complex manifold has its canonical real orientation. These classical theorems are accepted; no Hodge-type degeneration or ddbar lemma is assumed.
3. Every strictly positive smooth (n-1,n-1)-form has a unique smooth positive (n-1)st root, obtained by the positive definite cofactor matrix formula. In this bidegree the usual weak/strong positivity notions agree. The strict positive cone is open in the smooth topology on a compact manifold. Gauduchon's theorem supplies a Gauduchon metric. A nonzero positive (1,1)-current has strictly positive mass against every smooth strictly positive (n-1,n-1)-form; this follows from its local positive matrix of measures.

No theorem of Popovici is accepted as a black-box premise. The parent consulted the user-supplied private working reference and independently read the entire original proof of this particular criterion, tracing Proposition1.2 of arXiv:1009.5408v1 to Lemma3.2 and the proof of Proposition3.3 on pages16--17 of arXiv:0910.2032v1. The draft below reconstructs the argument directly from the stated classical inputs. The private reference is not supplied here or integrated into the book. No modification or deformation result from those papers is used.

Important checks: The relevant real smooth-form space has all complementary type components; separation must force the current to be of type (1,1) by varying the other components freely. Positivity on the open cone must imply positivity on every semipositive test by epsilon addition. Annihilating closed forms is stronger than being closed and must be used to prove exactness. Check the sign and normalization of the explicit d^c primitive. The positive-root step requires n>=2, which is explicit. No bounded-mass hypothesis, nonlinear product, Kahler metric or regularity of a general positive current may be inferred.

Proof:

\begin{definition}\label{def:strongly-gauduchon}
A Hermitian metric $\gamma$ is \emph{strongly Gauduchon} if $\gamma^{n-1}$ is the $(n-1,n-1)$-component of a smooth closed real $(2n-2)$-form.
\end{definition}

Writing that form as
\[
 \Theta=\gamma^{n-1}+\beta+\overline\beta,
 \qquad \beta\text{ of type }(n,n-2),
\]
shows that the definition is equivalent to $\partial(\gamma^{n-1})$ being $\bar\partial$-exact: its value is $-\bar\partial\beta$. Conversely, this equation and its conjugate give $\mathrm{d}\Theta=0$, because the remaining types exceed dimension $n$. Applying $\bar\partial$ also shows that $\gamma$ is Gauduchon. Every balanced metric is strongly Gauduchon by taking $\Theta=\gamma^{n-1}$.

\begin{proposition}\label{prop:lee-strong-obstruction}
A strongly Gauduchon metric has zero Lee--Gauduchon class. A connected
compact complex manifold of dimension $n\geq2$ admits such a metric if
and only if it has no nonzero positive de Rham-exact $(1,1)$-current.
\end{proposition}
\begin{proof}
Put $\Gamma=\gamma^{n-1}$ and use $\beta$ as above. In our normalization,
\[
 \dc\Gamma
 =\frac{\mathrm i}{4\pi}
       (\bar\partial\beta-\partial\overline\beta)
 =\mathrm{d}\!\left(\frac{\mathrm i}{4\pi}
                              (\beta-\overline\beta)\right).
\]
Thus $[\dc\Gamma]=0$.

\Needspace{8\baselineskip}
For the obstruction, suppose $T=\mathrm{d}S\geq0$ is nonzero and $\Theta$ is a closed real form with strictly positive $(n-1,n-1)$-part $\Gamma$. Type considerations and distributional Stokes give
\[
 \int_XT\wedge\Gamma
 =\int_XT\wedge\Theta=0.
\]
The first integral is strictly positive because $T\ne0$ and $\Gamma>0$,
a contradiction. Such a current also obstructs balanced metrics, since
these are strongly Gauduchon.

For the converse, suppose that no strongly Gauduchon metric exists.
In the real Fr\'echet space of smooth $(2n-2)$-forms, let $\mathcal Z$
be the closed subspace of closed forms and let $\mathcal P$ be the open
convex cone of forms with strictly positive $(n-1,n-1)$-part.
This cone is nonempty, since it contains $h^{n-1}$ for any Hermitian
metric $h$. The two sets are disjoint: the positive $(n-1)$st root of
the pure-type part of a form in their intersection would be a strongly
Gauduchon metric. Hahn--Banach separation therefore gives a nonzero
real current $T$ of degree two such that
\[
 T|_{\mathcal Z}=0,\qquad T(\Theta)\geq0\quad(\Theta\in\mathcal P).
\]
Fix $\Theta_0\in\mathcal P$. If a real form $\Psi$ has zero
$(n-1,n-1)$-part, then $\Theta_0+t\Psi\in\mathcal P$ for every
$t\in\R$, so $T(\Psi)=0$. Thus $T$ is of type $(1,1)$.
For any semipositive $(n-1,n-1)$-form $\Gamma$,
$\Gamma+\varepsilon\Theta_0\in\mathcal P$ when $\varepsilon>0$.
Letting $\varepsilon\downarrow0$ proves $T(\Gamma)\geq0$.

Since $T$ annihilates every exact test form, it is closed. The de Rham
theorem for currents and Poincar\'e duality identify its cohomology
class with its pairings against closed complementary forms. All these
pairings vanish, so $T=\mathrm{d}S$ for a real current $S$.
This gives the required nonzero positive exact current and proves the
converse. The argument uses full currents and smooth test forms;
no non-pluripolar product is involved.
\end{proof}

Equivalently, every nonzero pseudoeffective Bott--Chern class must have
nonzero de Rham image. Indeed, a positive current representing the zero
Bott--Chern class has zero pairing with a Gauduchon metric and must vanish.
Thus the nonzero positive exact currents in the criterion correspond
precisely to the nonzero pseudoeffective classes with zero de Rham image.

