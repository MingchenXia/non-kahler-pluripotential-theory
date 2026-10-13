# a5j audit of r5g13

## Verdict
**r5g13: CORRECT AFTER FIXES.** I made two small local fixes, both in section_diffuse_product_polar_obstruction. I found no other problem introduced by the pass.

## What I checked
- **11 hypothesis removals or weakenings.** Each proof checked in the enlarged scope, with every cited result and every caller.
- **14 duplicate removals or citation replacements.** Each surviving statement checked against every `\cref` of the moved labels, and for circularity.
- **5 simplified proofs.**
- **Whole-file math diff of the diffuse file.** I compared old and new statement by statement. Every result, case and constant of the five old statements is still present:
  - the Kähler proposition;
  - the Kähler exact-volume corollary;
  - the Hermitian mass polynomial;
  - the invariant-mass corollary;
  - the representative-mass proposition.

  This includes:
  - existence of δ with p,0 ∈ M_δ;
  - d(p,0)>0 and δ^pol=0;
  - trivial ideals, and p not an ideal model;
  - V(p_t)=A−Mt^n, d=M|s^n−t^n|, and the interval [0,Mt_0^n];
  - the c_j, the surface formula, and the v_± bounds;
  - the Gauduchon-surface case.

## Priority items
**1. lem:diffuse-cutoff-polar-blindness: correct.**
- Every p ≥ sH−c has zero Lelong numbers: off S, p is bounded below; at a point a of S, p ≥ s g(z_1) − c with ν(g,a_1)=0.
- Skoda's theorem then gives I(λp)=O_X for every λ>0.
- Pol_π(p)=0 on every smooth modification:
  - cor:closed-current-hausdorff-null applies with j=1<n, since n≥2 is the standing assumption.
  - The support theorem leaves only divisorial components.
  - By the proof of lem:nonclosed-divisorial-removal, b_i ≤ ν(p∘π,E_i).
  - Exceptional divisors with image in S map to points, and ν(g(a_1+ζ'^m),E_i)=0 kills those coefficients.
- The anisotropic reduction holds: g≤0 gives h_a ≥ (max_j a_j)h, so p_a ≥ t(max_j a_j)H.

**2. Merged proposition (prop:diffuse-representative-mass = prop:diffuse-hermitian-mass-polynomial): correct.** I checked:
- the weak convergence to Φ_v through thm:small-pole-local-products, using the decreasing sequence v_k+ψ_1;
- eq:diffuse-residual-local, through cor:closed-current-hausdorff-null and lem:small-pole-residual-invariance (whose two functions need not share a correction);
- the mass formula, and the bounds by v_±;
- the invariant-mass case (n−j ∈ [1,n−1]) and the surface case;
- Φ_{tH}(S) = t^n σ^{⊗n}(S) = Mt^n, with M=1;
- c_j(tH)=c_j t^j, using max(tH,−k)=tH_{k/t}. The new H_L=max(H,−L) differs from the old χh_L, but no caller outside the file uses H_L or c_j.

Callers of both labels (in the file, research program, history) still get what they use.

**3. Moved labels: correct.**
- prop:all-modifications-diffuse-polar-blindness, now on prop:diffuse-two-mass-model-obstruction: v_±=∫ω^n for Kähler ω by Stokes' theorem, and all old conclusions are stated.
- cor:diffuse-product-exact-volume, now on cor:diffuse-mass-invariant-models: the proof through cor:diffuse-hermitian-model-interval and thm:ordinary-envelope-volumes is complete.
- The index entries moved with both labels.

**4. prop:small-curvature-intrinsic-traces without simple normal crossings: correct.**
- First inclusion: the weight |g|²∏|s_j|^{2(⌈ta_j⌉−ta_j)}e^{O(1)} is bounded.
- Second inclusion: it only needs membership in the *principal* ideal (∏ s_j^{⌊ta_j⌋}), and that is decided in codimension one.
  - At a general point of D_j, lem:smooth-center-multiplier-ideal with k=1 gives order at least ⌊ta_j⌋ along D_j.
  - The general points of D_j are dense in every local branch of D_j, and distinct D_j share no branch.
  - Unique factorization in O_{X,x} then gives divisibility.
- The argument never claims the multiplier ideal is divisorial, so the concern about integrally closed but non-divisorial ideals does not arise.
- Restriction, pullback, division by t and thm:intrinsic-trace-profile give the trace formula, and ν(σ_Δ+q,Y)=0.
- The caller prop:ruled-intrinsic-ideal-orders is consistent: D_X is smooth and Y ⊄ D_X.

**5. Hopf section, n≥3 → n≥2: correct.** For n=2 (d=1):
- lem:hopf-basic-potentials is stated for n≥2.
- Darvas's completion and CAT(0) theorems hold on P^1.
- I recomputed the Hessian: it is 2n∫⟨(w_t+dcw_r)² − d(d+1)c²w_r²/2⟩. The mode value is nπ²/2·(1−c²k²) for d=1, negative for large k.
- ω_2 is Gauduchon, since α_2²=0.
- The diagonal-geodesic moments (2/(n(n+1)) and 1/(n(n+1))) hold for n=2.
- The energy threshold d/(d+2)=1/3 holds for d=1.

**6. Gauduchon section and its neighbours: correct.**
- prop:closed-pole-compatible-limits uses only p_j ≤ 0 and sup p_j = 0.
- Without the identity in ℛ, the curve formula still holds: every π∈ℛ is an isomorphism on a curve, and ℛ is nonempty. Nothing else uses the identity in ℛ or Pol_1 inside δ^pol.
- The recalled regularization in subsec:psh-closed-regularization contains both the absorption of ε_j and the Dini step, so lem:zero-lelong-strict-smoothing can cite it.
- cor:countable-modification-polar-blindness: since x∉S_j, π_j is biholomorphic near the single pole y_j, and the polar current pulls back to Pol_1(p_a)=0.

## Fixes made (section_diffuse_product_polar_obstruction.tex)
**Fix 1: bounded mass in prop:equal-residual-anisotropic-models (proof, paragraph "Near S, …").**
- **Problem.** The pass deleted the step v_−=v_+=A. That step is what gives the bounded mass property, which the cited results of chapter_mass_bound_volumes require as a standing hypothesis: thm:ordinary-envelope-volumes, thm:small-pole-envelope-residual, prop:model-volume-separation and d_ω.
- **Old:** "Near $S$, the function $u_a=th_a$ is plurisubharmonic. Hence …"
- **New:** "By \cref{thm:mass-invariance-characterization}, all bounded $\omega$-plurisubharmonic functions have mass $A$, so $v_-(\omega)=v_+(\omega)=A$; in particular, $X$ has the bounded mass property. Near $S$, the function $u_a=th_a$ is plurisubharmonic. Hence …"

**Fix 2: the constant C was never fixed.**
- **Problem.** The later statements use "0<t<1/C", but the lemma only says "There is C>0"; the old statements said "Fix H, C, M of …".
- **Old:** "In a nonclosed background, the mass of a potential also involves …"
- **New:** "From now on, $C$ is a fixed constant as in \cref{lem:diffuse-cutoff-polar-blindness}. In a nonclosed background, the mass of a potential also involves …"

## Proposals outside my files (no edit made)
chapter_history.tex l.631: "The normal crossing ideal formula in \cref{prop:small-curvature-intrinsic-traces}" → "The ideal bounds in \cref{prop:small-curvature-intrinsic-traces}". The proposition no longer assumes normal crossings. This agrees with r5g13's proposal.

## Minor (no action needed)
section_gauduchon_polar_comparison says "n≥1 is arbitrary" but takes Pol_π from subsec:polar-first-current-obstruction, whose standing assumption is n≥2. The definition does not depend on the dimension, so this is harmless.

## Compile check
`chapcheck.sh a5j chapter_igood chapter_rays chapter_testcurves chapter_trace_data`, run twice:
- no errors, no overfull boxes, no undefined references;
- only the allowed Underfull (badness 1783) in section_nonclosed_ruled_trace_masses, which is not one of my files.

On the first run, eq:diffuse-residual-local (new label) and lem:auxiliary-slice-envelopes (another part's file) were undefined; both resolved on the second run.
