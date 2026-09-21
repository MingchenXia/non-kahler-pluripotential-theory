# Verification audit: lck_chern_ricci_rigidity_01

## Verdict

**Correct.** No critical errors or proof gaps were detected. This audit checks the reconstructed argument independently of its cited target theorem.

## Hypotheses

The metric is smooth, Hermitian, LCK, Gauduchon and Chern–Ricci flat on a compact complex manifold without boundary, of complex dimension n ≥ 2. The proof uses the stated convention that Vaisman means parallel Lee form.

## Sequential deduction checks

### 1. Input subproof: Gauduchon implies harmonic Lee form

1. Closedness of lambda gives local real potentials f by the Poincare lemma.
2. d(e^-f omega)=e^-f(d omega-df wedge omega)=0; integrability of J and positivity imply e^-f omega is Kahler.
3. For the convention omega(U,V)=g(JU,V), Jlambda=-lambda composed with J and d^c f=Jlambda/(4 pi).
4. The closed pure-type form (e^-f omega)^(n-1) is d^c-closed. Applying the Leibniz rule to omega^(n-1)=e^((n-1)f)(e^-f omega)^(n-1) gives d^c omega^(n-1)=(n-1)d^c f wedge omega^(n-1).
5. In the complex orientation, a unitary real orthonormal coframe gives Jlambda wedge omega^(n-1)=(n-1)! *lambda. Thus d^c omega^(n-1)=(n-1)(n-1)!/(4 pi) *lambda.
6. The coefficient is nonzero for n>=2. Hence dd^c omega^(n-1)=0 iff d(*lambda)=0 iff delta lambda=0 (delta=-*d* on real one-forms in even dimension).
7. Together with d lambda=0 this gives harmonicity for the Hodge Laplacian. There is no normalization or global-potential problem: Jlambda is globally defined.

Result: passed; no errors or gaps.

### 2. Proof opening: definitions and harmonicity

1. A=lambda sharp and B=JA are smooth global vector fields; B flat=Jlambda.
2. The Levi-Civita connection is torsion-free, so S(U,V)-S(V,U)=d lambda(U,V)=0.
3. delta lambda=-tr_g(nabla lambda)=-div A. The verified input subproof implies tr_g S=div A=0.
4. S+ is well defined on real symmetric tensors; no dc factor is built into Jlambda.

Result: passed; no errors or gaps.

### 3. eq:lck-ricci-real: local conformal Ricci formula

1. For real dimension m=2n and gtilde=e^(2u)g, Ric_gtilde=Ric_g-(m-2)(nabla^2 u-du tensor du)-(Delta u+(m-2)|du|^2)g, with Delta=div grad.
2. Taking u=-f/2 gives Ric_gtilde=Ric_g+(n-1)S+(n-1)/2 lambda tensor lambda+(Delta f/2-(n-1)|lambda|^2/2)g.
3. Delta f=tr_g S=0, giving exactly the proposed display. Ricci is a covariant two-tensor, so there is no additional overall conformal factor.

Result: passed; no errors or gaps.

### 4. eq:lck-ricci-real: Chern–Ricci form and normalization

1. Write the unnormalized Chern–Ricci form as rho_g=-i partial barpartial log det(g_{a bar b}). The positive normalization in the question has the same vanishing condition.
2. det(gtilde_{a bar b})=e^-nf det(g_{a bar b}), hence rho_gtilde=rho_g+n i partial barpartial f=n i partial barpartial f.
3. Jdf=i(barpartial-partial)f, so d(Jlambda)=2i partial barpartial f and rho_gtilde=(n/2)d(Jlambda).
4. For a Kahler metric with omega(U,V)=g(JU,V), rho(U,V)=Ric(JU,V) and rho(U,JV)=Ric(U,V). This conversion has the sign used in the proof.

Result: passed; no errors or gaps.

### 5. eq:lck-ricci-real: conformal connection and nabla J

1. The connection change is gtilde_nabla_U V=nabla_U V-(lambda(U)V+lambda(V)U-g(U,V)A)/2.
2. Expand gtilde_nabla J=0 and use g(U,JV)=-g(JU,V). This gives (nabla_U J)V=(lambda(JV)U-lambda(V)JU+g(U,V)JA+g(JU,V)A)/2 exactly.
3. Differentiate Jlambda(V)=-lambda(JV) covariantly to obtain (nabla_U Jlambda)(V)=-S(U,JV)-lambda((nabla_U J)V).

