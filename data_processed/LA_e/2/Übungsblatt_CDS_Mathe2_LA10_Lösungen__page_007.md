<|ref|>text<|/ref|><|det|>[[117, 83, 864, 127]]<|/det|>
Die Koeffizientenmatrizen der zugehörigen homogenen Gleichungssysteme \((A_3 - \lambda_{1,2}E)x = 0\) bzw. \((A_3 - \lambda_3E)x = 0\) liefern folgende Eigenräume: 

<|ref|>equation<|/ref|><|det|>[[243, 141, 737, 205]]<|/det|>
\[ \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix} \implies \mathbb{L}_{1,2} = \text{Span} \left\{ \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \right\}, \]

<|ref|>text<|/ref|><|det|>[[117, 221, 405, 243]]<|/det|>
also sind auch \(\dim \mathbb{L}_{1,2} = 2\), bzw. 

<|ref|>equation<|/ref|><|det|>[[285, 258, 696, 323]]<|/det|>
\[ \begin{pmatrix} -1 & 1 & 1 \\ 1 & -1 & 1 \\ 0 & 0 & -2 \end{pmatrix} \implies \mathbb{L}_3 = \text{Span} \left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \right\}, \]

<|ref|>text<|/ref|><|det|>[[117, 340, 260, 361]]<|/det|>
und \(\dim \mathbb{L}_3 = 1\). 

<|ref|>text<|/ref|><|det|>[[117, 359, 150, 376]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[117, 372, 864, 433]]<|/det|>
Die Matrizen \(A_2\) und \(A_3\) sind ähnlich zu einer Diagonalmatrix, da bei diesen jeweils die algebraischen und geometrischen Vielfachheiten übereinstimmen. Dagegen ist \(A_1\) nicht diagonalisierbar. 

<|ref|>sub_title<|/ref|><|det|>[[117, 445, 291, 464]]<|/det|>
## 6. Diagonalmatrix 

<|ref|>text<|/ref|><|det|>[[117, 460, 860, 590]]<|/det|>
Überprüfen Sie, dass \(\vec{v}_1 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}\), \(\vec{v}_2 = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}\) und \(\vec{v}_3 = \begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix}\) Eigenvektoren der Matrix
\[ A = \begin{pmatrix} -5 & 8 & 8 \\ -3 & 5 & 3 \\ -1 & 3 & 4 \end{pmatrix} \] sind und bestimmen Sie die dazugehörigen Eigenwerte. Finden Sie eine Matrix \(C\), so dass \(C^{-1}AC\) eine Diagonalmatrix ist und berechnen Sie \(A^n\) für alle \(n \in \mathbb{N}\). 

<|ref|>text<|/ref|><|det|>[[117, 605, 183, 625]]<|/det|>
Es gilt 

<|ref|>equation<|/ref|><|det|>[[221, 634, 610, 808]]<|/det|>
\[ \begin{aligned} A\vec{v}_1 &= \begin{pmatrix} -5 & 8 & 8 \\ -3 & 5 & -3 \\ -1 & 2 & 4 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ 3 \end{pmatrix} = 3\vec{v}_1 \\ A\vec{v}_2 &= \begin{pmatrix} -5 & 8 & 8 \\ -3 & 5 \\ -1 & 2 & 4 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} -2 \\ -1 \\ 0 \end{pmatrix} = -\vec{v}_2 \\ A\vec{v}_3 &= \begin{pmatrix} -5 & 8 & 8 \\ -3 & 5 \end{pmatrix} \begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -2 \\ 2 \end{pmatrix} = 2\vec{v}_3. \end{aligned} \]