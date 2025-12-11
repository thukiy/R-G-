<|ref|>equation<|/ref|><|det|>[[117, 81, 540, 125]]<|/det|>
\[
\frac{S_{xy} \cdot \mathbf{v}}{S_{xy} \cdot \mathbf{w}} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 0 \cdot 2 + 1 \cdot 3 \\ 1 \cdot 2 + 0 \cdot 3 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[117, 128, 593, 170]]<|/det|>
\[
\frac{S_{xy} \cdot \mathbf{w}}{S_{xy} \cdot \mathbf{w}} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \cdot (-1) + 1 \cdot 2 \\ 1 \cdot (-1) + 0 \cdot 2 \end{bmatrix} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 172, 145, 191]]<|/det|>
b) 

<|ref|>image<|/ref|><|det|>[[115, 190, 655, 378]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 380, 700, 408]]<|/det|>
Wir gehen gleich wie in a) vor und benutzen \(\sin(\frac{\pi}{4}) = \cos(\frac{\mu}{4}) = \frac{1}{\sqrt{2}}\). 

<|ref|>equation<|/ref|><|det|>[[117, 408, 696, 508]]<|/det|>
\[
\begin{align*}
R_{\pi/4} &= \begin{bmatrix} R_{\pi/4} \cdot \hat{e}_x & R_{\pi/4} \cdot \hat{e}_y \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix} \begin{bmatrix} -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \begin{bmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix} \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\frac{1}{\sqrt{2}}} \end{bmatrix} \\
&= \frac{1}{\sqrt{2}} \cdot \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 523, 330, 541]]<|/det|>
2. Drehmatrizen in 2D 

<|ref|>text<|/ref|><|det|>[[115, 540, 852, 558]]<|/det|>
Im Folgenden lernen Sie Form und Eigenschaften von Drehmatrizen in 2D kennen. 

<|ref|>text<|/ref|><|det|>[[115, 557, 875, 592]]<|/det|>
a) Bestimmen Sie die Matrix \(R_\alpha\) mit Hilfe des Spaltenvektor Konstruktionsverfahrens, die die Drehung um den Ursprung um den Winkel \(\alpha \in \mathbb{R}\) beschreibt. 

<|ref|>text<|/ref|><|det|>[[115, 590, 654, 608]]<|/det|>
b) Bestimmen Sie die Matrix \(R_\alpha\) mit Hilfe des Spaltenvektor 

<|ref|>text<|/ref|><|det|>[[115, 606, 870, 679]]<|/det|>
Konstruktionsverfahrens, die die Drehung um den Ursprung um den Winkel \(-\alpha \in \mathbb{R}\) (also Drehung im Uhrzeigersinn) beschreibt.
Hinweis: Verwenden Sie die Paritätseigenschaften, dass gilt: \(\sin(-\alpha) = -\sin\alpha\) und \(\cos(-\alpha) = \cos\alpha\). 

<|ref|>text<|/ref|><|det|>[[115, 676, 841, 712]]<|/det|>
c) Welcher Zusammenhang besteht zwischen den Drehmatrizen aus Aufgabe a) und b)? Berechnen Sie die Matrixprodukte \(R_\alpha \cdot R_{-\alpha}\) und \(R_{-\alpha} \cdot R_\alpha\). 

<|ref|>text<|/ref|><|det|>[[115, 710, 736, 728]]<|/det|>
d) Berechnen Sie die Matrixprodukte \(R_\alpha \cdot R_\beta\) und \(R_\beta \cdot R_\alpha\) mit \(\alpha, \beta \in \mathbb{R}\). 

<|ref|>text<|/ref|><|det|>[[115, 726, 875, 778]]<|/det|>
Hinweis: Überlegen Sie sich, was passiert, wenn man nacheinander die Drehungen auf denselben Vektor ausführt. Nutzen Sie die Additionstheoreme zur Vereinfachung der Matrizen. 

<|ref|>text<|/ref|><|det|>[[115, 777, 792, 807]]<|/det|>
e) Geben Sie die Drehmatrizen für \(\alpha \in \{0, \pm \frac{\pi}{6}, \pm \frac{\pi}{4}, \pm \frac{\pi}{3}, \pm \frac{\pi}{2}, \pm \pi\}\) explizit an.