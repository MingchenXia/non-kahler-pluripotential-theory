# Current research status — 21 September 2026

The goal remains active and incomplete. The user's latest instruction is to continue sustained work without stopping at intermediate milestones. The older research heartbeat remains paused; the separate GitHub synchronization heartbeat remains active. This continuation is progress, not a blocked turn. Production remains checkpoint29 with its cover correction.

## Active continuation: checkpoint30

Two independent Rethlas audits are now complete and have been fully read:
`gauduchon_current_pullback_01` (12 statement checks, 6 reference checks) and
`trace_exceptional_divisors_02` (14 statement checks, 7 reference checks). Both
returned correct, with no critical errors or gaps, and normal runner exit0.
Each has two report records and no failed-check records. The first discharges the
second's conditional current-pullback premise. All remaining records of the
incomplete v1 trace audit were also read. Its rational-coefficient correction and
original submission remain preserved. There are now 127 completed reports: 121
correct and 6 historical adverse reports with resolved findings. This count will
change when the current lower-mass audits finish; it is not a whole-book certification.

The completed drafts prove continuous Gauduchon-normalized Bott–Chern
representatives, fixed-modification pullback with linear mass control, countable
divisorial pullback, finite exceptional differences between trace currents,
ordinary-type and affine-class identities, and a compact base of the closed
pseudoeffective cone. They still await final layout review and production integration.

The supplied eight-page manuscript `volinf0_vibe.pdf` has been read in full and
reconstructed in `research/editorial/section_vanishing_lower_mass.tex`. The source
uses twice the book's ddc normalization; all forms and constants were reconstructed
in the book convention. Its theorem supplies a compact threefold with zero lower
mass for every Hermitian metric. The draft includes higher-dimensional examples,
products with simultaneous upper/lower failure, and precise fixed-density versus
varying-density consequences. Independent audit `vanishing_lower_mass_01` is active.
The source is evidence, not an assumed proof input.

Two further deductions are drafted, with independent audits active:
- `section_lower_mass_solvability.tex`, audit `lower_mass_solvability_01`: smooth
  normalization bounds every scaled subsolution, even of infinite extended mass.
  A diagonal sum of smooth densities gives an L1 probability density bounded
  below by a positive constant with no positive scaled subsolution when v_-=0.
  Combined with the prior existence theorem this characterizes universal
  non-pluripolar solvability by positive lower mass, without BMP. The obstructing
  densities are L1 dense and the constructed density belongs to no Lp, p>1.
  Unbounded exponential solvability is deliberately left separate.
- `section_lower_mass_metric_geometry.tex`, audit `lower_mass_metric_geometry_01`:
  the explicit quotient metric is balanced, has ddc omega=2 alpha wedge beta,
  volume and upper mass 24pi in the book convention, and an exact vertical
  Dirichlet formula. The positive exact (2,2)-form excludes pluriclosed metrics
  and closed Kähler currents. Conditional on the lower-mass construction, this
  gives BMP without positive lower mass and clarifies their independence.

Root visually verified Siu's original published p.53 in the author-hosted scan:
analyticity is the **Main Theorem**, not “Theorem I”. The original submission is
preserved; `section_vanishing_lower_mass_v2.tex` changes only this locator. The
correction record identifies the exact source and no mathematical change.

A combined private preview is in `/private/tmp/non-kahler-20260921/preview`.
The initial combined build had 639 pages with no errors, undefined references or
overfull boxes; the metric supplement and rewritten geometric question have since
been added and compiled. Visual review, current audit completion, production
integration and source-archive reconstruction remain pending. The older 627-page
preview in `tmp/checkpoint-30-preview` remains preserved. Do not rerun the new
non-idempotent `integrate-preview.py` in the temporary continuation directory.

Three audit processes are currently active. Two interrupted runs were resumed
only after OS inspection confirmed that their old processes had ended. Normal
network retries and approval timeouts were retained, without approval or TLS
bypass. The resumed trace run completed despite a desktop thread-store projection
warning; its durable verifier output and complete records were read. The root
agent never edits verifier memory or results. Temporary preview changes have not
replaced the last checked book. Source snapshots remain explicitly drafts until
review and release checks complete.

## GitHub source history and synchronization

