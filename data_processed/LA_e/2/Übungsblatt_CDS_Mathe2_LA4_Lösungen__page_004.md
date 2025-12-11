<|ref|>text<|/ref|><|det|>[[146, 97, 836, 151]]<|/det|>
➔ Die Multiplikation von Matrizen ist im Allgemeinen nicht kommutativ, d. h. abhängig von den Matrizen A und B kann entweder AB = BA oder AB ≠ BA gelten. 

<|ref|>sub_title<|/ref|><|det|>[[114, 165, 375, 183]]<|/det|>
## 5. Produkte mit Matrizen II 

<|ref|>text<|/ref|><|det|>[[114, 182, 375, 199]]<|/det|>
Gegeben seien die Matrizen 

<|ref|>equation<|/ref|><|det|>[[114, 203, 420, 240]]<|/det|>
\[A = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix} \text{ und } B = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}.\]

<|ref|>text<|/ref|><|det|>[[114, 243, 550, 261]]<|/det|>
Berechnen Sie die jeweiligen Produkte der Matrizen. 

<|ref|>text<|/ref|><|det|>[[114, 259, 250, 277]]<|/det|>
a) \(C = A^T \cdot A\) 

<|ref|>text<|/ref|><|det|>[[114, 275, 244, 293]]<|/det|>
d) \(C = A^T \cdot B^T\) 

<|ref|>text<|/ref|><|det|>[[400, 259, 525, 277]]<|/det|>
b) \(C = A \cdot A^T\) 

<|ref|>text<|/ref|><|det|>[[400, 275, 528, 293]]<|/det|>
e) \(C = B^T \cdot A^T\) 

<|ref|>text<|/ref|><|det|>[[680, 259, 830, 277]]<|/det|>
c) \(C = (A \cdot B)^T\) 

<|ref|>text<|/ref|><|det|>[[680, 275, 833, 293]]<|/det|>
f) \(C = (B^T \cdot A^T)^T\) 

<|ref|>text<|/ref|><|det|>[[114, 309, 336, 326]]<|/det|>
Transponierte Matrizen: 

<|ref|>equation<|/ref|><|det|>[[114, 324, 404, 361]]<|/det|>
\[A^T = \begin{pmatrix} 3 & -2 \\ -1 & 1 \end{pmatrix}, B^T = \begin{pmatrix} 2 & 3 \\ -1 & 4 \end{pmatrix}\]

<|ref|>text<|/ref|><|det|>[[114, 357, 144, 374]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[119, 370, 835, 461]]<|/det|>
\[\begin{aligned} \underline{C} &= A^T \cdot A = \begin{bmatrix} 3 \cdot 3 + (-2) \cdot (-2) & 3 \cdot (-1) + (-2) \cdot 1 \\ (-1) \cdot 3 + 1 \cdot (-2) & (-1) \cdot (-1) + 1 \cdot 1 \end{bmatrix} = \begin{bmatrix} 9 + 4 & -3 - 2 \\ -3 - 2 & 1 + 1 \end{bmatrix} \\ &= \begin{bmatrix} 13 & -5 \\ -5 & 2 \end{bmatrix}. \end{aligned}\]

<|ref|>text<|/ref|><|det|>[[114, 467, 144, 484]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[119, 487, 835, 580]]<|/det|>
\[\begin{aligned} \underline{C} &= A \cdot A^T = \begin{bmatrix} 3 \cdot 3 + (-1) \cdot (-1) & 3 \cdot (-2) + (-1) \cdot 1 \\ (-2) \cdot 3 + 1 \cdot (-1) & (-2) \cdot (-2) + 1 \cdot 1 \end{bmatrix} = \begin{bmatrix} 9 & 1 & -6 & -1 \\ -6 & -1 & 4 & 1 \end{bmatrix} \\ &= \begin{bmatrix} 10 & -7 \\ -7 & 5 \end{bmatrix} \neq A^T \cdot A. \end{aligned}\]

<|ref|>text<|/ref|><|det|>[[114, 585, 144, 602]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[119, 604, 850, 707]]<|/det|>
\[\begin{aligned} \underline{C} &= (A \cdot B)^T = \begin{bmatrix} 3 \cdot 2 + (-1) \cdot 3 & 3 \cdot (-1) + (-1) \cdot 4 \\ (-2) \cdot 2 + 1 \cdot 3 & (-2) \cdot (-1) + 1 \cdot 4 \end{bmatrix}^T = \begin{bmatrix} 6 & -3 & -3 & -4 \\ -4 & +3 & 2 & +4 \end{bmatrix}^T \\ &= \begin{bmatrix} 3 & -7 \\ -1 & 6 \end{bmatrix}^T = \begin{bmatrix} 3 & -1 \\ -7 & 6 \end{bmatrix}. \end{aligned}\]

<|ref|>text<|/ref|><|det|>[[114, 711, 144, 728]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[114, 730, 816, 835]]<|/det|>
\[\begin{aligned} \underline{C} &= A^T \cdot B^T = \begin{bmatrix} 3 \cdot 2 + (-2) \cdot (-1) & 3 \cdot 3 + (-2) \cdot 4 \\ (-1) \cdot 2 + 1 \cdot (-1) & (-1) \cdot 3 + 1 \cdot 4 \end{bmatrix} = \begin{bmatrix} 6 + 2 & 9 - 8 \\ -2 - 1 & -3 + 4 \end{bmatrix} \\ &= \begin{bmatrix} 8 & 1 \\ -3 & 1 \end{bmatrix} \neq (A \cdot B)^T. \end{aligned}\]