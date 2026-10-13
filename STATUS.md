# Research Status

## Evidence labels

- Main random-family canonical fixed-support nonlinear `u=2` lower bound `q=Ω(w)`: **PROVED** (human-checkable proof; not machine-formally verified).
- Explicit structured Fano-based family with `u=2, q=2`: **PROVED / EXECUTED**.
- State-local congestion theorem: **PROVED**.
- Extension of the main `Ω(w)` theorem to moving/state-dependent/history-dependent supports: **OPEN**.
- Headline theorem novelty: **LIKELY DISTINCT WITHIN SEARCH SCOPE**.

## Final scientific frontier

1. **Structured fixed support.** Explicit infinite families have logarithmic batch size and constant recovery locality.
2. **Random fixed support.** Random logarithmic-size families require linear recovery locality under two fixed essential write locations per source coordinate, even for nonlinear cells and adaptive exact queries.
3. **Moving support.** Any hypothetical sublinear-query representation must maintain high state-local write congestion, but whether moving hubs can beat the fixed-support barrier remains open.

## Scope restrictions that must remain visible

The main theorem assumes:

- exact recovery;
- canonical memory state as a function of the logical source state;
- `w`-bit dynamic cells;
- fixed **essential** supports `S_j` with `|S_j|≤2`;
- worst-case query probe bound `q`;
- deterministic exact queries (zero-error worst-case randomized queries reduce by fixing the tape).

The state-local congestion theorem is broader and does not require a canonical global representation or fixed supports. Its update transition is taken to be deterministic once the memory state and source-coordinate flip are specified.

## Publication positioning

The final research audit found no materially equivalent theorem in the literature searched through October 2026. This is not an absolute priority claim. The manuscript deliberately avoids claiming that local update/local decode, support graphs, Fano coding, sketch-aided probing, or batch coding are themselves new.
