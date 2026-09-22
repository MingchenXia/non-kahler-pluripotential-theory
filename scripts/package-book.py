#!/usr/bin/env python3
"""Package only manuscript sources used by the two completed LaTeX builds."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import zipfile

root = Path(__file__).resolve().parent.parent
book = root / "book"
selected = set()
for stem in ("book", "numa-thin-zero-set-note"):
    for line in (book / f"{stem}.fls").read_text().splitlines():
        if not line.startswith("INPUT "):
            continue
        item = Path(line[6:])
        item = item if item.is_absolute() else book / item
        item = item.resolve()
        if not item.is_relative_to(book) or not item.is_file():
            continue
        if item.suffix in {".tex", ".cls", ".sty", ".png", ".jpg", ".eps"}:
            selected.add(item)
selected.update(p for p in (book / "style").iterdir() if p.is_file())
for name in (
    "book/references.bib", "book/latexmkrc", "scripts/build-book.sh",
    "scripts/build-numa-note.sh", "PLAN.md", "BLUEPRINT.md", "CHANGELOG.md", "research/comparison.md",
    "research/audits/cover-revision-2026-09-21.json",
    "research/proof-obligations.md", "research/literature.md", "research/READING-GUIDE.md",
    "research/source-outline.md", "research/source-manifest.json",
    "research/sources/manifest.json",
    "research/editorial/uniqueness-integration-map.json",
    "research/editorial/typography-changes.json",
    "research/editorial/REVISION-PLAN.md",
    "research/editorial/loci-lck-source-review.md",
    "research/editorial/loci-lck-integration-map.json",
    "research/editorial/null-locus-integration-plan.md",
    "research/editorial/nakamaye-adaptation-map.json",
    "research/editorial/nakamaye-integration-review.md",
    "research/editorial/relative-general-measure-review.md",
    "research/editorial/relative-general-measure-map.json",
    "research/editorial/section_relative_extended_domination.tex",
    "research/editorial/section_relative_moving_measures.tex",
    "research/editorial/section_general_measure_relative.tex",
    "research/editorial/big-relative-reconstruction-review.md",
    "research/editorial/big-relative-reconstruction-map.json",
    "research/editorial/section_big_relative_foundations.tex",
    "research/editorial/section_big_relative_energy.tex",
    "research/editorial/big-minimal-equations-review.md",
    "research/editorial/big-minimal-equations-map.json",
    "research/editorial/section_big_minimal_comparison.tex",
    "research/editorial/section_big_minimal_existence.tex",
    "research/editorial/big-minimal-measures-review.md",
    "research/editorial/big-minimal-measures-map.json",
    "research/editorial/section_big_minimal_moments.tex",
    "research/editorial/section_big_minimal_measures.tex",
    "research/editorial/big-weighted-addition-review.md",
    "research/editorial/big-weighted-addition-map.json",
    "research/editorial/section_big_weighted_limits.tex",
    "research/editorial/section_big_weighted_addition.tex",
    "research/editorial/big-model-equations-review.md",
    "research/editorial/big-model-equations-map.json",
    "research/editorial/section_big_relative_projection.tex",
    "research/editorial/section_big_model_measures.tex",
    "research/editorial/section_big_unrestricted_addition.tex",
    "research/editorial/section_big_model_lp.tex",
    "research/editorial/integrable-infinite-mass-review.md",
    "research/editorial/integrable-infinite-mass-map.json",
    "research/editorial/section_integrable_infinite_mass.tex",
    "research/editorial/lee-gauduchon-review.md",
    "research/editorial/lee-gauduchon-map.json",
    "research/editorial/section_lee_gauduchon_cone.tex",
    "research/editorial/section_lee_gauduchon_strong.tex",
    "research/editorial/analytic-envelope-limits-review.md",
    "research/editorial/analytic-envelope-limits-map.json",
    "research/editorial/section_analytic_envelope_limits.tex",
    "research/editorial/birational-partial-kernels-review.md",
    "research/editorial/birational-partial-kernels-map.json",
    "research/editorial/section_birational_partial_kernels.tex",
    "research/editorial/fiber-point-kernels-review.md",
    "research/editorial/fiber-point-kernels-map.json",
    "research/editorial/section_fiber_point_kernels.tex",
    "research/editorial/section_hopf_point_equilibrium.tex",
    "research/editorial/build-hopf-point-plot.py",
    "research/editorial/hopf-point-plot-checks.json",
    "research/editorial/current-theory-lower-mass-review.md",
    "research/editorial/current-theory-lower-mass-map.json",
    "research/editorial/trace-exceptional-author-correction.md",
    "research/editorial/lower-mass-author-correction.md",
    "research/editorial/section_continuous_bc_representatives.tex",
    "research/editorial/section_trace_exceptional_divisors.tex",
    "research/editorial/section_trace_exceptional_divisors_v2.tex",
    "research/editorial/section_affine_trace_difference.tex",
    "research/editorial/section_bott_chern_cone_compactness.tex",
    "research/editorial/section_vanishing_lower_mass.tex",
    "research/editorial/section_vanishing_lower_mass_v2.tex",
    "research/editorial/section_lower_mass_solvability.tex",
    "research/editorial/section_lower_mass_metric_geometry.tex",
    "research/editorial/chapters-16-26-review.md",
    "research/editorial/chapters-16-26-map.json",
    "research/editorial/chapters-27-29-map.json",
    "research/editorial/chapters-30-appendix-map.json",
    "research/editorial/individual-density-map.json",
    "research/editorial/individual-stability-map.json",
    "research/editorial/root-tail-map.json",
    "research/editorial/tail-divisor-map.json",
    "research/editorial/positive-lower-threshold-map.json",
    "research/editorial/exponential-tail-modulus-map.json",
    "research/editorial/exponential-tail-modulus-review.md",
    "research/editorial/section_exponential_tail_modulus.tex",
    "research/editorial/section_smooth_dual_regularity.tex",
    "research/editorial/smooth-dual-regularity-followup.md",
    "research/editorial/smooth-dual-regularity-map.json",
    "research/editorial/smooth-dual-regularity-review.md",
    "research/editorial/section_smooth_dual_regularity_v2.tex",
    "research/editorial/section_smooth_dual_sharpness.tex",
    "research/editorial/section_semipositive_capacity_limit.tex",
    "research/editorial/capacity-and-trace-map.json",
    "research/editorial/capacity-and-trace-review.md",
    "research/editorial/section_semipositive_lp_limit.tex",
    "research/editorial/section_semipositive_projective_example.tex",
    "research/editorial/projective-dual-map.json",
    "research/editorial/projective-dual-review.md",
    "research/editorial/section_divisorial_residual_rigidity.tex",
    "research/editorial/divisorial-rigidity-map.json",
    "research/editorial/divisorial-rigidity-review.md",
    "research/editorial/geometry-review-map.json",
    "research/editorial/geometry-review-review.md",
    "research/editorial/section_divisorial_residual_families.tex",
    "research/editorial/divisorial-families-map.json",
    "research/editorial/divisorial-families-review.md",
    "research/editorial/section_general_damping_weights.tex",
    "research/editorial/general-damping-map.json",
    "research/editorial/general-damping-review.md",
    "research/editorial/equations-review-map.json",
    "research/editorial/equations-review.md",
    "research/editorial/prescribed-review-map.json",
    "research/editorial/prescribed-review.md",
    "research/editorial/relative-review-map.json",
    "research/editorial/relative-review.md",
    "research/editorial/singularity-review-map.json",
    "research/editorial/singularity-review.md",
    "research/editorial/trace-sections-review-map.json",
    "research/editorial/trace-sections-review.md",
    "research/editorial/volume-kernel-review-map.json",
    "research/editorial/volume-kernel-review.md",
    "research/editorial/section_semipositive_trace_rate.tex",
    "research/editorial/current-rate-and-approximation-map.json",
    "research/editorial/current-rate-and-approximation-review.md",
    "research/editorial/section_semipositive_divisors.tex",
    "research/editorial/section_semipositive_exponential_limit.tex",
    "research/editorial/semipositive-dual-consequences-map.json",
    "research/editorial/semipositive-dual-consequences-review.md",
    "research/editorial/section_semipositive_dual_attainment_v2.tex",
    "research/editorial/semipositive-uniqueness-followup.md",
    "research/editorial/threshold-solution-polytope-draft.tex",
    "research/editorial/semipositive-dual-uniqueness-map.json",
    "research/editorial/semipositive-dual-uniqueness-review.md",
    "research/editorial/section_semipositive_dual_attainment.tex",
    "research/editorial/semipositive-dual-attainment-map.json",
    "research/editorial/semipositive-dual-attainment-review.md",
    "research/editorial/equation-exposition-map.json",
    "research/editorial/equation-exposition-review.md",
    "research/editorial/smooth-dual-sharpness-map.json",
    "research/editorial/smooth-dual-sharpness-review.md",
    "research/editorial/section_smooth_dual_sharpness_v2.tex",
    "research/editorial/positive-lower-threshold-review.md",
    "research/editorial/tail-divisor-review.md",
    "research/editorial/section_root_tail_continuity.tex",
    "research/editorial/section_threshold_divisorial_constraints.tex",
    "research/editorial/section_threshold_divisorial_geometry.tex",
    "research/editorial/section_threshold_divisorial_geometry_v2.tex",
    "research/editorial/section_positive_lower_mass_threshold.tex",
    "research/editorial/section_nef_divisor_threshold.tex",
    "research/editorial/positive-lower-mass-threshold-followup.md",
    "research/editorial/nef-divisor-followup.md",
    "research/editorial/root-tail-review.md",
    "research/editorial/section_root_uniform_tails.tex",
    "research/editorial/section_integrable_gauduchon_currents.tex",
    "research/editorial/section_threshold_trace_saturation.tex",
    "research/editorial/threshold-rate-working-note.md",
    "research/editorial/threshold-divisorial-tests.md",
    "research/editorial/individual-stability-review.md",
    "research/editorial/section_individual_density_stability.tex",
    "research/editorial/section_individual_density_stability_v2.tex",
    "research/editorial/section_individual_exponential_equations.tex",
    "research/editorial/section_integrable_gauduchon_tests.tex",
    "research/editorial/individual-density-next-questions.md",
    "research/editorial/individual-density-review.md",
    "research/editorial/section_individual_density_subsolutions.tex",
    "research/editorial/individual-measure-tests.md",
    "research/editorial/individual-density-followup.md",
    "research/editorial/chapters-30-appendix-review.md",
    "research/audits/build-snapshot-38.json",
    "research/editorial/chapters-27-29-review.md",
    "research/audits/build-snapshot-37.json",
    "research/editorial/chapters-14-15-review.md",
    "research/editorial/chapters-14-15-map.json",
    "research/editorial/chapter-13-review.md",
    "research/editorial/chapter-13-map.json",
    "research/editorial/chapters-10-12-review.md",
    "research/editorial/chapters-10-12-map.json",
    "research/editorial/chapters-6-9-review.md",
    "research/editorial/chapters-6-9-map.json",
    "research/editorial/elliptic-foundations-review.md",
    "research/editorial/elliptic-foundations-map.json",
    "research/editorial/chapter-review-20260921.md",
    "research/editorial/section_elliptic_closed_current_descent.tex",
    "research/editorial/section_elliptic_boundary_volume.tex",
    "research/editorial/section_elliptic_gauduchon_limits.tex",
    "research/editorial/curve-fibration-traces-review.md",
    "research/editorial/curve-fibration-traces-map.json",
    "research/editorial/section_curve_fibration_traces.tex",
    "research/editorial/section_trace_product_measures.tex",
    "research/editorial/section_divisorial_trace_representatives.tex",
):
    selected.add(root / name)
selected.update((root / "research/audits").glob("build-snapshot-*.json"))
completed_runs = set()
for directory in (root / "research/rethlas/verification/results").iterdir():
    if not (directory / "verification.json").is_file():
        continue
    selected.add(directory / "verification.json")
    selected.update(directory.glob("*.md"))
    completed_runs.add(directory.name)
for submission in (root / "research/rethlas/verification/inputs").glob("*.md"):
    match = re.search(r"Run_id:\s*`?([a-zA-Z0-9_]+)", submission.read_text())
    if match and match.group(1) in completed_runs:
        selected.add(submission)

readme = """# Singularities in Hermitian pluripotential theory

