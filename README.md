# Singularities in Hermitian pluripotential theory

Working manuscript for the compact Hermitian generalization of Mingchen Xia’s *Singularities in global pluripotential theory*. The supplied svmono template, fonts and conventions are retained. This is an AI-assisted draft for mathematical review; the research remains incomplete.

The current structure has 33 chapters and an appendix. The main sequence develops extended measures, finite damping, envelopes, singularities, individual-density equations, Gauduchon duality and geometric examples without imposing bounded mass or positive lower mass throughout. Each result retains its stated background, reference and data hypotheses.

The Introduction explains the differences from Kähler theory through mass, comparison, energy, equations and singularities. A subject index with clickable page references follows the bibliography; its locators are generated from the manuscript during the build.

The fresh whole-book polish has completed the front units, Chapters 1–33, Appendix A, references and index at checkpoints 297–333. The final post-body Introduction and reader-route review passes; empty-source reconstruction, live publication and private synchronization pass. The writing/polish release is accepted at its recorded review scope. Open-problem research remains active. See [the reading queue](research/editorial/whole-book-polish-queue-20261002.md) for actual completed scopes.

The latest independently reconstructed extension adds Lemma1.6.1 on weighted decreasing products and SectionA.8 on nonclosed cuspidal-product equations. A positive reference repair gives quantitative full-variable small-data existence, ambient Holder1/3 regularity and uniqueness among every bounded competitor; a separate internal-theorem corollary gives bounded existence for arbitrary nonnegative normalization-side Lp data,p>1. The1160-page release and homepage are live-verified; general P23 remains open. See [the scoped review](research/editorial/nonclosed-cuspidal-products-406.md). Sections25.16.7--25.16.8 retain the flat anticanonical/divisor-complement results, and Sections7.5.1 and8.7 retain the standard Hopf shrinking-defect classification. The complete S17 source has passed [independent scoped proof and primary review407](research/editorial/local-critical-adjoints-review-407.md); its local strong-topology density estimates are queued for checked book integration. The preserved S07 divisorial smoothing/adjoint obstruction source awaits complete independent review immediately afterward.

Further direct research adds the complete joint curve/background space in Section 29.14, including zero-area limits, exact analytic closure and gauge/scaling compatibility. Proposition 15.6.19 shows that first polar curvature alone misses isolated logarithmic poles in higher dimension. Corollaries 15.6.10 and 15.6.11 recover that pole after blowing up its point and show that any prescribed countable family of modifications misses some models. Propositions 15.6.20 and 15.6.21 normalize polar trace over modifications and separate analytic ordinary models; their complete coordinate space leaves simultaneous model realization open. Proposition 1.25.1 proves polar curvature invariance under bounded changes, and Corollary 15.6.12 transports the comparison exactly through ordinary-model gauge projection. Proposition 1.25.3 proves closed positive polar curvature for arbitrary pole sets; Lemma 1.25.3 and Corollary 15.6.13 recover those currents from their fixed scalar traces. Proposition 1.25.2 proves exact polar pushforward for arbitrary pole sets, and Proposition 15.6.22 constructs compatible weak polar-current limits for comparison-Cauchy models with arbitrary pole sets, with one genuine pole carrier. Proposition 15.6.23 shows that arbitrary independent Gauduchon choices can fail positive-volume compatibility. Proposition 15.6.24 constructs a positive-volume nonideal model with zero first polar curvature on every modification, on every compact Kähler manifold of dimension at least two. Corollary 15.6.14 computes the scaled model volumes and distances and gives a complete ordered interval in any positive cutoff below the background volume. Proposition 15.6.25 computes the displayed potential mass in arbitrary Hermitian backgrounds, with finite torsion terms. Corollary 15.6.15 extends the complete model interval and its all-modification polar obstruction to Hermitian backgrounds satisfying the power identities, including Gauduchon surfaces. Every choice of forms therefore fails general separation and exact ideal analytic closure for this first-polar candidate. Proposition 15.6.26 computes the mass of every diffuse bounded-equivalent representative in any Hermitian background. Corollary 15.6.16 shows that this class has invariant mass on a surface exactly when the chosen metric is Gauduchon. Proposition 15.6.27 extends the ordinary-model obstruction to backgrounds with both mass properties, including every Hermitian metric on every compact complex surface. Theorem 29.3.3 preserves full residual measures under small-pole ordinary projection, and Corollary 15.6.17 gives a complete diffuse interval in this whole Hermitian mass regime. Proposition 15.6.28 shows that disjoint diffuse models can have the same residual total, and in invariant-mass backgrounds the same two scalar volumes, while their distance remains positive. The unrestricted higher-dimensional topology problem remains open. The author has removed Xean from the workflow.

