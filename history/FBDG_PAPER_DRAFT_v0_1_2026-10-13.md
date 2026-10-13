# Dynamic Fixed-Batch Retrieval: Structured Codes and Random-Family Locality Barriers

**Draft v0.1 — 2026-10-13**  
**Paper type:** theoretical computer science / data structures / coding-theoretic locality  
**Status:** main random fixed-support theorem proof closed; several supporting results are carried from the research handoff and should have their full archived proofs inserted before submission.

---

## Abstract

We study a dynamic retrieval problem in which a Boolean vector is maintained under point updates while queries ask for the exact contents of one set from a fixed family of sparse batches. We call the model **Fixed-Batch Dynamic Gather (FBDG)**. The central question is whether a representation can simultaneously have very low write locality and very low recovery locality when each requested batch has size \(w=\Theta(\log n)\).

The answer depends sharply on the incidence structure of the batch family. On the positive side, structured families admit nonlinear or linear coded representations with two fixed update locations per source coordinate and constant recovery locality; an asymptotic construction achieves \(u=2\) and \(q=2\) with \(w=\Theta(\log n)\). On the negative side, we prove that a random family of \(M=\Theta(n)\) independent \(w\)-subsets has, with high probability, the opposite behavior: every exact canonical representation into \(w\)-bit cells in which each source coordinate has at most two **fixed** update locations requires
\[
q=\Omega(w),
\]
even when cell contents are arbitrary nonlinear functions and the decoder is fully adaptive.

The proof is based on a structure-versus-congestion dichotomy for the fixed update-support graph. In the diffuse case, a random requested batch contains a linear-size matching uniformly over all support systems, forcing a linear-size hitting set. In the hub-concentrated case, a small set of cells can be treated as a short sketch; canonicality bounds the size of each residual source group, random-family spreading supplies many queries touching distinct groups, and a self-contained adaptive decision-tree counting lemma forces linearly many residual group probes. The fixed-support hypothesis is essential to this proof. Allowing update supports to move with the state or update history remains open; the best unrestricted baseline in our current development is \(\Omega(w/\log w)\).

The resulting picture is a locality separation between structured and random batch families under two-write canonical encodings, with a remaining frontier concentrated on the power of moving high-influence write hubs.

---

## 1. Introduction

Dynamic data structures are usually studied by specifying an update operation and a query operation, then asking how the two costs trade off. In many applications, however, the query workload is not arbitrary: it consists of a fixed collection of small groups of coordinates that must be recovered together. This occurs naturally in batched retrieval, materialized views, packed microstructures, coded storage, and algorithmic reductions in which a larger query is decomposed into many fixed local subqueries.

This paper isolates that regime in a minimal exact-recovery problem. A logical state
\[
x\in\{0,1\}^n
\]
is maintained under single-coordinate flips. A fixed family
\[
\mathcal B=(B_1,\ldots,B_M),\qquad B_i\subseteq[n],\quad |B_i|=w,
\]
is known in advance. Query \(i\) must return the complete vector \(x|_{B_i}\). We measure **write locality** \(u\), the number of dynamic memory words that may change after a source-coordinate update, and **query locality** \(q\), the number of dynamic words probed by a query. Cell contents may be nonlinear, and query probes may be adaptive.

At first sight one might expect that forcing \(u\) to be a small constant should make exact recovery of a \(w\)-bit batch cost \(\Theta(w)\). This intuition is false already at \(u=2\). A seven-coordinate Fano-plane instance admits a two-write, two-probe representation, and the same algebraic mechanism can be amplified to an infinite structured family with \(w=\Theta(\log n)\) while retaining constant update and recovery locality. Thus no universal theorem of the form \(u=2\Rightarrow q=\Omega(w)\) can hold.

The natural question is then structural:

> **When do two fixed update locations permit constant recovery, and when does the batch incidence pattern force linear recovery locality?**

Our main result answers this for random batch families under a canonical fixed-support representation. If \(M=\Theta(n)\) and each \(B_i\) is an independent random \(w\)-subset with \(w=\Theta(\log n)\), then with high probability every exact canonical representation in which each source coordinate can influence at most two fixed memory cells satisfies
\[
q=\Omega(w).
\]
The lower bound allows arbitrary nonlinear cell functions and fully adaptive exact decoding.

The proof reveals why the structured examples are exceptional. Represent the two fixed update locations of each source coordinate as the endpoints of an edge. If the resulting support graph is diffuse, a random batch contains many pairwise disjoint support edges, and any query must hit all of them. If instead many source coordinates concentrate around a small hub set of memory cells, those hub cells form only \(O(w^2)\) bits of global information. Canonicality then forces the remaining source coordinates to break into bounded-size residual groups. Random batches spread across those groups, and enough group-disjoint queries create many independent target bits outside the hub sketch. An adaptive decision-tree counting argument then forces \(\Omega(w)\) residual probes per query.