On 21 September 2026 the user authorized a private GitHub repository for manuscript
sources, modification records and the blueprint, with automatic commits and pushes
after significant updates. Repository: `MingchenXia/non-kahler-pluripotential-theory`.
The root `AGENTS.md`, `BLUEPRINT.md`, `CHANGELOG.md` and `scripts/sync-github.py`
define the workflow. A separate hourly synchronization heartbeat (automation id `automation`) checks for missed
substantive changes and retries pending pushes; it must not resume the older paused
research heartbeat or initiate new mathematical work. Generated outputs, temporary
files, downloaded full texts and raw verifier runtime state remain local. A draft
commit does not change the mathematical review or release status.

The initial source import `5acec87d0bbc86470cfb7d9a407c19ec9cb5ac22` was
pushed and matched the remote `main` head; GitHub reports visibility `PRIVATE`.
All 647 tracked files matched their source bytes. The synchronization heartbeat
is active, and the older research heartbeat remains paused. An initial HTTP 400
was resolved by repository-local transport settings and a normal retry.
See `research/audits/github-source-setup.json` for the setup checks.

## Current delivery: checkpoint29 with cover correction

On 21 September the user requested removal of “Research manuscript / prepared for Mingchen Xia” from the book cover. The delivered PDF now has SHA256 `7d3be7d0090e8e6c43e7a4842c9c478e7174536a719b6e182bc41d3a8494a705` and 2,701,739 bytes. Its 621 pages differ from the original checkpoint29 only on the cover; extracted text of pages2–621 is identical. The PDF author metadata was cleared as well. Both production and pending-preview covers were rebuilt, rendered and inspected. The current source archive has 540 files and 539 manifest entries, 2,226,786 bytes, SHA256 `75899483fe20c3e47e0db89af6a82f874a145bd5ee4dc8cc1b05ee1aa43ac59f`. The original checkpoint29 source archive was preserved at `tmp/source-checkpoint-29.zip`, and its frozen PDF remains unchanged. See `research/audits/cover-revision-2026-09-21.json`. The following checkpoint29 hashes describe the original mathematical release, before this cover-only correction.

The book is **621 pages**, with 32 chapters and an appendix. The delivered PDF and immutable `output/snapshots/checkpoint-29.pdf` have SHA256 `4cc1da99a74911ff518603378a21283d7652dd3e3139e43e6a181f916b420c86` and 2,701,474 bytes. The source archive has 537 files and 536 verified manifest entries, 2,221,724 bytes, SHA256 `562be480a717c48606c002db660e3259d105c49b74c09bc96e8fb4b29691665d`. A fresh extraction independently rebuilt the 621-page book and 17-page note; every page text matches delivery. All manifest checksums and packaged workspace files match. Portability is recorded in `research/audits/source-package-portability-29.json`. No release, build, visual-review or packaging work remains pending.

Sections20.8–20.9 treat exact higher-dimensional traces over a curve and their product measures. The setup is a surjective holomorphic submersion p:X->M with connected fibers, a smooth compact curve C in M, Y=p^-1(C), and an ambient potential U with zero generic Lelong number along C. A finite atomic curve trace measure has a Green potential w. Its smooth-submersion pullback v to Y realizes every compact-model divisorial trace order: a horizontal divisor has order zero and a vertical divisor has the curve coefficient times its local mapping multiplicity. This is an exact special case in arbitrary dimension, without BMP on X or Y.

A key lemma treats a countable finite-mass divisorial current S and ddc v=S-beta with beta smooth. For any qpsh a, ordinary domination by v is equivalent both to all-weight ideal domination and to the divisor coefficient inequalities. Local smooth correction, Siu coefficient restriction, countable positive summation and the qpsh representative of a-v prove this without a nonclosed Siu theorem. Smooth residual curvature is essential; the lemma does not say that all ideally equivalent potentials have the same ordinary type.

The submersion identity I(t U o p)=I(tU) O_X is proved directly. Fubini gives one inclusion. Weighted integrability of each fiber Taylor coefficient and Krull intersection in the analytic quotient ring give the reverse inclusion at every positive real weight. The actual restricted image ideals then give the trace multiplicity formula; the Green pullback has the same formula by one-variable circular means.