Editable source of an AI-assisted mathematical working draft prepared for Mingchen Xia.
The manuscript retains the supplied SGPT template and notation. It develops the main
Hermitian framework without a bounded mass assumption, with explicit hypotheses for
special regimes. This is not an author-approved revision or a novelty certification.

Build with a TeX distribution providing latexmk, pdfLaTeX, BibTeX, the newtx fonts,
and the packages used in book/preamble.tex:

    bash scripts/build-book.sh
    bash scripts/build-numa-note.sh

Outputs appear in output/pdf/. The second file is a standalone proof of the
hypersurface nonuniqueness constructions, including a density
with exactly quadratic zeros. It shares the same
proof source as the book.

Read research/READING-GUIDE.md for three routes through the manuscript,
research/comparison.md for the disposition of every original-book subject and
research/proof-obligations.md for the exact proof boundary. The semipositive prescribed-reference general-measure
equations are reconstructed under positive lower volume, with no bounded mass
hypothesis. Minimal ordinary-type Lp equations for ANY smooth big background are
now reconstructed without BMP or PVP, using strict pole-barrier comparison,
resolution and a singular Gauduchon trace estimate. Minimal-reference GENERAL
non-pluripolar measure existence for any smooth big background is also reconstructed
under BMP and positive lower minimal volume, through higher moments, local smoothing
and fixed-dominator limits. Both metric volume properties imply those hypotheses.
Weighted addition in an arbitrary prescribed class is also reconstructed, with a
common relative lower bound permitting different approximating singularity types
and an infinite undamped weighted reference measure. The arbitrary-model supersolution construction, both general-measure equations,
unrestricted addition and the Lp ordinary-type refinement are now reconstructed.
BMP and positive lower model volume imply metric PVP, so the hypothesis formulation
does not enlarge the cited regime. The main extension beyond BMP and the distinct
geometry/singularity research questions remain open in the manuscript.

