<|ref|>title<|/ref|><|det|>[[115, 183, 456, 217]]<|/det|>
Übungsblatt LA 6 

<|ref|>text<|/ref|><|det|>[[576, 195, 880, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 277]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 304, 210, 321]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 872, 355]]<|/det|>
- Sie kennen die Begriffe orthogonale Matrix, Drehmatrix, Spiegelmatrix und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 354, 770, 372]]<|/det|>
- Sie kennen diejenigen der 2x2 Standardmatrizen, die orthogonal sind. 

<|ref|>text<|/ref|><|det|>[[115, 370, 820, 404]]<|/det|>
- Sie kennen das Spaltenvektor Konstruktionsverfahren zur Bestimmung von Matrizen und können dieses anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 403, 840, 437]]<|/det|>
- Sie können Dreh- und Spiegelmatrizen zur Lösung konkreter Fragestellungen anwenden. 

<|ref|>sub_title<|/ref|><|det|>[[115, 468, 685, 486]]<|/det|>
1. Spaltenvektor Konstruktionsverfahren für Matrizen in 2D 

<|ref|>text<|/ref|><|det|>[[115, 485, 860, 518]]<|/det|>
Benutzen Sie das Spaltenvektor Konstruktionsverfahren, um die jeweilige Matrix zu bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 517, 732, 534]]<|/det|>
a) Bestimmen Sie die Matrix \(S_{xy}\), die die Spiegelung an der Geraden 

<|ref|>text<|/ref|><|det|>[[115, 532, 833, 567]]<|/det|>
\(\{(x, y) \in \mathbb{R}^2 | x = y\}\) beschreibt. Testen Sie die Wirkung der Matrix an 2 selbst gewählten Vektoren. 

<|ref|>text<|/ref|><|det|>[[115, 567, 870, 601]]<|/det|>
b) Bestimmen Sie die Matrix \(R_{\pi/4}\), die die Drehung um den Ursprung um den Winkel \(\pi/4\) beschreibt. 

<|ref|>text<|/ref|><|det|>[[115, 619, 145, 636]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 633, 720, 666]]<|/det|>
Wir wählen als Testvektoren \(\vec{v} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}\), \(\vec{w} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}\). Nun führen wir die 

<|ref|>text<|/ref|><|det|>[[115, 664, 574, 682]]<|/det|>
Matrixoperationen im xy-Koordinatensystem durch. 

<|ref|>image<|/ref|><|det|>[[115, 682, 654, 840]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 841, 860, 876]]<|/det|>
Mittels des Spaltenvektor Konstruktionsverfahrens (hierfür nutzen wir die Bilder von \(\hat{e}_x\) und \(\hat{e}_y\), die wir aus der Zeichnung ablesen) erhalten wir die Matrix 

<|ref|>equation<|/ref|><|det|>[[115, 875, 696, 920]]<|/det|>
\[
\frac{S_{xy}}{S_{xx}} = \begin{bmatrix} S_{xy} \cdot \hat{e}_x & S_{xy} \cdot \hat{e}_y \end{bmatrix} = \begin{bmatrix} \hat{e}_y & \hat{e}_x \end{bmatrix} = \begin{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} & \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} .
\]