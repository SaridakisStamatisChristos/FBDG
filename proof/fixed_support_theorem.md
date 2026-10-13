# Fixed-Support FBDG Lower Bound — Formal Mathematical Package

**Date:** 2026-10-13  
**Purpose:** Paper-ready mathematical closure of the random-family canonical fixed-support nonlinear `u=2` lower bound for Fixed-Batch Dynamic Gather (FBDG).  
**Evidence state:** `PROVED` (human-checkable proof package; not formally machine-verified).  
**Novelty state:** preserve `LIKELY DISTINCT WITHIN SEARCH SCOPE` from the prior-art audit.  
**Scope warning:** this package does **not** cover state-dependent or history-dependent moving update supports.

---

## 1. Model

Let \(\mathcal B=(B_1,\dots,B_M)\) be a family of subsets of \([n]\), each of size \(w\). The dynamic logical state is
\[
 x\in\{0,1\}^n.
\]
A query for \(B_i\) must return the exact vector \(x|_{B_i}\).

A **canonical encoding** is a map
\[
E:\{0,1\}^n\to (\{0,1\}^w)^{\mathcal C},
\]
where \(\mathcal C\) is an arbitrary set of dynamic memory cells and \(E_c(x)\in\{0,1\}^w\) is cell \(c\)'s content. Canonicality means the memory state is a function only of the current logical state \(x\), not of the update history.

For a logical coordinate \(j\), define its **essential fixed support**
\[
S_j:=\{c\in\mathcal C:\exists x\in\{0,1\}^n\text{ with }E_c(x)\neq E_c(x\oplus e_j)\}.
\]
The fixed-support \(u=2\) hypothesis is
\[
|S_j|\le 2\qquad\forall j\in[n].
\]
Thus every flip of coordinate \(j\) can change only the same at-most-two cells in every state. Using the essential support avoids dummy/padded support locations.

A query algorithm may be computationally unbounded and fully adaptive. Its probe complexity is the maximum number of dynamic cells read on any query and state; denote this by \(q\).

Define the active logical coordinates
\[
A:=\bigcup_{i=1}^M B_i.
\]
Only active coordinates are semantically required to be recoverable.

---

## 2. Main theorem

### Theorem 2.1 (random fixed-support nonlinear `u=2` barrier)
Fix constants
\[
0<c_-\le c_+<\infty,\qquad 0<\mu_-\le \mu_+<\infty.
\]
Suppose
\[
c_-\log n\le w\le c_+\log n,
\qquad
\mu_-n\le M\le \mu_+n.
\]
Choose \(B_1,\dots,B_M\) independently and uniformly from \(\binom{[n]}{w}\).

Then there exists a constant
\[
c_*=c_*(c_-,c_+,\mu_-,\mu_+)>0
\]
such that, with probability \(1-o(1)\) over \(\mathcal B\), every exact canonical FBDG encoding into \(w\)-bit cells satisfying
\[
|S_j|\le2\qquad\forall j
\]
has
\[
q\ge c_* w.
\]
In particular,
\[
\boxed{q=\Omega(w)}.
\]
The conclusion allows arbitrary nonlinear cell functions and fully adaptive exact queries.

The theorem also extends immediately to zero-error randomized queries whose worst-case probe bound holds for every random tape, by fixing any tape.

---

## 3. Deterministic structural lemmas

### Lemma 3.1 (cell-local dependence)
For every cell \(c\), define
\[
N(c):=\{j:c\in S_j\}.
\]
If \(x,y\in\{0,1\}^n\) agree on \(N(c)\), then
\[
E_c(x)=E_c(y).
\]
Hence \(E_c(x)\) is a function only of \(x|_{N(c)}\).

**Proof.** Transform \(x\) to \(y\) by flipping only coordinates outside \(N(c)\). By definition of essential support, flipping any \(j\notin N(c)\) leaves cell \(c\) unchanged. Canonicality identifies each intermediate memory state with \(E(\cdot)\). Therefore the content of \(c\) remains unchanged along the path. ∎

### Lemma 3.2 (active-coordinate injectivity)
If two states \(x,y\) differ on some active coordinate \(j\in A\), then
\[
E(x)\neq E(y).
\]

