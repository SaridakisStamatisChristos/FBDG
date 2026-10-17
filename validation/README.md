# Structured-family validation

The executable artifact validates the **positive structured construction** only. The random-family lower bound is a mathematical theorem and is not inferred from testing.

## Run

From the repository root:

```bash
python validation/fbdg_structured_validate.py
```

No third-party Python packages are required. The CI workflow uses Python 3.12; the script is compatible with Python 3.9+.

## Exact retained output

The canonical expected stdout is stored in:

```text
validation/EXPECTED_OUTPUT.txt
```

To verify byte-for-byte agreement:

```bash
python validation/fbdg_structured_validate.py > /tmp/fbdg-output.txt
diff -u validation/EXPECTED_OUTPUT.txt /tmp/fbdg-output.txt
```

The expected counts are:

- fixed Fano decoder assignment: `896` exhaustive state/query cases;
- every valid cell-pair/line decoder relation: `1536` exhaustive cases;
- packed-family differential checks: `7000`, `14000`, `21000`, `28000`, `7000`, and `11200` checks for `t = 1,2,3,4,5,8` respectively.

## Manifest

`validation/manifest.json` records the validation command, retained expected-output checksum, the validator's Git blob identity at the time the reproducibility package was frozen, and the exact claims that the script checks.

This artifact is evidence for the finite constructive side of the paper. It is **not** evidence for Theorem 5.1 or any asymptotic lower bound.
