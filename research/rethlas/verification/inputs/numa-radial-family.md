Run_id: numa_radial_family_01

Statement: Independently audit the full proof of an explicit uncountable family of distinct normalized C1,1 solutions for the smooth degenerate NUMA projective-threefold equation, including an explicit involution-invariant solution. This is a proposed derived consequence of the user's supplied construction, not a result attributed to the source paper. No novelty claim or convergence of positive-exponent approximation is made.

Accepted prerequisite: the complete construction in /Users/mingchen/Non-Kahler/book/author/section_degenerate_nonuniqueness.tex has passed degenerate_nonuniqueness_01 with zero errors/gaps. Read it to recover every coefficient and support condition precisely. In particular X=P(C2 directsum C2), r=log|A|2/|B|2 on U, P,Q,R rank-one independent smooth semipositive forms, ddcG=G'(P-Q)+G''R, cube=6xyzPQR. On [-1,1], x=p+a,y=p+b,z=z0=sqrt((p')2+chi2); p even positive inside flat ends,p'>0negativehalf,<0positivehalf; a=0r>=-1/3,b=0r<=1/3; z0even>=|p'| and strictnearzero. Smooth omega=omega0+ddcrho is positive, source density fomegaFS3 equals omega0^3 outside band and zero on band. Smooth original solutions slopes +/-p. Allforms/bookconvention ddc=i/(2pi)partialbarpartial fixed. Choosing rho even is permitted by choosing its cutoff even. Do not reprove that prerequisite but check ALL uses.

Standard real Lipschitz/Sobolev calculus and bounded local Bedford--Taylor uniform continuity may be used. The proof independently explains a.e Hessian/product identification; verify that distributional Hessians and products carry no extra transition-surface measure and that the regularity is genuinely C1,1 globally. Check signs, root existence, parameter distinctness, global extension, invariance, and exact equality of data. Do not assume a radial average of two solutions solves the equation. No new PDE result should be imported.

Proof:

\section{A family of solutions from the radial equation}
\label{sec:numa-radial-family}

The scalar coefficients of the preceding projective example also allow a direct construction of further solutions. It is useful to make the construction explicit: no compactness argument is needed, and the regularity at the transition hypersurfaces can be checked.

Retain all the data of \cref{thm:degenerate-hermitian-nonuniqueness}. In particular, on $-1<r<1$ we have
\[
 x=p+a,\qquad y=p+b,\qquad z=z_0,
 \qquad p'=q,\quad z_0\geq|q|.
\]
Both $p$ and $z_0$ are even, $p>0$ in the interior, and $p'<0$ on $(0,1)$. The strict inequality $z_0>|q|$ holds on a neighborhood of zero. Hence
\begin{equation}\label{eq:numa-half-excess}
 \int_0^1z_0(r)\,dr>\int_0^1|p'(r)|\,dr=p(0).
\end{equation}

\begin{proposition}\label{prop:numa-radial-continuum}
The same smooth background and smooth density in \cref{thm:degenerate-hermitian-nonuniqueness} admit uncountably many distinct normalized $C^{1,1}$ solutions of
\[
 \mathrm{MA}_\omega(u)=f\omega_X^3.
\]
They include a directly constructed solution invariant under the block exchange $\iota[A:B]=[B:A]$, if the cutoff defining $\rho$ is chosen even. This assertion does not claim that the additional solutions are smooth.
\end{proposition}
\begin{proof}
Choose $-1<I<0<J<1$ satisfying
\begin{equation}\label{eq:numa-transition-balance}
 \int_I^J z_0(r)\,dr=p(I)+p(J).
\end{equation}
We first show there are an interval's worth of choices. For fixed $I$, define
\[
 K(I,J)=\int_I^Jz_0(r)\,dr-p(I)-p(J).
\]
At $I=0$ we have $K(0,0)=-2p(0)<0$ and $K(0,1)>0$ by \eqref{eq:numa-half-excess}. Continuity gives $\epsilon>0$ such that these opposite signs persist for every $I\in[-\epsilon,0]$. For $0<J<1$,
\[
 \partial_JK(I,J)=z_0(J)-p'(J)>0.
\]
The intermediate value theorem therefore supplies a unique $J=J(I)\in(0,1)$ for every $I\in[-\epsilon,0)$. Shrink $\epsilon$ below one.

For any pair satisfying \eqref{eq:numa-transition-balance}, define the slope on $[-1,1]$ by
\[
 h_{I,J}(r)=
 \begin{cases}
 p(r),&-1\leq r\leq I,\\
 p(I)-\displaystyle\int_I^r z_0(s)\,ds,&I\leq r\leq J,\\
 -p(r),&J\leq r\leq1,
 \end{cases}
\]
and extend it by zero outside that interval. The balance identity makes it continuous at $J$, and continuity at $I$ is immediate. Each piece has bounded derivative. Thus $h_{I,J}$ is globally Lipschitz; it is flat at $\pm1$. Let $G_{I,J}$ be any primitive. It is $C^{1,1}$ and constant at each end of the real line. Consequently $G_{I,J}(r)$ extends to a global $C^{1,1}$ function on $X$, smooth near $X\setminus U$.

