<|ref|>equation<|/ref|><|det|>[[115, 84, 515, 129]]<|/det|>
\[
\mathbf{B} = \mathbf{A} + \mathbf{a} = \begin{bmatrix} -1 \\ 3 \end{bmatrix} + \begin{bmatrix} -1 \\ -3 \end{bmatrix} = \begin{bmatrix} -2 \\ 0 \end{bmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[115, 137, 511, 181]]<|/det|>
\[
\mathbf{D} = \mathbf{A} + \mathbf{d} = \begin{bmatrix} -1 \\ 3 \end{bmatrix} + \begin{bmatrix}\phantom{-}3 \\ -1 \end{bmatrix} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[115, 181, 250, 199]]<|/det|>
2. Möglichkeit: 

<|ref|>text<|/ref|><|det|>[[115, 197, 864, 234]]<|/det|>
Wir berechnen die Hälfte der zweiten Diagonale. Hierfür verkürzen wir den Vektor \(\vec{u}\) um den Faktor 2 und drehen um \(\pi/2\). Wir verwenden die folgenden beiden Matrizen 

<|ref|>equation<|/ref|><|det|>[[122, 234, 559, 277]]<|/det|>
\[
Z(1/2) = \frac{1}{2} \cdot \mathbb{1} \quad \text{bzw.} \quad R(\pi/2) = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 278, 625, 298]]<|/det|>
Anwenden auf \(\vec{u}\) ergibt die Hälfte der anderen Diagonale 

<|ref|>equation<|/ref|><|det|>[[115, 299, 870, 390]]<|/det|>
\[
\mathbf{v} = Z(1/2) \cdot R(\pi/2) \cdot \mathbf{u} = \frac{1}{2} \cdot \mathbb{1} \cdot \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \cdot \begin{bmatrix} 2 \\ -4 \end{bmatrix} = \frac{1}{2} \cdot \begin{bmatrix} 0 \cdot 2 + (-1) \cdot (-4) \\ 1 \cdot 2 + 0 \cdot (-4) \end{bmatrix} \\
= \frac{1}{2} \cdot \begin{bmatrix} 4 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[115, 391, 639, 410]]<|/det|>
Nun können wir den Mittelpunkt des Quadrats bestimmen: 

<|ref|>equation<|/ref|><|det|>[[122, 415, 755, 461]]<|/det|>
\[
\mathbf{M} = \mathbf{A} + \frac{1}{2} \cdot \mathbf{u} = \begin{bmatrix} -1 \\ 3 \end{bmatrix} + \frac{1}{2} \cdot \begin{bmatrix} 2 \\ -4 \end{bmatrix} = \begin{bmatrix} -1 \\ 3 \end{bmatrix} + \begin{bmatrix}-1 \\ -2 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 462, 585, 481]]<|/det|>
Für die Ortsvektoren der beiden Punkte erhalten wir 

<|ref|>equation<|/ref|><|det|>[[122, 485, 496, 531]]<|/det|>
\[
\mathbf{B} = \mathbf{M} - \mathbf{v} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} - \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} -2 \\ 0 \end{bmatrix}
\]

Der Vektor vom Mittelpunkt zu Punkt A ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[115, 536, 500, 581]]<|/det|>
\[
\mathbf{D} = \mathbf{M} + \mathbf{v} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} + \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}.
\] 

<|ref|>text<|/ref|><|det|>[[115, 585, 145, 602]]<|/det|>
b) 

<|ref|>image<|/ref|><|det|>[[115, 603, 740, 825]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 825, 590, 844]]<|/det|>
Der Vektor vom Mittelpunkt zu Punkt A ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[122, 848, 496, 893]]<|/det|>
\[
\mathbf{u} := \mathbf{A} - \mathbf{M} = \begin{bmatrix} 0 \\ 3 \end{bmatrix} - \begin{bmatrix} 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 893, 780, 928]]<|/det|>
Um die Punkte B und C zu bestimmen, drehen wir \(\vec{u}\) um \(2\pi/3\) und spiegeln
anschliessend an der y-Achse. Die Drehmatrix ergibt sich zu