The fixed-support restriction is not cosmetic. The proof repeatedly uses a static incidence relation between source coordinates and memory cells: it defines which logical variables can affect a cell, permits a static support graph, identifies a permanent hub, and partitions crossing coordinates into residual groups. If supports can move with the current state or update history, this geometry can twist across the Boolean cube. Removing fixed support is therefore the central open problem left by our result.

### 1.1 Contributions

The current contribution stack is deliberately stated in bounded form.

1. **FBDG formulation and application bridge.** We isolate exact fixed-family vector retrieval under point updates as a locality problem. This formulation is useful for a Binary-DVESP microblock reduction, but we do not claim that simultaneous local update and local decode is new; that theme is well established in coding and compression \cite{chandran2014luldc,vatedka2020bigdata,vatedka2020worstcase}.

2. **Structured two-write constructions.** We retain a Fano-plane witness and an asymptotic structured family with \(u=2,q=2\). These serve as the positive side of the separation. Closely related finite-geometry, arbitrary-access-set, and graph-based coding mechanisms already exist \cite{ishai2004batch,paterson2009cbc,rawat2016batchgraphs,maturana2021arbitrary}; the contribution here is their role inside the dynamic fixed-batch locality dichotomy rather than a claim that Fano coding itself is new.

3. **Random-family fixed-support lower bound.** The main theorem shows that random \(\Theta(\log n)\)-uniform families require \(\Omega(w)\) adaptive probes under two fixed update locations per source coordinate, even for arbitrary nonlinear cell contents. Within the literature searched as of October 2026, we did not identify a materially equivalent theorem. We therefore treat the result as **likely distinct within the searched scope**, not as an absolute priority claim.

4. **A self-contained hub-case information argument.** The proof derives a sketch-probe lower bound specialized to exact recovery of independent target bits from distinct residual groups. The argument is a standard-style decision-tree/help-bits counting argument rather than a claimed new information-theoretic framework. Recent Query-with-Sketch work provides a much more general min-entropy formalism for adaptive probing with short sketches \cite{garg2026qws}.

5. **Explicit frontier.** The theorem does not handle moving or history-dependent update supports. That case remains open and is separated sharply from the fixed-support result throughout the paper.

---

## 2. Model and notation

### 2.1 Fixed-Batch Dynamic Gather

An FBDG instance consists of a universe \([n]\) and a fixed batch family
\[
\mathcal B=(B_1,\ldots,B_M),\qquad B_i\in\binom{[n]}{w}.
\]
The maintained state is \(x\in\{0,1\}^n\). An update flips a single coordinate \(x_j\). A query for \(B_i\) must output the exact ordered restriction \(x|_{B_i}\).

Dynamic memory is divided into \(w\)-bit cells. Computation is free; the cost of a query is the number of dynamic cells probed. The family \(\mathcal B\), code description, and any state-independent constants are available to the algorithm at no probe cost.

### 2.2 Canonical fixed-support encodings

A **canonical encoding** is a map
\[
E:\{0,1\}^n\to(\{0,1\}^w)^{\mathcal C}
\]
from the logical state to dynamic memory. Canonicality rules out update-history-dependent representations: the encoded state is determined by the current \(x\) alone.

For each logical coordinate \(j\), define its essential support
\[
S_j:=\{c\in\mathcal C:\exists x\text{ such that }E_c(x)\neq E_c(x\oplus e_j)\}.
\]
The fixed-support locality condition \(u=2\) is
\[
|S_j|\le2\qquad\forall j.
\]
This definition removes irrelevant dummy write locations and captures exactly which cells can depend on coordinate \(j\).

The query algorithm may be fully adaptive. Let \(q\) be its worst-case number of cell probes.

### 2.3 Active coordinates

Let
\[
A:=\bigcup_{i=1}^M B_i.
\]
Only coordinates in \(A\) are constrained by the query workload. This distinction matters in the information-capacity arguments: an inactive coordinate need not be represented at all.

---

## 3. Deterministic consequences of fixed support

The main lower bound begins with three elementary but crucial facts.

### Lemma 3.1 (cell-local dependence)
For a memory cell \(c\), let
\[
N(c)=\{j:c\in S_j\}.
\]
Then \(E_c(x)\) depends only on \(x|_{N(c)}\).

#### Proof
If two logical states \(x,y\) agree on \(N(c)\), transform \(x\) to \(y\) by flipping only coordinates outside \(N(c)\). None of these flips can change cell \(c\), by definition of the essential supports. Canonicality ensures that every intermediate memory state is the canonical encoding of the corresponding logical state. Therefore \(E_c(x)=E_c(y)\). ∎

