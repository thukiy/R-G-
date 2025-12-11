<|ref|>text<|/ref|><|det|>[[117, 80, 833, 113]]<|/det|>
in einem Gauss-Schema und bringen dieses mit Hilfe des Gauss-Verfahrens auf Stufenform. Es gilt 

<|ref|>equation<|/ref|><|det|>[[117, 118, 264, 181]]<|/det|>
\[
\begin{bmatrix}
1 & 1 & 1 & 0 \\
0 & [1] & 1 & 1 \\
0 & 0 & [1] & 0
\end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[117, 185, 430, 202]]<|/det|>
Das LGLS hat offensichtlich den Rang 

<|ref|>equation<|/ref|><|det|>[[383, 215, 561, 231]]<|/det|>
\[
n_{\text{R}} = 3 = n < 4 = m.
\]

<|ref|>text<|/ref|><|det|>[[117, 243, 810, 260]]<|/det|>
Demnach ist M linear abhängig sowie erzeugend und bildet folglich keine Basis von V. 

<|ref|>text<|/ref|><|det|>[[117, 262, 150, 280]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[117, 278, 360, 293]]<|/det|>
Wir betrachten die Teilmenge 

<|ref|>equation<|/ref|><|det|>[[244, 303, 700, 380]]<|/det|>
\[
M = \{v_1, v_2, v_3\} = \begin{Bmatrix} 1 \\ 2 \\ 3 \\ 4 \end{Bmatrix}, \begin{Bmatrix} 5 \\ 6 \\ 7 \\ 8 \end{Bmatrix}, \begin{Bmatrix} 2 \\ 4 \\ 6 \\ 8 \end{Bmatrix} \subset V = \mathbb{R}^4
\]

<|ref|>text<|/ref|><|det|>[[117, 389, 571, 405]]<|/det|>
aus \(m = 3\) Vektoren. Wir schreiben das homogene LGLS 

<|ref|>equation<|/ref|><|det|>[[200, 415, 744, 492]]<|/det|>
\[
0 = x_1 \cdot v_1 + x_2 \cdot v_2 + x_3 \cdot v_3 = x_1 \cdot \begin{bmatrix} 1 \\ 2 \\ 3 \\ 4 \end{bmatrix} + x_2 \cdot \begin{bmatrix} 5 \\ 6 \\ 7 \\ 8 \end{bmatrix} + x_3 \cdot \begin{bmatrix} 2 \\ 4 \\ 6 \\ 8 \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[117, 492, 833, 524]]<|/det|>
in einem Gauss-Schema und bringen dieses mit Hilfe des Gauss-Verfahrens auf Stei- form. Es gilt 

<|ref|>equation<|/ref|><|det|>[[120, 535, 680, 660]]<|/det|>
\[
\begin{bmatrix}
1 & 5 & 2 \\
2 & 6 & 4 \\
3 & 7 & 6 \\
4 & 8 & 8
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & 5 & 2 \\
0 & -4 & 0 \\
0 & -8 & 0 \\
0 & -12 & 0
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & 5 & 2 \\
1 & 0 & 0 \\
1 & 0 & 1 \\
1 & 0 & 0
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & 5 &2 \\
0 & [1] & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[120, 670, 430, 707]]<|/det|>
\[
\Leftrightarrow
\begin{bmatrix}
1 & 5 & 2 \\
0 & [1] & 0 \\
0 & 0 & 0
\end{bmatrix}
.\]

<|ref|>text<|/ref|><|det|>[[117, 726, 833, 780]]<|/det|>
Demnach ist M linear abhängig sowie nicht erzeugend und bildet folglich keine Basis von V. 

<|ref|>text<|/ref|><|det|>[[0, 0, 0, 0]]<|/det|>
f) 

<|ref|>text<|/ref|><|det|>[[117, 780, 360, 797]]<|/det|>
Wir betrachten die Teilmenge 

<|ref|>equation<|/ref|><|det|>[[202, 810, 744, 895]]<|/det|>
\[
M = \{v_1, v_2, v_3, v_4\} = \begin{Bmatrix} 1 \\ 0 \\ 1 \\ 0 \end{Bmatrix}, \begin{Bmatrix} 1 \\ 1 \\ 0 \\ 0 \end{Bmatrix}, \begin{Bmatrix} 0 \\ 1 \\ 0 \\ 1 \end{Bmatrix} \subset V = \mathbb{R}^4
\]