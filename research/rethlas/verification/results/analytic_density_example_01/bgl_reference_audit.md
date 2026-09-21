# Section 8: BGL lower-volume comparison and upper mass bound

Audit result: **pass**, with no mathematical error or substantive gap in these two applications.

## Primary sources inspected

- Boucksom–Guedj–Lu, *Volumes of Bott–Chern classes*, arXiv:2406.01090v1: https://arxiv.org/pdf/2406.01090 . Definition 3.1 is on printed page 19; Proposition 3.7 and its proof are on printed page 21. The bounded mass property is defined in Definitions 1.18–1.19, pages 10–11. Section 3 explicitly assumes that property throughout.
- Public HTML: https://arxiv.org/html/2406.01090v1 . Relevant locations are Section 1.5 and Section 3.1, Definition 3.1, Example 3.2 and Proposition 3.7. The HTML displayed an anomalous current date in its header; the theorem text was cross-checked against the archived PDF and published version.
- Published primary article: https://link.springer.com/article/10.1007/s42543-025-00105-2 . Proposition 3.7 retains the same statement. Local archived primary files inspected: `/Users/mingchen/Non-Kahler/research/sources/BGL25.txt` and `BGL25-published.txt`. No previous verification report was used.

## Exact logical scope of the external result

In BGL's notation, smooth real forms theta_1 <= theta_2 and potentials phi_i in PSH(theta_i) satisfying phi_1 <= phi_2 determine currents T_i=theta_i+D phi_i. Proposition 3.7 gives both lower_vol(T_1)<=lower_vol(T_2) and upper_vol(T_1)<=upper_vol(T_2). There is no assumption that the two forms are closed or in one common Bott–Chern class. The section's standing bounded-mass assumption must nevertheless be checked.

Definition 3.1 uses infima/suprema of total non-pluripolar masses over positive currents in the same dd^c class and the same singularity type as the specified current. In terms of a representation T=theta+D phi, its competitors are theta+D psi with psi=phi+O(1).

For the manuscript's use, phi_1=phi_2=0. A global theta-psh competitor psi has psi=0+O(1) if and only if it is bounded. The non-pluripolar mass then agrees with its bounded Bedford–Taylor mass. Thus these two lower volumes are exactly the manuscript's v_-(epsilon Omega) and v_-(omega); there is no identification with a different relative full-mass class.

Both zero potentials are admissible because epsilon Omega and omega are smooth positive forms. They satisfy 0<=0, and the compactness comparison supplies epsilon Omega<=omega. Smooth forms are quasi-closed in BGL's sense since their exterior derivatives are smooth; omega need not be closed. Proposition 3.7 therefore supplies the desired inequality in the asserted direction.

For epsilon Omega, closedness makes every bounded potential's total mass equal to the mass of the background, by expanding and integrating dd^c-exact terms (or BGL Example 3.2). Hence v_-(epsilon Omega)=epsilon^n integral_X Omega^n>0.

## Upper mass bound and the standing bounded-mass hypothesis

Fix a bounded omega-psh potential a. Write T=omega+dd^c a>=0 and Delta=C Omega-omega>=0. Then C Omega+dd^c a=T+Delta>=0. Bounded Hermitian mixed products are multilinear and positive on positive factors, so

    (T+Delta)^n-T^n = sum_{j=1}^n binom(n,j) T^(n-j) wedge Delta^j >= 0.

The potential a is also C Omega-psh and bounded. Closedness of C Omega gives integral_X(C Omega+dd^c a)^n=C^n integral_X Omega^n. Taking the supremum proves v_+(omega)<infinity with a constant independent of a. In particular the same bound holds for every smooth omega-psh test, which directly establishes the bounded mass property required by BGL; no extra inference concerning other metrics is needed. All steps work with the product Kahler form Omega_n in higher dimensions.

## Operator normalization

The published BGL paper states on its second PDF page that d^c=i(barpartial-partial), so its D=dd^c=2i partial barpartial. The manuscript uses dd^c=i/(2pi) partial barpartial, hence D=4pi dd^c. The bijection a -> a/(4pi) preserves each solution/current form, positivity, boundedness, equivalent singularity types, and total mass. It sends both zero potentials to zero. There is therefore no hidden multiplicative factor in either v_- or v_+ or in epsilon^n integral Omega^n.

## Reference-search audit trail

1. Read the required `check-referenced-statements` skill.
2. Attempted the required first `search_arxiv_theorems` call with the manuscript's full lower-volume application. Automatic approval review rejected that payload as potentially unpublished manuscript-derived content transmitted to an untrusted external theorem-search endpoint. That rejected payload was not rerouted.
3. Continued safely using public bibliographic identifiers to find the primary paper, and read the archived primary files and public arXiv text.
4. After establishing public provenance, submitted only the public Proposition 3.7 statement to `search_arxiv_theorems`. This call was approved and completed. It returned three unrelated results (arXiv:2209.00248, Theorems 3.1 and 1.7; arXiv:2307.01991, Theorem 3.2), none a valid match.
5. Used built-in web fallback on the public theorem wording; the published primary Springer result matched Proposition 3.7 exactly. Its definitions and global assumptions were checked as above.

The reference check completed via the safe primary-source path; there is no remaining approval blocker and no mathematical failure to record for this subtask.
