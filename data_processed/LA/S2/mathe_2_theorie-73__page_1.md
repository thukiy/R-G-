<|ref|>sub_title<|/ref|><|det|>[[25, 15, 470, 58]]<|/det|>
# Matrizen und LGS 

<|ref|>equation<|/ref|><|det|>[[55, 90, 327, 117]]<|/det|>
\[5x_1 + 3x_2 - x_3 = 4\]

<|ref|>equation<|/ref|><|det|>[[55, 128, 355, 156]]<|/det|>
\[2x_1 + 7x_2 + 2x_3 = -3\]

<|ref|>equation<|/ref|><|det|>[[55, 168, 351, 195]]<|/det|>
\[-x_1 + 4x_2 + 3x_3 = 1\]

<|ref|>text<|/ref|><|det|>[[45, 207, 720, 234]]<|/det|>
→ können wir mit Matrixmultiplikation ausdrücken 

<|ref|>equation<|/ref|><|det|>[[100, 243, 512, 350]]<|/det|>
\[\begin{pmatrix} 5 & 3 & -1 \\ 2 & 7 & 2 \\ -1 & 4 & 3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 4 \\ -3 \\ 1 \end{pmatrix}\]

<|ref|>text<|/ref|><|det|>[[95, 360, 375, 389]]<|/det|>
allgemein: \(A \cdot \vec{x} = \vec{b}\) 

<|ref|>text<|/ref|><|det|>[[575, 325, 653, 346]]<|/det|>
Matrix 

<|ref|>sub_title<|/ref|><|det|>[[20, 422, 212, 447]]<|/det|>
## Inverse Matrix 

<|ref|>text<|/ref|><|det|>[[50, 460, 770, 490]]<|/det|>
für reelle Zahlen kann folgende Gleichung gelöst werden: 

<|ref|>equation<|/ref|><|det|>[[110, 499, 510, 563]]<|/det|>
\[a \cdot x = b \quad | \cdot a^{-1} \quad a \neq 0\]

<|ref|>equation<|/ref|><|det|>[[160, 533, 840, 562]]<|/det|>
\[x = a^{-1} \cdot b \quad \text{für } a = 0 \text{ muss auch } b = 0 \text{ sein}\]

<|ref|>text<|/ref|><|det|>[[20, 597, 843, 625]]<|/det|>
→ auf Matrizen angewandt (Matrix muss quadratisch sein, also 

<|ref|>equation<|/ref|><|det|>[[80, 636, 255, 660]]<|/det|>
\[n \times n \text{ Matrix})\]

<|ref|>equation<|/ref|><|det|>[[100, 671, 365, 700]]<|/det|>
\[A \cdot \vec{x} = \vec{b} \quad | \cdot A^{-1} \]

<|ref|>equation<|/ref|><|det|>[[95, 711, 350, 760]]<|/det|>
\[A^{-1} \cdot A \cdot \vec{x} = A^{-1} \cdot \vec{b}\]

<|ref|>equation<|/ref|><|det|>[[95, 772, 295, 797]]<|/det|>
\[\rightarrow A^{-1} \cdot A = 11\]

<|ref|>text<|/ref|><|det|>[[152, 813, 760, 840]]<|/det|>
Voraussetzung, dass Matrix A invertierbar ist: 

<|ref|>equation<|/ref|><|det|>[[160, 852, 685, 878]]<|/det|>
\[A \text{ muss vollen Rang haben, } d.h. n_R = n\]

<|ref|>text<|/ref|><|det|>[[168, 890, 504, 916]]<|/det|>
→ A heisst dann regulär 

<|ref|>text<|/ref|><|det|>[[168, 928, 890, 953]]<|/det|>
→ A heisst singulär, wenn \(n_R < n\) und \(A\) ist dann nicht 

<|ref|>text<|/ref|><|det|>[[230, 966, 375, 990]]<|/det|>
inveiterbar