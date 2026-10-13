# Algorithm Foundry Research Handoff — FBDG / Binary DVESP / Structure-vs-Randomness Locality

**Date:** 2026-10-13  
**Purpose:** Full continuity handoff for a new chat.  
**Primary modes:** `@Algorithm Foundry`, optionally `@SOTA Research Auditor`.  
**Status:** The research has progressed from DVESP/Binary-DVESP into a sharper data-structure/coding-theory paper centered on **Fixed-Batch Dynamic Gather (FBDG)** and a **structure-vs-randomness locality dichotomy**.

---

# 0. NEW CHAT — START HERE

Paste this prompt in the new chat together with this handoff:

> **@Algorithm Foundry continue exactly from the attached handoff. Do not restart from DVESP or repeat refuted branches. Preserve all theorem/evidence and novelty labels exactly unless you identify a concrete defect. Primary target: adversarially audit and formalize the random-family fixed-support nonlinear `u=2` lower bound `q=Ω(w)`, then attack the remaining moving-support/history-dependent case. Treat prior-art audit findings in this handoff as binding continuity context, but verify bibliographic details before manuscript submission. Do not promote novelty beyond `LIKELY DISTINCT WITHIN SEARCH SCOPE` / `POSSIBLY_NOVEL` without a fresh focused audit.**

Recommended follow-up:

> **@SOTA Research Auditor perform a formal proof audit and prior-art equivalence audit of the fixed-support `u=2` theorem and the complete paper contribution stack.**

---

# 1. EXECUTIVE SUMMARY

The current research thesis is:

> **Dynamic fixed-batch retrieval exhibits a locality dichotomy between highly structured incidence families and sufficiently random fixed batch families.**

For suitable **structured** families, exact retrieval of a `w=Θ(log n)` batch can be achieved on an ordinary word RAM with:

\[
u=2,\qquad q=2,
\]

and even:

\[
D(w)=O(1),\qquad G(w)=O(1).
\]

For sufficiently **random** `w`-uniform families with `M=Θ(n)`, the strongest proved lower bound currently is:

\[
oxed{q=\Omega(w)}
\]

for **canonical fixed-support nonlinear `u=2` encodings with fully adaptive exact queries**.

The fully unrestricted case allowing state-dependent/moving update supports and history-dependent representations remains:

\[
oxed{	ext{OPEN}}.
\]

A more general unrestricted lower bound already proved is:

\[
oxed{q=\Omega(w/\log w)}
\]

for an explicit hard family under constant write locality.

The strongest current paper is therefore built around:

1. the FBDG formulation and Binary-DVESP transfer;
2. structured constant-locality positive constructions;
3. block-linear and nonlinear lower bounds;
4. an unrestricted baseline `Ω(w/log w)` lower bound;
5. the new **random-family fixed-support nonlinear `u=2` lower bound `Ω(w)`**;
6. state-local congestion / high-influence structure theorems;
7. the remaining open problem: removing fixed support.

---

# 2. EVIDENCE / NOVELTY LABELS

Use only these evidence labels:

- `PROVED`
- `CONDITIONAL`
- `EXECUTED`
- `REFUTED`
- `SURVIVING`
- `OPEN`

Use these novelty labels:

- `PRIOR_ART_FOUND`
- `POSSIBLY_NOVEL`
- `NOVELTY_SUPPORTED`
- `LIKELY DISTINCT WITHIN SEARCH SCOPE`
- `INCREMENTAL / COMBINATIONAL`
- `SUBSTANTIALLY OVERLAPPING`
- `UNRESOLVED`

Do **not** claim “first”, “optimal”, “state of the art”, or “solved” unless a new audit explicitly supports it.

---

# 3. ORIGINAL CHAIN — PRESERVE, DO NOT RESTART

The research evolution is:

\[
	ext{Metric closure}
ightarrow
	ext{DVESP}
ightarrow
k	ext{-state kernel}
ightarrow
	ext{OuMv frontier}
ightarrow
	ext{Binary DVESP}
ightarrow
	ext{first-event algorithm}
ightarrow
O(k^2/\log k)
ightarrow
	ext{UWRAM }O(k^2/\log^2 k)
ightarrow
	ext{adaptive first-cover}
ightarrow
	ext{FBDG}
ightarrow
	ext{linear barrier}
ightarrow
u=1	ext{ nonlinear rigidity}
ightarrow
u=2	ext{ Fano escape}
ightarrow
	ext{structure-vs-randomness locality}.
\]

