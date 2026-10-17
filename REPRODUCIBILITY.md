# Reproducibility

The central lower bound is a mathematical theorem; no benchmark or empirical experiment is required for its validity. The executable artifact validates the finite structured construction and preserves the exact outputs reported in Appendix C of the paper.

## Requirements

- Python 3.9+ for validation (standard library only).
- CI currently exercises Python 3.12.
- Pandoc + XeLaTeX only if rebuilding the manuscript exports.

## Validation

Run from the repository root:

```bash
python validation/fbdg_structured_validate.py
```

For exact reproduction of the retained output:

```bash
python validation/fbdg_structured_validate.py > /tmp/fbdg-output.txt
diff -u validation/EXPECTED_OUTPUT.txt /tmp/fbdg-output.txt
```

The script performs:

1. exhaustive validation of the fixed Fano decoder assignment over all `2^7` states and seven requested lines (`896` cases);
2. exhaustive validation of every valid cell-pair/line decoder relation (`1536` cases);
3. construction of `7t` distinct all-active global batches for `t in {1,2,3,4,5,8}`;
4. deterministic-seed randomized differential checks against raw source bits for those `t` values.

The retained stdout is `validation/EXPECTED_OUTPUT.txt`. Its SHA-256 is:

```text
3f4cf123386c0239858e0ef597a91b4650574447c7a5a0a77b1788ab2c242012
```

`validation/manifest.json` records the command, Python assumptions, retained counts, output checksum, and the validator Git-blob identity used when this reproducibility package was frozen on 2026-10-17. CI rejects changes that alter the retained stdout without an explicit artifact update.

## Proof reproducibility

The complete fixed-support proof is duplicated in two forms:

- `paper/fbdg.md` - canonical integrated manuscript source;
- `proof/fixed_support_theorem.md` - focused theorem package with dependencies and repair ledger.

The proof package records earlier counterexamples to insufficient intermediate lemmas so that repaired conditions are not accidentally removed.

## Scope of executable evidence

The validation program supports the finite constructive side of the paper. It is **not** evidence for Theorem 5.1 or the asymptotic random-family lower bound, whose support is the mathematical proof.

## Rebuilding the paper

With Pandoc and XeLaTeX available:

```bash
make paper
```

The Markdown source is canonical. Generated `.tex`, `.docx`, and `.pdf` files should be refreshed from that source before a tagged archival release.
