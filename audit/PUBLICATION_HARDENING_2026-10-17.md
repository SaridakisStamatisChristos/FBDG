# FBDG Publication Hardening Audit — 2026-10-17

## Decision

**Workflow state:** `READY WITH MINOR FIXES` for a generic theoretical-CS submission package. This is not an acceptance prediction and does not replace venue-specific compliance checks.

The central scientific claims remain deliberately bounded:

- explicit structured canonical fixed-support families achieve `u=2, q=2` with `w=Theta(log n)`;
- random `Theta(log n)`-uniform families require `q=Omega(w)` for exact canonical encodings with at most two fixed essential update locations per source coordinate, arbitrary nonlinear cell contents, and fully adaptive exact queries;
- the full `Omega(w)` result for moving/state-dependent/history-dependent update supports remains **OPEN**;
- the state-local congestion theorem survives without the global fixed-support assumption and characterizes the high-influence hubs required by any sublinear-query escape.

## Auditor findings implemented

1. **Dynamic lower-bound context.** Related Work now places FBDG next to the Multiphase and modern dynamic cell-probe lower-bound lineage and states why those results are complementary rather than direct collisions.
2. **Cell-width normalization.** Section 2.1 now explains why the main model uses `w`-bit cells and records the constant-factor robustness of the proof for cell width `b=Theta(w)` without extending the formal claim to superlinear cells.
3. **Reproducibility freeze.** The finite structured-construction validator now has a retained expected-output file, SHA-256 checksum, machine-readable manifest, and CI byte-for-byte output gate.
4. **Claim boundary.** The manuscript continues to avoid absolute “first”, “optimal”, and “state of the art” language; moving support remains explicitly open.

## Targeted adversarial proof pass

The final hardening pass rechecked the proof locations most likely to affect Theorem 5.1.

### Uniform small-set spreading (Lemma 7.4)

Checked:

- the extraction of exactly `t` excess incidences when `Z(S) >= t`;
- the containment probability for a specified `k`-subset under uniform sampling without replacement;
- summation over selected batches and compositions;
- the worst case over the number of contributing batches;
- the union bound over all sets with size `O(w^2)`.

No contradiction was found. With `w=Theta(log n)` and fixed `K>=3`, the resulting bound remains summable over all `s<=O(log^2 n)`.

### Uniform diffuse matching (Lemma 7.5)

Checked:

- at most `2n` physical cells can occur in the union of essential supports;
- the resulting support-system count is `exp(2n log n + O(n))`;
- conditional rejection probability in the greedy exposure is bounded by the diffuse incidence condition;
- independent random batches provide the `exp(-Theta(n log n))` amplification required to union-bound over all support systems.

No defect was found in the quantifier order: the random family is fixed first and, with high probability, is hard simultaneously for every eligible fixed support system.

### Hub branch and group-disjoint selection

Checked:

- inactive coordinates are removed before injectivity/capacity counting;
- hub-internal active coordinates are bounded by the information capacity of the hub cells;
- crossing coordinates partition into residual groups because each crossing essential support has one hub and one nonhub endpoint;
- each residual group has size `O(w^2)`;
- uniform spreading controls total collision excess across the residual partition;
- the source-degree bound and residual-group-size bound imply a greedy conflict bound allowing `L=Theta(h)` pairwise group-disjoint batches because `O(w^5)=o(n)`.

No defect was found.

### Adaptive sketch-probe reduction (Lemma 8.1 and Section 9.2)

Checked specifically against the common invalid step of conditioning on an informative sketch and then assuming the remaining target entropy is unchanged. The proof does **not** make that step. It bounds short correct leaves in each sketch-indexed decision tree using the underlying product distribution and pays explicitly for all `2^s` sketch values.

For the FBDG reduction:

- selected target bits lie in distinct residual groups and are independent under the hard product distribution;
- revealing an entire raw residual group only strengthens a nonhub cell probe;
- hub cells are safely given for free as an arbitrary `hw`-bit sketch;
- sequentially simulating the selected queries costs at most `Lq` raw-group probes, while Lemma 8.1 forces `Omega(Lw)` average probes;
- the explicit choice `L=ceil(4h/kappa)` prevents the hub sketch from absorbing the target and yields `q=Omega(w)`.

No fatal proof gap or counterexample was found in this targeted pass. The theorem remains **human-checkable, not machine-formally verified**.

## Remaining submission tasks

These are packaging/venue tasks rather than new scientific blockers:

- choose the target venue and apply its current anonymity, format, page-limit, conflict, and artifact rules;
- regenerate committed manuscript exports from the canonical Markdown source before an archival tag/release;
- perform a final bibliography/reference-render check under the selected venue style.

The moving-support problem should remain future work; it is not required to make the present fixed-support structure-versus-randomness separation a coherent paper.
