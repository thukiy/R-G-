<|ref|>title<|/ref|><|det|>[[115, 183, 456, 217]]<|/det|>
# Übungsblatt LA 5 

<|ref|>text<|/ref|><|det|>[[576, 196, 880, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 277]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[751, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 304, 210, 321]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 875, 355]]<|/det|>
- Sie kennen die Begriffe Matrix, inverse Matrix, Drehmatrix, lineare Abbildung und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 353, 850, 387]]<|/det|>
- Sie kennen die 2x2 Standardmatrizen und die dadurch beschriebenen linearen Abbildungen in 2D. 

<|ref|>text<|/ref|><|det|>[[115, 386, 820, 419]]<|/det|>
- Sie kennen das Spaltenvektor Konstruktionsverfahren zur Bestimmung von Matrizen. 

<|ref|>text<|/ref|><|det|>[[115, 418, 794, 437]]<|/det|>
- Sie können lineare Gleichungssysteme mit Hilfe von Matrizen darstellen. 

<|ref|>text<|/ref|><|det|>[[115, 435, 760, 470]]<|/det|>
- Sie können bestimmen, ob eine Matrix invertierbar ist oder nicht und gegebenenfalls die inverse Matrix bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 468, 820, 501]]<|/det|>
- Sie können Verknüpfungen von linearen Abbildungen durch Matrixprodukte ausdrücken. 

<|ref|>sub_title<|/ref|><|det|>[[115, 534, 336, 551]]<|/det|>
### 1. Matrizen invertieren 

<|ref|>text<|/ref|><|det|>[[115, 550, 592, 569]]<|/det|>
Berechnen Sie die inverse Matrix folgender Matrizen. 

<|ref|>equation<|/ref|><|det|>[[115, 570, 666, 691]]<|/det|>
\[
\begin{align*}
\text{a)} \quad A &= \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \quad & \text{b)} \quad A &= \begin{pmatrix} \frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix} \\
\text{c)} \quad A &= \begin{pmatrix} 0 & 3 & -6 \\ 1 & -1 & 3 \\ 2 & -5 & 9 \end{pmatrix} \quad & \text{d)} \quad A &= \begin{pmatrix} 1 & 2 & 2 & -3 \\ 4 & 5 & 5 & -8 \\ -6 & 0 & -3 & 7 \\ 2 & 1 & 3 & -6 \end{pmatrix}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[115, 686, 333, 721]]<|/det|>
\[
\text{e)} \quad A = \begin{pmatrix} \cos \phi & -\sin \phi \\ \sin \phi & \cos \phi \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 732, 145, 750]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[115, 754, 352, 800]]<|/det|>
\[
A^{-1} = \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 801, 145, 819]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[115, 820, 364, 876]]<|/det|>
\[
B^{-1} = \begin{pmatrix} \frac{1}{2} & \frac{\sqrt{3}}{2} \\ -\frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 938, 150, 956]]<|/det|>
1