### Lemma 3.2 (active-coordinate injectivity)
If \(x\) and \(y\) differ on some coordinate in \(A\), then \(E(x)\neq E(y)\).

#### Proof
Choose a batch containing a coordinate on which \(x\) and \(y\) differ. Exact recovery of the requested vector would be impossible from identical encoded states. ∎

### Lemma 3.3 (adaptive hitting)
Fix a state \(x\), a batch \(B\), and the actual adaptive probe path \(P_B(x)\). For every \(j\in B\),
\[
P_B(x)\cap S_j\neq\varnothing.
\]

#### Proof
Assume the path on \(x\) avoids \(S_j\). Compare the execution with the one on \(x\oplus e_j\). The two encodings can differ only on \(S_j\). Inductively, every probed cell has the same content in both executions, so the adaptive algorithm follows the same address sequence and produces the same output. The requested bit \(j\) differs, contradicting exactness. ∎

Hence every actual probe set is a hitting set for the queried supports. In particular, if a batch contains \(r\) coordinates with pairwise disjoint supports, then every correct adaptive query uses at least \(r\) probes.

---

## 4. The structured side of the separation

The universal implication \(u=2\Rightarrow q\ge w\) is false. The smallest witness in our development is the seven-point Fano-plane instance with \(w=3\), where a linear representation achieves
\[
u=2,\qquad q=2.
\]
All \(2^7\times7=896\) logical-state/query cases were exhaustively checked in the accompanying research process.

The same algebraic pattern admits an asymptotic amplification. Using independent \(t\)-bit source blocks
\[
U_0,U_1,U_2,L_1,L_2,R_1,R_2,
\]
store three \(3t\)-bit words
\[
C_0=(U_0,L_1,L_2),
\]
\[
C_1=(U_1,R_1,R_2),
\]
\[
C_2=(U_2,L_1\oplus R_1,L_2\oplus R_2).
\]
Coordinates in \(U_0,U_1,U_2\) affect one stored word, while coordinates in each \(L_i\) or \(R_i\) affect two. Thus \(u\le2\). The corresponding structured query family recovers every requested \(3t\)-bit batch from two stored words using constant word operations. Taking sufficiently many disjoint gadgets gives
\[
n=\Theta(t2^t),\qquad w=3t=\Theta(\log n),
\]
and
\[
u=2,\qquad q=2,
\qquad D(w)=G(w)=O(1).
\]

**Draft-integrity note.** The exact incidence list for the asymptotic batch family and its archived differential-test evidence must be imported into the final appendix before submission. The present draft records the verified algebraic normal form and asymptotic parameters but does not reconstruct missing incidence details from memory.

This construction establishes the positive side needed for the paper's main message: two fixed writes can support constant recovery on highly structured families.

---

## 5. Main theorem: random families are hard

We now turn to independent random batches.

### Theorem 5.1 (random fixed-support nonlinear two-write lower bound)
Fix positive constants
\[
0<c_-\le c_+,
\qquad
0<\mu_-\le\mu_+.
\]
Let
\[
c_-\log n\le w\le c_+\log n,
\qquad
\mu_-n\le M\le\mu_+n,
\]
and sample \(B_1,\ldots,B_M\) independently and uniformly from \(\binom{[n]}{w}\).

There exists a constant \(c_*>0\), depending only on the displayed constants, such that with probability \(1-o(1)\) over the random family, every exact canonical FBDG encoding into \(w\)-bit cells with essential supports
\[
|S_j|\le2
\]
has worst-case adaptive query complexity
\[
q\ge c_*w.
\]
Thus
\[
\boxed{q=\Omega(w)}.
\]

The theorem places no linearity restriction on the encoded cells.

### 5.1 Parameter choices

Set
\[
a=\frac18.
\]
Choose \(\varepsilon>0\) sufficiently small that
\[
\Gamma=(1-a)\log\frac1{2\varepsilon}-\log2
\]
satisfies
\[
\Gamma\mu_-c_->3.
\]
Define
\[
\delta=\frac\varepsilon2,
\qquad
\kappa=\frac\delta4=\frac\varepsilon8.
\]
The proof establishes several random-family properties simultaneously and then applies a deterministic diffuse/hub dichotomy to every possible fixed support system.

---

## 6. Random-family lemmas

### Lemma 6.1 (almost all source coordinates are active)
With probability \(1-o(1)\), at most \(\varepsilon n/4\) coordinates lie outside \(A\).

#### Proof
For fixed \(j\),
\[
\Pr[j\notin A]
=\left(1-\frac wn\right)^M
\le e^{-Mw/n}
\le n^{-\mu_-c_-}.
\]
The expected number of inactive coordinates is \(o(n)\); Markov's inequality finishes the proof. ∎

