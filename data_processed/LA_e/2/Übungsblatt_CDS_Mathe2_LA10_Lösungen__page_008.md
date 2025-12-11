<|ref|>text<|/ref|><|det|>[[119, 82, 875, 119]]<|/det|>
Die zu den Vektoren \(\vec{v}_1\), \(\vec{v}_2\) und \(\vec{v}_3\) gehörenden Eigenwerte sind \(\lambda_1 = 3\), \(\lambda_2 = -1\) und \(\lambda_3 = 2\). 

<|ref|>text<|/ref|><|det|>[[119, 122, 660, 143]]<|/det|>
Für die Matrix \(C = (\vec{v}_1 \vec{v}_2 \vec{v}_3)\) ist \(C^{-1}AC\) eine Diagonalmatrix, 

<|ref|>equation<|/ref|><|det|>[[261, 152, 730, 209]]<|/det|>
\[D = \begin{pmatrix} 3 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2 \end{pmatrix} = C^{-1}AC \text{ mit } C = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & -1 \\ 1 & 0 & 1 \end{pmatrix}.\]

<|ref|>text<|/ref|><|det|>[[119, 210, 560, 229]]<|/det|>
Wir berechnen \(C^{-1}\) mit Hilfe des Gaußverfahrens: 

<|ref|>equation<|/ref|><|det|>[[203, 236, 787, 404]]<|/det|>
\[ (C|E) = \begin{pmatrix} 1 & 2 & 0 & | & 1 & 0 & 0 \\ 0 & 1 & -1 & | & 0 & 1 & 0 \\ 1 & 0 & 1 & | & 0 & 0 & 1 \end{pmatrix} \sim \begin{pmatrix} 1 & 2 & 0 & | & 1 & 1 & 0 \\ 0 & 1 & -1 & | & 0 & 0 & 1 \\ 0 & -2 & 1 & | & -1 & 0 & 1 \end{pmatrix} \\ \sim \begin{pmatrix} 1 & 0 & 2 & | & 1 & -2 & 0 \\ 0 & 1 & -1 & | & 0 & 2 & 1 \\ 0 & 0 & -1 & | & -1 & 2 & 1 \end{pmatrix} \\ \sim \begin{pmatrix} 1 & 0& 0 & | & -1 & 2 & 2 \\ 0 & 1 & 0 & | & 1 & -1 & -1 \\ 0 & 0 & 1 & | & 1 & -2 & -1 \end{pmatrix} = (E|C^{-1}) \]

<|ref|>text<|/ref|><|det|>[[119, 406, 653, 427]]<|/det|>
Nun gilt \(A = CDC^{-1}\) und \(A^n = (CDC^{-1})^n = CD^nC^{-1}\), also 

<|ref|>equation<|/ref|><|det|>[[204, 437, 785, 608]]<|/det|>
\[ \begin{aligned} A^n &= \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} 3^n & 0 & 0 \\ 0 & (-1)^n & 0 \\ 0 & 0 & 2^n \end{pmatrix} \begin{pmatrix} -1 & 2 & 2 \\ 1 & -1 & -1 \\ 1 & -2 & -1 \end{pmatrix} \\ &= \begin{pmatrix} 3^n & 2(-1)^n & 0 \\ 0 & (-1)^n & -2^n \\ 3^n & 0 & 2^n \end{pmatrix} \begin{pmatrix} -1 & 1 & 2 \\ 1 & -1 & -1 \\ 1 & -2 & 1 \end{pmatrix} \\ &= \begin{pmatrix} -3^n + 2(-1)^n & 2 \cdot 3^n + 2 \cdot (-1)^{n+1} & 2 \cdot 3^n + 2 \cdot (-1)^{n+1}\\ (-1)^n - 2^n & (-1)^{n+1} + 2^{n+1} & (-1)^{n+1} + 2^n \\ -3^n + 2^n & 2 \cdot 3^n - 2^{n+1} & 2 \cdot 3^n - 2^n \end{pmatrix}. \end{aligned} \]