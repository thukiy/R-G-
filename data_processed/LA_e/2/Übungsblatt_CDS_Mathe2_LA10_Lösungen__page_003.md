<|ref|>text<|/ref|><|det|>[[114, 83, 144, 101]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[122, 103, 824, 225]]<|/det|>
\[
A: \quad \begin{bmatrix} -2 & 4 & 8 \\ 1 & -2 & -4 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -2 & -4 \\ 2 & 2 & -4 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -1 & -4 \\ 0 & 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -2 & -4 \end{bmatrix} \\
A^T: \quad \begin{bmatrix} -2 & 1 \\ 4 & -2 \\ 8 & -4 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -1 \\ 4 & -2 \\ 8 & -4 \end{bmatrix} \Leftarrow \begin{bmatrix} 2 & -1 \\ 0 & 0 \\ 0 & 0 \end{bmatrix} \Leftarrow \begin{bmatrix} 1 & -\frac{1}{2} \end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[114, 228, 437, 247]]<|/det|>
Für die Vektoren im Kern von A gilt 

<|ref|>equation<|/ref|><|det|>[[114, 250, 488, 287]]<|/det|>
\[
1 \cdot x - 2 \cdot y - 4 \cdot z = 0 \Rightarrow x = 2 \cdot y + 4 \cdot z
\]

<|ref|>text<|/ref|><|det|>[[114, 266, 300, 285]]<|/det|>
Daraus erhalten wir 

<|ref|>equation<|/ref|><|det|>[[114, 290, 620, 360]]<|/det|>
\[
\ker(A) = \left\{ \begin{bmatrix} 2y + 4z \\ y \\ z \end{bmatrix} \in \mathbb{R}^3 \right\} = \text{span} \left\{ \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 4 \\ 0 \\ 1 \end{bmatrix} \right\}
\]

<|ref|>text<|/ref|><|det|>[[114, 360, 385, 379]]<|/det|>
Für das Bild von A ergibt sich 

<|ref|>equation<|/ref|><|det|>[[114, 380, 512, 428]]<|/det|>
\[
\text{img}(A) = \text{span} \left\{ \begin{bmatrix} 1 \\ -\frac{1}{2} \end{bmatrix} \right\} = \text{span} \left\{ \begin{bmatrix} 2 \\ -1 \end{bmatrix} \right\}
\]

<|ref|>text<|/ref|><|det|>[[114, 428, 144, 446]]<|/det|>
e) 

<|ref|>equation<|/ref|><|det|>[[122, 448, 810, 572]]<|/det|>
\[
A: \quad \begin{bmatrix} -2 & 4 & -8 \\ 1 & -2 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -2 \\ 2 & -4 & -8 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -2 & 0 \\ 0 & 0 & -8 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -2 \\ 0 & 0 & 1 \end{bmatrix} \\
A^T: \quad \begin{bmatrix} -2 & 4 & -8 \\ 1 & 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -1 \\ 4 - 2 & 0 \\ 8 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -1 & -1 \\ 0 & 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix}- \frac{1}{2} & 1 & -\frac{1}{2} \\ 0 & 1 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[114, 574, 437, 592]]<|/det|>
Für die Vektoren im Kern von A gilt 

<|ref|>equation<|/ref|><|det|>[[0, 0, 0, 0]]<|/det|>
\[
0 \cdot x + 0 \cdot y + 1 \cdot z = 0 \Rightarrow z = 0
\]

<|ref|>equation<|/ref|><|det|>[[114, 616, 556, 635]]<|/det|>
\[
1 \cdot x - 2 \cdot y - 0 \cdot z = 0 \Rightarrow x = 2 \cdot y + 0 \cdot 0 = 2 \cdot y
\]

<|ref|>equation<|/ref|><|det|>[[114, 636, 512, 703]]<|/det|>
\[
\ker(A) = \left\{ \begin{bmatrix} 2 y \\ y \\ 0 \end{bmatrix} \in \mathbb{R}^3 \right\} = \text{span}\left\{ \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix} \right\}
\]

<|ref|>text<|/ref|><|det|>[[114, 706, 385, 725]]<|/det|>
Für das Bild von A ergibt sich 

<|ref|>equation<|/ref|><|det|>[[0, 0, 0, 0]]<|/det|>
\[\text{img}(A) = \text{span} \left\{ \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \right\} = \mathbb{R}^2\]

<|ref|>text<|/ref|><|det|>[[114, 729, 144, 747]]<|/det|>
f) 

<|ref|>equation<|/ref|><|det|>[[122, 749, 814, 848]]<|/det|>
\[
A: \quad \begin{bmatrix} -2 & 1 \\ 4 & -2 \\ -2 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -1\\ 4 & -2\\ 8 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & 0 & 0\\ 0 & 0 & 0\\ 0 & 0 & 4 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix} \\
A^T: \quad\begin{bmatrix} -2 & 4 & 8\\ 1 & -2 & 0\\ 1 & 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} -2 & 0 & 0\\ 2 & -4 & -8\\ 2 & 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 \\ 0 & 0 & 0\\ 0 & 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} -1 & 0 & 0\\ 0 & 1 & 0\\ 0 \\ 0 & 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix}
1 & -2 & 0\\ 0 & 0 & 1\\ 0 & 0 & 0 \end{bmatrix} .
\]

<|ref|>equation<|/ref|><|det|>[[122, 860, 812, 907]]<|/det|>
\[
A^T: \quad \begin{bmatrix} -2 & 4 & 8 \\ 1 & 0 & 0 \end{bmatrix} \Leftrightarrow \begin{smallmatrix} 1 & -2 & 0 \\ 2 & -4 & -8 \end{smallmatrix} \Leftrightarrow \begin{smallmatrix} 1 & -2 & 0 \\ -2 & 0 & 0 \end{smallmatrix} \Leftrightarrow \begin{smallmatrix} 1 & -1 & 0 \\ 0 & 0 & 0 \end{smallmatrix} \Leftrightarrow \begin{smallmatri
\]