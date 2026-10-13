# Reproducibility

The central lower bound is a mathematical theorem; no benchmark or empirical experiment is required for its validity. The executable artifact validates the finite structured construction and preserves the exact outputs reported in Appendix C of the paper.

## Requirements

- Python 3.9+ for validation (standard library only).
- Pandoc + XeLaTeX only if rebuilding the manuscript exports.

## Validation

Run:

```bash
python validation/fbdg_structured_validate.py
```

The script performs:

1. exhaustive validation of the fixed Fano decoder assignment over all `2^7` states and seven requested lines (`896` cases);
2. exhaustive validation of every valid cell-pair/line decoder relation (`1536` cases);
3. construction of `7t` distinct all-active global batches for `t in {1,2,3,4,5,8}`;
4. deterministic-seed randomized differential checks against raw source bits for those `t` values.

The script was rerun during the final October 13, 2026 research audit and reproduced the counts stored in the paper.

## Proof reproducibility

The complete fixed-support proof is duplicated in two forms:

- `paper/fbdg.md` - integrated manuscript proof;
- `proof/fixed_support_theorem.md` - focused theorem package with dependencies and repair ledger.

The proof package records earlier counterexamples to insufficient intermediate lemmas so that the repaired conditions are not accidentally removed.