Result: passed; no errors or gaps.

### 6. eq:lck-ricci-real: antisymmetrization and final coefficients

1. Put beta=Jlambda, q=|lambda|^2. Substitution gives (nabla_U beta)(V)=-S(U,JV)+(lambda(U)beta(V)-beta(U)lambda(V)-q omega(U,V))/2.
2. Antisymmetrization gives d beta(U,V)=-S(U,JV)+S(V,JU)+(lambda wedge beta)(U,V)-q omega(U,V).
3. At (U,JV), J(JV)=-V, beta(JV)=lambda(V), lambda(JV)=-beta(V), omega(U,JV)=g(U,V). Symmetry of S therefore gives d beta(U,JV)=S(U,V)+S(JU,JV)-q g(U,V)+lambda(U)lambda(V)+beta(U)beta(V).
4. Multiply by n/2 and solve the conformal Ricci identity for Ric_g: the S coefficient is -(n-1), the S+ coefficient is n, the qg coefficient is -n/2+(n-1)/2=-1/2, the lambda-square coefficient is n/2-(n-1)/2=1/2, and the beta-square coefficient is n/2.
5. All terms in the resulting tensor identity are global, so local derivation proves the global identity without a global conformal factor.

Result: passed; no errors or gaps.

### 7. eq:lck-aa-zero

1. Metric compatibility gives A(|lambda|^2)=2<nabla_A A,A>=2 S(A,A).
2. Since div A=0, div(|lambda|^2 A)=A(|lambda|^2).
3. X is compact without boundary, so the divergence theorem implies integral S(A,A)=0.

Result: passed; no errors or gaps.

### 8. Contracted Bianchi identity and eq:lck-bianchi-integral

1. Integration by parts gives integral <Ric,S>=-integral (div Ric)(A).
2. With the curvature convention in the standard conformal Ricci and Bochner formulas, div Ric=(1/2)d Scal. Therefore integral <Ric,S>=-(1/2)integral A(Scal)=(1/2)integral Scal div A=0.
3. The map T(S)(U,V)=S(JU,JV) is an orthogonal involution on symmetric covariant two-tensors at each point. Thus P=(Id+T)/2 is the orthogonal projection onto its +1 eigenspace, and <S+,S>=|S+|^2.
4. Contracting eq:lck-ricci-real with S gives n|S+|^2-(n-1)|S|^2-q tr(S)/2+S(A,A)/2+n S(B,B)/2.
5. tr S=0 pointwise and integral S(A,A)=0 remove the last two relevant terms and give exactly eq:lck-bianchi-integral.

Result: passed; no errors or gaps.

### 9. Integrated Bochner identity and eq:lck-bochner-integral

1. For the harmonic one-form lambda, the integrated Weitzenbock formula for the nonnegative Hodge Laplacian gives 0=integral |nabla lambda|^2+integral Ric(A,A). The first term is |S|^2.
2. Let q=|lambda|^2. Then g(A,A)=lambda(A)=q, beta(A)=g(JA,A)=0. Consequently -(q/2)g(A,A)+(1/2)lambda(A)^2=0 and (n/2)beta(A)^2=0.
3. S+(A,A)=(S(A,A)+S(B,B))/2, so Ric(A,A)=(1-n/2)S(A,A)+(n/2)S(B,B).
4. Integration and eq:lck-aa-zero give integral |S|^2+(n/2)integral S(B,B)=0 with the proposed sign and coefficient.

Result: passed; no errors or gaps.

### 10. Subtracting the two integral identities: first equality case

1. Subtracting eq:lck-bochner-integral from eq:lck-bianchi-integral yields n integral (|S+|^2-|S|^2)=0. Division by n>0 gives the displayed identity.
2. Orthogonal projection implies |S|^2-|S+|^2=|S-S+|^2>=0 pointwise.
3. The smooth nonnegative function |S-S+|^2 has zero integral against the positive volume measure, hence vanishes at every point; S=S+ everywhere.

Result: passed; no errors or gaps.

### 11. Final equality case and parallel Lee form

