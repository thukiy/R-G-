<|ref|>text<|/ref|><|det|>[[114, 82, 144, 100]]<|/det|>
a) 

<|ref|>image<|/ref|><|det|>[[114, 98, 655, 393]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 396, 880, 470]]<|/det|>
In der Zeichnung haben wir die Bilder der Vektoren \(\hat{e}_x\) und \(\hat{e}_y\) eingezeichnet, die wir durch Anwenden der Matrix \(R_\alpha\) erhalten. Somit können wir aus der Zeichnung nun die Vektorkomponenten ablesen und das Spaltenvektor Konstruktionsverfahren zur Bestimmung der Matrix \(R_\alpha\) anwenden. 

<|ref|>equation<|/ref|><|det|>[[114, 466, 777, 508]]<|/det|>
\[ \frac{R_\alpha}{R_\alpha} = \begin{bmatrix} R_\alpha \cdot \hat{e}_x & R_\alpha \cdot \hat{e}_y \end{bmatrix} = \begin{bmatrix} \cos(\alpha) & -\sin(\alpha) \\ \sin(\alpha) & \cos(\alpha) \end{bmatrix} \begin{bmatrix} -\sin(\alpha) \\ \cos(\alpha) \end{bmatrix} = \begin{bmatrix} \cos(\alpha) & -\sin(\alpha)\\ \sin(\alpha) & \cos(\alpha) \end{bmatrix} \begin{bmatrix} \cos(\alpha) & -\sin(\alpha)\\ \sin(\alpha)& \cos(\alpha) \end{bmatrix}. \] 

<|ref|>text<|/ref|><|det|>[[114, 511, 147, 529]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 527, 697, 546]]<|/det|>
Wir ersetzen in der Matrix \(R_\alpha\) den Winkel \(\alpha\) durch -\(\alpha\) und erhalten 

<|ref|>equation<|/ref|><|det|>[[119, 545, 584, 587]]<|/det|>
\[ \frac{R_{-\alpha}}{R_{-\alpha}} = \begin{bmatrix} \cos(-\alpha) & -\sin(-\alpha) \\ \sin(-\alpha) & \cos(-\alpha) \end{bmatrix} = \begin{bmatrix} \cos(\alpha) & \sin(\alpha) \\ -\sin(\alpha) & \cos(\alpha) \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[114, 590, 147, 607]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[114, 604, 861, 675]]<|/det|>
Hintereinanderausführung von Drehung um denselben Winkel \(\alpha\), jedoch in entgegengesetzte Richtung, sollte zur Ausgangssituation führen. D. h., dass \(R_\alpha\) und \(R_{-\alpha}\) zueinander inverse Matrizen sein sollten. Dies können wir mittels Matrixmultiplikation nachrechnen: 

<|ref|>equation<|/ref|><|det|>[[119, 675, 783, 850]]<|/det|>
\[ \begin{aligned} \frac{R_\alpha \cdot R_{-\alpha}}{R_{-\alpha}} &= \begin{bmatrix} \cos(\alpha) & -\sin(\alpha) \\ \sin(\beta) & \cos(\beta) \end{bmatrix} \cdot \begin{bmatrix} \cos(\alpha) & \sin(\alpha) \\ -\sin(\beta) & \cos(\beta) \end{bmatrix} \\ &= \begin{bmatrix} \cos(\alpha) \cos(\beta) + (-\sin(\alpha))(-\sin(\beta)) & \cos(\alpha) \sin(\alpha) - \sin(\alpha) \cos(\beta) \\ \sin(\alpha) \cos(\beta) + \cos(\alpha)(-\sin(\alpha)) & \sin(\alpha) \sin(\alpha) + \cos(\alpha) \cos(\beta) \end{bmatrix} \\ &= \begin{bmatrix} \cos^2(\alpha) + \sin^2(\alpha) & \cos(\alpha) \sin(\alpha) - \sin(\alpha) \cos (\beta) \\ \sin(\alpha) \cos(\beta) - \cos(\alpha) \sin(\alpha) & \sin^2(\alpha) + \cos^2(\alpha) \end{bmatrix} \\ &= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \mathbb{1} \end{aligned} \]