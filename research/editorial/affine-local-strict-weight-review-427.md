# Local affine regularity and strict weights — review 427

The exact Narzillaev v1 preprint, arXiv:2609.23530, gives a local strict-weight estimate in Theorem 4.2 (p.10) and an upper-semicontinuous-weight criterion in Lemma 4.1 (p.10). The estimate depends on a relative-extremal characterization recalled on p.5. The argument below reconstructs that characterization by explicit logarithmic pasting and the already checked pole barrier, instead of importing its unreviewed historical proof. It then proves the two weighted statements at their precise scope. No novelty or original-problem closure is claimed.

## Relative and global extremal values

For a compact E inside an open Euclidean ball B in C^n, define

\[
 h_{E,B}=\sup\{u\in\operatorname{PSH}(B):
                    -1\le u\le0,\ u|_E\le-1\}.
\]

The constant -1 is admissible. The local upper-envelope theorem gives a genuine bounded plurisubharmonic h^*_{E,B} between -1 and 0. This general definition belongs with the Chapter 1 local foundations; the growth-class comparison below belongs in Chapter 12. The lower truncation does not change the raw supremum, since taking max(u,-1) preserves every upper and obstacle constraint.

Fix a point a and 0<r<R, put B=B(a,R), and let E be a compact subset of the closed inner ball. If E is pluripolar, the checked logarithmic pole barrier gives b in L_1 with b=-infinity on E. Choose a finite upper bound C for b on B. Then

\[
 u_\epsilon=\max\{-1,\epsilon(b-C)\}
\]

is an admissible relative competitor and tends to zero almost everywhere as epsilon decreases to zero. Since h^*_{E,B} dominates each competitor, almost-everywhere canonical order gives h^*_{E,B}=0 everywhere on B. In particular its value at a cannot be -1.

Suppose now E is non-pluripolar and write V_E^* for its genuine unweighted growth-one extremal function. Its finiteness and local upper bound follow from the checked affine/projective correspondence. Choose M>=1 with V_E^*<=M on B. If v is a raw global competitor for the zero obstacle on E, then

\[
 \max\{-1,v/M-1\}
\]

is a relative competitor. Taking suprema and regularization near a gives

\[
 h^*_{E,B}(a)\ge\max\{-1,V_E^*(a)/M-1\}.
\]

Thus h^*_{E,B}(a)=-1 implies V_E^*(a)=0, since V_E^*>=0.

Conversely choose r<R_0<R and k>0 such that k log(R_0/r)>1. The logarithmic barrier L(z)=k log(norm(z-a)/r) is plurisubharmonic and has growth allowance k. For each relative competitor u, put v=u+1 and define W=max(v,L) on B and W=L outside B. On the outer collar, L>1>=v, so the pieces agree and the psh gluing lemma applies. On E, v=0 and L<=0, hence W=0. On the open inner ball, W=v. Consequently W/k is a global growth-one competitor on E and

\[
 V_E^*(a)\ge\frac{1+h^*_{E,B}(a)}k.
\]

The same k works for every relative competitor. It follows that V_E^*(a)=0 implies h^*_{E,B}(a)=-1. These two inequalities prove the relative/global zero-value equivalence. No product formula, thinness theorem or noncompact-set removal statement is used.

## Local pluriregularity and upper-semicontinuous weights

For a non-pluripolar compact K and a point a in K, put K_r=K intersect the closed ball B(a,r). Local pluriregularity means that every K_r is non-pluripolar and V^*_{K_r}(a)=0. It is enough to check arbitrarily small positive radii: monotonicity of the compact-set extremals handles the larger pieces. The relative/global comparison proves the equivalent h^*_{K_r,B(a,R)}(a)=-1 conditions on small concentric balls, and excludes polar pieces.

Let q be bounded and upper semicontinuous on K, and let delta be a global raw-contact parameter, so V_{delta,K,q}=q everywhere on K. If a is locally pluriregular and M_r=sup_{K_r}q, then

\[
 q(a)\le F_{\delta,K,q}(a)
 \le F_{\delta,K_r,q}(a)
 \le M_r+\delta V^*_{K_r}(a)=M_r.
\]