Section6.8 refines the infinite-mass witness to a full current with integrable
complex Hessian coefficients. Smooth current approximants converge in coefficient
L1 while their top-degree masses diverge. Small multiples have full Gauduchon traces
converging in total variation and still have infinite determinant integral and
extended mass. The pointwise determinant is compared with, not identified with,
the non-pluripolar measure. Chapters4–7 explain how finite damping supplies
nonlinear information beyond finite traces, without BMP.

Section16.6 proves that ordinary envelopes of dyadic analytic regularizations decrease to the ideal envelope, without BMP, closedness or bigness. This gives a specific approximation criterion for P=Q. In a Hermitian background, rational scaling keeps the approximation in the same background and proves analytic density in the entire elementary ideal-type metric space. A topology on arbitrary ordinary singularity types and a general volume characterization remain open.

Section28.6 proves exact multiplier-ideal and partial-kernel transformation formulas under a modification, including the relative canonical bundle and its Jacobian metric. Closed-background ideal envelopes and non-pluripolar measures also descend. With a Kähler modification and positive closed-curvature mass, the original SGPT equilibrium theorem gives kernel-measure and determinant-functional limits. This geometric hypothesis implies BMP; the general birational identities require no mass bound. The lower-dimensional Hopf limit and general lower Fubini–Study questions remain distinct.

