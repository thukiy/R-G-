<|ref|>text<|/ref|><|det|>[[114, 83, 144, 100]]<|/det|>
a) 

<|ref|>image<|/ref|><|det|>[[114, 99, 597, 325]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 326, 264, 343]]<|/det|>
Seitenvektoren: 

<|ref|>equation<|/ref|><|det|>[[120, 346, 625, 386]]<|/det|>
\[ \mathbf{a} := \mathbf{C} - \mathbf{B} = \begin{bmatrix} -1 \\ -1 \end{bmatrix} - \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} -1 - 1 \\ -1 - 2 \end{bmatrix} = \begin{bmatrix} -2 \\ -3 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[120, 391, 625, 432]]<|/det|>
\[ \mathbf{b} := \mathbf{A} - \mathbf{C} = \begin{bmatrix} 2 \\ 0 \end{bmatrix} - \begin{bmatrix} -1 \\ -1 \end{bmatrix} = \begin{bmatrix} 2 - (-1) \\ 0 - (-1) \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[120, 439, 600, 480]]<|/det|>
\[ \mathbf{c} := \mathbf{B} - \mathbf{A} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} - \begin{bmatrix} 2 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 - 2 \\ 2 - 0 \end{bmatrix} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[114, 481, 612, 500]]<|/det|>
Die Längen der Seiten erhalten wir mittels des Betrags: 

<|ref|>equation<|/ref|><|det|>[[120, 504, 540, 530]]<|/det|>
\[ \underline{a} = |\mathbf{a}| = \sqrt{\langle \mathbf{a}, \mathbf{a} \rangle} = \sqrt{(-2)^2 + (-3)^2} = \sqrt{13} \]

<|ref|>equation<|/ref|><|det|>[[120, 543, 561, 568]]<|/det|>
\[ \underline{b} = |\mathbf{b}| = \sqrt{\langle \mathbf{b}, \mathbf{b} \rangle} = \sqrt{3^2 + 1^2} = \sqrt{10} = \sqrt{2} \sqrt{5} \]

<|ref|>equation<|/ref|><|det|>[[120, 580, 500, 604]]<|/det|>
\[ \underline{c} = |\mathbf{c}| = \sqrt{\langle \mathbf{c}, \mathbf{c} \rangle} = \sqrt{(-1)^2 + 2^2} = \sqrt{5}. \]

<|ref|>text<|/ref|><|det|>[[114, 603, 860, 655]]<|/det|>
Die Innenwinkel sind die jeweiligen Winkel zwischen zwei Seiten. Es gilt jedoch zu beachten, dass die Vektoren beide vom Eckpunkt wegzeigen, d. h. es muss jeweils einer der Vektoren umgekehrt werden. 

<|ref|>equation<|/ref|><|det|>[[120, 652, 707, 720]]<|/det|>
\[ \underline{a} = \angle(-\mathbf{b}, \mathbf{c}) = \arccos\left(\frac{-\langle \mathbf{b}, \mathbf{c} \rangle}{|\mathbf{b}| \cdot |\mathbf{c}|}\right) = \arccos\left(\frac{-3 \cdot (-1) - 1 \cdot 2}{\sqrt{2} \cdot 5}\right) \\ = \arccos\left(\frac{1}{\sqrt{2} \cdot 5}\right) \approx 1.428'9 \approx 0.455 \pi \]

<|ref|>equation<|/ref|><|det|>[[120, 743, 766, 808]]<|/det|>
\[ \underline{\beta} = \angle(-\mathbf{c}, \mathbf{a}) = \arccos\left(\frac{-\langle \mathbf{c}, \mathbf{a} \rangle}{|\mathbf{c}| \cdot |\mathbf{a}|}\right) = \arccos\left(\frac{-(-1) \cdot (-2) - 2 \cdot (-3)}{\sqrt{5} \sqrt{13}}\right) \\ = \arccos\left(\frac{4}{\sqrt{5} \sqrt{13}}\right) \approx 1.051'7 \approx 0.335 \pi \]

<|ref|>equation<|/ref|><|det|>[[120, 840, 738, 896]]<|/det|>
\[ \underline{\gamma} = \angle(-\mathbf{a}, \mathbf{b}) = \arccos\left(\frac{-\langle \mathbf{a}, \mathbf{b} \rangle}{|\mathbf{a}| \cdot |\mathbf{b}|}\right) = \arccos\left(\frac{-(-2) \cdot 3 - (-3) \cdot 1}{\sqrt{13} \sqrt{2} \sqrt{5}}\right) \\ = \arccos\left(\frac{9}{\sqrt{13} \sqrt{2} \sqrt{5}}\right) \approx 0.661'04 \approx 0.210 \pi. \]