**Proof.** Some batch \(B_i\) contains \(j\). Exact recovery of \(x|_{B_i}\) from \(E(x)\) and of \(y|_{B_i}\) from \(E(y)\) would be impossible if the encoded states were identical. ∎

### Lemma 3.3 (adaptive hitting)
Fix a state \(x\), a queried batch \(B\), and let \(P_B(x)\) denote the set of cells probed on the actual adaptive execution path. Then for every \(j\in B\),
\[
P_B(x)\cap S_j\neq\varnothing.
\]

**Proof.** Suppose \(P_B(x)\cap S_j=\varnothing\). Compare the run on \(x\) with the run on \(x\oplus e_j\). The two encodings differ only inside \(S_j\). By induction on the adaptive transcript, every cell probed on the run from \(x\) has the same content in the flipped state, so the query chooses the same next address at every step and returns the same output. But the requested output bit \(j\) differs, contradicting exactness. ∎

### Corollary 3.4 (support hitting/vertex cover)
For any batch \(B\), every actual probe set is a hitting set for \(\{S_j:j\in B\}\). In particular, if \(B\) contains \(r\) coordinates whose supports are pairwise disjoint, then
\[
q\ge r.
\]

---

## 4. Random-family events

Set
\[
a:=\frac18.
\]
Choose a sufficiently small constant \(\varepsilon\in(0,1/16)\) such that
\[
\Gamma:=(1-a)\log\frac1{2\varepsilon}-\log2
\]
satisfies
\[
\Gamma\mu_-c_->3.
\]
Such a constant exists. Define
\[
\delta:=\frac\varepsilon2,
\qquad
\kappa:=\frac\delta4=\frac\varepsilon8.
\]
All logarithms in the probability estimates are natural logarithms.

### Lemma 4.1 (almost all coordinates active)
With probability \(1-o(1)\),
\[
|[n]\setminus A|\le \frac{\varepsilon n}{4}.
\]

**Proof.** For each \(j\),
\[
\Pr[j\notin A]
=\left(1-\frac wn\right)^M
\le e^{-Mw/n}
\le e^{-\mu_-w}
\le n^{-\mu_-c_-}.
\]
Hence the expected number of inactive coordinates is at most \(n^{1-\mu_-c_-}=o(n)\). Markov's inequality gives the claim. ∎

### Lemma 4.2 (uniform degree bound)
There exists a constant \(\Delta=\Delta(c_-,\mu_+)\) such that, with probability \(1-o(1)\), every source coordinate occurs in at most \(\Delta w\) batches:
\[
d_j:=|\{i:j\in B_i\}|\le\Delta w
\qquad\forall j\in[n].
\]

**Proof.** For fixed \(j\), \(d_j\sim\operatorname{Bin}(M,w/n)\) with mean at most \(\mu_+w\). A standard Chernoff bound gives
\[
\Pr[d_j\ge\Delta w]
\le \left(\frac{e\mu_+}{\Delta}\right)^{\Delta w}.
\]
Choose \(\Delta\) so that the exponent is at most \(-2\log n\) for \(w\ge c_-\log n\), then union bound over \(n\) coordinates. ∎

### Lemma 4.3 (uniform large-set richness)
With probability \(1-o(1)\), every set \(C\subseteq[n]\) with \(|C|\ge\delta n\) has at least \(M/2\) batches satisfying
\[
|B_i\cap C|\ge \frac{\delta w}{2}.
\]

**Proof.** Fix \(C\) of size at least \(\delta n\). For one random batch, \(|B_i\cap C|\) is hypergeometric with mean at least \(\delta w\). A hypergeometric Chernoff lower-tail bound yields
\[
\Pr\left[|B_i\cap C|<\frac{\delta w}{2}\right]
\le e^{-\delta w/8}=:p.
\]
The batches are independent. The probability that at least \(M/2\) batches are bad is at most
\[
2^M p^{M/2}
\le
\exp\left(M\log2-\frac{\delta Mw}{16}\right)
=
\exp(-\Omega(nw)).
\]
There are at most \(2^n\) possible sets \(C\). Since \(w=\Theta(\log n)\), a union bound remains \(o(1)\). ∎