1. S=S+ implies S(JU,JV)=S(U,V), so S(B,B)=S(A,A) pointwise even at zeros of lambda.
2. eq:lck-aa-zero now gives integral S(B,B)=0. eq:lck-bochner-integral implies integral |S|^2=0.
3. Smoothness and positivity of volume imply S=nabla lambda=0 everywhere.
4. This is exactly the parallel-Lee definition of Vaisman used in the proof. The conclusion includes lambda=0; if terminology reserves Vaisman for nonzero Lee form, that case is Kahler and the geometric result reads 'Kahler or Vaisman'. The proof establishes the stated parallelism unconditionally.

Result: passed; no errors or gaps.

### 12. Full proof: hypothesis and dependency audit

1. LCK gives a global closed lambda and local Kahler conformal rescalings; no globally defined f is assumed.
2. Gauduchon gives co-closedness, which removes the conformal Hessian trace and licenses both divergence integrations.
3. Chern–Ricci flatness is used precisely to compute the local Kahler Ricci form.
4. n>=2 is needed for the nonzero (n-1) factor in the Gauduchon/Lee equivalence; every later division is by n>0, so n=2 is allowed.
5. Compactness without boundary justifies the divergence theorem and all integrated identities. Smoothness justifies tensor differentiation, integration, and equality everywhere.
6. Connectedness is harmlessly redundant for the parallelism proof: the same argument holds on each compact connected component. It also means the final parallel Lee form has constant norm globally and is either identically zero or nowhere zero.
7. No bounded mass property, positivity of the Ricci tensor, nonvanishing of lambda, or cited target theorem is needed.

Result: passed; no errors or gaps.

## Reference checks

The required arXiv theorem-search service was attempted first and failed with an SSL unexpected-EOF transport error. Built-in web search and direct inspection of the official version-2 text resolved the reference check. This is a tool-service failure, not a mathematical defect.

### Source attribution and opening citation [BO25LCK, Section 4], Theorem A

The source uses d omega=theta wedge omega with closed real theta, Ric(omega)=-i partial barpartial log det omega, Jtheta=-theta composed with J, and (nabla theta)^(1,1)=(nabla theta+nabla theta(J.,J.))/2. Its introduction explicitly reserves 'lcK' for nonexact Lee forms and hence excludes globally conformally Kahler metrics. Its Vaisman condition is Levi-Civita-parallel Lee form within that strict class. Gauduchon here is the condition on the metric, not a choice of Gauduchon connection. The proof's unnormalized Jlambda agrees with the source; d^c f=Jlambda/(4 pi) has already been independently accounted for.

Taking t=0 and using delta lambda=0 in source equation (4) gives exactly eq:lck-ricci-real. Equations (5), (7), and the t=0 equality argument match the reconstructed Bianchi, Bochner, and equality steps. No bounded mass hypothesis occurs in this theorem or its argument.

The source theorem has not been used as a premise. All local tensor identities and integration steps were verified before inspecting the source proof. The only scope difference is the source's strict-lcK convention: the independent reconstructed argument also covers lambda=0. For an exact Lee form lambda=df that is co-closed on compact X, integral |df|^2=-integral f div grad f=0, so lambda=0; consequently the nonzero case automatically has nonexact Lee form and matches the source's scope. Under the proof's explicit parallel-Lee convention, 'Vaisman' includes this zero case; under the source's strict convention state 'Kahler or Vaisman'. This terminology distinction does not invalidate the parallelism conclusion or the attribution of the argument.

### Internal prop:lck-gauduchon and standard Riemannian identities

The content of prop:lck-gauduchon is supplied in the input and verified in statement_checks sequence 1, so no unavailable chapter proposition is being assumed.

These standard identities are not cited to an external paper in the submitted proof. Their exact signs, normalizations, specializations, and required hypotheses were checked directly in the sequential audit. References cited only inside the source paper are not premises of the reconstructed proof.

Primary sources: [official arXiv v2 record](https://arxiv.org/abs/2509.18364v2), [Section 4, Theorem A](https://arxiv.org/html/2509.18364v2#S4), and [archived text](/Users/mingchen/Non-Kahler/research/sources/BO25-LCK-CY.txt:711).

## Independent cross-checks

An independent tensor audit confirmed the connection, conformal Ricci, Chern–Ricci and antisymmetrization calculations. An independent integration audit confirmed the Gauduchon normalization, Bianchi and Bochner signs, and both equality cases. Both reported no error or gap.

## Final findings

- Critical errors: none.
- Gaps: none.
- Repair hints: none required.
- No bounded mass hypothesis is needed.