Sections28.10–28.11 treat non-descended isolated logarithmic selecting weights on fibrations. Exact base point-vanishing spaces differ from base multiplier-ideal spaces by O(m^(q-1)) dimensions, giving kernel and determinant limits under a positive-mass base hypothesis. The one-point Hopf model has explicit binomial kernels, an L1 and local-uniform potential limit, and total-variation measure convergence. Moving the pole along its fiber preserves every selected space, even with positive intrinsic growth; the limit can lose the original ideal type. These arguments require no BMP on the total space.

Sections20.8–20.9 give exact higher-dimensional traces over an ambient curve problem under a smooth connected-fiber holomorphic submersion. A Green pullback realizes every compact-model divisor order and its ordinary type is independent of a sufficiently large background. A product formula for extended Monge–Ampère measures includes infinite total mass and gives separated Lp equations. Products with a factor failing BMP have finite- and infinite-mass representatives with all the same multiplier ideals and exact trace numbers. Corollary24.5.1 combines the Gauduchon mass bound with a smooth residual current to determine a canonical ordinary type on each fixed model; this alone does not recover the trace data on further modifications.

Chapters 29–31 develop ordinary Bott–Chern loci, the full supplied transcendental
Nakamaye proof, and locally conformally Kähler geometry. The weak nef-difference
criterion is proved through Monge–Ampère equations and Gauduchon duality. Two local
auxiliary lemmas allow Hermitian reference metrics, retaining the required closed
background; the main numerical theorem remains Kähler. A complete reconstructed
Chern–Ricci-flat Gauduchon rigidity proof is also included.
Lee–Gauduchon strict duality and bimeromorphic invariance are reconstructed in
Section31.8, using classical analytic weak factorization. Strict tests exclude the
full kernel. The explicitly constructed Calabi–Eckmann example has zero cone but
no strongly Gauduchon or balanced metric, exhibiting the limitation of this
invariant. These results require no BMP or LCK assumption. Transverse Vaisman
existence remains an explicit external input.

