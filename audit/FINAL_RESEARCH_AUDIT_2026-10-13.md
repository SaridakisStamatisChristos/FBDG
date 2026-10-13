# Final SOTA Research Audit - 2026-10-13

## Verdict

**READY WITH MINOR FIXES** for a full technical paper/preprint. The main theorem survived the formal proof audit; no theorem-breaking defect was found.

## Supported central claims

- Random canonical fixed-support nonlinear `u=2` implies `q=Ω(w)` for `M=Θ(n)` and `w=Θ(log n)`, with arbitrary nonlinear `w`-bit cells and fully adaptive exact queries.
- The Fano-based structured family achieves `u=2, q=2` asymptotically.
- The state-local congestion theorem remains valid without fixed support/canonical global memory and isolates the high-influence-hub requirement for any moving-support escape.

## Scope boundary

The main theorem **does not** cover state-dependent or history-dependent moving write supports. The full moving-support `Ω(w)` lower bound remains open.

## Novelty verdict

`LIKELY DISTINCT WITHIN SEARCH SCOPE`.

The audit did not identify a materially equivalent theorem combining random fixed batch families, exact vector recovery, two fixed update locations per source coordinate, arbitrary nonlinear canonical encoding, fully adaptive probing, and an `Ω(w)` lower bound. This is bounded evidence, not an absolute first-priority claim.

## Minor fixes requested by the audit

1. Add close literature on restricted-query/reconstruction-size batch codes, stronger batch-code lower bounds, and older update-efficiency coding work.
2. Ship the validation script referenced in Appendix C.
3. Synchronize the explicit theorem constant and spreading-union-bound notation between manuscript and focused proof package.
4. Clarify deterministic state-local update semantics and remove the wide display responsible for an overfull PDF line.

## Repository packaging status

All four fixes above are incorporated in the canonical files committed with this research package. The validation script was rerun and reproduced:

```text
896
1536
(7, 7, 7000)
(14, 14, 14000)
(21, 21, 21000)
(28, 28, 28000)
(35, 35, 7000)
(56, 56, 11200)
```

The proof remains human-checkable rather than machine-formally verified.
