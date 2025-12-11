<|ref|>text<|/ref|><|det|>[[118, 85, 633, 101]]<|/det|>
Variante 2: Wir wenden das GAUSS-JORDAN-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[140, 106, 759, 199]]<|/det|>
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
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
2 & 0 & -2 \\
0 & 1 & 2
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & 0 & -1 \\
0 & 1 & 2
\end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[118, 206, 440, 222]]<|/det|>
Die Lösungsmenge des LGLS ist demnach 

<|ref|>equation<|/ref|><|det|>[[388, 227, 520, 250]]<|/det|>
\[
\mathbb{L} = \{(-1; 2)\}.
\]

<|ref|>text<|/ref|><|det|>[[115, 254, 144, 271]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[118, 271, 315, 287]]<|/det|>
Wir betrachten das LGLS 

<|ref|>equation<|/ref|><|det|>[[118, 291, 249, 334]]<|/det|>
\[
\begin{cases}
3x - 2y = \frac{5}{6} \\
-\frac{1}{2}x + y = \frac{1}{12}
\end{cases}
\]

<|ref|>text<|/ref|><|det|>[[118, 341, 549, 357]]<|/det|>
Variante 1: Wir wenden das GAUSS-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[140, 362, 700, 406]]<|/det|>
\[
\begin{bmatrix}
3 & -2 & \frac{5}{6} \\
-\frac{1}{2} & 1 & \frac{1}{12}
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -\frac{1}{6} \\
3 & -2 & \frac{5}{6}
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -\frac{6}{8} \\
0 & 4 & \frac{5}{6}
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -\frac{1}{\frac{3}{2}} \\
0 & 1 & \frac{1}{3}
\end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[140, 410, 415, 427]]<|/det|>
Durch Rückwärtseinsetzen finden wir 

<|ref|>equation<|/ref|><|det|>[[238, 431, 417, 465]]<|/det|>
\[
1y = \frac{1}{3} \quad \Rightarrow \quad y = \frac{1}{3}
\]

<|ref|>equation<|/ref|><|det|>[[226, 461, 682, 494]]<|/det|>
\[
x - 2y = -\frac{1}{6} \quad \Rightarrow \quad x = 2y - \frac{1}{6} = 2 \cdot \frac{1}{3} - \frac{1}{6} = \frac{4}{6} - \frac{1}{6} = \frac{2}{6} = \frac{1}{2}.
\]

<|ref|>text<|/ref|><|det|>[[118, 495, 617, 510]]<|/det|>
Variante 2: Wir wenden das GAUSS-JORDAN-Verfahren a. Es gilt 

<|ref|>equation<|/ref|><|det|>[[140, 515, 730, 608]]<|/det|>
\[
\begin{bmatrix}
3 & -2 & \frac{5}{6}\\
-\frac{1}{2} & 1 & \frac{1}{12}
\end{ bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -\frac{1}{6}\\
3 & -2 & \frac{5}{6}
\end{bmatrix}
\Leftrightarrow
\underbrace{
\begin{bmatrix}
1 & -2 & -\frac{1}{6}\\
0 & 4 & \frac{5}{6}
\end{bmatrix}}_{=}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -\frac{1}{6}
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -\left(\frac{1}{2}\right)
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -\frac{1}
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & -2 & -\frac{3}{2}
\end{bmatrix}
.\]

<|ref|>text<|/ref|><|det|>[[118, 611, 465, 627]]<|/det|>
Die Lösungsmenge des LGLS ist demnach 

<|ref|>equation<|/ref|><|det|>[0.5, 0.5, 0.5]{
\underline{L} = \{(\frac{1}{2}; \frac{1}{3})\}.
}

<|ref|>sub_title<|/ref|><|det|>[[115, 682, 444, 699]]<|/det|>
4. Auslastung von Mitarbeitenden 

<|ref|>text<|/ref|><|det|>[[115, 699, 852, 749]]<|/det|>
Ein Produktionsteam besteht aus 2 Mitarbeitenden (MA) mit unterschiedlichen von
einander unabhängigen Aufgaben und stellt 2 Produkte her. Um jeweils eines der
beiden Produkte herzustellen, werden folgende Arbeitseinsätze benötigt: 

<|ref|>table<|/ref|><|det|>[[115, 748, 510, 800]]<|/det|>
<table><tr><td>Arbeitsbedarf</td><td>MA 1</td><td>MA 2</td></tr><tr><td>Produkt A</td><td>18 min</td><td>5 min</td></tr><tr><td>Produkt B</td><td>6 min</td><td>15 min</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 800, 850, 851]]<|/det|>
Wie viele der jeweiligen Produkte müssen täglich jeweils produziert werden, damit
die beiden Mitarbeiter während der gesamten Arbeitszeit von 8 Stunden ganz
ausgelastet sind? 

<|ref|>text<|/ref|><|det|>[[115, 865, 780, 916]]<|/det|>
Wenn täglich a Produkte A und b Produkte b hergestellt werden und beide
Mitarbeiter jeweils 8 h = 8*60 min = 480 min arbeiten, dann muss gelten:
a*18 min + b*6 min = 480 min