### Lemma 6.2 (uniform source degree)
There is a constant \(\Delta\) such that, with probability \(1-o(1)\), every coordinate occurs in at most \(\Delta w\) batches.

#### Proof sketch
For fixed \(j\), the degree is binomial with mean at most \(\mu_+w\). Choose \(\Delta\) so that a Chernoff upper tail is at most \(n^{-2}\), and union bound over \(j\in[n]\). ∎

### Lemma 6.3 (uniform richness of linear-size source sets)
With probability \(1-o(1)\), every \(C\subseteq[n]\) of size at least \(\delta n\) is hit in at least \(\delta w/2\) coordinates by at least \(M/2\) batches.

#### Proof
For fixed \(C\), the intersection size of one batch is hypergeometric with mean at least \(\delta w\). Its probability of falling below half the mean is \(e^{-\Omega(w)}\). The probability that at least half of the \(M=\Theta(n)\) independent batches are bad is therefore \(e^{-\Omega(nw)}\), which survives a union bound over all \(2^n\) choices of \(C\). ∎

### Lemma 6.4 (uniform spreading on polylogarithmic sets)
There is a constant \(K\) such that, with probability \(1-o(1)\), every \(S\subseteq[n]\) with
\[
|S|\le(2aw+1)w=O(w^2)
\]
satisfies
\[
\sum_{i=1}^M(|B_i\cap S|-1)_+\le K|S|.
\]

#### Proof
Fix \(|S|=s\) and let \(t=\lceil Ks\rceil\). If the displayed excess is at least \(t\), then there exist \(r\le t\) distinct batches and positive integers \(t_1+\cdots+t_r=t\) such that batch \(\ell\) contains at least \(t_\ell+1\) prescribed elements of \(S\). A fixed \(k\)-subset lies inside a random \(w\)-subset with probability at most \((2w/n)^k\) for the relevant \(k=o(n)\). Therefore, with \(\alpha=2sw/n\),
\[
\Pr[Z(S)\ge t]
\le
\alpha^t
\sum_{r=1}^t
\binom Mr\binom{t-1}{r-1}\alpha^r.
\]
Using the standard bounds on the binomial coefficients gives
\[
\Pr[Z(S)\ge t]
\le
t\left(\frac{C s^3w^2}{n}\right)^t
\]
for a constant \(C\). Because \(s=O(w^2)\) and \(w=O(\log n)\), choosing any fixed \(K\ge3\) makes the union bound over all \(\binom ns\) sets and all admissible \(s\) tend to zero. ∎

### Lemma 6.5 (uniform diffuse matching)
Let
\[
r=\lfloor aw\rfloor.
\]
With probability \(1-o(1)\), the following holds simultaneously for every fixed support system \((S_1,\ldots,S_n)\) with \(|S_j|\le2\): if every set of at most \(2r\) memory cells is incident to at most \(\varepsilon n\) source coordinates, then at least one random batch contains \(r\) coordinates with pairwise disjoint supports.

#### Proof
The union of all essential supports contains at most \(2n\) cells. After relabeling these cells, the number of support systems is at most
\[
\left(1+2n+\binom{2n}{2}\right)^n
\le
(3n^2)^n
=
\exp(2n\log n+O(n)).
\]

Fix one diffuse support system and expose a random batch sequentially, accepting a source coordinate when its support is disjoint from all previously accepted supports. Until \(r\) coordinates have been accepted, the union of accepted supports has size at most \(2r\), so the conditional rejection probability is at most \(2\varepsilon\) for large \(n\). Fewer than \(r\) acceptances require at least \((1-a)w\) rejections, hence
\[
\Pr[\nu(B)<r]
\le
2^w(2\varepsilon)^{(1-a)w}
=e^{-\Gamma w}.
\]
All \(M\) independent batches fail with probability at most \(e^{-\Gamma Mw}\). The choice \(\Gamma\mu_-c_->3\) leaves enough exponent to union bound over every support system. ∎

---

## 7. A sketch-probe lemma for the hub case

The hub proof needs one information-theoretic statement. Because the residual hard distribution is a product and the selected target bits lie in distinct groups, a short self-contained argument suffices.

### Lemma 7.1 (independent-target sketch-probe bound)
Let \(X_1,\ldots,X_N\) be independent group-valued random variables. Suppose
\[
F(X)=(Y_1,\ldots,Y_m)
\]
consists of independent unbiased bits and each \(Y_\ell\) belongs to a distinct input group. Consider a deterministic exact algorithm given an arbitrary \(s\)-bit sketch \(S(X)\), after which it may adaptively probe whole groups. If \(D\) is the number of group probes, then for every integer \(c\ge1\),
\[
\mathbb E[D]
\ge
(1-2^{-c})(m-s-c)
\]
whenever \(m>s+c\).

