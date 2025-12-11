<|ref|>sub_title<|/ref|><|det|>[[115, 81, 455, 100]]<|/det|>
## 7. Kombination von Matrizen in 2D 

<|ref|>text<|/ref|><|det|>[[115, 99, 839, 152]]<|/det|>
Bestimmen Sie die Matrix, welche sich durch die Kombination der jeweiligen Abbildungen ergibt. Wenden Sie die jeweils erhaltene Abbildung auf \(\hat{e}_x\), \(\hat{e}_y\) sowie einen weiteren selbst gewählten Vektor an. 

<|ref|>text<|/ref|><|det|>[[115, 150, 768, 169]]<|/det|>
Hinweis: Verwenden Sie die in Aufgabe 5 gegebenen Standardmatrizen. 

<|ref|>text<|/ref|><|det|>[[115, 167, 866, 201]]<|/det|>
a) Erst Streckung am Ursprung um den Faktor 2 und anschliessend Spiegelung an der x-Achse. 

<|ref|>text<|/ref|><|det|>[[115, 199, 860, 218]]<|/det|>
b) Erst Spiegelung an der x-Achse und anschliessend Spiegelung an der y-Achse. 

<|ref|>text<|/ref|><|det|>[[115, 216, 860, 234]]<|/det|>
c) Erst Spiegelung an der y-Achse und anschliessend Spiegelung an der x-Achse. 

<|ref|>text<|/ref|><|det|> [[115, 232, 810, 251]]<|/det|>
d) Projektion auf die y-Achse und anschliessend Spiegelung an der x-Achse. 

 <|ref|>text<|/ref|><|det|>[[115, 249, 857, 268]]<|/det|>
e) Erst Spiegelung an der x-Achse und anschliessend Projektion auf die y-Achse. 

<|ref|>text<|/ref|><|det|>[[115, 266, 880, 301]]<|/det|>
f) Erst Drehung um den Ursprung um den Winkel \(\pi/2\) und anschliessend Spiegelung an der x-Achse. 

<|ref|>text<|/ref|><|det|>([[115, 299, 880, 335]]<|/det|>
g) Erst Drehung um den Ursprung um den Winkel \(\pi/2\) und anschlIessend Spiegelung an der x-Achse und anschliessend Streckung um den Faktor -3. 

<|ref|>text<|/ref|><|det|>[[115, 333, 866, 386]]<|/det|>
h) Erst Spiegelung an der x-Achse, anschliessend Spiegelung an der y-Achse, anschliessend Spiegelung an der x-Achse und abschliessend Spiegelung an der y-Achse. 

<|ref|>text<|/ref|><|det|>[[115 403, 145, 421]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[115, 415, 530, 457]]<|/det|>
\[ \underline{A} = S_x \cdot Z_2 = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \cdot \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix}. \]

<|ref|>equation<|/ref|><|det|>[[115, 465, 640, 507]]<|/det|>
\[ \underline{A} \cdot \hat{e}_x = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \cdot 1 + 0 \cdot 0 \\ 0 \cdot 1 + (-2) \cdot 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix} = 2 \cdot \hat{e}_x \]

<|ref|>equation<|/ref|><|det|>[[115, 512, 660, 554]]<|/det|>
\[ \underline{A} \cdot \hat{e}_y = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix}\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \cdot 0 + 0 \cdot 1 \\ 0 \cdot 0 + (-2) \cdot 1 \end{bmatrix} = \begin{bmatrix} 0 \\ -2 \end{bmatrix} = -2 \cdot \hat{e}_y \]

<|ref|>equation<|/ref|><|det|>[[115, 558, 590, 599]]<|/det|>
\[ \underline{A} \cdot \underline{u} = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{ bmatrix} \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 \cdot 3 + 0 \cdot 2 \\ 0 \cdot 3 + (-2) \cdot 2 \end{bmatrix} = \begin{bmatrix} 6 \\ -4 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[115, 597, 145, 615]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[115, 610, 585, 653]]<|/det|>
\[ \underline{A} = S_y \cdot S_x = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix} = \underline{P} \]

<|ref|>equation<|/ref|><|det|>[[115, 653, 300, 675]]<|/det|>
\[ \underline{A} \cdot \hat{e}_x = \underline{P} \cdot \hat{e}_x = -\hat{e}_x \]

<|ref|>equation<|/ref|><|det|>[[115, 682, 300, 705]]<|/det|>
\[ \underline{A} \cdot \hat{e}_y = \underline{P} \cdot \hat{e}_y = -\hat{e}_y \]

<|ref|>equation<|/ref|><|det|>[[115, 716, 293, 737]]<|/det|>
\[ \underline{A} \cdot \underline{u} = \underline{P} \cdot \underline{u} = -\underline{u}. \]

<|ref|>text<|/ref|><|det|>[[115, 739, 145, 757]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[115, 759, 666, 800]]<|/det|>
\[ \underline{A} = S_x \cdot S_y = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\cdot \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}=P=S_y \cdot S_x. \]

<|ref|>text<|/ref|><|det|>[[115, 798, 866, 833]]<|/det|>
Die Nacheinanderausführung der Spiegelungen an der x- und y-Achse (unabhängig von der Reihenfolge) ist somit identisch zur Punktspiegelung am Ursprung. 

<|ref|>text<|/ref|><|det|>[[115, 831, 145, 849]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[115, 847, 528, 889]]<|/det|>
\[ \underline{A} = S_x \cdot P_y = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{ bmatrix} \cdot \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & -1 \end{bmatrix}. \]