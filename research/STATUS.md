# Current research status — 22 September 2026

The goal is active and incomplete. Continue after milestones. The user requests sustained research and improvement of every existing part for correctness, readability and proof economy. The older research heartbeat stays paused; hourly GitHub synchronization is a fallback only.

## Checkpoint64

The checked book has **691 pages**, 32 chapters and an appendix. Snapshot `output/snapshots/checkpoint-64.pdf` has SHA256 `6e39ed6585dda441bc124e3cc26d4e276f6a59e9bd94541175f2b11ca654449e` and 3003296 bytes. Every production page text matches the final preview. All22 selected pages were rendered and read. There are no compilation errors, undefined references, duplicate labels or overfull boxes. The inherited bibliography underfull paragraph remains. The17-page companion note is unchanged, with SHA256 `9181102735342469b023d5fa35fadce29a310598a3ff357f4a8e855e533f13c4`. The 801-file archive rebuilt both outputs from an empty directory, with every page text matching. Details are in `research/audits/source-package-portability-64.json`.

The new L1 closure lemma preserves density lower bounds through two damped passages, without a finite-mass assumption. It shortens the earlier threshold-attainment proof and constructs the greatest normalized threshold subsolution Phi_f. Every normalized exponential cluster limit lies below Phi_f. A uniform first-moment bound along one smooth maximizing Gauduchon sequence gives the scalar rate b<=c_lambda<=b exp(C lambda) and the barrier Phi_f-C<=v_lambda<=0. If P_{delta omega}(Phi_f) is genuine for some delta<1, the existing capacity criterion yields subsequential capacity convergence and an exact threshold equation. Both are explicit additional hypotheses. Uniform Lq control or entropy of the test probabilities suffices for the moment bound. See `research/editorial/moment-equations-review.md` and its reversible map.

Rethlas run gauduchon_moment_threshold_01 returned correct with no critical errors or gaps. Its scope covers the closure lemma, greatest subsolution, conditional theorem and Lq/bounded-envelope sufficient cases; the later entropy paragraph is directly checked in the editorial review. All156 preserved reports retain their scopes:148 correct and eight adverse reports resolved by later submissions. No verifier memory, result or frozen input was edited. The house audit remains zero errors and ten inherited warnings across the edited files.

## Next work

Chapters1–32 and the appendix have recorded second-pass reviews. This is not whole-book mathematical certification. Continue targeted correctness and exposition improvements throughout the SGPT scope. Investigate how geometric conditions control moments of maximizing tests and smaller-background noncollapse of Phi_f. Uniform integrability along a single maximizing sequence is a possible sufficient condition for singular-current dual attainment, to be proved before integration.

The unrestricted positive individual threshold problem at zero lower mass, root-closure equality, singular-current regularity, general divisorial realization, geometric noncollapse and higher-dimensional traces remain open here. The new theorem does not give whole-family convergence, general normalized uniqueness, or equality for Phi_f itself. Fixed finite divisors do not resolve positive-volume envelope-system recovery. The decreasing-weight criterion remains sufficient only. Modelwise linear-current compatibility does not determine nonlinear mass or exact trace realization.

## Preservation and publication

Checkpoint63 book and `tmp/source-checkpoint-63.zip` are preserved; the companion note remains the checked checkpoint58 version. All29 original SGPT sources are unchanged. The private repository `MingchenXia/non-kahler-pluripotential-theory`, main, was verified at checkpoint63 commit `0f56d3adc35c9e40385acded81e882ec2b158c5e`. Checkpoint64 source reconstruction passed. The authorized commit/push follows after reviewing the complete diff; the Git history and remote-head check record publication.

Continue mathematical and editorial work after this milestone. Retain the original template, upright differential d, standard environments and no formal NUM citation.