#### Proof
Fix a sketch value \(z\). It defines an adaptive decision tree over the raw groups. Let
\[
t=m-s-c.
\]
At any leaf of depth at most \(t\), at most \(t\) target groups have been revealed. Conditioned on that leaf's partial assignment, at least
\[
m-t=s+c
\]
target bits remain independent and unbiased. Hence the probability of the leaf's declared output vector is at most \(2^{-(s+c)}\) times the probability of the leaf cylinder. The leaf cylinders of one decision tree are disjoint, so the correct probability mass of all depth-at-most-\(t\) leaves in that tree is at most \(2^{-(s+c)}\). Summing over the at most \(2^s\) sketch values gives
\[
\Pr[\text{correct and }D\le t]\le2^{-c}.
\]
Exactness implies
\[
1\le\Pr[D>t]+2^{-c}.
\]
Markov's inequality gives \(\Pr[D>t]\le\mathbb E[D]/t\), proving the claim. ∎

This lemma is closely aligned with the decision-tree/help-bits viewpoint underlying more general Query-with-Sketch lower bounds \cite{garg2026qws}. We use the specialized form because it is sufficient and avoids importing unnecessary machinery.

---

## 8. Proof of Theorem 5.1

Condition on the simultaneous random-family events of Section 6. Fix an arbitrary canonical fixed-support representation.

### 8.1 Diffuse case

Suppose every set of at most \(2r\) memory cells is incident to at most \(\varepsilon n\) source coordinates. By Lemma 6.5, some requested batch contains \(r=\Theta(w)\) coordinates whose supports are pairwise disjoint. Lemma 3.3 forces the query to hit every one of these supports. Therefore
\[
q\ge r=\Omega(w).
\]

### 8.2 Hub-concentrated case

Otherwise there exists a set \(H\) of memory cells with
\[
h:=|H|\le2r=O(w)
\]
incident to more than \(\varepsilon n\) source coordinates.

Let
\[
I_H=\{j\in A:S_j\subseteq H\}.
\]
Fixing all other logical coordinates, varying \(I_H\) can alter only the \(h\) hub cells. Active-coordinate injectivity implies
\[
|I_H|\le hw=O(w^2)=o(n).
\]
By Lemma 6.1, at most \(\varepsilon n/4\) coordinates are inactive. Hence at least \(\delta n\) active coordinates have supports with one endpoint in \(H\) and one outside. Call this crossing set \(C\).

For every nonhub cell \(v\), define
\[
G_v=\{j\in C:v\in S_j\}.
\]
These groups partition \(C\). Fixing all coordinates outside one group \(G_v\), varying that group can change only the \(h+1\) cells in \(H\cup\{v\}\). Injectivity gives
\[
|G_v|\le(h+1)w=O(w^2).
\]

By the uniform richness lemma, at least \(M/2\) batches contain at least \(\delta w/2\) crossing coordinates. For batch \(i\), let
\[
e_i=\sum_v(|B_i\cap G_v|-1)_+.
\]
The spreading lemma yields
\[
\sum_i e_i
=
\sum_v\sum_i(|B_i\cap G_v|-1)_+
\le
K\sum_v|G_v|
=O(n).
\]
Thus only \(O(n/w)=o(n)\) batches have \(e_i>\delta w/4\). A constant fraction of all batches therefore touch at least
\[
\frac{\delta w}{4}=\kappa w
\]
distinct residual groups.

The degree bound now lets us separate these batches. A group \(G_v\) occurs in at most
\[
\sum_{j\in G_v}d_j
\le
\Delta w|G_v|
\le
\Delta(h+1)w^2
\]
batches. Selecting one candidate batch therefore conflicts with at most \(O((h+1)w^3)\) others. Because the candidate pool has \(\Theta(n)\) batches and \(h=O(w)\), a greedy argument selects
\[
L=\left\lceil\frac{4h}{\kappa}\right\rceil=O(w)
\]
batches whose residual-group sets are pairwise disjoint.

From each touched residual group in each selected batch, choose one requested source bit. The resulting target vector has
\[
m\ge\kappa Lw
\]
independent unbiased bits, each from a distinct residual group.

Now draw a logical state by fixing every coordinate outside \(C\) to zero and making all coordinates in \(C\) independent unbiased bits. Treat the residual groups \(X_v=x|_{G_v}\) as the raw input groups. Give all hub-cell contents to the decoder for free; this is an
\[
s=hw
\]
bit sketch.

Every nonhub encoded cell \(v\) is, by Lemma 3.1, a function only of the source coordinates whose essential supports contain \(v\). Under the chosen distribution, its only unfixed influences are exactly the bits in \(G_v\). Therefore one raw group probe reveals enough information to simulate a probe to encoded cell \(v\). Hub probes are free from the sketch, and cells with empty residual group are constant under the distribution.

