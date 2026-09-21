# ALS reference audit — analytic_density_example_01

Scope: only the ALS imports and associated definitions in Section 8. No previous verification reports or Sections 1–6 uniqueness results were used.

## Sources and search procedure

- Archived primary paper read: /Users/mingchen/Non-Kahler/research/sources/ALS26.pdf and its text extraction ALS26.txt. The archive identifies itself as arXiv:2511.02339v1, 4 November 2025 (manuscript date November 5, 2025).
- Primary URL: https://arxiv.org/abs/2511.02339 ; full text https://arxiv.org/html/2511.02339v1 .
- search_arxiv_theorems was called first separately for strict domination, existence/unique constant, and the positive-exponent twisted equation. It returned unrelated theorems, so none was accepted as a match. The existence search first encountered an automatic-review deadline timeout and succeeded on one allowed retry.
- Built-in web search was then called with the same three statement queries. The arXiv primary full text and archive confirm the numbered results.
- This is a statement/application verification, not a re-proof of the primary paper.

## Context and exact specialization

ALS fixes a compact Hermitian manifold, a smooth semipositive big form θ, and a θ-model potential φ. The manuscript specializes θ=ω and φ=0. Its ω is strictly positive, hence satisfies semipositivity and bigness. In ALS Definition 2.13 (p. 11), the model conditions are Pθ[φ]=φ and Pεθ(φ) not identically minus infinity for some 0<ε<1. At φ=0, both envelopes equal zero, so the model conditions hold. ALS itself explicitly includes zero among its model potentials.

ALS Definition 3.2 (p. 12) defines the relative class by u⪯φ and Pθ(bu−(b−1)φ) belonging to PSH(X,θ) for every b≥1. At φ=0 this becomes exactly Pω(bu)∈PSH(X,ω) for every b≥1. Every compact quasi-psh function is bounded above, so the condition u⪯0 is automatic. ALS prints this specialization immediately after the definition. Thus the manuscript's E_env is the identical class, not merely an analogous mass-equality class.

ALS Section 2.1 (p. 5) uses the strong increasing limit of restrictions of the bounded truncations to {u>−t}. Integer truncations in the manuscript are cofinal and give the same measure. ALS explicitly does not assume v_+ finite for this general definition and does not promise finite mass for every member. The manuscript likewise does not impose or use such a blanket finite-mass conclusion.

The numeric dd^c multiplier is not explicitly fixed in the inspected ALS text. No numeric formula is imported that depends on it. For any standard positive normalization change D0=kD, use a0=a/k. Then ω+D0 a0=ω+D a, P0(h/k)=P_D(h)/k, the envelope class corresponds, the restricted truncations are cofinal, and v_± are unchanged. Strict comparison sets are preserved. For the twisted equation, λ0=kλ preserves e^{λ0a0}=e^{λa}. Hence no normalization mismatch affects any imported assertion.

## Theorem 3.14 — p. 16 (proof continues p. 17)

Actual hypotheses: v_−(θ)>0; u∈E(X,θ,φ); v∈PSH(X,θ) with v⪯φ; at least one of ∫θ_u^n and ∫θ_v^n finite; and θ_u^n≤cθ_v^n on {u<v}, where 0≤c<1. Conclusion u≥v.

At φ=0, the extra v⪯φ condition is automatic by compact upper boundedness. Thus the manuscript's version, including the one-finite-mass condition and the strict factor, is exact and applicable. There is no requirement v_+(ω)<∞ here. The manuscript correctly declines to replace c<1 by c=1.

Status: PASS; no critical error or gap.

## Theorem 5.8 — pp. 28–29

Section 5.2, immediately before the theorem, explicitly imposes v_−(θ)>0. For λ>0 and a positive non-pluripolar Radon measure μ, the theorem produces exactly one solution in E(X,θ,φ) of θ_u^n=e^{λu}μ. The manuscript appropriately requires μ nonzero. The theorem assumes no v_+ bound. At φ=0 this is potential uniqueness in precisely E_env, not uniqueness among every PSH function without a class condition.

For any such solution, compact upper boundedness gives ∫θ_u^n≤e^{λ sup u}μ(X)<∞. Therefore the finite-mass qualification needed by domination is automatic for all competing solutions. More explicitly, on {a<b−δ}, their measures satisfy NMA(a)≤e^{−λδ}NMA(b−δ), so Theorem 3.14 gives a≥b−δ. Reverse the pair and let δ decrease to zero. This verifies the manuscript's positive-exponent uniqueness sentence and shows why it does not yield the untwisted equality case.

Status: PASS; no critical error or gap.

## Corollary 5.9 — pp. 29–30

Under the same Section 5.2 hypotheses, the corollary gives a unique positive constant c and a function u∈E(X,θ,φ) with θ_u^n=cμ. The uniqueness asserted is that of c, not of u. Its proof explicitly obtains uniqueness of c from Corollary 3.15 (p. 17). The manuscript parses this distinction correctly.

For any competing solution of this equation, mass is cμ(X), hence finite. If two constants c1<c2 were possible, the ratio κ=c1/c2<1 would let Theorem 3.14 compare the first solution with every constant translate of the second and force an impossible inequality. Therefore uniqueness applies to all E_env solutions, including the displayed smooth solutions. Their exhibited c=1 consequently fixes the unique possible constant.

Status: PASS; no critical error or gap.

## Other local transitions in the audited reference passage

For bounded ω-psh a, the envelope of ta is sandwiched between a constant lower barrier and a finite constant upper bound. The locally upper bounded supremum, followed by upper semicontinuous regularization, is ω-psh. Hence bounded a∈E_env. No total-mass identity is invoked.

A smooth density times a smooth volume defines a finite Radon measure on compact X and annihilates pluripolar sets, which have zero smooth volume. Smooth bounded potentials have non-pluripolar measure equal to their usual top power because deep truncations leave them unchanged. These statements supply the inputs needed for the final ALS application, conditional only on the separately audited construction and v_->0.

Overall ALS verdict: every ALS statement in Section 8 matches and specializes correctly. No critical errors or gaps found. The broader construction and BGL lower-volume theorem are outside this delegated audit.