The original graph theorem is no longer the main paper contribution.

---

# 4. DVESP / BINARY-DVESP CORE RESULTS

## 4.1 Exact `k`-state DVESP kernel

For volatile edges \(e_i=(a_i,b_i)\), define on the stable backbone \(H=G-F\):

\[
lpha_i=d_H(s,a_i),\qquad
eta_i=d_H(b_i,t),\qquad
C_{ij}=d_H(b_i,a_j),
\]

with volatile weight \(\lambda_i\).

The dynamic transition matrix is:

\[
W_{ij}=C_{ij}+\lambda_j.
\]

After preprocessing:

\[
U(k)=O(1),\qquad Q(k)=O(k^2).
\]

**State:** `PROVED`.

## 4.2 Generic conditional barrier

An OuMv/OMv-style reduction inside the special form \(W_{ij}=C_{ij}+\lambda_j\) yields:

\[
kU(k)+Q(k)\ge k^{2-o(1)}.
\]

Thus generic polynomially sublinear updates plus polynomially subquadratic queries are conditionally ruled out.

**State:** `CONDITIONAL`.

## 4.3 Binary DVESP

For:

\[
C_{ij}\in\{0,1\},
\]

the one-`1`-edge lemma and first-event characterization give:

\[
Q(k)=O(k^2/\log k+k\log k),\qquad U(k)=O(1).
\]

On UWRAM:

\[
Q(k)=O(k^2/\log^2 k+k\log k).
\]

The missing ordinary-RAM logarithm motivated FBDG.

**State:** `PROVED` for the standard-RAM algorithm and correctness mechanism; UWRAM asymptotic reasoned from the model primitive.

---

# 5. FBDG DEFINITION

Preprocess a fixed polynomial-size family:

\[
B_1,\ldots,B_M\subseteq[n],
\]

typically:

\[
M=\Theta(n),\qquad |B_i|=w,\qquad w=\Theta(\log n).
\]

Maintain:

\[
x\in\{0,1\}^n
\]

under point updates.

A query for \(B_i\) must return:

\[
x|_{B_i}.
\]

Parameters:

- \(u\): update/write locality;
- \(q\): number of dynamic memory words probed;
- \(D(w)\): actual update time;
- \(G(w)\): actual gather/query time.

Encodings may be nonlinear and queries adaptive unless a theorem explicitly adds restrictions.

---

# 6. BINARY-DVESP ↔ FBDG TRANSFER

If FBDG has gather time \(G(w)\) and point-update time \(D(w)\), then:

\[
oxed{
Q(k)=
O\!\left(
\left(k+rac{k^2}{w^2}ight)G(w)
+kD(w)+k\log k
ight).
}
\]

For \(w=\Theta(\log k)\):

- \(G(w)=\Theta(w)\) gives \(O(k^2/\log k)\);
- \(G(w)=O(1)\) would give \(O(k^2/\log^2 k)\).

Every FBDG result must be translated back through this equation.

---

# 7. EARLIER FBDG LOWER BOUNDS

## 7.1 Block-linear lower bound

For suitable random `w`-uniform families:

\[
q+2u\ge w-O(\log w).
\]

Thus constant update locality implies:

\[
q\ge w-O(\log w).
\]

**State:** `PROVED IN BLOCK-LINEAR MODEL`.

Broad sparse-factorization language has prior art; the exact sparse FBDG bound remains a candidate distinct result.

## 7.2 Canonical nonlinear `u=1`

\[
u=1\Longrightarrow q\ge w.
\]

**State:** `PROVED`.

## 7.3 Unrestricted `q=1`

\[
q=1\Longrightarrow
u\ge\max_j d_j.
\]

For suitable random families:

\[
q=1\Longrightarrow u=\Omega(w).
\]

**State:** `PROVED`.

---

# 8. FANO `u=2,q=2` AND THE PHASE TRANSITION

The universal statement:

\[
u=2\Rightarrow q\ge w
\]

is false.

For the 7 Fano-plane triples:

\[
n=7,\qquad w=3,
\]

there is a linear encoding into three 3-bit words with:

\[
u=2,\qquad q=2.
\]

All:

\[
2^7	imes 7=896
\]

state/query cases were exhaustively validated.

**State:** `PROVED / EXECUTED`.

This establishes a real phase transition between `u=1` and `u=2`.

---

# 9. ALGEBRAIC NORMAL FORM AND ASYMPTOTIC STRUCTURED FAMILY

For independent \(t\)-bit blocks:

