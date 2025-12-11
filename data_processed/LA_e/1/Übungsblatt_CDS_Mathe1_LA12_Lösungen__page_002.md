<|ref|>text<|/ref|><|det|>[[114, 83, 145, 100]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 99, 835, 135]]<|/det|>
Die Ebenengleichung kann als LGS aufgefasst werden (mit zwei Nullzeilen, d. h. zwei Parameter dürfen frei gewählt werden). Setze \(x = \lambda\) und \(y = \mu\) mit \(\lambda, \mu \in \mathbb{R}\). 

<|ref|>equation<|/ref|><|det|>[[303, 134, 612, 152]]<|/det|>
\[ -2z = 3 + 4x - y = 3 + 4\lambda - \mu \]

<|ref|>text<|/ref|><|det|>[[119, 161, 780, 182]]<|/det|>
\(z = -3/2 - 2\lambda + \mu/2\), woraus eine Paramaterformulierung für \(E\) folgt: 

<|ref|>equation<|/ref|><|det|>[[163, 210, 755, 286]]<|/det|>
\[ E : \vec{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ -3/2 \end{pmatrix} + \lambda \begin{pmatrix} 1 \\ 0 \\ -2 \end{pmatrix} + \mu \begin{pmatrix} 0 \\ 1 \\ 1/2 \end{pmatrix}, \quad \lambda, \mu \in \mathbb{R} \]

<|ref|>text<|/ref|><|det|>[[114, 286, 221, 321]]<|/det|>
c) Wir wählen 

<|ref|>equation<|/ref|><|det|>[[129, 323, 270, 397]]<|/det|>
\[ s_0 := \mathbf{A} = \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[129, 403, 533, 481]]<|/det|>
\[ \mathbf{v} := \mathbf{A} - \mathbf{B} = \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix} - \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[129, 488, 567, 564]]<|/det|>
\[ \mathbf{w} := \mathbf{C} - \mathbf{A} = \begin{bmatrix} -3 \\ 4 \\ -1 \end{bmatrix} - \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix} = \begin{bmatrix} -5 \\ 3 \\ -4 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[114, 565, 550, 584]]<|/det|>
Es ergibt sich dann die folgende Parameterform 

<|ref|>equation<|/ref|><|det|>[[117, 582, 744, 658]]<|/det|>
\[ \mathbf{s}(\tau; \sigma) = s_0 + \tau \cdot \mathbf{v} + \sigma \cdot \mathbf{w} = \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix} + \tau \cdot \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} + \sigma \cdot \begin{bmatrix} -5 \\ 3 \\ -4 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[114, 661, 750, 755]]<|/det|>
\[ \begin{aligned} \mathbf{n} &= \mathbf{v} \times \mathbf{w} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \times \begin{bmatrix} -5 \\ 3 \\ -4 \end{bmatrix} = \begin{bmatrix} 1 \cdot (-4) - 1 \cdot 3 \\ 1 \cdot (-5) - 1 \cdot (-4) \\ 1 \cdot 3 - 1 \cdot (-5) \end{bmatrix} = \begin{bmatrix} -7 \\ -1 \\ 8 \end{bmatrix} \\ \end{aligned} \]

<|ref|>equation<|/ref|><|det|>[[119, 770, 610, 874]]<|/det|>
\[ |\mathbf{n}| = \sqrt{(-7)^2 + (-1)^2 + 8^2} = \sqrt{49 + 1 + 64} = \sqrt{114} \\ \hat{\mathbf{n}} = \frac{1}{|\mathbf{n}|} \cdot \mathbf{n} = \frac{1}{\sqrt{114}} \begin{bmatrix} -7 \\ -1 \\ 8 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[114, 880, 382, 899]]<|/det|>
Bestimmung der Normalform