**Part IX, “Theory under mass bounds”, collects the substantial additional theory:**

- Chapter 29, *Volumes under bounded mass*: finite singularity volumes, comparison, the relation between envelope and volume full mass classes, and the conditional volume characterization of ideal-envelope equality.
- Chapter 30, *Relative equations under positive lower mass*: semipositive big backgrounds and smaller-background model references, assuming positive lower mass and allowing infinite upper mass.
- Chapter 31, *Big backgrounds under bounded mass*: arbitrary smooth big backgrounds, bounded mass and positive lower volume of the model reference.

The former Chapter 30, *A transcendental Nakamaye theorem*, is temporarily excluded at the user’s request. Its three source files and revision history are preserved. The current volume chapter is Chapter 29. The chapters on ordinary Bott–Chern loci and LCK geometry remain active.

The general relative-envelope lemmas and both measure-representation constructions remain in the main theory. A measure representation with an integrable density does not imply an exact equation. Characterizations of mass properties, their failure examples, and geometric cases where those properties follow from other hypotheses also remain in the main sequence.

The [reading guide](research/READING-GUIDE.md) describes the current routes and proof boundaries. The [blueprint](BLUEPRINT.md) records research priorities; [research/STATUS.md](research/STATUS.md) gives the checked release and continuation state. [CHANGELOG.md](CHANGELOG.md) and the private Git history preserve prior arrangements and audits; their historical chapter numbers refer to their respective checkpoints.

The editable manuscript is in [book/](book/). Build the book with `bash scripts/build-book.sh` and the 17-page companion note with `bash scripts/build-numa-note.sh`. Outputs are written to `output/pdf/`. The builds require `latexmk`, pdfLaTeX, BibTeX, MakeIndex, newtx fonts and the packages in `book/preamble.tex`; the supplied template is in `book/style/`.

### Reproduce the TeX environment

Use the existing checkout; no separate worktree is needed. On Debian 13 (trixie), install the base tools if they are absent:

```bash
sudo apt-get update
sudo apt-get install --no-install-recommends python3 latexmk poppler-utils texlive-base texlive-latex-extra texlive-latex-recommended texlive-pictures texlive-fonts-recommended
```

Then, from the repository root:

```bash
bash scripts/setup-tex.sh
source scripts/tex-env.sh
python3 scripts/check-citation-placement.py
bash scripts/build-numa-note.sh
(cd book && latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex)
pdfinfo book/book.pdf | grep '^Pages:'
```

The setup script checks the installed TeX files and, on Debian 13, downloads pinned `texlive-fonts-extra`, `texlive-plain-generic` and `tex-gyre` packages from Debian's signed repository when needed. It extracts them without administrator access into `.texlive-extra` beside the checkout and configures user font maps there. Downloads and build outputs stay outside Git. Run `source scripts/tex-env.sh` in each new shell before a build. If the checkout's parent is not writable, set `NKPT_TEX_STATE_DIR` to an absolute writable directory before running either script. On other platforms, install `newtx`, `doublestroke` and TeX Gyre with the local TeX package manager; the script will verify them without using Debian packages.

The direct `latexmk` command above checks the full PDF locally. In the authoring repository, `bash scripts/build-book.sh` also copies the PDF to `output/pdf/` and attempts the authorized homepage publication. Each account needs its own access to the private repository and authenticated GitHub CLI access for publication; no credentials are stored in this repository.

Successful full-book builds in the authoring repository also publish the PDF to [the author's homepage](https://mingchenxia.github.io/Papers/SHPT_vibe.pdf), updating its description with the last printed page number and current date. Publication uses the authenticated GitHub CLI and Poppler's `pdfinfo` and `pdftotext`; it changes only the PDF and its description in the website repository. Extracted source packages build locally without publishing. If publication fails, keep the compiled PDF and retry `python3 scripts/publish-homepage.py`. GitHub Pages deployment must be checked separately from the verified repository update.

This repository is private. Significant updates are committed and pushed under [AGENTS.md](AGENTS.md). Apart from the explicitly published book PDF, build products, source archives, downloaded full texts, credentials and raw verifier runtime files stay local. Bounded verification reports retain their accepted inputs and scope; they are not formal verification or certification of the whole book. Original references and the Rethlas installation remain unchanged. The private Popovici working reference is consulted before checking any proposed use and is not integrated or packaged.
