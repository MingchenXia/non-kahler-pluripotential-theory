# a4b audit: r4g07–r4g13 (Hessian chapter) and coordinator edits

## Verdicts
| Report | Files | Verdict |
|---|---|---|
| r4g07 | chapter file, cone, Liouville | EDITS CORRECT |
| r4g08 | trace, complex_limits | EDITS CORRECT |
| r4g09 | proper/bounded approximation, continuous products | EDITS CORRECT |
| r4g10 | continuous regularity, bounded currents | EDITS CORRECT |
| r4g11 | Sobolev two factors, bounded locality | EDITS CORRECT |
| r4g12 | smooth capacity | EDITS CORRECT |
| r4g13 | mass comparison | EDITS CORRECT |
| Coordinator (H_m reminder; cone notation in bounded_currents:38, continuous_regularity:147) | | CORRECT |

## Counts
- 55 mathematical corrections checked. Each was re-derived against `git diff e2cac72`, and every caller of a changed statement was checked.
- 11 renamings checked: Q→P; h→ψ; η'→η; H,H̃ and w,w̃; F→g; s→x; S→α; b→M+3; the A_d index; M→B̄.
- 3 coordinator edits checked.
- mathdiff3 was run on all 14 files; no unintended change of a formula.
- `chapcheck.sh a4b chapter_hessian_equations`: no errors and no undefined references. The only message is the known Underfull (badness 1783).

## Key verifications
- **Normalization.** α^j∧ω^{n-j}=σ_jω^n (j!(n-j)!S_j/n!) is used consistently in every section:
  - the cone-shift polynomial;
  - the mixed trace, where ∏σ_{k+1}/((k+1)σ_k)=σ_m/(m!σ_1);
  - quadratic coercivity, Q=fS/m−(m+1)fS_{m+1}/(mS_m), and 𝓕=fσ_{m-1}/σ_m;
  - the F_i bound L^{m-1}/(nf_0^{m-1});
  - the Liouville rescaling, with κ=1/(2π) correct for i∂∂̄/(2π);
  - the torus example: n!(2−mπ²t/(2n))B_n.
- **Cone notation.**
  - Γ_m holds vectors, Γ_m(ω) and its closure hold forms, C_{n,m} holds matrices.
  - The coordinator's replacements use these correctly, and "since m≥2" is exactly the hypothesis needed for the closed-cone inclusion.
  - closed Γ_m(ω) with σ_m>0 does lie in Γ_m(ω), by Maclaurin on the closure.
- **H_m.** H_m is defined for smooth potentials (proper_approximation:7), for continuous ones (continuous-products statement), and first for bounded ones at bounded_locality:95. No bounded use comes earlier; the mass-comparison text is now only a reminder.
- **Repair in proper approximation.** The repair is valid and the hypotheses of prescribed-potential-trace hold:
  - h(x,τ)=τH(x), with v=t and φ=t_i;
  - M=max(1,‖H‖), B=1.
- **Continuous case.** The first inequality comes from the maximum principle via (1+N⁻¹)(ω+dd^c w_N)−N⁻¹ω. The second is Maclaurin σ_{m-1}≥σ_m^{(m-1)/m}.
- **Scope changes.** All callers still have the required hypotheses:
  - regularized-maximum (max of bounded admissible functions): canonical-order, bounded-nonvanishing;
  - absolute-mixed-forms (closed cone): continuous products, mass comparison, bounded locality;
  - weighted-measure-convergence (limits quasicontinuous): bounded locality ×2, joint-decreasing-products, weighted-positive-products;
  - smooth-capacity-convergence (m-subharmonic sequences): rough-coefficient-capacity;
  - proper-bounded-stability (∂_t f≥κ on X×[A,B]): proper-bounded-smoothness;
  - proper-auxiliary-limit (J interval): continuous-hessian-regularity.
- **Case 2 of the trace estimate.** The added terms −(9q²+2q)|a_i|² on I and −(3q²+2q+rq²)|a_i|² off I bring both to −(9q²+2q+rq²), which matches the absorption lemma with the single penalty r≤1/2. The value δ≤τ/(72A+τ) gives the coefficient 4δΨ'²/(1−δ)≤Ψ''/2.

## Problems found
No error was introduced by the review edits, and I made no edits.

The following minor points predate the edits and were left unedited. Proposed fixes:
1. **complex_limits:109.** "In the closed $2$-cone," is the last remaining "closed k-cone" phrase. Replace it with "Since $m\geq2$, $C_{n,m}\subset C_{n,2}$, so".
2. **trace:187.** `W\in\Gamma_m,\qquad I+v_{i\bar j}\in\overline{\Gamma_m}` applies the vector cone to matrices. Replace it with `\lambda\in\Gamma_m,\qquad I+v_{i\bar j}\in C_{n,m}`, using the λ of trace:12 and the unitary frame already stated.
3. **cone:140.** The lemma-local `W:=\sum_iF_iM_{i\bar i}` clashes with the trace section's W=g^{-1}H, while trace:43 calls this quantity W_M. Rename it to `W_M:=`; it is used only in the statement.
4. **Maclaurin on the closure.** cone:21–22 states Maclaurin only "on Γ_k", but it is used on the closure at continuous_regularity:147–149 and complex_limits:115. Optional fix: "on $\Gamma_k$, and by continuity on $\overline{\Gamma_k}$,".
5. **σ_j overload (harmless).** σ_j=ω+dd^c u_j at bounded_currents:33, and σ, σ_u, σ_V, σ_i elsewhere, reuse the letter of the normalized σ_j, though always in a different proof. A rename (for example β_j) is optional.
