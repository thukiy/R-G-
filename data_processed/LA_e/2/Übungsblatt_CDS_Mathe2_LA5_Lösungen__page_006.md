<|ref|>sub_title<|/ref|><|det|>[[114, 81, 490, 100]]<|/det|>
## 4. Aussagen über lineare Abbildungen 

<|ref|>text<|/ref|><|det|>[[114, 98, 680, 116]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[114, 113, 879, 320]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Jede Abbildung der Form \(a: \mathbb{R}^m \to \mathbb{R}^n\) kann durch eine \(n \times m\) Matrix dargestellt werden.</td><td></td><td>X</td></tr><tr><td>b) Jede Abbildung der Form \(a: \mathbb{R}^n \to \mathbb{R}^m\) kann durch eine quadratische Matrix dargestellt werden.</td><td>X</td><td></td></tr><tr><td>c) Die Funktion \(f: \mathbb{R} \to \mathbb{R}\) mit \(f(x) = 2x\) ist eine lineare Abbildung im Sinne der linearen Algebra.</td><td>X</td><td></td></tr><tr><td>d) Die Funktion \(f: \mathbb{R} \to \mathbb{R}\) mit \(f'(x) = 3x + 2\) ist eine lineare Abbildung im Sinne der linearen Algebra.</td><td></td><td>X</td></tr><tr><td>e) Für jede lineare Abbildung \(a: \mathbb{R}^m \to \mathbb{R}^n\) gilt: \(a(0) = 0\).</td><td>X</td><td></td></tr><tr><td>f) Eine lineare Abbildung ist genau dann umkehrbar, wenn sie durch eine reguläre Matrix beschrieben wird.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[114, 335, 355, 352]]<|/det|>
## 5. 2x2 Standardmatrizen 

<|ref|>text<|/ref|><|det|>[[114, 351, 770, 370]]<|/det|>
Untersuchen Sie die geometrische Wirkung der jeweiligen 2x2 Matrix auf 

<|ref|>text<|/ref|><|det|>[[114, 368, 872, 433]]<|/det|>
(Spalten)Vektoren. Betrachten Sie die Einheitsvektoren \(\hat{e}_x = \begin{pmatrix} 1 \\ 0 \end{pmatrix}\) und \(\hat{e}_y = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\) sowie einen weiteren selbst gewählten Vektor. Veranschaulichen Sie die Ergebnisse in einem xy-Diagramm. 

<|ref|>equation<|/ref|><|det|>[[114, 428, 820, 520]]<|/det|>
\[ \begin{align*} a) \mathbb{E} &= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} && b) P &= \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} && c) Z_3 = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} \\ d) P_x &= \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} && e) P_y &= \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} && f) A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} \\ g) S_x &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} && h) S_y &= \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} && i) \mathbb{I} &= \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \end{align*} \]

<|ref|>text<|/ref|><|det|>[[114, 550, 144, 567]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[120, 570, 580, 612]]<|/det|>
\[ \frac{1 \cdot \hat{e}_x}{1} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \cdot 1 + 0 \cdot 0 \\ 0 \cdot 1 + 1 \cdot 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \hat{e}_x \]

<|ref|>equation<|/ref|><|det|>[[120, 615, 580, 657]]<|/det|>
\[ \frac{1 \cdot \hat{e}_y}{1} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \cdot 0 + 0 \cdot 1 \\ 0 \cdot 0 + 1 \cdot 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \hat{e}_y \]

<|ref|>equation<|/ref|><|det|>[[120, 657, 576, 698]]<|/det|>
\[ \frac{1 \cdot \mathbf{u}}{1} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \mathbf{u} \end{bmatrix} \cdot \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \cdot 3 + 0 \cdot 2 \\ 0 \cdot 3 + 1 \cdot 2 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \mathbf{u}_x \]

<|ref|>image<|/ref|><|det|>[[114, 694, 652, 819]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 821, 857, 856]]<|/det|>
Die Einheitsmatrix überführt jeden Vektor in sich selbst und stellt somit die Identität dar.