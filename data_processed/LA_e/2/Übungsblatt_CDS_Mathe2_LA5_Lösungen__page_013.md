<|ref|>text<|/ref|><|det|>[[115, 81, 874, 120]]<|/det|>
b) Bestimmen Sie die Matrix \(R_{\pi/4}\), die die Drehung um den Ursprung um den Winkel \(\pi/4\) beschreibt. 

<|ref|>text<|/ref|><|det|>[[115, 135, 144, 153]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 149, 725, 199]]<|/det|>
Wir wählen als Testvektoren \(\vec{v} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}\), \(\vec{w} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}\). Nun führen wir die Matrixoperationen im xy-Koordinatensystem durch. 

<|ref|>image<|/ref|><|det|>[[115, 197, 655, 355]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 355, 861, 393]]<|/det|>
Mittels des Spaltenvektor Konstruktionsverfahrens (hierfür nutzen wir die Bilder von \(\hat{e}_x\) und \(\hat{e}_y\), die wir aus der Zeichnung ablesen) erhalten wir die Matrix 

<|ref|>equation<|/ref|><|det|>[[115, 393, 699, 437]]<|/det|>
\[ \begin{aligned} S_{xy} &= \begin{bmatrix} S_{xy} \cdot \hat{e}_x & S_{xy} \cdot \hat{e}_y \end{bmatrix} = \begin{bmatrix} \hat{e}_y & \hat{e}_x \end{bmatrix} = \begin{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \\ S_{xy} \cdot \mathbf{v} &= \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 0 \cdot 2 + 1 \cdot 3 \\ 1 \cdot 2 + 0 \cdot 3 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix} \\ S_{xy} \cdot \mathbf{w} &= \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{ bmatrix} = \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \cdot (-1) + 1 \cdot 2 \\ 1 \cdot (-1) + 0 \cdot 2 \end{bmatrix} = \begin{bmatrix} 2 \\ -1 \end{bmatrix} \end{aligned} \] 

<|ref|>equation<|/ref|><|det|>[[115, 440, 540, 485]]<|/det|>
\[ S_{xy} \cdot \mathbf{v} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{ bmatr} = \begin{bmatrix} 2 \\ 3 \end{bmatrix} = \begin{bmatrix}\begin{bmatrix} 0 \cdot 2 + 1 \cdot 3 \\ 1\cdot 2 + 0 \cdot 3 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix} \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[115, 485, 593, 529]]<|/det|>
\[ S_{xy} \cdot \mathbf{w} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatr} = \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix}\begin{bmatrix} 0 \cdot (-1) + 1 \cdot 2 \\ 0 \cdot (-1) + 0 \cdot 2 \end{bmatrix} = \begin{bmatr} 2 \\ -1 \end{bmatrix} \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 529, 144, 546]]<|/det|>
b) 

<|ref|>image<|/ref|><|det|>[[115, 545, 655, 732]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 733, 700, 764]]<|/det|>
Wir gehen gleich wie in a) vor und benutzen \(\sin(\frac{\pi}{4}) = \cos(\frac{\mu}{4}) = \frac{1}{\sqrt{2}}\). 

<|ref|>equation<|/ref|><|det|>[[115, 764, 700, 810]]<|/det|>
\[ \frac{R_{\pi/4}}{4} = \begin{bmatrix} R_{\pi/4} \cdot \hat{e}_x & R_{\pi/4} \cdot \hat{e}_y \end{bmatrix} = \begin{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix} & \begin{bmatrix} -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \right] \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix} \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[161, 815, 323, 860]]<|/det|>
\[ = \frac{1}{\sqrt{2}} \cdot \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix} \]