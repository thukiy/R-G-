<|ref|>sub_title<|/ref|><|det|>[[115, 183, 456, 219]]<|/det|>
Übungsblatt LA 4 

<|ref|>text<|/ref|><|det|>[[576, 196, 880, 232]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 278]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 256, 880, 274]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 880, 405]]<|/det|>
- Sie kennen die Begriffe Matrix, symmetrische/schiefsymmetrische Matrix, Einheitsmatrix, inverse Matrix, Transposition und deren wichtigste Eigenschaften.
- Sie können Matrizen addieren, subtrahieren und mit einem Skalar bzw. mit einer anderen Matrix multiplizieren und bestimmen, ob diese Operationen für gegebene Matrizen durchführbar sind oder nicht. 

<|ref|>sub_title<|/ref|><|det|>[[115, 436, 377, 454]]<|/det|>
1. Aussagen über Matrizen 

<|ref|>text<|/ref|><|det|>[[115, 453, 680, 470]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 468, 880, 830]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Eine reelle 2 x 3 Matrix besteht aus 2 Zeilen und 3 Spalten.</td><td>X</td><td></td></tr><tr><td>b) Eine reelle Zahl \(x \in \mathbb{R}\) kann als 1 x 1 Matrix aufgefasst werden.</td><td>X</td><td></td></tr><tr><td>c) Ein Vektor \(\vec{v} \in \mathbb{R}^3\) kann als reelle 3 x 1 Matrix interpretiert werden.</td><td>X</td><td></td></tr><tr><td>d) Eine reelle 2 x 3 Matrix hat 8 Komponenten.</td><td></td><td>X</td></tr><tr><td>e) Wenn A eine 2123 x 8248 Matrix ist und B eine 8248 x 9178 Matrix, dann ist die Summe A+B definiert.</td><td></td><td>X</td></tr><tr><td>f) Wenn A eine 2123 x 8248 Matrix ist und B eine 8248x 9178 Matrix, dann ist das Produkt A·B definiert.</td><td>X</td><td></td></tr><tr><td>g) Wenn \(\vec{u}\) und \(\vec{v}\) zwei Vektoren sind, dann ist das Produkt \(\vec{v} \cdot \vec{u}^T\) definiert.</td><td>X</td><td></td></tr><tr><td>h) Für zwei beliebige quadratische n x n Matrizen gilt: A·B=B·A.</td><td></td><td>X</td></tr><tr><td>i) Für jede beliebige Matrix gilt: \(((A^T)^T)^T = (A^T)^T\).</td><td>X</td><td></td></tr><tr><td>j) Hat eine Matrix genau 13 Komponenten, so handelt es sich entweder um eine 13 x 1 oder eine 1 x 13 Matrix.</td><td>X</td><td></td></tr><tr><td>k) Wenn A eine 16 x 20 Matrix und B eine 16 x 30 Matrix ist, dann ist das Produkt A^T·B definiert.</td><td>X</td><td></td></tr><tr><td>l) Für 2 beliebige 2 x 2 Matrizen A und B mit A≠B gilt: A·B≠B·A.</td><td></td><td>X</td></tr><tr><td>m) Ist eine 2 x 2 Matrix sowohl symmetrisch als auch schiefsymmetrisch, dann gilt: A=0.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 845, 616, 863]]<|/det|>
2. Addition, Subtraktion, Transposition mit Matrizen 

<|ref|>text<|/ref|><|det|>[[115, 862, 744, 879]]<|/det|>
Berechnen Sie die folgenden Ausdrücke mit den gegebenen Matrizen. 

<|ref|>equation<|/ref|><|det|>[[330, 883, 664, 919]]<|/det|>
\[A = \begin{pmatrix} 1 & 3 & -1 \\ 4 & -2 & 8 \end{pmatrix}, \quad B = \begin{pmatrix} -3 & 9 & 3 \\ -6 & 6 & 3 \end{pmatrix}\]