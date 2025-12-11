<|ref|>sub_title<|/ref|><|det|>[[114, 80, 725, 100]]<|/det|>
3. Eindeutig lösbare lineare Gleichungssysteme für 2 Variablen 

<|ref|>text<|/ref|><|det|>[[114, 99, 848, 134]]<|/det|>
Bringen Sie die linearen Gleichungssysteme in ein Gauß-Schema und bestimmen Sie die Lösung mit Hilfe des Gauß- oder Gauß-Jordan-Verfahrens. 

<|ref|>equation<|/ref|><|det|>[[114, 133, 810, 168]]<|/det|>
\[
\begin{align*}
\text{a)} & \quad 2x - y = 1 \quad \text{b)} \quad 5x + 3y = 1 \quad \text{c)} \quad 3x - 2y = 5/6 \\
& \quad 2y - x = 7 \quad \text{2x + y = 0} \quad \text{-1/2x + y = 1/12}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 182, 147, 199]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[122, 202, 600, 220]]<|/det|>
Variante 1: Wir wenden das GAUSS-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[147, 228, 744, 275]]<|/det|>
\[
\begin{bmatrix}
2 & -1 & 1 \\
-1 & 2 & 7
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
-1 & 2 & 7 \\
2 & -1 & 1
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -7 \\
2 & -1 & 1
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix} 1 & -2 & -7 \\ 0 & 3 & 15 \end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[144, 284, 453, 301]]<|/det|>
Durch Rückwärtseinsetzen finden wir 

<|ref|>equation<|/ref|><|det|>[[280, 308, 721, 365]]<|/det|>
\[
\begin{align*}
3y &= 15 \quad \Rightarrow \quad y = \frac{15}{3} = 5 \\
x - 2y &= -7 \quad \Rightarrow \quad x = 2y - 7 = 2 \cdot 5 - 7 = 10 - 7 = 3.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[122, 373, 675, 391]]<|/det|>
Variante 2: Wir wenden das GAUSS-JORDAN-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[147, 399, 736, 500]]<|/det|>
\[
\begin{bmatrix}
2 & -1 & 1 \\
-1 & -2 & 7
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
-1 & 1 & 7 \\
2 & -1 & 1
\end{bmatrix}
\Leftrightarrow
\boxed{
\begin{bmatrix}
1 & -2 & -7 \\
0 & 3 & 15
\end{bmatrix}
}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -7 \\
0 & 3 & 15
\boxed{
\begin{bmatrix}
1 & -2 & -7 \\
0 & 1 & 5
\end{bmatrix}
}
.\]

<|ref|>text<|/ref|><|det|>[[122, 511, 468, 529]]<|/det|>
Die Lösungsmenge des LGLS ist demnach 

<|ref|>equation<|/ref|><|det|>[[420, 538, 546, 563]]<|/det|>
\[
\underline{L} = \{\{3; 5\}\}.
\]

<|ref|>text<|/ref|><|det|>[[114, 568, 147, 585]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[122, 588, 323, 604]]<|/det|>
Wir betrachten das LGLS 

<|ref|>equation<|/ref|><|det|>[[122, 610, 240, 650]]<|/det|>
\[
\begin{cases}
5x + 3y = 1 \\
2x + y = 0.
\end{cases}
\]

<|ref|>text<|/ref|><|det|>[[114, 660, 565, 676]]<|/det|>
Variante 1: Wir wenden das GAUSS-Verfahren an. Es gitt 

<|ref|>equation<|/ref|><|det|>[[139, 682, 610, 727]]<|/det|>
\[
\begin{bmatrix}
5 & 3 & 1 \\
2 & 1 & 0
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
2 & 1 & 0 \\
5 & 3 & 1
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
2 & 1 & 0 \\
0 & \frac{1}{2} & 1
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
2 & 1 & \frac{1}{2} \\
0 & 1 & 2
\end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[144, 732, 428, 748]]<|/det|>
Durch Rückwärtseinsetzen finden wir 

<|ref|>equation<|/ref|><|det|>[[348, 752, 500, 769]]<|/det|>
\[
1y = 2 \Rightarrow y = 2
\]

<|ref|>equation<|/ref|><|det|>[[320, 773, 611, 802]]<|/det|>
\[
2x + y = 0 \Rightarrow x = -\frac{y}{2} = -\frac{2}{2} = -1.
\]