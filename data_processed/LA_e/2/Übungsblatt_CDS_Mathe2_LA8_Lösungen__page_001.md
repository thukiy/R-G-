<|ref|>title<|/ref|><|det|>[[115, 183, 456, 217]]<|/det|>
Übungsblatt LA 8 

<|ref|>text<|/ref|><|det|>[[576, 196, 880, 232]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 277]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 257, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 875, 370]]<|/det|>
- Sie kennen die Begriffe charakteristisches Polynom, charakteristische Gleichung, Eigenwert, Eigenvektor, Spektrum und Eigenraum und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 369, 848, 403]]<|/det|>
- Sie können das charakteristische Polynom, die Eigenwerte und Eigenvektoren einer quadratischen Matrix berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 402, 866, 437]]<|/det|>
- Sie können die Eigenschaften einer Matrix bzw. linearen Abbildung anhand ihrer Eigenwerte/Eigenvektoren beurteilen und umgekehrt. 

<|ref|>sub_title<|/ref|><|det|>[[115, 468, 540, 485]]<|/det|>
1. Aussagen über Eigenwerte und -vektoren 

<|ref|>text<|/ref|><|det|>[[115, 485, 680, 502]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 500, 880, 672]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Jede quadratische Matrix hat mindestens einen reellen Eigenwert.</td><td></td><td>X</td></tr><tr><td>b) Sind \(\vec{v}\) und \(\vec{w}\) zwei Eigenvektoren einer Matrix, dann gilt dies auch für \(\vec{u} = \vec{v} + \vec{w}\).</td><td></td><td>X</td></tr><tr><td>c) Sind \(\vec{v}\) und \(\vec{w}\) zwei Eigenvektoren einer Matrix zum selben Eigenwert \(\lambda\), dann gilt dies auch für \(\vec{u} = \vec{v} + \vec{w}\).<br/>d) Eine 3x3 Matrix hat maximal drei verschiedene Eigenwerte.</td><td>X</td><td></td></tr><tr><td>e) Gilt \(\text{spec}(A) = \{0\}\), dann gilt: \(\text{tr}(A) = 0\).</td><td></td><td>X</td></tr><tr><td>f) Gilt \(0 \in \text{spec}(A)\), dann gilt: \(\text{det}(A) = 0\).</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 688, 655, 705]]<|/det|>
2. Eigenwerte und -vektoren der Standardmatrizen in 2D 

<|ref|>text<|/ref|><|det|>[[115, 704, 707, 722]]<|/det|>
Betrachten Sie die Standardmatrizen E, \(\mathbb{I}\), P, \(\mathbb{Z}_a\), \(\mathbb{P}_x\), \(\mathbb{P}_y\), \(\mathbb{S}_x\) und \(\mathbb{S}_y\). 

<|ref|>text<|/ref|><|det|>[[115, 721, 870, 755]]<|/det|>
a) Welche reellen Eigenwerte und Eigenvektoren der Standardmatrizen können Sie ohne zu rechnen angeben? 

<|ref|>text<|/ref|><|det|>[[115, 754, 878, 789]]<|/det|>
b) Berechnen Sie das charakteristische Polynom, die Eigenwerte und Eigenvektoren der Standardmatrizen. 

<|ref|>text<|/ref|><|det|>[[115, 806, 141, 822]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 821, 833, 870]]<|/det|>
Die Matrix \(\mathbb{1}\) beschreibt die Identität auf \(\mathbb{R}^2\), die jeden Vektor auf sich selber abbildet. Dies entspricht bei allen Vektoren in \(\mathbb{R}^2\) genau der Multiplikation mit der reellen Zahl 1. Demnach gilt 

<|ref|>equation<|/ref|><|det|>[[333, 877, 612, 898]]<|/det|>
\[ \text{spec}(\mathbb{1}) = \{1\} \quad \text{und} \quad E_1(\mathbb{1}) = \mathbb{R}^2. \]