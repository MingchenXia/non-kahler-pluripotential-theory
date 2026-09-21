Run_id: primitive_criterion_01

Statement: Let X be a connected compact complex manifold of dimension n>=2 without boundary, and let omega be a smooth real strictly positive (1,1)-form. Write dc=i/(4pi)(bar-partial minus partial), ddc=i/(2pi)partial bar-partial. On H_omega={u in C-infinity(X,R): omega+ddc u>0}, define alpha_u(v)=integral_X v(omega+ddc u)^n. A primitive means a functional E whose restriction to each finite-dimensional affine slice is C2 and whose derivative satisfies DE_u(v)=alpha_u(v). Claim: alpha has a primitive on H_omega if and only if d omega=0. In fact, existence of a primitive on any C2-open neighborhood of 0 in H_omega already forces d omega=0.

Proof:

Lemma 1 (formal symmetry). For a smooth real (n-1,n-1)-form Omega, the bilinear pairing B(v,w)=integral_X w ddc v wedge Omega on smooth real functions is symmetric if and only if d Omega=0.

Proof of Lemma 1. Two applications of Stokes give integral_X ddc f wedge T=integral_X f ddc T for every smooth function f and smooth (n-1,n-1)-form T. Consequently symmetry is equivalent, for each w, to the distributional (and hence smooth) form identity

ddc(w Omega) - ddc w wedge Omega =0.

Indeed, multiplying this expression by an arbitrary test function v and integrating is B(v,w)-B(w,v). Expanding by the Leibniz rule gives

w ddc Omega + dw wedge dc Omega - dc w wedge d Omega=0.

Taking w=1 gives ddc Omega=0. The remaining first-order expression must vanish for every first jet of a real smooth w. By complex linearity it therefore vanishes for the jets of complex smooth w as well. At a fixed point x, choose a global smooth complex function equal near x to a complex linear holomorphic coordinate function. Its first jet can have partial w=lambda arbitrary in Lambda^(1,0), and bar-partial w=0. If a=i/(4pi), the expression above is

2a(partial w wedge bar-partial Omega - bar-partial w wedge partial Omega).

Hence lambda wedge bar-partial Omega=0 for every (1,0)-covector lambda. The exterior product pairing of (1,0)-covectors with (n-1,n)-forms is nondegenerate, so bar-partial Omega=0 at x. Since Omega is real, partial Omega=0 also. As x is arbitrary, d Omega=0. Conversely if d Omega=0, reality and pure type give partial Omega=bar-partial Omega=0, and the product formula above proves symmetry. End proof of Lemma 1.

Lemma 2 (pointwise exterior algebra). If a form T of type (2,1)+(1,2) on a complex n-dimensional vector space satisfies T wedge A^(n-2)=0 for every Hermitian (1,1)-form A in some open neighborhood of a positive form, then T=0.

Proof of Lemma 2. The expression is a polynomial in the real coefficients of the Hermitian form A, so vanishing on an open set implies vanishing for every real (1,1)-form A. Polarization gives T wedge A_1 wedge ... wedge A_(n-2)=0 for arbitrary real (1,1)-forms. By complex linearity this also holds for complex (1,1)-forms. Products of n-2 complex (1,1)-forms span Lambda^(n-2,n-2), by writing each standard basis monomial as a product of dz_j wedge dbar z_k. Thus T wedge B=0 for every B of bidegree (n-2,n-2). The components T^(2,1) and T^(1,2) vanish separately after this wedge because their resulting bidegrees differ. Wedging the identity for T^(2,1) with arbitrary (0,1)-covectors gives T^(2,1) wedge C=0 for every (n-2,n-1)-form C, since these C are spanned by B wedge beta. Perfect exterior pairing to the top-degree space implies T^(2,1)=0. Likewise T^(1,2)=0. For n=2 the assertion is immediate from A^0=1. End proof of Lemma 2.

Main implication. If E is a primitive on an open neighborhood U of 0, equality of mixed second derivatives along any affine two-plane through u in U gives

integral_X w ddc v wedge omega_u^(n-1)=integral_X v ddc w wedge omega_u^(n-1)

for all smooth v,w. Lemma 1 gives d(omega_u^(n-1))=0 for all u in U. Since d omega_u=d omega,

(n-1)d omega wedge (omega+ddc u)^(n-2)=0.

Fix x and a coordinate neighborhood. A real quadratic polynomial times a smooth cutoff equal to one near x realizes any prescribed real (1,1) Hessian H=ddc u(x). Choose a real linear map from the finite-dimensional space of H into these cutoff polynomials. Its C2 norm is bounded by a constant times the coefficient norm of H. Thus, for H sufficiently small, the resulting u belongs to U and to H_omega. It follows that d omega(x) wedge A^(n-2)=0 for every Hermitian A in an open neighborhood of omega(x). Lemma 2 implies d omega(x)=0. This holds at every point, proving d omega=0.

Converse. If d omega=0, define

E(u)=1/(n+1) sum_{j=0}^n integral_X u omega_u^j wedge omega^(n-j).

The derivative of its j-th summand in direction v is integral_X v omega_u^j omega^(n-j)+j integral_X u ddc v omega_u^(j-1)omega^(n-j). All mixed powers in the second term are d- and dc-closed, so integration by parts replaces u ddc v by v ddc u. Using ddc u=omega_u-omega, the derivative becomes (j+1)integral_X v omega_u^j omega^(n-j)-j integral_X v omega_u^(j-1)omega^(n-j+1). Summing telescopes to (n+1)integral_X v omega_u^n. Dividing by n+1 proves DE=alpha. Each restriction is polynomial, hence C2. This proves the theorem.

Verification instructions: This is a bounded audit of the above proof, using the Rethlas verification AGENTS.md and its three verification skills. Initialize and use the verification memory tools. Check all signs, quantifiers, test-function realizations and exterior-algebra steps. This proof uses only Stokes, finite-dimensional polynomial polarization and elementary linear algebra, which are explained here; there are no substantive external research theorem citations. Do not infer correctness from its polished form. Produce results/primitive_criterion_01/verification.json and a concise final report. Do not edit the book or any files outside this copied verification workspace. No new proof-generation task or indefinite search loop is requested.
