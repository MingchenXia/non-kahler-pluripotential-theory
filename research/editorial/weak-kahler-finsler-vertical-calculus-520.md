# Complex Finsler torsion and vertical calculus — checkpoint 520

Date: 6 October 2026. Private baseline 3229d2fbd639684534fe84372d28a07643912364 is independently verified on remote main. The manuscript remains at 519, with 1347 printed / 1373 physical pages and the 17-page companion. Three proofs in the inactive 67-line fragment have complete first and automatic second reads. All 38 original directions remain open; no original problem is closed.

## Primary scope

Xiaoshu Ge, On the Definition and Smooth Examples of Weakly Kähler–Finsler Metrics, arXiv2610.03535v1, submitted 2 October 2026 at 16:19:58UTC, has 18 PDF pages and 1005 main-source lines. Official metadata/PDF/source hashes are recorded in the audit. Safe extraction preserved source bytes. The main source requires a cp1252 fallback after actual UTF8 decoding failed at byte 0xb5. Actual source 136–538 is completely read first; 139–187 and 287–538 are read again. PDF text 1–3 and 5–10 is actually read first; all three physical images 7–9 are actually viewed individually. The scoped inputs are Definitions 1.1 / 1.3, the explicit connection coefficients and Euler identities, Proposition 3.1 p 8 and Theorem 3.2 pp 8–9. Neither the remaining 1005-line source nor the whole 18-page proof is certified. The later stronger-condition criteria and Kobayashi examples, including their external existence/rigidity dependencies, remain unreviewed.

The Denisi–Höring 2610.03048v1 official metadata/PDF/source was also downloaded and safely extracted. Its abstract is read, but no new complete primary proof is read. The book already integrates its elliptic ruled-surface/canonical-extension results; this is not a new adoption or a duplicate addition.

## Mathematical reconstruction

For G>0 smooth and complex degree-two homogeneous off the tangent zero section, with positive fibre Levi matrix H, the adapted fields Dj=partial_vj-Gja H^{bar b a}partial_barvb satisfy Djv^k=delta_j^k and DjGk=0. The forms dv and d_vGi form an invertible triangular coframe on the complexified vertical cotangent at a fixed base point. Their annihilation by the vertical brackets proves commutation. This is not a holomorphic Legendre coordinate construction and does not require real strong convexity.

A smooth skew tensor A with cyclic adapted derivatives and EA=0 vanishes if v-contracted A vanishes. Differentiating both contractions and summing gives the precise identity EA+2A=0. For the metric-paired torsion Tjk=Gi(Gamma^i_j;k-Gamma^i_k;j), Tjk=DjG_;k-DkG_;j. Commutation gives cyclic closure, and complex homogeneity gives ET=0. This reconstructs Ge's weak equivalence, retaining the Gi pairing rather than asserting that the full torsion vanishes.

The stronger equivalence uses a separate argument. Direct inverse-matrix differentiation proves Gamma^i_j;k=partial_vj N^i_k. Since N has complex weight(1,0), the contracted Kähler condition gives 2N^i_k=partial_vk(vjN^i_j). A second fibre derivative is symmetric, so the full horizontal torsion vanishes. The original Chen–Shen paper has not been read; this is a direct coordinate reconstruction, with no false claim to certify its proof. For a Hermitian quadratic G, the weak paired torsion has coefficients independent of v; vanishing for every v recovers d omega=0. All dimensions n>=1 are covered.

## Primary issues and correction

Definition 1.3 omits =0 from its weak-condition display, while the later equation 2.10 and Theorem 3.2 specify zero. The connection-form display uses barpartial despite its stated(1,0) type; explicit coefficient formulas suffice. Equations 2.11–2.12 swap the Kähler/strongly Kähler labels relative to Definition 1.3. Proposition 3.1's coframe must be interpreted vertically. The final display after 3.9 drops a skew sign, while the conclusion follows from ET+2T=0.

Remark 3.3 repeats a term in its tensor definition and asserts delta_k H_jbar a=DjG_bar a;k. The early inactive draft also used this identity. Direct differentiation shows it is false; the draft's entire stronger-condition paragraph was replaced before adoption or release. An exact countermodel is G=R+(1+|z1|^2)|v1|^4/(10R), where R=sum|vj|^2 on a three-dimensional coordinate base with |z1|<3. For x=|v1|^2,

L(x^2/R)(w)=2x/R |w1|^2-x^2/R^2 |w|^2+(2/R)|barv1 w1-(x/R)sum barvj wj|^2>=-|w|^2.

Thus the model's fibre Levi form is bounded below by(1-(1+|z1|^2)/10)|w|^2>0. At z1=1 and v=(1,2,1), the first entry of the disputed identity's exact residual is -3575/3887892. The audit includes the whole rational residual matrix and positive leading minors. This critical check does not invalidate the independently reconstructed weak equivalence, and the incorrect auxiliary identity is not adopted.

## Checks and preservation

Twenty-eight direct analytic obligations and four supplementary exact rational model groups pass. These are mathematical review and supporting algebra, not machine proofs. Strict house audit is 0 errors / 0 warnings using the actual book/references.bib. The initial audit mistakenly named a nonexistent default bibliography path; the corrected invocation passes. The initial model mistakenly assigned a nonzero diagonal to its skew T matrix; restricting construction to off-diagonal entries repairs it without changing the verified mathematics. The initial baseline seal used relative control paths outside the repository cwd; corrected before creating the seal, with no repository modification.

All 368 book assets / 1163 retained proof bodies, both catalogue files, both original manifests, 451 protected sources and ten incoming author files remain byte-exact. No book adoption, bibliography addition, new author build or publication occurs. The saved catalogue source remains SHA 37e5e5c5655d25f204959e2ff70fc1caa1794d9861be00433140fc7db2c165bc. Native 219 actually ends with connection closed before the server answered, without compiler diagnostics or success. The same editor remains open; no duplicate native call is made.

Current-package checks reuse the actual 519 empty-source outputs and pass all 2504 safe unique relative nonsymlink paths / 2503 current payload checksums, 365 book-source byte comparisons and every 1373 book / 17 companion page text. Reconstructed logs remain clean and publication is excluded. No new extraction or build is claimed. Private 520 synchronization is pending. Next: read the stronger criteria and example dependencies; choose a coherent natural home before book adoption. No total-space psh, curvature sign, complement-index or general weak-versus-strong equivalence is inferred from the checked contractions.
