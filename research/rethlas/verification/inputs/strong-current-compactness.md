Run_id: strong_current_compactness_01

Run scope: Bounded verification through the normal Rethlas workflow. The parent owns manuscript edits, build and release. Restrict writes to normal verifier tools, memory and results. Do not alter book/editorial/blueprint/status/changelog files, frozen inputs, original references or historical reports. Do not commit or push.

Statement: Check the supplied corollary: on a connected compact complex n-manifold, n>=2, existence of a strongly Gauduchon metric is equivalent to a bound of the linear mass of every closed positive (1,1)-current by a fixed constant times the norm of its degree-two de Rham class. Under this condition prove weak compactness for the family with classes in any fixed compact subset of H^2_dR, and prove that the de Rham image of the pseudoeffective Bott--Chern cone is closed, convex and contains no nonzero line. This is an elementary consequence of the already reconstructed criterion, not a novelty claim or a theorem on varying complex structures.

Definitions: A strongly Gauduchon metric gamma has gamma^(n-1) as the (n-1,n-1) component of a smooth closed real (2n-2)-form Theta. A real Bott--Chern (1,1) class is pseudoeffective if it has a closed positive (1,1)-current representative. Its de Rham image is the class of the same current. The mass against a fixed Hermitian h is the integral T wedge h^(n-1); h need not be Gauduchon. The norm on H^2_dR is arbitrary but fixed.

Accepted inputs:
1. The full criterion proved in the preceding book proposition: X admits a strongly Gauduchon metric iff there is no nonzero positive de Rham-exact (1,1)-current. The entire original proof of this particular Popovici criterion was independently read after consulting the user's private reference. The book's complete reconstruction was checked in the correct report strong_gauduchon_criterion_01. No other result of Popovici is accepted or needed. For clarity, the forward implication of the new corollary should follow directly from the defining closed form, without using an extra theorem.
2. Current de Rham cohomology agrees with smooth cohomology; Poincare duality identifies real degree-two classes with pairings against a finite smooth closed basis of complementary cohomology. In particular, verify explicitly that weak convergence of closed currents gives convergence of these classes. Smooth and current Bott--Chern cohomology agree in (1,1).
3. A family of positive (1,1)-currents with uniformly bounded mass is relatively weakly compact. Positivity, type and closedness pass to weak limits. A positive current of zero mass is zero. Comparison of strictly positive smooth forms on a compact manifold gives uniform constants. These standard current facts are accepted.

Checks: h need not be closed or Gauduchon, because it is compared to the pure-type part of a closed complementary form. A compact set of de Rham classes is closed and bounded. The proof must not assume injectivity of the full Bott--Chern-to-de-Rham map or assert uniqueness of a current in a class. Treat a zero-dimensional H^2 group and an empty family correctly. Distinguish the linear mass of closed positive currents from nonlinear Monge--Ampere mass in a nonclosed background. No bounded-mass property, positive-lower-mass property or uniform estimate in a varying complex structure may be inferred.

Proof:

The criterion also characterizes when de Rham classes control the linear
masses of closed positive currents.

\begin{corollary}\label{cor:strong-gauduchon-current-compactness}
Let $X$ be a connected compact complex manifold of dimension $n\geq2$.
Fix a Hermitian metric $h$ and a norm on $H^2_{\mathrm{dR}}(X,\R)$.
Then $X$ admits a strongly Gauduchon metric if and only if there is a
constant $C>0$ such that every closed positive $(1,1)$-current $T$ satisfies
\begin{equation}\label{eq:strong-gauduchon-class-mass}
 \int_XT\wedge h^{n-1}\leq C\|[T]_{\mathrm{dR}}\|.
\end{equation}
Under this condition, the family of closed positive $(1,1)$-currents
whose de Rham classes belong to a fixed compact set is weakly compact.
The image of the pseudoeffective Bott--Chern cone in
$H^2_{\mathrm{dR}}(X,\R)$ is a closed convex cone containing no nonzero line.
\end{corollary}
\begin{proof}
Suppose $\gamma$ is strongly Gauduchon, and choose a smooth closed real
form $\Theta$ whose $(n-1,n-1)$-part is $\gamma^{n-1}$.
Compactness gives $h^{n-1}\leq A\gamma^{n-1}$ for some $A>0$.
Positivity and type then give
\[
 \int_XT\wedge h^{n-1}
 \leq A\int_XT\wedge\gamma^{n-1}
 =A\langle[T]_{\mathrm{dR}},[\Theta]_{\mathrm{dR}}\rangle.
\]
The last pairing is a fixed linear functional on the finite-dimensional
de Rham group, proving \eqref{eq:strong-gauduchon-class-mass}.
Conversely, that bound makes every closed positive de Rham-exact current
zero. Apply \cref{prop:lee-strong-obstruction}.

For the compactness assertion, the bound gives uniformly bounded trace
mass. A weak limit of such currents is positive and closed. Its de Rham
class is the limit of their classes: this follows by pairing against a
finite smooth closed basis of complementary cohomology and using
Poincar\'e duality. Thus the family is also weakly closed, and the usual
weak compactness of positive currents proves the assertion.

Let $c_j$ be a convergent sequence in the image cone, and choose closed
positive representatives $T_j$ with $[T_j]_{\mathrm{dR}}=c_j$.
The compactness assertion gives a closed positive limit representing
the limiting de Rham class. Its Bott--Chern class is pseudoeffective,
so the image cone is closed. Convexity follows from addition and
nonnegative scaling. Finally, if both $c$ and $-c$ lie in the image,
choose positive representatives $T$ and $S$ for them. Their sum is exact,
so \eqref{eq:strong-gauduchon-class-mass} makes $T+S=0$. Positivity gives
$T=S=0$ and hence $c=0$.
\end{proof}
