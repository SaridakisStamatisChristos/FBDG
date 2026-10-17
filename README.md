# Fixed-Batch Dynamic Gather (FBDG)

Research artifact for **Dynamic Fixed-Batch Retrieval: Structured Codes and Random-Family Locality Barriers**.

**Author:** Stamatis-Christos Saridakis  
**Research state:** October 2026  
**Main theorem status:** human-checkable `PROVED`; not machine-formally verified  
**Novelty status:** `LIKELY DISTINCT WITHIN SEARCH SCOPE`  
**Submission state:** `READY WITH MINOR FIXES` after the 2026-10-17 publication-readiness audit; venue-specific formatting/rules remain separate.

## Core result

FBDG maintains a Boolean vector under point updates while every query asks for the exact contents of one set from a fixed family of `w`-coordinate batches. In the regime

\[
M=\Theta(n),\qquad w=\Theta(\log n),
\]

the repository establishes a structure-versus-randomness separation at write locality two:

- **structured fixed-support families:** explicit infinite families achieve `u = 2`, `q = 2`;
- **random fixed-support families:** with high probability every exact canonical representation with arbitrary nonlinear `w`-bit cells and fully adaptive queries requires `q = Ω(w)`;
- **moving/history-dependent supports:** the full `Ω(w)` lower bound remains open, while a state-local congestion theorem shows that any `q=o(w)` escape must maintain high-influence write hubs at every reachable state.

The fixed-support qualification is essential. Nothing in this repository claims the main `Ω(w)` theorem for unrestricted state-dependent or history-dependent write locations.

## Repository layout

```text
.
├── README.md
├── STATUS.md
├── REPRODUCIBILITY.md
├── CITATION.cff
├── Makefile
├── paper/
│   ├── fbdg.md               # canonical manuscript source
│   ├── fbdg.tex              # generated LaTeX export
│   ├── fbdg.pdf              # generated rendered paper
│   ├── fbdg.docx             # generated Word export
│   └── references.bib
├── proof/
│   └── fixed_support_theorem.md
├── validation/
│   ├── README.md
│   ├── fbdg_structured_validate.py
│   ├── EXPECTED_OUTPUT.txt
│   └── manifest.json
├── audit/
│   └── FINAL_RESEARCH_AUDIT_2026-10-13.md
├── history/
│   ├── README.md
│   ├── FBDG_PRIOR_ART_AND_PAPER_HISTORY_2026-10-13.md
│   ├── FBDG_PAPER_DRAFT_v0_1_2026-10-13.md
│   ├── FBDG_PAPER_STATE_v0_1_2026-10-13.md
│   └── fbdg_references_v0_1_2026-10-13.bib
└── .github/workflows/validate.yml
```

`history/` contains dated research snapshots and continuity material retained for provenance and reproducibility. Those files are non-authoritative unless a current document explicitly incorporates them; see `history/README.md`.

## Main theorem

Let `B_1,...,B_M` be independent uniform `w`-subsets of `[n]`, with constants `c_-,c_+,μ_-,μ_+>0` satisfying

\[
c_-\log n\le w\le c_+\log n,
\qquad
\mu_-n\le M\le\mu_+n.
\]

For a canonical encoding into `w`-bit dynamic cells, define the essential fixed support of source coordinate `j` by

\[
S_j=\{c:\exists x, E_c(x)\ne E_c(x\oplus e_j)\}.
\]

If `|S_j|≤2` for every `j`, then with probability `1-o(1)` over the random batch family,

\[
q=\Omega(w)
\]

for every exact query algorithm, even with arbitrary nonlinear cell contents and fully adaptive probing.

The proof uses a uniform **diffuse-versus-hub dichotomy**. Diffuse supports yield an `Ω(w)` matching in some random batch; hub-concentrated supports reduce to an exact sketch-and-adaptive-probe problem on bounded residual source groups.

The manuscript normalizes dynamic cell width to the batch size `w`. The lower-bound proof is robust to any cell width `b=Θ(w)`: capacity and sketch terms change by constant factors while the diffuse branch is unchanged. The paper keeps `b=w` to isolate the locality question cleanly and because the entire requested answer then fits information-theoretically in one cell.

## Structured upper bound

The paper also gives an explicit Fano-based family with

\[
n=M=7t2^t,\qquad w=3t=\Theta(\log n),\qquad u=2,\qquad q=2.
\]

This shows that two fixed writes do **not** universally force linear recovery locality; the incidence structure of the batch family matters.

## Reproduce the validation artifact

The validation script uses only the Python standard library:

```bash
python validation/fbdg_structured_validate.py
```

To compare against the frozen retained output:

```bash
python validation/fbdg_structured_validate.py > /tmp/fbdg-output.txt
diff -u validation/EXPECTED_OUTPUT.txt /tmp/fbdg-output.txt
```

`validation/manifest.json` records the command, Python assumptions, expected counts, and retained-output checksum. CI performs the same exact-output check.

These checks validate the finite structured construction. They are not evidence for the asymptotic lower bound, which is mathematical.

## Build the paper

With Pandoc and XeLaTeX installed:

```bash
make paper
```

or manually:

```bash
pandoc paper/fbdg.md --citeproc --bibliography=paper/references.bib --standalone -o paper/fbdg.tex
pandoc paper/fbdg.md --citeproc --bibliography=paper/references.bib --standalone -o paper/fbdg.docx
pandoc paper/fbdg.md --citeproc --bibliography=paper/references.bib --pdf-engine=xelatex -V geometry:margin=1in -V fontsize=10pt -o paper/fbdg.pdf
```

`paper/fbdg.md` is the canonical manuscript source. Generated exports should be refreshed before a tagged archival release.

## Scientific boundary

The exact frontier preserved by the manuscript is:

- `structured fixed-support u=2`: `q=O(1)` (indeed `q=2`);
- `random fixed-support u=2`: `q=Ω(w)`;
- `unrestricted moving/history-dependent u=2`: full `Ω(w)` is **OPEN**.

Please read `STATUS.md`, the formal package under `proof/`, and the audit materials before reusing theorem statements.
