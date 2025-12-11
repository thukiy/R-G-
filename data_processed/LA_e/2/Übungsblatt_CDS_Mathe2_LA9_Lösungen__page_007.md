<|ref|>text<|/ref|><|det|>[[117, 85, 315, 105]]<|/det|>
Matrizenschreibweise: 

<|ref|>equation<|/ref|><|det|>[[187, 112, 414, 385]]<|/det|>
\[
\begin{pmatrix}
2 & 1 & 0 \\
0 & 1 & -1 \\
1 & 0 & a
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0 & 1 \\
2 & 1
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0 & 1 & -1 \\
0 & 1 & -2a
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0 & 1
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0 & 1 - 2a
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0 & -1
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0 & 0
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0 & 0 & 1 - 2a
\end{pmatrix}
\mapsto
\begin{pmatrix}
0
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0 & 2a
\end{pmatrix}
\mapsto
\begin{pmatrix}
0 & 0 \\
0
\end{pmatrix} 
\]

<|ref|>text<|/ref|><|det|>[[117, 392, 510, 412]]<|/det|>
Das LGS ist also dann nur trivial lösbar, wenn 

<|ref|>equation<|/ref|><|det|>[[183, 423, 295, 485]]<|/det|>
\[
\begin{align*}
1 - 2a \neq 0 \\
a \neq \frac{1}{2}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[117, 494, 590, 516]]<|/det|>
Also bilden die 3 Vektoren für \(a \neq \frac{1}{2}\) eine Basis des \(\mathbb{R}^3\). 

<|ref|>text<|/ref|><|det|>[[117, 520, 150, 538]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[117, 536, 424, 555]]<|/det|>
Linearkombination des Nullvektors: 

<|ref|>equation<|/ref|><|det|>[[179, 562, 625, 622]]<|/det|>
\[
\lambda_1 \begin{pmatrix} 6 \\ a \\ 7 \end{pmatrix} + \lambda_2 \begin{pmatrix} -a \\ -1 \\ 2 \end{pmatrix} + \lambda_3 \begin{pmatrix} 3 \\ a \\ 4 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[117, 631, 255, 650]]<|/det|>
In Koordinaten: 

<|ref|>equation<|/ref|><|det|>[[191, 659, 390, 714]]<|/det|>
\[
\begin{align*}
6\lambda_1 - a\lambda_2 + 3\lambda_3 &= 0 \\
a\lambda_1 - \lambda_2 + a\lambda_3 &= 0 \\
7\lambda_1 + 2\lambda_2 + 4\lambda_3 &= 0
\end{align*}
\]