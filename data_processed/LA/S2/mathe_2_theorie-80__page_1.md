<|ref|>sub_title<|/ref|><|det|>[[20, 10, 285, 39]]<|/det|>
Orthogonale Matrix 

<|ref|>text<|/ref|><|det|>[[20, 49, 950, 81]]<|/det|>
Def: eine quadratische \(n \times n\) Matrix heisst orthogonal, wenn gilt: 

<|ref|>equation<|/ref|><|det|>[[110, 87, 240, 116]]<|/det|>
\[A^{-1} = A^T\]

<|ref|>equation<|/ref|><|det|>[[40, 147, 400, 177]]<|/det|>
\[\rightarrow A \cdot A^{-1} = \mathbb{1} = A \cdot A^T\]

<|ref|>equation<|/ref|><|det|>[[40, 186, 750, 216]]<|/det|>
\[\rightarrow \text{für } A \text{ orthogonal und symmetrisch } A^{-1} = A^T = A\]

<|ref|>equation<|/ref|><|det|>[[125, 222, 480, 252]]<|/det|>
\[\rightarrow A^2 = A \cdot A = A \cdot A^{-1} = \mathbb{1}\]

<|ref|>equation<|/ref|><|det|>[[40, 263, 833, 294]]<|/det|>
\[\rightarrow \text{für } A \text{ orthogonal und schiefsymmetricch } A^{-1} = A^T = -A\]

<|ref|>equation<|/ref|><|det|>[[125, 300, 960, 330]]<|/det|>
\[\rightarrow A^2 = A \cdot A = -A^{-1} \cdot A = -\mathbb{1} \quad (\text{verhält sich wie imaginäre Einheit})\]

<|ref|>equation<|/ref|><|det|>[[40, 343, 645, 373]]<|/det|>
\[\rightarrow \text{dosen eines LGS, wenn } A \text{ orthogonal ist:}\]

<|ref|>equation<|/ref|><|det|>[[103, 378, 360, 490]]<|/det|>
\[A \cdot \vec{x} = \vec{b} \quad | \cdot A^T\]

<|ref|>equation<|/ref|><|det|>[[103, 496, 350, 480]]<|/det|>
\[A^T \cdot A \cdot \vec{x} = A^T \cdot \vec{b}\]

<|ref|>equation<|/ref|><|det|>[[185, 456, 350, 488]]<|/det|>
\[\vec{x} = A^T \cdot \vec{b}\]

<|ref|>sub_title<|/ref|><|det|>[[20, 519, 457, 546]]<|/det|>
Bsp: für orthogonale Matrixen 

<|ref|>equation<|/ref|><|det|>[[143, 552, 490, 600]]<|/det|>
\[\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \frac{1}{\sqrt{10}} \cdot \begin{pmatrix} 1 & -3 \\ 3 & 1 \end{pmatrix}\]

<|ref|>equation<|/ref|><|det|>[[46, 625, 360, 666]]<|/det|>
\[\mathbb{1} = A \cdot A^{-1} = A \cdot A^T\]

<|ref|>equation<|/ref|><|det|>[[46, 667, 360, 710]]<|/det|>
\[A = \begin{bmatrix} \vec{a}_1 & \vec{a}_2 & \dots & \vec{a}_n \end{bmatrix}\]

<|ref|>equation<|/ref|><|det|>[[431, 621, 610, 720]]<|/det|>
\[\begin{pmatrix} \vec{a}_1^T \\ \vec{a}_2^T \\ \vdots \\ \vec{a}_n^T \end{pmatrix}\]

<|ref|>equation<|/ref|><|det|>[[46, 743, 920, 835]]<|/det|>
\[A^T \cdot A = \begin{pmatrix} \vec{a}_1^T \\ \vec{a}_2^T \\vdots \\ \vec{a}_n^T \end{pmatrix} \cdot (\vec{a}_1 \vec{a}_2 \dots \vec{a}_n) = \begin{pmatrix} \vec{a}_1^T \vec{a}_1 & \vec{a}_1^T \vec{a}_2 & \dots & \vec{a}_1^T \vec{a}_n \\ \vec{a}_2^T \vec{a}_1 & \vec{a}_2^T \vec{a}_2 & \dots & \vec{a}_2^T \vec{a}_n \\ \vdots & \vdots & \ddots & \vdots \\ \vec{a}_n^T \vec{a}_1 & \vec{a}_n^T \vec{a}_2 & \dots & \vec{a}_n^T \vec{a}_n \end{pmatrix}\]

<|ref|>equation<|/ref|><|det|>[[143, 860, 830, 955]]<|/det|>
\[= \begin{pmatrix} \langle \vec{a}_1, \vec{a}_1^T \rangle & \langle \vec{a}_1, \vec{a}_2 \rangle & \dots & \langle \vec{a}_1, \vec{a}_n \rangle \\ \langle \vec{a}_2, \vec{a}_1^T \rangle & \langle \vec{a}_2, \vec{a}_2 \rangle & \dots & \langle \vec{a}_2, \vec{a}_n \rangle \\ \vdots & \vdots & \ddots & \vdots \\ \langle \vec{a}_n, \vec{a}_1^T \rangle & \langle \vec{a}_n, \vec{a}_2 \rangle & \dots & \langle \vec{a}_n, \vec{a}_n \rangle \end{pmatrix} = \mathbb{1}\]