Running the original exact algorithms for the \(L\) selected batches therefore yields an exact sketch-probe algorithm for the \(m\) selected target bits using at most \(Lq\) group probes. Lemma 7.1 with \(c=2\) gives
\[
Lq\ge\frac34(m-s-2).
\]
Because \(m\ge\kappa Lw\), \(s=hw\), and \(L\ge4h/\kappa\),
\[
q
\ge
\frac34\left(\kappa w-\frac{hw}{L}-\frac2L\right)
\ge
\Omega(w).
\]
This completes the hub case and the theorem. ∎

---

## 9. Why fixed support is essential

Several proof steps fail immediately if update locations can move with the current state or update history.

First, Lemma 3.1 requires a static set \(N(c)\) of logical coordinates capable of influencing cell \(c\). Second, the diffuse/hub dichotomy is a statement about one fixed support graph. Third, the residual groups \(G_v\) are defined by permanent outside endpoints of crossing supports. Finally, the hub sketch is useful because the nonhub cells can be simulated from fixed raw source groups.

A moving-support encoding can route the same logical coordinate through different physical cells in different regions of the Boolean cube. Such a representation need not admit any globally meaningful residual partition. Our theorem therefore does not imply a lower bound for unrestricted history-dependent two-write data structures.

The current frontier is
\[
\begin{array}{ll}
\text{structured fixed-support }u=2 &: q=O(1),\\
\text{random fixed-support }u=2 &: q=\Omega(w),\\
\text{moving/history-dependent }u=2 &: \Omega(w/\log w)\text{ known in our current development; }\Omega(w)\text{ open}.
\end{array}
\]

A promising route to the moving-support case is to view the update locations as labels on edges of the Boolean cube and exploit commutation around squares. One would like to show that a large subcube stabilizes many supports, after which the fixed-support theorem could be applied. A counterexample would instead need to maintain high-congestion hubs while continuously moving which physical cells play the hub role.

---

## 10. Supporting locality bounds

The broader project contains several supporting results that sharpen the context around Theorem 5.1.

### 10.1 Block-linear representations

For suitable random \(w\)-uniform families, the block-linear model satisfies
\[
q+2u\ge w-O(\log w).
\]
Thus constant write locality forces \(q=w-O(\log w)\) in that restricted algebraic model. The sparse-factorization viewpoint for dynamic linear representations has neighboring prior art, including the preliminary 2026 note of Blanchi \cite{blanchi2026sparse}; the exact FBDG inequality should therefore be presented as a workload-specific bound rather than as the invention of the general factorization correspondence.

### 10.2 Canonical nonlinear \(u=1\)

For canonical nonlinear encodings,
\[
u=1\Longrightarrow q\ge w.
\]
The Fano construction shows that the behavior changes genuinely at \(u=2\).

### 10.3 Unrestricted baseline

A reduction from existential Marked Ancestor yields an explicit hard FBDG family with \(M=\Theta(n)\) and \(w=\Theta(\log n)\) for which constant write locality implies
\[
q=\Omega(w/\log w).
\]
Marked Ancestor is a classical source of dynamic cell-probe lower bounds \cite{alstrup1998marked}. The role of this result in the present paper is as an unrestricted baseline, not as the main novelty claim.

### 10.4 State-local congestion

At a fixed reachable state \(\sigma\), let \(U_j(\sigma)\) be the cells changed by flipping coordinate \(j\), and let
\[
f(\sigma)=\max_c|\{j:c\in U_j(\sigma)\}|.
\]
The project derives a congestion inequality of the form
\[
M\left(\frac{w^2}{q}-w\right)
\le
un(f(\sigma)-1)+2\rho(\mathcal B),
\]
where \(\rho\) measures repeated source-pair co-occurrence across the batch family. For random families with \(M=n\), this implies that any hypothetical \(q=o(w)\) unrestricted representation must maintain superlinear-in-\(w\) write influence at every reachable state. This structural statement motivates the moving-hub interpretation of the remaining open problem.

**Draft-integrity note.** The complete archived proofs of Sections 10.1–10.4 must be inserted or linked in the final theorem appendix. The present draft preserves their proven research-state labels but does not invent missing proof text.

---

## 11. Connection to Binary DVESP

The original motivation came from a packed-query bottleneck in Binary Dynamic Volatile-Edge Shortest Paths (Binary DVESP). The relevant transfer statement is the following: if an FBDG instance with batch width \(w\) admits gather time \(G(w)\) and point-update time \(D(w)\), then the associated Binary-DVESP construction has query time
\[
Q(k)=
O\!\left(
\left(k+\frac{k^2}{w^2}\right)G(w)
+kD(w)
+k\log k
\right).
\]
With \(w=\Theta(\log k)\), constant-time gather would yield an ordinary-RAM scale
\[
O\!\left(\frac{k^2}{\log^2k}+k\log k\right),
\]
whereas \(G(w)=\Theta(w)\) returns the familiar \(k^2/\log k\) scale.