\[
U_0,U_1,U_2,L_1,L_2,R_1,R_2,
\]

store:

\[
C_0=(U_0,L_1,L_2),
\]

\[
C_1=(U_1,R_1,R_2),
\]

\[
C_2=(U_2,L_1\oplus R_1,L_2\oplus R_2).
\]

Changing \(U_0,U_1,U_2\) changes one word; changing \(L_i,R_i\) changes two.

Therefore:

\[
u\le2.
\]

Set:

\[
W=3t.
\]

One gadget has:

\[
n_g=7t,\qquad M_g=7t.
\]

Each query reads exactly two \(W\)-bit words and reconstructs the requested batch with constant word operations.

Thus:

\[
u=2,\qquad q=2,\qquad D(W)=G(W)=O(1).
\]

Using \(g=2^t\) disjoint gadgets gives:

\[
n=7t2^t,\qquad M=n,\qquad W=\Theta(\log n).
\]

Hence:

\[
oxed{u=2,\qquad q=2=o(W)}
\]

for an infinite structured family.

**State:** `PROVED / EXECUTED`.

### Framing

This is the **structured side of the dichotomy**. The auditor found strong neighboring Fano/finite-geometry/arbitrary-access-set prior art, so do not make the Fano mechanism itself the headline novelty claim.

---

# 10. UNRESTRICTED BASELINE LOWER BOUND

A reduction from existential Marked Ancestor gives an explicit FBDG hard family:

\[
M=\Theta(n),\qquad w=\Theta(\log n),
\]

with:

\[
oxed{
q=
\Omega\!\left(
rac{\log n}
{\log(uw\log n)}
ight).
}
\]

For constant \(u\):

\[
oxed{q=\Omega(w/\log w)}.
\]

This permits nonlinear encodings, adaptive queries, free update-side reads, state/history-dependent update locations, and polynomial space.

**State:** `PROVED`.

Treat as baseline inherited dynamic hardness, not the headline novelty theorem.

---

# 11. STATE-LOCAL HITTING AND CONGESTION

At reachable state \(\sigma\), let:

\[
U_j(\sigma)
\]

be the cells modified by flipping logical coordinate \(j\), and let:

\[
P_B(\sigma)
\]

be the adaptive probe path for batch \(B\).

For every \(j\in B\):

\[
oxed{
P_B(\sigma)\cap U_j(\sigma)
eqarnothing.
}
\]

**State:** `PROVED`.

Define:

\[
d_c(\sigma)=|\{j:c\in U_j(\sigma)\}|,
\qquad
f(\sigma)=\max_c d_c(\sigma).
\]

Define pair-repetition excess:

\[
ho(\mathcal B)=
\sum_{\{a,b\}}
(\deg_{\mathcal B}(a,b)-1)_+.
\]

Then:

\[
oxed{
M\left(rac{w^2}{q}-wight)
\le
un(f(\sigma)-1)+2ho(\mathcal B).
}
\]

For random `w`-uniform families with `M=n`:

\[
q\ge
rac{w^2}
{w+u(f(\sigma)-1)+o(1)}.
\]

Equivalently:

\[
f(\sigma)\ge
1+rac{w^2/q-w-o(1)}{u}.
\]

Therefore:

\[
q=o(w)\Longrightarrow f(\sigma)=\omega(w)
\]

at every reachable state.

**State:** `PROVED`.

Exact inequality: `POSSIBLY_NOVEL / LIKELY DISTINCT WITHIN SEARCH SCOPE`. Broader influence/congestion ideas have prior art.

---

# 12. BOUNDED-CONGESTION AND HUB-FIBER BARRIERS

If:

\[
f(\sigma)=O(w)
\]

for every reachable state and \(u=O(1)\), random FBDG forces:

\[
oxed{q=\Omega(w)}.
\]

**State:** `PROVED`.

A further restricted theorem handles:

- a small collection of arbitrary/global hub words;
- residual words depending on bounded-size source groups.

A representative bound is:

\[
q\ge
rac{\delta(n-hw)}
{M\min(D,w)}
\]

for a \(\delta\)-regular family after conditioning on \(h\) hub words and with residual dependency size \(D\).

For:

\[
M=n,\quad \deltasymp w,\quad h=o(n/w),\quad D=O(1),
\]

this gives:

\[
q=\Omega(w).
\]

**State:** `PROVED` in the stated canonical/hub-fiber model.

These results show that any unrestricted sublinear-query counterexample must use **moving high-congestion hubs**.