Checkpoint30 adds continuous Bott–Chern representatives and exceptional trace divisors in Sections24.8–24.9, an affine residual-class identity in Section25.2, and the compact cone base in Proposition29.1.2. Section27.15 reconstructs the elliptic threefold with zero lower mass but a balanced metric of finite upper mass. Section13.22 proves the equivalence between positive lower mass and universal normalized non-pluripolar solvability, without BMP; it constructs obstructing positive L1 densities when lower mass vanishes. Fixed-density volumes, arbitrary individual measures and unbounded exponential equations remain distinct. All five bounded audits passed, and the exact integration map records editorial changes.

Checkpoint31 adds the elliptic closed-current cone and potential/section descent, the exact boundary-volume orders, and the smooth limits of minimizing Gauduchon forms with possibly unbounded metric roots in Section29.7. All three bounded audits passed. Chapters1–5 have received a systematic correctness and exposition pass, with exact scope and pending chapters in the chapter-review ledger. The integration map and build snapshot record checked sources and visual review.

Checkpoint32 integrates the Chapters6–9 systematic correctness and exposition pass: decreasing contact approximation, a streamlined tail criterion, and reuse of the established elliptic local inverse. The technical Hopf and smooth-equation estimates are retained. The chapter ledger records completed Chapters1–9 and remaining work; this root review is not an independent mathematical certification.

Checkpoint33 integrates the complete Chapters10–12 root review. Repeated comparison/energy proofs are shortened, the nonuniqueness examples retain their technical estimates, and two elementary envelope statements lose unused bigness assumptions. Extended volume definitions are separated from the hypotheses for finiteness and comparison. Two notation corrections also appear in the standalone note. The chapter ledger records completed Chapters1–12 and the partial Chapter13 pass.