The structured FBDG constructions therefore demonstrate that the stronger packed scale is possible for special incidence families. Conversely, Theorem 5.1 shows that a random fixed-support two-write gather mechanism cannot achieve constant recovery.

This is **not** yet an unrestricted Binary-DVESP lower bound. A separate argument would be required to show that the specific microblock batch families generated by Binary DVESP satisfy the relevant hardness conditions, or to prove a direct lower bound in the graph problem itself.

---

## 12. Related work

### Batch and graph-based codes

Batch codes were introduced by Ishai, Kushilevitz, Ostrovsky, and Sahai to retrieve multiple requested items with bounded load across storage buckets \cite{ishai2004batch}. Combinatorial and graph-based variants developed a substantial incidence-structure literature \cite{paterson2009cbc,rawat2016batchgraphs}. In two-replication combinatorial batch codes, a source item naturally corresponds to an edge joining the two servers that store it, closely paralleling the support graph used here. We therefore do not claim the graph representation itself as new.

Our setting differs in objective and dynamics. The requested family is fixed in advance rather than universally quantifying over all batches of a given size; writes correspond to source-coordinate updates; cells may contain arbitrary nonlinear functions; and the lower bound asks how a random fixed family constrains recovery locality under fixed write supports.

### Local update and local decode

Simultaneous local updating and local decoding has been studied directly in coding and compression. Chandran, Kanukurthi, and Ostrovsky introduced locally updatable and locally decodable codes \cite{chandran2014luldc}. Vatedka and Tchamkerten studied compression with local decode and update, including constant average locality in one regime \cite{vatedka2020bigdata}; Vatedka, Chandar, and Tchamkerten studied worst-case locality and obtained \(O(\log\log n)\) bounds together with converse results under stated assumptions \cite{vatedka2020worstcase}. These works make clear that “local read plus local write” is an established theme. FBDG instead focuses on exact recovery of one batch from a fixed multi-coordinate query family and on a support-incidence separation between structured and random workloads.

### Arbitrary access sets and finite geometry

Maturana and Rashmi study storage codes tailored to prescribed access sets rather than requiring MDS-style recovery from all subsets \cite{maturana2021arbitrary}. Their orientation differs from ours—their access sets are storage-node sets sufficient to reconstruct a message, whereas our sets are requested source-coordinate batches—but the finite-geometry neighborhood is relevant to the structured side. Accordingly, the Fano-plane example is used as an illustrative witness, not as a headline coding novelty claim.

### Sparse factorization

For linear dynamic representations, update and query locality translate naturally into column and row sparsity of a factorization \(A=RM\). A June 2026 preliminary note by Blanchi explicitly develops this sparse-factorization viewpoint \cite{blanchi2026sparse}. That note is self-described as preliminary and AI-assisted, but it is sufficient to make a broad “sparse factorization is new” claim inappropriate. Our block-linear FBDG inequality, where used, should be positioned as a workload-specific lower bound.

### Query-with-Sketch and adaptive help bits

Garg, He, Li, Papakonstantinou, and Yang introduce a general Query-with-Sketch model and a min-entropy lifting lemma for systematic data-structure lower bounds \cite{garg2026qws}. Their model explicitly permits adaptive probes after an arbitrary short sketch. The hub case in our proof has the same high-level flavor: hub contents act as a sketch, while nonhub encoded-cell probes are strengthened to raw residual-group probes. Because our residual distribution is a product and our target bits occupy distinct groups, we use a simpler self-contained counting lemma rather than invoking the full min-entropy machinery.

### Dynamic lower bounds

The unrestricted \(\Omega(w/\log w)\) baseline in our research development descends from classical dynamic hardness around Marked Ancestor \cite{alstrup1998marked}. This line provides context for the scale of general dynamic cell-probe lower bounds, while the main theorem here exploits the much stronger fixed-support structure to reach \(\Omega(w)\).

---

## 13. Contribution preflight and novelty boundary

The manuscript should not use “first,” “optimal,” or “state of the art” in its title or abstract. The current bounded contribution assessment is:

| Candidate contribution | Closest neighborhood | Status |
|---|---|---|
| FBDG terminology/formalization | batch retrieval + locally updatable/decodable coding | incremental/combinational |
| support graph for fixed `u=2` | two-replication graph batch codes | established mechanism |
| Fano structured witness | finite-geometry / arbitrary-access-set coding | overlapping neighborhood |
| sparse linear factorization viewpoint | Blanchi 2026 preliminary note and broader linear-data-structure folklore | prior art found broadly |
| random fixed-support nonlinear `u=2 => q=Omega(w)` | no materially equivalent theorem found in searched literature | **survives; likely distinct within search scope** |
| moving-support `Omega(w)` theorem | unresolved | open |