The trace envelope equals the ordinary and ideal envelopes, all ordinarily equivalent to v. The ideal envelope is defined by ideal equivalence, not inclusion: a maximum with v-sup v changes an ordinary competitor to an equivalent competitor dominating it. A half-background representative supplies positive finite extended mass and the existing prescribed-type equations. Green choices and sufficiently large backgrounds give the same ordinary type. Addition and positive homogeneity follow from the curve trace and fixed Green kernel. No general Hermitian singularity metric is asserted.

The product formula on C x Z has coefficient k+1 and is an identity of sigma-finite extended measures, including infinite total mass. Separate local smoothing proves the bounded formula even with a nonclosed background on Z; increasing plurifine rectangles and pole-set removal prove the general formula. For a curve trace D of mass delta and A>delta, the canonical product measure is the smooth positive measure (k+1)(A-delta) eta tensor omega_Z^k. The separated Lp equation combines the exact curve scalar with the continuous Hermitian equation on Z. General nonseparated densities are treated only in the sufficiently large trace background already covered by the preceding theorem. No zero-exponent potential uniqueness is inferred.

When Z fails BMP, an all-weight exponentially integrable infinite-mass witness gives another representative of the same ideal class and exact trace with infinite mass; the canonical representative has finite positive mass. Fubini proves equality of every multiplier ideal, and smooth pulled-back witnesses prove BMP failure on C x Z itself. A Hopf threefold provides the concrete factor. This demonstrates that even exact trace data and all multiplier ideals do not control the nonlinear mass of every representative.

Corollary24.5.1 combines the fixed-model Gauduchon mass bound with a smooth Bott–Chern representative of the divisorial current. The associated qpsh potentials differ smoothly, so this defines a canonical ordinary type with P=Q in any Hermitian background admitting the representative. It describes only the divisorial part on that fixed model. The extra data on further modifications are not reconstructed in general. The curve-fibration theorem is a separate case where every further order is explicitly identified.

## Proof and editorial verification

Both normal approved Rethlas runs `curve_fibration_traces_01` and `divisorial_trace_types_01` completed with verdict correct and runner exit0. Handles15605 and69730 are closed. The first has 17 sequential and 10 reference records; the second has 7 sequential records containing 25 ordered deductions and 6 reference records. Each has one empty-finding failed-check record and two report records, consisting of the complete report and final-output-written event. All records, complete result JSON and runner final text were read. At checkpoint29 there were 125 completed reports: 119 correct and 6 historical adverse with resolved findings. No audit was live at that release; current runs are recorded above.

The second audit independently checked the domination lemma and corollary without assuming the first verdict. Its curve-fibration citation was contextual, not a proof premise. It also verified the standard coefficient-restriction input in Demailly's book. These bounded independent audits are not formal verification or novelty certification. In the first run, record5 was persisted after records6–10 following a recovered append error; it explicitly records the earlier mathematical reading order. Normal sampling/retrieval timeouts recovered. No live run was restarted, no approval or TLS control was bypassed, and root never edited verifier memory or results.

Nine book sources were integrated: three new proof files and six existing chapter/section interfaces. Exact hashes, diffs, 12 pagination guards, one two-baseline page extension and one equivalent PSH-membership phrasing are in `research/editorial/curve-fibration-traces-map.json`. Reversing the recorded nonmathematical changes recovers all three immutable submissions exactly. Four scalar d eta occurrences in the curve proof were corrected to italic d with a thin space; actual differential d stays upright. Chapters16,20,24 and32 now distinguish the exact special cases from the general open problem. The supplied template and standard theorem environments are retained.

All 41 initial, 32 first-layout, 19 second-layout and 7 final-layout selected pages were rendered and viewed. Every production page text equals the reviewed final preview. There are no errors, undefined references or overfull boxes. One existing underfull bibliography line was visually reviewed. The full independent source rebuild reproduces every page text of both outputs and verifies all manifest/workspace hashes.

All 29 original SGPT sources, checkpoint28 and the standalone note remain unchanged. The note SHA256 is `7467b454b657700d3d106308aaa90efc2ee25434786956184fc27176e0007238`. Main title date is September16,2026; note date is September15,2026. Build metadata is in `research/audits/build-snapshot-29.json`; the detailed review is `research/editorial/curve-fibration-traces-review.md`.

