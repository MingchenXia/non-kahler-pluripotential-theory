# Closed loci and LCK integration — 15 September 2026

The two new chapters are included in the checkpoint16 build after the targeted repair passed. The supplied Vu–Xia full proof has passed its source audit; adaptation into the book remains to be written. It is not a premise of either new chapter.

## Mathematical source reading

- Boucksom thesis: §§1.2.3–1.2.6, §§2.1.2–2.1.3, Definition2.1.19 and Theorem2.1.20. Classical Bott–Chern classes have CLOSED representatives; the auxiliary Hermitian lower bound is not a cohomology perturbation. The printed regularization theorem1.2.10(ii) omits the gamma term. The original 2004 published Theorem2.1 was read directly and archived: it retains gamma-epsilon omega. The chapter now states that precise bound and cites both sources.
- Vu–Xia source: all 2,046 lines read. Full verification `transcendental_nakamaye_01` completed with verdict correct, and its final JSON was read. The provisional disconnected-ambient principalization objection was withdrawn by the verifier as convention-dependent, not a confirmed error; the final proof uses connected ambient manifolds. Any adapted auxiliary statement will explicitly use the connected setting. Original source remains byte-identical.
- Ornea–Verbitsky book v6: §§3.4,7.4,12.3.3,18.3–18.5,23.1,Chapter32,Question47.56. Main concepts are rewritten with our dc normalization and lambda for the Lee form.
- Original Vaisman Calabi–Yau paper v2: Theorem4.1, Lemmas4.2–4.4 and full proof read. Lee AND anti-Lee invariance is required, even though the book's Theorems32.2/32.6 omit it in their displayed formulations. The paper's footnote5 explicitly identifies this use. No arbitrary-volume existence claimed.
- Ornea–Verbitsky balanced/LCK paper v2: §§4.1–4.2 and conjecture/degree computation read. Positivity against the LCK Gauduchon metric alone is not the full Lee-curvature pseudoeffectivity conjecture.
- Lee–Gauduchon paper v2: Definitions3.3/3.5, Theorems3.11/4.5 and their proofs read. In our integration the pairing is written with the one-form first; zero classes are handled by nonnegative duality, not strict positivity against every member of a cone containing zero.
- Barbaro–Otiman v2: introduction, preliminaries and full TheoremA proof (§4) read. Metric-level rigidity differs from the manifold-level Calabi–Yau/Vaisman conjecture. A self-contained proof of the Chern–Ricci-flat specialization, using standard Riemannian identities, is drafted separately.
- Collins–Tosatti: 2015v5 Theorem1.1 and introduction; published2022 definitions, Lemma2.1 context and Remark2.2 read. Strong analytic singularities include smooth remainder. Arbitrary-ambient replacement of the Kähler error is not justified.

## Included claims

`chapter_bott_chern_loci.tex`: minimal multiplicities and loci with Hermitian lower bounds; Gauduchon linear compactness; classical attainment and no isolated non-Kähler points; exact classical/restricted definitions; zero-class infinite Hermitian-error supremum as an immediate consequence of the existing Hopf mass theorem.

`chapter_lck.tex` + `section_lck_volume_literature.tex`: Lee/Gauduchon harmonicity and degree; balanced obstruction; ordinary versus twisted Hessians and class identifications; Hopf metric Vaisman; coupled twisted-volume/conformal-Gauduchon system; precise known Vaisman theorem and current geometric questions; Lee–Gauduchon pairing.

Complete two-chapter verification `closed_loci_lck_connections_01` returned wrong: a definition permitted zero Lee form in the Vaisman volume-uniqueness theorem, and one STW reference pointed to the wrong chapter. Both are repaired. The definition and volume theorem now explicitly require strict/nonzero Lee form, and the citation points to thm:stw-volume. The remaining original claims passed. The original adverse report is retained.

`section_lck_chern_ricci_proof.tex`: reconstructed real Ricci formula and Bianchi/Bochner proof of the rigidity specialization. Separate verification `lck_chern_ricci_rigidity_01` completed with verdict correct. The full 155-line report and final JSON were read. Its proof now replaces the external paragraph in the draft; no target theorem is used as a premise.

All audits use ordinary Rethlas approval mode. Root has not edited verifier results or memory. There is no new external-message or publication authorization involved.

## Repair and integration

Targeted `closed_loci_lck_connections_repair_01` completed with verdict correct. Its full report and final JSON were read. Besides the two repairs, it checks the ordinary closed-bigness obstruction for strict LCK manifolds, the precise regularization statement, and the strict-definition interface of the reconstructed Ricci proof. No other previously completed audit was restarted. Both prior audit directories were preserved unchanged. All four new audit subprocesses have exited successfully.

The initial private preview was reviewed on 41 selected pages. The final 499-page preview was reviewed on 45 selected pages on 12 boards, covering the preface, changed contents, both new chapters, the complete reflowed research-program chapter and all three bibliography pages. Definitions and proofs are grouped, and Vaisman volume, Chern–Ricci rigidity and the Lee–Gauduchon cone have conventional section headings. Two final paragraph-grouping adjustments changed only physical pages456–457 and467–468 (printed440–441 and451–452); all four production pages were rendered and visually reviewed. Every other production page has identical extracted text to the final preview. These changes do not alter mathematical claims. Both final production logs are clean.