---

# 13. MAIN CURRENT THEOREM — RANDOM FAMILY, CANONICAL FIXED-SUPPORT `u=2`

Let:

\[
w=\Theta(\log n),\qquad M=\Theta(n),
\]

and choose the \(M\) batches independently as random \(w\)-subsets of \([n]\).

Consider an exact **canonical** FBDG representation in \(w\)-bit cells with **fixed update supports**:

\[
S_j,\qquad |S_j|\le2,
\]

meaning each logical coordinate \(j\) may modify only the same at-most-two physical cells in every state.

Cell contents may be arbitrary nonlinear functions, and queries may be fully adaptive.

Then, with high probability over the random batch family:

\[
oxed{q=\Omega(w)}.
\]

**State:** `PROVED` in the research session.

**Critical restriction:** `fixed support`.

This theorem does **not** cover state-dependent/moving supports.

---

# 14. MAIN THEOREM — PROOF SKELETON

## 14.1 Support graph

Build a graph:

- vertex = dynamic memory cell;
- logical coordinate \(j\) = edge joining its at-most-two fixed support cells.

The hitting lemma implies that every actual probe set is a vertex cover of the queried support edges.

The proof splits into two cases.

## 14.2 Diffuse case

If no small vertex set is incident to more than a small constant fraction of logical coordinates, a random `w`-edge batch contains a matching of size \(\Omega(w)\) with exponentially high probability.

A union bound over all relevant fixed-support graphs gives a batch with:

\[

u(B)=\Omega(w).
\]

Every vertex cover of that batch therefore has size \(\Omega(w)\), forcing:

\[
q=\Omega(w).
\]

## 14.3 Hub-concentrated case

Otherwise a set:

\[
H,\qquad |H|=h=O(w),
\]

of memory cells touches a constant fraction of logical coordinates.

Give the hub contents to the decoder for free as an `hw`-bit sketch.

Coordinates supported entirely inside \(H\) are information-limited to:

\[
O(hw)=O(w^2)=o(n).
\]

Thus a constant fraction still have one endpoint in \(H\) and one endpoint outside.

For each nonhub cell \(v\), define a residual source group \(G_v\).

Canonical injectivity implies:

\[
|G_v|\le(h+1)w=O(w^2).
\]

## 14.4 Random-family spreading lemma

Uniformly over all small \(S\) of size at most \(O(w^2)\):

\[
oxed{
\sum_i(|B_i\cap S|-1)_+
\le K|S|
}
\]

with high probability.

Random batches therefore do not repeatedly cluster inside the same residual source groups.

## 14.5 Query-with-Sketch reduction

Select \(L=\Theta(h)\) batches with sufficiently separated residual groups.

Concatenate their requested surviving bits into \(F(X)\).

The hub cells provide an `s=hw`-bit sketch.

Strengthen any residual encoded-cell probe by revealing the entire raw source group \(X_{G_v}\). This can only help the decoder.

A Query-with-Sketch min-entropy theorem permitting adaptive decision trees then forces:

\[
\Omega(Lw)
\]

total residual group probes across the selected queries.

The original FBDG algorithm would use at most:

\[
Lq.
\]

Therefore:

\[
Lq=\Omega(Lw),
\]

so:

\[
oxed{q=\Omega(w)}.
\]

---

# 15. PROOF-INTEGRITY WARNING

The main fixed-support theorem is the strongest paper result, but it has **not yet received the full independent adversarial proof audit required before submission**.

Highest-risk obligations:

1. exact counting/union bound in the diffuse case;
2. number of relevant support graphs;
3. spreading lemma uniformly over all small \(S\);
4. selection of the required \(L=\Theta(h)\) batches;
5. exact assumptions of Query-with-Sketch;
6. validity of raw-group revelation as a strengthening;
7. conditional min-entropy after hub conditioning;
8. exact use of canonicality;
9. no silent transition from fixed support to state-dependent support;
10. constants in the `w=C log n` regime.

Before submission run:

> **@SOTA Research Auditor formal theorem audit of the random-family fixed-support nonlinear `u=2` lower bound.**

---

# 16. CENTRAL OPEN PROBLEM — MOVING SUPPORTS

Can one prove:

\[
q=\Omega(w)
\]

for random/expanding `w`-uniform families with:

\[
M=\Theta(n),\qquad w=\Theta(\log n),\qquad u=2
\]

when update locations may depend on the state/history?

The congestion theorem implies that any hypothetical:

