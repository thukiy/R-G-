<|ref|>title<|/ref|><|det|>[[115, 181, 476, 216]]<|/det|>
Übungsblatt LA 10 

<|ref|>text<|/ref|><|det|>[[578, 195, 880, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 249, 270, 278]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 256, 880, 274]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 857, 371]]<|/det|>
- Sie kennen die Begriffe Bild, Kern, algebraische und geometrische Vielfachheit, ähnliche Matrix, Diagonalisierbarkeit einer Matrix und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 369, 707, 387]]<|/det|>
- Sie können Bild und Kern einer linearen Abbildung berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 386, 831, 421]]<|/det|>
- Sie können bestimmen, ob eine Matrix diagonalisierbar ist oder nicht und die Diagonalmatrix angeben. 

<|ref|>sub_title<|/ref|><|det|>[[115, 452, 427, 470]]<|/det|>
1. Aussagen über Bild und Kern 

<|ref|>text<|/ref|><|det|>[[115, 469, 386, 486]]<|/det|>
Gegeben sei eine mxn Matrix. 

<|ref|>text<|/ref|><|det|>[[115, 485, 680, 503]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 501, 880, 628]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Es gilt: \(\ker(A) \neq \emptyset\).</td><td>X</td><td></td></tr><tr><td>b) Für \(m = 2\) und \(n = 3\) gilt: \(\ker(A) \neq \{0\}\).</td><td>X</td><td></td></tr><tr><td>c) Für \(m = 3\) und \(n = 2\) gilt: \(\ker(A) \neq \{0\}\).</td><td>X</td><td>X</td></tr><tr><td>d) Für \(n = m\) und \(A\) regulär gilt: \(\ker(A) \neq \{0\}\).</td><td>X</td><td>X</td><td></td></tr><tr><td>e) Für \(n = m\) und \(A\) singulär gilt: \(\ker(A) \neq \{0\}\).</td><td>X</td><td>X<td></td></td></tr><tr><td>f) Für \(m = 3\) und \(n = 4\) gilt: \(\dim(\ker(A)) + \dim(\img(A)) = 7\).</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 643, 385, 660]]<|/det|>
2. Bild und Kern berechnen 

<|ref|>text<|/ref|><|det|>[[115, 659, 650, 677]]<|/det|>
Berechnen Sie jeweils Bild und Kern der gegebenen Matrix. 

<|ref|>equation<|/ref|><|det|>[[115, 679, 810, 770]]<|/det|>
\[
\begin{align*}
a) \begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix} \qquad b) \begin{pmatrix} 2 & 3 \\ 4 & 6 \end{pmatrix} \qquad c) \begin{pmatrix} 0 & -3 & 2 \\ 3 & 0 & -1 \\ -2 & 1 & 0 \end{pmatrix} \\
d) \begin{pmatrix} -2 & 4 & 8 \\ 1 & -2 & -4 \end{pmatrix} \qquad e) \begin{pmatrix} -2 & 4 & 8 \\ 1 & -2 \end{pmatrix} \qquad f) \begin{pmatrix} -2 & 4 & 8 \\ 8 & 0 \end{pmatrix}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 784, 142, 800]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[120, 799, 352, 815]]<|/det|>
Wir betrachten die Matrix 

<|ref|>equation<|/ref|><|det|>[[431, 828, 561, 867]]<|/det|>
\[
A = \begin{bmatrix} 2 & 3 \\ 4 & 5 \end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[115, 878, 485, 895]]<|/det|>
Offensichtlich ist A quadratisch und es gilt 

<|ref|>equation<|/ref|><|det|>[[315, 907, 678, 927]]<|/det|>
\[
\det(A) = 2 \cdot 5 - 4 \cdot 3 = 10 - 12 = -2 \neq 0.
\]