Checkpoint34 integrates the full Chapter13 review: earlier compactness replaces repeated regularity-based compactness, scalar tails and envelope bounds are streamlined, and cutoff/regularization language is precise. Extended volume invariance is distinguished from conditional comparison. The ledger records completed Chapters1–13 and the partial Chapter14 pass; this remains a working manuscript.

Checkpoint35 integrates the complete Chapters14–15 review. Repeated normalized-exponential limits share one proved lemma, big-background compactness states the exact prerequisites for proof reuse, and adjoint stability uses its earlier proposition. No existence/uniqueness assumptions are changed. Chapters1–15 have received this systematic root pass; later chapters and research remain incomplete.

Checkpoint36 records the full root reread of Chapters16–26 and all their inputs. Repeated divisorial estimates for restriction, addition and self-trace share earlier proved results, and the trace comparison lemma comes before its applications. The ledger now covers Chapters1–26; the remaining chapters, appendix and research are incomplete.

Checkpoint37 completes the root reread of Chapters 27–29 and all twenty inputs. Three proof simplifications reuse established divisorial, envelope and descent results without changing theorem scope. The ledger now covers Chapters 1–29; Chapters 30–32, the appendix and research remain incomplete.

Checkpoint38 completes the first systematic root reread of all 32 chapters, every nested proof input and the appendix. Four edits supply a residual-nefness proof and reuse established divisorial, cone and local ideal arguments. All exact hypotheses remain explicit. The review and reversible map record the scope; this is not whole-book certification. Research and further focused checks remain active.

Checkpoint39 adds the attained individual-L1 subsolution threshold and a counterexample to sufficiency of smooth comparison tests in Section13.23. The bounded audit passed; exact threshold equations and their singularity class remain an explicit problem in Section32.2. The follow-up topology note is unaudited and not included in the book. The compiled manuscript has653 pages.

Checkpoint40 extends the exact Gauduchon formula to integrable densities, shortens the threshold topology proofs, separates the roles of upper/lower mass in the root space, and constructs greatest exponential solutions from subsolutions. Both bounded audits passed; exact zero-exponent equations and normalized-potential capacity convergence remain open. The compiled book has661 pages. The further root-space tail note is unaudited and not part of the book.

Checkpoint41 identifies the bounded-root closure by uniform tails and proves integrable-current attainment, supporting-probability formulas and trace saturation at the subsolution threshold. Smooth dual attainment gives rigidity of threshold subsolutions. Both bounded audits passed; the preceding trace audit's stale dependency-status finding is preserved and resolved by run02. The compiled book has665 pages. Scalar-rate and divisorial working notes are explicitly unaudited and not book content. No exact rough equation or singular-current wedge is inferred.

Checkpoint42 adds the continuity characterization of root tails, divisorial coefficient loss and geometric restrictions on threshold subsolutions. The weak closure of smooth tests is distinguished from all normalized Gauduchon currents. Two bounded audits passed after the explicit nonzero-density restatement. The compiled book has669 pages. Separate research-only drafts about positive-lower-mass threshold identification and nef divisors are not part of this manuscript checkpoint.

Checkpoint43 integrates the passed positive-lower-mass threshold identification and subsequential capacity convergence, and the zero-volume constraint on nef divisors at the threshold. The compiled book has671 pages. These are short deductions from existing chapter results. The exact equation with vanishing lower mass, whole-family convergence and divisor realization remain separate questions; no BMP is imposed.

Checkpoint44 adds a checked quantitative exponential-damping modulus and scalar/total-variation error bounds. The compiled book has673 pages. A separate smooth-dual regularity draft is explicitly unreviewed and is not book content. No general zero-lower-mass exact equation or capacity conclusion is inferred from the error modulus.

Checkpoint45 proves smooth exact threshold equations under smooth strictly positive dual attainment in dimension at least two, without mass properties or root tails. The compiled book has675 pages. A separate closed-background and nonclosed zero-density sharpness draft is explicitly unreviewed and is not book content.

