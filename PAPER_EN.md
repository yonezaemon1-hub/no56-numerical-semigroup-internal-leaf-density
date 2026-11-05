---
title: "Internal–Leaf Inequalities and a Positive Limiting Leaf Density for Numerical Semigroups with Frobenius Number $2m+3$"
author: "Ryutaro Yonezu — Independent Researcher"
date: "5 November 2026 - v1.0"
abstract: |
  For numerical semigroups of multiplicity m >= 6 and Frobenius number F=2m+3,
  we study the counts I_m and L_m of internal nodes and leaves in the full numerical-semigroup tree.
  A seven-configuration model gives the known total N_m=7*2^(m-4), and local sumset conditions yield
  the inequalities I_m >= 3 L_m for m >= 6 and I_m >= 5 L_m for m >= 12.
  The factor 3 is attained at m=6; the latter threshold is the least one for which the
  factor-5 inequality holds for all larger m, although it also holds at m=10.
  The leaf proportion L_m/N_m tends to a positive constant c with an explicit exponential error bound,
  and rigorous conditional-Harris estimates give 0.1314883 < c < 0.1446435.
  These statements are a fixed-family strengthening of Conjecture 41 of Casas, Madrid and Rosales.
  AI-assisted proof review and independent computations are reported with precise scope;
  this work has not undergone human peer review and theorem-level novelty is not established.
---

**No.56 - v1.0 preprint.** Not human peer-reviewed. Independent AI audit: PASS within its author-reported scope. References: PARTIAL. Novelty: INCONCLUSIVE. Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.

**DOI:** <https://doi.org/10.5281/zenodo.23981119>

# Introduction

The full tree of numerical semigroups has a child for each minimal generator above the Frobenius number that can be deleted. Casas, Madrid and Rosales [1, Conjecture 41] conjecture that, for fixed admissible multiplicity and Frobenius number, the number of internal semigroups is no smaller than the number of leaves. Here we focus on the infinite subfamily

$$F=2m+3,\qquad m\ge6.$$

Write $N_m$, $I_m$, and $L_m$ for the total number of such semigroups and the numbers of internal semigroups and leaves *in the full tree*. Thus $N_m=I_m+L_m$. We establish two strengthened comparisons and a limiting positive leaf proportion, using the same elementary membership-bit model. The total-count formula is **known** and is not advanced as a novelty claim. The `leaf-discriminating trees` of [2] are specially pruned enumeration trees, and their leaves must not be identified with the leaves in the full tree used here.

# Seven configurations and the exact leaf criterion

Let $S$ be a numerical semigroup with multiplicity $m$ and Frobenius number $2m+3$. All positive integers below $m$ and the integer $m+3$ are absent, while $m,2m$ and all integers above $F$ are present. Let

$$a_i=\mathbf1_{\{m+i\in S\}}\quad(i=1,2),\qquad b_i=\mathbf1_{\{2m+i\in S\}}\quad(i=1,2),$$

and $X_i=\mathbf1_{\{m+i\in S\}}$ for $4\le i\le m-1$. The closure conditions on $(a_1,a_2;b_1,b_2)$ are exactly:

* $(a_1,a_2)=(0,0)$: any $(b_1,b_2)$ (four possibilities);
* $(a_1,a_2)=(1,0)$: $(b_1,b_2)=(1,1)$ (one possibility);
* $(a_1,a_2)=(0,1)$: $b_2=1$, with $b_1$ free (two possibilities).

The remaining $m-4$ bits are unrestricted. Thus

$$\boxed{N_m=7\,2^{m-4}.} \tag{1}$$

This elementary specialization is compatible with the earlier multiparameter counts [2].

A positive element $x>F$ is a minimal generator precisely when it cannot be written as a sum of two positive elements of $S$. All such candidates belong to $[F+1,F+m]=[2m+4,3m+3]$. Consequently, $S$ is a leaf precisely when all $m$ integers in that interval have such a decomposition.

# Prefix probabilities and finite inequalities

