# FBDG Paper State v0.1 — 2026-10-13

## Paper frame

**Title:** Dynamic Fixed-Batch Retrieval: Structured Codes and Random-Family Locality Barriers  
**Type:** theoretical computer science / data structures / coding locality  
**Central theorem state:** `PROVED`  
**Central novelty state:** `LIKELY DISTINCT WITHIN SEARCH SCOPE`  
**Moving-support theorem:** `OPEN`

## Contribution preflight

| Contribution | Closest prior-art neighborhood | Preflight status | Safe framing |
|---|---|---|---|
| FBDG formalization | batch codes; local update/decode | `OVERLAP / INCREMENTAL` | useful formulation, not first-of-kind |
| support graph for fixed `u=2` | 2-replication graph batch codes | `OVERLAP` | proof representation, not novelty |
| Fano positive witness | finite geometry / arbitrary-access-set coding | `OVERLAP` | illustrative structured witness |
| asymptotic structured `u=2,q=2` FBDG family | nearby coding constructions | `SURVIVES` but bounded | positive side of the FBDG separation |
| sparse factorization viewpoint | Blanchi 2026 preliminary note + broader folklore | `OVERLAP` broadly | do not claim general viewpoint as new |
| exact block-linear FBDG lower bound | no exact collision found in prior audit | `SURVIVES` within scope | supporting theorem |
| state-local congestion inequality | influence/congestion neighborhood | `SURVIVES` within scope | supporting structural theorem |
| random fixed-support nonlinear `u=2 => q=Omega(w)` | no materially equivalent theorem found | **`SURVIVES`** | headline theorem |
| moving-support `Omega(w)` | unresolved | `UNRESOLVED` | open problem only |

## Mathematical closure completed in this session

The main theorem now has a self-contained proof package with:

1. essential fixed-support definition;
2. cell-local dependence;
3. active-coordinate injectivity;
4. adaptive hitting;
5. almost-all-active random-family event;
6. uniform source-degree event;
7. uniform large-set richness;
8. uniform small-set spreading;
9. uniform diffuse matching after union bound over all fixed support systems;
10. hub internal-capacity bound;
11. residual-group size bound;
12. corrected group-disjoint batch-selection lemma;
13. a self-contained independent-target sketch-probe decision-tree lemma;
14. explicit choice `L = ceil(4h/kappa)`;
15. final diffuse/hub proof of `q = Omega(w)`.

The main proof no longer depends on importing the full Query-with-Sketch min-entropy theorem, although that work remains important related methodology.

## Reviewer #2 findings

### Major 1 — structured-family appendix incomplete
The draft states the asymptotic structured construction and its algebraic normal form, but the exact batch-incidence list and archived dynamic differential-test evidence are not present in the current handoff.

**Repair:** import the exact structured-family definition and its existing validation artifact before submission.

### Major 2 — secondary theorem proofs not yet embedded
The draft states the block-linear bound, canonical nonlinear `u=1` theorem, unrestricted `Omega(w/log w)` baseline, and state-local congestion inequality, but the current source packet contains only theorem summaries rather than their complete derivations.

**Repair:** import the archived full proofs into appendices or narrow the submission to the structured-vs-random theorem pair.

### Major 3 — final exact-equivalence novelty audit still required
The prior-art audit supports `LIKELY DISTINCT WITHIN SEARCH SCOPE`, but publication metadata should not claim absolute novelty.

**Repair:** run a final theorem-shape equivalence search after the statement is frozen.

### Moderate 1 — canonicality deserves front-page emphasis
The cell-local dependence lemma uses history independence critically.

**Repair:** keep “canonical fixed-support” in the theorem statement, abstract limitation sentence, introduction, and conclusion.

### Moderate 2 — fixed-support versus moving-support distinction must remain visually explicit
Readers may otherwise overread the theorem as an unrestricted dynamic cell-probe lower bound.

**Repair:** retain the three-line frontier table and the dedicated limitations section.

### Moderate 3 — reproducibility archive should be bundled
The Fano `896/896` validation and structured-family tests are evidence-bearing artifacts.

**Repair:** package scripts, seeds/configuration, expected outputs, and a short manifest.

## Quality-gate status

| Gate | Status |
|---|---|
| Problem | PASS |
| Evidence inventory | PASS-CONDITIONAL |
| Literature | PASS-CONDITIONAL |
| Contribution preflight | PASS |
| Main theorem correctness | PASS |
| Claim/evidence alignment | PASS for main theorem; conditional for secondary theorems |
| Citation integrity | PASS for references currently used; final reconciliation pending |
| Limitations | PASS |
| Reviewer gate | PASS-CONDITIONAL |
| Contribution stress test | preliminary survivor: main fixed-support random-family theorem |
| Artifact completeness | NOT YET |
| Submission readiness | NOT YET |

## Current surviving contribution set

1. **Headline:** random `Theta(log n)`-uniform FBDG families force `q=Omega(w)` for exact canonical nonlinear encodings with two fixed update locations per source coordinate and adaptive decoding.
2. **Positive counterpart:** structured fixed-support families can achieve `u=2,q=2`, demonstrating a genuine structure-versus-randomness separation.
3. **Supporting structure:** the fixed-support proof exposes a diffuse/hub dichotomy and shows why any extension to moving support must defeat static residual-group geometry.
4. **Application bridge:** the result explains the gather bottleneck relevant to the Binary-DVESP transfer without claiming an unrestricted Binary-DVESP lower bound.

## Publication status

**Verdict:** `PASS-CONDITIONAL` for continued manuscript development.  
The central theorem is ready to be written as a formal result. The paper is **not yet submission-ready** until the structured-family appendix, secondary-proof archive, reproducibility package, and final exact-equivalence prior-art audit are incorporated.
