<|ref|>text<|/ref|><|det|>[[20, 18, 60, 42]]<|/det|>
10) 

<|ref|>equation<|/ref|><|det|>[[92, 15, 333, 80]]<|/det|>
\[A = \begin{pmatrix} 2 & 1 & -2 \\ -6 & -5 & 8 \\ -2 & -2 & 3 \end{pmatrix}\]

<|ref|>equation<|/ref|><|det|>[[415, 31, 590, 80]]<|/det|>
\[A = B^{-1} \cdot D \cdot B\]

<|ref|>text<|/ref|><|det|>[[550, 55, 797, 75]]<|/det|>
Transformationsmatrix 

<|ref|>text<|/ref|><|det|>[[476, 75, 610, 96]]<|/det|>
Diagonalmatrix 

<|ref|>text<|/ref|><|det|>[[90, 112, 230, 137]]<|/det|>
Eigenwerke: 

<|ref|>equation<|/ref|><|det|>[[280, 110, 710, 160]]<|/det|>
\[\text{det}(A - \lambda I) = \text{det} \begin{pmatrix} 2 - \lambda & 1 & -2 \\ -6 & -5 - \lambda & 8 \\ -2 & -2 & 3 - \lambda \end{pmatrix}\]

<|ref|>equation<|/ref|><|det|>[[90, 186, 655, 210]]<|/det|>
\[= (2 - \lambda)(-5 - \lambda)(3 - \lambda) - 16 - 24 - 4(-5 - \lambda) + 16(2 - \lambda) + 6(3 - \lambda)\]

<|ref|>equation<|/ref|><|det|>[[90, 220, 655, 250]]<|/det|>
\[= (-10 - 2\lambda + 5\lambda + \lambda^2)(3 - \lambda) - 40 + 20 + 4\lambda + 32 - 16\lambda + 18 - 6\lambda\]

<|ref|>equation<|/ref|><|det|>[[90, 263, 515, 287]]<|/det|>
\[= -30 + 10\lambda + 9\lambda - 3\lambda^2 + 3\lambda^2 - \lambda^3 + 30 - 18\lambda\]

<|ref|>equation<|/ref|><|det|>[[90, 300, 384, 325]]<|/det|>
\[= \lambda - \lambda^3 = \lambda(1 - \lambda^2) \stackrel{!}{=} 0\]

<|ref|>equation<|/ref|><|det|>[[80, 341, 600, 366]]<|/det|>
\[\lambda_1 = 0 \quad 1 - \lambda^2 = 0 \quad \iff \quad \lambda_2 = 1 \quad \lambda_3 = -1\]

<|ref|>text<|/ref|><|det|>[[80, 380, 707, 405]]<|/det|>
→ A kann diagonalisiert werden (weil 3 Eigenwerke) 

<|ref|>equation<|/ref|><|det|>[[80, 415, 330, 479]]<|/det|>
\[D = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{pmatrix}\]

<|ref|>text<|/ref|><|det|>[[80, 494, 840, 520]]<|/det|>
für Transformationsmatrix B müssen die Eigenvektoren zu den 

<|ref|>text<|/ref|><|det|>[[80, 532, 450, 555]]<|/det|>
Eigenweiten bestimmt werden: 

<|ref|>text<|/ref|><|det|>[[140, 568, 508, 593]]<|/det|>
Eigenvektoren = Spalten von B 

<|ref|>text<|/ref|><|det|>[[90, 628, 384, 652]]<|/det|>
Eigenvektor zu \(\lambda_1 = 0\): 

<|ref|>equation<|/ref|><|det|>[[120, 660, 420, 725]]<|/det|>
\[\begin{pmatrix} 2 & 1 & -2 \\ -6 & -5 & 1 \\ -2 & -2 & 3 \end{pmatrix} \cdot \vec{E}_1 = 0\]

<|ref|>equation<|/ref|><|det|>[[120, 737, 861, 802]]<|/det|>
\[\begin{pmatrix} 2 & 1 & -2 \\ -6 & 5 & 8 \\ -2 & -2 & 3 \end{pmatrix} \cdot \vec{E}_2 = 0\]

<|ref|>equation<|/ref|><|det|>[[120, 835, 688, 860]]<|/det|>
\[-2y + 2z = 0 \quad \iff \quad y = 2 \quad \text{wähle } z = t\]

<|ref|>equation<|/ref|><|det|>[[120, 870, 620, 900]]<|/det|>
\[2x + y - 2z = 0 \quad \iff \quad x = -\frac{1}{2}y + z = \frac{1}{2}z\]

<|ref|>equation<|/ref|><|det|>[[120, 910, 300, 970]]<|/det|>
\[\vec{E}_1 = t \cdot \begin{pmatrix} \frac{1}{2} \\ 1 \\ 1 \end{pmatrix}\]