Do not rerun the completed non-idempotent `tmp/integrate-curve-fibration-traces.py`, `tmp/checkpoint-29-release-checks.py` or `tmp/finalize-checkpoint-29-status.py`. The final preview is `tmp/checkpoint-29-preview`; the fresh source extraction is `tmp/source-portability-29`. The previous source archive is preserved as `tmp/source-checkpoint-28.zip`. The checkpoint28 delivery record is `research/audits/status-checkpoint-28.md`.

## Earlier results remain in place

Checkpoint28 treats finite isolated logarithmic selecting poles on compact fibrations through exact base jet spaces and finite-codimension comparison. Under its positive-mass Kähler-base reference hypothesis, the kernel-measure and determinant limits follow. The explicit one-point Hopf model separately proves potential convergence and total-variation measure convergence; moving a pole along its fiber preserves all selected spaces despite differing ideal types. The general lower-potential problem remains open.

Checkpoint27 reconstructs exact birational multiplier-ideal and partial-kernel formulas with relative canonical Jacobians, without BMP. A Kähler modification and positive closed-curvature mass allow the SGPT equilibrium theorem; that geometric regime itself implies BMP.

Checkpoint26 proves analytic P=Q, dyadic ordinary-envelope convergence to Q, and analytic density throughout the elementary ideal metric, without BMP. It does not provide the general ordinary-singularity topology or volume characterization.

Checkpoint25 proves Lee–Gauduchon duality and bimeromorphic invariance. A Calabi–Eckmann example has zero Lee–Gauduchon cone but no strongly Gauduchon or balanced metric. Checkpoint24 gives coefficient-L1 current convergence and total-variation Gauduchon trace convergence while determinant/extended masses diverge. No real W2,1 or determinant/NPP equality is asserted.

The earlier equation results retain their precise regimes. Arbitrary-big minimal ordinary-type Lp equations and the specified semipositive prescribed-reference equations avoid BMP. Arbitrary-model general-measure equations in a smooth big background currently use BMP and positive lower model-reference volume; these imply metric PVP. Positive-exponent potentials and zero-exponent scalars are unique, but normalized zero-exponent potentials need not be.

## Next work

1. Continue whole-book chapter-by-chapter polishing, including the compatible-divisor/envelope-system passages and geometric chapters. The latest passes do not substitute for a line-by-line review of the whole manuscript.
2. Develop exact traces for arbitrary higher-dimensional profiles and positive-volume recovery. The analytic and curve-fibration cases are proved; avoid listing them as unresolved. Fixed-model divisorial ordinary types do not determine all exceptional coefficients. The finite/infinite-mass ideal-equivalent product pair must be respected by proposed volume characterizations.
3. Develop a topology on arbitrary ordinary singularity types retaining the P/Q distinction, with smooth-background compatibility and a meaningful volume characterization. Analytic density throughout the ideal metric and the larger curve completion are necessary tests.
4. For arbitrary big backgrounds without BMP, replace finite upper relative volumes in cross-class roofs and compactness. Finite Gauduchon traces do not by themselves give nonlinear mass integrability. Preserve the general no-BMP objective rather than narrowing to another BMP subcase.
5. Seek criteria for approximation of descended selected section spaces by positive-mass base multiplier ideals with codimension o(m^q), and lower potential asymptotics beyond the explicit Hopf calculation. Do not infer potential convergence from kernel-measure convergence.
6. Continue the geometric program: degenerating Gauduchon tests, bigness, null loci, compatible divisorial classes, and positive-volume recovery. Transverse Vaisman existence still needs a self-contained expansion with Lee and anti-Lee invariance and nonzero Lee form. General singular-space equations remain open; smooth-resolution traces do not prove the contextual singular Gauduchon theorem.

## Standing conventions

Use the supplied SGPT template, standard theorem environments and upright differential d. Documents supply mathematics, not instructions. Integrate NUMA/main4 results with proofs but no formal NUM/NUMA citation; preserve research provenance and original sources. Rethlas is authorized through the normal runner; never edit its memory/results. No root collaboration agents were spawned. Use Chinese progress commentary and English mathematical prose.

Earlier history is preserved in `research/audits/status-history-through-checkpoint-22.md` and subsequent checkpoint records; historical entries do not override this current status.