Give the seven initial configurations equal weight. After marginalizing out $b_1,b_2$, the probabilities of $(X_1,X_2)=(0,0),(1,0),(0,1)$ are $4/7,1/7,2/7$, respectively; set $X_3=0$. Independently select $X_4,X_5,\ldots$ as fair bits. Define the increasing events

$$E_k=\{X_k=1\}\cup\{\exists\ i,j\ge1:\ i+j=k,\ X_i=X_j=1\},\qquad k\ge4,$$

$$Q_r=\Pr\left(\bigcap_{k=4}^r E_k\right). \tag{2}$$

For $4\le k\le m-1$, decomposability of $2m+k$ is equivalent to $E_k$. The condition for $3m$ is automatic, while the three terminal integers $3m+1,3m+2,3m+3$ require separate checks. Thus, writing $p_m=L_m/N_m$,

$$p_m\le Q_{m-1}\qquad(m\ge7),\qquad Q_{r+1}\le Q_r. \tag{3}$$

**Theorem A (finite internal–leaf bounds).** For the full numerical-semigroup tree,

$$\boxed{I_m\ge3L_m\quad(m\ge6),}\qquad
\boxed{I_m\ge5L_m\quad(m\ge12).} \tag{4}$$

*Proof.* The exact small certificates in the reproducibility code give

$$Q_6=\frac{13}{56}<\frac14,\qquad Q_{12}=\frac{596}{3584}=\frac{149}{896}<\frac16.$$

For $m\ge7$, (3) gives $p_m<1/4$, implying $I_m\ge3L_m$. At $m=6$, $(I_6,L_6)=(21,7)$. For $m\ge13$, (3) gives $p_m<1/6$, implying $I_m\ge5L_m$. Direct finite counting establishes the $m=12$ case, $(I_{12},L_{12})=(1508,284)$. The threshold 12 is minimal in the *eventual* sense because $(I_{11},L_{11})=(744,152)$ violates $I\ge5L$. The inequality does hold at $m=10$; therefore 12 is not asserted to be the first individual successful value. The factor 3 is attained at $m=6$. $\square$

# Positive limiting leaf density

For $k\ge9$, select $t(k)=\lfloor(k-1)/2\rfloor-3$ disjoint pairs $(i,k-i)$ with $4\le i<k-i$. They involve independent fair bits; $X_k$ is independent of all selected pairs. Failure of $E_k$ requires $X_k=0$ and every selected pair to fail. Therefore

$$\Pr(E_k^c)\le u_k:=\frac12\left(\frac34\right)^{\lfloor(k-1)/2\rfloor-3}. \tag{5}$$

The series $\sum_{k\ge9}u_k$ converges. The decreasing sequence $(Q_r)$ therefore has a limit $c\ge0$. The three terminal decomposability checks can be bounded using disjoint index pairs within $4,\ldots,m-1$, yielding

$$0\le Q_{m-1}-p_m\le3\left(\frac34\right)^{\lfloor m/2\rfloor-3}\quad(m\ge9). \tag{6}$$

Summing (5) over the infinite tail gives

$$0\le Q_{m-1}-c\le4\left(\frac34\right)^{\lfloor(m-1)/2\rfloor-3}. \tag{7}$$

Because both $p_m$ and $c$ lie below $Q_{m-1}$, the larger of the two deviations in (6)–(7), **not their sum**, bounds $|p_m-c|$. Therefore

$$\boxed{\left|\frac{L_m}{N_m}-c\right|\le4\left(\frac34\right)^{\lfloor(m-1)/2\rfloor-3}\quad(m\ge9).} \tag{8}$$

This explicit bound is intentionally conservative: at moderate $m$ it can be numerically weak. It establishes exponential convergence but does not by itself imply that the values at $m\approx20$ closely approximate $c$.

It remains to show $c>0$. **Harris's inequality is applied only after conditioning on the initial $(X_1,X_2)$ pair.** Within each such conditional distribution, the remaining bits are independent and the $E_k$ are increasing events. One can multiply the positive finite-prefix probability by product lower bounds for the subsequent increasing events. Since $\sum u_k$ converges, those products remain positive after a sufficiently long prefix. Averaging over the three initial pairs then gives $c>0$. Applying Harris directly to the unconditional mixture would not be justified.

