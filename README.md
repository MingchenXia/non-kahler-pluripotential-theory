# Singularities in Hermitian pluripotential theory

Working manuscript for the compact Hermitian generalization of Mingchen Xia’s *Singularities in global pluripotential theory*. The supplied svmono template, fonts and conventions are retained. This is an AI-assisted draft for mathematical review; the research remains incomplete.

The current structure has 33 chapters and an appendix. The main sequence develops extended measures, finite damping, envelopes, singularities, individual-density equations, Gauduchon duality and geometric examples without imposing bounded mass or positive lower mass throughout. Each result retains its stated background, reference and data hypotheses.

The Introduction explains the differences from Kähler theory through mass, comparison, energy, equations and singularities. A subject index with clickable page references follows the bibliography; its locators are generated from the manuscript during the build.

The fresh whole-book polish has completed the front units and Chapters 1–9 at checkpoints 298–306. Chapter 10 is next; the final Introduction reread and open-problem research remain active. See [the reading queue](research/editorial/whole-book-polish-queue-20261002.md) for actual completed scopes.

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
