<|ref|>sub_title<|/ref|><|det|>[[114, 98, 387, 116]]<|/det|>
## 6. Bild und Kern berechnen 

<|ref|>text<|/ref|><|det|>[[114, 115, 650, 134]]<|/det|>
Berechnen Sie jeweils Bild und Kern der gegebenen Matrix. 

<|ref|>equation<|/ref|><|det|>[[114, 134, 810, 228]]<|/det|>
\[
\begin{align*}
a) \begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix} \qquad b) \begin{pmatrix} 2 & 3 \\ 4 & 6 \end{pmatrix} \qquad c) \begin{pmatrix} 0 & -3 & 8 \\ 3 & 0 & -1 \\ -2 & 1 & 0 \end{pmatrix} \\
d) \begin{pmatrix} -2 & 4 & 8 \\ 1 & -2 & -4 \end{pmatrix} \qquad e) \begin{pmatrix} -2 & 4 & 8 \\ 1 & -2& 0 \end{pmatrix} \qquad f) \begin{pmatrix} -2 & 1 \\ 4 & -2 \\ 8 & 0 \end{pmatrix}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 241, 145, 258]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 255, 352, 273]]<|/det|>
Wir betrachten die Matrix 

<|ref|>equation<|/ref|><|det|>[[430, 284, 562, 325]]<|/det|>
\[
A = \begin{bmatrix} 2 & 3 \\ 4 & 5 \end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[114, 334, 485, 352]]<|/det|>
Offensichtlich ist A quadratisch und es gilt 

<|ref|>equation<|/ref|><|det|>[[315, 364, 677, 383]]<|/det|>
\[
\det(A) = 2 \cdot 5 - 4 \cdot 3 = 10 - 12 = -2 \neq 0.
\]

<|ref|>text<|/ref|><|det|>[[114, 394, 415, 413]]<|/det|>
Demnach ist A regulär und es gilt 

<|ref|>equation<|/ref|><|det|>[[344, 424, 650, 447]]<|/det|>
\[
\ker(A) = \{0\} \quad \text{und} \quad \img(A) = \mathbb{R}^2.
\]

<|ref|>text<|/ref|><|det|>[[114, 450, 145, 467]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 465, 875, 500]]<|/det|>
Wir erzeugen mit dem Gauß-Jordan-Verfahren reduzierte Stufenform (aus A ergeben
sich die Vektoren im Kern, aus Aᵀ das Bild von A): 

<|ref|>equation<|/ref|><|det|>[[114, 499, 520, 589]]<|/det|>
\[
\begin{align*}
A: \begin{bmatrix} 2 & 3 \\ 4 & 6 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & 3 \\ 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 3 \\ 0 & 0 \end{bmatrix} \\
A^T: \begin{bmatrix} 2 & 4 \\ 3 & 6 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 2 \\ 1 & 2 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 \\ 1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 590, 692, 609]]<|/det|>
ker(A) enthält alle die Vektoren, die folgende Gleichung erfüllen: 

<|ref|>equation<|/ref|><|det|>[[119, 608, 400, 644]]<|/det|>
\[
1 \cdot x + \frac{3}{2} \cdot y = 0 \Rightarrow x = -\frac{3}{2} \cdot y
\]

<|ref|>equation<|/ref|><|det|>[[119, 652, 700, 700]]<|/det|>
\[
\ker(A) = \left\{ \begin{bmatrix} -\frac{3}{2}y \\ y \end{bmatrix} \in \mathbb{R}^2 \right\} = \operatorname{span} \left\{ \begin{bmatrix} -\frac{3}{2} \\ 1 \end{bmatrix} \right\} = \operatorname{span} \left\{ \begin{bmatrix} 3 \\ -2 \end{bmatrix} \right\}
\]

<|ref|>text<|/ref|><|det|>[[114, 700, 384, 718]]<|/det|>
Für das Bild von A ergibt sich 

<|ref|>equation<|/ref|><|det|>[[119, 720, 339, 762]]<|/det|>
\[
\operatorname{img}(A) = \operatorname{span} \left\{ \begin{bmatrix} 1 \\ 2 \end{bmatrix} \right\}
\]