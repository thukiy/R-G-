<|ref|>sub_title<|/ref|><|det|>[[25, 12, 415, 38]]<|/det|>
## Multiplikation von Matrizen 

<|ref|>table<|/ref|><|det|>[[55, 45, 683, 207]]<|/det|>
<table><tr><td>A sei l x m Matrix, B sei m x n Matrix</td></tr><tr><td>C = A · B = (cix)e,n</td><td>l x n Matrix</td></tr><tr><td>Cik = a1i b1k + a1i b2k + ... + aim bmk</td><td></td></tr><tr><td>= m ∑<sub>j=1</sub><sup>m</sup> aij bjk</td><td></td></tr></table>

<|ref|>text<|/ref|><|det|>[[45, 225, 950, 291]]<|/det|>
→ A · B nun möglich, wenn Spaltenanzahl von A mit Zeilenanzahl von B überschlimmt 

<|ref|>text<|/ref|><|det|>[[45, 303, 715, 330]]<|/det|>
→ Zeilen von A mit Spalten von B multiplizieren 

<|ref|>text<|/ref|><|det|>[[25, 362, 100, 388]]<|/det|>
Bsp.: 

<|ref|>equation<|/ref|><|det|>[[135, 360, 300, 409]]<|/det|>
\(A = \begin{pmatrix} 1 & 3 \\ 5 & 7 \end{pmatrix}\)

<|ref|>equation<|/ref|><|det|>[[360, 360, 565, 409]]<|/det|>
\(B = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}\)

<|ref|>equation<|/ref|><|det|>[[135, 415, 300, 465]]<|/det|>
\(A \cdot B = \begin{pmatrix} 1 & 3 \\ 5 & 7 \end{pmatrix} \cdot \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 1 \cdot 2 + 3 \cdot 3 & 1 \cdot 1 + 3 \cdot 4 \\ 5 \cdot 2 + 7 \cdot 3 & 5 \cdot 1 + 7 \cdot 4 \end{pmatrix} = \begin{pmatrix} 11 & 13 \\ 31 & 33 \end{pmatrix}\) 

<|ref|>equation<|/ref|><|det|>[[135, 473, 300, 523]]<|/det|>
\(B \cdot A = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix} \cdot \begin{pmatrix} 1 & 3 \\ 5 & 7 \end{pmatrix} = \begin{pmatrix} 2 \cdot 1 + 1 \cdot 5 & 2 \cdot 3 + 1 \cdot 7 \\ 3 \cdot 1 + 4 \cdot 5 & 3 \cdot 3 + 4 \cdot 7 \end{pmatrix} = \begin{pmatrix} 7 & 13 \\ 23 & 37 \end{pmatrix}\) 

<|ref|>equation<|/ref|><|det|>[[135, 554, 300, 604]]<|/det|>
\(A = \begin{pmatrix} 1 & 4 & 2 \\ 4 & 0 & -3 \end{pmatrix} \cdot \begin{pmatrix} 2 & 3 \\ 2 & 3 \end{pmatrix}\)

<|ref|>equation<|/ref|><|det|>[[565, 553, 800, 622]]<|/det|>
\(B = \begin{pmatrix} 1 & 0 \\ -2 & 3 \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 3 & 3 \\ 4 & 5 \end{pmatrix}\)

<|ref|>equation<|/ref|><|det|>[[135, 620, 300, 680]]<|/det|>
\(A \cdot B = \begin{pmatrix} 1 & 4 & 2 \\ 4 & 0 -3 \end{pmatrix} \cdot \begin{pmatrix} 1 & 4 & 2 \\ 4 & 0 - 3 \end{pmatrix} = \begin{pmatrix} 1 & 4 & 2 \\ 4 & 0 \end{pmatrix} \cdot \begin{pmatrix} 1 & 4 & 2 \\ -2 & 3 & 5 \\ 0 & 1 & 4 \end{pmatrix} = \begin{pmatrix} -7 & 15 & 28 \\ 4 & 1 & 12 \\ bc & bd & be \end{pmatrix} \cdot \begin{pmatrix} 1 & 4 & 2 \\ b & 0 & -3 \end{pmatrix}\) 

<|ref|>equation<|/ref|><|det|>[[135, 688, 432, 737]]<|/det|>
\(B \cdot A \text{ nicht möglich}\)

<|ref|>text<|/ref|><|det|>[[45, 771, 512, 798]]<|/det|>
→ im Allgemeinen: \(A \cdot B \neq B \cdot A\) 

<|ref|>text<|/ref|><|det|>[[340, 812, 576, 837]]<|/det|>
nicht kommutativ 

<|ref|>sub_title<|/ref|><|det|>[[25, 869, 230, 896]]<|/det|>
## Rechenregeln : 

<|ref|>equation<|/ref|><|det|>[[55, 904, 300, 936]]<|/det|>
\(0 \cdot (A + B)^T = A^T + B^T\)

<|ref|>equation<|/ref|><|det|>[[520, 905, 800, 936]]<|/det|>
\(0 \cdot 11 \cdot A = A \cdot 11 = A\)

<|ref|>equation<|/ref|><|det|>[[55, 944, 300, 976]]<|/det|>
\(0 \cdot (A \cdot B)^T = B^T \cdot A^T\)

<|ref|>equation<|/ref|><|det|>[[520, 944, 895, 976]]<|/det|>
\(0 \cdot A \cdot (B + C) = A \cdot B + A \cdot C\)