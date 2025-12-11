<|ref|>text<|/ref|><|det|>[[115, 86, 572, 103]]<|/det|>
aus \(m = 4\) Vektoren. Wir schreiben das homogene LGLS 

<|ref|>equation<|/ref|><|det|>[[257, 115, 690, 207]]<|/det|>
\[
\begin{align*}
0 &= x_1 \cdot \mathbf{v}_1 + x_2 \cdot \mathbf{v}_2 + x_3 \cdot \mathbf{v}_3 + x_4 \cdot \mathbf{v}_4 \\
&= x_1 \cdot \begin{bmatrix} 1 \\ 0 \\ 1 \\ 0 \end{bmatrix} + x_2 \cdot \begin{bmatrix} 1 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_3 \cdot \begin{bmatrix} 0 \\ 1 \\ 0 \\ 1 \end{bmatrix} + x_4 \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \\ 1 \end{bmatrix}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 214, 833, 249]]<|/det|>
in einem Gauss-Schema und bringen dieses mit Hilfe des Gauss-Verfahrens auf Stufenform. Es gilt 

<|ref|>equation<|/ref|><|det|>[[120, 257, 825, 410]]<|/det|>
\[
\begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \right] \Leftrightarrow \begin{bmatrix} 1 & 1 & 0 & 0 \\0 & 1 & 1 & 0 \\0 & 0 & 1 & 1 \\1 & 0 & 0 & 1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 0 & 0 \\ 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 1 & 0 \\0 & 1 & 1 \\0 & 0 & 0 \\0 & 0 & 0 \end{bmatrix}
\end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 418, 432, 436]]<|/det|>
Das LGLS hat offensichtlich den Rang 

<|ref|>equation<|/ref|><|det|>[[383, 447, 563, 464]]<|/det|>
\[
n_R = 3 < 4 = m = n.
\]

<|ref|>text<|/ref|><|det|>[[115, 473, 832, 511]]<|/det|>
Demnach ist M linear abhängig sowie nicht erzeugend und bildet folglich keine Basis von V. 

<|ref|>sub_title<|/ref|><|det|>[[115, 526, 200, 543]]<|/det|>
4. Basis 

<|ref|>text<|/ref|><|det|>[[115, 543, 780, 561]]<|/det|>
Für welche Werte von a bilden die folgenden Vektoren eine Basis des \(\mathbb{R}^3\)? 

<|ref|>equation<|/ref|><|det|>[[115, 559, 567, 610]]<|/det|>
\[
\text{a)} \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ -1 \\ a \end{pmatrix} \quad \text{b)} \begin{pmatrix} 6 \\ a \\ 7 \end{pmatrix}, \begin{pmatrix} -a \\ -1 \\ 2 \end{pmatrix}, \begin{pmatrix} 3 \\ a \\ 4 \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 622, 856, 659]]<|/det|>
Anzahl der Basisvektoren im \(\mathbb{R}^3\) ist 3, d. h. es muss die lineare Unabhängigkeit der
gegebenen Vektoren überprüft werden. 

<|ref|>text<|/ref|><|det|>[[115, 657, 147, 675]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 674, 427, 692]]<|/det|>
Linearkombination des Nullvektors: 

<|ref|>equation<|/ref|><|det|>[[182, 700, 625, 760]]<|/det|>
\[
\lambda_1 \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix} + \lambda_2 \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + \lambda_3 \begin{pmatrix} 0 \\ -1 \\ a \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 770, 258, 788]]<|/det|>
In Koordinaten: 

<|ref|>equation<|/ref|><|det|>[[192, 797, 384, 853]]<|/det|>
\[
\begin{align*}
2\lambda_1 + \lambda_2 &= 0 \\
+ \lambda_2 - \lambda_3 &= 0 \\
\lambda_1 + a\lambda_3 &= 0
\end{align*}
\]