The lower bound uses raw contact. The upper bounds use monotonicity in the compact set and the obstacle sandwich. Upper semicontinuity and inclusion of a imply M_r decreases to q(a), giving equality. Every compact subset inherits raw contact by sandwiching its raw envelope between the original raw envelope and its obstacle. Applying the same bounds with r<s proves F_{delta,K_s,q}(a)=q(a) for every s>0. Thus the conclusion is both global and local weighted regularity at the stated point. Raw contact persists for all later parameters, so the criterion also gives persistence and zero initial growth derivative there.

## Local strictness gives a quantitative defect

Let tau>0, let Psi be continuous on C^n and belong to L_tau, and put q=Psi restricted to K. Suppose for some R,c>0,

\[
 \mathrm{dd}^c\Psi\ge c\omega_0\quad\hbox{on }B(a,R),
 \qquad \omega_0=\mathrm{dd}^c\|z\|^2
\]

in the book convention. Both the source operator and its omega_0 are pi times these book quantities, so the coefficient c and the estimate below are unchanged. The inequality means exactly that Psi-c norm(z-a)^2 is plurisubharmonic on the ball. The global extension remains essential to the construction.

For 0<r<R put E=K_r and take a relative competitor u. On B=B(a,R),

\[
 H_u(z)=\Psi(z)-c\|z-a\|^2+cr^2(u(z)+1)
\]

is plurisubharmonic. Since u<=0, H_u<=Psi when norm(z-a)>=r. Paste max(Psi,H_u) on B with Psi outside B. The pieces agree on an outer collar and give a global W in L_tau. On E, u=-1 implies H_u<=Psi; on the remainder of K the distance bound does the same. Hence W=q everywhere on K and is a raw competitor for each delta>=tau. Taking the supremum of H_u near a and then regularizing, using continuity of Psi, gives

\[
 F_{\delta,K,q}(a)-\Psi(a)
 \ge cr^2\bigl(1+h^*_{K_r,B(a,R)}(a)\bigr)
 \qquad(\delta\ge\tau).
\]

This proves the source estimate with the same closed inner-ball convention. Psi itself also shows [tau,infinity) is contained in the raw contact ray. If regular contact holds at one delta>=tau, the left side is zero, so every displayed relative value is -1. The direct relative/global equivalence proves local pluriregularity. Conversely local pluriregularity and the upper-semicontinuous-weight criterion prove regularity for every delta>=tau, including tau. Thus the exact source persistence conclusion follows without borrowing the unreviewed historical characterization. In this regular case V_K^*(a)=0 by compact-set monotonicity and D_tau(a)=0 by persistence.

If Psi is C^2 and regular contact holds at tau but fails later, then (dd^c Psi)^n(a)=0. Indeed, Psi is plurisubharmonic, so its smooth Hessian is semipositive. A nonzero top power at a would make it positive definite there; continuity gives a positive lower bound c omega_0 on a neighborhood. The proved strict-weight criterion would force persistence, a contradiction. This is a pointwise degeneracy assertion, not a classification of all semidefinite extending weights.

## Actual source scope and continuation

Fresh complete text pages 2--5 and 9--11 are read, with six actual images 3,4,5,9,10,11. The cached exact 22-page PDF has SHA256 88fd47ac7cd605b2d796facfc1b316222965ca924e01ba8b8a54db00cfd7fba5. The latest abstract is freshly retrieved with HTTP200, SHA256 c6b6f699e80dff0cb17ee78046d0e483308264fe216ed9288f826218799c6786, and still lists only v1, submitted 20 September 2026. No fresh full-22-page or entire cited-proof-tree review is claimed. The primary's later thinness/plurifine classifications remain outside adoption.

The complete 250-line local-capacity parent is read as placement context. The maxima/gluing/canonical-order and upper-envelope facts are read in the existing maxima input; the local compactness prefix is supporting context. The six-input affine subsection retains its complete 426 review. These are scoped reads, not a new recursive Chapter1/12 certification. The accepted global Josefson foundation remains explicit through the existing pole barrier.

The next unit places the general relative-extremal definition in Chapter1, then the direct affine comparison, local regularity criterion, strict-weight estimate and pointwise Hessian consequence in Chapter12, with exact Chapter33 attribution and the complete manuscript release checks.

All 47 direct obligations and both complete mathematical reads pass at the stated dependency scope. All 331 tracked book files and 1004 proofs, both catalogues/manifests and 451 protected sources remain exact. The package has 2154 archive entries and 2153 checksum-validated current payloads; its 328 book-source files match the actual 426 empty reconstruction. No new author build, native call, fresh reconstruction or publication is claimed. Normal private synchronization follows actual diff review.