The safest contribution sentence is:

> Within the literature searched as of October 2026, we did not identify a materially equivalent lower bound for exact fixed-batch dynamic retrieval showing that random \(\Theta(\log n)\)-uniform batch families require \(\Omega(\log n)\) adaptive word probes under two fixed update locations per source coordinate, even with arbitrary nonlinear cell contents.

This must be followed immediately by the restriction:

> The result applies to canonical fixed-support encodings; removing fixed support remains open.

---

## 14. Limitations and open problems

The main limitation is structural rather than quantitative. The lower bound does not cover moving update supports or history-dependent memory states. The exact role of canonicality should also be kept explicit: Lemma 3.1 uses the fact that a cell's value is a well-defined function of the current logical state.

Several questions remain.

1. **Remove fixed support.** Can random \(w\)-uniform families force \(q=\Omega(w)\) when each update writes at most two cells whose addresses may depend on state or history?
2. **General constant \(u\).** Does an analogous structure-versus-randomness theorem hold for every fixed \(u>2\)?
3. **Characterize the easy/hard incidence parameter.** Randomness is sufficient for hardness and finite-geometric structure can be easy, but the exact deterministic combinatorial property separating the two remains unknown.
4. **Binary-DVESP microblocks.** Do the batch families arising in the graph reduction inherit the random-family barrier or some deterministic analogue?
5. **Canonicality.** Can one quantify the additional power of history-dependent representations separately from the power of moving physical write locations?
6. **Tighter constants and derandomization.** The proof uses deliberately wasteful constants in the uniform diffuse union bound. Explicit pseudorandom or expanding families satisfying the same events would strengthen the theorem from a random existence statement to a constructive hard family.

---

## 15. Conclusion

Fixed-batch dynamic retrieval exhibits a sharp dependence on incidence structure. Two fixed writes per source bit do not by themselves force expensive recovery: structured families can encode enough overlap algebraically to answer \(\Theta(\log n)\)-bit batches from only two words. Random families behave differently. With high probability, every canonical two-fixed-write representation must spend \(\Omega(w)\) adaptive probes per batch even when storage is nonlinear.

The proof gives a concrete structural explanation. A fixed support system is either diffuse, in which case a random query exposes many disjoint supports, or it concentrates influence in a small hub. A hub can summarize only \(O(w^2)\) bits; canonicality confines the remaining influence to small residual groups; random batches spread across those groups; and a short sketch cannot replace the information carried by linearly many adaptive residual probes.

The remaining escape route is precisely the one excluded by the theorem: moving high-influence write hubs whose identities depend on the current state or update history. Resolving whether such motion can beat linear recovery locality is the next mathematical frontier.

---

## Appendix A. Theorem-dependency graph

```text
Main random-family theorem
|
+-- canonical fixed-support model
|   +-- cell-local dependence
|   +-- active-coordinate injectivity
|   +-- adaptive hitting
|
+-- random-family events
|   +-- almost-all-active
|   +-- maximum source degree O(w)
|   +-- uniform large-set richness
|   +-- uniform small-set spreading
|   +-- uniform diffuse matching over all support systems
|
+-- diffuse/hub dichotomy
    |
    +-- diffuse
    |   +-- random batch matching
    |   +-- adaptive hitting => Omega(w) probes
    |
    +-- hub
        +-- internal active coordinates <= hw
        +-- Omega(n) active crossing coordinates
        +-- residual group size <= (h+1)w
        +-- many group-rich batches
        +-- greedy selection of L=Theta(h) group-disjoint batches
        +-- independent-target sketch-probe lemma
        +-- Lq >= Omega(Lw)
        +-- q = Omega(w)
```

---

## Appendix B. Proof-repair ledger

The final proof incorporates the following defects found during adversarial audit.

1. **Spreading alone does not imply separated queries.** Two batches can touch the same group once each while contributing zero spreading excess. The repair adds a uniform source-degree bound and a greedy conflict argument.
2. **`L=Theta(h)` needs an explicit constant.** A hub sketch can store an entire target when too few batches are aggregated. The repaired proof fixes \(L=\lceil4h/\kappa\rceil\).
3. **Inactive coordinates cannot be used in injectivity counts.** The repair proves that a random family leaves only \(o(n)\) inactive coordinates and applies capacity arguments only to the active set.
4. **Dummy support locations are eliminated.** Essential supports are defined from actual dependence of the canonical encoding.
5. **No step is extended to moving support.** Every use of the fixed-support geometry is explicit.

---

## References

The accompanying BibTeX file `fbdg_references_2026-10-13.bib` contains the verified source registry used in this draft.