\[
q=o(w)
\]

counterexample must maintain:

\[
f(\sigma)=\Omega(w^2/q)
\]

at every reachable state.

At:

\[
q=\Theta(w/\log w),
\]

this requires:

\[
f(\sigma)=\Omega(w\log w).
\]

The remaining problem is therefore specifically the power of **moving high-influence write hubs**.

A likely route is:

1. model the canonical state-dependent `u=2` encoding as an edge-labeling of the Boolean cube;
2. exploit square/commutation consistency;
3. prove that a large subcube stabilizes many update supports;
4. restrict to that subcube;
5. apply the fixed-support theorem.

If false, search for the smallest twisting/moving-support counterexample.

---

# 17. DEAD / REFUTED BRANCHES

Do not revisit without a concrete defect:

1. original metric-closure novelty;
2. DVESP as broadly novel;
3. smooth generic polynomial update/query tradeoff;
4. MIW as a novel parameter;
5. generic Monge novelty;
6. naive Four-Russians;
7. ordinary BMV/minimum-witness direct transfer;
8. eager transposed packed layouts;
9. full `w^2`-state tabulation;
10. generic dynamic set intersection as automatic constant gather;
11. linear coding as route to `G(w)=O(1)` for hard families;
12. canonical nonlinear `u=1` constructions;
13. fixed-support rigidity generalized directly from `u=1` to `u=2`;
14. universal `u=2 ⇒ q≥w`;
15. direct use of Multiphase lower bounds without preserving `w=Θ(log n)` batch size;
16. literal Ko-2026 Disjointness hard-distribution transplantation;
17. “one coordinate per epoch” as enough for `Ω(w)` — it naturally tops out at `Ω(w/log w)`;
18. naive Larsen-style independent cell sampling relying only on sparse vector-output entropy.

---

# 18. PAPER THESIS

Strongest defensible thesis:

> **Fixed-batch dynamic retrieval admits a structure-versus-randomness locality separation under two fixed write locations per source coordinate: highly structured families can support constant-time exact recovery, while random `Θ(log n)`-uniform families require linear recovery locality even with arbitrary nonlinear storage and adaptive decoding.**

---

# 19. SUGGESTED TITLES

Best current title:

**Dynamic Fixed-Batch Retrieval: Structured Codes and Random-Family Locality Barriers**

Alternatives:

- **Update–Recovery Locality in Fixed-Batch Dynamic Retrieval**
- **Structure versus Randomness in Dynamic Fixed-Batch Retrieval**

Avoid putting DVESP in the title unless the graph application becomes a larger part of the final manuscript.

---

# 20. PROPOSED PAPER STRUCTURE

1. **Introduction**
   - FBDG motivation;
   - ordinary-RAM gather bottleneck;
   - structured vs random separation;
   - Binary-DVESP as application.

2. **Model and notation**
   - FBDG;
   - word size;
   - update/write locality;
   - adaptive probes;
   - canonicality;
   - fixed vs moving support;
   - exact packed-vector recovery.

3. **Binary-DVESP connection**
   - enough background to derive the transfer theorem;
   - no generic DVESP novelty claims.

4. **Block-linear barrier**
   \[
   q+2u\ge w-O(\log w).
   \]

5. **Nonlinear `u=1` rigidity**
   \[
   u=1\Rightarrow q\ge w.
   \]

6. **Structured `u=2` constructions**
   - Fano example;
   - normal form;
   - asymptotic structured family with:
   \[
   u=2,\ q=2,\ G(w)=D(w)=O(1).
   \]

7. **Unrestricted baseline hardness**
   \[
   q=\Omega(w/\log w).
   \]

8. **State-local congestion**
   - congestion inequality;
   - bounded-congestion `Ω(w)` corollary.

9. **Main theorem**
   - random fixed-support nonlinear `u=2`;
   - diffuse/hub dichotomy;
   - spreading lemma;
   - Query-with-Sketch reduction.

10. **Consequences for Binary DVESP**

11. **Related work**

12. **Open problems**
   - remove fixed support;
   - general constant `u`;
   - characterize exact easy/hard incidence property;
   - determine whether Binary-DVESP microblock families are hard.

---

# 21. SOTA RESEARCH AUDITOR — PRIOR-ART FINDINGS

## 21.1 Overall verdict

The auditor performed a mechanism-level search.

For the strongest theorem:

> random fixed-batch retrieval + canonical fixed-support nonlinear `u=2` + adaptive exact recovery ⇒ `q=Ω(w)`

