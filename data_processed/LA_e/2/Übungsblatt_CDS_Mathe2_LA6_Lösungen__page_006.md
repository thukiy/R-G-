<|ref|>text<|/ref|><|det|>[[114, 83, 144, 100]]<|/det|>
a) 

<|ref|>image<|/ref|><|det|>[[117, 100, 740, 323]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[120, 323, 374, 342]]<|/det|>
Der Diagonalen-Vektor ist 

<|ref|>equation<|/ref|><|det|>[[120, 351, 536, 395]]<|/det|>
\[ \mathbf{u} := \mathbf{C} - \mathbf{A} = \begin{bmatrix} 1 \\ -1 \end{bmatrix} - \begin{bmatrix} -1 \\ 3 \end{bmatrix} = \begin{bmatrix} 2 \\ -4 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[114, 395, 250, 413]]<|/det|>
1. Möglichkeit: 

<|ref|>text<|/ref|><|det|>[[114, 413, 852, 472]]<|/det|>
Wir berechnen die Vektoren \(\vec{a}\) (Verbindung von Punkt A und B) und \(\vec{d}\) (Verbindung von Punkt A und D). Hierfür verkürzen wir den Vektor \(\vec{u}\) um \(\sqrt{2}\) und drehen anschliessend um \(\pi/4\) bzw. \(-\pi/4\). Hierfür nutzen wir die folgenden beiden Matrizen 

<|ref|>equation<|/ref|><|det|>[[123, 468, 312, 508]]<|/det|>
\[ Z\left(1/\sqrt{2}\right) = \frac{1}{\sqrt{2}} \cdot \mathbb{1} \]

<|ref|>equation<|/ref|><|det|>[[135, 515, 395, 558]]<|/det|>
\[ R\left(+\pi/4\right) = \frac{1}{\sqrt{2}} \cdot \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[135, 566, 520, 610]]<|/det|>
\[ R\left(-\pi/4\right) = R^T\left(+\pi/4\right) = \frac{1}{\sqrt{2}} \left[ \begin{array}{cc} 1 & 1 \\ -1 & 1 \end{array} \right] \]

<|ref|>text<|/ref|><|det|>[[114, 610, 247, 629]]<|/det|>
Es ergibt sich 

<|ref|>equation<|/ref|><|det|>[[120, 627, 725, 672]]<|/det|>
\[ \mathbf{d} = Z\left(1/\sqrt{2}\right) \cdot R\left(+\pi/4\right) \cdot \mathbf{u} = \frac{1}{\sqrt{2}} \cdot \mathbb{1} \cdot \frac{1}{\sqrt{2}} \cdot \begin{bmatrix} 1 & - 1 \\ 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} 2 \\ -4 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[140, 678, 630, 722]]<|/det|>
\[ = \frac{1}{2} \cdot \begin{bmatrix} 1 \cdot 2 + (-1) \cdot (-4) \\ 1 \cdot 2 + 1 \cdot (-4) \end{bmatrix} = \frac{1}{2} \cdot \begin{bmatrix} 6 \\ -2 \end{bmatrix} = \begin{bmatrix} 3 \\ -1 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[120, 728, 725, 773]]<|/det|>
\[ \mathbf{a} = Z\left(1/\sqrt{2}\right) \cdot R\left(-\pi/4\right) \cdot \mathbf{u} = \frac{1}{\sqrt{3}} \cdot \mathbb{1} \cdot \frac{1}{\sqrt{2}} = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} \cdot \begin{bmatrix} 2 \\ -4\end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[140, 779, 639, 824]]<|/det|>
\[ = \frac{1}{2} \cdot \begin{bmatrix} 2 \cdot 1 + 1 \cdot (-4) \\ (-1) \cdot 2 + 1 \cdot (-4) \end{bmatrix} = \frac {1}{2} \cdot \begin{bmatrix} -2 \\ -6 \end{bmatrix} = \begin{bmatrix} -1 \\ -3 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[114, 827, 616, 847]]<|/det|>
Für die Ortsvektoren der beiden Eckpunkte erhalten wir