### Lemma 4.4 (uniform small-set spreading)
There exists an absolute constant \(K\ge3\) such that, with probability \(1-o(1)\), simultaneously for every set \(S\subseteq[n]\) with
\[
1\le |S|\le D_0:=(2aw+1)w,
\]
we have
\[
\boxed{
Z(S):=\sum_{i=1}^M (|B_i\cap S|-1)_+\le K|S|.
}
\]

**Proof.** Fix \(S\) of size \(s\le D_0\) and let \(t:=\lceil Ks\rceil\). If \(Z(S)\ge t\), then for some integer \(1\le r\le t\), there exist distinct batches \(i_1,\dots,i_r\) and positive integers \(t_1,\dots,t_r\) with \(\sum_\ell t_\ell=t\) such that
\[
|B_{i_\ell}\cap S|\ge t_\ell+1
\qquad(\ell=1,\dots,r).
\]
Indeed, choose exactly \(t\) excess incidences from the batches contributing to \(Z(S)\).

For any fixed \(k\)-subset \(T\subseteq[n]\), with \(k\le D_0+1=o(n)\),
\[
\Pr[T\subseteq B_i]
=\frac{(w)_k}{(n)_k}
\le\left(\frac{2w}{n}\right)^k
\]
for all sufficiently large \(n\). Therefore, writing
\[
\alpha:=\frac{2sw}{n},
\]
a union bound over the chosen batches, compositions, and subsets of \(S\) gives
\[
\Pr[Z(S)\ge t]
\le
\alpha^t
\sum_{r=1}^t
\binom Mr\binom{t-1}{r-1}\alpha^r.
\]
Using
\[
\binom Mr\le\left(\frac{eM}{r}\right)^r,
\qquad
\binom{t-1}{r-1}\le\left(\frac{et}{r}\right)^r,
\]
we obtain
\[
\Pr[Z(S)\ge t]
\le
\alpha^t
\sum_{r=1}^t
\left(\frac{e^2Mt\alpha}{r^2}\right)^r.
\]
Because \(M\le\mu_+n\), \(t=O(s)\), and \(s\le O(w^2)\), there is a constant \(C\) for which
\[
\Pr[Z(S)\ge t]
\le
 t\left(\frac{C s^3w^2}{n}\right)^t
\le
 t\left(\frac{C' w^8}{n}\right)^{Ks}.
\]
Now union bound over all \(\binom ns\le(en/s)^s\) sets of size \(s\):
\[
\Pr[\exists S,|S|=s:Z(S)\ge Ks]
\le
 t\left[
 \frac{en}{s}
 \left(\frac{C'w^8}{n}\right)^K
 \right]^s.
\]
For any fixed \(K\ge3\), the bracket is \(n^{1-K}\operatorname{polylog}(n)=o(1)\). Summing over \(1\le s\le D_0=O(\log^2n)\) yields \(o(1)\). ∎

### Lemma 4.5 (uniform diffuse-family matching event)
With probability \(1-o(1)\), the following property holds simultaneously for every fixed-support system \((S_1,\dots,S_n)\) with \(|S_j|\le2\):

If every cell set \(T\) with
\[
|T|\le 2r,
\qquad r:=\lfloor aw\rfloor,
\]
is incident to at most \(\varepsilon n\) source coordinates, i.e.
\[
|\{j:S_j\cap T\neq\varnothing\}|\le\varepsilon n,
\]
then some random batch \(B_i\) contains \(r\) coordinates with pairwise disjoint supports.

**Proof.** First count relevant support systems. The union of all supports contains at most \(2n\) dynamic cells. Cells never belonging to any support are constant over the Boolean cube by Lemma 3.1 and can be compiled into the query algorithm. Relabel the at-most-\(2n\) support cells by \([2n]\). Each logical coordinate chooses a subset of size \(0,1\), or \(2\), so the number of labeled support systems is at most
\[
\left(1+2n+\binom{2n}{2}\right)^n
\le(3n^2)^n
=
\exp(2n\log n+O(n)).
\]

Fix one support system satisfying the diffuse condition. Expose one random batch as an ordered sample of \(w\) distinct coordinates and greedily accept a coordinate when its support is disjoint from all previously accepted supports. Before \(r\) acceptances, the union \(T\) of accepted supports has size at most \(2r\), so at most \(\varepsilon n\) source coordinates conflict with \(T\). Conditional on the past, a new draw is rejected with probability at most
\[
\frac{\varepsilon n}{n-w}\le2\varepsilon
\]
for large \(n\).

If fewer than \(r\) coordinates are accepted, at least \(w-r+1\ge(1-a)w\) draws are rejected. Hence
\[
\Pr[\text{matching size}<r]
\le
2^w(2\varepsilon)^{(1-a)w}
=
e^{-\Gamma w}.
\]
For all \(M\) independent batches to fail has probability at most
\[
e^{-\Gamma Mw}
\le
\exp(-\Gamma\mu_-c_-n\log n).
\]
Union bounding over all support systems gives
\[
\exp\left((2-\Gamma\mu_-c_-+o(1))n\log n\right)=o(1)
\]
by the choice \(\Gamma\mu_-c_->3\). ∎

---

## 5. A self-contained sketch-probe lemma

The hub case can be closed without importing the full Query-with-Sketch theorem. The following exact-product special case is enough and is stronger for the present application.

### Lemma 5.1 (independent-target sketch-probe bound)
Let
\[
X=(X_1,\dots,X_N)
\]
be independent group-valued random variables. Let
\[
F(X)=(Y_1,\dots,Y_m)\in\{0,1\}^m
\]
where the \(Y_\ell\) are independent unbiased bits and each \(Y_\ell\) is contained in a **distinct** input group \(X_{g(\ell)}\).

Consider any deterministic algorithm that:

1. receives an arbitrary \(s\)-bit sketch \(S(X)\);
2. adaptively probes whole input groups \(X_i\);
3. computes \(F(X)\) exactly.

Then for every integer \(c\ge1\), its average number \(D\) of group probes under the product distribution satisfies
\[
\boxed{
\mathbb E[D]
\ge
(1-2^{-c})(m-s-c)
}
\]
whenever \(m>s+c\).

In particular, with \(c=2\),
\[
\mathbb E[D]\ge\frac34(m-s-2).
\]

**Proof.** For each sketch value \(z\in\{0,1\}^s\), fix the adaptive decision tree followed when the sketch equals \(z\). Let
\[
t:=m-s-c.
\]
Consider a leaf of this tree reached after at most \(t\) group probes, with partial assignment \(\sigma\) to those probed groups and output \(y\in\{0,1\}^m\). Since at most \(t\) target groups have been revealed and the target groups are distinct, conditioned on \(\sigma\) at least \(m-t=s+c\) target bits remain independent and unbiased. Thus
\[
\Pr[F(X)=y\mid\sigma]\le2^{-(m-t)}=2^{-(s+c)}.
\]
Equivalently,
\[
\Pr[F(X)=y\wedge\sigma]
\le
2^{-(s+c)}\Pr[\sigma].
\]
For a fixed sketch tree, the cylinder events \(\sigma\) of distinct leaves are disjoint. Therefore the total probability mass of inputs that are both correct and halt within \(t\) probes in this tree is at most \(2^{-(s+c)}\). Summing over all at most \(2^s\) sketch values gives
\[
\Pr[\text{correct and }D\le t]\le2^{-c}.
\]
The algorithm is exact, so
\[
1\le\Pr[D>t]+2^{-c}.
\]
By Markov's inequality,
\[
\Pr[D>t]\le\frac{\mathbb E[D]}{t}.
\]
Hence
\[
\frac{\mathbb E[D]}{t}\ge1-2^{-c},
\]
which proves the claim. ∎

**Remark.** This is a specialized decision-tree-with-help-bits argument. It can also be viewed as a product-distribution exact-recovery specialization of modern Query-with-Sketch min-entropy machinery; no novelty claim is made for the lemma itself.

---

## 6. Diffuse/hub dichotomy

Fix a support system after the random family satisfies Lemmas 4.1–4.5.

### Case I: diffuse supports
Suppose every \(T\) with \(|T|\le2r\) is incident to at most \(\varepsilon n\) coordinates. By Lemma 4.5, some batch contains a matching of \(r=\lfloor aw\rfloor\) pairwise disjoint supports. Lemma 3.3 forces the adaptive query path to hit each support, hence
\[
q\ge r\ge \frac{a}{2}w
\]
for sufficiently large \(n\). Thus
\[
q=\Omega(w).
\]

### Case II: hub-concentrated supports
Otherwise there exists a cell set \(H\) with
\[
h:=|H|\le2r\le2aw
\]
that is incident to more than \(\varepsilon n\) logical coordinates.

#### Lemma 6.1 (active coordinates internal to the hub)
Let
\[
I_H:=\{j\in A:S_j\subseteq H\}.
\]
Then
\[
|I_H|\le hw.
\]

**Proof.** Fix all logical coordinates outside \(I_H\). By Lemma 3.1, varying \(x|_{I_H}\) can change only cells in \(H\). By active-coordinate injectivity (Lemma 3.2), the map from \(\{0,1\}^{I_H}\) to the \(hw\) hub bits must be injective. Therefore \(2^{|I_H|}\le2^{hw}\). ∎

For large \(n\), \(hw=O(w^2)=o(n)\). Lemma 4.1 also gives at most \(\varepsilon n/4\) inactive coordinates. Hence at least
\[
\varepsilon n-\frac{\varepsilon n}{4}-hw
\ge
\frac{\varepsilon n}{2}
=\delta n
\]
active coordinates incident to \(H\) have an essential support with exactly one endpoint in \(H\) and one outside. Call this crossing set \(C\).

For each nonhub cell \(v\notin H\), define the residual source group
\[
G_v:=\{j\in C:v\in S_j\}.
\]
The nonempty groups \(G_v\) partition \(C\).

#### Lemma 6.2 (residual group size)
For every nonhub cell \(v\),
\[
|G_v|\le(h+1)w\le D_0.
\]

**Proof.** Fix all logical coordinates outside \(G_v\). Varying \(G_v\) can change only cells in \(H\cup\{v\}\). Active-coordinate injectivity therefore gives
\[
2^{|G_v|}\le2^{(h+1)w}.
\]
The bound \((h+1)w\le(2aw+1)w=D_0\) follows from \(h\le2aw\). ∎

#### Lemma 6.3 (many batches touch many distinct residual groups)
There are \(\Theta(n)\) batches that each touch at least \(\kappa w\) distinct groups \(G_v\), where \(\kappa=\delta/4\).

**Proof.** By Lemma 4.3, at least \(M/2\) batches satisfy
\[
r_i:=|B_i\cap C|\ge\frac{\delta w}{2}.
\]
For batch \(i\), define its collision excess
\[
e_i:=\sum_v(|B_i\cap G_v|-1)_+.
\]
The number \(g_i\) of distinct groups touched inside \(C\) is
\[
g_i=r_i-e_i.
\]
Using Lemma 4.4 group-by-group and the fact that the groups partition \(C\),
\[
\sum_i e_i
=
\sum_v Z(G_v)
\le
K\sum_v|G_v|
=K|C|
\le Kn.
\]
Thus the number of batches with \(e_i>\delta w/4\) is at most
\[
\frac{4Kn}{\delta w}=o(n).
\]
Since \(M=\Theta(n)\), for large \(n\) a constant fraction of the \(M/2\) rich batches also satisfy \(e_i\le\delta w/4\). Every such batch has
\[
g_i\ge\frac{\delta w}{4}=\kappa w.
\]
∎

#### Lemma 6.4 (selection of group-disjoint batches)
For
\[
L:=\left\lceil\frac{4h}{\kappa}\right\rceil,
\]
there exist \(L\) batches among those from Lemma 6.3 whose touched residual-group sets are pairwise disjoint.

**Proof.** By Lemma 4.2 and Lemma 6.2, a fixed group \(G_v\) is touched by at most
\[
\sum_{j\in G_v}d_j
\le
\Delta w|G_v|
\le
\Delta(h+1)w^2
\]
batches. A candidate batch touches at most \(w\) groups, so selecting it eliminates at most
\[
\Delta(h+1)w^3
\]
other candidates through group conflicts. The initial candidate pool has \(\Theta(n)\) batches. Since
\[
L\cdot\Delta(h+1)w^3
=O(h(h+1)w^3)
=O(w^5)
=o(n),
\]
a greedy selection succeeds for all sufficiently large \(n\). ∎

---

## 7. Closing the hub case by the sketch-probe lemma

Select the \(L\) pairwise group-disjoint batches from Lemma 6.4. In each selected batch, choose one requested coordinate from each residual group it touches. Across all \(L\) batches this produces
\[
m\ge\kappa Lw
\]
requested source bits, each located in a distinct residual group.

Now define a hard distribution on logical states:

- all coordinates outside \(C\) are fixed to \(0\);
- coordinates in \(C\) are mutually independent unbiased bits.

For each nonempty residual group \(G_v\), define one raw input group
\[
X_v:=x|_{G_v},
\]
padding to a common alphabet length if desired. The \(X_v\)'s are independent.

Give the decoder the contents of all hub cells \(H\) for free. This is an
\[
s:=hw
\]
bit sketch of the residual input.

Whenever the original FBDG query probes a nonhub cell \(v\):

- if \(G_v\neq\varnothing\), reveal the whole raw group \(X_v\); by Lemma 3.1 and because all non-crossing logical bits are fixed, \(E_v(x)\) is a deterministic function of \(X_v\) and fixed constants;
- if \(G_v=\varnothing\), \(E_v(x)\) is constant under this distribution and can be supplied for free;
- hub-cell probes are answered from the sketch.

Thus the \(L\) original adaptive FBDG queries induce a deterministic exact sketch-probe algorithm for the \(m\) selected independent target bits using at most
\[
Lq
\]
raw-group probes in the worst case.

Apply Lemma 5.1 with \(c=2\):
\[
Lq
\ge
\frac34(m-s-2).
\]
Since
\[
m\ge\kappa Lw,
\qquad
s=hw,
\qquad
L\ge\frac{4h}{\kappa},
\]
we have
\[
\frac{s}{L}=\frac{hw}{L}\le\frac{\kappa w}{4}.
\]
Therefore
\[
q
\ge
\frac34\left(\kappa w-\frac{hw}{L}-\frac2L\right)
\ge
\frac{9\kappa}{16}w-o(w).
\]
In particular, for sufficiently large \(n\),
\[
q\ge\frac\kappa2 w.
\]
Since \(\kappa=\varepsilon/8\), the hub branch yields
\[
q\ge\frac{\varepsilon}{16}w
\]
for all sufficiently large \(n\), after harmless constant slack.

Combining the diffuse and hub cases proves Theorem 2.1. A safe explicit global constant is, for example,
\[
c_*:=\min\left\{\frac1{16},\frac{\varepsilon}{16}\right\},
\]
where \(\varepsilon\) is any fixed constant satisfying the diffuse union-bound inequality above.

---

## 8. Dependency DAG

```text
THEOREM 2.1: random fixed-support nonlinear u=2 => q = Ω(w)
│
├── Deterministic model
│   ├── Lemma 3.1 cell-local dependence
│   ├── Lemma 3.2 active-coordinate injectivity
│   └── Lemma 3.3 adaptive hitting
│
├── Random-family events
│   ├── Lemma 4.1 almost-all-active
│   ├── Lemma 4.2 max source degree O(w)
│   ├── Lemma 4.3 uniform large-set richness
│   ├── Lemma 4.4 uniform small-set spreading
│   └── Lemma 4.5 uniform diffuse matching
│
└── Dichotomy
    ├── Diffuse
    │   └── Lemma 4.5 + Lemma 3.3 => q = Ω(w)
    │
    └── Hub
        ├── Lemma 6.1 hub internal capacity
        ├── crossing set |C| = Ω(n)
        ├── Lemma 6.2 residual groups size O(w^2)
        ├── Lemma 6.3 many group-rich batches
        ├── Lemma 6.4 select L = Θ(h) group-disjoint batches
        ├── Lemma 5.1 independent-target sketch-probe bound
        └── Lq >= Ω(Lw) => q = Ω(w)
```

---

## 9. Counterexample/defect ledger incorporated into the repair

1. **Spreading alone does not imply group-disjoint batches.**  
   Counterexample: two batches may each touch the same singleton residual group once; the excess statistic is zero but the batches are not group-disjoint.  
   **Repair:** add the uniform source-degree event and a greedy conflict bound (Lemma 6.4).

2. **An unspecified statement `L=Theta(h)` is insufficient when using a sketch lemma.**  
   If \(h=1,L=1\), an \(s=w\)-bit sketch may encode an entire \(w\)-bit target.  
   **Repair:** choose the constant explicitly, here \(L=\lceil4h/\kappa\rceil\).

3. **Injectivity cannot be applied to coordinates never appearing in any query.**  
   An inactive logical coordinate need not be represented.  
   **Repair:** separate the active set \(A\), prove that only \(o(n)\) random-family coordinates are inactive, and apply all capacity arguments to active coordinates.

4. **Dummy support locations can break structural interpretation.**  
   **Repair:** define \(S_j\) as the essential support induced by the canonical encoding.

5. **The proof cannot be transferred to moving/state-dependent support.**  
   The static cell-dependency relation, support graph, hub set, and residual partition all use fixed supports essentially. The moving-support case remains `OPEN`.

---

## 10. Exact frontier preserved

The current theorem landscape remains:
\[
\boxed{
\begin{array}{ll}
\text{structured fixed-support }u=2 &: q=O(1),\\[3pt]
\text{random fixed-support }u=2 &: q=\Omega(w),\\[3pt]
\text{unrestricted moving/history-dependent }u=2 &: \Omega(w/\log w)\text{ known, }\Omega(w)\text{ OPEN}.
\end{array}
}
\]

This package proves only the middle line.

---

## 11. Relation to Query-with-Sketch

The recent Query-with-Sketch framework of Garg, He, Li, Papakonstantinou, and Yang (arXiv:2609.18024, 2026) allows an arbitrary sketch and adaptive input probes and derives probe lower bounds from conditional min-entropy. It can be used to close the hub case after choosing enough group-disjoint batches.

For the present theorem, however, the residual input distribution is a direct product and the selected output contains one independent unbiased target bit from each of distinct groups. Lemma 5.1 gives a shorter self-contained exact-recovery argument and a stronger constant. The paper should therefore present Lemma 5.1 as the main proof tool and cite Query-with-Sketch as closely related general methodology, without claiming the sketch-probe principle itself as novel.

---

## 12. Evidence ledger

| Claim | State | Basis |
|---|---|---|
| Cell-local dependence under canonical fixed support | `PROVED` | Lemma 3.1 |
| Adaptive hitting lemma | `PROVED` | Lemma 3.3 |
| Uniform diffuse matching event | `PROVED` | Lemma 4.5 |
| Uniform small-set spreading | `PROVED` | Lemma 4.4 |
| Hub internal capacity | `PROVED` | Lemma 6.1 |
| Residual group size bound | `PROVED` | Lemma 6.2 |
| Existence of Θ(h) group-disjoint rich batches | `PROVED` | Lemmas 4.2–4.4, 6.3–6.4 |
| Adaptive sketch-probe lower bound for selected targets | `PROVED` | Lemma 5.1 |
| Random fixed-support nonlinear u=2 lower bound q=Ω(w) | `PROVED` | Theorem 2.1 |
| Extension to moving/state-dependent supports | `OPEN` | fixed support used essentially |
| Novelty of theorem | `LIKELY DISTINCT WITHIN SEARCH SCOPE` | preserve prior-art audit label |

---

## 13. Manuscript instructions for the writing stage

The paper should state the main theorem with **canonicality** and **fixed essential supports** explicitly. It should not describe the result as an unrestricted dynamic cell-probe lower bound. The hub proof should use the self-contained sketch-probe Lemma 5.1, while Query-with-Sketch is positioned as neighboring general methodology.

The novelty wording should remain bounded:

> Within the literature searched as of October 2026, we did not identify a materially equivalent lower bound for exact fixed-batch dynamic retrieval showing that random Θ(log n)-uniform batch families require Ω(log n) adaptive word probes under two fixed update locations per source coordinate, even with arbitrary nonlinear cell contents. The result applies to canonical fixed-support encodings; removing fixed support remains open.