the auditor found **no materially equivalent prior theorem** in the searched literature.

Current novelty classification:

\[
oxed{	exttt{LIKELY DISTINCT WITHIN SEARCH SCOPE}}
\]

—not “first” or absolute novelty.

---

# 22. SPECIFIC PRIOR-ART FINDINGS

## 22.1 Sparse-factorization prior art

The audit found a June 2026 public preliminary note by **Luca Blanchi**, *Local Linear Presentations and Sparse Factorization Complexity*.

It characterizes dynamic exact linear representations through:

\[
A=RM,
\]

where row sparsity corresponds to query locality and column sparsity to update locality.

### Implication

Do **not** claim the general sparse-factorization interpretation as new.

The auditor did **not** find the exact sparse FBDG theorem:

\[
q+2u\ge w-O(\log w)
\]

there.

Status:

- broad factorization characterization: `PRIOR_ART_FOUND`;
- exact sparse FBDG lower bound: `LIKELY DISTINCT WITHIN SEARCH SCOPE`.

Bibliographic metadata should be re-verified before submission.

---

## 22.2 Locally updatable / locally decodable codes

Prior work explicitly studies simultaneous local reads and writes, including Chandran–Kanukurthi–Ostrovsky and later local-update/local-decode coding/compression work.

### Implication

Do not claim:

> “We introduce simultaneous local decoding and local updating.”

Instead:

> “We study exact dynamic recovery of a fixed family of multi-coordinate batches under bounded write locality.”

---

## 22.3 Vatedka–Chandar–Tchamkerten

This work is especially relevant because it studies local decoding and updating with assumptions involving:

- bounded influence;
- restrictions on update-history dependence.

They identify removal of such restrictions as difficult/open territory.

### Implication

Do not claim:

> “history dependence/high influence is the hard part”

as a new observation.

What may be new is the sharper FBDG theorem in the random fixed-support regime.

---

## 22.4 Fano / arbitrary-access-set codes

The audit found close Fano-plane prior art in **Maturana and Rashmi (2021)** on irregular array codes with arbitrary access sets.

The orientation differs:

- their Fano sets are storage-node access sets recovering a whole message;
- our Fano sets are requested source-coordinate batches recovered from encoded words.

### Implication

Treat Fano as:

- an illustrative structured counterexample;
- a positive witness for the dichotomy.

Do **not** present Fano coding itself as headline novelty.

---

## 22.5 Replication-2 graph batch codes

The graph interpretation:

- source coordinate/item = edge;
- two storage/update locations = endpoints;

has clear batch-code prior art.

### Implication

Do not claim the support-graph representation itself as new.

The candidate contribution is the **random-family nonlinear adaptive lower bound built on top of that model**.

---

## 22.6 Query-with-Sketch

Query-with-Sketch is prior-art methodology for:

- arbitrary global sketches;
- adaptive queries;
- conditional min-entropy.

### Implication

It is a proof ingredient, not the paper novelty.

The novel candidate is the reduction of the FBDG hub case into a form where that machinery can apply.

This step needs the strongest proof audit.

---

## 22.7 Marked Ancestor

The unrestricted:

\[
\Omega(w/\log w)
\]

baseline inherits its scale from classical Marked Ancestor lower bounds.

### Implication

Treat it as:

- a useful reduction;
- baseline hardness;
- not the main theorem.

---

## 22.8 Modern Multiphase lower bounds

Recent Multiphase/Disjointness lower bounds are stronger in other regimes but do not preserve:

\[
|B|=\Theta(\log n)
\]

exact vector-return FBDG structure.

They are neighboring machinery, not direct collisions.

---

# 23. AUDITOR NOVELTY MAP

| Contribution | Auditor status |
|---|---|
| FBDG terminology/formalization | `INCREMENTAL / COMBINATIONAL` |
| Binary-DVESP → FBDG application bridge | useful, not headline novelty |
| sparse-factorization viewpoint | `PRIOR_ART_FOUND` broadly |
| exact block-linear sparse-family bound | `LIKELY DISTINCT WITHIN SEARCH SCOPE` |
| canonical nonlinear `u=1` theorem | `LIKELY DISTINCT WITHIN SEARCH SCOPE` |
| Fano structured mechanism | `SUBSTANTIALLY OVERLAPPING NEIGHBORHOOD` |
| asymptotic structured FBDG family | candidate contribution, close coding prior art |
| unrestricted `Ω(w/log w)` | derived/combinational baseline |
| state-local congestion inequality | `LIKELY DISTINCT WITHIN SEARCH SCOPE` |
| bounded-congestion `Ω(w)` | `LIKELY DISTINCT WITHIN SEARCH SCOPE` |
| **random fixed-support nonlinear `u=2 ⇒ q=Ω(w)`** | **`LIKELY DISTINCT WITHIN SEARCH SCOPE` — strongest candidate** |
| moving/history-dependent support theorem | `OPEN` |
| overall paper novelty | **SURVIVES** |

