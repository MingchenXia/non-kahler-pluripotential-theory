# Singularities in Hermitian pluripotential theory

Working manuscript for the compact Hermitian generalization of Mingchen Xia’s *Singularities in global pluripotential theory*. The supplied svmono template, fonts and conventions are retained. This is an AI-assisted draft for mathematical review; the research remains incomplete.

The current structure has 33 chapters and an appendix. The main sequence develops extended measures, finite damping, envelopes, singularities, individual-density equations, Gauduchon duality and geometric examples without imposing bounded mass or positive lower mass throughout. Each result retains its stated background, reference and data hypotheses.

The Introduction explains the differences from Kähler theory through mass, comparison, energy, equations and singularities. A subject index with clickable page references follows the bibliography; its locators are generated from the manuscript during the build.

**Part XII, “Theory under mass bounds”, collects the substantial additional theory:**

- Chapter 29, *Volumes under bounded mass*: finite singularity volumes, comparison, the relation between envelope and volume full mass classes, and the conditional volume characterization of ideal-envelope equality.
- Chapter 30, *Relative equations under positive lower mass*: semipositive big backgrounds and smaller-background model references, assuming positive lower mass and allowing infinite upper mass.
- Chapter 31, *Big backgrounds under bounded mass*: arbitrary smooth big backgrounds, bounded mass and positive lower volume of the model reference.

The former Chapter 30, *A transcendental Nakamaye theorem*, is temporarily excluded at the user’s request. Its three source files and revision history are preserved. The current volume chapter is Chapter 29. The chapters on ordinary Bott–Chern loci and LCK geometry remain active.

The general relative-envelope lemmas and both measure-representation constructions remain in the main theory. A measure representation with an integrable density does not imply an exact equation. Characterizations of mass properties, their failure examples, and geometric cases where those properties follow from other hypotheses also remain in the main sequence.

The [reading guide](research/READING-GUIDE.md) describes the current routes and proof boundaries. The [blueprint](BLUEPRINT.md) records research priorities; [research/STATUS.md](research/STATUS.md) gives the checked release and continuation state. [CHANGELOG.md](CHANGELOG.md) and the private Git history preserve prior arrangements and audits; their historical chapter numbers refer to their respective checkpoints.

The editable manuscript is in [book/](book/). Build the book with `bash scripts/build-book.sh` and the 17-page companion note with `bash scripts/build-numa-note.sh`. Outputs are written to `output/pdf/`. The builds require `latexmk`, pdfLaTeX, BibTeX, MakeIndex, newtx fonts and the packages in `book/preamble.tex`; the supplied template is in `book/style/`.

This repository is private. Significant updates are committed and pushed under [AGENTS.md](AGENTS.md). Build products, source archives, downloaded full texts, credentials and raw verifier runtime files stay local. Bounded verification reports retain their accepted inputs and scope; they are not formal verification or certification of the whole book. Original references and the Rethlas installation remain unchanged. The private Popovici working reference is consulted before checking any proposed use and is not integrated or packaged.
