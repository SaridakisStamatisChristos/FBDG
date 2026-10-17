# Research Status

## Evidence labels

- Main random-family canonical fixed-support nonlinear `u=2` lower bound `q=Ω(w)`: **PROVED** (human-checkable proof; not machine-formally verified).
- Explicit structured Fano-based family with `u=2, q=2`: **PROVED / EXECUTED**.
- State-local congestion theorem: **PROVED**.
- Extension of the main `Ω(w)` theorem to moving/state-dependent/history-dependent supports: **OPEN**.
- Headline theorem novelty: **LIKELY DISTINCT WITHIN SEARCH SCOPE**.

## Publication-readiness state

The 2026-10-17 SOTA Research Auditor pass classified the generic theory-paper package as **READY WITH MINOR FIXES**, not as a prediction of acceptance. The auditor found no fatal scientific defect in the current central theorem/construction package. This branch implements the resulting hardening actions:

1. modern dynamic cell-probe / Multiphase context added to Related Work;
2. the `w`-bit cell normalization and its `b=Θ(w)` robustness made explicit;
3. the finite validation artifact frozen with exact stdout, checksum, manifest, and CI diff checks;
4. bounded novelty language preserved.

Venue-specific page limits, anonymity, formatting, artifact policy, and submission metadata remain separate checks once a target venue is chosen.

## Final scientific frontier

1. **Structured fixed support.** Explicit infinite families have logarithmic batch size and constant recovery locality.
2. **Random fixed support.** Random logarithmic-size families require linear recovery locality under two fixed essential write locations per source coordinate, even for nonlinear cells and adaptive exact queries.
3. **Moving support.** Any hypothetical sublinear-query representation must maintain high state-local write congestion, but whether moving hubs can beat the fixed-support barrier remains open.

## Scope restrictions that must remain visible

The main theorem assumes:

- exact recovery;
- canonical memory state as a function of the logical source state;
- dynamic cell width normalized to `w` bits in the main statement;
- fixed **essential** supports `S_j` with `|S_j|≤2`;
- worst-case query probe bound `q`;
- deterministic exact queries (zero-error worst-case randomized queries reduce by fixing the tape).

The lower-bound proof is robust under any cell width `b=Θ(w)`: the diffuse branch is unchanged, while hub-capacity, residual-group, and sketch-length terms change only by constants. The manuscript keeps `b=w` as the clean normalization and does not claim the same statement for superlinear cell widths without additional analysis.

The state-local congestion theorem is broader and does not require a canonical global representation or fixed supports. Its update transition is taken to be deterministic once the memory state and source-coordinate flip are specified.

## Publication positioning

The literature audit found no materially equivalent theorem in the searched literature through October 2026. This is not an absolute priority claim. The manuscript deliberately avoids claiming that local update/local decode, support graphs, Fano coding, sketch-aided probing, batch coding, or the general Multiphase/cell-probe lower-bound framework are themselves new.

The surviving contribution is the fixed-family exact-retrieval **structure-versus-randomness locality separation** together with the state-local congestion barrier and the explicit identification of moving support geometry as the remaining frontier.
