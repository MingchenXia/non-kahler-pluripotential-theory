STATUS UPDATE: Both audits passed, all full records read, and the section is included. The historical draft notes below document the construction and pre-inclusion checks. A standalone note shares the same proof source. Current status is in STATUS.md.

# NUMA: density positive off two real hypersurfaces

Draft section_numa_thin_zero_set.tex is EXCLUDED pending two independent audits: numa_thin_zero_set_01 (exec1987), numa_thin_zero_set_independent_01 (exec6435). No novelty assertion. This could answer the source manuscript's empty-interior uniqueness question, so treat every sign and endpoint extension carefully.

Fix s in (0,1), source p=C exp(-1/(1-r^2)) and h_s=sp. Density g=(omega0+sH)^3/FS^3 is positive except at M+- (r=+-1). Its data k_s=(x+sp)(y-sp)(z+sq). New h solves h'=k_s/((x+h)(y-h))-z, initial h0=sp0-eta.

At left endpoint coefficients are x=1+p,y=p,z=q>0. Trial c p has k_c=(1-c^2)(1+(1+c)p)pq. Choose 0<cL<s: k_cL>k_s near p=0. Thus cL p is strict SUPERSOLUTION forward and LOWER barrier backward. At right x=p,y=1+p,z=-q>0; k_c=(1-c^2)(1+(1-c)p)p(-q). Choose s<t<1: k_-t<k_s, so -tp is lower barrier forward. On a fixed compact middle interval, continuous dependence makes small positive eta admissible and between the endpoint traps. Exact solution sp is the upper bound everywhere by ODE uniqueness. Compact continuation gives h on(-1,1).

Flatness is the key: b=h/p stays in a compact subinterval(-1,1) at each end. b'=(p'/p)(R(p,b)-b), R smooth with bounded derivatives and p'/p=-2r/(1-r^2)^2. Induct polynomial endpoint growth of every b derivative. Every p derivative is p times a rational function, so every h derivative is p times a polynomially bounded function ->0. Extension h=0 outside is C-infinity and flat. Primitive constant on projective ends ->global smooth potential G-rho. ODE supplies positive radial coefficient and exact common cube; all forms rank1 only at M+-. Different eta changes slope0, so normalization does not identify solutions.

A pure-Python RK4 check in tmp/numa-shooting-experiment.py (not a proof) for s=.5, eta/p0 between1e-5 and.01 consistently approached h/p=.5 on left and -.5 on right. The proof does NOT require those asymptotic limits, only traps. No numeric claim belongs in the theorem.

Checked the archived KN19 primary Theorem A (KN19.txt lines75-110): known uniqueness/stability assumes f>=c0>0, not merely positivity almost everywhere. The proposed density violates that lower bound. An internet search of primary Lu2025 mean-field discussion also retains strict-positive hypothesis; no conflicting theorem has been found. Do not confuse e^(lambda u) restoring uniqueness with smoothing the zero-density band: the separate89 draft addresses nonC2 at positive exponent for the ORIGINAL f, not this new g.

If BOTH audits pass: read both full reports and JSON, include after section_numa_radial_family in chapter10; update originalNUMA ending to historical question plus forward reference; revise geometry Problem28.5.4 (empty-interior part would be answered negatively; keep general selection, ask finite-order vanishing instead). Preface distinguish source construction from new deduction, no novelty certification. Strengthen source-vs-draft ledger clearly. Consider adding finite-order-degeneracy question because this example uses infinite-order vanishing. Do not make those updates before audits.
