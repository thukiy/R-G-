<|ref|>text<|/ref|><|det|>[[18, 10, 800, 40]]<|/det|>
→ ist A invertierbar und \(A^{-1}\) die Inverse zu A, dann gilt: 

<|ref|>equation<|/ref|><|det|>[[112, 51, 400, 78]]<|/det|>
\[A \cdot A^{-1} = \mathbb{1} = A^{-1} \cdot A\]

<|ref|>sub_title<|/ref|><|det|>[[20, 110, 206, 137]]<|/det|>
Eigenschaften: 

<|ref|>equation<|/ref|><|det|>[[40, 147, 222, 175]]<|/det|>
\[(A^{-1})^{-1} = A\]

<|ref|>equation<|/ref|><|det|>[[40, 188, 821, 214]]<|/det|>
\[\text{• A und B seien invertierbar, dann gilt: } (A \cdot B)^{-1} = B^{-1} \cdot A^{-1}\]

<|ref|>equation<|/ref|><|det|>[[40, 226, 193, 252]]<|/det|>
\[\mathbb{1} \cdot \mathbb{1}^{-1} = \mathbb{1}\]

<|ref|>equation<|/ref|><|det|>[[40, 263, 288, 291]]<|/det|>
\[\text{• } (A^{-1})^{\text{T}} = (A^{\text{T}})^{-1}\]

<|ref|>sub_title<|/ref|><|det|>[[20, 325, 425, 351]]<|/det|>
Bestimmung der inversen Matrix 

<|ref|>equation<|/ref|><|det|>[[40, 361, 644, 395]]<|/det|>
\[A \cdot A^{-1} = \mathbb{1} \quad \text{mit } A^{-1} (\vec{s}_1 \cdot \vec{s}_n)\]

<|ref|>equation<|/ref|><|det|>[[40, 396, 300, 440]]<|/det|>
\[A \cdot \vec{s}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \hat{e}_1\]

<|ref|>equation<|/ref|><|det|>[[40, 440, 300, 494]]<|/det|>
\[A \cdot \vec{s}_n = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \hat{e}_n\]

<|ref|>text<|/ref|><|det|>[[18, 518, 777, 586]]<|/det|>
→ die \(\vec{s}_n\) sind zu bestimmen, d.h. wir haben \(n\) lineare Gleichungssysteme zu lösen 

<|ref|>text<|/ref|><|det|>[[18, 598, 951, 627]]<|/det|>
→ wir lösen die \(n\) LGS gleichzeitig mit dem Gauss-Jordan-Verfahren 

<|ref|>equation<|/ref|><|det|>[[80, 656, 320, 682]]<|/det|>
\[A \mid \mathbb{1} = \mathbb{1} \mid A^{-1}\]

<|ref|>text<|/ref|><|det|>[[88, 695, 951, 763]]<|/det|>
→ A wird auf Diagonalform mit Gauss-Jordan gebracht mit nun "1" als Einhängen in Hauptdiagonale