On the middle interval the slope lies between $-p$ and $p$. Indeed,
\[
 (h_{I,J}-p)'=-z_0-p'\leq0,
 \qquad
 (h_{I,J}+p)'=-z_0+p'\leq0.
\]
The first difference starts at zero at $I$; the second ends at zero at $J$. These two inequalities give $h_{I,J}\leq p$ and $h_{I,J}\geq-p$, respectively.

Put $\widetilde u_{I,J}=G_{I,J}(r)-\rho$. Its solution form is, almost everywhere on $U$,
\begin{equation}\label{eq:numa-slope-form}
 \omega+\ddc\widetilde u_{I,J}
 =\omega_0+\ddc G_{I,J}(r)
 =(x+h_{I,J})P+(y-h_{I,J})Q+(z+h_{I,J}')R.
\end{equation}
On $I<r<J$, the first two coefficients are nonnegative because $x=p+a$, $y=p+b$ and $-p\leq h_{I,J}\leq p$. The third is zero. On $-1<r<I$, we have $h_{I,J}=p$ and $b=0$, since $I<0$; the second coefficient is zero and the others are nonnegative, using $z_0+p'\geq0$. On $J<r<1$, we have $h_{I,J}=-p$ and $a=0$; the first coefficient is zero and the others are nonnegative, using $z_0-p'\geq0$. Outside the band, $h_{I,J}=h_{I,J}'=0$, so the form equals $\omega_0$.

There is no additional hypersurface term in \eqref{eq:numa-slope-form}: $G_{I,J}$ is $C^{1,1}$, and its first derivative is continuous at both transition points. Its distributional Hessian is the bounded almost-everywhere Hessian. The preceding coefficient inequalities therefore prove $\omega+\ddc\widetilde u_{I,J}\geq0$ as a current.

For completeness, the Bedford--Taylor product of a $C^{1,1}$ quasi-plurisubharmonic potential agrees with the almost-everywhere wedge of its Hessian. On a smaller coordinate ball, add a fixed smooth quadratic to make the potential plurisubharmonic and convolve. The Hessians of the convolutions are uniformly bounded and converge to the weak Hessian in every finite $L^r$ space. Their finite products therefore converge in $L^1$. The potentials converge uniformly, so bounded Bedford--Taylor continuity identifies the same limit as their pluripotential product. Expanding off the smooth quadratic proves the assertion for the original nonclosed background as well.

The rank-one formula \eqref{eq:numa-rank-frame} now shows that the cube of \eqref{eq:numa-slope-form} is zero almost everywhere on the band, and equals $\omega_0^3$ off it. These are exactly the defining values of $f\omega_X^3$ in the preceding construction. Thus $\widetilde u_{I,J}$ solves the equation. Subtracting its supremum gives a normalized solution $u_{I,J}$.

Different $I$ in the interval above give different normalized solutions. If $I_1<I_2<0$ and $I_1<r<I_2$, then the slope belonging to $I_2$ is $p(r)$, whereas
\[
 p(r)-h_{I_1,J(I_1)}(r)
       =\int_{I_1}^r(p'(s)+z_0(s))\,ds>0,
\]
because $p'>0$ on $(-1,0)$. The two primitives therefore cannot differ by a constant. An interval contains uncountably many parameters, proving the first assertion. None of these slopes is identically $p$ or identically $-p$, so the constructed solutions are also distinct from the original two smooth solutions.

Finally, the function
\[
 L(t)=\int_0^t z_0(r)\,dr-p(t),\qquad 0\leq t\leq1,
\]
is negative at zero, positive at one, and strictly increasing on $(0,1)$. Its unique zero $t_*$ gives an admissible symmetric pair $I=-t_*$, $J=t_*$. Evenness of $z_0$ and $p$ then makes $h_{I,J}$ odd: on the middle interval it is $-\int_0^r z_0(s)\,ds$. Choose its primitive even. If $\rho$ is even, $G_{I,J}(r)-\rho$ and its normalized version are fixed by $\iota$. This proves the explicit invariant-solution assertion.
\end{proof}

The family shows that the ambiguity in the degenerate equation can persist within the regularity class $C^{1,1}$. The transition hypersurfaces of these additional solutions lie inside the zero-density band. Positive-exponent approximation is still a separate selection problem: the construction does not identify its limit with one particular member of this family.


Follow AGENTS.md: every deduction sequentially, required reference checks if a new reference is used, persist all checks and full readable report. Write results/numa_radial_family_01/verification.json via verification MCP. Do not edit book or prior results. Correct iff zero errors/gaps under the explicit prerequisite.