Checkpoint46 adds the checked uniform exponential-limit consequence, closed-background characterization and nonclosed zero-density construction under smooth dual attainment. The book has679 pages. General singular-current regularity, vanishing-lower-mass individual equations and degenerate-density selection remain open outside the stated regimes.

Checkpoint47 revises Chapter13 proof economy and the distinction between scalar, measure and potential limits. It has679 pages and a focused root review, with no new independent theorem audit. The earlier proof boundaries remain.

Checkpoint48 extends exact threshold equations to an assumed smooth semipositive Gauduchon maximizer positive outside a proper analytic set. Differences are divisorial, with a Bott--Chern relation and uniqueness within multiplier-ideal classes. Its bounded audit passed. The681-page build preserves the general singular-current and divisor-realization questions.

Checkpoint49 strengthens and shortens Section27.11.4: maxima and Gauduchon Stokes prove uniqueness of all threshold subsolutions under the same smooth semipositive dual hypothesis. No ideal class or divisor-class independence is prescribed. The separate bounded audit passed; the681-page source was checked. The exploratory polytope draft remains unaudited research history outside the book.

Checkpoint50 adds two audited consequences under smooth semipositive dual attainment: whole-family normalized exponential L1 convergence with a common lower barrier and a quantitative scalar bound, and independence of positive pole-divisor classes. The683-page build has synchronized Chapter13/32 interfaces. No capacity or global regularity conclusion across the degeneracy set is claimed.

Checkpoint51 adds audited quantitative convergence for full Gauduchon traces and local coefficient currents, and polishes Chapters18/19 with a shorter local Bergman L1 proof and explicit pole/restriction examples. The685-page build retains the general capacity and global regularity questions.

Checkpoint52 adds an audited conditional capacity corollary with an explicit smaller-background envelope hypothesis. Chapters20–22 and every nested input were reread; the685-page build clarifies the nonzero section-space case and trace notation while preserving the general open questions.

Primary-source versions and checksums are in research/literature.md and
research/sources/manifest.json. Copyrighted reference PDFs are not bundled. Bounded
Rethlas audit submissions and reports are retained under research/rethlas/verification/.
Historical adverse reports are preserved: common_barrier_compactness_01 is resolved
by common_barrier_repair_01; envelope_testcurves_01 by envelope_testcurves_connected_01;
hopf_reduction_01 by hopf_reduction_reference_repair_01; geometry_problem_connections_01
by geometry_problem_connections_repair_01; closed_loci_lck_connections_01 by
closed_loci_lck_connections_repair_01. Audit premises and scope remain part of each
report. The Nakamaye integration audit accepted all mathematics but recorded a stale
map checksum; that metadata-only finding was repaired and deterministically checked
in research/editorial/nakamaye-integration-review.md. Its adverse report is preserved.
A passed report is not formal verification.

This archive includes sources actually read by the two completed builds. Unincluded
working drafts, generated TeX files, downloaded reference PDFs and verifier internals
are excluded. MANIFEST.json records every packaged file's checksum.
"""
payloads = {str(p.relative_to(root)): p.read_bytes() for p in sorted(selected)}
payloads["README.md"] = readme.encode()
manifest = {
    "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "scope": "Editable manuscript, standalone nonuniqueness note, provenance and bounded audits",
    "files": [{"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
              for name, data in sorted(payloads.items())],
}
out = root / "output/source"
out.mkdir(parents=True, exist_ok=True)
encoded = json.dumps(manifest, ensure_ascii=False, indent=2).encode()
(out / "package-manifest.json").write_bytes(encoded)
payloads["MANIFEST.json"] = encoded
target = out / "hermitian-pluripotential-source.zip"
with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for name, data in sorted(payloads.items()):
        archive.writestr(name, data)
with zipfile.ZipFile(target) as archive:
    assert archive.testzip() is None
    for entry in manifest["files"]:
        assert hashlib.sha256(archive.read(entry["path"])).hexdigest() == entry["sha256"]
print(f"Packaged {len(payloads)} files: {target} ({target.stat().st_size} bytes)")