---

# 24. CLAIMS TO AVOID

Do **not** claim:

1. FBDG is the first dynamic retrieval model of this type.
2. Simultaneous local update and local decode is new.
3. Sparse factorization of dynamic linear representations is new.
4. Fano-plane coding is new.
5. The graph representation of `u=2` fixed supports is new.
6. The hitting/set-cover principle is new.
7. The `Ω(w/log w)` scale is new in dynamic data structures.
8. Existing Multiphase lower bounds directly solve FBDG.
9. The fixed-support theorem already handles moving/state-dependent supports.
10. The Binary-DVESP standard-RAM `O(k^2/log^2 k)` question is resolved in full generality.

---

# 25. STRONGEST DEFENSIBLE NOVELTY WORDING

Use wording like:

> **Within the literature searched as of October 2026, we did not identify a materially equivalent lower bound for exact fixed-batch dynamic retrieval showing that random `Θ(log n)`-uniform batch families require `Ω(log n)` adaptive word probes under two fixed update locations per source coordinate, even with arbitrary nonlinear cell contents.**

Immediately state:

> **The result applies to canonical fixed-support encodings; removing fixed support remains open.**

Do not say “first” without a final exact-equivalence audit.

---

# 26. PUBLICATION READINESS

The project is already strong enough to justify drafting.

Approximate planning status:

- **solid publishable theory paper:** `80–90%` conceptually;
- **strong theory-conference submission:** `65–75%`, pending proof cleanup and final novelty audit.

These are planning estimates, not acceptance probabilities.

Recommendation:

\[
oxed{	ext{BEGIN WRITING THE PAPER NOW}}
\]

while attacking moving supports in parallel.

Do not require the unrestricted theorem before drafting.

---

# 27. CURRENT MAIN RISK

Prior art is no longer the main risk.

The main risk is:

\[
oxed{	ext{proof integrity of the fixed-support }u=2	ext{ theorem}}
\]

especially the hub-concentrated case and Query-with-Sketch reduction.

Before submission:

1. rewrite every lemma formally;
2. build the theorem dependency DAG;
3. search for smallest counterexamples;
4. verify every probability/union-bound constant;
5. verify exact assumptions of imported theorems;
6. separate canonicality from fixed-support assumptions;
7. ensure no step silently assumes nonadaptivity;
8. ensure random-family events hold uniformly over encodings/support graphs;
9. rerun prior-art search against the final exact statement.

---

# 28. PRIORITY NEXT STEPS

## Priority 1 — Formal proof audit

Use:

> **@SOTA Research Auditor formal theorem audit of the random-family fixed-support nonlinear `u=2` lower bound. Build a lemma dependency graph, verify every random-family union bound, verify the hub/diffuse dichotomy, verify the Query-with-Sketch reduction and imported assumptions, and actively search for counterexamples. Do not soften defects.**

## Priority 2 — Paper-ready theorem normalization

Use:

> **@Algorithm Foundry rewrite the theorem and proof in paper-ready form with exact assumptions, theorem numbering, lemma dependency graph, and no informal gaps.**

## Priority 3 — Reproducibility archive

Preserve:

- Fano exhaustive `896/896`;
- earlier Binary-DVESP/microblock tests;
- asymptotic structured-family dynamic differential tests;
- random pair-codegree/congestion experiments;
- `PG(2,3)` negative search;
- any spreading/support-graph counterexample-search scripts.

## Priority 4 — Final prior-art equivalence audit

Search exact theorem shape across:

- batch codes;
- graph batch codes;
- functional batch codes;
- arbitrary access set codes;
- locally updatable/decodable codes;
- locally decodable source coding;
- nonlinear index coding;
- Query-with-Sketch;
- sparse factorization/presentation complexity;
- write-probe models;
- dynamic cell-probe lower bounds.

## Priority 5 — Attack moving supports

After the fixed-support theorem is stable.

---

# 29. PAPER-LEVEL RESULT HIERARCHY

## Headline