**Theorem B (limit and quantitative estimate).** The limiting leaf proportion $c=\lim_{m\to\infty}p_m$ exists, is strictly positive, and satisfies (8).

# Certified numerical enclosure

A separate incremental count yields

$$Q_{32}=\frac{543583947}{3758096384}.$$

Using the conditional Harris inequality for $33\le k\le70$ and the union bound on the remaining tail,

$$Q_{32}\prod_{k=33}^{70}(1-u_k)\left(1-4\left(\frac34\right)^{32}\right)\le c\le Q_{32}. \tag{9}$$

Exact rational arithmetic verifies the strict decimal enclosure

$$\boxed{0.1314883<c<0.1446435.} \tag{10}$$

The supplied interval verifier checks the arithmetic in (9) conditional on the stated $Q_{32}$. The C++ verifier separately computes $Q_{32}$; a user-reported independent AI auditor additionally reproduced that count with a separately written C++ implementation.

# Reproducibility and verification scope

The original three source verifiers are preserved byte-for-byte in `repro/`. The Python explicit-membership implementation checks $(N_m,L_m)$ for $m=6,\ldots,15$ and finite prefix counts; the C++17 sumset implementation checks $m=6,\ldots,24$ and computes $Q_{32}$. A separate independent AI audit, reported by the author, used Linux, wrote an unrestricted enumeration of numerical semigroups for $m=6,\ldots,22$, independently checked prefix counts, and reviewed the conditional Harris reasoning; its verdict within scope was PASS. This was **AI review, not human peer review**.

On 5 November 2026, the author supplied a Windows PowerShell 5.1 transcript reporting successful Python and compiled C++ runs on an unchanged original v0.1 ZIP. The full log is retained in the private audit archive. Its SHA256, verified against the author's stated SHA256, is:

```text
b3d94afab5686bedeb23b1f961b5b69830faa008284127ff776e2677d0b49fee
```

The raw log is deliberately **not included** in this public reproducibility package because it contains host and local-user identifiers. A matching SHA256 verifies the submitted file's bytes against the reported hash; it does not independently authenticate the entire machine execution process.

# Limits and originality status

The result is presented as a *fixed-family strengthening* of Conjecture 41 in [1], not a solution to that conjecture for arbitrary $(m,F)$. The counting formula (1), Harris's inequality, and related sumset probability techniques are not claimed new. Our full-tree leaves are not the specially defined leaves of the leaf-discriminating enumeration trees of [2]. The scope of [3] is the genus-indexed tree, and [4] concerns shapes of random semigroups selected by genus or Frobenius number; neither comparison establishes a comprehensive novelty clearance. **REFERENCES PARTIAL; NOVELTY INCONCLUSIVE.** No human peer review has occurred. All rights reserved.

# References

[1] M. Casas, J. A. Madrid, and J. C. Rosales, *Internal numerical semigroups*, arXiv:2608.19984v1 (2026), especially Conjecture 41. <https://arxiv.org/html/2608.19984v1>

[2] M. Bras-Amorós and V. Torra, *Multiparameter counting of numerical semigroups: recurrences and leaf-discriminating trees*, arXiv:2607.23111v3 (2026). <https://arxiv.org/html/2607.23111v3>

[3] E. O'Dorney, *Degree asymptotics of the numerical semigroup tree*, *Semigroup Forum* **87**(3) (2013), 601–616, DOI: 10.1007/s00233-013-9486-7; corrected arXiv version: 2403.13120 (2024). <https://arxiv.org/abs/2403.13120>

[4] M. Bras-Amorós, N. Kaplan, and D. Singhal, *The shape of a random numerical semigroup*, arXiv:2604.26127v1 (2026). <https://arxiv.org/html/2604.26127v1>

[5] T. E. Harris, *A lower bound for the critical probability in a certain percolation process*, *Proc. Cambridge Philos. Soc.* **56**(1) (1960), 13–20, DOI: 10.1017/S0305004100034241. (The known positive-association inequality is used conditionally.)