\[
oxed{
	ext{Random fixed-support nonlinear }u=2
\Longrightarrow
q=\Omega(w)
}
\]

for:

\[
w=\Theta(\log n),\qquad M=\Theta(n).
\]

## Positive counterpart

\[
oxed{
	ext{Structured families admit }u=2,\ q=2.
}
\]

## Supporting bounds

\[
q+2u\ge w-O(\log w)
\]

in the block-linear model;

\[
u=1\Rightarrow q\ge w
\]

for canonical nonlinear encodings;

\[
q=\Omega(w/\log w)
\]

for unrestricted constant-write hard families.

## Structural explanation

\[
M\left(rac{w^2}{q}-wight)
\le
un(f-1)+2ho.
\]

Thus sublinear query locality in the unrestricted model requires state-by-state high-influence hubs.

---

# 30. EXACT IMPLICATION BACK TO BINARY DVESP

For structured FBDG families with:

\[
G(w)=D(w)=O(1)
\]

and \(w=\Theta(\log k)\):

\[
Q(k)=
O\left(
rac{k^2}{\log^2 k}
+k\log k
ight)
\]

on an ordinary word RAM.

For hard random FBDG families in the fixed-support `u=2` model:

\[
G(w)=\Omega(w),
\]

so the current transfer route cannot beat the:

\[
\Omega(k^2/\log k)
\]

gather scale.

### Critical caveat

This is **not yet** an unrestricted Binary-DVESP lower bound.

One must prove that Binary-DVESP microblock-generated FBDG families satisfy the needed hardness conditions, or derive a direct lower bound.

---

# 31. CENTRAL OPEN PROBLEMS

1. Remove fixed support from the random-family `u=2` theorem.
2. Generalize from `u=2` to all constant `u`.
3. Identify the exact incidence parameter separating easy structured families from hard random families.
4. Determine whether any moving-support construction achieves:
   \[
   q=o(w).
   \]
5. Determine whether Binary-DVESP microblock batches inherit the hard-family barrier.
6. Tighten novelty of the exact sparse linear bound and congestion theorem.
7. Decide whether the structured asymptotic construction is independently publishable or should remain an illustrative half of the dichotomy.

---

# 32. MOST IMPORTANT CONTINUITY RULE

Do **not** let a new chat collapse:

\[
	ext{fixed-support theorem}
\]

into:

\[
	ext{unrestricted theorem}.
\]

The exact frontier is:

\[
oxed{
egin{array}{ll}
	ext{structured fixed-support }u=2 &: q=O(1),\[4pt]
	ext{random fixed-support }u=2 &: q=\Omega(w),\[4pt]
	ext{unrestricted moving-support }u=2 &: q=\Omega(w/\log w)	ext{ known, }\Omega(w)	ext{ OPEN}.
\end{array}
}
\]

That distinction is the central scientific boundary of the project.

---

# 33. RECOMMENDED FIRST THREE TASKS IN THE NEW CHAT

### Task 1

> **@SOTA Research Auditor formally audit the proof of the random-family canonical fixed-support nonlinear `u=2` lower bound `q=Ω(w)`. Check every lemma, constant, union bound, entropy argument, and use of Query-with-Sketch. Search aggressively for the smallest counterexample.**

### Task 2

If it survives:

> **@Algorithm Foundry rewrite the theorem and proof in paper-ready form with exact assumptions, theorem numbering, lemma dependency graph, and no informal gaps.**

### Task 3

Then:

> **@SOTA Research Auditor perform a final exact-equivalence prior-art audit against batch codes, locally updatable/locally decodable codes, arbitrary-access-set codes, nonlinear index coding, Query-with-Sketch, sparse factorization, write-probe models, and dynamic cell-probe lower bounds.**

Only then should the theorem be promoted beyond `LIKELY DISTINCT WITHIN SEARCH SCOPE`.

---

# 34. FINAL STATE

The project is plausibly paper-worthy **without** solving the moving-support case.

The strongest current scientific story is:

> A fixed family of sparse dynamic retrieval demands can be dramatically easy or provably hard depending on incidence structure. Two fixed writes per source bit are enough for constant-time recovery on carefully structured families, yet random `Θ(log n)`-uniform families require `Ω(log n)` adaptive word probes even with nonlinear storage. The only known route around this barrier is to let write supports move with the state/history, and the state-local congestion theorem shows that any such escape must continually maintain high-influence write hubs.

That is the correct research state to continue from.

---

**End of handoff.**
